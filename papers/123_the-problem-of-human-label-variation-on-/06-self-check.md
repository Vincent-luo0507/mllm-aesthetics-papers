# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 147（文本 46 / 原子 101）|
| 已译文本块 | 46 / 46 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 4 · 已还原 4 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 26 |
| `<img>` 元素 | 6 |
| `<table>` 元素 | 1 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| human label variation (HLV) | 人类标注变异（HLV） | 全文核心术语，首次出现括注英文与缩写，其后统一用「人类标注变异」或 HLV |
| ground truth | 真值（ground truth） | 不译作「基准真相」，沿用 ML 惯例 |
| gold label / hard label | 金标签 / 硬标签 | 与 soft label 对举，二者分别固定 |
| aggregation | 聚合 | 指多数投票、概率聚合等把多标注压成单标签的操作 |
| majority vote | 多数投票 | |
| un-aggregated labels | 未聚合标签 | 指保留标注者级别、未合并的标签 |
| annotator | 标注者 | 全文统一，不混用「标注员」 |
| annotator disagreement | 标注者分歧 | 与「变异（variation）」在本篇中有明确区分 |
| disagreement | 分歧 | 与 variation 严格区分，不互换 |
| subjectivity | 主观性 | |
| hard cases | 困难样例 | |
| soft label / soft metrics | 软标签 / 软指标 | 与硬标签、准确率对举 |
| calibration | 校准 | 指模型置信度校准 |
| overconfidence | 过度自信 | |
| training dynamics | 训练动态 | |
| data maps | 数据地图（data maps） | Swayamdipta 等提出的专有说法 |
| active learning | 主动学习 | |
| human-computer interaction (HCI) | 人机交互（HCI） | |
| natural language inference (NLI) | 自然语言推理（NLI） | |
| perspectivism | 视角主义（perspectivism） | 原文拼写为 perspectivisim，按词义订正译出 |
| contested labels | 争议性标签 | HCI 文献用法 |
| regularization | 正则化 | |
| multi-task learning | 多任务学习 | |
| sequential fine-tuning | 序贯微调 | |
| crowd layer | 众包层（crowd layer） | Rodrigues 与 Pereira 的架构名 |
| data statements | 数据说明（data statements） | Bender 与 Friedman 的专有说法 |
| meta-data | 元数据 | |
| in-vitro / in-vivo evaluation | 实验室评测（in-vitro）/ 真实环境评测（in-vivo） | 全篇两处保持同一译法 |
| dual use | 双重用途 | 伦理声明中的常见表述 |
| position paper | 立场论文 | |

### 交叉验证记录

| 块 id | 原文要点 | 译文 | 一致性 |
|---|---|---|---|
| b0005 | NLP 进展依赖微调预训练模型；流程为 data/modeling/evaluation；每实例单一 gold label，由聚合（多数投票）得到 | 在自然语言处理（NLP）中，当下的多数进展由这样一种做法驱动……每个实例只取用单一的金标签（gold label）。该金标签由人类给出的标注聚合而成，例如多数投票。 | 一致。三个环节名词、gold label、多数投票均保留，未增删内容 |
| b0014 | 定义 HLV 为 plausible variation；偏好 variation 而非 disagreement；errors 源于注意力疏漏；聚合掩盖复杂性 | 我们将人类标注变异（HLV）定义为标注中合理的变异（见图 1）……聚合操作掩盖了现实世界的这种复杂性。 | 一致。「变异／分歧」的区分被准确传达 |
| b0017 | 综述 HLV 在 CV、HCI、NLP 中的不同名称；Pavlick 等发现至少 20% 数据存在合理变异；Alm（2011）提出可接受性比「对错」更有用 | HLV 在 CV 中已有研究，那里称之为人类不确定性（human uncertainty）……捕捉 HLV 而非全局多数，正与这一观点相合。 | 一致。「至少 20%」等数字原样保留，全部引用与年份未改 |
| b0025 | 两大方向：直接从未聚合标签学习、用 HLV 丰富金标签；列举 crowd layer、soft labels、代价敏感损失加权等 | 第二大阵营则致力于接纳人类标注变异，包含两个宽泛方向……或作为刻画逐实例人类标签分布的单一“软标签”辅助任务 Fornaciari 等（2021）。 | 一致。方法名与文献引用逐条对应 |
| b0038 | 软评测指标：交叉熵、熵相关性、KL／Jensen-Shannon 散度；以及按标注者一致性、聚类、难度等划分数据子集的做法 | ML、CV 与 NLP 的研究已开始推动硬标签与软标签评测……后者最近还为自然语言推理数据中的分歧建立了一套分类体系。 | 一致。Pearson、F1、KL、Jensen-Shannon 等指标名原样保留 |

### 一致性与数字核查

- **术语统一**：用 Grep 在 `zh.json` 中回查了「人类标注变异／HLV」「标注者」「未聚合标签」「金标签」「软标签」「校准」「困难样例」「视角主义」「实验室评测／真实环境评测」等词条，确认全文译法唯一，未出现同义轮换（例如未混用「标注员／标注者」「真值／基准真相」）。
- **数字与指标**：原文出现的 20%、SemEval 2021/2023、ERC Consolidator Grant DIALECT 101043235、图 1–3、表 1、第 2–4 节编号等全部原样保留；Pearson 相关系数、F1、KL、Jensen-Shannon、argmax 等指标名未作改动或翻译。
- **占位符**：`⟦SLOT_0⟧`–`⟦SLOT_3⟧` 共 4 个槽位在译文中逐个原样保留，未改写编号、未在占位符内插入文字；构建脚本还原计数为「总数 4 · 已还原 4」，残留 0。
- **编码**：`zh.json` 与 `index.html` 均不含 U+FFFD，脚本 `mojibake` 项为 0。
- **去 AI 味**：按 anti-ai-patterns 规则回扫，避免了「值得注意的是／毋庸置疑／众所周知」等空洞填充与句首模板，长句按中文习惯以分号、破折号断开。

### 遗留问题

- 块 `b0006`、`b0015`、`b0026` 的原文为 PDF 转换残留的 LaTeX 宏包源码（`@goptd@color`、`\HyColor@XZeroOneThreeFour`、`\pdfmark` 等）与屏幕阅读器注释，无可读正文。按规格书 §7 处理，译文写作「（原文此处为 LaTeX 排版宏与 PDF 屏幕阅读器注释源码，不可解析）」，并保留其中的 `⟦SLOT_0⟧`／`⟦SLOT_1⟧`／`⟦SLOT_2⟧` 占位符；这三处对应图 1、图 2、图 3 的辅助标注，图题本身（b0007、b0016、b0027）已正常翻译。
- 原文 `perspectivisim` 为拼写错误，按 `perspectivism` 译作「视角主义」，未改动原文。
- 图片文件齐全，`missing_img` 为 0，无图片缺失问题。


## 复核记录（第二轮交叉验证）

- 复核人：独立复核团队 09 号 Agent
- 抽查块（14 个）：`b0019`、`b0031`、`b0029`、`b0023`、`b0046`、`b0038`、`b0032`、`b0044`（种子 9）；`b0032`、`b0029`、`b0026`、`b0007`、`b0012`、`b0023`（种子 21）。另全量脚本比对 147 个块的占位符与数字。
- 结构核验：`tex-mml-chtml.js` 已加载；6 张图片 `src` 均为 `figures/` 本地相对路径，无 http 外链；无 U+FFFD；顶部中文标题／摘要、底部「返回总目录」均在。

### 发现并修正

| 块 ID | 问题类型 | 修正前 | 修正后 |
|---|---|---|---|
| `b0006` | 漏译整句（屏幕阅读器说明文字整体未译，仅标注「不可解析」） | （原文此处为 LaTeX 排版宏与 PDF 屏幕阅读器注释源码，不可解析）⟦SLOT_0⟧ | （原文此处为 LaTeX 排版宏与 PDF 注释源码，其中的屏幕阅读器说明文字为：人类标注变异与标注错误的示意图。标注中的不一致可能源于标注者真实的分歧、主观性，或仅仅因为两种（或多种）看法都成立。）⟦SLOT_0⟧ |
| `b0015` | 漏译整句（图 2 三个困难样例的说明文字整体未译） | （原文此处为 LaTeX 排版宏与 PDF 屏幕阅读器注释源码，不可解析）⟦SLOT_1⟧ | 同上处理，补入：该图展示了三个困难样例。样例 1：'This was an excellent offer and i didn't not enjoy it' 的情感是什么（正面、中性、负面）？样例 2：A 是否蕴含 B？'A: Paola drinks oat milk'、'B: Paolo drinks milk.'。样例 3：低分辨率图像，问题是它究竟是猫、狗还是其他动物。保留 ⟦SLOT_1⟧ |
| `b0026` | 漏译整句（图 3 柱状图说明文字整体未译） | （原文此处为 LaTeX 排版宏与 PDF 屏幕阅读器注释源码，不可解析）⟦SLOT_2⟧ | 同上处理，补入：该图是一幅柱状图，按年份统计发布未聚合标签的 NLP 论文数量，图中呈现上升趋势。保留 ⟦SLOT_2⟧ |

说明：三处原文虽为 PDF 转换残留的 LaTeX 宏（`\pdfmark`、`/F 768`、`/Ff 65536` 等），但其中的 `Screenreader caption` 是可读正文，属图 1／图 2／图 3 的辅助文字描述（图 2、图 3 的说明在图题 b0016、b0027 中并无对应内容），原处理方式造成实质信息缺失，故补译；宏源码本身仍不逐字翻译。

### 未修改项

- 其余抽查块（`b0019`、`b0029`、`b0031`、`b0032`、`b0038`、`b0044`、`b0046`、`b0007`、`b0012`、`b0023`）信息点覆盖完整，数字、引用年份、指标名（cross entropy、entropy correlation、KL、F1、Pearson）、资助号（ERC Consolidator Grant DIALECT 101043235）均与原样一致；无占位符丢失或错位；术语「人类标注变异／HLV」「分歧」「困难样例」全篇统一。
- `b0006`、`b0015`、`b0026` 中残留的 PDF 控件参数数字（768、65536、0）为宏源码，按规范不译。

### 复跑构建

`{"blocks": 147, "missing": 0, "math": 26, "img": 6, "table": 1, "stray": 0, "mojibake": 0, "missing_img": 0}` —— 四项校验（missing／stray／mojibake／missing_img）全为 0。
