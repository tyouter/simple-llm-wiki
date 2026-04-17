from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path

import frontmatter


class PageType(str, Enum):
    CONCEPT = "concept"
    ENTITY = "entity"
    SOURCE = "source"
    ANSWER = "answer"
    OVERVIEW = "overview"


@dataclass
class WikiPage:
    title: str
    page_type: PageType
    content: str
    sources: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    related: list[str] = field(default_factory=list)
    confidence: str = "high"
    created_at: str = ""
    updated_at: str = ""

    def __post_init__(self):
        now = datetime.now().isoformat()
        if not self.created_at:
            self.created_at = now
        if not self.updated_at:
            self.updated_at = now

    @property
    def sub_dir(self) -> str:
        plurals = {
            "concept": "concepts",
            "entity": "entities",
            "source": "sources",
            "answer": "answers",
            "overview": "overviews",
        }
        return plurals.get(self.page_type.value, f"{self.page_type.value}s")

    @property
    def filename(self) -> str:
        slug = _slugify(self.title)
        return f"{slug}.md"

    def to_markdown(self) -> str:
        fm = {
            "title": self.title,
            "type": self.page_type.value,
            "sources": self.sources,
            "tags": self.tags,
            "confidence": self.confidence,
            "created_at": self.updated_at,
            "updated_at": self.updated_at,
        }
        if self.related:
            fm["related"] = self.related

        lines = ["---"]
        for key, val in fm.items():
            if isinstance(val, list):
                if val:
                    lines.append(f"{key}:")
                    for item in val:
                        lines.append(f'  - "{item}"')
                else:
                    lines.append(f"{key}: []")
            else:
                lines.append(f'{key}: "{val}"' if isinstance(val, str) else f"{key}: {val}")
        lines.append("---")
        lines.append("")
        lines.append(self.content)

        if self.related:
            lines.append("")
            lines.append("## Related")
            for r in self.related:
                lines.append(f"- [[{r}]]")

        return "\n".join(lines)

    def save(self, wiki_dir: Path) -> Path:
        dir_path = wiki_dir / self.sub_dir
        dir_path.mkdir(parents=True, exist_ok=True)
        file_path = dir_path / self.filename
        file_path.write_text(self.to_markdown(), encoding="utf-8")
        return file_path


def load_page(path: Path) -> WikiPage:
    post = frontmatter.load(str(path))
    metadata = post.metadata

    return WikiPage(
        title=metadata.get("title", path.stem),
        page_type=PageType(metadata.get("type", "concept")),
        content=post.content,
        sources=metadata.get("sources", []),
        tags=metadata.get("tags", []),
        related=metadata.get("related", []),
        confidence=metadata.get("confidence", "high"),
        created_at=metadata.get("created_at", ""),
        updated_at=metadata.get("updated_at", ""),
    )


def _slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s\-/&,]", " ", text)
    text = re.sub(r"[/&]", "-", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    text = re.sub(r"^[-,]+|[-,]+$", "", text)
    return text


def extract_wikilinks(content: str) -> list[str]:
    return re.findall(r"\[\[([^\]]+)\]\]", content)


def page_exists(wiki_dir: Path, title: str, page_type: PageType) -> bool:
    slug = _slugify(title)
    plurals = {"concept": "concepts", "entity": "entities", "source": "sources", "answer": "answers", "overview": "overviews"}
    subdir = plurals.get(page_type.value, f"{page_type.value}s")
    path = wiki_dir / subdir / f"{slug}.md"
    return path.exists()


def find_page_by_title(wiki_dir: Path, title: str) -> Path | None:
    slug = _slugify(title)
    for subdir in WIKI_SUBDIRS:
        path = wiki_dir / subdir / f"{slug}.md"
        if path.exists():
            return path
    return None


WIKI_SUBDIRS = ["concepts", "entities", "sources", "answers"]
