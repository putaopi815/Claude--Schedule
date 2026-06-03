# 🧠 AI Skills & Agents Daily — 2026-06-03

> **Date**: 2026-06-03
> **Time Window**: 过去 24h（优先）/ 3 天内（补充）
> **Sources Checked**: GitHub Trending / Anthropic Blog / Claude Platform Release Notes / GitHub Changelog / TechGenyz
> **Dedup Check**: ✅ 已对比 2026-05-20 报告（Claude Managed Agents / mattpocock/skills / OpenHuman / LangGraph v1.2 / anthropics/skills 已收录，本期不重复）

---

## 1. 🎨 UX / Design Focused

### 1.1 Tencent Miora — AI 创意 Agent Studio：图像 + 视频 + UI/UX + 3D 一体化

- **链接**：https://miora.design
- **类型**：Creative Agent Studio / UX Generation / Multi-modal
- **发布时间**：🟡 3天内 — 2026-05-29 国际 Beta 发布
- **做什么**：腾讯推出全能 AI 创意 Agent Studio，将图像生成、视频制作、UI/UX 设计、故事板和 3D 资产整合到单一工作区。内置 "Specialist Crew"（品牌 / 插图 / 故事板 / 视频 / UI-UX / 3D 分工 Agent），支持用户自定义 Skills 并向社区共享工作流。
- **核心能力**：
  - 单 Canvas 多模态生成（图像 / 视频 / UI / 3D 不切换工具）
  - 任务型 AI Specialist Agent（专项 Agent 分工协作）
  - 自定义 Skills + Workflow 社区共享机制
  - 上下文感知：记住用户偏好，自主调用工具，跨 workflow 协作
- **使用场景**：设计师在 Miora 描述"移动端 SaaS 落地页"→ UI/UX Specialist Agent 生成交互原型 → 切换 3D 模块添加产品渲染 → 一键导出到开发工作流，全程不离开单一工作区，无跨工具上下文丢失。
- **为什么重要（UX视角）**：直接对标 Figma + Adobe + Midjourney 的碎片化工作流。Single Canvas + Skills 体系（类 Claude Code Skills 但面向创意场景）开创"创意 Agent Skills"新品类。腾讯明确全球化布局（非中国专属）。**Design → Dev gap 缩短信号：强。**
- **是否值得收藏**：✅ Yes — UX 创意 Agent Studio 赛道标杆产品，国际 Beta 中，适合设计团队早期评测入场。

---

### 1.2 OpenAI Codex Sites — 无代码 App 生成器：文档 / 计划一键变 Web App

- **链接**：https://openai.com（via blockchain.news 2026-06-02）
- **类型**：No-code Web App Builder / Document-to-App
- **发布时间**：🔴 24h内 — 2026-06-02 发布，Business / Enterprise 计划先行
- **做什么**：OpenAI 在 Codex 内推出 Sites 功能——将文档、计划、想法直接转为带 URL 的交互式 Web App。非技术用户无需写代码即可生成功能性产品展示页或数据看板，输出可实时基于反馈更新。
- **核心能力**：自然语言 → 交互式网站 / 数据看板、文档 / 项目计划 → 功能 App、实时反馈更新、一键分享 URL
- **使用场景**：PM 将产品路线图文档上传至 Codex Sites，获得交互式展示页；设计团队将设计说明书转为可点击原型与利益相关方共享——全程无需前端工程师介入。
- **为什么重要（UX视角）**：将"文档 → 原型"路径压缩到极致，打通 PM / 设计 → 开发 gap 的最后一公里。与 Claude Design（从设计系统出发）形成互补——两者共同推动 No-code 原型成为行业标配，快速验证设计意图的门槛将降至零。
- **是否值得收藏**：✅ Yes — OpenAI 在 no-code 方向的重要入场，为 UX 工作流"快速原型展示"提供新选项，值得与 Claude Design 并行评估。

---

## 2. ⚙️ GitHub Trending Agents

### 2.1 HKUDS/nanobot v0.2.1 — 44K Stars 轻量 Agent：WebUI 升级为全功能工作台

- **链接**：https://github.com/HKUDS/nanobot
- **类型**：Open-source AI Agent / Long-running Workflow / MCP-native
- **发布时间**：🔴 24h内 — 2026-06-01 发布，84 PRs 合并，17 位新贡献者
- **功能**：开源轻量 AI Agent，v0.2.1 重大升级三条主线：
  - **WebUI 真正工作台化**：实时文件编辑可见、工具 trace 渲染清晰、项目工作区 + 访问控制 + 模型切换 + Slash 命令，WebUI 从"打包的聊天界面"升级为全天候工作台
  - **长运行 Agent 稳定性**：Goal 模式续跑、per-session 锁防竞争条件、AutoCompact 竞态修复、无神秘中断
  - **CLI Apps + MCP 统一扩展路径**：extension registry 让"本地工具 → nanobot 工作流"路径标准化，Gateway 冷启动从秒级降至亚秒
- **使用场景**：设计工程师将自定义 MCP 工具（Figma API / design token 解析器）注册为 nanobot 扩展后，在 WebUI 启动多小时批量组件审查 Agent 任务，完成后通过 Signal / Telegram / Discord 推送结果报告。
- **是否值得收藏**：✅ Yes — 44K stars，v0.2.1 是里程碑版本，WebUI 升级使其成为开源 Agent 中 UX 最完善的日常工作台候选，MCP 原生支持是加分项。

---

### 2.2 simstudioai/sim v0.6.99 — 29K Stars AI Agent 调度平台：34 工具 iMessage 集成 + 多云模型

- **链接**：https://github.com/simstudioai/sim
- **类型**：Agent Orchestration Platform / Multi-channel / Multi-provider
- **发布时间**：🔴 24h内 — 2026-06-02 发布
- **功能**：AI Agent 构建、部署、调度平台（定位"AI 劳动力中央智能层"），v0.6.99 新增：
  - Linq iMessage / SMS / RCS 集成（34 个工具，块级操作 + 附件上传）
  - 新增 Together AI、Baseten、Ollama Cloud 模型提供商
  - Tables 过滤器扩展（not-contains、starts/ends-with、not-in、empty 操作符）
- **使用场景**：UX 研究团队用 sim 构建"用户访谈调度 Agent"——自动通过 iMessage/SMS 发送邀请，收到回复触发下一节点（日历预约 / 资料发送），全流程 Agent 自动完成，无人工干预。
- **是否值得收藏**：✅ Yes — 29K stars 持续快速迭代；iMessage 集成让 Agent 触达渠道大幅拓展，多云模型支持增强灵活性，是构建跨渠道 UX 研究自动化的有力底座。

---

### 2.3 openclaw v2026.6.1-beta.1 — 376K Stars AI 助手：Skill Workshop 治理工作流 + Workboard 多 Agent 调度

- **链接**：https://github.com/openclaw/openclaw
- **类型**：Personal AI Assistant / Skills Governance / Multi-agent Orchestration
- **发布时间**：🔴 24h内 — 2026-06-01 beta 发布
- **功能**：超高星 (376K!) 个人 AI 助手，本期 beta 重点：
  - **Skill Workshop**：带治理流程的技能创建系统（提案 → 审查 → 批准 → 部署 / 拒绝 / 隔离，支持 CLI / Gateway / Agent 工具审查，含回滚元数据）
  - **Workboard**：多 Agent 协调原语 + 任务追踪，用于多 Agent 并行规划与状态管理
  - **Skills 运行时统一加载**：技能索引 + 状态过滤 + prompt 格式化，Skills 生命周期全流程管理
- **使用场景**：设计系统团队通过 Skill Workshop 提交"自动检查 WCAG 可访问性"技能提案，经 reviewer 审查批准后部署为共享 Skill；团队任何成员触发该 Skill，享受标准化可访问性审查工作流，不符合规范的版本可随时 rollback。
- **是否值得收藏**：✅ Yes — 376K stars 极强社区基础；Skill Workshop 治理模型是 Skills 生态走向企业合规的重要参考，Workboard 为复杂多 Agent 任务提供任务级协调原语。

---

## 3. 🧩 Claude Skills（本期重点）

### 3.1 Claude Code Dynamic Workflows（"ultracode" 触发词） — Claude 自写 Agent 编排代码

- **链接**：https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code
- **类型**：Claude Code Feature / Dynamic Agent Orchestration
- **发布时间**：🔴 24h内 — 2026-06-02 官方博客发布，同日 Claude Code v2.1.160 将触发词正式改为 `ultracode`
- **工作流描述**：Claude Code 现可根据任务即时**自动生成并执行多 Agent 编排逻辑（harness）**，无需预先定义工作流。Claude Opus 4.8 根据任务需求实时生成最优 harness，执行完成后可按 `s` 保存工作流，并通过 Skill 分发。官方已在 Skills 仓库发布 `/deep-research` 动态工作流（fan-out 搜索 → fetch → 逆向验证 → 合成引用报告）。触发方式：在 Claude Code prompt 输入 `ultracode` 关键词（紫色高亮显示）。
- **为什么重要（UX视角）**：这是 AI Coding Agent 的范式跳跃——从"固定工作流模板"转向"按需生成编排代码"。UX 含义：不再需要预先设计 Agent 工作流，Claude 根据具体任务自动设计最优执行路径，将 Agent 工作流复杂度从"工程师设计"转移到"模型即时生成"。**Design → Dev gap 缩短信号：范式级。**
- **使用时机**：遇到超出单次对话、需要多步骤 Agent 协作的复杂任务时（如：批量组件迁移、多文件设计规范检查、大型代码库重构审计），在 prompt 中键入 `ultracode` 触发动态工作流自动生成与执行。

---

### 3.2 Claude Platform Agent Skills API — 官方 Skills 开放 API + Office / PDF 预置 Skills

- **链接**：https://platform.claude.com/docs/en/release-notes/overview
- **类型**：Claude API / Agent Skills / Pre-built Skills
- **发布时间**：🔴 24h内 — 2026-06-02 Platform Release Notes 正式发布
- **工作流描述**：Anthropic 正式推出 Agent Skills API（`skills-2025-10-02` beta）：
  - **Anthropic 管理的预置 Skills**：开箱即用处理 PowerPoint（.pptx）、Excel（.xlsx）、Word（.docx）、PDF 文件（需开启代码执行工具）
  - **自定义 Skills 上传 API**：通过 `/v1/skills` 端点上传包含专领域指令 + 脚本 + 资源的 Skills 包，注入组织知识和工作流
  - 同日：MCP Tunnels、Self-hosted Sandboxes 正式升级为 Research Preview 可用，Claude Code Workflows 成为 Research Preview
- **使用时机**：
  - 需要 Claude API 应用处理企业文档（PPT 提案分析、Excel 数据报告、PDF 合同审查）时，直接加载 Anthropic 预置 Office Skills
  - 需要将团队专有设计流程（如特定组件规范检查 / 品牌一致性验证）封装为可复用 Skills 时，通过 `/v1/skills` 上传自定义 Skill 包

---

## 4. 💡 Emerging Patterns（今日新范式）

### Pattern 1: 动态编排——Agent 自写 Orchestration 代码

Claude Code Dynamic Workflows 标志着关键跃迁：AI 不再执行人预写的编排逻辑，而是**根据任务即时生成最优编排**。与 LangGraph（静态 DAG）、固定 Skill 链路形成根本对比——orchestration complexity 从"工程师设计"转移到"模型按需生成"。UX 工作流自动化的门槛将大幅降低：你只需描述目标，Claude 负责设计执行路径。这是 2026 年 Agent 工程的最重要范式变化之一。

### Pattern 2: Skills 治理化——从"个人技能包"到"组织级审批流程"

openclaw Skill Workshop（提案 → 审查 → 批准 → 回滚）和 Anthropic Agent Skills API（组织级 Skills 上传 / 管理）共同指向：Skills 从"个人工具"走向**组织资产**，需要治理、版本控制、访问控制和回滚机制。预示 2026 下半年将出现 Skills Registry / Skills Governance 专属工具品类。

### Pattern 3: 调度作为原生 Agent 行为

GitHub Copilot CLI 的 `/every 30m` `/after 2h` 调度命令，nanobot 的 Goal 续跑模式，以及 sim 的 Tables Workflow 计划任务——共同推动**定期 / 延迟执行成为 Agent 的内置基元**，而非依赖外部 cron。对 UX 工作流的意义：自动化"每日设计系统一致性检查""每周可访问性审计"等周期性任务成为标配，UX 质量保障从人工触发走向 Agent 自驱。

### Pattern 4: 创意生产力 → Agent Studio 化

Tencent Miora（多模态创意 Agent）、OpenAI Sites（文档 → App）、Claude Design（设计 → 代码）三者同期爆发，指向同一大趋势：**创意 / 设计生产工具正在被重构为 Agent Studio**——核心协作对象从"工具"变成"Agent"，设计师角色从"执行者"转向"Agent 导演"。入局窗口期正在收窄。

---

## 📊 今日信号总结

| 项目 | 类型 | 时间信号 | UX 相关度 | 推荐优先级 |
|------|------|---------|-----------|-----------|
| Claude Code Dynamic Workflows (ultracode) | Claude 特性 | 🔴 24h内 | ⭐⭐⭐⭐⭐ | 🔴 必看 |
| Claude Platform Agent Skills API | Claude API | 🔴 24h内 | ⭐⭐⭐⭐⭐ | 🔴 必看 |
| Tencent Miora | UX/创意 Agent Studio | 🟡 3天内 | ⭐⭐⭐⭐⭐ | 🟠 重要 |
| openclaw Skill Workshop | Skills 治理 | 🔴 24h内 | ⭐⭐⭐⭐ | 🟠 重要 |
| HKUDS/nanobot v0.2.1 | 开源 Agent | 🔴 24h内 | ⭐⭐⭐ | 🟠 重要 |
| OpenAI Codex Sites | No-code App 生成 | 🔴 24h内 | ⭐⭐⭐⭐ | 🟡 参考 |
| simstudioai/sim v0.6.99 | Agent 调度平台 | 🔴 24h内 | ⭐⭐⭐ | 🟡 参考 |

---

*生成时间：2026-06-03 | 数据来源：Anthropic Blog / Claude Platform Release Notes / GitHub Releases / TechGenyz / GitHub Changelog / blockchain.news*
