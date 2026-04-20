---
title: "Harness Engineering"
type: "concept"
sources:
  - "wiki/sources/zhihu-discussion-harness-engineering-agent-development-philosophy.md"
tags:
  - "ai-agent"
  - "software-engineering"
  - "cybernetics"
confidence: "high"
created_at: "2026-04-20T12:00:00"
updated_at: "2026-04-20T12:00:00"
---

# Harness Engineering

## 核心概念

Harness Engineering 是 Agent 运行时的"工程环境总和"，是让 Agent 能被稳定驾驭的环境系统。

### 公式演进

**旧公式**：Agent = Loop(LLM + Context + Tools)

**新公式**：Agent = Loop(Model + Harness)

### Harness 五层架构

| 层级 | 功能 | 关键组件 |
|------|------|----------|
| 上下文装配 | 动态拼装提示词 | 基础模板、SOUL.md、AGENTS.md |
| 工具治理 | 系统化工具管理 | DSL定义、风险分级、编排层 |
| 安全审批 | 运行时边界 | 子进程管理、命令守卫、审批系统 |
| 反馈状态 | 质量闭环 | system_hint、状态恢复 |
| 熵管理 | 系统健康 | 规则失效、上下文压缩 |

### 与其他工程阶段对比

| 阶段 | 核心问题 | 类比 |
|------|----------|------|
| Prompt Engineering | 怎么说清楚 | 写一封信 |
| Context Engineering | 给什么信息 | 准备档案 |
| Harness Engineering | 环境怎么搭 | 一座工厂 |

### 控制论视角

Harness Engineering 是控制论的第三次现身：
- 第一次：瓦特调速器（蒸汽机）
- 第二次：Kubernetes（容器编排）
- 第三次：Harness（Agent运行时）

### 核心哲学

> Humans steer. Agents execute.

> Agent的重点不在模型，而在环境。

> Harness级别的agent靠的是"即便模型不听话，系统也有边界"。

## Related
- [[Agent环境设计]]
- [[控制论与Agent]]
- [[熵管理]]
