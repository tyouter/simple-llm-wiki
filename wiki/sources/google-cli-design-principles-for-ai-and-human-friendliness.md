---
title: "谷歌CLI设计原则"
type: "source"
sources:
  - "raw/articles/b5d1922b_谷歌提出CLI的7条设计原则AI和人类都友好的CLI长这样.md"
tags:
  - "cli-design"
  - "ai-interoperability"
  - "data-presentation-separation"
  - "developer-tools"
confidence: "high"
created_at: "2026-04-20T12:00:00"
updated_at: "2026-04-20T12:00:00"
related:
  - "CLI设计原则"
  - "数据与呈现分离"
---

# 谷歌CLI设计原则

## 核心内容

谷歌提出的CLI设计七大原则，目标是让CLI同时服务AI和人类。

### 核心哲学：数据与呈现分离

**解决方案**：把数据从呈现中剥离。
- AI需要原始、结构化数据（JSON）
- 人类需要可读、交互式格式（TUI）
- CLI内部逻辑是数据引擎，终端UI只是一个渲染客户端

```bash
# 人类看到交互式TUI
a2acli watch --task abc123
# AI拿到结构化NDJSON
a2acli watch --task abc123 --no-tui
```

### 七条设计原则

#### 1. 结构化可发现性
- --help按功能分组
- 标记入口点：(start here)
- 三个必填字段：Short、Long、Example
- 仓库根目录放AGENTS.md

#### 2. AI优先互操作性
- --json或--no-tui支持
- 自动检测受众：NO_COLOR和[APP]_NO_TUI环境变量
- 非交互式回退机制
- 保护上下文窗口：截断大段文本
- 预处理数据：最关键项目永远在顶部
- 无状态设计：用引用标识符保持CLI无状态

#### 3. 配置与上下文
- 遵循XDG规范：配置放~/.config/app/config.yaml
- 命名环境：--env切换配置

#### 4. 错误指导
- 上下文提示：Error + Hint
- 快速失败：执行前先验证配置
- 确定性退出码：0成功、1一般错误、2无效用法、3认证失败

#### 5. Flag一致性
- 标准化shorthands
- 位置参数用于必需实体，--flags用于可选修饰符
- 安全默认值：破坏性操作要求显式flag

#### 6. 视觉设计
- 语义颜色token：Accent、Command、Pass、Warn、Fail、Muted、ID
- 保留颜色给状态
- 支持明暗主题

#### 7. 版本与生命周期
- 支持--version
- 优雅处理中断：SIGINT时不损坏数据
- 追踪操作者：写操作记录Actor

### 关键洞察

> 2026年的CLI不为AI优化，等于不存在。Cursor、Claude、Copilot等AI正在接管开发工作流。你的CLI迟早被调用。AI解析不了输出，它就去找别的工具。

> 数据与呈现分离是CLI设计的终极形态。前后端分离、API与UI分离，我们见过无数次。但应用到CLI这个"古老"工具上，却是一种顿悟。

## Related
- [[CLI设计原则]]
- [[数据与呈现分离]]
- [[AI优先互操作性]]
