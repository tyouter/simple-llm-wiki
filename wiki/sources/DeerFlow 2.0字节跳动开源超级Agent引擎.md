---
title: "DeerFlow 2.0：字节跳动开源超级Agent引擎"
type: source
sources:
  - "raw/videos/ced2ad0c_DeerFlow 2.0字节跳动开源下一代超级 Agent 员工.md"
tags:
  - "agent"
  - "bytedance"
  - "opensource"
  - "deerflow"
  - "multi-agent"
  - "github"
confidence: medium
created_at: "2026-04-20T12:00:00"
updated_at: "2026-04-20T12:00:00"
---

# DeerFlow 2.0：字节跳动开源超级Agent引擎

## 项目概述

DeerFlow 2.0是字节跳动开源的超级智能体引擎，开源当天登上GitHub Trending榜首，两天斩获3.7万星标。官方定义它为"超级智能体引擎"，不仅是框架，而是完整的智能体员工系统。

## 核心能力

### 全套流水线功能

- **沙盒环境**：任务运行在隔离的Docker容器
- **长效记忆**：记住代码习惯、技术栈偏好、写作风格
- **技能扩展**：可扩展能力模块
- **多智能体编排**：复杂任务自动派出子Agent分头执行

### 内置技能

- 写报告
- 建网站
- 做PPT
- 生成视频

## 技术架构

| 模块 | 功能 |
|------|------|
| Docker沙盒 | 完整文件系统，支持读写编辑、代码执行 |
| 长期记忆 | 用户习惯学习，越用越顺手 |
| 子Agent | 任务分解与汇总交付 |
| 模型接入 | GPT、DeepSeek、豆包等 |

## 工作方式

1. 接收复杂任务
2. 自动派出子Agent
3. 分头执行分解后的任务
4. 汇总交付最终结果

## 项目数据

- **GitHub Stars**：3.7万（两天）
- **排名**：GitHub Trending榜首
- **开源方**：字节跳动
- **代码状态**：完全开源

## 模型支持

- GPT
- DeepSeek
- 豆包
- 其他主流大模型

## 与传统框架对比

| 传统框架 | DeerFlow 2.0 |
|---------|-------------|
| 深度研究局限 | 全套流水线 |
| 单Agent | 多Agent编排 |
| 无记忆 | 长效记忆 |
| 无沙盒 | Docker隔离 |

## Related

- [[多智能体系统]]
- [[字节跳动AI]]
- [[Agent框架]]
- [[OpenClaw]]
- [[DeepAgents框架]]