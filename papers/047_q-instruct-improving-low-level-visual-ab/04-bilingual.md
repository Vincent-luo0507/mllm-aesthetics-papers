# Q-Instruct：提升多模态基座模型的底层视觉能力

> 原标题：Q-Instruct: Improving Low-level Visual Abilities for Multi-modality Foundation Models
> 作者：Haoning Wu, Zicheng Zhang, Erli Zhang, Chaofeng Chen, Liang Liao, Annan Wang, Kaixin Xu, Chunyi Li, Jingwen Hou, Guangtao Zhai, Geng Xue, Wenxiu Sun 等 · arXiv:2311.06783 · 2023-11-12

<!-- [原子块 · verbatim] Q-Instruct: Improving Low-level Visual Abilities for Multi-modality Foundation Models -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] Multi-modality large language models (MLLMs), as represented by GPT-4V, have introduced a paradigm shift for visual perception and understanding tasks, that a variety of abilities can be achieved with -->

<!-- [原子块 · img]  -->

**EN** Figure 1: Abilities of Q-Instruct-tuned LLaVA-v1.5-7B [29] on various low-level visual tasks, in comparison with the baseline version.

**ZH** 图 1：经 Q-Instruct 微调的 LLaVA-v1.5-7B [29] 与基线版本在各项底层视觉任务上的能力对比。

**EN** 1 Introduction

**ZH** 1 引言

<!-- [原子块 · img]  -->

**EN** Figure 2: Data construction pipeline. First, we collect 58K human feedbacks on low-level visual aspects (the Q-pathway, a/b); they are then converted into with 200K instruction-response pairs (the Q-Instruct, c), which are used for (d) low-level visual instruction tuning.

**ZH** 图 2：数据构建流水线。首先收集 58K 条关于底层视觉属性的人类反馈（Q-Pathway，a/b）；随后将其转换为 200K 条指令—响应对（Q-Instruct，c），用于（d）底层视觉指令微调。

**EN** Computer vision has witnessed a recent paradigm shift attributed to the emergence of multi-modality large language models (MLLMs) [37, 30, 7, 11]. These models aim to transcend traditional task-specific experts, and serve as general-purpose foundation models capable of facilitating humans across a variety of visual tasks [25]. Specifically, these foundation models also bring exciting potentials in the domain of low-level visual perception and understanding. This domain includes not only commonly-focused image quality assessment (IQA) [14, 60, 55] tasks, but also finer-grained abilities to identify the low-level visual attributes (noise, blur, etc) [43], or evaluate the low-level visual dimensions (clarity, brightness, etc) [9, 56]. As human cognition associated with these tasks is highly interconnected, we aspire for a unified foundation model to establish general abilities across these tasks, which could robustly respond to open-ended human queries on low-level visual aspects.

**ZH** 计算机视觉近来经历了一次范式转变，其动因是多模态大语言模型（MLLM）[37, 30, 7, 11] 的涌现。这类模型力图超越传统的任务专用专家模型，成为通用基座模型，能够在多种视觉任务上为人类提供便利 [25]。具体地，这些基座模型在底层视觉感知与理解领域同样带来令人振奋的潜力。该领域不仅包含常受关注的图像质量评价（IQA）[14, 60, 55] 任务，还包括识别底层视觉属性（噪声、模糊等）[43] 或评估底层视觉维度（清晰度、亮度等）[9, 56] 等更细粒度的能力。由于人类在这些任务上的认知高度关联，我们期望有一个统一的基座模型来建立跨任务的通用能力，从而稳健地回应人类关于底层视觉方面的开放式提问。

**EN** Nevertheless, though existing MLLMs can basically reply to human queries regarding low-level visual aspects, the accuracy of their responses remains unsatisfactory [31, 57] (Fig. 1(a)). The primary problem is the lack of low-level visual datasets during training MLLMs, where publicly available datasets generally only focus on high-level visual abilities [32, 2, 16, 22]. To solve this problem, we construct the Q-Instruct, the first large-scale low-level visual instruction tuning dataset, in the following two steps:

**ZH** 然而，尽管现有 MLLM 基本能够回答人类关于底层视觉方面的问题，其回答的准确性仍不尽如人意 [31, 57]（图 1(a)）。主要问题在于训练 MLLM 时缺少底层视觉数据集——公开可得的数据集通常只关注高层视觉能力 [32, 2, 16, 22]。为解决该问题，我们分两步构建了 Q-Instruct——首个大规模底层视觉指令微调数据集：

**EN** Step 1: Collect human feedbacks for low-level vision.

**ZH** 步骤 1：收集面向底层视觉的人类反馈。

**EN** For this step, we invite human subjects to provide direct feedbacks on their low-level perception and understanding over a variety of images (Fig. 2(b)). Specifically, each feedback should include two parts: 1) Primarily, an exhaustive description on elemental low-level attributes (e.g. blurs, noises, clarity, color, brightness). Such descriptions should also include content [27, 49] or position [52, 60] contexts (e.g. the duck / the left part of the image is under-exposed) that are related to low-level attributes. 2) Then, an overall conclusion on the image quality based on the description of the attributes. With the two parts, the feedbacks, denoted as pathway feedbacks, not only record fundamental human low-level perception but also reflect the human reasoning process on evaluating visual quality. The hence-constructed Q-Pathway dataset (Fig 2(b)) contains 58K pathway feedbacks on 18,973 multi-sourced images, each image with at least three feedbacks (avg. 46.4 words per feedback).

**ZH** 在这一步中，我们邀请受试者对大量图像的底层感知与理解给出直接反馈（图 2(b)）。具体地，每条反馈应包含两部分：1）首先是对基本底层属性（如模糊、噪声、清晰度、色彩、亮度）的详尽描述；该描述还应包含与底层属性相关的内容 [27, 49] 或位置 [52, 60] 上下文（例如这只鸭子／图像左侧欠曝）。2）其次是基于属性描述得出的图像质量总体结论。具备这两部分的反馈（记作 pathway 反馈）既记录了人类最基本的底层感知，也反映了人类评估视觉质量时的推理过程。由此构建的 Q-Pathway 数据集（图 2(b)）包含 18,973 张多源图像上的 58K 条 pathway 反馈，每张图像至少三条反馈（每条反馈平均 46.4 词）。

**EN** Step 2: Convert these feedbacks for instruction tuning.

**ZH** 步骤 2：把这些反馈转换为指令微调数据。

**EN** While these pathway feedbacks themselves make up an important subset for the low-level visual instruction tuning, the full instruction tuning dataset should be designed to activate more capabilities. Primarily, it should also include a low-level visual question answering (VQA) subset. To generate a reliable VQA subset, we refer to the setting that how COCO-VQA [2] is derived from image captions, and employ GPT [36] to convert the pathway feedbacks into question-answer pairs with adjectives (e.g. good/fair/poor) or nouns (e.g. noise/motion blur) as answers. Similarly, we also collect a balanced yes-or-no question-answer set based on the information in the feedbacks (answered with yes), or information contrast to the feedbacks (answered with no); some context-related question-answer pairs are also created to better ground [62] the low-level attributes. Following existing studies [40], all question-answer pairs in the VQA subset include both multiple-choice (A/B/C/D) and direct-answer settings. Furthermore, besides the VQA subset, with the assistance of GPT, we also collect a subset of long conversations related to the low-level concerns (e.g. why the distortions happen, how to improve the picture quality). The subsets compose into the Q-Instruct dataset (Fig. 2(c)) with 200K instruction-response pairs, which is designed to enhance MLLMs on a variety of low-level visual abilities.

**ZH** 虽然这些 pathway 反馈本身构成了底层视觉指令微调的一个重要子集，完整的指令微调数据集还应被设计为激活更多能力。首要的是，它还应包含一个底层视觉问答（VQA）子集。为生成可靠的 VQA 子集，我们参照 COCO-VQA [2] 由图像描述派生而来的设定，用 GPT [36] 把 pathway 反馈转换为问答对，答案以形容词（如 good/fair/poor）或名词（如 noise/motion blur）给出。类似地，我们还基于反馈中的信息（答案为 yes）或与反馈相反的信息（答案为 no）收集了一个均衡的是非问答集；此外也构造了一些与上下文相关的问答对，以更好地为底层属性提供落点 [62]。沿用既有研究 [40]，VQA 子集中所有问答对都同时涵盖多选（A/B/C/D）与直接作答两种设定。进一步地，除 VQA 子集外，我们还在 GPT 的协助下收集了一个与底层关切相关的长对话子集（例如失真为何发生、如何提升画面质量）。这些子集共同构成 Q-Instruct 数据集（图 2(c)），含 200K 条指令—响应对，旨在增强 MLLM 在多种底层视觉任务上的能力。

**EN** The core contributions of our study can be summarized as follows: 1) We collect the Q-Pathway, a multi-modality dataset for low-level visual perception and quality assessment, which includes direct human feedbacks (with reasoning) on low-level visual aspects. 2) Based on Q-Pathway, we construct the Q-Instruct, the first instruction tuning dataset that focuses on human queries related to low-level vision. 3) Our rich experiments on low-level visual instruction tuning ((Fig. 2 (d)) validate that the Q-Instruct improve various low-level abilities of MLLMs (Fig. 1), and bring insights for future studies to inject various low-level visual abilities into the scope of general foundation models.

**ZH** 本研究的核心贡献可概括如下：1）我们采集了 Q-Pathway——一个面向底层视觉感知与质量评价的多模态数据集，包含人类对底层视觉方面带推理的直接反馈。2）在 Q-Pathway 的基础上，我们构建了 Q-Instruct——首个聚焦底层视觉相关人类提问的指令微调数据集。3）我们在底层视觉指令微调上开展的大量实验（图 2(d)）验证了 Q-Instruct 能提升 MLLM 的各项底层能力（图 1），并为后续研究把多种底层视觉能力纳入通用基座模型的范畴带来启示。

**EN** 2 Related Works

**ZH** 2 相关工作

**EN** 2.1 Low-level Visual Perception

**ZH** 2.1 底层视觉感知

**EN** Tasks and Datasets.

**ZH** 任务与数据集。

**EN** Image quality assessment (IQA), targeting to predict accurate scores aligned with integrated human opinions on all low-level aspects, has always been the chief task in low-level visual perception. Many datasets are developed to address IQA on artificially-distorted images [17, 28] (JPEG, AWGN, etc), in-the-wild photographs [14, 60], or recently-popular AI-generated contents [26, 58], providing important metrics for visual content production and distribution. Despite general IQA, recent studies have started to focus on finer-grained low-level visual aspects, and explored some related tasks such as evaluating on low-level visual dimensions (e.g. color, brightness) [9, 56], or distinguishing the existing distortions (e.g. blur, noise, over-exposure) in images [43]. Some recent works [55, 53, 54] also consider some photography-related dimensions (e.g. composition, lighting, bokeh) [21] as a broader sense of low-level aspects. In general, low-level visual perceptual tasks can include all aspects of image appearance (in contrast to object-level contents) that can be perceived by human and evoke different human feelings. While these low-level visual tasks used to be tackled separately, the proposed datasets bring the opportunities to include, relate and learn these tasks together, supporting one foundational model to generally master on these tasks.

**ZH** 图像质量评价（IQA）旨在预测与人类对所有底层方面综合意见相一致的准确分数，一直是底层视觉感知中的首要任务。已有许多数据集针对人工失真图像 [17, 28]（JPEG、AWGN 等）、真实场景照片 [14, 60] 或近来流行的 AI 生成内容 [26, 58] 上的 IQA 而构建，为视觉内容的生产与分发提供了重要度量。除通用 IQA 外，近期研究开始关注更细粒度的底层视觉方面，并探索了一些相关任务，例如评估底层视觉维度（如色彩、亮度）[9, 56]，或判别图像中存在的失真（如模糊、噪声、过曝）[43]。一些近期工作 [55, 53, 54] 还把构图、光照、虚化等摄影相关维度 [21] 视为更广义的底层方面。总体而言，底层视觉感知任务可涵盖图像外观中所有能被人类感知并引发不同感受的方面（与对象级内容相对）。这些底层视觉任务过去常被分别处理，而我们所提出的数据集为把它们纳入进来、建立关联并一同学习提供了机会，从而支撑一个基座模型在这些任务上实现通用掌握。

**EN** Approaches.

**ZH** 方法。

**EN** Similarly, the approaches designed for low-level visual perception also basically focus on their general IQA abilities. The traditional IQA metrics, e.g. NIQE [34], operate on discipline-based methodologies without training with human opinions, offering robust but less accurate evaluations. In contrast, deep learning-based methods [64, 42, 18, 8, 4, 51] utilize task-specific data, capitalizing on the extensive learning capacities of neural networks to tailor their assessment to particular data distributions, while they also suffer from compromised generalization abilities. Notably, recent methods [48, 65, 15, 67, 19] explore CLIP [38] for IQA, which stand out for their pioneer efforts on multi-modality integration for low-level vision, and exciting zero-shot performance. Their zero-shot IQA abilities are also inherited by most recent MLLMs [29, 63, 3]. Similar as NIQE, these multi-modality IQA methods are robust on various scenarios, yet not enough accurate on each single case. While these methods present improving performance on general IQA, the other finer-grained low-level visual perception abilities are still yet to be deeply investigated; moreover, tackling all these tasks separately may overlook the underlying relationships between them, refraining from reasoning among these sections. After instruction tuning with the proposed Q-Instruct, MLLMs can significantly improve their abilities on various low-level visual abilities, forecasting a future to unify these tasks through one model.

**ZH** 类似地，为底层视觉感知设计的方法也基本聚焦于其通用 IQA 能力。NIQE [34] 等传统 IQA 指标依据学科化的方法论运作，不利用人类意见作训练，评价稳健但精度有限。相比之下，基于深度学习的方法 [64, 42, 18, 8, 4, 51] 使用任务专用数据，借助神经网络强大的学习能力把评估裁剪到特定的数据分布上，代价是泛化能力受损。值得注意的是，近期一些方法 [48, 65, 15, 67, 19] 探索了把 CLIP [38] 用于 IQA，其在底层视觉的多模态融合上作出了开创性努力，并取得了令人惊喜的零样本性能；这类零样本 IQA 能力也被多数新近的 MLLM [29, 63, 3] 所继承。与 NIQE 类似，这些多模态 IQA 方法在各类场景下表现稳健，但在单个样本上精度不足。尽管这些方法在通用 IQA 上性能不断提升，其他更细粒度的底层视觉感知能力仍待深入探究；况且，分别处理所有这些任务可能忽略彼此之间的内在联系，从而妨碍在这些环节之间展开推理。经所提 Q-Instruct 指令微调后，MLLM 能显著提升其在各项底层视觉任务上的能力，预示了用一个模型统一这些任务的未来前景。

**EN** 2.2 Multi-modality Large Language Models

**ZH** 2.2 多模态大语言模型

**EN** Large language models (LLMs), e.g. GPT-4 [37], T5 [6], LLaMA [46], has shown great language abilities regarding general human knowledge. With CLIP [38] and additional adapting modules to involve visual inputs into LLMs, the multi-modality large language models (MLLMs) [24, 11, 30, 7, 63] can tackle a variety of multi-modality tasks for high-level vision, such as image captioning [5, 1, 61], visual question answering (VQA) [2, 32, 40], and more language-related capabilities [31, 10, 23]. Nevertheless, the evaluation results in the recent benchmark [57] reveal that MLLMs’ low-level visual abilities are still unsatisfactory, especially when it comes to the finer-grained low-level perception questions. While we notice that this is mainly due to the lack of respective data, we collect the first low-level visual instruction tuning dataset, the Q-Instruct, to improve low-level visual abilities for different MLLMs, and bring them into the realm of low-level visual perception.

**ZH** GPT-4 [37]、T5 [6]、LLaMA [46] 等大语言模型（LLM）在通用人类知识方面展现出强大的语言能力。借助 CLIP [38] 与额外的适配模块把视觉输入引入 LLM，多模态大语言模型（MLLM）[24, 11, 30, 7, 63] 能够处理多种面向高层视觉的多模态任务，例如图像描述 [5, 1, 61]、视觉问答（VQA）[2, 32, 40]，以及更多与语言相关的能力 [31, 10, 23]。然而，近期基准 [57] 的评测结果表明，MLLM 的底层视觉能力仍不尽如人意，在涉及更细粒度底层感知问题时尤其明显。我们注意到这主要源于相应数据的缺失，因而采集了首个底层视觉指令微调数据集 Q-Instruct，以提升不同 MLLM 的底层视觉能力，并把它们带入底层视觉感知的领地。

**EN** 3 the Q-Pathway

**ZH** 3 Q-Pathway

**EN** As the fundamental part of the dataset construction, we introduce the Q-Pathway, the first large scale dataset that collects text feedbacks from human on low-level visual aspects. To diversify and balance different low-level appearances, we sub-sample images from seven sources (Sec. 3.1) and reduce the skews in the source distributions (Tab. 1). After the preparation of images, we discuss the rationality and the detailed task definition for the pathway feedbacks (Sec. 3.2), a kind of natural language feedback, as collected in the Q-Pathway. The subjective study is conducted in-lab (Sec. 3.3), where all subjects are trained before providing feedback. The analysis of the Q-Pathway is in Sec. 3.4.

**ZH** 作为数据集构建的基础部分，我们引入 Q-Pathway——首个大规模收集人类对底层视觉方面文本反馈的数据集。为使不同的底层外观多样化且均衡，我们从七个来源（第 3.1 节）中对图像作子采样，并降低来源分布上的偏斜（表 1）。图像准备就绪后，我们讨论 pathway 反馈——Q-Pathway 所采集的一类自然语言反馈——的合理性与详细任务定义（第 3.2 节）。主观实验在实验室内开展（第 3.3 节），所有受试者在提供反馈前均经过培训。Q-Pathway 的分析见第 3.4 节。

**EN** Table 1: The Q-Pathway compared to its sources. We sub-sample the source images to reduce the skews in their ⟦SLOT_0⟧ distributions, resulting in the sampled distribution to be further balanced.

**ZH** 表 1：Q-Pathway 与其来源的对比。我们对来源图像作子采样，以降低其 ⟦SLOT_0⟧ 分布上的偏斜，使采样后的分布更为均衡。

<!-- [原子块 · table] Image Sources MOS ∈ [ 0,100 ) \mathrm{MOS}\in[0,100) Original Distribution Sampled Distribution Size μ MOS \mu_{\mathrm{MOS}} σ MOS \sigma_{\mathrm{MOS}} Size μ MOS \mu_{\mathrm{MOS}} σ MOS \sigma_{\m -->

<!-- [原子块 · img]  -->

**EN** Figure 3: (a) Example pathway feedbacks, each containing a detailed description followed by an overall evaluation, with context included. (b) The distribution of pathway feedback lengths. (c) Wordcloud of the Q-Pathway. (d) Top-frequency words related to low-level vision.

**ZH** 图 3：(a) pathway 反馈示例，每条都包含一段详细描述及随后的总体评价，并带有上下文。(b) pathway 反馈的长度分布。(c) Q-Pathway 的词云。(d) 与底层视觉相关的高频词。

**EN** 3.1 Preparation of Images

**ZH** 3.1 图像准备

**EN** The images in the Q-Pathway are sampled from various sources, including four in-the-wild IQA datasets [9, 14, 60, 12], and two datasets with AI-generated images [26, 58]. Specifically, as compared in Tab. 1, the sub-sampled population of images is carefully constructed to introduce more diverse low-level appearances in the Q-Pathway, which is neither skewed towards positive appearances nor towards negative appearances. Moreover, to further diversify the low-level appearances of the collected images, we design a custom variant of imagecorruptions [33] to randomly corrupt 1,012 originally-pristine images from COCO [5] dataset with one in 15 artificial distortions. The assembled sub-sampled dataset consists of 18,973 images, which are further fed to human subjects to provide pathway feedbacks.

**ZH** Q-Pathway 中的图像采样自多个来源，包括四个真实场景 IQA 数据集 [9, 14, 60, 12]，以及两个含 AI 生成图像的数据集 [26, 58]。具体地，如表 1 所对比，子采样出的图像总体经过精心构造，以在 Q-Pathway 中引入更多样化的底层外观，既不偏向正面外观也不偏向负面外观。此外，为进一步丰富所采集图像的底层外观，我们设计了 imagecorruptions [33] 的一个自定义变体，用 15 种人工失真之一随机破坏来自 COCO [5] 数据集的 1,012 张原本无失真图像。组装好的子采样数据集共含 18,973 张图像，随后交由受试者提供 pathway 反馈。

**EN** 3.2 Task Definition: the pathway Feedbacks

**ZH** 3.2 任务定义：pathway 反馈

**EN** For the Q-Pathway, to collect a richer and more nuanced understanding of human perception on low-level visual aspects, instead of collecting multi-dimensional scores as in existing studies [9, 56], we opt to collect a new format of annotation, termed pathway feedbacks, with an exhaustive natural language description on low-level visual attributes e.g. noise, brightness, clarity) followed by a general conclusion. The rationales for this format are as follows: (1) Primarily, the descriptions can preserve what humans perceive more completely and precisely. For instance, if an image has both dark and bright areas such as Fig 3(a) upper, the brightness score might not properly record [60, 52] this situation: the positional context cannot be preserved, and the reliability of the score could also be compromised, as neither labeling it as ‘dark’ nor as ‘bright’ is accurate. (2) Moreover, unlike free-form text feedbacks, the order of the two parts in pathway feedbacks generally aligns with the human reasoning process. For instance, while human subjects are shown with an underexposed yet clear image, they can provide intuitive reasoning leading to eclectic conclusions like “Thus, the quality of the image is acceptable”. This reasoning will help MLLMs to better emulate human perception and understanding related to low-level vision. While this pathway-style format faces challenges to be transformed into machine learning objectives in the past, the emergence of MLLMs has provided the opportunity to learn from these direct human feedbacks, in order to allow machines to more precisely and robustly align with human perception.

**ZH** 对 Q-Pathway 而言，为收集更丰富、更细致的人类对底层视觉方面的感知，我们没有像既有研究 [9, 56] 那样收集多维度分数，而是选择收集一种新格式的标注，称为 pathway 反馈：先对底层视觉属性（如噪声、亮度、清晰度）作详尽的自然语言描述，随后给出一个总体结论。采用这一格式的理由如下：(1) 首先，描述能更完整、更精确地保留人类的感知内容。例如，若一张图像同时存在暗部与亮部（如图 3(a) 上方），亮度分数可能无法妥善记录 [60, 52] 这一情形：位置上下文无法被保留，分数的可靠性也会受损，因为无论标为“暗”还是“亮”都不准确。(2) 其次，与自由格式的文本反馈不同，pathway 反馈中两部分的顺序大体契合人类的推理过程。例如当受试者看到一张欠曝但清晰的图像时，可以给出直观的推理，从而得出“因此，该图像质量尚可”这类折中的结论。这种推理将帮助 MLLM 更好地模拟人类在底层视觉上的感知与理解。过去这种 pathway 式的格式难以转化为机器学习目标，而 MLLM 的出现为从这些直接的人类反馈中学习提供了机会，使机器能够更精确、更稳健地与人类感知对齐。

**EN** 3.3 The subjective study process.

**ZH** 3.3 主观实验流程。

**EN** The subjective study is carried out in a well-controlled laboratory environment, during which a total of 39 trained human subjects are invited. Based on task definition, training material includes not only calibration on overall quality, but also on the respective text descriptions of different low-level appearances shown in visuals. Furthermore, as the majority of images come from IQA datasets, the mean opinion scores (MOSs) of them are also displayed to subjects to better calibrate them with a common understanding of quality. To facilitate their feedback process, we also show a reference attribute set that can be used in the descriptions. To avoid test fatigue of subjects, consecutive feedbacks on more than 30 images will be warned and discouraged; it will be further forcefully paused after 50 images. 58K pathway feedbacks are collected during the study, as exemplified in Fig. 3(a).

**ZH** 主观实验在严格受控的实验室环境中进行，共邀请 39 名经培训的受试者。依据任务定义，培训材料既包括总体质量上的校准，也包括对视觉中呈现的不同底层外观各自文字描述的校准。此外，由于多数图像来自 IQA 数据集，我们同时向受试者展示这些图像的平均意见分（MOS），以更好地把他们校准到对质量的共同理解上。为便利反馈过程，我们还展示了一组可用于描述中的参考属性。为避免受试者产生测试疲劳，连续对超过 30 张图像提供反馈会被警告并劝阻，超过 50 张后则被强制暂停。实验期间共收集到 58K 条 pathway 反馈，示例如图 3(a)。

<!-- [原子块 · img]  -->

**EN** Figure 4: The composition of the Q-Instruct dataset, in which the 200K instruction-response pairs include (a) 58K pathway reasoning, (b) visual question answering, with 76K what/how questions and 57K balanced yes-or-no questions, and (c) 12K extended conversations.

**ZH** 图 4：Q-Instruct 数据集的构成，其中 200K 条指令—响应对包括 (a) 58K 条 pathway 推理、(b) 视觉问答（76K 条 what/how 问题与 57K 条均衡的是非问题），以及 (c) 12K 条扩展对话。

**EN** 3.4 Analysis

**ZH** 3.4 分析

**EN** After the subjective study, we briefly analyze the collected feedbacks. Qualitatively (Fig. 3(a)), the pathway feedbacks can generally preserve the respective contexts related to low-level attributes. Moreover, feedbacks from different human subjects for the same image (as exemplified in [A] and [B] for each image) shows decent consistency (no controversial information), and slightly complements one another. Statistically, the length of feedbacks generally ranges from 20 to 100 words, with an average of 46.4 words, 4 times as long as common high-level image captions [5, 61] (Fig 3(b)). We also visualize the wordcloud [35] and the bar chart for the top frequency words related to low-level vision†† For better visualization, the two words that appear in every feedback, image and quality, are removed from the bar chart in Fig. 3(d)., demonstrating that the collected Q-Pathway covers a wide range of low-level attributes, and includes positive and negative feedbacks within similar proportions.

**ZH** 主观实验结束后，我们对收集到的反馈作简要分析。定性方面（图 3(a)），pathway 反馈大体能保留与底层属性相关的各自上下文。此外，不同受试者对同一张图像给出的反馈（每张图像以 [A] 与 [B] 为例）表现出良好的一致性（无相互矛盾的信息），并略有互补。统计方面，反馈长度一般介于 20 至 100 词，平均 46.4 词，是常见高层图像描述 [5, 61] 的 4 倍（图 3(b)）。我们还可视化了词云 [35] 以及与底层视觉相关的高频词条形图†† 为便于可视化，图 3(d) 的条形图移去了每条反馈中都会出现的两个词：image 与 quality。，表明所采集的 Q-Pathway 覆盖了广泛的底层属性，且正面与负面反馈所占比例相近。

**EN** 4 the Q-Instruct

**ZH** 4 Q-Instruct

**EN** The long and diverse feedbacks in the Q-Pathway provides sufficient reference for the automatic generation process of instruction-response pairs to be used for low-level visual instruction tuning. While the pathway feedbacks themselves can teach MLLMs to reason low-level aspects and predict quality (Sec. 4.1), we design more instruction types to allow MLLMs to respond to a variety of human queries, including a visual question answering subset (Sec. 4.2) for more accurate low-level perception ability [57], and an extended conversation subset (Sec. 4.3) to allow MLLMs to seamlessly chat with human about topics related to low-level visual aspects. Overall, the Q-Instruct dataset includes 200K instruction-response pairs, with its details as follows.

**ZH** Q-Pathway 中长而多样的反馈，为自动生成用于底层视觉指令微调的指令—响应对提供了充足参考。虽然 pathway 反馈本身就能教会 MLLM 对底层方面作推理并预测质量（第 4.1 节），我们仍设计了更多指令类型，使 MLLM 能够回应多样的人类提问，包括一个视觉问答子集（第 4.2 节）以获得更准确的底层感知能力 [57]，以及一个扩展对话子集（第 4.3 节）使 MLLM 能就输入图像的底层视觉方面与人类顺畅交谈。总体而言，Q-Instruct 数据集包含 200K 条指令—响应对，具体如下。

**EN** 4.1 Low-level Reasoning with pathway Feedbacks

**ZH** 4.1 基于 pathway 反馈的底层推理

**EN** Similar as image captioning [5, 1, 61], a general low-level visual description ability is also vital for MLLMs. As analyzed in Fig. 3, the pathway feedbacks are direct and holistic human responses that generally describe low-level visual appearances. Furthermore, these feedbacks provide reasoning from low-level attributes (brightness, clarity) to overall quality ratings (good/poor), which could activate the potential reasoning abilities [50, 20] of MLLMs on IQA. Henceforth, with each pathway feedback as response and a general prompt as instruction, we include 58K pathway reasoning (Fig. 4(a)) as the primary part of the Q-Instruct dataset.

**ZH** 与图像描述 [5, 1, 61] 类似，通用的底层视觉描述能力对 MLLM 同样至关重要。如图 3 所分析，pathway 反馈是直接而完整的人类回应，通常描述底层视觉外观；而且这些反馈提供了从底层属性（亮度、清晰度）到总体质量评级（好／差）的推理，有望激活 MLLM 在 IQA 上的潜在推理能力 [50, 20]。因此，我们以每条 pathway 反馈作为响应、以一个通用提示作为指令，把 58K 条 pathway 推理（图 4(a)）纳入 Q-Instruct 数据集，作为其主要部分。

**EN** 4.2 Visual Question Answering (VQA)

**ZH** 4.2 视觉问答（VQA）

**EN** Besides directly apply the Q-Pathway into low-level visual instruction tuning, we also design a GPT [36]-participated pipeline to convert them into a visual question answering (VQA) subset. In general, we ask GPT to generate diverse-style questions related to low-level-vision from the pathway feedbacks, and provide answers with as few words as possible. Via this process, we convert the feedbacks into 76K questions, including how questions answered with opinion-related adjectives (e.g. good/poor, high/low), or i.e. what questions answered with attribute-related (blur/noise/focus) or context-related (left/the peacock/the background) nouns, as shown in the upper part of Fig. 4(b). We further instruct GPT to generate binary judgments (yes/no, Fig. 4(b) lower) from the feedbacks, and balance yes and no into 1:1 ratio, with 57K yes-or-no questions collected at last. As for the answering format, following A-OKVQA [40], despite the direct answers, we also create several distracting answers for the questions, and convert them into an additional multi-choice question (MCQ) format (the pink boxes in Fig. 4(b)).

**ZH** 除直接把 Q-Pathway 用于底层视觉指令微调外，我们还设计了一条 GPT [36] 参与的流水线，把它们转换为视觉问答（VQA）子集。总体上，我们让 GPT 依据 pathway 反馈生成与底层视觉相关的多种风格问题，并要求答案尽可能简短。通过这一过程，我们把反馈转换为 76K 条问题，包括以观点性形容词作答的 how 问题（如 good/poor、high/low），或以属性相关（blur/noise/focus）或上下文相关（left/the peacock/the background）名词作答的 what 问题，如图 4(b) 上半部分所示。我们进一步指示 GPT 由反馈生成二值判断（yes/no，图 4(b) 下半部分），并把 yes 与 no 平衡到 1:1 比例，最终收集到 57K 条是非问题。在作答格式上，沿用 A-OKVQA [40]，除直接答案外，我们还为每个问题构造若干干扰答案，并转换为额外的多选题（MCQ）格式（图 4(b) 中的粉色框）。

**EN** 4.3 Extended Conversations

**ZH** 4.3 扩展对话

**EN** While the first two subsets are designed to enhance the fundamental language-related abilities for low-level vision, the third subset of the Q-Instruct, the extended conversations (Fig. 4(c)), focuses on improving the ability to discuss with human grounded on the low-level visual aspects of an input image. These discussions include five major scopes: 1) Examining the causes of low-level visual patterns; 2) Providing improvement suggestions on photography; 3) Providing tools to restore, enhance, or edit the image; 4) Recommending the image to respective consumers; 5) Other conversations that may happen given the low-level visual descriptions provided in the pathway feedbacks. Similarly, the extended conversation subset is also generated by GPT, with in total 12K conversations collected for the Q-Instruct.

**ZH** 前两个子集旨在增强底层视觉相关的基础语言能力，Q-Instruct 的第三个子集——扩展对话（图 4(c)）——则聚焦于提升围绕输入图像底层视觉方面与人类讨论的能力。这些讨论涵盖五个主要范畴：1）检视底层视觉模式的成因；2）给出摄影方面的改进建议；3）提供可用于复原、增强或编辑图像的工具；4）把该图像推荐给相应的受众；5）在 pathway 反馈所提供的底层视觉描述下可能发生的其他对话。扩展对话子集同样由 GPT 生成，共为 Q-Instruct 收集了 12K 条对话。

<!-- [原子块 · img]  -->

**EN** Figure 5: Training strategies for low-level visual instruction tuning evaluated in our study, including (a) mix the Q-Instruct with high-level visual instruction tuning datasets, (b) conduct a further low-level tuning stage with only Q-Instruct after high-level tuning.

**ZH** 图 5：本研究评测的底层视觉指令微调训练策略，包括 (a) 把 Q-Instruct 与高层视觉指令微调数据集混合，(b) 在高层微调之后只用 Q-Instruct 作进一步的底层微调阶段。

**EN** 5 Low-level Visual Instruction Tuning

**ZH** 5 底层视觉指令微调

**EN** In this section, we discuss the standard training strategies for low-level visual instruction tuning, i.e. when to involve the Q-Instruct dataset during the training of MLLMs. In general, the training of open-source MLLMs [7, 24, 63] includes two stages: First, aligning the representation space of the visual backbone and the LLM with million-scale web data [39, 41]. Second, visual instruction tuning with a combination of human-labeled datasets [62, 2, 5, 32]. Considering the scale of the Q-Instruct, a general strategy is to mix its instruction-response pairs with the high-level datasets in the second stage, so as to ideally built their low-level visual abilities within general high-level awareness, as shown in Fig. 5(a). Another faster and more convenient strategy is a further third stage only with the Q-Instruct (Fig. 5(b)) after original high-level tuning. In our experiments, we validate that they both bring notable improvements on various low-level visual tasks, and involving high-level awareness contributes to the effectiveness of both strategies.

**ZH** 本节讨论底层视觉指令微调的标准训练策略，即在 MLLM 训练过程中何时引入 Q-Instruct 数据集。总体而言，开源 MLLM [7, 24, 63] 的训练包含两个阶段：其一，用百万量级的网络数据 [39, 41] 对齐视觉骨干与 LLM 的表示空间；其二，用人工标注数据集的组合 [62, 2, 5, 32] 作视觉指令微调。考虑到 Q-Instruct 的规模，一种通用策略是在第二阶段把其指令—响应对与高层数据集混合，从而理想地在通用高层认知之内构建底层视觉能力，如图 5(a) 所示。另一种更快、更便捷的策略是在原有高层微调之后，增加只用 Q-Instruct 的第三阶段（图 5(b)）。实验中我们验证，两种策略都能在各项底层视觉任务上带来显著改进，而引入高层认知对两种策略的有效性均有贡献。

**EN** 6 Experiments

**ZH** 6 实验

**EN** 6.1 Experimental Setups

**ZH** 6.1 实验设置

**EN** Baseline models.

**ZH** 基线模型。

**EN** We pick four variants of three state-of-the-art MLLMs within diverse meta structures (Tab. 2) as baseline models to evaluate their low-level visual abilities before and after training with the Q-Instruct. Each model is evaluated under both strategies as in Fig. 5, with the original combination of high-level datasets unchanged.

**ZH** 我们选取三个最先进 MLLM 的四个变体（具有不同元结构，表 2）作为基线模型，以评估它们在用 Q-Instruct 训练前后的底层视觉能力。每个模型都在图 5 所示的两种策略下评测，高层数据集的原始组合保持不变。

**EN** Table 2: Baseline MLLMs for low-level visual instruction tuning.

**ZH** 表 2：用于底层视觉指令微调的基线 MLLM。

<!-- [原子块 · table] Month/Year {}^{\text{Month/Year}} Model Name Visual Backbone V → \to L Module Language Model Oct/23 {}^{\text{Oct/23}} LLaVA-v1.5 ( 7B ) [ 29 ] CLIP-ViT-L14 ↑336 MLP Vicuna-v1.5-7B [ 68 ] Oct/23 {}^{\ -->

**EN** Table 3: Comparison of the low-level Perception ability between baseline MLLMs and Q-Instruct-tuned versions, on LLVisionQA-dev.

**ZH** 表 3：基线 MLLM 与经 Q-Instruct 微调版本在 LLVisionQA-dev 上底层感知能力的对比。

<!-- [原子块 · table] Model (variant) Q-Instruct Strategy Yes-or-No ↑ \uparrow What ↑ \uparrow How ↑ \uparrow Distortion ↑ \uparrow Other ↑ \uparrow I-C Distortion ↑ \uparrow I-C Other ↑ \uparrow Overall ↑ \uparrow random  -->

**EN** Table 4: Comparison of the low-level Perception ability between baseline MLLMs and Q-Instruct-tuned versions, on LLVisionQA-test.

**ZH** 表 4：基线 MLLM 与经 Q-Instruct 微调版本在 LLVisionQA-test 上底层感知能力的对比。

<!-- [原子块 · table] Model (variant) Q-Instruct Strategy Yes-or-No ↑ \uparrow What ↑ \uparrow How ↑ \uparrow Distortion ↑ \uparrow Other ↑ \uparrow I-C Distortion ↑ \uparrow I-C Other ↑ \uparrow Overall ↑ \uparrow random  -->

**EN** Training Settings.

**ZH** 训练设置。

**EN** We follow the default instruction tuning hyper-parameters of MLLMs during all training processes involving the Q-Instruct. As we aim to reach a unified low-level visual foundation model, for each MLLM, the final checkpoint is saved and tested for all evaluations. To avoid data contamination, during training, we remove data items with images that may appear in the evaluation sets.

**ZH** 在所有涉及 Q-Instruct 的训练过程中，我们沿用 MLLM 默认的指令微调超参数。由于目标是达成一个统一的底层视觉基座模型，对每个 MLLM，我们保存最终检查点并用于所有评测。为避免数据污染，训练过程中我们剔除了图像可能出现在评测集中的数据项。

**EN** 6.2 Main Results

**ZH** 6.2 主要结果

**EN** The low-level visual abilities of MLLMs after low-level visual instruction tuning are quantitatively evaluated in three tasks defined by [57], including (A1) Perception, by measuring the accuracy of answering multi-choice questions (MCQ) related to low-level vision (Fig. 1); (A2) Description, which examines how MLLMs can generally transform low-level visual information into text. As for (A3) Quality Assessment, considering that the Q-Instruct already contains a large proportion of images in major IQA databases, we evaluate and discuss how the instructed MLLMs generalize on unseen images. For reproducibility, all responses from MLLMs are generated with greedy search. Qualitative analyses are provided in supplementary materials.

**ZH** 经底层视觉指令微调后，MLLM 的底层视觉能力在 [57] 定义的三项任务上得到定量评测，包括 (A1) 感知——通过回答与底层视觉相关的多选题（MCQ）的准确率来衡量（图 1）；(A2) 描述——考察 MLLM 把底层视觉信息转化为文本的一般能力。至于 (A3) 质量评价，考虑到 Q-Instruct 已包含主要 IQA 数据库中相当大比例的图像，我们评测并讨论经指令微调的 MLLM 在未见过图像上的泛化表现。为保证可复现，MLLM 的所有回答均以贪心搜索生成。定性分析见补充材料。

**EN** (A1) Perception (MCQ).

**ZH** (A1) 感知（MCQ）。

**EN** From Tab. 3 and Tab. 4, we observe that either strategy of including Q-Instruct into the training of MLLMs can significantly improve their low-level perception ability. The results demonstrate the effectiveness of the proposed pipeline to automatically generate the VQA subset (including MCQ) from the pathway feedbacks via GPT, which could be expected to extend to further query types. Specifically, among all dimensions, we notice that the accuracy on Yes-or-No question type is most significantly enhanced (avg. more than 10%). Moreover, improvements on distortions are more significant than on other low-level attributes (aesthetics, photography techniques), suggesting that the major concerns as raised by human in the Q-Pathway are still related to distortions. We hope that our pipeline can be extended to cover more types of questions and a broader range of concerns in the future.

**ZH** 由表 3 与表 4 可见，无论采用哪种把 Q-Instruct 纳入 MLLM 训练的策略，都能显著提升其底层感知能力。结果证明了所提流水线的有效性——借助 GPT 由 pathway 反馈自动生成 VQA 子集（含 MCQ），并有希望推广到更多提问类型。具体地，在所有维度中我们注意到，是非类问题的准确率提升最为显著（平均超过 10%）。此外，失真方面的提升比其他底层属性（美学、摄影技法）更明显，说明人类在 Q-Pathway 中提出的主要关切仍与失真相关。我们期待该流水线未来能扩展到更多问题类型与更广的关切范围。

**EN** (A2) Description.

**ZH** (A2) 描述。

**EN** The low-level visual instruction tuning also notably improve the low-level description ability of MLLMs, especially on the relevance (+0.31), with all tuned variants obtaining more than 1.5/2 average score. In contrast, the improvements on completeness (+0.17) and precision (+0.04) are less significant, implying that the captioning-like instruction format may not be sufficient for the low-level description task that requires much longer responses. We look forward to better solutions in the future.

**ZH** 底层视觉指令微调也显著提升了 MLLM 的底层描述能力，尤其是相关性（+0.31），所有微调变体都取得了超过 1.5/2 的平均分。相比之下，完整性（+0.17）与精确性（+0.04）的提升较不显著，说明类似图像描述的指令格式可能不足以支撑需要更长响应的底层描述任务。我们期待未来有更好的解决方案。

**EN** Table 5: Comparison of the low-level Description ability between baseline MLLMs and Q-Instruct-tuned versions, under the same prompt: “Describe and evaluate the quality of the image.”

**ZH** 表 5：在统一提示“描述并评价该图像的质量。”下，基线 MLLM 与经 Q-Instruct 微调版本底层描述能力的对比。

<!-- [原子块 · table] Model (variant) Q-Instruct Strategy completeness precision relevance sum LLaVA-v1.5 ( 7B ) no (Baseline) 0.90 1.13 1.18 3.21 (a) mix w/ high-level 1.12 1.17 1.57 3.86 (b) after high-level 1.11 1.16 1. -->

**EN** Table 6: Comparison of the Quality Assessment (A3) ability between baseline MLLMs and Q-Instruct-tuned versions, where “Mostly Seen” datasets denote those with the majority of their images sampled in the Q-Instruct, and “Barely Seen” represent those with only a small proportion (⟦SLOT_1⟧20%) sampled. The “Never Seen” datasets have zero overlap with the Q-Instruct. Metrics are SRCC / PLCC.

**ZH** 表 6：基线 MLLM 与经 Q-Instruct 微调版本在质量评价（A3）能力上的对比，其中“Mostly Seen”表示其大部分图像被采样进 Q-Instruct 的数据集，“Barely Seen”表示仅有小部分（⟦SLOT_1⟧20%）被采样。“Never Seen”数据集与 Q-Instruct 零重叠。指标为 SRCC / PLCC。

<!-- [原子块 · table] Dataset Group Mostly Seen Barely Seen Never Seen % of dataset seen during training 48.92% 95.26% 2.00% 17.11% 13.41% 0% 0% 0% Model ( variant ) Q-Instruct Strategy KonIQ-10k SPAQ LIVE-FB LIVE-itw AGIQ -->

**EN** (A3) Image Quality Assessment (IQA).

**ZH** (A3) 图像质量评价（IQA）。

**EN** Despite the two directly tuned tasks, we follow the softmax pooling strategy [57] to extract quality scores from MLLMs and evaluate their IQA ability, as listed in Tab. 6. Primarily, we notice the excellent performance on two “mostly seen” datasets. As we do not directly use any MOS values during training, this result suggests that we can effectively tune MLLMs to reach very high accuracy on IQA without any numerical values as supervision. This result by-side suggests the high reliability of the proposed datasets. The more exciting results are the huge improvements on “barely seen” (with a small proportion of images sampled into the Q-Instruct) and even “never seen” (cross-set) datasets. Considering the three “never seen” datasets [66, 13, 28] (with computer-generated images, artificially-degraded image, and even videos respectively) have notable domain gap with the major part of the Q-Instruct dataset (mostly in-the-wild photographs), the +0.243 average SRCC gain on them demonstrates that the low-level instruction tuning can robustly improve low-level perception abilities of MLLMs on a broad domain.

**ZH** 除两个直接微调的任务外，我们沿用 softmax 池化策略 [57] 从 MLLM 中抽取质量分数并评测其 IQA 能力，结果列于表 6。首先，我们注意到在两个“mostly seen”数据集上的出色表现。由于训练过程中并未直接使用任何 MOS 数值，该结果表明我们能有效微调 MLLM，在没有任何数值监督的情况下于 IQA 上达到很高的精度；这一结果也侧面印证了所提数据集的高可靠性。更令人振奋的是在“barely seen”（少量图像被采样进 Q-Instruct）乃至“never seen”（跨集）数据集上的巨大提升。考虑到三个“never seen”数据集 [66, 13, 28]（分别含计算机生成图像、人工退化图像乃至视频）与 Q-Instruct 数据集主体（多为真实场景照片）存在明显的域差异，其上 +0.243 的平均 SRCC 增益说明，底层指令微调能稳健地提升 MLLM 在宽广域上的底层感知能力。

**EN** 6.3 Ablation Studies

**ZH** 6.3 消融研究

<!-- [原子块 · img]  -->

**EN** Figure 6: Accuracy on MCQ questions with respect to data samples seen during training (in comparison with baseline), demonstrating the effectiveness of scaling up the Q-Instruct dataset.

**ZH** 图 6：MCQ 问题准确率随训练中所见数据样本量的变化（与基线对比），说明了扩大 Q-Instruct 数据集规模的有效性。

**EN** Despite the main results for low-level visual instruction tuning, we also compare among several data variations during tuning on LLaVA-v1.5 (7B), analyzed as follows.

**ZH** 除底层视觉指令微调的主要结果外，我们还在 LLaVA-v1.5（7B）上比较了微调期间的若干数据变体，分析如下。

**EN** #1: Effects of scaling up the Q-Instruct.

**ZH** #1：扩大 Q-Instruct 的效应。

**EN** The first group of variations discuss the effects of data amount during low-level visual instruction tuning. As illustrated in Fig. 6, under either mix or after strategy, scaling up the Q-Instruct during training can continuously improve the low-level perceptual accuracy. Moreover, the results suggest that the performance of MLLMs is still not saturated even with the current 200K data scale, encouraging us to further unleash their vast underlying power on tackling low-level visual tasks.

**ZH** 第一组变体讨论底层视觉指令微调中数据量的影响。如图 6 所示，无论采用混合还是后置策略，训练时扩大 Q-Instruct 规模都能持续提升底层感知准确率。此外，结果表明即便在当前 200K 的数据规模下，MLLM 的性能仍未饱和，这激励我们进一步释放其在处理底层视觉任务上蕴藏的巨大潜力。

**EN** Table 7: Comparison on low-level Description ability between full Q-Instruct and only Q-Pathway as low-level training dataset.

**ZH** 表 7：以完整 Q-Instruct 与仅 Q-Pathway 作为底层训练数据集时，底层描述能力的对比。

<!-- [原子块 · table] Q-Instruct Strategy low-level dataset completeness precision relevance sum no (Baseline) None 0.90 1.13 1.18 3.21 (a) mix w/ high-level only Q-Pathway 1.07 1.13 1.54 3.74 full Q-Instruct 1.12 1.17 1.5 -->

**EN** Table 8: Comparison on low-level Perception ability (test set) between training with full Q-Instruct dataset and only VQA subset.

**ZH** 表 8：以完整 Q-Instruct 数据集与仅 VQA 子集训练时，底层感知能力（测试集）的对比。

<!-- [原子块 · table] Q-Instruct Strategy low-level dataset Yes-or-No What How Overall no (Baseline) None 64.6% 59.2% 55.8% 60.1% (a) mix w/ high-level only VQA subset 78.1% 61.5% 61.5% 67.6% full Q-Instruct 78.7% 64.0% 63 -->

**EN** #2: Effects of joint training.

**ZH** #2：联合训练的效应。

**EN** In the low-level visual instruction tuning, we combine different subsets together and train them jointly under one unified model. To validate its effectiveness, we compare this approach with traditional task-separate tuning, on both low-level description (Tab. 7) and question-answering (Tab. 8) capabilities. Both experiments indicate that a joint learning scheme can improve the accuracy on these abilities, especially when low-level data is independently used during tuning. While the different subsets in the Q-Instruct come from the same original human feedbacks, the improvement is cost-efficient, and inspires further explorations for low-level visual instruction tuning to expand to even more tasks, so as to further improve the low-level capabilities of these MLLMs.

**ZH** 在底层视觉指令微调中，我们把不同子集合并，在一个统一模型下联合训练。为验证其有效性，我们在底层描述（表 7）与问答（表 8）两项能力上，把该做法与传统的分任务微调作比较。两组实验都表明，联合学习方案能提升这些能力上的准确率，在微调时独立使用底层数据时尤为明显。由于 Q-Instruct 中不同子集源自同一批原始人类反馈，这种提升是低成本的，并启发人们进一步探索把底层视觉指令微调扩展到更多任务，从而持续提升这些 MLLM 的底层能力。

**EN** Table 9: Comparison between the proposed two strategies (as in Sec. 5, and another variant that replaces high-level tuning into the low-level tuning, on their low-level Perception ability (test set).

**ZH** 表 9：所提两种策略（见第 5 节）与另一种把高层微调替换为底层微调的变体在底层感知能力（测试集）上的对比。

<!-- [原子块 · table] Q-Instruct Strategy Yes-or-No What How Overall no (Baseline) 64.6% 59.2% 55.8% 60.1% replace high-level ( not adopted ) 75.0% 59.4% 56.4% 64.1% mix with high-level ( ours , strategy (a)) 78.7% 64.0% 6 -->

**EN** #3: Effects of high-level awareness.

**ZH** #3：高层认知的效应。

**EN** While we notice generally on par abilities between the mix strategy and the after strategy, we further investigate the performance if we replace the second stage datasets into the Q-Instruct, while no high-level instruction tuning datasets are involved during training. As compared in Tab. 9, the “replace” strategy is notably worse than the two adopted strategies in Sec. 5, suggesting that fundamental high-level awareness is important on general low-level visual recognition for MLLMs.

**ZH** 我们注意到混合策略与后置策略的能力大体相当，因此进一步考察：若把第二阶段的数据集替换为 Q-Instruct、训练中完全不引入高层指令微调数据集，性能会如何。如表 9 所对比，“替换”策略明显劣于第 5 节采用的两种策略，说明基础性的高层认知对 MLLM 的通用底层视觉识别十分重要。

**EN** 7 Conclusion

**ZH** 7 结论

**EN** Our work proposes the first-of-a-kind multi-modal datasets on low-level visual aspects, including the Q-Pathway with 58K human text feedbacks, and the derived Q-Instruct with 200K instruction-response pairs, to facilitate low-level visual instruction tuning for MLLMs. They allow MLLMs to significantly improve their question-answering accuracy related to low-level visual perception, and showcase the potential for providing more reliable low-level descriptions for images and eventually relieving human burdens on this task. Further, their IQA performance reveals an intriguing phenomenon, that pure text-driven instruction tuning can sufficiently align MLLMs with numerical quality scores, with impressive generalization on unseen types of visual inputs. In summary, our work has advanced a solid step forward on improving the low-level visual abilities of MLLMs, and we hope that our progress and insights can encourage future explorations towards an eventual goal that foundation models understand the low-level visual world like a human.

**ZH** 本文提出了首个面向底层视觉方面的多模态数据集，包括含 58K 条人类文本反馈的 Q-Pathway，以及由其派生、含 200K 条指令—响应对的 Q-Instruct，用以支撑 MLLM 的底层视觉指令微调。它们使 MLLM 显著提升了与底层视觉感知相关的问答准确率，并展现出为图像提供更可靠底层描述、最终减轻人类在该任务上负担的潜力。进一步地，其 IQA 性能揭示了一个耐人寻味的现象：纯文本驱动的指令微调足以让 MLLM 与数值化质量分数对齐，并对未见过的视觉输入类型具有出色的泛化能力。总而言之，本文在提升 MLLM 底层视觉能力上迈出了坚实的一步；我们也希望这一进展与洞见能激励后续探索，朝着“基座模型像人一样理解底层视觉世界”这一最终目标前进。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] [1] Harsh Agrawal, Karan Desai, Yufei Wang, Xinlei Chen, Rishabh Jain, Mark Johnson, Dhruv Batra, Devi Parikh, Stefan Lee, and Peter Anderson. nocaps: novel object captioning at scale. In ICCV , 2019. -->

<!-- [原子块 · verbatim] [2] Stanislaw Antol, Aishwarya Agrawal, Jiasen Lu, Margaret Mitchell, Dhruv Batra, C. Lawrence Zitnick, and Devi Parikh. VQA: Visual Question Answering. In ICCV , 2015. -->

<!-- [原子块 · verbatim] [3] Jinze Bai, Shuai Bai, Shusheng Yang, Shijie Wang, Sinan Tan, Peng Wang, Junyang Lin, Chang Zhou, and Jingren Zhou. Qwen-vl: A versatile vision-language model for understanding, localization, text  -->

<!-- [原子块 · verbatim] [4] Chaofeng Chen, Jiadi Mo, Jingwen Hou, Haoning Wu, Liang Liao, Wenxiu Sun, Qiong Yan, and Weisi Lin. Topiq: A top-down approach from semantics to distortions for image quality assessment, 2023. -->

<!-- [原子块 · verbatim] [5] Xinlei Chen, Hao Fang, Tsung-Yi Lin, Ramakrishna Vedantam, Saurabh Gupta, Piotr Dollar, and C. Lawrence Zitnick. Microsoft coco captions: Data collection and evaluation server, 2015. -->

<!-- [原子块 · verbatim] [6] Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang, Mostafa Dehghani, Siddhartha Brahma, Albert Webson, Shixiang Shane Gu, Zhuyun Dai, Mirac Suzgun,  -->

<!-- [原子块 · verbatim] [7] Wenliang Dai, Junnan Li, Dongxu Li, Anthony Meng Huat Tiong, Junqi Zhao, Weisheng Wang, Boyang Li, Pascale Fung, and Steven Hoi. Instructblip: Towards general-purpose vision-language models with i -->

<!-- [原子块 · verbatim] [8] Keyan Ding, Kede Ma, Shiqi Wang, and Eero P. Simoncelli. Image quality assessment: Unifying structure and texture similarity. IEEE TPAMI , 44(5):2567–2581, 2022. -->

<!-- [原子块 · verbatim] [9] Yuming Fang, Hanwei Zhu, Yan Zeng, Kede Ma, and Zhou Wang. Perceptual quality assessment of smartphone photography. In CVPR , 2020. -->

<!-- [原子块 · verbatim] [10] Chaoyou Fu, Peixian Chen, Yunhang Shen, Yulei Qin, Mengdan Zhang, Xu Lin, Zhenyu Qiu, Wei Lin, Jinrui Yang, Xiawu Zheng, Ke Li, Xing Sun, and Rongrong Ji. Mme: A comprehensive evaluation benchmar -->

<!-- [原子块 · verbatim] [11] Peng Gao, Jiaming Han, Renrui Zhang, Ziyi Lin, Shijie Geng, Aojun Zhou, Wei Zhang, Pan Lu, Conghui He, Xiangyu Yue, Hongsheng Li, and Yu Qiao. Llama-adapter v2: Parameter-efficient visual instruc -->

<!-- [原子块 · verbatim] [12] Deepti Ghadiyaram and Alan C. Bovik. Massive online crowdsourced study of subjective and objective picture quality. IEEE , 25(1):372–387, 2016. -->

<!-- [原子块 · verbatim] [13] Vlad Hosu, Franz Hahn, Mohsen Jenadeleh, Hanhe Lin, Hui Men, Tamás Szirányi, Shujun Li, and Dietmar Saupe. The konstanz natural video database (konvid-1k). In QoMEX , pages 1–6, 2017. -->

<!-- [原子块 · verbatim] [14] Vlad Hosu, Hanhe Lin, Tamas Sziranyi, and Dietmar Saupe. Koniq-10k: An ecologically valid database for deep learning of blind image quality assessment. IEEE TIP , 29:4041–4056, 2020. -->

<!-- [原子块 · verbatim] [15] Jingwen Hou, Weisi Lin, Yuming Fang, Haoning Wu, Chaofeng Chen, Liang Liao, and Weide Liu. Towards transparent deep image aesthetics assessment with tag-based content descriptors. IEEE TIP , 2023 -->

<!-- [原子块 · verbatim] [16] Drew A Hudson and Christopher D Manning. Gqa: A new dataset for real-world visual reasoning and compositional question answering. Conference on Computer Vision and Pattern Recognition (CVPR) , 20 -->

<!-- [原子块 · verbatim] [17] Dinesh Jayaraman, Anish Mittal, Anush K. Moorthy, and Alan C. Bovik. Objective quality assessment of multiply distorted images. In ASILOMAR , pages 1693–1697, 2012. -->

<!-- [原子块 · verbatim] [18] Junjie Ke, Qifei Wang, Yilin Wang, Peyman Milanfar, and Feng Yang. Musiq: Multi-scale image quality transformer. In ICCV , pages 5148–5157, 2021. -->

<!-- [原子块 · verbatim] [19] Junjie Ke, Keren Ye, Jiahui Yu, Yonghui Wu, Peyman Milanfar, and Feng Yang. Vila: Learning image aesthetics from user comments with vision-language pretraining, 2023. -->

<!-- [原子块 · verbatim] [20] Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yutaka Matsuo, and Yusuke Iwasawa. Large language models are zero-shot reasoners, 2023. -->

<!-- [原子块 · verbatim] [21] Shu Kong, Xiaohui Shen, Zhe Lin, Radomir Mech, and Charless Fowlkes. Photo aesthetics ranking network with attributes and content adaptation. In ECCV , 2016. -->

<!-- [原子块 · verbatim] [22] Ranjay Krishna, Yuke Zhu, Oliver Groth, Justin Johnson, Kenji Hata, Joshua Kravitz, Stephanie Chen, Yannis Kalantidis, Li-Jia Li, David A. Shamma, Michael S. Bernstein, and Li Fei-Fei. Visual gen -->

<!-- [原子块 · verbatim] [23] Bohao Li, Rui Wang, Guangzhi Wang, Yuying Ge, Yixiao Ge, and Ying Shan. Seed-bench: Benchmarking multimodal llms with generative comprehension, 2023a. -->

<!-- [原子块 · verbatim] [24] Bo Li, Yuanhan Zhang, Liangyu Chen, Jinghao Wang, Jingkang Yang, and Ziwei Liu. Otter: A multi-modal model with in-context instruction tuning. arXiv preprint arXiv:2305.03726 , 2023b. -->

<!-- [原子块 · verbatim] [25] Chunyuan Li, Zhe Gan, Zhengyuan Yang, Jianwei Yang, Linjie Li, Lijuan Wang, and Jianfeng Gao. Multimodal foundation models: From specialists to general-purpose assistants, 2023c. -->

<!-- [原子块 · verbatim] [26] Chunyi Li, Zicheng Zhang, Haoning Wu, Wei Sun, Xiongkuo Min, Xiaohong Liu, Guangtao Zhai, and Weisi Lin. Agiqa-3k: An open database for ai-generated image quality assessment, 2023d. -->

<!-- [原子块 · verbatim] [27] Dingquan Li, Tingting Jiang, Weisi Lin, and Ming Jiang. Which has better visual quality: The clear blue sky or a blurry animal? IEEE TMM , 21(5):1221–1234, 2019. -->

<!-- [原子块 · verbatim] [28] Hanhe Lin, Vlad Hosu, and Dietmar Saupe. Kadid-10k: A large-scale artificially distorted iqa database. In QoMEX , pages 1–3, 2019. -->

<!-- [原子块 · verbatim] [29] Haotian Liu, Chunyuan Li, Yuheng Li, and Yong Jae Lee. Improved baselines with visual instruction tuning, 2023a. -->

<!-- [原子块 · verbatim] [30] Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. Visual instruction tuning, 2023b. -->

<!-- [原子块 · verbatim] [31] Yuan Liu, Haodong Duan, Yuanhan Zhang, Bo Li, Songyang Zhang, Wangbo Zhao, Yike Yuan, Jiaqi Wang, Conghui He, Ziwei Liu, Kai Chen, and Dahua Lin. Mmbench: Is your multi-modal model an all-around  -->

<!-- [原子块 · verbatim] [32] Kenneth Marino, Mohammad Rastegari, Ali Farhadi, and Roozbeh Mottaghi. Ok-vqa: A visual question answering benchmark requiring external knowledge. In Conference on Computer Vision and Pattern Rec -->

<!-- [原子块 · verbatim] [33] Claudio Michaelis, Benjamin Mitzkus, Robert Geirhos, Evgenia Rusak, Oliver Bringmann, Alexander S. Ecker, Matthias Bethge, and Wieland Brendel. Benchmarking robustness in object detection: Autono -->

<!-- [原子块 · verbatim] [34] Anish Mittal, Rajiv Soundararajan, and Alan C. Bovik. Making a “completely blind” image quality analyzer. IEEE Signal Processing Letters , 20(3):209–212, 2013. -->

<!-- [原子块 · verbatim] [35] Layla Oesper, Daniele Merico, Ruth Isserlin, and Gary D Bader. Wordcloud: a cytoscape plugin to create a visual semantic summary of networks. Source code for biology and medicine , 6(1):7, 2011. -->

<!-- [原子块 · verbatim] [36] OpenAI. Chatgpt (june 13 version), 2023a. Large language model. -->

<!-- [原子块 · verbatim] [37] OpenAI. Gpt-4 technical report, 2023b. -->

<!-- [原子块 · verbatim] [38] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, and Ilya Sutskever. Learning  -->

<!-- [原子块 · verbatim] [39] Christoph Schuhmann, Richard Vencu, Romain Beaumont, Robert Kaczmarczyk, Clayton Mullis, Aarush Katta, Theo Coombes, Jenia Jitsev, and Aran Komatsuzaki. Laion-400m: Open dataset of clip-filtered  -->

<!-- [原子块 · verbatim] [40] Dustin Schwenk, Apoorv Khandelwal, Christopher Clark, Kenneth Marino, and Roozbeh Mottaghi. A-okvqa: A benchmark for visual question answering using world knowledge. arXiv , 2022. -->

<!-- [原子块 · verbatim] [41] Piyush Sharma, Nan Ding, Sebastian Goodman, and Radu Soricut. Conceptual captions: A cleaned, hypernymed, image alt-text dataset for automatic image captioning. In ACL , 2018. -->

<!-- [原子块 · verbatim] [42] Shaolin Su, Qingsen Yan, Yu Zhu, Cheng Zhang, Xin Ge, Jinqiu Sun, and Yanning Zhang. Blindly assess image quality in the wild guided by a self-adaptive hyper network. In CVPR , 2020. -->

<!-- [原子块 · verbatim] [43] Shaolin Su, Vlad Hosu, Hanhe Lin, Yanning Zhang, and Dietmar Saupe. Koniq++ : Boosting no-reference image quality assessment in the wild by jointly predicting image quality and defects. In The Br -->

<!-- [原子块 · verbatim] [44] Quan Sun, Yuxin Fang, Ledell Wu, Xinlong Wang, and Yue Cao. Eva-clip: Improved training techniques for clip at scale, 2023. -->

<!-- [原子块 · verbatim] [45] InternLM Team. Internlm: A multilingual language model with progressively enhanced capabilities. https://github.com/InternLM/InternLM , 2023. -->

<!-- [原子块 · verbatim] [46] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, Aurelien Rodriguez, Armand Joulin,  -->

<!-- [原子块 · verbatim] [47] Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, Dan Bikel, Lukas Blecher, Cristian Cant -->

<!-- [原子块 · verbatim] [48] Jianyi Wang, Kelvin C. K. Chan, and Chen Change Loy. Exploring clip for assessing the look and feel of images, 2022. -->

<!-- [原子块 · verbatim] [49] Yilin Wang, Junjie Ke, Hossein Talebi, Joong Gon Yim, Neil Birkbeck, Balu Adsumilli, Peyman Milanfar, and Feng Yang. Rich features for perceptual quality assessment of ugc videos. In CVPR , pages -->

<!-- [原子块 · verbatim] [50] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc Le, and Denny Zhou. Chain-of-thought prompting elicits reasoning in large language models, 2022. -->

<!-- [原子块 · verbatim] [51] Haoning Wu, Chaofeng Chen, Jingwen Hou, Liang Liao, Annan Wang, Wenxiu Sun, Qiong Yan, and Weisi Lin. Fast-vqa: Efficient end-to-end video quality assessment with fragment sampling. In ECCV , 202 -->

<!-- [原子块 · verbatim] [52] Haoning Wu, Chaofeng Chen, Liang Liao, Jingwen Hou, Wenxiu Sun, Qiong Yan, Jinwei Gu, and Weisi Lin. Neighbourhood representative sampling for efficient end-to-end video quality assessment, 2023a -->

<!-- [原子块 · verbatim] [53] Haoning Wu, Liang Liao, Chaofeng Chen, Jingwen Hou Hou, Erli Zhang, Annan Wang, Wenxiu Sun, Qiong Yan, and Weisi Lin. Exploring opinion-unaware video quality assessment with semantic affinity cri -->

<!-- [原子块 · verbatim] [54] Haoning Wu, Liang Liao, Annan Wang, Chaofeng Chen, Jingwen Hou Hou, Erli Zhang, Wenxiu Sun Sun, Qiong Yan, and Weisi Lin. Towards robust text-prompted semantic criterion for in-the-wild video qua -->

<!-- [原子块 · verbatim] [55] Haoning Wu, Erli Zhang, Liang Liao, Chaofeng Chen, Jingwen Hou, Annan Wang, Wenxiu Sun, Qiong Yan, and Weisi Lin. Exploring video quality assessment on user generated contents from aesthetic and  -->

<!-- [原子块 · verbatim] [56] Haoning Wu, Erli Zhang, Liang Liao, Chaofeng Chen, Jingwen Hou, Annan Wang, Wenxiu Sun, Qiong Yan, and Weisi Lin. Towards explainable video quality assessment: A database and a language-prompted  -->

<!-- [原子块 · verbatim] [57] Haoning Wu, Zicheng Zhang, Erli Zhang, Chaofeng Chen, Liang Liao, Annan Wang, Chunyi Li, Wenxiu Sun, Qiong Yan, Guangtao Zhai, and Weisi Lin. Q-bench: A benchmark for general-purpose foundation m -->

<!-- [原子块 · verbatim] [58] Jiazheng Xu, Xiao Liu, Yuchen Wu, Yuxuan Tong, Qinkai Li, Ming Ding, Jie Tang, and Yuxiao Dong. Imagereward: Learning and evaluating human preferences for text-to-image generation, 2023. -->

<!-- [原子块 · verbatim] [59] Qinghao Ye, Haiyang Xu, Jiabo Ye, Ming Yan, Anwen Hu, Haowei Liu, Qi Qian, Ji Zhang, Fei Huang, and Jingren Zhou. mplug-owl2: Revolutionizing multi-modal large language model with modality collab -->

<!-- [原子块 · verbatim] [60] Zhenqiang Ying, Haoran Niu, Praful Gupta, Dhruv Mahajan, Deepti Ghadiyaram, and Alan Bovik. From patches to pictures (paq-2-piq): Mapping the perceptual space of picture quality. In CVPR , 2020. -->

<!-- [原子块 · verbatim] [61] Peter Young, Alice Lai, Micah Hodosh, and Julia Hockenmaier. From image descriptions to visual denotations: New similarity metrics for semantic inference over event descriptions. Transactions of  -->

<!-- [原子块 · verbatim] [62] Licheng Yu, Patrick Poirson, Shan Yang, Alexander C. Berg, and Tamara L. Berg. Modeling context in referring expressions, 2016. -->

<!-- [原子块 · verbatim] [63] Pan Zhang, Xiaoyi Dong, Bin Wang, Yuhang Cao, Chao Xu, Linke Ouyang, Zhiyuan Zhao, Shuangrui Ding, Songyang Zhang, Haodong Duan, Wenwei Zhang, Hang Yan, Xinyue Zhang, Wei Li, Jingwen Li, Kai Chen -->

<!-- [原子块 · verbatim] [64] Weixia Zhang, Kede Ma, Jia Yan, Dexiang Deng, and Zhou Wang. Blind image quality assessment using a deep bilinear convolutional neural network. IEEE TCSVT , 30(1):36–47, 2020. -->

<!-- [原子块 · verbatim] [65] Weixia Zhang, Guangtao Zhai, Ying Wei, Xiaokang Yang, and Kede Ma. Blind image quality assessment via vision-language correspondence: A multitask learning perspective. In IEEE Conference on Compu -->

<!-- [原子块 · verbatim] [66] Zicheng Zhang, Wei Sun, Tao Wang, Wei Lu, Quan Zhou, Qiyuan Wang, Xiongkuo Min, Guangtao Zhai, et al. Subjective and objective quality assessment for in-the-wild computer graphics images. arXiv p -->

<!-- [原子块 · verbatim] [67] Zicheng Zhang, Wei Sun, Yingjie Zhou, Haoning Wu, Chunyi Li, Xiongkuo Min, and Xiaohong Liu. Advancing zero-shot digital human quality assessment through text-prompted evaluation, 2023d. -->

<!-- [原子块 · verbatim] [68] Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric. P Xing, Hao Zhang, Joseph E. Gonzalez, and Ion Stoica. Judging llm-as- -->

**EN** Supplementary Material

**ZH** 补充材料

**EN** Appendix A Details for Data Collection

**ZH** 附录 A 数据采集细节

**EN** A.1 Interface for Subjective Experiments

**ZH** A.1 主观实验界面

**EN** The interface for the subjective experiments is built upon Gradio 3.34.0, set up locally on Ubuntu 20.04 workstations. All participants need to record their ID and write down their pathway feedbacks for a given image. The MOS for the image and possible low-level attributes are listed as reference. A screenshot of the interface is shown in Fig. 7.

**ZH** 主观实验界面基于 Gradio 3.34.0 构建，本地部署在 Ubuntu 20.04 工作站上。所有参与者需记录自己的 ID，并为给定图像写下 pathway 反馈。图像的 MOS 与可能出现的底层属性被列出作为参考。界面截图如图 7 所示。

<!-- [原子块 · img]  -->

**EN** Figure 7: The gradio interface for subjects to provide pathway feedbacks. While the quality scores (MOS) of images are available, these scores will be provided to the subjects as a reference, allowing the feedbacks to truly become explanations of these quality scores.

**ZH** 图 7：供受试者提供 pathway 反馈的 Gradio 界面。图像的质量分数（MOS）可得，这些分数将作为参考提供给受试者，使反馈真正成为对这些质量分数的解释。

**EN** A.2 Prompts for Building Q-Instruct with GPT

**ZH** A.2 用 GPT 构建 Q-Instruct 的提示词

**EN** What/How questions.

**ZH** What/How 问题。

**EN** Generate multiple question and answer pairs based on the following description of an image quality. The questions can start with ”What/Why/How”. The answer should be concise and only contain the core information with minimum words. You should also generate several false answers for each question under the key of “false candidates”, which are also reasonable given the question by contradicts with the description. Organize the output a list in JSON format and when you respond, please only output the json, no other words are needed:

**ZH** 根据以下对图像质量的描述生成多组问答对。问题可用 “What/Why/How” 开头。答案应简洁，只包含以最少词语表达的核心信息。你还应为每个问题在 “false candidates” 键下生成若干错误答案，这些答案在给定问题下同样合理，但与描述相矛盾。把输出组织为 JSON 格式的列表；回复时请只输出该 json，不需要其他文字：

**EN** Description: $DESC

**ZH** 描述：$DESC

**EN** Yes/No questions.

**ZH** 是／否问题。

**EN** Generate multiple yes-or-no question and answer pairs based on the following description of an image quality. The answer should be concise and only contain ”Yes” or ”No”. The number of questions with the answer ”Yes” should be close to the number of questions with the answer ”No”. You can also ask questions about quality issues that are not mentioned in the analysis. The answer for those unsure questions should be ”No”. Organize the output a list in JSON format and when you respond, please only output the json, no other words are needed:

**ZH** 根据以下对图像质量的描述生成多组是非问答对。答案应简洁，只包含 “Yes” 或 “No”。答案为 “Yes” 的问题数量应与答案为 “No” 的问题数量接近。你也可以就分析中未提及的质量问题提问，这类不确定问题的答案应为 “No”。把输出组织为 JSON 格式的列表；回复时请只输出该 json，不需要其他文字：

**EN** Description: $DESC

**ZH** 描述：$DESC

**EN** Extended conversations.

**ZH** 扩展对话。

**EN** Generate conversations based on the following description of quality and other low-level visual attributes of an image. These conversations can include one of the aspects in the folow 1. Examining the causes of low-level visual patterns; 2. Providing improvement suggestions on photography; 3. Providing tools to restore, enhance, or edit the image; 4. Recommending the image to respective consumers; 5. Other conversations that may happen given the descriptions. Remember to be relevant to the image. Organize the output a list in JSON format (interleaved with ”query” and ”response” keys for each conversation) and when you respond, please only output the json, no other words are needed:

**ZH** 根据以下对图像质量及其他底层视觉属性的描述生成对话。这些对话可涵盖以下方面之一：1. 检视底层视觉模式的成因；2. 给出摄影方面的改进建议；3. 提供可用于复原、增强或编辑图像的工具；4. 把该图像推荐给相应的受众；5. 在给定描述下可能发生的其他对话。记得要与图像相关。把输出组织为 JSON 格式列表（每段对话以 “query” 与 “response” 键交错排列）；回复时请只输出该 json，不需要其他文字：

**EN** Description: $DESC

**ZH** 描述：$DESC

**EN** Appendix B Hyper-parameters during Training

**ZH** 附录 B 训练超参数

**EN** Hyper-parameters for LLaVA-v1.5.

**ZH** LLaVA-v1.5 的超参数。

**EN** The low-level visual instruction tuning for LLaVA-v1.5 (7B/13B) is conducted with 8 NVIDIA A100-SMX4-80GB GPU (requiring 16 hours for 7B, 22 hours for 13B, for the mix version). We record all hyper-parameters in Tab. 10.

**ZH** 对 LLaVA-v1.5（7B/13B）的底层视觉指令微调使用 8 块 NVIDIA A100-SMX4-80GB GPU（混合版 7B 需 16 小时，13B 需 22 小时）。全部超参数记录于表 10。

<!-- [原子块 · table] Hyper-parameter mix with high-level after high-level ViT init. CLIP-L/14-336 [ 38 ] LLM init. Vicuna-v1.5 [ 68 ] LLaVA-v1.5 image resolution 336 × 336 336\times 336 336 × 336 336\times 336 group modal -->

**EN** Table 10: Hyper-parameters of low-level visual instruction tuning on LLaVA-v1.5 (7B/13B), the same as original LLaVA-v1.5.

**ZH** 表 10：LLaVA-v1.5（7B/13B）上底层视觉指令微调的超参数，与原版 LLaVA-v1.5 相同。

**EN** Hyper-parameters for mPLUG-Owl-2.

**ZH** mPLUG-Owl-2 的超参数。

**EN** The low-level visual instruction tuning for mPLUG-Owl-2 is conducted with 32 NVIDIA A100-SMX4-80GB GPU (requiring 8 hours for the mix version). Hyper-parameters in Tab. 11.

**ZH** 对 mPLUG-Owl-2 的底层视觉指令微调使用 32 块 NVIDIA A100-SMX4-80GB GPU（混合版需 8 小时）。超参数见表 11。

<!-- [原子块 · table] Hyper-parameter mix with high-level after high-level ViT init. Pre-train stage (updated CLIP-L/14 [ 38 ] ) LLM init. LLaMA-2 [ 47 ] visual abstractor init. Pre-train stage mPLUG-Owl-2 image resolution -->

**EN** Table 11: Hyper-parameters of low-level visual instruction tuning on mPLUG-Owl-2, the same as the original model.

**ZH** 表 11：mPLUG-Owl-2 上底层视觉指令微调的超参数，与原模型相同。

**EN** Hyper-parameters for InternLM-XComposer-VL.

**ZH** InternLM-XComposer-VL 的超参数。

**EN** Similar as mPLUG-Owl-2, the low-level visual instruction tuning for InternLM-XComposer-VL is conducted with 32 NVIDIA A100-SMX4-80GB GPU (requiring 13 hours for the mix version). Hyper-parameters are listed in Tab. 12.

**ZH** 与 mPLUG-Owl-2 类似，对 InternLM-XComposer-VL 的底层视觉指令微调使用 32 块 NVIDIA A100-SMX4-80GB GPU（混合版需 13 小时）。超参数列于表 12。

<!-- [原子块 · table] Hyper-parameter mix with high-level after high-level ViT init. EVA-CLIP-G [ 44 ] LLM init. Pre-train stage InternLM-XComposer-VL perceive sampler init. Pre-train stage InternLM-XComposer-VL image reso -->

**EN** Table 12: Hyper-parameters of low-level visual instruction tuning on InternLM-XComposer-VL, the same as the original model.

**ZH** 表 12：InternLM-XComposer-VL 上底层视觉指令微调的超参数，与原模型相同。

**EN** Appendix C Evaluation Details

**ZH** 附录 C 评测细节

**EN** C.1 Prompt Settings on (A1) Perception (via MCQ)

**ZH** C.1 (A1) 感知（经 MCQ）的提示设置

**EN** Denote the image tokens as <image>, the question as <QUESTION>, choices as <CHOICEi>, the prompt settings for different models on answering Multi-Choice Questions (MCQ) are slightly different, listed as follows. To ensure optimal results, during training, we also transform the VQA subset under the same settings, respectively.

**ZH** 记图像词元为 <image>，问题为 <QUESTION>，选项为 <CHOICEi>，不同模型在回答多选题（MCQ）时的提示设置略有差异，列举如下。为获得最优结果，训练时我们也分别按相同设置对 VQA 子集作转换。

<!-- [原子块 · img]  -->

**EN** Figure 8: Qualitative Analysis (I): A multi-turn conversation that the user subsequently queries the Q-Instruct-tuned MLLM on (1) rating image quality, (2) reasoning the rating, (3) providing improvement suggestions, and (4) discerning the most important suggestion.

**ZH** 图 8：定性分析（I）：一段多轮对话，用户依次向经 Q-Instruct 微调的 MLLM 询问 (1) 给图像质量打分、(2) 解释打分的理由、(3) 给出改进建议、(4) 判别最重要的建议。

<!-- [原子块 · img]  -->

**EN** Figure 9: Qualitative Analysis (II): The Q-Instruct-tuned MLLM can serve as a multi-purpose (overall quality or specific distortion) and multi-format (text, good/average/poor or numerical, e.g. 1/2/3/4/5) quality evaluator.

**ZH** 图 9：定性分析（II）：经 Q-Instruct 微调的 MLLM 可作为多用途（总体质量或特定失真）、多格式（文本、good/average/poor 或数值，如 1/2/3/4/5）的质量评价器。

**EN** Prompt Settings for LLaVA-v1.5 (7B/13B).

**ZH** LLaVA-v1.5（7B/13B）的提示设置。

**EN** A chat between a curious human and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the human’s questions. USER:<image> <QUESTION> Answer with the option’s letter from the given choices directly. A. <CHOICEA> B. <CHOICEB> C. <CHOICEC> ASSISTANT:

**ZH** 一段好奇的人类与人工智能助手之间的对话。助手对人类的问题给出有帮助、详细且礼貌的回答。USER：<image> <QUESTION> 直接用给定选项的字母作答。A. <CHOICEA> B. <CHOICEB> C. <CHOICEC> ASSISTANT：

**EN** Prompt Settings for mPLUG-Owl-2.

**ZH** mPLUG-Owl-2 的提示设置。

**EN** USER: <image> <QUESTION> Answer with the option’s letter from the given choices directly. A. <CHOICEA> B. <CHOICEB> C. <CHOICEC> ASSISTANT:

**ZH** USER：<image> <QUESTION> 直接用给定选项的字母作答。A. <CHOICEA> B. <CHOICEB> C. <CHOICEC> ASSISTANT：

**EN** Prompt Settings for InternLM-XComposer-VL.

**ZH** InternLM-XComposer-VL 的提示设置。

**EN** <|User|>: <image>Please answer this question by choosing the correct choice.Context: N/A Question: <QUESTION> Options: A. <CHOICEA> B. <CHOICEB> C. <CHOICEC> <TOKENS_UNUSED_0> <|Bot|>: Answer: The answer is

**ZH** <|User|>: <image>请从给定选项中选择正确答案来回答该问题。Context: N/A Question: <QUESTION> Options: A. <CHOICEA> B. <CHOICEB> C. <CHOICEC> <TOKENS_UNUSED_0> <|Bot|>: Answer: The answer is

**EN** C.2 Prompt Setting on (A2) Description

**ZH** C.2 (A2) 描述的提示设置

**EN** For the (A2) Description task, we unify all models under the same prompt: “Describe and evaluate the quality of the image.”, as this is the only prompt that can effectively allow every base model to describe low-level visual attributes and then evaluate image quality. For the alternate prompt as shown in Fig. 1, “Rate the quality of the image. Think step by step.”, the base InternLM-XComposer-VL only provides numbers (1/2/3/4/5) without explanations or reasonings. Therefore, we choose the current prompt to evaluate the description ability among all variants.

**ZH** 对于 (A2) 描述任务，我们把所有模型统一在同一个提示下：“描述并评价该图像的质量。”，因为这是唯一能有效让每个基座模型先描述底层视觉属性、再评价图像质量的提示。若改用图 1 所示的备选提示“给图像质量打分。逐步思考。”，基座 InternLM-XComposer-VL 只给出数字（1/2/3/4/5），不含任何解释或推理。因此我们选用当前提示来评测各变体的描述能力。

**EN** C.3 Prompt Setting on (A3) Assessment

**ZH** C.3 (A3) 评价的提示设置

**EN** For the (A3) Quality Assessment task, we follow the strategy as proposed by Q-Bench [57], with the softmax output between good and poor to collect better quantifiable scores for images, under the first output token of MLLMs:

**ZH** 对于 (A3) 质量评价任务，我们沿用 Q-Bench [57] 提出的策略，在 MLLM 的首个输出词元上取 good 与 poor 之间的 softmax 输出，以收集更可量化的图像分数：

<!-- [原子块 · table] q pred = e x SCORE_TOKEN good e x SCORE_TOKEN good + e x SCORE_TOKEN poor q_{\mathrm{pred}}=\frac{e^{x^{\text{{good}}}_{\textit{SCORE\_TOKEN}}}}{e^{x^{\text{{good}}}_{\textit{SCORE\_TOKEN}}}+e^{x^{\te -->

**EN** For KoNViD-1k, the video quality assessment dataset as evaluated, we sample one frame per second (the same as NIQE [34]), and average the image quality scores as calculated by Eq. 1 among frames. While we acknowledge that this is not the optimal strategy for evaluating video quality, the excellent results in Tab. 6 already significantly outperform all methods that are not trained for video quality assessment, suggesting that if better strategies are adopted, MLLMs can do even better on video quality assessment.

**ZH** 对于所评测的视频质量数据集 KoNViD-1k，我们每秒采样一帧（与 NIQE [34] 相同），并对各帧按式 1 计算出的图像质量分数取平均。我们承认这并非评测视频质量的最优策略，但表 6 中的出色结果已显著超越所有未针对视频质量评价训练的方法，说明若采用更好的策略，MLLM 在视频质量评价上还能做得更好。

**EN** Appendix D Qualitative Analyses

**ZH** 附录 D 定性分析

**EN** Considering that different base MLLMs reach similar performance after low-level visual instruction tuning, we build a publicly-accessible demo for Q-Instruct-mPLUG-Owl-2 under the mix strategy, and invite our team members to really chat with it. These conversations exhibit its exellent abilities on various scenraios, including multi-turn queries (Fig. 8), multi-purpose assessment (Fig. 9), correction (Fig. 10), and local in-context perception (Fig. 11).

**ZH** 考虑到不同基座 MLLM 经底层视觉指令微调后达到相近的性能，我们为混合策略下的 Q-Instruct-mPLUG-Owl-2 搭建了一个公开可访问的 demo，并邀请团队成员与它真实对话。这些对话展示了它在多种场景下的出色能力，包括多轮提问（图 8）、多用途评价（图 9）、纠正（图 10）与局部上下文感知（图 11）。

<!-- [原子块 · img]  -->

**EN** Figure 10: Qualitative Analysis (III): The Q-Instruct-tuned MLLM can correct itself based on further instructions. While provided with additional context (i.e. background bokeh is intentional), it can modify its rating to align with the context.

**ZH** 图 10：定性分析（III）：经 Q-Instruct 微调的 MLLM 能依据后续指令自我纠正。当获得额外上下文（例如背景虚化是有意为之）时，它能修改自己的评分以与该上下文一致。

<!-- [原子块 · img]  -->

**EN** (a) A strong contrast image.

**ZH** (a) 一张强对比度图像。

<!-- [原子块 · img]  -->

**EN** (b) A partly in-focus image.

**ZH** (b) 一张部分对焦的图像。

**EN** Figure 11: Qualitative Analysis (IV): Local in-context low-level perceptual abilities of Q-Instruct-tuned MLLMs. They can effectively discern the bright part and dark part in a strong contrast image (a), or the clarity of different objects/areas in a partly in-focus image (b).

**ZH** 图 11：定性分析（IV）：经 Q-Instruct 微调的 MLLM 的局部上下文底层感知能力。它们能有效判别强对比度图像中的亮部与暗部（a），或部分对焦图像中不同对象／区域的清晰度（b）。

**EN** Appendix E Limitations

**ZH** 附录 E 局限性

**EN** The known limitations of our studies are as follows. First, though with improved quality assessment and low-level visual perception abilities, the Q-Instruct-tuned models have witnessed declined performance on general-purpose tasks, especially language-centric tasks, or tasks that require heavy reasoning abilities. Therefore, they may produce unwanted outputs if applied to tasks other than low-level visual perception and understanding. Second, though with improved accuracy, the Q-Instruct-tuned models still perform worse (68%-71% accuracy on LLVisionQA-test) than an average human (about 74%), and may not yet be able to directly replace human on low-level related tasks. Thirdly, the Q-Instruct dataset mainly consists of natural in-the-wild images. Though they prove excellent generalization on other types of visual contents, the performance might still be improveable if further tuned on these datasets.

**ZH** 本研究已知的局限如下。其一，尽管质量评价与底层视觉感知能力有所提升，经 Q-Instruct 微调的模型在通用任务上性能出现下降，尤其是以语言为中心的任务或需要重度推理的任务。因此，若应用于底层视觉感知与理解之外的任务，它们可能产生不合意的输出。其二，尽管准确率提升，经 Q-Instruct 微调的模型（在 LLVisionQA-test 上为 68%–71% 的准确率）仍低于普通人类（约 74%），尚不足以在底层相关任务上直接替代人类。其三，Q-Instruct 数据集主要由自然真实场景图像构成。尽管它们在其他类型的视觉内容上证明了出色的泛化能力，若在这些数据集上进一步微调，性能仍可能继续提升。

**EN** Appendix F Ethical Acknowledgements

**ZH** 附录 F 伦理声明

**EN** In our study, all participants were fully informed about the nature and amount of the tasks involved prior to their participation. No uncomfortable content was reported during this process. We express our gratitude to the participants for their valuable contributions, which were essential to the success of our research. We commit to upholding all ethical standards to ensure the well-being of our participants, as well as the integrity of our research findings.

**ZH** 在本研究中，所有参与者在参与前均已充分知晓所涉任务的性质与工作量。过程中未报告任何令人不适的内容。我们感谢参与者的宝贵贡献，它们对本研究取得成功不可或缺。我们承诺恪守一切伦理规范，以保障参与者的福祉以及研究发现的正当性。

**EN** Appendix G Acknowledgements

**ZH** 附录 G 致谢

**EN** Our team would like to sincerely thank Qinghao Ye and Xiaoyi Dong for providing pre-trained weights of mPLUG-Owl-2 and InternLM-XComposer-VL after the low-level visual instruction tuning, including a complete training recipe on their respective high-level datasets mixed with the Q-Instruct. We believe these weights will significantly contribute to the open-source community working on tasks related to low-level visual perception and understanding.

**ZH** 本团队诚挚感谢 Qinghao Ye 与 Xiaoyi Dong 提供了 mPLUG-Owl-2 与 InternLM-XComposer-VL 经底层视觉指令微调后的预训练权重，包括在各自高层数据集与 Q-Instruct 混合后的完整训练配方。我们相信这些权重将为从事底层视觉感知与理解相关任务的开源社区作出重要贡献。

**EN** Appendix H License

**ZH** 附录 H 许可

**EN** Researchers and open-source developers are free to use the Q-Instruct dataset and the fine-tuned weights as provided for the four MLLMs. We also allow commercial use, while any commercial use should be pre-permitted by our team. Any usage should also comply with licenses of the original base models (inc. base LLMs such as Vicuna, LLaMA-2).

**ZH** 研究者与开源开发者可自由使用所提供的 Q-Instruct 数据集以及四个 MLLM 的微调权重。我们也允许商业使用，但任何商业用途须事先获得本团队许可。任何使用还须遵守原始基座模型（含 Vicuna、LLaMA-2 等基座 LLM）的许可协议。
