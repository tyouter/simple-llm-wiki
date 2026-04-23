---
title: "从会用AI到构建AI协作框架"
type: source
sources:
  - "raw/videos/92471d0f_从会用AI到构建AI协作框架.md"
tags:
  - Skills
  - AI协作
  - 结构化思维
  - PPT制作
  - 工作流
confidence: medium
created_at: "2026-04-20T21:00:00"
updated_at: "2026-04-23T00:42:39.046186"
---

# 从会用AI到构建AI协作框架

## 概述

讲解如何将AI做PPT的三件套（NotebookLM → Gemini → Gamma）封装成一个Skill并发布到GitHub。强调这不是工具堆叠，而是结构拆解。Skill的本质是一个流程守护系统，而非替代工具。

## 核心要点

### Skill封装的三要素
1. **清晰的工作链**：NotebookLM → Gemini → Gamma，固定工具固定顺序
2. **可复用的操作流程**：事实梳理 → 结构判断 → 表达升级 → 结果呈现
3. **明确的使用场景和输出格式**：适合职场汇报场景

### Skill与复制Prompt的区别
- **内嵌流程**：不需要手动复制粘贴模板，避免漏掉步骤或用错版本
- **结构强制**：预设结构逻辑，不跑偏（如事实梳理、结构判断、取舍、表达升级）
- **场景化调用**：知道输入是什么、流程是什么、输出格式是什么
- **体验稳定**：模块化调用，每次执行逻辑一致，结果更可控

### 核心价值定位
- 不是自动化，而是结构化的一致性
- 是一个流程守护系统
- 是调度不同AI进行协作的框架
- 帮你用对工具，而非替代工具

### 安装使用
- GitHub搜索：wilingna / ai-ppt-toolkit
- 安装后只需一句话触发完整流程
- Claude自动调用Skill按流程执行

### 未来展望
- 如果Claude可以直接调用Gemini或NotebookLM API
- 可以升级成自动化版本
- 目前是流程强化版

## Related
- [[Anthropic Skills工程方法]]
- [[Agent Skills与MCP技术对比与企业应用]]
- [[Claude Code工作流技术与架构分析]]
- [[在中国生活的身份认同反思]]
- [[Skill]]