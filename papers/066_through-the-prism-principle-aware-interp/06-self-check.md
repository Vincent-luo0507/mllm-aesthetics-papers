# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 195（文本 112 / 原子 83）|
| 已译文本块 | 112 / 112 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 57 · 已还原 57 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 165 |
| `<img>` 元素 | 28 |
| `<table>` 元素 | 12 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| PRISM | PRISM | 基准名，全称在首次出现处给出中文释义 |
| design principle | 设计原则 | |
| coherence | 连贯性 | 文本与视觉元素之间的语义一致性 |
| readability | 可读性 | |
| contrast | 对比度 | |
| alignment | 对齐 | |
| overlap | 遮挡 | overlap perturbation 亦指非预期遮蔽 |
| layout | 版面 | 全文统一，graphics layout 同样译「版面」 |
| composed layout / perturbed layout | 原始版面 / 扰动版面 | |
| perturbation | 扰动 | |
| principle-disentangled | 原则解耦 | disentanglement 统一译「解耦」 |
| scorer | 打分器 | PRISM-Scorer 不译 |
| localiser / localisation | 定位器 / 定位 | |
| grounding function | 评估函数 | 指出满足某原则的概率；visual grounding 另译「视觉定位」 |
| vision-language model (VLM) | 视觉语言模型（VLM） | |
| multimodal large language model (MLLM) | 多模态大语言模型（MLLM） | |
| instruction tuning / instruct-tuning | 指令微调 | 全文统一 |
| beam search | 集束搜索 | |
| system prompt | 系统提示 | |
| few-shot prompting | 少样本提示 | |
| SigLIP-v2 / OpenCLIP / DINOv2 | SigLIP-v2 / OpenCLIP / DINOv2 | 模型名不译 |
| Crello / CreatiDesign / GDE | Crello / CreatiDesign / GDE | 数据集名不译 |
| IoU | IoU | 交并比，首次出现括注 |
| AUC / Precision / Recall / F1 | AUC / 精确率 / 召回率 / F1 | |
| LoRA adapter | LoRA 适配器 | |
| held-out validation split | 留出验证集 | |
| out-of-domain (OOD) | 分布外（OOD） | |
| early stopping | 早停 | |
| element ID | 元素 ID | |
| theme | 主题 | |

### 交叉验证记录

| 块 id | 原文要点 | 译文要点 | 一致性 |
|---|---|---|---|
| b0031 | 五项原则的定义：连贯性、可读性、对比度、对齐、遮挡 | 五项定义逐条对应，未遗漏或调换顺序 | 一致 |
| b0034 | Crello 约 20K 训练 / 2K 验证；每原则各约 20K / 2K；五项合计约 100K / 10K | 三组数量与「每原则」与「合计」的层级关系均保留 | 一致 |
| b0064 | 五分类器；40K 训练、4K 测试；90–10 验证划分；连续七轮无改善早停 | 四个数量与早停条件原样保留，指标名未改 | 一致 |
| b0068 | TP/FP/FN 定义；LoRA 适配器每条原则一个；3-shot 少样本基线 | 三类集合关系与对比基线（base、3-shot、GPT-4o-mini、GPT-4o）逐项对应 | 一致 |
| b0083 | 指令微调模型 F1：可读性 0.80、对比度 0.72、遮挡 0.77 | 三个分数与各自原则一一对应，未互换 | 一致 |

### 一致性与数字核查

- 术语一致性：用 Grep 在 `zh.json` 中检索「连贯性」「可读性」「对比度」「对齐」「遮挡」「版面」「扰动」「打分器」「定位器」「解耦」「指令微调」「集束搜索」等核心术语，确认全文译法唯一；「版面」未与「布局」混用，「遮挡」未与「重叠」混用（IoU 相关处保留「重叠（IoU）」这一原文表述）。
- 数字与指标：所有数量（100K、10K、20K、2K、400K、40K、4K、200、100、15、10、3、7、2 等）、评分量表（1–7，中点为 4；0–1 连续量表）、分数区间（F1 0.72–0.76、AUC 0.80–0.82）、具体分数（0.80、0.72、0.77、0.19、0.62、0.66、1.3）与划分比例（90–10）均原样保留；模型名（Qwen-2.5-VL、GPT-4o、GPT-4o-mini、SigLIP-v2、OpenCLIP、DINOv2、ViT-B/16）、数据集名（Crello、CreatiDesign、GDE、WebLI、ImageNet）与指标名（IoU、AUC、F1、RGB、JSON）未做任何改动。
- 占位符完整性：写入前逐块比对原文与译文的 `⟦SLOT_n⟧` 列表，slot 0–56 全部一一对应；脚本校验 `⟦SLOT⟧` 残留为 0。
- 编码：`zh.json` 与 `index.html` 均不含 U+FFFD，脚本 mojibake 计数为 0。
- 不变量：参考文献、表格、公式、图片（`t:"keep"`）一律未翻译；正文块一块对一块，未合并或拆分。

### 遗留问题

- b0046 与 b0033、b0052 中包含英文提示模板与示例字符串（如 “Select the text with readability issues due to small font size.”、“dolphin show”、“onedito”、“Kid’s Birthday Party”）。这些是实际输入模型的指令或数据集中的字面内容，改动会破坏可复现性，故保留英文原文。
- 原文 b0166 提示「结果见图 3」，而第 6 节与附录 F 引用「Section 5.4」，正文实际并无 5.4 节；译文按原文保留这些交叉引用，未做修改。
- 无图片缺失（missing_img = 0）。

## 复核记录（第二轮交叉验证）

- 复核方式：`sample_blocks.py`（随机种子 4 与 11，各取 6／4 块）＋ 全文机检（缺译、未译、⟦SLOT_n⟧ 槽位一致性、数字、残留英文词、结构与编码）。
- 抽查块 ID（9 块）：b0085、b0040、b0090、b0078、b0066、b0052、b0063、b0039、b0030
- 结构核验：`index.html` 已加载 `tex-mml-chtml.js`；图片 `src` 全为 `figures/...` 本地相对路径、无 http 外链；无 U+FFFD；顶部中文标题与中文摘要、底部「返回总目录」链接均存在。
- 抽查 9 块，未发现实质错误：无漏译整句、无错译关键结论、数字／百分比／模型名／数据集名／指标名与原文一致、`⟦SLOT_n⟧` 槽位数量与编号一致（个别块内槽位顺序按中文语序调整，语义对应正确）、术语篇内统一。
- 已重跑 `build_index.py` 校验，输出 `missing`／`stray`／`mojibake`／`missing_img` 四项均为 0。
- 未改动项：保留英文的专有名词、参考文献、代码与提示词模板、表格数据（规范要求），例如章节标题中的缩写名与 `{...}` 占位模板均按原文保留。
