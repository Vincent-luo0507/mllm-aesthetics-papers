# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 180（文本 104 / 原子 76）|
| 已译文本块 | 104 / 104 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 38 · 已还原 38 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 129 |
| `<img>` 元素 | 6 |
| `<table>` 元素 | 18 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| Large Multi-modality Model (LMM) | 大模态模型（LMM） | 全文统一，不译「多模态大模型」 |
| visual scoring | 视觉评分 | 统一译法 |
| syllabus | 教学方案 | 指训练 LMM 的课程设计，首次出现括注原词语境 |
| text-defined rating level | 文本定义的评分等级 | 核心概念，统一不轮换 |
| mean opinion score (MOS) | 平均意见分数（MOS） | 首次出现括注缩写 |
| image quality assessment (IQA) | 图像质量评估（IQA） | 三项任务统一格式 |
| image aesthetic assessment (IAA) | 图像美学评估（IAA） | |
| video quality assessment (VQA) | 视频质量评估（VQA） | 注意与 Visual Question Answering 缩写冲突，本文语境为质量评估 |
| out-of-distribution (OOD) | 分布外（OOD） | 统一 |
| in-the-wild | 真实场景 | 指自然拍摄数据，不译「野外」 |
| cross-dataset / cross-set | 跨数据集 | 统一 |
| intra-dataset | 数据集内 | 与 cross-dataset 对举 |
| visual assessor | 视觉评估器 | |
| rating level | 评分等级 | 不译「评级」以免与 rating 歧义 |
| qualitative adjective | 定性形容词 | |
| equidistant interval partition | 等距区间划分 | |
| close-set softmax | 闭集 softmax | |
| softmax pooling | softmax 池化 | |
| visual abstractor | 视觉抽象器 | mPLUG-Owl-2 中的模块名 |
| supervised fine-tuning (SFT) | 监督微调（SFT） | |
| visual instruction tuning | 视觉指令微调 | |
| logits | logits | 不译，保留原文 |
| log probability | 对数概率 | |
| FewShot-Q-Align | FewShot-Q-Align | 少样本变体名保留原文 |
| OneAlign | OneAlign | 统一模型名保留原文 |
| state-of-the-art | 最优 | 视语境译作「最优（方法）」或「现有最优方法」 |
| SRCC / PLCC | SRCC / PLCC | 指标名原样保留 |
| OOM | 显存溢出（OOM） | 首次括注说明 |
| latency / throughput | 延迟 / 吞吐量 | |
| epoch | 轮次 | 统一，不译「纪元」 |
| ensemble | 集成 | |
| ablation study | 消融实验 | |
| baseline | 基线 | |

### 交叉验证记录

| 块 id | 原文要点 | 译文要点 | 一致性 |
|---|---|---|---|
| b0012 | 人类标注者从不学习或标注具体分数，如 [1,5] 区间内的 3.457 | 人类标注者从不学习或标注具体分数（如 [1,5] 区间内的 3.457） | 一致，数值原样保留 |
| b0016 | 仅需 1/5（IQA）或 1/10（IAA）数据即可竞争 | 1/5（IQA）乃至 1/10（IAA）的数据 | 一致 |
| b0070 | 视觉抽象器把每幅图像词元数降至 64；LLaMA2 上下文下可输入 30 幅图像（无抽象器为 2 幅） | 词元数降至 64，最多同时输入 30 幅图像（不使用抽象器则仅为 2 幅） | 一致，数字未改动 |
| b0101 | 相对 LIQE 提升 7%、Aesthetic Predictor 提升 10%、VILA 提升 6%；FewShot 用 10% AVA | 各项百分比与 10% 数据设定相同 | 一致 |
| b0125 | 第二高等级显示 (B) 美感介于 fair 与 poor、质量介于 poor 与 bad；不会对非相邻等级预测前二 | 译文中等级名保留原文，语义一致 | 一致，占位符 SLOT_37 保留 |

### 一致性与数字核查

- 全文术语已统一：LMM→大模态模型、rating level→评分等级、MOS→平均意见分数、in-the-wild→真实场景、cross-dataset→跨数据集、epoch→轮次，未出现同义轮换。
- 数字与指标逐一核对：1168、0.95、64、30、2、1fps、236K、19K、28K、11K、1.1K、12（数据集数）、20%、10%、7%、6%、1%、40%、9（分钟）、23、4.2、1.9、5s、12s 等均原样保留；SRCC、PLCC、OOM、MOS、IQA/IAA/VQA 等指标与缩写未改动。
- 模型名与数据集名（Q-Align、OneAlign、mPLUG-Owl-2、LLaMA2、CLIP、CLIP-IQA+、LIQE、MUSIQ、NIMA、DBCNN、HyperIQA、VILA、DOVER、FAST-VQA、KonIQ-10k、SPAQ、KADID-10k、AVA、LSVQ、KoNViD-1k、MaxWell、AGIQA-3K、LIVE、CSIQ 等）全部保留原文。
- 占位符核查：`⟦SLOT_0⟧`—`⟦SLOT_37⟧` 在译文中逐一原样保留，编号未改写；脚本报告 stray = 0。
- 编码核查：`zh.json` 与 `index.html` 均不含 U+FFFD。
- 表格、公式、图片与参考文献块按规范跳过未译；对话模板中的 `<img>`、`<level>`、`#User:`、`#Assistant:` 标记原样保留。

### 遗留问题

- b0116 原文写作 “In Tab. 10 and Tab. 10”，疑为笔误（按上下文应为表 9 与表 10）。译文按原文忠实译作“表 10 与表 10”，未擅自改动编号，特此记录。
- b0029 中引用 “DisCoVQA（Wu 等，）” 年份缺失，系原文如此，译文保留原样。
- 图片引用缺失数为 0，公式与表格均正常还原。

## 复核记录（第二轮交叉验证）

- 复核人：Agent 02（独立复核，非译者）
- 结构核验：MathJax（`tex-mml-chtml.js`）已加载；6 处图片 `src` 全部为 `figures/` 本地相对路径，无 http 外链；无 U+FFFD；顶部中文标题与中文摘要齐备，底部有「返回总目录」链接。
- 抽查块：b0110、b0005、b0081、b0097、b0062、b0018（seed=2）；加抽 b0105、b0071、b0051、b0031（seed=7）
- 判定：上述全部抽查块在完整性（无漏译跳句）、准确性（无错译、无因果/否定/数量颠倒）、数字与符号（模型名/数据集名/指标名/百分数原样一致）、公式占位符（`⟦SLOT_n⟧` 集合与顺序全篇逐块机器比对一致）、术语一致性、中文通顺度六项上均通过，**抽查未发现实质错误，未作任何修改**。
- 构建产物校验：`index.html` 四项校验（missing / stray / mojibake / missing_img）均为 0，本次未改动 `zh.json`，未重跑构建。
