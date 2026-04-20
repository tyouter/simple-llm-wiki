---
title: "OpenPencil - AI原生开源设计编辑器"
type: "source"
sources:
  - "raw/videos/136f10d5_开源 Figma 来了AI 原生设计编辑器 OpenPencil7MB 本地运行还能多人协作.md"
tags:
  - "开源设计工具"
  - "AI设计"
  - "Figma替代"
  - "OpenPencil"
  - "Vue3"
  - "Tauri"
confidence: "medium"
created_at: "2026-04-20T12:00:00"
updated_at: "2026-04-20T12:00:00"
---

# OpenPencil - AI原生开源设计编辑器

## 概述
OpenPencil是一个AI原生的开源设计编辑器，完全兼容Figma的.fig文件格式，内置75个AI工具，整个应用仅7MB，支持本地运行和多人协作。该项目是对Figma封杀第三方自动化接口的回应，为设计师提供了开源替代方案。

## 关键内容

### 核心特性
- **原生兼容Figma文件**：完全兼容.fig文件格式，支持节点复制粘贴
- **AI原生设计**：内置75个AI工具，支持自然语言描述生成设计
- **轻量化**：整个应用仅7MB，不需要账号和联网即可本地运行
- **MCP服务连接**：可与Claude Code或Cursor等AI编程工具连接，支持CLI命令行操作
- **多人协作**：基于WebRTC点对点协作，不需要服务器

### 技术栈
- Vue 3 + Skia渲染引擎
- Tauri v2桌面端打包
- MIT开源协议

### 项目背景
Figma封杀了第三方自动化接口后，设计师的工作流被平台绑架。OpenPencil作为开源替代方案，解决了以下痛点：
- MCP服务只能读不能写的问题
- CDP协议绕过限制被封锁的问题
- 设计文件和工作流被平台控制的风险

## 相关概念
- [[开源设计工具]]
- [[AI原生应用]]
- [[MCP服务]]

## 相关实体
- [[锋芒AI]]