---
title: "Slash Commands Customization"
type: "concept"
sources:
  - "wiki/sources/advanced-claude-code-workflow-techniques-and-architecture-analysis.md"
tags:
  - "claude-code"
  - "workflow"
  - "customization"
  - "automation"
  - "reusable-commands"
confidence: "high"
created_at: "2026-04-18T00:50:51.014028"
updated_at: "2026-04-23T00:42:20.524990"
---

# Slash Commands Customization

Claude Code 中创建可复用工作流命令的机制，允许用户定义带有参数的自定义命令以自动化常见任务。

## 核心要点

- **可复用命令**: 将常用工作流封装为 `/command` 形式，避免每次重复输入相同指令
- **参数支持**: 命令可以接受参数，实现动态定制，例如 `/review-pr 123` 自动检查特定 PR
- **工作流自动化**: 结合 Skills 和 Hooks，形成完整的自动化开发工作流体系
- **减少上下文消耗**: 预定义命令减少主上下文中的指令输入，提高效率
- **与 Skills 协同**: Slash Commands 可触发特定 Skills，实现复杂的组合操作

## Related
- [[Claude Code Automation/Configuration Management]]
- [[Single-Loop Architecture]]
- [[Advanced Claude Code Workflow Techniques and Architecture Analysis]]
- [[Claude Code工作流技术与架构分析]]

- [[Claude Code]]
- [[Claude Code Skills系统]]
- [[Hooks for Deterministic Automation]]
- [[Plan Mode工作流]]
- workflow-optimization