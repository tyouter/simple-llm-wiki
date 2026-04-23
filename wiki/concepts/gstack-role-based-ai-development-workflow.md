---
title: "GStack: Role-Based AI Development Workflow"
type: "concept"
sources:
  - "wiki/sources/gstack-role-based-ai-development-workflow-for-claude-code.md"
tags:
  - "workflow"
  - "role-based"
  - "claude-code"
  - "multi-agent"
confidence: "high"
created_at: "2026-04-17T21:56:25.442155"
updated_at: "2026-04-23T00:53:47.183870"
---

# GStack: Role-Based AI Development Workflow (GStack角色化AI开发工作流)

## 概述
GStack是由Garry Tan创建的Claude Code技能包，引入八个专业化斜杠命令，每个代表不同的工程角色（CEO、Engineer、QA等），实现结构化的角色分离开发工作流。

## 核心要点
- **八个角色命令**：
  - `/plan-ceo-review`：CEO视角，定义"10-star体验"和产品愿景
  - `/plan-engineer`：工程师视角，转化为技术规格和实施计划
  - `/implement`：核心编码，基于批准计划编写代码
  - `/review-pr`：代码评审，评估质量和潜在问题
  - `/qa-staging`：QA工程师，模拟测试环境验证
  - `/qa-prod`：生产级最终验证
  - `/debug`：故障排查修复
  - `/refactor`：代码重构优化
- **Role-Based AI Development**：通过角色分离实现认知职责分离，避免Single-Mode Problem
- **Plan-First Mandate**：强制规划先行，确保构建正确的东西再正确构建
- **并行执行**：使用Conductor工具可并行运行多个Claude Code会话
- **收敛演化**：与TurboDocx的"Director/Manager/Team"模型概念相似，代表结构化多角色趋势

## 相关概念
- [[Role-Based AI Development]]
- [[Single-Mode Problem]]
- [[Convergent Evolution (in AI Tools)]]
- [[Agent Operating System]]
- [[Agent Skills Framework|Skills]]
- [[Claude Code]]

## 相关实体
- [[Garry Tan]]
- [[Brian Chesky]]
- [[Claude Code]]
- [[Conductor]]
- [[TurboDocx]]

## 来源
- [src: GStack: Role-Based AI Development Workflow for Claude Code]
## Related
- [[Anthropic Skills: Engineering Approach to Agent Capability Development|Anthropic Skills Framework]]

