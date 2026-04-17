from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .config import WikiConfig
from .schema import extract_wikilinks, find_page_by_title, load_page
from .utils import get_all_wiki_pages


@dataclass
class LintIssue:
    severity: str  # "error", "warning", "info"
    category: str  # "orphan", "dead-link", "stale", "shallow", "missing-concept"
    page: str
    description: str


def lint_wiki(config: WikiConfig) -> list[LintIssue]:
    issues: list[LintIssue] = []
    wiki_dir = config.wiki_dir

    all_pages = get_all_wiki_pages(wiki_dir)
    if not all_pages:
        return [LintIssue("info", "empty", "", "Wiki is empty — no pages to lint")]

    page_titles = set()
    page_paths = {}
    inbound_links: dict[str, list[str]] = {}
    all_wikilinks: dict[str, list[str]] = {}

    for path in all_pages:
        try:
            page = load_page(path)
        except Exception:
            issues.append(LintIssue("error", "parse-error", str(path), f"Could not parse {path.name}"))
            continue

        page_titles.add(page.title)
        page_paths[page.title] = path
        inbound_links[page.title] = []

        links = extract_wikilinks(page.to_markdown())
        all_wikilinks[page.title] = links

    for title, links in all_wikilinks.items():
        for link in links:
            if link in inbound_links:
                inbound_links[link].append(title)
            elif find_page_by_title(wiki_dir, link):
                resolved = find_page_by_title(wiki_dir, link)
                try:
                    resolved_page = load_page(resolved)
                    if resolved_page.title in inbound_links:
                        inbound_links[resolved_page.title].append(title)
                    else:
                        inbound_links[resolved_page.title] = [title]
                except Exception:
                    pass
            else:
                issues.append(
                    LintIssue(
                        severity="error",
                        category="dead-link",
                        page=title,
                        description=f"[[{link}]] links to a non-existent page",
                    )
                )

    for title in page_titles:
        if not inbound_links.get(title):
            if title.lower() not in ("wiki overview", "overview"):
                issues.append(
                    LintIssue(
                        severity="warning",
                        category="orphan",
                        page=title,
                        description=f"'{title}' has no inbound links — consider adding cross-references",
                    )
                )

    for path in all_pages:
        try:
            page = load_page(path)
        except Exception:
            continue

        content_words = len(page.content.split())
        if content_words < 30:
            issues.append(
                LintIssue(
                    severity="warning",
                    category="shallow",
                    page=page.title,
                    description=f"'{page.title}' has only {content_words} words — consider expanding",
                )
            )

        if not page.tags:
            issues.append(
                LintIssue(
                    severity="info",
                    category="missing-tags",
                    page=page.title,
                    description=f"'{page.title}' has no tags",
                )
            )

    for title, links in all_wikilinks.items():
        for link in links:
            if link in page_titles and link not in all_wikilinks.get(link, []):
                pass

    mentioned_in_text = set()
    for path in all_pages:
        try:
            content = path.read_text(encoding="utf-8")
        except Exception:
            continue
        for title in page_titles:
            if title in content and f"[[{title}]]" not in content:
                mentioned_in_text.add((path.stem, title))

    for page_name, concept in mentioned_in_text:
        issues.append(
            LintIssue(
                severity="info",
                category="missing-concept",
                page=page_name,
                description=f"'{concept}' is mentioned but not linked with [[{concept}]]",
            )
        )

    return issues
