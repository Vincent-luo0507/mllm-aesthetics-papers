# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 212（文本 114 / 原子 98）|
| 已译文本块 | 114 / 114 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 73 · 已还原 73 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 208 |
| `<img>` 元素 | 29 |
| `<table>` 元素 | 22 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| multimodal large language model (MLLM) | 多模态大语言模型 | 首现保留英文缩写 |
| poster | 海报 | 全文统一 |
| typography | 字体排印 | 含字形、字重、字号、字距等排印属性 |
| font | 字体 | 与 typography 区分 |
| layout | 版式 | 指元素排布结构；Layout Generation 译"版面生成" |
| composition | 构图 | 与 layout 区分，指构成手法 |
| visual hierarchy | 视觉层次 | 信息层级 |
| saliency (control) | 显著性（控制） | 注意力导向 |
| intention | 意图 | 设计传达目的 |
| metaphor | 隐喻 | 视觉修辞手法 |
| visual rhetoric | 视觉修辞 | |
| empty space | 留白 | 版面中可放置新内容的空白区域 |
| whitespace | 留白 | 与 empty space 同一译法 |
| figure–ground | 图形—背景 | 视觉组织关系 |
| glyph | 字形 | |
| readability / legibility | 可读性 | 统一为可读性 |
| word-level recall (WR) | 词级召回率 | 指标名保留 WR |
| IoU | IoU | 交并比，首次括注 |
| ground truth | 真值 | 不译"地面真值" |
| bounding box | 边界框 | |
| patch (ID) | 图块（编号） | 网格切分单元 |
| judge (LLM-as-judge) | 评审模型 | "以大语言模型为评审" |
| checkpoint | 检查点 | 生成任务的核验项 |
| Point Score | 要点得分 | 指标名 |
| Font Richness | 字体丰富度 | 指标名 |
| Center Bias / Area Ratio | 中心偏移 / 面积比 | 保留英文原指标名 |
| prompt following | 提示词遵循 | |
| open-source / proprietary (Closed) | 开源模型 / 闭源模型 | 二者指同一集合，统一为闭源 |
| T2I (text-to-image) | 文生图 | 首现给出英文 |
| diffusion-based generator | 基于扩散的生成器 | |
| annotator | 标注员 | |
| inter-annotator agreement | 标注员间一致度 | |

### 交叉验证记录

| 块 id | 原文要点 | 我的译文 | 一致性 |
|---|---|---|---|
| b0022 | 五个 OCR 子任务：Logo / Real-World Poster / Simple / Hard / Multi-Size；Hard OCR 排除 "l"/"I"，14 种字号 | 五个子任务逐项对应，14 种字号、排除易混淆字符均保留 | 一致，数字未改动 |
| b0037 | 7,765 理解实例、822 生成提示、24 类任务；3005/2788/1178/575/219 与 114/135/256/117/200 | 全部数字逐项照录 | 一致 |
| b0057 | Gemini 构图/意图领先；GPT-Image-1 风格/意图领先但密集/字体落后；字体最佳 0.391、构图最高 0.866 | 保留 0.391、0.866 及各模型优劣关系 | 一致，未添加评价 |
| b0063 | VLM 监督 T2I 的迭代设置；VLM 只接收图像与原提示词；第 0 轮出现骷髅等不适元素 | 迭代流程、约束条件与第 0 轮问题均译出 | 一致 |
| b0172 | SLOT_65…SLOT_71 共 7 个占位符，属性覆盖率定义 | 7 个占位符顺序与原文完全一致 | 一致（已程序化校验） |

### 一致性与数字核查

- 术语统一：用 Grep 复核"字体排印""版式""构图""留白""真值""评审模型"在 zh.json 中用法一致，未出现"版面/布局""留白区/空白"等同义轮换；`proprietary` 与 `Closed` 统一译为"闭源"。
- 数字核查：7,765、822、24、3,005、2,788、1,178、575、219、114、135、256、117、200、0.9、0.45、0.295、0.802、0.824、0.391、0.866、80%、92%、90%、14、37、17、9、48 等全部原样保留，未换算或四舍五入。
- 占位符完整性：以脚本逐块比对 `⟦SLOT_n⟧` 序列，114 个文本块全部与原文序列完全一致，数量为 0 处偏差（脚本输出 slot mismatch: []）。
- 编码检查：zh.json 与 index.html 中均不含 U+FFFD（构建脚本 mojibake=0）。

### 遗留问题

- 原文 b0063 有一处语法不完整句"the enhanced prompt without any human or domain-specific design hints"，按上下文译为"增强后的提示词不含任何人工或领域专用的设计提示"，未改动源文件。
- 图片文件全部齐备（missing_img=0），无遗留图片问题。

## 复核记录（第二轮交叉验证）

抽查块：b0072、b0182、b0006、b0057、b0029、b0184


- **发现问题数**：0
- **已修正数**：0

判定依据：逐块对照 EN/ZH，完整性（无漏译跳句）、准确性（方法名/指标名/因果关系/否定/数量均无误）、
数字与符号（数值、百分比、模型名、数据集名、指标名原样一致）、公式占位符（`⟦SLOT_n⟧` 编号与数量
一致，随其指称成分一并移位属正常）、术语一致性、中文质量（通顺、无生造词、无明显 AI 腔）六项均未
见实质错误。另经全量脚本核查：占位符集合一致、无缺失译文块。

结构核验：MathJax 已加载；图片均为 `figures/` 本地相对路径、无 http 外链；无 U+FFFD；
顶部含中文标题与中文摘要；底部含「返回总目录」链接。重跑 `build_index.py` 后
`missing / stray / mojibake / missing_img` 四项均为 0。
