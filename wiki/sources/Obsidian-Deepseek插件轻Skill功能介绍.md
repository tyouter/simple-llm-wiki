---
title: "Obsidian-Deepseek插件轻Skill功能介绍"
type: source
sources:
  - "raw/videos/bb57b09a_Obsidian-deepseek 新功能 轻SKILL介绍没有发布.md"
tags:
  - "obsidian"
  - "deepseek"
  - "plugin"
  - "skill"
  - "ai-integration"
confidence: medium
created_at: "2026-04-20T12:00:00"
updated_at: "2026-04-20T12:00:00"
---

# Obsidian-Deepseek插件轻Skill功能介绍

## 概述

Obsidian-Deepseek插件新增了轻Skill功能，允许用户自定义常用命令，通过变量系统实现更灵活的笔记处理工作流。

## Skill核心功能

Skill系统允许用户创建自定义命令模板，实现：

- **选择内容处理**：对选中的文本内容进行特定处理
- **标题提取**：自动提取文档标题作为变量
- **笔记生成**：根据提示词模板自动生成新笔记
- **命令集成**：将常用操作封装为快捷命令

## 变量系统

目前实现的四个核心变量：

1. **$title**：文档标题
2. **$selection**：选择的内容
3. **文件属性信息变量**（规划中）
4. **文档内容变量**（规划中）

## 使用流程

1. 在Skill配置中定义命令模板
2. 选择需要处理的文本内容
3. 执行对应的Skill命令
4. 内容发送到Deepseek进行AI处理
5. 根据提示词生成处理结果

## 后续规划

- 增加更多变量类型
- 支持输入框功能，实时输入提示词
- 完善文档说明
- 发布正式版本

## Related

- [[Claude Code Skills系统]]
- [[Obsidian插件生态]]
- [[Deepseek]]