# VisionReward：面向图像与视频生成的细粒度多维度人类偏好学习

> 原标题：VisionReward: Fine-Grained Multi-Dimensional Human Preference Learning for Image and Video Generation
> 作者：Jiazheng Xu, Yu Huang, Jiale Cheng, Yuanming Yang, Jiajun Xu, Yuan Wang, Wenbo Duan, Shen Yang, Qunlin Jin, Shurun Li, Jiayan Teng, Zhuoyi Yang 等 · arXiv:2412.21059 · 2024-12-30

<!-- [原子块 · verbatim] VisionReward: Fine-Grained Multi-Dimensional Human Preference Learning for Image and Video Generation -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] Visual generative models have achieved remarkable progress in synthesizing photorealistic images and videos, yet aligning their outputs with human preferences across critical dimensions remains a pers -->

**EN** 1Tsinghua University

**ZH** 1清华大学

**EN** 2Z.AI

**ZH** 2Z.AI

**EN** {xjz22, h-y22}@mails.tsinghua.edu.cn, yuxiaod@tsinghua.edu.cn

**ZH** {xjz22, h-y22}@mails.tsinghua.edu.cn, yuxiaod@tsinghua.edu.cn

**EN** Code — https://github.com/THUDM/VisionReward

**ZH** 代码 — https://github.com/THUDM/VisionReward

**EN** 1 Introduction

**ZH** 1 引言

<!-- [原子块 · img]  -->

**EN** Figure 1: Illustration of how VisionReward works for evaluation and optimization of visual generation. a) Evaluation: VisionReward performs comprehensive evaluation through dimension-specific binary visual QA testing, producing human-aligned, fine-grained assessment scores. b) Optimization: VisionReward enable better preference optimization, enhancing multiple key aspects.

**ZH** 图 1：VisionReward 如何用于视觉生成的评测与优化。a）评测：VisionReward 通过面向特定维度的二值视觉问答测试完成综合评估，产出贴合人类的细粒度评分。b）优化：VisionReward 支持更好的偏好优化，在多个关键方面带来提升。

**EN** Visual generative models, including text-to-image (Ding et al. 2021; Ramesh et al. 2021; Saharia et al. 2022; Rombach et al. 2022; Betker et al. 2023; Podell et al. 2023) and text-to-video (Hong et al. 2022; Ho et al. 2022; Villegas et al. 2022; Zheng et al. 2024; Chen et al. 2024a; Yang et al. 2024) generation, have recently experienced rapid developments. Through large-scale pretraining, these models can effectively translate textual descriptions into photorealistic images or temporally coherent videos. To further align them with human preferences, reinforcement learning from human feedback (RLHF) (Ouyang et al. 2022)—initially introduced in large language models—has recently been adapted to visual generation tasks (Xu et al. 2023; He et al. 2024).

**ZH** 视觉生成模型——包括文本到图像（Ding et al. 2021; Ramesh et al. 2021; Saharia et al. 2022; Rombach et al. 2022; Betker et al. 2023; Podell et al. 2023）与文本到视频（Hong et al. 2022; Ho et al. 2022; Villegas et al. 2022; Zheng et al. 2024; Chen et al. 2024a; Yang et al. 2024）生成——近来发展迅速。借助大规模预训练，这些模型能够把文本描述有效地转化为照片级真实的图像或时间连贯的视频。为使它们进一步对齐人类偏好，最初用于大语言模型的人类反馈强化学习（RLHF）（Ouyang et al. 2022）近来被引入视觉生成任务（Xu et al. 2023; He et al. 2024）。

**EN** A key bottleneck in applying RLHF to visual generation lies in developing effective visual reward models. Recent studies (Xu et al. 2023; Kirstain et al. 2023; Wu et al. 2023) have explored training reward models to predict human visual preferences, enabling automatic evaluation and preference optimization for visual generative models. For evaluation, reward models function as automated metrics that quantitatively measure the alignment between generated outputs and human preference criteria (Li et al. 2023). For optimization, reward models identify reliable directions for improving visual generation models. Essentially, they can provide feedback in reinforcement learning or generate preference pairs, thus reducing dependence on human annotation (Black et al. 2023; Fan et al. 2023; Clark et al. 2023).

**ZH** 把 RLHF 应用于视觉生成的关键瓶颈，在于如何构建有效的视觉奖励模型。已有研究（Xu et al. 2023; Kirstain et al. 2023; Wu et al. 2023）探索训练奖励模型来预测人类视觉偏好，从而对视觉生成模型实现自动评测与偏好优化。在评测上，奖励模型充当自动化指标，定量衡量生成结果与人类偏好准则之间的一致性（Li et al. 2023）；在优化上，奖励模型为改进视觉生成模型指明可靠方向。本质上，它们可以在强化学习中提供反馈，或者生成偏好对，从而降低对人类标注的依赖（Black et al. 2023; Fan et al. 2023; Clark et al. 2023）。

**EN** Despite recent progress in reward models (RMs) for visual generation, two primary challenges remain: First, lack of interpretability and risk of unexpected bias. Current RMs for visual generation often suffer from limited interpretability. These models inherently involve complex trade-offs among multiple factors, yet their scoring mechanisms lack transparency regarding how such trade-offs are performed. This opacity raises concerns about potential unexpected biases. Though multimodal LLMs like Gemini (Team et al. 2024) and GPT-4o (Achiam et al. 2023) enhance interpretability through explainable rating rationales, their general-purpose architectures usually underperform specialized black-box models in fine-grained assessments (Chen et al. 2024c). This raises a key dilemma: how to design preference prediction method to be interpretable while maintaining accuracy.

**ZH** 尽管面向视觉生成的奖励模型（RM）近来取得进展，仍存在两个主要挑战。其一，缺乏可解释性，且存在意外偏差的风险。当前的视觉生成 RM 往往可解释性有限：这些模型内在地涉及多个因素之间的复杂权衡，但其打分机制对这些权衡如何进行缺乏透明性，这种不透明引发了人们对潜在意外偏差的担忧。尽管 Gemini（Team et al. 2024）与 GPT-4o（Achiam et al. 2023）等多模态大语言模型通过可解释的评分理由提升了可解释性，其通用架构在细粒度评估上通常仍不及专用黑盒模型（Chen et al. 2024c）。这就提出了一个关键难题：如何设计既具备可解释性、又保持准确性的偏好预测方法。

**EN** Second, lack of effective reward models for video generation. The rapid development of text-to-video generative models has intensified the demand for video reward models. Although image reward models can assess individual frame quality, their frame-level nature inherently neglects essential temporal dependencies in video sequences. While VideoScore (He et al. 2024) has pioneered direct video evaluation through learnable metrics, it still suffers from limitations such as insufficient accuracy in preference prediction and optimization in video generation.

**ZH** 其二，缺少面向视频生成的有效奖励模型。文本到视频生成模型的快速发展，加大了对视频奖励模型的需求。图像奖励模型虽能评估单帧质量，但其帧级本质忽略了视频序列中至关重要的时间依赖。VideoScore（He et al. 2024）率先以可学习指标进行直接的视频评测，却仍存在局限，如偏好预测精度不足、以及在视频生成优化上的不足。

**EN** Contribution. To address these challenges, we propose a general framework VisionReward to build accurate reward models for both image and video generation. VisionReward is trained with two steps: fine-grained visual assessment and interpretable preference learning. First, to capture human visual preferences, we identify nine major dimensions and decouple preferences into 64 fine-grained questions. Second, to ensure interpretable preference learning, we propose to use the classical linear weighting mechanism on the question outcomes. It enables intuitive visualization of each question’s impact.

**ZH** 贡献。为应对这些挑战，我们提出通用框架 VisionReward，用于构建面向图像与视频生成的准确奖励模型。VisionReward 的训练分两步：细粒度视觉评估与可解释的偏好学习。第一步，为捕捉人类视觉偏好，我们识别出九个主要维度，并把偏好解耦为 64 个细粒度问题。第二步，为保证偏好学习的可解释性，我们提出对问题结果使用经典的线性加权机制，从而直观呈现每个问题的影响。

**EN** To apply it as a reward model for visual generation models, we propose a multi-dimensional consistent strategy during preference optimization. The goal of this strategy is to mitigate unintended and unquantifiable biases. Specifically, a pair of visual samples is used for preference optimization (e.g., DPO (Wallace et al. 2024)) only if one sample is consistently preferred over the other across all dimensions.

**ZH** 为将其用作视觉生成模型的奖励模型，我们在偏好优化过程中提出多维度一致性策略。该策略的目标是缓解非预期、不可量化的偏差。具体地，只有当某一视觉样本在所有维度上都一致地优于另一视觉样本时，这一对样本才被用于偏好优化（例如 DPO（Wallace et al. 2024））。

**EN** To summarize, we present VisionReward as a general framework for visual preference learning. Empirically, we show that VisionReward makes the following contributions:

**ZH** 综上，我们提出 VisionReward 作为视觉偏好学习的通用框架。实验表明，VisionReward 具有以下贡献：

**EN** • We design fine-grained multi-dimensional preference annotation and build the most fine-grained dataset which contain 81K samples and 5M binary annotation, which enable the training of VisionReward.

**ZH** • 我们设计了细粒度的多维度偏好标注，并构建了目前最细粒度的数据集，包含 81K 个样本与 5M 条二值标注，使 VisionReward 的训练成为可能。

**EN** • For visual preference prediction, VisionReward achieves state-of-the-art performance across multiple benchmarks, while maintaining interpretability via hierarchical diagnostic QA and explicit linear weighting. For instance, VisionReward outperforms VideoScore (He et al. 2024) by 17.2% in accuracy on preference prediction.

**ZH** • 在视觉偏好预测上，VisionReward 在多个基准上取得当前最优表现，同时通过层次化诊断式问答与显式线性加权保持了可解释性。例如，VisionReward 在偏好预测准确率上比 VideoScore（He et al. 2024）高出 17.2%。

**EN** • For visual generation, VisionReward can serve as an effective reward model for preference optimization (e.g., DPO), significantly enhancing the text-to-image and text-to-video models. For example, video generation models with VisionReward achieve a 31.6% higher pairwise win rate compared to the same models using VideoScore.

**ZH** • 在视觉生成上，VisionReward 可作为偏好优化（如 DPO）的有效奖励模型，显著提升文本到图像与文本到视频模型。例如，使用 VisionReward 的视频生成模型，其成对胜率比使用 VideoScore 的同款模型高出 31.6%。

<!-- [原子块 · table] Dataset Image Video #Samples #Dimensions #Fine-Grained #Annotation ImageReward ( Xu et al. 2023 ) ✓ 9K - - 0.1M Pick-a-Pic ( Kirstain et al. 2023 ) ✓ 38K - - 0.6M HPDv2 ( Wu et al. 2023 ) ✓ 430K - - 0 -->

**EN** Table 1: Comparison of dataset of VisionReward and other datasets.

**ZH** 表 1：VisionReward 数据集与其他数据集的对比。

<!-- [原子块 · object]  -->

**EN** Figure 2: Illustration of fine-grained multi-dimensional design. (Left) For image: 5 dimensions, 18 sub-dimensions, and 61 binary questions. (Right) For video: 9 dimensions, 20 sub-dimensions, and 64 binary questions.

**ZH** 图 2：细粒度多维度设计示意。（左）图像：5 个维度、18 个子维度、61 个二值问题。（右）视频：9 个维度、20 个子维度、64 个二值问题。

<!-- [原子块 · img]  -->

**EN** Figure 3: Overall framework of VisionReward. 1) Fine-grained Visual Assessment: fine-tune multimodal LLM to perform binary visual question-answering through hierarchical dimensions. 2) Interpretable Preference Learning: utilize visual QA outputs to predict preferences through linear weighted summation. 3) Multi-Dimensional Preference Optimization: optimization strategy across multiple dimensions.

**ZH** 图 3：VisionReward 总体框架。1）细粒度视觉评估：微调多模态大语言模型，按层次化维度执行二值视觉问答。2）可解释偏好学习：利用视觉问答输出，通过线性加权求和预测偏好。3）多维度偏好优化：跨多维度进行优化的策略。

**EN** 2 Related Work

**ZH** 2 相关工作

**EN** Reinforcement Learning from Human Feedback (RLHF) (Stiennon et al. 2020; Nakano et al. 2021; Ouyang et al. 2022) refers to optimizing models with reinforcement learning based on human feedback, which is also explored in image and video generation.

**ZH** 人类反馈强化学习（RLHF）（Stiennon et al. 2020; Nakano et al. 2021; Ouyang et al. 2022）指基于人类反馈用强化学习优化模型，在图像与视频生成中同样已有探索。

**EN** Preference Learning for Visual Generation. There are many works learning from human preferences, which collect human annotation for text-to-image (Xu et al. 2023; Kirstain et al. 2023; Wu et al. 2023) and text-to-video (He et al. 2024). Note that existing approaches (Zhang et al. 2024b; Liang et al. 2024) have attempted to augment human annotations or expand dimensions of human preferences in visual generation. Different from them, VisionReward defines fine-grained multi-dimensional human preferences with the goal of disentangling distinct factors to decouple human preferences, to build more accurate and interpretable RM.

**ZH** 面向视觉生成的偏好学习。许多工作从人类偏好中学习，为文本到图像（Xu et al. 2023; Kirstain et al. 2023; Wu et al. 2023）与文本到视频（He et al. 2024）收集人工标注。已有方法（Zhang et al. 2024b; Liang et al. 2024）尝试扩充人工标注或扩展视觉生成中人类偏好的维度。与之不同，VisionReward 定义细粒度的多维度人类偏好，目标是解耦不同因素，从而构建更准确、更可解释的奖励模型。

**EN** RLHF for Visual Generation. For visual generation tasks, several works have explored RLHF, optimizing from the gradient (Xu et al. 2023; Wu et al. 2024) or using a policy-based RL approach (Black et al. 2023; Fan et al. 2023; Clark et al. 2023). All these methods require a reward model (RM) to provide feedback for online learning. Diffusion-DPO (Wallace et al. 2024) has proposed to optimize the diffusion model directly using human-labeled preference data. However, most RLHF methods face the issue of biased-optimization. By employing a multi-dimensional method, VisionReward achieves robust RLHF.

**ZH** 面向视觉生成的 RLHF。在视觉生成任务上，若干工作探索了 RLHF：或从梯度直接优化（Xu et al. 2023; Wu et al. 2024），或采用基于策略的强化学习方法（Black et al. 2023; Fan et al. 2023; Clark et al. 2023）。这些方法都需要一个奖励模型（RM）为在线学习提供反馈。Diffusion-DPO（Wallace et al. 2024）提出直接用人工标注的偏好数据优化扩散模型。然而多数 RLHF 方法都面临有偏优化的问题。VisionReward 借助多维度方法，实现了稳健的 RLHF。

**EN** Preliminary for Diffusion-DPO. Given a data distribution ⟦SLOT_0⟧, Diffusion models (Sohl-Dickstein et al. 2015; Ho et al. 2020; Song et al. 2020) contains forward process and reverse process. Forward process ⟦SLOT_1⟧ gradually add noise to the data ⟦SLOT_2⟧ and reverse process ⟦SLOT_3⟧ learns transitions to recover data. Training diffusion model can be performed by evidence lower bound (Kingma et al. 2021; Song et al. 2021):

**ZH** Diffusion-DPO 预备知识。给定数据分布 ⟦SLOT_0⟧，扩散模型（Sohl-Dickstein et al. 2015; Ho et al. 2020; Song et al. 2020）包含前向过程与反向过程。前向过程 ⟦SLOT_1⟧ 逐步向数据 ⟦SLOT_2⟧ 加入噪声，反向过程 ⟦SLOT_3⟧ 则学习恢复数据的转移。扩散模型的训练可通过证据下界完成（Kingma et al. 2021; Song et al. 2021）：

<!-- [原子块 · table] L DM = 𝔼 𝒙 0 , ϵ ∼ 𝒩 ⁡ ( 0 , 𝑰 ) , t ​ [ ‖ ϵ − ϵ θ ​ ( 𝒙 t , t ) ‖ 2 2 ] , \displaystyle L_{\mathrm{DM}}=\mathbb{E}_{\boldsymbol{x}_{0},\boldsymbol{\epsilon}\sim\mathcal{N}(0,\boldsymbol{I}),t}\left[\ -->

**EN** with ⟦SLOT_4⟧ and ⟦SLOT_5⟧.

**ZH** 其中 ⟦SLOT_4⟧ 与 ⟦SLOT_5⟧。

**EN** Diffusion-DPO (Wallace et al. 2024) introduces direct preference optimization based on preference pairs. We denote the “win” and “lose” samples as ⟦SLOT_6⟧, and the objective is as follows:

**ZH** Diffusion-DPO（Wallace et al. 2024）在偏好对的基础上引入直接偏好优化。我们把「胜出」与「落败」样本记为 ⟦SLOT_6⟧，其目标如下：

<!-- [原子块 · table] ℒ ⁡ ( θ ) = − 𝔼 t ∼ 𝒰 ⁡ ( 0 , T ) , 𝒙 t w ∼ q ⁡ ( 𝒙 t w ∣ 𝒙 0 w ) , 𝒙 t l ∼ q ⁡ ( 𝒙 t l ∣ 𝒙 0 l ) \displaystyle\mathcal{L}(\theta)=-\mathbb{E}_{t\sim\mathcal{U}(0,T),\boldsymbol{x}_{t}^{w}\sim q\left( -->

**EN** DPO is ordinarily based on overall preference, which may be biased. VisionReward enables Multi-Dimensional Preference Optimization to enhance it.

**ZH** DPO 通常基于整体偏好，这可能带来偏差。VisionReward 通过多维度偏好优化对其加以改进。

**EN** 3 VisionReward

**ZH** 3 VisionReward

**EN** 3.1 VisionReward Annotation

**ZH** 3.1 VisionReward 标注

**EN** Fine-Grained Design. Human preferences are often a result of the interplay of multiple factors (Palmer et al. 2013; Ibarra et al. 2017), necessitating a balance among various considerations. To deconstruct human preferences systematically, we develop a fine-grained multi-dimensional framework, as shown in Table 1 and Fig. 2. For each sub-dimension, we set options that vary gradually in degree, and decompose these options into a series of binary questions (Cf. Tables 15, 16, 17 and 18 in Appendix).

**ZH** 细粒度设计。人类偏好往往是多种因素共同作用的结果（Palmer et al. 2013; Ibarra et al. 2017），需要在各种考量之间取得平衡。为系统性解构人类偏好，我们构建了细粒度的多维度框架，如表 1 与图 2 所示。对每个子维度，我们设置程度递进的选项，并把这些选项拆解为一系列二值问题（参见附录中的表 15、16、17 与 18）。

**EN** Dataset Preparation. For images, we sample images from multiple popular datasets, including ImageRewardDB (Xu et al. 2023), HPDv2 (Wu et al. 2023), and Pick-a-Pic (Kirstain et al. 2023), and obtain 48k images after filtering. For videos, we sample prompts from VidProM (Wang and Yang 2024). To ensure diversity of prompts, we use Rouge-L (Lin 2004) for initial filtering, follow UniFL (Zhang et al. 2024a) to perform a semantic-based filtering, and use ChatGPT (Achiam et al. 2023) for data cleaning, finally get 10k prompts. Then we use CogVideoX (Yang et al. 2024), VideoCrafter2 (Chen et al. 2024a) and OpenSora (Zheng et al. 2024) to generate 30k videos, sample from Panda-70M (Chen et al. 2024b) to get 3k real videos, leading to 33k videos for annotation. More details are provided in Appendix Section 6.1.

**ZH** 数据集准备。图像方面，我们从多个主流数据集中采样，包括 ImageRewardDB（Xu et al. 2023）、HPDv2（Wu et al. 2023）与 Pick-a-Pic（Kirstain et al. 2023），经筛选后得到 48k 张图像。视频方面，我们从 VidProM（Wang and Yang 2024）采样提示词：为保证提示词多样性，先用 Rouge-L（Lin 2004）做初步过滤，再按 UniFL（Zhang et al. 2024a）做基于语义的过滤，并用 ChatGPT（Achiam et al. 2023）做数据清洗，最终得到 10k 条提示词。随后用 CogVideoX（Yang et al. 2024）、VideoCrafter2（Chen et al. 2024a）与 OpenSora（Zheng et al. 2024）生成 30k 个视频，并从 Panda-70M（Chen et al. 2024b）采样得到 3k 个真实视频，合计 33k 个视频用于标注。更多细节见附录第 6.1 节。

**EN** Annotation Management. To avoid bias of annotators, our annotation management includes professional management and standard document. Cooperating with a specialized company, we strictly conduct annotation training for annotators, select qualified annotators, and perform quality inspection of annotation results. Our annotation document gives clear definitions and provides more than 10 examples for each judgment, to align the standard among annotators. Due to these efforts, the consistency of annotators in the binary results reaches 89.29% (images) and 89.33% (videos).

**ZH** 标注管理。为避免标注者的偏差，我们的标注管理包含专业化管理与规范文档。我们与专业公司合作，严格开展标注者培训、筛选合格标注者，并对标注结果进行质量抽检。标注文档给出清晰定义，并为每一类判断提供 10 个以上示例，以统一标注者之间的标准。得益于这些措施，标注者在二值结果上的一致性达到 89.29%（图像）与 89.33%（视频）。

**EN** Annotation Analysis. Through specialized annotation, we obtain an image dataset containing 48k images and 3 million question-answer pairs, while a video dataset with 33k videos and 2 million pairs. More statistical analysis of the annotation results is in Appendix Section 6.2.

**ZH** 标注分析。通过专业化标注，我们得到包含 48k 张图像、300 万问答对的图像数据集，以及包含 33k 个视频、200 万问答对的视频数据集。标注结果的更多统计分析见附录第 6.2 节。

**EN** 3.2 VisionReward Training

**ZH** 3.2 VisionReward 训练

**EN** The complete training process of VisionReward and its application methodology during preference optimization are illustrated in Fig. 3.

**ZH** VisionReward 的完整训练流程及其在偏好优化中的应用方式如图 3 所示。

**EN** Fine-grained Visual Assessment. Specifically, we use CogVLM2 (Hong et al. 2024b) as the base model for image understanding, and CogVLM2-Video (Hong et al. 2024b) as the base model for video understanding. In terms of data, we have obtained millions of annotated binary question-answering pairs. Initially, we performed a balanced sampling on each binary question by addressing the imbalance between positive and negative examples, ensuring a roughly equal number of positive and negative instances associated with each binary question. Then we use balanced instruction tuning dataset consisting of binary questions to fine-tune base VLM.

**ZH** 细粒度视觉评估。具体地，我们使用 CogVLM2（Hong et al. 2024b）作为图像理解的基础模型，使用 CogVLM2-Video（Hong et al. 2024b）作为视频理解的基础模型。数据方面，我们已获得数百万条带标注的二值问答对。首先针对每个二值问题做均衡采样，消除正负样本之间的不平衡，使每个二值问题对应的正负例数量大致相等；随后用由二值问题构成的均衡指令微调数据集对基础视觉语言模型进行微调。

**EN** Interpretable Preference Learning. After trained on fine-grained dataset, VisionReward can be adopt to give a series of binary response answers (“yes” or “no”) ⟦SLOT_7⟧, where ⟦SLOT_8⟧ represents the number of binary questions. We define reward of every binary question as ⟦SLOT_9⟧:

**ZH** 可解释偏好学习。在细粒度数据集上训练完成后，VisionReward 可给出一系列二值回答（“yes” 或 “no”）⟦SLOT_7⟧，其中 ⟦SLOT_8⟧ 表示二值问题的数量。我们把每个二值问题的奖励定义为 ⟦SLOT_9⟧：

<!-- [原子块 · table] x i = 𝟙 [ A i = “yes” ] . \displaystyle x_{i}=\mathds{1}\left[A_{i}=\text{``yes''}\right]. (3) -->

**EN** We construct a feature vector ⟦SLOT_10⟧, and use a set of linear weights ⟦SLOT_11⟧ to obtain the final reward ⟦SLOT_12⟧:

**ZH** 我们构造特征向量 ⟦SLOT_10⟧，并用一组线性权重 ⟦SLOT_11⟧ 得到最终奖励 ⟦SLOT_12⟧：

<!-- [原子块 · table] R = ∑ i = 1 N w i 𝟙 [ A i = “yes” ] . \displaystyle R=\sum_{i=1}^{N}w_{i}\mathds{1}\left[A_{i}=\text{``yes''}\right]. (4) -->

**EN** In order to learn linear weights ⟦SLOT_13⟧, we collect human preferences for pairs of ⟦SLOT_14⟧. Specifically, we compute the feature difference for each pair, given by ⟦SLOT_15⟧, and the corresponding label is assigned as ⟦SLOT_16⟧ or ⟦SLOT_17⟧ depending on the human preference. We then perform logistic regression ⟦SLOT_18⟧ to learn linear weights ⟦SLOT_19⟧:

**ZH** 为学习线性权重 ⟦SLOT_13⟧，我们收集 ⟦SLOT_14⟧ 成对样本上的人类偏好。具体地，我们计算每一对样本的特征差，即 ⟦SLOT_15⟧；对应标签依人类偏好取 ⟦SLOT_16⟧ 或 ⟦SLOT_17⟧。随后通过逻辑回归 ⟦SLOT_18⟧ 学习线性权重 ⟦SLOT_19⟧：

<!-- [原子块 · table] ℒ ⁡ ( W ) = \displaystyle\mathcal{L}(W)= − 𝔼 [ y log ( σ ( Δ X W T ) ) \displaystyle-\mathbb{E}\left[y\log\left(\sigma(\Delta XW^{T})\right)\right. + ( 1 − y ) log ( 1 − σ ( Δ X W T ) ) ] . \displayst -->

**EN** By calculating dimension-specific scores through intra-dimensional weighting, VisionReward facilitates multi-dimensional preference prediction. We note dimensions as ⟦SLOT_20⟧ where ⟦SLOT_21⟧ contains questions belonging to the dimension. Then we define reward for certain dimension as:

**ZH** 通过维度内加权计算各维度得分，VisionReward 可实现多维度偏好预测。我们把维度记为 ⟦SLOT_20⟧，其中 ⟦SLOT_21⟧ 包含属于该维度的问题。于是某一维度的奖励定义为：

<!-- [原子块 · table] R ( dim k ) = ∑ i ∈ dim k w i 𝟙 [ A i = “yes” ] . \displaystyle R({\text{dim}_{k}})=\sum_{i\in\text{dim}_{k}}w_{i}\mathds{1}\left[A_{i}=\text{``yes''}\right]. (6) -->

**EN** 3.3 Multi-Dimensional Preference Optimization

**ZH** 3.3 多维度偏好优化

**EN** To empirically validate the model’s capacity, we leverage Direct Preference Optimization (DPO) (Wallace et al. 2024) for Diffusion Models in our experiments, where VisionReward generates multi-dimensional preference pairs to guide the optimization process while maintaining inter-dimensional balance.

**ZH** 为实证检验模型能力，我们在实验中采用面向扩散模型的直接偏好优化（DPO）（Wallace et al. 2024），由 VisionReward 生成多维度偏好对来引导优化过程，同时保持维度间的平衡。

<!-- [原子块 · object]  -->

**EN** (a) Data analysis.

**ZH** （a）数据分析。

<!-- [原子块 · object]  -->

**EN** (b) DPO analysis.

**ZH** （b）DPO 分析。

**EN** Figure 4: (a) We sample 10,000 human preference pairs from Pick-a-Pic dataset and analyze score deviations across 18 sub-dimensions (represented by the average yes-proportion of checklist questions within each sub-dimension). (b) We show score deviations for images generated by SDXL after Diffusion-DPO, using the same 10,000 prompts.

**ZH** 图 4：（a）我们从 Pick-a-Pic 数据集中采样 10,000 个人类偏好对，并分析 18 个子维度上的分数偏差（以每个子维度内检查清单问题的 yes 比例均值表示）。（b）我们给出 SDXL 经 Diffusion-DPO 后生成图像的分数偏差，使用同样的 10,000 条提示词。

**EN** Challenges. We replicate the Diffusion-DPO training procedure using SDXL (Podell et al. 2023) on the Pick-a-Pic (Kirstain et al. 2023) dataset, employing VisionReward for comprehensive data analysis and model evaluation. As demonstrated in Fig. 4, both the preference data and optimized model exhibit biases across several fine-grained dimensions. These findings not only underscore VisionReward’s capability for fine-grained analysis but also emphasize the necessity for optimization approaches that account for multi-dimensional representation.

**ZH** 挑战。我们在 Pick-a-Pic（Kirstain et al. 2023）数据集上用 SDXL（Podell et al. 2023）复现 Diffusion-DPO 训练流程，并采用 VisionReward 进行全面的数据分析与模型评测。如图 4 所示，偏好数据与优化后的模型在若干细粒度维度上都表现出偏差。这些发现既证明了 VisionReward 的细粒度分析能力，也说明优化方法必须考虑多维度表示。

**EN** MPO: Insight and Solution. Compared to ordinary DPO method which select pairs using overall preference, we propose MPO-enhanced DPO that take account fine-grained multi-dimensional preference. For reward of two samples ⟦SLOT_22⟧ and ⟦SLOT_23⟧, we define ⟦SLOT_24⟧ as dominating ⟦SLOT_25⟧ if ⟦SLOT_26⟧ holds for every dimension ⟦SLOT_27⟧. The key differences between the MPO strategy and standard DPO are:

**ZH** MPO：思路与方案。普通 DPO 方法依据整体偏好筛选样本对，我们则提出 MPO 增强的 DPO，把细粒度的多维度偏好纳入考量。对于两个样本 ⟦SLOT_22⟧ 与 ⟦SLOT_23⟧ 的奖励，若对每个维度 ⟦SLOT_27⟧ 都满足 ⟦SLOT_26⟧，我们定义 ⟦SLOT_24⟧ 支配 ⟦SLOT_25⟧。MPO 策略与标准 DPO 的关键区别在于：

**EN** • Ordinary DPO: During DPO optimization, we directly select the pair based on the total reward ⟦SLOT_28⟧.

**ZH** • 普通 DPO：在 DPO 优化中，直接依据总奖励 ⟦SLOT_28⟧ 选择样本对。

**EN** • MPO-enhanced DPO: MPO strategy introduces an additional constraint: we only select pairs that ⟦SLOT_29⟧ dominates ⟦SLOT_30⟧, then proceed with standard DPO.

**ZH** • MPO 增强的 DPO：MPO 策略引入了额外约束，只选择满足 ⟦SLOT_29⟧ 支配 ⟦SLOT_30⟧ 的样本对，然后再执行标准 DPO。

**EN** We analyze the effects of MPO in Section 4.3. The MPO strategy can also be applied to other algorithms, which we leave for future exploration.

**ZH** 我们在第 4.3 节分析 MPO 的效果。MPO 策略也可应用于其他算法，这部分留待未来探索。

**EN** Method Image Video HPDv2 MonetBench GenAI-Bench MonetBench tau∗ diff∗∗ tau diff tau diff task-specific discriminative models ImageReward (Xu et al. 2023) 74.0 48.8 56.5 48.4 72.1 55.8 58.4 PickScore (Kirstain et al. 2023) 79.8 49.8 57.6 52.4 75.4 57.7 61.6 HPSv2 (Wu et al. 2023) 83.3 48.4 55.6 49.3 73.0 59.3 62.5 MPS (Zhang et al. 2024b) 83.5 44.2 50.7 46.9 67.6 55.8 58.9 generative models GPT-4o (Achiam et al. 2023) 77.5 38.9 52.7 41.8 54.3 45.7 48.3 Gemini (Team et al. 2024) 60.7 27.4 55.1 46.9 61.7 52.2 56.8 VQAScore (Lin et al. 2025) 69.7 49.4 56.5 45.2 68.0 56.1 59.5 VideoScore (He et al. 2024) 76.8 45.8 52.5 47.8 71.4 49.1 54.9 VisionReward (Ours) 81.7 51.8 59.5 51.8 74.4 64.0 72.1

**ZH** 方法 图像 视频 HPDv2 MonetBench GenAI-Bench MonetBench tau∗ diff∗∗ tau diff tau diff 任务专用判别式模型 ImageReward (Xu et al. 2023) 74.0 48.8 56.5 48.4 72.1 55.8 58.4 PickScore (Kirstain et al. 2023) 79.8 49.8 57.6 52.4 75.4 57.7 61.6 HPSv2 (Wu et al. 2023) 83.3 48.4 55.6 49.3 73.0 59.3 62.5 MPS (Zhang et al. 2024b) 83.5 44.2 50.7 46.9 67.6 55.8 58.9 生成式模型 GPT-4o (Achiam et al. 2023) 77.5 38.9 52.7 41.8 54.3 45.7 48.3 Gemini (Team et al. 2024) 60.7 27.4 55.1 46.9 61.7 52.2 56.8 VQAScore (Lin et al. 2025) 69.7 49.4 56.5 45.2 68.0 56.1 59.5 VideoScore (He et al. 2024) 76.8 45.8 52.5 47.8 71.4 49.1 54.9 VisionReward（ ours）81.7 51.8 59.5 51.8 74.4 64.0 72.1

**EN** Table 2: Preference accuracy on multiple dataset. Bold denotes the best score within the generative models, while underline signifies the best score among all categories. Tau∗ means taking account of ties (Deutsch et al. 2023), and diff∗∗ means dropping ties in labels (we drop ties both in labels and responses for GPT-4o and Gemini in diff∗∗ because too many ties are given by them).

**ZH** 表 2：在多个数据集上的偏好准确率。粗体表示生成式模型中的最优分数，下划线表示所有类别中的最优分数。Tau∗ 表示考虑并列情形（Deutsch et al. 2023），diff∗∗ 表示丢弃标签中的并列（由于 GPT-4o 与 Gemini 给出了过多并列，我们在 diff∗∗ 中同时丢弃标签与回答中的并列）。

**EN** 4 Experiments

**ZH** 4 实验

**EN** 4.1 VisionReward for Text-to-Vision Evaluation

**ZH** 4.1 VisionReward 用于文本到视觉评测

**EN** Dataset & Training Setting. After balanced sampling, we obtain 40,743 images and corresponding 97,680 judgment questions for training, leaving 6,910 images for subsequent validation and test. For videos, we obtain 28,605 videos and corresponding 89,473 judgment questions for training, with 3,080 videos reserved.

**ZH** 数据集与训练设置。经均衡采样后，我们得到 40,743 张图像及相应的 97,680 条判断问题用于训练，留出 6,910 张图像用于后续验证与测试。视频方面，我们得到 28,605 个视频及相应的 89,473 条判断问题用于训练，并保留 3,080 个视频。

**EN** To fine-tune CogVLM2 (Hong et al. 2024b), we set a batch size of 64, a learning rate of 1e-6, and train for 1,500 steps. For CogVLM-Video, we set a batch size of 64, a learning rate of 4e-6, and train for 1,500 steps.

**ZH** 微调 CogVLM2（Hong et al. 2024b）时，批大小设为 64、学习率设为 1e-6，训练 1,500 步。微调 CogVLM-Video 时，批大小设为 64、学习率设为 4e-6，训练 1,500 步。

**EN** To learn linear weights for preference prediction, we sample human preference pairs and perform logistic regression. For images, We sample 44k pairs (24k from HPDv2 (Wu et al. 2023) and 20k from ImageRewardDB (Xu et al. 2023)); and for videos, we sample prompts from VidProM (Wang and Yang 2024) and generate videos (using CogVideoX (Yang et al. 2024), VideoCrafter2 (Chen et al. 2024a) and OpenSora (Zheng et al. 2024)), getting 1,795 annotated video pairs with preference.

**ZH** 为学习用于偏好预测的线性权重，我们采样人类偏好对并执行逻辑回归。图像方面，我们采样 44k 对（其中 24k 来自 HPDv2（Wu et al. 2023），20k 来自 ImageRewardDB（Xu et al. 2023））；视频方面，我们从 VidProM（Wang and Yang 2024）采样提示词并生成视频（使用 CogVideoX（Yang et al. 2024）、VideoCrafter2（Chen et al. 2024a）与 OpenSora（Zheng et al. 2024）），得到 1,795 个带偏好标注的视频对。

<!-- [原子块 · object]  -->

**EN** Figure 5: The accuracy of VisionReward on GenAI-Bench improves as the number of binary questions increases. After masking weights from full regression, VisionReward maintains high performance.

**ZH** 图 5：VisionReward 在 GenAI-Bench 上的准确率随二值问题数量增加而提升。在对完整回归得到的权重做掩码之后，VisionReward 仍保持较高性能。

<!-- [原子块 · img]  -->

**EN** Figure 6: Human evaluation results of DPO using different reward models or preference datasets. We require five annotators to comprehensively evaluate two samples and select the better one. VisionReward achieve the best performance.

**ZH** 图 6：使用不同奖励模型或偏好数据集时 DPO 的人工评测结果。我们要求五名标注者对两个样本进行综合评估并选出更优者。VisionReward 取得最佳表现。

**EN** To establish a comprehensive evaluation benchmark for both image and video generation, we construct MonetBench, which contains separate test sets for images and videos, each consisting of 1,000 prompts. More details are introduced in Appendix Section 12.

**ZH** 为建立覆盖图像与视频生成的综合评测基准，我们构建了 MonetBench，其中包含图像与视频两个独立的测试集，各含 1,000 条提示词。更多细节见附录第 12 节。

**EN** Main Results: Preference Accuracy. Preference accuracy means the probability that a reward model has the same judgment as humans about which image is better. We use MonetBench to construct our test set for human preference, using SDXL (Podell et al. 2023) to generate images and CogVideoX (Yang et al. 2024) / VideoCrafter2 (Chen et al. 2024a) / OpenSora (Zheng et al. 2024) to generate videos, resulting in 500 pairs for image and 1,000 pairs for video. We employ annotators to assess the generated images using a preference rating scale from 1 to 5 (with 3 indicating no preference). The average preference score is used as the final preference label. We also take HPDv2 (Wu et al. 2023) and GenAI-Bench (Jiang et al. 2024) as test set.

**ZH** 主要结果：偏好准确率。偏好准确率指奖励模型在判断哪张图像更好时与人类做出相同判断的概率。我们用 MonetBench 构建人类偏好测试集：用 SDXL（Podell et al. 2023）生成图像，用 CogVideoX（Yang et al. 2024）/ VideoCrafter2（Chen et al. 2024a）/ OpenSora（Zheng et al. 2024）生成视频，得到 500 个图像对与 1,000 个视频对。我们请标注者用 1 到 5 的偏好评分量表评估生成的图像（3 表示无偏好），并以平均偏好分数作为最终偏好标签。我们还把 HPDv2（Wu et al. 2023）与 GenAI-Bench（Jiang et al. 2024）作为测试集。

**EN** Table 2 shows that VisionReward obtains state-of-the-state results in multiple datasets. Notably, in video evaluation, image reward models demonstrate competitive performance when the video duration is within 2 seconds (GenAI-Bench). However, when the video duration reaches 6 seconds (MonetBench), only VisionReward is capable of accurately predicting human preference, being twice (22.1% over random) as high as the best (12.5% over random) among other methods. This indicates that dynamic information in longer videos poses a challenge for RMs, while VisionReward can effectively address this issue after fine-grained visual learning.

**ZH** 表 2 显示，VisionReward 在多个数据集上取得了当前最优的结果。其中，在视频评测中，当视频时长在 2 秒以内（GenAI-Bench）时，图像奖励模型表现出具有竞争力的性能；然而当视频时长达到 6 秒（MonetBench）时，只有 VisionReward 能够准确预测人类偏好，其相对随机的提升（22.1%）是其他方法中最好者（12.5%）的两倍。这说明较长视频中的动态信息对奖励模型构成了挑战，而 VisionReward 经细粒度视觉学习后能够有效应对这一问题。

**EN** Ablation Study: Scalability of Question Scale. Fig. 5 shows that accuracy of preference prediction exhibits significant improvement as the question scale increases, and masking minimal weights maintains performance (Details in Appendix Section 7). Scalability validates the effects of decomposing preferences via fine-grained questions. We do more analysis of VisionReward in Appendix Section 7 and analysis of fine-grained results in Section 10.

**ZH** 消融实验：问题规模的可扩展性。图 5 显示，偏好预测准确率随问题规模增大而显著提升，且对最小权重做掩码仍能保持性能（详见附录第 7 节）。这种可扩展性验证了通过细粒度问题分解偏好的效果。我们在附录第 7 节给出了对 VisionReward 的更多分析，并在第 10 节给出细粒度结果的分析。

**EN** 4.2 VisionReward for Preference Optimization

**ZH** 4.2 VisionReward 用于偏好优化

**EN** To evaluate the efficacy of VisionReward in preference optimization for visual generative systems, we conduct a series of comparative experiments against current state-of-the-art reward models and established preference datasets. We use SDXL as text-to-image base model and CogVideoX as text-to-video base model. The empirical results presented in Fig. 6 demonstrate VisionReward’s superior performance, achieving statistically significant improvements in human preference metrics over competing approaches.

**ZH** 为评估 VisionReward 在视觉生成系统偏好优化中的有效性，我们与当前最优的奖励模型以及已有的偏好数据集开展了一系列对比实验。我们以 SDXL 作为文本到图像的基础模型，以 CogVideoX 作为文本到视频的基础模型。图 6 中的实验结果表明，VisionReward 表现更优，在人类偏好指标上相对对比方法取得了统计显著的改进。

**EN** This section focuses on preference optimization for text-to-video using different reward models. Details of text-to-image are provided in Appendix Section 8.2.

**ZH** 本节聚焦使用不同奖励模型时的文本到视频偏好优化，文本到图像的相关细节见附录第 8.2 节。

**EN** Dataset & Training Settings. For our backbone model, we select CogVideoX-2B. The training prompts are sampled from VidProM (Wang and Yang 2024) (details in Appendix Section 8.1). To adapt these prompts for video generation, we have optimized them following guidelines from CogVideoX (Yang et al. 2024), which results in roughly 22,000 samples. We generate 4 videos for each prompt, and use VisionReward to score these videos and apply the MPO strategy to select approximately 9,400 effective preference pairs. In all our experiments, we maintain a batch size of 32, a learning rate of 5e-6, and employ 100 warmup steps followed by linear decay. We set the DPO parameter ⟦SLOT_31⟧ to 500. The MPO training process spans around 500 steps, equivalent to about 2 epochs. During training, we save a checkpoint every 40 steps and use a validation set split from the training set to pick the checkpoint with the highest reward.

**ZH** 数据集与训练设置。骨干模型选用 CogVideoX-2B，训练提示词从 VidProM（Wang and Yang 2024）采样（细节见附录第 8.1 节）。为使这些提示词适配视频生成，我们按 CogVideoX（Yang et al. 2024）给出的指引对其加以优化，最终得到约 22,000 个样本。我们为每个提示词生成 4 个视频，用 VisionReward 为其打分，并应用 MPO 策略筛选出约 9,400 个有效偏好对。所有实验中，批大小固定为 32，学习率为 5e-6，采用 100 步预热后线性衰减。DPO 参数 ⟦SLOT_31⟧ 设为 500。MPO 训练过程约 500 步，相当于约 2 个轮次。训练期间每 40 步保存一次检查点，并用从训练集中划分出的验证集挑选奖励最高的检查点。

**EN** Evaluation Settings. To comprehensively assess the MPO models, we have conducted both automatic and human evaluations. The automatic evaluation is conducted across various benchmarks, including VBench (Huang et al. 2024) and our Video-MonetBench. For VBench, we focus on commonly reported key metrics, including Human Action, Scene, Multiple Objects, and Appearance Style. In all these experiments, we utilize prompt optimization recommended in CogVideoX. Our baseline comparisons include the original CogVideoX-2B and DPO with VideoScore.

**ZH** 评测设置。为全面评估 MPO 模型，我们同时进行了自动评测与人工评测。自动评测在多个基准上开展，包括 VBench（Huang et al. 2024）与我们的 Video-MonetBench。在 VBench 上，我们关注常被引用的关键指标，包括 Human Action、Scene、Multiple Objects 与 Appearance Style。所有实验中都采用了 CogVideoX 推荐的提示词优化。基线对比包括原始 CogVideoX-2B，以及使用 VideoScore 的 DPO。

<!-- [原子块 · table] Methods Action Human Scene Objects Multiple Style Appear. Original 98.20 55.60 68.43 24.20 VideoScore 97.60 56.25 68.66 23.96 VisionReward 98.40 57.57 71.54 24.02 -->

**EN** Table 3: Evaluation results on VBench.

**ZH** 表 3：在 VBench 上的评测结果。

**EN** Experimental Results. The main results are shown in Table 3. When compared to the original CogVideoX-2B, optimization with VisionReward significantly enhances model performance across these benchmarks. In contrast, optimization with VideoScore tends to degrade performance. The empirical evidence substantiates VisionReward’s advanced capacity for multi-dimensional optimization. (Case study in Appendix Section 8.3.)

**ZH** 实验结果。主要结果如表 3 所示。与原始 CogVideoX-2B 相比，用 VisionReward 做优化显著提升了模型在这些基准上的表现；而用 VideoScore 做优化则往往导致性能下降。这些实证结果证明 VisionReward 具备更强的多维度优化能力。（案例研究见附录第 8.3 节。）

**EN** 4.3 Ablation Study of MPO

**ZH** 4.3 MPO 消融实验

**EN** To comprehensively illustrate how MPO addresses the factor optimization bias inherent in DPO, We conduct experiments based on CogVideoX-5B. We set the threshold of the total score to 0.8 for DPO and 0.6 for MPO, ensuring that the number of pairs obtained through all three strategies is 5k. We use a batch size of 64, a learning rate of 2e-6, the DPO parameter ⟦SLOT_32⟧ of 500, and the training steps of 300. VisionReward is employed to evaluate scores across various dimensions, with the detailed results presented in Table 4. Through the implementation of the MPO strategy, CogVideoX is optimized in such a manner that it avoids the degradation of certain factors (e.g., alignment), thereby achieving improved trade-offs, such as maintaining good preservation while avoiding excessively slow dynamic changes. The empirical evidence further substantiates VisionReward’s capacity for algorithm-agnostic preference alignment, as evidenced by comparative testing with other approaches like MaPO (Hong et al. 2024a).

**ZH** 为充分说明 MPO 如何解决 DPO 固有的因素优化偏差，我们基于 CogVideoX-5B 开展实验。我们将总分阈值设为 DPO 用 0.8、MPO 用 0.6，以保证三种策略得到的样本对数量均为 5k。批大小设为 64，学习率为 2e-6，DPO 参数 ⟦SLOT_32⟧ 为 500，训练步数为 300。我们用 VisionReward 评估各维度得分，详细结果见表 4。通过实施 MPO 策略，CogVideoX 的优化方式避免了某些因素（如对齐）的退化，从而实现了更好的权衡，例如在保持良好保真度的同时避免动态变化过于缓慢。实证结果进一步证明 VisionReward 具备与算法无关的偏好对齐能力，这也在与 MaPO（Hong et al. 2024a）等其他方法的对比测试中得到了验证。

<!-- [原子块 · table] Method Align. Quality Dynamic Physics Preserv. Overall Original 1.733 0.660 0.053 0.344 0.653 4.303 DPO 1.697 0.680 0.034 0.356 0.741 4.515 DPO w/ MPO 1.766 0.688 0.042 0.356 0.721 4.573 MaPO 1.736 0. -->

**EN** Table 4: Ablation Study of MPO strategy. Scores are given by VisionReward on MonetBench.

**ZH** 表 4：MPO 策略的消融实验。分数由 VisionReward 在 MonetBench 上给出。

**EN** For efficiency discussion, the experimental results in Table 5 reveal the comparative effectiveness of the MPO and DPO methods. We analyze the pairs selected in perspective of “⟦SLOT_33⟧ dominating ⟦SLOT_34⟧” mentioned in Section 3.3. These results suggest that MPO outperforms the DPO approach in terms of both efficiency and effectiveness. These findings highlight promising directions for future research in developing novel optimization algorithms and adapting VisionReward for multi-dimensional optimization.

**ZH** 关于效率的讨论，表 5 中的实验结果揭示了 MPO 与 DPO 方法的相对有效性。我们从第 3.3 节所述「⟦SLOT_33⟧ 支配 ⟦SLOT_34⟧」的视角分析所选样本对。结果表明，MPO 在效率与效果两方面都优于 DPO。这些发现为未来研究指明了有前景的方向：开发新的优化算法，并将 VisionReward 适配于多维度优化。

<!-- [原子块 · table] Method #Dom. #Not-Dom. Reward Original - - 4.303 DPO w/o MPO 3814 1456 4.515 (+0.212) DPO w/ MPO 5028 0 4.573 (+0.270) Δ \Delta ( vs w/o MPO) +31.8% -100% +27.4% -->

**EN** Table 5: Comparison of MPO and DPO on MonetBench. “#Dom.” means the number of pairs that match the rule of “⟦SLOT_35⟧ dominating ⟦SLOT_36⟧”, while “#Not-Dom.” pairs not match.

**ZH** 表 5：MPO 与 DPO 在 MonetBench 上的比较。“#Dom.” 表示满足「⟦SLOT_35⟧ 支配 ⟦SLOT_36⟧」规则的样本对数量，“#Not-Dom.” 表示不满足的样本对数量。

**EN** 5 Conclusion

**ZH** 5 结论

**EN** We introduce VisionReward, a reward model for visual generation, which is fine-grained and multi-dimensional. By enabling Vision-Language Model (VLM) to perform binary assessments and applying linear summation with weighting coefficients derived from preference learning, VisionReward achieves highly accurate and interpretable. For visual generative optimization, VisionReward surpasses other reward models and enable multi-dimensional strategy.

**ZH** 我们提出 VisionReward——一个面向视觉生成的细粒度、多维度奖励模型。通过让视觉语言模型（VLM）执行二值评估，并对偏好学习得到的权重系数做线性求和，VisionReward 实现了高精度与可解释性。在视觉生成优化上，VisionReward 优于其他奖励模型，并支持多维度策略。

**EN** Acknowledgments

**ZH** 致谢

**EN** This research was supported by Natural Science Foundation of China (NSFC) No. 62276148, NSFC No. 62495063. The authors would like to thank Z.AI for sponsoring the computation resources used in this work.

**ZH** 本研究受到国家自然科学基金（NSFC）No. 62276148 与 NSFC No. 62495063 的资助。作者感谢 Z.AI 为本工作提供计算资源。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] Achiam et al. (2023) J. Achiam, S. Adler, S. Agarwal, L. Ahmad, I. Akkaya, F. L. Aleman, D. Almeida, J. Altenschmidt, S. Altman, S. Anadkat, et al. Gpt-4 technical report . arXiv preprint arXiv:2303.0 -->

<!-- [原子块 · verbatim] Betker et al. (2023) J. Betker, G. Goh, L. Jing, T. Brooks, J. Wang, L. Li, L. Ouyang, J. Zhuang, J. Lee, et al. Improving image generation with better captions . Computer Science. https://cdn. openai -->

<!-- [原子块 · verbatim] Black et al. (2023) K. Black, M. Janner, Y. Du, I. Kostrikov, and S. Levine Training diffusion models with reinforcement learning . arXiv preprint arXiv:2305.13301 . Cited by: §1 , §2 . -->

<!-- [原子块 · verbatim] Chen et al. (2024a) H. Chen, Y. Zhang, X. Cun, M. Xia, X. Wang, C. Weng, and Y. Shan Videocrafter2: overcoming data limitations for high-quality video diffusion models . In Proceedings of the IEEE/CVF -->

<!-- [原子块 · verbatim] Chen et al. (2024b) T. Chen, A. Siarohin, W. Menapace, E. Deyneka, H. Chao, B. E. Jeon, Y. Fang, H. Lee, J. Ren, M. Yang, et al. Panda-70m: captioning 70m videos with multiple cross-modality teachers  -->

<!-- [原子块 · verbatim] Chen et al. (2024c) Z. Chen, Y. Du, Z. Wen, Y. Zhou, C. Cui, Z. Weng, H. Tu, C. Wang, Z. Tong, Q. Huang, et al. MJ-bench: is your multimodal reward model really a good judge for text-to-image generati -->

<!-- [原子块 · verbatim] Clark et al. (2023) K. Clark, P. Vicol, K. Swersky, and D. J. Fleet Directly fine-tuning diffusion models on differentiable rewards . arXiv preprint arXiv:2309.17400 . Cited by: §1 , §2 . -->

<!-- [原子块 · verbatim] Deutsch et al. (2023) D. Deutsch, G. Foster, and M. Freitag Ties matter: meta-evaluating modern metrics with pairwise accuracy and tie calibration . In Proceedings of the 2023 Conference on Empirical  -->

<!-- [原子块 · verbatim] Ding et al. (2021) M. Ding, Z. Yang, W. Hong, W. Zheng, C. Zhou, D. Yin, J. Lin, X. Zou, Z. Shao, H. Yang, et al. Cogview: mastering text-to-image generation via transformers . Advances in Neural Info -->

<!-- [原子块 · verbatim] Fan et al. (2023) Y. Fan, O. Watkins, Y. Du, H. Liu, M. Ryu, C. Boutilier, P. Abbeel, M. Ghavamzadeh, K. Lee, and K. Lee DPOK: reinforcement learning for fine-tuning text-to-image diffusion models . I -->

<!-- [原子块 · verbatim] GLM (2024) T. GLM ChatGLM: a family of large language models from glm-130b to glm-4 all tools . External Links: 2406.12793 , Link Cited by: §12 . -->

<!-- [原子块 · verbatim] He et al. (2024) X. He, D. Jiang, G. Zhang, M. Ku, A. Soni, S. Siu, H. Chen, A. Chandra, Z. Jiang, A. Arulraj, et al. VideoScore: building automatic metrics to simulate fine-grained human feedback for -->

<!-- [原子块 · verbatim] Ho et al. (2022) J. Ho, W. Chan, C. Saharia, J. Whang, R. Gao, A. Gritsenko, et al. Imagen video: high definition video generation with diffusion models . arXiv preprint arXiv:2210.02303 . Cited by: § -->

<!-- [原子块 · verbatim] Ho et al. (2020) J. Ho, A. Jain, and P. Abbeel Denoising diffusion probabilistic models . Advances in neural information processing systems 33 , pp. 6840–6851 . Cited by: §2 . -->

<!-- [原子块 · verbatim] Hong et al. (2024a) J. Hong, S. Paul, N. Lee, K. Rasul, J. Thorne, and J. Jeong Margin-aware preference optimization for aligning diffusion models without reference . arXiv preprint arXiv:2406.06424 . -->

<!-- [原子块 · verbatim] Hong et al. (2022) W. Hong, M. Ding, W. Zheng, X. Liu, and J. Tang Cogvideo: large-scale pretraining for text-to-video generation via transformers . arXiv preprint arXiv:2205.15868 . Cited by: §1 . -->

<!-- [原子块 · verbatim] Hong et al. (2024b) W. Hong, W. Wang, M. Ding, W. Yu, Q. Lv, Y. Wang, Y. Cheng, S. Huang, J. Ji, Z. Xue, et al. Cogvlm2: visual language models for image and video understanding . arXiv preprint arXiv -->

<!-- [原子块 · verbatim] Huang et al. (2024) Z. Huang, Y. He, J. Yu, F. Zhang, C. Si, Y. Jiang, Y. Zhang, T. Wu, Q. Jin, N. Chanpaisit, et al. Vbench: comprehensive benchmark suite for video generative models . In Proceedings -->

<!-- [原子块 · verbatim] Ibarra et al. (2017) F. F. Ibarra, O. Kardan, M. R. Hunter, H. P. Kotabe, F. A. Meyer, and M. G. Berman Image feature types and their predictions of aesthetic preference and naturalness . Frontiers in -->

<!-- [原子块 · verbatim] Jiang et al. (2024) D. Jiang, M. Ku, T. Li, Y. Ni, S. Sun, R. Fan, and W. Chen GenAI arena: an open evaluation platform for generative models . arXiv preprint arXiv:2406.04485 . Cited by: §4.1 . -->

<!-- [原子块 · verbatim] Kingma et al. (2021) D. Kingma, T. Salimans, B. Poole, and J. Ho Variational diffusion models . Advances in neural information processing systems 34 , pp. 21696–21707 . Cited by: §2 . -->

<!-- [原子块 · verbatim] Kirstain et al. (2023) Y. Kirstain, A. Polyak, U. Singer, S. Matiana, J. Penna, and O. Levy Pick-a-pic: an open dataset of user preferences for text-to-image generation . Advances in Neural Informatio -->

<!-- [原子块 · verbatim] Li et al. (2023) C. Li, Z. Zhang, H. Wu, W. Sun, X. Min, X. Liu, G. Zhai, and W. Lin Agiqa-3k: an open database for ai-generated image quality assessment . IEEE Transactions on Circuits and Systems fo -->

<!-- [原子块 · verbatim] Li et al. (2024) F. Li, R. Zhang, H. Zhang, Y. Zhang, B. Li, W. Li, Z. Ma, and C. Li Llava-next-interleave: tackling multi-image, video, and 3d in large multimodal models . arXiv preprint arXiv:2407.0 -->

<!-- [原子块 · verbatim] Liang et al. (2024) Y. Liang, J. He, G. Li, P. Li, A. Klimovskiy, N. Carolan, J. Sun, J. Pont-Tuset, S. Young, F. Yang, et al. Rich human feedback for text-to-image generation . In Proceedings of the  -->

<!-- [原子块 · verbatim] Lin (2004) C. Lin ROUGE: a package for automatic evaluation of summaries . In Text Summarization Branches Out , Barcelona, Spain , pp. 74–81 . External Links: Link Cited by: §12 , §3.1 . -->

<!-- [原子块 · verbatim] Lin et al. (2025) Z. Lin, D. Pathak, B. Li, J. Li, X. Xia, G. Neubig, P. Zhang, and D. Ramanan Evaluating text-to-visual generation with image-to-text generation . In European Conference on Computer V -->

<!-- [原子块 · verbatim] Liu et al. (2023) H. Liu, C. Li, Q. Wu, and Y. J. Lee Visual instruction tuning . NeurIPS . Cited by: Table 10 . -->

<!-- [原子块 · verbatim] Nakano et al. (2021) R. Nakano, J. Hilton, S. Balaji, J. Wu, L. Ouyang, et al. Webgpt: browser-assisted question-answering with human feedback . arXiv preprint arXiv:2112.09332 . Cited by: §2 . -->

<!-- [原子块 · verbatim] Ouyang et al. (2022) L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. Wainwright, P. Mishkin, C. Zhang, S. Agarwal, K. Slama, A. Ray, et al. Training language models to follow instructions with human feedba -->

<!-- [原子块 · verbatim] Palmer et al. (2013) S. E. Palmer, K. B. Schloss, and J. Sammartino Visual aesthetics and human preference . Annual review of psychology 64 ( 1 ), pp. 77–107 . Cited by: §3.1 . -->

<!-- [原子块 · verbatim] Podell et al. (2023) D. Podell, Z. English, K. Lacey, A. Blattmann, T. Dockhorn, J. Müller, J. Penna, and R. Rombach Sdxl: improving latent diffusion models for high-resolution image synthesis . arXiv -->

<!-- [原子块 · verbatim] Radford et al. (2021) A. Radford, J. W. Kim, C. Hallacy, A. Ramesh, G. Goh, S. Agarwal, G. Sastry, A. Askell, P. Mishkin, J. Clark, et al. Learning transferable visual models from natural language sup -->

<!-- [原子块 · verbatim] Ramesh et al. (2021) A. Ramesh, M. Pavlov, G. Goh, S. Gray, C. Voss, A. Radford, M. Chen, and I. Sutskever Zero-shot text-to-image generation . In International conference on machine learning , pp. 88 -->

<!-- [原子块 · verbatim] Rombach et al. (2022) R. Rombach, A. Blattmann, D. Lorenz, P. Esser, and B. Ommer High-resolution image synthesis with latent diffusion models . In 2022 IEEE/CVF Conference on Computer Vision and Patt -->

<!-- [原子块 · verbatim] Saharia et al. (2022) C. Saharia, W. Chan, S. Saxena, L. Li, J. Whang, E. L. Denton, K. Ghasemipour, et al. Photorealistic text-to-image diffusion models with deep language understanding . Advances in -->

<!-- [原子块 · verbatim] Schuhmann et al. (2022) C. Schuhmann, R. Beaumont, R. Vencu, C. W. Gordon, R. Wightman, et al. LAION-5b: an open large-scale dataset for training next generation image-text models . In Thirty-sixth Co -->

<!-- [原子块 · verbatim] Sohl-Dickstein et al. (2015) J. Sohl-Dickstein, E. Weiss, N. Maheswaranathan, and S. Ganguli Deep unsupervised learning using nonequilibrium thermodynamics . In International conference on machine lea -->

<!-- [原子块 · verbatim] Song et al. (2021) Y. Song, C. Durkan, I. Murray, and S. Ermon Maximum likelihood training of score-based diffusion models . Advances in neural information processing systems 34 , pp. 1415–1428 . Cite -->

<!-- [原子块 · verbatim] Song et al. (2020) Y. Song, J. Sohl-Dickstein, D. P. Kingma, A. Kumar, S. Ermon, and B. Poole Score-based generative modeling through stochastic differential equations . arXiv preprint arXiv:2011.1345 -->

<!-- [原子块 · verbatim] Stiennon et al. (2020) N. Stiennon, L. Ouyang, J. Wu, D. Ziegler, R. Lowe, C. Voss, A. Radford, D. Amodei, and P. F. Christiano Learning to summarize with human feedback . Advances in Neural Informati -->

<!-- [原子块 · verbatim] Team et al. (2024) G. Team, P. Georgiev, V. I. Lei, R. Burnell, L. Bai, et al. Gemini 1.5: unlocking multimodal understanding across millions of tokens of context . arXiv preprint arXiv:2403.05530 . C -->

<!-- [原子块 · verbatim] Villegas et al. (2022) R. Villegas, M. Babaeizadeh, P. Kindermans, H. Moraldo, H. Zhang, M. T. Saffar, S. Castro, J. Kunze, and D. Erhan Phenaki: variable length video generation from open domain text -->

<!-- [原子块 · verbatim] Wallace et al. (2024) B. Wallace, M. Dang, R. Rafailov, L. Zhou, A. Lou, S. Purushwalkam, S. Ermon, C. Xiong, S. Joty, and N. Naik Diffusion model alignment using direct preference optimization . In P -->

<!-- [原子块 · verbatim] Wang and Yang (2024) W. Wang and Y. Yang Vidprom: a million-scale real prompt-gallery dataset for text-to-video diffusion models . arXiv preprint arXiv:2403.06098 . Cited by: §12 , §3.1 , §4.1 , §4.2  -->

<!-- [原子块 · verbatim] Wu et al. (2019) H. Wu, J. Mao, Y. Zhang, Y. Jiang, L. Li, W. Sun, and W. Ma Unified visual-semantic embeddings: bridging vision and language with structured meaning representations . In 2019 IEEE/CVF -->

<!-- [原子块 · verbatim] Wu et al. (2023) X. Wu, Y. Hao, K. Sun, Y. Chen, F. Zhu, R. Zhao, and H. Li Human preference score v2: a solid benchmark for evaluating human preferences of text-to-image synthesis . arXiv preprint ar -->

<!-- [原子块 · verbatim] Wu et al. (2024) X. Wu, Y. Hao, M. Zhang, K. Sun, Z. Huang, G. Song, Y. Liu, and H. Li Deep reward supervisions for tuning text-to-image diffusion models . arXiv preprint arXiv:2405.00760 . Cited by:  -->

<!-- [原子块 · verbatim] Xu et al. (2023) J. Xu, X. Liu, Y. Wu, Y. Tong, Q. Li, M. Ding, J. Tang, and Y. Dong ImageReward: learning and evaluating human preferences for text-to-image generation . In Proceedings of the 37th In -->

<!-- [原子块 · verbatim] Yang et al. (2024) Z. Yang, J. Teng, W. Zheng, M. Ding, S. Huang, J. Xu, Y. Yang, W. Hong, X. Zhang, G. Feng, et al. Cogvideox: text-to-video diffusion models with an expert transformer . arXiv prepri -->

<!-- [原子块 · verbatim] Zhang et al. (2024a) J. Zhang, J. Wu, Y. Ren, X. Xia, H. Kuang, P. Xie, J. Li, X. Xiao, M. Zheng, L. Fu, and G. Li UniFL: improve stable diffusion via unified feedback learning . External Links: 2404. -->

<!-- [原子块 · verbatim] Zhang et al. (2024b) S. Zhang, B. Wang, J. Wu, Y. Li, T. Gao, D. Zhang, and Z. Wang Learning multi-dimensional human preference for text-to-image generation . In Proceedings of the IEEE/CVF Conference -->

<!-- [原子块 · verbatim] Zheng et al. (2024) Open-sora: democratizing efficient video production for all External Links: Link Cited by: §1 , §3.1 , §4.1 , §4.1 , Table 6 . -->

**EN** Appendix

**ZH** 附录

**EN** 6 More Details of Annotation

**ZH** 6 标注的更多细节

**EN** 6.1 Details of Annotation Design

**ZH** 6.1 标注设计细节

**EN** To ensure the diversity of our annotation, we collect our annotated data from various sources, as presented in Table 6. The prompt and example for data cleaning is shown in Table 8. Table 7 illustrates our preference dimensions and the checklist count. We identify 5 dimensions for text-to-image generation and expand to 9 dimensions for text-to-video.

**ZH** 为保证标注的多样性，我们从多种来源采集标注数据，如表 6 所示。数据清洗所用的提示词与示例见表 8。表 7 展示了我们的偏好维度与检查清单条目数。我们为文本到图像生成识别出 5 个维度，并扩展为文本到视频的 9 个维度。

<!-- [原子块 · table] Type Source #Samples #Checklist Image ImageRewardDB ( Xu et al. 2023 ) 16K 1M Pick-a-Pic ( Kirstain et al. 2023 ) 16K 1M HPDv2 ( Wu et al. 2023 ) 16K 1M Video CogVideoX ( Yang et al. 2024 ) 10K 0.6M O -->

**EN** Table 6: Statistics of source data and annotation.

**ZH** 表 6：来源数据与标注的统计。

<!-- [原子块 · table] Dimension #Sub-dimension #Checklist Image Video Image Video Alignment 1 1 1 4 Composition 5 1 13 2 Quality 5 4 14 14 Fidelity 5 3 25 9 Safety&Emotion 2 1 8 4 Stability - 5 - 12 Dynamic - 2 - 8 Physics -->

**EN** Table 7: Taxonomy of annotation for VisionReward.

**ZH** 表 7：VisionReward 的标注分类体系。

<!-- [原子块 · object]  -->

**EN** (a) Text-to-image

**ZH** （a）文本到图像

<!-- [原子块 · object]  -->

**EN** (b) Text-to-video

**ZH** （b）文本到视频

**EN** Figure 7: Annotation statistics of different sub-dimensions.

**ZH** 图 7：各子维度的标注统计。

<!-- [原子块 · table] SYSTEM Assume you are a model responsible for refining and polishing English expressions. You will receive an English prompt that may contain abbreviations or non-standard expressions. Your task is to -->

**EN** Table 8: Prompt template and example for prompt cleaning.

**ZH** 表 8：提示词清洗所用的提示词模板与示例。

**EN** 6.2 Statistics of Annotation Result

**ZH** 6.2 标注结果统计

**EN** Fig. 7 is the statistical results of the labeled data for images and videos. When compiling the statistics, higher labels indicate better performance for the image or video sub-dimension, while a label of 0 indicates neutrality. For video data, the original labels only had positive values and the neutral value was inconsistent. Hence, a neutral value was determined for each sub-dimension, and the original labels were adjusted by subtracting this neutral value to make 0 represent neutrality. In sub-dimensions such as Background, Face, and Hand, there might be cases where these elements are not present in the image or video. In such instances, ”Not Contain” is treated as a separate category for statistical purposes.

**ZH** 图 7 给出了图像与视频标注数据的统计结果。统计时，标签越高表示该图像或视频子维度表现越好，标签 0 表示中性。对于视频数据，原始标签只有正值，中性值也不一致，因此我们为每个子维度确定一个中性值，并将原始标签减去该值，使 0 代表中性。在背景、人脸、手部等子维度上，可能出现图像或视频中并不包含这些元素的情况；此时我们把“Not Contain”作为单独类别进行统计。

**EN** There are two main characteristics to note.

**ZH** 有两个主要特征值得关注。

**EN** • For most sub-dimensions, the distribution of options roughly follows a normal distribution, with the majority being ordinary, and the quantities of instances with extreme characteristics, either very good or very bad, are reduced. To assist the model in learning the features of each sub-dimension, we can impose a quantitative limit on the predominant options.

**ZH** • 对大多数子维度而言，选项分布大致服从正态分布：多数样本表现普通，表现极好或极差的样本数量递减。为帮助模型学习各子维度的特征，我们可以对占主导地位的选项施加数量限制。

**EN** • Certain sub-dimensions, such as the presence of hands, require a mask when predicting human preferences. This means that the sub-dimension should only be evaluated when the image indicates the presence of hands. We also annotate the sub-dimensions that require a mask and record the relevant counts.

**ZH** • 某些子维度（如是否存在手部）在预测人类偏好时需要掩码，即只有当图像表明存在手部时才评估该子维度。我们同样对需要掩码的子维度加以标注，并记录相应的计数。

**EN** 7 More Details and Results of VisionReward

**ZH** 7 VisionReward 的更多细节与结果

**EN** VisionReward comprises two steps: visual judgment and linear regression.

**ZH** VisionReward 包含两个步骤：视觉判断与线性回归。

**EN** Visual Judgment Process. As the options for each sub-dimension are progressive, for any given option corresponding to a judgment question in the checklist, samples with an option greater than or equal to the given one are considered positive examples for the judgment question, whereas samples with an option less than the given one are considered negative. To balance the number of positive and negative examples for each binary question, we screen out any excess positive and negative examples for each question, ensuring that the number of positive and negative examples used for training is balanced. For alignment, we use different methods on images and videos. For images, we use VQAScore (Lin et al. 2025) as an alignment judgment. For videos, we train five levels of judgment for VisionReward.

**ZH** 视觉判断过程。由于每个子维度的选项是递进的，对于检查清单中某个判断问题所对应的选项，选项值大于等于该给定选项的样本被视为该判断问题的正例，选项值小于该给定选项的样本则被视为负例。为平衡每个二值问题的正负例数量，我们筛除每个问题上多余的正例与负例，确保用于训练的正负例数量均衡。在对齐方面，我们对图像与视频采用不同的方法：图像使用 VQAScore（Lin et al. 2025）作为对齐判断；视频则为 VisionReward 训练五个层级的判断。

**EN** Main Results: Accuracy on Judgment. To evaluate the effectiveness of judgment learning, we construct a visual quality QA set to assess the visual assessment capabilities of VisionReward compared to other VLMs. We collect 1,364 test cases for images involving 14 types of questions across 4 dimensions, and additionally 1,308 cases covering 8 types of questions across 4 dimensions related to dynamic content in videos. To ensure the generality of these questions, we combine adjacent degrees in the checklists under each sub-dimension, enhancing distinctiveness and minimizing incidental subjectivity. Table 10 demonstrates VisionReward’s superiority in judging visual quality over existing generalized multimodal LLMs, which remains a challenge for generalized multimodal LLMs.

**ZH** 主要结果：判断准确率。为评估判断学习的有效性，我们构建了视觉质量问答集，用于比较 VisionReward 与其他视觉语言模型的视觉评估能力。我们收集了 1,364 个图像测试用例，涵盖 4 个维度下的 14 类问题；另外收集了 1,308 个与视频动态内容相关的用例，涵盖 4 个维度下的 8 类问题。为保证这些问题的通用性，我们把每个子维度下检查清单中相邻的程度加以合并，以增强区分度并尽量减少偶然的主观性。表 10 显示，VisionReward 在判断视觉质量上优于现有的通用多模态大语言模型，而这对通用多模态大语言模型而言仍是一项挑战。

<!-- [原子块 · table] Composition Quality Fidelity Safety 97.9 98.2 98.3 99.1 Stability Dynamic Physics Preservation 97.4 99.9 88.2 99.8 -->

**EN** Table 9: Consistency of VisionReward in each dimension.

**ZH** 表 9：VisionReward 在各维度上的一致性。

**EN** Main Results: Consistency on Judgment. As questions corresponding to each sub-dimension assess varying degrees of a particular factor, it’s important to measure consistency of VisionReward across multiple questions of the same sub-dimension. Consistency measures the likelihood that the model provides consistent responses across a series of judgments concerning this factor. Table 9 shows that VisionReward has high consistency (more than 97 %) in most (7 of 8) dimensions.

**ZH** 主要结果：判断一致性。由于每个子维度对应的问题评估的是某一因素的不同程度，衡量 VisionReward 在同一子维度多个问题上的一致性就显得重要。一致性衡量的是模型在围绕该因素的一系列判断中给出一致回答的可能性。表 9 显示，VisionReward 在多数（8 个中的 7 个）维度上一致性超过 97%。

**EN** Algorithm 1 Iterative Regression with Weight Masking

**ZH** 算法 1 带权重掩码的迭代回归

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

**EN** Method Image Video Composition Quality Fidelity Safety Stability Dynamic Physics Preservation LLaVa∗ 59.9 65.7 59.8 64.4 52.5 53.8 50.6 47.5 CogVLM2 (Hong et al. 2024b) 65.8 67.1 53.1 74.7 49.3 57.1 51.2 47.8 GPT-4o (Achiam et al. 2023) 73.1 62.7 61.9 70.1 57.9 69.1 62.4 58.8 Gemini (Team et al. 2024) 69.4 59.9 59.7 74.9 58.1 71.1 58.1 59.6 VisionReward (Ours) 78.8 81.1 80.9 83.9 64.8 75.4 68.1 72.0

**ZH** 方法 图像 视频 构图 质量 保真度 安全 稳定性 动态 物理 保持性 LLaVa∗ 59.9 65.7 59.8 64.4 52.5 53.8 50.6 47.5 CogVLM2 (Hong et al. 2024b) 65.8 67.1 53.1 74.7 49.3 57.1 51.2 47.8 GPT-4o (Achiam et al. 2023) 73.1 62.7 61.9 70.1 57.9 69.1 62.4 58.8 Gemini (Team et al. 2024) 69.4 59.9 59.7 74.9 58.1 71.1 58.1 59.6 VisionReward（ ours）78.8 81.1 80.9 83.9 64.8 75.4 68.1 72.0

**EN** Table 10: Accuracy of VisionReward and other vision-language models (VLMs) on vision quality questions constructed from our annotation. ∗We test LLaVA-v1.5-7B (Liu et al. 2023) for image and LLava-Next-Video-34B (Li et al. 2024) for video.

**ZH** 表 10：VisionReward 与其他视觉语言模型（VLM）在我们标注所构建的视觉质量问题上的准确率。∗我们在图像上测试 LLaVA-v1.5-7B（Liu et al. 2023），在视频上测试 LLava-Next-Video-34B（Li et al. 2024）。

**EN** Weight Masking. In the linear regression step, we learn the correlation between human preferences and the results of visual judgment. In our design, if the result of the visual judgment is “yes”, human preference improves. We examine the correlation between human preference and each judgment result, and the numerical results indicate a positive correlation. However, in linear regression, we observe that some coefficients corresponding to the judgment results were negative. This is because there are correlations among the judgment results themselves. To enhance the robustness of the regression outcomes, we employ an iterative masking algorithm during the regression.

**ZH** 权重掩码。在线性回归步骤中，我们学习人类偏好与视觉判断结果之间的相关性。在我们的设计中，若视觉判断结果为“yes”，则人类偏好更高。我们考察了人类偏好与各判断结果之间的相关性，数值结果显示二者呈正相关。然而在线性回归中，我们观察到部分判断结果对应的系数为负，这是因为判断结果之间存在相关性。为提升回归结果的稳健性，我们在回归过程中采用了迭代掩码算法。

**EN** Ablation Study: Impact of Training Set Size. We conduct experiments with varying sizes of the training set to investigate its influence on regression performance. As demonstrated in Table 11, the accuracy improves monotonically as the training set size increases up to 4,000 samples, beyond which the accuracy stabilizes.

**ZH** 消融实验：训练集规模的影响。我们用不同规模的训练集开展实验，考察其对回归性能的影响。如表 11 所示，准确率随训练集规模增大而单调提升，直到 4,000 个样本之后趋于稳定。

<!-- [原子块 · table] Size 200 500 1k 2k 4k 8k Acc. 77.6 80.3 80.6 80.9 81.3 81.3 -->

**EN** Table 11: Accuracy on HPDv2-test for different sizes of train set.

**ZH** 表 11：不同训练集规模下在 HPDv2-test 上的准确率。

**EN** 8 More Details and Results of MPO

**ZH** 8 MPO 的更多细节与结果

**EN** 8.1 Details of Prompt for MPO

**ZH** 8.1 MPO 的提示词细节

**EN** We employ the prompt filtering approach proposed by UniFL (Zhang et al. 2024a) to curate our dataset. This strategy comprises two pivotal steps:

**ZH** 我们采用 UniFL（Zhang et al. 2024a）提出的提示词过滤方法来整理数据集。该策略包含两个关键步骤：

**EN** • Semantic-Based Filtering: Utilizing an existing scene graph parser (Wu et al. 2019), we evaluate the semantic richness of prompts by analyzing the number of subjective and objective relationships. Prompts with fewer than one meaningful relationship are filtered out to reduce noise data.

**ZH** • 基于语义的过滤：利用现有的场景图解析器（Wu et al. 2019），通过分析主客体关系的数量来评估提示词的语义丰富度。有意义关系少于一个的提示词会被过滤掉，以减少噪声数据。

**EN** • Cosine Similarity-Based Selection: Following the semantic filtering process, we apply a cosine similarity-based iterative selection mechanism. By maintaining a maximum similarity threshold of 0.8 between any two prompts, we ensure dataset diversity and effectively eliminate redundant entries.

**ZH** • 基于余弦相似度的选择：在语义过滤之后，我们应用基于余弦相似度的迭代选择机制，使任意两条提示词之间的相似度不超过 0.8 的阈值，从而保证数据集多样性并有效去除冗余条目。

**EN** 8.2 VisionReward for Text-to-Image Optimization

**ZH** 8.2 VisionReward 用于文本到图像优化

**EN** Dataset & Training Settings. We strategically sample 63,165 prompts from existing datasets and generate 8 images per prompt using SDXL (this procedure theoretically produces 1.76M text-image pairs). Employing the MPO algorithm, we obtain 760k dominant pairs with 63,069 unique prompts. For comparison, we use HPSv2 with a threshold of 0.0015, getting 770k pairs with 63,107 unique prompts from the same source. We also compare with human annotated pairs, sampling 780k human preference pairs with 57,674 unique prompts from Pick-a-Pic v2 dataset.

**ZH** 数据集与训练设置。我们从已有数据集中策略性地采样 63,165 条提示词，并用 SDXL 为每条提示词生成 8 张图像（该流程理论上产出 1.76M 个文本-图像对）。采用 MPO 算法后，我们得到 760k 个支配对，涵盖 63,069 条不同的提示词。作为对比，我们使用 HPSv2 并以 0.0015 为阈值，从同一来源得到 770k 个样本对、涵盖 63,107 条不同提示词；我们还与人工标注的样本对进行比较，从 Pick-a-Pic v2 数据集中采样得到 780k 个人类偏好对、涵盖 57,674 条不同提示词。

**EN** We maintain consistent training parameters and dataset sizes across all experiments to ensure fair comparison. For all three experiments, we used an effective batch size of 256 (with GAS set to 4 and train batch size set to 1), set ⟦SLOT_37⟧ to 5000, and a learning rate of 5e-9 (before scaling). We employ a constant warmup strategy with 100 steps and the training is conducted over 3,000 steps (approximately 1 epoch).

**ZH** 为保证公平比较，所有实验均采用一致的训练参数与数据集规模。三组实验中，有效批大小均为 256（GAS 设为 4，训练批大小设为 1），⟦SLOT_37⟧ 设为 5000，学习率为 5e-9（缩放前）。我们采用 100 步的恒定预热策略，共训练 3,000 步（约 1 个轮次）。

**EN** Evaluation Settings. We conducted both automatic and human evaluation on DrawBench (Saharia et al. 2022). Automatic evaluation includes multiple metrics such as human preference RMs, CLIP (Radford et al. 2021) and LAION-Aesthetic (Schuhmann et al. 2022).

**ZH** 评测设置。我们在 DrawBench（Saharia et al. 2022）上同时进行了自动评测与人工评测。自动评测包含多个指标，如人类偏好奖励模型、CLIP（Radford et al. 2021）与 LAION-Aesthetic（Schuhmann et al. 2022）。

**EN** Experimental Results. Main results are demonstrated in Table 12 and Table 13. VisionReward gets leading results across multiple machine metrics and achieves significant improvements across all four dimensions of VisionReward.

**ZH** 实验结果。主要结果如表 12 与表 13 所示。VisionReward 在多个机器指标上取得领先结果，并在 VisionReward 的全部四个维度上均实现显著改进。

<!-- [原子块 · table] Methods CLIP Aes HPSv2 PickScore Original 0.273 5.463 0.282 22.25 Pick-a-Pic 0.279 5.511 0.286 22.45 HPSv2 0.277 5.599 0.292 22.58 VisionReward 0.279 5.612 0.289 22.61 -->

**EN** Table 12: Evaluation results of multiple metrics on DrawBench.

**ZH** 表 12：DrawBench 上多个指标的评测结果。

<!-- [原子块 · table] Methods Composition Quality Fidelity Safety Original 0.755 0.550 0.009 -0.008 Pick-a-Pic 0.765 0.588 0.009 -0.009 HPSv2 0.874 0.630 0.010 -0.004 VisionReward 0.894 0.670 0.017 -0.001 -->

**EN** Table 13: Evaluation results on MonetBench.

**ZH** 表 13：在 MonetBench 上的评测结果。

**EN** 8.3 More Results of MPO

**ZH** 8.3 MPO 的更多结果

**EN** Case Study. Fig. 8 shows MPO cases for text-to-image, while Fig. 9 and Fig. 10 show MPO cases for text-to-video. MPO fine-tuned model surpasses the original model in multiple aspects and also outperforms other scoring methods.

**ZH** 案例研究。图 8 展示了文本到图像的 MPO 案例，图 9 与图 10 展示了文本到视频的 MPO 案例。经 MPO 微调的模型在多个方面超过原始模型，也优于其他打分方法。

**EN** Training Curve. Fig. 11 shows the variation of the dimensional scores during the MPO process with respect to the number of training samples. The results demonstrate that the MPO method enables the model to avoid trade-offs during training, thereby achieving simultaneous improvements across various sub-dimensions. In contrast, the DPO (Wallace et al. 2024) method fails to achieve this level of concurrent enhancement.

**ZH** 训练曲线。图 11 展示了 MPO 过程中各维度得分随训练样本数量的变化。结果表明，MPO 方法使模型在训练中避免权衡取舍，从而实现各子维度的同步提升；相比之下，DPO（Wallace et al. 2024）方法无法达到这种并发式的提升。

**EN** Ablation Study: Different Strategy for MPO. In using the MPO strategy, we define the way in which ⟦SLOT_38⟧ dominates ⟦SLOT_39⟧ (given two images ⟦SLOT_40⟧ and ⟦SLOT_41⟧) to select pairs. The definition of “dominate” includes at least three methods for different reward objective: score of each dimension, score of each sub-dimension, and score of each binary question. To investigate the impact of different definitions of “dominate”, we conduct experiments based on CogVideoX-5B. Specifically, we employ three different strategies, setting the threshold of the total score to 0.6, 0.5, and 0.4 respectively, ensuring that the number of pairs obtained through all three strategies is 5k. We use a batch size of 64, a learning rate of 2e-6, the DPO parameter ⟦SLOT_42⟧ of 500, and the training steps of 300. After training, we compare the evaluation results of VisionReward on MonetBench. Table 14 shows that using the score for each dimension as objective yields the best results.

**ZH** 消融实验：MPO 的不同策略。在使用 MPO 策略时，我们通过定义 ⟦SLOT_38⟧ 支配 ⟦SLOT_39⟧ 的方式（给定两张图像 ⟦SLOT_40⟧ 与 ⟦SLOT_41⟧）来筛选样本对。“支配”的定义针对不同奖励目标至少包含三种方式：每个维度的分数、每个子维度的分数，以及每个二值问题的分数。为考察不同「支配」定义的影响，我们基于 CogVideoX-5B 开展实验，具体采用三种不同策略，总分阈值分别设为 0.6、0.5 与 0.4，以保证三种策略得到的样本对数量均为 5k。批大小设为 64，学习率为 2e-6，DPO 参数 ⟦SLOT_42⟧ 为 500，训练步数为 300。训练完成后，我们比较 VisionReward 在 MonetBench 上的评测结果。表 14 显示，以每个维度的分数为目标时效果最佳。

<!-- [原子块 · table] Methods Baseline Dimension Sub-dimension Question Reward 4.303 4.573 4.539 4.514 -->

**EN** Table 14: Score of VisionReward after different strategies of MPO. Dimension: “dominate” based on score of each dimension. Sub-dimension: “dominate” based on score of each sub-dimension. Question: “dominate” based on score of each binary question.

**ZH** 表 14：不同 MPO 策略下 VisionReward 的分数。Dimension：基于每个维度的分数判定「支配」；Sub-dimension：基于每个子维度的分数判定「支配」；Question：基于每个二值问题的分数判定「支配」。

<!-- [原子块 · img]  -->

**EN** Figure 8: Qualitative result of MPO in text-to-image.

**ZH** 图 8：MPO 在文本到图像上的定性结果。

<!-- [原子块 · img]  -->

**EN** Figure 9: Qualitative result of MPO in text-to-video.

**ZH** 图 9：MPO 在文本到视频上的定性结果。

<!-- [原子块 · img]  -->

**EN** Figure 10: Qualitative result of MPO in text-to-video.

**ZH** 图 10：MPO 在文本到视频上的定性结果。

<!-- [原子块 · object]  -->

**EN** (a) Overall Score

**ZH** （a）总分

<!-- [原子块 · object]  -->

**EN** (b) Composition Score

**ZH** （b）构图分数

<!-- [原子块 · object]  -->

**EN** (c) Fidelity Score

**ZH** （c）保真度分数

<!-- [原子块 · object]  -->

**EN** (d) Alignment Score

**ZH** （d）对齐分数

<!-- [原子块 · object]  -->

**EN** (e) Quality Score

**ZH** （e）质量分数

<!-- [原子块 · object]  -->

**EN** (f) Safety & Emotion Score

**ZH** （f）安全与情感分数

**EN** Figure 11: Variation of dimensional scores during the MPO process with respect to the number of training samples.

**ZH** 图 11：MPO 过程中各维度得分随训练样本数量的变化。

**EN** 9 Details of Fine-Grained Questions

**ZH** 9 细粒度问题详情

**EN** Table 15 and Table 16 show the annotation taxonomy of images, while Table 17 and Table 18 show for videos.

**ZH** 表 15 与表 16 给出了图像的标注分类体系，表 17 与表 18 给出了视频的标注分类体系。

**EN** 10 More Results of Fine-Grained Design

**ZH** 10 细粒度设计的更多结果

**EN** Weight and Accuracy of Checklist. We curate separate test sets of images and videos from outside the training set to evaluate the accuracy of judgment questions. The test set comprises 1,209 images and 1,000 videos, respectively. We report the accuracy of judgment questions (Cf. Table 19 and Table 20 for text-to-image, Table 21 and Table 22 for text-to-video). As a reference, we specifically record the linear weights obtained from linear regression on human preference data as well as the Spearman rank correlation coefficient between human preference and the results of each judgment question.

**ZH** 检查清单的权重与准确率。我们从训练集之外整理出独立的图像与视频测试集，用于评估判断问题的准确率。测试集分别包含 1,209 张图像与 1,000 个视频。我们报告了判断问题的准确率（文本到图像见表 19 与表 20，文本到视频见表 21 与表 22）。作为参考，我们还专门记录了在人类偏好数据上通过线性回归得到的线性权重，以及人类偏好与各判断问题结果之间的 Spearman 秩相关系数。

**EN** Correlation of Sub Dimensions. To mine the correlation between the sub-dimensions after preference decoupling, we show the correlation coefficients between the sub-dimensions in a heat map (Cf. Fig. 12).

**ZH** 子维度的相关性。为挖掘偏好解耦之后各子维度之间的相关性，我们用热力图展示了子维度之间的相关系数（参见图 12）。

**EN** Dimension Sub-dimension Option Checklist Composition Symmetry symmetrical Is the image symmetrical? ordinary Does the image avoid asymmetry? asymmetrical Composition Object pairing coordinated Are the objects well-coordinated? ordinary Does the image avoid poorly coordinated objects? uncoordinated Composition Main object prominent Is the main subject prominent? ordinary Does the image avoid an unclear main subject? prominent Composition Richness very rich Is the image very rich? rich Is the image rich? ordinary Is the image not monotonous? monotonous Is the image not empty? empty Composition Background beautiful Is the background beautiful? somewhat beautiful Is the background somewhat beautiful? ordinary Is there a background? no background Quality Clarity very clear Is the image very clear? clear Is the image clear? ordinary Does the image avoid being blurry? blurry Does the image avoid being completely blurry? completely blurry Quality Color Brightness bright Are the colors bright? ordinary Are the colors not dark? dark Quality Color Aesthetic beautiful colors Are the colors beautiful? ordinary colors Are the colors not ugly? ugly colors Quality Lighting Distinction very distinct Is the lighting and shadow very distinct? distinct Is the lighting and shadow distinct? ordinary Is there lighting and shadow? no lighting Quality Lighting Aesthetic very beautiful Are the lighting and shadows very beautiful? beautiful Are the lighting and shadows beautiful? ordinary Is there lighting and shadow? no lighting

**ZH** Dimension Sub-dimension Option Checklist Composition Symmetry symmetrical Is the image symmetrical? ordinary Does the image avoid asymmetry? asymmetrical Composition Object pairing coordinated Are the objects well-coordinated? ordinary Does the image avoid poorly coordinated objects? uncoordinated Composition Main object prominent Is the main subject prominent? ordinary Does the image avoid an unclear main subject? prominent Composition Richness very rich Is the image very rich? rich Is the image rich? ordinary Is the image not monotonous? monotonous Is the image not empty? empty Composition Background beautiful Is the background beautiful? somewhat beautiful Is the background somewhat beautiful? ordinary Is there a background? no background Quality Clarity very clear Is the image very clear? clear Is the image clear? ordinary Does the image avoid being blurry? blurry Does the image avoid being completely blurry? completely blurry Quality Color Brightness bright Are the colors bright? ordinary Are the colors not dark? dark Quality Color Aesthetic beautiful colors Are the colors beautiful? ordinary colors Are the colors not ugly? ugly colors Quality Lighting Distinction very distinct Is the lighting and shadow very distinct? distinct Is the lighting and shadow distinct? ordinary Is there lighting and shadow? no lighting Quality Lighting Aesthetic very beautiful Are the lighting and shadows very beautiful? beautiful Are the lighting and shadows beautiful? ordinary Is there lighting and shadow? no lighting

**EN** Table 15: Annotation taxonomy and checklist details for text-to-image evaluation. (part 1)

**ZH** 表 15：文本到图像评测的标注分类体系与检查清单详情。（第 1 部分）

**EN** Dimension Sub-dimension Option Checklist Fidelity Detail reality realistic Are the image details realistic? neutral Do the image details avoid being unrealistic? unrealistic Do the image details avoid being very unrealistic? very unrealistic Do the image details avoid being greatly unrealistic? greatly unrealistic Fidelity Detail refinement very refined Are the image details very exquisite? refined Are the image details exquisite? ordinary Do the image details avoid being coarse? rough Do the image details avoid being very coarse? very rough Does the image avoid being hard to recognize? indistinguishable Does the image avoid being fragmented? fragmented Fidelity Body no errors Is the human body in the image completely correct? neutral Does the human body in the image avoid errors? some errors Does the human body in the image avoid obvious errors? obvious errors Does the human body in the image avoid serious errors? serious errors Is there a human body in the image? no human figure Fidelity Face very beautiful Is the human face very beautiful? beautiful Is the human face beautiful? normal Does the human face avoid errors? some errors Does the human face avoid serious errors? serious errors Is there a human face in the image? no human face Fidelity Hands perfect Are the human hands perfect? mostly correct Are the human hands essentially correct? minor errors Do the human hands avoid obvious errors? obvious errors Do the human hands avoid serious errors? serious errors Are there human hands in the image? no human hands Safety & Emotion Emotion very positive Can the image evoke a very positive emotional response? positive Can the image evoke a positive emotional response? ordinary Does the image avoid evoking a negative emotional response? negative Does the image avoid evoking a very negative emotional response? very negative Safety & Emotion Safety safe Is the image completely safe? neutral Is the image harmless? potentially harmful Does the image avoid obvious harmfulness? harmful Does the image avoid serious harmfulness? very harmful

**ZH** Dimension Sub-dimension Option Checklist Fidelity Detail reality realistic Are the image details realistic? neutral Do the image details avoid being unrealistic? unrealistic Do the image details avoid being very unrealistic? very unrealistic Do the image details avoid being greatly unrealistic? greatly unrealistic Fidelity Detail refinement very refined Are the image details very exquisite? refined Are the image details exquisite? ordinary Do the image details avoid being coarse? rough Do the image details avoid being very coarse? very rough Does the image avoid being hard to recognize? indistinguishable Does the image avoid being fragmented? fragmented Fidelity Body no errors Is the human body in the image completely correct? neutral Does the human body in the image avoid errors? some errors Does the human body in the image avoid obvious errors? obvious errors Does the human body in the image avoid serious errors? serious errors Is there a human body in the image? no human figure Fidelity Face very beautiful Is the human face very beautiful? beautiful Is the human face beautiful? normal Does the human face avoid errors? some errors Does the human face avoid serious errors? serious errors Is there a human face in the image? no human face Fidelity Hands perfect Are the human hands perfect? mostly correct Are the human hands essentially correct? minor errors Do the human hands avoid obvious errors? obvious errors Do the human hands avoid serious errors? serious errors Are there human hands in the image? no human hands Safety & Emotion Emotion very positive Can the image evoke a very positive emotional response? positive Can the image evoke a positive emotional response? ordinary Does the image avoid evoking a negative emotional response? negative Does the image avoid evoking a very negative emotional response? very negative Safety & Emotion Safety safe Is the image completely safe? neutral Is the image harmless? potentially harmful Does the image avoid obvious harmfulness? harmful Does the image avoid serious harmfulness? very harmful

**EN** Table 16: Annotation taxonomy and checklist details for text-to-image evaluation. (part 2)

**ZH** 表 16：文本到图像评测的标注分类体系与检查清单详情。（第 2 部分）

**EN** Dimension Sub-dimension Option Checklist Alignment Alignment meet 100% Does the video meet all the requirements stated in the text ”[[prompt]]”? meet 80%-100% Does the video meet most of the requirements stated in the text ”[[prompt]]”? meet 60%-80% Does the video meet some of the requirements stated in the text ”[[prompt]]”? meet 40%-60% Does the video not completely fail to meet the requirements stated in the text ”[[prompt]]”? meet 0-40% Composition Composition good Is the composition aesthetically pleasing? normal Does the composition have no obvious flaws? bad Quality Color very beautiful Are the colors exceptionally beautiful? beautiful Are the colors beautiful? normal Are the colors not unattractive? unattractive Are the colors not significantly unattractive? very unattractive Quality Lighting Accurate good Is the lighting perfectly accurate? normal Does the lighting have no obvious errors? bad Is there any lighting present? no lighting Quality Lighting Aes very good Is the lighting exceptionally beautiful? good Is the lighting beautiful? normal Is the lighting not unattractive? bad Quality Clear very clear Is it very clear? clear Is it clear? normal Is it not blurry? blurry Is it not completely blurry? completely blurry Fidelity Detail Refinement very refined Are the details very refined? refined Are the details refined? normal Are the details not rough? rough Are the details not significantly rough? very rough Fidelity Movement Reality good Is the object’s movement completely realistic? normal Does the object’s movement have no obvious realism issues? bad Fidelity Letters good Are all the letters correct? normal Do the letters have no obvious errors? bad Are there any letters present? no letter Safety Safety 100% safe Is the video content safe? 80%-100% safe Is the video content definitely free of harmful material? 60%-80% safe Does the video content contain no harmful material? 40%-60% safe Does the video content contain no extremely harmful material? 0-40% safe

**ZH** Dimension Sub-dimension Option Checklist Alignment Alignment meet 100% Does the video meet all the requirements stated in the text ”[[prompt]]”? meet 80%-100% Does the video meet most of the requirements stated in the text ”[[prompt]]”? meet 60%-80% Does the video meet some of the requirements stated in the text ”[[prompt]]”? meet 40%-60% Does the video not completely fail to meet the requirements stated in the text ”[[prompt]]”? meet 0-40% Composition Composition good Is the composition aesthetically pleasing? normal Does the composition have no obvious flaws? bad Quality Color very beautiful Are the colors exceptionally beautiful? beautiful Are the colors beautiful? normal Are the colors not unattractive? unattractive Are the colors not significantly unattractive? very unattractive Quality Lighting Accurate good Is the lighting perfectly accurate? normal Does the lighting have no obvious errors? bad Is there any lighting present? no lighting Quality Lighting Aes very good Is the lighting exceptionally beautiful? good Is the lighting beautiful? normal Is the lighting not unattractive? bad Quality Clear very clear Is it very clear? clear Is it clear? normal Is it not blurry? blurry Is it not completely blurry? completely blurry Fidelity Detail Refinement very refined Are the details very refined? refined Are the details refined? normal Are the details not rough? rough Are the details not significantly rough? very rough Fidelity Movement Reality good Is the object’s movement completely realistic? normal Does the object’s movement have no obvious realism issues? bad Fidelity Letters good Are all the letters correct? normal Do the letters have no obvious errors? bad Are there any letters present? no letter Safety Safety 100% safe Is the video content safe? 80%-100% safe Is the video content definitely free of harmful material? 60%-80% safe Does the video content contain no harmful material? 40%-60% safe Does the video content contain no extremely harmful material? 0-40% safe

**EN** Table 17: Annotation taxonomy and checklist details for text-to-video evaluation. (part 1)

**ZH** 表 17：文本到视频评测的标注分类体系与检查清单详情。（第 1 部分）

**EN** Dimension Sub-dimension Option Checklist Stability Movement smoothness good Is the smoothness of the object’s movement good? normal Does the smoothness of the object’s movement have no obvious issues? bad Stability Image quality stability very stable Is the image quality very stable? stable Is the image quality stable? normal Is the image quality not unstable? unstable Is the image quality free of noticeable instability? very unstable Stability Focus good Is the focus aesthetically pleasing? normal Does the focus have no obvious flaws? bad Stability Camera movement good Is the camera movement aesthetically pleasing? normal Does the camera movement have no obvious flaws? bad Stability Camera stability stable Is the camera stable? normal Is the camera not unstable? unstable Preservation Shape at beginning completely accurate Is the shape of the object at the beginning of the video completely accurate? no errors Does the shape of the object at the beginning have no obvious errors? not chaotic Is the shape of the object at the beginning not chaotic? flawed Preservation Shape throughout perfectly maintained Is the shape of the object perfectly maintained throughout the video? no issues Does the shape of the object have no obvious issues throughout the video? normal Does the shape of the object generally have no major issues throughout the video? not chaotic Is the shape of the object not chaotic throughout the video? flawed Dynamic Object Motion dynamic highly dynamic Is the object’s motion highly dynamic? dynamic Is the object’s motion dynamic? normal Is the object’s motion not minimal? not static Is the object’s motion not static? static Dynamic Camera motion dynamic highly dynamic Is the camera motion highly dynamic? dynamic Is the camera motion dynamic? not minimal Is the camera motion not minimal? not static Is the camera motion not static? static Physics Physics law full compliance Does it fully comply with the laws of physics? partial compliance Does it partially comply with the laws of physics? no obvious violations Does it have no obvious violations of the laws of physics? physical world Is the video content part of the physical world? non-compliance

**ZH** Dimension Sub-dimension Option Checklist Stability Movement smoothness good Is the smoothness of the object’s movement good? normal Does the smoothness of the object’s movement have no obvious issues? bad Stability Image quality stability very stable Is the image quality very stable? stable Is the image quality stable? normal Is the image quality not unstable? unstable Is the image quality free of noticeable instability? very unstable Stability Focus good Is the focus aesthetically pleasing? normal Does the focus have no obvious flaws? bad Stability Camera movement good Is the camera movement aesthetically pleasing? normal Does the camera movement have no obvious flaws? bad Stability Camera stability stable Is the camera stable? normal Is the camera not unstable? unstable Preservation Shape at beginning completely accurate Is the shape of the object at the beginning of the video completely accurate? no errors Does the shape of the object at the beginning have no obvious errors? not chaotic Is the shape of the object at the beginning not chaotic? flawed Preservation Shape throughout perfectly maintained Is the shape of the object perfectly maintained throughout the video? no issues Does the shape of the object have no obvious issues throughout the video? normal Does the shape of the object generally have no major issues throughout the video? not chaotic Is the shape of the object not chaotic throughout the video? flawed Dynamic Object Motion dynamic highly dynamic Is the object’s motion highly dynamic? dynamic Is the object’s motion dynamic? normal Is the object’s motion not minimal? not static Is the object’s motion not static? static Dynamic Camera motion dynamic highly dynamic Is the camera motion highly dynamic? dynamic Is the camera motion dynamic? not minimal Is the camera motion not minimal? not static Is the camera motion not static? static Physics Physics law full compliance Does it fully comply with the laws of physics? partial compliance Does it partially comply with the laws of physics? no obvious violations Does it have no obvious violations of the laws of physics? physical world Is the video content part of the physical world? non-compliance

**EN** Table 18: Annotation taxonomy and checklist details for text-to-video evaluation. (part 2)

**ZH** 表 18：文本到视频评测的标注分类体系与检查清单详情。（第 2 部分）

<!-- [原子块 · table] ID Checklist Acc ρ \rho Weight 1 Is there a human body in the image? 93.13 0.090 mask 2 Is there a human face in the image? 96.20 0.110 mask 3 Are there human hands in the image? 93.30 0.022 mask 4 Is -->

**EN** Table 19: Accuracy, spearman correlation, and linear weights of VisionReward in text-to-image. (Part 1)

**ZH** 表 19：VisionReward 在文本到图像上的准确率、Spearman 相关系数与线性权重。（第 1 部分）

<!-- [原子块 · table] ID Checklist Acc ρ \rho Weight 41 Do the image details avoid being unrealistic? 63.94 0.140 0.000 42 Do the image details avoid being very unrealistic? 74.19 0.156 0.000 43 Do the image details avoid  -->

**EN** Table 20: Accuracy, spearman correlation, and linear weights of VisionReward in text-to-image. (Part 2)

**ZH** 表 20：VisionReward 在文本到图像上的准确率、Spearman 相关系数与线性权重。（第 2 部分）

<!-- [原子块 · table] ID Checklist Acc ρ \rho Weight 1 Does the video meet all the requirements stated in the text ”[[prompt]]”? 69.5 0.315 0.954 2 Does the video meet most of the requirements stated in the text ”[[prompt] -->

**EN** Table 21: Accuracy, spearman correlation, and linear weights of VisionReward in text-to-video. (Part 1)

**ZH** 表 21：VisionReward 在文本到视频上的准确率、Spearman 相关系数与线性权重。（第 1 部分）

<!-- [原子块 · table] ID Checklist Acc ρ \rho Weight 21 Is the shape of the object at the beginning of the video completely accurate? 63.0 0.292 0.129 22 Does the shape of the object at the beginning have no obvious errors -->

**EN** Table 22: Accuracy, spearman correlation, and linear weights of VisionReward in text-to-video. (Part 2)

**ZH** 表 22：VisionReward 在文本到视频上的准确率、Spearman 相关系数与线性权重。（第 2 部分）

<!-- [原子块 · img]  -->

**EN** Figure 12: Correlation heatmap of text-to-video sub dimensions.

**ZH** 图 12：文本到视频各子维度的相关性热力图。

**EN** 11 Limitations

**ZH** 11 局限性

**EN** This section outlines several limitations of the VisionReward framework that emerged during its development.

**ZH** 本节列出 VisionReward 框架在开发过程中显现的若干局限。

**EN** Supported Video Frame Rate and Length. While training datasets of VisionReward contain videos up to 6 seconds in duration at 4 frames per second (fps), this may be insufficient for evaluating the outputs of next-generation video generation models, which are capable of producing longer and more complex content. Therefore, extending the model’s capacity to handle longer video sequences is a critical direction for future work.

**ZH** 支持的视频帧率与时长。VisionReward 的训练数据集包含时长最多 6 秒、帧率为每秒 4 帧（fps）的视频，这可能不足以评测下一代视频生成模型的输出——它们能够生成更长、更复杂的内容。因此，扩展模型以处理更长的视频序列，是未来工作的一个关键方向。

**EN** Leverage of Foundation Model. The model’s performance is inherently tied to the capabilities of its base Vision-Language Model (VLM). Our current approach utilizes a question-answering (QA) mechanism to tap into the VLM’s foundational knowledge. However, with the rise of sophisticated reasoning models, a more effective avenue for enhancing our reward model would be to integrate explicit reasoning abilities. This represents a key area for future investigation to move beyond foundational understanding towards more complex evaluation.

**ZH** 基础模型的利用。模型性能本质上受制于其基础视觉语言模型（VLM）的能力。我们当前的方法通过问答（QA）机制来调用 VLM 的基础知识。然而，随着复杂推理模型的兴起，提升奖励模型的一条更有效途径是融入显式的推理能力。这是未来研究的关键方向，可使评测从基础理解走向更复杂的评估。

**EN** 12 More Details of MonetBench

**ZH** 12 MonetBench 的更多细节

<!-- [原子块 · table] Type Image Video Content People, Objects, Animals, Story, Human Activity, Architecture, Landscape, Artificial Scene, Others, Vehicles, Plants, Food, Natural Animal Activity, Others, Scenes Physical Ph -->

**EN** Table 23: Content and Challenge of MonetBench.

**ZH** 表 23：MonetBench 的内容类别与挑战类别。

**EN** Image-MonetBench Construction. We first establish our dataset foundation by collecting 4,038 seed prompts through strategic sampling from established datasets (1,000 from ImageRewardDB (Xu et al. 2023), 1,000 from HPDv2 (Xu et al. 2023), and 2,038 from Pick-a-Pic (Kirstain et al. 2023)). Through systematic analysis of these prompts, we identify nine fundamental visual elements as content categories and twelve distinct aspects of generation complexity as challenge categories, maintaining the categorical distributions observed in the source datasets.

**ZH** Image-MonetBench 构建。我们首先通过对已有数据集策略性采样，收集 4,038 条种子提示词（1,000 条来自 ImageRewardDB（Xu et al. 2023），1,000 条来自 HPDv2（Xu et al. 2023），2,038 条来自 Pick-a-Pic（Kirstain et al. 2023）），以此奠定数据集基础。通过对这些提示词的系统分析，我们识别出九种基本视觉元素作为内容类别，以及十二个不同的生成复杂度方面作为挑战类别，并保持源数据集中观察到的类别分布。

**EN** Video-MonetBench Construction. For video prompt evaluation, we initially sample 20,000 prompts from the VproM (Wang and Yang 2024) dataset, which are filtered to 13,342 valid entries after removing duplicates and invalid content. Our video classification system comprises seven content categories reflecting different video scenarios, and thirteen challenge categories capturing various technical and creative aspects of video generation.

**ZH** Video-MonetBench 构建。在视频提示词评测方面，我们先从 VproM（Wang and Yang 2024）数据集中采样 20,000 条提示词，去重并剔除无效内容后筛选出 13,342 条有效条目。我们的视频分类体系包含反映不同视频场景的七个内容类别，以及涵盖视频生成中各类技术与创意方面的十三个挑战类别。

**EN** Prompt Generation and Filtering. To ensure benchmark quality and diversity, we employ ChatGLM (GLM 2024) to generate 1,000 new prompts for each benchmark following the established category distributions. Each generated prompt undergoes a three-stage filtering process: (1) Rouge-L (Lin 2004) similarity checking for textual diversity, (2) semantic filtering with a cosine similarity threshold of 0.9, and (3) proportional sampling to maintain the intended category distributions.

**ZH** 提示词生成与过滤。为保证基准的质量与多样性，我们使用 ChatGLM（GLM 2024）按既定的类别分布为每个基准生成 1,000 条新提示词。每条生成的提示词都要经过三阶段过滤：（1）用 Rouge-L（Lin 2004）相似度检验文本多样性；（2）以 0.9 为余弦相似度阈值进行语义过滤；（3）按比例采样以维持预期的类别分布。

**EN** Table 23 shows content and challenge categories for MonetBench. The resulting benchmark achieves balanced coverage across all categories while maintaining high standards of prompt diversity and quality. This carefully crafted multi-dimensional design enables comprehensive evaluation of visual reward models across both fundamental content types and various generation challenges.

**ZH** 表 23 给出了 MonetBench 的内容与挑战类别。最终基准在各类别上实现了均衡覆盖，同时保持提示词的高多样性与高质量。这种精心构造的多维度设计，使得可以从基础内容类型到各种生成挑战，对视觉奖励模型进行全面评测。

**EN** For experimental efficiency, we provide a condensed version by randomly sampling 500 prompts from each benchmark while preserving the categorical distribution.

**ZH** 为提高实验效率，我们提供一个精简版本：在保持类别分布的前提下，从每个基准中随机采样 500 条提示词。

**EN** Details of Classification Proportions. After completing the design of the comprehensive two-dimensional classification framework, we utilized ChatGLM to categorize each prompt in the dataset across content and challenge dimensions. We then calculated the proportions of different classification labels for content and challenges. The content and challenge categories and their respective examples are summarized in Tables 24 and 25. Based on these proportions, we used ChatGLM to construct Benchmark prompts (all prompts were generated by ChatGLM, not directly sampled from the dataset). During the construction process, we specified the investigation direction and randomly sampled four ”seed prompts” from the categorized prompts to generate new, higher-quality prompts with ChatGLM. This synthesis approach produced two benchmark datasets, containing 1,000 and 1,007 meticulously crafted prompts, respectively, preserving the statistical characteristics of the original data.

**ZH** 分类比例细节。在完成这套二维分类框架的设计之后，我们用 ChatGLM 对数据集中每条提示词在内容与挑战两个维度上进行归类，并计算不同内容与挑战标签的占比。内容与挑战类别及其示例分别汇总于表 24 与表 25。基于这些占比，我们用 ChatGLM 构建基准提示词（所有提示词均由 ChatGLM 生成，而非直接从数据集采样）。在构建过程中，我们指定调研方向，并从已归类的提示词中随机采样四条「种子提示词」，由 ChatGLM 生成质量更高的新提示词。这种合成方式产出了两个基准数据集，分别包含 1,000 条与 1,007 条精心构造的提示词，并保留了原始数据的统计特征。

**EN** The final datasets provide balanced and comprehensive coverage of content and challenge categories. Table 26 lists the specific content and challenge categories with detailed descriptions and example prompts, providing a clear understanding of the dataset’s composition. The structured methodology ensures the datasets’ diversity and alignment with real-world visual generation requirements, enabling nuanced benchmarking of visual models.

**ZH** 最终数据集在内容与挑战类别上实现了均衡而全面的覆盖。表 26 列出了具体的内容与挑战类别，并给出详细描述与示例提示词，便于清楚理解数据集的构成。这套结构化方法确保了数据集的多样性，以及与真实世界视觉生成需求的契合，从而支持对视觉模型进行细粒度的基准评测。

<!-- [原子块 · table] Image Video Type Ratio Count Type Ratio Count People 8 286 Story 5 265 Objects 4 143 Human Activity 4 212 Animals 4 143 Artificial Scene 3 159 Architecture 4 143 Natural Scenes 3 159 Others 2 72 Anima -->

**EN** Table 24: Content Categories for Image and Video

**ZH** 表 24：图像与视频的内容类别

<!-- [原子块 · table] Image Video Type Ratio Count Type Ratio Count Unreal 8 187 Style 13 465 Style & Format 8 187 Material/Texture 8 292 Fine-grained Detail 8 186 Emotional Expr. 7 249 Color 4 93 Color/Tone 7 261 Famous C -->

**EN** Table 25: Challenge Categories for Image and Video

**ZH** 表 25：图像与视频的挑战类别

<!-- [原子块 · table] Categorie Description Example Prompt Content Human Activity Descriptions about daily human activities, sports, performing arts, and professional skills. A family enjoying a picnic in a park, children  -->

**EN** Table 26: Video classification standards with example prompts.

**ZH** 表 26：视频分类标准及示例提示词。
