# 🧠 AI Skills & Agents Daily — 2026-04-22

> 数据来源：GitHub Trending（今日）、官方发布公告、社区讨论  
> 时间约束：优先24h内，补充3天内项目

---

## 1. 🎨 UX / Design Focused

### 1.1 Figma AI Agent Canvas（MCP Write Access）
- **链接**：[figma.com/blog/the-figma-canvas-is-now-open-to-agents](https://www.figma.com/blog/the-figma-canvas-is-now-open-to-agents/)
- **类型**：Tool / MCP Integration
- **发布时间**：Open Beta 发布于 2026-03-24，4月持续活跃讨论 ⚡ 3天内
- **做什么**：通过 MCP，AI Agent（Claude Code、Codex 等）可直接在 Figma 画布上创建和编辑设计元素，使用真实组件、变量和 Auto Layout。
- **核心能力**：
  - `generate_figma_design`：将最新 UI 拉入 Figma 进行迭代
  - `use_figma`：基于设计系统创建/编辑元素
  - 自愈迭代：Agent 截图后自动检测偏差并修正
  - 与设计系统深度绑定，保证品牌一致性
- **使用场景**：产品设计师描述"首页英雄区改成深色+玻璃拟态"，Agent 直接在 Figma 中修改组件并对齐 token，无需手动拖拽。
- **为什么重要（UX视角）**：首次实现 AI 对 Figma 的写权限。过去 AI 只能"看"设计，现在可以"改"设计。**Design → Development gap 被大幅缩短**——Agent 可在设计层面直接操作，而非仅生成代码后再手动同步。
- **是否值得收藏**：✅ Yes — 这是 2026 设计工作流最重要的基础设施变化之一。

---

### 1.2 Google Stitch 2.0 + 开源 DESIGN.md
- **链接**：[stitch.withgoogle.com](https://stitch.withgoogle.com/) | [DESIGN.md 开源公告](https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-design-md/)
- **类型**：Tool / Open Standard
- **发布时间**：2026-03-19 更新，4月22日 DESIGN.md 规范持续讨论 ⚡ 3天内
- **做什么**：AI 原生无限画布设计工具，从自然语言生成最多5个屏幕的完整 UI 流，同时开放 DESIGN.md 格式规范（跨平台的设计描述标准）。
- **核心能力**：
  - "Vibe Design"：Design Agent 跨整个项目进行推理
  - 语音指令直接修改 UI
  - DESIGN.md：从任意 URL 提取设计意图，可跨工具导入
  - 免费：550 次生成/月（含 Gemini 3.0 Pro）
- **使用场景**：用一段话描述一个3步注册流程，Stitch 直接生成3个关联屏幕、可点击原型，导出 DESIGN.md 后在其他工具中继续迭代。
- **为什么重要（UX视角）**：DESIGN.md 作为开放标准意义深远——类似 OpenAPI 之于 REST API，它可能成为"设计意图的通用语言"，让 AI 在不同设计工具之间无缝协作。**Design → Dev gap 缩短信号：强。**
- **是否值得收藏**：✅ Yes — DESIGN.md 开源是新范式，值得长期跟踪。

---

### 1.3 claude-context（zilliztech）
- **链接**：[github.com/zilliztech/claude-context](https://github.com/zilliztech/claude-context)
- **类型**：MCP Tool / Skill
- **发布时间**：今日 GitHub Trending +169 stars ⚡ 24h内
- **做什么**：为 Claude Code（及其他 AI 编码 Agent）提供整个代码库的语义搜索上下文，通过 MCP 接入。
- **核心能力**：
  - 混合搜索（BM25 + 稠密向量），~40% token 节省
  - AST 级别代码切分，增量索引（Merkle tree）
  - VSCode 扩展 + MCP server 双模式
- **使用场景**：前端团队使用 Claude Code 开发时，Agent 能直接语义搜索"处理用户认证的函数"，无需手动粘贴代码片段。
- **为什么重要（UX视角）**：缩短 Dev 侧工作流中的上下文准备成本。对设计-开发协同场景：Agent 理解整个设计系统代码后，可更准确地将 Figma 设计实现为组件。
- **是否值得收藏**：✅ Yes — 今日爆发，MCP 生态中高实用性工具。

---

## 2. ⚙️ GitHub Trending Agents

### 2.1 Hermes Agent v0.10.0（NousResearch）
- **链接**：[github.com/NousResearch/hermes-agent](https://github.com/nousresearch/hermes-agent)
- **类型**：Agent Framework
- **发布时间**：2026-04-16，103k stars ⚡ 3天内活跃
- **功能**：住在你服务器上的自持续 AI Agent，具备持久记忆、自动生成技能（Skill），基于 GEPA 自改进机制（ICLR 2026 Oral），重复任务速度提升40%。
- **核心特性**：
  - 118 个预置 Skills（开发、研究、写作、数据处理等）
  - 孤立子 Agent：独立对话、终端、Python RPC
  - 多平台：Telegram/Discord/Slack/Email/CLI
  - 5 种执行后端：local/Docker/SSH/Singularity/Modal
- **使用场景**：给 Hermes 布置"每天早上汇总竞品 UI 变化"，它自动学习你的风格偏好，生成的摘要质量随时间提升。
- **是否值得收藏**：✅ Yes — 自改进机制是真实的工程突破，103k stars 验证社区认可。

---

### 2.2 MassGen v0.1.79（massgen）
- **链接**：[github.com/massgen/MassGen](https://github.com/massgen/MassGen)
- **类型**：Multi-Agent Framework
- **发布时间**：v0.1.79 发布于 2026-04-20，959 stars ⚡ 24h内
- **功能**：终端运行的多 Agent 扩展系统，协调 Claude/GPT-5/Gemini/Grok 等模型并行推理，通过共识投票得出最优答案。
- **核心特性**：
  - 并行 Agent + 实时互相批评机制
  - Trace Analyzer 子 Agent（v0.1.71+）
  - 支持 MCP、Docker、20+ AI 提供商
  - 终端 UI / Web 界面实时可视化
- **使用场景**：用多个不同模型同时分析一个复杂的 UI 可用性问题，各 Agent 互相挑战对方的结论，最终投票出最合理的改进方案。
- **是否值得收藏**：✅ Yes — 多模型共识机制是对单 Agent 的实质性超越。

---

### 2.3 Microsoft Agent Framework v1.2.0
- **链接**：[github.com/microsoft/agent-framework](https://github.com/microsoft/agent-framework)
- **类型**：Agent Framework
- **发布时间**：dotnet-1.2.0 / python-1.1.0 发布于 2026-04-21 ⚡ 24h内
- **功能**：生产级多 Agent 编排框架（统一 Semantic Kernel + AutoGen），图结构编排 + 中间件 pipeline + YAML 声明式 Agent 定义。
- **最新更新**：
  - dotnet-1.2.0：Foundry Hosted Agents 支持，workflow 单测
  - python-1.1.0：GeminiChatClient，文件历史 provider
- **使用场景**：企业级产品团队用 YAML 定义"设计审核 Agent → 代码生成 Agent → QA Agent"的流水线，Microsoft 基础设施保障生产稳定性。
- **是否值得收藏**：✅ Yes — 昨日发布，企业场景最成熟的选择之一。

---

### 2.4 RAG-Anything v1.2.10（HKUDS）
- **链接**：[github.com/HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything)
- **类型**：Workflow / Tool
- **发布时间**：v1.2.10 发布于 2026-03-24，16.9k stars
- **功能**：多模态 RAG 框架，统一处理 PDF、图片、表格、公式、图表，通过知识图谱跨模态检索。
- **使用场景**：从竞品产品手册（含截图、设计规范表格）中提取设计决策，喂给 UX 研究 Agent 做竞品分析。
- **是否值得收藏**：⭕ Conditional — 16.9k stars 有价值，但最新版本已是3月底，今日无明显增量。适合需要文档分析 Agent 的场景收藏。

---

## 3. 🧩 Claude Skills（当前生态）

### 3.1 claude-context MCP（zilliztech）
- **Skill 名称**：codebase-semantic-search
- **工作流描述**：`npx @zilliz/claude-context-mcp` 接入 Claude Code，为 Agent 提供整个代码库的语义搜索能力，减少手动粘贴代码上下文。
- **使用时机**：项目代码量超过 Claude 单次上下文窗口时；需要 Agent 精准定位特定模式代码时。

### 3.2 Figma MCP Write Skill
- **Skill 名称**：figma-agent-canvas
- **工作流描述**：通过 `use_figma` 工具，Claude Code 直接操作 Figma 画布，基于设计系统组件进行创建/修改，截图自愈迭代。
- **使用时机**：需要将自然语言设计需求直接落地到 Figma 组件时；设计-开发协同场景中减少手动操作。

### 3.3 MassGen Skills 接入
- **Skill 名称**：massgen-multi-agent
- **工作流描述**：`npx skills add massgen/skills --all` 安装后，在 Claude Code / Cursor / Copilot 中调用 MassGen 多 Agent 并行分析能力。
- **使用时机**：复杂问题需要多视角验证时；单 Agent 输出质量不稳定时。

---

## 4. 💡 Emerging Patterns（今日新范式）

### Pattern 1: Agent → Design System（写入式 AI 设计）
Figma MCP write access 标志着一个转折：AI 从"生成代码以实现设计"升级为"直接操作设计文件"。设计系统不再只是约束，而成为 Agent 的工具库。**这是 design-to-code 链路被反转的起点：code-aware design agent。**

### Pattern 2: 开放设计语言（DESIGN.md 作为 AI 设计 API）
Google Stitch 开源 DESIGN.md 格式——用自然语言描述 UI 意图的标准规范。这类似于 OpenAPI 对 REST 的意义。未来 Agent 可用 DESIGN.md 在 Figma、Stitch、Framer 之间无缝迁移设计意图，无需重新描述。

### Pattern 3: 后台自主性（Async Agent）
Hermes Agent GEPA + MassGen Trace Analyzer 均将"后台并行工作"作为核心特性。Agent 不再阻塞用户，而是异步执行长任务后主动通知。这是 AI Agent 从"工具"进化为"协作者"的关键行为模式变化。

### Pattern 4: 自改进 Agent（Memory + Skill 自生成）
Hermes Agent 的 GEPA 机制（20+ 自生成 Skill 后速度提升40%）预示：未来 Agent 将通过使用自动变得更好，而非依赖人工 prompt 优化。这对 UX 的意义：个人化的 design assistant 会随时间越来越懂你的设计语言。

### Pattern 5: 多模型共识优于单模型
MassGen 的"并行 + 互相批评 + 投票"机制，让复杂设计决策不再依赖单一模型的幻觉，而是通过多模型共识达到更高质量。这将成为高风险 AI 辅助决策的标配模式。

---

## 📊 今日信号总结

| 项目 | 类型 | 时间信号 | UX 相关度 | 推荐优先级 |
|------|------|---------|-----------|-----------|
| Figma AI Agent Canvas | MCP Tool | 3天内热议 | ⭐⭐⭐⭐⭐ | 🔴 必看 |
| Google Stitch + DESIGN.md | Tool + 开放标准 | 3天内 | ⭐⭐⭐⭐⭐ | 🔴 必看 |
| claude-context | MCP | 24h内爆发 | ⭐⭐⭐⭐ | 🟠 重要 |
| Hermes Agent v0.10 | Agent | 3天内 | ⭐⭐⭐ | 🟠 重要 |
| Microsoft Agent Framework | Framework | 24h内发布 | ⭐⭐ | 🟡 参考 |
| MassGen v0.1.79 | Multi-Agent | 24h内发布 | ⭐⭐⭐ | 🟡 参考 |
| RAG-Anything | RAG Workflow | 3天以上 | ⭐⭐ | 🟢 收藏备用 |

---

*生成时间：2026-04-22 | 数据来源：GitHub Trending、官方博客、社区讨论*
