#!/usr/bin/env python3
"""Fix ALL pipe-syntax dead links by replacing with clean links."""

from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path

ROOT_DIR = Path(__file__).parent
WIKI_DIR = ROOT_DIR / "wiki"

pages = {}
for subdir in ["concepts", "entities", "sources", "answers"]:
    d = WIKI_DIR / subdir
    if d.exists():
        for path in d.glob("*.md"):
            try:
                content = path.read_text(encoding="utf-8")
                title_match = re.search(r'^title: "(.+)"', content, re.MULTILINE)
                title = title_match.group(1) if title_match else path.stem
                pages[title] = {"path": path, "content": content, "subdir": subdir}
            except:
                pass

all_titles = set(pages.keys())

# Also fix source titles with pipe characters
print("=== Fixing source titles with pipe characters ===")
source_title_fixes = 0
for title, info in list(pages.items()):
    if "|" in title:
        clean_title = title.split("|")[0].strip()
        content = info["content"]
        content = content.replace(f'title: "{title}"', f'title: "{clean_title}"')
        content = re.sub(r'updated_at: "[^"]*"', f'updated_at: "{datetime.now().isoformat()}"', content)
        info["path"].write_text(content, encoding="utf-8")
        if clean_title != title:
            pages[clean_title] = info
            del pages[title]
            source_title_fixes += 1

all_titles = set(pages.keys())
print(f"  Fixed {source_title_fixes} source titles")

# Fix pipe links
print("\n=== Fixing pipe links ===")
pipe_pattern = re.compile(r"\[\[([^\]]+?)\s*\|\s*([^\]]+?)\]\]")
fixed_links = [0]

for title, info in pages.items():
    content = info["content"]
    original = content

    def replace_pipe_link(match):
        link_target = match.group(1).strip()
        display_text = match.group(2).strip()

        if link_target in all_titles:
            return match.group(0)

        full_title = None
        for t in all_titles:
            if t == link_target:
                full_title = t
                break
            if t.startswith(link_target) and len(link_target) / max(len(t), 1) >= 0.4:
                full_title = t
                break

        if not full_title:
            for t in all_titles:
                t_lower = t.lower()
                lt_lower = link_target.lower()
                if lt_lower in t_lower or t_lower in lt_lower:
                    if min(len(lt_lower), len(t_lower)) / max(len(lt_lower), len(t_lower)) >= 0.5:
                        full_title = t
                        break

        if full_title:
            fixed_links[0] += 1
            return f"[[{full_title}]]"
        else:
            fixed_links[0] += 1
            return display_text

    new_content = pipe_pattern.sub(replace_pipe_link, content)

    if new_content != original:
        new_content = re.sub(
            r'updated_at: "[^"]*"',
            f'updated_at: "{datetime.now().isoformat()}"',
            new_content,
        )
        info["path"].write_text(new_content, encoding="utf-8")
        info["content"] = new_content

print(f"  Fixed {fixed_links[0]} pipe links")

# Verify
all_titles = set()
for subdir in ["concepts", "entities", "sources", "answers"]:
    d = WIKI_DIR / subdir
    if d.exists():
        for path in d.glob("*.md"):
            try:
                content = path.read_text(encoding="utf-8")
                title_match = re.search(r'^title: "(.+)"', content, re.MULTILINE)
                title = title_match.group(1) if title_match else path.stem
                all_titles.add(title)
            except:
                pass

dead = 0
dead_targets = set()
for title, info in pages.items():
    links = re.findall(r"\[\[([^\]]+)\]\]", info["content"])
    for l in links:
        lt = l.split("|")[0].strip() if "|" in l else l.strip()
        if lt and lt not in all_titles:
            dead += 1
            dead_targets.add(lt)

print(f"\nRemaining dead links: {dead}")
print(f"Remaining unique dead targets: {len(dead_targets)}")
for dt in sorted(dead_targets):
    print(f"  [[{dt}]]")
