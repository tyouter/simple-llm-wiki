---
title: "Claude Code Skills官方文档"
type: "source"
sources:
  - "raw/webpages/f599cc5e_Extend Claude with skills - Claude Code DocsExtend Claude with skills.md"
tags:
  - "claude-code"
  - "skills"
  - "official-docs"
  - "agent-skills-standard"
confidence: "high"
created_at: "2026-04-20T12:00:00"
updated_at: "2026-04-20T12:00:00"
related:
  - "Claude Code Skills系统"
  - "Agent Skills开放标准"
---

# Claude Code Skills官方文档

## 概述

Claude Code Skills是扩展Claude能力的官方机制，通过创建SKILL.md文件来添加自定义指令和方法。

## 内置Skills

| Skill | 用途 |
|-------|------|
| /batch | 大规模并行修改，分解为5-30独立单元，每个spawn后台Agent |
| /claude-api | 加载Claude API参考材料（Python、TypeScript等） |
| /debug | 启用调试日志，分析当前会话问题 |
| /loop | 定时重复运行prompt |
| /simplify | 审查代码质量、效率问题并修复 |

## Skills存储位置

| 位置 | 路径 | 适用范围 |
|------|------|---------|
| 企业级 | 管理设置 | 组织内所有用户 |
| 个人级 | ~/.claude/skills/ | 用户所有项目 |
| 项目级 | .claude/skills/ | 当前项目 |
| 插件级 | <plugin>/skills/ | 插件启用时 |

优先级：企业 > 个人 > 项目

## Frontmatter配置

```yaml
---
name: my-skill
description: 描述技能用途
disable-model-invocation: true  # 阻止Claude自动加载
allowed-tools: Read Grep        # 工具白名单
model: sonnet                   # 指定模型
effort: high                    # 思考努力程度
context: fork                   # 在子代理中运行
---
```

## 字符替换变量

- `$ARGUMENTS`：传入的所有参数
- `$ARGUMENTS[N]`：按索引访问参数
- `$N`：简写，如$0、$1
- `${CLAUDE_SESSION_ID}`：当前会话ID
- `${CLAUDE_SKILL_DIR}`：技能目录路径

## 支持文件结构

```
my-skill/
├── SKILL.md       # 主指令（必需）
├── reference.md   # 详细参考文档
├── examples.md    # 使用示例
└── scripts/       # 执行脚本
```

## Agent Skills开放标准

Claude Code Skills遵循Agent Skills开放标准，跨多AI工具通用。Claude Code扩展了标准：
- Invocation控制
- Subagent执行
- 动态上下文注入

## Related
- [[Claude Code Skills系统]]
- [[Agent Skills开放标准]]
- [[Claude Code深度使用指南]]