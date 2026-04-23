---
title: "Claude Code Hidden Features Guide: Efficiency-Boosting Commands and Techniques"
type: "source"
sources:
  - "raw/articles/27bcfccd_Claude Code 深度用法指南那些让效率翻倍的隐藏技巧.md"
tags:
  - "claude-code"
  - "ai-development-tools"
  - "workflow-optimization"
  - "hidden-features"
  - "command-guide"
  - "multi-agent"
  - "efficiency"
  - "source"
confidence: "high"
created_at: "2026-04-17T21:50:12.391445"
updated_at: "2026-04-23T00:42:21.306732"
related:
  - "Claude Code"
  - "Thariq"
  - "Boris"
  - "Context Pollution"
  - "Parallel Agent Review"
  - "Model-Switching Optimization"
  - "Workflow Branching"
  - "gstack-role-based-ai-development-workflow-for-claude-code"
  - "AI Tool Chaining/Combination"
  - "Zhihu Discussion: AI Agent Engineering Career Paths and Technical Approaches"
---

# Claude Code Hidden Features Guide: Efficiency-Boosting Commands and Techniques

## Summary
A practical guide detailing lesser-known but highly effective commands and shortcuts for the [[Claude Code]] AI development tool. The guide focuses on features that improve workflow efficiency, such as parallel task management, context preservation, and model optimization. Many of these features are not well-documented in official sources and have been discovered and shared through developer social media channels.

## Key Commands and Techniques

### /btw Command
**Purpose**: Solves the problem of [[Context Pollution]] by allowing users to ask unrelated questions without corrupting the main workflow context.
**Source**: Announced by [[Thariq]] (Claude Code's product lead) on social media.
**Usage**: When working on a main task, use `/btw` followed by a separate question to handle side inquiries without derailing the primary execution.

### /simplify Command
**Purpose**: Implements [[Parallel Agent Review]] by having multiple AI agents simultaneously review code from different perspectives (reusability, quality, efficiency).
**Source**: Used daily by [[Boris]], a core team member of Claude Code.
**Usage**: After generating or modifying code, use `/simplify` to get comprehensive feedback from specialized review agents.

### /model opusplan Command
**Purpose**: Enables [[Model-Switching Optimization]] by using Claude Opus for planning and Claude Sonnet for execution.
**Usage**: Start with `/model opusplan` to have Opus create a detailed plan, then Sonnet executes it efficiently, conserving premium model tokens.

### /branch Command
**Purpose**: Facilitates [[Workflow Branching]] by creating parallel development paths from a shared starting point.
**Usage**: When exploring different implementation approaches, use `/branch` to test alternatives without losing the original context.

### /rewind Command
**Purpose**: Allows backtracking to previous states in the conversation when context becomes corrupted or the agent goes off-track.
**Usage**: Use `/rewind` followed by a step number or description to return to a cleaner context state.

### /export Command
**Purpose**: Enables cross-tool validation and integration by exporting context to other development tools.
**Usage**: Use `/export` to feed Claude Code context into tools like Codex or other AI assistants for validation or continued work.

## Relation to Existing Concepts

### Connection to [[Claude]]
This guide provides concrete, low-level commands that can be used within or to enhance the higher-level, role-based workflow described in GStack. The `/btw`, `/rewind`, and `/simplify` commands are particularly useful for maintaining clean context in complex role-based workflows.

### Connection to [[AI Tool Chaining/Combination]]
The guide implicitly promotes tool chaining within Claude Code itself and explicitly mentions using `/export` to feed context into other tools. This represents a practical implementation of the tool chaining concept within a single AI development environment.

### Connection to [[Zhihu Discussion: AI Agent Engineering Career Paths and Technical Approaches]]
Both documents discuss practical, technical approaches to using AI agents effectively. While the Zhihu article focuses on foundational architecture (DSLs, TIR), this source serves as a user manual for specific efficiency features in one tool, providing complementary implementation details.

## Practical Applications

### Development Workflow Optimization
- Use `/btw` for documentation lookups during coding sessions
- Apply `/simplify` after each major code iteration for quality assurance
- Implement `/model opusplan` for complex architectural decisions

### Team Collaboration
- Share `/branch` workflows for code review and alternative approach testing
- Use `/export` to transfer context between team members using different tools
- Document `/rewind` points for complex debugging sessions

## Source Attribution
This guide synthesizes information from developer social media posts, particularly from Claude Code team members [[Thariq]] and [[Boris]], as well as community discoveries shared in development forums and chat groups.

**Note**: Features described may evolve as Claude Code updates, and some commands may be experimental or require specific access levels.

## Related
- [[Claude Code]]
- [[Thariq]]
- [[Boris]]
- [[Context Pollution]]
- [[Parallel Agent Review]]
- [[Model-Switching Optimization]]
- [[Workflow Branching]]
- [[Claude]]
- [[AI Tool Chaining/Combination]]
- [[Zhihu Discussion: AI Agent Engineering Career Paths and Technical Approaches]]