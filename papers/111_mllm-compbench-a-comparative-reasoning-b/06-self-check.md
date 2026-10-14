# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 247（文本 149 / 原子 98）|
| 已译文本块 | 149 / 149 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 3 · 已还原 3 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 7 |
| `<img>` 元素 | 17 |
| `<table>` 元素 | 11 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| comparative reasoning | 比较推理 | 本文核心能力名，全文统一 |
| relativity | 相对性 | 八类比较维度统称 |
| MLLM-CompBench | MLLM-CompBench | 基准名，保留原文 |
| artificial general intelligence (AGI) | 通用人工智能（AGI） | 首次附英文 |
| multimodal large language model (MLLM) | 多模态大语言模型（MLLM） | 首次附英文，后文用 MLLM |
| large multimodal model (LMM) | 大型多模态模型（LMM） | MLLM 的别称 |
| vision and language (V&L) | 视觉与语言（V&L） | 任务域统称 |
| visual question answering (VQA) | 视觉问答（VQA） | 首次附英文 |
| image captioning | 图像描述 | 任务名 |
| image-text retrieval | 图文检索 | 任务名 |
| Visual Attribute relativity | 视觉属性相对性 | 八类之一 |
| Existence relativity | 存在性相对性 | 八类之一 |
| State relativity | 状态相对性 | 八类之一 |
| Emotion relativity | 情绪相对性 | 八类之一 |
| Temporality / Spatiality relativity | 时间性／空间性相对性 | 八类之二 |
| Quantity / Quality relativity | 数量／质量相对性 | 八类之二 |
| triplet | 三元组 | 图像对＋问题＋答案 |
| image pair | 图像对 | 数据基本单位 |
| two-stage reasoning | 两阶段推理 | 先分别描述再比较 |
| LoRA | LoRA | 微调技术，保留原名 |
| CLIP similarity | CLIP 相似度 | 筛选图像对的手段 |
| learning to rank (LTR) | 排序学习（LTR） | 相关工作 |
| learning with preference | 基于偏好的学习 | 相关工作 |
| in-context learning | 上下文学习 | 提示策略 |
| multiple-choice question | 多项选择题 | 自动评测用题型 |
| test split / held-out split | 测试划分／保留划分 | 80:20 切分 |
| chance level | 随机水平 | 二值选择题基线 |
| error analysis | 错误分析 | §5.3 小节 |
| out-of-focus | 失焦 | 错误类型之一 |
| annotator / evaluator | 标注者／评测者 | 两类人员，严格区分 |
| low-level visual perception | 低层视觉感知 | 质量相对性所需能力 |

### 交叉验证记录

| 块 id | 原文要点 | 译文要点 | 一致性 |
|---|---|---|---|
| b0009 | 八类相对性定义，含 SLOT_1 个 K 级三元组，举例鸟喙长度、蝴蝶特征、任意球帧、杯子远近、动物实例数 | 八类逐项对应，示例问题与槽位原样保留 | 一致 |
| b0058 | 质量控制：剔除低分辨率、含糊相对性、CLIP 过滤、交叉核验，最终 39.8K 三元组、八类相对性、十四领域 | 数字与流程逐项对应 | 一致 |
| b0065 | 所有模型平均准确率低于 SLOT_3%，GPT-4V 最高 74.7% | 槽位与 74.7% 原样保留 | 一致 |
| b0070 | 空间任务全部低于 70%，GPT-4V 与 Gemini1.0-Pro 仅 56.1% 与 56.6%，略高于随机水平 | 四个百分比原样保留 | 一致 |
| b0075 | 微调实验：SoccerNet 20.6K、VQAv2 20.9K，LoRA 微调 LLaVA-1.6，时间任务受益、数量增益有限，归因于 CLIP 编码器 | 数字、模型名与技术名原样保留 | 一致 |

### 一致性与数字核查

- 术语统一：以 Grep 核对 zh.json，全文统一使用「比较推理」「相对性」「三元组」「图像对」「两阶段推理」「标注者／评测者」等译法；八类相对性名称（视觉属性、存在性、状态、情绪、时间性、空间性、数量、质量）在正文与附录中译法完全一致。
- 数字核查：40K / 39.8K / 31.8K / 7.9K / 5.3K / 2.2K / 1.1K / 13.3K / 1.9K / 9.8K / 1K / 20.6K / 20.9K / 74.7% / 92.2% / 89.7% / 91.8% / 96.2% / 56.1% / 56.6% / 63.8% / 47.7% / 73.0% / 18% / 140 / 245 / 115 / 27 / 294 / 620 / 15 / 22 / 200K / 40 / 16／3／2e-5 等数值均与原文一致。
- 占位符完整性：脚本自校验 `⟦SLOT⟧` 残留为 0；另用脚本逐块比对原文与译文的 `⟦SLOT_n⟧` 序列，149 个文本块全部完全一致（含顺序）。
- 编码检查：zh.json 与 index.html 均不含 U+FFFD，脚本 mojibake 计数为 0。

### 遗留问题

- 无图片缺失（missing_img = 0）。
- 原文脚注（如 b0062 的脚注 1、2 与 b0226 的脚注 3–6）在提取时与主文本混排，译文以括号形式就地标注脚注内容，未改动原文信息。
- 附录 B 中的英文提示词模板（b0185、b0190、b0192、b0201）属于自然语言指令而非代码，按正文要求译为中文，其中的占位符标记（如 [属性列表]、[上一步得到的物体]）原样保留。

## 复核记录（第二轮交叉验证）

- 抽查块（9 块，随机种子 7 与 42）：b0089、b0244、b0052、b0072、b0033、b0087、b0222、b0036、b0023
- 全篇自动化校验：逐块比对 EN/ZH 的 `⟦SLOT_n⟧` 占位符编号与顺序、数字/量级一致性，未发现丢失、错位或篡改。
- 抽查 9 块，未发现实质错误。
- 重跑 `build_index.py` 后四项校验：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
