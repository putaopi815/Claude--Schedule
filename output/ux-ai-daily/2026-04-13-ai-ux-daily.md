# UX-AI-Daily | 2026-04-13

> AI 行业动态日报 — 面向 UX / 产品设计师
> 数据范围：2026-04-10 ~ 2026-04-13（严格 3 天内）

---

## 🧰 工具 Tools

### 1. Anthropic 发布 Claude for Word (Beta)
**发布时间：2026-04-10（过去 3 天内）**

Anthropic 推出 Claude for Word 公测版，作为 Microsoft Word 原生侧边栏插件（Mac/Windows），支持在 Word 中直接进行 AI 辅助起草、编辑和修改。所有 AI 编辑以 Word 原生"修订跟踪"形式呈现，保留复杂文档结构（多级编号、交叉引用、标题层级）。可与 Claude for Excel、Claude for PowerPoint 跨文档联动，单一对话线程横跨三个文档。目前面向 Team 和 Enterprise 用户开放。

**为什么重要：** AI 首次以"原生修订跟踪"方式深度嵌入 Office 编辑流程。对 UX 设计师而言：PRD 撰写、设计规范文档、用户研究报告等工作流将直接受益。跨 Office 三件套联动意味着报告-数据-演示之间的一致性可以由 AI 自动校验。

🔗 [Anthropic 官方](https://cybersecuritynews.com/claude-beta-for-word/) | [TNW](https://thenextweb.com/news/dario-amodei-london-united-kingdom) | [Artificial Lawyer](https://www.artificiallawyer.com/2026/04/11/anthropic-targets-lawyers-with-claude-for-word/)

---

## 📰 新闻 News

### 2. MiniMax M2.7 正式开源：首个"自我进化"Agent 模型
**发布时间：2026-04-12（过去 24h 内）**

MiniMax 正式开源 M2.7 模型权重。该模型具备"自我进化"能力——自主执行超 100 轮"分析失败→规划修改→修改代码→评估→决策保留/回滚"循环，无需外部重新训练即可自主提升 30% 性能。SWE-Pro 基准 56.22%（匹配 GPT-5.3-Codex），MoE 架构仅需 230B 参数中激活部分即可运行。

**为什么重要：** "自我进化"模型意味着 AI 产品可以持续自我改进而非等待版本更新。对 UX 设计师的启示：未来产品的 AI 能力不是静态的，如何设计"能力在成长的 AI"的用户预期管理、进度透明度和信任机制是新课题。

🔗 [MarkTechPost（4/12）](https://www.marktechpost.com/2026/04/12/minimax-just-open-sourced-minimax-m2-7-a-self-evolving-agent-model-that-scores-56-22-on-swe-pro-and-57-0-on-terminal-bench-2/) | [VentureBeat](https://venturebeat.com/technology/new-minimax-m2-7-proprietary-ai-model-is-self-evolving-and-can-perform-30-50) | [MiniMax 官方](https://www.minimax.io/news/minimax-m27-en)

---

### 3. ACM CHI 2026 今日开幕：HCI 顶会聚焦 AI 与人机交互
**发布时间：2026-04-13（今天）**

ACM CHI 2026（人机交互领域最高级别学术会议）今日在巴塞罗那 CCIB 正式开幕，持续至 4 月 17 日。主题"Mediterranean Synergy"，引入全新议程格式：上午论文报告 + 下午五类互动环节。Responsible AI 专题由英国 RAI 主导，聚焦跨文化背景下的负责任 AI 设计。

**为什么重要：** CHI 是 UX/HCI 领域最重要的学术风向标。今年大量论文聚焦 AI agent 交互、Generative UI、AI 辅助设计决策等主题。设计师应关注本周 CHI 产出——这些研究将定义未来 1-2 年的交互设计范式。

🔗 [CHI 2026 官方](https://chi2026.acm.org/) | [SIGCHI](https://sigchi.org/events/chi-2026/) | [RAI @CHI2026](https://rai.ac.uk/events/rai-chi2026/)

---

## 💻 GitHub 趋势

### 4. NousResearch/hermes-agent — 今日 GitHub 全站 #1
**时间：2026-04-13 今日 | 今日 +7,454 stars | 总 67,460 stars**

"The agent that grows with you"——自学习 AI Agent，内置学习循环：从经验中创建技能、使用中自我改进、跨会话持久化记忆、构建用户画像。支持 Telegram/Discord/Slack/WhatsApp/Signal 多平台网关。可运行在 $5 VPS 上。v0.8.0（4/8 发布）新增后台任务通知、实时模型切换、MCP OAuth 2.1。

**为什么重要：** 7,454 stars/天说明社区对"可成长 Agent"的强烈需求。对 UX 设计师而言，"Agent 随使用而成长"是全新交互范式——需要设计学习进度可视化、行为可预测性保障、以及用户对 Agent 能力边界的认知管理。

🔗 [GitHub](https://github.com/NousResearch/hermes-agent) | [AIToolly（4/12）](https://aitoolly.com/ai-news/article/2026-04-12-nousresearch-launches-hermes-agent-a-new-intelligent-agent-designed-to-grow-with-users) | [官方网站](https://hermes-agent.nousresearch.com/)

---

### 5. GitNexus — 代码知识图谱 + Graph RAG
**时间：2026-04-10 登顶 GitHub Trending #1 | 单日 +1,195 stars（过去 3 天内）**

零服务器代码智能引擎，在浏览器内将代码库解析为知识图谱（Tree-sitter），内置 Graph RAG Agent 提供结构化上下文。支持 TypeScript/Python/Java/Go/Rust 等 8 种语言。无需后端，完全客户端运行。

**为什么重要：** "理解代码 > 生成代码"的趋势信号。对 design-to-code 工具有启发：未来设计工具不仅要生成代码，更需理解现有代码结构以实现无缝集成。图结构正成为 AI 理解复杂系统的主流方案。

🔗 [GitHub](https://github.com/abhigyanpatwari/GitNexus) | [Pebblous Blog（4/10）](https://blog.pebblous.ai/blog/gitnexus-code-knowledge-graph-2026/en/)

---

### 6. multica-ai/multica — 开源托管 Agent 平台
**时间：2026-04-13 今日 trending | 今日 +1,609 stars | 总 9,496 stars**

"Turn coding agents into real teammates"——开源多 Agent 协作平台，将编码 Agent 转化为可管理的团队成员角色，支持架构设计、编码、测试、部署的多 Agent 协作流程。

**为什么重要：** 从"AI 工具"到"AI 队友"的范式转变。对 UX 产品设计师的启示：未来产品中的 AI 不是按钮或功能，而是具有角色身份的协作者。如何设计 Agent 的"存在感"、任务分配界面、协作状态反馈将成为核心 UX 课题。

🔗 [GitHub](https://github.com/multica-ai/multica)

---

### 7. forrestchang/andrej-karpathy-skills — Claude Code 行为优化配置
**时间：2026-04-13 今日 trending | 今日 +2,369 stars | 总 17,079 stars**

一个单文件 CLAUDE.md 配置方案，通过结构化指令优化 Claude Code 的编码行为，使 AI 编码 Agent 更好地理解项目上下文、遵循开发规范。

**为什么重要：** 反映"通过配置而非对话塑造 AI 行为"的新交互模式。对 UX 设计师构建 AI 产品的启示：用户定制 AI 行为的最佳方式可能不是聊天，而是声明式配置文件——这是一种新型的"设置页面"设计挑战。

🔗 [GitHub](https://github.com/forrestchang/andrej-karpathy-skills)

---

## 💡 洞察 Insights

### 8. AG-UI + A2UI：Agent 驱动界面的标准栈正在形成
**状态：持续发展中 | Oracle/Google/CopilotKit 联合推动**

三层标准正在协同形成 Agent-UI 的完整技术栈：
- **Oracle Open Agent Spec**：框架无关的 Agent 逻辑定义标准
- **AG-UI（CopilotKit）**：Agent 与前端的实时双向通信协议
- **A2UI（Google 主导）**：Agent 用结构化 JSONL 描述 UI 需求（表单/表格/多步流程）

三种 Generative UI 模式已明确：受控式（AG-UI）→ 声明式（A2UI/Open-JSON-UI）→ 开放式（MCP Apps）。

**为什么重要：** 这是 AI-native UX 最重要的基础设施变化。当 Agent 可以标准化地描述和生成 UI 时，设计师角色从"设计每个页面"转向"设计 UI 生成规则与约束系统"。强烈建议 UX 设计师关注 A2UI 规范。

🔗 [CopilotKit 指南](https://www.copilotkit.ai/blog/the-developer-s-guide-to-generative-ui-in-2026) | [Google A2UI](https://developers.googleblog.com/introducing-a2ui-an-open-project-for-agent-driven-interfaces/) | [Oracle Blog](https://blogs.oracle.com/ai-and-datascience/announcing-agent-spec-for-a2ui-copilotkit-ag-ui)

---

## 📊 今日关键数字

| 指标 | 数值 | 时间 |
|------|------|------|
| hermes-agent 今日新增 stars | 7,454 | 4/13 |
| andrej-karpathy-skills 今日新增 stars | 2,369 | 4/13 |
| multica 今日新增 stars | 1,609 | 4/13 |
| MiniMax M2.7 自我进化性能提升 | +30% | 4/12 开源 |
| MiniMax M2.7 SWE-Pro 得分 | 56.22% | 匹配 GPT-5.3-Codex |
| CHI 2026 会期 | 4/13-17 | 今天开幕 |

---

*报告生成时间：2026-04-13 | 所有内容严格限定在 2026-04-10 ~ 2026-04-13 时间窗口内*
*数据来源：MarkTechPost, VentureBeat, GitHub Trending, ACM CHI, CopilotKit, TNW, Anthropic*
