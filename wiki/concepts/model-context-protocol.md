---
title: "Model Context Protocol"
type: "concept"
sources:
  - "wiki/sources/Claude Code Agent技术分析与多代理架构.md"
  - "wiki/sources/Agent Skills与MCP技术对比与企业应用.md"
tags:
  - "anthropic"
  - "protocol"
  - "tool-integration"
  - "agent-architecture"
confidence: "high"
created_at: "2026-04-18T01:05:59.625540"
updated_at: "2026-04-20T12:00:00"
---

# Model Context Protocol (MCP)

模型上下文协议是Anthropic推出的标准协议，用于连接外部工具和数据源到AI Agent，实现结构化的工具集成。

## 核心要点

- **Anthropic标准**：官方推出的工具连接协议
- **统一接口**：标准化工具描述和调用方式
- **数据源集成**：支持文件系统、数据库、API等多种数据源
- **工具扩展**：突破LLM内置能力限制
- **流行度对比**：相比Skills获得更广泛的社区采用

## Related
- [[MCP Server Integration]]
- [[Claude Code]]
- [[Agent Skills框架]]
- [[Claude Code Agent技术分析与多代理架构]]
- [[Agent Skills与MCP技术对比与企业应用]]