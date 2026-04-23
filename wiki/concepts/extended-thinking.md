---
title: "Extended Thinking"
type: "concept"
sources:
  - "wiki/sources/claude-code-agent-technical-analysis-and-multi-agent-architecture.md"
  - "wiki/sources/anthropic-s-china-restrictions-and-claude-reasoning-distillation-techniques.md"
  - "raw/articles/0bbdb067_为什么Claude的代码能力会这么强为什么Claude的代码能力会这么强.md"
  - "raw/articles/53771cca_Anthropic的Claude Code Agent效果很好有没有人深入分析其技术原理Anthropic的Claude Code Agent效果很好有.md"
  - "raw/articles/55258346_claude code使用感受如何claude code使用感受如何.md"
  - "raw/videos/c1b57a29_Every Claude Code Concept Explained for Normal People.md"
tags:
  - "reasoning"
  - "claude"
  - "agent-architecture"
  - "cot"
confidence: "high"
created_at: "2026-04-18T01:05:59.625540"
updated_at: "2026-04-23T00:53:47.216702"
---

# Extended Thinking (扩展思考)

## 概述
Extended Thinking是Claude Code Agent的核心特性，允许模型进行内部深度推理而非直接响应，是Agentic Loop架构的关键组成部分。

## 核心要点
- **Agentic Loop位置**：在用户输入后、工具选择前进行内部推理
- **深度推理**：允许Agent进行多步骤思考，而非快速给出答案
- **与CoT关联**：Extended Thinking产生的推理过程可作为CoT输出用于知识蒸馏
- **可蒸馏特性**：Claude Opus 4.6的Extended Thinking能力被蒸馏到开源模型
- **生产应用**：OpenAI的3工程师、5个月、100万行代码实验验证了深度推理的价值
- **计算资源分配**：Effort Budgeting机制指导Agent在不同复杂度任务上分配思考资源

## 相关概念
- [[Agentic Loop]]
- [[Chain-of-Thought (CoT) Reasoning)]]
- [[Knowledge Distillation (Model Distillation)]]
- [[AI Agent]]
- [[Claude Code]]
- Effort Budgeting

## 相关实体
- [[Claude Opus 4.6]]
- [[Anthropic]]
- [[Flood Sung]]

## 来源
- [src: Claude Code Agent Technical Analysis and Multi-Agent Architecture]
- [src: Anthropic's China Restrictions and Claude Reasoning Distillation Techniques]
## Related
- [[Agent]]
- [[Api]]
- [[Auto Memory]]
- [[CLAUDE.md]]
- [[Cli]]
- [[Code Review]]
- [[Context Window]]
- [[Copilot]]
- [[Cursor]]
- [[Deepseek]]
- [[Distributed Context Management]]
- [[Figma]]
- [[Frontmatter]]
- [[Gemini]]
- [[Git Worktrees]]
- [[Git]]
- [[Hooks]]
- [[Luhui Dev]]
- [[Markdown]]
- [[Mcp]]
- [[Mental Model]]
- [[Model Context Protocol]]

