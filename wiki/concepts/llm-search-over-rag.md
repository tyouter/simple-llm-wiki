---
title: "LLM Search over RAG"
type: "concept"
sources:
  - "wiki/sources/Claude Code工作流技术与架构分析.md"
  - "wiki/sources/advanced-claude-code-workflow-techniques-and-architecture-analysis.md"
  - "wiki/sources/karpathy-llm-knowledge-base-architecture.md"
tags:
  - "claude-code"
  - "search-strategy"
  - "rag"
  - "knowledge-management"
confidence: "high"
created_at: "2026-04-18T00:50:51.014028"
updated_at: "2026-04-20T12:00:00"
---

# LLM Search over RAG

Claude Code的设计理念：让模型自行决定如何搜索而非依赖僵化的RAG系统，配合精心设计的工具（Bash、Edit、Grep）进行知识探索。

## 核心要点

- **自主搜索**：LLM决定搜索策略而非预设检索流程
- **工具组合**：Bash、Edit、Grep等工具提供灵活探索能力
- **优于僵化RAG**：避免向量检索的黑盒和不可溯源问题
- **编译器模式类比**：区别于每次现场翻译的解释器模式RAG
- **知识复利**：搜索过程积累的结构化知识可供后续复用

## Related
- [[RAG Retrieval-Augmented Generation]]
- [[Claude Code]]
- [[Single-Loop Architecture]]
- [[知识编译器模式]]
- [[karpathy-llm-knowledge-base-architecture]]