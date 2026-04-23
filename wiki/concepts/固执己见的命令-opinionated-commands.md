---
title: "固执己见的命令 (Opinionated Commands)"
type: "concept"
sources:
  - "raw/articles/093f7d65_gstackClaude工程团队.md"
tags:
  - "用户体验"
  - "最佳实践"
  - "设计哲学"
  - "约束性设计"
confidence: "high"
created_at: "2026-04-21T18:02:02.813622"
updated_at: "2026-04-23T00:42:20.639084"
related:
  - "技能包"
  - "gstack"
  - "车道限制"
  - "Brian Chesky模式"
  - "Garry Tan"
  - "Agent Skills Framework"
---

**固执己见的命令**指那些在[[技能包 (Skill Pack)]]中预定义的、内置了特定工作流、最佳实践和强约束条件的AI技能或斜杠命令。它们不提供无限的可配置性或灵活性，而是强制用户按照设计者预设的、被认为是最优或最高效可靠的方式来执行特定任务。

[[GStack]]的八个斜杠命令被明确描述为“固执己见的”。这意味着每个命令都封装了[[Garry Tan]]及其团队对特定工程角色应如何工作的强烈观点和偏好。例如，`/plan-ceo-review`强制进行[[Brian Chesky模式 (Brian Chesky Mode)]]的“10星体验”思考；`/plan-eng-review`则要求输出ASCII架构图，而不是任意的设计描述格式。

这种固执己见性有多重好处：首先，它极大地减少了开发者的决策疲劳，用户无需思考“如何让AI做好代码审查”，只需调用`/review`。其次，它确保了输出质量和格式的一致性，便于团队协作和知识传递。最后，它是一种最佳实践的推广机制，将资深工程师的经验固化到工具中。固执己见的命令是[[车道限制 (Lane Restriction)]]原则得以严格执行的技术实现，也是[[Agent Skills Framework]]具有实际约束力和价值的体现。

**反向链接说明**：此概念在 [[gstack：Claude工程团队 - 汇智网分析]] 中被用来描述[[GStack]]命令的特性，是[[技能包 (Skill Pack)]]设计哲学的核心。

## Related
- [[技能包 (Skill Pack)]]
- [[GStack]]
- [[车道限制 (Lane Restriction)]]
- [[Brian Chesky模式 (Brian Chesky Mode)]]
- [[Garry Tan]]
- [[Agent Skills Framework]]