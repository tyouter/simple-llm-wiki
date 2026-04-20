---
title: "OpenClaw"
type: "entity"
sources:
  - "wiki/sources/知乎讨论-普通人第一次用OpenClaw应该注意什么.md"
  - "wiki/sources/知乎讨论-OpenClaw实用应用与局限性.md"
  - "wiki/sources/openclaw-complete-deployment-tutorial.md"
tags:
  - "ai-framework"
  - "agent-orchestration"
  - "benchmark-tool"
  - "complex-deployment"
confidence: "high"
created_at: "2026-04-19T21:41:38.070657"
updated_at: "2026-04-20T00:00:00"
---

# OpenClaw

## 概述
OpenClaw是开源AI助手框架，在AGENT元年被称为具有"明星效应"的标杆作品，支持多模型接入、多Agent协作和自动化工作流配置，但部署复杂且存在安全风险，需要虚拟机隔离和严格的权限管理。

## 基本信息
- 类型：AI Agent框架
- 特点：开源、多Agent协作、工具链组合
- 相关领域：AI自动化、Agent编排、本地部署

## 核心能力

### Agent编排
- 作为[[Agent Operating System]]协调专业化AI代理
- 实现[[AI工具链组合]]原则构建复杂工作流
- 支持多模型接入与容灾切换机制

### 工具集成
- 技能(Skill)系统扩展能力
- MCP服务器集成
- 自动化工作流配置

### 模型抽象
- 支持多种AI模型
- 实现fallback能力解决单点故障
- Token消耗管理机制

## 版本特性

### 3.2+版本
- 默认只读模式需配置修改获得完整功能
- 后续版本增加安全特性
- 考虑技能和配置迁移兼容性

## 部署要求

### 安全强制措施
- **虚拟机隔离**：必须在虚拟机中部署
- **最小权限**：最小权限执行原则
- **技能审查**：谨慎评估技能安装风险

### 技术前提
- 支持快照功能的虚拟化平台
- API管理和Token监控系统
- 性能和安全监控基础设施

## 社区定位
- AGENT元年的标杆作品
- "明星效应"反映广泛关注和采用
- 非新手友好，需要技术指导

## 相关
- [[知乎讨论-普通人第一次用OpenClaw应该注意什么]]
- [[知乎讨论-OpenClaw实用应用与局限性]]
- [[Moltbot]]
- [[ClawdBot]]
- [[OpenAkita开源自我进化AI助手框架]]
- [[模型容灾机制]]