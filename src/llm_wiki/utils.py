from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime
from pathlib import Path

from .config import WikiConfig
from .schema import PageType, extract_wikilinks, find_page_by_title


def compute_file_hash(path: Path) -> str:
    content = path.read_bytes()
    return hashlib.sha256(content).hexdigest()


def compute_text_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def today_str() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def now_str() -> str:
    return datetime.now().isoformat()


def format_log_entry(operation: str, description: str) -> str:
    return f"## [{today_str()}] {operation} | {description}\n\n"


def append_to_log(config: WikiConfig, operation: str, description: str) -> None:
    entry = format_log_entry(operation, description)
    log_path = config.log_path
    content = log_path.read_text(encoding="utf-8") if log_path.exists() else ""
    content += entry
    log_path.write_text(content, encoding="utf-8")


def update_index(config: WikiConfig, title: str, page_type: PageType, summary: str) -> None:
    index_path = config.index_path
    content = index_path.read_text(encoding="utf-8") if index_path.exists() else ""

    section_header = f"## {page_type.value.capitalize()}s"
    new_entry = f"- [[{title}]] — {summary}"

    if section_header not in content:
        content += f"\n{section_header}\n\n{new_entry}\n"
    else:
        pattern = re.escape(title)
        if re.search(pattern, content):
            return

        parts = content.split(section_header, 1)
        after = parts[1] if len(parts) > 1 else ""
        lines = after.split("\n")

        insert_idx = 1
        for i, line in enumerate(lines):
            if line.startswith("- [["):
                insert_idx = i + 1
            elif line.strip() == "" and insert_idx > 1:
                break

        lines.insert(insert_idx, new_entry)
        content = parts[0] + section_header + "\n".join(lines)

    index_path.write_text(content, encoding="utf-8")


def resolve_wikilinks(config: WikiConfig, content: str) -> list[Path]:
    links = extract_wikilinks(content)
    resolved = []
    for link in links:
        path = find_page_by_title(config.wiki_dir, link)
        if path:
            resolved.append(path)
    return resolved


def get_all_wiki_pages(wiki_dir: Path) -> list[Path]:
    pages = []
    for subdir in ["concepts", "entities", "sources", "answers"]:
        d = wiki_dir / subdir
        if d.exists():
            pages.extend(d.glob("*.md"))
    return pages


def get_raw_sources(raw_dir: Path, ingested: bool = False) -> list[Path]:
    subdir = "ingested" if ingested else "untracked"
    d = raw_dir / subdir
    if not d.exists():
        return []
    return sorted(d.rglob("*.md"))


def get_source_files(config: WikiConfig) -> list[Path]:
    files = []
    source_dir = config.raw_source_dir
    if source_dir.exists():
        for subdir in ["articles", "videos"]:
            d = source_dir / subdir
            if d.exists():
                files.extend(sorted(d.glob("*.md")))
    untracked = config.raw_dir / "untracked"
    if untracked.exists():
        files.extend(sorted(untracked.rglob("*.md")))
    return files


def load_ingest_cache(config: WikiConfig) -> dict[str, str]:
    cache_path = config.hash_cache_path
    if cache_path.exists():
        try:
            return json.loads(cache_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return {}
    return {}


def save_ingest_cache(config: WikiConfig, cache: dict[str, str]) -> None:
    config.hash_cache_path.write_text(
        json.dumps(cache, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def is_source_ingested(config: WikiConfig, source_path: Path) -> bool:
    cache = load_ingest_cache(config)
    key = str(source_path.relative_to(config.root))
    current_hash = compute_file_hash(source_path)
    return cache.get(key) == current_hash


def mark_source_ingested(config: WikiConfig, source_path: Path) -> None:
    cache = load_ingest_cache(config)
    key = str(source_path.relative_to(config.root))
    cache[key] = compute_file_hash(source_path)
    save_ingest_cache(config, cache)


def move_to_ingested(config: WikiConfig, source_path: Path) -> Path:
    try:
        rel = source_path.relative_to(config.raw_dir / "untracked")
        dest = config.raw_dir / "ingested" / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        source_path.rename(dest)
        return dest
    except ValueError:
        mark_source_ingested(config, source_path)
        return source_path


def parse_source_metadata(content: str) -> dict:
    metadata = {"type": "article", "author": "", "platform": ""}

    if "## 视频信息" in content or "## 视频信息" in content:
        metadata["type"] = "video"
    elif "## 文章信息" in content:
        metadata["type"] = "article"

    author_match = re.search(r"\*\*作者\*\*:\s*(.+)", content)
    if author_match:
        metadata["author"] = author_match.group(1).strip()

    platform_match = re.search(r"\*\*平台\*\*:\s*(.+)", content)
    if platform_match:
        metadata["platform"] = platform_match.group(1).strip()

    tags_match = re.search(r"\*\*标签\*\*:\s*(.+)", content)
    if tags_match:
        metadata["tags"] = [t.strip() for t in tags_match.group(1).split(",")]

    return metadata


def extract_clean_content(content: str) -> str:
    lines = content.split("\n")
    clean_lines = []
    in_metadata = False
    content_started = False

    for line in lines:
        if line.strip().startswith("## 文章信息") or line.strip().startswith("## 视频信息"):
            in_metadata = True
            continue
        if in_metadata and line.strip().startswith("## "):
            in_metadata = False
            content_started = True
        if in_metadata:
            continue
        if line.strip().startswith("## 内容"):
            content_started = True
            continue
        if content_started:
            clean_lines.append(line)

    return "\n".join(clean_lines).strip() if clean_lines else content


def count_tokens_approx(text: str) -> int:
    return len(text) // 4


def truncate_to_tokens(text: str, max_tokens: int = 8000) -> tuple[str, bool]:
    approx = count_tokens_approx(text)
    if approx <= max_tokens:
        return text, False
    char_limit = max_tokens * 4
    return text[:char_limit], True
