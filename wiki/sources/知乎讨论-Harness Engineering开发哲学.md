---
title: "知乎讨论：Harness Engineering开发哲学"
type: "source"
sources:
  - "raw/articles/b99fad36_Harness Engineering的本质是什么Harness Engineering的本质是什么.md"
tags:
  - "harness-engineering"
  - "ai-agent"
  - "软件工程"
  - "控制论"
confidence: "high"
created_at: "2026-04-20T12:00:00"
updated_at: "2026-04-20T12:00:00"
related:
  - "Harness Engineering"
  - "控制论与Agent"
  - "Agent环境设计"
---

# 知乎讨论：Harness Engineering开发哲学

## 核心内容

这篇知乎讨论深入解析了 Harness Engineering 的本质，将其定义为 Agent 运行时的"工程环境总和"。

### Harness 定义

**核心公式升级**：
- 旧公式：Agent = Loop(LLM + Context + Tools)
- 新公式：Agent = Loop(Model + Harness)

**本质**：Harness 不是模型、不是 Prompt、不是 Tool Call、不是框架。Harness 是 Agent 运行时的"工程环境总和"。

### Harness 五层架构

1. **上下文装配系统**：提示词不是静态文档，而是动态拼装系统
   - 基础模板
   - 用户偏好（SOUL.md）
   - 项目上下文（AGENTS.md）
   - Skills工具描述
   - 工具定义JSON

2. **工具治理系统**：
   - 工具定义层：声明式DSL
   - 风险与审批层：read/write/execute/critical分级
   - 编排层：统一入参校验、审批拦截、结果裁剪

3. **安全与审批系统**：
   - 子进程管理
   - 命令守卫
   - 审批系统

4. **反馈与状态系统**：
   - XML system_hint承载异常状态
   - 工具执行结果翻译成模型可消费的反馈

5. **熵管理系统**：
   - 过期规则失效
   - 长上下文压缩
   - 低价值历史退出

### 控制论视角

文章将 Harness Engineering 与控制论联系起来：

| 时代 | 传感器 | 执行器 | 人类角色 |
|------|--------|--------|----------|
| 蒸汽机 | 飞球 | 阀门 | 设计调速器 |
| Kubernetes | metrics/health check | 调度器 | 编写目标spec |
| Harness Engineering | 测试/Linter/可观测性 | LLM | 设计运行环境 |

**核心哲学**：Humans steer. Agents execute. 人负责掌舵，Agent负责执行。

### 实践建议

1. 先别急着追最强模型，先把环境搭起来
2. 把工具系统做成"系统"
3. 上下文不要写成一坨
4. 安全边界必须在运行时
5. 所有失败都尽量可解释
6. 给长任务设计状态与恢复机制
7. 定期做熵管理

### 关键洞察

> Agent 的重点从来都不在模型，而在环境。

> 真正的安全边界，必须落在运行时。你不能把"请不要执行危险命令"写在 prompt 里，然后假装问题解决了。

> Harness 级别的 agent 靠的是"即便模型不听话，系统也有边界"。

## Related
- [[Harness Engineering]]
- [[控制论与Agent]]
- [[Agent环境设计]]
- [[熵管理]]