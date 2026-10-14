# DesignProbe：面向多模态大语言模型的平面设计基准

> 原标题：DesignProbe: A Graphic Design Benchmark for Multimodal Large Language Models
> 作者：Jieru Lin, Danqing Huang, Tiejun Zhao, Dechen Zhan, Chin-Yew Lin · arXiv:2404.14801 · 2024-04-23

<!-- [原子块 · verbatim] DesignProbe: A Graphic Design Benchmark for Multimodal Large Language Models -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] A well-executed graphic design typically achieves harmony in two levels, from the fine-grained design elements (color, font and layout) to the overall design. This complexity makes the comprehension o -->

<!-- [原子块 · img]  -->

**EN** Figure 1: The performance of 5 MLLMs at overall design level and design element level (color, font and layout) in DesignProbe.

**ZH** 图 1：5 个 MLLM 在 DesignProbe 中于整体设计层面与设计元素层面（色彩、字体和版式）上的表现。

<!-- [原子块 · img]  -->

**EN** Figure 2: Overview of our benchmark. It comprises a total of eight tasks to evaluate the proficiency of MLLM in design. The assessment occurs on two distinct levels: the element level and the overall design level. At the element level, it focus on three fundamental design components: color, font and layout. For each, both visual and semantic aspects are included. Each task is presented with an example.

**ZH** 图 2：本基准概览。它共包含八项任务，用于评价 MLLM 在平面设计上的能力。评估在两个不同层面展开：元素层面与整体设计层面。在元素层面，重点关注三个基本设计要素：色彩、字体与版式，每个要素都包含视觉与语义两个方面。每项任务均给出一个示例。

**EN** 1 Introduction

**ZH** 1 引言

**EN** Graphic design is essential for our daily experiences, appearing everywhere from movie posters to slides. A well-executed graphic design typically achieves dual-level harmony, weaving together fine-grained design elements such as color, font, and layout with the overall design among different types of elements Huang et al. (2023). The fine-grained elements should not only stand alone their own aesthetic principles but also contribute to the overall design harmony. Take the basic design element as examples, colors in design need to have contrast and cooperation between them, which offering clarity and charm, and also require to align with the overall mood and style as well color?.

**ZH** 平面设计对我们的日常体验至关重要，从电影海报到幻灯片，无处不在。一件出色的平面设计通常实现双重层面的和谐，把色彩、字体、版式等细粒度设计元素与不同类型元素之间的整体设计编织在一起（Huang 等，2023）。细粒度元素既要自身符合美学原则，也要为整体设计的和谐作出贡献。以基本设计元素为例，设计中的色彩之间需要有对比与配合，从而带来清晰感与魅力，同时还需要与整体情绪和风格相一致。

**EN** The complexity inherent in design poses challenges to understanding graphic design. One must first recognize the design elements and then comprehend the overall design. The recognition of design elements presents a challenge to existing vision models, for lacking of the design-related data in the pertaining of these models. The different and abstract appearance of these design elements compared with the real word object may add more difficulty in recognition. Comprehending is an equally daunting task as well. They may encounter design tasks for the first time without equipping with the design knowledge, such as the contract and harmony of colors, the different clarity and symbolism carried by different font, and the purposeful arrangement within layout. Furthermore, there is currently limited insight into the performance of AI systems in understanding design, leaving an area ripe for exploration and advancement.

**ZH** 设计本身固有的复杂性给理解平面设计带来挑战：人们必须先识别设计元素，再理解整体设计。设计元素的识别对现有视觉模型构成挑战，因为这些模型在预训练时缺少与设计相关的数据；这些设计元素相对真实世界物体而言外观迥异且抽象，也会增加识别难度。理解同样是一项艰巨的任务：模型可能是首次遇到设计任务，不具备设计知识，例如色彩的对比与和谐、不同字体所承载的不同清晰度与象征意义，以及版式中有目的的排布。此外，目前对 AI 系统理解设计之表现的了解还很有限，这是一个亟待探索与推进的领域。

**EN** Recent advancements in the field of Multimodal Large Language Models (MLLMs) Li et al. (2023c); Dai et al. (2023), especially GPT-4 Vision OpenAI (2023b), have demonstrated extraordinary capabilities in a wide range of image-to-text tasks. These models perform inspiring not only in visual recognition tasks such as object detection Zhu et al. (2020) but also in semantic reasoning tasks, including commonsense reasoning Fu et al. (2023) and answering college exam questions Yue et al. (2023) under a zero-shot setting. Inspired by these advancements, we introduce DesignProbe, a benchmark designed to explore the performance of MLLMs in the field of design.

**ZH** 多模态大语言模型（MLLM）领域的近期进展（Li 等，2023c；Dai 等，2023），尤其是 GPT-4 Vision（OpenAI，2023b），已在广泛的图像到文本任务中展现出非凡能力。这些模型不仅在目标检测（Zhu 等，2020）等视觉识别任务上表现亮眼，在常识推理（Fu 等，2023）与零样本设置下回答大学考试题目（Yue 等，2023）等语义推理任务上也同样出色。受这些进展启发，我们提出 DesignProbe——一个用于探究 MLLM 在设计领域表现的基准。

**EN** In practice, a comprehensive design task commonly need to combine of both recognition and understanding. Building upon the framework delineated in the comprehensive design survey by Huang et al. (2023), we categorize the design tasks into two distinct levels: the design element level and the overall design level. The former level focus on the detailed dimension of design and different type of elements are considered separately. In this level, our focus is centered on three fundamental components: color, typography and layout. For each, we consider both the dimensions of aesthetic harmony and semantic conveyance. While in overall design level, we focus on the overall feel of the whole design, usually consider different elements together. To this end, we orchestrate a comprehensive set of eight tasks, the details of which are illustrated in Figure2. For evaluation, we apply GPT-4 to evaluate results automatically, which gains similar performance with human annotators but is more stable and cheaper than human.

**ZH** 在实践中，一项完整的设计任务通常需要把识别与理解结合起来。基于 Huang 等（2023）在综合设计综述中勾勒的框架，我们把设计任务划分为两个层面：设计元素层面与整体设计层面。前者关注设计的细节维度，分别考虑不同类型的元素；在该层面，我们聚焦于三个基本要素：色彩、字体与版式，并对每个要素同时考察美学和谐与语义传达两个维度。而在整体设计层面，我们关注整个设计的整体观感，通常把不同元素放在一起考虑。为此，我们编排了一套共八项任务的完整集合，其细节如图 2 所示。在评价方面，我们采用 GPT-4 自动评价结果，其表现与人类标注者相近，但更稳定且成本更低。

**EN** Besides the evaluation of existing baseline models, we delve into analytical studies to explore how prompt effect MLLMs performance. In order to investigate the variance in model performance with different system prompts and the prompt refinement capabilities of various LLMs, we design a experiment by employing multiple LLMs to rewrite the questions in benchmark. We find that the model with better performance in original task appears to be more robust under different prompts. Besides, refinements using the corresponding LLMs of MLLMs consistently lead to performance improvements.

**ZH** 除评价现有基线模型外，我们还深入分析提示词如何影响 MLLM 的表现。为考察不同系统提示词下模型性能的差异，以及不同 LLM 的提示词改写能力，我们设计了一项实验，用多个 LLM 重写基准中的问题。我们发现，在原始任务上表现更好的模型在不同提示词下似乎更为稳健；此外，用 MLLM 自身对应的 LLM 进行改写，总能带来性能提升。

**EN** Moreover, design knowledge is essential as training of MLLMs lacks design task related data. To equip MLLMs with design knowledge in simple methods, we build up experiments to introduce additional information to prompt in two distinct types: textual and visual information. The experiment results indicate that both types of information are effective, and the direct addition of visual examples leads to substantially greater enhancements in performance compared to textual descriptions alone.

**ZH** 此外，由于 MLLM 的训练缺少与设计任务相关的数据，设计知识十分必要。为以简便的方式为 MLLM 配备设计知识，我们构建实验，向提示词中引入两类额外信息：文本信息与视觉信息。实验结果表明，两类信息都有效，而直接加入视觉样例相比仅加入文本描述带来显著更大的性能提升。

**EN** Our main contributions are listed as follow:

**ZH** 我们的主要贡献如下：

**EN** • To the best of our knowledge, we are the first to conduct a detailed and comprehensive benchmark of design understanding for MLLMs. To facilitate this evaluation, we have curated and re-annotated multiple datasets, and introduce a new dataset for the recognition in layout to enrich the scope of assessment. We test 9 multimodal LLMs, including GPT-4 Vision, Gemini Pro Vision. For evaluation, we employ GPT-4 to measure the distance between ground truth and model outputs.

**ZH** • 据我们所知，我们首次针对 MLLM 的设计理解能力开展了细致而全面的基准评测。为支持该评测，我们整理并重新标注了多个数据集，并引入了一个用于版式识别的新数据集以丰富评测范围。我们测试了 9 个多模态大语言模型，包括 GPT-4 Vision 与 Gemini Pro Vision。评价方面，我们采用 GPT-4 来衡量标准答案与模型输出之间的距离。

**EN** • We conduct multiple experiments to refine prompts within the benchmark along with two dimensions: Firstly, to explore the variance of different MLLMs and the prompt refining capability of different LLMs, we conduct a experiments by using LLMs to rewrite the questions. Experiment results show the robustness of better performance models under different prompts and the efficiency when refining prompt using MLLM’s own LLM. Secondly, we incorporate the supplementary knowledge about design tasks to the questions in both text and image types. Experiment results show that adding image type of information directly results in a higher performance gain compared to text.

**ZH** • 我们在基准内沿两个维度开展了多项提示词优化实验：第一，为考察不同 MLLM 的差异以及不同 LLM 的提示词改写能力，我们用 LLM 重写问题开展了一项实验；实验结果表明，性能更好的模型在不同提示词下更为稳健，而用 MLLM 自身的 LLM 改写提示词更为有效。第二，我们把与设计任务相关的补充知识以文本与图像两种类型加入问题；实验结果表明，直接加入图像类型的信息比文本带来更高的性能增益。

**EN** 2 Related Work

**ZH** 2 相关工作

**EN** 2.1 Graphic Design

**ZH** 2.1 平面设计

**EN** In recent years, a growing interest has emerged in graphic design. Pioneering researches conducted in this field include tasks such as layout generation Yang et al. (2021); Inoue et al. (2023), color scheme suggestion Bahng et al. (2018), and font extraction Zhao et al. (2018b). These tasks can be divided into two distinct levels as outlined by Huang et al. (2023): the element level and the overall design level. At the element level, the goal is to understand or generate a single category of elements separately, while at the overall design level, elements are considered comprehensively. For the element level, there are three basic design elements: color, font, and layout. Color theory has been widely studied, with tasks focusing on both understanding and generation Bahng et al. (2018); Qiu et al. (2022). These tasks may involve building a comprehension task for understanding the color palette or automatically suggesting color palettes for a given design. Fonts are yet another critical element, with research focusing on font extraction Zhao et al. (2018b), understanding Virkus (2022), and generation Zhao et al. (2018a) tasks. For layout elements, there are numerous studies on layout generation, which aim to generate layouts that are visually appealing and convey a clear mood.

**ZH** 近年来，平面设计引起了越来越多的关注。该领域的开创性研究包括版式生成（Yang 等，2021；Inoue 等，2023）、配色方案推荐（Bahng 等，2018）与字体提取（Zhao 等，2018b）等任务。如 Huang 等（2023）所归纳，这些任务可分为两个层面：元素层面与整体设计层面。在元素层面，目标是单独理解或生成某一类元素；而在整体设计层面，则综合地考虑各元素。在元素层面，有三个基本设计要素：色彩、字体与版式。色彩理论已被广泛研究，任务涵盖理解与生成两个方面（Bahng 等，2018；Qiu 等，2022），这些任务可能包括构建理解调色板的理解型任务，或为给定设计自动推荐配色。字体是另一项关键要素，研究聚焦于字体提取（Zhao 等，2018b）、字体理解（Virkus，2022）与字体生成（Zhao 等，2018a）等任务。对于版式要素，大量研究关注版式生成，旨在生成视觉上美观且能传达明确情绪的版式。

**EN** Despite the progress in these individual areas, the challenge of capturing and combining features of different design elements remains. Lin et al. (2023) is the first to build a design benchmark for text-to-image tasks and show comprehensive results of Dalle-3 OpenAI (2023a). The tasks (color, font, layout, and style) in their benchmark are considered and integrated into the task structure of our benchmark. Building upon this foundation, our work presents a more comprehensive image-to-text task structure by adding visual and semantic aspects.

**ZH** 尽管这些各自独立的领域都有进展，如何捕捉并组合不同设计元素的特征仍是难题。Lin 等（2023）首次为文本到图像任务构建了设计基准，并展示了 Dalle-3（OpenAI，2023a）的综合结果；其基准中的任务（色彩、字体、版式与风格）被纳入我们基准的任务结构。在此基础上，本文通过加入视觉与语义两个方面，提出了一个更完整的图像到文本任务结构。

**EN** 2.2 Multimodal LLMs

**ZH** 2.2 多模态大语言模型

**EN** Multimodal large language models, particularly those that integrate vision and language, such as GPT-4 Vision OpenAI (2023b) and Gemini Team et al. (2023), have shown remarkable capabilities. These models excel not only in basic recognition tasks like object identification but also in more nuanced understanding, such as grasping the humor or sentiment behind memes.

**ZH** 多模态大语言模型，尤其是融合视觉与语言的模型，如 GPT-4 Vision（OpenAI，2023b）与 Gemini（Team 等，2023），已展现出卓越的能力。这些模型不仅在物体识别等基础识别任务上表现出色，在更细致的理解上也同样优秀，例如领会表情包背后的幽默或情绪。

**EN** The landscape includes not only commercial models like GPT-4 Vision OpenAI (2023b) but also a burgeoning suite of open-source alternatives. The BLIP series Li et al. (2023c); Dai et al. (2023) and MiniGPT-4 Zhu et al. (2023), which merge language models with vision encoders, have delivered promising outcomes in tasks that require visual comprehension. LLaVA Liu et al. (2023b), on the other hand, has pioneered in generating data that guide models in following multimodal instructions, thereby enhancing their conversational abilities. Furthermore, models like CM3Leon Yu et al. (2023a), DreamLLM Dong et al. (2023), and Emu Sun et al. (2023) have integrated both image understanding and generation into a unified framework. The evolution of multimodal LLMs Li et al. (2023a); Zhang et al. (2023); Ye et al. (2023); Bai et al. (2023); Awadalla et al. (2023) continues with improvements driven by the incorporation of grounding data, architectural refinements, and other advancements.

**ZH** 相关格局既包括 GPT-4 Vision（OpenAI，2023b）等商业模型，也包括迅速壮大的开源替代品。BLIP 系列（Li 等，2023c；Dai 等，2023）与 MiniGPT-4（Zhu 等，2023）把语言模型与视觉编码器相结合，在需要视觉理解的任务上取得了可喜成果；LLaVA（Liu 等，2023b）则在生成引导模型遵循多模态指令的数据方面开创了先河，从而增强了模型的对话能力。此外，CM3Leon（Yu 等，2023a）、DreamLLM（Dong 等，2023）与 Emu（Sun 等，2023）等模型已把图像理解与生成整合进统一框架。多模态大语言模型的演进（Li 等，2023a；Zhang 等，2023；Ye 等，2023；Bai 等，2023；Awadalla 等，2023）在引入定位数据、架构改进等推动下持续前行。

**EN** This paper examines a collection of these models, spanning both open-source and proprietary frameworks, with an aim to assess their proficiency in interpreting images within the specialized context of graphic design.

**ZH** 本文考察上述模型的一个集合，涵盖开源与专有框架，旨在评估它们在平面设计这一专门语境下解读图像的能力。

**EN** The rapid development of multimodal large language models raise the important issue of how to accurately measure their comprehension abilities. Common benchmarks such as captioning Chen et al. (2015); Agrawal et al. (2019) and visual question answering Goyal et al. (2017); Gurari et al. (2018); Hudson and Manning (2019) have been used to gauge these models’ understanding, yet these metrics offer a somewhat limited perspective. To address this limitation, recent efforts Yu et al. (2023b); Fu et al. (2023); Li et al. (2023b); Liu et al. (2023c) have introduced a variety of open-ended evaluation benchmarks that challenge models from multiple dimensions, including cognition and reasoning. Despite these advancements, there remains a gap in evaluating the models’ proficiency in specific domains, such as graphic design.

**ZH** 多模态大语言模型的快速发展提出了一个重要问题：如何准确衡量它们的理解能力。图像描述（Chen 等，2015；Agrawal 等，2019）与视觉问答（Goyal 等，2017；Gurari 等，2018；Hudson 和 Manning，2019）等常见基准已被用于衡量这些模型的理解能力，但这些指标提供的视角较为有限。为缓解这一局限，近期工作（Yu 等，2023b；Fu 等，2023；Li 等，2023b；Liu 等，2023c）引入了多种开放式评价基准，从认知与推理等多个维度挑战模型。尽管有这些进展，在评估模型于平面设计等特定领域的能力方面仍存在空白。

**EN** This paper aims to fill this void by proposing a new benchmark tailored to assess the ability of multimodal LLMs in understanding content within the nuanced field of graphic design, thereby providing a more detailed and domain-specific metric for evaluating the capabilities of these sophisticated models.

**ZH** 本文旨在填补这一空白，提出一个新的基准，专门评估多模态大语言模型在平面设计这一微妙领域中理解内容的能力，从而为评价这些复杂模型的能力提供一个更细致、面向特定领域的度量。

**EN** 3 DesignProbe

**ZH** 3 DesignProbe

**EN** The proposed benchmark comprises a total of eight tasks that evaluate the performance of Multimodal Large Language Models (MLLMs) in design. Below is a detailed introduction to the tasks and the evaluation method.

**ZH** 所提出的基准共包含八项任务，用于评价多模态大语言模型（MLLM）在设计上的表现。下文详细介绍各项任务与评价方法。

**EN** 3.1 Tasks

**ZH** 3.1 任务

**EN** In order to comprehensively assess design capabilities, we prioritize two distinct levels of design: the element level and the overall design level. At the element level, tasks are categorized into two principal aspects: (1) attribute recognition for the visual component and (2) understanding for the semantic dimension. Within each aspect, we focus on three principal design elements: color, font, and layout. Additionally, at the overall design level, we focus on the tasks of style classification and visual metaphor. Figure 2 depicts the framework, which includes a total of eight tasks.

**ZH** 为全面评估设计能力，我们优先考察两个不同层面的设计：元素层面与整体设计层面。在元素层面，任务分为两个主要方面：（1）面向视觉成分的属性识别；（2）面向语义维度的理解。在每个方面中，我们聚焦三个主要设计元素：色彩、字体与版式。此外，在整体设计层面，我们关注风格分类与视觉隐喻两项任务。图 2 描绘了这一框架，共包含八项任务。

**EN** In the element level, we conduct attribute recognition tasks as follows:

**ZH** 在元素层面，我们开展如下属性识别任务：

**EN** • Task #1: Color Theme. The objective is to evaluate the models’ ability to identify the primary colors in a design, a critical skill for discerning color harmony and thematic color transitions. We established this task by randomly sampling 50 design instances from Crello Yamaguchi (2021), computing the most frequent colors in a design, and then manually reviewing these examples. For the query structure, we compiled a set of commonly used color palettes, and the models are required to choose their output colors from this predefined selection.

**ZH** • 任务 #1：色彩主题。目标是评价模型识别设计中主色的能力，这是辨别色彩和谐与主题色彩过渡的一项关键技能。我们从 Crello（Yamaguchi，2021）中随机抽取 50 个设计样本，计算设计中最频繁出现的颜色，然后人工复核这些样例来构建该任务。在查询结构方面，我们整理了一组常用调色板，模型需从这一预定义集合中选取其输出颜色。

**EN** • Task #2: Font Extraction. The task recognizes the font face from a design image where the font is outlined in red. To construct this task, we prompt the model with a single-choice question based on instances randomly sampled from CTXFont Zhao et al. (2018b).

**ZH** • 任务 #2：字体提取。该任务从设计图像中识别以红色描边标出的字体。为构建该任务，我们基于从 CTXFont（Zhao 等，2018b）随机抽取的样本，向模型提出单项选择题。

**EN** • Task #3: Negative Space Detection. This task focuses on the detection of negative space, which provides a clear area where elements can be placed without disrupting the visual balance within a design. The model is tasked with analyzing a background image to determine a suitable location for the title. We obtained the background images from Midjourney. After professional designers manually annotated the optimal title locations, the instances were converted into single-choice questions.

**ZH** • 任务 #3：负空间检测。该任务关注负空间的检测——负空间提供了可以放置元素而不破坏设计视觉平衡的清晰区域。模型的任务是分析一张背景图像，为标题确定合适的位置。背景图像取自 Midjourney。在专业设计师人工标注出最优标题位置后，这些样本被转换为单项选择题。

**EN** Semantic understanding tasks are outlined as follows:

**ZH** 语义理解任务如下：

**EN** • Task #4: Color Meaning. Different combinations of colors can convey different meanings, and certain color palettes may symbolize specific themes or moods. For example, black is rarely found in the color palette associated with “weddings & celebrations”. We utilize the PAT dataset Bahng et al. (2018) to evaluate this ability. We randomly sampled and manually filtered out examples with ambiguous meanings. The remaining 50 distinct examples were converted into multiple-choice questions.

**ZH** • 任务 #4：色彩含义。不同的色彩组合可以传达不同的含义，某些配色可能象征特定的主题或情绪。例如，黑色很少出现在与“婚礼与庆典”相关的配色中。我们利用 PAT 数据集（Bahng 等，2018）来评价这一能力，随机抽样并人工滤除含义模糊的样例，把剩余的 50 个不同样例转换为多项选择题。

**EN** • Task #5: Font Style. In addition to recognizing font faces, we expect the model to understand the styles of the given fonts. This is crucial for ensuring that the fonts are consistent with the overall design’s mood or theme. We derived the annotations for the fonts and their styles from the Dafonts dataset Virkus (2022) and transformed them into a single-choice question format.

**ZH** • 任务 #5：字体风格。除识别字体外，我们还期望模型理解给定字体的风格，这对确保字体与整体设计的情绪或主题一致至关重要。我们从 Dafonts 数据集（Virkus，2022）中获得字体及其风格的标注，并将其转换为单项选择题形式。

**EN** • Task #6: Visual Importance. Understanding the visual center is essential for layout comprehension and can provide significant feedback for design generation. This task presents the model with a design image and requires it to identify the visual center of the design. We obtained the input images from the Imp-1k dataset Fosco et al. (2020). Since producing a salience map is challenging for MLLMs and difficult to assess, we categorized the ground truth map into different position descriptions using a 3x3 grid. This task is also formulated as a single-choice question.

**ZH** • 任务 #6：视觉重要性。理解视觉中心对版式理解至关重要，并能为设计生成提供重要反馈。该任务向模型呈现一张设计图像，要求它识别设计的视觉中心。输入图像取自 Imp-1k 数据集（Fosco 等，2020）。由于生成显著性图对 MLLM 而言有难度且难以评估，我们用一个 3x3 网格把标准答案图标注为不同的位置描述。该任务同样被构造为单项选择题。

**EN** For overall design level:

**ZH** 整体设计层面：

**EN** • Task #7: Overall Style. To test the overall design feel of MLLMs, this task asks models to identify the visual style of a given poster from the Poster dataset Zhao et al. (2018c). We sampled 50 different examples with a uniform distribution of styles, annotated them with the help of multiple professional designers, and transformed the instances into single-choice questions.

**ZH** • 任务 #7：整体风格。为测试 MLLM 对整体设计观感的把握，该任务要求模型从 Poster 数据集（Zhao 等，2018c）中识别给定海报的视觉风格。我们抽取了 50 个风格分布均匀的不同样例，在多名专业设计师协助下完成标注，并把样本转换为单项选择题。

**EN** • Task #8: Visual Metaphor. This task delves deeper into understanding the semantic level of design. Visual metaphors often involve using common objects in creative and unfamiliar ways, which can make it challenging to provide the correct caption and the true metaphorical meaning. The designs and explanations were derived from the VisMet dataset Steen et al. (2010). After manual filtering, these instances were transformed into open-ended questions.

**ZH** • 任务 #8：视觉隐喻。该任务深入到对设计语义层面的理解。视觉隐喻常以创意而陌生的方式使用常见物体，这使得给出正确描述与真实隐喻含义变得困难。设计与解释取自 VisMet 数据集（Steen 等，2010），经人工过滤后，这些样本被转换为开放式问题。

<!-- [原子块 · table] Evaluators Detailed Acc. Correct (22) Partially (7) Incorrect (20) Irrelevant (1) GPT-3.5-turbo 95.5 100.0 10.0 0.00 60.0 GPT-4 100.0 100.0 75.0 100.0 90.0 -->

**EN** Table 1: The results(%) of GPT-4 and GPT-3.5-turbo as evaluators. Detailed accuracy of each category are shown. The number of cases for each category in the test set is indicated in parentheses following the category. GPT-4 achieves an overall accuracy of 90%, demonstrating its performance to be quite comparable to that of a human evaluator, while significantly reducing labor costs.

**ZH** 表 1：GPT-4 与 GPT-3.5-turbo 作为评价器的结果（%）。表中列出各类别的详细准确率；类别后括号中的数字表示测试集中该类别的样本数。GPT-4 的总体准确率达到 90%，表明其表现与人类评价者相当接近，同时大幅降低了人力成本。

**EN** 3.2 GPT-4 Evaluator

**ZH** 3.2 GPT-4 评价器

**EN** Although our questions are single-choice, the model still tends to produce open-ended responses. This makes it impractical to compute the performance by simple rules. Therefore, we introduce an automatic evaluation method using GPT-4. Given the question, the golden answer and the MLLMs’ generated output, the GPT-4 evaluator is asked to assign a grade by comparing the output with the standard answer. We set the grading scale as [“Correct”, “Partially Correct”,“Incorrect”, “Irrelevant”]. Below is the detailed descriptions of each grade:

**ZH** 尽管我们的题目是单选形式，模型仍倾向于给出开放式回答，这使得用简单规则计算性能变得不切实际。为此，我们引入一种基于 GPT-4 的自动评价方法：给定问题、标准答案与 MLLM 的生成输出，GPT-4 评价器被要求通过把输出与标准答案作比较来给出等级。我们把评分等级设定为 [“正确”、“部分正确”、“错误”、“无关”]。以下是各等级的详细说明：

**EN** • Correct The style identified in the model’s output matches the standard answer perfectly.

**ZH** • 正确：模型输出中识别出的风格与标准答案完全吻合。

**EN** • Partially Correct This grade applies in two cases: (1) The style is correctly identified, but the model’s answer to the question is wrong. (2) The style is incorrectly identified, but the elements of the style are the same as those in the standard answer.

**ZH** • 部分正确：该等级适用于两种情况：（1）风格识别正确，但模型对问题的回答错误。（2）风格识别错误，但风格中的元素与标准答案中的元素相同。

**EN** • Incorrect The model’s output incorrectly identifies the style of the overall design and the elements within.

**ZH** • 错误：模型输出错误地识别了整体设计的风格及其中的元素。

**EN** • Irrelevant The model’s output does not address the question of style at all.

**ZH** • 无关：模型输出完全没有回应风格问题。

**EN** To better estimate the performance of the GPT-4 evaluator compared with a human, we build up a test set of 50 questions manually annotated by multiple annotators. We also test the performance of GPT-3.5-turbo with the same prompt. As shown in Table 1, GPT-4 achieves an overall accuracy of 90%, which demonstrates that GPT-4 can perform quite similarly to the human evaluator and significantly reduce expensive labor costs.

**ZH** 为更好地估计 GPT-4 评价器相对人类的表现，我们构建了一个由多名标注者人工标注的 50 道题目的测试集；我们还用相同提示词测试了 GPT-3.5-turbo 的表现。如表 1 所示，GPT-4 的总体准确率达到 90%，表明 GPT-4 的表现与人类评价者相当接近，并能显著降低昂贵的人力成本。

<!-- [原子块 · table] Models Element Overall Design Average Recognition Understanding #7 Style #8 Metaphor #1 Color #2 Font #3 Layout #4 Color #5 Font #6 Layout random 20.0 25.0 25.0 25.0 25.0 25.0 25.0 0.0 21.3 InstructBL -->

**EN** Table 2: DesignProbe evaluation results (%) of different MLLMs. All the value in this table is normalized to 1, larger is better. The average values in last column is the average performance of the current MLLM. The table is sorted by average performance. For each column, the highest, the second, and the third highest figures are highlighted by purple, green and pink backgrounds.

**ZH** 表 2：不同 MLLM 在 DesignProbe 上的评价结果（%）。表中所有数值均归一化到 1，越大越好。最后一列的平均值为当前 MLLM 的平均性能，表格按平均性能排序。每一列中，最高、第二与第三高的数值分别以紫色、绿色与粉色背景标出。

<!-- [原子块 · table] Models based LLM Ori. LLaMA2 Re. Vicuna Re. GPT-4 Re. Gemini Re. std. Otter MPT 47.5 38.0 52.0 33.0 48.0 7.9 mPLUG-OWL2 LLaMA2 66.5 77.0 76.5 70.0 74.0 4.5 LLaVA Vicuna v1.5 82.0 79.5 83.5 80.0 81.5 1 -->

**EN** Table 3: The evaluation results (%) of different MLLMs using different refined system prompts. Ori represents the original questions in DesignProbe. Re. is the abbreviation of “refined”. std. represent the standard deviation of each row. The corresponding MLLMs with its based LLM are highlighted by gray. The best performance of each MLLMs is in bold.

**ZH** 表 3：不同 MLLM 使用不同改写后系统提示词的评价结果（%）。Ori 表示 DesignProbe 中的原始问题；Re. 是“改写后”（refined）的缩写；std. 表示每一行的标准差。MLLM 与其所基于的 LLM 以灰色底纹标示。每个 MLLM 的最佳性能以粗体标出。

<!-- [原子块 · img]  -->

**EN** Figure 3: The examples of adding example into prompt.

**ZH** 图 3：向提示词中加入示例的样例。

<!-- [原子块 · img]  -->

**EN** Figure 4: The experiment results (%) of adding additional different types of information to the questions. Ori in green represents the performance under original questions in DesignProbe. + test in yellow represents adding text description to the questions. + concated image in pink represents combining multiple image examples into one image due to the unsupportment of multiple images input in LLaVA. + image means adding multiple image examples.

**ZH** 图 4：向问题中加入不同类型附加信息的实验结果（%）。绿色的 Ori 表示在 DesignProbe 原始问题下的性能；黄色的 + test 表示向问题中加入文本描述；粉色的 + concated image 表示由于 LLaVA 不支持多图输入，把多个图像示例合并为一张图像；+ image 表示加入多个图像示例。

<!-- [原子块 · img]  -->

**EN** Figure 5: Error cases of overall design level tasks. In case 1, the model fails to recognize the creative use of record. In case2, the model fails to recognize the abstract represent of theater seats in car.

**ZH** 图 5：整体设计层面任务的错误案例。在案例 1 中，模型未能识别唱片的创意化使用；在案例 2 中，模型未能识别车内对剧院座椅的抽象表现。

**EN** 4 Experiments

**ZH** 4 实验

**EN** In this section, we conduct extensive experiments on our design benchmark to evaluate a total of nine MLLMs, comprising both open-source and proprietary models.

**ZH** 本节在我们的设计基准上开展了大量实验，共评价九个 MLLM，涵盖开源与专有模型。

**EN** To mitigate any positional bias of the correct answer among the various options, we repeat each question four times with different positions of the correct answer, resulting in a total of 200 questions per task. The results presented in Table 2 are averaged by position. More detailed results will be provided in the Supplementary Material.

**ZH** 为缓解正确答案在各选项中位置偏置的影响，我们把每道题重复四次，每次正确答案的位置不同，使每项任务共产生 200 道题。表 2 中的结果按位置取平均。更详细的结果将在补充材料中给出。

**EN** 4.1 Evaluated Models

**ZH** 4.1 被评测模型

**EN** We evaluate a total of nine MLLMs, selecting the version of each model that demonstrates the best possible performance.

**ZH** 我们共评价九个 MLLM，为每个模型选择表现最佳的版本。

**EN** LLaVA v1.5 Liu et al. (2023a) integrates vision and language capabilities through a simple projection layer. We use LLaVA v1.5, which is based on the LLM Vicuna v1.5 13B Zheng et al. (2023).

**ZH** LLaVA v1.5（Liu 等，2023a）通过一个简单的投影层整合视觉与语言能力。我们使用的 LLaVA v1.5 基于 LLM Vicuna v1.5 13B（Zheng 等，2023）。

**EN** Otter Li et al. (2023a) facilitates multimodal in-context instruction tuning, building upon the OpenFlamingo Awadalla et al. (2023) model. We evaluate the “Otter-image-MPT7B” version.

**ZH** Otter（Li 等，2023a）在 OpenFlamingo（Awadalla 等，2023）模型之上实现了多模态上下文指令微调。我们评测的是“Otter-image-MPT7B”版本。

**EN** LLaMA-Adapter-v2 Zhang et al. (2023) exclusively employs language data for instruction tuning and establishes a connection between vision and language in a parameter-efficient way. This model is based on LLaMA 7B Touvron et al. (2023a).

**ZH** LLaMA-Adapter-v2（Zhang 等，2023）仅使用语言数据做指令微调，并以参数高效的方式建立视觉与语言之间的联系。该模型基于 LLaMA 7B（Touvron 等，2023a）。

**EN** MiniGPT v2 Chen et al. (2023) directly projects visual features into LLM feature space using a linear layer and employs unique identifiers for different tasks during training. We use “MiniGPT v2” version, which is based on LLaMA2 7B Touvron et al. (2023b).

**ZH** MiniGPT v2（Chen 等，2023）用一个线性层把视觉特征直接投影到 LLM 的特征空间，并在训练时为不同任务采用独特标识符。我们使用基于 LLaMA2 7B（Touvron 等，2023b）的“MiniGPT v2”版本。

**EN** InstructBLIP Dai et al. (2023) builds upon BLIP-2Li et al. (2023c) and performs instruction tuning with 26 datasets. We test the model based on Vicuna v1.1 13B.

**ZH** InstructBLIP（Dai 等，2023）构建于 BLIP-2（Li 等，2023c）之上，并用 26 个数据集做指令微调。我们测试的是基于 Vicuna v1.1 13B 的模型。

**EN** mPLUG-OWL2 Ye et al. (2023) utilizes the language decoder as a universal interface to handle different modalities through shared functional modules. We evaluate the “mplug-owl2-llama2-7b” version.

**ZH** mPLUG-OWL2（Ye 等，2023）以语言解码器作为通用接口，通过共享功能模块处理不同模态。我们评测的是“mplug-owl2-llama2-7b”版本。

**EN** BLIP2 Li et al. (2023c) incorporates a Q-Former module to align image features with the LLM token space. This model is based on FLAN-T5-XXL Chung et al. (2022) with a parameter count of 12 billion.

**ZH** BLIP2（Li 等，2023c）引入 Q-Former 模块，把图像特征与 LLM 的词元空间相对齐。该模型基于 FLAN-T5-XXL（Chung 等，2022），参数量为 120 亿。

**EN** Gemini Pro Vision Team et al. (2023), GPT-4 Vision OpenAI (2023b) are evaluated through their respective APIs. Gemini Pro Vision is initially trained using a combination of image and text data. GPT-4 Vision, a large-scale MLLM, performs exceptionally well across various benchmarks Liu et al. (2023c); Yue et al. (2023).

**ZH** Gemini Pro Vision（Team 等，2023）与 GPT-4 Vision（OpenAI，2023b）通过各自的 API 进行评测。Gemini Pro Vision 最初使用图像与文本数据组合训练；GPT-4 Vision 是一个大规模 MLLM，在各种基准上表现极为出色（Liu 等，2023c；Yue 等，2023）。

**EN** 4.2 MLLM Performance in DesignProbe

**ZH** 4.2 MLLM 在 DesignProbe 上的表现

**EN** Our benchmark evaluation results are listed in Table 2. From these, we summarize our observations into three interesting findings.

**ZH** 我们的基准评价结果列于表 2。由此我们把观察归纳为三点有趣的发现。

**EN** (1) Overall: Tasks are challenging. The highest overall average performance is achieved by GPT-4 Vision at 59.4%. Despite its significant lead over other baseline models, it is still not enough to meet the passing threshold of 60%, leaving considerable room for exploration.

**ZH** （1）总体：任务具有挑战性。最高的总平均性能由 GPT-4 Vision 取得，为 59.4%。尽管它大幅领先其他基线模型，这一成绩仍不足以达到 60% 的及格线，留下了相当大的探索空间。

**EN** (2) Color vs. Font vs. Layout: Models may be more experienced in color than others. As the results shown in column #1 Color and #4 Color in Table 2, we observe an advantage in color-related tasks (with GPT-4 Vision scoring 72.0% and 43.5% in color and font). The challenging with font tasks for MLLMs may stem from lacking font-related data during training and instruction tuning. In terms of layout tasks, MLLMs appears to struggle with spatial relationships within design elements, which leads to the performance drop in these related tasks.

**ZH** （2）色彩 vs. 字体 vs. 版式：模型在色彩上可能比其他方面更有经验。如表 2 中第 #1 列色彩与第 #4 列色彩的结果所示，我们观察到模型在色彩相关任务上具有优势（GPT-4 Vision 在色彩与字体上分别得到 72.0% 与 43.5%）。MLLM 在字体任务上表现吃力，可能源于训练与指令微调时缺少字体相关数据。在版式任务方面，MLLM 似乎难以把握设计元素之间的空间关系，导致相关任务的性能下降。

**EN** Interestingly, there is a performance drop between BLIP-2 and InstructBLIP in column #1 Color and #4 Color in Table 2. Given that InstructBLIP is essentially BLIP-2 with added instructional tuning, this drop may reveals a trade off between aligning with human preferences and optimizing the model capability.

**ZH** 有意思的是，在表 2 的第 #1 列色彩与第 #4 列色彩上，BLIP-2 与 InstructBLIP 之间出现了性能下降。鉴于 InstructBLIP 本质上是在 BLIP-2 之上加入了指令微调，这一下降可能揭示了与人类偏好相对齐与优化模型能力之间的一种权衡。

**EN** (3) Metaphor: The low performance can be primarily attributed to the models’ inability to recognize design objects accurately. Task#8 Visual Metaphor is complex as it requires to recognize the abstract design elements and understanding the metaphor they represent. After error analysis, we find there are no instances of ’Correct caption, Wrong reasoning’ errors, but an 8% error rate occurred in cases of ’Correct reasoning, Wrong caption’. This suggests that the main obstacle in metaphor tasks is the models’ ability to correctly recognize design objects.

**ZH** （3）隐喻：性能偏低主要可归因于模型无法准确识别设计对象。任务 #8 视觉隐喻较为复杂，它要求识别抽象的设计元素并理解其所代表的隐喻。经过错误分析，我们发现不存在“描述正确、推理错误”的错误案例，而“推理正确、描述错误”的错误率为 8%。这说明隐喻任务中的主要障碍在于模型正确识别设计对象的能力。

**EN** 4.3 Exploration of Prompt Refining

**ZH** 4.3 提示词优化的探索

**EN** We conduct multiple experiments to refine prompts within DesignProbe along two distinct dimensions: firstly, we focus on rewriting the task description to enhance clarity and precision without introducing additional information; secondly, we enrich the prompts by providing more contextual and task-related data.

**ZH** 我们沿两个不同维度在 DesignProbe 内开展多项提示词优化实验：其一，重写任务描述以提升清晰度与准确性，不引入额外信息；其二，通过提供更多与上下文和任务相关的数据来丰富提示词。

**EN** 4.3.1 Prompt Rewriting

**ZH** 4.3.1 提示词改写

**EN** To investigate model response variance to prompts, we design an experiment involving multiple LLMs to refine the original prompt. We then verify the outcomes on Task#7 Style Classification. These LLMs are selected based on the underlying language models of different MLLMs. Evaluating these MLLMs with the refined prompts, we obtain the results shown in Table 3. We summarize three key findings as follows:

**ZH** 为考察模型对提示词的响应差异，我们设计了一项实验，用多个 LLM 改写原始提示词，并在任务 #7 风格分类上验证结果。这些 LLM 依据不同 MLLM 所基于的语言模型选取。用改写后的提示词评价这些 MLLM，我们得到表 3 所示结果，并归纳出三点关键发现：

**EN** • The better an MLLM performs on a task, the more robust it is to different prompts. For instance, while Otter exhibits significant variance (7.9%) under different prompts, GPT-4 Vision demonstrates considerable robustness with only a 1.2% variance. Furthermore, the standard deviation can shed light on MLLM performance, as a small decrease in this variance is often caused by an unsuitable system prompt.

**ZH** • MLLM 在某项任务上表现越好，对不同提示词就越稳健。例如，Otter 在不同提示词下表现出显著方差（7.9%），而 GPT-4 Vision 则表现出相当的稳健性，方差仅为 1.2%。此外，标准差可以反映 MLLM 的性能，因为该方差的小幅下降往往是由不合适的系统提示词引起的。

**EN** • There is always improvement when refining prompts using MLLMs’ corresponding base LLMs. For open-source models, employing their own base LLMs yields the best performance.

**ZH** • 用 MLLM 对应的基础 LLM 改写提示词总能带来提升。对开源模型而言，使用其自身的基础 LLM 能取得最佳性能。

**EN** • Refinement in the language aspect alone generally leads to gains, while other types of refinement may not. To assess the true refinement capabilities of different LLMs, we instruct each LLM to refine questions in their preferred manner using the exact same prompt. Surprisingly, we find that Vicuna consistently performs the best, in contrast to GPT-4. Upon detailed examination of the refined questions, we notice that Vicuna simply rewrites the prompt without adding any text, whereas GPT-4 tends to include additional descriptions of steps for solving the questions. To confirm the impact of these additional texts, we remove them and discover that this action yields the best performance for LLaVA, with an 85% success rate.

**ZH** • 仅在语言层面进行改写通常会带来增益，而其他类型的改写则未必。为评估不同 LLM 真正的改写能力，我们指示每个 LLM 用完全相同的提示词以其偏好的方式改写问题。令人意外的是，我们发现 Vicuna 始终表现最佳，与 GPT-4 形成对比。细致考察改写后的问题后我们注意到，Vicuna 只是重写提示词而不添加任何文本，而 GPT-4 倾向于加入额外的解题步骤描述。为确认这些附加文本的影响，我们把它们移除，结果发现这一操作使 LLaVA 取得最佳性能，成功率为 85%。

**EN** 4.3.2 Incorporating Supplementary Information

**ZH** 4.3.2 引入补充信息

**EN** The original prompts in DesignProbe are relatively basic and lack detailed task descriptions, potentially leading to confusion for models. To mitigate this, we introduce supplementary information to prompts. Our experiment involves the addition of two types of information: textual descriptions and visual examples. We present the examples of the enhanced prompts for each format in Figure 3. To ensure a consistent level of information gain when adding task details, we initially utilize GPT-4 Vision to generate text descriptions for the provided image examples. We then perform minimal manual refinements where necessary. The results of the experiment for Task#5 Font Style are illustrated in Figure 4.

**ZH** DesignProbe 中的原始提示词相对基础，缺少详尽的任务描述，可能导致模型困惑。为缓解这一点，我们向提示词中引入补充信息。实验中加入两类信息：文本描述与视觉示例。我们在图 3 中给出每种格式下增强提示词的示例。为保证加入任务细节时信息增益水平一致，我们首先用 GPT-4 Vision 为所给图像示例生成文本描述，随后在必要时做最小限度的人工修改。任务 #5 字体风格的实验结果如图 4 所示。

**EN** Below are three interesting findings from this experiment:

**ZH** 该实验有三点有趣的发现：

**EN** • Incorporating textual descriptions consistently enhances performance. As demonstrated in Figure 4, there is an improvement of 3.0% for LLaVA v1.5 and 2.5% for GPT-4 Vision.

**ZH** • 加入文本描述总能提升性能。如图 4 所示，LLaVA v1.5 提升了 3.0%，GPT-4 Vision 提升了 2.5%。

**EN** • Adding visual examples directly results in a significantly higher performance gain compared to textual information. For instance, GPT-4 Vision experiences a 10.5% increase when supplemented with image examples, as opposed to a 2.5% increase with text alone.

**ZH** • 直接加入视觉示例相比文本信息带来显著更高的性能增益。例如，GPT-4 Vision 在补充图像示例后提升 10.5%，而仅用文本时提升 2.5%。

**EN** • Combining multiple image examples into a single composite image can be a potential workaround for models that only accept a single image input. While LLaVA does not support multiple images, we attempt to merge various image examples into one composite image, drawing inspiration from Bar et al. (2022). However, this approach appears to be counterproductive for LLaVA, as performance decreases from 43.0% to 38.5%. Conversely, when applying this method to GPT-4 Vision, the results suggest that such a technique may be beneficial, as it exhibits an opposite effect to LLaVA. This discrepancy leads us to hypothesize that LLaVA may struggle to distinguish between different image examples within a composite image, particularly in tasks requiring spatial recognition, as evidenced by its notably poor performance in layout tasks (#3, #6), which is documented in Table2.

**ZH** • 把多个图像示例合并为一张合成图像，可作为只接受单图输入的模型的一种潜在变通方案。虽然 LLaVA 不支持多图输入，我们受 Bar 等（2022）启发，尝试把多个图像示例合并为一张合成图像。然而，这一做法对 LLaVA 似乎适得其反，性能从 43.0% 降至 38.5%。相反，把该方法用于 GPT-4 Vision 时，结果表明该技术可能有益，其效果与 LLaVA 相反。这一差异使我们推测：LLaVA 可能难以区分合成图像中的不同图像示例，尤其是在需要空间识别的任务中——这可由它在版式任务（#3、#6）上的明显糟糕表现佐证，相关数据记录在表 2 中。

**EN** 4.4 Error Case Analysis

**ZH** 4.4 错误案例分析

**EN** In addition to the quantitative results presented earlier, we conduct a thorough analysis of error cases to identify the current limitations of MLLMs in design tasks.

**ZH** 除前述定量结果外，我们还对错误案例作了细致分析，以识别当前 MLLM 在设计任务中的局限。

**EN** Significant Variance Based on the Position of the Correct Option. We observe that models, such as InstructBLIP and LLaMA-Adapter v2, exhibit considerable variability in performance depending on the position of the correct option among choices A, B, C, and D. We will provide more detailed results in the supplementary materials.

**ZH** 随正确选项位置产生的显著方差。我们观察到，InstructBLIP 与 LLaMA-Adapter v2 等模型的性能会随正确选项在 A、B、C、D 中的位置不同而产生相当大的波动。我们将在补充材料中给出更详细的结果。

**EN** Deficiency in Understanding Design Elements. The models may not be well-acquainted with the tasks or the concepts involved in the tasks, as most tasks within DesignProbe are not covered by the pretraining and fine-tuning datasets of MLLMs. Taking GPT-4 Vision as an example, it exhibits poor performance in Task# 5 Font Style as shown in Table 2. However, its performance improves significantly when we supplement it with additional knowledge pertinent to the task. The disparity in performance between tasks involving color and font styles further supports this observation, as evidenced in Table 2. Although there are straightforward methods to enhance performance, a more comprehensive investigation is necessary to equip MLLMs with a robust understanding of design principles.

**ZH** 对设计元素理解不足。模型可能并不熟悉这些任务或任务中涉及的概念，因为 DesignProbe 中的多数任务并未被 MLLM 的预训练与微调数据集覆盖。以 GPT-4 Vision 为例，如表 2 所示，它在任务 #5 字体风格上表现较差；然而，当我们为其补充与该任务相关的额外知识后，其性能显著提升。色彩与字体风格两类任务之间的性能差距进一步支持了这一观察，见表 2。尽管存在提升性能的直接方法，要让 MLLM 具备对设计原则的稳健理解，仍需更全面的研究。

**EN** Challenges in Recognizing Creative Representations within Design Imagery Focusing on the general design tasks #7 and #8, models frequently struggle to generate precise captions for designs, leading to incorrect responses to subsequent questions. Design objects are often abstract and may diverge significantly from real-world imagery. For instance, as illustrated in Figure 5, in case (a), LLaVA fails to recognize the inventive representation of a record and consequently misclassifies the style; in case (b), GPT-4 Vision is unable to identify the theater seats within a car and incorrectly interprets the visual metaphor.

**ZH** 识别设计图像中创意化呈现的困难。聚焦于 #7 与 #8 这两项总体设计任务，模型经常难以为设计生成精确的描述，从而导致对后续问题的回答错误。设计对象往往是抽象的，并可能与真实世界图像有显著偏离。例如，如图 5 所示，在案例（a）中，LLaVA 未能识别唱片的创意化呈现，因而错误地分类了风格；在案例（b）中，GPT-4 Vision 无法识别车内的剧院座椅，错误地解读了视觉隐喻。

**EN** 5 Conclusion

**ZH** 5 结论

**EN** In this work, we have pioneered the creation of a comprehensive benchmark to assess design capabilities of Multi-Modal Language Models (MLLMs), a first in the field. Our benchmark includes eight tasks across two levels of design complexity: the element level and the overall design level. At the element level, we build up tasks that evaluate both the recognition of visual components and the understanding of semantic content. In each type of tasks, we focus on three fundamental design elements: color, font, and layout. At the overall design level, our tasks include style classification and the interpretation of visual metaphors. To support these tasks, we have curated and reannotated datasets to align with our novel task framework and introduced a new dataset aimed at negative space detection to extend the benchmark’s breadth. Nine MLLMs were put to the test, with GPT-4 serving as the evaluator.

**ZH** 本工作首创了一个综合基准来评估多模态大语言模型（MLLM）的设计能力，这在该领域尚属首次。我们的基准包含横跨两个设计复杂度层面（元素层面与整体设计层面）的八项任务。在元素层面，我们构建了评价视觉成分识别与语义内容理解的任务；在每一类任务中，我们聚焦三个基本设计元素：色彩、字体与版式。在整体设计层面，我们的任务包括风格分类与视觉隐喻解读。为支撑这些任务，我们整理并重新标注了若干数据集，使其与我们的新任务框架相对齐，并引入了一个面向负空间检测的新数据集，以拓展基准的广度。共测试了九个 MLLM，由 GPT-4 担任评价器。

**EN** In addition, we experimented with prompt refining across two dimensions. We first introduced a experiment for prompt rewriting using LLMs corresponding to each MLLMs, revealing the robustness of better performance models under different prompts and the efficiency when refining prompt using its LLMs. We also experimented with adding additional design knowledge to prompts in both textual and visual formats, revealing that adding image information can achieve the better performance than text. This benchmark sets a new standard for evaluating MLLMs and opens the door for future research to expand upon the intersection of design understanding.

**ZH** 此外，我们从两个维度探索了提示词优化。首先，我们引入了一项用各 MLLM 对应 LLM 进行提示词改写的实验，揭示了性能更好的模型在不同提示词下的稳健性，以及使用其自身 LLM 改写提示词的有效性。我们还尝试以文本与视觉两种格式向提示词中加入额外的设计知识，发现加入图像信息能取得优于文本的性能。该基准为评价 MLLM 树立了新标准，也为未来在设计理解这一交叉方向上的拓展研究打开了大门。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] Agrawal et al. [2019] Harsh Agrawal, Karan Desai, Yufei Wang, Xinlei Chen, Rishabh Jain, Mark Johnson, Dhruv Batra, Devi Parikh, Stefan Lee, and Peter Anderson. nocaps: novel object captioning at scal -->

<!-- [原子块 · verbatim] Awadalla et al. [2023] Anas Awadalla, Irena Gao, Josh Gardner, Jack Hessel, Yusuf Hanafy, Wanrong Zhu, Kalyani Marathe, Yonatan Bitton, Samir Gadre, Shiori Sagawa, Jenia Jitsev, Simon Kornblith, Pang  -->

<!-- [原子块 · verbatim] Bahng et al. [2018] Hyojin Bahng, Seungjoo Yoo, Wonwoong Cho, David Keetae Park, Ziming Wu, Xiaojuan Ma, and Jaegul Choo. Coloring with words: Guiding image colorization through text-based palette gen -->

<!-- [原子块 · verbatim] Bai et al. [2023] Jinze Bai, Shuai Bai, Shusheng Yang, Shijie Wang, Sinan Tan, Peng Wang, Junyang Lin, Chang Zhou, and Jingren Zhou. Qwen-vl: A versatile vision-language model for understanding, local -->

<!-- [原子块 · verbatim] Bar et al. [2022] Amir Bar, Yossi Gandelsman, Trevor Darrell, Amir Globerson, and Alexei Efros. Visual prompting via image inpainting. Advances in Neural Information Processing Systems , 35:25005–2501 -->

<!-- [原子块 · verbatim] Chen et al. [2015] Xinlei Chen, Hao Fang, Tsung-Yi Lin, Ramakrishna Vedantam, Saurabh Gupta, Piotr Dollár, and C Lawrence Zitnick. Microsoft coco captions: Data collection and evaluation server. arXiv -->

<!-- [原子块 · verbatim] Chen et al. [2023] Jun Chen, Deyao Zhu, Xiaoqian Shen, Xiang Li, Zechun Liu, Pengchuan Zhang, Raghuraman Krishnamoorthi, Vikas Chandra, Yunyang Xiong, and Mohamed Elhoseiny. Minigpt-v2: Large language -->

<!-- [原子块 · verbatim] Chung et al. [2022] Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Yunxuan Li, Xuezhi Wang, Mostafa Dehghani, Siddhartha Brahma, et al. Scaling instruction-finetuned lang -->

<!-- [原子块 · verbatim] Dai et al. [2023] W Dai, J Li, D Li, AMH Tiong, J Zhao, W Wang, B Li, P Fung, and S Hoi. Instructblip: Towards general-purpose vision-language models with instruction tuning. arXiv preprint arXiv:2305 -->

<!-- [原子块 · verbatim] Dong et al. [2023] Runpei Dong, Chunrui Han, Yuang Peng, Zekun Qi, Zheng Ge, Jinrong Yang, Liang Zhao, Jianjian Sun, Hongyu Zhou, Haoran Wei, et al. Dreamllm: Synergistic multimodal comprehension and  -->

<!-- [原子块 · verbatim] Fosco et al. [2020] Camilo Fosco, Vincent Casser, Amish Kumar Bedi, Peter O’Donovan, Aaron Hertzmann, and Zoya Bylinskii. Predicting visual importance across graphic design types. In Proceedings of th -->

<!-- [原子块 · verbatim] Fu et al. [2023] Chaoyou Fu, Peixian Chen, Yunhang Shen, Yulei Qin, Mengdan Zhang, Xu Lin, Jinrui Yang, Xiawu Zheng, Ke Li, Xing Sun, Yunsheng Wu, and Rongrong Ji. Mme: A comprehensive evaluation benc -->

<!-- [原子块 · verbatim] Goyal et al. [2017] Yash Goyal, Tejas Khot, Douglas Summers-Stay, Dhruv Batra, and Devi Parikh. Making the v in vqa matter: Elevating the role of image understanding in visual question answering. In P -->

<!-- [原子块 · verbatim] Gurari et al. [2018] Danna Gurari, Qing Li, Abigale J. Stangl, Anhong Guo, Chi Lin, Kristen Grauman, Jiebo Luo, and Jeffrey P. Bigham. Vizwiz grand challenge: Answering visual questions from blind peo -->

<!-- [原子块 · verbatim] Huang et al. [2023] Danqing Huang, Jiaqi Guo, Shizhao Sun, Hanling Tian, Jieru Lin, Zheng Hu, Chin-Yew Lin, Jian-Guang Lou, and Dongmei Zhang. A survey for graphic design intelligence. arXiv preprint  -->

<!-- [原子块 · verbatim] Hudson and Manning [2019] Drew A. Hudson and Christopher D. Manning. Gqa: A new dataset for real-world visual reasoning and compositional question answering. In Proceedings of the IEEE/CVF Conference  -->

<!-- [原子块 · verbatim] Inoue et al. [2023] Naoto Inoue, Kotaro Kikuchi, Edgar Simo-Serra, Mayu Otani, and Kota Yamaguchi. Layoutdm: Discrete diffusion model for controllable layout generation. In Proceedings of the IEEE/CVF -->

<!-- [原子块 · verbatim] Li et al. [2023a] Bo Li, Yuanhan Zhang, Liangyu Chen, Jinghao Wang, Jingkang Yang, and Ziwei Liu. Otter: A multi-modal model with in-context instruction tuning. arXiv preprint arXiv:2305.03726 , 2023. -->

<!-- [原子块 · verbatim] Li et al. [2023b] Bohao Li, Rui Wang, Guangzhi Wang, Yuying Ge, Yixiao Ge, and Ying Shan. Seed-bench: Benchmarking multimodal llms with generative comprehension. arXiv preprint arXiv:2307.16125 , 2023 -->

<!-- [原子块 · verbatim] Li et al. [2023c] Junnan Li, Dongxu Li, Silvio Savarese, and Steven Hoi. Blip-2: Bootstrapping language-image pre-training with frozen image encoders and large language models. arXiv preprint arXiv:23 -->

<!-- [原子块 · verbatim] Lin et al. [2023] Kevin Lin, Zhengyuan Yang, Linjie Li, Jianfeng Wang, and Lijuan Wang. Designbench: Exploring and benchmarking dall-e 3 for imagining visual design. arXiv preprint arXiv:2310.15144 ,  -->

<!-- [原子块 · verbatim] Liu et al. [2023a] Haotian Liu, Chunyuan Li, Yuheng Li, and Yong Jae Lee. Improved baselines with visual instruction tuning, 2023. -->

<!-- [原子块 · verbatim] Liu et al. [2023b] Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. Visual instruction tuning. arXiv preprint arXiv:2304.08485 , 2023. -->

<!-- [原子块 · verbatim] Liu et al. [2023c] Yuan Liu, Haodong Duan, Yuanhan Zhang, Bo Li, Songyang Zhang, Wangbo Zhao, Yike Yuan, Jiaqi Wang, Conghui He, Ziwei Liu, Kai Chen, and Dahua Lin. Mmbench: Is your multi-modal model  -->

<!-- [原子块 · verbatim] OpenAI [2023a] OpenAI. Dall·e 3 system card, 2023. -->

<!-- [原子块 · verbatim] OpenAI [2023b] OpenAI. Gpt-4 technical report. arXiv preprint arXiv:2303.08774 , 2023. -->

<!-- [原子块 · verbatim] Qiu et al. [2022] Qianru Qiu, Xueting Wang, Mayu Otani, and Yuki Iwazaki. Color recommendation for vector graphic documents based on multi-palette representation. arXiv preprint , 2022. -->

<!-- [原子块 · verbatim] Steen et al. [2010] Gerard Steen, Aletta G Dorst, J Berenike Herrmann, Anna Kaal, Tina Krennmayr, Trijntje Pasma, et al. A method for linguistic metaphor identification. Amsterdam: Benjamins , 2010. -->

<!-- [原子块 · verbatim] Sun et al. [2023] Quan Sun, Qiying Yu, Yufeng Cui, Fan Zhang, Xiaosong Zhang, Yueze Wang, Hongcheng Gao, Jingjing Liu, Tiejun Huang, and Xinlong Wang. Generative pretraining in multimodality. arXiv pr -->

<!-- [原子块 · verbatim] Team et al. [2023] Gemini Team, Rohan Anil, Sebastian Borgeaud, Yonghui Wu, Jean-Baptiste Alayrac, Jiahui Yu, Radu Soricut, Johan Schalkwyk, Andrew M Dai, Anja Hauth, et al. Gemini: a family of highly -->

<!-- [原子块 · verbatim] Touvron et al. [2023a] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, Aurelien Rodrigue -->

<!-- [原子块 · verbatim] Touvron et al. [2023b] Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al. Llama 2: Open  -->

<!-- [原子块 · verbatim] Virkus [2022] D. Virkus. Dafonts free dataset, 2022. -->

<!-- [原子块 · verbatim] Yamaguchi [2021] Kota Yamaguchi. Canvasvae: Learning to generate vector graphic documents. ICCV , 2021. -->

<!-- [原子块 · verbatim] Yang et al. [2021] Cheng-Fu Yang, Wan-Cyuan Fan, Fu-En Yang, and Yu-Chiang Frank Wang. LayoutTransformer: Scene Layout Generation with Conceptual and Spatial Diversity. In 2021 IEEE/CVF Conference on  -->

<!-- [原子块 · verbatim] Ye et al. [2023] Qinghao Ye, Haiyang Xu, Jiabo Ye, Ming Yan, Anwen Hu, Haowei Liu, Qi Qian, Ji Zhang, Fei Huang, and Jingren Zhou. mplug-owl2: Revolutionizing multi-modal large language model with mod -->

<!-- [原子块 · verbatim] Yu et al. [2023a] Lili Yu, Bowen Shi, Ramakanth Pasunuru, Benjamin Muller, Olga Golovneva, Tianlu Wang, Arun Babu, Binh Tang, Brian Karrer, Shelly Sheynin, et al. Scaling autoregressive multi-modal mo -->

<!-- [原子块 · verbatim] Yu et al. [2023b] Weihao Yu, Zhengyuan Yang, Linjie Li, Jianfeng Wang, Kevin Lin, Zicheng Liu, Xinchao Wang, and Lijuan Wang. Mm-vet: Evaluating large multimodal models for integrated capabilities. ar -->

<!-- [原子块 · verbatim] Yue et al. [2023] Xiang Yue, Yuansheng Ni, Kai Zhang, Tianyu Zheng, Ruoqi Liu, Ge Zhang, Samuel Stevens, Dongfu Jiang, Weiming Ren, Yuxuan Sun, Cong Wei, Botao Yu, Ruibin Yuan, Renliang Sun, Ming Yin, -->

<!-- [原子块 · verbatim] Zhang et al. [2023] Renrui Zhang, Jiaming Han, Chris Liu, Peng Gao, Aojun Zhou, Xiangfei Hu, Shilin Yan, Pan Lu, Hongsheng Li, and Yu Qiao. Llama-adapter: Efficient fine-tuning of language models with -->

<!-- [原子块 · verbatim] Zhao et al. [2018a] Nanxuan Zhao, Ying Cao, and Rynson W. H. Lau. Modeling fonts in context: Font prediction on web designs. Computer Graphics Forum , 2018. -->

<!-- [原子块 · verbatim] Zhao et al. [2018b] Nanxuan Zhao, Ying Cao, and Rynson W.H. Lau. Modeling fonts in context: Font prediction on web designs. Computer Graphics Forum (Proc. Pacific Graphics 2018) , 37, 2018. -->

<!-- [原子块 · verbatim] Zhao et al. [2018c] Nanxuan Zhao, Ying Cao, and Rynson W.H. Lau. What characterizes personalities of graphic designs? ACM Transactions on Graphics (Proc. of SIGGRAPH 2018) , 37, 2018. -->

<!-- [原子块 · verbatim] Zheng et al. [2023] Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric. P Xing, Hao Zhang, Joseph E. Gonzalez, and Ion Stoica.  -->

<!-- [原子块 · verbatim] Zhu et al. [2020] Xizhou Zhu, Weijie Su, Lewei Lu, Bin Li, Xiaogang Wang, and Jifeng Dai. Deformable detr: Deformable transformers for end-to-end object detection. arXiv preprint arXiv:2010.04159 , 20 -->

<!-- [原子块 · verbatim] Zhu et al. [2023] Deyao Zhu, Jun Chen, Xiaoqian Shen, Xiang Li, and Mohamed Elhoseiny. Minigpt-4: Enhancing vision-language understanding with advanced large language models. arXiv preprint arXiv:2304 -->
