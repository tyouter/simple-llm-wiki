---
title: "概率算法思维"
type: "concept"
sources:
  - "wiki/sources/zhihu-discussion-algorithms-that-inspire-awe-in-computer-science.md"
tags:
  - "algorithm"
  - "probability"
  - "computer-science"
confidence: "high"
created_at: "2026-04-20T12:00:00"
updated_at: "2026-04-20T12:00:00"
---

# 概率算法思维

## 核心概念

惊艳的算法往往不是在硬算，而是在"偷懒"——从确定性记录转向概率统计。

### 核心转变

**传统思维**：我要数人头，就得把每个人头都记下来

**概率思维**：我不记人头，我记人头出现的特征概率

### 典型概率算法

#### HyperLogLog
- 统计1亿基数仅需12KB
- 误差1%内
- 核心：伯努利试验（抛硬币连续正面次数）

#### Bloom Filter
- "宁可错杀，不可放过"
- 返回"可能存在"或"绝对不存在"
- 不漏判，但会误判

### 思维共性

| 算法 | "偷懒"方式 |
|------|------------|
| HyperLogLog | 不存全量数据，改玩概率 |
| Bloom Filter | 不追求100%准确，换取速度 |
| Word2Vec | 不搞复杂语法规则，改算向量距离 |
| 一致性哈希 | 不搞全局重排，改做局部调整 |

### 核心洞察

> 在海量数据面前，99%的精准度加上极致的资源节省，就是完美的工程解。

> 算法的本质是对问题维度的重构。高阶的算法是跳出当前逻辑维度，用概率、几何、物理的思维去降维打击。

## Related
- [[HyperLogLog算法]]
- [[Bloom Filter]]
- [[一致性哈希]]
