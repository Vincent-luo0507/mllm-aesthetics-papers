# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 280（文本 169 / 原子 111）|
| 已译文本块 | 169 / 169 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 15 · 已还原 15 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 30 |
| `<img>` 元素 | 16 |
| `<table>` 元素 | 37 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| reward model (RM) | 奖励模型 | 全文统一，不译作「回报模型」 |
| omni model | 全模态模型 | 指可交错处理图文的理解/生成一体模型 |
| preference pair | 偏好对 | 由提示词 + 优选响应 + 淘汰响应构成 |
| chosen / rejected response | 被选中的 / 被拒绝的响应 | §3 中成对数据的两个成员 |
| judge / MLLM-as-a-judge | 评判器 / 以多模态大模型充当评判器 | 全文统一用「评判器」 |
| judge-human agreement | 评判器—人类一致率 | 带百分比时译「一致率」 |
| text-to-image | 文生图 | 任务名统一 |
| image editing | 图像编辑 | |
| interleaved generation | 交错生成 | 图文交错序列生成 |
| multimodal reasoning | 多模态推理 | |
| thinking with images | 用图像思考 | 保留原文引号含义 |
| annotator | 标注者 | 不译「注释者」 |
| ensemble filtering | 集成过滤 | 多评判器投票过滤简单样本 |
| position bias | 位置偏差 | |
| positional consistent dual evaluation | 位置一致的双次评测 | 正序 + 逆序各评一次 |
| Likert scale | 李克特量表 | |
| test-time scaling | 测试时扩展 | |
| best-of-N sampling | Best-of-N 采样 | 保留 N 不译 |
| win rate | 胜率 | |
| same-model / different-model pair | 同源模型对 / 跨模型对 | |
| pointwise evaluation | 逐点评测 | 与「总体偏好」相对 |
| agent / sketchpad agent | 智能体 / sketchpad 智能体 | |
| prompt | 提示词 | |
| response | 响应 | |
| frontier model | 前沿模型 | |
| headroom | 提升空间 | |
| distribution shift | 分布偏移 | |
| capability boundary | 能力边界 | |
| inter-annotator agreement | 标注者间一致率 | |

### 交叉验证记录

| id | 原文要点 | 译文 | 语义一致性 |
|---|---|---|---|
| b0008 | 介绍 MMRB2 四项子任务、每任务 1000 组专家偏好对、21 个源任务、三项设计特征 | 完整译出四项子任务、1000 组、21 个源任务与三点设计特征 | 一致，数字（1000、21）未改动 |
| b0014 | Best-of-N 选择与 GenAI-Bench、GEdit-Bench、ISGBench、EMMA 的相关性 | 保留 Best-of-⟦SLOT_0⟧ 占位符与四个基准名 | 一致，占位符原样保留 |
| b0063 | EditReward +9.4%、UnifiedReward +9.4%/+1.4%、ImageReward 54.0、HPSv2 54.7、PickScore 58.6 | 逐项对应，含 ⟦SLOT_1⟧–⟦SLOT_3⟧ 三处箭头占位符 | 一致，全部百分比与增量数值未改 |
| b0078 | 混合模态偏好对中 GPT-5 88.2% vs 38.9%，差 49.3 个百分点；Gemini 2.5 Pro 27.7、Qwen3-VL-30BA3B 36.0、Gemini 3 Pro 17.9 | 数值与模型名逐个对应 | 一致 |
| b0214 | 生成图像整体质量的 4 点量表（0–3 各档标签与描述） | 完整翻译四档评分标签与描述 | 一致，评分数字与量表结构未改 |

### 一致性与数字核查

- 已用 Grep 在 `zh.json` 中核对核心术语：奖励模型、全模态模型、偏好对、评判器、交错生成、文生图、一致率、智能体等译法全文唯一，未出现同义词轮换。
- 全部数字、百分比、区间（如 74–80%、66–75%、27.7–49.3%、+9.4%）、美元与小时薪酬、模型名（Gemini 3 Pro、Qwen3-VL-32B、GPT-Image-1 等）、基准名（GenAI-Bench、ISGBench、EMMA 等）均原样保留，未做任何换算或改写。
- 占位符核查：原文 15 处 `⟦SLOT_n⟧`（b0014、b0063 ×3、b0068、b0069、b0081、b0082、b0083 ×6、b0194），译文中数量与编号逐一对应，未被删除或翻译。脚本校验 `stray=0`、`missing=0`。
- 编码核查：`zh.json` 与 `index.html` 中均不含 `�`（U+FFFD），脚本 `mojibake=0`。

### 遗留问题

- b0019 中原文存在一段明显为排版/提取错误的乱码字符串「mdiirhtdkltrnlldrnvhbccugtflukgivodels」（OmniVerifier 一句之后），已按原文原样保留，未作删改。
- 图片文件齐全（`missing_img=0`），无缺图。

## 复核记录（第二轮交叉验证）

- 复核 Agent：06 号（独立交叉验证）
- 结构核验：MathJax（`tex-mml-chtml.js`）已加载；图片 `src` 全部为 `figures/...` 本地相对路径、无 http 外链；全文无 U+FFFD 乱码；顶部有中文标题与中文摘要，底部有「返回总目录」链接 —— 全部通过。
- 抽查块（10 块）：b0007、b0257、b0267、b0033、b0024、b0246、b0054、b0265、b0041、b0071
- 逐块比对 EN/ZH 的六项判读：完整性（无漏译整句/跳句）、准确性（无错译、无因果或否定反转）、数字与符号（数字、百分比、模型名、数据集名、指标名与原样一致）、公式占位符（`⟦SLOT_n⟧` 编号与顺序完全一致）、术语一致性（同篇内译法统一）、中文质量（通顺、无生造词、无 AI 腔堆砌）—— **未发现实质错误**。
- 附加机器校验：全篇文本块无缺失译文；每块占位符数量与顺序逐一比对一致；数字差分扫描命中的差异经人工核对均为中英数量表达差异（如 `4.8 million` → 「480 万」、`7.6B` → 「76 亿」、`10,073` → 「10,073」），非错译。
另注：章节标题 `3 Multimodal RewardBench 2` 保留英文原题，其余章节均已译为中文，属专有名词保留，按规范不改。
- 已修正：无（未改动 `zh.json`）。
- 重跑 `build_index.py` 四项校验：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
