# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 277（文本 140 / 原子 137）|
| 已译文本块 | 140 / 140 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 139 · 已还原 139 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 333 |
| `<img>` 元素 | 19 |
| `<table>` 元素 | 35 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| Group Relative Policy Optimization (GRPO) | 组相对策略优化（GRPO） | 核心算法，保留缩写 |
| rectified flow | 整流流 | 全文统一，不作"矫正流" |
| diffusion model | 扩散模型 | — |
| Markov Decision Process (MDP) | 马尔可夫决策过程（MDP） | 采样过程的形式化 |
| Stochastic / Ordinary Differential Equation (SDE / ODE) | 随机 / 常微分方程（SDE / ODE） | 缩写保留 |
| Reinforcement Learning from Human Feedback (RLHF) | 基于人类反馈的强化学习（RLHF） | — |
| policy gradient | 策略梯度 | — |
| advantage function | 优势函数 | 多奖励聚合时聚合的是优势函数 |
| KL-regularization | KL 正则项 | 默认省略 |
| rollout | 轨迹采样 | 与 trajectory（轨迹）配合 |
| reward hacking | 奖励破解 | 视频生成中的失败模式 |
| reward model | 奖励模型 | — |
| binary (0/1) reward | 二值（0/1）奖励 | 阈值化得到 |
| thresholding | 阈值化 | — |
| Best-of-N inference scaling | Best-of-N 推理扩展 | 保留原名 |
| Classifier-Free Guidance (CFG) | 无分类器引导（CFG） | — |
| timestep | 时间步 | 不写作"步长" |
| noise schedule | 噪声调度 | — |
| velocity / vector field | 速度 / 向量场 | 整流流术语 |
| denoising | 去噪 | — |
| foundation model | 基础模型 | 四个基座模型 |
| text-to-image / text-to-video / image-to-video (T2I / T2V / I2V) | 文本到图像 / 文本到视频 / 图像到视频（T2I / T2V / I2V） | — |
| stochastic interpolant | 随机插值（stochastic interpolant） | 附录理论框架 |
| Score-Based Diffusion Model (SBDM) | 基于分数的扩散模型（SBDM） | — |
| Brownian motion | 布朗运动 | — |
| Dirac delta distribution | 狄拉克 delta 分布 | — |
| VRAM | 显存 | — |
| moving average | 滑动平均 | 奖励曲线绘制方式 |
| UNet / VAE / CLIP / VLM / Qwen-VL | 同名保留 | 模型与组件名 |
| HPS-v2.1 / CLIP score / VideoAlign / GenEval / Pick-a-Pic | 同名保留 | 基准与奖励名 |

### 交叉验证记录

| 块 id | 原文要点 | 本文译文 | 一致性判断 |
|---|---|---|---|
| b0015 | 扩散过程在时间步 ⟦SLOT_1⟧ 上逐步破坏数据点 ⟦SLOT_0⟧ | 两槽位原样保留，顺序照原文 | 一致 |
| b0031 | ⟦SLOT_27⟧ 提示词、⟦SLOT_28⟧ 转移概率、⟦SLOT_33⟧ 个时间步、⟦SLOT_35⟧ 奖励模型 | 九个槽位逐一保留，CLIP/Qwen-VL 保留 | 一致 |
| b0093 | HPS 从 0.239 升至 0.365，CLIP Score 从 0.363 升至 0.395 | 四个数值原样，未做四舍五入 | 一致 |
| b0104 | Videoscore 不稳定；Visionreward-Video 为 29 维指标；视觉质量与运动质量相对提升 56% 与 181% | 维度数与两个百分比原样保留 | 一致 |
| b0233 | 比较式（17）与式（20）中布朗运动项 ⟦SLOT_129⟧ 的系数，推导 ⟦SLOT_134⟧ | 九个槽位全部保留，式号照原文 | 一致 |

### 一致性与数字核查

- 术语统一性：`rectified flow` 全文统一为"整流流"；`timestep` 统一为"时间步"；`advantage` 统一为"优势"；`rollout` 统一为"轨迹采样"；`reward hacking` 统一为"奖励破解"；未出现同义轮换。
- 数字核查：181%、56%、118%、0.239/0.365/0.363/0.395、0.28、0.39、0.23/0.33、480×480、10,000、1,000/240/200、32/8/64 块 H800 GPU、50/25 步、40%、30%、60%、0.3 等数值与单位均逐字核对，未做换算。
- 占位符核查：139 个 `⟦SLOT_n⟧` 槽位在译文中数量与编号完全一致，构建脚本报告 stray = 0。
- 编码核查：`zh.json` 与 `index.html` 均不含 U+FFFD。
- 公式块、算法块与表格按规范跳过未译；作者与项目链接块仅译说明文字，URL 与 LaTeX 命令原样保留。

### 遗留问题

- 无图片缺失（missing_img = 0）。
- 原文 b0242 写"in three key aspects"却列出四条，译文保留原文的"三个关键方面"并如实列出四项。
- 原文多处引用"Table 3.1"（如表 3.1）而本文并无 3.1 号表，疑为笔误，译文按字面保留。
- 原文 b0114 "Futhermore"、b0240 "Morever" 为拼写笔误，译文按语义处理，不影响内容。

## 复核记录（第二轮交叉验证）

- 复核人：独立复核团队 03 号 Agent
- 抽查块数：**12**（随机种子 3 取 6 块 + 种子 7 取 6 块）
- 抽查块 ID：`b0019`、`b0190`、`b0099`、`b0116`、`b0248`、`b0260`（种子 3）；`b0035`、`b0205`、`b0194`、`b0022`、`b0188`、`b0038`（种子 7）

### 结构核验

- `index.html` 含 `tex-mml-chtml.js`，MathJax 已加载。
- 图片 `src` 全部为 `figures/...` 本地相对路径，无 `http` 外链。
- 无 U+FFFD 乱码；顶部有中文标题与中文摘要，底部有「返回总目录」链接。
- 重跑 `build_index.py`：`missing`、`stray`、`mojibake`、`missing_img` 四项**全为 0**。

### 发现与修正

| 块 ID | 问题类型 | 修正前 | 修正后 |
|---|---|---|---|
| `b0188` | 中文质量（生造词） | 本文**连用到**一类特殊的随机插值 | 本文**关联到**一类特殊的随机插值 |

修正后已重跑 `build_index.py`，四项校验仍全为 0。

### 其他说明

- 全文存在 6 处 `⟦SLOT_n⟧` 顺序与 EN 不一致（`b0015`、`b0017`、`b0022`、`b0038`、`b0192`、`b0219`），均为中文语序自然调整所致，且每个占位符与其所指（数据点/时间步/模型/输出、阈值与被约束量等）绑定正确，语义无偏差，**判定为非错误，未作改动**。
