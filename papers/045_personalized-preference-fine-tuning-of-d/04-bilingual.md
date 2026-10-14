# 扩散模型的个性化偏好微调

> 原标题：Personalized Preference Fine-tuning of Diffusion Models
> 作者：Meihua Dang, Anikait Singh, Linqi Zhou, Stefano Ermon, Jiaming Song · arXiv:2501.06655 · 2025-01-11

<!-- [原子块 · verbatim] Personalized Preference Fine-tuning of Diffusion Models -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] RLHF techniques like DPO can significantly improve the generation quality of text-to-image diffusion models. However, these methods optimize for a single reward that aligns model generation with popul -->

**EN** 1 Introduction

**ZH** 1 引言

**EN** Diffusion models [12, 40, 42, 43] have achieved great success in text-to-images generation tasks, as demonstrated by models such as DALL-E 2 [33], Imagen [35], Stable Diffusion [34, 29], and Stable Cascade [27]. These large-scale models, often trained through supervised fine-tuning on text-image datasets containing high-quality aesthetic images such as LAION-5B [38], demonstrate impressive image quality and a remarkable visual understanding of text prompts. Recent advances focus on fine-tuning diffusion models to better align with human preferences. Methods such as DDPO [2] and DPOK [9] employ reinforcement learning from human feedback (RLHF) techniques to optimize human-alignment reward functions. Alternatively, Diffusion-DPO [45] utilize direct preference optimization (DPO) [32] to directly optimizes for human preferences using an offline ranking dataset. SD3 [7] shows that fine-tuning diffusion models with human feedback techniques can significantly enhance overall image quality.

**ZH** 扩散模型 [12, 40, 42, 43] 在文本到图像生成任务上取得了巨大成功，DALL-E 2 [33]、Imagen [35]、Stable Diffusion [34, 29] 与 Stable Cascade [27] 等模型即为代表。这些大规模模型通常在 LAION-5B [38] 这类包含高质量美学图像的图文数据集上做监督微调，展现出令人印象深刻的图像质量，以及对文本提示出色的视觉理解能力。近期研究聚焦于微调扩散模型以更好地契合人类偏好：DDPO [2] 与 DPOK [9] 等方法采用人类反馈强化学习（RLHF）技术来优化人类对齐奖励函数；Diffusion-DPO [45] 则改用直接偏好优化（DPO）[32]，借助离线排序数据集直接针对人类偏好做优化。SD3 [7] 表明，用人类反馈技术微调扩散模型可显著提升整体图像质量。

**EN** Despite these promising results, Diffusion-DPO aligns a model with a single reward that represents population-level human preferences. These fine-tuning techniques are thus insufficient for achieving personalized preference alignment. As studied in domains such as language [36, 10, 44], individual users have unique preferences—for instance, some may favor images with brighter colors, while others might prefer images with centralized foregrounds. Fine-tuning a separate model for each person based on their preference data is impractical and does not scale well, limiting the feasibility of personalized alignment. Additionally, this may limit cross-user generalization.

**ZH** 尽管结果喜人，Diffusion-DPO 只能让模型对齐单一奖励，而该奖励代表的是群体层面的人类偏好，这类微调技术因而不足以实现个性化偏好对齐。正如语言领域 [36, 10, 44] 的研究所指出的，个体用户有各自独特的偏好——例如有人偏爱色彩更明亮的图像，有人则更喜欢主体居中的构图。依据每位用户的偏好数据分别微调一个模型既不现实也难以扩展，限制了个性化对齐的可行性，并且可能削弱跨用户的泛化能力。

**EN** A complementary research direction introduces additional control mechanisms into diffusion models to enable customization and personalization. Approaches such as IP-Adapter [51] and CtrlNet [54] allow for controlled image generation by using an additional conditioning image that encodes personalization features. However, these methods are constrained by their reliance on single-image inputs and do not directly learn or adapt to human preferences.

**ZH** 另一条互补的研究路线是向扩散模型引入额外的控制机制，以实现定制与个性化。IP-Adapter [51] 与 CtrlNet [54] 等方法通过一张编码了个性化特征的额外条件图像来实现可控图像生成。不过这些方法受限于只能接受单张图像输入，并不直接学习或适应人类偏好。

**EN** To address these limitations, we propose PPD, a general framework that incorporates personalization into a diffusion model preference alignment through multi-reward optimization. Our approach learns a diverse set of human preferences within a single model and generalizes effectively to new users. Personalization in our approach requires minimal additional data, as we label samples in the preference dataset with a unique identifier for each user. This annotation is inexpensive to obtain and commonly included in datasets such as Pick-a-Pic [16]. We leverage vision-language models (VLMs) such as LLaVA-OneVision [20] to extract user preference embeddings from few-shot pairwise preference examples for each user. We show that these few-shot text embeddings from preference pairs serve as effective features to represent reward functions under the Bradley-Terry model [3] and thus are suitable for conditioning the diffusion model. Next, adopting Stable Cascade [27] as our base model, we condition the diffusion model on these user embeddings through additional cross-attention layers and fine-tune it with a variant of the Diffusion-DPO [45] objective for preference alignment.

**ZH** 为克服上述局限，我们提出 PPD——一个通过多奖励优化把个性化引入扩散模型偏好对齐的通用框架。该方法在单一模型内学到多样化的人类偏好，并能有效泛化到新用户。个性化所需的额外数据极少：只需在偏好数据集中为每个用户标注唯一标识即可。这类标注获取成本低廉，Pick-a-Pic [16] 等数据集通常已包含。我们利用 LLaVA-OneVision [20] 等视觉语言模型（VLM），从每位用户的少样本成对偏好示例中提取用户偏好嵌入。我们证明，这些来自偏好对的少样本文本嵌入在 Bradley-Terry 模型 [3] 下可作为表征奖励函数的有效特征，因而适合作为扩散模型的条件。随后，我们以 Stable Cascade [27] 为基座模型，通过额外的交叉注意力层把用户嵌入作为条件注入扩散模型，并用 Diffusion-DPO [45] 目标的一个变体做偏好对齐微调。

**EN** Our empirical evaluations demonstrate that PPD can effectively optimize multiple rewards including CLIP [13, 31], Aesthetic [37], and HPS [47], significantly outperforming baselines. It also interpolates smoothly between different rewards during inference. Additionally, in real-world user scenarios, PPD aligns more closely with individual user preferences on the dataset Pick-a-Pic [16]. Notably, with only a few-shot ranking examples for a new user, PPD generate images that align closely with that user’s specific preference and outperforms prior approaches such as Stable Cascade, achieving an average win rate of 76%, as evaluated by GPT4o [26].

**ZH** 实验表明，PPD 能有效优化 CLIP [13, 31]、Aesthetic [37] 与 HPS [47] 等多个奖励，显著优于基线方法，并且在推理时可在不同奖励之间平滑插值。此外，在真实用户场景中，PPD 在 Pick-a-Pic [16] 数据集上与个体用户偏好的吻合度更高。值得注意的是，仅需为新用户提供少量排序示例，PPD 就能生成高度贴合该用户特定偏好的图像，在 GPT4o [26] 评测下相对 Stable Cascade 取得 76% 的平均胜率。

<!-- [原子块 · img]  -->

**EN** Figure 1: The overall architecture of PPD. In Stage 1, user embedding are generated with few-shot preference examples using a VLM. In Stage 2, we fine-tune diffusion models on the preference datasets with the user embedding as conditioning added to cross-attention.

**ZH** 图 1：PPD 的整体架构。阶段一，用视觉语言模型基于少样本偏好示例生成用户嵌入；阶段二，在偏好数据集上微调扩散模型，并将用户嵌入作为条件加入交叉注意力。

**EN** 2 Related Work

**ZH** 2 相关工作

**EN** Aligning Diffusion Models

**ZH** 扩散模型对齐

**EN** Aligning text-to-image diffusion models has been extensively studied. Some methods optimize with online RL using a Bradley Terry reward function [2, 9, 55]. Others fine-tune diffusion models to increase the reward of generated images by gradient back-propagation on the reward function [5, 49, 30]. Recently proposed approaches [45, 50] leverage the duality of the reward learning and policy optimization from DPO [32] to eliminate the need of on-policy samples and only utilize offline human preference data. Alternatively, DiffusionKTO [22] replaces DPO with KTO [8], eliminating the need for paired data. Additionally, some methods modify the training data distribution on visually appealing and textually cohered data [48, 18, 6], while others improve text accuracy by re-captioning pre-collected web images [11, 39].

**ZH** 文生图扩散模型的对齐已被广泛研究。部分方法采用 Bradley-Terry 奖励函数做在线强化学习优化 [2, 9, 55]；另一些则在奖励函数上做梯度反向传播来微调扩散模型，以提高生成图像的奖励值 [5, 49, 30]。近期工作 [45, 50] 利用 DPO [32] 中奖励学习与策略优化的对偶性，摆脱了对同策略样本的依赖，仅使用离线人类偏好数据。此外，DiffusionKTO [22] 用 KTO [8] 取代 DPO，不再需要成对数据。还有一些方法从数据侧入手，调整训练数据分布以偏向视觉美观、文本一致的数据 [48, 18, 6]，或通过重新标注已采集的网络图像来提升文本准确性 [11, 39]。

**EN** Controllable Generation for Diffusion Models

**ZH** 扩散模型的可控生成

**EN** To address the lack of fine-grained control in image synthesis, various methods add conditional controls to text-to-image diffusion models. CtrlNet [54] and T2I-Adapter [25] introduce additional UNet modules that encode spatial information, such as edges and human poses, derived from conditioning images. IP-Adapter [51] introduces additional cross-attention layers to incorporate high-level semantic information from reference images.

**ZH** 为弥补图像合成中细粒度控制的缺失，多种方法为文生图扩散模型加入了条件控制。CtrlNet [54] 与 T2I-Adapter [25] 引入额外的 UNet 模块来编码边缘、人体姿态等来自条件图像的空间信息；IP-Adapter [51] 则引入额外的交叉注意力层，以注入参考图像的高层语义信息。

**EN** LLM Alignment

**ZH** 大语言模型对齐

**EN** The alignment of large language models (LLMs) using RLHF objectives has been extensively explored [56, 1, 32], demonstrating effective instruction-following and alignment to population values. However, a key challenge remains in representing the diversity of human preferences [36], as these models often capture an averaged population preference rather than accounting for individual differences, leading to biases and reduced alignment with underrepresented communities. Pluralistic Alignment [10, 44] addresses this issue by modeling a distribution of individuals, each with distinct values and perspectives, with methods like distributional and overton alignment enhancing calibration across diverse user groups. Several works have investigated LLM personalization through the reparameterization of reward models [28, 52, 23], enabling a more tailored user experience. However, these works leverage synthetic users and study a limited number of users, particularly in text and robotic control domains.

**ZH** 用 RLHF 目标对齐大语言模型（LLM）的研究已相当充分 [56, 1, 32]，在指令跟随与对齐群体价值观方面效果显著。然而如何表征人类偏好的多样性 [36] 仍是一大难题：这些模型往往只捕捉到平均化的群体偏好，未顾及个体差异，因而产生偏见，并降低与弱势群体之间的对齐程度。Pluralistic Alignment [10, 44] 通过对个体分布建模来应对该问题——每个个体拥有各自的价值观与视角，分布式对齐与 overton 对齐等方法则提升了跨多样用户群体的校准效果。另有若干工作通过重参数化奖励模型来研究 LLM 个性化 [28, 52, 23]，以提供更贴合的用户体验。不过这些工作依赖合成用户，研究的用户数量有限，且主要集中于文本与机器人控制领域。

**EN** 3 Preliminary

**ZH** 3 预备知识

**EN** We introduce the preliminaries behind diffusion models, DPO and its adaption to diffusion models.

**ZH** 本节介绍扩散模型、DPO 及其在扩散模型上的适配形式背后的预备知识。

**EN** Diffusion Models

**ZH** 扩散模型

**EN** Diffusion models are generative models consisting two processes: a forward (diffusion) process and a backward (denoising) process [12, 40, 42, 43]. In the forward process, Gaussian noise ⟦SLOT_0⟧ is progressively added to a data distribution ⟦SLOT_1⟧ over ⟦SLOT_2⟧ steps, guided by noise scheduling functions ⟦SLOT_3⟧ and ⟦SLOT_4⟧. At timestep ⟦SLOT_5⟧, noisy images ⟦SLOT_6⟧ are generated via ⟦SLOT_7⟧. In the backward process, samples are generated from Gaussian noise with a learnable model, which can also be conditioned on additional inputs, such as text in the case of text-to-image diffusion models. Typically, diffusion models – denoted as ⟦SLOT_8⟧ – are trained to predict the Gaussian noise ⟦SLOT_9⟧ from noisy images ⟦SLOT_10⟧ at timestep ⟦SLOT_11⟧ with conditioning ⟦SLOT_12⟧, using a denoising objective:

**ZH** 扩散模型是一类由前向（扩散）过程与反向（去噪）过程构成的生成模型 [12, 40, 42, 43]。前向过程中，高斯噪声 ⟦SLOT_0⟧ 被逐步加入数据分布 ⟦SLOT_1⟧，共进行 ⟦SLOT_2⟧ 步，由噪声调度函数 ⟦SLOT_3⟧ 与 ⟦SLOT_4⟧ 引导；在时刻 ⟦SLOT_5⟧，加噪图像 ⟦SLOT_6⟧ 经由 ⟦SLOT_7⟧ 生成。反向过程中，样本由一个可学习模型从高斯噪声生成，该模型还可附加条件输入，文生图扩散模型中的文本即属此类。通常，记为 ⟦SLOT_8⟧ 的扩散模型被训练为预测高斯噪声 ⟦SLOT_9⟧，即从加噪图像 ⟦SLOT_10⟧ 出发，在时刻 ⟦SLOT_11⟧ 以条件 ⟦SLOT_12⟧ 完成预测，使用的去噪目标为：

<!-- [原子块 · table] L DM = 𝔼 𝐱 0 , ϵ , t ​ [ ω ⁡ ( λ t ) ​ ‖ ϵ − ϵ θ ​ ( 𝐱 t , 𝐜 , t ) ‖ 2 2 ] , L_{\text{DM}}=\mathbb{E}_{{\mathbf{x}}_{0},{\mathbf{\epsilon}},t}\left[\omega(\lambda_{t})\|{\mathbf{\epsilon}}-{\mathbf{\e -->

**EN** where ⟦SLOT_13⟧ is a signal-to-noise ratio, ⟦SLOT_14⟧ is a pre-specified weighting function [14]. Once the model ⟦SLOT_15⟧ is trained, images can be generated from random noise using accelerated sampling methods such as DDIM [41].

**ZH** 其中 ⟦SLOT_13⟧ 为信噪比，⟦SLOT_14⟧ 是预先设定的加权函数 [14]。模型 ⟦SLOT_15⟧ 训练完成后，即可用 DDIM [41] 等加速采样方法从随机噪声生成图像。

**EN** Direct Preference Optimization (DPO)

**ZH** 直接偏好优化（DPO）

**EN** DPO [32] is a fine-tuning paradigm that aligns autoregressive large language models (LLMs) with human preferences without relying on traditional reinforcement learning techniques. Unlike Reinforcement Learning from Human Feedback (RLHF), which involves training a reward model and then fine-tuning the LLM using reinforcement learning, DPO directly optimizes the model based on human preference data. Given a dataset containing ranking pairs ⟦SLOT_16⟧ where ⟦SLOT_17⟧ being the prompt and ⟦SLOT_18⟧ being the preferred and dispreferred responses labeled by human, the training objective optimizes a simple loss under which we can obtain an optimal policy:

**ZH** DPO [32] 是一种微调范式，可在不依赖传统强化学习技术的前提下让自回归大语言模型（LLM）对齐人类偏好。与需要先训练奖励模型、再用强化学习微调 LLM 的人类反馈强化学习（RLHF）不同，DPO 直接基于人类偏好数据优化模型。给定包含排序对 ⟦SLOT_16⟧ 的数据集，其中 ⟦SLOT_17⟧ 为提示，⟦SLOT_18⟧ 为人类标注的优选与非优选回复，训练目标优化一个简单损失，由此可得到最优策略：

<!-- [原子块 · table] L DPO ​ ( θ ) = − 𝔼 𝐜 , 𝐱 0 + , 𝐱 0 − ​ [ log ⁡ σ ⁡ ( β ​ Δ ) ] , where Δ = ( log ⁡ p θ ​ ( 𝐱 0 + | 𝐜 ) p ref ​ ( 𝐱 0 + | 𝐜 ) − log ⁡ p θ ​ ( 𝐱 0 − | 𝐜 ) p ref ​ ( 𝐱 0 − | 𝐜 ) ) , \displaystyle\begin{ -->

**EN** where ⟦SLOT_19⟧ is the sigmoid function and ⟦SLOT_20⟧ is a hyperparameter determining how much ⟦SLOT_21⟧ may deviate from a reference distribution ⟦SLOT_22⟧. Intuitively, the objective aims to increase the likelihoods of preferred responses while decreasing that of dispreferred ones.

**ZH** 其中 ⟦SLOT_19⟧ 为 sigmoid 函数，⟦SLOT_20⟧ 是决定 ⟦SLOT_21⟧ 允许偏离参考分布 ⟦SLOT_22⟧ 多少的超参数。直观地说，该目标旨在提高优选回复的似然，同时降低非优选回复的似然。

**EN** Diffusion DPO

**ZH** 扩散 DPO

**EN** The DPO objective in Eq. 2 requires optimization of log-likelihoods ⟦SLOT_23⟧, which is analytically intractable for diffusion models. Diffusion-DPO [45] leverages the fact that the (appropriately weighted) training objective of diffusion models as in Eq. 1 can be viewed as the evidence lower bound (ELBO) of their log-likelihoods. It derives an upper bound to DPO for diffusion models to align them with human preferences:

**ZH** 式 2 中的 DPO 目标需要优化对数似然 ⟦SLOT_23⟧，这对扩散模型而言难以解析求解。Diffusion-DPO [45] 利用了一个事实：式 1 中经过适当加权的扩散模型训练目标可视为其对数似然的证据下界（ELBO）。由此推导出适用于扩散模型的 DPO 上界，使其对齐人类偏好：

<!-- [原子块 · table] L Diff-DPO ​ ( θ ) = − 𝔼 𝐜 , 𝐱 0 + , 𝐱 0 − ​ [ log ⁡ σ ⁡ ( − β ​ T ​ ω ​ ( λ t ) ​ Δ ) ] , where \displaystyle L_{\text{Diff-DPO}}({\mathbf{\theta}})=-\mathbb{E}_{{\mathbf{c}},{\mathbf{x}}^{+}_{0},{\m -->

**EN** where ⟦SLOT_24⟧ is the caption; ⟦SLOT_25⟧ and ⟦SLOT_26⟧ are the preferred and dispreferred images; ⟦SLOT_27⟧ and ⟦SLOT_28⟧ are noisy images obtained from forward process with Gaussian noise ⟦SLOT_29⟧ and ⟦SLOT_30⟧ at timestep ⟦SLOT_31⟧. This objective computes 4 terms as in Eq. 1: the denoising loss of training and preference distributions ⟦SLOT_32⟧ and ⟦SLOT_33⟧ on preferred and dispreferred noisy images ⟦SLOT_34⟧ and ⟦SLOT_35⟧ respectively. Intuitively, it aims to decrease the loss of preferred images while increasing that of dispreferred ones.

**ZH** 其中 ⟦SLOT_24⟧ 为图像描述；⟦SLOT_25⟧ 与 ⟦SLOT_26⟧ 分别为优选与非优选图像；⟦SLOT_27⟧ 与 ⟦SLOT_28⟧ 是由前向过程得到的加噪图像，所用高斯噪声为 ⟦SLOT_29⟧ 与 ⟦SLOT_30⟧，时刻为 ⟦SLOT_31⟧。该目标如式 1 那样计算四项：训练分布 ⟦SLOT_32⟧ 与偏好分布 ⟦SLOT_33⟧ 分别在优选与非优选加噪图像 ⟦SLOT_34⟧ 与 ⟦SLOT_35⟧ 上的去噪损失。直观上，它旨在降低优选图像的损失、提高非优选图像的损失。

**EN** 4 Method

**ZH** 4 方法

**EN** Despite impressive image quality and alignment control achieved in prior works, a key limitation among works that use DPO for diffusion models is that it assumes a uniform preference among all users for generated images. In practice, this assumption often fails, as individuals may have diverse preferences related to style, color, lighting, and other visual attributes. While such preferences can be easily expressed by human through pairwise comparisons, it is challenging to summarize them accurately through text or single-image prompts, due to the inaccuracy of natural language and the limitations inherent in single-prompt formats.

**ZH** 尽管已有工作在图像质量与对齐控制上表现出色，但用 DPO 训练扩散模型的方法存在一个关键局限：它假定所有用户对生成图像的偏好是一致的。实践中该假设常常不成立，个体在风格、色彩、光照等视觉属性上可能有截然不同的偏好。这类偏好很容易通过成对比较由人表达出来，却难以用文本或单张图像的提示准确概括——自然语言本身不够精确，单一提示的形式也有固有局限。

**EN** Motivated by this problem, we propose PPD, a method that aligns diffusion models with individual-level human preferences. We first formulate the problem of personalization and define a new DPO variant for this task (Sec. 4.1), and then show that individual-level preference learning can be achieved using few-shot comparison examples using a VLM (Sec. 4.2), finally we introduce a parameterization of denoiser that can takes advantage of the VLM embeddings (Sec. 4.3). The overall architecture is in Fig. 1.

**ZH** 针对这一问题，我们提出 PPD，一种让扩散模型对齐个体层面人类偏好的方法。我们先形式化描述个性化问题并为该任务定义新的 DPO 变体（第 4.1 节），随后说明如何借助视觉语言模型、利用少样本比较示例实现个体层面的偏好学习（第 4.2 节），最后给出一种能利用 VLM 嵌入的去噪器参数化方式（第 4.3 节）。整体架构见图 1。

**EN** 4.1 Problem Setup

**ZH** 4.1 问题设定

**EN** We consider a dataset containing ⟦SLOT_36⟧ where ⟦SLOT_37⟧ is the text prompt, ⟦SLOT_38⟧ are preferred and dispreferred generated images and ⟦SLOT_39⟧ represents the user labeling the preference. User features ⟦SLOT_40⟧ can be high-dimensional including information like age or gender, but often ⟦SLOT_41⟧ consists only of scalar user IDs ⟦SLOT_42⟧. We define ⟦SLOT_43⟧ as the reward on image ⟦SLOT_44⟧ for user ⟦SLOT_45⟧ given prompt ⟦SLOT_46⟧. We would like to fine-tune a text-to-image models ⟦SLOT_47⟧ for individual user ⟦SLOT_48⟧ such that reward is maximized for this user while keeping close to a reference model ⟦SLOT_49⟧ in terms of KL-divergence as regularization :

**ZH** 考虑一个数据集 ⟦SLOT_36⟧，其中 ⟦SLOT_37⟧ 为文本提示，⟦SLOT_38⟧ 为优选与非优选生成图像，⟦SLOT_39⟧ 表示标注该偏好的用户。用户特征 ⟦SLOT_40⟧ 可以是高维的，包含年龄、性别等信息，但通常 ⟦SLOT_41⟧ 仅由标量用户 ID ⟦SLOT_42⟧ 构成。我们把 ⟦SLOT_43⟧ 定义为图像 ⟦SLOT_44⟧ 对用户 ⟦SLOT_45⟧ 的奖励，其中提示为 ⟦SLOT_46⟧。我们希望微调文生图模型 ⟦SLOT_47⟧ 以适应个体用户 ⟦SLOT_48⟧，使该用户的奖励最大化，同时以 KL 散度为正则项，保持与参考模型 ⟦SLOT_49⟧ 接近：

<!-- [原子块 · table] max p θ i 𝔼 𝐜 , 𝐱 0 ​ [ r ⁡ ( 𝐜 , 𝐱 0 , 𝐮 i ) ] − β 𝔻 KL [ p θ i ( 𝐱 0 | 𝐜 ) ∥ p ref ( 𝐱 0 | 𝐜 ) ] , \displaystyle\begin{split}\max_{p_{\theta_{i}}}&\mathbb{E}_{{\mathbf{c}},{\mathbf{x}}_{0}}\left[r({ -->

**EN** where ⟦SLOT_50⟧ is a parameter controlling how much ⟦SLOT_51⟧ deviates from ⟦SLOT_52⟧. Following [32], the optimal ⟦SLOT_53⟧ for user ⟦SLOT_54⟧ takes the form

**ZH** 其中 ⟦SLOT_50⟧ 是控制 ⟦SLOT_51⟧ 偏离 ⟦SLOT_52⟧ 幅度的参数。沿用 [32]，最优的 ⟦SLOT_53⟧（对应用户 ⟦SLOT_54⟧）具有如下形式

<!-- [原子块 · table] p θ i ​ ( 𝐱 0 | 𝐜 ) ∝ p ref ​ ( 𝐱 0 | 𝐜 ) ​ exp ⁡ ( r ⁡ ( 𝐜 , 𝐱 0 , 𝐮 i ) / β ) . p_{\theta_{i}}({\mathbf{x}}_{0}|{\mathbf{c}})\propto p_{\text{ref}}({\mathbf{x}}_{0}|{\mathbf{c}})\exp\left(r({\mathbf -->

**EN** Suppose model ⟦SLOT_55⟧ has sufficient capacity, we can represent ⟦SLOT_56⟧ as ⟦SLOT_57⟧, where ⟦SLOT_58⟧ serves as as a conditioning. This allows us to jointly optimize a single model ⟦SLOT_59⟧ for all users. Following [45], we have the following objective to learn a personalized diffusion models:

**ZH** 假设模型 ⟦SLOT_55⟧ 容量充足，我们可以将 ⟦SLOT_56⟧ 表示为 ⟦SLOT_57⟧，其中 ⟦SLOT_58⟧ 充当条件。这样便能用单一模型 ⟦SLOT_59⟧ 联合优化所有用户。沿用 [45]，我们得到如下用于学习个性化扩散模型的目标：

<!-- [原子块 · table] L PPD ​ ( θ ) = − 𝔼 𝐜 , 𝐱 0 + , 𝐱 0 − , 𝐮 ​ [ log ⁡ σ ⁡ ( − β ​ T ​ ω ​ ( λ t ) ​ Δ ) ] , where \displaystyle L_{\text{PPD }}({\mathbf{\theta}})=-\mathbb{E}_{{\mathbf{c}},{\mathbf{x}}^{+}_{0},{\mathbf -->

**EN** This objective is similar to Eq. 3 but with the addition of ⟦SLOT_60⟧, representing extra features conditioned on for each user. But what user features should be conditioned on?

**ZH** 该目标与式 3 类似，只是增加了 ⟦SLOT_60⟧，表示每位用户额外的条件特征。那么，究竟应该以什么用户特征为条件？

**EN** 4.2 Generating User Features from a VLM with In-Context Examples

**ZH** 4.2 借助上下文示例从视觉语言模型生成用户特征

**EN** Discussion on User Features in Preference Datasets

**ZH** 关于偏好数据集中用户特征的讨论

**EN** One fundamental challenge in personalized image generation lies in the effective parameterization of the user representation, denoted as ⟦SLOT_61⟧, for each individual. This parameterization is critical because it directly influences the model’s capacity to generate outputs tailored to specific user preferences. Existing image preference datasets, such as Pick-a-Pic [16], typically lack comprehensive user information beyond basic identifiers, often focusing on generic preference data rather than capturing the nuanced individual preferences necessary for effective personalization.

**ZH** 个性化图像生成的一个根本挑战，在于如何为每个个体有效参数化用户表征 ⟦SLOT_61⟧。这一参数化至关重要，因为它直接影响模型生成贴合特定用户偏好输出的能力。Pick-a-Pic [16] 等现有图像偏好数据集除基础标识外通常缺乏完整的用户信息，往往只关注泛化的偏好数据，而没有捕捉有效个性化所必需的细微个体偏好。

**EN** Even in preference datasets that include user information (e.g PRISM [15]), this information is frequently obtained through self-reported surveys, which can lead to incomplete or biased user profiles. Discrepancies often arise between stated preferences and actual behavior; users may not accurately articulate their likes and dislikes, or they may respond in a manner that they perceive as socially desirable rather than truthful. Such inconsistencies present significant challenges when attempting to model and predict user preferences accurately.

**ZH** 即便在包含用户信息的偏好数据集中（如 PRISM [15]），这些信息也多来自自我报告式问卷，容易导致用户画像不完整或有偏。陈述偏好与实际行为之间常有出入：用户未必能准确表达自己的喜好，也可能按社会期许而非真实想法作答。这类不一致给准确建模与预测用户偏好带来了显著困难。

**EN** To address these issues, we adopt a simplified approach by assuming access solely to a unique user ID for each individual in the dataset. This user ID serves as a key to differentiate users within the labeled preference dataset, represented as ⟦SLOT_62⟧, where ⟦SLOT_63⟧ denotes a unique user identifier.

**ZH** 为规避这些问题，我们采取简化处理：假设数据集中每个个体只有一个唯一用户 ID 可用。该 ID 作为在带标注偏好数据集中区分用户的键，记作 ⟦SLOT_62⟧，其中 ⟦SLOT_63⟧ 表示唯一的用户标识。

<!-- [原子块 · img]  -->

**EN** Figure 2: Top-K accuracy of the User Classification. We fine-tune a user-classifier from the frozen embeddings from the VLM on few-shot preference examples for 300 users. This classifier significantly outperforms a random chance baseline.

**ZH** 图 2：用户分类的 Top-K 准确率。我们基于视觉语言模型在少样本偏好示例上的冻结嵌入，为 300 位用户微调了一个用户分类器。该分类器显著优于随机猜测基线。

**EN** Conditioning on a Unique User Identifier

**ZH** 以唯一用户标识为条件

**EN** The primary challenge, then, is to leverage this user ID ⟦SLOT_64⟧ to construct a meaningful user embedding that can effectively guide the model’s predictions. A naïve approach might involve representing the embedding ⟦SLOT_65⟧ using a one-hot encoding of the user IDs, which can be formally defined by a function ⟦SLOT_66⟧, establishing a bijective mapping from the set of user IDs ⟦SLOT_67⟧ to the space of one-hot encoded vectors ⟦SLOT_68⟧, where ⟦SLOT_69⟧ represents the total number of unique users in the dataset. While this method uniquely encodes each user, it suffers from a critical limitation: the inability to generalize to new, unseen users, as the embedding space is inherently tied to the users present in the training data.

**ZH** 于是首要挑战变成：如何利用该用户 ID ⟦SLOT_64⟧ 构造出能有效指导模型预测的用户嵌入。一种朴素做法是用用户 ID 的 one-hot 编码表示嵌入 ⟦SLOT_65⟧，形式化地由函数 ⟦SLOT_66⟧ 定义，它建立从用户 ID 集合 ⟦SLOT_67⟧ 到 one-hot 编码向量空间 ⟦SLOT_68⟧ 的双射，其中 ⟦SLOT_69⟧ 为数据集中唯一用户的总数。该方法虽能唯一编码每位用户，却有致命缺陷：无法泛化到未见的新用户，因为嵌入空间与训练数据中出现过的用户牢牢绑定。

**EN** To enhance generalization and adaptability, we reconsider the parameterization of ⟦SLOT_70⟧ in the context of learning the distribution of reward functions, denoted as ⟦SLOT_71⟧. Here, a more flexible and robust parameterization leverages few-shot examples that reflect an individual user’s preferences. These examples can be extracted from the offline preference dataset for each user, providing concrete instances of preferred and dispreferred content. Conditioning on these examples allows for a more accurate estimation of the reward function ⟦SLOT_72⟧ for each user.

**ZH** 为提升泛化性与适应性，我们重新考虑 ⟦SLOT_70⟧ 的参数化，将其置于学习奖励函数分布 ⟦SLOT_71⟧ 的语境下。一种更灵活、更稳健的参数化方式是利用反映个体用户偏好的少样本示例。这些示例可从每位用户的离线偏好数据集中提取，提供了「喜欢什么、不喜欢什么」的具体实例。以这些示例为条件，可以更准确地估计每位用户的奖励函数 ⟦SLOT_72⟧。

**EN** In this work, we utilize the features of a pre-trained vision-language Model (VLM), specifically LLaVA-OneVision [21], an open-source multimodal model with multi-image processing capabilities. For each user, a set of ⟦SLOT_73⟧ few-shot examples is selected, comprising a caption describing the context, a preferred image, and a dispreferred image. These examples are processed by the VLM, from which we extract an intermediate hidden state.

**ZH** 本文采用预训练视觉语言模型（VLM）——具体为 LLaVA-OneVision [21]，一个具备多图处理能力的开源多模态模型——的特征。对每位用户选取 ⟦SLOT_73⟧ 个少样本示例，每个示例由一段描述上下文的说明文字、一张优选图像与一张非优选图像组成。这些示例经 VLM 处理后，我们提取其中一个中间隐藏状态。

**EN** To validate that the user embedding is effective, we condition on the frozen embedding to classify which user provided the preference annotations. As seen in Figure 2, the classifier significantly outperforms chance with a top-16 accuracy of 90%, indicating that the embedding can disentangle different users in the preference dataset effectively. By incorporating this user-specific embedding into the conditioning of a text-to-image diffusion model, we enable user-aware reward modeling and generation.

**ZH** 为验证用户嵌入的有效性，我们以该冻结嵌入为条件，去分类是哪位用户给出了偏好标注。如图 2 所示，分类器的 top-16 准确率达 90%，远超随机水平，说明该嵌入能有效区分偏好数据集中的不同用户。把这种用户专属嵌入纳入文生图扩散模型的条件，即可实现具备用户感知的奖励建模与生成。

**EN** 4.3 Personalization as Conditioning

**ZH** 4.3 把个性化作为条件

**EN** In order to add the user embedding as conditioning to the diffusion model in image generation, we utilize additional cross-attention layers akin to IP-Adapter [51]. Here we learn to condition on the user information using the VLM embeddings and then integrate the image features into pretrained UNet by adapted modules with decoupled cross-attention. There are many other ways to add conditioning information to diffusion models; we chose this instantiation due to its training and parameter efficiency.

**ZH** 为在图像生成时把用户嵌入作为条件加入扩散模型，我们采用了类似 IP-Adapter [51] 的额外交叉注意力层。具体地，我们学习以 VLM 嵌入所携带的用户信息为条件，再通过带解耦交叉注意力的适配模块把图像特征融入预训练 UNet。向扩散模型注入条件信息还有其他途径，我们选择这一实现方式是出于训练与参数效率的考虑。

**EN** We utilize Stable Cascade [27] as our base model which comprises of three stages: Stages A-C. Stage A and B are image compressors, similar to the VAE in Stable Diffusion [34] but achieve a much higher compression rate; and Stage C is the generation module conditioned on text. In Stage C, the text features ⟦SLOT_74⟧ from pretrained CLIP text encoder are plugged into the model by feeding into the cross-attention layers. Given the query features ⟦SLOT_75⟧ and text features ⟦SLOT_76⟧, the output is ⟦SLOT_77⟧ where ⟦SLOT_78⟧, ⟦SLOT_79⟧, ⟦SLOT_80⟧ are query, key and values, and ⟦SLOT_81⟧ are trainable layers.

**ZH** 我们以 Stable Cascade [27] 为基座模型，它包含 A、B、C 三个阶段。阶段 A 与 B 是图像压缩器，类似 Stable Diffusion [34] 中的 VAE，但压缩率高得多；阶段 C 是以文本为条件的生成模块。在阶段 C 中，预训练 CLIP 文本编码器给出的文本特征 ⟦SLOT_74⟧ 被送入交叉注意力层接入模型。给定查询特征 ⟦SLOT_75⟧ 与文本特征 ⟦SLOT_76⟧，输出为 ⟦SLOT_77⟧，其中 ⟦SLOT_78⟧、⟦SLOT_79⟧、⟦SLOT_80⟧ 分别是查询、键与值，⟦SLOT_81⟧ 为可训练层。

**EN** Following IP-Adapter [51], we utilize a decoupled cross-attention mechanism to condition on the user embedding. First, we add a new cross-attention layer to each cross-attention layer in the Stage C model, using the original query ⟦SLOT_82⟧ and introducing new keys ⟦SLOT_83⟧ and values ⟦SLOT_84⟧ for user features. Then, we simply add the output of user cross-attention to the output of text cross-attention. Hence the final formulation of cross-attention is

**ZH** 沿用 IP-Adapter [51]，我们采用解耦交叉注意力机制以用户嵌入为条件。首先，为阶段 C 模型中每个交叉注意力层各新增一个交叉注意力层，沿用原有查询 ⟦SLOT_82⟧，并为用户特征引入新的键 ⟦SLOT_83⟧ 与值 ⟦SLOT_84⟧。然后，把用户交叉注意力的输出直接加到文本交叉注意力的输出上。因此交叉注意力的最终形式为

<!-- [原子块 · table] 𝐙 ′ = Softmax ​ ( 𝐐𝐊 T d ) ​ 𝐕 + Softmax ​ ( 𝐐 ​ ( 𝐊 ′ ) T d ) ​ 𝐕 ′ , {\mathbf{Z}}^{\prime}=\text{Softmax}(\frac{{\mathbf{Q}}{\mathbf{K}}^{T}}{\sqrt{d}}){\mathbf{V}}+\text{Softmax}(\frac{{\mathbf{Q}} -->

**EN** where ⟦SLOT_85⟧, ⟦SLOT_86⟧, ⟦SLOT_87⟧, ⟦SLOT_88⟧, ⟦SLOT_89⟧ and ⟦SLOT_90⟧ are new introduced trainable parameters for ⟦SLOT_91⟧. During training, we optimize only the added cross-attention layers while keeping the parameters of pretrained diffusion model frozen, using the training objective as in Eq. 6. We also randomly drop user features (zero out the user embedding) in the training stage as regularization. This allows us to also prompt the model unconditionally of the user, by passing a zero embedding for the user.

**ZH** 其中 ⟦SLOT_85⟧、⟦SLOT_86⟧、⟦SLOT_87⟧、⟦SLOT_88⟧、⟦SLOT_89⟧ 与 ⟦SLOT_90⟧ 是为 ⟦SLOT_91⟧ 新引入的可训练参数。训练时我们只优化新增的交叉注意力层，冻结预训练扩散模型的参数，并使用式 6 的训练目标。训练阶段还随机丢弃用户特征（把用户嵌入置零）作为正则化。这样一来，我们也可以传入零嵌入，使模型在不依赖用户的情况下生成。

<!-- [原子块 · table] CLIP Aesthetic HPS Stable Cascade 31.97 5.33 23.87 Diffusion-DPO 32.48 5.46 25.96 SFT 32.26 5.56 25.78 ours 32.66 5.92 27.51 Diffusion-DPO (CLIP) 32.96 - - Diffusion-DPO (Aesthetic) - 6.42 - Diffusion -->

**EN** Table 1: Averaged scores on three reward function. We condition on each reward to generate images both in SFT and our methods. Diffusion-DPO (*) are upper-bounds.

**ZH** 表 1：三种奖励函数上的平均得分。SFT 与本文方法均以各奖励为条件生成图像。Diffusion-DPO（*）为性能上界。

**EN** 5 Experiments

**ZH** 5 实验

**EN** Models and Dataset

**ZH** 模型与数据集

**EN** In this section, we demonstrate the performance of PPD across a range of experiments designed to assess its capabilities in personalized preference alignment. We use the objective from Eq. 6 to fine-tune the open-source diffusion model, Stable Cascade [27] – specifically Stage C, which is responsible for text-conditioned generation. Following Wallace et al. [45], we fine-tune our model on the Pick-a-Pic v2 dataset [16], a preference dataset containing 58K text prompts and 0.8M image pairs labeled by 5K users.

**ZH** 本节通过一系列实验检验 PPD 在个性化偏好对齐上的能力。我们用式 6 的目标微调开源扩散模型 Stable Cascade [27]，具体是负责文本条件生成的阶段 C。沿用 Wallace 等 [45]，我们在 Pick-a-Pic v2 数据集 [16] 上微调模型，该偏好数据集含 58K 条文本提示与 0.8M 对图像，由 5K 位用户标注。

<!-- [原子块 · img]  -->

**EN** Figure 3: Automatic win rate evaluation with reward functions. We compare against Stable Cascade, Diffusion-DPO, and SFT.

**ZH** 图 3：基于奖励函数的自动胜率评测。对比对象为 Stable Cascade、Diffusion-DPO 与 SFT。

<!-- [原子块 · img]  -->

**EN** Figure 4: PPD is able to interpolate among three distinct objectives during inference. (a) generated images conditioned on (b) various weights, with three axes representing CLIP, Aesthetic, and HPS; (c) reward scores for each image. The score for each objective increases as its respective weight increases, and decreasing otherwise. For each row from left to right, the CLIP score increases alongside its weight, leading to a decrease in the Aesthetic score as its weight decreases. From bottom to top, the HPS score increases with its weight.

**ZH** 图 4：PPD 能在推理时对三个不同目标做插值。(a) 以 (b) 中不同权重为条件生成的图像，三个坐标轴分别代表 CLIP、Aesthetic 与 HPS；(c) 每张图像的奖励得分。某一目标的得分随其权重上升而升高，反之则下降。从左至右逐行看，CLIP 得分随其权重上升而提高，同时 Aesthetic 得分随权重下降而降低；自下而上，HPS 得分随其权重上升而提高。

**EN** Training Details

**ZH** 训练细节

**EN** During training of PPD, we only optimize the added cross-attention layers while keeping the pretrained diffusion model fixed, as described in Sec. 4.3. We use AdamW [24] with an effective batch size of 768 pairs and a learning rate of ⟦SLOT_92⟧ for all experiments, training for one epoch. We find ⟦SLOT_93⟧ for hyperparameter tuning. Details are in Appendix B.

**ZH** 训练 PPD 时，如第 4.3 节所述，我们只优化新增的交叉注意力层，固定预训练扩散模型。所有实验均使用 AdamW [24]，有效批大小为 768 对，学习率为 ⟦SLOT_92⟧，训练一个轮次。我们为超参数调优寻找 ⟦SLOT_93⟧，细节见附录 B。

**EN** User Information Conditioning

**ZH** 用户信息条件化

**EN** We begin by demonstrating the model’s ability to condition on synthetic user information, optimizing three distinct reward functions, we further show that generalize by linearly interpolating the weights of different reward functions (Sec. 5.1). We then show that the model can also condition on real user preferences, generating personalized images based on few-shot examples from new users (Sec. 5.2).

**ZH** 我们先展示模型以合成用户信息为条件、优化三种不同奖励函数的能力，并进一步说明通过对不同奖励函数权重做线性插值所体现的泛化性（第 5.1 节）。随后说明模型同样能以真实用户偏好为条件，依据新用户的少样本示例生成个性化图像（第 5.2 节）。

<!-- [原子块 · table] Stable Cascade Diffusion-DPO User Profile Append user profile to caption as augmentation Diffusion-DPO Ours The preferred images share common themes of wood grain, classic or futuristic design element -->

**EN** Figure 5: Qualitative Analysis of Images Generated by PPD and Baselines. Compared to Diffusion-DPO, PPD achieves closer alignment with the generated user profile, highlighted in green. The caption-augmented method captures user profile details; however, it often leads to unintended image alterations, causing the image to disregard the caption itself, as indicated in red.

**ZH** 图 5：PPD 与基线方法生成图像的定性分析。相比 Diffusion-DPO，PPD 与生成的用户画像吻合更紧密（绿色高亮部分）。改进提示词的方法虽能捕捉用户画像细节，却常引发非预期的图像改动，使图像忽略提示词本身（红色标注部分）。

**EN** 5.1 Synthetic User Alignment

**ZH** 5.1 合成用户对齐

**EN** Synthetic User

**ZH** 合成用户

**EN** We utilize three reward functions, each representing a aspect of image-to-text generation quality, to simulate three distinct synthetic users: (i) CLIP (OpenCLIP ViT-H/14) [13, 31] for prompt image alignment, (ii) Aesthetic Predictor [37] for image visual appeal, and (iii) HPSv2 (Human Preference Score v2) [47] for human preference estimate. In the dataset, each user has an equal chance of appearing. We relabel ranking pairs ⟦SLOT_94⟧ based on the above reward functions, where ⟦SLOT_95⟧ is a one-hot vector indicating the reward function, taking one of 3 values: ⟦SLOT_96⟧.

**ZH** 我们用三个奖励函数分别刻画文生图质量的一个方面，以模拟三位不同的合成用户：（i）CLIP（OpenCLIP ViT-H/14）[13, 31] 衡量提示与图像的对齐程度；（ii）Aesthetic Predictor [37] 衡量图像的视觉吸引力；（iii）HPSv2（人类偏好分数 v2）[47] 估计人类偏好。数据集中每位用户出现的概率相等。我们依据上述奖励函数重新标注排序对 ⟦SLOT_94⟧，其中 ⟦SLOT_95⟧ 是指示奖励函数的 one-hot 向量，取 3 个值之一：⟦SLOT_96⟧。

**EN** Baseline

**ZH** 基线方法

**EN** We compare our method with the following baseline: (1) Stable Cascade [27] pretrained model, which is also the reference model during training; (2) Diffusion-DPO, fine-tuned on Pick-a-Pic label without user conditioning [45]; (3) SFT, supervised fine-tuning on relabeled data with user conditioning. We also compare with (4) Diffusion-DPO (CLIP/Aesthetic/HPS), each annotation indicating a separately fine-tuned model with corresponding reward, this serves as the upper-bound of our method, where oracle information about the user is provided during inference to choose the appropriate model. For a fair comparison, all baselines are fine-tuned using Stable Cascade with the same architecture as our model, optimizing only the added cross-attention layers.

**ZH** 我们与下列基线比较：（1）Stable Cascade [27] 预训练模型，同时也是训练时的参考模型；（2）Diffusion-DPO，在 Pick-a-Pic 标注上微调但不加用户条件 [45]；（3）SFT，在重新标注的数据上做带用户条件的监督微调。还与（4）Diffusion-DPO（CLIP/Aesthetic/HPS）比较，每个标注对应一个用相应奖励单独微调的模型，这构成本文方法的上界——推理时提供了关于用户的预言信息，用以挑选合适的模型。为保证公平，所有基线都用与本文模型相同架构的 Stable Cascade 微调，只优化新增的交叉注意力层。

**EN** Text-to-Image Generation

**ZH** 文生图生成

**EN** For each method, we generate images with 30 inference steps using captions from PartiPrompts [53], a benchmark containing 1.6K examples across various categories and challenge aspects. For SFT and our method, we generate three images per prompt, each conditioned on one reward function. For Diffusion-DPO (CLIP/Aesthetic/HPS), images for each annotation are generated from its corresponding model. We report averaged reward scores in Tab. 1 and win rate comparisons in Fig. 3, we can see that our method significantly outperforms Stable Cascade in different reward functions, achieving win rates of 60%, 90%, and 93% in terms of CLIP, Aesthetic, and HPS respectively. Our method effectively optimizes each reward by conditioning on individual preference, outperforming supervised fine-tuning by a large margin. Unlike Diffusion-DPO, our method can jointly optimize multiple user rewards, achieving win rates comparable to Diffusion-DPO models fine-tuned separately on each user’s data.

**ZH** 每种方法都用 30 步推理生成图像，提示词取自 PartiPrompts [53]——一个包含 1.6K 条示例、覆盖多个类别与挑战方面的基准。SFT 与本文方法为每个提示生成三张图像，每张分别以一个奖励函数为条件；Diffusion-DPO（CLIP/Aesthetic/HPS）的各类图像则由对应模型生成。表 1 报告平均奖励得分，图 3 给出胜率对比。可以看到，本文方法在各奖励函数上均显著优于 Stable Cascade，在 CLIP、Aesthetic 与 HPS 上的胜率分别为 60%、90% 与 93%。本文方法通过以个体偏好为条件有效优化了每个奖励，大幅超过监督微调。与 Diffusion-DPO 不同，本文方法能联合优化多个用户奖励，取得的胜率与分别在各用户数据上微调的 Diffusion-DPO 模型相当。

**EN** Generalization via Interpolation

**ZH** 通过插值实现泛化

**EN** During training we fine-tune the model using one-hot encoding of each objective. Specifically, the user embedding vector ⟦SLOT_97⟧ being ⟦SLOT_98⟧ corresponding to optimization for CLIP, Aesthetic, and HPS. The user embedding can also be seen as weighting mechanism for each objective. However, during inference, we are also interested in whether we can trade-off among different objectives by interpolating their respective weights. In Fig. 4, we generate images conditioned on various objective weightings, namely interpolating the given user embedding, we can see that as the weight of an objective increases, the corresponding score also rises, and vice versa. Therefore, our method can generalize to different reward combinations, even only trained on single objective data. This can not be achieved by optimizing separate models and each with an objective.

**ZH** 训练时我们用每个目标的 one-hot 编码微调模型，即用户嵌入向量 ⟦SLOT_97⟧ 取 ⟦SLOT_98⟧，分别对应 CLIP、Aesthetic 与 HPS 的优化。用户嵌入也可视为各目标的加权机制。而在推理时，我们同样关心能否通过对各自权重插值来在不同目标间权衡。图 4 中，我们以不同的目标权重为条件生成图像，即对给定用户嵌入做插值；可以看到，某目标的权重增大时，对应得分随之上升，反之亦然。因此，即便只在单一目标数据上训练，本文方法也能泛化到不同的奖励组合，而这是为每个目标分别优化独立模型所无法实现的。

**EN** This shows that by linearly interpolating the user embedding, we can adjust the rewards of the generated images accordingly. This finding aligns with the real user experiments presented next, as real user embeddings exhibit a linear correlation in embedding space.

**ZH** 这表明，通过对用户嵌入做线性插值，我们可以相应地调节生成图像的各项奖励。该结论与接下来展示的真实用户实验相一致：真实用户嵌入在嵌入空间中呈现线性相关。

**EN** 5.2 Personalized Real User Alignment

**ZH** 5.2 真实用户个性化对齐

**EN** We now consider a realistic setting with preferences from the Pick-a-Pic dataset for each user. In this setting, we utilize the user features which are generated from a VLM on in-context preference examples as outlined in Section 4.2. We scale from the 3 synthetic ”users” in Section 5.1 to a filtered subset of the 4800 unique users in Pick-a-Pic.

**ZH** 现在考虑一个更贴近现实的设定：使用 Pick-a-Pic 数据集中每位用户的偏好。在此设定下，我们采用第 4.2 节所述、由视觉语言模型基于上下文偏好示例生成的用户特征。我们把第 5.1 节的 3 个合成「用户」扩展到 Pick-a-Pic 中筛选出的 4800 位唯一用户的子集。

**EN** Experiment setting

**ZH** 实验设置

**EN** We repartition the Pick-a-Pic dataset into a set of 4 splits: (1) Train, (2) Validation, (3) Test with Seen Users + Held-out Captions and (4) Test with Unseen Users + Held-out Captions. This decomposition allows us to study independently the generalization of our methods to new prompts and unseen users. Additionally, for each user, we take sets of ⟦SLOT_99⟧ few-shot preference examples for each user and use these groupings for the conditioning of the VLM on few-shot preference pairs. We thus have to filter out 824 users in Pick-a-Pic which have less than 4 examples per user, as no user embedding for this user can be formed. We generate the user embedding through the procedure outlined in Sec. 4.2.

**ZH** 我们把 Pick-a-Pic 数据集重新划分为 4 个子集：（1）训练集，（2）验证集，（3）已见用户 + 留出提示的测试集，（4）未见用户 + 留出提示的测试集。这一划分使我们能分别考察方法对新提示与未见用户的泛化能力。此外，我们为每位用户取 ⟦SLOT_99⟧ 组少样本偏好示例，用这些分组对视觉语言模型做少样本偏好对的条件化。由于每位用户不足 4 条示例时无法形成用户嵌入，我们据此剔除了 Pick-a-Pic 中的 824 位用户。用户嵌入按第 4.2 节的流程生成。

**EN** Generation Results

**ZH** 生成结果

**EN** We perform qualitative analysis on the set of images generated for each user. We perform this evaluation by generating a user profile per user. We use a set of few-shot preference pairs per user which we condition a VLM on along with Chain-of-Thought prompting (COT) to construct a user-profile consistent with the preference pairs. The COT prompt asks the model to summarize each image in the preference pair and describe the differences between them, which is then aggregated to form a user profile. Sample user profiles and the full Chain-of-Thought prompt is found in Appendix B. As seen in Fig. 5, our method has closer alignment to the user profile with respect to Stable Cascade and Diffusion-DPO, being able to pick up details about the user such as the highlighted part. While Stable Cascade and Diffusion-DPO with augmented captions can capture certain aspects of the user description, they often overfit to the user profile, resulting in generated images that overlook the intended image caption.

**ZH** 我们对每位用户生成的图像做定性分析，方法是为每位用户生成一份用户画像：取该用户的一组少样本偏好对，以此为视觉语言模型的条件，并结合思维链提示（COT）构建与偏好对一致的用户画像。该思维链提示要求模型先分别描述偏好对中的两张图像、再说明二者差异，最后汇总成用户画像。示例用户画像与完整思维链提示见附录 B。如图 5 所示，相比 Stable Cascade 与 Diffusion-DPO，本文方法与用户画像的吻合更紧密，能捕捉到高亮标注的那类用户细节。Stable Cascade 与改进提示词的 Diffusion-DPO 虽能捕捉用户描述的某些方面，却常常过拟合于用户画像，导致生成图像忽略了原本的图像提示。

**EN** Personalized Preference Alignment Evaluation

**ZH** 个性化偏好对齐评测

**EN** We evaluate whether the generated model aligns with specific user preference using a VLM as a judge, leveraging strong VLMs such as GPT4o-vision [26], similar to recipes in prior work [19, 4]. In particular, we condition the VLM on few-shot examples from the user as well as a pair of images for a given test time caption and ask the model to judge which of the two images would be preferred by the user. To ensure consistency of the response the model selects, we judge each pair of images twice using the VLM, flipping the ordering of the images, filtering out pairs where the VLM is inconsistent. With this paradigm and ⟦SLOT_100⟧ shots per user, we find that the VLM is able to match the ground truth personalized human preference with ⟦SLOT_101⟧ accuracy.

**ZH** 我们用一个视觉语言模型充当裁判，评估生成模型是否契合特定用户偏好，采用的是 GPT4o-vision [26] 等强视觉语言模型，做法类似已有工作 [19, 4]。具体地，我们把该用户的少样本示例，以及针对测试时提示生成的一对图像一并作为视觉语言模型的条件，让它判断用户会更偏好两者中的哪一张。为保证模型选择的一致性，我们用视觉语言模型对每对图像判断两次（交换图像顺序），并剔除两次判断不一致的样本。在该范式下，每位用户取 ⟦SLOT_100⟧ 个示例，视觉语言模型对真实个性化人类偏好的判断准确率达到 ⟦SLOT_101⟧。

**EN** We decompose our evaluation into two settings: (1) evaluating users that were seen during training but on captions that were held out and (2) evaluating held-out users and captions. We aggregate over these settings to also compute metrics for the general user in the dataset. For the 4341 users in Pick-a-Pic we select 192 held out and 277 in-distribution users. For each of these users, we choose ⟦SLOT_102⟧ examples, where 4 examples are used for the in-context conditioning for the user and 1 example is used as the caption for evaluation. We compute an automatic win-rate using pairs of models, generating one image for each caption and evaluating with the VLM-as-Judge pipeline outlined above.

**ZH** 评测分两种设定：（1）评估训练时见过、但提示被留出的用户；（2）评估用户与提示都被留出的情况。我们还把两种设定汇总，计算数据集中一般用户的指标。在 Pick-a-Pic 的 4341 位用户中，我们选取 192 位留出用户与 277 位分布内用户。对每位用户取 ⟦SLOT_102⟧ 条示例，其中 4 条用于用户的上下文条件化，1 条作为评测用的提示。我们用模型两两配对计算自动胜率：为每条提示各生成一张图像，再按上述 VLM 裁判流程评测。

<!-- [原子块 · object]  -->

**EN** Figure 6: Automatic Win Rate Evaluation with GPT-4o We evaluate on seen users, held out users, and aggregate to see win-rates for generic users, comparing Stable Cascade and PPD.

**ZH** 图 6：基于 GPT-4o 的自动胜率评测。我们在已见用户、留出用户上评测，并汇总得到一般用户的胜率，对比 Stable Cascade 与 PPD。

**EN** We report win rate comparisons in Fig. 6. Here, PPD significantly outperforms Stable Cascade in all three evaluation settings, achieving a win rate of 83% on seen users, and 78% on unseen users, aggregated to 81% on all users.

**ZH** 图 6 报告了胜率对比。PPD 在三种评测设定下均显著优于 Stable Cascade：已见用户胜率 83%，未见用户 78%，全体用户汇总为 81%。

**EN** 6 Discussion, Conclusion, and Limitations

**ZH** 6 讨论、结论与局限

**EN** This work presents a framework for personalization in text-to-image diffusion models using user feature embeddings derived from a VLM. By conditioning on these embeddings through decoupled cross-attention layers and fine-tuning with the DPO objective, our method achieves both accurate reward modeling and high-quality personalized image generation. This approach allows us to generalize effectively to unseen users, requiring only few-shot preference examples from new users at test time.

**ZH** 本文提出一个文生图扩散模型个性化框架，其用户特征嵌入由视觉语言模型导出。通过解耦交叉注意力层以这些嵌入为条件、并用 DPO 目标微调，本文方法同时实现了准确的奖励建模与高质量的个性化图像生成。该方法能有效泛化到未见用户，测试时只需新用户提供少量偏好示例。

**EN** However, several open questions and limitations remain. Currently, our conditioning on few-shot examples is caption agnostic, as it selects a set of random preferences from a user. Future work could investigate methods for actively selecting the preferences that the VLM embeds, potentially enhancing personalization. Additionally, extending this technique to video generation could enable effective personalized video content, which is an exciting direction for further research. Finally, exploring the trade-offs between implicit and stated preferences may provide insights into optimizing user experience and model performance.

**ZH** 不过仍存在若干开放问题与局限。目前我们对少样本示例的条件化与提示无关，只是从用户数据中随机选取一组偏好；未来可研究如何主动选择供视觉语言模型嵌入的偏好，有望进一步增强个性化。此外，把该技术扩展到视频生成，有望实现有效的个性化视频内容，是一个令人期待的方向。最后，探究隐式偏好与陈述偏好之间的权衡，或能为优化用户体验与模型性能带来启发。

**EN** Acknowledgment

**ZH** 致谢

**EN** This research is done during MD’s internship at Luma AI and supported in part by ARO (W911NF-21-1-0125), ONR (N00014-23-1-2159), and the CZ Biohub. AS gratefully acknowledges the support of the NSF Graduate Research Fellowship Program.

**ZH** 本研究在 MD 于 Luma AI 实习期间完成，并得到 ARO（W911NF-21-1-0125）、ONR（N00014-23-1-2159）与 CZ Biohub 的部分支持。AS 感谢 NSF 研究生研究奖学金计划的支持。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] [1] Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort, Deep Ganguli, Tom Henighan, Nicholas Joseph, Saurav Kadavath, Jackson Kernion, Tom Coner -->

<!-- [原子块 · verbatim] [2] Kevin Black, Michael Janner, Yilun Du, Ilya Kostrikov, and Sergey Levine. Training diffusion models with reinforcement learning. In The Twelfth International Conference on Learning Representations -->

<!-- [原子块 · verbatim] [3] Ralph Allan Bradley and Milton E Terry. Rank analysis of incomplete block designs: I. the method of paired comparisons. Biometrika , 39(3/4):324–345, 1952. -->

<!-- [原子块 · verbatim] [4] Zhaorun Chen, Yichao Du, Zichen Wen, Yiyang Zhou, Chenhang Cui, Zhenzhen Weng, Haoqin Tu, Chaoqi Wang, Zhengwei Tong, Qinglan Huang, Canyu Chen, Qinghao Ye, Zhihong Zhu, Yuqing Zhang, Jiawei Zhou, -->

<!-- [原子块 · verbatim] [5] Kevin Clark, Paul Vicol, Kevin Swersky, and David J Fleet. Directly fine-tuning diffusion models on differentiable rewards. arXiv preprint arXiv:2309.17400 , 2023. -->

<!-- [原子块 · verbatim] [6] Xiaoliang Dai, Ji Hou, Chih-Yao Ma, Sam Tsai, Jialiang Wang, Rui Wang, Peizhao Zhang, Simon Vandenhende, Xiaofang Wang, Abhimanyu Dubey, et al. Emu: Enhancing image generation models using photoge -->

<!-- [原子块 · verbatim] [7] Patrick Esser, Sumith Kulal, Andreas Blattmann, Rahim Entezari, Jonas Müller, Harry Saini, Yam Levi, Dominik Lorenz, Axel Sauer, Frederic Boesel, et al. Scaling rectified flow transformers for hig -->

<!-- [原子块 · verbatim] [8] Kawin Ethayarajh, Winnie Xu, Niklas Muennighoff, Dan Jurafsky, and Douwe Kiela. Kto: Model alignment as prospect theoretic optimization. arXiv preprint arXiv:2402.01306 , 2024. -->

<!-- [原子块 · verbatim] [9] Ying Fan, Olivia Watkins, Yuqing Du, Hao Liu, Moonkyung Ryu, Craig Boutilier, Pieter Abbeel, Mohammad Ghavamzadeh, Kangwook Lee, and Kimin Lee. Reinforcement learning for fine-tuning text-to-image -->

<!-- [原子块 · verbatim] [10] Shangbin Feng, Taylor Sorensen, Yuhan Liu, Jillian Fisher, Chan Young Park, Yejin Choi, and Yulia Tsvetkov. Modular Pluralism: Pluralistic Alignment via Multi-LLM Collaboration. arXiv e-prints ,  -->

<!-- [原子块 · verbatim] [11] Gabriel Goh, James Betker, Li Jing, Aditya Ramesh, Tim Brooks, Jianfeng Wang, Lindsey Li, Long Ouyang, Juntang Zhuang, Joyce Lee, Prafulla Dhariwal, Casey Chu, Joy Jiao, Jong Wook Kim, Alex Nicho -->

<!-- [原子块 · verbatim] [12] Jonathan Ho, Ajay Jain, and Pieter Abbeel. Denoising diffusion probabilistic models. In Advances in neural information processing systems , pages 6840–6851, 2020. -->

<!-- [原子块 · verbatim] [13] Gabriel Ilharco, Mitchell Wortsman, Ross Wightman, Cade Gordon, Nicholas Carlini, Rohan Taori, Achal Dave, Vaishaal Shankar, Hongseok Namkoong, John Miller, Hannaneh Hajishirzi, Ali Farhadi, and  -->

<!-- [原子块 · verbatim] [14] Diederik P. Kingma, Tim Salimans, Ben Poole, and Jonathan Ho. Variational diffusion models. In Advances in Neural Information Processing Systems 34 , 2021. -->

<!-- [原子块 · verbatim] [15] Hannah Rose Kirk, Alexander Whitefield, Paul Röttger, Andrew Bean, Katerina Margatina, Juan Ciro, Rafael Mosquera, Max Bartolo, Adina Williams, He He, Bertie Vidgen, and Scott A. Hale. The PRISM  -->

<!-- [原子块 · verbatim] [16] Yuval Kirstain, Adam Polyak, Uriel Singer, Shahbuland Matiana, Joe Penna, and Omer Levy. Pick-a-pic: An open dataset of user preferences for text-to-image generation. arXiv preprint arXiv:2305.01 -->

<!-- [原子块 · verbatim] [17] Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yutaka Matsuo, and Yusuke Iwasawa. Large language models are zero-shot reasoners, 2023. -->

<!-- [原子块 · verbatim] [18] Kimin Lee, Hao Liu, Moonkyung Ryu, Olivia Watkins, Yuqing Du, Craig Boutilier, Pieter Abbeel, Mohammad Ghavamzadeh, and Shixiang Shane Gu. Aligning text-to-image models using human feedback. arXi -->

<!-- [原子块 · verbatim] [19] Seongyun Lee, Seungone Kim, Sue Hyun Park, Geewook Kim, and Minjoon Seo. Prometheus-Vision: Vision-Language Model as a Judge for Fine-Grained Evaluation. arXiv e-prints , art. arXiv:2401.06591, 2 -->

<!-- [原子块 · verbatim] [20] Bo Li, Yuanhan Zhang, Dong Guo, Renrui Zhang, Feng Li, Hao Zhang, Kaichen Zhang, Yanwei Li, Ziwei Liu, and Chunyuan Li. Llava-onevision: Easy visual task transfer. arXiv preprint arXiv:2408.03326 -->

<!-- [原子块 · verbatim] [21] Bo Li, Yuanhan Zhang, Dong Guo, Renrui Zhang, Feng Li, Hao Zhang, Kaichen Zhang, Peiyuan Zhang, Yanwei Li, Ziwei Liu, and Chunyuan Li. LLaVA-OneVision: Easy Visual Task Transfer. arXiv e-prints , -->

<!-- [原子块 · verbatim] [22] Shufan Li, Konstantinos Kallidromitis, Akash Gokul, Yusuke Kato, and Kazuki Kozuka. Aligning diffusion models by optimizing human utility. arXiv preprint arXiv:2404.04465 , 2024a. -->

<!-- [原子块 · verbatim] [23] Xinyu Li, Zachary C Lipton, and Liu Leqi. Personalized language modeling from personalized human feedback. arXiv preprint arXiv:2402.05133 , 2024b. -->

<!-- [原子块 · verbatim] [24] Ilya Loshchilov and Frank Hutter. Decoupled weight decay regularization. arXiv preprint arXiv:1711.05101 , 2017. -->

<!-- [原子块 · verbatim] [25] Chong Mou, Xintao Wang, Liangbin Xie, Yanze Wu, Jian Zhang, Zhongang Qi, and Ying Shan. T2i-adapter: Learning adapters to dig out more controllable ability for text-to-image diffusion models. In  -->

<!-- [原子块 · verbatim] [26] OpenAI. Gpt-4 technical report. ArXiv , abs/2303.08774, 2023. -->

<!-- [原子块 · verbatim] [27] Pablo Pernias, Dominic Rampas, Mats Leon Richter, Christopher Pal, and Marc Aubreville. Würstchen: An efficient architecture for large-scale text-to-image diffusion models. In The Twelfth Interna -->

<!-- [原子块 · verbatim] [28] Sriyash Poddar, Yanming Wan, Hamish Ivison, Abhishek Gupta, and Natasha Jaques. Personalizing reinforcement learning from human feedback with variational preference learning. arXiv preprint arXiv -->

<!-- [原子块 · verbatim] [29] Dustin Podell, Zion English, Kyle Lacey, Andreas Blattmann, Tim Dockhorn, Jonas Müller, Joe Penna, and Robin Rombach. SDXL: Improving latent diffusion models for high-resolution image synthesis.  -->

<!-- [原子块 · verbatim] [30] Mihir Prabhudesai, Anirudh Goyal, Deepak Pathak, and Katerina Fragkiadaki. Aligning text-to-image diffusion models with reward backpropagation. arXiv preprint arXiv:2310.03739 , 2023. -->

<!-- [原子块 · verbatim] [31] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, et al. Learning transferable visual models from -->

<!-- [原子块 · verbatim] [32] Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and Chelsea Finn. Direct preference optimization: Your language model is secretly a reward model. In Advances  -->

<!-- [原子块 · verbatim] [33] Aditya Ramesh, Prafulla Dhariwal, Alex Nichol, Casey Chu, and Mark Chen. Hierarchical text-conditional image generation with clip latents. arXiv preprint arXiv:2204.06125 , 2022. -->

<!-- [原子块 · verbatim] [34] Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, and Björn Ommer. High-resolution image synthesis with latent diffusion models. In Proceedings of the IEEE/CVF conference on comput -->

<!-- [原子块 · verbatim] [35] Chitwan Saharia, William Chan, Saurabh Saxena, Lala Li, Jay Whang, Emily L Denton, Kamyar Ghasemipour, Raphael Gontijo Lopes, Burcu Karagol Ayan, Tim Salimans, Jonathan Ho, David J Fleet, and Moh -->

<!-- [原子块 · verbatim] [36] Shibani Santurkar, Esin Durmus, Faisal Ladhak, Cinoo Lee, Percy Liang, and Tatsunori Hashimoto. Whose Opinions Do Language Models Reflect? arXiv e-prints , art. arXiv:2303.17548, 2023. -->

<!-- [原子块 · verbatim] [37] Christoph Schuhmann. CLIP MLP aesthetic score predictor. https://github.com/christophschuhmann/improved-aesthetic-predictor , 2022. Accessed: 2024-11-06. -->

<!-- [原子块 · verbatim] [38] Christoph Schuhmann, Romain Beaumont, Richard Vencu, Cade Gordon, Ross Wightman, Mehdi Cherti, Theo Coombes, Aarush Katta, Clayton Mullis, Mitchell Wortsman, et al. LAION-5b: An open large-scale  -->

<!-- [原子块 · verbatim] [39] Eyal Segalis, Dani Valevski, Danny Lumen, Yossi Matias, and Yaniv Leviathan. A picture is worth a thousand words: Principled recaptioning improves image generation. arXiv preprint arXiv:2310.1665 -->

<!-- [原子块 · verbatim] [40] Jascha Sohl-Dickstein, Eric Weiss, Niru Maheswaranathan, and Surya Ganguli. Deep unsupervised learning using nonequilibrium thermodynamics. In International conference on machine learning , pages -->

<!-- [原子块 · verbatim] [41] Jiaming Song, Chenlin Meng, and Stefano Ermon. Denoising diffusion implicit models. In International Conference on Learning Representations , 2021a. -->

<!-- [原子块 · verbatim] [42] Yang Song and Stefano Ermon. Generative modeling by estimating gradients of the data distribution. Advances in neural information processing systems , 32, 2019. -->

<!-- [原子块 · verbatim] [43] Yang Song, Jascha Sohl-Dickstein, Diederik P Kingma, Abhishek Kumar, Stefano Ermon, and Ben Poole. Score-based generative modeling through stochastic differential equations. In International Conf -->

<!-- [原子块 · verbatim] [44] Taylor Sorensen, Jared Moore, Jillian Fisher, Mitchell Gordon, Niloofar Mireshghallah, Christopher Michael Rytting, Andre Ye, Liwei Jiang, Ximing Lu, Nouha Dziri, Tim Althoff, and Yejin Choi. A R -->

<!-- [原子块 · verbatim] [45] Bram Wallace, Meihua Dang, Rafael Rafailov, Linqi Zhou, Aaron Lou, Senthil Purushwalkam, Stefano Ermon, Caiming Xiong, Shafiq Joty, and Nikhil Naik. Diffusion model alignment using direct prefere -->

<!-- [原子块 · verbatim] [46] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc Le, and Denny Zhou. Chain-of-thought prompting elicits reasoning in large language models, 2023. -->

<!-- [原子块 · verbatim] [47] Xiaoshi Wu, Yiming Hao, Keqiang Sun, Yixiong Chen, Feng Zhu, Rui Zhao, and Hongsheng Li. Human preference score v2: A solid benchmark for evaluating human preferences of text-to-image synthesis.  -->

<!-- [原子块 · verbatim] [48] Xiaoshi Wu, Keqiang Sun, Feng Zhu, Rui Zhao, and Hongsheng Li. Human preference score: Better aligning text-to-image models with human preference. In Proceedings of the IEEE/CVF International Con -->

<!-- [原子块 · verbatim] [49] Jiazheng Xu, Xiao Liu, Yuchen Wu, Yuxuan Tong, Qinkai Li, Ming Ding, Jie Tang, and Yuxiao Dong. Imagereward: Learning and evaluating human preferences for text-to-image generation. In Advances in -->

<!-- [原子块 · verbatim] [50] Kai Yang, Jian Tao, Jiafei Lyu, Chunjiang Ge, Jiaxin Chen, Weihan Shen, Xiaolong Zhu, and Xiu Li. Using human feedback to fine-tune diffusion models without any reward model. In Proceedings of th -->

<!-- [原子块 · verbatim] [51] Hu Ye, Jun Zhang, Sibo Liu, Xiao Han, and Wei Yang. Ip-adapter: Text compatible image prompt adapter for text-to-image diffusion models. arXiv preprint arxiv:2308.06721 , 2023. -->

<!-- [原子块 · verbatim] [52] Chao Yu, Hong Lu, Jiaxuan Gao, Qixin Tan, Xinting Yang, Yu Wang, Yi Wu, and Eugene Vinitsky. Few-shot in-context preference learning using large language models. arXiv preprint arXiv:2410.17233 , -->

<!-- [原子块 · verbatim] [53] Jiahui Yu, Yuanzhong Xu, Jing Yu Koh, Thang Luong, Gunjan Baid, Zirui Wang, Vijay Vasudevan, Alexander Ku, Yinfei Yang, Burcu Karagol Ayan, Ben Hutchinson, Wei Han, Zarana Parekh, Xin Li, Han Zha -->

<!-- [原子块 · verbatim] [54] Lvmin Zhang, Anyi Rao, and Maneesh Agrawala. Adding conditional control to text-to-image diffusion models. In Proceedings of the IEEE/CVF International Conference on Computer Vision , pages 3836– -->

<!-- [原子块 · verbatim] [55] Yinan Zhang, Eric Tzeng, Yilun Du, and Dmitry Kislyuk. Large-scale reinforcement learning for diffusion models. arXiv preprint arXiv:2401.12244 , 4, 2024. -->

<!-- [原子块 · verbatim] [56] Rui Zheng, Shihan Dou, Songyang Gao, Yuan Hua, Wei Shen, Binghai Wang, Yan Liu, Senjie Jin, Qin Liu, Yuhao Zhou, Limao Xiong, Lu Chen, Zhiheng Xi, Nuo Xu, Wenbin Lai, Minghao Zhu, Cheng Chang, Zh -->

**EN** Supplementary Material

**ZH** 补充材料

**EN** Appendix A Direct Preference Optimization on Diffusion Models

**ZH** 附录 A 扩散模型上的直接偏好优化

**EN** Given dataset containing examples ⟦SLOT_103⟧, we define ⟦SLOT_104⟧ as the reward on image ⟦SLOT_105⟧ given prompt ⟦SLOT_106⟧. We would like to fine-tune a text-to-image models ⟦SLOT_107⟧ such that reward is maximized while keeping close to a reference model ⟦SLOT_108⟧ in terms of KL-divergence as regularization :

**ZH** 给定包含样本 ⟦SLOT_103⟧ 的数据集，我们把 ⟦SLOT_104⟧ 定义为图像 ⟦SLOT_105⟧ 的奖励，其中提示为 ⟦SLOT_106⟧。我们希望微调文生图模型 ⟦SLOT_107⟧，使奖励最大化的同时以 KL 散度为正则项、保持与参考模型 ⟦SLOT_108⟧ 接近：

<!-- [原子块 · table] max p θ 𝔼 𝐜 , 𝐱 0 [ r ( 𝐜 , 𝐱 0 ) ] − β 𝔻 KL [ p θ ( 𝐱 0 | 𝐜 ) ∥ p ref ( 𝐱 0 | 𝐜 ) ] , \max_{p_{\theta}}\mathbb{E}_{{\mathbf{c}},{\mathbf{x}}_{0}}\left[r({\mathbf{c}},{\mathbf{x}}_{0})\right]-\beta\ma -->

**EN** where ⟦SLOT_109⟧ is a parameter controlling how much ⟦SLOT_110⟧ deviates from ⟦SLOT_111⟧.

**ZH** 其中 ⟦SLOT_109⟧ 是控制 ⟦SLOT_110⟧ 偏离 ⟦SLOT_111⟧ 幅度的参数。

**EN** We introduce latent variables ⟦SLOT_112⟧ and define ⟦SLOT_113⟧ as the reward on the whole diffusion chain, such that we can define ⟦SLOT_114⟧. Given Eq. 8, we have

**ZH** 我们引入潜变量 ⟦SLOT_112⟧，并把 ⟦SLOT_113⟧ 定义为整条扩散链上的奖励，从而可以定义 ⟦SLOT_114⟧。由式 8 可得

<!-- [原子块 · table] min p θ − 𝔼 p θ ​ ( 𝐱 0 | 𝐜 ) [ r ( 𝐜 , 𝐱 0 ) / β ] + 𝔻 KL [ p θ ( 𝐱 0 | 𝐜 ) | | p ref ( 𝐱 0 | 𝐜 ) ] ≤ min p θ − 𝔼 p θ ​ ( 𝐱 0 | 𝐜 ) [ r ( 𝐜 , 𝐱 0 ) / β ] + 𝔻 KL [ p θ ( 𝐱 0 : T | 𝐜 ) | | p ref ( 𝐱 0  -->

**EN** where ⟦SLOT_115⟧ is the partition function. The optimal ⟦SLOT_116⟧ of Equation (9) has a unique closed-form solution:

**ZH** 其中 ⟦SLOT_115⟧ 为配分函数。式 (9) 的最优 ⟦SLOT_116⟧ 有唯一的闭式解：

<!-- [原子块 · table] p θ ∗ ( 𝐱 0 : T | 𝐜 ) = p ref ( 𝐱 0 : T | 𝐜 ) exp ( R ( 𝐜 , 𝐱 0 : T ) / β ) / Z ( 𝐜 ) , \displaystyle p_{\theta}^{*}({\mathbf{x}}_{0:T}|{\mathbf{c}})=p_{\text{ref}}({\mathbf{x}}_{0:T}|{\mathbf{c}})\ex -->

**EN** Therefore, we have the reparameterization of reward function

**ZH** 于是得到奖励函数的重参数化形式

<!-- [原子块 · table] R ( 𝐜 , 𝐱 0 : T ) \displaystyle R({\mathbf{c}},{\mathbf{x}}_{0:T}) = β log p θ ∗ ( 𝐱 0 : T | 𝐜 ) p ref ( 𝐱 0 : T | 𝐜 ) + β log Z ( 𝐜 ) . \displaystyle=\beta\log\frac{p_{\theta}^{*}({\mathbf{x}}_{0:T}| -->

**EN** Plug this into the definition of ⟦SLOT_117⟧, hence we have

**ZH** 将其代入 ⟦SLOT_117⟧ 的定义，可得

<!-- [原子块 · table] r ( 𝐜 , 𝐱 0 ) = β 𝔼 p θ ( 𝐱 1 : T | 𝐱 0 , 𝐜 ) [ log p ∗ θ ( 𝐱 0 : T | 𝐜 ) p ref ( 𝐱 0 : T | 𝐜 ) ] + β log Z ( 𝐜 ) . r({\mathbf{c}},{\mathbf{x}}_{0})=\beta\mathbb{E}_{p_{\theta}({\mathbf{x}}_{1:T}|{\ma -->

**EN** Substituting this reward reparameterization into maximum likelihood objective of the Bradly-Terry model, the partition function cancels for image pairs, and we get a maximum likelihood objective defined on diffusion models, for a single pair ⟦SLOT_118⟧:

**ZH** 把这一奖励重参数化代入 Bradley-Terry 模型的极大似然目标，配分函数在图像对上相互抵消，由此得到定义在扩散模型上、针对单个样本对 ⟦SLOT_118⟧ 的极大似然目标：

<!-- [原子块 · table] L Diffusion-DPO ( θ ) = − log σ ( β 𝔼 𝐱 + 1 : T , 𝐱 − 1 : T [ log p θ ( 𝐱 + 0 : T | 𝐜 ) p ref ( 𝐱 + 0 : T | 𝐜 ) − log p θ ( 𝐱 − 0 : T | 𝐜 ) p ref ( 𝐱 − 0 : T | 𝐜 ) ] ) L_{\text{Diffusion-DPO }}(\theta -->

**EN** where ⟦SLOT_119⟧ and ⟦SLOT_120⟧. Since sampling from ⟦SLOT_121⟧ is intractable, we utilize the forward process ⟦SLOT_122⟧ for approximation.

**ZH** 其中 ⟦SLOT_119⟧ 与 ⟦SLOT_120⟧。由于从 ⟦SLOT_121⟧ 采样难以处理，我们改用前向过程 ⟦SLOT_122⟧ 近似。

<!-- [原子块 · table] L approx ​ ( θ ) = − log σ ( β 𝔼 𝐱 + 1 : T , 𝐱 − 1 : T [ log p θ ( 𝐱 + 0 : T ) p ref ( 𝐱 + 0 : T ) − log p θ ( 𝐱 − 0 : T ) p ref ( 𝐱 − 0 : T ) ] ) \displaystyle\begin{split}L_{\text{approx}}(\theta)&= -->

**EN** where ⟦SLOT_123⟧. Therefore,

**ZH** 其中 ⟦SLOT_123⟧。因此，

<!-- [原子块 · table] L approx ​ ( θ ) = − log σ ( β 𝔼 𝐱 + 1 : T , 𝐱 − 1 : T [ ∑ t = 1 T log p θ ​ ( 𝐱 t − 1 + | 𝐱 t + ) p ref ​ ( 𝐱 t − 1 + | 𝐱 t + ) − log p θ ​ ( 𝐱 t − 1 − | 𝐱 t − ) p ref ​ ( 𝐱 t − 1 − | 𝐱 t ) ] ) = − l -->

**EN** where ⟦SLOT_124⟧ and ⟦SLOT_125⟧. Since function ⟦SLOT_126⟧ is a convex function, by Jensen’s inequality, we can push ⟦SLOT_127⟧ to the outside of ⟦SLOT_128⟧ and get an upper bound, therefore we have

**ZH** 其中 ⟦SLOT_124⟧ 与 ⟦SLOT_125⟧。由于函数 ⟦SLOT_126⟧ 是凸函数，由 Jensen 不等式可把 ⟦SLOT_127⟧ 移到 ⟦SLOT_128⟧ 之外从而得到上界，于是有

<!-- [原子块 · table] L approx ​ ( θ ) ≤ \displaystyle L_{\text{approx}}(\theta)\leq − 𝔼 t , 𝐱 t + , 𝐱 t − ​ log ⁡ σ ⁡ ( β ​ T ​ 𝔼 𝐱 t − 1 + , 𝐱 t − 1 − ​ [ log ⁡ p θ ​ ( 𝐱 t − 1 + | 𝐱 t + ) p ref ​ ( 𝐱 t − 1 + | 𝐱 t + ) − -->

**EN** Using the Gaussian parameterization of the reverse process (Eq. 1), the above loss simplifies to:

**ZH** 利用逆向过程的高斯参数化形式（式 1），上述损失可化简为：

<!-- [原子块 · table] L approx ​ ( θ ) = − 𝔼 𝐜 , 𝐱 0 + , 𝐱 0 − ​ log ⁡ σ ⁡ ( − β ​ T ​ ω ​ ( λ t ) CLOSE \displaystyle L_{\text{approx}}(\theta)=-\mathbb{E}_{{\mathbf{c}},{\mathbf{x}}^{+}_{0},{\mathbf{x}}^{-}_{0}}\log\sigm -->

**EN** where ⟦SLOT_129⟧, ⟦SLOT_130⟧, ⟦SLOT_131⟧, ⟦SLOT_132⟧ is a signal-to-noise ratio term.

**ZH** 其中 ⟦SLOT_129⟧、⟦SLOT_130⟧、⟦SLOT_131⟧、⟦SLOT_132⟧ 为信噪比项。

**EN** Appendix B Experiments Details

**ZH** 附录 B 实验细节

**EN** B.1 Diffusion Model Fine-tuning Details

**ZH** B.1 扩散模型微调细节

**EN** For the experiments shown in Sec. 5.1, we optimize only the added cross-attention layers, with 150M trainable parameters in total. All models are trained using the AdamW optimizer with an effective batch size of 768 pairs, a learning rate of ⟦SLOT_133⟧, and a single training epoch. The hyperparameter ⟦SLOT_134⟧ is tuned within the range ⟦SLOT_135⟧. Training is conducted on the Pick-a-Pic training set, with the best ⟦SLOT_136⟧ selected based on the averaged rewards of generated samples evaluated on the Pick-a-Pic validation set, which contains 500 unique captions. Results are reported on the Partipromt dataset containing 1632 captions. For each method (each row in Tab. 1), ⟦SLOT_137⟧ is tuned independently. Experiments are conducted on H100 GPUs with 80GB of memory. Using 8 GPUs, each with a local batch size of 16, training for one epoch (approximately 1000 gradient update steps) takes about 2 hours.

**ZH** 在第 5.1 节的实验中，我们只优化新增的交叉注意力层，可训练参数共 150M。所有模型均使用 AdamW 优化器，有效批大小为 768 对，学习率 ⟦SLOT_133⟧，训练一个轮次。超参数 ⟦SLOT_134⟧ 在 ⟦SLOT_135⟧ 范围内调优。训练在 Pick-a-Pic 训练集上进行，最优 ⟦SLOT_136⟧ 依据生成样本在 Pick-a-Pic 验证集（含 500 条唯一提示）上的平均奖励选定。结果在含 1632 条提示的 Partipromt 数据集上报告。对于每种方法（表 1 的每一行），⟦SLOT_137⟧ 都独立调优。实验在显存 80GB 的 H100 GPU 上进行；使用 8 张 GPU、单卡本地批大小 16 时，训练一个轮次（约 1000 次梯度更新）约需 2 小时。

**EN** For the personalized real user experiments shown in Sec. 5.2, we use the same training settings as in Sec. 5.1 except for a reduced learning rate of ⟦SLOT_138⟧. We train on Pick-a-Pic training set, find the best hyper-parameter on Pick-a-Pic validation set and report results on Partiprompt dataset. As there are no automatic evaluation metrics to evaluate alignment with individualized user preferences, we find the best ⟦SLOT_139⟧ based on the highest PickScore on the Pick-a-Pic validation set. We then run Diffusion-DPO with the same ⟦SLOT_140⟧ as baseline.

**ZH** 在第 5.2 节的真实用户个性化实验中，除学习率降低为 ⟦SLOT_138⟧ 外，训练设置与第 5.1 节相同。我们在 Pick-a-Pic 训练集上训练，在 Pick-a-Pic 验证集上确定最优超参数，并在 Partiprompt 数据集上报告结果。由于缺乏衡量与个体用户偏好对齐程度的自动评测指标，我们以验证集上最高的 PickScore 为依据确定最优 ⟦SLOT_139⟧，随后用相同 ⟦SLOT_140⟧ 运行 Diffusion-DPO 作为基线。

**EN** B.2 Additional Details for Generating User Embeddings

**ZH** B.2 生成用户嵌入的补充细节

**EN** As mentioned in Sec. 4.2, features from pre-trained VLM, LLaVA-OneVision [20], are constructed from ⟦SLOT_141⟧ few-shot examples. To elicit these features, we employ Zero-Shot Chain of Thought Prompting (COT) [17, 46] to allow the model to reason about the images in a preference pair as well as generate a user profile. The prompt used for this COT can be found in Tab. 2. We then extract an embedding from the VLM from the last hidden state of the Qwen 2 Language Model in the LLaVA OneVision architecture for the final token it generates for the User Profile (Step 5 in the COT Assistant Prompt in Tab. 2). For sampling, we use a temperature of 0.7 with nucleus sampling probability of 1.0 (no nucleus sampling). As seen in Fig. 2, the top-k accuracy of a learned classifier from this frozen embedding is high, significantly outperforming random chance, indicating that this embedding is expressive, able to distinguish users within the pick-a-pick dataset. We additionally store the generated user profile for the baselines where the user profile is appended to the caption as an augmentation for the fairest comparison.

**ZH** 如第 4.2 节所述，预训练视觉语言模型 LLaVA-OneVision [20] 的特征由 ⟦SLOT_141⟧ 个少样本示例构建。为引出这些特征，我们采用零样本思维链提示（COT）[17, 46]，让模型对偏好对中的图像进行推理并生成用户画像，所用的思维链提示见表 2。随后，我们从 LLaVA OneVision 架构中 Qwen 2 语言模型的最后一层隐藏状态提取嵌入，取的是模型为用户画像生成的最后一个词元（表 2 中 COT 助手提示的第 5 步）。采样时温度为 0.7，核采样概率为 1.0（即不启用核采样）。如图 2 所示，基于该冻结嵌入学到的分类器 top-k 准确率很高，远超随机水平，说明该嵌入表达力充足，能够区分 Pick-a-Pic 数据集中的不同用户。我们还额外保存了生成的用户画像，供那些把用户画像拼接到提示上作为增强的基线方法使用，以保证比较的公平性。

**EN** B.3 Additional Details for Scoring

**ZH** B.3 评分的补充细节

**EN** We similarly employ COT for scoring. We add an additional assistant prompt for User Preference Prediction as found in Tab. 2. Here, we employ a stronger VLM as a Judge, GPT 4o-mini. For consistency, we present each pair of images twice to the model. In particular, for two images A and B, we ask the VLM to judge the images in two different permutations: first A then B and first B then A. We omit comparisons where the model isn’t consistent in scoring (i.e A chosen for both comparisons or B chosen for both comparisons). For sampling, we utilize a temperature of 1.0 and nucleus sampling probability of 1.0 (no nucleus sampling). With COT and consistency, we find that we can match the preferences from real users in the Pick-a-Pic v2 dataset [16] with 83% accuracy.

**ZH** 评分环节同样采用思维链。我们额外加入一段用于用户偏好预测的助手提示，见表 2。此处使用更强的视觉语言模型 GPT 4o-mini 作为裁判。为保证一致性，我们把每对图像向模型呈现两次：对图像 A 与 B，分别以「先 A 后 B」和「先 B 后 A」两种顺序让视觉语言模型评判，并剔除模型两次评判不一致的样本（即两次都选 A 或两次都选 B）。采样时温度为 1.0，核采样概率为 1.0（不启用核采样）。借助思维链与一致性筛选，我们对 Pick-a-Pic v2 数据集 [16] 中真实用户偏好的判断准确率达到 83%。

**EN** B.4 Additional Details for Evaluation and Dataset Construction

**ZH** B.4 评测与数据集构建的补充细节

**EN** Due to the restriction of fewshot prompting, we require at least ⟦SLOT_142⟧ examples per user. Therefore, we drop users in the Pick-a-Pic v2 dataset where the number of preference pairs that the user labels are below ⟦SLOT_143⟧. For classification, we subsample 300 users with the most preference pairs to allow for more examples in classification.

**ZH** 受少样本提示长度的限制，我们要求每位用户至少有 ⟦SLOT_142⟧ 条示例，因此剔除了 Pick-a-Pic v2 数据集中标注偏好对数量少于 ⟦SLOT_143⟧ 的用户。在分类实验中，我们抽取偏好对最多的 300 位用户，以便在分类时提供更多示例。

<!-- [原子块 · table] System Prompt You are an expert in image aesthetics and have been asked to predict which image a user would prefer based on the examples provided. COT Assistant Prompt You will be shown a few examples -->

**EN** Table 2: Instructions for Embedding Generation and User Preference Prediction

**ZH** 表 2：嵌入生成与用户偏好预测的指令

**EN** Appendix C More Qualitative Examples

**ZH** 附录 C 更多定性示例

**EN** Similar to Fig. 4, the following figures show that PPD is able to interpolate among three distinct rewards during inference.

**ZH** 与图 4 类似，下面几组图展示了 PPD 能在推理时对三个不同奖励做插值。

<!-- [原子块 · table] a cream-colored labradoodle wearing glasses and black beret teaching calculus at a blackboard -->

**EN** Figure 7:

**ZH** 图 7：

<!-- [原子块 · table] a black baseball hat with a flame decal on it -->

**EN** Figure 8:

**ZH** 图 8：

<!-- [原子块 · table] trees seen through a car window on a rainy day -->

**EN** Figure 9:

**ZH** 图 9：
