# 🧠 AI Skills & Agents Daily — 2026-07-01

> **Date**: 2026-07-01
> **Time Window**: 过去 24h（优先）/ 3 天内（补充）
> **Sources Checked**: GitHub Trending / Anthropic Releasebot / Google Labs / OSSInsight / startupcorners.com / opendatascience.com
> **Dedup Check**: ✅ 已对比最近历史报告（LangGraph v1.2 / Claude Managed Agents / mattpocock/skills / OpenHuman 已在上期收录，本期不重复）

---

## 1. 🎨 UX / Design Focused

### 1.1 google-labs-code/design.md — DESIGN.md 规范：让 AI Agent 真正"读懂"设计系统

- **链接**：[github.com/google-labs-code/design.md](https://github.com/google-labs-code/design.md)
- **类型**：Design System Standard / Design-to-Code / Agent Context Protocol
- **发布时间**：🟡 3天内 — Google Stitch 团队近期发布，社区快速扩散
- **做什么**：DESIGN.md 是一个纯文本格式规范，用于向 AI Coding Agent 描述项目的视觉身份（颜色系统、排版、间距、组件风格、品牌语气）。Agent 读取 DESIGN.md 后，可在整个代码库中生成风格一致的 UI，无需反复在 prompt 中重复设计约束。
- **核心能力**：
  - 一次定义，全局生效：将设计 token、品牌色、字体层级写入 DESIGN.md，所有 AI 生成的组件自动遵循
  - 跨 Agent 兼容：与 Claude Code、Cursor、Copilot、Gemini CLI 等主流 AI 编码工具兼容
  - 结构化设计语言：将设计师的意图转化为 Agent 可解析的结构，消除"AI 生成的 UI 风格飘移"问题
- **使用场景**：将 Figma 设计规范提炼为 DESIGN.md，放入项目根目录。此后要求 Claude Code "新建一个订单详情页"，Agent 自动读取品牌色、圆角规范、按钮层级，生成的代码无需人工再纠正视觉风格。
- **为什么重要（UX视角）**：这是 **design-to-code gap 缩短的关键基础设施升级**。此前 AI 生成代码最大的痛点之一是视觉一致性无法保证。DESIGN.md 将"品牌语言"首次标准化为 Agent 可直接消费的上下文，Design → Dev 自动化从"功能可用"迈向"视觉可信"。Google 的背书加速了这一标准的社区采纳速度。
- **是否值得收藏**：✅ Yes — UX 工程师必须关注。这是 2026 年 design-to-code 链路中最重要的范式级变化之一，预计很快成为各 AI Coding 工具的原生支持目标。

---

### 1.2 VoltAgent/awesome-design-md — 主流品牌设计系统的 DESIGN.md 开箱即用库

- **链接**：[github.com/voltagent/awesome-design-md](https://github.com/voltagent/awesome-design-md)
- **类型**：Design System Resource / Design-to-Code Toolkit
- **发布时间**：🟡 3天内 — 随 DESIGN.md 规范热度同步爆发
- **做什么**：收录主流品牌设计系统（如 Material Design、Tailwind、shadcn/ui 等）的高质量 DESIGN.md 文件。开发者将对应文件复制到项目中，即可让 AI Agent 立刻生成匹配该品牌设计语言的 UI 组件。
- **核心能力**：
  - 开箱即用：无需从零写 DESIGN.md，直接借用知名品牌的设计规范
  - 降低入门门槛：产品经理或前端开发无需系统学习设计规范，Agent 代劳
  - 社区共建：仓库持续吸引社区贡献更多品牌的 DESIGN.md 文件
- **使用场景**：快速原型阶段选用 shadcn/ui 的 DESIGN.md，让 Claude Code 在 3 分钟内生成视觉一致的 Dashboard 原型，大幅压缩 design → prototype 时间。
- **为什么重要（UX视角）**：与 google-labs-code/design.md 形成生态闭环，前者是规范，后者是内容库。两者结合意味着 **"从零到品牌一致 UI"的链路首次可以完全由 AI 自动完成**。
- **是否值得收藏**：✅ Yes — 快速原型设计的效率神器，与 DESIGN.md 规范一起收藏使用。

---

## 2. ⚙️ GitHub Trending Agents

### 2.1 bytedance/deer-flow v2.0 — 字节跳动开源超级 Agent，v2.0 登顶 GitHub Trending

- **链接**：[github.com/bytedance/deer-flow](https://github.com/bytedance/deer-flow)
- **类型**：Super Agent / Multi-Agent Orchestration / Long-Horizon Tasks
- **发布时间**：🟡 3天内 — v2.0 发布后登顶 GitHub Trending #1
- **功能**：DeerFlow 是字节跳动开源的长链路超级 Agent 框架，v2.0 重点解决长 Agent Workflow 的五大痛点：记忆弱、任务分解混乱、工具调用脆弱、状态不透明、失败后无法恢复。新版本引入子 Agent 编排、持久化记忆、安全沙箱执行和可扩展 Skills 系统。
- **核心特性**：
  - 子 Agent 分工：研究 / 代码生成 / 内容创作各自由专门 Agent 负责，主 Agent 负责任务分解与汇总
  - 持久化记忆：跨会话保留上下文，支持长期项目状态管理
  - 可扩展 Skills：类似 Claude Code Skills，支持按领域安装技能包
  - 失败恢复：单个子 Agent 失败后自动重试或降级，不中断整体 workflow
- **使用场景**：产品团队使用 DeerFlow 执行"竞品分析 → 功能规格生成 → 原型描述 → 技术方案评估"完整链路，每个阶段由专属子 Agent 完成，主 Agent 汇总结果并生成最终报告。
- **是否值得收藏**：✅ Yes — v2.0 解决了生产级长链路 Agent 的关键可靠性问题，字节工程团队背书质量，Skills 系统扩展性强；与 LangGraph 互补，适合需要端到端自主执行的重型 workflow 场景。

---

### 2.2 NousResearch/hermes-agent — "随用户成长"的通用 Agent

- **链接**：[github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- **类型**：General-Purpose Agent / Adaptive / User-Model Driven
- **发布时间**：⚪ 持续趋势 — 持续登上 GitHub Trending，社区活跃度高
- **功能**：Hermes Agent 的核心理念是"agent 应随用户成长而演进"。它持续学习用户的工作习惯、工具偏好和项目上下文，自动调整执行策略与工具选择，从而减少用户重复说明背景的认知负担。
- **核心特性**：
  - 用户 profile 持续更新：记录并推断偏好，下次使用时自动应用
  - 自适应工具选择：根据历史偏好决定调用哪个 MCP 工具
  - 与 Claude Agent SDK 深度兼容
- **使用场景**：UX 研究员使用 Hermes Agent 处理访谈记录，Agent 随时间学习到"该用户偏好摘要卡片格式、关注情感词汇密度"，无需每次都重新说明输出偏好。
- **是否值得收藏**：⚠️ 条件性 Yes — 适合有固定工作模式的重度用户；如需快速验证单次任务，DeerFlow 或直接 Claude Code 更合适。

---

## 3. 🧩 Claude Skills / Platform 更新

### 3.1 Claude Code 2026-07 最新更新：Sonnet 5 默认 + `/rewind` + MCP 增强

- **链接**：[releasebot.io/updates/anthropic/claude-code](https://releasebot.io/updates/anthropic/claude-code)
- **类型**：Claude Code CLI / Platform Update
- **发布时间**：🔴 24h内 — 2026年7月正式推送
- **核心变更**：
  - **Claude Sonnet 5 成为默认模型**：原生 1M token 上下文窗口，覆盖超大型代码库和长 workflow；促销定价持续至 2026-08-31
  - **`/rewind` 命令**：可回退到 `/clear` 之前的对话状态，误清除上下文后一键恢复，极大降低长 session 操作风险
  - **MCP 稳定性提升**：MCP 连接重试机制增强 + OAuth 错误处理优化，减少 MCP 服务断连导致的 workflow 中断
  - **性能优化**：流式输出阶段 CPU 使用量下降约 37%，长 session 内存泄漏问题修复
- **对 UX Workflow 的影响**：1M token 上下文意味着可以在单个 Claude Code session 中同时载入完整的设计系统代码库 + Figma token JSON + 组件库文档，不再需要手工切割上下文。`/rewind` 让设计 → 代码的探索性迭代更安全。
- **是否值得收藏**：✅ Yes — 常规更新但影响显著，特别是 1M 上下文对 design-to-code 多文件操作场景的提升是实质性的。

---

### 3.2 Anthropic Beta：Tool Search Tool — 工具按需发现，减少 85% token 用量

- **链接**：[anthropic.com/engineering/advanced-tool-use](https://www.anthropic.com/engineering/advanced-tool-use)
- **类型**：Agent Infra / Tool-Use Enhancement / Beta Feature
- **发布时间**：🟡 3天内 — Anthropic 工程博客近期发布
- **做什么**：传统 Agent 需要在系统 prompt 中预装所有可能用到的工具定义，导致 token 消耗巨大。Tool Search Tool 是 Anthropic 新 Beta 功能，让 Claude **按需发现工具**：Agent 只在需要时才"搜索"并加载工具定义，不用的工具不占用 context 窗口。
- **核心能力**：
  - 工具懒加载：从完整工具库中按需拉取，实测减少 85% token 用量
  - 动态发现：Agent 可在运行中根据任务需求扩展可用工具集
  - 无需重构现有工具库：兼容已有的 MCP 工具定义
- **使用场景**：一个包含 200 个 MCP 工具的设计系统 Agent，不再需要将所有工具塞入 context。Agent 根据任务动态加载 Figma 工具 / 组件生成工具 / CSS 分析工具，每次调用成本降低 85%，也大幅降低 LLM 因工具过载而产生幻觉的概率。
- **是否值得收藏**：✅ Yes — 对构建复杂 Agent 系统的工程团队是重要的效率与成本双赢升级，代表 Anthropic 在 tool-use 架构上的方向性变化。

---

## 4. 💡 Emerging Patterns — 今日关键新范式

### 🔑 Pattern 1：DESIGN.md 作为"设计系统的 API 层"

DESIGN.md 的出现标志着一个范式变化：**设计规范不再只面向人，而是同时面向 AI Agent**。设计师的工作产物（颜色系统、排版规范、品牌语气）开始被标准化为机器可读的结构。这与 README.md 对开发者的角色类似——它是 AI 编码时代设计系统与代码库之间的"元数据层"。预计半年内各主流 Design System（MUI、shadcn、Radix）都将官方维护自己的 DESIGN.md。

> **Design → Dev gap 信号：极强缩短** ↓

### 🔑 Pattern 2：工具懒加载（Lazy Tool Loading）成为 Agent 基础设施新标准

Tool Search Tool 将"将所有工具塞入 context"的做法定性为反模式。未来的 Agent 系统将普遍采用按需加载工具的架构，MCP 工具库从"静态配置"演变为"可被 Agent 动态搜索的工具目录"。这对构建大规模 Agent 系统的产品团队是结构性变化。

### 🔑 Pattern 3：Skills 标准化加速，"Skills 市场"形态初现

从 mattpocock/skills 到 VoltAgent/awesome-design-md，AI 能力不再只是 prompt 片段，而是版本化、可安装、可在团队间共享的工程资产。这预示着"Skills 市场"形态的快速成熟——设计团队可像安装 npm 包一样安装"设计系统同步 Skill"或"Figma → Tailwind 转换 Skill"。

---

## 📊 今日评分总览

| 项目 | 类型 | 时效 | UX 价值 | 推荐 |
|------|------|------|---------|------|
| google-labs-code/design.md | Design Standard | 🟡 3天内 | ⭐⭐⭐⭐⭐ | ✅ 必看 |
| VoltAgent/awesome-design-md | Resource Library | 🟡 3天内 | ⭐⭐⭐⭐ | ✅ 收藏 |
| bytedance/deer-flow v2.0 | Super Agent | 🟡 3天内 | ⭐⭐⭐⭐ | ✅ 重点关注 |
| Claude Code 7月更新 | Platform | 🔴 24h内 | ⭐⭐⭐⭐ | ✅ 立即更新 |
| Anthropic Tool Search Tool | Agent Infra | 🟡 3天内 | ⭐⭐⭐⭐⭐ | ✅ 构建者必读 |
| NousResearch/hermes-agent | General Agent | ⚪ 持续趋势 | ⭐⭐⭐ | ⚠️ 按需参考 |

---

*报告生成时间：2026-07-01 | 数据来源：GitHub Trending / Anthropic Releasebot / Google Labs / OSSInsight / OpenDataScience*
