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
  - "持久记忆体系"
  - "上下文窗口"
  - "笙囧同学"
  - "Spec Coding vs Vibe Coding"
  - "会话失忆"
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

---

## Additional Insights


## 不同实践哲学
在[[Claude Code高效配置与开发实践指南]]的讨论中，出现了三种不同的CLAUDE.md编写哲学：

### 详尽规范派（[[白玉京]]）
- 建议控制在200行以内
- 提供详细的结构化示例
- 强调全面覆盖项目规则
- 适合需要严格规范的团队

### 核心共识派（[[yahah]]）
- 追求极致简洁
- 提供高度凝练的哲学化示例
- 强调只记录最核心共识
- 适合小型团队或个人项目

### 实践精简派（[[笙囧同学]]）
- 从"三千字砍到八百字"的经验出发
- 强调"短"为第一原则
- 定位为"共识备忘录"而非"规则手册"
- 基于实际使用体验持续迭代

## 与上下文窗口的平衡
所有答主都强调[[上下文窗口]]对CLAUDE.md长度的约束。过长的文件会挤占分析当前代码的空间，可能导致"context fail"。最佳实践是根据项目复杂度动态调整，在信息完整性和上下文效率间找到平衡点。

Source: [[raw/articles/12be559f_claude.md怎么写才能让Claude Code更高效claude.md怎么写才能让Claude Code更高效.md]]

## Related
- [[Persistent Memory System (Claude Code)]]
- [[Auto Memory]]
- [[Spec Coding vs. Vibe Coding]]
- [[Permission Modes (Claude Code)]]
- [[白玉京]]
- [[yahah]]
- [[持久记忆体系]]
- [[上下文窗口]]
- [[笙囧同学]]

---

## Additional Insights


## 关于内容长度的争议
对于 [[CLAUDE.md]] 的理想长度和内容，存在不同观点。[[白玉京]] 提供了详细的模板并建议控制在200行以内，以确保在 [[上下文窗口]] 中的有效性。而 [[yahah]] 则强烈反对套用空泛的长篇模板，分享了自己从3000字精简到800字的经验，强调只写最关键、最可能被 AI 使用的信息，认为过长的规则会被忽略。这反映了在“提供全面指导”与“追求极致注意力聚焦”之间的权衡，也间接关联到 [[Spec Coding vs Vibe Coding]] 的方法论选择——一个详细的 Spec 可能更适合放在项目文档中，而非全部塞入 CLAUDE.md。

Source: [[raw/articles/12be559f_claude.md怎么写才能让Claude Code更高效claude.md怎么写才能让Claude Code更高效.md]]

## Related
- [[Persistent Memory System (Claude Code)]]
- [[Auto Memory]]
- [[Spec Coding vs. Vibe Coding]]
- [[Permission Modes (Claude Code)]]
- [[白玉京]]
- [[yahah]]
- [[持久记忆体系]]
- [[上下文窗口]]
- [[笙囧同学]]
- [[Spec Coding vs Vibe Coding]]
- [[会话失忆]]