---
title: "Simplest Working Solution Principle"
type: "concept"
sources:
  - "raw\articles\3f3fc556_Claude code 产品经理Cat Wu亲述我是如何用AI彻底重构PM工作流的.md"
tags:
  - "engineering-principle"
  - "simplicity"
  - "technical-debt"
  - "adaptability"
  - "optimization"
confidence: "high"
created_at: "2026-04-17T22:10:58.491222"
updated_at: "2026-04-17T22:10:58.491222"
related:
  - "Anthropic"
  - "Cat Wu"
  - "Model-Capability-Driven Product Evolution"
  - "AI-Exponential Product Management"
  - "Prototype-First Development"
---

# Simplest Working Solution Principle

## Definition
An organizational principle at [[Anthropic]] that favors the simplest implementation that solves a problem, avoiding complex workarounds for AI model limitations that are likely to become obsolete with next-generation models. This approach recognizes that in an environment of exponential AI improvement, optimization for current limitations has limited value.

## Core Philosophy

### Avoiding Over-Engineering for Limitations
When AI models have limitations, traditional engineering approaches might create:
- Complex architectures to work around model constraints
- Elaborate preprocessing or postprocessing pipelines
- Sophisticated error handling for edge cases

The Simplest Working Solution Principle argues that instead, teams should:
1. Implement the simplest solution that works with current capabilities
2. Accept that some edge cases may not be perfectly handled
3. Plan to revisit the implementation when model capabilities improve

### Betting on Exponential Improvement
This principle is based on the observation that AI models improve exponentially. Therefore:
- Today's limitation may be gone in the next model release
- Engineering workarounds have short useful lifespans
- Simple solutions can often be replaced entirely rather than incrementally improved

## Implementation at Anthropic

### Practical Applications
According to [[Cat Wu]], this principle guides decisions such as:
- Choosing straightforward implementations over optimized ones
- Accepting "good enough" solutions that leverage current model capabilities
- Avoiding complex architectures designed to compensate for model weaknesses
- Prioritizing speed of implementation over perfection

### Integration with Other Practices
This principle works with:
- **[[Prototype-First Development]]**: Simple prototypes are faster to build and test
- **[[Model-Capability-Driven Product Evolution]]**: Simple solutions are easier to replace when capabilities improve
- **[[Edge Exploration Projects (Side Quests)]]**: Simple implementations enable rapid experimentation

## Benefits

### Development Speed
Simple solutions can be implemented faster, allowing:
- More rapid iteration and testing
- Quicker user feedback cycles
- Faster adaptation to changing requirements

### Reduced Technical Debt
By avoiding complex workarounds for model limitations:
- Codebases remain cleaner and more maintainable
- Less time is spent maintaining obsolete optimizations
- Teams can focus on adding value rather than managing complexity

### Adaptability
Simple implementations are easier to:
- Replace when better approaches become possible
- Modify as requirements change
- Understand and maintain by different team members

## Contrast with Traditional Approaches
This principle contradicts traditional engineering wisdom that often emphasizes:
- Comprehensive handling of all edge cases
- Optimization for current constraints
- Building for long-term stability
- Avoiding temporary solutions

## Source
Described by Cat Wu as an organizational principle at Anthropic.

## Tags
engineering-principle, simplicity, technical-debt, adaptability, optimization

## Related
- [[Anthropic]]
- [[Cat Wu]]
- [[Model-Capability-Driven Product Evolution]]
- [[AI-Exponential Product Management]]
- [[Prototype-First Development]]