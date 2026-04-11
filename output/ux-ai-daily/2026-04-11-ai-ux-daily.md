# AI + UX Daily Digest — April 11, 2026

> 面向 UX / 产品设计师的 AI 行业每日精选。仅收录过去 24h–3 天内的高时效内容。

---

## 🧰 工具 Tools

### 1. Figma Make Kits & Attachments — 让 AI 生成真正符合设计系统的 UI
Figma 于 4 月 2 日发布 Make Kits 和 Make Attachments。Make Kits 允许设计系统作者将组件、样式与使用指南打包为可复用的 Kit，教会 Figma Make 如何正确使用你的设计系统。Make Attachments 允许将 PRD、品牌指南、代码文件、CSV、图片等直接附加到 prompt 中，使生成结果基于真实项目上下文而非通用占位符。

**为什么重要：** 这是 AI 辅助设计从「生成随机 UI」到「生成符合你设计系统的 UI」的关键转变。设计师终于可以让 AI 理解并遵循团队的设计规范。

🔗 [Figma Blog: Make Kits & Attachments](https://www.figma.com/blog/introducing-make-kits-and-make-attachments/) · [Figma Help: Get Started with Make Kits](https://help.figma.com/hc/en-us/articles/39241689698839-Get-started-with-Make-kits)
📅 2026-04-02（过去 9 天 / 本周仍在滚动推出中）

---

### 2. DESIGN.md 协议 — 纯文本设计系统成为 AI Agent 的通用语言
由 Google Stitch 引入的 DESIGN.md 格式正在迅速成为标准：一个放在项目根目录的 Markdown 文件，包含完整的设计规范（色彩、字体、组件样式、布局原则、设计哲学），任何 AI 编码 Agent 都能直接读取并生成一致的 UI。VoltAgent/awesome-design-md 仓库 3 月 31 日上线，3 天内达到 4,385 stars，截至 4 月 9 日已超 35,000 stars。

**为什么重要：** DESIGN.md 正在成为设计师与 AI Agent 之间的「通信协议」。预计 Figma、Framer 等工具将很快支持「导出为 DESIGN.md」。这从根本上改变了设计系统的交付方式。

🔗 [OSS Insight: DESIGN.md Protocol](https://ossinsight.io/blog/design-md-protocol-2026) · [awesome-design-md (GitHub)](https://github.com/VoltAgent/awesome-design-md)
📅 过去 1–2 周持续爆发

---

### 3. CopilotKit Generative UI — 三种 Agent 驱动的 UI 模式标准化
CopilotKit 联合 Google、Oracle 推动 Generative UI 标准化，定义了三种实用模式：**AG-UI**（高控制/受控生成）、**A2UI/Open-JSON-UI**（共享控制/声明式生成）、**MCP Apps**（高自由度/开放式生成）。Google 的 A2UI 规范允许 Agent 用结构化 JSONL 描述所需 UI，CopilotKit 自动渲染。

**为什么重要：** 这是 Agent UI 从实验走向工业标准的信号。UX 设计师需要理解这三种模式——它们定义了 AI Agent 如何生成和控制界面。

🔗 [CopilotKit: Developer's Guide to Generative UI](https://www.copilotkit.ai/blog/the-developer-s-guide-to-generative-ui-in-2026) · [AG-UI and A2UI Explained](https://www.copilotkit.ai/blog/ag-ui-and-a2ui-explained-how-the-emerging-agentic-stack-fits-together)
📅 过去 1–2 周 / Google Cloud Next 2026 期间重点推动

---

## 📰 新闻 News

### 4. Anthropic Claude Mythos Preview — 限制发布开创 AI 安全新模式
Anthropic 于 4 月 7 日宣布 Claude Mythos Preview 不会公开发布，而是通过 **Project Glasswing** 仅向 40+ 家科技和安全公司（AWS、Apple、Google、Microsoft、CrowdStrike 等）提供，用于防御性安全工作。该模型在测试中自主发现了数千个零日漏洞，包括一个存在 17 年的 FreeBSD 远程代码执行漏洞。

**为什么重要：** 这是 AI 行业首次因安全能力过强而选择限制发布的案例，开创了「能力越强、发布越谨慎」的先例。对产品设计师意味着：AI 安全设计和责任 AI 将成为产品必选项。

🔗 [Anthropic: Project Glasswing](https://www.anthropic.com/glasswing) · [TechCrunch Coverage](https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/) · [Simon Willison 分析](https://simonwillison.net/2026/Apr/7/project-glasswing/)
📅 2026-04-07（过去 4 天）

---

### 5. Meta Muse Spark — Meta 重返 AI 竞赛的多模态推理模型
Meta 于 4 月 8 日发布 Muse Spark，这是 Alexandr Wang 加入后的首个重大模型。原生多模态（语音、文本、图像输入），支持工具调用、视觉推理链和多 Agent 编排。Contemplating mode 通过多 Agent 并行推理对标 Gemini Deep Think 和 GPT Pro。Artificial Analysis 评分 52，仅次于 Gemini 3.1 Pro、GPT-5.4 和 Claude Opus 4.6。

**为什么重要：** 与之前的开源 Llama 不同，Muse Spark 是闭源的 Meta 专属模型，将驱动 WhatsApp、Instagram、Facebook 等 30 亿用户平台的 AI 体验。对 UX 影响巨大——这意味着更强的多模态交互即将进入社交产品。

🔗 [Meta AI Blog](https://ai.meta.com/blog/introducing-muse-spark-msl/) · [TechCrunch](https://techcrunch.com/2026/04/08/meta-debuts-the-muse-spark-model-in-a-ground-up-overhaul-of-its-ai/) · [Simon Willison](https://simonwillison.net/2026/Apr/8/muse-spark/)
📅 2026-04-08（过去 3 天）

---

### 6. OpenAI 推出 $100/月 Pro 计划 + GPT-5.3 Instant Mini 更新
OpenAI 4 月更新：推出新的 $100/月 Pro 计划，面向高强度 Codex 编程场景，包含无限 GPT-5.4 访问和最高 10x Codex 用量。同时 GPT-5.3 Instant Mini 替代 GPT-5 Instant Mini 成为新的 fallback 模型，对话更自然、写作和上下文感知更强。

**为什么重要：** Pro 计划信号明确——AI 编码 Agent 正在成为付费工具链的核心。设计师也将越来越多地使用 AI Agent 完成从设计到代码的全流程。

🔗 [OpenAI: GPT-5.3 Instant](https://openai.com/index/gpt-5-3-instant/) · [OpenAI Release Notes](https://releasebot.io/updates/openai)
📅 2026 年 4 月（过去 1–2 周）

---

## 💻 GitHub

### 7. VoltAgent/awesome-design-md — AI Agent 的设计系统集合
收录流行品牌网站的 DESIGN.md 文件，直接放入项目即可让 AI Agent 生成匹配的 UI。3 月 31 日发布，截至 4 月 9 日已达 **35,000+ stars / 4,400 forks**，是 GitHub 增长最快的仓库之一。

**为什么重要：** 对 UX 设计师来说，这是一个即用型资源库。可以参考现有 DESIGN.md 为自己的项目创建设计规范文件，让 AI 编码工具直接理解设计意图。

🔗 [GitHub: awesome-design-md](https://github.com/VoltAgent/awesome-design-md)
📅 过去 1–2 周持续爆发 | ⭐ 35k+

---

### 8. VoltAgent/awesome-agent-skills — 1000+ Agent Skills 集合
手工精选的 1000+ Agent Skills，来自 Anthropic、Google Labs、Vercel、Stripe、Cloudflare、Figma 等官方团队及社区。兼容 Claude Code、Codex、Gemini CLI、Cursor、GitHub Copilot 等主流 AI 编码工具。

**为什么重要：** Agent Skills 生态正在爆发。设计师和产品经理可以在此发现能力边界——了解 AI Agent 当前能做什么，才能设计出合理的 Agent 交互体验。

🔗 [GitHub: awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)
📅 持续活跃更新

---

### 9. Google LiteRT-LM — 跨平台边缘 LLM 推理引擎开源
Google AI Edge 本周开源 LiteRT-LM，支持 Android、iOS、Web、桌面、Raspberry Pi 等平台的高性能本地 LLM 推理。

**为什么重要：** 边缘推理意味着 AI 功能可以在设备端运行，无需联网。对产品设计师意味着：可以设计离线可用的 AI 功能，降低延迟，保护隐私。

🔗 [GitHub Trending Weekly 2026-04-08](https://www.shareuhack.com/en/posts/github-trending-weekly-2026-04-08)
📅 本周开源

---

## 💡 洞察 Insights

### 10. Agent UI 三大设计范式正在成形
从本周的行业动态可以看到，Agent 驱动的 UI 设计正在沿三条路径标准化：

- **受控生成（Controlled）**：Agent 在预定义组件库内生成 UI（如 Figma Make Kits + AG-UI），设计师保留最大控制权
- **声明式生成（Declarative）**：Agent 用结构化规范描述 UI 需求，框架自动渲染（如 Google A2UI），设计师定义规则而非像素
- **开放式生成（Open-ended）**：Agent 自由生成 UI（如 MCP Apps），适合探索阶段和原型设计

**为什么重要：** 理解这三种模式是 2026 年 UX 设计师的必修课。不同产品阶段和场景适合不同模式，选择错误会导致「AI 生成的 UI 不可控」或「限制过多无法发挥 AI 优势」。

🔗 [CopilotKit: State of Agentic UI](https://www.copilotkit.ai/blog/the-state-of-agentic-ui-comparing-ag-ui-mcp-ui-and-a2ui-protocols) · [Fifty Five and Five: DESIGN.md Patterns](https://fiftyfiveandfive.com/resources/design-md-files-and-the-foundational-patterns-of-ai-assisted-design/)

---

*Curated for UX designers and product builders. Quality over quantity.*
*Report generated: 2026-04-11*
