# 🧠 AI Skills & Agents Daily — 2026-07-22

> **Date**: 2026-07-22
> **Time Window**: 过去 24h（优先）/ 3 天内（补充）
> **Sources Checked**: GitHub Trending / AnalyticsVidhya / EINPresswire / MarkTechPost / PyShine / explainx.ai / Claude Code Docs W29
> **Dedup Check**: ✅ 已对比 2026-07-15 报告（Flowstep / last30days-skill / agent-teams-ai / deer-flow / crawl4ai / FastMCP 均已收录，本期不重复）

---

## 1. 🎨 UX / Design Focused

### 1.1 Meta Astryx — Meta 开源「Agent-First」React 设计系统，150+ 组件 + CLI + MCP

- **链接**：[Meta Astryx 开源公告](https://www.marktechpost.com/2026/07/21/meta-open-sources-astryx-an-agent-ready-react-design-system-with-150-accessible-components-seven-themes-and-a-cli/) | [@astryxdesign/core](https://www.astryxdesign.com)
- **类型**：Design System / Agent-Ready / React Components / CLI + MCP
- **发布时间**：🔴 24h内 — 2026-07-21 正式开源（Beta）
- **做什么**：Astryx 是 Meta 内部最大设计系统，经 8 年生产验证后于 2026-07-21 以 MIT 协议开源。包含 160+ 无障碍 React 组件、7 套主题、暗黑模式、页面模板、以及一个 CLI（`@astryxdesign/cli`）。CLI 支持列出并脚手架模板、打印完整组件文档、生成主题、运行 codemod 版本迁移，以及通过 **MCP 暴露机器可读文档**——让 AI 编码代理（Claude Code、Cursor 等）可以精确读取组件 API 而非依赖训练数据猜测。
- **核心能力**：
  - 160+ React 19+ 组件，一致的命名/prop/组合规则，人和 AI 均可预测行为
  - StyleX 驱动，行为与无障碍在系统内处理，视觉外观通过 CSS Token 主题覆盖
  - CLI MCP 模式：任何 AI 编码代理可实时查询最新组件文档，告别"AI 乱猜 prop"问题
  - 支持 Next.js（Tailwind/StyleX）、Vite、无构建 CDN（unpkg / jsDelivr）
- **使用场景**：团队使用 Claude Code 生成 UI 时，Claude 通过 Astryx CLI 的 MCP 接口读取最新组件规范，生成的代码直接符合 Meta 级别的无障碍与设计标准，无需事后大量修正。
- **为什么重要（UX视角）**：Astryx 是"Agent-First 设计系统"理念的最权威实现案例——Meta 明确表示，每一个让 AI 更易使用的改动，同时也让设计师更易使用。这是**设计系统与 AI 编码代理深度集成**的里程碑：不是把设计系统"适配"给 AI，而是从立项起就把 AI 当一等公民。Design → Dev gap 直接在系统层消解。
- **是否值得收藏**：✅ Yes — Meta 8 年生产验证背书，MIT 开源；CLI + MCP 让 AI 代理实时获取权威组件文档，是目前最具可信度的 Agent-First 设计系统方案。

---

### 1.2 ProtoPie MCP — 高保真原型工具原生接入 MCP，Studio + Code 双轨工作流

- **链接**：[ProtoPie MCP 发布公告](https://www.einpresswire.com/article/927085421/protopie-launches-native-mcp-support-connecting-human-precision-to-the-era-of-ai-vibe-coding)
- **类型**：Prototyping / MCP Integration / Design-Dev Handoff
- **发布时间**：🔴 24h内 — 2026-07-20 正式发布，今日可用
- **做什么**：ProtoPie 在 2026-07-20 推出原生 MCP 支持，推出双支柱系统：**Studio MCP**（设计端，BYOM 模式，将 Claude Code / Cursor / Codex 等 AI 助手直接接入 ProtoPie Studio，用自然语言生成复杂交互逻辑）和 **Code MCP**（开发端，将可视化原型中的变量、公式、触发器转为机器可读的开放格式，AI 编码代理可直接翻译为干净的生产代码）。
- **核心能力**：
  - Studio MCP：一次生成交互结构，其余 10% 在 ProtoPie 画布上手动精修——**彻底规避持续 re-prompting 的 Token 消耗**
  - Code MCP / Dev View：开发者在 Dev View 中检查交互并复制目标链接，直接喂给 AI 编码环境
  - 支持传感器/跨设备/IoT 原型（AI 屏幕生成工具的盲区），不仅限于屏幕内交互
  - Figma Import + ProtoPie AI 协同：快速导入静态稿 → AI 生成交互结构 → 手动精调 → Code MCP 交付
- **使用场景**：产品团队在 ProtoPie 中验证完复杂手势交互逻辑后，通过 Code MCP 将交互规格直接传给 Claude Code，工程师无需重新解读设计稿——原型本身成为开发的"源头真相"。
- **为什么重要（UX视角）**：ProtoPie MCP 直接回应了"vibe-coding 隐形成本"问题——re-prompting token 消耗、黑盒验证陷阱、仅限屏幕的生成局限。它代表一种新的设计-开发协作范式：**人类做精准控制，AI 做初始生成和代码翻译，MCP 成为连接精度层和效率层的协议**。
- **是否值得收藏**：✅ Yes — 高保真原型领域首家原生 MCP 集成，Studio + Code 双轨解决"AI 速度 vs 交互精度"核心矛盾；对复杂交互产品（IoT/汽车 HMI/跨设备应用）尤其不可替代。

---

### 1.3 Google Stitch Skills — Google Labs 开源 Design-to-Code MCP Agent Skills 库（14 项技能）

- **链接**：[aitodaybrief.com 报道](https://aitodaybrief.com/en/high-performance-embeddings-and-local-llm-text-classification/google-labs-releases-stitch-skills-agent-library-for-design-to-code-workflows) | [pyshine.com 深度解析](https://pyshine.com/Stitch-Skills-Google-Stitch-Agent-Skills-Design-to-Code/) | [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills)
- **类型**：Agent Skills Library / Design-to-Code / MCP Compatible
- **发布时间**：🟡 3天内 — 开源更新与媒体报道集中于 2026-07-16~19；6,900 stars，Apache-2.0
- **做什么**：Stitch Skills 是 Google Labs 开源的 MCP 兼容 Agent Skills 库，将 AI 编码代理（Claude Code、Cursor、Codex、Gemini CLI）与 Google Stitch 设计平台双向打通。共 14 个 Skill，分三大插件：`stitch-design`（前端代码→Stitch 设计、生成 UI 变体、管理设计系统）、`stitch-build`（Stitch 设计→React/React Native 组件、Remotion 视频、shadcn-ui 集成）、`stitch-utilities`（提示词增强、DESIGN.md 生成）。旗舰技能 `stitch-loop` 可从单个 prompt 生成完整多页网站并自动验证。
- **核心能力**：
  - `stitch::code-to-design`：将现有 React/Vue 前端代码逆向提取为 Stitch 设计
  - `stitch::react-components` / `react-native`：将 Stitch 设计转换为生产就绪组件代码
  - `stitch::extract-design-md`：从 `/src` 目录直接提取 `DESIGN.md` 设计系统文档
  - `stitch::stitch-loop`：单 prompt → 完整多页网站，附带自动化验证
- **使用场景**：前端团队在 Claude Code 中运行 `stitch::code-to-design`，将现有 React 组件库逆向同步至 Stitch 设计平台，设计师在 Stitch 中做变体后，开发者再用 `stitch::react-components` 拉回代码——实现真正双向的 Design ↔ Code 同步。
- **为什么重要（UX视角）**：Stitch Skills 是 Google Labs 对"设计与开发双向同步"的具体实现——不仅是单向 design-to-code，而是**形成设计-开发闭环**。14 个标准化 Skill + DESIGN.md 强制模板，体现 Google 将 MCP Skills 标准化推进到设计工具领域的战略意图。
- **是否值得收藏**：✅ Yes — Google Labs 出品；14 个精心设计的 Skill 覆盖完整设计-开发链路；双向同步能力是目前开源方案中的稀缺功能。

---

### 1.4 Nutlope/hallmark — 11K Stars 反 AI 套话设计 Skill，57 道质量门控

- **链接**：[github.com/Nutlope/hallmark](https://github.com/Nutlope/hallmark) | [explainx.ai 技能详情页](https://explainx.ai/skills/Nutlope/hallmark/hallmark)
- **类型**：Design Skill / Anti-Slop / UI Quality Gate
- **发布时间**：🟡 3天内 — explainx.ai 深度报告发布于 2026-07-17；v1.1.0 持续增长，11.1K stars
- **做什么**：Hallmark 是 Together AI 出品的反 AI 套话设计 Skill。问题背景：让 AI 生成"落地页"时，结果总是紫色渐变 + 三张特性卡 + "Revolutionize your workflow" 的千篇一律视觉。Hallmark 通过编码拒绝这些"分布均值"的规则，并在输出代码前运行 **57 道 slop-test 质量门控**（+ 6 轴前置批评：哲学 / 层次 / 执行 / 具体性 / 克制 / 多样性）。支持四个动词：`build`（默认）/ `audit` / `redesign` / `study`，可用于新建 UI、审计现有代码、重建视觉结构或提取设计 DNA。
- **使用场景**：在 Claude Code 中执行 `/hallmark redesign index.html`——Skill 抛弃现有视觉结构，保留内容和信息架构，基于内置的 20 个布局主题（Carnival、Modern-Minimal 等）重建视觉指纹，输出自包含 HTML + CSS，风格保证不重复。
- **是否值得收藏**：✅ Yes — 57 门控 + 6 轴批评体系是目前开源 Skill 中最严格的 UI 质量控制机制；对需要大量生成落地页/营销页面的产品团队有直接价值；11K stars 证明社区认可。

---

## 2. ⚙️ GitHub Trending Agents

### 2.1 JustVugg/colibri — 纯 C 实现，25GB 消费级内存运行 744B GLM-5.2 MoE 大模型

- **链接**：[github.com/JustVugg/colibri](https://github.com/JustVugg/colibri)
- **类型**：Local LLM Runtime / Consumer Hardware / High-Performance Inference
- **发布时间**：🔴 24h内 — v1.0.0 发布于 2026-07-19；最近一次 push：2026-07-21；17,536 stars，60 位贡献者
- **功能**：colibri 是一个纯 C 编写、零依赖的 MoE 推理引擎，可在约 25GB RAM 的消费级设备上运行 GLM-5.2（744B 参数 MoE 模型）。核心设计：MoE 模型每个 token 只激活约 40B 参数，colibri 将 dense 部分（~9.9GB）常驻 RAM，19,456 个稀疏专家（~370GB）从磁盘按需流式加载，配合 per-layer LRU 缓存 + 学习型热点固定（`.coli_usage` 自动记录热点专家，越用越快）。单文件 C 实现（`c/glm.c`），无 BLAS，无 Python 运行时，无 GPU 要求。
- **使用场景**：本地开发机（Macbook Pro、工作站）上私有化运行 744B 量级大模型，用于对话、Agent 本地推理后端、离线代码生成——彻底摆脱 API 费用与数据上传隐患；适合需要本地隐私保护的 B 端产品开发团队。
- **是否值得收藏**：✅ Yes — 744B 级别模型的消费级硬件运行是行业突破；60 位贡献者 + v1.0.0 正式版证明稳定性；学习型缓存设计有创新价值；对追求本地化 AI 推理的工程团队意义重大。

---

### 2.2 usestrix/strix v1.2.0 — 开源 AI 渗透测试 Agent 框架，多 Agent 协作找漏洞

- **链接**：[github.com/usestrix/strix](https://github.com/usestrix/strix)
- **类型**：Multi-Agent / Security / AI Pentesting Framework
- **发布时间**：🔴 24h内 — v1.2.0 发布于 2026-07-21；43,193 stars，1.2K+ forks
- **功能**：strix 是开源 AI 自动化渗透测试框架，多个专业化 AI Agent 协作（侦察、利用、后渗透），模拟真实黑客行为。v1.2.0 核心特性：增强 LiteLLM 依赖支持更多模型提供商、`force_required_tool_choice` 设置、多 Agent 协调架构强化、GitHub Actions CI/CD 原生集成（PR 自动安全扫描）。输出包括 PoC 可利用漏洞证明 + 一键 autofix PR。
- **使用场景**：产品团队将 strix 接入 GitHub Actions，每次 PR 自动触发安全扫描；CI/CD 阻断不安全代码合并到生产，生成合规报告（SOC 2、ISO 27001、PCI DSS）。
- **是否值得收藏**：✅ Yes — 43K stars 是 Security Agent 赛道最具规模的开源项目之一；Multi-Agent 协作架构可直接参考用于其他复杂 Agent 设计；CI/CD 集成让安全测试进入日常工程流程。

---

## 3. 🧩 Claude Skills

### 3.1 Claude Code W29：Artifacts 可通过 MCP 连接器实时拉取数据（2026-07-13~17）

- **链接**：[Claude Code Docs — Week 29 更新](https://code.claude.com/docs/en/whats-new/2026-w29)
- **Skill 名称**：Artifact MCP Live Data（制品实时数据连接）
- **发布时间**：🟡 3天内 — W29 更新，发布区间 2026-07-13~17
- **工作流描述**：W29 最重要更新：**发布的 Artifact 现在可在每次查看时调用 MCP 连接器**——仪表盘展示的是实时数据而非构建时的快照。查看者访问时，系统通过其本人账户的 MCP 连接运行，首次调用前需查看者授权。同期还新增了 Artifact 公开分享链接、Team/Enterprise 计划编辑者角色、Claude Tag 会话创建 Artifact。辅助更新：MCP 工具调用超过 2 分钟自动移入后台，通过 `CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS` 调整阈值；新增屏幕阅读器模式（`axScreenReader` 设置）。
- **使用时机**：
  - 需要构建"实时仪表盘 Artifact"——数据在查看时实时拉取而非构建时固化 → **启用 Artifact MCP 连接器**
  - MCP 工具调用耗时过长影响会话响应 → 依赖自动后台化（2分钟阈值）
  - 团队需要多人协作编辑同一 Artifact → 使用编辑者角色（Team/Enterprise）

---

## 4. 💡 Emerging Patterns（今日新范式）

### Pattern 1: 设计系统进入「Agent-First」时代——人机共用同一 API

Meta Astryx 和 mahmoudilyan/marmoui 均明确宣示「Agent-First 设计系统」理念：**同一套组件 API、文档和 CLI（可通过 MCP 暴露），人和 AI 编码代理使用同一份参考**。这不是给设计系统"打补丁"以适配 AI，而是从底层架构决策开始就把 AI 代理当一等公民。含义：未来的设计系统评估标准将增加"AI 可用性"这一维度——组件命名一致性、prop 预测性、MCP 文档覆盖率。

### Pattern 2: MCP 成为设计工具的标准交付协议（ProtoPie + Google Stitch + marmoui 三线验证）

本周三个来自不同方向的设计工具——高保真原型（ProtoPie）、设计平台（Google Stitch）、React 组件库（marmoui）——均选择 **MCP 作为连接 AI 编码代理的核心协议**。这标志着 MCP 在设计工具领域的地位从"实验性集成"转变为"行业事实标准"。对 UX 工程团队的含义：工具选型应将"是否原生支持 MCP"列为关键评估标准。

### Pattern 3: 「反套话」质量门控成为 AI 生成 UI 的必要基础设施

Hallmark（11K stars）的爆发式增长说明一个真实痛点：AI 大量生成 UI 时，视觉趋同（"AI slop"）已成为团队交付质量的主要威胁。57 道质量门控作为 Skill 的封装，代表**质量约束从人工 review 流程转向 AI 可执行的规则系统**。预计"Anti-Slop Skill"将成为各类生产内容团队（落地页、营销站点、SaaS 产品页）的标配组件。

### Pattern 4: 本地大模型推理进入「消费级硬件 + 生产质量」新阶段

colibri（JustVugg）在 25GB 消费级内存上运行 744B MoE 模型，且引擎自我学习热点专家持续提速——这意味着"本地化私有 Agent"从小模型的妥协方案升级为旗舰模型的可行路径。对注重数据安全的产品团队，本地部署 Agent 的可行性门槛在 2026 年 7 月显著降低。

---

## 📊 今日信号总结

| 项目 | 类型 | 时间信号 | UX 相关度 | 推荐优先级 |
|------|------|---------|-----------|-----------|
| Meta Astryx（Agent-First 设计系统）| Design System + MCP | 🔴 24h内 | ⭐⭐⭐⭐⭐ | 🔴 必看 |
| ProtoPie MCP（原型工具原生 MCP）| Prototyping + Handoff | 🔴 24h内 | ⭐⭐⭐⭐⭐ | 🔴 必看 |
| Google Stitch Skills（14个 design-to-code Skill）| Agent Skills Library | 🟡 3天内 | ⭐⭐⭐⭐⭐ | 🔴 必看 |
| Nutlope/hallmark v1.1.0（反 AI 套话设计 Skill）| Design Quality Skill | 🟡 3天内 | ⭐⭐⭐⭐ | 🟠 重要 |
| JustVugg/colibri v1.0.0（消费级硬件 744B MoE）| Local LLM Runtime | 🔴 24h内 | ⭐⭐ | 🟠 重要 |
| usestrix/strix v1.2.0（AI 渗透测试 Agent）| Security Multi-Agent | 🔴 24h内 | ⭐⭐ | 🟡 参考 |
| Claude Code W29：Artifact MCP 实时数据 | Platform Feature | 🟡 3天内 | ⭐⭐⭐ | 🟡 参考 |

---

*生成时间：2026-07-22 | 数据来源：GitHub Trending / MarkTechPost / EINPresswire / aitodaybrief / PyShine / explainx.ai / Claude Code Docs W29*
