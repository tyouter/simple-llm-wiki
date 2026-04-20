---
title: "Code Fence + Sandbox Iframe Architecture"
type: "concept"
sources:
  - "raw\articles\a1824936_你写过什么不错的开源项目你写过什么不错的开源项目.md"
tags:
  - "architecture"
  - "security"
  - "generative-ui"
  - "sandboxing"
  - "implementation"
confidence: "high"
created_at: "2026-04-18T23:00:54.014122"
updated_at: "2026-04-18T23:00:54.014122"
related:
  - "CodePilot"
  - "Generative UI"
  - "Streaming Rendering"
  - "歸藏"
  - "Local Data Sovereignty in Automation"
---

# Code Fence + Sandbox Iframe Architecture

## Definition
An alternative implementation approach for [[Generative UI]] systems that uses markdown code fences to contain generated code, which is then executed within a sandboxed iframe for preview and interaction. This architecture was developed by [[歸藏]] for the [[CodePilot]] project as an alternative to Claude's official `tool_use` mechanism.

## How It Works
1. **Code Generation**: The AI generates visualization code (typically JavaScript/HTML) within markdown code blocks
2. **Sandboxed Execution**: The code is extracted and executed within a securely sandboxed iframe
3. **Progressive Display**: As code is generated incrementally, the iframe content updates progressively, enabling [[Streaming Rendering]]
4. **Isolation**: The iframe provides security isolation from the main application

## Advantages Over tool_use Approach
According to the [[CodePilot]] developer:
- **Better Streaming Experience**: Allows preview during code generation rather than after completion
- **Flexibility**: Can handle any visualization library that works in browser context
- **Simplicity**: Avoids complex tool definition and calling mechanisms

## Security Considerations
- **Sandbox Attributes**: Uses iframe sandboxing to restrict capabilities
- **Content Security Policy**: Additional CSP headers to prevent malicious code execution
- **Input Sanitization**: Careful handling of AI-generated code before execution

## Implementation in [[CodePilot]]
The architecture enables [[CodePilot]] to support multiple AI models including [[Kimi K2.5]] and [[MiniMax M2.5]] for chart generation, with real-time [[Streaming Rendering]] as the code is produced.

## Related Concepts
- [[Generative UI]]
- [[Streaming Rendering]]
- [[Local Data Sovereignty in Automation]] (shares similar philosophy of local execution)

**Source**: Based on analysis of [[Zhihu Discussion: Open Source Projects for AI Visualization and Hardware Development]] and the [[CodePilot]] implementation

## Related
- [[CodePilot]]
- [[Generative UI]]
- [[Streaming Rendering]]
- [[歸藏]]
- [[Local Data Sovereignty in Automation]]