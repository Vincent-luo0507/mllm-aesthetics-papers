# Q-Bench：面向通用基础模型底层视觉能力的基准

> 原标题：Q-Bench: A Benchmark for General-Purpose Foundation Models on Low-level Vision
> 作者：Haoning Wu, Zicheng Zhang, Erli Zhang, Chaofeng Chen, Liang Liao, Annan Wang, Chunyi Li, Wenxiu Sun, Qiong Yan, Guangtao Zhai, Weisi Lin · arXiv:2309.14181 · 2023-09-25

<!-- [原子块 · verbatim] Q-Bench: A Benchmark for General-Purpose Foundation Models on Low-level Vision -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] The rapid evolution of Multi-modality Large Language Models (MLLMs) has catalyzed a shift in computer vision from specialized models to general-purpose foundation models. Nevertheless, there is still  -->

<!-- [原子块 · table]  -->

**EN** 1 Introduction

**ZH** 1 引言

**EN** The emergent large language models (LLMs) such as ChatGPT and Bard, as well as their excellent open-source counterparts (e.g., LLaMA (Touvron et al., 2023), MPT (Team, 2023)), have served as powerful general-purpose assistants, which opens a new era for artificial intelligence (AI) from targeting specific tasks towards general intelligence. Following the advancements of LLMs, multi-modality large language models (MLLMs), as represented by LLaVA (Liu et al., 2023b), MiniGPT-4 (Zhu et al., 2023), InstructBLIP (Dai et al., 2023), and Otter (Li et al., 2023a), have brought exciting progresses on the vision field as well. They are capable of providing robust general-level abilities on visual perception/understanding and can even seamlessly dialog and interact with humans through natural language. While such abilities of MLLMs have been explored and validated on several vision-language tasks such as image captioning (Chen et al., 2015), visual question answering (Antol et al., 2015), cross-modality grounding (Peng et al., 2023), and traditional vision tasks such as image classification or segmentation (Lai et al., 2023), most attention is paid to the high-level perception and understanding of visual contents. Meanwhile, the ability of MLLMs remains not clear on low-level visual perception and understanding, which play significant roles in image quality assessment (IQA) (Hosu et al., 2020; Fang et al., 2020) and its associated tasks on perceiving visual distortions (noises, blurs) (Su et al., 2021; Wu et al., 2023d) and other low-level attributes (color, lighting, composition, style, etc) (Kong et al., 2016) that may relate to aesthetics and emotions of natural photos (Murray et al., 2012) and human preferences on emerging computer-graphics generated (Zhang et al., 2023b) or AI-generated images (Li et al., 2023c; Xu et al., 2023). These low-level visual abilities are strongly associated with a wide range of applications, such as recommendation (Wu et al., 2023c), guidance on camera systems (Zhang et al., 2022), or visual quality enhancement (Zhang et al., 2018). Henceforth, it is crucial to evaluate the current abilities of these general-purpose foundation models in low-level visual perception and understanding, to ideally relieve extensive human resources to give feedback on every specific low-level task.

**ZH** 以 ChatGPT、Bard 为代表的大语言模型（LLM），以及 LLaMA（Touvron 等，2023）、MPT（Team，2023）等优秀的开源对应模型，已成为强大的通用助手，开启了人工智能（AI）从面向特定任务走向通用智能的新时代。伴随 LLM 的进展，以 LLaVA（Liu 等，2023b）、MiniGPT-4（Zhu 等，2023）、InstructBLIP（Dai 等，2023）与 Otter（Li 等，2023a）为代表的多模态大语言模型（MLLM）也在视觉领域带来了令人振奋的进展。它们能够在视觉感知/理解上提供稳健的通用能力，甚至可以通过自然语言与人类无缝对话交互。尽管 MLLM 的这些能力已在图像描述（Chen 等，2015）、视觉问答（Antol 等，2015）、跨模态定位（Peng 等，2023）等视觉—语言任务，以及图像分类、分割（Lai 等，2023）等传统视觉任务上得到探索与验证，绝大部分关注仍集中在视觉内容的高层感知与理解上。与此同时，MLLM 在底层视觉感知与理解上的能力仍不明朗，而后者在图像质量评价（IQA）（Hosu 等，2020；Fang 等，2020）及其相关任务中扮演重要角色——包括感知视觉失真（噪声、模糊）（Su 等，2021；Wu 等，2023d）以及其他底层属性（颜色、光照、构图、风格等）（Kong 等，2016），这些属性可能与自然照片的美学与情绪（Murray 等，2012），以及人类对新兴计算机图形生成（Zhang 等，2023b）或人工智能生成图像（Li 等，2023c；Xu 等，2023）的偏好相关。这些底层视觉能力与大量应用紧密相连，例如推荐（Wu 等，2023c）、相机系统引导（Zhang 等，2022）与视觉质量增强（Zhang 等，2018）。因此，评估这些通用基础模型当前在底层视觉感知与理解上的能力至关重要；理想情况下，可借此把在每个具体底层任务上提供反馈所需的大量人力解放出来。

<!-- [原子块 · img]  -->

**EN** Figure 1: In the proposed Q-Bench, we build the first benchmark on emerging abilities of MLLMs on low-level vision, including perception of low-level attributes (by correctly answering diverse queries) and description of low-level quality-related information via natural language. Furthermore, the Q-bench also evaluates the quantitative assessment ability of MLLMs on traditional IQA tasks.

**ZH** 图 1：在本文提出的 Q-Bench 中，我们构建了首个针对 MLLM 底层视觉新兴能力的基准，包括对底层属性的感知（通过正确回答各类提问），以及用自然语言描述底层质量相关信息。此外，Q-Bench 还评估 MLLM 在传统 IQA 任务上的定量评价能力。

**EN** In our work, we propose the first systematic benchmark to measure the low-level visual perception and understanding abilities of MLLMs. Our benchmark is constructed around a key question:

**ZH** 本文提出首个系统性基准，用于衡量 MLLM 的底层视觉感知与理解能力。我们的基准围绕一个关键问题构建：

**EN** How do MLLMs emulate human ability related to low-level visual perception and understanding?

**ZH** MLLM 如何在底层视觉感知与理解上复现人类的能力？

**EN** A simple answer is language, which is the fundamental property of MLLMs. Specifically, we define two emerging language abilities of MLLMs on low-level vision as follows:

**ZH** 一个简单的答案是语言——这正是 MLLM 的根本属性。具体而言，我们把 MLLM 在底层视觉上的两种新兴语言能力定义如下：

**EN** • Ability 1 (A1): Perception of Low-level Attributes. As shown in Fig. 1(a), like a human, an MLLM should be able to respond accurately to simple questions related to low-level attributes, e.g answering ‘No’ for a blurry image when queried with ‘Is this image clear?’

**ZH** • 能力 1（A1）：底层属性感知。如图 1（a）所示，如同人类一样，MLLM 应当能够准确回答与底层属性相关的简单问题，例如当被问到“这张图像清晰吗？”时，对一张模糊图像回答“否”。

**EN** • Ability 2 (A2): Description via Natural Language. As shown in Fig. 1(b), like a human, an MLLM should be able to describe the quality and other low-level information for an image with natural language. The descriptions should be both complete and accurate.

**ZH** • 能力 2（A2）：用自然语言描述。如图 1（b）所示，如同人类一样，MLLM 应当能够用自然语言描述图像的质量与其他底层信息，描述既要完整也要准确。

**EN** To systematically evaluate the low-level perception ability (A1) on various low-level attributes under diverse circumstances, we construct the LLVisionQA dataset, including 2,990 images from 10 diverse sources. Aligned with existing practices (Liu et al., 2023c; Lu et al., 2023), each image in LLVisionQA is equipped with a question, alongside a correct answer and false candidate answers. In LLVisionQA, we design three diverse types of questions: Yes-or-No questions, What questions, and How questions. Moreover, we divide low-level concerns into four quadrants, via two axes: (1) distortions (blur, noises, etc) vs other low-level attributes (color, lighting, composition, etc) (Guha et al., 2020). (2) global perception (e.g., sharpness of the whole picture) vs local content-related in-context perception (e.g., whether the red flower is in focus) (Li et al., 2019). With three types of questions and four quadrants of concerns, the proposed LLVisionQA dataset provides a holistic, diverse, and balanced benchmark for the perception ability on low-level visual attributes of MLLMs.

**ZH** 为系统评估 MLLM 在多样场景下对各类底层属性的感知能力（A1），我们构建 LLVisionQA 数据集，包含来自 10 个不同来源的 2,990 张图像。与已有做法（Liu 等，2023c；Lu 等，2023）一致，LLVisionQA 中每张图像都配有一个问题，并附带一个正确答案与若干错误候选答案。LLVisionQA 设计了三种多样的问题类型：是非型问题、What 型问题与 How 型问题。此外，我们通过两条轴把底层关注点划分为四个象限：（1）失真（模糊、噪声等）与其他底层属性（颜色、光照、构图等）之别（Guha 等，2020）；（2）全局感知（如整幅画面的锐度）与局部内容相关的上下文感知（如红花是否合焦）之别（Li 等，2019）。凭借三种问题类型与四个关注点象限，LLVisionQA 数据集为 MLLM 的底层视觉属性感知能力提供了一个全面、多样且均衡的基准。

**EN** For the description ability (A2), given that the output description is expected to be complex (without fixed formats), we propose the LLDescribe dataset by inviting experts to write long golden low-level descriptions (average 58 words per description) for 499 images, which serve as the reference texts for the single-modal GPT to evaluate MLLM output descriptions. The quality of MLLM descriptions is evaluated through three dimensions: completeness (punish missing information), preciseness (punish outputs controversial with reference), as well as relevance (punish outputs irrelevant to low-level attributes). With golden descriptions and the multi-dimensional evaluation process participated by GPT, we comprehensively evaluate the low-level description ability of MLLMs.

**ZH** 针对描述能力（A2），考虑到输出描述预期较为复杂（没有固定格式），我们提出 LLDescribe 数据集：邀请专家为 499 张图像撰写长篇黄金底层描述（平均每条 58 词），作为参考文本，供单模态 GPT 评估 MLLM 的输出描述。MLLM 描述的质量从三个维度评估：完整性（惩罚信息缺失）、精确性（惩罚与参考相矛盾的输出）以及相关性（惩罚与底层属性无关的输出）。借助黄金描述与 GPT 参与的多维评估流程，我们全面评估了 MLLM 的底层描述能力。

**EN** Besides the two emerging language abilities, we also evaluate MLLMs on the traditional IQA task, a more abstract task that requires understanding on human opinions of low-level attributes, as follows:

**ZH** 除这两种新兴语言能力外，我们还在传统 IQA 任务上评估 MLLM——这是一项更抽象的任务，要求理解人类对底层属性的意见，具体如下：

**EN** • Ability 3 (A3): Precise Assessment Aligned with Human Opinions. As depicted in Fig. 1(c), an MLLM should be able to predict quantifiable quality scores for images, which can be aligned with the human-rated mean opinion scores (MOS) on low-level visual appearances.

**ZH** • 能力 3（A3）：契合人类意见的精确评价。如图 1（c）所示，MLLM 应当能够为图像预测可量化的质量分数，并使其与人类对底层视觉外观给出的平均意见分数（MOS）相契合。

**EN** For the assessment ability (A3), we utilize plenty of existing IQA databases (Hosu et al., 2020; Lin et al., 2019; Li et al., 2023c) that focus on various low-level appearances of images, to benchmark MLLMs within conventional IQA settings. Specifically, we notice that MLLMs encounter difficulties in providing sufficiently quantifiable outputs, whether instructed to directly rate with texts or provide numerical outputs. To solve this challenge, we propose to extract the softmax pooling result on the logits of the two most frequent tokens (good and poor) under the response template of MLLMs (Fig 1(c)) as their quality predictions. Our studies prove that the proposed softmax-based strategy is generally better correlated with human perception than direct token outputs of MLLMs (via argmax), which bridges between these emergent MLLMs and the traditional IQA task settings. Under this strategy, we evaluate all MLLMs on their precise assessment ability by measuring the correlations between their predictions and human opinion scores in various IQA databases.

**ZH** 针对评价能力（A3），我们利用大量已有的 IQA 数据库（Hosu 等，2020；Lin 等，2019；Li 等，2023c）——它们关注图像的各种底层外观——在常规 IQA 设定下对 MLLM 做基准测试。具体而言，我们注意到 MLLM 难以给出足够可量化的输出，无论是指示其直接用文本打分还是给出数值输出。为解决这一难题，我们提出在 MLLM 的回复模板（图 1（c））下，提取两个最高频词元（good 与 poor）在 logits 上的 softmax 池化结果，作为其质量预测。我们的研究证明，相比 MLLM 直接输出词元（通过 argmax），所提出的基于 softmax 的策略与人类感知的相关性普遍更好，从而在这些新兴 MLLM 与传统 IQA 任务设定之间架起了桥梁。在该策略下，我们通过衡量 MLLM 的预测与各 IQA 数据库中人类意见分数的相关性，评估所有 MLLM 的精确评价能力。

**EN** In summary, we systematically explore the potential of MLLMs on three low-level visual abilities: perception, description, and assessment. The three realms compose into the proposed Q-Bench, a MLLM benchmark on low-level visual tasks. Our contributions can be summarized as three-fold:

**ZH** 综上，我们系统探索了 MLLM 在感知、描述与评价三项底层视觉能力上的潜力。这三个领域共同构成所提出的 Q-Bench——一个面向底层视觉任务的 MLLM 基准。我们的贡献可概括为三方面：

**EN** • We build a benchmark for MLLMs on low-level perception ability. To achieve this, we construct a first-of-its-kind balanced and comprehensive LLVisionQA dataset with 2,990 images with one low-level-related question-answer pair for each image. The LLVisionQA includes three question types and four quadrants of low-level concerns to ensure diversity.

**ZH** • 我们为 MLLM 构建了底层感知能力基准。为此，我们构建了首个均衡而全面的 LLVisionQA 数据集，包含 2,990 张图像，每张图像配有一组与底层相关的问题—答案对。LLVisionQA 包含三种问题类型与四个底层关注点象限，以保证多样性。

**EN** • We define a benchmark process to evaluate the low-level description ability of MLLMs, including an LLDescription dataset of 499 images with expert-labelled long golden quality descriptions, and a GPT-assisted evaluation to rate MLLM-descriptions in terms of completeness, preciseness, and relevance compared with golden descriptions.

**ZH** • 我们定义了一套评估 MLLM 底层描述能力的基准流程，包括含 499 张图像的 LLDescribe 数据集（由专家标注长篇黄金质量描述），以及在完整性、精确性与相关性三个维度上与黄金描述对比、由 GPT 辅助对 MLLM 描述打分的评估方法。

**EN** • To evaluate precise quality assessment ability, we propose a unified softmax-based quality prediction strategy for all MLLMs based on their probability outputs. With its effectiveness validated in our experiments, the proposed strategy sets up a bridge between general-purpose MLLMs and traditional IQA tasks that requires quantifiable scores as outputs.

**ZH** • 为评估精确质量评价能力，我们基于所有 MLLM 的概率输出，提出一种统一的基于 softmax 的质量预测策略。该策略的有效性在实验中得到验证，从而在通用 MLLM 与要求可量化分数输出的传统 IQA 任务之间架起了桥梁。

**EN** Table 1: Overview of the 10 diverse image source datasets in the Q-Bench, and the respective benchmark dataset size for each low-level ability among perception, descrption and assessment. The Corrupted COCO denotes COCO-Captions images corrupted by Michaelis et al. (2019).

**ZH** 表 1：Q-Bench 中 10 个不同图像来源数据集的概览，以及感知、描述与评价三项底层能力各自对应的基准数据集规模。Corrupted COCO 表示由 Michaelis 等（2019）施加失真后的 COCO-Captions 图像。

<!-- [原子块 · table] Type Image Source Dataset Sampled Size Sampled Size Full Dataset Size in LLVisionQA in LLDescribe for Assessment Task In-the-wild KONiQ-10K ( Hosu et al., 2020 ) 600 100 10,073 SPAQ ( Fang et al., 202 -->

**EN** 2 Constructing the Q-Bench

**ZH** 2 构建 Q-Bench

**EN** 2.1 General Principles

**ZH** 2.1 总体原则

**EN** Focusing on Low-level Visual Abilities of MLLMs.

**ZH** 聚焦 MLLM 的底层视觉能力。

**EN** Unlike existing MLLM benchmarks (Li et al., 2023b; Liu et al., 2023c; Lu et al., 2023) that aim at all-round abilities, the tasks in Q-Bench are constrained with two basic principles: (1) Requiring perception and/or understanding on low-level attributes of images; (2) Not requiring reasoning (i.e. why) or outside knowledge (Marino et al., 2019). We adhere to the principles in designing the perception, description, and assessment tasks, making the proposed Q-bench a focused reflection on the low-level visual abilities of MLLMs.

**ZH** 与面向全面能力的现有 MLLM 基准（Li 等，2023b；Liu 等，2023c；Lu 等，2023）不同，Q-Bench 的任务受两条基本原则约束：（1）要求对图像的底层属性进行感知和/或理解；（2）不要求推理（即“为什么”）或外部知识（Marino 等，2019）。我们在设计感知、描述与评价任务时都恪守这两条原则，使所提出的 Q-Bench 成为 MLLM 底层视觉能力的集中体现。

**EN** Covering Diverse Low-level Appearances.

**ZH** 覆盖多样的底层外观。

**EN** To cover diverse low-level appearances, we collect multi-sourced images for each task, as depicted in Tab. 1. Among all images in the perception and description tasks, two-thirds are in-the-wild images directly collected from social media posts, smartphones or professional photography. The rest one-third images are collected after various artificial distortions, or via generative processes (CGI, AIGC). Furthermore, we employ k-means clustering for the low-level attribute indicators to certify that the sub-sampled images retain high diversity. In the assessment task, full images of 7 IQA datasets within all three source types are evaluated through traditional IQA metrics. The diverse and multiple sources of images morph the Q-bench into a holistic and balanced benchmark to fairly evaluate low-level-related abilities.

**ZH** 为覆盖多样的底层外观，我们为每个任务收集多来源图像，如表 1 所示。在感知与描述任务的全部图像中，三分之二为直接采集自社交媒体帖子、智能手机或专业摄影的真实场景图像；其余三分之一则经各种人工失真处理，或通过生成流程（CGI、AIGC）得到。此外，我们对底层属性指标做 k 均值聚类，以确认子采样后的图像仍保持较高多样性。在评价任务中，我们在全部三种来源类型下评估 7 个 IQA 数据集的完整图像。多来源的多样图像使 Q-Bench 成为一个全面均衡的基准，能够公平评估与底层相关的能力。

**EN** 2.2 Benchmark on Low-level Perception Ability

**ZH** 2.2 底层感知能力基准

**EN** In the first task of Q-Bench, we evaluate the low-level perception ability of MLLMs to examine whether they can answer simple natural queries related to low-level attributes. For this purpose, we first collect 2,990 images (I) from multiple sources (see Table 1) with diverse low-level concerns. Then, we collect one low-level-related question (Q), one correct answer to the question (C), and 1-3 candidate false answers (F) for each image. The 2,990 (I,Q,C,F) tuples compose into the LLVisionQA dataset (as illustrated in Fig. 2), the first visual question answering (VQA) dataset in the low-level computer vision field. Specifically, the questions in LLVisionQA cover four quadrants of distinct low-level concerns (in Sec. 2.2.1) and three question types (in Sec. 2.2.2). After constructing the dataset, the (I,Q,C,F) are together fed into MLLMs for evaluation, while their outputs are further examined by GPT to judge correctness (in Sec. 2.2.3). The details are elaborated as follows.

**ZH** 在 Q-Bench 的第一个任务中，我们评估 MLLM 的底层感知能力，考察它们能否回答与底层属性相关的简单自然问询。为此，我们首先从多个来源（见表 1）收集 2,990 张具有多样底层关注点的图像（I）；随后为每张图像收集一个与底层相关的问题（Q）、一个正确答案（C）以及 1–3 个候选错误答案（F）。这 2,990 个 (I,Q,C,F) 元组构成 LLVisionQA 数据集（如图 2 所示），它是底层计算机视觉领域的首个视觉问答（VQA）数据集。具体而言，LLVisionQA 中的问题覆盖四个不同底层关注点象限（见 2.2.1 节）与三种问题类型（见 2.2.2 节）。数据集构建完成后，(I,Q,C,F) 被一并输入 MLLM 进行评估，其输出再由 GPT 判定正确性（见 2.2.3 节）。细节如下。

<!-- [原子块 · img]  -->

**EN** Figure 2: A dataset card of LLVisionQA that evaluates the low-level perception ability of MLLMs. 2,990 (I,Q,C,F) tuples are collected to cover three question types and four quadrants of low-level visual concerns, providing an all-around evaluation of low-level visual perception for MLLMs.

**ZH** 图 2：LLVisionQA 的数据集卡片，用于评估 MLLM 的底层感知能力。共收集 2,990 个 (I,Q,C,F) 元组，覆盖三种问题类型与四个底层视觉关注点象限，为 MLLM 的底层视觉感知提供全方位评估。

**EN** 2.2.1 Quadrants for Low-level Visual Concerns

**ZH** 2.2.1 底层视觉关注点的象限

**EN** Axis 1: Distortions vs Other Low-level Attributes. The primary axis differentiates two categories of low-level perceptual attributes: 1) technical distortions (Su et al., 2021), seen as the low-level characteristics that directly degrade the quality of images (Ying et al., 2020), and 2) aesthetic-related other low-level attributes (Kong et al., 2016; Hou et al., 2023) which are discernible to human perception and evoke varied emotions. Several studies (Talebi & Milanfar, 2018; Ying et al., 2020; Guha et al., 2020) follow this paradigm and categorize them through a relative golden standard, that whether the attributes directly improve or degrade picture quality (Yes⟦SLOT_0⟧Distortions; No⟦SLOT_1⟧Others). Despite this standard, we also enumerate common types of distortions vs other low-level attributes as extra guidance for constructing the LLVisionQA dataset, as listed in Sec. A.1.2.

**ZH** 轴 1：失真 vs 其他底层属性。第一条轴区分两类底层感知属性：1）技术性失真（Su 等，2021），被视为直接降低图像质量的底层特征（Ying 等，2020）；2）与美学相关的其他底层属性（Kong 等，2016；Hou 等，2023），它们可被人类感知辨别并唤起不同情绪。若干研究（Talebi & Milanfar，2018；Ying 等，2020；Guha 等，2020）沿用这一范式，并依据一个相对的黄金标准——该属性是否直接提升或降低画面质量——对二者分类（是⟦SLOT_0⟧失真；否⟦SLOT_1⟧其他）。除该标准外，我们还列举了失真与其他底层属性的常见类型，作为构建 LLVisionQA 数据集的额外指引，见 A.1.2 节。

**EN** Axis 2: Global Perception vs Local In-context Perception. In recent research on low-level vision, it is observed that human perceptions of low-level visuals often intertwine with higher-level contextual comprehension (Li et al., 2019; Wang et al., 2021; Wu et al., 2023a). For instance, a clear sky might lack complex textures yet display exceptional clarity. Furthermore, localized low-level appearances can deviate from their overall counterparts, as observed by Wu et al. (2022); Ying et al. (2021). Acknowledging these differences, we curate local in-context perception (Fig. 2 right) questions, that require MLLMs to grasp the content or other context to answer correctly, while other questions are categorized as global perception (Fig. 2 left). (More analysis in Sec. A.1.2.)

**ZH** 轴 2：全局感知 vs 局部上下文感知。在近期的底层视觉研究中，人们观察到人类对底层视觉的感知常常与更高层的上下文理解交织在一起（Li 等，2019；Wang 等，2021；Wu 等，2023a）。例如，一片晴朗的天空可能缺乏复杂纹理，却表现出极佳的清晰度。此外，局部的底层外观也可能偏离整体表现，Wu 等（2022）、Ying 等（2021）均有此观察。鉴于这些差异，我们精心设计了局部上下文感知问题（图 2 右），要求 MLLM 把握内容或其他上下文才能正确作答；其余问题则归为全局感知（图 2 左）。（更多分析见 A.1.2 节。）

**EN** 2.2.2 Question Types

**ZH** 2.2.2 问题类型

**EN** In the LLVisionQA dataset, we curate three question types, Yes-or-No, What, and How to simulate multiple query forms from humans. The details of the three question types are defined as follows.

**ZH** 在 LLVisionQA 数据集中，我们精心设计了是非型、What 型与 How 型三种问题类型，以模拟人类的多种提问形式。三种问题类型的具体定义如下。

**EN** Type 1: Yes-or-No Questions. The fundamental type of questions is Yes-or-No, i.e., judgments. Specifically, we notice that some MLLMs especially prefer to respond with yes rather than no. To reduce such biases in our benchmark, though designing questions with answers as yes is easier, we ensure that around 40% of all judgments are with correct answers as no, via querying on contrastive low-level attributes or non-existing low-level attributes. We further measure the bias levels of different MLLMs and present a further de-biased evaluation among them, as discussed in Sec. A.3.2.

**ZH** 类型 1：是非型问题。最基本的问题类型是是非型，即判断。具体而言，我们注意到部分 MLLM 尤其倾向于回答“是”而非“否”。为在本基准中降低这类偏差，尽管设计答案为“是”的问题更为容易，我们仍通过针对对比性底层属性或不存在的底层属性提问，确保约 40% 的判断类问题正确答案为“否”。我们进一步衡量不同 MLLM 的偏差程度，并在它们之间给出去偏后的评估结果，见 A.3.2 节。

**EN** Type 2: What Questions. Despite Yes-or-No judgments, the what questions are also a common type of queries in recent MLLM benchmarks such as Lu et al. (2023). In Q-bench, they classify low-level attributes in pictures (e.g., What distortion occurs in the image?), or associated context given specific low-level appearances (for in-context perception questions, e.g., Which object in the image is under-exposed?). Unlike Yes-or-No questions, the What questions examine more comprehensive low-level attribute understanding of MLLMs, by requiring correct perception on multiple attributes.

**ZH** 类型 2：What 型问题。除是非判断外，What 型问题也是近期 MLLM 基准（如 Lu 等（2023））中常见的问询类型。在 Q-Bench 中，这类问题对图像中的底层属性做分类（例如：图像中出现了哪种失真？），或在给定特定底层外观时判断相关上下文（对上下文感知问题，例如：图像中哪个物体曝光不足？）。与是非型问题不同，What 型问题要求对多个属性都形成正确感知，因而考察 MLLM 更全面的底层属性理解。

**EN** Type 3: How Questions. Despite the two common types, we also include a special type, the How questions, to cover non-extreme appearances (Wu et al., 2023d) of low-level attribute dimensions into our benchmark, as an extension to Yes-or-No questions. As shown in Fig. 2, we can query How is the clarity of the image? for the image with both clear and blurry areas, and answer with Medium. With this special question type, we broaden the Q-bench into finer-grained low-level perception.

**ZH** 类型 3：How 型问题。除上述两种常见类型外，我们还纳入一种特殊类型——How 型问题，以把底层属性维度上的非极端外观（Wu 等，2023d）纳入本基准，作为对是非型问题的扩展。如图 2 所示，对于同时存在清晰区域与模糊区域的图像，我们可以提问“图像的清晰度如何？”，并以“中等”作答。借助这一特殊问题类型，我们把 Q-Bench 拓展到更细粒度的底层感知。

**EN** 2.2.3 GPT-assisted Evaluation Process

**ZH** 2.2.3 GPT 辅助的评估流程

**EN** After constructing the LLVisionQA dataset, we feed it to multiple MLLMs to evaluate their abilities on low-level visual perception. The input format to query MLLMs is exemplified as follows:

**ZH** 构建完 LLVisionQA 数据集后，我们把它输入多个 MLLM，以评估它们的底层视觉感知能力。查询 MLLM 的输入格式示例如下：

**EN** #User: How is the clarity of the image? (Question) [IMAGE_TOKEN] (Image) Choose between one of the following options: A. High (Correct) B. Medium(Wrong) C. Low(Wrong)

**ZH** #用户：图像的清晰度如何？（问题）[IMAGE_TOKEN]（图像）请从以下选项中选择其一：A. 高（正确）B. 中等（错误）C. 低（错误）

**EN** The correct and wrong answers are shuffled during the actual evaluation. Moreover, while traditional visual question answering (Antol et al., 2015; Marino et al., 2019) tasks typically employ traditional language metrics (BLEU-4, CIDEr) to compare performance, as observed by recent studies (Ye et al., 2023) and validated by us, most MLLMs cannot consistently provide outputs on instructed formats. Given the question above, different MLLMs may reply “A.”, “High”, “The clarity of the image is high.”, “The image is of high clarity.” (all correct), which are difficult to be exhaustively-included under traditional metrics. To solve this problem, we design, validate, and employ a 5-round GPT-assisted evaluation process inspired by Liu et al. (2023c). Under this process, the question, correct answers, and MLLM replies are fed into GPT for evaluation (See Sec. A.2.1 for its details).

**ZH** 实际评估时，正确与错误答案会被打乱顺序。此外，尽管传统视觉问答任务（Antol 等，2015；Marino 等，2019）通常采用 BLEU-4、CIDEr 等传统语言指标比较性能，但正如近期研究（Ye 等，2023）所观察并经我们验证，多数 MLLM 无法稳定地按指定格式输出。对于上述问题，不同 MLLM 可能回复“A.”、“高”、“图像的清晰度高。”、“这张图像清晰度很高。”（全部正确），这些形式很难被传统指标穷尽涵盖。为解决该问题，我们设计、验证并采用了一种受 Liu 等（2023c）启发的 5 轮 GPT 辅助评估流程。在该流程下，问题、正确答案与 MLLM 回复被一并送入 GPT 进行评估（细节见 A.2.1 节）。

**EN** 2.3 Benchmark on Low-level Description Ability

**ZH** 2.3 底层描述能力基准

<!-- [原子块 · img]  -->

**EN** Figure 3: A dataset card of LLDescribe that evaluates the low-level description ability of MLLMs. 499 images from 10 diverse sources are labeled with golden descriptions, to serve as text references for single-modal GPT to evaluate the completeness, preciseness, and relevance of MLLM outputs.

**ZH** 图 3：LLDescribe 的数据集卡片，用于评估 MLLM 的底层描述能力。来自 10 个不同来源的 499 张图像被标注了黄金描述，作为文本参考，供单模态 GPT 评估 MLLM 输出的完整性、精确性与相关性。

**EN** In the second task of Q-Bench, we evaluate the language description ability of MLLMs on low-level information. This task is a sibling task of image captioning (Chen et al., 2015; Young et al., 2014; Agrawal et al., 2019) that describes image content with natural language, with a specific concern on the low-level appearance of images. To evaluate this ability automatically, we first derive a golden low-level description dataset, denoted as LLDescribe (Sec. 2.3.1), including one long (average 40 words) golden description provided by experts for each of 499 images. With these golden text descriptions, we are able to measure the quality of output low-level descriptions from MLLMs with a single-modal GPT, under the three dimensions: completeness, preciseness, as well as relevance (Sec 2.3.2). The discussions of the golden descriptions and the evaluation process are as follows.

**ZH** 在 Q-Bench 的第二个任务中，我们评估 MLLM 用语言描述底层信息的能力。该任务是用自然语言描述图像内容的图像描述任务（Chen 等，2015；Young 等，2014；Agrawal 等，2019）的姊妹任务，只是特别关注图像的底层外观。为自动评估这一能力，我们首先构建了一个黄金底层描述数据集，记为 LLDescribe（2.3.1 节），由专家为 499 张图像各提供一条长篇（平均 40 词）黄金描述。借助这些黄金文本描述，我们得以用单模态 GPT 从完整性、精确性与相关性三个维度（2.3.2 节）衡量 MLLM 输出的底层描述质量。关于黄金描述与评估流程的讨论如下。

**EN** 2.3.1 Defining Golden Low-level Descriptions for Images

**ZH** 2.3.1 为图像定义黄金底层描述

**EN** For the description ability, MLLMs should accurately and completely describe low-level visual information of images. Thus, the ground truths for these MLLMs are also built within a basic principle to cover as many low-level concerns as possible, so long as they are enumerated in Sec. 2.2.1 and occur in images. The resulting golden descriptions in LLDescribe have an average duration of 58 words, notably longer than common high-level image caption datasets (11 for Agrawal et al. (2019), 10 for Chen et al. (2015)). Similar to the LLVisionQA dataset for the perception task, the 499 images in LLDescribe dataset also include all 10 sources (as in Tab. 1) to cover images with diverse low-level appearances. The golden descriptions on different sources of images are depicted in Fig. 3.

**ZH** 就描述能力而言，MLLM 应当准确且完整地描述图像的底层视觉信息。因此，这些 MLLM 的真值也遵循一条基本原则构建：只要某底层关注点在 2.2.1 节中被列出且出现在图像中，就尽可能多地涵盖。最终 LLDescribe 中的黄金描述平均长 58 词，明显长于常见的高层图像描述数据集（Agrawal 等（2019）为 11 词，Chen 等（2015）为 10 词）。与感知任务的 LLVisionQA 数据集类似，LLDescribe 数据集中的 499 张图像同样涵盖全部 10 个来源（见表 1），以覆盖底层外观多样的图像。不同来源图像上的黄金描述见图 3。

**EN** 2.3.2 Evaluation with Single-modal GPT

**ZH** 2.3.2 用单模态 GPT 评估

**EN** Recent studies (Zheng et al., 2023) have proved single-modal GPT (OpenAI, 2023) to be a reliable evaluation tool for pure language tasks. Via the LLDescribe dataset, we convert the multi-modality problem into a text-only setting, by matching the MLLM outputs with the golden descriptions with single-modal GPT under three dimensions: (1) Completeness. More matched information with the golden description is encouraged. (2) Preciseness. The controversial information with the golden description is punished. (3) Relevance. More proportions of MLLM outputs should be related to low-level information, instead of others. Each dimension is scored among [0,1,2]. Similar as Sec. 2.2.3, we repeat 5 rounds for each single evaluation and collect the weighted average as the final score. The detailed settings for GPT to evaluate the three dimensions are in Sec. A.2.2.

**ZH** 近期研究（Zheng 等，2023）证明单模态 GPT（OpenAI，2023）是纯语言任务可靠的评估工具。通过 LLDescribe 数据集，我们把多模态问题转化为纯文本设定：用单模态 GPT 从三个维度把 MLLM 输出与黄金描述匹配：（1）完整性，鼓励与黄金描述匹配的信息更多；（2）精确性，惩罚与黄金描述相矛盾的信息；（3）相关性，要求 MLLM 输出中与底层信息相关的比例更高，而非其他内容。每个维度在 [0,1,2] 内打分。与 2.2.3 节类似，每次评估重复 5 轮，并取加权平均作为最终分数。GPT 评估三个维度的详细设定见 A.2.2 节。

**EN** 2.4 Benchmark on Precise Quality Assessment Ability

**ZH** 2.4 精确质量评价能力基准

<!-- [原子块 · object]  -->

**EN** Figure 4: The proposed softmax-based quality assessment strategy for MLLMs. Instead of directly decoding tokens from the [SCORE_TOKEN] position, the strategy extracts log probabilities (logits) of good and poor, and predicts quantifiable score via a softmax pooling between the two logits.

**ZH** 图 4：本文提出的面向 MLLM 的基于 softmax 的质量评价策略。该策略不从 [SCORE_TOKEN] 位置直接解码词元，而是提取 good 与 poor 的对数概率（logits），并对两个 logits 做 softmax 池化，从而预测出可量化的分数。

**EN** In the third task, we benchmark the ability of MLLMs to provide quantitative assessment on the overall low-level appearance of images. Unlike the two tasks above, we utilize existing IQA datasets that are collected across a variety of low-level appearances to evaluate how MLLMs can predict quantitative quality scores aligned with human opinions. All the three types of IQA datasets (in-the-wild, generated, artificially-distorted) as mentioned in Sec. 2.1 are evaluated, to provide a broad range measurement of the assessment ability of MLLMs. Nevertheless, how to collect quantifiable quality scores from MLLMs remains challenging as their outputs only have weak measurability (Sec. 2.4.1). Noticing that MLLMs can provide probabilities of tokens, we employ softmax pooling on the logits of good and poor under a simple and direct prompt template, deriving into quantifiable quality score predicted by MLLMs (Sec. 2.4.2), as illustrated in Fig. 4. Details are as follows.

**ZH** 在第三个任务中，我们对 MLLM 就图像整体底层外观给出定量评价的能力做基准测试。与上面两个任务不同，我们利用跨越多种底层外观收集的已有 IQA 数据集，评估 MLLM 预测的可量化质量分数能否与人类意见相契合。2.1 节提到的三类 IQA 数据集（真实场景、生成式、人工失真）全部参与评估，以便对 MLLM 的评价能力做宽范围度量。然而，由于 MLLM 的输出可度量性很弱（2.4.1 节），如何从中收集可量化的质量分数仍然困难。注意到 MLLM 能够给出词元的概率，我们在一个简单直接的提示模板下对 good 与 poor 的 logits 做 softmax 池化，得到 MLLM 预测的可量化质量分数（2.4.2 节），如图 4 所示。细节如下。

**EN** 2.4.1 Weak Measurability of MLLM Outputs

**ZH** 2.4.1 MLLM 输出的弱可度量性

**EN** In Q-Bench, we aim to fairly compare the assessment ability between different MLLMs on diverse low-level appearances. Henceforth, our principle is to define a unified, simplest instruction that is applicable for all MLLMs on all IQA datasets. Under this principle, we conduct toy experiments on LLVisionQA on Shikra and LLaVA-v1, with two simple instruction strategies: (A) Direct Instruction, in which the prompt is designed as simple as “Rate the quality of the image”. The top-frequency answers are good (78%), and poor (20%), with other outputs almost negligible. (B) Numerical Instruction, in which we specifically instruct numerical ratings, with the prompt: “Score the quality of the image from 1 to 5, with 1 as lowest and 5 as highest.”. Under the numerical strategy, the top-frequency answers are 5 (84%), 1 (9%), and 3 (5%); though within the score range, the frequencies of scores 2 and 4 are both less than 1%. The toy experiments imply the weak measurability of MLLM outputs, given that the answers are statistically 1) biased towards positive, 2) biased towards extreme, and 3) with only two effective scales. Therefore, it is necessary to explore extended strategies for MLLMs to provide truly quantifiable outputs for low-level assessment.

**ZH** 在 Q-Bench 中，我们旨在公平比较不同 MLLM 在多样底层外观上的评价能力。因此我们的原则是：定义一套统一、最简单的指令，适用于所有 MLLM 与所有 IQA 数据集。在此原则下，我们在 LLVisionQA 上用 Shikra 与 LLaVA-v1 做了两种简单指令策略的玩具实验：（A）直接指令，提示设计为最简单的“评价这张图像的质量”。最高频答案为 good（78%）与 poor（20%），其他输出几乎可忽略。（B）数值指令，即明确要求给出数值评分，提示为：“请给这张图像的质量打分，1 到 5 分，1 分最低，5 分最高。”在数值策略下，最高频答案为 5（84%）、1（9%）与 3（5%）；虽然在分值范围内，分数 2 与 4 的出现频率都不足 1%。这些玩具实验说明 MLLM 输出的可度量性很弱——答案在统计上 1）偏向正向，2）偏向极端，3）只有两个有效刻度。因此有必要探索扩展策略，使 MLLM 能为底层评价提供真正可量化的输出。

**EN** 2.4.2 A Softmax-based Evaluation Strategy

**ZH** 2.4.2 基于 Softmax 的评估策略

**EN** Given the above observations, we design the softmax-based evaluation strategy (Fig. 4) to reduce the negative impacts of the biases and lack of scales. To start with, we design our strategy within the Direct Instruction, which is more general and less biased than the Numerical Instruction. The strategy is based on the observation that two top-frequency outputs, good and poor, can be considered as anchors for better and worse human perception, and the Direct Strategy can be approximated into a binary classification problem on the [SCORE_TOKEN] position, or technically, an argmax between the logits of good (⟦SLOT_2⟧) and poor (⟦SLOT_3⟧) on this position. In our revised strategy, we modify the argmax into softmax to collect better quantifiable scores:

**ZH** 基于上述观察，我们设计了基于 softmax 的评估策略（图 4），以降低偏差与刻度不足带来的负面影响。首先，我们把策略建立在直接指令之上——它比数值指令更通用、偏差更小。该策略基于如下观察：good 与 poor 这两个最高频输出可被视为人类感知中“较好”与“较差”的锚点，直接策略可近似为 [SCORE_TOKEN] 位置上的二分类问题，技术上即该位置上 good（⟦SLOT_2⟧）与 poor（⟦SLOT_3⟧）两个 logits 之间的 argmax。在我们改进后的策略中，把 argmax 改为 softmax，以收集更好的可量化分数：

<!-- [原子块 · table] q pred = e x SCORE_TOKEN good e x SCORE_TOKEN good + e x SCORE_TOKEN poor q_{\mathrm{pred}}=\frac{e^{x^{\text{{good}}}_{\textit{SCORE\_TOKEN}}}}{e^{x^{\text{{good}}}_{\textit{SCORE\_TOKEN}}}+e^{x^{\te -->

**EN** This simple and generally-applicable strategy enables us to collect quantifiable outputs (⟦SLOT_4⟧) from MLLMs with higher correlation to human ratings, as verified in our experimental analysis (Tab. 9).

**ZH** 这一简单且普遍适用的策略使我们能够从 MLLM 收集到与人类评分相关性更高的可量化输出（⟦SLOT_4⟧），实验分析（表 9）验证了这一点。

**EN** 3 Results on Q-Bench

**ZH** 3 Q-Bench 上的结果

**EN** In Q-Bench, we evaluate 15 variants on 13 up-to-date popular and competitive open-source MLLMs, together with GPT-4V, under zero-shot settings. More results and analyses are appended in Sec. A.3.

**ZH** 在 Q-Bench 中，我们在零样本设定下评估了 13 个当下流行且有竞争力的开源 MLLM 的 15 个变体，以及 GPT-4V。更多结果与分析见 A.3 节。

**EN** Table 2: Results on the test subset for the low-level Perception ability of MLLMs. MLLMs with top-3 performance in each sub-category and the overall LLVisionQA is emphasized with boldface.

**ZH** 表 2：MLLM 底层感知能力在测试子集上的结果。各子类别与 LLVisionQA 整体上表现前三的 MLLM 以粗体标出。

<!-- [原子块 · table] Sub-categories Question Types Quadrants of Low-level Concerns Overall ↑ \uparrow Model (variant) Yes-or-No ↑ \uparrow What ↑ \uparrow How ↑ \uparrow Distortion ↑ \uparrow Other ↑ \uparrow In-context I -->

**EN** 3.1 Results and Observations on Perception

**ZH** 3.1 感知方面的结果与观察

**EN** Open-Source MLLMs. For a holistic examination on the perception ability of MLLMs, we evaluate the multi-choice correctness of MLLMs on different sub-categories of the LLVision dataset, which is equally divided as dev (Tab. 7, will be released) and test (Tab. 2, will keep private) subsets. We are glad that the majority of MLLMs can significantly outperform random guess on all sub-categories. Considering that all participating MLLMs are without any explicit training on low-level visual attributes, these results show strong potentials for these general-purpose models when further fine-tuned with respective low-level datasets. Among all MLLMs, the recently-released InternLM-XComposer-VL reaches the best accuracy on this question-answering task, followed by LLaVA-v1.5, QWen-VL and InstructBLIP (Flan-T5), which show rather close results. By achieving more than 60% accuracy on both subsets, these models show exciting potentials as robust low-level visual assistants in the future. Another key observation is that almost all methods perceive worse on distortions than other low-level attributes. One exception is LLaMA-Adapter-V2, which is the only MLLM that adopts multi-scale features as visual inputs. We also notice that all MLLMs prefer yes than no among Yes-or-No questions, as analyzed in Tab. 8; qualitative comparisons are illustrated in Fig. 10. For Kosmos-2, we specially adopt close-set inference for it, as discussed in Sec. A.2.1.

**ZH** 开源 MLLM。为全面考察 MLLM 的感知能力，我们评估各 MLLM 在 LLVision 数据集不同子类别上的多选正确率；该数据集被等分为开发集（表 7，将公开）与测试集（表 2，将保持私有）两个子集。令人欣慰的是，多数 MLLM 在所有子类别上都显著优于随机猜测。考虑到所有参评 MLLM 都未针对底层视觉属性做过任何显式训练，这些结果显示出这些通用模型在用相应底层数据集进一步微调后的巨大潜力。在所有 MLLM 中，近期发布的 InternLM-XComposer-VL 在该问答任务上取得最佳准确率，其次是 LLaVA-v1.5、QWen-VL 与 InstructBLIP（Flan-T5），它们的结果相当接近。这些模型在两个子集上都取得了 60% 以上的准确率，展现出未来作为稳健底层视觉助手的喜人潜力。另一个关键观察是，几乎所有方法对失真的感知都弱于其他底层属性。唯一的例外是 LLaMA-Adapter-V2，它是唯一采用多尺度特征作为视觉输入的 MLLM。我们还注意到，在是非型问题上所有 MLLM 都更偏向“是”而非“否”，表 8 对此做了分析；定性比较见图 10。对于 Kosmos-2，我们特别采用了闭集推理，见 A.2.1 节。

**EN** GPT-4V vs Human. To evaluate the low-level perception abilities of the commercial MLLM, GPT-4V, we gauge its accuracy against human using the test subset of LLVision dataset. GPT-4V exhibits competitive performance and outperforms open-source MLLMs by a large margin (+9%), and on par accuracy with the Junior-level Human. Despite its prowess, there is still a way to go for GPT-4V before it can match the overall proficiency of the Senior-level Human (with experiences on low-level visual tasks, 8% better than GPT-4V). Furthermore, across all categories, the results show that GPT-4V, much like its open-source counterparts, faces challenges in recognizing distortions.

**ZH** GPT-4V 与人类对比。为评估商用 MLLM GPT-4V 的底层感知能力，我们用 LLVision 数据集的测试子集把它的准确率与人类做对比。GPT-4V 表现出有竞争力的性能，大幅领先开源 MLLM（+9%），并与初级人类水平持平。尽管表现出色，GPT-4V 要达到资深人类（具备底层视觉任务经验，比 GPT-4V 高 8%）的整体熟练度仍有距离。此外，各类别的结果显示，GPT-4V 与其开源同类一样，在识别失真方面存在困难。

**EN** 3.2 Results and Observations on Description

**ZH** 3.2 描述方面的结果与观察

**EN** For the description ability, InternLM-XComposer-VL reaches best proficiency again, especially in terms of the relevance dimension. Nevertheless, in the perspective of the completeness and precision of the descriptions, even the best of all MLLMs cannot obtain an excellent score; on the contrary, almost all MLLMs reach an acceptable standard (0.8/2.0). In general, all MLLMs at present are only with relatively limited and primary ability to provide low-level visual descriptions. We also conduct a qualitative comparison for MLLM descriptions in Sec. A.3.3.

**ZH** 在描述能力上，InternLM-XComposer-VL 再次达到最佳水平，尤其在相关性维度上。然而从描述的完整性与精确性看，即便所有 MLLM 中最好的一个也无法取得优秀分数；相反，几乎所有 MLLM 都只达到可接受的水平（0.8/2.0）。总体而言，当前所有 MLLM 提供底层视觉描述的能力仍相对有限、处于初级水平。我们还在 A.3.3 节对 MLLM 描述做了定性比较。

**EN** Table 3: Results on the low-level Description ability of MLLMs. ⟦SLOT_5⟧ denotes frequency for score ⟦SLOT_6⟧.

**ZH** 表 3：MLLM 底层描述能力的结果。⟦SLOT_5⟧ 表示分数 ⟦SLOT_6⟧ 出现的频次。

<!-- [原子块 · table] Dimensions Completeness Precision Relevance Sum. ↑ \uparrow Model ( variant ) P 0 P_{0} P 1 P_{1} P 2 P_{2} score ↑ \uparrow P 0 P_{0} P 1 P_{1} P 2 P_{2} score ↑ \uparrow P 0 P_{0} P 1 P_{1} P 2 P_{2 -->

**EN** Table 4: Main evaluation results on the zero-shot Assessment ability of MLLMs, in comparison with NIQE and CLIP-ViT-Large-14, the visual backbone of most MLLMs. Metrics are SRCC/PLCC.

**ZH** 表 4：MLLM 零样本评价能力的主要评估结果，并与 NIQE 及多数 MLLM 的视觉骨干 CLIP-ViT-Large-14 对比。指标为 SRCC/PLCC。

<!-- [原子块 · table] Dataset Type In-the-wild Generated Artificial Average Model / Dataset KONiQ-10k SPAQ LIVE-FB LIVE-itw CGIQA-6K AGIQA-3K KADID-10K NIQE ( Mittal et al., 2013 ) 0.316/0.377 0.693 / 0.669 0.211/0.288 0.4 -->

**EN** 3.3 Results and Observations on Assessment

**ZH** 3.3 评价方面的结果与观察

**EN** To measure the assessment ability, we evaluate the performance of 15 MLLMs on 7 IQA datasets that are with at least 1,000 images and 15 human ratings per image (itu, 2000). Primarily, we notice that the majority of MLLMs are notably better than NIQE on non-natural circumstances (CGI, AIGC, artificial distortions), showing their potential towards general-purpose evaluators on a broader range of low-level appearances. We also notice that without explicit alignment with human opinions during training, the most excellent MLLM, which is again InternLM-XComposer-VL, can already outperform CLIP-ViT-Large-14 by a large margin (20%), marking the dawn of MLLMs as robust quality evaluators. Furthermore, we also design a synonym ensemble (see Sec. A.2.3) strategy which can further generally improve IQA accuracy of MLLMs, whose results are analyzed in Sec. A.3.5. Despite their proficiency, current MLLMs are still less accurate in finer-grained situations (LIVE-FB, CGIQA-6K) for the assessment task, which could be enhanced in the future.

**ZH** 为衡量评价能力，我们在 7 个 IQA 数据集上评估了 15 个 MLLM 的表现，这些数据集各自至少包含 1,000 张图像，且每张图像有 15 个人类评分（itu，2000）。首先我们注意到，在非自然场景（CGI、AIGC、人工失真）下，多数 MLLM 明显优于 NIQE，显示出它们作为面向更广泛底层外观的通用评价器的潜力。我们还注意到，在训练中未与人类意见做显式对齐的情况下，最优秀的 MLLM——同样是 InternLM-XComposer-VL——已经可以大幅（20%）超过 CLIP-ViT-Large-14，标志着 MLLM 作为稳健质量评价器的曙光。此外，我们还设计了一种同义词集成策略（见 A.2.3 节），可进一步普遍提升 MLLM 的 IQA 准确性，其结果在 A.3.5 节分析。尽管表现不俗，当前 MLLM 在更细粒度的场景（LIVE-FB、CGIQA-6K）下评价仍不够准确，这可在未来加以改进。

**EN** 4 Conclusion

**ZH** 4 结论

**EN** In this study, we construct the Q-Bench, a benchmark to examine the progresses of MLLMs on low-level visual abilities. Anticipating these large foundation models to be general-purpose intelligence that can ultimately relieve human efforts, we propose that MLLMs should achieve three important and distinct abilities: accurate perception on low-level visual attributes, precise and complete language description on low-level visual information, as well as quantitative assessment on image quality. To evaluate the abilities, we collect two multi-modality benchmark datasets for low-level vision, and propose a unified softmax-based quantitative IQA strategy on MLLMs. Our evaluation proves that even without any low-level-specific training, several extraordinary MLLMs still have decent low-level abilities. Nevertheless, there is still a long way to go for MLLMs to be truly-reliable general low-level visual assistants. We sincerely hope that the observations found in the Q-Bench can inspire future MLLMs to enhance the low-level perception and understanding abilities.

**ZH** 本研究构建了 Q-Bench——一个用于检验 MLLM 在底层视觉能力上进展的基准。我们期待这些大型基础模型成为最终能把人类从繁重劳动中解放出来的通用智能，并提出 MLLM 应当具备三项重要而不同的能力：对底层视觉属性的准确感知、对底层视觉信息的精确而完整的语言描述，以及对图像质量的定量评价。为评估这些能力，我们收集了两个面向底层视觉的多模态基准数据集，并提出一种面向 MLLM 的、统一的基于 softmax 的定量 IQA 策略。我们的评估证明，即便没有任何底层专项训练，若干出色的 MLLM 仍具备不错的底层能力。尽管如此，MLLM 要成为真正可靠的通用底层视觉助手仍有很长的路要走。我们衷心希望 Q-Bench 中的发现能启发未来的 MLLM 增强其底层感知与理解能力。

**EN** Author Contributions

**ZH** 作者贡献

**EN** We will reveal the contributions of authors in the final edition.

**ZH** 我们将在最终版本中公布作者贡献。

**EN** Acknowledgments

**ZH** 致谢

**EN** 100% of the annotated labels in the LLVisionQA and LLDescribe datasets (question-answers and long golden descriptions) are conducted by human experts. We sincerely thank their efforts.

**ZH** LLVisionQA 与 LLDescribe 数据集中的标注（问答与长篇黄金描述）100% 由人类专家完成。我们衷心感谢他们的付出。

**EN** We thank the anonymous reviewers on ICLR2024 Conference on providing valuable and constructive suggestions for us to improve this paper.

**ZH** 感谢 ICLR2024 会议的匿名审稿人提出宝贵而富有建设性的建议，帮助我们改进本文。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] itu (2000) Recommendation 500-10: Methodology for the subjective assessment of the quality of television pictures. ITU-R Rec. BT.500, 2000. -->

<!-- [原子块 · verbatim] Agrawal et al. (2019) Harsh Agrawal, Karan Desai, Yufei Wang, Xinlei Chen, Rishabh Jain, Mark Johnson, Dhruv Batra, Devi Parikh, Stefan Lee, and Peter Anderson. nocaps: novel object captioning at scal -->

<!-- [原子块 · verbatim] Antol et al. (2015) Stanislaw Antol, Aishwarya Agrawal, Jiasen Lu, Margaret Mitchell, Dhruv Batra, C. Lawrence Zitnick, and Devi Parikh. VQA: Visual Question Answering. In ICCV , 2015. -->

<!-- [原子块 · verbatim] Bai et al. (2023) Jinze Bai, Shuai Bai, Shusheng Yang, Shijie Wang, Sinan Tan, Peng Wang, Junyang Lin, Chang Zhou, and Jingren Zhou. Qwen-vl: A versatile vision-language model for understanding, local -->

<!-- [原子块 · verbatim] Chen et al. (2023) Keqin Chen, Zhao Zhang, Weili Zeng, Richong Zhang, Feng Zhu, and Rui Zhao. Shikra: Unleashing multimodal llm’s referential dialogue magic. arXiv preprint arXiv:2306.15195 , 2023. -->

<!-- [原子块 · verbatim] Chen et al. (2015) Xinlei Chen, Hao Fang, Tsung-Yi Lin, Ramakrishna Vedantam, Saurabh Gupta, Piotr Dollar, and C. Lawrence Zitnick. Microsoft coco captions: Data collection and evaluation server, 2015 -->

<!-- [原子块 · verbatim] Dai et al. (2023) Wenliang Dai, Junnan Li, Dongxu Li, Anthony Meng Huat Tiong, Junqi Zhao, Weisheng Wang, Boyang Li, Pascale Fung, and Steven Hoi. Instructblip: Towards general-purpose vision-language -->

<!-- [原子块 · verbatim] Du et al. (2022) Zhengxiao Du, Yujie Qian, Xiao Liu, Ming Ding, Jiezhong Qiu, Zhilin Yang, and Jie Tang. Glm: General language model pretraining with autoregressive blank infilling. In Proceedings of  -->

<!-- [原子块 · verbatim] Fang et al. (2020) Yuming Fang, Hanwei Zhu, Yan Zeng, Kede Ma, and Zhou Wang. Perceptual quality assessment of smartphone photography. In CVPR , 2020. -->

<!-- [原子块 · verbatim] Gao et al. (2023) Peng Gao, Jiaming Han, Renrui Zhang, Ziyi Lin, Shijie Geng, Aojun Zhou, Wei Zhang, Pan Lu, Conghui He, Xiangyu Yue, Hongsheng Li, and Yu Qiao. Llama-adapter v2: Parameter-efficient v -->

<!-- [原子块 · verbatim] Ghadiyaram & Bovik (2016) Deepti Ghadiyaram and Alan C. Bovik. Massive online crowdsourced study of subjective and objective picture quality. IEEE , 25(1):372–387, 2016. -->

<!-- [原子块 · verbatim] Guha et al. (2020) Tanaya Guha, Vlad Hosu, Dietmar Saupe, Bastian Goldlücke, Naveen Kumar, Weisi Lin, Victor Martinez, Krishna Somandepalli, Shrikanth Narayanan, Wen-Huang Cheng, Kree McLaughlin, Hart -->

<!-- [原子块 · verbatim] Hosu et al. (2020) Vlad Hosu, Hanhe Lin, Tamas Sziranyi, and Dietmar Saupe. Koniq-10k: An ecologically valid database for deep learning of blind image quality assessment. IEEE TIP , 29:4041–4056, 2020 -->

<!-- [原子块 · verbatim] Hou et al. (2023) Jingwen Hou, Weisi Lin, Yuming Fang, Haoning Wu, Chaofeng Chen, Liang Liao, and Weide Liu. Towards transparent deep image aesthetics assessment with tag-based content descriptors. IE -->

<!-- [原子块 · verbatim] Huggingface (2023) Huggingface. Introducing idefics: An open reproduction of state-of-the-art visual language model, 2023. URL https://huggingface.co/blog/idefics . -->

<!-- [原子块 · verbatim] Jayaraman et al. (2012) Dinesh Jayaraman, Anish Mittal, Anush K. Moorthy, and Alan C. Bovik. Objective quality assessment of multiply distorted images. In ASILOMAR , pp. 1693–1697, 2012. -->

<!-- [原子块 · verbatim] Kong et al. (2016) Shu Kong, Xiaohui Shen, Zhe Lin, Radomir Mech, and Charless Fowlkes. Photo aesthetics ranking network with attributes and content adaptation. In ECCV , 2016. -->

<!-- [原子块 · verbatim] Lai et al. (2023) Xin Lai, Zhuotao Tian, Yukang Chen, Yanwei Li, Yuhui Yuan, Shu Liu, and Jiaya Jia. Lisa: Reasoning segmentation via large language model. arXiv preprint arXiv:2308.00692 , 2023. -->

<!-- [原子块 · verbatim] Li et al. (2023a) Bo Li, Yuanhan Zhang, Liangyu Chen, Jinghao Wang, Jingkang Yang, and Ziwei Liu. Otter: A multi-modal model with in-context instruction tuning. arXiv preprint arXiv:2305.03726 , 2023a -->

<!-- [原子块 · verbatim] Li et al. (2023b) Bohao Li, Rui Wang, Guangzhi Wang, Yuying Ge, Yixiao Ge, and Ying Shan. Seed-bench: Benchmarking multimodal llms with generative comprehension, 2023b. -->

<!-- [原子块 · verbatim] Li et al. (2023c) Chunyi Li, Zicheng Zhang, Haoning Wu, Wei Sun, Xiongkuo Min, Xiaohong Liu, Guangtao Zhai, and Weisi Lin. Agiqa-3k: An open database for ai-generated image quality assessment, 2023c. -->

<!-- [原子块 · verbatim] Li et al. (2019) Dingquan Li, Tingting Jiang, Weisi Lin, and Ming Jiang. Which has better visual quality: The clear blue sky or a blurry animal? IEEE TMM , 21(5):1221–1234, 2019. -->

<!-- [原子块 · verbatim] Lin et al. (2019) Hanhe Lin, Vlad Hosu, and Dietmar Saupe. Kadid-10k: A large-scale artificially distorted iqa database. In QoMEX , pp. 1–3, 2019. -->

<!-- [原子块 · verbatim] Liu et al. (2023a) Haotian Liu, Chunyuan Li, Yuheng Li, and Yong Jae Lee. Improved baselines with visual instruction tuning, 2023a. -->

<!-- [原子块 · verbatim] Liu et al. (2023b) Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. Visual instruction tuning, 2023b. -->

<!-- [原子块 · verbatim] Liu et al. (2023c) Yuan Liu, Haodong Duan, Yuanhan Zhang, Bo Li, Songyang Zhang, Wangbo Zhao, Yike Yuan, Jiaqi Wang, Conghui He, Ziwei Liu, Kai Chen, and Dahua Lin. Mmbench: Is your multi-modal model  -->

<!-- [原子块 · verbatim] Lu et al. (2023) Jiaying Lu, Jinmeng Rao, Kezhen Chen, Xiaoyuan Guo, Yawen Zhang, Baochen Sun, Carl Yang, and Jie Yang. Evaluation and mitigation of agnosia in multimodal large language models, 2023. -->

<!-- [原子块 · verbatim] Marino et al. (2019) Kenneth Marino, Mohammad Rastegari, Ali Farhadi, and Roozbeh Mottaghi. Ok-vqa: A visual question answering benchmark requiring external knowledge. In Conference on Computer Vision -->

<!-- [原子块 · verbatim] Michaelis et al. (2019) Claudio Michaelis, Benjamin Mitzkus, Robert Geirhos, Evgenia Rusak, Oliver Bringmann, Alexander S. Ecker, Matthias Bethge, and Wieland Brendel. Benchmarking robustness in objec -->

<!-- [原子块 · verbatim] Mittal et al. (2013) Anish Mittal, Rajiv Soundararajan, and Alan C. Bovik. Making a “completely blind” image quality analyzer. IEEE Signal Processing Letters , 20(3):209–212, 2013. -->

<!-- [原子块 · verbatim] Murray et al. (2012) Naila Murray, Luca Marchesotti, and Florent Perronnin. Ava: A large-scale database for aesthetic visual analysis. In CVPR , pp. 2408–2415, 2012. -->

<!-- [原子块 · verbatim] OpenAI (2023) OpenAI. Gpt-4 technical report, 2023. -->

<!-- [原子块 · verbatim] Peng et al. (2023) Zhiliang Peng, Wenhui Wang, Li Dong, Yaru Hao, Shaohan Huang, Shuming Ma, and Furu Wei. Kosmos-2: Grounding multimodal large language models to the world. ArXiv , abs/2306, 2023. -->

<!-- [原子块 · verbatim] Radford et al. (2021) Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, and Ilya Sut -->

<!-- [原子块 · verbatim] Su et al. (2021) Shaolin Su, Vlad Hosu, Hanhe Lin, Yanning Zhang, and Dietmar Saupe. Koniq++ : Boosting no-reference image quality assessment in the wild by jointly predicting image quality and defect -->

<!-- [原子块 · verbatim] Talebi & Milanfar (2018) Hossein Talebi and Peyman Milanfar. Nima: Neural image assessment. IEEE TIP , 2018. -->

<!-- [原子块 · verbatim] Team (2023) MosaicML NLP Team. Introducing mpt-7b: A new standard for open-source, commercially usable llms, 2023. URL www.mosaicml.com/blog/mpt-7b . Accessed: 2023-05-05. -->

<!-- [原子块 · verbatim] Touvron et al. (2023) Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, Aurelien Rodriguez -->

<!-- [原子块 · verbatim] Wang et al. (2022) Jianyi Wang, Kelvin C. K. Chan, and Chen Change Loy. Exploring clip for assessing the look and feel of images, 2022. -->

<!-- [原子块 · verbatim] Wang et al. (2021) Yilin Wang, Junjie Ke, Hossein Talebi, Joong Gon Yim, Neil Birkbeck, Balu Adsumilli, Peyman Milanfar, and Feng Yang. Rich features for perceptual quality assessment of ugc videos. I -->

<!-- [原子块 · verbatim] Wu et al. (2022) Haoning Wu, Chaofeng Chen, Jingwen Hou, Liang Liao, Annan Wang, Wenxiu Sun, Qiong Yan, and Weisi Lin. Fast-vqa: Efficient end-to-end video quality assessment with fragment sampling. I -->

<!-- [原子块 · verbatim] Wu et al. (2023a) Haoning Wu, Chaofeng Chen, Liang Liao, Jingwen Hou, Wenxiu Sun, Qiong Yan, Jinwei Gu, and Weisi Lin. Neighbourhood representative sampling for efficient end-to-end video quality asse -->

<!-- [原子块 · verbatim] Wu et al. (2023b) Haoning Wu, Liang Liao, Chaofeng Chen, Jingwen Hou Hou, Erli Zhang, Annan Wang, Wenxiu Sun, Qiong Yan, and Weisi Lin. Exploring opinion-unaware video quality assessment with semantic -->

<!-- [原子块 · verbatim] Wu et al. (2023c) Haoning Wu, Erli Zhang, Liang Liao, Chaofeng Chen, Jingwen Hou, Annan Wang, Wenxiu Sun, Qiong Yan, and Weisi Lin. Exploring video quality assessment on user generated contents from a -->

<!-- [原子块 · verbatim] Wu et al. (2023d) Haoning Wu, Erli Zhang, Liang Liao, Chaofeng Chen, Jingwen Hou, Annan Wang, Wenxiu Sun, Qiong Yan, and Weisi Lin. Towards explainable video quality assessment: A database and a langu -->

<!-- [原子块 · verbatim] Xu et al. (2023) Jiazheng Xu, Xiao Liu, Yuchen Wu, Yuxuan Tong, Qinkai Li, Ming Ding, Jie Tang, and Yuxiao Dong. Imagereward: Learning and evaluating human preferences for text-to-image generation, 20 -->

<!-- [原子块 · verbatim] Ye et al. (2023) Qinghao Ye, Haiyang Xu, Guohai Xu, Jiabo Ye, Ming Yan, Yiyang Zhou, Junyang Wang, Anwen Hu, Pengcheng Shi, Yaya Shi, Chaoya Jiang, Chenliang Li, Yuanhong Xu, Hehong Chen, Junfeng Tian -->

<!-- [原子块 · verbatim] Ying et al. (2020) Zhenqiang Ying, Haoran Niu, Praful Gupta, Dhruv Mahajan, Deepti Ghadiyaram, and Alan Bovik. From patches to pictures (paq-2-piq): Mapping the perceptual space of picture quality. In -->

<!-- [原子块 · verbatim] Ying et al. (2021) Zhenqiang Ying, Maniratnam Mandal, Deepti Ghadiyaram, and Alan Bovik. Patch-vq: ’patching up’ the video quality problem. In CVPR , 2021. -->

<!-- [原子块 · verbatim] Young et al. (2014) Peter Young, Alice Lai, Micah Hodosh, and Julia Hockenmaier. From image descriptions to visual denotations: New similarity metrics for semantic inference over event descriptions. T -->

<!-- [原子块 · verbatim] Zhang et al. (2022) Cheng Zhang, Shaolin Su, Yu Zhu, Qingsen Yan, Jinqiu Sun, and Yanning Zhang. Exploring and evaluating image restoration potential in dynamic scenes. In CVPR , pp. 2057–2066, 2022. -->

<!-- [原子块 · verbatim] Zhang et al. (2023a) Pan Zhang, Xiaoyi Dong, Bin Wang, Yuhang Cao, Chao Xu, Linke Ouyang, Zhiyuan Zhao, Shuangrui Ding, Songyang Zhang, Haodong Duan, Wenwei Zhang, Hang Yan, Xinyue Zhang, Wei Li, Jing -->

<!-- [原子块 · verbatim] Zhang et al. (2018) Richard Zhang, Phillip Isola, Alexei A. Efros, Eli Shechtman, and Oliver Wang. The unreasonable effectiveness of deep features as a perceptual metric. In CVPR , pp. 586–595, 2018. -->

<!-- [原子块 · verbatim] Zhang et al. (2023b) Zicheng Zhang, Wei Sun, Tao Wang, Wei Lu, Quan Zhou, Qiyuan Wang, Xiongkuo Min, Guangtao Zhai, et al. Subjective and objective quality assessment for in-the-wild computer graphics -->

<!-- [原子块 · verbatim] Zhang et al. (2023c) Zicheng Zhang, Wei Sun, Yingjie Zhou, Haoning Wu, Chunyi Li, Xiongkuo Min, and Xiaohong Liu. Advancing zero-shot digital human quality assessment through text-prompted evaluation, -->

<!-- [原子块 · verbatim] Zheng et al. (2023) Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric. P Xing, Hao Zhang, Joseph E. Gonzalez, and Ion Stoica.  -->

<!-- [原子块 · verbatim] Zhu et al. (2023) Deyao Zhu, Jun Chen, Xiaoqian Shen, Xiang Li, and Mohamed Elhoseiny. Minigpt-4: Enhancing vision-language understanding with advanced large language models. arXiv preprint arXiv:2304 -->

**EN** Appendix A Appendix

**ZH** 附录 A 附录

**EN** A.1 More Information on Benchmark Datasets

**ZH** A.1 关于基准数据集的更多信息

**EN** A.1.1 Subjective Experiment

**ZH** A.1.1 主观实验

**EN** A total of eleven experts, each with professional skills and extensive experience in photography, are invited to participate in the subjective labeling experiment of Q-Bench. The subjective experiment takes place in a laboratory environment with standard indoor lighting. A Dell-4K monitor, which supports a resolution of ⟦SLOT_7⟧, is used for displaying the interfaces. The screenshots of interfaces can be referred to in Fig. 5. Each expert annotates up to 30 images a day to avoid fatigue, and every annotation is carefully reviewed by at least three other experts before acceptance. In this way, we ensure the accuracy and rigor of the Q-Bench labels to the greatest extent possible. This, in turn, makes the performance testing capability of Q-Bench more precise and meaningful.

**ZH** 我们邀请了共十一位具备专业技能与丰富摄影经验的专家参与 Q-Bench 的主观标注实验。主观实验在标准室内照明的实验室环境中进行，使用一台支持 ⟦SLOT_7⟧ 分辨率的 Dell-4K 显示器呈现界面，界面截图可参见图 5。每位专家每天最多标注 30 张图像以避免疲劳，每条标注在采纳前都经过至少三位其他专家的仔细复核。如此，我们尽最大可能保证 Q-Bench 标注的准确性与严谨性，进而使 Q-Bench 的性能测试能力更加精确、更有意义。

<!-- [原子块 · img]  -->

**EN** (a) Interface for the LLVisionQA dataset (Perception)

**ZH** （a）LLVisionQA 数据集（感知）的界面

<!-- [原子块 · img]  -->

**EN** (b) Interface for the LLDescribe dataset (Description)

**ZH** （b）LLDescribe 数据集（描述）的界面

**EN** Figure 5: The illustration of the annotation interfaces for the LLVisionQA dataset (questions, answers) on Peception ability, and the LLDescribe dataset (text description) on Description ability.

**ZH** 图 5：LLVisionQA 数据集（问题、答案）在感知能力上，与 LLDescribe 数据集（文本描述）在描述能力上的标注界面示意。

**EN** A.1.2 More Details on LLVisionQA

**ZH** A.1.2 关于 LLVisionQA 的更多细节

**EN** The Enumeration on Distortions and Other Low-level Attributes:

**ZH** 失真与其他底层属性的枚举：

**EN** Distortions: Blurs [lens blur (out-of-focus), motion blur, zoom blur, gaussian blur, glass blur], Noises [gaussian noise, speckle noise, pepper noise], Artifacts [compression artifact, transmission error], Exposure Issues [under-exposure, over-exposure], Miscellaneous Artificial Distortions [pixelate, color-diffusion, jitter, etc] Other low-level attributes: Color [color style, color vividity], Lighting [bright, dim], Composition [Symmetrical, Rule-of-Thirds], Visual Styles [animation, realism, computer-generated, AI-generated], Photographic Methods [background bokeh (shallow DOF), high contrast, motion blur (on fast-moving objects), etc]

**ZH** 失真：模糊［镜头模糊（失焦）、运动模糊、变焦模糊、高斯模糊、玻璃模糊］、噪声［高斯噪声、散斑噪声、椒盐噪声］、伪影［压缩伪影、传输错误］、曝光问题［曝光不足、曝光过度］、其他人工失真［像素化、色彩扩散、抖动等］ 其他底层属性：颜色［色彩风格、色彩鲜艳度］、光照［明亮、昏暗］、构图［对称、三分法］、视觉风格［动画、写实、计算机生成、人工智能生成］、摄影手法［背景虚化（浅景深）、高对比度、运动模糊（针对快速运动物体）等］

**EN** Relationship between In-context Questions and Global Questions:

**ZH** 上下文问题与全局问题之间的关系：

**EN** Distortions: Is this image blurred? ⟦SLOT_8⟧ In-context Distortions: Is the tree in the image blurred? Distortions: How is the clarity of the image? ⟦SLOT_9⟧ In-context Distortions: How is the clarity of the man’s face?

**ZH** 失真：这张图像模糊吗？⟦SLOT_8⟧ 上下文失真：图像中的树模糊吗？ 失真：图像的清晰度如何？⟦SLOT_9⟧ 上下文失真：画面中男子的面部清晰度如何？

**EN** Other low-level: Is this image colorful? ⟦SLOT_10⟧ In-context Other: Is the house colorful? Other low-level: How is brightness of the image? ⟦SLOT_11⟧ In-context Other: Which is the darkest object?

**ZH** 其他底层属性：这张图像色彩丰富吗？⟦SLOT_10⟧ 上下文其他属性：这栋房子色彩丰富吗？ 其他底层属性：图像的亮度如何？⟦SLOT_11⟧ 上下文其他属性：哪个物体最暗？

**EN** A.2 Details on Benchmark Evaluation Settings

**ZH** A.2 基准评估设定的细节

**EN** A.2.1 Evaluation Details for Perception Ability

**ZH** A.2.1 感知能力评估细节

**EN** [Special Note] Multi-choice Question vs Close-Set Inference for Kosmos-2:

**ZH** ［特别说明］Kosmos-2 的多选题与闭集推理：

**EN** While Kosmos-2 performs generally well on the description and assessment tasks, we notice that it is hardly capable of answering a multi-choice question with the general prompt form applicable for other methods, as follows:

**ZH** 虽然 Kosmos-2 在描述与评价任务上总体表现良好，我们注意到它几乎无法用适用于其他方法的通用提示形式来回答多选题，如下所示：

**EN** How is the clarity of the image? (Question) [IMAGE_TOKEN] (Image) Choose between one of the following options: A. High (Correct) B. Medium(Wrong) C. Low(Wrong)

**ZH** 图像的清晰度如何？（问题）[IMAGE_TOKEN]（图像）请从以下选项中选择其一：A. 高（正确）B. 中等（错误）C. 低（错误）

**EN** For most situations (86%) in our primary sample test with the prompts above, Kosmos-2 will directly append a new candidate (e.g., D. Excellent or D. Very Low) answer instead of choosing one option among them, denoted as prompt failure. This might be because the language model of Kosmos-2 has smaller capacity (1B) than other MLLMs that are based on LLaMA/MPT (7B/13B).

**ZH** 在我们用上述提示所做的初步抽样测试中，多数情况（86%）下 Kosmos-2 会直接追加一个新的候选答案（如 D. 极佳 或 D. 极低），而不是在已有选项中做出选择，我们称之为提示失效。这可能是因为 Kosmos-2 的语言模型容量（1B）小于其他基于 LLaMA/MPT（7B/13B）的 MLLM。

**EN** Considering that the prompt failure is actually not directly related with low-level perception, we try different prompt engineering techniques to reduce the prompt failure rate, and finalize with a simple modification which can limit the prompt failure to less than 10% in our sample set, as follows:

**ZH** 考虑到提示失效实际上与底层感知没有直接关系，我们尝试了不同的提示工程技术来降低提示失效率，最终找到一种简单修改，可把样本集上的提示失效率限制在 10% 以下，如下所示：

**EN** How is the clarity of the image? (Question) [IMAGE_TOKEN] (Image) Choose between one of the following options: A. High (Correct) B. Medium(Wrong) C. Low(Wrong) #Answer:

**ZH** 图像的清晰度如何？（问题）[IMAGE_TOKEN]（图像）请从以下选项中选择其一：A. 高（正确）B. 中等（错误）C. 低（错误）#答案：

**EN** Nevertheless, we are still not able to eliminate the prompt failures for Kosmos-2. Henceforth, to systematically remove the negative effect of prompt failures on multi-choice questions for Kosmos-2, we conduct a choice-free special setting for it, i.e. close-set inference, via ranking the perplexity of different answers and choose the answer with minimum generative loss:

**ZH** 尽管如此，我们仍无法彻底消除 Kosmos-2 的提示失效。因此，为系统性消除提示失效对 Kosmos-2 多选题的负面影响，我们为其设计了一种无选项的特殊设定，即闭集推理：对不同答案的困惑度排序，并选择生成损失最小的答案：

**EN** How is the clarity of the image? [IMAGE_TOKEN] #Answer: High ⟦SLOT_12⟧ loss:7.43 ⟦SLOT_13⟧ ✓ Choose this. How is the clarity of the image? [IMAGE_TOKEN] #Answer: Medium ⟦SLOT_14⟧ loss:7.56 ⟦SLOT_15⟧ ✗ How is the clarity of the image? [IMAGE_TOKEN] #Answer: Low ⟦SLOT_16⟧ loss:7.92 ⟦SLOT_17⟧ ✗

**ZH** 图像的清晰度如何？[IMAGE_TOKEN] #答案：高 ⟦SLOT_12⟧ 损失：7.43 ⟦SLOT_13⟧ ✓ 选择此项。 图像的清晰度如何？[IMAGE_TOKEN] #答案：中等 ⟦SLOT_14⟧ 损失：7.56 ⟦SLOT_15⟧ ✗ 图像的清晰度如何？[IMAGE_TOKEN] #答案：低 ⟦SLOT_16⟧ 损失：7.92 ⟦SLOT_17⟧ ✗

**EN** As shown in Tab. 5, perplexity-based close-set inference can notably improve results of Kosmos-2. Considering that it is still the MLLM with fewest parameters among the ten models, its results are decent at its model size. More importantly, they validate that our observation on the prompt failure is reasonable, and we will further delve deeper into this problem of MLLMs in our extended works.

**ZH** 如表 5 所示，基于困惑度的闭集推理能显著改善 Kosmos-2 的结果。考虑到它仍是十个模型中参数量最少的 MLLM，其结果在其模型规模下已相当不错。更重要的是，这些结果验证了我们关于提示失效的观察是合理的，我们将在后续工作中进一步深入这一问题。

**EN** Table 5: Perplexity-based close-set evaluation compared with normal evaluation on LLVisionQA; after eliminating the prompt failures, the results of Kosmos-2 significantly improved.

**ZH** 表 5：LLVisionQA 上基于困惑度的闭集评估与常规评估的对比；在消除提示失效后，Kosmos-2 的结果显著提升。

<!-- [原子块 · table] Sub-categories Question Types Quadrants of Low-level Concerns Overall ↑ \uparrow # ↓ \downarrow Model (variant) Yes-or-No ↑ \uparrow What ↑ \uparrow How ↑ \uparrow Distortion ↑ \uparrow Other ↑ \uparr -->

**EN** Settings for GPT Evaluation:

**ZH** GPT 评估的设置：

**EN** Given GPT’s inherent variability, identical prompts can yield non-definitive responses. To address the impact of such situations on our evaluation, we’ve implemented a 5-round voting strategy. Under this approach, we pose the same prompt as defined in the following templates five times, taking the popular votes of GPT’s answers to determine the final outcome. Our human analysis on a sample set confirms that the 5-round voting strategy improves GPT evaluation accuracy from 93.2% to 98.4%, reducing errors to only 1/4 compared with the single-round evaluation.

**ZH** 鉴于 GPT 固有的可变性，相同的提示可能产生不确定的回复。为降低此类情况对评估的影响，我们实施了 5 轮投票策略：把下述模板中定义的同一提示提交五次，取 GPT 回答的多数票决定最终结果。我们在样本集上的人工分析确认，5 轮投票策略把 GPT 评估准确率从 93.2% 提升到 98.4%，相较单轮评估把错误降至约四分之一。

**EN** Prompt Templates for GPT Evaluation:

**ZH** GPT 评估的提示模板：

**EN** #System: You are a helpful assistant that grades answers related to image quality and aesthetics. There are a lot of special terms or keywords related to image processing and photography. You will pay attention to the context of ’quality evaluation’ when grading.

**ZH** #系统：你是一个乐于助人的助手，负责对与图像质量和美学相关的回答打分。图像处理与摄影领域有大量专业术语或关键词。打分时请注意“质量评价”这一语境。

**EN** #User: Assuming you are a grader, you will now be provided with a question [question] and a set of options [options] with option [options[0]] being the correct answer. Additionally, there will be an answer [answer] provided by a respondent. Please determine whether the respondentś answer is correct considering the context of the question. Even if the word choice is not completely the same, you can decide based on the given options and see whether the one in the answer is close enough to the given correct answer, The result is 1 if the answer is correct and else the result is 0. Please only provide the result in the following format: Result:

**ZH** #用户：假设你是一名评分者，现在将向你提供一个问题 [question] 和一组选项 [options]，其中选项 [options[0]] 为正确答案。此外，还会有一个回答者给出的答案 [answer]。请结合问题的语境判断该回答者的答案是否正确。即便用词不完全一致，你也可以依据所给选项判断答案中的表述是否与正确答案足够接近。答案正确则结果为 1，否则为 0。请仅按以下格式给出结果：结果：

**EN** Examples for GPT Evaluation:

**ZH** GPT 评估的示例：

<!-- [原子块 · img]  -->

**EN** Figure 6: Image of example (1).

**ZH** 图 6：示例（1）的图像。

<!-- [原子块 · img]  -->

**EN** Figure 7: Image of example (2).

**ZH** 图 7：示例（2）的图像。

<!-- [原子块 · img]  -->

**EN** Figure 8: Image of example (3).

**ZH** 图 8：示例（3）的图像。

**EN** (1) “Rephrased” Answers. (Fig. 8)

**ZH** （1）“改写式”答案。（图 8）

**EN** Question: Which is the brightest part in this image?

**ZH** 问题：这张图像中最亮的部分是哪里？

**EN** Choices: [‘Capital letters E and S’, ‘ST’, ‘18’, ‘56’]

**ZH** 选项：［“大写字母 E 和 S”、“ST”、“18”、“56”］

**EN** MLLM Answer:

**ZH** MLLM 回答：

**EN** The brightest part in this image is the neon sign with the letters “E” and “S” in capital letters.

**ZH** 这张图像中最亮的部分是带有大写字母“E”和“S”的霓虹灯招牌。

**EN** 5-Round GPT Answers: [“Score: 1”,“Score: 1”,“Score: 1”,“Score: 1”,“Score: 1”] ⟦SLOT_18⟧ Final Correctness after Voting: ✓

**ZH** 5 轮 GPT 回答：［“得分：1”、“得分：1”、“得分：1”、“得分：1”、“得分：1”］⟦SLOT_18⟧ 投票后最终正确性：✓

**EN** (2) “Distracted” Answers. (Fig. 8)

**ZH** （2）“分心式”答案。（图 8）

**EN** Question: How’s the level of blur in the image?

**ZH** 问题：图像的模糊程度如何？

**EN** Choices: [‘Some blur’, ‘Not blurry at all’, ‘Very blurry’]

**ZH** 选项：［“有些模糊”、“完全不模糊”、“非常模糊”］

**EN** MLLM Answer:

**ZH** MLLM 回答：

**EN** The image has some blur, but it is not very blurry.

**ZH** 这张图像有些模糊，但并不十分模糊。

**EN** 5-Round GPT Answers: [“Score: 1”,“Score: 1”,“Score: 1”,“Score: 1”,“Score: 1”] ⟦SLOT_19⟧ Final Correctness after Voting: ✓

**ZH** 5 轮 GPT 回答：［“得分：1”、“得分：1”、“得分：1”、“得分：1”、“得分：1”］⟦SLOT_19⟧ 投票后最终正确性：✓

**EN** (3) “Both” Answers. (Fig. 8)

**ZH** （3）“两者皆有式”答案。（图 8）

**EN** Question: Is the little boy emphasized in the center of the composition of the image?

**ZH** 问题：小男孩是否被强调在图像构图的中心？

**EN** Choices: [‘No’, ‘Yes’]

**ZH** 选项：［“否”、“是”］

**EN** MLLM Answer:

**ZH** MLLM 回答：

**EN** A. No, the little boy is not emphasized in the center of the composition of the image. B. Yes,

**ZH** A. 否，小男孩没有被强调在图像构图的中心。B. 是，

**EN** 5-Round GPT Answers: [“Score: 1”,“Score: 0”,“Score: 0”,“Score: 1”,“Score: 0”] ⟦SLOT_20⟧ Final Correctness after Voting: ✗

**ZH** 5 轮 GPT 回答：［“得分：1”、“得分：0”、“得分：0”、“得分：1”、“得分：0”］⟦SLOT_20⟧ 投票后最终正确性：✗

**EN** A.2.2 Evaluation Details for Description Ability

**ZH** A.2.2 描述能力评估细节

**EN** General Description Prompt for MLLMs:

**ZH** 面向 MLLM 的通用描述提示：

**EN** #User: Describe the quality, aesthetics and other low-level appearance of the image in details.

**ZH** #用户：请详细描述图像的质量、美学以及其他底层外观。

**EN** Settings for GPT Evaluation:

**ZH** GPT 评估的设置：

**EN** Given GPT’s inherent variability, identical prompts can yield non-definitive responses. To address the impact of such situations on our evaluation, we’ve implemented a 5-round average pooling strategy. Under this approach, we pose the same prompt as defined in the following templates five times, taking the mean result of GPT’s answers to determine the final outcome. This method effectively mitigates the unpredictability associated with GPT, ensuring a more accurate score.

**ZH** 鉴于 GPT 固有的可变性，相同的提示可能产生不确定的回复。为降低此类情况对评估的影响，我们实施了 5 轮平均池化策略：把下述模板中定义的同一提示提交五次，取 GPT 回答的均值决定最终结果。该方法有效缓解了 GPT 带来的不可预测性，确保分数更为准确。

**EN** Prompt Templates for GPT Evaluation:

**ZH** GPT 评估的提示模板：

**EN** #System: You are a helpful assistant.

**ZH** #系统：你是一个乐于助人的助手。

**EN** Completeness. #User: Evaluate whether the description [MLLM_DESC] completely includes the low-level visual information in the reference description [GOLDEN_DESC]. Please rate score 2 for completely or almost completely including reference information, 0 for not including at all, 1 for including part of the information or similar description. Please only provide the result in the following format: Score: Preciseness. #The precision metric punishes controversial low-level descriptions that output description contrasts with the referencce, e.g., blur for clear, high quality for low quality, colorful for monotonous, noisy for clean, bright for dark. Evaluate whether output [b] precisely reflects reference [a]. Please rate score 2 for totally no controversial low-level description, 1 for less controversial low-level description than matched descrpition, and 0 for more controversial low-level description than matched description. Please only provide the result in the following format: Score: Relevance. #User: Evaluate whether the description [MLLM_DESC] is relevant to the low-level visual information, which may include blur, noise, exposure, artifact, color, lighting, focus, composition, etc. Please rate score 2 for completely relevant, 1 for partly relevant, and 0 for totally irrelevant. Please only provide the result in the following format: Score:

**ZH** 完整性。#用户：请评估描述 [MLLM_DESC] 是否完整涵盖了参考描述 [GOLDEN_DESC] 中的底层视觉信息。若完全或几乎完全涵盖参考信息请打 2 分，完全未涵盖打 0 分，涵盖部分信息或描述相近打 1 分。请仅按以下格式给出结果：得分： 精确性。#精确性指标惩罚那些与参考相矛盾的底层描述，例如把清晰说成模糊、把低质量说成高质量、把单调说成多彩、把干净说成有噪、把暗说成亮。请评估输出 [b] 是否精确反映了参考 [a]。若完全没有矛盾的底层描述打 2 分，矛盾的底层描述少于匹配描述打 1 分，矛盾的底层描述多于匹配描述打 0 分。请仅按以下格式给出结果：得分： 相关性。#用户：请评估描述 [MLLM_DESC] 是否与底层视觉信息相关，后者可能包括模糊、噪声、曝光、伪影、颜色、光照、对焦、构图等。完全相关打 2 分，部分相关打 1 分，完全不相关打 0 分。请仅按以下格式给出结果：得分：

**EN** In the prompt template, the [MLLM_DESC] denotes the output description from MLLMs, and [GOLDEN_DESC] denotes the golden description in the LLDescribe dataset.

**ZH** 在提示模板中，[MLLM_DESC] 表示 MLLM 的输出描述，[GOLDEN_DESC] 表示 LLDescribe 数据集中的黄金描述。

**EN** Examples for GPT Evaluation:

**ZH** GPT 评估的示例：

**EN** (A) Completeness.

**ZH** （A）完整性。

**EN** User Input: #User: Evaluate whether the description [ The image is a large, clear, and detailed picture of a white airplane flying in the sky. The airplane appears to be a JAL (Japan Airlines) passenger jet, and it is flying at a relatively low altitude. The plane’s white color and its distinctive red logo are clearly visible, making it easily discernable as a JAL aircraft. Overall, the image captures a clear, beautiful scene of the airplane in flight, with a blue sky as the backdrop.] completely includes the low-level visual information in the reference description [This image has poor lighting. The blue sky has vivid colors, but the overall tone is dark. The focus is on the main subject, the aircraft. Apart from the backlighting on the wings, the details of the aircraft are clear. The composition is slightly incomplete, and the clarity of the background sky is average. Overall, the image quality is good.]. Please rate score 2 for completely or almost completely including reference information, 0 for not including at all, 1 for including part of the information or similar description. Please only provide the result in the following format: Score:

**ZH** 用户输入：#用户：请评估描述［这张图像是一幅大而清晰、细节丰富的大幅画面，一架白色飞机在天空中飞行。这架飞机似乎是一架 JAL（日本航空）客机，飞行高度相对较低。飞机白色的机身与醒目的红色标志清晰可辨，很容易被认出是 JAL 的飞机。总体而言，图像捕捉到了飞机飞行的清晰、优美场景，背景是蓝天。］是否完整涵盖了参考描述［这张图像光照较差。蓝天色彩鲜艳，但整体色调偏暗。对焦落在主体飞机上。除机翼存在逆光外，飞机的细节是清晰的。构图略显不完整，背景天空的清晰度一般。整体图像质量良好。］中的底层视觉信息。若完全或几乎完全涵盖参考信息请打 2 分，完全未涵盖打 0 分，涵盖部分信息或描述相近打 1 分。请仅按以下格式给出结果：得分：

**EN** 5-Round GPT Answers: [“Score: 1”,“Score: 1”,“Score: 1”,“Score: 1”,“Score: 1”] ⟦SLOT_21⟧ Final Score: 1.0

**ZH** 5 轮 GPT 回答：［“得分：1”、“得分：1”、“得分：1”、“得分：1”、“得分：1”］⟦SLOT_21⟧ 最终得分：1.0

**EN** (B) Preciseness.

**ZH** （B）精确性。

**EN** User Input: #User: The precision metric punishes controversial low-level descriptions that output description outputs contrast with the referencce, e.g., blur for clear, high quality for low quality, colorful for monotonous, noisy for clean, bright for dark. Evaluate whether output [The image quality is good, with a clear and well-exposed scene. The lighting appears to be natural, as the sun is shining on the scene, which adds a warm and inviting atmosphere to the image. The composition is well-balanced, with the focus on the trees and the pathway, which creates a sense of depth and perspective. The aesthetics of the image are pleasing, with the use of natural light and the greenery of the trees contributing to a visually appealing scene. The overall feeling of the image is peaceful and serene, as the viewer is invited to walk down the pathway surrounded by the trees and the cityscape in the background.] precisely reflect reference [The overall clarity of this image is very low, with serious focusing issues and significant noise. The lighting is adequate, but the colors are monotone. The main subjects are trees and distant buildings, which are extremely blurry and lack any texture details. The composition is unbalanced, and the background is very blurry. Therefore, the quality of this image is very poor.], Please rate score 2 for no controversial low-level description, 1 for less controversial low-level description than matched descrpition, and 0 for more controversial low-level description than matched description. Please only provide the result in the following format: Score:

**ZH** 用户输入：#用户：精确性指标惩罚那些与参考相矛盾的底层描述，例如把清晰说成模糊、把低质量说成高质量、把单调说成多彩、把干净说成有噪、把暗说成亮。请评估输出［这张图像质量良好，场景清晰且曝光得当。光照看起来是自然的，阳光洒在场景中，为画面增添了温暖而宜人的氛围。构图均衡，对焦落在树木与小径上，营造出纵深感与透视感。图像的美感令人愉悦，自然光的运用与树木的葱郁共同构成了赏心悦目的画面。图像整体给人的感觉是平和而宁静，观者仿佛被邀请漫步于树木环绕的小径，背景是城市景观。］是否精确反映了参考［这张图像整体清晰度很低，存在严重的对焦问题和明显噪声。光照尚可，但色彩单调。主体是树木与远处建筑，极其模糊，缺乏任何纹理细节。构图不均衡，背景非常模糊。因此，这张图像的质量非常差。］。若没有矛盾的底层描述打 2 分，矛盾的底层描述少于匹配描述打 1 分，矛盾的底层描述多于匹配描述打 0 分。请仅按以下格式给出结果：得分：

**EN** 5-Round GPT Answers: [“Score: 0”,“Score: 0”,“Score: 0”,“Score: 0”,“Score: 0”] ⟦SLOT_22⟧ Final Score: 0.0

**ZH** 5 轮 GPT 回答：［“得分：0”、“得分：0”、“得分：0”、“得分：0”、“得分：0”］⟦SLOT_22⟧ 最终得分：0.0

**EN** (C) Relevance.

**ZH** （C）相关性。

**EN** User Input: #User: Evaluate whether the description [ The image is a low-level shot of a white dog walking through a dark forest. The dog appears to be somewhat blurry, suggesting a level of motion in the picture. The photo is not very detailed, and the colors in the image might be somewhat muted due to the darkness of the forest. Overall, the picture has a somewhat mysterious and moody atmosphere.] is relevant to the low-level visual information, which may include blur, noise, exposure, artifact, color, lighting, focus, composition, etc. Please rate score 2 for completely relevant, 1 for partly relevant, and 0 for totally irrelevant. Please only provide the result in the following format: Score:

**ZH** 用户输入：#用户：请评估描述［这张图像是一张低角度拍摄的照片，一只白狗走过幽暗的森林。狗看起来有些模糊，暗示画面中存在一定的运动。照片细节不够丰富，图像中的色彩可能因森林的幽暗而略显沉闷。总体而言，画面带有几分神秘而忧郁的氛围。］是否与底层视觉信息相关，后者可能包括模糊、噪声、曝光、伪影、颜色、光照、对焦、构图等。完全相关打 2 分，部分相关打 1 分，完全不相关打 0 分。请仅按以下格式给出结果：得分：

**EN** 5-Round GPT Answers: [“Score: 2”,“Score: 1”,“Score: 1”,“Score: 2”,“Score: 1”] ⟦SLOT_23⟧ Final Score: 1.4

**ZH** 5 轮 GPT 回答：［“得分：2”、“得分：1”、“得分：1”、“得分：2”、“得分：1”］⟦SLOT_23⟧ 最终得分：1.4

**EN** Algorithm 1 Pytorch-style Pseudo Code for Softmax-based Strategy for IQA with MLLMs

**ZH** 算法 1 面向 MLLM 的基于 Softmax 的 IQA 策略的 PyTorch 风格伪代码

**EN** A.2.3 Evaluation Details for Assessment Ability

**ZH** A.2.3 评价能力评估细节

**EN** Example Pseudo Code for MLLMs on IQA:

**ZH** 面向 MLLM 的 IQA 示例伪代码：

**EN** In Algo. 1, we provide an example on how to evaluate image quality with MLLMs. The algorithm is simple with only 9 lines, and could be easily integrated with any new MLLMs (based on causal LLMs), so as to allow these models to quantitatively predict the quality of images.

**ZH** 在算法 1 中，我们给出一个如何用 MLLM 评价图像质量的示例。该算法很简单，仅 9 行代码，可轻松集成到任何新的（基于因果 LLM 的）MLLM 中，使这些模型能够定量预测图像质量。

**EN** IQA Evaluation Strategy for CLIP-ViT-Large-14:

**ZH** CLIP-ViT-Large-14 的 IQA 评估策略：

**EN** In Tab. 4, we compare the IQA performance of MLLMs with CLIP-ViT-Large-14, the visual backbone of the majority of MLLMs. Attempting to understand whether the new language part (LLM) can do better than the original language part of CLIP, we try to compare between CLIP and MLLMs in a relatively aligned setting. Firstly, noticing that most MLLMs will resize images into ⟦SLOT_24⟧ as their input sizes, we align this setting on CLIP, and ignore the strategies as proposed by (Wang et al., 2022). Secondly, same as the strategy on MLLMs, we also apply softmax pooling between good and poor, as in the CLIP’s zero-shot classification format: a photo of good quality and a photo of poor quality. Besides the two alignments, similar as existing practices (Wang et al., 2022; Wu et al., 2023b; Zhang et al., 2023c), the quality scores of CLIP-ViT-Large-14 are obtained as follows:

**ZH** 在表 4 中，我们把 MLLM 的 IQA 性能与多数 MLLM 的视觉骨干 CLIP-ViT-Large-14 做比较。为理解新增的语言部分（LLM）能否优于 CLIP 原有的语言部分，我们尝试在相对对齐的设定下比较 CLIP 与 MLLM。首先，注意到多数 MLLM 会把图像缩放至 ⟦SLOT_24⟧ 作为输入尺寸，我们在 CLIP 上对齐这一设定，并忽略（Wang 等，2022）提出的策略。其次，与 MLLM 上的策略相同，我们也在 good 与 poor 之间做 softmax 池化，采用 CLIP 的零样本分类格式：a photo of good quality（一张质量好的照片）与 a photo of poor quality（一张质量差的照片）。除这两处对齐外，与已有做法（Wang 等，2022；Wu 等，2023b；Zhang 等，2023c）类似，CLIP-ViT-Large-14 的质量分数按如下方式获得：

<!-- [原子块 · table] q pred , CLIP = e CosineSimilarity ⁡ ( f [ IMAGE ] , f a photo of good quality ) e CosineSimilarity ⁡ ( f [ IMAGE ] , f a photo of good quality ) + e CosineSimilarity ⁡ ( f [ IMAGE ] , f a photo of po -->

**EN** Special IQA Settings for Flan-T5-based InstructBLIP:

**ZH** 面向基于 Flan-T5 的 InstructBLIP 的特殊 IQA 设定：

**EN** For InstructBLIP (Dai et al., 2023) (Flan-T5-XL), different from the majority of LLaMA-based (or MPT-based Otter-v1) MLLMs, the two top-frequency tokens are high (89%) and low (8%) instead of the common good⟦SLOT_25⟧poor. Henceforth, based on our motivation to only modify the argmax into softmax and follow the default top-frequency output tokens of MLLMs, we replace the probabilities of good⟦SLOT_26⟧poor into those of high⟦SLOT_27⟧low in Eq. 1 for T5, defined as follows:

**ZH** 对于 InstructBLIP（Dai 等，2023）（Flan-T5-XL），与多数基于 LLaMA（或基于 MPT 的 Otter-v1）的 MLLM 不同，其两个最高频词元是 high（89%）与 low（8%），而非常见的 good⟦SLOT_25⟧poor。因此，基于我们只把 argmax 改为 softmax、并沿用 MLLM 默认最高频输出词元的出发点，我们在式 1 中把 good⟦SLOT_26⟧poor 的概率替换为 high⟦SLOT_27⟧low 的概率（针对 T5），定义如下：

<!-- [原子块 · table] q pred , T5 = e x SCORE_TOKEN high e x SCORE_TOKEN high + e x SCORE_TOKEN low q_{\mathrm{pred,T5}}=\frac{e^{x^{\text{{high}}}_{\textit{SCORE\_TOKEN}}}}{e^{x^{\text{{high}}}_{\textit{SCORE\_TOKEN}}}+e^ -->

**EN** As validated in our experiments (Tab. 10, the high⟦SLOT_28⟧low pair generally predicts better than good⟦SLOT_29⟧poor on majority of databases. The better performance on MLLM-specific top-frequency tokens by side validates the effectiveness of our methodology for MLLMs on IQA.

**ZH** 如我们的实验（表 10）所验证，high⟦SLOT_28⟧low 词对在多数数据库上普遍优于 good⟦SLOT_29⟧poor。MLLM 特有的最高频词元表现更好，从侧面验证了本文方法在 MLLM 上做 IQA 的有效性。

**EN** Further Improving IQA Abilities of MLLMs with Synonym Ensemble:

**ZH** 用同义词集成进一步提升 MLLM 的 IQA 能力：

**EN** The quality assessment scores for the synonym ensemble strategy can be derived as:

**ZH** 同义词集成策略的质量评价分数可按如下方式得到：

<!-- [原子块 · table] q pred = e ∑ t t ∈ 𝒫 x SCORE_TOKEN t e ∑ t t ∈ 𝒫 x SCORE_TOKEN t + e ∑ t t ∈ 𝒩 x SCORE_TOKEN t q_{\mathrm{pred}}=\frac{e^{\sum_{t}^{t\in\mathcal{P}}x^{t}_{\textit{SCORE\_TOKEN}}}}{e^{\sum_{t}^{t\in\ma -->

**EN** where ⟦SLOT_30⟧ indicates the positive token set (from good, fine, high, etc.), while ⟦SLOT_31⟧ represents the negative token set (from poor, bad, low, etc.). The results of different ⟦SLOT_32⟧ and ⟦SLOT_33⟧ are listed in Tab. 11.

**ZH** 其中 ⟦SLOT_30⟧ 表示正向词元集合（取自 good、fine、high 等），⟦SLOT_31⟧ 表示负向词元集合（取自 poor、bad、low 等）。不同 ⟦SLOT_32⟧ 与 ⟦SLOT_33⟧ 的结果列于表 11。

**EN** Special Validation Protocol for CGIQA-6K:

**ZH** CGIQA-6K 的特殊验证协议：

<!-- [原子块 · object]  -->

**EN** Figure 9: Radar chart for the Perception ability, where the performance of all MLLMs is presented by subtracting the accuracy of random guess. See Tab. 7 for the respective numerical results.

**ZH** 图 9：感知能力的雷达图，其中所有 MLLM 的表现均以减去随机猜测准确率后的方式呈现。相应数值结果见表 7。

**EN** Table 6: A brief view of 15 open-source MLLMs evaluated in the Q-Bench in chronological order.

**ZH** 表 6：Q-Bench 中按时间顺序排列的 15 个参评开源 MLLM 概览。

<!-- [原子块 · table] Month of Release {}^{\textit{Month of Release}} Model Names Vision Architectures (V) V → \to L Language Architectures (L) Backbone #Size Alignment Backbone Type Oct. {}^{\textit{Oct.}} LLaVA-v1.5 ( Vi -->

**EN** The CGIQA-6K (Zhang et al., 2023b) dataset contains two separate sub-sets which consist of 3,000 game images and 3,000 movie images respectively, with different instructions for human annotators during its subjective experiments. Therefore, we validate the MLLMs’ assessment performance on the two sub-sets individually and average the results for the final exhibition. The results of NIQE and CLIP-ViT-Large-14 are also obtained under the same protocol for a fair comparison.

**ZH** CGIQA-6K（Zhang 等，2023b）数据集包含两个独立的子集，分别由 3,000 张游戏图像与 3,000 张电影图像组成，其主观实验中对人类标注者使用了不同的指令。因此，我们分别验证 MLLM 在这两个子集上的评价性能，并对结果取平均作为最终展示。NIQE 与 CLIP-ViT-Large-14 的结果也在同一协议下获得，以保证比较公平。

**EN** A.3 Extended Experimental Results

**ZH** A.3 扩展实验结果

**EN** A.3.1 Architectures of Different MLLMs

**ZH** A.3.1 不同 MLLM 的架构

**EN** As compared in Tab. 6, the 15 variants of MLLMs as evaluated in the Q-Bench are with varying vision and language architectures, as well as the alignment strategies between the two modalities. It can be noticed that all MLLMs are combined with a version of CLIP Radford et al. (2021) and a large language model, which are generally connected under one among three strategies: direct project layers (MLP or linear layer), Q-Former (a transformer to abstract visual features into LLM tokens), or cross-attention (use visual features as conditions for text generation).

**ZH** 如表 6 所比较，Q-Bench 中评估的 15 个 MLLM 变体具有不同的视觉与语言架构，以及两模态之间不同的对齐策略。可以看到，所有 MLLM 都由某个版本的 CLIP（Radford 等，2021）与一个大语言模型组合而成，二者一般通过三种策略之一连接：直接投影层（MLP 或线性层）、Q-Former（把视觉特征抽象为 LLM 词元的 Transformer），或交叉注意力（把视觉特征作为文本生成的条件）。

**EN** Table 7: Results on the dev subset for the low-level Perception ability of MLLMs. MLLMs with top-3 performance in each sub-category and the overall LLVisionQA is emphasized with boldface.

**ZH** 表 7：MLLM 底层感知能力在开发子集上的结果。各子类别与 LLVisionQA 整体上表现前三的 MLLM 以粗体标出。

<!-- [原子块 · table] Sub-categories Question Types Quadrants of Low-level Concerns Overall ↑ \uparrow Model (variant) Yes-or-No ↑ \uparrow What ↑ \uparrow How ↑ \uparrow Distortion ↑ \uparrow Other ↑ \uparrow In-context I -->

**EN** A.3.2 Extended Results for Perception

**ZH** A.3.2 感知的扩展结果

**EN** Results on the dev subset:

**ZH** 开发子集上的结果：

**EN** In Tab. 7, we list the results on the dev subset of the LLVisionQA benchmark set for the low-level perception task. This subset is planned to be opened to public in the future. Therefore, the performance in it will only be taken as a reference. At present, all MLLMs as evaluated have not yet seen this subset, so it can be taken as a cross-validation with the test subset. From Tab. 7 and Tab. 2, we validate that MLLMs perform pretty similar between the two subsets, suggesting that LLVisionQA is a reliable and stable benchmark set for question answering on low-level vision.

**ZH** 在表 7 中，我们列出 LLVisionQA 基准集开发子集上底层感知任务的结果。该子集计划在未来公开，因此其中的性能仅作参考。目前所有参评 MLLM 都尚未见过该子集，故可将其视为与测试子集的交叉验证。从表 7 与表 2 可以验证，MLLM 在两个子集上的表现相当接近，说明 LLVisionQA 是一个可靠、稳定的底层视觉问答基准集。

**EN** Radar Chart for Different MLLMs:

**ZH** 不同 MLLM 的雷达图：

**EN** In Fig. 9, we show the radar chart to compare the low-level perception abiliies among different MLLMs. Despite the observations as revealed in Sec. 3.1, we also notice two extra fun facts: 1) Adding the content context does not degrade the performance of MLLMs. On the contrary, MLLMs can answer better on in-context questions. This result validates the aforementioned conjectures that appropriate higher-level contexts as prompts may help improve the preciseness of low-level visual perception; 2) MLLMs have strong capabilities of answering what questions, suggesting potential reasoning abilities. In the future, we will excavate more interesting characteristics of MLLMs and try to improve their perception accuracy through better guidance based on these characteristics.

**ZH** 在图 9 中，我们给出雷达图以比较不同 MLLM 的底层感知能力。除 3.1 节揭示的观察外，我们还注意到两个有趣的现象：1）加入内容上下文并不会降低 MLLM 的表现；相反，MLLM 在上下文问题上答得更好。这一结果验证了前述猜想，即适当的更高层上下文作为提示可能有助于提升底层视觉感知的精确性；2）MLLM 回答 What 型问题的能力很强，显示出潜在的推理能力。未来我们将挖掘 MLLM 更多有趣特性，并尝试基于这些特性通过更好的引导来提升其感知准确率。

**EN** Table 8: Judgment accuracies of MLLMs on questions with correct answers as Yes or No.

**ZH** 表 8：MLLM 在正确答案为“是”或“否”的问题上的判断准确率。

<!-- [原子块 · table] Model (variant) all correct answer: Yes correct answer: No mean de-biased # ↓ \downarrow random guess 50.00% 50.00% 50.00% 50.00% - Shikra ( Vicuna-7B ) 66.91% 71.79% 60.00% 65.90% 3 LLaVA-v1 ( Vicuna -->

**EN** “Yes or No?”: How Biased are MLLMs?

**ZH** “是或否？”：MLLM 的偏差有多大？

**EN** In this section, we take a deeper analysis on the Yes-or-No judgment ability of MLLMs, that whether these models can get similar accuracy on questions that should be answered with Yes, as those should be replied as No. Sadly, we notice that all MLLMs have higher prediction accuracy on Yes-questions than No-questions, while some MLLMs are more very severe biased (e.g., IDEFICS-Instruct). Considering that our LLVisionQA dataset contains more (62%) Yes-questions than No-questions (38%) and may introduce biases while comparing different MLLMs, we further compute a de-biased accuracy for all these methods, as the mean value of the accuracies on two types of questions, and present the respective de-biased rank for all participating MLLMs, as listed in Tab 8. We hope this study on the biases and the de-biased results can provide a fairer comparison among them, as well as bring insights on the future improvements of MLLMs for low-level perception.

**ZH** 本节更深入地分析 MLLM 的是非判断能力，即这些模型在应回答“是”的问题上能否取得与应回答“否”的问题相近的准确率。遗憾的是，我们注意到所有 MLLM 在“是”类问题上的预测准确率都高于“否”类问题，其中部分 MLLM（如 IDEFICS-Instruct）的偏差尤为严重。考虑到我们的 LLVisionQA 数据集中“是”类问题（62%）多于“否”类问题（38%），在比较不同 MLLM 时可能引入偏差，我们进一步为所有这些方法计算去偏准确率——即两类问题准确率的均值——并给出各参评 MLLM 的去偏排名，如表 8 所示。我们希望这项关于偏差与去偏结果的研究能为它们提供更公平的比较，也为 MLLM 在底层感知上的未来改进带来启示。

**EN** Qualitative examples of MLLM responses:

**ZH** MLLM 回答的定性示例：

**EN** In Fig. 10, we show qualitative examples of MLLM responses on questions in the LLVisionQA dataset, that MLLMs are still unstable on basic low-level attributes such as blurs (Fig. 10(a)), and may fail on in-context questions that are easy to human (Fig. 10(b)). These unsatisfactory results suggest that we still need to improve the basic low-level perception ability of these models.

**ZH** 在图 10 中，我们给出 MLLM 对 LLVisionQA 数据集中问题的回答定性示例：MLLM 在模糊等基础底层属性上仍不稳定（图 10（a）），并且可能在人类看来很容易的上下文问题上失败（图 10（b））。这些不尽如人意的结果说明，我们仍需提升这些模型的基础底层感知能力。

<!-- [原子块 · img]  -->

**EN** Figure 10: Qualitative comparison for MLLM perception responses.

**ZH** 图 10：MLLM 感知回答的定性比较。

**EN** A.3.3 Extended Results for Description

**ZH** A.3.3 描述的扩展结果

**EN** Bar Chart for Different MLLMs:

**ZH** 不同 MLLM 的柱状图：

**EN** In Fig. 11, we show the bar chart to visualize MLLM capabilities on the three dimensions of low-level visual description. From the figure, we notice that current MLLMs still struggle on describing complete and accurate low-level information. As the relevance scores are generally higher (showing that most MLLMs can follow this abstract instruction well), the results suggest that the main bottleneck of MLLMs on enhancing their description ability is still the perception on low-level attributes.

**ZH** 在图 11 中，我们用柱状图可视化 MLLM 在底层视觉描述三个维度上的能力。从图中可以看到，当前 MLLM 在描述完整、准确的底层信息上仍然吃力。由于相关性分数普遍较高（说明多数 MLLM 能很好地遵循这一抽象指令），结果表明 MLLM 提升描述能力的主要瓶颈仍在于对底层属性的感知。

<!-- [原子块 · object]  -->

**EN** Figure 11: Bar chart for the Description ability, with scores in all dimensions normalized into ⟦SLOT_34⟧.

**ZH** 图 11：描述能力的柱状图，各维度分数被归一化到 ⟦SLOT_34⟧。

<!-- [原子块 · img]  -->

**EN** Figure 12: A qualitative comparison for MLLM descriptions on an AI-generated image.

**ZH** 图 12：在一张人工智能生成图像上 MLLM 描述的定性比较。

<!-- [原子块 · img]  -->

**EN** Figure 13: A qualitative comparison for MLLM descriptions on an in-the-wild photograph.

**ZH** 图 13：在一张真实实拍照片上 MLLM 描述的定性比较。

**EN** A Qualitative Comparison on the Descriptions:

**ZH** 描述上的定性比较：

**EN** In Fig. 12 and Fig 12 we qualitatively compare among different MLLM low-level descriptions on an AI-generated image and a natural photograph. While most MLLMs can precisely describe their contents (which are actually not instructed in our user prompt), different MLLMs may have several divergences on their quality and related low-level attributes, especially on the AI-generated image. Some MLLMs describe it as clear, colorful, or aesthetically pleasing, which are typically incorrect; on the contrary, some correct descriptions are also seen, such as colors are subdued, not as clear as it could be, or not very detailed. This qualitative study validates our quantitative conclusion that current MLLMs general cannot provide noise-free low-level visual descriptions of images in a stable manner. Moreover, we notice that even given the same prompt, different MLLMs tend to describe the image with diverse output styles and lengths, while the longer descriptions usually come with a larger percentage of descriptions on irrelevant information.

**ZH** 在图 12 与图 13 中，我们对不同 MLLM 在一张人工智能生成图像与一张自然照片上的底层描述做定性比较。尽管多数 MLLM 能准确描述其内容（这实际上并非我们用户提示所要求的），不同 MLLM 在质量及相关底层属性上可能存在若干分歧，在人工智能生成图像上尤甚。部分 MLLM 将其描述为清晰、色彩丰富或美感愉悦，这通常是不正确的；相反，也有一些正确描述，例如色彩偏柔和、不如其本应达到的清晰、或细节不够丰富。这项定性研究验证了我们的定量结论：当前 MLLM 一般无法稳定地给出无噪声的图像底层视觉描述。此外我们注意到，即便给定相同提示，不同 MLLM 也倾向于以不同的输出风格与长度描述图像，而更长的描述往往伴随更高比例的无信息量内容。

**EN** A.3.4 Extended Results for Assessment

**ZH** A.3.4 评价的扩展结果

**EN** Radar Chart for Different MLLMs:

**ZH** 不同 MLLM 的雷达图：

**EN** Table 9: Effectiveness of the proposed softmax probability-based strategy against the baseline argmax strategy, on multiple MLLMs and different IQA datasets. Metrics are SRCC/PLCC.

**ZH** 表 9：所提出的基于 softmax 概率的策略相对基线 argmax 策略，在多个 MLLM 与不同 IQA 数据集上的有效性。指标为 SRCC/PLCC。

<!-- [原子块 · table] Dataset Type In-the-wild Generated Artificial Model / Dataset Strategy KONiQ-10k SPAQ LIVE-FB LIVE-itw AGIQA-3K KADID-10K Shikra ( Vicuna-7B ) argmax 0.178/0.201 0.277/0.281 0.152/0.169 0.248/0.267 0. -->

**EN** In Fig. 14, we visualize the IQA performance of different MLLMs on seven IQA datasets. The visualization proves that MLLMs can notably positively correlate with human ratings, and could very highly align with human perception on relatively coarse situations (AGIQA-3K, SPAQ). As such results are obtained via no direct alignment with human perception and from the simplest prompts (“Rate the quality of the image.”), they suggest the exciting underlying abilities of general intelligence to naturally understand “quality” via their vast training data. However, the performance are still yet to be accurate on finer-grained situations, such as LIVE-FB, which is constructed by more than 95% high-quality images (i.e. quality score ⟦SLOT_35⟧ 50/100), or CGIQA-6K, made up entirely by relatively high-quality images collected from video games or movies. This suggests that MLLMs still need to improve the measurability on their predictions through well-designed fine-tuning.

**ZH** 在图 14 中，我们可视化不同 MLLM 在七个 IQA 数据集上的 IQA 表现。该可视化证明 MLLM 能与人类评分显著正相关，并且在相对粗粒度的场景（AGIQA-3K、SPAQ）上能与人类感知高度契合。由于这些结果是在未与人类感知做直接对齐、且使用最简单提示（“评价这张图像的质量。”）的情况下获得的，它们显示出通用智能通过其海量训练数据自然理解“质量”的令人振奋的潜在能力。然而，在更细粒度的场景下表现仍不够准确，例如 LIVE-FB——其 95% 以上为高质量图像（即质量分数 ⟦SLOT_35⟧ 50/100），或 CGIQA-6K——其图像全部来自电子游戏或电影，质量相对较高。这说明 MLLM 仍需通过精心设计的微调来提升其预测的可度量性。

<!-- [原子块 · object]  -->

**EN** Figure 14: Radar chart for the Assessment ability, where the performance of all MLLMs is presented by an average of SRCC/PLCC metrics. See Tab. 4 for the respective numerical results.

**ZH** 图 14：评价能力的雷达图，其中所有 MLLM 的表现以 SRCC/PLCC 指标的平均值呈现。相应数值结果见表 4。

**EN** A Deep Dive Into the Probabilities:

**ZH** 深入考察概率：

**EN** (A) Softmax vs Argmax:

**ZH** （A）Softmax 与 Argmax 之别：

**EN** In the first part of the deep dive, we quantitatively evaluate the correlation with human perception on a simple argmax strategy between good⟦SLOT_36⟧bad and our proposed softmax strategy. In Tab. 9, we confirm that for all MLLMs on all IQA datasets, the more measurable softmax strategy predicts better than the argmax strategy, which degenerates into only two scores, 0 and 1. Though the result is generally expected, the experiments validate that MLLMs have quantitative assessment ability hidden behind their word outputs, and prove the effectiveness of our softmax-based IQA strategy.

**ZH** 在深入考察的第一部分，我们定量评估 good⟦SLOT_36⟧bad 之间简单 argmax 策略与本文所提 softmax 策略与人类感知的相关性。在表 9 中我们确认，对所有 MLLM 在所有 IQA 数据集上，可度量性更强的 softmax 策略都优于退化为 0 与 1 两个分数的 argmax 策略。尽管这一结果大体在意料之中，实验仍验证了 MLLM 的词语输出背后隐藏着定量评价能力，并证明了我们基于 softmax 的 IQA 策略的有效性。

**EN** (B) [For T5-based InstructBLIP] high⟦SLOT_37⟧low vs good⟦SLOT_38⟧poor:

**ZH** （B）［针对基于 T5 的 InstructBLIP］high⟦SLOT_37⟧low 与 good⟦SLOT_38⟧poor 之别：

**EN** We further conduct a special study for InstructBLIP (Flan-T5-XL). With a different LLM as language backbone, even pre-trained with the same settings, the T5-version of InstructBLIP tends to predict more high⟦SLOT_39⟧low than good⟦SLOT_40⟧poor, different from its Vicuna-7B-based counterpart. The experimental results in Tab 10 validate that the more probable high⟦SLOT_41⟧low tokens are more competitive in IQA than good⟦SLOT_42⟧bad tokens, suggesting that top-frequency tokens are more quality-distinctive.

**ZH** 我们进一步对 InstructBLIP（Flan-T5-XL）做了专项研究。由于语言骨干不同，即便采用相同设定预训练，T5 版本的 InstructBLIP 也倾向于更多预测 high⟦SLOT_39⟧low 而非 good⟦SLOT_40⟧poor，这与基于 Vicuna-7B 的对应模型不同。表 10 中的实验结果验证，概率更高的 high⟦SLOT_41⟧low 词元在 IQA 中比 good⟦SLOT_42⟧bad 词元更有竞争力，说明最高频词元具有更强的质量区分度。

**EN** A.3.5 Synonym Ensemble: Further Improving IQA ability (A3) for MLLMs

**ZH** A.3.5 同义词集成：进一步提升 MLLM 的评价能力（A3）

**EN** Table 10: Comparison between high⟦SLOT_43⟧low and good⟦SLOT_44⟧poor on InstructBLIP (Flan-T5-XL).

**ZH** 表 10：InstructBLIP（Flan-T5-XL）上 high⟦SLOT_43⟧low 与 good⟦SLOT_44⟧poor 的对比。

<!-- [原子块 · table] Dataset Type In-the-wild Generated Artificial Model / Dataset tokens KONiQ-10k SPAQ LIVE-FB LIVE-itw AGIQA-3K KADID-10K InstructBLIP (Flan-T5-XL) good ↔ \leftrightarrow poor 0.288/0.289 0.581/ 0.618 0 -->

**EN** As shown in Table 11, the synonym ensemble strategy (as proposed in Eq. 4) on top-5 methods (i.e. InternLM-XComposer-VL, QWen-VL, LLaVA-v1.5 (13B), mPLUG-Owl, and LLaVA-v1.5 (7B)) can in average lead to up to 2% accuracy improvement (in average 1.3%). We believe it is a useful boost to improve the performance of MLLMs on IQA task.

**ZH** 如表 11 所示，在排名前五的方法（即 InternLM-XComposer-VL、QWen-VL、LLaVA-v1.5（13B）、mPLUG-Owl 与 LLaVA-v1.5（7B））上应用同义词集成策略（如式 4 所提出），平均可带来最高 2% 的准确率提升（平均 1.3%）。我们认为这是提升 MLLM 在 IQA 任务上表现的有益助推。

**EN** Nevertheless, we also notice that different MLLMs perform best with different specific prompt combos. For example, the good+fine⟦SLOT_45⟧poor+bad performs best on InternLM-XComposer-VL, but comes with reduced accuracy on QWen-VL compared with only good⟦SLOT_46⟧poor. While good⟦SLOT_47⟧poor is proved overall best single word pair for the evaluation and shows stable results across MLLMs, we decide to keep the current strategy in Q-Bench to evaluate MLLMs.

**ZH** 然而我们也注意到，不同 MLLM 在特定的提示组合下表现最佳的搭配各有不同。例如，good+fine⟦SLOT_45⟧poor+bad 在 InternLM-XComposer-VL 上表现最好，但在 QWen-VL 上相比仅用 good⟦SLOT_46⟧poor 反而准确率下降。鉴于 good⟦SLOT_47⟧poor 被证明是整体上最佳的单组词对，且在各 MLLM 上表现稳定，我们决定在 Q-Bench 中保留当前策略来评估 MLLM。

**EN** Table 11: Evaluation results on the synonym ensemble strategy for the (A3) Assessment ability on MLLMs with top-5 results in the default A3 leaderboard of the Q-Bench. After ensemble, the rankings among them are not changed. Metrics are SRCC/PLCC.

**ZH** 表 11：在 Q-Bench 默认 A3 排行榜前五的 MLLM 上，同义词集成策略对（A3）评价能力的评估结果。集成后它们之间的排名未发生变化。指标为 SRCC/PLCC。

<!-- [原子块 · table] Dataset Type In-the-wild Generated Artificial Average Prompt / Dataset KONiQ-10k SPAQ LIVE-FB LIVE-itw CGIQA-6K AGIQA-3K KADID-10K LLaVA-v1.5 ( Vicuna-v1.5-13B ) good ↔ \leftrightarrow poor 0.448/0.46 -->

**EN** Appendix B Statement on Data Contamination

**ZH** 附录 B 关于数据污染的声明

**EN** The Q-bench contains three tasks, where the first two tasks, (A1) perception and (A2) description, are evaluated with our own datasets proposed with the paper. For these two tasks, the questions, answers, or low-level descriptions in the two datasets are not seen by any existing MLLMs. Half of LLVisionQA (i.e. the test subset) and full of LLDescribe labels are kept private, to avoid being added to the training sets of any MLLMs. We hope that this measure will allow Q-Bench to have long-term significance as an indicator of low-level visual abilities.

**ZH** Q-Bench 包含三个任务，其中前两个任务（A1）感知与（A2）描述使用本文提出的数据集进行评估。对于这两个任务，两个数据集中的问题、答案或底层描述均未被任何现有 MLLM 见过。LLVisionQA 的一半（即测试子集）与 LLDescribe 的全部标注保持私有，以避免被加入任何 MLLM 的训练集。我们希望这一措施能让 Q-Bench 作为底层视觉能力的指示器具有长期意义。

**EN** For the third task, (A3) assessment, the situation is a bit more complicated. For open-source models as tested, almost all of them have provided their technical reports, and as far as we know, no image quality assessment (IQA) dataset has participated in the multi-modality training stages of them. While text knowledge about image quality assessment should have been injected to them (e.g. a blurry image is a low quality image) during their pure-language training stages, we think this should not be regarded as data contamination for IQA, because the images cannot be seen by a language model. Instead, they are important knowledge for MLLMs to better link particular visual attributes (blur) to human opinions (quality), which motivates us to explore MLLMs for these tasks.

**ZH** 对于第三个任务（A3）评价，情况稍复杂。就所测试的开源模型而言，它们几乎都提供了技术报告，而据我们所知，没有任何图像质量评价（IQA）数据集参与过它们的多模态训练阶段。尽管在纯语言训练阶段，关于图像质量评价的文本知识应当已被注入这些模型（例如模糊图像即低质量图像），我们认为这不应被视为 IQA 的数据污染，因为语言模型无法看到图像。相反，这些知识对 MLLM 更好地把特定视觉属性（模糊）与人类意见（质量）联系起来十分重要，这也正是我们探索用 MLLM 完成这些任务的动机。

**EN** Appendix C Limitations and Discussions

**ZH** 附录 C 局限与讨论

**EN** In Section A.3.2, we observed that MLLMs frequently respond with ‘yes’ to Yes-or-No questions. It’s worth noting that the current LLVisionQA dataset is skewed, with 62% of its questions being Yes-questions and only 38% being No-questions. This imbalance could introduce biases when comparing various MLLMs. To fully address this, we aim to balance the dataset by preparing a reversed version for each question in our subsequent work, ensuring a less biased evaluation.

**ZH** 在 A.3.2 节中，我们观察到 MLLM 对是非型问题频繁回答“是”。值得注意的是，当前的 LLVisionQA 数据集存在偏斜：62% 的问题为“是”类，仅 38% 为“否”类。这种不平衡在比较不同 MLLM 时可能引入偏差。为彻底解决该问题，我们计划在后续工作中为每个问题准备一个反转版本，使数据集趋于平衡，从而实现偏差更小的评估。

**EN** For the description task, we acknowledge that judging whether a description matches the gold description is a subjective process, which may not have an absolute standard. Even when evaluated by humans, the scores rated for the MLLM descriptions are subject to individual differences. Though we have employed the 5-round GPT-assisted evaluation protocol, which could be the most reliable and reproducible way at present, it may still unavoidably contain hallucinations (from GPT). We will continue to explore how to design a more reliable evaluation protocol for the low-level visual description task in our follow-up works.

**ZH** 对于描述任务，我们承认判断一条描述是否与黄金描述相符是一个主观过程，未必存在绝对标准。即便由人类评估，对 MLLM 描述所打的分数也会因个体差异而不同。尽管我们采用了 5 轮 GPT 辅助评估协议——这在当下可能是最可靠、可复现的方式——它仍可能不可避免地包含（来自 GPT 的）幻觉。我们将在后续工作中继续探索如何为底层视觉描述任务设计更可靠的评估协议。

**EN** While the proposed Q-Bench has offered a comprehensive evaluation on the low-level visual capabilities of MLLMs, it does not provide direct guidance on enhancing these capabilities. As our next steps, we intend to progressively scale up the LLDescribe and LLVisionQA datasets to eventually allow a reliable low-level visual instruction tuning process that can further improve the low-level abilities for MLLMs.

**ZH** 尽管所提出的 Q-Bench 对 MLLM 的底层视觉能力做了全面评估，它并未就如何增强这些能力提供直接指引。作为下一步，我们打算逐步扩大 LLDescribe 与 LLVisionQA 数据集的规模，最终支撑起可靠的底层视觉指令微调流程，从而进一步提升 MLLM 的底层能力。
