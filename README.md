# LLM Wiki

A personal knowledge base that builds itself — LLM incrementally compiles raw documents into an interlinked wiki with bidirectional links.

Inspired by [Andrej Karpathy's LLM Wiki concept](https://x.com/karpathy): instead of manually organizing notes, let an LLM read your documents and automatically generate a structured, cross-referenced knowledge base.

## How It Works

```
┌─────────────┐     LLM      ┌─────────────────────┐
│  Raw Sources │ ──────────► │     Wiki Pages       │
│  (immutable) │   ingest    │  (LLM-generated)     │
└─────────────┘             │                       │
                            │  concepts/  entities/  │
                            │  sources/   answers/   │
                            └───────┬───────────────┘
                                    │
                              [[wikilinks]]
                                    │
                            ┌───────▼───────────────┐
                            │   Knowledge Graph      │
                            │   (bidirectional)      │
                            └───────────────────────┘
```

Three-layer architecture:

1. **Raw Sources** (`raw/`) — Your original documents. Immutable. The source of truth.
2. **Wiki** (`wiki/`) — LLM-generated markdown pages with `[[wikilinks]]`. Obsidian-compatible.
3. **Schema** (`CLAUDE.md`) — Configuration that tells the LLM how to operate.

A single source document typically generates 5-15 interlinked wiki pages.

## Quick Start

### Option A: Agent Native LLM (Zero Config)

Works with Claude Code, Trae, Cursor, or any AI coding agent — no API key needed:

```bash
# Install
pip install -e .

# Initialize (default provider is "agent")
wiki init

# Drop documents into raw/
# ...

# Process sources — the Agent provides LLM responses
wiki ingest --all
```

When `provider: agent`, the CLI writes prompts to `.wiki_llm_prompt.json` and waits for the Agent to respond via `.wiki_llm_response.json`. The Agent handles this automatically.

### Option B: External API Key

For standalone CLI usage without an Agent:

```bash
# Install
pip install -e .

# Initialize
wiki init

# Configure API key
cp .wikirc.yaml.example .wikirc.yaml
# Edit .wikirc.yaml — set provider, apiKey, baseUrl, model

# Process sources
wiki ingest --all
```

## LLM Providers

| Provider | Config | How It Works |
|----------|--------|--------------|
| **agent** (default) | `provider: agent` | Agent's native LLM handles prompts via file protocol |
| openai | `provider: openai` | LiteLLM → OpenAI API |
| deepseek | `provider: deepseek` | LiteLLM → DeepSeek API |
| anthropic | `provider: anthropic` | LiteLLM → Anthropic API |
| Any LiteLLM provider | `provider: <name>` | LiteLLM → corresponding API |

### Agent Provider Details

When `provider: agent`, there are three integration modes:

**1. stdio Callback (Recommended for Agent integration)**

Set `WIKI_LLM_CALLBACK=stdio` — prompts go to stdout as JSON, responses come from stdin as JSON. Perfect for Agent pipeline:

```bash
# Agent reads prompts from stdout, writes responses to stdin
WIKI_LLM_CALLBACK=stdio wiki ingest --all
```

Each exchange is one JSON line:
- **Output (prompt)**: `{"prompt": "...", "timestamp": 1234567890}`
- **Input (response)**: `{"response": "..."}`

**2. JSONL Batch Mode (For bulk processing)**

Set `WIKI_LLM_CALLBACK=jsonl` — all prompts are appended to `.wiki_llm_prompts.jsonl`, Agent processes them in bulk and writes `.wiki_llm_responses.jsonl`:

```bash
# Terminal 1: Run ingest (prompts accumulate in .wiki_llm_prompts.jsonl)
WIKI_LLM_CALLBACK=jsonl wiki ingest --all

# Terminal 2: Agent processes all prompts at once, then writes responses
# Or use the batch respond command:
wiki agent-respond --batch responses.jsonl
```

JSONL format (one JSON object per line, matched by `id`):
- **Prompts**: `{"id": "abc123", "prompt": "...", "model": "...", "timestamp": ...}`
- **Responses**: `{"id": "abc123", "response": "..."}`

**3. File Protocol (For manual/debug)**

The CLI writes a single prompt file and waits for a response file:

```bash
# Terminal 1: Run a wiki command (waits for response)
wiki ingest --all

# Terminal 2: Agent responds to the prompt
wiki agent-respond --file response.txt
# or interactively:
wiki agent-respond --interactive
# or batch:
wiki agent-respond --batch responses.jsonl
```

**4. Python Callback (Agent script mode)**

When the Agent imports the package directly, it can set a callback function:

```python
from llm_wiki.llm import set_llm_callback
from llm_wiki.config import load_config
from llm_wiki.ingest import ingest_source

def my_llm(prompt: str) -> str:
    # Use Agent's native LLM here
    return agent_call_llm(prompt)

set_llm_callback(my_llm)

config = load_config()
pages = ingest_source(config, source_path)
```

### Choosing an Agent Mode

| Mode | Env Var | Best For | Speed |
|------|---------|----------|-------|
| **stdio** | `WIKI_LLM_CALLBACK=stdio` | Agent pipeline, automated | ⚡ Fastest |
| **JSONL batch** | `WIKI_LLM_CALLBACK=jsonl` | Bulk processing 10+ sources | ⚡ Fast |
| **File protocol** | *(default)* | Manual debug, single prompt | 🐢 Slow (one-by-one) |
| **Python callback** | *(code only)* | Programmatic use | ⚡ Instant |

## Commands

| Command | Description |
|---------|-------------|
| `wiki init` | Initialize a new wiki |
| `wiki ingest --all` | Process all raw sources into wiki pages |
| `wiki ingest <file>` | Process a single source file |
| `wiki ingest --url <url>` | Ingest from a URL |
| `wiki query "<question>"` | Ask a question against the wiki |
| `wiki search "<query>"` | BM25 fuzzy search |
| `wiki keywords <word1> <word2>` | Exact keyword search |
| `wiki links "<page title>"` | Show wikilinks in a page |
| `wiki tokens <file>` | Estimate token count |
| `wiki lint` | Health-check for issues |
| `wiki stats` | Show wiki statistics |
| `wiki list pages` | List all wiki pages |
| `wiki list orphans` | List orphan pages |
| `wiki config --show` | View current configuration |
| `wiki config --language cn` | Set output language to Chinese |
| `wiki agent-respond` | Respond to an Agent LLM prompt |
| `wiki agent-respond --batch <file>` | Batch respond from JSONL file |

### Deep Mode

Deep mode provides enhanced knowledge extraction with bidirectional linking:

| Command | Description |
|---------|-------------|
| `wiki deep parse --source <file>` | Deep parse a single source |
| `wiki deep parse --all` | Deep parse all pending sources |
| `wiki deep query --question "..."` | Deep query with more context |
| `wiki deep lint` | Check bidirectional link integrity |
| `wiki deep stats` | Quality metrics and statistics |
| `wiki deep fix` | Auto-fix quality issues |

**Deep Parse vs Normal Ingest:**

| Feature | Normal Ingest | Deep Parse |
|---------|---------------|------------|
| Concepts extracted | 3-5 | 10-15 |
| Link direction | One-way | Bidirectional (A↔B) |
| Content depth | 2-3 sentences | 5+ sentences |
| Relationship types | None | hierarchical / complementary / opposing |
| Existing page enhancement | None | Auto-adds new links and content |

## Page Format

Every wiki page uses YAML frontmatter + markdown with Obsidian-compatible wikilinks:

```markdown
---
title: "Harness Engineering"
type: concept
sources:
  - "raw/articles/harness-engineering.md"
tags:
  - "agent"
  - "engineering"
confidence: high
created_at: "2026-04-16T12:00:00"
updated_at: "2026-04-16T12:00:00"
---

# Harness Engineering

Agent运行时的工程环境总和...

## Related
- [[Agent Loop]]
- [[Compound Engineering]]
```

## Directory Structure

```
project/
├── CLAUDE.md              ← Schema (LLM instructions)
├── .wikirc.yaml           ← LLM configuration
├── raw/
│   ├── articles/          ← Article sources
│   ├── videos/            ← Video transcript sources
│   ├── webpages/          ← Webpage sources
│   └── untracked/         ← New sources waiting to be ingested
├── wiki/
│   ├── index.md           ← Content catalog (auto-maintained)
│   ├── log.md             ← Chronological operation record
│   ├── concepts/          ← Concept pages (ideas, methods, theories)
│   ├── entities/          ← Entity pages (people, orgs, products)
│   ├── sources/           ← Source summary pages
│   └── answers/           ← Saved query answers
└── src/llm_wiki/          ← Python package
    ├── cli.py             ← CLI entry point
    ├── config.py          ← Configuration
    ├── llm.py             ← Unified LLM interface (agent + API)
    ├── ingest.py          ← Source ingestion
    ├── deep.py            ← Deep mode logic
    ├── fix.py             ← Quality fix logic
    ├── lint.py            ← Health check
    ├── query.py           ← Question answering
    ├── search.py          ← BM25 search
    ├── schema.py          ← Page schema
    └── utils.py           ← Utilities
```

## Configuration

`.wikirc.yaml`:

```yaml
language: as_origin  # cn (Chinese) | en (English) | as_origin (follow source)
llm:
  provider: agent  # agent (native Agent LLM) | openai | deepseek | anthropic | etc.
  # For API providers, uncomment:
  # model: deepseek-chat
  # apiKey: 'your-api-key'
  # baseUrl: https://api.deepseek.com/v1
  temperature: 0.3
  max_tokens: 8192
```

## Quality Tools

### Lint

`wiki lint` and `wiki deep lint` detect:

- **Dead links** — `[[wikilinks]]` pointing to non-existent pages
- **Orphan pages** — Pages with no inbound links
- **Shallow pages** — Pages with less than 30 words
- **Missing concepts** — Terms mentioned but not linked
- **Missing bidirectional links** — A→B exists but B→A doesn't

### Fix

`wiki deep fix` automatically resolves:

- Dead links → redirected to best match or removed
- Missing bidirectional links → adds reverse links
- Orphan pages → adds related links based on content similarity
- Shallow pages → expands with structured content
- Missing tags → auto-generates from title

## Obsidian Integration

The wiki is fully Obsidian-compatible:

- Wikilinks (`[[Page Title]]`) work out of the box
- Graph view shows the knowledge network
- Backlinks panel shows all references
- YAML frontmatter is parsed as properties

## Requirements

- Python 3.11+
- Either an AI coding agent (Claude Code, Trae, Cursor) or an LLM API key

## License

MIT
