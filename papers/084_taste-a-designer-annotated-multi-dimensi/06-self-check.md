# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 181（文本 159 / 原子 22）|
| 已译文本块 | 159 / 159 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 280 · 已还原 280 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 646 |
| `<img>` 元素 | 5 |
| `<table>` 元素 | 16 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| text-to-image (T2I) | 文本到图像（T2I） | 全文统一，未写作「文生图」 |
| preference dataset | 偏好数据集 | 全文统一 |
| sub-dimension / criterion | 子维度 / 准则 | 前者强调分解结构，后者强调评分项 |
| designer panel / cohort | 设计师小组 / 队列 | rater panel 与 cohort 分别固定 |
| annotator / evaluator / rater | 标注者 / 评测者 / 评分者 | 按原文用词区分，同一角色不混译 |
| pairwise comparison | 成对比较 | 全文统一 |
| 4-way ranking | 四路排序 | 指四个生成器输出的完整排序 |
| Kendall's τ | Kendall ⟦SLOT⟧（τ） | 统计量名不译，符号原样 |
| majority-vote probability | 多数投票概率 | 全文统一 |
| Condorcet cycle | Condorcet 环 | 专名保留 |
| triadic intransitivity | 三元非传递性 | 与 Condorcet 环配套 |
| iid-uniform null | iid 均匀零假设 | 全文统一 |
| leave-one-out (LOO) ceiling | 留一（LOO）上限 | 全文统一 |
| reward model | 奖励模型 | 标准译法 |
| preference head | 偏好头 | 模块化 MLP 打分头 |
| scalar head / pairwise-difference head | 标量头 / 成对差分头 | 两种架构对照 |
| frozen backbone / encoder | 冻结骨干 / 编码器 | 全文统一 |
| Bradley–Terry (BT) loss | Bradley–Terry（BT）损失 | 专名保留 |
| position bias | 位置偏差 | 全文统一 |
| order-consistent verdict | 顺序一致的判定 | 与 MT-Bench S1 协议配套 |
| macro agreement / macro accuracy | 宏一致率 / 宏准确率 | 分别对应 agreement 与 accuracy |
| hallucination flag | 幻觉标记 | No / Minor / Major 三类 |
| ordinal distance metric | 序数距离度量 | Krippendorff α 所用度量 |
| bootstrap | bootstrap | 保留不译 |
| reference anchor | 参考锚点 | 跨域对照数据集 |
| gof test (chi-squared) | 卡方拟合优度检验 | 标准译法 |
| Monte Carlo | 蒙特卡洛 | 标准译法 |
| intransitive triple | 非传递三元组 | 与环率配套 |
| split bucket (3-2 split) | 分裂桶（3-2 分裂） | 投票分桶口径 |
| uninam / majority / split | 一致 / 多数 / 分裂 | 5-0、4-1、3-2 三档 |
| soft label | 软标签 | 全文统一 |
| criterion-conditioned prompt (CCP) | 准则条件化提示（CCP） | 附录与表 6 配套 |
| mean opinion score | 平均意见分 | AIGC 质量评估术语 |
| visual hierarchy | 视觉层级 | 全文统一 |
| color harmony | 色彩和谐 | 全文统一 |
| typography | 字体排版 | 全文统一，未写作「排版」 |
| spatial accuracy | 空间准确性 | 全文统一 |
| description fidelity | 描述保真度 | 全文统一 |

### 交叉验证记录

| 块 id | 原文要点 | 我的译文 | 一致性确认 |
|---|---|---|---|
| b0008 | 98,807 之外的 TASTE 数字：三项诊断、三个参考锚点、「字体排版与空间准确性的信号约为色彩和谐的两倍」 | 逐项照译，含 ⟦SLOT_0⟧–⟦SLOT_2⟧ | 语义一致，无增补 |
| b0033 | 九个子维度、两个队列、每子维度 80 条提示、两个 Typography 准则的区别 | 完整译出四项美学子准则与三项描述保真度子准则，80 条提示原样保留 | 数字与分类完全对应 |
| b0064 | Kendall τ 的三种取值情形：完全一致 / 随机 / 系统性相左 | 三种情形逐条对应 ⟦SLOT_40⟧、⟦SLOT_41⟧、⟦SLOT_42⟧ | 占位符顺序与原文一致 |
| b0132 | 逐桶准确率：5-0 / 4-1 / 3-2 三档及 ⟦SLOT_199⟧–⟦SLOT_211⟧ | 十三个占位符按原编号原顺序保留 | 数字与占位符均无遗漏 |
| b0155 | 三个锚点的子采样规模：Sushi、MovieLens、HPSv2（9 生成 + 1 COCO 真实） | 逐项照译，含 ⟦SLOT_263⟧–⟦SLOT_270⟧ | 与 §5 的描述一致 |

### 一致性与数字核查

- 术语统一性：已用 Grep 核查「成对比较」「四路排序」「位置偏差」「留一上限」「偏好头」「描述保真度」等核心术语，全文译法唯一；rater / evaluator / annotator 按原文语境分别固定为「评分者 / 评测者 / 标注者」，未混用。
- 数字核查：1,600 / 80 / 10 / 5 / 4 / 6 / 9 / 1.55M / 12k / 918k / 63 / 1.5M / 20 / 2 / 90 / 13 / 16 / 4-10 / 400 / 100 / 50 / 20,000 / 24,000 / 4,320 / 640K / 0.741 / 0.767 / 0.78 / 0.55 / 0.500 / 4.4 / 4.3 等全部与原文一致；表 1–表 11 为 keep 块，未作改动。
- 占位符完整性：原文 280 个 `⟦SLOT_n⟧` 全部按原编号、原顺序保留，构建后 stray = 0。
- 编码检查：`zh.json` 与 `index.html` 均不含 U+FFFD。

### 遗留问题

- 原文 b0012 中的「TASTE11 1」与 b0123 中的「22 2」疑为 LaTeX 脚注标记在抽取时残留的重复数字，译文按原文原样保留，未作删改。
- 原文 b0155 的措辞与 §5（b0069–b0072）在锚点规模描述上略有出入（例如 MovieLens 的评分区间），译文按各自段落原文照译，未做跨段统一。
- 无图片缺失，无原文乱码。

## 复核记录（第二轮交叉验证）

抽查块：b0033、b0067、b0093、b0171、b0163、b0110


- **发现问题数**：0
- **已修正数**：0

判定依据：逐块对照 EN/ZH，完整性（无漏译跳句）、准确性（方法名/指标名/因果关系/否定/数量均无误）、
数字与符号（数值、百分比、模型名、数据集名、指标名原样一致）、公式占位符（`⟦SLOT_n⟧` 编号与数量
一致，随其指称成分一并移位属正常）、术语一致性、中文质量（通顺、无生造词、无明显 AI 腔）六项均未
见实质错误。另经全量脚本核查：占位符集合一致、无缺失译文块。

结构核验：MathJax 已加载；图片均为 `figures/` 本地相对路径、无 http 外链；无 U+FFFD；
顶部含中文标题与中文摘要；底部含「返回总目录」链接。重跑 `build_index.py` 后
`missing / stray / mojibake / missing_img` 四项均为 0。
