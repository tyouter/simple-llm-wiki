#!/usr/bin/env python3
"""
Agent Deep Scan - Comprehensive knowledge base deep scan and improvement.
Uses rule-based extraction with domain knowledge to process source files
and generate high-quality wiki pages with bidirectional links.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT_DIR = Path(__file__).parent
WIKI_DIR = ROOT_DIR / "wiki"
RAW_DIR = ROOT_DIR / "raw"
CACHE_FILE = ROOT_DIR / ".ingest_cache.json"
CONCEPTS_DIR = WIKI_DIR / "concepts"
ENTITIES_DIR = WIKI_DIR / "entities"
SOURCES_DIR = WIKI_DIR / "sources"
ANSWERS_DIR = WIKI_DIR / "answers"

DOMAIN_CONCEPTS = {
    "agent": "AI Agent - 能够自主执行任务的AI系统，通过感知环境、做出决策和采取行动来完成任务",
    "ai agent": "AI Agent - 能够自主感知、决策和执行任务的智能体系统",
    "harness engineering": "Harness Engineering - Agent运行时的工程环境总和，包括任务表达、上下文组织、工具治理、状态管理、反馈回路和错误处理",
    "skill": "Agent Skill - 可复用的Agent能力包，通过SKILL.md定义指令和元数据",
    "skills": "Agent Skills - 标准化的Agent能力封装体系，支持渐进式披露和版本控制",
    "mcp": "Model Context Protocol - 模型上下文协议，标准化的工具连接和资源访问协议",
    "model context protocol": "Model Context Protocol - 连接AI模型与外部工具和资源的标准协议",
    "rag": "RAG (Retrieval-Augmented Generation) - 检索增强生成，结合外部知识检索来提升LLM回答质量",
    "prompt engineering": "Prompt Engineering - 提示词工程，设计和优化LLM输入以获得期望输出的技术",
    "context engineering": "Context Engineering - 上下文工程，系统性地管理LLM的上下文窗口和信息加载",
    "context window": "Context Window - 上下文窗口，LLM一次能处理的最大token数量",
    "progressive disclosure": "Progressive Disclosure - 渐进式披露，按需加载信息的架构模式",
    "vibe coding": "Vibe Coding - 氛围编程，通过自然语言描述让AI生成代码的编程方式",
    "spec coding": "Spec Coding - 规格编程，基于精确规格说明让AI生成代码的结构化编程方式",
    "chain of thought": "Chain of Thought (CoT) - 思维链，让LLM逐步推理的提示技术",
    "token optimization": "Token Optimization - Token优化，减少LLM调用中的token消耗",
    "agentic loop": "Agentic Loop - 智能体循环，Agent感知-决策-行动的迭代执行模式",
    "tool calling": "Tool Calling - 工具调用，LLM调用外部工具和API的能力",
    "multi-agent": "Multi-Agent - 多智能体，多个Agent协作完成复杂任务的架构",
    "subagent": "Subagent - 子代理，主Agent派生的执行特定子任务的代理",
    "reinforcement learning": "Reinforcement Learning - 强化学习，通过奖励信号优化策略的机器学习方法",
    "fine-tuning": "Fine-Tuning - 微调，在预训练模型基础上用特定数据进一步训练",
    "distillation": "Distillation - 蒸馏，将大模型知识转移到小模型的技术",
    "embedding": "Embedding - 嵌入，将文本转换为向量表示的技术",
    "vector search": "Vector Search - 向量搜索，基于语义相似度的信息检索方法",
    "semantic search": "Semantic Search - 语义搜索，理解查询语义的搜索技术",
    "bm25": "BM25 - 基于词频和文档频率的概率检索算法",
    "lora": "LoRA (Low-Rank Adaptation) - 低秩适应，参数高效的微调方法",
    "claude code": "Claude Code - Anthropic推出的AI编程助手，深度集成开发环境",
    "claude.md": "CLAUDE.md - Claude Code的配置文件，定义项目规则和偏好",
    "skill-creator": "Skill-Creator - Anthropic官方的Skill创建工具",
    "obsidian": "Obsidian - 基于Markdown的个人知识管理工具，支持双向链接",
    "n8n": "N8N - 开源的工作流自动化平台",
    "openclaw": "OpenClaw - 开源的AI Agent框架，支持多模型和多工具集成",
    "cursor": "Cursor - AI驱动的代码编辑器",
    "copilot": "GitHub Copilot - GitHub的AI编程助手",
    "deepseek": "DeepSeek - 中国的AI大模型公司及其模型",
    "gemini": "Gemini - Google的AI大模型",
    "figma": "Figma - 协作式UI设计工具",
    "playwright": "Playwright - 微软开源的浏览器自动化测试框架",
    "selenium": "Selenium - 浏览器自动化测试工具",
    "scraping": "Web Scraping - 网页数据抓取技术",
    "web scraping": "Web Scraping - 从网页自动提取数据的技术",
    "cli": "CLI (Command Line Interface) - 命令行界面",
    "api": "API (Application Programming Interface) - 应用编程接口",
    "sop": "SOP (Standard Operating Procedure) - 标准操作流程",
    "prd": "PRD (Product Requirements Document) - 产品需求文档",
    "a/b test": "A/B Testing - 对照实验，比较两个版本的效果差异",
    "baseline": "Baseline - 基线，用于对比的参考标准",
    "bidirectional link": "Bidirectional Link - 双向链接，页面A链接到B时B也链接回A",
    "wikilink": "Wikilink - 维基链接，使用[[PageTitle]]格式的内部链接",
    "frontmatter": "Frontmatter - Markdown文件头部的YAML元数据区域",
    "markdown": "Markdown - 轻量级标记语言",
    "yaml": "YAML - 数据序列化格式，常用于配置文件",
    "git": "Git - 分布式版本控制系统",
    "docker": "Docker - 容器化平台",
    "knowledge base": "Knowledge Base - 知识库，结构化的知识存储系统",
    "personal knowledge management": "Personal Knowledge Management - 个人知识管理",
    "zettelkasten": "Zettelkasten - 卡片盒笔记法，强调原子化和链接的知识管理方法",
    "second brain": "Second Brain - 第二大脑，数字化个人知识管理系统",
    "strategic planning": "Strategic Planning - 战略规划，组织长期发展方向和路径的制定",
    "balanced scorecard": "Balanced Scorecard - 平衡计分卡，从多维度衡量组织绩效的管理工具",
    "competitive advantage": "Competitive Advantage - 竞争优势，组织相对于竞争对手的优越地位",
    "swot": "SWOT Analysis - 态势分析法，评估优势、劣势、机会和威胁",
    "design pattern": "Design Pattern - 设计模式，软件设计中反复出现的问题解决方案",
    "microservice": "Microservice - 微服务，将应用拆分为小型独立服务的架构",
    "devops": "DevOps - 开发运维一体化",
    "ci/cd": "CI/CD - 持续集成/持续部署",
    "tdd": "TDD (Test-Driven Development) - 测试驱动开发",
    "code review": "Code Review - 代码审查",
    "technical debt": "Technical Debt - 技术债务",
    "refactoring": "Refactoring - 重构，改善代码结构而不改变功能",
    "mental model": "Mental Model - 心智模型，理解和解释世界的内在框架",
    "cognitive bias": "Cognitive Bias - 认知偏差，系统性偏离理性的思维模式",
    "decision making": "Decision Making - 决策制定",
    "systems thinking": "Systems Thinking - 系统思维，从整体和关联角度理解复杂系统",
    "first principles": "First Principles - 第一性原理，从基本假设出发推理的思维方式",
    "entropy": "Entropy - 熵，系统无序度的度量",
    "cybernetics": "Cybernetics - 控制论，研究系统控制和通信的理论",
    "feedback loop": "Feedback Loop - 反馈回路，系统输出影响输入的循环机制",
    "complexity": "Complexity - 复杂性，系统难以理解和预测的程度",
    "emergence": "Emergence - 涌现，系统整体表现出部分不具备的特性",
    "paradigm shift": "Paradigm Shift - 范式转变，根本性的思维模式变化",
    "commoditization": "Commoditization - 商品化，产品或服务从差异化变为标准化的过程",
    "moat": "Moat - 护城河，企业抵御竞争的持久优势",
    "network effect": "Network Effect - 网络效应，用户越多价值越大的现象",
    "economies of scale": "Economies of Scale - 规模经济",
    "product-market fit": "Product-Market Fit - 产品市场契合",
    "user persona": "User Persona - 用户画像，目标用户的典型特征描述",
    "scenario analysis": "Scenario Analysis - 场景分析，评估不同情境下的可能结果",
    "progressive disclosure mechanism": "渐进式披露机制 - 按需加载信息的架构模式，减少token消耗",
    "context pollution": "Context Pollution - 上下文污染，无关信息干扰LLM判断",
    "extended thinking": "Extended Thinking - 扩展思考，LLM的深度推理模式",
    "self-evolving": "Self-Evolving - 自我进化，系统能自主改进和优化",
    "auto memory": "Auto Memory - 自动记忆，AI系统自动存储和检索交互历史",
    "error memory": "Error Memory - 错误记忆，从失败经验中学习改进的机制",
    "plan mode": "Plan Mode - 计划模式，先规划再执行的AI工作模式",
    "permission mode": "Permission Mode - 权限模式，控制AI工具访问权限的安全机制",
    "hooks": "Hooks - 钩子，在特定事件触发时自动执行的回调机制",
    "worktree": "Git Worktree - Git工作树，允许同时检出多个分支",
    "ui/ux": "UI/UX - 用户界面/用户体验设计",
    "low-code": "Low-Code - 低代码，通过可视化工具减少编程工作量的开发方式",
    "no-code": "No-Code - 无代码，无需编程即可构建应用的方式",
    "generative ui": "Generative UI - 生成式UI，AI自动生成用户界面",
    "design system": "Design System - 设计系统，统一的设计规范和组件库",
    "tailwind": "Tailwind CSS - 实用优先的CSS框架",
    "slidev": "Slidev - 基于Markdown的演示文稿工具",
    "bmad-method": "BMAD Method - 一人公司开源方法论，内置项目经理的AI辅助开发方法",
    "deerflow": "DeerFlow - 字节跳动开源的多智能体深度研究框架",
    "supermemory": "Supermemory - AI记忆系统，让AI拥有持久记忆能力",
    "asmr": "ASMR (Agentic Search and Memory Retrieval) - 智能体搜索与记忆检索系统",
    "mem0": "Mem0 - 开源AI记忆框架",
    "litmaps": "Litmaps - 学术论文可视化工具，发现论文间的引用关系",
    "mineru": "MinerU - 解析复杂PDF的开源项目",
    "scrapling": "Scrapling - 自适应网页爬虫工具",
    "firecrawl": "Firecrawl - 网页内容提取API服务",
    "agent-reach": "Agent-Reach - AI Agent全网感知CLI工具",
    "opencode": "OpenCode - 开源版Claude Code，支持免费模型",
    "oh-my-claudecode": "Oh My ClaudeCode - Claude Code增强工具集",
    "open pencil": "Open Pencil - AI原生设计编辑器",
    "google stitch": "Google Stitch - Google的AI设计平台",
    "mcp2cli": "MCP2CLI - 将MCP工具转为CLI命令以节省token",
    "autoresearch": "AutoResearch - Claude Code自动迭代优化Skill",
    "gitnexus": "GitNexus - 代码知识图谱工具",
    "mirofish": "MiroFish - 群体智能预测引擎",
    "typewords": "TypeWords - 打字式背单词开源工具",
    "bilibili-cli": "Bilibili CLI - B站命令行客户端",
    "subbatch": "SubBatch - B站字幕批量处理插件",
    "dragger": "Obsidian Dragger - Obsidian文本块拖拽插件",
    "humanize": "Humanize - Obsidian AI辅助插件",
    "superpowers": "Claude Code Superpowers插件",
    "claudekit": "ClaudeKit - 前端设计Skill演示",
    "dataview": "Obsidian Dataview - Obsidian数据查询插件",
    "advanced slides": "Advanced Slides - Obsidian演示文稿插件",
    "bridge": "Obsidian Bridge - Obsidian文件桥接插件",
    "openviking": "OpenViking - 字节火山开源的OpenClaw记忆插件",
    "conductor": "Conductor - AI Agent编排工具",
    "swe-agent": "SWE-Agent - 软件工程Agent",
    "react pattern": "ReAct Pattern - 推理+行动的Agent执行模式",
    "productionization": "Productionization - 将原型系统转化为生产级系统的过程",
    "one-person company": "One-Person Company - 一人公司，个人运营的商业模式",
    "personal operating system": "Personal Operating System - 个人操作系统，管理个人知识和工作流的系统",
    "knowledge compiler": "Knowledge Compiler - 知识编译器，将原始信息转化为结构化知识的模式",
    "knowledge compression": "Knowledge Compression - 知识压缩，提炼核心知识减少冗余",
    "information fidelity": "Information Fidelity - 信息保真度，信息传递过程中的准确性",
    "scribe fallacy": "Scribe Fallacy - 书吏谬误，过度关注记录而忽视理解",
    "elevator effect": "Elevator Effect - 电梯效应，技术进步带来的认知局限",
    "engineering compromise": "Engineering Compromise - 工程妥协，在约束条件下寻找可行方案",
    "self-design": "Self-Design Through Environmental Engineering - 通过环境工程实现自我设计",
    "derivation-first learning": "Derivation-First Learning - 推导优先学习法",
    "description trigger optimization": "Description Trigger Optimization - 描述触发优化，改进Skill被自动激活的准确性",
    "iterative skill development": "Iterative Skill Development - 迭代式Skill开发",
    "skill as asset": "Skill as Asset - 将Skill视为可复用资产",
    "skill activation": "Skill Activation - Skill激活，Agent决定使用某个Skill的过程",
    "skill triggering": "Skill Triggering - Skill触发，识别何时应使用某个Skill",
    "enterprise skill engineering": "Enterprise Skill Engineering - 企业级Skill工程",
    "modular focused skill design": "Modular Focused Skill Design - 模块化聚焦Skill设计",
    "convergent evolution": "Convergent Evolution in AI Tools - AI工具的趋同进化",
    "benchmark vs engineering": "Benchmark vs Engineering Reality Gap - 基准测试与工程现实的差距",
    "cost management in ai": "Cost Management in AI Development - AI开发中的成本管理",
    "model failover": "Model Failover Mechanism - 模型故障转移机制",
    "model switching": "Model-Switching Optimization - 模型切换优化",
    "parallel tool calling": "Parallel Tool Calling - 并行工具调用",
    "cross-model code review": "Cross-Model Code Review - 跨模型代码审查",
    "distributed context": "Distributed Context Management - 分布式上下文管理",
    "local data sovereignty": "Local Data Sovereignty - 本地数据主权",
    "ai content saturation": "AI Content Saturation - AI内容饱和",
    "ai economics": "AI Economics - AI经济学",
    "ai reasoning models": "AI Reasoning Models - AI推理模型",
    "algorithmic mindset": "Algorithmic Mindset Shift - 算法思维转变",
    "probabilistic data structures": "Probabilistic Data Structures - 概率数据结构",
    "bit-level hacking": "Bit-Level Hacking - 位级技巧",
    "browser fingerprinting": "Browser Fingerprinting - 浏览器指纹识别",
    "exercise overload principle": "Exercise Overload Principle - 运动超负荷原则",
    "authenticity as capital": "Authenticity as Capital - 真实性作为资本",
    "curated digital exploration": "Curated Digital Exploration - 策展式数字探索",
    "open educational resources": "Open Educational Resources (OER) - 开放教育资源",
    "service trade globalization": "Service Trade Globalization - 服务贸易全球化",
    "industrial cluster advantage": "Industrial Cluster Advantage - 产业集群优势",
    "financial vs industrial logic": "Financial vs Industrial Logic - 金融逻辑与产业逻辑",
    "china manufacturing": "China Manufacturing - 中国制造业",
    "automotive electronics": "Automotive Electronics - 汽车电子",
    "cabin driving integration": "Cabin-Driving Integration - 舱驾一体",
    "smart cockpit": "Smart Cockpit - 智能座舱",
    "new energy vehicles": "New Energy Vehicles - 新能源汽车",
    "industrial moats": "Industrial Moats (护城河) - 产业护城河",
    "organizational system gap": "Organizational-System Gap - 组织与系统差距",
    "career transition barriers": "Career Transition Barriers - 职业转型障碍",
    "ai-assisted paper reading": "AI-Assisted Paper Reading - AI辅助论文阅读",
    "ai-enhanced note taking": "AI-Enhanced Note Taking - AI增强笔记",
    "ai native design workflow": "AI-Native Design Workflow - AI原生设计工作流",
    "ai tool specialization": "AI Tool Specialization - AI工具专业化",
    "ai tool chaining": "AI Tool Chaining - AI工具链组合",
    "ai free interface aesthetics": "AI-Free Interface Aesthetics - 无AI感界面美学",
    "design prompt engineering": "Design Prompt Engineering - 设计提示词工程",
    "design prompt curation": "Design Prompt Curation - 设计提示词策展",
    "front-end design": "Front-End Design - 前端设计，用户界面的视觉和交互设计",
    "low-code no-code frontend": "Low-Code/No-Code Frontend via AI - AI驱动的低代码/无代码前端",
    "content structure agility": "Content Structure Agility - 内容结构敏捷性",
    "coding plan": "Coding Plan - AI编程订阅计划",
    "agent shock": "Agent Shock - Agent冲击，AI Agent对行业的颠覆性影响",
    "agent first development": "Agent-First Development - Agent优先开发",
    "agent memory systems": "Agent Memory Systems - Agent记忆系统",
    "agent operating system": "Agent Operating System - Agent操作系统",
    "agent rl training": "Agent RL Training - Agent强化学习训练",
    "agent cognitive architecture": "AI Agent Cognitive Architecture - AI Agent认知架构",
    "agent complexity management": "AI Agent Complexity Management - AI Agent复杂性管理",
    "agent engineering career": "AI Agent Engineering Career Path - AI Agent工程职业路径",
    "multi-agent collaboration": "Multi-Agent Collaboration - 多Agent协作",
    "multi-agent orchestration": "Multi-Agent Orchestration - 多Agent编排",
    "productionization of agents": "Productionization of AI Agents - AI Agent的生产化",
    "enhanced rag": "Enhanced RAG with Human-like Reasoning - 增强型RAG",
    "llm search over rag": "LLM Search over RAG - LLM搜索优于RAG的观点",
    "domain specific language": "Domain-Specific Language (DSL) for AI Agents - AI Agent的领域特定语言",
    "compound engineering": "Compound Engineering - 复合工程",
    "decomposition as core skill": "Decomposition as Core Skill - 分解作为核心技能",
    "simplest working solution": "Simplest Working Solution Principle - 最简可行方案原则",
    "prototype first development": "Prototype-First Development - 原型优先开发",
    "rpa ai hybrid": "RPA-AI Hybrid Architecture - RPA与AI混合架构",
    "preset ai personalities": "Preset AI Personalities - 预设AI人格",
    "community driven development": "Community-Driven Feature Development - 社区驱动的功能开发",
    "model capability driven evolution": "Model Capability-Driven Product Evolution - 模型能力驱动的产品进化",
    "permission modes": "Permission Modes (Claude Code) - Claude Code的权限模式",
    "persistent memory system": "Persistent Memory System (Claude Code) - Claude Code的持久记忆系统",
    "git based knowledge management": "Git-Based Knowledge Management - 基于Git的知识管理",
    "git worktrees": "Git Worktrees for Parallel Development - Git工作树并行开发",
    "hooks for automation": "Hooks for Deterministic Automation - 确定性自动化的钩子",
    "managed scraping browser": "Managed Scraping Browser - 托管式爬虫浏览器",
    "local model deployment": "Local Model Deployment - 本地模型部署",
    "free model integration": "Free Model Integration via NIM - 通过NIM集成免费模型",
    "dynamic multi-llm": "Dynamic Multi-LLM Support with Failover - 动态多LLM支持与故障转移",
    "code fence sandbox": "Code Fence Sandbox/IFrame Architecture - 代码围栏沙箱架构",
    "multi-format block support": "Multi-Format Block Support - 多格式块支持",
    "mobile-first note taking": "Mobile-First Note Taking UX - 移动优先笔记体验",
    "obsidian plugin ecosystem": "Obsidian Plugin Ecosystem - Obsidian插件生态",
    "note organization philosophy": "Note Organization Philosophy - 笔记组织哲学",
    "markdown as interface": "Markdown as Human-AI Interface - Markdown作为人机界面",
    "cli design principles": "CLI Design for AI and Human - AI和人类友好的CLI设计原则",
    "self-directed learning": "Self-Directed Learning Infrastructure - 自主学习基础设施",
    "open source educational tools": "Open Source Educational Tools - 开源教育工具",
    "information source curation": "Information Source Curation - 信息源策展",
    "self-verification": "Self-Verification and Quality Auditing in AI Systems - AI系统中的自验证与质量审计",
    "humanize workflow": "Humanize Workflow - 人性化工作流",
    "constraint engineering": "Constraint Engineering - 约束工程，Vibe Coding的重点",
    "visual coding": "Visual Coding - 可视化编程，从Vibe Coding进化",
    "brian chesky mode": "Brian Chesky Mode - Brian Chesky的产品管理方式",
    "7-step strategic planning": "7-Step Strategic Planning Framework - 七步战略规划框架",
    "blm model": "BLM (Business Leadership Model) - 业务领导力模型",
    "persona method": "Persona (用户画像) - 用户画像方法",
    "offensive proactive personality": "Offensive Proactive Personality (进攻型人格) - 进攻型人格特质",
    "personal transformation": "Personal Transformation Through Incremental Action - 通过渐进行动实现个人转变",
    "memory command": "Memory Command (记忆命令) - AI记忆管理命令",
    "git ceremony automation": "Git Ceremony Automation (Git仪式自动化) - Git工作流自动化",
    "ai exponential pm": "AI Exponential Product Management - AI指数级产品管理",
    "ai induced disruption": "AI-Induced Industry Disruption - AI引发的行业颠覆",
    "ai programming ecosystem": "AI Programming Ecosystem - AI编程生态系统",
    "aesthetic judgment": "Aesthetic Judgment in Tech - 技术中的审美判断",
    "low cost aesthetic improvement": "Low-Cost Methods for Aesthetic Improvement - 低成本审美提升方法",
    "acceptance of imperfection": "Acceptance of Imperfection and Complexity - 接受不完美和复杂性",
    "dream first business second": "Dream First, Business Second Entrepreneurship - 梦想优先创业",
    "edge exploration": "Edge Exploration Projects (Side Quests) - 边缘探索项目",
    "single mode problem": "Single-Mode Problem - 单一模式问题",
    "contradiction analysis": "Contradiction Analysis - 矛盾分析",
    "knowledge wasteland": "Knowledge Wasteland (知识荒原) - 知识荒原现象",
    "ai model evolution": "AI大模型演进评估",
    "claude md philosophy": "CLAUDE.md配置哲学",
    "agent first year": "Agent元年 (Agent First Year) - Agent元年",
    "spec coding vs vibe coding": "Spec Coding vs Vibe Coding - 规格编程vs氛围编程",
    "comment poisoning": "注释毒化与生成物管理",
    "system prompt demotion": "系统提示降权",
    "model characteristics constraints": "模型特性与约束",
    "probabilistic prompt limitations": "概率性提示词局限",
    "tool chain plugin ecosystem": "工具链与插件生态",
    "local deployment integration": "本地部署与集成",
    "agent self evolution": "智能体自我进化",
    "role based ai development": "基于角色的AI开发",
    "skill package": "技能包",
    "gstack workflow": "GStack角色化AI开发工作流",
    "harness engineering zh": "Harness Engineering详解",
    "humanize zh": "Humanize工作流",
    "git ceremony": "Git仪式自动化",
    "agent skill vs mcp": "Agent Skill vs MCP技术对比",
    "agent skills knowledge retrieval": "Agent Skills知识库检索vs传统RAG",
    "openclaw global consensus": "OpenClaw全球共识窗口",
    "openclaw multi agent": "OpenClaw多Agent协作",
    "openclaw correct usage": "OpenClaw正确使用指南",
    "claude code hidden features": "Claude Code隐藏功能",
    "claude code developer tips": "Claude Code开发者踩坑经验",
    "claude code systematic tutorial": "Claude Code系统教程",
    "claude code workplace avatar": "Claude Code职场替身",
    "claude code notebooklm workflow": "Claude Code NotebookLM工作流",
    "claude code obsidian personal os": "Claude Code Obsidian个人操作系统",
    "claude code efficient config": "Claude Code高效配置",
    "claude code sub agents": "Claude Code子代理",
    "claude code hooks config": "Claude Code Hooks配置",
    "claude code skills system": "Claude Code Skills系统",
    "obsidian ai era advantage": "Obsidian在AI时代的优势",
    "obsidian sync solutions": "Obsidian同步方案",
    "obsidian mcp integration": "Obsidian MCP集成",
    "n8n workflow automation": "N8N工作流自动化",
    "n8n youtube intelligence": "N8N YouTube热点情报系统",
    "n8n multi platform sync": "N8N多平台同步工作流",
    "google ai agent whitepaper": "Google AI Agent白皮书",
    "karpathy knowledge base": "Karpathy知识库架构",
    "one person ai company": "一人AI公司架构",
    "vibe coding aesthetics": "Vibe Coding美学问题",
    "vibe design": "Vibe Design设计师变革",
    "visual coding evolution": "Visual Coding从Vibe Coding进化",
    "ai coding tools prompts": "AI编程工具提示词开源",
    "ai office efficiency": "AI办公提效工具",
    "ai learning efficiency": "AI学习效率工具",
    "marketing skill": "Marketing Skill营销专家",
    "product manager skill": "Product Manager Skill产品经理",
    "project analyzer skill": "Project Analyzer逆向工程Skill",
    "frontend design skill": "Frontend Design Skill前端设计",
    "slide generation skill": "幻灯片生成Skill",
    "bmad method analysis": "BMAD Method项目分析",
    "automotive terminology": "Automotive Electronics Terminology - 汽车电子术语",
    "porsche design evolution": "Porsche 911 Design Evolution - 保时捷911设计进化",
    "byd strategy": "BYD Strategy - 比亚迪战略",
    "new energy survival": "2026新能源大逃杀",
    "deepseek practical guide": "DeepSeek实用应用指南",
    "prompt optimizer": "提示词优化器开源项目",
    "freelancer platform": "自由职业者平台",
    "canirun local llm": "CanIRun本地LLM评估",
    "ltx desktop": "LTX Desktop AI视频编辑器",
    "creative tim": "Creative Tim UI组件库",
    "startup graveyard": "创业墓地网站",
    "personal top movies": "个人十佳电影推荐",
    "qiandao lake road trip": "千岛湖大环线自驾游",
    "chinese martial arts internal": "中国武术内功",
    "palm reading holographic": "手相与全息理论",
    "guangchen philosophy": "和光同尘哲学",
    "open source": "Open Source - 开源，源代码公开可自由使用的软件",
    "carney davos speech": "Carney 2026达沃斯演讲",
    "chen tianqiao agi": "陈天桥AGI愿景",
    "zhao tingyang humanities": "赵汀阳人工智能时代的文科",
    "kimi attention residual": "Kimi注意力残差论文",
    "shanghai aerial photography": "上海航拍",
    "ai decision quality": "AI真正改变的不是效率而是决策质量",
    "consumption vs production learning": "AI时代消费型学习VS生产型学习",
    "future skill combinations": "未来新的高收入技能组合",
    "microscope website": "显微镜微观世界网站",
    "ai-assisted design": "AI-Assisted Design - AI辅助设计",
    "agent-based active retrieval": "Agent-Based Active Retrieval - 基于Agent的主动检索",
    "agent-loop-model-harness": "Agent Loop Model Harness - Agent循环模型驾驭",
    "agent-harness": "Agent Harness - Agent驾驭系统",
    "autonomous-task-planning-execution": "Autonomous Task Planning & Execution - 自主任务规划与执行",
    "brain-prediction-model": "Brain Prediction Model - 大脑预测模型",
    "brain-prediction-model-updating": "Brain Prediction Model Updating - 大脑预测模型更新",
    "business-sop-automation": "Business SOP Automation - 业务SOP自动化",
    "chinese-language-ai-specialization": "Chinese Language AI Specialization - 中文AI语言特化",
    "chinese-large-language-models": "Chinese Large Language Models - 中国大语言模型",
    "claude-code-hooks": "Claude Code Hooks - Claude Code钩子系统",
    "claude-code-skills-system": "Claude Code Skills系统 - Claude Code的Skills系统",
    "claude-code-subagents": "Claude Code Subagents - Claude Code子代理系统",
    "gstack-role-based-ai-development-workflow-for-claude-code": "GStack角色化AI开发工作流",
    "ant-group": "Ant Group (蚂蚁集团) - 金融科技巨头",
    "armin-ronacher": "Armin Ronacher - Flask和Ruff的创造者",
    "bytedance-volcano-engine": "ByteDance Volcano Engine - 字节跳动火山引擎",
    "algorithms-probability-approach": "Algorithms: Probability Approach - 算法的概率方法",
    "baseline-a-b-testing": "Baseline & A/B Testing - 基线与A/B测试",
    "brian-chesky模式-brian-chesky-mode": "Brian Chesky模式 - Brian Chesky的产品管理方式",
    "claude-md": "CLAUDE.md - Claude Code配置文件",
    "claude-md配置哲学": "CLAUDE.md配置哲学 - CLAUDE.md的设计哲学和最佳实践",
    "agent-元年-agent-first-year": "Agent元年 - AI Agent发展的元年",
    "ai技术博客主题聚合": "AI技术博客主题聚合 - AI技术博客的主题分类和聚合",
    "ai-大模型演进评估": "AI大模型演进评估 - AI大模型的演进趋势评估",
}

KNOWN_ENTITIES = {
    "anthropic": ("organization", "Anthropic - AI安全公司，Claude和Claude Code的开发者"),
    "openai": ("organization", "OpenAI - AI研究公司，GPT和Codex的开发者"),
    "google": ("organization", "Google - 科技巨头，Gemini AI的开发者"),
    "microsoft": ("organization", "Microsoft - 科技巨头，Copilot和Azure AI的开发者"),
    "meta": ("organization", "Meta - 科技巨头，LLaMA系列开源模型"),
    "bytedance": ("organization", "字节跳动 - 中国科技公司，DeerFlow和火山引擎"),
    "nvidia": ("organization", "NVIDIA - GPU和AI芯片巨头"),
    "deepseek": ("organization", "DeepSeek - 中国AI公司，DeepSeek模型开发者"),
    "tesla": ("organization", "Tesla - 电动汽车和自动驾驶公司"),
    "byd": ("organization", "比亚迪 - 中国新能源汽车巨头"),
    "figma": ("product", "Figma - 协作式UI设计工具"),
    "obsidian": ("product", "Obsidian - 基于Markdown的双向链接知识管理工具"),
    "notion": ("product", "Notion - 多功能协作和笔记工具"),
    "cursor": ("product", "Cursor - AI驱动的代码编辑器"),
    "claude code": ("product", "Claude Code - Anthropic的AI编程助手"),
    "claude": ("product", "Claude - Anthropic的AI助手"),
    "chatgpt": ("product", "ChatGPT - OpenAI的AI对话助手"),
    "gemini": ("product", "Gemini - Google的AI大模型"),
    "gpt": ("product", "GPT - OpenAI的大语言模型系列"),
    "openclaw": ("product", "OpenClaw - 开源AI Agent框架"),
    "n8n": ("product", "N8N - 开源工作流自动化平台"),
    "playwright": ("product", "Playwright - 微软开源的浏览器自动化框架"),
    "selenium": ("product", "Selenium - 浏览器自动化测试工具"),
    "github": ("product", "GitHub - 代码托管和协作平台"),
    "kimi": ("product", "Kimi - 月之暗面的AI助手"),
    "qwen": ("product", "通义千问 - 阿里云的大语言模型"),
    "doubao": ("product", "豆包 - 字节跳动的AI助手"),
    "andrej karpathy": ("person", "Andrej Karpathy - AI研究者，前OpenAI创始成员和Tesla AI总监"),
    "simon willison": ("person", "Simon Willison - Django联合创始人，LLM工具开发者"),
    "ryan dahl": ("person", "Ryan Dahl - Node.js和Deno的创造者"),
    "armin ronacher": ("person", "Armin Ronacher - Flask和Ruff的创造者"),
    "mitchell hashimoto": ("person", "Mitchell Hashimoto - HashiCorp联合创始人"),
    "dhh": ("person", "David Heinemeier Hansson (DHH) - Rails创造者"),
    "brian chesky": ("person", "Brian Chesky - Airbnb联合创始人和CEO"),
    "ethan mollick": ("person", "Ethan Mollick - Wharton教授，AI应用研究者"),
    "陈天桥": ("person", "陈天桥 - 盛大网络创始人，AGI愿景倡导者"),
    "赵汀阳": ("person", "赵汀阳 - 中国社会科学院哲学家"),
    "王传福": ("person", "王传福 - 比亚迪创始人"),
    "吴恩达": ("person", "吴恩达 - AI教育家，DeepLearning.ai创始人"),
    "paul graham": ("person", "Paul Graham - Y Combinator联合创始人"),
    "steph ango": ("person", "Steph Ango (Kepano) - Obsidian CEO"),
    "thariq": ("person", "Thariq - Claude Code产品负责人"),
    "boris": ("person", "Boris - Claude Code核心团队成员"),
    "cat wu": ("person", "Cat Wu - Anthropic产品经理"),
    "ai学习的老章": ("person", "Ai学习的老章 - AI Skills领域知乎博主"),
    "非著名程序员": ("person", "非著名程序员 - 前端设计Skill推广者"),
    "闪客": ("person", "闪客 - AI技术深度解读博主"),
    "饼干哥哥agi": ("person", "饼干哥哥AGI - AI编程工具测评博主"),
    "好地方bug": ("person", "好地方bug - AI编程经验分享博主"),
    "序员先生": ("person", "序员先生 - AI编程教程博主"),
    "如萤随星": ("person", "如萤随星 - AI工具教程创作者"),
    "木游子": ("person", "木游子 - AI工具测评博主"),
    "汉松": ("person", "汉松 - AI编程实践分享者"),
    "白玉京": ("person", "白玉京 - AI Agent领域博主"),
    "歸藏": ("person", "歸藏 - AI行业分析博主"),
    "清华": ("organization", "清华大学 - 中国顶尖大学"),
    "港大": ("organization", "香港大学 - AI开源项目研究"),
    "知乎": ("platform", "知乎 - 中国问答社区平台"),
    "b站": ("platform", "B站 (Bilibili) - 中国视频分享平台"),
    "小红书": ("platform", "小红书 - 中国生活分享社区"),
    "hacker news": ("platform", "Hacker News - 技术新闻聚合平台"),
    "微博": ("platform", "微博 - 中国社交媒体平台"),
    "微信公众号": ("platform", "微信公众号 - 中国内容发布平台"),
    "飞书": ("product", "飞书 - 字节跳动的企业协作平台"),
    "chatgpt plus": ("product", "ChatGPT Plus - OpenAI的付费订阅服务"),
    "deepseek r1": ("product", "DeepSeek R1 - DeepSeek的推理模型"),
    "glm-5": ("product", "GLM-5 - 智谱AI的大语言模型"),
    "kimi k2.5": ("product", "Kimi K2.5 - 月之暗面的AI模型"),
    "minimax m2.5": ("product", "MiniMax M2.5 - MiniMax的AI模型"),
    "qwen3": ("product", "Qwen3 - 阿里云通义千问3"),
    "claude opus 4": ("product", "Claude Opus 4 - Anthropic最强模型"),
    "swe-agent": ("product", "SWE-Agent - Princeton的软件工程Agent"),
    "crewai": ("product", "CrewAI - 多Agent协作框架"),
    "autogen": ("product", "AutoGen - Microsoft的多Agent框架"),
    "langgraph": ("product", "LangGraph - LangChain的Agent编排框架"),
    "conductor": ("product", "Conductor - AI Agent编排工具"),
    "cherry studio": ("product", "Cherry Studio - AI对话客户端"),
    "tavily": ("product", "Tavily - AI搜索API"),
    "bright data": ("product", "Bright Data (亮数据) - 网页数据采集平台"),
    "unsloth": ("product", "Unsloth - LLM微调加速工具"),
    "opencode": ("product", "OpenCode - 开源Claude Code替代"),
    "canirun": ("product", "CanIRun.ai - 本地LLM运行评估工具"),
    "ltx desktop": ("product", "LTX Desktop - AI视频编辑器"),
    "creative tim": ("product", "Creative Tim - UI组件库"),
    "designprompts": ("product", "DesignPrompts.dev - 设计提示词策展平台"),
    "slidev": ("product", "Slidev - Markdown演示文稿工具"),
    "bmad-method": ("product", "BMAD Method - 一人公司AI开发方法论"),
    "deerflow": ("product", "DeerFlow - 字节跳动多Agent研究框架"),
    "supermemory": ("product", "Supermemory - AI记忆系统"),
    "mem0": ("product", "Mem0 - 开源AI记忆框架"),
    "litmaps": ("product", "Litmaps - 学术论文关系可视化"),
    "mineru": ("product", "MinerU - PDF解析开源项目"),
    "scrapling": ("product", "Scrapling - 自适应网页爬虫"),
    "firecrawl": ("product", "Firecrawl - 网页内容提取API"),
    "agent-reach": ("product", "Agent-Reach - Agent全网感知CLI"),
    "mcp2cli": ("product", "MCP2CLI - MCP工具转CLI命令"),
    "autoresearch": ("product", "AutoResearch - Claude Code自动迭代Skill"),
    "gitnexus": ("product", "GitNexus - 代码知识图谱"),
    "mirofish": ("product", "MiroFish - 群体智能预测引擎"),
    "typewords": ("product", "TypeWords - 打字式背单词工具"),
    "bilibili-cli": ("product", "Bilibili CLI - B站命令行客户端"),
    "subbatch": ("product", "SubBatch - B站字幕批量处理插件"),
    "dragger": ("product", "Obsidian Dragger - 文本块拖拽插件"),
    "humanize plugin": ("product", "Humanize - Obsidian AI辅助插件"),
    "superpowers plugin": ("product", "Superpowers - Claude Code增强插件"),
    "openviking": ("product", "OpenViking - 字节火山记忆插件"),
    "dataview": ("product", "Dataview - Obsidian数据查询插件"),
    "oh-my-claudecode": ("product", "Oh My ClaudeCode - Claude Code增强工具集"),
    "open pencil": ("product", "Open Pencil - AI原生设计编辑器"),
    "google stitch": ("product", "Google Stitch - AI设计平台"),
    "claudekit": ("product", "ClaudeKit - 前端设计Skill演示"),
    "skill-creator": ("product", "Skill-Creator - Anthropic官方Skill创建工具"),
    "porsche": ("organization", "Porsche (保时捷) - 德国豪华汽车品牌"),
    "geely": ("organization", "Geely (吉利) - 中国汽车集团"),
    "华为": ("organization", "Huawei (华为) - 中国科技巨头"),
    "腾讯": ("organization", "Tencent (腾讯) - 中国科技巨头"),
    "面壁": ("organization", "面壁智能 - 中国AI公司"),
    "alibaba": ("organization", "Alibaba (阿里巴巴) - 中国电商和云计算巨头"),
    "boeing": ("organization", "Boeing - 美国航空航天公司"),
    "khan academy": ("organization", "Khan Academy (可汗学院) - 免费教育平台"),
    "ant group": ("organization", "Ant Group (蚂蚁集团) - 金融科技巨头"),
    "antirez": ("person", "Antirez (Salvatore Sanfilippo) - Redis创造者"),
    "david autor": ("person", "David Autor - MIT经济学家，劳动和技术研究"),
    "james gleick": ("person", "James Gleick - 科学作家，《混沌》作者"),
    "mcell": ("person", "mCell - Harness Engineering深度分析作者"),
    "luhui dev": ("person", "Luhui Dev - AI工具开发者"),
    "海伦娜·坦格利安": ("person", "海伦娜·坦格利安 - AI技术评论者"),
    "mizore": ("person", "Mizore - Claude Code一键配置工具开发者"),
    "jasper wang": ("person", "Jasper Wang - AI工具测评博主"),
    "陈皓": ("person", "陈皓 (Coolshell/Haoel) - 技术博主，酷壳网站创始人"),
    "红杉资本": ("organization", "Sequoia Capital (红杉资本) - 全球顶级风投"),
    "cloudflare": ("organization", "Cloudflare - 网络安全和CDN服务商"),
    "volcano engine": ("product", "Volcano Engine (火山引擎) - 字节跳动的云服务平台"),
    "bilibili": ("platform", "Bilibili (B站) - 中国视频分享平台"),
    "youtube": ("platform", "YouTube - 全球最大视频分享平台"),
    "github copilot": ("product", "GitHub Copilot - GitHub的AI编程助手"),
    "windsurf": ("product", "Windsurf (原Codeium) - AI代码编辑器"),
    "trae": ("product", "Trae - 字节跳动的AI IDE"),
    "notebooklm": ("product", "NotebookLM - Google的AI笔记助手"),
    "vercel": ("organization", "Vercel - 前端云平台，Next.js开发者"),
    "stripe": ("organization", "Stripe - 在线支付平台"),
    "airbnb": ("organization", "Airbnb - 住宿共享平台"),
    "y combinator": ("organization", "Y Combinator - 全球顶级创业加速器"),
    "princeton": ("organization", "Princeton University - 普林斯顿大学"),
    "mit": ("organization", "MIT - 麻省理工学院"),
    "stanford": ("organization", "Stanford University - 斯坦福大学"),
    "harvard": ("organization", "Harvard University - 哈佛大学"),
    "wharton": ("organization", "Wharton School - 沃顿商学院"),
    "svpg": ("organization", "SVPG - Silicon Valley Product Group"),
}


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s\-/&,]", " ", text)
    text = re.sub(r"[/&]", "-", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    text = re.sub(r"^[-,]+|[-,]+$", "", text)
    return text


def compute_file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_ingest_cache() -> dict[str, str]:
    if CACHE_FILE.exists():
        try:
            return json.loads(CACHE_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return {}
    return {}


def save_ingest_cache(cache: dict[str, str]):
    CACHE_FILE.write_text(json.dumps(cache, indent=2, ensure_ascii=False), encoding="utf-8")


def mark_ingested(source_path: Path):
    cache = load_ingest_cache()
    key = str(source_path.relative_to(ROOT_DIR)).replace("\\", "/")
    cache[key] = compute_file_hash(source_path)
    save_ingest_cache(cache)


def is_ingested(source_path: Path) -> bool:
    cache = load_ingest_cache()
    key = str(source_path.relative_to(ROOT_DIR)).replace("\\", "/")
    return cache.get(key) == compute_file_hash(source_path)


def get_source_files() -> list[Path]:
    files = []
    for subdir in ["articles", "videos", "webpages"]:
        d = RAW_DIR / subdir
        if d.exists():
            files.extend(sorted(d.glob("*.md")))
    return files


def parse_source_metadata(content: str) -> dict:
    metadata = {"type": "article", "author": "", "platform": ""}
    if "## 视频信息" in content:
        metadata["type"] = "video"
    elif "## 文章信息" in content:
        metadata["type"] = "article"
    author_match = re.search(r"\*\*作者\*\*:\s*(.+)", content)
    if author_match:
        metadata["author"] = author_match.group(1).strip()
    platform_match = re.search(r"\*\*平台\*\*:\s*(.+)", content)
    if platform_match:
        metadata["platform"] = platform_match.group(1).strip()
    tags_match = re.search(r"\*\*标签\*\*:\s*(.+)", content)
    if tags_match:
        metadata["tags"] = [t.strip() for t in tags_match.group(1).split(",")]
    return metadata


def extract_clean_content(content: str) -> str:
    lines = content.split("\n")
    clean_lines = []
    in_metadata = False
    content_started = False
    for line in lines:
        if line.strip().startswith("## 文章信息") or line.strip().startswith("## 视频信息"):
            in_metadata = True
            continue
        if in_metadata and line.strip().startswith("## "):
            in_metadata = False
            content_started = True
        if in_metadata:
            continue
        if line.strip().startswith("## 内容"):
            content_started = True
            continue
        if content_started:
            clean_lines.append(line)
    return "\n".join(clean_lines).strip() if clean_lines else content


def extract_title(content: str, filepath: Path) -> str:
    first_line = content.strip().split("\n")[0] if content.strip() else ""
    if first_line.startswith("# "):
        return first_line[2:].strip()
    name = filepath.stem
    parts = re.split(r"[_]", name, 1)
    if len(parts) > 1:
        return parts[1].strip()
    return name.strip()


def find_matching_concepts(content: str, title: str) -> list[dict]:
    content_lower = content.lower()
    title_lower = title.lower()
    matched = []
    for key, definition in DOMAIN_CONCEPTS.items():
        key_lower = key.lower()
        if key_lower in content_lower or key_lower in title_lower:
            concept_name = key.split(" (")[0].split(" |")[0].strip()
            concept_name = concept_name.split(" - ")[0].strip()
            matched.append({
                "name": concept_name.title() if concept_name.isascii() and not any('\u4e00' <= c <= '\u9fff' for c in concept_name) else concept_name,
                "definition": definition,
                "key": key,
            })
    matched.sort(key=lambda x: len(x["key"]), reverse=True)
    seen_names = set()
    unique_matched = []
    for m in matched:
        name_lower = m["name"].lower()
        if name_lower not in seen_names:
            seen_names.add(name_lower)
            unique_matched.append(m)
    return unique_matched[:15]


def find_matching_entities(content: str, title: str) -> list[dict]:
    content_lower = content.lower()
    matched = []
    for key, (entity_type, description) in KNOWN_ENTITIES.items():
        if key.lower() in content_lower:
            matched.append({
                "name": key.title() if key.isascii() and not any('\u4e00' <= c <= '\u9fff' for c in key) else key,
                "type": entity_type,
                "description": description,
                "key": key,
            })
    matched.sort(key=lambda x: len(x["key"]), reverse=True)
    seen_names = set()
    unique_matched = []
    for m in matched:
        name_lower = m["name"].lower()
        if name_lower not in seen_names:
            seen_names.add(name_lower)
            unique_matched.append(m)
    return unique_matched[:10]


def generate_summary(content: str, title: str, concepts: list[dict], entities: list[dict]) -> str:
    sentences = re.split(r'[。！？\.\!\?]', content)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 20]
    if not sentences:
        return f"关于{title}的源文档。"
    summary_parts = sentences[:3]
    summary = "。".join(summary_parts)
    if len(summary) > 500:
        summary = summary[:500] + "..."
    return summary


def make_wikilink(title: str) -> str:
    return f"[[{title}]]"


def generate_source_page(title, source_ref, summary, concepts, entities, tags, content_type):
    now = datetime.now().isoformat()
    concept_links = [make_wikilink(c["name"]) for c in concepts]
    entity_links = [make_wikilink(e["name"]) for e in entities]
    all_related = concept_links + entity_links
    lines = [
        "---",
        f'title: "{title}"',
        f'type: "source"',
        f'sources:',
        f'  - "{source_ref}"',
        f'tags:',
    ]
    for tag in tags[:10]:
        lines.append(f'  - "{tag}"')
    lines.extend([
        f'confidence: "high"',
        f'created_at: "{now}"',
        f'updated_at: "{now}"',
    ])
    if all_related:
        lines.append("related:")
        for r in all_related[:20]:
            lines.append(f'  - "{r.strip("[]")}"')
    lines.extend(["---", ""])
    lines.extend([f"# {title}", "", "## 概述", "", summary, ""])
    if concepts:
        lines.extend(["## 核心概念", ""])
        for c in concepts[:10]:
            short_def = c["definition"].split(" - ")[0].strip() if " - " in c["definition"] else c["definition"][:80]
            lines.append(f"- {make_wikilink(c['name'])}: {short_def}")
        lines.append("")
    if entities:
        lines.extend(["## 相关实体", ""])
        for e in entities[:8]:
            lines.append(f"- {make_wikilink(e['name'])} ({e['type']})")
        lines.append("")
    if all_related:
        lines.append("## Related")
        for r in all_related[:20]:
            lines.append(f"- {r}")
    return "\n".join(lines)


def generate_concept_page(name, definition, source_ref, related_concepts, related_entities, tags, confidence="high"):
    now = datetime.now().isoformat()
    all_related = related_concepts + related_entities
    lines = [
        "---",
        f'title: "{name}"',
        f'type: "concept"',
        f'sources:',
        f'  - "{source_ref}"',
        f'tags:',
    ]
    for tag in tags[:8]:
        lines.append(f'  - "{tag}"')
    lines.extend([
        f'confidence: "{confidence}"',
        f'created_at: "{now}"',
        f'updated_at: "{now}"',
    ])
    if all_related:
        lines.append("related:")
        for r in all_related[:15]:
            lines.append(f'  - "{r}"')
    lines.extend(["---", ""])
    lines.extend([f"# {name}", "", "## 定义", "", definition, ""])
    if related_concepts:
        lines.extend(["## 相关概念", ""])
        for rc in related_concepts[:8]:
            lines.append(f"- {make_wikilink(rc)}")
        lines.append("")
    if related_entities:
        lines.extend(["## 相关实体", ""])
        for re_ent in related_entities[:5]:
            lines.append(f"- {make_wikilink(re_ent)}")
        lines.append("")
    if all_related:
        lines.append("## Related")
        for r in all_related[:15]:
            lines.append(f"- {make_wikilink(r)}")
    return "\n".join(lines)


def generate_entity_page(name, entity_type, description, source_ref, related_concepts, tags):
    now = datetime.now().isoformat()
    lines = [
        "---",
        f'title: "{name}"',
        f'type: "entity"',
        f'sources:',
        f'  - "{source_ref}"',
        f'tags:',
    ]
    for tag in tags[:6]:
        lines.append(f'  - "{tag}"')
    lines.extend([
        f'confidence: "high"',
        f'created_at: "{now}"',
        f'updated_at: "{now}"',
    ])
    if related_concepts:
        lines.append("related:")
        for r in related_concepts[:10]:
            lines.append(f'  - "{r}"')
    lines.extend(["---", ""])
    lines.extend([f"# {name}", "", "## 基本信息", "", f"**类型**: {entity_type}", "", "## 描述", "", description, ""])
    if related_concepts:
        lines.extend(["## 相关概念", ""])
        for rc in related_concepts[:8]:
            lines.append(f"- {make_wikilink(rc)}")
        lines.append("")
    if related_concepts:
        lines.append("## Related")
        for r in related_concepts[:10]:
            lines.append(f"- {make_wikilink(r)}")
    return "\n".join(lines)


def update_existing_page(path, source_ref, new_concepts, new_entities):
    try:
        existing = path.read_text(encoding="utf-8")
        changed = False
        source_match = re.search(r"sources:\n((?:  - .+\n)*)", existing)
        if source_match and source_ref not in source_match.group(0):
            new_sources = source_match.group(0) + f'  - "{source_ref}"\n'
            existing = existing[:source_match.start()] + new_sources + existing[source_match.end():]
            changed = True
        for name in new_concepts + new_entities:
            if name and f"[[{name}]]" not in existing and f'- "{name}"' not in existing:
                related_match = re.search(r"related:\n((?:  - .+\n)*)", existing)
                if related_match:
                    new_entry = f'  - "{name}"\n'
                    existing = existing[:related_match.end()] + new_entry + existing[related_match.end():]
                    changed = True
                related_section = re.search(r"## Related\n((?:- \[\[.+\]\]\n)*)", existing)
                if related_section:
                    new_link = f"- [[{name}]]\n"
                    existing = existing[:related_section.end()] + new_link + existing[related_section.end():]
                    changed = True
        if changed:
            existing = re.sub(r'updated_at: "[^"]*"', f'updated_at: "{datetime.now().isoformat()}"', existing)
            path.write_text(existing, encoding="utf-8")
    except Exception as e:
        print(f"  Warning: Failed to update {path}: {e}")


def add_bidirectional_link(source_title, target_title):
    target_slug = slugify(target_title)
    for subdir in ["concepts", "entities", "sources", "answers"]:
        target_path = WIKI_DIR / subdir / f"{target_slug}.md"
        if target_path.exists():
            try:
                content = target_path.read_text(encoding="utf-8")
                if f"[[{source_title}]]" not in content and f'- "{source_title}"' not in content:
                    related_match = re.search(r"related:\n((?:  - .+\n)*)", content)
                    if related_match:
                        new_entry = f'  - "{source_title}"\n'
                        content = content[:related_match.end()] + new_entry + content[related_match.end():]
                    related_section = re.search(r"## Related\n((?:- \[\[.+\]\]\n)*)", content)
                    if related_section:
                        new_link = f"- [[{source_title}]]\n"
                        content = content[:related_section.end()] + new_link + content[related_section.end():]
                    content = re.sub(r'updated_at: "[^"]*"', f'updated_at: "{datetime.now().isoformat()}"', content)
                    target_path.write_text(content, encoding="utf-8")
            except Exception:
                pass
            break


def process_source(source_path: Path) -> dict:
    raw_content = source_path.read_text(encoding="utf-8")
    metadata = parse_source_metadata(raw_content)
    clean_content = extract_clean_content(raw_content)
    title = extract_title(raw_content, source_path)
    source_ref = str(source_path.relative_to(ROOT_DIR)).replace("\\", "/")
    concepts = find_matching_concepts(clean_content, title)
    entities = find_matching_entities(clean_content, title)
    summary = generate_summary(clean_content, title, concepts, entities)
    tags = metadata.get("tags", [])
    if not tags:
        tags = [c["name"].lower().replace(" ", "-") for c in concepts[:5]]
    content_type = metadata.get("type", "article")
    pages_created = []
    pages_updated = []
    source_slug = slugify(title)
    source_page_path = SOURCES_DIR / f"{source_slug}.md"
    source_md = generate_source_page(title, source_ref, summary, concepts, entities, tags, content_type)
    source_page_path.parent.mkdir(parents=True, exist_ok=True)
    source_page_path.write_text(source_md, encoding="utf-8")
    pages_created.append(f"source:{title}")
    concept_names = [c["name"] for c in concepts]
    entity_names = [e["name"] for e in entities]
    for concept in concepts:
        concept_name = concept["name"]
        concept_slug = slugify(concept_name)
        concept_path = CONCEPTS_DIR / f"{concept_slug}.md"
        related_concepts = [cn for cn in concept_names if cn != concept_name][:6]
        related_entities = entity_names[:4]
        if concept_path.exists():
            update_existing_page(concept_path, source_ref, related_concepts, related_entities)
            pages_updated.append(f"concept:{concept_name}")
        else:
            concept_tags = [concept_name.lower().replace(" ", "-")]
            confidence = "high" if len(concept["definition"]) > 50 else "medium"
            concept_md = generate_concept_page(concept_name, concept["definition"], source_ref, related_concepts, related_entities, concept_tags, confidence)
            concept_path.parent.mkdir(parents=True, exist_ok=True)
            concept_path.write_text(concept_md, encoding="utf-8")
            pages_created.append(f"concept:{concept_name}")
    for entity in entities:
        entity_name = entity["name"]
        entity_slug = slugify(entity_name)
        entity_path = ENTITIES_DIR / f"{entity_slug}.md"
        related_concepts_for_entity = concept_names[:5]
        if entity_path.exists():
            update_existing_page(entity_path, source_ref, related_concepts_for_entity, [])
            pages_updated.append(f"entity:{entity_name}")
        else:
            entity_tags = [entity["type"], entity_name.lower().replace(" ", "-")]
            entity_md = generate_entity_page(entity_name, entity["type"], entity["description"], source_ref, related_concepts_for_entity, entity_tags)
            entity_path.parent.mkdir(parents=True, exist_ok=True)
            entity_path.write_text(entity_md, encoding="utf-8")
            pages_created.append(f"entity:{entity_name}")
    for concept in concepts:
        add_bidirectional_link(title, concept["name"])
    for entity in entities:
        add_bidirectional_link(title, entity["name"])
    mark_ingested(source_path)
    return {
        "title": title,
        "source_ref": source_ref,
        "concepts_found": len(concepts),
        "entities_found": len(entities),
        "pages_created": pages_created,
        "pages_updated": pages_updated,
    }


def fix_bidirectional_links():
    print("\n=== Fixing bidirectional links ===")
    all_pages = {}
    for subdir in ["concepts", "entities", "sources", "answers"]:
        d = WIKI_DIR / subdir
        if d.exists():
            for path in d.glob("*.md"):
                try:
                    content = path.read_text(encoding="utf-8")
                    title_match = re.search(r'^title: "(.+)"', content, re.MULTILINE)
                    title = title_match.group(1) if title_match else path.stem
                    links = re.findall(r"\[\[([^\]]+)\]\]", content)
                    all_pages[title] = {"path": path, "links": links, "content": content}
                except Exception:
                    pass
    fixed_count = 0
    for title, info in all_pages.items():
        for link in info["links"]:
            link_clean = link.split("|")[0].strip()
            if link_clean in all_pages:
                target_info = all_pages[link_clean]
                target_content = target_info["content"]
                if f"[[{title}]]" not in target_content and f'[[{title}' not in target_content:
                    try:
                        content = target_info["path"].read_text(encoding="utf-8")
                        related_match = re.search(r"related:\n((?:  - .+\n)*)", content)
                        if related_match:
                            new_entry = f'  - "{title}"\n'
                            content = content[:related_match.end()] + new_entry + content[related_match.end():]
                        related_section = re.search(r"## Related\n((?:- \[\[.+\]\]\n)*)", content)
                        if related_section:
                            new_link = f"- [[{title}]]\n"
                            content = content[:related_section.end()] + new_link + content[related_section.end():]
                        content = re.sub(r'updated_at: "[^"]*"', f'updated_at: "{datetime.now().isoformat()}"', content)
                        target_info["path"].write_text(content, encoding="utf-8")
                        target_info["content"] = content
                        fixed_count += 1
                    except Exception:
                        pass
    print(f"  Fixed {fixed_count} bidirectional links")


def fix_shallow_pages():
    print("\n=== Expanding shallow pages ===")
    expanded = 0
    for subdir in ["concepts", "entities"]:
        d = WIKI_DIR / subdir
        if not d.exists():
            continue
        for path in d.glob("*.md"):
            try:
                content = path.read_text(encoding="utf-8")
                fm_end = content.find("---", 3)
                if fm_end == -1:
                    continue
                body = content[fm_end + 3:].strip()
                if len(body) < 200:
                    title_match = re.search(r'^title: "(.+)"', content, re.MULTILINE)
                    title = title_match.group(1) if title_match else path.stem
                    if subdir == "concepts":
                        key_lower = title.lower()
                        definition = DOMAIN_CONCEPTS.get(key_lower, DOMAIN_CONCEPTS.get(title, ""))
                        if definition:
                            insert_pos = content.find("## 定义")
                            if insert_pos == -1:
                                insert_pos = content.find("# " + title)
                                if insert_pos != -1:
                                    nl = content.find("\n", insert_pos)
                                    if nl != -1:
                                        addition = f"\n\n## 定义\n\n{definition}\n"
                                        content = content[:nl + 1] + addition + content[nl + 1:]
                            elif "## 定义\n\n" in content:
                                def_start = content.find("## 定义\n\n") + len("## 定义\n\n")
                                def_end = content.find("\n## ", def_start)
                                if def_end == -1:
                                    def_end = len(content)
                                current_def = content[def_start:def_end].strip()
                                if len(current_def) < 30:
                                    content = content[:def_start] + definition + content[def_end:]
                    content = re.sub(r'updated_at: "[^"]*"', f'updated_at: "{datetime.now().isoformat()}"', content)
                    path.write_text(content, encoding="utf-8")
                    expanded += 1
            except Exception:
                pass
    print(f"  Expanded {expanded} shallow pages")


def generate_stats() -> dict:
    stats = {
        "concepts": len(list(CONCEPTS_DIR.glob("*.md"))) if CONCEPTS_DIR.exists() else 0,
        "entities": len(list(ENTITIES_DIR.glob("*.md"))) if ENTITIES_DIR.exists() else 0,
        "sources": len(list(SOURCES_DIR.glob("*.md"))) if SOURCES_DIR.exists() else 0,
        "answers": len(list(ANSWERS_DIR.glob("*.md"))) if ANSWERS_DIR.exists() else 0,
        "total_links": 0,
        "dead_links": 0,
        "orphan_pages": 0,
    }
    all_titles = set()
    all_pages = {}
    for subdir in ["concepts", "entities", "sources", "answers"]:
        d = WIKI_DIR / subdir
        if d.exists():
            for path in d.glob("*.md"):
                try:
                    content = path.read_text(encoding="utf-8")
                    title_match = re.search(r'^title: "(.+)"', content, re.MULTILINE)
                    title = title_match.group(1) if title_match else path.stem
                    all_titles.add(title)
                    links = re.findall(r"\[\[([^\]]+)\]\]", content)
                    all_pages[title] = {"path": path, "links": links, "linked_from": []}
                except Exception:
                    pass
    for title, info in all_pages.items():
        stats["total_links"] += len(info["links"])
        for link in info["links"]:
            link_clean = link.split("|")[0].strip()
            if link_clean not in all_titles:
                stats["dead_links"] += 1
            elif link_clean in all_pages:
                all_pages[link_clean]["linked_from"].append(title)
    for title, info in all_pages.items():
        if not info["linked_from"] and not info["links"]:
            stats["orphan_pages"] += 1
    stats["total_pages"] = stats["concepts"] + stats["entities"] + stats["sources"] + stats["answers"]
    return stats


def main():
    print("=" * 60)
    print("Agent Deep Scan - Comprehensive Knowledge Base Scan")
    print("=" * 60)
    source_files = get_source_files()
    print(f"\nFound {len(source_files)} source files")
    uningested = [f for f in source_files if not is_ingested(f)]
    print(f"Uningested: {len(uningested)} files")

    if not uningested:
        if "--force" in sys.argv:
            uningested = source_files
            print(f"Force mode: reprocessing all {len(uningested)} files")
        else:
            print("All source files have been ingested. Running quality fixes...")
            fix_bidirectional_links()
            fix_shallow_pages()
            stats = generate_stats()
            print(f"\n=== Final Stats ===")
            for k, v in stats.items():
                print(f"  {k}: {v}")
            return

    total_created = 0
    total_updated = 0
    total_concepts = 0
    total_entities = 0
    errors = 0

    for i, source_path in enumerate(uningested, 1):
        try:
            result = process_source(source_path)
            total_created += len(result["pages_created"])
            total_updated += len(result["pages_updated"])
            total_concepts += result["concepts_found"]
            total_entities += result["entities_found"]
            print(f"  [{i}/{len(uningested)}] {result['title']}: "
                  f"{result['concepts_found']} concepts, {result['entities_found']} entities, "
                  f"{len(result['pages_created'])} created, {len(result['pages_updated'])} updated")
        except Exception as e:
            errors += 1
            print(f"  [{i}/{len(uningested)}] ERROR: {source_path.name}: {e}")

    print(f"\n=== Processing Summary ===")
    print(f"  Sources processed: {len(uningested) - errors}")
    print(f"  Errors: {errors}")
    print(f"  Pages created: {total_created}")
    print(f"  Pages updated: {total_updated}")
    print(f"  Concepts found: {total_concepts}")
    print(f"  Entities found: {total_entities}")

    fix_bidirectional_links()
    fix_shallow_pages()

    stats = generate_stats()
    print(f"\n=== Final Stats ===")
    for k, v in stats.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()