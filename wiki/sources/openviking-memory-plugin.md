---
title: "OpenViking记忆插件"
type: "source"
sources:
  - "raw/videos/0ed3a20e_字节火山开源OpenViking记忆插件 openClaw token成本降低92.md"
tags:
  - "openviking"
  - "memory"
  - "token-optimization"
  - "openclaw"
  - "bytedance"
  - "llm"
confidence: "medium"
created_at: "2026-04-20T00:00:00"
updated_at: "2026-04-20T00:00:00"
---

# OpenViking记忆插件

## 概述

龙哥搞算法介绍字节火山开源的OpenViking记忆插件，采用文件系统管理方式，分层上下文按需加载，token成本降低92%。

## 视频信息

- **作者**: 龙哥搞算法
- **发布日期**: 2026-03-19
- **时长**: 0:30
- **观看数**: 2.8K
- **点赞数**: 108

## 关键内容

### 核心特点
- 字节火山开源项目
- 记忆数据库设计
- Token成本降低92%
- 与OpenClaw集成使用

### 分层架构
采用三层结构设计：
- **L0**: 最核心最常用的信息，常驻内存
- **L1**: 次重要的信息，按需加载
- **L2**: 大量历史信息，用时再读取

### 管理方式
- 文件系统管理方式
- 不需要复杂的向量数据库操作
- 只需建文件夹、拖文件

### 优势
- 显著降低token成本
- 简化操作流程
- 按需加载提高效率

## 相关概念

- [[OpenClaw]]
- [[大模型]]
- [[Token优化]]
- [[记忆系统]]

## 相关实体

- [[龙哥搞算法]]
- [[字节跳动]]