# 06 · 自检报告（自动部分）

| 校验项 | 结果 |
|---|---|
| 段落块总数 | 330（文本 188 / 原子 142）|
| 已译文本块 | 188 / 188 |
| 缺失译文块 | 0  |
| 内联公式/图片槽位 | 总数 97 · 已还原 97 |
| `⟦SLOT⟧` 残留（应为 0）| 0 |
| `<math>` 元素 | 242 |
| `<img>` 元素 | 13 |
| `<table>` 元素 | 39 |
| 图片文件引用缺失 | 0  |
| 乱码字符 U+FFFD（应为 0）| 0 |
| 文件编码 | UTF-8 |

## 译者补充

### 术语对照表

| English | 中文 | 说明 |
|---|---|---|
| flow matching | 流匹配 | 全文统一 |
| rectified flow | Rectified Flow | 框架名，保留英文 |
| ordinary differential equation (ODE) | 常微分方程 | 首次括注 ODE |
| stochastic differential equation (SDE) | 随机微分方程 | 首次括注 SDE |
| ODE-to-SDE conversion | ODE-to-SDE 转换 | 策略名保留连字符写法 |
| denoising reduction | 降噪步数缩减 | 策略名，首次括注英文 |
| velocity field | 速度场 | |
| score function | 分数函数 | |
| marginal distribution / density | 边缘分布／边缘概率密度 | |
| Wiener process increment | 维纳过程增量 | |
| Euler-Maruyama discretization | Euler-Maruyama 离散化 | 方法名不译 |
| Fokker–Planck equation | Fokker–Planck 方程 | 方程名不译 |
| reverse-time SDE | 逆时 SDE | |
| drift / diffusion coefficient | 漂移系数／扩散系数 | |
| Dirac delta distribution | 狄拉克 δ 分布 | |
| Markov Decision Process (MDP) | 马尔可夫决策过程 | |
| policy gradient | 策略梯度 | |
| advantage | 优势 | |
| group relative (GRPO) | 组内相对 | GRPO 缩写保留 |
| group size | 组大小 | |
| KL divergence / KL regularization | KL 散度／KL 正则化 | |
| reward hacking | 奖励黑客 | 领域通行译法 |
| rollout | rollout | 保留英文，RL 采样轨迹 |
| trajectory | 轨迹 | |
| text-to-image (T2I) generation | 文生图（T2I）生成 | 首次括注缩写 |
| compositional image generation | 组合式图像生成 | |
| visual text rendering | 视觉文字渲染 | |
| human preference alignment | 人类偏好对齐 | |
| verifiable reward | 可验证奖励 | |
| model-based reward | 基于模型的奖励 | |
| supervised fine-tuning (SFT) | 监督微调 | |
| reward weighted regression (RWR) | 奖励加权回归 | |
| direct preference optimization (DPO) | 直接偏好优化 | |
| early stopping | 早停 | |
| Dirichlet / isototropic Gaussian | 各向同性高斯分布 | |
| LoRA | LoRA | 保留原名 |
| PickScore / ImageReward / UnifiedReward / DeQA / Aesthetic Score | 同名保留 | 奖励模型与指标名不译 |

### 交叉验证记录

| 块 id | 原文要点 | 我的译文 | 一致性确认 |
|---|---|---|---|
| b0009 | GenEval 63%→95%，优于 GPT-4o；OCR 59%→92%；Pickscore；极少奖励黑客 | 四个百分比与基准名逐项对应 | 一致，未增删 |
| b0032 | MDP 五元组：状态 ⟦SLOT_8⟧、动作 ⟦SLOT_9⟧、策略 ⟦SLOT_10⟧、确定性转移 ⟦SLOT_11⟧、终局奖励 ⟦SLOT_15⟧/⟦SLOT_16⟧ | 槽位全部原样保留 | 一致 |
| b0060 | 训练时间步 ⟦SLOT_35⟧=⟦SLOT_36⟧，推理时间步 ⟦SLOT_37⟧ 保持默认 ⟦SLOT_38⟧ | 槽位与逻辑一致 | 一致 |
| b0099 | 噪声水平 0.1 限制探索；0.7 提升；0.7→1.0 无额外收益；过大导致零奖励与训练失败 | 数值与因果链一致 | 一致 |
| b0327 | 40 步 ODE／SDE 视觉上无法区分；10 步与 5 步引入颜色漂移与细节模糊；反而加速优化 | 同上 | 一致，未添加解释 |

### 一致性与数字核查

- 术语：全文统一「流匹配／速度场／降噪步数缩减／奖励黑客／优势／组大小／文生图／人类偏好对齐」，未做同义轮换；Flow-GRPO、GRPO、PPO、DDPO、ReFL、ORW、RWR、SFT、DPO、SD3.5-M、FLUX.1-Dev、GenEval、DrawBench、T2I-CompBench++、PickScore、ImageReward、UnifiedReward、DeQA、Aesthetic Score、LoRA、MDP、ODE、SDE、KL 等缩写与系统名一律原样保留。
- 占位符：逐块比对 `t:"text"` 块中 `⟦SLOT_n⟧` 集合与译文槽位集合，数量与编号完全一致（覆盖 ⟦SLOT_0⟧–⟦SLOT_96⟧）。
- 数字：63%、95%、59%、92%、T=10、40、10、5、0.04、0.01、512、24 块 A800、每 40 步、2 万条训练提示、1 千条测试提示、50 条 DrawBench 提示、64 幅／提示、Step 0/240/480/720/960、28.79→29.89、27.99/28.40/30.18、0.96/0.97/1.02、5.71/6.02 等均原样保留。
- 编码：`zh.json` 与 `index.html` 均不含 U+FFFD。
- 表格、公式、图片与参考文献块一律未翻译。

### 遗留问题

- 无图片缺失（`missing_img` 为 0）。
- 原文 b0291 中「Figure 11 shows the variant with different noise」与附录 C.3 主题（图 10：初始噪声的影响）不符，疑为原文笔误（应为 Figure 10），译文按原文直述为「图 11 显示」，未擅自改号。
- 原文 b0299 中「ablation of pickscore」与 b0104 中「maximises」保留了英式拼写，译文按原文语义处理，未改动。
- 原文 b0329「under difference inference settings」中 difference 疑为 different 之笔误，译文按语义译为「不同推理设置下」。
- 正文中大量数学推导以表格／公式块形式存在（式 1–27），属不译块，未处理。

## 复核记录（第二轮交叉验证）

- 复核人：Agent 02（独立复核，非译者）
- 结构核验：MathJax（`tex-mml-chtml.js`）已加载；13 处图片 `src` 全部为 `figures/` 本地相对路径，无 http 外链；无 U+FFFD；顶部中文标题与中文摘要齐备，底部有「返回总目录」链接。
- 抽查块：b0196、b0024、b0215、b0088、b0109、b0091（seed=2）；加抽 b0312、b0056、b0255（seed=7）
- 发现并修正的问题（已直接改写 `zh.json` 并重跑 `build_index.py`）：

| 块 ID | 问题类型 | 修正前 | 修正后 |
|---|---|---|---|
| b0032 | 占位符顺序错位 | 奖励只在最后一步给出：若 ⟦SLOT_16⟧ 则为 ⟦SLOT_15⟧，否则为 0。 | 奖励只在最后一步给出：⟦SLOT_15⟧（若 ⟦SLOT_16⟧），否则为 0。（顺序 15→16 与 EN 一致） |

- 其余抽查块：完整性、准确性、数字与符号、公式占位符、术语一致性均通过，未发现实质错误。
- 构建校验：重跑 `build_index.py` 后 `missing` / `stray` / `mojibake` / `missing_img` 四项均为 0。
