# LLM Wiki Skill

个人知识库系统 - LLM自动编译原始文档为交叉链接的Wiki知识库。

## 触发条件

当用户提到以下关键词时自动激活：
- `/wiki` - 直接调用
- "知识库"、"wiki"、"ingest" - 隐式触发
- "处理文档"、"生成wiki页面" - 操作触发

**语言设置触发** (自然对话):
- "用中文生成wiki" / "中文模式" → `wiki config --language cn`
- "用英文生成wiki" / "英文模式" → `wiki config --language en`
- "保持原文语言" / "跟随原文" → `wiki config --language as_origin`

## 功能概览

| 命令 | 功能 | 示例 |
|------|------|------|
| `wiki init` | 初始化新wiki | `/wiki init` |
| `wiki ingest` | 处理源文件生成wiki | `/wiki ingest --all` |
| `wiki query` | 向知识库提问 | `/wiki query "什么是Agent?"` |
| `wiki search` | 关键词搜索 | `/wiki search claude` |
| `wiki lint` | 健康检查 | `/wiki lint` |
| `wiki stats` | 统计信息 | `/wiki stats` |
| `wiki list` | 列出内容 | `/wiki list pages` |
| `wiki config` | 查看/修改配置 | `/wiki config --language cn` |

## 使用指南

### 初始化Wiki

```
/wiki init
```
在当前目录创建wiki结构：
- `raw/` - 原始文档目录
- `wiki/` - 生成的wiki页面
- `.wikirc.yaml` - 配置文件

### 处理文档

```bash
# 处理所有待处理文件
/wiki ingest --all

# 处理单个文件
/wiki ingest raw/articles/example.md

# 从URL抓取并处理
/wiki ingest --url https://example.com/article

# 预览模式（不写入）
/wiki ingest --all --dry-run

# 并行处理（加速）
/wiki ingest --all --workers 4
```

### 查询知识库

```
/wiki query "Claude Code和Cursor有什么区别?"

# 保存答案为新wiki页面
/wiki query "什么是Harness Engineering?" --save
```

### 搜索与统计

```bash
# 关键词搜索
/wiki search "agent框架"

# 查看统计
/wiki stats

# 列出所有页面
/wiki list pages

# 列出孤儿页面（无引用）
/wiki list orphans
```

### 健康检查

```
/wiki lint
```
检测问题：
- 孤儿页面（无入站链接）
- 断链（指向不存在页面）
- 浅页面（内容过少）
- 矛盾声明

## 工作流程

### 标准流程

1. **初始化**: `wiki init` 创建结构
2. **配置API**: 编辑 `.wikirc.yaml` 设置LLM
3. **添加源文件**: 将文档放入 `raw/`
4. **处理**: `wiki ingest --all` 生成wiki
5. **查询**: `wiki query "问题"` 使用知识库

### 持续维护

```bash
# 每周运行
wiki ingest --all    # 处理新文件
wiki lint            # 检查健康
wiki stats           # 查看增长
```

## 输出格式

每个源文件处理后生成：
- **1个Source页面** - 文档摘要
- **N个Concept页面** - 关键概念定义
- **M个Entity页面** - 人物/组织/产品

页面结构：
```markdown
---
title: "页面标题"
type: concept | entity | source
sources: ["raw/path/to/source.md"]
tags: ["tag1", "tag2"]
confidence: high | medium | low
---

# 内容
...
## Related
- [[其他页面]]
```

## 安装要求

```bash
pip install llm-wiki
```

依赖：
- Python 3.11+
- click, litellm, rich, pyyaml
- rank-bm25 (搜索)
- 可选: lancedb, sentence-transformers (向量搜索)

## 配置

`.wikirc.yaml`:
```yaml
language: as_origin  # Options: cn (Chinese), en (English), as_origin (follow source)
llm:
  apiKey: 'your-api-key'
  baseUrl: https://api.deepseek.com/v1
  model: deepseek-chat
  temperature: 0.3
  max_tokens: 8192
```

支持provider: `openai`, `anthropic`, `deepseek`, `gemini` 等。

### Language Mode

| Setting | Description |
|---------|-------------|
| `as_origin` | Default - follow source document language |
| `cn` | Force all wiki pages in Chinese |
| `en` | Force all wiki pages in English |

## 示例对话

用户: "帮我处理一下raw目录下的所有新文章"
→ 运行 `wiki ingest --all`

用户: "这个wiki里有什么关于Agent的内容?"
→ 运行 `wiki search agent` 并展示结果

用户: "知识库健康吗？有没有问题?"
→ 运行 `wiki lint` 报告问题

用户: "wiki现在有多少页面?"
→ 运行 `wiki stats` 展示统计

用户: "用中文生成wiki"
→ 运行 `wiki config --language cn`

用户: "切换到英文模式"
→ 运行 `wiki config --language en`

用户: "保持原文语言"
→ 运行 `wiki config --language as_origin`

用户: "看看当前配置"
→ 运行 `wiki config --show`

## 注意事项

- 处理大量文件时使用 `--workers` 并行加速
- `--dry-run` 可预览不写入，适合测试
- `query --save` 会创建新answer页面，避免重复查询
- 定期运行 `lint` 保持wiki健康