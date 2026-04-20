---
title: "Context Window Management"
type: "concept"
sources:
  - "raw\articles\0bbdb067_为什么Claude的代码能力会这么强为什么Claude的代码能力会这么强.md"
tags:
  - "claude-code"
  - "context-management"
  - "tokens"
  - "memory"
  - "optimization"
confidence: "high"
created_at: "2026-04-18T00:50:50.979040"
updated_at: "2026-04-18T00:50:50.979040"
related:
  - "Claude Code"
  - "Persistent Memory System (Claude Code)"
  - "Subagents for Context Efficiency"
  - "Single-Loop Architecture"
---

# Context Window Management

## Definition
Techniques for treating the AI context window as a scarce resource in [[Claude Code]], including monitoring token usage, avoiding auto-compaction, and strategically clearing context between work phases.

## Core Principles
- **Context as Limited Resource**: The context window has finite capacity that must be managed
- **Intentional Clearing**: Manual context management preferred over automatic compression
- **Phase-Based Work**: Clear context between distinct work phases (research, planning, implementation)

## Key Techniques

### 1. Token Usage Monitoring
- Regularly check context token count
- Be aware of what consumes context (conversation history, file contents, instructions)
- Prioritize essential information in context

### 2. Avoiding Auto-Compaction
- **Problem**: Automatic context compression can lose important details
- **Solution**: Manual context clearing between major task transitions
- **Benefit**: Maintains control over what information persists

### 3. Strategic Context Clearing
- Clear context when switching between unrelated tasks
- Preserve only essential project context (via [[CLAUDE.md]] and key files)
- Use [[Subagents for Context Efficiency]] for parallel research tasks

### 4. Modular Context Design
- Keep [[CLAUDE.md]] concise and modular
- Use `.claude/rules/` directory for organized, loadable rules
- Implement [[Progressive Disclosure (Agent Skills)]] for on-demand capability loading

## Connection to Architecture
Context management aligns with [[Claude Code]]'s [[Single-Loop Architecture]] philosophy:
- **Simplicity**: Clear, manageable context over complex retention systems
- **Debuggability**: Understandable context state for troubleshooting
- **Human Control**: Developer maintains oversight of context decisions

## Best Practices
1. **Monitor Regularly**: Check token usage at phase transitions
2. **Clear Intentionally**: Don't rely on automatic systems
3. **Design for Modularity**: Create context that can be loaded incrementally
4. **Use Subagents**: Offload research to preserve main context

## Related Concepts
- [[Persistent Memory System (Claude Code)]]: Broader system for maintaining project context
- [[Subagents for Context Efficiency]]: Technique for preserving main context
- [[Single-Loop Architecture]]: Design philosophy influencing context management approach

## Source
Based on techniques from [[Advanced Claude Code Workflow Techniques and Architecture Analysis]].

## Related
- [[Claude Code]]
- [[Persistent Memory System (Claude Code)]]
- [[Subagents for Context Efficiency]]
- [[Single-Loop Architecture]]