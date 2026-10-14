# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 297（文本 176 / 原子 121）|
| 已译文本块 | 176 / 176 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 23 · 已还原 23 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 75 |
| `<img>` 元素 | 34 |
| `<table>` 元素 | 23 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| image aesthetics assessment (IAA) | 图像美学评估 | 全文统一，与 IQA 区分 |
| image quality assessment (IQA) | 图像质量评价 | |
| multimodal large language model (MLLM) | 多模态大语言模型 | 首次出现附 MLLM |
| AI-generated content (AIGC) | 人工智能生成内容 | 首次出现附 AIGC |
| fine-grained aesthetic attribute | 细粒度美学属性 | |
| structural aesthetic analysis | 结构化美学分析 | |
| expert-level understanding | 专家级理解 | |
| holistic / overall aesthetics score | 整体美学分数 | |
| Token As Score | Token As Score | 方法名保留原文 |
| Text As Score | Text As Score | 对比方法名保留原文 |
| Level As Score | Level As Score | 对比方法名保留原文 |
| token | 词元 | 全文统一，不用「标记」 |
| tokenizer | 分词器 | |
| vocabulary | 词表 | |
| logits | logits | 保留原文 |
| expectation | 期望 | |
| cross-entropy loss | 交叉熵损失 | |
| LoRA | LoRA | 保留原文 |
| text pretrain | 文本预训练 | |
| score finetune | 分数微调 | |
| full fine-tuning | 全量微调 | |
| dynamic high-resolution strategy | 动态高分辨率策略 | |
| fixed-resolution strategy | 固定分辨率策略 | |
| SRCC / PLCC | SRCC / PLCC | 指标名保留 |
| mean opinion score (MOS) | 平均意见分 | 首次出现附 MOS |
| zero-shot transfer | 零样本迁移 | |
| out-of-distribution | 分布外 | |
| positivity bias | 正面偏置 | |
| discretization / quantization loss | 离散化 / 量化损失 | |
| thumbnail | 缩略图 | |
| two-stage training paradigm | 两阶段训练范式 | |

### 交叉验证记录

| 块 id | 原文要点 | 译文 | 语义一致性 |
|---|---|---|---|
| b0010 | 与 3–30 年经验的美学专家合作定义 8 个可解释细粒度属性；ArtiMuse-10K 含 10,000 张图、5 大类 | 我们与美学领域专家（从业经验从 3 年到 30 余年不等）合作，系统定义了八个可解释的细粒度美学属性……包含 10,000 张图像，覆盖 5 个大类与 15 个子类 | 一致，数值与类别数未改动 |
| b0053 | 指定 101 个已有词元对应 0–100 整数分数；分数 1 的实际词元为 ab | 我们指定 101 个已有词元作为 [Aes_Score_Token]，每个对应 0 到 100 的整数分数……其实际词元为 ab | 一致，4 个占位符顺序与原文一致 |
| b0071 | PARA 与 ArtiMuse-10K 上领先超过 0.05 PLCC | 它在 PARA [17] 与 ArtiMuse-10K 数据集上以超过 0.05 PLCC 的优势领先其他模型 | 一致 |
| b0168 | SPAQ 11,125 张图，80% 样本 MOS 或四项质量指标均值落在极端区间 | SPAQ 数据集包含 11,125 张图像，我们按两条关键准则筛选……80% 的样本……须落在 ⟦SLOT_7⟧ 或 ⟦SLOT_8⟧ 的极端区间内 | 一致，2 个占位符原样保留 |
| b0217 | 固定分辨率相比动态策略使 SRCC 与 PLCC 各提升约 0.3，效率提高一倍以上 | 采用固定分辨率策略相比动态高分辨率策略可使 SRCC 与 PLCC 指标各提升约 0.3，同时把训练与推理效率提高一倍以上 | 一致 |

### 一致性与数字核查

- 术语：全文统一使用「图像美学评估（IAA）」「多模态大语言模型（MLLM）」「词元」「分词器」「词表」「细粒度美学属性」「结构化美学分析」；`ArtiMuse`、`ArtiMuse-10K`、`Token As Score`、`Text As Score`、`Level As Score`、`InternVL-3-8B`、`Qwen2.5-7B`、`Gemini-2.0-flash`、`LoRA` 等专名原样保留。
- 数字与指标：10,000、5、15、8、101、0–100、350,000、10,023、4,898、11,125、1,488、1,443、1,400、4,800、9,000、1,000、20、128、80%、75、25、0.05、0.3、8B、72B、78B 等数值，以及 SRCC / PLCC / MOS / MOSz / PLCC / GPA 类指标名均原样保留，未作换算。
- 占位符：逐块脚本比对，`⟦SLOT_0⟧`–`⟦SLOT_22⟧` 共 23 处，译文与原文在编号、数量与出现顺序上完全一致；构建脚本 `stray=0`。
- 编码：`zh.json` 与 `index.html` 均不含 U+FFFD；构建脚本 `mojibake=0`。
- 不变量：表格、公式、SVG 提示模板、参考文献块未翻译；176 个 text 块一一对应，未做合并或拆分。

### 遗留问题

- 无图片缺失（`missing_img=0`）。
- 原文 b0015 中模型名写作 `ArtMuse`（疑为 `ArtiMuse` 笔误）、b0178 与 b0209 中数据集名写作 `AriMuse-10K`（疑为 `ArtiMuse-10K` 笔误），译文按原文拼写保留，未作改动，此处记录备查。
- 原文 b0029 称内部样本与整体构成「分别如图 4 与图 4 所示」，两处编号重复，译文按原文保留，未推测为其他图号。
- 原文 b0077 称「开展 4 组实验 (a)-(c)」，数量与编号范围不一致，译文按原文保留。

## 复核记录（第二轮交叉验证）

- 复核方式：`sample_blocks.py`（随机种子 4 与 11，各取 6／4 块）＋ 全文机检（缺译、未译、⟦SLOT_n⟧ 槽位一致性、数字、残留英文词、结构与编码）。
- 抽查块 ID（10 块）：b0057、b0074、b0171、b0056、b0217、b0220、b0253、b0084、b0165、b0188
- 结构核验：`index.html` 已加载 `tex-mml-chtml.js`；图片 `src` 全为 `figures/...` 本地相对路径、无 http 外链；无 U+FFFD；顶部中文标题与中文摘要、底部「返回总目录」链接均存在。
- 抽查 10 块，未发现实质错误：无漏译整句、无错译关键结论、数字／百分比／模型名／数据集名／指标名与原文一致、`⟦SLOT_n⟧` 槽位数量与编号一致（个别块内槽位顺序按中文语序调整，语义对应正确）、术语篇内统一。
- 已重跑 `build_index.py` 校验，输出 `missing`／`stray`／`mojibake`／`missing_img` 四项均为 0。
- 未改动项：保留英文的专有名词、参考文献、代码与提示词模板、表格数据（规范要求），例如章节标题中的缩写名与 `{...}` 占位模板均按原文保留。
