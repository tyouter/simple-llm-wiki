---
title: "Harness Engineering与复合工程"
type: "source"
sources:
  - "raw\articles\825c9077_为什么我觉得 AI 写代码纯属添乱为什么我觉得 AI 写代码纯属添乱.md"
tags:
  - "ai-development"
  - "harness-engineering"
  - "compound-engineering"
  - "agent-architecture"
  - "software-engineering"
  - "ai-agents"
  - "workflow-automation"
  - "knowledge-management"
  - "source-document"
confidence: "high"
created_at: "2026-04-19T01:52:16.381586"
updated_at: "2026-04-19T01:52:16.381586"
related:
  - "Harness Engineering"
  - "Compound Engineering"
  - "Agent Harness"
  - "OpenAI"
  - "Anthropic"
  - "Every"
  - "Mitchell Hashimoto"
  - "Ethan Mollick"
  - "汉松"
  - "Claude Code Agent Technical Analysis and Multi-Agent Architecture"
  - "Agent Operating System"
  - "AI Tool Chaining/Combination"
  - "GStack: Role-Based AI Development Workflow for Claude Code"
  - "Vibe Coding"
  - "Single-Mode Problem"
---

# Harness Engineering与复合工程

## 概述
本文对AI驱动的软件开发方法论进行了详细分析，重点关注[[Harness Engineering]]和[[Compound Engineering]]。文章描述了[[OpenAI]]和[[Anthropic]]等组织如何实施AI Agent自主编写和维护代码的系统，人类则专注于更高层的架构和监督。

## 核心发现

### 大规模纯AI开发
文章描述了[[OpenAI]]的一项实验：3人团队在5个月内使用纯AI开发产出100万行代码。这代表了与传统软件工程的根本转变——传统模式中人类编写大部分代码。

### 方法对比
文章对比了两种方法：
- **[[Vibe Coding]]**：使用高层审美提示词获得短期生产力提升
- **[[Compound Engineering]]**：长期的知识积累和复用

### 实践实施
作者[[汉松]]（来自蚂蚁集团）分享了在真实项目中实施[[Harness Engineering]]方法的实践经验，展示了从人类主导向[[Agent-First Development]]的转变。

## 核心概念

文章引入了多个关键概念：
1. **[[Harness Engineering]]**：AI Agent管理整个开发生命周期的方法论
2. **[[Agent Harness]]**：AI Agent的基础设施（类似于Docker之于容器）
3. **[[Compound Engineering]]**：知识积累方法论，每个任务都产生"复利"
4. **[[Context Engineering]]**：优化AI Agent输入以获得更好表现
5. **[[Agent-First Development]]**：将AI Agent视为主要开发者

## 行业背景

### 关键参与者
- **[[OpenAI]]**：进行了大规模纯AI开发实验
- **[[Anthropic]]**：开发了"agent harness"概念和Claude Agent SDK
- **[[EleutherAI]]**：创建了Language Model Evaluation Harness用于测试生成式AI模型
- **[[Every]]**：开发了"Compound Engineering"方法论

### 思想领袖
- **[[Mitchell Hashimoto]]**：HashiCorp联合创始人，正式定义了"harness engineering"术语
- **[[Ethan Mollick]]**：提出了三层AI生态系统模型：模型、应用和Harness

## 方法框架

文章描述了结构化的工作流程：
1. **头脑风暴（Brainstorm）**：生成想法和需求
2. **规划（Plan）**：创建详细实施计划
3. **执行（Work）**：执行开发任务
4. **审查（Review）**：评估和完善输出
5. **复利（Compound）**：记录并积累知识供未来复用

这一工作流代表了[[AI Tool Chaining/Combination]]的高级方法。

## 与其他概念的关联

- **[[Claude Code Agent Technical Analysis and Multi-Agent Architecture]]**：两者都讨论AI Agent架构和用于开发的多Agent系统
- **[[Agent Operating System]]**：[[Harness Engineering]]代表了类似的概念——协调AI Agent执行开发任务
- **[[GStack: Role-Based AI Development Workflow for Claude Code]]**：类似的结构化工作流方法，使用专业化角色/任务
- **[[Single-Mode Problem]]**：[[Harness Engineering]]使用多个专业化Agent而非单一模型处理所有任务

## 与传统方法的矛盾

1. **与传统软件工程矛盾**：主张纯AI代码生成配合人类监督，而非人类编写大部分代码
2. **与常见AI编程工具用法矛盾**：多数开发者将AI作为助手而非主要开发者使用
3. **与[[Vibe Coding]]矛盾**：强调系统性、长期方法而非短期生产力提升

## 重要意义

本文代表了软件开发方法论的重大转变——从人类主导编程转向AI驱动的开发系统。它为组织向[[Agent-First Development]]转型提供了理论框架和实践指导。

## 标签
ai-development, harness-engineering, compound-engineering, agent-architecture, software-engineering, ai-agents, workflow-automation, knowledge-management, source-document

## Related
- [[Harness Engineering]]
- [[Compound Engineering]]
- [[Agent Harness]]
- [[OpenAI]]
- [[Anthropic]]
- [[Every]]
- [[Mitchell Hashimoto]]
- [[Ethan Mollick]]
- [[汉松]]
- [[Claude Code Agent Technical Analysis and Multi-Agent Architecture]]
- [[Agent Operating System]]
- [[AI Tool Chaining/Combination]]
- [[GStack: Role-Based AI Development Workflow for Claude Code]]
- [[Vibe Coding]]
- [[Single-Mode Problem]]