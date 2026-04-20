---
title: "ASMR (Agentic Search and Memory Retrieval)"
type: "entity"
sources:
  - "raw\articles\58c1d7ba_如何看待Supermemory团队提出的超级记忆系统ASMR能解决AI的记忆问题吗如何看待Supermemory团队提出的超级记忆系统ASMR能解决AI.md"
tags:
  - "ai-memory"
  - "multi-agent-systems"
  - "retrieval-architecture"
  - "rag-alternative"
  - "experimental-system"
confidence: "high"
created_at: "2026-04-17T22:21:17.654329"
updated_at: "2026-04-17T22:21:17.654329"
related:
  - "Supermemory.ai"
  - "Agent-Based Active Retrieval"
  - "Multi-Agent Specialization & Orchestration"
  - "Supermemory's ASMR System: A Critical Look at AI Memory Breakthroughs"
  - "LongMemEval/LongMemEval_s"
---

# ASMR (Agentic Search and Memory Retrieval)

## Definition
ASMR is a pure agent-based memory architecture proposed and implemented by [[Supermemory.ai]]. It represents a radical departure from traditional Retrieval-Augmented Generation (RAG) systems by completely abandoning vector databases in favor of a coordinated fleet of parallel, specialized AI agents responsible for ingestion, retrieval, and aggregation of information.

## Core Architectural Principle
Instead of relying on passive similarity search, ASMR actively decomposes a memory query and tasks multiple smaller agents with solving parts of it concurrently. This embodies the paradigm of [[Agent-Based Active Retrieval]] and the practice of [[Multi-Agent Specialization & Orchestration]].

## How the ASMR System Worked (Based on Source Analysis)
1.  **Parallel Specialized Agents ("Observers"):** Different agents were designed for specific cognitive tasks, such as:
    *   **Fact Grabber:** Extract concrete facts.
    *   **Context Digger:** Find surrounding narrative or circumstantial information.
    *   **Timeline Reconstructor:** Piece together the temporal sequence of events.
2.  **Independent Search Agents:** Multiple instances or variants of agents would independently process the query and knowledge base.
3.  **Aggregation via Majority Voting:** An aggregator LLM (or "majority voter") would synthesize the outputs from the parallel agents, often using a [[Pass@k & Majority Voting for Benchmarking]] strategy to choose the best answer.

## Purpose & Achievements
*   **Benchmark Performance:** Achieved ~99% accuracy on the challenging [[LongMemEval/LongMemEval_s]] benchmark, which tests long-context understanding, timeline jumps, and handling of conflicting information.
*   **Proof-of-Concept:** Served as a tangible demonstration that agent-based systems could potentially solve memory problems intractable for vector-search-based RAG.
*   **Critical Provocation:** As detailed in [[Supermemory's ASMR System: A Critical Look at AI Memory Breakthroughs]], its primary purpose was revealed to be a "social experiment" highlighting the [[Benchmark vs. Engineering Reality Gap]], as the architecture was too slow and costly for practical deployment.

## Significance
ASMR is a landmark example in the critique of mainstream [[RAG (Retrieval-Augmented Generation)]] approaches. It forces a re-evaluation of retrieval, suggesting that the future of AI memory may lie in active, reasoning-based agent systems rather than passive similarity matching, even if current implementations face significant engineering hurdles.

## Tags
ai-memory, multi-agent-systems, retrieval-architecture, rag-alternative, experimental-system

## Related
- [[Supermemory.ai]]
- [[Agent-Based Active Retrieval]]
- [[Multi-Agent Specialization & Orchestration]]
- [[Supermemory's ASMR System: A Critical Look at AI Memory Breakthroughs]]
- [[LongMemEval/LongMemEval_s]]