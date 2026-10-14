# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 207（文本 146 / 原子 61）|
| 已译文本块 | 146 / 146 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 122 · 已还原 122 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 347 |
| `<img>` 元素 | 6 |
| `<table>` 元素 | 15 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| LLM-as-a-Judge | LLM 作为评判者（LLM-as-a-Judge） | 首次括注，后文用「LLM 评判者」 |
| position bias | 位置偏差 | 全文统一，不作「位置偏见」 |
| pairwise comparison | 成对比较 | 两候选比较 |
| list-wise comparison | 列表式比较 | 三候选及以上 |
| repetition stability (RS) | 重复稳定性 | 本文提出的指标 |
| position consistency (PC) | 位置一致性 | 沿用前人的指标 |
| preference fairness (PF) | 偏好公平性 | 本文提出的指标 |
| primacy / recency | 首位偏好 / 末位偏好 | 首次括注 primacy / recency |
| Judge-Level / Candidate-Level / Task-Level | 评判者层面 / 候选层面 / 任务层面 | 三层因素分类 |
| familial property | 家族属性 | 按模型系列分组的属性 |
| answer quality gap | 答案质量差距 | 候选层面核心因素 |
| win rate | 胜率 | 度量答案质量差距的载体 |
| overall win rate | 总体胜率 | 含平局折算 |
| consistent wins | 一致胜出 | 所有排列下同一胜者 |
| consistent ties | 一致平局 | 无确定胜者 |
| inconsistent judgment series | 不一致判断序列 | 置换后胜者不同 |
| bidirectional stepwise regression | 双向逐步回归 | 变量选择方法 |
| Akaike Information Criterion (AIC) | 赤池信息准则（AIC） | 首次括注 |
| forward selection / backward elimination | 前向选择 / 后向剔除 | 逐步回归的两个方向 |
| mutual agreement | 相互一致率 | 两评判者间一致的实例比例 |
| disagreement | 分歧度 | 偏离多数意见的判断数 |
| majority voting | 多数投票 | 提升判断可靠性的策略 |
| double-blind setting | 双盲设置 | 实验设置 |
| option mode | 选项模式 | 二选项/三选项模式 |
| permutation | 排列 | 列表式比较中顺序置换 |
| swap / swapped prompt | 交换（提示） | 成对比较中位置互换 |
| post hoc | 事后 | 分析在判断收集之后进行 |
| context window | 上下文窗口 | |
| baseline | 基线 | vicuna-13b-v1.3 / human |
| judgment series | 判断序列 | |

### 交叉验证记录

| 块 id | 原文要点 | 我的译文 | 一致性 |
|---|---|---|---|
| b0014 | 成对比较与双盲；交换提示构成判断对；首因选 ⟦SLOT_0⟧ 或近因选 ⟦SLOT_1⟧；二选项 A/B 与三选项含 C | 两个占位符原样保留；A/B/C 标签与选项模式描述完整 | 一致 |
| b0036 | 总体胜率 ⟦SLOT_35⟧ 定义式 ⟦SLOT_36⟧，⟦SLOT_37⟧ 个候选、⟦SLOT_38⟧ 个判断序列；质量差距 ⟦SLOT_39⟧=⟦SLOT_40⟧，⟦SLOT_41⟧ 为全平局期望基线；一致胜率 ⟦SLOT_42⟧、⟦SLOT_43⟧、⟦SLOT_44⟧ | 十个占位符顺序与数量完全一致，公式与文字对应关系未改动 | 一致 |
| b0041 | 每任务 3 问 × 4 候选 × 3 次重复 → MTBench 576、DevBench 432；温度=1；位置一致性与偏好公平性实例数 4,800 与 2,240；总计超 100,000 | 全部数值原样保留，温度与实例数未改动 | 一致 |
| b0140 | 15 个评判者下 MTBench 最大分歧度 10（5{A}-5{B}-5{C}）；DevBench 剔除 Gemini-1.5-flash 后 14 个评判者最大分歧度 7（7{A}-7{B}） | 数值与括号内的选择分布模式均原样保留 | 一致 |
| b0165 | AIC 变化 ⟦SLOT_114⟧；⟦SLOT_115⟧ 为增删后 AIC，⟦SLOT_116⟧ 为当前模型 AIC；若 ⟦SLOT_117⟧ 则模型被改进 | 四个占位符顺序一致，条件句语义对应 | 一致 |

### 一致性与数字核查

- 术语：Grep 复查「位置偏差」「位置一致性」「偏好公平性」「重复稳定性」「答案质量差距」「首位偏好」「末位偏好」等在 zh.json 中的用法，全文统一；「LLM-as-a-Judge」仅在首次出现时括注，后文统一用「LLM 评判者」。
- 数字：15 个评判者（12 闭源 + 3 开源）、22 个任务、约 40 个生成模型、150,000 个评测实例、576/432、4,800/2,240、100,000、30 与 10 个候选、8 与 14 个任务、10 与 8 个问题、0.85、0.95、93.44%→97.03%、70%/85%、40%、75%、80%、2%、5%、95%、3,000 美元、温度 1 等数值全部逐项核对，未改动。
- 模型与基准名（GPT-4、GPT-4-Turbo、GPT-4o、GPT-3.5-Turbo、o1-mini、Claude-3-Opus、Claude-3-Sonnet、Claude-3.5-Sonnet、Gemini-1.5-pro、Gemini-1.5-flash、Llama-3.1-8B、Llama-3.3-70B、Llama-405B、vicuna-13b-v1.3、MTBench、DevBench、PORTIA）原样保留。
- 占位符：含 ⟦SLOT⟧ 的文本块共 38 个，逐块按出现顺序比对完全一致，脚本 stray=0；全篇共 122 个占位符全部落在译文对应位置。
- 未翻译对象：参考文献、公式、表格、图片、模型清单（b0188、b0189）与任务清单（b0193、b0194）中的英文专名均原样保留。

### 遗留问题

- 原文存在若干拼写瑕疵（"From an exploratory perspectives"、"Tabel 2"、"gerenal metrics"、"positon bias"、"signficantly"、"major-ing voting"、"does not strong agree"），译文按正确语义处理，未加注释，也未改动源文件。
- 附录 C.2 中 MTBench 最大分歧度为 10、DevBench 为 7 的表述与选项模式（三选项 / 二选项）对应，译文保留了原文的对应关系，未做修正。
- 图片引用全部命中，missing_img=0，无缺失图片。

## 复核记录（第二轮交叉验证）

- 复核人：独立复核团队 03 号 Agent
- 抽查块数：**12**（随机种子 3 取 6 块 + 种子 7 取 6 块）
- 抽查块 ID：`b0163`、`b0033`、`b0192`、`b0135`、`b0117`、`b0039`（种子 3）；`b0133`、`b0056`、`b0042`、`b0153`、`b0033`、`b0035`（种子 7）

### 结构核验

- `index.html` 含 `tex-mml-chtml.js`，MathJax 已加载。
- 图片 `src` 全部为 `figures/...` 本地相对路径，无 `http` 外链。
- 无 U+FFFD 乱码；顶部有中文标题与中文摘要，底部有「返回总目录」链接。
- 重跑 `build_index.py`：`missing`、`stray`、`mojibake`、`missing_img` 四项**全为 0**。

### 发现与修正

抽查 12 块，**未发现实质错误**（无漏译整句、无错译关键结论、数字与指标未被改动、`⟦SLOT_n⟧` 占位符编号与顺序完整、术语译法篇内统一）。

### 其他说明

- `b0132` “3-option” 与 `b0140` 的 “2-option”、最大分歧度 10（5{A}-5{B}-5{C}）与 7（7{A}-7{B}）均译写正确，计数关系无误。
