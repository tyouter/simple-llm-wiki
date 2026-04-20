---
title: "Humanize Workflow"
type: "concept"
sources:
  - "raw/articles/12be559f_claude.md怎么写才能让Claude Code更高效claude.md怎么写才能让Claude Code更高效.md"
tags:
  - "workflow"
  - "multi-agent"
  - "code-review"
  - "ai-assisted-development"
confidence: "high"
created_at: "2026-04-17T21:42:57.896560"
updated_at: "2026-04-17T21:42:57.896560"
related:
  - "Spec Coding vs. Vibe Coding"
  - "AI Tool Chaining/Combination"
  - "yahah"
---

# Humanize Workflow

## Definition
An iterative, multi-agent AI-assisted development methodology mentioned in the [[Zhihu Discussion: Optimizing Claude Code with CLAUDE.md and Efficient Development Workflows]]. It structures development into a feedback loop where one AI agent (e.g., Claude) executes a plan, and a separate, independent agent (e.g., Codex) reviews the output against acceptance criteria, catching issues early.

## Process Overview
1.  **Specification & Planning**: A detailed specification and implementation plan are created, following the principles of [[Spec Coding vs. Vibe Coding|Spec Coding]].
2.  **Agent Execution**: The primary coding agent (Agent A, e.g., Claude Code) executes the plan, writing and modifying code.
3.  **Independent Review**: Upon completion of a milestone, a different AI agent (Agent B, e.g., a Codex-based reviewer) analyzes the output. This agent has not seen the development process and reviews the code "fresh" against the original spec.
4.  **Feedback Loop**: Reviewer Agent B provides feedback, critiques, or identifies gaps. This feedback is fed back to Agent A for correction.
5.  **Iteration**: Steps 2-4 repeat until the reviewer agent confirms all acceptance criteria from the spec are met.

## Philosophical Rationale
- **Mitigates AI Blind Spots**: An AI agent may become entrenched in its own reasoning path. A separate agent provides an independent perspective, simulating a human code review.
- **Enforces Specification Adherence**: The review is explicitly against the spec, reinforcing disciplined, spec-driven development.
- **Automates Quality Gates**: Creates an automated, AI-powered check within the development cycle.

## Relation to Other Concepts
- **[[Spec Coding vs. Vibe Coding]]**: The Humanize Workflow is a concrete system designed to enforce Spec Coding. The spec is the central artifact linking the execution and review agents.
- **[[AI Tool Chaining/Combination]]**: This workflow is a prime example of chaining different AI models (Claude + Codex) with specialized roles to achieve a more robust outcome than a single model could.
- **Contrast with [[gstack-role-based-ai-development-workflow-for-claude-code]]**: While GStack uses role-based prompts within a single Claude instance, Humanize uses distinct AI models/instances for execution and review, potentially offering greater independence in the review phase.

## Practical Considerations
- Requires setup of multiple AI tools or APIs.
- The reviewer agent must be effectively prompted to understand the spec and provide actionable feedback.
- Can increase the token cost and time per development cycle but aims to reduce overall error rates and rework.

## Related Concepts
- [[Spec Coding vs. Vibe Coding]]: The foundational methodology it enforces.
- [[AI Tool Chaining/Combination]]: The category of technique it exemplifies.
- [[yahah]]: The Zhihu user who advocated for this workflow in the source discussion.

## Related
- [[Spec Coding vs. Vibe Coding]]
- [[AI Tool Chaining/Combination]]
- [[yahah]]