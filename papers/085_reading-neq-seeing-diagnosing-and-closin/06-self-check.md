# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 292（文本 191 / 原子 101）|
| 已译文本块 | 191 / 191 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 48 · 已还原 48 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 122 |
| `<img>` 元素 | 7 |
| `<table>` 元素 | 15 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| Vision-Language Model (VLM) | 视觉语言模型 | 首现保留缩写 VLM |
| typography | 字体排印 | 与团队内 067 篇口径一致 |
| typography blindness / typography-blind | 字体排印盲 | |
| font family | 字体族 | 与 font 区分 |
| font size | 字号 | |
| font style | 字体样式 | regular/bold/italic/bold-italic |
| font color | 字体颜色 | |
| perception hierarchy | 感知层级 | 颜色 ⟶ 字体族 ⟶ 字号 ⟶ 样式 |
| difficulty invariance | 难度不变性 | 诊断性信号 |
| scaling paradox | 规模悖论 | 参数增加不带来提升 |
| capability-fragility trade-off | 能力—脆弱性权衡 | |
| OCR dominance | OCR 主导 | 文字内容压倒视觉证据 |
| stroop effect | stroop 效应 | 保留原文写法 |
| script / writing system | 文字系统 / 书写系统 | 二者统一 |
| CJK | CJK | 不译 |
| Devanagari | 天城文 | |
| serif / sans-serif / monospace / display | 衬线体 / 无衬线体 / 等宽体 / 装饰体 | |
| glyph | 字形 | |
| stroke weight | 笔画粗细 | |
| stroke terminal | 笔画末端 | |
| distractor | 干扰项 | 选择题干扰选项 |
| multiple-choice question (MCQ) | 多项选择题 | |
| random baseline | 随机基线 | |
| LoRA | LoRA | 不译 |
| patch-based encoder | 基于 patch 的编码器 | |
| latent feature | 潜在特征 | |
| relational comparison | 关系比较 | |
| attention heatmap | 注意力热图 | |
| percentage point (pp) | 百分点 | |
| quantization (NF4) | 量化（NF4） | |
| confidence interval | 置信区间 | |
| Wilson score interval | Wilson 得分区间 | 保留专名 |
| McNemar's test | McNemar 检验 | 保留专名 |
| contrast ratio | 对比度 | |
| anti-aliasing | 抗锯齿 | |
| pangram | 全字母句 | |
| FRB (Font Recognition Benchmark) | FRB | 保留原名，首现括注中文 |

### 交叉验证记录

| 块 id | 原文要点 | 我的译文 | 一致性 |
|---|---|---|---|
| b0007 | 15 个 VLM；颜色近完美、族与字号居中、样式仅略高于 25% 基线；剔除颜色后均值 35% | 层级顺序、25% 基线、35% 均照录 | 一致 |
| b0043 | Qwen3-VL-8B 简单 50.3%/中等 53.2%/困难 50.0%；Gemini-3-Flash 65.9%/67.2%/67.1% | 六个数值与难度顺序完全对应 | 一致 |
| b0049 | Qwen2.5：7B 51.2% > 32B 47.5%，72B 51.1%；Qwen3：30B-A3B 54.4% > 32B 51.4% | 数值与"小胜大"的悖论关系保留 | 一致 |
| b0077 | 3,000 样本；51.1→60.8、51.2→59.5；差距 15.6pp→5.9pp；32B 仅 3.5pp | 全部数值原样，增益关系未改写 | 一致 |
| b0229 | McNemar 检验；Gemini-3-Flash 显著优于全部；中位梯队不显著；GLM-4.5V 与 Pixtral-12B 与 25% 基线无显著差异；含 8 个模型名单 | 8 个模型名与显著性结论逐项译出 | 一致 |

### 一致性与数字核查

- 术语统一：Grep 复核"字体排印""字体族""字号""字体样式""感知层级""随机基线""关系比较"在 zh.json 中用法唯一；`script` 与 `writing system` 统一译为"文字系统"/"书写系统"，未出现"脚本"（避免与计算机语境混淆）等同义轮换。
- 数字核查：26、4、3、15、250、1,000、81.2%、35.2%/30.8%/34.0%、96 DPI、4.5:1、12–64pt、25%、6.7%、95–100%、23–34%、22–81%、33.6%、66.7%、55.6%、35%、3,000、7.6B/8.3B/32.8B、0.05、0.2–0.3%、22.0pp、14pp、16.0pp、1.6pp、100%、17.3pp、10.2pp、6.4pp、53.5%⟶61.8%、40.5%/22.9%/20.8%、9.6%/9.9%/10.1%、89.2%、97.6%、34.4%、44.4%、49.6%、36.8%、18、11、42、161 等全部原样保留，未换算或四舍五入。
- 占位符完整性：脚本逐块比对 `⟦SLOT_n⟧` 序列（含 SLOT_0～SLOT_47），191 个文本块全部一致，输出 slot mismatch: []。
- 编码检查：zh.json 与 index.html 中不含 U+FFFD（构建脚本 mojibake=0）。

### 遗留问题

- 原文 b0053 的脚注标记与正文粘连（"2⟦SLOT_14⟧).11 1 Baseline accuracies..."），按语义断句为"…分辨率…）。11 1 本节报告的基线准确率…"，未改动源文件。
- 原文 b0176 写作 "Tables 5 and 5 specify..."，疑为笔误（应为 Tables 4 and 5），照原文译为"表 5 与表 5"，未擅自更正，也未改动源文件。
- 原文 b0256 提到"表 13 给出按字号区间的表现"，而紧随的图注先出现"表 12：按字号区间划分"，编号顺序与正文引用不一致；按原文照译，未改动源文件。
- 图片文件全部齐备（missing_img=0）。

## 复核记录（第二轮交叉验证）

- 复核 Agent：06 号（独立交叉验证）
- 结构核验：MathJax（`tex-mml-chtml.js`）已加载；图片 `src` 全部为 `figures/...` 本地相对路径、无 http 外链；全文无 U+FFFD 乱码；顶部有中文标题与中文摘要，底部有「返回总目录」链接 —— 全部通过。
- 抽查块（9 块）：b0061、b0030、b0072、b0015、b0010、b0068、b0145、b0248、b0059
- 逐块比对 EN/ZH 的六项判读：完整性（无漏译整句/跳句）、准确性（无错译、无因果或否定反转）、数字与符号（数字、百分比、模型名、数据集名、指标名与原样一致）、公式占位符（`⟦SLOT_n⟧` 编号与顺序完全一致）、术语一致性（同篇内译法统一）、中文质量（通顺、无生造词、无 AI 腔堆砌）—— **未发现实质错误**。
- 附加机器校验：全篇文本块无缺失译文；每块占位符数量与顺序逐一比对一致；数字差分扫描命中的差异经人工核对均为中英数量表达差异（如 `4.8 million` → 「480 万」、`7.6B` → 「76 亿」、`10,073` → 「10,073」），非错译。
- 已修正：无（未改动 `zh.json`）。
- 重跑 `build_index.py` 四项校验：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
