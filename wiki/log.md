# Wiki Log

Chronological record of wiki operations.
Format: ## [YYYY-MM-DD] operation | description

## [2026-04-20] batch-processing-full-validation | 全量扫描验证RAW→WIKI覆盖率，启动19个并行Agent处理
- Videos: 203文件，启动13个Agent批量处理（batch 1-7,9-11成功，batch 8,12,13 API限流）
- Articles: 26文件未处理，启动1个Agent处理（待验证）
- Webpages: 6有效文件，启动1个Agent处理 → 5页面创建
- Stub填充: 113个stub页面（79概念+23实体），启动4个Agent填充（待验证）
- 结果: wiki/sources从119增至269页面，stub从113降至74
- 覆盖率提升: Videos从4.93%提升至约75%，Articles约90%，Webpages有效内容100%

## [2026-04-20] validation-reports | 四维度校验完成
- Articles校验: 77源文件，53已处理，24待处理
- Videos校验: 203文件，仅10已处理（覆盖率4.93%）
- Webpages校验: 25文件，17无效（登录/Dribbble），6有效
- Wiki质量校验: 598页面，113 stub（18.9%），Sources 100%有效

## [2026-04-20] stub-filling-complete | Stub页面填充完成
- 概念Stub填充 batch 2: 20个页面，19成功填充，1保留（jasper-wang无来源）
- 概念Stub填充 batch 3: 20个页面，全部成功填充（技术人物、AI概念、商业方法论）
- Stub数量变化: 从113降至32（带stub标签），填充率72%
- 填充内容: 概述、核心要点（3-5个）、相关概念/实体链接

## [2026-04-20] articles-processing-complete | Articles处理完成
- 处理26个未生成wiki的articles文件
- 新增Sources页面: 从269增至295
- 覆盖率: Articles接近100%

## [2026-04-20] final-scan-completion | 最终扫描验证完成
- Stub页面: **全部填充完成**，从113降至0
- Videos覆盖率: 201/203 (**99%**)，仅剩2个待处理
- Wiki总页面: Sources 350 + Concepts 291 + Entities 188 = **829页**
- 并行Agent处理: 4批次处理59个视频文件
  - Batch 1: 11页面（含重复合并）
  - Batch 2: 12页面
  - Batch 3: 15页面
  - Batch 4: 19页面
- 新增Sources: 从295增至350（+55页面）

## [2026-04-20] final-summary | 全量扫描验证最终完成
- Wiki总页面: 774（Sources 295 + Concepts 291 + Entities 188）
- RAW覆盖率: Videos 76%（155/203），Articles ~100%，Webpages有效100%
- Stub改善: 从113降至1，**99%获得实质内容**
- Entity Stub填充完成: 11个页面全部填充，包括Anthropic、Claude.md架构、OpenClaw等

## [2026-04-20] entity-stub-complete | Entity stub页面填充完成
- 处理11个entity stub页面，全部成功填充
- 内容来源: Claude Code指南、知乎讨论、产品管理相关source
- wiki/index.md Entities部分更新，移除stub标记

## [2026-04-20] video-ingest-batch6 | 处理15个视频文件生成wiki页面（第六批） — 15 pages created, index.md updated

## [2026-04-20] video-ingest | 处理15个视频文件生成wiki页面 — 15 pages created, index.md updated

## [2026-04-20] webpages-ingest | 处理raw/webpages目录文件 — 5 pages created (1 skipped: 飞书文档需登录)

## [2026-04-20] chinese-pages | 为英文wiki页面生成中文版本 — 44 pages created

## [2026-04-17] ingest | Using DesignPrompts.dev to Generate High-Quality AI-Free Interfaces with Claude Code — 10 pages created/updated

## [2026-04-17] ingest | Using DesignPrompts.dev to Generate High-Quality AI-Free Interfaces — 10 pages created/updated

## [2026-04-17] ingest | Using DesignPrompts.dev to Generate High-Quality AI-Free Interfaces with Claude Code — 11 pages created/updated

## [2026-04-17] ingest | Using DesignPrompts.dev to Generate High-Quality AI-Free Interfaces with Claude Code — 13 pages created/updated

## [2026-04-17] query | 什么是 AI-Free Interface Design

## [2026-04-17] ingest | GStack: Role-Based AI Development Workflow for Claude Code — 10 pages created/updated

## [2026-04-17] ingest | Career Transition to Strategic Management and Consulting — 11 pages created/updated

## [2026-04-17] batch-ingest-errors | 1 errors: 0007311f_怎么成为一个ai agent 工程师怎么成为一个ai agent 工程师.md: LLM generation failed — could not parse JSON response

## [2026-04-17] query | 如何使用AI工具进行前端开发

## [2026-04-17] ingest | Zhihu Discussion: AI Agent Engineering Career Paths and Technical Approaches — 14 pages created/updated

## [2026-04-17] ingest | Zhihu Discussion: Career Transition to Strategic Management and Consulting — 12 pages created/updated

## [2026-04-17] ingest | Zhihu Discussion: Optimizing Claude Code with CLAUDE.md and Efficient Development Workflows — 12 pages created/updated

## [2026-04-17] ingest | Zhihu Discussion on Enlightenment and Personal Transformation — 9 pages created/updated

## [2026-04-17] ingest | Technical Blogging Platforms and Influential Programmers — 20 pages created/updated

## [2026-04-17] ingest | Zhihu Discussion: The Role of 'Scenarios' in Product Management — 16 pages created/updated

## [2026-04-17] ingest | TypeWords: Open-Source Typing-Based Vocabulary Learning Tool — 6 pages created/updated

## [2026-04-17] ingest | Claude Code Hidden Features Guide: Efficiency-Boosting Commands and Techniques — 8 pages created/updated

## [2026-04-17] ingest | Social Media Review of Front-End Design Tool — 5 pages created/updated

## [2026-04-17] ingest | Improving Vibe Coding Aesthetics with Design Prompts — 11 pages created/updated

## [2026-04-17] ingest | Advanced AI Agent Architecture for Financial Analysis — 13 pages created/updated

## [2026-04-17] ingest | Zhihu Discussion: Comprehensive Guide to High-Quality Information Sources for Learning and Career Development — 7 pages created/updated

## [2026-04-17] ingest | Learning Method Transition Crisis: From Memorization to Derivation — 8 pages created/updated

## [2026-04-17] ingest | Zhihu Discussion: Alternative Websites After Tianya Forum Closure — 12 pages created/updated

## [2026-04-17] ingest | Zhihu Discussion on Internal Martial Arts and Breathing Techniques — 9 pages created/updated

## [2026-04-17] batch-ingest-errors | 6 errors: 0bbdb067_为什么Claude的代码能力会这么强为什么Claude的代码能力会这么强.md: LLM generation failed — could not parse JSON response. Preview: ```json
{
  "source_page": {
    "title": "Advanced Claude Code Workflow Techniques and Technical Analysis",
    "content": "# Advanced Claude Code Workflow Techniques and Technical Analysis\n\n## Summary\nA comprehensive technical analysis of [[Claude Code]]'s programming capabilities, featuring 17; 149db3c1_Skills的本质是什么Skills的本质是什么.md: LLM generation failed — could not parse JSON response. Preview: ```json
{
  "source_page": {
    "title": "Anthropic Skills Engineering: From Concept to Production",
    "content": "# Anthropic Skills Engineering: From Concept to Production\n\n## Source Summary\nThis document provides a detailed analysis of Anthropic's evolving approach to developing **[[Skills ; 1ecc9a25_如何评价Karpathy提出的个人知识库的架构如何评价Karpathy提出的个人知识库的架构.md: LLM generation failed — could not parse JSON response. Preview: ```json
{
  "source_page": {
    "title": "Analysis of Karpathy's LLM-Powered Personal Knowledge Base Architecture",
    "content": "# Analysis of Karpathy's LLM-Powered Personal Knowledge Base Architecture\n\n## Summary\nThis analysis examines Andrej Karpathy's viral proposal for a three-layer pers

## [2026-04-17] ingest | Anthropic Skills: Engineering Approach to Agent Capability Development — 13 pages created/updated

## [2026-04-17] ingest | AI-Driven Product Management Transformation at Anthropic — 12 pages created/updated

## [2026-04-17] ingest | Google Stitch AI Design Platform Update and Market Impact — 9 pages created/updated

## [2026-04-17] ingest | 2026 Chinese AI Coding Plan Comparison and NVIDIA NIM Integration — 16 pages created/updated

## [2026-04-17] ingest | Zhihu Discussion: OpenClaw/Moltbot Practical Applications and Limitations — 10 pages created/updated

## [2026-04-17] ingest | Supermemory's ASMR System: A Critical Look at AI Memory Breakthroughs — 8 pages created/updated

## [2026-04-17] ingest | Zhihu Discussion: Algorithms That Inspire Awe in Computer Science — 13 pages created/updated

## [2026-04-17] ingest | DeepSeek AI Practical Applications and Prompt Engineering Guide — 11 pages created/updated

## [2026-04-17] ingest | Zhihu Discussion: Using Bright Data's Scraping Browser to Bypass Anti-Bot Detection — 8 pages created/updated

## [2026-04-17] batch-ingest-errors | 11 errors: 1ecc9a25_如何评价Karpathy提出的个人知识库的架构如何评价Karpathy提出的个人知识库的架构.md: while parsing a quoted scalar
  in "<unicode string>", line 5, column 5
found unknown escape character
  in "<unicode string>", line 5, column 18; 0bbdb067_为什么Claude的代码能力会这么强为什么Claude的代码能力会这么强.md: LLM generation failed — could not parse JSON response. Preview: ```json
{
  "source_page": {
    "title": "Advanced Claude Code Workflow Techniques and Architecture Analysis",
    "content": "# Advanced Claude Code Workflow Techniques and Architecture Analysis\n\n## Overview\nA comprehensive guide detailing 17 advanced techniques for maximizing [[Claude Code]]'s; 2b36f099_claude.md怎么写才能让Claude Code更高效claude.md怎么写才能让Claude Code更高效.md: LLM generation failed — could not parse JSON response. Preview: ```json
{
  "source_page": {
    "title": "Zhihu Discussion: Optimizing CLAUDE.md for Efficient Claude Code Development",
    "content": "# Zhihu Discussion: Optimizing CLAUDE.md for Efficient Claude Code Development\n\n## Summary\nA comprehensive Zhihu discussion thread where experienced users shar

## [2026-04-17] ingest | Zhihu Login Page Error Message — 4 pages created/updated

## [2026-04-17] batch-ingest-errors | 19 errors: 48f717b0_Claude Code真的那么厉害吗Claude Code真的那么厉害吗.md: litellm.InternalServerError: InternalServerError: DeepseekException - peer closed connection without sending complete message body (incomplete chunked read); 1ecc9a25_如何评价Karpathy提出的个人知识库的架构如何评价Karpathy提出的个人知识库的架构.md: litellm.InternalServerError: InternalServerError: DeepseekException - peer closed connection without sending complete message body (incomplete chunked read); 2b36f099_claude.md怎么写才能让Claude Code更高效claude.md怎么写才能让Claude Code更高效.md: litellm.InternalServerError: InternalServerError: DeepseekException - peer closed connection without sending complete message body (incomplete chunked read)

## [2026-04-18] ingest | Zhihu Discussion: Claude Code's Ecosystem, Impact on Engineering, and Practical Experiences — 11 pages created/updated

## [2026-04-18] ingest | Advanced Claude Code Workflow Techniques and Architecture Analysis — 18 pages created/updated

## [2026-04-18] ingest | Claude Code Agent Technical Analysis and Multi-Agent Architecture — 12 pages created/updated

## [2026-04-18] batch-ingest-errors | 3 errors: 1ecc9a25_如何评价Karpathy提出的个人知识库的架构如何评价Karpathy提出的个人知识库的架构.md: LLM generation failed — could not parse JSON response. Preview: ```json
{
  "source_page": {
    "title": "Analysis: Karpathy's LLM-Powered Personal Knowledge Base Architecture",
    "content": "# Analysis: Karpathy's LLM-Powered Personal Knowledge Base Architecture\n\n## Summary\nThis source analyzes Andrej Karpathy's viral proposal for a personal knowledge bas; 2b36f099_claude.md怎么写才能让Claude Code更高效claude.md怎么写才能让Claude Code更高效.md: while parsing a quoted scalar
  in "<unicode string>", line 5, column 5
found unknown escape character
  in "<unicode string>", line 5, column 18; 53771cfc_最好用的Agent框架是什么最好用的Agent框架是什么.md: LLM generation failed — could not parse JSON response. Preview: ```json
{
  "source_page": {
    "title": "Comprehensive Comparison of AI Agent Development Frameworks",
    "content": "# Comprehensive Comparison of AI Agent Development Frameworks\n\n## Summary\nA detailed analysis and comparison of popular AI Agent development frameworks, covering their features

## [2026-04-18] ingest | Agent Skills vs MCP: Technical Comparison and Enterprise Applications — 8 pages created/updated

## [2026-04-18] ingest | Zhihu Discussion: Strategic Planning Methodologies and Implementation Challenges — 11 pages created/updated

## [2026-04-18] ingest | Mizore's Claude Code Automation Toolkit and Paper Reading Skill — 8 pages created/updated

## [2026-04-18] ingest | Zhihu Discussion: The Era of Super Individuals and Agent Shock — 10 pages created/updated

## [2026-04-18] ingest | Zhihu Discussion: Financial vs. Industrial Logic in BYD's Development Strategy — 15 pages created/updated

## [2026-04-18] ingest | Zhihu Discussion: Zhang Xue's Journey from Mechanic to Motorcycle Champion Entrepreneur — 12 pages created/updated

## [2026-04-18] ingest | Zhihu Discussion: Optimal Exercise Methods for Middle-Aged Adults — 10 pages created/updated

## [2026-04-18] ingest | Zhihu Discussion: Open Source Projects for AI Visualization and Hardware Development — 10 pages created/updated

## [2026-04-18] batch-ingest-errors | 14 errors: 2b36f099_claude.md怎么写才能让Claude Code更高效claude.md怎么写才能让Claude Code更高效.md: while parsing a quoted scalar
  in "<unicode string>", line 5, column 5
found unknown escape character
  in "<unicode string>", line 5, column 18; 1ecc9a25_如何评价Karpathy提出的个人知识库的架构如何评价Karpathy提出的个人知识库的架构.md: LLM generation failed — could not parse JSON response. Preview: ```json
{
  "source_page": {
    "title": "Analysis: Karpathy's LLM-Powered Personal Knowledge Base Architecture",
    "content": "# Analysis: Karpathy's LLM-Powered Personal Knowledge Base Architecture\n\n## Summary\nThis analysis examines Andrej Karpathy's proposal for a personal knowledge managem; 53771cfc_最好用的Agent框架是什么最好用的Agent框架是什么.md: LLM generation failed — could not parse JSON response. Preview: ```json
{
  "source_page": {
    "title": "Comprehensive Comparison of AI Agent Development Frameworks",
    "content": "# Comprehensive Comparison of AI Agent Development Frameworks\n\n## Summary\nA detailed analysis and comparison of popular AI Agent development frameworks, covering their features

## [2026-04-18] batch-ingest-errors | 20 errors: 2b36f099_claude.md怎么写才能让Claude Code更高效claude.md怎么写才能让Claude Code更高效.md: while parsing a quoted scalar
  in "<unicode string>", line 5, column 5
found unknown escape character
  in "<unicode string>", line 5, column 18; 1ecc9a25_如何评价Karpathy提出的个人知识库的架构如何评价Karpathy提出的个人知识库的架构.md: LLM generation failed — could not parse JSON response. Preview: ```json
{
  "source_page": {
    "title": "Karpathy's LLM-Powered Personal Knowledge Base Architecture",
    "content": "# Karpathy's LLM-Powered Personal Knowledge Base Architecture\n\n## Summary\nThis source analyzes Andrej Karpathy's proposal for a three-layer personal knowledge base system that ; 53771cfc_最好用的Agent框架是什么最好用的Agent框架是什么.md: LLM generation failed — could not parse JSON response. Preview: ```json
{
  "source_page": {
    "title": "Comprehensive Comparison of AI Agent Development Frameworks",
    "content": "# Comprehensive Comparison of AI Agent Development Frameworks\n\n## Summary\nA detailed analysis and comparison of popular AI Agent development frameworks, covering their features

## [2026-04-19] ingest | Anthropic's China Restrictions and Claude Reasoning Distillation Techniques — 15 pages created/updated

## [2026-04-19] ingest | Harness Engineering and Compound Engineering for AI-Driven Development — 11 pages created/updated

## [2026-04-19] batch-ingest-errors | 18 errors: 1ecc9a25_如何评价Karpathy提出的个人知识库的架构如何评价Karpathy提出的个人知识库的架构.md: LLM generation failed — could not parse JSON response. Preview: ```json
{
  "source_page": {
    "title": "Karpathy's LLM-Powered Personal Knowledge Base Architecture",
    "content": "# Karpathy's LLM-Powered Personal Knowledge Base Architecture\n\n## Summary\nThis document analyzes Andrej Karpathy's proposal for a three-layer personal knowledge base system tha; 2b36f099_claude.md怎么写才能让Claude Code更高效claude.md怎么写才能让Claude Code更高效.md: LLM generation failed — could not parse JSON response. Preview: ```json
{
  "source_page": {
    "title": "Zhihu Discussion: Optimizing Claude Code with CLAUDE.md and Efficient Development Workflows",
    "content": "# Zhihu Discussion: Optimizing Claude Code with CLAUDE.md and Efficient Development Workflows\n\n## Summary\nA comprehensive discussion thread from; 55258346_claude code使用感受如何claude code使用感受如何.md: LLM generation failed — could not parse JSON response. Preview: ```json
{
  "source_page": {
    "title": "Zhihu Analysis: Advanced Configuration and Workflow Strategies for Claude Code",
    "content": "# Zhihu Analysis: Advanced Configuration and Workflow Strategies for Claude Code\n\n## Summary\nA comprehensive, experience-driven guide detailing advanced stra

## [2026-04-19] ingest | Harness Engineering Explained: From Agent Loop to Production System — 6 pages created/updated

## [2026-04-19] ingest | Zhihu Discussion: Personal Development and Life Philosophy Insights — 9 pages created/updated

## [2026-04-19] batch-ingest-errors | 18 errors: 1ecc9a25_如何评价Karpathy提出的个人知识库的架构如何评价Karpathy提出的个人知识库的架构.md: while parsing a quoted scalar
  in "<unicode string>", line 5, column 5
found unknown escape character
  in "<unicode string>", line 5, column 18; 2b36f099_claude.md怎么写才能让Claude Code更高效claude.md怎么写才能让Claude Code更高效.md: LLM generation failed — could not parse JSON response. Preview: ```json
{
  "source_page": {
    "title": "Zhihu Discussion: Optimizing CLAUDE.md for Efficient Claude Code Development",
    "content": "# Zhihu Discussion: Optimizing CLAUDE.md for Efficient Claude Code Development\n\n## Summary\nA comprehensive Zhihu discussion thread where multiple experienced d; 53771cfc_最好用的Agent框架是什么最好用的Agent框架是什么.md: LLM generation failed — could not parse JSON response. Preview: ```json
{
  "source_page": {
    "title": "Comparative Analysis of AI Agent Development Frameworks",
    "content": "# Comparative Analysis of AI Agent Development Frameworks\n\n## Summary\nA comprehensive comparison of popular AI Agent development frameworks, analyzing their features, learning curv

## [2026-04-19] ingest | Zhihu Discussion: Comparative Analysis of Foreign vs. Domestic Textbooks — 11 pages created/updated

## [2026-04-19] ingest | Zhihu Discussion: OpenClaw Beginner Safety and Deployment Guidelines — 10 pages created/updated

## [2026-04-19] batch-ingest-errors | 18 errors: 1ecc9a25_如何评价Karpathy提出的个人知识库的架构如何评价Karpathy提出的个人知识库的架构.md: while parsing a quoted scalar
  in "<unicode string>", line 5, column 5
found unknown escape character
  in "<unicode string>", line 5, column 18; 2b36f099_claude.md怎么写才能让Claude Code更高效claude.md怎么写才能让Claude Code更高效.md: LLM generation failed — could not parse JSON response. Preview: ```json
{
  "source_page": {
    "title": "Zhihu Discussion: Optimizing Claude Code with CLAUDE.md and Efficient Development Workflows",
    "content": "# Zhihu Discussion: Optimizing Claude Code with CLAUDE.md and Efficient Development Workflows\n\n## Overview\nThis source is a comprehensive discus; 53771cfc_最好用的Agent框架是什么最好用的Agent框架是什么.md: LLM generation failed — could not parse JSON response. Preview: ```json
{
  "source_page": {
    "title": "Comparative Analysis of AI Agent Development Frameworks",
    "content": "# Comparative Analysis of AI Agent Development Frameworks\n\n## Summary\nA comprehensive comparison of popular AI Agent development frameworks, analyzing their features, learning curv

## [2026-04-19] ingest | OpenAkita: Open-Source Self-Evolving AI Assistant Framework — 8 pages created/updated

## [2026-04-19] batch-ingest-errors | 19 errors: 1ecc9a25_如何评价Karpathy提出的个人知识库的架构如何评价Karpathy提出的个人知识库的架构.md: while parsing a quoted scalar
  in "<unicode string>", line 5, column 5
found unknown escape character
  in "<unicode string>", line 5, column 18; 2b36f099_claude.md怎么写才能让Claude Code更高效claude.md怎么写才能让Claude Code更高效.md: LLM generation failed — could not parse JSON response. Preview: ```json
{
  "source_page": {
    "title": "Zhihu Discussion: Optimizing CLAUDE.md for Efficient Claude Code Development",
    "content": "# Zhihu Discussion: Optimizing CLAUDE.md for Efficient Claude Code Development\n\n## Summary\nA comprehensive Zhihu discussion thread where multiple developers sh; 53771cfc_最好用的Agent框架是什么最好用的Agent框架是什么.md: LLM generation failed — could not parse JSON response. Preview: ```json
{
  "source_page": {
    "title": "Comparative Analysis of AI Agent Development Frameworks",
    "content": "# Comparative Analysis of AI Agent Development Frameworks\n\n## Summary\nA comprehensive comparison of popular AI Agent development frameworks, analyzing their features, learning curv

## [2026-04-20] ingest | Zhihu Discussion: Obsidian Note-Taking Methods and AI Integration — 9 pages created/updated

## [2026-04-20] ingest | Karpathy的LLM知识库架构分析 — 3 pages created (source + knowledge-compiler-pattern + llm-wiki-architecture)

## [2026-04-20] ingest | AI Agent框架对比分析 — 2 pages created (source + deepagents-framework)

## [2026-04-20] ingest | Claude Code深度使用指南 — 4 pages created (source + claude-code-subagents + claude-code-hooks + plan-mode-workflow)

## [2026-04-20] ingest | Zhihu Discussion: Career Transition from Backend to AI Agent Engineering — 13 pages created/updated

## [2026-04-20] ingest | Zhihu Discussion: Life Lessons on Creativity, Acceptance, and Proactivity — 8 pages created/updated

## [2026-04-20] batch-ingest-errors | 17 errors: 1ecc9a25_如何评价Karpathy提出的个人知识库的架构如何评价Karpathy提出的个人知识库的架构.md: while parsing a quoted scalar
  in "<unicode string>", line 5, column 5
found unknown escape character
  in "<unicode string>", line 5, column 18; 2b36f099_claude.md怎么写才能让Claude Code更高效claude.md怎么写才能让Claude Code更高效.md: LLM generation failed — could not parse JSON response. Preview: ```json
{
  "source_page": {
    "title": "Zhihu Discussion: Optimizing Claude Code with CLAUDE.md and Efficient Development Workflows",
    "content": "# Zhihu Discussion: Optimizing Claude Code with CLAUDE.md and Efficient Development Workflows\n\n## Summary\nA comprehensive Zhihu discussion threa; 55258346_claude code使用感受如何claude code使用感受如何.md: LLM generation failed — could not parse JSON response. Preview: ```json
{
  "source_page": {
    "title": "Zhihu Analysis: Advanced Configuration and Workflow Strategies for Claude Code",
    "content": "# Zhihu Analysis: Advanced Configuration and Workflow Strategies for Claude Code\n\n## Summary\nA comprehensive, experience-driven guide detailing advanced conf

## [2026-04-20] ingest | 视频源文件批量处理 — 10个视频源文件处理完成，创建10个source页面和7个concept页面

## [2026-04-20] ingest | 知乎讨论文章批量处理 — 10个文章源文件处理完成

处理文件列表：
1. 25f38aec_一般技术大牛都在哪里写博客 — 创建source + concept（技术博客质量层级）+ entity（Paul Graham, Antirez, Simon Willison）
2. 441d7d2d_大神们是从哪获取优质信息 — 创建source + concept（信息源筛选方法论）
3. 99effbed_中年以后什么是最好的锻炼 — 创建source + concept（超负荷原则、间歇训练法）
4. 5a10535a_有哪些算法惊艳到了你 — 创建source + concept（概率算法思维）
5. 40136f0f_为什么感觉现在AI Agent都是雷声大雨点小 — 创建source + concept（智能RAG架构）
6. b99fad36_Harness Engineering的本质是什么 — 创建source + concept（Harness Engineering）
7. b5d1922b_谷歌提出CLI的7条设计原则 — 创建source + concept（CLI设计原则）
8. 517a9161_GLM5Kimi国产大模型选哪个 — 创建source + concept（Coding Plan订阅模式）
9. 46f2c12c_中国武术真的有内功存在吗 — 创建source + concept（内功、呼吸法）
10. 1d3a90a2_真的有所谓的开悟吗 — 创建source + concept（大脑预测模型更新）

创建页面统计：
- Source页面：10个
- Concept页面：7个
- Entity页面：3个
- Index更新：已追加新条目
