# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 285（文本 168 / 原子 117）|
| 已译文本块 | 168 / 168 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 43 · 已还原 43 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 118 |
| `<img>` 元素 | 7 |
| `<table>` 元素 | 26 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| VisionReward | VisionReward | 系统名不译 |
| visual generation / visual generative model | 视觉生成 / 视觉生成模型 | |
| text-to-image (T2I) | 文本到图像 | 全文统一，不写作「文生图」 |
| text-to-video | 文本到视频 | |
| reinforcement learning from human feedback (RLHF) | 人类反馈强化学习（RLHF） | 首次出现括注 |
| reward model (RM) | 奖励模型（RM） | |
| interpretability | 可解释性 | |
| fine-grained | 细粒度 | |
| multi-dimensional | 多维度 | |
| dimension / sub-dimension | 维度 / 子维度 | |
| binary question / binary visual QA | 二值问题 / 二值视觉问答 | |
| checklist | 检查清单 | 标注体系中的问答清单 |
| linear weighting | 线性加权 | |
| logistic regression | 逻辑回归 | |
| weight masking | 权重掩码 | |
| Multi-Dimensional Preference Optimization (MPO) | 多维度偏好优化（MPO） | |
| Direct Preference Optimization (DPO) | 直接偏好优化（DPO） | |
| dominate | 支配 | MPO 中的样本对筛选关系，全文统一 |
| preference accuracy | 偏好准确率 | |
| pairwise win rate | 成对胜率 | |
| Vision-Language Model (VLM) | 视觉语言模型（VLM） | |
| multimodal LLM (MLLM) | 多模态大语言模型 | |
| annotator | 标注者 | 统一，不混用「标注员」 |
| consistency | 一致性 | 标注者一致率与判断一致性均用此译法 |
| checkpoint | 检查点 | |
| warmup | 预热 | |
| threshold | 阈值 | |
| baseline | 基线 | |
| foundation / base model | 基础模型 | |
| frame-level | 帧级 | |
| MonetBench | MonetBench | 基准名不译 |

### 交叉验证记录

| 块 id | 原文要点 | 译文要点 | 一致性 |
|---|---|---|---|
| b0014 | 九个主要维度、64 个细粒度问题、线性加权机制 | 数字 9 / 64 原样保留，两步训练流程表述对应 | 一致 |
| b0039 | 48k 图像、10k 提示词、30k+3k=33k 视频，含 Rouge-L、UniFL、ChatGPT 等工具名 | 全部数量与工具名原样保留，采样与过滤顺序未变 | 一致 |
| b0078 | GenAI-Bench 2 秒视频下图像 RM 有竞争力；MonetBench 6 秒下 VisionReward 提升 22.1%，为其他最佳 12.5% 的两倍 | 时间长度与四个百分比数值逐一对齐 | 一致 |
| b0083 | 22,000 样本、每提示词 4 个视频、9,400 个偏好对、批大小 32、学习率 5e-6、DPO 参数 500 | 数值与学习率记法（5e-6）原样保留，⟦SLOT_31⟧ 占位符未丢失 | 一致 |
| b0209 | 63,165 条提示词、1.76M 图文对、760k/770k/780k 对比样本对及各自唯一提示词数 | 六组数量与三组对照方法（MPO / HPSv2 / Pick-a-Pic v2）均对应无误 | 一致 |

### 一致性与数字核查

- 术语一致性：用 Grep 在 `zh.json` 中检索「文本到图像」「文本到视频」「奖励模型」「细粒度」「多维度」「二值问题」「标注者」「支配」「偏好准确率」「可解释性」「视觉语言模型」等核心术语，确认全文同一种译法，未出现同义轮换。
- 数字与指标：所有数量（48k、81K、5M、1.76M、760k 等）、学习率（1e-6、4e-6、2e-6、5e-6、5e-9）、阈值（0.8、0.6、0.5、0.4、0.9、0.0015）、准确率与相关系数均原样保留；模型名（CogVLM2、CogVLM2-Video、CogVideoX-2B/5B、SDXL、VideoCrafter2、OpenSora、GPT-4o、Gemini、VQAScore、LLaVA 等）、数据集名（HPDv2、Pick-a-Pic、ImageRewardDB、VidProM、Panda-70M、VBench、MonetBench、DrawBench、GenAI-Bench）、指标名（tau、diff、Spearman、CLIP、LAION-Aesthetic）均未改动。
- 占位符完整性：写入前逐块比对原文与译文的 `⟦SLOT_n⟧` 列表，slot 0–42 全部一一对应；脚本校验 `⟦SLOT⟧` 残留为 0。
- 编码：`zh.json` 与 `index.html` 均不含 U+FFFD，脚本 mojibake 计数为 0。
- 不变量：参考文献、`t:"keep"` 的表格与公式一律未翻译；正文块一块对一块，未合并或拆分。

### 遗留问题

- b0247、b0249、b0251、b0253 四个块在 `translate_input.json` 中被标记为 `t:"text"`，但其内容是论文表 15–18（文本到图像 / 文本到视频的标注分类体系与检查清单）的逐行展开，属于表格数据而非论述性文本。依据规格书 §3 第 3 条「表格一律不翻译」，这四个块保留英文原文，对应的表题（b0248、b0250、b0252、b0254）已完整译为中文。
- b0065 与 b0197 同样是表 2、表 10 的展开内容，已按可读方式译出其中的分组与维度名称，模型名与数值原样保留。
- 无图片缺失（missing_img = 0）。

## 复核记录（第二轮交叉验证）

- 抽查块（8 块，随机种子 7 与 42）：b0041、b0209、b0027、b0066、b0070、b0248、b0025、b0098
- 全篇自动化校验：逐块比对 EN/ZH 的 `⟦SLOT_n⟧` 占位符编号与顺序、数字/量级一致性，未发现丢失、错位或篡改。
- 抽查 8 块，未发现实质错误。
- 重跑 `build_index.py` 后四项校验：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
