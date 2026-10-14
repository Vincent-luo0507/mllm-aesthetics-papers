# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 206（文本 102 / 原子 104）|
| 已译文本块 | 102 / 102 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 80 · 已还原 80 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 210 |
| `<img>` 元素 | 5 |
| `<table>` 元素 | 5 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| annotator | 标注者 | 全文统一 |
| annotation | 标注 | 与 label「标签」区分 |
| disagreement | 分歧 | 标注者之间的不一致 |
| majority vote | 多数投票 | 核心对照方法 |
| ground truth / gold label | 真值标签 / 金标签 | |
| multi-annotator model | 多标注者模型 | 本文方法总称 |
| multi-task / multi-label / ensemble | 多任务 / 多标签 / 集成 | 三种架构变体 |
| subjective task | 主观性任务 | |
| hate speech | 仇恨言论 | |
| online abuse / abusive language | 网络辱骂 / 辱骂性语言 | |
| affect | 情感 | 与 emotion「情绪」区分 |
| emotion | 情绪 | Ekman 六种情绪 |
| valence / arousal | 效价 / 唤醒度 | 情感维度 |
| prediction uncertainty | 预测不确定性 | |
| Monte Carlo dropout (MC dropout) | MC dropout | 首次出现写明「蒙特卡洛 dropout」 |
| Softmax probability | Softmax 概率 | 基线不确定性估计 |
| variance | 方差 | 度量不确定性与分歧 |
| classifier head / annotator head | 分类器头 / 标注者头 | 多任务架构中的结构 |
| fully-connected layer | 全连接层 | |
| precision / recall / F-score | 精确率 / 召回率 / F 分数 | 指标名统一 |
| stratified cross-validation | 分层交叉验证 | |
| early stopping | 早停 | |
| learning rate / epoch | 学习率 / 轮次 | |
| true positive / false positive | 真正例 / 假正例 | |
| false negative / true negative | 假负例 / 真负例 | |
| violin plot | 小提琴图 | |
| annotator pool | 标注者池 | |
| crowdsourcing | 众包 | |
| micro-averaged | 微平均 | |
| active learning | 主动学习 | 结论中提及 |

### 交叉验证记录

| 块 id | 原文要点 | 我的译文 | 一致性 |
|---|---|---|---|
| b0029 | 数据集 ⟦SLOT_0⟧、实例集 ⟦SLOT_1⟧、标注者集 ⟦SLOT_2⟧、标注矩阵 ⟦SLOT_3⟧、条目 ⟦SLOT_4⟧ 表示 ⟦SLOT_5⟧ 被 ⟦SLOT_6⟧ 赋的标签等 15 个符号 | 15 个占位符顺序与数量完全一致，定义逐项对应 | 一致 |
| b0043 | GHC：⟦SLOT_42⟧ = 27,665 条帖子；⟦SLOT_43⟧ = 18 位标注者；每实例标注数区间（⟦SLOT_44⟧、⟦SLOT_45⟧）；总标注数 ⟦SLOT_46⟧；每标注者实例数（⟦SLOT_47⟧、⟦SLOT_48⟧） | 七个占位符顺序一致，四个数值原样保留 | 一致 |
| b0053/b0054 | 集成 ⟦SLOT_61⟧=53.54 低于基线 ⟦SLOT_62⟧=57.32；多标签 ⟦SLOT_63⟧=56.94；多任务 ⟦SLOT_64⟧=59.49 显著高于基线 | 四个数值与对应关系原样保留，优劣方向未颠倒 | 一致 |
| b0087 | 全部 GHC 实例（⟦SLOT_76⟧）中有 1,945 个标签不一致；表 4 列号（第 6 列、第 4–5 列） | 占位符保留，1,945 与列号原样保留 | 一致 |
| b0094 | 真负例 ⟦SLOT_77⟧（不确定性）= 0.040；假正例 ⟦SLOT_78⟧（不确定性）= 0.199；真正例与假负例均值 0.140 与 0.141 | 两个占位符保留，四个数值原样保留 | 一致 |

### 一致性与数字核查

- 术语：Grep 复查「标注者」「分歧」「多数投票」「多标注者模型」「不确定性」「标注者头」等在 zh.json 中的用法，全文统一；「情感（affect）」与「情绪（emotion）」严格区分，未混用。
- 数字：27,665、18、43,410、5,427、5,426、82、53、1,000、100、29、1.6%、4.0%、1,945、57.94%、22.31%、12.19%、7.56%、54%/44%、0.25、0.049、0.170、0.040、0.199、0.140、0.141、0.86、0.47、0.53、0.6–0.7、53.54、57.32、56.94、59.49、63.20、63.2、768、5 折 ×5 轮、3 轮、1.4K、8K、6.1 与 5.2 分钟等数值全部逐项核对，未改动。
- 模型与数据集名（BERT-base、RoBERTa、GHC、GoEmotions、Gab.com、Ekman、Plutchik、MACE、Jigsaw、Crowdflower、HuggingFace、transformers v3.1、Adam）原样保留。
- 占位符：含 ⟦SLOT⟧ 的文本块共 24 个，逐块按出现顺序比对完全一致，脚本 stray=0。
- 未翻译对象：参考文献、公式、表格、图片均按 `t:"keep"` 跳过。

### 遗留问题

- 原文存在若干拼写瑕疵（"GHC experiments are conducted with a learning rates of"、"stratifed"、"as it require training"、"textual features that causes disagreement"、"al-ternation"），译文按正确语义处理，未加注释，也未改动源文件。
- b0034 中脚注标记"11 1"属原文转换产物，译文照原样保留。
- 图片引用全部命中，missing_img=0，无缺失图片。

## 复核记录（第二轮交叉验证）

- 复核人：独立复核团队 03 号 Agent
- 抽查块数：**12**（随机种子 3 取 6 块 + 种子 7 取 6 块）
- 抽查块 ID：`b0083`、`b0111`、`b0067`、`b0047`、`b0102`、`b0008`（种子 3）；`b0038`、`b0030`、`b0100`、`b0094`、`b0112`、`b0025`（种子 7）

### 结构核验

- `index.html` 含 `tex-mml-chtml.js`，MathJax 已加载。
- 图片 `src` 全部为 `figures/...` 本地相对路径，无 `http` 外链。
- 无 U+FFFD 乱码；顶部有中文标题与中文摘要，底部有「返回总目录」链接。
- 重跑 `build_index.py`：`missing`、`stray`、`mojibake`、`missing_img` 四项**全为 0**。

### 发现与修正

抽查 12 块，**未发现实质错误**（无漏译整句、无错译关键结论、数字与指标未被改动、`⟦SLOT_n⟧` 占位符编号与顺序完整、术语译法篇内统一）。
