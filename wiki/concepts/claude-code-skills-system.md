---
title: "Claude Code Skills系统"
type: "concept"
sources:
  - "raw/webpages/f599cc5e_Extend Claude with skills - Claude Code DocsExtend Claude with skills.md"
tags:
  - "claude-code"
  - "skills"
  - "extension-system"
  - "prompt-based"
confidence: "high"
created_at: "2026-04-20T12:00:00"
updated_at: "2026-04-20T12:00:00"
related:
  - "Claude Code Skills官方文档"
  - "Agent Skills开放标准"
  - "Claude Code Hooks"
---

# Claude Code Skills系统

## 定义

Claude Code的扩展机制，通过创建SKILL.md文件添加自定义指令和能力，让Claude学习新的工作方法。

## 核心特点

- **Prompt-based**：给Claude详细playbook，让它用工具orchestrate工作
- **可spawn并行Agent**
- **可读文件、适配代码库**
- **遵循Agent Skills开放标准**

## Skills vs Commands

| 维度 | Skills | Commands |
|------|--------|----------|
| 文件位置 | .claude/skills/name/SKILL.md | .claude/commands/name.md |
| 支持文件 | 支持目录结构 | 单文件 |
| Frontmatter | 完整配置 | 基础配置 |
| Invocation控制 | 支持 | 不支持 |
| Subagent执行 | 支持 | 不支持 |

同名时Skills优先。

## 两类内容

### Reference内容

添加知识Claude应用到当前工作：
- 约定、模式、风格指南
- 领域知识
- 运行inline，与对话上下文并存

### Task内容

给Claude步骤指令：
- 部署、提交、代码生成
- 通常用/skill-name手动触发
- 添加`disable-model-invocation: true`阻止自动加载

## Related
- [[Claude Code Skills官方文档]]
- [[Agent Skills开放标准]]
- [[Claude Code Hooks]]