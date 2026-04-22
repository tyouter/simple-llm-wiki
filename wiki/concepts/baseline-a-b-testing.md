---
title: "Baseline A/B Testing"
type: "concept"
sources:
  - "raw/articles/149db3c1_Skills的本质是什么Skills的本质是什么.md"
tags:
  - "Testing"
  - "Evaluation"
  - "Empirical Method"
confidence: "high"
created_at: "2026-04-21T18:28:45.947918"
updated_at: "2026-04-21T18:28:45.947918"
related:
  - "Skill-Creator Tool"
  - "Iterative Skill Development"
  - "Skill Evaluation & Assertions"
  - "Skill as Asset"
---

**Baseline A/B Testing** is a core empirical evaluation method within the [[Skill-Creator Tool]] workflow. It compares an agent's performance on a task with the [[Skills (Anthropic Framework)|Skill]] enabled (variant A) versus with it disabled or with a previous version (variant B). For each test case, two agent subprocesses are run in parallel, and their outputs are saved for comparison. This method establishes whether a skill provides a 'quantifiable lift' over the agent's native capabilities, preventing the illusion of improvement. It is the foundational step in [[Iterative Skill Development]], generating the data needed for [[Skill Evaluation & Assertions]]. By providing a clear before-and-after view, A/B testing turns skill development from an art into a measurable engineering discipline, directly supporting the argument for building [[Skill as Asset|durable skill assets]].

## Related
- [[Skill-Creator Tool]]
- [[Iterative Skill Development]]
- [[Skill Evaluation & Assertions]]
- [[Skill as Asset]]