---
title: "Progressive Disclosure Mechanism"
type: "concept"
sources:
  - "raw/articles/149db3c1_Skills的本质是什么Skills的本质是什么.md"
tags:
  - "design-pattern"
  - "context-management"
  - "skill-architecture"
  - "anthropic-claude"
confidence: "high"
created_at: "2026-04-17T22:06:46.779630"
updated_at: "2026-04-17T22:06:46.779630"
related:
  - "Anthropic Skills: Engineering Approach to Agent Capability Development"
  - "Skill Engineering Lifecycle"
  - "skill-creator"
  - "Agent Skills Framework"
  - "Context Window Management"
  - "Skill Activation"
  - "Skill Triggering"
---

# Progressive Disclosure Mechanism

## Definition
A core design philosophy within the [[Anthropic Skills: Engineering Approach to Agent Capability Development|Anthropic Skills Framework]] for efficiently managing an AI agent's context window. Information within a Skill is structured and loaded in sequential layers, only revealing full details when the Skill is specifically triggered by the agent.

## How It Works
The mechanism typically follows a layered structure:
1.  **Catalog/Index Layer:** A high-level list of available Skills with brief descriptions. This helps the agent (like Claude) discover which Skills might be relevant to a user's request.
2.  **Instruction Layer:** If the agent decides a Skill is relevant based on the catalog, it loads the Skill's core instructions and workflow logic from a file (typically `SKILL.md`).
3.  **Resource Layer:** Finally, the Skill may load additional, detailed resources (templates, data files, examples) only if and when they are needed during execution.

## Purpose and Benefits
- **Context Efficiency:** Prevents the agent's limited context window from being filled with the full details of all available Skills upfront.
- **Focused Activation:** Ensures the agent only spends "mental resources" on Skills it has decided to use.
- **Scalability:** Allows for larger libraries of Skills without degrading overall system performance.

## Implementation in Anthropic Skills
This mechanism is a foundational part of the standardized Skill format, which centers on a structured directory and a main `SKILL.md` file. The `skill-creator` tool from [[Anthropic]] helps implement this structure.

## Relation to Other Concepts
- **[[Skill Engineering Lifecycle]]:** Progressive disclosure is a key architectural decision made during the Skill design phase.
- **[[skills-vs-tools-distinction]]:** This mechanism is a practical implementation detail that supports the "Skill" side of the distinction, enabling efficient knowledge management.

## Tags
design-pattern, context-management, skill-architecture, anthropic-claude

## Related
[[Anthropic Skills: Engineering Approach to Agent Capability Development]], [[Skill Engineering Lifecycle]], [[skill-creator]]

## Related
- [[Anthropic Skills: Engineering Approach to Agent Capability Development]]
- [[Skill Engineering Lifecycle]]
- [[skill-creator]]

---

## Extended Definition

The **Progressive Disclosure Mechanism** is a layered context management strategy fundamental to the [[Agent Skills Framework]]. It addresses the constraint of [[Context Window Management]] by loading Skill information incrementally based on the agent's immediate need, rather than all at once. The mechanism typically operates across three tiers: 1) the **Catalog** (containing only skill names and descriptions) loaded at session start for discovery; 2) **Full Instructions** (the `SKILL.md` body) loaded during [[Skill Activation]] when a skill is triggered; and 3) **Resources** (scripts, detailed references) loaded on-demand during execution. This design conserves the agent's limited token budget, allowing it to be aware of dozens of skills without being overwhelmed. Only the skills relevant to the current task, as determined by [[Skill Triggering]], incur their full cognitive load, making the framework scalable and efficient.

## Related
- [[Anthropic Skills: Engineering Approach to Agent Capability Development]]
- [[Skill Engineering Lifecycle]]
- [[skill-creator]]
- [[Agent Skills Framework]]
- [[Context Window Management]]
- [[Skill Activation]]
- [[Skill Triggering]]

---

## Additional Insights



## Enhanced Insights from Analysis
This mechanism is the architectural linchpin that makes the [[Agent Skills Framework]] scalable. It directly solves the problem of [[Context Window Management]] by ensuring the agent's limited token budget is not wasted on loading irrelevant skill details. The transition from the catalog stage to the [[Skill Activation|activation stage]] is where the mechanism's efficiency is realized, allowing the agent to maintain a broad awareness of capabilities while focusing cognitive resources only on what is immediately necessary.

Source: [[raw/articles/149db3c1_Skills的本质是什么Skills的本质是什么.md]]

## Related
- [[Anthropic Skills: Engineering Approach to Agent Capability Development]]
- [[Skill Engineering Lifecycle]]
- [[skill-creator]]
- [[Agent Skills Framework]]
- [[Context Window Management]]
- [[Skill Activation]]
- [[Skill Triggering]]