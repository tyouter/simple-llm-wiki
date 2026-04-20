---
title: "Subagents for Context Efficiency"
type: "concept"
sources:
  - "wiki/sources/advanced-claude-code-workflow-techniques-and-architecture-analysis.md"
tags:
  - "claude-code"
  - "context-management"
  - "agent-architecture"
  - "efficiency"
confidence: "high"
created_at: "2026-04-18T00:50:51.015027"
updated_at: "2026-04-20T12:00:00"
---

# Subagents for Context Efficiency

Claude Code 中用于保护主上下文的子代理机制，通过将研究任务委托给独立的子代理，避免主会话的上下文污染。

## 核心要点

- **上下文隔离**: 子代理拥有独立、干净的上下文窗口，执行任务后只返回摘要结果
- **保护主上下文**: 避免大量原始数据（如日志、代码片段）填满主会话的 token 额度
- **任务委托**: 适用于需要大量阅读但不修改的任务，如代码审查、日志分析、文档阅读
- **单循环架构约束**: Claude Code 设计中限制最多一个子代理分支，优先保证可调试性
- **定期摘要**: 子代理完成后返回精炼摘要而非原始输出，保持主上下文整洁

## Related

- [[Claude Code子代理]]
- [[Context Window Management]]
- [[Single-Loop Architecture]]
- [[Claude Code]]
- [[Agentic Loop]]