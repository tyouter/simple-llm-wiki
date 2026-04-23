---
title: "为AI构建代码知识图谱的两个Skill"
type: source
sources:
  - "raw/videos/8b4f5533_我做了两个 Skill为 AI 构建代码知识图谱.md"
tags:
  - Skills
  - 知识图谱
  - AI编程
  - 代码分析
  - MCP
confidence: medium
created_at: "2026-04-20T21:00:00"
updated_at: "2026-04-23T00:42:21.984420"
---

# 为AI构建代码知识图谱的两个Skill

## 概述

作者开发了两个名为Nexus的Skills，帮助AI构建项目的代码知识图谱。这两个Skill解决的核心问题是：当上下文窗口接近限制或切换新对话时，让AI能够快速恢复对项目的理解，避免因读取项目不全面而产生误差。

## 核心要点

### 核心问题
- AI结对编程中上下文窗口容易耗尽
- 切换窗口或压缩对话后，AI需要重新理解项目
- 简单的文件读取容易遗漏关键信息
- 恢复记忆需要消耗大量时间和token

### Nexus Code Map Skill（完整版）
**结构化文档组成**：
- **引导文件index**：AI恢复项目记忆的主入口，包含项目概况和关键文件导航
- **架构层**：system记录核心系统，panaces记录调用关系，coverage记录测试情况
- **语义理解层**：JSON文件记录重要概念，MD格式解析术语
- **历史分析层**：分析git历史中活跃/高风险文件，经常一起改动的文件组合
- **原始数据层**：通过脚本分析得出的结构数据

**脚本功能**：
- 输出指定文件的结构评估
- 查询依赖指定文件/模块的文件列表
- 查询项目全局依赖图谱，找到核心结构
- 查询代码图中的节点信息

### Nexus STM Code Query Skill（轻量版）
- 不包含项目全景分析和地图文档
- 专注于结构分析
- 通过查询依赖图谱和代码结构为AI提供精准文档
- 适合不想做完整文档的用户

### 安装使用
- GitHub开源：搜索Nexus-skills
- 安装命令：`npx skills add haaaiawd/nexus-skills`

## Related
- [[Agent Skills与MCP技术对比与企业应用]]
- [[Anthropic Skills工程方法]]
- [[Claude Code隐藏功能指南]]
- 代码知识图谱构建