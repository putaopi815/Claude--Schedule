# 🧠 AI Skills & Agents Daily — April 12, 2026

> 每日精选最新 AI Skills、Agents 和可复用 Workflow，聚焦 UX/产品设计 + Agent 生态。
> 数据窗口：2026-04-10 ~ 2026-04-12（优先 24h 内，补充 3 天内）

---

## 1. 🎨 UX / Design Focused

### Flowstep — AI 原生设计画布，直出 React 代码
- **类型**: Tool / Workflow
- **做什么**: 用自然语言描述产品想法，在无限画布上生成完整用户流（登录、仪表盘、设置页），一键导出 React + TypeScript + Tailwind CSS 生产级代码，或直接 ⌘C/⌘V 粘贴到 Figma。
- **核心能力**: 消除「设计稿 → 前端代码」的翻译损耗，设计与代码 1:1 匹配。
- **使用场景**: 产品经理快速出交互原型 → 设计师在 Figma 微调 → 工程师直接使用导出代码。
- **为什么重要（UX 视角）**: 彻底缩短 design → development gap。设计师不再「画图给开发看」，而是直接产出可用代码。实时协作 + 无限画布意味着团队可以在同一个面上完成从概念到实现。
- **趋势标记**: 3 天内持续活跃，社区讨论增长
- **是否值得收藏**: **Yes** — 当前最接近「设计即开发」的 AI 工具之一
- 🔗 [flowstep.ai](https://flowstep.ai/)

### Google Stitch 2.0 — DESIGN.md 格式引领设计元数据标准化
- **类型**: Tool
- **做什么**: Google 的 AI 原生设计画布，支持文本/语音/草图生成 UI，March 2026 大更新引入 DESIGN.md 自然语言文件格式，可从任意 URL 提取界面设计细节并跨项目导入。
- **核心能力**: 语音驱动的「vibe design」、多屏同时生成、Gemini 3.0 驱动。
- **使用场景**: 用语音描述产品 → Stitch 生成 5 个屏幕的完整流程 → 导出 HTML/CSS 或粘贴到 Figma。
- **为什么重要（UX 视角）**: DESIGN.md 是一种全新的设计元数据格式，可能成为 AI 时代的「设计系统交换协议」。语音 + AI 画布 = 0 门槛设计。
- **趋势标记**: 3 天内（April 2026 持续迭代中，DESIGN.md 为新特性）
- **是否值得收藏**: **Yes** — 免费、Google 支持、DESIGN.md 是新范式信号
- 🔗 [stitch.withgoogle.com](https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-ai-ui-design/)

### VoltAgent/awesome-design-md — DESIGN.md 设计系统合集（GitHub 史上增速最快 awesome list）
- **类型**: Tool / Design Protocol
- **GitHub**: [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) ⭐ 35k（10 天内）
- **做什么**: 从 59 个知名网站提取完整设计系统规范为 DESIGN.md 文件，供 AI coding agent 生成一致 UI。涵盖色彩、排版、组件状态、设计哲学。
- **核心能力**: 解决 AI 生成代码「功能正确但 UI 通用」的根本问题。一个 DESIGN.md 让 agent 拥有人类设计师的设计上下文。
- **使用场景**: 在 Claude Code / Cursor 项目中放入 DESIGN.md → agent 自动生成符合品牌设计语言的 UI 组件。
- **为什么重要（UX 视角）**: Markdown 正在成为人类、设计、AI agent 之间的通用协议。设计师交付物从 Figma 转向 Markdown 规范，agent 直接消费设计意图而非像素。
- **趋势标记**: **3 天内持续爆发** — 10 天 35K stars + 4.4K forks，GitHub 史上最快 awesome list
- **是否值得收藏**: **Yes** — 2026 年 4 月最重要的 UX × AI 趋势，定义了设计与代码之间的新协议层

### ui-ux-pro-max-skill — 最流行的 AI 设计 Skill（v2.0 Design System Generator）
- **类型**: Claude Skill
- **GitHub**: [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) ⭐ 55.8k
- **做什么**: 为 Claude Code / Cursor / Windsurf 等 10+ 工具提供设计智能——50+ 风格、161 色板、57 字体搭配、99 UX 指南、25 图表类型。
- **核心能力**: v2.0 旗舰 Design System Generator — AI 推理引擎分析项目需求，秒级生成完整设计系统。
- **使用场景**: 新项目启动 → `uipro init --ai claude` → 秒级获得完整设计规范 + 组件风格指南，覆盖 React/Next.js/Vue/Svelte/Flutter 等 10 个框架。
- **为什么重要（UX 视角）**: 将「选字体配色彩」的设计决策从人工 2-3 天压缩到秒级，最成熟的 AI 设计 Skill 生态。
- **趋势标记**: 持续热门（社区最受欢迎的 UI/UX 设计 Skill）
- **是否值得收藏**: **Yes** — 如果只装一个设计 Skill，就选这个

---

## 2. ⚙️ GitHub Trending Agents

### Hermes Agent v0.8.0 — 自我进化的 AI Agent
- **类型**: Agent Framework
- **GitHub**: [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) ⭐ 58.4k
- **功能**: 完成任务后自动将解决路径提炼为可复用 Skill 文件存入 SQLite，未来遇到相似任务时 ~10ms 延迟检索已有 Skill。v0.8.0（4/8 发布）当天暴涨 6,400+ stars。
- **使用场景**: 需要 agent 在多次使用中「越来越聪明」的场景——运维自动化、重复性研发任务、数据处理流水线。
- **为什么重要**: 这是「自进化 agent」模式的标杆实现。不是静态技能，而是 agent 自我生成 + 自我优化技能。模型无关（支持 OpenRouter 200+ 模型）。
- **趋势标记**: **24h 内爆发** — v0.8.0 发布引发单日 6.4k star 增长，2 个月内从 0 到 58k stars
- **是否值得收藏**: **Yes** — 代表 agent 设计的下一个方向：自主学习

### Caveman — 用 65% 更少的 token 完成同样的事
- **类型**: Claude Code Skill
- **GitHub**: [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) ⭐ ~5k
- **功能**: 一个 CLAUDE.md Skill，指示 Claude Code「像穴居人一样说话」——去掉冠词、跳过客套、保留技术术语和代码。实测平均节省 65% output tokens，最高 87%。
- **使用场景**: 高频使用 Claude Code 的开发者，需要降低 API 成本和减少上下文消耗。
- **为什么重要**: 揭示了一个反直觉的洞察：**约束 LLM 的表达反而提升准确性**（ICLR 论文证实）。同时，这是最轻量的 Skill 示例——一个 .md 文件就能改变 agent 行为。
- **趋势标记**: **3 天内爆发** — HN 883 points + 361 评论，本周最热 Skill
- **是否值得收藏**: **Yes** — 实用性极高，且揭示了 Skill 设计的极简范式

### Superpowers — 编码 Agent 的完整工作流框架
- **类型**: Agent Skill Framework
- **GitHub**: [obra/superpowers](https://github.com/obra/superpowers/) ⭐ 121k
- **功能**: 为 AI 编码 agent 提供 7 阶段标准化软件开发工作流（头脑风暴 → Git Worktree → 计划 → TDD → 实现 → 验证 → 提交），每个阶段以可组合的 Skill 形式封装。
- **使用场景**: 让 Claude Code / 其他编码 agent 像高级工程师一样工作：先思考再动手，强制 TDD，自动隔离分支。
- **为什么重要**: 将软件工程最佳实践编码为 agent 可消费的格式。使用者报告测试覆盖率从 30-50% 提升到 85-95%。
- **趋势标记**: 3 天内持续增长（4/10 相关文章爆发）
- **是否值得收藏**: **Yes** — 最成熟的「agent 工程方法论」实现

### Microsoft Agent Framework 1.0 — 企业级 Multi-Agent + MCP
- **类型**: Agent Framework
- **GitHub**: [microsoft/agent-framework](https://github.com/microsoft/agent-framework)
- **功能**: 4/3 正式发布 1.0，支持 .NET + Python，内置 MCP 工具发现与调用、A2A 跨框架 agent 协作、DevUI 浏览器调试器可视化 agent 执行流。
- **使用场景**: 企业需要在 .NET/Python 生态中构建生产级多 agent 系统，同时需要与 MCP 工具生态和其他 agent 框架互操作。
- **为什么重要**: 微软正式入场 agent 基础设施，MCP + A2A 的双协议支持意味着 agent 互操作标准正在收敛。
- **趋势标记**: 3 天内（4/3 发布后持续关注，4/10 Dev Community 报道）
- **是否值得收藏**: **Yes** — 企业级首选，MCP 生态关键节点

### Archon — 首个开源 AI Coding Harness Builder（YAML 定义确定性工作流）
- **类型**: Workflow Engine / Agent Harness
- **GitHub**: [coleam00/Archon](https://github.com/coleam00/Archon) ⭐ 15.6k
- **功能**: 4/7 完成 TypeScript 全面重写。通过 YAML 定义 AI coding 工作流（planning → implementation → validation → code review → PR creation），将裸 LLM 代码的 6.7% PR 接受率提升至 ~70%。
- **使用场景**: 团队标准化 AI coding 流程 → 定义 YAML 工作流 → 多项目复用 → agent 在验证门控内自动执行。
- **为什么重要**: 代表「从 prompt engineering 到 harness engineering」的范式转移。控制 AI coding 质量的核心不再是 prompt，而是工作流骨架。
- **趋势标记**: **24h 内持续爆发** — GitHub Trending #2，4/7 重写后日增长爆炸
- **是否值得收藏**: **Yes** — Harness Engineering 新范式的标杆实现

### Multica — 开源 Managed Agents 平台（Agent 变队友）
- **类型**: Agent Platform
- **GitHub**: [multica-ai/multica](https://github.com/multica-ai/multica)
- **功能**: 将 coding agent 变成真正的「团队成员」——assign GitHub Issue 给 agent → 自动接单、写代码、报告阻塞、更新状态。支持 Claude Code / Codex / OpenClaw / OpenCode。
- **使用场景**: 人 + AI 混合团队：agent 出现在项目看板上，有 profile、发 comment、创建 issue、主动报告 blockers。
- **为什么重要**: 从「人使用 AI 工具」到「AI 作为团队正式成员」的本质转变。团队规模定义从 N 人 → N 人 + M agent。
- **趋势标记**: **3 天内活跃** — v0.1.8/v0.1.9 4 月初密集更新
- **是否值得收藏**: **Yes** — 目前最完整的开源 managed agents 方案

---

## 3. 🧩 Claude Skills

### last30days-skill — 跨平台趋势研究 Agent
- **Skill 名称**: last30days-skill
- **GitHub**: [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)
- **工作流描述**: 输入任意话题 → 并行搜索 Reddit、X、YouTube、HN、Polymarket、GitHub → AI 裁判综合评分 → 输出一份基于真实社区信号（upvotes、likes、交易量）的趋势摘要。首次运行启动设置向导，30 秒解锁所有源。
- **使用时机**: 产品立项前的市场调研、竞品分析、技术选型决策。
- **是否值得收藏**: **Yes** — 将「人肉刷社区」自动化为一个 Skill 调用

### Antigravity Awesome Skills — 1,370+ Agent Skills 库
- **Skill 名称**: antigravity-awesome-skills
- **GitHub**: [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) ⭐ 10.9k
- **工作流描述**: 可搜索、可安装的 SKILL.md 目录，支持 Claude Code / Cursor / Codex CLI / Gemini CLI 等 10+ 工具。`npx antigravity-awesome-skills` 一键安装，支持 bundles 和 workflows。
- **使用时机**: 需要快速为 agent 添加新能力时，先在这里搜索现有 Skills，避免重复造轮子。
- **是否值得收藏**: **Yes** — agent 时代的「npm registry」，技能发现的入口

### Google LiteRT-LM — 边缘设备 LLM 推理引擎
- **GitHub**: [google-ai-edge/LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM)
- **工作流描述**: 跨平台（Android/iOS/Web/Desktop/IoT）高性能 LLM 推理框架，支持 GPU/NPU 加速、工具调用（function calling）、多模态输入。
- **使用时机**: 需要在移动端/边缘设备运行 AI agent 的 UX 场景（离线设计助手、本地化语音交互）。
- **趋势标记**: 3 天内（4/8 正式开源，GitHub Trending 上榜）
- **是否值得收藏**: **Yes** — 端侧 agent 的基础设施，UX 产品的离线能力关键

### Claude Code v2.1.89–v2.1.92 — 4 月密集更新（MCP 500K / /powerup / 成本分析）
- **类型**: Platform Update
- **核心变更**:
  - **MCP 500K** — tool result 上限提升到 500,000 字符，大文件/数据库输出不再被截断
  - `/powerup` — 交互式学习系统，动画演示教学 Claude Code 功能
  - **Permission Deferral** — PreToolUse hook 新增 "defer" 选项，支持暂停等待外部信号
  - **Write tool 优化** — 大文件 diff 计算性能提升约 60%
  - `/cost` — 新增按模型和 cache-hit 的成本分析
- **使用时机**: 所有 Claude Code 用户应升级到 v2.1.92，MCP 500K 对重度 MCP 用户尤其关键

### oh-my-codex (OMX) v0.12.1 — Codex CLI 的增强编排层
- **GitHub**: [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) ⭐ 2.9k
- **工作流描述**: 给 Codex CLI 加上 hooks、agent teams、HUD 可视化 — 类似 "oh-my-zsh for AI coding"。v0.12.1（4/7）新增原生 Codex hooks、tmux 多 agent 并行、结构化工作流（autopilot / TDD / code review）。
- **使用时机**: 使用 OpenAI Codex CLI 且需要多 agent 编排和可视化监控时。

### everything-claude-code (ECC) — Claude Code 最全配置框架
- **GitHub**: [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) ⭐ 100k+
- **工作流描述**: 30 个专用 agent、136 个 skills、60 个 slash commands、自动化 hook 工作流。本周周增长 +19,869 stars，持续 #1。
- **使用时机**: 想要 Claude Code「开箱即战力」的开发者，一键获得完整 agent harness 配置。

---

## 4. 💡 Emerging Patterns（本周关键新范式）

### 🔄 Pattern 1: Self-Evolving Agents（自进化 Agent）
Hermes Agent 的 v0.7/v0.8 定义了一个新模式：agent 不只是执行任务，还会在每次任务后**自动生成可复用 Skill**，并在未来任务中优先检索已有 Skill。这不是 RAG，而是 agent 自主构建自己的「能力库」。配合 DSPy + GEPA（ICLR 2026 Oral），实现了 Skill 级别的自动优化。

**对 UX 的意义**: 未来的设计工具可能不需要「插件市场」——agent 会自动学会你的设计规范和偏好。

### 🪨 Pattern 2: Constraint-Driven Performance（约束即增强）
Caveman Skill 证明了：**限制 LLM 的输出格式反而提升了任务准确性**。这呼应了 ICLR 2026 论文「Brevity Constraints Reverse Performance Hierarchies」的发现。这意味着 Skill 设计不只是「告诉 agent 做什么」，更是「约束 agent 如何表达」。

**对 UX 的意义**: 极简约束（如「只输出 diff」「只回答 yes/no」）可能是提升 AI 产品用户体验的低成本高回报手段。

### 📐 Pattern 3: DESIGN.md — 设计的版本化与可编程化
Google Stitch 引入 DESIGN.md 格式，用自然语言描述界面设计细节，可从 URL 提取、跨项目导入。这预示着：**设计决策正在变成代码一样的可版本化、可 diff、可 agent 消费的资产**。

**对 UX 的意义**: 设计系统从「Figma 组件库」进化为「可被 agent 读取和执行的规范文件」，design-to-code 的中间层正在标准化。

### 🔗 Pattern 4: MCP + A2A 协议收敛
Microsoft Agent Framework 1.0 同时支持 MCP（工具调用）和 A2A（agent 间协作），MCP 月下载量突破 9,700 万次。v2.1 新增 Server Cards，让 MCP 服务可被自动发现。

**对 UX 的意义**: 设计工具（Figma）、开发工具（IDE）、部署平台之间的 agent 互操作正在变得标准化——这是「AI-native 设计工作流」的基础设施层。

### 🏗️ Pattern 5: Harness Engineering 取代 Prompt Engineering
Archon 和 Superpowers 代表的趋势——**控制 AI coding 质量的核心不再是 prompt，而是 harness（工作流骨架）**。YAML 定义验证门控、阶段划分、回归检查，agent 在框架内填充智能。裸 LLM PR 接受率 6.7% → harness-driven ~70%。

**对 UX 的意义**: 设计工作流也需要同样的「harness 化」——不是让 agent 自由发挥，而是定义「设计评审 → 组件拆分 → 代码生成 → 视觉回归测试」的确定性管道。

### 🤝 Pattern 6: Agent-as-Teammate（Agent 即队友）
Multica 将 agent 放进项目管理看板，assign issue → 自动执行 → 汇报阻塞。这不是「AI 辅助」，而是 **agent 作为团队正式成员**参与协作。团队规模的定义将从「N 个人」变为「N 个人 + M 个 agent」。

**对产品团队的影响**: 项目管理工具需要适配 agent 角色，设计评审流程需要考虑 agent 参与者。

---

## 📊 本日信号总结

| # | 项目 | 类型 | 趋势 | UX 相关度 | 收藏 |
|---|------|------|------|-----------|------|
| 1 | awesome-design-md | Protocol | 🚀 10天35K stars | ⭐⭐⭐⭐⭐ | ✅ |
| 2 | Flowstep | Design Tool | 🔥 活跃 | ⭐⭐⭐⭐⭐ | ✅ |
| 3 | Google Stitch 2.0 | Design Tool | 🔥 迭代中 | ⭐⭐⭐⭐⭐ | ✅ |
| 4 | ui-ux-pro-max-skill | Skill | 📈 55.8K stars | ⭐⭐⭐⭐⭐ | ✅ |
| 5 | Hermes Agent v0.8 | Agent | 🚀 爆发 | ⭐⭐⭐ | ✅ |
| 6 | Archon | Harness | 🚀 Trending #2 | ⭐⭐⭐ | ✅ |
| 7 | Multica | Platform | 🔥 活跃更新 | ⭐⭐⭐ | ✅ |
| 8 | Caveman | Skill | 🚀 HN 爆发 | ⭐⭐ | ✅ |
| 9 | Superpowers | Framework | 📈 增长 | ⭐⭐⭐ | ✅ |
| 10 | MS Agent Framework | Framework | 📈 v1.0发布 | ⭐⭐⭐ | ✅ |
| 11 | last30days-skill | Skill | 📈 活跃 | ⭐⭐ | ✅ |
| 12 | Antigravity Skills | Skill Registry | 📈 增长 | ⭐⭐ | ✅ |
| 13 | LiteRT-LM | Infra | 🆕 开源 | ⭐⭐⭐ | ✅ |

---

> **今日一句话**: Agent 正在从「执行工具」进化为「自我学习的伙伴」，而设计资产正在从「视觉文件」进化为「可编程规范」——两者的交汇点，就是下一代 AI-native 产品设计的起点。
