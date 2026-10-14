# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 204（文本 117 / 原子 87）|
| 已译文本块 | 117 / 117 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 144 · 已还原 144 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 316 |
| `<img>` 元素 | 83 |
| `<table>` 元素 | 23 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| diffusion model | 扩散模型 | 全文统一 |
| text-to-image (T2I) | 文生图 | 全文统一，不写作「文本到图像」 |
| preference alignment | 偏好对齐 | |
| personalized preference | 个性化偏好 | |
| multi-reward optimization | 多奖励优化 | |
| reinforcement learning from human feedback (RLHF) | 人类反馈强化学习 | 首次出现附英文缩写 |
| direct preference optimization (DPO) | 直接偏好优化 | 保留 DPO 缩写 |
| vision-language model (VLM) | 视觉语言模型 | |
| user embedding | 用户嵌入 | |
| user profile | 用户画像 | |
| user identifier / user ID | 用户标识 / 用户 ID | |
| cross-attention | 交叉注意力 | |
| decoupled cross-attention | 解耦交叉注意力 | IP-Adapter 机制名 |
| Bradley-Terry model | Bradley-Terry 模型 | 专有模型名不译 |
| evidence lower bound (ELBO) | 证据下界 | |
| KL-divergence | KL 散度 | |
| signal-to-noise ratio | 信噪比 | |
| chain-of-thought (COT) | 思维链 | 首次出现附 COT |
| few-shot | 少样本 | |
| in-context examples | 上下文示例 | |
| one-hot encoding | one-hot 编码 | |
| win rate | 胜率 | |
| interpolation | 插值 | |
| held-out | 留出 | 数据集划分用语 |
| reference model | 参考模型 | |
| reward function | 奖励函数 | |
| preference pair | 偏好对 | |
| denoiser | 去噪器 | |
| hyperparameter | 超参数 | |
| nucleus sampling | 核采样 | |

### 交叉验证记录

| 块 id | 原文要点 | 译文 | 语义一致性 |
|---|---|---|---|
| b0006 | Diffusion-DPO 只对齐群体层面单一奖励，逐人微调不可扩展，限制跨用户泛化 | 尽管结果喜人，Diffusion-DPO 只能让模型对齐单一奖励，而该奖励代表的是群体层面的人类偏好……并且可能削弱跨用户的泛化能力 | 一致，数字与引用编号未改动 |
| b0052 | one-hot 编码用户 ID 无法泛化到未见用户 | 一种朴素做法是用用户 ID 的 one-hot 编码表示嵌入 ⟦SLOT_65⟧……却有致命缺陷：无法泛化到未见的新用户 | 一致，5 个占位符顺序与原文一致 |
| b0083 | 30 步推理、PartiPrompts 1.6K 条、CLIP/Aesthetic/HPS 胜率 60%/90%/93% | 每种方法都用 30 步推理生成图像……在 CLIP、Aesthetic 与 HPS 上的胜率分别为 60%、90% 与 93% | 一致，数字原样保留 |
| b0098 | 已见用户 83%、未见用户 78%、全体 81% | PPD 在三种评测设定下均显著优于 Stable Cascade：已见用户胜率 83%，未见用户 78%，全体用户汇总为 81% | 一致 |
| b0187 | 150M 可训练参数、批大小 768、H100 80GB、8 卡、约 1000 步 / 2 小时 | 我们只优化新增的交叉注意力层，可训练参数共 150M……训练一个轮次（约 1000 次梯度更新）约需 2 小时 | 一致，单位与数值未改动 |

### 一致性与数字核查

- 术语：用脚本比对全文，「偏好对齐」「用户嵌入」「交叉注意力」「文生图」「奖励函数」「少样本」等核心术语译法统一，未出现同义轮换；`Diffusion-DPO`、`Stable Cascade`、`PartiPrompts`、`Pick-a-Pic`、`LLaVA-OneVision`、`IP-Adapter` 等专名一律原样保留。
- 数字与指标：76%、60%、90%、93%、83%、78%、81%、58K、0.8M、5K、4800、824、4341、192、277、150M、768、1632、1000 等数值，以及 CLIP / Aesthetic / HPS / PickScore 等指标名均原样保留，未作换算。
- 占位符：逐块脚本比对，`⟦SLOT_0⟧`–`⟦SLOT_143⟧` 共 144 处，译文与原文在编号、数量与出现顺序上完全一致；构建脚本 `stray=0`。
- 编码：`zh.json` 与 `index.html` 均不含 U+FFFD；构建脚本 `mojibake=0`。
- 不变量：表格、公式、图注标签、参考文献块未翻译；正文段落未做合并或拆分，117 个 text 块一一对应。

### 遗留问题

- 无图片缺失（`missing_img=0`）。
- 原文 b0072「We find ⟦SLOT_93⟧ for hyperparameter tuning.」一句语法欠完整，已按字面译为「我们为超参数调优寻找 ⟦SLOT_93⟧」，未作臆测补写。
- 原文 b0032、b0184 等处的公式符号经占位符还原，未改动任何 MathJax 标记。

## 复核记录（第二轮交叉验证）

- 抽查块（8 块，随机种子 7 与 42）：b0083、b0054、b0100、b0007、b0052、b0076、b0085、b0053
- 全篇自动化校验：逐块比对 EN/ZH 的 `⟦SLOT_n⟧` 占位符编号与顺序、数字/量级一致性，未发现丢失、错位或篡改。
- 抽查 8 块，未发现实质错误。
- 重跑 `build_index.py` 后四项校验：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
