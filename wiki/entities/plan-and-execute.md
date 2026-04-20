---
title: "Plan-and-Execute"
type: "entity"
sources:
  - "wiki/sources/claude-code-advanced-guide.md"
  - "wiki/sources/Claude Code完整概念指南27个核心概念详解.md"
tags:
  - "workflow"
  - "claude-code"
  - "planning"
  - "agentic"
confidence: "high"
created_at: "2026-04-20T00:24:41.159867"
updated_at: "2026-04-20T00:00:00"
---

# Plan-and-Execute

## 概述
Plan-and-Execute是Claude Code的核心工作流模式，强调先规划后执行的原则，通过Plan Mode实现只输出计划不执行操作的设计，复杂任务的标准工作流遵循Explore→Plan→Implement→Verify四阶段。

## 基本信息
- 类型：工作流模式
- 相关领域：AI辅助开发、任务规划、迭代开发

## Plan Mode机制

### 进入方式
- 命令行：`claude --permission-mode plan`
- 快捷键：Shift+Tab循环切换
- 自然语言："先别改代码，给我一个实施计划"

### 核心价值
- **只规划不执行**：输出计划但不实施操作
- **降低修改成本**：改计划一句话，改已写好的代码要十倍时间
- **强制思考阶段**：复杂任务永远先进Plan Mode

## 标准工作流

### 四阶段模型
```
Explore → Plan → Implement → Verify
```

| 阶段 | 任务 | 说明 |
|------|------|------|
| Explore | 探索理解 | 理解代码库和问题 |
| Plan | 制定计划 | 设计实施方案 |
| Implement | 执行实施 | 按计划编码 |
| Verify | 验证闭环 | 检验结果正确性 |

## 最佳实践

### 指令精准化三要素
1. **目标**：明确要达成什么
2. **约束**：不改什么、不加什么
3. **上下文**：@引用加行号精准聚焦

### "不要"比"要"更重要
- "不要加新依赖"比列出10个允许的库更有效
- "只改这个函数"比"修改这个功能"更精准

## 相关
- [[Plan Mode工作流]]
- [[Claude Code]]
- [[CLAUDE.md Architecture]]
- [[Claude Code子代理]]