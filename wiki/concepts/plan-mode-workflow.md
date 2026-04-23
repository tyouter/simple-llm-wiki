---
title: "Plan Mode工作流"
type: "concept"
sources:
  - "raw/articles/55258346_claude code使用感受如何claude code使用感受如何.md"
tags:
  - "claude-code"
  - "workflow"
  - "planning"
  - "implementation"
confidence: "high"
created_at: "2026-04-20T12:00:00"
updated_at: "2026-04-22T23:50:22.729019"
related:
  - "Claude Code深度使用指南"
  - "Claude Code子代理"
  - "Hooks for Deterministic Automation"
  - "Slash Commands Customization"
  - "TDD with Claude Code"
  - "CLAUDE.md Architecture"
  - "Plan-and-Execute"
  - "15条高频实用的Claude Code技巧"
  - "Claude Code职场替身应用"
  - "GSD AI编程工作流指南"
---

# Plan Mode工作流

## 定义

Claude Code的规划模式，只输出计划不执行任何操作，用于复杂任务的预规划。

## 进入方式

| 方式 | 操作 |
|------|-----|
| 启动时 | `claude --permission-mode plan` |
| 会话中 | Shift+Tab循环切换 |
| 自然语言 | "先别改代码，给我一个实施计划" |

## 核心价值

- **改计划一句话**：在编辑器里Ctrl+G打开计划，删掉不必要的步骤，加约束
- **改已写好的代码十倍时间**：避免走到一半引入循环依赖

## 标准四步workflow

```
Explore → Plan → Implement → Verify
```

1. **Explore**：Claude读代码，理解现状
2. **Plan**：输出实施计划
3. **Implement**：逐步执行
4. **Verify**：跑测试验证

## 适用判断

| 场景 | 是否用Plan Mode |
|------|----------------|
| 只有一种实现方式 | 不用 |
| 多个选择可能 | 用 |
| 超过3个文件的改动 | 用 |
| 重命名变量、修错字 | 不用 |

## 实践建议

复杂任务永远先进Plan Mode。确认后Claude按更新后的计划执行，避免反复修改。

## Related
- [[Claude Code深度使用指南]]
- [[Hooks for Deterministic Automation]]
- [[Slash Commands Customization]]
- [[TDD with Claude Code]]
- [[CLAUDE.md Architecture]]
- [[Plan-and-Execute]]
- [[15条高频实用的Claude Code技巧]]
- [[Claude Code职场替身应用]]
- [[GSD AI编程工作流指南]]
- [[Claude Code子代理]]