---
title: "OpenClaw"
type: "concept"
sources:
  - "raw/videos/00b97521_全网最细 OpenClaw 教学完整部署飞书连接白嫖LLM无限进化框架看完彻底学会.md"
  - "raw/videos/df67d69c_OpenClaw高级使用经验分享2026年最强生产力五分钟打造多Agent协作编程开发团队模型容灾机制深度配置云端Gateway操控本地macOS.md"
tags:
  - "openclaw"
  - "ai-agent"
  - "framework"
  - "automation"
confidence: "high"
created_at: "2026-04-20T12:00:00"
updated_at: "2026-04-20T12:00:00"
---

# OpenClaw

## 定义

OpenClaw 是一个开源的 AI 助手框架，支持多种大语言模型接入、自动化工作流配置和多 Agent 协作。

## 核心特性

### 多模型支持

- 支持 Anthropic、OpenAI、Google 等多种模型
- 模型容灾机制：三级自动切换
- 多认证 OAuth 登录与 Token 轮询

### 多 Agent 协作

三种核心协作模式：

| 模式 | 描述 |
|------|------|
| 线性流水线 | Agent 按顺序执行任务 |
| 并行依赖图 | 多 Agent 并行执行，根据依赖关系协调 |
| AI辩论模式 | 多 Agent 通过辩论达成共识 |

### 记忆与搜索

- 使用 Gemini 实现混合检索
- 无需本地模型
- 跨会话知识持久化

### 云端远程控制

- 通过 Node 配对实现远程控制
- 无需内网穿透
- 支持从云端操控本地设备

## GitHub 地址

https://github.com/Work-Fisher/openclaw-ai-assistant-framework

## 应用场景

- AI 编程开发团队
- 自动化工作流
- 企业 AI 定制服务
- 个人知识管理

## Related

- [[AI-Agent]]
- [[Multi-Agent-Orchestration]]
- [[Agent-Framework]]
- [[Model-Failover]]