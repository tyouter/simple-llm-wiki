---
title: "Claude Code编排n8n工作流"
type: source
sources:
  - "raw/videos/d88e13cd_用Claude Code自动编排n8n工作流告别手搓.md"
tags:
  - "claude-code"
  - "n8n"
  - "workflow"
  - "mcp"
  - "skills"
  - "automation"
  - "video"
confidence: medium
created_at: "2026-04-20T12:00:00"
updated_at: "2026-04-20T12:00:00"
---

# Claude Code编排n8n工作流

## 视频信息

- **作者**: 杰森的效率工坊
- **发布日期**: 2026-03-31
- **时长**: 11:47
- **观看数**: 8.5K
- **点赞数**: 386

## 核心内容

### 主题概述

在AI智能体时代，n8n工作流并未被淘汰，而是成为智能体（如OpenClaw大龙虾）的最佳搭档。视频展示如何用Claude Code/OpenCode智能体自动创建n8n工作流。

### 核心观点

**n8n与智能体结合的必要性**:
- 把固定性任务放到工作流，降低Token消耗
- 把隐私密钥封装在n8n中，降低安全风险
- 只通过Webhook调用n8n

### 环境搭建

#### n8n安装
- npm install -g n8n（最快捷）
- Docker安装（推荐Docker Desktop + compose.yml）

#### n8n配置
1. 创建API Key（设置 -> n8n API）
2. 创建Credential密钥（如AI大模型API Key）

### MCP与Skills配置

#### Claude Code配置
- Skills目录：用户目录下`.claude`文件夹
- MCP配置：`.claude.json`文件添加n8n MCP配置

#### OpenCode配置
- Skills目录：`.config/opencode/skills`
- MCP配置：`opencode.json`添加MCP配置

### 实战案例

#### AI资讯获取工作流
从Google DeepMind RSS订阅获取AI论文：
- 调用AI翻译整理
- 格式化数据
- 保存到n8n内置数据表格

#### 关键步骤
1. 把Credential ID发送给智能体
2. 智能体使用已创建的密钥创建节点
3. 工作流创建完毕后刷新执行

### 注意事项

1. **错误处理**: 复制错误信息发给Claude Code，智能体自行排查修复
2. **复杂工作流**: 先让智能体分析和计划，确认后再执行
3. **模型选择**: OpenCode可用免费模型（如小米Mimo V2 Pro）

### 相关资源

- awesome-open-claw-use-case仓库：有n8n案例和打包镜像

## Related

- [[n8n]]
- [[Claude Code]]
- [[MCP]]
- [[自动化工作流]]
- [[OpenClaw]]