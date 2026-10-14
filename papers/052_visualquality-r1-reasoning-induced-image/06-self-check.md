# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 162（文本 80 / 原子 82）|
| 已译文本块 | 80 / 80 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 74 · 已还原 74 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 160 |
| `<img>` 元素 | 6 |
| `<table>` 元素 | 26 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| image quality assessment (IQA) | 图像质量评价（IQA） | 首次出现括注缩写 |
| no-reference IQA (NR-IQA) | 无参考图像质量评价（NR-IQA） | 与 FR（全参考）对照 |
| full-reference (FR) | 全参考（FR） | |
| vision-language model (VLM) | 视觉语言模型（VLM） | |
| supervised fine-tuning (SFT) | 监督微调（SFT） | |
| reinforcement learning (RL) | 强化学习（RL） | |
| reinforcement learning to rank (RL2R) | 强化学习排序（RL2R） | 本文方法名，首次出现括注 |
| group relative policy optimization (GRPO) | 组相对策略优化（GRPO） | |
| Thurstone model | Thurstone 模型 | 保留人名 |
| Thurstone Case V | Thurstone Case V | 保留原写法 |
| comparative probability | 比较概率 | 含"非对称比较概率" |
| fidelity measure / loss / reward | 保真度度量 / 损失 / 奖励 | fidelity 统一译"保真度" |
| mean opinion score (MOS) | 平均意见分（MOS） | |
| perceptual scale realignment | 感知尺度重对齐 | |
| reasoning-induced | 推理驱动 | 全文统一，未轮换 |
| catastrophic forgetting | 灾难性遗忘 | |
| reward hacking | 奖励破解 | |
| policy / reference policy | 策略 / 参考策略 | |
| advantage | 优势 | RL 术语 |
| clipping threshold | 截断阈值 | |
| minibatch | 小批量 | |
| sample variance | 样本方差 | |
| standard deviation (std) | 标准差（std） | |
| zero-shot | 零样本 | |
| test-time scaling | 测试时扩展 | |
| distortion | 失真 | |
| artifact | 伪影 | |
| gMAD (group maximum differentiation) | 组最大差异化（gMAD） | |
| Kullback–Leibler (KL) divergence | KL 散度 | |
| earth mover's distance | 推土机距离 | 首次出现括注英文 |
| SRCC / PLCC | SRCC / PLCC | 指标名保留 |

### 交叉验证记录（抽样 5 块）

| id | 原文要点 | 我的译文 | 语义一致性 |
|---|---|---|---|
| b0010 | 用 GRPO 为一对图像的每张图导出多个分数；按 Thurstone 模型用均值差除以样本方差算比较概率；奖励用连续保真度度量 | 三层设计（多分数导出、Thurstone 比较概率、连续保真度奖励）逐条译出，SLOT 占位符按序保留 | 一致，无漏译 |
| b0027 | 高斯 CDF；均值与方差；小常数防除零；与以往固定方差为一不同，显式用 GRPO 导出的样本方差 | 式 (1) 引用与四项说明完整，未改动任何数学含义 | 一致 |
| b0049 | 骨干 Qwen2.5-VL-7B；AdamW 初始学习率；每提示 6 个候选回答；A100 卡数、每卡小批量 8、epoch 数、约 5 小时 | 数字 6、8、5（小时）与卡数、epoch 均由 SLOT 承载或原样保留，未作换算 | 一致，数字核对无误 |
| b0055 | 多数据集训练无需感知尺度重对齐；平均 SRCC/PLCC 从 X 升至 Y；Q-Insight† 因感知尺度差异未获益；KADID-10K 与 SPAQ 的 MOS 范围不同 | 两个数据集的评分区间、脚注中 MOS 线性重标定说明均完整保留 | 一致 |
| b0082 | 四项局限：测试时扩展导致慢/贵/耗显存且错误累积；固定提示；仅 NR 设定；可扩展到其他感知任务 | 四点逐条对应，扩展任务（美学评价、年龄估计、感知相似性排序）全部保留 | 一致，未添油加醋 |

### 一致性与数字核查

- 术语一致性：全文统一"图像质量评价（IQA）""无参考（NR）""推理驱动""保真度度量/奖励""比较概率""感知尺度重对齐""小批量"。模型名（VisualQuality-R1、Q-Insight、Q-Align、DeQA-Score、Compare2Score、DepictQA、LIQE、MUSIQ、MANIQA、UNIQUE、NIQE、BRISQUE、Qwen2.5-VL-7B、DeepSeek-R1、SwinIR）与数据集名（KADID-10K、SPAQ、BID、CLIVE、KonIQ-10k、Liu13、SRIQA-Bench、Min19、AGIQA-3K）全部原样保留；算法名（GRPO、RL2R、RankNet、AdamW）与指标名（SRCC、PLCC、MOS）未译。
- 数字核查：学习率、候选回答数（6）、每卡小批量（8）、epoch 数、训练时长（约 5 小时）、SLOT_50 的 SRCC 值、MOS 区间、分数范围等均由 SLOT 占位符或原文数字承载，未作任何换算、四舍五入或单位改写。
- 占位符完整性：80 个文本块的 `⟦SLOT_n⟧` 集合与原文逐块比对，零差异；构建脚本 stray = 0。
- 编码检查：`zh.json` 与 `index.html` 中均不含 U+FFFD。

### 遗留问题

- 无图片缺失（`missing_img = 0`），6 张 `<img>` 均指向已下载的 `figures/` 本地文件。
- b0008 与 b0055 含 PDF 抽取残留的脚注标记（`11 1 ...`、`22 2 ...`），已按原文位置内联保留，未单独拆块。
- b0038 原文以 "The second KL divergence term is approximated by" 结尾，公式本身在后续原子块中，译文同样以"由"字收尾，与原文断句一致。
- b0025 中"为 ⟦SLOT_15⟧ 与 ⟦SLOT_16⟧ 生成 ⟦SLOT_14⟧ 个质量预测"，原文未明确是否"各生成"；译文按上下文（成对比较）处理为两张图像各自生成，与图 2 说明一致。

## 复核记录（第二轮交叉验证）

- 复核 Agent：06 号（独立交叉验证）
- 结构核验：MathJax（`tex-mml-chtml.js`）已加载；图片 `src` 全部为 `figures/...` 本地相对路径、无 http 外链；全文无 U+FFFD 乱码；顶部有中文标题与中文摘要，底部有「返回总目录」链接 —— 全部通过。
- 抽查块（10 块）：b0063、b0020、b0018、b0157、b0153、b0149、b0060、b0079、b0007、b0016
- 逐块比对 EN/ZH 的六项判读：完整性（无漏译整句/跳句）、准确性（无错译、无因果或否定反转）、数字与符号（数字、百分比、模型名、数据集名、指标名与原样一致）、公式占位符（`⟦SLOT_n⟧` 编号与顺序完全一致）、术语一致性（同篇内译法统一）、中文质量（通顺、无生造词、无 AI 腔堆砌）—— **未发现实质错误**。
- 附加机器校验：全篇文本块无缺失译文；每块占位符数量与顺序逐一比对一致；数字差分扫描命中的差异经人工核对均为中英数量表达差异（如 `4.8 million` → 「480 万」、`7.6B` → 「76 亿」、`10,073` → 「10,073」），非错译。
- 已修正：无（未改动 `zh.json`）。
- 重跑 `build_index.py` 四项校验：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
