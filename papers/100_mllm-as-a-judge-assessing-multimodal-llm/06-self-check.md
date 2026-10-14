# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 304（文本 175 / 原子 129）|
| 已译文本块 | 175 / 175 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 24 · 已还原 24 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 69 |
| `<img>` 元素 | 8 |
| `<table>` 元素 | 12 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| Multimodal Large Language Model (MLLM) | 多模态大语言模型（MLLM） | 首次括注缩写，后文用「MLLM」 |
| LLM-as-a-Judge | LLM-as-a-Judge（以大模型为裁判） | 保留原名，首次括注中文 |
| judge (v./n.) | 判定 / 裁判 | 动词统一「判定」，名词统一「裁判」 |
| Scoring Evaluation | 评分评测 | 三类任务之一，统一 |
| Pair Comparison | 成对比较 | 统一 |
| Batch Ranking | 批量排序 | 统一；原文 §3.2 写作 Batch Evaluation，按正文任务名统一译为「批量评测/批量排序」对应其语境 |
| Analyze-then-Judge | 「先分析后判定」（Analyze-then-Judge） | 范式名，首次括注英文 |
| Chain-of-Thought (CoT) | 思维链（CoT） | 统一 |
| image-instruction pair | 图像—指令对 | 统一，连字符用一字线 |
| egocentric bias | 自我中心偏差 | 统一 |
| position bias | 位置偏差 | 统一 |
| length bias / verbosity bias | 长度偏差 / 冗长偏差 | 同一现象的两种叫法分别译出 |
| hallucination | 幻觉 | 统一 |
| human agreement | 人类认同度 | 统一，不用「一致性」以免与 consistency 混淆 |
| consistency | 一致性 | 指重复实验结果，统一 |
| Majority Consistency Criterion (MCC) | 多数一致性准则（MCC） | 统一 |
| Pearson similarity | 皮尔逊相似度 | 统一 |
| Normalized Levenshtein distance | 归一化 Levenshtein 距离 | 统一 |
| Mean Absolute Deviation (MAD) | 平均绝对偏差（MAD） | 统一 |
| F1-score / recall | F1 分数 / 召回率 | 统一 |
| vision expert | 视觉专家 | 指用 GPT-4V 生成图像描述，统一 |
| scaling law | 缩放定律 | 统一 |
| human-in-the-loop | 人在回路 | 首次括注英文 |
| multi-agent debating | 多智能体辩论 | 统一 |
| tie / non-tie | 平局 / 非平局 | 统一 |
| w. / w.o. vision input | 有 / 无视觉输入 | 统一 |
| free-form response | 自由形式回答 | 统一 |
| infographics | 信息图 | 统一 |
| Optical Character Recognition (OCR) | 光学字符识别（OCR） | 统一 |
| Visual Question Answering (VQA) | 视觉问答（VQA） | 统一 |
| sequential image dataset | 时序图像数据集 | 统一 |
| RLHF / DPO | RLHF / DPO | 保留缩写 |
| post-alignment training | 后对齐训练 | 统一 |

### 交叉验证记录

| 块 id | 原文要点 | 译文 | 一致性 |
|---|---|---|---|
| b0023 | 三步骤流程与数据集划分，含 SLOT_0–SLOT_9 | ……我们采集数据集 ⟦SLOT_0⟧，其中包含来自 10 个不同领域……的图像 ⟦SLOT_1⟧ 及其对应指令 ⟦SLOT_2⟧……⟦SLOT_7⟧ 用于评分评测，⟦SLOT_8⟧ 用于成对比较，⟦SLOT_9⟧ 用于批量排序 | 10 个占位符逐一对应；三步骤顺序与三个子集映射无错位 |
| b0058 | GPT-4V 0.490、Gemini 0.304；高分偏差类比 Yes/No 偏差 | GPT-4V 与人类评分的相似度最高，达到 0.490。相比之下，Gemini 仅为 0.304……我们把这归因于一种「高分」偏差，类似于 Liu 等（2023a）所识别的「是/否」偏差 | 数值与因果链条完整，未添加评论 |
| b0059 | 成对比较 0.636（tie）/ 0.773（non-tie），多数据集超 0.8 | GPT-4V 在成对比较任务中胜过其他 MLLM，在有平局设定下达到 0.636、在无平局设定下达到 0.773，在多个数据集上超过 0.8 | 三个数值与设定一一对应 |
| b0086 | LLaVA 复现「ABCD」序列的比例 88.2% | 若批量排序提示中包含形如「ABCD」的序列，LLaVA 会在 88.2% 的回答中复现该序列 | 数字与示例序列原样保留 |
| b0216 | 3,300 对 × 4 模型 = 13,200；总计 17,656 条回答 | 每个 VLM 生成一条回答，共形成 13,200 条回答的集合……在从 MLLM 处共收集到 17,656 条回答后 | 数量关系与模型分组（Mementos 用 ChatUnivi/VideoChat2）均完整 |

### 一致性与数字核查

- **术语统一**：已检索 `zh.json`，「判定 / 裁判 / 评分评测 / 成对比较 / 批量排序 / 人类认同度 / 一致性 / 幻觉 / 自我中心偏差 / 位置偏差 / 长度偏差」等核心术语译法唯一；「Batch Ranking」与原文 §3.2 的「Batch Evaluation」按各自语境分别译出，未强行统一为同一词。
- **数字核查**：核对了 14 个数据集、4,414 个图像—指令对、4,114 张图像、约 17,000 / 17,656 条回答、3,300、13,200、300、600、0.490、0.304、0.636、0.773、0.8、0.361、0.675、0.611、0.418、70%、79.3%、78%、72%、79.9%、67.7%、0.435、88.2%、0.6、0.75、50 条、10 位标注者、6 位作者、2048、温度 0.9/0.4/0 等全部数值，未作改动；模型名（GPT-4V、Gemini-Pro-Vision-1.0/1.5、LLaVA-1.5/1.6、CogVLM、Qwen-VL-Plus/Max、LLaMA-2-70b、Mixtral-8x7b、ChatUnivi、VideoChat2、GLM-4V）与指标名（BLEU、METEOR、ROUGE、CIDEr）均原样保留。
- **占位符完整性**：175 个文本块逐块比对 `⟦SLOT_n⟧` 集合，源文与译文完全一致（差异 0）。
- **编码检查**：`zh.json` 与 `index.html` 中 U+FFFD 计数为 0。
- **不变量**：表格、公式、图片与参考文献块按 `t:"keep"` 跳过；段落一一对应，未删减、合并或拆分。

### 遗留问题

- 原文 b0024–b0026 中任务名在正文与 §3.2 处存在 "Batch Ranking" / "Batch Evaluation" 两种写法，译文按原文各自用词分别处理。
- 原文 b0216 中的 "rebuttal"（同行评议答复期）属 arXiv 版本特有的表述，译文保留了该语境。
- 原文 b0224/b0229/b0231 中 tok-⟦SLOT_20⟧、top-⟦SLOT_21⟧、top-⟦SLOT_22⟧ 为公式占位符，已逐一原样保留。
- `missing_img` 为 0，无需补图。

## 复核记录（第二轮交叉验证）

- 复核方式：`sample_blocks.py`（随机种子 4 与 11，各取 6／4 块）＋ 全文机检（缺译、未译、⟦SLOT_n⟧ 槽位一致性、数字、残留英文词、结构与编码）。
- 抽查块 ID（10 块）：b0208、b0108、b0015、b0013、b0061、b0057、b0253、b0086、b0226、b0040
- 结构核验：`index.html` 已加载 `tex-mml-chtml.js`；图片 `src` 全为 `figures/...` 本地相对路径、无 http 外链；无 U+FFFD；顶部中文标题与中文摘要、底部「返回总目录」链接均存在。
- 抽查 10 块，未发现实质错误：无漏译整句、无错译关键结论、数字／百分比／模型名／数据集名／指标名与原文一致、`⟦SLOT_n⟧` 槽位数量与编号一致（个别块内槽位顺序按中文语序调整，语义对应正确）、术语篇内统一。
- 已重跑 `build_index.py` 校验，输出 `missing`／`stray`／`mojibake`／`missing_img` 四项均为 0。
- 未改动项：保留英文的专有名词、参考文献、代码与提示词模板、表格数据（规范要求），例如章节标题中的缩写名与 `{...}` 占位模板均按原文保留。
