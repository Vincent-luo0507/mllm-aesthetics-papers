# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 295（文本 123 / 原子 172）|
| 已译文本块 | 123 / 123 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 21 · 已还原 21 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 187 |
| `<img>` 元素 | 67 |
| `<table>` 元素 | 11 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| UX critique / UX report | UX 评论 / UX 报告 | 按语境选用，报告指结构化产物 |
| actionability | 可操作性 | 全文统一，本文核心概念 |
| UX judge / judge model | UX 评判者 / 评判模型 | |
| interaction-grounded | 以交互为依据的 | 全文统一，不写作「交互驱动的」 |
| evidence-grounded | 以证据为依据的 | |
| report-conditioned repair | 以报告为条件的修复 | |
| repair lift / repair gain | 修复增益 | 全文统一 |
| repair agent | 修复智能体 | |
| fixture | 固定样例 | 全文统一，指本地可运行 Web 样例 |
| local-first | 本地优先 | |
| real anchor | 真实锚点 | |
| synthetic sibling | 合成兄弟样例 | |
| product surface / surface family / category | 产品界面 / 界面族 / 类别 | 按层级区分 |
| coverage gate / coverage-gated | 覆盖率门控 / 受覆盖率门控的 | |
| trajectory | 轨迹 | |
| prescan | 预扫描 | |
| exploration plan | 探索计划 | |
| viewport | 视口 | |
| state transition | 状态转移 | |
| recovery path | 恢复路径 | |
| rubric | 量规 | 评分量规，全文统一 |
| rubric dimension | 评分维度 | |
| pairwise win rate | 成对胜率 | |
| blind human validation | 盲态人工验证 | |
| bootstrap confidence interval | 自助置信区间 | |
| effect size | 效应量 | |
| Wilcoxon signed-rank | Wilcoxon 符号秩 | |
| scanability | 可扫读性 | |
| information architecture (IA) | 信息架构 | |
| accessibility (A11y) | 可访问性 | |
| goal-state clarity | 目标状态清晰度 | |
| trust/consequence transparency | 信任／后果透明度 | |

### 交叉验证记录

| 块 id | 原文要点 | 译文 | 语义一致性 |
|---|---|---|---|
| b0012 | 预扫描→计划→观察—行动闭环；覆盖率门控防过早终止；七维报告；固定修复智能体保持品牌与交互语义 | 模型先预扫描固定样例，形成探索计划，然后反复观察渲染出的页面、采取类用户动作……覆盖率门控防止过早终止……覆盖七个评分维度……在保持原有产品意图、品牌识别与交互语义的前提下编辑固定样例 | 一致，未增删内容 |
| b0037 | 四阶段流程，分别对应 ⟦SLOT_0⟧–⟦SLOT_3⟧ | 一次 UXBench 运行分四个阶段推进：⟦SLOT_0⟧ 评判智能体执行一次轻量预扫描……⟦SLOT_3⟧ 该报告被一个固定的代码编辑智能体消费 | 一致，4 个占位符顺序与原文一致 |
| b0087 | 41 个固定样例：11 真实锚点 + 30 合成兄弟；可访问性暴露面分离最明显；跨页面耦合不分离 | UXBench 含 41 个固定样例：11 个真实锚点与 30 个合成兄弟样例……最明显的分离出现在可访问性暴露面上……跨页面耦合并没有把真实与合成样例清楚区分开 | 一致，数值原样保留 |
| b0096 | GPT-5.4 最大增益 +0.22，Gemini-3.1-Pro 最小 +0.14，1–5 尺度上 0.08 分差距 | GPT-5.4 取得最大的修复增益（+0.22），Gemini-3.1-Pro 最小（+0.14），在 1–5 量规尺度上形成 0.08 分的差距 | 一致 |
| b0278 | 报告的配对 ⟦SLOT_11⟧ 检验、Wilcoxon 符号秩 ⟦SLOT_12⟧ 值、配对 Cohen's ⟦SLOT_13⟧ | 我们报告配对的 ⟦SLOT_11⟧ 检验与 Wilcoxon 符号秩 ⟦SLOT_12⟧ 值，以及作为效应量度量的配对 Cohen's ⟦SLOT_13⟧ | 一致，3 个占位符原样保留 |

### 一致性与数字核查

- 术语：全文统一使用「以交互为依据的」「以证据为依据的」「固定样例」「修复增益」「合成兄弟样例」「真实锚点」「量规」「可操作性」；`UXBench`、`Claude Code`、`GPT-5.4`、`GPT-5.4-Mini`、`GPT-5.4-Nano`、`Claude-Sonnet-4.6`、`Gemini-3.1-Pro`、`Kimi-K2.5`、`GLM-5.1`、`Qwen-3.6-Plus`、`SUS`、`UEQ`、`PSSUQ`、`SUPR-Q`、`UMUX-Lite`、`SEQ`、`ASQ`、`CES`、`NASA-TLX`、`A11y`、`IA` 等专名与量表缩写一律原样保留。
- 数字与指标：41、11、30、10、7、8、6、1–5、+0.22、+0.14、0.08、0.57、0.5 等数值，以及 Spearman's ρ / Kendall's τ_b / Cohen's d_z 等统计量名均原样保留，未作换算或改动。
- 占位符：逐块脚本比对，`⟦SLOT_0⟧`–`⟦SLOT_20⟧` 共 21 处，译文与原文在编号、数量与出现顺序上完全一致；构建脚本 `stray=0`。
- 编码：`zh.json` 与 `index.html` 均不含 U+FFFD；构建脚本 `mojibake=0`。
- 不变量：算法块（math）、表格、SVG 图形与参考文献块未翻译；123 个 text 块一一对应，未做合并或拆分。

### 遗留问题

- 无图片缺失（`missing_img=0`）。
- 原文 b0270 称「图 6 中的人工成对矩阵」，但根据图注，图 6 为自动化成对胜率矩阵、图 9 为人工成对胜率矩阵，疑为原文笔误；译文按原文保留为「图 6」，未作推测修改。
- 原文 b0087「UXBench contains 41fixtures」与 b0029「Figure 2provides」、b0285「Table 8and Table 9」、b0286「Table 10compares」均为缺少空格的排版瑕疵，译文按中文标点规范处理为「41 个固定样例」「图 2 给出了」「表 8 与表 9」「表 10 在模型层面」，未改动源文件。
- 原文 b0262 中「The evaluation instructions is shown」主谓不一致，译文按语义正常表达，未作额外说明。

## 复核记录（第二轮交叉验证）

复核人：Agent 01 · 方法：随机抽样 6 块逐句 EN/ZH 对照 + 全文槽位/数字/脚注残留自动比对

抽查 6 块（b0294、b0110、b0010、b0006、b0041、b0260），未发现实质错误。另对全文所有文本块做了槽位—数字—脚注残留三项自动比对，亦无异常。本次未修改 zh.json。
修正后已重跑 `build_index.py`，四项校验（missing / stray / mojibake / missing_img）均为 0。
