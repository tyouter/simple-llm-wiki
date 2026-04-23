---
title: "AI Tool Chaining/Combination"
type: "concept"
sources:
  - "wiki/sources/agent-skills-vs-mcp-technical-comparison-and-enterprise-applications.md"
  - "wiki/sources/anthropic-skills-engineering-approach-to-agent-capability-development.md"
tags:
  - "ai-tools"
  - "workflow-automation"
  - "tool-orchestration"
confidence: "high"
created_at: "2026-04-17T22:06:46.803885"
updated_at: "2026-04-23T07:23:32.373748"
---

# AI Tool Chaining/Combination

## 概述

AI工具链/组合是一种将多个专业化AI工具或Skills按流程串联使用的方法，通过组合多个小型、专注的Skills来解决复杂任务，实现能力的组合与编排。

## 核心要点

- **组合优于单一**：创建多个小型、专注的Skills让Agent组合使用，而非单一复杂工具
- **专业化分工**：每个工具或Skill专注于特定任务领域，提高执行效率和准确性
- **Token效率优化**：工具链通过Progressive Disclosure机制实现4倍Token消耗降低
- **流程编排**：将复杂任务分解为可组合的子任务单元，每个单元由专业工具处理
- **跨工具协作**：可将Claude生成的内容作为其他工具(如Gemini、Antigravity)的输入起点

## Related

- [[Skill]]
- [[Mcp]]
- ai-tool-specialization-for-design
- progressive-disclosure-mechanism
- [[Agent]]