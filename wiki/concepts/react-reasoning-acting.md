---
title: "ReAct (Reasoning + Acting)"
type: "concept"
sources:
  - "wiki/sources/知乎讨论-怎么成为一个AI Agent工程师.md"
tags:
  - "agent-pattern"
  - "reasoning"
  - "acting"
  - "agentic-loop"
confidence: "high"
created_at: "2026-04-20T00:24:41.161868"
updated_at: "2026-04-20T12:00:00"
---

# ReAct (Reasoning + Acting)

ReAct是AI Agent的核心执行模式，将推理与行动交替进行，实现目标导向的迭代问题解决。

## 核心要点

- **推理-行动循环**：先思考推理，再执行行动，持续迭代
- **状态管理**：维护执行计划、中间步骤、验证历史等状态
- **规划器-执行器架构**：规划师制定计划，工具执行器按计划调用
- **自我验证**：审计员节点检查结果质量，低评分触发重新规划
- **Agent工程师必修**：成为AI Agent工程师的第一步理解

## Related
- [[Agentic Loop]]
- [[Claude Code]]
- [[Agent Skills框架]]
- [[知乎讨论-怎么成为一个AI Agent工程师]]
- [[智能RAG架构]]