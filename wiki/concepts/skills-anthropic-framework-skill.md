---
title: "Skills (Anthropic Framework)"
type: "concept"
sources:
  - "wiki/sources/anthropic-skills-engineering-approach-to-agent-capability-development.md"
tags:
  - "claude-code"
  - "agent-engineering"
  - "skill-development"
  - "anthropic"
  - "workflow-automation"
confidence: "high"
created_at: "2026-04-17T22:06:46.802580"
updated_at: "2026-04-20T12:00:00"
---

# Skills (Anthropic Framework)

Anthropic 推出的 AI Agent 能力扩展机制，通过 SKILL.md 文件系统化地定义可复用的代理能力，将一次性 Prompt 转化为持久资产。

## 核心要点

- **资产化思维**: Skills 将一次性的 Prompt 转化为可复用、可测试、可迭代的持久资产，而非临时的指令
- **渐进式披露**: 采用三层信息加载架构（catalog → instructions → resources），高效管理 Agent 的上下文窗口
- **工程化生命周期**: 包含问题定义、起草 SKILL.md、A/B 基线测试、可视化评估、迭代优化等完整工程流程
- **触发优化**: 类似 ML 超参数调优的过程，确保 Skill 在正确场景被正确触发
- **官方工具链**: Anthropic 提供 skill-creator 模板，引导系统化的 Skill 开发流程

## Related

- [[Claude Code Skills系统]]
- [[Anthropic]]
- [[Claude Code]]
- [[Progressive Disclosure (Agent Skills)]]
- [[MCP Server Integration]]
- [[Slash Commands Customization]]