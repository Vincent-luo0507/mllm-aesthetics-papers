# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 251（文本 155 / 原子 96）|
| 已译文本块 | 155 / 155 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 1 · 已还原 1 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 28 |
| `<img>` 元素 | 15 |
| `<table>` 元素 | 8 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| Multimodal Large Language Model (MLLM) | 多模态大语言模型（MLLM） | 首次出现附英文缩写，后文用 MLLM |
| UI/UX design | UI/UX 设计 | 全文保留斜杠写法，不拆译 |
| A/B test | A/B 测试 | 保留字母标记 |
| winning variant / winner | 胜出变体 / 胜出方案 | 指 A/B 测试中表现更优的 UI |
| key interpretation | 关键解读 | 指专家撰写的解释性标注 |
| post-hoc | 事后 | post-hoc interpretation 作「事后解读」 |
| selection task | 选择任务 | 任务 1 |
| interpretation task | 解读任务 | 任务 2 |
| perception / memory / action | 感知 / 记忆 / 行动 | Norman（2007）的三个 UX 认知维度 |
| UX law | UX 定律 | 12 条经遴选的定律 |
| position bias | 位置偏置 | 成对比较中的已知问题 |
| First Accuracy (FA) | 首位准确率（FA） | |
| Second Accuracy (SA) | 次位准确率（SA） | |
| Average Accuracy (AA) | 平均准确率（AA） | |
| Consistent Accuracy (CA) | 一致准确率（CA） | 与顺序无关的指标 |
| Interpretation Recall | 解读召回率 | |
| Instance-level Recall | 实例级召回率 | |
| Interactive Control (IC) | 交互控件（IC） | 元素功能分组之一 |
| Content & State Display (CSD) | 内容与状态展示（CSD） | |
| Container & Layout Structure (CLS) | 容器与布局结构（CLS） | |
| Contrastive Chain-of-Thought (CoCoT) | 对比式思维链（CoCoT） | 推理策略 |
| Duty-Distinct Chain-of-Thought (DDCoT) | 职责分离式思维链（DDCoT） | |
| Multi-Agent Debate (MAD) | 多智能体辩论（MAD） | R1 / R3 保留 |
| inpainting | 图像修复 | 用于移除视觉指示标记 |
| token | 词元 | |
| abductive reasoning | 溯因推理 | |
| persona-based agent | 基于人物角色的智能体 | |
| landing page | 落地页 | 与 homepage（主页）区分 |

### 交叉验证记录

| 块 id | 原文要点 | 译文 | 一致性确认 |
|---|---|---|---|
| b0012 | 300 对真实 UI 图像、684 条专家关键解读、三个认知维度（感知/记忆/行动） | 全部保留，维度名与括号释义一一对应 | 数量与结构一致，未增删 |
| b0039 | 三位专家独立标注；至少两方一致才保留；845 条候选中得 684 条（562 三方一致、122 两方一致）；12 条 UX 定律 | 逐项保留 845 / 684 / 562 / 122 / 12 | 数字与筛选规则一致 |
| b0056 | FA / SA / AA / CA 四项定义；随机猜测 CA 为 25%（每顺序 50%） | 四项缩写与定义完整译出，25% 与 50% 原样保留 | 指标定义与数值一致 |
| b0074 | 解读召回率与实例级召回率定义；GPT-4o 评估器；1,000 样本、83.0%、Cohen’s kappa 0.66 | 保留 1,000 / 83.0% / 0.66 及 BLEU、ROUGE、METEOR、BERTScore 原名 | 指标名与验证数据一致 |
| b0213 | Table 6: Overview of Token Counts (⟦SLOT_0⟧) | 「表 6：WiserUI-Bench 上 UI/UX 设计选择任务的词元数量（⟦SLOT_0⟧）概览。」 | 占位符原样保留 |

### 一致性与数字核查

- 术语统一性：回扫确认「关键解读」「胜出方案/胜出变体」「事后解读」「位置偏置」「UI/UX 设计」等核心术语全文译法唯一；FA/SA/AA/CA 与 IC/CSD/CLS 等缩写均首次出现时给出中文全称并附英文缩写，后文保持一致。
- 数字与指标：300 / 684 / 562 / 122 / 845 / 12 / 11 / 13 / 2 / 1.53 / 1.99 / 19 / 14 / 2.28 / 50% / 25% / 70% / 7B / 8B / 30B-A3B / 32B / 38B / 83.0% / 0.66 / 1,000 / 225 / 48 / 0.2 / 4.53.2 / 0.9.2 / 48GB 等全部原样保留；模型名 o1、GPT-5.1、GPT-4o、Claude 4.5 Sonnet、Claude 3.5 Sonnet、Qwen3-VL、Qwen2.5-VL、InternVL-2.5、LLaVA-NeXT-7B、LLaVA-OneVision-7B 与数据集名 RICO 均保留原文。
- 占位符：全文 1 处 ⟦SLOT_0⟧（b0213），译文中数量与编号与原文一致；b0195 正文提及表 6 处原文无占位符，译文未添加。构建脚本 `stray` 为 0。
- 编码：`zh.json` 与 `index.html` 均不含 U+FFFD。
- 未改动 `blocks.json` / `translate_input.json` / `orig.html`。

### 遗留问题

- b0175、b0177 中的 API 参数说明（reasoning effort: none、thinking type: disabled）属配置项取值，译文以「推理强度：none」「思考类型：禁用」处理，保留参数语义而未改动取值本身。
- b0197 中 AS / CS 的原文表述（total correct、both correct cases）较为简略，译文按字面处理为「总正确数」与「两次均正确情形」，未作推测性扩展。
- 图片文件引用缺失为 0，无图片下载需求。


## 复核记录（第二轮交叉验证）

- 复核人：Agent 02（独立复核，非译者）
- 结构核验：MathJax（`tex-mml-chtml.js`）已加载；15 处图片 `src` 全部为 `figures/` 本地相对路径，无 http 外链；无 U+FFFD；顶部中文标题与中文摘要齐备，底部有「返回总目录」链接。
- 抽查块：b0166、b0213、b0163、b0041、b0205、b0202（seed=2）；加抽 b0023、b0027、b0042、b0202（seed=7）
- 另复核短译文块 b0050（455→113 字符，第二项任务定义完整，无漏译）。
- 判定：上述全部抽查块在完整性（无漏译跳句）、准确性（无错译、无因果/否定/数量颠倒）、数字与符号（模型名/数据集名/指标名/百分数原样一致）、公式占位符（`⟦SLOT_n⟧` 集合与顺序全篇逐块机器比对一致）、术语一致性、中文通顺度六项上均通过，**抽查未发现实质错误，未作任何修改**。
- 构建产物校验：`index.html` 四项校验（missing / stray / mojibake / missing_img）均为 0，本次未改动 `zh.json`，未重跑构建。
