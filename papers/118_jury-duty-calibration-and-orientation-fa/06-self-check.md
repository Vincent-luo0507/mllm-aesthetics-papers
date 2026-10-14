# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 228（文本 153 / 原子 75）|
| 已译文本块 | 153 / 153 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 200 · 已还原 200 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 411 |
| `<img>` 元素 | 6 |
| `<table>` 元素 | 4 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| MLLM-as-a-Judge | MLLM 即评判者（MLLM-as-a-Judge） | 首次出现括注英文 |
| LLM-as-a-Judge | LLM 即评判者 | |
| human reference pool | 人类参照池 | |
| annotator pool | 标注者池 | |
| cultural ambiguity | 文化模糊性 | |
| calibration failure | 校准失效 | 指无法给出低端评分 |
| orientation failure | 取向失效 | 指默认采用某一种文化规范 |
| positivity floor | 积极性下限 | 模型几乎不产出 1/2 分 |
| orientation residual | 取向残差 | 校准部分恢复后仍残留的倾斜 |
| tilt / cultural tilt | 倾斜 / 文化倾斜 | |
| tilt-to-CN | 向中国倾斜 | |
| cross-pool divergence | 跨池分歧 | |
| within-pool reliability | 池内可靠性 | |
| anchor / contested probe | 锚点 / 争议探针 | 基准条目二分 |
| concept-paired | 概念配对 | |
| in-context learning (ICL) | 上下文学习（ICL） | |
| in-context demonstration | 上下文示例 | |
| persona prompting | 角色提示 | |
| persona prefix | 角色前缀 | |
| model origin | 模型来源 | 按开发者地理分组 |
| covariate | 协变量 | |
| bicultural-fluent | 双文化流利 | |
| mainland Chinese | 中国大陆 | |
| U.S.-aligned / Chinese-aligned | 美国对齐 / 中国对齐 | 修饰图像 |
| ordinal scale | 有序量表 | |
| Likert | Likert | 保留 |
| Krippendorff's alpha | Krippendorff α | |
| quadratic-weighted kappa | 二次加权 κ | |
| MAE / Pearson | MAE / Pearson | 指标名保留 |
| paired Wilcoxon | 配对 Wilcoxon | |
| fixed effects | 固定效应 | |
| construct label | 构念标签 | |
| leaderboard | 排行榜 | |
| RLAIF | RLAIF | 保留 |
| WEIRD | WEIRD | 保留原词 |

### 交叉验证记录（随机抽样 5 块）

| 块 id | 原文要点 | 本文译文 | 一致性判断 |
|---|---|---|---|
| b0026 | 626 个条目、各 313；三个类别及每类数量（147/64/102）；概念配对定义 | 全部数值与类别名逐项对应 | 数字一致，未四舍五入 |
| b0047 | Krippendorff ⟦SLOT_10⟧ 在 Q1 上为 ⟦SLOT_11⟧（美）/⟦SLOT_12⟧（中），超过 ⟦SLOT_13⟧ 与 ⟦SLOT_14⟧ 阈值 | 四项占位符原样保留 | 占位符与语义一致 |
| b0062 | 模型几乎不产 1/2 分（⟦SLOT_49⟧–⟦SLOT_50⟧）；美国共识为 ⟦SLOT_52⟧ 的 ⟦SLOT_51⟧ 个条目上仅 ⟦SLOT_53⟧–⟦SLOT_54⟧ 降得那么低；最强美国角色也只到 ⟦SLOT_55⟧–⟦SLOT_56⟧ | 各百分比与占位符原样保留，机制解释完整译出 | 语义一致 |
| b0082 | 固定示例图像/标注者池时 ⟦SLOT_111⟧–⟦SLOT_114⟧ 的位移；ac 设计下 glm-5 例外；1.49 对 1.48 | 数值与例外条件均保留 | 数字与结论一致 |
| b0209 | 中栏方便面杯示例：全球扩散、低声望涵义相同、两池收敛于中高分；排除标准 | 示例描述与排除准则逐项对应 | 语义一致 |

### 一致性与数字核查

- 术语统一性：用 Grep 复核「MLLM 即评判者」「人类参照池」「标注者池」「文化模糊性」「校准失效」「取向失效」「积极性下限」「取向残差」「跨池分歧」「上下文示例」「角色提示」「模型来源」等核心术语，确认全文译法唯一；「美国/中国」作为池名统一写作「美国池/中国池」或「美国人类/中国人类」，未混用。
- 数字核查：条目数 626 / 313 / 147 / 64 / 102、锚点与争议探针 227/39/360、187,800 单元、10.9%–12.7%、14.2–16.6% 对 16.5%、1.486 对 1.480、3.84 与 3.90–3.98、每小时 20 美元、约 1700 美元等均逐项比对原文，未做任何换算或改写；统计量一律以占位符保留。
- 占位符完整性：200 个 ⟦SLOT_n⟧ 槽位在译文中数量与编号与原文完全一致。
- 编码检查：zh.json 与 index.html 中 U+FFFD 计数均为 0。

### 遗留问题

- 原文 b0011 中「VOIR DIRE」后的脚注标记「11 1」为抽取残留，译文按原样保留。
- 原文 b0226 末句「(…) the demonstrations convert…」前缺少标点，译文中补入逗号使句子通顺，未添加任何新信息。
- 原文 b0072「collapses to ⟦SLOT_85⟧ to ⟦SLOT_86⟧」两处占位符之间缺少介词，译文按「从…坍缩至…」处理以贴合语义，未改动占位符。
- 原文 b0003 缺失（block id 从 b0002 直接跳到 b0004），非译文遗漏；已核对 translate_input.json 本身即无 b0003。



## 复核记录（第二轮交叉验证）

- 复核 Agent：06 号（独立交叉验证）
- 结构核验：MathJax（`tex-mml-chtml.js`）已加载；图片 `src` 全部为 `figures/...` 本地相对路径、无 http 外链；全文无 U+FFFD 乱码；顶部有中文标题与中文摘要，底部有「返回总目录」链接 —— 全部通过。
- 抽查块（9 块）：b0047、b0082、b0078、b0076、b0099、b0224、b0021、b0070、b0014
- 逐块比对 EN/ZH 的六项判读：完整性（无漏译整句/跳句）、准确性（无错译、无因果或否定反转）、数字与符号（数字、百分比、模型名、数据集名、指标名与原样一致）、公式占位符（`⟦SLOT_n⟧` 编号与顺序完全一致）、术语一致性（同篇内译法统一）、中文质量（通顺、无生造词、无 AI 腔堆砌）—— **未发现实质错误**。
- 附加机器校验：全篇文本块无缺失译文；每块占位符数量与顺序逐一比对一致；数字差分扫描命中的差异经人工核对均为中英数量表达差异（如 `4.8 million` → 「480 万」、`7.6B` → 「76 亿」、`10,073` → 「10,073」），非错译。
另注：章节标题 `3 VOIR DIRE` 保留英文原题，属专有名词保留，按规范不改。
- 已修正：无（未改动 `zh.json`）。
- 重跑 `build_index.py` 四项校验：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
