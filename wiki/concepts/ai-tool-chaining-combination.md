---
title: "AI Tool Chaining/Combination"
type: "concept"
sources:
  - "wiki/sources/harness-engineering-explained-from-agent-loop-to-production-system-zhihu-discussion.md"
  - "wiki/sources/agent-skills-vs-mcp-technical-comparison-and-enterprise-applications.md"
  - "raw/articles/02dbcccb_Rrupmid Nyche 的想法 让 Claude Code 生成无 AI 感高品质界面比前端和 UI Pro Max 技能更强 想要 Claude.md"
tags:
  - "tool-chain"
  - "agent-orchestration"
  - "workflow-automation"
confidence: "high"
created_at: "2026-04-20T16:00:00"
updated_at: "2026-04-20T16:00:00"
related:
  - "AI Tool Specialization for Design"
  - "AI-Native Design Workflow"
  - "Prompt Engineering for Aesthetic Control"
  - "Prompt Combination & Meta-Prompting"
  - "Low-Code/No-Code Frontend via AI"
---

# AI Tool Chaining/Combination

## 概述
AI工具链组合是指将多个AI工具按特定顺序或并行组合使用，以解决复杂任务的技术策略，是Agent工程和工作流自动化的核心组成部分。

## 核心要点
- **专业化组合**：创建多个小型、专注的Skills，Agent可组合使用解决复杂任务
- **工具治理**：Harness Engineering中的关键组成部分，确保工具使用安全可控
- **并行工具调用**：性能优化技术，允许同时执行多个工具提高效率
- **MCP协议**：Anthropic的标准协议，用于连接外部工具和数据源
- **渐进式披露**：Skills框架的核心原则，分阶段加载必要信息优化上下文
- **Skills vs MCP**：MCP提供工具连接，Skills定义业务流程和执行标准

## 相关概念
- [[Agent Skills Framework|Skills]]
- [[Model Context Protocol (MCP)]]
- [[Harness Engineering]]
- [[Progressive Disclosure]]
- [[AI Tool Specialization]]
- [[Multi-Agent Orchestration]]

## 相关实体
- [[Anthropic]]
- [[Playwright CLI]]
- [[Claude Code]]

## 来源
- [src: Harness Engineering Explained: From Agent Loop to Production System]
- [src: Agent Skills vs MCP: Technical Comparison and Enterprise Applications]

---

## Additional Insights



## Example Workflow from Source
The source describes a specific chain: 1. Download XML prompts from [[designprompts.dev]] (an external resource). 2. Feed prompts to [[Claude Code]] for initial code generation. 3. (Optionally) Pass the generated code to a design-specialized agent like [[Gemini]] for enhancement. This chain combines resources and agents with different specializations ([[AI Tool Specialization for Design]]) into a cohesive [[AI-Native Design Workflow]], all guided by [[Prompt Engineering for Aesthetic Control]].

Source: [[raw/articles/02dbcccb_Rrupmid Nyche 的想法 让 Claude Code 生成无 AI 感高品质界面比前端和 UI Pro Max 技能更强 想要 Claude.md]]

## Related
- [[AI Tool Specialization for Design]]
- [[AI-Native Design Workflow]]
- [[Prompt Engineering for Aesthetic Control]]

---

## Additional Insights



## 在前端设计场景下的应用
本文展示了两种链式组合在前端设计中的具体应用：1) **提示词组合**：将多个XML设计提示词组合使用，这是 [[Prompt Combination & Meta-Prompting]] 的体现。2) **工具链建议**：根据 [[AI Tool Specialization for Design]] 的认知，建议让更擅长前端设计的Gemini或Antigravity来代替或辅助Claude Code。这两种组合都服务于 [[Low-Code/No-Code Frontend via AI]] 的最终目标，是人工构建的、基于工具特长的优化流程，可视为人类主导的 [[Agentic Loop]] 类比。

Source: [[raw/articles/02dbcccb_Rrupmid Nyche 的想法 让 Claude Code 生成无 AI 感高品质界面比前端和 UI Pro Max 技能更强 想要 Claude.md]]

## Related
- [[AI Tool Specialization for Design]]
- [[AI-Native Design Workflow]]
- [[Prompt Engineering for Aesthetic Control]]
- [[Prompt Combination & Meta-Prompting]]
- [[Low-Code/No-Code Frontend via AI]]