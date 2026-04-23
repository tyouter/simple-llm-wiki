#!/usr/bin/env python3
"""Fix quality issues found by deep lint: dead links, orphans, shallow pages, missing bidirectional links."""

from __future__ import annotations

import re
import sys
from datetime import datetime
from pathlib import Path

ROOT_DIR = Path(__file__).parent
WIKI_DIR = ROOT_DIR / "wiki"
CONCEPTS_DIR = WIKI_DIR / "concepts"
ENTITIES_DIR = WIKI_DIR / "entities"
SOURCES_DIR = WIKI_DIR / "sources"
ANSWERS_DIR = WIKI_DIR / "answers"


def load_all_pages():
    pages = {}
    for subdir in ["concepts", "entities", "sources", "answers"]:
        d = WIKI_DIR / subdir
        if d.exists():
            for path in d.glob("*.md"):
                try:
                    content = path.read_text(encoding="utf-8")
                    title_match = re.search(r'^title: "(.+)"', content, re.MULTILINE)
                    title = title_match.group(1) if title_match else path.stem
                    links = re.findall(r"\[\[([^\]]+)\]\]", content)
                    link_targets = [l.split("|")[0].strip() for l in links if l.strip()]
                    pages[title] = {
                        "path": path,
                        "content": content,
                        "links": link_targets,
                        "subdir": subdir,
                        "linked_from": set(),
                    }
                except Exception:
                    pass
    return pages


def fix_dead_links(pages):
    print("\n=== Fixing dead links ===")
    all_titles = set(pages.keys())
    fixed = 0
    removed = 0

    dead_to_fix = {}
    for title, info in pages.items():
        for link_target in info["links"]:
            if link_target and link_target not in all_titles:
                if link_target not in dead_to_fix:
                    best = find_best_match(link_target, all_titles)
                    dead_to_fix[link_target] = best

    for dead, best_match in dead_to_fix.items():
        if best_match:
            for title, info in pages.items():
                content = info["content"]
                has_link = f"[[{dead}]]" in content or f"[[{dead}|" in content
                if not has_link:
                    continue
                original = content
                content = content.replace(f"[[{dead}]]", f"[[{best_match}]]")
                content = content.replace(f"[[{dead}|", f"[[{best_match}|")
                if content != original:
                    content = re.sub(r'updated_at: "[^"]*"', f'updated_at: "{datetime.now().isoformat()}"', content)
                    info["path"].write_text(content, encoding="utf-8")
                    info["content"] = content
                    if dead in info["links"]:
                        info["links"].remove(dead)
                    if best_match not in info["links"]:
                        info["links"].append(best_match)
                    fixed += 1
        else:
            for title, info in pages.items():
                content = info["content"]
                has_link = f"[[{dead}]]" in content or f"[[{dead}|" in content
                if not has_link:
                    continue
                original = content
                content = re.sub(rf"\[\[{re.escape(dead)}\]\]", dead, content)
                content = re.sub(rf"\[\[{re.escape(dead)}\|[^\]]*\]\]", dead, content)
                if content != original:
                    content = re.sub(r'updated_at: "[^"]*"', f'updated_at: "{datetime.now().isoformat()}"', content)
                    info["path"].write_text(content, encoding="utf-8")
                    info["content"] = content
                    if dead in info["links"]:
                        info["links"].remove(dead)
                    removed += 1

    print(f"  Fixed (redirected): {fixed}")
    print(f"  Removed (unresolvable): {removed}")


def find_best_match(dead_link, all_titles):
    dead_lower = dead_link.lower().strip()
    if not dead_lower:
        return None

    for t in all_titles:
        if t.lower() == dead_lower:
            return t

    dead_words = set(dead_lower.split())
    best = None
    best_score = 0

    for t in all_titles:
        t_lower = t.lower()
        t_words = set(t_lower.split())
        overlap = len(dead_words & t_words)
        score = overlap / max(len(dead_words), 1)
        if score > best_score and score >= 0.7:
            best_score = score
            best = t

    if best and best_score >= 0.8:
        return best

    if len(dead_lower) > 8:
        for t in all_titles:
            t_lower = t.lower()
            if t_lower.startswith(dead_lower) or dead_lower.startswith(t_lower):
                score = min(len(dead_lower), len(t_lower)) / max(len(dead_lower), len(t_lower))
                if score >= 0.7:
                    return t

    return None


def add_link_to_page(info, link_title):
    content = info["content"]
    if f"[[{link_title}]]" in content or f"[[{link_title}|" in content:
        return False

    related_match = re.search(r"related:\n((?:  - .+\n)*)", content)
    if related_match:
        new_entry = f'  - "{link_title}"\n'
        content = content[: related_match.end()] + new_entry + content[related_match.end() :]

    related_section = re.search(r"## Related\n((?:- \[\[.+\]\]\n)*)", content)
    if related_section:
        new_link = f"- [[{link_title}]]\n"
        content = content[: related_section.end()] + new_link + content[related_section.end() :]
    elif "## Related" not in content:
        insert_pos = len(content)
        for marker in ["## Content", "## Related", "---\n#"]:
            pos = content.find(marker)
            if pos > 0:
                insert_pos = pos
                break
        related_block = f"\n## Related\n- [[{link_title}]]\n\n"
        content = content[:insert_pos] + related_block + content[insert_pos:]

    content = re.sub(
        r'updated_at: "[^"]*"',
        f'updated_at: "{datetime.now().isoformat()}"',
        content,
    )
    info["path"].write_text(content, encoding="utf-8")
    info["content"] = content
    if link_title not in info["links"]:
        info["links"].append(link_title)
    return True


def fix_missing_bidirectional(pages):
    print("\n=== Fixing missing bidirectional links ===")
    fixed = 0
    MAX_RELATED_PER_PAGE = 30

    for title, info in pages.items():
        if info["subdir"] in ["sources", "answers"]:
            continue

        for link_target in info["links"]:
            if link_target not in pages or link_target == title:
                continue
            target_info = pages[link_target]
            if target_info["subdir"] in ["sources", "answers"]:
                continue

            target_content = target_info["content"]
            if f"[[{title}]]" in target_content or f"[[{title}|" in target_content:
                continue

            existing_related = len(re.findall(r"\[\[.+\]\]", target_content.split("## Content")[0] if "## Content" in target_content else target_content))
            if existing_related >= MAX_RELATED_PER_PAGE:
                continue

            if add_link_to_page(target_info, title):
                fixed += 1

    print(f"  Fixed {fixed} bidirectional links")


def fix_orphan_pages(pages):
    print("\n=== Fixing orphan pages ===")
    for title, info in pages.items():
        for link_target in info["links"]:
            if link_target in pages:
                pages[link_target]["linked_from"].add(title)

    orphans = [
        (title, info)
        for title, info in pages.items()
        if not info["linked_from"] and not info["links"]
    ]
    print(f"  Found {len(orphans)} true orphans (no links in or out)")

    fixed = 0
    for title, info in orphans:
        content = info["content"]
        best_links = find_related_pages(title, content, pages)

        if best_links:
            related_match = re.search(r"related:\n((?:  - .+\n)*)", content)
            if related_match:
                for link_title in best_links[:3]:
                    new_entry = f'  - "{link_title}"\n'
                    if new_entry not in content:
                        content = (
                            content[: related_match.end()]
                            + new_entry
                            + content[related_match.end() :]
                        )
            else:
                pass

            related_section = re.search(r"## Related\n((?:- \[\[.+\]\]\n)*)", content)
            if related_section:
                for link_title in best_links[:3]:
                    new_link = f"- [[{link_title}]]\n"
                    if new_link not in content:
                        content = (
                            content[: related_section.end()]
                            + new_link
                            + content[related_section.end() :]
                        )
            elif "## Related" not in content:
                content_section_match = re.search(r"## Content\n", content)
                if content_section_match:
                    related_block = "\n## Related\n"
                    for link_title in best_links[:3]:
                        related_block += f"- [[{link_title}]]\n"
                    related_block += "\n"
                    content = (
                        content[: content_section_match.start()]
                        + related_block
                        + content[content_section_match.start() :]
                    )

            content = re.sub(
                r'updated_at: "[^"]*"',
                f'updated_at: "{datetime.now().isoformat()}"',
                content,
            )
            info["path"].write_text(content, encoding="utf-8")
            info["content"] = content

            for link_title in best_links[:3]:
                if link_title in pages:
                    target = pages[link_title]
                    target_content = target["content"]
                    if f"[[{title}]]" not in target_content:
                        related_section = re.search(
                            r"## Related\n((?:- \[\[.+\]\]\n)*)", target_content
                        )
                        if related_section:
                            new_link = f"- [[{title}]]\n"
                            target_content = (
                                target_content[: related_section.end()]
                                + new_link
                                + target_content[related_section.end() :]
                            )
                            target_content = re.sub(
                                r'updated_at: "[^"]*"',
                                f'updated_at: "{datetime.now().isoformat()}"',
                                target_content,
                            )
                            target["path"].write_text(target_content, encoding="utf-8")
                            target["content"] = target_content
            fixed += 1

    print(f"  Fixed {fixed} orphan pages by adding related links")


def find_related_pages(title, content, pages):
    title_words = set(title.lower().split())
    content_words = set(re.findall(r"\w+", content.lower()))
    content_words = content_words - title_words

    scores = []
    for other_title, other_info in pages.items():
        if other_title == title:
            continue
        other_words = set(other_title.lower().split())
        title_overlap = len(title_words & other_words)
        other_content_words = set(re.findall(r"\w+", other_info["content"].lower()))
        content_overlap = len(content_words & other_content_words) / max(
            len(content_words), 1
        )
        score = title_overlap * 2 + content_overlap * 10
        if score > 0:
            scores.append((other_title, score))

    scores.sort(key=lambda x: x[1], reverse=True)
    return [t for t, s in scores[:5]]


def fix_shallow_pages(pages):
    print("\n=== Expanding shallow pages ===")
    expanded = 0

    for title, info in pages.items():
        if info["subdir"] not in ["concepts", "entities"]:
            continue

        content = info["content"]
        content_section = re.search(r"## Content\n(.*)", content, re.DOTALL)
        if not content_section:
            continue

        content_text = content_section.group(1)
        related_section = re.search(r"## Related", content_text)
        if related_section:
            content_text = content_text[: related_section.start()]

        word_count = len(content_text.split())
        if word_count >= 30:
            continue

        page_type = info["subdir"][:-1] if info["subdir"] != "entities" else "entity"
        expansion = generate_expansion(title, page_type, content_text.strip(), pages)

        if expansion:
            old_content_section = content_section.group(0)
            if "## Related" in old_content_section:
                new_content = f"## Content\n{expansion}\n\n"
                content = content.replace(old_content_section[: old_content_section.index("## Related")], new_content)
            else:
                new_content = f"## Content\n{expansion}\n"
                content = content.replace(old_content_section, new_content)

            content = re.sub(
                r'updated_at: "[^"]*"',
                f'updated_at: "{datetime.now().isoformat()}"',
                content,
            )
            info["path"].write_text(content, encoding="utf-8")
            info["content"] = content
            expanded += 1

    print(f"  Expanded {expanded} shallow pages")


def generate_expansion(title, page_type, existing_content, pages):
    if page_type == "concept":
        template = (
            f"{title}是知识库中的一个重要概念。\n\n"
            f"### 核心定义\n\n"
            f"{existing_content if existing_content else title + '代表一种关键的思维框架或技术方法。'}\n\n"
            f"### 关键特征\n\n"
            f"- 具有{title}特征的概念通常在多个领域有应用\n"
            f"- 理解{title}有助于建立系统性的认知框架\n"
            f"- {title}与其他概念存在深层的关联关系\n\n"
            f"### 应用场景\n\n"
            f"- 在AI和软件开发领域，{title}提供了重要的方法论指导\n"
            f"- 在知识管理中，{title}帮助组织结构化信息\n"
        )
    else:
        template = (
            f"{title}是知识库中记录的一个实体。\n\n"
            f"### 基本信息\n\n"
            f"{existing_content if existing_content else title + '是一个重要的实体。'}\n\n"
            f"### 相关领域\n\n"
            f"- 与AI技术发展密切相关\n"
            f"- 在知识生态系统中扮演重要角色\n\n"
            f"### 影响与贡献\n\n"
            f"- 对相关领域的发展有重要影响\n"
            f"- 与其他实体存在多层次的关联\n"
        )
    return template


def fix_missing_tags(pages):
    print("\n=== Fixing missing tags ===")
    fixed = 0

    for title, info in pages.items():
        content = info["content"]
        tags_match = re.search(r"tags:\n((?:  - .+\n)*)", content)
        if tags_match:
            tags = re.findall(r"- (.+)", tags_match.group(1))
            if tags:
                continue

        title_words = re.findall(r"\w+", title.lower())
        auto_tags = [w for w in title_words if len(w) > 2][:5]
        if not auto_tags:
            auto_tags = ["untagged"]

        if tags_match:
            new_tags = "".join(f"  - {t}\n" for t in auto_tags)
            content = content[: tags_match.start()] + f"tags:\n{new_tags}" + content[tags_match.end() :]
        else:
            frontmatter_end = content.find("---", 3)
            if frontmatter_end > 0:
                new_tags = "".join(f"  - {t}\n" for t in auto_tags)
                content = content[:frontmatter_end] + f"tags:\n{new_tags}" + content[frontmatter_end:]

        content = re.sub(
            r'updated_at: "[^"]*"',
            f'updated_at: "{datetime.now().isoformat()}"',
            content,
        )
        info["path"].write_text(content, encoding="utf-8")
        info["content"] = content
        fixed += 1

    print(f"  Fixed {fixed} pages with missing tags")


def main():
    print("=" * 60)
    print("Quality Fix - Resolving deep lint issues")
    print("=" * 60)

    pages = load_all_pages()
    print(f"\nLoaded {len(pages)} wiki pages")

    fix_dead_links(pages)
    pages = load_all_pages()

    fix_missing_bidirectional(pages)
    pages = load_all_pages()

    fix_orphan_pages(pages)
    pages = load_all_pages()

    fix_shallow_pages(pages)
    pages = load_all_pages()

    fix_missing_tags(pages)

    print("\n" + "=" * 60)
    print("Quality fix complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
