# UNIAA：统一的多模态图像美学评估基线与基准

> 原标题：UNIAA: A Unified Multi-modal Image Aesthetic Assessment Baseline and Benchmark
> 作者：Zhaokun Zhou, Qiulin Wang, Bin Lin, Yiwei Su, Rui Chen, Xin Tao, Amin Zheng, Li Yuan, Pengfei Wan, Di Zhang · arXiv:2404.09619 · 2024-04-15

<!-- [原子块 · verbatim] UNIAA: A Unified Multi-modal Image Aesthetic Assessment Baseline and Benchmark -->

<!-- [原子块 · verbatim] Abstract. -->

<!-- [原子块 · verbatim] As an alternative to expensive expert evaluation, Image Aesthetic Assessment (IAA) stands out as a crucial task in computer vision. However, traditional IAA methods are typically constrained to a sing -->

**EN** Keywords:

**ZH** 关键词：

**EN** 1. Introduction

**ZH** 1. 引言

**EN** Image Aesthetics Assessment (IAA) in computer vision involves the evaluation of the photography techniques and artistic approaches of images (Deng et al., 2017), to categorize them into various aesthetic levels (Hou et al., 2022; Niu et al., 2022). Serving as an alternative to costly expert aesthetic evaluation, IAA has a wide range of applications in image retrieval (Liu et al., 2021), album curation (Guo et al., 2017), smart photography (Rawat and Kankanhalli, 2016), and image editing(Chai et al., 2020), which is still a challenging task (Yang et al., 2019). Various datasets and models for IAA have been proposed, achieving significant progress. IAA datasets offer images with aesthetic scores (Murray et al., 2012; Kong et al., 2016; Yang et al., 2022) and other annotations of aesthetic attributes (Kong et al., 2016; He et al., 2022; Yang et al., 2022; Murray et al., 2012), as well as overall description (Jin et al., 2019). Many studies have achieved promising results by employing data-driven approaches to directly predict the aesthetic mean opinion scores (MOS) (He et al., 2022; Xiong et al., 2023; He et al., 2023), including convolutional neural networks (Talebi and Milanfar, 2018; Chen et al., 2020; He et al., 2022; Hosu et al., 2019), and transformers (Ke et al., 2021; Xia et al., 2022; He et al., 2023). There are also works that use aesthetic attributes and image content to assist in predicting scores (Kong et al., 2016; Yang et al., 2022; He et al., 2023). VILA (Ke et al., 2023) and RPCD (Vera Nieto et al., 2022) have demonstrated the potential of learning image aesthetics from photo comments.

**ZH** 图像美学评估（Image Aesthetics Assessment, IAA）旨在评价图像的摄影技法与艺术手法（Deng et al., 2017），并将其归入不同的美学等级（Hou et al., 2022; Niu et al., 2022）。作为昂贵的专家美学评审的替代方案，IAA 在图像检索（Liu et al., 2021）、相册整理（Guo et al., 2017）、智能摄影（Rawat and Kankanhalli, 2016）与图像编辑（Chai et al., 2020）等场景中应用广泛，至今仍是一项富有挑战的任务（Yang et al., 2019）。已有研究提出了大量 IAA 数据集与模型，并取得显著进展。IAA 数据集既提供带美学分数的图像（Murray et al., 2012; Kong et al., 2016; Yang et al., 2022），也提供美学属性等其他标注（Kong et al., 2016; He et al., 2022; Yang et al., 2022; Murray et al., 2012），以及整体性描述（Jin et al., 2019）。许多工作采用数据驱动方式直接预测美学平均意见分（MOS）（He et al., 2022; Xiong et al., 2023; He et al., 2023），包括卷积神经网络（Talebi and Milanfar, 2018; Chen et al., 2020; He et al., 2022; Hosu et al., 2019）与 Transformer（Ke et al., 2021; Xia et al., 2022; He et al., 2023），取得了可观的效果。也有工作借助美学属性与图像内容来辅助分数预测（Kong et al., 2016; Yang et al., 2022; He et al., 2023）。VILA（Ke et al., 2023）与 RPCD（Vera Nieto et al., 2022）则展示了从照片评论中学习图像美学的潜力。

<!-- [原子块 · img]  -->

**EN** Figure 1. The Unified Multi-modal Image Aesthetic Assessment Framework, containing a baseline (a) and a benchmark (b). The aesthetic perception performance of UNIAA-LLaVA and other MLLMs is shown in (c).

**ZH** 图 1. 统一多模态图像美学评估框架，包含一个基线（a）与一个基准（b）。（c）展示 UNIAA-LLaVA 与其他 MLLM 的美学感知性能。

**EN** Psychological studies reveal that the human experience of aesthetics involves a series of information processing stages, encompassing perception, integration of implicit memory, explicit classification of content and style, and evaluation (Leder et al., 2004; Chatterjee, 2004). However, current IAA methods are not well-aligned with the human aesthetic process. Regarding IAA datasets, most of them only cover a partial level of the human aesthetic evaluation process and lack standardization in their formats, which makes it difficult to train them under a uniform architecture. For example, AVA contains both the MOS of images as well as rich comments, photography style labels, and content tags. Aesthetic annotations are represented in different formats consisting of numeric, language, and category/attribute labels. Regarding IAA methods, they only utilize a part of aesthetic information and are predominantly focused on a single aesthetic task. Scoring models struggle to recognize the aesthetic attributes of images, while aesthetic description models can not score photos.

**ZH** 心理学研究表明，人类的美学体验包含一系列信息处理阶段，涵盖感知、内隐记忆的整合、内容与风格的显式分类以及评价（Leder et al., 2004; Chatterjee, 2004）。然而现有 IAA 方法与人类美学过程并不吻合。就数据集而言，多数数据集只覆盖人类美学评价流程的部分环节，且格式缺乏统一，难以在同一架构下训练。以 AVA 为例，它同时提供图像的 MOS、丰富的评论、摄影风格标签与内容标签，美学标注以数值、语言与类别／属性标签等不同形式呈现。就方法而言，现有 IAA 只利用部分美学信息，且大多聚焦于单一美学任务：评分模型难以识别图像的美学属性，美学描述模型又无法为照片打分。

**EN** We need a unified IAA framework that can align well with human aesthetic processes, integrate different sources and formats of aesthetic data, and achieve good results in multiple aesthetic subtasks. Specifically, we argue that in the process of IAA-model learning, it is necessary to align with the process of human aesthetics, rather than simply relying on implicit mapping through learning MOS or partial attributes (Vera Nieto et al., 2022; Ke et al., 2023). The model necessitates a visual understanding and harbors inherent reservoirs of aesthetic knowledge. It needs to learn explicit categorization of the aesthetic attributes and integrate the aesthetic information to provide detailed descriptions and overall scores. MLLM (OpenAI, 2023; Alayrac et al., 2022; Li et al., 2022; Driess et al., 2023; Zhu et al., 2023; Liu et al., 2023; Huang et al., 2023; Li et al., 2023) is primarily composed of a vision encoder and an LLM, which is capable of visual perception and has substantial knowledge capacity (Schaeffer et al., 2023), making it a natural fit for human-aligned and unified IAA.

**ZH** 我们需要一个统一的 IAA 框架，既能与人类美学过程良好契合，又能整合不同来源与格式的美学数据，并在多个美学子任务上取得良好效果。具体而言，我们认为 IAA 模型的学习过程应当与人类美学过程相对齐，而不是单纯依赖通过 MOS 或部分属性学到的隐式映射（Vera Nieto et al., 2022; Ke et al., 2023）。模型需要具备视觉理解能力，并储备内在的美学知识；它要学习美学属性的显式分类，并整合美学信息以给出细致的描述与整体评分。多模态大语言模型（MLLM）（OpenAI, 2023; Alayrac et al., 2022; Li et al., 2022; Driess et al., 2023; Zhu et al., 2023; Liu et al., 2023; Huang et al., 2023; Li et al., 2023）主要由视觉编码器与大语言模型构成，兼具视觉感知能力与庞大的知识容量（Schaeffer et al., 2023），天然适合构建与人类对齐的统一 IAA。

**EN** We propose UNIAA, as shown in Figure 1, which to the best of our knowledge, introduces MLLM to IAA for the first time, including an IAA-MLLM baseline and a comprehensive aesthetic benchmark. The baseline is capable of unifying aesthetic perception, description, and assessment tasks, while the benchmark comprehensively evaluates the aesthetic capabilities of MLLM from these three aspects, which strives to align the aesthetic evaluation process with that of human experts. For the baseline model, we adopt the well-established LLaVA (Liu et al., 2023a; Liu et al., 2023b) architecture and further finetune it with aesthetic visual instruction tuning data to obtain our UNIAA-LLaVA (Figure 1(a)). Based on the integration of visually aesthetic perception by the vision encoder and memory of aesthetic knowledge through LLM, UNIAA-LLaVA demonstrates a strong ability to learn and align with human aesthetics. However, due to the subjective and complex nature of aesthetics (Yang et al., 2022), annotating a large amount of aesthetic visual instruction tuning data is very expensive. Therefore, we establish a low-cost IAA Dataset Conversion Paradigm (IDCP), aiming to convert aesthetic annotations such as aesthetic attributes and comments from off-the-shelf IAA datasets into a MLLM visual-instruction-tuning format.

**ZH** 我们提出 UNIAA（见图 1），据我们所知，它首次将 MLLM 引入 IAA，包含一个 IAA-MLLM 基线和一个全面的美学基准。基线能够统一美学感知、描述与评价三类任务；基准则从这三个方面系统评测 MLLM 的美学能力，力求使美学评价过程与人类专家一致。基线模型采用成熟的 LLaVA 架构（Liu et al., 2023a; Liu et al., 2023b），并用美学视觉指令微调数据进一步微调，得到 UNIAA-LLaVA（图 1(a)）。借助视觉编码器的美学视觉感知与大语言模型的美学知识记忆，UNIAA-LLaVA 展现出学习与对齐人类美学的强大能力。然而，由于美学本身主观且复杂（Yang et al., 2022），标注大规模美学视觉指令微调数据代价高昂。为此，我们建立了一套低成本的 IAA 数据集转换范式（IDCP），把现成 IAA 数据集中的美学属性、评论等标注转换为 MLLM 视觉指令微调格式。

**EN** To evaluate the aesthetic ability of the proposed UNIAA-LLaVA and other existing MLLMs, we construct a comprehensive and professional UNIAA-Bench (Figure 1(b)). To ensure diversity, we select test-set images from the IAA datasets as the in-domain split and collect images from the internet as the in-the-wild split. The in-the-wild split does not overlap with the IAA datasets that are used to train the UNIAA-LLaVA, which can further prove its generalization capability on various aesthetic tasks. In accordance with the image-quality Q-bench (Wu et al., 2023) and human aesthetic (Leder et al., 2004), we evaluate the aesthetic ability of MLLMs from three aspects, including Perception, Description, and Assessment. For Aesthetic Perception, we construct the UNIAA-QA dataset, which covers six general aesthetic attributes (Yang et al., 2022; Li et al., 2023) through its questions: content and theme, composition, color, light, focus and sentiments. For Aesthetic Description, we construct the UNIAA-Describe dataset to assess the ability of MLLM on detailed and professional aesthetic comments and suggestions. For Aesthetic Assessment, we test the zero-shot scoring ability of MLLMs through output token logits. Our contributions can be summed up into four points:

**ZH** 为评测 UNIAA-LLaVA 与其他现有 MLLM 的美学能力，我们构建了全面而专业的 UNIAA-Bench（图 1(b)）。为保证多样性，我们从 IAA 数据集中选取测试集图像作为域内（In-Domain）子集，并从互联网收集图像作为开放场景（In-the-Wild）子集。开放场景子集与训练 UNIAA-LLaVA 所用的 IAA 数据集不重叠，可进一步检验模型在各类美学任务上的泛化能力。参照图像质量 Q-bench（Wu et al., 2023）与人类美学模型（Leder et al., 2004），我们从感知、描述与评价三个方面评测 MLLM 的美学能力。美学感知方面，构建 UNIAA-QA 数据集，其问题覆盖六类通用美学属性（Yang et al., 2022; Li et al., 2023）：内容与主题、构图、色彩、光线、对焦与情感。美学描述方面，构建 UNIAA-Describe 数据集，考察 MLLM 给出细致、专业美学评论与建议的能力。美学评价方面，通过输出词元的 logits 测试 MLLM 的零样本评分能力。本文贡献可概括为四点：

**EN** ⟦SLOT_0⟧ We establish an IAA framework that includes an IAA-Baseline and a comprehensive IAA-Bench, namely UNIAA. Both the learning process and evaluation process of UNIAA align with the visual aesthetic process of human experts.

**ZH** ⟦SLOT_0⟧ 建立了一个包含 IAA 基线与综合 IAA 基准的 IAA 框架，即 UNIAA。UNIAA 的学习过程与评价过程均与人类专家的视觉美学过程相对齐。

**EN** ⟦SLOT_1⟧ We develop an IAA Datasets Conversion Paradigm (IDCP) to convert existing aesthetic datasets into a format suitable for MLLMs fine-tuning. Using converted data, we obtain the UNIAA-LLaVA, which unifies IAA subtasks with language.

**ZH** ⟦SLOT_1⟧ 提出 IAA 数据集转换范式（IDCP），将现有美学数据集转换为适用于 MLLM 微调的格式。利用转换后的数据训练得到 UNIAA-LLaVA，以语言统一了各 IAA 子任务。

**EN** ⟦SLOT_2⟧ We are constructing a comprehensive aesthetic evaluation benchmark called UNIAA-Bench, which systematically evaluates the aesthetic abilities of MLLMs from three overall dimensions: Aesthetic Perception, Aesthetic Description, and Aesthetic Assessment.

**ZH** ⟦SLOT_2⟧ 构建了全面的美学评测基准 UNIAA-Bench，从美学感知、美学描述与美学评价三个维度系统评估 MLLM 的美学能力。

**EN** ⟦SLOT_3⟧ We demonstrate the effectiveness of UNIAA-LLaVA and IDCP, the authority of UNIAA-Bench, and the feasibility of MLLM in accomplishing aesthetic tasks through experiments.

**ZH** ⟦SLOT_3⟧ 通过实验验证了 UNIAA-LLaVA 与 IDCP 的有效性、UNIAA-Bench 的权威性，以及 MLLM 完成美学任务的可行性。

**EN** 2. Related Work

**ZH** 2. 相关工作

**EN** 2.1. Image Aesthestic Assessment

**ZH** 2.1. 图像美学评估

**EN** Image Aesthetics Assessment has three main tasks: direct scoring of the aesthetic quality of images (Murray et al., 2012; Karayev et al., 2014; Tang et al., 2013; Ren et al., 2017; Lee et al., 2018; Yang et al., 2022; He et al., 2022), recognition of aesthetic attributes (Celona et al., 2022; Jin et al., 2019), and aesthetic description (Zhou et al., 2016; Wang et al., 2019). A multitude of approaches, encompassing network architecture design (Tang et al., 2013; He et al., 2023), loss function design (Kong et al., 2016; Talebi and Milanfar, 2018), utilization of the CLIP (Radford et al., 2021) pre-training model (Ke et al., 2023; Xiong et al., 2023), and more, have been proposed, demonstrating strong performance on their respective tasks and datasets. However, the majority of IAA models focus on accomplishing one or two subtasks. There is a lack of a comprehensive and versatile IAA model for holistic image aesthetic evaluation.

**ZH** 图像美学评估包含三类主要任务：直接对图像美学质量评分（Murray et al., 2012; Karayev et al., 2014; Tang et al., 2013; Ren et al., 2017; Lee et al., 2018; Yang et al., 2022; He et al., 2022）、识别美学属性（Celona et al., 2022; Jin et al., 2019）与美学描述（Zhou et al., 2016; Wang et al., 2019）。研究者提出了大量方法，涵盖网络结构设计（Tang et al., 2013; He et al., 2023）、损失函数设计（Kong et al., 2016; Talebi and Milanfar, 2018）、CLIP（Radford et al., 2021）预训练模型的利用（Ke et al., 2023; Xiong et al., 2023）等，在各自任务与数据集上表现优异。然而多数 IAA 模型只完成一到两个子任务，尚缺少一个全面、通用的 IAA 模型来做整体性的图像美学评价。

**EN** Numerous datasets emerge to support the advancement of IAA. Murray et al. (Murray et al., 2012) pioneered the AVA dataset, which has gained significant popularity. Kong et al. (Kong et al., 2016) introduced the Aesthetics and Attributes Database (AADB), encompassing subjective aesthetic scores and attributes Addressing the need for generating captions based on photo aesthetics, Yu et al. (Chang et al., 2017) developed the Photo Critique Captioning Dataset (PCCD). TAD66K (He et al., 2022) is an extensive dataset encompassing 47 subjects. The Personalized Image Aesthetics Database with Rich Attributes (PARA) (Yang et al., 2022) includes nine image-oriented objective attributes and four human-oriented subjective attributes. ICAA17K (He et al., 2023) comprises 17K images capturing 30 popular color combinations, providing a valuable resource for color-oriented analysis. While these datasets were previously handled separately, the shared and correlated nature of aesthetic knowledge provides the potential for integrating learning.

**ZH** 众多数据集推动了 IAA 的发展。Murray 等人（Murray et al., 2012）开创的 AVA 数据集广为使用；Kong 等人（Kong et al., 2016）提出了包含主观美学分数与属性的美学与属性数据库（AADB）；为满足基于照片美学的描述生成需求，Yu 等人（Chang et al., 2017）构建了照片评论描述数据集（PCCD）；TAD66K（He et al., 2022）是覆盖 47 个主题的大规模数据集；带有丰富属性的个性化图像美学数据库（PARA）（Yang et al., 2022）包含 9 项面向图像的客观属性与 4 项面向人的主观属性；ICAA17K（He et al., 2023）包含 17K 图像、覆盖 30 种流行色彩组合，为色彩导向的分析提供了宝贵资源。这些数据集以往都是各自独立使用的，而美学知识本身具有共享性与相关性，具备整合学习的潜力。

**EN** However, the current IAA methods still have a significant gap from a general-purpose image aesthetic evaluation, mainly due to the following two issues. Firstly, relying on human-labeled aesthetic ratings, i.e. MOS, for directly supervised learning may be sub-optimal, as it lacks of interpretability (Kang et al., 2020) and may lead to overfitting to label noise. Moreover, current methods are still constrained by the need to train different models for individual datasets. Tasks such as aesthetic perception, aesthetic description, and aesthetic assessment also require training in separate models (Yang et al., 2019). Current IAA methods lack comprehensive aesthetic information learning and universal applicability across different datasets and tasks. These limitations hinder the practical applicability and universality of IAA. Therefore, IAA urgently requires a unified and versatile approach to enhance its practical value.

**ZH** 然而，现有 IAA 方法与通用图像美学评价之间仍有明显差距，主要源于两方面问题。其一，直接依赖人工标注的美学评分（即 MOS）做监督学习并非最优：这种做法缺乏可解释性（Kang et al., 2020），还可能过拟合到标签噪声。其二，现有方法仍需为每个数据集单独训练模型，美学感知、美学描述与美学评价等任务也需要在不同模型上分别训练（Yang et al., 2019）。现有 IAA 方法既缺少对美学信息的综合学习，也缺乏跨数据集、跨任务的通用性，限制了 IAA 的实用价值与普适性。因此，IAA 亟需一种统一、通用的方案来提升其实用价值。

**EN** 2.2. Multi-modality Large Language Models

**ZH** 2.2. 多模态大语言模型

**EN** Large language models (LLMs) such as GPT-4 (OpenAI, 2023), T5 (Chung et al., 2022), and LLaMA (Touvron et al., 2023), have demonstrated a remarkable language proficiency in general knowledge. By incorporating vision encoders (Radford et al., 2021) and additional adaptive modules into LLMs, Multi-modal Large Language Models (MLLMs) (Li et al., 2023; Gao et al., 2023; Liu et al., 2023; Dai et al., 2023; Zhang et al., 2023) have driven significant progress in tackling various multi-modal tasks concerning high-level vision, such as image captioning (Chen et al., 2015; Agrawal et al., 2019; Young et al., 2014), visual question answering (VQA) (Antol et al., 2015; Marino et al., 2019; Schwenk et al., 2022), and other language-related abilities (Liu et al., 2023; Fu et al., 2023; Li et al., 2023).

**ZH** GPT-4（OpenAI, 2023）、T5（Chung et al., 2022）、LLaMA（Touvron et al., 2023）等大语言模型（LLM）在通用知识上展现出卓越的语言能力。通过在 LLM 中引入视觉编码器（Radford et al., 2021）与额外的适配模块，多模态大语言模型（MLLM）（Li et al., 2023; Gao et al., 2023; Liu et al., 2023; Dai et al., 2023; Zhang et al., 2023）在图像描述（Chen et al., 2015; Agrawal et al., 2019; Young et al., 2014）、视觉问答（VQA）（Antol et al., 2015; Marino et al., 2019; Schwenk et al., 2022）等高层视觉多模态任务上取得显著进展，也带动了其他语言相关能力的发展（Liu et al., 2023; Fu et al., 2023; Li et al., 2023）。

**EN** Although MLLMs (OpenAI, 2023; Alayrac et al., 2022; Li et al., 2022; Driess et al., 2023; Zhu et al., 2023; Liu et al., 2023; Huang et al., 2023; Li et al., 2023; Lin et al., 2023; Lin et al., 2024; Zhu et al., 2023; Jin et al., 2023) play a crucial role in advancing vision-language learning, they exhibit subpar performance in specific tasks and vertical applications (Li et al., 2023; Fu et al., 2023; Wu et al., 2023; Li et al., 2023). The emergence of fine-tuning with task-specific instructional knowledge has led to a surge of MLLMs tailored for specific tasks, such as Q-instruct (Wu et al., 2023), LLaVA-Med (Li et al., 2023), and Drive-GPT4 (Xu et al., 2023).

**ZH** 尽管 MLLM（OpenAI, 2023; Alayrac et al., 2022; Li et al., 2022; Driess et al., 2023; Zhu et al., 2023; Liu et al., 2023; Huang et al., 2023; Li et al., 2023; Lin et al., 2023; Lin et al., 2024; Zhu et al., 2023; Jin et al., 2023）在推动视觉—语言学习方面作用关键，但它们在特定任务与垂直应用上表现欠佳（Li et al., 2023; Fu et al., 2023; Wu et al., 2023; Li et al., 2023）。面向具体任务的指令知识微调随之兴起，催生了 Q-instruct（Wu et al., 2023）、LLaVA-Med（Li et al., 2023）、Drive-GPT4（Xu et al., 2023）等专用 MLLM。

**EN** Why choose MLLM for IAA? There are two reasons for adapting MLLMs to IAA tasks. (1) MLLMs are capable of aesthetic visual perception and knowledge integration. (2) The fine-tuning data and output are both mediated by language, which facilitates the natural integration of aesthetic visual instruction tuning and enables seamless completion of IAA subtasks. These training data and subtasks are highly associated with the human aesthetic process (Leder et al., 2004). Our goal is to create a unified aesthetic foundational model that can integrate various aesthetic information and establish general capabilities across various tasks while robustly responding to open-ended human queries.

**ZH** 为何选择 MLLM 做 IAA？原因有两点。（1）MLLM 具备美学视觉感知与知识整合的能力。（2）微调数据与输出均以语言为媒介，天然便于美学视觉指令微调的整合，并可无缝完成各 IAA 子任务。这些训练数据与子任务与人类美学过程高度相关（Leder et al., 2004）。我们的目标是打造一个统一的美学基础模型，既能整合各类美学信息、在多种任务上建立通用能力，又能稳健地回应人类的开放式提问。

<!-- [原子块 · img]  -->

**EN** Figure 2. The IAA Datasets Conversion Paradigm for UNIAA-LLaVA.

**ZH** 图 2. 面向 UNIAA-LLaVA 的 IAA 数据集转换范式。

**EN** 3. UNIAA-LLaVA

**ZH** 3. UNIAA-LLaVA

**EN** In the following two sections, we present the details of our proposed aesthetic evaluation framework, UNIAA, which aims to unify the aesthetic information perception, description, and assessment tasks. As a starting point, we integrate LLaVA, a versatile multimodal conversational model (Liu et al., 2023a), as the initial model. Subsequently, we consistently refine and fine-tune the model to specifically cater to the demands of the aesthetic domain. There is a shortage of multi-modal image aesthetic datasets for training an instruction-following assistant. To bridge this gap, we construct the initial dataset of its kind, derived from extensively available IAA datasets. As a fundamental part of constructing the instruction fine-tuning dataset, we first introduce a low-cost paradigm for converting the instruction fine-tuning data. Unlike the need for manual annotation collection, we utilize the existing IAA dataset and transform it into corresponding suitable IAA instruction fine-tuning data based on the aesthetic dimensions emphasized during its labeling and annotation settings. Then, further using the transformed data, we obtain the first MLLM of IAA via instruction fine-tuning on the LLaVA.

**ZH** 接下来两节介绍所提出的美学评价框架 UNIAA 的细节，它旨在统一美学信息的感知、描述与评价三项任务。作为起点，我们引入通用多模态对话模型 LLaVA（Liu et al., 2023a）作为初始模型，并针对美学领域的需求持续改造与微调。训练一个遵循指令的助手缺少多模态图像美学数据集，为填补这一空白，我们基于大量现成 IAA 数据集构建了首个此类数据集。构建指令微调数据集的基础工作，是先提出一种低成本的指令微调数据转换范式：无需人工收集标注，而是利用已有 IAA 数据集，依据其在标注与标注设置中所强调的美学维度，转换为对应的适用指令微调数据。随后用转换后的数据在 LLaVA 上做指令微调，得到首个面向 IAA 的 MLLM。

**EN** 3.1. IAA Datasets Conversion Paradigm

**ZH** 3.1. IAA 数据集转换范式

**EN** Inspired by the construction of classic datasets of instruction tuning (Fu et al., 2023; Liu et al., 2023; Wu et al., 2023; Chen et al., 2023), our IAA Data Conversion Paradigm (IDCP) consists of three steps: data selection, data filtering, and question-answer generation, as illustrated in Figure 2. The converted data will be used for training UNIAA-LLaVA. We hope that our IAA data transformation pipeline can provide inspiration and guidance for building new IAA instruction tuning datasets as well as other domain-specific task datasets.

**ZH** 借鉴经典指令微调数据集的构建思路（Fu et al., 2023; Liu et al., 2023; Wu et al., 2023; Chen et al., 2023），我们的 IAA 数据转换范式（IDCP）包含三个步骤：数据选择、数据筛选与问答生成，如图 2 所示。转换后的数据用于训练 UNIAA-LLaVA。我们希望这条 IAA 数据转换流程能为构建新的 IAA 指令微调数据集，以及其他领域专用任务数据集提供启发与借鉴。

**EN** 3.1.1. Data Selection.

**ZH** 3.1.1. 数据选择。

**EN** To maximize the diversity and comprehensiveness of UNIAA, we first select five open-source mainstream IAA datasets, AVA, AADB, ICAA17K, PARA, and PCCD, detailed in Appendix A.1. These datasets have aesthetic annotations across different dimensions. We select specific aesthetic information. The annotation content of existing IAA datasets can be primarily categorized into the following three types, aesthetic attributes, aesthetic comments, and aesthetic scores. We choose the first two categories.

**ZH** 为使 UNIAA 尽可能多样、全面，我们首先选取五个开源主流 IAA 数据集：AVA、AADB、ICAA17K、PARA 与 PCCD，详见附录 A.1。这些数据集在不同维度上带有美学标注，我们从中挑选特定的美学信息。现有 IAA 数据集的标注内容主要可分为美学属性、美学评论与美学分数三类，我们选用前两类。

**EN** Aesthetic Attributes are annotated information about photographs on specific objective aesthetic dimensions. Its exceptional suitability for conversion into visual question answering empowers the model with the ability to recognize and evaluate the aesthetic attributes of images using concise words. The data sources for aesthetic attributes include the photography styles annotated in AVA, the influence of aesthetic attributes on overall image aesthetics in AADB, the color schemes in the ICAA17K dataset, and the quality classification of aesthetic attributes in PARA.

**ZH** 美学属性是关于照片在特定客观美学维度上的标注信息。它非常适合转换为视觉问答，能让模型用简洁的词语识别并评价图像的美学属性。美学属性的数据来源包括：AVA 中标注的摄影风格、AADB 中美学属性对整体图像美学的影响、ICAA17K 数据集中的色彩搭配，以及 PARA 中美学属性的质量分级。

**EN** Aesthetic Comments are evaluations and descriptions of aesthetic features, aiming to explore and convey the aesthetic ambiance and emotional experiences that images invoke. Descriptions of aesthetic comments can be made from various perspectives, such as color, composition, form of expression, meaning, emotions, etc. These comments can help models better understand and appreciate images. The data sources for aesthetic comments include the overall comment on a photo in AVA and the dimensional comment in PCCD including the use of camera, photo subject, depth of field, focus, color brightness, composition, and overall impression.

**ZH** 美学评论是对美学特征的评价与描述，旨在挖掘并传达图像唤起的美学意境与情感体验。美学评论可从色彩、构图、表现形式、意涵、情感等多个视角展开，能帮助模型更好地理解与鉴赏图像。美学评论的数据来源包括 AVA 中对照片的整体评论，以及 PCCD 中的分维度评论，后者涵盖相机使用、拍摄主体、景深、对焦、色彩明暗、构图与整体印象。

**EN** Why not use Aesthetic Scores? Aesthetic Scores are highly subjective (Yang et al., 2022). Due to the differences in scoring rules and aesthetic differences among annotation experts, it is difficult to convert scores from different IAA datasets into unified evaluation scores. For example, a photo with a high score in one dataset may not have better aesthetic quality than a photo with a medium score in another dataset. Instead, we use attributes and descriptions to enable the UNIAA-LLaVA to have good zero-shot scoring capability, detailed in Section 5.3. As a supplementary experiment, based on the vision encoder of UNIAA-LLaVA, we further conduct supervised training on specific datasets and achieve the SOTA performance, demonstrating the generalization of our learning framework.

**ZH** 为何不使用美学分数？美学分数的主观性很强（Yang et al., 2022）。由于各数据集的评分规则不同、标注专家的审美取向也有差异，很难把不同 IAA 数据集的分数统一到同一评价体系中：一张在某一数据集中得分很高的照片，其美学质量未必优于另一数据集中得分中等的照片。因此，我们改用属性与描述来赋予 UNIAA-LLaVA 良好的零样本评分能力，详见第 5.3 节。作为补充实验，我们还在 UNIAA-LLaVA 视觉编码器的基础上对特定数据集做监督训练，取得了 SOTA 性能，验证了本学习框架的泛化性。

**EN** 3.1.2. Data Filtration.

**ZH** 3.1.2. 数据筛选。

**EN** Data Quality. We ensure the quality of the training data from the source by conducting manual checks on the selected data for both completeness and accuracy. We filter out empty or incomplete annotations and remove incorrectly labeled aesthetic dimensions. We check the difficulty of aesthetic information by removing data that is too simple or too difficult. We discard the "Tags" of AVA, which contain simple categories like "Water" and "Street" due to their low relevance to aesthetics. For some attributes in AADB, such as whether colors are harmonious, we filter out samples that are difficult for experts to judge.

**ZH** 数据质量。我们从源头把控训练数据质量，对所选数据做人工核查，兼顾完整性与准确性：滤除空标注或不完整的标注，剔除美学维度标注错误的样本，并按美学信息的难度剔除过易或过难的样本。AVA 的「Tags」字段包含「Water」「Street」等与美学相关性很低的简单类别，我们予以丢弃；AADB 中某些属性（如色彩是否和谐）连专家都难以判断，相应样本也被筛除。

**EN** Data Balance. To introduce diverse visual aesthetic appearances, we uniformly sampled images from each aesthetic quality range. We balance the number of aesthetic attributes as well as the number of options within each attribute. For yes or no questions, we ensure the balance between "yes" and "no" responses.

**ZH** 数据均衡。为引入多样的视觉美学外观，我们在各美学质量区间内均匀采样图像，并均衡各美学属性的数量以及每个属性内部的选项数量。对是非类问题，则保证「是」与「否」回答的数量均衡。

**EN** 3.1.3. QA Generation.

**ZH** 3.1.3. 问答生成。

**EN** Attributes-based Pipeline. According to aesthetic attribute annotation, aesthetic experts first manually write down several elemental questions, and then let ChatGPT expand them into various forms while ensuring the same meaning, detailed in Appendix A.2. To imitate diverse query formats from human beings (Wu et al., 2023), we organize three question types, Yes-or-No, What, and How, which correspond to different types of annotations. For binary attribute questions, such as whether elements in a photo are balanced, "yes/no" is used. Specifically, for questions about the types of attributes, such as the primary color usage of a picture, "what" is used. For quality classification questions, such as the quality of focus, "how" is used.

**ZH** 基于属性的流程。依据美学属性标注，美学专家先手工写出若干基础问题，再由 ChatGPT 在保持语义不变的前提下扩展为多种表述，详见附录 A.2。为模拟人类多样的提问方式（Wu et al., 2023），我们组织了 Yes-or-No、What、How 三类问题，对应不同类型的标注：二值属性问题（如画面元素是否平衡）用「是／否」；属性类型问题（如画面的主色运用）用「What」；质量分级问题（如对焦质量）用「How」。

<!-- [原子块 · img]  -->

**EN** Figure 3. The UNIAA-Bench overview. (a) UNIAA-QA contains 5354 Image-Question-Answer samples and (b) UNIAA-Describe contains 501 Image-Description samples. (c) For open-source MLLMs, Logits can be extracted to calculate the score.

**ZH** 图 3. UNIAA-Bench 概览。（a）UNIAA-QA 包含 5354 个「图像—问题—答案」样本，（b）UNIAA-Describe 包含 501 个「图像—描述」样本。（c）对开源 MLLM，可提取 logits 计算得分。

**EN** Comments-based Pipeline. The quality and style of aesthetic comments in different datasets can vary. For instance, the comments in the AVA (Murray et al., 2012) are more colloquial, whereas the PCCD (Chang et al., 2017) contains professional comments from experienced photographers. It is necessary to use ChatGPT (OpenAI, 2023a; OpenAI, 2023b) to clean the raw data, detailed in Appendix A.3. The transformation process of aesthetic comments mainly consists of two steps: comments rewriting and question matching. We utilize GPT and LLaVA to assist in rewriting the comments. LLaVA offers the image content and details. GPT is prompted to filter out the drawbacks of aesthetic comments from different datasets, such as the colloquial content in AVA that is not relevant to aesthetics and the excessively long comments in PCCD.

**ZH** 基于评论的流程。不同数据集的美学评论在质量与风格上差异明显：AVA（Murray et al., 2012）的评论偏口语化，而 PCCD（Chang et al., 2017）收录的是资深摄影师的专业评论。因此需要借助 ChatGPT（OpenAI, 2023a; OpenAI, 2023b）清洗原始评论，详见附录 A.3。美学评论的转换主要包含评论改写与问题匹配两步。我们利用 GPT 与 LLaVA 辅助改写：LLaVA 提供图像内容与细节，GPT 则被提示过滤掉不同数据集评论中的缺陷，例如 AVA 中与美学无关的口语内容、PCCD 中过长的评论。

**EN** Regarding question matching, we use the length and dimension of cleaned content as key points. We ask the MLLM questions to evaluate the image’s overall aesthetic and specific dimensions, such as composition, lighting, and impression. If the comments include explanations for aesthetic patterns and suggestions for aesthetic improvements, the matching questions will also include phrases such as "analyze the causes of this characteristic" and "please provide some aesthetic improvement suggestions." If the comments exceed a certain length, such as 100 words, the corresponding question would be to provide a “detailed” evaluation of the image.

**ZH** 问题匹配环节，我们以清洗后内容的长度与维度为依据。让 MLLM 回答的问题既有对图像整体美学的评价，也有构图、光线、印象等具体维度的评价。若评论中包含对美学成因的解释与改进建议，匹配的问题也会加入「分析这一特征产生的原因」「请给出若干美学改进建议」等表述。若评论超过一定长度（如 100 词），对应的问题会要求对图像做出「细致」的评价。

**EN** 3.1.4. IDCP Advantages Discussion.

**ZH** 3.1.4. IDCP 优势讨论。

**EN** As a general MLLM aesthetic data conversion paradigm, IDCP has the following three advantages. Firstly, it is low cost. IDCP integrates publicly available datasets, without the need for additional manpower to collect and annotate data. Secondly, it has uniformity. Through conversion, aesthetic comments and aesthetic attributes can be trained in a unified format, enhancing the overall aesthetic capabilities of the model. Thirdly, it has scalability. In addition to the five datasets we select, it can also be used to incorporate newly emerged aesthetic datasets, and more data will further enhance the aesthetic capabilities of the model.

**ZH** 作为一种通用的 MLLM 美学数据转换范式，IDCP 有三方面优势。其一是低成本：IDCP 整合公开数据集，无需额外人力收集与标注。其二是统一性：转换后，美学评论与美学属性可在统一格式下训练，整体提升模型的美学能力。其三是可扩展性：除所选五个数据集外，还可纳入新出现的美学数据集，更多数据会进一步增强模型的美学能力。

**EN** 3.2. Image Aesthetic Visual Instruction Tuning

**ZH** 3.2. 图像美学视觉指令微调

**EN** In this section, we discuss the training approaches used to fine-tune MLLMs with Image Aesthetic visual instructions. The training process for open-source MLLMs (Dai et al., 2023; Li et al., 2023; Zhang et al., 2023) consists of two stages. The first stage involves aligning the representation space of the visual backbone and LLM with million-scale data (Schuhmann et al., 2021; Sharma et al., 2018). The second stage includes fine-tuning the MLLM with a combination of human-labeled datasets (Yu et al., 2016; Antol et al., 2015; Chen et al., 2015; Marino et al., 2019) for visual instruction tuning. Considering the scale and computational cost of the IDCP dataset, we utilize the MLLM fine-tuned after the second stage for visual instruction tuning to perform IAA learning. IAA tasks require a finer level of visual perception. We open the parameter training of the vision encoder during training.

**ZH** 本节讨论用图像美学视觉指令微调 MLLM 的训练方式。开源 MLLM（Dai et al., 2023; Li et al., 2023; Zhang et al., 2023）的训练分两个阶段：第一阶段用百万级数据（Schuhmann et al., 2021; Sharma et al., 2018）对齐视觉骨干与大语言模型的表示空间；第二阶段用人工标注数据集的组合（Yu et al., 2016; Antol et al., 2015; Chen et al., 2015; Marino et al., 2019）做视觉指令微调。考虑到 IDCP 数据集的规模与计算成本，我们基于第二阶段微调后的 MLLM 再做视觉指令微调，以完成 IAA 学习。IAA 任务需要更精细的视觉感知，因此训练时开放了视觉编码器的参数。

**EN** 4. UNIAA-Bench

**ZH** 4. UNIAA-Bench

**EN** It is uncertain how well the UNIAA-LLaVA performs in image aesthetics. The lack of a dedicated benchmark for assessing the effectiveness of MLLMs in aesthetic evaluation presents an apparent obstacle, which may hinder the progress of advanced MLLMs capable of aesthetics. To solve this problem, we propose UNIAA-Bench, an expert benchmark designed to comprehensively evaluate the aesthetic capabilities of MLLMs. To ensure the diversity of the benchmark (Liu et al., 2023a), we select images from the internet and other datasets that have never been seen by UNIAA-LLaVA, serving as In-the-Wild resources. IAA-Bench also contains test-set images from the IAA datasets as In Domain resources, whose training sets were previously used during the training of our baseline. Inspired by human aesthetic process (Leder et al., 2004) and image-quality bench (Wu et al., 2023), we suggest a collection of integrative standards to measure the aesthetic skills of MLLMs from three perspectives: Aesthetic Perception, Aesthetic Description, and Aesthetic Assessment.

**ZH** UNIAA-LLaVA 在图像美学上究竟表现如何尚无定论。缺少专门评测 MLLM 美学效果的基准是一大障碍，可能制约具备美学能力的高级 MLLM 的发展。为此，我们提出 UNIAA-Bench，这是一个专家级基准，用于全面评测 MLLM 的美学能力。为保证基准的多样性（Liu et al., 2023a），我们从互联网及其他数据集中选取 UNIAA-LLaVA 从未见过的图像作为开放场景（In-the-Wild）资源；UNIAA-Bench 同时也包含 IAA 数据集的测试集图像作为域内（In Domain）资源，其训练集此前已用于训练我们的基线。受人类美学过程（Leder et al., 2004）与图像质量基准（Wu et al., 2023）启发，我们提出一套综合标准，从美学感知、美学描述与美学评价三个视角衡量 MLLM 的美学能力。

**EN** 4.1. Aesthetic Perception

**ZH** 4.1. 美学感知

**EN** We construct the UNIAA-QA to investigate whether MLLMs can accurately respond to simple natural language queries related to aesthetic attributes, which is also an ability of human experts to recognize explicit aesthetic information (Leder et al., 2004). UNIAA-QA contains 5,354 images, as listed in Figure 3(a), including 2,229 images in the domain and 3,125 images from the wild. The aesthetic issues examined in the WILD do not exist in the training of UNIAA-LLaVA, as indicated by the item highlighted in red in Figure 3(a). For each image, there is one question related to perception, with one correct option and 1-3 false options. Drawing on recent studies on aesthetic perception (Yang et al., 2022) and the human perception process related to image aesthetics (Li et al., 2023), the UNIIAA-QA subset addresses six dimensions through its questions: Content and Theme, Composition, Color, Light, Focus and Sentiment.

**ZH** 我们构建 UNIAA-QA，考察 MLLM 能否准确回答与美学属性相关的简单自然语言提问——识别显式的美学信息本就是人类专家的一项能力（Leder et al., 2004）。UNIAA-QA 含 5,354 张图像，如图 3(a) 所列，其中域内图像 2,229 张、开放场景图像 3,125 张。图 3(a) 中红色标出的项表明，WILD 所考察的美学问题在 UNIAA-LLaVA 的训练中并未出现。每张图像配一个感知类问题，含一个正确选项与 1～3 个错误选项。借鉴近期美学感知研究（Yang et al., 2022）与图像美学相关的人类感知过程研究（Li et al., 2023），UNIIAA-QA 子集的问题覆盖六个维度：内容与主题、构图、色彩、光线、对焦与情感。

**EN** Content and Theme are the first aspects that need to be understood when analyzing the aesthetics (Leder et al., 2004; Li et al., 2023). Question design includes asking about photo theme, subject type, content, and influence on aesthetics. Composition is a critical indicator in characterizing the aesthetic qualities of an image (Celona et al., 2022), which structures the visual story and enhances the aesthetic appeal. Within visual arts, the visual elements of an image are interdependent through composition (Liu et al., 2019), relying on each other to collectively showcase the aesthetic qualities of the entire image. Composition contains multiple categories, such as the rule of thirds, diagonal, symmetry, and centering. Color is considered more perceptually distinct and relevant than other aesthetic features (He et al., 2023) since the human eye can directly perceive different wavelengths of light and convert them into distinct color signals. UNIAA-Bench examines color scheme, color combination, and color harmony. Light affects aspects of the image such as brightness, contrast, and saturation, which can create a sense of visual hierarchy and depth. The perception of light includes the lighting quality, the type of luminance source, and the lighting tone. Focus highlights the important part of the image. A good focus can help the viewer better understand the story of the image and the emotions conveyed, thus improving the aesthetic quality of the image. Sentiment plays a crucial role in visual aesthetic (Feng et al., 2023; Leder et al., 2004). It encompasses emotional reactions, attractiveness, and understanding of atmosphere in aesthetic experiences.

**ZH** 内容与主题是分析美学时首先需要理解的方面（Leder et al., 2004; Li et al., 2023），问题设计涵盖照片主题、主体类型、内容及其对美学的影响。构图是刻画图像美学品质的关键指标（Celona et al., 2022），它组织视觉叙事并增强美感；在视觉艺术中，图像的各视觉元素通过构图相互依存（Liu et al., 2019），共同呈现整幅图像的美学品质。构图包含三分法、对角线、对称、居中等多种类型。色彩比其他美学特征更具感知区分度与相关性（He et al., 2023），因为人眼能直接感知不同波长的光并将其转化为不同的色彩信号；UNIAA-Bench 考察色彩搭配、色彩组合与色彩和谐。光线影响图像的明暗、对比与饱和度，可营造视觉层次与纵深；对光线的感知包括光照质量、光源类型与光调。对焦突出画面重点，良好的对焦能帮助观者更好地理解图像叙事与所传达的情感，从而提升图像的美学品质。情感在视觉美学中作用关键（Feng et al., 2023; Leder et al., 2004），涵盖审美体验中的情绪反应、吸引力与氛围理解。

**EN** The UNIAA-QA utilizes three question types commonly used in human queries when interacting with MLLMs (Chen et al., 2023; Wu et al., 2023): "Yes-or-No" questions requires a positive or negative response (e.g., Does this photo employ the rule of thirds in its composition?). "What" questions examine more comprehensive aesthetic perception, such as "What type of composition is used in this photo?". "How" questions are used to evaluate more details about the grade and production of aesthetic feeling in the image, such as "How does the use of symmetry composition affect photo aesthetic quality?".

**ZH** UNIAA-QA 采用人类与 MLLM 交互时常用的三类提问方式（Chen et al., 2023; Wu et al., 2023）：「Yes-or-No」类问题要求给出肯定或否定回答（如：这张照片的构图是否采用了三分法？）；「What」类问题考察更综合的美学感知（如：这张照片使用了何种构图方式？）；「How」类问题用于评价图像美感的等级与营造细节（如：对称式构图对照片的美学质量有何影响？）。

**EN** Table 1. Evaluation results on the Aesthetic Perception ability. We highlight the best result of each subclass with bold and underline the second, third, and fourth best sub-optimal results. CS means the model is the close source. *GPT-4V may refuse to answer some questions, and the accuracy is calculated based on the questions it answers.

**ZH** 表 1. 美学感知能力评测结果。每个子类的最优结果以粗体标出，次优、第三与第四好成绩以下划线标出。CS 表示该模型为闭源模型。*GPT-4V 可能拒绝回答部分问题，其准确率按实际回答的问题计算。

<!-- [原子块 · table] MLLM Aesthetic Attributes Question Types Image Sources Overall Rank Con. The. Comp. Color Light Focus Sent. Yes-No What How In-Domain Wild Random guess 36.15% 33.67% 39.43% 39.62% 38.07% 41.72% 50.00% -->

**EN** 4.2. Aesthetic Description

**ZH** 4.2. 美学描述

**EN** We construct the UNIAA-Describe subset to examine the aesthetic language description ability of MLLMs. UNIAA-Describe is a golden aesthetic description dataset, consisting of a single long (averaging 100 words) expert-provided description for each image. The dataset consists of 501 images, categorized into low, medium, and high aesthetic quality with 151, 150, and 200 images respectively. The description includes a concise and detailed analysis of the aesthetic attributes and photographic techniques used in the image, such as composition, color, focus, lighting, and sentiment. Improvement suggestions and overall aesthetic conclusions are summarized at the end of the description. All descriptions have been written by aesthetic experts and manually reviewed. Referring to these golden text descriptions, we can measure the quality of MLLMs output using a single-modal GPT (Wu et al., 2023), evaluated along three dimensions: Completeness, Preciseness, and Relevance. The prompt words used to generate descriptions for MLLM are as follows:

**ZH** 我们构建 UNIAA-Describe 子集，考察 MLLM 的美学语言描述能力。UNIAA-Describe 是一个黄金标准美学描述数据集，每幅图像配有一段由专家给出的长描述（平均 100 词）。数据集共 501 张图像，按低、中、高美学质量分别有 151、150、200 张。描述内容对图像所用美学属性与摄影技法（如构图、色彩、对焦、光线、情感等）做简明而细致的分析，并在结尾总结改进建议与整体美学结论。所有描述均由美学专家撰写并经过人工复核。参照这些黄金文本描述，我们可用单模态 GPT（Wu et al., 2023）从完整性、准确性与相关性三个维度衡量 MLLM 输出的质量。生成描述所用的 MLLM 提示语如下：

**EN** User: Describe and evaluate the aesthetic attribute in detail.

**ZH** 用户：详细描述并评价该图像的美学属性。

**EN** For images with medium and low aesthetic quality, we prompt MLLM to generate additional aesthetic improvement suggestions: Give suggestions for improvement. The specific GPT evaluation prompts can be found in Appendix B.6.

**ZH** 对美学质量中等与偏低的图像，我们提示 MLLM 额外给出美学改进建议：给出改进建议。GPT 评测所用的具体提示见附录 B.6。

**EN** 4.3. Aesthetic Assessment

**ZH** 4.3. 美学评价

**EN** The third task tests the zero-shot capability of MLLMs to provide quantitative scores of the overall aesthetic of images. Recent explorations (Wu et al., 2023) have observed that LMMs exhibit similar behavior patterns to humans when instructed to score, preferring to respond defined levels, such as good and poor. Using the prompt,

**ZH** 第三项任务测试 MLLM 对图像整体美学给出量化分数的零样本能力。近期探索（Wu et al., 2023）发现，LMM 在被要求打分时的行为模式与人类相似，倾向于用「好」「差」等既定等级作答。使用如下提示，

**EN** User: Rate this image from an aesthetic perspective.

**ZH** 用户：从美学角度为这张图像打分。

**EN** MLLM: The aesthetic quality is [Score Token].

**ZH** MLLM：其美学质量为[分数词元]。

**EN** MLLMs can provide log probabilities (logits) of the score token. The standard rating level texts (Series, 2012), are bad, poor, fair, good, excellent. Inspired by Q-bench(Wu et al., 2023) and Q-align(Wu et al., 2023), we employ softmax pooling on the logits of rating level words of the score token, to obtain their probabilities. Figure 3(c) gives an assessment example.

**ZH** MLLM 可给出分数词元的对数概率（logits）。标准评分等级文本（Series, 2012）为 bad、poor、fair、good、excellent。受 Q-bench（Wu et al., 2023）与 Q-align（Wu et al., 2023）启发，我们对分数词元在各评分等级词上的 logits 做 softmax 池化，得到相应概率。图 3(c) 给出一个评价示例。

**EN** The quantified scores ⟦SLOT_4⟧ for the five rating-level words:

**ZH** 五个评分等级词的量化分数 ⟦SLOT_4⟧ 如下：

**EN** Excellent: 5, Good: 4, Fair: 3, Poor: 2, Bad: 1

**ZH** Excellent: 5，Good: 4，Fair: 3，Poor: 2，Bad: 1

**EN** The probability calculation for each rating-level word is as follows:

**ZH** 各评分等级词的概率计算如下：

<!-- [原子块 · table] (1) p r i = e ℒ r i ∑ j = 1 5 e ℒ r j , p_{r_{i}}=\frac{e^{\mathcal{L}_{r_{i}}}}{\sum_{j=1}^{5}{e^{\mathcal{L}_{r_{j}}}}}, -->

**EN** where ⟦SLOT_5⟧ is the rating-level word, and ⟦SLOT_6⟧ represents the logits of the rating word output by MLLMs. We obtain an aesthetic quantification score of the image using MLLMs by multiplying the corresponding quantified score of the five rating-level adjectives by their respective probabilities:

**ZH** 其中 ⟦SLOT_5⟧ 为评分等级词，⟦SLOT_6⟧ 表示 MLLM 输出的该评分词的 logits。将五个评分等级形容词各自的量化分数与其概率相乘，即可得到 MLLM 给出的图像美学量化分数：

<!-- [原子块 · table] (2) S MLMM = ∑ i = 1 5 p r i ​ S i \mathrm{S_{MLMM}}=\sum_{i=1}^{5}p_{r_{i}}S_{i} -->

**EN** ⟦SLOT_7⟧ and the ground-truth scores will be used to calculate Spearman’s rank correlation coefficient (SRCC) and Pearson linear correlation coefficient (PLCC). The higher these two metrics are, the better the scoring ability of MLLMs. We select four mainstream IAA dataset sources: AVA, PARA, TAD66K, and Flick-Aes (Ren et al., 2017), of which the training set of the first two are used in the training process, while the latter two are not. They are depicted in Appendix B.3. It is worth noting that although we use the aesthetic information annotations of AVA and PARA during the training process, we do not use their MOS for training. So it is a zero-shot assessment task.

**ZH** ⟦SLOT_7⟧ 将与真实标注分数一起用于计算斯皮尔曼秩相关系数（SRCC）与皮尔逊线性相关系数（PLCC）。两项指标越高，说明 MLLM 的评分能力越强。我们选用四个主流 IAA 数据源：AVA、PARA、TAD66K 与 Flick-Aes（Ren et al., 2017），其中前两者的训练集参与了训练过程，后两者未参与，详见附录 B.3。需要说明的是，训练中虽使用了 AVA 与 PARA 的美学信息标注，但未使用它们的 MOS，因此这属于零样本评价任务。

**EN** 5. Experiments

**ZH** 5. 实验

**EN** We select LLaVA-1.5-7B (Liu et al., 2023b) as the base model, which contains a ViT-L image encoder, a LLaMA-2-7B, and an MLP connector. Detailed training information is in the Appendix A.5. In UNIAA-Bench, we assess 13 variants on the 10 most current and competitive open-source MLLMs, as well as GPT-4V and Gemini-Pro-Vision. We also report the perception results of human aesthetic judgment.

**ZH** 我们选用 LLaVA-1.5-7B（Liu et al., 2023b）作为基座模型，它包含一个 ViT-L 图像编码器、一个 LLaMA-2-7B 与一个 MLP 连接器，详细训练信息见附录 A.5。在 UNIAA-Bench 上，我们评估了 10 个最新且具竞争力的开源 MLLM 的 13 个变体，以及 GPT-4V 与 Gemini-Pro-Vision，同时还报告了人类美学判断的感知结果。

**EN** 5.1. Results on Aesthetic Perception

**ZH** 5.1. 美学感知结果

**EN** We assess the aesthetic perception of MLLMs by testing their capability to provide accurate responses to uncomplicated natural language queries related to aesthetic attributes. Table 1 summarizes the outcomes. It is pleasing to note that the majority of MLLMs can significantly surpass random guessing on all aesthetic attributes. Except for Qwen-VL, it will answer "uncertain" for some of the questions about aesthetic choices. We provide its response examples in the Appendix B.5. Given that these general-purpose models did not receive much explicit training on visual aesthetic attributes, these findings demonstrate their strong potential for aesthetics. By comparing UNIAA-LLaVA with the original LLaVA-1.5, it can be found that using aesthetic fine-tuning data obtained by the IAA conversion pipeline can significantly improve the aesthetic perception ability of MLLM. There is an increase of over 10% in almost all aesthetic dimensions. It is worth noting that the accuracy of composition has been improved from less than 50% to 66.82%. In terms of question types, the largest improvement is in the "How" type of questions, which increases by 30%. The simultaneous improvement of UNIAA-LLaVA in both in-the-wild and in-domain data proves its generalization of aesthetic perception ability. This finding demonstrates that aesthetic abilities are transferable and can be well generalized to unseen images. Compared with GPT-4V, we achieve a leading performance in four out of six dimensions except for the composition and content and have an overall accuracy higher than GPT-4V (78.48% vs. 74.74%). In addition to our model, two closed-source models have a high visual aesthetic perception ability in mainstream MLLMs. There is no doubt that GPT-4V is the strongest, with Gemini Pro ranking fourth among all models and only slightly behind mPLUG-Owl2. The best in open-source MLLM is mPLUG-Owl2, with its perceptual accuracy surpassing ShareGPT-4V by 3.59%. The most challenging perceptual dimension for MLLM is Composition, with most models not exceeding 60%. This may be due to the difficulty of the composition appreciation task and the diversity of composition techniques. Compared to "what" and "yes/no" questions, MLLMs generally have low accuracy in answering "how" questions, indicating that their ability to rate aesthetics needs to be improved.

**ZH** 我们通过测试 MLLM 能否准确回答与美学属性相关的简单自然语言提问来评估其美学感知能力，结果汇总于表 1。令人欣喜的是，多数 MLLM 在各美学属性上都能显著超过随机猜测。Qwen-VL 是个例外，它对部分美学选择题会回答「不确定」，相关回答示例见附录 B.5。考虑到这些通用模型并未接受过多少显式的视觉美学属性训练，上述结果说明它们在美学上具有很大潜力。对比 UNIAA-LLaVA 与原始 LLaVA-1.5 可见，使用 IAA 转换流程得到的美学微调数据能显著提升 MLLM 的美学感知能力，几乎所有美学维度上都有超过 10% 的提升，其中构图准确率从不足 50% 提高到 66.82%。从问题类型看，「How」类问题的提升最大，增幅达 30%。UNIAA-LLaVA 在开放场景与域内数据上同时提升，证明其美学感知能力具有泛化性，也说明美学能力可以迁移并良好泛化到未见过的图像。与 GPT-4V 相比，除构图与内容两项外，我们在其余四个维度上领先，整体准确率也高于 GPT-4V（78.48% vs. 74.74%）。除我们的模型外，主流 MLLM 中还有两个闭源模型具备较高的视觉美学感知能力：GPT-4V 无疑最强，Gemini Pro 在所有模型中排名第四，仅略低于 mPLUG-Owl2。开源 MLLM 中最好的是 mPLUG-Owl2，其感知准确率比 ShareGPT-4V 高 3.59%。对 MLLM 最具挑战的感知维度是构图，多数模型未超过 60%，这可能源于构图鉴赏任务本身的难度与构图技法的多样性。与「What」和「是／否」类问题相比，MLLM 回答「How」类问题的准确率普遍偏低，说明其美学评级能力仍有待提升。

**EN** MLLMs VS. Human. Although leading other models, UNIAA-LLaVA still lags behind Junior-level Humans slightly (78.48% VS. 79.01%). Despite its prowess, there is still a way to go for UNIAA-LLaVA before it can match the overall proficiency of the Senior-level Human (with experiences on visual aesthetic tasks, 10% better than UNIAA-LLaVA). The aspect in which the largest gap between MLLMs and humans exists is composition. The comparative results with human evaluation indicate that MLLMs still have a long way to go in terms of visual aesthetics, and it is necessary to continue enhancing the visual aesthetic ability of MLLMs.

**ZH** MLLM 对比人类。尽管领先其他模型，UNIAA-LLaVA 仍略逊于初级水平人类（78.48% vs. 79.01%）。要达到资深水平人类（具备视觉美学任务经验，比 UNIAA-LLaVA 高 10%）的整体水准，UNIAA-LLaVA 还有相当距离。MLLM 与人类差距最大的方面是构图。与人类评测的对比结果表明，MLLM 在视觉美学上仍有很长一段路要走，持续提升其视觉美学能力十分必要。

**EN** 5.2. Result on Aesthetic Description

**ZH** 5.2. 美学描述结果

**EN** In terms of descriptive ability, as shown in Table 2, GPT-4V achieves the highest performance and UNIAA-LLaVA takes the lead in completeness and preciseness. As accurate description is the most difficult, all MLLMs have not achieved a score of 1 or higher in preciseness. Instead, They achieve good scores in completeness, with scores higher than 0.8. Overall, only the GPT-4V, UNIAA-LLaVA, and ShareGPT-4V score over 3 out of 6. All the MLLMs fail the UNIAA-Describe test (3.6/6.0). MLLMs have relatively limited and basic abilities in providing aesthetic descriptions. Detailed examples and qualitative analysis can be found in Appendix C.3.

**ZH** 描述能力方面，如表 2 所示，GPT-4V 性能最高，UNIAA-LLaVA 则在完整性与准确性上领先。由于准确描述难度最大，所有 MLLM 的准确性都未达到 1 分及以上；而在完整性上表现较好，得分均高于 0.8。整体来看，只有 GPT-4V、UNIAA-LLaVA 与 ShareGPT-4V 在 6 分制下超过 3 分，所有 MLLM 都未能通过 UNIAA-Describe 测试（3.6/6.0）。MLLM 提供美学描述的能力相对有限且偏基础。详细示例与定性分析见附录 C.3。

**EN** Table 2. Evaluation on the Aesthetic Description. Due to the high cost and difficulty, human results are not be provided.

**ZH** 表 2. 美学描述评测结果。由于成本与难度较高，未提供人类结果。

<!-- [原子块 · table] MLLM Comp. Prec. Rele. Overall UNIAA-LLaVA 1.581 0.821 1.046 3.448 GPT-4V (CS) 1.448 0.754 1.372 3.574 ShareGPT-4V 1.427 0.722 0.978 3.127 LLaVA-1.5 1.271 0.709 0.948 2.928 LLaVA 1.287 0.673 0.956 2.9 -->

**EN** Table 3. Evaluation results on the Aesthetic Assessment ability. Metrics are PLCC/SRCC. Seen means using the data in training UNIAA-LLaVA, while unseen means not using. Due to the enormous quantity, we do not use human-assessment.

**ZH** 表 3. 美学评价能力评测结果。指标为 PLCC/SRCC。Seen 表示数据曾用于训练 UNIAA-LLaVA，unseen 表示未使用。由于样本量巨大，未采用人类评价。

<!-- [原子块 · table] Model AVA PARA TAD66K Flickr-Aes Seen Seen Unseen Unseen UNIAA-LLaVA 0.704/0.713 0.895/0.864 0.425/0.411 0.751/0.724 Aes-CLIP 0.637/0.647 - - - VILA 0.664/0.658 0.635/0.657 0.372/0.350 0.602/0.577 Q-I -->

**EN** 5.3. Result on Aesthetic Assessment

**ZH** 5.3. 美学评价结果

**EN** As depicted in 4.3, we use the score token to predict aesthetic scores, and compute the PLCC/SRCC concerning ground truth. The results are listed in Table 3. UNIAA-LLaVA leads zero-shot score performance on all four mainstream IAA datasets, even though it has not been trained on TAD66K and Flick-AES. It’s worth noting that we do not use MOS values during the training. The result indicates that we can fine-tune MLLMs effectively on Aesthetic Assessment by utilizing aesthetic knowledge transformed from IDCP. Additionally, we obtain the state-of-the-art (SOTA) performance on AVA and TAD66K by conducting supervised training using the vision encoder of UNIAA-LLaVA, as shown in Appendix C.1. We achieve a PLCC of 0.838 on AVA and 0.553 on TAD66K with our vision encoder and some additional linear layers.

**ZH** 如 4.3 节所述，我们用分数词元预测美学分数，并相对真实标注计算 PLCC/SRCC，结果列于表 3。UNIAA-LLaVA 在四个主流 IAA 数据集上的零样本评分性能均居首，即便它并未在 TAD66K 与 Flick-AES 上训练过。需要说明的是，训练过程中并未使用 MOS 值。该结果表明，借助 IDCP 转换得到的美学知识，可以有效微调 MLLM 完成美学评价。此外，如附录 C.1 所示，利用 UNIAA-LLaVA 的视觉编码器做监督训练，我们在 AVA 与 TAD66K 上取得了当前最优（SOTA）性能：在视觉编码器之外仅附加若干线性层，即在 AVA 上取得 0.838 的 PLCC、在 TAD66K 上取得 0.553。

**EN** Table 4. Ablation study. AA represents using aesthetic attribute data obtained from IDCP to optimize MLLM, while AC represents using aesthetic comment/description data. RAW represents using raw comment data without going through IDCP.

**ZH** 表 4. 消融实验。AA 表示使用 IDCP 得到的美学属性数据优化 MLLM，AC 表示使用美学评论／描述数据。RAW 表示使用未经 IDCP 处理的原始评论数据。

<!-- [原子块 · table] AA AC Perception Desc. TAD66K Flickr-Aes In-domain Wild Overall ✓ \checkmark ✓ \checkmark 78.78% 78.27% 78.48% 3.448 0.43/0.41 0.75/0.72 ✓ \checkmark × \times 75.68% 72.58% 73.87% 2.511 0.32/0.30 0.68 -->

**EN** 5.4. Ablation Study

**ZH** 5.4. 消融实验

**EN** 5.4.1. IDCP ablation experiments

**ZH** 5.4.1. IDCP 消融实验

**EN** To validate the effectiveness of IDCP, we conduct ablation experiments on aesthetic data types, cleaning steps, and additional MLLM, as shown in Table 4. When using only aesthetic attributes or aesthetic descriptions, a decrease in perception occurs in both cases, with a greater decrease observed in the latter. This reflects the importance of attributes and comments in improving aesthetic capabilities. The use of raw comments training led to a 3.8% decrease in WILD, demonstrating that lacking IDCP cleaning can affect generalization. Meanwhile, the description ability decreases significantly, indicating the necessity of rewriting the raw data using IDCP. When any of the IDCP stages is missing, the performance of the model will decrease to a different extent.

**ZH** 为验证 IDCP 的有效性，我们在美学数据类型、清洗步骤与附加 MLLM 三方面做了消融实验，见表 4。仅使用美学属性或仅使用美学描述时，感知能力均出现下降，后者降幅更大，说明属性与评论对提升美学能力都很重要。使用原始评论训练使 WILD 下降 3.8%，说明缺少 IDCP 清洗会影响泛化；同时描述能力显著下降，表明用 IDCP 改写原始数据确有必要。缺失 IDCP 任一阶段，模型性能都会有不同程度的下降。

**EN** Table 5. Results on Q-bench LLVisionQA dev set. QI represents Q-Instruct data for image quality assessment finetuning.

**ZH** 表 5. Q-bench LLVisionQA 开发集上的结果。QI 表示用于图像质量评估微调的 Q-Instruct 数据。

<!-- [原子块 · table] Method Acc. InstructBLIP 56.72% LLaVa-v1.5-7B 58.66% LLaMA-Adapter-V2 59.46% LLaVA-v1.5-13B 62.14% mPLUG-Owl2 62.90% InternLM-XComposer-VL 65.35% Qwen-VL-Plus (CS) 66.04% Gemini-pro-vison (CS) 68.16%  -->

**EN** 5.4.2. UNIAA on mPLUG-OWL2

**ZH** 5.4.2. UNIAA 在 mPLUG-OWL2 上的实验

**EN** We obtain the UNIAA-mPLUG-OWL2 using the same data of UNIAA-LLaVA, and find that its accuracy on the Aesthetic Perception is 77.89%, which is slightly lower than UNIAA-LLaVA and better than GPT-4V. This further proves the generality of IDCP. UNIAA-mPLUG-OWL2 also achieves significant improvements in both description and assessment compared to the vanilla model.

**ZH** 我们使用与 UNIAA-LLaVA 相同的数据得到 UNIAA-mPLUG-OWL2，其美学感知准确率为 77.89%，略低于 UNIAA-LLaVA 但优于 GPT-4V，进一步证明了 IDCP 的通用性。相比原始模型，UNIAA-mPLUG-OWL2 在描述与评价上也均有显著提升。

**EN** 5.4.3. Ablation of Fine-tuning the vision encoder.

**ZH** 5.4.3. 微调视觉编码器的消融实验

**EN** We freeze the weights of vision encoder during training while keeping other training settings consistent. The perception is 76.82%, lower than the original UNIAA-LLaVA (78.48%), and a similar trend is observed in assessment. It shows that IAA tasks require a finer level of visual perception. Freezing VE slightly improves aesthetic description.

**ZH** 我们在训练时冻结视觉编码器权重，其余训练设置保持不变。此时感知准确率为 76.82%，低于原始 UNIAA-LLaVA（78.48%），评价任务上也呈相同趋势，说明 IAA 任务确实需要更精细的视觉感知。冻结视觉编码器则对美学描述有轻微提升。

**EN** 5.4.4. Generalization on image quality benchmark.

**ZH** 5.4.4. 在图像质量基准上的泛化性

**EN** Q-bench (Wu et al., 2023) is a low-level visual benchmark on image quality assessment. As shown in Table 5, UNIAA-LLaVA performs surprisingly well. Without being trained on image quality datasets, it not only outperforms many open-source MLLMs, but also surpasses models trained using Q-instruct, which is specifically designed for image quality. The consistency result between Q-bench and UNIAA-Bench demonstrates the effectiveness of IDCP and the reliability of UNIAA-Bench.

**ZH** Q-bench（Wu et al., 2023）是面向图像质量评估的低层视觉基准。如表 5 所示，UNIAA-LLaVA 的表现意外地好：在未于图像质量数据集上训练的情况下，它不仅超过许多开源 MLLM，还超越了用专为图像质量设计的 Q-instruct 训练的模型。Q-bench 与 UNIAA-Bench 结果的一致性，证明了 IDCP 的有效性以及 UNIAA-Bench 的可靠性。

**EN** 6. Conclusion

**ZH** 6. 结论

**EN** In this work, we introduce Unified Multi-modal Image Aesthetic Assessment (UNIAA), a complete framework to enhance and examine the visual aesthetic ability of MLLMs, including UNIAA-LLaVA and UNIAA-Bench. We propose the first-of-a-kind multi-modal IAA Datasets Conversion Paradigm (IDCP). It permits MLLMs to substantially enhance accuracy in answering queries about visual aesthetic perception and also demonstrates the potential to produce more dependable aesthetic descriptions of images. Ultimately, this could serve to alleviate the workload of human experts in performing IAA. UNIAA-Bench examines MLLMs based on three crucial capabilities: the ability to perceive aesthetic attributes, the ability to provide an accurate and thorough aesthetic description, and the capacity to offer a score of aesthetic quality. The evaluation carried out by UNIAA-Bench has yielded two significant findings. The first finding is that UNIAA-LLaVA exhibits superior aesthetic abilities compared to other MLLM models, which serves as evidence of the effectiveness of IDCP. The second finding is that, in comparison to human experts, MLLMs still have a significant distance to traverse in order to become a truly dependable general visual aesthetic assistant. We sincerely hope that UNIAA can inspire future MLLMs to enhance their aesthetic abilities.

**ZH** 本文提出统一多模态图像美学评估（UNIAA），一套用于增强与检验 MLLM 视觉美学能力的完整框架，包含 UNIAA-LLaVA 与 UNIAA-Bench。我们提出了首个面向多模态图像美学的数据集转换范式（IDCP），它使 MLLM 在回答视觉美学感知类问题时的准确率大幅提升，并展现出生成更可靠图像美学描述的潜力，最终有望减轻人类专家从事 IAA 的工作负担。UNIAA-Bench 从三项关键能力考察 MLLM：感知美学属性的能力、给出准确而全面的美学描述的能力，以及给出美学质量分数的能力。基于 UNIAA-Bench 的评测得到两点重要发现。第一，UNIAA-LLaVA 的美学能力优于其他 MLLM 模型，这印证了 IDCP 的有效性。第二，与人类专家相比，MLLM 要成为真正可靠的通用视觉美学助手仍有很大的差距。我们诚挚希望 UNIAA 能启发未来的 MLLM 提升其美学能力。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] Deng et al . (2017) Yubin Deng, Chen Change Loy, and Xiaoou Tang. 2017. Image aesthetic assessment: An experimental survey. IEEE Signal Processing Magazine 34, 4 (2017), 80–106. -->

<!-- [原子块 · verbatim] Hou et al . (2022) Jingwen Hou, Henghui Ding, Weisi Lin, Weide Liu, and Yuming Fang. 2022. Distilling knowledge from object classification to aesthetics assessment. IEEE Transactions on Circuits and S -->

<!-- [原子块 · verbatim] Niu et al . (2022) Yuzhen Niu, Shanshan Chen, Bingrui Song, Zhixian Chen, and Wenxi Liu. 2022. Comment-guided semantics-aware image aesthetics assessment. IEEE Transactions on Circuits and Systems for -->

<!-- [原子块 · verbatim] Liu et al . (2021) Fangcen Liu, Chenqiang Gao, Yongqing Sun, Yue Zhao, Feng Yang, Anyong Qin, and Deyu Meng. 2021. Infrared and visible cross-modal image retrieval through shared features. IEEE Transa -->

<!-- [原子块 · verbatim] Guo et al . (2017) Cong Guo, Xinmei Tian, and Tao Mei. 2017. Multigranular event recognition of personal photo albums. IEEE Transactions on Multimedia 20, 7 (2017), 1837–1847. -->

<!-- [原子块 · verbatim] Rawat and Kankanhalli (2016) Yogesh Singh Rawat and Mohan S Kankanhalli. 2016. ClickSmart: A context-aware viewpoint recommendation system for mobile photography. IEEE Transactions on Circuits and Sys -->

<!-- [原子块 · verbatim] Chai et al . (2020) Xiongli Chai, Feng Shao, Qiuping Jiang, and Yo-Sung Ho. 2020. Roundness-preserving warping for aesthetic enhancement-based stereoscopic image editing. IEEE Transactions on Circuits -->

<!-- [原子块 · verbatim] Yang et al . (2019) Hongtao Yang, Ping Shi, Saike He, Da Pan, Zefeng Ying, and Ling Lei. 2019. A comprehensive survey on image aesthetic quality assessment. In 2019 IEEE/ACIS 18th International Confer -->

<!-- [原子块 · verbatim] Murray et al . (2012) Naila Murray, Luca Marchesotti, and Florent Perronnin. 2012. AVA: A large-scale database for aesthetic visual analysis. In 2012 IEEE conference on computer vision and pattern rec -->

<!-- [原子块 · verbatim] Kong et al . (2016) Shu Kong, Xiaohui Shen, Zhe Lin, Radomir Mech, and Charless Fowlkes. 2016. Photo aesthetics ranking network with attributes and content adaptation. In European conference on comput -->

<!-- [原子块 · verbatim] Yang et al . (2022) Yuzhe Yang, Liwu Xu, Leida Li, Nan Qie, Yaqian Li, Peng Zhang, and Yandong Guo. 2022. Personalized Image Aesthetics Assessment With Rich Attributes. In Proceedings of the IEEE/CVF  -->

<!-- [原子块 · verbatim] He et al . (2022) Shuai He, Yongchang Zhang, Rui Xie, Dongxiang Jiang, and Anlong Ming. 2022. Rethinking Image Aesthetics Assessment: Models, Datasets and Benchmarks. In Proceedings of the Thirty-Firs -->

<!-- [原子块 · verbatim] Jin et al . (2019) Xin Jin, Le Wu, Geng Zhao, Xiaodong Li, Xiaokun Zhang, Shiming Ge, Dongqing Zou, Bin Zhou, and Xinghui Zhou. 2019. Aesthetic attributes assessment of images. In Proceedings of the 2 -->

<!-- [原子块 · verbatim] Xiong et al . (2023) Zhiwei Xiong, Yunfan Zhang, Zhiqi Shen, Peiran Ren, and Han Yu. 2023. Image Aesthetics Assessment via Learnable Queries. arXiv preprint arXiv:2309.02861 (2023). -->

<!-- [原子块 · verbatim] He et al . (2023) Shuai He, Anlong Ming, Shuntian Zheng, Haobin Zhong, and Huadong Ma. 2023. EAT: An Enhancer for Aesthetics-Oriented Transformers. In Proceedings of the 31st ACM International Confere -->

<!-- [原子块 · verbatim] Talebi and Milanfar (2018) Hossein Talebi and Peyman Milanfar. 2018. NIMA: Neural image assessment. IEEE transactions on image processing 27, 8 (2018), 3998–4011. -->

<!-- [原子块 · verbatim] Chen et al . (2020) Qiuyu Chen, Wei Zhang, Ning Zhou, Peng Lei, Yi Xu, Yu Zheng, and Jianping Fan. 2020. Adaptive Fractional Dilated Convolution Network for Image Aesthetics Assessment. In IEEE/CVF Co -->

<!-- [原子块 · verbatim] Hosu et al . (2019) Vlad Hosu, Bastian Goldlucke, and Dietmar Saupe. 2019. Effective Aesthetics Prediction With Multi-Level Spatially Pooled Features. In Proceedings of the IEEE/CVF Conference on Comp -->

<!-- [原子块 · verbatim] Ke et al . (2021) Junjie Ke, Qifei Wang, Yilin Wang, Peyman Milanfar, and Feng Yang. 2021. MUSIQ: Multi-Scale Image Quality Transformer. In Proceedings of the IEEE/CVF International Conference on Comp -->

<!-- [原子块 · verbatim] Xia et al . (2022) Zhuofan Xia, Xuran Pan, Shiji Song, Li Erran Li, and Gao Huang. 2022. Vision transformer with deformable attention. In Proceedings of the IEEE/CVF conference on computer vision and  -->

<!-- [原子块 · verbatim] He et al . (2023) Shuai He, Anlong Ming, Yaqi Li, Jinyuan Sun, ShunTian Zheng, and Huadong Ma. 2023. Thinking image color aesthetics assessment: Models, datasets and benchmarks. In Proceedings of the  -->

<!-- [原子块 · verbatim] Ke et al . (2023) Junjie Ke, Keren Ye, Jiahui Yu, Yonghui Wu, Peyman Milanfar, and Feng Yang. 2023. VILA: Learning Image Aesthetics from User Comments with Vision-Language Pretraining. In Proceedings  -->

<!-- [原子块 · verbatim] Vera Nieto et al . (2022) Daniel Vera Nieto, Luigi Celona, and Clara Fernandez Labrador. 2022. Understanding Aesthetics with Language: A Photo Critique Dataset for Aesthetic Assessment. Advances in Ne -->

<!-- [原子块 · verbatim] Leder et al . (2004) Helmut Leder, Benno Belke, Andries Oeberst, and Dorothee Augustin. 2004. A model of aesthetic appreciation and aesthetic judgments. British journal of psychology 95, 4 (2004), 489 -->

<!-- [原子块 · verbatim] Chatterjee (2004) Anjan Chatterjee. 2004. Prospects for a cognitive neuroscience of visual aesthetics. Bulletin of Psychology and the Arts 4, 2 (2004), 56–60. -->

<!-- [原子块 · verbatim] OpenAI (2023) OpenAI. 2023. GPT-4V(ision) System Card. https://api.semanticscholar.org/CorpusID:263218031 . -->

<!-- [原子块 · verbatim] Alayrac et al . (2022) Jean-Baptiste Alayrac, Jeff Donahue, Pauline Luc, Antoine Miech, Iain Barr, Yana Hasson, Karel Lenc, Arthur Mensch, Katie Millican, Malcolm Reynolds, Roman Ring, Eliza Rutherfor -->

<!-- [原子块 · verbatim] Li et al . (2022) Junnan Li, Dongxu Li, Silvio Savarese, and Steven C. H. Hoi. 2022. BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models. In ICML . -->

<!-- [原子块 · verbatim] Driess et al . (2023) Danny Driess, F. Xia, Mehdi S. M. Sajjadi, Corey Lynch, Aakanksha Chowdhery, Brian Ichter, Ayzaan Wahid, Jonathan Tompson, Quan Ho Vuong, Tianhe Yu, Wenlong Huang, Yevgen Chebota -->

<!-- [原子块 · verbatim] Zhu et al . (2023) Deyao Zhu, Jun Chen, Xiaoqian Shen, Xiang Li, and Mohamed Elhoseiny. 2023. MiniGPT-4: Enhancing Vision-Language Understanding with Advanced Large Language Models. arXiv preprint arX -->

<!-- [原子块 · verbatim] Liu et al . (2023) Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. 2023. Visual Instruction Tuning. -->

<!-- [原子块 · verbatim] Huang et al . (2023) Shaohan Huang, Li Dong, Wenhui Wang, Yaru Hao, Saksham Singhal, Shuming Ma, Tengchao Lv, Lei Cui, Owais Khan Mohammed, Qiang Liu, Kriti Aggarwal, Zewen Chi, Johan Bjorck, Vishrav  -->

<!-- [原子块 · verbatim] Li et al . (2023) Kunchang Li, Yinan He, Yi Wang, Yizhuo Li, Wen Wang, Ping Luo, Yali Wang, Limin Wang, and Yu Qiao. 2023. VideoChat: Chat-Centric Video Understanding. ArXiv abs/2305.06355 (2023). -->

<!-- [原子块 · verbatim] Schaeffer et al . (2023) Rylan Schaeffer, Brando Miranda, and Sanmi Koyejo. 2023. Are emergent abilities of Large Language Models a mirage? arXiv preprint arXiv:2304.15004 (2023). -->

<!-- [原子块 · verbatim] Liu et al . (2023a) Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. 2023a. Visual instruction tuning. arXiv preprint arXiv:2304.08485 (2023). -->

<!-- [原子块 · verbatim] Liu et al . (2023b) Haotian Liu, Chunyuan Li, Yuheng Li, and Yong Jae Lee. 2023b. Improved baselines with visual instruction tuning. arXiv preprint arXiv:2310.03744 (2023). -->

<!-- [原子块 · verbatim] Wu et al . (2023) Haoning Wu, Zicheng Zhang, Erli Zhang, Chaofeng Chen, Liang Liao, Annan Wang, Chunyi Li, Wenxiu Sun, Qiong Yan, Guangtao Zhai, and Weisi Lin. 2023. Q-Bench: A Benchmark for General-P -->

<!-- [原子块 · verbatim] Li et al . (2023) Leida Li, Yipo Huang, Jinjian Wu, Yuzhe Yang, Yaqian Li, Yandong Guo, and Guangming Shi. 2023. Theme-aware Visual Attribute Reasoning for Image Aesthetics Assessment. IEEE Transactio -->

<!-- [原子块 · verbatim] Karayev et al . (2014) Sergey Karayev, Matthew Trentacoste, Helen Han, Aseem Agarwala, Trevor Darrell, Aaron Hertzmann, and Holger Winnemoeller. 2014. Recognizing Image Style. In Proceedings of the Br -->

<!-- [原子块 · verbatim] Tang et al . (2013) Xiaoou Tang, Wei Luo, and Xiaogang Wang. 2013. Content-based photo quality assessment. IEEE Transactions on Multimedia 15, 8 (2013), 1930–1943. -->

<!-- [原子块 · verbatim] Ren et al . (2017) Jian Ren, Xiaohui Shen, Zhe Lin, Radomir Mech, and David J. Foran. 2017. Personalized Image Aesthetics. In The IEEE International Conference on Computer Vision (ICCV) . -->

<!-- [原子块 · verbatim] Lee et al . (2018) Jun-Tae Lee, Han-Ul Kim, Chul Lee, and Chang-Su Kim. 2018. Photographic composition classification and dominant geometric element detection for outdoor scenes. Journal of Visual Com -->

<!-- [原子块 · verbatim] Celona et al . (2022) Luigi Celona, Marco Leonardi, Paolo Napoletano, and Alessandro Rozza. 2022. Composition and style attributes guided image aesthetic assessment. IEEE Transactions on Image Process -->

<!-- [原子块 · verbatim] Zhou et al . (2016) Ye Zhou, Xin Lu, Junping Zhang, and James Z Wang. 2016. Joint image and text representation for aesthetics analysis. In Proceedings of the 24th ACM international conference on Mult -->

<!-- [原子块 · verbatim] Wang et al . (2019) Wenshan Wang, Su Yang, Weishan Zhang, and Jiulong Zhang. 2019. Neural aesthetic image reviewer. IET Computer Vision 13, 8 (2019), 749–758. -->

<!-- [原子块 · verbatim] Radford et al . (2021) Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, and Ilya Su -->

<!-- [原子块 · verbatim] Chang et al . (2017) Kuang-Yu Chang, Kung-Hung Lu, and Chu-Song Chen. 2017. Aesthetic critiques generation for photos. In Proceedings of the IEEE international conference on computer vision . 3514–352 -->

<!-- [原子块 · verbatim] Kang et al . (2020) Chen Kang, Giuseppe Valenzise, and Frédéric Dufaux. 2020. EVA: An Explainable Visual Aesthetics Dataset. In Joint Workshop on Aesthetic and Technical Quality Assessment of Multimed -->

<!-- [原子块 · verbatim] OpenAI (2023) OpenAI. 2023. GPT-4 Technical Report. arXiv:2303.08774 [cs.CL] -->

<!-- [原子块 · verbatim] Chung et al . (2022) Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang, Mostafa Dehghani, Siddhartha Brahma, Albert Webson, Shixiang Shane Gu, Zhuyun Da -->

<!-- [原子块 · verbatim] Touvron et al . (2023) Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, Aurelien Rodrigue -->

<!-- [原子块 · verbatim] Li et al . (2023) Bo Li, Yuanhan Zhang, Liangyu Chen, Jinghao Wang, Jingkang Yang, and Ziwei Liu. 2023. Otter: A Multi-Modal Model with In-Context Instruction Tuning. ArXiv abs/2305.03726 (2023). -->

<!-- [原子块 · verbatim] Gao et al . (2023) Peng Gao, Jiaming Han, Renrui Zhang, Ziyi Lin, Shijie Geng, Aojun Zhou, Wei Zhang, Pan Lu, Conghui He, Xiangyu Yue, Hongsheng Li, and Yu Qiao. 2023. LLaMA-Adapter V2: Parameter-Effi -->

<!-- [原子块 · verbatim] Dai et al . (2023) Wenliang Dai, Junnan Li, Dongxu Li, Anthony Meng Huat Tiong, Junqi Zhao, Weisheng Wang, Boyang Li, Pascale Fung, and Steven Hoi. 2023. InstructBLIP: Towards General-purpose Vision-L -->

<!-- [原子块 · verbatim] Zhang et al . (2023) Pan Zhang, Xiaoyi Dong, Bin Wang, Yuhang Cao, Chao Xu, Linke Ouyang, Zhiyuan Zhao, Shuangrui Ding, Songyang Zhang, Haodong Duan, Wenwei Zhang, Hang Yan, Xinyue Zhang, Wei Li, Jing -->

<!-- [原子块 · verbatim] Chen et al . (2015) Xinlei Chen, Hao Fang, Tsung-Yi Lin, Ramakrishna Vedantam, Saurabh Gupta, Piotr Dollar, and C. Lawrence Zitnick. 2015. Microsoft COCO Captions: Data Collection and Evaluation Serve -->

<!-- [原子块 · verbatim] Agrawal et al . (2019) Harsh Agrawal, Karan Desai, Yufei Wang, Xinlei Chen, Rishabh Jain, Mark Johnson, Dhruv Batra, Devi Parikh, Stefan Lee, and Peter Anderson. 2019. nocaps: novel object captioning  -->

<!-- [原子块 · verbatim] Young et al . (2014) Peter Young, Alice Lai, Micah Hodosh, and Julia Hockenmaier. 2014. From image descriptions to visual denotations: New similarity metrics for semantic inference over event descript -->

<!-- [原子块 · verbatim] Antol et al . (2015) Stanislaw Antol, Aishwarya Agrawal, Jiasen Lu, Margaret Mitchell, Dhruv Batra, C. Lawrence Zitnick, and Devi Parikh. 2015. VQA: Visual Question Answering. In ICCV . -->

<!-- [原子块 · verbatim] Marino et al . (2019) Kenneth Marino, Mohammad Rastegari, Ali Farhadi, and Roozbeh Mottaghi. 2019. OK-VQA: A Visual Question Answering Benchmark Requiring External Knowledge. In Conference on Computer -->

<!-- [原子块 · verbatim] Schwenk et al . (2022) Dustin Schwenk, Apoorv Khandelwal, Christopher Clark, Kenneth Marino, and Roozbeh Mottaghi. 2022. A-OKVQA: A Benchmark for Visual Question Answering using World Knowledge. arXiv -->

<!-- [原子块 · verbatim] Liu et al . (2023) Yuanzhan Liu, Haodong Duan, Yuanhan Zhang, Bo Li, Songyang Zhang, Wangbo Zhao, Yike Yuan, Jiaqi Wang, Conghui He, Ziwei Liu, Kai Chen, and Dahua Lin. 2023. MMBench: Is Your Multi-mo -->

<!-- [原子块 · verbatim] Fu et al . (2023) Chaoyou Fu, Peixian Chen, Yunhang Shen, Yulei Qin, Mengdan Zhang, Xu Lin, Zhenyu Qiu, Wei Lin, Jinrui Yang, Xiawu Zheng, Ke Li, Xing Sun, and Rongrong Ji. 2023. MME: A Comprehensive  -->

<!-- [原子块 · verbatim] Li et al . (2023) Bohao Li, Rui Wang, Guangzhi Wang, Yuying Ge, Yixiao Ge, and Ying Shan. 2023. SEED-Bench: Benchmarking Multimodal LLMs with Generative Comprehension. arXiv:2307.16125 [cs.CL] -->

<!-- [原子块 · verbatim] Lin et al . (2023) Bin Lin, Bin Zhu, Yang Ye, Munan Ning, Peng Jin, and Li Yuan. 2023. Video-llava: Learning united visual representation by alignment before projection. arXiv preprint arXiv:2311.1012 -->

<!-- [原子块 · verbatim] Lin et al . (2024) Bin Lin, Zhenyu Tang, Yang Ye, Jiaxi Cui, Bin Zhu, Peng Jin, Junwu Zhang, Munan Ning, and Li Yuan. 2024. Moe-llava: Mixture of experts for large vision-language models. arXiv prepri -->

<!-- [原子块 · verbatim] Zhu et al . (2023) Bin Zhu, Bin Lin, Munan Ning, Yang Yan, Jiaxi Cui, HongFa Wang, Yatian Pang, Wenhao Jiang, Junwu Zhang, Zongwei Li, et al . 2023. Languagebind: Extending video-language pretraining  -->

<!-- [原子块 · verbatim] Jin et al . (2023) Peng Jin, Ryuichi Takanobu, Caiwan Zhang, Xiaochun Cao, and Li Yuan. 2023. Chat-UniVi: Unified Visual Representation Empowers Large Language Models with Image and Video Understandin -->

<!-- [原子块 · verbatim] Wu et al . (2023) Haoning Wu, Zicheng Zhang, Weixia Zhang, Chaofeng Chen, Liang Liao, Chunyi Li, Yixuan Gao, Annan Wang, Erli Zhang, Wenxiu Sun, et al . 2023. Q-align: Teaching lmms for visual scoring -->

<!-- [原子块 · verbatim] Li et al . (2023) Chunyuan Li, Cliff Wong, Sheng Zhang, Naoto Usuyama, Haotian Liu, Jianwei Yang, Tristan Naumann, Hoifung Poon, and Jianfeng Gao. 2023. Llava-med: Training a large language-and-vision -->

<!-- [原子块 · verbatim] Wu et al . (2023) Haoning Wu, Zicheng Zhang, Erli Zhang, Chaofeng Chen, Liang Liao, Annan Wang, Kaixin Xu, Chunyi Li, Jingwen Hou, Guangtao Zhai, et al . 2023. Q-instruct: Improving low-level visual a -->

<!-- [原子块 · verbatim] Xu et al . (2023) Zhenhua Xu, Yujia Zhang, Enze Xie, Zhen Zhao, Yong Guo, Kenneth KY Wong, Zhenguo Li, and Hengshuang Zhao. 2023. Drivegpt4: Interpretable end-to-end autonomous driving via large langu -->

<!-- [原子块 · verbatim] Chen et al . (2023) Lin Chen, Jisong Li, Xiaoyi Dong, Pan Zhang, Conghui He, Jiaqi Wang, Feng Zhao, and Dahua Lin. 2023. Sharegpt4v: Improving large multi-modal models with better captions. arXiv prep -->

<!-- [原子块 · verbatim] OpenAI (2023a) OpenAI. 2023a. ChatGPT (June 13 version). https://chat.openai.com/chat Large language model. -->

<!-- [原子块 · verbatim] OpenAI (2023b) OpenAI. 2023b. GPT-4 Technical Report. ArXiv abs/2303.08774 (2023). -->

<!-- [原子块 · verbatim] Schuhmann et al . (2021) Christoph Schuhmann, Richard Vencu, Romain Beaumont, Robert Kaczmarczyk, Clayton Mullis, Aarush Katta, Theo Coombes, Jenia Jitsev, and Aran Komatsuzaki. 2021. LAION-400M: Open -->

<!-- [原子块 · verbatim] Sharma et al . (2018) Piyush Sharma, Nan Ding, Sebastian Goodman, and Radu Soricut. 2018. Conceptual Captions: A Cleaned, Hypernymed, Image Alt-text Dataset For Automatic Image Captioning. In ACL . -->

<!-- [原子块 · verbatim] Yu et al . (2016) Licheng Yu, Patrick Poirson, Shan Yang, Alexander C. Berg, and Tamara L. Berg. 2016. Modeling Context in Referring Expressions. arXiv:1608.00272 [cs.CV] -->

<!-- [原子块 · verbatim] Liu et al . (2019) Dong Liu, Rohit Puri, Nagendra Kamath, and Subhabrata Bhattacharya. 2019. Modeling image composition for visual aesthetic assessment. In Proceedings of the IEEE/CVF Conference on Co -->

<!-- [原子块 · verbatim] Feng et al . (2023) Tinglei Feng, Jiaxuan Liu, and Jufeng Yang. 2023. Probing Sentiment-Oriented Pre-Training Inspired by Human Sentiment Perception Mechanism. In Proceedings of the IEEE/CVF Conferenc -->

<!-- [原子块 · verbatim] Chen et al . (2023) Yi Chen, Yuying Ge, Yixiao Ge, Mingyu Ding, Bohao Li, Rui Wang, Ruifeng Xu, Ying Shan, and Xihui Liu. 2023. EgoPlan-Bench: Benchmarking Egocentric Embodied Planning with Multimodal -->

<!-- [原子块 · verbatim] Wu et al . (2023) Haoning Wu, Erli Zhang, Liang Liao, Chaofeng Chen, Jingwen Hou, Annan Wang, Wenxiu Sun, Qiong Yan, and Weisi Lin. 2023. Towards explainable in-the-wild video quality assessment: a da -->

<!-- [原子块 · verbatim] Series (2012) B Series. 2012. Methodology for the subjective assessment of the quality of television pictures. Recommendation ITU-R BT 500, 13 (2012). -->

<!-- [原子块 · verbatim] Ren et al . (2017) Jian Ren, Xiaohui Shen, Zhe Lin, Radomir Mech, and David J Foran. 2017. Personalized image aesthetics. In Proceedings of the IEEE international conference on computer vision . 638–6 -->

<!-- [原子块 · verbatim] Ma et al . (2017) Shuang Ma, Jing Liu, and Chang Wen Chen. 2017. A-lamp: Adaptive layout-aware multi-patch deep convolutional neural network for photo aesthetic assessment. In Proceedings of the IEEE  -->

<!-- [原子块 · verbatim] She et al . (2021) Dongyu She, Yu-Kun Lai, Gaoxiong Yi, and Kun Xu. 2021. Hierarchical layout-aware graph convolutional network for unified aesthetics assessment. In Proceedings of the IEEE/CVF Confer -->

<!-- [原子块 · verbatim] Tu et al . (2022) Zhengzhong Tu, Hossein Talebi, Han Zhang, Feng Yang, Peyman Milanfar, Alan Bovik, and Yinxiao Li. 2022. MaxViT: Multi-Axis Vision Transformer. European conference on computer vision  -->

**EN** Appendix A More Information of IDCP

**ZH** 附录 A IDCP 的更多信息

**EN** A.1. Data Source Details

**ZH** A.1. 数据来源细节

**EN** The sample size of IDCP using five IAA datasets sources is shown in Table 6. Overall Comments provide a general evaluation of the photo. Photo Style is an annotation of the photographic and aesthetic style, such as macro photography, motion blur, long exposure, etc. Binary Attributes are binary annotations of aesthetic attributes, Such as whether there is balance in the elements, and whether the rule of thirds is applied. Attributes Level is an evaluation of the quality level of the aesthetic attributes. Single Attribute Comments are comments about a specific dimension of the photo, and Color Scheme is an annotation of the color combinations in the photo.

**ZH** IDCP 所用五个 IAA 数据来源的样本量见表 6。Overall Comments（整体评论）给出对照片的总体评价；Photo Style（摄影风格）是对摄影与美学风格的标注，如微距摄影、运动模糊、长曝光等；Binary Attributes（二值属性）是对美学属性的二值标注，如画面元素是否平衡、是否应用三分法；Attributes Level（属性等级）是对美学属性质量等级的评价；Single Attribute Comments（单属性评论）是针对照片某一具体维度的评论；Color Scheme（色彩搭配）是对照片色彩组合的标注。

**EN** Table 6. Datasets resource detail. The total number of data sources is 278,181.

**ZH** 表 6. 数据集来源细节。数据来源总数为 278,181。

<!-- [原子块 · table] Dataset Annotation Size AVA Overall Commments 26562 Photo style 30957 AADB Binary Attributes 30976 PARA Attributes Level 141100 PCCD Overall Comments 4202 Single Attribute Comments 27033 ICAA17K Color -->

**EN** A.2. Prompt of Question Generation on Aesthetic Attributes

**ZH** A.2. 美学属性问题生成提示

**EN** We first assign the role of an aesthetic expert to ChatGPT and ask it to design a question based on a specific aesthetic dimension. Then, while maintaining the same meaning, we ask it to expand the question into multiple different sentence structures. The following is a prompt for designing a question about composition.

**ZH** 我们先为 ChatGPT 指定美学专家角色，让它围绕某一具体美学维度设计问题，然后要求它在保持语义不变的前提下把问题扩展为多种不同句式。以下是围绕构图设计问题的提示。

**EN** User: Assuming you are an aesthetic expert, please design a question to ask What kind of composition is used for this photo. Rewrite the question into five different sentences with the same meaning.

**ZH** 用户：假设你是一位美学专家，请设计一个问题来询问这张照片使用了何种构图方式。请将该问题改写为五个语义相同的不同句子。

**EN** A.3. Prompt of Description Generation

**ZH** A.3. 描述生成提示

**EN** Given an image, we use LLaVA to generate its content. LLaVA is required to output the image content and spatial information. It is not allowed to provide any aesthetic-related information to prevent any interference with the real aesthetic annotation.

**ZH** 给定一张图像，我们用 LLaVA 生成其内容描述，要求 LLaVA 输出图像内容与空间信息，且不允许提供任何与美学相关的信息，以免干扰真实的美学标注。

**EN** User: Provide a detailed description of this image, including the spatial and relative position of the elements in the picture. Do not output any information related to aesthetics, such as atmosphere, emotion, and the beauty of the scenery, etc.

**ZH** 用户：请详细描述这张图像，包括画面中各元素的空间位置与相对位置。不要输出任何与美学相关的信息，例如氛围、情感、景物是否美观等。

**EN** We input the annotated comments and the captions generated by LLaVA into GPT and request GPT to rewrite the comments.

**ZH** 我们把标注评论与 LLaVA 生成的描述一并输入 GPT，要求 GPT 改写评论。

**EN** User: Assistant is a professional aesthetic critic.

**ZH** 用户：助手是一位专业的美学评论家。

**EN** The assistant is a highly professional individual who possesses a remarkable eye for aesthetics and aligns well with the views of the general public. Instructions: - You’re given a caption of an image and some comments on the image from a photography website.

**ZH** 这位助手高度专业，具备出色的审美眼光，与大众的审美取向高度一致。指令：- 你会得到一张图像的文字描述，以及来自某摄影网站对这幅图像的一些评论。

**EN** - Step1: Rewrite the comments into professional aesthetic comments and ignore those comments that are not highly related to aesthetics or only expressions of personal affection. Please be objective and do not use colloquial words.

**ZH** - 第一步：将这些评论改写为专业的美学评论，忽略那些与美学关联不强或只是个人情感表达的评论。请保持客观，不要使用口语化词汇。

**EN** - Step2: Summarize the rewritten aesthetic comments and your answers in Step2 into one complete aesthetic comment written by a professional aesthetic critic. You may refer to the image caption as though you are truly seeing this image, but please focus solely on the aesthetic-related content.

**ZH** - 第二步：把改写后的美学评论与你在第二步中的回答整合为一段完整的、由专业美学评论家撰写的美学评论。你可以参考图像描述，如同亲眼看到这幅图像，但请只关注与美学相关的内容。

**EN** When the image caption conflicts with the given comments, follow the comments. Do not imagine and give irrelevant or groundless responses regarding the given comments.

**ZH** 当图像描述与给定评论冲突时，以评论为准。不要凭空想象，也不要给出与给定评论无关或无根据的回答。

**EN** A.4. Examples of IDCP Data

**ZH** A.4. IDCP 数据示例

**EN** Following are some examples of training data obtained through IDCP transformation.

**ZH** 以下是经 IDCP 转换得到的部分训练数据示例。

**EN** Aesthetic Attributes AVA: Question: What kind of photography style is this image in? Answer: Soft Focus.

**ZH** 美学属性 AVA：问题：这幅图像属于何种摄影风格？回答：柔焦。

**EN** AADB: Question: Are the elements in this image balancing? Answer: No.

**ZH** AADB：问题：这幅图像中的元素是否平衡？回答：否。

**EN** PARA: Question: How would you rate the composition of this image? Answer: The image has a fair score of composition.

**ZH** PARA：问题：你如何评价这幅图像的构图？回答：该图像的构图得分一般。

**EN** ICAA17K: Question: What is the color scheme employed in this picture? Answer: Complementary.

**ZH** ICAA17K：问题：这幅图像采用了何种色彩搭配？回答：互补色。

**EN** Question: What complementary colors are used in this photo? Answer: Orange and Violet.

**ZH** 问题：这张照片使用了哪些互补色？回答：橙色与紫色。

**EN** Aesthetic Comments AVA: Question: What is your overall impression of this image from an aesthetic viewpoint? Answer: The image seems to be the result of well-coordinated, meticulous work that features impressive captures of the lunar eclipse across different stages. The successful inclusion of background stars further enriches the image’s overall visual appeal and depth. Expert editing appears to have been utilized proficiently, contributing substantially to the enchanting allure of the artwork. However, a minor flaw can be noted on the eighth moon, indicating room for further refinements. The work invokes a blend of admiration and curiosity, leaving the observer to ponder whether this breathtaking display was captured entirely in nature or whether digital enhancements played a role. Nonetheless, the image stands out as a favorite due to its unique and striking aesthetic elements.

**ZH** 美学评论 AVA：问题：从美学视角看，你对这幅图像的整体印象如何？回答：这幅图像似乎是经过精心协调与细致打磨的成果，精彩地记录了月食的不同阶段。背景星空的巧妙纳入进一步丰富了画面的整体视觉感染力与纵深。看来运用了娴熟的专业后期处理，极大增添了作品的魅力。不过第八个月亮上可以注意到一个细微瑕疵，说明仍有改进空间。作品唤起了赞叹与好奇交织的感受，让观者不禁思考这一震撼景象究竟是完全实拍，还是借助了数字增强。尽管如此，凭借其独特而醒目的美学元素，这幅图像仍不失为一件出众之作。

**EN** PCCD: Question: Summarize your aesthetic evaluations of this image as if you are a professional aesthetic critic. Answer: The composition of the image is well-executed, with the baby girl placed in the center and occupying a significant portion of the frame. The use of a white blanket as the background creates a serene and soothing atmosphere. The pink bow in the baby’s hair adds a touch of color and serves as the main focal point of the image. The lighting, with its rosy effect, enhances the overall aesthetic appeal, giving the image a gentle and warm tone. However, the image lacks a strong emotional impact and fails to capture the viewer’s attention.

**ZH** PCCD：问题：请以专业美学评论家的身份总结你对这幅图像的美学评价。回答：图像构图处理得当，女婴居于画面中央并占据较大画幅。以白色毯子作为背景营造出宁静舒缓的氛围；女婴发间的粉色蝴蝶结增添了一抹色彩，并成为画面的主要视觉焦点。带有玫瑰色调的光线增强了整体美感，使画面呈现柔和温暖的基调。不过，图像缺乏强烈的情感冲击力，未能抓住观者的注意力。

**EN** PCCD: Question: How would you evaluate the aesthetic expression of the use of camera of this image? Answer: The photographer made skillful choices in the use of the camera for this image. The angle chosen provides an interesting perspective, allowing us to fully appreciate the details of the subject. The f-stop and shutter speed selection contribute to the clean and well-captured image, ensuring that the details are sharp and clear.

**ZH** PCCD：问题：你如何评价这幅图像在相机使用上的美学表达？回答：摄影师在相机使用上做出了娴熟的选择：所选角度提供了富有趣味的视角，使我们得以充分欣赏主体的细节；光圈与快门的选择令画面干净利落，确保细节清晰锐利。

**EN** A.5. Hyper-parameters of Training

**ZH** A.5. 训练超参数

**EN** Table 7 contains the hyper-parameters utilized for tuning the IAA instructions in LLaVA-v1.5-7B and mPLUG-OWL2 using 8 NVIDIA V100 GPU. The fine-tuning took a total of 16 hours for UNIAA-LLaVA and 22 hours for UNIAA-mPLUG-OWL2. We conduct a third stage of fine-tuning solely with converted aesthetic instruct tuning data to obtain the UNIAA-LLaVA for 2 epochs with a learning rate of 2e-5 and a batch size of 128.

**ZH** 表 7 给出了在 8 块 NVIDIA V100 GPU 上对 LLaVA-v1.5-7B 与 mPLUG-OWL2 做 IAA 指令微调所用的超参数。UNIAA-LLaVA 的微调共耗时 16 小时，UNIAA-mPLUG-OWL2 耗时 22 小时。我们仅用转换后的美学指令微调数据做第三阶段微调，训练 2 个 epoch，学习率 2e-5，批大小 128，得到 UNIAA-LLaVA。

**EN** Table 7. Hyper-parameters of IAA visual instruction tuning on UNIAA-LLaVA and UNIAA-mPLUG-OWL2, the same as original baselines.

**ZH** 表 7. UNIAA-LLaVA 与 UNIAA-mPLUG-OWL2 上 IAA 视觉指令微调的超参数，与原基线相同。

<!-- [原子块 · table] Hyper-parameter UNIAA-LLaVA UNIAA-mPLUG-OWL2 ViT init. CLIP-L/14-336 CLIP-L/14-448 LLM init. LLaMA2-7B image resolution 336 × 336 336\times 336 448 × 448 448\times 448 batch size 128 lr max 2e-5 lr sc -->

**EN** Appendix B Details on UNIAA-Bench Evaluation

**ZH** 附录 B UNIAA-Bench 评测细节

**EN** B.1. Examples of UNIAA-QA

**ZH** B.1. UNIAA-QA 示例

**EN** Here we present examples of UNIAA-QA questions with different aesthetic attributes.

**ZH** 这里给出不同美学属性下 UNIAA-QA 的问题示例。

**EN** Content and Theme Question: What is the object of interest in this photo? Candidates: A. Landscape B. Portrait C. Still life D. Animal

**ZH** 内容与主题 问题：这张照片的关注对象是什么？选项：A. 风景 B. 人像 C. 静物 D. 动物

**EN** Composition Question: What is the specific composition method used in this image? Candidates: A. Diagonal composition B. Center composition C. Triangle D. Symmetrical composition

**ZH** 构图 问题：这幅图像使用了何种具体构图方法？选项：A. 对角线构图 B. 中心构图 C. 三角形 D. 对称构图

**EN** Color Question: What is the color saturation of the picture? Candidates: A. Oversaturated B. Appropriate C. Undersaturated

**ZH** 色彩 问题：这幅图像的色彩饱和度如何？选项：A. 过饱和 B. 适中 C. 欠饱和

**EN** Light Question: What is the source of light in this image? Candidates: A. Natural light B. Artificial light

**ZH** 光线 问题：这幅图像的光源是什么？选项：A. 自然光 B. 人造光

**EN** Focus Question: What type of shot is this photo? Candidates: A. Long shot B. Medium shot C. Close-up

**ZH** 对焦 问题：这张照片属于何种景别？选项：A. 远景 B. 中景 C. 特写

**EN** Sentiment Question: Based on the color and content of this picture, what emotion does this photo evoke from you? Candidates: A. The character’s demeanor and the surrounding atmosphere in this image evoke a sense of longing and nostalgia. B. This picture resonates with a sense of introspection and contemplation due to the character’s actions and the environment, devoid of any traces of regret or sadness. C. The character’s actions and environment bring about a feeling of melancholy and regret. D. Despite the gloomy mood implied by the character’s actions and environment in the picture, a feeling of peacefulness and serenity suffuses throughout.

**ZH** 情感 问题：结合画面的色彩与内容，这张照片唤起了你怎样的情绪？选项：A. 画面中人物的神态与周围氛围唤起一种思念与怀旧之感。B. 由于人物的动作与环境，这幅图像引发一种内省与沉思的共鸣，不带任何遗憾或伤感的痕迹。C. 人物的动作与环境带来忧郁与遗憾之感。D. 尽管人物动作与环境暗示出阴郁的情绪，一种平和与宁静却贯穿整个画面。

**EN** B.2. Example of UNIAA-Describe

**ZH** B.2. UNIAA-Describe 示例

**EN** Question: Describe and evaluate the aesthetic attributes in detail. Give suggestions for improvement. Answer: The upward angle captures the grand structure and spatiality of the urban architecture. The composition is relatively neat and harmonious, with the top of the two buildings forming a diagonal composition, giving the image a certain sense of depth. However, there is a large empty space in the middle, making the image slightly unbalanced. The overall color is dark and low in saturation, lacking color coordination and contrast, making the image dull and uninteresting. The overall brightness is insufficient, lacking layers and details. To improve, the shooting position needs to be changed to reduce the empty sky in the middle of the frame, while emphasizing the diagonal composition to make the image more vivid and layered. The saturation of colors needs to be increased to make the image more vibrant and lively. Lastly, overall exposure needs to be increased to enhance the layers and image details. This is a below-average architectural photography photo.

**ZH** 问题：详细描述并评价该图像的美学属性，并给出改进建议。回答：仰拍视角捕捉到城市建筑的宏大结构与空间感。构图较为规整和谐，两栋建筑的顶部构成对角线构图，赋予画面一定的纵深。不过画面中部留白过大，使图像略显失衡。整体色调偏暗、饱和度偏低，缺少色彩协调与对比，画面显得平淡无趣；整体亮度不足，缺少层次与细节。改进方面，需要改变拍摄位置以减少画面中部的空白天空，同时强化对角线构图，使画面更生动、更有层次；需要提高色彩饱和度，让画面更鲜明活泼；最后需要整体提高曝光，以增强层次与细节。这是一张低于平均水平的建筑摄影作品。

**EN** B.3. Example of UNIAA Assessment Dataset

**ZH** B.3. UNIAA 评价数据集示例

**EN** There are 19,928 samples in the AVA test set. The number of samples in the test set of PARA, TAD66K, and Flickr-aes is 14,079, 3,000, and 4,737, respectively. The aesthetic assessment datasets image samples are shown in Figure 4. The maximum aesthetic score is 10 for AVA, TAD66K, and Flicker-aes, while it is 5 for PARA.

**ZH** AVA 测试集含 19,928 个样本；PARA、TAD66K 与 Flickr-aes 的测试集样本数分别为 14,079、3,000 与 4,737。美学评价数据集的图像样例如图 4 所示。AVA、TAD66K 与 Flicker-aes 的美学最高分为 10 分，PARA 为 5 分。

<!-- [原子块 · img]  -->

**EN** Figure 4. Image examples of four datasets in Aesthetic Assessment. Below the images are the corresponding aesthetic scores.

**ZH** 图 4. 美学评价中四个数据集的图像样例。图像下方为对应的美学分数。

**EN** B.4. Evaluation Details for Aesthetic Perception

**ZH** B.4. 美学感知评测细节

**EN** For the majority of the models, we use multiple-choice prompts as follows,

**ZH** 对多数模型，我们使用如下选择题提示，

**EN** How would you describe the color saturation of this picture? (Question) [IMAGE_TOKEN] (Image) Choose between one of the options as follows: A. Oversaturated (Correct) B. Undersaturated(Wrong) C. Appropriate(Wrong) #Answer:

**ZH** 你会如何描述这幅图像的色彩饱和度？（问题）[IMAGE_TOKEN]（图像）请从下列选项中选择其一：A. 过饱和（正确） B. 欠饱和（错误） C. 适中（错误） #答案：

**EN** B.5. Exceptions Perception Responses.

**ZH** B.5. 异常感知回答

**EN** For the InstructBLIP, although it has aesthetic perception capabilities, it usually provides a paragraph in response instead of options. To deal with this, we use chatGPT to determine its choice based on its response,

**ZH** 对 InstructBLIP，尽管它具备美学感知能力，其回答通常却是一段文字而非选项。为此，我们用 ChatGPT 根据其回答判定所选项，

**EN** As a language expert, please complete the following task. You are now an answer selection expert, and I will provide you with a question with several options, as well as a target sentence. Please return the alphabet of the option with the highest probability of matching this target sentence. Given questions with options and the target sequence [MLLM ANSWER]. Please output your responses in the form of a dictionary "maximum probability": "xxx", where xxx is A or B or C or …

**ZH** 作为语言专家，请完成以下任务。你现在是一名答案选择专家，我将为你提供一个带若干选项的问题以及一个目标语句。请返回与该目标语句匹配概率最高的选项字母。给定带选项的问题与目标序列 [MLLM ANSWER]。请以字典形式输出回答："maximum probability": "xxx"，其中 xxx 为 A 或 B 或 C 或……

**EN** For Qwen-VL, it may present options that do not exist or the response ’information is insufficient’, and we consider this to be a wrong answer,

**ZH** 对 Qwen-VL，它可能给出不存在的选项或回答「信息不足」，我们将这种情况判为错误，

**EN** How would you describe the color saturation of this picture? (Question) [IMAGE_TOKEN] (Image) Choose between one of the options as follows: A. Oversaturated (Correct) B. Undersaturated(Wrong) C. Appropriate(Wrong) #Answer: D. Not enough information

**ZH** 你会如何描述这幅图像的色彩饱和度？（问题）[IMAGE_TOKEN]（图像）请从下列选项中选择其一：A. 过饱和（正确） B. 欠饱和（错误） C. 适中（错误） #答案：D. 信息不足

**EN** Regarding GPT-4V, it occasionally encounters unknown errors or refuses to respond. We have made repeated attempts and still encountered 500+ such incidents. Therefore, we calculated its accuracy in answering questions.

**ZH** 对 GPT-4V，它偶尔会遇到未知错误或拒绝回答。我们反复尝试后，仍出现 500 余次此类情况，因此按其已回答的问题计算准确率。

**EN** B.6. Evaluation Details for Aesthetic Description

**ZH** B.6. 美学描述评测细节

**EN** Settings for GPT Evaluation:

**ZH** GPT 评测设置：

**EN** Due to the inherent variability of GPT, responses to identical prompts may not always be definitive. In order to alleviate the impact of these situations on our evaluation, we have adopted an average pooling strategy over 5 rounds. This involves presenting the same prompt as defined in the following templates five times, and averaging the results of GPT’s answers to obtain the final outcome. By using this method, we can effectively alleviate the unpredictability of GPT, resulting in a more accurate score.

**ZH** 由于 GPT 本身存在不确定性，相同提示下的回答未必稳定。为缓解这一情况对评测的影响，我们采用 5 轮平均池化策略：将下列模板所定义的同一提示呈现五次，对 GPT 的回答结果取平均作为最终结果。该方法能有效缓解 GPT 的不可预测性，得到更准确的分数。

**EN** Prompt Templates for GPT Evaluation:

**ZH** GPT 评测提示模板：

**EN** #System: As a language expert, please complete the following task.

**ZH** #System：作为语言专家，请完成以下任务。

**EN** Completeness. #User: Evaluate whether the description [MLLM_DESC] contains the dimensions of aesthetic, including composition, color, lighting, focus and suggestions, etc., in the reference description [GOLDEN_DESC]. Please rate score 2 for completely or almost completely including aesthetic dimensions, 0 for not including at all, and 1 for including part of the dimensions or similar description.. Please only provide the result in the following format: Score: Preciseness. # The precision metric punishes highly controversial aesthetic perspectives that output contrasts with the reference, e.g., positive for negative evaluations, good composition for messy composition, harmonious colors for abrupt colors, appropriate lighting for inappropriate lighting, high quality for low quality, colorful for monotonous. Evaluate whether [MLLM_DESC] precisely reflects reference [GOLDEN_DESC]. Please rate score 2 for a totally no controversial aesthetic description, 1 for less controversial aesthetic description than the matched description, and 0 for more controversial aesthetic description than the matched. Please only provide the result in the following format: Score: Relevance. #User: Evaluate whether the [MLLM_DESC] is relevant to the aesthetic evaluation, aesthetic attributes and aesthetic terminology. Aesthetic attributes include composition, color, lighting, focus, sentiments, and suggestions for improvement. Please rate score 2 for completely relevant, with no content unrelated to aesthetics; 1 for partly relevant, with a small amount of content unrelated to aesthetics; 0 for a large amount of content unrelated to aesthetics, even irrelevant. Please only provide the result in the following format: Score:

**ZH** 完整性。#User：评价描述 [MLLM_DESC] 是否包含参考描述 [GOLDEN_DESC] 中的美学维度，包括构图、色彩、光线、对焦以及建议等。若完全或几乎完全包含上述美学维度，请打 2 分；完全不包含打 0 分；包含部分维度或有相似描述打 1 分。请仅按以下格式给出结果：Score: 准确性。# 准确性指标用于惩罚那些输出与参考相左、争议较大的美学观点，例如把负面评价说成正面、把杂乱构图说成良好构图、把突兀配色说成和谐、把不当光线说成适当、把低质量说成高质量、把单调说成丰富多彩。请评价 [MLLM_DESC] 是否准确反映了参考描述 [GOLDEN_DESC]。若完全无争议的美学描述打 2 分；与匹配描述相比争议更少打 1 分；争议更多打 0 分。请仅按以下格式给出结果：Score: 相关性。#User：评价 [MLLM_DESC] 是否与美学评价、美学属性及美学术语相关。美学属性包括构图、色彩、光线、对焦、情感与改进建议。完全相关、无任何与美学无关的内容打 2 分；部分相关、含少量与美学无关的内容打 1 分；大量内容与美学无关甚至毫不相关打 0 分。请仅按以下格式给出结果：Score:

<!-- [原子块 · object]  -->

**EN** Figure 5. Supervised training model of MOS prediction. F1 represents the features of the last layer of the Vision Encoder, while F2 represents the features of the second-to-last layer.

**ZH** 图 5. MOS 预测的有监督训练模型。F1 表示视觉编码器最后一层的特征，F2 表示倒数第二层的特征。

**EN** Table 8. Results on AVA and Tad66K datasets. Blue and black numbers in bold represent the best and second best respectively. Metrics are PLCC/SRCC.

**ZH** 表 8. AVA 与 Tad66K 数据集上的结果。蓝色与黑色加粗数字分别表示最优与次优结果。指标为 PLCC/SRCC。

<!-- [原子块 · table] Method AVA TAD66K NIMA ( Talebi and Milanfar, 2018 ) 0.636/0.612 0.405/0.390 ALamp ( Ma et al., 2017 ) 0.671/0.666 0.422/0.411 HGCN ( She et al., 2021 ) 0.687/0.665 0.493/0.486 MaxViT ( Tu et al., 202 -->

**EN** Appendix C Supplemental experiment

**ZH** 附录 C 补充实验

**EN** C.1. Result on Supervised Scoring

**ZH** C.1. 有监督评分结果

**EN** To further enhance the scoring capability on specific datasets, we extract the vision encoder of UNIAA-LLaVA. We use the features from its last two layers, each of which is separately projected through a linear layer, then added together and passed through a score prediction head. The entire training model is shown in Figure 5. We test its performance on AVA and Tad66K, as shown in Table 8. We use a learning rate of 4e-6, a batch size of 32, a middle dimension of 4096 for the linear layers, and 40 training epochs. It is evident that even compared with the state-of-the-art EAT(He et al., 2023), our model still achieves superiority, further proving the capability of UNIAA-LLaVA on IAA.

**ZH** 为进一步提升在特定数据集上的评分能力，我们取出 UNIAA-LLaVA 的视觉编码器，取其最后两层的特征，各自经一个线性层投影后相加，再送入分数预测头。整体训练模型如图 5 所示。我们在 AVA 与 Tad66K 上测试其性能，结果见表 8。学习率取 4e-6，批大小 32，线性层中间维度 4096，训练 40 个 epoch。可以看到，即便与当前最优的 EAT（He et al., 2023）相比，我们的模型仍具优势，进一步证明了 UNIAA-LLaVA 在 IAA 上的能力。

**EN** C.2. Qualitative Analyse on Perception

**ZH** C.2. 感知定性分析

**EN** In Figure 6 , we show qualitative examples of MLLM responses on questions in the UNIAA-QA. Some of the MLLM still have inadequate spatial perception of the camera shot.

**ZH** 图 6 给出 MLLM 回答 UNIAA-QA 问题的定性示例。部分 MLLM 对拍摄景别的空间感知仍不充分。

<!-- [原子块 · img]  -->

**EN** Figure 6. Answer examples of MLLMs on ’Focus’ perception.

**ZH** 图 6. MLLM 在「对焦」感知上的回答示例。

**EN** C.3. Qualitative Analyse on Description

**ZH** C.3. 描述定性分析

**EN** As shown in Figure 7 and 8, we have presented examples of MLLM descriptions of high and low aesthetic quality. As shown in Figure 7, when MLLMs evaluate high aesthetic quality images, their descriptions are complete, accurate, and relevant, and their scores are high. UNIAA-LLaVA uses more aesthetic terms such as well-balanced composition, shallow depth of field, and color contrast, providing a professional description. GPT-4V has a clear structure and provides the longest answers among all models. When evaluating low aesthetic quality images, the model scores are lower, which also indicates an insight that accurately identifying the shortcomings of an image is more challenging than praising one. UNIAA-LLaVA can still pinpoint the shortcomings of the images accurately, such as cluttered composition and overexposure, while other models tend to praise the images instead. Using IDCP data could lead to better aesthetic discernment and expression ability.

**ZH** 如图 7 与图 8 所示，我们给出了 MLLM 对高、低美学质量图像的描述示例。由图 7 可见，评价高美学质量图像时，各模型的描述完整、准确且相关，得分也高。UNIAA-LLaVA 使用了更多美学术语，如构图均衡、浅景深、色彩对比，描述更为专业；GPT-4V 结构清晰，且在所有模型中回答最长。评价低美学质量图像时，模型得分普遍更低，这也揭示出一点：准确指出图像的不足比赞美图像更具挑战。UNIAA-LLaVA 仍能准确指出图像的问题所在，如构图杂乱、过曝，而其他模型则倾向于赞美图像。使用 IDCP 数据有助于获得更好的美学鉴别力与表达能力。

<!-- [原子块 · img]  -->

**EN** Figure 7. Description examples on the high-aesthetic image of MLLMs.

**ZH** 图 7. MLLM 对高美学质量图像的描述示例。

<!-- [原子块 · img]  -->

**EN** Figure 8. Description example on the low-aesthetic image of MLLMs.

**ZH** 图 8. MLLM 对低美学质量图像的描述示例。

**EN** Appendix D Limitations

**ZH** 附录 D 局限性

**EN** D.1. UNIAA-LLaVA Limitations

**ZH** D.1. UNIAA-LLaVA 的局限

**EN** Despite the enhanced aesthetic abilities, the performance on general-purpose tasks, especially those that require heavy reasoning abilities and language tasks, has decreased. Hence, if UNIAA-LLaVA is used for tasks other than aesthetic perception and understanding, it may generate undesired outcomes. Secondly, despite the improved accuracy, UNIAA-LLaVA still performs worse than the human. Therefore, they may not be able to replace humans directly. Thirdly, the Converted dataset from IDCP mostly comprises natural in-the-wild images. The performance can be further refined by adding more dataset sources, including natural image datasets, artistic image datasets, AI Generated Content datasets. Future work will focus on universal visual aesthetics, including aesthetic evaluation of videos.

**ZH** 尽管美学能力有所增强，模型在通用任务（尤其是那些需要大量推理与语言能力的任务）上的性能有所下降。因此，若将 UNIAA-LLaVA 用于美学感知与理解之外的任务，可能产生不理想的结果。其次，准确率虽有提升，UNIAA-LLaVA 仍不及人类，尚不能直接取代人类。第三，IDCP 转换得到的数据集以自然场景图像为主，可通过增加自然图像数据集、艺术图像数据集与人工智能生成内容（AIGC）数据集等更多来源进一步提升性能。未来工作将面向通用视觉美学，包括视频的美学评价。

**EN** D.2. UNIAA-Bench Limitations

**ZH** D.2. UNIAA-Bench 的局限

**EN** Although we have already aimed to maintain a balance in the number of dimensions for each aesthetic attribute and the balance between options, there inevitably exists some numerical deviation in the collection process. We will continue to refine the benchmark. Regarding the description task, we recognize that determining whether an MLLM answer aligns with the gold description is a subjective process that lacks an absolute standard. Human scores on the MLLM descriptions are also subject to individual differences. Despite employing the 5-round GPT-assisted evaluation protocol, which is currently the most trustworthy and reproducible approach, there may still be hallucinations (from GPT) that cannot be avoided. Moving forward, we will keep exploring better evaluation protocols for the low-level visual description task. We will continue to expand the scope of the aesthetic evaluation system in UNIAA-Bench, including but not limited to art paintings, AIGC, videos, movie clips, and other samples along with their corresponding aesthetic dimensions.

**ZH** 尽管我们已尽力保持各美学属性维度数量与选项之间的均衡，采集过程中仍不可避免地存在一定数量偏差，我们将持续改进该基准。就描述任务而言，我们认识到判断 MLLM 的回答是否与黄金描述一致本身是一个主观过程，缺少绝对标准，人类对 MLLM 描述的打分也会因人而异。尽管采用了目前最可信、可复现的 5 轮 GPT 辅助评测方案，仍可能存在无法避免的（GPT）幻觉。后续我们将继续探索更适合低层视觉描述任务的评测方案，并持续扩展 UNIAA-Bench 的美学评价体系，纳入但不限于艺术绘画、AIGC、视频、电影片段等样本及其对应的美学维度。
