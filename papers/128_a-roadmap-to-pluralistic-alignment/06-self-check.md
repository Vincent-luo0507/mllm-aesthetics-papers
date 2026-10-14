# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 315（文本 167 / 原子 148）|
| 已译文本块 | 167 / 167 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 129 · 已还原 129 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 260 |
| `<img>` 元素 | 2 |
| `<table>` 元素 | 8 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| pluralistic alignment | 多元对齐 | 本文核心议题，全文统一 |
| pluralism | 多元性 | 技术语境下统一译法 |
| Overton pluralism | Overton 多元性 | 三类之一 |
| steerable pluralism | 可引导多元性 | 三类之一 |
| distributional pluralism | 分布多元性 | 三类之一 |
| Overton window | Overton 窗口 | 合理回答的集合 |
| monistic | 一元（的） | 与 pluralistic 相对 |
| multi-objective benchmark | 多目标基准 | 三类多元基准之一 |
| trade-off steerable benchmark | 权衡可引导基准 | 三类之一 |
| jury-pluralistic benchmark | 陪审团多元基准 | 三类之一 |
| commensurating function | 通约函数 | 把多目标合并为单标量 |
| Pareto improvement | Pareto 改进 | 多目标比较概念 |
| welfare function / social welfare function | 福利函数／社会福利函数 | 陪审团效用聚合 |
| steering attribute | 引导属性 | 可引导多元性的条件 |
| faithfulness | 忠实度 | 属性专属评分 |
| reference population | 参照人群 | 分布多元性的目标 |
| Jensen-Shannon distance / divergence | Jensen-Shannon 距离／散度 | 分布比较指标 |
| KL-divergence | KL 散度 | 分布比较指标 |
| Wasserstein distance | Wasserstein 距离 | 分布比较指标 |
| tetrachoric correlation | 四分相关 | 硬指标之一 |
| reinforcement learning with human feedback (RLHF) | 基于人类反馈的强化学习（RLHF） | 当前主流对齐技术 |
| controllable decoding | 可控解码 | 推理时引导方法 |
| model soups | model soups（模型汤） | 推理时引导方法 |
| cross entropy | 交叉熵 | 语言建模目标 |
| bothsidesism / false balance | 两面主义／虚假平衡 | Overton 多元性的风险 |
| scalable oversight | 可扩展监督 | 应用场景 |
| algorithmic monoculture | 算法单一化 | 支持多元性的论据 |
| hypervolume indicator | 超体积指标 | 相关概念 |
| expected utility metric | 期望效用指标 | 相关概念 |
| max-min / Rawlsian objective | 最大最小／罗尔斯式目标 | 福利函数变体 |
| tyranny of the majority | 多数暴政 | 福利函数风险 |
| Machine Personality Inventory (MPI) | 机器人格量表（MPI） | 实验数据集 |

### 交叉验证记录

| 块 id | 原文要点 | 译文要点 | 一致性 |
|---|---|---|---|
| b0008 | 三种多元性定义与三类多元基准，含各节交叉引用（§3.1–3.3、§4.1–4.3） | 三类定义与三类基准逐项对应，节号原样保留 | 一致 |
| b0028 | Overton 窗口定义，含 SLOT_8 与脚注 1 对政治学概念的说明 | 槽位与脚注内容完整保留（脚注以括号形式标注） | 一致 |
| b0062 | 分布多元模型定义（10），含 SLOT_42–SLOT_47 六个槽位 | 六个槽位顺序与数量完全对应 | 一致 |
| b0129 | 实验设计：LLaMA(2)/Gemma/GPT-3、GlobalOpinionQA 与 MPI、120 题、日本与美国、JS 距离 .26、5 个提示，含脚注 3–5 | 模型名、数据集名、数字与脚注均原样保留 | 一致 |
| b0302 | 附录 A.1 进一步分析，含 SLOT_116–SLOT_121 六个槽位与脚注 8 | 六个槽位顺序与数量对应，脚注内容完整 | 一致 |

### 一致性与数字核查

- 术语统一：以 Grep 核对 zh.json，全文统一使用「多元对齐」「多元性」「Overton 多元性」「可引导多元性」「分布多元性」「通约函数」「陪审团多元基准」「Pareto 改进」等译法，未出现同义轮换；哲学语境中的「政治多元主义／价值多元主义」与技术语境中的「多元性」作了明确区分。
- 数字核查：20 条形式化定义编号（1）–（20）、120 道 MPI 问题、5 个提示、JS 距离 .26、FA8650-23-C-7316、N00014-24-1-2207、IHS018186 等编号与数值均与原文一致；SLOT_111–SLOT_128 中的样本量与国家数均按原样保留为占位符。
- 占位符完整性：脚本自校验 `⟦SLOT⟧` 残留为 0；另用脚本逐块比对原文与译文的 `⟦SLOT_n⟧` 序列，167 个文本块全部完全一致（含顺序）。
- 编码检查：zh.json 与 index.html 均不含 U+FFFD，脚本 mojibake 计数为 0。

### 遗留问题

- 无图片缺失（missing_img = 0）。
- 原文脚注（第 1–9、11 号）在提取时与主文本混排，译文以括号形式就地标注脚注内容，未改动原文信息。
- b0304 原文有一句完全重复的陈述（关于 LLaMA 与 LLaMA2 差距翻倍的说明），为忠实对应原文，译文保留了重复，未作删并。
- b0312 提到「表 11」而 b0314 的表题标注为「表 5」，两处均按原样保留，未擅自统一。

## 复核记录（第二轮交叉验证）

抽查块：b0102、b0098、b0137、b0148、b0112、b0297


- **发现问题数**：0
- **已修正数**：0

判定依据：逐块对照 EN/ZH，完整性（无漏译跳句）、准确性（方法名/指标名/因果关系/否定/数量均无误）、
数字与符号（数值、百分比、模型名、数据集名、指标名原样一致）、公式占位符（`⟦SLOT_n⟧` 编号与数量
一致，随其指称成分一并移位属正常）、术语一致性、中文质量（通顺、无生造词、无明显 AI 腔）六项均未
见实质错误。另经全量脚本核查：占位符集合一致、无缺失译文块。

结构核验：MathJax 已加载；图片均为 `figures/` 本地相对路径、无 http 外链；无 U+FFFD；
顶部含中文标题与中文摘要；底部含「返回总目录」链接。重跑 `build_index.py` 后
`missing / stray / mojibake / missing_img` 四项均为 0。
