---
title: "CLAUDE.md"
type: "concept"
sources:
  - "raw/articles/12be559f_claude.md怎么写才能让Claude Code更高效claude.md怎么写才能让Claude Code更高效.md"
tags:
  - "claude-code"
  - "configuration"
  - "prompt-engineering"
  - "persistent-memory"
  - "documentation"
confidence: "high"
created_at: "2026-04-17T21:42:57.894466"
updated_at: "2026-04-17T21:42:57.894466"
related:
  - "Persistent Memory System (Claude Code)"
  - "Auto Memory"
  - "Spec Coding vs. Vibe Coding"
  - "Permission Modes (Claude Code)"
  - "白玉京"
  - "yahah"
---

# CLAUDE.md

## Definition
A user-written "permanent manual" file that [[Claude Code]] automatically reads at the start of each coding session. It serves as the cornerstone of Claude's [[Persistent Memory System (Claude Code)]], providing project-specific rules, coding standards, architectural context, and developer preferences to mitigate "session amnesia."

## Purpose and Function
- **Cross-Session Memory**: Provides consistent context across different chat sessions and workdays.
- **Project Specification**: Defines the project's purpose, structure, key files, and dependencies.
- **Coding Standards**: Enforces style guides, naming conventions, and architectural patterns (e.g., MVC, Clean Architecture).
- **Workflow Rules**: Instructs Claude on preferred processes, such as always creating a plan before coding or using specific testing frameworks.
- **Personal Preferences**: Captures developer idiosyncrasies (e.g., "I prefer early returns," "Avoid comments that state the obvious").

## Content and Structure
A CLAUDE.md file typically includes sections such as:
1.  **Project Overview**: Brief description of the project's goal and tech stack.
2.  **Project Structure**: Explanation of key directories and their purposes.
3.  **Coding Rules & Conventions**: Language-specific standards and patterns to follow/avoid.
4.  **Workflow Instructions**: How to approach tasks (e.g., "Always start with a `/plan`").
5.  **Communication Style**: How to explain changes or ask questions.

## Philosophical Debate
As highlighted in the [[Zhihu Discussion: Optimizing Claude Code with CLAUDE.md and Efficient Development Workflows]], there is significant controversy over the optimal length and detail of a CLAUDE.md file:
- **Comprehensive Approach**: Advocates (like [[白玉京]]) suggest detailed files (150-200 lines) to leave no ambiguity for the AI.
- **Minimalist Approach**: Advocates (like [[yahah]] and [[笙囧同学]]) argue for extreme brevity (~50-800 words), believing overly long files reduce effectiveness and that clarity should be enforced through external workflows like [[Spec Coding vs. Vibe Coding|Spec Coding]].

## Best Practices (Synthesized)
1.  Place it in the project root directory.
2.  Start with the most critical, high-impact rules.
3.  Use clear, imperative language.
4.  Structure it for easy scanning with headers.
5.  Iterate based on observed AI behavior—add rules to correct mistakes, remove ones that are never used.
6.  Consider complementing it with a `.claude/rules/` directory for more granular, reusable instruction sets.

## Related Concepts
- [[Persistent Memory System (Claude Code)]]: The broader system CLAUDE.md is part of.
- [[Auto Memory]]: Claude's feature to automatically supplement CLAUDE.md with learned habits.
- [[Spec Coding vs. Vibe Coding]]: The disciplined development methodology a well-crafted CLAUDE.md often aims to enforce.
- [[Permission Modes (Claude Code)]]: Configuration that affects how Claude interacts with files, including reading the CLAUDE.md.

## Related
- [[Persistent Memory System (Claude Code)]]
- [[Auto Memory]]
- [[Spec Coding vs. Vibe Coding]]
- [[Permission Modes (Claude Code)]]
- [[白玉京]]
- [[yahah]]