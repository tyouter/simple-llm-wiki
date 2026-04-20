---
title: "Claude Code子代理"
type: "concept"
sources:
  - "raw/articles/55258346_claude code使用感受如何claude code使用感受如何.md"
tags:
  - "claude-code"
  - "subagent"
  - "context-isolation"
  - "agent-architecture"
confidence: "high"
created_at: "2026-04-20T12:00:00"
updated_at: "2026-04-20T12:00:00"
related:
  - "Claude Code深度使用指南"
  - "DeepAgents框架"
  - "上下文隔离"
---

# Claude Code子代理

## 定义

Claude Code的子代理机制，用于隔离上下文、分配专业任务，解决复杂项目上下文窗口迅速填满的问题。

## 核心价值

**上下文隔离**：每个子代理有自己的上下文窗口，输出留在子代理里，只把摘要返回主会话。

## 三种代理模板

| 代理 | 能力配置 | 用途 |
|------|---------|------|
| explorer | 只读工具 | 快速代码库搜索 |
| planner | 只读工具 | 研究和分析 |
| executor | 全能力 | 复杂任务执行 |

## 配置示例

```yaml
---
name: code-reviewer
description: 代码审查代理，只读
tools: Read, Grep, Glob, Bash
model: sonnet
---
你是一个代码审查员。检查：安全漏洞、性能问题、可维护性。
只报告问题。不要修改代码，不要建议重构。
```

## 重要提示

子代理默认继承父会话的工具。想要真正只读的代理，必须显式设置工具白名单。只在描述里写"read-only"不会限制工具访问。

## AI人格测试法

用子代理扮演不同用户角色进行测试：
- 怀疑型资深工程师 → 关注安全、副作用
- 安全审计员 → 关注密钥泄露
- 新接手维护者 → 关注文档清晰度
- 重度CLI用户 → 关注命令一致性
- 运维/SRE → 关注可观测性
- 文档优先新手 → 关注README完整性

15分钟运行6个代理，可发现人工测试需要一周才能找到的信任断点。

## Related
- [[Claude Code深度使用指南]]
- [[DeepAgents框架]]
- [[上下文隔离]]