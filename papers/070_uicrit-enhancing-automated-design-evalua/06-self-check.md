# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 289（文本 223 / 原子 66）|
| 已译文本块 | 223 / 223 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 1 · 已还原 1 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 2 |
| `<img>` 元素 | 11 |
| `<table>` 元素 | 7 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| UI evaluation | UI 评估 | 全文统一，不译为「界面评估」 |
| design critique | 设计评语 | 与 comment（设计评论）区分：critique 指结构化评语，comment 指生成式输出 |
| heuristic evaluation | 启发式评估 | 沿用 Nielsen 经典译法 |
| few-shot prompting | 少样本提示 | 含 2/4/8-shot 一律作「N 样本」 |
| zero-shot prompting | 零样本提示 | |
| visual prompting | 视觉提示 | 指在截图上叠加坐标/网格/图块编号的图像增强方式 |
| prompt chain | 提示链 | 多次 LLM 调用串联 |
| bounding box | 边界框 | 与 ROI 一并保留英文缩写 |
| region of interest (ROI) | 兴趣区域（ROI） | 首次出现附英文缩写 |
| design quality rating | 设计质量评分 | rating 统一作「评分」，score 作「得分」 |
| rubric | 量规 | 评分标准表 |
| Likert scale | 李克特量表 | |
| annotator / worker | 标注者 / 工作者 | 指众包标注人员时互换使用，保持各自一致 |
| inter-rater agreement | 评分者间一致性 | Fleiss’ Kappa 保留原文 |
| intersection over union (IoU) | 交并比（IoU） | |
| hallucination | 幻觉 | |
| tool-agnostic | 与工具无关 | 指不依赖设计工具内部表示 |
| reward model | 奖励模型 | |
| learnability | 可学习性 | Nielsen 五要素之一 |
| button usability | 按钮可用性 | 数据集五大主题之一 |
| text readability | 文字可读性 | |
| color contrast | 颜色对比度 | |
| visual hierarchy | 视觉层级 | |
| view hierarchy | 视图层级 | Android 结构树，与前者区分 |
| mockup | 设计稿 | Figma 语境 |
| K-means clustering | K 均值聚类 | |
| grounded theory coding | 扎根理论编码 | |
| thematic analysis | 主题分析 | |
| codebook | 编码本 | 定性分析产物 |
| affordance | 可供性 | 交互设计术语 |

### 交叉验证记录

| 块 id | 原文要点 | 译文 | 一致性确认 |
|---|---|---|---|
| b0043 | 3,059 条评语中 2,283（74.6%）来自人类、256（8.3%）来自 Gemini、520（17.1%）共同给出；Gemini 生成 5,927 条仅 776 条有效（13.1%） | 逐项保留 3,059 / 2,283 / 74.6% / 256 / 8.3% / 520 / 17.1% / 5,927 / 776 / 13.1% | 数字、百分比、归属关系一致，无增删 |
| b0078 | 计算 UICrit 界面级评分与 Google Play 商店应用评分的皮尔逊相关系数，多屏应用取平均 | 完整保留「皮尔逊相关系数」「Google Play 商店」「多屏取平均」 | 方法名与数据处理方式一致 |
| b0093 | 三种少样本采样：随机、视觉相似度（均方根差）、语义相似度（CLIP 共享图文空间） | 三项逐一对应，保留 RMS 差与 CLIP 的方法名 | 技术路径与动机一一对应 |
| b0130 | 本方法平均质量分高出零样本基线 0.17（⟦SLOT_0⟧），相当于 55% 提升；Fleiss Kappa 0.29 | 保留 0.17、55%、0.29 与占位符 ⟦SLOT_0⟧ | 占位符原样保留，数值未改动 |
| b0211 | Poor Text Justification and Formatting: Poor text alignment and justification | 「文字对齐与排版不佳：文字对齐与两端对齐处理不当」 | 代码名与定义均译出，无遗漏 |

### 一致性与数字核查

- 术语统一性：以 Grep 全篇回扫确认，`设计评语`（critique）与`设计评论`（comment）分工固定；`少样本提示`、`零样本提示`、`视觉提示`、`边界框`、`UI 评估`、`设计稿`等核心术语全文译法唯一，未出现同义词轮换。
- 数字与指标：3,059 / 983 / 7 / 1,000 / 2,283 / 74.6% / 256 / 8.3% / 520 / 17.1% / 5,927 / 776 / 13.1% / 0.30 / 0.31 / 0.29 / 0.55 / 0.17 / 55% / 0.007 / 0.022 / 0.023 / 0.875 / 95 / 208 / 66k / 9.3k / 27 等全部原样保留；模型名 Gemini Pro Vision、GPT-4V、CLIP、SentenceBERT、t-SNE、K 均值与数据集名 RICO、CLAY、UIEyes、MoTIF 均保留原文。
- 占位符：全文 1 处 ⟦SLOT_0⟧（b0130），译文中数量与编号与原文一致，构建脚本 `stray` 为 0。
- 编码：`zh.json` 与 `index.html` 均不含 U+FFFD。
- 未改动 `blocks.json` / `translate_input.json` / `orig.html`。

### 遗留问题

- 部分图注（b0029、b0031、b0038、b0042、b0048、b0059、b0072、b0086、b0116、b0201）末尾附有一句与论文内容无关的图像描述句「A woman and a girl in white dresses sit in an open car.」，疑为自动图像描述（alt-text）串入原文。按不删改原文的要求，已如实译出并保留位置，未修改源文件。
- b0247 原文句末似有截断（「the need to increase or change the font weight for better」），译文按原文如实处理，未补全。
- b0220「Layout Simplicity」的定义在原文中复用了对齐问题的表述（疑为原文笔误），译文按原文照译，未作修正。
- 图片文件引用缺失为 0，无图片下载需求。


## 复核记录（第二轮交叉验证）

- 复核人：独立复核 Agent 08 号
- 抽查方式：`sample_blocks.py` 两轮随机抽样（种子 8 与 2024）+ 全量脚本化交叉校验（数字/公式占位符/未译块/长度比）
- 抽查块（共 12 块次）：b0083, b0032, b0097, b0051, b0131, b0279 / b0225, b0066, b0083, b0111, b0086, b0005
- 结论：共记录 1 条核验事项，逐条判定如下。

| 块 ID | 问题类型 | 复核发现 | 判定与处理 |
|---|---|---|---|
| b0008, b0130, b0136, b0026, b0043 | 数字一致性复核 | 脚本检出 55 percent / 3,059 / 7 annotators 未逐字保留 | ZH 分别译为「55%」「3,059」「七位」，数值与格式均正确，未修改。 |

- 其中标注「未修改」者为经核对后确认**非错误**（中文语序换位、等值数字改写、规范要求的英文专名保留），按规格书 §2「避免过度修改」不予改动。
- 重跑 `build_index.py`：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
