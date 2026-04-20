---
title: "Obsidian CLI + Claude Code AI笔记工作流"
type: "source"
sources:
  - "raw/videos/5630b8bc_ObsidianCLIClaudeCode我的AI笔记工作流.md"
tags:
  - "obsidian"
  - "claude-code"
  - "cli"
  - "workflow"
  - "skills"
  - "note-taking"
confidence: "high"
created_at: "2026-04-20T12:00:00"
updated_at: "2026-04-20T12:00:00"
---

# Obsidian CLI + Claude Code AI笔记工作流

## 概述

Obsidian 官方推出了 CLI 命令行工具，面向所有用户开放。这意味着 AI 可以直接调用笔记、日志、标签、反向链接，彻底改变了传统笔记的使用规则。

## CLI 的核心变化

### 数据读取革命

- AI 不再需要逐个文件扫描
- 可以快速准确读取笔记库
- 直接访问数据库内容

### 能力边界扩展

从「只能改文件的编辑器」变成「能操控 Obsidian 的 AI 助手」：
- 触发 Obsidian 核心插件
- 操作数据库
- 管理同步
- 模板操作

## 工作流设计

### 1. 每日开场流程

一条指令自动完成：
- 加载记忆
- 读取日志
- 查看任务
- 规划一天重点

### 2. Skill 系统

- 封装常用操作为可复用工作流
- 随时调用
- 支持自定义创建

### 3. Skill 创建方法

让 AI 帮你创建 Skill：
- 描述需要的功能
- AI 自动生成 Skills 文件
- 包含 Obsidian CLI 调用规则
- 定义触发条件和输出规则

## Skill 文件结构

```markdown
# Skill 示例
需要用到：
- CLI 命令
- 具体读取文件
- 模板应用
- 核心规则
- 触发条件
- 输出规则
- 相关定义
```

## 实战演示

创建一个 Skill 来：
- 读取所有重要任务文件
- 分析状态
- 生成报告
- 推荐优先级

## 视频信息

- **作者**: Kiven大汉堡
- **发布日期**: 2026-03-01
- **时长**: 5:34
- **观看数**: 2.1万
- **点赞数**: 396

## Related

- [[Obsidian]]
- [[Claude-Code]]
- [[Obsidian-CLI]]
- [[Skills]]
- [[AI-Enhanced-Note-Taking]]