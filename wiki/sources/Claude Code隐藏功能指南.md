---
title: "Claude Code隐藏功能指南"
type: "source"
sources:
  - "raw/articles/27bcfccd_Claude Code 深度用法指南那些让效率翻倍的隐藏技巧.md"
tags:
  - "claude-code"
  - "ai-development-tools"
  - "workflow-optimization"
  - "hidden-features"
  - "command-guide"
  - "multi-agent"
  - "efficiency"
  - "source"
confidence: "high"
created_at: "2026-04-17T21:50:12.391445"
updated_at: "2026-04-22T23:50:27.644000"
related:
  - "Claude Code"
  - "Thariq"
  - "Boris"
  - "Context Pollution"
  - "Parallel Agent Review"
  - "Model-Switching Optimization"
  - "Workflow Branching"
  - "GStack角色化AI开发工作流"
  - "AI Tool Chaining/Combination"
  - "Claude Code 2026完整新手教程"
  - "Oh My ClaudeCode把Claude变成Coding武器"
  - "为AI构建代码知识图谱的两个Skill"
  - "约束工程与VibeCoding的核心要点"
---

# Claude Code隐藏功能指南

## 概述
一份详细介绍[[Claude Code]] AI开发工具鲜为人知但高效实用的命令和快捷方式的实用指南。本指南聚焦于提升工作流效率的功能，如并行任务管理、上下文保护和模型优化。许多功能在官方文档中未充分记录，通过开发者社交媒体渠道被发现和分享。

## 关键命令与技巧

### /btw 命令
**用途**: 解决[[Context Pollution]]问题，允许用户在不污染主工作流上下文的情况下提出无关问题。
**来源**: [[Thariq]]（Claude Code产品负责人）在社交媒体宣布。
**用法**: 在执行主任务时，使用`/btw`后跟独立问题来处理侧边询问，避免偏离主要执行。

### /simplify 命令
**用途**: 实现[[Parallel Agent Review]]，让多个AI代理同时从不同角度（可复用性、质量、效率）审查代码。
**来源**: [[Boris]]（Claude Code核心团队成员）日常使用。
**用法**: 在生成或修改代码后，使用`/simplify`从专用审查代理获取综合反馈。

### /model opusplan 命令
**用途**: 启用[[Model-Switching Optimization]]，使用Claude Opus进行规划，Claude Sonnet进行执行。
**用法**: 以`/model opusplan`开始，让Opus创建详细计划，然后Sonnet高效执行，节省高端模型token。

### /branch 命令
**用途**: 促进[[Workflow Branching]]，从共享起点创建并行开发路径。
**用法**: 在探索不同实现方法时，使用`/branch`测试替代方案而不丢失原始上下文。

### /rewind 命令
**用途**: 允许在上下文损坏或代理偏离轨道时回溯到对话的前置状态。
**用法**: 使用`/rewind`后跟步骤编号或描述返回更清洁的上下文状态。

### /export 命令
**用途**: 通过导出上下文到其他开发工具实现跨工具验证和集成。
**用法**: 使用`/export`将Claude Code上下文导入Codex或其他AI助手进行验证或继续工作。

## 与现有概念的关联

### 与[[GStack角色化AI开发工作流]]的连接
本指南提供了可在GStack高层角色化工作流中使用或增强的具体低级命令。`/btw`、`/rewind`和`/simplify`命令在复杂角色化工作流中维护清洁上下文特别有用。

### 与[[AI Tool Chaining/Combination]]的连接
指南隐含提倡在Claude Code内部进行工具链式组合，并明确提及使用`/export`将上下文导入其他工具。这代表了单一AI开发环境中工具链概念的实用实现。

## 实践应用

### 开发工作流优化
- 在编码会话中使用`/btw`进行文档查阅
- 每次重大代码迭代后应用`/simplify`进行质量保证
- 对复杂架构决策实施`/model opusplan`

### 团队协作
- 共享`/branch`工作流用于代码审查和替代方案测试
- 使用`/export`在使用不同工具的团队成员间转移上下文
- 为复杂调试会话记录`/rewind`点

## 来源归属
本指南综合了开发者社交媒体帖子的信息，特别是来自Claude Code团队成员[[Thariq]]和[[Boris]]，以及开发论坛和聊天群中分享的社区发现。

**注意**: 描述的功能可能随Claude Code更新而演进，部分命令可能是实验性的或需要特定访问级别。

## Related
- [[Claude Code]]
- [[Thariq]]
- [[Boris]]
- [[Context Pollution]]
- [[Parallel Agent Review]]
- [[Model-Switching Optimization]]
- [[Workflow Branching]]
- [[GStack角色化AI开发工作流]]
- [[Claude Code 2026完整新手教程]]
- [[Oh My ClaudeCode把Claude变成Coding武器]]
- [[为AI构建代码知识图谱的两个Skill]]
- [[约束工程与VibeCoding的核心要点]]
- [[AI Tool Chaining/Combination]]