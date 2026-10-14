# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 297（文本 206 / 原子 91）|
| 已译文本块 | 206 / 206 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 48 · 已还原 48 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 188 |
| `<img>` 元素 | 11 |
| `<table>` 元素 | 16 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| Multi-modality Large Language Model (MLLM) | 多模态大语言模型（MLLM） | 全文统一 |
| low-level vision | 底层视觉 | 与 high-level（高层）相对 |
| low-level attribute | 底层属性 | 颜色、光照、构图、风格等 |
| Image Quality Assessment (IQA) | 图像质量评价（IQA） | — |
| Mean Opinion Score (MOS) | 平均意见分数（MOS） | 人类主观评分 |
| distortion | 失真 | 模糊、噪声、伪影等 |
| in-the-wild | 真实场景（自然实拍） | 与人工失真、生成式相对 |
| artificially distorted | 人工失真 | — |
| CGI / AIGC | 同名保留 | 生成式图像来源 |
| LLVisionQA | 同名保留 | 感知基准数据集 |
| LLDescribe | 同名保留 | 描述基准数据集 |
| golden description | 黄金描述 | 专家标注的参考描述 |
| completeness / preciseness / relevance | 完整性 / 精确性 / 相关性 | 描述评估三维度 |
| Yes-or-No / What / How questions | 是非型 / What 型 / How 型问题 | 三种问题类型 |
| global perception | 全局感知 | 与局部上下文感知相对 |
| local in-context perception | 局部上下文感知 | — |
| quadrant | 象限 | 两条轴划分的四个关注点象限 |
| softmax pooling | softmax 池化 | 核心评价策略 |
| logits | logits（未归一化对数概率） | 保留英文术语 |
| argmax | argmax | 基线策略，保留 |
| perplexity | 困惑度 | Kosmos-2 闭集推理依据 |
| close-set inference | 闭集推理 | — |
| prompt failure | 提示失效 | Kosmos-2 的失效模式 |
| de-biased accuracy | 去偏准确率 | 是非型问题的公平比较 |
| synonym ensemble | 同义词集成 | IQA 增强策略 |
| SRCC / PLCC | 斯皮尔曼秩相关系数 / 皮尔逊线性相关系数 | IQA 指标，缩写保留 |
| Junior-level / Senior-level Human | 初级人类 / 资深人类 | 人类对照水平 |
| dev / test subset | 开发集 / 测试集 | — |
| random guess | 随机猜测 | 基线正确率 |
| radar chart / bar chart | 雷达图 / 柱状图 | — |
| k-means clustering | k 均值聚类 | 多样性验证 |
| Q-Former | Q-Former | 视觉—语言对齐模块，保留 |
| cross-attention | 交叉注意力 | — |

### 交叉验证记录

| 块 id | 原文要点 | 本文译文 | 一致性判断 |
|---|---|---|---|
| b0035 | 黄金标准：是⟦SLOT_0⟧失真；否⟦SLOT_1⟧其他 | 两槽位原样保留，分类标准照译 | 一致 |
| b0059 | 直接指令下 good 78%、poor 20%；数值指令下 5 占 84%、1 占 9%、3 占 5%，2 与 4 均不足 1% | 六个百分比原样保留 | 一致 |
| b0168 | 三个候选答案的困惑度损失 7.43 / 7.56 / 7.92，六个槽位 ⟦SLOT_12⟧–⟦SLOT_17⟧ | 数值与槽位全部保留，✓/✗ 符号保留 | 一致 |
| b0229 | Flan-T5-XL 最高频词元为 high（89%）与 low（8%），三槽位 ⟦SLOT_25⟧–⟦SLOT_27⟧ | 百分比与槽位原样保留 | 一致 |
| b0286 | 前五方法上同义词集成平均最高提升 2%（平均 1.3%） | 两个数值原样保留 | 一致 |

### 一致性与数字核查

- 术语统一性：`low-level` 全文统一为"底层"，未混用"低层"；`distortion` 统一为"失真"；`golden description` 统一为"黄金描述"；`completeness/preciseness/relevance` 统一为"完整性/精确性/相关性"；`A1/A2/A3` 统一为"能力 1/2/3"并在括号中保留原记号。
- 数字核查：2,990、499、10、7、15、1,000、40%、62%、38%、60%、+9%、8%、20%、0.8/2.0、86%、10%、93.2%、98.4%、1.3%、2%、3,000、50/100 等数值与百分比均逐字核对，未做换算。
- 占位符核查：48 个 `⟦SLOT_n⟧` 槽位在译文中数量与编号完全一致，构建脚本报告 stray = 0。
- 编码核查：`zh.json` 与 `index.html` 均不含 U+FFFD。
- 提示模板与示例块（b0044、b0163、b0166、b0168、b0175、b0176、b0204、b0208、b0209 等）在译文中给出中文对应，同时保留 [IMAGE_TOKEN]、#用户/#系统、选项标号与格式标记，便于与左栏英文原文对照。

### 遗留问题

- 无图片缺失（missing_img = 0）。
- 原文 b0049 称黄金描述"平均 40 词"，而 b0014 与 b0051 称"平均 58 词"，两处不一致；译文各自按原文如实译出，未做统一。
- 原文 b0270 "In Fig. 12 and Fig 12"疑为笔误（应为图 12 与图 13），译文按上下文译为"图 12 与图 13"。
- 原文 b0251 "abiliiies"、b0209 "referencce""descrpition"等拼写笔误，译文按语义处理，不影响内容。

## 复核记录（第二轮交叉验证）

- 复核人：独立复核 Agent 08 号
- 抽查方式：`sample_blocks.py` 两轮随机抽样（种子 8 与 2024）+ 全量脚本化交叉校验（数字/公式占位符/未译块/长度比）
- 抽查块（共 12 块次）：b0072, b0164, b0195, b0206, b0270, b0241 / b0231, b0007, b0169, b0226, b0056, b0294
- 结论：共记录 1 条核验事项，逐条判定如下。

| 块 ID | 问题类型 | 复核发现 | 判定与处理 |
|---|---|---|---|
| b0066, b0173, b0245, b0286, b0288 | 数字一致性复核 | 脚本检出 top-3 / 1/4 / top-5 等数字未逐字保留 | ZH 分别译为「前三名」「约四分之一」「排名前五」，与 EN 语义等价，未修改。 |

- 其中标注「未修改」者为经核对后确认**非错误**（中文语序换位、等值数字改写、规范要求的英文专名保留），按规格书 §2「避免过度修改」不予改动。
- 重跑 `build_index.py`：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
