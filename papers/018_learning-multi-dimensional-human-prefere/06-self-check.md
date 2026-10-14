# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 120（文本 77 / 原子 43）|
| 已译文本块 | 77 / 77 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 67 · 已还原 67 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 152 |
| `<img>` 元素 | 5 |
| `<table>` 元素 | 9 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| text-to-image (generation) | 文本到图像（生成） | 全文统一，不简称“文生图” |
| Multi-dimensional Human Preference (MHP) | 多维人类偏好（MHP） | 数据集名，首次出现附英文缩写 |
| Multi-dimensional Preference Score (MPS) | 多维偏好分数（MPS） | 评分模型名 |
| preference condition | 偏好条件 | 指美学/细节/对齐等打分维度条件 |
| condition mask | 条件掩码 | 由提示词-条件相似度得到的注意力掩码 |
| semantic alignment | 语义对齐 | 与 text-image consistency 同义时统一为该译法 |
| detail quality / detail quantity | 细节质量 / 细节数量 | 原文两词并存，分别按字面译，未合并 |
| overall score / overall assessment | 总体分数 / 总体评估 | 评分维度与句子表述分别处理 |
| aesthetics | 美学 | 评分维度名 |
| prompt | 提示词 | 全文统一，不写作“提示”“Prompt” |
| annotator / quality inspector | 标注员 / 质检员 | 标注流程角色 |
| cross-attention (CA) | 交叉注意力 | 模块名 |
| vision-language model (VLM) | 视觉-语言模型 | |
| long-tail distribution | 长尾分布 | |
| preference accuracy | 偏好准确率 | 评价指标名 |
| latent diffusion model (LDM) | 潜扩散模型 | |
| auto-regressive model | 自回归模型 | |
| generative adversarial network (GAN) | 生成对抗网络 | |
| latent space | 潜空间 | |
| token | 词元 | 统一用“词元”，不用“令牌” |
| ablation study | 消融实验 | |
| Grad-CAM | Grad-CAM | 方法名保留 |
| CLIP Score / Aesthetic score | CLIP Score / Aesthetic score | 指标名保留英文 |
| Inception Score (IS) | Inception Score（IS） | |
| Fréchet Inception Distance (FID) | Fréchet Inception Distance（FID） | |
| KL divergence | KL 散度 | |
| pairwise comparison | 图像对（比较） | 依语境译为“图像对” |
| warmup | 预热 | |
| crowdsourced team | 众包团队 | |
| PickScore / ImageReward / HPS / HPS v2 / HPD | 保留原名 | 模型与数据集名不译 |

### 交叉验证记录（随机抽 5 块）

| id | 原文要点 | 我的译文 | 一致性结论 |
|---|---|---|---|
| b0009 | MHP 在三方面领先；Diffusion DB 无偏好标注；KOLORS 提供 ⟦SLOT_0⟧10w 提示词 | 表 1：……MHP 数据集在提示词收集、图像生成与偏好标注三方面相较已有工作取得显著进展……KOLORS 是来自内部设计师平台的数据集，提供了 ⟦SLOT_0⟧10w 条提示词。 | 一致；数字 10w 原样保留，占位符 1 个保留 |
| b0034 | 从 3 个库收集提示词；初标 59,396 → 筛后 52,057；长尾分布 | 提示词采集自 PromptHero/DiffusionDB/KOLORS-dataset……初步收集 59,396 条……得到 52,057 条……呈长尾分布 | 一致；四个数字逐一核对无改动 |
| b0045 | 1–5 分归一化到 ⟦SLOT_4⟧；210 人团队，198 人参与，170 标注员 + 28 质检员；每组 3 人标注；20% 抽检 | 同上中文表述 | 一致；人数与百分比全部保留 |
| b0065 | CLIP-H 初始化；训练 30,000 步；batch 128；lr 3e-6；warmup 500 | 同上中文表述 | 一致；超参数原样 |
| b0078 | CLIP/Aesthetic 只在特定偏好好；偏好模型缺泛化；MPS 全维度一致；表 4 大幅领先 | 同上中文表述（含原文 ** * 脚注标记保留） | 一致；未添加任何原文没有的解释 |

### 一致性与数字核查

- 术语统一性：已用 Grep 检索 zh.json，确认「提示词」「偏好条件」「条件掩码」「语义对齐」「标注员」「潜空间」「词元」等核心术语全文译法唯一，未出现同义轮换；「细节质量」与「细节数量」按原文用词分别对应，未混用。
- 数字与指标：607,541 / 918,315 / 66,389 / 59,396 / 52,057 / 898,315 / 10,000 / 4,000 / 30,000 / 128 / 3e-6 / 500 / 20% / 80% / 0-7 / 1-5 / 0.5 等全部逐位核对，未改写；IS、FID、CLIP Score、Aesthetic score、KL 散度、R 值、准确率（%）均保留原记法。
- 占位符完整性：脚本式校验逐块比对 `⟦SLOT_n⟧` 序列，77 个文本块的占位符数量与顺序与原文完全一致（mismatch 列表为空）；构建脚本 stray=0。
- 编码检查：zh.json 与 index.html 均不含 U+FFFD 乱码字符，文件为 UTF-8。

### 遗留问题

1. 原文 5.2 节小标题 “Multinational Preference accuracy.” 与该段内容（多维偏好）不符，应为 multi-dimensional 的笔误；译文按语境译为「多维偏好准确率」，未改动原意。
2. 原文 b0084 “our HPS attends to…” 疑为 MPS 的笔误，为忠实原文仍译为「我们的 HPS」，未擅自更正。
3. b0078 中残留的 `** *` 脚注标记与 b0086 中的 `†† †` 标记属原文本身排版残留，译文原样保留其位置。
4. 图片缺失数 0，figures/ 下资源齐全，无遗留下载问题。

## 复核记录（第二轮交叉验证）

抽查块：b0092、b0071、b0022、b0028、b0032、b0013


- **发现问题数**：0
- **已修正数**：0

判定依据：逐块对照 EN/ZH，完整性（无漏译跳句）、准确性（方法名/指标名/因果关系/否定/数量均无误）、
数字与符号（数值、百分比、模型名、数据集名、指标名原样一致）、公式占位符（`⟦SLOT_n⟧` 编号与数量
一致，随其指称成分一并移位属正常）、术语一致性、中文质量（通顺、无生造词、无明显 AI 腔）六项均未
见实质错误。另经全量脚本核查：占位符集合一致、无缺失译文块。

结构核验：MathJax 已加载；图片均为 `figures/` 本地相对路径、无 http 外链；无 U+FFFD；
顶部含中文标题与中文摘要；底部含「返回总目录」链接。重跑 `build_index.py` 后
`missing / stray / mojibake / missing_img` 四项均为 0。
