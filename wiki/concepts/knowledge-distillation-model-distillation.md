---
title: "Knowledge Distillation (Model Distillation)"
type: "concept"
sources:
  - "wiki/sources/Anthropic对中国控股公司的限制.md"
tags:
  - "machine-learning"
  - "model-optimization"
  - "transfer-learning"
  - "local-deployment"
confidence: "high"
created_at: "2026-04-19T01:51:50.676970"
updated_at: "2026-04-20T12:00:00"
---

# Knowledge Distillation (Model Distillation)

知识蒸馏是将大型模型（教师模型）的能力迁移到小型模型（学生模型）的技术，常用于本地部署和资源受限场景。

## 核心要点

- **教师-学生架构**：大模型输出作为训练数据，教会小模型复杂能力
- **推理能力蒸馏**：将Claude Opus等模型的Chain-of-Thought输出用于训练开源模型
- **本地部署优势**：蒸馏后的模型可在消费级GPU（如RTX 3090/4090）上运行
- **LoRA适配**：结合Low-Rank Adaptation减少训练计算需求
- **社区实践**：Qwen3.5-27B-Claude-Opus-Distill等项目展示了蒸馏的实际应用

## Related
- [[LoRA Low-Rank Adaptation]]
- [[Local Model Deployment]]
- [[Chain-of-Thought Reasoning]]
- [[Anthropic对中国控股公司的限制]]
- [[Qwen]]