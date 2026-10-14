# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 322（文本 220 / 原子 102）|
| 已译文本块 | 220 / 220 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 171 · 已还原 171 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 366 |
| `<img>` 元素 | 23 |
| `<table>` 元素 | 24 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| Human Preference Score v3 (HPSv3) | 人类偏好分数 v3（HPSv3） | 本文提出的评测指标，首次出现括注英文 |
| Human Preference Dataset v3 (HPDv3) | 人类偏好数据集 v3（HPDv3） | 本文发布的数据集 |
| wide-spectrum | 宽谱 | 指质量/来源谱系跨度大，全文统一 |
| text-to-image generation | 文本到图像生成 | 不写作「文生图」，保持术语稳定 |
| text-image pair | 文本-图像对 | 全文统一 |
| pairwise comparison | 成对比较 | 与 pairwise data「成对数据」配套 |
| human-centric metric | 以人为中心的指标 | |
| Vision-Language Model (VLM) | 视觉语言模型（VLM） | 首次出现括注，后文用中文 |
| backbone | 骨干网络 | |
| multilayer perceptron (MLP) | 多层感知机（MLP） | |
| uncertainty-aware ranking loss | 不确定性感知排序损失 | 核心贡献术语，全文唯一译法 |
| Chain-of-Human-Preference (CoHP) | 人类偏好链（CoHP） | |
| Chain-of-Thought (CoT) | 思维链（CoT） | |
| reward model | 奖励模型 | |
| Model-wise Preference | 模型级偏好 | CoHP 第一阶段 |
| Sample-wise Preference | 样本级偏好 | CoHP 第二阶段 |
| denoising strength | 去噪强度 | |
| annotator | 标注者 | 统一，不混用「标注人员」「评测人员」 |
| annotation convergence | 标注收敛度 | |
| inter-annotator agreement | 标注者间一致率 | |
| percent point (pp) | 百分点（pp） | 缩写 pp 原样保留 |
| aesthetic score / Aesthetic Predictor | 美学分数 / 美学预测器 | |
| upper quality bound | 质量上界 | |
| reward hacking | 奖励破解 | RL 语境固定译法 |
| golden model / golden image | 黄金模型 / 黄金图像 | |
| Bradley-Terry loss | Bradley-Terry 损失 | 人名与损失名保留原文 |
| RankNet | RankNet | 不译 |
| Diffusion Transformer / autoregressive model | 扩散 Transformer / 自回归模型 | |
| high-quality (HQI) / low-quality (LQI) image | 高质量（HQI）/ 低质量（LQI）图像 | 缩写原样保留 |
| prompt | 提示词 | 全文统一，不译作「提示」「提示符」 |

### 交叉验证记录

| 块 id | 原文要点 | 译文要点 | 一致性 |
|---|---|---|---|
| b0014 | HPDv3 含 1.08M 文本-图像对、1.17M 成对比较；加入 SOTA 自回归/扩散模型输出与互联网高质量真实图像 | 译文保留 108 万 / 117 万，并保留 HPDv3、JourneyDB 等专名 | 一致 |
| b0046 | 验证集由 N 位专业艺术家标注、收敛度阈值、主数据集每对由 N 至 N 名标注者评判 | 全部数字以 ⟦SLOT⟧ 占位符原样保留，语义与句序对应 | 一致 |
| b0092 | 训练用 N 百万成对样本、Qwen2VL-7B 骨干、N 轮、A800 GPU、学习率/批大小/分辨率 | 数值全部落在占位符内，模型名 Qwen2VL-7B、NVIDIA A800 未改 | 一致 |
| b0101 | PickScore 下降 N pp、MPS 下降 N pp、HPSv3 仅降 N pp | 三个百分点数字与比较对象均对应，无误译或调换 | 一致 |
| b0283 | DanceGRPO 实验：300 次迭代、SD1.4 基座、四个奖励模型的对比结论 | 迭代次数与模型名原样保留，四个模型名以 ⟦SLOT⟧ 保留 | 一致 |

### 一致性与数字核查

- 术语一致性：用 Grep 在 `zh.json` 中检索「提示词」「文本-图像对」「成对比较」「标注者」「不确定性感知排序损失」「视觉语言模型」「奖励模型」「奖励破解」「百分点」等核心术语，确认全文译法唯一，未出现同义轮换（例如「标注者」未与「标注员」混用，「文本到图像生成」未与「文生图」混用）。
- 数字与指标：所有数字、百分比、单位（GB、像素、k、M）、模型名（Qwen2VL-7B、CLIP、BLIP、SD3、FLUX.1-dev 等）、数据集名（HPDv2/HPDv3、JourneyDB、Pick-A-Pic、Unsplash）、指标名（Spearman、Kendall、KL 散度、FID 类）均原样保留，未做任何换算或改写；涉及数值的句子中数值均以 `⟦SLOT_n⟧` 占位符承载，未发生移位。
- 占位符完整性：脚本校验「内联公式/图片槽位 总数 171 · 已还原 171」，`⟦SLOT⟧` 残留为 0；写入前另用脚本逐块比对原文与译文的 `⟦SLOT_n⟧` 集合，无增减、无改号。
- 编码：`zh.json` 与 `index.html` 均不含 U+FFFD，脚本 mojibake 计数为 0。
- 不变量：表格、公式、代码块、参考文献（`t:"keep"`）一律未翻译；正文块一块对一块，未做合并或拆分。

### 遗留问题

- 补充材料中的 b0299、b0301、b0303 为 HPDv3 基准的提示词原文清单（共约 1.1 万字符）。这些内容是数据集样本本身，性质等同数据而非论述性文本，因此仅把类别名（Animals / Architecture / Arts / Characters / Design / Food / Natural Scenery / Plants / Products / Transportation / Science / Others）译为「中文（English）：」形式，具体提示词字符串保持英文原样，以免破坏其作为数据集样本的可检索性。已在译文中体现，非漏译。
- 原文 b0043 中「Midjourney 11 1」为脚注标记解析残留，译文按原文形式保留。
- 原文 b0206 末句「assessment of content and aesthetic qualities independent of image proportions」为残句，译文按语义补足为完整中文句，未增删实质信息。
- 无图片缺失（missing_img = 0）。

## 复核记录（第二轮交叉验证）

- 复核方式：`sample_blocks.py`（随机种子 4 与 11，各取 6／4 块）＋ 全文机检（缺译、未译、⟦SLOT_n⟧ 槽位一致性、数字、残留英文词、结构与编码）。
- 抽查块 ID（10 块）：b0005、b0037、b0278、b0287、b0272、b0295、b0300、b0105、b0053、b0246
- 结构核验：`index.html` 已加载 `tex-mml-chtml.js`；图片 `src` 全为 `figures/...` 本地相对路径、无 http 外链；无 U+FFFD；顶部中文标题与中文摘要、底部「返回总目录」链接均存在。
- 抽查 10 块，未发现实质错误：无漏译整句、无错译关键结论、数字／百分比／模型名／数据集名／指标名与原文一致、`⟦SLOT_n⟧` 槽位数量与编号一致（个别块内槽位顺序按中文语序调整，语义对应正确）、术语篇内统一。
- 已重跑 `build_index.py` 校验，输出 `missing`／`stray`／`mojibake`／`missing_img` 四项均为 0。
- 未改动项：保留英文的专有名词、参考文献、代码与提示词模板、表格数据（规范要求），例如章节标题中的缩写名与 `{...}` 占位模板均按原文保留。
