---
title: "CLI设计原则（AI与人类友好）"
type: "concept"
sources:
  - "wiki/sources/google-cli-design-principles-for-ai-and-human-friendliness.md"
tags:
  - "cli"
  - "ai-interoperability"
  - "developer-tools"
confidence: "high"
created_at: "2026-04-20T12:00:00"
updated_at: "2026-04-20T12:00:00"
---

# CLI设计原则（AI与人类友好）

## 核心概念

CLI设计的核心哲学是数据与呈现分离，让同一个命令同时服务AI和人类。

### 双渲染器模式

```bash
# 人类看到交互式TUI
a2acli watch --task abc123
# AI拿到结构化NDJSON
a2acli watch --task abc123 --no-tui
```

### 七条设计原则

| 原则 | AI需求 | 人类需求 |
|------|--------|----------|
| 结构化可发现性 | AGENTS.md定义规则 | --help分组展示 |
| AI优先互操作性 | --json/NDJSON输出 | 交互式TUI |
| 配置与上下文 | 环境变量切换 | XDG规范配置 |
| 错误指导 | 确定性退出码 | Hint提示指路 |
| Flag一致性 | 可预测语法 | 直觉延伸 |
| 视觉设计 | 无颜色干扰 | 语义颜色token |
| 版本生命周期 | 版本追踪 | 优雅中断处理 |

### 关键机制

**自动检测受众**：
- NO_COLOR环境变量
- [APP]_NO_TUI环境变量
- stdout管道传输时跳过交互元素

**确定性退出码**：
- 0：成功
- 1：一般错误
- 2：无效用法
- 3：认证失败

### 核心洞察

> 2026年的CLI不为AI优化，等于不存在。

> 数据与呈现分离是CLI设计的终极形态。

## Related
- [[数据与呈现分离]]
- [[AGENTS.md]]
