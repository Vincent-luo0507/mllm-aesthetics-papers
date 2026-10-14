# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 307（文本 233 / 原子 74）|
| 已译文本块 | 233 / 233 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 35 · 已还原 35 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 167 |
| `<img>` 元素 | 13 |
| `<table>` 元素 | 17 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| text-to-image synthesis / generation | 文本到图像生成 | 正文首次用全称，后文用“文生图” |
| human preference | 人类偏好 | 全文统一 |
| preference prediction model | 偏好预测模型 | HPS v2 的角色 |
| pairwise comparison | 两两比较 | HPD v2 的标注单位 |
| annotator / labeler | 标注者 / 标注员 | 团队 57 人 |
| checker | 质检员 | 7 名，负责交叉复核 |
| inter-annotator agreement | 标注者间一致性 | 表 4、图 4、图 5 |
| prompt | 提示词 | 全文统一 |
| style word | 风格词 | 需由 ChatGPT 去除 |
| conflict prompt | 冲突提示词 | 风格词自相矛盾 |
| NSFW score | NSFW 分数 | 阈值 0.4 |
| image-text alignment | 图文对齐 | 标注两大因素之一 |
| visual attractiveness | 视觉吸引力 | 标注另一因素 |
| vision-language model (VLM) | 视觉语言模型（VLM） | CLIP 所属类别 |
| fine-tune | 微调 | 在 HPD v2 上微调 CLIP |
| cosine similarity | 余弦相似度 | CLIP 的对齐度量 |
| temperature scalar | 温度标量 | CLIP 学习所得 |
| KL-divergence | KL 散度 | 训练目标 |
| AdamW | AdamW | 优化器，保留原文 |
| weight decay | 权重衰减 | 0.35 |
| cosine learning rate schedule | 余弦学习率调度 | 预热 500 步后 |
| Bayesian optimization | 贝叶斯优化 | 超参数确定方式 |
| ViT-H/14 / OpenCLIP / LAION-2B | ViT-H/14 / OpenCLIP / LAION-2B | 模型与数据名保留 |
| Inception Score (IS) | Inception Score（IS） | 保留缩写 |
| Fréchet Inception Distance (FID) | 弗雷歇 inception 距离（FID） | 首次括注 |
| LPIPS / HYPE | LPIPS / HYPE | 感知相似度指标 |
| aesthetic score | 美学分数 | 对照指标 |
| benchmark | 基准 | 第 5 节 |
| test-time trick | 测试时技巧 | 噪声与先验图像混合 |
| latent feature | 潜特征 | 检索初始化 |
| noise schedule | 噪声调度 | 训练与推理不一致 |
| DDIM sampler / DPM Solver | DDIM 采样器 / DPM Solver | 保留原名 |
| guidance scale | 引导尺度 | 7.5 等 |
| datasheet | 数据说明书 | 附录 H |
| visual Turing test | 视觉图灵测试 | Fake2M |

### 交叉验证记录

| 块 id | 原文要点 | 本文译文 | 一致性 |
|---|---|---|---|
| b0007 | 两类偏差（图像来源、提示词风格词），798k 比较，9 个模型 + COCO，ChatGPT 去风格词 | 两类偏差分述，数字与 9 个模型、COCO 引用保留 | 一致 |
| b0025 | DiffusionDB 中 15.0% 含“Greg Rutkowski”、28.5% 含“artstation”，表 1 第一条冲突示例 | 百分数与三个冲突短语原样保留 | 一致 |
| b0050 | 测试划分 400 组（300+100）、9 幅/组、10 位标注者、153,000 条；训练划分 107,515 组、4 幅/组、645,090 条、28,172 条 COCO 提示词 | 六个数字全部对应 | 一致 |
| b0065 | AdamW、4,000 步、学习率 SLOT、权重衰减 0.35、批大小 128、预热 500 步、图像编码器最后 20 层、文本编码器最后 11 层、贝叶斯优化 | 训练超参数完整，⟦SLOT_13⟧/⟦SLOT_14⟧ 顺序一致 | 一致 |
| b0153 | 图 8/图 9 的排序原则，含 ⟦SLOT_17⟧ ⟦SLOT_18⟧ 两个行内图像占位符 | 两个占位符各出现一次、位置与原文一致，提示词原文保留 | 一致 |

### 一致性与数字核查

- 术语：复核 zh.json，文本到图像生成、提示词、偏好预测模型、标注者、风格词、图文对齐、引导尺度等核心术语全文译法唯一，未出现同义轮换。
- 数字：798k、434k、433,760、789,090、107,515、645,090、153,000、28,172、3200、800、80、200、15.0%、28.5%、61%、57、50、7、10%、300、400、100、4,000、0.35、128、500、20、11、0.4、7.5、3.0、5.0、1000、5、25、6.0、0.1、50、27 等均未改动。
- 占位符：脚本逐块比对 `⟦SLOT_0⟧`–`⟦SLOT_34⟧` 共 35 处，修订 b0059、b0074 两处顺序后完全一致，stray=0。
- 编码：zh.json 与 index.html 均不含 U+FFFD。

### 遗留问题

- 无缺失图片（missing_img=0）。
- b0180 原文写作“表 12、表 12、表 12”，疑为 LaTeX 交叉引用错误（应为表 10–12），译文按原文逐字保留。
- b0153 原文图 8／图 9 中的图像引用被占位符替换后文字略显不顺（如“which is previously sampled from”），已按上下文补全语义，未改动占位符数量。
- b0141 中 ChatGPT 要求回复的英文词元（paintings、anime and cartoon 等）属程序输出标记，按原样保留。


## 复核记录（第二轮交叉验证）

- 复核人：独立复核团队 03 号 Agent
- 抽查块数：**12**（随机种子 3 取 6 块 + 种子 7 取 6 块）
- 抽查块 ID：`b0016`、`b0232`、`b0227`、`b0218`、`b0194`、`b0074`（种子 3）；`b0255`、`b0168`、`b0042`、`b0145`、`b0161`、`b0137`（种子 7）

### 结构核验

- `index.html` 含 `tex-mml-chtml.js`，MathJax 已加载。
- 图片 `src` 全部为 `figures/...` 本地相对路径，无 `http` 外链。
- 无 U+FFFD 乱码；顶部有中文标题与中文摘要，底部有「返回总目录」链接。
- 重跑 `build_index.py`：`missing`、`stray`、`mojibake`、`missing_img` 四项**全为 0**。

### 发现与修正

抽查 12 块，**未发现实质错误**（无漏译整句、无错译关键结论、数字与指标未被改动、`⟦SLOT_n⟧` 占位符编号与顺序完整、术语译法篇内统一）。

### 其他说明

- `b0031` 原文两处均写作 “Fig. 3”，但据本文题注，NSFW 分数分布直方图为**图 2**、风格词频次为**图 3**，译文分别译为“图 2”“图 3”，属对原文笔误的正确处理，予以保留。
- `b0153`/`b0154` 原文因抽取退化出现多个同名 “Fig. 8/Fig. 9”，译文改用“第一幅/第二幅”区分，语义完整且未丢信息。
