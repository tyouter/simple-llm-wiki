---
title: "Skill Activation"
type: "concept"
sources:
  - "raw/articles/149db3c1_Skills的本质是什么Skills的本质是什么.md"
tags:
  - "Process"
  - "Execution Stage"
  - "Mechanism"
confidence: "high"
created_at: "2026-04-21T18:28:45.956933"
updated_at: "2026-04-22T23:50:12.416573"
related:
  - "Progressive Disclosure Mechanism"
  - "Skill Triggering"
  - "Agent Skills Framework"
  - "Context Window Management"
  - "Claude"
---

**Skill Activation** is the moment within the [[Progressive Disclosure Mechanism]] when an AI agent moves a [[Skills (Anthropic Framework)|Skill]] from the catalog tier (name/description) to the instruction tier, loading its full `SKILL.md` content into the working context. This is the direct result of a positive [[Skill Triggering]] decision, which can be model-driven (the agent autonomously deems the skill relevant) or user-driven (via an explicit command). Upon activation, the skill's instructions become part of the agent's directive context, guiding its actions for the relevant task. It is noted that once activated, skill content should be protected from mid-task context compression or truncation to prevent silent performance degradation. Activation is the bridge that turns a listed capability into an active guide for the agent.

## Related
- [[Progressive Disclosure Mechanism]]
- [[Skill Triggering]]
- [[Context Window Management]]
- [[Claude]]
- [[Agent Skills Framework]]