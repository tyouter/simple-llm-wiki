# CLAUDE.md — LLM Wiki Schema

This document tells the LLM how the wiki is structured, what conventions to follow, and what workflows to use. This is the Schema layer — the key configuration that makes the LLM a disciplined wiki maintainer.

## Architecture

Three layers:

1. **Raw Sources** (`raw/`) — Immutable source documents. The LLM reads but never modifies these. This is the source of truth.
2. **Wiki** (`wiki/`) — LLM-generated markdown files. The LLM owns this layer entirely. You read it; the LLM writes it.
3. **Schema** (`CLAUDE.md`) — This file. Tells the LLM how to operate.

## Directory Structure

```
llm-wiki/
├── CLAUDE.md              ← This file (schema)
├── .wikirc.yaml           ← LLM configuration
├── raw/
│   ├── untracked/         ← New sources waiting to be ingested
│   │   └── YYYY/MM/DD/   ← Organized by date
│   └── ingested/          ← Sources that have been processed
│       └── YYYY/MM/DD/
└── wiki/
    ├── index.md           ← Content catalog (auto-maintained)
    ├── log.md             ← Chronological operation record
    ├── overview.md        ← Evolving synthesis of all knowledge
    ├── concepts/          ← Concept pages (ideas, methods, theories)
    ├── entities/          ← Entity pages (people, orgs, products)
    ├── sources/           ← Source summary pages
    └── answers/           ← Saved query answers
```

## Page Format

Every wiki page uses YAML frontmatter + markdown:

```markdown
---
title: "Page Title"
type: concept | entity | source | answer
sources:
  - "path/to/source.md"
tags:
  - "tag1"
  - "tag2"
confidence: high | medium | low
created_at: "2026-04-16T12:00:00"
updated_at: "2026-04-16T12:00:00"
---

# Page Title

Content here...

## Related
- [[OtherPage]]
- [[AnotherConcept]]
```

## Cross-Reference Convention

- Use `[[PageTitle]]` for wiki-internal links (Obsidian-compatible wikilinks)
- Every page that mentions a concept or entity should link to it
- Pages should have a `## Related` section listing connected pages

## Operations

### Ingest

When adding a new source:

1. Read the source document
2. Read `wiki/index.md` to understand existing knowledge
3. Use BM25 search to find related wiki pages
4. Analyze: identify key entities, concepts, arguments, connections, contradictions
5. Generate wiki pages:
   - One **source page** summarizing the document
   - Multiple **concept pages** for key ideas (update if exists)
   - Multiple **entity pages** for key entities (update if exists)
6. Update `wiki/index.md` with new entries
7. Append entry to `wiki/log.md`
8. Move source from `raw/untracked/` to `raw/ingested/`

A single source typically touches 5-15 wiki pages.

### Query

When answering a question:

1. Read `wiki/index.md` to find relevant pages
2. Use BM25 search to retrieve top pages
3. Optionally dive into source files for deeper detail
4. Synthesize an answer with citations: `[src: PageTitle]`
5. If the answer is novel (combines multiple sources), save it as a new wiki page

### Lint

Periodically health-check the wiki:

- **Orphan pages** — pages with no inbound links
- **Dead links** — `[[wikilinks]]` pointing to non-existent pages
- **Shallow pages** — pages with less than 30 words
- **Missing concepts** — terms mentioned but not linked
- **Contradictions** — conflicting claims across pages
- **Stale claims** — outdated information superseded by newer sources

## Index Format

`wiki/index.md` is organized by category:

```markdown
# Wiki Index

## Concepts
- [[ConceptName]] — one-line summary

## Entities
- [[EntityName]] — one-line summary

## Sources
- [[SourceName]] — one-line summary

## Answers
- [[AnswerTitle]] — one-line summary
```

## Log Format

`wiki/log.md` uses parseable headers:

```markdown
## [2026-04-16] ingest | Article Title — 8 pages created/updated
## [2026-04-16] query | What is X?
## [2026-04-16] lint | 3 issues found
```

This format enables: `grep "^## \[" log.md | tail -5` to see recent activity.

## Tags Convention

- Lowercase with hyphens: `machine-learning`, `transformer-architecture`
- Include domain tags: `nlp`, `cv`, `rl`
- Include type tags: `paper`, `article`, `tutorial`, `concept`, `method`

## Confidence Levels

- **high** — well-established, multiple sources agree
- **medium** — supported by evidence but could change
- **low** — speculative, single source, or contradicted

## Tips

- The wiki is a git repo — version history is free
- Obsidian is the recommended viewer (graph view, backlinks, search)
- Use `wiki stats` to monitor wiki growth
- Run `wiki lint` regularly to keep the wiki healthy
- When in doubt, create a new page rather than overloading an existing one
