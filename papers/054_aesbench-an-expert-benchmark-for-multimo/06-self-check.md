# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 123（文本 64 / 原子 59）|
| 已译文本块 | 64 / 64 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 3 · 已还原 3 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 6 |
| `<img>` 元素 | 2 |
| `<table>` 元素 | 5 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| image aesthetics perception | 图像美学感知 | 全文统一，不译「审美感知」 |
| Aesthetic Perception (AesP) | 美学感知（AesP） | 四维框架之一 |
| Aesthetic Empathy (AesE) | 美学共情（AesE） | |
| Aesthetic Assessment (AesA) | 美学评价（AesA） | |
| Aesthetic Interpretation (AesI) | 美学阐释（AesI） | |
| Expert-labeled Aesthetics Perception Database (EAPD) | 专家标注美学感知数据库（EAPD） | |
| Multimodal Large Language Model (MLLM) | 多模态大语言模型 | 首次出现补英文 |
| natural images (NIs) | 自然图像（NI） | |
| artistic images (AIs) | 艺术图像（AI） | |
| AI-generated images (AGIs) | 人工智能生成图像（AGI） | |
| perceptual dimension | 感知维度 | |
| Technical quality | 技术质量 | 四感知维度之一 |
| Color and light | 色彩与光影 | |
| Composition | 构图 | |
| Content | 内容 | |
| empathy dimension | 共情维度 | |
| Emotion / Interest / Uniqueness / Vibe | 情绪 / 兴趣 / 独特性 / 氛围 | |
| question type (Yes-or-No / What / How / Why) | 是非题 / What 问句 / How 问句 / Why 问句 | |
| explicit response / ambiguous response | 显式回答 / 模糊回答 | GPT 辅助评测中的两类输出 |
| GPT-assisted evaluation strategy | GPT 辅助评测策略 | |
| text-to-score | 文本转分数 | |
| Relevance / Precision / Completeness | 相关性 / 精确性 / 完整性 | 阐释评测三维度 |
| subjective experiment | 主观实验 | |
| test fatigue | 测试疲劳 | |
| ground truth / golden annotation | 真值 / 黄金标注 | |
| accuracy rate | 准确率 | |
| random guess | 随机猜测 | |
| hallucination | 幻觉 | |
| three-grade classification | 三档分类 | |
| scene classification model | 场景分类模型 | |
| Big-Five personality traits | 大五人格特质 | |

### 交叉验证记录

| id | 原文要点 | 译文 | 语义一致性 |
|---|---|---|---|
| b0007 | EAPD 含 2800 张图、覆盖 NI/AI/AGI、由三类美学专家标注 | 逐项对应，数字 2800 与三类专家身份原样保留 | 一致 |
| b0020 | 九个来源数据集、场景标签采样 2493 张、补 152 张高美学与 155 张低美学图像，合计 2800 | 全部数字（2493、152、155、2800）与数据集名原样保留 | 一致 |
| b0026 | 56 个场次 × 50 张图、8400 组问答对、2800 条阐释、每图三问一阐释、四个子集 | 逐项对应，数字未改动 | 一致 |
| b0039 | 输入提示模板、BLEU-4/CIDEr 不适用、显式/模糊回答、GPT 辅助评测 | 提示模板原文（含 A) Yes B) No 的中文对应）完整译出，指标名保留 | 一致 |
| b0068 | Q-Instruct 最优、最高准确率仅 52.86%、GPT-4V 次优 50.86%、NI>AI>AGI | 全部数值与模型名原样保留 | 一致 |

### 一致性与数字核查

- 术语统一性已用 Grep 复核：图像美学感知、美学共情、美学阐释、专家标注美学感知数据库、自然／艺术／人工智能生成图像、GPT 辅助评测策略等译法全文唯一。
- 全部数字原样保留：2800、8400、2493、152、155、56×50、32 位专家、30 张疲劳阈值、15 个 MLLM、52.86%、50.86%、[0, 2] 区间、大五人格等均未改动；模型名（GPT-4V、Gemini Pro Vision、Q-Instruct、ShareGPT4V、mPLUG-Owl2 等）与数据集名（AADB、PARA、TAD66K、BAID、CAD、ArtEmis、DiffusionDB、AGIQA-1K/3K 等）全部保留原文。
- 占位符核查：本文 SLOT 编号 1、2、3（分别位于 b0013–b0015 段首，对应贡献编号标记），译文中原样保留。脚本校验 `stray=0`、`missing=0`。
- 编码核查：`zh.json` 与 `index.html` 中不含 `�`（U+FFFD），脚本 `mojibake=0`。

### 遗留问题

- 无。图片文件齐全（`missing_img=0`）。

## 复核记录（第二轮交叉验证）

- 复核人：独立复核 Agent 08 号
- 抽查方式：`sample_blocks.py` 两轮随机抽样（种子 8 与 2024）+ 全量脚本化交叉校验（数字/公式占位符/未译块/长度比）
- 抽查块（共 12 块次）：b0010, b0044, b0013, b0008, b0058, b0028 / b0012, b0006, b0011, b0036, b0033, b0009
- 结论：共记录 1 条核验事项，逐条判定如下。

| 块 ID | 问题类型 | 复核发现 | 判定与处理 |
|---|---|---|---|
| b0013, b0020, b0026 等 | 数字一致性复核 | 脚本检出 EN「2,800 / 8,400 / 2,493」在 ZH 中写作「2800 / 8400 / 2493」 | 仅千位分隔符写法差异，数值一致，未修改。 |

- 其中标注「未修改」者为经核对后确认**非错误**（中文语序换位、等值数字改写、规范要求的英文专名保留），按规格书 §2「避免过度修改」不予改动。
- 重跑 `build_index.py`：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
