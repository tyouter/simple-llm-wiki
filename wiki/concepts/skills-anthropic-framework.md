---
title: "Skills (Anthropic Framework)"
type: "concept"
sources:
  - "raw\articles\149db3c1_Skills的本质是什么Skills的本质是什么.md"
tags:
  - "skill-development"
  - "anthropic-claude"
  - "standardization"
  - "reusable-assets"
  - "agent-capability"
confidence: "high"
created_at: "2026-04-17T22:06:46.780634"
updated_at: "2026-04-17T22:06:46.780634"
related:
  - "skills-vs-tools-distinction"
  - "Skill Engineering Lifecycle"
  - "skill-creator"
  - "Anthropic"
  - "Anthropic Skills: Engineering Approach to Agent Capability Development"
---

# Skills (Anthropic Framework)

## Definition
A standardized format and methodology, developed by [[Anthropic]], for packaging domain expertise, workflows, and standards into reusable capability modules that an AI agent (like Claude) can actively invoke. It is centered on a structured directory and a core `SKILL.md` file, and is developed through a systematic [[Skill Engineering Lifecycle]].

## Core Characteristics

### Structured Format
- **`SKILL.md` File:** The central file containing the Skill's instructions, workflow logic, and standards.
- **Structured Directory:** Includes supporting resources, examples, and templates.
- **[[Progressive Disclosure Mechanism]]:** Information is layered for efficient context management.

### Design Philosophy
- **Reusable Assets:** Skills are designed as permanent, versioned assets, contrasting with one-off prompts. The mantra is "Prompt 是一次性的。Skill 才是资产。"
- **Focused and Composable:** Skills are typically small and focused on a specific task, enabling complex problem-solving through [[AI Tool Chaining/Combination|combination]] by the agent.
- **Engineered, Not Written:** Created through a process involving A/B testing, quantitative assertions, and iterative refinement.

## Development Process
Skills are created using the official [[skill-creator]] tool and follow the [[Skill Engineering Lifecycle]], which includes critical steps like [[Description Trigger Optimization]].

## Relation to Broader Concepts
This framework is the primary, concrete implementation of the theoretical [[skills-vs-tools-distinction]]. It provides the "how" for encoding the "Skills" side (expertise, best practices) as executable agent capabilities.

## Use Cases and Examples
- Encoding a code review checklist and process into a "Code Review Skill."
- Packaging a content marketing workflow into a "Blog Post Drafting Skill."
- Creating a "Data Analysis Report Skill" that standardizes chart types and narrative structure.

## Source
This specific framework is detailed in the analysis [[Anthropic Skills: Engineering Approach to Agent Capability Development]], based on Anthropic's official documentation and tools.

## Tags
skill-development, anthropic-claude, standardization, reusable-assets, agent-capability

## Related
[[skills-vs-tools-distinction]], [[Skill Engineering Lifecycle]], [[skill-creator]], [[Anthropic]], [[Anthropic Skills: Engineering Approach to Agent Capability Development]]

## Related
- [[skills-vs-tools-distinction]]
- [[Skill Engineering Lifecycle]]
- [[skill-creator]]
- [[Anthropic]]
- [[Anthropic Skills: Engineering Approach to Agent Capability Development]]