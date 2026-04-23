---
title: "Permission Modes (Claude Code)"
type: "concept"
sources:
  - "raw/articles/12be559f_claude.md怎么写才能让Claude Code更高效claude.md怎么写才能让Claude Code更高效.md"
tags:
  - "claude-code"
  - "security"
  - "configuration"
  - "workflow"
confidence: "high"
created_at: "2026-04-17T21:42:57.896560"
updated_at: "2026-04-22T23:50:18.499485"
related:
  - "Persistent Memory System (Claude Code)"
  - "CLAUDE.md"
  - "Spec Coding vs. Vibe Coding"
  - "白玉京"
---

# Permission Modes (Claude Code)

## Definition
Configurable security and interaction levels in [[Claude Code]] that determine the degree of autonomy the AI has when performing actions such as reading files, editing code, executing terminal commands, or running plans. These modes balance developer control against workflow fluidity.

## Common Modes and Their Effects
As detailed in the [[Zhihu Discussion: Optimizing Claude Code with CLAUDE.md and Efficient Development Workflows]], users can configure modes that change Claude's behavior:

1.  **default / acceptEdits**: The standard mode. Claude asks for explicit confirmation before editing any existing file. This is safe but can interrupt flow.
2.  **plan**: A mode where Claude operates primarily by generating and executing step-by-step plans (`/plan` command). It may have specific permissions within the context of an approved plan.
3.  **auto**: A more permissive mode where Claude can directly edit files (often within a certain scope or file type) without asking for confirmation each time, significantly speeding up iterative tasks.
4.  **bypassPermissions**: A highly permissive mode (use with caution) that removes most guardrails, allowing Claude to read, edit, and execute commands freely. Suitable for highly trusted environments or automated tasks.

## Purpose and Strategic Use
- **Security vs. Speed Trade-off**: More restrictive modes (default) prevent accidental changes; more permissive modes (auto) enable rapid prototyping and refactoring.
- **Workflow Specialization**: Switching to `plan` mode when doing high-level architecture, or `auto` mode when implementing a well-specified component.
- **Memory System Interaction**: Permissions affect Claude's ability to read ([[CLAUDE.md]]) and write ([[Auto Memory]]) to its [[Persistent Memory System (Claude Code)]].

## Configuration Philosophy
The optimal setting is subjective and ties into the broader workflow debate:
- **Cautious/Comprehensive Workflow**: May prefer `default` or `plan` mode, relying on detailed specs and manual approval for each change.
- **Fluid/Minimalist Workflow**: May prefer `auto` mode for trusted projects, relying on clear communication (via [[Spec Coding vs. Vibe Coding|Spec Coding]]) and version control as the safety net, rather than constant confirmations.

## Best Practices
1.  Start with a restrictive mode (`default`) when exploring a new project or tool.
2.  Adjust the mode based on the task: planning, safe editing, or rapid development.
3.  Never use highly permissive modes (`bypassPermissions`) on critical or unfamiliar codebases without other safeguards.
4.  Remember that permissions are a tool to shape the collaboration dynamic, not just a security setting.

## Related Concepts
- [[Persistent Memory System (Claude Code)]]: Permission modes control access to this system.
- [[Spec Coding vs. Vibe Coding]]: The chosen methodology may influence which permission mode feels most natural.
- [[CLAUDE.md]]: The file whose reading is governed by these permissions.

## Related
- [[Persistent Memory System (Claude Code)]]
- [[CLAUDE.md]]
- [[白玉京]]
- [[Spec Coding vs. Vibe Coding]]