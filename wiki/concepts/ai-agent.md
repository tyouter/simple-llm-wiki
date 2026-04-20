---
title: "AI Agent"
type: "concept"
sources:
  - "wiki/sources/claude-code-agent-technical-analysis-and-multi-agent-architecture.md"
  - "wiki/sources/zhihu-discussion-ai-agent-engineering-career-paths-and-technical-approaches.md"
tags:
  - "ai-agent"
  - "agent-architecture"
  - "multi-agent"
  - "agentic-loop"
confidence: "high"
created_at: "2026-04-17T16:57:33.446590"
updated_at: "2026-04-20T16:00:00"
---

# AI Agent

## 概述
AI Agent是具备自主决策和执行能力的智能系统，通过Agentic Loop（代理循环）实现从任务理解到结果输出的完整工作流，区别于传统的代码补全工具。

## 核心要点
- **Agentic Loop架构**：用户输入 -> LLM思考 -> 工具选择 -> 执行 -> 观察 -> 继续思考 -> 结果返回的循环模式
- **范式转变**：从代码补全建议到自主执行的转变，Agentic Loop vs Inline Suggestion Model
- **Extended Thinking**：内部推理模式，允许Agent进行深度思考而非直接响应
- **Multi-Agent系统**：专业化Agent分工协作，Lead Agent协调并行执行，克服Single-Mode问题
- **工具系统设计**：工具描述定义Agent对现实的理解，直接影响性能表现
- **公式**：Agent = Loop(Model + Harness)，强调环境和模型同等重要

## 相关概念
- [[Agentic Loop]]
- [[Extended Thinking]]
- [[Multi-Agent Orchestration]]
- [[Agent Memory Systems]]
- [[Agent RL Training]]
- [[Agent Skills Framework|Skills]]
- [[Model Context Protocol (MCP)]]
- [[Harness Engineering]]
- [[Single-Mode Problem]]

## 相关实体
- [[Claude Code]]
- [[Anthropic]]
- [[Flood Sung]]
- [[MetaBot]]

## 来源
- [src: Claude Code Agent Technical Analysis and Multi-Agent Architecture]
- [src: Zhihu Discussion: AI Agent Engineering Career Paths and Technical Approaches]