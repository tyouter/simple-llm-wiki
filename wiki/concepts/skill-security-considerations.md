---
title: "Skill Security Considerations"
type: "concept"
sources:
  - "raw/articles/149db3c1_Skills的本质是什么Skills的本质是什么.md"
tags:
  - "Security"
  - "Best Practices"
  - "Risk Management"
confidence: "high"
created_at: "2026-04-21T18:28:45.952727"
updated_at: "2026-04-22T23:50:20.851074"
related:
  - "Agent Skills Framework"
  - "Model Context Protocol (MCP)"
  - "Skill as Asset"
  - "Anthropic Skills Framework: Engineering Approach to Agent Capability Development"
---

**Skill Security Considerations** are formalized guidelines that emerge as the [[Agent Skills Framework]] ecosystem matures, addressing the risks inherent in executable agent capabilities. Key guidelines include: never hardcoding API keys, passwords, or other secrets into `SKILL.md` files or accompanying scripts; thoroughly reviewing the content of third-party skills before installation; and using secure, standardized protocols like the [[Model Context Protocol (MCP)]] for connecting to external services, rather than embedding direct access credentials. These considerations acknowledge that Skills are not just text but can orchestrate tools and access sensitive systems. Implementing these practices is crucial for safe adoption in organizational settings, ensuring that the power of reusable [[Skill as Asset|Skill assets]] does not introduce vulnerabilities.

## Related
- [[Agent Skills Framework]]
- [[Model Context Protocol (MCP)]]
- [[Anthropic Skills Framework: Engineering Approach to Agent Capability Development]]
- [[Skill as Asset]]