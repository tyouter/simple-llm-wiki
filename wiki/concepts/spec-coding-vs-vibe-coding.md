---
title: "Spec Coding vs. Vibe Coding"
type: "concept"
sources:
  - "raw\articles\12be559f_claude.md怎么写才能让Claude Code更高效claude.md怎么写才能让Claude Code更高效.md"
tags:
  - "workflow"
  - "methodology"
  - "prompt-engineering"
  - "ai-assisted-development"
confidence: "high"
created_at: "2026-04-17T21:42:57.896032"
updated_at: "2026-04-17T21:42:57.896032"
related:
  - "Humanize Workflow"
  - "gstack-role-based-ai-development-workflow-for-claude-code"
  - "CLAUDE.md"
  - "yahah"
---

# Spec Coding vs. Vibe Coding

## Definition
A key distinction in AI-assisted development methodologies that emerged prominently in the [[Zhihu Discussion: Optimizing Claude Code with CLAUDE.md and Efficient Development Workflows]]. It describes two opposing approaches to prompting and collaborating with AI coding assistants.

## Spec Coding
**Spec Coding** is a disciplined, structured approach where development begins with the creation of a detailed, text-based specification.

### Characteristics:
- **Pre-Implementation Planning**: The user (or AI) writes a comprehensive plan detailing features, acceptance criteria, file structures, and APIs before any code is generated.
- **Clarity and Scope**: Aims to eliminate ambiguity about what is being built.
- **Referenceable Artifact**: The spec serves as a shared source of truth between the developer and the AI, against which progress can be measured.
- **Encouraged by Tools**: Modes like Claude Code's `/plan` command are built to support this workflow.

### Benefits:
- Reduces backtracking and wasted effort.
- Makes AI output more predictable and aligned with intent.
- Creates documentation alongside development.
- Is explicitly advocated for in minimalist [[CLAUDE.md]] templates (e.g., by [[yahah]]).

## Vibe Coding
**Vibe Coding** is a high-level, conceptual, and often ambiguous prompting style.

### Characteristics:
- **Aesthetic/Conceptual Prompts**: Relies on prompts like "make it sleek," "build a dashboard that feels modern," or "implement the business logic."
- **Lack of Precision**: Fails to provide concrete requirements, boundaries, or technical details.
- **Iterative Guesswork**: Forces the AI to guess the developer's intent, leading to multiple rounds of corrections and refinements.

### Drawbacks:
- Highly inefficient, leading to context-switching and frustration.
- Produces inconsistent and often unsatisfactory results.
- Fails to leverage the AI's capability to execute precise instructions.
- Is strongly discouraged in the source discussion as an anti-pattern.

## Connection to Workflows and Configuration
The debate between these methodologies underpins the contradiction in the Zhihu discussion:
- Advocates for detailed [[CLAUDE.md]] files aim to bake spec-like discipline into every interaction via rules.
- Advocates for minimalist CLAUDE.md files argue that the discipline must come from the external workflow (enforcing Spec Coding), not from a long list of internal AI instructions.

The [[Humanize Workflow]] mentioned in the discussion is an example of a structured process that enforces Spec Coding through multi-agent review cycles.

## Related Concepts
- [[Humanize Workflow]]: An example of a structured, spec-driven development process.
- [[gstack-role-based-ai-development-workflow-for-claude-code]]: Another workflow emphasizing planning and structure.
- [[CLAUDE.md]]: A file often used to enforce a spec-coding mentality on the AI.

## Related
- [[Humanize Workflow]]
- [[gstack-role-based-ai-development-workflow-for-claude-code]]
- [[CLAUDE.md]]
- [[yahah]]