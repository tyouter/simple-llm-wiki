---
title: "Frontmatter"
type: "concept"
sources:
  - "raw/articles/12be559f_claude.md怎么写才能让Claude Code更高效claude.md怎么写才能让Claude Code更高效.md"
tags:
  - "YAML"
  - "配置"
  - "元数据"
  - "Markdown"
confidence: "high"
created_at: "2026-04-21T18:22:23.249742"
updated_at: "2026-04-21T18:22:23.249742"
related:
  - "Rules规则目录"
  - "CLAUDE.md"
  - "持久记忆体系"
---

一种写在 Markdown 文件顶部的、用 `---` 包裹的 YAML 配置区块，用于为文件附加元数据。在 [[Claude Code]] 的 [[Rules规则目录]] 机制中，Frontmatter 被用来声明该规则文件的生效范围。通过在 Frontmatter 中配置 `paths` 字段，可以指定通配符路径，使得该规则仅对匹配路径的文件生效。这实现了规则的精细化、条件化应用，是管理大型、多模块项目编码规范的核心工具，也是对 [[CLAUDE.md]] 单一文件作用域的强大补充。例如，可以在 `code-style.md` 顶部配置 `paths: ["src/**/*.py"]` 来确保该代码风格规则只应用于 Python 源文件。

## Related
- [[Rules规则目录]]
- [[CLAUDE.md]]
- [[持久记忆体系]]