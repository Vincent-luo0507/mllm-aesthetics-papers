# Step1X-Edit：面向通用图像编辑的实用框架

> 原标题：Step1X-Edit: A Practical Framework for General Image Editing
> 作者：Shiyu Liu, Yucheng Han, Peng Xing, Fukun Yin, Rui Wang, Wei Cheng, Jiaqi Liao, Yingming Wang, Honghao Fu, Chunrui Han, Guopeng Li, Yuang Peng 等 · arXiv:2504.17761 · 2025-04-24

<!-- [原子块 · verbatim] Step1X-Edit: A Practical Framework for General Image Editing -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] In recent years, image editing technology has witnessed remarkable and rapid development. The recent unveiling of cutting-edge multimodal models such as GPT-4o and Gemini2 Flash has presented highly p -->

**EN** 1 Introduction

**ZH** 1 引言

**EN** Image editing with natural language instructions has become an increasingly important task in vision-language research. It offers intuitive interaction for end users while posing unique technical challenges: understanding nuanced semantics, precisely localizing regions to edit, and preserving image fidelity. While diffusion models [42, 5, 7, 11, 41] have dramatically improved image generation quality, the existing design by integrating text encoder, e.g., CLIP [44] and T5 [45], with diffusion transformer often struggles with following editing instruction to maintain alignment between input image and edit instruction, especially when edit instructions are subtle or compositional.

**ZH** 用自然语言指令做图像编辑，已成为视觉—语言研究中一项日渐重要的任务。它为终端用户提供了直观的交互方式，同时也带来独特的技术挑战：理解细微的语义、精确定位待编辑区域、并维持图像的保真度。扩散模型 [42, 5, 7, 11, 41] 大幅提升了图像生成质量，但把 CLIP [44]、T5 [45] 等文本编码器与扩散 Transformer 拼接起来的既有设计，常常难以遵循编辑指令、保持输入图像与编辑指令之间的一致，当指令较为微妙或具有组合性时尤其如此。

**EN** Recent advances in proprietary multimodal foundation models, such as GPT-4o [37], Gemini2 Flash [15], and SeedEdit/Doubao [50], have pushed the frontier of instruction-based image editing. These systems leverage large-scale vision-language modeling capabilities to perform high-fidelity edits across diverse scenarios. However, their closed nature limits reproducibility and transparency. In parallel, open-source efforts like OmniGen [61] and ACE++ [34] aim to replicate similar capabilities but still fall short in terms of overall generalization, edit accuracy, and the quality of generated images.

**ZH** GPT-4o [37]、Gemini2 Flash [15]、SeedEdit/Doubao [50] 等闭源多模态基座模型的近期进展，把基于指令的图像编辑推到了新的前沿。这些系统借助大规模的视觉—语言建模能力，在多样场景中完成高保真编辑。然而其封闭性限制了可复现性与透明度。与此同时，OmniGen [61] 与 ACE++ [34] 等开源工作试图复现相近能力，但在整体泛化性、编辑准确率与生成图像质量上仍有差距。

**EN** In this work, we aim to narrow the performance gap between open-source and closed-source editing systems, while also pushing the boundary of practical and user-grounded editing evaluation. Although researchers have open-sourced editing datasets like AnyEdit [64] and OmniEdit [59], we argue that the quality and diversity of these datasets are not good enough to obtain comparable performance against the close-source algorithms like GPT-4o. Thus, to target the image edit problem, we first try to build a large-scale high quality dataset for training. More specifically, we identify ⟦SLOT_0⟧ major editing task categories based on the commonly used editing instructions. Guided by this taxonomy, we develop a scalable and flexible data pipeline to generate over ⟦SLOT_1⟧ million high-quality training data. These image-instruction pairs encompass a broad spectrum of editing operations, including object manipulation, attribute modification, layout adjustment, and stylization, ensuring comprehensive coverage of real-world editing scenarios.

**ZH** 本文的目标是缩小开源与闭源编辑系统之间的性能差距，同时推动编辑评测走向实用、扎根用户。尽管研究者已开源 AnyEdit [64]、OmniEdit [59] 等编辑数据集，我们认为这些数据集的质量与多样性还不足以支撑模型取得可与 GPT-4o 等闭源算法比肩的性能。因此，针对图像编辑问题，我们首先着手构建一个大规模高质量训练数据集。具体而言，我们依据常用编辑指令归纳出 ⟦SLOT_0⟧ 个主要编辑任务类别；在该分类体系的引导下，开发了一套可扩展、灵活的数据流水线，生成超过 ⟦SLOT_1⟧ 百万条高质量训练数据。这些图像—指令对涵盖了对象操作、属性修改、布局调整与风格化等广泛的编辑操作，确保对真实编辑场景的全面覆盖。

<!-- [原子块 · img]  -->

**EN** Figure 1: Overview of Step1X-Edit. Step1X-Edit is an open-source general editing model that achieves proprietary-level performance with comprehensive editing capabilities.

**ZH** 图 1：Step1X-Edit 概览。Step1X-Edit 是一个开源通用编辑模型，具备全面的编辑能力，并达到闭源模型水准的性能。

**EN** Building on this dataset, we propose, Step1X-Edit, a unified image editing model that combines the strong semantic reasoning of Multimedia Large Language Model (MLLM), e.g., Qwen-VL [3], with a DiT-style diffusion architecture. The reference image and editing prompts can be processed by the MLLM to generate a target image latent condition which will be integrated with the diffusion model to obtain the output image. Our approach maintains a good balance between reference image reconstruction and editing prompt following. To train the model, we start from a text-to-image model to retain aesthetic quality and visual consistency, which can be easily replace by the existing text-to-image models like SD3 [11], FLUX[5, 7, 26], HiDream-I1 [18] and Flex [38]. To evaluate the existing editing models, we introduce a new benchmark named GEdit-Bench. By carefully collecting the images and editing prompts, GEdit-Bench ensures both real-world editing requirements and the diversity of the editing prompts. The experiments on GEdit-Bench validate that Step1X-Edit outperforms existing open-source baselines with a large-margin and approaches the performance of leading proprietary models, e.g., GPT-4o.

**ZH** 在该数据集之上，我们提出 Step1X-Edit——一个统一的图像编辑模型，它把多模态大语言模型（Multimedia Large Language Model, MLLM），例如 Qwen-VL [3]，强大的语义推理能力与 DiT 式扩散架构结合起来。参考图像与编辑提示交由 MLLM 处理，生成目标图像的潜层条件，该条件再与扩散模型融合以得到输出图像；本方法在参考图像重建与编辑提示遵循之间维持了良好平衡。训练时我们从文生图模型出发，以保留美学质量与视觉一致性——该文生图模型可方便地替换为 SD3 [11]、FLUX [5, 7, 26]、HiDream-I1 [18]、Flex [38] 等既有模型。为评测现有编辑模型，我们提出了一个名为 GEdit-Bench 的新基准。通过精心采集图像与编辑提示，GEdit-Bench 兼顾了真实世界的编辑需求与编辑提示的多样性。在 GEdit-Bench 上的实验表明，Step1X-Edit 以大幅优势超越现有开源基线，并接近 GPT-4o 等头部闭源模型的性能。

**EN** In summary, there will be three contributions of our work:

**ZH** 综上，本文有三项贡献：

**EN** • We will open-source our Step1X-Edit model, to reduce the performance gap between open-source and closed-source image editing systems and boost further research in the field of image editing.

**ZH** • 开源 Step1X-Edit 模型，以缩小开源与闭源图像编辑系统之间的性能差距，并推动该领域的后续研究。

**EN** • A data generation pipeline is designed to produce high-quality image editing data. It ensures that the dataset is diverse, representative, and of sufficient quality to support the development of effective image editing models. The availability of such a pipeline provides a valuable resource for researchers and developers working on similar projects.

**ZH** • 设计了一套数据生成流水线，用于产出高质量的图像编辑数据。它确保数据集具有多样性、代表性与足够的质量，足以支撑有效图像编辑模型的开发。该流水线的开放为从事同类项目的研究者与开发者提供了有价值的资源。

**EN** • A new benchmark, named GEdit-Bench, grounded in real-world usages is developed to support more authentic and comprehensive evaluation. This benchmark, which is carefully curated to reflect actual user editing needs and a wide range of editing scenarios, enables more authentic and comprehensive evaluations of image editing models.

**ZH** • 提出了一个立足真实使用场景的新基准 GEdit-Bench，以支持更真实、更全面的评测。该基准经精心策管，反映用户的实际编辑需求与广泛的编辑场景，使图像编辑模型的评测更加真实、全面。

**EN** 2 Related Work

**ZH** 2 相关工作

**EN** 2.1 Controllable Image Generation and Edit

**ZH** 2.1 可控图像生成与编辑

**EN** Autoregressive (AR) models have been actively studied for controllable image generation and editing by modeling images as sequences of discrete tokens. Works such as ControlAR [29], ControlVAR [27], and CAR [63] incorporate spatial and pixel-level guidance—such as edges, segmentation masks, and depth maps—into the decoding process, enabling localized and structured control. Extensions like Training-Free VAR [58], M2M [48], and Instruct-imagen [20] further improve editing flexibility and broaden application scenarios. UniFluid [12] explores unified autoregressive generation and understanding with continuous visual tokens. However, due to reliance on discrete tokens and sequence length constraints, AR models often struggle to produce high-resolution and photorealistic results, especially in complex scenes.

**ZH** 自回归（AR）模型把图像建模为离散词元序列，在可控图像生成与编辑方面得到了积极研究。ControlAR [29]、ControlVAR [27]、CAR [63] 等工作把边缘、分割掩码、深度图等空间与像素级引导注入解码过程，实现了局部化、结构化的控制。Training-Free VAR [58]、M2M [48]、Instruct-imagen [20] 等扩展进一步提升了编辑灵活性并拓宽应用场景。UniFluid [12] 探索了用连续视觉词元实现统一的自回归生成与理解。然而，由于依赖离散词元且受序列长度约束，AR 模型往往难以产出高分辨率、照片级真实的结果，在复杂场景中尤其明显。

**EN** Diffusion models have become the dominant approach for high-fidelity image synthesis, offering strong capabilities in photorealism, structural consistency, and diversity. Beginning with DDPM [19] and DDIM [51], and further advanced by Latent Diffusion [47, 42], diffusion models operate in latent spaces for improved scalability. With the introduction of DiT architectures [41], diffusion models have made significant strides in generalization, image quality, and knowledge capacity, becoming the predominant architecture in modern image generation [1, 5, 7]. Based on the above text2image models, ControlNet [67], and T2I-Adapter [36] inject spatial or task-specific control into the generation process. BrushNet [23], PowerPaint [73], and FLUX-Fill [6] further improve inpainting quality and versatility. Despite these advances, diffusion models often rely on static prompts or fixed conditions and lack the capacity for multi-turn reasoning or flexible language alignment, limiting their application in open-ended editing scenarios.

**ZH** 扩散模型已成为高保真图像合成的主流路线，在照片真实感、结构一致性与多样性上能力突出。从 DDPM [19]、DDIM [51] 起步，再由潜扩散 [47, 42] 推进，扩散模型在潜空间中运作以获得更好的可扩展性。随着 DiT 架构 [41] 的引入，扩散模型在泛化性、图像质量与知识容量上取得长足进步，成为现代图像生成中的主流架构 [1, 5, 7]。在上述文生图模型的基础上，ControlNet [67] 与 T2I-Adapter [36] 把空间或任务特定的控制注入生成过程；BrushNet [23]、PowerPaint [73]、FLUX-Fill [6] 进一步提升了图像修复的质量与通用性。尽管有这些进展，扩散模型往往依赖静态提示或固定条件，缺乏多轮推理或灵活语言对齐的能力，限制了其在开放式编辑场景中的应用。

**EN** These limitations have led to growing interest in unified image editing frameworks that combine the symbolic control of AR models with the generative fidelity of diffusion. Such models aim to tightly couple instruction understanding, spatial reasoning, and photorealistic synthesis within a single architecture, offering more flexible, general, and user-controllable editing capabilities.

**ZH** 这些局限引发了人们对统一图像编辑框架的与日俱增的兴趣——把 AR 模型的符号化控制与扩散模型的生成保真度结合起来。这类模型力图在单一架构内把指令理解、空间推理与照片级真实合成紧密耦合，从而提供更灵活、更通用、更可由用户掌控的编辑能力。

**EN** 2.2 Instruction-based Image Editing Models

**ZH** 2.2 基于指令的图像编辑模型

**EN** Instruction-based image editing models aim to bridge semantic instruction understanding and precise visual manipulation. Early approaches such as InstructEdit [55], InstructPix2Pix [8], MagicBrush [66], and BrushEdit [28] adopt modular pipelines where MLLMs generate prompts, spatial cues, or synthetic instruction-image pairs to guide diffusion-based editing.

**ZH** 基于指令的图像编辑模型力图打通语义指令理解与精确的视觉操控。InstructEdit [55]、InstructPix2Pix [8]、MagicBrush [66]、BrushEdit [28] 等早期工作采用模块化流水线，由 MLLM 生成提示、空间线索或合成的指令—图像对，用以引导基于扩散的编辑。

**EN** Recent works move toward tighter integration between instruction and generation. SmartEdit [21], X2I [33], RPG [62], AnyEdit [64], and UltraEdit [71] enhance multimodal interaction and instruction fidelity through improved model architectures, task-aware routing, and fine-grained editing capabilities. Meanwhile, unified generation and editing frameworks such as OmniGen [61], ACE [16], ACE++[34], and Lumina-OmniLV[43] consolidate diverse visual tasks under a single architecture. Methods like Qwen2VL-Flux [31], DreamEngine [9] and MetaQueries [39] further explore efficient control integration and direct latent-level fusion between MLLMs and diffusion decoders. Moreover, Hidream-E1 [17] incorporates instructions and edited image descriptions as inputs, enabling more detailed edit information. Additionally, some researchers focus on more efficient methods to ensure editing performance while reducing training costs. For example, ICEdit [70] employs LoRA-MoE hybrid tuning and identifies better initial noise distributions, while SuperEdit [35] uses higher-quality training data and introduces contrastive supervision signals.

**ZH** 近期工作转向指令与生成之间更紧密的耦合。SmartEdit [21]、X2I [33]、RPG [62]、AnyEdit [64]、UltraEdit [71] 通过改进模型架构、任务感知路由与细粒度编辑能力，增强了多模态交互与指令保真度。与此同时，OmniGen [61]、ACE [16]、ACE++ [34]、Lumina-OmniLV [43] 等统一生成与编辑框架把多种视觉任务整合到单一架构之下。Qwen2VL-Flux [31]、DreamEngine [9]、MetaQueries [39] 等方法进一步探索高效的控制注入，以及 MLLM 与扩散解码器之间直接的潜层融合。此外，Hidream-E1 [17] 把指令与被编辑图像的描述一并作为输入，从而提供更细致的编辑信息。还有一些研究者关注在降低训练成本的同时保证编辑性能的更高效方法：例如 ICEdit [70] 采用 LoRA-MoE 混合微调并识别出更优的初始噪声分布，SuperEdit [35] 则使用更高质量的训练数据并引入对比监督信号。

**EN** More generally, models such as Gemini [15] and GPT-4o [37] demonstrate strong visual fluency through joint vision-language training, showing promising capabilities in understanding and generating consistent, context-aware images. Collectively, these developments reflect a shift from loosely coupled systems toward tightly integrated, instruction-driven editing frameworks.

**ZH** 更广泛地说，Gemini [15] 与 GPT-4o [37] 等模型通过视觉—语言联合训练展现出强大的视觉流畅性，在理解与生成一致、具备上下文感知的图像方面表现可期。这些进展共同反映出一条从松耦合系统走向紧耦合、指令驱动的编辑框架的转变。

**EN** However, existing approaches still face key limitations. Most methods are task-specific and lack general-purpose editability. They typically do not support incremental editing, fine-grained region correspondence, or instruction feedback refinement. Moreover, architectural coupling remains shallow in many designs, failing to unify instruction understanding and generation into a cohesive framework. These challenges motivate Step1X-Edit, which tightly integrates MLLM-based multimodal reasoning with diffusion-based controllable synthesis, enabling scalable, interactive, and instruction-faithful image editing across diverse editing goals.

**ZH** 然而，现有方法仍面临若干关键局限。多数方法面向特定任务，缺乏通用可编辑性；它们通常不支持增量编辑、细粒度区域对应或基于指令反馈的精修。此外，许多设计中的架构耦合仍然较浅，未能把指令理解与生成统一为一个有机整体。这些挑战催生了 Step1X-Edit：它把基于 MLLM 的多模态推理与基于扩散的可控合成紧密结合，从而在不同编辑目标下实现可扩展、可交互且忠实于指令的图像编辑。

**EN** 3 Step1X-Edit

**ZH** 3 Step1X-Edit

**EN** 3.1 Data Creation

**ZH** 3.1 数据构建

**EN** 3.1.1 Data Pipeline

**ZH** 3.1.1 数据流水线

<!-- [原子块 · object]  -->

**EN** Figure 2: Data Volume Comparison.

**ZH** 图 2：数据规模对比。

<!-- [原子块 · img]  -->

**EN** Figure 3: Data Construction Pipeline and Sub-Task Distribution.

**ZH** 图 3：数据构建流水线与子任务分布。

**EN** In the existing literature, current image editing datasets are constrained either by the scale or the quality of the collected data. To address this gap, this report endeavors to assemble a large-scale, high-quality dataset specifically tailored for image editing tasks.

**ZH** 在既有文献中，当前的图像编辑数据集要么受限于规模，要么受限于所采集数据的质量。为弥补这一缺口，本报告着力组装一个专为图像编辑任务定制的大规模高质量数据集。

**EN** We initiate the dataset collection process by web crawling a diverse set of image editing examples from the Internet. Through in-depth analysis of these examples, we systematically categorize the image editing problem into 11 distinct categories, which has been partly referenced by [64, 40]. These categories are designed to comprehensively encompass the vast majority of image editing requirements in practice. An overview of these 11 categories, along with the detailed data collection pipeline, is illustrated in Fig. 3.

**ZH** 我们先从互联网上爬取一组多样化的图像编辑样例，启动数据采集流程。通过对这些样例的深入分析，我们把图像编辑问题系统性地归为 11 个不同类别，其中部分参考了 [64, 40]。这些类别的设定力求全面覆盖实践中绝大多数图像编辑需求。这 11 个类别的概览与详细的数据采集流水线如图 3 所示。

**EN** To collect a large-scale high-quality triplets consisting of a source image, an editing instruction, and a target image, we designed a sophisticated data pipeline, which enabled us to generate over ⟦SLOT_2⟧ million instruction-images triplets. Following rigorous filtering using both Multimodal LLMs, e.g. step-1o [52], and human annotators, we retained more than ⟦SLOT_3⟧ million high-quality triplets. In Fig. 2, we present a side-by-side comparison of all existing editing datasets [13, 14, 74, 59, 65, 53, 22, 66, 2, 64]. Our Step1X-Edit dataset surpasses all others in scale. Even after a rigorous filtering process (with a retention ratio of 20:1), the Step1X-Edit-HQ subset remains on par with other datasets in terms of absolute magnitude. The full data collection pipeline for each subtask is outlined below.

**ZH** 为采集由源图像、编辑指令与目标图像构成的大规模高质量三元组，我们设计了一套精密的数据流水线，据此生成了超过 ⟦SLOT_2⟧ 百万条指令—图像三元组。经 step-1o [52] 等多模态大语言模型与人工标注者的严格筛选，我们保留了 ⟦SLOT_3⟧ 百万余条高质量三元组。图 2 给出了与所有现有编辑数据集 [13, 14, 74, 59, 65, 53, 22, 66, 2, 64] 的并排对比，Step1X-Edit 数据集在规模上超越所有对手；即便经过严格筛选（留存比 20:1），Step1X-Edit-HQ 子集在绝对量级上仍与其他数据集相当。各子任务完整的数据采集流水线如下。

**EN** Subject Addition & Removal: For subject-add and subject-remove tasks, we begin by annotating our proprietary dataset using Florence-2 [60], which supports diverse semantic granularities, spatial hierarchies, and annotation types such as object detection and classification. We then apply SAM-2 [46] for segmentation and use ObjectRemovalAlpha [30] to perform inpainting. Editing instructions are generated using a combination of Step-1o model [52] and GPT-4o, followed by manual review to ensure data validity.

**ZH** 主体添加与移除： 对于主体添加与主体移除任务，我们先用 Florence-2 [60] 对自有数据集作标注，该模型支持多样的语义粒度、空间层级以及目标检测与分类等标注类型；随后用 SAM-2 [46] 作分割，并用 ObjectRemovalAlpha [30] 执行图像修复。编辑指令由 Step-1o 模型 [52] 与 GPT-4o 组合生成，再经人工复核以确保数据有效。

**EN** Subject Replacement & Background Change: This category shares similar preprocessing steps with subject-add/remove, including Florence-2 [60] annotation and SAM-2 [46] segmentation. However, for these tasks, we utilize Qwen2.5-VL [3] and the Recognize-Anything Model [69] to identify target objects or keywords, followed by Flux-Fill [6] for content-aware inpainting. The instructions are automatically generated by Step-1o and the triplets are human-verified.

**ZH** 主体替换与背景更换： 该类别与主体添加／移除共享相似的预处理步骤，包括 Florence-2 [60] 标注与 SAM-2 [46] 分割。但对这两类任务，我们使用 Qwen2.5-VL [3] 与 Recognize-Anything Model [69] 来识别目标对象或关键词，随后用 Flux-Fill [6] 作内容感知的图像修复。指令由 Step-1o 自动生成，三元组经人工核验。

**EN** Color Alteration & Material Modification: After detecting objects in the image, we employ Zeodepth [4] for depth estimation to understand object geometry. Based on the identified target transformation (e.g., change of color or material), we use ControlNet [67] with diffusion model [1] to generate new images that preserve object identity while altering appearance attributes such as texture or color.

**ZH** 颜色更改与材质修改： 检测到图像中的对象后，我们用 Zeodepth [4] 作深度估计以理解物体几何形态。根据识别出的目标变换（例如换色或换材质），我们用 ControlNet [67] 配合扩散模型 [1] 生成新图像，在改变纹理或颜色等外观属性的同时保留对象身份。

**EN** Text Modification: For text-editing tasks, we differentiate between valid and invalid text edits. We use PPOCR [10], which focuses on recognizing correct characters, alongside the Step-1o model to distinguish correct and incorrect regions of text. Based on this classification, we generate corresponding editing instructions. All outputs are finalized via human post-processing (e.g., manual retouching of text).

**ZH** 文字修改： 对于文字编辑任务，我们区分有效与无效的文字编辑。我们使用专注于正确字符识别的 PPOCR [10]，配合 Step-1o 模型来区分文字的正确与错误区域，据此生成相应的编辑指令。所有输出均经人工后处理（例如手工修整文字）定稿。

**EN** Motion Change: To handle motion-related transformations, we leverage videos from Koala-36M [56], extracting frame pairs as input. We use BiRefNet [72] and RAFT [54] for foreground-background separation and optical flow estimation. Specifically, we compute the mean of the foreground flow norm and the norm of the background flow mean, ensuring robustness in selecting pairs where only the foreground exhibits motion. Finally, GPT-4o is used to annotate the change in motion between frames as editing instructions.

**ZH** 动作变化： 为处理与动作相关的变换，我们利用 Koala-36M [56] 中的视频，抽取帧对作为输入；用 BiRefNet [72] 与 RAFT [54] 分别作前景—背景分离与光流估计。具体地，我们计算前景流范数的均值与背景流均值的范数，以稳健地筛选出只有前景发生运动的帧对。最后用 GPT-4o 标注帧间的动作变化，作为编辑指令。

**EN** Portrait Editing and Beautification: Data are collected and created by two major sources: (a) Beautification pairs from public sources. Faces are detected and passed through Step-1o to assess layout and background consistency. (b) Beautification of the human editor, we invite the human editor to conduct beatification on collected data. All data are manually validated.

**ZH** 人像编辑与美化： 数据由两个主要来源采集并构建：(a) 来自公开渠道的美化样本对——检测人脸后交由 Step-1o 评估其布局与背景的一致性；(b) 人工编辑者的美化——我们邀请人工编辑者对采集到的数据实施美化。所有数据均经人工校验。

**EN** Style Transfer: We handle stylization in two directions depending on the target visual domain: For styles such as Ghibli, ink painting, or 3D anime style, generating photorealistic images from stylized inputs yields better alignment. We extract edges from stylized images and generate realistic outputs using controlled diffusion model [67, 1]. Conversely, for styles like oil painting or pixel art, we begin with realistic images and generate stylized outputs using the same edge-to-image pipeline.

**ZH** 风格迁移： 我们依据目标视觉域，从两个方向处理风格化。对于吉卜力、水墨、3D 动画等风格，由风格化输入生成照片级真实图像能获得更好的对齐效果：我们从风格化图像中抽取边缘，用受控扩散模型 [67, 1] 生成真实感输出。反之，对于油画、像素艺术等风格，则从真实图像出发，用同一条边缘到图像的流水线生成风格化输出。

**EN** Tone Transformation: This category focuses on global tonal adjustments, including color grading, dehazing, deraining, and seasonal transformations. These changes are largely driven by algorithmic tools and automated filters to simulate realistic environmental changes.

**ZH** 色调变换： 该类别关注全局色调调整，包括调色、去雾、去雨与季节变换。这些变化主要由算法工具与自动滤镜驱动，用以模拟真实的环境变化。

**EN** 3.1.2 Caption Strategy

**ZH** 3.1.2 标注策略

**EN** To obtain high-quality and fine-grained editing instruction–image pairs, we adopt the following annotation strategies:

**ZH** 为获得高质量、细粒度的编辑指令—图像对，我们采用如下标注策略：

**EN** Redundancy-Enhanced Annotation: Given the well-known limitations of Vision-Language Models (VLMs)—such as vague background descriptions and susceptibility to hallucinations—we employ a multi-round annotation strategy. Specifically, the annotation results from a previous round are fed into the next round as contextual input. This recursive refinement strengthens semantic consistency across annotations and significantly mitigates hallucination-related issues. Deterministic information is reinforced through repeated confirmations, ensuring higher reliability of the final annotation.

**ZH** 冗余增强标注： 鉴于视觉语言模型（VLM）存在背景描述含糊、易受幻觉影响等众所周知的问题，我们采用多轮标注策略——把上一轮的标注结果作为上下文输入馈入下一轮。这种递归式精化强化了标注之间的语义一致性，并显著缓解了与幻觉相关的问题；确定性信息通过反复确认得到加强，从而保证最终标注具有更高的可靠性。

**EN** Stylized Annotation via Contextual Examples: During the captioning process, we provide annotators (or models) with a large set of style-aligned examples as contextual references. These examples guide the tone, structure, and granularity of the captions, ensuring a consistent and stylized annotation format throughout the dataset.

**ZH** 借助上下文样例的风格化标注： 在撰写描述的过程中，我们向标注者（或模型）提供大量风格一致的样例作为上下文参照。这些样例引导描述的语气、结构与粒度，确保整个数据集的标注格式统一且风格一致。

**EN** Bilingual Annotation (Chinese-English): All our annotations are conducted bilingually, in both Chinese and English. This not only enhances accessibility and usability across different linguistic communities but also lays the groundwork for multilingual model training and evaluation.

**ZH** 中英双语标注： 我们所有的标注均以中文与英文双语进行。这既提升了在不同语言社群中的可用性与易用性，也为多语言模型训练与评测打下基础。

**EN** 3.2 Our Method

**ZH** 3.2 本文方法

<!-- [原子块 · img]  -->

**EN** Figure 4: Framework of Step1X-Edit. Step1X-Edit leverages the image understanding capabilities of MLLMs to parse editing instructions and generate editing tokens, which are then decoded into images using a DiT-based network.

**ZH** 图 4：Step1X-Edit 框架。Step1X-Edit 利用 MLLM 的图像理解能力解析编辑指令并生成编辑词元，再由基于 DiT 的网络将其解码为图像。

**EN** As illustrated in Fig. 4, our algorithm involves three key components: a Multimedia Large Language Model (MLLM), a connector module, and a Diffusion in Transformer (DiT) [41]. The input editing instruction, accompanied by the reference image, is first introduced to the MLLM; e.g., Qwen-VL [3] (hereafter abbreviated as Qwen). In conjunction with a system prefix, these inputs are jointly processed through a single forward pass of the MLLM, enabling the model to capture the semantic relationships between the instruction and the visual content. To isolate and emphasize the semantic elements relevant to the editing task, we selectively discard the token embeddings associated with the prefix. This filtering process retains only the token embeddings that directly align with the edit information, ensuring that subsequent processing focuses precisely on the editing requirements.

**ZH** 如图 4 所示，本算法包含三个关键组件：一个多模态大语言模型（MLLM）、一个连接模块，以及一个 Diffusion in Transformer（DiT）[41]。输入的编辑指令连同参考图像首先送入 MLLM（例如 Qwen-VL [3]，下文简称 Qwen）。这些输入与系统前缀一起，经 MLLM 单次前向传播联合处理，使模型得以捕捉指令与视觉内容之间的语义关系。为隔离并突出与编辑任务相关的语义元素，我们有选择地丢弃与前缀相关的词元嵌入；这一过滤过程只保留与编辑信息直接对应的词元嵌入，确保后续处理精确聚焦于编辑需求。

<!-- [原子块 · img]  -->

**EN** Figure 5: DiT module details.

**ZH** 图 5：DiT 模块细节。

**EN** The extracted embeddings are then fed into a lightweight connector module, such as the token refiner [32, 24]. This module restructures the embeddings into a more compact multimodal feature representation, which is subsequently used as the multimodal embedding input to the downstream DiT network. Furthermore, we calculate the mean of valid embeddings from Qwen. This mean value is then projected through a linear layer, generating a global guidance vector. By doing so, the image editing network can leverage Qwen’s enhanced semantic comprehension capabilities, enabling more accurate and context-aware editing operations.

**ZH** 抽取出的嵌入随后送入一个轻量连接模块，例如 token refiner [32, 24]。该模块把嵌入重组为更紧凑的多模态特征表示，作为多模态嵌入输入给下游 DiT 网络。此外，我们计算 Qwen 中有效嵌入的均值，并把该均值经一个线性层投影，生成一个全局引导向量。如此，图像编辑网络得以借助 Qwen 增强的语义理解能力，执行更准确、更具上下文感知的编辑操作。

**EN** To effectively train the Token Refiner and enable rich cross-modal conditioning, we carefully design our feature aggregation strategy. Compared to approaches such as FLUX-Fill [6], which uses channel concatenation, and methods like SeedEdit [50], which introduce additional causal self-attention mechanisms, we follow OminiControl [53] and adopt token concatenation to better balance responsiveness to editing instructions with the preservation of fine-grained image details. During training, the reference image is encoded by a VAE encoder, and its latent features are linearly projected into reference image tokens. As illustrated in Fig. 5, the image tokens (highlighted in the green box) are concatenated with noise image tokens along the token length dimension to construct the final visual input.

**ZH** 为有效训练 Token Refiner 并实现丰富的跨模态条件注入，我们精心设计特征聚合策略。FLUX-Fill [6] 采用通道拼接，SeedEdit [50] 等方法引入额外的因果自注意力机制；与之不同，我们遵循 OminiControl [53] 采用词元拼接，以更好地兼顾对编辑指令的响应能力与细粒度图像细节的保留。训练时，参考图像由 VAE 编码器编码，其潜特征经线性投影成为参考图像词元。如图 5 所示，图像词元（绿色框标示）与噪声图像词元沿词元长度维度拼接，构成最终的视觉输入。

**EN** Recent research has also explored alternative approaches to enhance cross-model understanding by leveraging MLLMs. For instance, Qwen2VL-FLUX [31] introduces a pioneering approach by replacing the traditional T5 [45] text encoder in DiT-based text-to-image models with MLLMs to enhance multi-modal understanding and generation. However, it still retains T5 [45] for text encoding, which limits its ability to perform comprehensive cross-modal reasoning. In contrast, approaches like DreamEngine [9] leverage Qwen to align image and text modalities, with their features serving as external conditional inputs for SD3.5 [1] in the image synthesis. This method establishes a shared representation space that facilitates a more coherent process of generation and understanding. Nevertheless, in DreamEngine, the challenge remains in fully capturing the fine-grained details of reference images using only MLLM features.

**ZH** 近期研究也探索了借助 MLLM 增强跨模型理解的其他路径。例如 Qwen2VL-FLUX [31] 开创性地把基于 DiT 的文生图模型中的传统 T5 [45] 文本编码器替换为 MLLM，以增强多模态理解与生成；但它仍保留 T5 [45] 作文本编码，限制了其执行全面跨模态推理的能力。相比之下，DreamEngine [9] 等方法利用 Qwen 对齐图像与文本模态，其特征作为 SD3.5 [1] 图像合成的外部条件输入，建立起共享表示空间，使生成与理解的过程更为连贯。然而在 DreamEngine 中，仅凭 MLLM 特征充分捕捉参考图像的细粒度细节这一难题依然存在。

**EN** Compared to these approaches, our model not only retains cross-modal understanding but also enhances the extraction of image details. By combining structured visual-language guidance, detailed visual condition, and strong pretrained backbones within a unified framework, our method significantly boosts the system’s capability to perform high-fidelity, semantically aligned image edits across a diverse range of user instructions. During training, we jointly optimize the connector and the downstream DiT using only the diffusion loss, following the rectified flow [11] formulation. Moreover, our method ensures stable training without relying on the mask loss trick, which distinguishes it from OmniGen [61]. The learning rate is fixed at ⟦SLOT_4⟧ to ensure a good trade-off between training stability and convergence speed.

**ZH** 与这些方法相比，我们的模型既保留了跨模态理解，又强化了对图像细节的提取。通过在统一框架内结合结构化的视觉—语言引导、细致的视觉条件与强大的预训练骨干，本方法显著提升了系统在多样化用户指令下执行高保真、语义对齐编辑的能力。训练时，我们仅用扩散损失（遵循 rectified flow [11] 的形式化）联合优化连接器与下游 DiT。此外，本方法无需依赖掩码损失技巧即可稳定训练，这一点区别于 OmniGen [61]。学习率固定为 ⟦SLOT_4⟧，以在训练稳定性与收敛速度之间取得良好折中。

**EN** 4 Benchmark and Evaluation

**ZH** 4 基准与评测

**EN** 4.1 GEdit(Genuine Edit)-Bench

**ZH** 4.1 GEdit（Genuine Edit）-Bench

**EN** To evaluate the performance of the image editing models, we collect a new benchmark called GEdit(Genuine Edit)-Bench. The main motivation of the benchmark is to collect the real-world user editing instances in order to evaluate how the existing editing algorithms can be suffice for the practical editing instructions. More specifically, we collect more than 1K user editing instances from the Internet, e.g., reddit, and manually split these editing instructions into the ⟦SLOT_5⟧ categories. To keep the diversity of the benchmark, we filter those editing instructions with similar purpose. Finally, we obtain 606 testing examples whose reference images are from the real-world cases which make it more genuine for the applications. Based on GEdit-Bench, we evaluate the existing open-source image editing algorithms like ACE++ and AnyEdit, as well as the closed-source algorithms like GPT-4o and Gemini2 Flash.

**ZH** 为评测图像编辑模型的性能，我们采集了一个名为 GEdit（Genuine Edit）-Bench 的新基准。构建该基准的主要动机是收集真实世界的用户编辑实例，用以评估现有编辑算法在多大程度上能够满足实用编辑指令。具体地，我们从互联网（如 reddit）收集了 1K 余条用户编辑实例，并把这些编辑指令人工划分到 ⟦SLOT_5⟧ 个类别中。为保持基准的多样性，我们剔除了目的相似的编辑指令，最终得到 606 条测试样本，其参考图像均取自真实案例，使评测更贴近实际应用。基于 GEdit-Bench，我们评测了 ACE++、AnyEdit 等现有开源图像编辑算法，以及 GPT-4o、Gemini2 Flash 等闭源算法。

<!-- [原子块 · img]  -->

**EN** Figure 6: De-Identification Process.

**ZH** 图 6：去标识化流程。

<!-- [原子块 · svg]  -->

**EN** (a) VIEScore for the Intersection-subset.

**ZH** (a) 交集子集上的 VIEScore。

<!-- [原子块 · svg]  -->

**EN** (b) VIEScore for the Full set.

**ZH** (b) 全集上的 VIEScore。

<!-- [原子块 · svg]  -->

**EN** (c) VIEScore for the Intersection-subset.

**ZH** (c) 交集子集上的 VIEScore。

<!-- [原子块 · svg]  -->

**EN** (d) VIEScore for the Full set.

**ZH** (d) 全集上的 VIEScore。

**EN** Figure 7: VIEScore of Each Sub-task in GEdit-Bench. All the results are evaluated by GPT-4o.

**ZH** 图 7：GEdit-Bench 中各子任务的 VIEScore。所有结果由 GPT-4o 评测。

<!-- [原子块 · table] Benchmarks Size Real Image Genuine Instruction Human Filtering #Sub-tasks Public Availability EditBench [ 57 ] 240 ✓ ✗ ✗ 1 ✓ EmuEdit [ 49 ] 3,055 ✓ ✗ ✗ 7 ✓ HIVE [ 68 ] 1,000 ✓ ✗ ✓ 1 ✓ HQ-Eidt [ 22 ] 1 -->

**EN** Table 1: Key Attributes of Open-source Edit Benchmarks. The reliance of existing open-source benchmarks on synthetic user inputs and minimal human involvement highlights the necessity of our proposed GEdit-Bench.

**ZH** 表 1：开源编辑基准的关键属性。现有开源基准依赖合成的用户输入、人工参与极少，这凸显了我们所提 GEdit-Bench 的必要性。

**EN** To safeguard privacy, a comprehensive de-identification protocol was meticulously implemented for all user-uploaded images prior to their utilization within the benchmarking framework as shown in Fig. 6. For each individual original image, a multi-faceted reverse image search strategy was employed, spanning across multiple public search engines. This process aimed to identify publicly accessible alternative images that demonstrated both visual similarity and semantic consistency with the original one, thereby aligning seamlessly with the corresponding editing instructions. In instances where public image alternatives could not be procured through this search methodology, a systematic approach to modifying the editing instructions was adopted. These modifications were carefully calibrated to maintain the highest degree of fidelity between the anonymized image-instruction example and the original user intents. This approach not only ensures the ethical integrity of the benchmark dataset but also preserves the essential characteristics required for accurate and meaningful evaluation of image editing models.

**ZH** 为保护隐私，我们在把用户上传图像纳入基准之前，对所有图像严格实施了一套完整的去标识化协议，如图 6 所示。对每一张原始图像，我们采用跨多个公共搜索引擎的多路反向图像检索策略，旨在找到与该图像在视觉上相似、语义上一致，且公开可获取的替代图像，从而与相应的编辑指令无缝契合。在通过检索无法获得公开替代图像的情形下，则采取系统化的编辑指令修改方案；这些修改经过精心校准，使匿名化后的图像—指令样例与原用户意图之间保持最高程度的忠实。该方案既确保了基准数据集的伦理正当性，也保留了对图像编辑模型作准确、有意义的评测所必需的本质特征。

<!-- [原子块 · table] Model GEdit-Bench-EN (Intersection subset) ↑ \uparrow GEdit-Bench-EN (Full set) ↑ \uparrow G_SC G_PQ G_O Q_SC Q_PQ Q_O G_SC G_PQ G_O Q_SC Q_PQ Q_O Instruct-Pix2Pix [ 8 ] 3.335 6.210 3.234 4.833 6.992  -->

**EN** Table 2: Quantitative evaluation on GEdit-Bench-EN. All metrics are reported as higher-is-better (⟦SLOT_6⟧). The Intersection subset reflects the subset of prompts where all methods return valid responses with a total of 434 instances; the Full set includes all the 606 instances. G_SC, G_PQ, and G_O refer to the metrics evaluated by GPT-4.1, while Q_SC, Q_PQ, and Q_O refer to the metrics evaluated by Qwen2.5-VL-72B.

**ZH** 表 2：GEdit-Bench-EN 上的定量评测。所有指标均为越高越好（⟦SLOT_6⟧）。交集子集指所有方法均返回有效响应的提示子集，共 434 条；全集包含全部 606 条样本。G_SC、G_PQ、G_O 指由 GPT-4.1 评测的指标，Q_SC、Q_PQ、Q_O 指由 Qwen2.5-VL-72B 评测的指标。

<!-- [原子块 · table] Model GEdit-Bench-CN (Intersection subset) ↑ \uparrow GEdit-Bench-CN (Full set) ↑ \uparrow G_SC G_PQ G_O Q_SC Q_PQ Q_O G_SC G_PQ G_O Q_SC Q_PQ Q_O Gemini [ 15 ] 5.316 7.571 5.208 5.658 7.372 5.566 5.2 -->

**EN** Table 3: Quantitative evaluation on GEdit-Bench-CN. All metrics are reported as higher-is-better (⟦SLOT_7⟧). The Intersection subset reflects the subset of prompts where all methods return valid responses with a total of 422 instances; the Full set includes all the 606 instances. G_SC, G_PQ, and G_O refer to the metrics evaluated by GPT-4.1, while Q_SC, Q_PQ, and Q_O refer to the metrics evaluated by Qwen2.5-VL-72B.

**ZH** 表 3：GEdit-Bench-CN 上的定量评测。所有指标均为越高越好（⟦SLOT_7⟧）。交集子集指所有方法均返回有效响应的提示子集，共 422 条；全集包含全部 606 条样本。G_SC、G_PQ、G_O 指由 GPT-4.1 评测的指标，Q_SC、Q_PQ、Q_O 指由 Qwen2.5-VL-72B 评测的指标。

**EN** 4.2 Experimental Results

**ZH** 4.2 实验结果

**EN** 4.2.1 Evaluation on GEdit-Bench

**ZH** 4.2.1 在 GEdit-Bench 上的评测

**EN** Based on the GEdit-Bench, we evaluated a diverse range of image editing algorithms, covering state-of-the-art open-source solutions such as Instruct-Pix2Pix [8], MagicBrush [66], AnyEdit [64], OmniGen [61], as well as proprietary algorithms like GPT-4.1 [37]11 1 The results are obtained based on ChatGPT APP in April 2025., doubao [50]22 2 The results are obtained based on doubao APP in April 2025., and Gemini2 Flash [15]33 3 The results are obtained in April 2025.. Following VIEScore [25], we adopt three metrics: SQ (Semantic Consistency), PQ (Perceptual Quality), and O (Overall Score). SQ assesses the degree to which the edited results conform to the given editing instruction, with a score ranging from ⟦SLOT_8⟧ to ⟦SLOT_9⟧. PQ evaluates the naturalness of the image and the presence of artifacts, also using a scoring scale that ranges from ⟦SLOT_10⟧ to ⟦SLOT_11⟧. The overall score is calculated based on these evaluations. To perform the automatic evaluation for VIEScore, we adopt the state-of-art MLLM model GPT-4o44 4 API access as of June 2025. Also, the evaluation based on the open-source model Qwen2.5-VL-72B [3] is included for reproduction. To comprehensively assess model capabilities on different languages, each image in our benchmark is paired with one English (EN) and one Chinese (CN) instruction. For EN instructions (GEdit-Bench-EN), both closed and open-source models are evaluated. For CN instructions (GEdit-Bench-CN), only those models which supports Chinese prompts, i.e., the close-source systems, are tested. During the evaluation process, we find that close-source image editing system such as GPT-4o may refuse certain instructions due to safety policies. To address this issue, we report two scores for two testing sets: (1) Intersection Subset — the subset of images whose results can be successfully returned from all the tested models, and (2) Full set — all the testing samples from GEdit-Bench. For the full set of results, we will calculate the average scores only for the cases where the models successfully generate and return the target image. For each evaluated model, instances where no result image is returned due to reasons such as safety concerns will be excluded from the averaging process.

**ZH** 基于 GEdit-Bench，我们评测了多种图像编辑算法，涵盖 Instruct-Pix2Pix [8]、MagicBrush [66]、AnyEdit [64]、OmniGen [61] 等最先进的开源方案，以及 GPT-4.1 [37]11 1 结果基于 2025 年 4 月的 ChatGPT APP 获取。、doubao [50]22 2 结果基于 2025 年 4 月的 doubao APP 获取。与 Gemini2 Flash [15]33 3 结果于 2025 年 4 月获取。等闭源算法。依照 VIEScore [25]，我们采用三项指标：SQ（语义一致性）、PQ（感知质量）与 O（总体得分）。SQ 评估编辑结果符合给定编辑指令的程度，分数区间为 ⟦SLOT_8⟧ 到 ⟦SLOT_9⟧；PQ 评估图像的自然度与伪影情况，同样使用 ⟦SLOT_10⟧ 到 ⟦SLOT_11⟧ 的评分区间；总体得分基于这两项评估计算得出。为执行 VIEScore 自动评测，我们采用当前最先进的 MLLM 模型 GPT-4o44 4 API 访问时间截至 2025 年 6 月。同时纳入基于开源模型 Qwen2.5-VL-72B [3] 的评测结果，以便复现。为全面评估模型在不同语言上的能力，基准中每张图像都配有一条英文（EN）与一条中文（CN）指令。对英文指令（GEdit-Bench-EN），闭源与开源模型均参与评测；对中文指令（GEdit-Bench-CN），只测试支持中文提示的模型，即闭源系统。评测过程中我们发现，GPT-4o 等闭源图像编辑系统可能因安全策略拒绝某些指令。为此，我们针对两个测试集分别报告两个分数：(1) 交集子集——所有被测模型均能成功返回结果的那部分图像；(2) 全集——GEdit-Bench 的全部测试样本。在全集结果中，我们只对模型成功生成并返回目标图像的样本计算平均分；对每个被测模型，因安全等原因未返回结果的样本将从平均过程中剔除。

**EN** Fig. 7 demonstrates the groundbreaking capacity of Step1X-Edit, which outperforms open-source counterparts across 11 distinct evaluation axes. When compared to closed models, it surpasses Gemini2 Flash [15] and even beats GPT-4o [37] in axes such as style change and color alteration. As detailed in Tab. 2, Step1X-Edit significantly outperforms the existing open-source models like OmniGen [61] and has comparable results against the closed model like Gemini2 Flash and Doubao. Furthermore, as shown in Tab. 3, Step1X-Edit demonstrates consistent performance, even surpassing Gemini2 Flash and Doubao when handling the Chinese editing instructions in GEdit-Bench-CN benchmark. These results highlight the outstanding performance of our model across all dimensions with a unified architecture, eliminating the requirement for masks during the editing process. Fig. 8 and Fig. 9 provide illustrative examples for English instructions and Chinese instructions, respectively.

**ZH** 图 7 展示了 Step1X-Edit 的突破性能力：它在 11 个不同的评测维度上均优于同类开源模型。与闭源模型相比，它超越了 Gemini2 Flash [15]，甚至在风格变换、颜色更改等维度上胜过 GPT-4o [37]。如表 2 详列，Step1X-Edit 显著超越 OmniGen [61] 等现有开源模型，并与 Gemini2 Flash、Doubao 等闭源模型结果相当。此外，如表 3 所示，在 GEdit-Bench-CN 基准上处理中文编辑指令时，Step1X-Edit 表现稳定，甚至超越了 Gemini2 Flash 与 Doubao。这些结果凸显了本模型以统一架构在各维度上的出色表现，且在编辑过程中无需掩码。图 8 与图 9 分别给出英文指令与中文指令下的示例对比。

<!-- [原子块 · img]  -->

**EN** Figure 8: A Comparative Illustration of Open-Source Approaches and Commercial systems for English Editing Instructions.

**ZH** 图 8：开源方法与商业系统在英文编辑指令下的对比示例。

<!-- [原子块 · img]  -->

**EN** Figure 9: A Comparative Illustration of state-of-art algorithms for Chinese Editing Instructions.

**ZH** 图 9：当前最先进算法在中文编辑指令下的对比示例。

**EN** 4.2.2 User Study

**ZH** 4.2.2 用户研究

**EN** To assess the subjective quality of image editing results, we conduct a comprehensive user preference study built upon the GEdit-Bench. A total of 55 participants are recruited to evaluate the outputs of four algorithms—Gemini2 Flash [15], Doubao[50], GPT-4o [37], and our method, Step1X-Edit. Each participant is presented with a series of test images and asked to rank the editing results generated by the four methods. This evaluation is performed in a blinded and subjective setting to minimize bias and ensure fairness.

**ZH** 为评估图像编辑结果的主观质量，我们在 GEdit-Bench 之上开展了一项全面的用户偏好研究。共招募 55 名参与者，对 Gemini2 Flash [15]、Doubao [50]、GPT-4o [37] 与本文方法 Step1X-Edit 这四种算法的输出作出评价。每位参与者会看到一系列测试图像，并被要求对四种方法生成的编辑结果排序。评测在盲评的主观设定下进行，以尽量减少偏见、确保公平。

**EN** Participants rate the outputs using a five-level quality scale, ranging from worst to excellent. To facilitate consistent comparison with quantitative evaluation metrics such as VIEScores, we map these qualitative ratings to numerical scores: worst = ⟦SLOT_12⟧, poor = ⟦SLOT_13⟧, fair = ⟦SLOT_14⟧, good = ⟦SLOT_15⟧, and excellent = ⟦SLOT_16⟧. For each editing task, we compute the mean preference score across all participants. The overall performance of each method is then summarized by averaging the scores over all editing tasks.

**ZH** 参与者用从“最差”到“优秀”的五级质量量表为输出打分。为便于与 VIEScore 等定量评测指标作一致比较，我们把这些定性评级映射为数值分数：最差 = ⟦SLOT_12⟧、较差 = ⟦SLOT_13⟧、一般 = ⟦SLOT_14⟧、良好 = ⟦SLOT_15⟧、优秀 = ⟦SLOT_16⟧。对每个编辑任务，计算所有参与者偏好分数的均值；每种方法的总体表现则通过对所有编辑任务的分数取平均得到。

**EN** The results, presented in Tab. 4 and Fig. 10, highlight the effectiveness of Step1X-Edit. Notably, our method achieves comparable subjective quality to other state-of-the-art approaches, reinforcing its capability in producing visually pleasing and user-preferred edits. It is worth noting that Gemini2 Flash achieves an astonishingly high user preference score primarily attributed to its strong identity-preserving capabilities in the testing examples. This characteristic was more favored by the participants in the user study.

**ZH** 结果如表 4 与图 10 所示，凸显了 Step1X-Edit 的有效性。值得注意的是，本方法取得的主观质量与其他最先进方法相当，印证了它产出视觉上令人愉悦、为用户所偏好的编辑结果的能力。值得一提的是，Gemini2 Flash 取得了惊人的高用户偏好分，主要归功于其在测试样本中强大的身份保持能力——这一特性在用户研究中更受参与者青睐。

<!-- [原子块 · table] Model Gemini [ 15 ] Doubao [ 50 ] GPT-4o [ 37 ] Step1X-Edit UP-IS ( ↑ \uparrow ) 7.109 6.320 6.961 6.544 UP-Full ( ↑ \uparrow ) 6.603 5.678 7.134 6.939 -->

**EN** Table 4: Overall user preference (UP) evaluation on GEdit-Bench. UP-IS and UP-Full represent user preference score for Intersection subset (IS) and Full set (Full), respectively. All metrics are reported as higher-is-better (⟦SLOT_17⟧).

**ZH** 表 4：GEdit-Bench 上的总体用户偏好（UP）评测。UP-IS 与 UP-Full 分别表示交集子集（IS）与全集（Full）上的用户偏好分数。所有指标均为越高越好（⟦SLOT_17⟧）。

<!-- [原子块 · object]  -->

**EN** (a) User Preference score in the Intersection subset.

**ZH** (a) 交集子集上的用户偏好分数。

<!-- [原子块 · object]  -->

**EN** (b) User Preference score in the full subset.

**ZH** (b) 全集上的用户偏好分数。

**EN** Figure 10: User Preference score of Each Sub-task in GEdit-Bench.

**ZH** 图 10：GEdit-Bench 中各子任务的用户偏好分数。

**EN** 5 Conclusion

**ZH** 5 结论

**EN** In this report, we present a new general image editing algorithm called Step1X-Edit, which will be publicly released to foster further innovation and research within the image editing community. To train the model effectively, we propose a new data generation pipeline which can generate large-scale high-quality image editing triples, each consisting of a reference image, an editing instruction, and a corresponding target image. Based on the collected dataset, we train our Step1X-Edit model by seamlessly integrating powerful Multimedia Large Language Model with a diffusion-based image decoder. According to the evaluations on our collected GEdit-Bench, our proposed algorithm outperforms the existing open-source image editing algorithms with a substantial margin.

**ZH** 本报告提出了一个新的通用图像编辑算法 Step1X-Edit，并将公开发布，以促进图像编辑社区内的进一步创新与研究。为有效训练模型，我们提出了一套新的数据生成流水线，可生成大规模高质量图像编辑三元组，每条三元组由参考图像、编辑指令与对应的目标图像构成。基于所采集的数据集，我们把强大的多模态大语言模型与基于扩散的图像解码器无缝结合，训练出 Step1X-Edit 模型。根据在我们所构建的 GEdit-Bench 上的评测，本算法以显著优势超越了现有开源图像编辑算法。

**EN** Contributors and Acknowledgments

**ZH** 贡献者与致谢

**EN** We designate core contributors as those who have been involved in the development of Step1X-Edit throughout its entire process, while contributors are those who worked on the early versions or contributed part-time.

**ZH** 我们把全程参与 Step1X-Edit 开发的人列为核心贡献者，把参与早期版本或兼职投入的人列为贡献者。

**EN** Core Contributors: Shiyu Liu, Yucheng Han, Peng Xing, Fukun Yin, Rui Wang, Wei Cheng, Jiaqi Liao, Yingming Wang, Xianfang Zeng, Gang Yu.

**ZH** 核心贡献者：Shiyu Liu、Yucheng Han、Peng Xing、Fukun Yin、Rui Wang、Wei Cheng、Jiaqi Liao、Yingming Wang、Xianfang Zeng、Gang Yu。

**EN** Contributors: Honghao Fu, Ruoyu Wang, Yongliang Wu, Tianyu Wang, Haozhen Sun, Wen Sun, Bizhu Huang, Mei Chen, Kang An, Shuli Gao, Wei Ji, Tianhao You, Chunrui Han, Guopeng Li, Yuang Peng, Quan Sun, Jingwei Wu, Yan Cai, Zheng Ge, Ranchen Ming, Lei Xia, Yibo Zhu, Binxing Jiao, Xiangyu Zhang, Daxin Jiang.

**ZH** 贡献者：Honghao Fu、Ruoyu Wang、Yongliang Wu、Tianyu Wang、Haozhen Sun、Wen Sun、Bizhu Huang、Mei Chen、Kang An、Shuli Gao、Wei Ji、Tianhao You、Chunrui Han、Guopeng Li、Yuang Peng、Quan Sun、Jingwei Wu、Yan Cai、Zheng Ge、Ranchen Ming、Lei Xia、Yibo Zhu、Binxing Jiao、Xiangyu Zhang、Daxin Jiang。

**EN** Corresponding Authors: Xianfang Zeng(zengxianfang@stepfun.com), Gang Yu (yugang@stepfu n.com), Daxin Jiang (djiang@stepfun.com).

**ZH** 通讯作者：Xianfang Zeng（zengxianfang@stepfun.com）、Gang Yu（yugang@stepfu n.com）、Daxin Jiang（djiang@stepfun.com）。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] [1] Stability AI. Stable diffusion 3.5. https://huggingface.co/stabilityai/stable-diffusion-3.5-large , 2024. Accessed: 2025-04-17. -->

<!-- [原子块 · verbatim] [2] Jinbin Bai, Wei Chow, Ling Yang, Xiangtai Li, Juncheng Li, Hanwang Zhang, and Shuicheng Yan. Humanedit: A high-quality human-rewarded dataset for instruction-based image editing. arXiv preprint ar -->

<!-- [原子块 · verbatim] [3] Shuai Bai, Keqin Chen, Xuejing Liu, Jialin Wang, Wenbin Ge, Sibo Song, Kai Dang, Peng Wang, Shijie Wang, Jun Tang, et al. Qwen2. 5-vl technical report. arXiv preprint arXiv:2502.13923 , 2025. -->

<!-- [原子块 · verbatim] [4] Shariq Farooq Bhat, Reiner Birkl, Diana Wofk, Peter Wonka, and Matthias Müller. Zoedepth: Zero-shot transfer by combining relative and metric depth. arXiv preprint arXiv:2302.12288 , 2023. -->

<!-- [原子块 · verbatim] [5] Black Forest Labs. Flux.1 [dev]. https://huggingface.co/black-forest-labs/FLUX.1-dev , 2024. -->

<!-- [原子块 · verbatim] [6] Black Forest Labs. Flux.1 fill [dev]. https://huggingface.co/black-forest-labs/FLUX.1-Fill-dev , 2024. Accessed: 2025-04-19. -->

<!-- [原子块 · verbatim] [7] Black Forest Labs. Flux.1 [schnell]. https://huggingface.co/black-forest-labs/FLUX.1-schnell , 2024. -->

<!-- [原子块 · verbatim] [8] Tim Brooks, Aleksander Holynski, and Alexei A. Efros. Instructpix2pix: Learning to follow image editing instructions. 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) , p -->

<!-- [原子块 · verbatim] [9] Liang Chen, Shuai Bai, Wenhao Chai, Weichu Xie, Haozhe Zhao, Leon Vinci, Junyang Lin, and Baobao Chang. Multimodal representation alignment for image generation: Text-image interleaved control is  -->

<!-- [原子块 · verbatim] [10] Yuning Du, Chenxia Li, Ruoyu Guo, Xiaoting Yin, Weiwei Liu, Jun Zhou, Yifan Bai, Zilin Yu, Yehua Yang, Qingqing Dang, and Haoshuang Wang. Pp-ocr: A practical ultra lightweight ocr system. arXiv p -->

<!-- [原子块 · verbatim] [11] Patrick Esser, Sumith Kulal, Andreas Blattmann, Rahim Entezari, Jonas Müller, Harry Saini, Yam Levi, Dominik Lorenz, Axel Sauer, Frederic Boesel, et al. Scaling rectified flow transformers for hi -->

<!-- [原子块 · verbatim] [12] Lijie Fan, Luming Tang, Siyang Qin, Tianhong Li, Xuan Yang, Siyuan Qiao, Andreas Steiner, Chen Sun, Yuanzhen Li, Tao Zhu, et al. Unified autoregressive visual generation and understanding with co -->

<!-- [原子块 · verbatim] [13] Rongyao Fang, Chengqi Duan, Kun Wang, Linjiang Huang, Hao Li, Shilin Yan, Hao Tian, Xingyu Zeng, Rui Zhao, Jifeng Dai, Xihui Liu, and Hongsheng Li. Got: Unleashing reasoning capability of multimo -->

<!-- [原子块 · verbatim] [14] Yuying Ge, Sijie Zhao, Chen Li, Yixiao Ge, and Ying Shan. Seed-data-edit technical report: A hybrid dataset for instructional image editing. arXiv preprint arXiv:2405.04007 , 2024. -->

<!-- [原子块 · verbatim] [15] Google Gemini2. Experiment with gemini 2.0 flash native image generation, 2025. -->

<!-- [原子块 · verbatim] [16] Zhen Han, Zeyinzi Jiang, Yulin Pan, Jingfeng Zhang, Chaojie Mao, Chenwei Xie, Yu Liu, and Jingren Zhou. Ace: All-round creator and editor following instructions via diffusion transformer. arXiv p -->

<!-- [原子块 · verbatim] [17] HiDream-ai. Hidream-e1. https://github.com/HiDream-ai/HiDream-E1 , 2025. -->

<!-- [原子块 · verbatim] [18] HiDream-ai. Hidream-i1. https://github.com/HiDream-ai/HiDream-I1 , 2025. -->

<!-- [原子块 · verbatim] [19] Jonathan Ho, Ajay Jain, and Pieter Abbeel. Denoising diffusion probabilistic models. Advances in neural information processing systems , 33:6840–6851, 2020. -->

<!-- [原子块 · verbatim] [20] Hexiang Hu, Kelvin CK Chan, Yu-Chuan Su, Wenhu Chen, Yandong Li, Kihyuk Sohn, Yang Zhao, Xue Ben, Boqing Gong, William Cohen, et al. Instruct-imagen: Image generation with multi-modal instruction -->

<!-- [原子块 · verbatim] [21] Yuzhou Huang, Liangbin Xie, Xintao Wang, Ziyang Yuan, Xiaodong Cun, Yixiao Ge, Jiantao Zhou, Chao Dong, Rui Huang, Ruimao Zhang, and Ying Shan. Smartedit: Exploring complex instruction-based imag -->

<!-- [原子块 · verbatim] [22] Mude Hui, Siwei Yang, Bingchen Zhao, Yichun Shi, Heng Wang, Peng Wang, Yuyin Zhou, and Cihang Xie. Hq-edit: A high-quality dataset for instruction-based image editing. arXiv preprint arXiv:2404.0 -->

<!-- [原子块 · verbatim] [23] Xuan Ju, Xian Liu, Xintao Wang, Yuxuan Bian, Ying Shan, and Qiang Xu. Brushnet: A plug-and-play image inpainting model with decomposed dual-branch diffusion. In European Conference on Computer Vi -->

<!-- [原子块 · verbatim] [24] Weijie Kong, Qi Tian, Zijian Zhang, Rox Min, Zuozhuo Dai, Jin Zhou, Jiangfeng Xiong, Xin Li, Bo Wu, Jianwei Zhang, et al. Hunyuanvideo: A systematic framework for large video generative models. a -->

<!-- [原子块 · verbatim] [25] Max Ku, Dongfu Jiang, Cong Wei, Xiang Yue, and Wenhu Chen. Viescore: Towards explainable metrics for conditional image synthesis evaluation. arXiv preprint arXiv:2312.14867 , 2023. -->

<!-- [原子块 · verbatim] [26] Black Forest Labs. Flux. https://github.com/black-forest-labs/flux , 2024. -->

<!-- [原子块 · verbatim] [27] Xiang Li, Kai Qiu, Hao Chen, Jason Kuen, Zhe Lin, Rita Singh, and Bhiksha Raj. Controlvar: Exploring controllable visual autoregressive modeling. arXiv preprint arXiv:2406.09750 , 2024. -->

<!-- [原子块 · verbatim] [28] Yaowei Li, Yuxuan Bian, Xu Ju, Zhaoyang Zhang, Ying Shan, and Qiang Xu. Brushedit: All-in-one image inpainting and editing. ArXiv , abs/2412.10316, 2024. -->

<!-- [原子块 · verbatim] [29] Zongming Li, Tianheng Cheng, Shoufa Chen, Peize Sun, Haocheng Shen, Longjin Ran, Xiaoxin Chen, Wenyu Liu, and Xinggang Wang. Controlar: Controllable image generation with autoregressive models. I -->

<!-- [原子块 · verbatim] [30] lrzjason. Objectremovalalpha dataset. https://huggingface.co/datasets/lrzjason/ObjectRemovalAlpha , 2025. Accessed: 2025-04-19. -->

<!-- [原子块 · verbatim] [31] Pengqi Lu. Qwen2vl-flux: Unifying image and text guidance for controllable image generation, 2024. -->

<!-- [原子块 · verbatim] [32] Bingqi Ma, Zhuofan Zong, Guanglu Song, Hongsheng Li, and Yu Liu. Exploring the role of large language models in prompt encoding for diffusion models. In The Thirty-eighth Annual Conference on Neu -->

<!-- [原子块 · verbatim] [33] Jiancang Ma, Qirong Peng, Xu Guo, Chen Chen, H. Lu, and Zhenyu Yang. X2i: Seamless integration of multimodal understanding into diffusion transformer via attention distillation. ArXiv , abs/2503. -->

<!-- [原子块 · verbatim] [34] Chaojie Mao, Jingfeng Zhang, Yulin Pan, Zeyinzi Jiang, Zhen Han, Yu Liu, and Jingren Zhou. Ace++: Instruction-based image creation and editing via context-aware content filling. arXiv preprint ar -->

<!-- [原子块 · verbatim] [35] Li Ming, Gu Xin, Chen Fan, Xing Xiaoying, Wen Longyin, Chen Chen, and Zhu Sijie. Superedit: Rectifying and facilitating supervision for instruction-based image editing. arXiv preprint arXiv:2505. -->

<!-- [原子块 · verbatim] [36] Chong Mou, Xintao Wang, Liangbin Xie, Jing Zhang, Zhongang Qi, Ying Shan, and Xiaohu Qie. T2i-adapter: Learning adapters to dig out more controllable ability for text-to-image diffusion models. A -->

<!-- [原子块 · verbatim] [37] OpenAI. Introducing 4o image generation, 2025. -->

<!-- [原子块 · verbatim] [38] ostris. Flex.2-preview. https://huggingface.co/ostris/Flex.2-preview , 2025. -->

<!-- [原子块 · verbatim] [39] Xichen Pan, Satya Narayan Shukla, Aashu Singh, Zhuokai Zhao, Shlok Kumar Mishra, Jialiang Wang, Zhiyang Xu, Jiuhai Chen, Kunpeng Li, Felix Juefei-Xu, et al. Transfer between modalities with metaq -->

<!-- [原子块 · verbatim] [40] Yulin Pan, Xiangteng He, Chaojie Mao, Zhen Han, Zeyinzi Jiang, Jingfeng Zhang, and Yu Liu. Ice-bench: A unified and comprehensive benchmark for image creating and editing. arXiv preprint arXiv:25 -->

<!-- [原子块 · verbatim] [41] William Peebles and Saining Xie. Scalable diffusion models with transformers. In Proceedings of the IEEE/CVF international conference on computer vision , pages 4195–4205, 2023. -->

<!-- [原子块 · verbatim] [42] Dustin Podell, Zion English, Kyle Lacey, Andreas Blattmann, Tim Dockhorn, Jonas Müller, Joe Penna, and Robin Rombach. SDXL: Improving latent diffusion models for high-resolution image synthesis.  -->

<!-- [原子块 · verbatim] [43] Yuandong Pu, Le Zhuo, Kaiwen Zhu, Liangbin Xie, Wenlong Zhang, Xiangyu Chen, Pneg Gao, Yu Qiao, Chao Dong, and Yihao Liu. Lumina-omnilv: A unified multimodal framework for general low-level visio -->

<!-- [原子块 · verbatim] [44] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, et al. Learning transferable visual models from -->

<!-- [原子块 · verbatim] [45] Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter J. Liu. Exploring the limits of transfer learning with a unified text-to-text -->

<!-- [原子块 · verbatim] [46] Nikhila Ravi, Valentin Gabeur, Yuan-Ting Hu, Ronghang Hu, Chaitanya Ryali, Tengyu Ma, Haitham Khedr, Roman Rädle, Chloe Rolland, Laura Gustafson, Eric Mintun, Junting Pan, Kalyan Vasudev Alwala,  -->

<!-- [原子块 · verbatim] [47] Robin Rombach, A. Blattmann, Dominik Lorenz, Patrick Esser, and Björn Ommer. High-resolution image synthesis with latent diffusion models. 2022 IEEE/CVF Conference on Computer Vision and Pattern  -->

<!-- [原子块 · verbatim] [48] Ying Shen, Yizhe Zhang, Shuangfei Zhai, Lifu Huang, Joshua M Susskind, and Jiatao Gu. Many-to-many image generation with auto-regressive diffusion models. arXiv preprint arXiv:2404.03109 , 2024. -->

<!-- [原子块 · verbatim] [49] Shelly Sheynin, Adam Polyak, Uriel Singer, Yuval Kirstain, Amit Zohar, Oron Ashual, Devi Parikh, and Yaniv Taigman. Emu edit: Precise image editing via recognition and generation tasks. In Procee -->

<!-- [原子块 · verbatim] [50] Yichun Shi, Peng Wang, and Weilin Huang. Seededit: Align image re-generation to image editing. arXiv preprint arXiv:2411.06686 , 2024. -->

<!-- [原子块 · verbatim] [51] Jiaming Song, Chenlin Meng, and Stefano Ermon. Denoising diffusion implicit models. International Conference on Learning Representations (ICLR) , 2021. -->

<!-- [原子块 · verbatim] [52] StepFun. step-1o-turbo-vision. https://platform.stepfun.com/ , 2025. -->

<!-- [原子块 · verbatim] [53] Zhenxiong Tan, Songhua Liu, Xingyi Yang, Qiaochu Xue, and Xinchao Wang. Ominicontrol: Minimal and universal control for diffusion transformer. arXiv preprint arXiv:2411.15098 , 2024. -->

<!-- [原子块 · verbatim] [54] Zachary Teed and Jia Deng. Raft: Recurrent all-pairs field transforms for optical flow. In Computer Vision–ECCV 2020: 16th European Conference, Glasgow, UK, August 23–28, 2020, Proceedings, Part  -->

<!-- [原子块 · verbatim] [55] Qian Wang, Biao Zhang, Michael Birsak, and Peter Wonka. Instructedit: Improving automatic masks for diffusion-based image editing with user instructions. ArXiv , abs/2305.18047, 2023. -->

<!-- [原子块 · verbatim] [56] Qiuheng Wang, Yukai Shi, Jiarong Ou, Rui Chen, Ke Lin, Jiahao Wang, Boyuan Jiang, Haotian Yang, Mingwu Zheng, Xin Tao, Fei Yang, Pengfei Wan, and Di Zhang. Koala-36m: A large-scale video dataset  -->

<!-- [原子块 · verbatim] [57] Su Wang, Chitwan Saharia, Ceslee Montgomery, Jordi Pont-Tuset, Shai Noy, Stefano Pellegrini, Yasumasa Onoe, Sarah Laszlo, David J Fleet, Radu Soricut, et al. Imagen editor and editbench: Advancin -->

<!-- [原子块 · verbatim] [58] Yufei Wang, Lanqing Guo, Zhihao Li, Jiaxing Huang, Pichao Wang, Bihan Wen, and Jian Wang. Training-free text-guided image editing with visual autoregressive model. arXiv preprint arXiv:2503.23897 -->

<!-- [原子块 · verbatim] [59] Cong Wei, Zheyang Xiong, Weiming Ren, Xinrun Du, Ge Zhang, and Wenhu Chen. Omniedit: Building image editing generalist models through specialist supervision. arXiv preprint arXiv:2411.07199 , 202 -->

<!-- [原子块 · verbatim] [60] Bin Xiao, Haiping Wu, Weijian Xu, Xiyang Dai, Houdong Hu, Yumao Lu, Michael Zeng, Ce Liu, and Lu Yuan. Florence-2: Advancing a unified representation for a variety of vision tasks. In Proceedings -->

<!-- [原子块 · verbatim] [61] Shitao Xiao, Yueze Wang, Junjie Zhou, Huaying Yuan, Xingrun Xing, Ruiran Yan, Chaofan Li, Shuting Wang, Tiejun Huang, and Zheng Liu. Omnigen: Unified image generation. arXiv preprint arXiv:2409.1 -->

<!-- [原子块 · verbatim] [62] Ling Yang, Zhaochen Yu, Chenlin Meng, Minkai Xu, Stefano Ermon, and Bin Cui. Mastering text-to-image diffusion: Recaptioning, planning, and generating with multimodal llms. ArXiv , abs/2401.11708 -->

<!-- [原子块 · verbatim] [63] Ziyu Yao, Jialin Li, Yifeng Zhou, Yong Liu, Xi Jiang, Chengjie Wang, Feng Zheng, Yuexian Zou, and Lei Li. Car: Controllable autoregressive modeling for visual generation. arXiv preprint arXiv:241 -->

<!-- [原子块 · verbatim] [64] Qifan Yu, Wei Chow, Zhongqi Yue, Kaihang Pan, Yang Wu, Xiaoyang Wan, Juncheng Li, Siliang Tang, Hanwang Zhang, and Yueting Zhuang. Anyedit: Mastering unified high-quality image editing for any id -->

<!-- [原子块 · verbatim] [65] Yongsheng Yu, Ziyun Zeng, Hang Hua, Jianlong Fu, and Jiebo Luo. Promptfix: You prompt and we fix the photo. arXiv preprint arXiv:2405.16785 , 2024. -->

<!-- [原子块 · verbatim] [66] Kai Zhang, Lingbo Mo, Wenhu Chen, Huan Sun, and Yu Su. Magicbrush: A manually annotated dataset for instruction-guided image editing. Advances in Neural Information Processing Systems , 36:31428– -->

<!-- [原子块 · verbatim] [67] Lvmin Zhang, Anyi Rao, and Maneesh Agrawala. Adding conditional control to text-to-image diffusion models. 2023 IEEE/CVF International Conference on Computer Vision (ICCV) , pages 3813–3824, 2023 -->

<!-- [原子块 · verbatim] [68] Shu Zhang, Xinyi Yang, Yihao Feng, Can Qin, Chia-Chih Chen, Ning Yu, Zeyuan Chen, Huan Wang, Silvio Savarese, Stefano Ermon, et al. Hive: Harnessing human feedback for instructional visual editin -->

<!-- [原子块 · verbatim] [69] Youcai Zhang, Xinyu Huang, Jinyu Ma, Zhaoyang Li, Zhaochuan Luo, Yanchun Xie, Yuzhuo Qin, Tong Luo, Yaqian Li, Shilong Liu, et al. Recognize anything: A strong image tagging model. arXiv preprint -->

<!-- [原子块 · verbatim] [70] Zechuan Zhang, Ji Xie, Yu Lu, Zongxin Yang, and Yi Yang. In-context edit: Enabling instructional image editing with in-context generation in large scale diffusion transformer. arXiv , 2025. -->

<!-- [原子块 · verbatim] [71] Haozhe Zhao, Xiaojian Shawn Ma, Liang Chen, Shuzheng Si, Rujie Wu, Kaikai An, Peiyu Yu, Minjia Zhang, Qing Li, and Baobao Chang. Ultraedit: Instruction-based fine-grained image editing at scale.  -->

<!-- [原子块 · verbatim] [72] Peng Zheng, Dehong Gao, Deng-Ping Fan, Li Liu, Jorma Laaksonen, Wanli Ouyang, and Nicu Sebe. Bilateral reference for high-resolution dichotomous image segmentation. CAAI Artificial Intelligence R -->

<!-- [原子块 · verbatim] [73] Junhao Zhuang, Yanhong Zeng, Wenran Liu, Chun Yuan, and Kai Chen. A task is worth one word: Learning with task prompts for high-quality versatile image inpainting. In European Conference on Compu -->

<!-- [原子块 · verbatim] [74] Bojia Zi, Penghui Ruan, Marco Chen, Xianbiao Qi, Shaozhe Hao, Shihao Zhao, Youze Huang, Bin Liang, Rong Xiao, and Kam-Fai Wong. Señorita-2m: A high-quality instruction-based dataset for general v -->
