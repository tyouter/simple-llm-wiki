---
title: "Humanize 工作流"
type: "concept"
sources:
  - "raw/articles/12be559f_claude.md怎么写才能让Claude Code更高效claude.md怎么写才能让Claude Code更高效.md"
tags:
  - "工作流"
  - "迭代开发"
  - "人机协作"
  - "自动化"
confidence: "high"
created_at: "2026-04-21T18:22:23.256922"
updated_at: "2026-04-23T00:42:20.301417"
related:
  - "Spec Coding vs Vibe Coding"
  - "Plan"
  - "yahah"
  - "Humanize"
  - "知乎讨论：claude.md怎么写才能让Claude Code更高效"
---

一种利用迭代反馈循环的 AI 辅助开发方法，由工具 [[Humanize]] 实现，其概念由 [[yahah]] 引入。核心是让一个 AI（如 Claude）执行 [[Plan]]，另一个 AI（如 Codex）独立审查，人类在循环中提供反馈。它不追求一次性产出完美代码，而是通过“执行-审查-反馈”的快速循环来逐步推进工作。这种模式旨在及早发现问题，并持续工作直到满足所有验收标准。[[yahah]] 还描述了一种“双开窗口”的高强度使用模式，让人类时间被完全利用（白天双开 Claude 窗口协作，晚上用 Spec 启动自动化任务）。这种工作流体现了 [[Spec Coding vs. Vibe Coding]] 的理念，旨在实现高效、可控的人机协作。

## Related
- [[Spec Coding vs. Vibe Coding]]
- [[Plan]]
- [[yahah]]
- [[知乎讨论：claude.md怎么写才能让Claude Code更高效]]
- [[Humanize]]