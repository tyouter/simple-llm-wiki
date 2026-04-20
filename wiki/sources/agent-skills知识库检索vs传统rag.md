---
title: "Agent Skills知识库检索vs传统RAG"
type: source
sources:
  - "raw/videos/9c48ef85_Agent Skills 做知识库检索能比传统 RAG 效果更好吗.md"
tags:
  - Skills
  - RAG
  - 知识库
  - 知识检索
  - Agent
confidence: medium
created_at: "2026-04-20T21:00:00"
updated_at: "2026-04-20T21:00:00"
---

# Agent Skills知识库检索vs传统RAG

## 概述

探讨用Agent Skills做知识库检索是否能比传统Chunk+Embedding模式RAG效果更好。作者分享了对传统RAG的偏见和改进思路，借鉴Skill的渐进式披露策略，实现专用于知识检索的Skill。

## 核心要点

### 传统RAG的问题
- Chunk+Embedding模式是当下妥协方案
- 调教过程痛苦，效果不稳定
- Llama Index创始人认为固定Chunk+Embedding模式已死
- 如果Agent可以动态扩展文件上下文，数据块大小考虑就无意义

### 知识检索Skill设计目标
1. 在指定目录检索关心的问题
2. 跨多种文件格式联合查询（Markdown、PDF、Excel等）
3. 按关键词逐步缩小范围，精准打开少量文件
4. 结合上下文给出可读的成段回答
5. 支持复杂问题多轮查找

### 实战演示效果
- 金融数据检索：准确找到三一重工股东信息
- 电商数据查询：跨表关联查询（顾客表+订单表）
- 复杂问题处理：多步骤检索和总结

### 实现原理
- **定位领域**：分析问题，按目录索引缩小范围
- **定位文件**：使用grep等命令筛选相关文件
- **读取分析**：按不同文件类型使用不同策略
  - Markdown：直接定位匹配段落
  - PDF：编写脚本解析成文本
  - Excel：只读取相关行和列

### 设计原则
- **渐进式检索**：尽量少读但要准确，优先查找最可能有答案的文件
- **保持简单可控**：用户只需告诉知识库位置，其余自动完成

### 技巧要求
- 文件夹按领域划分
- 每个文件夹包含目录索引文件（data_structure.md）
- 嵌套领域逐层读取索引

### 相关资源
- GitHub：https://github.com/ConardLi/rag-skill/
- AI教程汇总：https://github.com/ConardLi/easy-learn-ai

## Related
- [[Agent Skills与MCP技术对比与企业应用]]
- [[Anthropic Skills工程方法]]
- [[Supermemory AI记忆系统]]
- [[知乎讨论-为什么AI Agent雷声大雨点小]]