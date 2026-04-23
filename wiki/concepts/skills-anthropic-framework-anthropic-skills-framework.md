---
title: "Skills (Anthropic Framework)"
type: "concept"
sources:
  - "wiki/sources/anthropic-skills-engineering-approach-to-agent-capability-development.md"
  - "wiki/sources/claude-code-skills-docs.md"
  - "wiki/sources/skills本质分析.md"
tags:
  - "anthropic"
  - "skills-framework"
  - "agent-engineering"
  - "capability-encapsulation"
confidence: "high"
created_at: "2026-04-17T22:06:46.803885"
updated_at: "2026-04-23T07:23:32.375272"
---

# Anthropic Skills Framework

## 概述

Anthropic Skills框架是Claude Code的扩展机制，通过SKILL.md文件定义可复用的能力封装，支持Progressive Disclosure和Description Trigger优化等工程化实践。

## 核心要点

- **能力封装资产**：Skills是可复用的资产而非一次性Prompt
- **SKILL.md核心**：以SKILL.md文件为核心定义能力结构和触发条件
- **渐进披露机制**：信息分层加载(目录→指令→资源)，优化Token效率
- **Description Trigger优化**：类似ML超参数调优，确保Skill正确触发
- **工程生命周期**：包含问题定义、起草、A/B测试、迭代优化的完整流程

## Related

- [[Skill]]
- [[Skill]]
- progressive-disclosure-mechanism
- [[Skill]]
- [[Agent]]