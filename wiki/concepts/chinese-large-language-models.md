---
title: "国产大模型"
type: "concept"
sources:
  - "raw/videos/2c940938_爆肝5小时实测国产大模型横评Coding Plan避坑指南.md"
tags:
  - "chinese-llm"
  - "glm"
  - "minimax"
  - "qwen"
  - "coding"
confidence: "high"
created_at: "2026-04-20T12:00:00"
updated_at: "2026-04-20T12:00:00"
---

# 国产大模型

## 定义

国产大模型指由中国科技公司开发的大语言模型，包括 GLM、MiniMax、Qwen、Deepseek 等。

## 主要模型

### GLM 系列

- 开发方：智谱 AI (Zhipu AI)
- 特点：开源版本支持百万 tokens
- 版本：GLM-5 pro 版本

### MiniMax 系列

- 开发方：MiniMax
- 特点：UI 效果和还原度高
- 版本：MiniMax M2.5

### Qwen 系列

- 开发方：阿里巴巴
- 特点：性价比适中
- 版本：Qwen 3.5-plus

### Deepseek 系列

- 开发方：Deepseek
- 特点：Code v3.2 支持百万 tokens
- 定位：代码专用模型

## Coding 能力对比

根据实测：

| 模型 | UI原型 | 开发速度 | Token消耗 | 成本 |
|------|--------|----------|-----------|------|
| MiniMax M2.5 | 最高 | 最快 | ~15% | 低 |
| Qwen 3.5-plus | 较好 | 中等 | 中等 | ~30元 |
| GLM-5 pro | 较差 | 较慢 | ~95% | 高 |

## 选型建议

1. **性价比优先**: MiniMax M2.5
2. **稳定优先**: Qwen 3.5-plus
3. **开源优先**: Deepseek Code
4. **谨慎使用**: GLM-5 (Token消耗异常)

## 2026年发展趋势

- 多模型竞争加剧
- Coding Plan 成为核心评测维度
- Token 消耗优化成为关键

## Related

- [[Coding-Plan]]
- [[模型选型]]
- [[GLM]]
- [[MiniMax]]
- [[Qwen]]
- [[Deepseek]]