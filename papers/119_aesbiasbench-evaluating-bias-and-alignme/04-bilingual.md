# AesBiasBench：评估多模态语言模型在个性化图像美学评估中的偏见与对齐

> 原标题：AesBiasBench: Evaluating Bias and Alignment in Multimodal Language Models for Personalized Image Aesthetic Assessment
> 作者：Kun Li, Lai-Man Po, Hongzheng Yang, Xuyuan Xu, Kangcheng Liu, Yuzhi Zhao · arXiv:2509.11620 · 2025-09-15

<!-- [原子块 · verbatim] AesBiasBench: Evaluating Bias and Alignment in Multimodal Language Models for Personalized Image Aesthetic Assessment -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] Multimodal Large Language Models (MLLMs) are increasingly applied in Personalized Image Aesthetic Assessment (PIAA) as a scalable alternative to expert evaluations. However, their predictions may refl -->

**EN** 1 Introduction

**ZH** 1 引言

**EN** Multimodal Large Language Models (MLLMs) have demonstrated impressive capabilities in vision-language tasks such as image recognition Alayrac et al. (2022); Zhu et al. (2023), visual reasoning Achiam et al. (2023); Wu et al. (2025), and visual question answering Wu et al. (2023); Xu et al. (2025). Recently, these models have also been applied to Personalized Image Aesthetic Assessment (PIAA), which estimates the photographic or artistic quality of images based on individual preferences Yang et al. (2022). PIAA applications include image retrieval, photo ranking, and creative recommendation Ren et al. (2017).

**ZH** 多模态大语言模型（MLLM）在图像识别 Alayrac 等（2022）；Zhu 等（2023）、视觉推理 Achiam 等（2023）；Wu 等（2025）与视觉问答 Wu 等（2023）；Xu 等（2025）等视觉—语言任务上展现出令人印象深刻的能力。近来，这些模型也被应用于个性化图像美学评估（PIAA）——即依据个体偏好估计图像的摄影或艺术品质 Yang 等（2022）。PIAA 的应用包括图像检索、照片排序与创意推荐 Ren 等（2017）。

<!-- [原子块 · img]  -->

**EN** Figure 1: Examples illustrate bias in the image aesthetic empathy task. (a) and (b) show stereotypical bias in model outputs that arise from inherited cognitive priors. (c) presents human preferences for the image, which serve as a reference for evaluating the alignment of model predictions with human judgments.

**ZH** 图 1：图像美学共情任务中的偏见示例。(a) 与 (b) 展示了模型输出中源自既有认知先验的刻板印象偏见。(c) 给出人类对该图像的偏好，作为评估模型预测与人类判断对齐程度的参照。

**EN** Despite their promise, MLLMs may exhibit aesthetic bias, systematic differences in output driven by demographic attributes such as gender, age, geographic region, or education. Prior work has shown that even subtle biases in subjective tasks can lead to skewed outcomes Zangwill (2003); Dhamala et al. (2021); Tamkin et al. (2023); Bai et al. (2024). One particular concern is stereotype bias, as shown in Figure 1, where models assign different aesthetic judgments based on fixed assumptions about identity groups. Despite ongoing efforts to audit and debias deployed models for greater fairness Guo et al. (2022); Smith et al. (2023); Dige et al. (2024); Li et al. (2024a); Li et al. (2024b), implicit and often-overlooked aesthetic biases continue to persist. Moreover, bias detection alone does not explain whether these deviations are problematic. Some output variation may simply reflect valid preference alignment with real human judgments. To address this, we complement bias measurement with an explicit evaluation of alignment, how closely model outputs match the aesthetic preferences of human users from corresponding demographic groups.

**ZH** 尽管前景可期，MLLM 仍可能表现出美学偏见，即由性别、年龄、地理区域或教育程度等人口属性驱动的系统性输出差异。已有工作表明，主观任务中即便细微的偏见也会导致偏斜的结果 Zangwill（2003）；Dhamala 等（2021）；Tamkin 等（2023）；Bai 等（2024）。其中一个特别的关切是刻板印象偏见，如图 1 所示：模型依据对身份群体的固定假设给出不同的美学判断。尽管学界持续审计并去偏已部署的模型以提升公平性 Guo 等（2022）；Smith 等（2023）；Dige 等（2024）；Li 等（2024a）；Li 等（2024b），隐性的、常被忽视的美学偏见依然存在。此外，仅检测偏见并不能说明这些偏差是否成问题：某些输出差异可能只是反映了与真实人类判断的有效偏好对齐。为此，我们在偏见度量之外补充了对齐的显式评估，即模型输出与来自相应人口群体的真实人类美学偏好的贴合程度。

**EN** To support this dual analysis, we introduce AesBiasBench, a benchmark for assessing both stereotype bias and preference alignment in MLLMs applied to PIAA. Following the task structure defined in prior work Huang et al. (2024b); Huang et al. (2024a), our benchmark covers three subtasks. The first, Aesthetic Perception, concerns the evaluation of low-level technical properties such as sharpness, lighting, and color. The second, Aesthetic Assessment, captures subjective evaluations of overall visual appeal and composition. The third, Aesthetic Empathy, targets the emotional impact conveyed or evoked by an image. For each subtask, we define dedicated metrics to quantify both bias and alignment, including Identity Frequency Disparity (IFD), Normalized Representation Disparity (NRD) and Aesthetic Alignment Score (AAS).

**ZH** 为支撑这一双重分析，我们提出 AesBiasBench，一个用于评估 MLLM 在 PIAA 中刻板印象偏见与偏好对齐的基准。遵循已有工作定义的任务结构 Huang 等（2024b）；Huang 等（2024a），本基准覆盖三个子任务。第一个是美学感知，关注锐度、光照、色彩等低层技术属性的评价。第二个是美学评估，捕捉对整体视觉吸引力与构图的主观评价。第三个是美学共情，针对图像所传达或唤起的情感冲击。对每个子任务，我们定义了专门的指标来量化偏见与对齐，包括身份频率差异（IFD）、归一化表征差异（NRD）与美学对齐分数（AAS）。

**EN** We evaluate 19 MLLMs spanning a wide range of model families and parameter sizes. The results show that smaller models tend to exhibit stronger stereotype bias, while larger models demonstrate both improved fairness and closer alignment with human preferences. In perception and assessment tasks, model outputs often align most closely with the preferences of female users aged 22 to 25 with a university education. In the empathy task, model responses align with female preferences by default, but shift toward male preferences when gender information is made explicit. This shift highlights strong sensitivity to identity cues rather than neutrality. By analyzing both bias and alignment, AesBiasBench enables a more complete understanding of fairness and demographic sensitivity in MLLMs. It provides a foundation for future work on socially aware and user-aligned multimodal systems.

**ZH** 我们评估了 19 个 MLLM，覆盖广泛的模型族与参数规模。结果显示，较小的模型往往表现出更强的刻板印象偏见，而较大的模型既提升了公平性，也更贴近人类偏好。在感知与评估任务中，模型输出往往与 22 至 25 岁、受过大学教育的女性用户偏好最为契合。在共情任务中，模型回应默认与女性偏好一致，但当性别信息被显式给出时则转向男性偏好。这一转向凸显的是对身份线索的高度敏感，而非中立性。通过同时分析偏见与对齐，AesBiasBench 得以更完整地理解 MLLM 中的公平性与人口敏感性，并为具有社会意识、与用户对齐的多模态系统的后续研究奠定基础。

**EN** The contributions of this work are threefold:

**ZH** 本工作的贡献有三个方面：

**EN** • Revealing stereotype biases in MLLMs for PIAA using tailored metrics that quantify group-specific deviations.

**ZH** • 用专门设计、可量化群体特异性偏差的指标，揭示 MLLM 在 PIAA 中的刻板印象偏见。

**EN** • Analyzing alignment between model outputs and human aesthetic preferences across perceptual, assessment, and empathy dimensions.

**ZH** • 在感知、评估与共情三个维度上，分析模型输出与人类美学偏好之间的对齐。

**EN** • Evaluating 19 state-of-the-art MLLMs, highlighting the effect of model size and identity information on fairness and alignment.

**ZH** • 评估 19 个当前最优的 MLLM，凸显模型规模与身份信息对公平性与对齐的影响。

<!-- [原子块 · img]  -->

**EN** Figure 2: AesBiasBench framework for stereotype bias measurement and aesthetic alignment evaluation. The model’s default prompt includes an image ⟦SLOT_0⟧ and task ⟦SLOT_1⟧, while the personalized prompt adds a demographic group ⟦SLOT_2⟧. After obtaining model responses for all images, IFD and NRD detect stereotype bias, while AAS identifies alignment, revealing the demographic group the model’s aesthetic preferences align with.

**ZH** 图 2：AesBiasBench 框架，用于刻板印象偏见度量与美学对齐评估。模型的默认提示包含图像 ⟦SLOT_0⟧ 与任务 ⟦SLOT_1⟧，而个性化提示额外加入人口群体 ⟦SLOT_2⟧。在获得模型对所有图像的回应后，IFD 与 NRD 检测刻板印象偏见，AAS 则识别对齐，揭示模型的美学偏好与哪个人口群体相契合。

**EN** 2 Related Work

**ZH** 2 相关工作

**EN** 2.1 Personalized Image Aesthetic Assessment

**ZH** 2.1 个性化图像美学评估

**EN** Image aesthetic assessment (IAA) aims at evaluating image quality based on photographic rules Deng et al. (2017). Due to significant variations in aesthetic preferences among individuals, image aesthetics can be categorized into Generic Image Aesthetic Assessment (GIAA) and Personalized Image Aesthetic Assessment (PIAA). Regarding GIAA, early studies focused on designing and extracting image features, mapping them to annotated aesthetic labels. As a result, numerous IAA datasets have emerged to support research in this field Dhar et al. (2011); Murray et al. (2012); Yi et al. (2023).

**ZH** 图像美学评估（IAA）旨在依据摄影规则评价图像质量 Deng 等（2017）。由于个体之间的美学偏好差异显著，图像美学可分为通用图像美学评估（GIAA）与个性化图像美学评估（PIAA）。就 GIAA 而言，早期研究聚焦于设计与提取图像特征，并把它们映射到标注的美学标签上。由此涌现出大量 IAA 数据集来支撑该领域的研究 Dhar 等（2011）；Murray 等（2012）；Yi 等（2023）。

**EN** Personalized Image Aesthetic Assessment aims to capture the unique aesthetic preferences of individuals Yang et al. (2022). Early approaches typically adapted generic aesthetic models by integrating additional attributes or personal rating data. For instance, Ren et al. (2017) introduced residual scores to adjust generic predictions, while Zhu et al. (2020) fine-tuned pretrained GIAA models on user-specific annotations. Similarly, Cui et al. (2020) employed GIAA models as feature extractors to represent personalized preferences. Moving beyond direct adaptation, Hou et al. (2022) modeled personalized aesthetic experiences through interaction matrices between image content and user preferences. More recently, frameworks such as Q-instruct Wu et al. (2024a) and Q-align Wu et al. (2023) have enhanced the visual capabilities of MLLMs, laying a foundation for applying them to PIAA tasks.

**ZH** 个性化图像美学评估旨在捕捉个体独特的美学偏好 Yang 等（2022）。早期方法通常通过融入额外属性或个人评分数据来改造通用美学模型。例如，Ren 等（2017）引入残差分数来校正通用预测，Zhu 等（2020）则在用户专属标注上微调预训练的 GIAA 模型。类似地，Cui 等（2020）用 GIAA 模型作为特征提取器来表示个性化偏好。除直接改造之外，Hou 等（2022）通过图像内容与用户偏好之间的交互矩阵对个性化美学体验建模。更近期地，Q-instruct Wu 等（2024a）与 Q-align Wu 等（2023）等框架增强了 MLLM 的视觉能力，为把它们应用于 PIAA 任务奠定了基础。

**EN** 2.2 Biases in MLLMs

**ZH** 2.2 MLLM 中的偏见

**EN** The recent success of large language models (LLMs) has fueled exploration into vision-language interaction, leading to the emergence of multimodal large language models (MLLMs). These models have demonstrated strong capabilities in dialogue based on visual inputs. Given their advanced visual understanding, MLLMs can be leveraged to tackle various multimodal tasks related to high-level vision, including image aesthetic assessment Zhou et al. (2024). However, the inherent biases in MLLMs may introduce systematic distortions in image evaluations, leading to biased aesthetic assessments.

**ZH** 大语言模型（LLM）近来的成功推动了对视觉—语言交互的探索，催生了多模态大语言模型（MLLM）。这些模型在基于视觉输入的对话中展现出强大能力。凭借其先进的视觉理解，MLLM 可被用于处理与高层视觉相关的各类多模态任务，其中包括图像美学评估 Zhou 等（2024）。然而，MLLM 固有的偏见可能在图像评价中引入系统性扭曲，导致有偏的美学评估。

**EN** Recent studies have explored the response biases in LLMs, which often influenced by various contextual and cultural factors Gallegos et al. (2024); Tjuatja et al. (2023). Such biases also appear in MLLMs, where visual and textual modalities can interact in ways that reinforce existing societal biases Chen et al. (2024a). These biases are commonly detected and analyzed through its manifestations in model outputs Lin et al. (2024); Kumar et al. (2024); Naous et al. (2023). Specifically, Jiang et al. (2024) revealed differences in occupations, descriptions, and personality traits due to social gender and racial biases across both visual and language modalities. Building on this line of work Bai et al. (2024), where implicit bias is defined as systematic and unconscious associations embedded in model behavior, we extend this notion to the aesthetic domain.

**ZH** 近期研究探讨了 LLM 中的回应偏见，这类偏见常受各种语境与文化因素影响 Gallegos 等（2024）；Tjuatja 等（2023）。这类偏见同样出现在 MLLM 中：视觉与文本模态可能以强化既有社会偏见的方式相互作用 Chen 等（2024a）。这些偏见通常通过其在模型输出中的表现被检测和分析 Lin 等（2024）；Kumar 等（2024）；Naous 等（2023）。具体地，Jiang 等（2024）揭示了由社会性别与种族偏见在视觉与语言两种模态中造成的职业、描述与人格特质差异。在 Bai 等（2024）这一脉络的基础上——该工作把隐性偏见定义为嵌入模型行为的系统性、无意识关联——我们把这一概念扩展到美学领域。

**EN** We define aesthetic bias as a form of subtle bias in which aesthetic judgments consistently correlate with identity attributes such as gender, age, or education, even when the image content remains unchanged. These correlations may result from skewed training distributions or inductive biases in model architecture. We focus on aesthetic biases that emerge when MLLMs evaluate images conditioned on identity information, examining stereotype bias across demographic groups and assessing whether model outputs align with or distort corresponding human aesthetic preferences.

**ZH** 我们把美学偏见定义为一种细微的偏见形式：即便图像内容保持不变，美学判断仍持续地与性别、年龄或教育等身份属性相关联。这类关联可能源于偏斜的训练分布或模型架构中的归纳偏置。我们关注 MLLM 在以身份信息为条件评估图像时出现的美学偏见，考察跨人口群体的刻板印象偏见，并评估模型输出是与相应人类美学偏好相符，还是扭曲了它们。

**EN** 3 Methodology

**ZH** 3 方法

**EN** 3.1 Preliminaries

**ZH** 3.1 预备知识

**EN** This section introduces our definition and design of bias quantification when MLLMs applied to personalized image aesthetic assessment labeling. Our overall framework is illustrated in Figure 2, and the detailed prompt design can be found in the Appendix A. Basically, the bias quantification problem includes four components: the image to be assessed ⟦SLOT_3⟧, the specific assessment task ⟦SLOT_4⟧, the specific identity ⟦SLOT_5⟧ and the MLLM ⟦SLOT_6⟧ used for quality assessment. For task ⟦SLOT_7⟧, we can collect the response ⟦SLOT_8⟧ from the MLLM as follows:

**ZH** 本节介绍在 MLLM 应用于个性化图像美学评估标注时，我们对偏见量化的定义与设计。整体框架如图 2 所示，详细的提示设计见附录 A。大体上，偏见量化问题包含四个组成部分：待评估图像 ⟦SLOT_3⟧、具体评估任务 ⟦SLOT_4⟧、具体身份 ⟦SLOT_5⟧ 以及用于质量评估的 MLLM ⟦SLOT_6⟧。对于任务 ⟦SLOT_7⟧，我们可以如下从 MLLM 收集回应 ⟦SLOT_8⟧：

<!-- [原子块 · table] M ⁡ ( i , t , g ) = k , M(i,t,g)=k, (1) -->

**EN** where ⟦SLOT_9⟧ and ⟦SLOT_10⟧. Specifically, ⟦SLOT_11⟧ is the model output, ⟦SLOT_12⟧ denotes the output format set, and ⟦SLOT_13⟧ is the identity group, respectively.

**ZH** 其中 ⟦SLOT_9⟧ 与 ⟦SLOT_10⟧。具体地，⟦SLOT_11⟧ 是模型输出，⟦SLOT_12⟧ 表示输出格式集合，⟦SLOT_13⟧ 则是身份组。

**EN** Following Huang et al. (2024b), we focus on three assessment tasks, including Aesthetic Perception which representing the perceived quality of the image, Aesthetic Assessment which representing the subjective aesthetic appeal of the image, and Aesthetic Empathy which capturing the emotional response evoked by the image. Formally, ⟦SLOT_14⟧.

**ZH** 沿用 Huang 等（2024b），我们关注三项评估任务：美学感知，代表图像的感知质量；美学评估，代表图像的主观美学吸引力；美学共情，捕捉图像所唤起的情感反应。形式化地，⟦SLOT_14⟧。

**EN** Take PARA database (Yang et al., 2022) as an example, we define the output format set ⟦SLOT_15⟧ for each of the three tasks. For Aesthetic Perception and Aesthetic Assessment, ⟦SLOT_16⟧. For Aesthetic Empathy, ⟦SLOT_17⟧.

**ZH** 以 PARA 数据库（Yang 等, 2022）为例，我们为三项任务各定义输出格式集合 ⟦SLOT_15⟧。对于美学感知与美学评估，⟦SLOT_16⟧。对于美学共情，⟦SLOT_17⟧。

**EN** We define identity group set ⟦SLOT_18⟧ containing three categories, i.e., ⟦SLOT_19⟧ and ⟦SLOT_20⟧. Then, we divide the individuals into different identities ⟦SLOT_21⟧ in each group category ⟦SLOT_22⟧. For age group, ⟦SLOT_23⟧. For education group, ⟦SLOT_24⟧. For gender group, ⟦SLOT_25⟧.

**ZH** 我们定义身份组集合 ⟦SLOT_18⟧，包含三个类别，即 ⟦SLOT_19⟧ 与 ⟦SLOT_20⟧。随后，我们在每个组类别 ⟦SLOT_22⟧ 中把个体划分为不同的身份 ⟦SLOT_21⟧。对年龄组，⟦SLOT_23⟧。对教育组，⟦SLOT_24⟧。对性别组，⟦SLOT_25⟧。

**EN** Following the setting in the previous work Yang et al. (2022), we evaluate the bias among different image types ⟦SLOT_26⟧, where the image type set ⟦SLOT_27⟧ and ⟦SLOT_28⟧.

**ZH** 沿用先前工作 Yang 等（2022）的设置，我们评估不同图像类型 ⟦SLOT_26⟧ 之间的偏见，其中图像类型集合 ⟦SLOT_27⟧ 且 ⟦SLOT_28⟧。

**EN** 3.2 Quantifying Bias

**ZH** 3.2 量化偏见

**EN** To analyze stereotype bias, we propose two metrics: Identity Frequency Disparity (IFD) and Normalized Representation Disparity (NRD). IFD measures differences in how often the model assigns specific aesthetic evaluations ⟦SLOT_29⟧ to various identity groups. This metric quantifies disparities in frequency, revealing potential biases in how different identities are assessed. NRD examines the model’s preferences and emotional responses toward different types of images across identities. By normalizing for baseline differences in representation, NRD captures variations in the model’s perceptions and affective reactions that may indicate bias. Together, these metrics provide a structured approach to identify and quantify stereotype bias in the model’s behavior. Both IFD and NRD measure deviations from demographic parity. For unbiased case:

**ZH** 为分析刻板印象偏见，我们提出两个指标：身份频率差异（IFD）与归一化表征差异（NRD）。IFD 衡量模型把特定美学评价 ⟦SLOT_29⟧ 赋予不同身份组的频率差异，量化频率上的不均，从而揭示不同身份在被评估时可能存在的偏见。NRD 考察模型跨身份对不同类型图像的偏好与情感反应，通过归一化表征上的基线差异，捕捉模型感知与情感反应中可能指示偏见的变化。这两个指标共同提供了一种结构化途径，用于识别并量化模型行为中的刻板印象偏见。IFD 与 NRD 都度量对人口均等的偏离。对于无偏情形：

<!-- [原子块 · table] P ⁡ ( M ⁡ ( i , t , g ) = k ) \displaystyle P\!\big(M(i,t,g)=k\big) = P ⁡ ( M ⁡ ( i , t ) = k ) , \displaystyle=P\!\big(M(i,t)=k\big), (2) -->

**EN** where ⟦SLOT_30⟧ and ⟦SLOT_31⟧ is the identity group. It means that the output distributions are the same for input prompt with and without specific identity ⟦SLOT_32⟧.

**ZH** 其中 ⟦SLOT_30⟧，且 ⟦SLOT_31⟧ 为身份组。这意味着在带有与不带特定身份 ⟦SLOT_32⟧ 的提示下，输出分布相同。

**EN** For Identity Frequency Disparity (IFD), it’s based on total variation distance:

**ZH** 对于身份频率差异（IFD），它基于全变差距离：

<!-- [原子块 · table] IFD ​ ( t ) = 1 n Φ × n O ​ ∑ k ∈ O ∑ G ∈ Φ ∑ g ∈ G | p g , k − p G , k | , \text{IFD}(t)=\frac{1}{n_{\Phi}\times n_{O}}\sum_{k\in O}\sum_{G\in\Phi}\sum_{g\in G}{\left|p_{g,k}-p_{G,k}\right|}, (3) -->

<!-- [原子块 · table] p g , k = n ⁡ ( M ⁡ ( i , t , g ) = k ) ∑ r = 1 n O n ⁡ ( M ⁡ ( i , t , g ) = r ) , p_{g,k}=\frac{n(M(i,t,g)=k)}{\sum_{r=1}^{n_{O}}n(M(i,t,g)=r)}, (4) -->

**EN** where ⟦SLOT_33⟧ represents the proportion of choice ⟦SLOT_34⟧ in all choices made by the identity ⟦SLOT_35⟧ and ⟦SLOT_36⟧ denotes the number of times the model outputs ⟦SLOT_37⟧. ⟦SLOT_38⟧ represents the proportion of choice ⟦SLOT_39⟧ in all choices made by the all identities in the group ⟦SLOT_40⟧. ⟦SLOT_41⟧ is the number of identities in category ⟦SLOT_42⟧, ⟦SLOT_43⟧ is the number of group categories, and ⟦SLOT_44⟧ is the number of the output choices. The core component is: ⟦SLOT_45⟧. It measures the absolute deviation between the group-specific and the overall output distributions. This term satisfies non-negativity (⟦SLOT_46⟧), which is 0 only if perfect demographic parity holds, i.e., the probability of each output ⟦SLOT_47⟧ is the same across all identity groups.

**ZH** 其中 ⟦SLOT_33⟧ 表示在身份 ⟦SLOT_35⟧ 所做的全部选择中选项 ⟦SLOT_34⟧ 所占的比例，⟦SLOT_36⟧ 表示模型输出 ⟦SLOT_37⟧ 的次数；⟦SLOT_38⟧ 表示在组 ⟦SLOT_40⟧ 中所有身份所做的全部选择中选项 ⟦SLOT_39⟧ 所占的比例。⟦SLOT_41⟧ 是类别 ⟦SLOT_42⟧ 中的身份数量，⟦SLOT_43⟧ 是组类别数量，⟦SLOT_44⟧ 是输出选项数量。其核心部分是 ⟦SLOT_45⟧。它度量群体专属分布与整体输出分布之间的绝对偏离。该项满足非负性（⟦SLOT_46⟧），仅当完全的人口均等成立时取 0，即每个输出 ⟦SLOT_47⟧ 的概率在所有身份组之间相同。

**EN** The Normalized Representation Disparity (NRD) measures the disparities in the MLLM output ⟦SLOT_48⟧ between different specific identities ⟦SLOT_49⟧ for a given task ⟦SLOT_50⟧, where ⟦SLOT_51⟧, normalized by the total sentiment for each output ⟦SLOT_52⟧ across the identity group. For unbiased case:

**ZH** 归一化表征差异（NRD）度量在给定任务 ⟦SLOT_50⟧ 下，MLLM 输出 ⟦SLOT_48⟧ 在不同特定身份 ⟦SLOT_49⟧ 之间的差异（其中 ⟦SLOT_51⟧），并按身份组内每个输出 ⟦SLOT_52⟧ 的总情感做归一化。对于无偏情形：

<!-- [原子块 · table] P ⁡ ( g ∣ M ⁡ ( i , t ) = k , type ​ ( i ) = m ) = 1 n G , \displaystyle P(g\mid M(i,t)=k,\,\text{type}(i)=m)=\tfrac{1}{n_{G}}, (5) -->

**EN** which means different identities have the same preference distribution for a certain type of image.

**ZH** 这意味着不同身份对某一类型图像具有相同的偏好分布。

<!-- [原子块 · img]  -->

<!-- [原子块 · equation]  -->

**EN** Figure 3: Left: IFD scores heatmap across a diverse set of models. Right: Radar chart of IFD scores for InternVL-2.5 series models, showing variations by model size. A higher IFD indicates a greater degree of stereotype bias.

**ZH** 图 3：左：跨多个模型的 IFD 分数热力图。右：InternVL-2.5 系列模型的 IFD 分数雷达图，展示随模型规模的变化。IFD 越高表示刻板印象偏见越强。

**EN** NRD measures the deviation from this target. It is defined as:

**ZH** NRD 度量对这一目标的偏离。其定义为：

<!-- [原子块 · table] NRD ​ ( t ) = 1 n O ​ ∑ k ∈ O 1 n G ​ ∑ g ∈ G ∑ m ∈ Ω ( q g , k , m − 1 n G ) 2 , \text{NRD}(t)=\frac{1}{n_{O}}\sum_{k\in O}\sqrt{\frac{1}{n_{G}}\sum_{g\in G}\sum_{m\in\Omega}\left(q_{g,k,m}-\frac{1}{ -->

<!-- [原子块 · table] q g , k , m = n ⁡ ( M ⁡ ( i , t , g ) = k | m ) ∑ h = 1 n G n ⁡ ( M ⁡ ( i , t , h ) = k | m ) , q_{g,k,m}=\frac{n(M(i,t,g)=k|m)}{\sum_{h=1}^{n_{G}}n(M(i,t,h)=k|m)}, (7) -->

**EN** where ⟦SLOT_54⟧ is the number of times the model outputs ⟦SLOT_55⟧ for the task ⟦SLOT_56⟧ and the specific identity ⟦SLOT_57⟧ within image type ⟦SLOT_58⟧ (⟦SLOT_59⟧). Like IFD, NRD satisfies non-negativity (⟦SLOT_60⟧) which is 0 only if conditional demographic parity holds, meaning that for every output class ⟦SLOT_61⟧ and image type ⟦SLOT_62⟧, all identity groups appear with equal frequency in the outputs.

**ZH** 其中 ⟦SLOT_54⟧ 是模型在图像类型 ⟦SLOT_58⟧（⟦SLOT_59⟧）内、针对任务 ⟦SLOT_56⟧ 与特定身份 ⟦SLOT_57⟧ 输出 ⟦SLOT_55⟧ 的次数。与 IFD 类似，NRD 满足非负性（⟦SLOT_60⟧），仅当条件人口均等成立时取 0，即对每个输出类别 ⟦SLOT_61⟧ 与图像类型 ⟦SLOT_62⟧，所有身份组在输出中出现的频率相等。

**EN** 3.3 Alignment Evaluation

**ZH** 3.3 对齐评估

**EN** We evaluate the extent to which the biased outputs of MLLMs align with the aesthetic judgments of human users from corresponding demographic groups. This analysis focuses on measuring how closely model outputs reflect real human preferences, providing a complementary perspective on the effects of stereotype bias. We conduct this evaluation from two perspectives:

**ZH** 我们评估 MLLM 的带偏输出在多大程度上与来自相应人口群体的人类用户的美学判断相对齐。这一分析聚焦于度量模型输出反映真实人类偏好的贴合程度，从而为刻板印象偏见的影响提供一个互补视角。我们从两个角度开展评估：

**EN** • We examine which demographic groups the model’s aesthetic judgments are more aligned with its default or pre-trained aesthetic preferences. This focuses on identifying whether the model shows a stronger bias towards certain groups when no specific identity is specified.

**ZH** • 考察模型的美学判断与其默认（即预训练）美学偏好更贴合哪个人口群体。这聚焦于识别在未指定具体身份时，模型是否对某些群体表现出更强的偏向。

**EN** • We explore which demographic groups the model’s aesthetic judgments align more closely with human aesthetic preferences, when given the identity information explicitly. This helps identify whether the model’s outputs reflect the actual preferences of different identity groups.

**ZH** • 探索在显式给定身份信息时，模型的美学判断与哪个人口群体的人类美学偏好更贴合。这有助于识别模型输出是否反映了不同身份群体的实际偏好。

**EN** To measure the similarity between two outputs, we compute the similarity score using the Jensen-Shannon Divergence. Let ⟦SLOT_63⟧ and ⟦SLOT_64⟧ represent the model’s outputs for images from groups ⟦SLOT_65⟧ and ⟦SLOT_66⟧ where ⟦SLOT_67⟧. To compute the JS divergence, we first map the discrete aesthetic choices in ⟦SLOT_68⟧ to probability distributions using a one-hot encoding scheme, obtaining ⟦SLOT_69⟧ and ⟦SLOT_70⟧. The JS divergence between ⟦SLOT_71⟧ and ⟦SLOT_72⟧ can then be calculated as:

**ZH** 为度量两个输出之间的相似性，我们用 Jensen-Shannon 散度计算相似度分数。令 ⟦SLOT_63⟧ 与 ⟦SLOT_64⟧ 分别表示模型对来自组 ⟦SLOT_65⟧ 与 ⟦SLOT_66⟧ 的图像的输出，其中 ⟦SLOT_67⟧。为计算 JS 散度，我们先用独热编码把 ⟦SLOT_68⟧ 中的离散美学选项映射为概率分布，得到 ⟦SLOT_69⟧ 与 ⟦SLOT_70⟧。⟦SLOT_71⟧ 与 ⟦SLOT_72⟧ 之间的 JS 散度可如下计算：

<!-- [原子块 · table] JS ( E g ∥ E h ) = 1 2 [ KL ( E g ∥ E ¯ ) + KL ( E h ∥ E ¯ ) ] , \displaystyle\text{JS}(E_{g}\!\parallel\!E_{h})=\frac{1}{2}\left[\text{KL}(E_{g}\!\parallel\!\bar{E})\!+\!\text{KL}(E_{h}\!\parallel\!\ -->

**EN** where ⟦SLOT_73⟧ is the average distribution of ⟦SLOT_74⟧ and ⟦SLOT_75⟧, ⟦SLOT_76⟧. The Kullback-Leibler (KL) divergence KL is given by:

**ZH** 其中 ⟦SLOT_73⟧ 是 ⟦SLOT_74⟧ 与 ⟦SLOT_75⟧ 的平均分布，⟦SLOT_76⟧。Kullback-Leibler（KL）散度 KL 定义为：

<!-- [原子块 · table] KL ( E ∥ E ¯ ) \displaystyle\text{KL}(E\parallel\bar{E}) = ∑ j E ⁡ ( j ) ​ log ⁡ ( E ⁡ ( j ) E ¯ ​ ( j ) ) . \displaystyle=\sum_{j}E(j)\log\left(\frac{E(j)}{\bar{E}(j)}\right). (9) -->

**EN** To evaluate the alignment, we define the similarity score as:

**ZH** 为评估对齐，我们把相似度分数定义为：

<!-- [原子块 · table] S ( g ) = 1 − JS ( E g ∥ E h ) , S(g)=1-\text{JS}(E_{g}\parallel E_{h}), (10) -->

**EN** and the Aesthetic Alignment Score (AAS) is defined as follows:

**ZH** 而美学对齐分数（AAS）定义如下：

<!-- [原子块 · table] AAS ​ ( g ) = S ​ ( g ) − S ¯ , \text{AAS}(g)=S(g)-\bar{S}, (11) -->

**EN** where ⟦SLOT_77⟧ is the similarity score of the current identity ⟦SLOT_78⟧ and ⟦SLOT_79⟧ is the mean similarity score of all ⟦SLOT_80⟧ within the category ⟦SLOT_81⟧.

**ZH** 其中 ⟦SLOT_77⟧ 是当前身份 ⟦SLOT_78⟧ 的相似度分数，⟦SLOT_79⟧ 是类别 ⟦SLOT_81⟧ 内所有 ⟦SLOT_80⟧ 的平均相似度分数。

**EN** This metric is designed to compare the relative accuracy across different demographic groups, highlighting potential disparities in the model’s ability to align with human aesthetic evaluations.

**ZH** 该指标旨在比较不同人口群体之间的相对准确性，凸显模型在对齐人类美学评估能力上的潜在差异。

**EN** 4 Experiments

**ZH** 4 实验

**EN** 4.1 Experimental Setup

**ZH** 4.1 实验设置

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

**EN** Figure 4: Left: NRD scores for age, gender, and education across three tasks. Right: ⟦SLOT_82⟧ scores of fear emotion from different groups for the aesthetic empathy task in Claude-3.5-Sonnet, illustrating stereotype bias.

**ZH** 图 4：左：三项任务上按年龄、性别与教育划分的 NRD 分数。右：Claude-3.5-Sonnet 在美学共情任务中来自不同群体的恐惧情感 ⟦SLOT_82⟧ 分数，展示了刻板印象偏见。

**EN** Dataset. In our experiments, we investigate bias in three identity dimensions: gender, age, and education. Each dimension is specifically chosen to investigate societal biases in aesthetic perceptions toward the respective groups. We perform extensive testing on a well-established dataset for personalized image aesthetic assessment (Yang et al., 2022), the Personalized Image Aesthetics Database with Rich Attributes (PARA). PARA comprises 31,220 images annotated by 438 human raters with rich feature annotations. Built upon it, we generate three types of task evaluations for the 31,220 images: aesthetic perception, aesthetic assessment, and emotional perception. For aesthetic perception and aesthetic assessment, the scores in PARA range from 1 to 5. The three tasks are evaluated by IFD, NRD, AAS, and similarity score to examine both stereotype bias and aesthetic alignment.

**ZH** 数据集。在实验中，我们考察三个身份维度上的偏见：性别、年龄与教育。每个维度都是为了考察美学感知中针对相应群体的社会偏见而特意选取的。我们在一个成熟的个性化图像美学评估数据集（Yang 等, 2022）——带有丰富属性的个性化图像美学数据库（PARA）上开展大量测试。PARA 包含 31,220 张图像，由 438 名人类评分者标注，并带有丰富的特征标注。在其基础上，我们为这 31,220 张图像生成三类任务评估：美学感知、美学评估与情感感知。对于美学感知与美学评估，PARA 中的分数范围为 1 到 5。三项任务分别用 IFD、NRD、AAS 与相似度分数评估，以同时考察刻板印象偏见与美学对齐。

**EN** To consider the diversity of the PIAA database, we also evaluate on the Leuven Art Personalized Image Set (LAPIS) (Maerten et al., 2025), which contains 11,723 artistic images scored on a 0–100 scale by an average of 24 annotators (552 participants in total) and provides demographic metadata (age, gender, nationality, education, and art interest) for finer analysis under controlled conditions. Results on LAPIS are reported in the Appendix B.

**ZH** 为兼顾 PIAA 数据库的多样性，我们还在 Leuven 艺术个性化图像集（LAPIS）（Maerten 等, 2025）上评估，该数据集包含 11,723 张艺术图像，按 0–100 量表由平均 24 名标注者评分（共 552 名参与者），并提供人口元数据（年龄、性别、国籍、教育与艺术兴趣），以便在受控条件下做更精细的分析。LAPIS 上的结果报告于附录 B。

**EN** To align with human raters, we convert continuous scores into discrete rating levels. In AesBiasBench, this ensures consistency with the output formats ⟦SLOT_83⟧ and facilitates fair comparisons between model outputs and human judgments. For Aesthetic Perception and Aesthetic Assessment, we adopt equidistant intervals to convert scores into rating levels by mapping ⟦SLOT_84⟧ as in Wu et al. (2023), which is to uniformly divide the range between the highest score (⟦SLOT_85⟧) and lowest score (⟦SLOT_86⟧) into three distinct intervals. For the score ⟦SLOT_87⟧ in the dataset:

**ZH** 为与人类评分者对齐，我们把连续分数转换为离散的评分等级。在 AesBiasBench 中，这保证了与输出格式 ⟦SLOT_83⟧ 的一致性，并便于在模型输出与人类判断之间做公平比较。对于美学感知与美学评估，我们采用等距区间，通过映射 ⟦SLOT_84⟧ 把分数转换为评分等级（沿用 Wu 等（2023）的做法），即把最高分（⟦SLOT_85⟧）与最低分（⟦SLOT_86⟧）之间的范围均匀划分为三个区间。对数据集中的分数 ⟦SLOT_87⟧：

<!-- [原子块 · table] L ⁡ ( s ) = l j L(s)=l_{j} (12) -->

**EN** where ⟦SLOT_88⟧, and ⟦SLOT_89⟧. Take the PARA database as an example, ⟦SLOT_90⟧ and ⟦SLOT_91⟧, while for the LAPIS dataset, ⟦SLOT_92⟧ and ⟦SLOT_93⟧.

**ZH** 其中 ⟦SLOT_88⟧，且 ⟦SLOT_89⟧。以 PARA 数据库为例，⟦SLOT_90⟧ 且 ⟦SLOT_91⟧；而对 LAPIS 数据集，⟦SLOT_92⟧ 且 ⟦SLOT_93⟧。

**EN** Models. In this work, we investigate a diverse set of models, including InternVL2.5 (1B, 2B, 4B, 8B, 26B, 38B) Chen et al. (2024b); Chen et al. (2024c); Chen et al. (2024d), Qwen2.5-VL (3B, 7B) Yang et al. (2024), LLaVA-v1.5 (7B) Liu et al. (2023b), LLaVA-v1.6-vicuna (7B) Liu et al. (2023a), Llama-3.2-Vision (11B) Grattafiori et al. (2024), mPLUG-Owl3 (7B) Ye et al. (2024), Mono-InternVL (2B) Luo et al. (2024), Phi-3.5-Vision (4B) Abdin et al. (2024), GLM-4V (9B) GLM et al. (2024), and DeepSeek-VL2 (7B) Wu et al. (2024b). We also include closed-source models such as Claude-3.5-Sonnet, Gemini-2.0-flash, and GPT-4o in our analysis. This selection enables systematic evaluation of biases across architectures and scales. With this setup, we can compare bias variations within a model series across sizes and between models of similar sizes. These comparisons provide insights into how architecture, scale, and training paradigms influence bias.

**ZH** 模型。本工作考察一组多样的模型，包括 InternVL2.5（1B、2B、4B、8B、26B、38B）Chen 等（2024b）；Chen 等（2024c）；Chen 等（2024d）、Qwen2.5-VL（3B、7B）Yang 等（2024）、LLaVA-v1.5（7B）Liu 等（2023b）、LLaVA-v1.6-vicuna（7B）Liu 等（2023a）、Llama-3.2-Vision（11B）Grattafiori 等（2024）、mPLUG-Owl3（7B）Ye 等（2024）、Mono-InternVL（2B）Luo 等（2024）、Phi-3.5-Vision（4B）Abdin 等（2024）、GLM-4V（9B）GLM 等（2024）与 DeepSeek-VL2（7B）Wu 等（2024b）。分析中还纳入了 Claude-3.5-Sonnet、Gemini-2.0-flash 与 GPT-4o 等闭源模型。这一选择使我们能够系统评估跨架构与跨规模的偏见。借助这一设置，我们可以在同一模型系列内跨规模比较偏见变化，也可以在规模相近的模型之间比较。这些比较为架构、规模与训练范式如何影响偏见提供了洞见。

<!-- [原子块 · object]  -->

**EN** Figure 5: AAS of the model on three tasks without identity information, showing the two most common identity patterns for each task. ⟦SLOT_94⟧, ⟦SLOT_95⟧, and ⟦SLOT_96⟧ represent groups by gender, age, and education, respectively.

**ZH** 图 5：模型在无身份信息时三项任务上的 AAS，展示每项任务最常见的两种身份模式。⟦SLOT_94⟧、⟦SLOT_95⟧ 与 ⟦SLOT_96⟧ 分别表示按性别、年龄与教育划分的组。

**EN** 4.2 Stereotype Bias Analysis

**ZH** 4.2 刻板印象偏见分析

**EN** 4.2.1 Existence of Bias in MLLMs

**ZH** 4.2.1 MLLM 中偏见的存在性

**EN** We quantify stereotype bias in MLLMs performing PIAA using two metrics: Identity Fairness Deviation (IFD) and Normalized Response Deviation (NRD). The heatmap in Figure 3 shows the IFD scores across multiple models, indicating substantial identity-related biases, where higher IFD values reflect stronger bias. Among these, the InternVL2.5 model series consistently shows lower IFD values, suggesting better fairness across demographic identities.

**ZH** 我们用两个指标量化 MLLM 在执行 PIAA 时的刻板印象偏见：身份公平性偏差（IFD）与归一化响应偏差（NRD）。图 3 中的热力图展示了多个模型的 IFD 分数，表明存在大量与身份相关的偏见，IFD 值越高反映偏见越强。其中，InternVL2.5 模型系列一致表现出较低的 IFD 值，说明其跨人口身份的公平性更好。

**EN** Additionally, Figure 4 (left) illustrates NRD scores, confirming strong biases, particularly evident in empathy-driven aesthetic tasks. Gender is consistently identified as a major influencing factor, with notably higher NRD scores across all evaluated models. This emphasizes significant differences in the emotional perception of images among different demographic groups.

**ZH** 此外，图 4（左）展示了 NRD 分数，证实了强烈的偏见，在共情驱动的美学任务中尤为明显。性别始终被识别为主要影响因素，在所有受评模型上 NRD 分数都明显更高。这凸显了不同人口群体在图像情感感知上的显著差异。

**EN** To further illustrate this, Figure 4 right provides a detailed example using Claude-3.5-Sonnet in the empathy task. The model predicts that younger individuals, those with lower educational attainment, and females are more likely to exhibit fear responses. These results suggest that advanced models encode systematic differences across demographic groups in emotional aesthetic judgment, reinforcing the presence of subtle yet persistent stereotypical biases in MLLMs.

**ZH** 为进一步说明，图 4 右给出了一个用 Claude-3.5-Sonnet 在共情任务上的详细示例。该模型预测更年轻、教育程度更低以及女性群体更可能表现出恐惧反应。这些结果表明，先进模型在情感美学判断中对不同人口群体编码了系统性差异，强化了 MLLM 中细微却持续的刻板印象偏见的存在。

**EN** 4.2.2 Impact of Model Size on Bias

**ZH** 4.2.2 模型规模对偏见的影响

**EN** The radar chart in Figure 3 right shows the IFD scores across the InternVL2.5 series. The results reveal a clear inverse relationship between model size and stereotype bias: as the model size increases from 1B to 38B, the IFD scores consistently decrease. InternVL2.5-1B shows the highest level of bias, followed by 2B, 4B, and 8B, with each larger model displaying progressively lower bias. The largest models, 26B and 38B, yield the most stable and fair outputs. This trend indicates that identity-related bias decreases consistently with increasing model size.

**ZH** 图 3 右的雷达图展示了 InternVL2.5 系列各模型的 IFD 分数。结果揭示了模型规模与刻板印象偏见之间清晰的反向关系：随着模型规模从 1B 增至 38B，IFD 分数持续下降。InternVL2.5-1B 的偏见水平最高，其后依次是 2B、4B 与 8B，更大的模型偏见逐步降低。最大的两个模型 26B 与 38B 产出最稳定、最公平的输出。这一趋势表明，与身份相关的偏见随模型规模增大而持续下降。

**EN** This pattern is not limited to the InternVL2.5 series. Similar trends are observed in other model families, where smaller variants consistently exhibit higher IFD scores than their larger counterparts, indicating stronger stereotype bias. While this may appear to reflect the effect of model capacity alone, it is likely influenced by differences in training data scale and diversity as well. Larger models are often trained on broader and more balanced datasets, which may provide better coverage of identity-related variations and contribute to more equitable outputs.

**ZH** 这一模式并不局限于 InternVL2.5 系列。在其他模型族中也观察到类似趋势：较小的变体一致表现出比同族更大变体更高的 IFD 分数，说明刻板印象偏见更强。虽然这看似只反映模型容量的作用，但它很可能也受到训练数据规模与多样性差异的影响。更大的模型往往在更广泛、更均衡的数据集上训练，这可能为身份相关的变化提供更好的覆盖，从而促成更公平的输出。

<!-- [原子块 · object]  -->

**EN** Figure 6: AAS of the model on three tasks with identity information, showing the two most common identity patterns for each task. ⟦SLOT_97⟧, ⟦SLOT_98⟧, and ⟦SLOT_99⟧ represent groups by gender, age, and education, respectively.

**ZH** 图 6：模型在带身份信息时三项任务上的 AAS，展示每项任务最常见的两种身份模式。⟦SLOT_97⟧、⟦SLOT_98⟧ 与 ⟦SLOT_99⟧ 分别表示按性别、年龄与教育划分的组。

**EN** 4.3 Aesthetic Alignment Analysis

**ZH** 4.3 美学对齐分析

**EN** 4.3.1 Default Aesthetic Preferences of Models

**ZH** 4.3.1 模型的默认美学偏好

**EN** We begin by analyzing the default aesthetic alignment of MLLMs when no identity information is provided in the prompt. Using the Aesthetic Alignment Score (AAS), we measure the similarity between model outputs and the aesthetic preferences of different demographic groups across the three tasks.

**ZH** 我们首先分析在提示中未提供身份信息时 MLLM 的默认美学对齐。借助美学对齐分数（AAS），我们度量三项任务上模型输出与不同人口群体美学偏好之间的相似性。

**EN** The heatmap and radar plots in Figure 5 and summary statistics in Table 1 reveal clear and consistent demographic biases across tasks. All three tasks show a strong alignment with female aesthetic preferences, with 17 out of 19 models exhibiting this pattern. In terms of age, the 22–25 group dominates in Perception and Assessment, while Empathy shows a shift toward the younger 18–21 group. Educational alignment is more task-specific. The most consistent pattern appears in the Assessment task, where nearly all models align with the same group: female, aged 22–25, with a university education.

**ZH** 图 5 中的热力图与雷达图以及表 1 的汇总统计，揭示了跨任务清晰且一致的人口偏见。三项任务都表现出与女性美学偏好的强对齐，19 个模型中有 17 个呈现这一模式。在年龄方面，22–25 组在感知与评估中占主导，而共情则转向更年轻的 18–21 组。教育方面的对齐更具任务特异性。最一致的模式出现在评估任务中：几乎所有模型都与同一群体对齐——女性、22–25 岁、受过大学教育。

**EN** Task-specific patterns also emerge. As shown in Figure 5, the points in the radar plot for the Empathy task are more tightly clustered, indicating that the AAS values are generally lower compared to the other tasks. This aligns with the observation in Figure 3, where the Empathy task also exhibits lower IFD values. Together, these results show that the default models are fairer in the Empathy task and exhibit weaker alignment with human aesthetic preferences.

**ZH** 任务特异性模式也随之浮现。如图 5 所示，共情任务在雷达图上的点更为聚集，说明其 AAS 值总体低于其他任务。这与图 3 中的观察一致：共情任务的 IFD 值也更低。综合来看，这些结果表明默认模型在共情任务上更公平，且与人类美学偏好的对齐更弱。

<!-- [原子块 · table] Perception Assessment Empathy Gender female (17) female (17) female (17) Age 22_25 (12) 22_25 (17) 18_21 (8) Education Tech (7) University (17) Junior (7) -->

**EN** Table 1: The number of models exhibiting the highest AAS with different demographic groups across three tasks. The table summarizes results from 19 models.

**ZH** 表 1：在三项任务上与不同人口群体取得最高 AAS 的模型数量。该表汇总了 19 个模型的结果。

**EN** 4.3.2 Sensitivity to Identity in Aesthetic Preferences

**ZH** 4.3.2 美学偏好对身份的敏感性

**EN** To further examine how identity information influences aesthetic alignment, we analyze the consistency of identity patterns across tasks after explicitly including demographic attributes in the prompts.

**ZH** 为进一步考察身份信息如何影响美学对齐，我们分析在提示中显式加入人口属性之后，各任务上身份模式的一致性。

<!-- [原子块 · table] Perception Assessment Empathy Gender female (15) female (14) male (17) Age 22_25 (10) 22_25 (15) 30_34 (8) Education Junior (7) University (10) University (6) -->

**EN** Table 2: The number of models exhibiting the highest AAS with different demographic groups across three tasks when explicit identity attributes are provided. The table summarizes results from 19 models.

**ZH** 表 2：在显式提供身份属性时，三项任务上与不同人口群体取得最高 AAS 的模型数量。该表汇总了 19 个模型的结果。

**EN** As shown in Figure 6 and summary statistics in Table 2, adding explicit identity information reduces the number of models that share the same dominant aesthetic pattern. This shift reflects that model outputs are sensitive to demographic descriptors, indicating the absence of neutral or identity-invariant behavior. It indicates that aesthetic outputs are systematically influenced by identity descriptors, revealing latent social biases in the models.

**ZH** 如图 6 与表 2 的汇总统计所示，加入显式身份信息后，共享同一主导美学模式的模型数量减少。这一变化反映出模型输出对人口描述词敏感，说明不存在中立或身份不变的行为。它表明美学输出被身份描述词系统性地影响，揭示了模型中潜在的社会偏见。

**EN** In particular, Table 2 shows a striking shift in the Empathy task: 17 models align with male identities, which is a complete reversal from the identity-agnostic setting, where 17 models had aligned with female. Table 3 illustrates this bias sensitivity, showing increased alignment with male preferences when gender is added.

**ZH** 特别地，表 2 显示共情任务出现了显著转向：17 个模型与男性身份对齐，这与身份无关设置下 17 个模型与女性对齐形成了完全反转。表 3 说明了这种偏见敏感性，展示了加入性别后与男性偏好的对齐增强。

<!-- [原子块 · table] Model Δ \Delta S E S_{E} (M) Δ \Delta S E S_{E} (F) Δ \Delta GPT-4o 0.0395 -0.0748 0.1143 Claude-3.5-Sonnet 0.1180 -0.1166 0.2346 Gemini-2.0-Flash 0.0274 -0.3780 0.4054 DeepSeek-VL2 -0.0535 -0.0749 0. -->

**EN** Table 3: ⟦SLOT_100⟧(M) and ⟦SLOT_101⟧(F) denote the changes in similarity scores between the model outputs and the aggregated aesthetic preferences of male and female annotators, respectively, when comparing prompts without and with gender identity in the empathy task. ⟦SLOT_102⟧ represents the incremental gain of male over female, computed as ⟦SLOT_103⟧(M) ⟦SLOT_104⟧ ⟦SLOT_105⟧(F). The top 3 highest and lowest ⟦SLOT_106⟧ values are highlighted using soft red and blue gradients.

**ZH** 表 3：⟦SLOT_100⟧(M) 与 ⟦SLOT_101⟧(F) 分别表示在共情任务中，比较不带与带性别身份的提示时，模型输出与男性、女性标注者聚合美学偏好之间相似度分数的变化。⟦SLOT_102⟧ 表示男性相对女性的增量增益，按 ⟦SLOT_103⟧(M) ⟦SLOT_104⟧ ⟦SLOT_105⟧(F) 计算。最高与最低的三个 ⟦SLOT_106⟧ 值分别用柔和的红色与蓝色渐变标出。

**EN** As shown in Table 3, most models show a greater increase in similarity to male preferences after gender is specified, indicating higher sensitivity to male identity. Instead of exposing more balanced behavior, the inclusion of gender information reveals stronger model bias, with responses becoming more aligned to male-associated aesthetic patterns—a deviation possibly reflecting differences in training data composition or architectural design.

**ZH** 如表 3 所示，多数模型在指定性别之后与男性偏好的相似度提升更大，说明对男性身份的敏感性更高。加入性别信息并未带来更均衡的行为，反而暴露出更强的模型偏见——回应变得更贴合与男性相关的美学模式，这一偏离可能反映了训练数据构成或架构设计上的差异。

**EN** 5 Conclusion

**ZH** 5 结论

**EN** This paper introduced AesBiasBench, a benchmark for evaluating biases in MLLMs on PIAA tasks. To quantify stereotype bias, we proposed two metrics: IFD and NRD. In addition, we used the AAS to measure how model outputs correspond to human aesthetic preferences across demographic groups. Key findings include: (1) Stereotype bias is prevalent across models, with smaller models showing more pronounced deviations and larger models exhibiting lower IFD and NRD scores, indicating increased fairness with scale. (2) Model outputs align disproportionately with certain demographic groups, notably, female individuals aged 22–25 with a university education, even when identity information is not provided. (3) Adding identity descriptors amplifies existing biases, as shown in the empathy task where alignment shifts more strongly toward male preferences, revealing heightened sensitivity to demographic cues rather than neutrality. These results highlight the importance of identity-aware evaluation and point to the need for fairness-oriented design in future MLLMs used for subjective and socially-influenced tasks.

**ZH** 本文提出 AesBiasBench，一个用于评估 MLLM 在 PIAA 任务上偏见的基准。为量化刻板印象偏见，我们提出两个指标：IFD 与 NRD。此外，我们用 AAS 度量模型输出在跨人口群体上与人类美学偏好的对应程度。主要发现包括：(1) 刻板印象偏见在各模型中普遍存在，较小的模型偏差更明显，而较大的模型 IFD 与 NRD 分数更低，说明公平性随规模提升。(2) 模型输出不成比例地与某些人口群体对齐，尤其是 22–25 岁、受过大学教育的女性个体，即便未提供身份信息也是如此。(3) 加入身份描述词会放大既有偏见，如共情任务中对齐更强地转向男性偏好所示，这揭示的是对人口线索的高度敏感，而非中立。这些结果凸显了身份感知评估的重要性，并指出未来用于主观且受社会影响任务的 MLLM 需要面向公平性的设计。

**EN** 6 Discussion

**ZH** 6 讨论

**EN** Our focus is to benchmark and identify bias, which could lead to actionable mitigation. The proposed metrics (IFD, NRD, AAS) offer a structured way to quantify which demographic groups are favored or underrepresented. With known bias direction and magnitude, targeted strategies can be applied, which make the mitigation process efficient and transparent. Here we introduce several mitigation strategies

**ZH** 我们的重心是对偏见做基准评测与识别，从而促成可操作的缓解。所提出的指标（IFD、NRD、AAS）提供了一种结构化方式，量化哪些人口群体受到偏好或代表性不足。在已知偏见方向与量级的前提下，可以施加有针对性的策略，使缓解过程高效且透明。下面我们介绍若干缓解策略。

**EN** The first is concept editing, which adjusts model representations to weaken associations between aesthetic preferences and demographic attributes Yao et al. (2023). Known bias direction could help us determine which concept we should edit. Another approach is data re-balancing Maudslay et al. (2019), where training data is reweighted or augmented to achieve more equitable demographic representation. For instance, as shown in Figure 4 (right), the model associates the emotion “fear” more strongly with female, junior-high-educated, and younger individuals, suggesting a demographic-specific bias. Balancing the dataset in this context could involve enriching underrepresented groups in the “fear” category to counteract skewed associations. In addition, fairness-aware post-training Yang et al. (2023) can be applied using regularization terms informed by our metrics. These techniques aim to reduce representational disparities while preserving core model capabilities.

**ZH** 第一种是概念编辑，即调整模型表示以弱化美学偏好与人口属性之间的关联 Yao 等（2023）。已知的偏见方向可帮助我们确定应编辑哪个概念。另一种途径是数据再平衡 Maudslay 等（2019），即对训练数据重新加权或增广，以实现更公平的人口代表性。例如，如图 4（右）所示，模型把「恐惧」这一情感更强烈地与女性、初中教育程度以及更年轻的人关联起来，提示存在特定于人口群体的偏见。在此情境下做数据平衡，可以是丰富「恐惧」类别中代表性不足的群体，以抵消偏斜的关联。此外，还可以应用公平性感知的后训练 Yang 等（2023），使用由我们的指标指导的正则化项。这些技术旨在减少表征上的差异，同时保留模型的核心能力。

**EN** However, in some application contexts, we may indeed want models to behave differently for different demographic groups. For example, personalization is desired for a recommendation system. Alignment with group-specific preferences is necessary. Our benchmark’s AAS metric is designed to evaluate the degree of alignment between model outputs and human preferences. The fairness and alignment is dual-used and need to be considered together depending on the downstream use case.

**ZH** 然而，在某些应用场景中，我们可能确实希望模型对不同人口群体有不同表现。例如，推荐系统就希望有个性化。与群体专属偏好对齐是必要的。本基准的 AAS 指标正是为评估模型输出与人类偏好的对齐程度而设计的。公平性与对齐具有双重用途，需要根据下游用例一并考量。

**EN** Limitations

**ZH** 局限性

**EN** Our AesBiasBench evluates existing MLLMs along two complementary axes: (1) stereotype bias and (2) human preference alignment. To make the results more reliable, we indentify two possible limitations:

**ZH** 我们的 AesBiasBench 沿两个互补的轴线评估现有 MLLM：(1) 刻板印象偏见；(2) 人类偏好对齐。为使结果更可靠，我们指出两点可能的局限：

**EN** First, the analysis is restricted to three identity attributes: age, gender, and education. While these dimensions capture important aspects of demographic variation, other factors, such as culture, race, and religion, may also influence aesthetic preferences and model behavior. Incorporating a broader range of identity dimensions could enable a more comprehensive understanding of demographic bias in MLLMs.

**ZH** 第一，分析限定在年龄、性别与教育三个身份属性上。虽然这些维度捕捉了人口差异的重要方面，文化、种族与宗教等其他因素也可能影响美学偏好与模型行为。纳入更广的身份维度，可以更全面地理解 MLLM 中的人口偏见。

**EN** Second, we evaluate 19 MLLMs, including proprietary models (e.g., GPT-4o, Claude-3.5-Sonnet) and open-source models (e.g., InternVL2.5 and Qwen2.5-VL series). While this selection spans a range of model families and sizes, future work could explore a broader set of architectures, training strategies, and deployment contexts, which may reveal additional forms of bias or alternative alignment.

**ZH** 第二，我们评估了 19 个 MLLM，包括专有模型（如 GPT-4o、Claude-3.5-Sonnet）与开源模型（如 InternVL2.5 与 Qwen2.5-VL 系列）。虽然这一选择横跨多种模型族与规模，未来工作可以探索更广泛的架构、训练策略与部署语境，这可能揭示更多形式的偏见或替代性的对齐模式。

**EN** Ethics

**ZH** 伦理

**EN** In this study, we constructed AesBiasBench using the publicly accessible Personalized Image Aesthetics Database with Rich Attributes (PARA). No original data collection was conducted; all analyses relied solely on pre-existing dataset resources. To the best of our knowledge, the PARA dataset was developed in strict adherence to academic and scientific data collection protocols, ensuring compliance with ethical standards for research involving human subjects.

**ZH** 本研究使用可公开获取的带有丰富属性的个性化图像美学数据库（PARA）构建 AesBiasBench。我们未开展任何原始数据收集，所有分析仅依赖已有的数据集资源。据我们所知，PARA 数据集的构建严格遵循学术与科学的数据采集规范，确保符合涉及人类受试者研究的伦理标准。

**EN** Our research does not involve any personally identifiable information (PII) or process private/sensitive user data. The demographic attributes utilized (e.g., age groups, gender, education levels) are provided in the PARA dataset as anonymized and aggregated metadata, with no individual-level data accessible. This design ensures that no participant can be re-identified through the study’s analyses.

**ZH** 本研究不涉及任何个人身份信息（PII），也不处理私密或敏感的用户数据。所使用的人口属性（如年龄段、性别、教育水平）在 PARA 数据集中以匿名化、聚合的元数据形式提供，无法获取个体层面的数据。这一设计确保任何参与者都无法通过本研究的分析被重新识别。

**EN** The core objective of this research is to systematically uncover and characterize biased behaviors of multimodal large language models (MLLMs) in personalized aesthetic judgment tasks. By quantifying demographic disparities in model outputs, we aim to foster greater awareness within the research community and contribute to the development of more equitable, transparent, and socially accountable AI systems. Our work aligns with the broader ethical imperative to promote fairness in machine learning, particularly in applications impacting human values and societal norms.

**ZH** 本研究的核心目标是系统揭示并刻画多模态大语言模型（MLLM）在个性化美学判断任务中的偏见行为。通过量化模型输出中的人口差异，我们希望在研究社区内提升意识，并助力构建更公平、透明、具有社会问责性的 AI 系统。本工作契合在机器学习中促进公平性这一更广泛的伦理要求，尤其是在影响人类价值与社会规范的应用中。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] Abdin et al. (2024) Marah Abdin, Jyoti Aneja, Hany Awadalla, Ahmed Awadallah, Ammar Ahmad Awan, Nguyen Bach, Amit Bahree, Arash Bakhtiari, Jianmin Bao, Harkirat Behl, and 1 others. 2024. Phi-3 technic -->

<!-- [原子块 · verbatim] Achiam et al. (2023) Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, and 1 others. 2023. G -->

<!-- [原子块 · verbatim] Alayrac et al. (2022) Jean-Baptiste Alayrac, Jeff Donahue, Pauline Luc, Antoine Miech, Iain Barr, Yana Hasson, Karel Lenc, Arthur Mensch, Katherine Millican, Malcolm Reynolds, and 1 others. 2022. Flam -->

<!-- [原子块 · verbatim] Bai et al. (2024) Xuechunzi Bai, Angelina Wang, Ilia Sucholutsky, and Thomas L Griffiths. 2024. Measuring implicit bias in explicitly unbiased large language models. arXiv preprint arXiv:2402.04105 . -->

<!-- [原子块 · verbatim] Chen et al. (2024a) Dongping Chen, Ruoxi Chen, Shilin Zhang, Yinuo Liu, Yaochen Wang, Huichi Zhou, Qihui Zhang, Yao Wan, Pan Zhou, and Lichao Sun. 2024a. Mllm-as-a-judge: Assessing multimodal llm-as-a -->

<!-- [原子块 · verbatim] Chen et al. (2024b) Zhe Chen, Weiyun Wang, Yue Cao, Yangzhou Liu, Zhangwei Gao, Erfei Cui, Jinguo Zhu, Shenglong Ye, Hao Tian, Zhaoyang Liu, and 1 others. 2024b. Expanding performance boundaries of op -->

<!-- [原子块 · verbatim] Chen et al. (2024c) Zhe Chen, Weiyun Wang, Hao Tian, Shenglong Ye, Zhangwei Gao, Erfei Cui, Wenwen Tong, Kongzhi Hu, Jiapeng Luo, Zheng Ma, and 1 others. 2024c. How far are we to gpt-4v? closing the g -->

<!-- [原子块 · verbatim] Chen et al. (2024d) Zhe Chen, Jiannan Wu, Wenhai Wang, Weijie Su, Guo Chen, Sen Xing, Muyan Zhong, Qinglong Zhang, Xizhou Zhu, Lewei Lu, and 1 others. 2024d. Internvl: Scaling up vision foundation mod -->

<!-- [原子块 · verbatim] Cui et al. (2020) Chaoran Cui, Wenya Yang, Cheng Shi, Meng Wang, Xiushan Nie, and Yilong Yin. 2020. Personalized image quality assessment with social-sensed aesthetic preference. Information Sciences  -->

<!-- [原子块 · verbatim] Deng et al. (2017) Yubin Deng, Chen Change Loy, and Xiaoou Tang. 2017. Image aesthetic assessment: An experimental survey. IEEE Signal Processing Magazine , 34(4):80–106. -->

<!-- [原子块 · verbatim] Dhamala et al. (2021) J Dhamala, T Sun, V Kumar, S Krishna, Y Pruksachatkun, K-W Chang, and R Gupta. 2021. Bold: Dataset and metrics for measuring biases in open-ended language generation. In Proceedi -->

<!-- [原子块 · verbatim] Dhar et al. (2011) Sagnik Dhar, Vicente Ordonez, and Tamara L Berg. 2011. High level describable attributes for predicting aesthetics and interestingness. In CVPR 2011 , pages 1657–1664. IEEE. -->

<!-- [原子块 · verbatim] Dige et al. (2024) Omkar Dige, Diljot Singh, Tsz Fung Yau, Qixuan Zhang, Borna Bolandraftar, Xiaodan Zhu, and Faiza Khan Khattak. 2024. Mitigating social biases in language models through unlearning.  -->

<!-- [原子块 · verbatim] Gallegos et al. (2024) Isabel O Gallegos, Ryan A Rossi, Joe Barrow, Md Mehrab Tanjim, Sungchul Kim, Franck Dernoncourt, Tong Yu, Ruiyi Zhang, and Nesreen K Ahmed. 2024. Bias and fairness in large lang -->

<!-- [原子块 · verbatim] GLM et al. (2024) Team GLM, Aohan Zeng, Bin Xu, Bowen Wang, Chenhui Zhang, Da Yin, Diego Rojas, Guanyu Feng, Hanlin Zhao, Hanyu Lai, Hao Yu, Hongning Wang, Jiadai Sun, Jiajie Zhang, Jiale Cheng, Jiayi -->

<!-- [原子块 · verbatim] Grattafiori et al. (2024) Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Alex Vaughan, and 1 others. 2 -->

<!-- [原子块 · verbatim] Guo et al. (2022) Yue Guo, Yi Yang, and Ahmed Abbasi. 2022. Auto-debias: Debiasing masked language models with automated biased prompts. In Proceedings of the 60th Annual Meeting of the Association fo -->

<!-- [原子块 · verbatim] Hou et al. (2022) Jingwen Hou, Weisi Lin, Guanghui Yue, Weide Liu, and Baoquan Zhao. 2022. Interaction-matrix based personalized image aesthetics assessment. IEEE Transactions on Multimedia , 25:5263– -->

<!-- [原子块 · verbatim] Huang et al. (2024a) Yipo Huang, Xiangfei Sheng, Zhichao Yang, Quan Yuan, Zhichao Duan, Pengfei Chen, Leida Li, Weisi Lin, and Guangming Shi. 2024a. Aesexpert: Towards multi-modality foundation model  -->

<!-- [原子块 · verbatim] Huang et al. (2024b) Yipo Huang, Quan Yuan, Xiangfei Sheng, Zhichao Yang, Haoning Wu, Pengfei Chen, Yuzhe Yang, Leida Li, and Weisi Lin. 2024b. Aesbench: An expert benchmark for multimodal large langu -->

<!-- [原子块 · verbatim] Jiang et al. (2024) Yukun Jiang, Zheng Li, Xinyue Shen, Yugeng Liu, Michael Backes, and Yang Zhang. 2024. Modscan: Measuring stereotypical bias in large vision-language models from vision and language -->

<!-- [原子块 · verbatim] Kumar et al. (2024) Abhishek Kumar, Sarfaroz Yunusov, and Ali Emami. 2024. Subtle biases need subtler measures: Dual metrics for evaluating representative and affinity bias in large language models. a -->

<!-- [原子块 · verbatim] Li et al. (2024a) Cheng Li, Mengzhuo Chen, Jindong Wang, Sunayana Sitaram, and Xing Xie. 2024a. Culturellm: Incorporating cultural differences into large language models. arXiv preprint arXiv:2402.109 -->

<!-- [原子块 · verbatim] Li et al. (2024b) Cheng Li, Damien Teney, Linyi Yang, Jindong Wang, Qingsong Wen, Xing Xie, and Jindong Wang. 2024b. Culturepark: Boosting cross - cultural understanding in large language models. arXi -->

<!-- [原子块 · verbatim] Li et al. (2025) Weiqi Li, Xuanyu Zhang, Shijie Zhao, Yabin Zhang, Junlin Li, Li Zhang, and Jian Zhang. 2025. Q-insight: Understanding image quality via visual reinforcement learning. arXiv preprint a -->

<!-- [原子块 · verbatim] Lin et al. (2024) Luyang Lin, Lingzhi Wang, Jinsong Guo, and Kam-Fai Wong. 2024. Investigating bias in llm-based bias detection: Disparities between llms and human perception. arXiv preprint arXiv:240 -->

<!-- [原子块 · verbatim] Liu et al. (2023a) Haotian Liu, Chunyuan Li, Yuheng Li, and Yong Jae Lee. 2023a. Improved baselines with visual instruction tuning. -->

<!-- [原子块 · verbatim] Liu et al. (2023b) Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. 2023b. Visual instruction tuning. In NeurIPS . -->

<!-- [原子块 · verbatim] Luo et al. (2024) Gen Luo, Xue Yang, Wenhan Dou, Zhaokai Wang, Jiawen Liu, Jifeng Dai, Yu Qiao, and Xizhou Zhu. 2024. Mono-internvl: Pushing the boundaries of monolithic multimodal large language mode -->

<!-- [原子块 · verbatim] Maerten et al. (2025) Anne-Sofie Maerten, Li-Wei Chen, Stefanie De Winter, Christophe Bossens, and Johan Wagemans. 2025. Lapis: A novel dataset for personalized image aesthetic assessment. In Proceedi -->

<!-- [原子块 · verbatim] Maudslay et al. (2019) Rowan Hall Maudslay, Hila Gonen, Ryan Cotterell, and Simone Teufel. 2019. It’s all in the name: mitigating gender bias with name-based counterfactual data substitution. arXiv pr -->

<!-- [原子块 · verbatim] Murray et al. (2012) Naila Murray, Luca Marchesotti, and Florent Perronnin. 2012. Ava: A large-scale database for aesthetic visual analysis. In 2012 IEEE conference on computer vision and pattern reco -->

<!-- [原子块 · verbatim] Naous et al. (2023) Tarek Naous, Michael J Ryan, Alan Ritter, and Wei Xu. 2023. Having beer after prayer? measuring cultural bias in large language models. arXiv preprint arXiv:2305.14456 . -->

<!-- [原子块 · verbatim] Ren et al. (2017) Jian Ren, Xiaohui Shen, Zhe Lin, Radomir Mech, and David J Foran. 2017. Personalized image aesthetics. In Proceedings of the IEEE international conference on computer vision , pages  -->

<!-- [原子块 · verbatim] Smith et al. (2023) Brandon Smith, Miguel Farinha, Siobhan Mackenzie Hall, Hannah Rose Kirk, Aleksandar Shtedritski, and Max Bain. 2023. Balancing the picture: Debiasing vision-language datasets with  -->

<!-- [原子块 · verbatim] Tamkin et al. (2023) A Tamkin, A Askell, L Lovitt, E Durmus, N Joseph, S Kravec, K Nguyen, J Kaplan, and D Ganguli. 2023. Evaluating and mitigating discrimination in language model decisions. arXiv pr -->

<!-- [原子块 · verbatim] Tjuatja et al. (2023) Lindia Tjuatja, Valerie Chen, Sherry Tongshuang Wu, Ameet Talwalkar, and Graham Neubig. 2023. Do llms exhibit human-like response biases? a case study in survey design. arXiv pre -->

<!-- [原子块 · verbatim] Wu et al. (2024a) Haoning Wu, Zicheng Zhang, Erli Zhang, Chaofeng Chen, Liang Liao, Annan Wang, Kaixin Xu, Chunyi Li, Jingwen Hou, Guangtao Zhai, and 1 others. 2024a. Q-instruct: Improving low-level v -->

<!-- [原子块 · verbatim] Wu et al. (2023) Haoning Wu, Zicheng Zhang, Weixia Zhang, Chaofeng Chen, Liang Liao, Chunyi Li, Yixuan Gao, Annan Wang, Erli Zhang, Wenxiu Sun, and 1 others. 2023. Q-align: Teaching lmms for visual sc -->

<!-- [原子块 · verbatim] Wu et al. (2025) Mengyang Wu, Yuzhi Zhao, Jialun Cao, Mingjie Xu, Zhongming Jiang, Xuehui Wang, Qinbin Li, Guangneng Hu, Shengchao Qin, and Chi-Wing Fu. 2025. Icm-assistant: instruction-tuning multimo -->

<!-- [原子块 · verbatim] Wu et al. (2024b) Zhiyu Wu, Xiaokang Chen, Zizheng Pan, Xingchao Liu, Wen Liu, Damai Dai, Huazuo Gao, Yiyang Ma, Chengyue Wu, Bingxuan Wang, and 1 others. 2024b. Deepseek-vl2: Mixture-of-experts visio -->

<!-- [原子块 · verbatim] Xu et al. (2025) Mingjie Xu, Mengyang Wu, Yuzhi Zhao, Jason Chun Lok Li, and Weifeng Ou. 2025. Llava-spacesgg: Visual instruct tuning for open-vocabulary scene graph generation with enhanced spatial r -->

<!-- [原子块 · verbatim] Yang et al. (2024) An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan Li, Dayiheng Liu, Fei Huang, Haoran Wei, Huan Lin, Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin Ya -->

<!-- [原子块 · verbatim] Yang et al. (2023) Ke Yang, Charles Yu, Yi R Fung, Manling Li, and Heng Ji. 2023. Adept: A debiasing prompt framework. In Proceedings of the AAAI conference on artificial intelligence , volume 37, pag -->

<!-- [原子块 · verbatim] Yang et al. (2022) Yuzhe Yang, Liwu Xu, Leida Li, Nan Qie, Yaqian Li, Peng Zhang, and Yandong Guo. 2022. Personalized image aesthetics assessment with rich attributes. In Proceedings of the IEEE/CVF C -->

<!-- [原子块 · verbatim] Yao et al. (2023) Yunzhi Yao, Peng Wang, Bozhong Tian, Siyuan Cheng, Zhoubo Li, Shumin Deng, Huajun Chen, and Ningyu Zhang. 2023. Editing large language models: Problems, methods, and opportunities. a -->

<!-- [原子块 · verbatim] Ye et al. (2024) Jiabo Ye, Haiyang Xu, Haowei Liu, Anwen Hu, Ming Yan, Qi Qian, Ji Zhang, Fei Huang, and Jingren Zhou. 2024. mplug-owl3: Towards long image-sequence understanding in multi-modal large  -->

<!-- [原子块 · verbatim] Yi et al. (2023) Ran Yi, Haoyuan Tian, Zhihao Gu, Yu-Kun Lai, and Paul L Rosin. 2023. Towards artistic image aesthetics assessment: a large-scale dataset and a new method. In Proceedings of the IEEE/C -->

<!-- [原子块 · verbatim] Zangwill (2003) Nick Zangwill. 2003. Aesthetic judgment. -->

<!-- [原子块 · verbatim] Zhou et al. (2024) Zhaokun Zhou, Qiulin Wang, Bin Lin, Yiwei Su, Rui Chen, Xin Tao, Amin Zheng, Li Yuan, Pengfei Wan, and Di Zhang. 2024. Uniaa: A unified multi-modal image aesthetic assessment baseli -->

<!-- [原子块 · verbatim] Zhu et al. (2023) Deyao Zhu, Jun Chen, Xiaoqian Shen, Xiang Li, and Mohamed Elhoseiny. 2023. Minigpt-4: Enhancing vision-language understanding with advanced large language models. arXiv preprint arXi -->

<!-- [原子块 · verbatim] Zhu et al. (2020) Hancheng Zhu, Leida Li, Jinjian Wu, Sicheng Zhao, Guiguang Ding, and Guangming Shi. 2020. Personalized image aesthetics assessment via meta-learning with bilevel gradient optimizatio -->

**EN** Appendix A Prompt Description

**ZH** 附录 A 提示说明

**EN** We use a structured prompt design with two variants: a default version without demographic information and a personalized version that inserts the demographic cue at the opening clause (“As a [demographic], please …”). The task description and response format remain fixed across variants, so differences in outputs can be attributed to demographic conditioning rather than wording.

**ZH** 我们采用结构化的提示设计，包含两种变体：不含人口信息的默认版本，以及在句首插入人口线索的个性化版本（「作为一名[人口群体]，请……」）。两种变体的任务描述与回应格式保持固定，因此输出差异可归因于人口条件化，而非措辞差异。

**EN** For each image, we query one of three tasks.

**ZH** 对每张图像，我们查询三项任务之一。

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

**EN** The same textual structure and the same image input are used across models, tasks, and demographic conditions to ensure consistent evaluation. The default (non-personalized) version is obtained by removing the leading clause “As a [demographic], …” while keeping the rest unchanged.

**ZH** 各模型、任务与人口条件之间使用相同的文本结构与相同的图像输入，以保证评估的一致性。默认（非个性化）版本由删去句首小句「作为一名[人口群体]，……」而得，其余部分保持不变。

**EN** Appendix B Extended Evaluation

**ZH** 附录 B 扩展评估

**EN** Table 4: IFD and NRD values across models. InternVL-2.5 variants are grouped together, with Qwen2.5-VL-7B and Q-Insight shown separately. Note: For InternVL-2.5, the IFD score monotonically decreases as model size increases (2B ⟦SLOT_107⟧ 38B). Shading on the IFD row encodes magnitude (darker = larger).

**ZH** 表 4：各模型的 IFD 与 NRD 值。InternVL-2.5 的各变体归为一组，Qwen2.5-VL-7B 与 Q-Insight 单独列出。注：对 InternVL-2.5 而言，IFD 分数随模型规模增大单调下降（2B ⟦SLOT_107⟧ 38B）。IFD 行的阴影编码量级（越深越大）。

<!-- [原子块 · table] InternVL-2.5 Qwen2.5-VL-7B Q-Insight 2B 4B 8B 26B 38B IFD value 0.4651 0.4437 0.3560 0.2857 0.2020 1.1518 0.6160 NRD Age 0.530 0.154 0.076 0.126 0.336 0.566 0.503 Gender 0.648 0.303 0.318 0.225 0.468  -->

**EN** Table 5: Top-aligned demographic groups with corresponding AAS (in parentheses). InternVL-2.5 models are shown under one block, while Qwen2.5-VL-7B and Q-Insight are listed separately. Abbreviations: edu = education level {B = Bachelor, M = Master, D = Doctorate, P = Primary, S = Secondary}; geo = geographic region {EU = Europe, OC = Oceania}. The highest AAS in each row is highlighted in gray.

**ZH** 表 5：对齐度最高的人口群体及相应的 AAS（括号内）。InternVL-2.5 模型列于同一分组下，Qwen2.5-VL-7B 与 Q-Insight 单独列出。缩写：edu = 教育水平 {B = 学士, M = 硕士, D = 博士, P = 小学, S = 中学}；geo = 地理区域 {EU = 欧洲, OC = 大洋洲}。每行最高的 AAS 以灰色高亮。

<!-- [原子块 · table] InternVL-2.5 Qwen2.5-VL-7B Q-Insight 2B 4B 8B 26B 38B Default edu B (0.815) B (0.686) D (0.595) B (0.696) B (0.818) P (0.629) B (0.724) geo EU (0.760) EU (0.706) OC (0.638) EU (0.726) EU (0.838) OC (0 -->

**EN** We evaluate on diverse datasets to demonstrate the generalizability of our findings. We extended our evaluation beyond PARA to the Leuven Art Personalized Image Set Maerten et al. (2025) (LAPIS), a dataset of 11,723 artistic images rated on a 0–100 scale by an average of 24 annotators, with a total of 552 participants. LAPIS includes detailed demographic metadata such as age, gender, nationality, education, and art interest, enabling more fine-grained analysis under controlled conditions. We evaluated the proposed metrics IFD, NRD, and AAS on LAPIS using the following models: InternVL2.5 (2B, 4B, 8B, 26B, and 38B), Qwen2.5-VL (7B) and Q-insight Li et al. (2025), a new aesthetic model trained on Qwen2.5-VL (7B) using Group Relative Policy Optimization (GRPO), designed for score prediction and perceptual reasoning with improved generalization from limited annotations. In particular, experiments on LAPIS were conducted under the Aesthetic Assessment task.

**ZH** 我们在多样的数据集上评估，以证明本研究发现的泛化性。除 PARA 之外，我们把评估扩展到 Leuven 艺术个性化图像集 Maerten 等（2025）（LAPIS）：该数据集包含 11,723 张艺术图像，按 0–100 量表由平均 24 名标注者评分，参与者共 552 名。LAPIS 包含年龄、性别、国籍、教育与艺术兴趣等详尽的人口元数据，可在受控条件下做更细粒度的分析。我们在 LAPIS 上对 IFD、NRD 与 AAS 三个指标做了评估，所用模型包括：InternVL2.5（2B、4B、8B、26B 与 38B）、Qwen2.5-VL（7B）与 Q-insight Li 等（2025）——后者是一个在 Qwen2.5-VL（7B）上用组相对策略优化（GRPO）训练的新美学模型，面向分数预测与感知推理，能从有限的标注中获得更好的泛化。具体地，LAPIS 上的实验在美学评估任务下进行。

**EN** IFD. Results in Table 4 agree with PARA: within InternVL2.5, IFD decreases with model size (2B ⟦SLOT_108⟧ 38B). Qwen2.5-VL-7B has the highest IFD, indicating strong demographic skew. Q-Insight improves over its base model but still shows moderate bias.

**ZH** IFD。表 4 的结果与 PARA 一致：在 InternVL2.5 内部，IFD 随模型规模增大而下降（2B ⟦SLOT_108⟧ 38B）。Qwen2.5-VL-7B 的 IFD 最高，说明存在强烈的人口偏斜。Q-Insight 相较其基座模型有所改善，但仍表现出中等程度的偏见。

**EN** NRD. Table 4 also shows NRD by age, gender, geography, and education. The largest disparities are often on gender and age. Qwen2.5-VL-7B and Q-Insight yield higher NRD than most InternVL2.5 models, which indicates broader imbalance even for an aesthetic-focused model.

**ZH** NRD。表 4 还给出了按年龄、性别、地理与教育划分的 NRD。最大的差异往往出现在性别与年龄上。Qwen2.5-VL-7B 与 Q-Insight 的 NRD 高于多数 InternVL2.5 模型，这说明即便是一个以美学为核心的模型，也存在更广泛的不平衡。

**EN** AAS. Table 5 summarizes alignment. Without identity in the prompt, models most often align with users holding a bachelor’s degree and from Europe. Adding identity produces small shifts (for example, some cases move to master’s or to Oceania), but the same dominant groups remain. These outcomes match the trends observed on PARA and show that the findings generalize across datasets and model variants.

**ZH** AAS。表 5 汇总了对齐情况。在不带身份的提示下，模型最常与拥有学士学位、来自欧洲的用户对齐。加入身份会带来小幅变化（例如某些情形转向硕士或大洋洲），但主导群体保持不变。这些结果与在 PARA 上观察到的趋势一致，说明本研究发现可跨数据集与模型变体泛化。
