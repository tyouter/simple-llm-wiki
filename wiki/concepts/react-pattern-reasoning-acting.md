---
title: "ReAct Pattern (Reasoning + Acting)"
type: "concept"
sources:
  - "raw/raw/articles/0007311f_怎么成为一个ai agent 工程师怎么成为一个ai agent 工程师.md"
tags:
  - "agent-pattern"
  - "execution-loop"
  - "reasoning-systems"
  - "tool-integration"
  - "foundational-concept"
confidence: "high"
created_at: "2026-04-17T16:57:33.440111"
updated_at: "2026-04-17T16:57:33.440111"
related:
  - "Tool-Integrated Reasoning (TIR)"
  - "SubAgent Architecture"
  - "Model Context Protocol (MCP)"
  - "Domain-Specific Language (DSL) for AI Agents"
  - "AI Agent"
---

# ReAct Pattern (Reasoning + Acting)

## Definition
The fundamental execution loop in [[AI Agent]] systems where the model alternates between reasoning about what to do and acting by calling tools or taking actions, then observing results before repeating the cycle.

## Core Loop
1. **Reason**: Analyze current state and determine next action
2. **Act**: Execute action using available tools or capabilities
3. **Observe**: Process results and update internal state
4. **Repeat**: Continue until task completion or termination condition

## Implementation in Tutorial Context
The [[Zhihu Discussion: AI Agent Engineering Career Paths and Technical Approaches]] includes a practical 6-step tutorial that builds upon the ReAct pattern as a foundation for agent implementation.

## Key Components

### Reasoning Phase
- Problem decomposition
- Tool selection
- Parameter determination
- Contingency planning

### Acting Phase
- Tool invocation via protocols like Model Context Protocol (MCP)
- Action execution
- Error handling

### Observation Phase
- Result parsing
- State update
- Success/failure determination

## Advanced Variations

### [[Tool-Integrated Reasoning (TIR)]]
A more formal approach that mathematically guarantees expanded capabilities through tool integration.

### [[SubAgent Architecture]]
Decomposing complex reasoning into specialized sub-agents while maintaining the ReAct pattern at each level.

## Design Considerations

### Loop Control
- Termination conditions
- Maximum iteration limits
- Progress monitoring

### State Management
- Maintaining context across iterations
- Handling partial failures
- Supporting backtracking

### Tool Integration
- [[Model Context Protocol (MCP)]] for standardized tool access
- Error recovery mechanisms
- Parallel tool execution where possible

## Relation to Career Development
Mastering ReAct pattern implementation is identified as a foundational skill for [[AI Agent]] engineers, with more advanced concepts like [[Domain-Specific Language (DSL) for AI Agents]] building upon this foundation.

## Practical Applications
- **Customer Support Agents**: Reason about user issues, query knowledge bases, provide solutions
- **Development Agents**: Plan implementation, write code, test results
- **Research Agents**: Formulate hypotheses, run experiments, analyze data
- **Content Agents**: Plan content structure, research information, write drafts

**Source**: [[Zhihu Discussion: AI Agent Engineering Career Paths and Technical Approaches]]

## Tags
agent-pattern, execution-loop, reasoning-systems, tool-integration, foundational-concept

## Related
[[Tool-Integrated Reasoning (TIR)]], [[SubAgent Architecture]], [[Model Context Protocol (MCP)]], [[Domain-Specific Language (DSL) for AI Agents]], [[AI Agent]]

## Related
- [[Tool-Integrated Reasoning (TIR)]]
- [[SubAgent Architecture]]
- [[Model Context Protocol (MCP)]]
- [[Domain-Specific Language (DSL) for AI Agents]]
- [[AI Agent]]