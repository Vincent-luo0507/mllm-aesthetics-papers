# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 159（文本 74 / 原子 85）|
| 已译文本块 | 74 / 74 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 70 · 已还原 70 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 150 |
| `<img>` 元素 | 7 |
| `<table>` 元素 | 15 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| image aesthetic assessment (IAA) | 图像美学评价（IAA） | 首次出现括注英文 |
| personalized image aesthetic assessment (PIAA) | 个性化图像美学评价（PIAA） | |
| Multimodal Large Language Model (MLLM) | 多模态大语言模型（MLLM） | |
| PRAC | PRAC | 方法名不译 |
| PreferSelect / PreferMerge | PreferSelect / PreferMerge | 组件名不译 |
| preference-rich sample | 富偏好样本 | 全文统一 |
| aesthetically-resonant cohort | 美学共鸣群组 | cohort 统一译「群组」 |
| Collective Controversy Metric (CCM) | 群体争议度指标（CCM） | |
| Personalized Deviation Metric (PDM) | 个性化偏离度指标（PDM） | |
| preference richness | 偏好丰富度 | |
| preference embedding | 偏好嵌入 | |
| Generic Aesthetic Predictor | 通用美学预测器 | |
| model merging | 模型合并 | |
| few-shot learning (FSL) | 小样本学习（FSL） | |
| meta-learning | 元学习 | |
| task arithmetic | 任务算术 | |
| LoRA | LoRA | 参数高效微调模块，不译 |
| Kullback-Leibler (KL) divergence | KL 散度 | |
| Fisher Information Matrix (FIM) | Fisher 信息矩阵（FIM） | |
| User Pool | 用户池 | |
| Target Relevance / Cohort Diversity | 目标相关性 / 群组多样性 | |
| query set | 查询集 | |
| in-context learning | 上下文学习 | |
| Big-Five personality traits | 大五人格特质 | |
| SRCC | SRCC | Spearman 秩相关系数，指标名不译 |
| user profile | 用户画像 | |
| rationale | 解释依据 | |
| 10-shot / 100-shot | 10-shot / 100-shot | 设定名不译 |

### 交叉验证记录

| 块 id | 原文要点 | 译文要点 | 一致性 |
|---|---|---|---|
| b0025 | 五个离散美学层级 [Excellent, Good, Fair, Bad, Poor]；集成 LoRA 做美学分布训练；用 KL 散度损失优化 | 五个层级名原样保留，LoRA 与 KL 散度术语对应 | 一致 |
| b0034/b0036 | CCM 定义为分布的标准差；公式含 5 个层级、均值与概率 | 度量定义与公式变量说明逐项对应，未改变运算含义 | 一致 |
| b0057 | 四个基准数据集；PARA 的六个用户画像属性；REAL-CUR 每张图仅由所有者评分 | 四个数据集名与六个属性（年龄、性别、教育程度、艺术经验、摄影经验、人格特质）逐项对齐 | 一致 |
| b0060 | 超参数 α=0.3、K=6、β=0.5；单张 RTX 3090 可完成训练与推理 | 三个超参数值落在 ⟦SLOT_55–57⟧ 内，硬件型号未改动 | 一致 |
| b0078 | 每用户重复 10 次随机采样；四个数据集上提升均超过 5% | 「10 次」与「5%」原样保留，比较对象（通用美学预测器基线）未变 | 一致 |

### 一致性与数字核查

- 术语一致性：用 Grep 在 `zh.json` 中检索「图像美学评价」「个性化图像美学评价」「多模态大语言模型」「富偏好样本」「美学共鸣群组」「群体争议度」「个性化偏离度」「偏好嵌入」「模型合并」「查询集」「用户池」等核心术语，确认全文同一种译法，未出现同义轮换。
- 数字与指标：所有数量（398、40、37、22、14、28,220、3,000、35,263、4,737、2,871、8,458、1,542 等）、超参数（0.3、6、0.5、5%）、评测设定（10-shot、100-shot）与指标名（SRCC、CCM、PDM、FIM、KL）均原样保留；模型与数据集名（mPLUG-Owl3、Qwen3-VL、InternVL-3.5、PARA、FLICKR-AES、REAL-CUR、AADB、ImageCorruptions 等）未做任何改动。
- 占位符完整性：写入前逐块比对原文与译文的 `⟦SLOT_n⟧` 列表，slot 0–69 全部一一对应；脚本校验 `⟦SLOT⟧` 残留为 0。
- 编码：`zh.json` 与 `index.html` 均不含 U+FFFD，脚本 mojibake 计数为 0。
- 不变量：参考文献、表格、公式、图片（`t:"keep"`）一律未翻译；正文块一块对一块，未合并或拆分。

### 遗留问题

- b0026、b0037、b0087 三块包含英文提示模板原文（如 “How would you rate the aesthetic quality of this image?”、"You are a …"、“Please explain why you rated the image this way”）。这些是实际输入模型的提示词，改动会破坏其可复现性，故保留英文原文，仅把周围的说明性文字译为中文。
- b0025 与 b0029 中的五个美学层级名（Excellent、Good、Fair、Bad、Poor）属于数据集定义的枚举值，按原文保留。
- 无图片缺失（missing_img = 0）。

## 复核记录（第二轮交叉验证）

- 复核人：独立复核 Agent 08 号
- 抽查方式：`sample_blocks.py` 两轮随机抽样（种子 8 与 2024）+ 全量脚本化交叉校验（数字/公式占位符/未译块/长度比）
- 抽查块（共 12 块次）：b0019, b0094, b0062, b0073, b0002, b0047 / b0094, b0079, b0017, b0081, b0020, b0071
- 结论：共记录 1 条核验事项，逐条判定如下。

| 块 ID | 问题类型 | 复核发现 | 判定与处理 |
|---|---|---|---|
| b0045 | 公式占位符顺序校验 | EN 为 ⟦SLOT_34⟧⟦SLOT_35⟧ 顺序，ZH 为 ⟦SLOT_35⟧⟦SLOT_34⟧ | 经核对 slots 内容，ZH 语序与 EN 语义一致，属合理换位，未修改。 |

- 其中标注「未修改」者为经核对后确认**非错误**（中文语序换位、等值数字改写、规范要求的英文专名保留），按规格书 §2「避免过度修改」不予改动。
- 重跑 `build_index.py`：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
