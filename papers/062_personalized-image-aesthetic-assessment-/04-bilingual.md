# 通过富偏好样本挖掘与群组合并实现个性化图像美学评价

> 原标题：Personalized Image Aesthetic Assessment via Preference-rich Sample Mining and Cohort Merging
> 作者：Zhichao Yang, Tianjiao Gu, Zhixianhe Zhang, Xiangfei Sheng, Pengfei Chen, Leida Li · arXiv:2607.15752 · 2026-07-17

<!-- [原子块 · verbatim] Personalized Image Aesthetic Assessment via Preference-rich Sample Mining and Cohort Merging -->

<!-- [原子块 · img]  -->

**EN** Figure 1. Beauty is in the eye of the beholder. Individuals with distinct profiles demonstrate significant variations in aesthetic judgments of identical images. We propose PRAC, a Multimodal Large Language Model (MLLM)-based framework that accurately predicts aesthetic ratings aligned with individual preferences and offers interpretable rationales explaining divergent judgments.

**ZH** 图 1：美存在于观者眼中。画像各异的个体对同一图像的美学判断存在显著差异。我们提出 PRAC——一个基于多模态大语言模型（MLLM）的框架，能够准确预测与个体偏好相一致的美学评分，并给出可解释的依据来说明判断为何产生分歧。

<!-- [原子块 · verbatim] Abstract. -->

<!-- [原子块 · verbatim] Personalized Image Aesthetic Assessment (PIAA) aims to predict aesthetic ratings of images that vary across individuals. The aesthetic preferences manifest to different extents across distinct visual  -->

**EN** Keywords:

**ZH** 关键词：

**EN** 1. Introduction

**ZH** 1. 引言

**EN** The widespread use of smartphones and social networks have dramatically transformed the consumption patterns of visual media. This shift has intensified user attention on image aesthetics, establishing image aesthetic assessment (IAA) as a prominent research topic (Deng et al., 2017; Yang et al., 2026b; Li et al., 2024). Early studies primarily focused on generic IAA, which predicts average aesthetic ratings that reflect general judgments (Murray et al., 2012; Yang et al., 2024b; Huang et al., 2024b; Sheng et al., 2026b). However, aesthetics is inherently subjective—different users may have substantially different aesthetic evaluations of the same image (as illustrated in Figure 1). This has driven growing interest in personalized image aesthetic assessment (PIAA), which models individual preferences by adapting to user-centric aesthetic tastes (Ren et al., 2017; Chen et al., 2025; Maerten et al., 2025). With the surging demand for customization, PIAA offers expanding applications including personalized image recommendations (Chen et al., 2024; Liu et al., 2024; Sheng et al., 2025), user-centric photo enhancement (Zhang et al., 2022; Ni et al., 2022; Sheng et al., 2026a), and personalized image generation (Xu et al., 2025; Wei et al., 2025; Yang et al., 2026a; Yang et al., 2025).

**ZH** 智能手机与社交网络的广泛使用，极大地改变了视觉媒体的消费方式。这一转变强化了用户对图像美学的关注，使图像美学评价（IAA）成为一个重要的研究课题（Deng et al., 2017; Yang et al., 2026b; Li et al., 2024）。早期研究主要关注通用 IAA，即预测反映一般性判断的平均美学评分（Murray et al., 2012; Yang et al., 2024b; Huang et al., 2024b; Sheng et al., 2026b）。然而，美学本质上是主观的——不同用户对同一图像的美学评价可能大相径庭（如图 1 所示）。这推动了个性化图像美学评价（PIAA）的兴起，它通过适配以用户为中心的美学趣味来建模个体偏好（Ren et al., 2017; Chen et al., 2025; Maerten et al., 2025）。随着定制化需求的激增，PIAA 的应用不断拓展，包括个性化图像推荐（Chen et al., 2024; Liu et al., 2024; Sheng et al., 2025）、以用户为中心的照片增强（Zhang et al., 2022; Ni et al., 2022; Sheng et al., 2026a）以及个性化图像生成（Xu et al., 2025; Wei et al., 2025; Yang et al., 2026a; Yang et al., 2025）。

<!-- [原子块 · img]  -->

**EN** Figure 2. Motivation of this study. Individual aesthetic differences vary in magnitude across distinct visual stimuli and exhibit cohort-specific distribution patterns. Two example images from the PARA database (Yang et al., 2022) are shown, along with their corresponding personalized aesthetic ratings.

**ZH** 图 2：本研究动机。个体美学差异在不同视觉刺激上表现出不同的强度，并呈现群组特有的分布模式。图中展示了来自 PARA 数据库（Yang et al., 2022）的两张示例图像及其对应的个性化美学评分。

**EN** In the past few years, a proliferation of novel PIAA models have been reported in the literature. People’s aesthetic tastes are typically determined by complex factors including both image attributes and user characteristics. This requires that models possess not only visual understanding capabilities but also knowledge of various demographic and personality dimensions, such as age, cultural background, and psychological traits (Kim et al., 2018). To address these challenges, previous vision-based PIAA methods have largely resorted to auxiliary tasks related to preference representation, such as personalized feedback or personality trait prediction (Lv et al., 2021; Li et al., 2020). Another challenge in PIAA is the few-shot learning (FSL) nature, as it is difficult to collect a large number of annotated images for a specific user. To address the dilemma, previous approaches are typically designed by fine-tuning generic IAA models (Ren et al., 2017; Wang et al., 2018), or resort to meta-learning for extracting common aesthetic features across users that can efficiently transfer to target individuals (Zhu et al., 2020; Li et al., 2022).

**ZH** 过去几年中，文献中涌现出大量新的 PIAA 模型。人们的美学趣味通常由复杂因素决定，既包括图像属性，也包括用户特征。这要求模型不仅具备视觉理解能力，还要掌握人口统计学与人格等多个维度的知识，例如年龄、文化背景与心理特质（Kim et al., 2018）。为应对这些挑战，以往基于视觉的 PIAA 方法很大程度上依赖与偏好表示相关的辅助任务，例如个性化反馈或人格特质预测（Lv et al., 2021; Li et al., 2020）。PIAA 的另一重挑战在于其小样本学习（FSL）性质——为特定用户收集大量标注图像十分困难。为摆脱这一困境，以往方法通常设计为对通用 IAA 模型做微调（Ren et al., 2017; Wang et al., 2018），或借助元学习提取跨用户的共性美学特征，以便高效迁移到目标个体（Zhu et al., 2020; Li et al., 2022）。

**EN** Despite the encouraging progress achieved, two important aspects remain underexplored in current PIAA methods. First, psychological research has demonstrated that some stimuli naturally elicit more active preference responses than others (Risko et al., 2012), indicating that not all images are equally informative for modeling aesthetic taste. Second, researches in cognitive aesthetics (Celikors and Field, 2025) revealed that aesthetic preferences often cluster among individuals with shared sensibilities—‘beauty is in the eye of your cohort’—suggesting that identifying aesthetically-resonant cohort offers valuable insights for target user modeling. Inspired by the above psychological studies, we argue that 1) quantifying the richness of aesthetic preferences across images and 2) identifying aesthetically-resonant user cohorts, provide viable pathways for modeling personalized aesthetic preferences, as illustrated in Figure 2. In this context, identified informative samples and auxiliary cohorts can navigate the few-shot learning constraints in PIAA, maximizing the utility of the limited aesthetic annotations available for target users. With comprehensive visual understanding and extensive open-world knowledge of demographic and personality factors (Jiang et al., 2023; Li et al., 2023a), Multimodal Large Language Models (MLLMs) present natural advantages for sample measurement and cohort identification.

**ZH** 尽管已取得令人鼓舞的进展，当前 PIAA 方法仍有两方面未得到充分探索。第一，心理学研究表明，某些刺激天然会比另一些引发更活跃的偏好反应（Risko et al., 2012），这意味着并非所有图像对建模美学趣味都同等有效。第二，认知美学的研究（Celikors and Field, 2025）揭示，美学偏好常在具有共通感受力的个体之间聚集——「美存在于你的同好眼中」——说明识别美学共鸣群组能为目标用户建模提供有价值的线索。受上述心理学研究启发，我们认为：1）量化图像间美学偏好的丰富程度，2）识别美学共鸣的用户群组，为建模个性化美学偏好提供了可行路径，如图 2 所示。在此框架下，所识别的高信息量样本与辅助群组可以缓解 PIAA 中的小样本学习约束，最大化目标用户有限美学标注的效用。凭借全面的视觉理解能力，以及在人口统计学与人格因素上的丰富开放世界知识（Jiang et al., 2023; Li et al., 2023a），多模态大语言模型（MLLM）在样本度量与群组识别上具有天然优势。

**EN** Motivated by the above facts, this paper presents PRAC, a novel MLLM-based PIAA model that captures individual aesthetics by preference-rich sample mining and aesthetically-resonant cohort merging. PRAC is designed with two key components: PreferSelect and PreferMerge. Specifically, the MLLM is first instructed to predict aesthetic divergence across the public through aesthetic distribution training on rich generic aesthetic data. Building upon the learned consensus aesthetic understanding and MLLMs’ open-world knowledge, PreferSelect identifies preference-rich samples by analyzing both Collective Controversy and Personalized Deviation. Collective Controversy measures the intrinsic aesthetic controversy of an image among the general public, while Personalized Deviation captures the deviation of a specific user’s aesthetic taste from the public consensus. Subsequently, targeted fine-tuning is performed on the identified preference-rich samples to encode user-specific aesthetic patterns. PreferMerge searches for aesthetically-resonant user cohorts by comparing MLLM-derived preference embeddings. Cohort-based model merging is then performed to aggregate preference patterns from aesthetically-resonant users with similar tastes to further enhance personalization for the target individual. The contributions of this work are three-fold:

**ZH** 受上述事实驱动，本文提出 PRAC——一个新颖的基于 MLLM 的 PIAA 模型，它通过富偏好样本挖掘与美学共鸣群组合并来捕捉个体美学。PRAC 由两个关键组件构成：PreferSelect 与 PreferMerge。具体地，首先通过在丰富的通用美学数据上做美学分布训练，指导 MLLM 预测公众层面的美学分歧。在习得的共识性美学理解与 MLLM 的开放世界知识之上，PreferSelect 通过分析群体争议度与个性化偏离度来识别富偏好样本：前者度量图像在公众中固有的美学争议性，后者捕捉特定用户的美学趣味相对公众共识的偏离。随后，在识别出的富偏好样本上进行针对性微调，以编码用户特有的美学模式。PreferMerge 通过比较由 MLLM 导出的偏好嵌入来搜索美学共鸣的用户群组，再执行基于群组的模型合并，聚合趣味相近的美学共鸣用户的偏好模式，进一步增强对目标个体的个性化。本工作的贡献有三个方面：

**EN** • A novel MLLM-based framework for personalized image aesthetic assessment (PRAC), which identifies informative samples and auxiliary cohorts to customize MLLMs for individual aesthetic tastes with limited annotations.

**ZH** • 一个新颖的基于 MLLM 的个性化图像美学评价框架（PRAC），它通过识别高信息量样本与辅助群组，用有限的标注为个体美学趣味定制 MLLM。

**EN** • We design two key components for preference modeling: PreferSelect mines preference-rich samples through dual-metric analysis of Collective Controversy and Personalized Deviation, while PreferMerge integrates preference patterns from aesthetically-resonant users via cohort-based merging.

**ZH** • 我们为偏好建模设计了两个关键组件：PreferSelect 通过群体争议度与个性化偏离度的双指标分析挖掘富偏好样本；PreferMerge 则通过基于群组的合并整合美学共鸣用户的偏好模式。

**EN** • Extensive experiments conducted on four PIAA benchmarks demonstrate that PRAC outperforms state-of-the-arts on personalized rating prediction. Moreover, PRAC can offer rationales for varying aesthetic judgments, enhancing predictive interpretability.

**ZH** • 在四个 PIAA 基准上开展的大量实验表明，PRAC 在个性化评分预测上优于当前最优方法。此外，PRAC 能为不同的美学判断提供解释依据，提升了预测的可解释性。

<!-- [原子块 · img]  -->

**EN** Figure 3. Overview of the proposed PRAC. The framework consists of three stages: (a) Generic Aesthetic Predictor: the MLLM is trained with aesthetic distribution supervision on generic aesthetic data to establish foundational aesthetic understanding; (b) PreferSelect: preference-rich samples are identified through collective controversy and personalized deviation metrics; (c) PreferMerge: the target user’s personalized model is constructed by merging models from aesthetically-resonant cohort.

**ZH** 图 3：所提出的 PRAC 概览。该框架由三个阶段组成：(a) 通用美学预测器：在通用美学数据上以美学分布监督训练 MLLM，建立基础的美学理解；(b) PreferSelect：通过群体争议度与个性化偏离度指标识别富偏好样本；(c) PreferMerge：通过合并美学共鸣群组的模型来构建目标用户的个性化模型。

**EN** 2. Related Works

**ZH** 2. 相关工作

**EN** Personalized Image Aesthetic Assessment. PIAA aims to model individual aesthetic tastes based on few user-provided aesthetic annotations. To capture aesthetic preferences, existing vision-based PIAA methods leveraged aesthetics-related auxiliary tasks, including users’ photo favoriting behavior (Kim et al., 2018), image re-ranking (Hamzah, 2012), and personalized retouching (Lv et al., 2021), etc. Li et al. found that individual aesthetic preference strongly correlates with their personality traits and proposed a multi-task learning framework to jointly estimate both personality traits and aesthetic preferences (Li et al., 2020). Zhu et al. further introduced a personalized aesthetic assessment approach that models aesthetic attributes of images as subjective factors and users’ personality traits as objective factors (Zhu et al., 2021). To address the few-shot learning challenge, meta-learning was adopted to identify common aesthetic features across users that can be adapted to target individuals (Li et al., 2022; Zhu et al., 2020). Recently, Yang et al. applied contrastive learning to explore users’ preference differences across various aesthetic levels (Yang et al., 2024c). Yun et al. innovatively employed Task Arithmetic to model target users’ preferences by leveraging existing generic data (Yun and Choo, 2024). Different from these approaches, we model personalized aesthetics by quantifying preference richness across images and measuring preference similarity among users.

**ZH** 个性化图像美学评价。PIAA 旨在基于少量用户提供的美学标注来建模个体美学趣味。为捕捉美学偏好，已有的基于视觉的 PIAA 方法利用了与美学相关的辅助任务，包括用户的照片收藏行为（Kim et al., 2018）、图像重排序（Hamzah, 2012）与个性化修图（Lv et al., 2021）等。Li 等人发现个体美学偏好与其人格特质高度相关，并提出多任务学习框架联合估计人格特质与美学偏好（Li et al., 2020）。Zhu 等人进一步提出一种个性化美学评价方法，把图像的美学属性建模为主观因素、把用户的人格特质建模为客观因素（Zhu et al., 2021）。为应对小样本学习的挑战，元学习被用来识别可适配到目标个体的跨用户共性美学特征（Li et al., 2022; Zhu et al., 2020）。近来，Yang 等人用对比学习探索用户在不同美学层级上的偏好差异（Yang et al., 2024c）。Yun 等人创新性地采用任务算术（Task Arithmetic），利用已有的通用数据来建模目标用户的偏好（Yun and Choo, 2024）。与这些方法不同，我们通过量化图像间偏好的丰富程度、并度量用户之间的偏好相似性来建模个性化美学。

**EN** LLMs/MLLMs-based Personalization. The emergence of LLMs and MLLMs has opened new possibilities for personalization tasks due to their excellent capabilities in understanding complex patterns, reasoning about user behaviors, and generating contextually appropriate responses (Zhang et al., 2024b). Recent efforts employ techniques like personalized prompting, adaptation, and alignment to tailor these models to individual users (Liu et al., 2025; Huang et al., 2024a). Tan et al. employed personalized parameter-efficient fine-tuning to store user-specific behavior patterns and preferences, thereby democratizing LLMs (Tan et al., 2024). Zhang et al. proposed a parameterized memory-injected approach with a bayesian optimization search strategy to achieve LLM personalization (Zhang et al., 2024a). In this study, we present the first exploration of personalizing MLLMs for modeling individual aesthetic preferences.

**ZH** 基于 LLM/MLLM 的个性化。LLM 与 MLLM 的出现为个性化任务带来了新的可能，因为它们在理解复杂模式、推理用户行为以及生成贴合语境的回答方面表现出色（Zhang et al., 2024b）。近期工作采用个性化提示、适配与对齐等技术，使这些模型适配到个体用户（Liu et al., 2025; Huang et al., 2024a）。Tan 等人用个性化的参数高效微调来存储用户特有的行为模式与偏好，从而推动 LLM 的普惠化（Tan et al., 2024）。Zhang 等人提出一种参数化记忆注入方法，配合贝叶斯优化搜索策略实现 LLM 个性化（Zhang et al., 2024a）。本文首次探索对 MLLM 做个性化，用于建模个体美学偏好。

**EN** Model Merging. Model merging efficiently combines parameters from multiple specialized models to enhance overall capabilities without additional training. Representative approaches include linear interpolation, task arithmetic, and selective parameter merging(Li et al., 2023b). For LLMs and MLLMs, this paradigm enables capability integration without the prohibitive computational costs and data requirements of full-scale retraining (Yang et al., 2024a; Lu et al., 2024). Wu et al. proposed aggregating parameters from lightweight task-specific experts learned from similar tasks to benefit target downstream tasks (Wu et al., 2023). Tang et al. designed a partial linearization method for parameter-efficient fine-tuned models, improving multi-task fusion capabilities with low computational overhead (Tang et al., 2023). In this paper, we introduce cohort-based model merging for PIAA task.

**ZH** 模型合并。模型合并能高效地把多个专用模型的参数组合起来，在无需额外训练的情况下提升整体能力。代表性方法包括线性插值、任务算术与选择性参数合并（Li et al., 2023b）。对 LLM 与 MLLM 而言，这一范式可以在不承担全面重训练的高昂计算成本与数据需求的前提下实现能力整合（Yang et al., 2024a; Lu et al., 2024）。Wu 等人提出聚合从相似任务中学得的轻量级任务专用专家的参数，以惠及目标下游任务（Wu et al., 2023）。Tang 等人针对参数高效微调模型设计了部分线性化方法，以较低的计算开销提升多任务融合能力（Tang et al., 2023）。本文则把基于群组的模型合并引入 PIAA 任务。

**EN** 3. Method

**ZH** 3. 方法

**EN** In this section, we detail the proposed PRAC, which models aesthetic preferences by mining preference-rich samples and merging aesthetically-resonant cohorts. The overall framework is shown in Figure 3, which consists of three stages. First, we establish a Generic Aesthetic Predictor by training an MLLM on rich generic aesthetic data, enabling consensus aesthetic understanding. Building on this foundation and leveraging its powerful open-world knowledge, we design PreferSelect to mine preference-rich samples. Finally, we propose PreferMerge, a cohort-based model merging strategy that identifies aesthetically-resonant users and integrates them to further boost personalization for the target individual.

**ZH** 本节详述所提出的 PRAC，它通过挖掘富偏好样本与合并美学共鸣群组来建模美学偏好。总体框架如图 3 所示，包含三个阶段。首先，我们在丰富的通用美学数据上训练 MLLM，建立通用美学预测器，使其具备共识性的美学理解。在此基础之上，并借助其强大的开放世界知识，我们设计 PreferSelect 来挖掘富偏好样本。最后，我们提出 PreferMerge——一种基于群组的模型合并策略，它识别美学共鸣用户并加以整合，进一步增强对目标个体的个性化。

**EN** 3.1. Generic Aesthetic Predictor

**ZH** 3.1. 通用美学预测器

**EN** We first train a generic aesthetic predictor to model the distribution of public aesthetic judgments. Its ability to capture preference divergence serves as a crucial prerequisite for subsequent personalization stages. Given an image ⟦SLOT_0⟧, we obtain its aesthetic distribution from the statistics of individual annotations. The distribution label is represented as probabilities over five discrete aesthetic levels [Excellent, Good, Fair, Bad, Poor], denoted as ⟦SLOT_1⟧, where ⟦SLOT_2⟧ denotes the probability of the ⟦SLOT_3⟧-th aesthetic level. Utilizing these generic aesthetic data, we integrate a parameter-efficient LoRA module (Hu et al., 2022) into MLLMs to conduct aesthetic distribution training. Specifically, we design specialized prompt templates to guide MLLMs in generating aesthetic distributions and employ the Kullback-Leibler (KL) Divergence loss to optimize parameters.

**ZH** 我们首先训练一个通用美学预测器来建模公众美学判断的分布。它捕捉偏好分歧的能力，是后续个性化阶段的重要前提。给定图像 ⟦SLOT_0⟧，我们从个体标注的统计中得到其美学分布。分布标签表示为五个离散美学层级 [Excellent, Good, Fair, Bad, Poor] 上的概率，记为 ⟦SLOT_1⟧，其中 ⟦SLOT_2⟧ 表示第 ⟦SLOT_3⟧ 个美学层级的概率。利用这些通用美学数据，我们在 MLLM 中集成参数高效的 LoRA 模块（Hu et al., 2022）来执行美学分布训练。具体地，我们设计专门的提示模板来引导 MLLM 生成美学分布，并用 Kullback-Leibler（KL）散度损失优化参数。

**EN** Guiding MLLMs for Distribution Prediction. Inspired by the training of previous MLLMs-based scoring methods (Wu et al., 2024; You et al., 2025), we prompt the MLLM with an image along with a fixed question: ‘How would you rate the aesthetic quality of this image?’. Simultaneously, we specify the output template as ‘The aesthetic quality of the image is ⟦SLOT_4⟧Level Token⟦SLOT_5⟧’, where ⟦SLOT_6⟧Level Token⟦SLOT_7⟧ represents the predicted aesthetic level. Given that the token constitutes probabilities over all possible vocabulary in the language model, we perform a close-set softmax over the five textual aesthetic levels to obtain predicted aesthetic distribution of MLLMs, denoted as ⟦SLOT_8⟧.

**ZH** 引导 MLLM 做分布预测。受以往基于 MLLM 的打分方法训练方式的启发（Wu et al., 2024; You et al., 2025），我们用一张图像与一个固定问题来提示 MLLM：“How would you rate the aesthetic quality of this image?”。同时，我们把输出模板指定为 “The aesthetic quality of the image is ⟦SLOT_4⟧Level Token⟦SLOT_5⟧”，其中 ⟦SLOT_6⟧Level Token⟦SLOT_7⟧ 表示预测的美学层级。由于该词元在语言模型中构成覆盖全部词表的概率，我们对五个文本美学层级做闭集 softmax，得到 MLLM 预测的美学分布，记为 ⟦SLOT_8⟧。

**EN** KL Loss for Parameter Update. For the ⟦SLOT_9⟧-th image ⟦SLOT_10⟧, we compute the KL divergence between the predicted distribution ⟦SLOT_11⟧ from the MLLM and the ground-truth distribution ⟦SLOT_12⟧ as the training loss. By aggregating the total loss ⟦SLOT_13⟧ across the entire training set, we optimize the parameters of the integrated LoRA module. This is formulated as:

**ZH** 用于参数更新的 KL 损失。对第 ⟦SLOT_9⟧ 张图像 ⟦SLOT_10⟧，我们计算 MLLM 预测分布 ⟦SLOT_11⟧ 与真值分布 ⟦SLOT_12⟧ 之间的 KL 散度作为训练损失。通过在整个训练集上聚合总损失 ⟦SLOT_13⟧，我们优化所集成的 LoRA 模块的参数。其形式化如下：

<!-- [原子块 · table] (1) ℒ K ​ L = 1 N g ∑ i = 1 N g D K ​ L ( 𝐪 i ∥ 𝐩 i ) = 1 N g ​ ∑ i = 1 N g ∑ j = 1 5 q j i ​ log ⁡ ( q j i p j i ) , \begin{split}\mathcal{L}_{KL}&=\frac{1}{N_{g}}\sum_{i=1}^{N_{g}}D_{KL}(\mathbf{q}^ -->

**EN** where ⟦SLOT_14⟧ denotes the KL divergence operation, ⟦SLOT_15⟧ is the number of training images and ⟦SLOT_16⟧ indexes the five aesthetic levels of [Excellent, Good, Fair, Bad, Poor].

**ZH** 其中 ⟦SLOT_14⟧ 表示 KL 散度运算，⟦SLOT_15⟧ 为训练图像数量，⟦SLOT_16⟧ 索引 [Excellent, Good, Fair, Bad, Poor] 这五个美学层级。

<!-- [原子块 · img]  -->

**EN** Figure 4. Visualization of PreferSelect results. Two users from the PARA database (Yang et al., 2022) with distinct profiles (demographics and Big-Five personality traits) and their corresponding top-3/bottom-3 preference-rich samples based on ⟦SLOT_17⟧ rankings.

**ZH** 图 4：PreferSelect 结果的可视化。图中展示了 PARA 数据库（Yang et al., 2022）中画像（人口统计学特征与大五人格特质）各异的两位用户，以及按 ⟦SLOT_17⟧ 排序得到的各自前 3 个 / 后 3 个富偏好样本。

**EN** 3.2. Preference-rich Sample Mining

**ZH** 3.2. 富偏好样本挖掘

**EN** The varying richness of aesthetic preference across images lies in the fact that certain samples are more informative for personalization. PreferSelect aims to utilize the acquired aesthetics principles of the Generic Aesthetic Predictor along with MLLM’s extensive open-world knowledge to identify preference-rich samples. Inspired by research in cognitive aesthetics showing that aesthetic experiences arise from the interplay of demographics and personality traits (Washizu et al., 2025), we design a dual-metric selection mechanism to measure the preference richness of samples. This mechanism synergistically combines two perspectives: 1) the intrinsic aesthetic controversy of an image among the general public (Collective Controversy), and 2) the predicted deviation of a specific user’s taste from the public (Personalized Deviation).

**ZH** 不同图像上美学偏好的丰富程度各异，其原因在于某些样本对个性化更具信息量。PreferSelect 旨在利用通用美学预测器习得的美学规律，以及 MLLM 丰富的开放世界知识，来识别富偏好样本。受认知美学研究发现——美学体验源于人口统计学特征与人格特质的交互（Washizu et al., 2025）——的启发，我们设计了双指标选择机制来度量样本的偏好丰富度。这一机制协同结合了两个视角：1）图像在公众中固有的美学争议性（群体争议度）；2）特定用户趣味相对公众的预测偏离（个性化偏离度）。

**EN** Collective Controversy Metric (CCM). Images eliciting significant controversy in aesthetic judgments inherently encode richer personalized preference information. Based on this observation, we design a simple yet effective metric to quantify such controversy. Specifically, for a given image ⟦SLOT_18⟧, we utilize the Generic Aesthetics Predictor to predict its aesthetic distribution ⟦SLOT_19⟧ and calculate the standard deviation (STD) of this distribution as the measurement:

**ZH** 群体争议度指标（CCM）。在美学判断上引发显著争议的图像，天然编码了更丰富的个性化偏好信息。基于这一观察，我们设计了一个简洁而有效的指标来量化这种争议性。具体地，对给定图像 ⟦SLOT_18⟧，我们用通用美学预测器预测其美学分布 ⟦SLOT_19⟧，并计算该分布的标准差（STD）作为度量：

<!-- [原子块 · table] (2) CCM ​ ( I i ) = σ ⁡ ( 𝐩 i ) = ∑ j = 1 5 ( j − μ i ) 2 ⋅ p j i , \text{CCM}(I^{i})=\sigma(\mathbf{p}^{i})=\sqrt{\sum_{j=1}^{5}(j-\mu^{i})^{2}\cdot{p_{j}^{i}}}, -->

**EN** where ⟦SLOT_20⟧ denotes the standard deviation, and ⟦SLOT_21⟧ is the mean of the distribution for image ⟦SLOT_22⟧.

**ZH** 其中 ⟦SLOT_20⟧ 表示标准差，⟦SLOT_21⟧ 为图像 ⟦SLOT_22⟧ 对应分布的均值。

**EN** Personalized Deviation Metric (PDM). People’s aesthetic preferences are significantly influenced by their intrinsic attributes, particularly personality traits and photographic expertise (Yang et al., 2022). MLLMs with extensive open-world knowledge of demographic and personality traits (Jiang et al., 2023), provide a foundation for measuring the impact of these factors on aesthetic judgments. Inspired by in-context learning (Dong et al., 2024), we convert discrete user profiles (age, traits, expertise) into natural language descriptions and integrate them into the prompt: ‘You are a ⟦SLOT_23⟧User Profile⟦SLOT_24⟧, how would you rate the aesthetic quality of this image?’. This prompt is then input to the Generic Aesthetic Predictor to generate an in-context aesthetic distribution. The PDM is defined as the KL Divergence between the generic distribution ⟦SLOT_25⟧ and the in-context distribution ⟦SLOT_26⟧:

**ZH** 个性化偏离度指标（PDM）。人们的美学偏好受其内在属性显著影响，尤其是人格特质与摄影专业经验（Yang et al., 2022）。具备人口统计学与人格特质方面丰富开放世界知识的 MLLM（Jiang et al., 2023），为度量这些因素对美学判断的影响提供了基础。受上下文学习（Dong et al., 2024）启发，我们把离散的用户画像（年龄、特质、专业经验）转换为自然语言描述，并整合进提示：“You are a ⟦SLOT_23⟧User Profile⟦SLOT_24⟧, how would you rate the aesthetic quality of this image?”。该提示随后被输入通用美学预测器，生成上下文条件下的美学分布。PDM 定义为通用分布 ⟦SLOT_25⟧ 与上下文分布 ⟦SLOT_26⟧ 之间的 KL 散度：

<!-- [原子块 · table] (3) PDM ( I i ) = D K ​ L ( 𝐩 u i ∥ 𝐩 i ) . \text{PDM}(I^{i})=D_{KL}(\mathbf{p}_{u}^{i}\parallel\mathbf{p}^{i}). -->

**EN** To comprehensively integrate both Collective Controversy and Personalized Deviation, we propose a unified preference richness score ⟦SLOT_27⟧. For image ⟦SLOT_28⟧, it is formulated as a weighted combination of the two fundamental metrics:

**ZH** 为综合考量群体争议度与个性化偏离度，我们提出统一的偏好丰富度分数 ⟦SLOT_27⟧。对图像 ⟦SLOT_28⟧，它被表述为两个基础指标的加权组合：

<!-- [原子块 · table] (4) P score ​ ( I i ) = ( 1 − α ) ⋅ CCM ​ ( I i ) + α ⋅ PDM ​ ( I i ) , \text{P}_{\text{score}}(I^{i})=(1-\alpha)\cdot\text{CCM}(I^{i})+\alpha\cdot\text{PDM}(I^{i}), -->

**EN** where ⟦SLOT_29⟧ is a weighting hyperparameter that balances the contributions of collective controversy and personalized deviation. For a specific user ⟦SLOT_30⟧ with his/her personal images, we compute ⟦SLOT_31⟧ for each image and rank all candidates accordingly. Images with higher scores are selected to form the personalized query set ⟦SLOT_32⟧ for the user. This curated set facilitates efficient encoding of user-specific aesthetic patterns in the PreferMerge stage. Figure 4 illustrates the PreferSelect results: two users with distinct demographic and personality traits demonstrate markedly different preference-rich samples. Furthermore, within each user, top-3 samples exhibit significantly higher ⟦SLOT_33⟧ than bottom-3 samples, validating the quantification of preference-richness.

**ZH** 其中 ⟦SLOT_29⟧ 是平衡群体争议度与个性化偏离度贡献的加权超参数。对拥有其个人图像的特定用户 ⟦SLOT_30⟧，我们计算每张图像的 ⟦SLOT_31⟧ 并据此为所有候选样本排序。分数较高的图像被选出，构成该用户的个性化查询集 ⟦SLOT_32⟧。这一精选集合有助于在 PreferMerge 阶段高效编码用户特有的美学模式。图 4 展示了 PreferSelect 的结果：人口统计学特征与人格特质各异的两位用户呈现出明显不同的富偏好样本。此外，在每位用户内部，前 3 个样本的 ⟦SLOT_33⟧ 明显高于后 3 个样本，验证了偏好丰富度量化是有效的。

**EN** 3.3. Aesthetically-resonant Cohort Merging

**ZH** 3.3. 美学共鸣群组合并

**EN** Based on the identified preference-rich images, we propose PreferMerge, a cohort-based model merging strategy that discovers and integrates aesthetically-resonant user cohorts to enhance target user personalization. Under limited annotation scenarios (e.g., 10-shot or 100-shot settings, commonly adopted in the PIAA task) where the target user provides aesthetic ratings on preference-rich samples, PreferMerge first measures aesthetic preference similarity across users, then identifies and merges aesthetically-resonant users to strengthen personalization for the target individual.

**ZH** 在识别出的富偏好图像基础上，我们提出 PreferMerge——一种基于群组的模型合并策略，用于发现并整合美学共鸣的用户群组，以增强对目标用户的个性化。在标注有限的场景（例如 PIAA 任务中常用的 10-shot 或 100-shot 设定）下，目标用户对富偏好样本给出美学评分；PreferMerge 先度量用户之间的美学偏好相似性，再识别并合并美学共鸣用户，从而强化对目标个体的个性化。

**EN** Measuring Cross-user Preference Similarity. Individual annotations on preference-rich samples directly reflect their aesthetic sensibilities, providing a foundation for measuring cross-user preference similarity. We fine-tune the Generic Aesthetic Predictor using these personalized annotations and extract gradient directions as preference embeddings. The correlation between preference embeddings serves as a robust metric for quantifying preference similarity among users.

**ZH** 度量跨用户偏好相似性。个体在富偏好样本上的标注直接反映其美学感受力，为度量跨用户偏好相似性提供了基础。我们用这些个性化标注微调通用美学预测器，并提取梯度方向作为偏好嵌入。偏好嵌入之间的相关性可作为量化用户间偏好相似性的稳健指标。

**EN** Given a query set ⟦SLOT_34⟧ of preference-rich samples for user ⟦SLOT_35⟧, where ⟦SLOT_36⟧ denotes the user’s personalized annotation to image ⟦SLOT_37⟧ as a discrete aesthetic level label, we perform targeted fine-tuning. A user-specific LoRA module is injected into the Generic Aesthetic Predictor and fine-tuned exclusively on its parameters ⟦SLOT_38⟧. The cross-entropy loss between predicted and ground-truth aesthetic levels guides the parameter updates. We compute the gradient fluctuations of parameters ⟦SLOT_39⟧ on the query set ⟦SLOT_40⟧ as the preference embedding for user ⟦SLOT_41⟧. Specifically, we employ the Fisher Information Matrix (FIM) as an indicator (Amari, 1998), which quantifies the model’s sensitivity to parameter perturbations under limited data:

**ZH** 给定用户 ⟦SLOT_35⟧ 的富偏好样本查询集 ⟦SLOT_34⟧，其中 ⟦SLOT_36⟧ 表示用户对图像 ⟦SLOT_37⟧ 的个性化标注（离散的美学层级标签），我们执行针对性微调：把一个用户专用的 LoRA 模块注入通用美学预测器，并仅在其参数 ⟦SLOT_38⟧ 上微调。预测美学层级与真值之间的交叉熵损失指导参数更新。我们计算参数 ⟦SLOT_39⟧ 在查询集 ⟦SLOT_40⟧ 上的梯度波动，作为用户 ⟦SLOT_41⟧ 的偏好嵌入。具体地，我们采用 Fisher 信息矩阵（FIM）作为指标（Amari, 1998），它量化了在有限数据下模型对参数扰动的敏感程度：

<!-- [原子块 · table] (5) 𝐅 u = 𝔼 ( I , y ) ∼ 𝒟 u [ ∇ θ u ​ log ​ p ​ ( y ∣ I ) ​ ∇ θ u ​ log ⁡ p ​ ( y ∣ I ) T ] , \mathbf{F}_{u}=\mathop{\mathbb{E}}\limits_{(I,y)\sim\mathcal{D}_{u}}\left[\nabla_{\theta_{u}}\log p\left(y -->

**EN** where ⟦SLOT_42⟧ represents the preference embedding. For two users ⟦SLOT_43⟧ and ⟦SLOT_44⟧, with respective embeddings ⟦SLOT_45⟧ and ⟦SLOT_46⟧, we compute the cosine distance between them to measure preference similarity ⟦SLOT_47⟧:

**ZH** 其中 ⟦SLOT_42⟧ 表示偏好嵌入。对两个用户 ⟦SLOT_43⟧ 与 ⟦SLOT_44⟧，其嵌入分别为 ⟦SLOT_45⟧ 与 ⟦SLOT_46⟧，我们计算二者之间的余弦距离来度量偏好相似性 ⟦SLOT_47⟧：

<!-- [原子块 · table] (6) Sim ⁡ ( U i , U j ) = 𝐅 u i ⋅ 𝐅 u j ‖ 𝐅 u i ‖ ⋅ ‖ 𝐅 u j ‖ . \operatorname{Sim}\left(U_{i},U_{j}\right)=\frac{\mathbf{F}_{u}^{i}\cdot\mathbf{F}_{u}^{j}}{\left\|\mathbf{F}_{u}^{i}\right\|\cdot\left\ -->

**EN** Cohort Selection and Merging. With cross-user preference similarities quantified, we identify an optimal cohort of aesthetically-resonant users and merge them to enhance target user personalization. The selection is performed on a pre-constructed User Pool, which contains personalized LoRAs from multiple training users obtained through targeted fine-tuning on their respective query sets, serving as a rich library of diverse aesthetic preferences. The selection strategy balances two key objectives: Target Relevance and Cohort Diversity. Target Relevance ensures that selected users are maximally relevant to the target individual, while Cohort Diversity prevents redundancy among the selected users. To balance these two aspects, we introduce a trade-off parameter ⟦SLOT_48⟧ and formulate the optimal selection problem as:

**ZH** 群组选择与合并。在量化跨用户偏好相似性之后，我们识别出最优的美学共鸣用户群组并加以合并，以增强对目标用户的个性化。选择过程在一个预先构建的用户池上进行：该用户池包含多个训练用户经由各自查询集上的针对性微调得到的个性化 LoRA，构成了丰富多样的美学偏好库。选择策略权衡两个关键目标：目标相关性与群组多样性。目标相关性确保所选用户与目标个体尽可能相关，群组多样性则防止所选用户之间出现冗余。为平衡这两个方面，我们引入权衡参数 ⟦SLOT_48⟧，并把最优选择问题表述为：

<!-- [原子块 · table] (7) 𝒮 ∗ = arg ⁡ max 𝒮 ⊂ 𝒫 , | 𝒮 | = K [ \displaystyle\mathcal{S}^{*}=\mathop{\arg\max}\limits_{\mathcal{S}\subset\mathcal{P},\left|\mathcal{S}\right|=K}\Big[ β ⋅ ∑ U i ∈ 𝒮 Sim ⁡ ( U t ​ a ​ r ​ g ​ e  -->

**EN** where ⟦SLOT_49⟧ denotes the User Pool, and ⟦SLOT_50⟧ is the optimal subset of ⟦SLOT_51⟧ aesthetically-resonant users that maximizes relevance to the target user while minimizing intra-cohort redundancy.

**ZH** 其中 ⟦SLOT_49⟧ 表示用户池，⟦SLOT_50⟧ 是 ⟦SLOT_51⟧ 个美学共鸣用户的最优子集，它在最大化与目标用户相关性的同时最小化群组内部冗余。

**EN** Once the optimal set ⟦SLOT_52⟧ is identified, we merge the personalized LoRA models from these selected users through a weighted fusion operation. Each model contributes proportionally to its preference similarity with the target user:

**ZH** 一旦确定了最优集合 ⟦SLOT_52⟧，我们就通过加权融合运算合并这些所选用户的个性化 LoRA 模型。每个模型按其与目标用户的偏好相似性成比例地做出贡献：

<!-- [原子块 · table] (8) θ m ​ e ​ r ​ g ​ e ​ d = ∑ i = 1 K w i ⋅ θ u i , \theta_{merged}=\sum_{i=1}^{K}w_{i}\cdot\theta_{u}^{i}, -->

**EN** where ⟦SLOT_53⟧ represents the normalized merging weight for model ⟦SLOT_54⟧. This targeted merging efficiently leverages preference patterns from users with similar aesthetic tastes to enhance the personalization for the target individual.

**ZH** 其中 ⟦SLOT_53⟧ 表示模型 ⟦SLOT_54⟧ 的归一化合并权重。这种有针对性的合并高效地利用了趣味相近用户的偏好模式，从而增强对目标个体的个性化。

**EN** 4. Experiments

**ZH** 4. 实验

**EN** 4.1. Experimental Settings

**ZH** 4.1. 实验设置

**EN** Databases. To evaluate the proposed PRAC, we conduct extensive experiments on four PIAA benchmarks: PARA (Yang et al., 2022), FLICKR-AES (Ren et al., 2017), REAL-CUR (Ren et al., 2017), and AADB (Kong et al., 2016). In these datasets, each image is annotated by multiple users for preference modeling, with key statistics summarized in Table 1. Specifically, Ann. Users per Img and Ann. Imgs per User denote the average number of users annotating each image and the average number of images annotated per user, respectively. Notably, PARA (Yang et al., 2022) provides rich user profiles characterized by six attributes: age, gender, education, artistic experience, photographic experience, and personality traits. Moreover, REAL-CUR (Ren et al., 2017) consists of photographs from real personal albums, where each image is rated exclusively by its owner.

**ZH** 数据库。为评估所提出的 PRAC，我们在四个 PIAA 基准上开展了大量实验：PARA（Yang et al., 2022）、FLICKR-AES（Ren et al., 2017）、REAL-CUR（Ren et al., 2017）与 AADB（Kong et al., 2016）。在这些数据集中，每张图像都由多位用户标注以支持偏好建模，关键统计汇总于表 1。具体地，Ann. Users per Img 与 Ann. Imgs per User 分别表示标注每张图像的平均用户数，以及每位用户标注的平均图像数。值得注意的是，PARA（Yang et al., 2022）提供了由六个属性刻画的丰富用户画像：年龄、性别、教育程度、艺术经验、摄影经验与人格特质。此外，REAL-CUR（Ren et al., 2017）由来自真实个人相册的照片构成，每张图像仅由其所有者评分。

**EN** Table 1. Statistics of PIAA datasets. ‘/’ denotes train/test split.

**ZH** 表 1：PIAA 数据集的统计。‘/’ 表示训练/测试划分。

<!-- [原子块 · table] Database PARA FLICKR-AES REAL-CUR AADB Num. of Imgs 28,220 / 3,000 35,263 / 4,737 0 / 2,871 8,458 / 1,542 Num. of Users 398 / 40 173 / 37 0 / 14 168 / 22 Ann. Users per Img 25 5 1 5 Ann. Imgs per User -->

**EN** Implementation Details. We adopt the open-source MLLM mPLUG-Owl3 (Ye et al., 2024) as our base model. During the Generic Aesthetic Predictor phase, images labeled with distribution statistics derived from multiple users’ annotations within the target PIAA databases are employed for training. We construct the User Pool using training user data from each dataset, while the testing users serve as targets. The hyperparameters are set to ⟦SLOT_55⟧=0.3, ⟦SLOT_56⟧=6, and ⟦SLOT_57⟧=0.5, with detailed ablation studies provided in Section 4.3. Notably, both the training and inference of PRAC for a target user can be executed on a single NVIDIA RTX 3090 GPU, with memory consumption and inference speed detailed in Section 4.5.

**ZH** 实现细节。我们采用开源 MLLM mPLUG-Owl3（Ye et al., 2024）作为基础模型。在通用美学预测器阶段，我们使用在目标 PIAA 数据库内由多位用户标注统计得出的分布标签图像进行训练。我们用每个数据集的训练用户数据构建用户池，测试用户则作为目标。超参数设为 ⟦SLOT_55⟧=0.3、⟦SLOT_56⟧=6 与 ⟦SLOT_57⟧=0.5，详细的消融实验见第 4.3 节。值得注意的是，PRAC 针对目标用户的训练与推理都可以在单张 NVIDIA RTX 3090 GPU 上完成，显存占用与推理速度详见第 4.5 节。

**EN** Evaluation Criterion. Similar to the previous literature, we employ the Spearman Rank-order Correlation Coefficient (SRCC) as a criterion to validate the performance of PIAA models. Furthermore, there are two commonly used testing patterns based on the number of images in the query set ⟦SLOT_58⟧, namely 10-shot and 100-shot (Ren et al., 2017).

**ZH** 评测准则。与以往文献类似，我们采用 Spearman 秩相关系数（SRCC）作为准则来检验 PIAA 模型的性能。此外，基于查询集 ⟦SLOT_58⟧ 中图像数量的不同，存在两种常用的测试模式，即 10-shot 与 100-shot（Ren et al., 2017）。

**EN** Table 2. Comparison between PRAC and state-of-the-art PIAA methods, with the average SRCC of 40 testing users from PARA (Yang et al., 2022) in 10-shot and 100-shot testing modes.

**ZH** 表 2：PRAC 与当前最优 PIAA 方法的比较，报告 PARA（Yang et al., 2022）中 40 位测试用户在 10-shot 与 100-shot 测试模式下的平均 SRCC。

<!-- [原子块 · table] Methods 10-shot 100-shot PARA (unconditional) 0.681 0.695 PARA (artistic) 0.686 0.698 PARA (photographic) 0.683 0.698 PARA (personality) 0.691 0.705 BLG-PIAA ( Zhu et al., 2020 ) 0.688 0.698 PA-IAA (  -->

**EN** Table 3. Comparison between PRAC and 11 representative PIAA models across the 37 testing users of the FLICKR-AES database (Ren et al., 2017). The best results are shown in bold.

**ZH** 表 3：PRAC 与 11 个代表性 PIAA 模型在 FLICKR-AES 数据库（Ren et al., 2017）37 位测试用户上的比较。最优结果以粗体显示。

<!-- [原子块 · table] Methods 10-shot 100-shot PAM (attribute only) 0.511 0.516 PAM (content only) 0.512 0.516 PAM ( Ren et al., 2017 ) 0.513 0.524 USAR-PPR 0.521 0.544 USAR-PAD 0.520 0.537 USAR ( Lv et al., 2018 ) 0.525 0 -->

**EN** Table 4. Performance comparison conducted on 22 testing users from the AADB (Kong et al., 2016) database.

**ZH** 表 4：在 AADB（Kong et al., 2016）数据库 22 位测试用户上的性能比较。

<!-- [原子块 · table] Methods 10-shot 100-shot BA-PIAA ( Zhu et al., 2020 ) 0.450 0.513 BLG-PIAA ( Zhu et al., 2020 ) 0.497 0.545 Inductive-PIAA ( Li et al., 2022 ) 0.524 0.565 TAPP-PIAA ( Li et al., 2022 ) 0.534 0.612 MTC -->

**EN** Table 5. Cross-database evaluation. Models trained on FLICKR-AES (Ren et al., 2017) and evaluated on testing users from REAL-CUR (Ren et al., 2017) and AADB (Kong et al., 2016) databases.

**ZH** 表 5：跨数据库评测。模型在 FLICKR-AES（Ren et al., 2017）上训练，在 REAL-CUR（Ren et al., 2017）与 AADB（Kong et al., 2016）数据库的测试用户上评估。

<!-- [原子块 · table] Databases Methods 10-shot 100-shot REAL-CUR PA-PIAA ( Li et al., 2020 ) 0.443 0.562 BLG-PIAA ( Zhu et al., 2020 ) 0.448 0.578 PIAA-SOA ( Zhu et al., 2021 ) 0.487 0.589 TAPP-PIAA ( Li et al., 2022 ) -  -->

**EN** 4.2. Performance Evaluation

**ZH** 4.2. 性能评测

**EN** Intra-database Evaluation. We first evaluate the performance of the proposed PRAC in modeling personalized aesthetic preferences on the PARA (Yang et al., 2022), FLICKR-AES (Ren et al., 2017), and AADB (Kong et al., 2016) databases. The experimental results are presented in Table 2, Table 3, and Table 4, respectively. PRAC consistently achieves the best performance across all datasets, demonstrating that PreferSelect and PreferMerge accurately capture individual aesthetic preferences. Notably, compared to auxiliary task-based methods such as USAR (user-specific re-ranking) (Lv et al., 2018), UG-PIAA (user personalized retouching) (Lv et al., 2021), and IM-PIAA (user content preference) (Hou et al., 2022), PRAC achieves superior results using only aesthetic annotations, highlighting the advantages of leveraging MLLMs for preference modeling. Furthermore, PRAC outperforms meta-learning based methods such as BLG-PIAA (Zhu et al., 2020) and TAPP-PIAA (Li et al., 2022), validating the effectiveness of preference-rich sample mining and aesthetically-resonant cohort merging for few-shot preference modeling.

**ZH** 库内评测。我们首先在 PARA（Yang et al., 2022）、FLICKR-AES（Ren et al., 2017）与 AADB（Kong et al., 2016）数据库上评估 PRAC 建模个性化美学偏好的性能，实验结果分别见表 2、表 3 与表 4。PRAC 在所有数据集上一致取得最佳性能，说明 PreferSelect 与 PreferMerge 准确捕捉到了个体美学偏好。值得注意的是，相较于 USAR（用户专用重排序）（Lv et al., 2018）、UG-PIAA（用户个性化修图）（Lv et al., 2021）与 IM-PIAA（用户内容偏好）（Hou et al., 2022）等基于辅助任务的方法，PRAC 仅用美学标注就取得了更优结果，凸显了利用 MLLM 做偏好建模的优势。此外，PRAC 也优于 BLG-PIAA（Zhu et al., 2020）与 TAPP-PIAA（Li et al., 2022）等基于元学习的方法，验证了富偏好样本挖掘与美学共鸣群组合并对小样本偏好建模的有效性。

**EN** Cross-database Evaluation. To verify the generalization performance of the PRAC, we further conduct a cross-database testing experiment. Following the protocol established in previous work (Li et al., 2020; Zhu et al., 2020; Yang et al., 2024c), we utilized the model trained on the FLICKR-AES dataset (Ren et al., 2017) to evaluate the personalization performance on 14 real users from REAL-CUR (Ren et al., 2017) and 22 testing users from AADB (Kong et al., 2016). Table 5 presents the comparative results, where PRAC consistently achieves state-of-the-art performance. These results demonstrate that the proposed PRAC has a strong generalization ability, which is important for real world applications.

**ZH** 跨数据库评测。为验证 PRAC 的泛化性能，我们进一步开展跨数据库测试实验。沿用以往工作确立的协议（Li et al., 2020; Zhu et al., 2020; Yang et al., 2024c），我们用在 FLICKR-AES 数据集（Ren et al., 2017）上训练的模型，评估其在 REAL-CUR（Ren et al., 2017）的 14 位真实用户与 AADB（Kong et al., 2016）的 22 位测试用户上的个性化性能。表 5 给出了对比结果，PRAC 一致取得当前最优性能。这些结果表明，所提出的 PRAC 具有很强的泛化能力，这对真实世界应用十分重要。

**EN** Table 6. Ablation study of PRAC components across the four PIAA databases. The ✓indicates the component is enabled.

**ZH** 表 6：在四个 PIAA 数据库上对 PRAC 各组件的消融实验。✓ 表示该组件被启用。

<!-- [原子块 · table] Databases PreferSelect PreferMerge 10-shot 100-shot PARA – – 0.634 0.672 ✓ – 0.640 0.701 ✓ ✓ 0.707 0.733 FLICKR-AES – – 0.644 0.672 ✓ – 0.661 0.717 ✓ ✓ 0.692 0.778 AADB – – 0.541 0.602 ✓ – 0.570 0.613 -->

**EN** Table 7. Personalization performance of different open-source MLLMs with and without the proposed PRAC on the PIAA task evaluated on PARA database.

**ZH** 表 7：不同开源 MLLM 在 PARA 数据库上、使用与不使用所提 PRAC 时于 PIAA 任务上的个性化性能。

<!-- [原子块 · table] Backbone 10-shot 100-shot Qwen3-VL (w/o PRAC) 0.540 0.574 Qwen3-VL (w PRAC) 0.694 0.723 InternVL-3.5 (w/o PRAC) 0.394 0.478 InternVL-3.5 (w PRAC) 0.690 0.718 mPLUG-Owl3 (w/o PRAC) 0.497 0.647 mPLUG-Ow -->

**EN** 4.3. Ablation Study

**ZH** 4.3. 消融实验

**EN** Contributions of Model Components. To validate the effectiveness of each component in PRAC, we conduct comprehensive ablation experiments on the four benchmark PIAA datasets, as summarized in Table 6. First, we examine the personalization performance of the Generic Aesthetic Predictor (baseline) fine-tuned directly on randomly selected user query sets without PreferSelect and PreferMerge. To ensure unbiased evaluation, experiments for all testing users were conducted 10 times with random sampling of training images, and the average results were recorded. The results clearly demonstrate that PRAC outperforms the Generic Aesthetic Predictor by substantial margins, with performance improvements exceeding 5% across all datasets in both 10-shot and 100-shot settings. Furthermore, we test the model using only PreferSelect, which also shows notable improvements over the baseline. These results provide evidence for the effectiveness of both PreferSelect and PreferMerge in personalized aesthetic modeling.

**ZH** 模型组件的贡献。为验证 PRAC 中每个组件的有效性，我们在四个基准 PIAA 数据集上开展了全面的消融实验，汇总于表 6。首先，我们考察直接在随机选取的用户查询集上微调、且不使用 PreferSelect 与 PreferMerge 的通用美学预测器（基线）的个性化性能。为保证评测无偏，所有测试用户的实验都随机采样训练图像并重复 10 次，记录平均结果。结果清楚地表明，PRAC 以显著优势超过通用美学预测器：在 10-shot 与 100-shot 设定下，各数据集上的性能提升均超过 5%。此外，我们测试了仅使用 PreferSelect 的模型，它相对基线同样有明显改善。这些结果证明了 PreferSelect 与 PreferMerge 在个性化美学建模中的有效性。

**EN** Impact of MLLMs. We compare the personalization performance of popular open-source MLLMs (Qwen3-VL (Bai et al., 2023), InternVL-3.5 (Wang et al., 2025), and mPLUG-Owl3 (Ye et al., 2024)) with and without PRAC on the PARA dataset, as illustrated in Table 7. The results demonstrate that PRAC consistently outperforms direct fine-tuning (no personalization) in both 10-shot and 100-shot settings across all MLLMs. Moreover, the stable performance gains validate that PRAC is model-agnostic and can be effectively integrated with various MLLM architectures to enhance personalized aesthetic modeling.

**ZH** MLLM 的影响。我们在 PARA 数据集上比较了主流开源 MLLM（Qwen3-VL（Bai et al., 2023）、InternVL-3.5（Wang et al., 2025）与 mPLUG-Owl3（Ye et al., 2024））在使用与不使用 PRAC 时的个性化性能，如表 7 所示。结果表明，在所有 MLLM 上、在 10-shot 与 100-shot 两种设定下，PRAC 都一致优于直接微调（不做个性化）。此外，稳定的性能增益验证了 PRAC 与模型架构无关，能够有效集成到各种 MLLM 架构中以增强个性化美学建模。

<!-- [原子块 · object]  -->

**EN** Figure 5. Ablation study on weight ⟦SLOT_59⟧ (balancing CCM and PDM) and user profiles (demographics, art/photography experience, and personality traits) in PreferSelect.

**ZH** 图 5：PreferSelect 中权重 ⟦SLOT_59⟧（平衡 CCM 与 PDM）以及用户画像（人口统计学特征、艺术/摄影经验与人格特质）的消融实验。

<!-- [原子块 · img]  -->

**EN** Figure 6. Ablation study on aesthetically-resonant cohort size ⟦SLOT_60⟧ and the hyperparameter ⟦SLOT_61⟧ (balancing Target Relevance and Cohort Diversity) in PreferMerge.

**ZH** 图 6：PreferMerge 中美学共鸣群组规模 ⟦SLOT_60⟧ 与超参数 ⟦SLOT_61⟧（平衡目标相关性与群组多样性）的消融实验。

**EN** Ablation of PreferSelect. The hyperparameter ⟦SLOT_62⟧ (balancing CCM and PDM) and user profiles (demographics, art/photography experience, and personality traits), jointly influence preference-rich sample mining in PreferSelect. To scrutinize these effects, we conduct an ablation study on the PARA database (Yang et al., 2022), evaluating how PreferSelect influences the modeling of personalized aesthetic preferences under varying balancing weights and when different types of user information are excluded, as illustrated in Figure 5. Results show that ⟦SLOT_63⟧ achieves optimal performance, and all ablation settings outperform the baseline (w/o PreferSelect), validating the importance of preference-rich sample mining. Moreover, user traits notably impact the measurement of preference richness, underscoring the critical role of personality traits in shaping aesthetic preferences, as similarly evidenced in PIAA studies (Li et al., 2020; Zhu et al., 2021).

**ZH** PreferSelect 消融。超参数 ⟦SLOT_62⟧（平衡 CCM 与 PDM）与用户画像（人口统计学特征、艺术/摄影经验与人格特质）共同影响 PreferSelect 中的富偏好样本挖掘。为细察这些影响，我们在 PARA 数据库（Yang et al., 2022）上开展消融实验，评估在不同平衡权重下、以及排除不同类型用户信息时，PreferSelect 如何影响个性化美学偏好的建模，如图 5 所示。结果显示，⟦SLOT_63⟧ 取得最优性能，且所有消融设定都优于基线（不使用 PreferSelect），验证了富偏好样本挖掘的重要性。此外，用户特质显著影响偏好丰富度的度量，凸显了人格特质在塑造美学偏好中的关键作用，这一点在 PIAA 研究中也有类似证据（Li et al., 2020; Zhu et al., 2021）。

**EN** Ablation of PreferMerge. The search for aesthetically-resonant users and the cohort size used for merging are crucial factors affecting the prediction of personalized aesthetic preferences for target individuals. Figure 6 presents an ablation study on the hyperparameter ⟦SLOT_64⟧ (balancing Target Relevance and Cohort Diversity) and the cohort size ⟦SLOT_65⟧ in PreferMerge. Optimal performance is achieved at ⟦SLOT_66⟧. The results reveal that smaller cohorts (⟦SLOT_67⟧) benefit from higher diversity weighting, while larger cohorts (⟦SLOT_68⟧) suffer from user redundancy, leading to performance degradation. The setting of ⟦SLOT_69⟧ demonstrates that the optimal aesthetically-resonant cohort takes into account both relevance and diversity.

**ZH** PreferMerge 消融。美学共鸣用户的搜索与用于合并的群组规模，是影响目标个体个性化美学偏好预测的关键因素。图 6 给出了对超参数 ⟦SLOT_64⟧（平衡目标相关性与群组多样性）与 PreferMerge 中群组规模 ⟦SLOT_65⟧ 的消融实验。在 ⟦SLOT_66⟧ 时取得最优性能。结果显示，较小的群组（⟦SLOT_67⟧）受益于更高的多样性权重，而较大的群组（⟦SLOT_68⟧）则因用户冗余导致性能下降。⟦SLOT_69⟧ 的设定说明，最优的美学共鸣群组同时兼顾了相关性与多样性。

**EN** 4.4. Qualitative Analysis

**ZH** 4.4. 定性分析

**EN** How PRAC Personalizes Using PreferSelect and PreferMerge? Beyond quantitative evaluation on rating prediction, we conduct a qualitative study using two example users to visualize how the proposed PRAC model performs sample mining and cohort merging, ultimately facilitating personalized aesthetic expression. As illustrated in Figure 7, for each testing user, we visualize: (1) the top-3 preference-rich samples mined by PreferSelect; (2) the identified cohort with merging weights from PreferMerge; (3) predicted ratings and reasons generated using the prompt ‘Please explain why you rated the image this way’. The two users exhibit opposite evaluations (Bad vs Good) on the same image, supported by distinct explanations, different samples from PreferSelect, and diverse cohorts from PreferMerge. This demonstrates the effectiveness of PRAC in capturing personalized aesthetic preferences.

**ZH** PRAC 如何借助 PreferSelect 与 PreferMerge 实现个性化？除评分预测上的定量评测外，我们还用两位示例用户开展定性研究，可视化 PRAC 模型如何进行样本挖掘与群组合并，最终促成个性化的美学表达。如图 7 所示，对每位测试用户我们可视化：(1) PreferSelect 挖掘出的前 3 个富偏好样本；(2) PreferMerge 识别出的群组及其合并权重；(3) 用提示 “Please explain why you rated the image this way” 生成的预测评分与理由。两位用户对同一图像给出了相反的评价（Bad 对 Good），并伴有各自的解释、来自 PreferSelect 的不同样本，以及来自 PreferMerge 的不同群组。这证明了 PRAC 捕捉个性化美学偏好的有效性。

<!-- [原子块 · img]  -->

**EN** Figure 7. Visualization of personalization modeling in PRAC with two testing users from the PARA database (Yang et al., 2022).

**ZH** 图 7：PRAC 中个性化建模的可视化，示例为 PARA 数据库（Yang et al., 2022）中的两位测试用户。

**EN** How Do Personality Traits relate to Preference Embeddings? Personality traits play a crucial role in preference-rich sample mining, while preference embeddings facilitate aesthetically-resonant cohort merging. Preference embeddings are derived by calculating parameter perturbations during the fine-tuning of the MLLM on selected preference-rich samples. To investigate the relationship between the Big-Five Personality Traits and Preference Embeddings, we conduct a qualitative analysis involving 398 users in the PARA (Yang et al., 2022). Specifically, we recorded each user’s preference embedding alongside their personality traits, which include five dimensions: Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism. Subsequently, unsupervised clustering was applied across all users, followed by the calculation of average personality traits for each cluster, as illustrated in Figure 8. The results indicate that users exhibit highly concentrated and distinct personality trait distributions. For instance, the purple cluster is characterized by high Agreeableness (Agr), while the orange cluster displays notably high levels of Extraversion (Ext) and Neuroticism (Neu). These observations underscore the effectiveness of PRAC, through PreferSelect and PreferMerge, in modeling personalized aesthetic preferences.

**ZH** 人格特质与偏好嵌入有何关系？人格特质在富偏好样本挖掘中起着关键作用，而偏好嵌入则促成了美学共鸣群组合并。偏好嵌入是通过计算 MLLM 在所选富偏好样本上微调过程中的参数扰动得到的。为考察大五人格特质与偏好嵌入之间的关系，我们对 PARA（Yang et al., 2022）中的 398 位用户开展定性分析。具体地，我们记录每位用户的偏好嵌入及其人格特质，后者包含五个维度：开放性（Openness）、尽责性（Conscientiousness）、外向性（Extraversion）、宜人性（Agreeableness）与神经质（Neuroticism）。随后对所有用户做无监督聚类，并计算每个聚类的人格特质均值，如图 8 所示。结果表明，用户呈现出高度集中且彼此区分的人格特质分布。例如，紫色聚类以高宜人性（Agr）为特征，而橙色聚类则表现出明显偏高的外向性（Ext）与神经质（Neu）。这些观察凸显了 PRAC 通过 PreferSelect 与 PreferMerge 建模个性化美学偏好的有效性。

<!-- [原子块 · img]  -->

**EN** Figure 8. Clustering distribution of 398 users based on their Big-Five personality traits and Preference Embeddings.

**ZH** 图 8：398 位用户基于其大五人格特质与偏好嵌入的聚类分布。

<!-- [原子块 · object]  -->

**EN** Figure 9. Comparison of computational costs between PRAC and the current state-of-the-art PIAA method (Yun and Choo, 2024).

**ZH** 图 9：PRAC 与当前最优 PIAA 方法（Yun and Choo, 2024）在计算开销上的比较。

**EN** 4.5. Computational Cost

**ZH** 4.5. 计算开销

**EN** For the proposed PRAC, all target users share a frozen MLLM backbone (e.g., mPLUG-Owl3) equipped with different trained personalized LoRAs. Figure 9 compares the computational costs (memory per target, training time per target, and inference speed) between PRAC and the current state-of-the-art ViT-based PIAA model (Yun and Choo, 2024). The results demonstrate that PRAC achieves competitive performance in both memory consumption and runtime efficiency. All metrics are measured on a single RTX 3090 GPU.

**ZH** 对 PRAC 而言，所有目标用户共享一个冻结的 MLLM 骨干（例如 mPLUG-Owl3），并配备各自训练好的个性化 LoRA。图 9 比较了 PRAC 与当前最优的基于 ViT 的 PIAA 模型（Yun and Choo, 2024）在计算开销（每目标显存、每目标训练时间、推理速度）上的差异。结果表明，PRAC 在显存占用与运行效率两方面都具有竞争力。所有指标均在单张 RTX 3090 GPU 上测得。

**EN** 5. Conclusion

**ZH** 5. 结论

**EN** In this paper, we rethink personalized image aesthetic assessment by modeling preference richness across images and cross-user preference similarity. We have proposed PRAC, the first MLLM-based PIAA model that accurately predicts users’ personalized aesthetic ratings on images and provides interpretable rationales explaining divergent judgments. Through preference-rich sample mining and aesthetically-resonant cohort merging, we effectively model individual aesthetic preferences under few-shot annotations. Extensive evaluations across four PIAA benchmark datasets demonstrate the superior performance of the proposed model. While very encouraging results have been achieved in this work, investigations on the cohort-relatedness of aesthetic preferences would further facilitate preference modeling, which is worth of more explorations.

**ZH** 本文通过建模图像间的偏好丰富程度与跨用户的偏好相似性，重新思考了个性化图像美学评价。我们提出 PRAC——首个基于 MLLM 的 PIAA 模型，它能准确预测用户对图像的个性化美学评分，并提供可解释的依据来说明判断为何产生分歧。借助富偏好样本挖掘与美学共鸣群组合并，我们在小样本标注条件下有效地建模了个体美学偏好。在四个 PIAA 基准数据集上的大量评测表明，所提模型性能优越。尽管本工作已取得令人鼓舞的结果，对美学偏好的群组关联性展开研究将进一步完善偏好建模，值得更多探索。

**EN** Acknowledgements.

**ZH** 致谢。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] Amari (1998) S. Amari Natural gradient works efficiently in learning . Neural computation 10 ( 2 ), pp. 251–276 . Cited by: §3.3 . -->

<!-- [原子块 · verbatim] Bai et al. (2023) J. Bai, S. Bai, Y. Chu, Z. Cui, K. Dang, X. Deng, Y. Fan, W. Ge, Y. Han, F. Huang, et al. Qwen technical report . arXiv preprint arXiv:2309.16609 . Cited by: §4.3 . -->

<!-- [原子块 · verbatim] Celikors and Field (2025) E. Celikors and D. J. Field Beauty is in the eye of your cohort: structured individual differences allow predictions of individualized aesthetic ratings of images . Cognition -->

<!-- [原子块 · verbatim] Chen et al. (2025) L. Chen, O. Strafforello, A. Maerten, T. Tuytelaars, and J. Wagemans On the role of individual differences in current approaches to computational image aesthetics . arXiv preprint a -->

<!-- [原子块 · verbatim] Chen et al. (2024) Z. Chen, L. Zhang, F. Weng, L. Pan, and Z. Lan Tailored visions: enhancing text-to-image generation with personalized prompt rewriting . In Proceedings of the IEEE/CVF Conference on -->

<!-- [原子块 · verbatim] Deng et al. (2017) Y. Deng, C. C. Loy, and X. Tang Image aesthetic assessment: an experimental survey . IEEE Signal Processing Magazine 34 ( 4 ), pp. 80–106 . Cited by: §1 . -->

<!-- [原子块 · verbatim] Dong et al. (2024) Q. Dong, L. Li, D. Dai, C. Zheng, J. Ma, R. Li, H. Xia, J. Xu, Z. Wu, B. Chang, et al. A survey on in-context learning . In Proceedings of the 2024 Conference on Empirical Methods i -->

<!-- [原子块 · verbatim] Hamzah (2012) M. Hamzah Objectifying subjectivity in images through aesthetics: a bergsonian approach . In 2012 International Conference on Innovation Management and Technology Research , pp. 247–252  -->

<!-- [原子块 · verbatim] Hou et al. (2022) J. Hou, W. Lin, G. Yue, W. Liu, and B. Zhao Interaction-matrix based personalized image aesthetics assessment . IEEE Transactions on Multimedia 25 , pp. 5263–5278 . Cited by: §4.2 ,  -->

<!-- [原子块 · verbatim] Hu et al. (2022) E. J. Hu, Y. Shen, P. Wallis, Z. Allen-Zhu, Y. Li, S. Wang, L. Wang, W. Chen, et al. Lora: low-rank adaptation of large language models. . ICLR 1 ( 2 ), pp. 3 . Cited by: §3.1 . -->

<!-- [原子块 · verbatim] Huang et al. (2024a) Y. Huang, X. Sheng, Z. Yang, Q. Yuan, Z. Duan, P. Chen, L. Li, W. Lin, and G. Shi Aesexpert: towards multi-modality foundation model for image aesthetics perception . In Proceedin -->

<!-- [原子块 · verbatim] Huang et al. (2024b) Y. Huang, Q. Yuan, X. Sheng, Z. Yang, H. Wu, P. Chen, Y. Yang, L. Li, and W. Lin Aesbench: an expert benchmark for multimodal large language models on image aesthetics perception  -->

<!-- [原子块 · verbatim] Jiang et al. (2023) G. Jiang, M. Xu, S. Zhu, W. Han, C. Zhang, and Y. Zhu Evaluating and inducing personality in pre-trained language models . In Advances in Neural Information Processing Systems , A. -->

<!-- [原子块 · verbatim] Kim et al. (2018) W. Kim, J. Choi, and J. Lee Objectivity and subjectivity in aesthetic quality assessment of digital photographs . IEEE Transactions on Affective Computing 11 ( 3 ), pp. 493–506 . Cit -->

<!-- [原子块 · verbatim] Kong et al. (2016) S. Kong, X. Shen, Z. Lin, R. Mech, and C. Fowlkes Photo aesthetics ranking network with attributes and content adaptation . In European conference on computer vision , pp. 662–679 . -->

<!-- [原子块 · verbatim] Li et al. (2023a) C. Li, J. Wang, K. Zhu, Y. Zhang, W. Hou, J. Lian, and X. Xie Emotionprompt: leveraging psychology for large language models enhancement via emotional stimulus . arXiv preprint arXiv -->

<!-- [原子块 · verbatim] Li et al. (2024) L. Li, X. Sheng, P. Chen, J. Wu, and W. Dong Towards explainable image aesthetics assessment with attribute-oriented critiques generation . IEEE Transactions on Circuits and Systems f -->

<!-- [原子块 · verbatim] Li et al. (2020) L. Li, H. Zhu, S. Zhao, G. Ding, and W. Lin Personality-assisted multi-task learning for generic and personalized image aesthetics assessment . IEEE Transactions on Image Processing 2 -->

<!-- [原子块 · verbatim] Li et al. (2023b) W. Li, Y. Peng, M. Zhang, L. Ding, H. Hu, and L. Shen Deep model fusion: a survey . arXiv preprint arXiv:2309.15698 . Cited by: §2 . -->

<!-- [原子块 · verbatim] Li et al. (2022) Y. Li, Y. Yang, H. Li, H. Chen, L. Xu, L. Li, Y. Li, and Y. Guo Transductive aesthetic preference propagation for personalized image aesthetics assessment . In Proceedings of the 30th -->

<!-- [原子块 · verbatim] Liu et al. (2025) J. Liu, Z. Qiu, Z. Li, Q. Dai, J. Zhu, M. Hu, M. Yang, and I. King A survey of personalized large language models: progress and future directions . arXiv preprint arXiv:2502.11528 .  -->

<!-- [原子块 · verbatim] Liu et al. (2024) Q. Liu, J. Zhu, Y. Yang, Q. Dai, Z. Du, X. Wu, Z. Zhao, R. Zhang, and Z. Dong Multimodal pretraining, adaptation, and generation for recommendation: a survey . In Proceedings of the  -->

<!-- [原子块 · verbatim] Lu et al. (2024) Z. Lu, C. Fan, W. Wei, X. Qu, D. Chen, and Y. Cheng Twin-merging: dynamic integration of modular expertise in model merging . Advances in Neural Information Processing Systems 37 , pp -->

<!-- [原子块 · verbatim] Lv et al. (2021) P. Lv, J. Fan, X. Nie, W. Dong, X. Jiang, B. Zhou, M. Xu, and C. Xu User-guided personalized image aesthetic assessment based on deep reinforcement learning . IEEE Transactions on Mul -->

<!-- [原子块 · verbatim] Lv et al. (2018) P. Lv, M. Wang, Y. Xu, Z. Peng, J. Sun, S. Su, B. Zhou, and M. Xu USAR: an interactive user-specific aesthetic ranking framework for images . In Proceedings of the 26th ACM internatio -->

<!-- [原子块 · verbatim] Maerten et al. (2025) A. Maerten, L. Chen, S. De Winter, C. Bossens, and J. Wagemans LAPIS: a novel dataset for personalized image aesthetic assessment . In Proceedings of the Computer Vision and Patt -->

<!-- [原子块 · verbatim] Murray et al. (2012) N. Murray, L. Marchesotti, and F. Perronnin AVA: a large-scale database for aesthetic visual analysis . In 2012 IEEE conference on computer vision and pattern recognition , pp. 24 -->

<!-- [原子块 · verbatim] Ni et al. (2022) S. Ni, F. Shao, X. Chai, H. Chen, and Y. Ho Composition-guided neural network for image cropping aesthetic assessment . IEEE Transactions on Multimedia 25 , pp. 6836–6851 . Cited by:  -->

<!-- [原子块 · verbatim] Ren et al. (2017) J. Ren, X. Shen, Z. Lin, R. Mech, and D. J. Foran Personalized image aesthetics . In Proceedings of the IEEE international conference on computer vision , pp. 638–647 . Cited by: §1  -->

<!-- [原子块 · verbatim] Risko et al. (2012) E. F. Risko, N. C. Anderson, S. Lanthier, and A. Kingstone Curious eyes: individual differences in personality predict eye movement behavior in scene-viewing . Cognition 122 ( 1 ), -->

<!-- [原子块 · verbatim] Sheng et al. (2026a) X. Sheng, Z. Duan, X. Pan, Y. Huang, Z. Yang, P. Chen, and L. Li TuningIQA: fine-grained blind image quality assessment for livestreaming camera tuning . In Proceedings of the AAA -->

<!-- [原子块 · verbatim] Sheng et al. (2026b) X. Sheng, X. Pan, Z. Yang, P. Chen, and L. Li Fine-grained image quality assessment for perceptual image restoration . In Proceedings of the AAAI Conference on Artificial Intellig -->

<!-- [原子块 · verbatim] Sheng et al. (2025) X. Sheng, P. Xie, W. Zou, P. Chen, T. Zhu, and L. Li InstructCrop: teaching multimodal large language models to crop aesthetic images . In Proceedings of the 33rd ACM International -->

<!-- [原子块 · verbatim] Tan et al. (2024) Z. Tan, Q. Zeng, Y. Tian, Z. Liu, B. Yin, and M. Jiang Democratizing large language models via personalized parameter-efficient fine-tuning . In Proceedings of the 2024 Conference on -->

<!-- [原子块 · verbatim] Tang et al. (2023) A. Tang, L. Shen, Y. Luo, Y. Zhan, H. Hu, B. Du, Y. Chen, and D. Tao Parameter efficient multi-task model fusion with partial linearization . arXiv preprint arXiv:2310.04742 . Cited -->

<!-- [原子块 · verbatim] Wang et al. (2018) G. Wang, J. Yan, and Z. Qin Collaborative and attentive learning for personalized image aesthetic assessment. . In IJCAI , pp. 957–963 . Cited by: §1 , Table 3 . -->

<!-- [原子块 · verbatim] Wang et al. (2025) W. Wang, Z. Gao, L. Gu, H. Pu, L. Cui, X. Wei, Z. Liu, L. Jing, S. Ye, J. Shao, et al. Internvl3. 5: advancing open-source multimodal models in versatility, reasoning, and efficienc -->

<!-- [原子块 · verbatim] Washizu et al. (2025) S. Washizu, Y. Abe, T. Daikoku, and Y. Kuniyoshi Bodily sensations, emotions, and personality traits in the aesthetic experience of everyday photographs . Scientific Reports . Ci -->

<!-- [原子块 · verbatim] Wei et al. (2025) Y. Wei, Y. Zheng, Y. Zhang, M. Liu, Z. Ji, L. Zhang, and W. Zuo Personalized image generation with deep generative models: a decade survey . arXiv preprint arXiv:2502.13081 . Cited b -->

<!-- [原子块 · verbatim] Wu et al. (2023) C. Wu, T. Wang, Y. Ge, Z. Lu, R. Zhou, Y. Shan, and P. Luo Pi-tuning: transferring multimodal foundation models with optimal multi-task interpolation . In International Conference on  -->

<!-- [原子块 · verbatim] Wu et al. (2024) H. Wu, Z. Zhang, W. Zhang, C. Chen, L. Liao, C. Li, Y. Gao, A. Wang, E. Zhang, W. Sun, et al. Q-align: teaching lmms for visual scoring via discrete text-defined levels . In Internati -->

<!-- [原子块 · verbatim] Xu et al. (2025) Y. Xu, W. Wang, Y. Zhang, B. Tang, P. Yan, F. Feng, and X. He Personalized image generation with large multimodal models . In Proceedings of the ACM on Web Conference 2025 , pp. 264–2 -->

<!-- [原子块 · verbatim] Yang et al. (2024a) E. Yang, L. Shen, G. Guo, X. Wang, X. Cao, J. Zhang, and D. Tao Model merging in llms, mllms, and beyond: methods, theories, applications and opportunities . arXiv preprint arXiv:2 -->

<!-- [原子块 · verbatim] Yang et al. (2022) Y. Yang, L. Xu, L. Li, N. Qie, Y. Li, P. Zhang, and Y. Guo Personalized image aesthetics assessment with rich attributes . In Proceedings of the IEEE/CVF Conference on Computer Visi -->

<!-- [原子块 · verbatim] Yang et al. (2026a) Z. Yang, T. Gu, J. Wang, F. Lin, X. Sheng, P. Chen, and L. Li Longt2ibench: a benchmark for evaluating long text-to-image generation with graph-structured annotations . In Proceedi -->

<!-- [原子块 · verbatim] Yang et al. (2024b) Z. Yang, L. Li, P. Chen, J. Wu, and W. Dong Semantics-aware image aesthetics assessment using tag matching and contrastive ranking . In Proceedings of the 32nd ACM International Co -->

<!-- [原子块 · verbatim] Yang et al. (2025) Z. Yang, L. Li, P. Chen, J. Wu, and G. Valenzise Language-guided visual perception disentanglement for image quality assessment and conditional image generation . arXiv preprint arX -->

<!-- [原子块 · verbatim] Yang et al. (2024c) Z. Yang, L. Li, Y. Yang, Y. Li, and W. Lin Multi-level transitional contrast learning for personalized image aesthetics assessment . IEEE Transactions on Multimedia 26 ( ), pp. 194 -->

<!-- [原子块 · verbatim] Yang et al. (2026b) Z. Yang, J. Wang, Z. Zhang, P. Xie, X. Sheng, P. Chen, and L. Li Fine-grained image aesthetic assessment: learning discriminative scores from relative ranks . In Proceedings of the -->

<!-- [原子块 · verbatim] Ye et al. (2024) J. Ye, H. Xu, H. Liu, A. Hu, M. Yan, Q. Qian, J. Zhang, F. Huang, and J. Zhou Mplug-owl3: towards long image-sequence understanding in multi-modal large language models . arXiv prepri -->

<!-- [原子块 · verbatim] You et al. (2025) Z. You, X. Cai, J. Gu, T. Xue, and C. Dong Teaching large language models to regress accurate image quality scores using score distribution . In Proceedings of the Computer Vision an -->

<!-- [原子块 · verbatim] Yun and Choo (2024) J. Yun and J. Choo Scaling up personalized image aesthetic assessment via task vector customization . In European Conference on Computer Vision , pp. 323–339 . Cited by: §2 , Figur -->

<!-- [原子块 · verbatim] Zhang et al. (2024a) K. Zhang, Y. Kim, and X. Liu Personalized llm response generation with parameterized memory injection . arXiv preprint arXiv:2404.03565 . Cited by: §2 . -->

<!-- [原子块 · verbatim] Zhang et al. (2022) M. Zhang, M. Li, J. Yu, and L. Chen Aesthetic photo collage with deep reinforcement learning . IEEE Transactions on Multimedia 25 , pp. 4653–4664 . Cited by: §1 . -->

<!-- [原子块 · verbatim] Zhang et al. (2024b) Z. Zhang, R. A. Rossi, B. Kveton, Y. Shao, D. Yang, H. Zamani, F. Dernoncourt, J. Barrow, T. Yu, S. Kim, et al. Personalization of large language models: a survey . arXiv preprint -->

<!-- [原子块 · verbatim] Zhu et al. (2020) H. Zhu, L. Li, J. Wu, S. Zhao, G. Ding, and G. Shi Personalized image aesthetics assessment via meta-learning with bilevel gradient optimization . IEEE Transactions on Cybernetics 52 -->

<!-- [原子块 · verbatim] Zhu et al. (2021) H. Zhu, Y. Zhou, L. Li, Y. Li, and Y. Guo Learning personalized image aesthetics from subjective and objective attributes . IEEE Transactions on Multimedia 25 , pp. 179–190 . Cited b -->

<!-- [原子块 · verbatim] Zhu et al. (2022) H. Zhu, Y. Zhou, Z. Shao, W. Du, G. Wang, and Q. Li Personalized image aesthetics assessment via multi-attribute interactive reasoning . Mathematics 10 ( 22 ), pp. 4181 . Cited by: T -->
