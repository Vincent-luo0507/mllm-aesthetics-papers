# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 207（文本 138 / 原子 69）|
| 已译文本块 | 138 / 138 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 73 · 已还原 73 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 166 |
| `<img>` 元素 | 8 |
| `<table>` 元素 | 17 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| compositional reasoning | 组合推理 | 全文统一，未写作「组合性推理」 |
| physically grounded reasoning | 物理定位推理 | 论文核心概念，与语义推理相对 |
| semantic compositional reasoning | 语义组合推理 | 与前一条配套 |
| counterfactual example / pair | 反事实样本 / 反事实对 | 全文统一 |
| data curation | 数据策划 | 全文统一，未写作「数据整理」 |
| large multimodal model (LMM) | 大型多模态模型（LMM） | 首次出现括注缩写 |
| contrastive model | 对比式模型 | 与 generative model 相对 |
| generative model | 生成式模型 | 全文统一 |
| negative image / negative caption | 负样本图像 / 负样本字幕 | 全文统一，未写作「负例」 |
| positive image-caption pair | 正样本图像-字幕对 | 全文统一 |
| hard negative | 难负样本 | 全文统一 |
| grouping | 分组 | 论文提出的批构造策略，首现括注 Grouping |
| grounded image generation | 定位图像生成 | 指带边界框条件的生成 |
| image inpainting | 图像修复 | 全文统一 |
| object removal | 物体移除 | 与 inpainting 对照 |
| positional understanding | 位置理解 | 全文统一 |
| object counting | 物体计数 | 全文统一 |
| bounding box | 边界框 | 标准译法 |
| entity / objectified caption | 实体 / 实体化字幕 | 附录 A 中的方括号标注格式 |
| visual question answering (VQA) | 视觉问答 | 标准译法 |
| zero-shot | 零样本 | 全文统一 |
| next-token prediction loss | 下一词元预测损失 | 标准译法 |
| contrastive loss | 对比损失 | 标准译法 |
| cross-entropy loss | 交叉熵损失 | 标准译法 |
| cosine similarity | 余弦相似度 | 标准译法 |
| similarity matrix | 相似矩阵 | 标准译法 |
| mixed precision | 混合精度 | 标准译法 |
| weight decay | 权重衰减 | 标准译法 |
| ablation study | 消融研究 | 标准译法 |
| train-test split | 训练-测试划分 | 全文统一 |
| text score | 文本分数 | Winoground 评测项 |
| retrieval precision | 检索精确率 | 表 6 指标 |
| SOTA | SOTA | 保留不译 |
| vanilla model | 原始模型 | 指未经微调的基座模型 |
| prompt engineering | 提示工程 | 标准译法 |
| overfitting | 过拟合 | 标准译法 |
| downstream task | 下游任务 | 标准译法 |
| swap / add / replace | 交换 / 添加 / 替换 | SugarCrepe 三大类别 |

### 交叉验证记录

| 块 id | 原文要点 | 我的译文 | 一致性确认 |
|---|---|---|---|
| b0013 | CLIP 提升 33%+、LLaVA 提升 37%+，用水平翻转与 GLIGEN | 两个百分比原样保留，方法描述逐项对应 | 数字一致，无增补 |
| b0041 | 边界框公式说明：每个类别至多一个实例、每对物体 ⟦SLOT_5⟧ | 六个占位符按原编号原顺序保留 | 占位符与语义均一致 |
| b0071 | 各数据集的学习率与批大小：1e-5/256/5、2e-6/16/1、2.56e-5/1024、50 与 15 轮、5e-5 | 全部超参数原样保留 | 数字与配置项无遗漏 |
| b0098 | 随机抽取 300 张 DALLE-3 图像，一致性分数 84.67% | 数字原样保留 | 数字一致 |
| b0173 | 附录 A 的 GPT-4V 输出格式示例，含方括号实体标签与 JSON 结构 | 实体标签、编号与 JSON 键名原样保留，仅叙述文字译为中文 | 结构完整，未改动格式 |

### 一致性与数字核查

- 术语统一性：已用 Grep 核查「组合推理」「负样本图像」「负样本字幕」「物理定位推理」「反事实」「数据策划」等核心术语，全文译法唯一；caption 一律译为「字幕」，未与「描述」混用。
- 数字核查：33%+ / 37%+ / 96% / 94.17% / 10% / 4:1 / 0.5 / 300 / 84.67% / 1e-5 / 2e-6 / 2.56e-5 / 5e-5 / 256 / 16 / 1024 / 5 / 1 / 50 / 15 / 0.9 / 0.98 / 0.2 / 2.5k / 10 万 / 246 / 500+ / 1000+ / 1 与 4 块 A100 80GB 等全部与原文一致；表 1–表 12 为 keep 块，未作改动。
- 占位符完整性：原文 73 个 `⟦SLOT_n⟧` 全部按原编号、原顺序保留，构建后 stray = 0。
- 编码检查：`zh.json` 与 `index.html` 均不含 U+FFFD。

### 遗留问题

- 原文 b0010 中的「11 1」疑为 LaTeX 脚注标记抽取时残留的重复数字，译文按原文原样保留。
- 原文 b0024 的组合推理示例写作「blank pants and white shorts」与「white pants and blank shorts」，疑为 black 的笔误，译文保留原文英文字符串未作修正。
- 原文 b0039 与 b0041 被边界框公式（keep 块）截断为同一句的两半，译文按块边界分别成段，公式两侧的语序已在中文内部保持连贯。
- 附录 A（b0161–b0173）为直接投给 GPT-4V 的英文提示模板，按要求译为中文，但方括号实体标签（如 [/EN#1/people …]）、JSON 键名与示例英文原句均原样保留。
- 无图片缺失，无原文乱码。

## 复核记录（第二轮交叉验证）

抽查块：b0076、b0068、b0082、b0071、b0022、b0053


- **发现问题数**：0
- **已修正数**：0

判定依据：逐块对照 EN/ZH，完整性（无漏译跳句）、准确性（方法名/指标名/因果关系/否定/数量均无误）、
数字与符号（数值、百分比、模型名、数据集名、指标名原样一致）、公式占位符（`⟦SLOT_n⟧` 编号与数量
一致，随其指称成分一并移位属正常）、术语一致性、中文质量（通顺、无生造词、无明显 AI 腔）六项均未
见实质错误。另经全量脚本核查：占位符集合一致、无缺失译文块。

结构核验：MathJax 已加载；图片均为 `figures/` 本地相对路径、无 http 外链；无 U+FFFD；
顶部含中文标题与中文摘要；底部含「返回总目录」链接。重跑 `build_index.py` 后
`missing / stray / mojibake / missing_img` 四项均为 0。
