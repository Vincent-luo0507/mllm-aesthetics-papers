# PPTAgent：超越文本到幻灯片的演示文稿生成与评测

> 原标题：PPTAgent: Generating and Evaluating Presentations Beyond Text-to-Slides
> 作者：Hao Zheng, Xinyan Guan, Hao Kong, Jia Zheng, Weixiang Zhou, Hongyu Lin, Yaojie Lu, Ben He, Xianpei Han, Le Sun · arXiv:2501.03936 · 2025-01-07

<!-- [原子块 · verbatim] PPTAgent : Generating and Evaluating Presentations Beyond Text-to-Slides -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] Automatically generating presentations from documents is a challenging task that requires accommodating content quality, visual appeal, and structural coherence. Existing methods primarily focus on im -->

**EN** 1 Introduction

**ZH** 1 引言

**EN** Presentations are a widely used medium for information delivery, valued for their visual effectiveness in engaging and communicating with audiences. However, creating high-quality presentations requires a captivating storyline, well-designed layouts, and rich, compelling content (Fu et al., 2022). Consequently, creating well-rounded presentations requires advanced presentation skills and significant effort. Given the inherent complexity of the presentation creation, there is growing interest in automating the presentation generation process (Mondal et al., 2024; Maheshwari et al., 2024; Ge et al., 2025) by leveraging the generalization capabilities of Large Language Models (LLMs) and Multimodal Large Language Models (MLLMs).

**ZH** 演示文稿是一种被广泛使用的信息传递媒介，因其吸引并沟通受众的视觉效果而受到重视。然而，制作高质量演示文稿需要引人入胜的故事线、精心设计的版式以及丰富而有说服力的内容（Fu et al., 2022）。因此，做出面面俱到的演示文稿既需要高超的演示技巧，也需要投入大量精力。鉴于演示文稿创作本身的复杂性，借助大语言模型（LLM）与多模态大语言模型（MLLM）的泛化能力来自动化演示文稿生成过程，正引起越来越多的关注（Mondal et al., 2024; Maheshwari et al., 2024; Ge et al., 2025）。

<!-- [原子块 · img]  -->

**EN** Figure 1: Comparison between our PPTAgent approach (left) and the conventional abstractive summarization method (right).

**ZH** 图 1：本文的 PPTAgent 方法（左）与常规抽象式摘要方法（右）的对比。

<!-- [原子块 · img]  -->

**EN** Figure 2: Overview of the PPTAgent workflow. StageI: Presentation Analysis involves analyzing the input presentation to cluster slides into groups and extract their content schemas. Stage II: Presentation Generation generates new presentations guided by the outline, incorporating self-correction mechanisms to ensure robustness.

**ZH** 图 2：PPTAgent 工作流程总览。阶段 I 演示文稿分析：分析输入演示文稿，把幻灯片聚类成组并抽取其内容模式。阶段 II 演示文稿生成：在大纲引导下生成新的演示文稿，并引入自我纠正机制以保证鲁棒性。

**EN** Existing approaches typically follow a text-to-slides paradigm, which converts LLM outputs into slides using predefined rules or templates. As shown in Figure 1, prior studies (Mondal et al., 2024; Sefid et al., 2021) tend to treat presentation generation as an abstractive summarization task, focusing primarily on textual content while neglecting the visual-centric nature (Fu et al., 2022) of presentation. This results in text-heavy and monotonous presentations that fail to engage audiences effectively (Barrick et al., 2018).

**ZH** 现有方法通常遵循文本到幻灯片（text-to-slides）范式，即用预定义规则或模板把 LLM 的输出转换为幻灯片。如图 1 所示，此前的研究（Mondal et al., 2024; Sefid et al., 2021）倾向于把演示文稿生成当作抽象式摘要任务，主要关注文本内容，却忽略了演示文稿以视觉为中心的本质（Fu et al., 2022）。这导致生成的演示文稿文字密集、单调乏味，难以有效吸引受众（Barrick et al., 2018）。

**EN** Rather than creating complex presentations from scratch in a single pass, human workflows typically involve selecting exemplary slides as references and then summarizing and transferring key content onto them (Duarte, 2010). Inspired by this process, we propose PPTAgent, which decomposes slide generation into two phases: selecting the reference slide and editing it step by step. However, achieving such an edit-based approach for presentation generation is challenging. First, due to the layout and modal complexity of presentations, it is difficult for LLMs to directly determine which slides should be referenced. The key challenge lies in enhancing LLMs’ understanding of reference presentations’ structure and content patterns. Second, most presentations are saved in PowerPoint’s XML format, as demonstrated in Figure 11, which is inherently verbose and redundant (Gryk, 2022), making it challenging for LLMs to robustly perform editing operations.

**ZH** 与一次性从零创作复杂演示文稿不同，人类的工作流程通常是先挑选优秀的幻灯片作为参考，再把关键内容概括并迁移上去（Duarte, 2010）。受此过程启发，我们提出 PPTAgent，它把幻灯片生成分解为两个阶段：选择参考幻灯片，再逐步编辑它。然而，为演示文稿生成实现这种基于编辑的范式并不容易。首先，由于演示文稿在版式与模态上的复杂性，LLM 难以直接判断应当参考哪些幻灯片，关键挑战在于增强 LLM 对参考演示文稿结构与内容模式的理解。其次，多数演示文稿以 PowerPoint 的 XML 格式保存（如图 11 所示），该格式本身冗长而冗余（Gryk, 2022），使 LLM 难以稳健地执行编辑操作。

**EN** To address these challenges, PPTAgent operates in two stages. Stage I performs a comprehensive analysis of reference presentations to extract functional types and content schemas of slides, facilitating subsequent reference selection and slide generation. Stage II introduces a suite of edit APIs with HTML-rendered representation that simplifies slide modifications through code interaction (Wang et al., 2024b). Furthermore, we implement a self-correction mechanism (Kamoi et al., 2024) that allows LLMs to iteratively refine generated editing actions based on intermediate results and execution feedback, ensuring robust generation. As shown in Figure 2, we first analyze and cluster reference slides into categories (e.g., opening slides, bullet-point slides). For each new slide, PPTAgent selects an appropriate reference slide (e.g., opening slide for the first slide) and generates a series of editing actions (e.g., replace_span) to modify it.

**ZH** 为应对这些挑战，PPTAgent 分两个阶段运行。阶段 I 对参考演示文稿做全面分析，抽取幻灯片的功能类型与内容模式，为后续的参考选择与幻灯片生成提供便利。阶段 II 引入一组带有 HTML 渲染表示的编辑 API，通过代码交互简化幻灯片修改（Wang et al., 2024b）。此外，我们实现了一种自我纠正机制（Kamoi et al., 2024），让 LLM 依据中间结果与执行反馈迭代改进所生成的编辑动作，确保生成过程稳健。如图 2 所示，我们首先把参考幻灯片分析并聚类为若干类别（例如开场幻灯片、要点幻灯片）。对每张新幻灯片，PPTAgent 选取合适的参考幻灯片（例如用开场幻灯片作为第一页），并生成一系列编辑动作（例如 replace_span）来修改它。

**EN** Due to the lack of a comprehensive evaluation framework, we propose PPTEval, which adopts the MLLM-as-a-judge paradigm Chen et al. (2024a) to evaluate presentations across three dimensions: Content, Design, and CoherenceDuarte (2010). Human evaluations validate the reliability and effectiveness of PPTEval. Results demonstrate that PPTAgent generates high-quality presentations, achieving an average score of 3.67 for the three dimensions in PPTEval.

**ZH** 由于缺少全面的评测框架，我们提出 PPTEval。它采用以多模态大语言模型充当评判器（MLLM-as-a-judge）的范式（Chen et al., 2024a），从内容、设计与连贯性三个维度评价演示文稿（Duarte, 2010）。人工评测验证了 PPTEval 的可靠性与有效性。结果表明，PPTAgent 能生成高质量演示文稿，在 PPTEval 三个维度上的平均得分为 3.67。

**EN** Our main contributions can be summarized as follows:

**ZH** 我们的主要贡献可概括如下：

**EN** ⟦SLOT_0⟧ We propose PPTAgent, a framework that redefines automatic presentation generation as an edit-based process guided by reference presentations.

**ZH** ⟦SLOT_0⟧ 我们提出 PPTAgent，一个把自动演示文稿生成重新定义为「由参考演示文稿引导的基于编辑的过程」的框架。

**EN** ⟦SLOT_1⟧ We introduce PPTEval, a comprehensive evaluation framework that assesses presentations across three dimensions: Content, Design, and Coherence.

**ZH** ⟦SLOT_1⟧ 我们提出 PPTEval，一个从内容、设计与连贯性三个维度评价演示文稿的综合评测框架。

**EN** ⟦SLOT_2⟧ We release the PPTAgent and PPTEval codebases, along with a new presentation dataset Zenodo10K, to support future research.

**ZH** ⟦SLOT_2⟧ 我们发布 PPTAgent 与 PPTEval 的代码库，以及一个新的演示文稿数据集 Zenodo10K，以支持后续研究。

**EN** 2 PPTAgent

**ZH** 2 PPTAgent

**EN** In this section, we formulate the presentation generation task and introduce our proposed PPTAgent framework, which consists of two distinct stages. In stage I, we analyze reference presentations through slide clustering and schema extraction, providing a comprehensive understanding of input presentations that facilitates subsequent reference selection and slide generation. In stage II, we leverage analyzed reference presentations to select reference slides and generate the target presentation for the input document through an iterative editing process. An overview of our workflow is illustrated in Figure 2.

**ZH** 本节给出演示文稿生成任务的形式化定义，并介绍我们提出的 PPTAgent 框架，它由两个不同阶段组成。在阶段 I，我们通过幻灯片聚类与模式抽取来分析参考演示文稿，形成对输入演示文稿的全面理解，为后续的参考选择与幻灯片生成提供便利。在阶段 II，我们利用分析好的参考演示文稿选择参考幻灯片，并通过迭代编辑过程为输入文档生成目标演示文稿。工作流程总览见图 2。

**EN** 2.1 Problem Formulation

**ZH** 2.1 问题定义

**EN** PPTAgent is designed to generate an engaging presentation through an edit-based process. We provide formal definitions for the conventional method and PPTAgent to highlight their key differences.

**ZH** PPTAgent 旨在通过基于编辑的过程生成引人入胜的演示文稿。我们给出常规方法与 PPTAgent 的形式化定义，以凸显二者的关键差异。

**EN** The conventional method (Bandyopadhyay et al., 2024; Mondal et al., 2024) for creating each slide ⟦SLOT_3⟧ is formalized in Equation 1. Given the input content ⟦SLOT_4⟧, it generates ⟦SLOT_5⟧ slide elements, each defined by its type, content, and styling attributes, such as ⟦SLOT_6⟧.

**ZH** 常规方法（Bandyopadhyay et al., 2024; Mondal et al., 2024）为创建每张幻灯片 ⟦SLOT_3⟧ 的过程在式 (1) 中形式化。给定输入内容 ⟦SLOT_4⟧，它生成 ⟦SLOT_5⟧ 个幻灯片元素，每个元素由其类型、内容与样式属性（例如 ⟦SLOT_6⟧）定义。

<!-- [原子块 · table] 𝑺 = { e 1 , e 2 , … , e n } = f ⁡ ( C ) \bm{S}=\{e_{1},e_{2},\dots,e_{n}\}=f(C) (1) -->

**EN** While this conventional method is straightforward, it requires manual specification of styling attributes, which is challenging for automated generation (Guo et al., 2023). Instead of creating slides from scratch, PPTAgent generates a sequence of executable actions to edit reference slides, thereby preserving their well-designed layouts and styles. As shown in Equation 2, given the input content ⟦SLOT_7⟧ and the ⟦SLOT_8⟧-th reference slide ⟦SLOT_9⟧, which is selected from the reference presentation, PPTAgent generates a sequence of ⟦SLOT_10⟧ executable actions, where each action ⟦SLOT_11⟧ corresponds to a line of executable code.

**ZH** 常规方法虽然直截了当，却需要人工指定样式属性，这对自动生成而言颇具挑战（Guo et al., 2023）。PPTAgent 不从零创建幻灯片，而是生成一串可执行的动作来编辑参考幻灯片，从而保留其精心设计的版式与风格。如式 (2) 所示，给定输入内容 ⟦SLOT_7⟧ 与从参考演示文稿中选出的第 ⟦SLOT_8⟧ 张参考幻灯片 ⟦SLOT_9⟧，PPTAgent 生成一串 ⟦SLOT_10⟧ 个可执行动作，其中每个动作 ⟦SLOT_11⟧ 对应一行可执行代码。

<!-- [原子块 · table] 𝑨 = { a 1 , a 2 , … , a m } = g ⁡ ( C , R j ) \bm{A}=\{a_{1},a_{2},\dots,a_{m}\}=g(C,R_{j}) (2) -->

**EN** 2.2 Stage I : Presentation Analysis

**ZH** 2.2 阶段 I：演示文稿分析

**EN** In this stage, we analyze the reference presentation to guide the reference selection and slide generation. Firstly, we categorize slides based on their structural and layout characteristics through slide clustering. Then, we extract content schemas to identify the content organization of the slide in each cluster, providing a comprehensive description of slide elements.

**ZH** 在这一阶段，我们分析参考演示文稿，为参考选择与幻灯片生成提供指导。首先，我们通过幻灯片聚类，依据幻灯片的结构与版式特征对其分类；随后抽取内容模式，以识别每个簇中幻灯片的内容组织方式，从而给出幻灯片元素的全面描述。

**EN** Slide Clustering

**ZH** 幻灯片聚类

**EN** Slides can be categorized into two main types based on their functionalities: structural slides that support the presentation’s organization (e.g., opening slides) and content slides that convey specific information (e.g., bullet-point slides). To distinguish between these two types, we employ LLMs to segment the presentation accordingly. For structural slides, we leverage LLMs’ long-context capability to analyze all slides in the input presentation, identifying structural slides, labeling their structural roles based on their textual features, and grouping them accordingly. For content slides, we first convert them into images and then apply a hierarchical clustering approach to group similar slide images. Subsequently, we utilize MLLMs to analyze the converted slide images, identifying layout patterns within each cluster. Further details are provided in Appendix D.

**ZH** 按功能划分，幻灯片可分为两大类：支撑演示文稿组织的结构性幻灯片（例如开场幻灯片），以及传达具体内容的内容型幻灯片（例如要点幻灯片）。为区分这两类，我们用 LLM 对演示文稿做相应切分。对结构性幻灯片，我们利用 LLM 的长上下文能力分析输入演示文稿中的全部幻灯片，识别结构性幻灯片，依据其文本特征标注结构角色，并据此分组。对内容型幻灯片，我们先把它们转换为图像，再用层次聚类方法把相似的幻灯片图像归组；随后用 MLLM 分析转换后的幻灯片图像，识别每个簇内的版式模式。更多细节见附录 D。

**EN** Schema Extraction

**ZH** 模式抽取

**EN** After clustering, we further analyzed their content schemas to facilitate the slide generation. Specifically, we define an extraction framework where each element is represented by its category, description, and content. This framework enables a clear and structured representation of each slide. Detailed instructions are provided in Appendix F, with an example of the schema shown below.

**ZH** 聚类之后，我们进一步分析其内容模式，为幻灯片生成提供便利。具体地，我们定义一个抽取框架，其中每个元素由类别、描述与内容表示。该框架使每张幻灯片都能得到清晰、结构化的表示。详细指令见附录 F，下面给出一个模式示例。

<!-- [原子块 · table] Category Description Data Title Main title Sample Library Date Date of the event 15 February 2018 Image Primary image to illustrate the slide Picture: Children in a library with … -->

**EN** 2.3 Stage II : Presentation Generation

**ZH** 2.3 阶段 II：演示文稿生成

**EN** PPTAgent first generates an outline specifying reference slides and relevant content for each new slide. Then, it iteratively edits elements from reference slides through edit APIs to create the target presentation.

**ZH** PPTAgent 首先生成一份大纲，指明每张新幻灯片所用的参考幻灯片与相关内容；随后通过编辑 API 迭代地编辑参考幻灯片中的元素，生成目标演示文稿。

**EN** Outline Generation

**ZH** 大纲生成

**EN** As shown in Figure 2, we utilize LLM to generate a structured outline consisting of multiple entries. Each entry represents a new slide, containing the reference slide and relevant document content of the new slide. The reference slide is selected based on the slide-level functional description in Stage I, while the relevant document content is identified based on the input document.

**ZH** 如图 2 所示，我们利用 LLM 生成由多个条目构成的结构化大纲。每个条目代表一张新幻灯片，包含参考幻灯片与新幻灯片的相关文档内容。参考幻灯片依据阶段 I 得到的幻灯片级功能描述来选择，而相关文档内容则依据输入文档来确定。

**EN** Slide Generation

**ZH** 幻灯片生成

**EN** Guided by the structured outline, slides are generated iteratively based on the corresponding entries. For each slide, LLMs incorporate textual content and extracted image captions from the input document. The new slide adopts the layout of the reference slide while ensuring consistency in content and structural clarity.

**ZH** 在结构化大纲的引导下，幻灯片依据相应条目迭代生成。对每张幻灯片，LLM 会结合输入文档中的文本内容与抽取出的图像说明。新幻灯片沿用参考幻灯片的版式，同时保证内容的一致性与结构的清晰性。

**EN** Specifically, to generate a new slide based on the corresponding entry in the outline, we design edit-based APIs to enable LLMs to edit the reference slide. As shown below, these APIs support editing, removing, and duplicating slide elements. Moreover, given the complexity of the XML format in presentations, which is demonstrated in Appendix E, we render the reference slide into an HTML representation (Feng et al., 2024), offering a more precise and intuitive format for easier understanding. This HTML-based format, combined with our edit-based APIs, enables LLMs to perform precise content modifications on reference slides.

**ZH** 具体地，为根据大纲中的相应条目生成新幻灯片，我们设计了基于编辑的 API，使 LLM 能够编辑参考幻灯片。如下所示，这些 API 支持对幻灯片元素进行编辑、删除与复制。此外，鉴于演示文稿 XML 格式的复杂性（见附录 E），我们把参考幻灯片渲染为 HTML 表示（Feng et al., 2024），它更精确、更直观，便于理解。这种基于 HTML 的格式与我们的编辑 API 相结合，使 LLM 能够对参考幻灯片做出精确的内容修改。

<!-- [原子块 · table] Function Name Description del_span Delete a span. del_image Delete an image element. clone_paragraph Create a duplicate of an existing paragraph. replace_span Replace the content of a span. replace_im -->

**EN** Furthermore, to enhance robustness during the editing process, we implement a self-correction mechanism (Kamoi et al., 2024). Specifically, the generated editing actions are executed within a REPL11 1 https://en.wikipedia.org/wiki/REPL environment. When actions fail to apply to reference slides, the REPL provides execution feedback22 2 https://docs.python.org/3/tutorial/errors.html to assist LLMs in refining their actions. The LLM then analyzes this feedback to adjust its editing actions (Guan et al., 2024; Wang et al., 2024b), enabling iterative refinement until a valid slide is generated or the maximum retry limit is reached.

**ZH** 此外，为提升编辑过程的鲁棒性，我们实现了一种自我纠正机制（Kamoi et al., 2024）。具体地，生成的编辑动作在 REPL11 1 https://en.wikipedia.org/wiki/REPL 环境中执行。当动作无法作用于参考幻灯片时，REPL 会提供执行反馈22 2 https://docs.python.org/3/tutorial/errors.html，协助 LLM 改进其动作。LLM 随后分析该反馈以调整编辑动作（Guan et al., 2024; Wang et al., 2024b），迭代改进直到生成有效幻灯片或达到最大重试次数。

**EN** 3 PPTEval

**ZH** 3 PPTEval

**EN** We introduce PPTEval, a comprehensive framework that evaluates presentation quality from multiple dimensions, addressing the absence of reference-free evaluation for presentations. The framework provides both numeric scores (1-to-5 scale) and detailed rationales to justify each dimension’s assessment.

**ZH** 我们提出 PPTEval——一个从多个维度评价演示文稿质量的综合框架，弥补了演示文稿无参考评测的缺失。该框架既提供数值分数（1–5 分制），也给出详细的评分理由来支撑每个维度的判断。

**EN** Grounded in established presentation design principles (Duarte, 2008; Duarte, 2010), our evaluation framework focuses on three key dimensions, as summarized in Table 1. Specially, given a generated presentation, we assess the content and design at the slide level, while evaluating coherence across the entire presentation.

**ZH** 立足于成熟的演示文稿设计原则（Duarte, 2008; Duarte, 2010），我们的评测框架聚焦三个关键维度，如表 1 所示。具体地，给定一份生成的演示文稿，我们在幻灯片层面评价内容与设计，而在整个演示文稿层面评价连贯性。

**EN** The complete evaluation process is illustrated in Figure 3, with detailed scoring criteria and representative examples provided in Appendix B.

**ZH** 完整的评测流程如图 3 所示，详细的评分标准与代表性示例见附录 B。

<!-- [原子块 · img]  -->

**EN** Figure 3: PPTEval assesses presentations from three dimensions: content, design, and coherence.

**ZH** 图 3：PPTEval 从内容、设计与连贯性三个维度评价演示文稿。

<!-- [原子块 · table] Dimension Criteria Content Text should be concise and grammatically sound, supported by relevant images. Design Harmonious colors and proper layout ensure readability, while visual elements like geome -->

**EN** Table 1: The scoring criteria of dimensions in PPTEval, all evaluated in 1-5 scale.

**ZH** 表 1：PPTEval 各维度的评分标准，全部采用 1–5 分制。

**EN** 4 Experiment

**ZH** 4 实验

**EN** 4.1 Dataset

**ZH** 4.1 数据集

**EN** Existing presentation datasets, such as Mondal et al. (2024); Sefid et al. (2021); Sun et al. (2021); Fu et al. (2022), have two main issues. First, they are mostly stored in PDF or JSON formats, which leads to a loss of semantic information, such as structural relationships and styling attributes of elements. Additionally, these datasets primarily consist of academic presentations in artificial intelligence, limiting their diversity. To address these limitations, we introduce Zenodo10K, a new dataset sourced from Zenodo (European Organization For Nuclear Research and OpenAIRE, 2013), which hosts diverse artifacts across domains, all under clear licenses. We have curated 10,448 presentations from this source and made them publicly available to support further research.

**ZH** 现有演示文稿数据集（如 Mondal et al. (2024); Sefid et al. (2021); Sun et al. (2021); Fu et al. (2022)）存在两个主要问题。首先，它们多以 PDF 或 JSON 格式存储，导致语义信息（例如元素间的结构关系与样式属性）丢失；其次，这些数据集主要由人工智能领域的学术演示文稿构成，多样性有限。为弥补这些不足，我们引入 Zenodo10K——一个取自 Zenodo（European Organization For Nuclear Research and OpenAIRE, 2013）的新数据集，该平台托管各领域的多样成果，且均具有明确的许可协议。我们从该来源整理了 10448 份演示文稿并公开发布，以支持后续研究。

**EN** Following Mondal et al. (2024), we sample 50 presentations in five domains to serve as reference presentations. In addition, we collected 50 documents from the same domains to be used as input documents. The sampling criteria and preprocessing details are provided in Appendix A, while the dataset statistics are summarized in Table 2.

**ZH** 沿用 Mondal et al.（2024）的做法，我们在五个领域各采样 50 份演示文稿作为参考演示文稿；此外，我们从相同领域收集了 50 份文档作为输入文档。采样标准与预处理细节见附录 A，数据集统计汇总于表 2。

<!-- [原子块 · table] Domain Document Presentation #Chars #Figs #Chars #Figs #Pages Culture 12,708 2.9 6,585 12.8 14.3 Education 12,305 5.5 3,993 12.9 13.9 Science 16,661 4.8 5,334 24.0 18.4 Society 13,019 7.3 3,723 9.8 12 -->

**EN** Table 2: Statistics of the dataset used in our experiments, detailing the number of characters (‘#Chars’) and figures (‘#Figs’), as well as the number of pages (‘#Pages’).

**ZH** 表 2：实验所用数据集的统计信息，详列字符数（‘#Chars’）与图片数（‘#Figs’），以及页数（‘#Pages’）。

<!-- [原子块 · table] Configuration Existing Metrics PPTEval Language Model Vision Model SR(%) ↑ \uparrow PPL ↓ \downarrow ROUGE-L ↑ \uparrow FID ↓ \downarrow Content ↑ \uparrow Design ↑ \uparrow Coherence ↑ \uparrow Avg.  -->

**EN** Table 3: Performance comparison of presentation generation methods, including DocPres, KCTV, and our proposed PPTAgent. The best/second-best scores are bolded/underlined. Results are reported using existing metrics, including Success Rate (SR), Perplexity (PPL), Rouge-L, Fréchet Inception Distance (FID), and PPTEval.

**ZH** 表 3：各演示文稿生成方法的性能对比，包括 DocPres、KCTV 与我们提出的 PPTAgent。最优／次优分数分别加粗／加下划线。结果采用既有指标报告，包括成功率（SR）、困惑度（PPL）、Rouge-L、Fréchet Inception Distance（FID），以及 PPTEval。

**EN** 4.2 Implementation Details

**ZH** 4.2 实现细节

**EN** PPTAgent is implemented with three models: GPT-4o-2024-08-06 (GPT-4o), Qwen2.5-72B-Instruct (Qwen2.5, Yang et al., 2024), and Qwen2-VL-72B-Instruct (Qwen2-VL, Wang et al., 2024a). These models are categorized according to the specific modalities they handle, whether textual or visual, as indicated by their subscripts. Specifically, we define configurations as combinations of a language model (LM) and a vision model (VM), such as Qwen2.5⟦SLOT_12⟧+Qwen2-VL⟦SLOT_13⟧.

**ZH** PPTAgent 用三个模型实现：GPT-4o-2024-08-06（GPT-4o）、Qwen2.5-72B-Instruct（Qwen2.5，Yang et al., 2024）与 Qwen2-VL-72B-Instruct（Qwen2-VL，Wang et al., 2024a）。这些模型依据其处理的模态——文本或视觉——以下标加以区分。具体地，我们把配置定义为语言模型（LM）与视觉模型（VM）的组合，例如 Qwen2.5⟦SLOT_12⟧+Qwen2-VL⟦SLOT_13⟧。

**EN** Experiment data covers 5 domains, each with 10 input documents and 10 reference presentations, totaling 500 presentation generation tasks per configuration (5 domains × 10 input documents × 10 reference presentations). Each slide generation allows a maximum of two self-correction iterations. We use Chen et al. (2024b) and Wu et al. (2020) to compute the text and image embeddings respectively. All open-source LLMs are deployed using the VLLM framework (Kwon et al., 2023) on NVIDIA A100 GPUs. The total computational cost for experiments are approximately 500 GPU hours.

**ZH** 实验数据覆盖 5 个领域，每域 10 份输入文档与 10 份参考演示文稿，每种配置合计 500 个演示文稿生成任务（5 个领域 × 10 份输入文档 × 10 份参考演示文稿）。每张幻灯片的生成最多允许两轮自我纠正迭代。我们分别用 Chen et al.（2024b）与 Wu et al.（2020）计算文本与图像嵌入。所有开源 LLM 均通过 VLLM 框架（Kwon et al., 2023）部署在 NVIDIA A100 GPU 上，实验总计算开销约为 500 GPU 小时。

**EN** 4.3 Baselines

**ZH** 4.3 基线

**EN** We choose the following baseline methods: DocPres (Bandyopadhyay et al., 2024) propose a rule-based approach that generates narrative-rich slides through multi-stages, and incorporates images through a similarity-based mechanism. KCTV (Cachola et al., 2024) propose a template-based method that creates slides in an intermediate format before converting them into final presentations using predefined templates. The baseline methods operate without vision models since they do not process visual information. Each configuration generates 50 presentations (5 domains × 10 input documents), as they do not require reference presentations. Consequently, the FID metric is excluded from their evaluation.

**ZH** 我们选取如下基线方法：DocPres（Bandyopadhyay et al., 2024）提出一种基于规则的方法，通过多个阶段生成叙事丰富的幻灯片，并以基于相似度的机制引入图像；KCTV（Cachola et al., 2024）提出一种基于模板的方法，先以中间格式创建幻灯片，再用预定义模板转换为最终演示文稿。这些基线方法不处理视觉信息，因而不使用视觉模型。每种配置生成 50 份演示文稿（5 个领域 × 10 份输入文档），因为它们不需要参考演示文稿；相应地，其评测中不含 FID 指标。

**EN** 4.4 Evaluation Metrics

**ZH** 4.4 评测指标

**EN** We evaluated the presentation generation using the following metrics:

**ZH** 我们用以下指标评测演示文稿生成：

**EN** ⟦SLOT_14⟧ Success Rate (SR) evaluates the robustness of presentation generation (Wu et al., 2024), calculated as the percentage of successfully completed tasks. For PPTAgent, success requires the generation of all slides without execution errors after self-correction. For KCTV, success is determined by the successful compilation of the generated LaTeX file. DocPres is excluded from this evaluation due to its deterministic rule-based conversion.

**ZH** ⟦SLOT_14⟧ 成功率（SR）衡量演示文稿生成的鲁棒性（Wu et al., 2024），按成功完成的任务占比计算。对 PPTAgent，成功要求在自我纠正后生成全部幻灯片且不出现执行错误；对 KCTV，成功取决于所生成 LaTeX 文件能否成功编译；DocPres 因其基于规则的确定性转换而被排除在该评测之外。

**EN** ⟦SLOT_15⟧ Perplexity (PPL) measures the likelihood of the model generating the given sequence. Using Llama-3-8B (Dubey et al., 2024), we calculate the average perplexity across all slides in a presentation. Lower perplexity scores indicate higher textual fluency (Bandyopadhyay et al., 2024).

**ZH** ⟦SLOT_15⟧ 困惑度（PPL）度量模型生成给定序列的似然。我们使用 Llama-3-8B（Dubey et al., 2024）计算演示文稿中所有幻灯片的平均困惑度。困惑度越低，说明文本流畅度越高（Bandyopadhyay et al., 2024）。

**EN** ⟦SLOT_16⟧ Rouge-L (Lin, 2004) evaluates textual similarity by measuring the longest common subsequence between generated and reference texts. We report the F1 score to balance precision and recall.

**ZH** ⟦SLOT_16⟧ Rouge-L（Lin, 2004）通过度量生成文本与参考文本的最长公共子序列来评估文本相似度。我们报告 F1 分数，以平衡精确率与召回率。

**EN** ⟦SLOT_17⟧ FID (Heusel et al., 2017) measures the similarity between the generated presentation and the reference presentation in the feature space. Due to the limited sample size, we calculate the FID using a 64-dimensional output vector.

**ZH** ⟦SLOT_17⟧ FID（Heusel et al., 2017）在特征空间中度量生成的演示文稿与参考演示文稿之间的相似度。受样本量所限，我们用 64 维输出向量计算 FID。

**EN** ⟦SLOT_18⟧ PPTEval employs GPT-4o as the judging model to evaluate presentation quality across three dimensions: content, design, and coherence. We compute content and design scores by averaging across slides, while coherence is assessed at the presentation level.

**ZH** ⟦SLOT_18⟧ PPTEval 采用 GPT-4o 作为评判模型，从内容、设计与连贯性三个维度评价演示文稿质量。内容与设计分数在幻灯片层面取平均得到，连贯性则在演示文稿层面评定。

**EN** 4.5 Overall Result

**ZH** 4.5 总体结果

**EN** Table 3 presents the performance comparison between PPTAgent and baselines, revealing that:

**ZH** 表 3 给出了 PPTAgent 与基线的性能对比，结果显示：

<!-- [原子块 · table] Setting SR(%) Content Design Coherence Avg. PPTAgent 95.0 3.28 3.27 4.48 3.67 w/o Outline 91.0 3.24 3.30 3.36 3.30 w/o Schema 78.8 3.08 3.23 4.04 3.45 w/o Structure 92.2 3.28 3.25 3.45 3.32 w/o CodeRe -->

**EN** Table 4: Ablation analysis of PPTAgent utilizing the Qwen2.5⟦SLOT_19⟧+Qwen2-VL⟦SLOT_20⟧ configuration, demonstrating the contribution of each components.

**ZH** 表 4：在 Qwen2.5⟦SLOT_19⟧+Qwen2-VL⟦SLOT_20⟧ 配置下对 PPTAgent 的消融分析，展示了各组件的贡献。

**EN** PPTAgent Significantly Improves Overall Presentation Quality.

**ZH** PPTAgent 显著改善演示文稿的总体质量。

**EN** PPTAgent demonstrates statistically significant performance improvements over baseline methods across all three dimensions of PPTEval. Compared to the rule-based baseline (DocPres), PPTAgent exhibits substantial improvements in both the design and content dimensions (3.34 vs. 2.37, +40.9%; 3.34 vs. 2.98, +12.1%), as presentations generated by the DocPres method show minimal design effort. In comparison with the template-based baseline (KCTV), PPTAgent also achieves notable improvements in both design and content (3.34 vs. 2.95, +13.2%; 3.28 vs. 2.55, +28.6%), underscoring the efficacy of the edit-based paradigm. Most notably, PPTAgent shows a significant enhancement in the coherence dimension (4.48 vs. 3.57, +25.5% for DocPres; 4.48 vs. 3.28, +36.6% for KCTV). This improvement can be attributed to PPTAgent ’s comprehensive analysis of the structural role of slides.

**ZH** 在 PPTEval 的全部三个维度上，PPTAgent 相较基线方法都取得了统计显著的性能提升。与基于规则的基线（DocPres）相比，PPTAgent 在设计维度与内容维度上均有大幅改善（3.34 对 2.37，+40.9%；3.34 对 2.98，+12.1%），因为 DocPres 生成的演示文稿几乎没有设计投入。与基于模板的基线（KCTV）相比，PPTAgent 在设计与内容上同样有明显提升（3.34 对 2.95，+13.2%；3.28 对 2.55，+28.6%），印证了基于编辑的范式的有效性。最突出的是，PPTAgent 在连贯性维度上提升显著（对 DocPres 为 4.48 对 3.57，+25.5%；对 KCTV 为 4.48 对 3.28，+36.6%）。这一改善可归因于 PPTAgent 对幻灯片结构角色的全面分析。

**EN** PPTAgent Exhibits Robust Generation Performance.

**ZH** PPTAgent 表现出稳健的生成性能。

**EN** Our approach empowers LLMs to produce well-rounded presentations with remarkable success rate, achieving ⟦SLOT_21⟧ success rate for both Qwen2.5⟦SLOT_22⟧+Qwen2-VL⟦SLOT_23⟧ and GPT-4o⟦SLOT_24⟧+GPT-4o⟦SLOT_25⟧, which is a significant improvement compared to KCTV (97.8% vs. 88.0%). Moreover, detailed performance of Qwen2.5⟦SLOT_26⟧+Qwen2-VL⟦SLOT_27⟧ across various domains is illustrated in Table 8, underscoring the versatility and robustness of our approach.

**ZH** 我们的方法使 LLM 能以极高的成功率产出面面俱到的演示文稿：Qwen2.5⟦SLOT_22⟧+Qwen2-VL⟦SLOT_23⟧ 与 GPT-4o⟦SLOT_24⟧+GPT-4o⟦SLOT_25⟧ 均达到 ⟦SLOT_21⟧ 的成功率，相比 KCTV 有显著提升（97.8% 对 88.0%）。此外，表 8 展示了 Qwen2.5⟦SLOT_26⟧+Qwen2-VL⟦SLOT_27⟧ 在各领域的详细表现，印证了本方法的通用性与鲁棒性。

**EN** PPTEval Demonstrates Superior Evaluation Capability.

**ZH** PPTEval 展现出更优的评测能力。

**EN** Traditional metrics like PPL and ROUGE-L demonstrate inconsistent evaluation trends compared to PPTEval. For instance, KCTV achieves a high ROUGE-L (16.76) but a low content score (2.55), while our method shows the opposite trend with ROUGE-L (14.25) and content score (3.28). Moreover, we observe that ROUGE score overemphasizes textual alignment with source documents, potentially compromising the expressiveness of presentations. Most importantly, PPTEval advances beyond existing metrics through its dual capability of reference-free design assessment and holistic evaluation of presentation coherence. Further agreement evaluation is shown in Section 5.5.

**ZH** 与 PPTEval 相比，PPL 与 ROUGE-L 等传统指标呈现出不一致的评测趋势。例如 KCTV 取得了较高的 ROUGE-L（16.76）却只有较低的内容分（2.55），而我们的方法趋势相反——ROUGE-L 为 14.25、内容分为 3.28。此外我们观察到，ROUGE 分数过分强调与源文档的文本对齐，可能损害演示文稿的表现力。最重要的是，PPTEval 凭借无参考的设计评估与对演示文稿连贯性的整体评价这双重能力，超越了既有指标。更多一致性评测见 5.5 节。

**EN** 5 Analysis

**ZH** 5 分析

**EN** 5.1 Ablation Study

**ZH** 5.1 消融研究

**EN** We conducted ablation studies across four settings: (1) randomly selecting a slide as the reference (w/o Outline), (2) omitting structural slides during outline generation (w/o Structure), (3) replacing the slide representation with the method proposed by Guo et al. (2023) (w/o CodeRender), and (4) removing guidance from the content schema (w/o Schema). All experiments were conducted using the Qwen2.5⟦SLOT_28⟧+Qwen2-VL⟦SLOT_29⟧ configuration.

**ZH** 我们在四种设置下开展消融研究：（1）随机选择一张幻灯片作为参考（w/o Outline）；（2）在大纲生成时略去结构性幻灯片（w/o Structure）；（3）把幻灯片表示替换为 Guo et al.（2023）提出的方法（w/o CodeRender）；（4）去掉内容模式的引导（w/o Schema）。所有实验均在 Qwen2.5⟦SLOT_28⟧+Qwen2-VL⟦SLOT_29⟧ 配置下进行。

<!-- [原子块 · object]  -->

**EN** Figure 4: Score distributions of presentations generated by PPTAgent, DocPres, and KCTV across the three evaluation dimensions: Content, Design, and Coherence, as assessed by PPTEval.

**ZH** 图 4：由 PPTEval 评定的 PPTAgent、DocPres 与 KCTV 生成演示文稿在内容、设计与连贯性三个评测维度上的分数分布。

<!-- [原子块 · img]  -->

**EN** Figure 5: Comparative analysis of presentation generation across different methods. PPTAgent generates under different reference presentations, indicated as PPTAgent (a) and PPTAgent (b).

**ZH** 图 5：不同方法生成演示文稿的对比分析。PPTAgent 在不同参考演示文稿下生成的结果分别记为 PPTAgent (a) 与 PPTAgent (b)。

**EN** As demonstrated in Table 4, our experiments reveal two key findings: 1) The HTML-based representation significantly reduces interaction complexity, evidenced by the substantial decrease in success rate from 95.0% to 74.6% when removing the Code Render component. 2) The presentation analysis is crucial for generation quality, as removing the outline and structural slides significantly degrades coherence (from 4.48 to 3.36/3.45) and eliminating the slide schema reduces the success rate from 95.0% to 78.8%.

**ZH** 如表 4 所示，我们的实验揭示了两个关键发现：1）基于 HTML 的表示显著降低了交互复杂度——去掉 Code Render 组件后，成功率从 95.0% 大幅下降至 74.6%。2）演示文稿分析对生成质量至关重要——去掉大纲与结构性幻灯片会显著损害连贯性（从 4.48 降至 3.36/3.45），而去掉幻灯片模式会把成功率从 95.0% 拉低到 78.8%。

**EN** 5.2 Case Study

**ZH** 5.2 案例研究

**EN** We present representative examples of presentations generated under different configurations in Figure 5. PPTAgent demonstrates superior presentation quality across multiple dimensions. First, it effectively incorporates visual elements with contextually appropriate image placements, while maintaining concise and well-structured slide content. Second, it exhibits diversity in generating visually engaging slides under diverse references. In contrast, baseline methods (DocPres and KCTV) produce predominantly text-based slides with limited visual variation, constrained by their rule-based or template-based paradigms.

**ZH** 图 5 给出了不同配置下生成的演示文稿的代表性示例。PPTAgent 在多个维度上展现出更优的演示文稿质量。首先，它能有效融入视觉元素、把图像放在语境恰当的位置，同时保持幻灯片内容的简洁与结构清晰。其次，在不同参考下生成富有视觉吸引力的幻灯片时，它表现出多样性。相比之下，基线方法（DocPres 与 KCTV）受制于基于规则或基于模板的范式，生成的幻灯片以文本为主，视觉变化有限。

<!-- [原子块 · object]  -->

**EN** Figure 6: The number of iterative self-corrections required to generate a single slide under different models.

**ZH** 图 6：不同模型生成单张幻灯片所需的迭代自我纠正次数。

**EN** 5.3 Score Distribution

**ZH** 5.3 分数分布

**EN** We further investigated the score distribution of generated presentations to compare the performance characteristics across methods, as shown in Figure 4. Constrained by their rule-based or template-based paradigms, baseline methods exhibit limited diversity in both content and design dimensions, with scores predominantly concentrated at levels 2 and 3. In contrast, PPTAgent demonstrates a more dispersed score distribution, with the majority of presentations (>80%) achieving scores of 3 or higher in these dimensions. Furthermore, due to PPTAgent’s comprehensive consideration of structural slides, it achieves notably superior coherence scores, with over 80% of the presentations receiving scores above 4.

**ZH** 我们进一步考察了生成演示文稿的分数分布，以比较各方法的表现特征，如图 4 所示。受制于基于规则或基于模板的范式，基线方法在内容与设计维度上多样性有限，分数集中在 2 分与 3 分档。相比之下，PPTAgent 的分数分布更为分散，超过 80% 的演示文稿在这两个维度上取得 3 分及以上。此外，由于 PPTAgent 充分考虑了结构性幻灯片，其连贯性分数明显更优——超过 80% 的演示文稿得分在 4 分以上。

**EN** 5.4 Effectiveness of Self-Correction

**ZH** 5.4 自我纠正的有效性

**EN** Figure 6 illustrates the number of iterations required to generate a slide using different language models. Although GPT-4o exhibits superior self-correction capabilities compared to Qwen2.5, Qwen2.5 encounters fewer errors in the first generation. Additionally, we observed that Qwen2-VL experiences errors more frequently and has poorer self-correction capabilities, likely due to its multimodal post-training (Wang et al., 2024a). Ultimately, all three models successfully corrected more than half of the errors, demonstrating that our iterative self-correction mechanism effectively ensures the success of the generation process.

**ZH** 图 6 展示了使用不同语言模型生成一张幻灯片所需的迭代次数。尽管 GPT-4o 展现出比 Qwen2.5 更强的自我纠正能力，Qwen2.5 在首次生成时的出错更少。此外我们观察到，Qwen2-VL 出错更频繁且自我纠正能力较弱，这可能是其多模态后训练所致（Wang et al., 2024a）。最终，三个模型都成功纠正了半数以上的错误，说明我们的迭代自我纠正机制有效地保障了生成过程的成功。

**EN** 5.5 Agreement Evaluation

**ZH** 5.5 一致性评测

<!-- [原子块 · img]  -->

**EN** Figure 7: Correlation heatmap between existing automated evaluation metrics along with the content and design dimension in PPTEval.

**ZH** 图 7：既有自动评测指标与 PPTEval 内容、设计维度之间的相关性热力图。

**EN** PPTEval with Human Preferences

**ZH** PPTEval 与人类偏好

**EN** Despite Chen et al. (2024a) have highlighted the impressive human-like discernment of LLMs in various generation tasks. However, it remains crucial to assess the correlation between LLM evaluations and human evaluations in the context of presentations. This necessity arises from findings by Laskar et al. (2024), which indicate that LLMs may not be adequate evaluators for complex tasks. Table 5 shows the correlation of ratings between humans and LLMs. The average Pearson correlation of 0.71 exceeds the scores of other evaluation methods (Kwan et al., 2024), indicating that PPTEval aligns well with human preferences.

**ZH** 尽管 Chen et al.（2024a）已强调 LLM 在各类生成任务中具备出色的类人辨别力，在演示文稿场景下评估 LLM 评价与人类评价之间的相关性仍十分必要。这一必要性源自 Laskar et al.（2024）的发现：对复杂任务而言，LLM 未必是合格的评测者。表 5 给出了人类评分与 LLM 评分之间的相关性。平均皮尔逊相关系数达 0.71，高于其他评测方法（Kwan et al., 2024），说明 PPTEval 与人类偏好高度契合。

**EN** PPTEval with Existing Metrics

**ZH** PPTEval 与既有指标

**EN** We analyzed the relationships between PPTEval’s content and design dimensions and existing metrics through Pearson correlation analysis, as shown in Figure 7. The Pearson correlation coefficients reveal that current metrics are ineffective for presentation evaluation. Specifically, PPL primarily measures text fluency but performs poorly on slide content due to its inherent fragmented nature, frequently producing outlier measurements. Similarly, while ROUGE-L and FID quantify similarity to reference text and presentations respectively, these metrics inadequately assess content and design quality, as high conformity to references does not guarantee presentation effectiveness. These weak correlations highlight the necessity of PPTEval for robust and comprehensive presentation evaluation that considers both content quality and design effectiveness.

**ZH** 我们通过皮尔逊相关分析考察了 PPTEval 内容与设计维度与既有指标之间的关系，如图 7 所示。相关系数表明，现有指标对演示文稿评测是失效的。具体地，PPL 主要度量文本流畅度，但由于幻灯片内容天然碎片化，它在幻灯片内容上表现很差，常产生离群测量值。类似地，ROUGE-L 与 FID 分别量化与参考文本、参考演示文稿的相似度，但这些指标无法充分评估内容与设计质量，因为与参考高度一致并不保证演示文稿的有效性。这些微弱的相关性凸显了 PPTEval 的必要性——它能兼顾内容质量与设计效果，对演示文稿做出稳健而全面的评测。

**EN** 6 Related Works

**ZH** 6 相关工作

**EN** Automated Presentation Generation

**ZH** 自动演示文稿生成

**EN** Recent proposed methods for slide generation can be categorized into rule-based and template-based based on how they handle element placement and styling. Rule-based methods, such as those proposed by Mondal et al. (2024) and Bandyopadhyay et al. (2024), often focus on enhancing textual content but neglect the visual-centric nature of presentations, leading to outputs that lack engagement. Template-based methods, including Cachola et al. (2024) and industrial solutions like Tongyi, rely on predefined templates to create visually appealing presentations. However, their dependence on extensive manual effort for template annotation significantly limits scalability and flexibility.

**ZH** 近期提出的幻灯片生成方法，可按其处理元素摆放与样式的方式分为基于规则与基于模板两类。基于规则的方法（如 Mondal et al. (2024) 与 Bandyopadhyay et al. (2024)）往往专注于强化文本内容，却忽视演示文稿以视觉为中心的本质，导致输出缺乏吸引力。基于模板的方法（包括 Cachola et al. (2024) 以及通义等工业界方案）依赖预定义模板来生成视觉上美观的演示文稿，但模板标注需要大量人工投入，严重限制了可扩展性与灵活性。

**EN** LLM Agent

**ZH** LLM 智能体

**EN** Numerous studies (Li et al., 2024; Deng et al., 2024; Tang et al., 2025) have explored the potential of LLMs to act as agents assisting humans in a wide array of tasks. For example, Wang et al. (2024b) demonstrate the capability of LLMs to accomplish tasks by generating executable actions. Furthermore, Guo et al. (2023) demonstrated the potential of LLMs in automating presentation-related tasks through API integration.

**ZH** 大量研究（Li et al., 2024; Deng et al., 2024; Tang et al., 2025）探索了让 LLM 充当智能体、在广泛任务中辅助人类的潜力。例如 Wang et al.（2024b）展示了 LLM 通过生成可执行动作来完成任务的能力；Guo et al.（2023）则展示了 LLM 通过 API 集成自动化处理演示文稿相关任务的潜力。

**EN** LLM as a Judge

**ZH** LLM 作为评判者

**EN** LLMs have exhibited strong capabilities in instruction following and context perception, which has led to their widespread adoption as judges (Liu et al., 2023; Zheng et al., 2023). Chen et al. (2024a) demonstrated the feasibility of using MLLMs as judges, while Kwan et al. (2024) proposed a multi-dimensional evaluation framework. Additionally, Ge et al. (2025) investigated the use of LLMs for assessing single-slide quality. However, they did not evaluate presentation quality from a holistic perspective.

**ZH** LLM 在指令遵循与语境感知上表现出色，因而被广泛用作评判者（Liu et al., 2023; Zheng et al., 2023）。Chen et al.（2024a）证明了用 MLLM 充当评判器的可行性，Kwan et al.（2024）提出了一个多维度评测框架，Ge et al.（2025）则研究了用 LLM 评估单张幻灯片质量。但它们都未从整体视角评价演示文稿质量。

<!-- [原子块 · table] Correlation Content Design Coherence Avg. Pearson 0.70 0.90 0.55 0.71 Spearman 0.73 0.88 0.57 0.74 -->

**EN** Table 5: The correlation scores between human ratings and LLM ratings under different dimensions (Coherence, Content, Design). All presented data of similarity exhibit a p-value below 0.05, indicating a statistically significant level of confidence.

**ZH** 表 5：人类评分与 LLM 评分在各维度（连贯性、内容、设计）上的相关性分数。所有相似性数据的 p 值均低于 0.05，表明具有统计显著的置信水平。

**EN** 7 Conclusion

**ZH** 7 结论

**EN** In this paper, we introduce PPTAgent, which conceptualizes presentation generation as a two-stage presentation editing task completed through LLMs’ abilities to understand and generate code. Moreover, we propose PPTEval to provide quantitative metrics for assessing presentation quality. Our experiments across data from multiple domains have demonstrated the superiority of our method. This research provides a new paradigm for generating slides under unsupervised conditions and offers insights for future work in presentation generation.

**ZH** 本文提出 PPTAgent，它把演示文稿生成构想为一项两阶段的演示文稿编辑任务，借助 LLM 理解与生成代码的能力来完成。此外，我们提出 PPTEval，为评估演示文稿质量提供量化指标。我们在多领域数据上开展的实验证明了本方法的优越性。本研究为无监督条件下生成幻灯片提供了新范式，并为演示文稿生成的后续工作带来启示。

**EN** Limitations

**ZH** 局限性

**EN** While PPTAgent demonstrates promising capabilities in presentation generation, several limitations remain. First, despite achieving a high success rate (>95%) on our dataset, the model occasionally fails to generate presentations, which could limit its reliability. Second, although we can provide high-quality preprocessed presentations as references, the quality of generated presentations is still influenced by the input reference presentation, which may lead to suboptimal outputs. Third, although PPTAgent shows improvements in layout optimization compared to prior approaches, it does not fully utilize visual information to refine the slide design. This manifests in occasional design flaws, such as overlapping elements, which can compromise the readability of generated slides. Future work should focus on enhancing the robustness, reducing reference dependency, and better incorporating visual information into the generation process.

**ZH** 尽管 PPTAgent 在演示文稿生成上展现出可期的能力，仍存在若干局限。首先，尽管在我们的数据集上成功率很高（超过 95%），模型偶尔仍会生成失败，这可能限制其可靠性。其次，尽管我们能提供高质量的预处理演示文稿作为参考，生成演示文稿的质量仍受输入参考演示文稿的影响，可能导致次优输出。第三，尽管相较此前方法，PPTAgent 在版式优化上有所改进，它并未充分利用视觉信息来打磨幻灯片设计，这表现为偶发的设计缺陷（例如元素重叠），会损害生成幻灯片的可读性。未来工作应聚焦于增强鲁棒性、降低对参考的依赖，并在生成过程中更好地融入视觉信息。

**EN** Ethical Considerations

**ZH** 伦理考量

**EN** In the construction of Zenodo10K, we utilized the publicly available API to scrape data while strictly adhering to the licensing terms associated with each artifact. Specifically, artifacts that were not permitted for modification or commercial use under their respective licenses were filtered out to ensure compliance with intellectual property rights. Additionally, all annotation personnel involved in the project were compensated at rates exceeding the minimum wage in their respective cities, reflecting our commitment to fair labor practices and ethical standards.

**ZH** 在构建 Zenodo10K 时，我们使用公开 API 抓取数据，并严格遵守每件成果所附的许可条款。具体地，我们过滤掉了在各自许可下不允许修改或商业使用的成果，以确保符合知识产权要求。此外，项目所有标注人员的报酬均高于其所在城市的最低工资标准，体现了我们对公平劳动实践与伦理准则的坚守。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] Bandyopadhyay et al. (2024) Sambaran Bandyopadhyay, Himanshu Maheshwari, Anandhavelu Natarajan, and Apoorv Saxena. 2024. Enhancing presentation slide generation by llms with a multi-staged end-to-end  -->

<!-- [原子块 · verbatim] Barrick et al. (2018) Andrea Barrick, Dana Davis, and Dana Winkler. 2018. Image versus text in powerpoint lectures: Who does it benefit? Journal of Baccalaureate Social Work , 23(1):91–109. -->

<!-- [原子块 · verbatim] Cachola et al. (2024) Isabel Alyssa Cachola, Silviu Cucerzan, Allen Herring, Vuksan Mijovic, Erik Oveson, and Sujay Kumar Jauhar. 2024. Knowledge-centric templatic views of documents . In Findings of  -->

<!-- [原子块 · verbatim] Chen et al. (2024a) Dongping Chen, Ruoxi Chen, Shilin Zhang, Yinuo Liu, Yaochen Wang, Huichi Zhou, Qihui Zhang, Pan Zhou, Yao Wan, and Lichao Sun. 2024a. Mllm-as-a-judge: Assessing multimodal llm-as-a -->

<!-- [原子块 · verbatim] Chen et al. (2024b) Jianlv Chen, Shitao Xiao, Peitian Zhang, Kun Luo, Defu Lian, and Zheng Liu. 2024b. Bge m3-embedding: Multi-lingual, multi-functionality, multi-granularity text embeddings through s -->

<!-- [原子块 · verbatim] Deng et al. (2024) Xiang Deng, Yu Gu, Boyuan Zheng, Shijie Chen, Sam Stevens, Boshi Wang, Huan Sun, and Yu Su. 2024. Mind2web: Towards a generalist agent for the web. Advances in Neural Information Pr -->

<!-- [原子块 · verbatim] Duarte (2008) Nancy Duarte. 2008. Slide: ology: The art and science of creating great presentations , volume 1. O’Reilly Media Sebastapol. -->

<!-- [原子块 · verbatim] Duarte (2010) Nancy Duarte. 2010. Resonate: Present visual stories that transform audiences . John Wiley & Sons. -->

<!-- [原子块 · verbatim] Dubey et al. (2024) Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Amy Yang, Angela Fan, et al. 2024. The llama 3 herd of -->

<!-- [原子块 · verbatim] European Organization For Nuclear Research and OpenAIRE (2013) European Organization For Nuclear Research and OpenAIRE. 2013. Zenodo . -->

<!-- [原子块 · verbatim] Feng et al. (2024) Weixi Feng, Wanrong Zhu, Tsu-jui Fu, Varun Jampani, Arjun Akula, Xuehai He, Sugato Basu, Xin Eric Wang, and William Yang Wang. 2024. Layoutgpt: Compositional visual planning and gen -->

<!-- [原子块 · verbatim] Fu et al. (2022) Tsu-Jui Fu, William Yang Wang, Daniel McDuff, and Yale Song. 2022. Doc2ppt: Automatic presentation slides generation from scientific documents . Proceedings of the AAAI Conference on  -->

<!-- [原子块 · verbatim] Ge et al. (2025) Jiaxin Ge, Zora Zhiruo Wang, Xuhui Zhou, Yi-Hao Peng, Sanjay Subramanian, Qinyue Tan, Maarten Sap, Alane Suhr, Daniel Fried, Graham Neubig, et al. 2025. Autopresent: Designing structu -->

<!-- [原子块 · verbatim] Gryk (2022) Michael Robert Gryk. 2022. Human readability of data files. Balisage series on markup technologies , 27. -->

<!-- [原子块 · verbatim] Guan et al. (2024) Xinyan Guan, Yanjiang Liu, Hongyu Lin, Yaojie Lu, Ben He, Xianpei Han, and Le Sun. 2024. Mitigating large language model hallucinations via autonomous knowledge graph-based retrofit -->

<!-- [原子块 · verbatim] Guo et al. (2023) Yiduo Guo, Zekai Zhang, Yaobo Liang, Dongyan Zhao, and Duan Nan. 2023. Pptc benchmark: Evaluating large language models for powerpoint task completion. arXiv preprint arXiv:2311.0176 -->

<!-- [原子块 · verbatim] Heusel et al. (2017) Martin Heusel, Hubert Ramsauer, Thomas Unterthiner, Bernhard Nessler, and Sepp Hochreiter. 2017. Gans trained by a two time-scale update rule converge to a local nash equilibrium. -->

<!-- [原子块 · verbatim] Kamoi et al. (2024) Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, and Rui Zhang. 2024. When can llms actually correct their own mistakes? a critical survey of self-correction of llms. Transactions of -->

<!-- [原子块 · verbatim] Kwan et al. (2024) Wai-Chung Kwan, Xingshan Zeng, Yuxin Jiang, Yufei Wang, Liangyou Li, Lifeng Shang, Xin Jiang, Qun Liu, and Kam-Fai Wong. 2024. Mt-eval: A multi-turn capabilities evaluation benchmar -->

<!-- [原子块 · verbatim] Kwon et al. (2023) Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph Gonzalez, Hao Zhang, and Ion Stoica. 2023. Efficient memory management for large language mode -->

<!-- [原子块 · verbatim] Laskar et al. (2024) Md Tahmid Rahman Laskar, Sawsan Alqahtani, M Saiful Bari, Mizanur Rahman, Mohammad Abdullah Matin Khan, Haidar Khan, Israt Jahan, Amran Bhuiyan, Chee Wei Tan, Md Rizwan Parvez, En -->

<!-- [原子块 · verbatim] Li et al. (2024) Yanda Li, Chi Zhang, Wanqi Yang, Bin Fu, Pei Cheng, Xin Chen, Ling Chen, and Yunchao Wei. 2024. Appagent v2: Advanced agent for flexible mobile interactions. arXiv preprint arXiv:2408 -->

<!-- [原子块 · verbatim] Lin (2004) Chin-Yew Lin. 2004. ROUGE: A package for automatic evaluation of summaries . In Text Summarization Branches Out , pages 74–81, Barcelona, Spain. Association for Computational Linguistics. -->

<!-- [原子块 · verbatim] Liu et al. (2023) Yang Liu, Dan Iter, Yichong Xu, Shuohang Wang, Ruochen Xu, and Chenguang Zhu. 2023. G-eval: NLG evaluation using gpt-4 with better human alignment . In Proceedings of the 2023 Confer -->

<!-- [原子块 · verbatim] Maheshwari et al. (2024) Himanshu Maheshwari, Sambaran Bandyopadhyay, Aparna Garimella, and Anandhavelu Natarajan. 2024. Presentations are not always linear! gnn meets llm for document-to-presentation -->

<!-- [原子块 · verbatim] Mondal et al. (2024) Ishani Mondal, S Shwetha, Anandhavelu Natarajan, Aparna Garimella, Sambaran Bandyopadhyay, and Jordan Boyd-Graber. 2024. Presentations by the humans and for the humans: Harnessing -->

<!-- [原子块 · verbatim] Sefid et al. (2021) Athar Sefid, Prasenjit Mitra, and Lee Giles. 2021. Slidegen: an abstractive section-based slide generator for scholarly documents. In Proceedings of the 21st ACM Symposium on Docum -->

<!-- [原子块 · verbatim] Sun et al. (2021) Edward Sun, Yufang Hou, Dakuo Wang, Yunfeng Zhang, and Nancy XR Wang. 2021. D2s: Document-to-slide generation via query-based text summarization. arXiv preprint arXiv:2105.03664 . -->

<!-- [原子块 · verbatim] Tang et al. (2025) Hao Tang, Darren Key, and Kevin Ellis. 2025. Worldcoder, a model-based llm agent: Building world models by writing code and interacting with the environment. Advances in Neural Info -->

<!-- [原子块 · verbatim] VikParuchuri (2023) VikParuchuri. 2023. marker . -->

<!-- [原子块 · verbatim] Wang et al. (2024a) Peng Wang, Shuai Bai, Sinan Tan, Shijie Wang, Zhihao Fan, Jinze Bai, Keqin Chen, Xuejing Liu, Jialin Wang, Wenbin Ge, et al. 2024a. Qwen2-vl: Enhancing vision-language model’s perc -->

<!-- [原子块 · verbatim] Wang et al. (2024b) Xingyao Wang, Yangyi Chen, Lifan Yuan, Yizhe Zhang, Yunzhu Li, Hao Peng, and Heng Ji. 2024b. Executable code actions elicit better llm agents. arXiv preprint arXiv:2402.01030 . -->

<!-- [原子块 · verbatim] Wu et al. (2020) Bichen Wu, Chenfeng Xu, Xiaoliang Dai, Alvin Wan, Peizhao Zhang, Zhicheng Yan, Masayoshi Tomizuka, Joseph Gonzalez, Kurt Keutzer, and Peter Vajda. 2020. Visual transformers: Token-bas -->

<!-- [原子块 · verbatim] Wu et al. (2024) Tong Wu, Guandao Yang, Zhibing Li, Kai Zhang, Ziwei Liu, Leonidas Guibas, Dahua Lin, and Gordon Wetzstein. 2024. Gpt-4v (ision) is a human-aligned evaluator for text-to-3d generation. -->

<!-- [原子块 · verbatim] Yang et al. (2024) An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan Li, Dayiheng Liu, Fei Huang, Haoran Wei, et al. 2024. Qwen2. 5 technical report. arXiv preprint arXi -->

<!-- [原子块 · verbatim] Zheng et al. (2023) Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric Xing, et al. 2023. Judging llm-as-a-judge with mt-bench  -->

**EN** Appendix A Data Preprocessing

**ZH** 附录 A 数据预处理

**EN** To maintain a reasonable cost, we selected presentations ranging from 12 to 64 pages and documents with text lengths from 2,048 to 20,480 characters. We extracted both textual and visual content from the source documents using VikParuchuri (2023). The extracted text was then organized into sections. For visual content, we generated image captions to assist in relevant image selection through textual descriptions. To minimize redundancy, we identified and removed duplicate images if their image embeddings had a cosine similarity score exceeding 0.85. For slide-level deduplication, we removed individual slides if their text embeddings had a cosine similarity score above 0.8 compared to the preceding slide, as suggested by Fu et al. (2022).

**ZH** 为控制合理的成本，我们选取页数在 12 到 64 之间的演示文稿，以及文本长度在 2048 到 20480 字符之间的文档。我们使用 VikParuchuri（2023）从源文档中提取文本内容与视觉内容，并把提取出的文本组织为若干章节。对视觉内容，我们生成图像说明，以便通过文本描述辅助相关图像的选取。为减少冗余，若两张图像的嵌入余弦相似度超过 0.85，我们判定并删除重复图像。在幻灯片层面，若某张幻灯片与上一张幻灯片的文本嵌入余弦相似度高于 0.8，则删除该幻灯片（依 Fu et al. (2022) 的建议）。

**EN** Appendix B Details of PPTEval

**ZH** 附录 B PPTEval 细节

**EN** We recruited four graduate students through a Shanghai-based crowdsourcing platform to evaluate a total of 250 presentations: 50 randomly selected from Zenodo10K representing real-world presentations, along with two sets of 100 presentations generated by the baseline method and our approach respectively. Following the evaluation framework proposed by PPTEval, assessments were conducted across three dimensions using the scoring criteria detailed in Appendix F. Evaluators were provided with converted slide images, scored them individually, and then discussed the results to reach a consensus on the final scores.

**ZH** 我们通过一家位于上海的众包平台招募了四名研究生，对共计 250 份演示文稿进行评测：其中 50 份从 Zenodo10K 中随机选取，代表真实世界的演示文稿；另有两组各 100 份，分别由基线方法与我们的方法生成。依照 PPTEval 提出的评测框架，评测沿三个维度展开，评分标准详见附录 F。评测者拿到转换后的幻灯片图像，各自独立打分，随后讨论结果以就最终分数达成共识。

**EN** Moreover, We measured inter-rater agreement using Fleiss’ Kappa, with an average score of 0.59 across three dimensions (0.61, 0.61, 0.54 for Content, Design, and Coherence, respectively) indicating satisfactory agreement (Kwan et al., 2024) among evaluators. Representative scoring examples are shown in Figure 8.

**ZH** 此外，我们用 Fleiss’ Kappa 度量评分者间一致性，三个维度的平均分为 0.59（内容、设计与连贯性分别为 0.61、0.61、0.54），表明评测者之间具有令人满意的一致性（Kwan et al., 2024）。代表性评分示例如图 8 所示。

**EN** We provided detailed illustration as below:

**ZH** 下面给出详细说明：

**EN** Content:

**ZH** 内容：

**EN** The content dimension evaluates the information presented on the slides, focusing on both text and images. We assess content quality from three perspectives: the amount of information, the clarity and quality of textual content, and the support provided by visual content. High-quality textual content is characterized by clear, impactful text that conveys the proper amount of information. Additionally, images should complement and reinforce the textual content, making the information more accessible and engaging. To evaluate content quality, we employ MLLMs on slide images, as slides cannot be easily comprehended in a plain text format.

**ZH** 内容维度评价幻灯片上呈现的信息，同时关注文本与图像。我们从三个角度评估内容质量：信息量、文本内容的清晰度与质量，以及视觉内容提供的支撑。高质量的文本内容应清晰、有力，传递恰当分量的信息。此外，图像应补充并强化文本内容，使信息更易于理解、更具吸引力。为评估内容质量，我们在幻灯片图像上使用 MLLM，因为幻灯片难以用纯文本格式理解。

**EN** Design:

**ZH** 设计：

**EN** Good design not only captures attention but also enhances content delivery. We evaluate the design dimension based on three aspects: color schemes, visual elements, and overall design. Specifically, the color scheme of the slides should have clear contrast to highlight the content while maintaining harmony. The use of visual elements, such as geometric shapes, can make the slide design more expressive. Finally, good design should adhere to basic design principles, such as avoiding overlapping elements and ensuring that design does not interfere with content delivery.

**ZH** 优秀的设计不仅能抓住注意力，还能强化内容传达。我们从三个方面评价设计维度：配色方案、视觉元素与整体设计。具体地，幻灯片的配色应具有清晰对比以突出内容，同时保持和谐；几何形状等视觉元素的运用能让幻灯片设计更具表现力；最后，好的设计应遵循基本设计原则，例如避免元素重叠、确保设计不妨碍内容传达。

**EN** Coherence:

**ZH** 连贯性：

**EN** Coherence is essential for maintaining audience engagement in a presentation. We evaluate coherence based on the logical structure and the contextual information provided. Effective coherence is achieved when the model constructs a captivating storyline, enriched with contextual information that enables the audience to follow the content seamlessly. We assess coherence by analyzing the logical structure and contextual information extracted from the presentation.

**ZH** 连贯性对维持演示文稿的受众参与度至关重要。我们依据逻辑结构与所提供的语境信息来评价连贯性。当模型构建出引人入胜的故事线，并辅以能让受众顺畅跟随内容的语境信息时，就实现了有效的连贯性。我们通过分析从演示文稿中抽取的逻辑结构与语境信息来评估连贯性。

**EN** Appendix C Detailed Performance of PPTAgent

**ZH** 附录 C PPTAgent 的详细表现

**EN** We present a detailed performance analysis of Qwen2.5LM+Qwen2-VLVM across various domains in Table 8. Additionally, Table 7 and 6 show the success rate-weighted performance, where failed generations receive a PPTEval score of 0, demonstrating that a lower success rate significantly impacts the overall effectiveness of the method.

**ZH** 表 8 给出了 Qwen2.5LM+Qwen2-VLVM 在各领域的详细性能分析。此外，表 7 与表 6 展示了按成功率加权后的性能——生成失败的样本 PPTEval 分数记为 0——说明较低的成功率会显著影响方法的整体效果。

**EN** As demonstrated in Table 6. GPT-4o consistently demonstrates outstanding performance across various evaluation metrics, highlighting its advanced capabilities. While Qwen2-VL exhibits limitations in linguistic proficiency due to the trade-offs from multimodal post-training, GPT-4o maintains a clear advantage in handling language tasks. However, the introduction of Qwen2.5 successfully mitigates these linguistic deficiencies, bringing its performance on par with GPT-4o, and achieving the best performance. This underscores the significant potential of open-source LLMs as competitive and highly capable presentation agents.

**ZH** 如表 6 所示，GPT-4o 在各项评测指标上始终表现突出，彰显了其先进能力。虽然 Qwen2-VL 因多模态后训练的取舍而在语言能力上存在局限，GPT-4o 在处理语言任务上保持明显优势。然而，引入 Qwen2.5 成功弥补了这些语言缺陷，使其性能与 GPT-4o 相当，并取得最佳表现。这凸显了开源 LLM 作为有竞争力且能力出众的演示文稿智能体的巨大潜力。

**EN** Appendix D Slide Clustering

**ZH** 附录 D 幻灯片聚类

**EN** We present our hierarchical clustering algorithm for layout analysis in Algorithm 1, where slides are grouped into clusters using a similarity threshold ⟦SLOT_30⟧ of 0.65. To focus exclusively on layout patterns and minimize interference from specific content, we preprocess the slides by replacing text content with a placeholder character (“a”) and substituting image elements with solid-color backgrounds. Then, we compute the similarity matrix using cosine similarity based on the ViT embeddings of converted slide images between each slide pair. Figure 9 illustrates representative examples from the resulting slide clusters.

**ZH** 算法 1 给出了我们用于版式分析的层次聚类算法，其中幻灯片以 0.65 的相似度阈值 ⟦SLOT_30⟧ 归组。为只关注版式模式、尽量减少具体内容带来的干扰，我们对幻灯片做了预处理：把文本内容替换为占位字符（“a”），并把图像元素替换为纯色背景。随后，我们基于转换后幻灯片图像的 ViT 嵌入，用余弦相似度计算每对幻灯片之间的相似度矩阵。图 9 展示了所得幻灯片簇的代表性示例。

**EN** Appendix E Code Interaction

**ZH** 附录 E 代码交互

**EN** For visual reference, Figure 10 illustrates a slide rendered in HTML format, while Figure 11 displays its excerpt (first 60 lines) of the XML representation (out of 1,006 lines).

**ZH** 为便于直观参照，图 10 展示了一张以 HTML 格式渲染的幻灯片，图 11 则展示了其 XML 表示的节选（前 60 行，全长 1006 行）。

**EN** Appendix F Prompts

**ZH** 附录 F 提示词

**EN** F.1 Prompts for Presentation Analysis

**ZH** F.1 演示文稿分析所用提示词

**EN** The prompts used for presentation analysis are illustrated in Figures 12, 13, and 14.

**ZH** 演示文稿分析所用的提示词见图 12、图 13 与图 14。

**EN** F.2 Prompts for Presentation Generation

**ZH** F.2 演示文稿生成所用提示词

**EN** The prompts used for generating presentations are shown in Figures 15, 16, and 17.

**ZH** 生成演示文稿所用的提示词见图 15、图 16 与图 17。

**EN** F.3 Prompts for PPTEval

**ZH** F.3 PPTEval 所用提示词

**EN** The prompts used in PPTEval are shown in Figure 18, 19, 20, 21, 22 and 23.

**ZH** PPTEval 所用的提示词见图 18、19、20、21、22 与 23。

**EN** Algorithm 1 Slides Clustering Algorithm

**ZH** 算法 1 幻灯片聚类算法

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

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · table] Configuration Existing Metrics PPTEval Language Model Vision Model SR(%) ↑ \uparrow PPL ↓ \downarrow ROUGE-L ↑ \uparrow FID ↓ \downarrow Content ↑ \uparrow Design ↑ \uparrow Coherence ↑ \uparrow Avg.  -->

**EN** Table 6: Weighted Performance comparison of presentation generation methods, including DocPres, KCTV, and our proposed PPTAgent. Results are evaluated using Success Rate (SR), Perplexity (PPL), Rouge-L, Fr’echet Inception Distance (FID), and SR-weighted PPTEval.

**ZH** 表 6：各演示文稿生成方法（包括 DocPres、KCTV 与我们提出的 PPTAgent）的加权性能对比。评测采用成功率（SR）、困惑度（PPL）、Rouge-L、Fréchet Inception Distance（FID）以及按 SR 加权的 PPTEval。

<!-- [原子块 · table] Setting SR(%) Content Design Coherence Avg. PPTAgent 95.0 3.11 3.10 4.25 3.48 w/o Outline 91.0 2.94 3.00 3.05 3.00 w/o Schema 78.8 2.42 2.54 3.18 2.71 w/o Structure 92.2 3.02 2.99 3.18 3.06 w/o CodeRe -->

**EN** Table 7: Ablation analysis of PPTAgent utilizing the Qwen2.5⟦SLOT_31⟧+Qwen2-VL⟦SLOT_32⟧ configuration, with PPTEval scores weighted by success rate to demonstrate each component’s contribution.

**ZH** 表 7：在 Qwen2.5⟦SLOT_31⟧+Qwen2-VL⟦SLOT_32⟧ 配置下对 PPTAgent 的消融分析，其中 PPTEval 分数按成功率加权，以展示各组件的贡献。

**EN** Domain SR (%) PPL FID PPTEval Culture 93.0 185.3 5.00 3.70 Education 94.0 249.0 7.90 3.69 Science 96.0 500.6 6.07 3.56 Society 95.0 396.8 5.32 3.59 Tech 97.0 238.7 6.72 3.74

**ZH** 领域 SR (%) PPL FID PPTEval Culture 93.0 185.3 5.00 3.70 Education 94.0 249.0 7.90 3.69 Science 96.0 500.6 6.07 3.56 Society 95.0 396.8 5.32 3.59 Tech 97.0 238.7 6.72 3.74

**EN** Table 8: Evaluation results under the configuration of Qwen2-VL⟦SLOT_33⟧+Qwen2-VL⟦SLOT_34⟧ in different domains, using the success rate (SR), PPL, FID and the average PPTEval score across three evaluation dimensions.

**ZH** 表 8：在 Qwen2-VL⟦SLOT_33⟧+Qwen2-VL⟦SLOT_34⟧ 配置下各领域的评测结果，采用成功率（SR）、PPL、FID 以及三个评测维度的 PPTEval 平均分。

<!-- [原子块 · img]  -->

**EN** Figure 8: Scoring Examples of PPTEval.

**ZH** 图 8：PPTEval 的评分示例。

<!-- [原子块 · img]  -->

**EN** Figure 9: Example of slide clusters.

**ZH** 图 9：幻灯片簇示例。

<!-- [原子块 · img]  -->

**EN** Figure 10: Example of rendering a slide into HTML format.

**ZH** 图 10：把一张幻灯片渲染为 HTML 格式的示例。

<!-- [原子块 · img]  -->

**EN** Figure 11: The first 60 lines of the XML representation of a presentation slide (out of 1,006 lines).

**ZH** 图 11：一张演示文稿幻灯片的 XML 表示的前 60 行（全长 1006 行）。

<!-- [原子块 · object]  -->

**EN** Figure 12: Illustration of the prompt used for clustering structural slides.

**ZH** 图 12：用于结构性幻灯片聚类的提示词示例。

<!-- [原子块 · object]  -->

**EN** Figure 13: Illustration of the prompt used to infer layout patterns.

**ZH** 图 13：用于推断版式模式的提示词示例。

<!-- [原子块 · object]  -->

**EN** Figure 14: Illustration of the prompt used to extract the slide schema.

**ZH** 图 14：用于抽取幻灯片模式的提示词示例。

<!-- [原子块 · object]  -->

**EN** Figure 15: Illustration of the prompt used for generating the outline.

**ZH** 图 15：用于生成大纲的提示词示例。

<!-- [原子块 · object]  -->

**EN** Figure 16: Illustration of the prompt used for generating slide content.

**ZH** 图 16：用于生成幻灯片内容的提示词示例。

<!-- [原子块 · object]  -->

**EN** Figure 17: Illustration of the prompt used for generating editing actions.

**ZH** 图 17：用于生成编辑动作的提示词示例。

<!-- [原子块 · object]  -->

**EN** Figure 18: Illustration of the prompt used to describe content in PPTEval.

**ZH** 图 18：PPTEval 中用于描述内容的提示词示例。

<!-- [原子块 · object]  -->

**EN** Figure 19: Illustration of the prompt used to describe style in PPTEval.

**ZH** 图 19：PPTEval 中用于描述风格的提示词示例。

<!-- [原子块 · object]  -->

**EN** Figure 20: Illustration of the prompt used to extract content in PPTEval.

**ZH** 图 20：PPTEval 中用于抽取内容的提示词示例。

<!-- [原子块 · object]  -->

**EN** Figure 21: Illustration of the prompt used to evaluate content in PPTEval.

**ZH** 图 21：PPTEval 中用于评价内容的提示词示例。

<!-- [原子块 · object]  -->

**EN** Figure 22: Illustration of the prompt used to evaluate style in PPTEval.

**ZH** 图 22：PPTEval 中用于评价风格的提示词示例。

<!-- [原子块 · object]  -->

**EN** Figure 23: Illustration of the prompt used to evaluate coherence in PPTEval.

**ZH** 图 23：PPTEval 中用于评价连贯性的提示词示例。
