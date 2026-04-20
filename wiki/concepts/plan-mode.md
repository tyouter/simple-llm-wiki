---
title: "Plan Mode"
type: "concept"
sources:
  - "raw/articles/0bbdb067_为什么Claude的代码能力会这么强为什么Claude的代码能力会这么强.md"
tags:
  - "claude-code"
  - "workflow"
  - "planning"
  - "read-only"
  - "productivity"
confidence: "high"
created_at: "2026-04-18T00:50:50.978533"
updated_at: "2026-04-18T00:50:50.978533"
related:
  - "Claude Code"
  - "Context Window Management"
  - "TDD with Claude Code"
  - "Single-Loop Architecture"
  - "雁南飞"
---

# Plan Mode

## Definition
A [[Claude Code]] feature (activated with Shift+Tab) designed for read-only codebase exploration before implementation. It enforces a structured 'research → plan → implement → verify' workflow by preventing immediate code changes during the planning phase.

## Purpose and Function
- **Structured Workflow Enforcement**: Forces developers to understand the codebase before making changes
- **Context Preservation**: Allows exploration without consuming context with implementation details
- **Reduced Errors**: Minimizes premature implementation that might require rework
- **Better Planning**: Encourages comprehensive understanding of dependencies and architecture

## How It Works
1. **Activation**: Press Shift+Tab in Claude Code interface
2. **Read-Only Exploration**: Browse and analyze code without editing capabilities
3. **Planning Phase**: Create implementation plan based on understanding
4. **Transition to Implementation**: Switch to normal mode for actual coding

## Best Practices
1. **Use for Complex Changes**: Especially valuable for architectural refactoring or large feature additions
2. **Document Findings**: Take notes on dependencies, patterns, and potential issues
3. **Create Step-by-Step Plans**: Break implementation into verifiable steps
4. **Validate Assumptions**: Use Plan Mode to test understanding before committing to implementation

## Connection to Workflow Discipline
Plan Mode is a key component of the professional workflow discipline advocated by [[雁南飞]], supporting the broader philosophy of [[Spec Coding vs. Vibe Coding|Spec Coding]] over ad-hoc development.

## Related Concepts
- [[Context Window Management]]: Plan Mode helps preserve context for implementation phase
- [[TDD with Claude Code]]: Both emphasize structured, verifiable approaches
- [[Single-Loop Architecture]]: Part of Claude Code's focused tool design philosophy

## Source
Based on workflow techniques documented in [[Advanced Claude Code Workflow Techniques and Architecture Analysis]] by [[雁南飞]].

## Related
- [[Claude Code]]
- [[Context Window Management]]
- [[TDD with Claude Code]]
- [[Single-Loop Architecture]]
- [[雁南飞]]