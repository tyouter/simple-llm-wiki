---
title: "EditorConfig"
type: "entity"
sources:
  - "raw/articles/2b36f099_claude.md怎么写才能让Claude Code更高效claude.md怎么写才能让Claude Code更高效.md"
tags:
  - "工具"
  - "配置"
  - "代码格式化"
confidence: "high"
created_at: "2026-04-21T14:48:09.254238"
updated_at: "2026-04-21T14:48:09.254238"
related:
  - "工具链与插件生态"
  - "概率性提示词局限"
  - "Claude Code"
  - "CLAUDE.md配置哲学"
  - "注意力稀释效应"
  - "代码即规范"
---

用于统一代码格式的配置文件工具。在AI编程中被推荐用于解决代码格式化问题，作为确定性工具替代概率性提示词。

EditorConfig是[[工具链与插件生态]]中的基础工具之一，直接体现了“能用确定性工具解决的，就别依赖概率性提示词”的原则。它通过配置文件强制统一代码格式，避免了依赖[[Claude Code]]自觉遵守格式化规则的不确定性。

在[[CLAUDE.md配置哲学]]的框架下，EditorConfig承担了代码格式化的责任，使得CLAUDE.md可以专注于更高层次的架构和设计规则，而不是低级的格式化细节。这有助于减轻[[注意力稀释效应]]——CLAUDE.md中的规则越少，每条规则获得的注意力就越多。

EditorConfig与Git Hooks等工具结合使用，可以在提交前自动格式化代码，确保代码库始终保持一致的风格。这支持了[[代码即规范]]的理念——如果代码库本身格式统一，AI就更可能生成风格一致的代码。

## Related
- [[工具链与插件生态]]
- [[概率性提示词局限]]
- [[Claude Code]]
- [[CLAUDE.md配置哲学]]
- [[注意力稀释效应]]
- [[代码即规范]]