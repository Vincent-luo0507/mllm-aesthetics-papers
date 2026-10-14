# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 204（文本 123 / 原子 81）|
| 已译文本块 | 123 / 123 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 102 · 已还原 102 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 251 |
| `<img>` 元素 | 4 |
| `<table>` 元素 | 13 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| diffusion model | 扩散模型 | |
| reward overoptimization | 奖励过优化 | 全文统一，与 reward hacking 区分 |
| reward hacking | 奖励破解 | 仅在 b0019 作为别名出现 |
| inductive bias | 归纳偏置 | |
| temporal inductive bias | 时序归纳偏置 | 本文首个成因 |
| primacy bias | 首因偏置 | 本文第二个成因 |
| temporal critic | 时序评论家 | critic 首次出现时括注 |
| temporal reward | 时序奖励 | 依赖时间步的奖励 |
| active neuron | 活跃神经元 | 反映首因偏置 |
| dormant neuron | 休眠神经元 | 起自适应正则化作用 |
| plasticity loss | 可塑性丧失 | 首因偏置的上位概念 |
| cross-reward generalization | 跨奖励泛化 | 本文新提出的量化指标 |
| sample efficiency | 样本效率 | |
| policy gradient | 策略梯度 | TDPO-R 所属类别 |
| denoising | 去噪 | |
| per-timestep gradient update | 逐时间步梯度更新 | 与逐批更新对举 |
| trajectory | 轨迹 | |
| Markov Decision Process (MDP) | 马尔可夫决策过程（MDP） | |
| importance sampling | 重要性采样 | |
| early stopping | 早停 | 对比策略之一 |
| KL regularization | KL 正则化 | 对比策略之二 |
| LoRA (Low-Rank Adaptation) | 低秩适配（LoRA） | 首次括注 |
| Multi-Layer Perceptron (MLP) | 多层感知机（MLP） | 时序评论家的轻量头 |
| encoder alignment | 编码器对齐 | 附录 E 主题 |
| catastrophic forgetting | 灾难性遗忘 | 策略活跃神经元重置的后果 |
| replay buffer | 回放缓冲区 | 未来工作方向 |
| Aesthetic Score | Aesthetic Score | 基准奖励名，保留原名 |
| HPSv2 / PickScore / ImageReward | HPSv2 / PickScore / ImageReward | 奖励／评测模型名保留 |
| Stable Diffusion v1.4 | Stable Diffusion v1.4 | 基础模型 |
| DDPO / AlignProp | DDPO / AlignProp | 基线方法名保留 |
| classifier-free guidance (CFG) | 无分类器引导（CFG） | 附录 F |

### 交叉验证记录

| 块 id | 原文要点 | 本文译文 | 一致性 |
|---|---|---|---|
| b0009 | 时序归纳偏置错配：现有方法只用最终图像奖励，忽视序贯本性与中间信息，导致过拟合与错位 | 因果链与“期望结果 vs 实际质量”的错位表述完整 | 一致 |
| b0010 | 首因偏置定义；Sokar 等认为休眠神经元有害，本文发现相反 | 两组结论的对比关系保留，未颠倒 | 一致 |
| b0083 | 重置休眠神经元降低休眠百分比却加剧过优化；与 Sokar 等 2023 结论相左 | 反转关系明确译出 | 一致 |
| b0173 | DDPO 复现：更新频率 100、学习率 1e-4、梯度累积 16⟦SLOT_102⟧→16、⟦SLOT_103⟧ 默认 50、8 张 A100 40GB | 数字与占位符顺序一致 | 一致，无换算 |
| b0206 | 时序评论家 MLP 五层维度 1024、128、64、16、1；编码器复用与显存优势 | 五个维度数字原样保留 | 一致 |

### 一致性与数字核查

- 术语：复核 zh.json，奖励过优化、归纳偏置、时序归纳偏置、首因偏置、时序评论家、活跃／休眠神经元、跨奖励泛化、样本效率等核心术语全文译法唯一。
- 数字：42、7 ⟦SLOT⟧ 0.1、45、802、100、2、16、50、1e-4、8、4、40GB、5、1024、128、64、16、1、0、0.1、100% 等均未改动。
- 占位符：脚本逐块比对 `⟦SLOT_1⟧`–`⟦SLOT_105⟧` 共 102 处，修订 b0007、b0023、b0025、b0028、b0035、b0038、b0042、b0048、b0055 九处顺序后完全一致，stray=0。
- 编码：zh.json 与 index.html 均不含 U+FFFD。

### 遗留问题

- 无缺失图片（missing_img=0）。
- b0213 原文仅为“3334”，系页码残留，按规范译为“（原文此处不可解析）”。
- b0097 与 b0173 含脚注／上标残留（如“11 1”“16⟦SLOT_102⟧”），已按上下文并入正文，未改动数字。


## 复核记录（第二轮交叉验证）

复核人：Agent 01 · 方法：随机抽样 6 块逐句 EN/ZH 对照 + 全文槽位/数字/脚注残留自动比对

抽查 6 块（b0098、b0028、b0055、b0011、b0008、b0042），未发现实质错误。另对全文所有文本块做了槽位—数字—脚注残留三项自动比对，亦无异常。本次未修改 zh.json。
修正后已重跑 `build_index.py`，四项校验（missing / stray / mojibake / missing_img）均为 0。
