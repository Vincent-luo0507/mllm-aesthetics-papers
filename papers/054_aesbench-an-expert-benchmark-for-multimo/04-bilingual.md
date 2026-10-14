# AesBench：面向多模态大语言模型图像美学感知的专家基准

> 原标题：AesBench: An Expert Benchmark for Multimodal Large Language Models on Image Aesthetics Perception
> 作者：Yipo Huang, Quan Yuan, Xiangfei Sheng, Zhichao Yang, Haoning Wu, Pengfei Chen, Yuzhe Yang, Leida Li, Weisi Lin · arXiv:2401.08276 · 2024-01-16

<!-- [原子块 · verbatim] AesBench: An Expert Benchmark for Multimodal Large Language Models on Image Aesthetics Perception -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] With collective endeavors, multimodal large language models (MLLMs) are undergoing a flourishing development. However, their performances on image aesthetics perception remain indeterminate, which is  -->

**EN** 1 Introduction

**ZH** 1 引言

**EN** Recent advancements in large language models (LLMs), such as ChatGPT OpenAI (2023) and LLaMA Touvron et al. (2023), have demonstrated remarkable achievements in comprehension, reasoning, and generation, garnering substantial interest from both academia and industry. Building on the success of LLMs in pure-textual tasks, multimodal large language models (MLLMs) have sparked a new wave in the field of visual-language processing, releasing numerous representative works, such as MiniGPT Zhu et al. (2023), Otter Li et al. (2023a) and LLaVA Liu et al. (2023b). Recently, these MLLMs have evolved into versatile assistants, facilitating human-machine interaction and collaboration Zhang et al. (2023b). Despite the broad capabilities of MLLMs, existing benchmarks mainly focus on general evaluation in several language or vision tasks, e.g. visual question answering Antol et al. (2015), image captioning Hossain et al. (2019), object segmentation Lai et al. (2023) and content understanding Cai et al. (2023). However, the effectiveness of MLLMs on the highly abstract image aesthetics perception task remains underexplored, which plays a significant role in image aesthetics assessment, aesthetic attribute analysis, image aesthetics cropping and image aesthetics captioning Huang et al. (2023). The potential of MLLMs in image aesthetics perception holds considerable promise for applications in smart photography, album management, photo recommendation and image enhancement, etc Lu et al. (2021); Huang et al. (2020). Therefore, it is highly desired to evaluate the abilities of existing MLLMs on aesthetic perception, which is expected to promote the further development of more advanced MLLMs with better aesthetic perception.

**ZH** 以 ChatGPT（OpenAI, 2023）与 LLaMA（Touvron et al., 2023）为代表的大语言模型（LLM）近来取得瞩目成就，在理解、推理与生成上表现卓越，引发了学术界与产业界的广泛关注。在 LLM 于纯文本任务取得成功的基础上，多模态大语言模型（MLLM）掀起了视觉—语言处理领域的新浪潮，涌现出 MiniGPT（Zhu et al., 2023）、Otter（Li et al., 2023a）与 LLaVA（Liu et al., 2023b）等一批代表性工作。近来，这些 MLLM 已演进为通用助手，服务于人机交互与协作（Zhang et al., 2023b）。尽管 MLLM 能力广泛，现有基准主要聚焦于若干语言或视觉任务上的通用评测，例如视觉问答（Antol et al., 2015）、图像描述（Hossain et al., 2019）、目标分割（Lai et al., 2023）与内容理解（Cai et al., 2023）。然而，MLLM 在高度抽象的图像美学感知任务上的有效性仍未被充分探索，而这一任务在图像美学评估、美学属性分析、图像美学裁剪与图像美学描述中举足轻重（Huang et al., 2023）。MLLM 在图像美学感知上的潜力，为智能摄影、相册管理、照片推荐与图像增强等应用带来了可观前景（Lu et al., 2021; Huang et al., 2020）。因此，评估现有 MLLM 的美学感知能力十分必要，这有望推动具备更强美学感知能力的先进 MLLM 进一步发展。

<!-- [原子块 · equation]  -->

**EN** Figure 1: Overview of the proposed AesBench. We first construct a high-quality Expert-labeled Aesthetics Perception Database (EAPD), based on which we further build the golden benchmark to evaluate four abilities of MLLMs on image aesthetics perception, including Aesthetic Perception (AesP), Aesthetic Empathy (AesE), Aesthetic Assessment (AesA) and Aesthetic Interpretation (AesI).

**ZH** 图 1：本文提出的 AesBench 总览。我们首先构建高质量的专家标注美学感知数据库（EAPD），并在此基础上进一步构建黄金基准，用以评测 MLLM 在图像美学感知上的四项能力，即美学感知（AesP）、美学共情（AesE）、美学评价（AesA）与美学阐释（AesI）。

**EN** In this work, we propose AesBench, a systematically designed golden benchmark to comprehensively evaluate the aesthetic perception abilities of MLLMs. Specifically, the proposed AesBench encompasses two major facets, i.e. high-quality data and integrative criteria. In terms of the former, we construct the Expert-labeled Aesthetics Perception Database (EAPD), which consists of 2,800 diverse-sourced images covering natural images (NIs), artistic images (AIs) and artificial intelligence-generated images (AGIs). Furthermore, each image of the EAPD is annotated by experts with professional backgrounds in aesthetics, which comprises researchers engaged in computational aesthetics, educators versed in aesthetic principles, and art students possessing sophisticated art skills. With these high-quality annotations, the benchmark results of MLLMs can be more reliable. For the latter, we develop a set of integrative criteria to systematically evaluate the aesthetic perception abilities of MLLMs. These criteria are designed from four dimensions, which are illustrated in Figure 1.

**ZH** 本文提出 AesBench——一个经过系统设计的黄金基准，用以全面评估 MLLM 的美学感知能力。具体地，AesBench 包含两个主要方面，即高质量数据与综合性准则。就前者而言，我们构建了专家标注美学感知数据库（EAPD），它由 2800 张多来源图像构成，覆盖自然图像（NI）、艺术图像（AI）与人工智能生成图像（AGI）。此外，EAPD 中的每张图像都由具备美学专业背景的专家标注，这些专家包括从事计算美学研究的科研人员、通晓美学原理的教育工作者，以及具备深厚艺术功底的艺术专业学生。借助这些高质量标注，MLLM 的基准评测结果更为可靠。就后者而言，我们提出了一套综合性准则，从四个维度系统评估 MLLM 的美学感知能力，如图 1 所示。

**EN** • Aesthetic Perception (AesP): As shown in Figure 1(a), this dimension focuses on the ability of MLLMs to recognize and understand aesthetic attributes.

**ZH** • 美学感知（AesP）：如图 1(a) 所示，该维度关注 MLLM 识别和理解美学属性的能力。

**EN** • Aesthetic Empathy (AesE): As shown in Figure 1(b), this dimension evaluates the ability of MLLMs to resonate with the emotional aspects conveyed through aesthetic expressions like humans.

**ZH** • 美学共情（AesE）：如图 1(b) 所示，该维度评估 MLLM 像人类一样与美学表达所传递的情绪层面产生共鸣的能力。

**EN** • Aesthetic Assessment (AesA): As shown in Figure 1(c), this dimension evaluates the ability of MLLMs to judge aesthetic grades and predict quality scores based on the language description.

**ZH** • 美学评价（AesA）：如图 1(c) 所示，该维度评估 MLLM 依据语言描述判断美学等级、预测质量分数的能力。

**EN** • Aesthetic Interpretation (AesI): As shown in Figure 1(d), this dimension involves the ability of MLLMs to interpret and analyze the reasons for aesthetic quality.

**ZH** • 美学阐释（AesI）：如图 1(d) 所示，该维度涉及 MLLM 阐释与分析美学质量成因的能力。

**EN** In summary, we present a comprehensive exploration of the abilities of MLLMs for the task of image aesthetics perception, which is structured around a novel four-dimensional evaluation framework, encompassing perception, empathy, assessment, and interpretation. These dimensions collectively form the foundation of AesBench, a golden benchmark of MLLMs on image aesthetics perception. The contributions of this work can be summarized as three-fold.

**ZH** 综上，我们围绕一个新颖的四维评测框架，对 MLLM 在图像美学感知任务上的能力做了全面探索，涵盖感知、共情、评价与阐释四个方面。这些维度共同构成了 AesBench——面向 MLLM 图像美学感知的黄金基准。本文的贡献可概括为三点。

**EN** ⟦SLOT_1⟧ We construct a high-quality Expert-labeled Aesthetics Perception Database (EAPD), encompassing 2,800 diverse-sourced images, along with 8,400 question-answer pairs and 2,800 aesthetic interpretations, all meticulously annotated by professional experts in aesthetics.

**ZH** ⟦SLOT_1⟧ 我们构建了高质量的专家标注美学感知数据库（EAPD），包含 2800 张多来源图像、8400 组问答对以及 2800 条美学阐释，全部由美学领域的专业专家精心标注。

**EN** ⟦SLOT_2⟧ We propose a set of integrative criteria to systematically evaluate the aesthetic perception abilities of MLLMs, which is based on the four-dimensional evaluation framework, including perception (AesP), empathy (AesE), assessment (AesA), and interpretation (AesI).

**ZH** ⟦SLOT_2⟧ 我们提出一套综合性准则，基于感知（AesP）、共情（AesE）、评价（AesA）与阐释（AesI）的四维评测框架，系统评估 MLLM 的美学感知能力。

**EN** ⟦SLOT_3⟧ We conduct extensive evaluations on 15 well-known MLLMs using AesBench, including two authoritative GPT-4V and Gemini Pro Vision, as well as thirteen state-of-the-art open-source counterparts. Comprehensive experimental results reveal that there is still a significant gap between MLLMs and humans in image aesthetics perception.

**ZH** ⟦SLOT_3⟧ 我们用 AesBench 对 15 个知名 MLLM 做了广泛评测，其中包括两个权威模型 GPT-4V 与 Gemini Pro Vision，以及 13 个最先进的开源同类模型。全面的实验结果表明，在图像美学感知上，MLLM 与人类之间仍存在显著差距。

**EN** We will make our code and database publicly available. We hope that these contributions can encourage the community to delve into more profound investigations of the yet untapped aesthetic potentials of MLLMs in future studies.

**ZH** 我们将公开代码与数据库。希望这些贡献能够激励学界在未来研究中更深入地挖掘 MLLM 尚未被触及的美学潜力。

**EN** 2 Constructing the EAPD

**ZH** 2 构建 EAPD

**EN** Image aesthetics perception is widely regarded as a highly abstract and complex task Sheng et al. (2023); Yang et al. (2022); Li et al. (2023c). To ensure the reliability of AesBench, it is essential to construct a high-quality Expert-labeled Aesthetics Perception Database (EAPD), meticulously annotated by professional experts in aesthetics. Specifically, the construction of EAPD consists of three stages, including data collection, expert selection and subjective experiments.

**ZH** 图像美学感知被广泛视为一项高度抽象而复杂的任务（Sheng et al., 2023; Yang et al., 2022; Li et al., 2023c）。为保证 AesBench 的可靠性，必须构建一个由美学专业专家精心标注的高质量专家标注美学感知数据库（EAPD）。具体地，EAPD 的构建包含三个阶段：数据采集、专家遴选与主观实验。

**EN** 2.1 Data Collection

**ZH** 2.1 数据采集

**EN** To cover diversified image contents, we collect multi-sourced images from diverse datasets, including three natural-image datasets (i.e. AADB Kong et al. (2016), PARA Yang et al. (2022) and TAD66K He et al. (2022)), three artistic image datasets (i.e. BAID Yi et al. (2023), CAD Li et al. (2018) and ArtEmis Achlioptas et al. (2021)), as well as three artificial intelligence-generated image datasets (i.e. DiffusionDB Wang et al. (2023), AGIQA-1K Li et al. (2023b) and AGIQA-3K Zhang et al. (2023a)). Then, we use a well-trained scene classification model Radford et al. (2021) to predict the scene labels automatically, and then double-check the labels manually to maintain annotation correctness. Next, we sample 2,493 images based on scene labels to maintain content diversity. Further, we add 152 high-aesthetic images from LITE Unsplash (2023) and Impressions Kruk et al. (2023) datasets, and 155 low-aesthetic images from SPAQ Fang et al. (2020) and KonIQ-10K Hosu et al. (2020) datasets, to balance aesthetic quality distribution. The information of sampled multi-sourced images is summarized in Table 1. Finally, the EAPD consists of 2,800 multi-sourced images, which are provided to professional aesthetic experts for high-quality annotation.

**ZH** 为覆盖多样化的图像内容，我们从多个数据集中采集多来源图像，包括三个自然图像数据集（AADB（Kong et al., 2016）、PARA（Yang et al., 2022）与 TAD66K（He et al., 2022））、三个艺术图像数据集（BAID（Yi et al., 2023）、CAD（Li et al., 2018）与 ArtEmis（Achlioptas et al., 2021）），以及三个人工智能生成图像数据集（DiffusionDB（Wang et al., 2023）、AGIQA-1K（Li et al., 2023b）与 AGIQA-3K（Zhang et al., 2023a））。随后，我们用一个训练良好的场景分类模型（Radford et al., 2021）自动预测场景标签，再人工复核标签以保证标注正确。接着，我们依据场景标签采样 2493 张图像以维持内容多样性。此外，我们从 LITE Unsplash（2023）与 Impressions（Kruk et al., 2023）数据集中加入 152 张高美学质量图像，从 SPAQ（Fang et al., 2020）与 KonIQ-10K（Hosu et al., 2020）数据集中加入 155 张低美学质量图像，以平衡美学质量分布。所采集的多来源图像信息汇总于表 1。最终，EAPD 由 2800 张多来源图像构成，交由专业美学专家进行高质量标注。

**EN** 2.2 Expert Selection

**ZH** 2.2 专家遴选

**EN** Table 1: Overview of the image source datasets.

**ZH** 表 1：图像来源数据集总览。

<!-- [原子块 · table] Type Dataset Sampled Size NIs AADB Kong et al. (2016) 96 PARA Yang et al. (2022) 539 TAD66K He et al. (2022) 304 LITE Unsplash (2023) 146 Impressions Kruk et al. (2023) 6 SPAQ Fang et al. (2020) 50 Ko -->

**EN** Unlike most existing aesthetics-related datasets, all participants in this work are expected to be experts with rich aesthetic experience. Specifically, to guarantee quality and diversity of annotation, we recruit subjects by considering six perspectives, including health state, age distribution, gender balance, educational background, working experience, and personality traits. First, we ensure that each participant is in good health, strictly adhering to ethical guidelines that prohibit any form of coerced participation. Second, we require that all participants should have professional backgrounds in aesthetics, which include researchers engaged in computational aesthetics, educators versed in aesthetic principles, and art students possessing sophisticated art skills. Third, we pay great attention to ensure diversity among all participants, particularly in age distribution, gender balance, good educational background, and personality traits (based on Big-Five personality traitsYang et al. (2022)). Taking into account the above factors comprehensively, we recruited 32 professional aesthetic experts who met the aforementioned criteria to participate in the subjective experiment, ensuring the validity and reliability of annotations. The detailed portrait distribution of participants is provided in Supplementary Section 1.

**ZH** 与多数既有的美学相关数据集不同，本文要求所有参与者都是具备丰富美学经验的专家。具体地，为保证标注的质量与多样性，我们从六个方面招募被试：健康状况、年龄分布、性别均衡、教育背景、从业经历与人格特质。首先，我们确保每位参与者身体健康，严格遵守禁止任何形式强制参与的伦理准则。其次，我们要求所有参与者具备美学专业背景，包括从事计算美学研究的科研人员、通晓美学原理的教育工作者，以及具备深厚艺术功底的艺术专业学生。第三，我们高度重视参与者之间的多样性，尤其是年龄分布、性别均衡、良好教育背景与人格特质（基于大五人格特质（Yang et al., 2022））。综合上述因素，我们招募了 32 位符合上述标准的专业美学专家参与主观实验，以保证标注的有效性与可靠性。参与者的详细画像分布见补充材料第 1 节。

**EN** 2.3 Subjective Experiments

**ZH** 2.3 主观实验

**EN** In this work, we conduct subjective experiments to collect expert annotations, in strict compliance with the generic psychological experiment protocol Sheikh et al. (2006). First, the images of the entire database are segmented into 56 distinct sessions, and each session contains 50 unlabeled images. Then, we develop a local-deployed annotation tool (.exe format) and assign a personal user ID to each participant. Furthermore, a well-devised annotation quality control strategy ensures that all qualified annotations are automatically saved based on text richness and diversity, and each image is annotated by at least one expert (details are provided in Supplementary Section 1). To mitigate the risk of test fatigue, consecutive annotations on more than 30 images will trigger a reminder of the break. Similar to the existing MLLM benchmarks Chen et al. (2023c); Cai et al. (2023), we collect a total of 8,400 question-answer pairs and 2,800 aesthetic interpretations. Specifically, each image is equipped with three expert-asked questions focusing on AesP, AesE and AesA respectively, and one expert-answered aesthetic interpretation for AesI. These golden annotations serve as ground truth for evaluating the abilities of MLLMs. Therefore, the EAPD can be divided into four subsets based on the benchmark objectives, as illustrated in Figure 2, i.e. AesPQA subset (evaluating AesP), AesEQA subset (evaluating AesE), AesAQA subset (evaluating AesA) and AesInter subset (evaluating AesI). These subsets are described in detail below.

**ZH** 本文严格按照通用心理学实验规程（Sheikh et al., 2006）开展主观实验以采集专家标注。首先，把整个数据库的图像切分为 56 个独立场次，每场包含 50 张未标注图像。随后，我们开发了一个本地部署的标注工具（.exe 格式），并为每位参与者分配了个人用户 ID。此外，一套精心设计的标注质量控制策略确保：所有合格标注会基于文本丰富度与多样性被自动保存，且每张图像至少由一位专家标注（细节见补充材料第 1 节）。为降低测试疲劳的风险，连续标注超过 30 张图像会触发休息提醒。与现有的 MLLM 基准类似（Chen et al., 2023c; Cai et al., 2023），我们共采集了 8400 组问答对与 2800 条美学阐释。具体地，每张图像配有分别聚焦 AesP、AesE 与 AesA 的三个专家提问，以及一条面向 AesI 的专家作答的美学阐释。这些黄金标注作为评测 MLLM 能力的真值。由此，EAPD 可按基准目标划分为四个子集，如图 2 所示，即 AesPQA 子集（评测 AesP）、AesEQA 子集（评测 AesE）、AesAQA 子集（评测 AesA）与 AesInter 子集（评测 AesI）。下面详细介绍这些子集。

<!-- [原子块 · equation]  -->

**EN** Figure 2: Data samples from the constructed EAPD, which includes four subsets, i.e. AesPQA subset (benchmarking AesP), AesEQA subset (benchmarking AesE), AesAQA subset (benchmarking AesA) and AesInter subset (benchmarking AesI).

**ZH** 图 2：所构建 EAPD 的数据样例，包含四个子集，即 AesPQA 子集（评测 AesP）、AesEQA 子集（评测 AesE）、AesAQA 子集（评测 AesA）与 AesInter 子集（评测 AesI）。

**EN** 3 Developing the Criteria

**ZH** 3 制定评测准则

**EN** Based on the expert-labeled aesthetics perception database, we propose a set of integrative criteria to measure the aesthetic perception abilities of MLLMs from four perspectives, including Perception (AesP), Empathy (AesE), Assessment (AesA) and Interpretation (AesI).

**ZH** 在专家标注美学感知数据库的基础上，我们提出一套综合性准则，从感知（AesP）、共情（AesE）、评价（AesA）与阐释（AesI）四个视角衡量 MLLM 的美学感知能力。

**EN** 3.1 Benchmark on Aesthetic Perception

**ZH** 3.1 美学感知基准

**EN** We first leverage the AesPQA subset to evaluate the aesthetic perception (AesP) ability of MLLMs, aiming to investigate whether they can accurately respond to simple natural language queries related to aesthetic attributes. The AesPQA subset contains 2,800 multi-sourced images (as listed in Table 1), and each image is equipped with one perception-related question, one correct option, and 1-3 false options (as illustrated in Figure 2). Specifically, the questions in AesPQA cover four perceptual dimensions and four question types. These diverse questions will be fed into MLLMs for evaluation, and then their outputs are further calculated as the rate of correct answers.

**ZH** 我们首先利用 AesPQA 子集评估 MLLM 的美学感知（AesP）能力，旨在考察它们能否准确回答与美学属性相关的简单自然语言提问。AesPQA 子集包含 2800 张多来源图像（见表 1），每张图像配有一个感知相关问题、一个正确选项与 1–3 个错误选项（如图 2 所示）。具体地，AesPQA 中的问题覆盖四个感知维度与四种问题类型。这些多样化的问题将被输入 MLLM 进行评测，其输出进而被统计为正确率。

**EN** Perceptual Dimensions: Inspired by recent research on aesthetic perception Yang et al. (2022) and human perception process on image aesthetics Li et al. (2023c), the questions of the AesPQA subset consist of four dimensions as follows:

**ZH** 感知维度：受近期美学感知研究（Yang et al., 2022）以及人类图像美学感知过程（Li et al., 2023c）的启发，AesPQA 子集的问题由以下四个维度构成：

**EN** • Technical quality focuses on fundamental aspects such as sharpness, contrast, exposure, noise, etc, which are pivotal in influencing the aesthetic appeal of an image, forming the cornerstone of overall visual attractiveness.

**ZH** • 技术质量关注锐度、对比度、曝光、噪声等基础方面，它们对图像的美感影响重大，构成了整体视觉吸引力的基石。

**EN** • Color and light are crucial for both the overall aesthetic expression of an image and the local emphasis on objects, which involve a detailed evaluation of color contrast, color harmony, color richness, and use of light.

**ZH** • 色彩与光影对图像的整体美学表达与对物体的局部强调都至关重要，涉及色彩对比、色彩和谐、色彩丰富度以及用光方式的细致评价。

**EN** • Composition is not merely the visual location of the target but a fundamental aspect of conveying meaning and aesthetic value in images, e.g. symmetry, rule of thirds, and leading lines, playing a crucial role in structuring the visual narrative and enhancing the aesthetic appeal.

**ZH** • 构图不仅是主体的视觉位置，更是图像传达意义与美学价值的基本方面，例如对称、三分法与引导线，它在组织视觉叙事、增强美感上起着关键作用。

**EN** • Content focuses on the thematic essence, personal character, and the manner of story presentation in an image, which is crucial for evaluating elements such as originality, creativity, attraction, and enjoyment.

**ZH** • 内容关注图像的主题内核、人物个性与故事呈现方式，这对原创性、创意、吸引力与愉悦感等要素的评价至关重要。

**EN** Question Types: In the AesPQA subset, inspired by the existing MLLM benchmarks Chen et al. (2023c); Cai et al. (2023), four commonly used question types are utilized to simulate human query formats when interacting with MLLMs. 1) Yes-or-No questions are binary queries requiring a simple positive or negative response (e.g., Does the image maintain a balance between warm and cold colors?). 2) What questions are used to examine more comprehensive aesthetic perception. For example, What aspect of the image is primarily used to enhance the aesthetic perception? 3) How questions are employed to evaluate more details about the production of aesthetic feeling (e.g., How is the aesthetic perception felt in this image?). 4) Why questions aim to understand the rationale behind aesthetic perception, including the reasons for aesthetic judgment or the underlying principles of visual appeal (e.g., Why might the aesthetic perception of the photograph be considered less appealing?). The diversified question types effectively simulate a wide range of human-like inquiries, facilitating the practicability of AesBench in evaluating the aesthetic perception abilities of MLLMs.

**ZH** 问题类型：在 AesPQA 子集中，受现有 MLLM 基准启发（Chen et al., 2023c; Cai et al., 2023），我们采用四种常用问题类型来模拟人类与 MLLM 交互时的提问形式。1）是非题是需要简单肯定或否定回答的二元提问（例如：这幅图像是否保持了冷暖色彩之间的平衡？）。2）What 问句用于考察更全面的美学感知，例如：图像主要借助哪个方面来增强美学感受？3）How 问句用于评估美感产生的更多细节（例如：这幅图像的美感是如何被感受到的？）。4）Why 问句旨在理解美学感知背后的缘由，包括美学判断的理由或视觉吸引力的深层原理（例如：为什么这幅照片的美学感受可能被认为欠佳？）。多样化的问题类型有效模拟了广泛的人类式提问，提升了 AesBench 在评测 MLLM 美学感知能力上的实用性。

**EN** Evaluation Process: Based on the AesPQA subset, we feed the perception-related questions to various MLLMs to measure their abilities on aesthetic perception. The input prompt to query MLLMs is exemplified as #User: Does the image maintain a balance between warm and cold colors? [Image_token] Choose one from the following options: A) Yes B) No. You should output the correct option without explanation. Despite the explicit prompt for MLLMs to merely provide the correct option, as observed by recent works Wu et al. (2024); Cai et al. (2023); Wu et al. (2023b) and further validated by us, some MLLMs are unable to consistently generate outputs that align with instructed format. For the above Yes-or-No question with the correct option: B) No, different MLLMs may output “B) No”, “B”, “No”, or “The image can not maintain a balance between warm and cold colors”, which are all correct in fact. These irregular formats present significant challenges for the accurate assessment by existing traditional language metrics (such as BLEU-4, CIDEr). Inspired by Liu et al. (2023b), we propose, validate, and implement a GPT-assisted evaluation strategy that integrates decision rules with GPT. Specifically, outputs of MLLMs that align strictly with the candidate options are regarded as ‘explicit responses’, determined through direct comparison with the correct option. Otherwise, the outputs are regarded as ‘ambiguous responses’. For these, the questions, correct answers and ambiguous responses of MLLMs are submitted to GPT for evaluation (details are provided in Supplementary Section 2).

**ZH** 评测流程：基于 AesPQA 子集，我们把感知相关问题输入各个 MLLM，以衡量它们的美学感知能力。查询 MLLM 的输入提示示例为：#User: 这幅图像是否保持了冷暖色彩之间的平衡？[Image_token] 从以下选项中选择其一：A) 是 B) 否。你只需输出正确选项，不要解释。尽管已明确提示 MLLM 仅给出正确选项，但正如近期工作（Wu et al., 2024; Cai et al., 2023; Wu et al., 2023b）所观察到、并被我们进一步验证的那样，部分 MLLM 无法始终按指令格式生成输出。对上述正确选项为 B) 否 的是非题，不同 MLLM 可能输出“B) 否”“B”“否”或“这幅图像未能保持冷暖色彩之间的平衡”，事实上这些都算正确。这些不规范的格式给传统语言指标（如 BLEU-4、CIDEr）的准确评测带来很大挑战。受 Liu et al.（2023b）启发，我们提出、验证并实现了一种把判定规则与 GPT 相结合的 GPT 辅助评测策略。具体地，与候选选项严格一致的 MLLM 输出被视为“显式回答”，通过与正确选项直接比较来判定；否则输出被视为“模糊回答”。对于模糊回答，我们把问题、正确答案与 MLLM 的模糊回答一并提交给 GPT 评判（细节见补充材料第 2 节）。

**EN** 3.2 Benchmark on Aesthetic Empathy

**ZH** 3.2 美学共情基准

**EN** Aesthetic empathy, a critical aspect of image aesthetics perception, embodies a multi-dimensional and comprehensive process, involving emotional response, interest, recognition of uniqueness, and understanding of the vibe in aesthetic experiences. Therefore, based on the proposed AesEQA subset, we further study the abilities of MLLMs to understand the aesthetic empathy contained in images as humans. Like AesPQA, the AesEQA subset comprises 2,800 images, each accompanied by one empathy-related question, one correct option, and 1-3 false options, as illustrated in Figure 2. These questions are fed into MLLMs for evaluation, and the efficacy of these models is quantified based on the accuracy rate of their responses. Specifically, based on the principles of sentiment analysis research Feng et al. (2023), AesEQA collects empathy-related questions from four dimensions as follows:

**ZH** 美学共情是图像美学感知的关键一环，体现为一个多维、综合的过程，涉及审美体验中的情绪反应、兴趣、对独特性的识别以及对氛围的理解。因此，基于所提出的 AesEQA 子集，我们进一步研究 MLLM 像人类一样理解图像所蕴含的美学共情的能力。与 AesPQA 类似，AesEQA 子集包含 2800 张图像，每张配有一个共情相关问题、一个正确选项与 1–3 个错误选项，如图 2 所示。这些问题被输入 MLLM 进行评测，模型效果以其回答的准确率来量化。具体地，依据情感分析研究的原则（Feng et al., 2023），AesEQA 从以下四个维度采集共情相关问题：

**EN** • Emotion refers to the complex emotional reactions that images evoke. It includes a range of emotional responses, such as joy, sadness, fear, and surprise, which are triggered by the image.

**ZH** • 情绪指图像所唤起的复杂情绪反应，包括由图像引发的喜悦、悲伤、恐惧、惊讶等一系列情感回应。

**EN** • Interest is defined as the degree of curiosity and attraction towards images, such as visual allure, emotional resonance, novelty, facts and culture.

**ZH** • 兴趣定义为对图像的好奇与吸引程度，例如视觉魅力、情感共鸣、新奇感、事实性与文化内涵。

**EN** • Uniqueness evaluates the originality and distinctiveness of photographic images or artworks, e.g. novel concepts, unique stylistic approaches and innovative techniques.

**ZH** • 独特性评价摄影图像或艺术作品的原创性与与众不同之处，例如新颖的构思、独特的风格手法与创新的技法。

**EN** • Vibe refers to the overarching emotional ambiance or thematic representation conveyed by images, which articulates a holistic sensation, characterized by harmony, liveliness, mystery, elegance, and others.

**ZH** • 氛围指图像传达的整体情绪基调或主题表征，它表达一种整体感受，其特征可以是和谐、生动、神秘、优雅等等。

**EN** Each dimension provides a unique perspective for evaluating the empathy-related abilities of current MLLMs. Additionally, the AesEQA subset also integrates a quartet of question types: Yes-or-No, What, How and Why. These four types of questions are leveraged to examine the ability to deal with common cases of human-machine interaction and collaboration, which play a pivotal role in the thorough evaluation of MLLMs. Finally, we also employ the GPT-assisted evaluation strategy to calculate the accuracy rate of the responses generated by MLLMs.

**ZH** 每个维度都为评估当前 MLLM 的共情相关能力提供了独特视角。此外，AesEQA 子集同样整合了是非题、What、How 与 Why 四种问题类型。这四类问题被用于考察模型处理人机交互与协作中常见情形的能力，在对 MLLM 的完备评测中起着关键作用。最后，我们也采用 GPT 辅助评测策略来计算 MLLM 所生成回答的准确率。

**EN** Table 2: Evaluation results on the Aesthetic Perception ability. We highlight the best results of each sub-category in bold and the second-best results in underlining.

**ZH** 表 2：美学感知能力的评测结果。各子类别的最优结果加粗，次优结果加下划线。

<!-- [原子块 · table] MLLM Perceptual Dimensions Image Sources Question Types Overall Rank Tec. Qua. Col. Lig. Comp. Content NIs AIs AGIs Yes-No What How Why Random guess 34.82% 31.02% 30.53% 37.20% 31.59% 32.50% 31.19% 50 -->

**EN** Table 3: Evaluation results on the Aesthetic Empathy ability.

**ZH** 表 3：美学共情能力的评测结果。

<!-- [原子块 · table] MLLM Empathy Dimensions Image Sources Question Types Overall Rank Emotion Interest Uniqueness Vibe NIs AIs AGIs Yes-No What How Why Random guess 40.28% 37.80% 36.25% 42.12% 33.10% 30.62% 30.67% 50.00% -->

**EN** 3.3 Benchmark on Aesthetic Assessment

**ZH** 3.3 美学评价基准

**EN** In the third task of AesBench, the objective is to evaluate the abilities of MLLMs to quantify the aesthetic quality of images. Specifically, in the AesAQA subset, we collect three aesthetic ratings for 2,800 images from aesthetic experts, including high, medium, and low. Then, we feed the quality-related questions to various MLLMs to measure the simple task of aesthetic three-grade classification, as illustrated in Figure 2. The input prompt is exemplified as: #User: How is the aesthetic quality of this image? [Image_token] Choose one from the following options: A) High B) Medium C) Low. You should output the correct option without explanation. Finally, we leverage the GPT-assisted evaluation strategy to calculate the accuracy rate of the responses generated by MLLMs.

**ZH** AesBench 的第三项任务旨在评估 MLLM 量化图像美学质量的能力。具体地，在 AesAQA 子集中，我们从美学专家处采集了 2800 张图像的三种美学评级，包括高、中、低。随后，我们把质量相关问题输入各个 MLLM，以衡量美学三档分类这一简单任务，如图 2 所示。输入提示示例为：#User: 这幅图像的美学质量如何？[Image_token] 从以下选项中选择其一：A) 高 B) 中 C) 低。你只需输出正确选项，不要解释。最后，我们借助 GPT 辅助评测策略计算 MLLM 所生成回答的准确率。

**EN** Although the numerical prediction of MLLMs is not the research focus in the community, we still try to explore the abilities of MLLMs to generate fine-grained aesthetic scores. Generally, the outputs of MLLMs are usually verbal text rather than a definite numerical value, and the existing work indicates that the direct output of quality score does not apply to existing MLLMs Wu et al. (2024). Therefore, how to collect quantifiable scores from MLLMs remains challenging. Inspired by recent studies on text-based aesthetic assessment Sheng et al. (2023); Zhong et al. (2023), we introduce a text-to-score approach to convert aesthetic quality descriptions of MLLMs into aesthetic quality scores via a BERT-based regressor Devlin et al. (2019). Technical details and results are provided in Supplementary Sections 2 and 3.

**ZH** 尽管 MLLM 的数值预测并非学界的研究重点，我们仍尝试探索 MLLM 生成细粒度美学分数的能力。一般而言，MLLM 的输出通常是口头文本而非确定的数值，既有工作也表明直接输出质量分数并不适用于现有 MLLM（Wu et al., 2024）。因此，如何从 MLLM 收集可量化的分数仍具挑战。受近期基于文本的美学评估研究启发（Sheng et al., 2023; Zhong et al., 2023），我们引入一种文本转分数方法，通过基于 BERT 的回归器（Devlin et al., 2019）把 MLLM 的美学质量描述转换为美学质量分数。技术细节与结果见补充材料第 2 节与第 3 节。

**EN** 3.4 Benchmark on Aesthetic Interpretation

**ZH** 3.4 美学阐释基准

**EN** Language interpretation ability is an important feature of MLLMs Liu et al. (2023b). In the last task of AesBench, we examine whether current MLLMs can accurately interpret the reasons for the aesthetic quality. In the AesInter subset, we collect expert interpretations for each of the 2,800 images, as shown in Figure 2. Then, we feed the interpretation-related questions to MLLMs for evaluation. The input prompt is exemplified as: #User: This is an image with [high] aesthetics, please explain the reasons that are related to the aesthetic quality, where [high] is replaced by the actual aesthetic quality grades. The purpose of this is, in the case of known true aesthetic quality, to explore whether current MLLMs can give an aesthetic interpretation that is consistent with aesthetic experts. To evaluate this, we refer to recent works Zheng et al. (2023); Wu et al. (2024), which have validated the efficacy of using a single-modal GPT as a reliable evaluation tool for pure language tasks. Leveraging this paradigm, this task is converted into a text-only evaluation by matching the MLLM outputs with the expert interpretations under three dimensions: Relevance, Precision, and Completeness, ensuring a comprehensive benchmark on the aesthetic interpretation. The configurations of the GPT-based evaluation are delineated in Supplementary Section 2.

**ZH** 语言阐释能力是 MLLM 的一项重要特征（Liu et al., 2023b）。在 AesBench 的最后一项任务中，我们考察现有 MLLM 能否准确阐释美学质量的成因。在 AesInter 子集中，我们为 2800 张图像中的每一张采集了专家阐释，如图 2 所示。随后，我们把阐释相关问题输入 MLLM 进行评测。输入提示示例为：#User: 这是一幅具有[高]美感的图像，请解释与美学质量相关的原因，其中[高]会被替换为实际的美学质量等级。这样做的目的是：在已知真实美学质量的前提下，探索现有 MLLM 能否给出与美学专家一致的阐释。为进行评测，我们参考近期工作（Zheng et al., 2023; Wu et al., 2024）——它们验证了用单模态 GPT 作为纯语言任务可靠评测工具的有效性。沿用这一范式，本任务被转化为纯文本评测：在相关性、精确性与完整性三个维度上把 MLLM 的输出与专家阐释相匹配，从而保证对美学阐释的全面评测。基于 GPT 的评测配置详见补充材料第 2 节。

**EN** 4 Experiments on AesBench

**ZH** 4 在 AesBench 上的实验

**EN** 4.1 Experimental Setting

**ZH** 4.1 实验设置

**EN** In this section, we conduct extensive experiments with 15 different MLLMs to evaluate their abilities on image aesthetics perception, including the popular GPT-4V Yang et al. (2023) and Gemini Pro Vision Google (2023), as well as 13 state-of-the-art variants with open sources, i.e. LLaVA (LLaMA-2-Chat-7B) Liu et al. (2023b), LLaVA-1.5 (Vicuna-v1.5-7B) Liu et al. (2023a), ShareGPT4V (Vicuna-v1.5-7B) Chen et al. (2023b), Q-Instruct (Vicuna-v1.5-7B) Wu et al. (2023a), mPLUG-Owl2 (LLaMA-2-7B) Ye et al. (2023), InstructBLIP (Vicuna-7B) Dai et al. (2023), MiniGPT-4 (Vicuna-7B) Zhu et al. (2023), MiniGPT-v2 (LLaMA-2-Chat-7B) Chen et al. (2023a), IDEFICS-Instruct (LLaMA-7B) Huggingface (2023), GLM (ChatGLM-6B) Du et al. (2022) Otter (MPT-7B) Li et al. (2023a), TinyGPT-V (Phi-2) Yuan et al. (2023) and Qwen-VL (QWen-7B) Bai et al. (2023). To ensure integrity and fairness, these MLLMs are evaluated using the original model weights as released by the authors without any dataset-specific tuning. It is worth noting that GPT-4V and Gemini Pro Vision have not been made available in the public domain as open-source entities. To facilitate experimental analysis, their capabilities are gauged through responses obtained via APIs. More experimental details and analyses are provided in Supplementary Section 3.

**ZH** 本节我们用 15 个不同的 MLLM 开展大量实验，以评估它们的图像美学感知能力，其中包括流行的 GPT-4V（Yang et al., 2023）与 Gemini Pro Vision（Google, 2023），以及 13 个最先进的开源变体，即 LLaVA（LLaMA-2-Chat-7B）（Liu et al., 2023b）、LLaVA-1.5（Vicuna-v1.5-7B）（Liu et al., 2023a）、ShareGPT4V（Vicuna-v1.5-7B）（Chen et al., 2023b）、Q-Instruct（Vicuna-v1.5-7B）（Wu et al., 2023a）、mPLUG-Owl2（LLaMA-2-7B）（Ye et al., 2023）、InstructBLIP（Vicuna-7B）（Dai et al., 2023）、MiniGPT-4（Vicuna-7B）（Zhu et al., 2023）、MiniGPT-v2（LLaMA-2-Chat-7B）（Chen et al., 2023a）、IDEFICS-Instruct（LLaMA-7B）（Huggingface, 2023）、GLM（ChatGLM-6B）（Du et al., 2022）、Otter（MPT-7B）（Li et al., 2023a）、TinyGPT-V（Phi-2）（Yuan et al., 2023）与 Qwen-VL（QWen-7B）（Bai et al., 2023）。为保证完整性与公平性，这些 MLLM 均使用作者发布的原始模型权重进行评测，未针对任何数据集做调优。值得注意的是，GPT-4V 与 Gemini Pro Vision 并未以开源形式公开。为便于实验分析，我们通过 API 获取其回答来衡量其能力。更多实验细节与分析见补充材料第 3 节。

**EN** 4.2 Evaluation on Aesthetic Perception

**ZH** 4.2 美学感知评测

**EN** To comprehensively evaluate the aesthetic perception abilities of current MLLMs, we measure the accuracy of responses produced by these MLLMs across various perceptual dimensions, image sources, and question types using the AesPQA subset. The results are listed in Table 2. Notably, Q-Instruct achieves superior overall performance in aesthetic perception. For different perceptual dimensions, GPT-4V performs best in terms of Technical Quality and Color and Light, while Q-Instruct outperforms other MLLMs in terms of Composition and Content. We also notice that most MLLMs perform best on natural images, followed by artistic images, and worst on artificial intelligence-generated images, which potentially correlates with the data composition in their training sets. In conclusion, AesBench can effectively discriminate among the aesthetic perception capabilities of MLLMs.

**ZH** 为全面评估现有 MLLM 的美学感知能力，我们利用 AesPQA 子集衡量这些 MLLM 在各个感知维度、图像来源与问题类型上回答的准确率，结果列于表 2。值得注意的是，Q-Instruct 在美学感知上取得了最优的总体表现。就不同感知维度而言，GPT-4V 在技术质量与色彩光影上表现最好，而 Q-Instruct 在构图与内容上优于其他 MLLM。我们还注意到，多数 MLLM 在自然图像上表现最好，其次是艺术图像，在人工智能生成图像上最差，这可能与其训练集的数据构成有关。综上，AesBench 能有效区分各 MLLM 的美学感知能力。

**EN** 4.3 Evaluation on Aesthetic Empathy

**ZH** 4.3 美学共情评测

**EN** For evaluating the aesthetic empathy capabilities of current MLLMs, we test their accuracy in generating responses across various empathy dimensions, image sources, and question types, utilizing the AesEQA subset. Table 3 summarizes the experimental results. The results indicate that among the evaluated MLLMs, Q-Instruct exhibits the highest overall performance in aesthetic empathy, while Gemini Pro Vision achieves the second-best overall performance. For different empathy dimensions, Q-Instruct outperforms other MLLMs in terms of Emotion and Uniqueness; Gemini Pro Vision reaches the best accuracy on Interest, and GPT-4V performs best on Vibe. TinyGPT performs worst overall, even lower than the accuracy of random guesses. In summary, we comprehensively evaluate the strengths and weaknesses of current MLLMs in aesthetic empathy.

**ZH** 为评估现有 MLLM 的美学共情能力，我们利用 AesEQA 子集测试它们在各个共情维度、图像来源与问题类型上生成回答的准确率。表 3 汇总了实验结果。结果表明，在所评测的 MLLM 中，Q-Instruct 在美学共情上总体表现最高，Gemini Pro Vision 总体位居第二。就不同共情维度而言，Q-Instruct 在情绪与独特性上优于其他 MLLM；Gemini Pro Vision 在兴趣上准确率最高；GPT-4V 在氛围上表现最好。TinyGPT 总体最差，甚至低于随机猜测的准确率。综上，我们全面评估了现有 MLLM 在美学共情上的长处与短板。

**EN** Table 4: Evaluation results on the Aesthetic Assessment ability.

**ZH** 表 4：美学评价能力的评测结果。

<!-- [原子块 · table] MLLM NIs AIs AGIs Overall Rank Random guess 33.33% 33.33% 33.33% 33.33% / Q-Instruct 62.20% 49.75% 40.69% 52.86% 1 GPT-4V 59.98% 46.92% 40.59% 50.86% 2 mPLUG-Owl2 57.78% 49.50% 40.83% 50.57% 3 Gemini  -->

**EN** Table 5: Evaluation results on the Aesthetic Interpretation ability.

**ZH** 表 5：美学阐释能力的评测结果。

<!-- [原子块 · table] MLLM Rele. Prec. Comp. Overall Rank GPT-4V 1.385 1.151 1.366 1.301 1 ShareGPT4V 1.440 1.117 1.331 1.296 2 Gemini Pro Vision 1.416 1.087 1.164 1.222 3 Qwen-VL 1.393 1.006 1.175 1.192 4 mPLUG-Owl2 1.402 -->

**EN** 4.4 Evaluation on Aesthetic Assessment

**ZH** 4.4 美学评价评测

**EN** To benchmark the aesthetic assessment capabilities, we evaluate the performance of existing MLLMs on the AesAQA subset. The experimental results are reported in Table 4. The results indicate that Q-Instruct achieves superior performance in overall accuracy for aesthetic classification. However, it is notable that the highest recorded prediction accuracy is only 52.86%, underscoring the limitations of even the most advanced MLLMs in accurately assessing aesthetic quality. Additionally, GPT-4V emerges as the model with the second-highest prediction accuracy, at 50.86%. An interesting observation from this table is the varying performance of MLLMs across different image types: the models are most effective with natural images, moderately effective with artistic images, and least effective with images generated by artificial intelligence. Furthermore, we also try to explore the abilities of MLLMs to generate fine-grained aesthetic scores, and results are provided in Supplementary Section 3. These experiments demonstrate that the aesthetic assessment abilities of MLLMs still need to be further strengthened in the future.

**ZH** 为对美学评价能力建立基准，我们在 AesAQA 子集上评测了现有 MLLM 的表现，实验结果报告于表 4。结果表明，Q-Instruct 在美学分类的总体准确率上表现最优。但值得注意的是，最高的预测准确率仅为 52.86%，这说明即便是最先进的 MLLM，在准确评价美学质量上仍存在局限。此外，GPT-4V 以 50.86% 的预测准确率位居第二。从表中还能观察到一个有趣现象：MLLM 在不同图像类型上的表现各异——模型在自然图像上最有效，在艺术图像上效果中等，在人工智能生成图像上最差。此外，我们还尝试探索 MLLM 生成细粒度美学分数的能力，结果见补充材料第 3 节。这些实验表明，MLLM 的美学评价能力在未来仍需进一步加强。

**EN** 4.5 Evaluation on Aesthetic Interpretation

**ZH** 4.5 美学阐释评测

**EN** We benchmark the interpretation abilities of current MLLMs in Table 5, where the values range from [0, 2], and the higher the value, the better the performance. From the table, GPT-4V is superior to other MLLMs in overall performance, while ShareGPT obtains the second-best overall performance. For the three different dimensions, we can find that almost all models suffer from unsatisfactory Precision, significantly less than the other dimensions (Relevance and Completeness). The significantly lower precision highlights the strong hallucination in the context of aesthetic interpretation, which underscores the crucial research for enhancing the aesthetic interpretation abilities of MLLMs, especially on language precision.

**ZH** 我们在表 5 中对现有 MLLM 的阐释能力建立基准，取值区间为 [0, 2]，数值越高表现越好。从表中可见，GPT-4V 在总体表现上优于其他 MLLM，ShareGPT 取得总体第二的成绩。就三个不同维度而言，我们发现几乎所有模型的精确性都不理想，明显低于另外两个维度（相关性与完整性）。精确性显著偏低凸显了美学阐释场景中的严重幻觉问题，这也说明提升 MLLM 美学阐释能力——尤其是语言精确性——是一项关键研究课题。

**EN** 5 Conclusion

**ZH** 5 结论

**EN** In this work, we introduce AesBench, an expert benchmark to comprehensively evaluate the aesthetic perception capacities of the current MLLMs. AesBench comprises two main components. First, the Expert-labeled Aesthetics Perception Database (EAPD), a high-quality dataset that serves as a gold standard for evaluating MLLMs in image aesthetics perception. Second, a four-dimensional evaluation framework is proposed, which consists of a set of comprehensive criteria across four key dimensions: Perception (AesP), Empathy (AesE), Assessment (AesA), and Interpretation (AesI). Experimental evaluations on AesBench demonstrate that most MLLMs are still weak in aesthetic perception capabilities. This also highlights that future development of MLLMs needs to consider more aesthetic dimensions.

**ZH** 本文提出 AesBench，一个用于全面评估当前 MLLM 美学感知能力的专家基准。AesBench 包含两个主要组成部分：其一是专家标注美学感知数据库（EAPD），这是一个高质量数据集，可作为评测 MLLM 图像美学感知能力的黄金标准；其二是一个四维评测框架，由覆盖感知（AesP）、共情（AesE）、评价（AesA）与阐释（AesI）四个关键维度的一整套综合准则构成。在 AesBench 上的实验评测表明，多数 MLLM 的美学感知能力仍然薄弱。这也提示未来 MLLM 的发展需要纳入更多美学维度。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] Achlioptas et al. [2021] Panos Achlioptas, Maks Ovsjanikov, Kilichbek Haydarov, Mohamed Elhoseiny, and Leonidas Guibas. Artemis: Affective language for visual art. In Proc. IEEE Conf. Comput. Vis. Pat -->

<!-- [原子块 · verbatim] Antol et al. [2015] Stanislaw Antol, Aishwarya Agrawal, Jiasen Lu, Margaret Mitchell, Dhruv Batra, C. Lawrence Zitnick, and Devi Parikh. VQA: Visual question answering. In Proc. IEEE Int. Conf. on Com -->

<!-- [原子块 · verbatim] Bai et al. [2023] Jinze Bai, Shuai Bai, Shusheng Yang, Shijie Wang, Sinan Tan, Peng Wang, Junyang Lin, Chang Zhou, and Jingren Zhou. Qwen-VL: A versatile vision-language model for understanding, local -->

<!-- [原子块 · verbatim] Cai et al. [2023] Rizhao Cai, Zirui Song, Dayan Guan, Zhenhao Chen, Xing Luo, Chenyu Yi, and Alex Kot. BenchLMM: Benchmarking cross-style visual capability of large multimodal models. arXiv preprint a -->

<!-- [原子块 · verbatim] Chen et al. [2023a] Jun Chen, Deyao Zhu, Xiaoqian Shen, Xiang Li, Zechu Liu, Pengchuan Zhang, Raghuraman Krishnamoorthi, Vikas Chandra, Yunyang Xiong, and Mohamed Elhoseiny. MiniGPT-v2: large language -->

<!-- [原子块 · verbatim] Chen et al. [2023b] Lin Chen, Jisong Li, Xiaoyi Dong, Pan Zhang, Conghui He, Jiaqi Wang, Feng Zhao, and Dahua Lin. ShareGPT4V: Improving large multi-modal models with better captions. arXiv preprint a -->

<!-- [原子块 · verbatim] Chen et al. [2023c] Yi Chen, Yuying Ge, Yixiao Ge, Mingyu Ding, Bohao Li, Rui Wang, Ruifeng Xu, Ying Shan, and Xihui Liu. EgoPlan-Bench: Benchmarking egocentric embodied planning with multimodal large -->

<!-- [原子块 · verbatim] Dai et al. [2023] Wenliang Dai, Junnan Li, Dongxu Li, Anthony Meng Huat Tiong, Junqi Zhao, Weisheng Wang, Boyang Li, Pascale Fung, and Steven Hoi. InstructBLIP: Towards general-purpose vision-language -->

<!-- [原子块 · verbatim] Devlin et al. [2019] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. BERT: Pre-training of deep bidirectional transformers for language understanding. arXiv preprint arXiv:1810.04805 -->

<!-- [原子块 · verbatim] Du et al. [2022] Zhengxiao Du, Yujie Qian, Xiao Liu, Ming Ding, Jiezhong Qiu, Zhilin Yang, and Jie Tang. GLM: General language model pretraining with autoregressive blank infilling. arXiv preprint arX -->

<!-- [原子块 · verbatim] Fang et al. [2020] Yuming Fang, Hanwei Zhu, Yan Zeng, Kede Ma, and Zhou Wang. Perceptual quality assessment of smartphone photography. In Proc. IEEE Conf. Comput. Vis. Pattern Recognit. , pages 3674–3 -->

<!-- [原子块 · verbatim] Feng et al. [2023] Tinglei Feng, Jiaxuan Liu, and Jufeng Yang. Probing sentiment-oriented pretraining inspired by human sentiment perception mechanism. In Proc. IEEE Conf. Comput. Vis. Pattern Recogni -->

<!-- [原子块 · verbatim] Google [2023] Google. Build with gemini, 2023. -->

<!-- [原子块 · verbatim] He et al. [2022] Shuai He, Yongchang Zhang, Rui Xie, Dongxiang Jiang, and Anlong Ming. Rethinking image aesthetics assessment: Models, datasets and benchmarks. Proc. Int. Joint Conf. Artif. Intell. ,  -->

<!-- [原子块 · verbatim] Hossain et al. [2019] MD Zakir Hossain, Ferdous Sohel, Mohd Fairuz Shiratuddin, and Hamid Laga. A comprehensive survey of deep learning for image captioning. ACM Computing Surveys (CsUR) , 51(6):1–36, -->

<!-- [原子块 · verbatim] Hosu et al. [2020] Vlad Hosu, Hanhe Lin, Tamas Sziranyi, and Dietmar Saupe. KonIQ-10k: An ecologically valid database for deep learning of blind image quality assessment. IEEE Trans. Image Process. ,  -->

<!-- [原子块 · verbatim] Huang et al. [2020] Yipo Huang, Leida Li, Hancheng Zhu, and Bo Hu. Blind quality index of depth images based on structural statistics for view synthesis. IEEE Signal Process. Lett. , 27:685–689, Apr.  -->

<!-- [原子块 · verbatim] Huang et al. [2023] Yipo Huang, Leida Li, Yuzhe Yang, Yaqian Li, and Yandong Guo. Explainable and generalizable blind image quality assessment via semantic attribute reasoning. IEEE Trans. Multimedia  -->

<!-- [原子块 · verbatim] Huggingface [2023] Huggingface. Introducing idefics: An open reproduction of state-of-the-art visual language model, 2023. -->

<!-- [原子块 · verbatim] Kong et al. [2016] S. Kong, X. Shen, Z. Lin, R. Mech, and C. Fowlkes. Photo aesthetics ranking network with attributes and content adaptation. In Proc. Eur. Conf. Comput. Vis. , pages 662–679, Sep. 20 -->

<!-- [原子块 · verbatim] Kruk et al. [2023] Julia Kruk, Caleb Ziems, and Diyi Yang. Impressions: Understanding visual semiotics and aesthetic impact. arXiv preprint arXiv:2310.17887 , 2023. -->

<!-- [原子块 · verbatim] Lai et al. [2023] Xin Lai, Zhuotao Tian, Yukang Chen, Yanwei Li, Yuhui Yuan, Shu Liu, and Jiaya Jia. LISA: Reasoning segmentation via large language model. arXiv preprint arXiv:2308.00692 , 2023. -->

<!-- [原子块 · verbatim] Li et al. [2018] Bo Li, Caiming Xiong, Tianfu Wu, Yu Zhou, Lun Zhang, and Rufeng Chu. Neural abstract style transfer for chinese traditional painting. arXiv preprint arXiv:1812.03264 , 2018. -->

<!-- [原子块 · verbatim] Li et al. [2023a] Bo Li, Yuanhan Zhang, Liangyu Chen, Jinghao Wang, Jingkang Yang, and Ziwei Liu. Otter: A multi-modal model with in-context instruction tuning. arXiv preprint arXiv:2305.03726 , 2023. -->

<!-- [原子块 · verbatim] Li et al. [2023b] Chunyi Li, Zicheng Zhang, Haoning Wu, Wei Sun, Xiongkuo Min, Xiaohong Liu, Guangtao Zhai, and Weisi Lin. AGIQA-3K: An open database for ai-generated image quality assessment. arXiv p -->

<!-- [原子块 · verbatim] Li et al. [2023c] Leida Li, Yipo Huang, Jinjian Wu, Yuzhe Yang, Yaqian Li, Yandong Guo, and Guangming Shi. Theme-aware visual attribute reasoning for image aesthetics assessment. IEEE Trans. Circuits  -->

<!-- [原子块 · verbatim] Liu et al. [2023a] Haotian Liu, Chunyuan Li, Yuheng Li, and Yong Jae Lee. Improved baselines with visual instruction tuning. arXiv preprint arXiv:2310.03744 , 2023. -->

<!-- [原子块 · verbatim] Liu et al. [2023b] Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. Visual instruction tuning. arXiv preprint arXiv:2304.08485 , 2023. -->

<!-- [原子块 · verbatim] Lu et al. [2021] Peng Lu, Hao Zhang, Xujun Peng, and Xiaofu Jin. Learning the relation between interested objects and aesthetic region for image cropping. IEEE Trans. Multimedia , 23:3618–3630, Oct. 2 -->

<!-- [原子块 · verbatim] OpenAI [2023] OpenAI. Introducing chatgpt, 2023. -->

<!-- [原子块 · verbatim] Radford et al. [2021] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, and Ilya Sut -->

<!-- [原子块 · verbatim] Sheikh et al. [2006] H.R. Sheikh, M.F. Sabir, and A.C. Bovik. A statistical evaluation of recent full reference image quality assessment algorithms. IEEE Trans. Image Process. , 15(11):3440–3451, Nov. -->

<!-- [原子块 · verbatim] Sheng et al. [2023] Xiangfei Sheng, Leida Li, Pengfei Chen, Jinjian Wu, Weisheng Dong, Yuzhe Yang, Liwu Xu, Yaqian Li, and Guangming Shi. Aesclip: Multi-attribute contrastive learning for image aesthe -->

<!-- [原子块 · verbatim] Touvron et al. [2023] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, Aurelien Rodriguez -->

<!-- [原子块 · verbatim] Unsplash [2023] Unsplash. Access the world’s largest open library dataset, 2023. -->

<!-- [原子块 · verbatim] Wang et al. [2023] Zijie J. Wang, Evan Montoya, David Munechika, Haoyang Yang, Benjamin Hoover, and Duen Horng Chau. DiffusionDB: A large-scale prompt gallery dataset for text-to-image generative mode -->

<!-- [原子块 · verbatim] Wu et al. [2023a] Haoning Wu, Zicheng Zhang, Erli Zhang, Chaofeng Chen, Liang Liao, Annan Wang, Kaixin Xu, Chunyi Li, Jingwen Hou, Guangtao Zhai, Geng Xue, Wenxiu Sun, Qiong Yan, and Weisi Lin. Q-Inst -->

<!-- [原子块 · verbatim] Wu et al. [2023b] Haoning Wu, Zicheng Zhang, Weixia Zhang, Chaofeng Chen, Liang Liao, Chunyi Li, Yixuan Gao, Annan Wang, Erli Zhang, Wenxiu Sun, Qiong Yan, Xiongkuo Min, Guangtao Zhai, and Weisi Lin.  -->

<!-- [原子块 · verbatim] Wu et al. [2024] Haoning Wu, Zicheng Zhang, Erli Zhang, Chaofeng Chen, Liang Liao, Annan Wang, Chunyi Li, Wenxiu Sun, Qiong Yan, Guangtao Zhai, and Weisi Lin. Q-Bench: A benchmark for general-purpose  -->

<!-- [原子块 · verbatim] Yang et al. [2022] Y. Yang, L. Xu, L. Li, N. Qie, Y. Li, P. Zhang, and Y. Guo. Personalized image aesthetics assessment with rich attributes. In Proc. IEEE Conf. Comput. Vis. Pattern Recog. , pages 19 -->

<!-- [原子块 · verbatim] Yang et al. [2023] Zhengyuan Yang, Linjie Li, Kevin Lin, Jianfeng Wang, Chung-Ching Lin, Zicheng Liu, and Lijuan Wang. The dawn of lmms: Preliminary explorations with gpt-4v(ision). arXiv preprint arX -->

<!-- [原子块 · verbatim] Ye et al. [2023] Qinghao Ye, Haiyang Xu, Jiabo Ye, Ming Yan, Anwen Hu, Haowei Liu, Qi Qian, Ji Zhang, Fei Huang, and Jingren Zhou. mPLUG-Owl2: Revolutionizing multi-modal large language model with mod -->

<!-- [原子块 · verbatim] Yi et al. [2023] Ran Yi, Haoyuan Tian, Zhihao Gu, Yu-Kun Lai, and Paul L. Rosin. Towards artistic image aesthetics assessment: a large-scale dataset and a new method. In Proc. IEEE Conf. Comput. Vis.  -->

<!-- [原子块 · verbatim] Yuan et al. [2023] Zhengqing Yuan, Zhaoxu Li, and Lichao Sun. TinyGPT-V: Efficient multimodal large language model via small backbones. arXiv preprint arXiv:2312.16862 , 2023. -->

<!-- [原子块 · verbatim] Zhang et al. [2023a] Zicheng Zhang, Chunyi Li, Wei Sun, Xiaohong Liu, Xiongkuo Min, and Guangtao Zhai. A perceptual quality assessment exploration for aigc images. arXiv preprint arXiv:2303.12618 , 20 -->

<!-- [原子块 · verbatim] Zhang et al. [2023b] Zicheng Zhang, Haoning Wu, Zhongpeng Ji, Chunyi Li, Erli Zhang, Wei Sun, Xiaohong Liu, Xiongkuo Min, Fengyu Sun, Shangling Jui, Weisi Lin, and Guangtao Zhai. Q-boost: On visual qu -->

<!-- [原子块 · verbatim] Zheng et al. [2023] Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric P. Xing, Hao Zhang, Joseph E. Gonzalez, and Ion Stoica.  -->

<!-- [原子块 · verbatim] Zhong et al. [2023] Zhipeng Zhong, Fei Zhou, and Guoping Qiu. Aesthetically relevant image captioning. In Proc. AAAI , volume 37, pages 3733–3741, 2023. -->

<!-- [原子块 · verbatim] Zhu et al. [2023] Deyao Zhu, Jun Chen, Xiaoqian Shen, Xiang Li, and Mohamed Elhoseiny. MiniGPT-4: Enhancing vision-language understanding with advanced large language models. arXiv preprint arXiv:2304 -->
