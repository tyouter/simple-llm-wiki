---
title: "Claude Code Skills系统"
type: "concept"
sources:
  - "raw/webpages/f599cc5e_Extend Claude with skills - Claude Code DocsExtend Claude with skills.md"
tags:
  - "claude-code"
  - "skills"
  - "extension-system"
  - "prompt-based"
confidence: "high"
created_at: "2026-04-20T12:00:00"
updated_at: "2026-04-23T00:42:26.842830"
related:
  - "Claude Code Skills官方文档"
  - "Agent Skills开放标准"
  - "Claude Code Hooks"
  - "Progressive Disclosure (Agent Skills)"
  - "Slash Commands Customization"
  - "CLAUDE.md Architecture"
  - "GStack"
  - "AI Agent构建指南：30分钟掌握90%核心知识"
  - "AI决策五步法"
  - "Anthropic黑客马拉松获胜者的Claude Code配置"
  - "AutoResearch Claude Code Skill实战"
  - "Claude Code Obsidian论文阅读自动化"
  - "Claude Code Superpowers插件详解"
  - "Claude Code完整概念指南：27个核心概念详解"
  - "15条高频实用的Claude Code技巧"
  - "Claude Code职场替身应用"
  - "Creative Tim UI：前端开发神器"
  - "用Skills把AI变成前端设计师"
  - "Everything-Claude-Code - 54K Star AI开发生态系统剖析"
  - "Visual Coding：从Vibe Coding进化"
  - "Claude Code revealjs-skill幻灯片生成"
  - "Gemini CLI搭配设计Skill实战"
  - "LTX Desktop：全球首款原生AI剪辑软件"
  - "Marketing Skills：Claude Code营销专家技能包"
  - "mcp2cli：CLI取代MCP的Token优化方案"
  - "Meta工程师Claude Code使用技巧"
  - "n8n自动化工作流：多平台内容同步"
  - "Obsidian-Deepseek插件轻Skill功能介绍"
  - "Obsidian与Gemini CLI工作流：ADHD患者的第二大脑"
  - "开源Agent Skills社区资源整理"
  - "OpenCode详细攻略"
  - "OpenSpace自我进化智能体"
  - "Product Manager Skills：让Claude秒变产品经理的Skill"
  - "project-analyzer逆向工程Skill介绍"
  - "Skills数量过多的管理策略"
  - "Stop Writing Bad CLAUDE.md Files - Claude Code配置最佳实践"
  - "Supermemory AI记忆系统"
  - "Trae Skills教程：AI编程变天了"
  - "从零入门深度学习AI路线图"
  - "停止在终端中使用Claude Code：管理目标而非会话"
  - "国产大模型横评：Coding Plan避坑指南"
  - "纳瓦尔Podcast：AI与未来工作——心智的摩托车"
  - "视频-闪客拆穿SkillMCPRAGAgentOpenClaw底层逻辑"
  - "视频-闪客揭秘Clawdbot背后干了什么"
  - "Agent Skill vs MCP 对比分析"
  - "Claude Code Skills推荐合集"
  - "OpenCLI Skill - 龙虾版分析"
  - "Skills的本质分析"
---

# Claude Code Skills系统

## 定义

Claude Code的扩展机制，通过创建SKILL.md文件添加自定义指令和能力，让Claude学习新的工作方法。

## 核心特点

- **Prompt-based**：给Claude详细playbook，让它用工具orchestrate工作
- **可spawn并行Agent**
- **可读文件、适配代码库**
- **遵循Agent Skills开放标准**

## Skills vs Commands

| 维度 | Skills | Commands |
|------|--------|----------|
| 文件位置 | .claude/skills/name/SKILL.md | .claude/commands/name.md |
| 支持文件 | 支持目录结构 | 单文件 |
| Frontmatter | 完整配置 | 基础配置 |
| Invocation控制 | 支持 | 不支持 |
| Subagent执行 | 支持 | 不支持 |

同名时Skills优先。

## 两类内容

### Reference内容

添加知识Claude应用到当前工作：
- 约定、模式、风格指南
- 领域知识
- 运行inline，与对话上下文并存

### Task内容

给Claude步骤指令：
- 部署、提交、代码生成
- 通常用/skill-name手动触发
- 添加`disable-model-invocation: true`阻止自动加载

## Related
- [[Claude Code Skills官方文档]]
- [[Agent]]
- [[Progressive Disclosure (Agent Skills)]]
- [[Slash Commands Customization]]
- [[CLAUDE.md Architecture]]
- [[GStack]]
- [[AI Agent构建指南：30分钟掌握90%核心知识]]
- [[AI决策五步法]]
- [[Anthropic黑客马拉松获胜者的Claude Code配置]]
- [[AutoResearch Claude Code Skill实战]]
- [[Claude Code Obsidian论文阅读自动化]]
- [[Claude Code Superpowers插件详解]]
- [[Claude Code完整概念指南：27个核心概念详解]]
- [[15条高频实用的Claude Code技巧]]
- [[Claude Code职场替身应用]]
- [[Creative Tim UI：前端开发神器]]
- [[用Skills把AI变成前端设计师]]
- [[Everything-Claude-Code - 54K Star AI开发生态系统剖析]]
- [[Visual Coding：从Vibe Coding进化]]
- [[Claude Code revealjs-skill幻灯片生成]]
- [[Gemini CLI搭配设计Skill实战]]
- [[LTX Desktop：全球首款原生AI剪辑软件]]
- [[Marketing Skills：Claude Code营销专家技能包]]
- [[mcp2cli：CLI取代MCP的Token优化方案]]
- [[Meta工程师Claude Code使用技巧]]
- [[n8n自动化工作流：多平台内容同步]]
- [[Obsidian-Deepseek插件轻Skill功能介绍]]
- [[Obsidian与Gemini CLI工作流：ADHD患者的第二大脑]]
- [[开源Agent Skills社区资源整理]]
- [[OpenCode详细攻略]]
- [[OpenSpace自我进化智能体]]
- [[Product Manager Skills：让Claude秒变产品经理的Skill]]
- [[project-analyzer逆向工程Skill介绍]]
- [[Skills数量过多的管理策略]]
- [[Stop Writing Bad CLAUDE.md Files - Claude Code配置最佳实践]]
- [[Supermemory AI记忆系统]]
- [[Trae Skills教程：AI编程变天了]]
- [[从零入门深度学习AI路线图]]
- [[停止在终端中使用Claude Code：管理目标而非会话]]
- [[国产大模型横评：Coding Plan避坑指南]]
- [[纳瓦尔Podcast：AI与未来工作——心智的摩托车]]
- [[视频-闪客拆穿SkillMCPRAGAgentOpenClaw底层逻辑]]
- [[视频-闪客揭秘Clawdbot背后干了什么]]
- [[Agent Skill vs MCP 对比分析]]
- [[Claude Code Skills推荐合集]]
- [[OpenCLI Skill - 龙虾版分析]]
- [[Skills的本质分析]]
- [[Claude Code Hooks]]