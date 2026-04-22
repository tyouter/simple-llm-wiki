---
title: "Claude"
type: "entity"
sources:
  - "wiki/sources/claude-code-agent-technical-analysis-and-multi-agent-architecture.md"
  - "wiki/sources/advanced-claude-code-workflow-techniques-and-architecture-analysis.md"
  - "raw/videos/ab312a84_AI真正改变的不是效率而是决策质量.md"
  - "raw/articles/149db3c1_Skills的本质是什么Skills的本质是什么.md"
tags:
  - "ai-model"
  - "anthropic"
  - "llm"
confidence: "high"
created_at: "2026-04-20T00:00:00"
updated_at: "2026-04-20T00:00:00"
related:
  - "工具链专业化组合"
  - "结构层（决策第二步）"
  - "ChatGPT / GPT"
  - "AI Tool Specialization"
  - "Anthropic"
  - "Agent Skills Framework"
  - "Progressive Disclosure Mechanism"
---

# Claude

## 概述
Anthropic开发的大型语言模型系列，以安全性和可控性著称，在代码生成、推理和对话方面表现卓越，是Claude Code等产品的底层模型。

## 基本信息
- 类型：AI模型系列
- 开发者：Anthropic
- 相关领域：自然语言处理、代码生成、AI安全

## 模型演进
- Claude Sonnet 3.5
- Claude Opus 4.6
- 模型能力按指数级改进

## 特点
- 强调AI安全和对齐
- 优秀的代码生成能力
- 支持长上下文处理

## 相关概念
- [[Claude Code]]
- [[Anthropic]]
- [[Model Context Protocol (MCP)]]
- [[国产大模型]]（作为对比参考）

## 相关
- [[Claude.ai]]
- [[Claude Code]]
- [[OpenAI]]

---

## 概述
由Anthropic开发的大型语言模型，以其较强的逻辑性、安全性和长上下文处理能力著称。

## 在本框架中的角色
在[[AI决策五步法：提升判断与决策能力的结构化框架]]中，**Claude** 被定位为**负责[[结构层（决策第二步）]]的逻辑收敛与严谨分析**的关键工具。作者观察到，与[[ChatGPT / GPT]]相比，Claude在分析问题时往往更偏向于严谨、细致和逻辑收敛，擅长对复杂信息进行梳理、分类和深度剖析。因此，在[[工具链专业化组合]]的工作流中，Claude常被用于处理[[信息层（决策第一步）]]收集来的原始信息，将其结构化，并帮助发现决策者自身的认知盲点和逻辑矛盾，为后续GPT的开放推演打下坚实的基础。这种分工是[[AI Tool Specialization|AI工具专业化]]理念的典型体现。

## 相关标签
#Anthropic #逻辑分析 #长上下文 #安全AI #信息结构化

## Related
- [[工具链专业化组合]]
- [[结构层（决策第二步）]]
- [[ChatGPT / GPT]]
- [[AI Tool Specialization]]

---

**Claude** is the AI assistant (large language model) developed by [[Anthropic]]. The [[Agent Skills Framework]] is described as evolving into a 'core capability layer' for Claude, fundamentally integrated into its functionality and expansion. Claude is the primary agent platform for which Skills are engineered, using the [[Progressive Disclosure Mechanism]] to manage its [[Context Window Management|context window]] and dynamically [[Skill Activation|activate]] capabilities based on [[Skill Triggering]]. The engineering practices surrounding the framework, including the use of the [[Skill-Creator Tool]], are aimed at augmenting Claude's native abilities with specialized, reusable [[Skill as Asset|skill assets]].

## Related
- [[工具链专业化组合]]
- [[结构层（决策第二步）]]
- [[ChatGPT / GPT]]
- [[AI Tool Specialization]]
- [[Anthropic]]
- [[Agent Skills Framework]]
- [[Progressive Disclosure Mechanism]]