---
title: "Context Pollution"
type: "concept"
sources:
  - "raw/articles/27bcfccd_Claude Code 深度用法指南那些让效率翻倍的隐藏技巧.md"
tags:
  - "ai-context"
  - "workflow-management"
  - "context-pollution"
  - "ai-limitations"
  - "claude-code"
confidence: "high"
created_at: "2026-04-17T21:50:12.391958"
updated_at: "2026-04-17T21:50:12.391958"
related:
  - "Claude Code"
  - "Thariq"
  - "Parallel Agent Review"
  - "Workflow Branching"
  - "gstack-role-based-ai-development-workflow-for-claude-code"
---

# Context Pollution

## Definition
Context Pollution refers to a problem in AI agent interactions where inserting unrelated questions or tasks into an agent's main workflow can corrupt its execution context, leading to derailed or confused responses. This occurs because AI models maintain a continuous context window, and irrelevant information can dilute or distort the agent's understanding of the primary task.

## Problem Description
When working with AI development tools like [[Claude Code]], users often need to ask secondary questions (e.g., "What does this library function do?") while engaged in a primary coding task. Without proper isolation mechanisms, these side inquiries can:
1. **Dilute focus**: The agent may start incorporating unrelated concepts into its main reasoning
2. **Corrupt memory**: Previous context becomes contaminated with irrelevant information
3. **Reduce efficiency**: The agent spends tokens processing off-topic content
4. **Cause hallucinations**: Mixed contexts can lead to incorrect assumptions or outputs

## Solution in Claude Code
[[Claude Code]] addresses this problem through the `/btw` command, which allows users to ask "by the way" questions without affecting the main workflow context. This command was specifically designed to solve context pollution and was announced by [[Thariq]], Claude Code's product lead.

## Technical Implications
Context pollution is particularly problematic for:
- **Long-running sessions**: Where context accumulates over many interactions
- **Complex workflows**: Like those described in [[gstack-role-based-ai-development-workflow-for-claude-code]]
- **Multi-step tasks**: Where maintaining clean context is essential for consistency

## Related Concepts
- [[Parallel Agent Review]]: Another technique for maintaining clean context by using specialized agents
- [[Workflow Branching]]: Creating separate contexts for alternative approaches
- [[AI Tool Chaining/Combination]]: Managing context across different tools

## Best Practices
1. Use isolation commands (like `/btw`) for secondary questions
2. Regularly check context clarity during long sessions
3. Use `/rewind` to return to clean context states when pollution occurs
4. Document context boundaries in complex workflows

## Source
Concept identified and named in the "Claude Code Hidden Features Guide" based on practical experience with AI development tools.

## Related
- [[Claude Code]]
- [[Thariq]]
- [[Parallel Agent Review]]
- [[Workflow Branching]]
- [[gstack-role-based-ai-development-workflow-for-claude-code]]