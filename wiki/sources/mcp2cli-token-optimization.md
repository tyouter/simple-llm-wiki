---
title: "mcp2cli：CLI取代MCP的Token优化方案"
type: source
sources:
  - "raw/videos/d241c58b_一个CLI干掉所有MCP工具省99的token mcp2cli.md"
tags:
  - "MCP协议"
  - "CLI工具"
  - "Token优化"
  - "AI工具调用"
confidence: medium
created_at: "2026-04-20T08:00:00"
updated_at: "2026-04-20T08:00:00"
---

# mcp2cli：CLI取代MCP的Token优化方案

## 核心信息

- **项目名称**: mcp2cli
- **发布时间**: 2026年3月10日
- **GitHub热度**: 发布一天获得372颗星
- **核心价值**: 将MCP协议Token浪费降低99%

## 问题背景

### MCP协议的Token浪费痛点
- 每轮对话客户端都会把所有工具完整schema塞进上下文
- 一个工具约120个token，30个工具=3600个token
- 120个工具25轮对话光schema就吃掉36万token
- 大量工具实际根本用不上

## 解决方案：懒发现机制

### 三步查询流程
1. **List命令**: 只返回工具名称（每个工具16个token）
2. **Help命令**: AI觉得有用时获取详细schema（80-200个token）
3. **确认执行**: 15个token确认调用

### 效果对比
- 30个工具15轮：从5.4万token降到2300token（节省96%）
- 120个工具场景：节省99%

## 技术实现

- **核心代码**: 仅一个Python文件
- **依赖**: HTTPX、MCP、PML（仅3个）
- **接入模式**: MCP HTTP远程服务器、MCP本地实例、OpenAPI规范

## 社区争议

- **支持者**: CLI才是正确方案，简单通用，任何大模型都能用
- **反对者质疑**: 懒发现是否降低准确率？多步往返是否增加延迟？
- **批评**: 只展示Token节省数据，未给出准确率对比

## 相关
- [[Claude Code Skills系统]]
- [[MCP协议分析]]
- [[AI工具调用效率]]