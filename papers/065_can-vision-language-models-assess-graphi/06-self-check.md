# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 509（文本 489 / 原子 20）|
| 已译文本块 | 489 / 489 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 0 · 已还原 0 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 0 |
| `<img>` 元素 | 20 |
| `<table>` 元素 | 0 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| graphic design | 平面设计 | 全文统一 |
| aesthetic quality assessment | 美学质量评估 | 统一译法 |
| design aesthetics assessment | 设计美学评估 | 与 image aesthetics assessment 对举 |
| image aesthetics assessment | 图像美学评估 | |
| vision-language model (VLM) | 视觉语言模型（VLM） | 首次出现括注缩写 |
| dimension | 维度 | 指 layout/font/color/graphics 四个大类 |
| indicator | 指标 | 指十二项细分指标，全文统一 |
| typography / font | 字体排版 / 字体 | 维度名统一用「字体」 |
| layout | 版式 | 不用「布局」，与 UI 语境区分 |
| color | 色彩 | |
| graphics | 图形 | |
| balance | 平衡 | 指标名固定 |
| layering | 层次 | |
| whitespace | 留白 | |
| alignment | 对齐 | |
| harmony | 和谐 | |
| contrast | 对比 | |
| appeal | 吸引力 | |
| psychology | 心理 | 原文表格中拼作 psycholoy，按语义译「心理」 |
| legibility | 易读性 | |
| hierarchy | 层级 | |
| quality | 质量 | |
| relevance | 相关性 | |
| aesthetic judgment | 审美判断 | 三项任务之一 |
| region selection | 区域选择 | |
| precise localization | 精确定位 | |
| bounding box (bbox) | 边界框（bbox） | 首次出现括注缩写 |
| intersection over union (IoU) | 交并比（IoU） | |
| reasoning-augmented VLM | 推理增强型 VLM | |
| human-guided VLM labeling | 人类引导的 VLM 标注 | |
| indicator-grounded reasoning | 指标锚定推理 | |
| reasoning path | 推理路径 | |
| perturbation | 扰动 | 数据构建中的操作 |
| human-in-the-loop | 人在环路 | |
| metadata | 元数据 | |
| full-parameter finetuning | 全参数微调 | |
| out-of-distribution (OOD) | 分布外（OOD） | |
| ablation study | 消融研究 | |
| baseline | 基线 | |

### 交叉验证记录

| 块 id | 原文要点 | 译文要点 | 一致性 |
|---|---|---|---|
| b0018 | 四维度（typography/layout/color/graphics）、十二指标、三项任务（judgment / selection / localization） | 四个维度、十二项指标、审美判断／区域选择／精确定位 | 一致，任务名与数字未改动 |
| b0059 | 从 Crello 测试划分采样 1200 件设计；答案分别为 yes/no、四选一索引、bbox 或 None | 1200 件设计，三类答案形式 | 一致，1200 原样保留 |
| b0133 | 选择题部分最佳 0.6090；bbox 部分 GPT-5 低于 0.20 | 最佳模型总体分数 0.6090；GPT-5 低于 0.20 | 一致 |
| b0227 | +AesEval-Train 提升 5.97%；−推理路径 0.6576；−正样本 0.2072 | 同样数值，仅把行首标签译为「−推理路径／−正样本」 | 一致，所有数字未改动 |
| b0400/b0401 | McNemar 检验 p=0.004 与 p<0.001；配对 t 检验 t=4.82、p<0.01 | 数值与检验名原样保留 | 一致 |

### 一致性与数字核查

- 全文术语已统一：indicator→指标、dimension→维度、layout→版式、bbox→边界框、IoU→交并比、perturbation→扰动、reasoning path→推理路径，未出现同义轮换。
- 数字与指标逐一核对：1200、1500、4500、30k、4.5k、∼10k、∼6k、∼1.6k、∼2k、∼3k、1e-6、3%、32B/72B/7B/13B/8B/14B、0.7252、0.6090、0.20、5.97%、2.70%、17.17%、p=0.004、p<0.001、t=4.82、p<0.01 等均原样保留。
- 表格中的模型名与指标名（LLaVA-13B、Qwen-VL-7B/32B/72B、Intern-VL3-8B/14B、GPT-4o、GPT-5、GPT-o1、GPT-o3、Gemini-2.5-Pro、AesExpert、UNIAA-LLaVA、AesBench、UNIAA-Bench、DesignBench、DesignProbe、UI-Bench、UICrit、Crello 等）全部保留原文。
- 占位符核查：本篇 `translate_input.json` 中未出现 `⟦SLOT_n⟧` 占位符，脚本报告 stray = 0。
- 编码核查：`zh.json` 与 `index.html` 均不含 U+FFFD。
- 参考文献条目（b0243–b0349）按规范「参考文献不翻译」处理，逐条保留原文；作者块与 arXiv 页眉同样保留原文。
- 图表中的纯数值刻度、表格数值行、指标轴标签等非叙述性内容照原样保留，仅把指标名与图例文字译为中文。

### 遗留问题

- 原文表格中指标名 “psycholoy” 疑为 “psychology” 的拼写错误，译文按语义处理为「心理」，未改动原文数值与排版。
- 原文算法 1 为伪代码块，译文保留全部符号与公式，仅把说明性注释（如 {Shift position}）译为中文。
- 图片引用缺失数为 0；本篇未检测到公式元素（math = 0），与原文排版一致。

## 复核记录（第二轮交叉验证）

- 复核人：独立复核团队 03 号 Agent
- 抽查块数：**12**（随机种子 3 取 6 块 + 种子 7 取 6 块）
- 抽查块 ID：`b0044`、`b0323`、`b0080`、`b0243`、`b0330`、`b0026`（种子 3）；`b0017`、`b0362`、`b0292`、`b0083`、`b0403`、`b0077`（种子 7）

### 结构核验

- `index.html` 含 `tex-mml-chtml.js`，MathJax 已加载。
- 图片 `src` 全部为 `figures/...` 本地相对路径，无 `http` 外链。
- 无 U+FFFD 乱码；顶部有中文标题与中文摘要，底部有「返回总目录」链接。
- 重跑 `build_index.py`：`missing`、`stray`、`mojibake`、`missing_img` 四项**全为 0**。

### 发现与修正

抽查 12 块，**未发现实质错误**（无漏译整句、无错译关键结论、数字与指标未被改动、`⟦SLOT_n⟧` 占位符编号与顺序完整、术语译法篇内统一）。

### 其他说明

- 该篇有 32 个长文本块（`b0094`–`b0105` 等）为纯数值表体，ZH 与 EN 完全相同。按规范「表格数据保留原文」处理，未译，属正确做法。
