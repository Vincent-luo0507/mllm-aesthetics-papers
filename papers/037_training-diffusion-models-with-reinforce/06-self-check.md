# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 293（文本 155 / 原子 138）|
| 已译文本块 | 155 / 155 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 115 · 已还原 115 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 236 |
| `<img>` 元素 | 247 |
| `<table>` 元素 | 15 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| denoising diffusion policy optimization (DDPO) | 去噪扩散策略优化（DDPO） | 本文核心算法，首次出现括注英文 |
| reward-weighted regression (RWR) | 奖励加权回归（RWR） | 对照方法 |
| diffusion probabilistic model | 扩散概率模型 | |
| denoising / denoising process | 去噪 / 去噪过程 | |
| log-likelihood | 对数似然 | |
| variational lower bound / variational bound | 变分下界 / 变分界 | |
| Markov decision process (MDP) | 马尔可夫决策过程（MDP） | |
| policy gradient | 策略梯度 | |
| score function estimator | 得分函数估计器 | DDPO_SF |
| importance sampling estimator | 重要性采样估计器 | DDPO_IS |
| trust region | 信任域 | |
| proximal policy optimization (PPO) | 近端策略优化（PPO） | |
| trajectory | 轨迹 | |
| transition kernel | 转移核 | |
| absorbing termination state | 吸收性终止状态 | |
| Dirac delta distribution | Dirac delta 分布 | 分布名不译 |
| isotropic Gaussian | 各向同性高斯 | |
| reward function / reward query | 奖励函数 / 奖励查询 | |
| compressibility / incompressibility | 可压缩性 / 不可压缩性 | |
| aesthetic quality | 美学质量 | |
| prompt-image alignment | 提示词-图像对齐 | 亦简作「图文对齐」，两处含义相同 |
| vision-language model (VLM) | 视觉语言模型（VLM） | |
| RLAIF | RLAIF | 不译 |
| overoptimization | 过度优化 | |
| reward exploitation | 奖励利用 | 与 overoptimization 配套 |
| typographic attack | 排版攻击 | |
| classifier guidance | 分类器引导 | |
| classifier-free guidance (CFG) | 无分类器引导（CFG） | |
| universal guidance | 通用引导 | |
| low-rank adaptation (LoRA) | 低秩适配（LoRA） | |
| guidance weight | 引导权重 | |
| on-policy / off-policy | 同策略 / 异策略 | |
| value function baseline | 值函数基线 | |
| advantage-weighted regression (AWR) | 优势加权回归 | |
| clip range | 裁剪范围 | |
| minibatch | 小批量 | |
| checkpoint | 检查点 | |
| inverse temperature | 逆温度 | |

### 交叉验证记录

| 块 id | 原文要点 | 译文要点 | 一致性 |
|---|---|---|---|
| b0067 | 分辨率固定 512x512；可压缩性最小化 JPEG 后文件大小，不可压缩性最大化 | 分辨率与两个任务的定义、比较方向均逐字对应 | 一致 |
| b0069 | LAION 美学预测器、176,000 条人类评分、CLIP 嵌入之上的线性模型、分值 1–10 | 四个数值与模型名原样保留，评分范围未改动 | 一致 |
| b0082 | Stable Diffusion v1.4 基础模型；398 种动物；45 种常见动物 | 模型版本与两组数量一一对应 | 一致 |
| b0213 | 25k 次奖励查询内出现过度优化；20k 次查询时图像质量仍高；用 ImageReward 训练、LAION 评估 | 三个数量与两组模型/指标名均对应，因果关系未颠倒 | 一致 |
| b0232 | 每轮 256 个样本；4 个小批量 4 次更新；裁剪范围 1e-4 | 数值与学习率记法原样保留，⟦SLOT_188–190⟧ 未丢失 | 一致 |

### 一致性与数字核查

- 术语一致性：用 Grep 在 `zh.json` 中检索「去噪」「策略梯度」「奖励加权回归」「马尔可夫决策过程」「提示词-图像对齐」「视觉语言模型」「过度优化」「无分类器引导」「同策略 / 异策略」等核心术语，确认全文译法唯一，未出现同义轮换。
- 数字与指标：所有数量（176,000、398、45、50、256、10,000、20k、25k、50k 等）、分辨率（512x512）、学习率（3e-4）、裁剪范围（1e-4）、耗时（2 分钟 / 4 秒 / 4 小时）、硬件型号（v3-128、v4-64 TPU pod、80Gb A100）均原样保留；模型与工具名（Stable Diffusion v1.4/v1-5、LLaVA、CLIP、BERTScore、ImageReward、LAION aesthetics predictor、UNet、LoRA、JAX、Flax、NumPy 等）未做任何改动。
- 占位符完整性：写入前逐块比对原文与译文的 `⟦SLOT_n⟧` 列表，slot 18–210 全部一一对应；脚本校验 `⟦SLOT⟧` 残留为 0。
- 编码：`zh.json` 与 `index.html` 均不含 U+FFFD，脚本 mojibake 计数为 0。
- 不变量：参考文献、公式、SVG、表格（`t:"keep"`）一律未翻译；正文块一块对一块，未合并或拆分。

### 遗留问题

- b0093 与 b0097 为图内坐标轴 / 图例标签，内容几乎全部由 `⟦SLOT_n⟧` 占位符与提示词片段构成，无自然语言成分，故按原文保留。
- 原文 b0203 中的「universal guidance11 1」为脚注标记解析残留，译文按原文形式保留。
- 本页 `img` 计数较高（247），原因是原文大量图像以 SVG/内联形式存在；脚本报告 `missing_img = 0`，无图片缺失。

- 术语统一说明：`prompt-image alignment` 全文统一译为「提示词-图像对齐」，图题中的简写「图文对齐」已在复核后一并改为完整译法，避免同义轮换。

## 复核记录（第二轮交叉验证）

- 抽查块（9 块，随机种子 7 与 42）：b0027、b0242、b0073、b0203、b0071、b0206、b0069、b0056、b0030
- 全篇自动化校验：逐块比对 EN/ZH 的 `⟦SLOT_n⟧` 占位符编号与顺序、数字/量级一致性，未发现丢失、错位或篡改。
- 抽查 9 块，未发现实质错误。
- 重跑 `build_index.py` 后四项校验：`missing=0`、`stray=0`、`mojibake=0`、`missing_img=0`。
