# ArtiMuse：兼具联合评分与专家级理解的细粒度图像美学评估

> 原标题：ArtiMuse: Fine-Grained Image Aesthetics Assessment with Joint Scoring and Expert-Level Understanding
> 作者：Shuo Cao, Nan Ma, Jiayang Li, Xiaohui Li, Lihao Shao, Kaiwen Zhu, Yu Zhou, Yuandong Pu, Jiarui Wu, Jiaquan Wang, Bo Qu, Wenhai Wang 等 · arXiv:2507.14533 · 2025-07-19

<!-- [原子块 · verbatim] ArtiMuse: Fine-Grained Image Aesthetics Assessment with Joint Scoring and Expert-Level Understanding -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] The rapid advancement of educational applications, artistic creation, and AI-generated content (AIGC) technologies has substantially increased practical requirements for comprehensive Image Aesthetics -->

<!-- [原子块 · img]  -->

**EN** Figure 1: ArtiMuse provides granular, expert-level textual understanding results for images across eight fine-grained aesthetic attributes. Additionally, it achieves precise image aesthetics scoring, significantly outperforming state-of-the-art models across multiple widely-used benchmarks.

**ZH** 图 1：ArtiMuse 为图像提供细粒度、专家级的文本化理解结果，覆盖八个美学属性。此外，它还能实现精确的图像美学评分，在多个广泛使用的基准上显著优于当前最优模型。

**EN** 1 Introduction

**ZH** 1 引言

**EN** In the era of digitalization and visual information explosion, images have become an essential medium for human beings to perceive the world, document daily life, and express emotions. From professional photography and painting to casual snapshots and sharing, images play a crucial role in conveying aesthetic values, emotional narratives, and storytelling. The advent of artificial intelligence generated content (AIGC) technologies [1, 2, 3] has further democratized visual content creation. However, this abundance of visual content also poses new challenges for quality assessment, filtering, and recommendation. While existing image quality assessment (IQA) techniques [4, 5, 6] have matured in detecting low-level degradations such as blurriness, noise, and compression artifacts, they largely focus on the technical fidelity of images and fail to capture their higher-level aesthetic attributes. Image aesthetics assessment (IAA) [7, 8, 9], which evaluates aspects such as artistic appeal, color harmony, and emotional expression, is increasingly recognized as a fundamental capability in applications including AIGC content evaluation, creative assistance, and photography education.

**ZH** 在数字化与视觉信息爆炸的时代，图像已成为人类感知世界、记录日常生活与表达情感的重要媒介。从专业摄影、绘画到随手拍摄与分享，图像在传递美学价值、情感叙事与故事性方面起着关键作用。人工智能生成内容（AIGC）技术 [1, 2, 3] 的出现进一步降低了视觉内容创作的门槛。然而，视觉内容的极大丰富也给质量评估、筛选与推荐带来了新挑战。现有图像质量评价（IQA）技术 [4, 5, 6] 在检测模糊、噪声、压缩伪影等底层退化方面已相当成熟，但它们主要关注图像的技术保真度，无法捕捉更高层的美学属性。图像美学评估（IAA）[7, 8, 9] 审视艺术感染力、色彩和谐、情感表达等方面，正日益被视为 AIGC 内容评测、创作辅助与摄影教育等应用中的一项基础能力。

**EN** Despite the growing demand, current IAA methods face notable limitations. Most existing approaches rely on simplistic score predictions without capturing the inherent subjectivity, multidimensionality, and nuanced interpretations of aesthetics. Moreover, available datasets are often small in scale, coarse in granularity, and lack professionally curated annotations based on established aesthetic theories. This gap severely limits the ability of state-of-the-art multimodal large models (MLLMs) [10, 11] to understand and reason about aesthetics.

**ZH** 尽管需求持续增长，现有 IAA 方法仍存在明显局限。多数方法只做简单的分数预测，未能刻画美学固有的主观性、多维性与细微阐释。此外，现有数据集往往规模小、粒度粗，且缺乏基于成熟美学理论的专业标注。这一缺口严重制约了当前最优多模态大模型（MLLM）[10, 11] 理解与推理美学的能力。

<!-- [原子块 · img]  -->

**EN** Figure 2: In comparison with existing models, ArtiMuse outperforms them by simultaneously achieving both accurate evaluation and precise aesthetics scoring in multi-dimensional assessments.

**ZH** 图 2：与现有模型相比，ArtiMuse 在多维评估中同时实现准确评价与精确美学评分，表现更优。

**EN** To address these challenges, we introduce ArtiMuse, a multimodal large language model (MLLM) for professional aesthetic understanding, together with ArtiMuse-10K, a meticulously curated, expert-annotated dataset. Collaborating with domain experts in aesthetics, each with 3 to over 30 years of experience, we systematically define eight explainable and fine-grained aesthetic attributes, covering aspects such as Composition & Design, Visual Elements & Structure, and Originality & Creativity, among others. Based on these attributes, we construct ArtiMuse-10K, the largest and most comprehensive fine-grained image aesthetics dataset to date, featuring both quantitative aesthetic scores and expert-written textual analyses across diverse visual domains, including graphic design, 3D design, AIGC-generated images, photography, and painting & calligraphy.

**ZH** 为应对这些挑战，我们推出 ArtiMuse——一个面向专业美学理解的多模态大语言模型（MLLM），以及精心整理、由专家标注的数据集 ArtiMuse-10K。我们与美学领域专家（从业经验从 3 年到 30 余年不等）合作，系统定义了八个可解释的细粒度美学属性，涵盖构图与设计、视觉元素与结构、原创性与创造力等方面。基于这些属性，我们构建了 ArtiMuse-10K——迄今规模最大、最完备的细粒度图像美学数据集，既包含量化的美学分数，也包含专家撰写的文本分析，覆盖平面设计、三维设计、AIGC 生成图像、摄影以及绘画与书法等多个视觉领域。

**EN** Leveraging this dataset, ArtiMuse is trained to jointly predict aesthetic scores and generate expert-level, fine-grained textual feedback, advancing aesthetic AI from mere score prediction toward holistic aesthetic reasoning and user-interpretable analysis. Notably, ArtiMuse achieves state-of-the-art performance across multiple widely used public aesthetics benchmarks, demonstrating its robust generalization ability and superior performance in both quantitative assessment and qualitative explanation, as shown in Fig. 1.

**ZH** 依托该数据集，ArtiMuse 被训练为同时预测美学分数并生成专家级、细粒度的文本反馈，把美学 AI 从单纯的分数预测推向整体性的美学推理与用户可理解的分析。如图 1 所示，ArtiMuse 在多个广泛使用的公开美学基准上取得当前最优性能，展现出稳健的泛化能力，在定量评估与定性解释两方面均表现优异。

**EN** In addition, a core technical challenge in aesthetics modeling lies in continuous score prediction using MLLMs, which are inherently designed for discrete token generation. Existing methods such as Q-Align [12] attempt to transform continuous scores into discrete ratings, and then reconstruct continuous values by weighted averaging over rating logits. However, this discretization inevitably incurs significant information loss and often leads to inaccurate predictions. To overcome this limitation, we propose a novel Token As Score strategy that densely maps predefined discrete tokens to continuous values. Specifically, we utilize existing tokens within the native LLM tokenizer to represent numeric values, thus eliminating the need to expand the vocabulary or retrain the tokenizer. This lightweight yet effective technique enables precise and robust modeling of continuous values within the MLLM framework, substantially improving the fidelity of aesthetics scoring.

**ZH** 此外，美学建模的一个核心技术难点在于：MLLM 天生是为离散词元生成而设计的，却要用于连续分数预测。Q-Align [12] 等已有方法尝试把连续分数转换为离散等级，再通过对等级 logits 加权平均重建连续值。然而这种离散化不可避免地造成显著信息损失，并常导致预测不准。为克服这一局限，我们提出一种新颖的 Token As Score 策略，把预定义的离散词元稠密地映射到连续值。具体地，我们利用原生 LLM 分词器中已有的词元来表示数值，因而无需扩展词表或重新训练分词器。这一轻量而有效的技术使 MLLM 框架内连续值的建模更精确、更稳健，大幅提升了美学评分的保真度。

**EN** Our main contributions can be summarized as follows:

**ZH** 我们的主要贡献可概括如下：

**EN** (1) ArtiMuse-10K, a comprehensive and meticulously annotated image aesthetic assessment dataset containing 10,000 images spanning over 5 main categories and 15 subcategories. Each image is manually annotated by professional experts with detailed textual evaluations across 8 aesthetic attributes, accompanied by an overall aesthetics score. As far as we know, This dataset represents the most extensive expert-curated resource for aesthetics assessment to date.

**ZH** （1）ArtiMuse-10K：一个完备且标注精细的图像美学评估数据集，含 10,000 张图像，覆盖 5 个大类与 15 个子类。每张图像由专业专家手工标注，给出 8 个美学属性的详细文本评价，并附带整体美学分数。据我们所知，该数据集是迄今规模最大的专家整理的美学评估资源。

**EN** (2) ArtiMuse, a novel image aesthetics assessment model, is capable of performing fine-grained expert-level textual analysis and providing accurate aesthetic scores. ArtMuse exhibits significantly superior aesthetic assessment expertise and fine-grained analysis compared to other IAA models and general-purpose MLLMs.

**ZH** （2）ArtiMuse：一种新型图像美学评估模型，能够执行细粒度的专家级文本分析并给出准确的美学分数。与其他 IAA 模型及通用 MLLM 相比，ArtMuse 展现出明显更优的美学评估专业性与细粒度分析能力。

**EN** (3) Token As Score, which enables precise continuous aesthetics scoring in MLLMs by mapping existing tokens to numeric values, avoiding quantization loss and tokenizer changes. It offers a lightweight, effective solution for accurate and stable score prediction.

**ZH** （3）Token As Score：通过把已有词元映射为数值，在 MLLM 中实现精确的连续美学评分，避免量化损失与分词器改动。它为准确、稳定的分数预测提供了一种轻量而有效的方案。

**EN** 2 Related Work

**ZH** 2 相关工作

**EN** 2.1 Multi-modality Large Language Models

**ZH** 2.1 多模态大语言模型

**EN** With the advancement of MLLMs [13, 14, 11, 10], their ability has expanded from basic image-text matching to understanding high-level semantic content, offering new possibilities for image aesthetics assessment. However, current MLLMs still struggle with objective evaluation, often producing overly positive and superficial judgments. Moreover, the text they generate differs significantly from the professional descriptions used by human experts, making them less suitable for high-quality automated aesthetic evaluation. Therefore, it is necessary to systematically optimize and guide these models through fine-tuning strategies.

**ZH** 随着 MLLM [13, 14, 11, 10] 的发展，其能力已从基础的图文匹配扩展到理解高层语义内容，为图像美学评估提供了新的可能。然而，当前 MLLM 在客观评价上仍有困难，常给出过于正面、流于表面的判断；而且它们生成的文本与人类专家所用的专业描述差异显著，难以胜任高质量的自动化美学评估。因此有必要通过微调策略对这类模型进行系统优化与引导。

**EN** 2.2 Image Aesthetics Assessment

**ZH** 2.2 图像美学评估

**EN** Datasets. As summarized in Table 1, existing IAA datasets suffer from three key limitations: (1) Many [15, 16, 17, 18] offer overall aesthetics scores but lack detailed evaluative descriptions, while others [19, 20] provide only vague comments without numerical ratings; (2) Most [9, 21] focus solely on overall impressions, lacking fine-grained aesthetic attribute annotations; (3) In terms of content, datasets [16, 17, 18] are mainly photographic, with limited inclusion of artworks [9, 19, 22] and little to no AIGC or everyday scene coverage. These gaps hinder comprehensive aesthetic modeling, underscoring the need for a more diverse, well-annotated benchmark.

**ZH** 数据集。如表 1 所总结，现有 IAA 数据集存在三方面关键局限：（1）许多数据集 [15, 16, 17, 18] 提供整体美学分数却缺少详细的评价性描述，另一些 [19, 20] 只给出模糊评论而没有数值评分；（2）多数数据集 [9, 21] 只关注整体印象，缺少细粒度美学属性标注；（3）在内容上，数据集 [16, 17, 18] 以摄影为主，艺术作品 [9, 19, 22] 收录有限，AIGC 与日常场景几乎没有覆盖。这些缺口阻碍了全面的美学建模，凸显出构建更多样、标注更完善基准的必要性。

**EN** Models. IAA models have evolved from simple regression to multimodal generative evaluation with integrated language understanding. Existing approaches fall into two categories: (1) Regression-based models (e.g., TANet [15], AesMamba [8]) directly predict aesthetics scores from image features but lack interpretability and generalization; (2) MLLM-based generative models leverage vision-language understanding to align better with human perception. Instruction-tuned models [23, 24] improve text generation but with limited granularity. AesExpert [7] produces expert-style descriptions but lacks score prediction. Q-Align [12] and UNIAA [25] combine text and discrete scores, yet lack fine-grained dimension-level evaluation. To overcome these gaps, we introduce ArtiMuse, a unified model that generates expert-level analysis and accurate aesthetics scores.

**ZH** 模型。IAA 模型已从简单的回归演进为融合语言理解的多模态生成式评估。现有方法分两类：（1）基于回归的模型（如 TANet [15]、AesMamba [8]）直接从图像特征预测美学分数，但缺乏可解释性与泛化能力；（2）基于 MLLM 的生成式模型借助视觉语言理解，与人类感知契合更好。经指令微调的模型 [23, 24] 改善了文本生成，但粒度有限。AesExpert [7] 能生成专家式描述，却不具备分数预测能力。Q-Align [12] 与 UNIAA [25] 结合了文本与离散分数，仍缺少细粒度的维度级评估。为弥补这些不足，我们提出 ArtiMuse——一个统一的模型，既能生成专家级分析，也能给出准确的美学分数。

**EN** 3 ArtiMuse-10K Dataset

**ZH** 3 ArtiMuse-10K 数据集

**EN** 3.1 Dataset Overview

**ZH** 3.1 数据集概览

**EN** As shown in Tab. 1, ArtiMuse-10K far exceeds existing IAA datasets in diversity and granularity. It contains 10,000 images across 5 main categories (Design, AIGC, photography, etc.) with 15 fine-grained subcategories. Each image is annotated by professional experts on eight aesthetic attributes and an overall score, offering superior professional rigor and annotation granularity.

**ZH** 如表 1 所示，ArtiMuse-10K 在多样性与粒度上远超现有 IAA 数据集。它包含 10,000 张图像，覆盖 5 个大类（设计、AIGC、摄影等）与 15 个细分子类。每张图像由专业专家就八个美学属性以及整体分数进行标注，在专业严谨性与标注粒度上均更胜一筹。

**EN** Table 1: A Comparison between ArtiMuse-10K dataset and existing IAA datasets.

**ZH** 表 1：ArtiMuse-10K 数据集与现有 IAA 数据集的对比。

<!-- [原子块 · table] Dataset Main Categories Subcategories # Image Score Text Caption # Attribute Attribute Categories Annotators AVA [ 18 ] Photography – 255,528 – – Non-Experts AADB [ 16 ] Photography – 10,000 – – Non-E -->

**EN** 3.2 Image Collection

**ZH** 3.2 图像采集

**EN** Previous studies [9, 12, 7, 29, 30, 31] have emphasized the importance of ensuring dataset diversity and extending domain coverage to enhance the quality and robustness of aesthetic assessment models. Building upon these insights, we construct ArtiMuse-10K, a high-quality dataset comprising 10,000 carefully curated images spanning five primary categories: Graphic Design, 3D Design, AIGC-generated images, Photography, and Painting & Calligraphy. These categories are subdivided into 15 distinct subcategories, such as Chinese Painting, Sculpture, and Daily Photography, ensuring comprehensive representation of diverse artistic expressions. The internal data samples and overall dataset composition are illustrated in Fig. 4 and Fig. 4, respectively.

**ZH** 已有研究 [9, 12, 7, 29, 30, 31] 强调，保证数据集多样性、扩展领域覆盖对提升美学评估模型的质量与稳健性十分重要。基于这些认识，我们构建了 ArtiMuse-10K——一个包含 10,000 张精心挑选图像的高质量数据集，涵盖五个主要类别：平面设计、三维设计、AIGC 生成图像、摄影、绘画与书法。这些类别进一步细分为 15 个不同子类，如中国画、雕塑、日常摄影等，确保对多样艺术表现形式有全面覆盖。数据集的内部数据样本与整体构成分别如图 4 与图 4 所示。

**EN** Non-AIGC Images. For non-AIGC images, we collaborate with domain experts to curate professionally created artworks sourced from academic settings, including student assignments and competition entries. To ensure the dataset reflects contemporary trends, we also collect a wide range of artistic and photographic works from reputable online art and photography platforms.

**ZH** 非 AIGC 图像。对于非 AIGC 图像，我们与领域专家合作，从学术场景中挑选专业创作的艺术作品，包括学生作业与竞赛投稿。为使数据集反映当代趋势，我们还从知名的在线艺术与摄影平台收集了大量艺术与摄影作品。

**EN** AIGC Images. We utilize state-of-the-art generative models (Stable Diffusion series [3], Dreamlike Photoreal 2.0 [1], FLUX [2], etc.) to systematically produce synthetic images. We further augment this core dataset with open-source community contributions produced using comparable architectures.

**ZH** AIGC 图像。我们使用当前最优的生成模型（Stable Diffusion 系列 [3]、Dreamlike Photoreal 2.0 [1]、FLUX [2] 等）系统性地合成图像，并进一步用开源社区中采用相近架构生成的作品扩充这一核心数据集。

<!-- [原子块 · img]  -->

**EN** Figure 3: Data examples in ArtiMuse-10K.

**ZH** 图 3：ArtiMuse-10K 中的数据示例。

<!-- [原子块 · img]  -->

**EN** Figure 4: Composition of ArtiMuse-10K.

**ZH** 图 4：ArtiMuse-10K 的构成。

**EN** 3.3 Aesthetic Attributes

**ZH** 3.3 美学属性

**EN** To establish a fine-grained annotated dataset for image aesthetics assessment, the primary task involves developing a comprehensive assessment system. Through systematic consultations with artistic experts, we have formulated a novel aesthetic assessment system. This system comprises 8 specific aesthetic attributes and an overall aesthetics score, systematically defining key dimensions of image aesthetics including Composition & Design, Visual Elements & Structure, Technical Execution, Originality & Creativity, Theme & Communication, Emotion & Viewer Response, Overall Gestalt and Comprehensive Evaluation. Notably, our system is content-agnostic and universally applicable to image types from natural to AIGC.

**ZH** 要建立细粒度标注的图像美学评估数据集，首要任务是构建一套完备的评估体系。通过与艺术专家的系统性咨询，我们制定了一套新的美学评估体系。该体系由 8 个具体美学属性与一个整体美学分数构成，系统定义了图像美学的关键维度，包括构图与设计、视觉元素与结构、技术执行、原创性与创造力、主题与传达、情感与观者反应、整体完形以及综合评价。值得注意的是，我们的体系与内容无关，普遍适用于从自然图像到 AIGC 图像的各种类型。

**EN** 3.4 Human Annotations

**ZH** 3.4 人工标注

**EN** Based on the predefined aesthetic attributes, we invite professional experts to meticulously annotate images in the ArtiMuse-10K dataset. We collaborate with domain experts whose professional experience spans a broad spectrum, ranging from at least three years to over three decades, including distinguished authorities in the field. The entire annotation process is illustrated in Fig. 5 as Type 3: Professionally Selected Images. Each image in ArtiMuse-10K is ultimately annotated with textual analysis describing eight distinct aesthetic attributes and an overall aesthetics score. Our comprehensive annotation framework enhances dataset quality and model performance by integrating multi-dimensional aesthetic attributes for fine-grained visual analysis, expert-curated scores for reliable aesthetic assessment, and rich semantic annotations for improving training robustness.

**ZH** 基于预先定义的美学属性，我们邀请专业专家对 ArtiMuse-10K 数据集中的图像进行细致标注。我们合作的领域专家从业经历跨度很大，从至少三年到三十余年不等，其中不乏该领域的权威人士。整个标注流程如图 5 中的「类型 3：专业遴选图像」所示。ArtiMuse-10K 中每张图像最终都配有描述八个不同美学属性的文本分析，以及一个整体美学分数。我们的综合标注框架从三方面提升了数据集质量与模型性能：以多维美学属性支撑细粒度视觉分析，以专家给出的分数保证美学评估的可靠性，以丰富的语义标注增强训练稳健性。

**EN** 4 Methodology

**ZH** 4 方法

<!-- [原子块 · img]  -->

**EN** Figure 5: Overview of ArtiMuse. ArtiMuse encompasses a multi-stage pipeline spanning data collection & processing, annotation generation, and model training, systematically enhancing its text evaluation capabilities and score assessment proficiency across multiple dimensions.

**ZH** 图 5：ArtiMuse 总览。ArtiMuse 包含一条贯穿数据采集与处理、标注生成与模型训练的多阶段流水线，系统性地提升其在多个维度上的文本评价能力与评分水平。

**EN** 4.1 Dataset Collection & Processing

**ZH** 4.1 数据采集与处理

**EN** Richer data sources and more meticulous manual annotations are crucial for enhancing dataset quality. In addition to the ArtiMuse-10K dataset, we carefully curate over 350,000 high-quality annotated images from existing datasets, including APDDv2 [9], PARA [17], Impressions [20] and so on.

**ZH** 更丰富的数据来源与更细致的人工标注对提升数据集质量至关重要。除 ArtiMuse-10K 数据集外，我们还从现有数据集（APDDv2 [9]、PARA [17]、Impressions [20] 等）中精心挑选了超过 350,000 张高质量标注图像。

**EN** Aesthetic Caption Quality. We place particular emphasis on the aesthetic caption quality. Our selection criteria prioritize datasets that include valuable aesthetic-related captions such as aesthetics scores, comprehensive textual analyses, and aesthetic attribute tags. These captions are subsequently utilized in the Annotation Generation phase to systematically enhance dataset quality.

**ZH** 美学描述质量。我们特别重视美学描述的质量。筛选标准优先考虑那些包含有价值美学相关描述的数据集，例如美学分数、综合性文本分析与美学属性标签。这些描述随后在标注生成阶段被系统性地用于提升数据集质量。

**EN** Aesthetic Quality Diversity. Our collection specifically incorporates images with varying aesthetic qualities, including intentionally retained lower-quality samples, to address both dataset diversity requirements and mitigate the prevalent preference bias observed in contemporary LLMs. This carefully balanced composition strategy enhances model training through controlled inclusion of suboptimal visual materials, thereby improving discriminative capabilities in aesthetic assessment.

**ZH** 美学质量多样性。我们的采集特意纳入美学质量各异的图像，包括有意保留的低质量样本，以兼顾数据集的多样性要求，并缓解当前 LLM 中普遍存在的偏好偏置。这种经过仔细权衡的构成策略，通过可控地引入次优视觉素材来强化模型训练，从而提升美学评估中的判别能力。

**EN** 4.2 Annotation Generation

**ZH** 4.2 标注生成

**EN** The Annotation Generation stage aims to enrich the dataset with detailed descriptive and evaluative annotations, illustrated in Fig. 5. This process involves creating distinct annotation types based on the available information for each image. Type 1: For images with only score caption, we leverage this global quality assessment to generate holistic analyses. We design a prompt to guide the MLLM in producing a comprehensive evaluation based on predefined aesthetic attributes, while incorporating both the score and visual input. Type 2: For images with partial text captions containing specific aesthetic descriptions, we employ a prompt to instruct the MLLM to generate fine-grained evaluations. For each image, the model produces a structural analysis across 8 aesthetic attributes, utilizing both the textual and visual inputs. Type 3: For professionally selected images, we engage experts to conduct structural analysis based on pre-defined aesthetic attributes, along with providing an overall aesthetics score. More details are in the Supp.

**ZH** 标注生成阶段旨在为数据集补充详细的描述性与评价性标注，如图 5 所示。该过程依据每张图像可用信息的不同，生成不同类型的标注。类型 1：对于只有分数描述的图像，我们借助这一全局质量评估来生成整体性分析。我们设计了一条提示，引导 MLLM 在预定义美学属性基础上、结合分数与视觉输入生成综合评估。类型 2：对于带有具体美学描述的部分文本描述的图像，我们用一条提示指示 MLLM 生成细粒度评价。对每张图像，模型结合文本与视觉输入，产出覆盖 8 个美学属性的结构化分析。类型 3：对于专业遴选的图像，我们请专家依据预定义美学属性开展结构化分析，并给出整体美学分数。更多细节见补充材料。

**EN** Importance of Manual Annotations. Although MLLMs demonstrate strong aesthetic evaluation capabilities, our empirical analysis reveals a systematic bias: they tend to generate overwhelmingly positive assessments regardless of the actual image quality, as shown in Fig. 7. This positivity bias leads to annotations that poorly reflect true aesthetic merit. To address this limitation, we incorporate professional human evaluations to provide balanced and reliable ground-truth annotations.

**ZH** 人工标注的重要性。尽管 MLLM 展现出较强的美学评估能力，我们的实证分析揭示了一种系统性偏置：无论图像实际质量如何，它们倾向于生成压倒性正面的评价，如图 7 所示。这种正面偏置导致标注难以反映真实的美学价值。为弥补这一缺陷，我们引入专业人工评价，以提供均衡、可靠的真值标注。

**EN** 4.3 Training Strategy

**ZH** 4.3 训练策略

**EN** ArtiMuse is built on InternVL-3-8B [10]. We modify the dynamic resolution strategy to a fixed-resolution approach while retaining the remaining components. The training process consists of two distinct phases: text pretraining and score fine-tuning, as illustrated in Fig. 5. In both stages, we jointly train the vision encoder, MLP, and LLM components, with the LLM undergoing LoRA-based fine-tuning. The ArtiMuse uses common GPT loss [32], i.e. minimizing the cross-entropy loss between the predicted logits and target tokens.

**ZH** ArtiMuse 以 InternVL-3-8B [10] 为基础构建。我们把动态分辨率策略改为固定分辨率策略，其余组件保持不变。训练过程包含两个不同阶段：文本预训练与分数微调，如图 5 所示。两个阶段中，我们联合训练视觉编码器、MLP 与 LLM 组件，其中 LLM 采用基于 LoRA 的微调。ArtiMuse 使用常规的 GPT loss [32]，即最小化预测 logits 与目标词元之间的交叉熵损失。

**EN** Text Pretrain. The text pretraining phase utilizes our complete collected image dataset, where each image is paired with its corresponding aesthetic analysis caption generated during the annotation generation stage. This phase aims to equip the model with accurate structural aesthetic analysis capabilities while largely preserving the MLLM’s pretrained knowledge. To achieve this balance, we apply LoRA fine-tuning specifically to the LLM component.

**ZH** 文本预训练。文本预训练阶段使用我们采集到的完整图像数据集，每张图像配以其在标注生成阶段产生的美学分析描述。该阶段旨在赋予模型准确的结构化美学分析能力，同时大体保留 MLLM 的预训练知识。为实现这一平衡，我们对 LLM 组件专门施加 LoRA 微调。

**EN** Score Finetune. After establishing foundational aesthetic understanding through pretraining, we proceed to score fine-tuning. In this phase, we convert each image’s overall aesthetics score into a specialized scoring token designed exclusively for aesthetics scoring, which then serves as the training caption. Inspired by previous works [12, 25, 33], we propose a novel score prediction strategy called Token As Score, which eliminates the need for vocabulary expansion or tokenizer retraining. Specifically, we designate 101 existing tokens as [Aes_Score_Token]s, each corresponding to integer scores ranging from 0 to 100. We select tokens that are concise and inherently carry ordinal semantic information from the vocabulary. In our implementation, we employ twin-letter combinations as tokens (e.g., Score 1 is represented as [Aes_Score_Token_1], where the actual token is ab. See supp. for more details). During data preprocessing, we first normalize aesthetics scores to the [0,100] range and then map them to their corresponding tokens. This methodology enables the construction of training data where continuous scores are discretized into token representations. The model is subsequently fine-tuned to predict these discrete tokens. During inference, we convert the predicted tokens back to their numerical values, and the final aesthetics score is derived by computing the expectation over the probability distribution of all possible score tokens. Specifically, we denote ⟦SLOT_0⟧ and ⟦SLOT_1⟧ for logits and probability of [Aes_Score_Token_i], the final aesthetics score ⟦SLOT_2⟧ is compute as: ⟦SLOT_3⟧.

**ZH** 分数微调。在通过预训练建立基础美学理解之后，我们进入分数微调阶段。在该阶段，我们把每张图像的整体美学分数转换为一个专用于美学评分的专用评分词元，并将其作为训练描述。受已有工作 [12, 25, 33] 启发，我们提出一种名为 Token As Score 的新型分数预测策略，无需扩展词表或重新训练分词器。具体地，我们指定 101 个已有词元作为 [Aes_Score_Token]，每个对应 0 到 100 的整数分数。我们从词表中挑选简洁且天然携带序数语义信息的词元。在我们的实现中，采用双字母组合作为词元（例如分数 1 表示为 [Aes_Score_Token_1]，其实际词元为 ab，详见补充材料）。在数据预处理时，我们先把美学分数归一化到 [0,100] 区间，再映射到对应词元。通过这一方法，可构造出连续分数被离散化为词元表示的训练数据，模型随后被微调以预测这些离散词元。推理时，我们把预测的词元还原为数值，最终美学分数由所有可能分数词元的概率分布求期望得到。具体地，我们记 ⟦SLOT_0⟧ 与 ⟦SLOT_1⟧ 分别为 [Aes_Score_Token_i] 的 logits 与概率，最终美学分数 ⟦SLOT_2⟧ 计算为：⟦SLOT_3⟧。

<!-- [原子块 · img]  -->

**EN** Figure 6: Comparison of score prediction methods. Token As Score features a more rational design and delivers more precise results.

**ZH** 图 6：分数预测方法的对比。Token As Score 设计更合理，结果更精确。

**EN** Why Token As Score? Current approaches for scoring with MLLMs primarily fall into two categories: (1) directly prompting the LLM to output scores as text (Text As Score), or (2) predefining discrete levels corresponding to specific score intervals and computing the final score based on the model’s predicted token distribution (Level As Score). Previous works [12, 33, 25] demonstrate that directly generating scores as text leads to severe hallucination issues. Thus, we adopt the Token As Score approach and investigate the impact of token granularity on model performance. A comparison of these score prediction methods is shown in Fig. 6. Further experiments in Tab. 4 show that 100 aesthetics score tokens achieve optimal results.

**ZH** 为何采用 Token As Score？当前用 MLLM 打分的方法主要分两类：（1）直接提示 LLM 以文本形式输出分数（Text As Score）；（2）预定义对应特定分数区间的离散等级，再依据模型预测的词元分布计算最终分数（Level As Score）。已有工作 [12, 33, 25] 表明，直接以文本生成分数会引发严重的幻觉问题。因此我们采用 Token As Score 方案，并考察词元粒度对模型性能的影响。这些分数预测方法的对比见图 6。表 4 中的进一步实验表明，100 个美学分数词元可取得最优结果。

**EN** Maintaining Text Ability. A widely recognized challenge in IAA and IQA tasks is that MLLMs often struggle to simultaneously preserve their textual understanding and scoring capabilities [4, 6]. Since the training data in the score fine-tuning phase is significantly more monotonous than in text pretraining, full fine-tuning of the LLM can easily degrade its structural aesthetic analysis ability. To mitigate this issue while maintaining textual proficiency, we employ LoRA-based fine-tuning for the LLM, enabling the model to retain both its linguistic and scoring capabilities.

**ZH** 保持文本能力。IAA 与 IQA 任务中一个广为人知的挑战是：MLLM 往往难以同时保持其文本理解能力与评分能力 [4, 6]。由于分数微调阶段的训练数据比文本预训练阶段单调得多，对 LLM 做全量微调很容易削弱其结构化美学分析能力。为在保持文本能力的同时缓解这一问题，我们对 LLM 采用基于 LoRA 的微调，使模型同时保留语言能力与评分能力。

**EN** 5 Experiments

**ZH** 5 实验

**EN** 5.1 Implementation Details

**ZH** 5.1 实现细节

**EN** In our experiments, we adopt InternVL-3-8B [10] as the base model initialized with its pretrained weights. During text pretraining, we implement a batch size of 128 and learning rate of ⟦SLOT_4⟧ with a cosine annealing schedule [34], training for one epoch to balance convergence with prior knowledge preservation. For the score fine-tuning, we maintain the batch size at 128 while adjusting the learning rate to ⟦SLOT_5⟧ across 2 training epochs. We maintain identical configurations across all experiments, with all training conducted on 4 * NVIDIA A100 80GB GPUs. The text pretraining phase typically takes 5 hours, while the score fine-tuning duration varies between 10 minutes to 4 hours depending on dataset size, demonstrating efficient convergence across different scales.

**ZH** 实验中我们采用 InternVL-3-8B [10] 作为基座模型，并用其预训练权重初始化。文本预训练阶段批大小为 128，学习率 ⟦SLOT_4⟧，采用余弦退火调度 [34]，训练一个轮次，以在收敛与保留先验知识之间取得平衡。分数微调阶段批大小保持 128，学习率调整为 ⟦SLOT_5⟧，训练 2 个轮次。所有实验配置保持一致，全部训练在 4 * NVIDIA A100 80GB GPU 上进行。文本预训练阶段通常耗时 5 小时，分数微调耗时随数据集规模在 10 分钟到 4 小时之间变化，体现出不同规模下的高效收敛。

**EN** 5.2 Structural Aesthetic Analysis

**ZH** 5.2 结构化美学分析

**EN** Judging by MLLM. To evaluate current models’ ability of structural aesthetic analysis, we design a judgement framework leveraging the superior comprehension power of MLLM. An image is presented to both experts and various models to generate aesthetic analysis on 8 aesthetics attributes. Then a judging MLLM selects which model performs best across each attribute, using the human expert’s description as a reference. The results in Tab. 2 show ArtiMuse outperforms other models across 8 aesthetic attributes, demonstrating superior structural aesthetic analysis capability.

**ZH** 由 MLLM 评判。为评估现有模型的结构化美学分析能力，我们设计了一个借助 MLLM 强大理解力的评判框架。把同一张图像呈现给专家与各模型，请它们就 8 个美学属性生成美学分析；随后由一个评判 MLLM 以人类专家的描述为参照，选出各属性上表现最佳的模型。表 2 的结果显示，ArtiMuse 在 8 个美学属性上均优于其他模型，展现出更强的结构化美学分析能力。

**EN** Judging by Human. In addition, we conduct a user study where participants are asked to compare and vote for the model they perceive as producing higher-quality aesthetic analysis. The proportion of selections for each model, presented as Human Rate in Table 2, demonstrates that our approach achieves a significantly higher preference rate compared to other methods.

**ZH** 由人类评判。此外我们开展了一项用户研究，请参与者比较并投票选出他们认为美学分析质量更高的模型。各模型被选中的比例（表 2 中的 Human Rate）表明，本文方法的偏好率显著高于其他方法。

**EN** Table 2: The selection rates of different models. For the first 8 aesthetic attributes, evaluations are performed by Gemini-2.0-flash, while Human Rate is provided by volunteer participants.

**ZH** 表 2：不同模型的选中率。前 8 个美学属性的评测由 Gemini-2.0-flash 完成，Human Rate 由志愿者提供。

<!-- [原子块 · table] Aesthetic Attributes AesExpert [ 7 ] Qwen-2.5-VL-7B [ 11 ] InternVL3-8B [ 10 ] ArtiMuse 1. Composition & Design 0.0% 12.7% 10.4% 76.9% 2. Visual Elements & Structure 0.0% 19.3% 16.5% 64.2% 3. Technica -->

**EN** Qualitative comparison. Fig. 7presents a systematic evaluation of aesthetic analysis performance across different models. Our approach demonstrates consistent superiority in analyzing both natural and AIGC images, with particular strengths in identifying key aesthetic elements such as compositional cohesion and characteristic AIGC artifacts. More results are provided in the Supp.

**ZH** 定性对比。图 7 展示了不同模型美学分析性能的系统性评测。本文方法在分析自然图像与 AIGC 图像时均表现出一致的优越性，在识别构图凝聚力、AIGC 典型伪影等关键美学要素上尤为突出。更多结果见补充材料。

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

**EN** Figure 7: Structural aesthetic analysis results. Red, green, and brown denote positive, negative, and expert-level analyses, respectively. ArtiMuse uniquely identifies flaws in low-aesthetic images while providing professional assessment of high-aesthetic images, capabilities absent in other models.

**ZH** 图 7：结构化美学分析结果。红色、绿色与棕色分别表示正面、负面与专家级分析。ArtiMuse 能独特地识别低美感图像中的缺陷，同时对高美感图像给出专业评估，这些能力是其他模型所不具备的。

**EN** 5.3 Aesthetics Scoring

**ZH** 5.3 美学评分

**EN** Comparison across Multiple Image Aesthetics Scoring Datasets. We evaluate the performance of ArtiMuse against other models across multiple Image aesthetics scoring datasets. For models unable for test (TANet [15], AesMamba [8], UNIAA-LLaVA [25], Next Token Is Enough [33]), we directly adopt the test results reported in their original papers. For models with unclear training protocols or those trained on general scenarios (MUSIQ [35], VILA [36], mPLUG-Owl2 [37], ShareGPT-4V [38], Qwen-2.5-VL-7B [11], InternVL3-8B [10], Q-Instruct [39], PEAS [40]), we test their official released models. Both Q-Align [12] and our proposed model are fine-tuned on each target dataset. As shown in Tab. 3, ArtiMuse demonstrates superior performance, achieving nearly the highest metrics across all datasets. Notably, it outperforms other models by over 0.05 PLCC on the PARA [17] and ArtiMuse-10K datasets, demonstrating its accurate aesthetics scoring capability.

**ZH** 在多个图像美学评分数据集上的对比。我们在多个图像美学评分数据集上评估 ArtiMuse 与其他模型的性能。对于无法测试的模型（TANet [15]、AesMamba [8]、UNIAA-LLaVA [25]、Next Token Is Enough [33]），我们直接采用其原论文报告的测试结果。对于训练协议不明或面向通用场景训练的模型（MUSIQ [35]、VILA [36]、mPLUG-Owl2 [37]、ShareGPT-4V [38]、Qwen-2.5-VL-7B [11]、InternVL3-8B [10]、Q-Instruct [39]、PEAS [40]），我们测试其官方发布的模型。Q-Align [12] 与本文模型均在各目标数据集上做了微调。如表 3 所示，ArtiMuse 性能优越，在所有数据集上几乎都取得最高指标。值得注意的是，它在 PARA [17] 与 ArtiMuse-10K 数据集上以超过 0.05 PLCC 的优势领先其他模型，体现出准确的美学评分能力。

**EN** Generalization Ability. We compare the generalization capabilities of ArtiMuse and Q-Align, the top-performing baseline model in our comparison. Both models are fine-tuned solely on the largest AVA dataset [18] and subsequently evaluated on out-of-distribution datasets without additional adaptation. As presented in Table 3, ArtiMuse consistently achieves superior performance over Q-Align across all benchmark datasets. Remarkably, ArtiMuse’s zero-shot transfer performance exceeds that of several specialized IAA models, highlighting its exceptional generalization ability.

**ZH** 泛化能力。我们比较 ArtiMuse 与对比中表现最好的基线模型 Q-Align 的泛化能力。两个模型都只在规模最大的 AVA 数据集 [18] 上微调，随后在不做额外适配的情况下于分布外数据集上评测。如表 3 所示，ArtiMuse 在所有基准数据集上始终优于 Q-Align。尤为突出的是，ArtiMuse 的零样本迁移性能超过了若干专用 IAA 模型，凸显其卓越的泛化能力。

**EN** Discussion of Image Aesthetics Scoring Datasets. Prior work [12, 6, 25, 33] has consistently demonstrated that IAA remains a challenging task due to the subjective nature of aesthetic perception and the substantial distributional shifts across different datasets. Our results in Tab. 3 further corroborate this observation: while models can achieve strong performance when fine-tuned on a single dataset, their accuracy often degrades significantly when evaluated on unseen datasets.

**ZH** 关于图像美学评分数据集的讨论。已有工作 [12, 6, 25, 33] 一致表明，由于美感感知的主观性以及不同数据集之间巨大的分布偏移，IAA 始终是一项具有挑战性的任务。我们在表 3 中的结果进一步印证了这一点：模型在单一数据集上微调时可以取得很好的性能，但在未见数据集上评测时准确率往往显著下降。

**EN** Table 3: Comparison on aesthetics scoring. The best and second-best performances are highlighted in red and blue, respectively. † Results are taken directly from original papers as these models cannot be tested. * Results are trained only on AVA to compare the generalization ability. For models without scoring capability, we prompt them to directly output scores as text for evaluation.

**ZH** 表 3：美学评分对比。最优与次优性能分别以红色与蓝色标出。† 结果直接引自原论文，因为这些模型无法测试。* 结果仅在 AVA 上训练，用于比较泛化能力。对于不具备评分能力的模型，我们提示它们直接以文本形式输出分数用于评测。

<!-- [原子块 · table] Model AVA [ 18 ] PARA [ 17 ] TAD66K [ 15 ] FLICKR-AES [ 26 ] ArtiMuse-10K SRCC PLCC SRCC PLCC SRCC PLCC SRCC PLCC SRCC PLCC Traditional Models MUSIQ [ 35 ] 0.225 0.258 0.490 0.600 0.099 0.149 0.150 0. -->

**EN** 5.4 Ablation Studies

**ZH** 5.4 消融实验

**EN** Datasets Variants. We conduct 4 experiments (a)-(c) to systematically validate the contribution of each dataset component, as shown in Tab. 4. The results demonstrate consistent performance drop when any component is removed, with the most significant drop occurring upon exclusion of the Images w/ score caption subset, for the subset’s inclusion of data from AVA. The results underscore the critical impact of dataset composition on model performance.

**ZH** 数据集变体。我们开展了 4 组实验 (a)-(c)，系统验证各数据集组成部分的贡献，如表 4 所示。结果表明，去掉任一组成部分都会导致性能下降，其中剔除「带分数描述的图像」子集时下降最为显著，因为该子集包含了来自 AVA 的数据。这些结果凸显了数据集构成对模型性能的关键影响。

**EN** Training Strategy. Comparative analysis between (d) and (i) reveals that full fine-tuning significantly impacts model performance, primarily due to the loss of fundamental aesthetic priors acquired during the text pretraining phase. This finding is further substantiated by the comparison between (e) and (i), which conclusively demonstrates the effectiveness of our proposed 2-stage training paradigm. The results indicate that preserving pretrained text representations while adapting to score prediction tasks yields superior performance compared to end-to-end joint training approaches.

**ZH** 训练策略。(d) 与 (i) 的对比分析表明，全量微调会显著影响模型性能，主要原因是在文本预训练阶段获得的基础美学先验丢失。(e) 与 (i) 的对比进一步佐证了这一点，确证了我们提出的两阶段训练范式的有效性。结果表明，在保留预训练文本表示的同时适配分数预测任务，其性能优于端到端的联合训练方式。

**EN** Score Prediction. Our systematic exploration of score prediction strategies is presented in (f)-(i). Exp.(f), which directly converts scores to text for both training and inference, demonstrates suboptimal performance. The introduction of aesthetics score Tokens yields significant improvements, with analysis revealing that (g) suffers from insufficient token granularity while (h) is hampered by excessive token complexity. Configuration (i) achieves the optimal balance between precision and learnability, establishing it as our final choice. More experiments are provided in the Supp.

**ZH** 分数预测。我们对分数预测策略的系统性探索见 (f)-(i)。实验 (f) 在训练与推理时都直接把分数转换为文本，性能欠佳。引入美学分数词元后效果显著改善，分析显示 (g) 受词元粒度不足所限，而 (h) 则因词元过于复杂而受阻。配置 (i) 在精度与可学习性之间取得最优平衡，因而成为我们的最终选择。更多实验见补充材料。

**EN** Table 4: Ablation studies. The table compares different combinations of dataset variants, training, and training methods, with evaluation metrics SRCC and PLCC reported for AVA dataset.

**ZH** 表 4：消融实验。表中比较了数据集变体、训练与训练方法的不同组合，并在 AVA 数据集上报告 SRCC 与 PLCC 指标。

<!-- [原子块 · table] Exp. Images w/ Score Caption Images w/ Partial Text Caption Professionally Selected Images Training Strategies Score Prediction SRCC PLCC (a) ✓ \checkmark ✓ \checkmark – LLM LoRA / 2-Stage Training 10 -->

**EN** 6 Conclusion

**ZH** 6 结论

**EN** We introduce ArtiMuse-10K, a large expert-annotated dataset for image aesthetics assessment, and ArtiMuse, the first model to achieve expert-level textual evaluation and precise aesthetics scoring. Additionally, we propose Token As Score, a lightweight yet effective method enabling precise continuous score prediction in MLLMs. Together these contributions will advance the field of image aesthetics assessment by providing more comprehensive dataset, more superior model, and more efficient scoring paradigm.

**ZH** 我们提出 ArtiMuse-10K——一个面向图像美学评估的大型专家标注数据集，以及 ArtiMuse——首个同时实现专家级文本评价与精确美学评分的模型。此外，我们提出 Token As Score，一种轻量而有效的方法，使 MLLM 能够精确预测连续分数。这些贡献将从更完备的数据集、更优越的模型与更高效的评分范式三个方面推动图像美学评估领域的发展。

**EN** Limitations. The current model is limited to understanding and analyzing, and is unable to provide professional aesthetic enhancement recommendations, which will be addressed in future work.

**ZH** 局限性。当前模型仅限于理解与分析，尚不能提供专业的美学改进建议，这将在未来工作中解决。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] [1] dreamlike.art, “Dreamlike photoreal 2.0,” https://huggingface.co/dreamlike-art/dreamlike-photoreal-2.0 , 2023, accessed: 2025-05-14, Licensed under CreativeML OpenRAIL-M (modified). -->

<!-- [原子块 · verbatim] [2] B. F. Labs, “Flux,” https://github.com/black-forest-labs/flux , 2024. -->

<!-- [原子块 · verbatim] [3] R. Rombach, A. Blattmann, D. Lorenz, P. Esser, and B. Ommer, “High-resolution image synthesis with latent diffusion models,” 2021. -->

<!-- [原子块 · verbatim] [4] Z. You, Z. Li, J. Gu, Z. Yin, T. Xue, and C. Dong, “Depicting beyond scores: Advancing image quality assessment through multi-modal language models,” in European Conference on Computer Vision , 20 -->

<!-- [原子块 · verbatim] [5] Z. You, J. Gu, Z. Li, X. Cai, K. Zhu, C. Dong, and T. Xue, “Descriptive image quality assessment in the wild,” arXiv preprint arXiv:2405.18842 , 2024. -->

<!-- [原子块 · verbatim] [6] Z. You, X. Cai, J. Gu, T. Xue, and C. Dong, “Teaching large language models to regress accurate image quality scores using score distribution,” in IEEE Conference on Computer Vision and Pattern Re -->

<!-- [原子块 · verbatim] [7] Y. Huang, X. Sheng, Z. Yang, Q. Yuan, Z. Duan, P. Chen, L. Li, W. Lin, and G. Shi, “Aesexpert: Towards multi-modality foundation model for image aesthetics perception,” arXiv:2404.09624 , 2024. -->

<!-- [原子块 · verbatim] [8] F. Gao, Y. Lin, J. Shi, M. Qiao, and N. Wang, “Aesmamba: Universal image aesthetic assessment with state space models,” in Proceedings of the 32nd ACM International Conference on Multimedia , 2024 -->

<!-- [原子块 · verbatim] [9] X. Jin, Q. Qiao, Y. Lu, H. Wang, H. Huang, S. Gao, J. Liu, and R. Li, “Apddv2: Aesthetics of paintings and drawings dataset with artist labeled scores and comments,” 2024. [Online]. Available: htt -->

<!-- [原子块 · verbatim] [10] J. Zhu, W. Wang, Z. Chen, Z. Liu, S. Ye, L. Gu, Y. Duan, H. Tian, W. Su, J. Shao et al. , “Internvl3: Exploring advanced training and test-time recipes for open-source multimodal models,” arXiv p -->

<!-- [原子块 · verbatim] [11] S. Bai, K. Chen, X. Liu, J. Wang, W. Ge, S. Song, K. Dang, P. Wang, S. Wang, J. Tang et al. , “Qwen2.5-vl technical report,” arXiv preprint arXiv:2502.13923 , 2025. -->

<!-- [原子块 · verbatim] [12] H. Wu, Z. Zhang, W. Zhang, C. Chen, L. Liao, C. Li, Y. Gao, A. Wang, E. Zhang, W. Sun, Q. Yan, X. Min, G. Zhai, and W. Lin, “Q-align: Teaching LMMs for visual scoring via discrete text-defined le -->

<!-- [原子块 · verbatim] [13] J. Achiam, S. Adler, S. Agarwal, L. Ahmad, I. Akkaya, F. L. Aleman, D. Almeida, J. Altenschmidt, S. Altman, S. Anadkat et al. , “Gpt-4 technical report,” arXiv preprint arXiv:2303.08774 , 2023. -->

<!-- [原子块 · verbatim] [14] G. Team, R. Anil, S. Borgeaud, J.-B. Alayrac, J. Yu, R. Soricut, J. Schalkwyk, A. M. Dai, A. Hauth, K. Millican et al. , “Gemini: a family of highly capable multimodal models,” arXiv preprint arX -->

<!-- [原子块 · verbatim] [15] S. He, Y. Zhang, R. Xie, D. Jiang, and A. Ming, “Rethinking image aesthetics assessment: Models, datasets and benchmarks,” IJCAI , 2022. -->

<!-- [原子块 · verbatim] [16] S. Kong, X. Shen, Z. Lin, R. Mech, and C. Fowlkes, “Photo aesthetics ranking network with attributes and content adaptation,” 2016. [Online]. Available: https://arxiv.org/abs/1606.01621 -->

<!-- [原子块 · verbatim] [17] Y. Yang, L. Xu, L. Li, N. Qie, Y. Li, P. Zhang, and Y. Guo, “Personalized image aesthetics assessment with rich attributes,” 2022. [Online]. Available: https://arxiv.org/abs/2203.16754 -->

<!-- [原子块 · verbatim] [18] N. Murray, L. Marchesotti, and F. Perronnin, “Ava: A large-scale database for aesthetic visual analysis,” in 2012 IEEE Conference on Computer Vision and Pattern Recognition , 2012, pp. 2408–2415. -->

<!-- [原子块 · verbatim] [19] P. Achlioptas, M. Ovsjanikov, K. Haydarov, M. Elhoseiny, and L. Guibas, “Artemis: Affective language for visual art,” CoRR , vol. abs/2101.07396, 2021. -->

<!-- [原子块 · verbatim] [20] J. Kruk, C. Ziems, and D. Yang, “Impressions: Understanding visual semiotics and aesthetic impact,” 2023. [Online]. Available: https://arxiv.org/abs/2310.17887 -->

<!-- [原子块 · verbatim] [21] D. V. Nieto, L. Celona, and C. F. Labrador, “Understanding aesthetics with language: A photo critique dataset for aesthetic assessment,” in Thirty-sixth Conference on Neural Information Processin -->

<!-- [原子块 · verbatim] [22] R. Yi, H. Tian, Z. Gu, Y.-K. Lai, and P. L. Rosin, “Towards artistic image aesthetics assessment: a large-scale dataset and a new method,” 2023. [Online]. Available: https://arxiv.org/abs/2303.15 -->

<!-- [原子块 · verbatim] [23] H. Wu, Z. Zhang, E. Zhang, C. Chen, L. Liao, A. Wang, K. Xu, C. Li, J. Hou, G. Zhai et al. , “Q-instruct: Improving low-level visual abilities for multi-modality foundation models,” in Proceeding -->

<!-- [原子块 · verbatim] [24] J. Yun and J. Choo, “Scaling up personalized image aesthetic assessment via task vector customization,” in European Conference on Computer Vision . Springer, 2024, pp. 323–339. -->

<!-- [原子块 · verbatim] [25] Z. Zhou, Q. Wang, B. Lin, Y. Su, R. Chen, X. Tao, A. Zheng, L. Yuan, P. Wan, and D. Zhang, “Uniaa: A unified multi-modal image aesthetic assessment baseline and benchmark,” arXiv preprint arXiv:2 -->

<!-- [原子块 · verbatim] [26] J. Ren, X. Shen, Z. Lin, R. Mech, and D. J. Foran, “Personalized image aesthetics,” in The IEEE International Conference on Computer Vision (ICCV) , Oct 2017. -->

<!-- [原子块 · verbatim] [27] Y. Fang, H. Zhu, Y. Zeng, K. Ma, and Z. Wang, “Perceptual quality assessment of smartphone photography,” in IEEE Conference on Computer Vision and Pattern Recognition , 2020, pp. 3677–3686. -->

<!-- [原子块 · verbatim] [28] V. Hosu, H. Lin, T. Sziranyi, and D. Saupe, “Koniq-10k: An ecologically valid database for deep learning of blind image quality assessment,” IEEE Transactions on Image Processing , vol. 29, p. 40 -->

<!-- [原子块 · verbatim] [29] S. Cao, Y. Liu, W. Zhang, Y. Qiao, and C. Dong, “Grids: Grouped multiple-degradation restoration with image degradation similarity,” in European Conference on Computer Vision . Springer, 2024, pp -->

<!-- [原子块 · verbatim] [30] X. Li, Y. Liu, S. Cao, Z. Chen, S. Zhuang, X. Chen, Y. He, Y. Wang, and Y. Qiao, “Diffvsr: Enhancing real-world video super-resolution with diffusion models for advanced visual quality and tempor -->

<!-- [原子块 · verbatim] [31] S. Cao, Y. Liu, X. Li, Y. Gao, Y. Zhou, and C. Dong, “Dualx-vsr: Dual axial spatial × \times temporal transformer for real-world video super-resolution without motion compensation,” 2025. [Online -->

<!-- [原子块 · verbatim] [32] A. Radford, J. Wu, R. Child, D. Luan, D. Amodei, I. Sutskever et al. , “Language models are unsupervised multitask learners,” OpenAI blog , vol. 1, no. 8, p. 9, 2019. -->

<!-- [原子块 · verbatim] [33] M. Li, R. Wang, L. Sun, Y. Bai, and X. Chu, “Next token is enough: Realistic image quality and aesthetic scoring with multimodal large language model,” 2025. [Online]. Available: https://arxiv.or -->

<!-- [原子块 · verbatim] [34] I. Loshchilov and F. Hutter, “Sgdr: Stochastic gradient descent with warm restarts,” in ICLR , 2017. -->

<!-- [原子块 · verbatim] [35] J. Ke, Q. Wang, Y. Wang, P. Milanfar, and F. Yang, “Musiq: Multi-scale image quality transformer,” 2021. [Online]. Available: https://arxiv.org/abs/2108.05997 -->

<!-- [原子块 · verbatim] [36] J. Lin, H. Yin, W. Ping, Y. Lu, P. Molchanov, A. Tao, H. Mao, J. Kautz, M. Shoeybi, and S. Han, “Vila: On pre-training for visual language models,” 2023. -->

<!-- [原子块 · verbatim] [37] Q. Ye, H. Xu, J. Ye, M. Yan, A. Hu, H. Liu, Q. Qian, J. Zhang, F. Huang, and J. Zhou, “mplug-owl2: Revolutionizing multi-modal large language model with modality collaboration,” 2023. [Online]. A -->

<!-- [原子块 · verbatim] [38] L. Chen, J. Li, X. Dong, P. Zhang, C. He, J. Wang, F. Zhao, and D. Lin, “Sharegpt4v: Improving large multi-modal models with better captions,” in European Conference on Computer Vision . Springer -->

<!-- [原子块 · verbatim] [39] H. Wu, Z. Zhang, E. Zhang, C. Chen, L. Liao, A. Wang, K. Xu, C. Li, J. Hou, G. Zhai, G. Xue, W. Sun, Q. Yan, and W. Lin, “Q-instruct: Improving low-level visual abilities for multi-modality found -->

<!-- [原子块 · verbatim] [40] J. Yun and J. Choo, “Scaling up personalized image aesthetic assessment via task vector customization,” 2024. [Online]. Available: https://arxiv.org/abs/2407.07176 -->

<!-- [原子块 · verbatim] [41] R. BT, “Methodology for the subjective assessment of the quality of television pictures,” International Telecommunication Union , vol. 4, p. 19, 2002. -->

**EN** Appendix

**ZH** 附录

**EN** Appendix A ArtiMuse-10K Dataset Details

**ZH** 附录 A ArtiMuse-10K 数据集细节

**EN** A.1 Details of Aesthetic Attributes

**ZH** A.1 美学属性细节

**EN** The ArtiMuse-10K dataset employs structural analysis for textual annotations, with each image evaluated across eight fine-grained aesthetic attributes. These attributes were rigorously defined by a panel of domain experts, all of whom possess at least 3 years of formal training in aesthetics, with the most senior member boasting over 30 years of professional experience in the field. This ensures comprehensive coverage of key image aesthetics dimensions while maintaining robust generalizability across diverse image types—including designs, photographs, paintings, calligraphy, and AI-generated content (AIGC) images. The detailed of these attributes are presented in Tab. 5.

**ZH** ArtiMuse-10K 数据集采用结构化分析作为文本标注形式，每张图像沿八个细粒度美学属性进行评估。这些属性由一组领域专家严格界定，专家均具备至少 3 年的美学专业训练，其中资历最深者在该领域拥有超过 30 年的从业经验。这保证了对图像美学关键维度的全面覆盖，同时在多种图像类型——包括设计作品、照片、绘画、书法与人工智能生成内容（AIGC）图像——上保持稳健的泛化性。这些属性的详细说明见表 5。

**EN** Table 5: Aesthetic attributes and their descriptions of ArtiMuse-10K dataset.

**ZH** 表 5：ArtiMuse-10K 数据集的美学属性及其描述。

<!-- [原子块 · table] No. Attribute Description 1 Composition & Design Evaluate the balance, contrast, layout aesthetics, and rhythm of the composition. Focus on the use of dynamic focal points, unity, and harmony in the d -->

**EN** A.2 Charateristics of ArtiMuse-10K

**ZH** A.2 ArtiMuse-10K 的特征

**EN** WordCloud. WordCloud of our introduced ArtiMuse-10K dataset is depicted in Fig. 8 . We analyze the textual annotations of ArtiMuse across eight aesthetic attributes and find that the most frequently occurring terms—such as "image," "visual," "composition," "overall," and "elements"—are strongly correlated with image aesthetic quality. This observation suggests that human experts primarily focus on fundamental visual characteristics when assessing artistic merit.

**ZH** 词云。图 8 给出了我们提出的 ArtiMuse-10K 数据集的词云。我们分析了 ArtiMuse 在八个美学属性上的文本标注，发现出现频率最高的词——如「image」「visual」「composition」「overall」「elements」——与图像美学质量高度相关。这一观察表明，人类专家在评判艺术价值时主要关注基础视觉特征。

<!-- [原子块 · img]  -->

**EN** Figure 8: Wordcloud of ArtiMuse-10K dataset. The most frequent words in ArtiMuse-10K dataset are all highly relevant to the aesthetic assessment of images.

**ZH** 图 8：ArtiMuse-10K 数据集的词云。ArtiMuse-10K 数据集中出现最频繁的词都与图像美学评估高度相关。

**EN** Score Distributions. We divide the 10,000 images in the ArtiMuse-10K dataset into a training split (9,000 images) and a test split (1,000 images). The score distributions for both the training and test datasets are shown in Fig. 9. To compare the distribution differences across datasets, we normalize the scores of AVA [18], PARA [17], TAD66K [15], and FLICKR-AES [26] to the ⟦SLOT_6⟧ range and analyze their score distributions, with results shown in Fig. 10, Fig. 11, Fig. 12, and Fig. 13 respectively. Our analysis reveals that all aesthetic scoring datasets, including ArtiMuse, approximately follow Gaussian distributions. Notably, ArtiMuse demonstrates superior score diversity compared to other datasets.

**ZH** 分数分布。我们把 ArtiMuse-10K 数据集中的 10,000 张图像划分为训练集（9,000 张）与测试集（1,000 张），两者的分数分布如图 9 所示。为比较不同数据集间的分布差异，我们把 AVA [18]、PARA [17]、TAD66K [15] 与 FLICKR-AES [26] 的分数归一化到 ⟦SLOT_6⟧ 区间并分析其分数分布，结果分别见图 10、图 11、图 12 与图 13。分析表明，包括 ArtiMuse 在内的所有美学评分数据集都近似服从高斯分布。值得注意的是，ArtiMuse 相比其他数据集展现出更优的分数多样性。

<!-- [原子块 · object]  -->

<!-- [原子块 · object]  -->

**EN** Figure 9: Score distribution of training and test splits in ArtiMuse-10K.

**ZH** 图 9：ArtiMuse-10K 训练集与测试集的分数分布。

<!-- [原子块 · object]  -->

<!-- [原子块 · object]  -->

**EN** Figure 10: Score distribution of training and test splits in AVA.

**ZH** 图 10：AVA 训练集与测试集的分数分布。

<!-- [原子块 · object]  -->

<!-- [原子块 · object]  -->

**EN** Figure 11: Score distribution of training and test splits in PARA.

**ZH** 图 11：PARA 训练集与测试集的分数分布。

<!-- [原子块 · object]  -->

<!-- [原子块 · object]  -->

**EN** Figure 12: Score distribution of training and test splits in TAD66K.

**ZH** 图 12：TAD66K 训练集与测试集的分数分布。

<!-- [原子块 · object]  -->

<!-- [原子块 · object]  -->

**EN** Figure 13: Score distribution of training and test splits in FLICKR-AES.

**ZH** 图 13：FLICKR-AES 训练集与测试集的分数分布。

**EN** Statistical Analysis across Categories. The images in ArtiMuse-10K are sourced from diverse origins and encompass a total of 5 main categories and 15 subcategories. The detailed distribution of image counts across these categories is presented in Tab. 6.

**ZH** 跨类别统计分析。ArtiMuse-10K 中的图像来源多样，共包含 5 个大类与 15 个子类。各类别图像数量的详细分布见表 6。

**EN** Table 6: Statistics of ArtiMuse-10K across main categories and subcategories.

**ZH** 表 6：ArtiMuse-10K 在大类与子类上的统计。

<!-- [原子块 · table] Main Category Subcategory Description # Image Photography Daily Photo Casual photos capturing daily scenes 3071 Photographic Art Photos with artistic processing 758 Architecture Photos of buildings an -->

**EN** Appendix B Details of Public Dataset Collection & Processing

**ZH** 附录 B 公开数据集采集与处理的细节

**EN** We select and sample a subset of high-quality aesthetic captions from existing public datasets, with particular emphasis on ensuring both aesthetic caption quality and diversity in the sampling process. The specific sampling statistics are presented in Tab. 7.

**ZH** 我们从现有公开数据集中筛选并采样了一部分高质量美学描述，采样过程中特别注重保证美学描述的质量与多样性。具体采样统计见表 7。

**EN** Table 7: Collection & processing results of public datasets.

**ZH** 表 7：公开数据集的采集与处理结果。

<!-- [原子块 · table] Public Dataset Dataset Type Sampled Size APDDv2 [ 9 ] w / partial text caption 4,898 SPAQ [ 27 ] w / partial text caption 1,537 KonIQ-10k [ 28 ] w / partial text caption 1,488 Impressions [ 20 ] w / p -->

**EN** B.1 Datasets w/ Score Caption

**ZH** B.1 带分数描述的数据集

**EN** AVA [18], TAD66K [15], PARA [17], FLICKR-AES [26]. For datasets containing only aesthetic scores without multi-dimensional annotations, we employ the scores as the primary guidance for MLLM to generate comprehensive image evaluations. The following prompt template is adopted:

**ZH** AVA [18]、TAD66K [15]、PARA [17]、FLICKR-AES [26]。对于只含美学分数而无多维标注的数据集，我们把分数作为主要引导，让 MLLM 生成全面的图像评价。采用的提示模板如下：

<!-- [原子块 · svg]  -->

**EN** Here, <score> and <range> represents the scores and their value ranges, extracted from the dataset with score caption, serve as quantitative indicators to guide the MLLM’s image analysis process.

**ZH** 其中 <score> 与 <range> 表示从带分数描述的数据集中提取的分数及其取值范围，作为引导 MLLM 图像分析过程的量化指标。

**EN** B.2 Datasets w/ Partial Text Caption

**ZH** B.2 带部分文本描述的数据集

**EN** APDDv2 [9]. The APDDv2 dataset comprises 10,023 images, each annotated with multiple attributes, including: filename, Artistic Categories, Total aesthetic score, Theme and logic, Creativity, Layout and composition, Space and perspective, The sense of order, Light and shadow, Color, Details and texture, The overall, Mood, and Language Comment (the most critical attribute for our study). We filter out samples with excessively short or missing Language Comment entries, retaining 4,898 valid instances. For the filtered data, we design a structured prompt template:

**ZH** APDDv2 [9]。APDDv2 数据集包含 10,023 张图像，每张标注了多个属性，包括：文件名、艺术类别、美学总分、主题与逻辑、创造力、布局与构图、空间与透视、秩序感、光影、色彩、细节与质感、整体、情绪以及语言评论（本研究中最关键的属性）。我们滤除语言评论过短或缺失的样本，保留 4,898 条有效实例。针对筛选后的数据，我们设计了如下结构化提示模板：

<!-- [原子块 · svg]  -->

**EN** which incorporates key information such as the overall comment, category labels, and subcategory scores to ensure comprehensive utilization of the available annotations. Here, words enclosed in angle brackets (<>) denote referenced phrases or statements. For instance, <language_comment>, <artistic_categories>, <total_aesthetic_score>, …, and <mood> refer to the corresponding captions in the dataset, while <attribute> and <description> represent the specific attribute and its description listed in Tab. 5.

**ZH** 该模板纳入整体评论、类别标签与子类分数等关键信息，确保充分利用可用标注。这里，尖括号（<>）内的词表示被引用的短语或陈述。例如 <language_comment>、<artistic_categories>、<total_aesthetic_score>、……与 <mood> 指数据集中对应的描述，而 <attribute> 与 <description> 表示表 5 中列出的具体属性及其描述。

**EN** SPAQ [27]. The original dataset contains various image attributes, including EXIF tags, mean opinion scores (MOS), image attribute scores, and scene category labels. The SPAQ dataset comprises 11,125 images, which we filter according to two key criteria: (1) 80% of the filtered subset must have either MOS (Mean Opinion Score) or the average of four quality metrics (brightness, colorfulness, contrast, and sharpness) falling within the extreme ranges of ⟦SLOT_7⟧ or ⟦SLOT_8⟧, ensuring sufficient representation of both low and high aesthetic quality samples; (2) all selected images must contain valid entries for the "categories" attribute. From these, we select attributes relevant to visual aesthetics—specifically, MOS ratings and a subset of aesthetic-related attribute scores—and designed the following prompt template:

**ZH** SPAQ [27]。原始数据集包含多种图像属性，包括 EXIF 标签、平均意见分（MOS）、图像属性分数与场景类别标签。SPAQ 数据集包含 11,125 张图像，我们按两条关键准则筛选：（1）筛选子集中 80% 的样本，其 MOS（平均意见分）或四项质量指标（亮度、色彩丰富度、对比度、清晰度）的平均值须落在 ⟦SLOT_7⟧ 或 ⟦SLOT_8⟧ 的极端区间内，以保证低美感与高美感样本都有充分代表；（2）所有入选图像都必须含有有效的「categories」属性项。从中我们选取与视觉美学相关的属性——具体为 MOS 评分及一部分美学相关属性分数——并设计了如下提示模板：

<!-- [原子块 · svg]  -->

**EN** Here, The classification into high-degree and low-degree categories is governed by the MOS threshold: instances with MOS > 75 are designated as high-degree, while those with MOS < 25 are categorized as low-degree. The placeholders <mos>, <brightness>, <colorfulness>, …, and <categories> correspond to the respective captions from the SPAQ dataset, while <attribute> and <description> refer to the specific aesthetic attributes and their detailed descriptions as presented in Table 5.

**ZH** 这里，高程度与低程度的划分由 MOS 阈值决定：MOS > 75 者为高程度，MOS < 25 者为低程度。占位符 <mos>、<brightness>、<colorfulness>、……与 <categories> 对应 SPAQ 数据集中各自的描述，而 <attribute> 与 <description> 指表 5 中列出的具体美学属性及其详细描述。

**EN** KonIQ-10K [28]. The KonIQ-10K dataset comprises 10,000 images, from which we select the following aesthetic-relevant attributes for filtering: MOSz, brightness, contrast, colorfulness, sharpness, and quality_factor. Our filtering criteria requires that 80% of the selected images must have MOSz scores falling within either the ⟦SLOT_9⟧ or ⟦SLOT_10⟧ ranges, ensuring balanced representation of both low and high aesthetic quality samples. Through this process, we obtain 1,488 filtered images, which are then annotated by the MLLM using the following prompt template:

**ZH** KonIQ-10K [28]。KonIQ-10K 数据集包含 10,000 张图像，我们选取以下与美学相关的属性用于筛选：MOSz、亮度、对比度、色彩丰富度、清晰度与 quality_factor。筛选准则要求所选图像中 80% 的 MOSz 分数须落在 ⟦SLOT_9⟧ 或 ⟦SLOT_10⟧ 区间内，以保证低美感与高美感样本的均衡代表。通过该流程我们得到 1,488 张筛选后的图像，随后用如下提示模板交由 MLLM 标注：

<!-- [原子块 · svg]  -->

**EN** Here, The classification into high-degree and low-degree categories is governed by the MOSz threshold: instances with MOSz > 75 are designated as high-degree, while those with MOSz < 25 are categorized as low-degree. The placeholders <MOSz>, <brightness>, <contrast>, …, and <sharpness> correspond to the respective captions from the KonIQ-10K dataset, while <attribute> and <description> refer to the specific aesthetic attributes and their detailed descriptions as presented in Table 5.

**ZH** 这里，高程度与低程度的划分由 MOSz 阈值决定：MOSz > 75 者为高程度，MOSz < 25 者为低程度。占位符 <MOSz>、<brightness>、<contrast>、……与 <sharpness> 对应 KonIQ-10K 数据集中各自的描述，而 <attribute> 与 <description> 指表 5 中列出的具体美学属性及其详细描述。

**EN** Impressions [20]. The original dataset contains over 1,400 images, each accompanied by multiple annotations (including image descriptions, impressions, and aesthetic evaluations) from different annotators, resulting in more than 4,800 data entries in total. Along with these annotations, Impressions also collects detailed annotator metadata such as educational background and aesthetic experience. To ensure annotation quality, we apply the following filtering criterion: for each image, we retain only the evaluation from the most aesthetically experienced annotator. This filtering process yields a refined dataset of 1,443 high-quality annotations, which are then annotated by the MLLM using the following prompt template:

**ZH** Impressions [20]。原始数据集包含 1,400 余张图像，每张配有多位标注者给出的多种标注（包括图像描述、印象与美学评价），总计超过 4,800 条数据。除这些标注外，Impressions 还收集了详细的标注者元信息，如教育背景与美学经验。为保证标注质量，我们采用如下筛选准则：对每张图像，只保留美学经验最丰富的标注者给出的评价。该筛选流程得到 1,443 条高质量标注，随后用如下提示模板交由 MLLM 标注：

<!-- [原子块 · svg]  -->

**EN** Here, the placeholders <caption>, <image_description>, <image_impression>, and <image_aesthetic_eval> correspond to the respective captions from the Impressions dataset, while <attribute> and <description> refer to the specific aesthetic attributes and their detailed descriptions as presented in Table 5.

**ZH** 这里，占位符 <caption>、<image_description>、<image_impression> 与 <image_aesthetic_eval> 对应 Impressions 数据集中各自的描述，而 <attribute> 与 <description> 指表 5 中列出的具体美学属性及其详细描述。

**EN** Appendix C Details of Token As Score Strategy

**ZH** 附录 C Token As Score 策略的细节

**EN** We conducted a comprehensive comparison of various score prediction strategies, and the experimental results are presented in Tab. 10. Across all experiments, the prediction score methodology was the sole differentiating factor, while the training data, training configurations, and model architecture remained consistent. To ensure robust and reliable experimental conclusions, we conduct comprehensive evaluations on both AVA (the largest image aesthetics scoring dataset) [18] and ArtiMuse-10K (ours).

**ZH** 我们对各种分数预测策略做了全面比较，实验结果见表 10。所有实验中，分数预测方法是唯一的变量，训练数据、训练配置与模型架构保持一致。为保证实验结论稳健可靠，我们在 AVA（规模最大的图像美学评分数据集）[18] 与 AriMuse-10K（本文所提数据集）上分别做了全面评测。

**EN** C.1 Level As Score

**ZH** C.1 Level As Score

**EN** Following Q-Align [12], we predict scores by predicting five distinct discrete levels. Specifically, during training, we convert the continuous scores in the dataset into corresponding levels based on a predefined mapping and train the model to predict these discrete levels. This mapping scheme involves uniformly dividing the range between the maximum score (M) and the minimum score (m) into five distinct intervals, with scores within each interval being assigned to a corresponding discrete level:

**ZH** 沿用 Q-Align [12]，我们通过预测五个不同的离散等级来预测分数。具体地，训练时依据预定义映射把数据集中的连续分数转换为相应等级，并训练模型预测这些离散等级。该映射方案把最高分（M）与最低分（m）之间的区间均匀划分为五个区间，落在各区间内的分数被赋予对应的离散等级：

<!-- [原子块 · table] L ⁡ ( s ) = l i ​ if ​ m + i − 1 5 × ( M − m ) < s ≤ m + i 5 × ( M − m ) L(s)=l_{i}\text{ if }m+\frac{i-1}{5}\times(M-m)<s\leq m+\frac{i}{5}\times(M-m) (1) -->

**EN** where

**ZH** 其中

<!-- [原子块 · table] { l i } i = 1 5 = { bad, poor, fair, good, excellent } \{l_{i}\}_{i=1}^{5}=\{\text{bad, poor, fair, good, excellent}\} (2) -->

**EN** which are the standard text rating levels as defined by ITU [41]. During inference, the final score prediction was derived by computing a weighted sum of the predicted probability distribution across these five levels.

**ZH** 即 ITU [41] 定义的标准文本评级等级。推理时，最终分数预测由这五个等级的预测概率分布加权求和得到。

**EN** Discussions. The comparison between Exp. (a) and (i) in Tab. 10, along with other experimental groups, demonstrates that the Level As Score approach exhibits a significant performance degradation compared to the Token As Score. This decline can be attributed to the overly coarse-grained level partitioning scheme, which fails to achieve fine-grained score mapping. Furthermore, the adopted vocabulary lacks proper alignment with the LLM’s lexical table design, collectively contributing to the suboptimal outcomes.

**ZH** 讨论。表 10 中实验 (a) 与 (i) 以及其他实验组的对比表明，Level As Score 相比 Token As Score 有明显性能下降。这一下滑可归因于等级划分方案过于粗粒度，无法实现细粒度的分数映射；此外所采用的词表与 LLM 的词表设计缺乏恰当对齐，共同导致了次优结果。

**EN** C.2 Token As Score w/ Expanding Tokens

**ZH** C.2 扩展词元的 Token As Score

**EN** We provide a detailed exposition of the Token As Score strategy, as referenced in the Sec. 4.3, Score Finetune of the main paper. In this investigation, we explore the expansion of the LLM vocabulary by incorporating additional tokens specifically for aesthetics score prediction. For instance, in the "Expanding 25 Tokens" configuration, we augment the vocabulary with the following tokens: [AES_SCORE_TOKEN_0], [AES_SCORE_TOKEN_1], [AES_SCORE_TOKEN_2], …, [AES_SCORE_TOKEN_25]. These tokens correspond to predicted scores of 0, 4, 8, …, 100, respectively. The model is trained to predict these specialized tokens, and during inference, the final aesthetic score is derived by computing a weighted sum based on the predicted probability distribution over these tokens.

**ZH** 我们对第 4.3 节「分数微调」中提到的 Token As Score 策略做详细阐述。在这项考察中，我们探索通过为美学分数预测专门引入额外词元来扩展 LLM 词表。例如在「扩展 25 个词元」配置下，我们向词表加入以下词元：[AES_SCORE_TOKEN_0]、[AES_SCORE_TOKEN_1]、[AES_SCORE_TOKEN_2]、……、[AES_SCORE_TOKEN_25]。这些词元分别对应 0、4、8、……、100 的预测分数。模型被训练为预测这些专用词元，推理时最终美学分数由这些词元的预测概率分布加权求和得到。

**EN** Discussions. A comparison of experiments (b)-(f) on AVA reveals that the performance of the Token As Score strategy initially improves and then declines as the number of introduced tokens increases, peaking at 100 tokens. This trend occurs because an insufficient number of tokens fails to establish an accurate token-score mapping, while an excessive number exceeds the available data or model capacity, leading to underfitting. Experimental results on ArtiMuse-10K demonstrate that the Token As Score approach with expanding tokens performs poorly, suggesting this method fails to converge properly when either the dataset is inherently challenging or insufficient in size.

**ZH** 讨论。在 AVA 上比较实验 (b)-(f) 可见，随着引入词元数量增加，Token As Score 策略的性能先升后降，在 100 个词元时达到峰值。出现这一趋势的原因是：词元数量不足无法建立准确的词元—分数映射，而数量过多则超出可用数据或模型容量，导致欠拟合。在 ArtiMuse-10K 上的实验结果表明，采用扩展词元的 Token As Score 表现不佳，说明该方法在数据集本身难度较大或规模不足时难以正常收敛。

**EN** C.3 Token As Score w/ Existing Tokens

**ZH** C.3 基于已有词元的 Token As Score

**EN** We futher explore the selection of a subset of the LLM’s existing displayable tokens for aesthetics score prediction. Our selection criteria prioritize brevity, inherent order, ease of convergence during training, and minimal ambiguity with numerical scores. As illustrated in Tab. 10, our specific configurations in experiments are as follows:

**ZH** 我们进一步探索从 LLM 已有的可显示词元中选取子集用于美学分数预测。选取准则优先考虑简洁性、内在顺序性、训练中易于收敛，以及与数值分数的歧义最小。如表 10 所示，我们在实验中的具体配置如下：

**EN** Existing 25 Tokens. We select the tokens a, b, c, … , y, which are sequentially mapped to scores ranging from 0 to 100 with an interval of 4 (i.e., 0, 4, 8, …, 100).

**ZH** 已有 25 个词元。我们选取词元 a、b、c、……、y，依次映射到 0 到 100、间隔为 4 的分数（即 0、4、8、……、100）。

**EN** Existing 50 Tokens. We select the tokens a, b, c, … , y, A, B, C, … , Y, which are sequentially mapped to scores ranging from 0 to 100 with an interval of 2 (i.e., 0, 2, 4, …, 100).

**ZH** 已有 50 个词元。我们选取词元 a、b、c、……、y、A、B、C、……、Y，依次映射到 0 到 100、间隔为 2 的分数（即 0、2、4、……、100）。

**EN** Existing 100 Tokens (non-ordered). We select the first 100 character tokens starting from 0 within the vocabulary of the Qwen2.5-7B LLM, as detailed in Tab. 8. These tokens are sequentially mapped to scores from 0 to 100.

**ZH** 已有 100 个词元（无序）。我们从 Qwen2.5-7B LLM 词表中选取自 0 开始的前 100 个字符词元，详见表 8。这些词元依次映射到 0 到 100 的分数。

**EN** Table 8: Token-score mapping table for existing 100 tokens (non-ordered).

**ZH** 表 8：已有 100 个词元（无序）的词元—分数映射表。

<!-- [原子块 · table] Token ID 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 Token 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C Score 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 -->

<!-- [原子块 · table] Token ID 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 Token D E F G H I J K L M N O P Q R S T U V W Score 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 -->

<!-- [原子块 · table] Token ID 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 Token X Y Z [ \ ] ˆ _ ` a b c d e f g h i j k Score 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 -->

<!-- [原子块 · table] Token ID 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 Token l m n o p q r s t u v w x y z { | | } ~ ¡ Score 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 -->

<!-- [原子块 · table] Token ID 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 Token ¢ £ ¤ ¥ ¦ § ¨ © ª « ¬ ® ¯ ° ± ² ³ ´ µ ¶ · Score 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 9 -->

**EN** Existing 100 Tokens (ordered). This represents the final approach adopted in ArtiMuse. We construct 100 tokens by concatenating lowercase letters, ensuring these tokens are ordered within the vocabulary of the Qwen2.5-7B LLM, as presented in Tab. 9. These tokens are sequentially mapped to scores from 0 to 100.

**ZH** 已有 100 个词元（有序）。这是 ArtiMuse 最终采用的方案。我们通过拼接小写字母构造出 100 个词元，并确保这些词元在 Qwen2.5-7B LLM 词表中是有序的，如表 9 所示。这些词元依次映射到 0 到 100 的分数。

**EN** Table 9: Token-score mapping table for existing 100 tokens (ordered), which is used in ArtiMuse.

**ZH** 表 9：已有 100 个词元（有序）的词元—分数映射表，ArtiMuse 采用该表。

<!-- [原子块 · table] Token aa ab ac ad ae af ag ah ai aj ak al am an ao ap aq ar as at Score 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 -->

<!-- [原子块 · table] Token au av aw ax ay az ca cb cc cd ce cf cg ch ci cj ck cl cm cn Score 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 -->

<!-- [原子块 · table] Token co cp cq cr cs ct cu cv cw cx cy da db dc dd de df dg dh di Score 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 -->

<!-- [原子块 · table] Token dj dk dl dm dn do dp dq dr ds dt du dv dw dx dy ea eb ec ed Score 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 -->

<!-- [原子块 · table] Token ee ef eg eh ei ej ek el em en eo ep eq er es et eu ev ew ex ey Score 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 -->

**EN** Discussions. The comparisons in (b)-(g), (c)-(h), and (d)-(j) demonstrate that when using the same number of tokens for prediction in the Token As Score, tokens from the existing vocabulary consistently yield better performance. This occurs because newly introduced tokens lack corresponding prior knowledge from the model’s pretraining phase and do not possess inherent ordinal relationships with scores, making them less effective than tokens in the LLM vocabulary that carry clear semantic information and sequential relationships.

**ZH** 讨论。(b)-(g)、(c)-(h) 与 (d)-(j) 的对比表明，在 Token As Score 中使用相同数量的词元做预测时，来自已有词表的词元始终取得更好的性能。原因在于：新引入的词元在模型预训练阶段缺乏相应的先验知识，与分数之间也不具备内在的序数关系，因而不如 LLM 词表中那些携带明确语义信息与顺序关系的词元有效。

**EN** Furthermore, experiments (g), (h), and (j) reveal that when using existing tokens for Token As Score, model performance improves significantly as the number of tokens increases. Due to the limited number of displayable characters in the Qwen2.5-7B LLM vocabulary, we are currently unable to further increase this quantity, which will be explored in future work. Additionally, comparing (i) and (j) shows that the choice of tokens also affects performance—the token mapping scheme in (j), which has more explicit semantic and ordinal relationships, leads to better results.

**ZH** 此外，实验 (g)、(h) 与 (j) 表明，在使用已有词元做 Token As Score 时，模型性能随词元数量增加而显著提升。受 Qwen2.5-7B LLM 词表中可显示字符数量所限，我们目前无法进一步增加这一数量，将留待未来工作探索。另外，(i) 与 (j) 的对比说明词元的选择同样会影响性能——(j) 的词元映射方案具有更明确的语义与序数关系，因而结果更好。

**EN** Table 10: Explorations on score prediction strategies. To ensure experimental validity, we conduct our experiments both on the AVA dataset and AriMuse-10K dataset. (j) represents the setting of Token As Score strategy in ArtiMuse. Beyond the convergence issues observed with the expanding strategy on ArtiMuse-10K, the 100-token configuration demonstrates peak performance across various token quantities.

**ZH** 表 10：分数预测策略的探索。为保证实验有效性，我们在 AVA 数据集与 AriMuse-10K 数据集上均开展了实验。(j) 表示 ArtiMuse 中 Token As Score 策略的设置。除了扩展策略在 ArtiMuse-10K 上出现的收敛问题外，100 词元配置在各种词元数量中均展现出峰值性能。

<!-- [原子块 · table] Exp. Score Prediction AVA [ 18 ] ArtiMuse-10K SRCC PLCC SRCC PLCC (a) 5 Levels 0.820 0.818 0.571 0.551 (b) Expanding 25 Tokens 0.803 0.665 0.045 0.055 (c) Expanding 50 Tokens 0.822 0.821 0.018 0.027 ( -->

**EN** Appendix D Implementation Details

**ZH** 附录 D 实现细节

**EN** D.1 Training Details

**ZH** D.1 训练细节

**EN** Hyperparameters. We employ the InternVL-3-8B [10] model as our base model and adopt its default hyperparameters for the aesthetic assessment task through two training stages: Text Pretrain and Score Finetune. The pre-trained models and specific hyperparameter configurations are detailed in Table 11, with modifications carefully designed to address the unique requirements of visual aesthetic evaluation.

**ZH** 超参数。我们采用 InternVL-3-8B [10] 模型作为基座模型，并沿用其默认超参数，通过文本预训练与分数微调两个训练阶段完成美学评估任务。预训练模型与具体超参数配置详见表 11，其中的改动都经过精心设计，以适应视觉美学评估的特殊要求。

**EN** Table 11: Pre-trained models and hyperparameters used for ArtiMuse, including text pretraining and score finetuning.

**ZH** 表 11：ArtiMuse 使用的预训练模型与超参数，包括文本预训练与分数微调两部分。

<!-- [原子块 · table] Pre-trained models / Hyperparameters Text Pretrain Score Finetune Vison Encoder InternViT-300M-448px-V2.5 InternViT-300M-448px-V2.5 Large Language Model Qwen2.5-7B Qwen2.5-7B Large Language Model LoRA -->

**EN** Resolution Strategy. The original InternVL-3 model employs a dynamic high-resolution strategy [10] to handle images of varying resolutions and attribute ratios. This approach involves three key steps: closest attribute ratio matching, image resizing and splitting, and optional thumbnail generation. Given an input image with dimensions ⟦SLOT_11⟧, the aspect ratio ⟦SLOT_12⟧ is computed. The algorithm selects a target aspect ratio ⟦SLOT_13⟧ from a predefined set ⟦SLOT_14⟧, which minimizes distortion while constraining the number of tiles ⟦SLOT_15⟧ within a range ⟦SLOT_16⟧. The image is resized to dimensions ⟦SLOT_17⟧ (where ⟦SLOT_18⟧) and split into ⟦SLOT_19⟧ tiles of size ⟦SLOT_20⟧. If ⟦SLOT_21⟧, a thumbnail of size ⟦SLOT_22⟧ is appended to preserve a global view.

**ZH** 分辨率策略。原始 InternVL-3 模型采用动态高分辨率策略 [10] 来处理不同分辨率与宽高比的图像。该策略包含三个关键步骤：最接近宽高比匹配、图像缩放与切分、以及可选的缩略图生成。给定尺寸为 ⟦SLOT_11⟧ 的输入图像，计算宽高比 ⟦SLOT_12⟧。算法选择目标宽高比 ⟦SLOT_13⟧，其取自预定义集合 ⟦SLOT_14⟧，在使失真最小的同时把分块数 ⟦SLOT_15⟧ 约束在 ⟦SLOT_16⟧ 范围内。图像被缩放至 ⟦SLOT_17⟧（其中 ⟦SLOT_18⟧）并切分为 ⟦SLOT_19⟧ 个大小为 ⟦SLOT_20⟧ 的分块。若 ⟦SLOT_21⟧，则追加一张大小为 ⟦SLOT_22⟧ 的缩略图以保留全局视图。

**EN** However, in ArtiMuse, we adopt a fixed-resolution strategy instead of the dynamic approach. Aesthetic evaluation relies heavily on holistic image features, such as composition, color harmony, and spatial relationships, which can be disrupted by splitting an image into localized tiles. The dynamic strategy’s tile-based processing risks fragmenting these global characteristics, thereby degrading performance in tasks requiring an integrated understanding of visual aesthetics. By resizing all images to a uniform resolution without tiling, we preserve the structural and semantic coherence of the entire image. This adjustment ensures that the model captures aesthetic qualities through a consistent, undistorted representation of the input, aligning better with the requirements of fine-grained aesthetic analysis. Our experiments demonstrate that employing the fixed-resolution strategy yields approximately 0.3 improvements in both SRCC and PLCC metrics for aesthetic scoring tasks compared to the dynamic high-resolution strategy, while simultaneously more than doubling training and inference efficiency.

**ZH** 然而在 ArtiMuse 中，我们采用固定分辨率策略而非动态策略。美学评估高度依赖构图、色彩和谐、空间关系等整体性图像特征，而把图像切分为局部小块会破坏这些特征。动态策略基于分块的处理方式有可能割裂这些全局特性，从而在需要整体理解视觉美学的任务上降低性能。通过把所有图像缩放到统一分辨率而不做切分，我们保留了整幅图像在结构与语义上的连贯性。这一调整确保模型通过一致、无失真的输入表示来捕捉美学特质，更契合细粒度美学分析的要求。我们的实验表明，在美学评分任务上，采用固定分辨率策略相比动态高分辨率策略可使 SRCC 与 PLCC 指标各提升约 0.3，同时把训练与推理效率提高一倍以上。

**EN** D.2 Inference Details for Aesthetics Scoring

**ZH** D.2 美学评分的推理细节

**EN** We present the implementation details for various models in the aesthetic scoring task. Note that certain models—including TANet [15], AesMamba [8], UNIAA-LLaVA [25], and Next Token Is Enough [33]—are excluded from this discussion due to testing constraints.

**ZH** 我们给出美学评分任务中各模型的实现细节。需注意，受测试条件限制，TANet [15]、AesMamba [8]、UNIAA-LLaVA [25] 与 Next Token Is Enough [33] 等模型不在此讨论范围内。

**EN** Models w/ Scoring Ability. For models capable of generating aesthetic scores (Q-Instruct [39], PEAS [40], Q-Align [12]), we directly utilize their scoring outputs. In cases where a model provides only general assessments (MUSIQ [35]), we adopt its general score as the final evaluation result.

**ZH** 具备评分能力的模型。对于能够生成美学分数的模型（Q-Instruct [39]、PEAS [40]、Q-Align [12]），我们直接采用其评分输出。若某模型只提供通用评估（MUSIQ [35]），我们采用其通用分数作为最终评测结果。

**EN** Models w/o Scoring Ability. For models lacking inherent scoring capabilities (VILA [36], mPLUG-Owl2 [37], ShareGPT-4V [38], Qwen-2.5-VL-7B [11], InternVL3-8B [10]), we employ carefully designed prompts to elicit numerical evaluations. The prompt structure is as follows:

**ZH** 不具备评分能力的模型。对于本身不具备评分能力的模型（VILA [36]、mPLUG-Owl2 [37]、ShareGPT-4V [38]、Qwen-2.5-VL-7B [11]、InternVL3-8B [10]），我们精心设计提示以引出数值评价。提示结构如下：

<!-- [原子块 · svg]  -->

**EN** This prompt guides the model to output an integer score from 0 to 100, aligning with ArtiMuse’s scoring format. We use these prompted scores for comparative analysis, ensuring consistency across all evaluated models.

**ZH** 该提示引导模型输出 0 到 100 的整数分数，与 ArtiMuse 的评分格式保持一致。我们使用这些提示得到的分数进行比较分析，以保证所有参评模型之间的一致性。

**EN** D.3 Inference Details for Textual Analysis

**ZH** D.3 文本分析的推理细节

**EN** When evaluating the model’s textual analysis capability, we design specialized prompts for comparative models by incorporating relevant aesthetic background knowledge to ensure fairness. Specifically, for ArtiMuse, we employ the following prompt format during testing:

**ZH** 在评测模型的文本分析能力时，我们为对比模型设计了专门的提示，并引入相关美学背景知识以保证公平。具体地，对 ArtiMuse，测试时采用如下提示格式：

<!-- [原子块 · svg]  -->

**EN** where <attribute> represents the specific attribute listed in Tab. 5. For other models, we augment their inputs with corresponding attribute descriptions to maintain parity in contextual understanding:

**ZH** 其中 <attribute> 表示表 5 中列出的具体属性。对其他模型，我们在其输入中补充相应的属性描述，以保持上下文理解上的对等：

<!-- [原子块 · svg]  -->

**EN** where <attribute> and <description> represent the specific attribute and its description listed in Tab. 5. Additional textual evaluation results and analysis are presented in Section E.5.

**ZH** 其中 <attribute> 与 <description> 表示表 5 中列出的具体属性及其描述。更多文本评测结果与分析见第 E.5 节。

**EN** D.4 Comparison Details

**ZH** D.4 对比细节

**EN** Judging by MLLM. We provide a detailed explanation of the methodology employed in Sec. 5.2 of the main paper for using MLLMs to select among different models’ structural aesthetic analysis results. As illustrated in Fig. 14, we first determine the input image and the corresponding aesthetic attributes, then guide the MLLM to generate textual evaluations using the following prompt template:

**ZH** 由 MLLM 评判。我们详细说明正文第 5.2 节中用 MLLM 在多个模型的结构化美学分析结果之间做选择的方法。如图 14 所示，我们先确定输入图像与相应的美学属性，再用如下提示模板引导 MLLM 生成文本评价：

<!-- [原子块 · svg]  -->

**EN** where <attribute> corresponds to the specific aesthetic attributes listed in Tab. 5. For human experts, we also provide the attribute and invite them to provide textual evaluations. The image, attribute, expert evaluations, and the outputs from different models are then fed into a judgment MLLM (specifically, Gemini-2.0-flash) for assessment. We guide this MLLM to evaluate and select the highest-quality responses among the model outputs using a single-choice question format prompt (Taking 4 models as an example):

**ZH** 其中 <attribute> 对应表 5 中列出的具体美学属性。对人类专家，我们同样提供属性并请他们给出文本评价。随后，图像、属性、专家评价以及各模型的输出被一并送入一个裁判 MLLM（具体为 Gemini-2.0-flash）进行评判。我们引导该 MLLM 以单选提问形式的提示，在各模型输出中评估并选出质量最高的回答（以 4 个模型为例）：

<!-- [原子块 · svg]  -->

**EN** which minimizes hallucinations, provides sufficient information for decision-making, and ensures consistent evaluation criteria across all model responses, thereby yielding relatively accurate and stable selection outcomes. The results is presented in Tab. 2 of the main paper.

**ZH** 这一方式既能减少幻觉，又为决策提供了充分信息，并保证所有模型回答采用一致的评判标准，从而得到较为准确、稳定的选择结果。结果见正文表 2。

<!-- [原子块 · img]  -->

**EN** Figure 14: Pipeline of the structural aesthetic analysis ability judgment by MLLM.

**ZH** 图 14：由 MLLM 评判结构化美学分析能力的流水线。

**EN** Judging by Human. For the user study, we randomly select 20 images from the ArtiMuse-10K test set, ensuring coverage across different categories and varying aesthetic qualities. Each image is evaluated by different models across 8 aesthetic attributes, with their outputs recorded. We compile these results into 20 multiple-choice questions, where each question corresponds to one image and the model-generated evaluations for a specific attribute, supplemented by a detailed description of that attribute for context. We recruit 20 volunteers, including both individuals without formal training and those with extensive aesthetic evaluation experience, to participate in the study. Their selections are collected, and the preference rates for each model are computed. The results are presented in Tab. 2 of the main paper.

**ZH** 由人类评判。在用户研究中，我们从 ArtiMuse-10K 测试集中随机选取 20 张图像，确保覆盖不同类别与不同美学质量。每张图像由各模型就 8 个美学属性给出评价并记录输出。我们把这些结果编制成 20 道选择题，每题对应一张图像及某个特定属性上模型生成的评价，并附上该属性的详细描述作为背景。我们招募了 20 名志愿者参与研究，其中既有未受专业训练者，也有具备丰富美学评估经验者。收集他们的选择后，计算各模型的偏好率。结果见正文表 2。

**EN** Appendix E More Results

**ZH** 附录 E 更多结果

**EN** E.1 Comparison with SOTA Open-Source & Closed-Source MLLMs

**ZH** E.1 与当前最优开源及闭源 MLLM 的对比

**EN** We benchmark ArtiMuse against state-of-the-art multimodal large language models (MLLMs), including both open-source (Qwen-2.5-VL-72B-instruct [11] and InternVL3-78B [10]) and closed-source models (GPT-4o [13] and Gemini-2.0-Flash [14]). As shown in Tab. 12, closed-source models generally outperform open-source models. Notably, ArtiMuse achieves significantly higher performance in aesthetics scoring than these leading MLLMs despite having only 8B parameters, demonstrating its exceptional capability in image aesthetic assessment.

**ZH** 我们把 ArtiMuse 与当前最优的多模态大语言模型（MLLM）做基准对比，包括开源模型（Qwen-2.5-VL-72B-instruct [11] 与 InternVL3-78B [10]）与闭源模型（GPT-4o [13] 与 Gemini-2.0-Flash [14]）。如表 12 所示，闭源模型总体优于开源模型。值得注意的是，尽管 ArtiMuse 只有 8B 参数，其在美学评分上的性能仍显著高于这些领先 MLLM，展现出卓越的图像美学评估能力。

**EN** Table 12: More comparison on aesthetics scoring. The best and second-best performances are highlighted in red and blue, respectively. ArtiMuse demonstrates superior performance when compared to various state-of-the-art open-source & closed-source MLLMs.

**ZH** 表 12：美学评分的更多对比。最优与次优性能分别以红色与蓝色标出。与各类当前最优开源及闭源 MLLM 相比，ArtiMuse 展现出更优性能。

<!-- [原子块 · table] Model AVA [ 18 ] PARA [ 17 ] TAD66K [ 15 ] FLICKR-AES [ 26 ] ArtiMuse-10K SRCC PLCC SRCC PLCC SRCC PLCC SRCC PLCC SRCC PLCC Comparison with SOTA Open-Source & Closed-Source MLLMs Qwen-2.5-VL-72B-instr -->

**EN** E.2 Further Comparison of Generalization Ability

**ZH** E.2 泛化能力的进一步对比

**EN** We further experimentally validate ArtiMuse’s generalization ability through comprehensive cross-dataset evaluations. As shown in Tab. 13, we train both the state-of-the-art open-source IAA model Q-Align [12] and ArtiMuse on AVA [18], PARA [17], TAD66K [15], FLICKR-AES [26], and ArtiMuse-10K, then evaluate them across all five datasets. The results demonstrate that ArtiMuse consistently outperforms Q-Align on unseen datasets in most cases, confirming its superior generalization capability.

**ZH** 我们通过全面的跨数据集评测进一步验证 ArtiMuse 的泛化能力。如表 13 所示，我们把当前最优的开源 IAA 模型 Q-Align [12] 与 ArtiMuse 分别在 AVA [18]、PARA [17]、TAD66K [15]、FLICKR-AES [26] 与 ArtiMuse-10K 上训练，然后在全部五个数据集上评测。结果表明，在未见数据集上 ArtiMuse 多数情况下始终优于 Q-Align，印证了其更强的泛化能力。

**EN** Table 13: Further comparison of generalization ability. The best performances are highlighted in red. * Results are trained only on single dataset to compare the generalization ability. ArtiMuse demonstrates strong generalization capabilities when compared to state-of-the-art IAA models.

**ZH** 表 13：泛化能力的进一步对比。最优性能以红色标出。* 结果仅在单一数据集上训练，用于比较泛化能力。与当前最优 IAA 模型相比，ArtiMuse 展现出强大的泛化能力。

<!-- [原子块 · table] Model AVA [ 18 ] PARA [ 17 ] TAD66K [ 15 ] FLICKR-AES [ 26 ] ArtiMuse-10K SRCC PLCC SRCC PLCC SRCC PLCC SRCC PLCC SRCC PLCC Further Comparison of Generalization Ability Q-Align (AVA) * 0.822 0.817 0.6 -->

**EN** E.3 Image Examples in ArtiMuse-10K

**ZH** E.3 ArtiMuse-10K 中的图像示例

**EN** As illustrated in Fig. 15, Fig. 16 and Fig. 17, the ArtiMuse-10K dataset includes a diverse collection of images, meticulously organized across all specified subcategories. The dataset encompasses a wide range of aesthetic qualities and sources, ensuring rich variability and broad representativeness.

**ZH** 如图 15、图 16 与图 17 所示，ArtiMuse-10K 数据集包含多样的图像集合，按所有指定子类精心组织。该数据集涵盖范围广泛的美学质量与来源，保证了丰富的变异性与广泛的代表性。

**EN** E.4 Complete Examples in ArtiMuse-10K

**ZH** E.4 ArtiMuse-10K 中的完整示例

**EN** In ArtiMuse-10K, professional experts meticulously evaluate each image across eight aesthetic attributes, providing detailed textual assessments along with an overall aesthetics score. Here, we present the complete data examples form each main categories in the dataset, including Photography, Painting & Calligraphy, AIGC, 3D Design and Graphic Design, as shown in Fig. 19, Fig. 20, Fig. 21, Fig. 22, Fig. 23, Fig. 24, and Fig. 25.

**ZH** 在 ArtiMuse-10K 中，专业专家沿八个美学属性对每张图像做细致评估，给出详细的文本评价与整体美学分数。这里我们给出数据集中各主要类别的完整数据示例，包括摄影、绘画与书法、AIGC、三维设计与平面设计，如图 19、图 20、图 21、图 22、图 23、图 24 与图 25 所示。

**EN** E.5 Further Comparison of Textual Analysis

**ZH** E.5 文本分析的进一步对比

**EN** We provide comprehensive examples of ArtiMuse’s structural aesthetic analysis on images, accompanied by expert commentary and comparative evaluations with other models, as illustrated in Fig. 26, Fig. 27, and Fig. 28. All images used in this analysis are sourced from the ArtiMuse-10K test set.

**ZH** 我们给出 ArtiMuse 对图像做结构化美学分析的完整示例，配以专家点评以及与其他模型的对比评价，如图 26、图 27 与图 28 所示。本分析所使用的全部图像均取自 ArtiMuse-10K 测试集。

**EN** E.6 Results on Real-world Images

**ZH** E.6 真实场景图像上的结果

**EN** To evaluate ArtiMuse’s capability in processing out-of-distribution images, we employed real-world images for testing. As demonstrated in Fig. 29, Fig. 30 and Fig. 31, our model maintains accurate and expert-level analysis even when handling real-world scenarios. The results showcase ArtiMuse’s ability to provide professional aesthetic assessments, systematically identifying both strengths and weaknesses based on detailed visual characteristics.

**ZH** 为评估 ArtiMuse 处理分布外图像的能力，我们采用真实场景图像进行测试。如图 29、图 30 与图 31 所示，即便面对真实场景，本文模型仍能保持准确、专家级的分析。结果展示了 ArtiMuse 提供专业美学评估的能力，能依据细粒度视觉特征系统地识别优缺点。

<!-- [原子块 · img]  -->

**EN** Figure 15: Image examples from the Photography category in ArtiMuse-10K dataset.

**ZH** 图 15：ArtiMuse-10K 数据集中摄影类别的图像示例。

<!-- [原子块 · img]  -->

**EN** Figure 16: Image examples from the Painting & Calligraphy category in ArtiMuse-10K dataset.

**ZH** 图 16：ArtiMuse-10K 数据集中绘画与书法类别的图像示例。

<!-- [原子块 · img]  -->

**EN** Figure 17: Image examples from the AIGC, 3D Design and Graphic Design categories in ArtiMuse-10K dataset.

**ZH** 图 17：ArtiMuse-10K 数据集中 AIGC、三维设计与平面设计类别的图像示例。

<!-- [原子块 · img]  -->

**EN** Figure 18: High-aesthetic example from Photography category.

**ZH** 图 18：摄影类别的高美感示例。

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

**EN** Figure 19: Medium-aesthetic example and low-aesthetic example from Photography category.

**ZH** 图 19：摄影类别的中等美感示例与低美感示例。

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

**EN** Figure 20: High-aesthetic and medium-aesthetic example from Painting & Calligraphy category.

**ZH** 图 20：绘画与书法类别的高美感示例与中等美感示例。

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

**EN** Figure 21: Low-aesthetic example from Painting & Calligraphy category and high-aesthetic example from AIGC category.

**ZH** 图 21：绘画与书法类别的低美感示例与 AIGC 类别的高美感示例。

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

**EN** Figure 22: Medium-aesthetic example and low-aesthetic example from AIGC category.

**ZH** 图 22：AIGC 类别的中等美感示例与低美感示例。

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

**EN** Figure 23: High-aesthetic and medium-aesthetic example from 3D Design category.

**ZH** 图 23：三维设计类别的高美感示例与中等美感示例。

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

**EN** Figure 24: Low-aesthetic example from 3D Design category and high-aesthetic example from Graphic Design category.

**ZH** 图 24：三维设计类别的低美感示例与平面设计类别的高美感示例。

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

**EN** Figure 25: Medium-aesthetic example and low-aesthetic example from Graphic Design category.

**ZH** 图 25：平面设计类别的中等美感示例与低美感示例。

<!-- [原子块 · img]  -->

**EN** Figure 26: Structural aesthetic analysis results and comparisons on AIGC images from ArtiMuse-10K test set. Red and green denote positive and negative analyses, respectively. ArtiMuse demonstrates superior performance in identifying flaws in low-aesthetic AIGC images, achieving higher accuracy than competing models and closely aligning with expert human evaluations.

**ZH** 图 26：ArtiMuse-10K 测试集中 AIGC 图像的结构化美学分析结果与对比。红色与绿色分别表示正面与负面分析。ArtiMuse 在识别低美感 AIGC 图像缺陷方面表现更优，准确率高于对比模型，并与人类专家评价高度吻合。

<!-- [原子块 · img]  -->

**EN** Figure 27: Structural aesthetic analysis results and comparisons on photographic images from ArtiMuse-10K test set. Red and green denote positive and negative analyses, respectively. ArtiMuse demonstrates superior performance in identifying flaws in low-aesthetic photographic images, achieving higher accuracy than competing models and closely aligning with expert human evaluations.

**ZH** 图 27：ArtiMuse-10K 测试集中摄影图像的结构化美学分析结果与对比。红色与绿色分别表示正面与负面分析。ArtiMuse 在识别低美感摄影图像缺陷方面表现更优，准确率高于对比模型，并与人类专家评价高度吻合。

<!-- [原子块 · img]  -->

**EN** Figure 28: Structural aesthetic analysis results and comparisons on paintings from ArtiMuse-10K test set. Brown denote expert-level analyses. ArtiMuse demonstrates superior technical analysis capabilities for high-aesthetic images, exhibiting higher accuracy than competing models and achieving near-expert-level performance in aesthetic evaluation.

**ZH** 图 28：ArtiMuse-10K 测试集中绘画图像的结构化美学分析结果与对比。棕色表示专家级分析。ArtiMuse 对高美感图像展现出更强的技术分析能力，准确率高于对比模型，在美学评估上达到接近专家的水平。

<!-- [原子块 · img]  -->

**EN** Figure 29: Textual results of ArtiMuse on real-world images. Red and green denote positive and negative analyses, respectively. ArtiMuse delivers expert-level image analysis, offering accurate evaluations of both strengths and weaknesses.

**ZH** 图 29：ArtiMuse 在真实场景图像上的文本结果。红色与绿色分别表示正面与负面分析。ArtiMuse 提供专家级图像分析，对优缺点给出准确评价。

<!-- [原子块 · img]  -->

**EN** Figure 30: Textual results of ArtiMuse on real-world images. Brown denote expert-level analyses. ArtiMuse is capable of generating expert-level, granular assessments of visual content.

**ZH** 图 30：ArtiMuse 在真实场景图像上的文本结果。棕色表示专家级分析。ArtiMuse 能够对视觉内容生成专家级、细粒度的评估。

<!-- [原子块 · img]  -->

**EN** Figure 31: Textual results of ArtiMuse on real-world images. Red and green denote positive and negative analyses, respectively. ArtiMuse delivers expert-level image analysis, offering accurate evaluations of both strengths and weaknesses.

**ZH** 图 31：ArtiMuse 在真实场景图像上的文本结果。红色与绿色分别表示正面与负面分析。ArtiMuse 提供专家级图像分析，对优缺点给出准确评价。
