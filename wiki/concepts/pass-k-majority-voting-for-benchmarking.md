---
title: "Pass@k & Majority Voting for Benchmarking"
type: "concept"
sources:
  - "raw/articles/58c1d7ba_如何看待Supermemory团队提出的超级记忆系统ASMR能解决AI的记忆问题吗如何看待Supermemory团队提出的超级记忆系统ASMR能解决AI.md"
tags:
  - "benchmarking"
  - "evaluation-metrics"
  - "llm-inference"
  - "ai-optimization"
  - "stochastic-methods"
confidence: "high"
created_at: "2026-04-17T22:21:17.652329"
updated_at: "2026-04-17T22:21:17.652329"
related:
  - "Benchmark vs. Engineering Reality Gap"
  - "Supermemory's ASMR System: A Critical Look at AI Memory Breakthroughs"
  - "Multi-Agent Specialization & Orchestration"
---

# Pass@k & Majority Voting for Benchmarking

## Definition
Evaluation techniques used to measure and often improve the reported performance of AI systems (especially LLM-based agents) on benchmarks. While valid as statistical measures, they can inflate scores compared to what a single, deterministic query would achieve, highlighting a tension with production feasibility.

## 1. Pass@k

### What it is
A metric where, for a given task, the system is allowed to generate `k` independent candidate solutions or answers. If **any one** of the `k` candidates is correct, the task is counted as a "pass."

### How it works
1.  The system (or multiple variants of an agent) is run `k` times on the same problem.
2.  This generates `k` potentially different outputs.
3.  If at least one output is correct, the system gets credit for solving the task.

### Implications
*   **Inflates Scores:** Dramatically increases reported accuracy, especially for tasks where the model has a moderate single-shot success rate. It rewards stochasticity and multiple attempts.
*   **Example:** If a single agent has a 40% chance of being correct, using Pass@5 (5 attempts) raises the probability of at least one success to ~92%.
*   **Production Reality:** Running `k` times in production is `k` times more expensive and slower, making high Pass@k scores misleading for latency/cost-sensitive applications.

## 2. Majority Voting (Self-Consistency)

### What it is
A technique where `k` independent candidate answers are generated, and the final answer is selected as the one that appears most frequently among them. A separate LLM (an "aggregator" or "voter") may be used to judge and select the best answer if no clear majority exists.

### How it works
1.  Generate `k` candidate answers (e.g., by sampling different reasoning chains).
2.  Tally the frequency of each distinct answer.
3.  Choose the most frequent answer as the final output.

### Implications
*   **Improves Accuracy:** Often yields higher accuracy than any single sample by averaging out individual errors.
*   **Increases Cost & Latency:** Requires `k` model calls plus an aggregation step, multiplying inference cost and time.
*   **Benchmark vs. Reality:** A system using Majority Voting may top a benchmark leaderboard but be economically non-viable for a product, exemplifying the [[Benchmark vs. Engineering Reality Gap]].

## Context from Source
In the analysis of [[Supermemory's ASMR System: A Critical Look at AI Memory Breakthroughs]], these techniques were implicitly or explicitly part of how the ASMR system achieved its ~99% score on [[LongMemEval/LongMemEval_s]]. The use of multiple parallel "search agents" and a "majority voter" aggregator is a direct application of these methods. The source critiques this as part of a benchmark-optimized, rather than engineering-optimized, approach.

## Relation to Other Concepts
*   A key method that can widen the [[Benchmark vs. Engineering Reality Gap]].
*   Often implemented within a [[Multi-Agent Specialization & Orchestration]] framework (e.g., multiple independent agents voting).
*   Contrasts with the need for deterministic, low-latency performance in production systems.

## Tags
benchmarking, evaluation-metrics, llm-inference, ai-optimization, stochastic-methods

## Related
- [[Benchmark vs. Engineering Reality Gap]]
- [[Supermemory's ASMR System: A Critical Look at AI Memory Breakthroughs]]
- [[Multi-Agent Specialization & Orchestration]]