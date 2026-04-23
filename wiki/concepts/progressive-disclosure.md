---
title: "Progressive Disclosure"
type: "concept"
sources:
  - "raw/articles/697c42e9_Agent Skill 为何没有像 MCP 那样火爆Agent Skill 为何没有像 MCP 那样火爆.md"
  - "raw/articles/0bbdb067_为什么Claude的代码能力会这么强为什么Claude的代码能力会这么强.md"
  - "raw/articles/149db3c1_Skills的本质是什么Skills的本质是什么.md"
  - "raw/articles/55fe935f_Claude CodeCursorTRAE究竟谁最强Claude CodeCursorTRAE究竟谁最强.md"
  - "raw/articles/b99fad36_Harness Engineering的本质是什么Harness Engineering的本质是什么.md"
  - "raw/articles/ef5489cd_Skills的本质是什么Skills的本质是什么.md"
  - "raw/videos/1a8159fd_Stop Writing Bad CLAUDE.md Files.md"
  - "raw/videos/42a13a06_Obsidian CLI80命令让笔记库听命于终端.md"
tags:
  - "architecture-principle"
  - "token-optimization"
  - "context-management"
  - "agent-design"
confidence: "high"
created_at: "2026-04-18T01:17:46.828011"
updated_at: "2026-04-23T00:42:26.468882"
related:
  - "Agent Skills Framework"
  - "Token Efficiency Optimization"
  - "Playwright CLI"
  - "skill-creator"
  - "Model Context Protocol"
  - "Extended Thinking"
  - "Git Worktrees"
  - "Claude Code"
  - "Code Review"
  - "Claude.Md"
  - "Github Copilot"
  - "Anthropic"
  - "Deepseek"
  - "为什么Claude的代码能力会这么强？"
  - "Prompt Engineering"
  - "Skill-Creator"
  - "Frontmatter"
  - "Playwright"
  - "Ai Agent"
  - "Skills的本质是什么？"
  - "Plan Mode"
  - "Markdown"
  - "Notebooklm"
  - "Claude Code、Cursor、TRAE，究竟谁最强？"
  - "Agent Skill 为何没有像 MCP 那样火爆？"
  - "Harness Engineering"
  - "Context Engineering"
  - "Vibe Coding"
  - "Spec Coding"
  - "Mitchell Hashimoto"
  - "Swe-Agent"
  - "Harness Engineering的本质是什么？"
  - "Agent"
  - "Hooks"
  - "Git"
  - "Claude"
  - "Github"
  - "Mit"
  - "Stop Writing Bad CLAUDE.md Files"
  - "Obsidian"
  - "Mcp"
  - "Cli"
  - "Youtube"
  - "Obsidian CLI：80+命令让笔记库听命于终端"
  - "A/B Test"
  - "AI Tool Chaining/Combination"
  - "Anthropic Skills: Engineering Approach to Agent Capability Development|Anthropic Skills Framework"
  - "Api"
  - "CLAUDE.md"
  - "Copilot"
  - "Cybernetics"
  - "Docker"
  - "Enterprise Skill Engineering"
  - "Figma"
  - "Gemini"
  - "Humanize"
  - "Opencode"
  - "Rag"
  - "Subagent"
  - "Worktree"
  - "Yaml"
  - "Ai学习的老章"
  - "Chatgpt"
  - "Cloudflare"
  - "DeepSeek"
  - "GitHub"
  - "mCell"
  - "Meta"
  - "Notion"
  - "OpenCode"
  - "Stripe"
  - "SWE-agent"
  - "Vercel"
  - "Agent Skills vs MCP: Technical Comparison and Enterprise Applications"
  - "Skill"
  - "Skills"
---

# Progressive Disclosure

## Definition
Core architectural principle of the [[Agent Skills Framework]] where only necessary information is loaded into context at each execution stage to minimize token usage. This approach represents a sophisticated method for managing AI agent context and optimizing resource utilization.

## Technical Implementation

### Stage-Based Information Loading
- **Initial Stage:** Loads high-level descriptions and triggers
- **Execution Stage:** Loads specific instructions and parameters
- **Result Stage:** Loads validation and output formatting rules
- Each stage loads only what's needed for that specific phase

### Token Optimization Mechanism
- Reduces context window bloat by avoiding premature information loading
- Enables handling of complex workflows within token limits
- Particularly effective for multi-step processes

## Advantages

### Token Efficiency
- Demonstrates 4x reduction in token consumption compared to full-context approaches
- Enables more complex workflows within same token budget
- Reduces API costs and improves response times

### Cognitive Optimization
- Prevents information overload for the AI agent
- Focuses attention on relevant task components
- Improves accuracy by reducing distraction

### Scalability
- Supports arbitrarily complex workflows through staged execution
- Maintains performance consistency as complexity increases
- Enables modular design of agent capabilities

## Practical Applications

### Browser Automation Example
- [[Playwright CLI]] implementation shows practical benefits
- Initial stage: Load browser control basics
- Navigation stage: Load specific page interaction rules
- Data extraction stage: Load parsing and formatting instructions

### Enterprise Workflows
- Business process automation with staged rule loading
- Compliance checking with progressive rule application
- Multi-department coordination with phased information sharing

## Comparison with Alternatives

### vs. Full Context Loading
- Traditional approach loads all information upfront
- Progressive disclosure loads as needed
- Results in significant token savings for complex tasks

### vs. MCP Implementation
- [[Model Context Protocol|MCP]] focuses on resource access
- Progressive disclosure focuses on information management
- Complementary approaches can be combined

## Implementation Considerations

### Skill Design Requirements
- Requires careful planning of information staging
- Needs clear definition of execution phases
- Must maintain coherence across stages

### Tool Integration
- Supported by [[skill-creator]] for development
- Implemented in tools like [[Cursor]] and [[Playwright CLI]]
- Requires framework awareness in execution environment

## Related Concepts
- [[Token Efficiency Optimization]]: Primary benefit of this approach
- [[Agent Skills Framework]]: Main implementation context
- [[Skill Engineering Lifecycle]]: Development process incorporating this principle

## Tags
architecture-principle, token-optimization, context-management, agent-design

## Related
- [[Model Context Protocol]]
- [[Extended Thinking]]
- [[Git Worktrees]]
- [[Claude Code]]
- [[Code Review]]
- [[CLAUDE.md]]
- [[Github Copilot]]
- [[Anthropic]]
- [[Deepseek]]
- [[为什么Claude的代码能力会这么强？]]
- [[Prompt Engineering]]
- [[Skill-Creator]]
- [[Frontmatter]]
- [[Playwright]]
- [[AI Agent]]
- [[Skills的本质是什么？]]
- [[Plan Mode]]
- [[Markdown]]
- [[Notebooklm]]
- [[Claude Code、Cursor、TRAE，究竟谁最强？]]
- [[Agent Skill 为何没有像 MCP 那样火爆？]]
- [[Harness Engineering]]
- [[Context Engineering]]
- [[Vibe Coding]]
- [[Spec Coding]]
- [[Mitchell Hashimoto]]
- [[Swe-Agent]]
- [[Harness Engineering的本质是什么？]]
- [[Agent]]
- [[Hooks]]
- [[Git]]
- [[Claude]]
- [[GitHub]]
- [[Mit]]
- [[Stop Writing Bad CLAUDE.md Files]]
- [[Obsidian]]
- [[Mcp]]
- [[Cli]]
- [[Youtube]]
- [[Obsidian CLI：80+命令让笔记库听命于终端]]
- [[A/B Test]]
- [[AI Tool Chaining/Combination]]
- [[Anthropic Skills: Engineering Approach to Agent Capability Development|Anthropic Skills Framework]]
- [[Api]]
- [[CLAUDE.md]]
- [[Copilot]]
- [[Cybernetics]]
- [[Docker]]
- [[Enterprise Skill Engineering]]
- [[Figma]]
- [[Gemini]]
- [[Humanize]]
- [[Opencode]]
- [[Rag]]
- [[Subagent]]
- [[Worktree]]
- [[Yaml]]
- [[Ai学习的老章]]
- [[Chatgpt]]
- [[Cloudflare]]
- [[DeepSeek]]
- [[GitHub]]
- [[mCell]]
- [[Meta]]
- [[Notion]]
- [[OpenCode]]
- [[Stripe]]
- [[SWE-agent]]
- [[Vercel]]
- [[Agent Skills vs MCP: Technical Comparison and Enterprise Applications]]
- [[Skill]]
- [[Skills]]
[[Agent Skills Framework]], [[Token Efficiency Optimization]], [[Playwright CLI]], [[skill-creator]]

## Related
- [[Agent Skills Framework]]
- [[Token Efficiency Optimization]]
- [[Playwright CLI]]
- [[skill-creator]]