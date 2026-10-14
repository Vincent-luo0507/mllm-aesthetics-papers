# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 358（文本 219 / 原子 139）|
| 已译文本块 | 219 / 219 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 201 · 已还原 201 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 524 |
| `<img>` 元素 | 27 |
| `<table>` 元素 | 6 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| Direct Reward Fine-Tuning (DRaFT) | 直接奖励微调 | 方法名，保留缩写 DRaFT |
| differentiable reward | 可微奖励 | |
| reward fine-tuning | 奖励微调 | |
| backpropagation through sampling | 贯穿采样的反向传播 | 指沿采样链求导 |
| truncated backpropagation | 截断反向传播 | DRaFT-K 的核心机制 |
| gradient checkpointing | 梯度检查点 | 保留 @jax.checkpoint 原样 |
| low-rank adaptation (LoRA) | 低秩适配 | 保留 LoRA 缩写 |
| latent diffusion model | 潜变量扩散模型 | |
| denoising / denoiser | 去噪 / 去噪器 | |
| classifier-free guidance (CFG) | 无分类器引导 | guidance weight 译「引导权重」 |
| sampling chain / trajectory | 采样链 / 轨迹 | |
| noise schedule | 噪声调度 | |
| reward model | 奖励模型 | |
| human preference | 人类偏好 | |
| reward hacking | 奖励破解 | 指模型钻奖励漏洞 |
| over-optimization | 过度优化 | |
| over-generalization | 过度泛化 | |
| sample efficiency | 样本效率 | |
| exploding gradient | 梯度爆炸 | |
| gradient clipping | 梯度裁剪 | |
| stop-gradient / stop_grad | 停止梯度 | 保留 stop_grad 原样标识符 |
| policy gradient | 策略梯度 | |
| deterministic policy gradient (DPG) | 确定性策略梯度 | |
| critic | 评论家 | RL 语境 |
| re-ranking (best of 16) | 重排序（Best of 16） | |
| prompt engineering | 提示词工程 | |
| aesthetic predictor / classifier | 美学预测器 / 分类器 | LAION Aesthetics 相关 |
| interpolability / interpolation | 插值 | LoRA 权重插值 |
| incompressibility | 不可压缩性 | |
| adversarial example | 对抗样本 | |
| NSFW / SFW | NSFW / SFW | 保留原文缩写 |
| uncurated samples | 未筛选样本 | |
| guidance schedule | 引导调度 | |

### 交叉验证记录

| id | 原文要点 | 译文 | 语义一致性 |
|---|---|---|---|
| b0009 | 介绍 DRaFT（贯穿整条采样链反向传播）、梯度检查点 + LoRA、DRaFT-K 只对最后 K 步求导、DRaFT-LV 多噪声样本降方差 | 逐条对应，保留 ⟦SLOT_0⟧、⟦SLOT_1⟧ | 一致 |
| b0066 | 截断反向传播降低每步计算量并提升每步训练效率；K 小时不需要梯度检查点 | 完整译出，保留 ⟦SLOT_42⟧–⟦SLOT_45⟧ | 一致 |
| b0091 | DRaFT-1 略优于 ReFL；DRaFT-LV 最优、比 DRaFT-1 快约 ⟦SLOT_62⟧；小 K 在时间与效果上均更优 | 逐项对应，保留 ⟦SLOT_62⟧–⟦SLOT_65⟧ | 一致 |
| b0114 | JPEG 可压缩性：可微压缩/解压、最小化原始与重建图像的欧氏距离、取负得不可压缩 | 完整译出，保留 ⟦SLOT_85⟧–⟦SLOT_89⟧ | 一致 |
| b0291 | 两种提升多样性尝试：dropout 0.95 仍坍缩；LPIPS 多样性项以美学得分为代价 | 数值 0.95 原样保留，保留 ⟦SLOT_152⟧–⟦SLOT_154⟧ | 一致 |

### 一致性与数字核查

- 术语统一性已用 Grep 复核：DRaFT / DRaFT-K / DRaFT-LV、LoRA、奖励模型、潜变量、无分类器引导、采样链、奖励破解、过度优化等全文译法唯一。
- 全部数字原样保留：学习率 4e-4 / 2e-4、批大小 4 / 16、训练步数 2k / 10k、LoRA 内维 8 / 32、权重衰减 0.1、DDIM 步数 50、引导权重 7.5、dropout 0.95、LoRA 缩放 0.75、TPUv4 数量 4 / 16、DDPO 奖励 7.4 与 50k 查询、bfloat16 / float32 等均未改动。
- 占位符核查：本文 SLOT 编号从 0 连续到 200，共 201 处；译文中逐一原样保留，未被删除、改写或翻译。脚本校验 `stray=0`、`missing=0`。
- 编码核查：`zh.json` 与 `index.html` 中不含 `�`（U+FFFD），脚本 `mojibake=0`。

### 遗留问题

- 无。图片文件齐全（`missing_img=0`），公式槽位全部还原。

## 复核记录（第二轮交叉验证）

- 复核人：独立复核 Agent 08 号
- 抽查方式：`sample_blocks.py` 两轮随机抽样（种子 8 与 2024）+ 全量脚本化交叉校验（数字/公式占位符/未译块/长度比）
- 抽查块（共 12 块次）：b0218, b0234, b0124, b0221, b0282, b0300 / b0234, b0205, b0279, b0221, b0311, b0355
- 结论：共记录 2 条核验事项，逐条判定如下。

| 块 ID | 问题类型 | 复核发现 | 判定与处理 |
|---|---|---|---|
| b0076, b0082, b0336 | 数字一致性复核 | 脚本检出 EN 中 50k / 10k / 3D 在 ZH 中无逐字对应 | ZH 分别译为「5 万次奖励查询」「1 万步」「三维模型」，数值等价、读法正确，未修改。 |
| b0037, b0039, b0065, b0067, b0208, b0348 | 短块语种复核 | ZH 仅含 DRaFT／LoRA／ReFL 等专有名词 | EN 原文即为纯方法名词块，按规范保留英文专名，未修改。 |

- 其中标注「未修改」者为经核对后确认**非错误**（中文语序换位、等值数字改写、规范要求的英文专名保留），按规格书 §2「避免过度修改」不予改动。
- 重跑 `build_index.py`：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
