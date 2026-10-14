# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 173（文本 85 / 原子 88）|
| 已译文本块 | 85 / 85 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 54 · 已还原 54 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 117 |
| `<img>` 元素 | 2 |
| `<table>` 元素 | 6 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| Large Vision-Language Model (LVLM) | 大型视觉语言模型（LVLM） | 首次出现括注缩写，其后统一用「LVLM」 |
| large language model (LLM) | 大语言模型（LLM） | |
| position bias | 位置偏差 | 全文核心术语，不混用「位置偏见」 |
| recency bias | 近因偏差 | 与 primacy（首因）对举 |
| primacy | 首因 | 仅在 b0043 出现一次，与「近因」成对 |
| Position-wise Question Answering (PQA) | 逐位置问答（PQA） | 本文提出的任务名 |
| SoFt Attention (SoFA) | SoFt Attention（SoFA） | 方法专名，按系统名保留原文 |
| causal attention | 因果注意力 | |
| bidirectional attention | 双向注意力 | |
| isolated attention | 孤立注意力 | |
| inter-image causal attention | 图像间因果注意力 | |
| attention mask / causal mask | 注意力掩码 / 因果掩码 | |
| position embedding | 位置嵌入 | |
| position encoding function | 位置编码函数 | |
| hidden states | 隐状态 | |
| image tokens | 图像词元 | 全文统一，不混用「图像 token」 |
| linear interpolation | 线性插值 | |
| training-free | 无需训练 | 修饰 SoFA，固定译法 |
| autoregressive | 自回归 | |
| vision encoder | 视觉编码器 | |
| bridging projector | 桥接投影器 | |
| image-text interleaved data | 图文交错数据 | |
| multi-image | 多图像 | 全文统一，不混用「多图」 |
| prediction inconsistency | 预测不一致率 | 本文定义的度量，固定译法 |
| position-agnostic | 与位置无关 | |
| holistic comprehension | 整体理解 | |
| ground truth | 真值 | |
| multi-modal in-context learning | 多模态上下文学习 | |
| many-shot in-context learning | 多示例上下文学习（many-shot in-context learning） | |
| retrieval-augmented generation (RAG) | 检索增强生成（RAG） | |
| LLM-as-a-judge | 以 LLM 为裁判（LLM-as-a-judge） | |
| lost in the middle | “中部丢失”（lost in the middle） | 带引号的专名式说法 |
| multi-modal RAG | 多模态 RAG | |
| long-context | 长上下文 | |
| out-of-distribution | 分布外 | |
| ablation study | 消融实验 | |
| difference spotting | 差异识别 | 基准任务名 |
| object counting | 物体计数 | |
| forensic detection | 取证检测 | |
| visual retrieval / analogy | 视觉检索 / 类比 | |
| sub-image splitting | 子图切分 | |
| Flash Attention | Flash Attention | 不译 |
| U-shaped curve | U 形曲线 | |

### 交叉验证记录

| 块 id | 原文要点 | 译文 | 一致性 |
|---|---|---|---|
| b0009 | 提出「LVLM 中是否存在位置偏差」之问；打乱图像顺序会显著改变预测；举差异识别与计数任务两例 | 受上述研究启发，一个自然而然的问题出现了：LVLM 中是否也存在位置偏差？……这种位置敏感性即便在 GPT-4o [1] 这一领先的专有模型中同样明显。 | 一致。OpenFlamingo、Idefics2、GPT-4o 及文献编号 [56][19][4][24] 全部原样保留 |
| b0012 | 图像词元隐状态受相对位置影响；靠后图像可交互、靠前被孤立；提出 SoFA 作线性插值 | 位置偏差的存在严重损害了模型的稳健性……在现有多图像基准上取得 ⟦SLOT_0⟧ 的平均准确率提升。 | 一致。两点机制与槽位 ⟦SLOT_0⟧ 均保留，未自行填入数值 |
| b0049 | 逐项解释公式符号：查询／键／值、输入词元、位置嵌入、位置编码函数、因果掩码 | 其中 ⟦SLOT_11⟧、⟦SLOT_12⟧ 与 ⟦SLOT_13⟧ 分别表示查询、键与值……⟦SLOT_18⟧ 表示因果掩码，用以保证自回归生成。 | 一致。九个槽位的编号与顺序逐一对应，未改写 |
| b0057 | 替换因果掩码为孤立／双向形式可缓解偏差但带来性能下降，孤立最严重；归因于分布外隐状态 | 我们把语言解码器中默认的因果掩码分别替换为对应的孤立掩码与双向掩码……导致隐状态落入分布外。 | 一致。因果结论与「孤立注意力下降最严重」的判断未增删 |
| b0084 | SoFA 提升上下文学习能力；举 VQAv2／VizWiz／OK-VQA 三基准；VizWiz 4-shot 与 16-shot 的提升 | SoFA 提升了 LVLM 的上下文学习能力……在 VizWiz 上，4-shot 时准确率从 ⟦SLOT_39⟧ 提升到 ⟦SLOT_40⟧，16-shot 时从 ⟦SLOT_41⟧ 提升到 ⟦SLOT_42⟧。 | 一致。四个槽位及 shot 数原样保留，未擅自补值 |

### 一致性与数字核查

- **术语统一**：在 `zh.json` 中回查「位置偏差」「近因偏差」「逐位置问答（PQA）」「图像间因果注意力」「双向注意力」「孤立注意力」「预测不一致率」「与位置无关」「多模态上下文学习」「隐状态」「图像词元」等词条，确认全文译法唯一，未出现同义轮换；「开源模型／专有模型（proprietary）」的对举在全文保持一致。
- **数字与指标**：5／10／15／20 张图像、1,000 与 5,000 个样本、576 个词元、32-shot、FP16、4-shot／8-shot／16-shot、100 张图像、DARPA TIAMAT HR00112490421，以及 b0087 中整行的准确率数值（55.34、59.32、61.37、41.56、44.65、45.35、45.19、48.30、49.02、56.13、61.30、64.85、42.30、46.98、49.17、45.93、49.87、52.36）全部原样保留；VQAv2、OK-VQA、MMMU、BLINK、Mantis-Eval、MuirBench、MIRB、NLVR2、MVBench、VizWiz、Visual Haystack、Multi-modal Haystack、Flash Attention 等数据集与系统名一律未译。
- **占位符**：`⟦SLOT_0⟧`–`⟦SLOT_53⟧` 共 54 个槽位在译文中逐个原样保留。用脚本逐块比对了 `translate_input.json` 与 `zh.json` 中槽位的数量与编号集合，结果为零差异；构建脚本还原计数为「总数 54 · 已还原 54」，残留 0。表格、公式、图片与参考文献块一律未译。
- **编码**：`zh.json` 与 `index.html` 均不含 U+FFFD，脚本 `mojibake` 项为 0。
- **去 AI 味**：回扫确认未使用「值得注意的是／毋庸置疑／众所周知」等空洞填充，未出现「首先…其次…最后」的机械列举；原文以 1）2）3）编号的段落沿用原编号，未改写为「首先／其次」。

### 遗留问题

- b0029 中脚注标记与正文粘连（「LLaVA-NeXT-Interleave11 1 为简洁起见……」），系 PDF 转换所致。译文按原位保留数字标记，未作删除或重排。
- b0087 是一行被识别为段落的表格式数字串（表 3 的扁平化内容）。该块被标记为待翻译文本，故按其原有次序译出表头词（Method → 方法、w/o SoFA → 无 SoFA、w/ SoFA → 有 SoFA），全部数值未作任何改动；表格本身（`<table>` 元素）未翻译。
- 原文 b0042 中「nearly lost」疑为「nearly loses」之笔误，译文按语义顺译，未改动原文。
- 图片文件齐全，`missing_img` 为 0，无图片缺失问题。


## 复核记录（第二轮交叉验证）

- 复核人：独立复核 Agent 08 号
- 抽查方式：`sample_blocks.py` 两轮随机抽样（种子 8 与 2024）+ 全量脚本化交叉校验（数字/公式占位符/未译块/长度比）
- 抽查块（共 12 块次）：b0055, b0072, b0049, b0040, b0045, b0030 / b0092, b0022, b0101, b0053, b0088, b0012
- 结论：抽查未发现实质错误。完整性、准确性、数字与符号、`⟦SLOT_n⟧` 占位符、术语一致性、中文表达六项均通过，未做任何修改。
- 重跑 `build_index.py`：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
