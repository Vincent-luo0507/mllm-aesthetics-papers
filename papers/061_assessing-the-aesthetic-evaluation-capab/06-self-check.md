# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 113（文本 81 / 原子 32）|
| 已译文本块 | 81 / 81 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 100 · 已还原 100 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 200 |
| `<img>` 元素 | 6 |
| `<table>` 元素 | 3 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| GPT-4 with Vision (GPT-4V) | GPT-4 with Vision（GPT-4V） | 模型名保留 |
| aesthetic evaluation | 审美评价 | 全文统一 |
| Generic Image Aesthetics Assessment (GIAA) | 通用图像美学评价（GIAA） | 预测群体均值 |
| Personalized Image Aesthetics Assessment (PIAA) | 个性化图像美学评价（PIAA） | 预测个体评分 |
| few-shot prompting / few-shot examples | 少样本提示 / 少样本示例 | — |
| prompt engineering | 提示工程 | — |
| system / user attribute prompt | 系统 / 用户属性提示 | API 消息角色 |
| persona | 角色设定 | 提示工程术语 |
| resolution mode (low / high) | 分辨率模式（低 / 高） | GPT-4V API 参数 |
| tokenized image | 经词元化的图像 | — |
| box-and-whisker plot | 箱线图 | — |
| quartile range | 四分位距 | — |
| outlier | 离群值 | — |
| 95% confidence interval | 95% 置信区间 | — |
| Welch's t-test | Welch t 检验 | 保留人名 |
| one-way ANOVA | 单因素方差分析 | — |
| significance level | 显著性水平 | — |
| p-value | p 值 | — |
| accuracy / precision / recall / f1-score | 正确率 / 精确率 / 召回率 / F1 分数 | 三类指标 |
| semantic pattern | 语义模式 | 10 类图像主题 |
| target-semantics / target-users | 目标语义类别 / 目标用户 | 本文术语 |
| chance level | 随机水平 | 三分类基线 |
| rule of thirds | 三分法 | 摄影构图技法 |
| low depth of field | 浅景深 | 摄影技法 |
| opposing colors | 对比色 | 摄影技法 |
| color wheel | 色环 | — |
| agent technology | 智能体技术 | 整合深度学习与 LLM |
| neuroaesthetics | 神经美学 | — |
| model-free / model-based | 无模型 / 基于模型 | 开发路径对比 |
| black box | 黑箱 | — |
| PARA / AVA | 同名保留 | 数据集名 |
| Fisher vector | Fisher 向量 | 传统图像特征 |
| content restriction policy | 内容限制策略 | GPT-4V 的图像拒绝策略 |

### 交叉验证记录

| 块 id | 原文要点 | 本文译文 | 一致性判断 |
|---|---|---|---|
| b0019 | PARA 含 438 名评分者对 31220 张图像的评价 | 两个数字原样保留 | 一致 |
| b0023 | 评分区间：>1.0 至 2.5 为低，>2.5 至 3.5 为中，>3.5 至 5.0 为高 | 三个区间与四个边界值原样保留 | 一致 |
| b0031 | 低分辨率 512×512；高分辨率先缩至 2048×2048 内、短边 768 | 三个尺寸数值原样保留 | 一致 |
| b0036 | 八项评价项目与三种摄影技法（三分法、浅景深、对比色） | 项目列表与技法解释照译，两个槽位 ⟦SLOT_6⟧、⟦SLOT_7⟧ 保留 | 一致 |
| b0085–b0086 | GIAA 与 PIAA 最佳条件下的正确率与随机水平，共六个槽位 ⟦SLOT_92⟧–⟦SLOT_98⟧ | 六个槽位原样保留，"四舍五入到小数点后第三位"照译 | 一致 |

### 一致性与数字核查

- 术语统一性：`aesthetic evaluation` 全文统一为"审美评价"；`GIAA`/`PIAA` 首次出现给出中文全称后保留缩写；`persona` 统一为"角色设定"；`accuracy` 统一为"正确率"，与 precision（精确率）、recall（召回率）严格区分。
- 数字核查：438、31220、10、6、1.0/2.5/3.5/5.0、5 个种子、512×512、2048×2048、768、95%、18 种模式、6 种角色设定、JPMJSP2108 等数值与编号均逐字核对，未做换算。
- 占位符核查：100 个 `⟦SLOT_n⟧` 槽位（SLOT_0–SLOT_99）在译文中数量与编号完全一致，构建脚本报告 stray = 0。
- 编码核查：`zh.json` 与 `index.html` 均不含 U+FFFD。
- 提示模板块（b0026、b0028、b0059、b0061、b0063、b0065、b0068）给出中文对应，同时保留 JSON 示例格式、花括号占位变量与 `####` 分隔符等格式标记，便于与左栏英文原文对照。

### 遗留问题

- 无图片缺失（missing_img = 0）。
- 原文 b0036 称"八个项目"却列出九项（构图、明暗、色彩、亮度、暗度、锐度、景深、情绪、创意），译文保留原文的"八个项目"并如实列出九项。
- 原文 b0069 的槽位顺序为"⟦SLOT_69⟧ 名用户中有 ⟦SLOT_70⟧ 名被排除"与常规语序不同，译文按槽位原顺序照译，未调换。
- 原文 b0034 "resolusion"、b0066 处 "mimimum""respectivly""evalution" 等拼写笔误，译文按语义处理，不影响内容。

## 复核记录（第二轮交叉验证）

- 抽查块（8 块，随机种子 7 与 42）：b0053、b0029、b0059、b0025、b0051、b0058、b0067、b0020
- 全篇自动化校验：逐块比对 EN/ZH 的 `⟦SLOT_n⟧` 占位符编号与顺序、数字/量级一致性，未发现丢失、错位或篡改。
- 抽查 8 块，未发现实质错误。
- 重跑 `build_index.py` 后四项校验：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
