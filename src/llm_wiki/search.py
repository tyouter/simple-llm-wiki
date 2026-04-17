from __future__ import annotations

import re
import time
from pathlib import Path

from rank_bm25 import BM25Okapi

_cache: dict[str, tuple[float, list[Path], list[str], BM25Okapi]] = {}
_CACHE_TTL = 30.0


def _tokenize(text: str) -> list[str]:
    return re.findall(r"\w+", text.lower())


def _strip_frontmatter(content: str) -> str:
    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            return content[end + 3:]
    return content


def _get_corpus(wiki_dir: Path) -> tuple[list[Path], list[str], BM25Okapi]:
    cache_key = str(wiki_dir)
    now = time.time()

    if cache_key in _cache:
        cached_time, cached_pages, cached_docs, cached_bm25 = _cache[cache_key]
        if now - cached_time < _CACHE_TTL:
            return cached_pages, cached_docs, cached_bm25

    pages = []
    for subdir in ["concepts", "entities", "sources", "answers"]:
        d = wiki_dir / subdir
        if d.exists():
            pages.extend(d.glob("*.md"))

    if not pages:
        return [], [], BM25Okapi([[""]])

    documents = []
    valid_pages = []
    for path in pages:
        try:
            content = path.read_text(encoding="utf-8")
            body = _strip_frontmatter(content)
            documents.append(body)
            valid_pages.append(path)
        except Exception:
            continue

    if not documents:
        return [], [], BM25Okapi([[""]])

    tokenized_corpus = [_tokenize(doc) for doc in documents]
    bm25 = BM25Okapi(tokenized_corpus)

    _cache[cache_key] = (now, valid_pages, documents, bm25)

    return valid_pages, documents, bm25


def invalidate_cache(wiki_dir: Path | None = None) -> None:
    if wiki_dir is None:
        _cache.clear()
    else:
        _cache.pop(str(wiki_dir), None)


def bm25_search(wiki_dir: Path, query: str, top_k: int = 10) -> list[tuple[Path, float]]:
    valid_pages, documents, bm25 = _get_corpus(wiki_dir)

    if not valid_pages:
        return []

    tokenized_query = _tokenize(query)
    scores = bm25.get_scores(tokenized_query)

    scored = list(zip(valid_pages, scores))
    scored.sort(key=lambda x: x[1], reverse=True)

    return scored[:top_k]


def keyword_search(wiki_dir: Path, keywords: list[str], top_k: int = 10) -> list[tuple[Path, int]]:
    results: dict[Path, int] = {}

    pages = []
    for subdir in ["concepts", "entities", "sources", "answers"]:
        d = wiki_dir / subdir
        if d.exists():
            pages.extend(d.glob("*.md"))

    for path in pages:
        try:
            content = path.read_text(encoding="utf-8").lower()
        except Exception:
            continue

        count = sum(1 for kw in keywords if kw.lower() in content)
        if count > 0:
            results[path] = count

    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
    return sorted_results[:top_k]
