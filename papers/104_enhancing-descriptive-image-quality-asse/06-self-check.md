# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 332（文本 174 / 原子 158）|
| 已译文本块 | 174 / 174 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 82 · 已还原 82 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 198 |
| `<img>` 元素 | 26 |
| `<table>` 元素 | 29 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| Image Quality Assessment (IQA) | 图像质量评价（IQA） | 首现附缩写，后文可用 IQA |
| Vision Language Model (VLM) | 视觉语言模型（VLM） | 同上 |
| descriptive IQA | 描述式 IQA | 与 score-based 对举 |
| score-based IQA | 基于分数的 IQA | 传统方法类别 |
| DepictQA-Wild | DepictQA-Wild | 模型名保留 |
| DQ-495K | DQ-495K | 数据集名保留 |
| distortion | 失真 | 全文统一，不写作"退化" |
| full-reference / non-reference | 全参考 / 无参考 | 两种设定统一译法 |
| single-image assessment | 单图评价 | 任务 1 |
| paired-image comparison | 双图比较 | 任务 2 |
| distortion identification | 失真识别 | 简要子任务 |
| instant rating | 即时评分 | 简要子任务 |
| assessment reasoning | 评价推理 | 详细子任务 |
| comparison reasoning | 比较推理 | 详细子任务 |
| Mean Opinion Score (MOS) | 平均意见分数（MOS） | |
| GT-informed generation | GT 引导生成 | 首现说明其为向 GPT-4V 提示真值细节 |
| severity level | 严重等级 | 五级：轻微/中等/明显/严重/灾难性 |
| super-category / sub-category | 父类 / 子类 | 12 个父类、35 个子类 |
| win rate | 胜率 | 质量分数的计算依据 |
| SRCC | Spearman 秩相关系数（SRCC） | 首现全称 |
| PLCC | Pearson 线性相关系数（PLCC） | 首现全称 |
| GPT-4 score | GPT-4 分数 | 以 GPT-4 打分的评估指标 |
| vision abstractor | 视觉抽象器 | 与 projector 对举 |
| projector | 投影器 | |
| token | 词元 | 全文统一，不写作"令牌" |
| confidence score | 置信度分数 | |
| semantic change testing | 语义变化测试 | 选关键词元的方法 |
| out-of-distribution (OOD) | 分布外（OOD） | |
| in-the-wild | 真实场景 | 指网络真实图像 |
| LoRA | LoRA | 微调技术名保留 |
| ablation study | 消融研究 | |
| two-alternative forced choice (2AFC) | 二选一强制选择（2AFC） | |
| pseudo label | 伪标签 | |
| patch | 图像块 | 视觉编码器输入单位 |

### 交叉验证记录

| 块 id | 原文要点 | 译文要点 | 一致性 |
|---|---|---|---|
| b0006 | Co-Instruct 在 TID2013 上 85.0%，在 BAPPS 上降至 50.7%；指出数据覆盖/质量/规模与固定分辨率的限制 | 两个百分比与四个限制因素逐项对应 | 一致 |
| b0024 | 多图（⟦SLOT_0⟧2）比较被略去，因可由成对情形扩展 | 槽位嵌入括号中，扩展理由表述一致 | 一致 |
| b0074 | 多失真下很高准确率（⟦SLOT_7⟧90%）难、中等准确率（⟦SLOT_8⟧40%）较易；OOD 设定描述 | 两个槽位顺序与数值一致，OOD 的子类划分示例（高斯噪声/脉冲噪声）未改动 | 一致 |
| b0088 | 全参考下 SSIM/FSIM/LPIPS/DepictQA-Wild 在四个数据集上的 SRCC / PLCC | 十六组数值原样保留，PIPAL⟦SLOT_9⟧ 与 KADID⟦SLOT_10⟧ 两个槽位保留 | 一致 |
| b0267 | 抖动模糊：位移 ⟦SLOT_28⟧ 像素、发生在 ⟦SLOT_29⟧ 与 ⟦SLOT_30⟧ 维度、共 5 次，其中 ⟦SLOT_31⟧ | 四个槽位按原文顺序出现，参数描述未增删 | 一致 |

### 一致性与数字核查

- 术语：distortion 统一为「失真」，full-reference / non-reference 统一为「全参考 / 无参考」，四个子任务名（失真识别、评价推理、即时评分、比较推理）全文写法一致；token 统一为「词元」。
- 数字与指标：35 种失真、5 个等级、5%、495K、439,676、55,577、112,000、19,829/7,981、215,676、95.9%、85.0%、88.1%、74.9%、48.1%、60.3%、58/62/60/15、7.11B/6.76B/0.30B/54M/70M/0.98%、2.23s、0.07s、22.97s、0.72s、22 小时等均按原文字面保留；SRCC、PLCC、BLEU、ROUGE-L、LoRA、PSNR、SSIM、LPIPS、DISTS、NIQE、CLIPIQA、MUSIQ、MANIQA 等指标与模型名未改写。
- 占位符：174 个文本块共 82 处 `⟦SLOT_n⟧`，生成前用脚本逐块比对槽位序列，全部一致；脚本校验残留为 0。
- 编码：zh.json 与 index.html 均不含 U+FFFD，脚本 mojibake 计数为 0。

### 遗留问题

- 无图片缺失（missing_img = 0），无不可解析块。
- 原文多处段落被 HTML 拆成两块（b0016、b0018、b0059、b0074、b0110、b0132），译文保持各自的截断位置，未做合并。
- 原文 b0057 两次引用「Fig. 6」（词长分布与词云各一次），疑为原文的图表编号笔误（图注分别为 Fig. 5 与 Fig. 6），译文忠实保留原文的引用写法，未擅自改正。
- 附录 -A1 中大量失真参数以公式槽位承载，中文仅描述其语义与参数名，公式本身由脚本还原。

## 复核记录（第二轮交叉验证）

- 复核人：独立复核 Agent 08 号
- 抽查方式：`sample_blocks.py` 两轮随机抽样（种子 8 与 2024）+ 全量脚本化交叉校验（数字/公式占位符/未译块/长度比）
- 抽查块（共 12 块次）：b0299, b0329, b0062, b0057, b0072, b0297 / b0080, b0060, b0085, b0088, b0260, b0077
- 结论：共记录 1 条核验事项，逐条判定如下。

| 块 ID | 问题类型 | 复核发现 | 判定与处理 |
|---|---|---|---|
| zh_abstract（meta.json） | 漏译整句（未修正） | EN 摘要末句「Codes, datasets, and model weights have been released in https://depictqa.github.io/.」在中文摘要中缺失，ZH 止于「……在评价网络下载图像、排序模型处理图像等真实应用中得到确认。」 | 属摘要漏译，应补「代码、数据集与模型权重已在 https://depictqa.github.io/ 发布。」；但中文摘要存放于 meta.json，规格书 §C 明确禁止修改该文件，故未直接改写，在此登记，建议由译者在 meta.json 的 zh_abstract 末尾补入该句。 |

- 其中标注「未修改」者为经核对后确认**非错误**（中文语序换位、等值数字改写、规范要求的英文专名保留），按规格书 §2「避免过度修改」不予改动。
- 重跑 `build_index.py`：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
