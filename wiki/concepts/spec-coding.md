---
title: "Spec Coding"
type: "concept"
sources:
  - "raw/articles/12be559f_claude.md怎么写才能让Claude Code更高效claude.md怎么写才能让Claude Code更高效.md"
  - "raw/articles/2b36f099_claude.md怎么写才能让Claude Code更高效claude.md怎么写才能让Claude Code更高效.md"
tags:
  - "开发方法论"
  - "软件工程"
  - "AI编程"
  - "规范驱动"
confidence: "high"
created_at: "2026-04-21T14:13:50.850073"
updated_at: "2026-04-21T14:13:50.850073"
related:
  - "Vibe Coding"
  - "Plan"
  - "Humanize"
  - "RLCR"
  - "Agent-First Development"
  - "Humanize插件"
  - "Agent协作与任务拆分"
  - "yahah"
---

# Spec Coding

## 定义
一种反对[[Vibe Coding]]（感觉式编程）的严谨开发方法，强调在实现前必须先有明确、详细的规格说明（Specification）。[[yahah]]在[[Claude Code高效配置与开发实践指南]]中将其描述为提高AI生成代码确定性、可验证性和架构合理性的关键方法。

## 核心组件
1. **Spec（规格说明）** - 描述"写什么、怎么写、设计是什么"的目标状态文档
2. **[[Plan]]（实施计划）** - 基于Spec制定的详细指令序列，描述"按什么顺序写、阶段测试点"的到达路径

## 工作流程
Spec Coding要求开发过程始于对代码架构的清晰理解（Spec），然后制定驱动实现的详细[[Plan]]，而非直接根据模糊感觉写代码。一个好的[[Plan]]应该让阅读者感觉"按照这个步骤，一个本科生也能在一个月内完成"。大型项目的Plan可能长达5-10页A4纸（约2万字符）。

## 与相关方法的关系
- **[[Humanize]]** - Spec Coding的一种具体实现模式，利用迭代反馈循环
- **[[RLCR]]** - 可用于执行Spec Coding中大规模修改任务的方法论
- **[[Agent-First Development]]** - 与Spec Coding兼容的开发范式

## 优势
- **提高确定性**：减少AI生成代码的随机性和方向性错误
- **增强可验证性**：明确的验收标准便于阶段性测试
- **改善架构**：提前思考整体设计，避免后期重构
- **便于协作**：清晰的文档让团队成员（包括AI）理解一致

## 实践建议
在实现新模块前，先编写详细的Spec文档，描述模块的接口、数据结构、与系统其他部分的交互关系。然后基于Spec制定分步实现的[[Plan]]，避免使用行号定位代码，而是使用概念性描述以提高鲁棒性。

## 相关概念
- [[Vibe Coding]] - 对立的方法论
- [[Plan]] - Spec Coding的核心输出
- [[Humanize]] - 利用Spec Coding的协同开发模式
- [[RLCR]] - 执行大规模Spec Coding任务的方法
- [[Agent-First Development]] - 兼容的开发范式

**backlinks_note**: 本概念在[[Claude Code高效配置与开发实践指南]]中作为反对[[Vibe Coding]]的高级开发方法论被详细阐述，由[[yahah]]重点介绍。

## Related
- [[Vibe Coding]]
- [[Plan]]
- [[Humanize]]
- [[RLCR]]
- [[Agent-First Development]]

---

## Additional Insights



在[[CLAUDE.md高效编写指南与AI编程实践]]中，[[yahah]]详细阐述了Spec Coding作为反对[[Vibe Coding]]的严谨开发方法。Spec Coding强调在实现前必须有明确的规格说明（Spec）和详细的实施[[Plan]]，这与文档中倡导的结构化AI编程理念完全一致。

[[Humanize插件]]是Spec Coding的一种具体实现模式，通过迭代反馈循环确保代码质量。Spec Coding也自然支持[[Agent协作与任务拆分]]——清晰的Spec和Plan使得任务分解和分配成为可能，不同Agent可以基于统一的规格说明并行工作。

文档指出，一个好的[[Plan]]应该详细到“按照这个步骤，一个本科生也能在一个月内完成”的程度。大型项目的Plan可能长达5-10页A4纸（约2万字符）。这种详细规划虽然前期耗时，但能显著提高AI生成代码的确定性、可验证性和架构合理性，是应对[[概率性提示词局限]]的有效策略。

Spec Coding与[[CLAUDE.md配置哲学]]互补：CLAUDE.md提供项目级约定，Spec提供任务级规格，Plan提供执行级指令，三者共同构成完整的AI编程指导体系。

Source: [[raw/articles/2b36f099_claude.md怎么写才能让Claude Code更高效claude.md怎么写才能让Claude Code更高效.md]]

## Related
- [[Vibe Coding]]
- [[Plan]]
- [[Humanize]]
- [[RLCR]]
- [[Agent-First Development]]
- [[Humanize插件]]
- [[Agent协作与任务拆分]]
- [[yahah]]