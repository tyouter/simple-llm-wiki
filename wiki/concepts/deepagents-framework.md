---
title: "DeepAgents框架"
type: "concept"
sources:
  - "raw/articles/53771cfc_最好用的Agent框架是什么最好用的Agent框架是什么.md"
tags:
  - "agent-framework"
  - "langchain"
  - "planning"
  - "subagent"
confidence: "high"
created_at: "2026-04-20T12:00:00"
updated_at: "2026-04-20T12:00:00"
related:
  - "LangChain"
  - "LangGraph"
  - "AI Agent框架对比"
---

# DeepAgents框架

## 定义

LangChain团队推出的深度代理框架，基于Claude Code、Deep Research等深度代理实践总结，解决传统"循环调用工具"式代理的规划能力不足问题。

## 解决的核心痛点

传统代理的三大困境：
1. **缺少全局规划**：只会根据最新提示执行局部操作
2. **上下文不稳定**：长步骤任务中重要信息容易遗失
3. **缺乏协作能力**：单一代理处理所有细节，难以管理

## 四大核心能力

### 1. 规划：TodoListMiddleware

- 让代理在执行复杂任务前进行规划
- 提供`write_todos`工具，输出待办列表
- 随执行动态更新计划

### 2. 上下文管理：FilesystemMiddleware

- 通过文件系统"外化"上下文
- 工具集合：ls、read_file、write_file、edit_file、glob、grep
- 避免信息在长对话中流失

### 3. 协作：SubAgentMiddleware

- 主代理（Supervisor）负责整体调度
- 子代理（Sub Agent）具备独立提示和工具
- 通过`task`工具将任务转交给子代理

### 4. 长期记忆：LangGraph Store

- 在多次会话间保留关键信息
- 支持长期项目或持续服务场景
- 可自定义读写逻辑

## 工作流程

```
收到任务 → write_todos生成计划 → 逐步执行
         ↑                    ↓
         └─── 更新计划 ←─── 完成步骤
```

## 使用方式

```python
from deepagents import create_deep_agent

agent = create_deep_agent(
    tools=[internet_search],
    system_prompt=research_instructions,
)

result = agent.invoke({
    "messages": [{"role": "user", "content": "What is LangGraph?"}]
})
```

## Related
- [[LangChain]]
- [[LangGraph]]
- [[AI Agent框架对比]]