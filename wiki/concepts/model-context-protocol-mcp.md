---
title: "Model Context Protocol (MCP)"
type: "concept"
sources:
  - "raw/articles/517a9161_GLM5Kimi 2.5Minimax M2.5千问豆包国产大模型选哪个GLM5Kimi 2.5Minimax M2.5千问豆包国产大模.md"
  - "wiki/sources/agent-skills-vs-mcp-technical-comparison-and-enterprise-applications.md"
  - "raw/articles/149db3c1_Skills的本质是什么Skills的本质是什么.md"
tags:
  - "protocols"
  - "integration"
  - "developer-tools"
  - "ai-assistants"
  - "local-computing"
confidence: "high"
created_at: "2026-04-20T12:00:00"
updated_at: "2026-04-20T12:00:00"
related:
  - "Coding Plan"
  - "AI Tool Chaining/Combination"
  - "CLAUDE.md"
  - "Alibaba Cloud Bailian"
  - "Skill Security Considerations"
  - "Agent Skills Framework"
---

# Model Context Protocol (MCP)

## 概述

MCP是一种协议标准，让AI编码助手能够安全地访问和交互本地开发工具、文件系统和资源，实现AI模型与本地环境的深度集成。

## 核心要点

- **本地工具集成**：允许AI与本地开发工具、版本控制、构建系统交互
- **文件系统访问**：提供安全、可控的本地文件和项目结构访问
- **安全边界**：定义清晰的权限和访问控制，保护敏感本地数据
- **标准化接口**：跨不同AI服务商的一致协议，便于工具发现和集成
- **2026 Coding Plan支持**：主要国产AI服务商已在其Coding Plan产品中原生支持MCP

## Related

- [[coding-plan]]
- [[ai-tool-chaining-combination-combination]]
- [[claude-md]]
- [[skills-anthropic-framework]]
- [[agent-skills-vs-mcp-technical-comparison-and-enterprise-applications]]

---

The **Model Context Protocol (MCP)** is a standardized protocol mentioned within [[Skill Security Considerations]] as the preferred method for [[Skills (Anthropic Framework)|Skills]] to securely connect to and access external services. Instead of embedding API keys or credentials directly into skill files—a significant security risk—MCP provides a secure, standardized interface for agents to interact with tools, databases, and other resources. Its adoption is encouraged as part of developing secure, production-ready skill assets within the [[Agent Skills Framework]], reflecting the ecosystem's maturation and focus on safe deployment.

## Related
- [[Coding Plan]]
- [[AI Tool Chaining/Combination]]
- [[CLAUDE.md]]
- [[Alibaba Cloud Bailian]]
- [[Skill Security Considerations]]
- [[Agent Skills Framework]]