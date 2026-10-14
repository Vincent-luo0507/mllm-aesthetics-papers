# IDEA-Bench：生成模型距离专业设计还有多远？

> 原标题：IDEA-Bench: How Far are Generative Models from Professional Designing?
> 作者：Chen Liang, Lianghua Huang, Jingwu Fang, Huanzhang Dou, Wei Wang, Zhi-Fan Wu, Yupeng Shi, Junge Zhang, Xin Zhao, Yu Liu · arXiv:2412.11767 · 2024-12-16

<!-- [原子块 · verbatim] IDEA-Bench: How Far are Generative Models from Professional Designing? -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] Real-world design tasks—such as picture book creation, film storyboard development using character sets, photo retouching, visual effects, and font transfer—are highly diverse and complex, requiring d -->

<!-- [原子块 · table]  -->

**EN** 1 Introduction

**ZH** 1 引言

<!-- [原子块 · img]  -->

**EN** Figure 1: Overview of IDEA-Bench. IDEA-Bench comprises 5 categories, encompassing a total of 100 professional-level subtasks, 275 cases, and 1,650 hierarchical evaluation questions. Each category provides subtask examples, quantitative statistics, and showcases a leaderboard of mainstream models.

**ZH** 图 1：IDEA-Bench 概览。IDEA-Bench 包含 5 个类别，涵盖共 100 个专业级子任务、275 个用例与 1,650 道层级化评估问题。每个类别提供子任务示例、量化统计，并展示主流模型的排行榜。

<!-- [原子块 · img]  -->

**EN** Figure 2: Demonstration of task definitions in IDEA-Bench. IDEA-Bench encompasses a diverse range of professional image design tasks. Input formats include plain text, single-image input, and multi-image input, while output formats span both single-image and multi-image generation.

**ZH** 图 2：IDEA-Bench 中任务定义的展示。IDEA-Bench 涵盖多种多样的专业图像设计任务。输入形式包括纯文本、单图输入与多图输入，输出形式则涵盖单图生成与多图生成。

**EN** Recent advancements in Text-to-Image (T2I) models (Ramesh et al., 2021; Ramesh et al., 2022; Esser et al., 2021; Rombach et al., 2022; Saharia et al., 2022; Betker et al., 2023; Podell et al., 2023; Esser et al., 2024a; Baldridge et al., 2024; Chen et al., 2023; Labs, 2024a) have significantly enhanced the ability to generate high-quality images from textual descriptions. Building on these successes, models such as ControlNet (Zhang et al., 2023a) and T2I-Adapter (Mou et al., 2024) integrate additional networks into text-to-image diffusion frameworks to incorporate visual conditioning. Similarly, InstructPix2Pix (Brooks et al., 2023) and Emu-Edit (Sheynin et al., 2024) are specifically trained on datasets tailored for complex image editing tasks. Despite the widespread popularity of models like DALL-E 3 (Ramesh et al., 2022) and FLUX-1 (Labs, 2024a), which attract millions of visits daily, professional users often rely on established workflows and specialized software for image creation. This reliance highlights a substantial gap between the capabilities of current image generation models and the demanding requirements of professional-grade image design. When most existing image generation models focus on academic task research, the rapid evolution of large language models (LLMs) (Radford et al., 2019; Raffel et al., 2020; Brown, 2020; Ouyang et al., 2022; Zhang et al., 2022; Touvron et al., 2023a; Touvron et al., 2023b; Dubey et al., 2024) and multimodal language models (MLLMs) (Li et al., 2024; Wang et al., 2024a; OpenAI, 2024; Team et al., 2023) indicate that future image generation models will increasingly aim to achieve both professional-grade quality and task unification, enabling them to handle a diverse range of complex applications seamlessly.

**ZH** 文本到图像（T2I）模型（Ramesh 等，2021；Ramesh 等，2022；Esser 等，2021；Rombach 等，2022；Saharia 等，2022；Betker 等，2023；Podell 等，2023；Esser 等，2024a；Baldridge 等，2024；Chen 等，2023；Labs，2024a）的最新进展显著提升了依据文本描述生成高质量图像的能力。在这些成果之上，ControlNet（Zhang 等，2023a）与 T2I-Adapter（Mou 等，2024）等模型把附加网络集成进文本到图像扩散框架，以引入视觉条件控制。类似地，InstructPix2Pix（Brooks 等，2023）与 Emu-Edit（Sheynin 等，2024）专为复杂图像编辑任务而在定制的数据集上训练。尽管 DALL-E 3（Ramesh 等，2022）与 FLUX-1（Labs，2024a）等模型广受欢迎、每日吸引数百万次访问，专业用户仍常依赖既有工作流与专用软件来创作图像。这种依赖凸显出当前图像生成模型的能力与专业级图像设计的严苛要求之间存在巨大落差。当多数现有图像生成模型聚焦于学术任务研究时，大语言模型（LLM）（Radford 等，2019；Raffel 等，2020；Brown，2020；Ouyang 等，2022；Zhang 等，2022；Touvron 等，2023a；Touvron 等，2023b；Dubey 等，2024）与多模态语言模型（MLLM）（Li 等，2024；Wang 等，2024a；OpenAI，2024；Team 等，2023）的快速演进表明，未来的图像生成模型将越来越追求同时实现专业级质量与任务统一，从而能够无缝处理各类复杂应用。

**EN** Recent advances in image generation have demonstrated robust task unification and generalization through large-scale pre-training and arbitrary task learning (Ge et al., 2023; Sun et al., 2023; Sun et al., 2024; Wang et al., 2024b; Chern et al., 2024; Huang et al., 2024). These models handle a wide range of academic tasks with a unified input-output format and can generalize to unseen tasks, showcasing in-context learning abilities. However, existing benchmarks (Cho et al., 2023; Ghosh et al., 2024; Sheynin et al., 2024; Hu et al., 2023; Ruiz et al., 2023; Ku et al., 2023) are often narrow in scope, focusing primarily on isolated academic tasks and lacking comprehensive criteria to evaluate the multifaceted demands of professional image design. Consequently, there is a critical need for more robust and versatile evaluation frameworks to effectively assess the diverse and sophisticated capabilities of contemporary generative models.

**ZH** 图像生成的最新进展已通过大规模预训练与任意任务学习展现出强大的任务统一性与泛化能力（Ge 等，2023；Sun 等，2023；Sun 等，2024；Wang 等，2024b；Chern 等，2024；Huang 等，2024）。这些模型以统一的输入输出格式处理范围广泛的学术任务，并能泛化到未见过的任务，展现出上下文学习能力。然而，现有基准（Cho 等，2023；Ghosh 等，2024；Sheynin 等，2024；Hu 等，2023；Ruiz 等，2023；Ku 等，2023）往往范围狭窄，主要聚焦孤立的学术任务，缺乏评估专业图像设计多方面需求的综合标准。因此，亟需更稳健、更通用的评估框架，以有效衡量当代生成模型多样而复杂的能力。

**EN** To bridge the gap between generative models and professional-grade design, we introduce IDEA-Bench (Intelligent Design Evaluation and Assessment Benchmark). We conduct a thorough review of real-world design and art tasks from diverse platforms, distilling 100 representative professional image generation tasks and 275 cases that comprehensively span the essential capabilities and effects for creating all forms of artwork. These tasks are systematically categorized into five distinct types based on required capabilities: text-to-image, image-to-image, images-to-image, text-to-images, and image(s)-to-images, as illustrated in fig. 1. Figure 2 provides an intuitive display of the definition of some tasks. Currently, only a few models (Yang et al., 2024a; Wu et al., 2024a; Wang et al., 2024b; Chern et al., 2024) can handle the most intricate category, which demands MLLM-level understanding of both image and text and the ability to produce variable-length image sequences. To evaluate generated images, we leverage MLLM to transform the evaluation into an image understanding task. This approach surpasses traditional metrics like FID (Chong and Forsyth, 2020) and CLIPScore (Hessel et al., 2021), which fail to capture nuances in aesthetic quality, contextual relevance, and multimodal integration. IDEA-Bench includes six detailed evaluation questions per case, totaling 1,650 binary scoring items, and a representative subset of 18 tasks for more nuanced and reliable assessments, ensuring precise and objective evaluations aligned with professional design standards.

**ZH** 为弥合生成模型与专业级设计之间的鸿沟，我们提出 IDEA-Bench（智能设计评测与评估基准）。我们全面梳理了来自多个平台的真实世界设计与艺术任务，提炼出 100 个具有代表性的专业图像生成任务与 275 个用例，完整覆盖创作各类艺术作品所需的核心能力与效果。这些任务按所需能力被系统地分为五种不同类型：文本到图像、图像到图像、多图到图像、文本到多图，以及图像/多图到多图，如图 1 所示；图 2 直观展示了部分任务的定义。目前只有少数模型（Yang 等，2024a；Wu 等，2024a；Wang 等，2024b；Chern 等，2024）能处理最复杂的那一类——它要求具备 MLLM 级别的图文理解能力，并能够产出可变长度的图像序列。为评估生成的图像，我们借助 MLLM 把评估转化为图像理解任务。这一途径优于 FID（Chong 和 Forsyth，2020）与 CLIPScore（Hessel 等，2021）等传统指标，后者无法捕捉美学质量、上下文相关性与多模态融合上的细微差别。IDEA-Bench 为每个用例设置六道细致的评估问题，共 1,650 项二值评分条目；另设 18 个任务的代表性子集用于更细腻、更可靠的评估，从而确保评估精确、客观并与专业设计标准对齐。

**EN** Our contributions can be summarized as follows:

**ZH** 我们的贡献可概括如下：

**EN** • We introduce IDEA-Bench to bridge the gap between current generative model capabilities and the stringent demands of professional-grade image design, which consists of 100 carefully selected tasks.

**ZH** • 我们提出 IDEA-Bench，以弥合当前生成模型能力与专业级图像设计严苛要求之间的鸿沟；该基准包含 100 个精心挑选的任务。

**EN** • We develop a task categorization of five distinct categories based on complexity and modality requirements, with a detailed evaluation framework comprising 1,650 binary scoring items, enabling precise and objective assessment.

**ZH** • 我们依据复杂度与模态需求建立了五类任务划分，并配以包含 1,650 项二值评分条目的细致评估框架，从而实现精确、客观的评估。

**EN** • We leverage MLLM-evaluation on a subset of 18 representative tasks. IDEA-Bench demonstrates that MLLMs have the capability to perform objective image assessment.

**ZH** • 我们在 18 个代表性任务的子集上采用基于 MLLM 的评估，表明 MLLM 具备执行客观图像评估的能力。

**EN** 2 Related Work

**ZH** 2 相关工作

**EN** 2.1 Image Synthesis Models

**ZH** 2.1 图像合成模型

**EN** Recently, diffusion models such as Stable Diffusion (Podell et al., 2023; Esser et al., 2024b), DALL-E 3 (Ramesh et al., 2022), and FLUX-1 (Labs, 2024b) have gained significant popularity for generating photorealistic images and offering improved training stability. However, state-of-the-art models still struggle with intricate prompts involving multiple visual concepts and extensive textual information, similar to image editing models (Brooks et al., 2023; Zhang et al., 2024a; Sheynin et al., 2024), which find it challenging to interpret detailed commands requiring nuanced modifications for professional-grade tasks. To enhance generative models’ capabilities, IDEA-Bench assesses existing image editing models against the rigorous demands of professional image design, aiming to emulate the creative and analytical processes of human designers. Additionally, image customization (Gal et al., 2022; Hu et al., 2021; Ruiz et al., 2022) is crucial for professionals needing varied personalized images. While techniques like Textual Inversion (Gal et al., 2022), LoRA (Hu et al., 2021), and DreamBooth (Ruiz et al., 2022) improve text-to-image models through fine-tuning, they lack adaptability to unseen subjects. IDEA-Bench aims at comprehensively evaluating models’ customization capabilities across multi-image generation tasks, assessing consistency in content, style, identity, and conceptual aspects.

**ZH** 近来，Stable Diffusion（Podell 等，2023；Esser 等，2024b）、DALL-E 3（Ramesh 等，2022）与 FLUX-1（Labs，2024b）等扩散模型因能生成照片级真实图像并具备更好的训练稳定性而广受欢迎。然而，最先进的模型在处理包含多个视觉概念与大量文本信息的复杂提示时仍然吃力；图像编辑模型（Brooks 等，2023；Zhang 等，2024a；Sheynin 等，2024）同样如此，它们难以理解需要对专业级任务作细致修改的详尽指令。为提升生成模型的能力，IDEA-Bench 依据专业图像设计的严苛要求来评估现有图像编辑模型，力求模拟人类设计师的创造与分析过程。此外，图像定制（Gal 等，2022；Hu 等，2021；Ruiz 等，2022）对需要多样化个性化图像的专业人士至关重要。Textual Inversion（Gal 等，2022）、LoRA（Hu 等，2021）与 DreamBooth（Ruiz 等，2022）等技术通过微调改进了文本到图像模型，却缺乏对未见主体的适应性。IDEA-Bench 旨在跨多图生成任务全面评估模型的定制能力，考察其在内容、风格、身份与概念层面的一致性。

**EN** 2.2 Universal Generative Model

**ZH** 2.2 通用生成模型

**EN** Universal generative models have become pivotal in advancing AI’s ability to perform a diverse array of tasks across both language and vision domains. LLMs (Radford et al., 2019; Raffel et al., 2020; Brown, 2020; Ouyang et al., 2022; Zhang et al., 2022; Touvron et al., 2023a; Touvron et al., 2023b; Dubey et al., 2024) have demonstrated remarkable versatility, excelling in tasks such as question answering and summarization through extensive pretraining on varied datasets. Building on this success, recent academic efforts (Team, 2024; Zhou et al., 2024; Sun et al., 2024; Wang et al., 2024b; Xiao et al., 2024) aim to adopt a more cohesive paradigm that addresses a wide range of visual generation tasks, including text-to-image and autoregressive image synthesis. Despite these advancements, there remains a significant gap in establishing a unified benchmark that comprehensively evaluates the multifaceted capabilities of these generative models. IDEA-Bench establishes a unified evaluation standard to assesses the strengths and limitations of existing generative foundation models, while guiding the development towards handling realistic and complex real-world image generation tasks at the same time.

**ZH** 通用生成模型已成为推进 AI 在语言与视觉两大领域执行多样任务能力的枢纽。LLM（Radford 等，2019；Raffel 等，2020；Brown，2020；Ouyang 等，2022；Zhang 等，2022；Touvron 等，2023a；Touvron 等，2023b；Dubey 等，2024）通过在多样数据集上的大规模预训练展现出极强的通用性，在问答与摘要等任务上表现优异。在此成功之上，近期的学术工作（Team，2024；Zhou 等，2024；Sun 等，2024；Wang 等，2024b；Xiao 等，2024）致力于采用更具内聚性的范式，覆盖文本到图像、自回归图像合成等范围广泛的视觉生成任务。尽管有这些进展，在建立统一基准以全面评估这些生成模型多方面能力方面仍存在显著空白。IDEA-Bench 建立了统一的评估标准，用以衡量现有生成式基础模型的优势与局限，同时引导其发展，使之能够处理现实而复杂的真实世界图像生成任务。

**EN** 2.3 Benchmarks for Generative Models

**ZH** 2.3 面向生成模型的基准

**EN** Table 1: Comparison with other image generation benchmarks. IDEA-Bench offers a broader range of task categories, multiple levels of model capabilities for evaluation, and longer and more complex prompts.

**ZH** 表 1：与其他图像生成基准的对比。IDEA-Bench 提供更广的任务类别范围、多层次的模型能力评估，以及更长、更复杂的提示。

<!-- [原子块 · table] Benchmark Tasks Evaluation Category Avg. Length MLLM Eval. T2I T2Is I2I Is2I I(s)2Is PaintSkills ( Cho et al., 2023 ) 3 ✓ ✗ ✗ ✗ ✗ 10.44 ✗ GenEval ( Ghosh et al., 2024 ) 6 ✓ ✗ ✗ ✗ ✗ 7.61 ✗ EmuEdit ( Sh -->

**EN** The development of benchmarks typically keeps pace with advancements in text-to-image (T2I) synthesis (Ramesh et al., 2021; Ramesh et al., 2022; Esser et al., 2021; Rombach et al., 2022; Saharia et al., 2022; Betker et al., 2023; Podell et al., 2023; Esser et al., 2024a; Baldridge et al., 2024; Chen et al., 2023; Labs, 2024a). DrawBench was initially introduced by Imagen (Saharia et al., 2022), followed by DALL-EVAL (Cho et al., 2023), which proposed PaintSkills to evaluate visual reasoning and social bias capabilities. Recently, an increasing number of benchmarks have emerged (Petsiuk et al., 2022; Bakr et al., 2023; Huang et al., 2023; Lee et al., 2024; Ku et al., 2023). While these benchmarks primarily focus on assessing image quality and alignment, DEsignBench (Lin et al., 2023) shares similarities with our approach by emphasizing scenarios within authentic design contexts. Differently, IDEA-Bench extends beyond this by addressing additional open challenges in professional creativity. Furthermore, IDEA-Bench is more closely aligned with the latest model capabilities, enabling the use of multi-image and complex instructions as diverse forms of guidance. As shown in table 1, IDEA-Bench greatly expand the prompt length and adde two evaluation dimensions: multi-image input and multi-image generation. This allows for the generation of both single and multiple images, thereby better mimicking the workflows of professional designers.

**ZH** 基准的发展通常与文本到图像（T2I）合成的进展同步（Ramesh 等，2021；Ramesh 等，2022；Esser 等，2021；Rombach 等，2022；Saharia 等，2022；Betker 等，2023；Podell 等，2023；Esser 等，2024a；Baldridge 等，2024；Chen 等，2023；Labs，2024a）。DrawBench 最初由 Imagen（Saharia 等，2022）提出，其后 DALL-EVAL（Cho 等，2023）提出 PaintSkills 以评估视觉推理与社会偏置方面的能力。近来涌现出越来越多的基准（Petsiuk 等，2022；Bakr 等，2023；Huang 等，2023；Lee 等，2024；Ku 等，2023）。这些基准主要关注图像质量与对齐度的评估，其中 DEsignBench（Lin 等，2023）与我们的思路相近，强调真实设计语境下的场景；不同之处在于，IDEA-Bench 更进一步，处理专业创意中的其他开放性挑战。此外，IDEA-Bench 与最新的模型能力更为贴合，支持以多图像与复杂指令作为多样化的引导形式。如表 1 所示，IDEA-Bench 大幅扩展了提示长度，并新增了两个评估维度：多图输入与多图生成。这使得单图与多图的生成都成为可能，从而更好地模拟专业设计师的工作流程。

**EN** 3 IDEA-Bench

**ZH** 3 IDEA-Bench

**EN** We present IDEA-Bench, a comprehensive image generation benchmark that encompasses a wide range of professional tasks in image generation and rigorously challenges models across multiple dimensions of capability. In this section, we first introduce IDEA-Bench’s data collection over four different model level in section 3.1, as well as the manual annotation pipeline in section 3.2, followed by a detailed explanation of both human evaluation and automated assessment methodologies, along with the specific metrics used, in section 3.3.

**ZH** 我们提出 IDEA-Bench——一个覆盖广泛专业任务的综合图像生成基准，从多个能力维度对模型提出严格挑战。本节先在 3.1 节介绍 IDEA-Bench 在四个不同模型层级上的数据采集，在 3.2 节介绍人工标注流程，随后在 3.3 节详述人工评估与自动评估方法以及所采用的具体指标。

**EN** 3.1 Data Collection

**ZH** 3.1 数据采集

**EN** To ensure that the tasks evaluated in IDEA-Bench closely mirror real-world and professional scenarios, we source all task directives and data from the internet and professional designers. Leveraging the knowledge and capabilities of GPT-4o (OpenAI, 2024), we clearly define and classify the tasks, creating task variants aligned with existing model capabilities. The tasks in IDEA-Bench are categorized as follows:

**ZH** 为使 IDEA-Bench 所评估的任务贴近真实世界与专业场景，我们从互联网与专业设计师处获取全部任务指令与数据。借助 GPT-4o（OpenAI，2024）的知识与能力，我们对任务作出清晰的定义与分类，并创建与现有模型能力相匹配的任务变体。IDEA-Bench 中的任务分类如下：

<!-- [原子块 · img]  -->

**EN** Figure 3: Dataset construction process of IDEA-Bench. We categorize the task data from professional design websites and designers based on generative model capabilities and assign capability keywords to each category. For each specific task, we design image generation prompts and hierarchical evaluation questions. Evaluators then refine these evaluation questions on a representative subset.

**ZH** 图 3：IDEA-Bench 的数据集构建流程。我们依据生成模型能力，对来自专业设计网站与设计师的任务数据加以分类，并为每个类别赋予能力关键词。针对每个具体任务，我们设计图像生成提示与层级化评估问题；随后评估者在代表性子集上对这些评估问题加以精修。

**EN** Text-only Guided Image Generation

**ZH** 纯文本引导的图像生成

**EN** While typical T2I users provide brief descriptions and rely on the model’s discretion, professional users meticulously control every visual detail, often iterating multiple prompts to achieve the desired outcome. Current T2I models (Ramesh et al., 2021; Ramesh et al., 2022; Esser et al., 2021; Rombach et al., 2022; Saharia et al., 2022; Betker et al., 2023; Podell et al., 2023; Esser et al., 2024a; Baldridge et al., 2024; Chen et al., 2023; Labs, 2024a) struggle with complex prompts that include numerous visual concepts and lengthy text. To address this, IDEA-Bench includes 11 tasks designed to evaluate models’ ability to handle extensive visual components and incorporate text within images, essential for tasks like poster generation and business card generation.

**ZH** 典型的 T2I 用户提供简短描述并由模型自行发挥，而专业用户会细致把控每一处视觉细节，常常反复迭代多条提示以获得理想结果。当前的 T2I 模型（Ramesh 等，2021；Ramesh 等，2022；Esser 等，2021；Rombach 等，2022；Saharia 等，2022；Betker 等，2023；Podell 等，2023；Esser 等，2024a；Baldridge 等，2024；Chen 等，2023；Labs，2024a）在处理包含大量视觉概念与长文本的复杂提示时表现不佳。为此，IDEA-Bench 纳入 11 个任务，用以评估模型处理丰富视觉要素以及在图像中嵌入文字的能力——这对海报生成、名片生成等任务不可或缺。

**EN** Image / Multi-image Guided Image Generation

**ZH** 图像 / 多图引导的图像生成

**EN** Unlike ImagenHub (Ku et al., 2023), which categorizes conditional image generation tasks under specific definitions, we unify these into image-to-image and images-to-image. This consolidation promotes the development of models with enhanced task unification and generalization, similar to advancements in LLMs. IDEA-Bench includes numerous design tasks guided by both image and text inputs in real-world contexts, such as brand merchandise generation, package rendering, and image retouching. With the advent of models like GDT (Huang et al., 2024), Emu2 (Sun et al., 2024), and OmniGen (Xiao et al., 2024), we anticipate future models will exhibit strong multimodal understanding and generative capabilities.

**ZH** 与把条件图像生成任务归入特定定义的 ImagenHub（Ku 等，2023）不同，我们把这些任务统一为图像到图像与多图到图像。这种归并推动了具备更强任务统一性与泛化能力的模型的发展，与 LLM 领域的进展相类似。IDEA-Bench 包含大量在真实情境下由图像与文本共同引导的设计任务，如品牌周边生成、包装渲染与图像修图。随着 GDT（Huang 等，2024）、Emu2（Sun 等，2024）与 OmniGen（Xiao 等，2024）等模型的出现，我们预期未来的模型将展现出强大的多模态理解与生成能力。

**EN** Text / (Multi-)image Guided Multi-image Generation

**ZH** 文本 /（多）图引导的多图生成

**EN** Distinct from previous benchmarks (Cho et al., 2023; Ghosh et al., 2024; Sheynin et al., 2024; Hu et al., 2023; Ruiz et al., 2023; Ku et al., 2023), IDEA-Bench introduces tasks that require generating multiple related images simultaneously. These tasks cater to professional demands such as creating series images around a subject, multi-view image generation, and illustrating storybooks. Unlike video generation (Zhao et al., 2024; Yang et al., 2024b), these image tasks involve significant visual differences while maintaining specific correlations. We further subdivide multi-image generation into text-to-images and image(s)-to-images categories to address models’ limitations in handling diverse input modalities, thereby testing their ability to maintain detail, style, and content consistency.

**ZH** 与既往基准（Cho 等，2023；Ghosh 等，2024；Sheynin 等，2024；Hu 等，2023；Ruiz 等，2023；Ku 等，2023）不同，IDEA-Bench 引入了需要同时生成多张相关图像的任务。这些任务回应了专业需求，例如围绕同一主体创作系列图像、多视角图像生成，以及为故事书画插图。与视频生成（Zhao 等，2024；Yang 等，2024b）不同，这些图像任务在保持特定关联的同时存在显著视觉差异。我们进一步把多图生成细分为文本到多图与图像/多图到多图两类，以针对模型在处理多样输入模态上的局限，检验其保持细节、风格与内容一致性的能力。

**EN** 3.2 Data Annotation

**ZH** 3.2 数据标注

**EN** Prompt Generation

**ZH** 提示生成

**EN** After collecting all tasks and corresponding images, annotators provide clear task definitions for each specific case, which, along with input images, are fed to GPT-4o (OpenAI, 2024) to generate image prompts tailored to each case. To ensure consistent evaluation across tasks, we also use GPT-4o to create a standardized set of six evaluation questions per task, ranging from basic to advanced difficulty levels. Specifically, recognizing the inherent subjectivity in both MLLM-based and human evaluations, we adopt a binary scoring system (0 or 1) for each question. This approach draws from methodologies in recent multimodal benchmarks (Bai et al., 2023; Liu et al., 2025; Li et al., 2023; Zhang et al., 2024b), where multiple-choice formats are used to mitigate interpretive bias.

**ZH** 在收集完所有任务与对应图像后，标注者为每个具体用例给出清晰的任务定义，并将其与输入图像一并送入 GPT-4o（OpenAI，2024），以生成贴合该用例的图像提示。为保证跨任务评估的一致性，我们还用 GPT-4o 为每个任务生成一套标准化的六道评估问题，难度由基础到进阶分布。具体地，鉴于基于 MLLM 的评估与人工评估都存在固有的主观性，我们对每道问题采用二值计分（0 或 1）。这一做法借鉴了近期多模态基准（Bai 等，2023；Liu 等，2025；Li 等，2023；Zhang 等，2024b）的方法论——它们以选择题形式来缓解解读偏差。

**EN** To further enhance objectivity and reduce variability, we modify the typical multi-level scoring scale found in existing datasets and models, converting it into a set of six binary (true/false) questions. Each question is accompanied by clearly defined scoring criteria, with 0 indicating unmet standards and 1 representing success. For deeper granularity, questions 1-2 assess the model’s understanding of basic task requirements, questions 3-4 evaluate the quality of task completion, and questions 5-6 examine the model’s attention to detail and aesthetic quality in the generated images. This structured assessment methodology ensures a rigorous and objective evaluation framework, aligning with professional standards and reducing potential sources of instability in scoring.

**ZH** 为进一步提升客观性、降低波动，我们改造了现有数据集与模型中常见的多级评分量表，把它转换为一组六道二值（真/假）问题。每道问题都配有明确界定的评分标准，0 表示未达标，1 表示达标。为获得更细的粒度，问题 1–2 考察模型对基本任务要求的理解，问题 3–4 评估任务完成的质量，问题 5–6 则审视模型对生成图像细节与美学品质的关注。这种结构化的评估方法确保了框架严谨而客观，既契合专业标准，也减少了评分中潜在的不稳定来源。

**EN** Prompt Refinement

**ZH** 提示精修

**EN** However, despite our efforts to define evaluation questions as objectively as possible, multimodal large language models (MLLMs) (Li et al., 2024; Wang et al., 2024a; OpenAI, 2024; Team et al., 2023) still struggle to match human evaluators on complex, real-world tasks, limited by current models’ gaps in image comprehension relative to human capabilities. To address this, we select a subset of tasks and refine the evaluation questions based on specific examples, ensuring that MLLMs can yield intuitively reasonable results.

**ZH** 然而，尽管我们已尽力使评估问题尽可能客观，多模态大语言模型（MLLM）（Li 等，2024；Wang 等，2024a；OpenAI，2024；Team 等，2023）在复杂的真实世界任务上仍难以媲美人类评估者，其受限于当前模型在图像理解上相对人类能力的差距。为此，我们选取一部分任务，并基于具体示例对评估问题加以精修，确保 MLLM 能给出直观上合理的结果。

**EN** One challenge in using MLLMs as evaluators is the sensitivity of models like GPT-4V/GPT-4o to the order of image presentation (Wang et al., 2022; Wu et al., 2024b; Zhang et al., 2023b; Zheng et al., 2023), which particularly makes these models less reliable for consistent comparative evaluation. MLLMs also fail to identify the sequence of multiple input images, whether it is input separately for multiple images or input as a collage. To mitigate this, we manually fine-tune evaluation questions for each case within the task subset, ensuring alignment with human intuition.

**ZH** 把 MLLM 用作评估者时存在的一个挑战是：GPT-4V/GPT-4o 等模型对图像呈现顺序很敏感（Wang 等，2022；Wu 等，2024b；Zhang 等，2023b；Zheng 等，2023），这尤其削弱了这些模型在一致性比较评估中的可靠性。MLLM 也无法识别多张输入图像的顺序——无论这些图像是逐张分别输入，还是以拼图方式输入。为缓解这一点，我们在任务子集内逐用例人工微调评估问题，确保其与人类直觉相符。

**EN** For example, in the task of generating a children’s storybook with defined character images, we refine each evaluation angle by randomly sampling pairs of input and output images to test consistency. A typical question might ask if the primary character in the first input image appears with consistent features in the third output image. For testing, we use the Gemini 1.5 Pro (Team et al., 2023) to score model outputs and compared these results against human ratings. In cases where discrepancies arise, annotators iteratively refine the language of the evaluation questions until the MLLM evaluations align with human judgment. This approach enhances the robustness of our benchmark, ensuring that evaluations reflect both task-specific accuracy and consistency across diverse visual requirements.

**ZH** 例如，在依据给定角色图像生成儿童绘本的任务中，我们通过随机抽样输入与输出图像配对来检验一致性，以此精修每个评估角度。一道典型问题可能询问：第一张输入图像中的主要角色，是否在第三张输出图像中以一致的特征出现。测试时，我们使用 Gemini 1.5 Pro（Team 等，2023）为模型输出打分，并把这些结果与人工评分对比。若出现分歧，标注者就迭代地修改评估问题的措辞，直到 MLLM 的评估与人类判断一致。这种做法增强了基准的鲁棒性，确保评估既反映任务特有的准确性，也反映跨多样视觉要求的一致性。

<!-- [原子块 · img]  -->

**EN** Figure 4: Visualization of model generated images on IDEA-Bench. We present the generation results of some models in representative task examples, including text-to-image, image-to-image, and images-to-image. In the case of no input image or no generated image, use "⟦SLOT_0⟧" instead.

**ZH** 图 4：IDEA-Bench 上模型生成图像的可视化。我们展示部分模型在代表性任务示例中的生成结果，涵盖文本到图像、图像到图像与多图到图像。若无输入图像或无生成图像，则以“⟦SLOT_0⟧”代替。

**EN** 3.3 Evaluation

**ZH** 3.3 评估

**EN** 3.3.1 Human Evaluation

**ZH** 3.3.1 人工评估

**EN** Evaluation Metric

**ZH** 评估指标

**EN** Each subtask in IDEA-Bench comprises 2 to 5 specific cases, with all cases within a subtask being evaluated using the same set of six binary (0 or 1) judgment questions. These evaluation questions are organized into three hierarchical levels, reflecting the priority of task completion over mere aesthetic quality. For each case, scoring progresses sequentially through these levels. If a model does not achieve a perfect score at a lower level, the scores for all higher levels are automatically set to 0. This hierarchical approach ensures that while a model may generate high-quality and visually appealing images, it must also fully meet the task requirements to receive a high overall score. This methodology aligns the evaluation criteria with human design standards, emphasizing the importance of fulfilling task objectives.

**ZH** IDEA-Bench 中每个子任务包含 2 至 5 个具体用例，同一子任务内的所有用例均采用同一套六道二值（0 或 1）判断题进行评估。这些评估问题被组织为三个层级，体现出「完成任务优先于单纯美学质量」的取向。对每个用例，评分按层级顺序推进：若模型在较低层级未取得满分，则所有更高层级的得分自动置 0。这种层级化方式确保：即便模型生成了高质量、赏心悦目的图像，它也必须完全满足任务要求才能获得较高总分。该方法使评估标准与人类设计标准相一致，强调了达成任务目标的重要性。

**EN** Formally, let the dataset be denoted as ⟦SLOT_1⟧. Each subtask ⟦SLOT_2⟧ consists of 2 to 5 specific cases, all evaluated using the same set of six binary (0 or 1) judgment questions. The score for each subtask is calculated by averaging the binary scores of its cases. Subsequently, each major category ⟦SLOT_3⟧ receives its score by averaging the scores of its subtasks and converting the result to a percentage. The overall score for the entire dataset ⟦SLOT_4⟧ is then determined by averaging the scores of all ⟦SLOT_5⟧ major categories.

**ZH** 形式化地，记数据集为 ⟦SLOT_1⟧。每个子任务 ⟦SLOT_2⟧ 由 2 至 5 个具体用例组成，全部采用同一套六道二值（0 或 1）判断题评估；每个子任务的得分由其各用例的二值得分取平均得到。随后，每个大类 ⟦SLOT_3⟧ 的得分由其子任务得分取平均并换算为百分比得到。整个数据集 ⟦SLOT_4⟧ 的总分则由全部 ⟦SLOT_5⟧ 个大类的得分取平均确定。

**EN** Importantly, if a model fails to complete a specific task, it is assigned a score of 0 for that task, ensuring that incomplete performances are accurately reflected in the overall evaluation. This hierarchical scoring framework ensures a precise and objective assessment of model performance, closely aligning with the rigorous standards expected by professional designers.

**ZH** 重要的是，若模型未能完成某项具体任务，则该任务计 0 分，确保未完成的表现被准确反映在总体评估中。这一层级化评分框架保证了对模型性能的精确、客观评估，与专业设计师所期望的严苛标准高度吻合。

**EN** 3.3.2 Automated Evaluation

**ZH** 3.3.2 自动评估

**EN** Automated evaluation is performed on a subset of IDEA-Bench comprising 18 tasks, named IDEA-Bench-mini. During the prompt refinement phase, annotators craft unique evaluation questions for each case, in contrast to the human evaluation setup where all cases within a subtask share the same 6 evaluation questions. This tailored approach allows for more precise and context-specific assessments. Scoring is conducted using Gemini 1.5 Pro (Team et al., 2023), adhering to the same hierarchical scoring methodology outlined in section 3.3.1. To enhance result stability and reliability, each case is evaluated three times independently, and the final score is computed as the average of these three evaluations. This repetition mitigates potential variability in automated assessments and ensures consistent and robust scoring outcomes.

**ZH** 自动评估在 IDEA-Bench 中由 18 个任务构成的子集上进行，该子集名为 IDEA-Bench-mini。在提示精修阶段，标注者为每个用例撰写独特的评估问题——这与人工评估设置不同，后者中同一子任务内的所有用例共享同样的 6 道评估问题。这种量身定制的方式使评估更精确、更贴合具体语境。评分使用 Gemini 1.5 Pro（Team 等，2023）执行，遵循 3.3.1 节所述的同一套层级化评分方法。为提升结果的稳定性与可靠性，每个用例独立评估三次，最终得分取三次评估的平均值。这种重复降低了自动评估中潜在的波动，确保评分结果一致而稳健。

**EN** By integrating both human and automated evaluation methods, IDEA-Bench provides a comprehensive framework for assessing the multifaceted capabilities of generative models. This dual approach not only leverages the nuanced judgment of human evaluators but also benefits from the scalability and consistency of automated tools, thereby offering a balanced and thorough evaluation of model performance.

**ZH** 通过融合人工与自动两种评估方法，IDEA-Bench 为评估生成模型的多方面能力提供了综合框架。这种双重途径既利用了人类评估者的细腻判断，又受益于自动工具的可扩展性与一致性，从而对模型性能作出均衡而透彻的评估。

**EN** Table 2: Experimental results on all categories of IDEA-Bench. Each task category is averaged across all its subtasks, with the top-ranked model scores for each task type highlighted in bold. Task types that a model cannot support are marked with "–" and are treated as 0 points in the average score calculation. "⟦SLOT_6⟧" represents rephrasing using GPT-4o to adapt the model to all tasks.

**ZH** 表 2：IDEA-Bench 全部类别上的实验结果。每个任务类别在其全部子任务上取平均，各任务类型得分最高的模型以粗体标出。模型不支持的任务类型以“–”标记，并在平均分计算中按 0 分处理。“⟦SLOT_6⟧”表示使用 GPT-4o 改写提示以使模型适配所有任务。

<!-- [原子块 · table] Method Param. Scores on All Categories Avg. Score T2I I2I Is2I T2Is I(s)2Is FLUX-1 † \dagger ( Labs, 2024b ) 12B 46.06 12.13 4.89 20.15 29.17 22.48 DALL-E 3 † \dagger ( Ramesh et al., 2022 ) 12B 24.34 -->

**EN** 4 Experiments

**ZH** 4 实验

**EN** 4.1 Experimental Details

**ZH** 4.1 实验细节

**EN** 4.1.1 Prompts Rephrasing

**ZH** 4.1.1 提示改写

**EN** Currently, only a few models (Yang et al., 2024a; Wu et al., 2024a; Wang et al., 2024b; Chern et al., 2024) are capable of generating multiple related images simultaneously, makes it difficult to analyse a model’s ability to generate multiple images potentially. However, as DALL-E 3 (Ramesh et al., 2022) could perform multi-image generation owing to its MLLM GPT-4o (OpenAI, 2024), which could summarize multimodal input and then generate the corresponding prompt for each image. To empower other leading T2I models (Labs, 2024b; Esser et al., 2024a; Chen et al., 2023), we feed all input images and text prompt to GPT-4o and rephrase prompts for each image to be generated. By combining MLLM’s multimodal understanding ability, we can approximately achieve the multi-image generation tasks even with basic T2I models.

**ZH** 目前只有少数模型（Yang 等，2024a；Wu 等，2024a；Wang 等，2024b；Chern 等，2024）能够同时生成多张相关图像，这使得分析模型的多图生成能力变得困难。然而，DALL-E 3（Ramesh 等，2022）之所以能执行多图生成，正是依靠其 MLLM GPT-4o（OpenAI，2024）——后者可以总结多模态输入，再为每张图像生成相应的提示。为了让其他领先的 T2I 模型（Labs，2024b；Esser 等，2024a；Chen 等，2023）也具备该能力，我们把全部输入图像与文本提示送入 GPT-4o，并为每张待生成图像改写提示。借助 MLLM 的多模态理解能力，即便使用基础的 T2I 模型，我们也能近似地实现多图生成任务。

**EN** 4.1.2 Model Reimplementation

**ZH** 4.1.2 模型复现

**EN** We evaluate the capabilities of four categories of models in our study. For leading text-to-image (T2I) models, we select FLUX-1 (Labs, 2024b), Stable Diffusion 3 (SD3) (Esser et al., 2024a), Pixart (Chen et al., 2023), and DALL-E 3 (Ramesh et al., 2022). For image editing models, we choose InstructPix2Pix (Brooks et al., 2023) and MagicBrush Zhang et al. (2024a) To assess models with unified generation capabilities, we select Emu2 (Sun et al., 2024) and OmniGen (Xiao et al., 2024). Additionally, for models that support interleaved text and image generation, we include Anole (Chern et al., 2024). Notably, among the selected models, Anole (Chern et al., 2024) is the only one capable of handling an unrestricted number of input and output images. We endeavor to utilize the officially released model parameters and inference settings wherever possible; further details are provided in section 6.2.

**ZH** 我们在研究中评估了四类模型的能力。对于领先的 T2I 模型，我们选取 FLUX-1（Labs，2024b）、Stable Diffusion 3（SD3）（Esser 等，2024a）、Pixart（Chen 等，2023）与 DALL-E 3（Ramesh 等，2022）。对于图像编辑模型，我们选取 InstructPix2Pix（Brooks 等，2023）与 MagicBrush（Zhang 等，2024a）。为评估具备统一生成能力的模型，我们选取 Emu2（Sun 等，2024）与 OmniGen（Xiao 等，2024）。此外，对于支持图文交错生成的模型，我们纳入 Anole（Chern 等，2024）。值得注意的是，在所选模型中，Anole（Chern 等，2024）是唯一能够处理不受限数量输入与输出图像的模型。我们尽可能使用官方发布的模型参数与推理设置，更多细节见 6.2 节。

**EN** Table 3: Experimental results on Text-to-Image. Each task category is averaged across all its subtasks, with the top-ranked model scores for each subtask highlighted in bold.

**ZH** 表 3：文本到图像任务上的实验结果。每个任务类别在其全部子任务上取平均，各子任务得分最高的模型以粗体标出。

<!-- [原子块 · table] Method Subtasks Score Avg. Score Arch. Style Bus. Card Game UI Inf. Chart Int. Paint. Sculp. Ticket Land. LOGO Poster FLUX-1 ( Labs, 2024b ) 100.00 38.89 5.56 0.00 66.67 61.11 16.67 16.67 83.33 61.11  -->

**EN** Table 4: Experimental results on Image-to-Image. Each task category is averaged across all its subtasks, with the top-ranked model scores for each subtask highlighted in bold. "⟦SLOT_7⟧" represents the use of MLLM for prompt rephrasing.

**ZH** 表 4：图像到图像任务上的实验结果。每个任务类别在其全部子任务上取平均，各子任务得分最高的模型以粗体标出。“⟦SLOT_7⟧”表示使用 MLLM 进行提示改写。

<!-- [原子块 · table] Method Subtasks Score Avg. Score Anim. Attr. Coup. Icon ID Photo Blur Compl. Ret. Str. Light. Enl. Obj. Edit Pack. Rend. Style Edit Brand Merch. FLUX-1 † \dagger ( Labs, 2024b ) 0.00 16.67 0.00 2.78 4 -->

**EN** 4.2 Results on IDEA-Bench

**ZH** 4.2 IDEA-Bench 上的结果

**EN** Qualitative Analysis

**ZH** 定性分析

**EN** Figure 4 showcases the generated images across 7 models. For ease of comparison, we select several cases from three categories: text-to-image, image-to-image, and images-to-image. In fundamental text-to-image tasks, FLUX-1 (Labs, 2024b) demonstrates a clear advantage over other models, effectively comprehending the visual elements and professional-level requirements outlined in the prompts. Regarding image editing tasks, models that are not specifically designed for image editing struggle to preserve essential information from the original image. Emu2 (Sun et al., 2024) is the only model that roughly restores the shapes and compositions of objects from the original image. OmniGen (Xiao et al., 2024) excels in maintaining the identity of objects. However, for more complex tasks such as special effect synthesis, no current model sufficiently understands the intricate demands of these professional-level requirements.

**ZH** 图 4 展示了 7 个模型生成的图像。为便于比较，我们从文本到图像、图像到图像与多图到图像三个类别中选取了若干用例。在基础的文本到图像任务上，FLUX-1（Labs，2024b）相较其他模型优势明显，能有效领会提示中概述的视觉要素与专业级要求。在图像编辑任务上，并非专为图像编辑设计的模型难以保留原图中的关键信息；Emu2（Sun 等，2024）是唯一能大致还原原图中物体形状与构图的模型；OmniGen（Xiao 等，2024）在保持物体身份上表现突出。然而，对于特效合成等更复杂的任务，目前没有任何模型能充分理解这些专业级要求中的繁复之处。

**EN** We first present the ranking of all models based on their scores across the entire dataset, as detailed in table 2. Leveraging GPT-4o’s (OpenAI, 2024) multimodal understanding and task translation capabilities, FLUX-1 (Labs, 2024b) achieve the highest score of 22.46, significantly outperforming other models. Specialized image editing models (Brooks et al., 2023; Zhang et al., 2024a) lead in the image-to-image tasks, while the general-purpose generation model Emu2 (Sun et al., 2024) excels in the images-to-image tasks. In contrast, Anole (Chern et al., 2024), which is capable of generating multiple images simultaneously, do not achieve an ideal final score. Furthermore, no model surpass a score of 10 without utilizing the comprehension capabilities of MLLMs, indicating that general-purpose image generation models still face substantial challenges in achieving professional-grade performance. This underscores the need for comprehensive evaluation standards to guide the development of more specialized and capable generative models.

**ZH** 我们先给出所有模型在整份数据集上按得分的排名，详见表 2。借助 GPT-4o（OpenAI，2024）的多模态理解与任务转译能力，FLUX-1（Labs，2024b）取得 22.46 的最高分，显著优于其他模型。专用图像编辑模型（Brooks 等，2023；Zhang 等，2024a）在图像到图像任务上领先，而通用生成模型 Emu2（Sun 等，2024）在多图到图像任务上表现最佳。相比之下，能够同时生成多张图像的 Anole（Chern 等，2024）未取得理想的最终得分。此外，若不借助 MLLM 的理解能力，没有任何模型的得分能超过 10，说明通用图像生成模型在达到专业级表现上仍面临巨大挑战。这凸显出需要综合的评估标准来引导更专门、更强能力的生成模型的发展。

**EN** To further quantify the impact of MLLM (OpenAI, 2024) assistance on model capabilities within the benchmark, we proceed text-to-images and image(s)-to-images tasks that not supported by Emu2 (Sun et al., 2024) and OmniGen (Xiao et al., 2024) using GPT-4o-rephrased prompts. The results are supplemented at the bottom of table 2. Despite enhancing Emu2 and OmniGen’s capabilities with MLLMs, FLUX-1 (Labs, 2024b) remains the top performer, as shown in table 12. Notably, FLUX-1 even surpasses other models that support image input in image-to-image tasks. The advantage of T2I models (Labs, 2024b; Ramesh et al., 2022; Esser et al., 2024a; Chen et al., 2023) in this experiment lies in their ability to leverage MLLMs to understand different tasks. IDEA-Bench’s task definitions are highly specialized, making it difficult for other models to comprehend these tasks without relying on MLLM. Universal generative models also have difficult ensuring the quality of generated images, resulting in lower scores finally. Overall, to achieve high scores across all benchmark tasks, a model must possess both multimodal input-output capabilities and robust MLLM-level multimodal understanding. The following section provides a detailed analysis of each category.

**ZH** 为进一步量化 MLLM（OpenAI，2024）辅助对模型在基准中能力的影响，我们对 Emu2（Sun 等，2024）与 OmniGen（Xiao 等，2024）不支持的文本到多图与图像/多图到多图任务，采用经 GPT-4o 改写的提示加以处理，结果补充在表 2 底部。尽管用 MLLM 增强了 Emu2 与 OmniGen 的能力，FLUX-1（Labs，2024b）依旧位居榜首，如表 12 所示。值得注意的是，FLUX-1 甚至超越了其他支持图像输入的模型，在图像到图像任务上也占优。本实验中 T2I 模型（Labs，2024b；Ramesh 等，2022；Esser 等，2024a；Chen 等，2023）的优势在于它们能够借助 MLLM 来理解不同任务：IDEA-Bench 的任务定义高度专业化，其他模型若不依赖 MLLM 便难以理解这些任务；通用生成模型也难以保证生成图像的质量，最终得分偏低。总体而言，要在基准所有任务上取得高分，模型必须同时具备多模态输入输出能力与稳健的 MLLM 级多模态理解能力。下面逐类展开详细分析。

**EN** 4.2.1 Results on Text-to-Image

**ZH** 4.2.1 文本到图像上的结果

**EN** Table 5: Experimental results on Images-to-Image. Each task category is averaged across all its subtasks, with the top-ranked model scores for each subtask highlighted in bold. "⟦SLOT_8⟧" represents the use of MLLM for prompt rephrasing.

**ZH** 表 5：多图到图像任务上的实验结果。每个任务类别在其全部子任务上取平均，各子任务得分最高的模型以粗体标出。“⟦SLOT_8⟧”表示使用 MLLM 进行提示改写。

<!-- [原子块 · table] Method Subtasks Score Avg. Score Human Attr. Image Trans. Pan. Text Edit. 3D. Effect Image Blend. Spec. Effect Real and Anime FLUX-1 † \dagger ( Labs, 2024b ) 3.97 6.67 0.00 10.42 0.00 12.50 0.00 5.56 -->

**EN** Table 6: Experimental results on Text-to-Images. Each task category is averaged across all its subtasks, with the top-ranked model scores for each subtask highlighted in bold. "⟦SLOT_9⟧" represents the use of MLLM for prompt rephrasing.

**ZH** 表 6：文本到多图任务上的实验结果。每个任务类别在其全部子任务上取平均，各子任务得分最高的模型以粗体标出。“⟦SLOT_9⟧”表示使用 MLLM 进行提示改写。

<!-- [原子块 · table] Method Subtasks Score Avg. Score Anim. Grow. Child. Book Draw. Proc. Hist. Narr. Movie Shots Phys. Laws Plant Grow. Style Group Conc. Vis. Coup. Icon Dyn. Char. FLUX-1 † \dagger ( Labs, 2024b ) 25.00  -->

**EN** Table 7: Experimental results on Image(s)-to-Images. Each task category is averaged across all its subtasks, with the top-ranked model scores for each subtask highlighted in bold. "⟦SLOT_10⟧" represents the use of MLLM for prompt rephrasing.

**ZH** 表 7：图像/多图到多图任务上的实验结果。每个任务类别在其全部子任务上取平均，各子任务得分最高的模型以粗体标出。“⟦SLOT_10⟧”表示使用 MLLM 进行提示改写。

<!-- [原子块 · table] Method Subtasks Score Avg. Score Anim. Grow. Creat. Trans. Layer Decomp. Light. Effect Movie Shots Multi-app. Multi-dec. Multi-view Trans. FLUX-1 † \dagger ( Labs, 2024b ) 25.00 66.67 75.00 8.33 0.00  -->

**EN** Table 8: Experimental results on the subset IDEA-Bench-mini. Each task category is averaged across all its subtasks, with the top-ranked model scores for each subtask highlighted in bold. "G." represents evaluate using Gemini 1.5 pro (Team et al., 2023), "H." represents human evaluation. "⟦SLOT_11⟧" represents the use of MLLM for prompt rephrasing.

**ZH** 表 8：子集 IDEA-Bench-mini 上的实验结果。每个任务类别在其全部子任务上取平均，各子任务得分最高的模型以粗体标出。“G.”表示使用 Gemini 1.5 pro（Team 等，2023）评估，“H.”表示人工评估。“⟦SLOT_11⟧”表示使用 MLLM 进行提示改写。

<!-- [原子块 · table] Method CLIPScore Evaluation Category Avg. Score T2I I2I Is2I T2Is I(s)2Is G. H. G. H. G. H. G. H. G. H. G. H. FLUX-1 † \dagger ( Labs, 2024b ) 0.3432 83.33 67.04 28.71 5.56 4.86 6.25 32.29 28.13 37.50 -->

**EN** All models’ results on text-to-image tasks are presented in table 3. Notably, the FLUX-1 (Labs, 2024b) model significantly outperforms the others, effectively accomplishing the task objectives in the majority of tasks. Based on the task settings and each model’s performance, we observe the following:

**ZH** 所有模型在文本到图像任务上的结果见表 3。值得注意的是，FLUX-1（Labs，2024b）模型显著优于其他模型，在多数任务中有效达成了任务目标。基于任务设置与各模型表现，我们观察到以下几点：

**EN** • Text Generation Challenges: Text generation tasks are a common pain point for all models. Even though models can generate specific visual elements with high quality and understand style instructions specified in the prompts, they struggle to incorporate text into images as seamlessly as human designers. For example, in the business card generation task, only FLUX-1 (Labs, 2024b) received scores.

**ZH** • 文字生成的挑战：文字生成任务对所有模型而言都是一个共同的痛点。即便模型能高质量地生成特定视觉元素并理解提示中指定的风格指令，它们仍难以像人类设计师那样把文字自然融入图像。例如，在名片生成任务中，只有 FLUX-1（Labs，2024b）获得了分数。

**EN** • Performance of Basic vs. General Models: Basic text-to-image models generally demonstrate higher task completion rates compared to general models like Emu2 (Sun et al., 2024) and OmniGen (Xiao et al., 2024). This is expected, as general models prioritize enhancing task generalization and multimodal information processing capabilities, which inevitably compromises some aspects of image generation quality.

**ZH** • 基础模型与通用模型的表现：基础的文本到图像模型通常比 Emu2（Sun 等，2024）与 OmniGen（Xiao 等，2024）等通用模型表现出更高的任务完成率。这符合预期，因为通用模型优先提升任务泛化与多模态信息处理能力，难免在图像生成质量的某些方面作出妥协。

**EN** • Poor Performance on Information Charts: All models perform poorly on the information chart generation task, receiving a score of 0 from human evaluators. The primary reason is that generative models struggle to accurately transfer large amounts of text from the input to the output image, which is a basic ability to human designers. Additionally, many models do not support ultra-long text inputs.

**ZH** • 信息图表上的糟糕表现：所有模型在信息图表生成任务上表现都很差，被人工评估者评为 0 分。主要原因是生成模型难以把大量文字从输入准确转移到输出图像中，而这本是人类设计师的一项基础能力。此外，许多模型不支持超长文本输入。

**EN** 4.2.2 Results on Image-to-Image & Images-to-Image

**ZH** 4.2.2 图像到图像与多图到图像上的结果

**EN** The image-to-image tasks represent the strengths of image editing models. In table 4, MagicBrush (Zhang et al., 2024a) and InstructPix2Pix (Brooks et al., 2023) achieve the first and second highest evaluation scores, respectively. The images-to-image tasks involve more complex and diverse guidance or conditions, with Emu2 (Sun et al., 2024) attaining the highest score of 8.98, as shwon in table 5. From these results, we derive the following key insights:

**ZH** 图像到图像任务体现了图像编辑模型的优势。在表 4 中，MagicBrush（Zhang 等，2024a）与 InstructPix2Pix（Brooks 等，2023）分别取得第一与第二高的评估得分。多图到图像任务涉及更复杂多样的引导或条件，Emu2（Sun 等，2024）取得 8.98 的最高分，如表 5 所示。从这些结果中我们得出以下关键认识：

**EN** • Pros and Cons of Image Editing Models: In local editing tasks such as image blur and image retouching, image editing models excel at preserving the original features of the image. However, these models are typically trained or fine-tuned on specific image editing datasets, which diminishes their ability to perform subject-driven tasks, such as branded merchandise generation.

**ZH** • 图像编辑模型的优劣：在图像模糊、图像修图等局部编辑任务中，图像编辑模型擅长保留图像的原有特征。然而，这些模型通常在特定的图像编辑数据集上训练或微调，因而削弱了它们执行主体驱动任务（如品牌周边生成）的能力。

**EN** • In-Context Learning Capabilities: Emu2 (Sun et al., 2024) and OmniGen (Xiao et al., 2024) exhibit in-context learning abilities, as evidenced by OmniGen’s significantly higher scores in tasks like branded merchandise generation and special effect synthesis, achieving ID consistency between input and output images. Emu2 demonstrates the ability to comprehend and partially complete the image straighten task, indicating that the model possesses an understanding of the semantic aspects of visual elements.

**ZH** • 上下文学习能力：Emu2（Sun 等，2024）与 OmniGen（Xiao 等，2024）展现出上下文学习能力，这体现在 OmniGen 在品牌周边生成与特效合成等任务上得分明显更高，实现了输入与输出图像之间的 ID 一致性；Emu2 则展现出理解并部分完成图像校正任务的能力，说明该模型对视觉元素的语义层面有所把握。

**EN** • Challenges for Generative Models: General-purpose models perform poorly in tasks such as light condition editing. Although these tasks are frequently encountered by designers, the models require a certain level of understanding of real-world physical models, presenting a challenge for future generative models.

**ZH** • 生成模型面临的挑战：通用模型在光照条件编辑等任务上表现糟糕。尽管设计师频繁遇到这些任务，但模型需要对真实世界的物理模型具备一定程度的理解，这对未来的生成模型构成挑战。

**EN** 4.2.3 Results on Text-to-Images & Image(s)-to-Images

**ZH** 4.2.3 文本到多图与图像/多图到多图上的结果

**EN** Table 6 and table 7 present the evaluation results for text-to-images and select image(s)-to-images tasks, respectively. In both categories, SD3 (Esser et al., 2024a) and FLUX-1 (Labs, 2024b) achieve the highest scores. For tasks such as historical event generation, MLLMs can effectively convey detailed style requirements during the prompt rephrasing phase, resulting in relatively consistent style outcomes. However, for more complex tasks like children’s book generation that involve sophisticated capabilities such as consistency and preservation over ID and style, existing models struggle to perform adequately even when assisted by MLLMs. Nonetheless, generating multiple related images holds significant value; for example, the generated movie shots can serve as guiding conditions for multi-shot video generation models. We aim for the task types designed in our benchmark to align generative models with the capabilities of human designers, thereby further advancing toward general AI.

**ZH** 表 6 与表 7 分别给出文本到多图与部分图像/多图到多图任务的评估结果。在这两个类别中，SD3（Esser 等，2024a）与 FLUX-1（Labs，2024b）得分最高。对于历史事件生成等任务，MLLM 能在提示改写阶段有效传达细致的风格要求，从而得到相对一致的风格结果。然而，对于儿童绘本生成这类涉及 ID 与风格的保持与一致性等复杂能力的任务，现有模型即便借助 MLLM 也难以胜任。尽管如此，生成多张相关图像仍具有重要价值——例如，生成的电影镜头可作为多镜头视频生成模型的引导条件。我们期望基准中设计的任务类型能使生成模型向人类设计师的能力靠拢，从而进一步迈向通用 AI。

**EN** 4.2.4 Results on IDEA-Bench-mini

**ZH** 4.2.4 IDEA-Bench-mini 上的结果

**EN** Table 8 presents the evaluation results for a subset of 18 tasks within our benchmark, where we calculate CLIPScore (Hessel et al., 2021), Gemini 1.5 Pro (Team et al., 2023) scores, and human evaluation scores. As shown in table 8, FLUX-1 (Labs, 2024b), leveraging MLLM’s prompt rephrasing capabilities, achieve the highest scores in both MLLM-based and human evaluations within this subset. In contrast, when excluding the use of MLLMs, Emu2 (Sun et al., 2024) secure the top score. These experimental results are consistent with the overall benchmark dataset findings. Additionally, compared to CLIPScore, MLLM-based evaluations more closely align with human preferences in terms of professional evaluation data and assessment criteria. This suggests that as MLLM capabilities continue to evolve, utilizing MLLMs for image generation evaluation will become increasingly stable and reliable.

**ZH** 表 8 给出了基准中 18 个任务子集的评估结果，其中我们计算了 CLIPScore（Hessel 等，2021）、Gemini 1.5 Pro（Team 等，2023）评分与人工评估评分。如表 8 所示，借助 MLLM 提示改写能力的 FLUX-1（Labs，2024b）在该子集的 MLLM 评估与人工评估中均取得最高分；相反，在排除 MLLM 使用时，Emu2（Sun 等，2024）取得最高分。这些实验结果与整体基准数据集上的发现一致。此外，与 CLIPScore 相比，基于 MLLM 的评估在专业评估数据与评估准则上更贴近人类偏好。这说明随着 MLLM 能力持续演进，用 MLLM 进行图像生成评估将变得日益稳定可靠。

**EN** 5 Conclusion

**ZH** 5 结论

**EN** We introduce IDEA-Bench, a comprehensive benchmark designed to bridge the gap between current generative model capabilities and the stringent demands of professional-grade image design. IDEA-Bench encompasses 100 professional image generation tasks across five distinct categories, utilizing a detailed evaluation framework to ensure precise and objective assessments. Additionally, we build a representative subset IDEA-Bench-mini that facilitates automated evaluation using MLLMs. Our evaluations reveal significant gaps in existing models, particularly in handling intricate instructions and maintaining consistency in multi-image generation, underscoring the need for more advanced and versatile models. By aligning evaluation standards with the nuanced requirements of human designers, IDEA-Bench serves as a pivotal tool for guiding the development of generative models toward achieving professional-grade performance and advancing toward general artificial intelligence with autonomous and sophisticated visual generation capabilities.

**ZH** 我们提出 IDEA-Bench——一个旨在弥合当前生成模型能力与专业级图像设计严苛要求之间鸿沟的综合基准。IDEA-Bench 涵盖五个不同类别下的 100 个专业图像生成任务，并采用细致的评估框架以确保评估精确、客观。此外，我们构建了一个代表性子集 IDEA-Bench-mini，以支持基于 MLLM 的自动评估。我们的评估揭示了现有模型的显著差距，尤其体现在处理繁复指令与保持多图生成一致性方面，凸显出对更先进、更通用模型的迫切需求。通过使评估标准与人类设计师的细腻要求相对齐，IDEA-Bench 成为引导生成模型迈向专业级表现、并朝着具备自主而复杂视觉生成能力的通用人工智能推进的关键工具。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] Ramesh et al. [2021] Aditya Ramesh, Mikhail Pavlov, Gabriel Goh, Scott Gray, Chelsea Voss, Alec Radford, Mark Chen, and Ilya Sutskever. Zero-shot text-to-image generation. In International conference  -->

<!-- [原子块 · verbatim] Ramesh et al. [2022] Aditya Ramesh, Prafulla Dhariwal, Alex Nichol, Casey Chu, and Mark Chen. Hierarchical text-conditional image generation with clip latents. arXiv preprint arXiv:2204.06125 , 1(2):3 -->

<!-- [原子块 · verbatim] Esser et al. [2021] Patrick Esser, Robin Rombach, and Bjorn Ommer. Taming transformers for high-resolution image synthesis. In Proceedings of the IEEE/CVF conference on computer vision and pattern rec -->

<!-- [原子块 · verbatim] Rombach et al. [2022] Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, and Björn Ommer. High-resolution image synthesis with latent diffusion models. In Proceedings of the IEEE/CVF con -->

<!-- [原子块 · verbatim] Saharia et al. [2022] Chitwan Saharia, William Chan, Saurabh Saxena, Lala Li, Jay Whang, Emily L Denton, Kamyar Ghasemipour, Raphael Gontijo Lopes, Burcu Karagol Ayan, Tim Salimans, et al. Photorealis -->

<!-- [原子块 · verbatim] Betker et al. [2023] James Betker, Gabriel Goh, Li Jing, Tim Brooks, Jianfeng Wang, Linjie Li, Long Ouyang, Juntang Zhuang, Joyce Lee, Yufei Guo, et al. Improving image generation with better captions -->

<!-- [原子块 · verbatim] Podell et al. [2023] Dustin Podell, Zion English, Kyle Lacey, Andreas Blattmann, Tim Dockhorn, Jonas Müller, Joe Penna, and Robin Rombach. Sdxl: Improving latent diffusion models for high-resolution i -->

<!-- [原子块 · verbatim] Esser et al. [2024a] Patrick Esser, Sumith Kulal, Andreas Blattmann, Rahim Entezari, Jonas Müller, Harry Saini, Yam Levi, Dominik Lorenz, Axel Sauer, Frederic Boesel, et al. Scaling rectified flow tra -->

<!-- [原子块 · verbatim] Baldridge et al. [2024] Jason Baldridge, Jakob Bauer, Mukul Bhutani, Nicole Brichtova, Andrew Bunner, Kelvin Chan, Yichang Chen, Sander Dieleman, Yuqing Du, Zach Eaton-Rosen, et al. Imagen 3. arXiv pr -->

<!-- [原子块 · verbatim] Chen et al. [2023] Junsong Chen, Jincheng Yu, Chongjian Ge, Lewei Yao, Enze Xie, Yue Wu, Zhongdao Wang, James Kwok, Ping Luo, Huchuan Lu, et al. Pixart-alpha: Fast training of diffusion transformer fo -->

<!-- [原子块 · verbatim] Labs [2024a] Black Forest Labs. Flux: Inference repository. https://github.com/black-forest-labs/flux , 2024a. Accessed: 2024-10-25. -->

<!-- [原子块 · verbatim] Zhang et al. [2023a] Lvmin Zhang, Anyi Rao, and Maneesh Agrawala. Adding conditional control to text-to-image diffusion models. In Proceedings of the IEEE/CVF International Conference on Computer Visi -->

<!-- [原子块 · verbatim] Mou et al. [2024] Chong Mou, Xintao Wang, Liangbin Xie, Yanze Wu, Jian Zhang, Zhongang Qi, and Ying Shan. T2i-adapter: Learning adapters to dig out more controllable ability for text-to-image diffusio -->

<!-- [原子块 · verbatim] Brooks et al. [2023] Tim Brooks, Aleksander Holynski, and Alexei A Efros. Instructpix2pix: Learning to follow image editing instructions. In Proceedings of the IEEE/CVF Conference on Computer Vision a -->

<!-- [原子块 · verbatim] Sheynin et al. [2024] Shelly Sheynin, Adam Polyak, Uriel Singer, Yuval Kirstain, Amit Zohar, Oron Ashual, Devi Parikh, and Yaniv Taigman. Emu edit: Precise image editing via recognition and generation -->

<!-- [原子块 · verbatim] Radford et al. [2019] Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, Ilya Sutskever, et al. Language models are unsupervised multitask learners. OpenAI blog , 1(8):9, 2019. -->

<!-- [原子块 · verbatim] Raffel et al. [2020] Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter J Liu. Exploring the limits of transfer learning with a unifi -->

<!-- [原子块 · verbatim] Brown [2020] Tom B Brown. Language models are few-shot learners. arXiv preprint arXiv:2005.14165 , 2020. -->

<!-- [原子块 · verbatim] Ouyang et al. [2022] Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. Training language models to f -->

<!-- [原子块 · verbatim] Zhang et al. [2022] Susan Zhang, Stephen Roller, Naman Goyal, Mikel Artetxe, Moya Chen, Shuohui Chen, Christopher Dewan, Mona Diab, Xian Li, Xi Victoria Lin, et al. Opt: Open pre-trained transformer l -->

<!-- [原子块 · verbatim] Touvron et al. [2023a] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, et al. Llama: Ope -->

<!-- [原子块 · verbatim] Touvron et al. [2023b] Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al. Llama 2: Open  -->

<!-- [原子块 · verbatim] Dubey et al. [2024] Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Amy Yang, Angela Fan, et al. The llama 3 herd of model -->

<!-- [原子块 · verbatim] Li et al. [2024] Bo Li, Kaichen Zhang, Hao Zhang, Dong Guo, Renrui Zhang, Feng Li, Yuanhan Zhang, Ziwei Liu, and Chunyuan Li. Llava-next: Stronger llms supercharge multimodal capabilities in the wild, -->

<!-- [原子块 · verbatim] Wang et al. [2024a] Peng Wang, Shuai Bai, Sinan Tan, Shijie Wang, Zhihao Fan, Jinze Bai, Keqin Chen, Xuejing Liu, Jialin Wang, Wenbin Ge, et al. Qwen2-vl: Enhancing vision-language model’s perception  -->

<!-- [原子块 · verbatim] OpenAI [2024] OpenAI. Gpt-4o, 2024. URL https://openai.com/index/hello-gpt-4o/ . -->

<!-- [原子块 · verbatim] Team et al. [2023] Gemini Team, Rohan Anil, Sebastian Borgeaud, Jean-Baptiste Alayrac, Jiahui Yu, Radu Soricut, Johan Schalkwyk, Andrew M Dai, Anja Hauth, Katie Millican, et al. Gemini: a family of hi -->

<!-- [原子块 · verbatim] Ge et al. [2023] Yuying Ge, Sijie Zhao, Ziyun Zeng, Yixiao Ge, Chen Li, Xintao Wang, and Ying Shan. Making llama see and draw with seed tokenizer. arXiv preprint arXiv:2310.01218 , 2023. -->

<!-- [原子块 · verbatim] Sun et al. [2023] Quan Sun, Qiying Yu, Yufeng Cui, Fan Zhang, Xiaosong Zhang, Yueze Wang, Hongcheng Gao, Jingjing Liu, Tiejun Huang, and Xinlong Wang. Emu: Generative pretraining in multimodality. In  -->

<!-- [原子块 · verbatim] Sun et al. [2024] Quan Sun, Yufeng Cui, Xiaosong Zhang, Fan Zhang, Qiying Yu, Yueze Wang, Yongming Rao, Jingjing Liu, Tiejun Huang, and Xinlong Wang. Generative multimodal models are in-context learne -->

<!-- [原子块 · verbatim] Wang et al. [2024b] Xinlong Wang, Xiaosong Zhang, Zhengxiong Luo, Quan Sun, Yufeng Cui, Jinsheng Wang, Fan Zhang, Yueze Wang, Zhen Li, Qiying Yu, et al. Emu3: Next-token prediction is all you need. ar -->

<!-- [原子块 · verbatim] Chern et al. [2024] Ethan Chern, Jiadi Su, Yan Ma, and Pengfei Liu. Anole: An open, autoregressive, native large multimodal models for interleaved image-text generation. arXiv preprint arXiv:2407.0613 -->

<!-- [原子块 · verbatim] Huang et al. [2024] Lianghua Huang, Wei Wang, Zhi-Fan Wu, Huanzhang Dou, Yupeng Shi, Yutong Feng, Chen Liang, Yu Liu, and Jingren Zhou. Group diffusion transformers are unsupervised multitask learners -->

<!-- [原子块 · verbatim] Cho et al. [2023] Jaemin Cho, Abhay Zala, and Mohit Bansal. Dall-eval: Probing the reasoning skills and social biases of text-to-image generation models. In Proceedings of the IEEE/CVF International C -->

<!-- [原子块 · verbatim] Ghosh et al. [2024] Dhruba Ghosh, Hannaneh Hajishirzi, and Ludwig Schmidt. Geneval: An object-focused framework for evaluating text-to-image alignment. Advances in Neural Information Processing System -->

<!-- [原子块 · verbatim] Hu et al. [2023] Yushi Hu, Benlin Liu, Jungo Kasai, Yizhong Wang, Mari Ostendorf, Ranjay Krishna, and Noah A Smith. Tifa: Accurate and interpretable text-to-image faithfulness evaluation with question -->

<!-- [原子块 · verbatim] Ruiz et al. [2023] Nataniel Ruiz, Yuanzhen Li, Varun Jampani, Yael Pritch, Michael Rubinstein, and Kfir Aberman. Dreambooth: Fine tuning text-to-image diffusion models for subject-driven generation. I -->

<!-- [原子块 · verbatim] Ku et al. [2023] Max Ku, Tianle Li, Kai Zhang, Yujie Lu, Xingyu Fu, Wenwen Zhuang, and Wenhu Chen. Imagenhub: Standardizing the evaluation of conditional image generation models. arXiv preprint arXiv: -->

<!-- [原子块 · verbatim] Yang et al. [2024a] Shuai Yang, Yuying Ge, Yang Li, Yukang Chen, Yixiao Ge, Ying Shan, and Yingcong Chen. Seed-story: Multimodal long story generation with large language model. arXiv preprint arXiv:2 -->

<!-- [原子块 · verbatim] Wu et al. [2024a] Shengqiong Wu, Hao Fei, Leigang Qu, Wei Ji, and Tat-Seng Chua. Next-gpt: Any-to-any multimodal llm. In Proceedings of the International Conference on Machine Learning , pages 53366–5 -->

<!-- [原子块 · verbatim] Chong and Forsyth [2020] Min Jin Chong and David Forsyth. Effectively unbiased fid and inception score and where to find them. In Proceedings of the IEEE/CVF conference on computer vision and pattern  -->

<!-- [原子块 · verbatim] Hessel et al. [2021] Jack Hessel, Ari Holtzman, Maxwell Forbes, Ronan Le Bras, and Yejin Choi. Clipscore: A reference-free evaluation metric for image captioning. arXiv preprint arXiv:2104.08718 , 202 -->

<!-- [原子块 · verbatim] Esser et al. [2024b] Patrick Esser, Sumith Kulal, Andreas Blattmann, Rahim Entezari, Jonas Müller, Harry Saini, Yam Levi, Dominik Lorenz, Axel Sauer, Frederic Boesel, Dustin Podell, Tim Dockhorn, Zion -->

<!-- [原子块 · verbatim] Labs [2024b] Black Forest Labs. Flux.1, 2024b. URL https://github.com/black-forest-labs/flux . -->

<!-- [原子块 · verbatim] Zhang et al. [2024a] Kai Zhang, Lingbo Mo, Wenhu Chen, Huan Sun, and Yu Su. Magicbrush: A manually annotated dataset for instruction-guided image editing. Advances in Neural Information Processing Sys -->

<!-- [原子块 · verbatim] Gal et al. [2022] Rinon Gal, Yuval Alaluf, Yuval Atzmon, Or Patashnik, Amit H Bermano, Gal Chechik, and Daniel Cohen-Or. An image is worth one word: Personalizing text-to-image generation using textua -->

<!-- [原子块 · verbatim] Hu et al. [2021] Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen. Lora: Low-rank adaptation of large language models. arXiv preprint arXiv: -->

<!-- [原子块 · verbatim] Ruiz et al. [2022] Nataniel Ruiz, Yuanzhen Li, Varun Jampani, Yael Pritch, Michael Rubinstein, and Kfir Aberman. Dreambooth: Fine tuning text-to-image diffusion models for subject-driven generation. a -->

<!-- [原子块 · verbatim] Team [2024] Chameleon Team. Chameleon: Mixed-modal early-fusion foundation models. arXiv preprint arXiv:2405.09818 , 2024. -->

<!-- [原子块 · verbatim] Zhou et al. [2024] Chunting Zhou, Lili Yu, Arun Babu, Kushal Tirumala, Michihiro Yasunaga, Leonid Shamis, Jacob Kahn, Xuezhe Ma, Luke Zettlemoyer, and Omer Levy. Transfusion: Predict the next token an -->

<!-- [原子块 · verbatim] Xiao et al. [2024] Shitao Xiao, Yueze Wang, Junjie Zhou, Huaying Yuan, Xingrun Xing, Ruiran Yan, Shuting Wang, Tiejun Huang, and Zheng Liu. Omnigen: Unified image generation. arXiv preprint arXiv:2409 -->

<!-- [原子块 · verbatim] Petsiuk et al. [2022] Vitali Petsiuk, Alexander E Siemenn, Saisamrit Surbehera, Zad Chin, Keith Tyser, Gregory Hunter, Arvind Raghavan, Yann Hicke, Bryan A Plummer, Ori Kerret, et al. Human evaluation -->

<!-- [原子块 · verbatim] Bakr et al. [2023] Eslam Mohamed Bakr, Pengzhan Sun, Xiaoqian Shen, Faizan Farooq Khan, Li Erran Li, and Mohamed Elhoseiny. Hrs-bench: Holistic, reliable and scalable benchmark for text-to-image model -->

<!-- [原子块 · verbatim] Huang et al. [2023] Kaiyi Huang, Kaiyue Sun, Enze Xie, Zhenguo Li, and Xihui Liu. T2i-compbench: A comprehensive benchmark for open-world compositional text-to-image generation. Advances in Neural Inf -->

<!-- [原子块 · verbatim] Lee et al. [2024] Tony Lee, Michihiro Yasunaga, Chenlin Meng, Yifan Mai, Joon Sung Park, Agrim Gupta, Yunzhi Zhang, Deepak Narayanan, Hannah Teufel, Marco Bellagente, et al. Holistic evaluation of tex -->

<!-- [原子块 · verbatim] Lin et al. [2023] Kevin Lin, Zhengyuan Yang, Linjie Li, Jianfeng Wang, and Lijuan Wang. Designbench: Exploring and benchmarking dall-e 3 for imagining visual design. arXiv preprint arXiv:2310.15144 ,  -->

<!-- [原子块 · verbatim] Zhao et al. [2024] Xuanlei Zhao, Xiaolong Jin, Kai Wang, and Yang You. Real-time video generation with pyramid attention broadcast. arXiv preprint arXiv:2408.12588 , 2024. -->

<!-- [原子块 · verbatim] Yang et al. [2024b] Zhuoyi Yang, Jiayan Teng, Wendi Zheng, Ming Ding, Shiyu Huang, Jiazheng Xu, Yuanming Yang, Wenyi Hong, Xiaohan Zhang, Guanyu Feng, et al. Cogvideox: Text-to-video diffusion models  -->

<!-- [原子块 · verbatim] Bai et al. [2023] Shuai Bai, Shusheng Yang, Jinze Bai, Peng Wang, Xingxuan Zhang, Junyang Lin, Xinggang Wang, Chang Zhou, and Jingren Zhou. Touchstone: Evaluating vision-language models by language mo -->

<!-- [原子块 · verbatim] Liu et al. [2025] Yuan Liu, Haodong Duan, Yuanhan Zhang, Bo Li, Songyang Zhang, Wangbo Zhao, Yike Yuan, Jiaqi Wang, Conghui He, Ziwei Liu, et al. Mmbench: Is your multi-modal model an all-around playe -->

<!-- [原子块 · verbatim] Li et al. [2023] Bohao Li, Rui Wang, Guangzhi Wang, Yuying Ge, Yixiao Ge, and Ying Shan. Seed-bench: Benchmarking multimodal llms with generative comprehension. arXiv preprint arXiv:2307.16125 , 2023. -->

<!-- [原子块 · verbatim] Zhang et al. [2024b] Yi-Fan Zhang, Huanyu Zhang, Haochen Tian, Chaoyou Fu, Shuangqing Zhang, Junfei Wu, Feng Li, Kun Wang, Qingsong Wen, Zhang Zhang, et al. Mme-realworld: Could your multimodal llm ch -->

<!-- [原子块 · verbatim] Wang et al. [2022] Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa Liu, Noah A Smith, Daniel Khashabi, and Hannaneh Hajishirzi. Self-instruct: Aligning language models with self-generated instructi -->

<!-- [原子块 · verbatim] Wu et al. [2024b] Tong Wu, Guandao Yang, Zhibing Li, Kai Zhang, Ziwei Liu, Leonidas Guibas, Dahua Lin, and Gordon Wetzstein. Gpt-4v (ision) is a human-aligned evaluator for text-to-3d generation. In P -->

<!-- [原子块 · verbatim] Zhang et al. [2023b] Xinlu Zhang, Yujie Lu, Weizhi Wang, An Yan, Jun Yan, Lianke Qin, Heng Wang, Xifeng Yan, William Yang Wang, and Linda Ruth Petzold. Gpt-4v (ision) as a generalist evaluator for vis -->

<!-- [原子块 · verbatim] Zheng et al. [2023] Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric Xing, et al. Judging llm-as-a-judge with mt-bench and ch -->

**EN** 6 Implementation Details

**ZH** 6 实现细节

**EN** In this section, we detail the methods used for IDEA-Bench construction and experimental anlyses to ensure reproducibility. Section 6.1 provides example instructions for utilizing GPT-4o [OpenAI, 2024] in the construction of IDEA-Bench , while section 6.2 outlines the experimental configurations.

**ZH** 本节详述构建 IDEA-Bench 与开展实验分析所采用的方法，以保证可复现性。6.1 节给出在 IDEA-Bench 构建中使用 GPT-4o [OpenAI, 2024] 的示例指令，6.2 节概述实验配置。

**EN** 6.1 IDEA-Bench Construction Instruction

**ZH** 6.1 IDEA-Bench 构建指令

**EN** Instruction for prompt rephrasing

**ZH** 提示改写指令

**EN** As mentioned in section 4.1.1, to closely align with real design scenarios, IDEA-Bench includes multi-image generation tasks that most existing models do not support. To thoroughly evaluate current generative models’ capabilities in these tasks, we utilize one of the most advanced MLLMs, GPT-4o [OpenAI, 2024], to rephrase multimodal inputs (which may include multiple images and complex long texts) into several text-to-image prompts. The specific rephrasing instruction is illustrated in fig. 7. However, transforming tasks through rephrasing is merely a workaround, as text alone cannot capture all the details of the given images. Human designers have the ability to autonomously extract information from images and transform it into outputs in a freeform manner. We aim for IDEA-Bench to drive future generative models to acquire this capability.

**ZH** 如 4.1.1 节所述，为贴近真实设计场景，IDEA-Bench 包含了多数现有模型不支持的多图生成任务。为充分评估当前生成模型在这些任务上的能力，我们使用当前最先进的 MLLM 之一 GPT-4o [OpenAI, 2024]，把多模态输入（可能包含多张图像与复杂长文本）改写为若干条文本到图像提示，具体改写指令见图 7。然而，通过改写来转换任务只是一种权宜之计，因为单靠文本无法捕捉给定图像的全部细节；人类设计师能够自主地从图像中提取信息，并以自由形式把它转换为输出。我们希望 IDEA-Bench 能推动未来的生成模型获得这种能力。

**EN** Instruction for evaluation question construction

**ZH** 评估问题构建指令

**EN** After collecting the task data, we generate evaluation questions in bulk by combining task keywords provided by human annotators with GPT-4o [OpenAI, 2024]. Figure 8 illustrates an example of the instruction for generating evaluation questions for image(s)-to-images tasks. In fig. 8, the red sections indicate prompts that need to be customized for each specific task, while the JSON format templates are omitted. Within the fixed prompts, we first outline the basic requirements for the evaluation questions, such as multi-level standards, the exclusive use of objective judgment questions, and the convention that a score of 1 signifies a better result compared to 0. After incorporating the fundamental task definitions provided by annotators, the prompts also include frequently occurring evaluation capability keywords specific to multi-image generation tasks. This ensures that the evaluation questions defined by GPT-4o maintain a professional standard.

**ZH** 在收集任务数据后，我们把人工标注者提供的任务关键词与 GPT-4o [OpenAI, 2024] 相结合，批量生成评估问题。图 8 展示了为图像/多图到多图任务生成评估问题的指令示例。图 8 中红色部分标示需针对每个具体任务定制的提示，JSON 格式模板已略去。在固定提示中，我们先概述评估问题的基本要求，如多层级标准、只使用客观判断题，以及 1 分表示结果优于 0 分的约定；在纳入标注者提供的基本任务定义后，提示还包含多图生成任务中常出现的评估能力关键词，从而确保 GPT-4o 定义的评估问题维持专业水准。

**EN** 6.2 Inference Configuration

**ZH** 6.2 推理配置

**EN** Table 9 details the configurations applied during inference for all models. To ensure fairness, all diffusion-based models employ 50 sampling steps (DALL-E 3 [Ramesh et al., 2022] utilizes the official API and is therefore excluded from the statistics). Notably, Anole’s visual decoder is not diffusion-based [Chern et al., 2024]; instead, it employs a diffusion-free, token-based architecture. We adhere to the text guidance scale and image guidance scale recommended by the official project codes, as illustrated in table 9.

**ZH** 表 9 详列了所有模型在推理时采用的配置。为保证公平，所有基于扩散的模型均采用 50 步采样（DALL-E 3 [Ramesh 等, 2022] 使用官方 API，故不计入统计）。值得注意的是，Anole 的视觉解码器并非基于扩散 [Chern 等, 2024]，而是采用无扩散的、基于词元的架构。我们遵循各官方项目代码推荐的文本引导系数与图像引导系数，如表 9 所示。

**EN** 7 Statistical Analysis

**ZH** 7 统计分析

**EN** Figure 1 visualizes the distribution of all subtasks across categories. In this section, we further conduct statistical analyses on the composition of the prompts and evaluation criteria of IDEA-Bench.

**ZH** 图 1 可视化了各子任务在各类别间的分布。本节进一步对 IDEA-Bench 的提示构成与评估准则作统计分析。

**EN** Distribution of prompt length.

**ZH** 提示长度分布

**EN** In fig. 5, we present the distribution of prompt lengths across the five task categories using histograms. According to the statistics in table 1, IDEA-Bench’s prompts have an average length of approximately 139 words. Prompts shorter than the average are primarily found in the image-to-image and images-to-image tasks, as these tasks rely heavily on input images to guide the final generation, reducing the need for extensive textual descriptions. However, the prompt lengths for these two categories still significantly exceed those of other benchmarks [Cho et al., 2023, Ghosh et al., 2024, Sheynin et al., 2024, Hu et al., 2023, Ruiz et al., 2023, Ku et al., 2023]. Additionally, both text-to-image and image-to-images tasks feature excessively long prompts, due to the requirements for complex and rich visual elements or detailed descriptions for multiple generated images.

**ZH** 在图 5 中，我们以直方图呈现五类任务的提示长度分布。据表 1 的统计，IDEA-Bench 的提示平均长度约为 139 词。短于平均的提示主要出现在图像到图像与多图到图像任务中，因为这两类任务高度依赖输入图像来引导最终生成，对详尽文字描述的需求较低。然而，这两个类别的提示长度仍显著超过其他基准 [Cho 等, 2023；Ghosh 等, 2024；Sheynin 等, 2024；Hu 等, 2023；Ruiz 等, 2023；Ku 等, 2023]。此外，文本到图像与图像到多图任务的提示也格外长，原因在于需要复杂丰富的视觉要素，或对多张生成图像作细致描述。

**EN** Table 9: Inference details of the models being tested. "–" indicates either an API call or the absence of relevant parameters.

**ZH** 表 9：被测模型的推理细节。“–”表示通过 API 调用或不存在相关参数。

<!-- [原子块 · table] Method Param. DiT based Text Guid. Scale Image Guid. Scale Steps FLUX-1 [ Labs, 2024b ] 12B ✓ 3.5 – 50 DALL-E 3 [ Ramesh et al., 2022 ] 12B ✗ – – – SD3 [ Esser et al., 2024a ] 2B ✓ 7.0 – 50 Pixart [ C -->

**EN** Distribution of evaluation ability.

**ZH** 评估能力分布

**EN** We conduct a statistical analysis of the evaluation dimensions involved in each subtask within every category, with the results illustrated in the figure. In fig. 6, a higher value for a dimension indicates that the category places greater emphasis on assessing the model’s capabilities in that dimension. The analysis reveals that all five categories prioritize the evaluation of aesthetic aspects and the quality of the association between the generated images and the details in the prompts. Specifically, text-to-image tasks emphasize assessments of style, image composition, and text quality. In contrast, image-to-image and images-to-image tasks focus on evaluating the retention of elements between the input and output images. Meanwhile, text-to-images and image(s)-to-images tasks, which involve generating multiple images, concentrate on evaluating dimensions such as ID consistency and style consistency among the generated images.

**ZH** 我们对每个类别内各子任务涉及的评估维度作统计分析，结果如图所示。在图 6 中，某维度的取值越高，表示该类别越重视评估模型在该维度上的能力。分析显示，五个类别都优先评估美学方面，以及生成图像与提示细节之间关联的质量。具体地，文本到图像任务强调对风格、图像构图与文字质量的评估；相比之下，图像到图像与多图到图像任务聚焦评估输入与输出图像之间元素的保留情况；而涉及多图生成的文本到多图与图像/多图到多图任务，则集中于评估所生成图像之间的 ID 一致性与风格一致性等维度。

**EN** 8 Additional Experiments

**ZH** 8 补充实验

**EN** Supplementary results on image(s)-to-images

**ZH** 图像/多图到多图上的补充结果

**EN** Due to space constraints, we do not include all experimental results for the image(s)-to-images category in table 7. Supplementary results are provided in table 10. The current abilities of all models to achieve inter-image associations like ID consistency and style consistency stem from GPT-4o’s [OpenAI, 2024] detailed rephrasing of each prompt, akin to the group image descriptions in GDT [Huang et al., 2024]. However, GDT employs a design where image tokens are concatenated during attention computation, whereas solely using MLLM rephrasing does not facilitate inter-image association modeling in the latent space. In the future, to enable multi-image generation tasks with complex associations, models will need to consider parallel generation of multiple images or utilize partially generated images as input conditions to guide the generation of subsequent images.

**ZH** 受篇幅限制，我们未把图像/多图到多图类别的全部实验结果列入表 7，补充结果见表 10。当前所有模型之所以能实现 ID 一致性与风格一致性等图间关联，源于 GPT-4o [OpenAI, 2024] 对每条提示的细致改写，这与 GDT [Huang 等, 2024] 中的组图描述相类似。然而，GDT 采用了在注意力计算时拼接图像词元的设计，而仅使用 MLLM 改写并不能在潜空间中实现图间关联建模。未来，要实现具有复杂关联的多图生成任务，模型需要考虑多张图像的并行生成，或利用部分已生成的图像作为输入条件来引导后续图像的生成。

**EN** Table 10: Experimental results on Image(s)-to-Images. Each task category is averaged across all its subtasks, with the top-ranked model scores for each task type highlighted in bold. Task types that a model cannot support are marked with "–". "⟦SLOT_12⟧" represents the use of MLLM for prompt rephrasing.

**ZH** 表 10：图像/多图到多图任务上的实验结果。每个任务类别在其全部子任务上取平均，各任务类型得分最高的模型以粗体标出。模型不支持的任务类型以“–”标记。“⟦SLOT_12⟧”表示使用 MLLM 进行提示改写。

<!-- [原子块 · table] Method Subtasks Score Avg. Score Paint. Undo Same Pose Three-view Trans. Child. Book Plant Growth Prod. Usage Scen. Stop-motion Anim. FLUX-1 † \dagger [ Labs, 2024b ] 0.00 0.00 0.00 45.83 41.67 33.33  -->

**EN** GPT or Gemini for Evaluation?

**ZH** 用 GPT 还是 Gemini 作评估？

**EN** On a subset of the dataset, we select Gemini 1.5 Pro [Team et al., 2023] to score the images generated by models based on the refined evaluation questions. However, MLLMs produce free-form textual outputs, making it challenging to ensure binary scores of 0 or 1 as human annotators do, potentially resulting in scoring failures. In table 11, we report the failure rates of Gemini 1.5 pro [Team et al., 2023] and GPT-4o [OpenAI, 2024], representing the proportion of evaluation questions where scoring failed. Specifically, we conduct three evaluations per question. If all three attempts do not yield a clear score, the evaluation is considered a failure. Across all models and evaluation questions, Gemini 1.5 pro exhibits a low failure rate of 0.95%, whereas GPT-4o shows a high failure rate of 52.84%, rendering it unsuitable as a reliable automated evaluation model. In practice, GPT-4o frequently responds with phrases such as "I’m sorry, I can’t assist with that", whereas Gemini 1.5 pro provides more consistent responses.

**ZH** 在数据集的一个子集上，我们选取 Gemini 1.5 Pro [Team 等, 2023]，依据精修后的评估问题为模型生成的图像打分。然而，MLLM 产生的是自由形式的文本输出，难以像人类标注者那样确保给出 0 或 1 的二值分数，可能导致评分失败。在表 11 中，我们报告 Gemini 1.5 pro [Team 等, 2023] 与 GPT-4o [OpenAI, 2024] 的失败率，即评分失败的评估问题所占比例。具体地，我们对每道问题做三次评估；若三次尝试都未能给出明确分数，则视为评估失败。在所有模型与评估问题上，Gemini 1.5 pro 的失败率仅为 0.95%，而 GPT-4o 的失败率高达 52.84%，因此不适合作为可靠的自动评估模型。实践中，GPT-4o 常以「抱歉，我无法协助此事」之类的措辞回应，而 Gemini 1.5 pro 的回答更为一致。

**EN** Table 11: Comparison of evaluation failure rates among different MLLMs. For each evaluation question, MLLMs score the model-generated outputs three times. If none of the three scores return the required value (0 or 1), the evaluation is considered a failure.

**ZH** 表 11：不同 MLLM 评估失败率的对比。对于每个评估问题，MLLM 对模型生成输出评分三次；若三次评分均未返回所需的取值（0 或 1），则视为评估失败。

<!-- [原子块 · table] Eval. MLLM Method Total FLUX-1 DALL-E 3 SD3 Pixart InstructPix2Pix MagicBrush Emu2 OmniGen Gemini 1.5 pro [ Team et al., 2023 ] 0.33% 1.63% 1.96% 0.00% 0.00% 0.00% 0.67% 1.33% 0.95% GPT-4o [ OpenAI, 2 -->

**EN** Table 12: Additional experimental results on all categories of IDEA-Bench. "⟦SLOT_13⟧" represents the use of MLLM for prompt rephrasing. All models perform text-to-image generation on prompts rephrased by GPT-4o.

**ZH** 表 12：IDEA-Bench 全部类别上的补充实验结果。“⟦SLOT_13⟧”表示使用 MLLM 进行提示改写。所有模型均在经 GPT-4o 改写的提示上执行文本到图像生成。

<!-- [原子块 · table] Method Scores on All Categories Avg. Score T2I I2I Is2I T2Is I(s)2Is FLUX-1 † \dagger [ Labs, 2024b ] 46.06 12.13 4.89 20.15 29.17 22.48 DALL-E 3 † \dagger [ Ramesh et al., 2022 ] 24.34 6.95 5.26 14.3 -->

**EN** Comparison of T2I capabilities across all models

**ZH** 各模型 T2I 能力的对比

**EN** We also apply prompt rephrasing to all models in text-to-image generation settings. In this setup, all models have unified input comprehension capabilities, evaluating whether they can accurately translate prompts into high-quality generated images. The results are included in table 12, featuring Emu2 [Sun et al., 2024], OmniGen [Xiao et al., 2024], and Anole [Chern et al., 2024], each distinguished by the “-T2I” suffix. FLUX-1 [Labs, 2024b] remains the top-ranked model. FLUX-1 demonstrates a strong ability to convert prompts into images, maintaining stable image quality with only rare instances of failure.

**ZH** 我们还把提示改写应用于所有模型的文本到图像生成设置。在该设置下，所有模型具备统一的输入理解能力，从而考察它们能否准确地把提示转化为高质量的生成图像。结果见表 12，其中 Emu2 [Sun 等, 2024]、OmniGen [Xiao 等, 2024] 与 Anole [Chern 等, 2024] 各以“-T2I”后缀加以区分。FLUX-1 [Labs, 2024b] 依旧位居榜首，展现出把提示转化为图像的强大能力，图像质量稳定，失败案例极少。

**EN** 9 Data Examples

**ZH** 9 数据示例

**EN** Additional model-generated results are demonstrated in fig. 9 - fig. 13, including the input images and text prompts used. Some text prompts are omitted due to their length. Since different models support a limited number of task categories, we only showcase the models that are capable of handling each respective category in the generation results.

**ZH** 图 9 至图 13 展示了更多的模型生成结果，含所用的输入图像与文本提示；部分文本提示因过长而略去。由于不同模型支持的任务类别数量有限，我们在生成结果中只展示能够处理相应类别的模型。

**EN** Examples of automated evaluations conducted using Gemini 1.5 pro [Team et al., 2023] are illustrated in fig. 14 and fig. 15. Due to the detailed definitions of the generation prompts and evaluation questions, the evaluation process can be effectively transformed into a multimodal understanding task, which MLLM excels at. In both presented examples, the model-generated results fail to fully meet the prompt requirements, resulting in a score of 0.

**ZH** 图 14 与图 15 展示了使用 Gemini 1.5 pro [Team 等, 2023] 开展自动评估的示例。得益于生成提示与评估问题的细致定义，评估过程可有效地转化为 MLLM 所擅长的多模态理解任务。在所示的两个示例中，模型生成结果都未完全满足提示要求，因而得分为 0。

**EN** 10 Limitations & Future Work

**ZH** 10 局限性与未来工作

**EN** Due to the current capabilities of multimodal large language models (MLLMs) still falling short of human performance, we are unable to apply automated MLLM evaluations to all tasks while meeting the evaluation standards of professional designers. Furthermore, the primary goal of IDEA-Bench is to bridge the gap between current generative models and professional tasks, pushing model capabilities toward a professional level. However, there remains a significant distance to match the proficiency of professional designers. In the future, we will focus on updating and maintaining IDEA-Bench, continuously refining automated evaluation methods in line with the real-time advancements of MLLMs, and expanding to more specialized tasks. This will ensure that the benchmark effectively supports the ongoing evolution of generative model capabilities.

**ZH** 由于当前多模态大语言模型（MLLM）的能力仍不及人类，我们还无法在满足专业设计师评估标准的前提下，把基于 MLLM 的自动评估应用于全部任务。此外，IDEA-Bench 的主要目标是弥合当前生成模型与专业任务之间的鸿沟，把模型能力推向专业水准；但要媲美专业设计师的熟练程度仍有相当距离。未来我们将专注于更新与维护 IDEA-Bench，紧跟 MLLM 的实时进展持续改进自动评估方法，并扩展到更专门化的任务，以确保该基准能有效支撑生成模型能力的持续演进。

<!-- [原子块 · object]  -->

**EN** Figure 5: Statistics of prompt lengths for all tasks in IDEA-Bench. Each of the five task categories is represented by a distinct color. Prompt lengths are divided into five intervals, and the y-axis shows the number of tasks that fall within each interval.

**ZH** 图 5：IDEA-Bench 全部任务的提示长度统计。五个任务类别各以一种颜色表示。提示长度被划分为五个区间，纵轴显示落入各区间的任务数量。

<!-- [原子块 · object]  -->

**EN** Figure 6: Statistics of evaluation dimensions for all tasks in IDEA-Bench. Each of the five task categories is represented by a distinct color. A total of 12 evaluation dimensions are analyzed, with the radar chart values indicating the proportion of evaluation questions related to each dimension within each category.

**ZH** 图 6：IDEA-Bench 全部任务的评估维度统计。五个任务类别各以一种颜色表示。共分析 12 个评估维度，雷达图取值表示各类别中与该维度相关的评估问题占比。

<!-- [原子块 · img]  -->

**EN** Figure 7: An instruction example for prompt rephrasing. The red sections indicate customization for different subtasks. The JSON file format templates within the instructions are not shown.

**ZH** 图 7：提示改写的指令示例。红色部分标示针对不同子任务的定制内容，指令中的 JSON 文件格式模板未予展示。

<!-- [原子块 · img]  -->

**EN** Figure 8: An instruction example for generating evaluation questions. The red sections indicate customization for different subtasks. The JSON file format templates within the instructions are not shown.

**ZH** 图 8：生成评估问题的指令示例。红色部分标示针对不同子任务的定制内容，指令中的 JSON 文件格式模板未予展示。

<!-- [原子块 · img]  -->

**EN** Figure 9: Generations for selected cases in the text-to-image category. The displayed task categories, from top to bottom, include game UI generation, business card generation, architectural style generation, painting generation, and ticket generation.

**ZH** 图 9：文本到图像类别中选定用例的生成结果。自上而下展示的任务类别包括游戏 UI 生成、名片生成、建筑风格生成、绘画生成与票券生成。

<!-- [原子块 · img]  -->

**EN** Figure 10: Generations for selected cases in the image-to-image category. The displayed task categories, from top to bottom, include animal hair editing, image straighten, image retouching, text insertion, and time editing.

**ZH** 图 10：图像到图像类别中选定用例的生成结果。自上而下展示的任务类别包括动物毛发编辑、图像校正、图像修图、文字插入与时间编辑。

<!-- [原子块 · img]  -->

**EN** Figure 11: Generations for selected cases in the multi-image-to-image category. The displayed task categories, from top to bottom, include text style transfer, body painting transfer, art style transfer, 3D rendering, and double explosure.

**ZH** 图 11：多图到图像类别中选定用例的生成结果。自上而下展示的任务类别包括文字风格迁移、人体彩绘迁移、艺术风格迁移、三维渲染与双重曝光。

<!-- [原子块 · img]  -->

**EN** (a) Generated images for character action design

**ZH** (a) 角色动作设计的生成图像

<!-- [原子块 · img]  -->

**EN** (b) Generated images for character expression design

**ZH** (b) 角色表情设计的生成图像

**EN** Figure 12: Generations for selected cases in the text-to-multi-image category.

**ZH** 图 12：文本到多图类别中选定用例的生成结果。

<!-- [原子块 · img]  -->

**EN** Figure 13: Generations for the task of children’s storybook generation. The dashed line above represents the model’s input text prompts and role definition images, while the dashed line below illustrates the prompt generation results after rephrasing by GPT-4o [OpenAI, 2024] for four models.

**ZH** 图 13：儿童绘本生成任务的生成结果。上方虚线以上为模型的输入文本提示与角色定义图像，下方虚线以下展示经 GPT-4o [OpenAI, 2024] 改写后四个模型的提示生成结果。

<!-- [原子块 · img]  -->

**EN** Figure 14: Automated evaluation of poster generation. The red font represents content that changes with each task or evaluation question.

**ZH** 图 14：海报生成的自动评估。红色字体表示随任务或评估问题而变化的内容。

<!-- [原子块 · img]  -->

**EN** Figure 15: Automated evaluation of 3D rendering generation. The red font represents content that changes with each task or evaluation question.

**ZH** 图 15：三维渲染生成的自动评估。红色字体表示随任务或评估问题而变化的内容。
