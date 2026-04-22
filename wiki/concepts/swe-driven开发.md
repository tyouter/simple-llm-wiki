---
title: "SWE Driven开发"
type: "concept"
sources:
  - "raw/articles/2b36f099_claude.md怎么写才能让Claude Code更高效claude.md怎么写才能让Claude Code更高效.md"
tags:
  - "方法论"
  - "研究前沿"
  - "自动化"
confidence: "high"
created_at: "2026-04-21T14:48:09.178943"
updated_at: "2026-04-21T14:48:09.178943"
related:
  - "Agent-First Development"
  - "Agent协作与任务拆分"
  - "Benchmark vs. Engineering Reality Gap"
  - "Spec Coding"
  - "SWE-agent"
  - "yahah"
---

该方法源自[[SWE-agent]]等研究，核心是将写代码的流程从以人类为中心重新设计为以智能体为中心。它是[[Agent-First Development]]的同义表述，强调结果导向的验证。

实验流程包括：给定Issue描述，Agent被放入代码仓库，需要自己定位Bug、修改代码，最终通过真实的单元测试来验证。它强调“不看生成的代码像不像，只看最终能不能通过测试”，这与[[Spec Coding]]的理念一致，但更加自动化。

[[Agent协作与任务拆分]]是SWE Driven开发的重要实践模式，通过分工协作提高复杂任务的处理能力。然而，这种方法也面临[[Benchmark vs. Engineering Reality Gap]]的挑战——基准测试环境与真实工程环境存在差异。[[yahah]]在讨论中提到了这种方法的潜力，认为它代表了AI编程的未来方向。

## Related
- [[Agent-First Development]]
- [[Agent协作与任务拆分]]
- [[Benchmark vs. Engineering Reality Gap]]
- [[Spec Coding]]
- [[SWE-agent]]
- [[yahah]]