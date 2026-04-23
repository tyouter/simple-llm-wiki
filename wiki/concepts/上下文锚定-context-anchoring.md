---
title: "上下文锚定 (Context Anchoring)"
type: "concept"
sources:
  - "raw/articles/093f7d65_gstackClaude工程团队.md"
tags:
  - "认知科学"
  - "LLM局限性"
  - "提示工程"
  - "心理学"
confidence: "high"
created_at: "2026-04-21T18:02:02.812040"
updated_at: "2026-04-23T00:42:20.602565"
related:
  - "单一模糊模式问题"
  - "对抗性通过"
  - "基于角色的AI开发"
  - "Agent Memory Systems"
---

**上下文锚定**是AI交互中的一种认知现象或偏差，指大型语言模型（LLM）在长对话或多轮交互中，会过度依赖并固化在对话历史早期建立的信息、假设、决策或代码结构。这使得模型难以跳出已形成的思维框架，接受根本性的改变或进行彻底的批判性思考。

在AI编程的[[单一模糊模式问题 (Single Fuzzy Mode Problem)]]中，上下文锚定是一个核心的深层原因。当同一个AI对话从需求讨论自然过渡到代码实现时，模型已经将自己“锚定”在最初的需求描述和初步设计上。即使后续意识到有更好的架构或存在逻辑漏洞，它也会倾向于维护早期的决定，导致输出“在错误的方向上做得很好”。

[[基于角色的AI开发 (Role-Based AI Development)]]范式通过创建全新的、隔离的对话上下文来专门解决这个问题。例如，[[对抗性通过 (Adversarial Pass)]]（由独立的`/review`技能执行）之所以有效，正是因为它在一个没有实现历史的新会话中运行，完全打破了上下文锚定，从而能够以新鲜的视角发现缺陷。[[车道限制 (Lane Restriction)]]原则也通过禁止角色越界讨论，减少了无关上下文对当前任务的锚定影响。

**反向链接说明**：此概念在 [[gstack：Claude工程团队 - 汇智网分析]] 中被阐述为[[单一模糊模式问题 (Single Fuzzy Mode Problem)]]的成因之一，是[[对抗性通过 (Adversarial Pass)]]所要克服的关键障碍。

## Related
- [[单一模糊模式问题 (Single Fuzzy Mode Problem)]]
- [[对抗性通过 (Adversarial Pass)]]
- [[基于角色的AI开发 (Role-Based AI Development)]]
- [[Agent Memory Systems]]