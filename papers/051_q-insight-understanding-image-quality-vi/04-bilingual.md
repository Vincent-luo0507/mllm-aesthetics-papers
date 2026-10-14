# Q-Insight：通过视觉强化学习理解图像质量

> 原标题：Q-Insight: Understanding Image Quality via Visual Reinforcement Learning
> 作者：Weiqi Li, Xuanyu Zhang, Shijie Zhao, Yabin Zhang, Junlin Li, Li Zhang, Jian Zhang · arXiv:2503.22679 · 2025-03-28

<!-- [原子块 · verbatim] Q-Insight: Understanding Image Quality via Visual Reinforcement Learning -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] Image quality assessment (IQA) focuses on the perceptual visual quality of images, playing a crucial role in downstream tasks such as image reconstruction, compression, and generation. The rapid advan -->

**EN** 1 Introduction

**ZH** 1 引言

**EN** Image quality assessment (IQA) is a fundamental task in computer vision, critical for optimizing algorithms, enhancing user experiences, and verifying content authenticity across diverse domains, such as image processing [41, 22, 11, 53] and AI-generated content (AIGC) [37, 8]. Traditional IQA methods rely heavily on hand-crafted metrics, either through reference-based comparisons [50] or statistical measures of natural image properties [64]. However, these approaches typically focus on local image characteristics and fail to comprehensively capture global visual quality, limiting their reliability in complex real-world scenarios. More recently, deep learning-based IQA models [47, 19] have emerged, utilizing neural networks to learn hierarchical image representations. Nevertheless, these methods struggle to face significant challenges in out-of-distribution (OOD) generalization.

**ZH** 图像质量评估（IQA）是计算机视觉的基础任务，在优化算法、提升用户体验与验证内容真实性等方面至关重要，应用遍及图像处理 [41, 22, 11, 53] 与 AI 生成内容（AIGC）[37, 8] 等多个领域。传统 IQA 方法高度依赖手工设计的指标，或是通过基于参考的比较 [50]，或是通过自然图像属性的统计度量 [64]。然而，这些方法通常只关注图像的局部特征，无法全面刻画整体视觉质量，在复杂真实场景中的可靠性因而受限。近年来，基于深度学习的 IQA 模型 [47, 19] 兴起，用神经网络学习层次化的图像表示；但这些方法在分布外（OOD）泛化上仍面临严峻挑战。

**EN** With recent advances in multi-modal large language models (MLLMs) [23, 1, 48], researchers have begun to leverage these models’ extensive world knowledge and perceptual abilities to enhance IQA performance and broaden its applicability [53, 60, 59, 58, 52]. Existing MLLM-based IQA methods generally fall into two categories: score-based methods, such as Q-Align [53] and DeQA-Score [58], and description-based methods, exemplified by DepictQA [60] and DepictQA-Wild [59]. Score-based methods transform discrete tokens into continuous quality scores, thereby improving adaptability but typically sacrificing interpretability and neglecting MLLMs’ intrinsic reasoning and descriptive capabilities. Meanwhile, simply regressing a quality score may not be meaningful in certain scenarios, as image quality scores are subjective, inherently biased, and lack uniform standards across different datasets and content types. For example, when evaluating AIGC-generated data, unusual visual effects and vibrant colors often imply better quality. However, for evaluating super-resolution results, these same features are often considered too painterly, losing the image’s authenticity and fidelity. Conversely, description-based methods produce detailed textual explanations of image degradations and comparative assessments, ensuring interpretability yet heavily depending on extensive textual depiction for supervised fine-tuning. Moreover, these models cannot output precise scores, making them unsuitable when used as loss functions or for performing accurate ranking of image quality. Consequently, integrating numerical scoring and descriptive reasoning into a unified, interpretable MLLM-based IQA framework remains an essential yet unresolved challenge.

**ZH** 随着多模态大语言模型（MLLM）[23, 1, 48] 的最新进展，研究者开始利用这些模型广博的世界知识与感知能力来提升 IQA 性能并拓展其适用范围 [53, 60, 59, 58, 52]。现有基于 MLLM 的 IQA 方法大致分为两类：基于分数的方法，如 Q-Align [53] 与 DeQA-Score [58]；基于描述的方法，以 DepictQA [60] 与 DepictQA-Wild [59] 为代表。基于分数的方法把离散词元转换为连续的质量分数，提升了适应性，却通常以牺牲可解释性为代价，并忽视了 MLLM 固有的推理与描述能力。同时，单纯回归质量分数在某些场景下意义有限，因为图像质量分数具有主观性、天然存在偏差，且在不同数据集与内容类型之间缺乏统一标准。例如在评估 AIGC 生成数据时，奇特的视觉效果与鲜艳的色彩往往意味着更好的质量；但在评估超分辨率结果时，同样的特征常被认为过于“绘画感”，丧失了图像的真实性与保真度。相反，基于描述的方法会给出关于图像退化与比较评估的详细文本解释，保证了可解释性，却严重依赖大规模文本描述来进行监督微调。此外，这类模型无法输出精确分数，因而不适合用作损失函数，也不适合用于图像质量的精确排序。因此，把数值评分与描述性推理整合进一个统一、可解释的基于 MLLM 的 IQA 框架，仍是一项关键而未解决的挑战。

<!-- [原子块 · img]  -->

**EN** Figure 1: PLCC comparisons between our proposed Q-Insight and existing IQA metrics (left) and three example applications of our Q-Insight (right) are presented. Q-Insight demonstrates significantly improved performance compared to existing methods such as DeQA-Score [58], especially on out-of-domain datasets (e.g., CSIQ [20]). Additionally, Q-Insight effectively supports quality score regression, image degradation perception, and zero-shot image comparison reasoning tasks.

**ZH** 图 1：展示了我们所提出的 Q-Insight 与现有 IQA 指标的 PLCC 对比（左），以及 Q-Insight 的三个应用示例（右）。相比 DeQA-Score [58] 等现有方法，Q-Insight 性能显著提升，在域外数据集（如 CSIQ [20]）上尤为明显。此外，Q-Insight 能有效支持质量分数回归、图像退化感知与零样本图像比较推理任务。

**EN** In this paper, we move towards a comprehensive understanding of image quality by addressing tasks such as image description, aesthetic and compositional evaluation, degradation perception, and comparative reasoning across images. Rather than teaching the large model “How to score images”, we aim to inspire it “How to reason deeply and formulate insightful perspectives on image quality metrics during scoring”. To this end, we resort to Group Relative Policy Optimization (GRPO) [40], a reinforcement learning framework inspired by DeepSeek-R1 [15]. GRPO has recently shown to be highly effective in large language models (LLMs). It uses heuristic reward signals to efficiently guide LLMs in uncovering their intrinsic reasoning capabilities, removing extensive reliance on annotated reasoning chains or additional value models. Recently, researchers have also successfully adapted GRPO to vision-language tasks, including few-shot object detection, reasoning grounding [25], and medical analysis [34]. In the context of image quality understanding, the introduction of GRPO provides at least three distinct advantages: (1) no reliance on massive textual training data, (2) strong generalization to OOD evaluated images, and (3) high diversity in supporting multiple tasks. These benefits align well with our goal of developing a generalized image quality understanding agent.

**ZH** 本文致力于全面理解图像质量，涵盖图像描述、美学与构图评价、退化感知以及跨图像比较推理等任务。我们的目标不是教会大模型“如何给图像打分”，而是启发它“如何在打分时深入推理，并就图像质量指标形成有洞见的判断”。为此，我们采用受 DeepSeek-R1 [15] 启发的强化学习框架——组相对策略优化（GRPO）[40]。GRPO 近期在大型语言模型（LLM）中展现出极高的有效性：它用启发式奖励信号高效引导 LLM 发掘自身内在的推理能力，摆脱了对标注推理链或额外价值模型的重度依赖。近期研究者也成功将 GRPO 适配到视觉—语言任务，包括少样本目标检测、推理定位 [25] 与医学分析 [34]。在图像质量理解这一语境下，引入 GRPO 至少带来三点独特优势：（1）不依赖海量文本训练数据；（2）对被评估的 OOD 图像具有强泛化性；（3）支持多任务时的高度多样性。这些优势恰好契合我们构建通用图像质量理解智能体的目标。

**EN** Specifically, we design Q-Insight upon the GRPO framework. In our Q-Insight, we jointly optimize score regression and degradation perception tasks, and carefully design three reward functions: a verifiable score reward for the score regression task, and degradation classification and intensity perception rewards for the degradation perception task. Consequently, Q-Insight effectively exhibits robust reasoning performance using only limited Mean Opinion Scores (MOS) and degradation labels. As shown in Fig. 1, our Q-Insight delivers remarkable performance improvements especially on OOD datasets, while demonstrating comprehensive capabilities across multiple quality assessment and reasoning tasks. For example, it can accurately identify cases where a slightly blurred background, usually regarded as undesirable, effectively helps to emphasize the primary subject of the image. Our empirical investigation reveals that: (1) training solely with score labels results in poor perception of image detail degradations (e.g., JPEG compression), while jointly training with the degradation perception task significantly enhances the model’s sensitivity to such degradations, and (2) score regression and degradation perception tasks are mutually beneficial. Extensive experiments across score regression and degradation perception tasks demonstrate that Q-Insight consistently outperforms existing model-based IQA metrics as well as SFT-driven large language models. Moreover, it exhibits impressive zero-shot generalization on unseen tasks, such as image comparison reasoning, highlighting the robustness and versatility of our method. In summary, our contributions are:

**ZH** 具体而言，我们在 GRPO 框架上设计了 Q-Insight。在 Q-Insight 中，我们联合优化分数回归与退化感知两项任务，并精心设计了三个奖励函数：面向分数回归任务的可验证分数奖励，以及面向退化感知任务的退化分类奖励与强度感知奖励。因此，Q-Insight 仅需有限的平均意见分数（MOS）与退化标签，便展现出稳健的推理性能。如图 1 所示，Q-Insight 尤其在 OOD 数据集上带来显著的性能提升，同时在多种质量评估与推理任务上展现出全面的能力。举例来说，它能准确识别出：通常被视为不利的轻微背景虚化，实际上有助于突出画面主体。我们的实证研究发现：（1）仅用分数标签训练会导致模型对图像细节退化（如 JPEG 压缩）感知不佳，而与退化感知任务联合训练则显著提升了模型对此类退化的敏感度；（2）分数回归与退化感知两项任务互为助益。在分数回归与退化感知任务上的大量实验表明，Q-Insight 持续优于现有的基于模型的 IQA 指标以及 SFT 驱动的大语言模型。此外，它在未见过任务（如图像比较推理）上展现出令人印象深刻的零样本泛化能力，凸显了本方法的鲁棒性与通用性。综上，我们的贡献如下：

**EN** ❑(1) We propose Q-Insight, the first reasoning-style multi-modal large language model specifically designed for comprehensive image quality understanding. Unlike previous methods that depend heavily on detailed textual descriptions for supervised fine-tuning (SFT), our approach achieves superior understanding capability using only limited mean opinion scores or degradation labels.

**ZH** ❑(1) 我们提出 Q-Insight，首个专为全面图像质量理解而设计的推理式多模态大语言模型。与以往严重依赖详细文本描述进行监督微调（SFT）的方法不同，本方法仅需有限的平均意见分数或退化标签，即可获得更优的理解能力。

**EN** ❑(2) We introduce a unified framework that jointly optimizes image quality rating and degradation perception, revealing mutual benefits across tasks. Within this framework, we develop three specialized rewards, including verifiable score reward, degradation classification and intensity perception rewards, enabling the GRPO framework to effectively generalize to low-level vision applications.

**ZH** ❑(2) 我们引入一个统一框架，联合优化图像质量评分与退化感知，揭示了任务之间的互惠效应。在该框架内，我们设计了三种专门的奖励——可验证分数奖励、退化分类奖励与强度感知奖励，使 GRPO 框架得以有效泛化到低层视觉应用。

**EN** ❑(3) Extensive experiments across diverse datasets and IQA tasks demonstrate that Q-Insight consistently outperforms existing model-based IQA metrics as well as SFT-driven large language models. Moreover, it exhibits impressive zero-shot generalization on unseen tasks, such as reference-based image comparison reasoning, highlighting the robustness and versatility of our method.

**ZH** ❑(3) 在多个数据集与 IQA 任务上的大量实验表明，Q-Insight 持续优于现有的基于模型的 IQA 指标以及 SFT 驱动的大语言模型。此外，它在未见过任务（如基于参考的图像比较推理）上展现出令人印象深刻的零样本泛化能力，凸显了本方法的鲁棒性与通用性。

**EN** 2 Related Work

**ZH** 2 相关工作

**EN** Score-based IQA methods include full-reference and no-reference approaches. Full-reference methods [50, 42, 65] assess image quality by comparing distorted images with high-quality references using traditional metrics (e.g., SSIM [50]) or advanced deep-learning-based metrics [3, 4, 10, 9, 13, 36] like LPIPS [66]. Non-reference methods evaluate quality without reference images, shifting from traditional handcrafted statistics [27, 28, 29, 30, 31, 38] to deep-learning-derived quality priors [18, 19, 24, 33, 44, 72, 73, 45, 49]. Recent multi-modal large language model (MLLM)-based methods, such as Q-Align [53] and DeQA-Score [58], leverage MLLMs’ knowledge and perceptual abilities to produce scores. However, they sacrifice the intrinsic descriptive capabilities of MLLMs.

**ZH** 基于分数的 IQA 方法包括全参考与无参考两类。全参考方法 [50, 42, 65] 通过把失真图像与高质量参考图像比较来评估质量，所用指标既有传统指标（如 SSIM [50]），也有先进的深度学习指标 [3, 4, 10, 9, 13, 36]（如 LPIPS [66]）。无参考方法不需要参考图像，其演进路径是从传统手工统计量 [27, 28, 29, 30, 31, 38] 转向由深度学习得到的质量先验 [18, 19, 24, 33, 44, 72, 73, 45, 49]。近期基于多模态大语言模型（MLLM）的方法，如 Q-Align [53] 与 DeQA-Score [58]，利用 MLLM 的知识与感知能力输出分数，却牺牲了 MLLM 固有的描述能力。

**EN** Description-based IQA methods utilize the foundational knowledge of MLLMs to deliver detailed qualitative assessments and improved interpretability [51, 52, 60, 59, 54, 5, 69, 70, 68]. For instance, Q-Bench [51] and Q-Instruct [52] enhance the low-level perceptual capabilities of MLLMs through specialized datasets and tailored evaluation strategies. Co-Instruct [54] specifically focuses on comparative quality assessments among multiple images. Approaches such as DepictQA [60] and DepictQA-Wild [59] handle both single-image and paired-image evaluations across full-reference and no-reference scenarios. Q-Ground [5] emphasizes a detailed visual quality analysis through visual grounding. However, these methods are highly dependent on extensive textual annotations for supervised fine-tuning, leading to considerable costs in human labor or GPT token consumption.

**ZH** 基于描述的 IQA 方法借助 MLLM 的基础知识，给出细致的定性评估并提升可解释性 [51, 52, 60, 59, 54, 5, 69, 70, 68]。例如，Q-Bench [51] 与 Q-Instruct [52] 通过专用数据集与定制的评估策略增强 MLLM 的低层感知能力；Co-Instruct [54] 专门关注多图之间的比较质量评估；DepictQA [60] 与 DepictQA-Wild [59] 则在全参考与无参考场景下同时处理单图与成对图像的评估；Q-Ground [5] 强调通过视觉定位做细致的视觉质量分析。然而，这些方法高度依赖大规模文本标注以进行监督微调，带来可观的人力成本或 GPT 词元开销。

**EN** Reinforcement learning (RL) has emerged as an effective strategy to enhance the reasoning performance of LLMs through feedback-driven refinement [7, 43, 40, 55, 57, 17, 67]. Methods like RLHF [32] and RLAIF [2] employ human or AI-generated feedback to refine model behavior. In vision-language tasks, RL has successfully been employed to align model predictions closely with human preferences and reduce hallucinations [46, 61, 62, 71]. Recently, DeepSeek-R1-Zero [15] introduced group relative policy optimization (GRPO) [40], leveraging rule-based rewards to strengthen reasoning capabilities without supervised fine-tuning. Furthermore, Visual-RFT [25] applied GRPO to visual grounding, and Med-R1 [34] adopted GRPO for medical reasoning tasks. R1-VL [63] extends GRPO through step-wise optimization for multi-modal reasoning. Distinctly, our Q-Insight is the first to integrate RL-based strategies into the foundational visual quality understanding model. It jointly trains on multiple tasks and demonstrates mutually beneficial effects among them.

**ZH** 强化学习（RL）已成为通过反馈驱动的精调来增强 LLM 推理性能的有效策略 [7, 43, 40, 55, 57, 17, 67]。RLHF [32] 与 RLAIF [2] 等方法借助人类或 AI 生成的反馈来改进模型行为。在视觉—语言任务中，RL 已被成功用于使模型预测更贴近人类偏好并减少幻觉 [46, 61, 62, 71]。近期，DeepSeek-R1-Zero [15] 提出组相对策略优化（GRPO）[40]，基于规则奖励强化推理能力，无需监督微调。此外，Visual-RFT [25] 将 GRPO 应用于视觉定位，Med-R1 [34] 把 GRPO 用于医学推理任务，R1-VL [63] 则通过分步优化将 GRPO 扩展到多模态推理。与之不同，我们的 Q-Insight 首次把基于 RL 的策略引入基础视觉质量理解模型，在多个任务上联合训练，并展现出任务之间的互惠效应。

**EN** 3 Methodology

**ZH** 3 方法

**EN** 3.1 Preliminaries

**ZH** 3.1 预备知识

**EN** Group Relative Policy Optimization (GRPO) is an innovative reinforcement learning paradigm that has been widely used in models such as DeepSeek R1-Zero [15], achieving excellent results. Unlike Proximal Policy Optimization (PPO) [39], which requires an explicit critic model to evaluate the performance of the policy model, GRPO [40] directly computes the advantage by comparing a group of responses sampled from the policy model, greatly reducing the computational burden. Specifically, given a query ⟦SLOT_0⟧, GRPO samples ⟦SLOT_1⟧ distinct responses ⟦SLOT_2⟧ from the old policy ⟦SLOT_3⟧. Then, the method performs the corresponding actions and receives the respective rewards ⟦SLOT_4⟧ according to the task-specific rules. By calculating the mean and standard deviation of the rewards, the relative advantages of each response can be obtained as follows:

**ZH** 组相对策略优化（GRPO）是一种创新的强化学习范式，已在 DeepSeek R1-Zero [15] 等模型中广泛应用并取得优异效果。与需要显式评论家（critic）模型来评估策略模型表现的近端策略优化（PPO）[39] 不同，GRPO [40] 通过比较从策略模型采样出的一组回答直接计算优势，大幅降低了计算负担。具体而言，给定查询 ⟦SLOT_0⟧，GRPO 从旧策略 ⟦SLOT_3⟧ 采样出 ⟦SLOT_1⟧ 个不同的回答 ⟦SLOT_2⟧；随后执行相应动作，并依据任务特定规则获得各自的奖励 ⟦SLOT_4⟧。通过计算奖励的均值与标准差，可得到每个回答的相对优势如下：

<!-- [原子块 · table] A ^ ( i ) \displaystyle\hat{A}^{(i)} = r ( i ) − mean ⁡ ( { r ( 1 ) , r ( 2 ) ​ … , r ( N ) } ) std ⁡ ( { r ( 1 ) , r ( 2 ) ​ … , r ( N ) } ) , \displaystyle=\frac{r^{(i)}-\operatorname{mean}(\{r^{(1) -->

**EN** where ⟦SLOT_5⟧ represents the normalized relative quality of the ⟦SLOT_6⟧-th answer. Overall, GRPO guides the policy model to prioritize higher-quality answers that receive higher reward values within the group. After obtaining the advantage ⟦SLOT_7⟧, GRPO calculates the ratio of the probabilities of each response under the new policy ⟦SLOT_8⟧ and the old policy ⟦SLOT_9⟧, denoted as ⟦SLOT_10⟧. To prevent overly large updates to the model and stabilize training, GRPO restricts the ⟦SLOT_11⟧ to the range ⟦SLOT_12⟧. To further maintain closeness to the reference distribution ⟦SLOT_13⟧, a KL divergence penalty weighted by ⟦SLOT_14⟧ is adopted. Finally, the optimization objective of GRPO can be formulated as follows:

**ZH** 其中 ⟦SLOT_5⟧ 表示第 ⟦SLOT_6⟧ 个回答的归一化相对质量。总体上，GRPO 引导策略模型优先选择组内获得更高奖励值的高质量回答。得到优势 ⟦SLOT_7⟧ 后，GRPO 计算每个回答在新策略 ⟦SLOT_8⟧ 与旧策略 ⟦SLOT_9⟧ 下的概率之比，记为 ⟦SLOT_10⟧。为防止模型更新幅度过大并稳定训练，GRPO 把 ⟦SLOT_11⟧ 限制在 ⟦SLOT_12⟧ 范围内。为进一步保持与参考分布 ⟦SLOT_13⟧ 的接近，还引入以 ⟦SLOT_14⟧ 加权的 KL 散度惩罚。最终，GRPO 的优化目标可表述如下：

<!-- [原子块 · table] 𝒥 ⁡ ( θ ) = 𝔼 [ q ∼ Q , o ( i ) ∼ π θ old ] \displaystyle\mathcal{J}(\theta)=\mathbb{E}_{[q\sim Q,o^{(i)}\sim\pi_{\theta_{\text{old}}}]} { min [ ρ ( i ) A ^ ( i ) , clip ( ρ ( i ) , 1 − δ , 1 + δ ) A  -->

**EN** where ⟦SLOT_15⟧, ⟦SLOT_16⟧ denotes the candidate question set, and ⟦SLOT_17⟧ denotes the KL regularization. ⟦SLOT_18⟧ is typically a frozen pre-trained MLLM. GRPO effectively integrates consistent policy updates and strong reward signals in a balanced way. To our knowledge, we are the first to apply GRPO to image quality understanding tasks, enabling our model to achieve robust reasoning and generalization performance without heavy reliance on extensive annotated data.

**ZH** 其中 ⟦SLOT_15⟧、⟦SLOT_16⟧ 表示候选问题集合，⟦SLOT_17⟧ 表示 KL 正则项。⟦SLOT_18⟧ 通常为冻结的预训练 MLLM。GRPO 以均衡的方式有效整合了一致的策略更新与强奖励信号。据我们所知，我们是首个将 GRPO 应用于图像质量理解任务的工作，使模型无需重度依赖大规模标注数据即可获得稳健的推理与泛化性能。

**EN** 3.2 Overview of Q-Insight

**ZH** 3.2 Q-Insight 概览

**EN** The overall framework of Q-Insight is illustrated in Fig. 2. During training, we jointly optimize two tasks: score regression and degradation perception. Specifically, the multi-modal input for each task comprises an image paired with a task-specific question. Given these inputs, the policy model ⟦SLOT_19⟧ generates groups of answers, each accompanied by explicit reasoning steps. Subsequently, each answer is evaluated using its corresponding reward function: ⟦SLOT_20⟧ for score regression, and ⟦SLOT_21⟧ and ⟦SLOT_22⟧ for degradation perception. After computing rewards for each group of answers, the policy model is optimized jointly via the multi-task GRPO algorithm. Additionally, a KL-divergence loss is applied to constrain deviations between the policy model ⟦SLOT_23⟧ and the reference model ⟦SLOT_24⟧. During inference, the trained Q-Insight generates coherent reasoning processes and outputs precise answers. Further details regarding multi-task GRPO and data construction are provided in Sec. 3.3 and Sec. 3.4.

**ZH** Q-Insight 的整体框架如图 2 所示。训练时，我们联合优化分数回归与退化感知两项任务。具体而言，每项任务的多模态输入由一幅图像与一个任务特定的问题组成。给定这些输入，策略模型 ⟦SLOT_19⟧ 生成多组回答，每组回答都带有显式的推理步骤。随后，用相应的奖励函数评估每个回答：分数回归任务用 ⟦SLOT_20⟧，退化感知任务用 ⟦SLOT_21⟧ 与 ⟦SLOT_22⟧。在计算出每组回答的奖励后，通过多任务 GRPO 算法联合优化策略模型。此外，还施加 KL 散度损失，以约束策略模型 ⟦SLOT_23⟧ 与参考模型 ⟦SLOT_24⟧ 之间的偏差。推理时，训练好的 Q-Insight 会生成连贯的推理过程并输出精确答案。关于多任务 GRPO 与数据构建的更多细节见第 3.3 节与第 3.4 节。

<!-- [原子块 · img]  -->

**EN** Figure 2: Overview of the proposed Q-Insight framework. The policy model receives queries from multiple tasks and generates corresponding groups of responses accompanied by explicit reasoning steps. Task-specific reward functions (⟦SLOT_25⟧, ⟦SLOT_26⟧, and ⟦SLOT_27⟧) are then applied, and the policy model is subsequently optimized jointly using the multi-task group relative policy optimization algorithm.

**ZH** 图 2：所提出的 Q-Insight 框架概览。策略模型接收来自多个任务的查询，并生成相应的回答组，每组附带显式的推理步骤。随后施加任务特定的奖励函数（⟦SLOT_25⟧、⟦SLOT_26⟧ 与 ⟦SLOT_27⟧），再用多任务组相对策略优化算法联合优化策略模型。

**EN** 3.3 Multi-Task Group Relative Policy Optimization

**ZH** 3.3 多任务组相对策略优化

**EN** As depicted in Fig. 2, for each input data pair, the policy model ⟦SLOT_28⟧ generates a group of ⟦SLOT_29⟧ responses, denoted as ⟦SLOT_30⟧. We then evaluate each of these responses using the proposed reward functions (⟦SLOT_31⟧, ⟦SLOT_32⟧, and ⟦SLOT_33⟧) and obtain the overall rewards ⟦SLOT_34⟧. Proper reward design is crucial, as informative and carefully constructed rewards directly facilitate Q-Insight’s ability to effectively learn reasoning and perception patterns, thus ensuring robust performance across multiple tasks. Specifically, Q-Insight employs a general format reward function shared across all tasks, as well as task-specific reward functions tailored to the unique characteristics of each individual task.

**ZH** 如图 2 所示，对每个输入数据对，策略模型 ⟦SLOT_28⟧ 生成一组 ⟦SLOT_29⟧ 个回答，记为 ⟦SLOT_30⟧。随后用所提出的奖励函数（⟦SLOT_31⟧、⟦SLOT_32⟧ 与 ⟦SLOT_33⟧）评估每个回答，得到总体奖励 ⟦SLOT_34⟧。恰当的奖励设计至关重要，因为信息量充足、构造精细的奖励能直接帮助 Q-Insight 有效学习推理与感知模式，从而确保其在多个任务上的稳健表现。具体而言，Q-Insight 采用一个跨任务共享的通用格式奖励函数，以及针对各任务独特特性定制的任务特定奖励函数。

**EN** Format reward evaluates whether the reasoning steps are properly enclosed within “<think>” and “</think>” tags, and the final answer is correctly enclosed within “<answer>” and “</answer>” tags [15]. Additionally, we require that the content inside “<answer>” tags follow a JSON-like format: beginning with “{”, ending with “}”, and containing no additional “{” or “}” characters internally. This ensures that Q-Insight can consistently parse results across different tasks. The reward score ⟦SLOT_35⟧ is set to ⟦SLOT_36⟧ if the ⟦SLOT_37⟧-th response fulfills all the above conditions; otherwise, its reward is ⟦SLOT_38⟧.

**ZH** 格式奖励用于评判推理步骤是否正确包含在“<think>”与“</think>”标签内，以及最终答案是否正确包含在“<answer>”与“</answer>”标签内 [15]。此外，我们要求“<answer>”标签内的内容遵循类 JSON 格式：以“{”开头、以“}”结尾，且内部不含额外的“{”或“}”字符。这确保 Q-Insight 能在不同任务上一致地解析结果。若第 ⟦SLOT_37⟧ 个回答满足上述全部条件，奖励值 ⟦SLOT_35⟧ 设为 ⟦SLOT_36⟧，否则其奖励为 ⟦SLOT_38⟧。

**EN** Rewards for score regression task. A standard way to quantify image quality is by using the Mean Opinion Score (MOS). Instead of directly fitting the MLLM predictions to MOS, we use MOS as a general guideline to motivate the model towards deeper reasoning and generating insightful perspectives during the process of evaluating image quality. Inspired by the treatment of mathematical reasoning tasks in DeepSeek-R1 [15], we consider the continuous MOS prediction as either correct or incorrect, thereby adopting a binary reward to avoid extremely large or small reward values. Denoting the predicted score of the ⟦SLOT_39⟧-th response as ⟦SLOT_40⟧ and the ground-truth score as ⟦SLOT_41⟧, we design the verifiable reward for scoring as follows. The reward value ⟦SLOT_42⟧ for the ⟦SLOT_43⟧-th response is determined by:

**ZH** 分数回归任务的奖励。量化图像质量的标准方式是使用平均意见分数（MOS）。我们没有让 MLLM 的预测直接拟合 MOS，而是把 MOS 作为一般性指引，促使模型在评估图像质量的过程中进行更深入的推理并生成有洞见的判断。受 DeepSeek-R1 [15] 处理数学推理任务的方式启发，我们把连续的 MOS 预测判定为正确或错误两类，从而采用二值奖励以避免出现过大或过小的奖励值。记第 ⟦SLOT_39⟧ 个回答的预测分数为 ⟦SLOT_40⟧、真值分数为 ⟦SLOT_41⟧，我们设计的可验证评分奖励如下。第 ⟦SLOT_43⟧ 个回答的奖励值 ⟦SLOT_42⟧ 由下式确定：

<!-- [原子块 · table] r scr ( i ) = 1 if ​ ∣ scr pred ( i ) − scr gt ∣ < ϵ , otherwise ​ 0 , r^{(i)}_{\text{scr}}=1\ \quad\text{if}\ \mid\!\text{scr}^{(i)}_{\text{pred}}-\text{scr}_{\text{gt}}\!\mid<\epsilon,~\text{otherwi -->

**EN** where ⟦SLOT_44⟧ is a predefined threshold. In particular, if ⟦SLOT_45⟧ is set to ⟦SLOT_46⟧, the reward simplifies to exact-answer matching. Otherwise, the threshold ⟦SLOT_47⟧ allows the model’s predicted scores to fluctuate within an acceptable range, rather than strictly requiring exact accuracy. As depicted in Fig. 2, the predicted score receives a reward of ⟦SLOT_48⟧ if it lies within the threshold ⟦SLOT_49⟧ of the ground-truth MOS, and ⟦SLOT_50⟧ otherwise.

**ZH** 其中 ⟦SLOT_44⟧ 为预设阈值。特别地，若 ⟦SLOT_45⟧ 设为 ⟦SLOT_46⟧，该奖励即简化为精确答案匹配。否则，阈值 ⟦SLOT_47⟧ 允许模型预测的分数在可接受范围内浮动，而不严格要求完全准确。如图 2 所示，若预测分数落在真值 MOS 的阈值 ⟦SLOT_49⟧ 之内，则获得奖励 ⟦SLOT_48⟧，否则为 ⟦SLOT_50⟧。

**EN** Rewards for degradation perception task. We find that training solely with score labels leads to poor perception of detailed image degradations (e.g., JPEG compression). This may be because generic multimodal models are pre-trained primarily to capture high-level semantic information, causing them to ignore subtle low-level distortions. To address this issue, we jointly train the model with a degradation perception task, leveraging easily obtainable degradation labels, thus enhancing the model’s sensitivity to these image degradations. In this task, the model is required to predict both the distortion class and the corresponding distortion level. Since distortion class and level are inherently discrete variables, we similarly design binary rewards for this task. Denoting the predicted distortion class and level of the ⟦SLOT_51⟧-th response as ⟦SLOT_52⟧ and ⟦SLOT_53⟧ respectively, we define the degradation classification reward as follows. The reward value ⟦SLOT_54⟧ is determined by:

**ZH** 退化感知任务的奖励。我们发现，仅用分数标签训练会导致模型对图像细节退化（如 JPEG 压缩）感知不佳。原因可能在于通用多模态模型的预训练主要面向捕捉高层语义信息，因而忽略了细微的低层失真。为解决这一问题，我们联合训练退化感知任务，利用易于获取的退化标签来增强模型对此类图像退化的敏感度。在该任务中，模型需要同时预测失真类别与相应的失真等级。由于失真类别与等级本质上是离散变量，我们同样为该任务设计二值奖励。记第 ⟦SLOT_51⟧ 个回答预测的失真类别与等级分别为 ⟦SLOT_52⟧ 与 ⟦SLOT_53⟧，我们定义退化分类奖励如下。奖励值 ⟦SLOT_54⟧ 由下式确定：

<!-- [原子块 · table] r deg ( i ) = 1 if ​ deg pred ( i ) = deg gt , otherwise ​ 0 . r^{(i)}_{\text{deg}}=1\quad\text{if}\ \text{deg}^{(i)}_{\text{pred}}=\text{deg}_{\text{gt}},~\text{otherwise }0. (4) -->

**EN** This means the predicted distortion class receives a reward of ⟦SLOT_55⟧ if correct, and ⟦SLOT_56⟧ otherwise, as illustrated in Fig. 2. Similarly, the intensity perception reward ⟦SLOT_57⟧ is determined by:

**ZH** 这意味着，若预测的失真类别正确则获得奖励 ⟦SLOT_55⟧，否则为 ⟦SLOT_56⟧，如图 2 所示。类似地，强度感知奖励 ⟦SLOT_57⟧ 由下式确定：

<!-- [原子块 · table] r lev ( i ) = 1 if ​ deg pred ( i ) = deg gt ​ and ​ lev pred ( i ) = lev gt , otherwise ​ 0 . r^{(i)}_{\text{lev}}=1\quad\text{if}\ \text{deg}^{(i)}_{\text{pred}}=\text{deg}_{\text{gt}}\ {\text{and}} -->

**EN** As depicted in Fig. 2, the predicted distortion level earns a reward of ⟦SLOT_58⟧ only when both the predicted class and the level exactly match the ground truth; otherwise, it receives ⟦SLOT_59⟧.

**ZH** 如图 2 所示，只有当预测的类别与等级都与真值精确匹配时，预测的失真等级才获得奖励 ⟦SLOT_58⟧，否则为 ⟦SLOT_59⟧。

**EN** Overall multi-task reward. Finally, the overall reward of ⟦SLOT_60⟧-th response is calculated as:

**ZH** 总体多任务奖励。最后，第 ⟦SLOT_60⟧ 个回答的总体奖励计算如下：

<!-- [原子块 · table] r ( i ) = r fmt ( i ) + 𝟙 scr ⋅ r scr ( i ) + 𝟙 deg ⋅ ( α 1 ⋅ r deg ( i ) + α 2 ⋅ r lev ( i ) ) , r^{(i)}=r^{(i)}_{\text{fmt}}+\mathds{1}_{\text{scr}}\cdot r^{(i)}_{\text{scr}}+\mathds{1}_{\text{deg}} -->

**EN** where ⟦SLOT_61⟧ equals ⟦SLOT_62⟧ if the score regression task is selected (and ⟦SLOT_63⟧ otherwise), and similarly, ⟦SLOT_64⟧ equals ⟦SLOT_65⟧ if the degradation perception task is selected (and ⟦SLOT_66⟧ otherwise). Note that the reasoning process illustrated in Fig. 2 emerges naturally from the model’s internal capability, without relying on external constraints or additional annotated data. After computing rewards for all generated responses ⟦SLOT_67⟧, the policy model is updated following Eqs. (1) and (2). With this flexible design, Q-Insight can seamlessly switch between tasks and jointly optimize them during training. During inference, the trained policy model can directly perform image quality understanding without requiring additional fine-tuning. Experimental results presented in Tabs. 3 and 4 and Fig. A further demonstrate that jointly addressing the score regression and degradation perception tasks substantially improves performance, highlighting the beneficial interactions between these two tasks.

**ZH** 其中，若选中分数回归任务则 ⟦SLOT_61⟧ 取 ⟦SLOT_62⟧（否则取 ⟦SLOT_63⟧）；类似地，若选中退化感知任务则 ⟦SLOT_64⟧ 取 ⟦SLOT_65⟧（否则取 ⟦SLOT_66⟧）。需要说明的是，图 2 中展示的推理过程源自模型的内在能力自然涌现，不依赖外部约束或额外的标注数据。在为所有生成的回答 ⟦SLOT_67⟧ 计算完奖励后，策略模型按式 (1) 与式 (2) 更新。凭借这一灵活设计，Q-Insight 可以在训练期间无缝切换任务并联合优化它们。推理时，训练好的策略模型无需额外微调即可直接执行图像质量理解。表 3、表 4 与图 A 中的实验结果进一步表明，同时处理分数回归与退化感知任务可大幅提升性能，凸显了这两项任务之间的良性互动。

**EN** 3.4 Data Construction

**ZH** 3.4 数据构建

**EN** We construct multi-modal training data to jointly train Q-Insight on the score regression and degradation perception tasks. The prompts designed for each task are detailed in Tab. A in the appendix. For the score regression task, the input includes a task-specific prompt and the image to be rated, with the Mean Opinion Score (MOS) serving as the guideline to calculate the corresponding reward. In the degradation perception task, the input consists of a prompt and an image characterized by a specific distortion class and severity level. There are five distortion categories: “noise”, “blur”, “JPEG”, “darken”, and “null”, where “null” indicates no distortion. Each distortion type has five severity levels: “slight”, “moderate”, “obvious”, “serious”, and “catastrophic”. The distortion class and corresponding severity level constitute the ground-truth labels to calculate the degradation classification and intensity perception rewards. Overall, our carefully-designed GRPO-based framework and multi-task training strategy help Q-Insight achieve robust reasoning and perception capability even from limited annotated labels. More importantly, this flexible approach facilitates effective generalization to various low-level vision applications, as demonstrated by extensive experiments in Sec. 4, clearly highlighting the advantages of our framework in addressing practical vision tasks.

**ZH** 我们构建多模态训练数据，在分数回归与退化感知任务上联合训练 Q-Insight。各任务设计的提示详见附录表 A。对于分数回归任务，输入包括任务特定的提示与待评分的图像，以平均意见分数（MOS）作为计算相应奖励的依据。对于退化感知任务，输入包括提示与一幅具有特定失真类别与严重程度的图像。失真类别共五类：“noise”“blur”“JPEG”“darken”与“null”，其中“null”表示无失真。每种失真类型有五个严重程度等级：“slight”“moderate”“obvious”“serious”与“catastrophic”。失真类别与相应的严重程度等级共同构成真值标签，用于计算退化分类与强度感知奖励。总体而言，我们精心设计的基于 GRPO 的框架与多任务训练策略，使 Q-Insight 即使在有限标注标签下也能获得稳健的推理与感知能力。更重要的是，这种灵活的方式有利于有效泛化到各类低层视觉应用，第 4 节的大量实验证明了这一点，也清晰展现了本框架在解决实际视觉任务上的优势。

**EN** Table 1: PLCC / SRCC comparison on the score regression tasks between our Q-Insight and other competitive IQA methods. All methods except handcrafted ones are trained on the KonIQ dataset. The best and second-best results of each test setting are highlighted in bold red and underlined blue.

**ZH** 表 1：Q-Insight 与其他有竞争力的 IQA 方法在分数回归任务上的 PLCC / SRCC 对比。除手工设计的方法外，所有方法均在 KonIQ 数据集上训练。每种测试设置下的最优与次优结果分别以红色粗体与蓝色下划线标出。

<!-- [原子块 · table] Category Methods KonIQ SPAQ KADID PIPAL LiveW AGIQA CSIQ AVG. Handcrafted NIQE [ 29 ] 0.533 0.679 0.468 0.195 0.493 0.560 0.718 0.521 (SPL 2012) / 0.530 / 0.664 / 0.405 / 0.161 / 0.449 / 0.533 / 0.628 -->

**EN** 4 Experiments

**ZH** 4 实验

**EN** 4.1 Experimental Setup

**ZH** 4.1 实验设置

**EN** Datasets and Metrics. For the score regression task, we use diverse IQA datasets across four categories: (a) in-the-wild datasets, including KonIQ [16], SPAQ [11], and LIVE-Wild [12]; (b) synthetic distortion datasets, including KADID [22] and CSIQ [20]; (c) model-processed distortions, including PIPAL [14]; and (d) AI-generated images from AGIQA [21]. Following [58], we split KonIQ into training and test sets, with approximately ⟦SLOT_68⟧ training images. Mean Opinion Scores (MOS) across these datasets are normalized into the range ⟦SLOT_69⟧. The remaining datasets are exclusively used to evaluate the model’s out-of-distribution (OOD) generalization capability. For degradation perception task, we randomly select ⟦SLOT_70⟧ images from DQ-495K [59] that contain a single distortion for training, with an additional ⟦SLOT_71⟧ images reserved for testing. We adopt the pearson linear correlation coefficient (PLCC) and spearman rank-order correlation coefficient (SRCC) as metrics to evaluate performance on score regression task, following [19, 53, 58]. For degradation perception, we use the accuracy of distortion class and degradation level as evaluation metrics.

**ZH** 数据集与指标。对于分数回归任务，我们使用涵盖四类的多个 IQA 数据集：（a）真实场景数据集，包括 KonIQ [16]、SPAQ [11] 与 LIVE-Wild [12]；（b）合成失真数据集，包括 KADID [22] 与 CSIQ [20]；（c）模型处理产生的失真，包括 PIPAL [14]；（d）来自 AGIQA [21] 的 AI 生成图像。沿用 [58] 的做法，我们把 KonIQ 划分为训练集与测试集，其中训练图像约 ⟦SLOT_68⟧ 张。这些数据集上的平均意见分数（MOS）被归一化到 ⟦SLOT_69⟧ 区间。其余数据集专门用于评估模型的分布外（OOD）泛化能力。对于退化感知任务，我们从 DQ-495K [59] 中随机选取 ⟦SLOT_70⟧ 张仅含单一失真的图像用于训练，另留 ⟦SLOT_71⟧ 张用于测试。沿用 [19, 53, 58]，我们采用皮尔逊线性相关系数（PLCC）与斯皮尔曼秩相关系数（SRCC）作为分数回归任务的评估指标。对于退化感知，我们使用失真类别准确率与退化等级准确率作为评估指标。

**EN** Implementation Details. We adopt Qwen-2.5-VL-7B-Instruct [1] as our base model. In the GRPO algorithm, the generation number ⟦SLOT_72⟧ is set to ⟦SLOT_73⟧, the weight of KL divergence penalty ⟦SLOT_74⟧ is set to ⟦SLOT_75⟧, while the weights ⟦SLOT_76⟧ and ⟦SLOT_77⟧ are set to ⟦SLOT_78⟧ and ⟦SLOT_79⟧, respectively. The threshold ⟦SLOT_80⟧ is set to ⟦SLOT_81⟧. We employ AdamW [26] as the optimizer, using an initial learning rate of ⟦SLOT_82⟧ that linearly decays to ⟦SLOT_83⟧ during training. The model is trained for ⟦SLOT_84⟧ epochs with a total batch size of ⟦SLOT_85⟧. Training is completed in approximately one day using 16 NVIDIA A100 GPUs.

**ZH** 实现细节。我们采用 Qwen-2.5-VL-7B-Instruct [1] 作为基座模型。在 GRPO 算法中，生成数量 ⟦SLOT_72⟧ 设为 ⟦SLOT_73⟧，KL 散度惩罚权重 ⟦SLOT_74⟧ 设为 ⟦SLOT_75⟧，权重 ⟦SLOT_76⟧ 与 ⟦SLOT_77⟧ 分别设为 ⟦SLOT_78⟧ 与 ⟦SLOT_79⟧，阈值 ⟦SLOT_80⟧ 设为 ⟦SLOT_81⟧。我们使用 AdamW [26] 作为优化器，初始学习率为 ⟦SLOT_82⟧，在训练中线性衰减至 ⟦SLOT_83⟧。模型训练 ⟦SLOT_84⟧ 个轮次，总批大小为 ⟦SLOT_85⟧。使用 16 张 NVIDIA A100 GPU 约一天即可完成训练。

<!-- [原子块 · img]  -->

**EN** Figure 3: Score rating and explanation results of our Q-Insight. Q-Insight is capable of recognizing text, analyzing the lighting and shading conditions of an image, and understanding its composition.

**ZH** 图 3：Q-Insight 的评分与解释结果。Q-Insight 能够识别文字、分析图像的光照与明暗条件，并理解其构图。

**EN** Table 2: Distortion prediction accuracy (Deg. Acc.) and degradation level accuracy (Lev. Acc.) comparison between our Q-Insight and AgenticIR [75]. Our method outperforms AgenticIR across all degradations, especially in Noise and JPEG Compression.

**ZH** 表 2：Q-Insight 与 AgenticIR [75] 在失真预测准确率（Deg. Acc.）与退化等级准确率（Lev. Acc.）上的对比。本方法在所有退化类型上均优于 AgenticIR，在噪声与 JPEG 压缩上尤为突出。

<!-- [原子块 · table] Method Metrics Noise Blur JPEG Darken Null Average AgenticIR [ 75 ] (ICLR 2025) Deg. Acc. 0.4646 0.8390 0.0135 0.7478 0.9339 0.5998 Lev. Acc. 0.1858 0.3219 0.0000 0.2611 - 0.1922 Q-Insight (Ours) Deg. -->

**EN** 4.2 Score Regression

**ZH** 4.2 分数回归

**EN** We first evaluate our Q-Insight on the score regression task. We compare Q-Insight with handcrafted methods NIQE [29] and BRISQUE [28]; non-MLLM deep-learning methods including NIMA [47], MUSIQ [19], CLIP-IQA+ [49], and ManIQA [56]; and recent MLLM-based methods such as C2Score [74], Q-Align [53], DeQA-Score [58], and a supervised fine-tuned Qwen [1]. For a fair comparison, all methods (except handcrafted ones) are trained on the KonIQ dataset, and all MLLM-based methods utilize approximately 7B parameters. The comparison results in terms of PLCC and SRCC between Q-Insight and other IQA methods are presented in Tab. 1. Compared with the state-of-the-art method DeQA-Score, our Q-Insight performs slightly worse on the in-domain KonIQ dataset. However, on out-of-distribution (OOD) datasets, Q-Insight consistently outperforms all baseline methods across nearly all benchmarks, achieving approximately ⟦SLOT_86⟧ improvements in both PLCC and SRCC. This demonstrates the effectiveness and strong generalization capability of our approach. Fig. 3 illustrates two cases showing the reasoning capability in the score regression task. Specifically, our method goes beyond merely outputting numerical scores and provides detailed, structured reasoning. In the first case (top of Fig. 3), Q-Insight correctly identifies and analyzes textual information displayed on a neon sign, thoroughly examining details such as lighting conditions. In the second case (bottom of Fig. 3), Q-Insight demonstrates its strength in interpreting image composition aspects, such as the arrangement of visual elements and the primary focal point of the image. These examples further illustrate how Q-Insight advances beyond score regression task, offering valuable insights into image quality by examining various perceptual factors from multiple perspectives, ultimately contributing to a comprehensive understanding of image quality.

**ZH** 我们首先在分数回归任务上评估 Q-Insight，将其与手工设计方法 NIQE [29] 与 BRISQUE [28]、非 MLLM 的深度学习方法（包括 NIMA [47]、MUSIQ [19]、CLIP-IQA+ [49] 与 ManIQA [56]），以及近期基于 MLLM 的方法（如 C2Score [74]、Q-Align [53]、DeQA-Score [58] 与监督微调后的 Qwen [1]）进行比较。为保证比较公平，除手工设计方法外，所有方法都在 KonIQ 数据集上训练，且所有基于 MLLM 的方法参数量均约为 7B。表 1 给出了 Q-Insight 与其他 IQA 方法在 PLCC 与 SRCC 上的对比结果。与最优方法 DeQA-Score 相比，我们的 Q-Insight 在域内的 KonIQ 数据集上略逊一筹；但在分布外（OOD）数据集上，Q-Insight 在几乎所有基准上都持续优于所有基线方法，PLCC 与 SRCC 均取得约 ⟦SLOT_86⟧ 的提升，证明了本方法的有效性与强泛化能力。图 3 展示了两个体现分数回归任务中推理能力的案例。具体而言，本方法不止输出数值分数，还提供细致、结构化的推理。第一个案例（图 3 上）中，Q-Insight 正确识别并分析了霓虹灯牌上显示的文字信息，并细致考察了光照条件等细节。第二个案例（图 3 下）中，Q-Insight 展现出在解读图像构图方面的优势，如视觉元素的排布与画面主焦点。这些例子进一步说明，Q-Insight 超越了单纯的分数回归任务，通过从多个视角考察各类感知因素，为图像质量提供了有价值的洞见，最终促成对图像质量的全面理解。

**EN** Table 3: Ablation study on the score regression task between multi-task and single-task training. Q-Insight with joint-training significantly outperforms score-only training on PLCC / SRCC metrics.

**ZH** 表 3：分数回归任务上多任务训练与单任务训练的消融研究。联合训练的 Q-Insight 在 PLCC / SRCC 指标上显著优于仅用分数训练。

<!-- [原子块 · table] Method KonIQ SPAQ KADID PIPAL LiveW AGIQA CSIQ AVG. Ours (Score-Only) 0.918 0.903 0.702 0.458 0.870 0.816 0.685 0.765 / 0.895 / 0.899 / 0.702 / 0.435 / 0.839 / 0.766 / 0.640 / 0.739 Ours (Joint-Traini -->

**EN** Table 4: Ablation study on the degradation perception task between multi-task and single-task training. Jointly training with score regression improves the accuracy of degradation perception.

**ZH** 表 4：退化感知任务上多任务训练与单任务训练的消融研究。与分数回归联合训练可提升退化感知的准确率。

<!-- [原子块 · table] Method Metrics Noise Blur JPEG Darken Null Average Ours (Degradation-Only) Deg. Acc. 0.9867 0.9268 0.9685 0.8805 0.5702 0.8960 Lev. Acc. 0.4343 0.3951 0.3108 0.2567 - 0.3492 Ours (Joint-Training) Deg. -->

**EN** 4.3 Distortion Perception

**ZH** 4.3 失真感知

**EN** We further evaluate Q-Insight on the distortion perception task, comparing it with AgenticIR [75], which fine-tunes an MLLM to perform a similar distortion prediction function. The comparative results are presented in Tab. 2. Notably, AgenticIR requires sequential queries for each possible distortion type, whereas Q-Insight identifies distortion types using only a single query. Q-Insight consistently outperforms AgenticIR across nearly all distortion categories, resulting in significantly higher average accuracy. However, for the “null” category (no distortion), our performance is slightly lower than AgenticIR, possibly because the reasoning mechanism of Q-Insight is more sensitive to the presence of potential distortions. Overall, these results highlight Q-Insight’s ability to efficiently and accurately perceive image distortions through a concise and unified reasoning framework.

**ZH** 我们进一步在失真感知任务上评估 Q-Insight，并与 AgenticIR [75] 对比——后者通过微调 MLLM 来实现类似的失真预测功能，对比结果见表 2。值得注意的是，AgenticIR 需要对每种可能的失真类型依次查询，而 Q-Insight 仅需一次查询即可识别失真类型。Q-Insight 在几乎所有失真类别上持续优于 AgenticIR，平均准确率显著更高。但在“null”（无失真）类别上，我们的性能略低于 AgenticIR，可能因为 Q-Insight 的推理机制对潜在失真的存在更为敏感。总体而言，这些结果说明 Q-Insight 能通过简洁统一的推理框架高效、准确地感知图像失真。

<!-- [原子块 · img]  -->

**EN** Figure 4: Image comparison reasoning results of our Q-Insight and DepictQA [60]. Q-Insight outperforms DepictQA in comprehensive content understanding and accurate degradation perception.

**ZH** 图 4：Q-Insight 与 DepictQA [60] 的图像比较推理结果。Q-Insight 在全面的内容理解与准确的退化感知上优于 DepictQA。

**EN** 4.4 Ablation Studies

**ZH** 4.4 消融实验

**EN** Effect of multi-task training. To validate the effectiveness of multi-task training, we compare our jointly trained Q-Insight model with two single-task variants, each trained independently on a single task. The comparison results are presented in Tabs. 3 and 4. As shown in Tab. 3, the jointly trained Q-Insight significantly outperforms the score-only variant on nearly all datasets, especially on datasets involving synthetic distortions (KADID [22], CSIQ [20]) and those containing model-generated distortions (PIPAL [14]). This demonstrates that incorporating the degradation perception task can effectively enhance performance in the score regression task. Fig. A in the appendix further presents the benefits of multi-task training, showing that Q-Insight can precisely identify detailed degradations such as pixel-level artifacts, thereby improving overall accuracy in quality assessment. Similarly, Tab. 4 indicates that in the degradation perception task, our jointly trained model consistently surpasses the degradation-only variant across all distortion types. This suggests that the score regression task also positively contributes to degradation perception capabilities. These experimental results verify the mutual benefit and effectiveness of the proposed multi-task training strategy. Moreover, our findings clearly show that the visual quality understanding potential of MLLMs can be significantly improved through carefully designed training tasks and learning objectives.

**ZH** 多任务训练的作用。为验证多任务训练的有效性，我们把联合训练的 Q-Insight 与两个单任务变体（各自在单一任务上独立训练）做比较，结果见表 3 与表 4。如表 3 所示，联合训练的 Q-Insight 在几乎所有数据集上显著优于仅用分数的变体，在含合成失真的数据集（KADID [22]、CSIQ [20]）与含模型生成失真的数据集（PIPAL [14]）上尤为突出。这说明引入退化感知任务能有效提升分数回归任务的性能。附录图 A 进一步展示了多任务训练的收益：Q-Insight 能精确识别像素级伪影等细微退化，从而提升质量评估的整体准确率。类似地，表 4 显示，在退化感知任务上，我们的联合训练模型在所有失真类型上均持续优于仅做退化感知的变体，说明分数回归任务也对退化感知能力有正向贡献。这些实验结果验证了所提多任务训练策略的互惠性与有效性。此外，我们的发现清楚地表明，通过精心设计的训练任务与学习目标，MLLM 的视觉质量理解潜力可以得到显著释放。

**EN** Ablation on the score threshold ⟦SLOT_87⟧. Introducing the threshold allows the model’s predictions to vary within an acceptable margin. Tab. B in the appendix reports the ablation results for different choices of ⟦SLOT_88⟧. Q-Insight consistently achieves robust and stable performance across various threshold values, demonstrating that its effectiveness does not depend on careful tuning of ⟦SLOT_89⟧.

**ZH** 分数阈值 ⟦SLOT_87⟧ 的消融。引入阈值可让模型的预测在可接受的余量内浮动。附录表 B 报告了 ⟦SLOT_88⟧ 取不同值时的消融结果。Q-Insight 在各种阈值下都保持稳健、稳定的性能，说明其有效性并不依赖对 ⟦SLOT_89⟧ 的精细调节。

**EN** Table 5: Accuracy and PLCC / SRCC results of the reference-based comparison task on the SRbench [6]. Reg-Acc and Gen-Acc represent the accuracy between regression-based and generation-based restoration methods, respectively. Q-Insight outperforms score- and description-based methods.

**ZH** 表 5：在 SRbench [6] 上基于参考的比较任务的准确率与 PLCC / SRCC 结果。Reg-Acc 与 Gen-Acc 分别表示在基于回归的重建方法与基于生成的重建方法上的准确率。Q-Insight 优于基于分数与基于描述的方法。

<!-- [原子块 · table] Category Method Reg-Acc Gen-Acc Overall-Acc PLCC SRCC Score-Based PSNR 80.07% 41.70% 34.70% – – SSIM [ 50 ] (TIP 04) 83.00% 45.30% 37.40% – – LPIPS [ 66 ] (CVPR 18) 82.00% 63.90% 65.80% – – A-FINE [ 6 -->

**EN** 4.5 Image Comparison Reasoning

**ZH** 4.5 图像比较推理

**EN** Our Q-Insight effectively generalizes to zero-shot image comparison reasoning tasks in both reference-based and non-reference-based scenarios, as illustrated in Figs. 1 and 4. Specifically, Fig. 1 shows a reference-based comparison scenario, where the reference image is of lower quality, and Images A and B are outputs generated by two different super-resolution methods. Fig. 4 demonstrates Q-Insight’s superiority over DepictQA [60], highlighting its enhanced content understanding and precise perception of degradations. These examples illustrate Q-Insight’s robust generalization ability, largely enabled by its RL-based framework and multi-task training strategy.

**ZH** 如图 1 与图 4 所示，我们的 Q-Insight 能有效零样本泛化到基于参考与非基于参考的图像比较推理任务。具体而言，图 1 展示了基于参考的比较场景：参考图像质量较低，图像 A 与 B 是两种不同超分辨率方法生成的结果。图 4 则展示了 Q-Insight 相对 DepictQA [60] 的优势，凸显其更强的内容理解与更精准的退化感知。这些例子说明 Q-Insight 具备稳健的泛化能力，这主要得益于其基于 RL 的框架与多任务训练策略。

**EN** Furthermore, the comparison reasoning performance can be further boosted by training on a small number of labeled comparison pairs using reinforcement learning. Specifically, we randomly sample 5k data pairs from the DiffIQA [6] dataset, where each pair is labeled only with comparison results, without any textual descriptions. Results are shown in Tab. 5. Our Q-Insight consistently surpasses all score-based and description-based methods in terms of overall accuracy and PLCC/SRCC metrics, demonstrating its promising applicability to various image enhancement tasks. Notably, even the zero-shot version of Q-Insight substantially outperforms DepictQA [60], despite the latter relying on large-scale textual datasets. Additionally, A-Fine [6] utilizes more than 200k data pairs collected from four different datasets, combined with a complex three-stage training pipeline, thus requiring over 40 times more data and considerable effort to develop optimal training strategies. In contrast, Q-Insight achieves superior performance through relatively straightforward yet highly effective visual reinforcement learning. Further details and additional results are provided in Sec. C of the Appendix.

**ZH** 此外，用少量带标签的比较对做强化学习训练，还能进一步提升比较推理性能。具体而言，我们从 DiffIQA [6] 数据集中随机采样 5k 个数据对，每对仅标注比较结果，不含任何文本描述。结果如表 5 所示。我们的 Q-Insight 在总体准确率与 PLCC/SRCC 指标上持续超越所有基于分数与基于描述的方法，展现出其在各类图像增强任务上的应用前景。值得注意的是，即便是零样本版本的 Q-Insight 也大幅优于 DepictQA [60]，尽管后者依赖大规模文本数据集。此外，A-Fine [6] 使用了从四个不同数据集收集的 200k 余个数据对，并配合复杂的三阶段训练流程，所需数据量超过我们 40 倍，还需投入大量精力设计最优训练策略；相比之下，Q-Insight 通过相对直接却极为有效的视觉强化学习取得了更优性能。更多细节与补充结果见附录 C 节。

**EN** 5 Conclusion

**ZH** 5 结论

**EN** In this paper, we introduce Q-Insight, a novel GRPO-based model for comprehensive image quality understanding. It jointly optimizes score regression and degradation perception tasks using only a limited amount of labeled data. Unlike traditional methods that rely on extensive textual annotations or purely numerical scoring, our framework combines numerical accuracy with interpretative reasoning, significantly improving the perceptual analysis capabilities of image quality models. Extensive experiments show that Q-Insight consistently outperforms existing state-of-the-art methods across various datasets and tasks, demonstrating impressive zero-shot generalization and superior comparison reasoning capability. Looking ahead, Q-Insight can extend its capabilities to a wide range of tasks, such as image aesthetic assessments, and serve as a powerful discriminative signal to improve image enhancement models. As a unified model for scoring, perception, comparison, and reasoning, Q-Insight can act as a central hub, coordinating image reconstruction tools and providing valuable insights into the enhancement process. This integrated and automated system has the potential to revolutionize image quality understanding and enhancement, providing a unified solution that can transform how image quality is evaluated, improved, and applied across various fields.

**ZH** 本文提出 Q-Insight，一个基于 GRPO 的新型模型，用于全面的图像质量理解。它仅需有限的标注数据，即可联合优化分数回归与退化感知任务。与依赖大量文本标注或纯数值评分的传统方法不同，本框架把数值准确性与可解释的推理结合起来，显著提升了图像质量模型的感知分析能力。大量实验表明，Q-Insight 在各数据集与任务上持续优于现有最优方法，展现出令人印象深刻的零样本泛化能力与优异的比较推理能力。展望未来，Q-Insight 可把能力拓展到更广泛的任务，如图像美学评估，并可作为强大的判别信号来改进图像增强模型。作为一个集评分、感知、比较与推理于一体的统一模型，Q-Insight 能够充当中枢，协调各类图像重建工具，并为增强过程提供有价值的洞见。这一集成化、自动化的系统有望变革图像质量理解与增强，提供统一的解决方案，改变各领域中图像质量的评估、改进与应用方式。

**EN** Limitations. While achieving promising performance, Q-Insight focuses primarily on natural images. Extending to AI-generated images and videos remains essential and is reserved for future exploration.

**ZH** 局限性。尽管性能可观，Q-Insight 目前主要聚焦自然图像。拓展到 AI 生成图像与视频仍然必要，我们将留待未来探索。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] [1] Shuai Bai, Keqin Chen, Xuejing Liu, Jialin Wang, Wenbin Ge, Sibo Song, Kai Dang, Peng Wang, Shijie Wang, Jun Tang, et al. Qwen2.5-vl technical report. arXiv preprint arXiv:2502.13923 , 2025. -->

<!-- [原子块 · verbatim] [2] Yuntao Bai, Saurav Kadavath, Sandipan Kundu, Amanda Askell, Jackson Kernion, Andy Jones, Anna Chen, Anna Goldie, Azalia Mirhoseini, Cameron McKinnon, et al. Constitutional ai: Harmlessness from ai -->

<!-- [原子块 · verbatim] [3] Sebastian Bosse, Dominique Maniry, Klaus-Robert Müller, Thomas Wiegand, and Wojciech Samek. Deep neural networks for no-reference and full-reference image quality assessment. IEEE Transactions on  -->

<!-- [原子块 · verbatim] [4] Yue Cao, Zhaolin Wan, Dongwei Ren, Zifei Yan, and Wangmeng Zuo. Incorporating semi-supervised and positive-unlabeled learning for boosting full reference image quality assessment. In Proceedings o -->

<!-- [原子块 · verbatim] [5] Chaofeng Chen, Sensen Yang, Haoning Wu, Liang Liao, Zicheng Zhang, Annan Wang, Wenxiu Sun, Qiong Yan, and Weisi Lin. Q-ground: Image quality grounding with large multi-modality models. In Proceedi -->

<!-- [原子块 · verbatim] [6] Du Chen, Tianhe Wu, Kede Ma, and Lei Zhang. Toward generalized image quality assessment: Relaxing the perfect reference quality assumption. In Proceedings of the IEEE/CVF Conference on Computer Vi -->

<!-- [原子块 · verbatim] [7] Paul F Christiano, Jan Leike, Tom Brown, Miljan Martic, Shane Legg, and Dario Amodei. Deep reinforcement learning from human preferences. Proceedings of the Advances in Neural Information Processi -->

<!-- [原子块 · verbatim] [8] Prafulla Dhariwal and Alexander Nichol. Diffusion models beat gans on image synthesis. Proceedings of the Advances in Neural Information Processing Systems (NeurIPS) , 34:8780–8794, 2021. -->

<!-- [原子块 · verbatim] [9] Keyan Ding, Yi Liu, Xueyi Zou, Shiqi Wang, and Kede Ma. Locally adaptive structure and texture similarity for image quality assessment. In Proceedings of the ACM International Conference on Multim -->

<!-- [原子块 · verbatim] [10] Keyan Ding, Kede Ma, Shiqi Wang, and Eero P Simoncelli. Image quality assessment: Unifying structure and texture similarity. IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI) -->

<!-- [原子块 · verbatim] [11] Yuming Fang, Hanwei Zhu, Yan Zeng, Kede Ma, and Zhou Wang. Perceptual quality assessment of smartphone photography. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recogn -->

<!-- [原子块 · verbatim] [12] Deepti Ghadiyaram and Alan C Bovik. Live in the wild image quality challenge database. Online: http://live. ece. utexas. edu/research/ChallengeDB/index. html [Mar, 2017] , 2015. -->

<!-- [原子块 · verbatim] [13] Abhijay Ghildyal and Feng Liu. Shift-tolerant perceptual similarity metric. In Proceedings of the European Conference on Computer Vision (ECCV) , pages 91–107. Springer, 2022. -->

<!-- [原子块 · verbatim] [14] Jinjin GU, Haoming Cai, Haoyu Chen, Xiaoxing Ye, Ren Jimmy S, and Chao Dong. Pipal: a large-scale image quality assessment dataset for perceptual image restoration. In Proceedings of the European -->

<!-- [原子块 · verbatim] [15] Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al. Deepseek-r1: Incentivizing reasoning capability in llms via reinforce -->

<!-- [原子块 · verbatim] [16] Vlad Hosu, Hanhe Lin, Tamas Sziranyi, and Dietmar Saupe. Koniq-10k: An ecologically valid database for deep learning of blind image quality assessment. IEEE Transactions on Image Processing (TIP) -->

<!-- [原子块 · verbatim] [17] Binyuan Hui, Jian Yang, Zeyu Cui, Jiaxi Yang, Dayiheng Liu, Lei Zhang, Tianyu Liu, Jiajun Zhang, Bowen Yu, Keming Lu, et al. Qwen2.5-coder technical report. arXiv preprint arXiv:2409.12186 , 2024 -->

<!-- [原子块 · verbatim] [18] Le Kang, Peng Ye, Yi Li, and David Doermann. Convolutional neural networks for no-reference image quality assessment. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Reco -->

<!-- [原子块 · verbatim] [19] Junjie Ke, Qifei Wang, Yilin Wang, Peyman Milanfar, and Feng Yang. Musiq: Multi-scale image quality transformer. In Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)  -->

<!-- [原子块 · verbatim] [20] Eric C Larson and Damon M Chandler. Most apparent distortion: full-reference image quality assessment and the role of strategy. Journal of Electronic Imaging , 19(1):011006–011006, 2010. -->

<!-- [原子块 · verbatim] [21] Chunyi Li, Zicheng Zhang, Haoning Wu, Wei Sun, Xiongkuo Min, Xiaohong Liu, Guangtao Zhai, and Weisi Lin. Agiqa-3k: An open database for ai-generated image quality assessment. IEEE Transactions on -->

<!-- [原子块 · verbatim] [22] Hanhe Lin, Vlad Hosu, and Dietmar Saupe. Kadid-10k: A large-scale artificially distorted iqa database. In Proceedings of International Conference on Quality of Multimedia Experience (QoMEX) , pag -->

<!-- [原子块 · verbatim] [23] Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. Visual instruction tuning. Proceedings of the Advances in Neural Information Processing Systems (NeurIPS) , 36:34892–34916, 2023. -->

<!-- [原子块 · verbatim] [24] Xialei Liu, Joost Van De Weijer, and Andrew D Bagdanov. Rankiqa: Learning from rankings for no-reference image quality assessment. In Proceedings of the IEEE/CVF International Conference on Compu -->

<!-- [原子块 · verbatim] [25] Ziyu Liu, Zeyi Sun, Yuhang Zang, Xiaoyi Dong, Yuhang Cao, Haodong Duan, Dahua Lin, and Jiaqi Wang. Visual-rft: Visual reinforcement fine-tuning. arXiv preprint arXiv:2503.01785 , 2025. -->

<!-- [原子块 · verbatim] [26] Ilya Loshchilov and Frank Hutter. Decoupled weight decay regularization. arXiv preprint arXiv:1711.05101 , 2017. -->

<!-- [原子块 · verbatim] [27] Chao Ma, Chih-Yuan Yang, Xiaokang Yang, and Ming-Hsuan Yang. Learning a no-reference quality metric for single-image super-resolution. Computer Vision and Image Understanding , 158:1–16, 2017. -->

<!-- [原子块 · verbatim] [28] Anish Mittal, Anush Krishna Moorthy, and Alan Conrad Bovik. No-reference image quality assessment in the spatial domain. IEEE Transactions on Image Processing (TIP) , 21(12):4695–4708, 2012. -->

<!-- [原子块 · verbatim] [29] Anish Mittal, Rajiv Soundararajan, and Alan C Bovik. Making a “completely blind” image quality analyzer. IEEE Signal Processing Letters , 20(3):209–212, 2012. -->

<!-- [原子块 · verbatim] [30] Anush Krishna Moorthy and Alan Conrad Bovik. A two-step framework for constructing blind image quality indices. IEEE Signal Processing Letters , 17(5):513–516, 2010. -->

<!-- [原子块 · verbatim] [31] Anush Krishna Moorthy and Alan Conrad Bovik. Blind image quality assessment: From natural scene statistics to perceptual quality. IEEE Transactions on Image Processing (TIP) , 20(12):3350–3364, 2 -->

<!-- [原子块 · verbatim] [32] Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. Training language models to follow instructio -->

<!-- [原子块 · verbatim] [33] Da Pan, Ping Shi, Ming Hou, Zefeng Ying, Sizhe Fu, and Yuan Zhang. Blind predicting similar quality map for image quality assessment. In Proceedings of the IEEE/CVF Conference on Computer Vision  -->

<!-- [原子块 · verbatim] [34] Jiazhen Pan, Che Liu, Junde Wu, Fenglin Liu, Jiayuan Zhu, Hongwei Bran Li, Chen Chen, Cheng Ouyang, and Daniel Rueckert. Medvlm-r1: Incentivizing medical reasoning capability of vision-language m -->

<!-- [原子块 · verbatim] [35] Nikolay Ponomarenko, Lina Jin, Oleg Ieremeiev, Vladimir Lukin, Karen Egiazarian, Jaakko Astola, Benoit Vozel, Kacem Chehdi, Marco Carli, Federica Battisti, and C.-C. Jay Kuo. Image database tid20 -->

<!-- [原子块 · verbatim] [36] Ekta Prashnani, Hong Cai, Yasamin Mostofi, and Pradeep Sen. Pieapp: Perceptual image-error assessment through pairwise preference. In Proceedings of the IEEE/CVF Conference on Computer Vision and -->

<!-- [原子块 · verbatim] [37] Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, and Björn Ommer. High-resolution image synthesis with latent diffusion models. In Proceedings of the IEEE/CVF Conference on Comput -->

<!-- [原子块 · verbatim] [38] Michele A Saad, Alan C Bovik, and Christophe Charrier. Blind image quality assessment: A natural scene statistics approach in the dct domain. IEEE Transactions on Image Processing (TIP) , 21(8):3 -->

<!-- [原子块 · verbatim] [39] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. arXiv preprint arXiv:1707.06347 , 2017. -->

<!-- [原子块 · verbatim] [40] Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li, Y Wu, et al. Deepseekmath: Pushing the limits of mathematical reasoning in open langua -->

<!-- [原子块 · verbatim] [41] H Sheikh. Live image quality assessment database release 2. http://live. ece. utexas. edu/research/quality , 2005. -->

<!-- [原子块 · verbatim] [42] Hamid R Sheikh and Alan C Bovik. Image information and visual quality. IEEE Transactions on Image Processing (TIP) , 15(2):430–444, 2006. -->

<!-- [原子块 · verbatim] [43] David Silver, Julian Schrittwieser, Karen Simonyan, Ioannis Antonoglou, Aja Huang, Arthur Guez, Thomas Hubert, Lucas Baker, Matthew Lai, Adrian Bolton, et al. Mastering the game of go without hum -->

<!-- [原子块 · verbatim] [44] Shaolin Su, Qingsen Yan, Yu Zhu, Cheng Zhang, Xin Ge, Jinqiu Sun, and Yanning Zhang. Blindly assess image quality in the wild guided by a self-adaptive hyper network. In Proceedings of the IEEE/C -->

<!-- [原子块 · verbatim] [45] Simeng Sun, Tao Yu, Jiahua Xu, Wei Zhou, and Zhibo Chen. Graphiqa: Learning distortion graph representations for blind image quality assessment. IEEE Transactions on Multimedia (TMM) , 25:2912–29 -->

<!-- [原子块 · verbatim] [46] Zhiqing Sun, Sheng Shen, Shengcao Cao, Haotian Liu, Chunyuan Li, Yikang Shen, Chuang Gan, Liang-Yan Gui, Yu-Xiong Wang, Yiming Yang, et al. Aligning large multimodal models with factually augment -->

<!-- [原子块 · verbatim] [47] Hossein Talebi and Peyman Milanfar. Nima: Neural image assessment. IEEE Transactions on Image Processing (TIP) , 27(8):3998–4011, 2018. -->

<!-- [原子块 · verbatim] [48] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, et al. Llama: Open and efficient fo -->

<!-- [原子块 · verbatim] [49] Jianyi Wang, Kelvin CK Chan, and Chen Change Loy. Exploring clip for assessing the look and feel of images. In Proceedings of the AAAI Conference on Artificial Intelligence (AAAI) , volume 37, pa -->

<!-- [原子块 · verbatim] [50] Zhou Wang, Alan C Bovik, Hamid R Sheikh, and Eero P Simoncelli. Image quality assessment: from error visibility to structural similarity. IEEE Transactions on Image Processing (TIP) , 13(4):600–6 -->

<!-- [原子块 · verbatim] [51] Haoning Wu, Zicheng Zhang, Erli Zhang, Chaofeng Chen, Liang Liao, Annan Wang, Chunyi Li, Wenxiu Sun, Qiong Yan, Guangtao Zhai, et al. Q-bench: A benchmark for general-purpose foundation models on -->

<!-- [原子块 · verbatim] [52] Haoning Wu, Zicheng Zhang, Erli Zhang, Chaofeng Chen, Liang Liao, Annan Wang, Kaixin Xu, Chunyi Li, Jingwen Hou, Guangtao Zhai, et al. Q-instruct: Improving low-level visual abilities for multi-m -->

<!-- [原子块 · verbatim] [53] Haoning Wu, Zicheng Zhang, Weixia Zhang, Chaofeng Chen, Liang Liao, Chunyi Li, Yixuan Gao, Annan Wang, Erli Zhang, Wenxiu Sun, et al. Q-align: Teaching LMMs for visual scoring via discrete text-d -->

<!-- [原子块 · verbatim] [54] Haoning Wu, Hanwei Zhu, Zicheng Zhang, Erli Zhang, Chaofeng Chen, Liang Liao, Chunyi Li, Annan Wang, Wenxiu Sun, Qiong Yan, et al. Towards open-ended visual quality comparison. In Proceedings of  -->

<!-- [原子块 · verbatim] [55] An Yang, Beichen Zhang, Binyuan Hui, Bofei Gao, Bowen Yu, Chengpeng Li, Dayiheng Liu, Jianhong Tu, Jingren Zhou, Junyang Lin, et al. Qwen2.5-math technical report: Toward mathematical expert mode -->

<!-- [原子块 · verbatim] [56] Sidi Yang, Tianhe Wu, Shuwei Shi, Shanshan Lao, Yuan Gong, Mingdeng Cao, Jiahao Wang, and Yujiu Yang. Maniqa: Multi-dimension attention network for no-reference image quality assessment. In Proce -->

<!-- [原子块 · verbatim] [57] Huaiyuan Ying, Shuo Zhang, Linyang Li, Zhejian Zhou, Yunfan Shao, Zhaoye Fei, Yichuan Ma, Jiawei Hong, Kuikun Liu, Ziyi Wang, et al. Internlm-math: Open math large language models toward verifiab -->

<!-- [原子块 · verbatim] [58] Zhiyuan You, Xin Cai, Jinjin Gu, Tianfan Xue, and Chao Dong. Teaching large language models to regress accurate image quality scores using score distribution. In Proceedings of the IEEE/CVF Confe -->

<!-- [原子块 · verbatim] [59] Zhiyuan You, Jinjin Gu, Zheyuan Li, Xin Cai, Kaiwen Zhu, Chao Dong, and Tianfan Xue. Descriptive image quality assessment in the wild. arXiv preprint arXiv:2405.18842 , 2024. -->

<!-- [原子块 · verbatim] [60] Zhiyuan You, Zheyuan Li, Jinjin Gu, Zhenfei Yin, Tianfan Xue, and Chao Dong. Depicting beyond scores: Advancing image quality assessment through multi-modal language models. In Proceedings of the -->

<!-- [原子块 · verbatim] [61] Tianyu Yu, Yuan Yao, Haoye Zhang, Taiwen He, Yifeng Han, Ganqu Cui, Jinyi Hu, Zhiyuan Liu, Hai-Tao Zheng, Maosong Sun, et al. Rlhf-v: Towards trustworthy mllms via behavior alignment from fine-gr -->

<!-- [原子块 · verbatim] [62] Tianyu Yu, Haoye Zhang, Yuan Yao, Yunkai Dang, Da Chen, Xiaoman Lu, Ganqu Cui, Taiwen He, Zhiyuan Liu, Tat-Seng Chua, et al. Rlaif-v: Aligning mllms through open-source ai feedback for super gpt- -->

<!-- [原子块 · verbatim] [63] Jingyi Zhang, Jiaxing Huang, Huanjin Yao, Shunyu Liu, Xikun Zhang, Shijian Lu, and Dacheng Tao. R1-vl: Learning to reason with multimodal large language models via step-wise group relative policy -->

<!-- [原子块 · verbatim] [64] Lin Zhang, Lei Zhang, and Alan C Bovik. A feature-enriched completely blind image quality evaluator. IEEE Transactions on Image Processing (TIP) , 24(8):2579–2591, 2015. -->

<!-- [原子块 · verbatim] [65] Lin Zhang, Lei Zhang, Xuanqin Mou, and David Zhang. Fsim: A feature similarity index for image quality assessment. IEEE Transactions on Image Processing (TIP) , 20(8):2378–2386, 2011. -->

<!-- [原子块 · verbatim] [66] Richard Zhang, Phillip Isola, Alexei A Efros, Eli Shechtman, and Oliver Wang. The unreasonable effectiveness of deep features as a perceptual metric. In Proceedings of the IEEE/CVF Conference on  -->

<!-- [原子块 · verbatim] [67] Yuxiang Zhang, Shangxi Wu, Yuqi Yang, Jiangming Shu, Jinlin Xiao, Chao Kong, and Jitao Sang. o1-coder: an o1 replication for coding. arXiv preprint arXiv:2412.00154 , 2024. -->

<!-- [原子块 · verbatim] [68] Zicheng Zhang, Ziheng Jia, Haoning Wu, Chunyi Li, Zijian Chen, Yingjie Zhou, Wei Sun, Xiaohong Liu, Xiongkuo Min, Weisi Lin, et al. Q-bench-video: Benchmarking the video quality understanding of  -->

<!-- [原子块 · verbatim] [69] Zicheng Zhang, Tengchuan Kou, Shushi Wang, Chunyi Li, Wei Sun, Wei Wang, Xiaoyu Li, Zongyu Wang, Xuezhi Cao, Xiongkuo Min, et al. Q-eval-100k: Evaluating visual quality and alignment level for te -->

<!-- [原子块 · verbatim] [70] Zicheng Zhang, Haoning Wu, Ziheng Jia, Weisi Lin, and Guangtao Zhai. Teaching lmms for image quality scoring and interpreting. arXiv preprint arXiv:2503.09197 , 2025. -->

<!-- [原子块 · verbatim] [71] Zhiyuan Zhao, Bin Wang, Linke Ouyang, Xiaoyi Dong, Jiaqi Wang, and Conghui He. Beyond hallucinations: Enhancing lvlms through hallucination-aware direct preference optimization. arXiv preprint ar -->

<!-- [原子块 · verbatim] [72] Heliang Zheng, Huan Yang, Jianlong Fu, Zheng-Jun Zha, and Jiebo Luo. Learning conditional knowledge distillation for degraded-reference image quality assessment. In Proceedings of the IEEE/CVF In -->

<!-- [原子块 · verbatim] [73] Hancheng Zhu, Leida Li, Jinjian Wu, Weisheng Dong, and Guangming Shi. Metaiqa: Deep meta-learning for no-reference image quality assessment. In Proceedings of the IEEE/CVF Conference on Computer  -->

<!-- [原子块 · verbatim] [74] Hanwei Zhu, Haoning Wu, Yixuan Li, Zicheng Zhang, Baoliang Chen, Lingyu Zhu, Yuming Fang, Guangtao Zhai, Weisi Lin, and Shiqi Wang. Adaptive image quality assessment via teaching large multimodal -->

<!-- [原子块 · verbatim] [75] Kaiwen Zhu, Jinjin Gu, Zhiyuan You, Yu Qiao, and Chao Dong. An intelligent agentic system for complex image restoration problems. Proceedings of the International Conference on Learning Represent -->

**EN** Appendix A Designed Prompts

**ZH** 附录 A 设计的提示

**EN** The prompts designed for each task are detailed in Tab. A. Specifically, a general system prompt is shared across tasks, which encourages the model to explicitly output its reasoning process and provide structured responses. This general prompt is supplemented by task-specific prompts tailored for score regression and degradation perception, respectively. For the score regression task, the input includes a task-specific prompt and the image to be rated, with the Mean Opinion Score (MOS) serving as the ground-truth. In the degradation perception task, the input consists of a prompt and an image characterized by a specific distortion class and severity level. We define five distortion categories: “noise”, “blur”, “JPEG”, “darken”, and “null”, where “null” indicates no distortion. Each distortion type has five severity levels: “slight”, “moderate”, “obvious”, “serious”, and “catastrophic”. The distortion class and corresponding severity level constitute the ground-truth labels. Additionally, for the comparative reasoning scenario, the inputs include a prompt, two images to be compared, and an optional reference image.

**ZH** 各任务设计的提示详见表 A。具体而言，所有任务共享一个通用系统提示，用于鼓励模型显式输出推理过程并给出结构化回答；在该通用提示之外，还分别为分数回归与退化感知设计了任务特定提示。对于分数回归任务，输入包括任务特定的提示与待评分的图像，以平均意见分数（MOS）作为真值。对于退化感知任务，输入包括提示与一幅具有特定失真类别与严重程度等级的图像。我们定义五类失真：“noise”“blur”“JPEG”“darken”与“null”，其中“null”表示无失真。每种失真类型有五个严重程度等级：“slight”“moderate”“obvious”“serious”与“catastrophic”。失真类别与相应的严重程度等级共同构成真值标签。此外，在比较推理场景下，输入包括一个提示、两幅待比较的图像以及一幅可选的参考图像。

**EN** Table A: Prompts for Different Tasks. The system prompt is shared across all tasks, while task-specific prompts are additionally designed for each individual task.

**ZH** 表 A：不同任务的提示。系统提示为所有任务共享，此外还为每个具体任务设计了任务特定提示。

<!-- [原子块 · table] System Prompt: A conversation between User and Assistant. The user asks a question, and the Assistant solves it. The assistant first thinks about the reasoning process in the mind and then provides th -->

**EN** Appendix B More Results of Ablation Studies

**ZH** 附录 B 消融研究的更多结果

**EN** B.1 Ablation study of the threshold ⟦SLOT_90⟧

**ZH** B.1 阈值 ⟦SLOT_90⟧ 的消融研究

**EN** When the difference between the model’s predicted score and the ground-truth score is less than ⟦SLOT_91⟧, the model receives the score reward, enabling predictions to fluctuate within an acceptable range. The ablation study on the threshold ⟦SLOT_92⟧ is presented in Tab. B in the following. Q-Insight consistently achieves robust and stable performance across various choices of ⟦SLOT_93⟧, demonstrating that its effectiveness does not rely on meticulous tuning of the threshold.

**ZH** 当模型预测分数与真值分数之差小于 ⟦SLOT_91⟧ 时，模型获得分数奖励，使预测可在可接受范围内浮动。阈值 ⟦SLOT_92⟧ 的消融研究见下表 B。Q-Insight 在 ⟦SLOT_93⟧ 的各种取值下都保持稳健、稳定的性能，说明其有效性并不依赖对阈值的精细调节。

**EN** Table B: Ablation study on the threshold ⟦SLOT_94⟧ for the score regression task. Q-Insight demonstrates robust and stable performance, indicating it does not require careful tuning of the threshold ⟦SLOT_95⟧.

**ZH** 表 B：分数回归任务中阈值 ⟦SLOT_94⟧ 的消融研究。Q-Insight 表现出稳健、稳定的性能，说明无需精细调节阈值 ⟦SLOT_95⟧。

<!-- [原子块 · table] Method KonIQ SPAQ KADID PIPAL LiveW AGIQA CSIQ ϵ = 0.15 \epsilon=0.15 0.918/0.900 0.903/ 0.903 0.749 /0.744 0.443/0.441 0.876/0.847 0.835 /0.764 0.857/0.793 ϵ = 0.25 \epsilon=0.25 0.929/0.911 0.902/0. -->

**EN** B.2 Effect of multi-task training

**ZH** B.2 多任务训练的作用

**EN** In the main paper, we have quantitatively demonstrated the mutual benefits derived from multi-task training. Here, we further illustrate the effectiveness of our multi-task approach qualitatively in Fig. A. Specifically, multi-task training enables Q-Insight to better perceive detailed degradations such as pixel-level artifacts, thereby improving its overall accuracy in image quality assessment.

**ZH** 在主文中，我们已定量展示了多任务训练带来的互惠收益。这里我们在图 A 中进一步定性说明多任务方法的有效性：多任务训练使 Q-Insight 能更好地感知像素级伪影等细微退化，从而提升其在图像质量评估中的整体准确率。

<!-- [原子块 · img]  -->

**EN** Figure A: Subjective ablation comparison between joint multi-task training and w/o joint training on the explanation of image scoring. With joint training, our method can better perceive degradation cues in images (such as pixelated appearance), thereby improving the accuracy of quality assessment.

**ZH** 图 A：联合多任务训练与无联合训练在图像打分解释上的主观消融对比。经联合训练后，本方法能更好地感知图像中的退化线索（如像素化外观），从而提升质量评估的准确率。

**EN** Appendix C Experimental Setups and More Results of Comparison Reasoning

**ZH** 附录 C 实验设置与比较推理的更多结果

**EN** C.1 Datasets

**ZH** C.1 数据集

**EN** For training, we use the DiffIQA [6] dataset, which contains approximately 180k reference–test image pairs generated by applying diffusion-based enhancement methods to reference images of varying quality. Each reference image is paired with multiple test images, and human annotators provide preference labels through triplet-based comparisons, resulting in roughly 180k comparison pairs. Notably, A-Fine [6] aggregates datasets from DiffIQA, TID2013 [35], KADID [22], and PIPAL [14], totaling over 200k comparison pairs for training. In contrast, we randomly sample only 5k pairs from DiffIQA for our training.

**ZH** 训练方面，我们使用 DiffIQA [6] 数据集，它包含约 180k 个参考—测试图像对，由对不同质量的参考图像施加基于扩散的增强方法生成。每个参考图像配有多张测试图像，标注者通过三元组比较给出偏好标签，最终形成约 180k 个比较对。值得注意的是，A-Fine [6] 汇总了来自 DiffIQA、TID2013 [35]、KADID [22] 与 PIPAL [14] 的数据集，训练用比较对总计超过 200k；相比之下，我们仅从 DiffIQA 中随机采样 5k 对用于训练。

**EN** For evaluation, we adopt SRIQA-Bench [6], a benchmark specifically designed to evaluate the generalization ability of IQA models in real-world super-resolution (SR) scenarios. This dataset includes 100 low-resolution (LR) reference images, each enhanced by 10 distinct SR methods encompassing both regression-based and generative models. Human raters perform exhaustive pairwise comparisons within each image group, with each comparison annotated by at least 10 annotators to ensure reliability. Since no ground-truth high-resolution reference images are provided, models must evaluate perceptual quality based solely on the degraded LR images. Thus, SRIQA-Bench poses a challenging scenario to rigorously assess the robustness of full-reference IQA models under imperfect reference conditions. we report Reg-Acc, Gen acc, and overall ACC, which denote pairwise ranking accuracy on regression-based SR methods, generation-based SR methods, and all SR outputs, respectively. These metrics measure alignment between model predictions and human judgments under varying super-resolution styles and distortion characteristics. We also report the PLCC and SRCC of Description-based methods.

**ZH** 评估方面，我们采用 SRIQA-Bench [6]，这是专为评估 IQA 模型在真实超分辨率（SR）场景下泛化能力而设计的基准。该数据集包含 100 张低分辨率（LR）参考图像，每张由 10 种不同的 SR 方法增强，涵盖基于回归与基于生成的两类模型。评分者在每个图像组内进行穷尽的成对比较，每次比较至少由 10 名标注者标注，以保证可靠性。由于不提供真值高分辨率参考图像，模型必须仅凭退化的 LR 图像评估感知质量。因此，SRIQA-Bench 构造了一个具有挑战性的场景，用以严格考察全参考 IQA 模型在参考不完美条件下的鲁棒性。我们报告 Reg-Acc、Gen-Acc 与总体 ACC，分别表示在基于回归的 SR 方法、基于生成的 SR 方法以及全部 SR 输出上的成对排序准确率。这些指标衡量在不同超分辨率风格与失真特性下，模型预测与人类判断的一致程度。我们还报告基于描述方法的 PLCC 与 SRCC。

**EN** C.2 Reward Design and Training Details

**ZH** C.2 奖励设计与训练细节

**EN** In the image comparison task, the model is expected to determine which image is superior or if they are comparable. Denote the predicted score of the ⟦SLOT_96⟧-th response as ⟦SLOT_97⟧, we design a comparison reward function ⟦SLOT_98⟧ as follows. The reward value ⟦SLOT_99⟧ for the ⟦SLOT_100⟧-th response is determined by :

**ZH** 在图像比较任务中，模型需要判断哪幅图像更优，或两者是否相当。记第 ⟦SLOT_96⟧ 个回答的预测分数为 ⟦SLOT_97⟧，我们设计比较奖励函数 ⟦SLOT_98⟧ 如下。第 ⟦SLOT_100⟧ 个回答的奖励值 ⟦SLOT_99⟧ 由下式确定：

<!-- [原子块 · table] r comp ( i ) = 1 if ​ res pred ( i ) = res comp , otherwise ​ 0 . r^{(i)}_{\text{comp}}=1\quad\text{if}\ \text{res}^{(i)}_{\text{pred}}=\text{res}_{\text{comp}},~\text{otherwise }0. (7) -->

**EN** Finally, the overall reward of ⟦SLOT_101⟧-th response is calculated as:

**ZH** 最后，第 ⟦SLOT_101⟧ 个回答的总体奖励计算如下：

<!-- [原子块 · table] r ( i ) = r fmt ( i ) + r comp ( i ) , r^{(i)}=r^{(i)}_{\text{fmt}}+r^{(i)}_{\text{comp}}, (8) -->

**EN** where ⟦SLOT_102⟧ is the format reward. For training, we employ AdamW [26] as the optimizer, using an initial learning rate of ⟦SLOT_103⟧ that linearly decays to ⟦SLOT_104⟧ during training. The model is trained for ⟦SLOT_105⟧ epochs with a total batch size of ⟦SLOT_106⟧. Training is completed in approximately ⟦SLOT_107⟧ hours using 16 NVIDIA A100 GPUs.

**ZH** 其中 ⟦SLOT_102⟧ 为格式奖励。训练方面，我们使用 AdamW [26] 作为优化器，初始学习率为 ⟦SLOT_103⟧，在训练中线性衰减至 ⟦SLOT_104⟧。模型训练 ⟦SLOT_105⟧ 个轮次，总批大小为 ⟦SLOT_106⟧。使用 16 张 NVIDIA A100 GPU 约 ⟦SLOT_107⟧ 小时完成训练。

**EN** C.3 More Qualitative Results

**ZH** C.3 更多定性结果

**EN** We provide quantitative results in Tab. 5 in the main paper. Here we present additional qualitative results of reference-based image comparison reasoning in Figs. B, C, D, and E. It can be observed that, despite training on only 5k comparison pairs, Q-Insight surpasses DepictQA [60] by more effectively recognizing subtle image details and distortions, thereby producing more accurate outcomes.

**ZH** 我们在主文表 5 中给出了定量结果，这里在图 B、C、D、E 中补充基于参考的图像比较推理的定性结果。可以看到，尽管仅用 5k 个比较对训练，Q-Insight 凭借更有效地识别细微的图像细节与失真，仍然超越了 DepictQA [60]，产出更准确的结果。

<!-- [原子块 · img]  -->

**EN** Figure B: Reference-based image comparison reasoning results of our Q-Insight and DepictQA [60] on image “online4” from SRBench [6].

**ZH** 图 B：Q-Insight 与 DepictQA [60] 在 SRBench [6] 中“online4”图像上的基于参考的图像比较推理结果。

<!-- [原子块 · img]  -->

**EN** Figure C: Reference-based image comparison reasoning results of our Q-Insight and DepictQA [60] on image “online23” from SRBench [6].

**ZH** 图 C：Q-Insight 与 DepictQA [60] 在 SRBench [6] 中“online23”图像上的基于参考的图像比较推理结果。

<!-- [原子块 · img]  -->

**EN** Figure D: Reference-based image comparison reasoning results of our Q-Insight and DepictQA [60] on image “realworld33” from SRBench [6].

**ZH** 图 D：Q-Insight 与 DepictQA [60] 在 SRBench [6] 中“realworld33”图像上的基于参考的图像比较推理结果。

<!-- [原子块 · img]  -->

**EN** Figure E: Reference-based image comparison reasoning results of our Q-Insight and DepictQA [60] on image “srtest55” from SRBench [6].

**ZH** 图 E：Q-Insight 与 DepictQA [60] 在 SRBench [6] 中“srtest55”图像上的基于参考的图像比较推理结果。
