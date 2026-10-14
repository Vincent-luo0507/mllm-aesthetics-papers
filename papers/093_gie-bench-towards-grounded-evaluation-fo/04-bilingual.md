# GIE-Bench：面向文本引导图像编辑的有依据评测

> 原标题：GIE-Bench: Towards Grounded Evaluation for Text-Guided Image Editing
> 作者：Yusu Qian, Jiasen Lu, Tsu-Jui Fu, Xinze Wang, Chen Chen, Yinfei Yang, Wenze Hu, Zhe Gan · arXiv:2505.11493 · 2025-05-16

<!-- [原子块 · verbatim] GIE-Bench: Towards Grounded Evaluation for Text-Guided Image Editing -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] Editing images using natural language instructions has become a natural and expressive way to modify visual content; yet, evaluating the performance of such models remains challenging. Existing evalua -->

<!-- [原子块 · img]  -->

**EN** Figure 1: Overview of the proposed GIE-Bench pipeline for grounded and fine-grained evaluation of text-guided image editing models. GIE-Bench consists of two components: (⟦SLOT_0⟧) functional correctness evaluation; and (⟦SLOT_1⟧) content preservation evaluation.

**ZH** 图 1：本文提出的 GIE-Bench 流程概览，用于对文本引导的图像编辑模型做有依据的细粒度评测。GIE-Bench 由两部分组成：（⟦SLOT_0⟧）功能正确性评测；（⟦SLOT_1⟧）内容保持评测。

**EN** 1 Introduction

**ZH** 1 引言

**EN** Text-guided image editing has become a powerful and accessible way for users to modify images by simply describing the desired change in natural language, eliminating the need for complex tools or interfaces. Recent advances in diffusion models and multimodal large language models (MLLMs) have significantly improved the visual quality and instruction-following capability of these systems. Among them, GPT-Image-1 (gptimage1), a recently released model from OpenAI, has gained significant attention for its impressive performance in image editing. However, fine-grained evaluation of its editing performance remains limited.

**ZH** 用户只需用自然语言描述期望的改动即可修改图像，文本引导的图像编辑因此成为一种强大且易用的方式，免去了复杂工具或界面的需要。扩散模型与多模态大语言模型（MLLM）的近期进展显著提升了这类系统的视觉质量与指令遵循能力。其中，OpenAI 近期发布的 GPT-Image-1（gptimage1）因在图像编辑上的亮眼表现而备受关注。然而，针对其编辑性能的细粒度评测仍然有限。

**EN** Most prior works evaluate text-guided image editing performance using CLIP-based (radford2021learningtransferablevisualmodels) similarity metrics or human preference scores. While useful, these approaches have key limitations. CLIP similarity offers only global alignment and does not reflect whether a model correctly executed the intended semantic change. Human evaluations, on the other hand, are costly, non-reproducible, and difficult to scale across thousands of examples.

**ZH** 此前多数工作使用基于 CLIP（radford2021learningtransferablevisualmodels）的相似度指标或人类偏好分数来评测文本引导的图像编辑。这些方法虽有作用，却存在关键局限。CLIP 相似度只提供全局层面的对齐，无法反映模型是否正确执行了预期的语义改动。人工评测则成本高、不可复现，且难以扩展到上千个样本。

**EN** To address this gap, we introduce GIE-Bench,11 1 short for Grounded Image Editing Evaluation Benchmark. Benchmark data and evaluation code will be released soon. a new benchmark for evaluating text-guided image editing in a grounded manner, with precise and interpretable metrics. Our evaluation framework is twofold: (⟦SLOT_2⟧) functional correctness evaluation, and (⟦SLOT_3⟧) content preservation evaluation.

**ZH** 为填补这一空缺，我们提出 GIE-Bench，11 1 即 Grounded Image Editing Evaluation Benchmark 的简称。基准数据与评测代码将很快发布。它以有依据的方式、用精确且可解释的指标评测文本引导的图像编辑。我们的评测框架是双轴的：（⟦SLOT_2⟧）功能正确性评测；（⟦SLOT_3⟧）内容保持评测。

**EN** First, we assess functional correctness using a VQA-style protocol. For each edit, we formulate a multiple-choice question grounded in the edited image, designed to verify whether the intended semantic change was applied. Unlike previous VQA-style evaluations that use binary yes/no questions (e.g., in I2E-Bench (ma2024i2ebench)), our multiple-choice format includes two to five answer options, increasing the difficulty and reducing the chance of success by guessing. This enables automatic, objective, and more grounded assessment of instruction execution.

**ZH** 第一，我们用 VQA 式的协议评估功能正确性。对每一条编辑，我们围绕编辑后的图像设计一道选择题，用于验证预期的语义改动是否被施加。此前的 VQA 式评测多采用二元的「是/否」问题（例如 I2E-Bench（ma2024i2ebench）），而我们的选择题形式提供 2 至 5 个选项，提高了难度，也降低了猜对的概率，从而实现对指令执行的自动、客观且更有依据的评估。

**EN** Second, we evaluate image content preservation, the model’s ability to leave irrelevant areas of the image unchanged. Unlike prior work that applies global similarity metrics, we introduce an object-aware preservation score. Our benchmark provides masks for edited objects and computes similarity over the remaining area that is intended to be left untouched. This localized approach yields more sensitive and precise measurement of unintended changes.

**ZH** 第二，我们评估图像内容的保持性，即模型让图像中无关区域保持不变的能力。此前工作采用全局相似度指标，我们则引入对象感知的保持分数。本基准为被编辑对象提供掩码，并在本应保持不变的其余区域上计算相似度。这种局部化的方法能更灵敏、更精确地度量非预期的改动。

**EN** To support robust evaluation, our benchmark covers over 800 diverse images across 20 categories (e.g., human faces, animals, architecture, text, cartoon, art, food, and electronics), with over 1000 editing tasks spanning 9 functional edit types. Each sample includes natural language instructions, edit type metadata, object masks, a multiple-choice question for functional correctness evaluation, and human-annotated ground truth.

**ZH** 为支撑稳健的评测，本基准覆盖 20 个类别（如人脸、动物、建筑、文字、卡通、艺术、食物与电子产品）下 800 余张多样化图像，包含 9 类功能性编辑类型、共 1000 余项编辑任务。每个样本都含自然语言指令、编辑类型元数据、对象掩码、一道用于功能正确性评测的选择题，以及人工标注的真值。

**EN** Finally, we benchmark and compare a wide array of state-of-the-art image editing models, including MGIE (fu2024mgie), OmniGen (xiao2024omnigenunifiedimagegeneration), and the most recent GPT-Image-1 (gptimage1). Our results highlight GPT-Image-1’s strong performance in functional correctness, while also revealing its tendency to over-edit irrelevant regions, as captured by our preservation metrics.

**ZH** 最后，我们对一系列先进的图像编辑模型做基准比较，包括 MGIE（fu2024mgie）、OmniGen（xiao2024omnigenunifiedimagegeneration），以及最新的 GPT-Image-1（gptimage1）。结果显示，GPT-Image-1 在功能正确性上表现强劲，同时也暴露出它过度编辑无关区域的倾向——这一点正由我们的保持类指标捕捉到。

**EN** Our contributions are summarized as follows.

**ZH** 本文的贡献概括如下。

**EN** • A high-quality image editing benchmark covering diverse domains and instruction types;

**ZH** • 一个覆盖多样领域与指令类型的高质量图像编辑基准；

**EN** • A precise, fully automated evaluation protocol using VQA-style questions and object-aware masking to assess both functional correctness and preservation;

**ZH** • 一套精确、全自动的评测协议：用 VQA 式问题与对象感知掩码同时评估功能正确性与内容保持；

**EN** • A standardized empirical comparison of leading image editing models, with a detailed focus on GPT-Image-1’s strengths and weaknesses.

**ZH** • 一份对主流图像编辑模型的标准化实证比较，其中细致剖析了 GPT-Image-1 的优势与不足。

<!-- [原子块 · table] Benchmark Instruction Eval Preserv. Eval Mask Usage in Eval Edit Types Covered I2E-Bench ( ma2024i2ebench ) ✓(VQA) ✗ ✗ Diverse IE-Bench ( sun2025iebenchadvancingmeasurementtextdriven ) ✓(Human-rated)  -->

**EN** Table 1: Comparison of text-guided image editing evaluation benchmarks. Our benchmark uniquely evaluates both functional correctness and content preservation with precise mask-based protocols.

**ZH** 表 1：文本引导图像编辑评测基准的对比。本基准独到之处在于，用基于掩码的精确协议同时评估功能正确性与内容保持。

**EN** 2 Related Work

**ZH** 2 相关工作

**EN** Text-Guided Image Editing. Early methods such as Prompt2Prompt (hertz2022prompttopromptimageeditingcross) and Imagic (Kawar_2023) introduced ways to edit images with text prompts by modifying either the attention layers or the latent space of diffusion models. DiffEdit (couairon2022diffeditdiffusionbasedsemanticimage) further refined image editing by detecting editable regions and generating masks. Text-guided image editing models have since emerged to simplify user interaction by directly following natural language instructions. InstructPix2Pix (Brooks_2023) fine-tuned diffusion models on synthetic image editing pairs guided by instructions. More recent models xiao2024omnigenunifiedimagegeneration; geng2023instructdiffusiongeneralistmodelinginterface; fu2024mgie; fu2025univg; le2024diffusiongenerate; Zhang2023MagicBrush; huang2023smarteditexploringcomplexinstructionbased; li2024instructany2pixflexiblevisualediting; lin2024textdrivenimageeditinglearnable; meng2024instructgiegeneralizableimageediting; han2024styleboothimagestyleediting; li2024zonezeroshotinstructionguidedlocal; guo2023focusinstructionfinegrainedmultiinstruction; santos2024leveragingllmsontheflyinstruction; zhao2024instructbrushlearningattentionbasedinstruction have advanced the semantic and compositional understanding of edits. InstructAny2Pix (li2024instructany2pixflexiblevisualediting) uses multimodal inputs (e.g., audio, image) for editing guidance. SmartEdit (huang2023smarteditexploringcomplexinstructionbased) focuses on complex scenes and incorporates MLLMs for better instruction comprehension. MGIE (fu2024mgie) learns to derive expressive instructions from user input and provides explicit guided visual editing. Most recently, OneDiffusion (le2024diffusiongenerate) and UniVG (fu2025univg) presents generalist diffusion models for unified image generation and editing.

**ZH** 文本引导的图像编辑。早期方法如 Prompt2Prompt（hertz2022prompttopromptimageeditingcross）与 Imagic（Kawar_2023）通过修改扩散模型的注意力层或潜空间，实现了用文本提示编辑图像。DiffEdit（couairon2022diffeditdiffusionbasedsemanticimage）通过检测可编辑区域并生成掩码，进一步改进了图像编辑。此后出现了直接遵循自然语言指令、以简化用户交互为目标的文本引导图像编辑模型。InstructPix2Pix（Brooks_2023）在指令引导的合成图像编辑对上对扩散模型做微调。更近期的工作 xiao2024omnigenunifiedimagegeneration; geng2023instructdiffusiongeneralistmodelinginterface; fu2024mgie; fu2025univg; le2024diffusiongenerate; Zhang2023MagicBrush; huang2023smarteditexploringcomplexinstructionbased; li2024instructany2pixflexiblevisualediting; lin2024textdrivenimageeditinglearnable; meng2024instructgiegeneralizableimageediting; han2024styleboothimagestyleediting; li2024zonezeroshotinstructionguidedlocal; guo2023focusinstructionfinegrainedmultiinstruction; santos2024leveragingllmsontheflyinstruction; zhao2024instructbrushlearningattentionbasedinstruction 推进了对编辑的语义与构图理解。InstructAny2Pix（li2024instructany2pixflexiblevisualediting）用多模态输入（如音频、图像）指导编辑。SmartEdit（huang2023smarteditexploringcomplexinstructionbased）聚焦复杂场景，并引入 MLLM 以更好地理解指令。MGIE（fu2024mgie）学习从用户输入中推导出富有表现力的指令，并提供显式的引导式视觉编辑。最近的 OneDiffusion（le2024diffusiongenerate）与 UniVG（fu2025univg）则提出了面向统一图像生成与编辑的通用扩散模型。

**EN** Benchmarks for Text-Guided Image Editing. To address the need for image editing evaluation, several benchmarks basu2023editvalbenchmarkingdiffusionbased; ma2024i2ebench; sun2025iebenchadvancingmeasurementtextdriven; couairon2022diffeditdiffusionbasedsemanticimage have been proposed. EditVal (basu2023editvalbenchmarkingdiffusionbased) assesses the fidelity of generated images across various edit types. It evaluates models based on their ability to perform specific attribute edits. I2E-Bench (ma2024i2ebench) emphasizes human perception alignment. IE-Bench (sun2025iebenchadvancingmeasurementtextdriven) introduces a database containing diverse source images, editing prompts, and results from different editing methods, along with Mean Opinion Scores from human subjects. These benchmarks have advanced image editing evaluation, but often focus on either high-level text-image alignment or human perceptual scores without integrating functional correctness and content preservation in a unified framework. More related work on text-to-image generation benchmarks is provided in Appendix A.1.

**ZH** 文本引导图像编辑的基准。为满足图像编辑评测的需求，已有若干基准被提出 basu2023editvalbenchmarkingdiffusionbased; ma2024i2ebench; sun2025iebenchadvancingmeasurementtextdriven; couairon2022diffeditdiffusionbasedsemanticimage。EditVal（basu2023editvalbenchmarkingdiffusionbased）评估生成图像在各类编辑类型上的保真度，依据模型执行特定属性编辑的能力来打分。I2E-Bench（ma2024i2ebench）强调与人类感知的对齐。IE-Bench（sun2025iebenchadvancingmeasurementtextdriven）构建了一个包含多样源图像、编辑提示以及不同编辑方法结果的数据库，并附带来自人类被试的平均意见分。这些基准推动了图像编辑评测的发展，但往往只关注高层级的图文对齐或人类感知分数，未把功能正确性与内容保持整合进统一框架。关于文本到图像生成基准的更多相关工作见附录 A.1。

**EN** Evaluation of Content Preservation. Evaluating content preservation is crucial to ensure that edits are confined to specified regions without unintended alterations. Traditional preservation metrics that compute CLIP (radford2021learningtransferablevisualmodels) similarity over the entire image are flawed because they conflate intended edits with unintended changes, failing to isolate regions that should remain untouched.

**ZH** 内容保持的评测。评估内容保持对确保编辑被限定在指定区域内、不产生非预期改动至关重要。传统的保持指标在整幅图像上计算 CLIP（radford2021learningtransferablevisualmodels）相似度，这种做法有缺陷：它把预期编辑与非预期改动混为一谈，无法分离出本应保持原样的区域。

**EN** Evaluation of Functional Correctness via VQA. Incorporating VQA into image editing evaluation offers a promising avenue for assessing functional correctness. By formulating the evaluation as a VQA task, models can be tested on their understanding of the edits in relation to the instructions. For example, TIFA (hu2023tifaaccurateinterpretabletexttoimage) and Davidsonian Scene Graph (cho2024davidsonianscenegraphimproving) use VQA-based approaches to evaluate fine-grained alignment between text and images. I2E-Bench (ma2024i2ebench) also adopts a VQA-style evaluation by generating binary (yes/no) questions that query whether a particular edit was made. While effective, such binary formulations may oversimplify the evaluation and are easier to answer by chance. In contrast, our benchmark formulates each evaluation as a multiple-choice question with 2–5 carefully constructed options, requiring more nuanced reasoning and disambiguation.

**ZH** 通过 VQA 评估功能正确性。把视觉问答引入图像编辑评测，为评估功能正确性提供了一条可行途径。把评测形式化为一个 VQA 任务，就能检验模型对编辑与指令之间关系的理解。例如，TIFA（hu2023tifaaccurateinterpretabletexttoimage）与 Davidsonian Scene Graph（cho2024davidsonianscenegraphimproving）用基于 VQA 的方法评估文本与图像之间的细粒度对齐。I2E-Bench（ma2024i2ebench）也采用 VQA 式评测，生成二元（是/否）问题来询问某项编辑是否已完成。这种方法虽有效，二元形式却可能过度简化评测，也更容易凭偶然猜中。相比之下，本基准把每项评测构造成含 2–5 个精心构造选项的选择题，要求更细致的推理与消歧。

**EN** Our Contributions. As shown in Table 1, most image editing benchmarks do not precisely evaluate whether the background is preserved while assessing instruction correctness. The use of segmentation masks to precisely isolate editable and non-editable regions is largely absent from these prior works.

**ZH** 本文的贡献。如表 1 所示，多数图像编辑基准在评估指令正确性的同时，并未精确评估背景是否得以保持。用分割掩码精确隔离可编辑区域与不可编辑区域，在这些前人工作中基本缺失。

**EN** GIE-Bench addresses these gaps by providing: (⟦SLOT_4⟧) precise preservation evaluation by separating areas intended to edit from areas not intended to be edited by providing object masks, (⟦SLOT_5⟧) VQA-style multiple-choice questions to assess edits without requiring access to the original instruction. The dual-axis evaluation of GIE-Bench enables us to differentiate between models that make accurate edits but introduce unnecessary changes, and those that preserve image integrity but fail to satisfy the instruction. Our use of automated, mask-aware metrics makes our benchmark uniquely suited for large-scale, fine-grained evaluation of instruction following behavior in image editing models.

**ZH** GIE-Bench 通过以下两点填补这些空缺：（⟦SLOT_4⟧）提供对象掩码，把打算编辑的区域与不打算编辑的区域分开，实现精确的内容保持评测；（⟦SLOT_5⟧）采用 VQA 式选择题评估编辑，且无需访问原始指令。GIE-Bench 的双轴评测使我们能够区分两类模型：一类做出了准确的编辑却引入不必要的改动，另一类保持了图像完整性却未能满足指令。我们所采用的自动化、掩码感知指标，使本基准特别适合对图像编辑模型的指令遵循行为做大规模、细粒度的评测。

**EN** 3 Benchmark Construction

**ZH** 3 基准构建

**EN** 3.1 Dataset Collection

**ZH** 3.1 数据采集

<!-- [原子块 · img]  -->

**EN** Figure 2: Example image editing instructions and edited results by GPT-Image-1 (gptimage1), OmniGen (xiao2024omnigenunifiedimagegeneration), and MGIE (fu2024mgie).

**ZH** 图 2：GPT-Image-1（gptimage1）、OmniGen（xiao2024omnigenunifiedimagegeneration）与 MGIE（fu2024mgie）的图像编辑指令与编辑结果示例。

**EN** Source of Images. To ensure diversity in visual content and evaluate text-based image editing across a wide range of domains, we hand-selected 2000 images from Pexels, a repository of high-quality, royalty-free images. The images are of various resolution. They are evenly distributed across 20 distinct categories, with 100 images per category. These categories span a broad spectrum of real-world and synthetic visual content.

**ZH** 图像来源。为保证视觉内容的多样性，并在广泛的领域上评测基于文本的图像编辑，我们从 Pexels（一个高质量、免版税图像库）中人工挑选了 2000 张图像。图像分辨率各异，均匀分布在 20 个不同类别上，每类 100 张。这些类别覆盖了真实与合成视觉内容的广泛谱系。

**EN** The selected categories are: (⟦SLOT_6⟧) Objects & Environments: furniture, architecture, electronics, home appliance, city, nature, plant; (⟦SLOT_7⟧) People & Clothing: human, human face, cloth, accessories, jewellery; (⟦SLOT_8⟧) Animals & Creatures: animal, cartoon; (⟦SLOT_9⟧) Food & Lifestyle: food, musical instrument, art; (⟦SLOT_10⟧) Text & Symbols: text, sign; (⟦SLOT_11⟧) Vehicles: transportation. This collection was curated to represent both structured and unstructured scenes, photographic and illustrated styles, and static and dynamic subjects.

**ZH** 所选类别为：（⟦SLOT_6⟧）物体与环境：家具、建筑、电子产品、家用电器、城市、自然、植物；（⟦SLOT_7⟧）人物与服饰：人、人脸、衣物、配饰、珠宝；（⟦SLOT_8⟧）动物与生物：动物、卡通；（⟦SLOT_9⟧）食物与生活方式：食物、乐器、艺术；（⟦SLOT_10⟧）文字与符号：文字、标识；（⟦SLOT_11⟧）交通工具：交通运输。该集合的挑选兼顾了结构化与非结构化场景、摄影与插画风格，以及静态与动态主体。

**EN** Generation of Editing Instructions. Each image in our dataset is randomly paired with 3 editing tasks, from the 9 editing types: Color Change, Add Object, Remove Object, Attribute Change, Object Replacement, Layout Modification, Scene/Background Change, Size Change, and Textual Edit (only for images containing text). This variety is designed to comprehensively evaluate an image editing model’s ability to handle both low-level appearance modifications and high-level semantic changes. We then prompt GPT-4o to generate edit instructions based on the image and edit type. We provide the detailed prompt in Appendix A.3. Figure 2 shows 4 examples of editing instructions and edited results.

**ZH** 编辑指令的生成。数据集中每张图像随机搭配 3 项编辑任务，取自 9 种编辑类型：颜色更改、添加物体、移除物体、属性更改、物体替换、布局修改、场景/背景更改、尺寸更改与文字编辑（仅适用于含文字的图像）。这种多样性意在全面考察图像编辑模型处理低层外观修改与高层语义改动的能力。我们随后提示 GPT-4o 依据图像与编辑类型生成编辑指令，详细提示见附录 A.3。图 2 给出 4 组编辑指令与编辑结果的示例。

**EN** 3.2 Generation of Multiple-Choice Questions for Functional Correctness Evaluation

**ZH** 3.2 面向功能正确性评测的选择题生成

**EN** To assess whether a model has correctly executed a given instruction, we introduce a VQA-style evaluation framework focused on functional correctness. For each instruction-image pair, GPT-4o generates a multiple-choice question that can only be answered correctly by inspecting the edited image, along with 2 to 5 answer choices including plausible distractors. The correct answer serves as ground-truth for automated evaluation. The quality of these questions is validated by testing them on original (unedited) images, yielding only 17% accuracy, confirming that successful answers require the correct edit. Prompt templates and examples are provided in Appendix A.3 and A.2.

**ZH** 为评估模型是否正确执行了给定指令，我们引入聚焦功能正确性的 VQA 式评测框架。对每个「指令—图像」对，GPT-4o 生成一道选择题——只有查看编辑后的图像才能答对——并给出 2 至 5 个选项，其中包含具有迷惑性的干扰项。正确答案作为自动评测的真值。这些题目的质量通过在原始（未编辑）图像上测试加以验证：准确率仅 17%，说明答对确实需要正确的编辑。提示模板与示例见附录 A.3 与 A.2。

**EN** 3.3 Object Extraction and Mask Generation for Image Content Preservation Evaluation

**ZH** 3.3 面向图像内容保持评测的对象提取与掩码生成

**EN** Traditional approaches to evaluating content preservation in text-based image editing often rely on computing similarity metrics across the entire edited image compared to the original. However, this strategy is fundamentally flawed. For example, if a model makes no edits at all, these metrics would yield a perfect similarity score, even though the editing instruction has been ignored. This makes it incorrect to assume that higher similarity scores necessarily indicate better performance. To address this, we propose a more precise and targeted evaluation method that focuses on the regions of the image that are not supposed to be edited. Our key idea is to isolate the editable region using segmentation masks, and then invert the mask to define the rest of the image: the portion that should remain unchanged. By comparing these preserved regions between the original and edited images, we obtain a much more faithful estimate of content preservation.

**ZH** 评估基于文本的图像编辑中的内容保持，传统做法往往是在整幅编辑后图像与原始图像之间计算相似度指标。然而这一策略存在根本缺陷。举例来说，若模型完全不做编辑，这些指标会给出满分相似度，尽管编辑指令被彻底忽略。因此，不能想当然地认为相似度分数越高表现就越好。为此，我们提出一种更精确、更有针对性的评测方法，聚焦图像中本不应被编辑的区域。核心思路是：用分割掩码隔离出可编辑区域，再把掩码取反以定义图像的其余部分——即应当保持不变的部分。通过比较原图与编辑图的这些保持区域，我们能得到对内容保持更为忠实的估计。

<!-- [原子块 · img]  -->

**EN** Figure 3: Distribution of object mask size ratios.

**ZH** 图 3：对象掩码面积占比的分布。

**EN** Extracting and Segmenting Edit Targets. To identify the region to be edited, we first extract the target object to be edited from each instruction using GPT-4, prompting it to return concise phrases (e.g., “the green bus”, “dog’s tail”). These phrases are then passed to Grounded SAM (liu2023grounding) to produce a binary segmentation mask of the edit region. All masks are verified through human validation to ensure accuracy. This approach enables open-vocabulary grounding and supports precise, instruction-specific evaluation. The prompt used for GPT-4 is included in Appendix A.3.

**ZH** 编辑目标的提取与分割。为确定待编辑区域，我们先用 GPT-4 从每条指令中提取待编辑的目标物体，提示它返回简洁短语（例如「the green bus」「dog’s tail」）。这些短语随后被送入 Grounded SAM（liu2023grounding），生成编辑区域的二值分割掩码。所有掩码都经人工校验以确保准确。这一方案支持开放词汇定位，也支持针对具体指令的精确评测。GPT-4 所用的提示见附录 A.3。

**EN** Object Detection. We use the object label predicted by GPT-4 (e.g., “tree trunk”) to perform open-vocabulary object detection using the GroundingDINO-Tiny model (liu2023grounding). GroundingDINO outputs bounding boxes along with confidence scores and associated class names. When multiple detections are returned for the same label, we select the one with the highest confidence score.

**ZH** 目标检测。我们用 GPT-4 预测出的物体标签（例如「tree trunk」），借助 GroundingDINO-Tiny 模型（liu2023grounding）执行开放词汇目标检测。GroundingDINO 输出边界框、置信度分数与关联类别名。当同一标签返回多个检测结果时，我们选取置信度分数最高的那个。

**EN** Mask Generation. Given the bounding box returned by GroundingDINO, we apply the Segment Anything Model (SAM-ViT-Base) (kirillov2023segany) to produce a pixel-level segmentation mask for the object. This mask defines the editable region of the image and is stored as the object mask. We then compute and store the rest-of-image mask by inverting the object mask; this represents all parts of the image not intended for editing. The distribution of object mask size ratio is shown in Figure 3. Most object masks occupy less than 20% of the image area, indicating the prevalence of fine-grained edits.

**ZH** 掩码生成。给定 GroundingDINO 返回的边界框，我们应用 Segment Anything Model（SAM-ViT-Base）（kirillov2023segany）生成该物体的像素级分割掩码。该掩码定义了图像的可编辑区域，并被存为对象掩码。随后我们对对象掩码取反，计算并保存「图像其余部分」掩码，它代表图像中所有本不打算编辑的部分。对象掩码面积占比的分布如图 3 所示。多数对象掩码占图像面积不足 20%，说明细粒度编辑占主导。

**EN** This combination of using (⟦SLOT_12⟧) GPT-4 for understanding open-domain natural language, (⟦SLOT_13⟧) GroundingDINO for open-vocabulary detection, and (⟦SLOT_14⟧) SAM for high-fidelity segmentation, allows us to robustly localize editable regions even when instructions involve abstract, uncommon, or compositional object references.

**ZH** 把（⟦SLOT_12⟧）GPT-4 用于开放域自然语言理解、（⟦SLOT_13⟧）GroundingDINO 用于开放词汇检测、（⟦SLOT_14⟧）SAM 用于高保真分割这三者结合，使我们即便在指令涉及抽象、罕见或组合式物体指代时，也能稳健地定位可编辑区域。

**EN** 3.4 Human Filtering for High-Quality Annotations

**ZH** 3.4 面向高质量标注的人工筛选

**EN** To ensure high-quality evaluation data, we applied a human filtering step to our initially generated benchmark. We initially sampled 3 edit instructions for each image, resulting in a raw pool of 6,000 image-instruction pairs. However, we observed that some automatically generated object masks were inaccurate, and some edit instructions were ambiguous or invalid. To address these issues, we manually reviewed the entire dataset to only keep high-quality examples. The final curated benchmark consists of 1,080 high-quality image-instruction pairs with 856 unique images. We also made sure that these examples are carefully balanced across 9 edit types (120 edit instructions in each edit type) and 20 image categories.

**ZH** 为保证评测数据的高质量，我们对初步生成的基准施加了一道人工筛选环节。最初我们为每张图像采样 3 条编辑指令，得到 6000 个「图像—指令」对的原始池。但我们发现，部分自动生成的对象掩码不够准确，部分编辑指令含糊或无效。为此，我们人工复核了整个数据集，只保留高质量样例。最终整理出的基准包含 1080 个高质量「图像—指令」对，涉及 856 张不重复图像。我们还确保这些样例在 9 种编辑类型（每种 120 条编辑指令）与 20 个图像类别之间精细均衡。

**EN** 3.5 Evaluation Metrics

**ZH** 3.5 评测指标

**EN** We report functional correctness and content preservation as separate metrics because combining them into a single score would obscure the trade-off between instruction following and image consistency.

**ZH** 我们把功能正确性与内容保持作为两个独立的指标分别报告，因为把它们合并成单一分数会掩盖指令遵循与图像一致性之间的权衡。

**EN** Functional Correctness. To evaluate functional correctness, we adopt the VQA-style multiple-choice format described in Section 3.2. We use GPT-4o to answer each question, using only the edited image unless the question asks for a comparison between the original and edited images, and the question itself. We report accuracy of each edit type and overall accuracy across all benchmark entries.

**ZH** 功能正确性。评估功能正确性时，我们采用 3.2 节所述的 VQA 式选择题形式。我们让 GPT-4o 回答每道问题，输入只有编辑后的图像（除非题目要求比较原图与编辑图）以及问题本身。我们报告每种编辑类型的准确率，以及全部基准条目上的整体准确率。

**EN** Image Content Preservation. In addition to evaluating instruction fidelity, our benchmark assesses how well models preserve unedited content. To this end, we introduce a calibrated metric based on masked, aligned mean squared error (MSE) difference. Specifically, we compute the mean squared error between the original and edited images over unmasked regions, that is, regions that should remain unchanged, after applying geometric alignment.

**ZH** 图像内容保持。除评估指令保真度外，本基准还考察模型对未编辑内容的保持程度。为此，我们引入一个基于掩码、经几何对齐的均方误差（MSE）差分构建的校准指标。具体地，在施加几何对齐之后，我们在未掩码区域——即应保持原样的区域——上计算原图与编辑图之间的均方误差。

**EN** To mitigate the impact of spatial shifts introduced during generation, we first align the edited image to the original using SIFT keypoints (lowe2004distinctive), FLANN-based matching (muja2009fast), and affine transformation. This yields an partially aligned edited image ⟦SLOT_15⟧ to the original image ⟦SLOT_16⟧. We then invert and min-max normalize the MSE values across all benchmark entries to produce a calibrated preservation score in the range ⟦SLOT_17⟧, where higher values indicate better preservation.

**ZH** 为缓解生成过程中引入的空间偏移的影响，我们先用 SIFT 关键点（lowe2004distinctive）、基于 FLANN 的匹配（muja2009fast）与仿射变换，把编辑后图像对齐到原图，得到与原图 ⟦SLOT_16⟧ 部分对齐的编辑图 ⟦SLOT_15⟧。随后我们对全部基准条目的 MSE 值取反并做最小—最大归一化，得到落在 ⟦SLOT_17⟧ 区间内的校准保持分数，数值越高表示保持得越好。

**EN** In addition to masked MSE, we also compute masked SSIM, masked CLIP, and masked PSNR to evaluate both semantic and pixel-level preservation. Together, they provide a more comprehensive view of unintended changes introduced during editing and correlate strongly with human-annotated preservation scores (see Section 4.3).

**ZH** 除掩码 MSE 外，我们还计算掩码 SSIM、掩码 CLIP 与掩码 PSNR，以从语义与像素两个层面评估保持性。这些指标合在一起，能更全面地反映编辑过程中引入的非预期改动，并与人工标注的保持分数高度相关（见 4.3 节）。

**EN** 4 Experiments

**ZH** 4 实验

<!-- [原子块 · img]  -->

**EN** Figure 4: Left: Functional correctness per edit type. Right: Model preservation rankings based on masked MSE (inverted), PSNR, and CLIP scores. We empirically observe that model ranking evaluated by masked CLIP differs from model ranking evaluated by CLIP.

**ZH** 图 4：左图为各编辑类型上的功能正确性；右图为基于掩码 MSE（取反）、PSNR 与 CLIP 分数的模型保持性排名。我们实证观察到，用掩码 CLIP 评出的模型排名与用 CLIP 评出的模型排名不同。

**EN** 4.1 Main Results

**ZH** 4.1 主要结果

**EN** Model Add Object Attribute Change Color Change Layout Modif. Object Replace Remove Object Scene / Bkgd Change Size Change Textual Edit Overall StableDiffusion 4.17 0.83 0.00 8.33 0.83 22.50 3.33 7.50 0.00 5.28 HQ-Edit 4.17 6.67 8.33 10.83 6.67 11.67 14.17 6.67 0.00 7.69 OneDiffusion 49.17 44.17 65.83 10.00 35.83 14.17 35.00 7.50 6.67 29.81 InsPix2Pix-CLIP 35.83 40.83 40.83 10.83 46.67 40.00 51.67 6.67 2.50 30.65 InsPix2Pix 38.33 47.50 43.33 12.50 48.33 39.17 43.33 15.83 2.50 32.31 InsDiffusion 40.00 41.67 56.67 8.33 53.33 50.00 60.83 4.17 1.67 35.19 MGIE 60.00 40.00 48.33 15.00 53.33 46.67 58.33 7.50 0.00 36.57 MagicBrush 70.83 57.50 75.00 13.33 72.50 48.33 82.50 9.17 5.83 48.33 OmniGen 78.33 70.83 84.17 39.17 66.67 46.67 85.83 30.00 45.00 60.74 GPT-Image-1* 92.98 94.59 92.04 64.08 97.32 73.45 96.36 45.95 83.33 82.42 GPT-Image-1 94.74 95.50 95.58 63.11 99.11 83.19 98.18 45.05 88.33 85.00

**ZH** 模型｜添加物体｜属性更改｜颜色更改｜布局修改｜物体替换｜移除物体｜场景/背景更改｜尺寸更改｜文字编辑｜整体：StableDiffusion 4.17 0.83 0.00 8.33 0.83 22.50 3.33 7.50 0.00 5.28；HQ-Edit 4.17 6.67 8.33 10.83 6.67 11.67 14.17 6.67 0.00 7.69；OneDiffusion 49.17 44.17 65.83 10.00 35.83 14.17 35.00 7.50 6.67 29.81；InsPix2Pix-CLIP 35.83 40.83 40.83 10.83 46.67 40.00 51.67 6.67 2.50 30.65；InsPix2Pix 38.33 47.50 43.33 12.50 48.33 39.17 43.33 15.83 2.50 32.31；InsDiffusion 40.00 41.67 56.67 8.33 53.33 50.00 60.83 4.17 1.67 35.19；MGIE 60.00 40.00 48.33 15.00 53.33 46.67 58.33 7.50 0.00 36.57；MagicBrush 70.83 57.50 75.00 13.33 72.50 48.33 82.50 9.17 5.83 48.33；OmniGen 78.33 70.83 84.17 39.17 66.67 46.67 85.83 30.00 45.00 60.74；GPT-Image-1* 92.98 94.59 92.04 64.08 97.32 73.45 96.36 45.95 83.33 82.42；GPT-Image-1 94.74 95.50 95.58 63.11 99.11 83.19 98.18 45.05 88.33 85.00。

**EN** Table 2: Functional correctness (multiple-choice accuracy) per edit type evaluated by GPT-4o. Values are raw percentages. * denotes judgment by Gemini-2-Flash gemini2flash as the second judge. Full Gemini-2-Flash results are in Appendix A.4.

**ZH** 表 2：由 GPT-4o 评测的各类编辑上的功能正确性（选择题准确率）。数值为原始百分比。* 表示由 Gemini-2-Flash gemini2flash 作为第二评判者给出。Gemini-2-Flash 的完整结果见附录 A.4。

**EN** Functional Correctness. Figure 4 (left) reports functional correctness evaluation results across various edit types, evaluated via multiple-choice QA with GPT-4o. Detailed numbers are reported in Table 2. Interestingly, GPT-image-1 maintains consistent high accuracy across all categories, while other models tend to vary more significantly depending on edit type, indicating a disparity in generalization capabilities. These findings highlight the importance of model architecture and instruction-following ability in achieving faithful functional edits.

**ZH** 功能正确性。图 4（左）报告了以 GPT-4o 通过选择题问答评测的各类编辑上的功能正确性结果，详细数值见表 2。有意思的是，GPT-Image-1 在所有类别上都保持稳定的高准确率，而其他模型随编辑类型的波动明显更大，说明泛化能力存在差距。这些发现凸显了模型架构与指令遵循能力在实现忠实的功能性编辑中的重要性。

**EN** In Figure 5, we show examples of both correct and incorrect edits, some failing in executing the instruction, and others failing to preserve areas not meant to be modified, emphasizing why a dual-axis evaluation is necessary.

**ZH** 图 5 展示了正确与错误编辑的示例：有些未能执行指令，有些则未能保持本不应修改的区域，这说明双轴评测是必要的。

<!-- [原子块 · img]  -->

**EN** Figure 5: Examples showing three failure modes: functional failure, preservation failure, and combined failure, paired with correct editing.

**ZH** 图 5：展示三种失败模式的示例——功能失败、保持失败与复合失败，并与正确编辑并列对照。

<!-- [原子块 · table] Model SSIM ↑ \uparrow CLIP ↑ \uparrow Unmasked CLIP ↑ \uparrow PSNR ↑ \uparrow MSE ↓ \downarrow OneDiffusion 0.9585 0.9805 0.9434 26.24 521.57 MagicBrush 0.8703 0.9489 0.8399 20.48 1529.45 GPT-Image-1 -->

**EN** Table 3: Preservation scores across five automatic metrics. All scores are computed over regions outside the object mask to evaluate unintended changes, except Unmasked CLIP which is widely used in previous work on image editing to evaluate preservation.

**ZH** 表 3：五种自动指标下的保持分数。除 Unmasked CLIP（此前图像编辑工作中广泛用于评估保持性）外，所有分数都在对象掩码之外的区域上计算，以评估非预期改动。

**EN** Image Content Preservation.

**ZH** 图像内容保持。

**EN** Figure 4 (right) presents normalized preservation scores across models using both CLIP-based and pixel-based metrics. Detailed results are reported in Table 3. We observe that OneDiffusion and MagicBrush consistently achieve the highest preservation scores across all metrics. Interestingly, some models (e.g., GPT-Image-1) score better on masked CLIP than pixel-based metrics, implying they preserve semantic structure better than low-level appearance. Depending on whether semantic preservation or exact pixel-level preservation is more important for the application, users can choose to evaluate preservation using CLIP-based or pixel-based metrics, respectively.

**ZH** 图 4（右）给出各模型在基于 CLIP 与基于像素的指标上的归一化保持分数，详细结果见表 3。我们观察到，OneDiffusion 与 MagicBrush 在所有指标上始终取得最高保持分。有意思的是，部分模型（如 GPT-Image-1）在掩码 CLIP 上的得分优于基于像素的指标，说明它们保持语义结构的能力强于保持低层外观。根据具体应用更看重语义层面的保持还是精确的像素级保持，用户可以分别选用基于 CLIP 或基于像素的指标来评估保持性。

**EN** 4.2 How Well Does GPT-Image-1 Edit Images?

**ZH** 4.2 GPT-Image-1 编辑图像的表现如何？

<!-- [原子块 · img]  -->

**EN** Figure 6: Examples of GPT-Image-1’s failure modes.

**ZH** 图 6：GPT-Image-1 的失败模式示例。

**EN** GPT-Image-1 demonstrates strong overall performance across a wide range of text-guided editing instructions. It excels particularly in appearance-level edits, such as changing colors, modifying textures, adding or replacing objects, and editing text. For example, the model accurately changes the color of clothing items and signage, introduces new objects like potted plants or balloons with realistic rendering, and performs text edits with high spatial and semantic fidelity. These strengths highlight its powerful visual grounding and instruction-following ability.

**ZH** GPT-Image-1 在广泛的文本引导编辑指令上展现出强劲的整体表现，尤其擅长外观层面的编辑，例如更改颜色、修改纹理、添加或替换物体，以及编辑文字。举例来说，该模型能准确更改衣物与标识的颜色，以逼真的渲染加入盆栽或气球等新物体，并以较高的空间与语义保真度完成文字编辑。这些优势凸显了它强大的视觉定位与指令遵循能力。

**EN** However, GPT-Image-1 shows noticeable weaknesses in spatial and layout-related edits. For layout modifications (e.g., “move the table to the left side” or “move the person to the right”), the model often interprets the direction loosely or inconsistently (example in Figure 6 top left). Similarly, in size-change instructions (e.g., “make the vase twice as large as the lamp”), the modified objects sometimes appear disproportionate or fail to satisfy the relative sizing constraints (example in Figure 6 top right). These issues suggest that GPT-Image-1 struggles with precise spatial reasoning and proportional scaling.

**ZH** 然而，GPT-Image-1 在空间与布局相关的编辑上表现出明显弱点。对于布局修改（如「把桌子移到左侧」或「把人移到右边」），模型常常宽松或不一致地理解方向（示例见图 6 左上）。类似地，在尺寸更改指令（如「把花瓶做得有台灯两倍大」）中，被修改的物体有时显得不成比例，或未能满足相对尺寸的约束（示例见图 6 右上）。这些问题说明 GPT-Image-1 在精确的空间推理与等比缩放上存在困难。

**EN** In object removal tasks, GPT-Image-1 occasionally leaves residual artifacts or incompletely erases the object (example in Figure 6 bottom left), especially when the background is complex.

**ZH** 在物体移除任务中，GPT-Image-1 偶尔会留下残留痕迹或未能完整擦除物体（示例见图 6 左下），当背景复杂时尤为明显。

**EN** Another common failure is imprecision in preserving non-targeted regions. GPT-Image-1 frequently introduces unintended changes in areas unrelated to the instruction (example in Figure 6 bottom right), such as altering background textures, shifting lighting, or distorting peripheral objects. In contrast, models like MGIE tend to preserve these untouched regions more faithfully, leading to higher preservation scores and more stable image content.

**ZH** 另一类常见失败是对非目标区域的保持不够精确。GPT-Image-1 经常在与指令无关的区域引入非预期改动（示例见图 6 右下），例如改变背景纹理、偏移光照，或扭曲周边的物体。相比之下，MGIE 等模型往往能更忠实地保持这些未触及的区域，因而取得更高的保持分数与更稳定的图像内容。

**EN** Overall, while GPT-Image-1 is highly capable in executing core edits, it lacks fine-grained control over spatial relationships and content preservation, leaving room for improvement for tasks that demand high precision or minimal collateral changes.

**ZH** 总的来看，GPT-Image-1 在执行核心编辑上能力很强，却缺乏对空间关系与内容保持的细粒度控制；对于要求高精度或最小附带改动的任务，仍有改进空间。

**EN** 4.3 Human Study

**ZH** 4.3 人工研究

<!-- [原子块 · img]  -->

**EN** Figure 7: Left: Correlation between human and GPT-4o evaluated functional correctness scores. Right: Correlation between human-evaluated preservation and inverted calibrated MSE rank.

**ZH** 图 7：左图为人类与 GPT-4o 评出的功能正确性分数之间的相关性；右图为人工评估的保持性与取反后的校准 MSE 排名之间的相关性。

<!-- [原子块 · table] Metric Spearman Masked SSIM 0.881 Masked CLIP 0.952 Masked PSNR 0.905 Masked Inverted MSE 0.833 -->

**EN** Table 4: Spearman correlation between human ratings on content preservation and automatic metrics.

**ZH** 表 4：内容保持上的人工评分与自动指标之间的 Spearman 相关系数。

**EN** One of the central goals of our benchmark is to faithfully reflect human preferences when evaluating text-guided image editing. To assess this alignment, we conduct a human ranking study over a representative subset of 100 editing examples. Each example consists of an original image, an edit instruction, and the corresponding outputs generated by nine models22 2 GPT-Image-1 API was not released at the time thus not included.: StableDiffusion, HQ-Edit, OneDiffusion, InsPix2Pix-CLIP, InsPix2Pix, InsDiffusion, MGIE, MagicBrush, and OmniGen. Each image-edit pair is independently evaluated by four human annotators, who are instructed to provide two scores: one for instruction adherence and another for preservation of regions that are not supposed to be edited. Both scores used a 4-point scale, where 0 denotes complete failure, 1 indicates weak rejection, 2 represents weak acceptance, and 3 signals complete success. We then compute the average rank for each model across all 100 examples and annotators.

**ZH** 本基准的核心目标之一，是在评测文本引导的图像编辑时忠实地反映人类偏好。为检验这种对齐程度，我们在 100 个具代表性的编辑样例上开展了人工排序研究。每个样例由一张原图、一条编辑指令，以及九个模型22 2 当时 GPT-Image-1 的 API 尚未发布，因此未纳入。生成的对应输出组成：StableDiffusion、HQ-Edit、OneDiffusion、InsPix2Pix-CLIP、InsPix2Pix、InsDiffusion、MGIE、MagicBrush 与 OmniGen。每个「图像—编辑」对由四名标注者独立评估，他们被要求给出两个分数：一个衡量指令遵循程度，另一个衡量本不应编辑区域的保持程度。两个分数都采用 4 分制，0 表示完全失败，1 表示弱否决，2 表示弱接受，3 表示完全成功。我们随后计算每个模型在全部 100 个样例与所有标注者上的平均排名。

**EN** Figure 7 (left) visualizes the relationship between GPT-4o evaluated functional correctness scores and human-annotated correctness, showing a clear positive trend. Table 4 reports the Spearman correlation coefficients between masked SSIM, masked CLIP, masked PSNR, and masked inverted MSE scores and human rankings (inverted so that higher values indicate better human preference alignment). Figure 7 (right) shows a strong correspondence between human preservation scores and inverted MSE rank, with models like OneDiffusion and MagicBrush scoring highly on both.

**ZH** 图 7（左）可视化了 GPT-4o 评出的功能正确性分数与人工标注正确性之间的关系，呈现出清晰的正向趋势。表 4 报告了掩码 SSIM、掩码 CLIP、掩码 PSNR 与掩码取反 MSE 分数与人工排名之间的 Spearman 相关系数（已取反，使数值越高表示与人类偏好越一致）。图 7（右）显示，人工保持分数与取反 MSE 排名之间存在很强的对应性，OneDiffusion 与 MagicBrush 等模型在两者上都得分很高。

**EN** Together, these two metrics provide complementary views of model quality. Functional correctness captures whether the desired edit was made, while preservation evaluates whether it was done in a controlled and localized way. The strong alignment of both metrics with human preferences supports their joint use for comprehensive evaluation in text-guided image editing.

**ZH** 这两个指标合在一起，提供了互补的模型质量视角：功能正确性刻画期望的编辑是否完成，保持性则评估编辑是否以受控、局部化的方式完成。两个指标都与人类偏好高度吻合，这支持了把它们联合用于文本引导图像编辑的综合评测。

**EN** 5 Conclusion

**ZH** 5 结论

**EN** We introduce a benchmark for evaluating text-based image editing models along two critical axes: functional correctness and content preservation. Our evaluation combines VQA-style multiple-choice questions and object-aware preservation score to ensure edits are both instruction-faithful and minimally invasive. With over 1000 annotated examples across 20 diverse domains, the benchmark offers a scalable and interpretable framework. We also present a comparative analysis of leading editing models, revealing key strengths and weaknesses. We hope our benchmark drives progress toward developing text-based image editing systems that are not only visually compelling but also faithful to instructions and minimally invasive to unedited regions.

**ZH** 我们提出一个沿功能正确性与内容保持两个关键轴评估基于文本的图像编辑模型的基准。我们的评测把 VQA 式选择题与对象感知的保持分数结合起来，以确保编辑既忠实于指令，又尽可能少地侵入无关区域。该基准含 20 个多样领域下逾 1000 个带标注的样例，提供了一个可扩展、可解释的框架。我们还给出了主流编辑模型的对比分析，揭示了各自的关键优势与不足。我们希望本基准能推动基于文本的图像编辑系统朝着不仅视觉上吸引人、而且忠实于指令、并对未编辑区域改动最小的方向发展。

**EN** Limitation

**ZH** 局限性

**EN** Our benchmark focuses on evaluating single-turn text-guided image edits where instructions are relatively atomic and localized. While this setting captures a wide range of edit types, it does not yet address more complex scenarios such as multi-step editing, interactive refinement, or long-form compositional instructions. In real-world applications, users often use sequential or iterative commands that require maintaining visual and semantic coherence over time. These scenarios pose additional challenges for instruction interpretation, memory, and image consistency, demanding more advanced model capabilities and evaluation methods. In future work, we plan to extend text-guided image-editing evaluation to these more dynamic settings.

**ZH** 本基准聚焦于评估单轮的文本引导图像编辑，其中指令相对原子化且局部化。这一设定虽覆盖了广泛的编辑类型，却尚未涉及更复杂的场景，例如多步编辑、交互式细化，或长篇幅的组合式指令。在实际应用中，用户常常使用需要随时间维持视觉与语义连贯性的顺序式或迭代式命令。这类场景对指令理解、记忆与图像一致性提出了额外挑战，要求模型具备更高级的能力，也需要更先进的评测方法。后续工作中，我们计划把文本引导图像编辑的评测扩展到这些更具动态性的设定。

**EN** Acknowledgments and Disclosure of Funding

**ZH** 致谢与经费披露

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] [1] OpenAI. Gpt image 1: State-of-the-art image generation model. https://platform.openai.com/docs/models/gpt-image-1 , 2025. -->

<!-- [原子块 · verbatim] [2] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, and Ilya Sutskever. Learning t -->

<!-- [原子块 · verbatim] [3] Yiwei Ma, Jiayi Ji, Ke Ye, Weihuang Lin, Yonghan Zheng, Qiang Zhou, Xiaoshuai Sun, Rongrong Ji, et al. I2ebench: A comprehensive benchmark for instruction-based image editing. In The Thirty-eighth -->

<!-- [原子块 · verbatim] [4] Tsu-Jui Fu, Wenze Hu, Xianzhi Du, William Yang Wang, Yinfei Yang, and Zhe Gan. Guiding Instruction-based Image Editing via Multimodal Large Language Models. In International Conference on Learning -->

<!-- [原子块 · verbatim] [5] Shitao Xiao, Yueze Wang, Junjie Zhou, Huaying Yuan, Xingrun Xing, Ruiran Yan, Chaofan Li, Shuting Wang, Tiejun Huang, and Zheng Liu. Omnigen: Unified image generation, 2024. -->

<!-- [原子块 · verbatim] [6] Shangkun Sun, Bowen Qu, Xiaoyu Liang, Songlin Fan, and Wei Gao. Ie-bench: Advancing the measurement of text-driven image editing for human perception alignment, 2025. -->

<!-- [原子块 · verbatim] [7] Su Wang, Chitwan Saharia, Ceslee Montgomery, Jordi Pont-Tuset, Shai Noy, Stefano Pellegrini, Yasumasa Onoe, Sarah Laszlo, David J Fleet, Radu Soricut, et al. Imagen editor and editbench: Advancing -->

<!-- [原子块 · verbatim] [8] Guillaume Couairon, Jakob Verbeek, Holger Schwenk, and Matthieu Cord. Diffedit: Diffusion-based semantic image editing with mask guidance, 2022. -->

<!-- [原子块 · verbatim] [9] Amir Hertz, Ron Mokady, Jay Tenenbaum, Kfir Aberman, Yael Pritch, and Daniel Cohen-Or. Prompt-to-prompt image editing with cross attention control, 2022. -->

<!-- [原子块 · verbatim] [10] Bahjat Kawar, Shiran Zada, Oran Lang, Omer Tov, Huiwen Chang, Tali Dekel, Inbar Mosseri, and Michal Irani. Imagic: Text-based real image editing with diffusion models. In 2023 IEEE/CVF Conference -->

<!-- [原子块 · verbatim] [11] Tim Brooks, Aleksander Holynski, and Alexei A. Efros. Instructpix2pix: Learning to follow image editing instructions. In 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) -->

<!-- [原子块 · verbatim] [12] Zigang Geng, Binxin Yang, Tiankai Hang, Chen Li, Shuyang Gu, Ting Zhang, Jianmin Bao, Zheng Zhang, Han Hu, Dong Chen, and Baining Guo. Instructdiffusion: A generalist modeling interface for visio -->

<!-- [原子块 · verbatim] [13] Tsu-Jui Fu, Yusu Qian, Chen Chen, Wenze Hu, Zhe Gan, and Yinfei Yang. Univg: A generalist diffusion model for unified image generation and editing, 2025. -->

<!-- [原子块 · verbatim] [14] Duong H. Le, Tuan Pham, Sangho Lee, Christopher Clark, Aniruddha Kembhavi, Stephan Mandt, Ranjay Krishna, and Jiasen Lu. One diffusion to generate them all, 2024. -->

<!-- [原子块 · verbatim] [15] Kai Zhang, Lingbo Mo, Wenhu Chen, Huan Sun, and Yu Su. Magicbrush: A manually annotated dataset for instruction-guided image editing. In Advances in Neural Information Processing Systems , 2023. -->

<!-- [原子块 · verbatim] [16] Yuzhou Huang, Liangbin Xie, Xintao Wang, Ziyang Yuan, Xiaodong Cun, Yixiao Ge, Jiantao Zhou, Chao Dong, Rui Huang, Ruimao Zhang, and Ying Shan. Smartedit: Exploring complex instruction-based imag -->

<!-- [原子块 · verbatim] [17] Shufan Li, Harkanwar Singh, and Aditya Grover. Instructany2pix: Flexible visual editing via multimodal instruction following, 2024. -->

<!-- [原子块 · verbatim] [18] Yuanze Lin, Yi-Wen Chen, Yi-Hsuan Tsai, Lu Jiang, and Ming-Hsuan Yang. Text-driven image editing via learnable regions, 2024. -->

<!-- [原子块 · verbatim] [19] Zichong Meng, Changdi Yang, Jun Liu, Hao Tang, Pu Zhao, and Yanzhi Wang. Instructgie: Towards generalizable image editing, 2024. -->

<!-- [原子块 · verbatim] [20] Zhen Han, Chaojie Mao, Zeyinzi Jiang, Yulin Pan, and Jingfeng Zhang. Stylebooth: Image style editing with multimodal instruction, 2024. -->

<!-- [原子块 · verbatim] [21] Shanglin Li, Bohan Zeng, Yutang Feng, Sicheng Gao, Xuhui Liu, Jiaming Liu, Li Lin, Xu Tang, Yao Hu, Jianzhuang Liu, and Baochang Zhang. Zone: Zero-shot instruction-guided local editing, 2024. -->

<!-- [原子块 · verbatim] [22] Qin Guo and Tianwei Lin. Focus on your instruction: Fine-grained and multi-instruction image editing by attention modulation, 2023. -->

<!-- [原子块 · verbatim] [23] Rodrigo Santos, João Silva, and António Branco. Leveraging llms for on-the-fly instruction guided image editing, 2024. -->

<!-- [原子块 · verbatim] [24] Ruoyu Zhao, Qingnan Fan, Fei Kou, Shuai Qin, Hong Gu, Wei Wu, Pengcheng Xu, Mingrui Zhu, Nannan Wang, and Xinbo Gao. Instructbrush: Learning attention-based instruction optimization for image edi -->

<!-- [原子块 · verbatim] [25] Samyadeep Basu, Mehrdad Saberi, Shweta Bhardwaj, Atoosa Malemir Chegini, Daniela Massiceti, Maziar Sanjabi, Shell Xu Hu, and Soheil Feizi. Editval: Benchmarking diffusion based text-guided image  -->

<!-- [原子块 · verbatim] [26] Yushi Hu, Benlin Liu, Jungo Kasai, Yizhong Wang, Mari Ostendorf, Ranjay Krishna, and Noah A Smith. Tifa: Accurate and interpretable text-to-image faithfulness evaluation with question answering,  -->

<!-- [原子块 · verbatim] [27] Jaemin Cho, Yushi Hu, Roopal Garg, Peter Anderson, Ranjay Krishna, Jason Baldridge, Mohit Bansal, Jordi Pont-Tuset, and Su Wang. Davidsonian scene graph: Improving reliability in fine-grained eva -->

<!-- [原子块 · verbatim] [28] Shilong Liu, Zhaoyang Zeng, Tianhe Ren, Feng Li, Hao Zhang, Jie Yang, Chunyuan Li, Jianwei Yang, Hang Su, Jun Zhu, et al. Grounding dino: Marrying dino with grounded pre-training for open-set obj -->

<!-- [原子块 · verbatim] [29] Alexander Kirillov, Eric Mintun, Nikhila Ravi, Hanzi Mao, Chloe Rolland, Laura Gustafson, Tete Xiao, Spencer Whitehead, Alexander C. Berg, Wan-Yen Lo, Piotr Dollár, and Ross Girshick. Segment any -->

<!-- [原子块 · verbatim] [30] David G Lowe. Distinctive image features from scale-invariant keypoints. International journal of computer vision , 60:91–110, 2004. -->

<!-- [原子块 · verbatim] [31] Marius Muja and David G Lowe. Fast approximate nearest neighbors with automatic algorithm configuration. VISAPP (1) , 2(331-340):2, 2009. -->

<!-- [原子块 · verbatim] [32] Google. Introducing gemini 2.0: our new ai model for the agentic era. https://blog.google/technology/google-deepmind/google-gemini-ai-update-december-2024/ , 2024. -->

<!-- [原子块 · verbatim] [33] Chitwan Saharia, William Chan, Saurabh Saxena, Lala Li, Jay Whang, Emily Denton, Seyed Kamyar Seyed Ghasemipour, Burcu Karagol Ayan, S. Sara Mahdavi, Rapha Gontijo Lopes, Tim Salimans, Jonathan H -->

<!-- [原子块 · verbatim] [34] Jiahui Yu, Yuanzhong Xu, Jing Yu Koh, Thang Luong, Gunjan Baid, Zirui Wang, Vijay Vasudevan, Alexander Ku, Yinfei Yang, Burcu Karagol Ayan, Ben Hutchinson, Wei Han, Zarana Parekh, Xin Li, Han Zha -->

<!-- [原子块 · verbatim] [35] Yuval Kirstain, Adam Polyak, Uriel Singer, Shahbuland Matiana, Joe Penna, and Omer Levy. Pick-a-pic: An open dataset of user preferences for text-to-image generation, 2023. -->

<!-- [原子块 · verbatim] [36] Shuhao Han, Haotian Fan, Jiachen Fu, Liang Li, Tao Li, Junhui Cui, Yunqiu Wang, Yang Tai, Jingwei Sun, Chunle Guo, and Chongyi Li. Evalmuse-40k: A reliable and fine-grained benchmark with compreh -->

<!-- [原子块 · verbatim] [37] Chunyi Li, Zicheng Zhang, Haoning Wu, Wei Sun, Xiongkuo Min, Xiaohong Liu, Guangtao Zhai, and Weisi Lin. Agiqa-3k: An open database for ai-generated image quality assessment, 2023. -->

<!-- [原子块 · verbatim] [38] Jiarui Wang, Huiyu Duan, Yu Zhao, Juntong Wang, Guangtao Zhai, and Xiongkuo Min. Lmm4lmm: Benchmarking and evaluating large-multimodal image generation with lmms, 2025. -->

<!-- [原子块 · verbatim] [39] Dhruba Ghosh, Hanna Hajishirzi, and Ludwig Schmidt. Geneval: An object-focused framework for evaluating text-to-image alignment, 2023. -->

**EN** Appendix A Appendix

**ZH** 附录 A 附录

**EN** A.1 Related Work on Benchmarks for Text-to-Image Generation

**ZH** A.1 文本到图像生成基准的相关工作

**EN** Several benchmarks [33, 34, 16, 35, 36, 37, 38, 26, 27, 39] have been proposed to evaluate text-to-image generation models from different aspects. DrawBench [33] and PartiPrompt [34] assess basic compositional abilities like attributes and spatial relationships. T2I-CompBench [16] introduces more complex reasoning skills such as comparison and logic. Pick-a-Pic [35] and EvalMuse-40K [36] collect large-scale human preferences for ranking outputs. Meanwhile, AGIQA-3K [37] and EvalMi-50K [38] incorporate detailed perceptual and correspondence annotations, providing fine-grained and scalable evaluation of both image quality and instruction adherence. GenEval [39] offers an object-centric evaluation framework that assesses compositional properties. TIFA [26] and Davidsonian Scene Graph [27] adopt VQA-based methods to assess fine-grained text-image alignment.

**ZH** 已有若干基准 [33, 34, 16, 35, 36, 37, 38, 26, 27, 39] 从不同角度评估文本到图像生成模型。DrawBench [33] 与 PartiPrompt [34] 考察属性、空间关系等基本组合能力。T2I-CompBench [16] 引入了比较与逻辑等更复杂的推理技能。Pick-a-Pic [35] 与 EvalMuse-40K [36] 收集大规模人类偏好以对输出排序。AGIQA-3K [37] 与 EvalMi-50K [38] 则纳入细致的感知与对应性标注，对图像质量与指令遵循提供细粒度、可扩展的评测。GenEval [39] 提供了一个以对象为中心的评测框架，用于评估组合属性。TIFA [26] 与 Davidsonian Scene Graph [27] 采用基于 VQA 的方法评估细粒度的图文对齐。

**EN** A.2 Examples for Functional Correctness Evaluation

**ZH** A.2 功能正确性评测的示例

**EN** Table 5 provides representative examples of the nine edit types included in GIE-Bench, covering both low-level appearance changes and high-level semantic modifications. For each edit type, we show the input image content, the natural language instruction provided to the model, the corresponding multiple-choice question used for functional correctness assessment, and the expected answer.

**ZH** 表 5 给出 GIE-Bench 所含九种编辑类型的代表性示例，既涵盖低层外观改动，也涵盖高层语义修改。对每种编辑类型，我们展示输入图像内容、提供给模型的自然语言指令、用于功能正确性评测的对应选择题，以及预期答案。

<!-- [原子块 · table] Edit Type Image Content Example Instruction Evaluation Question and Options Expected Answer Color Change A black coffee mug on a wooden table Change the color of the mug to red. What color is the mug? -->

**EN** Table 5: Examples of edit instructions, evaluation questions and options, and expected answer of 9 edit types (Scene Change and Background Change are in the same category).

**ZH** 表 5：九种编辑类型的编辑指令、评测问题与选项，以及预期答案示例（场景更改与背景更改归入同一类别）。

**EN** A.3 Prompt Templates to Generate Benchmark

**ZH** A.3 用于生成基准的提示模板

**EN** The prompts we used to generate editing instructions using GPT-4o are shown in Figure 8. The prompt we used to summarize object to edit based on the editing instruction is shown in Figure 9.

**ZH** 我们用 GPT-4o 生成编辑指令时所用的提示见图 8。我们依据编辑指令归纳待编辑物体时所用的提示见图 9。

<!-- [原子块 · object]  -->

**EN** Figure 8: Prompts used to generate editing instructions, multiple-choice questions, and true answers.

**ZH** 图 8：用于生成编辑指令、选择题与正确答案的提示。

<!-- [原子块 · object]  -->

**EN** Figure 9: Prompt used to summarize object to edit in the editing instructions.

**ZH** 图 9：用于归纳编辑指令中待编辑物体的提示。

**EN** A.4 Robustness of GPT-4o-Based Evaluation

**ZH** A.4 基于 GPT-4o 的评测的稳健性

**EN** To evaluate the stability of using GPT-4o for automatic functional correctness assessment in our VQA-style setup, we conducted three independent runs of the evaluation process. For each run, GPT-4o was provided with the same sets of multiple-choice questions and corresponding edited images for each model. We set the decoding temperature to 0 in all runs to ensure deterministic outputs.

**ZH** 为评估在我们的 VQA 式设定中用 GPT-4o 做自动功能正确性评测的稳定性，我们把评测流程独立运行了三次。每次运行中，向 GPT-4o 提供相同的选择题集合与各模型对应的编辑后图像。三次运行均把解码温度设为 0，以保证输出的确定性。

<!-- [原子块 · table] Model GPT-4o Run 1 GPT-4o Run 2 GPT-4o Run 3 StableDiffusion 5.19 5.46 5.28 HQ-Edit 7.78 8.06 7.69 InsDiffusion 35.46 35.37 35.19 OmniGen 61.02 61.48 60.74 -->

**EN** Table 6: Functional correctness accuracy (%) across three evaluation runs using GPT-4o with temperature set to 0.

**ZH** 表 6：温度设为 0 时，用 GPT-4o 进行三轮评测的功能正确性准确率（%）。

**EN** The results show strong consistency across runs, with negligible fluctuations (typically under ⟦SLOT_18⟧0.3 percentage points). The per-model scores are stable. This confirms that GPT-4o, when used deterministically, provides a robust evaluation, which strengthens the benchmark’s reproducibility and fairness in model comparison.

**ZH** 结果显示各轮之间高度一致，波动可忽略（通常在 ⟦SLOT_18⟧0.3 个百分点以内），各模型的分数稳定。这印证了 GPT-4o 在确定性使用方式下能提供稳健的评测，从而增强了本基准的可复现性以及模型比较的公平性。

**EN** Model Add Object Attribute Change Color Change Layout Modif. Object Replace Remove Object Scene / Bkgd Change Size Change Textual Edit Overall StableDiffusion 6.67% 5.83% 4.17% 13.33% 5.00% 21.67% 7.50% 15.83% 3.33% 9.26% HQ-Edit 11.67% 10.00% 16.67% 11.67% 10.00% 15.00% 17.50% 17.50% 3.33% 12.59% OneDiffusion 44.17% 43.33% 64.17% 10.83% 35.83% 11.67% 37.50% 22.50% 9.17% 31.02% InsPix2Pix-CLIP 38.33% 42.50% 39.17% 15.83% 48.33% 30.00% 47.50% 20.83% 7.50% 32.22% InsPix2Pix 42.50% 47.50% 44.17% 19.17% 55.83% 30.83% 45.00% 17.50% 8.33% 34.54% MGIE 49.17% 36.67% 50.00% 19.17% 50.83% 40.00% 61.67% 22.50% 2.50% 36.94% InsDiffusion 48.33% 45.00% 67.50% 15.83% 59.17% 44.17% 67.50% 13.33% 2.50% 40.37% MagicBrush 67.50% 57.50% 76.67% 15.83% 70.00% 39.17% 77.50% 19.17% 7.50% 47.87% OmniGen 78.33% 75.00% 84.17% 49.17% 70.83% 38.33% 80.83% 35.00% 50.83% 62.50% GPT-Image-1 92.98% 94.59% 92.04% 65.05% 97.32% 73.45% 96.36% 46.85% 84.17% 82.72%

**ZH** 模型｜添加物体｜属性更改｜颜色更改｜布局修改｜物体替换｜移除物体｜场景/背景更改｜尺寸更改｜文字编辑｜整体：StableDiffusion 6.67% 5.83% 4.17% 13.33% 5.00% 21.67% 7.50% 15.83% 3.33% 9.26%；HQ-Edit 11.67% 10.00% 16.67% 11.67% 10.00% 15.00% 17.50% 17.50% 3.33% 12.59%；OneDiffusion 44.17% 43.33% 64.17% 10.83% 35.83% 11.67% 37.50% 22.50% 9.17% 31.02%；InsPix2Pix-CLIP 38.33% 42.50% 39.17% 15.83% 48.33% 30.00% 47.50% 20.83% 7.50% 32.22%；InsPix2Pix 42.50% 47.50% 44.17% 19.17% 55.83% 30.83% 45.00% 17.50% 8.33% 34.54%；MGIE 49.17% 36.67% 50.00% 19.17% 50.83% 40.00% 61.67% 22.50% 2.50% 36.94%；InsDiffusion 48.33% 45.00% 67.50% 15.83% 59.17% 44.17% 67.50% 13.33% 2.50% 40.37%；MagicBrush 67.50% 57.50% 76.67% 15.83% 70.00% 39.17% 77.50% 19.17% 7.50% 47.87%；OmniGen 78.33% 75.00% 84.17% 49.17% 70.83% 38.33% 80.83% 35.00% 50.83% 62.50%；GPT-Image-1 92.98% 94.59% 92.04% 65.05% 97.32% 73.45% 96.36% 46.85% 84.17% 82.72%。

**EN** Table 7: Functional correctness (multiple-choice accuracy) per edit type as judged by Gemini-2-flash.

**ZH** 表 7：由 Gemini-2-flash 评判的各类编辑上的功能正确性（选择题准确率）。

**EN** To assess the robustness of our functional correctness evaluation, we employed Gemini-2-Flash [32] as a secondary judge alongside GPT-4o. For each edited image and its associated multiple-choice question, we recorded the answer selected by Gemini-2-Flash using the same VQA-style evaluation protocol. As shown in Table 3, the scores from Gemini closely track those of GPT-4o, confirming the reliability of our automatic evaluation framework across different models.

**ZH** 为检验功能正确性评测的稳健性，我们引入 Gemini-2-Flash [32] 作为与 GPT-4o 并列的第二评判者。对每个编辑后图像及其对应的选择题，我们用相同的 VQA 式评测协议记录 Gemini-2-Flash 所选的答案。如表 3 所示，Gemini 给出的分数与 GPT-4o 高度贴近，印证了我们的自动评测框架在不同模型间是可靠的。

**EN** A.5 Human Study

**ZH** A.5 人工研究

<!-- [原子块 · img]  -->

**EN** Figure 10: The annotation guidance we provided to human annotators on how to assign scores.

**ZH** 图 10：我们向人工标注者提供的打分指导说明。

**EN** To validate the alignment of our automatic evaluation metrics with human perception, we conducted a human study over a randomly chosen subset of 100 edited examples from GIE-Bench.

**ZH** 为验证本文自动评测指标与人类感知的对齐程度，我们在从 GIE-Bench 中随机选取的 100 个编辑样例子集上开展了人工研究。

**EN** Annotation Setup. For each example, participants were presented with: (⟦SLOT_19⟧) one original image (top row), (⟦SLOT_20⟧) a set of nine edited images, each generated by a different image editing model (arranged in rows below), (⟦SLOT_21⟧) the editing instruction (e.g., “Remove the photo of the circular window.”), and the edit type (e.g., Remove Object) displayed at the bottom.

**ZH** 标注设置。对每个样例，向参与者呈现：（⟦SLOT_19⟧）一张原图（置于顶行）；（⟦SLOT_20⟧）一组九张编辑后图像，分别由不同的图像编辑模型生成（在其下方按行排列）；（⟦SLOT_21⟧）编辑指令（例如「Remove the photo of the circular window.」），以及置于底部的编辑类型（例如 Remove Object）。

**EN** The annotation guidance we provided on how to assign scores is shown in Figure 10. The human annotation task in this study involved scoring visual outputs of image editing models and did not collect any personal or sensitive information from participants. Hourly wage is 25 USD.

**ZH** 我们提供的打分指导说明见图 10。本研究中的人工标注任务是对图像编辑模型的视觉输出打分，未收集参与者的任何个人或敏感信息。时薪为 25 美元。
