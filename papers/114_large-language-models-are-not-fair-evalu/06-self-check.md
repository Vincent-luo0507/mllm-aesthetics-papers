# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 130（文本 69 / 原子 61）|
| 已译文本块 | 69 / 69 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 90 · 已还原 90 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 201 |
| `<img>` 元素 | 2 |
| `<table>` 元素 | 8 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| Large Language Model (LLM) | 大语言模型（LLM） | 首现附缩写 |
| evaluator / referee | 评估者 | 全文统一，不混用"评判者" |
| LLM-as-evaluator paradigm | 以 LLM 为评估者的范式 | |
| positional bias | 位置偏差 | 本文核心概念 |
| candidate response | 候选回复 | |
| win/tie/lose | 胜/平/负 | 人工标注的三类结果 |
| win rate | 胜率 | |
| Conflict Rate | 冲突率 | 交换位置后结论矛盾的比例 |
| Multiple Evidence Calibration (MEC) | 多证据校准（MEC） | 首现附缩写 |
| Balanced Position Calibration (BPC) | 均衡位置校准（BPC） | 同上 |
| Human-in-the-Loop Calibration (HITLC) | 人在回路校准（HITLC） | 同上 |
| Evidence Calibration (EC) | 证据校准（EC） | MEC 的单次版本 |
| Balanced Position Diversity Entropy (BPDE) | 均衡位置多样性熵（BPDE） | 首现附英文全称 |
| Vanilla Diversity Entropy | Vanilla 多样性熵 | 基线名保留 Vanilla |
| Vanilla evaluation method | Vanilla 评估方法 | 先前工作的原始方法 |
| scoring / comparing template | Scoring / Comparing 评估模板 | 模板名保留英文 |
| auto-regressive model | 自回归模型 | |
| ensemble | 集成 | 指多次采样结果合并 |
| sampling temperature | 采样温度 | |
| kappa correlation coefficient | kappa 相关系数 | 统计量名保留 |
| indicator function | 指示函数 | |
| hyper-parameter | 超参数 | |
| majority opinion | 多数意见 | 三位标注者的投票规则 |
| annotator | 标注者 | |
| n-gram metric | n 元组指标 | |
| Vicuna Benchmark | Vicuna 基准 | 基准名保留 |
| Assistant 1 / Assistant 2 | Assistant 1 / Assistant 2 | 模板角色名保留 |
| placeholder / slot | 占位符 / 插槽 | 模板组件，两词各有对应 |
| entropy | 熵 | |
| perturbation | 扰动 | |

### 交叉验证记录

| 块 id | 原文要点 | 译文要点 | 一致性 |
|---|---|---|---|
| b0009 | GPT-4 偏爱第一个候选、ChatGPT 偏爱第二个，交换顺序即可逆转结果 | 两种偏好方向与"交换顺序可逆转结论"的表述均一致，无添加解释 | 一致 |
| b0019 | 三占位符 ⟦SLOT_6⟧；对问题 ⟦SLOT_7⟧ 与回复 ⟦SLOT_8⟧、⟦SLOT_9⟧ 构成提示 ⟦SLOT_10⟧ | 五个槽位按原文顺序嵌入，位置偏差的定义（两次查询产生矛盾）未改动 | 一致 |
| b0026 | 指示函数 ⟦SLOT_19⟧；GPT-4 冲突率 46.3% 与 5.0%，ChatGPT 82.5% 与 52.5% | 四个百分比与槽位对应，结论「更强模型受影响更小」一致 | 一致 |
| b0042 | BPC 构造提示 ⟦SLOT_40⟧（交换 ⟦SLOT_41⟧ 中位置）；得到 ⟦SLOT_42⟧ 个分数 ⟦SLOT_43⟧/⟦SLOT_44⟧ 对应 ⟦SLOT_45⟧/⟦SLOT_46⟧；最终分为 ⟦SLOT_49⟧ 个分数的均值 | 十一个槽位按原文顺序出现，取平均的规则表述准确 | 一致 |
| b0061 | ⟦SLOT_59⟧ 个标注样本；准确率提升 14.3%；kappa 从 ⟦SLOT_62⟧ 到 ⟦SLOT_63⟧；20%（⟦SLOT_67⟧）人工协助把成本从 ⟦SLOT_68⟧ 降至 ⟦SLOT_69⟧ | 数字与槽位一一对应，脚注中最低时薪与 3 分钟/样本的换算未改动 | 一致 |

### 一致性与数字核查

- 术语：positional bias 统一为「位置偏差」，evaluator 统一为「评估者」，candidate response 统一为「候选回复」，三个校准策略缩写（MEC/BPC/HITLC）与 BPDE 全文写法一致。
- 数字与指标：46.3%、5.0%、82.5%、52.5%、14.3%、20%、80、66、3 分钟、100 次运行、1/3/5/7、6% 等均按原文字面保留；BLEU、ROUGE、BERTScore、BARTScore、kappa、Acc.、Kap.、C.R 等指标名与缩写未改写。
- 占位符：69 个文本块共 90 处 `⟦SLOT_n⟧`，生成前用脚本逐块比对槽位序列，全部一致；脚本校验残留为 0。
- 编码：zh.json 与 index.html 均不含 U+FFFD，脚本 mojibake 计数为 0。

### 遗留问题

- 无图片缺失（missing_img = 0），无不可解析块。
- 原文 b0061 为一个段落被 HTML 拆成两块，译文保持各自的截断位置，未做合并。
- b0061 脚注中「11 1 The minimum hourly wage...」的编号排版为原文 HTML 解析产物，译文照原样保留，未做重排。
- b0040、b0059 等处 k、t、N 等符号以公式槽位承载，中文仅描述其含义，符号由脚本还原。

## 复核记录（第二轮交叉验证）

- 复核人：Agent 02（独立复核，非译者）
- 结构核验：MathJax（`tex-mml-chtml.js`）已加载；2 处图片 `src` 全部为 `figures/` 本地相对路径，无 http 外链；无 U+FFFD；顶部中文标题与中文摘要齐备，底部有「返回总目录」链接。
- 抽查块：b0042、b0079、b0027、b0071、b0049、b0016（seed=2）；加抽 b0069、b0028、b0065、b0023（seed=7）
- 判定：上述全部抽查块在完整性（无漏译跳句）、准确性（无错译、无因果/否定/数量颠倒）、数字与符号（模型名/数据集名/指标名/百分数原样一致）、公式占位符（`⟦SLOT_n⟧` 集合与顺序全篇逐块机器比对一致）、术语一致性、中文通顺度六项上均通过，**抽查未发现实质错误，未作任何修改**。
- 构建产物校验：`index.html` 四项校验（missing / stray / mojibake / missing_img）均为 0，本次未改动 `zh.json`，未重跑构建。
