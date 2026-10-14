# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 148（文本 91 / 原子 57）|
| 已译文本块 | 91 / 91 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 0 · 已还原 0 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 0 |
| `<img>` 元素 | 5 |
| `<table>` 元素 | 3 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| graphic design | 平面设计 | 全文统一 |
| design element | 设计元素 | 指色彩、字体、版式三类 |
| element level / overall design level | 元素层面 / 整体设计层面 | 基准的两个层级，全文统一 |
| fine-grained | 细粒度 | |
| color / font / layout | 色彩 / 字体 / 版式 | 三大基本要素，typography 亦统一译“字体” |
| typography | 字体 | 与 font 同指三大要素之一，未另译“字体排印” |
| Multimodal Large Language Model (MLLM) | 多模态大语言模型（MLLM） | 首次出现附缩写 |
| attribute recognition | 属性识别 | 元素层面的视觉方面 |
| semantic understanding | 语义理解 | 元素层面的语义方面 |
| visual metaphor | 视觉隐喻 | 任务 #8 |
| negative space | 负空间 | 任务 #3 |
| visual center | 视觉中心 | 任务 #6 |
| salience map | 显著性图 | |
| style classification | 风格分类 | 任务 #7 |
| single-choice question | 单项选择题 | |
| multiple-choice question | 多项选择题 | |
| open-ended question | 开放式问题 | |
| ground truth | 标准答案 | |
| evaluator | 评价器 | 指 GPT-4 评价器 |
| prompt refining / refinement | 提示词优化 | 总称 |
| prompt rewriting | 提示词改写 | 4.3.1 小节 |
| supplementary information | 补充信息 | 4.3.2 小节 |
| composite image | 合成图像 | 多图合并后的单图 |
| instruction tuning | 指令微调 | |
| positional bias | 位置偏置 | |
| standard deviation | 标准差 | |
| Crello / CTXFont / PAT / Dafonts / Imp-1k / Poster / VisMet | 保留原名 | 数据集名 |
| Q-Former / FLAN-T5-XXL / Vicuna / LLaMA / OpenFlamingo | 保留原名 | 模型与模块名 |
| DesignProbe | 保留原名 | 基准名 |

### 交叉验证记录（随机抽 5 块）

| id | 原文要点 | 我的译文 | 一致性结论 |
|---|---|---|---|
| b0032 | 任务 #1 色彩主题；从 Crello 抽样 50 个样本；预定义调色板 | • 任务 #1：色彩主题。目标是评价模型识别设计中主色的能力……从 Crello（Yamaguchi，2021）中随机抽取 50 个设计样本…… | 一致；数字 50 与数据集名保留 |
| b0045 | 单选仍产生开放式回答；GPT-4 自动评价；四级评分 [Correct, Partially Correct, Incorrect, Irrelevant] | 同上中文表述，四级译为「正确／部分正确／错误／无关」 | 一致；四个等级名逐项对应 |
| b0063 | 每题重复四次、正确答案位置不同；每项任务共 200 题 | 同上中文表述 | 一致；两个数字原样保留 |
| b0076 | GPT-4 Vision 总平均 59.4%；及格线 60% | 同上中文表述 | 一致；两个百分比未改动 |
| b0092 | LLaVA 从 43.0% 降至 38.5%；GPT-4 Vision 变化相反；版式任务 #3、#6 | 同上中文表述 | 一致；两个百分比与任务编号保留 |

### 一致性与数字核查

- 术语统一性：Grep 复核 zh.json，「平面设计」「设计元素」「元素层面／整体设计层面」「色彩／字体／版式」「视觉隐喻」「负空间」「视觉中心」「提示词改写」「提示词优化」「评价器」等核心术语全文译法唯一；三个基本要素在各章节与任务描述中统一为「色彩、字体、版式」。
- 数字与指标：8、9、5、50、200、4、3x3、90%、59.4%、60%、72.0%、43.5%、7.9%、1.2%、8%、3.0%、2.5%、10.5%、43.0%、38.5%、85%、26 个数据集、13B／7B／120 亿 等全部逐位保留；任务编号 #1～#8、选项 A/B/C/D、Ori、Re.、std. 等记法原样。
- 占位符完整性：本文 91 个文本块不含 `⟦SLOT_n⟧` 占位符（mismatch 列表为空），构建脚本 stray=0、math=0。
- 编码检查：zh.json 与 index.html 均不含 U+FFFD 乱码字符，编码为 UTF-8。

### 遗留问题

1. 原文 b0008 末尾残留引用标记 “color?.”，疑为失效的 LaTeX 引用；译文按语义收束为“同时还需要与整体情绪和风格相一致”，未保留该标记。
2. b0006 中 “it focus on” 等主谓不一致、b0020 中 “comprehensive” 等拼写问题属原文自身笔误，译文按正确语义处理，未额外标注。
3. 本文所有 `t:"text"` 块均不含公式槽位，故未产生占位符还原工作；math=0 属原文结构特性，非遗漏。
4. 图片缺失 0，figures/ 资源齐全。

## 复核记录（第二轮交叉验证）

- 复核人：Agent 02（独立复核，非译者）
- 结构核验：MathJax（`tex-mml-chtml.js`）已加载；5 处图片 `src` 全部为 `figures/` 本地相对路径，无 http 外链；无 U+FFFD；顶部中文标题与中文摘要齐备，底部有「返回总目录」链接。
- 抽查块：b0004、b0081、b0011、b0050、b0083、b0079（seed=2）；加抽 b0045、b0022、b0037、b0004（seed=7）
- 另复核短译文块 b0024（216→50 字符，语义完整）。
- 判定：上述全部抽查块在完整性（无漏译跳句）、准确性（无错译、无因果/否定/数量颠倒）、数字与符号（模型名/数据集名/指标名/百分数原样一致）、公式占位符（`⟦SLOT_n⟧` 集合与顺序全篇逐块机器比对一致）、术语一致性、中文通顺度六项上均通过，**抽查未发现实质错误，未作任何修改**。
- 构建产物校验：`index.html` 四项校验（missing / stray / mojibake / missing_img）均为 0，本次未改动 `zh.json`，未重跑构建。
