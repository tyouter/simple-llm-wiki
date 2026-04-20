---
title: "CLAUDE.md Architecture"
type: "entity"
sources:
  - "wiki/sources/知乎讨论-claude.md怎么写才能让Claude Code更高效.md"
  - "wiki/sources/claude-md-高效配置-杞鋂.md"
  - "wiki/sources/claude-code-advanced-guide.md"
tags:
  - "claude-code"
  - "configuration"
  - "memory-system"
  - "context-management"
confidence: "high"
created_at: "2026-04-18T00:50:51.015027"
updated_at: "2026-04-20T00:00:00"
---

# CLAUDE.md Architecture

## 概述
CLAUDE.md是Claude Code的持久记忆系统架构，作为项目配置文件实现"一次性编写、持续生效"的上下文管理机制，是Claude Code六层系统架构的最顶层。

## 基本信息
- 类型：配置系统架构
- 相关领域：AI辅助开发、上下文管理、持久记忆

## 核心架构

### 六层系统模型
Claude Code的完整架构包含六层：

| 层 | 职责 | 说明 |
|---|-----|------|
| CLAUDE.md/rules/memory | 长期上下文 | 告诉Claude"是什么" |
| Tools/MCP | 动作能力 | 告诉Claude"能做什么" |
| Skills | 按需加载方法论 | 告诉Claude"怎么做" |
| Hooks | 强制执行 | 规则强制执行机制 |
| Subagents | 隔离上下文工作者 | 任务分配机制 |
| Verifiers | 验证闭环 | 结果检验机制 |

### 配置分层
- **全局层**（~/.claude/CLAUDE.md）：行为偏好、通用规则
- **项目层**（./CLAUDE.md）：项目事实、技术栈、架构决策
- **路径规则层**（.claude/rules/）：按路径匹配的局部规范

## 最佳实践

### 核心原则
- **越短越好**：控制在200行以内，太长会降低遵循度
- **放"为什么"**：架构决策、历史教训、业务约束、风格偏好
- **不放"是什么"**：API文档、逐文件描述（Claude自己会读代码）

### 配置争论
关于CLAUDE.md存在两种对立观点：
- **全面配置方法**：主张详细配置可达200行，覆盖项目规则、架构、编码标准
- **极简需求驱动方法**：主张简洁约50行，仅聚焦核心上下文和禁止事项

## 相关
- [[Claude Code]]
- [[Claude Code Skills系统]]
- [[Claude Code Hooks]]
- [[Claude Code子代理]]
- [[Plan Mode工作流]]
- [[知乎讨论-claude.md怎么写才能让Claude Code更高效]]