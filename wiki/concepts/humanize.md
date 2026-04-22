---
title: "Humanize"
type: "concept"
sources:
  - "raw/articles/12be559f_claude.md怎么写才能让Claude Code更高效claude.md怎么写才能让Claude Code更高效.md"
tags:
  - "AI协同开发"
  - "迭代开发"
  - "代码审查"
  - "工作流"
confidence: "high"
created_at: "2026-04-21T14:13:50.852718"
updated_at: "2026-04-21T14:13:50.852718"
related:
  - "Spec Coding"
  - "Plan"
  - "RLCR"
  - "Codex"
  - "Superpowers"
  - "Claude Code"
  - "Humanize工作流"
  - "Spec Coding vs Vibe Coding"
  - "yahah"
---

# Humanize

## 定义
一种利用迭代反馈循环的[[AI协同开发]]模式，强调[[Claude Code]]执行计划与[[Codex]]独立审查的分离。在[[Claude Code高效配置与开发实践指南]]中，[[yahah]]将其描述为[[Spec Coding]]的一种具体实现方式。

## 核心机制
建立"[[Claude Code]]执行 → [[Codex]]审查 → 发现问题 → 反馈修正"的持续循环。不追求一次性产出完美代码，而是通过迭代逐步完善：
1. [[Claude Code]]负责按照[[Plan]]写代码
2. 另一个AI（如[[Codex]]）独立审查进展
3. 及早发现问题并反馈
4. 工作持续进行，直到满足所有验收标准

## 最佳实践
"双开"窗口工作模式：
- **窗口A**：用于[[Plan]]制定和分析
- **窗口B**：用于代码实现
- **可选窗口C**：用于编写Spec文档

这种模式高效占用开发者的时间，同时保持高质量的代码产出。[[yahah]]建议白天开发时为同一项目打开两个[[Claude Code]]窗口，一个用于规划和审查，一个用于执行代码生成任务。

## 工具支持
- **[[Humanize工具]]** - GitHub项目humania-org/humanize提供的具体实现
- **[[Superpowers]]** - 确保AI代理能使用预定义技能的工具，可为[[Codex]]配置
- **[[Codex]]** - 通常指OpenAI的Codex模型，用作独立审查者

## 与相关方法的关系
- **[[Spec Coding]]** - Humanize是实现Spec Coding的具体模式之一
- **[[RLCR]]** - 互补的大规模代码修改方法，可结合使用
- **[[Plan]]** - Humanize工作流中Claude执行的基础

## 优势
- **早期问题发现**：独立审查避免盲点
- **质量保证**：迭代反馈提高代码健壮性
- **效率平衡**：开发者时间被高效利用
- **知识沉淀**：审查过程产生有价值经验

## 相关概念
- [[Spec Coding]] - 本方法所属的方法论框架
- [[Plan]] - 执行的基础
- [[RLCR]] - 互补的代码修改方法
- [[Codex]] - 常用的独立审查AI
- [[Superpowers]] - 支持工具

**backlinks_note**: 本概念在[[Claude Code高效配置与开发实践指南]]中作为高级开发方法论被介绍，是[[Spec Coding]]的具体实现模式，与[[RLCR]]互补。

## Related
- [[Spec Coding]]
- [[Plan]]
- [[RLCR]]
- [[Codex]]
- [[Superpowers]]
- [[Claude Code]]

---

一个利用迭代反馈循环进行 AI 辅助开发的工具/框架，由 “humania-org” 开发。其核心模式 [[Humanize工作流]] 是让一个 AI（如 Claude）执行 [[Plan]]，另一个 AI（如 Codex）进行独立审查，人类在快速迭代中提供反馈和裁决。该工具不追求一次性正确，而是通过自动化循环持续工作直至满足标准。[[yahah]] 在其回答中引用了此工具作为实践 [[Spec Coding vs Vibe Coding]] 理念的范例，并描述了将其融入高强度开发日程的“双开窗口”模式。

## Related
- [[Spec Coding]]
- [[Plan]]
- [[RLCR]]
- [[Codex]]
- [[Superpowers]]
- [[Claude Code]]
- [[Humanize工作流]]
- [[Spec Coding vs Vibe Coding]]
- [[yahah]]