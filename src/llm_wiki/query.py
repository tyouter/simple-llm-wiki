from __future__ import annotations

import json
from pathlib import Path

import litellm

from .config import WikiConfig
from .schema import PageType, WikiPage
from .search import bm25_search
from .utils import append_to_log, truncate_to_tokens, update_index


QUERY_PROMPT = """You are a knowledgeable research assistant with access to a personal wiki.
Answer the user's question based on the wiki pages provided below.
If the wiki pages don't contain enough information, say so clearly.
Always cite your sources using [src: PageTitle] format.

Wiki pages:
{wiki_pages}

User question: {question}

Provide a comprehensive answer in markdown format. Include citations where appropriate."""


NOVELTY_PROMPT = """You are evaluating whether a query answer contains novel synthesis worth preserving.

Question: {question}

Answer:
{answer}

Does this answer synthesize information across multiple pages in a way that would be valuable as a standalone wiki page?
Consider:
- Does it combine insights from multiple sources?
- Would someone benefit from finding this answer later?
- Is it more than just repeating a single page's content?

Respond in JSON:
{{"is_novel": true/false, "reason": "brief explanation"}}"""


def query_wiki(
    config: WikiConfig,
    question: str,
    save: bool = False,
    max_iterations: int = 3,
) -> str:
    if not config.index_path.exists():
        return "Wiki is empty. Add some sources first with `wiki ingest`."

    index_content = config.index_path.read_text(encoding="utf-8")

    all_page_contents = []
    seen_paths = set()

    for iteration in range(max_iterations):
        search_results = bm25_search(config.wiki_dir, question, top_k=10)

        for path, score in search_results:
            if path in seen_paths:
                continue
            seen_paths.add(path)

            content = path.read_text(encoding="utf-8")
            truncated, was_cut = truncate_to_tokens(content, max_tokens=2000)
            header = f"### {path.stem}"
            if was_cut:
                header += " (truncated)"
            all_page_contents.append(f"{header}\n{truncated}")

        if len(all_page_contents) >= 5 or iteration == max_iterations - 1:
            break

    if not all_page_contents:
        return "No relevant pages found in the wiki for your question."

    wiki_pages_text = "\n\n---\n\n".join(all_page_contents)

    prompt = QUERY_PROMPT.format(
        wiki_pages=wiki_pages_text,
        question=question,
    )

    response = litellm.completion(
        model=config.llm.model,
        messages=[{"role": "user", "content": prompt}],
        api_key=config.llm.api_key or None,
        api_base=config.llm.base_url,
        temperature=config.llm.temperature,
        max_tokens=config.llm.max_tokens,
    )

    answer = response.choices[0].message.content or "No answer generated."

    if save:
        _save_answer(config, question, answer)

    append_to_log(config, "query", question[:80])

    return answer


def _save_answer(config: WikiConfig, question: str, answer: str) -> None:
    novelty_prompt = NOVELTY_PROMPT.format(question=question, answer=answer[:2000])

    try:
        novelty_response = litellm.completion(
            model=config.llm.model,
            messages=[{"role": "user", "content": novelty_prompt}],
            api_key=config.llm.api_key or None,
            api_base=config.llm.base_url,
            temperature=0.1,
            max_tokens=256,
        )
        novelty_text = novelty_response.choices[0].message.content or ""
        start = novelty_text.find("{")
        end = novelty_text.rfind("}") + 1
        if start != -1 and end > start:
            novelty = json.loads(novelty_text[start:end])
            if not novelty.get("is_novel", False):
                return
    except Exception:
        pass

    title = question[:60].strip().rstrip("?.!") or "Query Answer"

    page = WikiPage(
        title=title,
        page_type=PageType.ANSWER,
        content=answer,
        tags=["query-answer"],
    )
    page.save(config.wiki_dir)
    update_index(config, title, PageType.ANSWER, f"Answer to: {question[:50]}")
    append_to_log(config, "save-answer", title)
