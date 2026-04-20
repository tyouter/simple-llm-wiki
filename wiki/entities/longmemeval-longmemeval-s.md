---
title: "LongMemEval/LongMemEval_s"
type: "entity"
sources:
  - "raw\articles\58c1d7ba_如何看待Supermemory团队提出的超级记忆系统ASMR能解决AI的记忆问题吗如何看待Supermemory团队提出的超级记忆系统ASMR能解决AI.md"
tags:
  - "ai-benchmark"
  - "long-context"
  - "memory-evaluation"
  - "rag-testing"
confidence: "high"
created_at: "2026-04-17T22:21:17.655329"
updated_at: "2026-04-17T22:21:17.655329"
related:
  - "Supermemory's ASMR System: A Critical Look at AI Memory Breakthroughs"
  - "ASMR (Agentic Search and Memory Retrieval)"
  - "Benchmark vs. Engineering Reality Gap"
---

# LongMemEval/LongMemEval_s

## Definition
A benchmark test designed to rigorously evaluate AI systems' capabilities for long-term memory. It is considered one of the most challenging and comprehensive benchmarks for assessing how well an AI can understand, reason about, and retrieve information from extensive context.

## Key Characteristics of the Benchmark
1.  **Massive Context:** Involves processing and reasoning over approximately **115k tokens** of historical records or narrative text, pushing the limits of models' long-context windows.
2.  **Temporal Complexity:** Includes **timeline jumps**, requiring the system to track events and facts across different points in time and understand chronological sequences.
3.  **Logical Challenges:** Presents **conflicting or contradictory information** within the context, testing the system's ability to resolve discrepancies, assess reliability, or understand narrative evolution.
4.  **Comprehensive Questioning:** Queries are designed to probe not just fact retrieval, but also contextual understanding, causal reasoning, and synthesis across the entire document.

## Role in the ASMR Analysis
The [[ASMR (Agentic Search and Memory Retrieval)]] system developed by [[Supermemory.ai]] was evaluated on this benchmark, achieving a score of approximately **99% accuracy**. This exceptional result was central to the narrative discussed in [[Supermemory's ASMR System: A Critical Look at AI Memory Breakthroughs]].

## Significance as a Benchmark
*   **Rigor:** Its difficulty makes it a respected measure of true long-context memory performance, beyond simpler QA tasks.
*   **Revelatory Tool:** In the cited analysis, LongMemEval served as the stage for exposing the [[Benchmark vs. Engineering Reality Gap]]. The ASMR system's high score demonstrated benchmark optimization, while its impractical architecture highlighted what such optimization can sacrifice (latency, cost).
*   **Stress Test for Architectures:** It effectively discriminates between systems that merely store long text and those that can actively reason within it, thus validating the need for approaches like [[Agent-Based Active Retrieval]].

## Tags
ai-benchmark, long-context, memory-evaluation, rag-testing

## Related
- [[Supermemory's ASMR System: A Critical Look at AI Memory Breakthroughs]]
- [[ASMR (Agentic Search and Memory Retrieval)]]
- [[Benchmark vs. Engineering Reality Gap]]