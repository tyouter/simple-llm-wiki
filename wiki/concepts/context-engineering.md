---
title: "Context Engineering"
type: "concept"
sources:
  - "wiki/sources/harness-engineering-explained-from-agent-loop-to-production-system-zhihu-discussion.md"
  - "wiki/sources/anthropic-skills-engineering-approach-to-agent-capability-development.md"
tags:
  - "prompt-engineering"
  - "context-management"
  - "agent-architecture"
confidence: "high"
created_at: "2026-04-19T01:52:16.569131"
updated_at: "2026-04-20T16:00:00"
---

# Context Engineering (上下文工程)

## 概述
上下文工程是Harness Engineering的子集，专注于设计和优化AI Agent的上下文环境，包括信息分层加载、token效率和上下文污染管理等技术。

## 核心要点
- **Harness Engineering子集**：作为Harness Engineering的核心组成部分，专注于上下文层面
- **Progressive Disclosure**：渐进式信息披露，分层加载信息（catalog -> instructions -> resources）
- **分布式上下文管理**：使用多个清洁的上下文窗口配合定期摘要，克服token限制
- **上下文污染**：Context Pollution是需要避免的问题，防止无关信息干扰Agent决策
- **Effort Budgeting**：指导Agent在不同任务复杂度上分配计算资源的机制
- **Token效率**：优化上下文使用，减少不必要的token消耗

## 相关概念
- [[Harness Engineering]]
- [[Progressive Disclosure]]
- [[Distributed Context Management]]
- [[Context Pollution]]
- [[Agent Memory Systems]]
- [[Token Efficiency in AI Reasoning]]

## 相关实体
- [[OpenAI]]
- [[DeepSeek]]
- [[Anthropic]]
- [[mCell]]

## 来源
- [src: Harness Engineering Explained: From Agent Loop to Production System]
- [src: Anthropic Skills: Engineering Approach to Agent Capability Development]