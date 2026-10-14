# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 260（文本 155 / 原子 105）|
| 已译文本块 | 155 / 155 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 65 · 已还原 65 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 161 |
| `<img>` 元素 | 19 |
| `<table>` 元素 | 20 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| instruction-guided image editing | 指令引导的图像编辑 | 全文统一 |
| reward model | 奖励模型 | |
| human-aligned | 与人类对齐 | 不译作「人类对齐的」作形容词堆砌 |
| preference pair | 偏好对 | |
| preference dataset | 偏好数据集 | |
| VLM-as-a-judge | 以视觉语言模型为裁判 | 方法类别名 |
| Vision-Language Model (VLM) | 视觉语言模型 | 首次括注缩写 |
| Multi-Layer Perceptron (MLP) | 多层感知机 | |
| reward head | 奖励头 | |
| backbone | 骨干 | |
| multi-task learning (MTL) | 多任务学习 | |
| instruction following (IF) | 指令遵循 | 评分维度，缩写 IF |
| visual quality (VQ) | 视觉质量 | 评分维度，缩写 VQ |
| Likert scale | 李克特量表 | |
| rubric | 评分细则 | |
| inter-annotator agreement (IAA) | 标注者间一致性 | |
| Krippendorff's Alpha | Krippendorff's Alpha | 指标名，希腊字母符号以槽位保留 |
| Fleiss' Kappa | Fleiss' Kappa | 指标名不译 |
| tie / tie pair | 平局／平局对 | 偏好标注中两者无优劣 |
| tie disentanglement | 平局解耦 | |
| aggregation strategy | 聚合策略 | |
| uncertainty-aware | 不确定性感知 | |
| Gaussian distribution | 高斯分布 | |
| negative log-likelihood | 负对数似然 | |
| multi-way preference | 多路偏好 | |
| ternary / quaternary tuple | 三元／四元元组 | |
| out-of-distribution (OOD) | 分布外 | |
| data curation | 数据整理 | |
| held-out | 留出 | |
| Spearman rank correlation | 斯皮尔曼秩相关 | |
| mean squared error (MSE) | 均方误差 | |
| test-time scaling | 测试时扩展 | |
| post-training | 后训练 | |
| positional bias | 位置偏置 | |
| failure mode | 失败模式 | |
| ablation study | 消融实验 | |
| signal-to-noise ratio | 信噪比 | |

### 交叉验证记录

| 块 id | 原文要点 | 我的译文 | 一致性确认 |
|---|---|---|---|
| b0008 | GenAI-Bench 65.72 vs GPT-5 59.61；AURORA 63.62 vs GPT-4o 50.81；ImagenHub 35.20；Top 20K；GEdit-Bench 6.7→7.1 | 数字与基准名逐项对应，未增删 | 一致 |
| b0014 | 9557 对；六来源 606/737/1053/1250/5611/300；六模型生成 12 候选、抽 7；4 点李克特；IF/VQ；K-Alpha 槽位 ⟦SLOT_0⟧–⟦SLOT_4⟧ | 数字与槽位完全对应 | 一致 |
| b0046 | BTT 模型；平局对 ⟦SLOT_40⟧ 分解为 ⟦SLOT_41⟧/⟦SLOT_42⟧；式 6 | 槽位与因果逻辑一致 | 一致 |
| b0066 | Top 20K G_O 7.086 优于 6.444 与 6.780；Top 10K 6.938；Top 30K 6.962；Doubao 6.983 | 五个数值原样保留 | 一致，未换算 |
| b0253 | 失败模式 1：对鲜艳度的感知偏见，继承自 VLM 预训练 | 同上 | 一致，未添加评论 |

### 一致性与数字核查

- 术语：全文统一「指令引导的图像编辑／奖励模型／偏好对／指令遵循／视觉质量／评分细则／标注者间一致性／分布外／数据整理」，未做同义轮换；EditReward、EditReward-Data、EditReward-Bench、GenAI-Bench、AURORA-Bench、ImagenHub、GEdit-Bench、ShareGPT-4o-Image、Step1X-Edit、Qwen2.5-VL、MiMo-VL、HPSv3、BTT、MTL、IAA、OOD 等系统名与缩写一律原样保留。
- 占位符：逐块比对 `t:"text"` 块中 `⟦SLOT_n⟧` 集合与译文槽位集合，数量与编号完全一致（覆盖 ⟦SLOT_0⟧–⟦SLOT_64⟧）。
- 数字：200K、9557、9,557、606、737、1,053、1,250、5,611、300、12、7、4 点量表、65.72、59.61、63.62、50.81、35.20、36.18、38.42、38.02、37.81、28.31、40.48、63.97、49.62、60.17、59.50、46,000、20K、7.086、6.444、6.780、6.938、6.962、6.983、253、185、55.28、50.16、5.11、130k/200k、32.45→36.18、62.24→63.97、51.36→53.33、2.61 GPU 小时、0.25 秒/样本、8 卡 A800、0.05 预热比例 等均原样保留。
- 编码：`zh.json` 与 `index.html` 均不含 U+FFFD。
- 表格、公式、图片与参考文献块一律未翻译。

### 遗留问题

- 无图片缺失（`missing_img` 为 0）。
- 原文 b0196 与 b0258 中分别出现「In Figure x」与「Failure Mode Examplex 2」，疑为排版遗留占位符，译文按原文直述为「在图 x 中」与「失败模式示例 2」，未擅自补全图号。
- 附录 A.9 的输入提示模板以 SVG（b0207–b0209）形式存在，属不译块，未处理。

## 复核记录（第二轮交叉验证）

- 复核方式：`sample_blocks.py`（随机种子 4 与 11，各取 6／4 块）＋ 全文机检（缺译、未译、⟦SLOT_n⟧ 槽位一致性、数字、残留英文词、结构与编码）。
- 抽查块 ID（10 块）：b0070、b0176、b0078、b0084、b0181、b0231、b0008、b0185、b0256、b0174
- 结构核验：`index.html` 已加载 `tex-mml-chtml.js`；图片 `src` 全为 `figures/...` 本地相对路径、无 http 外链；无 U+FFFD；顶部中文标题与中文摘要、底部「返回总目录」链接均存在。
- 抽查 10 块，未发现实质错误：无漏译整句、无错译关键结论、数字／百分比／模型名／数据集名／指标名与原文一致、`⟦SLOT_n⟧` 槽位数量与编号一致（个别块内槽位顺序按中文语序调整，语义对应正确）、术语篇内统一。
- 已重跑 `build_index.py` 校验，输出 `missing`／`stray`／`mojibake`／`missing_img` 四项均为 0。
- 未改动项：保留英文的专有名词、参考文献、代码与提示词模板、表格数据（规范要求），例如章节标题中的缩写名与 `{...}` 占位模板均按原文保留。
