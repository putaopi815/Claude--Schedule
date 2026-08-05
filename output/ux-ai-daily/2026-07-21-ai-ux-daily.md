# AI × UX 每日速报 · 2026-07-21

> **Date**: 2026-07-21
> **Time Window**: 过去 24h（优先）/ 3 天内（补充）
> **Sources Checked**: EINPresswire / UX Planet / DONGA / GlobalNewsWire / UserTesting Release Notes / Varikons
> **Dedup Check**: ✅ 已对比 2026-07-14 报告，无重复项

---

## 🧰 工具 Tools

### 1. ProtoPie 正式推出原生 MCP 支持：Studio MCP + Code MCP 双轨制工作流
🔴 **24h内** | 发布时间：2026-07-20

**核心内容：** ProtoPie 推出双支柱 MCP 架构——**Studio MCP**（支持 BYOM，将 Claude Code、Cursor 等 AI 助手直接接入 ProtoPie 画布，用自然语言生成高保真交互结构）和 **Code MCP**（将交互式原型转化为结构化机器可读"真实来源"，供 AI 编码 Agent 直接翻译为生产代码）。核心卖点：用 AI 生成初始结构后，设计师在原型画布上无限精调——无需继续消耗 AI Token。

**为什么重要（UX/产品视角）：** 这是"vibe coding 隐性税"的首个系统性解法：ProtoPie MCP 把 AI 速度（快速搭建交互骨架）与设计师精度（精调手势、时序、条件逻辑）显式拆分为两个阶段，让 Token 只花在值得的地方。Code MCP 的"Agent-Ready 设计数据"标准也是 design-to-code 链路工程化的重要一步，值得设计+开发团队重点关注。

**原始链接：** [EINPresswire 发布公告](https://www.einnews.com/pr_news/927085421/protopie-launches-native-mcp-support-connecting-human-precision-to-the-era-of-ai-vibe-coding)

---

### 2. Google Stitch 重大更新：Missing States / 可访问性审计 / App Store 素材 / 原型互联
🟡 **3天内** | 发布时间：2026-07-17

**核心内容：** Google Stitch 新增五项核心功能：① **Missing States 生成**（自动推断错误态、空态等缺失页面）；② **Animate 动效生成**（为单屏添加动画）；③ **Accessibility Audit**（自动生成可访问性报告）；④ **App Store Assets + Marketing Kit**（生成应用商店图标、截图及营销物料）；⑤ **Interactive Prototype**（将静态页面转为可点击原型，支持在原型中直接增删页面并自动建立跳转连接）。底层模型已支持 Gemini 3.1 Pro 和 Gemini 3 Flash 可选。

**为什么重要（UX/产品视角）：** Missing States 生成是 Stitch 最实用的新功能——AI 自动补全设计师往往遗漏的错误态和空态，有效堵住原型评审中的常见漏洞。Accessibility Audit 内嵌于设计工具中，标志着 a11y 合规从"事后检查"走向"生成即审查"的流程变革。整体上 Stitch 已从"早期概念探索工具"升级为覆盖原型到发布全链路的 AI 设计套件。

**原始链接：** [UX Planet 评测文章](https://uxplanet.org/google-stitch-just-got-a-major-update-1dae251f54e7)

---

### 3. UserTesting 推出 MCP 服务器：将用户研究直接嵌入 Claude / Figma Make / ChatGPT
🟡 **3天内** | 发布时间：2026年7月季度发布

**核心内容：** UserTesting 发布 July 2026 季度更新，核心亮点是推出 **UserTesting MCP Server**，将参与者招募、测试创建和研究结果直接接入 Claude、ChatGPT、Figma Make 等 AI 客户端。同时 Figma 插件升级支持多任务/多原型的单次研究（复杂多步骤流程不再需要导出文件或切换工具），并开放了 7.6M 参与者网络（含 140 个行业的 3.2M 认证专业人士）的精准定向招募。

**为什么重要（UX/产品视角）：** "在 Figma 里直接发起用研" 是设计师期待已久的工作流融合。UserTesting MCP 的推出意味着用户洞察可以在 AI 辅助设计流程的最早期就介入——在 AI 生成界面草稿后，设计师直接在同一环境下招募真实用户进行验证，打通了"AI 生成 → 人工验证"的完整闭环。这是研究工作流 AI 原生化的重要里程碑。

**原始链接：** [UserTesting July 2026 Release](https://www.usertesting.com/resources/product-releases/july-2026)

---

## 📰 新闻 News

### 4. WEVEN Zaemit.ai 面向专业市场正式发布：Apollon 设计模型 + 全生命周期多 Agent 网页生产
🔴 **24h内** | 发布时间：2026-07-20

**核心内容：** 韩国初创 WEVEN 正式推出面向代理商/设计师/开发者的专业版 **Zaemit.ai**，核心是自研设计模型 **Apollon**——基于行业分类和最优布局体系训练，可跨全站保持字体、间距、颜色、组件一致性，同时大幅降低 Token 消耗。新增功能包括：Workspace 项目管理系统、Block 组件管理（复用 HTML/CSS 模块）、以及基于对话的后端开发 Agent（用自然语言实现数据库、预约系统等复杂功能，无需编码知识）。通过 MCP 集成支持在 Claude/ChatGPT 中直接调用 Zaemit 服务。

**为什么重要（UX/产品视角）：** Zaemit 的差异化在于 Apollon 模型的"设计系统感知"——不同于通用 LLM 每次都从零生成，Apollon 将品牌规范内化为模型先验，实现跨页面视觉一致性。对于规模化 Web 交付（代理商、多客户管理），这是 AI 辅助网页设计中最接近"品牌一致性 + 批量交付"双目标的解法之一。

**原始链接：** [DONGA Tech 报道](https://www.donga.com/en/article/all/20260720/6313654/1)

---

### 5. Squirro Agent Catalog 正式上线：企业 AI Agent 一次部署，基础层复用提速
🔴 **24h内** | 发布时间：2026-07-20

**核心内容：** Squirro（客户包括德意志联邦银行、汉高）发布 **Agent Catalog**，涵盖财务、HR、法务、销售、运营、IT 共 13 个预构建 Agent。核心设计理念：第一个 Agent 部署时建立企业数据连接、安全合规审批和知识层的可复用基础，后续每个 Agent 直接继承这一基础——无需从零开始。合规审批只做一次，后续 Agent 共享，在金融/医疗等受监管行业意义尤为突出。

**为什么重要（UX/产品视角）：** "Agent Catalog + 可复用基础层"是企业 Agent 工具走向规模化的关键 UX 模式：从"每次定制开发"转向"选购+继承"，极大降低了部署门槛。对产品设计师而言，这提供了企业级 Agent 产品如何设计 onboarding 流程（一次性建立基础层信任）的重要参考案例。

**原始链接：** [PR Newswire 公告](https://www.prnewswire.co.uk/news-releases/squirro-launches-ai-agent-catalog-to-end-the-start-from-zero-problem-stalling-enterprise-ai-302829146.html)

---

## 💡 洞察 Insights

### 6. MCP 正在成为设计工具的标准接口：2026年7月出现集中落地潮
🟡 **持续趋势** | 近期集中观察（7月第3周）

**核心内容：** 过去一周，ProtoPie（Studio MCP + Code MCP）、Google Stitch（MCP Server）、UserTesting（MCP Server）、Relume（Library MCP with 1000+ components）相继宣布 MCP 支持。共同信号：**设计工具正将 MCP 作为连接 AI 助手的标准接口**，而非构建专属 AI 功能。每家工具都选择"让现有 AI（Claude、Cursor、Figma Make）直接调用自身能力"，而非打造独立 AI 生态。

**为什么重要（UX/产品视角）：** 这一模式预示着 AI 设计工具链的形态正在定型：**专业工具做深核心能力 + MCP 暴露为 Agent 可调用接口**，而非每家工具都塞入自己的 LLM。对 UX 设计师而言，这意味着未来设计工作流将越来越由"我在 Claude/Cursor 里描述需求，各专业工具作为 MCP 服务器响应"来驱动——工具选择的关键将从"哪个 AI 最强"转向"哪个 MCP 工具最精准"。

---

*报告生成时间：2026-07-21 | 内容时效：过去 24h（🔴 3项）/ 3天内（🟡 2项）/ 持续趋势（💡 1项）*
