from __future__ import annotations

import json
import re
from pathlib import Path

import litellm

from .config import WikiConfig
from .schema import PageType, WikiPage, extract_wikilinks, find_page_by_title, load_page
from .search import bm25_search
from .utils import (
    append_to_log,
    extract_clean_content,
    truncate_to_tokens,
    parse_source_metadata,
    update_index,
)


DEEP_ANALYSIS_PROMPT = """You are a deep knowledge analyst. Perform thorough analysis of this source document:

Source document:
{source_content}

Existing wiki concepts (for linking):
{existing_concepts}

TASKS:
1. Extract ALL key concepts (aim for 10-15, not just 3-5)
2. For each concept, identify:
   - Definition and core explanation
   - Related concepts (create bidirectional links)
   - Practical applications or examples
   - Connection strength (strong/medium/weak)
3. Extract ALL entities (people, orgs, products, tools)
4. Identify concept-concept relationships (hierarchical, complementary, opposing)
5. Find contradictions with existing knowledge

Respond in JSON:
{
  "title": "source title",
  "summary": "2-3 sentence summary",
  "concepts": [
    {
      "name": "ConceptName",
      "definition": "clear definition",
      "explanation": "detailed explanation (3-5 sentences)",
      "related_concepts": ["ConceptA", "ConceptB"],
      "relation_types": {"ConceptA": "hierarchical-parent", "ConceptB": "complementary"},
      "examples": ["example1"],
      "confidence": "high|medium|low"
    }
  ],
  "entities": [
    {
      "name": "EntityName",
      "type": "person|organization|product|tool",
      "description": "detailed description",
      "related_concepts": ["ConceptX"]
    }
  ],
  "concept_graph": {
    "hierarchical": [{"parent": "A", "child": "B"}],
    "complementary": [{"a": "A", "b": "B"}],
    "opposing": [{"a": "A", "b": "B"}]
  },
  "contradictions": ["contradiction1"],
  "tags": ["tag1", "tag2"]
}"""


DEEP_GENERATION_PROMPT = """You are a wiki architect. Create deep interconnected wiki pages.

Analysis:
{analysis}

Existing concept pages to enhance:
{existing_pages}

Generate wiki pages with RICH BIDIRECTIONAL LINKING:
{
  "source_page": {
    "title": "...",
    "content": "markdown with [[links]] to all concepts/entities",
    "tags": ["..."],
    "related": ["Concept1", "Entity1"]
  },
  "concept_pages": [
    {
      "title": "ConceptName",
      "content": "detailed content (5+ sentences) with [[links]] to related concepts",
      "tags": ["..."],
      "related": ["RelatedConcept1", "RelatedConcept2", "EntityName"],
      "backlinks_note": "This concept is referenced by: [[SourceName]], [[OtherConcept]]"
    }
  ],
  "entity_pages": [
    {
      "title": "EntityName",
      "content": "detailed content with [[links]] to related concepts",
      "tags": ["..."],
      "related": ["ConceptA", "ConceptB"]
    }
  ],
  "link_enrichments": [
    {
      "target_page": "ExistingConceptName",
      "new_related": ["NewConcept1", "NewConcept2"],
      "append_content": "Additional insights about this concept from new source"
    }
  ],
  "index_updates": [{"title": "...", "type": "...", "summary": "..."}]
}

RULES:
- Every concept MUST have 3+ related concepts with [[links]]
- Create bidirectional links (if A links to B, B should link to A)
- Include backlinks_note showing where concept is referenced
- Content should be 5+ sentences, not stubs
- Use hierarchical/complementary/opposing relationships
- Write in {language}"""


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
                timeout=180,
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
        return {}


def _get_existing_concepts(config: WikiConfig) -> list[str]:
    """Get list of existing concept names for linking."""
    concepts_dir = config.wiki_dir / "concepts"
    if not concepts_dir.exists():
        return []

    concepts = []
    for path in concepts_dir.glob("*.md"):
        try:
            page = load_page(path)
            concepts.append(page.title)
        except Exception:
            concepts.append(path.stem)

    return concepts[:100]  # Limit to avoid huge prompts


def _get_existing_pages_content(config: WikiConfig, concept_names: list[str]) -> dict[str, str]:
    """Get content of existing concept pages for enhancement."""
    existing = {}
    for name in concept_names[:10]:
        path = find_page_by_title(config.wiki_dir, name)
        if path:
            try:
                page = load_page(path)
                existing[name] = page.content[:500]  # Truncated for prompt
            except Exception:
                pass
    return existing


def _get_language_instruction(language: str) -> str:
    if language == "cn":
        return "Chinese (中文)"
    elif language == "en":
        return "English"
    else:
        return "the same language as the source document"


def _enrich_existing_pages(config: WikiConfig, enrichments: list[dict], source_ref: str) -> list[WikiPage]:
    """Add new related links and content to existing pages."""
    enriched_pages = []

    for enrichment in enrichments:
        target_title = enrichment.get("target_page", "")
        target_path = find_page_by_title(config.wiki_dir, target_title)

        if not target_path:
            continue

        try:
            page = load_page(target_path)

            # Add new related concepts
            new_related = enrichment.get("new_related", [])
            for rel in new_related:
                if rel and rel not in page.related:
                    page.related.append(rel)

            # Append additional content
            append_content = enrichment.get("append_content", "")
            if append_content:
                page.content += f"\n\n---\n\n## Additional Insights\n\n{append_content}\n\nSource: [[{source_ref}]]"

            # Add source to sources list
            if source_ref not in page.sources:
                page.sources.append(source_ref)

            page.save(config.wiki_dir)
            enriched_pages.append(page)

        except Exception:
            pass

    return enriched_pages


def deep_parse_source(config: WikiConfig, source_path: Path) -> list[WikiPage]:
    """Deep parse a source with enhanced concept extraction and bidirectional linking."""
    raw_content = source_path.read_text(encoding="utf-8")
    metadata = parse_source_metadata(raw_content)
    clean_content = extract_clean_content(raw_content)

    source_content, was_truncated = truncate_to_tokens(clean_content, max_tokens=12000)

    existing_concepts = _get_existing_concepts(config)
    existing_concepts_str = "\n".join(existing_concepts[:50]) if existing_concepts else "(none yet)"

    # Deep analysis
    analysis_prompt = DEEP_ANALYSIS_PROMPT.format(
        source_content=source_content,
        existing_concepts=existing_concepts_str,
    )

    analysis_text = _call_llm(config, analysis_prompt)
    analysis = _extract_json(analysis_text)

    if not analysis:
        raise ValueError("Deep analysis failed - could not parse JSON")

    # Get existing pages for concepts mentioned in analysis
    concept_names = [c.get("name", "") for c in analysis.get("concepts", [])]
    existing_pages = _get_existing_pages_content(config, concept_names)
    existing_pages_str = "\n".join([f"### {k}\n{v}" for k, v in existing_pages.items()]) if existing_pages else "(none)"

    language_instruction = _get_language_instruction(config.language)

    # Deep generation
    generation_prompt = DEEP_GENERATION_PROMPT.format(
        analysis=json.dumps(analysis, indent=2, ensure_ascii=False),
        existing_pages=existing_pages_str,
        language=language_instruction,
    )

    generation_text = _call_llm(config, generation_prompt)
    generation = _extract_json(generation_text)

    if not generation:
        raise ValueError("Deep generation failed - could not parse JSON")

    pages = []
    source_ref = source_path.relative_to(config.root).as_posix()

    # Source page
    source_data = generation.get("source_page", {})
    if source_data:
        source_page = WikiPage(
            title=source_data.get("title", analysis.get("title", source_path.stem)),
            page_type=PageType.SOURCE,
            content=source_data.get("content", analysis.get("summary", "")),
            sources=[source_ref],
            tags=source_data.get("tags", analysis.get("tags", [])),
            related=source_data.get("related", []),
        )
        source_page.save(config.wiki_dir)
        pages.append(source_page)

    # Concept pages with bidirectional linking
    for concept_data in generation.get("concept_pages", []):
        title = concept_data.get("title", "")
        if not title:
            continue

        existing_path = find_page_by_title(config.wiki_dir, title)

        if existing_path:
            # Update existing page
            try:
                page = load_page(existing_path)
                new_content = concept_data.get("content", "")
                if new_content:
                    page.content += f"\n\n---\n\n## Extended Definition\n\n{new_content}"

                # Add bidirectional links
                new_related = concept_data.get("related", [])
                for rel in new_related:
                    if rel and rel not in page.related:
                        page.related.append(rel)

                if source_ref not in page.sources:
                    page.sources.append(source_ref)

                page.save(config.wiki_dir)
                pages.append(page)
            except Exception:
                pass
        else:
            # Create new concept page
            page = WikiPage(
                title=title,
                page_type=PageType.CONCEPT,
                content=concept_data.get("content", ""),
                sources=[source_ref],
                tags=concept_data.get("tags", []),
                related=concept_data.get("related", []),
            )
            page.save(config.wiki_dir)
            pages.append(page)

    # Entity pages
    for entity_data in generation.get("entity_pages", []):
        title = entity_data.get("title", "")
        if not title:
            continue

        existing_path = find_page_by_title(config.wiki_dir, title)

        if existing_path:
            try:
                page = load_page(existing_path)
                new_content = entity_data.get("content", "")
                if new_content:
                    page.content += f"\n\n---\n\n{new_content}"

                new_related = entity_data.get("related", [])
                for rel in new_related:
                    if rel and rel not in page.related:
                        page.related.append(rel)

                if source_ref not in page.sources:
                    page.sources.append(source_ref)

                page.save(config.wiki_dir)
                pages.append(page)
            except Exception:
                pass
        else:
            page = WikiPage(
                title=title,
                page_type=PageType.ENTITY,
                content=entity_data.get("content", ""),
                sources=[source_ref],
                tags=entity_data.get("tags", []),
                related=entity_data.get("related", []),
            )
            page.save(config.wiki_dir)
            pages.append(page)

    # Enrich existing pages
    enrichments = generation.get("link_enrichments", [])
    enriched = _enrich_existing_pages(config, enrichments, source_ref)
    pages.extend(enriched)

    # Update index
    for update in generation.get("index_updates", []):
        update_index(
            config,
            title=update.get("title", ""),
            page_type=PageType(update.get("type", "concept")),
            summary=update.get("summary", ""),
        )

    # Log
    source_name = analysis.get("title", source_path.stem)
    append_to_log(config, "deep-parse", f"{source_name} - {len(pages)} pages created/enriched")

    return pages


def deep_query_wiki(config: WikiConfig, question: str, top_k: int = 20) -> str:
    """Query with deeper context retrieval."""
    from .query import query_wiki

    # Use more context pages for deeper answer
    return query_wiki(config, question, save=False, top_k=top_k)


def deep_lint_wiki(config: WikiConfig) -> list:
    """Deep lint with relationship analysis."""
    from .lint import lint_wiki
    from .schema import load_page, extract_wikilinks
    from .utils import get_all_wiki_pages

    issues = lint_wiki(config)

    # Additional deep checks
    pages = get_all_wiki_pages(config.wiki_dir)

    # Check for concepts with no bidirectional links
    for path in pages:
        if path.parent.name != "concepts":
            continue

        try:
            page = load_page(path)
            links = extract_wikilinks(page.to_markdown())

            # Check if linked pages link back
            for link in links[:5]:
                link_path = find_page_by_title(config.wiki_dir, link)
                if link_path:
                    try:
                        linked_page = load_page(link_path)
                        if page.title not in linked_page.related:
                            # Missing bidirectional link
                            class DeepIssue:
                                category = "missing-bidirectional"
                                pages = f"{page.title} -> {link}"
                                description = f"{link} links to {page.title} but {page.title} doesn't link back"

                            issues.append(DeepIssue())
                    except Exception:
                        pass
        except Exception:
            pass

    return issues


def deep_stats(config: WikiConfig) -> dict:
    """Deep statistics with quality metrics."""
    from .schema import load_page, extract_wikilinks
    from .utils import get_all_wiki_pages, count_tokens_approx

    pages = get_all_wiki_pages(config.wiki_dir)

    stats = {
        "Total Pages": len(pages),
        "Concept Pages": sum(1 for p in pages if p.parent.name == "concepts"),
        "Entity Pages": sum(1 for p in pages if p.parent.name == "entities"),
        "Source Pages": sum(1 for p in pages if p.parent.name == "sources"),
    }

    total_content_length = 0
    total_links = 0
    shallow_pages = 0
    pages_with_3plus_related = 0

    for path in pages:
        try:
            page = load_page(path)
            total_content_length += len(page.content)

            links = extract_wikilinks(page.to_markdown())
            total_links += len(links)

            if len(page.content.split()) < 30:
                shallow_pages += 1

            if len(page.related) >= 3:
                pages_with_3plus_related += 1

        except Exception:
            pass

    stats["Total Content Characters"] = total_content_length
    stats["Total Wikilinks"] = total_links
    stats["Average Links per Page"] = round(total_links / max(len(pages), 1), 2)
    stats["Shallow Pages (<30 words)"] = shallow_pages
    stats["Rich Pages (3+ related)"] = pages_with_3plus_related
    stats["Link Density Score"] = round(pages_with_3plus_related / max(stats["Concept Pages"], 1), 2)

    return stats