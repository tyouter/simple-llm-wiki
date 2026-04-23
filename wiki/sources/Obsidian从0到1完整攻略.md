---
title: "Obsidian从0到1完整攻略"
type: source
sources:
  - "raw/videos/eb586db5_Obsidian从0到1完整攻略 搞定同步打通AI.md"
tags:
  - "obsidian"
  - "setup"
  - "sync"
  - "ai-integration"
  - "claudian"
  - "cli"
  - "video"
confidence: medium
created_at: "2026-04-20T12:00:00"
updated_at: "2026-04-23T00:42:21.692247"
---

# Obsidian从0到1完整攻略

## 视频信息

- **作者**: Blink的AI笔记
- **发布日期**: 2026-03-29
- **时长**: 12:25
- **观看数**: 1.9万
- **点赞数**: 723

## 核心内容

### 主题概述

Obsidian上手第一天必做的7件事，解决新手被高自由度劝退的问题，从同步方案到AI集成一网打尽。

### 第一步：同步方案规划

#### 5种同步方案对比

1. **iCloud**: 苹果全家桶最佳，免费无缝同步
2. **官方同步服务**: 全平台支持，每月10刀订阅
3. **Google Drive**: 国外非苹果用户
4. **OneDrive**: 国内非苹果用户
5. **NAS/Git**: 极客方案

#### iCloud同步关键设置

开启"保留下载"：
- iCloud默认会自动删除本地不常用文件
- 对笔记来说反复下载影响效率
- 右键iCloud里的Obsidian文件夹开启保留下载

### 第二步：基础配置

#### 必做配置

1. **语言切换**: 简体中文
2. **链接设置**: 开启始终更新内部链接
3. **附件管理**: 创建attachments文件夹存放所有附件
4. **核心插件**: 开启反向链接、命令面板、属性列表

### 第三步：双向链接实践

使用双方括号创建链接：
- 中文输入法连续输两个方括号自动切换英文
- 显示反向链接（哪些笔记引用了当前笔记）
- 局部关系图可视化链接关系

### 第四步：笔记属性

笔记属性包括：
- 创建时间（自动）
- 更新时间（自动）
- 类型（card-note等）
- 标签
- 出处

可用于项目管理（状态标记等）

### 第五步：Daily日志与Bases

Bases功能通过条件筛选笔记，自动在日志展示：
- 今天创建的笔记
- 提到今天的笔记

### 第六步：Obsidian CLI开启

在设置-高级中开启命令行界面，注册

### 第七步：Claudian插件安装

#### 安装步骤

1. 先装社区插件（如Excalidraw）
2. 从Claudian GitHub下载三个文件
3. 放到`.obsidian/plugins/claudian`文件夹
4. 启用插件

#### Claudian配置

- 界面语言：简体中文
- 附件文件夹：attachments

### Claudian优势

1. **上下文感知**: 自动识别当前笔记
2. **直接修改**: AI输出可直接添加到选中文本下方
3. **不离开Obsidian**: 在软件内直接对话

## Related
- [[Agent]]
- [[Cli]]
- [[Git]]
- [[Markdown]]
- [[Skill]]
- [[GitHub]]
- [[Google]]
- [[Notion]]
- [[Obsidian CLI官方命令行工具教程]]
- [[Obsidian接入Claude Skill教程]]

- [[Obsidian]]
- [[Obsidian CLI]]
- Claudian插件
- 双向链接