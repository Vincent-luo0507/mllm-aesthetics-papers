# PAL：面向异质偏好学习的多元对齐框架

> 原标题：PAL: Pluralistic Alignment Framework for Learning from Heterogeneous Preferences
> 作者：Daiwei Chen, Yi Chen, Aniket Rege, Ramya Korlakai Vinayak · arXiv:2406.08469 · 2024-06-12

<!-- [原子块 · verbatim] PAL: Pluralistic Alignment Framework for Learning from Heterogeneous Preferences -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] Large foundation models pretrained on raw web-scale data are not readily deployable without additional step of extensive alignment to human preferences [ 1 ] . Such alignment is typically done by coll -->

**EN** A Preprint

**ZH** 一篇预印本

<!-- [原子块 · table]  -->

**EN** Keywords Alignment ⟦SLOT_0⟧ Preference Learning ⟦SLOT_1⟧ Plurality

**ZH** 关键词 对齐 ⟦SLOT_0⟧ 偏好学习 ⟦SLOT_1⟧ 多元性

**EN** 1 Introduction

**ZH** 1 引言

**EN** Large pre-trained “foundation” models [8], such as large language models (LLMs) for language generation [9, 10, 11, 12, 13, 14, 15] and text-to-image (TTI [16]) models for image generation [17, 18, 19, 20, 21, 22, 23], are trained on massive amounts of data, including data from the internet. While such models learn useful representations for general language or vision tasks, they are not readily deployable out-of-the-box to be used in the real world. Modern machine learning (ML) systems built on large foundation models go through rigorous fine-tuning or aligning towards human preferences to make them amenable to real-world usage. This is usually achieved through supervised fine-tuning (SFT) with direct human input on what the desired outputs should look like for a given context and then followed by alignment with large amounts of human preference feedback usually in the form of pairwise comparison of two outputs to a given input context [1]. This is usually achieved either by (i) fine-tuning the SFT model with explicitly learned reward as done in reinforcement learning with human feedback (RLHF) methods such as proximal policy optimization (PPO) [24] or implicitly with methods such as direct preference optimization (DPO) [25], or (ii) inference-time policy adaptation [26] without fine-tuning the original large policy model.

**ZH** 大规模预训练的“基础”模型 [8]——例如用于语言生成的大语言模型（LLM）[9, 10, 11, 12, 13, 14, 15]，以及用于图像生成的文本到图像（TTI [16]）模型 [17, 18, 19, 20, 21, 22, 23]——在海量数据（包括互联网数据）上训练而成。尽管这类模型学到了对通用语言或视觉任务有用的表示，它们却无法开箱即用地部署到真实世界。基于大型基础模型构建的现代机器学习（ML）系统，需要经过严格的微调或向人类偏好对齐，才能适用于真实场景。这通常分两步实现：先以人类直接输入的、给定上下文下期望输出应为何样的示范做监督微调（SFT），随后用大量人类偏好反馈做对齐，这些反馈通常以“对给定输入上下文的两个输出进行成对比较”为形式 [1]。对齐又通常通过两种方式之一完成：(i) 用显式习得的奖励微调 SFT 模型，如基于人类反馈的强化学习（RLHF）方法中的近端策略优化（PPO）[24]，或以直接偏好优化（DPO）[25] 等方法隐式地实现；或 (ii) 推理时策略适配 [26]，即不微调原始的大型策略模型。

**EN** While aligning ML/AI models to human preferences, it is imperative to ask ourselves whose preferences are we aligning the ML/AI models to? [27] The status quo of the alignment phase is to assume a homogeneous preference shared by all humans and attempt to learn a reward model to learn this preference with the Bradley-Terry-Luce (BTL) model [2] of paired preferences. We challenge these notions in an attempt to capture diverse, heterogeneous preferences [3, 28, 29, 30]. The importance of capturing the plurality of preferences and values among humans has also been highlighted recently by Sorensen et al.. However, the methods suggested therein and other recent works that look at learning multiple rewards as a top-down approach where the system designer decides the number and axes that one should care about [1, 27, 32, 33, 34], e.g., helpfulness vs. harmfulness [35, 36, 37, 38]. In reality, human preference is more complex than the designer-specified axes [28], which leads us to propose the following goal.

**ZH** 在把 ML/AI 模型对齐到人类偏好时，我们必须追问：我们究竟在把 ML/AI 模型对齐到谁的偏好？[27] 对齐阶段的现状是假设存在一种全人类共享的同质偏好，并试图用成对偏好的 Bradley-Terry-Luce（BTL）模型 [2] 学习一个奖励模型来拟合该偏好。我们对这些观念提出质疑，尝试捕捉多样化、异质的偏好 [3, 28, 29, 30]。Sorensen 等人近来也强调了捕捉人类偏好与价值多元性的重要性。然而，他们提出的方法以及其他近期把“学习多重奖励”视为自顶向下思路的工作——由系统设计者决定应当关注哪些维度及其数量 [1, 27, 32, 33, 34]——例如有用性与有害性 [35, 36, 37, 38]。现实中，人类偏好远比设计者指定的维度复杂 [28]，这促使我们提出如下目标。

<!-- [原子块 · svg]  -->

**EN** Our Contributions. Towards this goal, we make the following contributions,

**ZH** 我们的贡献。围绕这一目标，我们作出以下贡献：

**EN** 1. Novel Reformulation: We reframe the problem of alignment from human preferences by introducing the lens of ideal point model [4] and metric learning [39]. This re-framing enables leveraging modeling and algorithmic techniques from a richer set of toolboxes (Sections 2 and 3.1).

**ZH** 1. 新颖的重构：我们引入理想点模型 [4] 与度量学习 [39] 的视角，重构了从人类偏好出发的对齐问题。这一重构使我们得以借助更丰富的建模与算法工具箱（第 2 节与第 3.1 节）。

**EN** 2. New Framework for Pluralistic Alignment: We propose ⟦SLOT_2⟧, a general framework for pluralistic alignment using diverse human preferences from the ground up. Our framework uses a mixture modeling approach combined with the ideal point and metric learning reframing that is interpretable (Figure 1, Section 3). It can work with the output of any foundation model and learn reward function to generalize to a population of diverse people. Our framework is versatile to be applied to a wide variety of application domains.

**ZH** 2. 面向多元对齐的新框架：我们提出 ⟦SLOT_2⟧——一个从底层就利用多样化人类偏好的通用多元对齐框架。我们的框架把混合建模方法与理想点、度量学习的重构结合起来，具备可解释性（图 1，第 3 节）。它可作用于任何基础模型的输出，学习奖励函数以泛化到多样化的人群，并能灵活应用于广泛的应用领域。

**EN** 3. Empirical Validation on Benchmark Datasets: We evaluate our framework through extensive experiments on both synthetic and real datasets (Sections 4.1 and 4.3). Our experiments highlight the ability and versatility of the ⟦SLOT_3⟧ framework to learn from diverse preferences when heterogeneity exists in both language and vision data. Our experiments also reveal that even when the datasets are collected in a homogeneous way, ⟦SLOT_4⟧ can learn reward functions using very simple models, e.g., 2-layer MLP, on top of foundation models and are competitive with state-of-the-art (SoTA) models that fine-tune large foundation models. We discuss broader impacts, limitations and areas for future work in Section 6.

**ZH** 3. 在基准数据集上的实证验证：我们通过合成与真实数据集上的大量实验评估该框架（第 4.1 节与第 4.3 节）。实验凸显了 ⟦SLOT_3⟧ 框架在语言与视觉数据中都存在异质性时，从多样化偏好中学习的能力与通用性。实验还揭示，即便数据集以同质的方式收集，⟦SLOT_4⟧ 也能在基础模型之上用非常简单的模型（如 2 层 MLP）学习奖励函数，并与微调大型基础模型的当前最优（SoTA）模型相竞争。我们在第 6 节讨论更广泛的影响、局限性与未来方向。

<!-- [原子块 · img]  -->

**EN** Figure 1: Illustration of ⟦SLOT_5⟧ framework for learning from diverse preferences (Section 3). For any user ⟦SLOT_6⟧, the probability of preferring ⟦SLOT_7⟧ to ⟦SLOT_8⟧ for the context ⟦SLOT_9⟧ is given by a reward model ⟦SLOT_10⟧ which is modeled as a uses a mixture modeling approach to capture diverse user preferences – each user’s preference is modeled as a convex combination of ⟦SLOT_11⟧ prototypes. Reward function formulated using ⟦SLOT_12⟧ framework can be used flexibly, e.g, with fixed preference points (Model A), with preference points that are functions of the context/prompt ⟦SLOT_13⟧ (Model B).

**ZH** 图 1：⟦SLOT_5⟧ 框架从多样化偏好中学习的示意图（第 3 节）。对任意用户 ⟦SLOT_6⟧，在上下文 ⟦SLOT_9⟧ 下偏好 ⟦SLOT_7⟧ 胜过 ⟦SLOT_8⟧ 的概率由奖励模型 ⟦SLOT_10⟧ 给出；该模型采用混合建模方法捕捉多样化的用户偏好——每个用户的偏好被建模为 ⟦SLOT_11⟧ 个原型的凸组合。用 ⟦SLOT_12⟧ 框架构建的奖励函数可灵活使用，例如采用固定的偏好点（模型 A），或采用作为上下文/提示词 ⟦SLOT_13⟧ 函数的偏好点（模型 B）。

**EN** 2 Notations and Background

**ZH** 2 符号与背景

**EN** We begin with a brief discussion of the BTL model and how it is currently used in reward learning from pairwise preference comparisons, followed by motivating the ideal point model.

**ZH** 我们先简要讨论 BTL 模型及其当前在从成对偏好比较中学习奖励时的用法，随后引出理想点模型。

**EN** Bradley-Terry-Luce (BTL) model [2] is a parametric model for ranking. Given ⟦SLOT_14⟧ items or alternatives, the assumption is that there is a universal ranking: ⟦SLOT_15⟧ which are a reflection of the unknown true scores or weights associated with each of these items ⟦SLOT_16⟧, where ⟦SLOT_17⟧ denotes permutation and the scores ⟦SLOT_18⟧ are positive real numbers. Then, the probability that “⟦SLOT_19⟧ beats ⟦SLOT_20⟧" when comparing them, denoted by ⟦SLOT_21⟧ is given by,

**ZH** Bradley-Terry-Luce（BTL）模型 [2] 是一种用于排序的参数化模型。给定 ⟦SLOT_14⟧ 个条目或备选项，该模型假设存在一个通用排序：⟦SLOT_15⟧，它反映了与这些条目各自关联的未知真实分数或权重 ⟦SLOT_16⟧，其中 ⟦SLOT_17⟧ 表示排列，分数 ⟦SLOT_18⟧ 为正实数。那么，在比较二者时“⟦SLOT_19⟧ 胜过 ⟦SLOT_20⟧”的概率（记作 ⟦SLOT_21⟧）为：

<!-- [原子块 · table] Pr ⁡ ( i ≻ j ) = s i ⋆ s i ⋆ + s j ⋆ = exp ⁡ ( r i ) exp ⁡ ( r i ) + exp ⁡ ( r j ) , where the variables ​ r ​ re-parameterize ​ s > 0 . \Pr(i\succ j)=\frac{s^{\star}_{i}}{s^{\star}_{i}+s^{\star}_{j}} -->

**EN** Notation: We set up some notation for further discussion. Let ⟦SLOT_22⟧ denote the dimension of the representation space of the foundation models. Let ⟦SLOT_23⟧ denote the representation of the prompt or the context. Let ⟦SLOT_24⟧ and ⟦SLOT_25⟧ denote the embeddings of two items where the subscripts denote left and right respectively. Note that while we take the dimensions of the representation space for the prompt and the output to be the same, it need not be the same in general.

**ZH** 符号说明：我们为后续讨论设定一些符号。令 ⟦SLOT_22⟧ 表示基础模型表示空间的维度，⟦SLOT_23⟧ 表示提示词或上下文的表示，⟦SLOT_24⟧ 与 ⟦SLOT_25⟧ 分别表示两个条目的嵌入，下标分别表示左与右。需要说明的是，尽管我们令提示词与输出的表示空间维度相同，但一般而言二者不必相同。

**EN** In the literature on alignment with human feedback, the scores re-parametrized with reward, denoted here by ⟦SLOT_26⟧, are modeled using a neural network denoted by ⟦SLOT_27⟧. More concretely, given a context or prompt ⟦SLOT_28⟧, the probability that output ⟦SLOT_29⟧ is preferred to output ⟦SLOT_30⟧ under the BTL model is given by,

**ZH** 在基于人类反馈的对齐文献中，用奖励重新参数化的分数（此处记作 ⟦SLOT_26⟧）由神经网络 ⟦SLOT_27⟧ 建模。更具体地，给定上下文或提示词 ⟦SLOT_28⟧，在 BTL 模型下输出 ⟦SLOT_29⟧ 优于输出 ⟦SLOT_30⟧ 的概率为：

<!-- [原子块 · table] Pr ⁡ ( 𝐱 l ≻ 𝐱 r | 𝐱 c ) = exp ⁡ ( r θ ​ ( 𝐱 l , 𝐱 c ) ) exp ⁡ ( r θ ​ ( 𝐱 l , 𝐱 c ) ) + exp ⁡ ( r θ ​ ( 𝐱 r , 𝐱 c ) ) = 1 1 + exp ⁡ ( r θ ​ ( 𝐱 r , 𝐱 c ) − r θ ​ ( 𝐱 l , 𝐱 c ) ) . \displaystyle\hskip -->

**EN** The goal then is to learn this reward function ⟦SLOT_31⟧ that takes the output ⟦SLOT_32⟧ for a given context ⟦SLOT_33⟧, denoted by ⟦SLOT_34⟧, as input and map it to a real-valued reward score to approximate human preference. This learning of ⟦SLOT_35⟧ is done using lots of pairwise comparison data obtained by querying humans. Such a learned reward function can be used to align the model [1, 40, 41], score the generations during inference time to output more aligned answers [42] and to rank the generations of multiple models [43, 44]. Recent work from Rafailov et al. bypasses the status quo two-stage reward learning + RL pipeline and directly finetune on pairwise preferences, but still implicitly assumes the BTL model for ranking.

**ZH** 目标则是学习这个奖励函数 ⟦SLOT_31⟧：它以给定上下文 ⟦SLOT_33⟧ 下的输出 ⟦SLOT_32⟧（记作 ⟦SLOT_34⟧）为输入，将其映射为实值奖励分数，以逼近人类偏好。⟦SLOT_35⟧ 的学习借助通过向人类查询获得的大量成对比较数据完成。习得的奖励函数可用于对齐模型 [1, 40, 41]、在推理时为生成结果打分以输出更对齐的答案 [42]，以及对多个模型的生成结果排序 [43, 44]。Rafailov 等人的近期工作绕开了“奖励学习 + 强化学习”的两阶段现状，直接在成对偏好上微调，但其排序仍隐含地假设了 BTL 模型。

**EN** While most alignment literature focuses on the BTL modeling approach, we want to draw attention to the ideal point model [4] for preference learning.

**ZH** 尽管多数对齐文献聚焦于 BTL 建模思路，我们希望把注意力引向用于偏好学习的理想点模型 [4]。

**EN** Ideal point model was proposed by Coombs for human preference modeling in the psychology literature. The key idea behind this model is to exploit the geometry of the problem, assuming there exists a meaningful representation space for the items/alternates being compared. Let ⟦SLOT_36⟧ denote the domain of feature space of the concepts (items, objects, images, choices, etc.) with a distance associated with it. Preference learning based on ideal point model [4, 45, 46, 47, 48, 49, 50] assumes that there is an unknown ideal preference point ⟦SLOT_37⟧ that represents the reference point people use for their preference judgments based on distances. So, when asked “Do you prefer ⟦SLOT_38⟧ or ⟦SLOT_39⟧?”, they respond with ⟦SLOT_40⟧ as their preference if ⟦SLOT_41⟧ and vice versa, where ⟦SLOT_42⟧ are the feature representations of ⟦SLOT_43⟧ and ⟦SLOT_44⟧ respectively. That is, items that are closer to the user’s ideal preference points are preferred by the user over those that are farther away. The goal of preference learning then is to use the responses for pairwise comparison queries from people and learn the preference point ⟦SLOT_45⟧. Once we learn ⟦SLOT_46⟧, we can predict the choices people make between new unseen pairs. More formally, in general, the probability that ⟦SLOT_47⟧ beats ⟦SLOT_48⟧ in preference for user ⟦SLOT_49⟧ is given by,

**ZH** 理想点模型由 Coombs 在心理学文献中提出，用于人类偏好建模。该模型的关键思想是利用问题的几何结构，假设被比较的条目/备选项存在于一个有意义的表示空间中。令 ⟦SLOT_36⟧ 表示概念（条目、对象、图像、选项等）的特征空间域，并配有相应的距离。基于理想点模型的偏好学习 [4, 45, 46, 47, 48, 49, 50] 假设存在一个未知的理想偏好点 ⟦SLOT_37⟧，它代表人们基于距离作出偏好判断时所参照的参照点。因此，当被问到“你偏好 ⟦SLOT_38⟧ 还是 ⟦SLOT_39⟧？”时，若 ⟦SLOT_41⟧，他们会回答 ⟦SLOT_40⟧ 作为偏好，反之亦然，其中 ⟦SLOT_42⟧ 分别是 ⟦SLOT_43⟧ 与 ⟦SLOT_44⟧ 的特征表示。也就是说，用户更偏好离其理想偏好点更近的条目，而非更远的条目。于是偏好学习的目标就是利用人们对成对比较查询的回答来学习偏好点 ⟦SLOT_45⟧。一旦学到 ⟦SLOT_46⟧，我们就可预测人们在新未见对之间的选择。更形式化地，一般而言，对用户 ⟦SLOT_49⟧ 而言 ⟦SLOT_47⟧ 在偏好上胜过 ⟦SLOT_48⟧ 的概率为：

<!-- [原子块 · table] Pr ⁡ ( i ≻ j ) ∝ h ⁡ ( dist 2 ​ ( 𝐱 j , 𝐚 ) − dist 2 ​ ( 𝐱 i , 𝐚 ) ) , \Pr(i\succ j)\propto h(\text{dist}^{2}(\mathbf{x}_{j},\mathbf{a})-\text{dist}^{2}(\mathbf{x}_{i},\mathbf{a})), (3) -->

**EN** where ⟦SLOT_50⟧ is a link function [51] which can be any monotonic function such that ⟦SLOT_51⟧ when ⟦SLOT_52⟧ and ⟦SLOT_53⟧ when ⟦SLOT_54⟧. Essentially, the idea here is that the larger the difference in distance between the alternates to the ideal point, the easier it is to choose between them, and hence the answer is less noisy. In contrast, if the difference of distance is close to zero, the alternates seem to be equally good or bad to the user and therefore the probability of ⟦SLOT_55⟧ will be close to random.

**ZH** 其中 ⟦SLOT_50⟧ 为连接函数（link function）[51]，它可以是任意单调函数，满足：当 ⟦SLOT_52⟧ 时 ⟦SLOT_51⟧，当 ⟦SLOT_54⟧ 时 ⟦SLOT_53⟧。其核心思想是：备选项到理想点的距离差越大，二者之间越容易取舍，因而回答的噪声越小；反之，若距离之差接近于零，备选项对用户而言看起来同样好或同样差，⟦SLOT_55⟧ 的概率将接近随机。

**EN** 3 Framework for Pluralist Alignment (⟦SLOT_56⟧)

**ZH** 3 面向多元对齐的框架（⟦SLOT_56⟧）

**EN** In this section, we begin by describing how to view existing approaches that use the BTL model for alignment through the lens of the ideal point model, and then introduce our framework for pluralistic alignment.

**ZH** 本节先说明如何用理想点模型的视角看待现有使用 BTL 模型做对齐的方法，随后介绍我们的多元对齐框架。

**EN** 3.1 Viewing alignment through the lens of ideal point model and metric learning

**ZH** 3.1 从理想点模型与度量学习的视角看待对齐

**EN** The assumption in the ideal point model (Section 2) that the items being compared have representations in a vector space is mild one, especially while working with foundation models. However, assuming that the Euclidean distance or a known distance function in the representation space of these foundation models to be the correct notion of similarity and dissimilarity for human judgments is a strong one. We re-formulate the goal of alignment, i.e. learning a reward function, to learning a (potentially non-linear) transformation of the representation output by the foundation model where a known distance function, e.g., Euclidean distance or cosine similarity, is a good approximation (in the transformed space) to capture human judgments of similarity and dissimilarity.

**ZH** 理想点模型（第 2 节）假设被比较的条目在向量空间中有表示，这一假设相当温和，尤其是在使用基础模型时。然而，假设欧氏距离或这些基础模型表示空间中的某个已知距离函数就是人类判断相似与不相似的正确度量，则是一个很强的假设。我们重新表述对齐的目标——即学习奖励函数——使之成为：学习基础模型输出表示的一个（可能非线性的）变换，使得某个已知距离函数（如欧氏距离或余弦相似度）在该变换后的空间中能够很好地逼近人类对相似与不相似的判断。

**EN** Looking at the current alignment approaches using the BTL model through the lens of the ideal point model, we can re-interpret the Equation 2,

**ZH** 用理想点模型的视角审视当前使用 BTL 模型的对齐方法，我们可以把公式 2 重新解释为：

<!-- [原子块 · table] Pr ⁡ ( 𝐱 l ≻ 𝐱 r | 𝐱 c ) = 1 1 + exp ⁡ ( r θ ​ ( 𝐱 r , 𝐱 c ) − r θ ​ ( 𝐱 l , 𝐱 c ) ) . \Pr(\mathbf{x}_{l}\succ\mathbf{x}_{r}|\mathbf{x}_{c})=\frac{1}{1+\exp{(r_{\theta}(\mathbf{x}_{r};\mathbf{x}_{c})- -->

**EN** as an ideal point model where the difference of rewards is a proxy for the difference of distances11 1 We note that here reward function is a proxy and not real distance function. and the link function being the Sigmoid or logistic function.

**ZH** 一个理想点模型，其中奖励之差是距离之差的代理11 1 我们指出，这里的奖励函数是代理而非真实的距离函数，连接函数为 Sigmoid 或 logistic 函数。

**EN** By relaxing the requirement of the Sigmoid link function used by the BTL model and the known distance function by the ideal point model, we propose to view alignment from human preferences as learning a reward function that can generalize to the following:22 2 Note that in this view, the reward is lesser when it is preferred. So, one could rather think of this as cost or penalty function than reward function.

**ZH** 通过放宽 BTL 模型所用 Sigmoid 连接函数的要求，以及理想点模型对已知距离函数的要求，我们提出把从人类偏好出发的对齐视为学习一个能泛化到如下形式的奖励函数：22 2 注意，在这一视角下，越受偏好时奖励反而越小。因此，与其把它看作奖励函数，不如看作代价或惩罚函数。

<!-- [原子块 · table] Pr ⁡ ( 𝐱 l ≻ 𝐱 r | 𝐱 c ) = h ⁡ ( r θ ​ ( 𝐱 r , 𝐱 c ) − r θ ​ ( 𝐱 l , 𝐱 c ) ) , \Pr(\mathbf{x}_{l}\succ\mathbf{x}_{r}|\mathbf{x}_{c})=h(r_{\theta}(\mathbf{x}_{r};\mathbf{x}_{c})-r_{\theta}(\mathbf{x}_{ -->

**EN** where ⟦SLOT_57⟧ any monotonic link function appropriately normalized to obtain probabilities such that ⟦SLOT_58⟧ when ⟦SLOT_59⟧, i.e., there is a clear winner between items, and ⟦SLOT_60⟧ when ⟦SLOT_61⟧, i.e., the winner is random.

**ZH** 其中 ⟦SLOT_57⟧ 为经过适当归一化以得到概率的任意单调连接函数，满足：当 ⟦SLOT_59⟧ 时 ⟦SLOT_58⟧，即条目之间有明确胜者；当 ⟦SLOT_61⟧ 时 ⟦SLOT_60⟧，即胜者是随机的。

**EN** We instantiate the reward function in the following ways:

**ZH** 我们以如下方式实例化奖励函数：

**EN** 1. With unknown but fixed ideal point, unknown representation space for jointly representing the prompt input ⟦SLOT_62⟧ and the corresponding output ⟦SLOT_63⟧ from the foundation model and Euclidean distance, we model the reward function as, ⟦SLOT_64⟧, where mapping ⟦SLOT_65⟧ and ideal point ⟦SLOT_66⟧ are unknown and learned from pairwise comparison queries. This corresponds to the following pairwise ranking model, ⟦SLOT_67⟧ (6)

**ZH** 1. 在理想点未知但固定、用于联合表示基础模型提示词输入 ⟦SLOT_62⟧ 与相应输出 ⟦SLOT_63⟧ 的表示空间未知、且采用欧氏距离的情况下，我们把奖励函数建模为 ⟦SLOT_64⟧，其中映射 ⟦SLOT_65⟧ 与理想点 ⟦SLOT_66⟧ 均未知，需从成对比较查询中学习。这对应于如下成对排序模型：⟦SLOT_67⟧（6）

**EN** 2. The user ideal point is an unknown function of the prompt ⟦SLOT_68⟧ and distance is the angle between the ideal point conditioned on the prompt and the unknown representation space for the output ⟦SLOT_69⟧ from the foundation model, ⟦SLOT_70⟧, where the mappings ⟦SLOT_71⟧ and ⟦SLOT_72⟧ map ⟦SLOT_73⟧ and are unknown and are learned from pairwise comparisons. Here we assume that the range spaces of ⟦SLOT_74⟧ and ⟦SLOT_75⟧ are normalized to use the angle as the distance function. This corresponds to the following pairwise ranking model, ⟦SLOT_76⟧ (7)

**ZH** 2. 用户理想点是提示词 ⟦SLOT_68⟧ 的未知函数，距离是以提示词为条件的理想点与基础模型输出 ⟦SLOT_69⟧ 的未知表示空间之间的夹角，即 ⟦SLOT_70⟧，其中映射 ⟦SLOT_71⟧ 与 ⟦SLOT_72⟧ 映射 ⟦SLOT_73⟧，且均未知，需从成对比较中学习。此处我们假设 ⟦SLOT_74⟧ 与 ⟦SLOT_75⟧ 的值域已归一化，以便用夹角作为距离函数。这对应于如下成对排序模型：⟦SLOT_76⟧（7）

**EN** 3.2 Modeling diverse preferences

**ZH** 3.2 对多样化偏好建模

**EN** So far our discussion has focused on viewing the current alignment methods which assume a homogeneous model. That is, all users’ preferences are assumed to arrive from a universal model with disagreements modeled as noise. A natural extension to individualized modeling can be written as follows. For user ⟦SLOT_77⟧, ⟦SLOT_78⟧,where ⟦SLOT_79⟧ is any monotonic link function that can be dependent on the individual and the query, and ⟦SLOT_80⟧ denotes the reward function for individual ⟦SLOT_81⟧. We do not assume the knowledge of the link function for our learning algorithms (Section 3.3.2). One could use these models at a single-user level to learn a personalized model using lots of data from that specific user. However, such models will not generalize to other individuals.

**ZH** 到目前为止，我们的讨论聚焦于如何看待假设同质模型的现有对齐方法，即假设所有用户的偏好都来自一个通用模型，分歧被建模为噪声。一种向个体化建模的自然扩展可写作：对用户 ⟦SLOT_77⟧，⟦SLOT_78⟧，其中 ⟦SLOT_79⟧ 是任意单调连接函数（可依赖于个体与查询），⟦SLOT_80⟧ 表示个体 ⟦SLOT_81⟧ 的奖励函数。我们的学习算法并不假设已知连接函数（第 3.3.2 节）。人们可以在单用户层面使用这些模型，用来自该特定用户的大量数据学习个性化模型，但这类模型无法泛化到其他个体。

**EN** In reality, different people can have different preferences that are not just noisy perturbations of a universal model. That is, people can differ in systematically different ways. However, there are shared aspects across subgroups of people, e.g., owing to demographics, educational, socio-cultural, or other types of similarities. We propose a framework to capture human preferences by considering these differences and similarities by modeling the preferences of individuals with a low-rank model. In particular, we use a mixture modeling approach for capturing diverse preferences where we model each user as a convex combination of ⟦SLOT_82⟧ prototypes.

**ZH** 现实中，不同的人可以有各不相同的偏好，这些偏好并非只是通用模型上的噪声扰动，也就是说，人们可能以系统性的不同方式存在差异。不过，人群的子群体之间也存在共通之处，例如源于人口统计学、教育、社会文化或其他类型的相似性。我们提出一个框架，通过用低秩模型对个体偏好建模来兼顾这些差异与共性。具体地，我们采用混合建模方法捕捉多样化偏好，把每个用户建模为 ⟦SLOT_82⟧ 个原型的凸组合。

**EN** Model A: Diverse preference with fixed preference points. Here each user’s ideal point is modeled as a convex combination of ⟦SLOT_83⟧ prototypical ideal points, ⟦SLOT_84⟧ with ⟦SLOT_85⟧. The corresponding preference model is given as follows:

**ZH** 模型 A：具有固定偏好点的多样化偏好。此处每个用户的理想点被建模为 ⟦SLOT_83⟧ 个原型化理想点的凸组合，即 ⟦SLOT_84⟧，其中 ⟦SLOT_85⟧。相应的偏好模型如下：

<!-- [原子块 · table] Model A: Pr i ( 𝐱 l ≻ 𝐱 r | 𝐱 c ) = h ( | | f ( 𝐱 r ; 𝐱 c ) − f ( 𝐚 ( i ) ) | | 2 2 − | | f ( 𝐱 l ; 𝐱 c ) − f ( 𝐚 ( i ) ) | | 2 2 ) , \textbf{Model A: }\quad\text{$\Pr$}_{i}(\mathbf{x}_{l}\succ\mathbf -->

**EN** where ⟦SLOT_86⟧ with the weights ⟦SLOT_87⟧ and ⟦SLOT_88⟧. Denoting ⟦SLOT_89⟧ and ⟦SLOT_90⟧, where ⟦SLOT_91⟧ lies in ⟦SLOT_92⟧-dimensional simplex denoted by ⟦SLOT_93⟧.

**ZH** 其中 ⟦SLOT_86⟧，权重为 ⟦SLOT_87⟧ 且 ⟦SLOT_88⟧。记 ⟦SLOT_89⟧ 与 ⟦SLOT_90⟧，其中 ⟦SLOT_91⟧ 位于 ⟦SLOT_92⟧ 维单纯形（记作 ⟦SLOT_93⟧）中。

**EN** Model B: Diverse preference with preference points as function of input prompt. Here each user’s ideal point is modeled as a convex combination of ⟦SLOT_94⟧ prototypical functions that map input prompts to ideal points, ⟦SLOT_95⟧. The corresponding preference model is given as follows:

**ZH** 模型 B：以偏好点作为输入提示词函数的多样化偏好。此处每个用户的理想点被建模为 ⟦SLOT_94⟧ 个把输入提示词映射为理想点的原型化函数的凸组合，即 ⟦SLOT_95⟧。相应的偏好模型如下：

<!-- [原子块 · table] Model B: Pr i ( 𝐱 l ≻ 𝐱 r | 𝐱 c ) = h ( ⟨ f ( 𝐱 r ) , z ( i ) ( 𝐱 c ) ⟩ − ⟨ f ( 𝐱 l ) , z ( i ) ( 𝐱 c ) ⟩ ) , \textbf{Model B: }\quad\text{$\Pr$}_{i}(\mathbf{x}_{l}\succ\mathbf{x}_{r}|\mathbf{x}_{c})= -->

**EN** where ⟦SLOT_96⟧ with ⟦SLOT_97⟧ and ⟦SLOT_98⟧.

**ZH** 其中 ⟦SLOT_96⟧，且 ⟦SLOT_97⟧、⟦SLOT_98⟧。

**EN** We drop the superscript ⟦SLOT_99⟧ on ⟦SLOT_100⟧ for simplicity, however, we note that the link function need not be the same for all users and furthermore, our learning algorithm described in Section 3.3 does not need to know the link function(s). We illustrate the ⟦SLOT_101⟧ framework in Figure 1 and Figure 6 (Appendix A).

**ZH** 为简洁起见，我们省略了 ⟦SLOT_100⟧ 上的上标 ⟦SLOT_99⟧；但需要说明，连接函数不必对所有用户都相同，而且我们在第 3.3 节描述的学习算法无需知道连接函数。我们在图 1 与图 6（附录 A）中展示了 ⟦SLOT_101⟧ 框架。

**EN** 3.3 Learning ⟦SLOT_102⟧ models from Diverse Preferences

**ZH** 3.3 从多样化偏好中学习 ⟦SLOT_102⟧ 模型

**EN** Given a dataset of answers to pairwise comparison queries, ⟦SLOT_103⟧, where ⟦SLOT_104⟧ denote the number of pairs answered by user ⟦SLOT_105⟧, the goal of the learning algorithm in the ⟦SLOT_106⟧ framework is to learn the mappings and prototypes shared across the population, and for each user ⟦SLOT_107⟧ the weights ⟦SLOT_108⟧ with ⟦SLOT_109⟧ and ⟦SLOT_110⟧. For model A, mapping ⟦SLOT_111⟧ and the prototypes ⟦SLOT_112⟧ are shared, while for model B, are the mapping ⟦SLOT_113⟧ and the prototype mappings ⟦SLOT_114⟧ shared. Without loss of generality, we have assumed that ⟦SLOT_115⟧ is preferred over ⟦SLOT_116⟧. So, this is learning problem is can be looked at as a supervised learning setting with binary labels.

**ZH** 给定成对比较查询的回答数据集 ⟦SLOT_103⟧（其中 ⟦SLOT_104⟧ 表示用户 ⟦SLOT_105⟧ 回答的比较对数），⟦SLOT_106⟧ 框架中学习算法的目标是：学习全人群共享的映射与原型，并为每个用户 ⟦SLOT_107⟧ 学习权重 ⟦SLOT_108⟧，满足 ⟦SLOT_109⟧ 与 ⟦SLOT_110⟧。对模型 A，共享的是映射 ⟦SLOT_111⟧ 与原型 ⟦SLOT_112⟧；对模型 B，共享的是映射 ⟦SLOT_113⟧ 与原型映射 ⟦SLOT_114⟧。不失一般性，我们假设 ⟦SLOT_115⟧ 优于 ⟦SLOT_116⟧。因此，该学习问题可视为带二值标签的监督学习设置。

**EN** 3.3.1 Generalization over seen users versus unseen users

**ZH** 3.3.1 对已见用户的泛化与对未见用户的泛化

**EN** When learning a reward function from diverse preferences, there are two types of generalization to consider. (1) Generalization for unseen pairs for seen users, i.e., predicting well for new pairs for the people for whom the weights have already been learned from the training data. We call this seen accuracy. (2) Generalization is for unseen users, i.e., predicting well for people whose data was not part of the training data at all. For such new users, some part of their new data will be used to localize them within the learned model by only learning the weights for the new user by keeping the shared mappings and prototypes fixed. We call this unseen accuracy. We also note that we can use the weighted combination of the prototypes, i.e., an average of all the seen users, as the zero-shot ideal point for new users. However, we emphasize that it is important for reward functions to generalize to unseen users and our framework provides a natural way to localize the new user.

**ZH** 从多样化偏好中学习奖励函数时，需要考虑两类泛化。(1) 对已见用户的未见比较对的泛化，即对于那些权重已在训练数据中学得的用户，能很好地预测新的比较对，我们称之为已见准确率。(2) 对未见用户的泛化，即对于那些数据完全不出现在训练数据中的人也能很好地预测。对于这类新用户，其新数据中的一部分将被用于在所学模型中定位他们——只学习新用户的权重，同时保持共享映射与原型固定，我们称之为未见准确率。我们还要指出，可以把原型的加权组合（即所有已见用户的平均）作为新用户的零样本理想点。不过我们强调，奖励函数能够泛化到未见用户十分重要，而我们的框架提供了一种定位新用户的自然方式。

**EN** 3.3.2 Learning Algorithm

**ZH** 3.3.2 学习算法

**EN** Given the dataset ⟦SLOT_117⟧, loss function ⟦SLOT_118⟧ and model class for ⟦SLOT_119⟧, the learning algorithm for model A starts by randomly initializing the prototypes ⟦SLOT_120⟧, ⟦SLOT_121⟧, user weights ⟦SLOT_122⟧, where ⟦SLOT_123⟧. Then, in each iteration until convergence criteria, the following steps are repeated,

**ZH** 给定数据集 ⟦SLOT_117⟧、损失函数 ⟦SLOT_118⟧ 与 ⟦SLOT_119⟧ 的模型类，模型 A 的学习算法首先随机初始化原型 ⟦SLOT_120⟧、⟦SLOT_121⟧ 与用户权重 ⟦SLOT_122⟧，其中 ⟦SLOT_123⟧。随后，在每次迭代中重复以下步骤，直至满足收敛准则：

**EN** • Sample a random mini-batch ⟦SLOT_124⟧ of comparison data from ⟦SLOT_125⟧.

**ZH** • 从 ⟦SLOT_125⟧ 中随机采样一个小批量 ⟦SLOT_124⟧ 的比较数据。

**EN** • Compute user ideal points: ⟦SLOT_126⟧.

**ZH** • 计算用户理想点：⟦SLOT_126⟧。

**EN** • Compute distances: ⟦SLOT_127⟧, ⟦SLOT_128⟧.

**ZH** • 计算距离：⟦SLOT_127⟧、⟦SLOT_128⟧。

**EN** • Loss for each comparison ⟦SLOT_129⟧ for user ⟦SLOT_130⟧: ⟦SLOT_131⟧.

**ZH** • 用户 ⟦SLOT_130⟧ 的每次比较 ⟦SLOT_129⟧ 的损失：⟦SLOT_131⟧。

**EN** • Update Step: ⟦SLOT_132⟧.

**ZH** • 更新步骤：⟦SLOT_132⟧。

**EN** The above steps describe updating the learning algorithm for model A. Similarly, the dataset ⟦SLOT_133⟧, loss function ⟦SLOT_134⟧ and model class for ⟦SLOT_135⟧, the learning algorithm for model B starts by randomly initializing the prototype functions ⟦SLOT_136⟧, where each ⟦SLOT_137⟧ is a function that maps ⟦SLOT_138⟧ to ⟦SLOT_139⟧, user weights ⟦SLOT_140⟧, where ⟦SLOT_141⟧. Then, in each iteration until convergence criteria, the following steps are repeated,

**ZH** 上述步骤描述了模型 A 学习算法的更新过程。类似地，给定数据集 ⟦SLOT_133⟧、损失函数 ⟦SLOT_134⟧ 与 ⟦SLOT_135⟧ 的模型类，模型 B 的学习算法首先随机初始化原型函数 ⟦SLOT_136⟧（其中每个 ⟦SLOT_137⟧ 是一个把 ⟦SLOT_138⟧ 映射到 ⟦SLOT_139⟧ 的函数）与用户权重 ⟦SLOT_140⟧，其中 ⟦SLOT_141⟧。随后，在每次迭代中重复以下步骤，直至满足收敛准则：

**EN** • Sample a random mini-batch ⟦SLOT_142⟧ of comparison data from ⟦SLOT_143⟧.

**ZH** • 从 ⟦SLOT_143⟧ 中随机采样一个小批量 ⟦SLOT_142⟧ 的比较数据。

**EN** • Compute user ideal points: ⟦SLOT_144⟧.

**ZH** • 计算用户理想点：⟦SLOT_144⟧。

**EN** • Compute distances: ⟦SLOT_145⟧, ⟦SLOT_146⟧.

**ZH** • 计算距离：⟦SLOT_145⟧、⟦SLOT_146⟧。

**EN** • Loss for each comparison ⟦SLOT_147⟧ for user ⟦SLOT_148⟧: ⟦SLOT_149⟧.

**ZH** • 用户 ⟦SLOT_148⟧ 的每次比较 ⟦SLOT_147⟧ 的损失：⟦SLOT_149⟧。

**EN** • Update Step: ⟦SLOT_150⟧.

**ZH** • 更新步骤：⟦SLOT_150⟧。

**EN** See Appendix D for pseudocode details.

**ZH** 伪代码细节见附录 D。

**EN** 4 Experiments

**ZH** 4 实验

**EN** We conduct extensive experiments on simulated (Section 4.1), semi-synthetic (Section 4.2), and real (Section 4.3) preference datasets for both text and image generation tasks to demonstrate that our proposed ⟦SLOT_151⟧ (Pluralistic ALignment) framework can: (1) effectively capture the diversity of user preferences, thereby outperforming existing homogeneous reward models; (2) efficiently achieve performance comparable to the existing SoTA reward models with far fewer parameters and compute costs; and (3) be versatile and applied to different domains.

**ZH** 我们在模拟（第 4.1 节）、半合成（第 4.2 节）与真实（第 4.3 节）偏好数据集上，针对文本与图像生成任务开展了大量实验，以证明我们所提出的 ⟦SLOT_151⟧（Pluralistic ALignment，多元对齐）框架能够：(1) 有效捕捉用户偏好的多样性，从而优于现有的同质奖励模型；(2) 以远少的参数量与计算开销高效达到与现有 SoTA 奖励模型相当的性能；(3) 具备通用性，可应用于不同领域。

**EN** For experiments on semi-synthetic and real preference datasets, a simple two-layer MLP ⟦SLOT_152⟧ reward model can achieve or exceed the performance of existing status quo reward models, which often contain billions of parameters.

**ZH** 在半合成与真实偏好数据集上的实验表明，一个简单的两层 MLP ⟦SLOT_152⟧ 奖励模型即可达到或超过现有主流奖励模型的性能，而后者往往包含数十亿参数。

**EN** Compute Resources. We conducted most of our experiments using 4 RTX 4090, each with 24 GB of VRAM. All of our experiments can be run on a single RTX 4090 with RAM and VRAM usage of less than 16 GB. A typical experiment can be finished within 2 hours.

**ZH** 算力资源。我们的多数实验使用 4 张 RTX 4090 完成，每张显存 24 GB。我们所有的实验都能在单张 RTX 4090 上运行，内存与显存占用均低于 16 GB。一个典型实验可在 2 小时内完成。

**EN** 4.1 Heterogeneous Synthetic Dataset

**ZH** 4.1 异质合成数据集

**EN** Dataset. We synthesize a simple preference dataset with the normal distribution (we use a setting similar to [45]) and true ⟦SLOT_153⟧ is linear and the weight ⟦SLOT_154⟧. Let ⟦SLOT_155⟧ denote the ⟦SLOT_156⟧ item.

**ZH** 数据集。我们用正态分布合成了一个简单的偏好数据集（设置与 [45] 类似），真实的 ⟦SLOT_153⟧ 为线性，权重为 ⟦SLOT_154⟧。令 ⟦SLOT_155⟧ 表示第 ⟦SLOT_156⟧ 个条目。

**EN** Experiment Setup. Assume ⟦SLOT_157⟧ user prototypes ⟦SLOT_158⟧, where ⟦SLOT_159⟧ with the minimum distance constraint ⟦SLOT_160⟧. We consider two settings: 1) a mixture setting, where we assume each user is located in the convex hull of ⟦SLOT_161⟧ prototypes; 2) a simpler partition setting, where we assume ⟦SLOT_162⟧ users are evenly sampled from ⟦SLOT_163⟧ prototypes, with ⟦SLOT_164⟧. Each sample is generated as follows: we randomly draw two items ⟦SLOT_165⟧ and one user ⟦SLOT_166⟧, and label the user’s preference as ⟦SLOT_167⟧. We generate a total of ⟦SLOT_168⟧ samples per user to learn the user’s ideal point. We use model A with a single-layer MLP (without bias) with hinge loss and evaluate on the held-out test set.

**ZH** 实验设置。假设有 ⟦SLOT_157⟧ 个用户原型 ⟦SLOT_158⟧，其中 ⟦SLOT_159⟧ 满足最小距离约束 ⟦SLOT_160⟧。我们考虑两种设置：1) 混合设置，即假设每个用户位于 ⟦SLOT_161⟧ 个原型的凸包内；2) 更简单的划分设置，即假设 ⟦SLOT_162⟧ 个用户从 ⟦SLOT_163⟧ 个原型中均匀采样，其中 ⟦SLOT_164⟧。每个样本生成如下：随机抽取两个条目 ⟦SLOT_165⟧ 与一个用户 ⟦SLOT_166⟧，并把用户的偏好标注为 ⟦SLOT_167⟧。我们为每个用户生成共计 ⟦SLOT_168⟧ 个样本以学习该用户的理想点。我们使用带铰链损失的单层 MLP（无偏置）作为模型 A，并在留出的测试集上评估。

<!-- [原子块 · img]  -->

**EN** Figure 2: The performance of model A on the simulation datasets with ⟦SLOT_169⟧, ⟦SLOT_170⟧, ⟦SLOT_171⟧, ⟦SLOT_172⟧, and mixture user ideal point setting. For the fig 2(a) visualization, we set ⟦SLOT_173⟧, ⟦SLOT_174⟧, ⟦SLOT_175⟧.

**ZH** 图 2：模型 A 在 ⟦SLOT_169⟧、⟦SLOT_170⟧、⟦SLOT_171⟧、⟦SLOT_172⟧ 以及混合用户理想点设置下的模拟数据集上的性能。在图 2(a) 的可视化中，我们设 ⟦SLOT_173⟧、⟦SLOT_174⟧、⟦SLOT_175⟧。

**EN** Results. We simulate datasets with multiple settings (different true ⟦SLOT_176⟧, ⟦SLOT_177⟧ and, ⟦SLOT_178⟧ in both mixture and partition settings – see Appendix C.1 for details) and evaluate our model A on these simulation datasets with different # samples and # prototypes. Figure 2(a) shows that ⟦SLOT_179⟧ can align the user ideal points to the true user ideal points in the representation space. See Appendix C.1 for more detailed results. Figure 2(b) shows that the homogeneous reward model (# prototypes = 1) can only achieve sub-optimal performance on the simulated dataset when diverse preferences exist. When we learn pluralistic preferences by setting multiple learnable prototypes with ⟦SLOT_180⟧, we gain a significant ⟦SLOT_181⟧ accuracy boost. Figure 2(c) shows that as we increase the number of training samples for seen users, ⟦SLOT_182⟧ achieves higher test accuracy, and is also more accurate in capturing the true number of prototypes in the dataset (which we know from simulations).

**ZH** 结果。我们在多种设置下模拟数据集（不同的真实 ⟦SLOT_176⟧、⟦SLOT_177⟧ 与 ⟦SLOT_178⟧，涵盖混合与划分两种设置——详见附录 C.1），并在这些模拟数据集上以不同的样本数与原型数评估模型 A。图 2(a) 显示 ⟦SLOT_179⟧ 能把用户理想点在表示空间中对齐到真实的用户理想点，更细致的结果见附录 C.1。图 2(b) 显示，当存在多样化偏好时，同质奖励模型（原型数 = 1）在模拟数据集上只能达到次优性能；而当我们以 ⟦SLOT_180⟧ 设置多个可学习原型来学习多元偏好时，获得了显著的 ⟦SLOT_181⟧ 准确率提升。图 2(c) 显示，随着已见用户训练样本数的增加，⟦SLOT_182⟧ 的测试准确率提高，并且在捕捉数据集中真实原型数量（我们由模拟得知）上也更为准确。

**EN** Remark. Recall that seen users are the users whose data is a part of the training data and the accuracy for them is measured on prediction on unseen pairs using the weights learned during training. Notice that without enough samples per user, learning diverse preferences can harm the performance, which indicates the importance of sample size in pluralistic preference learning. Figure 2(d) presents ⟦SLOT_183⟧’s potential to generalize to unseen users. Without any further fine-tuning of the well-trained ⟦SLOT_184⟧ reward model (trained with 100 samples per seen user), we can simply learn a new weight for new unseen users with limited labeled samples to achieve prediction accuracy similar to that of seen users. That is, we keep the prototypes and mappings learned fixed, but only train the weights for the new user using a few comparison samples. We note that for alignment to be truly effective, it needs to generalize to new users beyond the set of users whose comparison data are part of the training dataset. Therefore, we clearly distinguish between accuracy for unseen pairs for seen users versus accuracy for unseen users.

**ZH** 评注。回顾一下：已见用户是指其数据属于训练数据的用户，其准确率是在用训练中学得的权重对未见比较对做预测时测得的。注意，若每用户样本不足，学习多样化偏好反而会损害性能，这说明样本量在多元偏好学习中的重要性。图 2(d) 展示了 ⟦SLOT_183⟧ 泛化到未见用户的潜力：无需对训练良好的 ⟦SLOT_184⟧ 奖励模型（以每已见用户 100 个样本训练）做任何进一步微调，我们只需用少量有标签样本为新的未见用户学习一个新权重，即可达到与已见用户相近的预测准确率。也就是说，我们保持学到的原型与映射固定，只用少量比较样本训练新用户的权重。我们指出，要让对齐真正有效，它必须能泛化到训练数据集所含用户之外的新用户，因此我们明确区分“已见用户在未见比较对上的准确率”与“未见用户的准确率”。

**EN** 4.2 Heterogeneous Semi-Synthetic Datasets

**ZH** 4.2 异质半合成数据集

**EN** We evaluate the performance of ⟦SLOT_185⟧ on semi-synthetic datasets which we construct by injecting diversity into real preference datasets for both text generation and image synthesis tasks. Our results show that ⟦SLOT_186⟧ can achieve or surpass existing state-of-the-art (SoTA) large reward models with only 2-layer MLP networks.

**ZH** 我们在半合成数据集上评估 ⟦SLOT_185⟧ 的性能——这些数据集通过向真实的文本生成与图像合成偏好数据集中注入多样性而构建。结果表明，⟦SLOT_186⟧ 仅用 2 层 MLP 网络即可达到或超越现有当前最优（SoTA）的大型奖励模型。

**EN** 4.2.1 Persona Dataset

**ZH** 4.2.1 Persona 数据集

**EN** Anthropic’s Persona dataset [7] consists of a series of personalities (personas), each corresponding with 500 statements that agree with the persona and 500 statements that do not. We denote the set of statements that agrees with a persona ⟦SLOT_187⟧ as ⟦SLOT_188⟧. We construct a semi-synthetic dataset using Anthropic’s Persona to evaluate ⟦SLOT_189⟧.

**ZH** Anthropic 的 Persona 数据集 [7] 由一系列人格（persona）构成，每个人格对应 500 条与该人格相符的陈述与 500 条不相符的陈述。我们把与人格 ⟦SLOT_187⟧ 相符的陈述集合记为 ⟦SLOT_188⟧。我们用 Anthropic 的 Persona 构建了一个半合成数据集来评估 ⟦SLOT_189⟧。

**EN** Dataset. Let ⟦SLOT_190⟧ denote the set of personas that exists in our semi-synthetic heterogeneous dataset with ⟦SLOT_191⟧ “true” preference groups i.e. each person (user) has one of the ⟦SLOT_192⟧ personalities. For each ⟦SLOT_193⟧, we generate ⟦SLOT_194⟧ synthetic seen and unseen users, where a seen user provides preference samples in the training and test sets, while the unseen user only provides samples in the test set. For each seen synthetic user, we generate ⟦SLOT_195⟧ queries that ask if the user agrees with a given statement from the persona dataset. For each unseen synthetic user, we generate ⟦SLOT_196⟧ queries. If the statement aligns with the persona ⟦SLOT_197⟧ of the user, i.e. the statement belongs to ⟦SLOT_198⟧, then the user answers yes, otherwise no. Table 1 lists the personas we used to create the dataset for each ⟦SLOT_199⟧. Figure 3 shows a sample question.

**ZH** 数据集。令 ⟦SLOT_190⟧ 表示我们的半合成异质数据集中的人格集合，共含 ⟦SLOT_191⟧ 个“真实”偏好组，即每个人（用户）具有 ⟦SLOT_192⟧ 种人格之一。对每个 ⟦SLOT_193⟧，我们生成 ⟦SLOT_194⟧ 个合成的已见用户与未见用户，其中已见用户在训练集与测试集中都提供偏好样本，而未见用户只在测试集中提供样本。对每个已见的合成用户，我们生成 ⟦SLOT_195⟧ 条查询，询问该用户是否同意 Persona 数据集中的某条陈述；对每个未见的合成用户，我们生成 ⟦SLOT_196⟧ 条查询。若该陈述与用户的人格 ⟦SLOT_197⟧ 相符，即该陈述属于 ⟦SLOT_198⟧，则用户回答“是”，否则回答“否”。表 1 列出了我们在每个 ⟦SLOT_199⟧ 下用于构建数据集的人格。图 3 展示了一个样例问题。

<!-- [原子块 · table] K ⋆ K^{\star} Personas 2 interest in art, interest in literature 3 interest in art, interest in literature, interest in math 4 interest in art, interest in literature, interest in math, interest in mu -->

**EN** Table 1: Personas used for each ⟦SLOT_200⟧ in our heteogeneous persona dataset.

**ZH** 表 1：我们的异质 persona 数据集中每个 ⟦SLOT_200⟧ 所使用的人格。

<!-- [原子块 · img]  -->

**EN** Figure 3: An example of pairwise comparison query with a prompt from our heterogeneous persona dataset generated using Anthropic’s Persona. A synthetic user who is assigned with a persona of interest in art will have a ground truth of ⟦SLOT_201⟧ by answering no, whereas a user who is assigned with interest in math pairs with a ground truth of ⟦SLOT_202⟧ by answering yes.

**ZH** 图 3：用 Anthropic 的 Persona 生成的异质 persona 数据集中的一个成对比较查询示例。被赋予“对艺术感兴趣”人格的合成用户，其真值为 ⟦SLOT_201⟧（回答“否”）；而被赋予“对数学感兴趣”的用户，其真值为 ⟦SLOT_202⟧（回答“是”）。

**EN** Experiment Setup. We evaluate the performance of model B with logistic loss on the heterogeneous persona dataset in various settings. We use model B, which accounts for user-specific variance in conditioning (text prompt), as the prompts in the dataset are the only quantities that differ from question to question. To examine the impact of various hyperparameters, we conduct experiments varying the number of true prototypes in the dataset ⟦SLOT_203⟧, number of prototypical groups used in the model ⟦SLOT_204⟧, queries per seen user ⟦SLOT_205⟧ and latent dimension ⟦SLOT_206⟧ with fixed number of users per group ⟦SLOT_207⟧ as seen in Figure 4.

**ZH** 实验设置。我们在异质 persona 数据集上、在多种设置下评估带逻辑损失的模型 B 的性能。我们采用模型 B，因为它考虑了条件（文本提示词）上用户特定的变化，而数据集中各问题之间唯一的差异正是提示词。为考察各超参数的影响，我们在固定每组用户数 ⟦SLOT_207⟧ 的情况下，改变数据集中真实原型的数量 ⟦SLOT_203⟧、模型所用原型组的数量 ⟦SLOT_204⟧、每已见用户的查询数 ⟦SLOT_205⟧ 与潜维度 ⟦SLOT_206⟧，如图 4 所示。

**EN** (a) Varying ⟦SLOT_208⟧ and ⟦SLOT_209⟧ while fixing ⟦SLOT_210⟧, ⟦SLOT_211⟧.

**ZH** (a) 改变 ⟦SLOT_208⟧ 与 ⟦SLOT_209⟧，固定 ⟦SLOT_210⟧、⟦SLOT_211⟧。

**EN** (b) Varying ⟦SLOT_212⟧ and ⟦SLOT_213⟧ while fixing ⟦SLOT_214⟧, and ⟦SLOT_215⟧.

**ZH** (b) 改变 ⟦SLOT_212⟧ 与 ⟦SLOT_213⟧，固定 ⟦SLOT_214⟧ 与 ⟦SLOT_215⟧。

**EN** (c) Varying ⟦SLOT_216⟧ and ⟦SLOT_217⟧ while fixing ⟦SLOT_218⟧, and ⟦SLOT_219⟧.

**ZH** (c) 改变 ⟦SLOT_216⟧ 与 ⟦SLOT_217⟧，固定 ⟦SLOT_218⟧ 与 ⟦SLOT_219⟧。

**EN** (d) Varying ⟦SLOT_220⟧ and ⟦SLOT_221⟧ while fixing ⟦SLOT_222⟧, ⟦SLOT_223⟧, and ⟦SLOT_224⟧.

**ZH** (d) 改变 ⟦SLOT_220⟧ 与 ⟦SLOT_221⟧，固定 ⟦SLOT_222⟧、⟦SLOT_223⟧ 与 ⟦SLOT_224⟧。

**EN** Results. We repeat these experiments five times and report the mean ⟦SLOT_225⟧ one standard deviation as bar plots in Figure 4. Figure 4 (a, b) illustrates the generalization performance of ⟦SLOT_226⟧ on the heterogeneous persona dataset. We observe that as ⟦SLOT_227⟧, the seen accuracy increases to 100% given a sufficient number of users and number of comparisons per user. Figure 4 (b) shows that as we get more comparisons per user, we achieve reasonable seen user accuracy, i.e. we can generalize to unseen pairs for users who are seen (provide training samples) in the dataset. Figure 4 (c) shows that the size of latent dimension ⟦SLOT_228⟧ does not affect the seen accuracy dramatically. Figure 4(d) shows the accuracy for unseen users, i.e., users who do not provide training samples. When ⟦SLOT_229⟧, there is no further learning needed to generalize to new users. However, when ⟦SLOT_230⟧, we require weights over the ⟦SLOT_231⟧ prototypes that we have not yet learned. To learn these new user weights, as discussed in Section 3.3.1, we fix the ⟦SLOT_232⟧ prototypes and the mapping ⟦SLOT_233⟧, and use only a few test data samples to learn the user weights (few-shot). We use these learned weights to make predictions on the remaining test data (Also see Remark, Section 4.1). From Figure 4(d) we see that for ⟦SLOT_234⟧ the number of samples used to learn weights makes no difference, since there are no weights to learn over a single prototype. For ⟦SLOT_235⟧, we see that as we use more data for learning the new user weights, the performance shows diminishing returns until saturation. We also demonstrate that as the number of prototypes ⟦SLOT_236⟧ increase, more comparisons per user are needed to learn the new user weights, since the dimension of the weight vector increases with ⟦SLOT_237⟧.

**ZH** 结果。我们重复这些实验五次，并在图 4 中以柱状图报告均值 ⟦SLOT_225⟧ 一个标准差。图 4 (a, b) 展示了 ⟦SLOT_226⟧ 在异质 persona 数据集上的泛化性能。我们观察到，随着 ⟦SLOT_227⟧，在用户数与每用户比较数充足时，已见准确率升至 100%。图 4 (b) 显示，随着每用户比较数增加，我们取得了合理的已见用户准确率，即能够对数据集中已见（提供训练样本）用户的未见比较对泛化。图 4 (c) 显示，潜维度 ⟦SLOT_228⟧ 的大小不会显著影响已见准确率。图 4(d) 展示了未见用户（即不提供训练样本的用户）的准确率：当 ⟦SLOT_229⟧ 时，泛化到新用户无需进一步学习；而当 ⟦SLOT_230⟧ 时，我们需要在我们尚未学得的 ⟦SLOT_231⟧ 个原型上的权重。为学习这些新用户权重，如第 3.3.1 节所述，我们固定 ⟦SLOT_232⟧ 个原型与映射 ⟦SLOT_233⟧，只用少量测试数据样本学习用户权重（少样本），再用所学权重对剩余测试数据做预测（另见第 4.1 节评注）。从图 4(d) 可见，对 ⟦SLOT_234⟧ 而言，用于学习权重的样本数没有影响，因为单一原型之上没有权重可学；而对 ⟦SLOT_235⟧，随着用于学习新用户权重的数据增多，性能呈现递减回报直至饱和。我们还证明，随着原型数 ⟦SLOT_236⟧ 增加，学习新用户权重所需的每用户比较数也随之增加，因为权重向量的维度随 ⟦SLOT_237⟧ 增大。

<!-- [原子块 · img]  -->

**EN** Figure 4: Seen accuracy (a,b,c) and unseen accuracy (d) evaluated on the heterogeneous persona dataset across the number of prototypical groups used in the model ⟦SLOT_238⟧. We vary (a) the number of true prototypes ⟦SLOT_239⟧, (b) the number of comparisons per seen user ⟦SLOT_240⟧, (c) the size of latent dimension ⟦SLOT_241⟧, (d) the number of comparisons per unseen user ⟦SLOT_242⟧.

**ZH** 图 4：在异质 persona 数据集上、跨模型所用原型组数 ⟦SLOT_238⟧ 评估的已见准确率 (a,b,c) 与未见准确率 (d)。我们改变 (a) 真实原型数 ⟦SLOT_239⟧、(b) 每已见用户的比较数 ⟦SLOT_240⟧、(c) 潜维度大小 ⟦SLOT_241⟧、(d) 每未见用户的比较数 ⟦SLOT_242⟧。

**EN** 4.2.2 Pick-a-Filter Dataset

**ZH** 4.2.2 Pick-a-Filter 数据集

**EN** We construct a semi-synthetic heterogeneous preference dataset which we call Pick-a-Filter, and show that our ⟦SLOT_243⟧ reward model can significantly surpass the homogeneous reward model when pluralistic preferences are present.

**ZH** 我们构建了一个半合成异质偏好数据集，称之为 Pick-a-Filter，并证明当存在多元偏好时，我们的 ⟦SLOT_243⟧ 奖励模型能显著超越同质奖励模型。

**EN** Dataset. The Pick-a-Pic dataset [6] is a large, open dataset for human feedback in text-to-image generation, designed to align pretrained models with human preferences. It contains around a million samples of text-to-image prompts and real user preferences over generated images from multiple open-source popular diffusion models, with anonymous user IDs. Motivated by a natural human color preference distribution [52], we construct the Pick-a-Filter dataset by adding different color filters to the generated images to explicitly "inject" diverse user preferences into the Pick-a-Pic V1 dataset. Further details are provided in Figure 7 and Appendix B. The magnitude of heterogeneous preference injection is determined by a hyperparameter called mixture ratio. The mixture ratio ⟦SLOT_244⟧ reflects the proportion between the original pairs from the Pick-a-Pic dataset and the color-filtered pairs. The larger the ⟦SLOT_245⟧, the more color-filtered pairs.

**ZH** 数据集。Pick-a-Pic 数据集 [6] 是一个面向文本到图像生成中人类反馈的大型开放数据集，旨在使预训练模型与人类偏好对齐。它包含约一百万条文本到图像提示词样本，以及真实用户对来自多个流行开源扩散模型的生成图像的偏好，并带有匿名用户 ID。受一种自然的人类颜色偏好分布 [52] 启发，我们通过在生成图像上添加不同的颜色滤镜来构建 Pick-a-Filter 数据集，以此向 Pick-a-Pic V1 数据集显式“注入”多样化的用户偏好。更多细节见图 7 与附录 B。异质偏好注入的强度由一个名为混合比例的超参数决定：混合比例 ⟦SLOT_244⟧ 反映 Pick-a-Pic 数据集原始图像对与加滤镜图像对之间的比例，⟦SLOT_245⟧ 越大，加滤镜的图像对越多。

**EN** Experiment Setup. We train model B with logistic loss on the Pick-a-Filter dataset with different mixture ratios. Detailed training setups are deferred to Appendix C.2.

**ZH** 实验设置。我们在 Pick-a-Filter 数据集上以不同的混合比例、用逻辑损失训练模型 B。详细的训练设置见附录 C.2。

**EN** Results. Figure 5 shows that ⟦SLOT_246⟧-B effectively captures diverse preferences across mixture ratios in Pick-a-Filter. We can view these mixture ratios as indicating the extent to which the two user groups prefer their respective color filters. The figure illustrates that ⟦SLOT_247⟧ enables learning beyond a universal preference (⟦SLOT_248⟧) to identify diverse user preference groups. ⟦SLOT_249⟧ significantly outperforms the homogeneous reward model in predicting user preferences – at a mixture ratio of 1, ⟦SLOT_250⟧ achieves 95.2% test accuracy compared to 75.4% from the homogeneous reward model.

**ZH** 结果。图 5 显示 ⟦SLOT_246⟧-B 在 Pick-a-Filter 上有效捕捉了跨混合比例的多样化偏好。我们可以把这些混合比例视为两个用户群各自偏好其对应颜色滤镜程度的指标。图中说明 ⟦SLOT_247⟧ 能够超越通用偏好（⟦SLOT_248⟧）进行学习，识别出多样化的用户偏好群体。⟦SLOT_249⟧ 在预测用户偏好上显著优于同质奖励模型——在混合比例为 1 时，⟦SLOT_250⟧ 达到 95.2% 的测试准确率，而同质奖励模型为 75.4%。

**EN** 4.3 Real Datasets

**ZH** 4.3 真实数据集

**EN** 4.3.1 Summary Dataset

**ZH** 4.3.1 Summary 数据集

**EN** Dataset. Reddit TL;DR summary dataset curated by [5] contains a series of preferences over summaries generated by language models. For each pair of summaries, ⟦SLOT_251⟧ and ⟦SLOT_252⟧, a worker ⟦SLOT_253⟧ determines if ⟦SLOT_254⟧ is preferred or not. Moreover, each pair is also accompanied by the unique identifier of the worker who provides the preference. This would allow us to apply our model to such a dataset.

**ZH** 数据集。由 [5] 整理的 Reddit TL;DR 摘要数据集包含一系列对语言模型生成摘要的偏好。对每对摘要 ⟦SLOT_251⟧ 与 ⟦SLOT_252⟧，由一名工作者 ⟦SLOT_253⟧ 判定 ⟦SLOT_254⟧ 是否更受偏好。此外，每对摘要还附有提供该偏好的工作者的唯一标识符，这使我们能够把模型应用到该数据集上。

**EN** Experiment Setup. We evaluate our model A with hinge loss on a trimmed version of the summary dataset described in [53]. Details regarding how the dataset is constructed and comparisons to other baselines are deferred to Appendix C.3.

**ZH** 实验设置。我们在 [53] 所述摘要数据集的一个精简版本上评估带铰链损失的模型 A。数据集的构建方式以及与其他基线的比较详见附录 C.3。

**EN** Results. Table 3 compares the performance of our method to the one proposed in [53]. We use the weighted average of prototypes learned as the general ideal point for new users to conduct zero-shot learning. We emphasize that even though our model only has 594K parameters and the sentence embeddings we used are generated from all-mpnet-base-v2 sentence transformer [54], which contains around 105M parameters, we still can achieve on par performance, especially in terms of unseen accuracy.

**ZH** 结果。表 3 把我们的方法与 [53] 所提出的方法作了性能对比。我们用所学原型的加权平均作为新用户的通用理想点，以进行零样本学习。我们要强调的是，尽管我们的模型只有 594K 参数，且所用的句子嵌入来自 all-mpnet-base-v2 句子转换器 [54]（约含 105M 参数），我们仍取得了相当的性能，尤其是在未见准确率方面。

<!-- [原子块 · img]  -->

**EN** Figure 5: ⟦SLOT_255⟧ Model B test accuracy on Pick-a-Filter compared to CLIP-H.

**ZH** 图 5：⟦SLOT_255⟧ 模型 B 在 Pick-a-Filter 上的测试准确率，与 CLIP-H 对比。

<!-- [原子块 · table] Model Test Accuracy(%) Pick-a-Pic v1 test CLIP-H14 59.23 PickScore 71.85 model A on CLIP-H 69.29 ± \pm 0.66 model B on CLIP-H 71.13 ± \pm 0.31 -->

**EN** Table 2: ⟦SLOT_256⟧ test accuracy can match SoTA Pickscore [6] on the Pick-a-Pic-v1 test set with a fraction of the compute.

**ZH** 表 2：⟦SLOT_256⟧ 的测试准确率能以极小部分的计算量，在 Pick-a-Pic-v1 测试集上媲美当前最优的 Pickscore [6]。

**EN** Table 3: Results for Summary Dataset: Seen accuracy and unseen accuracy of our model with ⟦SLOT_257⟧ compared to the individual user model proposed in [53]. With only 594K parameters, we achieve on-par performance compared to a method that requires a supervised-finetuned 6B model.

**ZH** 表 3：Summary 数据集上的结果：我们带 ⟦SLOT_257⟧ 的模型的已见准确率与未见准确率，与 [53] 提出的单用户模型对比。仅用 594K 参数，我们就取得了与需要一个监督微调 6B 模型的方法相当的性能。

<!-- [原子块 · table] K = 1 K=1 K = 5 K=5 K = 10 K=10 Li et. al. [ 53 ] Seen accuracy 59.28 ± 0.14 59.28\pm 0.14 59.66 ± 0.09 59.66\pm 0.09 59.51 ± 0.12 59.51\pm 0.12 61.72 Unseen accuracy (zero-shot) 59.20 ± 0.16 59.20\pm -->

**EN** 4.3.2 Pick-a-Pic Dataset

**ZH** 4.3.2 Pick-a-Pic 数据集

**EN** We conducted experiments on the Pick-a-Pic dataset [6] and show two benefits of our proposed ideal point model compared with existing reward models, including the ability to learn diverse user preferences and a competitive reward model with only 2-layer MLP networks. Recent works on the existing reward models usually require fine-tuning foundation models with billions of parameters [1, 6]. Our model can achieve comparable performance without any large model fine-tuning stage, which in turn saves plenty of computing costs.

**ZH** 我们在 Pick-a-Pic 数据集 [6] 上开展实验，展示了我们所提出的理想点模型相比现有奖励模型的两点优势：能够学习多样化的用户偏好，以及仅用 2 层 MLP 网络即可得到有竞争力的奖励模型。现有奖励模型的近期工作通常需要对数十亿参数的基础模型做微调 [1, 6]；我们的模型无需任何大型模型微调阶段即可达到相当的性能，从而节省了大量计算开销。

**EN** Dataset. There are two versions of Pick-a-Pic datasets, v1 and v2, where the Pick-a-Pic v2 dataset extends v1. To ensure fair model evaluation, we divide the Pick-a-Pic v2 test set [6] into “no-leakage" and “leakage" subsets due to overlap (“leakage”) with the v1 train set. Specifically, the Pick-a-Pic v2 test set contains 18391 samples with no preference ties, i.e. one generated image is preferred to the other. Out of these, 10587 samples (⟦SLOT_258⟧) overlap with the training and validation sets of Pick-a-Pic v1, which was used to train Pickscore [6] – we call this the v2 “leakage" subset. The remaining 7804 test samples (⟦SLOT_259⟧) in the v2 dataset do not overlap with the v1 training and validation datasets, ensuring they are distinct for evaluation purposes – we call this the v2 “no-leakage" subset.

**ZH** 数据集。Pick-a-Pic 数据集有 v1 与 v2 两个版本，v2 是对 v1 的扩展。为保证公平的模型评估，我们把 Pick-a-Pic v2 测试集 [6] 划分为“无泄漏”与“泄漏”两个子集，依据是它们与 v1 训练集是否存在重叠（“泄漏”）。具体地，Pick-a-Pic v2 测试集包含 18391 条无偏好并列的样本，即一幅生成图像优于另一幅；其中 10587 条（⟦SLOT_258⟧）与用于训练 Pickscore [6] 的 Pick-a-Pic v1 训练与验证集重叠，我们称之为 v2“泄漏”子集；v2 数据集中其余 7804 条测试样本（⟦SLOT_259⟧）与 v1 训练及验证集不重叠，确保了它们在评估上的独立性，我们称之为 v2“无泄漏”子集。

**EN** Experiment Setup. We trained model B with logistic loss on both v1 and v2 datasets over 10 epochs, using CLIP-H/14 or PickScore [6] latent embeddings as input. We adopt the same hyperparameters used in earlier Pick-a-Filter experiments, avoiding extensive hyperparameter tuning (see Appendix C.2).

**ZH** 实验设置。我们在 v1 与 v2 数据集上以 CLIP-H/14 或 PickScore [6] 的潜嵌入为输入，用逻辑损失训练模型 B，共 10 轮。我们沿用此前 Pick-a-Filter 实验中的超参数，避免大量的超参数调优（见附录 C.2）。

**EN** Results. Table 5 highlights the effectiveness of our proposed ideal point model framework: while training on Pick-a-Pic v1, ⟦SLOT_260⟧ exceeds SoTA reward model performance on no-leakage subset (i.e. fair comparison) by 2%. Additionally, the performance of model B trained on PickScore (trained on v1 train) latent embeddings is inferior to that of model B trained on default CLIP-H/14 embeddings. ⟦SLOT_261⟧ exceeds SoTA Pickscore performance while training a simple two-layer MLP network on a single RTX 4090 GPU, whereas PickScore requires fine-tuning a significant portion of CLIP-H/14 (⟦SLOT_262⟧ parameters) with 8⟦SLOT_263⟧A100 GPUs – this highlights the potential of ⟦SLOT_264⟧ for efficient reward modeling.

**ZH** 结果。表 5 凸显了我们所提出的理想点模型框架的有效性：在 Pick-a-Pic v1 上训练时，⟦SLOT_260⟧ 在无泄漏子集（即公平比较）上超出 SoTA 奖励模型性能 2%。此外，在 PickScore（在 v1 训练集上训练）的潜嵌入上训练的模型 B，其性能不及在默认 CLIP-H/14 嵌入上训练的模型 B。⟦SLOT_261⟧ 在单张 RTX 4090 GPU 上训练一个简单的两层 MLP 网络，即超过了 SoTA Pickscore 的性能，而 PickScore 需要用 8⟦SLOT_263⟧A100 GPU 微调 CLIP-H/14 的相当一部分（⟦SLOT_262⟧ 参数）——这凸显了 ⟦SLOT_264⟧ 在高效奖励建模上的潜力。

**EN** Remark. Since the data collection process for existing datasets involves the usage of strict rubrics [5, 6, 55], labeler performance monitoring [56] and disproportionate amount of data from small fraction of users, these datasets may not be heterogeneous. We note that a strict rubric leads to uniformity as it essentially crowdsources the criteria given under the rubric instead of eliciting preferences of the people. Therefore, even using ⟦SLOT_265⟧ with ⟦SLOT_266⟧, we can surpass existing SoTA performance. These results motivate the need for more nuanced approaches to collect datasets that elicit diverse opinions.

**ZH** 评注。由于现有数据集的采集过程使用了严格的标注细则 [5, 6, 55]、标注者表现监控 [56]，且来自极少数用户的数据占比畸高，这些数据集可能并非异质的。我们指出，严格的标注细则会导致趋同，因为它本质上是在众包该细则下给定的准则，而非引出人们自身的偏好。因此，即便使用 ⟦SLOT_265⟧ 且 ⟦SLOT_266⟧，我们仍能超越现有 SoTA 性能。这些结果说明，需要更细致的方法来采集能够引出多元观点的数据集。

**EN** Table 4: Test Accuracy of ⟦SLOT_267⟧ compared to CLIP-H and PickScore baselines on Pick-a-Pic v2. Entries with asterisk∗ have inflated accuracy due to the V2 test set overlap with the V1 train (See dataset details in Section 4.3.2).

**ZH** 表 4：⟦SLOT_267⟧ 在 Pick-a-Pic v2 上相对 CLIP-H 与 PickScore 基线的测试准确率。带星号∗的条目因 V2 测试集与 V1 训练集重叠而导致准确率虚高（数据集细节见第 4.3.2 节）。

<!-- [原子块 · table] Model Train Dataset Test Accuracy on Pick-a-Pic v2 (%) No-leakage Leakage CLIP-H14 - 62.57 58.59 PickScore pickapic v1 68.04 74.16 ∗ model B on CLIP-H pickapic v1 70.02 ± \pm 0.39 79.32 ± \pm 1.68 ∗ m -->

**EN** 5 Related Works

**ZH** 5 相关工作

**EN** Alignment Status Quo. Popular existing foundation models [1, 9, 11, 15] typically use RLHF [5, 40] to align models after pretraining. Recent foundation models such as Zephyr [57] and the Archangel suite33 3 https://github.com/ContextualAI/HALOs have shifted to directly optimizing on human preferences [25, 58, 59] to avoid the nuances of RL optimization [60]. There has also been significant recent work in collecting large human preference datasets for reward model training in the text-to-image (typically diffusion model [20]) space [6, 55, 56].

**ZH** 对齐现状。流行的现有基础模型 [1, 9, 11, 15] 通常在预训练后用 RLHF [5, 40] 对齐模型。Zephyr [57] 与 Archangel 套件33 3 https://github.com/ContextualAI/HALOs 等近期基础模型已转向直接在人类偏好上优化 [25, 58, 59]，以规避强化学习优化的种种微妙之处 [60]。在文本到图像（通常为扩散模型 [20]）领域，近来也有大量工作致力于采集大规模人类偏好数据集用于奖励模型训练 [6, 55, 56]。

**EN** Reward Modeling. These existing alignment frameworks generally assume that all humans share a single unified preference (e.g. LLM “helpfulness” or “harmlessness” [36]) and ascribe to the Bradley-Terry [2] model of pairwise preferences. Consensus-based methods [28] aims to find agreement among labelers for specific goals like harmlessness [35, 37], helpfulness [36], or engagement [61]. By design, these methods inherently prioritize the universal preference (and biases) induced by the labelers [27, 32, 34]. In reality, humans have diverse, heterogeneous preferences [29, 30, 31] that depend on individual contexts, and may even share a group structure [28]. Rewarded soups [38] make a case to capture diversity through post-hoc weight-space interpolation over a mixture of experts that learn diverse rewards. However, these rewards are learned by pre-defining what aspects are important which is done by the system designer. Separate datasets are collected to elicit human preferences on these axes as to how much people care of them. DPA [62] models rewards as directions instead of scalars, and trains a multi-objective reward model for RLHF. Wu et al. propose fine-grained multi-objective rewards to provide more focused signal for RLHF. Recently, Li et al. propose personalized reward modeling by learning a general user embedding and treating each individual as a perturbation to the embedding. As this preference formulation is still homogeneous, they can only generalize to unseen users using the fixed general user embedding.

**ZH** 奖励建模。这些现有对齐框架通常假设所有人类共享单一统一的偏好（例如 LLM 的“有用性”或“无害性” [36]），并遵循成对偏好的 Bradley-Terry [2] 模型。基于共识的方法 [28] 旨在为无害性 [35, 37]、有用性 [36] 或参与度 [61] 等特定目标在标注者之间达成一致。按设计，这些方法天然优先考虑由标注者引入的通用偏好（及偏见）[27, 32, 34]。现实中，人类拥有多样化、异质的偏好 [29, 30, 31]，这些偏好依赖于个体语境，甚至可能具有群体结构 [28]。Rewarded soups [38] 主张通过对学习多样化奖励的混合专家做事后权重空间插值来捕捉多样性；然而，这些奖励是通过系统设计师预先定义哪些方面重要来学习的，并为此分别采集数据集，以引出人们在这些维度上的在意程度。DPA [62] 把奖励建模为方向而非标量，并训练了一个用于 RLHF 的多目标奖励模型。Wu 等人提出细粒度的多目标奖励，为 RLHF 提供更聚焦的信号。近期 Li 等人提出通过学习一个通用用户嵌入、并把每个个体视为该嵌入上的扰动来实现个性化奖励建模；由于这一偏好形式化仍是同质的，他们只能用固定的通用用户嵌入来泛化到未见用户。

**EN** Recent survey works provide excellent summaries of literature for alignment [64] and reward modeling [65].

**ZH** 近期的综述工作对对齐 [64] 与奖励建模 [65] 的文献作了出色的总结。

**EN** Human Preference Datasets. The preference universality assumption also extends into the data annotation/labeling processing, where labelers are given a rubric to select preferences (e.g. to rank an image pair considering image aesthetics and image-prompt alignment [6]). Due to this rubric, the current largest scale text-to-image generation preference datasets [6, 55, 56] show limited diversity among labelers. In the Pick-a-Pic [6] train set, there are only 701 disagreements among the 12487 image pairs labeled by different users (94.38% agreement), and there are zero disagreements in validation (1261 pairs) and test (1453 pairs) sets. HPS [55] found that labeler agreement over diffusion model generations was higher for models of similar quality or size, though this diversity comes with the caveat of the labelers being provided a rubric to provide their preferences. Imagereward [56] use researcher agreement as a criteria to hire labelers. In the LLM domain, the popular Summarize from Feedback dataset [5] is also collected with rigid rubric, with labeler performance measured via agreement to the preferred answer of the authors. During the data collection period, only labelers with satisfactory agreement were retained, which led to a small number of users, all in agreement with the authors’ rubric, being responsible for a majority of labeled comparisons. Status quo preference datasets used to align foundation models thus suffer from a lack of diversity due to the nature of their data collection.

**ZH** 人类偏好数据集。偏好普适性的假设还延伸到数据标注/打标过程中——标注者会被给予一份标注细则来作出偏好选择（例如就图像美学与图文对齐对图像对排序 [6]）。正是由于这份细则，当前规模最大的文本到图像生成偏好数据集 [6, 55, 56] 在标注者之间表现出有限的多样性。在 Pick-a-Pic [6] 训练集中，不同用户标注的 12487 个图像对之间只有 701 处分歧（一致率 94.38%），而验证集（1261 对）与测试集（1453 对）中分歧为零。HPS [55] 发现，对于质量或规模相近的模型，标注者在扩散模型生成结果上的一致率更高，尽管这种多样性伴随一个前提：标注者是被给予一份细则来作出偏好判断的。Imagereward [56] 以研究者一致度作为雇用标注者的标准。在 LLM 领域，广为使用的 Summarize from Feedback 数据集 [5] 同样以严格的细则采集，标注者的表现通过与作者偏好的答案的一致度来衡量；在数据采集期间，只有一致度令人满意的标注者被保留，这导致少数与作者细则一致的用户承担了大部分已标注的比较。因此，用于对齐基础模型的主流偏好数据集，因其采集方式的性质而缺乏多样性。

**EN** Preference learning. There is rich literature on preference learning and ranking in various domains ranging from psychology, marketing, recommendation systems, quantifying social science surveys to crowdsourced democracy, voting theory and social choice theory. We provide a few relevant works here and direct reader to surveys such as [66]. Ranking based models, e.g., BTL-model [2, 67], stochastic transitivity models [68] focus on finding ranking of ⟦SLOT_268⟧ items or finding top-k items by pairwise comparisons [69, 70, 71, 72, 73, 74, 75]. Ranking ⟦SLOT_269⟧ items in these settings requires ⟦SLOT_270⟧ queries. There is also rich literature that stems from ideal point model proposed by Coombs [4, 45, 46, 47, 48, 49, 50]. Under the ideal point based models, the query complexity for ranking ⟦SLOT_271⟧ items reduces to ⟦SLOT_272⟧, where ⟦SLOT_273⟧ is the dimension of the domain of representations which is usually much smaller than the number of items being ranked [48]. This is due to the fact that once the preference point is learned, it can then be used to predict rankings of new items without needing more comparisons.

**ZH** 偏好学习。在心理学、市场营销、推荐系统、社会科学调查量化、众包式民主、投票理论与社会选择理论等诸多领域，关于偏好学习与排序的文献十分丰富。我们在此列出若干相关工作，并引导读者参阅 [66] 等综述。基于排序的模型（如 BTL 模型 [2, 67]、随机传递性模型 [68]）关注通过成对比较找出 ⟦SLOT_268⟧ 个条目的排序或前 k 个条目 [69, 70, 71, 72, 73, 74, 75]。在这类设置下对 ⟦SLOT_269⟧ 个条目排序需要 ⟦SLOT_270⟧ 次查询。另有一支源自 Coombs 所提理想点模型的丰富文献 [4, 45, 46, 47, 48, 49, 50]。在基于理想点的模型下，对 ⟦SLOT_271⟧ 个条目排序的查询复杂度降至 ⟦SLOT_272⟧，其中 ⟦SLOT_273⟧ 是表示空间的维度，通常远小于被排序的条目数 [48]。这是因为一旦学到偏好点，就可用它预测新条目的排序，而无需更多比较。

**EN** Metric learning has been studied quite extensively and we direct the reader to surveys [39] and books [76]. In particular, metric learning based on triplet querying has also been quite extensively studied [39, 77, 78, 79, 80, 81, 82, 83, 84, 85] which aims to learn the underlying unknown metric under the assumption that the people base their judgement for a triple query with concepts ⟦SLOT_274⟧ on the relative similarities based on the distances between these concepts under the unknown metric.

**ZH** 度量学习已被相当广泛地研究，我们引导读者参阅综述 [39] 与专著 [76]。特别是基于三元组查询的度量学习也有相当广泛的研究 [39, 77, 78, 79, 80, 81, 82, 83, 84, 85]，其目标是：假设人们在面对含概念 ⟦SLOT_274⟧ 的三元组查询时，依据未知度量下这些概念之间距离的相对相似性作出判断，由此学习底层的未知度量。

**EN** Simultaneous metric and preference learning. More recently a few works have considered the problem of unknown metric in preference learning and proposed methods [45, 50, 86] and provided sample complexity analysis [45, 86] for simultaneously learning an unknown Mahalanobis metric and unknown user preference(s). Learning the unknown Mahalanobis metric can be viewed as learning linear layer on top of the embeddings from a foundation model. From our reframing of alignment, these works can be looked as model A with linear function for ⟦SLOT_275⟧ and individual user preferences instead of having any structure over them.

**ZH** 度量与偏好的同步学习。近来有若干工作考虑了偏好学习中度量未知的问题，提出了相应方法 [45, 50, 86]，并就同时学习未知马氏度量与未知用户偏好给出了样本复杂度分析 [45, 86]。学习未知马氏度量可视为在基础模型的嵌入之上学习一个线性层。从我们对对齐的重构来看，这些工作可视为模型 A 中 ⟦SLOT_275⟧ 取线性函数、且采用个体用户偏好而不在其上施加任何结构的特例。

**EN** 6 Conclusions, Broader impacts, Limitations and Future Work

**ZH** 6 结论、更广泛的影响、局限性与未来工作

**EN** We proposed a novel reformulation of the problem of alignment with human preferences (Section 3.1) and proposed a new framework for pluralistic alignment with diverse preferences from the ground up (Sections 3.2 and 3.3) by leveraging shared structures across the population while learning to personalize using a mixture modeling approach. We demonstrate the ⟦SLOT_276⟧ framework is agnostic to modality, showing flexibility adaptivity to heterogeneous preferences for synthetic data (Section 4.1), semi-synthetic and real text data (Sections 4.2.1 and 4.3.1) and semi-synthetic and real image data (Sections 4.2.2 and 4.3.2). Our work aids in building much-needed foundations towards plurality for the alignment of ML/AI models. Our experiments also highlight the limitations of many real human preference datasets that are collected with rubrics that make the dataset homogeneous, thus calling for a more nuanced approach to data collection in the future (Section 4.3.2). While the mixture modeling approach of ⟦SLOT_277⟧ is flexible and interpretable, a limitation of using it is that it will not generalize to users who fall out of the convex hull of the learned prototypes (Section 4.1). A more pragmatic and exciting approach would be a continual learning approach of adding prototypes to adapt to new users over time, which we leave for future work.

**ZH** 我们提出了对人类偏好对齐问题的一种新颖重构（第 3.1 节），并提出了一个从底层就支持多样化偏好的多元对齐新框架（第 3.2 与 3.3 节）——它在利用人群间共享结构的同时，通过混合建模方法学习个性化。我们证明 ⟦SLOT_276⟧ 框架与模态无关，能够灵活适应合成数据（第 4.1 节）、半合成与真实文本数据（第 4.2.1 与 4.3.1 节）以及半合成与真实图像数据（第 4.2.2 与 4.3.2 节）中的异质偏好。我们的工作为 ML/AI 模型对齐走向多元性奠定了急需的基础。我们的实验还揭示了许多真实人类偏好数据集的局限——它们以细则采集，因而使数据集趋于同质，这呼吁未来采用更细致的数据采集方法（第 4.3.2 节）。尽管 ⟦SLOT_277⟧ 的混合建模方法灵活且可解释，使用它的一个局限是：它无法泛化到落在所学原型凸包之外的用户（第 4.1 节）。一个更务实也更令人振奋的思路是采用持续学习方法，随时间推移不断增加原型以适应新用户，我们将其留待未来工作。

**EN** 7 Acknowledgements

**ZH** 7 致谢

**EN** This work was partly supported by NSF grants NCS-FO 2219903 and NSF CAREER Award CCF 2238876.

**ZH** 本工作部分得到 NSF 基金 NCS-FO 2219903 与 NSF CAREER Award CCF 2238876 的资助。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] [1] Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. Training language models to follow instruction -->

<!-- [原子块 · verbatim] [2] Ralph Allan Bradley and Milton E Terry. Rank analysis of incomplete block designs: I. the method of paired comparisons. Biometrika , 39(3/4):324–345, 1952. -->

<!-- [原子块 · verbatim] [3] Esin Durmus, Karina Nguyen, Thomas I. Liao, Nicholas Schiefer, Amanda Askell, Anton Bakhtin, Carol Chen, Zac Hatfield-Dodds, Danny Hernandez, Nicholas Joseph, Liane Lovitt, Sam McCandlish, Orowa S -->

<!-- [原子块 · verbatim] [4] Clyde H Coombs. Psychological scaling without a unit of measurement. Psychological review , 57(3):145, 1950. -->

<!-- [原子块 · verbatim] [5] Nisan Stiennon, Long Ouyang, Jeffrey Wu, Daniel Ziegler, Ryan Lowe, Chelsea Voss, Alec Radford, Dario Amodei, and Paul F Christiano. Learning to summarize with human feedback. Advances in Neural I -->

<!-- [原子块 · verbatim] [6] Yuval Kirstain, Adam Polyak, Uriel Singer, Shahbuland Matiana, Joe Penna, and Omer Levy. Pick-a-pic: An open dataset of user preferences for text-to-image generation. Advances in Neural Informatio -->

<!-- [原子块 · verbatim] [7] Ethan Perez, Sam Ringer, Kamilė Lukošiūtė, Karina Nguyen, Edwin Chen, Scott Heiner, Craig Pettit, Catherine Olsson, Sandipan Kundu, Saurav Kadavath, Andy Jones, Anna Chen, Ben Mann, Brian Israel,  -->

<!-- [原子块 · verbatim] [8] Rishi Bommasani, Drew A Hudson, Ehsan Adeli, Russ Altman, Simran Arora, Sydney von Arx, Michael S Bernstein, Jeannette Bohg, Antoine Bosselut, Emma Brunskill, et al. On the opportunities and risks -->

<!-- [原子块 · verbatim] [9] Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. Gpt-4 technical report. arXiv p -->

<!-- [原子块 · verbatim] [10] Rohan Anil, Andrew M Dai, Orhan Firat, Melvin Johnson, Dmitry Lepikhin, Alexandre Passos, Siamak Shakeri, Emanuel Taropa, Paige Bailey, Zhifeng Chen, et al. Palm 2 technical report. arXiv preprin -->

<!-- [原子块 · verbatim] [11] AI Anthropic. The claude 3 model family: Opus, sonnet, haiku. Claude-3 Model Card , 2024. -->

<!-- [原子块 · verbatim] [12] Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, et al. Training compute- -->

<!-- [原子块 · verbatim] [13] Jack W Rae, Sebastian Borgeaud, Trevor Cai, Katie Millican, Jordan Hoffmann, Francis Song, John Aslanides, Sarah Henderson, Roman Ring, Susannah Young, et al. Scaling language models: Methods, an -->

<!-- [原子块 · verbatim] [14] Machel Reid, Nikolay Savinov, Denis Teplyashin, Dmitry Lepikhin, Timothy Lillicrap, Jean-baptiste Alayrac, Radu Soricut, Angeliki Lazaridou, Orhan Firat, Julian Schrittwieser, et al. Gemini 1.5:  -->

<!-- [原子块 · verbatim] [15] Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al. Llama 2: Open foundation and fin -->

<!-- [原子块 · verbatim] [16] Alexandra Sasha Luccioni, Christopher Akiki, Margaret Mitchell, and Yacine Jernite. Stable bias: Analyzing societal representations in diffusion models. arXiv preprint arXiv:2303.11408 , 2023. -->

<!-- [原子块 · verbatim] [17] Ming Ding, Wendi Zheng, Wenyi Hong, and Jie Tang. Cogview2: Faster and better text-to-image generation via hierarchical transformers. Advances in Neural Information Processing Systems , 35:16890– -->

<!-- [原子块 · verbatim] [18] Minguk Kang, Jun-Yan Zhu, Richard Zhang, Jaesik Park, Eli Shechtman, Sylvain Paris, and Taesung Park. Scaling up gans for text-to-image synthesis. In Proceedings of the IEEE/CVF Conference on Com -->

<!-- [原子块 · verbatim] [19] Aditya Ramesh, Prafulla Dhariwal, Alex Nichol, Casey Chu, and Mark Chen. Hierarchical text-conditional image generation with clip latents. arXiv preprint arXiv:2204.06125 , 1(2):3, 2022. -->

<!-- [原子块 · verbatim] [20] Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, and Björn Ommer. High-resolution image synthesis with latent diffusion models. In Proceedings of the IEEE/CVF conference on comput -->

<!-- [原子块 · verbatim] [21] Chitwan Saharia, William Chan, Saurabh Saxena, Lala Li, Jay Whang, Emily L Denton, Kamyar Ghasemipour, Raphael Gontijo Lopes, Burcu Karagol Ayan, Tim Salimans, et al. Photorealistic text-to-image -->

<!-- [原子块 · verbatim] [22] Axel Sauer, Tero Karras, Samuli Laine, Andreas Geiger, and Timo Aila. Stylegan-t: Unlocking the power of gans for fast large-scale text-to-image synthesis. arXiv preprint arXiv:2301.09515 , 2023. -->

<!-- [原子块 · verbatim] [23] Jiahui Yu, Yuanzhong Xu, Jing Yu Koh, Thang Luong, Gunjan Baid, Zirui Wang, Vijay Vasudevan, Alexander Ku, Yinfei Yang, Burcu Karagol Ayan, et al. Scaling autoregressive models for content-rich t -->

<!-- [原子块 · verbatim] [24] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. arXiv preprint arXiv:1707.06347 , 2017. -->

<!-- [原子块 · verbatim] [25] Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and Chelsea Finn. Direct preference optimization: Your language model is secretly a reward model. Advances in  -->

<!-- [原子块 · verbatim] [26] Ximing Lu, Faeze Brahman, Peter West, Jaehun Jung, Khyathi Chandu, Abhilasha Ravichander, Prithviraj Ammanabrolu, Liwei Jiang, Sahana Ramnath, Nouha Dziri, et al. Inference-time policy adapters ( -->

<!-- [原子块 · verbatim] [27] Shibani Santurkar, Esin Durmus, Faisal Ladhak, Cinoo Lee, Percy Liang, and Tatsunori Hashimoto. Whose opinions do language models reflect? In Andreas Krause, Emma Brunskill, Kyunghyun Cho, Barbar -->

<!-- [原子块 · verbatim] [28] Michiel Bakker, Martin Chadwick, Hannah Sheahan, Michael Tessler, Lucy Campbell-Gillingham, Jan Balaguer, Nat McAleese, Amelia Glaese, John Aslanides, Matt Botvinick, et al. Fine-tuning language  -->

<!-- [原子块 · verbatim] [29] Marcos Nadal and Anjan Chatterjee. Neuroaesthetics and art’s diversity and universality. Wiley Interdisciplinary Reviews: Cognitive Science , 10(3):e1487, 2019. -->

<!-- [原子块 · verbatim] [30] Aaron Wildavsky. Choosing preferences by constructing institutions: A cultural theory of preference formation. American political science review , 81(1):3–21, 1987. -->

<!-- [原子块 · verbatim] [31] Taylor Sorensen, Jared Moore, Jillian Fisher, Mitchell Gordon, Niloofar Mireshghallah, Christopher Michael Rytting, Andre Ye, Liwei Jiang, Ximing Lu, Nouha Dziri, et al. A roadmap to pluralistic  -->

<!-- [原子块 · verbatim] [32] Myra Cheng, Esin Durmus, and Dan Jurafsky. Marked personas: Using natural language prompts to measure stereotypes in language models. arXiv preprint arXiv:2305.18189 , 2023. -->

<!-- [原子块 · verbatim] [33] Hyeong Kyu Choi and Yixuan Li. Beyond helpfulness and harmlessness: Eliciting diverse behaviors from large language models with persona in-context learning. arXiv preprint arXiv:2405.02501 , 2024 -->

<!-- [原子块 · verbatim] [34] Grgur Kovač, Masataka Sawayama, Rémy Portelas, Cédric Colas, Peter Ford Dominey, and Pierre-Yves Oudeyer. Large language models as superpositions of cultural perspectives. arXiv preprint arXiv:23 -->

<!-- [原子块 · verbatim] [35] Yuntao Bai, Saurav Kadavath, Sandipan Kundu, Amanda Askell, Jackson Kernion, Andy Jones, Anna Chen, Anna Goldie, Azalia Mirhoseini, Cameron McKinnon, et al. Constitutional ai: Harmlessness from a -->

<!-- [原子块 · verbatim] [36] Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort, Deep Ganguli, Tom Henighan, et al. Training a helpful and harmless assistant with reinf -->

<!-- [原子块 · verbatim] [37] Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben Mann, Ethan Perez, Nicholas Schiefer, Kamal Ndousse, et al. Red teaming language models to reduce harm -->

<!-- [原子块 · verbatim] [38] Alexandre Rame, Guillaume Couairon, Corentin Dancette, Jean-Baptiste Gaya, Mustafa Shukor, Laure Soulier, and Matthieu Cord. Rewarded soups: towards pareto-optimal alignment by interpolating weig -->

<!-- [原子块 · verbatim] [39] Brian Kulis. Metric learning: A survey. Foundations and Trends® in Machine Learning , 5(4):287–364, 2013. -->

<!-- [原子块 · verbatim] [40] Paul F Christiano, Jan Leike, Tom Brown, Miljan Martic, Shane Legg, and Dario Amodei. Deep reinforcement learning from human preferences. Advances in neural information processing systems , 30, 2 -->

<!-- [原子块 · verbatim] [41] Jan Leike, David Krueger, Tom Everitt, Miljan Martic, Vishal Maini, and Shane Legg. Scalable agent alignment via reward modeling: a research direction. arXiv preprint arXiv:1811.07871 , 2018. -->

<!-- [原子块 · verbatim] [42] Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. Self-consistency improves chain of thought reasoning in language models, 2023. -->

<!-- [原子块 · verbatim] [43] Hanze Dong, Wei Xiong, Deepanshu Goyal, Yihan Zhang, Winnie Chow, Rui Pan, Shizhe Diao, Jipeng Zhang, Kashun Shum, and Tong Zhang. Raft: Reward ranked finetuning for generative foundation model a -->

<!-- [原子块 · verbatim] [44] Zheng Yuan, Hongyi Yuan, Chuanqi Tan, Wei Wang, Songfang Huang, and Fei Huang. Rrhf: Rank responses to align language models with human feedback without tears. arXiv preprint arXiv:2304.05302 , 2 -->

<!-- [原子块 · verbatim] [45] Gregory Canal, Blake Mason, Ramya Korlakai Vinayak, and Robert Nowak. One for all: Simultaneous metric and preference learning over multiple users. arXiv preprint arXiv:2207.03609 , 2022. -->

<!-- [原子块 · verbatim] [46] Cody Ding. Evaluating change in behavioral preferences: Multidimensional scaling single-ideal point model. Measurement and Evaluation in Counseling and Development , 49(1):77–88, 2016. -->

<!-- [原子块 · verbatim] [47] Joel Huber. Ideal point models of preference. ACR North American Advances , 1976. -->

<!-- [原子块 · verbatim] [48] Kevin G Jamieson and Robert Nowak. Active ranking using pairwise comparisons. Advances in neural information processing systems , 24, 2011. -->

<!-- [原子块 · verbatim] [49] Adish Singla, Sebastian Tschiatschek, and Andreas Krause. Actively learning hemimetrics with applications to eliciting user preferences. In International Conference on Machine Learning , pages 41 -->

<!-- [原子块 · verbatim] [50] Austin Xu and Mark Davenport. Simultaneous preference and metric learning from paired comparisons. Advances in Neural Information Processing Systems , 33:454–465, 2020. -->

<!-- [原子块 · verbatim] [51] J. A. Nelder and R. W. M. Wedderburn. Generalized linear models. Journal of the Royal Statistical Society. Series A (General) , 135(3):370–384, 1972. URL http://www.jstor.org/stable/2344614 . -->

<!-- [原子块 · verbatim] [52] Stephen E Palmer and Karen B Schloss. Human preference for individual colors. In Human Vision and Electronic Imaging XV , volume 7527, pages 353–364. SPIE, 2010. -->

<!-- [原子块 · verbatim] [53] Xinyu Li, Zachary C Lipton, and Liu Leqi. Personalized language modeling from personalized human feedback. arXiv preprint arXiv:2402.05133 , 2024. -->

<!-- [原子块 · verbatim] [54] Nils Reimers and Iryna Gurevych. Sentence-bert: Sentence embeddings using siamese bert-networks. In Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing . Associ -->

<!-- [原子块 · verbatim] [55] Xiaoshi Wu, Yiming Hao, Keqiang Sun, Yixiong Chen, Feng Zhu, Rui Zhao, and Hongsheng Li. Human preference score v2: A solid benchmark for evaluating human preferences of text-to-image synthesis.  -->

<!-- [原子块 · verbatim] [56] Jiazheng Xu, Xiao Liu, Yuchen Wu, Yuxuan Tong, Qinkai Li, Ming Ding, Jie Tang, and Yuxiao Dong. Imagereward: Learning and evaluating human preferences for text-to-image generation. Advances in Ne -->

<!-- [原子块 · verbatim] [57] Lewis Tunstall, Edward Beeching, Nathan Lambert, Nazneen Rajani, Kashif Rasul, Younes Belkada, Shengyi Huang, Leandro von Werra, Clémentine Fourrier, Nathan Habib, et al. Zephyr: Direct distillat -->

<!-- [原子块 · verbatim] [58] Mohammad Gheshlaghi Azar, Zhaohan Daniel Guo, Bilal Piot, Remi Munos, Mark Rowland, Michal Valko, and Daniele Calandriello. A general theoretical paradigm to understand learning from human prefer -->

<!-- [原子块 · verbatim] [59] Kawin Ethayarajh, Winnie Xu, Niklas Muennighoff, Dan Jurafsky, and Douwe Kiela. Kto: Model alignment as prospect theoretic optimization. arXiv preprint arXiv:2402.01306 , 2024. -->

<!-- [原子块 · verbatim] [60] Gabriel Dulac-Arnold, Nir Levine, Daniel J Mankowitz, Jerry Li, Cosmin Paduraru, Sven Gowal, and Todd Hester. Challenges of real-world reinforcement learning: definitions, benchmarks and analysis -->

<!-- [原子块 · verbatim] [61] Robert Irvine, Douglas Boubert, Vyas Raina, Adian Liusie, Ziyi Zhu, Vineet Mudupalli, Aliaksei Korshuk, Zongyi Liu, Fritz Cremer, Valentin Assassi, et al. Rewarding chatbots for real-world engage -->

<!-- [原子块 · verbatim] [62] Haoxiang Wang, Yong Lin, Wei Xiong, Rui Yang, Shizhe Diao, Shuang Qiu, Han Zhao, and Tong Zhang. Arithmetic control of llms for diverse user preferences: Directional preference alignment with mul -->

<!-- [原子块 · verbatim] [63] Zeqiu Wu, Yushi Hu, Weijia Shi, Nouha Dziri, Alane Suhr, Prithviraj Ammanabrolu, Noah A Smith, Mari Ostendorf, and Hannaneh Hajishirzi. Fine-grained human feedback gives better rewards for langua -->

<!-- [原子块 · verbatim] [64] Jiaming Ji, Tianyi Qiu, Boyuan Chen, Borong Zhang, Hantao Lou, Kaile Wang, Yawen Duan, Zhonghao He, Jiayi Zhou, Zhaowei Zhang, et al. Ai alignment: A comprehensive survey. arXiv preprint arXiv:23 -->

<!-- [原子块 · verbatim] [65] Binghai Wang, Rui Zheng, Lu Chen, Yan Liu, Shihan Dou, Caishuang Huang, Wei Shen, Senjie Jin, Enyu Zhou, Chenyu Shi, et al. Secrets of rlhf in large language models part ii: Reward modeling. arXi -->

<!-- [原子块 · verbatim] [66] Johannes Fürnkranz and Eyke Hüllermeier. Preference learning and ranking by pairwise comparison. In Preference learning , pages 65–82. Springer, 2010. -->

<!-- [原子块 · verbatim] [67] R Duncan Luce. Individual choice behavior: A theoretical analysis . New York: Wiley, 1959. -->

<!-- [原子块 · verbatim] [68] Nihar Shah, Sivaraman Balakrishnan, Aditya Guntuboyina, and Martin Wainwright. Stochastically transitive models for pairwise comparisons: Statistical and computational issues. In International Co -->

<!-- [原子块 · verbatim] [69] David R Hunter. Mm algorithms for generalized bradley-terry models. The annals of statistics , 32(1):384–406, 2004. -->

<!-- [原子块 · verbatim] [70] Claire Kenyon-Mathieu and Warren Schudy. How to rank with few errors. In Proceedings of the thirty-ninth annual ACM symposium on Theory of computing , pages 95–103, 2007. -->

<!-- [原子块 · verbatim] [71] Mark Braverman and Elchanan Mossel. Noisy sorting without resampling. arXiv preprint arXiv:0707.1051 , 2007. -->

<!-- [原子块 · verbatim] [72] Sahand Negahban, Sewoong Oh, and Devavrat Shah. Iterative ranking from pair-wise comparisons. Advances in neural information processing systems , 25, 2012. -->

<!-- [原子块 · verbatim] [73] Brian Eriksson. Learning to top-k search using pairwise comparisons. In Artificial Intelligence and Statistics , pages 265–273. PMLR, 2013. -->

<!-- [原子块 · verbatim] [74] Arun Rajkumar and Shivani Agarwal. A statistical convergence perspective of algorithms for rank aggregation from pairwise data. In International conference on machine learning , pages 118–126. PM -->

<!-- [原子块 · verbatim] [75] Nihar B Shah and Martin J Wainwright. Simple, robust and optimal ranking from pairwise comparisons. The Journal of Machine Learning Research , 18(1):7246–7283, 2017. -->

<!-- [原子块 · verbatim] [76] Aurélien Bellet, Amaury Habrard, and Marc Sebban. Metric learning . Springer Nature, 2022. -->

<!-- [原子块 · verbatim] [77] Roger N Shepard. The analysis of proximities: multidimensional scaling with an unknown distance function. i. Psychometrika , 27(2):125–140, 1962a. -->

<!-- [原子块 · verbatim] [78] Roger N Shepard. The analysis of proximities: Multidimensional scaling with an unknown distance function. ii. Psychometrika , 27(3):219–246, 1962b. -->

<!-- [原子块 · verbatim] [79] Roger N Shepard. Metric structures in ordinal data. Journal of Mathematical Psychology , 3(2):287–315, 1966. -->

<!-- [原子块 · verbatim] [80] Matthew Schultz and Thorsten Joachims. Learning a distance metric from relative comparisons. Advances in neural information processing systems , 16, 2003. -->

<!-- [原子块 · verbatim] [81] Omer Tamuz, Ce Liu, Serge Belongie, Ohad Shamir, and Adam Tauman Kalai. Adaptively learning the crowd kernel. arXiv preprint arXiv:1105.1033 , 2011. -->

<!-- [原子块 · verbatim] [82] Matthäus Kleindessner and Ulrike Luxburg. Uniqueness of ordinal embedding. In Conference on Learning Theory , pages 40–67. PMLR, 2014. -->

<!-- [原子块 · verbatim] [83] Aurélien Bellet, Amaury Habrard, and Marc Sebban. Metric learning. Synthesis lectures on artificial intelligence and machine learning , 9(1):1–151, 2015. -->

<!-- [原子块 · verbatim] [84] Aurélien Bellet and Amaury Habrard. Robustness and generalization for metric learning. Neurocomputing , 151:259–267, 2015. -->

<!-- [原子块 · verbatim] [85] Blake Mason, Lalit Jain, and Robert Nowak. Learning low-dimensional metrics. Advances in neural information processing systems , 30, 2017. -->

<!-- [原子块 · verbatim] [86] Zhi Wang, Geelon So, and Ramya Korlakai Vinayak. Metric learning from limited pairwise preference comparisons. In UAI , 2024c. -->

**EN** Appendix A Model Design

**ZH** 附录 A 模型设计

**EN** We illustrate the modeling mechanism of ⟦SLOT_278⟧ (Section 3.2) in slightly more detail in Figure 6.

**ZH** 我们在图 6 中略微更详细地展示了 ⟦SLOT_278⟧ 的建模机制（第 3.2 节）。

<!-- [原子块 · img]  -->

**EN** Figure 6: Illustration of ⟦SLOT_279⟧ framework for learning from diverse preferences (Section 3). For any user ⟦SLOT_280⟧, the probability of preferring ⟦SLOT_281⟧ to ⟦SLOT_282⟧ for the context ⟦SLOT_283⟧ is computed by a reward model ⟦SLOT_284⟧ which uses a mixture modeling approach to assign a scalar reward to a sample (e.g. ⟦SLOT_285⟧ or ⟦SLOT_286⟧) given context (⟦SLOT_287⟧). In ⟦SLOT_288⟧-A, each user ⟦SLOT_289⟧’s preference ⟦SLOT_290⟧ is modeled as a convex combination of ⟦SLOT_291⟧ prototypical preferences, i.e. ⟦SLOT_292⟧. In ⟦SLOT_293⟧-B, each user ⟦SLOT_294⟧’s preference ⟦SLOT_295⟧ is modeled as a convex combination of ⟦SLOT_296⟧ prototypical functions ⟦SLOT_297⟧, i.e. ⟦SLOT_298⟧. Reward function formulated using ⟦SLOT_299⟧ framework can be used flexibly, e.g., with fixed preference points (Model A), with preference points that are functions of the context/prompt ⟦SLOT_300⟧ (Model B).

**ZH** 图 6：⟦SLOT_279⟧ 框架从多样化偏好中学习的示意图（第 3 节）。对任意用户 ⟦SLOT_280⟧，在上下文 ⟦SLOT_283⟧ 下偏好 ⟦SLOT_281⟧ 胜过 ⟦SLOT_282⟧ 的概率由奖励模型 ⟦SLOT_284⟧ 计算；该模型采用混合建模方法，在给定上下文（⟦SLOT_287⟧）时为样本（如 ⟦SLOT_285⟧ 或 ⟦SLOT_286⟧）赋予一个标量奖励。在 ⟦SLOT_288⟧-A 中，每个用户 ⟦SLOT_289⟧ 的偏好 ⟦SLOT_290⟧ 被建模为 ⟦SLOT_291⟧ 个原型化偏好的凸组合，即 ⟦SLOT_292⟧。在 ⟦SLOT_293⟧-B 中，每个用户 ⟦SLOT_294⟧ 的偏好 ⟦SLOT_295⟧ 被建模为 ⟦SLOT_296⟧ 个原型化函数 ⟦SLOT_297⟧ 的凸组合，即 ⟦SLOT_298⟧。用 ⟦SLOT_299⟧ 框架构建的奖励函数可灵活使用，例如采用固定的偏好点（模型 A），或采用作为上下文/提示词 ⟦SLOT_300⟧ 函数的偏好点（模型 B）。

**EN** Appendix B Dataset Design

**ZH** 附录 B 数据集设计

**EN** Pick-a-Filter

**ZH** Pick-a-Filter

**EN** : due to the high level of “agreement” among labelers over image preferences on Pick-a-Pic V1 [6], we construct a semi-synthetic dataset by applying filters to a subset of Pick-a-Pic V1, which we call the Pick-a-Filter dataset. To construct the dataset, we consider only samples that have no ties, i.e. the labeler decides that one image is decisively preferable to the other, given the text prompt. As Pick-a-Pic provides unique and anonymous user IDs for all preference pairs, we consider a subset of users who provide samples in both the train and test sets (468 / 4223 users). We further only consider users who provide more than 50 labels (234 / 468 users) and sort the users by number of samples provided. We split these users into equal groups of 117 each, and we assume without loss of generality that the first group of users (G1) prefers “cold” tones (blue filter) and the second group (G2) prefers “warm” tones (red filter). Lastly, we arbitrarily consider the first 50 users (who provide the most number of samples) as “seen" users, i.e. users that provide samples in both the train and test sets of Pick-a-Filter. We add this seen vs. unseen distinction to evaluate how well ⟦SLOT_301⟧ can adapt to unseen (i.e. new) users after training. Currently, our experiments on Pick-a-Filter (Section 4.2.2) train on V1-train-seen (116031 samples) and evaluate on V1-test-seen (3693 samples). We show the number of samples in each of these splits in Table 5. After constructing splits, we apply the following filtering logic:

**ZH** ：由于在 Pick-a-Pic V1 [6] 上标注者对图像偏好的“一致度”很高，我们通过对 Pick-a-Pic V1 的一个子集施加滤镜构建了一个半合成数据集，称之为 Pick-a-Filter 数据集。构建时，我们只考虑无并列的样本，即标注者判定在给定文本提示词下一幅图像明确优于另一幅。由于 Pick-a-Pic 为所有偏好对提供了唯一且匿名的用户 ID，我们只考虑在训练集与测试集中都提供样本的用户子集（468 / 4223 名用户）；进一步只保留提供标签超过 50 条的用户（234 / 468 名），并按提供样本数对用户排序。我们把这些用户均分为每组 117 人的两组，并不失一般性地假设第一组用户（G1）偏好“冷”色调（蓝色滤镜），第二组（G2）偏好“暖”色调（红色滤镜）。最后，我们任意地把提供样本最多的前 50 名用户视为“已见”用户，即同时在 Pick-a-Filter 训练集与测试集中提供样本的用户。我们加入已见与未见的区分，是为了评估 ⟦SLOT_301⟧ 在训练后适应未见（即新）用户的能力。目前，我们在 Pick-a-Filter 上的实验（第 4.2.2 节）在 V1-train-seen（116031 个样本）上训练，在 V1-test-seen（3693 个样本）上评估。我们在表 5 中给出各划分的样本数。划分构建完成后，我们施加如下滤镜逻辑：

**EN** 1. Apply “winning” and “losing” filters to appropriate images depending on label. For G1 the winning filter is blue, and for G2 the winning filter is red.

**ZH** 1. 依据标签对相应图像施加“胜出”与“落败”滤镜。对 G1，胜出滤镜为蓝色；对 G2，胜出滤镜为红色。

**EN** 2. Randomly shortlist ⟦SLOT_302⟧ of samples to add filters. The remaining ⟦SLOT_303⟧ of samples will remain unaltered (default images from Pick-a-Pic v1).

**ZH** 2. 随机抽取 ⟦SLOT_302⟧ 的样本添加滤镜，其余 ⟦SLOT_303⟧ 的样本保持原样（Pick-a-Pic v1 的默认图像）。

**EN** 3. Randomly select ⟦SLOT_304⟧ of above-shortlisted samples to apply a filter to only the winning image, and the remaining ⟦SLOT_305⟧ to apply a filter to only losing image

**ZH** 3. 在上述抽出的样本中，随机选取 ⟦SLOT_304⟧ 只给胜出图像施加滤镜，其余 ⟦SLOT_305⟧ 只给落败图像施加滤镜。

**EN** We add these sources of randomness to make learning preferences on Pick-a-Filter less prone to hacking (e.g. the model could trivially learn to predict an image with a filter as the preferred image).

**ZH** 我们加入这些随机性，是为了让在 Pick-a-Filter 上学习偏好更不易被钻空子（例如模型可能轻易学会把带滤镜的图像预测为受偏好的图像）。

<!-- [原子块 · img]  -->

**EN** Figure 7: The construction diagram for the semi-synthetic Pick-a-Pic dataset. It involves randomly selecting approximately 100,000 samples from the Pick-a-Pic dataset and dividing the user IDs into two disjoint groups. We assume one group prefers images with “cold” (blue) filters and the other with “warm” (red) filters. To incorporate diverse color filter preferences, we randomly select ⟦SLOT_306⟧ of samples per user on which to apply filters.

**ZH** 图 7：半合成 Pick-a-Pic 数据集的构建示意图。它从 Pick-a-Pic 数据集中随机选取约 100,000 个样本，并把用户 ID 划分为两个不相交的组。我们假设一组偏好带“冷”（蓝）滤镜的图像，另一组偏好带“暖”（红）滤镜的图像。为纳入多样化的颜色滤镜偏好，我们为每个用户随机选取 ⟦SLOT_306⟧ 的样本施加滤镜。

**EN** Table 5: Number of samples in each split of the newly constructed Pick-a-Filter dataset.

**ZH** 表 5：新构建的 Pick-a-Filter 数据集各划分中的样本数。

<!-- [原子块 · table] Category Train Val Test Group 1 Seen 58831 628 1597 Unseen 9527 79 1886 Total 68358 707 3483 Group 2 Seen 57200 404 2096 Unseen 9402 52 1812 Total 66602 456 3908 -->

**EN** Appendix C Experiment Details

**ZH** 附录 C 实验细节

**EN** C.1 Heterogeneous Synthetic Dataset

**ZH** C.1 异质合成数据集

**EN** Experiment Setup. We introduce the dataset simulation procedure in the section 4.1. We use the following hyper-parameters to generate the synthetic dataset ⟦SLOT_307⟧. We generate another 50 comparison pairs per user as the held-out dataset. (Notice, we didn’t simulate the prompt-guided item generation ⟦SLOT_308⟧ procedure. Instead, we directly draw the item ⟦SLOT_309⟧ from a normal distribution for simplicity.) In the experimental setup, we apply a toy version of the modeling design A, the distance between the synthetic item and the user ideal point is measured by ⟦SLOT_310⟧. We use a projection matrix (i.e. one-layer MLP network without bias term and activation function) as the model architecture. We randomly initialize the learnable parameters of prototypical user groups and user weights. We use Adam as the optimizer. The learning rate of the projector ⟦SLOT_311⟧ is ⟦SLOT_312⟧. The learning rate of the learnable parameters of prototypical user groups and user weights is ⟦SLOT_313⟧. The weight decay of the projection matrix ⟦SLOT_314⟧ is ⟦SLOT_315⟧. To guarantee convergence, we run a total of 1000 epochs for each run. We run multiple trials to explore the influence of each factor: 1) varying the number of samples of seen users ⟦SLOT_316⟧, ⟦SLOT_317⟧, ⟦SLOT_318⟧, ⟦SLOT_319⟧, 2) varying the number of samples of new users ⟦SLOT_320⟧, ⟦SLOT_321⟧,⟦SLOT_322⟧, ⟦SLOT_323⟧, 3) varying the number of groups ⟦SLOT_324⟧, ⟦SLOT_325⟧, ⟦SLOT_326⟧, ⟦SLOT_327⟧.

**ZH** 实验设置。我们在第 4.1 节介绍了数据集的模拟流程，并使用如下超参数生成合成数据集 ⟦SLOT_307⟧。我们为每个用户另外生成 50 个比较对作为留出数据集。（注意，我们并未模拟提示词引导的条目生成 ⟦SLOT_308⟧ 流程，而是为简便起见直接从正态分布中抽取条目 ⟦SLOT_309⟧。）在实验设置中，我们采用建模设计 A 的简化版本：合成条目与用户理想点之间的距离由 ⟦SLOT_310⟧ 度量。我们用一个投影矩阵（即无偏置项与激活函数的单层 MLP 网络）作为模型架构，随机初始化原型用户组与用户权重的可学习参数，并用 Adam 作为优化器。投影器 ⟦SLOT_311⟧ 的学习率为 ⟦SLOT_312⟧，原型用户组与用户权重的可学习参数的学习率为 ⟦SLOT_313⟧，投影矩阵 ⟦SLOT_314⟧ 的权重衰减为 ⟦SLOT_315⟧。为保证收敛，每次运行共跑 1000 轮。我们进行了多组试验以探索各因素的影响：1) 改变已见用户的样本数 ⟦SLOT_316⟧、⟦SLOT_317⟧、⟦SLOT_318⟧、⟦SLOT_319⟧；2) 改变新用户的样本数 ⟦SLOT_320⟧、⟦SLOT_321⟧、⟦SLOT_322⟧、⟦SLOT_323⟧；3) 改变组数 ⟦SLOT_324⟧、⟦SLOT_325⟧、⟦SLOT_326⟧、⟦SLOT_327⟧。

<!-- [原子块 · img]  -->

**EN** Figure 8: Partition setting # prototypes in model = 1

**ZH** 图 8：划分设置，模型中原型数 = 1

<!-- [原子块 · img]  -->

**EN** Figure 9: Partition setting # prototypes in model = 2

**ZH** 图 9：划分设置，模型中原型数 = 2

<!-- [原子块 · img]  -->

**EN** Figure 10: Partition setting # prototypes in model = 3

**ZH** 图 10：划分设置，模型中原型数 = 3

<!-- [原子块 · img]  -->

**EN** Figure 11: Mixture setting # prototypes in model = 1

**ZH** 图 11：混合设置，模型中原型数 = 1

<!-- [原子块 · img]  -->

**EN** Figure 12: Mixture setting # prototypes in model = 2

**ZH** 图 12：混合设置，模型中原型数 = 2

<!-- [原子块 · img]  -->

**EN** Figure 13: Mixture setting # prototypes in model = 3

**ZH** 图 13：混合设置，模型中原型数 = 3

<!-- [原子块 · img]  -->

**EN** (a) Test accuracy: 72.2%

**ZH** (a) 测试准确率：72.2%

<!-- [原子块 · img]  -->

**EN** (b) Test accuracy: 83.96%

**ZH** (b) 测试准确率：83.96%

<!-- [原子块 · img]  -->

**EN** (c) Test accuracy: 91.26%

**ZH** (c) 测试准确率：91.26%

**EN** Figure 14: Normally distributed items with ⟦SLOT_328⟧. This figure plots all items, the predicted user ideal points, and the true user ideal points in the feature space. Recall that in our modeling design, the distance between the user ideal point and the item reflects the user’s preference; hence, the closer the predicted user ideal point is to the true ideal points, the higher the performance. As shown in the figures above, when we choose the hyperparameter ⟦SLOT_329⟧ (the correct number of groups), our model can accurately capture the group structure and predict each user’s ideal points.

**ZH** 图 14：服从正态分布、⟦SLOT_328⟧ 的条目。该图在特征空间中绘出全部条目、预测的用户理想点与真实的用户理想点。回顾一下，在我们的建模设计中，用户理想点与条目之间的距离反映用户的偏好；因此，预测的用户理想点越接近真实理想点，性能越高。如上图所示，当我们选取超参数 ⟦SLOT_329⟧（正确的组数）时，我们的模型能准确捕捉群体结构并预测每个用户的理想点。

**EN** C.2 Pick-a-Filter Dataset

**ZH** C.2 Pick-a-Filter 数据集

**EN** Experiment Setup. We choose two-layer MLP networks with ReLU activation and residual connection as the prompt mapping function ⟦SLOT_330⟧ and the output mapping function ⟦SLOT_331⟧. To avoid the overfitting issue, we set the dropout rate as ⟦SLOT_332⟧ and weight decay as ⟦SLOT_333⟧. We use Adam optimizer with a ⟦SLOT_334⟧ learning rate. When we measure the model’s performance, we load the best checkpoint evaluated on the validation set.

**ZH** 实验设置。我们选用带 ReLU 激活与残差连接的两层 MLP 网络作为提示词映射函数 ⟦SLOT_330⟧ 与输出映射函数 ⟦SLOT_331⟧。为避免过拟合，我们把 dropout 率设为 ⟦SLOT_332⟧，权重衰减设为 ⟦SLOT_333⟧。我们使用 Adam 优化器，学习率为 ⟦SLOT_334⟧。在衡量模型性能时，我们加载在验证集上评估得到的最佳检查点。

**EN** Results. To check whether our model trained on Pick-a-Filter dataset is capturing the users’ preference features or is just remembering colors, we verify the test accuracy separately on the color-filtered pairs and original pairs in the mixture-ratio dataset. Figure 15 shows that compared to the CLIP-H14 ⟦SLOT_335⟧ test accuracy, our model’s performance on the original no-filter pairs is still above the baseline, which verifies that our model utilizes both the users’ original preference and the "injected" heterogeneous color preference.

**ZH** 结果。为检验我们在 Pick-a-Filter 数据集上训练的模型究竟是捕捉了用户的偏好特征，还是仅仅记住了颜色，我们在混合比例数据集中分别对加滤镜图像对与原始图像对上的测试准确率作了验证。图 15 显示，相比 CLIP-H14 的 ⟦SLOT_335⟧ 测试准确率，我们的模型在原始无滤镜图像对上的性能仍高于基线，这验证了我们的模型同时利用了用户的原始偏好与“注入”的异质颜色偏好。

<!-- [原子块 · img]  -->

**EN** Figure 15: Test accuracy on color-filtered or original pairs in Pick-a-Filter dataset

**ZH** 图 15：Pick-a-Filter 数据集中加滤镜图像对与原始图像对上的测试准确率。

**EN** C.3 Summary Dataset

**ZH** C.3 Summary 数据集

**EN** Dataset.

**ZH** 数据集。

**EN** Reddit TL;DR summary dataset curated by [5] contains a series of preferences over summaries generated by language models. High-quality workers are hired by the authors to annotate their preferences over the summaries. Workers hired followed a rubric provided by the authors, who periodically fired those workers who did not meet their performance criteria.

**ZH** 由 [5] 整理的 Reddit TL;DR 摘要数据集包含一系列对语言模型生成摘要的偏好。作者雇用了高质量的工作者对摘要标注其偏好，受雇的工作者遵循作者提供的一份标注细则，作者会定期解雇未达成绩效标准的工作者。

**EN** For each pair of summaries ⟦SLOT_336⟧ and ⟦SLOT_337⟧, a worker ⟦SLOT_338⟧ determines if ⟦SLOT_339⟧ is preferred or not. Moreover, each pair is also accompanied by the unique identifier of the worker who provides the preference. This would allow us to apply our model to such a dataset.

**ZH** 对每对摘要 ⟦SLOT_336⟧ 与 ⟦SLOT_337⟧，由一名工作者 ⟦SLOT_338⟧ 判定 ⟦SLOT_339⟧ 是否更受偏好。此外，每对摘要还附有提供该偏好的工作者的唯一标识符，这使我们能够把模型应用到该数据集上。

**EN** Experiment Setup and Results: Comparing to [5]

**ZH** 实验设置与结果：与 [5] 对比

**EN** We trained our model A on the modified summary dataset with ⟦SLOT_340⟧. This is because we want to evaluate the performance of generalization on the unseen users. We split the given testing set into a seen testing set and an unseen dataset, where the seen testing set contains users in the training set, and the unseen dataset contains only users that are not in the training set. The seen testing set is used to validate the performance of seen user, unseen comparison generalization. We are going to conduct a train, test split on the unseen dataset to evaluate the performance of unseen user, unseen comparison generalization.

**ZH** 我们在修改后的摘要数据集上以 ⟦SLOT_340⟧ 训练模型 A，这是因为我们希望评估对未见用户的泛化性能。我们把给定的测试集划分为已见测试集与未见数据集：已见测试集包含训练集中的用户，未见数据集只包含不在训练集中的用户。已见测试集用于验证“已见用户、未见比较”的泛化性能；我们还要在未见数据集上做训练、测试划分，以评估“未见用户、未见比较”的泛化性能。

**EN** We adopt the hyperparameters used in the experiment described in C.2 in order to save time on hyperparameter tuning.

**ZH** 为节省超参数调优的时间，我们沿用 C.2 中所述实验所用的超参数。

**EN** Table 6 compares the performance of ⟦SLOT_341⟧ to the 1.7B reward model in [5]. The overall accuracy is the weighted average of seen and unseen user accuracy. We want to emphasize that the main advantage of our model is that we do not require the existence of a supervised fine-tuned model. We used all-mpnet-base-v2 sentence transformer [54], which contains around 105M parameters, to generate the embedding for summaries and trained a 2-layer MLP with roughly 592K parameters.

**ZH** 表 6 比较了 ⟦SLOT_341⟧ 与 [5] 中 1.7B 奖励模型的性能。总体准确率是已见与未见用户准确率的加权平均。我们要强调，我们模型的主要优势在于不需要存在监督微调后的模型。我们使用约含 105M 参数的 all-mpnet-base-v2 句子转换器 [54] 生成摘要嵌入，并训练了一个约 592K 参数的两层 MLP。

**EN** Table 6: The performance of our method vs. the 1.3B reward model from [5] on Summary Dataset. Notably, our approach does not necessitate a supervised fine-tuned model. We leverage the all-mpnet-base-v2 sentence transformer [54], with 105M parameters, for summary embeddings, and train a 2-layer MLP, with 592K parameters.

**ZH** 表 6：我们的方法与 [5] 中 1.3B 奖励模型在 Summary 数据集上的性能对比。值得注意的是，我们的方法无需监督微调模型：我们用含 105M 参数的 all-mpnet-base-v2 句子转换器 [54] 生成摘要嵌入，并训练一个含 592K 参数的两层 MLP。

<!-- [原子块 · table] K = 1 K=1 K = 2 K=2 K = 3 K=3 K = 4 K=4 Seen user accuracy 60.85 ± 0.11 60.85\pm 0.11 60.95 ± 0.12 60.95\pm 0.12 60.77 ± 0.10 60.77\pm 0.10 60.81 ± 0.12 60.81\pm 0.12 Unseen user accuracy 64.13 ± 0.14 -->

**EN** Experiment Setup and Results: Comparing to [53]

**ZH** 实验设置与结果：与 [53] 对比

**EN** We evaluate our model A with hinge loss on a trimmed version of the summary dataset described in [53], to compare our results with theirs. In [53], the original training set of the summary dataset is filtered with summaries generated by SFT policies and only those comparisons made by the top 10 workers who conduct the most pairwise comparisons are kept. The test dataset is split into 2 folds where those comparisons made by the 10 workers are used to evaluate the generalization performance on seen users, whereas those comparisons made by other workers are used to evaluate the generalization performance on unseen users.

**ZH** 我们在 [53] 所述摘要数据集的一个精简版本上评估带铰链损失的模型 A，以便与其结果比较。在 [53] 中，摘要数据集的原始训练集用 SFT 策略生成的摘要作了过滤，只保留由进行成对比较最多的前 10 名工作者所作的比较；测试集被划分为两部分，其中这 10 名工作者所作的比较用于评估对已见用户的泛化性能，其他工作者所作的比较用于评估对未见用户的泛化性能。

**EN** Table 3 compares the performance of the method to the one proposed in [53]. We use the weighted average of prototypes learned as the general ideal point for new users to conduct zero-shot learning. We emphasize that even though our model only has 594K parameters and the sentence embeddings we used are generated from all-mpnet-base-v2 sentence transformer [54], which contains around 105M parameters, we still can achieve on par performance, especially in terms of unseen accuracy.

**ZH** 表 3 比较了该方法与 [53] 所提出方法的性能。我们用所学原型的加权平均作为新用户的通用理想点，以进行零样本学习。我们要强调的是，尽管我们的模型只有 594K 参数，且所用的句子嵌入来自约含 105M 参数的 all-mpnet-base-v2 句子转换器 [54]，我们仍取得了相当的性能，尤其是在未见准确率方面。

**EN** Appendix D Modeling Design

**ZH** 附录 D 建模设计

**EN** Algorithm 1 ⟦SLOT_342⟧-A algorithm

**ZH** 算法 1 ⟦SLOT_342⟧-A 算法

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

**EN** Algorithm 2 ⟦SLOT_343⟧-B algorithm

**ZH** 算法 2 ⟦SLOT_343⟧-B 算法

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

**EN** Appendix E Broader Impacts

**ZH** 附录 E 更广泛的影响

**EN** This paper presents novel contributions to the field of machine learning towards foundations for learning from heterogeneous preferences aiding the development of models and algorithms to move the needle towards plurality.

**ZH** 本文在机器学习领域作出了新颖的贡献，为从异质偏好中学习奠定基础，助力模型与算法的发展，推动其走向多元性。
