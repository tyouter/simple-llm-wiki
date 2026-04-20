---
title: "LoRA (Low-Rank Adaptation)"
type: "concept"
sources:
  - "wiki/sources/Anthropic对中国控股公司的限制.md"
tags:
  - "machine-learning"
  - "fine-tuning"
  - "parameter-efficient"
  - "model-optimization"
confidence: "high"
created_at: "2026-04-19T01:51:50.675970"
updated_at: "2026-04-20T12:00:00"
---

# LoRA (Low-Rank Adaptation)

低秩适配是一种参数高效的模型微调方法，通过添加低秩矩阵而非修改全部参数，大幅减少训练计算需求。

## 核心要点

- **参数效率**：只训练少量参数即可实现模型适配
- **低秩分解**：将权重更新分解为两个低秩矩阵
- **计算友好**：使消费级硬件能够微调大模型
- **与蒸馏结合**：常与知识蒸馏配合用于本地模型部署
- **快速迭代**：支持快速实验和模型能力迁移

## Related
- [[Knowledge Distillation Model Distillation]]
- [[Local Model Deployment]]
- [[Unsloth框架]]
- [[Anthropic对中国控股公司的限制]]