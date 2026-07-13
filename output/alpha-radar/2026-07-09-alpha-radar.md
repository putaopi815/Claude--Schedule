# Claude Code Signal — 2026-07-09

> **Date**: 2026-07-09
> **Time Window**: 过去 24h（优先）/ 3 天内（补充）
> **Sources Checked**: VS Code Changelog / Claude Code Releasebot / GitHub / DEV Community / Exa
> **Dedup Check**: ✅ 已对比 2026-07-02 报告，以下内容均为本周新增

---

## 1. VS Code 1.128：一个 Claude Session 内运行多个并行 Chat，支持 Fork 和只读 Subagent 视图

🔴 24h内 | 2026-07-08 发布

**Source**:
- [Visual Studio Code 1.128 Release Notes](https://code.visualstudio.com/updates/v1_128)
- [Visual Studio Code 1.128 Launches with Multi-Chat Claude Agents — NT Compatible](https://www.ntcompatible.com/story/visual-studio-code-1128-launches-with-multichat-claude-agents-and-ga-copilot-vision)

**Summary（做了什么）**:
VS Code 1.128（7 月 8 日发布）为 Claude Agent Sessions 增加了 **Multi-Chat**：同一个 Session 内可以开启多个独立 Chat，各自保有独立的对话历史、标题和模型选择。支持从任意历史节点 Fork 出新 Chat（探索替代实现），多个 Chat 可以同时发送请求并行运行。同期发布**只读 Subagent Chat 视图**：当 Agent 派发 Subagent 时，可以在 Agents 窗口跟踪每个 Subagent 的实时进度，而不会干扰主 Chat 流程。此外新增 **Quick Chat**（无工作区的临时问答），以及 Copilot Vision（图片/PDF 拖拽附件）正式 GA。

**Key Insight（核心洞察）**:
**Multi-Chat Session 将 Claude Agent 从"单线程工具"变为"并行工作空间"。** 此前，同一个问题的不同解法必须分开成不同 Session，上下文完全隔离。现在，同一 Session 内的多个 Chat 共享 Session 级别的状态，可以同时执行"主 Chat 实现功能 + 对比 Chat 探索替代方案 + Fork Chat 写测试"——这实际上是把团队协作的并行工作模式带入了单人 AI 会话中。只读 Subagent 视图则解决了 Dynamic Workflow 运行时的"黑盒焦虑"：知道 Subagent 在做什么，但不打断它。

**Why it matters（为什么重要）**:
对于 UX/产品团队：可以在同一 Session 内并行比较多个 UI 方案——一个 Chat 生成 Option A，另一个生成 Option B，Fork Chat 进行组件拆解，全程保持同一上下文（设计稿、约束条件、品牌规范）无需重复输入。对于技术团队：Multi-Chat + Dynamic Workflows 的结合，让一个 Session 同时覆盖"主线开发 + 独立审查 + 性能分析"，彻底改变了"一次只能做一件事"的使用范式。

**How to apply（如何应用）**:
UX 并行原型工作流：
1. 在 Claude Agent Session 中描述设计目标（含 Figma 约束、设计令牌）
2. `+ New Chat` → "实现方案 A：卡片式布局"
3. `+ New Chat` → "实现方案 B：列表式布局"
4. 在两个 Chat 都输出结果后，`Fork Chat` 从最优方案分支出"编写可访问性测试"
5. Agents 窗口的 Subagent 面板实时追踪各 Chat 执行进度

---

## 2. slang-workflows：用类型化 .slang 文件声明多 Agent 工作流，非 LLM 确定性状态机执行

🔴 24h内 | 2026-07-07 发布

**Source**:
- [slang-workflows: provable multi-agent workflows for Claude Code — DEV Community](https://dev.to/alsterg/slang-workflows-provable-multi-agent-workflows-for-claude-code-jom)
- [GitHub — shofer-dev/claude-code-slang-orchestrator](https://github.com/shofer-dev/claude-code-slang-orchestrator)

**Summary（做了什么）**:
`slang-workflows` 是一个 Claude Code 插件，将 Dynamic Workflows 的"LLM 写脚本执行"模式推进为**可证明执行**：用户用类型化的 `.slang` 文件声明 Agent 协作拓扑（Agent 定义、消息路由、控制流、Budget 约束），由**纯 JavaScript 状态机**（非 LLM）负责执行和强制约束。关键能力：① **输出合约**（`output: {…}` schema + `where score >= 0 && score <= 100` 语义验证，违约自动重提示）；② **静态分析**（`validate_workflow` 在运行前检测死锁、无效引用、孤立输出）；③ **工具作用域**（`write_paths`/`deny` 限制每个 Agent 可写路径，由运行时而非 Prompt 强制执行）；④ **可证明终止**（Budget + 超时保证无死循环）；⑤ **自动拓扑图**（`get_topology` 输出 Mermaid 流程图，`get_trace` 输出执行序列图）。

**Key Insight（核心洞察）**:
**slang-workflows 提出了一个根本性的问题："为什么 Agent 协作的约束应该由 LLM 来维护？"** Dynamic Workflows 让 Claude 写 JS 编排脚本，仍是"LLM 自己决定如何遵守约束"——这对高可靠性场景（合规审查、财务数据处理、安全扫描）是不够的。slang-workflows 将约束的执行从 LLM 层移到确定性状态机层：**LLM 负责生成内容，状态机负责验证合约**。这是一个重要的架构分离：生成能力（随机性、创造性）与执行约束（确定性、可验证性）各司其职。

**Why it matters（为什么重要）**:
对于需要合规性保证的工作流（代码安全审计、合同生成、医疗文档）：纯 Dynamic Workflows 无法向监管机构证明"每一步都按规程执行"。slang-workflows 的 `validate_workflow` + 执行日志提供了可审计的执行证明。对于工程团队：`get_topology` 自动生成 Mermaid 拓扑图，让 Agent 系统的架构可视化——这解决了"多 Agent 系统黑盒"的文档问题，同时也是 PR Review 时解释 Agent 协作逻辑的利器。

**How to apply（如何应用）**:
```
/plugin marketplace add shofer-dev/claude-code-slang-orchestrator
/plugin install slang-workflows@shofer-slang-orchestrator
```
推荐场景：
- **代码安全审计 Workflow**：每个 Agent 只能读取指定路径（`deny: write`），输出合约验证报告格式，静态分析确保无漏步
- **设计规范检查 Workflow**：Figma 读取 Agent → 组件比对 Agent → 问题报告 Agent，每步有 schema 验证，`get_trace` 生成完整执行记录
- LLM 可以动态生成 `.slang` 文件（`get_slang_grammar` → `validate_workflow` → `run_workflow`），兼顾灵活性与确定性保证

---

## 3. Claude Code Week 27：Dynamic Workflow Size 设置、登录过期预警、更丰富的 Workflow 遥测

🔴 24h内 | 2026-07-07~09 发布（v2.1.204）

**Source**:
- [Claude Code Updates by Anthropic — July 2026 — Releasebot](https://releasebot.io/updates/anthropic/claude-code)
- [Claude Code Changelog July 2026 — Gradually.ai](https://www.gradually.ai/en/changelogs/claude-code/)

**Summary（做了什么）**:
本周（Week 27）Claude Code 发布了几个对生产 Agent 工作流有实际影响的更新：① **Dynamic Workflow Size 设置**：新增配置项，允许用户/管理员设定单个 Workflow 的最大 Subagent 规模（防止意外触发巨型 Workflow 消耗大量 Token）；② **登录过期预警**：在后台 Session Token 即将过期前主动提示，避免隔夜任务因认证失效静默失败；③ **Workflow 遥测增强**：更丰富的 `/workflows` 面板数据，包括每个 Agent 耗时、状态转换历史；④ **Manual Mode 徽章**：在 Agent Status 显示当前是否处于手动审批模式，减少"我以为 Agent 在自动执行"的混淆；⑤ **`/review` 恢复快速单次通道**：此前 `/review` 被调整为深度多 Agent 流程，本次恢复为快速单次审查，用户可按需选择深度。

**Key Insight（核心洞察）**:
**Workflow Size 限制 + 遥测增强，标志着 Claude Code 进入"可观测性阶段"**——从"让 Agent 能做到"转向"让用户知道 Agent 在做什么、花了多少"。登录过期预警看似小细节，实则解决了一个真实的生产痛点：设置隔夜 Dynamic Workflow 后发现第二天任务因 Token 过期静默失败是社区反馈中高频问题。这类"可靠性基础设施"的持续投入，是 Claude Code 从个人 POC 工具走向企业生产系统的关键路径。

**Why it matters（为什么重要）**:
对于运行大规模 Dynamic Workflows 的团队：Workflow Size 设置提供了成本护栏，配合 `budget` API 可以实现双重保护（按 Token 数 + 按 Subagent 数）。登录过期预警对于 Claude Code on the Web / Remote 用户尤其重要——远程 Session 的 Token 生命周期与本地不同，之前这类失败几乎没有任何提示。

**How to apply（如何应用）**:
- 在 `~/.claude/settings.json` 中设置 `workflowMaxAgents` 限制单个 Workflow 的 Subagent 上限，建议从 20-50 开始，根据任务复杂度调整
- 使用 `/workflows` 面板的新遥测数据建立你的 Workflow 性能基线：哪类任务耗时最长、哪类 Subagent 失败率最高
- 在启动隔夜 Dynamic Workflow 前检查 Session Token 有效期，养成"任务前认证检查"习惯

---

## 4. claude-code-system-prompts v2.1.204：515 个系统提示词实时更新，Claude Code 内部机制完整透视

🔴 24h内 | 2026-07-08 更新至 v2.1.204

**Source**:
- [GitHub — Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts)

**Summary（做了什么）**:
`claude-code-system-prompts` 由 Piebald.ai 团队维护，**在每个 Claude Code 版本发布后数分钟内**更新，收录所有已知的 Claude Code 系统提示词。最新版 v2.1.204（7 月 8 日）覆盖 **515 个系统提示词**（6 月扩展后从 350 增至 515），包含：主系统提示各条件分支（不同环境/配置下加载的不同段落）、27 个内置工具的完整描述、Plan/Explore/Task 三类 Sub-Agent 的专属提示词、CLAUDE.md 处理逻辑、Compact 模式提示、WebFetch/Bash 命令提示、Security Review 提示、Agent 创建逻辑。同时维护 **230 个版本的完整 CHANGELOG**，逐版本追踪提示词变化。

**Key Insight（核心洞察）**:
**系统提示词的版本化 CHANGELOG，将 Claude Code 的"隐式行为变化"变为可追踪的显式记录。** 每次 Claude Code 更新，用户感受到的行为变化（Agent 突然更保守了/更激进了/多了某个检查步骤）背后往往是系统提示词的微调。515 个提示词中，有大量条件逻辑（根据环境、配置、任务类型加载不同段落）——这意味着"同一个 Claude Code，不同配置下实际运行的是不同的 Agent"。对于构建 Claude Code 插件、Skill 或自定义 Agent 的开发者，了解当前版本的提示词结构是避免冲突、优化指令的基础。

**Why it matters（为什么重要）**:
对于 Claude Code 插件/Skill 开发者：了解 Sub-Agent（Explore/Plan/Task）的专属提示词，可以为自己的 Skill 设计更契合 Sub-Agent 行为模式的指令格式，减少指令被"稀释"的可能。对于 UX/产品团队：理解 Claude Code 的安全审查提示词逻辑，有助于预设哪些设计决策会触发额外确认流程，提前在 CLAUDE.md 中声明相关权限。

**How to apply（如何应用）**:
- Star 该仓库以接收每次 Claude Code 版本的提示词变化通知（GitHub Release 提醒）
- 在 Claude Code 行为出现意外变化时，查阅对应版本的 CHANGELOG，定位是哪段提示词发生了改变
- 对照 Sub-Agent 的提示词结构（尤其 Task Agent 的工具访问限制和优先级声明），优化自定义 Skill 的触发条件描述
- 阅读条件加载逻辑，理解 `ultracode`、`remote session`、`enterprise` 等模式下实际激活的提示词差异

---

## 5. ECC v2.0.0：261 个 Skill 的 Agent Harness 操作系统，224K Stars 成社区事实标准

🟢 重大更新 | v2.0.0 发布于 2026-06-10，最近一次 commit 2026-07-01，社区持续增长

**Source**:
- [GitHub — affaan-m/ECC](https://github.com/affaan-m/ecc)
- [ECC Tools Official Site](https://ecc.tools/)

**Summary（做了什么）**:
ECC（Everything Claude Code）v2.0.0 将自身定位从"配置包"升级为 **Agent Harness Operating System**：261 个 Skill 覆盖全栈工程场景（Python/Django、Java Spring Boot、前端框架、DevOps、安全扫描等）；**Instinct System v2**（基于置信度评分的持续学习，自动从用户行为中学习偏好，支持 `/instinct-export` 跨机器迁移）；**Continuous Memory**（跨 Session 的记忆持久化，学习过的 Skill、Session 别名、性能指标统一存储于 `~/.claude`）；**NanoClaw v2**（模型路由 + Skill 热加载 + Session 分支/搜索/导出/压缩/指标）；**Orchestrator 家族**（`orch-*`，面向复杂多 Agent 任务的内置编排器）。支持 Claude Code、Cursor、Codex、OpenCode、Gemini 等主流 Agent Harness，260 名贡献者，14 次正式 Release。

**Key Insight（核心洞察）**:
**ECC 的 Instinct System 是目前社区中最成熟的"Agent 持续学习"实现。** 大多数 Claude Code 配置包是静态的——你配置完就不变了。ECC 的 Instinct System 在每次 Session 中观察你的行为（你接受了哪些建议、拒绝了哪些、修改了什么），形成有置信度评分的"本能"规则，随使用时间自动优化。更重要的是，Instinct 可以导出/导入——**团队中表现最好的开发者的工作模式，可以直接迁移给团队其他成员**，这是一个被严重低估的团队杠杆。

**Why it matters（为什么重要）**:
224K Stars + 260 贡献者证明 ECC 已是 Claude Code 生态的事实标准配置框架。对于正在评估如何系统化提升 Claude Code 使用效率的团队：ECC 的 261 个 Skill 是一个已经过大规模实战验证的起点，无需从零构建。特别值得关注的是 `orch-*` 编排器家族——面向复杂多 Agent 任务，与 Dynamic Workflows 的关系是互补而非替代（ECC orchestrator 可以作为 Dynamic Workflow 的 Skill 被调用）。

**How to apply（如何应用）**:
```bash
npm i -g ecc-universal  # 一键安装所有 Skill、Agent、Hook
```
推荐的高价值入口：
- `/instinct-status` — 查看已学习的本能规则和置信度，定期 `/instinct-export` 备份
- `/evolve` — 将相关本能规则聚合提升为可复用 Skill
- `/harness-audit` — 检查当前 Agent Harness 配置健康度
- `/model-route` — 按任务类型自动路由到最优模型（Opus for planning/review，Haiku for quick checks）

---

# Meta Summary

## 🧠 Emerging Patterns（趋势）

- **并行 Agent 工作流正在成为 IDE 原生范式**：VS Code 1.128 的 Multi-Chat Session 将"多 Agent 并行"从 Dynamic Workflows 脚本层面下沉到 IDE UI 层面。一个 Session 内 Fork + 并行执行多个 Chat，是把团队多人协作模式内化为个人 AI 工作流的设计哲学。这一趋势将推动更多开发者从"单线程问答"升级为"并行探索 + 收敛决策"的工作模式。

- **"可证明执行"正在成为多 Agent 系统的新需求层**：slang-workflows 提出的核心主张——将约束执行从 LLM 层移到确定性状态机层——代表了一类新需求：当 Agent 工作流进入合规敏感场景（安全审计、财务处理、医疗文档），"可证明性"和"可审计性"比"灵活性"更重要。这预示着未来 Agent 工作流工具链会出现"高自由度版本（Dynamic Workflows）"和"高合规版本（Provable Execution）"的分叉。

- **可观测性基础设施加速补齐**：Dynamic Workflow Size 限制、Workflow 遥测增强、登录过期预警、Subagent 只读视图——本周四个更新都在解决同一个问题：让用户看清楚 Agent 系统在做什么。随着 Dynamic Workflows 被越来越多地用于生产任务，"可观测性"正从锦上添花变为必需品。

- **持续学习 + 团队知识传播成为下一个竞争维度**：ECC 的 Instinct System 指向了一个新的能力层次：不只是配置 Agent 能做什么，而是让 Agent 学习你的工作偏好并持续优化，最终将个人最佳实践编码为可传播的 Instinct。这一模式如果被 Anthropic 官方采纳，将从根本上改变"个人开发者效率"与"团队协作效率"之间的差距。

## ⚡ New Mental Models（认知升级）

- **Multi-Chat Session = 个人工作流中的"并行思维轨道"**：不要把 Multi-Chat 理解为"多开几个对话窗口"——要理解为在同一上下文下同时运行多条思维路径。关键是"同一 Session 上下文"：共享的约束、共享的项目背景、共享的工具访问权限。Fork 机制让"探索替代方案"成为零成本的可逆操作，而非新开 Session 的高成本决策。

- **LLM 生成 + 状态机验证 = 可靠 Agent 系统的正确分层**：slang-workflows 给出了一个清晰的分层模型——创造性任务（生成内容、设计方案、写代码）属于 LLM 层，约束执行（格式校验、权限控制、流程强制、合规验证）属于确定性层。未来设计 Agent 系统时，应该有意识地区分哪些逻辑该由 LLM 处理，哪些应该由确定性代码处理。

## 🚀 Opportunities（机会点）

- **UX 团队的 Multi-Chat 并行设计工作流**：VS Code Multi-Chat 为 UX/产品团队提供了一个高价值使用模式：在同一 Session（同一设计上下文）内，并行生成多个设计方案的可点击原型，每个 Chat 独立运行，最终在同一 Session 内对比评审。这个工作流目前几乎无人系统化地在做，是 UX 团队利用 Claude Code 的差异化机会。

- **面向合规场景的 Provable Workflow 产品**：slang-workflows 的架构（类型化声明 + 确定性执行 + 审计日志）在法律科技、医疗 AI、金融合规等领域有明显的产品化价值。一个"合规就绪的 Agent Workflow 框架"——预置行业特定的合规约束模板、自动生成审计报告——是目前几乎空白的市场。

- **Instinct 共享市场**：ECC 的 `/instinct-export` 功能已经具备了构建"专家知识迁移市场"的基础技术。面向特定领域（React 性能优化专家的 Instinct、数据库架构师的 Instinct、UX 研究员的 Instinct）的策划和分发平台，是一个尚未有人做的社区机会。
