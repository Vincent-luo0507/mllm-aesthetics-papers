# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 274（文本 132 / 原子 142）|
| 已译文本块 | 132 / 132 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 101 · 已还原 101 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 227 |
| `<img>` 元素 | 11 |
| `<table>` 元素 | 29 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| Image Quality Assessment (IQA) | 图像质量评估（IQA） | 首次出现附缩写 |
| Multi-modal Large Language Model (MLLM) | 多模态大语言模型（MLLM） | 首次出现附缩写 |
| score regression | 分数回归 | 全文统一 |
| score distribution | 分数分布 | 全文统一 |
| soft label | 软标签 | 与 one-hot 标签严格区分 |
| one-hot label | one-hot 标签 | 全文统一，不另译“独热” |
| Mean Opinion Score (MOS) | 平均意见分数（MOS） | 首次出现附英文全称 |
| discretization | 离散化 | 全文统一 |
| level token | 等级词元 | 指五个等级文本词元 |
| level text | 等级文本 | 消融实验中的变量 |
| fidelity loss | 保真损失 | 首次出现附英文原词 |
| Thurstone’s model | Thurstone 模型 | 心理测量模型名保留 |
| post-adjustment | 后调整 | 校正截断误差的步骤 |
| truncation error | 截断误差 | 全文统一 |
| vision abstractor | 视觉抽象器 | mPLUG-Owl2 组件，首次出现附英文 |
| vision-to-text connector | 视觉到文本连接器 | 架构组件 |
| closed-set softmax | 闭集 softmax | 推理时所用 |
| next token prediction loss | 下一词元预测损失 | 全文统一 |
| KL divergence | KL 散度 | 指标与损失名 |
| JS divergence | JS 散度 | 分布距离指标 |
| Wasserstein distance | Wasserstein 距离 | 分布距离指标 |
| PLCC (Pearson Linear Correlation Coefficient) | 皮尔逊线性相关系数（PLCC） | 首次出现附英文全称 |
| SRCC (Spearman Rank-order Correlation Coefficient) | 斯皮尔曼秩相关系数（SRCC） | 首次出现附英文全称 |
| full-reference / non-reference IQA | 全参考 / 无参考 IQA | 成对出现，译法固定 |
| in-the-wild | 真实场景 | 指真实拍摄失真 |
| synthetic distortion | 合成失真 | 失真类别之一 |
| model-processed distortion | 模型处理失真 | 指 PIPAL |
| out-of-distribution | 分布外 | 泛化评测语境 |
| co-training | 联合训练 | 全文统一 |
| two-alternative forced choice (2AFC) | 二选一强制选择（2AFC） | 首次出现附英文与缩写 |
| Elo rating | Elo 评分 | 标注体系名保留 |
| pseudo variance | 伪方差 | PIPAL 特殊设计 |
| unit impulse function | 单位冲激函数 | 数学术语 |

### 交叉验证记录

| 块 id | 原文要点 | 译文要点 | 一致性 |
|---|---|---|---|
| b0009 | MLLM 离散词元输出与连续分数之间的分布鸿沟；图 1 中图像 A/B/C 的 one-hot 标签反例 | 分布鸿沟与两个反例完整译出，引用 [70] 保留 | 一致，无漏译 |
| b0022 | MOS 4.30 落入第五区间 → “excellent”；五个等级文本；脚注 1 的归一化说明 | 4.30 与五个等级文本原样保留，⟦SLOT_2⟧、⟦SLOT_3⟧ 保留 | 一致 |
| b0025 | 三个局限（独立假设、忽略方差、边界问题）+ 信息损失；Q-Align 五级分数 {1,2,3,4,5}；误差约 ⟦SLOT_4⟧–⟦SLOT_5⟧ | 四点逐一对应，集合与两个占位符原样保留 | 一致 |
| b0085 | 多数据集联合训练四条结论；TID2013 SRCC 33.1%；PIPAL PLCC 0.495→0.724；CSIQ 0.900→0.863；AGIQA-3K 约 0.8 | 数字与数据集名原样保留，编号 #0/#1/#2 保留 | 一致，未换算 |
| b0268 | 7B 参数；15.2G 存储（bfloat16）；15.8G（bs 1）/ 23.0G（bs 64）显存 | 全部数字与格式名原样保留 | 一致 |

### 一致性与数字核查

- 术语统一：用 Grep 在 `zh.json` 中检索「图像质量评估」「多模态大语言模型」「分数回归」「分数分布」「软标签」「one-hot 标签」「平均意见分数」「离散化」「等级词元」「保真损失」「视觉抽象器」「联合训练」等核心术语，全文译法唯一；缩写 IQA / MLLM / LLM / MOS / PLCC / SRCC / KL / JS / 2AFC / LoRA 均原样保留；模型与数据集名（KonIQ、SPAQ、LIVE-Wild、FLIVE、KADID、TID2013、CSIQ、PIPAL、AGIQA-3K、Q-Align、mPLUG-Owl2、LLaMA-2-7B、ViT-L/14）一律不译。
- 数字核查：MOS 4.30 / 3.38 / 3.49、阈值 3.4、权重 0.05、学习率 2e-5、批大小 64 / 256、训练 3 轮、视觉词元 64、隐藏维度 4096 / 1024、预热比例 0.03、性能提升 1.3% / 4.6% / 33.1%、PLCC 0.462 / 0.495 / 0.724 / 0.900 / 0.863 / 约 0.8、吞吐 32.29 张/秒、存储 15.2G 与显存 15.8G / 23.0G、PIPAL 分数 934.95 与 1835.99、比例 20%、0.29% 均未改动或换算。
- 占位符完整性：脚本统计内联槽位 101、已还原 101；另用脚本逐块比对 132 个文本块的 `⟦SLOT_n⟧` 集合，全部一致。
- 编码检查：`zh.json` 与 `index.html` 中 U+FFFD 计数均为 0，编码 UTF-8。
- 不变量：表格、公式、图片、参考文献块一律未翻译；未删减、合并或拆分段落，一块对一块。

### 遗留问题

- 原文 b0104 写作 “Tabs. A7 and A7”，b0253 亦指向表 A7（等级数量消融），与表 A6 编号存在原文内部的不一致；译文按原文照录为“表 A7 与 A7”，未作更正，在此记录。
- 图片引用缺失 0，公式元素 227 个均正常还原，未发现原文乱码或不可解析的块。

## 复核记录（第二轮交叉验证）

- 复核方式：`sample_blocks.py`（随机种子 4 与 11，各取 6／4 块）＋ 全文机检（缺译、未译、⟦SLOT_n⟧ 槽位一致性、数字、残留英文词、结构与编码）。
- 抽查块 ID（9 块）：b0083、b0074、b0033、b0264、b0065、b0097、b0267、b0270、b0036
- 结构核验：`index.html` 已加载 `tex-mml-chtml.js`；图片 `src` 全为 `figures/...` 本地相对路径、无 http 外链；无 U+FFFD；顶部中文标题与中文摘要、底部「返回总目录」链接均存在。
- 抽查 9 块，未发现实质错误：无漏译整句、无错译关键结论、数字／百分比／模型名／数据集名／指标名与原文一致、`⟦SLOT_n⟧` 槽位数量与编号一致（个别块内槽位顺序按中文语序调整，语义对应正确）、术语篇内统一。
- 已重跑 `build_index.py` 校验，输出 `missing`／`stray`／`mojibake`／`missing_img` 四项均为 0。
- 未改动项：保留英文的专有名词、参考文献、代码与提示词模板、表格数据（规范要求），例如章节标题中的缩写名与 `{...}` 占位模板均按原文保留。
