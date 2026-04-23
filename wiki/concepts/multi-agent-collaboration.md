---
title: "Multi-Agent Collaboration"
type: "concept"
sources:
  - "wiki/sources/OpenClaw高级使用经验多Agent协作.md"
  - "wiki/sources/Claude Code Agent技术分析与多代理架构.md"
tags:
  - "agent-architecture"
  - "collaboration"
  - "orchestration"
  - "openclaw"
confidence: "high"
created_at: "2026-04-20T00:24:41.160867"
updated_at: "2026-04-22T23:50:25.616260"
---

# Multi-Agent Collaboration

多Agent协作是多个专用AI Agent协同完成复杂任务的架构模式，通过分工合作突破单Agent的能力和上下文限制。

## 核心要点

- **三种协作模式**：线性流水线、依赖图并行、AI辩论
- **专职分工**：编码Agent、测试Agent、文档Agent、审查Agent各司其职
- **突破单模式限制**：解决一个模型处理所有阶段的Single-Mode Problem
- **上下文扩展**：分布式Agent突破单个上下文窗口限制
- **生产级系统**：一条指令交付测试覆盖率98%的生产级代码

## Related
- [[OpenClaw]]
- [[Claude Code]]
- [[Single-Mode Problem]]
- [[MetaBot]]
- [[Claude Code Agent技术分析与多代理架构]]
- [[AI Agent Engineering Career Path]]
- [[AI玩家日志]]
- [[Zhihu: 从后端开发转型AI Agent工程师的路线图]]
- [[OpenClaw高级使用经验多Agent协作]]