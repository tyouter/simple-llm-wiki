---
title: "Claude Code深度使用指南"
type: "source"
sources:
  - "raw/articles/55258346_claude code使用感受如何claude code使用感受如何.md"
tags:
  - "claude-code"
  - "vibe-coding"
  - "claudemd"
  - "hooks"
  - "subagents"
  - "workflow"
confidence: "high"
created_at: "2026-04-20T12:00:00"
updated_at: "2026-04-23T00:42:21.289664"
related:
  - "CLAUDE.md配置"
  - "Claude Code Hooks"
  - "Claude Code子代理"
  - "Plan Mode"
  - "Claude Code Skills官方文档"
---

# Claude Code深度使用指南

## 核心认知

Claude Code不是聊天机器人，而是六层系统：

| 层 | 职责 |
|---|-----|
| CLAUDE.md/rules/memory | 长期上下文，告诉Claude"是什么" |
| Tools/MCP | 动作能力，告诉Claude"能做什么" |
| Skills | 按需加载的方法论，告诉Claude"怎么做" |
| Hooks | 强制执行某些行为 |
| Subagents | 隔离上下文的工作者 |
| Verifiers | 验证闭环 |

## CLAUDE.md最佳实践

### 核心原则

- **越短越好**：控制在200行以内，太长会降低遵循度
- **放"为什么"**：架构决策、历史教训、业务约束、风格偏好
- **不放"是什么"**：API文档、逐文件描述（Claude自己会读代码）

### 全局CLAUDE.md示例（4行）

```markdown
- commit信息使用conventional commits规范
- 修改前先解释计划，等我的确认
- 优先简单方案，不要过度工程
- 不要重构我没提到的文件
```

### 规则分层

- 全局（~/.claude/CLAUDE.md）：行为偏好
- 项目（./CLAUDE.md）：项目事实
- 路径规则（.claude/rules/）：按路径匹配的局部规范

## 子代理使用

### 三种代理模板

| 代理 | 能力 | 用途 |
|------|-----|------|
| explorer | 只读 | 快速代码库搜索 |
| planner | 只读 | 研究和分析 |
| executor | 全能力 | 复杂任务 |

### AI人格测试法

用6个子代理扮演不同用户角色，15分钟找到信任断点：
- 怀疑型资深工程师（关注安全、副作用）
- 安全审计员（关注密钥泄露、权限边界）
- 新接手维护者（关注文档清晰度）
- 重度CLI用户（关注命令一致性）
- 运维/SRE（关注可观测性）
- 文档优先新手（关注README完整性）

## 指令精准化

### 三要素

1. **目标**：明确要达成什么
2. **约束**：不改什么、不加什么
3. **上下文**：@引用加行号精准聚焦

### "不要"比"要"更重要

- "不要加新依赖"比列出10个允许的库更有效
- "只改这个函数"比"修改这个功能"更精准

## Plan Mode使用

### 进入方式

- `claude --permission-mode plan`
- Shift+Tab循环切换
- 自然语言："先别改代码，给我一个实施计划"

### 标准 workflow

```
Explore → Plan → Implement → Verify
```

复杂任务永远先进Plan Mode，改计划一句话，改已写好的代码要十倍时间。

## 上下文管理

### 五个策略

| 命令 | 用途 |
|------|-----|
| /clear | 全部清空，完全切换任务 |
| /compact [focus] | 压缩历史但保留关键点 |
| /context | 查看当前上下文使用率 |
| 子代理 | 单独模块用单独代理 |
| Compact Instructions | 告Claude压缩时保留什么 |

### HANDOFF.md方法

开新会话前，让Claude写一份进展报告：
- 试了什么、什么有效、什么没用
- 下一步该做什么
- 新会话只读这个文件就能接着做

## 权限配置

### settings.json示例

```json
{
  "permissions": {
    "deny": [
      "Bash(rm -rf*)",
      "Bash(*--force*)",
      "Edit(.env*)",
      "Edit(*.pem)"
    ],
    "ask": [
      "Bash(git push*)",
      "Bash(npm publish*)"
    ],
    "allow": [
      "Bash(npm run*)",
      "Bash(git commit*)",
      "Read(**)"
    ]
  }
}
```

优先级：deny > ask > allow

## Hooks系统

### 四种hook类型

| 类型 | 说明 |
|------|-----|
| command | 执行shell命令 |
| http | 发POST请求 |
| prompt | LLM调用判断 |
| agent | 生成子代理验证 |

### 实用场景

- 自动格式化：每次编辑后跑Prettier
- 保护关键文件：阻止修改生产配置
- 压缩后重新注入：重要指令不丢失

## 四条红线

1. **不懂的事别做**：生成你看不懂的代码是技术债
2. **没有版本控制别用**：没有Git就没有回滚
3. **别扔大任务**："重构整个系统"是灾难级提示
4. **别指望一次完美**：迭代才是正确方式

## Related
- [[Claude]]
- [[Claude Code Hooks]]
- [[Claude Code子代理]]
- [[Claude Code Skills官方文档]]
- [[Plan Mode工作流]]