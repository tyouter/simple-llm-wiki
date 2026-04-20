---
title: "skill-creator"
type: "entity"
sources:
  - "raw\articles\149db3c1_Skills的本质是什么Skills的本质是什么.md"
tags:
  - "tool"
  - "anthropic-official"
  - "github"
  - "cli"
  - "evaluation-framework"
confidence: "high"
created_at: "2026-04-17T22:06:46.780634"
updated_at: "2026-04-17T22:06:46.780634"
related:
  - "Anthropic"
  - "Skills (Anthropic Framework)"
  - "Skill Engineering Lifecycle"
  - "Anthropic Skills: Engineering Approach to Agent Capability Development"
---

# skill-creator

## Definition
An official template and command-line tool published by [[Anthropic]] on GitHub, designed to guide developers through the engineering process of creating, evaluating, and iterating on [[Skills (Anthropic Framework)|Skills]] for Claude.

## Purpose and Function
This tool operationalizes the theoretical [[Skill Engineering Lifecycle]]. Its main functions include:

- **Project Scaffolding:** Generating the standardized directory structure for a new Skill, centered on the `SKILL.md` file.
- **A/B Testing Framework:** Facilitating comparative testing between a Skill-in-development and a baseline (e.g., a standard prompt or a previous version).
- **Evaluation Viewer:** Providing a visual interface to review test results, making it easy to compare outputs and identify where the Skill succeeds or fails.
- **Assertion Testing:** Supporting the definition of quantitative assertions to measure Skill performance objectively.

## Role in the Skills Framework
The `skill-creator` is the primary practical tool for implementing the methodologies described in [[Anthropic Skills: Engineering Approach to Agent Capability Development]]. It enforces good practices like iterative testing and [[Description Trigger Optimization]].

## Source and Availability
- **Creator:** [[Anthropic]]
- **Platform:** GitHub (public repository)
- **Context:** Part of Anthropic's official documentation and resources for developing agent capabilities.

## Relation to Other Concepts
- **[[Skill Engineering Lifecycle]]:** This tool is the software implementation that guides users through each phase of the lifecycle.
- **[[Description Trigger Optimization]]:** Provides the testing harness necessary for this optimization process.
- **[[Progressive Disclosure Mechanism]]:** Helps create the structured directory that enables this mechanism.

## Tags
tool, anthropic-official, github, cli, evaluation-framework

## Related
[[Anthropic]], [[Skills (Anthropic Framework)]], [[Skill Engineering Lifecycle]], [[Anthropic Skills: Engineering Approach to Agent Capability Development]]

## Related
- [[Anthropic]]
- [[Skills (Anthropic Framework)]]
- [[Skill Engineering Lifecycle]]
- [[Anthropic Skills: Engineering Approach to Agent Capability Development]]