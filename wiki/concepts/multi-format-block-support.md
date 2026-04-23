---
title: "Multi-Format Block Support"
type: "concept"
sources:
  - "raw/videos/b9661a04_Obsidain 补完计划像 Notion 一样丝滑拖拽文本块Dragger.md"
tags:
  - "technical"
  - "format-support"
  - "markdown"
  - "content-types"
confidence: "high"
created_at: "2026-04-21T16:31:03.468467"
updated_at: "2026-04-22T23:50:23.954106"
related:
  - "Text Block as a Unit of Manipulation"
  - "Obsidian Dragger"
  - "Obsidian Dragger Plugin: Enhancing Text Block Management"
---

**Multi-Format Block Support** describes a content manipulation system's ability to handle diverse formatted content types—paragraphs, lists, tasks, tables, code blocks, callouts—as uniformly manipulable units. This goes beyond simple paragraph dragging to encompass the full richness of modern markdown or rich text editing.

The [[Obsidian Dragger]] plugin demonstrates comprehensive multi-format support by allowing drag-and-drop rearrangement of tasks, ordered/unordered lists, tables, and more. This technical achievement requires parsing and correctly re-rendering different markdown structures after move operations while preserving formatting, nesting, and functionality.

This capability is a specific implementation of the broader [[Text Block as a Unit of Manipulation]] concept. Without multi-format support, block-based manipulation remains limited to plain text, severely reducing real-world utility since notes typically contain mixed content types. The challenge lies in abstracting the "block" concept to be format-agnostic while maintaining each format's unique behaviors—for example, ensuring task checkboxes remain functional or table structures remain intact after being moved.

## Related
- [[Text Block as a Unit of Manipulation]]
- [[Obsidian Dragger Plugin: Enhancing Text Block Management]]
- [[Obsidian Dragger]]