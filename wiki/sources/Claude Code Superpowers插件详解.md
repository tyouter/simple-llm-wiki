---
title: "Claude Code Superpowers插件详解"
type: source
sources:
  - "raw/videos/cbf5a163_Claude Code Now Has SUPERPOWERS plugin.md"
tags:
  - "claude-code"
  - "plugin"
  - "superpowers"
  - "tdd"
  - "sub-agent"
  - "github"
confidence: medium
created_at: "2026-04-20T12:00:00"
updated_at: "2026-04-20T12:00:00"
---

# Claude Code Superpowers插件详解

## 项目概述

Superpowers是Claude Code的官方插件，强制执行正确的开发工作流程，包括头脑风暴、规划、TDD、子代理、代码审查和Git工作树隔离。43K+ GitHub Stars，已正式进入Anthropic官方市场。

## 核心功能

### 开发方法论强制执行

- **头脑风暴**：Brainstorm模式细化模糊提示词
- **规划文档**：PRD创建、设计文档、实现计划
- **TDD**：测试驱动开发
- **子代理开发**：分阶段执行实现计划
- **代码审查**：自动审查机制
- **Git工作树隔离**：独立分支开发

## 安装方式

### 方式一：官方市场安装（最简单）
- 通过Anthropic官方marketplace安装

### 方式二：GitHub仓库添加
- 仓库地址：https://github.com/obra/superpowers/tree/main
- 手动添加到Claude Code

## 核心命令

| 命令 | 功能 |
|------|------|
| /superpowers | 启动Superpowers |
| brainstorm | 头脑风暴模式 |
| write plan | 撰写实现计划 |
| execute plan | 执行实现计划 |

## 工作流程演示

从模糊提示词到完整应用：
1. Brainstorm细化想法
2. 创建PRD
3. 编写设计文档
4. 详细实现计划
5. 分阶段执行（子代理）
6. 测试与修复
7. 连接后端（如Supabase）
8. 最终演示

## 工作流优势

- 结构化输出，减少灾难性错误
- Claude像资深开发团队一样思考
- 开源免费，仅需API成本
- Anthropic官方认可

## 适用场景

- 复杂项目开发
- 已有代码库的迭代
- 需要结构化输出的场景

## 项目数据

- **GitHub Stars**：43K+
- **官方认证**：Anthropic marketplace
- **开源状态**：完全开源

## 相关工具集成

- Frontend-design插件
- Supabase（后端）
- Vercel（部署）

## Related

- [[Claude Code Skills系统]]
- [[TDD方法论]]
- [[子代理架构]]
- [[Git工作树]]