---
title: "Spaced Repetition via Error Tracking"
type: "concept"
sources:
  - "raw\articles\2a9adff3_Sylearn 的想法 Github项目推荐TypeWords打字式背单词 TypeWords 是一个开源的网页端英语学习工具主打用敲键盘 -.md"
tags:
  - "spaced-repetition"
  - "adaptive-learning"
  - "error-analysis"
  - "learning-systems"
  - "educational-technology"
confidence: "high"
created_at: "2026-04-17T21:49:07.820654"
updated_at: "2026-04-17T21:49:07.820654"
related:
  - "TypeWords: Open-Source Typing-Based Vocabulary Learning Tool"
  - "Typing-Based Language Learning"
  - "Open-Source Educational Tools"
  - "GStack: Role-Based AI Development Workflow for Claude Code"
---

# Spaced Repetition via Error Tracking

## Definition
A learning system that adjusts review schedules based on user error patterns during practice exercises. Unlike traditional spaced repetition systems (like Anki's SM-2 algorithm) that use binary "remembered/forgotten" judgments, this approach uses detailed error data to optimize review timing.

## How It Works
1. **Error Pattern Analysis**: Tracks not just whether an item was incorrect, but the type and frequency of errors
2. **Dynamic Scheduling**: Adjusts review intervals based on error severity and consistency
3. **Context-Aware Review**: Considers when and how errors occur during practice sessions
4. **Progressive Difficulty**: Gradually increases challenge as mastery improves

## Implementation in TypeWords
In [[TypeWords: Open-Source Typing-Based Vocabulary Learning Tool]], this system:
- Tracks typing accuracy for each vocabulary item
- Adjusts future appearance frequency based on error rates
- Prioritizes difficult words while reducing review of mastered items
- Provides statistical feedback to users about their error patterns

## Advantages Over Binary SRS
- **More Granular**: Uses continuous error data rather than binary success/failure
- **Adaptive to Learning Style**: Adjusts to individual error patterns
- **Early Intervention**: Identifies problematic items before complete forgetting occurs
- **Motivational Feedback**: Shows progress through decreasing error rates

## Applications Beyond Language Learning
- **Programming Education**: Could track syntax errors in coding exercises
- **Medical Training**: Monitoring diagnostic error patterns
- **Music Education**: Tracking performance mistakes in practice sessions

## Related Concepts
- [[Typing-Based Language Learning]]: Often incorporates error-tracking spaced repetition
- [[Open-Source Educational Tools]]: Many implement variations of this approach
- [[GStack: Role-Based AI Development Workflow for Claude Code]]: Represents another systematic, data-driven workflow approach

## Related
- [[TypeWords: Open-Source Typing-Based Vocabulary Learning Tool]]
- [[Typing-Based Language Learning]]
- [[Open-Source Educational Tools]]
- [[GStack: Role-Based AI Development Workflow for Claude Code]]