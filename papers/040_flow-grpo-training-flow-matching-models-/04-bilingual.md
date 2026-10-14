# Flow-GRPO：用在线强化学习训练流匹配模型

> 原标题：Flow-GRPO: Training Flow Matching Models via Online RL
> 作者：Jie Liu, Gongye Liu, Jiajun Liang, Yangguang Li, Jiaheng Liu, Xintao Wang, Pengfei Wan, Di Zhang, Wanli Ouyang · arXiv:2505.05470 · 2025-05-08

<!-- [原子块 · verbatim] Flow-GRPO: Training Flow Matching Models via Online RL -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] We propose Flow-GRPO, the first method to integrate online policy gradient reinforcement learning (RL) into flow matching models. Our approach uses two key strategies: (1) an ODE-to-SDE conversion tha -->

<!-- [原子块 · img]  -->

**EN** Figure 1: (a) GenEval performance rises steadily throughout Flow-GRPO’s training and outperforms GPT-4o. (b) Image quality metrics on DrawBench [1] remain essentially unchanged. (c) Human Preference Scores on DrawBench improves after training. Results show that Flow-GRPO enhances the desired capability while preserving image quality and exhibiting minimal reward-hacking.

**ZH** 图 1：（a）Flow-GRPO 训练过程中 GenEval 性能稳步上升，并最终超过 GPT-4o。（b）DrawBench [1] 上的图像质量指标基本保持不变。（c）DrawBench 上的人类偏好分数在训练后提升。结果表明，Flow-GRPO 增强了目标能力，同时保持了图像质量，且几乎未出现奖励黑客现象。

**EN** 1 Introduction

**ZH** 1 引言

**EN** Flow matching [2, 3] models have become dominant in image generation [4, 5] due to their solid theoretical foundations and strong performance in producing high quality images. However, they often struggle with composing complex scenes involving multiple objects, attributes, and relationships [6, 7], as well as text rendering [8]. At the same time, online reinforcement learning (RL) [9] has proven highly effective in enhancing the reasoning capabilities of large language models (LLMs) [10, 11]. While previous research has mainly focused on applying RL to early diffusion-based generative models [12] and offline RL techniques like direct preference optimization [13] for flow-based generative models [14, 15], the potential of online RL in advancing flow matching generative models remains largely unexplored. In this study, we explore how online RL can be leveraged to effectively improve flow matching models.

**ZH** 流匹配（flow matching）[2, 3] 模型凭借扎实的理论基础与生成高质量图像的强劲表现，已在图像生成领域占据主导地位 [4, 5]。然而，它们在组合涉及多个物体、属性与关系的复杂场景 [6, 7] 以及文字渲染 [8] 上往往力有不逮。与此同时，在线强化学习（RL）[9] 已被证明在提升大语言模型（LLM）推理能力上极为有效 [10, 11]。尽管以往研究主要聚焦于把 RL 应用于早期的基于扩散的生成模型 [12]，以及把直接偏好优化 [13] 等离线 RL 技术用于基于流的生成模型 [14, 15]，在线 RL 在推进流匹配生成模型上的潜力仍基本未被探索。本文研究如何利用在线 RL 有效改进流匹配模型。

**EN** Training flow models with RL presents several critical challenges: (1) Flow models rely on a deterministic generative process based on ODEs [3], meaning they cannot sample stochastically during inference. In contrast, RL relies on stochastic sampling to explore the environment, learning by trying different actions and improving based on rewards. This need for stochasticity in RL conflicts with the deterministic nature of flow matching models. (2) Online RL depends on efficient sampling to collect training data, but flow models typically require many iterative steps to generate each sample, limiting efficiency. This issue is more pronounced with large models [5, 4]. To make RL practical for tasks like image or video generation, improving sampling efficiency is essential.

**ZH** 用 RL 训练流模型面临若干关键挑战：（1）流模型依赖基于常微分方程（ODE）的确定性生成过程 [3]，这意味着它们在推理时无法随机采样。相反，RL 依赖随机采样来探索环境，通过尝试不同动作并依据奖励改进。RL 对随机性的这一需求与流匹配模型的确定性本质相冲突。（2）在线 RL 依赖高效采样来收集训练数据，但流模型通常生成每个样本都要大量迭代步骤，限制了效率；这一问题在大型模型上更为突出 [5, 4]。要让 RL 在图像或视频生成等任务上切实可行，提升采样效率至关重要。

**EN** To address these challenges, we propose Flow-GRPO, which integrates GRPO [16] into flow matching models for text-to-image (T2I) generation, using two key strategies. First, we adopt the ODE-to-SDE strategy to overcome the deterministic nature of the original flow model. By converting the ODE-based flow into an equivalent Stochastic Differential Equation (SDE) framework, we introduce randomness while preserving the original marginal distributions. Second, to improve sampling efficiency in online RL, we apply the Denoising Reduction strategy, which reduces denoising steps during training while keeping the full schedule during inference. Our experiments show that using fewer steps maintains performance while significantly reducing data generation costs.

**ZH** 为应对这些挑战，我们提出 Flow-GRPO，它把 GRPO [16] 引入流匹配模型用于文生图（T2I）生成，并采用两项关键策略。第一，我们采用 ODE-to-SDE 策略来克服原始流模型的确定性本质：通过把基于 ODE 的流转换为等价的随机微分方程（SDE）框架，在保留原始边缘分布的同时引入随机性。第二，为提升在线 RL 中的采样效率，我们应用降噪步数缩减（Denoising Reduction）策略，在训练时减少降噪步数，而在推理时保留完整的时间步调度。实验表明，使用更少的步数在保持性能的同时显著降低了数据生成成本。

**EN** We evaluate Flow-GRPO on T2I tasks with various reward types. (1) Verifiable rewards, using the GenEval [17] benchmark and visual text rendering task. GenEval includes compositional image generation tasks (e.g., generating specific object counts, colors, and spatial relationships), which can be automatically assessed with object detection methods. Flow-GRPO improves the accuracy of Stable Diffusion 3.5 Medium (SD3.5-M) [4] from 63% to 95% on GenEval, outperforming the state-of-the-art GPT-4o [18] model. For visual text rendering, SD3.5-M’s accuracy increases from 59% to 92%, greatly enhancing its text generation ability. (2) Model-based rewards, such as the human preference Pickscore [19] reward. These results show that our framework is task independent, demonstrating its generalizability and robustness. Importantly, all improvements are achieved with very little reward hacking, as demonstrated in Figure 1.

**ZH** 我们在多种奖励类型的 T2I 任务上评估 Flow-GRPO。（1）可验证奖励，使用 GenEval [17] 基准与视觉文字渲染任务。GenEval 包含组合式图像生成任务（例如生成特定数量的物体、颜色与空间关系），可用目标检测方法自动评估。Flow-GRPO 把 Stable Diffusion 3.5 Medium（SD3.5-M）[4] 在 GenEval 上的准确率从 63% 提升到 95%，超过当前最佳的 GPT-4o [18] 模型。在视觉文字渲染上，SD3.5-M 的准确率从 59% 提升到 92%，大幅增强了其文字生成能力。（2）基于模型的奖励，如人类偏好奖励 Pickscore [19]。这些结果表明我们的框架与任务无关，体现出其通用性与稳健性。重要的是，所有改进都是在极少奖励黑客的情况下取得的，如图 1 所示。

**EN** To summarize, the contributions of Flow-GRPO are as follows:

**ZH** 总之，Flow-GRPO 的贡献如下：

**EN** • We are the first to introduce GRPO to flow matching models by converting deterministic ODE sampling into SDE sampling, showing the effectiveness of online RL for T2I tasks. Flow-GRPO improves SD3.5-M accuracy from 63% to 95% without noticeably compromising image quality.

**ZH** • 我们首次把 GRPO 引入流匹配模型，通过把确定性 ODE 采样转换为 SDE 采样，展示了在线 RL 在 T2I 任务上的有效性。Flow-GRPO 把 SD3.5-M 的准确率从 63% 提升到 95%，且未明显损害图像质量。

**EN** • We find that online RL for flow matching models does not require the standard long timesteps for training sample collection. By using fewer denoising steps during training and retaining the original steps during testing, we can significantly accelerate the training process.

**ZH** • 我们发现，面向流匹配模型的在线 RL 并不需要标准的长时间步来采集训练样本。在训练时使用更少的降噪步数、在测试时保留原始步数，即可显著加速训练过程。

**EN** • We show that the Kullback-Leibler (KL) constraint effectively prevents reward hacking, where reward increases at the cost of image quality or diversity. KL regularization is not empirically equivalent to early stopping. With a proper KL term, we can match the high reward of the KL-free version while preserving image quality, albeit with longer training.

**ZH** • 我们证明 Kullback-Leibler（KL）约束能有效防止奖励黑客——即奖励上升却以图像质量或多样性为代价。KL 正则化在实证上并不等价于早停。借助恰当的 KL 项，我们可以在保持图像质量的同时达到无 KL 版本的高奖励，尽管需要更长的训练时间。

**EN** 2 Related Work

**ZH** 2 相关工作

**EN** RL for LLM.

**ZH** 面向 LLM 的 RL。

**EN** Online RL has effectively improved the reasoning abilities of LLMs, such as DeepSeek-R1 [10] and OpenAI-o1 [11], using policy gradient methods like PPO [20] or value-free GRPO [16]. GRPO is more memory efficient by removing the need for a value network, so we adopt it in this work. PPO can also be applied to flow matching in a similar way.

**ZH** 在线 RL 借助 PPO [20] 或无价值网络的 GRPO [16] 等策略梯度方法，有效提升了 LLM 的推理能力，例如 DeepSeek-R1 [10] 与 OpenAI-o1 [11]。GRPO 通过省去价值网络而在显存上更为高效，因此我们在本工作中采用它。PPO 也可以类似地应用于流匹配。

**EN** Diffusion and Flow Matching.

**ZH** 扩散与流匹配。

**EN** Diffusion models [21, 22, 23] add Gaussian noise to data and train a neural network to reverse the process. Sampling uses discrete DDPM steps or probability flow SDE solvers to generate high-fidelity outputs. Flow matching [2, 3] learns a continuous-time normalizing flow by directly matching the velocity field, allowing efficient deterministic sampling with only a few ODE steps. It achieves competitive FID with far fewer denoising steps than diffusion, making it the dominant choice in recent image [4, 5] and video [24, 25, 26, 27] generation models. Recent work [28, 29] unifies diffusion and flow models under an SDE/ODE framework. Our work builds on their theoretical foundations and introduces GRPO to flow-based models.

**ZH** 扩散模型 [21, 22, 23] 向数据加入高斯噪声，并训练神经网络逆转这一过程；采样时使用离散的 DDPM 步或概率流 SDE 求解器来生成高保真输出。流匹配 [2, 3] 通过直接匹配速度场来学习一个连续时间归一化流，只需少量 ODE 步即可实现高效的确定性采样。它以远少于扩散的降噪步数取得有竞争力的 FID，因而成为近期图像 [4, 5] 与视频 [24, 25, 26, 27] 生成模型的主流选择。近期工作 [28, 29] 在 SDE/ODE 框架下统一了扩散模型与流模型。我们的工作建立在他们的理论基础之上，并把 GRPO 引入基于流的模型。

**EN** Alignment for T2I.

**ZH** 面向 T2I 的对齐。

**EN** Recent efforts to align pretrained T2I models with human preferences follow five main directions: (1) direct fine-tuning with differentiable rewards [30, 31, 32, 33]; (2) Reward Weighted Regression (RWR) [34, 35, 36, 37]; (3) Direct Preference Optimization (DPO) and variants [38, 39, 14, 40, 41, 42, 43, 44, 45, 46]; (4) PPO-style policy gradients [47, 48, 49, 50, 51, 52]; (5) training-free alignment methods [53, 54, 55]. These methods have successfully aligned T2I models with human preferences, improving aesthetics and semantic consistency. Building on this progress, we introduce GRPO for flow matching models, the backbone of today’s state-of-the-art T2I systems. Concurrent work [56] applies GRPO to text-to-speech flow models, but instead of converting the ODE to an SDE to inject stochasticity, they reformulate velocity prediction by estimating a Gaussian distribution (predicting both the mean and variance of velocity), which requires retraining the pre-trained model. Another study [57] also explores SDE-based stochasticity but focuses on inference-time scaling.

**ZH** 近期把预训练 T2I 模型与人类偏好对齐的工作主要沿五个方向：（1）用可微奖励做直接微调 [30, 31, 32, 33]；（2）奖励加权回归（RWR）[34, 35, 36, 37]；（3）直接偏好优化（DPO）及其变体 [38, 39, 14, 40, 41, 42, 43, 44, 45, 46]；（4）PPO 式策略梯度 [47, 48, 49, 50, 51, 52]；（5）免训练对齐方法 [53, 54, 55]。这些方法已成功使 T2I 模型与人类偏好对齐，改善了美学与语义一致性。在这一进展之上，我们把 GRPO 引入流匹配模型——当今最佳 T2I 系统的骨干。同期工作 [56] 把 GRPO 应用于文生语音的流模型，但他们并非通过把 ODE 转换为 SDE 来注入随机性，而是通过估计高斯分布（同时预测速度的均值与方差）来重构速度预测，这需要重新训练预训练模型。另一项研究 [57] 也探索了基于 SDE 的随机性，但聚焦于推理时扩展。

**EN** 3 Preliminaries

**ZH** 3 预备知识

**EN** In this section, we introduce the mathematical formulation of flow matching and describe how the denoising process can be mapped as a multi-step MDP.

**ZH** 本节介绍流匹配的数学形式，并描述如何把降噪过程映射为一个多步 MDP。

**EN** Flow Matching.

**ZH** 流匹配。

**EN** Let ⟦SLOT_0⟧ be a data sample from the true distribution, and ⟦SLOT_1⟧ denote a noise sample. Recent advanced image-generation models (e.g., [4, 5]) and video-generation models (e.g., [24, 26, 25, 27]) adopt the Rectified Flow [3] framework, which defines the “noised” data ⟦SLOT_2⟧ as

**ZH** 设 ⟦SLOT_0⟧ 为来自真实分布的数据样本，⟦SLOT_1⟧ 表示噪声样本。近期先进的图像生成模型（如 [4, 5]）与视频生成模型（如 [24, 26, 25, 27]）采用 Rectified Flow [3] 框架，该框架把“加噪”后的数据 ⟦SLOT_2⟧ 定义为

<!-- [原子块 · table] 𝒙 t = ( 1 − t ) ​ 𝒙 0 + t ​ 𝒙 1 , {\bm{x}}_{t}=(1-t)\,{\bm{x}}_{0}\;+\;t\,{\bm{x}}_{1}, (1) -->

**EN** for ⟦SLOT_3⟧. Then a transformer model are trained to directly regress the velocity field ⟦SLOT_4⟧ by minimizing the Flow Matching objective [2, 3]:

**ZH** 对 ⟦SLOT_3⟧ 成立。随后训练一个 transformer 模型，通过最小化流匹配目标 [2, 3] 直接回归速度场 ⟦SLOT_4⟧：

<!-- [原子块 · table] ℒ ⁡ ( θ ) = 𝔼 t , 𝒙 0 ∼ X 0 , 𝒙 1 ∼ X 1 ​ [ ‖ 𝒗 − 𝒗 θ ​ ( 𝒙 t , t ) ‖ 2 ] , \mathcal{L}(\theta)=\mathbb{E}_{t,\;{\bm{x}}_{0}\sim X_{0},\;{\bm{x}}_{1}\sim X_{1}}\bigl[\;\|{\bm{v}}\;-\;{\bm{v}}_{\theta} -->

**EN** where the target velocity field is ⟦SLOT_5⟧.

**ZH** 其中目标速度场为 ⟦SLOT_5⟧。

<!-- [原子块 · img]  -->

**EN** Figure 2: Overview of Flow-GRPO. Given a prompt set, we introduce an ODE-to-SDE strategy to enable stochastic sampling for online RL. With Denoising Reduction (only T = 10 steps), we efficiently gather low-quality but still informative trajectories. Rewards from these trajectories feed the GRPO loss, which updates the model online and yields an aligned policy.

**ZH** 图 2：Flow-GRPO 概览。给定一组提示，我们引入 ODE-to-SDE 策略以实现面向在线 RL 的随机采样；借助降噪步数缩减（仅 T = 10 步），我们高效地采集出质量偏低但仍富含信息的轨迹。来自这些轨迹的奖励输入 GRPO 损失，在线更新模型，得到一个对齐后的策略。

**EN** Denoising as an MDP.

**ZH** 把降噪视为 MDP。

**EN** As shown in [12], the iterative denoising process in flow matching models can be formulated as a Markov Decision Process (MDP) ⟦SLOT_6⟧. The state at step ⟦SLOT_7⟧ is ⟦SLOT_8⟧, the action is the denoised sample ⟦SLOT_9⟧ predicted by the model, and the policy is ⟦SLOT_10⟧. The transition is deterministic: ⟦SLOT_11⟧, and the initial state distribution is ⟦SLOT_12⟧, where ⟦SLOT_13⟧ is the Dirac delta distribution centered at ⟦SLOT_14⟧. The reward is only given at the final step: ⟦SLOT_15⟧ if ⟦SLOT_16⟧, and 0 otherwise.

**ZH** 如 [12] 所示，流匹配模型中的迭代降噪过程可表述为一个马尔可夫决策过程（MDP）⟦SLOT_6⟧。第 ⟦SLOT_7⟧ 步的状态为 ⟦SLOT_8⟧，动作是模型预测的降噪样本 ⟦SLOT_9⟧，策略为 ⟦SLOT_10⟧。状态转移是确定性的：⟦SLOT_11⟧，初始状态分布为 ⟦SLOT_12⟧，其中 ⟦SLOT_13⟧ 是以 ⟦SLOT_14⟧ 为中心的狄拉克 δ 分布。奖励只在最后一步给出：⟦SLOT_15⟧（若 ⟦SLOT_16⟧），否则为 0。

**EN** 4 Flow-GRPO

**ZH** 4 Flow-GRPO

**EN** In this section, we present Flow-GRPO, which enhances flow models using online RL. We begin by revisiting the core idea of GRPO [16] and adapting it to flow matching. We then show how to convert the deterministic ODE sampler into a SDE sampler with the same marginal distribution, introducing the stochasticity needed for applying GRPO. Finally, we introduce Denoise Reduction, a practical sampling strategy that significantly speeds up training without sacrificing performance.

**ZH** 本节介绍 Flow-GRPO，它用在线 RL 增强流模型。我们先回顾 GRPO [16] 的核心思想并将其适配到流匹配，然后说明如何把确定性 ODE 采样器转换为具有相同边缘分布的 SDE 采样器，从而引入应用 GRPO 所需的随机性，最后介绍降噪步数缩减（Denoise Reduction）——一种在不牺牲性能的前提下大幅加速训练的实用采样策略。

**EN** GRPO on Flow Matching.

**ZH** 流匹配上的 GRPO。

**EN** RL aims to learn a policy that maximizes the expected cumulative reward. This is often formulated as optimizing a policy ⟦SLOT_17⟧ with a regularized objective:

**ZH** RL 旨在学习一个最大化期望累积奖励的策略，这通常表述为优化带正则项的策略 ⟦SLOT_17⟧：

<!-- [原子块 · table] max θ 𝔼 ( 𝒔 0 , 𝒂 0 , … , 𝒔 T , 𝒂 T ) ∼ π θ [ ∑ t = 0 T ( R ( 𝒔 t , 𝒂 t ) − β D KL ( π θ ( ⋅ ∣ 𝒔 t ) | | π ref ( ⋅ ∣ 𝒔 t ) ) ) ] . \max_{\theta}\mathbb{E}_{({\bm{s}}_{0},{\bm{a}}_{0},\dots,{\bm{s}}_{T -->

**EN** Unlike other policy based methods like PPO [20], GRPO [16] provides a lightweight alternative, which introduces a group relative formulation to estimate the advantage.

**ZH** 与 PPO [20] 等其他基于策略的方法不同，GRPO [16] 提供了一种轻量替代方案，它引入组内相对形式来估计优势。

**EN** Recall that the denoising process can be formulated as an MDP, as shown in Section 3. Given a prompt ⟦SLOT_18⟧, the flow model ⟦SLOT_19⟧ samples a group of ⟦SLOT_20⟧ individual images ⟦SLOT_21⟧ and the corresponding reverse-time trajectories ⟦SLOT_22⟧. Then, the advantage of the ⟦SLOT_23⟧-th image is calculated by normalizing the group-level rewards as follows:

**ZH** 回顾第 3 节所述，降噪过程可表述为 MDP。给定提示 ⟦SLOT_18⟧，流模型 ⟦SLOT_19⟧ 采样一组 ⟦SLOT_20⟧ 幅独立的图像 ⟦SLOT_21⟧ 以及相应的逆时轨迹 ⟦SLOT_22⟧。随后，第 ⟦SLOT_23⟧ 幅图像的优势通过如下的组级奖励归一化计算得到：

<!-- [原子块 · table] A ^ t i = R ⁡ ( 𝒙 0 i , 𝒄 ) − mean ​ ( { R ⁡ ( 𝒙 0 i , 𝒄 ) } i = 1 G ) std ​ ( { R ⁡ ( 𝒙 0 i , 𝒄 ) } i = 1 G ) . \hat{A}^{i}_{t}=\frac{R({\bm{x}}^{i}_{0},{\bm{c}})-\text{mean}(\{R({\bm{x}}^{i}_{0},{\b -->

**EN** GRPO optimizes the policy model by maximizing the following objective:

**ZH** GRPO 通过最大化以下目标来优化策略模型：

<!-- [原子块 · table] 𝒥 Flow-GRPO ( θ ) = 𝔼 𝒄 ∼ 𝒞 , { 𝒙 i } i = 1 G ∼ π θ old ( ⋅ ∣ 𝒄 ) f ( r , A ^ , θ , ε , β ) , \mathcal{J}_{\text{Flow-GRPO}}(\theta)=\mathbb{E}_{{\bm{c}}\sim\mathcal{C},\{{\bm{x}}^{i}\}_{i=1}^{G}\sim\ -->

**EN** where

**ZH** 其中

<!-- [原子块 · table] f ⁡ ( r , A ^ , θ , ε , β ) \displaystyle f(r,\hat{A},\theta,\varepsilon,\beta) = 1 G ∑ i = 1 G 1 T ∑ t = 0 T − 1 ( min ( r t i ( θ ) A ^ t i , clip ( r t i ( θ ) , 1 − ε , 1 + ε ) A ^ t i ) − β D KL  -->

**EN** From ODE to SDE.

**ZH** 从 ODE 到 SDE。

**EN** GRPO relies on stochastic sampling in Eq. 4 and Eq. 5 to generate diverse trajectories for advantage estimation and exploration. Diffusion models naturally support this: the forward process adds Gaussian noise step by step, and the reverse process approximates a score-based SDE solver via a Markov chain with decreasing variance. In contrast, flow matching models use a deterministic ODE for the forward process:

**ZH** GRPO 依赖式 4 与式 5 中的随机采样来生成多样化轨迹，用于优势估计与探索。扩散模型天然支持这一点：前向过程逐步加入高斯噪声，反向过程通过方差递减的马尔可夫链近似基于分数的 SDE 求解器。相比之下，流匹配模型的前向过程使用确定性 ODE：

<!-- [原子块 · table] d ​ 𝒙 t = 𝒗 t ​ d ​ t , \mathrm{d}{\bm{x}}_{t}={\bm{v}}_{t}\mathrm{d}t, (6) -->

**EN** where ⟦SLOT_24⟧ is learned via the flow matching objective in Eq. 2. A common sampling method is to discretize this ODE, yielding a one-to-one mapping between successive time steps.

**ZH** 其中 ⟦SLOT_24⟧ 由式 2 中的流匹配目标学得。常见的采样方法是对该 ODE 做离散化，从而在相邻时间步之间得到一一对应的映射。

**EN** This deterministic approach fails to meet the GRPO policy update requirements in two key ways: (1) ⟦SLOT_25⟧ in Eq. 5 requires computing ⟦SLOT_26⟧, which becomes computationally expensive under deterministic dynamics due to divergence estimation. (2) More importantly, RL depends on exploration. As shown in Section 5.3, reduced randomness greatly lowers training efficiency. Deterministic sampling, with no randomness beyond the initial seed, is especially problematic.

**ZH** 这种确定性方法在两个关键方面无法满足 GRPO 策略更新的要求：（1）式 5 中的 ⟦SLOT_25⟧ 需要计算 ⟦SLOT_26⟧，而在确定性动力学下由于散度估计，这一计算开销巨大。（2）更重要的是，RL 依赖探索。如第 5.3 节所示，随机性降低会大幅降低训练效率；除了初始种子外没有任何随机性的确定性采样尤其成问题。

**EN** To address this limitation, we convert the deterministic Flow-ODE from Eq. 6 into an equivalent SDE that matches the original model’s marginal probability density function at all timesteps. We outline the key process here. A detailed proof is provided in Appendix A. Following [23, 28, 29], we construct a reverse-time SDE formulation that preserves the marginal distribution:

**ZH** 为克服这一局限，我们把式 6 中的确定性 Flow-ODE 转换为一个在所有时间步上与原模型边缘概率密度函数相匹配的等价 SDE。这里概述关键过程，详细证明见附录 A。遵循 [23, 28, 29]，我们构造一个保持边缘分布的逆时 SDE 形式：

<!-- [原子块 · table] d 𝒙 t = ( 𝒗 t ( 𝒙 t ) − σ t 2 2 ∇ log p t ( 𝒙 t ) ) d t + σ t d 𝒘 , \mathrm{d}{\bm{x}}_{t}=\left({\bm{v}}_{t}({\bm{x}}_{t})-\frac{\sigma_{t}^{2}}{2}\nabla\log p_{t}({\bm{x}}_{t})\right)\mathrm{d}t+\si -->

**EN** where ⟦SLOT_27⟧ denotes Wiener process increments and ⟦SLOT_28⟧ control the level of stachasticity during generation. For rectified flow, Eq. 7 is specified as:

**ZH** 其中 ⟦SLOT_27⟧ 表示维纳过程增量，⟦SLOT_28⟧ 控制生成过程中的随机性程度。对于 rectified flow，式 7 具体化为：

<!-- [原子块 · table] d ​ 𝒙 t = [ 𝒗 t ​ ( 𝒙 t ) + σ t 2 2 ​ t ​ ( 𝒙 t + ( 1 − t ) ​ 𝒗 t ​ ( 𝒙 t ) ) ] ​ d ​ t + σ t ​ d ​ 𝒘 . \mathrm{d}{\bm{x}}_{t}=\left[{\bm{v}}_{t}({\bm{x}}_{t})+\frac{\sigma_{t}^{2}}{2t}\left({\bm{x}}_ -->

**EN** Applying Euler-Maruyama discretization yields the final update rule:

**ZH** 应用 Euler-Maruyama 离散化得到最终的更新规则：

<!-- [原子块 · table] 𝒙 t + Δ ​ t = 𝒙 t + [ 𝒗 θ ​ ( 𝒙 t , t ) + σ t 2 2 ​ t ​ ( 𝒙 t + ( 1 − t ) ​ 𝒗 θ ​ ( 𝒙 t , t ) ) ] ​ Δ ​ t + σ t ​ Δ ​ t ​ ϵ \displaystyle{\bm{x}}_{t+\Delta t}={\bm{x}}_{t}+\left[{\bm{v}}_{\theta}({\bm -->

**EN** where ⟦SLOT_29⟧ injects stochasticity. We use ⟦SLOT_30⟧ in this paper, where ⟦SLOT_31⟧ is a scalar hyper-parameter that controls the noise level (See Section 5.3 for its impact on performance).

**ZH** 其中 ⟦SLOT_29⟧ 注入随机性。本文使用 ⟦SLOT_30⟧，其中 ⟦SLOT_31⟧ 是控制噪声水平的标量超参数（其对性能的影响见第 5.3 节）。

**EN** Eq. 9 reveals that the policy ⟦SLOT_32⟧ is an isotropic Gaussian distribution. We can easily compute the KL divergence between ⟦SLOT_33⟧ and the reference policy ⟦SLOT_34⟧ in Eq. 5 as a closed form:

**ZH** 式 9 表明策略 ⟦SLOT_32⟧ 是一个各向同性高斯分布。我们可以容易地以闭式计算式 5 中 ⟦SLOT_33⟧ 与参考策略 ⟦SLOT_34⟧ 之间的 KL 散度：

<!-- [原子块 · table] D KL ( π θ | | π ref ) = ‖ 𝒙 ¯ t + Δ ​ t , θ − 𝒙 ¯ t + Δ ​ t , ref ‖ 2 2 ​ σ t 2 ​ Δ ​ t = Δ ​ t 2 ( σ t ​ ( 1 − t ) 2 ​ t + 1 σ t ) 2 ∥ 𝒗 θ ( 𝒙 t , t ) − 𝒗 ref ( 𝒙 t , t ) ∥ 2 D_{\text{KL}}(\pi_{\the -->

**EN** Denoising Reduction.

**ZH** 降噪步数缩减。

**EN** To produce high-quality images, flow models typically require many denoising steps, making data collection costly for online RL. However, we find that large timesteps are unnecessary during online RL training. We can use significantly fewer denoising steps during sample generation, while retaining the original denoising steps during inference to get high-quality samples. Note that we set the timestep ⟦SLOT_35⟧ as ⟦SLOT_36⟧ in training, while the inference timestep ⟦SLOT_37⟧ is set as the original default setting (⟦SLOT_38⟧) for SD3.5-M. Our experiments reveals that this approach enables fast training without sacrificing image quality at test time.

**ZH** 为生成高质量图像，流模型通常需要大量降噪步数，这使得在线 RL 的数据采集成本高昂。然而我们发现，在在线 RL 训练期间并不需要大的时间步数：我们可以在样本生成时使用显著更少的降噪步数，而在推理时保留原始降噪步数以获得高质量样本。需要说明的是，我们在训练时把时间步 ⟦SLOT_35⟧ 设为 ⟦SLOT_36⟧，而推理时间步 ⟦SLOT_37⟧ 对 SD3.5-M 保持原始默认设置（⟦SLOT_38⟧）。实验表明，这一做法能够实现快速训练，同时不牺牲测试时的图像质量。

**EN** 5 Experiments

**ZH** 5 实验

**EN** This section empirically evaluates Flow-GRPO’s ability to improve flow matching models on three tasks. (1) Composition Image Generation: This task requires precise object arrangement and attribute control. We report the results on GenEval. (2) Visual Text Rendering: a rule-based task that evaluates the accurate rendering of the text specified in the prompt. (3) Human Preference Alignment: This task aims to align T2I models with human preferences.

**ZH** 本节实证评估 Flow-GRPO 在三项任务上改进流匹配模型的能力。（1）组合式图像生成：该任务要求精确的物体排布与属性控制，我们在 GenEval 上报告结果。（2）视觉文字渲染：一项基于规则的任务，评估提示中所指定文字的准确渲染。（3）人类偏好对齐：该任务旨在使 T2I 模型与人类偏好对齐。

**EN** 5.1 Experimental Setup

**ZH** 5.1 实验设置

**EN** We introduce three tasks, detailing their respective prompts and reward definitions. For hyperparameter details and compute resource specifications, please refer to Appendix B.3 and Appendix B.4.

**ZH** 我们介绍这三项任务，详述各自的提示与奖励定义。超参数细节与计算资源规格见附录 B.3 与 B.4。

**EN** Compositional Image Generation.

**ZH** 组合式图像生成。

**EN** GenEval [17] assesses T2I models on complex compositional prompts—like object counting, spatial relations, and attribute binding—across six difficult compositional image generation tasks. We use its official evaluation pipeline, which detects object bounding boxes and colors, then infers their spatial relations. Training prompts are generated using official GenEval scripts, which apply templates and random combinations to construct the prompt dataset. The test set is strictly deduplicated: prompts differing only in object order (e.g., "a photo of A and B" vs. "a photo of B and A") are treated as identical, and these variants are removed from the training set. Based on the base model’s initial accuracy across the six tasks, we set the prompt ratio as ⟦SLOT_39⟧. Rewards are rule-based: (1) Counting: ⟦SLOT_40⟧; (2) Position / Color: If the object count is correct, a partial reward is assigned; the remainder is granted when the predicted position or color is also correct.

**ZH** GenEval [17] 在六个困难的组合式图像生成任务上评估 T2I 模型处理复杂组合提示（如物体计数、空间关系与属性绑定）的能力。我们使用其官方评估流程：检测物体边界框与颜色，再推断它们的空间关系。训练提示由 GenEval 官方脚本生成，通过模板与随机组合构建提示数据集。测试集经过严格去重：仅在物体顺序上有差异的提示（例如“a photo of A and B”与“a photo of B and A”）被视为同一条，这些变体已从训练集中移除。根据基础模型在六个任务上的初始准确率，我们把提示比例设为 ⟦SLOT_39⟧。奖励基于规则：（1）计数：⟦SLOT_40⟧；（2）位置／颜色：若物体数量正确，则给予部分奖励；当预测的位置或颜色也正确时，再给予剩余部分。

**EN** Visual Text Rendering [8].

**ZH** 视觉文字渲染 [8]。

**EN** Text is common in images such as posters, book covers, and memes, so the ability to place accurate and coherent text inside the generated images is crucial for T2I models. In our settings, we define an text rendering task, where each prompt follows the template ‘‘A sign that says ‘‘text’’. Specifically, the placeholder ‘‘text’’ is the exact string that should appear in the image. We use GPT4o to produce 20K training prompts and 1K test prompts. Following [58], we measure text fidelity with the reward ⟦SLOT_41⟧ where ⟦SLOT_42⟧ is the minimum edit distance between the rendered text and the target text and ⟦SLOT_43⟧ is the number of characters inside the quotation marks in the prompt. This reward also serves as our metric of text accuracy.

**ZH** 文字在海报、书封、表情包等图像中十分常见，因此在生成图像中放置准确、连贯的文字对 T2I 模型至关重要。在我们的设定中，我们定义一个文字渲染任务，其中每条提示遵循模板“A sign that says ''text''”。具体地，占位符“text”是应当出现在图像中的确切字符串。我们用 GPT4o 生成 2 万条训练提示与 1 千条测试提示。遵循 [58]，我们用奖励 ⟦SLOT_41⟧ 衡量文字保真度，其中 ⟦SLOT_42⟧ 是渲染出的文字与目标文字之间的最小编辑距离，⟦SLOT_43⟧ 是提示中引号内的字符数。该奖励同时用作我们衡量文字准确率的指标。

**EN** Human Preference Alignment [19].

**ZH** 人类偏好对齐 [19]。

**EN** This task aims to align T2I models with human preferences. We use PickScore [19] as our reward model, which is based on large-scale human annotated pairwise comparisons of images generated from the same prompt. For each image and prompt pair, PickScore provides an overall score that evaluates multiple criteria, such as the alignment of the image with the prompt and its visual quality.

**ZH** 该任务旨在使 T2I 模型与人类偏好对齐。我们使用 PickScore [19] 作为奖励模型，它基于对同一提示所生成图像的大规模人工成对比较。对每个图像—提示对，PickScore 给出一个综合分数，评估多项准则，例如图像与提示的对齐程度及其视觉质量。

**EN** Image Quality Evaluation Metric.

**ZH** 图像质量评估指标。

**EN** Since the T2I model is trained to maximize a predefined reward, it is vulnerable to reward hacking, where the reward increases but image quality or diversity declines. This study aims to make online RL effective for T2I generation without noticeably compromising quality or diversity. To detect reward hacking beyond task-specific accuracy, we evaluate four automatic image quality metrics: Aesthetic Score [59], DeQA [60], ImageReward [32], and UnifiedReward [61] (see Appendix B.1 for details). All metrics are computed on DrawBench [1], a comprehensive benchmark with diverse prompts for T2I models.

**ZH** 由于 T2I 模型被训练为最大化预定义奖励，它容易受到奖励黑客的影响，即奖励上升但图像质量或多样性下降。本研究旨在使在线 RL 在 T2I 生成上有效，同时不显著损害质量或多样性。为检测超出任务特定准确率的奖励黑客，我们评估四项自动图像质量指标：Aesthetic Score [59]、DeQA [60]、ImageReward [32] 与 UnifiedReward [61]（详见附录 B.1）。所有指标均在 DrawBench [1] 上计算，这是一个面向 T2I 模型、提示多样的综合基准。

**EN** Table 1: GenEval Result. Best scores are in blue, second-best in green. Results for models other than SD3.5-M are from [7] or their original papers. Obj.: Object; Attr.: Attribution.

**ZH** 表 1：GenEval 结果。最佳分数以蓝色标出，次佳以绿色标出。除 SD3.5-M 外其他模型的结果来自 [7] 或其原始论文。Obj.：物体；Attr.：属性。

<!-- [原子块 · table] Model Overall Single Obj. Two Obj. Counting Colors Position Attr. Binding Diffusion Models LDM [ 62 ] 0.37 0.92 0.29 0.23 0.70 0.02 0.05 SD1.5 [ 62 ] 0.43 0.97 0.38 0.35 0.76 0.04 0.06 SD2.1 [ 62 ] 0. -->

<!-- [原子块 · img]  -->

**EN** Figure 3: Qualitative Comparison on the GenEval Benchmark. Our approach demonstrates superior performance in Counting, Colors, Attribute Binding, and Position.

**ZH** 图 3：GenEval 基准上的定性比较。我们的方法在计数、颜色、属性绑定与位置上展现出优越性能。

**EN** Table 2: Performance on Compositional Image Generation, Visual Text Rendering, and Human Preference benchmarks, evaluated by task performance on test prompts, and by image quality and preference scores on DrawBench prompts. ImgRwd: ImageReward; UniRwd: UnifiedReward.

**ZH** 表 2：组合式图像生成、视觉文字渲染与人类偏好基准上的性能，其中任务性能在测试提示上评估，图像质量与偏好分数在 DrawBench 提示上评估。ImgRwd：ImageReward；UniRwd：UnifiedReward。

<!-- [原子块 · table] Model Task Metric Image Quality Preference Score GenEval OCR Acc. PickScore Aesthetic DeQA ImgRwd PickScore UniRwd SD3.5-M 0.63 0.59 21.72 5.39 4.07 0.87 22.34 3.33 Compositional Image Generation Flow -->

<!-- [原子块 · img]  -->

**EN** Figure 4: Comparison with Other Alignment Methods on the Compositional Generation Task.

**ZH** 图 4：在组合式生成任务上与其他对齐方法的比较。

<!-- [原子块 · object]  -->

**EN** Figure 5: Ablation Studies on Different Group Size ⟦SLOT_44⟧. Higher group size performs better.

**ZH** 图 5：关于不同组大小 ⟦SLOT_44⟧ 的消融研究。更大的组大小表现更好。

**EN** 5.2 Main Results

**ZH** 5.2 主要结果

**EN** Figure 1 and Table 1 show Flow-GRPO’s GenEval performance steadily improving during training, ultimately outperforming GPT-4o. This occurs while maintaining both image quality metrics and preference scores on DrawBench, a benchmark with diverse and comprehensive prompts for evaluating general model capabilities. Figure 3 offers qualitative comparisons. Beyond Compositional Image Generation, Table 2 details evaluations on Visual Text Rendering and Human Preference tasks. Flow-GRPO improved text rendering ability, again without decreasing image quality metrics and preference scores on DrawBench. See Figures 13, 14 & 15 in Appendix C.6 for related qualitative examples. For the Human Preference task, image quality did not decrease without KL regularization. However, we found that omitting KL caused a collapse in visual diversity, a form of reward hacking discussed further in Section 5.3. These results demonstrate that Flow-GRPO boosts desired capabilities while causing very little degradation to image quality or visual diversity.

**ZH** 图 1 与表 1 显示，Flow-GRPO 在 GenEval 上的性能随训练稳步提升，并最终超过 GPT-4o。这一过程中，DrawBench（一个提示多样而全面、用于评估模型通用能力的基准）上的图像质量指标与偏好分数都得以保持。图 3 给出了定性比较。除组合式图像生成外，表 2 详列了在视觉文字渲染与人类偏好任务上的评估：Flow-GRPO 提升了文字渲染能力，同样没有降低 DrawBench 上的图像质量指标与偏好分数。相关定性示例见附录 C.6 中的图 13、14 与 15。在人类偏好任务上，在不使用 KL 正则化时图像质量并未下降；但我们发现，省略 KL 会导致视觉多样性崩溃，这是一种奖励黑客，将在第 5.3 节进一步讨论。这些结果表明，Flow-GRPO 提升了目标能力，同时对图像质量或视觉多样性造成的退化极小。

**EN** Flow-GRPO vs. Other Alignment Methods.

**ZH** Flow-GRPO 与其他对齐方法的比较。

**EN** We compare Flow-GRPO with several alignment methods: supervised fine-tuning (SFT), Flow-DPO [14, 39], and their online variants. Flow-GRPO consistently outperforms all baselines by a significant margin. At each step, we generate a group of images using the same group size as in Flow-GRPO. The only difference lies in the update rule:

**ZH** 我们把 Flow-GRPO 与若干对齐方法比较：监督微调（SFT）、Flow-DPO [14, 39] 及其在线变体。Flow-GRPO 以显著优势一致地优于所有基线。每一步中，我们用与 Flow-GRPO 相同的组大小生成一组图像，唯一差别在于更新规则：

**EN** • SFT: Select the highest-reward image in each group and fine-tune on it.

**ZH** • SFT：在每组中选出奖励最高的图像，并在其上微调。

**EN** • Flow-DPO: Use the highest-reward image in each group as the chosen sample and the lowest as the rejected, then apply the DPO loss.

**ZH** • Flow-DPO：把每组中奖励最高的图像作为被选中样本、最低的作为被拒绝样本，然后施加 DPO 损失。

**EN** Offline variants use a fixed pretrained model for data collection, while online variants update their data collection models every 40 steps. As shown in Figure 5, Flow-GRPO outperforms all baselines. Online DPO also surpasses its offline counterpart, consistent with [15]. For the second-best online DPO, a hyperparameter search on its key parameter ⟦SLOT_45⟧ revealed that smaller values are not always optimal; excessively small ⟦SLOT_46⟧ values can cause training collapse. Appendix C presents more comprehensive comparisons covering additional methods and tasks.

**ZH** 离线变体用固定的预训练模型采集数据，而在线变体每 40 步更新其数据采集模型。如图 5 所示，Flow-GRPO 优于所有基线；在线 DPO 也超过其离线对应方法，与 [15] 一致。对于次优的在线 DPO，对其关键参数 ⟦SLOT_45⟧ 的超参数搜索显示，更小的值并不总是最优；过小的 ⟦SLOT_46⟧ 值会导致训练崩溃。附录 C 给出了涵盖更多方法与任务的更全面比较。

**EN** 5.3 Analysis

**ZH** 5.3 分析

**EN** This section presents several analyses to better understand the behavior and robustness of Flow-GRPO. We examine issues such as reward hacking, the impact of denoising reduction and noise levels, the effect of group size, and the model’s generalization ability. We provide additional analyses in the Appendix C.

**ZH** 本节给出若干分析，以更好地理解 Flow-GRPO 的行为与稳健性。我们考察奖励黑客、降噪步数缩减与噪声水平的影响、组大小的作用，以及模型的泛化能力。更多分析见附录 C。

**EN** Reward Hacking.

**ZH** 奖励黑客。

**EN** We use KL regularization to mitigate reward hacking by tuning the KL coefficient to keep the divergence small and nearly constant during training, keeping the model close to its pretrained weights. This allows task-specific reward optimization without harming overall performance. As shown in Table 2, removing the KL constraint for Compositional Image Generation and Visual Text Rendering significantly reduces image quality and preference scores on DrawBench. In contrast, a properly tuned KL preserves quality while achieving similar gains on task-specific metrics. In the Human Preference Alignment task, removing KL does not affect image quality, likely due to overlap between PickScore and evaluation metrics, but causes a collapse in visual diversity. Outputs converge to a single style, with different seeds producing nearly identical results. KL regularization prevents this collapse and maintains diversity. See Figure 12 in Appendix C.5 for training curves and Figure 6 for more examples.

**ZH** 我们使用 KL 正则化来缓解奖励黑客：通过调节 KL 系数，使训练期间的散度保持很小且近乎恒定，从而让模型贴近其预训练权重。这使得在不损害整体性能的前提下优化任务特定奖励成为可能。如表 2 所示，在组合式图像生成与视觉文字渲染上去掉 KL 约束会显著降低 DrawBench 上的图像质量与偏好分数；相比之下，恰当调节的 KL 在取得相近任务指标增益的同时保持了质量。在人类偏好对齐任务中，去掉 KL 并不影响图像质量，可能是因为 PickScore 与评估指标之间存在重叠，但会导致视觉多样性崩溃：输出收敛到单一风格，不同种子产生几乎相同的结果。KL 正则化阻止了这种崩溃并维持了多样性。训练曲线见附录 C.5 中的图 12，更多示例见图 6。

<!-- [原子块 · img]  -->

**EN** Figure 6: Effect of KL Regularization. The KL penalty effectively suppresses reward hacking, preventing Quality Degradation (for GenEval and OCR) and Diversity Decline (for PickScore).

**ZH** 图 6：KL 正则化的效果。KL 惩罚能有效抑制奖励黑客，防止质量退化（对 GenEval 与 OCR）以及多样性下降（对 PickScore）。

**EN** Effect of Denoising Reduction.

**ZH** 降噪步数缩减的效果。

**EN** Figure 7 (a) highlights Denoising Reduction’s significant impact on accelerating training. To explore how different timesteps affect optimization, these experiments are conducted without the KL constraint. Reducing data collection timesteps from ⟦SLOT_47⟧ to ⟦SLOT_48⟧ achieves over a ⟦SLOT_49⟧ speedup across all three tasks, without impacting final reward. Further reducing to ⟦SLOT_50⟧ does not consistently improve speed and sometimes slows training, so we choose ⟦SLOT_51⟧ timesteps for later experiments. For the other two tasks, learning curves of reward versus training time are presented in Figure 9 in the Appendix C.2.

**ZH** 图 7（a）突出了降噪步数缩减在加速训练上的显著作用。为探究不同时间步如何影响优化，这些实验在不加 KL 约束的条件下进行。把数据采集时间步从 ⟦SLOT_47⟧ 减少到 ⟦SLOT_48⟧，在三项任务上都实现了超过 ⟦SLOT_49⟧ 的加速，且不影响最终奖励。进一步减到 ⟦SLOT_50⟧ 并不能持续提升速度，有时反而使训练变慢，因此我们在后续实验中选择 ⟦SLOT_51⟧ 个时间步。另外两项任务的奖励—训练时间学习曲线见附录 C.2 中的图 9。

**EN** Effect of Noise Level.

**ZH** 噪声水平的影响。

**EN** Higher ⟦SLOT_52⟧ in the SDE boosts image diversity and exploration, vital for RL training. We control this exploration with a noise level ⟦SLOT_53⟧ (Eq. 9). Figure 7 (b) shows the impact of ⟦SLOT_54⟧ on performance. A small ⟦SLOT_55⟧ (e.g., 0.1) limits exploration and slows reward improvement. Increasing ⟦SLOT_56⟧ (up to 0.7) boosts exploration and speeds up reward gains. Beyond this point (e.g., from 0.7 to 1.0), further increases provide no additional benefit, as exploration is already sufficient. We also observe that injecting too much noise by further increasing ⟦SLOT_57⟧ degrades image quality, resulting in zero reward and failed training.

**ZH** SDE 中更高的 ⟦SLOT_52⟧ 能提升图像多样性与探索，这对 RL 训练至关重要。我们用一个噪声水平 ⟦SLOT_53⟧（式 9）来控制这种探索。图 7（b）显示了 ⟦SLOT_54⟧ 对性能的影响：较小的 ⟦SLOT_55⟧（如 0.1）会限制探索、减缓奖励提升；增大 ⟦SLOT_56⟧（直到 0.7）能增强探索并加快奖励增长；超过这一点（例如从 0.7 到 1.0）再增大则没有额外收益，因为探索已足够充分。我们还观察到，继续增大 ⟦SLOT_57⟧ 注入过多噪声会损害图像质量，导致奖励为零与训练失败。

<!-- [原子块 · object]  -->

**EN** (a). Effect of Denoising Reduction on GenEval

**ZH** (a). 降噪步数缩减在 GenEval 上的效果

<!-- [原子块 · object]  -->

**EN** (b). Effect of Noise Level Ablation on the OCR

**ZH** (b). 噪声水平消融在 OCR 上的效果

**EN** Figure 7: Ablation studies on our critical design choices. (a) Denoising Reduction: Fewer denoising steps accelerate convergence and yield similar performance. (b) Noise Level: Moderate noise level (⟦SLOT_58⟧) maximises OCR accuracy, while too little noise hampers exploration.

**ZH** 图 7：关于关键设计选择的消融研究。（a）降噪步数缩减：更少的降噪步数加速收敛并得到相近性能。（b）噪声水平：中等噪声水平（⟦SLOT_58⟧）使 OCR 准确率最大化，而噪声过少会妨碍探索。

**EN** Effect of Group Size.

**ZH** 组大小的影响。

**EN** Figure 5 shows the effect of group size ⟦SLOT_59⟧ using PickScore as the reward function. When the group size was reduced to ⟦SLOT_60⟧ and ⟦SLOT_61⟧, training became unstable and eventually collapsed, whereas ⟦SLOT_62⟧ remained stable throughout the process. We observe that smaller group sizes produce inaccurate advantage estimates, increasing variance and leading to training collapse, a phenomenon also reported in [71, 72].

**ZH** 图 5 显示了以 PickScore 作为奖励函数时组大小 ⟦SLOT_59⟧ 的影响。当组大小减小到 ⟦SLOT_60⟧ 与 ⟦SLOT_61⟧ 时，训练变得不稳定并最终崩溃，而 ⟦SLOT_62⟧ 在整个过程中保持稳定。我们观察到，更小的组大小会产生不准确的优势估计，增大方差并导致训练崩溃，这一现象在 [71, 72] 中也有报道。

**EN** Generalization Analysis.

**ZH** 泛化分析。

**EN** Flow-GRPO demonstrates strong generalization on unseen scenarios from GenEval (Table 4). Specifically, it captures object number, color, and spatial relations, generalizing well to unseen object classes. It also effectively controls object count, generalizing from training on ⟦SLOT_63⟧ objects to generate ⟦SLOT_64⟧ or ⟦SLOT_65⟧ objects. Furthermore, Table 3 shows Flow-GRPO achieves significant gains on T2I-CompBench++ [6, 73]. This comprehensive benchmark for open-world compositional T2I generation features object classes and relationships substantially different from our model’s GenEval-style training data.

**ZH** Flow-GRPO 在 GenEval 中未见过的场景上展现出很强的泛化能力（表 4）。具体地，它捕捉了物体数量、颜色与空间关系，能很好地泛化到未见过的物体类别；它还能有效控制物体数量，从在 ⟦SLOT_63⟧ 个物体上训练泛化到生成 ⟦SLOT_64⟧ 或 ⟦SLOT_65⟧ 个物体。此外，表 3 显示 Flow-GRPO 在 T2I-CompBench++ [6, 73] 上取得显著增益。这个面向开放世界组合式 T2I 生成的综合基准，其物体类别与关系与我们模型的 GenEval 式训练数据存在显著不同。

**EN** Table 3: T2I-CompBench++ Result. This evaluation uses the same model presented in Table 1, which was trained on the GenEval-generated dataset. The best score is in blue.

**ZH** 表 3：T2I-CompBench++ 结果。该评估使用表 1 中给出的同一模型，该模型在 GenEval 生成的数据集上训练。最佳分数以蓝色标出。

<!-- [原子块 · table] Model Color Shape Texture 2D-Spatial 3D-Spatial Numeracy Non-Spatial Janus-Pro-7B [ 69 ] 0.5145 0.3323 0.4069 0.1566 0.2753 0.4406 0.3137 EMU3 [ 67 ] 0.7913 0.5846 0.7422 — — — — FLUX.1 Dev [ 5 ] 0.74 -->

**EN** Table 4: Flow-GRPO demonstrates strong generalization. Unseen Objects: Trained on 60 object classes, evaluated on 20 unseen classes. Unseen Counting: Trained to render 2, 3, or 4 objects, and evaluated in two settings: rendering 5 or 6 objects, and rendering 12 objects.

**ZH** 表 4：Flow-GRPO 展现出很强的泛化能力。未见物体：在 60 个物体类别上训练，在 20 个未见类别上评估。未见计数：训练时渲染 2、3 或 4 个物体，在两种设定下评估：渲染 5 或 6 个物体，以及渲染 12 个物体。

<!-- [原子块 · table] Method Unseen Objects Unseen Counting Overall Single Obj. Two Obj. Counting Colors Position Attr. Binding 5 − - 6 Objects 12 Objects SD3.5-M 0.64 0.96 0.73 0.53 0.87 0.26 0.47 0.13 0.02 SD3.5-M+Flow-G -->

**EN** 6 Conclusion

**ZH** 6 结论

**EN** We have presented Flow-GRPO, the first method to integrate online policy gradient RL into flow matching models. By converting deterministic ODEs to SDEs and reducing denoising steps during training, Flow-GRPO enables efficient RL-based optimization without noticeably compromising image quality or diversity. Our method significantly improves performance on compositional generation, text rendering, and human preference alignment, with minimal reward hacking. Flow-GRPO offers a simple and general framework for applying online RL to flow-based generative models.

**ZH** 本文提出 Flow-GRPO，这是首个把在线策略梯度 RL 引入流匹配模型的方法。通过把确定性 ODE 转换为 SDE，并在训练时减少降噪步数，Flow-GRPO 实现了高效的基于 RL 的优化，同时不显著损害图像质量与多样性。本方法在组合式生成、文字渲染与人类偏好对齐上显著提升了性能，且几乎没有奖励黑客。Flow-GRPO 为把在线 RL 应用于基于流的生成模型提供了一个简洁而通用的框架。

**EN** Limitations & Future Work.

**ZH** 局限性与未来工作。

**EN** Although this work focuses on T2I tasks, Flow-GRPO has potential for video generation [25, 27], raising several future directions: (1) Reward Design: Simple heuristics, such as using object detectors or trackers as rule-based rewards, can encourage physical realism and temporal consistency, but more advanced reward models are needed. (2) Balancing Multiple Rewards: Video generation requires optimizing multiple objectives, including realism, smoothness, and coherence. Balancing these competing goals remains challenging and demands careful tuning. (3) Scalability: Video generation is far more resource-intensive than T2I, so applying Flow-GRPO at scale requires more efficient data collection and training pipelines. Additionally, better methods for preventing reward hacking are worth exploring. While KL regularization helps significantly, it requires longer training and occasional reward hacking occurs for certain prompts.

**ZH** 尽管本工作聚焦于 T2I 任务，Flow-GRPO 在视频生成上也具备潜力 [25, 27]，由此引出若干未来方向：（1）奖励设计：简单的启发式方法，如用目标检测器或跟踪器作为基于规则的奖励，可以鼓励物理真实感与时间一致性，但仍需要更先进的奖励模型。（2）多奖励的平衡：视频生成需要同时优化真实性、平滑性与连贯性等多个目标，如何平衡这些相互竞争的目标仍然具有挑战性，需要细致调参。（3）可扩展性：视频生成的资源消耗远高于 T2I，因此大规模应用 Flow-GRPO 需要更高效的数据采集与训练流程。此外，更好的防止奖励黑客的方法也值得探索：尽管 KL 正则化帮助显著，它需要更长的训练时间，且在某些提示上仍会偶尔出现奖励黑客。

**EN** Acknowledgements

**ZH** 致谢

**EN** This work was partially supported by the JC STEM Lab of AI for Science and Engineering, funded by The Hong Kong Jockey Club Charities Trust, the Research Grants Council of Hong Kong (Project No. CUHK14213224). We gratefully acknowledge Mingwu Zheng for his insightful discussions on the proof and Zhanhui Zhou for his valuable comments that improved the clarity of this paper.

**ZH** 本工作得到由香港赛马会慈善信托基金资助的 JC STEM Lab of AI for Science and Engineering，以及香港研究资助局（项目编号 CUHK14213224）的部分支持。我们诚挚感谢 Mingwu Zheng 在证明方面富有洞见的讨论，以及 Zhanhui Zhou 提出宝贵意见、提升了本文的清晰度。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] [1] Chitwan Saharia, William Chan, Saurabh Saxena, Lala Li, Jay Whang, Emily L Denton, Kamyar Ghasemipour, Raphael Gontijo Lopes, Burcu Karagol Ayan, Tim Salimans, et al. Photorealistic text-to-image  -->

<!-- [原子块 · verbatim] [2] Yaron Lipman, Ricky TQ Chen, Heli Ben-Hamu, Maximilian Nickel, and Matt Le. Flow matching for generative modeling. arXiv preprint arXiv:2210.02747 , 2022. -->

<!-- [原子块 · verbatim] [3] Xingchao Liu, Chengyue Gong, and Qiang Liu. Flow straight and fast: Learning to generate and transfer data with rectified flow. arXiv preprint arXiv:2209.03003 , 2022. -->

<!-- [原子块 · verbatim] [4] Patrick Esser, Sumith Kulal, Andreas Blattmann, Rahim Entezari, Jonas Müller, Harry Saini, Yam Levi, Dominik Lorenz, Axel Sauer, Frederic Boesel, et al. Scaling rectified flow transformers for hig -->

<!-- [原子块 · verbatim] [5] Black Forest Labs. Flux. https://github.com/black-forest-labs/flux , 2024. -->

<!-- [原子块 · verbatim] [6] Kaiyi Huang, Kaiyue Sun, Enze Xie, Zhenguo Li, and Xihui Liu. T2i-compbench: A comprehensive benchmark for open-world compositional text-to-image generation. Advances in Neural Information Process -->

<!-- [原子块 · verbatim] [7] Zhiyuan Yan, Junyan Ye, Weijia Li, Zilong Huang, Shenghai Yuan, Xiangyang He, Kaiqing Lin, Jun He, Conghui He, and Li Yuan. Gpt-imgeval: A comprehensive benchmark for diagnosing gpt4o in image gen -->

<!-- [原子块 · verbatim] [8] Jingye Chen, Yupan Huang, Tengchao Lv, Lei Cui, Qifeng Chen, and Furu Wei. Textdiffuser: Diffusion models as text painters. Advances in Neural Information Processing Systems , 36:9353–9387, 2023. -->

<!-- [原子块 · verbatim] [9] Richard S Sutton, Andrew G Barto, et al. Reinforcement learning: An introduction , volume 1. MIT press Cambridge, 1998. -->

<!-- [原子块 · verbatim] [10] Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al. Deepseek-r1: Incentivizing reasoning capability in llms via reinforce -->

<!-- [原子块 · verbatim] [11] Aaron Jaech, Adam Kalai, Adam Lerer, Adam Richardson, Ahmed El-Kishky, Aiden Low, Alec Helyar, Aleksander Madry, Alex Beutel, Alex Carney, et al. Openai o1 system card. arXiv preprint arXiv:2412. -->

<!-- [原子块 · verbatim] [12] Kevin Black, Michael Janner, Yilun Du, Ilya Kostrikov, and Sergey Levine. Training diffusion models with reinforcement learning. arXiv preprint arXiv:2305.13301 , 2023. -->

<!-- [原子块 · verbatim] [13] Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and Chelsea Finn. Direct preference optimization: Your language model is secretly a reward model. Advances in  -->

<!-- [原子块 · verbatim] [14] Jie Liu, Gongye Liu, Jiajun Liang, Ziyang Yuan, Xiaokun Liu, Mingwu Zheng, Xiele Wu, Qiulin Wang, Wenyu Qin, Menghan Xia, et al. Improving video generation with human feedback. arXiv preprint arX -->

<!-- [原子块 · verbatim] [15] Guibin Chen, Dixuan Lin, Jiangping Yang, Chunze Lin, Juncheng Zhu, Mingyuan Fan, Hao Zhang, Sheng Chen, Zheng Chen, Chengchen Ma, et al. Skyreels-v2: Infinite-length film generative model. arXiv  -->

<!-- [原子块 · verbatim] [16] Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li, Y Wu, et al. Deepseekmath: Pushing the limits of mathematical reasoning in open langua -->

<!-- [原子块 · verbatim] [17] Dhruba Ghosh, Hannaneh Hajishirzi, and Ludwig Schmidt. Geneval: An object-focused framework for evaluating text-to-image alignment. Advances in Neural Information Processing Systems , 36:52132–52 -->

<!-- [原子块 · verbatim] [18] Aaron Hurst, Adam Lerer, Adam P Goucher, Adam Perelman, Aditya Ramesh, Aidan Clark, AJ Ostrow, Akila Welihinda, Alan Hayes, Alec Radford, et al. Gpt-4o system card. arXiv preprint arXiv:2410.2127 -->

<!-- [原子块 · verbatim] [19] Yuval Kirstain, Adam Polyak, Uriel Singer, Shahbuland Matiana, Joe Penna, and Omer Levy. Pick-a-pic: An open dataset of user preferences for text-to-image generation. Advances in Neural Informati -->

<!-- [原子块 · verbatim] [20] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. arXiv preprint arXiv:1707.06347 , 2017. -->

<!-- [原子块 · verbatim] [21] Jonathan Ho, Ajay Jain, and Pieter Abbeel. Denoising diffusion probabilistic models. Advances in neural information processing systems , 33:6840–6851, 2020. -->

<!-- [原子块 · verbatim] [22] Jiaming Song, Chenlin Meng, and Stefano Ermon. Denoising diffusion implicit models. arXiv preprint arXiv:2010.02502 , 2020. -->

<!-- [原子块 · verbatim] [23] Yang Song, Jascha Sohl-Dickstein, Diederik P Kingma, Abhishek Kumar, Stefano Ermon, and Ben Poole. Score-based generative modeling through stochastic differential equations. arXiv preprint arXiv: -->

<!-- [原子块 · verbatim] [24] Kuaishou. Kling ai. https://klingai.kuaishou.com/ , 2024. -->

<!-- [原子块 · verbatim] [25] Ang Wang, Baole Ai, Bin Wen, Chaojie Mao, Chen-Wei Xie, Di Chen, Feiwu Yu, Haiming Zhao, Jianxiao Yang, Jianyuan Zeng, et al. Wan: Open and advanced large-scale video generative models. arXiv pre -->

<!-- [原子块 · verbatim] [26] Tim Brooks, Bill Peebles, Connor Holmes, Will DePue, Yufei Guo, Li Jing, David Schnurr, Joe Taylor, Troy Luhman, Eric Luhman, et al. Video generation models as world simulators. OpenAI Blog , 1:8 -->

<!-- [原子块 · verbatim] [27] Weijie Kong, Qi Tian, Zijian Zhang, Rox Min, Zuozhuo Dai, Jin Zhou, Jiangfeng Xiong, Xin Li, Bo Wu, Jianwei Zhang, et al. Hunyuanvideo: A systematic framework for large video generative models. a -->

<!-- [原子块 · verbatim] [28] Michael S Albergo, Nicholas M Boffi, and Eric Vanden-Eijnden. Stochastic interpolants: A unifying framework for flows and diffusions. arXiv preprint arXiv:2303.08797 , 2023. -->

<!-- [原子块 · verbatim] [29] Carles Domingo-Enrich, Michal Drozdzal, Brian Karrer, and Ricky TQ Chen. Adjoint matching: Fine-tuning flow and diffusion generative models with memoryless stochastic optimal control. arXiv prepr -->

<!-- [原子块 · verbatim] [30] Mihir Prabhudesai, Anirudh Goyal, Deepak Pathak, and Katerina Fragkiadaki. Aligning text-to-image diffusion models with reward backpropagation. arXiv preprint arXiv:2310.03739 , 2023. -->

<!-- [原子块 · verbatim] [31] Kevin Clark, Paul Vicol, Kevin Swersky, and David J Fleet. Directly fine-tuning diffusion models on differentiable rewards. arXiv preprint arXiv:2309.17400 , 2023. -->

<!-- [原子块 · verbatim] [32] Jiazheng Xu, Xiao Liu, Yuchen Wu, Yuxuan Tong, Qinkai Li, Ming Ding, Jie Tang, and Yuxiao Dong. Imagereward: Learning and evaluating human preferences for text-to-image generation. Advances in Ne -->

<!-- [原子块 · verbatim] [33] Mihir Prabhudesai, Russell Mendonca, Zheyang Qin, Katerina Fragkiadaki, and Deepak Pathak. Video diffusion alignment via reward gradients. arXiv preprint arXiv:2407.08737 , 2024. -->

<!-- [原子块 · verbatim] [34] Xue Bin Peng, Aviral Kumar, Grace Zhang, and Sergey Levine. Advantage-weighted regression: Simple and scalable off-policy reinforcement learning. arXiv preprint arXiv:1910.00177 , 2019. -->

<!-- [原子块 · verbatim] [35] Jiajun Fan, Shuaike Shen, Chaoran Cheng, Yuxin Chen, Chumeng Liang, and Ge Liu. Online reward-weighted fine-tuning of flow matching with wasserstein regularization. In The Thirteenth Internationa -->

<!-- [原子块 · verbatim] [36] Kimin Lee, Hao Liu, Moonkyung Ryu, Olivia Watkins, Yuqing Du, Craig Boutilier, Pieter Abbeel, Mohammad Ghavamzadeh, and Shixiang Shane Gu. Aligning text-to-image models using human feedback. arXi -->

<!-- [原子块 · verbatim] [37] Hanze Dong, Wei Xiong, Deepanshu Goyal, Yihan Zhang, Winnie Chow, Rui Pan, Shizhe Diao, Jipeng Zhang, Kashun Shum, and Tong Zhang. Raft: Reward ranked finetuning for generative foundation model a -->

<!-- [原子块 · verbatim] [38] Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and Chelsea Finn. Direct preference optimization: Your language model is secretly a reward model. Advances in  -->

<!-- [原子块 · verbatim] [39] Bram Wallace, Meihua Dang, Rafael Rafailov, Linqi Zhou, Aaron Lou, Senthil Purushwalkam, Stefano Ermon, Caiming Xiong, Shafiq Joty, and Nikhil Naik. Diffusion model alignment using direct prefere -->

<!-- [原子块 · verbatim] [40] Kai Yang, Jian Tao, Jiafei Lyu, Chunjiang Ge, Jiaxin Chen, Weihan Shen, Xiaolong Zhu, and Xiu Li. Using human feedback to fine-tune diffusion models without any reward model. In Proceedings of th -->

<!-- [原子块 · verbatim] [41] Zhanhao Liang, Yuhui Yuan, Shuyang Gu, Bohan Chen, Tiankai Hang, Ji Li, and Liang Zheng. Step-aware preference optimization: Aligning preference with denoising performance at each step. arXiv pre -->

<!-- [原子块 · verbatim] [42] Huizhuo Yuan, Zixiang Chen, Kaixuan Ji, and Quanquan Gu. Self-play fine-tuning of diffusion models for text-to-image generation. arXiv preprint arXiv:2402.10210 , 2024. -->

<!-- [原子块 · verbatim] [43] Runtao Liu, Haoyu Wu, Zheng Ziqiang, Chen Wei, Yingqing He, Renjie Pi, and Qifeng Chen. Videodpo: Omni-preference alignment for video diffusion generation. arXiv preprint arXiv:2412.14167 , 2024. -->

<!-- [原子块 · verbatim] [44] Jiacheng Zhang, Jie Wu, Weifeng Chen, Yatai Ji, Xuefeng Xiao, Weilin Huang, and Kai Han. Onlinevpo: Align video diffusion model with online video-centric preference optimization. arXiv preprint a -->

<!-- [原子块 · verbatim] [45] Hiroki Furuta, Heiga Zen, Dale Schuurmans, Aleksandra Faust, Yutaka Matsuo, Percy Liang, and Sherry Yang. Improving dynamic object interactions in text-to-video generation with ai feedback. arXiv -->

<!-- [原子块 · verbatim] [46] Zhanhao Liang, Yuhui Yuan, Shuyang Gu, Bohan Chen, Tiankai Hang, Mingxi Cheng, Ji Li, and Liang Zheng. Aesthetic post-training diffusion models from generic preferences with step-by-step preferen -->

<!-- [原子块 · verbatim] [47] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. arXiv preprint arXiv:1707.06347 , 2017. -->

<!-- [原子块 · verbatim] [48] Kevin Black, Michael Janner, Yilun Du, Ilya Kostrikov, and Sergey Levine. Training diffusion models with reinforcement learning. arXiv preprint arXiv:2305.13301 , 2023. -->

<!-- [原子块 · verbatim] [49] Ying Fan, Olivia Watkins, Yuqing Du, Hao Liu, Moonkyung Ryu, Craig Boutilier, Pieter Abbeel, Mohammad Ghavamzadeh, Kangwook Lee, and Kimin Lee. Reinforcement learning for fine-tuning text-to-imag -->

<!-- [原子块 · verbatim] [50] Shashank Gupta, Chaitanya Ahuja, Tsung-Yu Lin, Sreya Dutta Roy, Harrie Oosterhuis, Maarten de Rijke, and Satya Narayan Shukla. A simple and effective reinforcement learning method for text-to-ima -->

<!-- [原子块 · verbatim] [51] Zichen Miao, Jiang Wang, Ze Wang, Zhengyuan Yang, Lijuan Wang, Qiang Qiu, and Zicheng Liu. Training diffusion models towards diverse image generation with reinforcement learning. In Proceedings o -->

<!-- [原子块 · verbatim] [52] Hanyang Zhao, Haoxian Chen, Ji Zhang, David D Yao, and Wenpin Tang. Score as action: Fine-tuning diffusion generative models by continuous-time reinforcement learning. arXiv preprint arXiv:2502.0 -->

<!-- [原子块 · verbatim] [53] Po-Hung Yeh, Kuang-Huei Lee, and Jun-Cheng Chen. Training-free diffusion model alignment with sampling demons. arXiv preprint arXiv:2410.05760 , 2024. -->

<!-- [原子块 · verbatim] [54] Zhiwei Tang, Jiangweizhi Peng, Jiasheng Tang, Mingyi Hong, Fan Wang, and Tsung-Hui Chang. Tuning-free alignment of diffusion models with direct noise optimization. arXiv preprint arXiv:2405.18881 -->

<!-- [原子块 · verbatim] [55] Jiaming Song, Qinsheng Zhang, Hongxu Yin, Morteza Mardani, Ming-Yu Liu, Jan Kautz, Yongxin Chen, and Arash Vahdat. Loss-guided diffusion models for plug-and-play controllable generation. In Inter -->

<!-- [原子块 · verbatim] [56] Xiaohui Sun, Ruitong Xiao, Jianye Mo, Bowen Wu, Qun Yu, and Baoxun Wang. F5r-tts: Improving flow matching based text-to-speech with group relative policy optimization. arXiv preprint arXiv:2504.0 -->

<!-- [原子块 · verbatim] [57] Jaihoon Kim, Taehoon Yoon, Jisung Hwang, and Minhyuk Sung. Inference-time scaling for flow models via stochastic generation and rollover budget forcing. arXiv preprint arXiv:2503.19385 , 2025. -->

<!-- [原子块 · verbatim] [58] Lixue Gong, Xiaoxia Hou, Fanshi Li, Liang Li, Xiaochen Lian, Fei Liu, Liyang Liu, Wei Liu, Wei Lu, Yichun Shi, et al. Seedream 2.0: A native chinese-english bilingual image generation foundation  -->

<!-- [原子块 · verbatim] [59] Chrisoph Schuhmann. Laion aesthetics, Aug 2022. -->

<!-- [原子块 · verbatim] [60] Zhiyuan You, Xin Cai, Jinjin Gu, Tianfan Xue, and Chao Dong. Teaching large language models to regress accurate image quality scores using score distribution. arXiv preprint arXiv:2501.11561 , 20 -->

<!-- [原子块 · verbatim] [61] Yibin Wang, Yuhang Zang, Hao Li, Cheng Jin, and Jiaqi Wang. Unified reward model for multimodal understanding and generation. arXiv preprint arXiv:2503.05236 , 2025. -->

<!-- [原子块 · verbatim] [62] Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, and Björn Ommer. High-resolution image synthesis with latent diffusion models. In Proceedings of the IEEE/CVF conference on comput -->

<!-- [原子块 · verbatim] [63] Dustin Podell, Zion English, Kyle Lacey, Andreas Blattmann, Tim Dockhorn, Jonas Müller, Joe Penna, and Robin Rombach. Sdxl: Improving latent diffusion models for high-resolution image synthesis.  -->

<!-- [原子块 · verbatim] [64] Aditya Ramesh, Prafulla Dhariwal, Alex Nichol, Casey Chu, and Mark Chen. Hierarchical text-conditional image generation with clip latents. arXiv preprint arXiv:2204.06125 , 1(2):3, 2022. -->

<!-- [原子块 · verbatim] [65] James Betker, Gabriel Goh, Li Jing, Tim Brooks, Jianfeng Wang, Linjie Li, Long Ouyang, Juntang Zhuang, Joyce Lee, Yufei Guo, et al. Improving image generation with better captions. Computer Scien -->

<!-- [原子块 · verbatim] [66] Jinheng Xie, Weijia Mao, Zechen Bai, David Junhao Zhang, Weihao Wang, Kevin Qinghong Lin, Yuchao Gu, Zhijie Chen, Zhenheng Yang, and Mike Zheng Shou. Show-o: One single transformer to unify multi -->

<!-- [原子块 · verbatim] [67] Xinlong Wang, Xiaosong Zhang, Zhengxiong Luo, Quan Sun, Yufeng Cui, Jinsheng Wang, Fan Zhang, Yueze Wang, Zhen Li, Qiying Yu, et al. Emu3: Next-token prediction is all you need. arXiv preprint ar -->

<!-- [原子块 · verbatim] [68] Yiyang Ma, Xingchao Liu, Xiaokang Chen, Wen Liu, Chengyue Wu, Zhiyu Wu, Zizheng Pan, Zhenda Xie, Haowei Zhang, Liang Zhao, et al. Janusflow: Harmonizing autoregression and rectified flow for unif -->

<!-- [原子块 · verbatim] [69] Xiaokang Chen, Zhiyu Wu, Xingchao Liu, Zizheng Pan, Wen Liu, Zhenda Xie, Xingkai Yu, and Chong Ruan. Janus-pro: Unified multimodal understanding and generation with data and model scaling. arXiv  -->

<!-- [原子块 · verbatim] [70] Enze Xie, Junsong Chen, Yuyang Zhao, Jincheng Yu, Ligeng Zhu, Yujun Lin, Zhekai Zhang, Muyang Li, Junyu Chen, Han Cai, et al. Sana 1.5: Efficient scaling of training-time and inference-time compu -->

<!-- [原子块 · verbatim] [71] Mingjie Liu, Shizhe Diao, Ximing Lu, Jian Hu, Xin Dong, Yejin Choi, Jan Kautz, and Yi Dong. Prorl: Prolonged reinforcement learning expands reasoning boundaries in large language models. arXiv pr -->

<!-- [原子块 · verbatim] [72] Yang Chen, Zhuolin Yang, Zihan Liu, Chankyu Lee, Peng Xu, Mohammad Shoeybi, Bryan Catanzaro, and Wei Ping. Acereason-nemotron: Advancing math and code reasoning through reinforcement learning. ar -->

<!-- [原子块 · verbatim] [73] Kaiyi Huang, Chengqi Duan, Kaiyue Sun, Enze Xie, Zhenguo Li, and Xihui Liu. T2i-compbench++: An enhanced and comprehensive benchmark for compositional text-to-image generation. IEEE Transactions  -->

<!-- [原子块 · verbatim] [74] Bernt Øksendal and Bernt Øksendal. Stochastic differential equations . Springer, 2003. -->

<!-- [原子块 · verbatim] [75] Brian DO Anderson. Reverse-time diffusion equation models. Stochastic Processes and their Applications , 12(3):313–326, 1982. -->

<!-- [原子块 · verbatim] [76] Xue Bin Peng, Aviral Kumar, Grace Zhang, and Sergey Levine. Advantage-weighted regression: Simple and scalable off-policy reinforcement learning. arXiv preprint arXiv:1910.00177 , 2019. -->

**EN** Our Appendix consists of 4 sections. Readers can click on each section number to navigate to the corresponding section:

**ZH** 我们的附录由 4 节组成，读者可点击各节编号跳转至相应章节：

**EN** • Section A provides detailed derivations of stochastic sampling in flow matching models.

**ZH** • A 节给出流匹配模型中随机采样的详细推导。

**EN** • Section B presents details about our experimental setup.

**ZH** • B 节介绍实验设置的细节。

**EN** • Section C offers some additional experimental results, including 1) the comparison with other alignment methods, 2) ablation of denoising reduction on OCR accuracy and pickscore, 3) ablation of initial noise, 4) additional results on FLUX.1-Dev, 5) the learning curves of Flow-GRPO on three tasks, 6) additional qualitative results, and 7) evolution of evaluation images during training.

**ZH** • C 节提供一些额外的实验结果，包括：1）与其他对齐方法的比较；2）降噪步数缩减在 OCR 准确率与 PickScore 上的消融；3）初始噪声的消融；4）FLUX.1-Dev 上的额外结果；5）Flow-GRPO 在三项任务上的学习曲线；6）额外的定性结果；7）训练过程中评估图像的演化。

**EN** • Section D provides a visualization of training samples under the denoising reduction strategy.

**ZH** • D 节给出降噪步数缩减策略下训练样本的可视化。

**EN** In addition to this Appendix, we also provide more visualization results, see this website. We encourage the readers to consult this HTML page for a more intuitive assessment of the improvements brought by Flow-GRPO.

**ZH** 除本附录外，我们还提供了更多可视化结果，见该网站。我们建议读者查阅该 HTML 页面，以更直观地评估 Flow-GRPO 带来的改进。

**EN** Appendix A Mathematical Derivations for Stochastic Sampling using Flow Models

**ZH** 附录 A 基于流模型的随机采样的数学推导

**EN** We present a detailed proof here. To compute ⟦SLOT_66⟧ in Equation 5 during forward sampling, we adapt flow models to a stochastic differential equation (SDE). While flow models normally follow a deterministic ODE:

**ZH** 这里我们给出详细证明。为在前向采样时计算式 5 中的 ⟦SLOT_66⟧，我们把流模型适配为一个随机微分方程（SDE）。流模型通常遵循一个确定性 ODE：

<!-- [原子块 · table] d ​ 𝒙 t = 𝒗 t ​ d ​ t \mathrm{d}{\bm{x}}_{t}={\bm{v}}_{t}\mathrm{d}t (10) -->

**EN** We consider its stochastic counterpart. Inspired by the derivation from SDE to its probability flow ODE in SGMs [23], we aim to construct a forward SDE with specific drift and diffusion coefficients so that its marginal distribution matches that of Eq. 10. We begin with the generic form of SDE:

**ZH** 我们考虑其随机对应形式。受 SGM [23] 中从 SDE 推导其概率流 ODE 的启发，我们旨在构造一个具有特定漂移与扩散系数的前向 SDE，使其边缘分布与式 10 相匹配。我们从 SDE 的一般形式出发：

<!-- [原子块 · table] d ​ 𝒙 t = f SDE ​ ( 𝒙 t , t ) ​ d ​ t + σ t ​ d ​ 𝒘 , \mathrm{d}{\bm{x}}_{t}=f_{\text{SDE}}({\bm{x}}_{t},t)\mathrm{d}t+\sigma_{t}\mathrm{d}{\bm{w}}, (11) -->

**EN** Its marginal probability density ⟦SLOT_67⟧ evolves according to the Fokker–Planck equation [74], i.e.,

**ZH** 其边缘概率密度 ⟦SLOT_67⟧ 依据 Fokker–Planck 方程 [74] 演化，即

<!-- [原子块 · table] ∂ t p t ( x ) = − ∇ ⋅ [ f SDE ( 𝒙 t , t ) p t ( 𝒙 ) ] + 1 2 ∇ 2 [ σ t 2 p t ( 𝒙 ) ] \partial_{t}p_{t}(x)=-\nabla\cdot[f_{\text{SDE}}({\bm{x}}_{t},t)p_{t}({\bm{x}})]+\frac{1}{2}\nabla^{2}[\sigma_{t}^{2 -->

**EN** Similarly, the marginal probability density associated with Eq. 10 evolves:

**ZH** 类似地，式 10 对应的边缘概率密度演化如下：

<!-- [原子块 · table] ∂ t p t ​ ( 𝒙 ) \displaystyle\partial_{t}p_{t}({\bm{x}}) = − ∇ ⋅ [ 𝒗 t ( 𝒙 t , t ) p t ( 𝒙 ) ] \displaystyle=-\nabla\cdot[{\bm{v}}_{t}({\bm{x}}_{t},t)p_{t}({\bm{x}})] (13) -->

**EN** To ensure that the stochastic process shares the same marginal distribution as the ODE, we impose:

**ZH** 为使该随机过程与 ODE 具有相同的边缘分布，我们施加如下条件：

<!-- [原子块 · table] − ∇ ⋅ [ f SDE p t ( 𝒙 ) ] + 1 2 ∇ 2 [ σ t 2 p t ( 𝒙 ) ] = − ∇ ⋅ [ 𝒗 t ( 𝒙 t , t ) p t ( 𝒙 ) ] -\nabla\cdot[f_{\text{SDE}}\,p_{t}({\bm{x}})]+\frac{1}{2}\nabla^{2}[\sigma_{t}^{2}p_{t}({\bm{x}})]=-\nabla -->

**EN** Observing that

**ZH** 注意到

<!-- [原子块 · table] ∇ 2 [ σ t 2 ​ p t ​ ( 𝒙 ) ] \displaystyle\nabla^{2}[\sigma_{t}^{2}p_{t}({\bm{x}})] = σ t 2 ​ ∇ 2 p t ​ ( 𝒙 ) \displaystyle=\sigma_{t}^{2}\nabla^{2}p_{t}({\bm{x}}) (15) = σ t 2 ∇ ⋅ ( ∇ p t ( 𝒙 ) ) \dis -->

**EN** Substituting Eq. 15 to Eq. 14, we arrive at the drift coefficients of the target forward SDE:

**ZH** 把式 15 代入式 14，我们得到目标前向 SDE 的漂移系数：

<!-- [原子块 · table] f SDE = 𝒗 t ( 𝒙 t , t ) + σ t 2 2 ∇ log p t ( 𝒙 ) \displaystyle f_{\text{SDE}}={\bm{v}}_{t}({\bm{x}}_{t},t)+\frac{\sigma_{t}^{2}}{2}\nabla\log p_{t}({\bm{x}}) (16) -->

**EN** Hence, we can rewrite the forward SDE in Eq. 11 as:

**ZH** 因此，我们可以把式 11 中的前向 SDE 重写为：

<!-- [原子块 · table] d 𝒙 t = ( 𝒗 t ( 𝒙 t ) + σ t 2 2 ∇ log p t ( 𝒙 t ) ) d t + σ t d 𝒘 , \displaystyle\mathrm{d}{\bm{x}}_{t}=\left({\bm{v}}_{t}({\bm{x}}_{t})+\frac{\sigma_{t}^{2}}{2}\nabla\log p_{t}({\bm{x}}_{t})\right)\m -->

**EN** where ⟦SLOT_68⟧ denotes Wiener process increments, and ⟦SLOT_69⟧ is the diffusion coefficient controlling the level of stochasticity during sampling.

**ZH** 其中 ⟦SLOT_68⟧ 表示维纳过程增量，⟦SLOT_69⟧ 是控制采样过程中随机性程度的扩散系数。

**EN** The relationship between forward and reverse-time SDEs has been established in [75, 23]. Specifically, if the forward SDE takes the form

**ZH** 前向与逆时 SDE 之间的关系已在 [75, 23] 中建立。具体地，若前向 SDE 形如

<!-- [原子块 · table] d ​ 𝒙 t = f ⁡ ( 𝒙 t , t ) ​ d ​ t + g ⁡ ( t ) ​ d ​ 𝒘 , \displaystyle\mathrm{d}{\bm{x}}_{t}=f({\bm{x}}_{t},t)\,\mathrm{d}t+g(t)\,\mathrm{d}{\bm{w}}, (18) -->

**EN** then the corresponding reverse-time SDE is

**ZH** 则相应的逆时 SDE 为

<!-- [原子块 · table] d 𝒙 t = [ f ( 𝒙 t , t ) − g 2 ( t ) ∇ log p t ( 𝒙 t ) ] d t + g ( t ) d 𝒘 ¯ . \displaystyle\mathrm{d}{\bm{x}}_{t}=\left[f({\bm{x}}_{t},t)-g^{2}(t)\nabla\log p_{t}({\bm{x}}_{t})\right]\,\mathrm{d}t+g(t -->

**EN** Setting ⟦SLOT_70⟧, we obtain the reverse-time SDE corresponding to Eq. 17 as

**ZH** 令 ⟦SLOT_70⟧，我们得到式 17 对应的逆时 SDE 为

<!-- [原子块 · table] d ​ 𝒙 t \displaystyle\mathrm{d}{\bm{x}}_{t} = [ 𝒗 t ( 𝒙 t ) + σ t 2 2 ∇ log p t ( 𝒙 t ) − σ t 2 ∇ log p t ( 𝒙 t ) ] d t + σ t d 𝒘 ¯ . \displaystyle=\left[{\bm{v}}_{t}({\bm{x}}_{t})+\frac{\sigma_{t}^{2 -->

**EN** We thus arrive at the final form of the reverse-time SDE:

**ZH** 由此我们得到逆时 SDE 的最终形式：

<!-- [原子块 · table] d 𝒙 t = ( 𝒗 t ( 𝒙 t ) − σ t 2 2 ∇ log p t ( 𝒙 t ) ) d t + σ t d 𝒘 , \displaystyle\mathrm{d}{\bm{x}}_{t}=\left({\bm{v}}_{t}({\bm{x}}_{t})-\frac{\sigma_{t}^{2}}{2}\nabla\log p_{t}({\bm{x}}_{t})\right)\m -->

**EN** Once the score function ⟦SLOT_71⟧ is available, the process can be simulated directly. For flow matching, this score is implicitly linked to the velocity field ⟦SLOT_72⟧.

**ZH** 一旦得到分数函数 ⟦SLOT_71⟧，该过程即可直接模拟。对流匹配而言，这个分数与速度场 ⟦SLOT_72⟧ 有着隐式联系。

**EN** Specifically, let ⟦SLOT_73⟧. All expectations are over ⟦SLOT_74⟧ and ⟦SLOT_75⟧, where ⟦SLOT_76⟧ is the data distribution.

**ZH** 具体地，令 ⟦SLOT_73⟧。所有期望均对 ⟦SLOT_74⟧ 与 ⟦SLOT_75⟧ 取，其中 ⟦SLOT_76⟧ 是数据分布。

**EN** For the linear interpolation ⟦SLOT_77⟧, we have:

**ZH** 对于线性插值 ⟦SLOT_77⟧，我们有：

<!-- [原子块 · table] p t | 0 ​ ( 𝒙 t | 𝒙 0 ) = 𝒩 ⁡ ( 𝒙 t ∣ α t ​ 𝒙 0 , β t 2 ​ 𝑰 ) , p_{t|0}({\bm{x}}_{t}|{\bm{x}}_{0})=\mathcal{N}\left({\bm{x}}_{t}\mid\alpha_{t}{\bm{x}}_{0},\beta_{t}^{2}{\bm{I}}\right), (22) -->

**EN** yielding the conditional score:

**ZH** 由此得到条件分数：

<!-- [原子块 · table] ∇ log ⁡ p t | 0 ​ ( 𝒙 t | 𝒙 0 ) = − 𝒙 t − α t ​ 𝒙 0 β t 2 = − 𝒙 1 β t . \nabla\log p_{t|0}({\bm{x}}_{t}|{\bm{x}}_{0})=-\frac{{\bm{x}}_{t}-\alpha_{t}{\bm{x}}_{0}}{\beta_{t}^{2}}=-\frac{{\bm{x}}_{1}}{\b -->

**EN** The marginal score becomes:

**ZH** 边缘分数变为：

<!-- [原子块 · table] ∇ log ⁡ p t ​ ( 𝒙 t ) \displaystyle\nabla\log p_{t}({\bm{x}}_{t}) = 𝔼 ⁡ [ ∇ log ⁡ p t | 0 ​ ( 𝒙 t | 𝒙 0 ) ∣ 𝒙 t ] \displaystyle=\mathbb{E}\left[\nabla\log p_{t|0}({\bm{x}}_{t}|{\bm{x}}_{0})\mid{\bm{x} -->

**EN** For the velocity field ⟦SLOT_78⟧, we derive:

**ZH** 对于速度场 ⟦SLOT_78⟧，我们推导：

<!-- [原子块 · table] 𝒗 t ​ ( 𝒙 ) = 𝔼 ⁡ [ α t ˙ ​ 𝒙 0 + β t ˙ ​ 𝒙 1 ∣ 𝒙 t = 𝒙 ] = α t ˙ ​ 𝔼 ​ [ 𝒙 0 ∣ 𝒙 t = 𝒙 ] + β t ˙ ​ 𝔼 ​ [ 𝒙 1 ∣ 𝒙 t = 𝒙 ] = α t ˙ ​ 𝔼 ​ [ 𝒙 t − β t ​ 𝒙 1 α t ∣ 𝒙 t = 𝒙 ] + β t ˙ ​ 𝔼 ​ [ 𝒙 1 ∣ 𝒙 t = 𝒙  -->

**EN** Substituting ⟦SLOT_79⟧ and ⟦SLOT_80⟧ simplifies Equation 25 to:

**ZH** 把 ⟦SLOT_79⟧ 与 ⟦SLOT_80⟧ 代入，式 25 化简为：

<!-- [原子块 · table] 𝒗 t ( 𝒙 ) = − 𝒙 1 − t − t 1 − t ∇ log p t ( 𝒙 ) . {\bm{v}}_{t}({\bm{x}})=-\frac{{\bm{x}}}{1-t}-\frac{t}{1-t}\nabla\log p_{t}({\bm{x}}). (26) -->

**EN** Solving for the score yields:

**ZH** 解出分数得到：

<!-- [原子块 · table] ∇ log ⁡ p t ​ ( 𝒙 ) = − 𝒙 t − 1 − t t ​ 𝒗 t ​ ( 𝒙 ) . \nabla\log p_{t}({\bm{x}})=-\frac{{\bm{x}}}{t}-\frac{1-t}{t}{\bm{v}}_{t}({\bm{x}}). (27) -->

**EN** Substituting Equation 27 into 21 gives the final SDE:

**ZH** 把式 27 代入式 21 得到最终的 SDE：

<!-- [原子块 · table] d ​ 𝒙 t = [ 𝒗 t ​ ( 𝒙 t ) + σ t 2 2 ​ t ​ ( 𝒙 t + ( 1 − t ) ​ 𝒗 t ​ ( 𝒙 t ) ) ] ​ d ​ t + σ t ​ d ​ 𝒘 . \mathrm{d}{\bm{x}}_{t}=\left[{\bm{v}}_{t}({\bm{x}}_{t})+\frac{\sigma_{t}^{2}}{2t}\left({\bm{x}}_ -->

**EN** Applying Euler-Maruyama discretization yields the update rule:

**ZH** 应用 Euler-Maruyama 离散化得到更新规则：

<!-- [原子块 · table] 𝒙 t + Δ ​ t = 𝒙 t + [ 𝒗 θ ​ ( 𝒙 t , t ) + σ t 2 2 ​ t ​ ( 𝒙 t + ( 1 − t ) ​ 𝒗 θ ​ ( 𝒙 t , t ) ) ] ​ Δ ​ t + σ t ​ Δ ​ t ​ ϵ , \displaystyle{\bm{x}}_{t+\Delta t}={\bm{x}}_{t}+\left[{\bm{v}}_{\theta}({\ -->

**EN** where ⟦SLOT_81⟧ injects stochasticity.

**ZH** 其中 ⟦SLOT_81⟧ 注入随机性。

**EN** Appendix B Further Details on the Experimental Setup

**ZH** 附录 B 实验设置的更多细节

**EN** B.1 Quality Metrics

**ZH** B.1 质量指标

**EN** The details of quality metrics are as follows:

**ZH** 质量指标的细节如下：

**EN** • Aesthetic score [59]: a CLIP-based linear regressor that predicts an image’s aesthetic score.

**ZH** • Aesthetic score [59]：一个基于 CLIP 的线性回归器，用于预测图像的美学分数。

**EN** • DeQA score [60]: a multimodal large language model based image-quality assessment (IQA) model that quantifies how distortions, texture damage, and other low-level artefacts affect perceived quality.

**ZH** • DeQA score [60]：一个基于多模态大语言模型的图像质量评估（IQA）模型，量化失真、纹理损伤与其他底层伪影对感知质量的影响。

**EN** • ImageReward [32]: a general purpose T2I human preference reward model that captures text–image alignment, visual fidelity, and harmlessness.

**ZH** • ImageReward [32]：一个通用的 T2I 人类偏好奖励模型，刻画图文对齐、视觉保真度与无害性。

**EN** • UnifiedReward [61]: a recently proposed unified reward model for multimodal understanding and generation that currently achieves state-of-the-art performance on the human preference assessment leaderboard.

**ZH** • UnifiedReward [61]：近期提出的一个面向多模态理解与生成的统一奖励模型，目前在人类偏好评估排行榜上取得最佳性能。

**EN** B.2 Model Specification

**ZH** B.2 模型规格

**EN** The following table lists the base model and the reward models and their corresponding links.

**ZH** 下表列出基础模型与各奖励模型及其对应链接。

<!-- [原子块 · table] Models Links SD3.5-M [ 4 ] https://huggingface.co/stabilityai/stable-diffusion-3.5-medium Aesthetic Score [ 59 ] https://github.com/LAION-AI/aesthetic-predictor PickScore [ 19 ] https://huggingface.co -->

**EN** B.3 Hyperparameters Specification

**ZH** B.3 超参数规格

**EN** Except for ⟦SLOT_82⟧, GRPO hyperparameters are fixed across tasks. We use a sampling timestep ⟦SLOT_83⟧ and an evaluation timestep ⟦SLOT_84⟧. Other settings include a group size ⟦SLOT_85⟧, an noise level ⟦SLOT_86⟧ and an image resolution of 512. The KL ratio ⟦SLOT_87⟧ is set to 0.04 for GenEval and Text Rendering, and 0.01 for Pickscore. We use Lora with ⟦SLOT_88⟧ and ⟦SLOT_89⟧.

**ZH** 除 ⟦SLOT_82⟧ 外，GRPO 超参数在各任务上保持一致。我们使用采样时间步 ⟦SLOT_83⟧ 与评估时间步 ⟦SLOT_84⟧。其他设置包括组大小 ⟦SLOT_85⟧、噪声水平 ⟦SLOT_86⟧ 与 512 的图像分辨率。KL 比率 ⟦SLOT_87⟧ 对 GenEval 与文字渲染设为 0.04，对 Pickscore 设为 0.01。我们使用 LoRA，取 ⟦SLOT_88⟧ 与 ⟦SLOT_89⟧。

**EN** B.4 Compute Resources Specification

**ZH** B.4 计算资源规格

**EN** We train our model using 24 NVIDIA A800 GPUs. The learning curves in Appendix C.5 provide details on the specific GPU hours.

**ZH** 我们使用 24 块 NVIDIA A800 GPU 训练模型。附录 C.5 中的学习曲线给出了具体 GPU 小时数的细节。

**EN** Appendix C Extended Experimental Results

**ZH** 附录 C 扩展实验结果

**EN** C.1 Flow-GRPO vs. Other Alignment Methods

**ZH** C.1 Flow-GRPO 与其他对齐方法的比较

**EN** We compare Flow-GRPO with several alignment methods: supervised fine-tuning (SFT), reward-weighted regression (Flow-RWR [14, 76]), Flow-DPO [14], and their online variants. Flow-GRPO consistently outperforms all baselines by a significant margin. At each step, we generate a group of images using the same group size as in Flow-GRPO. The only difference lies in the update rule:

**ZH** 我们把 Flow-GRPO 与若干对齐方法比较：监督微调（SFT）、奖励加权回归（Flow-RWR [14, 76]）、Flow-DPO [14] 及其在线变体。Flow-GRPO 以显著优势一致地优于所有基线。每一步中，我们用与 Flow-GRPO 相同的组大小生成一组图像，唯一差别在于更新规则：

**EN** • SFT: Select the highest-reward image in each group and fine-tune on it.

**ZH** • SFT：在每组中选出奖励最高的图像，并在其上微调。

**EN** • Flow-RWR [14, 76]: Apply a softmax over rewards in each group and perform reward-weighted likelihood maximization.

**ZH** • Flow-RWR [14, 76]：在每组内对奖励做 softmax，并执行奖励加权的似然最大化。

**EN** • Flow-DPO [14, 39]: Use the highest-reward image in each group as the chosen sample and the lowest as the rejected, then apply the DPO loss.

**ZH** • Flow-DPO [14, 39]：把每组中奖励最高的图像作为被选中样本、最低的作为被拒绝样本，然后施加 DPO 损失。

**EN** Offline variants use a fixed pretrained model for data collection, while online variants update their data collection model every 40 steps. As shown in Figure 8, Flow-GRPO outperforms all other methods. The figure also indicates that DPO and SFT improve over time. In contrast, RWR does not, which aligns with experimental findings on RWR in [12]. Additionally, Online DPO surpasses offline DPO, aligning with [15]’s finding that online DPO performs better. For the second-best online DPO, a hyperparameter search on its key parameter ⟦SLOT_90⟧ revealed that smaller values are not always optimal; excessively small ⟦SLOT_91⟧ values can cause training collapse.

**ZH** 离线变体用固定的预训练模型采集数据，而在线变体每 40 步更新其数据采集模型。如图 8 所示，Flow-GRPO 优于所有其他方法。图中还显示，DPO 与 SFT 随时间有所改进，而 RWR 则不然，这与 [12] 中关于 RWR 的实验发现一致。此外，在线 DPO 超过离线 DPO，与 [15] 关于在线 DPO 表现更优的发现相符。对于次优的在线 DPO，对其关键参数 ⟦SLOT_90⟧ 的超参数搜索显示，更小的值并不总是最优；过小的 ⟦SLOT_91⟧ 值会导致训练崩溃。

<!-- [原子块 · img]  -->

<!-- [原子块 · object]  -->

**EN** Figure 8: Comparison of Flow-GRPO and Other Alignment Methods on the Human Preference Alignment task. Since methods like DPO use different tuned batch sizes from Flow-GRPO, we use the number of training prompts on the x-axis for a fair comparison across these methods.

**ZH** 图 8：Flow-GRPO 与其他对齐方法在人类偏好对齐任务上的比较。由于 DPO 等方法使用的批大小与 Flow-GRPO 不同（各自经过调优），我们在 x 轴上使用训练提示的数量，以便在这些方法间做公平比较。

**EN** DDPO.

**ZH** DDPO。

**EN** DDPO [12] was originally developed for diffusion-based backbones, so we adapted it to flow-matching models via our ODE-to-SDE conversion. Using SD3.5-M as the base model and PickScore as the reward signal, we track the evaluation reward throughout the entire training process in Figure 8. We find that DDPO’s reward increases more slowly than Flow-GRPO’s and eventually collapses in the later stages, whereas Flow-GRPO trains stably and continues to improve consistently over time.

**ZH** DDPO [12] 最初面向基于扩散的骨干网络开发，因此我们通过 ODE-to-SDE 转换把它适配到流匹配模型。以 SD3.5-M 为基础模型、PickScore 为奖励信号，我们在图 8 中跟踪整个训练过程中的评估奖励。我们发现，DDPO 的奖励增长比 Flow-GRPO 更慢，并在后期最终崩溃；而 Flow-GRPO 训练稳定，并随时间持续改进。

**EN** ReFL.

**ZH** ReFL。

**EN** ReFL [32] directly fine-tunes diffusion models by viewing reward model scores as human preference losses and back-propagating gradients to a randomly-picked late timestep ⟦SLOT_92⟧. Following ImageReward [32], we back-propagate gradients to a randomly chosen late timestep ⟦SLOT_93⟧ during denoising. Figure 8 shows that GRPO surpasses ReFL when the reward is differentiable, indicating that GRPO maintains strong performance in settings where ReFL applies. More importantly, GRPO does not require differentiable rewards, enabling direct use of state-of-the-art Vision-Language Models (VLMs) as reward providers. This offers two key advantages:

**ZH** ReFL [32] 把奖励模型分数视为人类偏好损失，并把梯度反向传播到一个随机选取的晚期时间步 ⟦SLOT_92⟧，从而直接微调扩散模型。遵循 ImageReward [32]，我们在降噪过程中把梯度反向传播到一个随机选取的晚期时间步 ⟦SLOT_93⟧。图 8 显示，在奖励可微时 GRPO 优于 ReFL，表明在 ReFL 适用的设定下 GRPO 仍保持强劲性能。更重要的是，GRPO 不要求奖励可微，从而可以直接使用当前最佳的视觉语言模型（VLM）作为奖励提供方。这带来两项关键优势：

**EN** • Sophisticated, General-Purpose Rewards: VLMs can conduct human-like evaluations through a structured reasoning process. Given a prompt, a VLM can decompose it into key criteria, reason step by step to verify each aspect in the generated image, and then provide a comprehensive overall score. This enables a single, unified reward model to handle diverse tasks, from text-to-image generation to complex instruction-based image editing.

**ZH** • 复杂而通用的奖励：VLM 可以通过结构化推理过程进行类人评估。给定一条提示，VLM 能把它分解为若干关键准则，逐步推理以核验生成图像中的各个方面，然后给出综合的总体分数。这使得单一的统一奖励模型能够处理从文生图到复杂的基于指令的图像编辑等多样任务。

**EN** • Future-Proof and Cost-Free Upgrades: The field of VLMs is advancing at a breathtaking pace. By using a VLM as the reward source, our framework automatically benefits from these improvements. As VLMs become more capable, the reward model becomes stronger without any additional training data or computational cost.

**ZH** • 面向未来且零成本的升级：VLM 领域正以惊人的速度前进。把 VLM 用作奖励来源，我们的框架会自动从这些进步中获益。随着 VLM 能力增强，奖励模型也随之变强，而无需任何额外的训练数据或计算成本。

**EN** ORW.

**ZH** ORW。

**EN** ORW [35] is an online reward-weighted regression method that guides the model to prioritize high-reward regions. Unlike KL regularization, it employs Wasserstein-2 regularization to prevent policy collapse and maintain diversity. To ensure a fair comparison, we adopt the same experimental setup as in our Human Preference Alignment task. For ORW, we set ⟦SLOT_94⟧ and ⟦SLOT_95⟧ (lower values led to unstable training). The steps_per_epoch parameter, which controls how frequently the data-collecting policy is updated, was chosen from ⟦SLOT_96⟧ based on best performance. Table 5 reports reward scores on the test set across training steps. Following ORW’s Table 1, we randomly sampled 50 DrawBench prompts and generated 64 images per prompt to compute CLIP and Diversity scores. As shown in Table 6, Flow-GRPO outperforms ORW on both metrics.

**ZH** ORW [35] 是一种在线奖励加权回归方法，引导模型优先关注高奖励区域。与 KL 正则化不同，它采用 Wasserstein-2 正则化来防止策略崩溃并维持多样性。为保证公平比较，我们采用与人类偏好对齐任务相同的实验设置。对 ORW，我们设 ⟦SLOT_94⟧ 与 ⟦SLOT_95⟧（更低的取值会导致训练不稳定）。控制数据采集策略更新频率的 steps_per_epoch 参数依据最佳性能从 ⟦SLOT_96⟧ 中选取。表 5 报告了各训练步上测试集的奖励分数。遵循 ORW 的表 1，我们随机采样 50 条 DrawBench 提示，每条提示生成 64 幅图像，以计算 CLIP 分数与多样性分数。如表 6 所示，Flow-GRPO 在两项指标上都优于 ORW。

**EN** Table 5: Reward scores on the test set over training steps.

**ZH** 表 5：各训练步上测试集的奖励分数。

<!-- [原子块 · table] Method Step 0 Step 240 Step 480 Step 720 Step 960 SD3.5-M + ORW 28.79 29.05 29.15 27.58 23.05 SD3.5-M + Flow-GRPO 28.79 29.10 29.17 29.51 29.89 -->

**EN** Table 6: Comparison of CLIP and diversity scores across different fine-tuning methods.

**ZH** 表 6：不同微调方法下 CLIP 分数与多样性分数的比较。

<!-- [原子块 · table] Method CLIP Score ↑ \uparrow Diversity Score ↑ \uparrow SD3.5-M 27.99 0.96 SD3.5-M + ORW 28.40 0.97 SD3.5-M + Flow-GRPO 30.18 1.02 -->

**EN** C.2 Effect of Denoising Reduction

**ZH** C.2 降噪步数缩减的效果

**EN** We show the extended Denoising Reduction ablations of Visual Text Rendering and Human Preference Alignment tasks in Figure 9.

**ZH** 我们在图 9 中给出视觉文字渲染与人类偏好对齐任务上扩展的降噪步数缩减消融。

<!-- [原子块 · object]  -->

**EN** (a) Visual Text Rendering

**ZH** (a) 视觉文字渲染

<!-- [原子块 · object]  -->

**EN** (b) Human Preference Alignment

**ZH** (b) 人类偏好对齐

**EN** Figure 9: Effect of Denoising Reduction

**ZH** 图 9：降噪步数缩减的效果

**EN** C.3 Effect of Initial Noise

**ZH** C.3 初始噪声的影响

**EN** We initialize each rollout with difference random noise to increase exploratory diversity during RL training. We perform an additioanl ablation to confirm this claim. With SD3.5-M as the base model and PickScore as the reward, we compare Flow-GRPO with different initial noise against Flow-GRPO with the same initial noise. Figure 11 shows the variant with different noise consistently achieved high rewards during the training process.

**ZH** 我们用不同的随机噪声初始化每次 rollout，以提升 RL 训练中的探索多样性。我们做了一项额外消融来证实这一判断。以 SD3.5-M 为基础模型、PickScore 为奖励，我们把使用不同初始噪声的 Flow-GRPO 与使用相同初始噪声的 Flow-GRPO 做比较。图 11 显示，使用不同噪声的变体在训练过程中持续取得更高的奖励。

<!-- [原子块 · object]  -->

**EN** Figure 10: Effect of Initial Noise

**ZH** 图 10：初始噪声的影响

<!-- [原子块 · object]  -->

**EN** Figure 11: Additional Results on FLUX.1-Dev

**ZH** 图 11：FLUX.1-Dev 上的额外结果

**EN** C.4 Additional Results on FLUX.1-Dev

**ZH** C.4 FLUX.1-Dev 上的额外结果

**EN** We run Flow-GRPO on FLUX.1-Dev [5] using PickScore as the reward signal. The reward curve rises steadily throughout training without noticeable reward hacking. Figure 11 shows the reward values over the training process, and Table 7 compares FLUX.1-Dev with FLUX.1-Dev + Flow-GRPO on DrawBench.

**ZH** 我们在 FLUX.1-Dev [5] 上运行 Flow-GRPO，使用 PickScore 作为奖励信号。奖励曲线在整个训练过程中稳步上升，没有明显的奖励黑客。图 11 显示了训练过程中的奖励值，表 7 比较了 FLUX.1-Dev 与 FLUX.1-Dev + Flow-GRPO 在 DrawBench 上的表现。

**EN** Table 7: Comparison of FLUX.1-Dev and Flow-GRPO fine-tuned models.

**ZH** 表 7：FLUX.1-Dev 与 Flow-GRPO 微调模型的比较。

<!-- [原子块 · table] Model Aesthetic DeQA ImageReward PickScore UnifiedReward FLUX.1-Dev 5.71 4.31 0.85 22.62 3.65 FLUX.1-Dev + Flow-GRPO 6.02 4.24 1.32 23.97 3.81 -->

**EN** C.5 Learning Curves with or without KL

**ZH** C.5 有无 KL 时的学习曲线

**EN** Figure 12 shows learning curves for three tasks, with and without KL. These results emphasize that KL regularization is not empirically equivalent to early stopping. Adding appropriate KL can achieve the same high reward as the KL-free version and maintain image quality, though it requires longer training.

**ZH** 图 12 给出了三项任务在有无 KL 时的学习曲线。这些结果强调，KL 正则化在实证上并不等价于早停：加入恰当的 KL 可以达到与无 KL 版本相同的高奖励并保持图像质量，尽管需要更长的训练时间。

<!-- [原子块 · object]  -->

**EN** (a) Compositional Image Generation

**ZH** (a) 组合式图像生成

<!-- [原子块 · object]  -->

**EN** (b) Visual Text Rendering

**ZH** (b) 视觉文字渲染

<!-- [原子块 · object]  -->

**EN** (c) Human Preference Alignment

**ZH** (c) 人类偏好对齐

**EN** Figure 12: Learning Curves with and without KL. KL penalty slows early training yet effectively suppresses reward hacking.

**ZH** 图 12：有无 KL 时的学习曲线。KL 惩罚在早期减缓训练，却能有效抑制奖励黑客。

**EN** C.6 Additional Qualitative Results

**ZH** C.6 额外的定性结果

**EN** Figures 13, 14 & 15 qualitatively compare SD3.5-M with its Flow-GRPO enhanced versions (with and without KL regularization) using GenEval, OCR and PickScore rewards, respectively. Flow-GRPO with KL regularization improves the target capability while maintaining image quality and minimizing reward-hacking. Conversely, removing the KL constraint significantly degrades image quality and diversity.

**ZH** 图 13、14 与 15 分别用 GenEval、OCR 与 PickScore 奖励，定性比较了 SD3.5-M 与其经 Flow-GRPO 增强的版本（有无 KL 正则化）。带 KL 正则化的 Flow-GRPO 在保持图像质量、最小化奖励黑客的同时提升了目标能力；相反，去掉 KL 约束会显著损害图像质量与多样性。

<!-- [原子块 · img]  -->

**EN** Figure 13: Additional Qualitative comparison between the SD3.5-M and SD3.5-M + Flow-GRPO trained with GenEval reward.

**ZH** 图 13：SD3.5-M 与用 GenEval 奖励训练的 SD3.5-M + Flow-GRPO 之间的额外定性比较。

<!-- [原子块 · img]  -->

**EN** Figure 14: Additional Qualitative comparison between the SD3.5-M and SD3.5-M + Flow-GRPO trained with OCR reward.

**ZH** 图 14：SD3.5-M 与用 OCR 奖励训练的 SD3.5-M + Flow-GRPO 之间的额外定性比较。

<!-- [原子块 · img]  -->

**EN** Figure 15: Additional Qualitative comparison between the SD3.5-M and SD3.5-M + Flow-GRPO trained with PickScore reward.

**ZH** 图 15：SD3.5-M 与用 PickScore 奖励训练的 SD3.5-M + Flow-GRPO 之间的额外定性比较。

**EN** C.7 Evolution of Evaluation Images During Flow-GRPO Training

**ZH** C.7 Flow-GRPO 训练过程中评估图像的演化

**EN** To better understand the training dynamics of our proposed Flow-GRPO framework, we visualize the evolution of generated samples corresponding to fixed evaluation prompts at regular intervals during training in Figure 16, 17 & 18. For consistency, all visualizations are produced using a 40-step ODE-based sampling schedule. These qualitative results provide a visual representation of how the model progressively improves its generation quality and alignment with task objectives over time.

**ZH** 为更好地理解我们所提 Flow-GRPO 框架的训练动态，我们在图 16、17 与 18 中可视化了训练期间按固定间隔、对应固定评估提示所生成样本的演化。为保持一致，所有可视化都使用 40 步基于 ODE 的采样调度生成。这些定性结果直观呈现了模型如何随时间逐步提升生成质量以及与任务目标的对齐程度。

<!-- [原子块 · img]  -->

**EN** Figure 16: We visualize the generated samples across successive training iterations during the optimization of SD3.5-Medium on the GenEval task.

**ZH** 图 16：我们可视化了在 GenEval 任务上优化 SD3.5-Medium 期间、连续训练迭代中生成的样本。

<!-- [原子块 · img]  -->

**EN** Figure 17: We visualize the generated samples across successive training iterations during the optimization of SD3.5-Medium on the OCR task.

**ZH** 图 17：我们可视化了在 OCR 任务上优化 SD3.5-Medium 期间、连续训练迭代中生成的样本。

<!-- [原子块 · img]  -->

**EN** Figure 18: We visualize the generated samples across successive training iterations during the optimization of SD3.5-Medium on the PickScore task.

**ZH** 图 18：我们可视化了在 PickScore 任务上优化 SD3.5-Medium 期间、连续训练迭代中生成的样本。

**EN** Appendix D Training Sample Visualization with Denoising Reduction

**ZH** 附录 D 降噪步数缩减下训练样本的可视化

**EN** In this section, we compare images obtained with SDE sampling at various steps against those produced by ODE sampling, and offer an intuitive view of the denoising reduction strategy. Figure 19 presents SD3.5-Medium samples under four inference settings: (a) ODE sampling with 40 steps; (b) SDE sampling with 40 steps; (c) SDE sampling with 10 steps; (d) SDE sampling with 5 steps.

**ZH** 本节我们把不同步数下 SDE 采样得到的图像与 ODE 采样产生的图像做比较，并给出降噪步数缩减策略的直观视图。图 19 呈现了 SD3.5-Medium 在四种推理设置下的样本：（a）40 步 ODE 采样；（b）40 步 SDE 采样；（c）10 步 SDE 采样；（d）5 步 SDE 采样。

**EN** The 40-step ODE and SDE runs yield visually indistinguishable images, confirming that our SDE sampler preserves quality. Shortening the SDE schedule to 10 and 5 steps introduces conspicuous artifacts, like color drift and fine details blur. Contrary to expectation that such low-quality samples might hinder optimization. it actually do just the opposite and accelerate optimization. Because Flow-GRPO relies on relative preferences, it still extracts a useful reward signal, while the shorter trajectories signifactly cut wall-clock time. Consequently, Flow-GRPO with denoising reduction strategy converges more quickly on both layout-oriented benchmarks such as GenEval and quality-focused metrics such as PickScore, without sacrificing final performance.

**ZH** 40 步的 ODE 与 SDE 采样产生的图像在视觉上无法区分，证实我们的 SDE 采样器保持了质量。把 SDE 调度缩短到 10 步与 5 步会引入明显的伪影，如颜色漂移与细节模糊。与「这类低质量样本可能妨碍优化」的预期相反，它们的效果恰恰相反，反而加速了优化：由于 Flow-GRPO 依赖相对偏好，它仍能提取出有用的奖励信号，而更短的轨迹显著削减了实际耗时。因此，采用降噪步数缩减策略的 Flow-GRPO 在 GenEval 等布局导向的基准与 PickScore 等质量导向的指标上都收敛得更快，且不牺牲最终性能。

<!-- [原子块 · img]  -->

**EN** Figure 19: Visualization of training samples under difference inference settings.

**ZH** 图 19：不同推理设置下训练样本的可视化。
