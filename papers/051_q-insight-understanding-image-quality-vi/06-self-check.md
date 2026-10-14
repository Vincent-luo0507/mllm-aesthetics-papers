# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 184（文本 82 / 原子 102）|
| 已译文本块 | 82 / 82 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 108 · 已还原 108 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 232 |
| `<img>` 元素 | 9 |
| `<table>` 元素 | 15 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| image quality assessment (IQA) | 图像质量评估（IQA） | 首次出现括注缩写 |
| multi-modal large language model (MLLM) | 多模态大语言模型（MLLM） | 与 048 篇的 LMM 区分，本文统一用 MLLM |
| group relative policy optimization (GRPO) | 组相对策略优化（GRPO） | 全文统一 |
| score regression | 分数回归 | 任务名统一 |
| degradation perception | 退化感知 | 任务名统一，不轮换为「失真感知」 |
| distortion perception | 失真感知 | 章节名，与 degradation perception 区别对待 |
| comparison reasoning | 比较推理 | |
| mean opinion score (MOS) | 平均意见分数（MOS） | |
| score-based / description-based methods | 基于分数的方法 / 基于描述的方法 | 两类方法对举 |
| supervised fine-tuning (SFT) | 监督微调（SFT） | |
| out-of-distribution (OOD) | 分布外（OOD） | 统一 |
| in-the-wild | 真实场景 | |
| full-reference / no-reference | 全参考 / 无参考 | IQA 传统二分 |
| policy model / reference model | 策略模型 / 参考模型 | |
| old policy / new policy | 旧策略 / 新策略 | |
| advantage | 优势 | RL 术语 |
| KL divergence | KL 散度 | |
| verifiable score reward | 可验证分数奖励 | |
| degradation classification reward | 退化分类奖励 | |
| intensity perception reward | 强度感知奖励 | |
| format reward | 格式奖励 | |
| binary reward | 二值奖励 | |
| zero-shot generalization | 零样本泛化 | |
| PLCC (Pearson linear correlation coefficient) | 皮尔逊线性相关系数（PLCC） | 首次出现给出全称 |
| SRCC (Spearman rank-order correlation coefficient) | 斯皮尔曼秩相关系数（SRCC） | |
| super-resolution (SR) | 超分辨率（SR） | |
| AI-generated content (AIGC) | AI 生成内容（AIGC） | |
| low-level vision | 低层视觉 | |
| threshold | 阈值 | |
| ablation study | 消融研究 / 消融实验 | 依语境统一为「消融研究」「消融实验」各自所在章节内一致 |
| baseline | 基线 | |
| state-of-the-art | 最优（方法） | |

### 交叉验证记录

| 块 id | 原文要点 | 译文要点 | 一致性 |
|---|---|---|---|
| b0008 | GRPO 三点优势：不依赖海量文本数据、对 OOD 图像强泛化、支持多任务多样性 | 同样三点优势，表述顺序一致 | 一致，未增删 |
| b0031 | 用 MOS 作为指引而非直接拟合；受 DeepSeek-R1 启发采用二值奖励 | 译文同样说明 MOS 作为一般指引、采用二值奖励 | 一致 |
| b0043 | 五类失真 noise/blur/JPEG/darken/null，五个等级 slight/moderate/obvious/serious/catastrophic | 类别与等级名原样保留，共五类五级 | 一致 |
| b0071 | 从 DiffIQA 采样 5k 对；A-Fine 使用 200k+ 对，数据量超 40 倍 | 5k 对、200k 余对、超过 40 倍 | 一致，数字未改动 |
| b0167 | SRIQA-Bench 含 100 张 LR 参考图、10 种 SR 方法、每对至少 10 名标注者 | 100 张、10 种、至少 10 名 | 一致 |

### 一致性与数字核查

- 全文术语已统一：IQA→图像质量评估、MLLM→多模态大语言模型、GRPO→组相对策略优化、degradation perception→退化感知、score regression→分数回归、OOD→分布外、in-the-wild→真实场景，未出现同义轮换。
- 数字与指标逐一核对：7B、5k、200k、180k、100、10、5（失真类别数）、5（严重等级数）、16（A100 GPU）、40（倍）等均原样保留；PLCC、SRCC、Reg-Acc、Gen-Acc、Deg. Acc.、Lev. Acc. 等指标名未改动。
- 模型名与数据集名（Q-Insight、Qwen-2.5-VL-7B-Instruct、DeepSeek-R1、Q-Align、DeQA-Score、DepictQA、DepictQA-Wild、AgenticIR、A-Fine、C2Score、KonIQ、SPAQ、LIVE-Wild、KADID、CSIQ、PIPAL、AGIQA、DQ-495K、DiffIQA、SRIQA-Bench、TID2013 等）全部保留原文。
- 标签与占位符：`<think>`、`</think>`、`<answer>`、`</answer>`、`{`、`}` 标记原样保留；`⟦SLOT_0⟧`—`⟦SLOT_107⟧` 在译文中逐一原样保留，脚本报告 stray = 0。
- 编码核查：`zh.json` 与 `index.html` 均不含 U+FFFD。
- 表格、公式、图片与参考文献块按规范跳过未译。

### 遗留问题

- 无。图片引用缺失数为 0，公式与表格均正常还原。

## 复核记录（第二轮交叉验证）

抽查块：b0175、b0021、b0067、b0161、b0034、b0049


- **发现问题数**：0
- **已修正数**：0

判定依据：逐块对照 EN/ZH，完整性（无漏译跳句）、准确性（方法名/指标名/因果关系/否定/数量均无误）、
数字与符号（数值、百分比、模型名、数据集名、指标名原样一致）、公式占位符（`⟦SLOT_n⟧` 编号与数量
一致，随其指称成分一并移位属正常）、术语一致性、中文质量（通顺、无生造词、无明显 AI 腔）六项均未
见实质错误。另经全量脚本核查：占位符集合一致、无缺失译文块。

结构核验：MathJax 已加载；图片均为 `figures/` 本地相对路径、无 http 外链；无 U+FFFD；
顶部含中文标题与中文摘要；底部含「返回总目录」链接。重跑 `build_index.py` 后
`missing / stray / mojibake / missing_img` 四项均为 0。
