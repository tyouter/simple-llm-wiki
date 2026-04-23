---
title: "AutoResearch Claude Code Skill实战"
type: source
sources:
  - "raw/videos/712bf9fc_AutoResearch 让Claude像Karpathy一样自己迭代自己代码内容性能全自动无限优化Claude Code Skill实战分.md"
tags:
  - "autoresearch"
  - "claude-code"
  - "karpathy"
  - "自动迭代"
  - "性能优化"
confidence: medium
created_at: "2026-04-20T12:00:00"
updated_at: "2026-04-23T00:42:21.211839"
---

# AutoResearch Claude Code Skill实战

## 背景来源

Andrej Karpathy开源的"autoresearch"概念：
- AI自己设定目标
- 自己做实验
- 自己跑loop
- 自己保留好结果、丢掉差的
- 睡觉时还在疯狂进步

## AutoSkill项目

由Udit Goenka开源，将Karpathy思想泛化：
- 从机器学习训练循环扩展到任何可量化指标任务
- 作为Claude Code Skill实现

## 应用场景

只要能给出明确目标+可自动运行的量化指标：
- 提升代码测试覆盖率到95%
- 降低前端bundle体积
- 优化Lighthouse性能分数
- 提高网页可访问性/SEO得分
- 改进邮件文案打开率、内容质量打分

## 工作原理

### 配置要素
1. Goal：告诉它想干嘛
2. Verify command：测效果的命令（如npm test --coverage）
3. 方向：越高越好还是越低越好

### 执行循环
修改代码/内容 → git commit → 跑verify命令测指标 → 变好保留/变差git reset回滚 → 下一轮

## 使用方式

### 安装
拷贝到Claude Code的skills目录

### 执行
输入/autoresearch，设定目标后自动循环

### 模式
- 默认模式：不停迭代
- n次模式：迭代n次后结束
- 交互模式：先规划再确认
- security模式：渗透测试、安全扫描

## 重要提醒

- 需要足够token额度
- 目标设置要明确
- 需要有足够的算力支持

## 相关
- [[Andrej Karpathy]]
- [[Claude Code Skills系统]]
- 自动迭代优化