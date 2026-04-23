---
title: "Agentic Loop"
type: "concept"
sources:
  - "raw/articles/53771cca_Anthropic的Claude Code Agent效果很好有没有人深入分析其技术原理Anthropic的Claude Code Agent效果很好有.md"
tags:
  - "agent-architecture"
  - "claude-code"
  - "workflow"
  - "autonomous-execution"
  - "tool-calling"
confidence: "high"
created_at: "2026-04-18T01:05:59.587391"
updated_at: "2026-04-23T00:42:26.267656"
related:
  - "Claude Code"
  - "Extended Thinking"
  - "Model Context Protocol"
  - "Multi-Agent Orchestration"
  - "advanced-claude-code-workflow-techniques-and-architecture-analysis"
  - "Prompt Engineering"
  - "Context Window"
  - "Multi-Agent"
  - "Anthropic"
  - "Luhui Dev"
  - "Deepseek"
  - "Anthropic的Claude Code Agent效果很好，有没有人深入分析其技术原理？"
  - "Agent RL Training"
  - "AI Agent"
  - "AI Tool Chaining/Combination"
  - "Api"
  - "Cli"
  - "Conductor"
  - "Copilot"
  - "Distributed Context Management"
  - "Gemini"
  - "Mcp"
  - "Parallel Tool Calling"
  - "Prompt Combination & Meta-Prompting"
  - "ReAct (Reasoning + Acting)"
  - "Subagent"
  - "Subagents for Context Efficiency"
  - "Vibe Coding"
  - "主动输入式学习"
  - "主观使用体验 (AI 模型)"
  - "代理操作系统 (Agent Operating System)"
  - "推理层（决策第三步）"
  - "智能体自我进化"
  - "碎片化学习节奏化"
  - "ChatGPT 5.2"
  - "DeepSeek"
  - "GitHub"
  - "Google"
  - "Meta"
  - "MetaBot"
  - "Notion"
  - "AI决策五步法：提升判断与决策能力的结构化框架"
  - "Claude Code Agent技术分析与多代理架构"
  - "Claude Code Agent Technical Analysis and Multi-Agent Architecture"
  - "主流 AI 大模型演进漫谈与使用体验分享 (2023-2024 H1)"
  - "Agent"
---

# Agentic Loop

## Definition
The core architectural pattern powering [[Claude Code]] and similar autonomous coding agents. It represents a structured cycle where an AI agent processes tasks through iterative reasoning, tool selection, execution, and observation phases.

## Architecture Components

### 1. User Input Phase
- Task specification from the developer
- Context establishment and goal definition
- Initial constraints and requirements gathering

### 2. LLM Thinking Phase
- [[Extended Thinking]] mode activation for complex reasoning
- Internal deliberation and planning
- Strategy formulation for task execution

### 3. Tool Selection Phase
- Evaluation of available tools against task requirements
- Selection of optimal tool or tool combination
- Parameter configuration for tool execution

### 4. Execution Phase
- Tool invocation through [[Model Context Protocol (MCP)]] or native interfaces
- Real-time execution monitoring
- Error handling and fallback mechanisms

### 5. Observation Phase
- Analysis of tool execution results
- Success/failure evaluation
- Learning from execution outcomes

### 6. Continued Thinking Phase
- Iterative refinement based on observations
- Strategy adjustment if needed
- Decision on next action (continue, retry, or complete)

### 7. Result Return Phase
- Final output delivery to user
- Explanation of actions taken
- Documentation of process and decisions

## Implementation in Claude Code
Based on analysis by [[零一猴子]] who reverse-engineered Claude Code's npm package, the agentic loop is implemented as:
- **State Machine**: Maintains loop state across iterations
- **Context Preservation**: Carries relevant information between phases
- **Tool Registry**: Dynamic tool discovery and registration

## Advantages

### Over Traditional Code Completion
- **Autonomous Execution**: Goes beyond suggestions to actual implementation
- **Complex Task Handling**: Can manage multi-step development processes
- **Self-Correction**: Iterative refinement based on execution results

### Engineering Benefits
- **Debuggability**: Clear phase transitions make debugging easier (as noted in [[Claude]])
- **Predictability**: Structured flow enables better outcome prediction
- **Extensibility**: New tools and capabilities can be integrated into the loop

## Related Concepts
- **[[Extended Thinking]]**: The internal reasoning mechanism used during thinking phases
- **[[Tool as World Model]]**: How tools define the agent's understanding of reality
- **[[Multi-Agent Orchestration]]**: How multiple agentic loops can coordinate
- **[[Single-Loop Architecture]]**: Claude Code's design choice to maintain one main loop

## Applications
- **Autonomous Code Generation**: From requirements to implementation
- **Bug Fixing**: Diagnosis and correction cycles
- **Refactoring**: Analysis and transformation iterations
- **Documentation**: Code analysis and documentation generation

## Tags
agent-architecture, claude-code, workflow, autonomous-execution, tool-calling

## Related
- [[Claude Code]]
- [[Extended Thinking]]
- [[Model Context Protocol]]
- [[Multi-Agent Orchestration]]
- [[Prompt Engineering]]
- [[Context Window]]
- [[Multi-Agent]]
- [[Anthropic]]
- [[Luhui Dev]]
- [[Deepseek]]
- [[Anthropic的Claude Code Agent效果很好，有没有人深入分析其技术原理？]]
- [[Agent RL Training]]
- [[AI Agent]]
- [[AI Tool Chaining/Combination]]
- [[Api]]
- [[Cli]]
- [[Conductor]]
- [[Copilot]]
- [[Distributed Context Management]]
- [[Gemini]]
- [[Mcp]]
- [[Parallel Tool Calling]]
- [[Prompt Combination & Meta-Prompting]]
- [[ReAct (Reasoning + Acting)]]
- [[Subagent]]
- [[Subagents for Context Efficiency]]
- [[Vibe Coding]]
- [[主动输入式学习]]
- [[主观使用体验 (AI 模型)]]
- [[代理操作系统 (Agent Operating System)]]
- [[推理层（决策第三步）]]
- [[智能体自我进化]]
- [[碎片化学习节奏化]]
- [[ChatGPT 5.2]]
- [[DeepSeek]]
- [[GitHub]]
- [[Google]]
- [[Meta]]
- [[MetaBot]]
- [[Notion]]
- [[AI决策五步法：提升判断与决策能力的结构化框架]]
- [[Claude Code Agent技术分析与多代理架构]]
- [[Claude Code Agent Technical Analysis and Multi-Agent Architecture]]
- [[主流 AI 大模型演进漫谈与使用体验分享 (2023-2024 H1)]]
- [[Agent]]
- [[Claude]]