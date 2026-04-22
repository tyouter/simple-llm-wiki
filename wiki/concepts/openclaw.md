---
title: "OpenClaw"
type: "concept"
sources:
  - "raw/videos/00b97521_全网最细 OpenClaw 教学完整部署飞书连接白嫖LLM无限进化框架看完彻底学会.md"
  - "raw/videos/df67d69c_OpenClaw高级使用经验分享2026年最强生产力五分钟打造多Agent协作编程开发团队模型容灾机制深度配置云端Gateway操控本地macOS.md"
  - "raw/articles/25f38aec_一般技术大牛都在哪里写博客一般技术大牛都在哪里写博客.md"
tags:
  - "openclaw"
  - "ai-agent"
  - "framework"
  - "automation"
confidence: "high"
created_at: "2026-04-20T12:00:00"
updated_at: "2026-04-20T12:00:00"
related:
  - "博客内容动态筛选机制"
  - "Agent-Based Active Retrieval"
  - "AI Content Saturation"
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

---

**OpenClaw** 是一个新兴的AI Agent（智能体）平台或框架，允许用户构建和部署能够执行复杂任务的自主AI程序。在本文提及的案例中，OpenClaw的社区开发者为其创建了一个特殊的“Skill”（技能）。这个Skill的功能是：定期从一个由人工维护的、包含数百个高质量技术博客的RSS源列表中抓取最新文章，然后利用AI对文章进行摘要或筛选，最终将精华内容推送给用户。

这个案例是[[博客内容动态筛选机制|自动化智能筛选机制]]的完美体现，它将传统RSS订阅与AI处理能力相结合。它也展示了[[Agent-Based Active Retrieval|基于智能体的主动信息检索]]在实际中的应用场景——AI Agent不再被动等待查询，而是主动为用户管理和提炼信息流。这种工具的出现，正是为了应对[[Andrej Karpathy]]所抱怨的、由[[AI Content Saturation|AI生成内容泛滥]]导致的信息环境恶化问题，旨在帮助用户重建一个高效、优质的信息摄入系统。

## Related
- [[博客内容动态筛选机制]]
- [[Agent-Based Active Retrieval]]
- [[AI Content Saturation]]