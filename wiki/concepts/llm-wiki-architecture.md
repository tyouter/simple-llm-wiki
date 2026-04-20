---
title: "LLM Wiki架构"
type: "concept"
sources:
  - "raw/articles/1ecc9a25_如何评价Karpathy提出的个人知识库的架构如何评价Karpathy提出的个人知识库的架构.md"
tags:
  - "knowledge-base"
  - "llm"
  - "architecture"
  - "three-layer-architecture"
confidence: "high"
created_at: "2026-04-20T12:00:00"
updated_at: "2026-04-20T12:00:00"
related:
  - "知识编译器模式"
  - "Andrej Karpathy"
  - "RAG检索增强生成"
---

# LLM Wiki架构

## 定义

Karpathy提出的基于LLM的个人知识库系统架构，将知识管理分为三个层次，形成"非代码项目的集成开发环境"。

## 三层架构

### 第一层：Raw原始数据层

- 存放原始文档，LLM只读不改
- 导入引擎将多种格式转换为Markdown
- 使用Obsidian Web Clipper把网页转为Markdown并本地化图片

### 第二层：Wiki知识图谱层

- LLM生成的结构化Markdown文件集合
- 包含概念页、来源摘要、实体条目
- 页面间通过backlinks相互引用
- 这是真正的知识库核心

### 第三层：Schema配置层

- 配置文件（如CLAUDE.md）定义Wiki的组织结构
- 格式约定和操作流程
- 将通用LLM变成有纪律的知识管理员

## 三种核心操作

1. **Ingest**：加入新原始资料，LLM读完后更新Wiki，通常触及10-15个已有页面
2. **Query**：提问，LLM翻自己写的Wiki回答，有价值回答也归档进Wiki
3. **Lint**：定期健康检查，找矛盾、孤立页面、过时内容

## 技术栈特点

- 简单：全是本地Markdown文件
- 可控：无外部API依赖
- 可溯源：所有证据链明文可读

## 应用扩展

这套架构不仅限于知识库，可扩展为"知识类工作的通用Agent"：

- 文员：整理邮件、会议纪要，做PPT
- 科研工作：通读论文，写综述
- 新闻媒体：整理热点，写播客稿
- 分析师：收集财报数据，写研究报告
- 作者：写大纲、收集资料、章节写作
- 教师：加工教材，产出课件、作业

## Related
- [[知识编译器模式]]
- [[Andrej Karpathy]]
- [[RAG检索增强生成]]