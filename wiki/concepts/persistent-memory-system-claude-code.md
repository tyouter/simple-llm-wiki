---
title: "Persistent Memory System (Claude Code)"
type: "concept"
sources:
  - "raw/articles/12be559f_claude.md怎么写才能让Claude Code更高效claude.md怎么写才能让Claude Code更高效.md"
tags:
  - "claude-code"
  - "memory"
  - "context-management"
  - "ai-assisted-development"
confidence: "high"
created_at: "2026-04-17T21:42:57.894466"
updated_at: "2026-04-17T21:42:57.894466"
related:
  - "CLAUDE.md"
  - "Auto Memory"
  - "Permission Modes (Claude Code)"
  - "Spec Coding vs. Vibe Coding"
---

# Persistent Memory System (Claude Code)

## Definition
The integrated suite of features in [[Claude Code]] designed to retain project context, developer preferences, and learned problem-solving approaches across different coding sessions. This system directly addresses the "session amnesia" limitation common to AI coding assistants.

## Core Components
The system is built on three pillars:

1.  **[[CLAUDE.md]]**: The user-authored, static "constitution" for a project. It provides the foundational rules, architecture, and standards that Claude reads at every session start.
2.  **Rules Files**: Optional, granular instruction files stored in a `.claude/rules/` directory. These allow for modular, reusable sets of instructions (e.g., `react_rules.md`, `testing_rules.md`) that can be referenced or combined across projects.
3.  **[[Auto Memory]]**: The dynamic, AI-generated component. Claude automatically records significant patterns, solved problems, developer corrections, and project-specific "gotchas" from interactions, building a living knowledge base that supplements the static CLAUDE.md.

## How It Works
1.  **Session Initialization**: When Claude Code starts in a project, it first reads the `CLAUDE.md` file to load the primary context.
2.  **Rule Application**: It may load additional rules from the `.claude/rules/` directory if referenced or configured to do so.
3.  **Auto-Memory Recall**: Throughout the session, Claude queries its stored auto-memory for relevant past solutions or warnings related to the current task.
4.  **Learning & Storage**: As work progresses, Claude identifies and stores new insights into the auto-memory for future use.

## Configuration and Philosophy
As discussed in the [[Zhihu Discussion: Optimizing Claude Code with CLAUDE.md and Efficient Development Workflows]], users configure and prioritize these components differently:
- Some rely heavily on a detailed, manually crafted `CLAUDE.md`.
- Others prefer a minimalist `CLAUDE.md` and depend more on `Auto Memory` to learn organically.
- The use of `Rules Files` allows for sophisticated, modular configuration but adds complexity.

The system's effectiveness is also intertwined with [[Permission Modes (Claude Code)]], which control Claude's ability to read and write these memory files.

## Related Concepts
- [[CLAUDE.md]]: The foundational manual component.
- [[Auto Memory]]: The self-learning component.
- [[Permission Modes (Claude Code)]]: Security settings affecting system access.
- [[Spec Coding vs. Vibe Coding]]: A methodology the memory system often aims to support.

## Related
- [[CLAUDE.md]]
- [[Auto Memory]]
- [[Permission Modes (Claude Code)]]
- [[Spec Coding vs. Vibe Coding]]