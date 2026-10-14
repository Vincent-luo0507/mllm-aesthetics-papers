# AutoPresent：从零开始设计结构化视觉内容

> 原标题：AutoPresent: Designing Structured Visuals from Scratch
> 作者：Jiaxin Ge, Zora Zhiruo Wang, Xuhui Zhou, Yi-Hao Peng, Sanjay Subramanian, Qinyue Tan, Maarten Sap, Alane Suhr, Daniel Fried, Graham Neubig, Trevor Darrell · arXiv:2501.00912 · 2025-01-01

<!-- [原子块 · verbatim] AutoPresent : Designing Structured Visuals from Scratch -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] Designing structured visuals such as presentation slides is essential for communicative needs, necessitating both content creation and visual planning skills. In this work, we tackle the challenge of  -->

**EN** 1 Introduction

**ZH** 1 引言

**EN** Designing structured visuals such as presentation slides from scratch is an essential skill for effective communication and conveying complex ideas [30]. Among various forms of visual communication, creating a compelling set of slides is a challenging problem, requiring content creation (text, pictures, diagrams, and more) and visual planning skills, to ensure the slides are well designed [25] and convey insights with clarity [3, 36]. Even human experts may need to spend hours iterating and polishing their slide decks [10] to produce high-quality designs with clear insights. While digital agents have demonstrated impressive capabilities in tasks such as software engineering [49], web navigation [54, 46], and free-form image design generation [8, 32], their creative capabilities in generating semi-structured communicative media like slide decks has not been extensively tested. Therefore, we ask: Can we employ powerful AI agents to create high-quality presentation slides that are well-structured and insight-revealing?

**ZH** 从零开始设计演示幻灯片这类结构化视觉内容，是有效沟通与传达复杂思想的一项必备技能 [30]。在各种视觉沟通形式中，制作一套有说服力的幻灯片是个颇具挑战的问题：它既需要内容创作（文字、图片、图表等），也需要视觉规划能力，以确保幻灯片设计得当 [25] 并清晰地传达洞见 [3, 36]。即便是人类专家，为了产出设计精良、洞见清晰的高质量作品，也可能需要花上数小时反复迭代与打磨自己的幻灯片组 [10]。尽管数字智能体已在软件工程 [49]、网页导航 [54, 46]、自由形式的图像设计生成 [8, 32] 等任务上展现出令人印象深刻的能力，它们在生成幻灯片组这类半结构化传播媒介上的创造能力尚未被充分检验。因此我们提出这样一个问题：能否借助强大的 AI 智能体，制作出结构良好、洞见彰显的高质量演示幻灯片？

**EN** In this work, we formulate the natural language (NL) to slide generation task. At a high level, the user provides the system with a natural language instruction about the desired slide, and the system then generates an editable presentation, as shown in . We consider three types of user instructions: (1) detailed instruction with images. (2) detailed instructions only. (3) high-level instructions, reflecting varying levels of design freedom.

**ZH** 本文形式化了自然语言（NL）到幻灯片的生成任务。在高层次上，用户向系统提供一段关于所需幻灯片的自然语言指令，系统随后生成一份可编辑的演示文稿，如图所示。我们考虑三类用户指令：(1) 带图像的详细指令；(2) 仅详细指令；(3) 高层指令，反映不同程度的设计自由度。

**EN** Since there are no existing tools for quantifying agent performance in slide generation tasks, we propose the SlidesBench benchmark (§2) as a training source and test bed for method comparisons. SlidesBench contains 7⟦SLOT_0⟧ training examples and 585 testing examples of varied instruction difficulties, constructed from 310 publicly available slide decks from 10 different domains, including art, business, and technology. To evaluate generated slides, we introduce two sets of evaluation metrics: reference-based metrics to examine position, content, and color match against the reference slide; and reference-free metrics inspired by slide design principles [9, 34, 5, 44, 39] to measure the design quality of agent-created slides alone, given that many good designs for the same instructions may vary from the reference slide.

**ZH** 由于现有工具无法量化智能体在幻灯片生成任务上的性能，我们提出 SlidesBench 基准（§2），作为方法比较的训练来源与测试平台。SlidesBench 包含 7⟦SLOT_0⟧ 条训练示例与 585 条测试示例，指令难度各异，由来自艺术、商业、科技等 10 个不同领域的 310 个公开可得的幻灯片组构建而成。为评估生成的幻灯片，我们引入两套评测指标：基于参考的指标，用于考察与参考幻灯片在位置、内容与颜色上的匹配；以及受幻灯片设计原则 [9, 34, 5, 44, 39] 启发的无参考指标，用于单独衡量智能体所生成幻灯片的设计质量——因为对同一指令而言，许多优秀设计可能与参考幻灯片并不相同。

**EN** To enable controlled and structured slide generation, we propose to create slides using program generation, where a model first generates a program from the natural language instruction, and then the program is executed to get the slide. We apply this approach to large language models (LLMs; LlaMa [11], DeepseekCoder [16], CodeLlama [33], GPT-4o [2]) and vision-language models (VLMs; LlaVa [51]). As illustrated in , given a natural language instruction, the model first generates a Python program and then executes it to obtain a PPTX slide. We find that small models such as LlaMa (8B) and LlaVa (7B) are often unable to produce executable code. While GPT-4o can produce reasonable slides, it still exhibits a substantial gap in design quality compared to human-generated slides (§5). By further conducting iterative refinement, we find that models can self-refine and further improve slide quality. We also find that code generation approaches substantially outperform end-to-end image generation methods (Stable Diffusion [32], Dall-E [8]).

**ZH** 为实现可控、结构化的幻灯片生成，我们提出用程序生成的方式来制作幻灯片：模型先从自然语言指令生成一个程序，再执行该程序得到幻灯片。我们把这一方法应用于大语言模型（LLM；LlaMa [11]、DeepseekCoder [16]、CodeLlama [33]、GPT-4o [2]）与视觉语言模型（VLM；LlaVa [51]）。如图所示，给定自然语言指令，模型先生成一个 Python 程序，再执行它以获得一张 PPTX 幻灯片。我们发现，LlaMa（8B）与 LlaVa（7B）等小模型常常无法产出可执行代码；GPT-4o 虽能生成尚可的幻灯片，但其设计质量与人类制作的幻灯片相比仍有明显差距（§5）。进一步开展迭代精修后，我们发现模型能够自我改进并进一步提升幻灯片质量。我们还发现，代码生成方法显著优于端到端图像生成方法（Stable Diffusion [32]、Dall-E [8]）。

**EN** To further enhance the current model’s ability to generate high-quality slides, we present our open-sourced AutoPresent (8B) model (§4.2) which is fine-tuned from LlaMa 8B on the SlidesBench training set. AutoPresent achieves state-of-the-art performance among small open-sourced models and approaches the performance of the closed-sourced model GPT-4o. Since directly generating a long program is difficult for current models [14], we further create the SlidesLib library to simplify the program generation process. SlidesLib contains high-level functions that are basic such as add_title, and image-related such as search_image and generate_image. We show that LLMs and VLMs generally perform better when given access to SlidesLib.

**ZH** 为进一步提升现有模型生成高质量幻灯片的能力，我们开源了 AutoPresent（8B）模型（§4.2），它在 SlidesBench 训练集上由 LlaMa 8B 微调而来。AutoPresent 在小型开源模型中取得最先进性能，并接近闭源模型 GPT-4o 的表现。由于直接生成长程序对当前模型而言较为困难 [14]，我们进一步创建了 SlidesLib 库以简化程序生成过程。SlidesLib 既包含 add_title 等基础高层函数，也包含 search_image 与 generate_image 等图像相关函数。我们表明，在获得 SlidesLib 之后，LLM 与 VLM 的表现普遍更好。

**EN** Our main contributions can be summarized as follows:

**ZH** 我们的主要贡献可概括如下：

**EN** • We formulate the NL-to-slide generation task and build SlidesBench, the first benchmark for slide generation, which contains 7⟦SLOT_1⟧ training and 585 test examples and supports automatic evaluations.

**ZH** • 我们形式化了自然语言到幻灯片的生成任务，并构建了 SlidesBench——首个面向幻灯片生成的基准，包含 7⟦SLOT_1⟧ 条训练示例与 585 条测试示例，并支持自动评测。

**EN** • We leverage NL-to-program generation methods with refinement to produce high-quality slides, and benchmark diffusion models, VLMs, and LLMs.

**ZH** • 我们借助自然语言到程序的生成方法并结合精修来产出高质量幻灯片，并对扩散模型、VLM 与 LLM 作了基准评测。

**EN** • We train an 8B parameter open-source LLM, AutoPresent, that approaches the performance of GPT-4o, and design a programmatic tool library SlidesLib that facilitates slide program generation across models.

**ZH** • 我们训练了一个 80 亿参数的开源 LLM——AutoPresent，其性能接近 GPT-4o；并设计了一个程序化工具库 SlidesLib，以跨模型地便利幻灯片程序的生成。

<!-- [原子块 · img]  -->

**EN** Figure 2: Illustration of SlidesBench. Each example of SlidesBench consists of three instructions: Detailed Instructions with Images, Detailed Instructions Only, and High-Level Instructions. The model is tasked to generate a slide based on the instruction, and the generated slide is evaluated on the metrics suite, which contains both the reference-free metrics and the reference-based metrics.

**ZH** 图 2：SlidesBench 示意。SlidesBench 的每个示例包含三条指令：带图像的详细指令、仅详细指令与高层指令。模型需依据指令生成一张幻灯片，生成的幻灯片在指标套件上被评测，该套件同时包含无参考指标与基于参考的指标。

**EN** 2 SlidesBench

**ZH** 2 SlidesBench

**EN** In this section, we describe the creation of the SlidesBench benchmark. Each instance consists of a natural language instruction to create a slide, and the slide itself (in PPTX format) as a reference. SlidesBench includes three scenarios of varying difficulty levels designed to evaluate models with different user input. We describe the slide data collection (§2.1), three task setups (§2.2), and the annotation process (§2.3).

**ZH** 本节描述 SlidesBench 基准的创建过程。每个实例由一条用于创建幻灯片的自然语言指令，以及该幻灯片本身（PPTX 格式）作为参考所构成。SlidesBench 包含三种难度各异的场景，旨在以不同的用户输入来评测模型。我们分别介绍幻灯片数据采集（§2.1）、三种任务设定（§2.2）与标注流程（§2.3）。

**EN** 2.1 Slides Data Collection

**ZH** 2.1 幻灯片数据采集

**EN** We search the web and collect presentation slide decks from 10 domains, including art, marketing, environment, technology, etc. To select the highest-quality slide decks from each domain, we manually go through the relevant slide decks and conduct initial processing, by checking if all its slides (i) have visually structured layouts, and (ii) extractable media such as images (if any). For the slide decks with all slides satisfying (i) and (ii) in each domain, we incorporate one slide deck into the test set, and others into the training set. This results in a total of 10 and 300 slide decks (in PPTX format) for testing and training, each containing 20 slides on average. To respect the rights of the slide creators, we do not redistribute the slides. Instead, we provide a list of URLs for the slides that we used so that others can download the slides directly from the original website. We also provide an opt-out mechanism for any creator who does not want their slides in the dataset. We provide implementation details in §A.

**ZH** 我们检索网络，收集了艺术、营销、环境、科技等 10 个领域的演示幻灯片组。为从每个领域挑选出质量最高的幻灯片组，我们人工逐一检视相关幻灯片组并作初步处理，检查其全部幻灯片是否 (i) 具有视觉上结构化的布局，(ii) 含有可提取的图像等媒体（若有）。对每个领域中所有幻灯片都满足 (i) 与 (ii) 的幻灯片组，我们把其中一个纳入测试集，其余纳入训练集。由此共得到 10 个测试用与 300 个训练用幻灯片组（PPTX 格式），每组平均含 20 张幻灯片。为尊重幻灯片创作者的权益，我们不重新分发这些幻灯片，而是提供所用幻灯片的 URL 列表，使他人可直接从原始网站下载。我们也为任何不希望其幻灯片出现在数据集中的创作者提供了退出机制。实现细节见 §A。

**EN** 2.2 Three Task Setups

**ZH** 2.2 三种任务设定

**EN** We formulate the task as an NL-to-slide generation process. Given the reference slide, we curate three versions of natural language instructions, as shown in Figure 2, to represent slide generation tasks under varied difficulty levels. We introduce each setup below.

**ZH** 我们把该任务形式化为一个自然语言到幻灯片的生成过程。针对参考幻灯片，我们策管出三个版本的自然语言指令，如图 2 所示，用以代表不同难度级别下的幻灯片生成任务。下面逐一介绍每种设定。

**EN** Detailed Instructions with Images The first and easiest setting is to provide the models with all the necessary information and assets to produce the reference slide, including text and image content, formatting and layout specifications. This setting evaluates models’ visual planning abilities, such as arranging spatial layouts, maintaining formatting consistency, balancing content proportions, and emphasizing key elements.

**ZH** 带图像的详细指令 第一种、也是最简单的设定，是向模型提供复现参考幻灯片所需的全部信息与素材，包括文字与图像内容、格式与布局规格。该设定考察模型的视觉规划能力，例如安排空间布局、维持格式一致、平衡内容比例以及突出重点元素。

**EN** Detailed Instructions Only Since a user may not specify, or know exactly what images to put on a slide, we propose a detailed instruction only setting, where we provide the same natural language instruction provided in the detailed instruction with images setting, but replace the provided images with their natural language descriptions (e.g., “two people shaking hands”) generated by gpt-4o-mini. We then instruct the models to obtain the images using image searching or image generation tools. This setting further challenges models to interpret complex or compositional descriptions of images and obtain visuals that align with the slide context.

**ZH** 仅详细指令 由于用户可能不会指定、也不一定确切知道该在幻灯片上放哪些图像，我们提出了「仅详细指令」设定：给出与带图像详细指令设定中相同的自然语言指令，但把所提供的图像替换为由 gpt-4o-mini 生成的自然语言描述（例如“两个人握手”）。随后我们指示模型通过图像检索或图像生成工具来获取图像。该设定进一步考验模型对复杂或组合式图像描述的理解，以及获取与幻灯片语境相符的视觉素材的能力。

**EN** High-Level Instructions In contrast to users who have a concrete target slide in mind and can spell out all detailed instructions, some users may only be able to express their needs on a high level. We thus devise a high-level instruction setting, where the natural language instructions are rather high-level and only provide a general topical idea of the slide, such as “create a title slide for Airbnb,” instead of detailing what logos and text to add and where, as exemplified in Figure 2. Models in this case need to both acquire or create content, and arrange the elements properly.

**ZH** 高层指令 与那些心中已有明确目标幻灯片、并能把所有细节指令一一列出的用户不同，部分用户可能只能从较高层次表达自己的需求。因此我们设计了高层指令设定：自然语言指令相当概括，只给出幻灯片的大致主题，例如“为 Airbnb 制作一张标题页”，而不具体说明要添加哪些标志与文字、放在何处，如图 2 所示。在此情形下，模型既要获取或创作内容，也要妥善排布元素。

**EN** 2.3 Example Annotation

**ZH** 2.3 示例标注

**EN** To annotate the dataset, we collect natural language instructions paired with each slide. For each slide, we create three versions corresponding to the three setups in §2.2.

**ZH** 为标注数据集，我们采集与每张幻灯片配对的自然语言指令。对每张幻灯片，我们创建对应 §2.2 中三种设定的三个版本。

**EN** Detailed Instructions with Images To produce detailed instruction with images, we use a scalable approach combining human-written examples and model-generated annotations. For each slide deck, we first write instructions for three example slides manually — including all necessary information (content, layout, formatting) to reproduce the slide, and providing paths to the images used in the slide (e.g., media/image_0.png), as shown in Figure 2 (top). We then use these (human-written instruction, reference slide) pairs as few-shot examples to prompt LLM (specifically, gpt-4o-mini) to generate natural language instructions for each slide in the current slide deck.** * Including the three slides with human-written instructions, to ensure instructions for all slides are consistent in style and specificity. Further, for the test set, we manually examined and refined the instructions by correcting incorrect specifications, adding missing content, and removing unnecessary or untrue content.

**ZH** 带图像的详细指令 为产出带图像的详细指令，我们采用了一种结合人工撰写示例与模型生成标注的可扩展方法。对每个幻灯片组，我们先为三张示例幻灯片人工撰写指令——包含复现该幻灯片所需的全部信息（内容、布局、格式），并给出幻灯片中所用图像的路径（如 media/image_0.png），如图 2（上）所示。随后，我们把这些（人工撰写指令，参考幻灯片）对作为少样本示例，提示 LLM（具体为 gpt-4o-mini）为当前幻灯片组中的每张幻灯片生成自然语言指令。** * 包括人工撰写指令的那三张幻灯片，以确保所有幻灯片的指令在风格与具体程度上保持一致。此外，对测试集，我们人工审阅并精修了指令，纠正错误的规格说明、补充缺失内容、删除不必要或不实的内容。

**EN** Detailed Instructions Only To produce detailed instruction only, we replace the image paths (e.g., media/image_0.png) with the natural language descriptions of the images(‘‘an artistic, colorful background’’). These descriptions are generated by gpt-4o-mini. For the test set, we manually refine the instructions to ensure that they do not refer to unavailable image paths (e.g., removing phrases like “use the provided images”), as shown in Figure 2 (middle).

**ZH** 仅详细指令 为产出仅详细指令，我们把图像路径（如 media/image_0.png）替换为图像的自然语言描述（“一幅富有艺术感、色彩丰富的背景”）。这些描述由 gpt-4o-mini 生成。对测试集，我们人工精修指令，确保它们不再指向不可用的图像路径（例如删除“使用所提供的图像”之类的措辞），如图 2（中）所示。

**EN** High-Level Instructions To create high-level instructions, we start with a similar approach by manually annotating three examples and then prompting the model to generate for all slides. Human-written instructions only provide a topical description of the slide and intentionally leave out specific content or layout details. This process ensures that the generated instructions remain concise and general, as shown in Figure 2 (bottom).

**ZH** 高层指令 为创建高层指令，我们采用相近的做法：先人工标注三个示例，再提示模型为所有幻灯片生成指令。人工撰写的指令只给出幻灯片的主题性描述，有意略去具体内容或布局细节。该过程确保生成的指令保持简洁、概括，如图 2（下）所示。

**EN** Overall, the instructions have an average of 115.6, 118.3, and 26.6 words under detailed instruction with images, detailed instruction only, and high-level instructions settings respectively, accompanied by an average of 1.1, 0.0, and 0.0 provided images.

**ZH** 总体而言，在带图像的详细指令、仅详细指令与高层指令三种设定下，指令的平均词数分别为 115.6、118.3 与 26.6，伴随提供的图像平均数分别为 1.1、0.0 与 0.0。

**EN** 3 Evaluation Metrics

**ZH** 3 评测指标

**EN** In this section, we describe the evaluation metrics that we designed for SlidesBench. We propose two sets of evaluation metrics: reference-based metrics for measuring models’ instruction-following abilities (§3.1), and reference-free metrics to examine the design quality of model-generated content (§3.2). We also use executability to examine the success rate of each model (§3.3).

**ZH** 本节描述我们为 SlidesBench 设计的评测指标。我们提出两套评测指标：用于衡量模型指令遵循能力的基于参考的指标（§3.1），以及用于检验模型生成内容设计质量的无参考指标（§3.2）。我们还用可执行性来考察每个模型的成功率（§3.3）。

**EN** 3.1 Reference-Based Metrics

**ZH** 3.1 基于参考的指标

**EN** Inspired by Design2Code [38] metrics, we implement four dimensions to examine the similarity between the model-produced slides and the reference slide.

**ZH** 受 Design2Code [38] 指标的启发，我们实现了四个维度来检验模型产出的幻灯片与参考幻灯片之间的相似度。

**EN** Element matching For the slide layout, we measure the total sizes of matched elements (in generated and reference slides) divided by the total sizes of all element, where each textbox, image, or shape constitutes an element. More concretely, we accurately parse out each element in the generated and reference slides, and compute their maximum matching using the match library.

**ZH** 元素匹配 对于幻灯片布局，我们衡量（生成幻灯片与参考幻灯片中）匹配元素的总尺寸除以所有元素的总尺寸，其中每个文本框、图像或形状都构成一个元素。更具体地，我们准确解析出生成幻灯片与参考幻灯片中的每个元素，并用 match 库计算它们的最大匹配。

**EN** Content similarity For each pair of matched elements, we compute their content similarity. If the reference element is text, we calculate the textual similarity using the cosine similarity of the embeddings produced with sentence-transformer with the default all-MiniLM-L6-v2 model [29]. If the reference element is an image, we calculate the CLIP score [19] of the image in two elements. We report the average content similarity across all matched element pairs, if either element contains a non-empty text string or an image component.

**ZH** 内容相似度 对每一对匹配的元素，我们计算其内容相似度。若参考元素是文字，我们用 sentence-transformer 默认的 all-MiniLM-L6-v2 模型 [29] 所产生嵌入的余弦相似度来计算文本相似度；若参考元素是图像，我们计算两个元素中图像的 CLIP 分数 [19]。只要任一元素含有非空文本串或图像成分，我们就报告所有匹配元素对上的平均内容相似度。

**EN** Color similarity We also measure the coloring similarity using the CIEDE2000 color difference formula [26], to quantify the perceptual difference between the colors. For every matched element pair, we measure the text font color similarity and element background color (if any). We additionally measure the color similarity between the background color of generated and reference slides.

**ZH** 颜色相似度 我们还用 CIEDE2000 色差公式 [26] 衡量着色相似度，以量化颜色之间的感知差异。对每一对匹配元素，我们衡量文本字体颜色的相似度与元素背景颜色（若有）的相似度；此外还衡量生成幻灯片与参考幻灯片背景颜色之间的颜色相似度。

**EN** Position similarity In addition to content and formatting, we also calculate the positional similarity between each pair of matched elements. More concretely, we follow Si et al. [38] to normalize the element coordinates to ⟦SLOT_2⟧ by the slide page length and width. We compute the Manhattan distance between the elements and formulate positional similarity as ⟦SLOT_3⟧.

**ZH** 位置相似度 除内容与格式外，我们还计算每对匹配元素之间的位置相似度。更具体地，我们遵循 Si et al. [38] 的做法，用幻灯片的页面长与宽把元素坐标归一化到 ⟦SLOT_2⟧。我们计算元素之间的曼哈顿距离，并把位置相似度表述为 ⟦SLOT_3⟧。

**EN** Note that a low text, color, or position similarity score could come from differences in text, color, and positions, or derivative errors caused by the inaccurate element-matching process (e.g., it may match the title box in the generated slide to a content textbox in the reference slide, which has different content or coloring requirements).

**ZH** 需要注意的是，文本、颜色或位置相似度分数偏低，可能源自文本、颜色与位置本身的差异，也可能源自元素匹配过程不准确所引起的衍生误差（例如，它可能把生成幻灯片中的标题框匹配到参考幻灯片中的内容文本框，而后者在内容或配色上要求不同）。

**EN** 3.2 Reference-Free Metrics

**ZH** 3.2 无参考指标

**EN** A well-designed slide generated by models may look very different from the reference slide. Therefore, we also propose four reference-free evaluation metrics, to independently assess the design quality of model-generated slides. To establish the metrics, we surveyed a wide range of literature on slide design principles [9, 34, 5, 44, 39], and summarized four major points as below and detailed in Table 1:

**ZH** 模型生成的设计精良的幻灯片，可能与参考幻灯片看上去截然不同。因此我们还提出四项无参考评测指标，用以独立评估模型生成幻灯片的设计质量。为确立这些指标，我们调研了大量关于幻灯片设计原则的文献 [9, 34, 5, 44, 39]，并总结出如下四点（详见表 1）：

<!-- [原子块 · table] Metric Criteria Text The title should be simple and clear to indicate the main point. For main content, avoid too many texts and keep words concise. Use a consistent and readable font size, style, and -->

**EN** Table 1: Reference-free metrics, all evaluated in 0-5 scale.

**ZH** 表 1：无参考指标，均在 0–5 量表上评测。

**EN** Text Using concise texts is important for slides to engage with the audience. An ideal slide should have a clear title, concise main content, and readable formatting.

**ZH** 文字 使用简洁的文字对幻灯片吸引受众很重要。理想的幻灯片应具备清晰的标题、简洁的主要内容与易读的排版。

**EN** Image Using appropriate visuals can engage audiences. We hence measure if models can find high-quality images and properly use them to enhance the slide quality.

**ZH** 图像 使用恰当的视觉素材能够吸引受众。因此我们衡量模型能否找到高质量的图像，并妥善地用它们来提升幻灯片质量。

**EN** Layout Slide layout is crucial to create visual balance. We examine whether all elements are within the slide, have no overlap, and align properly with the relevant elements.

**ZH** 布局 幻灯片布局对营造视觉平衡至关重要。我们考察所有元素是否都在幻灯片之内、是否无重叠、是否与相关元素正确对齐。

**EN** Color Vivid and consistent color use in slides can help deliver insights. We check if the slide uses high-contrast colors to facilitate visibility, and avoid high-glaring colors to discourage user engagement.

**ZH** 配色 幻灯片中鲜明而一致的色彩运用有助于传达洞见。我们检查幻灯片是否使用高对比度色彩以提升可见性，并避免使用过于刺眼的颜色以免降低用户投入度。

**EN** Validation of Reference-Free Evaluation

**ZH** 无参考评测的验证

**EN** For all the metrics, we provide the image version of the slide and ask the gpt-4o model to produce a score between 0–5. To examine the reliability of this model-based evaluation, we conduct a human study and compare the intraclass correlation coefficient (ICC) between two human annotators and model evaluation, on all ground-truth slides. Our examination gives high ICC scores across all four metrics: ⟦SLOT_4⟧–⟦SLOT_5⟧, which are well within the range of what is typically considered ‘‘high agreement’’. In experiments in later sections, we scale these 0-5 scale scores to the 0--100 range to enable comparisons on this more standard scale. †† † We still evaluate with 0-5 scale to maintain a robust, human-aligned evaluation process.

**ZH** 对所有指标，我们提供幻灯片的图像版本，并请 gpt-4o 模型给出 0–5 之间的分数。为检验这种基于模型的评测的可靠性，我们开展了一项人工研究，在所有真值幻灯片上比较两名人工标注者与模型评测之间的组内相关系数（ICC）。我们的检视显示四项指标上 ICC 都很高：⟦SLOT_4⟧–⟦SLOT_5⟧，完全落在通常被认为“高度一致”的区间内。在后续章节的实验中，我们把这些 0–5 量表的分数换算到 0–100 区间，以便在更标准的尺度上作比较。†† † 我们仍以 0–5 量表进行评测，以维持稳健、与人类对齐的评测过程。

**EN** 3.3 Executability

**ZH** 3.3 可执行性

**EN** Particularly for methods based on code generation (§4.1), we additionally measure the execution success rate to account for invalid programs. Concretely, we count the percentage of successfully executing programs generated by models among all examples. We report reference-based and free scores for executable slides only, to fairly compare their design quality. But we report ‘Overall’ scores for all slides by assigning zeros to non-executing slides, to account for execution failures. We report all metrics for successfully executing and all slides in §E.

**ZH** 特别是对于基于代码生成的方法（§4.1），我们额外衡量执行成功率，以计入无效程序的情形。具体地，我们统计模型生成的程序中成功执行的程序在所有示例中所占的百分比。我们只对可执行的幻灯片报告基于参考的分数与无参考分数，以公平比较它们的设计质量；但在报告“总体”分数时，我们覆盖所有幻灯片，并对未成功执行的幻灯片赋零，以计入执行失败的情况。我们在 §E 中报告成功执行的幻灯片与所有幻灯片的全部指标。

**EN** 4 Method

**ZH** 4 方法

**EN** We introduce our main method — slide generation via code generation, optionally using our SlidesLib toolkit (§4.1). Then, we present AutoPresent, trained on 7⟦SLOT_6⟧ slides, that achieves performance on par with strong GPT model (§4.2).

**ZH** 我们介绍本文的主要方法——通过代码生成来生成幻灯片，可选地使用我们的 SlidesLib 工具包（§4.1）。随后介绍在 7⟦SLOT_6⟧ 张幻灯片上训练的 AutoPresent，其性能可与强大的 GPT 模型相当（§4.2）。

**EN** 4.1 Slides via NL-to-Code Generation

**ZH** 4.1 经由自然语言到代码生成的幻灯片

**EN** Generating Python Programs

**ZH** 生成 Python 程序

**EN** Given natural language instructions in §2, models are tasked with generating Python programs using publicly available libraries such as python-pptx. The model receives two (natural language instruction, Python program) pairs as in-context examples, followed by the test instruction, and generates a Python program which is then executed and will ideally yield a PPTX file containing the requested slide.

**ZH** 给定 §2 中的自然语言指令，模型的任务是生成使用 python-pptx 等公开可用库的 Python 程序。模型接收两对（自然语言指令，Python 程序）作为上下文示例，其后是测试指令，随后生成一个 Python 程序；该程序被执行，理想情况下产出一个包含所请求幻灯片的 PPTX 文件。

**EN** Generating Programs with SlidesLib

**ZH** 用 SlidesLib 生成程序

**EN** Nonetheless, the programs above could be very long and complex (170 lines on average), which could be challenging for models to generate entirely correctly, as shown in previous work [14]. To address this, we design SlidesLib, a library that provides easier-to-use interfaces for several common actions such as setting a title or setting background color. Using SlidesLib, the average program length is reduced to 13 lines, significantly easing the generation task. As shown in Table 2, SlidesLib includes 4 functions for basic operations and 3 functions for image search and generation, these functions allow models to produce more concise and modular programs. To enable the model to generate programs using SlidesLib, we follow the visual programming method [43] by providing a prompt that includes the documentation of the functions and two in-context examples. See more SlidesLib details in §B.

**ZH** 尽管如此，上述程序可能非常长且复杂（平均 170 行），如前人工作 [14] 所示，要让模型完全正确地生成它们颇具挑战。为此，我们设计了 SlidesLib——一个为若干常见操作（如设置标题或设置背景颜色）提供更易用接口的库。使用 SlidesLib 后，程序平均长度降至 13 行，显著降低了生成难度。如表 2 所示，SlidesLib 包含 4 个基础操作函数与 3 个图像检索与生成函数，这些函数使模型能生成更简洁、更模块化的程序。为使模型能用 SlidesLib 生成程序，我们遵循视觉编程方法 [43]，提供一个包含函数文档与两个上下文示例的提示。更多 SlidesLib 细节见 §B。

<!-- [原子块 · table] Function Description add_title Insert a title in the slide. add_text Insert text at a specific location. add_bullet_points Insert a textbox with bullet points. add_image Insert image at a specific loc -->

**EN** Table 2: Basic (top) and image-specific (bottom) functions provided by SlidesLib.

**ZH** 表 2：SlidesLib 提供的基础函数（上）与图像专用函数（下）。

<!-- [原子块 · table] Method Execution% Reference-Based Reference-Free Overall element content color position text image layout color Reference 100.0 – 59.7 81.5 73.5 65.7 – End-to-end Image Generation Stable-Diffusion* 10 -->

**EN** Table 3: Results with detailed instructions with images. We found that small models like LlaVa (7B) and LlaMa (8B) can barely generate any slides, while AutoPresent (8B) generates slides on par with GPT-4o. All the models still underperform humans.

**ZH** 表 3：带图像的详细指令下的结果。我们发现 LlaVa（7B）与 LlaMa（8B）等小模型几乎无法生成任何幻灯片，而 AutoPresent（8B）生成的幻灯片可与 GPT-4o 相当。所有模型仍不及人类。

**EN** 4.2 AutoPresent

**ZH** 4.2 AutoPresent

**EN** Using the slides in the training set of SlidesBench, we construct (natural language instruction, program) pairs to form training data to train an open-sourced 8B model, AutoPresent. This model is based on the LlaMa-3.1-8B-Instruct and trained using LoRA [21] with a rank of 128.

**ZH** 利用 SlidesBench 训练集中的幻灯片，我们构造（自然语言指令，程序）对以形成训练数据，用于训练一个开源的 8B 模型 AutoPresent。该模型基于 LlaMa-3.1-8B-Instruct，并以秩为 128 的 LoRA [21] 训练。

**EN** Training Data Construction

**ZH** 训练数据构建

**EN** To create (natural language instruction, program) training pairs, we generate two versions of canonical program solutions for each slide:

**ZH** 为创建（自然语言指令，程序）训练对，我们为每张幻灯片生成两个版本的规范程序解：

**EN** (i) Basic Python Programs We derive canonical programs (that is, programs that can be executed to reproduce the slide) without SlidesLib. To do this, we manually design an extraction script that (i) extracts each element (e.g., text and image) on the given slide, and (ii) produces a rule-based program that adds each element to the slide. After extracting and adding each element to the slide, the resulting program accurately reproduces the original slide.

**ZH** (i) 基础 Python 程序 我们导出不使用 SlidesLib 的规范程序（即执行后可复现该幻灯片的程序）。为此，我们人工设计了一个抽取脚本，它 (i) 抽取给定幻灯片上的每个元素（如文字与图像），(ii) 生成一个基于规则的程序，把每个元素添加到幻灯片上。在抽取并把每个元素添加到幻灯片之后，所得程序能准确复现原始幻灯片。

**EN** (ii) SlidesLib Python Programs We also generate canonical programs using SlidesLib, by transforming snippets from the programs above into SlidesLib function calls. To reproduce images in detailed instruction only and high-level instructions settings, we generate a short caption for each image and provide it to GPT-4o to generate the program for producing that image using search_image or generate_image functions. More details of this automatic program generation process are in §B.2.

**ZH** (ii) SlidesLib Python 程序 我们还用 SlidesLib 生成规范程序，做法是把上述程序中的代码片段转换为 SlidesLib 函数调用。为在仅详细指令与高层指令设定下复现图像，我们为每张图像生成一个简短描述，并提供给 GPT-4o，以生成用 search_image 或 generate_image 函数产出该图像的程序。该自动程序生成过程的更多细节见 §B.2。

**EN** Training Set Composition

**ZH** 训练集构成

**EN** After obtaining three instructions and two program versions for each example, we construct four versions of the training data, each with 7⟦SLOT_7⟧ examples:

**ZH** 在为每个示例获得三条指令与两个程序版本之后，我们构造了四个版本的训练数据，每个版本含 7⟦SLOT_7⟧ 条示例：

**EN** 1. (detailed instruction with images, python program)

**ZH** 1. （带图像的详细指令，python 程序）

**EN** 2. (detailed instruction with images, SlidesLib program)

**ZH** 2. （带图像的详细指令，SlidesLib 程序）

**EN** 3. (detailed instruction only, SlidesLib program)

**ZH** 3. （仅详细指令，SlidesLib 程序）

**EN** 4. (high-level instructions, SlidesLib program)

**ZH** 4. （高层指令，SlidesLib 程序）

**EN** These training sets allowed us to train four specialized models that address different challenges, which we report in Table 3 (1,2) and Table 4 (3,4).

**ZH** 这些训练集使我们得以训练四个专门应对不同挑战的模型，我们在表 3（1、2）与表 4（3、4）中报告其表现。

**EN** 4.3 Iterative Refinement

**ZH** 4.3 迭代精修

**EN** Slide generation is by nature an iterative process and often requires visual-based refinements after the first draft. To enable models to refine slides as humans do, we explore an iterative refinement procedure, where the model is tasked to self-refine the slide it generated. Specifically, in the setting using SlidesLib, we provide GPT-4o (capable of consuming slide images) with the original language instruction, the program it generated in the first pass, and a snapshot of the rendered slide; the model is then asked to generate a new program based on these information to refine the slide quality by tweaking colors, spacing, and other aspects of the slide. See the prompts of this process in §D.

**ZH** 幻灯片生成本质上是一个迭代过程，初稿之后往往还需要基于视觉的精修。为使模型能像人一样精修幻灯片，我们探索了一种迭代精修流程：让模型对自身生成的幻灯片作自我精修。具体在 SlidesLib 设定下，我们向 GPT-4o（能够接收幻灯片图像）提供原始语言指令、它在第一轮生成的程序，以及渲染出的幻灯片快照；然后请模型基于这些信息生成一个新程序，通过调整颜色、间距与幻灯片的其他方面来提升幻灯片质量。该过程的提示词见 §D。

**EN** 5 Experiments and Results

**ZH** 5 实验与结果

<!-- [原子块 · img]  -->

**EN** Figure 3: Examples of slides generated by different methods in three scenarios. End-to-end image generation methods fail to generate structured and clear slides. Small open-sourced models like LlaMa and LlaVa can barely generate any usable slides, while AutoPresent produces quality slides. Adding SlidesLib improves GPT-4o’s performance on detailed instruction only and high-level instruction tasks.

**ZH** 图 3：不同方法在三种场景下生成的幻灯片示例。端到端图像生成方法无法生成结构清晰、条理分明的幻灯片。LlaMa 与 LlaVa 等小型开源模型几乎无法生成任何可用的幻灯片，而 AutoPresent 能产出高质量的幻灯片。加入 SlidesLib 提升了 GPT-4o 在仅详细指令与高层指令任务上的表现。

**EN** We first introduce the experimental setup (§5.1), then present the results under various scenarios (§5.2).

**ZH** 我们首先介绍实验设置（§5.1），然后给出各场景下的结果（§5.2）。

**EN** 5.1 Experimental Setup

**ZH** 5.1 实验设置

**EN** Code Generation Approaches

**ZH** 代码生成方法

**EN** For code generation approaches, we sample ⟦SLOT_8⟧ responses and iteratively go through them, using the first successfully executing program as the final output of the model. If none of the ⟦SLOT_9⟧ responses execute successfully, we count it as an execution failure. In addition to AutoPresent (§4.2), we benchmark several LMs out-of-the-box, including open-weights Llama 3.1 (8B, Instruct), the code generation models DeepseekCoder-7B-v1.5 and CodeLlaMa-7B-Instruct, the vision-language LlaVa v1.5 model (with a Vicuna-7B-v1.5 LM backbone); and the proprietary GPT-4o model (the gpt-4o-2024-08-06 checkpoint).

**ZH** 对代码生成方法，我们采样 ⟦SLOT_8⟧ 个回答并依次检视，取第一个成功执行的程序作为模型的最终输出。若 ⟦SLOT_9⟧ 个回答中没有一个执行成功，我们将其计为一次执行失败。除 AutoPresent（§4.2）外，我们还对若干开箱即用的语言模型作基准评测，包括开放权重的 Llama 3.1（8B, Instruct）、代码生成模型 DeepseekCoder-7B-v1.5 与 CodeLlaMa-7B-Instruct、视觉语言模型 LlaVa v1.5（LM 骨干为 Vicuna-7B-v1.5）；以及专有的 GPT-4o 模型（gpt-4o-2024-08-06 检查点）。

**EN** End-to-End Image Generation

**ZH** 端到端图像生成

**EN** We compare code generation with end-to-end neural image generation methods, which are a common way to produce visuals. These methods are good at creating scenic or artistic images, but may be imprecise in content (esp. text) and do not support easy further modification by users. We benchmark Stable-Diffusion 2 [32] and DALL-E 3 [8] by asking them to output slides given the natural language instructions. We adjust our reference-based evaluation procedure by first segmenting slide images into elements using Tesseract OCR[40] and further parse out the texts of the elements, then applying the default calculation process as in §3. For the detailed instruction with images setting, we also report the results of the end-to-end image generation methods, marked with a “*” to indicate that they do not actually use the image inputs.

**ZH** 我们把代码生成与端到端神经图像生成方法作比较，后者是制作视觉内容的常见方式。这类方法擅长创作风景或艺术图像，但在内容（尤其是文字）上可能不够精确，且不支持用户便捷的后续修改。我们评测了 Stable-Diffusion 2 [32] 与 DALL-E 3 [8]，要求它们根据自然语言指令输出幻灯片。我们调整了基于参考的评测流程：先用 Tesseract OCR [40] 把幻灯片图像分割为元素并进一步解析出元素中的文字，再按 §3 的默认计算流程处理。对于带图像的详细指令设定，我们也报告端到端图像生成方法的结果，并加注“*”以表明它们实际上并未使用图像输入。

<!-- [原子块 · table] Method Detailed Instructions Only High-Level Instructions exec ref-based ref-free overall exec ref-based ref-free overall End-to-End Image Generation SD2 100.0 48.0 35.5 48.0 100.0 47.7 31.5 47.7 DALL -->

**EN** Table 4: Results under detailed instruction only and high-level instructions settings. We assign 100% execution success rates for all end-to-end image generation methods because they do not generate programs and would not suffer from execution errors.

**ZH** 表 4：仅详细指令与高层指令设定下的结果。我们为所有端到端图像生成方法赋予 100% 的执行成功率，因为它们不生成程序，不会遭遇执行错误。

**EN** 5.2 Quantitative Results and Analysis

**ZH** 5.2 定量结果与分析

**EN** Table 3 shows the result of detailed instruction with images scenario and Table 4 shows the result of detailed instruction only and high-level instructions scenarios.

**ZH** 表 3 给出带图像的详细指令场景下的结果，表 4 给出仅详细指令与高层指令场景下的结果。

**EN** In the top row of Table 3, we first measure the scores of the reference slides, which shows that the quality of the human-created slides is among the highest.

**ZH** 在表 3 的首行，我们首先衡量参考幻灯片的分数，结果表明人类制作的幻灯片质量位居最高之列。

**EN** Compared to the scores achieved by GPT-4o, smaller open-source models such as Llama 3.1 and LlaVa barely produce any working slides out of the box. Although the significant gaps of ⟦SLOT_10⟧–⟦SLOT_11⟧ points exist in the detailed instruction with images setting, this gap shrinks to ⟦SLOT_12⟧–⟦SLOT_13⟧ when no visuals are provided a priori, in detailed instruction only and high-level instructions scenarios (Table 4). This demonstrates significant challenges in obtaining images in slides. In contrast to the low performance of open-weight models out-of-the-box, AutoPresent’s performance approaches that of GPT-4o.

**ZH** 与 GPT-4o 取得的分数相比，Llama 3.1 与 LlaVa 等较小的开源模型开箱即用时几乎无法产出任何可用的幻灯片。尽管在带图像的详细指令设定下存在 ⟦SLOT_10⟧–⟦SLOT_11⟧ 分的显著差距，但当不预先提供视觉素材时（仅详细指令与高层指令场景，表 4），这一差距缩小到 ⟦SLOT_12⟧–⟦SLOT_13⟧。这说明在幻灯片中获取图像存在巨大挑战。与开放权重模型开箱即用的低表现形成对照的是，AutoPresent 的性能接近 GPT-4o。

**EN** End-to-End Image Generation When no visuals are provided, end-to-end image-generation methods perform worse than the best code-generation approaches in both the reference-based and reference-free metrics, especially in generating accurate content. These methods also often produce creative figures without aligning with the design principles of slides, indicating its poorer controllability.

**ZH** 端到端图像生成 当不提供视觉素材时，端到端图像生成方法在基于参考与无参考两类指标上都劣于最优的代码生成方法，尤其在生成准确内容方面。这些方法还常常产出富有创意却不符合幻灯片设计原则的图形，说明其可控性较差。

**EN** Effect of SlidesLib SlidesLib brings observable gains in LlaMa and LlaVa in all three scenarios by at most ⟦SLOT_14⟧ points; and similarly increases the strong GPT-4o performance across scenarios, especially when no images are provided. This suggests the benefits of generating more modular and concise programs for structured visual design.

**ZH** SlidesLib 的效应 SlidesLib 为 LlaMa 与 LlaVa 在三种场景下都带来了可见增益，最高达 ⟦SLOT_14⟧ 分；同样也提升了本就强大的 GPT-4o 在各场景下的表现，尤其是在未提供图像时。这说明为结构化视觉设计生成更模块化、更简洁的程序是有益的。

**EN** VLM vs. LLM When no helper functions are presented, the one VLM that we tested (LlaVa) outperforms its LLM counterpart LlaMa in all scenarios by ⟦SLOT_15⟧–⟦SLOT_16⟧ points. However, LlaVa shows limited ability in using functions presented in context, as demonstrated by the large margin the library-augmented LlaMa has over LlaVa (⟦SLOT_17⟧–⟦SLOT_18⟧). All LLMs (LlaMa, GPT-4o) perform worse when the instructions become less specified (detailed instruction with images ⟦SLOT_19⟧ detailed instruction only ⟦SLOT_20⟧ high-level instructions). Nonetheless, SlidesLib can greatly mitigate this degradation due to the loss of input specificity, and help models produce better outcomes across all three scenarios.

**ZH** VLM 与 LLM 对比 当不提供辅助函数时，我们所测试的唯一一个 VLM（LlaVa）在所有场景下都以 ⟦SLOT_15⟧–⟦SLOT_16⟧ 分优于其对应的 LLM——LlaMa。然而，LlaVa 在使用上下文中给出的函数方面能力有限，这从库增强后的 LlaMa 对 LlaVa 的大幅领先（⟦SLOT_17⟧–⟦SLOT_18⟧）中可见一斑。所有 LLM（LlaMa、GPT-4o）在指令变得不那么具体时表现更差（带图像的详细指令 ⟦SLOT_19⟧ 仅详细指令 ⟦SLOT_20⟧ 高层指令）。尽管如此，SlidesLib 能大幅缓解这种因输入具体性丧失而导致的性能下降，并帮助模型在三种场景下产出更好的结果。

**EN** 5.3 Qualitative Case Study

**ZH** 5.3 定性案例研究

**EN** We illustrate several models-produced slides in Figure 3. For end-to-end image generation methods, the design is more creative and often more attractive, but the text does not constitute meaningful words, or even the characters themselves are not valid.

**ZH** 我们在图 3 中展示了若干模型生成的幻灯片。对端到端图像生成方法而言，设计更有创意、往往也更美观，但其中的文字并不构成有意义的词，甚至连字符本身都无效。

**EN** On the other hand, code generation methods, especially weaker LlaMa and LlaVa models, suffer more from visual layout — elements often overlap with each other or exceed the canvas, making it challenging for the audience to obtain all information clearly.

**ZH** 另一方面，代码生成方法——尤其是较弱的 LlaMa 与 LlaVa 模型——在视觉布局上问题更多：元素之间常常相互重叠或超出画布，使观众难以清晰地获取全部信息。

**EN** In contrast, AutoPresent generates slides with appropriate layouts without undesirable element overlaps. In addition, they better follow the user instructions and are not overly creative like the image generation methods.

**ZH** 相比之下，AutoPresent 生成的幻灯片布局得当，没有不希望出现的元素重叠；此外，它们更好地遵循用户指令，也不像图像生成方法那样过度发挥创意。

**EN** 5.4 Perceptual Evaluation

**ZH** 5.4 感知评测

<!-- [原子块 · table] Model Pairs Detailed+Images Detailed Only t-stat p-val t-stat p-val (GPT-4o, LlaMa ) 13.206 0.000 8.630 0.000 ( AutoPresent , LlaMa ) 13.180 0.000 2.955 0.004 (GPT-4o, AutoPresent ) -0.445 0.657 8.203 -->

**EN** Table 5: Paired t-test results comparing model performance across detailed instruction only setting and detailed instruction with images setting. AutoPresent and GPT-4o outperforms LlaMa with a statistically significant difference in both settings.

**ZH** 表 5：比较各模型在仅详细指令设定与带图像的详细指令设定下表现的配对 t 检验结果。AutoPresent 与 GPT-4o 在两种设定下都以统计显著的优势优于 LlaMa。

**EN** We performed a qualitative evaluation on 10 randomly selected slides from each domain generated by GPT-4o, Llama-8B, and AutoPresent under the detailed instruction with images and detailed instruction only settings. We also add the ground-truth reference slide to evaluate the performance gap between current models and human slide creators. We shuffle these slides and ask the annotators to rank each slide from 1-5 based on how likely they would be to use the slide. For the detailed instruction with images setting, we collect 25 responses in total, and for detailed instruction only, we collect 16 responses in total. We provide more details of the evaluation process in §F.

**ZH** 我们对 GPT-4o、Llama-8B 与 AutoPresent 在带图像的详细指令与仅详细指令设定下、从每个领域随机选取的 10 张幻灯片作了质性评测。我们还加入了真值参考幻灯片，以评估当前模型与人类幻灯片创作者之间的性能差距。我们打乱这些幻灯片，请标注者按自己使用该幻灯片的可能性从 1 到 5 打分。对于带图像的详细指令设定，我们共收集 25 份回答；对于仅详细指令，共收集 16 份回答。评测流程的更多细节见 §F。

**EN** The result is shown in Figure 4. By performing the paired ⟦SLOT_21⟧-test, we found differences between the models pairs in terms of user preferences, as shown in Table 5: (1) In both settings, AutoPresent and GPT-4o perform statistically significantly better than LlaMa. (2) In detailed instruction with images setting, GPT-4o and AutoPresent has no significant differences (3) In the detailed instruction only setting, AutoPresent is slightly worse than gpt-4o, aligning with our quantitative evaluations in Table 4. All three models still have an overall performance gap compared with human-designed slides, indicating room for improvement on the slide generation task.

**ZH** 结果如图 4 所示。通过执行配对 ⟦SLOT_21⟧ 检验，我们发现了各模型对之间在用户偏好上的差异，如表 5 所示：(1) 在两种设定下，AutoPresent 与 GPT-4o 的表现都统计显著地优于 LlaMa。(2) 在带图像的详细指令设定下，GPT-4o 与 AutoPresent 之间没有显著差异。(3) 在仅详细指令设定下，AutoPresent 略逊于 gpt-4o，这与我们在表 4 中的定量评测一致。三个模型相比人类设计的幻灯片在总体上仍有性能差距，说明幻灯片生成任务还有改进空间。

<!-- [原子块 · object]  -->

**EN** Figure 4: Perceptual evaluation results on detailed instruction (1) with images and (2) only settings. We ask the users to score the quality of each slide from 1-5 and report the average score of each model. The user reported preference on GPT-4o and AutoPresent compared with LlaMa, while still having a gap with human-designed slides.

**ZH** 图 4：在 (1) 带图像的详细指令与 (2) 仅详细指令设定下的感知评测结果。我们请用户按 1–5 为每张幻灯片的质量打分，并报告每个模型的平均分。用户对 GPT-4o 与 AutoPresent 的偏好高于 LlaMa，但与人类设计的幻灯片之间仍有差距。

**EN** 5.5 Result after Iterative Refinement

**ZH** 5.5 迭代精修后的结果

<!-- [原子块 · table] Iteration Detailed + Images Detailed Only High-Level 0 58.0 56.3 58.5 1 59.5 59.5 59.8 2 59.3 60.1 61.3 3 60.1 59.4 61.4 -->

**EN** Table 6: Overall scores after applying multi-rounds of refinement in the three scenarios, demonstrating that refinement boosts performance in all three scenarios.

**ZH** 表 6：在三种场景下施加多轮精修后的总体分数，表明精修在三种场景下都提升了性能。

**EN** Finally, as shown by Table 6, we find that refinement improves model performance on all three challenges. By doing an ablation on the round of iterations, we find that while continued refinement often increases the scores, the first iteration usually gives the biggest performance improvement. We present representative cases after doing one round of refinement in Figure 5, which indicates that refinement can improve content layout and detailed controls on coloring and sizing.

**ZH** 最后，如表 6 所示，我们发现精修能提升模型在三项挑战上的表现。通过对迭代轮次作消融，我们发现：虽然持续精修常常能抬高分数，但第一轮迭代通常带来最大的性能提升。我们在图 5 中展示了作一轮精修后的代表性案例，表明精修能够改善内容布局以及对配色与尺寸的细致控制。

<!-- [原子块 · img]  -->

**EN** Figure 5: Auto-refinement results with GPT-4o, where the model further addresses some previously neglected instructions (marked in green), such as shape, background color, and text.

**ZH** 图 5：GPT-4o 的自动精修结果，模型进一步处理了一些此前被忽略的指令（以绿色标示），例如形状、背景颜色与文字。

**EN** 6 Related Work

**ZH** 6 相关工作

**EN** Language and Vision Model-Based Agents Agents based on large language models (LLMs) [2, 11] and vision-language models (VLMs) [4, 51] have been widely adopted in various tasks such as web navigation [52, 54, 24], software engineering [49, 50], and web development [27, 38]. Creation of presentation materials is another common task [10] that has both similarities and differences from these more widely examined tasks.

**ZH** 基于语言与视觉模型的智能体 基于大语言模型（LLM）[2, 11] 与视觉语言模型（VLM）[4, 51] 的智能体已被广泛应用于网页导航 [52, 54, 24]、软件工程 [49, 50]、网页开发 [27, 38] 等各类任务。演示材料的制作是另一项常见任务 [10]，它与这些被更广泛研究的任务既有相似之处，也有不同之处。

**EN** Generating Programs for Vision Tasks End-to-end image generation models such as diffusion [20, 32, 48] and GAN [15, 35] are widely used at producing scenic images, yet falling short on more structured visuals such as websites and slides [38]. Generating programs (i.e., image-editing actions) is a useful means to get structured visuals [18, 43, 41, 45, 14], including Tikz figures [6, 7], SVG [31, 37], posters [51], and user interfaces [38, 28]. However, they often require detailed inputs and are limited to specific, simple figure types, so they are still far from creating complex, editable presentation slides from scratch. Our work extends this line of research by formulating and benchmarking the natural-language-to-slide generation task.

**ZH** 为视觉任务生成程序 扩散 [20, 32, 48] 与 GAN [15, 35] 等端到端图像生成模型被广泛用于生成风景图像，但在网站与幻灯片等更结构化的视觉内容上表现不足 [38]。生成程序（即图像编辑动作）是获得结构化视觉内容的有效手段 [18, 43, 41, 45, 14]，涵盖 Tikz 图形 [6, 7]、SVG [31, 37]、海报 [51] 与用户界面 [38, 28]。然而，它们往往需要详细的输入，且局限于特定、简单的图形类型，因而离从零开始创建复杂、可编辑的演示幻灯片仍很遥远。我们的工作通过形式化并对自然语言到幻灯片的生成任务作基准评测，拓展了这一研究脉络。

**EN** Automatic Slide Generation Previous works on slide creation mostly focus on basic extraction from provided documents [23, 22, 36, 42, 12] or having models generate content given a topic [3, 47, 1] without addressing how to organize content visually. More recently, some benchmarks [17, 53] and methods [13] have emerged that follow detailed instructions for slide editing (e.g., adjust the font size of the title from 20 to 24) of an existing slide. In contrast, we synthesize more complex and structured programs that can generate slides from scratch, including content creation, visual arrangement, and fine-grained editing, instead of refining an existing slide.

**ZH** 自动幻灯片生成 以往关于幻灯片制作的工作，大多聚焦于从给定文档中作基础抽取 [23, 22, 36, 42, 12]，或让模型按给定主题生成内容 [3, 47, 1]，而未解决如何在视觉上组织内容的问题。更近期出现了一些基准 [17, 53] 与方法 [13]，它们遵循详细指令对已有幻灯片作编辑（例如把标题字号从 20 调整到 24）。相比之下，我们合成的是更复杂、更结构化的程序，能从零开始生成幻灯片，涵盖内容创作、视觉排布与细粒度编辑，而非对已有幻灯片作精修。

**EN** 7 Conclusion and Limitations

**ZH** 7 结论与局限性

**EN** In this work, we address the challenge of creating structured visuals from scratch. Specifically, we introduced SlidesBench, the first benchmark for automatic slide generation with evaluation metrics based on and free of reference slides. We benchmark multiple end-to-end image and program generation approaches, and demonstrate that AutoPresent with SlidesLib achieves comparable performance with the top GPT-4o model. Our further exploration in iterative refinement also reveals certain effectiveness in self-refinement. This work is an initial step towards automated generation of structured visuals. Specifically, it focuses on single-slide generation and produces full slide code in a single pass, without leveraging iterative design workflows. Future research could address these limitations by expanding to full slide decks, adopting gradual and interactive slide generation, and incorporating slide-specific features like animations. Further, integrating more design principles, such as optimizing for attention capture and information clarity, would be crucial for making generated slides more impactful and effective.

**ZH** 本文着力解决从零开始创建结构化视觉内容这一挑战。具体地，我们提出了 SlidesBench——首个面向自动幻灯片生成的基准，配有基于参考与不依赖参考的两类评测指标。我们对多种端到端图像生成与程序生成方法作了基准评测，并证明配有 SlidesLib 的 AutoPresent 取得了可与顶级 GPT-4o 模型相媲美的性能。我们进一步对迭代精修的探索也揭示了自我精修的一定有效性。本工作是迈向结构化视觉内容自动生成的第一步：具体地说，它聚焦于单页幻灯片的生成，并在单次过程内产出完整的幻灯片代码，没有利用迭代式的设计工作流。未来研究可通过扩展到完整的幻灯片组、采用渐进且交互式的幻灯片生成、并纳入动画等幻灯片特有功能来克服这些局限。此外，融入更多设计原则（例如针对注意力捕获与信息清晰度作优化），对于让生成的幻灯片更具影响力、更有效也至关重要。

**EN** Acknowledgment

**ZH** 致谢

**EN** We would like to thank Yutong Bai for helping us draft and providing feedback on the paper, David Chan for providing detailed suggestions on the introduction, and Frank Xu and Sean Welleck for discussions at the initial stage of this project. Junyi Zhang and Haven Feng for feedback on the project.

**ZH** 我们感谢 Yutong Bai 协助起草论文并提供反馈，感谢 David Chan 对引言提出细致建议，感谢 Frank Xu 与 Sean Welleck 在项目初期的讨论，以及 Junyi Zhang 与 Haven Feng 对项目的反馈。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] [1] Gamma - ai-powered document creation and storytelling platform. Accessed: 2024-11-14. -->

<!-- [原子块 · verbatim] [2] Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. Gpt-4 technical report. arXiv p -->

<!-- [原子块 · verbatim] [3] Shaikh Mostafa Al Masum, Mitsuru Ishizuka, and Md Tawhidul Islam. ’auto-presentation’: a multi-agent system for building automatic multi-modal presentation of a topic from world wide web informati -->

<!-- [原子块 · verbatim] [4] Jean-Baptiste Alayrac, Jeff Donahue, Pauline Luc, Antoine Miech, Iain Barr, Yana Hasson, Karel Lenc, Arthur Mensch, Katherine Millican, Malcolm Reynolds, et al. Flamingo: a visual language model f -->

<!-- [原子块 · verbatim] [5] Angie Arriesgado. 45 tips to speed up your powerpoint design workflow, 2019. -->

<!-- [原子块 · verbatim] [6] Jonas Belouadi, Anne Lauscher, and Steffen Eger. Automatikz: Text-guided synthesis of scientific vector graphics with tikz. ArXiv , abs/2310.00367, 2023. -->

<!-- [原子块 · verbatim] [7] Jonas Belouadi, Simone Paolo Ponzetto, and Steffen Eger. Detikzify: Synthesizing graphics programs for scientific figures and sketches with tikz. arXiv preprint arXiv:2405.15306 , 2024. -->

<!-- [原子块 · verbatim] [8] James Betker, Gabriel Goh, Li Jing, Tim Brooks, Jianfeng Wang, Linjie Li, Long Ouyang, Juntang Zhuang, Joyce Lee, Yufei Guo, et al. Improving image generation with better captions. Computer Scienc -->

<!-- [原子块 · verbatim] [9] The LinkedIn community. How do you use design principles and best practices to evaluate and improve your slide layout and formatting?, 2024. -->

<!-- [原子块 · verbatim] [10] decktopus. Top presentation statistics for 2021, 2021. -->

<!-- [原子块 · verbatim] [11] Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Amy Yang, Angela Fan, et al. The llama 3 herd of models. arXiv prepri -->

<!-- [原子块 · verbatim] [12] Tsu-Jui Fu, William Yang Wang, Daniel McDuff, and Yale Song. Doc2ppt: Automatic presentation slides generation from scientific documents. In Proceedings of the AAAI Conference on Artificial Intel -->

<!-- [原子块 · verbatim] [13] Apurva Gandhi, Thong Q Nguyen, Huitian Jiao, Robert Steen, and Ameya Bhatawdekar. Natural language commanding via program synthesis. arXiv preprint arXiv:2306.03460 , 2023. -->

<!-- [原子块 · verbatim] [14] Jiaxin Ge, Sanjay Subramanian, Baifeng Shi, Roei Herzig, and Trevor Darrell. Recursive visual programming. In European Conference on Computer Vision , pages 1–18. Springer, 2025. -->

<!-- [原子块 · verbatim] [15] Ian Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville, and Yoshua Bengio. Generative adversarial nets. Advances in neural information proces -->

<!-- [原子块 · verbatim] [16] Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, YK Li, et al. Deepseek-coder: When the large language model meets programming–the rise of code -->

<!-- [原子块 · verbatim] [17] Yiduo Guo, Zekai Zhang, Yaobo Liang, Dongyan Zhao, and Nan Duan. Pptc benchmark: Evaluating large language models for powerpoint task completion. arXiv preprint arXiv:2311.01767 , 2023. -->

<!-- [原子块 · verbatim] [18] Tanmay Gupta and Aniruddha Kembhavi. Visual programming: Compositional visual reasoning without training. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition , pa -->

<!-- [原子块 · verbatim] [19] Jack Hessel, Ari Holtzman, Maxwell Forbes, Ronan Le Bras, and Yejin Choi. CLIPScore: A reference-free evaluation metric for image captioning. In Proceedings of the 2021 Conference on Empirical Me -->

<!-- [原子块 · verbatim] [20] Jonathan Ho, Ajay Jain, and Pieter Abbeel. Denoising diffusion probabilistic models. Advances in neural information processing systems , 33:6840–6851, 2020. -->

<!-- [原子块 · verbatim] [21] Edward J Hu, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, Weizhu Chen, et al. Lora: Low-rank adaptation of large language models. In International Conference on Learning Rep -->

<!-- [原子块 · verbatim] [22] Yue Hu and Xiaojun Wan. Ppsgen: Learning-based presentation slides generation for academic papers. IEEE transactions on knowledge and data engineering , 27(4):1085–1097, 2014. -->

<!-- [原子块 · verbatim] [23] Min-Yen Kan. Slideseer: A digital library of aligned document and presentation pairs. In Proceedings of the 7th ACM/IEEE-CS joint conference on Digital libraries , pages 81–90, 2007. -->

<!-- [原子块 · verbatim] [24] Jing Yu Koh, Robert Lo, Lawrence Jang, Vikram Duvvur, Ming Lim, Po-Yu Huang, Graham Neubig, Shuyan Zhou, Russ Salakhutdinov, and Daniel Fried. VisualWebArena: Evaluating multimodal agents on real -->

<!-- [原子块 · verbatim] [25] Wenyuan Kong, Zhaoyun Jiang, Shizhao Sun, Zhuoning Guo, Weiwei Cui, Ting Liu, Jianguang Lou, and Dongmei Zhang. Aesthetics++: Refining graphic designs by exploring design principles and human pre -->

<!-- [原子块 · verbatim] [26] M Ronnier Luo, Guihua Cui, and Bryan Rigg. The development of the cie 2000 colour-difference formula: Ciede2000. Color Research & Application: Endorsed by Inter-Society Color Council, The Colour  -->

<!-- [原子块 · verbatim] [27] Reiichiro Nakano, Jacob Hilton, Suchir Balaji, Jeff Wu, Long Ouyang, Christina Kim, Christopher Hesse, Shantanu Jain, Vineet Kosaraju, William Saunders, et al. Webgpt: Browser-assisted question-a -->

<!-- [原子块 · verbatim] [28] Yi-Hao Peng, Faria Huq, Yue Jiang, Jason Wu, Xin Yue Li, Jeffrey P Bigham, and Amy Pavel. Dreamstruct: Understanding slides and user interfaces via synthetic data generation. In European Conferen -->

<!-- [原子块 · verbatim] [29] Nils Reimers and Iryna Gurevych. Sentence-bert: Sentence embeddings using siamese bert-networks. In Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing . Associ -->

<!-- [原子块 · verbatim] [30] Garr Reynolds. Presentation Zen: Simple ideas on presentation design and delivery . New Riders, 2011. -->

<!-- [原子块 · verbatim] [31] Juan A Rodriguez, Shubham Agarwal, Issam H Laradji, Pau Rodriguez, David Vazquez, Christopher Pal, and Marco Pedersoli. Starvector: Generating scalable vector graphics code from images. arXiv pre -->

<!-- [原子块 · verbatim] [32] Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, and Björn Ommer. High-resolution image synthesis with latent diffusion models. In Proceedings of the IEEE/CVF conference on comput -->

<!-- [原子块 · verbatim] [33] Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, Sten Sootla, Itai Gat, Xiaoqing Ellen Tan, Yossi Adi, Jingyu Liu, Romain Sauvestre, Tal Remez, et al. Code llama: Open foundation models for code -->

<!-- [原子块 · verbatim] [34] Hitesh Sahni. Presentation design: A step-by-step guide, 2024. -->

<!-- [原子块 · verbatim] [35] Axel Sauer, Tero Karras, Samuli Laine, Andreas Geiger, and Timo Aila. Stylegan-t: Unlocking the power of gans for fast large-scale text-to-image synthesis. In International conference on machine  -->

<!-- [原子块 · verbatim] [36] Athar Sefid and Jian Wu. Automatic slide generation for scientific papers. In Third International Workshop on Capturing Scientific Knowledge co-located with the 10th International Conference on K -->

<!-- [原子块 · verbatim] [37] Pratyusha Sharma, Tamar Rott Shaham, Manel Baradad, Stephanie Fu, Adrian Rodriguez-Munoz, Shivam Duggal, Phillip Isola, and Antonio Torralba. A vision check-up for language models. In Proceedings -->

<!-- [原子块 · verbatim] [38] Chenglei Si, Yanzhe Zhang, Zhengyuan Yang, Ruibo Liu, and Diyi Yang. Design2code: How far are we from automating front-end engineering? arXiv preprint arXiv:2403.03163 , 2024. -->

<!-- [原子块 · verbatim] [39] Think Outside The Slide. Latest annoying powerpoint survey results, 2019. -->

<!-- [原子块 · verbatim] [40] Ray Smith. An overview of the tesseract ocr engine. In Ninth international conference on document analysis and recognition (ICDAR 2007) , pages 629–633. IEEE, 2007. -->

<!-- [原子块 · verbatim] [41] Sanjay Subramanian, Medhini Narasimhan, Kushal Khangaonkar, Kevin Yang, Arsha Nagrani, Cordelia Schmid, Andy Zeng, Trevor Darrell, and Dan Klein. Modular visual question answering via code genera -->

<!-- [原子块 · verbatim] [42] Edward Sun, Yufang Hou, Dakuo Wang, Yunfeng Zhang, and Nancy XR Wang. D2s: Document-to-slide generation via query-based text summarization. arXiv preprint arXiv:2105.03664 , 2021. -->

<!-- [原子块 · verbatim] [43] Dídac Surís, Sachit Menon, and Carl Vondrick. Vipergpt: Visual inference via python execution for reasoning. In Proceedings of the IEEE/CVF International Conference on Computer Vision , pages 118 -->

<!-- [原子块 · verbatim] [44] Utrecht University. Four principles for making a good powerpoint presentation, 2024. -->

<!-- [原子块 · verbatim] [45] Zhiruo Wang, Graham Neubig, and Daniel Fried. TroVE: Inducing verifiable and efficient toolboxes for solving programmatic tasks. In Forty-first International Conference on Machine Learning , 2024 -->

<!-- [原子块 · verbatim] [46] Zora Zhiruo Wang, Jiayuan Mao, Daniel Fried, and Graham Neubig. Agent workflow memory. arXiv preprint arXiv:2409.07429 , 2024b. -->

<!-- [原子块 · verbatim] [47] Thomas Winters and Kory W Mathewson. Automatically generating engaging presentation slide decks. In International Conference on Computational Intelligence in Music, Sound, Art and Design (Part of -->

<!-- [原子块 · verbatim] [48] Ximing Xing, Haitao Zhou, Chuang Wang, Jing Zhang, Dong Xu, and Qian Yu. Svgdreamer: Text guided svg generation with diffusion model. In Proceedings of the IEEE/CVF Conference on Computer Vision  -->

<!-- [原子块 · verbatim] [49] John Yang, Carlos E Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, and Ofir Press. Swe-agent: Agent-computer interfaces enable automated software engineering. arXiv pre -->

<!-- [原子块 · verbatim] [50] John Yang, Carlos E Jimenez, Alex L Zhang, Kilian Lieret, Joyce Yang, Xindi Wu, Ori Press, Niklas Muennighoff, Gabriel Synnaeve, Karthik R Narasimhan, et al. Swe-bench multimodal: Do ai systems g -->

<!-- [原子块 · verbatim] [51] Tao Yang, Yingmin Luo, Zhongang Qi, Yang Wu, Ying Shan, and Chang Wen Chen. Posterllava: Constructing a unified multi-modal layout generator with llm. arXiv preprint arXiv:2406.02884 , 2024c. -->

<!-- [原子块 · verbatim] [52] Shunyu Yao, Howard Chen, John Yang, and Karthik Narasimhan. Webshop: Towards scalable real-world web interaction with grounded language agents. In Advances in Neural Information Processing System -->

<!-- [原子块 · verbatim] [53] Zekai Zhang, Yiduo Guo, Yaobo Liang, Dongyan Zhao, and Nan Duan. Pptc-r benchmark: Towards evaluating the robustness of large language models for powerpoint task completion. arXiv preprint arXiv: -->

<!-- [原子块 · verbatim] [54] Shuyan Zhou, Frank F. Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Tianyue Ou, Yonatan Bisk, Daniel Fried, Uri Alon, and Graham Neubig. Webarena: A realistic web environment -->

**EN** Appendix A SlidesBench Details

**ZH** 附录 A SlidesBench 细节

**EN** A.1 Slide Deck Domains

**ZH** A.1 幻灯片组领域

**EN** The 10 domains we cover in SlidesBench include:

**ZH** SlidesBench 涵盖的 10 个领域包括：

**EN** 1. Art Photos

**ZH** 1. 艺术摄影

**EN** 2. Business

**ZH** 2. 商业

**EN** 3. Career

**ZH** 3. 职业

**EN** 4. Design

**ZH** 4. 设计

**EN** 5. Entrepreneur

**ZH** 5. 创业

**EN** 6. Environment

**ZH** 6. 环境

**EN** 7. Food

**ZH** 7. 美食

**EN** 8. Marketing

**ZH** 8. 营销

**EN** 9. Social Media

**ZH** 9. 社交媒体

**EN** 10. Technology

**ZH** 10. 科技

**EN** A.2 Slide Deck Source

**ZH** A.2 幻灯片组来源

**EN** There existis large amount of slide decks on the internet including Google Search, Bing Search etc. For convenience, we collect a list of slides from the slideshare.com website.

**ZH** 互联网上存在大量幻灯片组，包括 Google 搜索、Bing 搜索等。为方便起见，我们从 slideshare.com 网站收集了一份幻灯片列表。

**EN** A.3 Slide Deck Statistics Per Domain

**ZH** A.3 各领域的幻灯片组统计

**EN** The average images per domain and average text blocks per domain are shown in Figure 6.

**ZH** 每个领域的平均图像数与平均文本块数如图 6 所示。

<!-- [原子块 · img]  -->

**EN** Figure 6: SlidesBench statistics on different domains.

**ZH** 图 6：SlidesBench 在各领域上的统计。

**EN** Appendix B SlidesLib Details

**ZH** 附录 B SlidesLib 细节

**EN** In this section, we provide the detailed documentation and examples for all functions in our SlidesLib.

**ZH** 本节提供 SlidesLib 中所有函数的详细文档与示例。

**EN** B.1 SlidesLib Implementation

**ZH** B.1 SlidesLib 实现

**EN** Figure 7 shows the basic functions and Figure 8 shows the image-oriented functions.

**ZH** 图 7 展示基础函数，图 8 展示面向图像的函数。

**EN** Figure 7: Documentation for the basic functions in our SlidesLib.

**ZH** 图 7：SlidesLib 基础函数的文档。

**EN** Figure 8: Documentation for the image-oriented functions in our SlidesLib.

**ZH** 图 8：SlidesLib 面向图像函数的文档。

**EN** B.2 SlidesLib Usage Example

**ZH** B.2 SlidesLib 使用示例

**EN** Figure 9shows two example programs using multiple SlidesLib functions to produce slides.

**ZH** 图 9 展示了两个使用多个 SlidesLib 函数生成幻灯片的示例程序。

**EN** Figure 9: Example programs to produce slides using SlidesLib.

**ZH** 图 9：使用 SlidesLib 生成幻灯片的示例程序。

<!-- [原子块 · object]  -->

**EN** Figure 10: The percentage of each action taken by different models.

**ZH** 图 10：不同模型采取各类动作的百分比。

**EN** B.3 SlidesLib Usage Percentage

**ZH** B.3 SlidesLib 使用占比

**EN** The percentage of each action taken by GPT-4o, AutoPresent, and Llama-3.1 in all 3 scenarios are reported in Figure 10. On average, the most common actions are add_text (36.3%), add_image (20.3%), and add_title (13.5%).

**ZH** 图 10 报告了 GPT-4o、AutoPresent 与 Llama-3.1 在全部 3 种场景下采取各类动作的百分比。平均而言，最常见的动作是 add_text（36.3%）、add_image（20.3%）与 add_title（13.5%）。

**EN** Appendix C Training Details for AutoPresent

**ZH** 附录 C AutoPresent 的训练细节

**EN** The training parameters for AutoPresent are summarized in Table 7.

**ZH** AutoPresent 的训练参数汇总于表 7。

<!-- [原子块 · table] Parameter Value LoRA Parameters LoRA rank 128 LoRA alpha 32 LoRA dropout 0 Random state 3407 RS-LoRA Disabled LoFT-Q config None Trainer Parameters Batch size (per device) 1 Gradient accumulation step -->

**EN** Table 7: Training details for AutoPresent. LoRA and Trainer parameters are described in detail.

**ZH** 表 7：AutoPresent 的训练细节。详细描述 LoRA 与 Trainer 参数。

**EN** Appendix D Refinement Details

**ZH** 附录 D 精修细节

**EN** We provide the prompts that we used for auto-refinement in Figure 11. We input the instruction and the in-context examples, the previous code generated by the model, and the snapshot of the slide generated by executing this code to the model and let it correct the code.

**ZH** 我们在图 11 中给出用于自动精修的提示词。我们把指令与上下文示例、模型此前生成的代码，以及执行该代码所生成幻灯片的快照一并输入模型，让它修正代码。

**EN** Figure 11: Prompt we used for Auto-Refinement. The model receives the APIs and instruction, the previous generated slide and code, and is tasked to re-write the code to do slide refinement.

**ZH** 图 11：我们用于自动精修的提示词。模型接收 API 与指令、此前生成的幻灯片与代码，并被要求重写代码以完成幻灯片精修。

**EN** Appendix E Detailed Results

**ZH** 附录 E 详细结果

**EN** We report two sets of evaluation metrics (reference-based and reference-free) in both their average value on all slides (i.e., un-weighted by execution success) and on successfully rendered slides (i.e., weighted by execution success).

**ZH** 我们报告两套评测指标（基于参考与无参考），分别给出它们在所有幻灯片上的平均值（即未按执行成功率加权）与在成功渲染的幻灯片上的平均值（即按执行成功率加权）。

**EN** E.1 Detailed Instructions with Images

**ZH** E.1 带图像的详细指令

**EN** Table 8shows all metrics down-weighted by the execution success rate; Table 9 shows reference-based and reference-free metrics without down-weighting by execution success.

**ZH** 表 8 给出按执行成功率作降权后的全部指标；表 9 给出未按执行成功率降权的基于参考与无参考指标。

<!-- [原子块 · table] Method Execution% Reference-Based Reference-Free Average block text color position text image layout color Human 100.0 - 59.7 81.5 73.5 65.7 - Code Generation w/o Library LLaVA (7B) 11.3 7.0 11.0 0.7  -->

**EN** Table 8: Slide generation results (weighted by execution success) under the detailed instructions with images scenario.

**ZH** 表 8：带图像的详细指令场景下（按执行成功率加权）的幻灯片生成结果。

<!-- [原子块 · table] Method Execution% Reference-Based Reference-Free Avg block text color pos text img layout color Human 100.0 - 59.7 81.5 73.5 65.7 - Code Generation w/o Library LLaVA (7B) 11.3 61.9 97.3 6.2 70.8 41.6  -->

**EN** Table 9: Slide generation results (un-weighted by execution success) under the detailed instructions with images scenario.

**ZH** 表 9：带图像的详细指令场景下（未按执行成功率加权）的幻灯片生成结果。

**EN** E.2 Detailed Instructions Only

**ZH** E.2 仅详细指令

**EN** Table 10 shows all metrics down-weighted by the execution success rate; Table 11 shows reference-based and reference-free metrics without down-weighting by execution success.

**ZH** 表 10 给出按执行成功率作降权后的全部指标；表 11 给出未按执行成功率降权的基于参考与无参考指标。

<!-- [原子块 · table] Method Execution% Reference-Based Reference-Free Average block text color position text image layout color End-to-End Image Generation Stable-Diffusion 100.0 74.5 33.4 9.0 75.0 19.6 45.1 36.9 40.5 48. -->

**EN** Table 10: Results (weighted by execution success) under detailed instructions only scenario.

**ZH** 表 10：仅详细指令场景下（按执行成功率加权）的结果。

<!-- [原子块 · table] Method Execution% Reference-Based Reference-Free Overall block text color position text image layout color End-to-End Image Generation Stable-Diffusion 100.0 74.5 33.4 9.0 75.0 19.6 45.1 36.9 40.5 48. -->

**EN** Table 11: Results (un-weighted by execution success) under detailed instructions only scenario.

**ZH** 表 11：仅详细指令场景下（未按执行成功率加权）的结果。

**EN** E.3 High-Level Instructions Challenge

**ZH** E.3 高层指令挑战

**EN** Table 12 shows all metrics down-weighted by the execution success rate; Table 13 shows reference-based and reference-free metrics without down-weighting by execution success.

**ZH** 表 12 给出按执行成功率作降权后的全部指标；表 13 给出未按执行成功率降权的基于参考与无参考指标。

<!-- [原子块 · table] Method Execution% Reference-Based Reference-Free Average block text color position text image layout color End-to-End Image Generation Stable-Diffusion 100.0 72.0 33.2 8.3 77.2 3.3 49.3 35.6 37.8 47.7 -->

**EN** Table 12: Results (weighted by execution success) under high-level instructions scenario.

**ZH** 表 12：高层指令场景下（按执行成功率加权）的结果。

<!-- [原子块 · table] Method Execution% Reference-Based Reference-Free Average block text color position text image layout color End-to-End Image Generation Stable-Diffusion 100.0 72.0 33.2 8.3 77.2 3.3 49.3 35.6 37.8 47.7 -->

**EN** Table 13: Results (un-weighted by execution success) under high-level instructions scenario.

**ZH** 表 13：高层指令场景下（未按执行成功率加权）的结果。

**EN** Appendix F Perceptual Analysis

**ZH** 附录 F 感知分析

**EN** In this section, we provide perceptual analysis details. We build a google doc and ask the user to score each slide from 1-5 (1 is the worst and 5 is the best), as shown in Figure 12.

**ZH** 本节提供感知分析的细节。我们建立了一份 google doc，并请用户按 1–5 为每张幻灯片打分（1 为最差，5 为最好），如图 12 所示。

**EN** Figure 12: Instruction we used for the perceptual evaluation.

**ZH** 图 12：我们用于感知评测的指令。

<!-- [原子块 · img]  -->

**EN** Figure 13: An example of the perceptual analysis question. We ask the human to score the quality of the slide from 1-5.

**ZH** 图 13：感知分析问题的一个示例。我们请人类按 1–5 为幻灯片的质量打分。

**EN** An example of the question is shown in Figure 13.

**ZH** 问题示例如图 13 所示。
