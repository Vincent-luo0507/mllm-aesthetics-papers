# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 184（文本 123 / 原子 61）|
| 已译文本块 | 123 / 123 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 18 · 已还原 18 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 47 |
| `<img>` 元素 | 6 |
| `<table>` 元素 | 1 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| AI text-to-app tool | AI 文本到应用工具 | 首次括注 text-to-app，后文统一简称 |
| low-code / no-code platform | 低代码 / 无代码平台 | 统一 |
| visual design quality | 视觉设计质量 | 与 visual excellence「视觉水准」按语境分工，前者指被度量属性，后者指结果描述 |
| visual excellence | 视觉水准 | 统一 |
| pairwise comparison / judgement | 成对比较 / 成对判断 | 全文统一，不混用「两两比较」 |
| blinded / blinding | 盲态 | 统一，不用「双盲」以免与医学含义混淆 |
| expert designer / expert panel | 专家设计师 / 专家评审组 | 统一 |
| primary endpoint | 主要终点 | 沿用原文的实验设计用语 |
| TrueSkill | TrueSkill | 系统名保留 |
| Bradley–Terry model (BT) | Bradley–Terry 模型（BT） | 保留人名与缩写 |
| comparative judgement | 比较判断 | Thurstone 术语，统一 |
| credible interval | 可信区间 | 贝叶斯语境统一用「可信区间」；原文 contributions 处 95% confidence intervals 按原文译为「置信区间」 |
| posterior mean / posterior uncertainty | 后验均值 / 后验不确定性 | 统一 |
| leaderboard | 排行榜 | 统一 |
| prompt | 提示词 | 统一 |
| webapp | Web 应用 | 与「网站」区分，统一 |
| call to action (CTA) | 行动号召（CTA） | 首次括注 |
| full-view requirement | 完整浏览要求 | 协议要素，统一 |
| split voting sessions | 拆分投票场次 | 统一 |
| exposure balance | 曝光均衡 | 配对采样准则，统一 |
| opponent novelty | 对手新颖性 | 统一 |
| match quality | 匹配质量 | TrueSkill 术语，统一 |
| cool-down / repeat-cap | 冷却期 / 重复上限 | 统一 |
| win rate | 胜率 | 统一 |
| quality-gap analysis | 质量差距分析 | 统一 |
| failure mode | 失效模式 | 统一 |
| typography | 字体排印 | 统一 |
| hierarchy | 层级 | 统一 |
| responsiveness | 响应式 | 统一 |
| agent orchestration | 智能体编排 | 统一 |
| codebook | 编码手册 | 失效模式标注用，统一 |
| gold label | 金标 | 统一 |
| ground truth benchmark | 真值基准 | 与偏好基准相对，统一 |
| LLM-judge | 大模型裁判 | 统一 |

### 交叉验证记录

| 块 id | 原文要点 | 译文 | 一致性 |
|---|---|---|---|
| b0007 | 46% 用户评价提及外观与观感；视觉过载与内容体量损害参与度 | 用户在判断网站可信度时有 46% 的评价提及网站的外观与观感……视觉过载会在转化率上升之前就引发强烈的负面反应 | 数字 46% 与因果顺序一致，未添加评论 |
| b0020 | 综述多个基准；WebCode2M 2.56M 对；FrontendBench 90.45% 一致性；Design2Code 484 网页 | ……WebCode2M 提供 256 万条真实设计—代码对……FrontendBench 自动化沙箱测试，报告在特定 UI 行为上与专家达到 90.45% 的一致性……它精选 484 个网页 | 数值与系统名一一对应，三个 SLOT 原样保留 |
| b0044 | 竞技场两阶段采样、配对打分的四项加权因素、惩罚项与打破平局规则 | ……按曝光均衡、对手新颖性、不确定性 ⟦SLOT_5⟧ 与 TrueSkill 匹配质量的加权组合……再对专家已见过、处于近期冷却期、超出重复上限以及热门工具过度曝光的配对施加惩罚 | 语义一致，枚举项无遗漏，SLOT_5/SLOT_6 保留 |
| b0089 | Orchids 30.12 / 67.5%，Figma Make 27.46 / 57.1%，Lovable 27.14 / 54.8%，下游低于 24 | Orchids 以 30.12 的平均评分与 67.5% 的胜率居首……（Figma Make，⟦SLOT_15⟧=27.46，57.1%）……排名靠后的系统……评分低于 24 | 四组数值未改动，SLOT_15–SLOT_17 原样保留 |
| b0102 | Figma Make 的 500 字符上限，用 ChatGPT 压缩提示词 | Figma 的工具有 500 字符的输入上限，而我们的提示词一般超过 150 词。我们通过 ChatGPT 把所有提示词压缩…… | 限制条件与处理方式完整，数字一致 |

### 一致性与数字核查

- **术语统一**：核心术语「成对比较 / 盲态 / TrueSkill / 排版（字体排印）/ 提示词 / 排行榜 / 后验均值」在 `zh.json` 中逐条检索，全文译法唯一；「视觉设计质量」与「视觉水准」按原文用词分别对应，未交叉混用。
- **数字核查**：核对了 46%、25%、30 个提示词 / 五类 / 每类 6 个、150–180 词、500 字符、60 分钟、N=194 及各角色占比（65.5%/127、57.2%/111、60.3%/117、7.2%/14、10.8%/21、89.2%/173）、60 票 / 两场 / 90 票上限、30.12、67.5%、27.46、57.1%、27.14、54.8%、24、2.56M、90.45%、484、4,000+ 等全部数值，未作改动；工具名（v0 by Vercel、Bolt、Orchids、Lovable、Replit、Figma Make、Base44 by Wix、Magic Patterns、Same.new、Create Anything）与指标名（FID、CLIP、IS、BT、RLHF）均原样保留。
- **占位符完整性**：123 个文本块逐块比对 `⟦SLOT_n⟧` 集合，源文与译文完全一致（差异 0）。
- **编码检查**：`zh.json` 与 `index.html` 中 U+FFFD 计数为 0。
- **不变量**：表格、公式、图片与参考文献块按 `t:"keep"` 跳过；段落一一对应，未删减或合并。

### 遗留问题

- 原文小节标题 b0004 为 "Rapid Emergence of of AI App and Website Tools"，存在重复的 "of"，疑为原文笔误，译文按「AI 应用与网站工具的快速涌现」处理。
- 原文 b0096 句首 "We make no claims on AI failure modes related to losses clustering around:" 语法不完整，译文按字面忠实处理为「我们不对 AI 失效模式作出断言；相关的落败集中在以下方面」。
- `missing_img` 为 0，无需补图。

## 复核记录（第二轮交叉验证）

- 复核人：独立复核 Agent 08 号
- 抽查方式：`sample_blocks.py` 两轮随机抽样（种子 8 与 2024）+ 全量脚本化交叉校验（数字/公式占位符/未译块/长度比）
- 抽查块（共 12 块次）：b0049, b0081, b0070, b0079, b0068, b0089 / b0037, b0076, b0022, b0038, b0077, b0059
- 结论：共记录 1 条核验事项，逐条判定如下。

| 块 ID | 问题类型 | 复核发现 | 判定与处理 |
|---|---|---|---|
| b0020, b0029 | 数字一致性复核 | EN「2.56M」「240k+」在 ZH 中无逐字对应 | ZH 分别译为「256 万条」「24 万次以上」，数值等价，未修改。 |

- 其中标注「未修改」者为经核对后确认**非错误**（中文语序换位、等值数字改写、规范要求的英文专名保留），按规格书 §2「避免过度修改」不予改动。
- 重跑 `build_index.py`：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
