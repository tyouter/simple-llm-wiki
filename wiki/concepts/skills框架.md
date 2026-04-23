---
title: "Skills框架"
type: "concept"
sources:
  - "raw/articles/12be559f_claude.md怎么写才能让Claude Code更高效claude.md怎么写才能让Claude Code更高效.md"
tags:
  - "能力管理"
  - "技能库"
  - "扩展框架"
  - "专业化"
confidence: "high"
created_at: "2026-04-21T14:13:50.861009"
updated_at: "2026-04-23T00:42:20.522482"
related:
  - "Claude Code"
  - "持久记忆体系"
  - "Subagent"
  - "自动记忆"
---

# Skills框架

## 定义
一种组织[[Claude Code]]自定义能力的方法论和目录结构，将技能按通用和专项分类存放于特定目录，便于管理和扩展。在[[Claude Code高效配置与开发实践指南]]中，这被视为对[[持久记忆体系]]的重要扩展。

## 目录结构建议
在`~/.claude/skills/`目录下创建分类子目录：
- **common/** - 通用技能，适用于多种项目类型
- **ai-model/** - AI模型相关技能，如微调、评估
- **frontend/** - 前端开发技能，如组件生成、状态管理
- **devops/** - 运维部署技能，如容器化、CI/CD配置

## 技能定义文件
每个技能对应一个Markdown文件（如`tuning-skill.md`、`deploy-skill.md`），包含：
- 技能描述和适用场景
- 执行步骤和最佳实践
- 输入输出规范
- 常见问题和解决方案

## 沉淀原则
"重复出现3次的流程应沉淀为Skill" - 这是技能库建设的关键经验法则。通过将重复性任务标准化，提高[[Claude Code]]在特定领域的专业性和一致性。

## 与持久记忆体系的关系
[[Skills框架]]扩展了[[持久记忆体系]]的静态规则层：
- **基础层**：[[CLAUDE.md]]提供项目级通用规则
- **扩展层**：Skills提供领域级专业能力
- **动态层**：自动记忆学习项目特定经验

## 实施价值
1. **专业化提升**：让[[Claude Code]]在特定领域（如AI模型微调、前端组件生成）表现更专业
2. **一致性保证**：标准化流程确保相同任务产出一致结果
3. **知识积累**：团队最佳实践得以保存和传承
4. **效率提升**：减少重复配置和解释时间

## 示例技能
- **AI模型微调**：`~/.claude/skills/ai-model/tuning-skill.md`，定义如何为LLaMA模型编写微调脚本
- **React组件生成**：`~/.claude/skills/frontend/react-component.md`，包含组件结构、Props类型、样式规范
- **Docker部署**：`~/.claude/skills/devops/docker-deploy.md`，描述多阶段构建、健康检查配置

## 相关概念
- [[Claude Code]] - 技能的使用者
- [[持久记忆体系]] - 技能框架扩展的基础系统
- [[Subagent]] - 可能实现特定技能的专门化智能体
- 自动记忆 - 与技能框架协同的动态学习系统

**backlinks_note**: 本概念在[[Claude Code高效配置与开发实践指南]]中作为[[持久记忆体系]]的扩展被介绍，用于构建可扩展的专业能力库。

## Related
- [[Claude Code]]
- [[持久记忆体系]]
- [[Subagent]]
- 自动记忆