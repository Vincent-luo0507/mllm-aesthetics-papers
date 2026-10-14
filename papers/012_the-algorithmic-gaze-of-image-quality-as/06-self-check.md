# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 227（文本 100 / 原子 127）|
| 已译文本块 | 100 / 100 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 19 · 已还原 19 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 53 |
| `<img>` 元素 | 11 |
| `<table>` 元素 | 4 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| aesthetic quality assessment (AQA) | 美学质量评估（AQA） | 任务名，全文统一 |
| LAION-Aesthetics Predictor (LAP) | LAION-Aesthetics Predictor（LAP） | 模型名保留英文与缩写 |
| LAION-Aesthetics Dataset (LAD) | LAION-Aesthetics 数据集（LAD） | 数据集名，后文可用 LAD |
| Aesthetic Visual Analysis (AVA) | Aesthetic Visual Analysis（AVA） | 训练数据集名，保留 |
| Simulacra Aesthetic Captions (SAC) | Simulacra Aesthetic Captions（SAC） | 训练数据集名，保留 |
| LAION-Logos | LAION-Logos | 数据集名不译 |
| algorithmic gaze | 算法凝视 | 标题核心概念，全文统一 |
| male gaze | 男性凝视 | 艺术史既有译法 |
| imperial gaze | 帝国凝视 | 同上 |
| realist gaze | 现实主义凝视 | 与写实主义偏见呼应 |
| trace ethnography | 痕迹民族志 | Geiger & Ribes 提出的方法 |
| audit | 审计 | 算法审计语境统一用“审计” |
| representational harm | 表征性伤害 | 公平性研究术语 |
| text-to-image (T2I) | 文本到图像（T2I） | 首次出现附缩写 |
| photorealism | 照片级真实感 | 与 realism（写实性）区分 |
| pointwise mutual information (PMI) | 点互信息（PMI） | 首次出现附英文全称 |
| Majority World | 多数世界（Majority World） | 首次出现附英文原词 |
| CLIP embedding | CLIP 嵌入 | 不译模型名 |
| multi-layer perceptron | 多层感知机 | 通用术语 |
| CSAM (child sexual abuse material) | 儿童性虐待材料（CSAM） | 首次出现附英文全称 |
| NCII | NCII | 非自愿亲密影像，缩写保留 |
| WEIRD | WEIRD | Western, Educated, Industrialized, Rich, Democratic 缩写保留 |
| FAccT | FAccT | 会议名不译 |
| dpchallenge.com | dpchallenge.com | 网站名不译 |
| ukiyo-e | 浮世绘 | 日本木版画流派 |
| non-consensual inclusion | 非自愿的纳入 | 与数据排除相对 |
| universalism / pluralistic | 普世主义 / 多元主义 | 全文成对出现，译法固定 |
| prescriptive vs. descriptive measurement | 规定性度量 vs. 描述性度量 | 关键对立，全文统一 |

### 交叉验证记录

| 块 id | 原文要点 | 译文要点 | 一致性 |
|---|---|---|---|
| b0012 | LAP 对 LAION-Aesthetics（⟦SLOT_0⟧1.2B 张）过滤的女性/男性/LGBTQ+ 差异；为 ⟦SLOT_1⟧330k 张艺术图像打分；两个研究问题 RQ1/RQ2 | 数字 1.2B、330k 原样保留；占位符 0、1 原样；RQ1/RQ2 保留 | 一致，无漏译 |
| b0040 | ‘whites?’ 与 ‘latin[oaxe]s?’ PMI 均为 -0.95，对应 9,617 与 26 张；‘wom[ae]n’ 15,706；LGBTQ+ 正则式 102/20/9/2/0 | 全部正则式与计数原样保留，含单引号内的正则式文本 | 一致，正则式未做任何改写 |
| b0048 | 249,351 张图像、37,878 种媒材、14,946 位艺术家、177 张 ≥6.5、5 种媒材（72/60/26/15/2/1/1）、14 位艺术家占 88 张（50%） | 数字逐一对应，6 个 ⟦SLOT⟧ 全部保留 | 一致 |
| b0079 | 428,632 张训练图像中 AVA 255,530（⟦SLOT_16⟧60%）、SAC 146,372（⟦SLOT_17⟧34%）、LAION-Logos 26,730（⟦SLOT_18⟧6%）；TOP50 志愿者占 87.4%；18 位 LAION 志愿者 | 全部数字与三个占位符原样保留 | 一致，百分比未换算 |
| b0106 | Seaver 论述：审计识别偏见、民族志解释来源；“scavenging”；未列入索引视频的伦理问题 | 引用与论点完整译出，未添补评论 | 一致 |

### 一致性与数字核查

- 术语统一：用 Grep 在 `zh.json` 中检索“算法凝视”“男性凝视”“帝国凝视”“现实主义凝视”“美学质量评估”“痕迹民族志”“表征性伤害”“照片级真实感”“点互信息”“文本到图像”等核心术语，全文译法唯一；缩写 LAP / LAD / AVA / SAC / T2I / FAccT / PMI / CSAM / NCII / WEIRD 均原样保留。
- 数字核查：阈值 4.5 / 6.5 / 6+、规模 1.2B / 625k / 330k / 249,351 / 81,444 / 249,351 / 428,632、百分比 36% / 52% / 97% / 60% / 34% / 6% / 87.4% / 33%、计数 177 / 88 / 9,617 / 26 / 15,706 / 102 / 20 / 9 / 2 / 0 与分数区间比例 11/27、9/27、7/27、20/30、5/30、20/40、10/40、7/40 均未改动。
- 占位符完整性：脚本统计内联槽位 19、已还原 19；另用脚本逐块比对 100 个文本块的 `⟦SLOT_n⟧` 集合，全部一致。
- 编码检查：`zh.json` 与 `index.html` 中 U+FFFD 计数均为 0，编码 UTF-8。
- 不变量：表格、公式、图片、参考文献块一律未翻译；未删减、合并或拆分段落。

### 遗留问题

- 无。图片引用缺失 0，公式元素 53 个均正常还原，未发现原文乱码或不可解析的块。

## 复核记录（第二轮交叉验证）

- 抽查块（9 块，随机种子 7 与 42）：b0045、b0036、b0098、b0092、b0030、b0107、b0055、b0053、b0105
- 全篇自动化校验：逐块比对 EN/ZH 的 `⟦SLOT_n⟧` 占位符编号与顺序、数字/量级一致性，未发现丢失、错位或篡改。
- 发现并修正的问题：
  - **b0098**（准确性（增译原文没有的概念））：「这类暴力因商业化的人工智能**换脸脱衣**应用的兴起而加剧」 → 「这类暴力因商业化的人工智能**裸体化**应用的兴起而加剧」（EN 为 AI-based nudification apps，原文不含 face-swap/换脸 语义）
- 重跑 `build_index.py` 后四项校验：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
