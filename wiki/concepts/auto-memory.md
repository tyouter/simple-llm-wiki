---
title: "Auto Memory"
type: "concept"
sources:
  - "raw/articles/12be559f_claude.md怎么写才能让Claude Code更高效claude.md怎么写才能让Claude Code更高效.md"
tags:
  - "claude-code"
  - "machine-learning"
  - "adaptation"
  - "persistent-memory"
confidence: "high"
created_at: "2026-04-17T21:42:57.896032"
updated_at: "2026-04-17T21:42:57.896032"
related:
  - "Persistent Memory System (Claude Code)"
  - "CLAUDE.md"
  - "Permission Modes (Claude Code)"
  - "/memory 命令"
  - "会话失忆"
  - "yahah"
---

# Auto Memory

## Definition
A feature within [[Claude Code]]'s [[Persistent Memory System (Claude Code)]] where the AI automatically learns, records, and recalls user habits, problem solutions, project-specific nuances, and developer corrections from ongoing interactions. It functions as a dynamic, self-populating knowledge base that supplements the static [[CLAUDE.md]] file.

## Function and Purpose
- **Mitigates Repetition**: Remembers solutions to previously encountered errors or complex implementation patterns, so the user doesn't have to re-explain them.
- **Captures "Gotchas"**: Learns project-specific quirks, such as "API X always times out, so wrap it in a retry logic."
- **Adapts to Style**: Observes and internalizes developer preferences that may not be explicitly written in CLAUDE.md (e.g., a tendency to refactor a certain way after feature completion).
- **Builds Institutional Knowledge**: Over time, creates a valuable repository of how this particular project is built and maintained.

## How It Is Triggered
Claude identifies moments worth remembering, such as:
- Successfully debugging a non-obvious issue.
- The user providing a significant correction or refinement to Claude's output.
- Repeating a specific, complex task pattern.
- Explanations of why a certain architectural decision was made.

## Relationship to CLAUDE.md
- **CLAUDE.md is Proactive, Auto Memory is Reactive**: CLAUDE.md provides upfront rules; Auto Memory learns from what happens during development.
- **CLAUDE.md is Static, Auto Memory is Dynamic**: The manual is edited by the user; the memory grows organically through use.
- **They are Complementary**: A well-set CLAUDE.md sets the stage, and Auto Memory fills in the details through experience.

## Philosophical Considerations
In the debate highlighted in [[Zhihu Discussion: Optimizing Claude Code with CLAUDE.md and Efficient Development Workflows]], the role of Auto Memory is interpreted differently:
- **Pro-Comprehensive Guide View**: Auto Memory is a helpful supplement to a detailed manual, catching edge cases.
- **Pro-Minimalist View**: Auto Memory can be relied upon more heavily, reducing the need for an exhaustive upfront CLAUDE.md, as the AI will learn the important details through collaboration.

## Best Practices
1.  Allow it to function—avoid over-restricting Claude's permissions if you want it to learn.
2.  Periodically review what has been stored (if the interface allows) to ensure accuracy.
3.  Understand that it is not a perfect recall system and critical information should still be codified in CLAUDE.md or documentation.

## Related Concepts
- [[Persistent Memory System (Claude Code)]]: The overarching system.
- [[CLAUDE.md]]: The complementary static memory component.
- [[Permission Modes (Claude Code)]]: Settings that may affect Auto Memory's ability to write data.

## Related
- [[Persistent Memory System (Claude Code)]]
- [[CLAUDE.md]]
- [[Permission Modes (Claude Code)]]

---

## Additional Insights


## 局限性与管理
虽然 [[自动记忆]] 能有效学习习惯，但它也可能记录错误或过时的信息。用户应定期使用 [[/memory命令]] 进行检查和清理。此外，[[yahah]] 所倡导的 [[Spec Coding vs Vibe Coding]] 工作流，在一定程度上减少了对 AI “自行学习”模糊习惯的依赖，转而依靠人类明确编写的 [[Plan]] 和规格，这可能使得自动记忆的角色在高度规范化的项目中有所减弱。理解自动记忆的适用场景（学习个人微偏好、项目特定坑点）和局限（不适合学习复杂架构决策），是有效利用 [[持久记忆体系]] 的关键。

Source: [[raw/articles/12be559f_claude.md怎么写才能让Claude Code更高效claude.md怎么写才能让Claude Code更高效.md]]

## Related
- [[Persistent Memory System (Claude Code)]]
- [[CLAUDE.md]]
- [[Permission Modes (Claude Code)]]
- [[/memory 命令]]
- [[会话失忆]]
- [[yahah]]