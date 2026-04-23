---
title: "LangGraph"
type: "entity"
sources:
  - "raw/articles/40136f0f_为什么感觉现在AI Agent都是雷声大雨点小为什么感觉现在AI Agent都是雷声大雨点小.md"
  - "raw/articles/0007311f_怎么成为一个ai agent 工程师怎么成为一个ai agent 工程师.md"
  - "raw/articles/53771cfc_最好用的Agent框架是什么最好用的Agent框架是什么.md"
  - "raw/articles/cde8da65_怎么成为一个 ai agent 工程师怎么成为一个 ai agent 工程师.md"
tags:
  - "framework"
  - "state-machines"
  - "workflow-orchestration"
  - "langchain"
  - "multi-agent-systems"
confidence: "high"
created_at: "2026-04-17T21:56:25.395565"
updated_at: "2026-04-23T00:42:26.901728"
related:
  - "Multi-Tool Orchestration with State Machines"
  - "AI Agent Cognitive Architecture"
  - "Advanced AI Agent Architecture for Financial Analysis"
  - "杞鋂"
  - "Model Context Protocol"
  - "Harness Engineering"
  - "Claude Code"
  - "Code Review"
  - "Ai Agent"
  - "怎么成为一个ai agent 工程师？"
  - "Embedding"
  - "Agent"
  - "Rag"
  - "Git"
  - "为什么感觉现在AI Agent都是雷声大雨点小？"
  - "Plan Mode"
  - "Subagent"
  - "Openclaw"
  - "最好用的Agent框架是什么？"
  - "Reinforcement Learning"
  - "Prompt Engineering"
  - "Multi-Agent"
  - "Openviking"
  - "怎么成为一个 ai agent 工程师？"
  - "AI Agent Engineering Career Path"
  - "DeepAgents框架"
  - "AutoGen"
  - "CrewAI"
  - "Finalchemist"
  - "AI Agent框架对比分析"
  - "Zhihu: 从后端开发转型AI Agent工程师的路线图"
  - "金融分析高级AI Agent架构"
  - "Api"
  - "Cli"
  - "Copilot"
  - "Deepseek"
  - "Hooks"
  - "Mcp"
  - "Skill"
  - "Skills"
  - "如何成为 AI Agent 工程师？—— 知乎问答分析"
---

# LangGraph

## Description
A framework used to build reasoning engines and state machines for multi-agent systems. In the context of [[Advanced AI Agent Architecture for Financial Analysis]], LangGraph replaced deprecated LangChain functions to create the orchestration layer that coordinates specialized agents.

## Primary Function
LangGraph enables [[Multi-Tool Orchestration with State Machines]] by providing:
1. **Graph-based workflow definition**: Creating nodes and edges to represent cognitive processes
2. **State management**: Maintaining context across multiple steps of problem-solving
3. **Conditional transitions**: Moving between tools based on intermediate results
4. **Error handling and recovery**: Managing failures in individual components

## Key Features
### For AI Agent Development
1. **Declarative Workflow Definition**: Specify agents and tools as nodes in a graph
2. **Shared State**: Maintain context that all nodes can access and modify
3. **Conditional Logic**: Define rules for transitioning between nodes based on outputs
4. **Human-in-the-Loop**: Support for pausing workflows for human input
5. **Streaming Support**: Real-time updates as the workflow progresses

## Implementation in Financial Analysis
In the system described by [[杞鋂]], LangGraph is used to:
1. Coordinate the "Document Librarian" (RAG), "Data Analyst" (SQL), and "Intelligence Scout" (web search) agents
2. Implement quality checkpoints for [[Self-Verification and Quality Auditing in AI Systems]]
3. Manage the overall [[AI Agent Cognitive Architecture]]
4. Handle different types of financial queries with appropriate tool sequences

## Advantages Over Simpler Approaches
- **Explicit Control Flow**: Clear visualization of how information flows through the system
- **Robust Error Handling**: Built-in mechanisms for handling tool failures
- **Modular Design**: Easy to add, remove, or modify individual components
- **Debugging Support**: Traceability of decisions and state changes

## Relation to LangChain
While part of the LangChain ecosystem, LangGraph represents a more sophisticated approach to agent orchestration compared to earlier LangChain agent implementations. It addresses limitations in:
- Complex workflow management
- State persistence across multiple steps
- Conditional execution paths
- Long-running processes

## Common Use Cases
1. **Multi-step reasoning problems**: Where different tools are needed at different stages
2. **Quality-controlled workflows**: With verification steps between processing stages
3. **Adaptive problem-solving**: Where the approach changes based on intermediate results
4. **Human-AI collaboration**: Workflows that sometimes require human input

## Tags
framework, state-machines, workflow-orchestration, langchain, multi-agent-systems

## Related
- [[Model Context Protocol]]
- [[Harness Engineering]]
- [[Claude Code]]
- [[Code Review]]
- [[AI Agent]]
- [[怎么成为一个ai agent 工程师？]]
- [[Embedding]]
- [[Agent]]
- [[Rag]]
- [[Git]]
- [[为什么感觉现在AI Agent都是雷声大雨点小？]]
- [[Plan Mode]]
- [[Subagent]]
- [[OpenClaw]]
- [[最好用的Agent框架是什么？]]
- [[Reinforcement Learning]]
- [[Prompt Engineering]]
- [[Multi-Agent]]
- [[Openviking]]
- [[怎么成为一个 ai agent 工程师？]]
- [[AI Agent Engineering Career Path]]
- [[DeepAgents框架]]
- [[AutoGen]]
- [[CrewAI]]
- [[Finalchemist]]
- [[AI Agent框架对比分析]]
- [[Zhihu: 从后端开发转型AI Agent工程师的路线图]]
- [[金融分析高级AI Agent架构]]
- [[Api]]
- [[Cli]]
- [[Copilot]]
- [[Deepseek]]
- [[Hooks]]
- [[Mcp]]
- [[Skill]]
- [[Skills]]
- [[如何成为 AI Agent 工程师？—— 知乎问答分析]]
[[Multi-Tool Orchestration with State Machines]], [[AI Agent Cognitive Architecture]], [[Advanced AI Agent Architecture for Financial Analysis]], [[杞鋂]]

## Related
- [[Multi-Tool Orchestration with State Machines]]
- [[AI Agent Cognitive Architecture]]
- [[Advanced AI Agent Architecture for Financial Analysis]]
- [[杞鋂]]