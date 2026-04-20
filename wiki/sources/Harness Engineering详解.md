---
title: "Harness Engineering详解"
type: "source"
sources:
  - "raw\articles\b99fad36_Harness Engineering的本质是什么Harness Engineering的本质是什么.md"
tags:
  - "harness-engineering"
  - "ai-agents"
  - "software-engineering"
  - "cybernetics"
  - "zhihu-discussion"
  - "production-systems"
confidence: "high"
created_at: "2026-04-19T15:33:03.081079"
updated_at: "2026-04-19T15:33:03.081079"
related:
  - "mCell"
  - "riba2534"
  - "OpenAI"
  - "DeepSeek"
  - "Harness Engineering"
  - "Context Engineering"
  - "Entropy Management"
  - "Agent Operating System"
---

# Harness Engineering详解：从Agent Loop到生产系统

## 来源摘要
这是一篇知乎讨论的详细总结，全面解释了[[Harness Engineering]]作为使AI Agent能够在生产环境中可靠执行任务的工程环境。讨论指出，Agent开发的真正挑战不在于模型智能，而在于创建稳定、受限的环境——配备适当的反馈循环、工具治理和安全系统。

## 关键贡献者
- **[[mCell]]**：主要回答的作者，memo code项目创建者，提供Harness Engineering实施的实践经验
- **[[riba2534]]**：字节跳动后端工程师，提供第二个回答，贡献行业视角的Harness Engineering采用分析

## 核心论点
讨论挑战了"模型能力是Agent开发主要瓶颈"的观念。相反，它强调环境设计——即Harness——往往对可靠的生产系统更为关键。

## 核心洞察

### 更新的Agent公式
引入公式：**Agent = Loop(Model + Harness)**，强调Agent由模型和工程环境共同定义，上下文和工具是Harness的组成部分。

### 实践实施
- 描述了[[OpenAI]]如何使用Harness Engineering原则进行3工程师、5个月、100万行代码的实验
- 提到使用较老模型如[[DeepSeek]]测试环境有效性
- 讨论了行业采用模式和实践约束

### 控制论联系
提出Harness Engineering代表控制论原则的第三次出现，继Watt离心调速器和Kubernetes之后。

## 与现有Wiki的关系
本文提供了详细的实践解释，补充了现有[[Harness Engineering]]wiki页面的定义。它解决了几个矛盾：
1. 挑战"纯AI代码生成配合人类监督"的强调，提出更细致的观点——人类设计环境和约束
2. 解决"构建重型Harness"（OpenAI方法）与"信任模型"（Anthropic方法）之间的张力
3. 将概念扩展到代码生成之外，涵盖生产中的一般Agent操作

## 相关概念
- [[Context Engineering]]作为Harness Engineering的子集
- [[Entropy Management]]用于维护Agent环境
- [[Agent Operating System]]用于协调多个专业化Agent
- [[Single-Mode Problem]]通过创建专业化环境来解决
- [[AI Tool Chaining/Combination]]通过工具治理系统实现

## 标签
harness-engineering, ai-agents, software-engineering, cybernetics, context-engineering, agent-architecture, production-systems, zhihu-discussion

## Related
- [[mCell]]
- [[riba2534]]
- [[OpenAI]]
- [[DeepSeek]]
- [[Harness Engineering]]
- [[Context Engineering]]
- [[Entropy Management]]
- [[Agent Operating System]]