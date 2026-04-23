---
title: "Agent Skills Framework"
type: "concept"
sources:
  - "wiki/sources/anthropic-skills-engineering-approach-to-agent-capability-development.md"
  - "wiki/sources/agent-skills-vs-mcp-technical-comparison-and-enterprise-applications.md"
tags:
  - "agent-skills"
  - "claude-code"
  - "skill-engineering"
  - "anthropic"
confidence: "high"
created_at: "2026-04-18T01:17:46.939053"
updated_at: "2026-04-23T07:23:32.372710"
---

# Agent Skills Framework / Skills

## 概述
Anthropic推出的Skills框架是一种工程化的Agent能力开发方法，通过SKILL.md文件定义可重用的能力资产，实现渐进式信息披露和业务流程标准化。

## 核心要点
- **资产化理念**："Prompt是一次性的，Skill才是资产" - Skills被视为永久、可重用的资产而非一次性提示词
- **工程生命周期**：包括问题定义、起草、A/B基线测试、可视化评估、迭代优化等系统性流程
- **Progressive Disclosure**：渐进式信息披露设计哲学，分层加载信息（catalog -> instructions -> resources）高效管理Agent上下文
- **Token效率优化**：Skills相比MCP实现展现出4倍的token消耗降低（以浏览器自动化任务为例）
- **企业应用**：将业务SOP、规则和领域知识转化为标准化Skills，实现一致性的AI执行
- **描述触发优化**：类似ML超参数调优的关键过程，确保Agent正确调用Skill

## 相关概念
- [[Skill]]
- [[Token Efficiency in AI Reasoning]]
- [[AI Tool Chaining/Combination]]
- [[GStack: Role-Based AI Development Workflow]]
- [[Model Context Protocol (MCP)]]

## 相关实体
- [[Anthropic]]
- [[skill-creator]]
- [[Cursor]]
- [[Ai学习的老章]]

## 来源
- [src: Anthropic Skills: Engineering Approach to Agent Capability Development]
- [src: Agent Skills vs MCP: Technical Comparison and Enterprise Applications]