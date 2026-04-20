---
title: "RAG (Retrieval-Augmented Generation)"
type: "concept"
sources:
  - "wiki/sources/zhihu-discussion-why-ai-agents-underperform-in-practice-and-intelligent-rag-solutions.md"
  - "wiki/sources/karpathy-llm-knowledge-base-architecture.md"
tags:
  - "ai-architecture"
  - "knowledge-retrieval"
  - "generation"
  - "search"
confidence: "high"
created_at: "2026-04-17T21:56:25.442155"
updated_at: "2026-04-20T12:00:00"
---

# RAG (Retrieval-Augmented Generation)

检索增强生成是将信息检索与文本生成结合的架构，通过外部知识库扩展LLM的知识边界。

## 核心要点

- **检索+生成**：先从知识库检索相关信息，再基于检索结果生成回答
- **知识扩展**：突破LLM内置知识限制，支持动态信息更新
- **智能RAG改进**：添加状态机模拟人类分析师思维流程
- **与LLM Wiki对比**：RAG是解释器模式（每次现场翻译），LLM Wiki是编译器模式（提前编译）
- **局限**：向量检索的黑盒性和难以溯源问题

## Related
- [[LLM Search over RAG]]
- [[智能RAG架构]]
- [[知识编译器模式]]
- [[karpathy-llm-knowledge-base-architecture]]
- [[zhihu-discussion-why-ai-agents-underperform-in-practice-and-intelligent-rag-solutions]]