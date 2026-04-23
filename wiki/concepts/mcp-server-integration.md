---
title: "MCP Server Integration"
type: "concept"
sources:
  - "wiki/sources/Claude Code工作流技术与架构分析.md"
  - "wiki/sources/advanced-claude-code-workflow-techniques-and-architecture-analysis.md"
  - "wiki/sources/Agent Skills与MCP技术对比与企业应用.md"
tags:
  - "claude-code"
  - "mcp"
  - "integration"
  - "external-systems"
confidence: "high"
created_at: "2026-04-18T00:50:51.014028"
updated_at: "2026-04-23T00:42:20.356630"
---

# MCP Server Integration

MCP服务器集成是Claude Code连接外部系统（如GitHub、Sentry、数据库）的核心能力，通过Model Context Protocol实现标准化工具连接。

## 核心要点

- **外部系统连接**：支持GitHub、Sentry、数据库等系统的标准化接入
- **协议标准化**：MCP提供统一的工具描述和调用接口
- **工具扩展能力**：突破内置工具限制，扩展Agent能力边界
- **企业应用**：支持业务系统的无缝集成
- **与Skills对比**：MCP提供工具连接，Skills定义业务流程

## Related
- [[Model Context Protocol]]
- [[Claude Code]]
- [[Agent]]
- [[Agent Skills与MCP技术对比与企业应用]]
- [[雁南飞]]
- [[Advanced Claude Code Workflow Techniques and Architecture Analysis]]
- [[Claude Code工作流技术与架构分析]]