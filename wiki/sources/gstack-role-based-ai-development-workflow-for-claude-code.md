---
title: "GStack: Role-Based AI Development Workflow for Claude Code"
type: "source"
sources:
  - "raw/raw/articles/093f7d65_gstackClaude工程团队.md"
tags:
  - "ai-development"
  - "workflow-automation"
  - "claude-code"
  - "prompt-engineering"
  - "software-engineering"
  - "multi-agent"
  - "role-based-ai"
confidence: "high"
created_at: "2026-04-17T11:18:13.379563"
updated_at: "2026-04-17T11:18:13.379563"
related:
  - "Garry Tan"
  - "Claude Code"
  - "Role-Based AI Development"
  - "Single-Mode Problem"
  - "Convergent Evolution (in AI Tools)"
  - "Agent Operating System"
---

# GStack: Role-Based AI Development Workflow for Claude Code

## Summary
A workflow and "skill pack" created by [[Garry Tan]] that introduces eight specialized slash commands for [[Claude Code]], each representing a distinct engineering role (CEO, Engineer, QA, etc.). This system replaces the generic "single-mode" AI interaction with a structured, role-separated workflow that mirrors real-world software development processes, aiming to improve code quality and prevent AI from optimizing for flawed requirements.

## Core Workflow & Commands
GStack consists of eight opinionated slash commands, each with its own system prompt and completion criteria:

1.  **/plan-ceo-review**: Inspired by [[Brian Chesky]]'s focus on exceptional user experience, this command prompts the AI to act as a CEO, defining a "10-star experience" and high-level product vision before any code is written.
2.  **/plan-engineer**: Translates the CEO's vision into a concrete technical specification and implementation plan.
3.  **/implement**: The core coding command, where the AI acts as an Engineer to write code based on the approved plan.
4.  **/review-pr**: Simulates a code review, where the AI critiques the implementation for quality, adherence to the plan, and potential issues.
5.  **/qa-staging**: Acts as a QA engineer, testing the code in a simulated staging environment.
6.  **/qa-prod**: Performs final validation as if the code were in production.
7.  **/debug**: A specialized role for troubleshooting and fixing bugs.
8.  **/refactor**: Focuses on improving code structure and quality without changing functionality.

## Key Principles
- **[[Role-Based AI Development]]**: Enforces cognitive separation of duties by assigning the AI a specific, narrow role for each stage of development, preventing the "single-mode problem."
- **Plan-First Mandate**: Requires planning (CEO and Engineer review) before any implementation, ensuring the AI builds the *right thing* before building it *right*.
- **Parallel Execution**: The workflow is designed to be parallelizable using tools like [[Conductor]], which can run multiple [[Claude Code]] sessions simultaneously (e.g., QA, review, and implementation in isolated workspaces).
- **Convergent Evolution**: Represents a similar conceptual breakthrough to [[TurboDocx]]'s "Director/Manager/Team" model, indicating a broader trend towards structured, multi-role AI development.

## Connection to Existing Workflows
This approach **contradicts and expands upon** the simpler, linear workflow documented in [[Using DesignPrompts.dev to Generate High-Quality AI-Free Interfaces with Claude Code]]. While that method focuses on a single prompt-to-code generation for design, GStack introduces a mandatory, multi-stage review process and enables a non-linear, [[Agent Operating System]]-like model where roles can operate in parallel.

**Source:** Based on the analysis of GStack documentation and principles.

## Related
- [[Garry Tan]]
- [[Claude Code]]
- [[Role-Based AI Development]]
- [[Single-Mode Problem]]
- [[Convergent Evolution (in AI Tools)]]
- [[Agent Operating System]]
- [[Conductor]]
- [[TurboDocx]]

## Related
- [[Garry Tan]]
- [[Claude Code]]
- [[Role-Based AI Development]]
- [[Single-Mode Problem]]
- [[Convergent Evolution (in AI Tools)]]
- [[Agent Operating System]]