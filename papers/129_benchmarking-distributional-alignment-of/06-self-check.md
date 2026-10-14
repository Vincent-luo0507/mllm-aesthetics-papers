# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 270（文本 151 / 原子 119）|
| 已译文本块 | 151 / 151 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 58 · 已还原 58 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 326 |
| `<img>` 元素 | 6 |
| `<table>` 元素 | 17 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| distributional alignment | 分布对齐 | 核心概念，全文统一 |
| demographic group | 人口群体 | 统一 |
| steering (method) | 引导（方法） | 统一；不用「操控」 |
| steerability | 可引导性 | 统一 |
| persona steering | 人设引导 | 首次括注 persona steering，后文统一 |
| few-shot steering | 少样本引导 | 统一 |
| no steering | 无引导 | 统一 |
| distribution expression method | 分布表达方法 | 与 estimation 区分，统一 |
| distribution estimation method | 分布估计方法 | §3.1 标题用词，统一 |
| model log-probabilities | 模型对数概率 | 统一 |
| sequence of tokens | token 序列 | 统一 |
| verbalize distributional knowledge | 言语化分布知识 | 统一 |
| total variation (distance) | 全变差（距离） | 统一 |
| knowledge-to-simulation gap | 知识—模拟鸿沟 | 核心概念，首次括注英文，连字符用一字线 |
| mis-calibrated / calibration | 校准不良 / 校准 | 统一 |
| temperature scaling (TS) | 温度缩放（TS） | 统一 |
| Expected Calibration Error (ECE) | 期望校准误差（ECE） | 统一 |
| discretization error | 离散化误差 | 统一 |
| biased coin flip | 偏置硬币翻转 | 统一 |
| OpinionQA / GlobalOpinionQA / NYT Book Opinions | OpinionQA / GlobalOpinionQA / NYT Book Opinions | 数据集名保留 |
| Likert rating | 李克特评分 | 统一 |
| Cohen’s kappa | Cohen kappa | 保留专名 |
| bootstrapping | 自助法 | 统一 |
| confidence interval | 置信区间 | 统一 |
| KL divergence | KL 散度 | 统一 |
| in-group / out-group | 内群体 / 外群体 | 统一 |
| Perception Gap | 感知鸿沟 | 统一 |
| echo chamber | 回音室 | 统一 |
| polarization | 极化 | 统一 |
| distributionally pluralistic alignment | 分布多元对齐 | 统一 |
| prompt brittleness | 提示脆弱性 | 统一 |
| social desirability bias | 社会赞许性偏差 | 统一 |
| construct validity | 构念效度 | 统一 |
| ecological validity | 生态效度 | 统一 |
| RLHF | RLHF | 保留缩写 |

### 交叉验证记录

| 块 id | 原文要点 | 译文 | 一致性 |
|---|---|---|---|
| b0017 | 分布对齐形式化，含 SLOT_0–SLOT_6 | 令 ⟦SLOT_0⟧ 为一道调查问题，来自群体 ⟦SLOT_1⟧ 的回答者对它在多个选项 ⟦SLOT_2⟧ 上存在一个观点分布……模型将用分布表达方法 ⟦SLOT_6⟧ 来表达一个分布 ⟦SLOT_5⟧ | 7 个占位符逐一对应，定义要素无遗漏 |
| b0030 | 偏置硬币实验：H/T 概率的四个槽位，模型对数概率校准差 | 一个 LLM 被指示模拟一枚偏置硬币的翻转，其 ⟦SLOT_20⟧ 与 ⟦SLOT_21⟧……token「H」的模型对数概率为 ⟦SLOT_22⟧，「T」为 ⟦SLOT_23⟧ | 槽位与实验设定完整，结论方向未颠倒 |
| b0059 | 排行榜数值：0.363（均匀基线）、0.707（多数投票基线） | 这些数值可以直接与均匀基线（每个选项在序列中等可能出现，0.363）以及多数投票基线……（0.707）相对照 | 两个数值与各自基线定义正确匹配 |
| b0070 | 13% vs 33%、25% vs 12% 的刻板印象对比 | 被模拟的人类有 13% 的概率回答「极不可能读」，而我们的标注者该概率为 33%……有 25% 的概率回答「极可能读」，而我们的标注者该概率为 12% | 四个数值与模型/人类归属一一对应，未错位 |
| b0212 | 131/206/165/172 位标注者，每本书每群体 18 条标注 | 我们调查了 131 位男性、206 位女性、165 位民主党人与 172 位共和党人标注者，使每本书、每个人口群体获得 18 条标注 | 四组人数与性别/党派对应无误 |

### 一致性与数字核查

- **术语统一**：已检索 `zh.json`，「分布对齐 / 引导 / 人设引导 / 少样本引导 / 分布表达方法 / 模型对数概率 / 言语化分布知识 / 全变差 / 知识—模拟鸿沟 / 人口群体」等核心术语译法唯一；原文混用的 expression 与 estimation 分别译为「表达」与「估计」，未强行统一。
- **数字核查**：核对了 500 / 100 道题、六个人口群体、138→19 个国家、600 条回答、30 个 token、235 本书、346 位标注者、26 本/人、131/206/165/172、18 条/本/群体、0.363、0.707、13%、33%、25%、12%、54.8%、45.2%、246/374 位标注者、93%、$12/小时、$7.25、1000 个自助样本、gpt-4-0613、GPT-3.5-Turbo-0125、CC-BY 4.0 等全部数值，未作改动；模型名（GPT-4、GPT-3.5、Anthropic Haiku、Anthropic Opus、Llama-3-70B-Instruct）与数据集/平台名（OpinionQA、GlobalOpinionQA、NYT Book Opinions、Prolific、Huggingface）均原样保留。
- **占位符完整性**：151 个文本块逐块比对 `⟦SLOT_n⟧` 集合，源文与译文完全一致（差异 0）。
- **编码检查**：`zh.json` 与 `index.html` 中 U+FFFD 计数为 0。
- **不变量**：表格、公式、图片与参考文献块按 `t:"keep"` 跳过；段落一一对应，未删减或合并。

### 遗留问题

- 原文 b0018 中脚注 11 的内容被嵌在句子中间（"we construct a set11 ... ⟦SLOT_12⟧ of ground truth..."），属原文排版，译文以破折号保留其插入位置。
- 原文 b0026、b0028、b0029、b0030、b0052 中的脚注编号（22、33、44、55、77）按其出现位置原样保留。
- 原文 b0268 中 "(TS-Logp)" 与表 8 的 "(TS-Log-p)" 写法不一致，译文按各自原文分别保留。
- `missing_img` 为 0，无需补图。

## 复核记录（第二轮交叉验证）

- 复核 Agent：06 号（独立交叉验证）
- 结构核验：MathJax（`tex-mml-chtml.js`）已加载；图片 `src` 全部为 `figures/...` 本地相对路径、无 http 外链；全文无 U+FFFD 乱码；顶部有中文标题与中文摘要，底部有「返回总目录」链接 —— 全部通过。
- 抽查块（9 块）：b0085、b0262、b0218、b0088、b0037、b0188、b0026、b0044、b0083
- 逐块比对 EN/ZH 的六项判读：完整性（无漏译整句/跳句）、准确性（无错译、无因果或否定反转）、数字与符号（数字、百分比、模型名、数据集名、指标名与原样一致）、公式占位符（`⟦SLOT_n⟧` 编号与顺序完全一致）、术语一致性（同篇内译法统一）、中文质量（通顺、无生造词、无 AI 腔堆砌）—— **未发现实质错误**。
- 附加机器校验：全篇文本块无缺失译文；每块占位符数量与顺序逐一比对一致；数字差分扫描命中的差异经人工核对均为中英数量表达差异（如 `4.8 million` → 「480 万」、`7.6B` → 「76 亿」、`10,073` → 「10,073」），非错译。
另注：正文中脚注编号（22/33/44/55/66）均保留，个别脚注正文（多为仓库链接与文献出处）未逐条译出；属参考文献性质内容，按规范不改。
- 已修正：无（未改动 `zh.json`）。
- 重跑 `build_index.py` 四项校验：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
