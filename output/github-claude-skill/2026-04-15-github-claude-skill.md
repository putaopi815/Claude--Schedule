# 🧠 AI Skills & Agents Daily — 2026-04-15

> 时间窗口：2026-04-13 ~ 2026-04-15（优先 24h 内，补充 3 天内）
> 筛选标准：Signal > Noise / Prefer momentum / Prefer usable / 识别新模式

---

## 1. 🎨 UX / Design Focused

### 1.1 DESIGN.md + awesome-design-md

- **GitHub**: [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)（⭐ 44.5k，Fork 5.5k）
- **类型**: Tool / Protocol
- **一句话总结**: 纯 Markdown 描述设计系统，让 AI coding agent 自动生成一致的 UI
- **核心能力**: 将 Figma/设计稿中的 color、typography、spacing、component 规范压缩为一个 DESIGN.md 文件，LLM 原生可读，替代 JSON design token + Figma export 的传统 handoff
- **使用场景**: 在 Claude Code / Cursor 中放入 `DESIGN.md`，agent 自动按照 Stripe / Linear / Notion 风格生成 UI
- **为什么重要（UX 视角）**: **彻底改变 design → development handoff**。12.6% 的 fork rate 说明开发者在实际修改和使用，不是收藏。CJK 扩展（awesome-design-md-jp）已出现，生态在自发生长
- **趋势标记**: 🔥 持续爆发（3月31日发布，2周内 4.3k→44.5k stars）
- **是否值得收藏**: **Yes** — 这是 design-to-code 的新基础设施，DESIGN.md 正在成为 README.md 级别的项目标配

### 1.2 Google Stitch + stitch-skills

- **GitHub**: [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills)
- **类型**: Tool / Skill
- **一句话总结**: Google 的 AI-native 设计画布，从文本提示生成高保真 UI，并推出了 DESIGN.md 概念
- **核心能力**: 无限画布 + 上下文感知设计 agent + 即时原型生成。Stitch 是 DESIGN.md 的发起者，提供官方 skill 集合
- **使用场景**: 用自然语言描述界面需求 → Stitch 生成 5 屏原型 → 导出为 DESIGN.md → 任意 AI agent 实现
- **为什么重要（UX 视角）**: Google 正在定义 "vibe design" 范式 — 设计师用自然语言而非像素工作，AI 负责视觉实现。**Design → Development gap 被显著缩短**
- **趋势标记**: 3 天内（Stitch skills 仓库持续更新）
- **是否值得收藏**: **Yes** — 关注 Google 如何用 Stitch 定义下一代设计工具标准

---

## 2. ⚙️ GitHub Trending Agents

### 2.1 Microsoft Agent Framework 1.0

- **GitHub**: [microsoft/agent-framework](https://github.com/microsoft/agent-framework)
- **类型**: Agent Framework
- **一句话总结**: 微软将 Semantic Kernel + AutoGen 合并为统一的生产级 multi-agent 框架，4月3日发布 1.0
- **核心能力**: 多 agent 编排（sequential / concurrent / handoff / group chat / Magentic-One）、MCP + A2A 协议支持、15+ LLM provider connector、浏览器端 DevUI 调试器
- **使用场景**: 企业级 multi-agent 系统：客服流转、代码审查流水线、数据分析 pipeline
- **为什么重要**: 这是第一个 **同时支持 MCP（工具调用）和 A2A（agent 间通信）** 的生产级框架。Agent 互操作时代正式开始
- **趋势标记**: 🔥 3 天内（4月3日 GA，社区讨论高峰）
- **是否值得收藏**: **Yes** — 如果你做 multi-agent 系统，这是目前最完整的企业级选择

### 2.2 Claude Managed Agents（Public Beta）

- **文档**: [platform.claude.com/docs/en/managed-agents](https://platform.claude.com/docs/en/managed-agents/overview)
- **类型**: Agent Infrastructure / PaaS
- **一句话总结**: Anthropic 推出全托管 agent 运行时，sandboxed 执行 + 长时间会话 + 内置工具 + SSE 流
- **核心能力**: 无需自建 agent loop — session 持久化、sandbox 隔离、prompt caching、compaction、自动扩展。支持 multi-agent（research preview）
- **使用场景**: 构建能自主运行数小时的 coding agent / research agent / data pipeline agent，无需管理基础设施
- **为什么重要**: **$0.08/session-hour** 让部署 agent 的门槛降到接近零。这是 "agent-as-a-service" 模式的里程碑
- **趋势标记**: 🔥 本周爆发（4月8日 public beta）
- **是否值得收藏**: **Yes** — 对于想快速部署 production agent 的团队，这是最低摩擦的方案

### 2.3 Google ADK (Agent Development Kit)

- **GitHub**: [google/adk-python](https://github.com/google/adk-python)（⭐ 15.6k）
- **类型**: Agent Framework
- **一句话总结**: Google 的 code-first Python agent 框架，双周迭代，v1.19.0，被 2,800+ 项目采用
- **核心能力**: 模块化 agent 构建 + 评估 + 部署。优化 Gemini 但支持任意 model。code-first 设计强调可测试性和版本控制
- **使用场景**: 快速构建 multi-agent workflow，替代 LangChain/CrewAI 用于 Google 生态
- **为什么重要**: Google 的 agent 野心落地了 — ADK 是 Stitch（设计）+ Gemini（模型）+ Vertex（部署）的粘合层
- **趋势标记**: 3 天内（持续高速增长）
- **是否值得收藏**: **Yes** — Google 生态的 agent 标准入口

### 2.4 Goose → Agentic AI Foundation (AAIF)

- **GitHub**: [aaif-goose/goose](https://github.com/aaif-goose/goose)（原 block/goose，⭐ 4.9k+）
- **类型**: Agent / Tool
- **一句话总结**: Block 捐赠给 Linux Foundation 的 Rust 本地 AI agent，与 MCP 和 AGENTS.md 并列为 AAIF 基础项目
- **核心能力**: Rust 构建、15+ LLM provider、本地优先、MCP 原生支持、桌面 app + CLI + API 三形态
- **使用场景**: 本地开发环境中的通用 AI agent — 安装软件、执行测试、编辑代码、自动化工程任务
- **为什么重要**: Goose 进入 AAIF 标志着 **MCP + AGENTS.md + Goose 形成了开放 agent 基础设施三件套**，Linux Foundation 背书的开放标准
- **趋势标记**: 🔥 本周（4月7日宣布迁移至 AAIF）
- **是否值得收藏**: **Yes** — 关注 AAIF 如何定义开放 agent 标准

### 2.5 OpenClaw 2026.4.12

- **GitHub**: [openclaw/openclaw](https://github.com/openclaw/openclaw)（⭐ 351k+）
- **类型**: Agent Platform
- **一句话总结**: 史上增长最快的开源项目，日下载 50 万次的个人 AI 助手，4月12日发布质量更新
- **核心能力**: 自主浏览网页、填表、shell 命令、写代码、控制智能家居，并能自己写新 skill 扩展能力
- **使用场景**: 全能个人 AI agent — 从日程管理到代码开发到智能家居控制
- **为什么重要**: Active Memory 插件（专用记忆子 agent）代表了 agent 记忆架构的新方向。但需关注安全问题（13.5 万暴露实例）
- **趋势标记**: 24h 内（4月12日发布 v2026.4.12）
- **是否值得收藏**: **Yes（谨慎）** — 功能强大但安全风险需评估

---

## 3. 🧩 Claude Skills 生态

### 3.1 Skills 2.0 统一架构

- **文档**: [code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills)
- **变化**: Commands 和 Skills 统一 — `.claude/commands/deploy.md` 和 `.claude/skills/deploy/SKILL.md` 现在等价，都创建 `/deploy`
- **新增**: skill-creator 支持 evals — 可对 skill 运行测试 prompt 并评分
- **安装**: `npx skills add <owner/repo>` 一行搞定
- **跨平台**: SKILL.md 开放标准，兼容 Claude Code / Cursor / Codex CLI / Gemini CLI / GitHub Copilot
- **使用时机**: 当你需要封装可复用的 agent 能力（code review / deploy / design audit）时

### 3.2 SkillsMP 技能市场

- **网站**: [skillsmp.com](https://skillsmp.com)
- **规模**: 425,000+ skills，社区独立运营
- **特点**: Skills 是 model-invoked（AI 根据上下文自动决定何时使用），不同于 slash command 的 user-invoked 模式
- **使用时机**: 发现和安装社区 skill，快速扩展 agent 能力

### 3.3 Claude Code /powerup

- **版本**: v2.1.90（4月1日）
- **功能**: 交互式教程 + 动画演示，教你使用 Claude Code 高级功能
- **使用时机**: 新用户上手，或了解 agent 设计模式（tool surface 决策、context 管理、caching 策略）

---

## 4. 💡 Emerging Patterns（今日关键洞察）

### Pattern 1: DESIGN.md — 设计系统的 "Infrastructure as Code"

DESIGN.md 不只是一个文件格式，它代表一种范式转移：**设计系统从视觉工具（Figma）迁移到文本协议（Markdown）**。这意味着：
- 设计意图可以 git 版本化
- AI agent 可以原生理解设计规范
- Design review 可以像 code review 一样进行
- **设计师和开发者终于在同一个介质（文本）上工作**

👉 这是 2026 年最重要的 design-to-code 基础设施变革

### Pattern 2: Agent Infrastructure 三国演义

三大平台同时推出生产级 agent 基础设施：
- **Anthropic**: Managed Agents（全托管 PaaS）
- **Microsoft**: Agent Framework 1.0（开源 SDK + MCP/A2A）
- **Google**: ADK + Stitch（code-first + design-first）

👉 Agent 不再是 demo，而是 infrastructure。选择 agent 平台正在变成像选择云服务商一样的战略决策

### Pattern 3: 开放标准联盟成型 — AAIF

MCP（工具调用）+ AGENTS.md（agent 配置）+ Goose（参考实现）被捐赠到 Linux Foundation 的 AAIF。这标志着：
- Agent 互操作有了中立治理
- SKILL.md / DESIGN.md / AGENTS.md 构成了 agent 项目的标准文件集
- **一个项目的 "AI-readiness" 开始由这些 .md 文件定义**

### Pattern 4: Agent Memory 从附加功能变为核心架构

OpenClaw 的 Active Memory 插件将记忆实现为独立的子 agent，而非简单的 context window 管理。Claude Managed Agents 的 memory 也进入 research preview。

👉 未来的 agent 架构：**主 agent + 记忆 agent + 工具 agent** 的多 agent 协作模式

---

## 📊 今日速览表

| 项目 | 类型 | 趋势 | UX 相关 | 收藏 |
|------|------|------|---------|------|
| awesome-design-md | Protocol | 🔥 持续爆发 | ⭐⭐⭐ | ✅ |
| Google Stitch Skills | Tool | 3天内 | ⭐⭐⭐ | ✅ |
| MS Agent Framework 1.0 | Framework | 🔥 3天内 | ⭐ | ✅ |
| Claude Managed Agents | PaaS | 🔥 本周 | ⭐ | ✅ |
| Google ADK v1.19 | Framework | 3天内 | ⭐ | ✅ |
| Goose → AAIF | Agent | 🔥 本周 | ⭐ | ✅ |
| OpenClaw 2026.4.12 | Platform | 24h内 | ⭐ | ⚠️ |
| Skills 2.0 / SkillsMP | Ecosystem | 持续 | ⭐⭐ | ✅ |

---

## 🔗 Sources

- [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)
- [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills)
- [microsoft/agent-framework](https://github.com/microsoft/agent-framework)
- [Claude Managed Agents Docs](https://platform.claude.com/docs/en/managed-agents/overview)
- [google/adk-python](https://github.com/google/adk-python)
- [aaif-goose/goose](https://github.com/aaif-goose/goose)
- [openclaw/openclaw](https://github.com/openclaw/openclaw)
- [Claude Code Skills Docs](https://code.claude.com/docs/en/skills)
- [SkillsMP](https://skillsmp.com)
- [DESIGN.md Protocol](https://ossinsight.io/blog/design-md-protocol-2026)
- [OpenClaw Statistics](https://openclawvps.io/blog/openclaw-statistics)
- [MS Agent Framework 1.0 Blog](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/)
- [Google Stitch Blog](https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-ai-ui-design/)
- [Fazm - New Open Source AI April 2026](https://fazm.ai/blog/new-open-source-ai-projects-github-hugging-face-april-2026)
- [Goose moves to AAIF](https://goose-docs.ai/blog/2026/04/07/goose-moves-to-aaif/)
