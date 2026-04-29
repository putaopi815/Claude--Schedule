# 🧠 AI Skills & Agents Daily — 2026-04-29

> **Date**: 2026-04-29
> **Time Window**: 过去 24h（优先）/ 3 天内（补充）
> **Sources Checked**: GitHub Trending / HN / Reddit / Twitter / Release Notes / InfoQ / Google Developers Blog
> **Dedup Check**: ✅ 已对比最近 3 天报告（2026-04-22 最新）

---

## 1. 🎨 UX / Design Focused

### 1.1 Figma AI Skills — SKILL.md 驱动的设计 Agent 上下文系统

- **链接**：[figma.com/blog/figma-make-general-availability](https://www.figma.com/blog/figma-make-general-availability/)
- **类型**：Tool / Skill System
- **发布时间**：⚪ 持续趋势 — April 2026 全量上线，近期社区活跃讨论持续增长
- **做什么**：在 Figma MCP Agent 写权限基础上，新增 **Skills 机制**——任何理解 Figma 的人都可以编写 `.md` 技能文件，给 Agent 提供团队的设计决策、规范和意图上下文。提供官方入门技能 `/figma-use`，也可完全自定义。
- **核心能力**：
  - Skills 文件（即 SKILL.md 格式）封装团队设计语境：组件使用规范、交互惯例、品牌 token 约束
  - Agent 读取 Skills 后，生成的设计天然符合团队标准，无需每次重复说明
  - 与 Figma MCP Write Access 深度结合，实现"描述 → 组件 → 代码"完整链路
- **使用场景**：设计团队编写一个 `spacing-system.skill.md`，Agent 在任何设计任务中自动遵循 8px 栅格、正确使用 spacing token，无需每次 prompt 中重申。
- **为什么重要（UX视角）**：这是将"设计系统知识"从文档转为可被 Agent 直接调用的行动上下文。**Design → Dev gap 缩短信号：极强**——Skills 文件本质上是"团队设计语言"的 AI 可读编码。
- **是否值得收藏**：✅ Yes — Skills 文件范式将成为未来设计团队的基础设施标配，现在建立意识极有价值。

---

### 1.2 Google A2UI v0.9 — 框架无关的生成式 UI 开放标准

- **链接**：[github.com/google/A2UI](https://github.com/google/A2UI) | [developers.googleblog.com/a2ui-v0-9-generative-ui](https://developers.googleblog.com/a2ui-v0-9-generative-ui/)
- **类型**：Open Standard / SDK
- **发布时间**：🟢 重大更新 — 发布于 2026-04-17，标准级发布，影响持续扩散
- **做什么**：Agent-to-UI 通信的开放标准。允许 AI Agent 在对话中生成定制化 UI 组件（不是通用文本回复），并通过统一协议适配 React、Flutter、Angular、Lit 等任意前端框架。v0.9 新增客户端定义函数、弹性流式解析、动态 catalog 切换。
- **核心能力**：
  - 本地/远程 Agent 用统一语言与任意客户端应用通信
  - Agent SDK 优化了生成 pipeline 和缓存层，实现低延迟 UI 渲染
  - 版本协商机制：基于客户端能力动态选择最佳规范版本
  - 支持协同编辑场景的客户端 → 服务器数据同步
- **使用场景**：健康类 App 中的 AI 助理根据对话语境动态生成"体检结果卡片"、"疫苗提醒组件"或"附近诊所地图"，而非一段文字描述——每个交互都是最适配当前语境的 UI 组件。
- **为什么重要（UX视角）**：这是继 DESIGN.md 之后，又一个"AI 设计意图标准化"的关键信号。A2UI 将"Agent 生成界面"变为可跨平台移植的标准行为，而非各平台自己造轮子。**AI-native UX 机会：将 Agent 输出从"文字回复"升级为"上下文自适应 UI"。**
- **是否值得收藏**：✅ Yes — 开放标准类项目，一旦生态形成则影响深远，现在是建立认知的窗口期。

---

## 2. ⚙️ GitHub Trending Agents

### 2.1 GenericAgent（复旦团队）— 自演化技能树 Agent

- **链接**：[github.com/lsdefine/GenericAgent](https://github.com/lsdefine/GenericAgent)
- **类型**：Agent Framework / Self-Evolving
- **发布时间**：🟢 重大更新 — 技术报告发布于 2026-04-21（arXiv），L4 记忆 + Scheduler 更新于 04-11
- **功能**：从 3.3K 行种子代码出发，通过执行任务自动沉淀技能（Skill），形成独特的个人化技能树，实现 **6x token 消耗降低**。每完成一个新任务，执行路径被自动固化为可复用 Skill，遇到相似请求时直接调用，跳过重复规划过程。
- **核心特性**：
  - 原子工具集：浏览器 / 终端 / 文件系统 / 键鼠 / 视觉 / ADB 移动端控制
  - L4 会话存档记忆 + Cron Scheduler（04-11 更新）
  - 技能库（Skill Library）规模已达百万级（03-10 发布）
  - 支持 WeChat Bot 前端接入
- **使用场景**：每天让 Agent 执行"汇总设计社区今日热帖"，两周后它已有完整的"竞品监测技能"，执行速度比初次快 6 倍，token 消耗极低。
- **是否值得收藏**：✅ Yes — 自演化 Skill Tree 是今年最重要的 Agent 设计模式之一，复旦团队的学术严谨性保证了可信度。

---

### 2.2 Google ADK 2.0 Beta — 图结构确定性 Agent 工作流

- **链接**：[github.com/google/adk-python](https://github.com/google/adk-python) | [adk.dev/2.0/](https://adk.dev/2.0/)
- **类型**：Agent Framework / Workflow Orchestration
- **发布时间**：🟢 重大更新 — Beta 版于 April 2026 发布（8,200+ stars，活跃增长中）
- **功能**：Python-first 的生产级 Agent 开发套件。2.0 Beta 核心新增：**图结构工作流**（确定性路由 + 条件分支 + 并行扇出）、**Agent Teams**（多 Agent 协同）、可视化 Canvas 管理 Agent 架构。
- **核心特性**：
  - 图节点 = Agent / Function / 条件路由，用代码逻辑控制复杂分支
  - 状态 + Artifact delta bundling，支持断点续接长任务
  - 内置 Web UI：工作流图可视化 + 截图/日志 Inspector
  - Vertex AI Code Execution Sandbox API 集成
- **使用场景**：构建"UI 评审 Agent → 可访问性检查 Agent → 代码生成 Agent"的确定性流水线，每个节点可独立测试，整体流程可视化监控。
- **是否值得收藏**：✅ Yes — Google 背书 + 图结构工作流是企业场景的刚需，8k+ stars 验证社区接受度。

---

### 2.3 GitHub Agentic Workflows — pre-agent-steps 与安全扫描更新

- **链接**：[github.github.com/gh-aw/](https://github.github.com/gh-aw/)
- **类型**：Workflow Infrastructure / CI Security
- **发布时间**：🟡 3天内 — 2026-04-27 开始灰度推送
- **功能**：GitHub 原生 Agentic Workflows 新增两个关键特性：① **pre-agent-steps 前置步骤字段**，允许在 AI Agent 启动前运行自定义 GitHub Actions（认证、环境准备、依赖安装）；② **Agent 运行前自动扫描并清理潜在恶意可执行文件**，堵塞供应链攻击向量。
- **核心特性**：
  - `pre-agent-steps` frontmatter 字段：与 Agent 运行解耦的环境配置层
  - 每次 Agent 执行前扫描缓存中植入的可执行文件和禁止文件
  - 无需修改 Agent 本身逻辑即可增强安全边界
- **使用场景**：设计团队的 CI 流程中，先用 pre-agent-steps 拉取 Figma token 和设计 token 文件，再启动 design-to-code Agent 执行 UI 一致性检查。
- **是否值得收藏**：✅ Yes — 这是 GitHub 原生 Agentic 基础设施的正式成熟信号，**今日 3 天内发布，具有高时效性**。

---

### 2.4 obra/superpowers — 可组合 Skill 框架 + 软件开发方法论

- **链接**：[github.com/obra/superpowers](https://github.com/obra/superpowers)
- **类型**：Skill Framework / Agent Methodology
- **发布时间**：🟢 重大更新 — 4 月上旬活跃，可通过 Claude Plugin Marketplace 安装
- **功能**：为 Claude Code（及 Codex 等编码 Agent）提供完整的软件开发方法论，通过一组可组合的 Skill 文件驱动 Agent 在复杂任务中采用正确的工程思路：先发散 → 设计 → 计划 → 子 Agent 并行执行 → 两阶段审查。
- **核心技能集**：
  - `brainstorming`：代码前的方案发散，按模块呈现设计供确认
  - `using-git-worktrees`：设计批准后自动创建隔离工作区 + 验证测试基线
  - `writing-plans`：将工作拆解为 2-5 分钟粒度任务，每个有精确文件路径 + 验证步骤
  - `subagent-driven-development`：每个任务派发独立子 Agent + 两阶段代码质量审查
- **使用场景**：用一句话描述"重构设计系统的 Button 组件"，Superpowers 引导 Agent 先发散实现方案，再计划逐个文件的修改，最后子 Agent 并行执行并自动审查，全程不需人工干预 boilerplate 任务。
- **是否值得收藏**：✅ Yes — 这是目前最成熟的"Claude Skills 最佳实践"体系，直接可用于生产级工程任务。

---

## 3. 🧩 Claude Skills（本期重点）

### 3.1 /ultrareview — 多 Agent 云端代码审查

- **Skill 名称**：ultrareview
- **发布时间**：🟢 重大更新 — 2026-04-22 发布（CLI v2.1.86+），Pro/Max 用户赠 3 次免费使用（截至 05-05）
- **工作流描述**：执行 `/ultrareview` 或 `/ultrareview <PR#>`，Claude Code 打包仓库状态上传至远程沙箱，部署多个 Reviewer Agent 并行扫描。每个 Agent 负责不同维度（应用逻辑 / 边界情况 / 安全 / 性能），仅在 **Bug 被复现验证后** 才上报 Finding，大幅降低误报率。
- **使用时机**：合并关键功能分支前；重构后确认无回归问题时；需要覆盖安全和性能的全面审查时。

### 3.2 Superpowers Skills 套件（obra）

- **Skill 名称**：superpowers（via Claude Plugin Marketplace）
- **工作流描述**：`/use superpowers` 激活后，Claude Code 自动获得 brainstorming → plan → subagent-execute → review 的完整工程方法论。通过 SKILL.md 文件机制给 Agent 注入团队工程规范。
- **使用时机**：任何超过 2 个文件改动的工程任务；需要保证代码质量和测试覆盖的功能开发时。

### 3.3 Anthropic Managed Agents — 生产级托管执行层

- **发布时间**：🟢 重大更新 — 2026-04-08 公测，$0.08/session-hour + 标准 token 费率
- **工作流描述**：通过 `managed-agents-2026-04-01` header 接入 Claude API，Anthropic 托管 Agent 的沙箱 / 状态管理 / 错误恢复 / 会话连续性，开发者只需关注业务逻辑。特别适合长时间运行的多步骤工作流（如自动化 UX 测试 → 生成报告 → 通知设计团队）。
- **使用时机**：需要构建可靠的生产 Agent，但不想自建基础设施；Agent 需要在多次会话间保持状态时。

---

## 4. 💡 Emerging Patterns（今日新范式）

### Pattern 1: Skills 文件 = Agent 的组织记忆（Organizational Memory as Skills）

Figma Skills + obra/superpowers 都在验证同一个范式：**将团队知识编码为 SKILL.md 文件**，而非每次 prompt 重新描述。这类似于将公司的设计规范从 Notion 文档迁移到 Agent 可直接调用的行动指令。未来"设计团队的 SKILL.md 库"将成为核心知识资产，类似今天的设计 token 文件。

### Pattern 2: 生成式 UI 标准化竞赛（A2UI vs DESIGN.md）

Google A2UI v0.9 和 Google Stitch 的 DESIGN.md 同为 Google 推动、同在 April 2026 活跃——前者定义"Agent 如何生成 UI 组件协议"，后者定义"设计意图的描述规范"。两者方向互补，共同构建 **AI-native 产品界面的基础语言**。这场标准化竞赛将在 2026 年内分出胜负，需要持续关注哪个标准获得主流 React/Flutter 生态采纳。

### Pattern 3: 图结构工作流取代线性链（Graph > Chain）

ADK 2.0 Beta 和 GitHub AW 的 pre-agent-steps 都在推动同一范式转变：从 LangChain 时代的"线性调用链"升级为"图结构工作流"——节点可并行、可条件分支、可断点续接。这对 UX 设计流水线意味着：**设计审查 → 可访问性检测 → 代码生成** 不再是瀑布流程，而是可编排的有向无环图。

### Pattern 4: 自演化 Skills（Agent 越用越强）

GenericAgent 的技能树机制首次将"使用即学习"做到生产可用：6x token 降低不是靠更大的模型，而是靠执行路径的自动沉淀。这预示着未来 Agent 的核心竞争力不在于初始能力，而在于**个人化技能积累速度**。对 UX 实践者的启示：越早建立自己的 Agent Skill 库，差距越大。

---

## 📊 今日信号总结

| 项目 | 类型 | 时间信号 | UX 相关度 | 推荐优先级 |
|------|------|---------|-----------|-----------|
| Figma AI Skills (SKILL.md) | Skill System | ⚪ 持续趋势 | ⭐⭐⭐⭐⭐ | 🔴 必看 |
| Google A2UI v0.9 | 开放标准 | 🟢 重大更新 04-17 | ⭐⭐⭐⭐⭐ | 🔴 必看 |
| GitHub Agentic Workflows update | Infrastructure | 🟡 3天内 04-27 | ⭐⭐⭐ | 🟠 重要 |
| obra/superpowers | Skill Framework | 🟢 重大更新 | ⭐⭐⭐⭐ | 🟠 重要 |
| GenericAgent（复旦）| Self-Evolving Agent | 🟢 重大更新 04-21 | ⭐⭐⭐ | 🟡 参考 |
| Google ADK 2.0 Beta | Agent Framework | 🟢 重大更新 | ⭐⭐⭐ | 🟡 参考 |
| Claude /ultrareview | Skill | 🟢 重大更新 04-22 | ⭐⭐ | 🟡 参考 |
| Anthropic Managed Agents | API / Platform | 🟢 重大更新 04-08 | ⭐⭐ | 🟢 收藏备用 |

---

*生成时间：2026-04-29 | 数据来源：GitHub Trending、Google Developers Blog、InfoQ、releasebot.io、aitoolly.com、社区讨论*
