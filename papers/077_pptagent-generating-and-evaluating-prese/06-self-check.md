# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 237（文本 146 / 原子 91）|
| 已译文本块 | 146 / 146 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 35 · 已还原 35 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 126 |
| `<img>` 元素 | 9 |
| `<table>` 元素 | 11 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| presentation | 演示文稿 | 全文统一，不译「PPT」 |
| slide | 幻灯片 | |
| text-to-slides | 文本到幻灯片 | 范式名，首次出现补英文 |
| reference presentation / reference slide | 参考演示文稿 / 参考幻灯片 | |
| functional type | 功能类型 | |
| content schema | 内容模式 | schema 统一译「模式」 |
| slide clustering | 幻灯片聚类 | |
| structural slides / content slides | 结构性幻灯片 / 内容型幻灯片 | |
| schema extraction | 模式抽取 | |
| edit API | 编辑 API | API 名（replace_span 等）保留原文 |
| HTML-rendered representation | HTML 渲染表示 | |
| Code Render | Code Render | 消融组件名，保留英文 |
| self-correction mechanism | 自我纠正机制 | |
| REPL | REPL | 保留 |
| outline | 大纲 | |
| Content / Design / Coherence | 内容 / 设计 / 连贯性 | PPTEval 三维度 |
| MLLM-as-a-judge | 以多模态大语言模型充当评判器 | 首次出现补英文 |
| Success Rate (SR) | 成功率（SR） | |
| Perplexity (PPL) | 困惑度（PPL） | |
| ROUGE-L | ROUGE-L | 指标名保留 |
| FID | FID | 指标名保留 |
| Zenodo10K | Zenodo10K | 数据集名保留 |
| abstraction summarization | 抽象式摘要 | |
| rule-based / template-based | 基于规则 / 基于模板 | |
| inter-rater agreement | 评分者间一致性 | |
| Fleiss' Kappa | Fleiss' Kappa | 保留 |
| Pearson correlation | 皮尔逊相关系数 | |
| hierarchical clustering | 层次聚类 | |
| cosine similarity | 余弦相似度 | |
| image caption | 图像说明 | |
| two-stage | 两阶段 | |

### 交叉验证记录

| id | 原文要点 | 译文 | 语义一致性 |
|---|---|---|---|
| b0012 | 两阶段设计、HTML 渲染表示的编辑 API、自我纠正机制、按类别聚类参考幻灯片 | 逐条对应，replace_span 等 API 名原样保留 | 一致 |
| b0059 | 三个模型（GPT-4o、Qwen2.5-72B-Instruct、Qwen2-VL-72B-Instruct）、LM/VM 配置组合 | 模型名与下标说明完整译出，保留 ⟦SLOT_12⟧、⟦SLOT_13⟧ | 一致 |
| b0075 | 设计 3.34 vs 2.37（+40.9%）、内容 3.34 vs 2.98（+12.1%）、KCTV 3.34 vs 2.95（+13.2%）、3.28 vs 2.55（+28.6%）、连贯性 4.48 vs 3.57（+25.5%）与 4.48 vs 3.28（+36.6%） | 全部数值与增量百分比原样保留 | 一致 |
| b0087 | 去掉 Code Render 成功率 95.0%→74.6%；去掉大纲/结构幻灯片连贯性 4.48→3.36/3.45；去掉模式成功率 95.0%→78.8% | 数值逐项对应 | 一致 |
| b0156 | 页数 12–64、文本长度 2048–20480 字符、图像相似度阈值 0.85、幻灯片相似度阈值 0.8 | 全部阈值原样保留 | 一致 |

### 一致性与数字核查

- 术语统一性已用 Grep 复核：演示文稿、幻灯片、参考幻灯片、内容模式、幻灯片聚类、自我纠正机制、连贯性、成功率、困惑度等译法全文唯一。
- 全部数字原样保留：10448 份演示文稿、50×5 参考与文档、500 个生成任务、两轮自我纠正、500 GPU 小时、3.67 平均分、95.0%/74.6%/78.8%/91.0%/92.2%、4.48/3.36/3.45、16.76 与 14.25 的 ROUGE-L、Pearson 0.71、Fleiss' Kappa 0.59（0.61/0.61/0.54）、2048–20480 字符、12–64 页、阈值 0.85/0.8/0.65、1006 行 XML 等均未改动；模型名（GPT-4o、Qwen2.5、Qwen2-VL、Llama-3-8B）、基线名（DocPres、KCTV）、数据集名（Zenodo10K）与 API 名（replace_span、del_span、clone_paragraph 等）全部保留原文。
- 占位符核查：本文 SLOT 编号 0–34，共 35 处；译文中逐一原样保留，编号未错位（b0171 为 SLOT_30，b0203 为 SLOT_31/32，b0205 为 SLOT_33/34）。脚本校验 `stray=0`、`missing=0`。
- 编码核查：`zh.json` 与 `index.html` 中不含 `�`（U+FFFD），脚本 `mojibake=0`。

### 遗留问题

- 无。图片文件齐全（`missing_img=0`），公式槽位全部还原。

## 复核记录（第二轮交叉验证）

- 复核 Agent：06 号（独立交叉验证）
- 结构核验：MathJax（`tex-mml-chtml.js`）已加载；图片 `src` 全部为 `figures/...` 本地相对路径、无 http 外链；全文无 U+FFFD 乱码；顶部有中文标题与中文摘要，底部有「返回总目录」链接 —— 全部通过。
- 抽查块（10 块）：b0052、b0068、b0047、b0038、b0031、b0084、b0098、b0071、b0178、b0201
- 逐块比对 EN/ZH 的六项判读：完整性（无漏译整句/跳句）、准确性（无错译、无因果或否定反转）、数字与符号（数字、百分比、模型名、数据集名、指标名与原样一致）、公式占位符（`⟦SLOT_n⟧` 编号与顺序完全一致）、术语一致性（同篇内译法统一）、中文质量（通顺、无生造词、无 AI 腔堆砌）—— **未发现实质错误**。
- 附加机器校验：全篇文本块无缺失译文；每块占位符数量与顺序逐一比对一致；数字差分扫描命中的差异经人工核对均为中英数量表达差异（如 `4.8 million` → 「480 万」、`7.6B` → 「76 亿」、`10,073` → 「10,073」），非错译。
另注：章节标题 `2 PPTAgent`、`3 PPTEval` 保留英文原题，属专有名词保留，按规范不改。
- 已修正：无（未改动 `zh.json`）。
- 重跑 `build_index.py` 四项校验：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
