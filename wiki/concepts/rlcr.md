---
title: "RLCR"
type: "concept"
sources:
  - "raw/articles/12be559f_claude.md怎么写才能让Claude Code更高效claude.md怎么写才能让Claude Code更高效.md"
tags:
  - "代码重构"
  - "大规模修改"
  - "AI驱动"
  - "方法论"
confidence: "high"
created_at: "2026-04-21T14:13:50.854661"
updated_at: "2026-04-23T00:42:20.481264"
related:
  - "Plan"
  - "Humanize"
  - "蜂群"
  - "Spec Coding"
  - "/batch"
---

# RLCR

## 定义
一种AI驱动的代码重构与修改方法，名称可能为"Refactor, Loop, Check, Repeat"或类似含义的缩写。在[[Claude Code高效配置与开发实践指南]]中，[[yahah]]将其描述为针对大规模代码修改任务的方法论。

## 规模适应性
根据任务规模选择不同实施策略：
- **5k-10k行**：使用"普通的RLCR"
- **10k-30k行**：考虑使用"蜂群+RLCR"的增强模式
- **超过3万行**：可能需要使用带`/batch`命令的RLCR

## 核心思想
将大规模代码修改任务分解为可管理、可验证的步骤，通过循环迭代确保质量。其本质是[[Plan]]驱动的系统化方法，强调分阶段实施和持续验证。

## 成功案例
[[yahah]]分享了一个标志性成功案例：使用RLCR结合"蜂群"在**四小时内**完成了gem5仓库（一个广泛使用的计算机系统架构模拟器）构建系统从SCons到CMake的彻底替换。这展示了RLCR处理复杂、大规模工程任务的能力。

## 与相关方法的关系
- **[[Plan]]** - RLCR严重依赖详细的实施计划
- **[[Humanize]]** - 互补的协同开发方法，可结合使用
- **[[Spec Coding]]** - RLCR可用于执行Spec Coding中的大规模修改任务
- **蜂群** - 处理超大规模任务时的增强协同模式
- **`/batch`命令** - 自动化执行大规模任务的工具支持

## 实施要点
1. **任务分解**：将大任务拆分为可独立验证的子任务
2. **计划制定**：创建详细的阶段实施[[Plan]]
3. **循环验证**：每个阶段完成后进行检查
4. **迭代改进**：基于反馈持续优化

## 应用场景
- 大型单体应用模块化重构
- 构建系统迁移（如SCons到CMake）
- 框架升级（如AngularJS到Angular）
- 架构模式转换（如MVC到微服务）

## 相关概念
- [[Plan]] - 方法实施的基础
- [[Humanize]] - 互补的协同开发方法
- 蜂群 - 超大规模任务的增强模式
- [[Spec Coding]] - 兼容的方法论框架
- `/batch`命令 - 工具支持

**backlinks_note**: 本概念在[[Claude Code高效配置与开发实践指南]]中作为高级开发方法论被介绍，由[[yahah]]详细描述，与[[Humanize]]互补，成功应用于gem5项目。

## Related
- [[Plan]]
- [[Humanize]]
- 蜂群
- [[Spec Coding]]
- /batch