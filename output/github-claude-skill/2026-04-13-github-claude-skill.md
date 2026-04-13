# AI Skills & Agents Daily

> **Date**: 2026-04-13 | **Focus**: UX/Design-to-Code, AI Agents, Claude Skills
> **Time Window**: Past 24h–3 days (April 10–13, 2026)

---

## 1. UX / Design Focused

### 1.1 Google Stitch — AI-Native Design Canvas (March 2026 Major Update)

- **Link**: https://stitch.withgoogle.com/
- **Type**: Tool / Platform
- **Summary**: Google 重新发布 Stitch，从文本/语音/草图生成高保真 UI，支持无限画布 + 多屏幕生成 + Design Agent。
- **Core Capability**:
  - "Vibe Design" 模式：描述业务目标即可生成 UI（不需要先画线框）
  - 一次生成最多 5 个屏幕，支持语音交互
  - Design Agent 可跨项目推理设计一致性
  - 多框架代码导出（React / Tailwind CSS）
  - `DESIGN.md` 自然语言设计系统文件，维护跨工具设计一致性
- **Use Case**: 产品经理用自然语言描述需求 → 生成可点击原型 → 导出前端代码
- **Why It Matters (UX)**: 彻底消除 "设计 → 开发" 的 gap。DESIGN.md 概念与 CLAUDE.md 类似，标志着 AI-native 设计系统的诞生。免费 550 次/月生成。
- **Trend**: 3 天内持续爆发讨论
- **Worth Saving**: **Yes** — Design-to-code 最完整的免费方案，AI-native 设计范式

### 1.2 Emergent — Full-Stack Vibe Coding Platform

- **Link**: https://emergent.sh/
- **Type**: Platform / Workflow
- **Summary**: AI-native 全栈开发平台，多 agent 协作完成 UI 设计 → 前端 → 后端 → 测试 → 部署。
- **Core Capability**:
  - 多 Agent 架构：Planning Agent / Frontend Agent / Backend Agent / Testing Agent / Deployment Agent
  - 支持 100 万 token 上下文
  - 自然语言描述 → 完整可运行应用
- **Use Case**: 设计师描述产品概念 → 自动生成带后端的完整应用
- **Why It Matters (UX)**: 将设计 → 开发 → 部署 全链路压缩为一次对话。5M+ 用户，$50M ARR 验证了 vibe coding 模式可行。
- **Trend**: 持续增长（$300M 估值，SoftBank + Khosla 投资）
- **Worth Saving**: **Yes** — 多 Agent 协作的 design-to-deploy 范式

---

## 2. GitHub Trending Agents

### 2.1 Hermes Agent v0.8.0 — The Agent That Grows With You

- **Link**: https://github.com/NousResearch/hermes-agent
- **Type**: Agent Framework
- **Summary**: NousResearch 出品的自进化 Agent，会记忆、构建可复用 skill、随使用越来越智能。
- **Core Capability**:
  - 内置学习循环（唯一真正自进化的开源 agent）
  - 后台任务自动通知（notify_on_complete）
  - 实时模型切换 / MCP OAuth 2.1 支持
  - 支持 Matrix / Discord / Signal / Mattermost 多平台
- **Use Case**: 长期使用的个人 AI 助手，随使用自动积累能力
- **Why It Matters**: v0.8.0 于 4/8 发布（209 PRs, 82 issues），GitHub 61k stars，trending #3。"会成长的 Agent" 是全新设计模式。
- **Trend**: **24h–3 天内爆发** (v0.8.0 刚发布)
- **Worth Saving**: **Yes** — 自进化 Agent 范式的标杆

### 2.2 Microsoft Agent Framework 1.0

- **Link**: https://github.com/microsoft/agent-framework
- **Type**: Agent Framework
- **Summary**: 微软将 Semantic Kernel + AutoGen 合并为统一的生产级 Agent 框架，支持 .NET 和 Python。
- **Core Capability**:
  - 多 Agent 编排模式：Sequential / Concurrent / Handoff / Group Chat / Magentic-One
  - DevUI 浏览器调试器：可视化 agent 执行、消息流、tool 调用
  - 全模式支持 streaming / checkpointing / human-in-the-loop / pause-resume
  - 稳定 API + 长期支持承诺
- **Use Case**: 企业级多 Agent 应用开发（客服系统 / 自动化流程 / 数据分析）
- **Why It Matters**: 4/3 发布 1.0 正式版。结束了 Semantic Kernel vs AutoGen 的割裂局面。企业 Agent 开发的事实标准。
- **Trend**: **3 天内** (4/3 正式发布 GA)
- **Worth Saving**: **Yes** — 企业级 Multi-Agent 的首选框架

### 2.3 Goose — 通用 AI Agent（已捐赠 Linux Foundation）

- **Link**: https://github.com/aaif-goose/goose
- **Type**: Agent
- **Summary**: Block 出品的通用 AI Agent，Rust 构建，支持 15+ LLM 提供商，不仅限于代码。
- **Core Capability**:
  - Desktop App + CLI + API 三端覆盖
  - 支持 Anthropic / OpenAI / Google / Ollama / Azure / Bedrock 等 15+ 提供商
  - 可用于代码、研究、写作、自动化、数据分析
  - 4/7 捐赠给 Agentic AI Foundation（与 MCP、AGENTS.md 同属）
- **Use Case**: 通用工程自动化 — 安装、执行、编辑、测试的全流程 agent
- **Why It Matters**: 加入 Linux Foundation AAIF 意味着 MCP + AGENTS.md + Goose 成为 Agent 基础设施三件套。
- **Trend**: **24h–3 天内** (4/7 宣布捐赠)
- **Worth Saving**: **Yes** — Agent 基础设施标准化的重要信号

### 2.4 Caveman — Claude Code Token 削减 65% 的 Skill

- **Link**: https://github.com/JuliusBrussee/caveman
- **Type**: Claude Skill
- **Summary**: 让 Claude Code 像"穴居人"说话，削减 65%–75% 输出 token，保持完整技术准确性。
- **Core Capability**:
  - 平均削减 65% 输出 token（最高 87%）
  - 代码块、错误信息、技术术语完全不变
  - 一行安装：`npx skills add JuliusBrussee/caveman`
- **Use Case**: Claude Code 重度用户降低 API 成本
- **Why It Matters**: Hacker News 883 points / 361 comments，GitHub 5k+ stars。揭示了 "prompt-level cost optimization" 这一新模式 — 不改模型、不降质量、只优化表达方式。
- **Trend**: **3 天内爆发**（HN #1 + GitHub #1 trending）
- **Worth Saving**: **Yes** — Skill 设计的经典案例，成本优化新思路

---

## 3. Claude Skills & Ecosystem

### 3.1 Superpowers — Agent Skill 框架 & 开发方法论

- **Link**: https://github.com/obra/superpowers
- **Type**: Skill Framework / Methodology
- **Summary**: 为 AI coding agent 设计的模块化 skill 框架和软件开发方法论，强制执行最佳实践。
- **Core Capability**:
  - 可组合 Skill 系统：brainstorming → git-worktrees → writing-plans → TDD
  - 强制 RED-GREEN-REFACTOR 方法论
  - 任务拆解为 2–5 分钟的原子任务，含精确文件路径
  - 144k+ GitHub stars
- **Use Case**: 团队统一 AI 辅助开发流程，确保 agent 遵循工程最佳实践
- **When to Use**: 当需要 AI agent 做严肃工程（不是快速原型）时

### 3.2 VoltAgent/awesome-agent-skills — 跨平台 Skill 合集

- **Link**: https://github.com/VoltAgent/awesome-agent-skills
- **Type**: Skill Directory
- **Summary**: 1000+ 精选 Agent Skills，兼容 Claude Code / Codex / Gemini CLI / Cursor 等全平台。
- **Core Capability**:
  - 官方 Skills（Anthropic / Google / Vercel / Stripe / Cloudflare / Figma 等出品）
  - 社区贡献 + 人工审核（非 AI 生成）
  - 通用 SKILL.md 格式
- **Use Case**: 发现和安装适合自己工作流的 Agent Skills
- **When to Use**: 寻找特定领域 Skill 时的首选检索入口

### 3.3 "Seeing Like an Agent" — Anthropic 工具设计哲学

- **Link**: https://claude.com/blog/seeing-like-an-agent
- **Type**: Engineering Blog (4/10 发布)
- **Summary**: Anthropic 工程师 Thariq Shihipar 详述 Claude Code 的工具设计原则。
- **Key Insights**:
  - **Progressive Disclosure**: 让 agent 按需发现工具，而不是预加载全部
  - **Tool Search**: 按需工具发现机制（像搜索引擎一样检索工具）
  - Claude Code 维持约 20 个核心工具，新增门槛极高
  - 子 Agent 模式：为特定任务（如文档搜索）启动独立 context 的 subagent
- **When to Use**: 设计 MCP Server / 自定义工具 / Skill 时必读

---

## 4. Emerging Patterns（关键洞察）

### Pattern 1: DESIGN.md — AI-Native 设计系统

Google Stitch 引入 `DESIGN.md`（自然语言设计规范文件），与 `CLAUDE.md`、`AGENTS.md` 并列，标志着 **AI-native 文件协议** 正在覆盖软件开发全链路：
- `CLAUDE.md` → 代码行为规范
- `AGENTS.md` → Agent 协作规范
- `DESIGN.md` → 设计系统规范

**影响**: 设计师和开发者共享同一套自然语言规范，design-to-code 的 gap 从 "工具层" 消失提升到 "规范层" 消失。

### Pattern 2: Self-Evolving Agent（自进化 Agent）

Hermes Agent 的 "built-in learning loop" 代表 Agent 从 "一次性任务执行" 进化到 "持续学习 + skill 积累"。这是 2026 年最重要的 Agent 架构变化：
- Agent 不仅完成任务，还记住方法
- 可复用 Skills 自动生成
- 用户使用越多，Agent 越强

### Pattern 3: Prompt-Level Cost Engineering

Caveman Skill 证明了 "不改模型、不降质量、只优化输出格式" 就能削减 65%+ 成本。这是一个被忽视的优化维度：
- 成本优化不再只是 model routing / caching
- Skill 层面的 prompt engineering 成为新的效率杠杆

### Pattern 4: Agent 基础设施标准化

Goose + MCP + AGENTS.md 同时进入 Linux Foundation AAIF，标志着 Agent 基础设施正在标准化：
- MCP = Agent ↔ 外部系统的协议层
- AGENTS.md = Agent 行为规范
- Goose = 参考实现
- 这是 Agent 生态的 "HTTP + HTML + Browser" 时刻

### Pattern 5: Multi-Agent 编排走向生产

Microsoft Agent Framework 1.0 GA 意味着 Multi-Agent 从实验走向生产：
- 5 种编排模式标准化（Sequential / Concurrent / Handoff / Group Chat / Magentic-One）
- DevUI 可视化调试
- 企业级 checkpoint + human-in-the-loop

---

## Summary

| # | Project | Type | Signal | Worth Saving |
|---|---------|------|--------|--------------|
| 1 | Google Stitch (Major Update) | Design Tool | 3 天内持续爆发 | Yes |
| 2 | Emergent | Platform | 持续增长 | Yes |
| 3 | Hermes Agent v0.8.0 | Agent | 24h–3 天 (4/8 发布) | Yes |
| 4 | Microsoft Agent Framework 1.0 | Framework | 3 天内 (4/3 GA) | Yes |
| 5 | Goose → AAIF | Agent | 24h–3 天 (4/7 捐赠) | Yes |
| 6 | Caveman Skill | Claude Skill | 3 天内 (HN #1) | Yes |
| 7 | Superpowers | Skill Framework | 持续活跃 | Yes |
| 8 | awesome-agent-skills | Directory | 持续更新 | Yes |

---

> **Today's Verdict**: UX 领域 Google Stitch 的 DESIGN.md + Vibe Design 是最值得关注的范式变化。Agent 领域 Hermes Agent 的自进化模式和 Microsoft Agent Framework 1.0 GA 标志着 Agent 从玩具走向生产。Caveman Skill 作为 "prompt-level cost engineering" 的案例价值远超其本身。

---

*Sources*:
- [Google Stitch](https://stitch.withgoogle.com/)
- [Hermes Agent](https://github.com/NousResearch/hermes-agent)
- [Microsoft Agent Framework](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/)
- [Goose / AAIF](https://github.com/aaif-goose/goose)
- [Caveman](https://github.com/JuliusBrussee/caveman)
- [Superpowers](https://github.com/obra/superpowers)
- [awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)
- [Emergent](https://emergent.sh/)
- [Seeing Like an Agent](https://claude.com/blog/seeing-like-an-agent)
