---
title: "Skills (Anthropic Framework)"
type: "concept"
sources:
  - "wiki/sources/skills本质分析.md"
  - "wiki/sources/claude-code-skills-docs.md"
tags:
  - "skills"
  - "claude-code"
  - "design-pattern"
  - "capability-encapsulation"
confidence: "high"
created_at: "2026-04-17T22:06:46.802580"
updated_at: "2026-04-23T07:23:32.376275"
---

# Skills

## 概述

Skills是Claude Code的能力扩展机制，本质是可复用的能力封装，定义了做什么(What)、怎么做(How)、何时做(When)三个核心维度。

## 核心要点

- **封装性**：将复杂任务流程打包为可调用的能力单元
- **可复用性**：多次调用无需重写，维护成本低
- **触发性**：条件满足时自动执行，减少重复指令
- **状态管理**：包含决策逻辑和状态管理，不同于无状态的Function Calling
- **存储层级**：企业级、个人级(~/.claude/skills/)、项目级(.claude/skills/)三级存储

## Related

- [[Skill]]
- [[Skill]]
- [[Claude]]
- [[Skill]]