---
title: "Skills vs Tools Distinction"
type: "concept"
sources:
  - "raw\raw\articles\0007311f_怎么成为一个ai agent 工程师怎么成为一个ai agent 工程师.md"
tags:
  - "agent-design"
  - "capability-modeling"
  - "expertise-encoding"
  - "domain-knowledge"
  - "implementation-pattern"
confidence: "high"
created_at: "2026-04-17T16:57:33.440111"
updated_at: "2026-04-17T16:57:33.440111"
related:
  - "Domain-Specific Language (DSL) for AI Agents"
  - "Tool-Integrated Reasoning (TIR)"
  - "SubAgent Architecture"
  - "AI Agent"
---

# Skills vs Tools Distinction

## Definition
A conceptual framework for [[AI Agent]] design that differentiates between:
- **Tools**: What an agent can do (capabilities, APIs, functions)
- **Skills**: How to do it effectively (domain knowledge, best practices, execution strategies)

## Detailed Explanation

### Tools (Capabilities)
- External APIs, functions, or services the agent can invoke
- Defined interfaces with input/output specifications
- Examples: Database queries, calculation functions, web APIs, file operations

### Skills (Expertise)
- Knowledge of when and how to use tools effectively
- Domain-specific strategies and best practices
- Problem-solving approaches and heuristics
- Quality standards and validation methods

## Importance in Agent Design

### Beyond Tool Integration
Merely giving agents access to tools is insufficient—they need the skills to use them effectively, similar to how human professionals need both tools and expertise.

### Knowledge Encoding
Skills represent the encoding of domain expertise into executable form, often implemented using [[Domain-Specific Language (DSL) for AI Agents]].

### Transfer Learning
Skills can potentially be transferred between similar domains or adapted to new contexts.

## Implementation Approaches

### Skill Libraries
Collections of reusable skill implementations that can be combined for different tasks.

### Skill Composition
Building complex capabilities by combining simpler skills.

### Skill Adaptation
Modifying existing skills for new domains or constraints.

## Relation to Other Concepts

### [[Domain-Specific Language (DSL) for AI Agents]]
DSLs often encode skills in structured, executable form.

### [[Tool-Integrated Reasoning (TIR)]]
Skills enhance tool integration by providing strategic guidance on tool usage.

### [[SubAgent Architecture]]
Different sub-agents may specialize in different skill sets.

## Design Considerations

### Skill Granularity
Balancing between highly specific skills and more general, adaptable ones.

### Skill Discovery
Mechanisms for agents to identify which skills are relevant to a given problem.

### Skill Validation
Ensuring skills produce correct and reliable results.

## Career Implications
Understanding the skills vs tools distinction helps [[AI Agent]] engineers design more capable and reliable systems that go beyond simple tool invocation to embody true expertise.

**Source**: [[Zhihu Discussion: AI Agent Engineering Career Paths and Technical Approaches]]

## Tags
agent-design, capability-modeling, expertise-encoding, domain-knowledge, implementation-pattern

## Related
[[Domain-Specific Language (DSL) for AI Agents]], [[Tool-Integrated Reasoning (TIR)]], [[SubAgent Architecture]], [[AI Agent]]

## Related
- [[Domain-Specific Language (DSL) for AI Agents]]
- [[Tool-Integrated Reasoning (TIR)]]
- [[SubAgent Architecture]]
- [[AI Agent]]