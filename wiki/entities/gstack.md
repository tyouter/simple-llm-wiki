---
title: "GStack"
type: "entity"
sources:
  - "wiki/sources/gstack-role-based-ai-development-workflow-for-claude-code.md"
  - "wiki/sources/GStack角色化AI开发工作流.md"
  - "raw/articles/093f7d65_gstackClaude工程团队.md"
tags:
  - "workflow"
  - "claude-code"
  - "role-based"
confidence: "high"
created_at: "2026-04-20T00:00:00"
updated_at: "2026-04-23T00:42:26.970054"
related:
  - "Garry Tan"
  - "基于角色的AI开发"
  - "技能包"
  - "固执己见的命令"
  - "车道限制"
  - "单一模糊模式问题"
  - "代理操作系统"
  - "Convergent Evolution (in AI Tools)"
  - "Brian Chesky"
  - "gstack：Claude工程团队 - 汇智网分析"
  - "金融分析高级AI Agent架构"
---

# GStack

## 概述
由Garry Tan创建的基于角色的Claude Code AI开发工作流，包含八个预设斜杠命令，每个命令代表不同的工程角色，旨在通过认知职责分离解决"单模式问题"。

## 基本信息
- 类型：工作流系统/Skill Pack
- 创建者：Garry Tan
- 相关领域：AI开发工作流、角色化开发

## 八个角色命令
1. /plan-ceo-review：定义"十星体验"和产品愿景
2. /plan-engineer：转化为技术规范和实施计划
3. /implement：核心编码命令
4. /review-pr：代码审查角色
5. /qa-staging：QA工程师测试角色
6. /qa-prod：生产环境验证
7. /debug：故障排除和修复
8. /refactor：代码结构改进

## 核心原则
- [[Role-Based AI Development]]：认知职责分离
- Plan-First Mandate：先规划后实施
- Parallel Execution：支持并行执行
- 解决[[Single-Mode Problem]]

## 相关概念
- [[Role-Based AI Development]]
- [[Agent Operating System]]
- [[Claude Code Skills系统]]

## 相关
- [[Garry Tan]]
- [[Claude Code]]
- [[TurboDocx]]

---

**gstack** 是一个由[[Garry Tan]]开源、专为[[Claude Code]]环境设计的[[技能包 (Skill Pack)]]。它包含了八个[[固执己见的命令 (Opinionated Commands)]]，每个命令对应软件开发流程中的一个特定工程角色，是[[基于角色的AI开发 (Role-Based AI Development)]]范式的具体实现和标杆案例。

其八个命令覆盖了从战略规划到发布回顾的全流程：`/plan-ceo-review`（[[Brian Chesky模式 (Brian Chesky Mode)]]）、`/plan-eng-review`（工程规划）、`/implement`（实现）、`/review`（[[对抗性通过 (Adversarial Pass)]]审查）、`/browse`（[[视觉回归检查 (Visual Regression Checking)]]）、`/ship`（[[Git仪式自动化 (Git Ceremony Automation)]]）、`/retro`（[[提交分析模式识别 (Commit Analysis Pattern Discovery)]]）以及`/sync`（同步）。gstack的核心设计哲学是[[车道限制 (Lane Restriction)]]，即每个技能严格限定在其职责范围内，以模拟真实工程组织的专业分工。

gstack的诞生是为了从根本上解决[[单一模糊模式问题 (Single Fuzzy Mode Problem)]]，即通用AI编程伙伴的局限性。它通过强制性的角色分离和阶段化流程，提升了AI在各个环节的输出质量和针对性。项目本身正在演变为一个更复杂的[[代理操作系统 (Agent Operating System)]]的实验平台，探索如何使用类似[[Conductor]]的工具并行运行多个代理会话。gstack的成功和其引发的[[趋同进化 (Convergent Evolution)]]现象，标志着AI编程工具向专业化、结构化方向迈出了关键一步。

## Related
- [[Garry Tan]]
- [[基于角色的AI开发 (Role-Based AI Development)]]
- [[技能包 (Skill Pack)]]
- [[固执己见的命令 (Opinionated Commands)]]
- [[车道限制 (Lane Restriction)]]
- [[单一模糊模式问题 (Single Fuzzy Mode Problem)]]
- [[Convergent Evolution (in AI Tools)]]
- [[Brian Chesky]]
- [[gstack：Claude工程团队 - 汇智网分析]]
- [[金融分析高级AI Agent架构]]
- [[代理操作系统 (Agent Operating System)]]