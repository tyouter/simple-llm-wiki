---
title: "Anthropic Skills: Engineering Approach to Agent Capability Development|Anthropic Skills Framework"
type: "concept"
sources:
  - "wiki/sources/anthropic-skills-engineering-approach-to-agent-capability-development.md"
  - "wiki/sources/agent-skills-vs-mcp-technical-comparison-and-enterprise-applications.md"
tags:
  - "anthropic"
  - "skill-engineering"
  - "agent-framework"
  - "claude-code"
confidence: "high"
created_at: "2026-04-17T22:06:46.803885"
updated_at: "2026-04-20T16:00:00"
---

# Anthropic Skills Framework

## 概述
Anthropic Skills框架是Anthropic官方推出的工程化Agent能力开发方法论，将Skills视为永久可重用资产，提供系统性的创建、测试和优化流程。

## 核心要点
- **核心理念转变**：从Prompt一次性使用到Skill资产化："Prompt是一次性的，Skill才是资产"
- **工程生命周期**：问题定义 -> 起草SKILL.md -> A/B基线测试 -> 可视化评估 -> 迭代优化
- **Progressive Disclosure**：渐进式信息披露，分层加载（catalog -> instructions -> resources）管理上下文窗口
- **Description Trigger Optimization**：描述触发优化，类似ML超参数调优确保Agent正确调用Skill
- **官方工具支持**：skill-creator模板提供结构化目录和工程流程指导
- **Token效率**：相比MCP实现，Skills在浏览器自动化任务中展现4倍token消耗降低

## 相关概念
- [[Agent Skills Framework|Skills]]
- [[skills-vs-tools-distinction]]
- [[Token Efficiency in AI Reasoning]]
- [[GStack: Role-Based AI Development Workflow]]
- [[AI Tool Chaining/Combination]]
- [[Progressive Disclosure]]

## 相关实体
- [[Anthropic]]
- [[skill-creator]]
- [[Ai学习的老章]]

## 来源
- [src: Anthropic Skills: Engineering Approach to Agent Capability Development]
- [src: Agent Skills vs MCP: Technical Comparison and Enterprise Applications]