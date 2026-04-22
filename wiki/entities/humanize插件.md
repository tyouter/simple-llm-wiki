---
title: "Humanize插件"
type: "entity"
sources:
  - "raw/articles/2b36f099_claude.md怎么写才能让Claude Code更高效claude.md怎么写才能让Claude Code更高效.md"
tags:
  - "工具"
  - "插件"
  - "质量保证"
confidence: "high"
created_at: "2026-04-21T14:48:09.247477"
updated_at: "2026-04-21T14:48:09.247477"
related:
  - "工具链与插件生态"
  - "概率性提示词局限"
  - "Spec Coding"
  - "Agent协作与任务拆分"
  - "yahah"
  - "Superpowers插件"
---

一个利用迭代反馈循环的插件：Claude执行计划，Codex独立审查进展，及早发现问题并解决，直到满足所有验收标准。

Humanize插件是[[工具链与插件生态]]的关键组成部分，专门用于解决[[概率性提示词局限]]带来的质量问题。它是[[Spec Coding]]的一种具体实现模式，通过自动化审查流程确保代码符合规格说明。

该插件的工作流程体现了[[Agent协作与任务拆分]]的思想：一个Agent负责执行，另一个Agent负责审查，两者协作完成高质量的输出。这与[[yahah]]倡导的严谨开发方法高度一致，都强调验证和迭代的重要性。

Humanize插件与[[Superpowers插件]]互补：Superpowers提供技能框架和自主决策能力，Humanize提供质量保证机制。两者结合使用可以构建从规划到验证的完整AI编程工作流，减少对单一概率性提示词的依赖，提高输出的确定性和可靠性。

## Related
- [[工具链与插件生态]]
- [[概率性提示词局限]]
- [[Spec Coding]]
- [[Agent协作与任务拆分]]
- [[yahah]]
- [[Superpowers插件]]