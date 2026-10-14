# Pref-GRPO：面向稳定文本到图像强化学习的成对偏好奖励 GRPO

> 原标题：Pref-GRPO: Pairwise Preference Reward-based GRPO for Stable Text-to-Image Reinforcement Learning
> 作者：Yibin Wang, Zhimin Li, Yuhang Zang, Yujie Zhou, Jiazi Bu, Chunyu Wang, Qinglin Lu, Cheng Jin, Jiaqi Wang · arXiv:2508.20751 · 2025-08-28

<!-- [原子块 · verbatim] Pref-GRPO: Pairwise Preference Reward-based GRPO for Stable Text-to-Image Reinforcement Learning -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] Recent progress has made GRPO-based reinforcement learning central to advancing text-to-image (T2I) generation. Current GRPO methods score a group of generated images with pointwise reward models and  -->

<!-- [原子块 · verbatim] Alongside the optimization side, existing T2I benchmarks offer only coarse, primary-dimension-only evaluation , reporting aggregate scores that hide where models actually succeed or fail. We propose U -->

<!-- [原子块 · verbatim] Together, Pref-GRPO and UniGenBench contribute a more stable optimization objective and a more diagnostic evaluation framework, pointing to fine-grained compositional reasoning as the next frontier fo -->

**EN** Index Terms:

**ZH** 索引词：

<!-- [原子块 · img]  -->

**EN** Fig. 1. Pref-GRPO: from illusory advantage to pairwise preference fitting. (a) Pointwise reward models assign tightly clustered scores to images within a group, producing an illusory advantage after normalization and causing reward hacking. (b) Pref-GRPO reformulates the GRPO objective from absolute score maximization to pairwise preference fitting, enabling stable T2I optimization.

**ZH** 图 1. Pref-GRPO：从虚假优势到成对偏好拟合。(a) 逐点奖励模型给同一组内的图像打出高度集中的分数，归一化后产生虚假优势，进而引发奖励破解。(b) Pref-GRPO 把 GRPO 目标从绝对分数最大化重构为成对偏好拟合，从而实现稳定的 T2I 优化。

**EN** I Introduction

**ZH** I 引言

**EN** Recent progress in text-to-image (T2I) generation has made reinforcement learning [1, 2, 3, 4] and comprehensive benchmarking [5, 6, 7] two pivotal pillars for advancing model capabilities and for evaluating them reliably. Specifically, several GRPO-based approaches [1, 3] employ pointwise reward models [8, 9, 10] to score a group of generated images at each training step and normalize these scores into advantages following the GRPO objective [11]. This pipeline has proven highly effective in aligning T2I generation with human preferences.

**ZH** 文本到图像（T2I）生成的最新进展，使强化学习[1, 2, 3, 4] 与综合基准评测[5, 6, 7] 成为提升模型能力与可靠评测的两大支柱。具体地，若干基于 GRPO 的方法[1, 3] 采用逐点奖励模型[8, 9, 10]，在每一步训练中对一组生成图像打分，并按 GRPO 目标[11] 把这些分数归一化为优势。这一流程已被证明在让 T2I 生成与人类偏好对齐方面十分有效。

**EN** In parallel, evaluating T2I models, particularly their instruction-following capability, has become increasingly important. Widely adopted benchmarks [6, 5] probe compositional aspects using CLIP [12]-based or detection-based metrics, and TIIF-Bench [7] further incorporates additional dimensions such as text rendering.

**ZH** 与此同时，评测 T2I 模型——尤其是其指令遵循能力——变得日益重要。被广泛采用的基准[6, 5] 用基于 CLIP [12] 或基于检测的指标来考察组合性方面，TIIF-Bench [7] 进一步纳入了文本渲染等更多维度。

**EN** Despite these advances, existing approaches still face two key limitations: (1) Existing GRPO-based methods use pointwise reward models to maximize reward scores, which provides early gains but often leads to reward hacking: reward scores keep rising while image quality deteriorates over prolonged training (Fig. 2), a failure mode also noted in prior work [1, 3]. (2) Current T2I benchmarks provide only coarse, primary-dimension-only evaluation, covering a limited range of sub-dimensions without reporting fine-grained sub-dimension scores (Tab. I).

**ZH** 尽管取得上述进展，现有方法仍面临两方面的关键局限：(1) 现有基于 GRPO 的方法用逐点奖励模型最大化奖励分数，这在早期带来收益，却常导致奖励破解：随着训练时间延长，奖励分数持续上升而图像质量不断下降（图 2），这一失效模式在前人工作[1, 3] 中亦有提及。(2) 当前的 T2I 基准只提供粗粒度的、仅覆盖主维度的评测，子维度覆盖面有限，且不上报细粒度的子维度分数（表 I）。

<!-- [原子块 · img]  -->

**EN** Fig. 2: Reward hacking under UnifiedReward. (a) UnifiedReward scores rise monotonically during training. (b) Generated images gradually drift toward an unnaturally dark style, despite the rising reward, which is a clear reward-hacking signature.

**ZH** 图 2：UnifiedReward 下的奖励破解。(a) 训练过程中 UnifiedReward 分数单调上升。(b) 尽管奖励上升，生成图像逐渐偏向一种不自然的暗色风格，这是明确的奖励破解特征。

**EN** In light of these issues, we argue that (1) reward hacking in GRPO-based methods stems from an illusory advantage that arises when pointwise reward models assign tightly clustered scores to images within the same group. Normalizing these scores into advantages disproportionately amplifies small gaps. Under a reward-maximization objective, such inflated advantages drive the policy to over-optimize for trivial reward cues, eventually steering it toward reward-hacking behaviors that rapidly increase scores while destabilizing generation (Figs. Pref-GRPO: Pairwise Preference Reward-based GRPO for Stable Text-to-Image Reinforcement Learning and 2). Moreover, small biases in the reward model are similarly amplified, encouraging the policy to exploit reward-model flaws rather than align with human preferences. (2) Current T2I models already perform well on most primary dimensions (e.g., object attributes and actions), which makes it necessary to decompose these broad dimensions into finer-grained sub-dimensions for more rigorous, diagnostic evaluation.

**ZH** 鉴于上述问题，我们认为：(1) 基于 GRPO 的方法中出现的奖励破解，源于逐点奖励模型给同一组内图像打出高度集中的分数时所产生的虚假优势；把这些分数归一化为优势，会不成比例地放大微小差距。在奖励最大化目标下，这种被放大的优势驱使策略针对无关紧要的奖励线索过度优化，最终滑向奖励破解行为——分数快速上升，生成却愈发不稳定（图 1 与图 2）。此外，奖励模型中的微小偏差同样会被放大，促使策略利用奖励模型的缺陷，而非与人类偏好对齐。(2) 当前的 T2I 模型在多数主维度（如物体属性与动作）上已表现良好，因此有必要把这些宽泛维度分解为更细粒度的子维度，以实现更严格、更具诊断性的评测。

**EN** To this end, this work proposes Pref-GRPO, the first pairwise-preference-reward-based GRPO method for stable T2I reinforcement learning, and UniGenBench, a fine-grained T2I evaluation benchmark for semantic consistency.

**ZH** 为此，本文提出 Pref-GRPO——首个面向稳定 T2I 强化学习的、基于成对偏好奖励的 GRPO 方法，以及 UniGenBench——一个面向语义一致性的细粒度 T2I 评测基准。

**EN** (1) Pref-GRPO incorporates a Pairwise Preference Reward Model (PPRM) [13], reformulating the GRPO objective from absolute reward score maximization to pairwise preference fitting. As illustrated in Fig. Pref-GRPO: Pairwise Preference Reward-based GRPO for Stable Text-to-Image Reinforcement Learning, at each training step, given a group of generated images, we use the PPRM on each image pair to identify the preferred image. Each image’s win rate (the proportion of pairwise comparisons in which it is preferred) is then used as the reward signal for policy optimization. This design offers three key advantages: (a) Amplified reward variance: driving high-quality images toward win rates near 1 and low-quality ones toward 0 yields more separable reward distributions and more informative advantage estimates. (b) Robustness to reward noise: relying on relative rankings rather than absolute scores reduces over-optimization for marginal score gains and mitigates reward hacking. (c) Alignment with human preference: pairwise comparisons mirror the way humans compare images, producing reward signals that better capture nuanced preferences. Extensive experiments show that Pref-GRPO discerns subtle quality variations, produces more stable and directional advantages than pointwise scoring, and alleviates reward hacking.

**ZH** (1) Pref-GRPO 引入成对偏好奖励模型（PPRM）[13]，把 GRPO 目标从绝对奖励分数最大化重构为成对偏好拟合。如图 1 所示，每一步训练中，给定一组生成图像，我们用 PPRM 对每一对图像判断其中更受偏好的一幅；每幅图像的胜率（它在两两比较中被偏好的比例）随后被用作策略优化的奖励信号。这一设计带来三点优势：(a) 奖励方差被放大——把高质量图像推向接近 1 的胜率、低质量图像推向接近 0，得到更可分的奖励分布与信息量更大的优势估计。(b) 对奖励噪声更鲁棒——依赖相对排序而非绝对分数，减少了对微小分数增益的过度优化，缓解了奖励破解。(c) 与人类偏好一致——两两比较复现了人类比对图像的方式，使奖励信号更能捕捉细微偏好。大量实验表明，Pref-GRPO 能辨别细微的质量差异，产生比逐点打分更稳定、更具方向性的优势，并缓解奖励破解。

<!-- [原子块 · img]  -->

**EN** Fig. 3: UniGenBench overview. (a) Prompt themes: 5 primary categories and 20 sub-categories. (b) Subject categories. (c) Evaluation testpoints: 10 primary dimensions and 27 sub-dimensions. (d,e) Benchmarking results of representative open-source and closed-source T2I models on UniGenBench.

**ZH** 图 3：UniGenBench 概览。(a) 提示词主题：5 个主类别与 20 个子类别。(b) 主体类别。(c) 评测测试点：10 个主维度与 27 个子维度。(d, e) 代表性的开源与闭源 T2I 模型在 UniGenBench 上的基准结果。

**EN** TABLE I: Benchmark comparison with existing T2I benchmarks. We summarize benchmark coverage across the dimensions in UniGenBench. Existing benchmarks mainly report primary-dimension scores or cover only a sparse subset of sub-dimensions, whereas UniGenBench provides 10 primary dimensions and 27 sub-dimensions with fine-grained per-sub-dimension evaluation.

**ZH** 表 I：与现有 T2I 基准的比较。我们汇总了各基准在 UniGenBench 各维度上的覆盖情况。现有基准主要上报主维度分数，或只覆盖稀疏的子维度子集，而 UniGenBench 提供 10 个主维度与 27 个子维度，并给出细粒度的逐子维度评测。

<!-- [原子块 · table] Benchmark Score Mode Style World Know. Attribute Action Relationship Compound Grammar Layout Logical Reason. Text — — Quant. Expn. Material Size Shape Color Hand Full Body Animal Non Contact Contact S -->

**EN** (2) UniGenBench is built for fine-grained T2I evaluation, covering 10 primary dimensions and 27 sub-dimensions, alongside 5 prompt themes (20 sub-themes) and diverse subject categories (Fig. 3). Unlike existing benchmarks that provide only coarse, primary-dimension-only evaluation, most primary dimensions in UniGenBench are further subdivided into fine-grained sub-dimensions, each associated with explicit testpoints (Tab. I). We further build an automated evaluation pipeline powered by a strong MLLM (Gemini-2.5-Pro [14]) for both benchmark construction and T2I model evaluation, illustrated in Fig. 7. We benchmark popular closed-source models, including GPT-4o [15], Nano Banana, Seedream-4.0 [16], and Imagen-4.0-Ultra [17], as well as leading open-source models such as Qwen-Image [18], HiDream-I1-Full [19], and Bagel [20]. As shown in Fig. 3(d, e), both open- and closed-source models perform relatively well on Style and World Knowledge prompts, but consistently underperform on prompts requiring Logical Reasoning, such as those involving causal or contrastive relationships.

**ZH** (2) UniGenBench 面向细粒度的 T2I 评测而构建，覆盖 10 个主维度与 27 个子维度，并配有 5 个提示词主题（20 个子主题）和多样的主体类别（图 3）。与只提供粗粒度、仅覆盖主维度评测的现有基准不同，UniGenBench 中的多数主维度被进一步细分为更细粒度的子维度，每个子维度都配有明确的测试点（表 I）。我们还构建了一条由强 MLLM（Gemini-2.5-Pro [14]）驱动的自动化评测流程，同时用于基准构建与 T2I 模型评测，如图 7 所示。我们对主流闭源模型做了基准测试，包括 GPT-4o [15]、Nano Banana、Seedream-4.0 [16] 和 Imagen-4.0-Ultra [17]，以及领先开源模型 Qwen-Image [18]、HiDream-I1-Full [19] 和 Bagel [20]。如图 3(d, e) 所示，开源与闭源模型在 Style 与 World Knowledge 类提示词上表现相对较好，但在需要 Logical Reasoning 的提示词（如涉及因果或对比关系者）上始终表现不佳。

**EN** Contributions: (1) We identify a root cause of reward hacking in pointwise-reward GRPO: the illusory advantage induced by within-group score normalization. (2) We propose Pref-GRPO, the first pairwise-preference-reward-based GRPO method for stable T2I reinforcement learning, which reformulates the optimization objective from absolute reward score maximization to pairwise preference fitting. (3) Experiments on UniGenBench, GenEval, and T2I-CompBench show that Pref-GRPO alleviates reward hacking and improves semantic alignment (+5.84% overall on UniGenBench, with +12.69% on Text and +12.04% on Logical Reasoning), without sacrificing perceptual quality. (4) We introduce UniGenBench, a fine-grained T2I benchmark with 10 primary dimensions and 27 sub-dimensions across 5 prompt themes (20 sub-themes), together with an MLLM-based pipeline for benchmark construction and evaluation. (5) We benchmark representative open- and closed-source T2I models on UniGenBench, revealing that Style and World Knowledge are saturated across strong models, while fine-grained compositional capabilities such as Logical Reasoning, Grammar, and Compound remain the primary bottlenecks.

**ZH** 贡献如下：(1) 我们指出逐点奖励 GRPO 中奖励破解的一个根本原因——组内分数归一化所诱发的虚假优势。(2) 我们提出 Pref-GRPO，首个面向稳定 T2I 强化学习的、基于成对偏好奖励的 GRPO 方法，把优化目标从绝对奖励分数最大化重构为成对偏好拟合。(3) 在 UniGenBench、GenEval 与 T2I-CompBench 上的实验表明，Pref-GRPO 缓解了奖励破解并提升语义对齐（UniGenBench 整体 +5.84%，其中 Text 维度 +12.69%、Logical Reasoning 维度 +12.04%），且未牺牲感知质量。(4) 我们提出 UniGenBench，一个含 10 个主维度与 27 个子维度、覆盖 5 个提示词主题（20 个子主题）的细粒度 T2I 基准，并配套基于 MLLM 的构建与评测流程。(5) 我们在 UniGenBench 上对代表性开源与闭源 T2I 模型做了基准测试，发现 Style 与 World Knowledge 在强模型上已趋于饱和，而 Logical Reasoning、Grammar、Compound 等细粒度组合能力仍是主要瓶颈。

**EN** II Related Work

**ZH** II 相关工作

**EN** Reinforcement Learning for T2I Generation is gaining rapid momentum. Early efforts pursued preference-driven objectives [21, 22, 23]. For example, DiffusionDPO [23], adapted from Direct Preference Optimization (DPO) [24], optimizes preference consistency via a classification-style objective as a simpler alternative to RLHF. DyMO [21] offers a plug-and-play, training-free alignment method that steers generated images toward human preferences at inference. More recently, group relative policy optimization (GRPO) has advanced online RL-enhanced image generation. Flow-GRPO [25] and DanceGRPO [3] instantiate GRPO on flow-matching models, introducing stochasticity by recasting the original deterministic ODE as an equivalent SDE. While effective, these reward score-maximization methods are prone to reward hacking due to illusory advantage. To this end, we propose Pref-GRPO, which shifts training from reward-score maximization to pairwise preference fitting, yielding more stable advantages, and thereby mitigates reward hacking.

**ZH** 面向 T2I 生成的强化学习正迅速兴起。早期工作追求偏好驱动的目标[21, 22, 23]。例如，由直接偏好优化（DPO）[24] 改造而来的 DiffusionDPO [23]，以分类式目标优化偏好一致性，作为 RLHF 的一种更简单替代。DyMO [21] 提供一种即插即用、免训练的对齐方法，在推理阶段把生成图像导向人类偏好。更近期，组相对策略优化（GRPO）推动了在线 RL 增强的图像生成。Flow-GRPO [25] 与 DanceGRPO [3] 在流匹配模型上实例化 GRPO，通过把原确定性 ODE 改写为等价 SDE 引入随机性。这些方法虽然有效，但作为奖励分数最大化方法，因虚假优势而容易出现奖励破解。为此，我们提出 Pref-GRPO，把训练从奖励分数最大化转向成对偏好拟合，得到更稳定的优势，从而缓解奖励破解。

**EN** Existing Benchmarks for T2I Evaluation have expanded the evaluation of T2I models beyond simple visual fidelity, incorporating compositional reasoning [5, 6] and world knowledge [26]. Recently, [7] introduces TIIF-Bench, containing 5k prompts spanning multiple dimensions, i.e., text rendering and style control, rigorously evaluating model robustness to variations in prompt length. However, existing benchmarks largely focus on primary dimension–level coarse assessment, covering a limited set of sub-tasks and lacking fine-grained assessment of these sub-tasks. To address this gap, we propose a unified image generation benchmark, UniGenBench, consisting of 600 prompts spanning diverse themes and categories, assessing T2I models across 10 primary dimensions and 27 sub-dimensions.

**ZH** 面向 T2I 评测的现有基准已把 T2I 模型的评测从单纯的视觉保真度扩展开去，纳入了组合推理[5, 6] 与世界知识[26]。近来，[7] 提出 TIIF-Bench，含 5k 条覆盖多个维度（如文本渲染与风格控制）的提示词，严格评测模型对提示词长度变化的鲁棒性。然而现有基准大多停留在主维度层面的粗粒度评估，覆盖的子任务有限，且缺乏对这些子任务的细粒度评估。为填补这一空白，我们提出统一的图像生成基准 UniGenBench，由 600 条覆盖多样主题与类别的提示词构成，从 10 个主维度与 27 个子维度评估 T2I 模型。

**EN** III Motivation for Pairwise Preference Reward

**ZH** III 成对偏好奖励的动机

**EN** Existing GRPO-based text-to-image methods optimize the policy by maximizing pointwise reward scores [1, 3, 2, 4]. This design implicitly assumes that the absolute score assigned by the reward model is both sufficiently discriminative within a rollout group and reliable enough to support gradient scaling. In practice, however, these assumptions are often violated. For visually similar images sampled from the same prompt, pointwise reward models such as HPSv2 [9] and UnifiedReward [8] frequently produce highly compressed scores (see Fig. Pref-GRPO: Pairwise Preference Reward-based GRPO for Stable Text-to-Image Reinforcement Learning). GRPO then normalizes these near-identical scores by a very small group standard deviation, turning negligible score gaps into disproportionately large advantages. The optimization is therefore driven not by substantial quality differences, but by amplified numerical fluctuations, which leads to the illusory advantage phenomenon, as analyzed in Sec. IV-B.

**ZH** 现有基于 GRPO 的文本到图像方法通过最大化逐点奖励分数来优化策略[1, 3, 2, 4]。这一设计隐含假定：奖励模型给出的绝对分数在一次回放组内具有足够区分度，且足够可靠以支持梯度缩放。然而实践中这些假设常被打破。对同一提示词采样出的视觉上相近的图像，HPSv2 [9]、UnifiedReward [8] 等逐点奖励模型常常给出高度压缩的分数（见图 1）。GRPO 随后用一个极小的组内标准差对这些近乎相同的分数做归一化，把微弱的分数差距放大为不成比例的巨大优势。于是优化的驱动力并非实质性的质量差异，而是被放大的数值波动，这就导致了第 IV-B 节所分析的虚假优势现象。

**EN** The consequence is not merely optimization instability, but a deeper objective mismatch. Once the training target is defined as absolute reward maximization, the policy is encouraged to chase any reward increase, even when that increase comes from reward-model bias rather than genuine improvement in text-image alignment or visual quality. This helps explain the reward hacking behaviors reported in prior work [1, 3] and observed in our experiments: HPSv2 encourages over-saturated generations (see Fig. 9), while UnifiedReward tends to favor an unnatural dark style (see Fig. 2). Importantly, simply shrinking or clipping the normalized advantage can only dampen the update magnitude; it cannot remove the underlying tendency to optimize toward unreliable absolute-score increments.

**ZH** 其后果不只是优化不稳定，更是更深层的目标错配。一旦训练目标被定义为绝对奖励最大化，策略就会被鼓励追逐任何奖励增量，即便该增量来自奖励模型的偏差，而非图文对齐或视觉质量的真实改善。这也解释了前人工作[1, 3] 所报告、并在我们实验中观察到的奖励破解行为：HPSv2 会鼓励过饱和的生成（见图 9），而 UnifiedReward 倾向于偏爱不自然的暗色风格（见图 2）。重要的是，单纯缩小或截断归一化后的优势只能削弱更新幅度，无法消除朝不可靠的绝对分数增量优化的内在倾向。

**EN** These observations motivate replacing reward score maximization with pairwise preference fitting. Relative comparison is fundamentally better suited to this setting for two reasons. First, when candidate images are close in quality, determining which one is better is typically more reliable than assigning well-calibrated absolute scores to each image independently. Second, pairwise comparison discards uninformative score magnitude and focuses optimization on stable ordering information, making the reward signal less sensitive to small fluctuations and common calibration bias. This change also better matches human evaluation, which is usually comparative rather than absolute for similar generations. Motivated by this, we reformulate traditional GRPO with pairwise preference rewards and pairwise win rates, as detailed next.

**ZH** 这些观察促使我们用成对偏好拟合取代奖励分数最大化。相对比较本质上更契合这一场景，原因有二。其一，当候选图像质量接近时，判断哪一幅更好，通常比为每幅图像独立给出校准良好的绝对分数更可靠。其二，两两比较丢弃了无信息量的分数幅值，把优化聚焦在稳定的排序信息上，使奖励信号对小幅波动和常见的校准偏差不再敏感。这一改动也更贴合人类评估——对相近的生成结果，人类判断通常是比较式的而非绝对式的。受此启发，我们用成对偏好奖励与成对胜率重构了传统 GRPO，详见下文。

**EN** IV Pref-GRPO

**ZH** IV Pref-GRPO

**EN** This section presents the technical formulation of Pref-GRPO. We first introduce GRPO on flow matching models in Sec. IV-A, then analyze the illusory advantage phenomenon in Sec. IV-B, and finally describe our Pref-GRPO objective in Sec. IV-C.

**ZH** 本节给出 Pref-GRPO 的技术表述。我们先在第 IV-A 节介绍流匹配模型上的 GRPO，再在第 IV-B 节分析虚假优势现象，最后在第 IV-C 节描述 Pref-GRPO 的目标。

**EN** IV-A Flow Matching GRPO

**ZH** IV-A 流匹配 GRPO

**EN** Flow Matching

**ZH** 流匹配

**EN** Let ⟦SLOT_0⟧ be a data sample and ⟦SLOT_1⟧ a noise sample. Rectified flow [27] defines intermediate samples as

**ZH** 令 ⟦SLOT_0⟧ 为一个数据样本、⟦SLOT_1⟧ 为一个噪声样本。整流流[27] 把中间样本定义为

<!-- [原子块 · table] x t = ( 1 − t ) ​ x 0 + t ​ x 1 , t ∈ [ 0 , 1 ] , x_{t}=(1-t)x_{0}+tx_{1},\quad t\in[0,1], (1) -->

**EN** and trains a velocity field ⟦SLOT_2⟧ via the flow matching [28] objective:

**ZH** 并通过流匹配[28] 目标训练速度场 ⟦SLOT_2⟧：

<!-- [原子块 · table] ℒ FM ​ ( θ ) = 𝔼 t , x 0 , x 1 ​ [ ‖ v − v θ ​ ( x t , t ) ‖ 2 2 ] , v = x 1 − x 0 . \mathcal{L}_{\text{FM}}(\theta)=\mathbb{E}_{t,x_{0},x_{1}}\big[\|v-v_{\theta}(x_{t},t)\|_{2}^{2}\big],\quad v=x_{1} -->

**EN** Beyond training, the iterative denoising process at inference time can be naturally formalized as a Markov Decision Process [29]. We discretize ⟦SLOT_3⟧ into ⟦SLOT_4⟧ steps. At each step, the state is ⟦SLOT_5⟧, where ⟦SLOT_6⟧ denotes the prompt. The action ⟦SLOT_7⟧ corresponds to producing the denoised sample ⟦SLOT_8⟧, yielding a deterministic transition to ⟦SLOT_9⟧. The initial state samples a prompt ⟦SLOT_10⟧ with ⟦SLOT_11⟧ and ⟦SLOT_12⟧. A reward is only provided at the terminal state (⟦SLOT_13⟧): ⟦SLOT_14⟧, and zero otherwise.

**ZH** 除训练外，推理时的迭代去噪过程可以自然地形式化为一个马尔可夫决策过程[29]。我们把 ⟦SLOT_3⟧ 离散为 ⟦SLOT_4⟧ 步。每一步的状态为 ⟦SLOT_5⟧，其中 ⟦SLOT_6⟧ 表示提示词。动作 ⟦SLOT_7⟧ 对应产生去噪后的样本 ⟦SLOT_8⟧，从而确定性地转移到 ⟦SLOT_9⟧。初始状态采样提示词 ⟦SLOT_10⟧，并取 ⟦SLOT_11⟧ 与 ⟦SLOT_12⟧。奖励只在终止状态（⟦SLOT_13⟧）给出：⟦SLOT_14⟧，其余时刻为零。

**EN** GRPO on Flow Matching

**ZH** 流匹配上的 GRPO

**EN** GRPO [11] introduces a group-relative advantage to stabilize policy updates. On flow matching models, for a group of ⟦SLOT_15⟧ generated images ⟦SLOT_16⟧, the advantage of the ⟦SLOT_17⟧-th image is

**ZH** GRPO [11] 引入组相对优势以稳定策略更新。在流匹配模型上，对一组 ⟦SLOT_15⟧ 幅生成图像 ⟦SLOT_16⟧，第 ⟦SLOT_17⟧ 幅图像的优势为

<!-- [原子块 · table] A ^ t i = R ⁡ ( x 0 i , c ) − mean ⁡ ( { R ⁡ ( x 0 j , c ) } j = 1 G ) std ⁡ ( { R ⁡ ( x 0 j , c ) } j = 1 G ) . \hat{A}_{t}^{i}=\frac{R(x_{0}^{i},c)-\mathrm{mean}(\{R(x_{0}^{j},c)\}_{j=1}^{G})}{\math -->

**EN** The policy is updated by maximizing the clipped, KL-regularized objective

**ZH** 策略通过最大化带截断、KL 正则化的目标来更新

<!-- [原子块 · table] 𝒥 Flow ​ ( θ ) = 𝔼 c , { x i } ​ [ f ⁡ ( r , A ^ , θ , η , β ) ] , \mathcal{J}_{\text{Flow}}(\theta)=\mathbb{E}_{c,\{x^{i}\}}\Big[f(r,\hat{A},\theta,\eta,\beta)\Big], (4) -->

**EN** where

**ZH** 其中

<!-- [原子块 · table] f ( r , A ^ , θ , η , β ) = 1 G ∑ i = 1 G 1 T ∑ t = 0 T − 1 min ( r t i ( θ ) A ^ t i , \displaystyle f(r,\hat{A},\theta,\eta,\beta)=\frac{1}{G}\sum_{i=1}^{G}\frac{1}{T}\sum_{t=0}^{T-1}\min\Big(r_{t}^ -->

**EN** with ⟦SLOT_18⟧.

**ZH** 其中 ⟦SLOT_18⟧。

**EN** To enable the stochastic exploration required by GRPO, Flow-GRPO [1] converts the deterministic flow ODE ⟦SLOT_19⟧ to an equivalent SDE:

**ZH** 为实现 GRPO 所需的随机探索，Flow-GRPO [1] 把确定性流 ODE ⟦SLOT_19⟧ 转换为等价的 SDE：

<!-- [原子块 · table] d ​ x t = ( v θ ​ ( x t , t ) + σ t 2 2 ​ t ​ ( x t + ( 1 − t ) ​ v θ ​ ( x t , t ) ) ) ​ d ​ t + σ t ​ d ​ w t , dx_{t}=\big(v_{\theta}(x_{t},t)+\frac{\sigma_{t}^{2}}{2t}(x_{t}+(1-t)v_{\theta}(x_{t}, -->

**EN** where ⟦SLOT_20⟧ is a standard Wiener process and ⟦SLOT_21⟧ is a time-dependent noise scale. Euler-Maruyama discretization gives the update rule:

**ZH** 其中 ⟦SLOT_20⟧ 为标准维纳过程，⟦SLOT_21⟧ 为随时间变化的噪声尺度。Euler-Maruyama 离散化给出如下更新规则：

<!-- [原子块 · table] x t + Δ ​ t = x t + ( v θ ​ ( x t , t ) + σ t 2 2 ​ t ​ ( x t + ( 1 − t ) ​ v θ ​ ( x t , t ) ) ) ​ Δ ​ t \displaystyle x_{t+\Delta t}=x_{t}+\big(v_{\theta}(x_{t},t)+\frac{\sigma_{t}^{2}}{2t}(x_{t}+(1 -->

**EN** where ⟦SLOT_22⟧ and ⟦SLOT_23⟧ is a scalar hyperparameter.

**ZH** 其中 ⟦SLOT_22⟧，而 ⟦SLOT_23⟧ 是一个标量超参数。

**EN** IV-B Illusory Advantage in Pointwise-Reward GRPO

**ZH** IV-B 逐点奖励 GRPO 中的虚假优势

**EN** Existing flow-matching-based GRPO methods [1, 3, 2, 4] use pointwise reward models [8, 12, 9] to score a group of generated images at each update step. The advantage of each image is then obtained by normalizing its reward within the group, as in Eq. 3. This normalization is intended to standardize updates across samples. In practice, however, pointwise reward models often assign tightly clustered scores ⟦SLOT_24⟧ to visually similar images from the same prompt, yielding a small within-group standard deviation ⟦SLOT_25⟧. As a consequence, even minor score gaps are disproportionately magnified after normalization (see Fig. Pref-GRPO: Pairwise Preference Reward-based GRPO for Stable Text-to-Image Reinforcement Learning(a)).

**ZH** 现有基于流匹配的 GRPO 方法[1, 3, 2, 4] 在每一步更新时用逐点奖励模型[8, 12, 9] 对一组生成图像打分。每幅图像的优势随后由其在组内的奖励归一化得到，如式 3。该归一化意在使不同样本间的更新具有统一尺度。然而实践中，逐点奖励模型常给同一提示词下视觉相近的图像打出高度集中的分数 ⟦SLOT_24⟧，导致组内标准差 ⟦SLOT_25⟧ 很小。结果是，即便极小的分数差距也会在归一化后被不成比例地放大（见图 1(a)）。

**EN** To make this effect explicit, let ⟦SLOT_26⟧ and ⟦SLOT_27⟧ denote the mean and standard deviation of the group’s rewards. Define the centered reward of sample ⟦SLOT_28⟧ as ⟦SLOT_29⟧. The normalized advantage then becomes:

**ZH** 为使该效应更明确，令 ⟦SLOT_26⟧ 与 ⟦SLOT_27⟧ 分别表示组内奖励的均值与标准差。定义样本 ⟦SLOT_28⟧ 的中心化奖励为 ⟦SLOT_29⟧。归一化后的优势于是变为：

<!-- [原子块 · table] A ^ t i = Δ ​ r i σ r . \hat{A}_{t}^{i}=\frac{\Delta r_{i}}{\sigma_{r}}. (8) -->

**EN** For clarity, we drop the clip and KL terms and isolate the effect of reward normalization. The gradient of the GRPO objective with respect to ⟦SLOT_30⟧ is then:

**ZH** 为清晰起见，我们略去截断项与 KL 项，单独考察奖励归一化的作用。GRPO 目标对 ⟦SLOT_30⟧ 的梯度为：

<!-- [原子块 · table] ∇ θ 𝒥 Flow ​ ( θ ) = 𝔼 c , { x i } ​ [ 1 G ​ ∑ i = 1 G 1 T ​ ∑ t = 0 T − 1 ∇ θ ( r t i ​ ( θ ) ​ A ^ t i ) ] . \nabla_{\theta}\mathcal{J}_{\text{Flow}}(\theta)=\mathbb{E}_{c,\{x^{i}\}}\Bigg[\frac{1}{G -->

**EN** Substituting ⟦SLOT_31⟧ and treating ⟦SLOT_32⟧ as a per-group constant, we obtain:

**ZH** 代入 ⟦SLOT_31⟧，并把 ⟦SLOT_32⟧ 视作逐组常数，可得：

<!-- [原子块 · table] ∇ θ 𝒥 Flow ​ ( θ ) = 1 σ r ​ 𝔼 c , { x i } ​ [ 1 G ​ ∑ i = 1 G 1 T ​ ∑ t = 0 T − 1 ∇ θ ( r t i ​ ( θ ) ​ Δ ​ r i ) ] . \displaystyle\nabla_{\theta}\mathcal{J}_{\text{Flow}}(\theta)=\frac{1}{\sigma_{r} -->

**EN** The gradient norm therefore contains an explicit factor of ⟦SLOT_33⟧:

**ZH** 因此梯度范数中含有显式的 ⟦SLOT_33⟧ 因子：

<!-- [原子块 · table] ‖ ∇ θ 𝒥 Flow ‖ ∝ 1 σ r . \|\nabla_{\theta}\mathcal{J}_{\text{Flow}}\|\propto\frac{1}{\sigma_{r}}. (11) -->

**EN** Therefore, when a pointwise reward model assigns nearly identical scores to images within the same group (i.e., ⟦SLOT_34⟧), the normalization becomes highly sensitive to small perturbations. Even when ⟦SLOT_35⟧ is small, dividing by a small ⟦SLOT_36⟧ produces disproportionately large normalized advantages ⟦SLOT_37⟧, making the update direction overly dependent on noisy reward differences.

**ZH** 于是，当逐点奖励模型给同组内的图像打出几乎相同的分数（即 ⟦SLOT_34⟧）时，归一化会对微小扰动高度敏感。即便 ⟦SLOT_35⟧ 很小，除以一个很小的 ⟦SLOT_36⟧ 也会产生不成比例的巨大归一化优势 ⟦SLOT_37⟧，使更新方向过度依赖带噪声的奖励差异。

**EN** This amplification causes the model to over-optimize for spurious reward differences, manifesting as reward hacking. We term this failure mode the illusory advantage phenomenon. The illusory advantage has two detrimental effects. (1) Excessive optimization: minimal score variations are exaggerated, pushing the policy toward extreme, reward-hacked behaviors (Figs. 2 and 9). (2) Sensitivity to reward noise: the optimization becomes highly susceptible to biases in the reward model, encouraging the policy to exploit model flaws rather than pursue genuine quality improvements.

**ZH** 这种放大会使模型针对虚假的奖励差异过度优化，表现为奖励破解。我们把这一失效模式称为虚假优势现象。虚假优势有两方面危害：(1) 过度优化——极小的分数差异被放大，把策略推向极端的、被奖励破解的行为（图 2 与图 9）；(2) 对奖励噪声敏感——优化变得极易受奖励模型偏差影响，鼓励策略利用模型缺陷，而非追求真实的质量提升。

**EN** IV-C Pairwise Preference Reward-based GRPO

**ZH** IV-C 基于成对偏好奖励的 GRPO

**EN** To mitigate the illusory advantage, we propose Pref-GRPO, which uses a Pairwise Preference Reward Model (PPRM) [13] to reformulate the optimization objective as pairwise preference fitting. Instead of relying on absolute reward scores, Pref-GRPO evaluates relative preferences among generated images, mirroring the way humans compare images pairwise. This yields a reward signal that better captures nuanced differences in image quality and prompt alignment, producing more stable and informative advantages for policy optimization while reducing susceptibility to reward hacking. Specifically, given a set of ⟦SLOT_38⟧ images ⟦SLOT_39⟧ sampled from ⟦SLOT_40⟧ for prompt ⟦SLOT_41⟧, for each ordered pair ⟦SLOT_42⟧ with ⟦SLOT_43⟧ we use the PPRM to determine whether image ⟦SLOT_44⟧ is preferred over image ⟦SLOT_45⟧. The win rate of image ⟦SLOT_46⟧ is defined as

**ZH** 为缓解虚假优势，我们提出 Pref-GRPO，它用成对偏好奖励模型（PPRM）[13] 把优化目标重构为成对偏好拟合。Pref-GRPO 不依赖绝对奖励分数，而是评估生成图像之间的相对偏好，复现人类两两比对图像的方式。这得到的奖励信号能更好地捕捉图像质量与提示词对齐上的细微差异，为策略优化提供更稳定、信息量更大的优势，同时降低受奖励破解影响的可能。具体地，给定 ⟦SLOT_38⟧ 幅图像 ⟦SLOT_39⟧，它们从 ⟦SLOT_40⟧ 采样得到，对应提示词 ⟦SLOT_41⟧；对每个有序对 ⟦SLOT_42⟧（⟦SLOT_43⟧），我们用 PPRM 判断图像 ⟦SLOT_44⟧ 是否比图像 ⟦SLOT_45⟧ 更受偏好。图像 ⟦SLOT_46⟧ 的胜率定义为

<!-- [原子块 · table] w i = 1 G − 1 ​ ∑ j ≠ i 𝟙 ​ ( x 0 i ≻ x 0 j ) , w_{i}=\frac{1}{G-1}\sum_{j\neq i}\mathbb{1}\big(x_{0}^{i}\succ x_{0}^{j}\big), (12) -->

**EN** where ⟦SLOT_47⟧ is the indicator function, and ⟦SLOT_48⟧ indicates that image ⟦SLOT_49⟧ is preferred over image ⟦SLOT_50⟧ according to the PPRM. The win rates are then used as rewards, replacing the scalar rewards ⟦SLOT_51⟧ in the GRPO advantage:

**ZH** 其中 ⟦SLOT_47⟧ 为指示函数，⟦SLOT_48⟧ 表示按 PPRM 的判定，图像 ⟦SLOT_49⟧ 比图像 ⟦SLOT_50⟧ 更受偏好。这些胜率随后被用作奖励，取代 GRPO 优势中的标量奖励 ⟦SLOT_51⟧：

<!-- [原子块 · table] A ^ t i = w i − mean ⁡ ( { w j } j = 1 G ) std ⁡ ( { w j } j = 1 G ) . \hat{A}_{t}^{i}=\frac{w_{i}-\mathrm{mean}(\{w_{j}\}_{j=1}^{G})}{\mathrm{std}(\{w_{j}\}_{j=1}^{G})}. (13) -->

**EN** Compared to reward score maximization, Pref-GRPO offers several advantages: (1) Amplified reward variance: replacing scalar rewards with pairwise win rates spreads win rates across ⟦SLOT_52⟧, yielding a larger within-group variance. High-quality samples approach ⟦SLOT_53⟧, and lower-quality samples approach ⟦SLOT_54⟧, producing a more discriminative and robust reward distribution for advantage estimation, thereby mitigating reward hacking. (2) Robustness to reward noise: because optimization relies on relative rankings rather than raw scores, Pref-GRPO reduces sensitivity to small fluctuations and biases in the reward model, lowering the likelihood of reward hacking and improving training stability. (3) Alignment with human preference: human preference judgments over images are inherently relative rather than absolute. Mirroring this process lets Pref-GRPO capture fine-grained quality distinctions often missed by pointwise scoring, providing a more faithful signal for policy improvement.

**ZH** 与奖励分数最大化相比，Pref-GRPO 有几方面优势：(1) 奖励方差被放大——用成对胜率取代标量奖励，使胜率散布在 ⟦SLOT_52⟧ 之上，得到更大的组内方差；高质量样本趋近 ⟦SLOT_53⟧，低质量样本趋近 ⟦SLOT_54⟧，为优势估计提供更可判别、更鲁棒的奖励分布，从而缓解奖励破解。(2) 对奖励噪声更鲁棒——由于优化依赖相对排序而非原始分数，Pref-GRPO 降低了对奖励模型小幅波动与偏差的敏感度，减小了奖励破解的可能并提升训练稳定性。(3) 与人类偏好一致——人类对图像的偏好判断天然是相对的而非绝对的。复现这一过程使 Pref-GRPO 能捕捉逐点打分常漏掉的细粒度质量差异，为策略改进提供更忠实的信号。

**EN** V UniGenBench

**ZH** V UniGenBench

**EN** Rigorous evaluation is equally important for discerning whether a T2I model faithfully follows complex semantics. This requires a benchmark that goes beyond coarse aggregate scores and probes fine-grained semantic capabilities. However, existing benchmarks [5, 6, 7] still exhibit the following limitations: (1) Sparse sub-dimension coverage: existing benchmarks typically include only a few sub-dimensions within each primary dimension, missing many practical capabilities. For example, as shown in Tab. I, current benchmarks include only a single sub-dimension for Relationship and Grammar, leading to incomplete and potentially misleading assessments in these aspects. (2) No sub-dimension-level reporting: existing benchmarks report scores only at the primary-dimension level, without breaking down performance across sub-dimensions. This coarse reporting limits interpretability and prevents diagnosing a T2I model’s strengths and weaknesses.

**ZH** 严格评测对于判断一个 T2I 模型是否忠实遵循复杂语义同样重要。这需要一种超越粗粒度聚合分数、能够探查细粒度语义能力的基准。然而现有基准[5, 6, 7] 仍存在以下局限：(1) 子维度覆盖稀疏——现有基准在每个主维度下通常只包含少数几个子维度，遗漏了许多实用能力。例如，如表 I 所示，现有基准对 Relationship 与 Grammar 各只含一个子维度，导致这两方面的评估不完整、甚至可能产生误导。(2) 不上报子维度级分数——现有基准只在主维度层级上报分数，不按子维度拆分性能。这种粗粒度上报限制了可解释性，也无法诊断 T2I 模型的长处与短板。

**EN** Motivated by this gap, we propose UniGenBench, a T2I evaluation benchmark designed not only to compare models, but also to reveal where their semantic understanding actually breaks down. UniGenBench offers the following advantages:

**ZH** 受这一空白驱动，我们提出 UniGenBench——一个 T2I 评测基准，其目的不仅在于比较模型，更在于揭示模型的语义理解究竟在哪里失效。UniGenBench 具有如下优势：

**EN** • Comprehensive fine-grained evaluation: 10 primary dimensions and 27 sub-dimensions, enabling substantially finer-grained diagnosis than benchmarks that report only coarse dimension-level scores.

**ZH** • 全面的细粒度评测：10 个主维度与 27 个子维度，相比只上报粗粒度维度级分数的基准，能实现更细粒度的诊断。

**EN** • Broad prompt coverage: 5 major prompt themes and 20 sub-themes, spanning scenarios from realistic rendering to open-ended creative composition.

**ZH** • 广泛的提示词覆盖：5 个主要提示词主题与 20 个子主题，场景横跨从真实感渲染到开放式创意构图。

**EN** • Efficient benchmark design: 600 prompts, each with 1 to 5 explicit testpoints, achieving broad semantic coverage without the thousands of prompts used by prior benchmarks.

**ZH** • 高效的基准设计：600 条提示词，每条配 1 到 5 个明确测试点，无需像此前基准那样动用数千条提示词即可获得广泛的语义覆盖。

**EN** • Reliable MLLM-based assessment: each prompt is paired with structured testpoint descriptions, enabling precise, interpretable per-testpoint assessment of whether the intended semantic targets are satisfied.

**ZH** • 可靠的 MLLM 评估：每条提示词配结构化的测试点描述，从而对预期语义目标是否满足作出精确、可解释的逐测试点评估。

**EN** We will first introduce our design of prompt themes and evaluation criteria in the benchmark (Sec. V-A), and then elaborate on our MLLM-based automated pipeline for prompt generation and T2I evaluation (Sec. V-B).

**ZH** 我们先在第 V-A 节介绍基准中提示词主题与评测维度的设计，再在第 V-B 节详述我们基于 MLLM 的提示词生成与 T2I 评测自动化流程。

<!-- [原子块 · img]  -->

**EN** Fig. 4: Prompt themes of UniGenBench. Representative examples for each of the 5 primary themes and 20 sub-themes.

**ZH** 图 4：UniGenBench 的提示词主题。5 个主主题与 20 个子主题各自的代表性示例。

**EN** V-A Prompt Themes and Evaluation Dimensions

**ZH** V-A 提示词主题与评测维度

**EN** As shown in Fig. 3, UniGenBench covers five major prompt themes: Art, Illustration, Creative Divergence, Design, and Film&Storytelling, further divided into 20 subcategories. It also spans diverse subject categories including animals, objects, anthropomorphic characters, scenes, and an Other category for special entities (e.g., robots in science-fiction themes). This design ensures the benchmark spans both practical generation scenarios and open-ended creative settings, rather than skewing toward a narrow prompt distribution. Representative examples of the prompt themes are shown in Fig. 4.

**ZH** 如图 3 所示，UniGenBench 覆盖五个主要提示词主题：Art、Illustration、Creative Divergence、Design 与 Film&Storytelling，并进一步细分为 20 个子类别。它还涵盖多样的主体类别，包括动物、物体、拟人角色、场景，以及一个用于特殊实体（如科幻主题中的机器人）的 Other 类别。这一设计保证基准同时覆盖实用生成场景与开放式创意场景，而非偏向狭窄的提示词分布。提示词的代表性示例见图 4。

**EN** Unlike coarse benchmarks that only report a few high-level metrics, UniGenBench defines 10 primary evaluation dimensions and 27 sub-dimensions. As illustrated in Fig. 5, we explicitly include several challenging yet practically important capabilities that are often overlooked, such as logical reasoning, facial expressions, pronoun reference, hand actions, and fine-grained relationship understanding (e.g., composition, similarity, and inclusion relations), as well as grammatical consistency across multiple entities. This finer decomposition enables the benchmark to diagnose a model’s strengths and weaknesses more precisely, providing substantially richer feedback than dimension-level averages alone.

**ZH** 与只上报少数高层指标的粗粒度基准不同，UniGenBench 定义了 10 个主评测维度与 27 个子维度。如图 5 所示，我们明确纳入了若干常被忽视、却具有实际重要性的挑战性能力，如逻辑推理、面部表情、代词指代、手部动作以及细粒度的关系理解（如构成、相似与包含关系），还有跨多个实体的语法一致性。更细的分解使基准能更精确地诊断模型的长处与短板，提供比维度级平均值丰富得多的反馈。

**EN** At a high level, these ten dimensions cover complementary aspects of semantic faithfulness: Style evaluates adherence to the requested visual form; World Knowledge evaluates consistency with commonsense and real-world facts; Attribute evaluates whether entities exhibit the correct properties; Action evaluates whether entities perform the intended behaviors; Relationship evaluates whether inter-entity relations are grounded correctly; Layout evaluates whether spatial arrangements are rendered accurately; Compound evaluates whether multiple concepts are integrated coherently; Grammar evaluates language-sensitive grounding such as reference, consistency, and negation; Logical Reasoning evaluates causal, contrastive, and inferential understanding; and Text evaluates whether explicit textual content is generated correctly.

**ZH** 在高层面上，这十个维度覆盖了语义忠实性的互补方面：Style 评估对指定视觉形式的遵循程度；World Knowledge 评估与常识和现实世界事实的一致性；Attribute 评估实体是否表现出正确的属性；Action 评估实体是否执行了预期的行为；Relationship 评估实体间关系是否被正确落实；Layout 评估空间排布是否被准确呈现；Compound 评估多个概念是否被连贯地整合；Grammar 评估指称、一致性与否定等依赖语言的落地能力；Logical Reasoning 评估因果、对比与推理性理解；Text 评估明确的文字内容是否被正确生成。

**EN** To make these dimensions operational, we further instantiate them with explicit sub-dimension testpoints. Specifically, Attribute is decomposed into quantity, expression, material, size, shape, and color; Action is decomposed into hand actions, full-body motions, animal behaviors, contact interactions, non-contact interactions, and object states; Relationship is decomposed into composition, similarity, inclusion, and comparison; and Layout is decomposed into 2D placement and 3D spatial arrangement. This design allows UniGenBench to reveal which aspect of semantic generation actually fails, rather than only reporting a coarse dimension-level average.

**ZH** 为使这些维度可操作，我们进一步用明确的子维度测试点将它们实例化。具体地，Attribute 被分解为数量、表情、材质、尺寸、形状与颜色；Action 被分解为手部动作、全身动作、动物行为、接触式交互、非接触式交互与物体状态；Relationship 被分解为构成、相似、包含与比较；Layout 被分解为二维放置与三维空间排布。这一设计使 UniGenBench 能揭示语义生成究竟在哪一环节失败，而不只是上报一个粗粒度的维度级均值。

<!-- [原子块 · img]  -->

**EN** Fig. 5: Evaluation dimensions of UniGenBench. Representative prompt examples for each of the 27 sub-dimensions under the 10 primary evaluation dimensions.

**ZH** 图 5：UniGenBench 的评测维度。10 个主评测维度下 27 个子维度各自的代表性提示词示例。

**EN** We further control the complexity of each prompt through the number of associated testpoints. Instead of relying on thousands of prompts with diffuse evaluation targets, UniGenBench uses 600 prompts, each focusing on 1 to 5 specific testpoints. As shown in Fig. 6, this design achieves a practical balance between coverage and efficiency: each prompt remains interpretable and evaluation-friendly, while the benchmark as a whole still spans a broad set of semantic capabilities.

**ZH** 我们还通过每条提示词所关联测试点的数量来控制其复杂度。UniGenBench 没有采用数千条评测目标散乱的提示词，而是使用 600 条提示词，每条聚焦 1 到 5 个具体测试点。如图 6 所示，这一设计在覆盖度与效率之间取得了务实的平衡：每条提示词都保持可解释、便于评测，而基准整体仍覆盖广泛的语义能力。

<!-- [原子块 · img]  -->

**EN** Fig. 6: Distribution of testpoint counts per prompt in UniGenBench. Each prompt is associated with 1 to 5 testpoints, balancing coverage and evaluation interpretability.

**ZH** 图 6：UniGenBench 中每条提示词测试点数量的分布。每条提示词关联 1 到 5 个测试点，在覆盖度与评测可解释性之间取得平衡。

<!-- [原子块 · img]  -->

**EN** Fig. 7: UniGenBench construction and evaluation pipeline. An MLLM (Gemini-2.5-Pro) is used for (a) prompt and testpoint-description generation and (b) fine-grained per-testpoint evaluation.

**ZH** 图 7：UniGenBench 的构建与评测流程。用 MLLM（Gemini-2.5-Pro）完成（a）提示词与测试点描述的生成，以及（b）细粒度的逐测试点评测。

**EN** V-B Benchmark Construction and Evaluation Pipeline

**ZH** V-B 基准构建与评测流程

**EN** Having established diverse prompt themes, subject categories, and evaluation dimensions, we further construct an MLLM-based automated pipeline to operationalize the benchmark shown in Fig. 7. This pipeline serves two complementary purposes: (1) generating large-scale, diverse, and high-quality prompts in a systematic and controllable manner (Sec. V-B1), and (2) enabling scalable, reliable, and fine-grained evaluation of T2I models (Sec. V-B2). By leveraging the reasoning and perception capabilities of MLLMs, the pipeline eliminates the need for costly human annotation, while ensuring both efficiency and reliability in benchmark construction and model assessment.

**ZH** 在确立了多样的提示词主题、主体类别与评测维度之后，我们进一步构建了一条基于 MLLM 的自动化流程来落地该基准，如图 7 所示。该流程服务于两个互补目的：(1) 以系统、可控的方式生成大规模、多样且高质量的提示词（第 V-B1 节）；(2) 实现对 T2I 模型可扩展、可靠且细粒度的评测（第 V-B2 节）。借助 MLLM 的推理与感知能力，该流程免去了昂贵的人工标注，同时保证了基准构建与模型评估的效率与可靠性。

**EN** V-B1 Prompt and Testpoint Description Generation

**ZH** V-B1 提示词与测试点描述生成

**EN** Let ⟦SLOT_55⟧ denote the set of prompt themes, ⟦SLOT_56⟧ the set of subject categories, and ⟦SLOT_57⟧ the set of evaluation dimensions. For each prompt, we sample a theme ⟦SLOT_58⟧ and a subject category ⟦SLOT_59⟧ uniformly at random. Subsequently, a subset of ⟦SLOT_60⟧ testpoints ⟦SLOT_61⟧, with ⟦SLOT_62⟧, is sampled to target specific fine-grained evaluation aspects.

**ZH** 令 ⟦SLOT_55⟧ 表示提示词主题集合，⟦SLOT_56⟧ 表示主体类别集合，⟦SLOT_57⟧ 表示评测维度集合。对每条提示词，我们均匀随机采样一个主题 ⟦SLOT_58⟧ 与一个主体类别 ⟦SLOT_59⟧。随后采样一个含 ⟦SLOT_60⟧ 个测试点的子集 ⟦SLOT_61⟧（其中 ⟦SLOT_62⟧），以针对特定的细粒度评测方面。

**EN** The selected tuple ⟦SLOT_63⟧ is input into the MLLM, which generates two outputs: (i) a natural language prompt ⟦SLOT_64⟧ that conforms to the semantic constraints of the selected theme ⟦SLOT_65⟧ and subject category ⟦SLOT_66⟧, and (ii) a structured description set ⟦SLOT_67⟧, where each ⟦SLOT_68⟧ specifies how the corresponding testpoint ⟦SLOT_69⟧ is realized in the prompt. Formally, this process can be expressed as:

**ZH** 选定的元组 ⟦SLOT_63⟧ 被输入 MLLM，由其生成两项输出：(i) 一条自然语言提示词 ⟦SLOT_64⟧，符合所选主题 ⟦SLOT_65⟧ 与主体类别 ⟦SLOT_66⟧ 的语义约束；(ii) 一个结构化描述集合 ⟦SLOT_67⟧，其中每个 ⟦SLOT_68⟧ 说明对应测试点 ⟦SLOT_69⟧ 在该提示词中如何实现。形式化地，该过程可表示为：

<!-- [原子块 · table] ( p , { d 1 , … , d k } ) ∼ MLLM ( p , { d i } | t , s , { c 1 , … , c k } ) . (p,\{d_{1},\dots,d_{k}\})\sim\mathrm{MLLM}\Big(p,\{d_{i}\}\;\big|\;t,s,\{c_{1},\dots,c_{k}\}\Big). (14) -->

**EN** V-B2 T2I Model Evaluation

**ZH** V-B2 T2I 模型评测

**EN** Given the generated images ⟦SLOT_70⟧ for benchmark prompts ⟦SLOT_71⟧, we evaluate each image using an MLLM. Specifically, the image ⟦SLOT_72⟧, its corresponding prompt ⟦SLOT_73⟧, and its testpoint descriptions ⟦SLOT_74⟧ are provided as input. The MLLM evaluates each testpoint ⟦SLOT_75⟧ in the context of ⟦SLOT_76⟧, producing a binary score ⟦SLOT_77⟧ and a textual rationale ⟦SLOT_78⟧ justifying the assessment. This can be formally represented as:

**ZH** 给定生成图像 ⟦SLOT_70⟧ 与对应的基准提示词 ⟦SLOT_71⟧，我们用 MLLM 对每幅图像作评测。具体地，把图像 ⟦SLOT_72⟧、其对应提示词 ⟦SLOT_73⟧ 及其测试点描述 ⟦SLOT_74⟧ 作为输入。MLLM 评估每个测试点 ⟦SLOT_75⟧（在 ⟦SLOT_76⟧ 的语境下），给出二值分数 ⟦SLOT_77⟧ 与说明该判断的文本理由 ⟦SLOT_78⟧。该过程可形式化表示为：

<!-- [原子块 · table] ( r i , 1 , … , r i , k , e i , 1 , … , e i , k ) ∼ \displaystyle(r_{i,1},\dots,r_{i,k},e_{i,1},\dots,e_{i,k})\sim (15) MLLM ⁡ ( { r i , j , e i , j } | x i , p i , { d i , 1 , … , d i , k } ) . \disp -->

**EN** This process ensures that the evaluation captures both the quantitative performance on each testpoint and the qualitative reasoning behind the assessment.

**ZH** 这一过程保证评测既捕捉每个测试点上的量化表现，也捕捉判断背后的定性推理。

**EN** After obtaining the scores ⟦SLOT_79⟧ for each testpoint ⟦SLOT_80⟧ in all generated images, we aggregate them to compute scores of sub- and primary evaluation dimensions. Specifically, for each sub-dimension ⟦SLOT_81⟧, we define its score as the ratio of the number of times the model successfully satisfies the corresponding testpoint description to the total number of occurrences of that testpoint across the benchmark:

**ZH** 在得到分数 ⟦SLOT_79⟧——即全部生成图像中每个测试点 ⟦SLOT_80⟧ 的得分——之后，我们对其聚合，计算出子维度与主评测维度的分数。具体地，对每个子维度 ⟦SLOT_81⟧，我们把其分数定义为模型成功满足相应测试点描述的次数，与该测试点在整个基准中出现总次数之比：

<!-- [原子块 · table] R c = ∑ i , j 𝟏 { d i , j ∈ c and r i , j = 1 } ∑ i , j 𝟏 { d i , j ∈ c } , R_{c}=\frac{\sum_{i,j}\mathbf{1}\{d_{i,j}\in c\text{ and }r_{i,j}=1\}}{\sum_{i,j}\mathbf{1}\{d_{i,j}\in c\}}, (16) -->

**EN** where ⟦SLOT_82⟧ is the indicator function. The overall score for a primary dimension ⟦SLOT_83⟧ is then obtained by averaging the scores of all its sub-dimensions. This procedure ensures that both fine-grained performance on sub-dimensions and broader performance on primary dimensions are captured.

**ZH** 其中 ⟦SLOT_82⟧ 为指示函数。主维度 ⟦SLOT_83⟧ 的整体分数随后由其全部子维度分数平均得到。这一流程保证既捕捉子维度上的细粒度表现，也捕捉主维度上的整体表现。

**EN** VI Experiments

**ZH** VI 实验

**EN** VI-A Experimental Setup

**ZH** VI-A 实验设置

**EN** Baselines. We use FLUX.1-dev [30] as the base T2I model and UnifiedReward-Think [13] as the pairwise preference reward model (PPRM) in Pref-GRPO. As reward-maximization baselines, we train FLUX.1-dev with Flow-GRPO [1] using each of HPSv2 [9], CLIP [12], and UnifiedReward (UR) [8] as the pointwise reward.

**ZH** 基线。我们以 FLUX.1-dev [30] 作为基础 T2I 模型，以 UnifiedReward-Think [13] 作为 Pref-GRPO 中的成对偏好奖励模型（PPRM）。作为奖励最大化基线，我们用 Flow-GRPO [1] 训练 FLUX.1-dev，分别以 HPSv2 [9]、CLIP [12] 与 UnifiedReward（UR）[8] 作为逐点奖励。

**EN** Training. Using the pipeline in Fig. 7(a), we generate 5k training prompts, disjoint from the 600 UniGenBench evaluation prompts. The same 5k prompts are used to train Pref-GRPO and all reward-maximization baselines. Training is conducted on 64 H20 GPUs with 25 sampling steps, 8 rollouts per prompt from the same initial noise ⟦SLOT_84⟧, 4 gradient accumulation steps, and a learning rate of ⟦SLOT_85⟧. Following Flow-GRPO [1], the SDE noise-scale hyperparameter is set to ⟦SLOT_86⟧. We host the PPRM as an inference server using vLLM [31].

**ZH** 训练。使用图 7(a) 的流程，我们生成 5k 条训练提示词，与 UniGenBench 的 600 条评测提示词互不重叠。Pref-GRPO 与所有奖励最大化基线共用这 5k 条提示词。训练在 64 张 H20 GPU 上进行，采样步数 25，每个提示词从同一初始噪声 ⟦SLOT_84⟧ 出发做 8 次回放，梯度累积步数为 4，学习率为 ⟦SLOT_85⟧。沿用 Flow-GRPO [1]，SDE 噪声尺度超参数设为 ⟦SLOT_86⟧。我们用 vLLM [31] 把 PPRM 部署为推理服务。

**EN** Inference. At inference, we generate ⟦SLOT_87⟧ images with 30 sampling steps and a classifier-free guidance scale of 3.5, following the official FLUX.1-dev configuration. To ensure a fair comparison, all methods share identical prompts and initial noise at evaluation.

**ZH** 推理。推理时，我们按官方 FLUX.1-dev 配置，用 30 步采样、无分类器引导尺度 3.5 生成 ⟦SLOT_87⟧ 幅图像。为保证公平比较，所有方法在评测时使用相同的提示词与初始噪声。

**EN** Evaluation. We evaluate semantic consistency on UniGenBench, GenEval [5], and T2I-CompBench [6]. For each test prompt, we generate four images and report the average score. Image quality is further evaluated with UnifiedReward [8], ImageReward [32], PickScore [10], and Aesthetic [33]. ImageReward, PickScore, and Aesthetic are disjoint from the training rewards and serve as the independent quality metrics.

**ZH** 评测。我们在 UniGenBench、GenEval [5] 与 T2I-CompBench [6] 上评测语义一致性。对每条测试提示词生成四幅图像并上报平均分。图像质量进一步用 UnifiedReward [8]、ImageReward [32]、PickScore [10] 与 Aesthetic [33] 评测。ImageReward、PickScore 与 Aesthetic 与训练所用奖励互不重叠，充当独立的质量指标。

**EN** VI-B Main Results: Pref-GRPO vs. Reward-Maximization Baselines

**ZH** VI-B 主要结果：Pref-GRPO 与奖励最大化基线对比

**EN** Quantitative Results. Tab. II shows that Pref-GRPO delivers clear semantic gains on UniGenBench. Relative to the strongest score-maximization baseline (UR), it improves the overall score by 5.84%, with especially large gains on challenging dimensions such as Text (+12.69%) and Logical Reasoning (+12.04%). This pattern is consistent with our motivation in Sec. IV-B: pairwise preferences provide a cleaner gradient signal than pointwise scores on dimensions that require fine-grained semantic grounding and compositional understanding.

**ZH** 定量结果。表 II 显示，Pref-GRPO 在 UniGenBench 上带来明确的语义增益。相对最强的分数最大化基线（UR），它把整体分数提升 5.84%，在 Text（+12.69%）与 Logical Reasoning（+12.04%）等高难度维度上增益尤为显著。这一规律与第 IV-B 节的动机一致：在需要细粒度语义落地与组合理解的维度上，成对偏好比逐点分数提供了更干净的梯度信号。

**EN** The gains also generalize beyond our held-out evaluation on UniGenBench. As shown in Tabs. VI and IV, Pref-GRPO consistently outperforms reward-maximization baselines on both GenEval and T2I-CompBench, indicating improved out-of-domain compositional reasoning, attribute binding, and spatial understanding. Moreover, Tab. III shows that these semantic gains do not come at the expense of perceptual quality: Pref-GRPO achieves the best score on all four image-quality metrics. Overall, pairwise preference fitting improves semantic alignment without sacrificing image quality.

**ZH** 这些增益并不局限于 UniGenBench 上的留出评测。如表 VI 与表 IV 所示，Pref-GRPO 在 GenEval 与 T2I-CompBench 上同样持续优于奖励最大化基线，表明其域外组合推理、属性绑定与空间理解能力均有提升。此外，表 III 显示这些语义增益并非以牺牲感知质量为代价：Pref-GRPO 在四项图像质量指标上均取得最佳分数。总的来看，成对偏好拟合在提升语义对齐的同时并未损害图像质量。

**EN** TABLE II: In-domain semantic consistency comparison on UniGenBench. FLUX.1-dev fine-tuned with Flow-GRPO using different reward models, versus our Pref-GRPO. Gemini-2.5-Pro is used as the evaluator. Best scores are in bold, second-best are underlined.

**ZH** 表 II：UniGenBench 上的域内语义一致性比较。用不同奖励模型经 Flow-GRPO 微调的 FLUX.1-dev 与本文 Pref-GRPO 对比。评测器为 Gemini-2.5-Pro。最佳分数加粗，次优加下划线。

<!-- [原子块 · table] Model Overall Style World Know. Attr. Action Rel. Logic Reason. Grammar Compound Layout Text FLUX.1-dev 61.30 83.90 88.92 67.84 62.17 67.26 30.91 60.96 47.04 71.83 32.18 w/ HPSv2 58.77 75.20 88.77 66. -->

**EN** Qualitative Results. Examples are shown in Fig. 8. Existing methods exhibit varying degrees of reward hacking: HPSv2-optimized images tend to be oversaturated, while UR-optimized images drift toward an unnaturally dark style. We also explore mitigating reward hacking by combining multiple reward scores, i.e., summing HPSv2 and CLIP scores during training (third row in Fig. 8). While this partially reduces reward hacking, it does not eliminate it. In contrast, Pref-GRPO avoids these artifacts and faithfully renders the prompt semantics.

**ZH** 定性结果。示例见图 8。现有方法表现出不同程度的奖励破解：HPSv2 优化的图像趋于过饱和，而 UR 优化的图像偏向不自然的暗色风格。我们也探索了通过组合多个奖励分数来缓解奖励破解，即在训练中对 HPSv2 与 CLIP 分数求和（图 8 第三行）。这在一定程度上减轻了奖励破解，但并未根除。相比之下，Pref-GRPO 避免了这些伪影，并忠实呈现提示词语义。

<!-- [原子块 · img]  -->

**EN** Fig. 8: Qualitative comparison. Rows show FLUX.1-dev trained with HPSv2, HPSv2+CLIP, UnifiedReward, and Pref-GRPO. Pointwise-reward baselines exhibit reward-hacked artifacts (oversaturation for HPSv2, dark style for UnifiedReward), while Pref-GRPO preserves semantic faithfulness and the original FLUX.1-dev visual style.

**ZH** 图 8：定性比较。各行分别为用 HPSv2、HPSv2+CLIP、UnifiedReward 与 Pref-GRPO 训练的 FLUX.1-dev。逐点奖励基线呈现出被奖励破解的伪影（HPSv2 为过饱和，UnifiedReward 为暗色风格），而 Pref-GRPO 保持了语义忠实性与 FLUX.1-dev 原有的视觉风格。

**EN** A detailed analysis of reward hacking under UnifiedReward and HPSv2 is provided in Sec. VII-A.

**ZH** 关于 UnifiedReward 与 HPSv2 下奖励破解的详细分析见第 VII-A 节。

**EN** TABLE III: Image quality comparison. FLUX.1-dev fine-tuned with Flow-GRPO using different reward models, versus our Pref-GRPO. ImageReward, PickScore, and Aesthetic are not used as training rewards and serve as independent quality metrics. Best results are in bold, second-best are underlined.

**ZH** 表 III：图像质量比较。用不同奖励模型经 Flow-GRPO 微调的 FLUX.1-dev 与本文 Pref-GRPO 对比。ImageReward、PickScore 与 Aesthetic 未被用作训练奖励，充当独立的质量指标。最佳结果加粗，次优加下划线。

<!-- [原子块 · table] Model Unified Reward Pick Score Image Reward Aes. FLUX.1-dev 3.04 22.42 1.27 6.13 w/ HPSv2 3.09 22.62 1.34 6.20 w/ HPSv2+CLIP 3.08 22.61 1.30 6.25 w/ UnifiedReward 3.14 22.88 1.38 6.31 w/ Pref-GRPO 3. -->

**EN** TABLE IV: Out-of-domain performance comparison on T2I-CompBench. FLUX.1-dev fine-tuned with Flow-GRPO using different reward models, versus our Pref-GRPO. Best results are in bold, second-best are underlined.

**ZH** 表 IV：T2I-CompBench 上的域外性能比较。用不同奖励模型经 Flow-GRPO 微调的 FLUX.1-dev 与本文 Pref-GRPO 对比。最佳结果加粗，次优加下划线。

<!-- [原子块 · table] Model Overall Color Shape Texture 2D Spatial 3D Spatial Numeracy Non- Spatial Complex FLUX.1-dev 48.17 77.34 48.32 62.66 28.01 40.04 61.88 30.67 36.49 w/ HPSv2 46.77 78.17 51.55 66.13 22.06 33.75 56.3 -->

**EN** VI-C Benchmarked T2I Models on UniGenBench

**ZH** VI-C 在 UniGenBench 上做基准测试的模型

**EN** We further benchmark representative closed-source and open-source T2I models on UniGenBench, spanning diffusion, MMDiT, autoregressive, and unified architectures. Closed-source models are accessed via their official APIs, and open-source models via their released checkpoints, both using the providers’ default inference settings.

**ZH** 我们进一步在 UniGenBench 上对代表性的闭源与开源 T2I 模型做基准测试，覆盖扩散、MMDiT、自回归与统一式等多种结构。闭源模型通过官方 API 访问，开源模型通过已发布的检查点访问，两者均使用提供方默认的推理设置。

**EN** Closed-source Models. We benchmark GPT-4o [15] (OpenAI), Imagen-4.0-Ultra [17] (Google), Seedream-3.0 and Seedream-4.0 [16] (ByteDance), Nano Banana (Google), DALL-E-3 (OpenAI), FLUX-Pro-Ultra and Kontext-Max [30] (Black Forest Labs), and Keling-Ketu (Kuaishou).

**ZH** 闭源模型。我们测试了 GPT-4o [15]（OpenAI）、Imagen-4.0-Ultra [17]（Google）、Seedream-3.0 与 Seedream-4.0 [16]（字节跳动）、Nano Banana（Google）、DALL-E-3（OpenAI）、FLUX-Pro-Ultra 与 Kontext-Max [30]（Black Forest Labs），以及可灵-可图（快手）。

**EN** Open-source Models. We benchmark Qwen-Image [18], HiDream-I1-Full [19], Show-o2 [34], SD-3.5-Large [35], SDXL [35], FLUX.1-dev [30], CogView4 [36], Hunyuan-DiT [37], Playground 2.5 [38], Janus [39], Janus-Pro [40], Janus-Flow [41], Emu3 [42], Bagel [20], and BLIP3-o [43].

**ZH** 开源模型。我们测试了 Qwen-Image [18]、HiDream-I1-Full [19]、Show-o2 [34]、SD-3.5-Large [35]、SDXL [35]、FLUX.1-dev [30]、CogView4 [36]、Hunyuan-DiT [37]、Playground 2.5 [38]、Janus [39]、Janus-Pro [40]、Janus-Flow [41]、Emu3 [42]、Bagel [20] 与 BLIP3-o [43]。

**EN** VI-D Benchmarking Results on UniGenBench

**ZH** VI-D UniGenBench 上的基准测试结果

**EN** TABLE V: Benchmarking results on UniGenBench. We report the overall score and primary-dimension breakdown for the evaluated T2I models. Best and second-best scores are computed separately within the closed- and open-source groups; they are marked in bold and underlined, with top-3 per group annotated by the medal icons.

**ZH** 表 V：UniGenBench 上的基准测试结果。我们上报被测 T2I 模型的整体分数与主维度分项。最佳与次优分数在闭源组与开源组内分别计算，以加粗与下划线标出，每组前三用奖牌图标标注。

<!-- [原子块 · table] Model Overall Style World Know. Attr. Action Rel. Logic Reason. Grammar Compound Layout Text Closed-source Models Keling-Ketu 65.93 92.27 86.62 71.66 68.73 70.94 43.75 71.26 60.81 77.23 16.03 DALL-E-3 -->

**EN** TABLE VI: Out-of-domain performance comparison on GenEval. FLUX.1-dev fine-tuned with Flow-GRPO using different reward models, versus our Pref-GRPO. Best results are in bold, second-best are underlined.

**ZH** 表 VI：GenEval 上的域外性能比较。用不同奖励模型经 Flow-GRPO 微调的 FLUX.1-dev 与本文 Pref-GRPO 对比。最佳结果加粗，次优加下划线。

<!-- [原子块 · table] Model Overall Single Obj. Two Obj. Count. Color Pos. Attr. Bind. FLUX.1-dev 62.92 97.81 79.55 71.56 77.66 18.50 42.25 w/ HPSv2 59.31 97.43 75.00 62.81 73.67 21.00 34.75 w/ HPSv2+CLIP 64.85 98.12 81.00 -->

**EN** As shown in Tab. V, UniGenBench reveals a clear yet nuanced performance hierarchy. Closed-source models remain the strongest overall, with GPT-4o [15] and Imagen-4.0-Ultra [17] leading on 7 of 10 primary dimensions. Their advantage is most pronounced on dimensions that require deeper semantic grounding (e.g., Logical Reasoning, Relationship, Compound, and Text) rather than low-level visual quality. By contrast, dimensions such as Style and World Knowledge are already saturated across many models (most score above 0.8), indicating they are no longer the main bottlenecks for current T2I systems. This contrast illustrates why coarse overall scores are insufficient: the real gap between strong and weak models lies in higher-order semantic composition, not in basic visual plausibility.

**ZH** 如表 V 所示，UniGenBench 揭示出一个清晰而细腻的性能层级。闭源模型整体仍最强，GPT-4o [15] 与 Imagen-4.0-Ultra [17] 在 10 个主维度中的 7 个上领先。它们的优势在需要更深语义落地的维度（如 Logical Reasoning、Relationship、Compound 与 Text）上最为明显，而非低层视觉质量。相比之下，Style 与 World Knowledge 等维度在许多模型上已趋于饱和（多数得分高于 0.8），表明它们不再是当前 T2I 系统的主要瓶颈。这一对比说明粗粒度的整体分数为何不够用：强弱模型之间的真实差距位于更高阶的语义组合，而非基本的视觉合理性。

**EN** Open-source models are closing the gap but remain less balanced across dimensions. Qwen-Image [18] is the strongest open-source model overall, and HiDream-I1-Full [19] is competitive on Action, Layout, and Attribute. Compared with leading closed-source systems, however, open-source models show larger variance across the 10 primary dimensions, with noticeably weaker performance on Logical Reasoning, Grammar, and Compound. This indicates the remaining gap is not primarily one of image quality, but of fine-grained instruction grounding and coherently satisfying multiple constraints within a single prompt. UniGenBench thus serves not only as a leaderboard, but also as a diagnostic benchmark that exposes where current T2I models still fail.

**ZH** 开源模型正在缩小差距，但各维度间的均衡性仍显不足。Qwen-Image [18] 是整体最强的开源模型，HiDream-I1-Full [19] 在 Action、Layout 与 Attribute 上具有竞争力。然而与领先的闭源系统相比，开源模型在 10 个主维度上的方差更大，在 Logical Reasoning、Grammar 与 Compound 上明显更弱。这说明剩余差距主要不在图像质量，而在细粒度的指令落地以及在单条提示词内连贯满足多重约束的能力。因此 UniGenBench 不仅是一张排行榜，也是一个诊断性基准，能暴露当前 T2I 模型仍在何处失败。

**EN** Tab. VII further sharpens this diagnosis by exposing the sub-dimension breakdown hidden beneath the primary-dimension averages. Among closed-source models, GPT-4o leads on semantically fine-grained sub-dimensions such as expression, non-contact interaction, Grammar, and Logical Reasoning, whereas Imagen-4.0-Ultra leads on structure-sensitive sub-dimensions including quantity, contact interaction, composition, and 3D spatial arrangement (Layout). Even among top-tier systems, strengths are not uniform: some models are stronger on abstract semantic interpretation, others on preserving spatial and compositional structure. The fine-grained breakdown is even more informative for open-source models. Qwen-Image shows the most balanced profile and leads in a majority of sub-dimensions among open-source systems, indicating broad rather than narrow improvements. HiDream-I1-Full is competitive on several geometry- and action-related sub-dimensions, but remains visibly weaker on reasoning-intensive dimensions (Logical Reasoning, Grammar, and Compound). Crucially, models with similar primary-dimension averages can still differ substantially in the specific sub-dimensions they master, which UniGenBench makes explicit.

**ZH** 表 VII 通过揭示隐藏在主维度均值之下的子维度分项，进一步细化了这一诊断。在闭源模型中，GPT-4o 在表情、非接触式交互、Grammar 与 Logical Reasoning 等语义细粒度子维度上领先，而 Imagen-4.0-Ultra 在数量、接触式交互、构成与三维空间排布（Layout）等对结构敏感的子维度上领先。即便在顶级系统之间，优势也不均衡：有些模型更擅长抽象的语义解读，另一些则更善于保持空间与组合结构。细粒度分项对开源模型的信息量更大。Qwen-Image 的表现最均衡，在开源系统的多数子维度上领先，说明其改进是广谱的而非狭窄的。HiDream-I1-Full 在若干与几何和动作相关的子维度上具有竞争力，但在推理密集型维度（Logical Reasoning、Grammar 与 Compound）上明显偏弱。关键在于，主维度均值相近的模型，在其真正掌握的具体子维度上仍可能差异显著——正是 UniGenBench 把这一点显式呈现出来。

**EN** TABLE VII: Fine-grained benchmarking results of the models reported in Tab. V. We report sub-dimension breakdowns for overlapping models with available fine-grained annotations. Best scores are in bold, second-best in underlined, computed separately for closed- and open-source models.

**ZH** 表 VII：表 V 中各模型的细粒度基准结果。我们上报具有细粒度标注的重叠模型的子维度分项。最佳分数加粗，次优加下划线，对闭源与开源模型分别计算。

<!-- [原子块 · table] Model Style World Know. Attribute Action Relationship Compound Grammar Layout Logic Reason. Text Quant. Express. Materi. Size Shape Color Hand Full Body Animal Non Contact Contact State Compos. Sim. I -->

**EN** VII Analyses and Ablations

**ZH** VII 分析与消融

<!-- [原子块 · img]  -->

**EN** Fig. 9: Reward hacking under HPSv2. HPSv2 scores continue to rise, but image quality collapses around step 160, manifesting as severe over-saturation.

**ZH** 图 9：HPSv2 下的奖励破解。HPSv2 分数持续上升，但图像质量在第 160 步附近崩溃，表现为严重的过饱和。

**EN** VII-A Reward Hacking in Pointwise GRPO

**ZH** VII-A 逐点 GRPO 中的奖励破解

**EN** We analyze reward hacking under two representative pointwise reward models, UnifiedReward [8] and HPSv2 [9]. For UnifiedReward, Fig. 2 shows that reward scores rise rapidly during training, yet the generated images gradually drift toward an unnatural dark style and perceptual quality degrades. For HPSv2, the same failure mode emerges even more abruptly in Fig. 9: the reward keeps rising, while image quality starts to collapse at around step 160, accompanied by severe over-saturation. Taken together, these results reveal a consistent mismatch between reward growth and real generation quality under reward score maximization.

**ZH** 我们在两个代表性的逐点奖励模型 UnifiedReward [8] 与 HPSv2 [9] 下分析奖励破解。对 UnifiedReward，图 2 显示训练过程中奖励分数快速上升，而生成图像逐渐偏向不自然的暗色风格，感知质量退化。对 HPSv2，图 9 中的同一失效模式出现得更为突兀：奖励持续上升，而图像质量在第 160 步左右开始崩溃，并伴随严重的过饱和。综合来看，这些结果揭示出在奖励分数最大化下，奖励增长与真实生成质量之间存在一贯的错配。

**EN** This mismatch is consistent with the illusory advantage analysis in Sec. IV-B. Once pointwise reward scores within a rollout group become highly compressed, GRPO amplifies tiny score gaps into large normalized advantages, causing the policy to over-optimize for spurious reward cues rather than genuine improvements in alignment or aesthetics. HPSv2 exhibits reward hacking earlier than UnifiedReward, consistent with its smaller intra-group score variance in Fig. Pref-GRPO: Pairwise Preference Reward-based GRPO for Stable Text-to-Image Reinforcement Learning(a), which intensifies the amplification effect. By contrast, Pref-GRPO optimizes relative preferences rather than absolute-score increments, leading to substantially more stable training behavior.

**ZH** 这一错配与第 IV-B 节的虚假优势分析相符。一旦一次回放组内的逐点奖励分数高度压缩，GRPO 就会把微小的分数差距放大为巨大的归一化优势，使策略针对虚假的奖励线索而非对齐或美学上的真实改进过度优化。HPSv2 比 UnifiedReward 更早出现奖励破解，这与它在图 1(a) 中更小的组内分数方差一致——该特性加剧了放大效应。相比之下，Pref-GRPO 优化的是相对偏好而非绝对分数增量，因而训练行为明显更稳定。

**EN** Several complementary observations support this mitigation. First, Fig. Pref-GRPO: Pairwise Preference Reward-based GRPO for Stable Text-to-Image Reinforcement Learning(a) shows that Pref-GRPO maintains a larger intra-group reward variance, directly suppressing the illusory-advantage amplification mechanism. Second, Figs. 2 and 9 show that, unlike pointwise-score GRPO, Pref-GRPO does not drift toward visually degraded solutions during prolonged training. Third, the qualitative comparison in Fig. 8 shows that Pref-GRPO preserves the original FLUX.1-dev visual style and does not collapse to reward-hacked artifacts. Finally, as we show next in Sec. VII-B, a controlled point-score-derived win-rate variant further confirms that replacing absolute-score maximization with a relative-comparison objective is itself the key stabilizing factor.

**ZH** 若干互补观察支持这一缓解效果。第一，图 1(a) 显示 Pref-GRPO 保持了更大的组内奖励方差，直接抑制了虚假优势的放大机制。第二，图 2 与图 9 显示，与逐点分数 GRPO 不同，Pref-GRPO 在长时间训练中并未漂移到视觉退化的解。第三，图 8 的定性比较显示，Pref-GRPO 保持了 FLUX.1-dev 原有的视觉风格，没有坍缩为被奖励破解的伪影。最后，正如我们接下来在第 VII-B 节所示，一个受控的、由逐点分数导出的胜率变体进一步证实：用相对比较目标取代绝对分数最大化，本身就是关键的稳定因素。

**EN** VII-B Point-Score vs. Pairwise-Preference Win Rates

**ZH** VII-B 逐点分数与成对偏好胜率

**EN** To disentangle the effect of the optimization objective from that of the reward model itself, we introduce a controlled variant based on point score-derived win rates. Specifically, we first compute UnifiedReward scores for all images in a rollout group, then convert these scores into pairwise win rates by comparing every image pair, and finally use the resulting win rates as rewards for training. This keeps the underlying reward model unchanged while replacing reward score maximization with a relative-comparison objective.

**ZH** 为把优化目标的作用与奖励模型本身的作用区分开来，我们引入了一个基于逐点分数导出胜率的受控变体。具体地，我们先为一次回放组中的全部图像计算 UnifiedReward 分数，再通过逐对比较把这些分数转换为成对胜率，最后用所得胜率作为奖励进行训练。这保持了底层奖励模型不变，同时把奖励分数最大化替换为相对比较目标。

**EN** This ablation isolates the source of the stability gain. If the improvement of Pref-GRPO came solely from using a stronger pairwise reward model, then converting UnifiedReward scores into win rates should offer little benefit. However, Fig. 10 shows the opposite: once the optimization target is changed from reward score maximization to win-rate fitting, the dark-style reward hacking observed under UnifiedReward is already substantially alleviated. Quantitative results in Tab. VIII further confirm this trend: training with point-score-derived win rates consistently outperforms reward score maximization, and Pref-GRPO, which uses native pairwise preference rewards, achieves the best overall performance.

**ZH** 该消融实验分离出了稳定性增益的来源。若 Pref-GRPO 的改进仅来自使用了更强的成对奖励模型，那么把 UnifiedReward 分数转换为胜率应当几乎不带来收益。然而图 10 显示了相反的结果：一旦优化目标从奖励分数最大化改为胜率拟合，UnifiedReward 下观察到的暗色风格奖励破解就已大幅缓解。表 VIII 的定量结果进一步印证了这一趋势：用逐点分数导出的胜率做训练，持续优于奖励分数最大化；而使用原生成对偏好奖励的 Pref-GRPO 取得最佳整体性能。

**EN** These results support two conclusions. First, a significant part of the instability in prior GRPO methods arises from the objective formulation, not merely from imperfections in the reward model. Second, pairwise preference rewards outperform score-derived win rates, indicating that native pairwise supervision provides cleaner and more faithful relative signals than rankings derived from compressed pointwise scores. In short, Pref-GRPO benefits from both components: relative-preference optimization is the key stabilizing factor, strengthened further by a dedicated pairwise reward model. A practical corollary is that practitioners with only scalar rewards can adopt win-rate fitting as a drop-in stability improvement.

**ZH** 这些结果支持两点结论。第一，此前 GRPO 方法中的不稳定，很大一部分源自目标的形式，而不只是奖励模型的不完善。第二，成对偏好奖励优于由分数导出的胜率，说明原生的成对监督比从被压缩的逐点分数推导出的排序提供更干净、更忠实的相对信号。简言之，Pref-GRPO 同时受益于两个组成部分：相对偏好优化是关键的稳定因素，专用的成对奖励模型则进一步强化了它。一个实用的推论是：只有标量奖励的从业者可以采用胜率拟合，作为一种直接替换的稳定性改进手段。

<!-- [原子块 · img]  -->

**EN** Fig. 10: Point-score-derived win-rate training alleviates reward hacking. Converting UnifiedReward scores into pairwise win rates substantially mitigates the dark-style drift observed under direct score maximization, supporting relative preferences (not the reward model itself) as the key stabilizing factor.

**ZH** 图 10：逐点分数导出的胜率训练缓解了奖励破解。把 UnifiedReward 分数转换为成对胜率，显著减轻了直接分数最大化下观察到的暗色风格漂移，支持“相对偏好（而非奖励模型本身）是关键稳定因素”这一结论。

**EN** TABLE VIII: Point-score-derived win rate vs. pairwise preference win rate. Compared to direct score maximization (“w/ UR (score)”), converting UnifiedReward scores into pairwise win rates (“w/ UR (score win rate)”) already improves stability; Pref-GRPO further benefits from a native pairwise preference reward. Best results are in bold, second-best are underlined.

**ZH** 表 VIII：逐点分数导出胜率与成对偏好胜率的比较。相对直接分数最大化（“w/ UR (score)”），把 UnifiedReward 分数转换为成对胜率（“w/ UR (score win rate)”）已提升稳定性；Pref-GRPO 进一步受益于原生的成对偏好奖励。最佳结果加粗，次优加下划线。

<!-- [原子块 · table] Model UniGen GenEval Unified Reward Pick Score Image Reward Aes. FLUX.1-dev 61.30 62.92 3.04 22.42 1.27 6.13 w/ UR (score) 63.62 67.28 3.14 22.88 1.38 6.31 w/ UR (score winrate) 64.32 68.13 3.20 22.91 -->

**EN** VII-C Wall-Clock Overhead of Pairwise Rewards

**ZH** VII-C 成对奖励的时钟开销

**EN** Although pairwise rewards require ⟦SLOT_88⟧ comparisons within each rollout group of size ⟦SLOT_89⟧, the practical question is whether this additional computation becomes a prohibitive bottleneck during training. To answer this, we measure wall-clock reward computation time when training FLUX.1-dev on ⟦SLOT_90⟧ H800 GPUs, with the reward inference service deployed on another 4 H800 GPUs via vLLM [31]; this isolates per-step cost from the multi-node overhead of the 64-GPU main setup. We compare two settings across different group sizes: (i) point-score rewards from UnifiedReward, and (ii) pairwise preference win-rate rewards used in Pref-GRPO.

**ZH** 尽管成对奖励在每个回放组内需要 ⟦SLOT_88⟧ 次比较（组规模为 ⟦SLOT_89⟧），实际问题是这些额外计算在训练中是否会成为难以承受的瓶颈。为回答这一点，我们测量了在 ⟦SLOT_90⟧ 张 H800 GPU 上训练 FLUX.1-dev 时的奖励计算时钟时间，奖励推理服务通过 vLLM [31] 部署在另外 4 张 H800 GPU 上；这样可以把每步开销与 64 GPU 主配置的多节点开销分离。我们比较了不同组规模下的两种设置：(i) 由 UnifiedReward 给出的逐点分数奖励；(ii) Pref-GRPO 使用的成对偏好胜率奖励。

**EN** TABLE IX: Wall-clock reward computing time per training step. “Requests/step” counts the number of reward-model forward computations invoked by each scheme in a training step.

**ZH** 表 IX：每训练步的奖励计算时钟时间。“Requests/step”统计每种方案在一步训练中调用的奖励模型前向计算次数。

<!-- [原子块 · table] Reward type Rollouts / group Requests / step Time / step Point score (UnifiedReward) 8 32 3 s 16 64 5 s Pairwise winrate (Ours) 8 112 7 s 12 264 14 s 16 480 22 s -->

**EN** Tab. IX shows that the added cost is moderate. Under the default setting ⟦SLOT_91⟧, pairwise win-rate rewards increase the per-step reward time from 3 s to 7 s, an additional 4 s of overhead. At ⟦SLOT_92⟧, the number of reward-model requests grows from 64 to 480 (⟦SLOT_93⟧), yet wall-clock reward time grows only from 5 s to 22 s (⟦SLOT_94⟧), far sublinear in the number of pairwise comparisons. Pairwise supervision is therefore effectively amortized by parallel reward serving.

**ZH** 表 IX 显示，额外开销适中。在默认设置 ⟦SLOT_91⟧ 下，成对胜率奖励把每步奖励时间从 3 秒增至 7 秒，即多出 4 秒开销。在 ⟦SLOT_92⟧ 下，奖励模型请求数从 64 增至 480（⟦SLOT_93⟧），而奖励计算的时钟时间仅从 5 秒增至 22 秒（⟦SLOT_94⟧），远低于与两两比较次数成正比的线性增长。因此成对监督的开销被并行的奖励服务有效地摊还了。

**EN** The main concern with pairwise rewards is theoretical complexity, not practical infeasibility. In our setting, ⟦SLOT_95⟧ already yields strong empirical gains (Tab. III, Figs. 2, 8), so the added reward latency remains modest relative to the training benefit. Overall, Pref-GRPO achieves a favorable computation–performance trade-off: substantially improved generation quality and mitigated reward hacking, with only limited wall-clock overhead.

**ZH** 成对奖励的主要顾虑是理论复杂度，而非实际不可行。在我们的设置中，⟦SLOT_95⟧ 已带来显著的实证增益（表 III、图 2、图 8），因此相对训练收益而言，额外的奖励延迟仍然有限。总的来看，Pref-GRPO 取得了良好的计算—性能权衡：生成质量大幅提升、奖励破解得到缓解，而时钟开销仅有小幅增加。

<!-- [原子块 · img]  -->

**EN** Fig. 11: Joint optimization of Pref-GRPO with a CLIP score reward. Adding CLIP improves semantic consistency while slightly reducing perceptual quality, but does not trigger reward hacking. The pairwise preference fitting acts as a stabilizing regularizer for the auxiliary score signal.

**ZH** 图 11：Pref-GRPO 与 CLIP 分数奖励的联合优化。加入 CLIP 提升了语义一致性，同时略微降低感知质量，但不触发奖励破解。成对偏好拟合对辅助分数信号起到了稳定正则项的作用。

**EN** TABLE X: Joint optimization of Pref-GRPO and CLIP-based reward score maximization. Best results are in bold.

**ZH** 表 X：Pref-GRPO 与基于 CLIP 的奖励分数最大化的联合优化。最佳结果加粗。

<!-- [原子块 · table] Model UniGen GenEval Unified Reward Pick Score Image Reward Aes. Pref-GRPO 69.46 70.53 3.26 23.02 1.44 6.52 w/ CLIP 70.02 71.26 3.18 22.86 1.41 6.44 -->

**EN** VII-D Joint Optimization with Auxiliary Score Rewards

**ZH** VII-D 与辅助分数奖励的联合优化

**EN** To examine whether score-based rewards can still provide useful auxiliary supervision, we add a CLIP [12] reward on top of Pref-GRPO and perform joint optimization. Here CLIP serves as a score-based reward signal that focuses more on semantic consistency between the prompt and the generated image. This experiment tests whether pairwise preference fitting can serve as a stabilizing objective while score-based rewards provide complementary semantic guidance.

**ZH** 为检验基于分数的奖励是否仍能提供有用的辅助监督，我们在 Pref-GRPO 之上加入一个 CLIP [12] 奖励并做联合优化。此处 CLIP 充当基于分数的奖励信号，更关注提示词与生成图像之间的语义一致性。该实验检验成对偏好拟合能否作为稳定目标，而基于分数的奖励提供互补的语义引导。

**EN** As shown in Tab. X, joint optimization improves semantic consistency on UniGenBench and GenEval, but slightly reduces image-quality-oriented metrics relative to vanilla Pref-GRPO. The qualitative results in Fig. 11 show the same trade-off: semantics improve, while perceptual quality drops mildly. Importantly, unlike pure score maximization, this setting does not exhibit obvious reward hacking. This suggests that pairwise preference fitting acts as a stabilizing regularizer in joint optimization, making it possible to incorporate auxiliary score rewards without collapsing to reward-hacked solutions.

**ZH** 如表 X 所示，联合优化提升了 UniGenBench 与 GenEval 上的语义一致性，但相对原始 Pref-GRPO 略微降低了面向图像质量的指标。图 11 的定性结果呈现同样的权衡：语义改善，而感知质量略有下降。重要的是，与纯分数最大化不同，该设置并未出现明显的奖励破解。这说明成对偏好拟合在联合优化中充当了稳定正则项，使得纳入辅助分数奖励而不坍缩为被奖励破解的解成为可能。

**EN** VII-E Robustness to Noisy Preferences

**ZH** VII-E 对噪声偏好的鲁棒性

**EN** To test robustness to imperfect preference supervision, we inject synthetic noise into the pairwise reward during training by independently flipping each pairwise outcome with probability ⟦SLOT_96⟧, roughly matching typical human-disagreement rates on image preferences.

**ZH** 为检验对不完美偏好监督的鲁棒性，我们在训练中向成对奖励注入合成噪声：以概率 ⟦SLOT_96⟧ 独立翻转每一个成对比较的结果，该概率大致对应图像偏好上典型的人类分歧率。

**EN** As shown in Tab. XI, Pref-GRPO remains strong under noisy preferences and consistently outperforms all point score-based baselines. Although the injected noise causes a small drop relative to the clean Pref-GRPO model, the degradation is limited across all metrics. This result suggests that pairwise preference optimization remains robust under moderate label corruption, which is important in practical settings where preference annotations are often noisy, inconsistent, or partially unreliable.

**ZH** 如表 XI 所示，Pref-GRPO 在带噪偏好下依然强劲，持续优于所有基于逐点分数的基线。尽管注入的噪声使其相对干净的 Pref-GRPO 模型有小幅下降，但在所有指标上的退化都很有限。这一结果表明，成对偏好优化在中等程度的标签损坏下仍保持鲁棒——在实际场景中，偏好标注常常带噪、不一致或部分不可靠，这一点尤为重要。

**EN** TABLE XI: Robustness of Pref-GRPO under 10% preference noise. The noisy variant flips each pairwise preference outcome with probability ⟦SLOT_97⟧ during training.

**ZH** 表 XI：Pref-GRPO 在 10% 偏好噪声下的鲁棒性。带噪变体在训练中以概率 ⟦SLOT_97⟧ 翻转每个成对偏好结果。

<!-- [原子块 · table] Method UniGen T2I- Comp GenEval Unified Reward Pick Score FLUX.1.dev 61.30 48.17 62.92 3.04 22.42 w/ HPSv2+CLIP 58.77 46.77 59.31 3.09 22.62 w/ UnifiedReward 63.62 50.20 67.28 3.14 22.88 w/ Pref-GRPO  -->

**EN** VII-F Human Validation of the UniGenBench Evaluator

**ZH** VII-F UniGenBench 评测器的人工验证

**EN** To verify the reliability of the automatic judge used in UniGenBench, we conduct a testpoint-level agreement study between Gemini-2.5-Pro [14] and human annotators. We sample 400 held-out prompt-image-testpoint triplets from benchmark predictions generated by models of varying strengths, with 40 triplets for each of the 10 primary dimensions. Each triplet contains a prompt, a generated image, and one explicit testpoint description. Five annotators independently judge whether the image satisfies the specified testpoint using the same binary protocol as in benchmark evaluation, and the human majority vote is taken as the reference label.

**ZH** 为验证 UniGenBench 所用自动评判器的可靠性，我们开展了一项 Gemini-2.5-Pro [14] 与人类标注者在测试点级别的一致性研究。我们从不同强度模型的基准预测结果中采样 400 条留出的“提示词—图像—测试点”三元组，10 个主维度各 40 条。每个三元组包含一条提示词、一幅生成图像和一条明确的测试点描述。五名标注者依据与基准评测相同的二值规则，独立判断该图像是否满足指定测试点，并以人类多数投票作为参考标签。

**EN** We report inter-annotator agreement, Gemini-vs.-human-majority accuracy, macro-F1, and Cohen’s ⟦SLOT_98⟧ in Tab. XII. These metrics provide complementary views of evaluator reliability: inter-annotator agreement reflects the intrinsic ambiguity of each dimension and serves as a practical human reference ceiling, Gemini-vs.-human-majority accuracy measures direct agreement with human judgment, macro-F1 prevents class imbalance from dominating the result, and ⟦SLOT_99⟧ discounts agreement that may occur by chance. Gemini-2.5-Pro achieves strong overall consistency with human judgments. Agreement is highest on more direct dimensions such as Style, Attribute, and Layout, while more abstract dimensions such as Relationship, Compound, and Logical Reasoning remain relatively more challenging. This tracking behavior supports Gemini-2.5-Pro’s use as the UniGenBench evaluator.

**ZH** 我们在表 XII 中上报标注者间一致性、Gemini 对人类多数投票的准确率、macro-F1 以及 Cohen's ⟦SLOT_98⟧。这些指标从互补角度刻画评测器的可靠性：标注者间一致性反映各维度的固有歧义，可视为实用的人类参考上限；Gemini 对人类多数投票的准确率衡量与人类判断的直接一致程度；macro-F1 防止类别不平衡主导结果；而 ⟦SLOT_99⟧ 则剔除了偶然达成的一致。Gemini-2.5-Pro 与人类判断整体上高度一致。一致性在 Style、Attribute、Layout 等更直接的维度上最高，而 Relationship、Compound、Logical Reasoning 等更抽象的维度仍相对更具挑战。这种跟踪表现支持将 Gemini-2.5-Pro 用作 UniGenBench 的评测器。

**EN** TABLE XII: Human validation of Gemini-2.5-Pro as the UniGenBench evaluator. We report Inter-Ann. Agr., Gemini-vs.-human-majority Acc., Macro-F1, and Cohen’s ⟦SLOT_100⟧ for each primary dimension.

**ZH** 表 XII：Gemini-2.5-Pro 作为 UniGenBench 评测器的人工验证。我们逐主维度上报 Inter-Ann. Agr.、Gemini 对人类多数投票的 Acc.、Macro-F1 与 Cohen's ⟦SLOT_100⟧。

<!-- [原子块 · table] Dimension Inter-Ann. Agr. Acc. Macro- F1 𝜿 \boldsymbol{\kappa} Overall 0.92 0.83 0.82 0.66 Style 0.96 0.90 0.89 0.76 World Know. 0.91 0.82 0.81 0.64 Attribute 0.93 0.84 0.83 0.67 Action 0.91 0.82 0.81 -->

**EN** VIII Conclusion

**ZH** VIII 结论

**EN** This paper addresses two limitations in current T2I research: unstable GRPO optimization under pointwise reward score maximization, and the lack of fine-grained benchmarks for diagnosing semantic consistency. To this end, we propose Pref-GRPO, which replaces absolute score maximization with pairwise preference fitting, and UniGenBench, which evaluates semantic consistency through fine-grained testpoints spanning diverse prompt themes and evaluation dimensions. Extensive experiments show that Pref-GRPO yields more stable training, alleviates reward hacking, and achieves consistently stronger semantic consistency on both in-domain and out-of-domain benchmarks. Besides, UniGenBench reveals where strong T2I models still fail, especially on more demanding dimensions such as relationship understanding, compositional instruction following, logical reasoning, and text rendering. We hope these two contributions together provide a more reliable training objective and a more informative evaluation protocol for future T2I reinforcement learning research.

**ZH** 本文针对当前 T2I 研究中的两处局限：逐点奖励分数最大化下 GRPO 优化的不稳定，以及缺乏用于诊断语义一致性的细粒度基准。为此，我们提出 Pref-GRPO——用成对偏好拟合取代绝对分数最大化，以及 UniGenBench——通过覆盖多样提示词主题与评测维度的细粒度测试点来评估语义一致性。大量实验表明，Pref-GRPO 带来更稳定的训练，缓解奖励破解，并在域内与域外基准上持续取得更强的语义一致性。此外，UniGenBench 揭示了强 T2I 模型仍在何处失败，尤其是在关系理解、组合式指令遵循、逻辑推理与文本渲染等要求更高的维度上。我们希望这两项贡献共同为未来的 T2I 强化学习研究提供更可靠的训练目标与更具信息量的评测协议。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] [1] J. Liu, G. Liu, J. Liang, Y. Li, J. Liu, X. Wang, P. Wan, D. Zhang, and W. Ouyang (2025) Flow-grpo: training flow matching models via online rl . arXiv preprint arXiv:2505.05470 . Cited by: §I , § -->

<!-- [原子块 · verbatim] [2] J. Li, Y. Cui, T. Huang, Y. Ma, C. Fan, M. Yang, and Z. Zhong (2025) MixGRPO: unlocking flow-based grpo efficiency with mixed ode-sde . arXiv preprint arXiv:2507.21802 . Cited by: §I , §III , §IV- -->

<!-- [原子块 · verbatim] [3] Z. Xue, J. Wu, Y. Gao, F. Kong, L. Zhu, M. Chen, Z. Liu, W. Liu, Q. Guo, W. Huang, et al. (2025) DanceGRPO: unleashing grpo on visual generation . arXiv preprint arXiv:2505.07818 . Cited by: §I ,  -->

<!-- [原子块 · verbatim] [4] X. He, S. Fu, Y. Zhao, W. Li, J. Yang, D. Yin, F. Rao, and B. Zhang (2025) TempFlow-grpo: when timing matters for grpo in flow mdels . arXiv preprint arXiv:2508.04324 . Cited by: §I , §III , §IV-B -->

<!-- [原子块 · verbatim] [5] D. Ghosh, H. Hajishirzi, and L. Schmidt (2023) Geneval: an object-focused framework for evaluating text-to-image alignment . NIPS 36 , pp. 52132–52152 . Cited by: §I , §I , §II , §V , §VI-A . -->

<!-- [原子块 · verbatim] [6] K. Huang, K. Sun, E. Xie, Z. Li, and X. Liu (2023) T2i-compbench: a comprehensive benchmark for open-world compositional text-to-image generation . NIPS 36 , pp. 78723–78747 . Cited by: §I , §I ,  -->

<!-- [原子块 · verbatim] [7] X. Wei, J. Zhang, Z. Wang, H. Wei, Z. Guo, and L. Zhang (2025) TIIF-bench: how does your t2i model follow your instructions? . arXiv preprint arXiv:2506.02161 . Cited by: §I , §I , §II , §V . -->

<!-- [原子块 · verbatim] [8] Y. Wang, Y. Zang, H. Li, C. Jin, and J. Wang (2025) Unified reward model for multimodal understanding and generation . arXiv preprint arXiv:2503.05236 . Cited by: §I , §III , §IV-B , §VI-A , §VI-A -->

<!-- [原子块 · verbatim] [9] X. Wu, Y. Hao, K. Sun, Y. Chen, F. Zhu, R. Zhao, and H. Li (2023) Human preference score v2: a solid benchmark for evaluating human preferences of text-to-image synthesis . arXiv preprint arXiv:23 -->

<!-- [原子块 · verbatim] [10] Y. Kirstain, A. Polyak, U. Singer, S. Matiana, J. Penna, and O. Levy (2023) Pick-a-pic: an open dataset of user preferences for text-to-image generation . NIPS 36 , pp. 36652–36663 . Cited by: §I -->

<!-- [原子块 · verbatim] [11] D. Guo, D. Yang, H. Zhang, J. Song, R. Zhang, R. Xu, Q. Zhu, S. Ma, P. Wang, X. Bi, et al. (2025) Deepseek-r1: incentivizing reasoning capability in llms via reinforcement learning . arXiv prepri -->

<!-- [原子块 · verbatim] [12] A. Radford, J. W. Kim, C. Hallacy, A. Ramesh, G. Goh, S. Agarwal, G. Sastry, A. Askell, P. Mishkin, J. Clark, et al. (2021) Learning transferable visual models from natural language supervision . -->

<!-- [原子块 · verbatim] [13] Y. Wang, Z. Li, Y. Zang, C. Wang, Q. Lu, C. Jin, and J. Wang (2025) Unified multimodal chain-of-thought reward model through reinforcement fine-tuning . arXiv preprint arXiv:2505.03318 . Cited by -->

<!-- [原子块 · verbatim] [14] Y. Huang and L. F. Yang (2025) Gemini 2.5 pro capable of winning gold at imo 2025 . arXiv preprint arXiv:2507.15855 . Cited by: §I , §VII-F . -->

<!-- [原子块 · verbatim] [15] A. Hurst, A. Lerer, A. P. Goucher, A. Perelman, A. Ramesh, A. Clark, A. Ostrow, A. Welihinda, A. Hayes, A. Radford, et al. (2024) Gpt-4o system card . arXiv preprint arXiv:2410.21276 . Cited by:  -->

<!-- [原子块 · verbatim] [16] Y. Gao, L. Gong, Q. Guo, X. Hou, Z. Lai, F. Li, L. Li, X. Lian, C. Liao, L. Liu, et al. (2025) Seedream 3.0 technical report . arXiv preprint arXiv:2504.11346 . Cited by: §I , §VI-C . -->

<!-- [原子块 · verbatim] [17] C. Saharia, W. Chan, S. Saxena, L. Li, J. Whang, E. L. Denton, K. Ghasemipour, R. Gontijo Lopes, B. Karagol Ayan, T. Salimans, et al. (2022) Photorealistic text-to-image diffusion models with dee -->

<!-- [原子块 · verbatim] [18] C. Wu, J. Li, J. Zhou, J. Lin, K. Gao, K. Yan, S. Yin, S. Bai, X. Xu, Y. Chen, et al. (2025) Qwen-image technical report . arXiv preprint arXiv:2508.02324 . Cited by: §I , §VI-C , §VI-D . -->

<!-- [原子块 · verbatim] [19] Q. Cai, J. Chen, Y. Chen, Y. Li, F. Long, Y. Pan, Z. Qiu, Y. Zhang, F. Gao, P. Xu, et al. (2025) HiDream-i1: a high-efficient image generative foundation model with sparse diffusion transformer . -->

<!-- [原子块 · verbatim] [20] C. Deng, D. Zhu, K. Li, C. Gou, F. Li, Z. Wang, S. Zhong, W. Yu, X. Nie, Z. Song, et al. (2025) Emerging properties in unified multimodal pretraining . arXiv preprint arXiv:2505.14683 . Cited by: -->

<!-- [原子块 · verbatim] [21] X. Xie and D. Gong (2025) DyMO: training-free diffusion model alignment with dynamic multi-objective scheduling . In CVPR , pp. 13220–13230 . Cited by: §II . -->

<!-- [原子块 · verbatim] [22] K. Yang, J. Tao, J. Lyu, C. Ge, J. Chen, W. Shen, X. Zhu, and X. Li (2024) Using human feedback to fine-tune diffusion models without any reward model . In CVPR , pp. 8941–8951 . Cited by: §II . -->

<!-- [原子块 · verbatim] [23] B. Wallace, M. Dang, R. Rafailov, L. Zhou, A. Lou, S. Purushwalkam, S. Ermon, C. Xiong, S. Joty, and N. Naik (2024) Diffusion model alignment using direct preference optimization . In CVPR , pp.  -->

<!-- [原子块 · verbatim] [24] R. Rafailov, A. Sharma, E. Mitchell, C. D. Manning, S. Ermon, and C. Finn (2023) Direct preference optimization: your language model is secretly a reward model . NIPS 36 , pp. 53728–53741 . Cited -->

<!-- [原子块 · verbatim] [25] C. Tong, Z. Guo, R. Zhang, W. Shan, X. Wei, Z. Xing, H. Li, and P. Heng (2025) Delving into rl for image generation with cot: a study on dpo vs. grpo . arXiv preprint arXiv:2505.17017 . Cited by: -->

<!-- [原子块 · verbatim] [26] Y. Niu, M. Ning, M. Zheng, W. Jin, B. Lin, P. Jin, J. Liao, C. Feng, K. Ning, B. Zhu, et al. (2025) Wise: a world knowledge-informed semantic evaluation for text-to-image generation . arXiv prepr -->

<!-- [原子块 · verbatim] [27] X. Liu, C. Gong, and Q. Liu (2022) Flow straight and fast: learning to generate and transfer data with rectified flow . arXiv preprint arXiv:2209.03003 . Cited by: §IV-A . -->

<!-- [原子块 · verbatim] [28] Y. Lipman, R. T. Chen, H. Ben-Hamu, M. Nickel, and M. Le (2022) Flow matching for generative modeling . arXiv preprint arXiv:2210.02747 . Cited by: §IV-A . -->

<!-- [原子块 · verbatim] [29] K. Black, M. Janner, Y. Du, I. Kostrikov, and S. Levine (2023) Training diffusion models with reinforcement learning . arXiv preprint arXiv:2305.13301 . Cited by: §IV-A . -->

<!-- [原子块 · verbatim] [30] B. F. Labs. (2024) Flux . https://github.com/black-forest-labs/flux . Cited by: §VI-A , §VI-C , §VI-C . -->

<!-- [原子块 · verbatim] [31] W. Kwon, Z. Li, S. Zhuang, Y. Sheng, L. Zheng, C. H. Yu, J. Gonzalez, H. Zhang, and I. Stoica (2023) Efficient memory management for large language model serving with pagedattention . In SOSP , p -->

<!-- [原子块 · verbatim] [32] J. Xu, X. Liu, Y. Wu, Y. Tong, Q. Li, M. Ding, J. Tang, and Y. Dong (2023) Imagereward: learning and evaluating human preferences for text-to-image generation . NIPS 36 , pp. 15903–15935 . Cited  -->

<!-- [原子块 · verbatim] [33] C. Schuhmann. (2022) Laion aesthetics . https://github.com/LAION-AI/aesthetic-predictor . Cited by: §VI-A . -->

<!-- [原子块 · verbatim] [34] J. Xie, Z. Yang, and M. Z. Shou (2025) Show-o2: improved native unified multimodal models . arXiv preprint arXiv:2506.15564 . Cited by: §VI-C . -->

<!-- [原子块 · verbatim] [35] R. Rombach, A. Blattmann, D. Lorenz, P. Esser, and B. Ommer (2021) High-resolution image synthesis with latent diffusion models . External Links: 2112.10752 Cited by: §VI-C . -->

<!-- [原子块 · verbatim] [36] M. Ding, Z. Yang, W. Hong, W. Zheng, C. Zhou, D. Yin, J. Lin, X. Zou, Z. Shao, H. Yang, and J. Tang (2021) CogView: mastering text-to-image generation via transformers . arXiv preprint arXiv:2105 -->

<!-- [原子块 · verbatim] [37] Z. Li, J. Zhang, Q. Lin, J. Xiong, Y. Long, et al. (2024) Hunyuan-dit: a powerful multi-resolution diffusion transformer with fine-grained chinese understanding . External Links: 2405.08748 Cited -->

<!-- [原子块 · verbatim] [38] D. Li, A. Kamko, E. Akhgari, A. Sabet, L. Xu, and S. Doshi (2024) Playground v2. 5: three insights towards enhancing aesthetic quality in text-to-image generation . arXiv preprint arXiv:2402.1724 -->

<!-- [原子块 · verbatim] [39] C. Wu, X. Chen, Z. Wu, Y. Ma, X. Liu, Z. Pan, W. Liu, Z. Xie, X. Yu, C. Ruan, et al. (2025) Janus: decoupling visual encoding for unified multimodal understanding and generation . In CVPR , pp. 1 -->

<!-- [原子块 · verbatim] [40] X. Chen, Z. Wu, X. Liu, Z. Pan, W. Liu, Z. Xie, X. Yu, and C. Ruan (2025) Janus-pro: unified multimodal understanding and generation with data and model scaling . arXiv preprint arXiv:2501.17811  -->

<!-- [原子块 · verbatim] [41] Y. Ma, X. Liu, X. Chen, W. Liu, C. Wu, Z. Wu, Z. Pan, Z. Xie, H. Zhang, X. yu, L. Zhao, Y. Wang, J. Liu, and C. Ruan (2024) JanusFlow: harmonizing autoregression and rectified flow for unified mu -->

<!-- [原子块 · verbatim] [42] X. Wang, X. Zhang, Z. Luo, Q. Sun, Y. Cui, J. Wang, F. Zhang, Y. Wang, Z. Li, Q. Yu, et al. (2024) Emu3: next-token prediction is all you need . arXiv preprint arXiv:2409.18869 . Cited by: §VI-C  -->

<!-- [原子块 · verbatim] [43] J. Chen, Z. Xu, X. Pan, Y. Hu, C. Qin, T. Goldstein, L. Huang, T. Zhou, S. Xie, S. Savarese, et al. (2025) Blip3-o: a family of fully open unified multimodal models-architecture, training and dat -->
