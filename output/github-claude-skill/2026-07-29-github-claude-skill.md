# 🧠 AI Skills & Agents Daily — 2026-07-29

> **Date**: 2026-07-29
> **Time Window**: 过去 24h（优先）/ 3 天内（补充）
> **Sources Checked**: GitHub Trending / MCP Blog / OSSInsight / analyticsvidhya / startupcorners / x.ai / SecurityWeek / apptension / digitalapplied / stacktr.ee
> **Dedup Check**: ✅ 已对比 2026-07-15 报告（Flowstep / agent-teams-ai / last30days-skill / deer-flow / crawl4ai / Claude Code Skills 架构 / FastMCP 均已在上期收录，本期不重复）

---

## 1. 🎨 UX / Design Focused

### 1.1 MCP 2026-07-28 规范正式版 — Design Tool 与 Agent 集成的底层重构

- **链接**：[blog.modelcontextprotocol.io — 2026-07-28 Release](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) | [MCP Goes Stateless: What Changed](https://www.digitalapplied.com/blog/mcp-2026-07-28-spec-stateless-migration-guide) | [Stacktree 分析](https://stacktr.ee/blog/mcp-2026-spec-changes)
- **类型**：Protocol Update / MCP Infrastructure / Agent Integration
- **发布时间**：🔴 24h内 — MCP 规范正式版于 2026-07-28 发布，距今不足24小时
- **做什么**：MCP 协议自发布以来最大规模的修订版本正式落地，核心变化：
  - **Stateless 协议核心**：移除 `Mcp-Session-Id` 和 `initialize` 握手，任意 MCP 请求可落到任意服务器实例，无需 sticky session 或共享 session store
  - **MCP Apps 扩展**：首个正式 Extension，支持通过 MCP 渲染服务端 UI——Agent 可以直接输出可交互界面，而非仅返回文本
  - **Tasks 扩展**：支持长周期任务的标准化表达（长达数分钟/小时的 Agent 任务有了协议层支持）
  - **Auth 加固**：6 个 SEP（安全增强提案），更严格对齐 OAuth 和 OpenID Connect
  - **12个月弃用政策**：为工具开发者提供稳定的迁移窗口
- **对 UX/设计工具的直接影响**：
  - Figma MCP、Flowstep MCP、Canva MCP 等所有现有 design-to-code 集成**无需修改逻辑即可获得水平扩展能力**——原本需要粘性路由和共享 session store 的后端，现在只需普通 round-robin 负载均衡
  - **MCP Apps 扩展是新交互范式的起点**：设计工具通过 MCP 向 AI 编辑器推送服务端渲染 UI 面板成为可能，"设计工具控制面板直接嵌入 Claude Code 侧边栏"从理论变为协议层可实现
  - Tools list 响应可被客户端缓存（`ttlMs`），减少反复握手延迟，设计工具在 IDE 内的响应速度将明显提升
- **为什么重要（UX视角）**：MCP stateless 化意味着 design-to-code 链路的后端复杂度大幅下降——部署一个 Figma/Canva MCP server 不再需要运维有状态会话；MCP Apps 开辟了 Agent 输出交互式 UI 的全新可能，直接影响 Agentic UX 的设计空间。
- **是否值得收藏**：✅ Yes — 这是 MCP 生态的里程碑版本，所有在 Claude Code / Cursor 中使用 MCP 工具（包括设计工具）的团队都需要了解迁移要点。

---

### 1.2 Canva MCP AI Connector — 品牌资产与 Agent 工作流的直接对接

- **链接**：[Canva AI Connector (Moda 分析)](https://moda.app/blog/ai-agent-design-mcp-tools) | [orshot.com — Best AI Tools for Graphic Design with MCP](https://orshot.com/blog/ai-tools-for-graphic-design-with-mcp)
- **类型**：Design Tool MCP / Brand Asset Management / Agent Integration
- **发布时间**：⚪ 持续趋势 — 2026 年发布，7月在多份 MCP 设计工具评测中高频出现；MCP 2026-07-28 规范发布后预计将迎来功能更新
- **做什么**：Canva 推出的 MCP 兼容连接器，允许 AI Agent 直接创建和编辑 Canva 设计、管理品牌资产（颜色、字体、Logo）、搜索模板库，并以多种格式导出——整个过程无需打开 Canva 界面，Agent 通过 MCP 工具调用完成所有操作。
- **核心能力**：
  - Brand-aware 设计生成：Agent 获取品牌 token 后生成符合视觉规范的设计
  - 模板检索 + 编辑：Agent 语义搜索模板，直接修改内容层
  - 多格式导出：PNG、PDF、MP4 均可通过工具调用完成
- **使用场景**：营销内容工作流中，Agent 根据产品说明自动调取 Canva 品牌模板、填充文案与图片、导出各渠道所需格式——原本需要设计师手动完成的2小时工作压缩为 Agent 数分钟执行。
- **为什么重要（UX视角）**：**Canva MCP 是目前最成熟的"品牌设计 Agent 化"方案**——不是替代设计师创作，而是把品牌标准化部分（合规内容、营销物料）完全交给 Agent 自动生成。这是 design → asset production gap 缩短的具体实现。
- **是否值得收藏**：✅ Yes — 品牌设计、内容营销、产品运营团队直接可用；在 MCP 2026-07-28 stateless 规范落地后，其后端部署复杂度将进一步降低。

---

## 2. ⚙️ GitHub Trending Agents

### 2.1 OpenClaw — 年度增长最快开源 Agent 平台，382k stars

- **链接**：[analyticsvidhya.com — Top 10 GitHub AI Repos July 2026](https://www.analyticsvidhya.com/blog/2026/07/trending-ai-github-repositories/) | [OSSInsight Trending](https://ossinsight.io/trending/ai)
- **类型**：Agent Platform / Open Source / Composable
- **发布时间**：⚪ 持续趋势 — 2026年爆发成长，由 ~9,000 stars 增长至 382,000 stars，被多个来源描述为"2026年 GitHub 历史上增长最快的开源项目"；7月仍在趋势榜持续活跃
- **功能**：OpenClaw 是一个可组合的 Agent 平台，强调 composability（可组合性）—— MCP servers、Skills、Plugins、Hooks 均可作为独立模块接入，支持 Claude Code、Cursor、GitHub Copilot、Gemini CLI 等主流 AI 编辑器。last30days-skill 等知名 Skill 已将 OpenClaw 列为推荐运行环境之一。
- **使用场景**：作为"通用 Agent 主机"运行，将多个 Skills 和 MCP 工具组合为完整的工作流平台；也被 Skill 开发者用作多平台分发目标。
- **为什么重要（UX视角）**：OpenClaw 的爆发增长说明**开发者正在寻找统一的 Agent 运行环境**——不想被单一 AI 编辑器绑定。对 UX 工具链设计者，OpenClaw 的跨平台架构是一个重要参考：工具应设计为与运行环境无关的插件，而非深度耦合的集成。
- **是否值得收藏**：✅ Yes — 382k stars 的真实验证 + 多 Skill 生态已在此运行；值得关注其与 MCP 2026-07-28 stateless 规范的兼容进展。

---

### 2.2 OfficeCLI — 专为 AI Agent 设计的开源 Office 自动化套件

- **链接**：[analyticsvidhya.com — Top 10 GitHub AI Repos July 2026](https://www.analyticsvidhya.com/blog/2026/07/trending-ai-github-repositories/)
- **类型**：Tool / Document Automation / Agent Data Layer
- **发布时间**：🟡 3天内 — 出现于 2026 年 7 月 GitHub Trending 榜单，与近期活跃项目共同收录
- **功能**：OfficeCLI 是专为 AI Agent 构建的免费开源 Office 套件，支持 Agent 直接读取、编辑、自动化 Word（.docx）、Excel（.xlsx）、PowerPoint（.pptx）文件——输出格式对 LLM 直接可读，无需额外解析步骤。
- **核心能力**：
  - Word/Excel/PPT 的读写与结构化提取
  - Agent-friendly 输出格式（Markdown / JSON）
  - 适配 MCP 工具调用模式，可作为 MCP Server 的数据层
- **使用场景**：UX 研究 Agent 自动读取用研报告（Word/Excel）→ 提取关键数据 → 生成结构化摘要；产品 Agent 自动填写 PRD 模板（Word）并导出 PDF 交付。
- **为什么重要（UX视角）**：文档自动化是 UX 研究和产品管理工作流中最耗时的部分之一。OfficeCLI 让 Agent 直接操作 Office 文件，填补了"Agent 能读 Web 数据但无法处理企业文档"的空白。
- **是否值得收藏**：✅ Yes — 企业/大型团队的必备工具层；与 crawl4ai 一样属于 Agent 数据采集的基础设施范畴。

---

### 2.3 TencentCloud/CubeSandbox — Rust 编写的轻量级 Agent 沙箱，并发即时启动

- **链接**：[analyticsvidhya.com — Top 10 GitHub AI Repos July 2026](https://www.analyticsvidhya.com/blog/2026/07/trending-ai-github-repositories/)
- **类型**：Agent Infrastructure / Sandbox / Rust
- **发布时间**：🟡 3天内 — 出现于 2026 年 7 月 GitHub Trending 榜单，腾讯云出品
- **功能**：CubeSandbox 是腾讯云开源的 Rust 语言 Agent 沙箱，核心优势：**即时启动、高并发、超轻量**——为 AI Agent 执行代码、运行工具调用提供安全隔离环境，延迟远低于 Docker/VM 方案。
- **核心能力**：
  - 毫秒级沙箱创建（相比容器的秒级启动）
  - 并发执行：同时运行数百个独立 Agent 沙箱实例
  - Rust 实现保障内存安全和性能
- **使用场景**：多 Agent 系统中，每个 Sub-agent 在独立沙箱内执行工具调用（运行代码、访问文件系统）而不影响主进程安全；CI/CD 中为 Agent 代码生成 + 执行提供安全测试环境。
- **为什么重要（UX视角）**：Agent 沙箱是 Agentic 产品可靠性的基础——没有安全隔离的 Agent 在生产环境中是风险点。CubeSandbox 的 Rust 实现代表 **Agent 基础设施正在向系统编程语言迁移**，追求比 Python/Node 方案低一个数量级的延迟和更高的并发上限。这是构建流畅 Agent UX（无感知延迟）的底层要素。
- **是否值得收藏**：✅ Yes — 腾讯云出品，工业级可信度；Rust + 并发沙箱是未来 Agent 基础设施的方向，值得关注其 MCP 工具调用集成进展。

---

## 3. 🧩 Claude Skills

### 3.1 MCP Apps Extension — 服务端渲染 UI 进入 Claude 交互层

- **链接**：[MCP 2026-07-28 官方博客](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) | [MCP Is Growing Up (AAIF)](https://aaif.io/blog/mcp-is-growing-up)
- **Skill 名称**：MCP Apps（首个官方 MCP Extension）
- **发布时间**：🔴 24h内 — 随 MCP 2026-07-28 规范正式发布
- **工作流描述**：MCP Apps 是新规范中的首个正式 Extension，允许 MCP Server 向客户端（Claude Code、Claude Desktop 等）推送**服务端渲染的交互式 UI 面板**。这意味着：
  - MCP 工具不再只能返回文本/JSON，现在可以返回可交互的 UI 组件
  - 设计工具（如 Figma、Canva）的 MCP server 可以在 Claude 侧边栏中展示可交互的设计预览面板
  - Agent 执行中间结果可以用 UI 形式实时呈现（进度条、表单、选择器）
- **使用时机**：
  - 构建需要人机交互确认的 Agent 工作流 → 使用 MCP Apps 推送确认 UI
  - 设计工具 MCP server 需要展示视觉预览 → MCP Apps 比"返回图片链接"更原生
  - 多步骤任务需要中间状态展示 → Tasks Extension + MCP Apps 组合使用

---

## 4. 💡 Emerging Patterns（今日新范式）

### Pattern 1: MCP 协议 stateless 化 — Agent 基础设施从"有状态服务"转向"无状态函数"

MCP 2026-07-28 规范最深远的影响不是功能新增，而是**范式迁移**：把 MCP server 从"必须保持会话的有状态服务"变成"可以随意扩缩容的无状态函数"。对 Agent 工具开发者，这意味着一次架构简化——不再需要管理 session store、sticky routing、深度包检测。对 UX 工程团队，这意味着更快的工具响应（工具调用不再依赖会话预热）和更稳定的可用性（任意实例均可服务请求）。**Stateless MCP = Agent 工具从"服务"变为"函数"的基础设施时刻。**

### Pattern 2: Agent 沙箱成为一级基础设施关注点

CubeSandbox (Rust) 出现在 GitHub Trending 标志着 Agent 基础设施进入新阶段：**安全隔离不再是事后追加的功能，而是 Agent 系统的一级架构关注点**。Rust 的选择强调了"Agent 基础设施需要系统级性能"这一共识——毫秒级沙箱、零开销并发、内存安全，Python/Node 无法在同等硬件上达到相同指标。预计 2026 下半年 Rust-based Agent 沙箱方案将成为企业部署的标准选项。

### Pattern 3: Tool Harness 工程化 — AI 编码团队的新核心能力

2026 年 7 月的工程师博客（"Why AI Coding Teams Bet on Tool Harnesses"）标志着一个认知转变：优秀的 AI 编码团队的核心竞争力不再是"用更好的 Prompt"，而是**设计好的 Tool Harness**——即如何选择、组合、版本化、测试 Agent 使用的工具集。一个好的 Harness 定义了权限边界、工具组合、输入输出格式、错误恢复策略。这是 Agent 工程成熟的标志：从"玩 LLM"到"设计可维护的 Agent 系统"。

### Pattern 4: MCP Apps = Agentic UX 的新设计空间

MCP Apps Extension（服务端渲染 UI）打开了一个全新的 Agentic UX 设计空间：**Agent 不仅输出文本，还可以推送交互式界面**。这意味着"Agent 的 UI 层"开始独立于"Agent 的宿主工具（Claude Code / Cursor）"存在——MCP server 可以为自己的工具定义专属 UI 面板。对 UX 设计师，这是一个需要提前关注的范式：将来的 AI 产品设计不只是设计"对话界面"，还需要设计"Agent 工具面板"。

---

## 📊 今日信号总结

| 项目 | 类型 | 时间信号 | UX 相关度 | 推荐优先级 |
|------|------|---------|-----------|-----------|
| MCP 2026-07-28 规范（stateless + MCP Apps）| Protocol Update | 🔴 24h内 | ⭐⭐⭐⭐⭐ | 🔴 必看 |
| Canva MCP AI Connector | Design Tool MCP | ⚪ 持续趋势 | ⭐⭐⭐⭐⭐ | 🔴 必看 |
| MCP Apps Extension（服务端渲染 UI）| Claude Skill / MCP | 🔴 24h内 | ⭐⭐⭐⭐⭐ | 🔴 必看 |
| OpenClaw（382k stars）| Agent Platform | ⚪ 持续趋势 | ⭐⭐⭐⭐ | 🟠 重要 |
| OfficeCLI | Document Automation Agent | 🟡 3天内 | ⭐⭐⭐ | 🟡 参考 |
| TencentCloud/CubeSandbox | Rust Agent Sandbox | 🟡 3天内 | ⭐⭐⭐ | 🟡 参考 |

---

*生成时间：2026-07-29 | 数据来源：MCP Blog / OSSInsight / analyticsvidhya / orshot.com / moda.app / digitalapplied / stacktr.ee / apptension / x.ai / SecurityWeek*
