---
title: "Progressive Disclosure (Agent Skills)"
type: "concept"
sources:
  - "wiki/sources/Claude Code工作流技术与架构分析.md"
  - "wiki/sources/Agent Skills与MCP技术对比与企业应用.md"
tags:
  - "claude-code"
  - "agent-skills"
  - "token-optimization"
  - "context-management"
confidence: "high"
created_at: "2026-04-18T00:50:51.015027"
updated_at: "2026-04-23T00:42:20.455000"
---

# Progressive Disclosure (Agent Skills)

渐进式披露是Agent Skills的核心架构原则，仅在执行阶段按需加载必要信息到上下文中，实现Token效率优化。

## 核心要点

- **按需加载**：能力信息只在实际需要时才进入上下文
- **Token效率**：相比预加载所有信息，实现4倍的Token消耗降低
- **上下文优化**：保持主上下文清洁，避免信息过载
- **执行阶段触发**：Skill描述在触发执行时才被激活
- **架构核心**：Skills区别于MCP的关键效率机制

## Related
- [[Claude Code Skills系统]]
- [[Agent]]
- Token效率优化
- [[Agent Skills与MCP技术对比与企业应用]]
- [[Context Window Management]]
- [[Single-Loop Architecture]]
- [[Advanced Claude Code Workflow Techniques and Architecture Analysis]]
- [[Claude Code工作流技术与架构分析]]