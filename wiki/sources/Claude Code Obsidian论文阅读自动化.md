---
title: "Claude Code Obsidian论文阅读自动化"
type: source
sources:
  - "raw/videos/d907b96c_Claude CodeObsidian每天自动读论文早上到工位来上这么一篇真是惬意呀.md"
tags:
  - "claude-code"
  - "obsidian"
  - "paper-reading"
  - "automation"
  - "academic"
  - "skills"
  - "video"
confidence: medium
created_at: "2026-04-20T12:00:00"
updated_at: "2026-04-20T12:00:00"
---

# Claude Code Obsidian论文阅读自动化

## 视频信息

- **作者**: 居丽叶与谷密欧
- **发布日期**: 2026-03-04
- **时长**: 1:56
- **观看数**: 7.9万
- **点赞数**: 2.4K

## 核心内容

### 主题概述

使用Claude Code和Obsidian实现自动化论文阅读流程，每天自动推荐高质量论文并生成详细笔记。

### 工具组合

- Claude Code
- Obsidian

### 自动化流程

#### Skills配置
从GitHub下载四个skills放到Claude Code的skills目录下

#### 双源策略

1. **arXiv爬取**: 最近一个月的论文，按时间排序
2. **Semantic Scholar爬取**: 过去一年高引用高热度论文

策略原因：arXiv无法按引用数/热度搜索，Semantic Scholar弥补短板

#### 论文推荐机制

系统每天推荐10篇论文，从四个维度评分：
- 热度
- 发布时间
- 相关性
- 贡献度

按总分从高到低排序，返回前三篇高分论文

#### 笔记生成

- 自动在对应目录生成详细笔记
- 包含标签和论文间关系图谱
- 多模态论文关联脉络一目了然（如CLIP、BLIP）

#### 深入阅读

对于后7篇论文，输入 `paper analyze + 论文编号` 一键生成详细笔记，自动关联到今日推荐笔记

### Semantic Scholar优化

官网申请API Key可解除访问速率限制

## Related

- [[Claude Code]]
- [[Obsidian]]
- [[Claude Code Skills系统]]
- [[论文阅读自动化]]