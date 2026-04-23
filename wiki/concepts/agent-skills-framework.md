---
title: "Agent Skills Framework"
type: "concept"
sources:
  - "raw/articles/697c42e9_Agent Skill 为何没有像 MCP 那样火爆Agent Skill 为何没有像 MCP 那样火爆.md"
  - "raw/articles/149db3c1_Skills的本质是什么Skills的本质是什么.md"
tags:
  - "agent-framework"
  - "knowledge-encapsulation"
  - "progressive-disclosure"
  - "token-optimization"
  - "anthropic"
confidence: "high"
created_at: "2026-04-18T01:17:46.828011"
updated_at: "2026-04-23T00:42:26.541663"
related:
  - "Anthropic"
  - "Progressive Disclosure"
  - "Token Efficiency Optimization"
  - "Enterprise Skill Engineering"
  - "skill-creator"
  - "Progressive Disclosure Mechanism"
  - "Skill as Asset"
  - "Skill-Creator Tool"
  - "Claude"
  - "Iterative Skill Development"
  - "Context Window Management"
  - "Skill Triggering"
  - "Skill Activation"
  - "Skill Security Considerations"
  - "AI Agent"
  - "AI Tool Chaining/Combination"
  - "AI Tool Specialization"
  - "Anthropic Skills: Engineering Approach to Agent Capability Development|Anthropic Skills Framework"
  - "CLAUDE.md配置哲学"
  - "Git仪式自动化 (Git Ceremony Automation)"
  - "GStack: Role-Based AI Development Workflow"
  - "Model Context Protocol (MCP)"
  - "Modular & Focused Skill Design"
  - "从单词到语篇的渐进练习"
  - "任务驱动的技能生成"
  - "决策系统迭代"
  - "固执己见的命令 (Opinionated Commands)"
  - "基于角色的AI开发 (Role-Based AI Development)"
  - "复杂逻辑链路处理"
  - "工具链与插件生态"
  - "战略管理知识体系构建"
  - "技能包 (Skill Pack)"
  - "技能进化模式"
  - "Playwright CLI"
  - "Superpowers插件"
  - "Agent Skills vs MCP: Technical Comparison and Enterprise Applications"
  - "AI决策五步法：提升判断与决策能力的结构化框架"
  - "Anthropic Skills Framework: Engineering Approach to Agent Capability Development"
  - "gstack：Claude工程团队 - 汇智网分析"
  - "主流 AI 大模型演进漫谈与使用体验分享 (2023-2024 H1)"
  - "Token Efficiency in AI Reasoning"
  - "Ai学习的老章"
---

# Agent Skills Framework

## Definition
[[Anthropic]]'s standardized approach to packaging agent capabilities as reusable, version-controlled knowledge packages with [[Progressive Disclosure]] architecture. This framework represents a structured methodology for developing and deploying AI agent capabilities.

## Core Principles

### Progressive Disclosure Architecture
- Only necessary information is loaded into context at each execution stage
- Minimizes token usage by avoiding information overload
- Enables efficient handling of complex workflows

### Knowledge Encapsulation
- Packages business processes, SOPs, and domain knowledge into standardized units
- Solves the "single-mode problem" through structured knowledge packaging
- Enables consistent execution across different contexts

### Reusability and Version Control
- Skills are designed as reusable components
- Support versioning for iterative improvement
- Can be shared and standardized across organizations

## Technical Advantages

### Token Efficiency
- Demonstrates 4x reduction in token consumption compared to [[Model Context Protocol|MCP]] implementations
- Particularly effective for complex workflows like browser automation
- Optimizes context window usage through intelligent information loading

### Structured Development
- Provides clear engineering lifecycle from creation to deployment
- Supports testing and iteration through tools like [[skill-creator]]
- Enables objective performance measurement through assertion testing

## Comparison with MCP

### Key Distinctions
- **MCP:** Focuses on tool connectivity and resource access
- **Skills Framework:** Defines business processes and execution standards
- **Complementary Roles:** MCP connects tools, Skills define how to use them

### Enterprise Applications
- **[[Enterprise Skill Engineering]]:** Converting business knowledge into standardized Skills
- **Process Standardization:** Ensuring consistent AI execution across operations
- **Knowledge Management:** Creating reusable knowledge packages for organizational learning

## Implementation Examples

### Playwright CLI Integration
- Uses Skills architecture for token-efficient browser automation
- Demonstrates practical advantages in real-world applications
- Shows how Skills optimize complex interaction sequences

### Cursor IDE Integration
- [[Cursor]] integrates Skills framework for AI-assisted programming
- Enables structured code generation and problem-solving
- Demonstrates rapid adoption by major development tools

## Related Concepts
- [[Progressive Disclosure]]: Core architectural principle
- [[Token Efficiency Optimization]]: Key technical advantage
- [[Enterprise Skill Engineering]]: Business application practice
- [[Skill Engineering Lifecycle]]: Development process

## Tags
agent-framework, knowledge-encapsulation, progressive-disclosure, token-optimization, anthropic

## Related
- [[AI Agent]]
- [[AI Tool Chaining/Combination]]
- [[AI Tool Specialization]]
- [[Anthropic Skills: Engineering Approach to Agent Capability Development|Anthropic Skills Framework]]
- [[CLAUDE.md配置哲学]]
- [[Git仪式自动化 (Git Ceremony Automation)]]
- [[GStack: Role-Based AI Development Workflow]]
- [[Model Context Protocol (MCP)]]
- [[Modular & Focused Skill Design]]
- [[从单词到语篇的渐进练习]]
- [[任务驱动的技能生成]]
- [[决策系统迭代]]
- [[固执己见的命令 (Opinionated Commands)]]
- [[基于角色的AI开发 (Role-Based AI Development)]]
- [[复杂逻辑链路处理]]
- [[工具链与插件生态]]
- [[战略管理知识体系构建]]
- [[技能包 (Skill Pack)]]
- [[技能进化模式]]
- [[Playwright CLI]]
- [[Superpowers插件]]
- [[Agent Skills vs MCP: Technical Comparison and Enterprise Applications]]
- [[AI决策五步法：提升判断与决策能力的结构化框架]]
- [[Anthropic Skills Framework: Engineering Approach to Agent Capability Development]]
- [[gstack：Claude工程团队 - 汇智网分析]]
- [[主流 AI 大模型演进漫谈与使用体验分享 (2023-2024 H1)]]
- [[Token Efficiency in AI Reasoning]]
- [[Ai学习的老章]]
[[Anthropic]], [[Progressive Disclosure]], [[Token Efficiency Optimization]], [[Enterprise Skill Engineering]], [[skill-creator]]

## Related
- [[Anthropic]]
- [[Progressive Disclosure]]
- [[Token Efficiency Optimization]]
- [[Enterprise Skill Engineering]]
- [[skill-creator]]

---

## Extended Definition

The **Agent Skills Framework** is an open-format standard developed by [[Anthropic]] for endowing AI agents like [[Claude]] with new, reusable capabilities and domain expertise. It centers on packaging a capability as a self-contained directory with a `SKILL.md` file containing instructions, metadata, and optional supporting resources (scripts, references). This design enables 'write once, use anywhere' portability across compatible platforms (e.g., [[Claude Code]]), moving beyond one-off prompts to create durable, shareable assets. A core architectural innovation is the [[Progressive Disclosure Mechanism]], which efficiently manages the agent's [[Context Window Management|context window]] by loading skill information in tiers. The framework formalizes the entire lifecycle, from creation using the [[Skill-Creator Tool]] to activation via [[Skill Triggering]], embodying the principle of [[Skill as Asset]]. Its adoption signifies a shift from ad-hoc [[Prompt Engineering]] to systematic [[Iterative Skill Development]] of reliable, testable agent capabilities.

## Related
- [[Anthropic]]
- [[Progressive Disclosure]]
- [[Token Efficiency Optimization]]
- [[Enterprise Skill Engineering]]
- [[skill-creator]]
- [[Progressive Disclosure Mechanism]]
- [[Skill as Asset]]
- [[Skill-Creator Tool]]
- [[Claude]]
- [[Iterative Skill Development]]
- [[Context Window Management]]

---

## Additional Insights



## Enhanced Insights from Analysis
The framework is positioned not just as a technical specification but as the foundation for a broader engineering discipline. It enables the shift from [[Prompt Engineering]] to building [[Skill as Asset|durable assets]], facilitated by tools like the [[Skill-Creator Tool]]. Key to its operation is the dynamic interplay between [[Skill Triggering]] (the decision to use a skill) and [[Skill Activation]] (the loading of its instructions), all governed by the need for efficient [[Context Window Management]]. As the ecosystem matures, formal [[Skill Security Considerations]] have become an integral part of the framework's best practices.

Source: [[Skill]]

## Related
- [[Anthropic]]
- [[Progressive Disclosure]]
- [[Token Efficiency Optimization]]
- [[Enterprise Skill Engineering]]
- [[skill-creator]]
- [[Progressive Disclosure Mechanism]]
- [[Skill as Asset]]
- [[Skill-Creator Tool]]
- [[Claude]]
- [[Iterative Skill Development]]
- [[Context Window Management]]
- [[Skill Triggering]]
- [[Skill Activation]]
- [[Skill Security Considerations]]