from __future__ import annotations

import json
import re
from pathlib import Path

import litellm

from .config import WikiConfig
from .schema import PageType, WikiPage, extract_wikilinks, find_page_by_title, _slugify
from .search import bm25_search, invalidate_cache
from .utils import (
    append_to_log,
    extract_clean_content,
    is_source_ingested,
    mark_source_ingested,
    move_to_ingested,
    parse_source_metadata,
    truncate_to_tokens,
    update_index,
)


ANALYSIS_PROMPT = """You are a knowledge base analyst. Analyze the following source document and identify:
1. Key entities (people, organizations, products, etc.)
2. Key concepts (ideas, theories, methods, etc.)
3. Main arguments and findings
4. Connections to existing wiki content (listed below)
5. Contradictions with existing knowledge

Source document:
{source_content}

Existing wiki index:
{wiki_index}

Related wiki pages:
{related_pages}

Respond in JSON format:
{{
  "title": "short descriptive title for the source",
  "summary": "2-3 sentence summary",
  "entities": [{{"name": "...", "description": "..."}}],
  "concepts": [{{"name": "...", "description": "..."}}],
  "connections": ["connection to existing page 1", ...],
  "contradictions": ["contradiction 1", ...],
  "tags": ["tag1", "tag2", ...]
}}"""

GENERATION_PROMPT_TEMPLATE = """You are a knowledge base writer. Based on the analysis below, generate wiki pages in JSON format.

Analysis:
{analysis}

Existing wiki pages that should be updated:
{existing_pages}

Generate the following as JSON:
{{
  "source_page": {{
    "title": "...",
    "content": "markdown content for the source summary page",
    "tags": ["..."],
    "related": ["EntityOrConceptName1", ...]
  }},
  "concept_pages": [
    {{
      "title": "...",
      "content": "markdown content explaining this concept",
      "tags": ["..."],
      "related": ["OtherConcept", "EntityName"]
    }}
  ],
  "entity_pages": [
    {{
      "title": "...",
      "content": "markdown content describing this entity",
      "tags": ["..."],
      "related": ["ConceptName", "OtherEntity"]
    }}
  ],
  "index_updates": [
    {{"title": "...", "type": "concept|entity|source", "summary": "one-line summary"}}
  ]
}}

Rules:
- Use [[PageTitle]] syntax for cross-references
- Each page should be self-contained but link to related pages
- Content should be informative, not just a stub
- Include source attribution where appropriate
- Tags should be lowercase with hyphens
{language_instruction}"""


def _get_language_instruction(language: str) -> str:
    """Get language instruction based on config setting."""
    if language == "cn":
        return "- Write all content in Chinese (中文)"
    elif language == "en":
        return "- Write all content in English"
    else:  # as_origin
        return "- Write content in the same language as the source document"


def _call_llm(config: WikiConfig, prompt: str, retries: int = 3) -> str:
    last_error = None
    for attempt in range(retries):
        try:
            response = litellm.completion(
                model=config.llm.model,
                messages=[{"role": "user", "content": prompt}],
                api_key=config.llm.api_key or None,
                api_base=config.llm.base_url,
                temperature=config.llm.temperature,
                max_tokens=config.llm.max_tokens,
                timeout=120,
            )
            return response.choices[0].message.content or ""
        except Exception as e:
            last_error = e
            if attempt < retries - 1:
                import time
                time.sleep(2 ** attempt)
    raise last_error


def _extract_json(text: str) -> dict:
    json_block = re.search(r"```(?:json)?\s*\n?(.*?)\n?```", text, re.DOTALL)
    if json_block:
        text = json_block.group(1)

    start = text.find("{")
    end = text.rfind("}") + 1
    if start == -1 or end == 0:
        return {}
    candidate = text[start:end]
    try:
        return json.loads(candidate)
    except json.JSONDecodeError:
        pass

    cleaned = re.sub(r",\s*([}\]])", r"\1", candidate)
    cleaned = re.sub(r"[\x00-\x1f]+", " ", cleaned)
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        pass

    brace_count = 0
    best_start = start
    best_end = end
    for i in range(start, len(text)):
        if text[i] == "{":
            brace_count += 1
        elif text[i] == "}":
            brace_count -= 1
            if brace_count == 0:
                best_end = i + 1
                break
    try:
        return json.loads(text[best_start:best_end])
    except json.JSONDecodeError:
        return {}


def _find_related_pages(config: WikiConfig, source_content: str, top_k: int = 5) -> list[str]:
    index_content = ""
    if config.index_path.exists():
        index_content = config.index_path.read_text(encoding="utf-8")

    if not index_content.strip():
        return []

    results = bm25_search(config.wiki_dir, source_content[:2000], top_k=top_k)
    page_contents = []
    for path, _score in results:
        content = path.read_text(encoding="utf-8")
        truncated, was_cut = truncate_to_tokens(content, max_tokens=1500)
        page_contents.append(f"### {path.stem}\n{truncated}")

    return page_contents


def _create_missing_stub_pages(config: WikiConfig, pages: list[WikiPage]) -> None:
    all_wikilinks = set()
    for page in pages:
        links = extract_wikilinks(page.to_markdown())
        all_wikilinks.update(links)

    existing_titles = set()
    for page in pages:
        existing_titles.add(page.title)

    for path in config.wiki_dir.rglob("*.md"):
        if path.parent.name in ("concepts", "entities", "sources", "answers"):
            try:
                from .schema import load_page
                p = load_page(path)
                existing_titles.add(p.title)
            except Exception:
                pass

    for link_title in all_wikilinks:
        if link_title in existing_titles:
            continue
        if find_page_by_title(config.wiki_dir, link_title):
            continue

        slug = _slugify(link_title)
        has_dot = "." in link_title
        has_upper = any(c.isupper() for c in link_title)
        if has_dot or (has_upper and len(link_title.split()) == 1):
            page_type = PageType.ENTITY
        else:
            page_type = PageType.CONCEPT

        stub = WikiPage(
            title=link_title,
            page_type=page_type,
            content=f"*Stub page for {link_title}. Content to be expanded.*",
            tags=["stub"],
            related=[],
        )
        pages.append(stub)


def ingest_source(config: WikiConfig, source_path: Path, dry_run: bool = False) -> list[WikiPage]:
    if is_source_ingested(config, source_path) and not dry_run:
        return []

    raw_content = source_path.read_text(encoding="utf-8")
    metadata = parse_source_metadata(raw_content)
    clean_content = extract_clean_content(raw_content)

    source_content, was_truncated = truncate_to_tokens(clean_content)

    wiki_index = ""
    if config.index_path.exists():
        wiki_index = config.index_path.read_text(encoding="utf-8")

    related_pages = _find_related_pages(config, source_content)
    related_text = "\n\n".join(related_pages) if related_pages else "(no related pages yet)"

    analysis_prompt = ANALYSIS_PROMPT.format(
        source_content=source_content,
        wiki_index=wiki_index[:3000],
        related_pages=related_text[:4000],
    )

    analysis_text = _call_llm(config, analysis_prompt)
    analysis = _extract_json(analysis_text)

    if not analysis:
        raise ValueError("LLM analysis failed — could not parse JSON response")

    if metadata.get("tags"):
        existing_tags = analysis.get("tags", [])
        for tag in metadata["tags"]:
            if tag not in existing_tags:
                existing_tags.append(tag)
        analysis["tags"] = existing_tags

    existing_pages_text = related_text if related_text else "(none)"

    language_instruction = _get_language_instruction(config.language)
    generation_prompt = GENERATION_PROMPT_TEMPLATE.format(
        analysis=json.dumps(analysis, indent=2, ensure_ascii=False),
        existing_pages=existing_pages_text[:4000],
        language_instruction=language_instruction,
    )

    generation_text = _call_llm(config, generation_prompt)
    generation = _extract_json(generation_text)

    if not generation:
        preview = generation_text[:300] if generation_text else "(empty)"
        raise ValueError(f"LLM generation failed — could not parse JSON response. Preview: {preview}")

    pages = []

    source_data = generation.get("source_page", {})
    if source_data:
        source_type = PageType.SOURCE
        source_page = WikiPage(
            title=source_data.get("title", analysis.get("title", source_path.stem)),
            page_type=source_type,
            content=source_data.get("content", analysis.get("summary", "")),
            sources=[str(source_path.relative_to(config.root))],
            tags=source_data.get("tags", analysis.get("tags", [])),
            related=source_data.get("related", []),
        )
        pages.append(source_page)

    for concept_data in generation.get("concept_pages", []):
        existing = find_page_by_title(config.wiki_dir, concept_data.get("title", ""))
        if existing:
            existing_page = _load_and_update_page(existing, concept_data, str(source_path.relative_to(config.root)))
            pages.append(existing_page)
        else:
            page = WikiPage(
                title=concept_data["title"],
                page_type=PageType.CONCEPT,
                content=concept_data.get("content", ""),
                sources=[str(source_path.relative_to(config.root))],
                tags=concept_data.get("tags", []),
                related=concept_data.get("related", []),
            )
            pages.append(page)

    for entity_data in generation.get("entity_pages", []):
        existing = find_page_by_title(config.wiki_dir, entity_data.get("title", ""))
        if existing:
            existing_page = _load_and_update_page(existing, entity_data, str(source_path.relative_to(config.root)))
            pages.append(existing_page)
        else:
            page = WikiPage(
                title=entity_data["title"],
                page_type=PageType.ENTITY,
                content=entity_data.get("content", ""),
                sources=[str(source_path.relative_to(config.root))],
                tags=entity_data.get("tags", []),
                related=entity_data.get("related", []),
            )
            pages.append(page)

    if dry_run:
        return pages

    _create_missing_stub_pages(config, pages)

    for page in pages:
        page.save(config.wiki_dir)

    for update in generation.get("index_updates", []):
        update_index(
            config,
            title=update.get("title", ""),
            page_type=PageType(update.get("type", "concept")),
            summary=update.get("summary", ""),
        )

    source_name = analysis.get("title", source_path.stem)
    append_to_log(config, "ingest", f"{source_name} — {len(pages)} pages created/updated")

    invalidate_cache(config.wiki_dir)

    move_to_ingested(config, source_path)

    return pages


def _load_and_update_page(path: Path, new_data: dict, source_ref: str) -> WikiPage:
    from .schema import load_page

    existing = load_page(path)
    new_content = new_data.get("content", "")
    if new_content:
        existing.content += f"\n\n---\n\n## Updated from new source\n\n{new_content}"
    if source_ref not in existing.sources:
        existing.sources.append(source_ref)
    for tag in new_data.get("tags", []):
        if tag not in existing.tags:
            existing.tags.append(tag)
    for rel in new_data.get("related", []):
        if rel not in existing.related:
            existing.related.append(rel)

    from datetime import datetime
    existing.updated_at = datetime.now().isoformat()

    return existing


def ingest_url(config: WikiConfig, url: str, dry_run: bool = False) -> list[WikiPage]:
    import httpx
    from bs4 import BeautifulSoup

    try:
        resp = httpx.get(url, follow_redirects=True, timeout=30)
        resp.raise_for_status()
    except httpx.HTTPError as e:
        raise ValueError(f"Failed to fetch URL: {e}")

    soup = BeautifulSoup(resp.text, "html.parser")

    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()

    title = soup.title.string.strip() if soup.title and soup.title.string else url
    content = soup.get_text(separator="\n", strip=True)

    from datetime import datetime
    date_prefix = datetime.now().strftime("%Y/%m/%d")
    slug = title.lower().replace(" ", "-")[:50]

    untracked_dir = config.raw_dir / "untracked" / date_prefix
    untracked_dir.mkdir(parents=True, exist_ok=True)
    source_path = untracked_dir / f"{slug}.md"

    source_content = f"# {title}\n\nSource: {url}\n\n{content}"
    source_path.write_text(source_content, encoding="utf-8")

    return ingest_source(config, source_path, dry_run=dry_run)


def batch_ingest(config: WikiConfig, max_sources: int = 0, dry_run: bool = False, workers: int = 2) -> list[WikiPage]:
    from concurrent.futures import ThreadPoolExecutor, as_completed
    from .utils import get_source_files

    sources = get_source_files(config)

    uningested = []
    for src in sources:
        if not is_source_ingested(config, src):
            uningested.append(src)

    if max_sources > 0:
        uningested = uningested[:max_sources]

    if not uningested:
        return []

    all_pages = []
    errors = []

    if workers > 1 and len(uningested) > 1:
        actual_workers = min(workers, len(uningested))

        def _ingest_one(src: Path) -> tuple[Path, list[WikiPage] | None, str | None]:
            try:
                pages = ingest_source(config, src, dry_run=dry_run)
                return src, pages, None
            except Exception as e:
                return src, None, str(e)

        with ThreadPoolExecutor(max_workers=actual_workers) as executor:
            futures = {executor.submit(_ingest_one, src): src for src in uningested}
            for future in as_completed(futures):
                src, pages, error = future.result()
                if error:
                    errors.append((src, error))
                elif pages:
                    all_pages.extend(pages)
    else:
        for src in uningested:
            try:
                pages = ingest_source(config, src, dry_run=dry_run)
                all_pages.extend(pages)
            except Exception as e:
                errors.append((src, str(e)))

    if errors:
        error_summary = "; ".join(f"{s.name}: {e}" for s, e in errors[:3])
        append_to_log(config, "batch-ingest-errors", f"{len(errors)} errors: {error_summary}")

    return all_pages
