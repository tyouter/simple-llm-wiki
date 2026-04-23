---
title: "project-analyzer逆向工程Skill介绍"
type: source
sources:
  - "raw/videos/76198251_别再手撸PRD了我做了一个逆向工程Skill.md"
tags:
  - "claude-code"
  - "skill"
  - "逆向工程"
  - "PRD"
  - "开源项目分析"
confidence: medium
created_at: "2026-04-20T12:00:00"
updated_at: "2026-04-23T00:42:21.836861"
---

# project-analyzer逆向工程Skill介绍

## 核心痛点

对开源项目进行精品分析时：
- 成千上万行代码无从下手
- 开源项目没有PRD文档可供参考
- 需要从代码反推产品逻辑

## project-analyzer Skill功能

### 生成PRD文档
包含14个章节：
- 产品定位
- 用户故事
- Agent故事
- Agent流程设计
- 提示词设计策略
- Agent故事详细表系（输入输出、工具清单）
- 等等

### 提示词分析
- 自动提取Prompt
- 中文翻译
- 参数解析
- 相关代码对照
- 学习AI应用的教科书级资料

### 输出文件结构
- PRD文档（markdown）
- 提示词分析文件夹
- JSON格式的提示词目录
- 提示词文档（含原文、翻译、参数说明）

## 使用流程

### 两步操作
1. 输入开源项目路径，执行/project-analyzer
2. 查看提示词分析确认无误，输入"启动PRD生成"

## Skill来源

整合了两个Skill：
- 张佳老师的howPrompt（拆解提示词）
- 作者之前做的AI应用PRD生成Skill

通过多次迭代形成project-analyzer Skill

## 应用场景

- 快速调研竞品
- 接手公司的老旧项目
- 学习优秀开源项目
- 从"搬砖式看代码"变成"上帝视角读PRD文档"

## 相关
- [[Claude Code Skills系统]]
- 逆向工程
- [[Prd]]