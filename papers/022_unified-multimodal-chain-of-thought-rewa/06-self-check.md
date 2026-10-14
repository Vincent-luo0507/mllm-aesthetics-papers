# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 180（文本 112 / 原子 68）|
| 已译文本块 | 112 / 112 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 29 · 已还原 29 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 64 |
| `<img>` 元素 | 8 |
| `<table>` 元素 | 13 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| multimodal reward model (RM) | 多模态奖励模型（RM） | 首次出现附缩写 |
| Chain-of-Thought (CoT) | 思维链（CoT） | 全文统一，长链形式译为「长链 CoT 推理」 |
| long-chain reasoning | 长链推理 | 与短/浅层推理相对 |
| Visual-Language Model (VLM) | 视觉语言模型（VLM） | 首次出现附缩写 |
| supervised fine-tuning (SFT) | 监督微调（SFT） | 通用术语 |
| reinforcement fine-tuning (RFT) | 强化微调 | 全文统一，不译作「强化学习微调」 |
| cold start | 冷启动 | 训练第一阶段 |
| rejection sampling | 拒绝采样 | 训练第二阶段 |
| Group Relative Policy Optimization (GRPO) | 组相对策略优化（GRPO） | 首次出现附英文全称 |
| verifiable reward | 可验证奖励 | 含格式奖励与准确率奖励 |
| format reward | 格式奖励 | 全文统一 |
| accuracy reward | 准确率奖励 | 与 accuracy（准确率）呼应 |
| policy model | 策略模型 | 强化学习术语 |
| reference model | 参考模型 | 强化学习术语 |
| advantage | 优势 | 强化学习术语 |
| KL divergence | KL 散度 | 不译 Kullback-Leibler 全称 |
| ground truth (GT) | 真值（GT） | 首次出现附 GT |
| distillation | 蒸馏 | 从 GPT-4o 蒸馏推理过程 |
| implicit reasoning | 隐式推理 | 与显式 CoT 推理相对 |
| base model / backbone | 基座模型 / 骨干网络 | 二者分别固定，不混用 |
| visual understanding / generation | 视觉理解 / 视觉生成 | 全文成对出现 |
| reward signal | 奖励信号 | 全文统一 |
| tie case | 平局情形 | “Tau”/“Diff”指标语境 |
| pointwise / pairwise evaluation | 逐点评估 / 成对评估 | 评测方式 |
| ablation | 消融 | 通用术语 |
| Generalization | 泛化 | 通用术语 |

### 交叉验证记录

| 块 id | 原文要点 | 译文要点 | 一致性 |
|---|---|---|---|
| b0008 | 三阶段流程（Cold Start / Rejection Sampling / GRPO）、可验证奖励、多维度打分策略 | 三阶段名称与顺序完整对应，GRPO 全称首现附英文 | 一致，无漏译、未添加原文没有的解释 |
| b0025 | 冷启动用 GPT-4o 蒸馏；保留最终答案与 GT 一致的轨迹，记为 ⟦SLOT_0⟧，x 为原始输入，⟦SLOT_1⟧ 为蒸馏输出 | 三个占位符原样保留，GT 缩写保留 | 一致 |
| b0059 | HPD 25.6K、OIP 7.4K、EvalMuse 3K、OpenAI-4o_t2i_human_preference 6.7K、VideoDPO 10K、Text2Video 5.7K、LLaVA-Critic-113K 采样 30K、ShareGPTVideo-DPO 17K | 数据集名与规模数字全部原样保留，脚注编号 1、2 保留 | 一致，未换算 |
| b0061 | 批大小 1、16 步梯度累积、学习率 ⟦SLOT_25⟧、预热 0.3、8×H100(80GB)；GRPO 学习率 ⟦SLOT_26⟧、KL 系数 ⟦SLOT_27⟧、⟦SLOT_28⟧=8、64×H20(97GB) | 数字与四个占位符全部保留，GPU 型号与显存原样 | 一致 |
| b0165 | “Tau”面向平局情形、“Diff”排除平局；基线在平局上更强，本文在 Diff 上更优 | 两个指标名与引号原样保留，因果论述完整 | 一致 |

### 一致性与数字核查

- 术语统一：用 Grep 在 `zh.json` 中检索「多模态奖励模型」「思维链」「冷启动」「拒绝采样」「组相对策略优化」「可验证奖励」「格式奖励」「准确率奖励」「策略模型」「参考模型」「真值」「隐式推理」「基座模型」「骨干网络」等核心术语，全文译法唯一；缩写 CoT / VLM / SFT / GRPO / GT / RM 均原样保留。
- 数字核查：数据规模（25.6K / 7.4K / 3K / 6.7K / 10K / 5.7K / 30K / 17K / 137k / 37.6K / 182K / 26.5k / 1,250 / 10K / 5K / 3K）、超参数（批大小 1、16 步、0.3、8、64、8×H100、64×H20）与指标名（Tau / Diff / Overall Quality）均未改动或换算。
- 占位符完整性：脚本统计内联槽位 29、已还原 29；另用脚本逐块比对 112 个文本块的 `⟦SLOT_n⟧` 集合，全部一致。
- 编码检查：`zh.json` 与 `index.html` 中 U+FFFD 计数均为 0，编码 UTF-8。
- 不变量：表格、公式、图片、参考文献块一律未翻译；未删减、合并或拆分段落，一块对一块。

### 遗留问题

- 无。图片引用缺失 0，公式元素 64 个均正常还原，未发现原文乱码或不可解析的块。

## 复核记录（第二轮交叉验证）

复核人：Agent 01 · 方法：随机抽样 6 块逐句 EN/ZH 对照 + 全文槽位/数字/脚注残留自动比对

抽样 6 块（b0148、b0129、b0014、b0013、b0157、b0152）语义、数字、术语均无误。另对全文所有文本块做了槽位—数字—脚注残留三项自动比对，发现并修正 3 处：

| 块 ID | 问题类型 | 修正前 → 修正后 |
|---|---|---|
| b0046 | 公式占位符错位 | `⟦SLOT_15⟧ 采样 ⟦SLOT_13⟧…⟦SLOT_14⟧`（顺序 15/13/14/16，与 EN 的 13/14/15/16 不一致） → `采样 ⟦SLOT_13⟧ 个不同回答 ⟦SLOT_14⟧，它们来自先前的策略模型 ⟦SLOT_15⟧`（顺序恢复为 13/14/15/16）|
| b0059 | 脚注标记残留 | `OIP（7.4K）11 1 https://…open-image-preferences-v1-binarized`  → `OIP（7.4K）（https://…open-image-preferences-v1-binarized）`|
| b0059 | 脚注标记残留 | `OpenAI-4o_t2i_human_preference（6.7K）22 2 https://huggingface.co/datasets/Rapidata`  → `OpenAI-4o_t2i_human_preference（6.7K）（https://huggingface.co/datasets/Rapidata）`|

修正后已重跑 `build_index.py`，四项校验（missing / stray / mojibake / missing_img）均为 0。
