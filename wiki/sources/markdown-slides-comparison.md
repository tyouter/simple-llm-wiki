---
title: "Markdown制作幻灯片的三种方案对比"
type: source
sources:
  - "raw/webpages/0ac94217_让我们专注于内容Markdown 制作幻灯片的三种方案对比 - 少数派.md"
tags:
  - "markdown"
  - "ppt"
  - "效率工具"
  - "obsidian"
  - "marp"
  - "slidev"
confidence: medium
created_at: "2026-04-20T12:00:00"
updated_at: "2026-04-20T12:00:00"
---

# Markdown制作幻灯片的三种方案对比

## 概述
少数派文章，对比了三种使用Markdown制作演示文稿的方案：Obsidian幻灯片插件、Marp和Slidev。作者为知识工程研究者、Obsidian重度用户"西郊次生林"。

## PowerPoint的问题
- 排版手段过于灵活，容易排出混乱丑陋的版面
- 排版方式复杂，需要大量精力应付排版，不能专注内容
- 公式书写体验差（继承Office全家桶公式系统）
- AI生成的PPT虚有其表，内容细节禁不起推敲

## 三种方案对比

### Obsidian幻灯片（核心插件）
- **特点**：用`---`分隔页面，命令面板启动演示
- **缺点**：排版效果不佳（全文居中、字体浮夸），无自定义设置，无导出PPT选项
- **评价**：半成品状态，不适合实际应用

### Marp
- **特点**：
  - 支持实时预览
  - 支持导出PPT/PDF/PNG
  - 支持自定义主题（.scss文件）
  - Awesome Marp提供丰富主题库
- **注意事项**：
  - Obsidian插件存在bug（可能一键删除文件）
  - VSCode插件更成熟稳定
  - 导出位图PPT，不支持PowerPoint再修改
- **评价**：平衡了可定制性和易上手程度，推荐VSCode版本

### Slidev
- **特点**：
  - 基于Node.js，npm生成项目
  - 支持HTML语法自定义交互组件
  - 支持自定义CSS（渐变标题等）
  - shiki-magic-move实现惊艳代码动画
  - 属性更丰富，高度专业化
- **缺点**：
  - 上手难度高（需要前端背景）
  - 导出位图PPT，失去动画效果
  - 清晰度不高
- **评价**：适合用自己的电脑录制/现场演示，不适合导出使用

## 核心建议
使用Markdown做PPT的核心价值：**将注意力集中到内容而非排版**。

避免陷入配置陷阱：制作一个模板Markdown文件后复用，适可而止停止折腾。

## Related
- [[Obsidian]]
- [[效率工具]]
- [[Office替代方案]]