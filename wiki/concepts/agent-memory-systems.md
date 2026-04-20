---
title: "Agent Memory Systems"
type: "concept"
sources:
  - "wiki/sources/supermemory-s-asmr-system-a-critical-look-at-ai-memory-breakthroughs.md"
tags:
  - "ai-memory"
  - "multi-agent-systems"
  - "agent-architecture"
confidence: "high"
created_at: "2026-04-20T00:24:41.160867"
updated_at: "2026-04-20T16:00:00"
---

# Agent Memory Systems

## 概述
AI Agent的记忆系统是解决长期上下文保持和知识持久化的关键技术，涵盖向量数据库检索、多Agent协作记忆、以及主动式记忆检索等多种架构方案。

## 核心要点
- **向量数据库挑战**：传统向量数据库在处理时序推理、逻辑矛盾和动态上下文时面临瓶颈，被称为"走入死胡同"
- **Agent-Based Active Retrieval**：通过专业化Agent主动查询和合成信息的范式，优于被动语义相似性搜索
- **ASMR架构**：Supermemory团队提出的Agentic Search and Memory Retrieval系统，采用纯Agent架构分解记忆任务为并行处理
- **Benchmark vs Engineering Reality Gap**：高分数基准测试与实际工程需求之间存在显著差距，P99延迟（<6ms）、成本效率和可靠性同样重要
- **分布式上下文管理**：通过多个清洁的上下文窗口配合定期摘要，克服token限制

## 相关概念
- [[Multi-Agent Specialization & Orchestration]]
- [[AI Agent Cognitive Architecture]]
- [[Enhanced RAG with Human-like Reasoning]]
- [[Context Engineering]]
- [[Persistent Memory System (Claude Code)]]

## 相关实体
- [[Supermemory.ai]]
- [[LongMemEval/LongMemEval_s]]

## 来源
- [src: Supermemory's ASMR System: A Critical Look at AI Memory Breakthroughs]