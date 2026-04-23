---
title: "国产大模型 Coding Plan 横评避坑指南"
type: "source"
sources:
  - "raw/videos/2c940938_爆肝5小时实测国产大模型横评Coding Plan避坑指南.md"
tags:
  - "chinese-llm"
  - "coding-plan"
  - "model-comparison"
  - "evaluation"
  - "glm"
  - "minimax"
  - "qwen"
confidence: "high"
created_at: "2026-04-20T12:00:00"
updated_at: "2026-04-23T00:42:21.268030"
---

# 国产大模型 Coding Plan 横评避坑指南

## 概述

本视频对2026年初发布的国产大模型进行了5小时实测，对比它们在复杂项目开发中的表现，为开发者提供选型参考。

## 测试模型

| 模型 | 类型 | 备注 |
|------|------|------|
| GLM-5 | 开源模型 | pro 版本测试 |
| MiniMax M2.5 | 付费模型 | 测试版本 |
| Qwen 3.5-plus | 付费模型 | 最新版本 |

注：Deepseek Code v3.2 已正式版支持百万 tokens，但本次对比未纳入。

## 测试方法

### 环境准备

- GitHub 安装 web 工具
- Vim 中并行开发
- 多个 Claude Code 同时运行不同模型

### 测试流程

1. 在项目目录新建 docs 目录
2. 运行 web 工具选择不同供应商
3. 输入对应 API Key
4. 进行并行开发测试

### 评估维度

- UI 原型设计速度
- 开发计划编写能力
- 实际代码生成质量
- Token 消耗情况

## 测试结果

### MiniMax M2.5

- **优点**: UI 效果和还原度最高，开发速度最快
- **Token 消耗**: 仅消耗套餐额度约 15%
- **成本**: 相对较低

### Qwen 3.5-plus

- **优点**: 基本完成开发
- **Token 消耗**: 与 MiniMax 相近
- **实际费用**: 约 30 元以上

### GLM-5

- **问题**: Pro 版本 Token 消耗异常（约 95%）
- **结果**: 未输出完整 UI 原型和文档
- **成本**: 购买套餐成本高，性价比不佳

## 避坑建议

1. **GLM-5**: 购买套餐需谨慎，Token 消耗异常
2. **MiniMax M2.5**: 推荐，性价比最高
3. **Qwen 3.5-plus**: 可用，成本适中

## 视频信息

- **作者**: 野码AI
- **发布日期**: 2026-02-17
- **时长**: 7:46
- **观看数**: 5.1万
- **点赞数**: 721

## Related

- [[国产大模型]]
- [[Plan]]
- GLM
- [[MiniMax]]
- [[Qwen]]
- 模型选型