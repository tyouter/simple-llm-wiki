---
title: "Claude Code Hooks"
type: "concept"
sources:
  - "raw/articles/55258346_claude code使用感受如何claude code使用感受如何.md"
tags:
  - "claude-code"
  - "hooks"
  - "automation"
  - "rule-enforcement"
confidence: "high"
created_at: "2026-04-20T12:00:00"
updated_at: "2026-04-23T00:42:20.165764"
related:
  - "Claude Code深度使用指南"
  - "CLAUDE.md配置"
  - "Claude Code Skills系统"
  - "Hooks for Deterministic Automation"
  - "CLAUDE.md Architecture"
  - "Claude Code完整概念指南：27个核心概念详解"
  - "Meta工程师Claude Code使用技巧"
  - "Stop Writing Bad CLAUDE.md Files - Claude Code配置最佳实践"
---

# Claude Code Hooks

## 定义

Claude Code的强制执行机制，在生命周期事件前后执行规则，把软规则变成硬约束。

## 核心区别

- **CLAUDE.md里的规则**：建议，AI有时会忽略
- **Hooks**：代码级强制，永远不会忘

## 四种hook类型

| 类型 | 说明 | 用途 |
|------|-----|------|
| command | 执行shell命令，从stdin读JSON | 自动化脚本 |
| http | 发POST请求到URL | 外部服务集成 |
| prompt | LLM调用判断yes/no | 智能决策 |
| agent | 生成子代理验证 | 复杂验证 |

## 三个实用场景

### 1. 自动格式化

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Edit|Write",
      "hooks": [{"type": "command", "command": "jq -r '.tool_input.file_path' | xargs npx prettier --write"}]
    }]
  }
}
```

每次编辑后自动运行Prettier。

### 2. 保护关键文件

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Edit|Write",
      "hooks": [{"type": "command", "command": ".claude/hooks/protect-files.sh"}]
    }]
  }
}
```

退出码0允许，退出码2阻止。PreToolUse可在工具调用前阻止。

### 3. 压缩后重新注入

```json
{
  "hooks": {
    "SessionStart": [{
      "matcher": "compact",
      "hooks": [{"type": "command", "command": "echo 'Use Bun, not npm. Run bun test before committing.'"}]
    }]
  }
}
```

长对话被压缩时，重要指令自动重新注入。

## 真正价值

把工程标准变成系统约束。人会忘规则，代码不会。

## Related
- [[Claude Code深度使用指南]]
- [[Claude Code Skills系统]]
- [[Hooks for Deterministic Automation]]
- [[CLAUDE.md Architecture]]
- [[Claude Code完整概念指南：27个核心概念详解]]
- [[Meta工程师Claude Code使用技巧]]
- [[Stop Writing Bad CLAUDE.md Files - Claude Code配置最佳实践]]
- [[Claude]]