# AesthetiQ：通过多模态大语言模型的美学感知偏好对齐增强图形版面设计

> 原标题：AesthetiQ: Enhancing Graphic Layout Design via Aesthetic-Aware Preference Alignment of Multi-modal Large Language Models
> 作者：Sohan Patnaik, Rishabh Jain, Balaji Krishnamurthy, Mausoom Sarkar · arXiv:2503.00591 · 2025-03-01

<!-- [原子块 · verbatim] AesthetiQ : Enhancing Graphic Layout Design via Aesthetic-Aware Preference Alignment of Multi-modal Large Language Models -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] Visual layouts are essential in graphic design fields such as advertising, posters, and web interfaces. The application of generative models for content-aware layout generation has recently gained tra -->

**EN** 1 Introduction

**ZH** 1 引言

<!-- [原子块 · img]  -->

**EN** Figure 1: Existing cross-entropy loss based methods penalize element misalignment heavily while preferential tuning via AAPA better capture aesthetic nuances in layouts

**ZH** 图 1：现有基于交叉熵损失的方法会对元素错位施以重罚，而通过 AAPA 进行的偏好式微调能更好地捕捉版面中的美学细微差别。

**EN** The arrangement of visual elements for a graphic layout significantly impacts how users perceive and interact with digital content [24]. The growing demand for automated design solutions demonstrates broad impact across multiple domains, including poster design [51, 20], user interface design [11, 21], document layouts [56, 51], and presentation slides [14]. Designers expect layouts to achieve dual-level harmony, creating a seamless blend of fine-grained design elements - color, font, and layout - while ensuring they work cohesively with different types of elements in the overall design [18]. These fine-grained components must maintain aesthetic integrity and enhance the design’s collective harmony. For instance, when examining basic design elements, colors must strike a delicate balance between contrast and cooperation, delivering visual style.

**ZH** 视觉元素在图形版面中的排布方式，深刻影响用户感知与交互数字内容的方式 [24]。自动设计解决方案需求的增长，其影响已辐射到多个领域，包括海报设计 [51, 20]、用户界面设计 [11, 21]、文档版面 [56, 51] 与演示幻灯片 [14]。设计者期待版面达到双重层面的和谐：既让颜色、字体、版式等细粒度设计元素无缝融合，又保证它们与整体设计中的各类元素协调一致 [18]。这些细粒度要素必须保持美学上的完整性，并提升设计的整体和谐感。以基本设计元素为例，颜色需要在对比与协同之间取得微妙平衡，才能传达出视觉风格。

**EN** As digital content creation accelerates, the field of automated layout generation has evolved across multiple directions. Research has progressed from unconditional generation [2, 16, 21, 27, 51] to more sophisticated approaches, including conditional generation based on user inputs (such as element types [22, 23, 24], sizes [23, 27], or relationships [22, 24]), conditional refinement using coarse attributes [42], and conditional completion with partially available elements [16]. Recently, Multi-modal Large Language Models (MLLMs) have demonstrated remarkable capabilities in spatial reasoning and visual-semantic understanding [9, 31, 37]. Their ability to process both textual and visual information enables them to capture complex spatial relationships and translate challenging language concepts into coherent layout arrangements. Current approaches [44, 52, 46] primarily reduce the complex design problem to a numeric representation, where each design element is simplified to a tuple ⟦SLOT_0⟧ encoding its center coordinates, width, and height. While both autoregressive models and diffusion models [55, 1, 7] approach layout generation differently-the former through sequential prediction and the latter through denoising-they share a fundamental limitation: both treat layouting as an optimization problem over position representations. As illustrated in Fig.1, when multiple layouts are aesthetically pleasing, optimizing based on the absolute numerical position through cross-entropy-based loss incorrectly penalizes other alternative layouts predicted by the model, thus enforcing incorrect understanding. Moreover, reducing visual elements to numerical values strips away critical design attributes, hierarchical relationships, and semantic context that human designers naturally consider. This reductionist approach fails to capture the aesthetics or visual appeal of the rendered layouts, particularly when dealing with complex layouts that require subtle aesthetic considerations and contextual awareness.

**ZH** 随着数字内容创作提速，自动版面生成领域沿着多个方向演进。研究已从无条件生成 [2, 16, 21, 27, 51] 推进到更精细的路线，包括基于用户输入的条件生成（如元素类型 [22, 23, 24]、尺寸 [23, 27] 或关系 [22, 24]）、利用粗粒度属性的条件精修 [42]，以及在部分元素已知条件下的条件补全 [16]。近来，多模态大语言模型（MLLM）在空间推理与视觉语义理解上展现出可观的能力 [9, 31, 37]。它们能同时处理文本与视觉信息，因而可以捕捉复杂的空间关系，并把有难度的语言概念转译为连贯的版面排布。现有方法 [44, 52, 46] 主要把复杂的设计问题简化为数值表示，每个设计元素被压缩成一个元组 ⟦SLOT_0⟧，编码其中心坐标、宽度与高度。自回归模型与扩散模型 [55, 1, 7] 处理版面生成的路径不同——前者逐序预测，后者逐步去噪——但二者有一个共同的根本局限：都把排版视为在位置表示上的优化问题。如图 1 所示，当多个版面在美学上同样可取时，基于绝对数值位置、以交叉熵损失进行优化，会错误地惩罚模型预测出的其他可行版面，从而强加错误的理解。此外，把视觉元素简化为数值，会剥离掉人类设计师天然会考虑的关键设计属性、层级关系与语义上下文。这种还原论式的做法无法捕捉渲染后版面的美感或视觉吸引力，在处理需要细腻美学考量与上下文感知的复杂版面时尤甚。

**EN** To this end, we pose a fundamental research question: “Can we utilize aesthetic preferences to guide the training of MLLMs, thereby enhancing the visual impact of generated layouts?” While MLLMs demonstrate strong visual-semantic alignment capabilities, these are often underutilized when trained solely with supervised position loss per element, which enforces a single layout variation for each input. Although incorporating aesthetic awareness through rendered layouts and an aesthetic discriminator seems intuitive, creating a differentiable layout renderer and the discriminator is non-intuitive. Instead, we propose learning aesthetics by proxy through preference learning between multiple layouts, hypothesizing that this approach enables MLLMs to develop a deeper contextual and aesthetic understanding of design principles.

**ZH** 为此，我们提出一个根本性的研究问题：「能否利用美学偏好来指导 MLLM 的训练，从而增强所生成版面的视觉冲击力？」MLLM 虽然具备很强的视觉语义对齐能力，但在仅用逐元素监督位置损失训练时，这些能力往往未被充分利用，因为这种做法为每个输入强加单一版面变体。尽管通过渲染后的版面与美学判别器引入美学感知看似直观，但构造可微的版面渲染器与判别器并非易事。相反，我们提出通过在多个版面之间进行偏好学习来间接习得美学，并假设这一路径能让 MLLM 形成对设计原则更深层的上下文理解与美学理解。

**EN** In this paper, we introduce Aesthetic-Aware Preference Alignment (AAPA), a novel algorithm that extends Direct Preference Optimization (DPO) [41] for aesthetic-aware layout generation. AAPA creates multiple layout candidates and leverages an MLLM as a judge to rank them based on their aesthetics, thereby developing robust aesthetic preferences. To ensure reliable training, we implement a rigorous data filtering protocol using alignment and overlap metrics, guaranteeing the model learns preferences only from well-formed layouts. Additionally, we present a novel evaluation framework using MLLMs as aesthetic scorers, introducing the % win rate metric that measures how often model-generated layouts outperform ground-truth layouts aesthetically. This approach offers more direct quality assessment than traditional metrics like Intersection over Union (IoU) or Boundary Displacement Error (BDE) [26], which fail to capture subtle aesthetic considerations. Our main contributions can be summarized as follows:

**ZH** 本文提出美学感知偏好对齐（Aesthetic-Aware Preference Alignment, AAPA），这是一种面向美学感知版面生成、对直接偏好优化（DPO）[41] 加以扩展的新算法。AAPA 生成多个候选版面，并借助一个 MLLM 作为裁判按美学对他们排序，由此形成稳健的美学偏好。为保证训练可靠，我们实施了一套严格的数据过滤流程，使用对齐与重叠指标，确保模型只从结构良好的版面中学习偏好。此外，我们提出一种新的评测框架，用 MLLM 作为美学打分器，引入百分比胜率指标，衡量模型生成的版面在美学上优于真值版面的频率。相比交并比（IoU）或边界位移误差（BDE）[26] 等无法捕捉细微美学考量的传统指标，这一做法提供了更直接的质量评估。我们的主要贡献概括如下：

**EN** • We demonstrate that VLMs can effectively utilize their real-world knowledge and visual-semantic alignment capabilities to enhance layout prediction tasks.

**ZH** • 我们证明视觉语言模型可以有效运用其真实世界知识与视觉语义对齐能力来提升版面预测任务。

**EN** • We propose Aesthetic-Aware Preference Alignment, a novel method to improve aesthetics of generated layouts through preference-based learning.

**ZH** • 我们提出美学感知偏好对齐，一种基于偏好学习来改善生成版面美学质量的新方法。

**EN** • We highlight the importance of data filtering based on quality heuristics through alignment and overlap heuristics, ensuring robust training on high-quality samples.

**ZH** • 我们强调了基于质量启发式（对齐与重叠启发式）进行数据过滤的重要性，以保证在高质量样本上进行稳健训练。

**EN** • We develop a novel evaluation framework that assess layout aesthetics via MLLMs, providing more meaningful quality measurements than traditional metrics.

**ZH** • 我们设计了一种新的评测框架，通过 MLLM 评估版面美学，提供比传统指标更有意义的质量度量。

**EN** • We conduct extensive qualitative and quantitative analyses of each proposed component using two challenging benchmark datasets, Crello and WebUI, demonstrating the effectiveness of our approach across diverse settings.

**ZH** • 我们在 Crello 与 WebUI 两个具有挑战性的基准数据集上，对所提出的各组件做了充分的定性与定量分析，验证了本方法在多样设置下的有效性。

**EN** • We showcase the versatility and effectiveness of our approach across MLLMs of varying scales and families, and perform several ablation studies to provide deeper insights into the contributions of each component.

**ZH** • 我们展示了本方法在不同规模、不同系列的 MLLM 上的通用性与有效性，并进行了多项消融研究，以更深入地揭示各组件的贡献。

**EN** 2 Related works

**ZH** 2 相关工作

**EN** Graphic Layout Generation: As digital content creation continues to grow rapidly, the automated generation of visually appealing layouts that meet users’ needs has emerged as an important research problem. Early works employed rule-based [39] and energy optimization [36, 24] techniques to structure graphic layouts, providing a solid foundation but offering limited flexibility. GAN-based approaches [28, 22, 57] introduced frameworks for unconditional layout generation by capturing geometric relationships across elements and leveraging differentiable rendering in the image-space, while transformer models such as LayoutTransformer [16], VTN [1], and BLT [23] used autoregressive and bidirectional transformers to improve layout quality. With advancements in NLP, masking strategies, language models, and encoder-decoder architectures have been applied to layout generation. Approaches like CanvasVAE [51], FlexDM [20], and ICVT [5] integrate images and text to enhance content relevance, enabling conditional generation through multi-modal features extracted via transformer-based architectures [48, 12, 25]. However, these methods still face challenges in adaptability to diverse content and impose constraints that limit their practical usability in real-world design applications.

**ZH** 图形版面生成：随着数字内容创作持续增长，自动生成符合用户需求的美观版面已成为一项重要研究课题。早期工作采用基于规则 [39] 与能量优化 [36, 24] 的技术来组织图形版面，奠定了扎实基础但灵活性有限。基于 GAN 的方法 [28, 22, 57] 通过捕捉元素间的几何关系并利用图像空间中的可微渲染，建立了无条件版面生成的框架；LayoutTransformer [16]、VTN [1]、BLT [23] 等 Transformer 模型则使用自回归与双向 Transformer 来提升版面质量。随着自然语言处理的发展，掩码策略、语言模型与编码器-解码器架构也被引入版面生成。CanvasVAE [51]、FlexDM [20]、ICVT [5] 等方法融合图像与文本以增强内容相关性，借助基于 Transformer 架构 [48, 12, 25] 提取的多模态特征实现条件生成。然而，这些方法在适应多样内容方面仍存在困难，并带有制约其在真实设计场景中实用性的限制。

**EN** Constraint-aware Layout Prediction: Recent works have leveraged diffusion models to improve layout generation quality across various conditions. PLay [10] uses a latent diffusion model conditioned on guidelines to align elements, while LayoutDM [7] and LDGM [19] employ the discrete diffusion framework [3] to build unified models without guidelines, using attribute-specific corruption strategies [15] to restrict variables of different attributes to their respective sample spaces. LDGM further applies discretized Gaussian noise to enable gradual coordinate changes. Following a similar design, LayoutDiffusion [55] and LACE [8] enhance visual quality by scaling up the transformer backbone and improving alignment and overlap metrics. However, these methods lack contextual understanding and fail to capture semantic relationships across elements, leading to designs that may be geometrically accurate but aesthetically incoherent. Other diffusion-based methods [17, 6] attempt to generate layouts in continuous space but still rely on quantized geometric attributes or conditional generation based on categorical attributes, limiting their flexibility. Training diffusion models with masked and unmasked layouts [49] has shown potential for unifying various tasks but still lacks the contextual understanding.

**ZH** 约束感知的版面预测：近期工作借助扩散模型在各种条件下提升版面生成质量。PLay [10] 使用以设计准则为条件的潜扩散模型来对齐元素；LayoutDM [7] 与 LDGM [19] 采用离散扩散框架 [3] 构建无需准则的统一模型，并使用属性专属的 corruption 策略 [15]，把不同属性的变量限制在各自的样本空间内。LDGM 进一步施加离散化高斯噪声，使坐标得以渐变。沿类似思路，LayoutDiffusion [55] 与 LACE [8] 通过扩大 Transformer 骨干规模并改进对齐与重叠指标来提升视觉质量。然而，这些方法缺乏上下文理解，无法捕捉元素之间的语义关系，导致生成的版式可能几何上准确而美学上不连贯。其他基于扩散的方法 [17, 6] 尝试在连续空间中生成版面，但仍依赖量化的几何属性或基于类别属性的条件生成，灵活性受限。用带掩码与无掩码的版面训练扩散模型 [49] 在统一多种任务上显示出潜力，但同样缺乏上下文理解。

**EN** LLMs Assisted Layout Generation: Recent works have explored large language models (LLMs) for layout generation, treating layouts as structured data formats like XML or JSON. LayoutNUWA [46] fine-tunes LLaMa [47] and CodeLLaMa [43] for content-agnostic layout generation, achieving state-of-the-art results across multiple datasets. LayoutPrompter [29] introduces a training-free approach by leveraging RAG (Retrieval-Augmented Generation) to enhance in-context learning in GPT [4], though it is limited to open-domain generation. These methods, however, translate visual domain features into hard tokens, potentially leading to significant information loss. To address this, recent works propose multi-modal techniques such as visual instruction tuning [32] with aligned visual adaptation heads, allowing models to process visual information directly. While these approaches show promise, they rely on cross-entropy loss for optimization, which penalizes aesthetically good layouts along with poor ones (as depicted in Fig.1), neglecting aesthetic preferences and leading to suboptimal design outcomes. This cross-entropy loss-based optimization fails to capture nuanced aesthetic considerations essential for high-quality layouts.

**ZH** LLM 辅助的版面生成：近期工作探索用大语言模型（LLM）做版面生成，把版面视为 XML 或 JSON 之类的结构化数据格式。LayoutNUWA [46] 微调 LLaMa [47] 与 CodeLLaMa [43] 做与内容无关的版面生成，在多个数据集上取得了当前最优结果。LayoutPrompter [29] 利用检索增强生成（RAG）增强 GPT [4] 的上下文学习，提出一种免训练方法，但仅限于开放域生成。然而，这些方法把视觉域特征转译为硬令牌，可能造成显著的信息损失。为此，近期工作提出视觉指令微调 [32] 等多模态技术，配合对齐的视觉适配头，使模型能直接处理视觉信息。这些方法虽展现出前景，却依赖交叉熵损失做优化，而该损失会把美学上优秀的版面与拙劣的版面一并惩罚（如图 1 所示），忽视美学偏好，导致设计结果欠优。这种基于交叉熵损失优化的方式，无法捕捉高质量版面所必需的细腻美学考量。

**EN** 3 Methodology

**ZH** 3 方法

<!-- [原子块 · img]  -->

**EN** Figure 2: The training for the aesthetic layout prediction task consists of the following steps: 1) Vision Encoder: Design elements (images and text) are processed to generate image and text embeddings. 2) AesthetiQ Model Prediction: Embeddings are passed to the AesthetiQ model, which predicts layout coordinates. 3) Training with Cross-Entropy Loss: The predicted layout is compared with the ground truth and trained using cross-entropy loss. 4) Sampling for Comparison: Multiple layout predictions are generated using AesthetiQ inference. 5) Pair Selection and Quality Filtering: We filter the data based on quality heuristics to ensure layout quality in samples. 6) Judging by ViLA: The ViLA model compares layout pairs and selects the better one based on aesthetic preferences. 7) Aesthetic Preference Optimization (AAPA): Feedback from ViLA is used to fine-tune the AesthetiQ model for aesthetic optimization.

**ZH** 图 2：美学版面预测任务的训练包含以下步骤：1）视觉编码器：处理设计元素（图像与文本），生成图像嵌入与文本嵌入。2）AesthetiQ 模型预测：把嵌入送入 AesthetiQ 模型，预测版面坐标。3）交叉熵损失训练：把预测版面与真值比较，用交叉熵损失训练。4）采样用于比较：用 AesthetiQ 推理生成多个版面预测。5）配对选择与质量过滤：基于质量启发式过滤数据，保证样本中的版面质量。6）由 ViLA 判定：ViLA 模型比较两个版面，按美学偏好选出更优的一个。7）美学偏好优化（AAPA）：用 ViLA 的反馈微调 AesthetiQ 模型，实现美学优化。

**EN** Our approach to layout prediction focuses on generating aesthetically aligned designs, with a Multi-modal Large Language Model (MLLM) serving as an evaluator for layout quality. We want to capture design aesthetics in layout configurations by using another MLLM (judge). To address the challenges given by subjective design preferences, limited datasets, and high-dimensional variability, we use an Aesthetic-Aware Preference Alignment (AAPA) technique, which aligns our model’s output with aesthetic evaluations from the judge MLLM. We begin by formalizing the layout prediction task, discussing the input and output representations, and the fine-tuning approach. We then introduce AAPA, which drives aesthetic sensitivity in layout generation (Fig 2). Finally, we present additional insights gained from scaling and pretraining on a large dataset of templates.

**ZH** 我们的版面预测路线着眼于生成美学上协调的设计，并以多模态大语言模型（MLLM）作为版面质量的评估者。我们希望通过引入另一个 MLLM（裁判）来捕捉版面配置中的设计美感。面对设计偏好主观、数据集有限、高维变化等挑战，我们采用美学感知偏好对齐（AAPA）技术，把模型输出与裁判 MLLM 的美学评价对齐。我们首先形式化版面预测任务，讨论输入与输出的表示以及微调方式；随后介绍驱动版面生成中美学敏感性的 AAPA（图 2）；最后给出在大规模模板数据集上做规模化与预训练所获得的额外认识。

**EN** 3.1 Layout Prediction Task

**ZH** 3.1 版面预测任务

**EN** The goal of layout prediction involves placing design elements over a blank canvas to generate an aesthetically pleasing graphic template. Formally, consider a set of ⟦SLOT_1⟧ design elements ⟦SLOT_2⟧ that need to be placed over a canvas of width ⟦SLOT_3⟧ and height ⟦SLOT_4⟧ to obtain a graphic layout ⟦SLOT_5⟧. We define the placement of an element ⟦SLOT_6⟧ through bounding box attributes ⟦SLOT_7⟧ that represent the graphic element’s center coordinates, width, and height of the bounding box. Given the type of each element denoted by ⟦SLOT_8⟧, where ⟦SLOT_9⟧, we verbalise the input through a prompt template denoted by ⟦SLOT_10⟧ (Eq.1).

**ZH** 版面预测的目标是把设计元素摆放到空白画布上，生成具有美学感的图形模板。形式上，考虑 ⟦SLOT_1⟧ 个设计元素 ⟦SLOT_2⟧，需要把它们摆放到宽度为 ⟦SLOT_3⟧、高度为 ⟦SLOT_4⟧ 的画布上，得到图形版面 ⟦SLOT_5⟧。元素 ⟦SLOT_6⟧ 的摆放由边界框属性 ⟦SLOT_7⟧ 定义，这些属性表示该图形元素边界框的中心坐标、宽度与高度。给定每个元素的类型 ⟦SLOT_8⟧（其中 ⟦SLOT_9⟧），我们通过提示模板 ⟦SLOT_10⟧ 对输入进行语言化描述（式 1）。

<!-- [原子块 · table] 𝒫 H c , W c E = ⋃ i = 1 n { ImageTokens ​ ( e i ) if ​ T ​ ( e i ) ∈ 𝒯 − { text } TextTokens ​ ( e i ) if ​ T ​ ( e i ) = text \mathcal{P}^{E}_{H_{c},W_{c}}=\bigcup_{i=1}^{n}\begin{cases}\text{ImageTo -->

**EN** Consider the layout MLLM ⟦SLOT_11⟧ with three components: a vision encoder ⟦SLOT_12⟧, a text encoder ⟦SLOT_13⟧, and a large language model ⟦SLOT_14⟧. ⟦SLOT_15⟧ takes as input the verbalized prompt, ⟦SLOT_16⟧, by encoding each token in the prompt using either a vision encoder or a text encoder, depending on the type of the corresponding design element. For each token representing an element ⟦SLOT_17⟧ where ⟦SLOT_18⟧, the vision encoder ⟦SLOT_19⟧ produces an embedding ⟦SLOT_20⟧. For tokens representing elements where ⟦SLOT_21⟧, the text encoder ⟦SLOT_22⟧ produces an embedding ⟦SLOT_23⟧. The final multi-modal embedding ⟦SLOT_24⟧ for ⟦SLOT_25⟧ is then represented as the union of all encoded tokens, combining vision and text embeddings based on each token’s type (Eq.2).

**ZH** 考虑用于版面生成的多模态大语言模型 ⟦SLOT_11⟧，它由三个部分组成：视觉编码器 ⟦SLOT_12⟧、文本编码器 ⟦SLOT_13⟧ 与大语言模型 ⟦SLOT_14⟧。⟦SLOT_15⟧ 以语言化提示 ⟦SLOT_16⟧ 为输入，根据对应设计元素的类型，用视觉编码器或文本编码器对提示中的每个词元进行编码。对于表示元素 ⟦SLOT_17⟧ 的词元（其中 ⟦SLOT_18⟧），视觉编码器 ⟦SLOT_19⟧ 产生嵌入 ⟦SLOT_20⟧；对于表示元素且满足 ⟦SLOT_21⟧ 的词元，文本编码器 ⟦SLOT_22⟧ 产生嵌入 ⟦SLOT_23⟧。最终的多模态嵌入 ⟦SLOT_24⟧（对应 ⟦SLOT_25⟧）表示为所有已编码词元的并集，即按每个词元的类型把视觉嵌入与文本嵌入合并（式 2）。

<!-- [原子块 · table] Z = ⋃ i = 1 N { z i vision if ​ T ​ ( e i ) ∈ 𝒯 − { text } z i text if ​ T ​ ( e i ) = text Z=\bigcup_{i=1}^{N}\begin{cases}z_{i}^{\text{vision}}&\text{if }T(e_{i})\in\mathcal{T}-\{\text{text}\}\\ z_{ -->

**EN** Once the multi-modal embedding ⟦SLOT_26⟧ is constructed, it is fed into the large language model component ⟦SLOT_27⟧ of ⟦SLOT_28⟧ to predict the position of each design element.

**ZH** 多模态嵌入 ⟦SLOT_26⟧ 构造完成后，被送入大语言模型组件 ⟦SLOT_27⟧（属于 ⟦SLOT_28⟧），以预测每个设计元素的位置。

**EN** 3.2 Position-Aware Layout Instruction Tuning

**ZH** 3.2 位置感知的版面指令微调

**EN** To facilitate accurate layout prediction, we discretize the bounding box coordinates ⟦SLOT_29⟧. These continuous attributes are mapped into discrete bins based on the width ⟦SLOT_30⟧ and height ⟦SLOT_31⟧ of the canvas. The binning function ⟦SLOT_32⟧ depicted by Eq. 3 maps each continuous attribute into one of ⟦SLOT_33⟧ bins, where ⟦SLOT_34⟧ is the number of bins:

**ZH** 为了实现准确的版面预测，我们对边界框坐标 ⟦SLOT_29⟧ 做离散化。这些连续属性依据画布的宽度 ⟦SLOT_30⟧ 与高度 ⟦SLOT_31⟧ 被映射到离散的分箱中。式 3 给出的分箱函数 ⟦SLOT_32⟧ 把每个连续属性映射到 ⟦SLOT_33⟧ 个分箱之一，其中 ⟦SLOT_34⟧ 为分箱数量：

<!-- [原子块 · table] B ⁡ ( a i ) = ⌊ a i D × K ⌋ with D = { W c if ​ a i ∈ { x i , w i } H c if ​ a i ∈ { y i , h i } B(a_{i})=\left\lfloor\frac{a_{i}}{D}\times K\right\rfloor\quad\text{with}\quad D=\begin{cases}W_{c}&\te -->

**EN** For each of these binned values, we introduce position tokens ⟦SLOT_35⟧, where ⟦SLOT_36⟧. Thus, each attribute ⟦SLOT_37⟧ is assigned the tokens ⟦SLOT_38⟧, ⟦SLOT_39⟧, ⟦SLOT_40⟧, and ⟦SLOT_41⟧ respectively. This discretization reduces the continuous spatial attributes to a fixed set of discrete position tokens, simplifying the layout prediction task. By quantizing the position, the model can more effectively learn the spatial relationships across design elements. Once the position tokens are integrated into the multi-modal embedding, the language model component ⟦SLOT_42⟧ predicts the layout by outputting the corresponding position tokens for each element, which are mapped back to approximate spatial coordinates using the function ⟦SLOT_43⟧.

**ZH** 对每个分箱取值，我们引入位置词元 ⟦SLOT_35⟧，其中 ⟦SLOT_36⟧。于是，属性 ⟦SLOT_37⟧ 分别被赋予词元 ⟦SLOT_38⟧、⟦SLOT_39⟧、⟦SLOT_40⟧ 与 ⟦SLOT_41⟧。这一离散化把连续的空间属性压缩为一组固定的离散位置词元，简化了版面预测任务；通过对位置量化，模型可以更有效地学习设计元素之间的空间关系。位置词元并入多模态嵌入后，语言模型部分 ⟦SLOT_42⟧ 通过输出每个元素对应的位置词元来预测版面，再用函数 ⟦SLOT_43⟧ 把这些词元映射回近似的空间坐标。

**EN** Let ⟦SLOT_44⟧ represent the ground truth sequence of position tokens corresponding to the predicted bounding box attributes of the design elements, where each ⟦SLOT_45⟧, and ⟦SLOT_46⟧ is the number of output tokens. ⟦SLOT_47⟧ outputs policy ⟦SLOT_48⟧, a sequence of logits ⟦SLOT_49⟧, where ⟦SLOT_50⟧ represents the predicted probabilities for each position token of each design element ⟦SLOT_51⟧. We train ⟦SLOT_52⟧ through the cross-entropy loss (Eq. 4)

**ZH** 令 ⟦SLOT_44⟧ 表示设计元素预测边界框属性所对应的位置词元真值序列，其中每个 ⟦SLOT_45⟧，⟦SLOT_46⟧ 为输出词元的数量。⟦SLOT_47⟧ 输出策略 ⟦SLOT_48⟧，即一串 logits ⟦SLOT_49⟧，其中 ⟦SLOT_50⟧ 表示设计元素 ⟦SLOT_51⟧ 每个位置词元的预测概率。我们通过交叉熵损失训练 ⟦SLOT_52⟧（式 4）

<!-- [原子块 · table] ℒ CE = − 1 S ∑ i = 1 S ∑ j = 1 M ∑ k = 0 K 𝕀 ( y j = pos k ) log y ^ j , k \mathcal{L}_{\text{CE}}=-\frac{1}{S}\sum_{i=1}^{S}\sum_{j=1}^{M}\sum_{k=0}^{K}\mathbb{I}(y_{j}=\text{pos}_{k})\log\hat{y}_{j, -->

**EN** where ⟦SLOT_53⟧ is the indicator function and ⟦SLOT_54⟧ is the predicted probability (logit) for the ⟦SLOT_55⟧-th position token of the ⟦SLOT_56⟧-th element, and S is the size the dataset. Thus, during instruction tuning, the ⟦SLOT_57⟧ learns the correct spatial placement of each element through the alignment of the predicted position tokens with the ground truth tokens. However, cross-entropy loss is suboptimal as it requires an exact match (Fig 1). Additionally, if the ground-truth position token is ⟦SLOT_58⟧ and the model predicts ⟦SLOT_59⟧, the cross-entropy loss penalizes this heavily despite the minimal difference between the two positions.

**ZH** 其中 ⟦SLOT_53⟧ 为指示函数，⟦SLOT_54⟧ 是第 ⟦SLOT_55⟧ 个位置词元的预测概率（logit），该词元属于第 ⟦SLOT_56⟧ 个元素，S 为数据集规模。因此，在指令微调过程中，⟦SLOT_57⟧ 通过让预测的位置词元与真值词元对齐来学习每个元素的正确空间摆放。然而交叉熵损失并非最优，因为它要求完全匹配（图 1）。此外，若真值位置词元为 ⟦SLOT_58⟧ 而模型预测为 ⟦SLOT_59⟧，尽管两个位置差别极小，交叉熵损失仍会施以很重的惩罚。

**EN** 3.3 Aesthetic-Aware Preference Alignment

**ZH** 3.3 美学感知偏好对齐

**EN** A significant challenge in layout prediction arises from the non-differentiable nature of rendering individual elements on a canvas, which prevents the model from directly “seeing” the rendered template for aesthetic evaluation. To address this, we introduce a judge model ⟦SLOT_60⟧ that performs a pairwise comparison of two graphic layouts to determine which one is aesthetically superior. Given two graphic layouts, rendered on a canvas using a renderer ⟦SLOT_61⟧, denoted as ⟦SLOT_62⟧, ⟦SLOT_63⟧, the goal of ⟦SLOT_64⟧ is to decide which layout is better based on aesthetic criteria. ⟦SLOT_65⟧ takes as input a judge prompt ⟦SLOT_66⟧, which verbalizes the evaluation criteria for comparing the two layouts, and the two graphic layouts ⟦SLOT_67⟧ and ⟦SLOT_68⟧, to produce a binary decision about which layout is better. Formally,

**ZH** 版面预测面临的一大挑战在于：把各个元素渲染到画布上的过程不可微，模型因此无法直接「看到」渲染后的模板来做美学评价。为此，我们引入一个裁判模型 ⟦SLOT_60⟧，对两个图形版面做两两比较，判断哪一个在美学上更优。给定用渲染器 ⟦SLOT_61⟧ 在画布上渲染出的两个图形版面 ⟦SLOT_62⟧ 与 ⟦SLOT_63⟧，⟦SLOT_64⟧ 的目标是按照美学准则判定哪个版面更好。⟦SLOT_65⟧ 以裁判提示 ⟦SLOT_66⟧（它对比较两个版面所用的评价标准做了语言化描述）和两个图形版面 ⟦SLOT_67⟧、⟦SLOT_68⟧ 为输入，输出关于哪个版面更好的二元判定。形式化地，

<!-- [原子块 · table] d = ℳ judge ​ ( 𝒫 judge , G 1 , G 2 ) d=\mathcal{M}_{\text{judge}}(\mathcal{P}_{\text{judge}},G^{1},G^{2}) (5) -->

**EN** where ⟦SLOT_69⟧ represents the decision of the ⟦SLOT_70⟧. If ⟦SLOT_71⟧, then graphic layout ⟦SLOT_72⟧ is considered better than graphic layout ⟦SLOT_73⟧, and vice versa. Thus, we define

**ZH** 其中 ⟦SLOT_69⟧ 表示 ⟦SLOT_70⟧ 的判定结果。若 ⟦SLOT_71⟧，则认为图形版面 ⟦SLOT_72⟧ 优于图形版面 ⟦SLOT_73⟧，反之亦然。于是我们定义

<!-- [原子块 · table] G w = { G 1 if ​ d = 1 G 2 if ​ d = 2 , G r = { G 2 if ​ d = 1 G 1 if ​ d = 2 G^{\text{w}}=\begin{cases}G^{1}&\text{if }d=1\\ G^{2}&\text{if }d=2\end{cases},\quad G^{\text{r}}=\begin{cases}G^{2}&\text -->

**EN** Through this pairwise comparison, the judging model ⟦SLOT_74⟧ selects the best (⟦SLOT_75⟧) and worst (⟦SLOT_76⟧) graphic layouts based on aesthetic quality without computing any explicit scores. Scoring individual layouts was found to be challenging, as MLLMs often assign similar scores across a range of layouts due to their limited exposure to the design space. Once we obtain the preferential data from ⟦SLOT_77⟧, ⟦SLOT_78⟧ is tuned further to prefer the better layout compared to the worse layout evaluated based on aesthetics. For this, we apply Aesthetic-Aware Preference Alignment (AAPA) to train the layout model ⟦SLOT_79⟧ using AAPA loss (Eq. 7)

**ZH** 通过这种两两比较，裁判模型 ⟦SLOT_74⟧ 依据美学质量选出最优（⟦SLOT_75⟧）与最差（⟦SLOT_76⟧）的图形版面，整个过程不计算任何显式分数。我们发现给单个版面打分并不容易，因为多模态大语言模型对设计空间接触有限，往往给一系列版面打出相近的分数。从 ⟦SLOT_77⟧ 获得偏好数据后，我们进一步调整 ⟦SLOT_78⟧，使其在美学评价下更偏向较优的版面而非较差的版面。为此，我们采用美学感知偏好对齐（AAPA），用 AAPA 损失训练版面模型 ⟦SLOT_79⟧（式 7）

<!-- [原子块 · table] ℒ AAPA = − log ⁡ σ ⁡ ( β ⁡ ( log ⁡ π ℳ ​ ( 𝒫 H c , W c E w ) π ℳ ^ ​ ( 𝒫 H c , W c E w ) − log ⁡ π ℳ ​ ( 𝒫 H c , W c E r ) π ℳ ^ ​ ( 𝒫 H c , W c E r ) ) ) \mathcal{L}_{\text{AAPA}}=-\log\sigma\Bigg(\b -->

**EN** where ⟦SLOT_80⟧ and ⟦SLOT_81⟧ are the policies of layout prediction and reference model respectively, and ⟦SLOT_82⟧ is a hyper-parameter to control divergence from the reference model. We initialize the reference model ⟦SLOT_83⟧ to be the same as the layout prediction model ⟦SLOT_84⟧ at the start of the training.

**ZH** 其中 ⟦SLOT_80⟧ 与 ⟦SLOT_81⟧ 分别是版面预测模型与参考模型的策略，⟦SLOT_82⟧ 是控制与参考模型偏离程度的超参数。训练开始时，我们把参考模型 ⟦SLOT_83⟧ 初始化为与版面预测模型 ⟦SLOT_84⟧ 相同。

**EN** Quality Metrics-based Layout Filtering: To ensure high quality layouts are used to train ⟦SLOT_85⟧ through AAPA, we enforce a data filtration process based on quality metrics that evaluate the alignment and overlap of the predicted bounding boxes. The goal is to maximize alignment between design elements while minimizing overlap, ensuring that the selected layouts are aesthetically pleasing and well-structured. For each design element ⟦SLOT_86⟧, let ⟦SLOT_87⟧ represents the top-left (⟦SLOT_88⟧), center (⟦SLOT_89⟧), and bottom-right (⟦SLOT_90⟧) coordinates of the bounding box. We compute the minimum distance between the key coordinates of element ⟦SLOT_91⟧ and all of those other elements ⟦SLOT_92⟧ (⟦SLOT_93⟧), to find the adjacent element with respect to the key coordinates and compute alignment quality metric ⟦SLOT_94⟧, depicted by Eq.8.

**ZH** 基于质量指标的版面过滤：为保证通过 AAPA 训练 ⟦SLOT_85⟧ 时使用的是高质量版面，我们执行了一套基于质量指标的数据过滤流程，这些指标衡量预测边界框的对齐与重叠情况。其目标是在最大化设计元素之间对齐程度的同时最小化重叠，从而保证选出的版面既美观又结构良好。对于设计元素 ⟦SLOT_86⟧，令 ⟦SLOT_87⟧ 表示边界框的左上角（⟦SLOT_88⟧）、中心（⟦SLOT_89⟧）与右下角（⟦SLOT_90⟧）坐标。我们计算元素 ⟦SLOT_91⟧ 的关键坐标与所有其他元素 ⟦SLOT_92⟧（⟦SLOT_93⟧）关键坐标之间的最小距离，以找出相对于这些关键坐标最邻近的元素，并计算对齐质量指标 ⟦SLOT_94⟧，如式 8 所示。

<!-- [原子块 · table] 𝒬 align ​ ( G ) = 1 N ​ ∑ i = 1 N min ⁡ ( f ⁡ ( Δ ​ x i ∗ ) , f ⁡ ( Δ ​ y i ∗ ) ) − 1 e − 1 \mathcal{Q}_{\text{align}}(G)=\frac{1}{N}\sum_{i=1}^{N}\frac{\min(f(\Delta x_{i}^{*}),f(\Delta y_{i}^{*}))-1 -->

**EN** where ⟦SLOT_95⟧, ⟦SLOT_96⟧ and ⟦SLOT_97⟧. The horizontal and vertical distances are computed as ⟦SLOT_98⟧, and ⟦SLOT_99⟧ respectively. Similarly, we compute the average overlap of an element ⟦SLOT_100⟧ with all other elements ⟦SLOT_101⟧ and define ⟦SLOT_102⟧ using Eq. 9.

**ZH** 其中 ⟦SLOT_95⟧、⟦SLOT_96⟧ 与 ⟦SLOT_97⟧。水平与竖直距离分别按 ⟦SLOT_98⟧ 与 ⟦SLOT_99⟧ 计算。类似地，我们计算元素 ⟦SLOT_100⟧ 与所有其他元素 ⟦SLOT_101⟧ 的平均重叠，并用式 9 定义 ⟦SLOT_102⟧。

<!-- [原子块 · table] 𝒬 overlap ​ ( G ) = 1 N ​ ∑ i = 1 N ∑ j ≠ i ( 1 − Area ​ ( e i ∩ e j ) Area ​ ( e i ) ) \mathcal{Q}_{\text{overlap}}(G)=\frac{1}{N}\sum_{i=1}^{N}\sum_{j\neq i}\Big(1-\frac{\text{Area}(e_{i}\cap e_{j}) -->

**EN** where, ⟦SLOT_103⟧ denotes the area of intersection between element ⟦SLOT_104⟧ and ⟦SLOT_105⟧ and ⟦SLOT_106⟧ denotes the area of element ⟦SLOT_107⟧. Ideally, we want overlap to be less, and therefore higher ⟦SLOT_108⟧ denotes lesser overlap. We compute the overall quality metric ⟦SLOT_109⟧ for a graphic layout ⟦SLOT_110⟧ by taking the average of the alignment score ⟦SLOT_111⟧ and the overlap score ⟦SLOT_112⟧. For a given layout ⟦SLOT_113⟧, if its quality metric satisfies ⟦SLOT_114⟧, i.e., the quality metric exceeds one standard deviation below the mean quality metric across the entire dataset, we classify it as a higher-quality layout. By applying this data filtration process, we enhance the overall quality of the training data, which in turn helps to effectively train the layout model ⟦SLOT_115⟧.

**ZH** 其中 ⟦SLOT_103⟧ 表示元素 ⟦SLOT_104⟧ 与 ⟦SLOT_105⟧ 的交集面积，⟦SLOT_106⟧ 表示元素 ⟦SLOT_107⟧ 的面积。理想情况下我们希望重叠尽可能小，因此 ⟦SLOT_108⟧ 越高代表重叠越少。整体质量指标 ⟦SLOT_109⟧ 的计算方式是：对图形版面 ⟦SLOT_110⟧，取对齐分数 ⟦SLOT_111⟧ 与重叠分数 ⟦SLOT_112⟧ 的平均值。对于给定版面 ⟦SLOT_113⟧，若其质量指标满足 ⟦SLOT_114⟧，即该指标高于整个数据集质量指标均值以下一个标准差，则将其归为较高质量版面。通过这一数据过滤流程，我们提升了训练数据的整体质量，进而有助于更有效地训练版面模型 ⟦SLOT_115⟧。

**EN** Aesthetic-Aware Layout Evaluation: To evaluate the aesthetic quality of predicted layouts, we employ the judge model ⟦SLOT_116⟧ to perform pairwise comparisons between predicted layouts and their corresponding ground truth layouts. For a test dataset ⟦SLOT_117⟧ containing ⟦SLOT_118⟧ samples, let ⟦SLOT_119⟧ be the predicted layout and ⟦SLOT_120⟧ be the ground truth layout for the ⟦SLOT_121⟧-th sample. The win rate ⟦SLOT_122⟧ is computed as:

**ZH** 美学感知的版面评价：为评估预测版面的美学质量，我们让裁判模型 ⟦SLOT_116⟧ 在预测版面与对应真值版面之间做两两比较。对于测试数据集 ⟦SLOT_117⟧（含 ⟦SLOT_118⟧ 个样本），令 ⟦SLOT_119⟧ 为预测版面、⟦SLOT_120⟧ 为真值版面，二者均对应第 ⟦SLOT_121⟧ 个样本。胜率 ⟦SLOT_122⟧ 计算如下：

<!-- [原子块 · table] 𝒲 = 1 S ∑ i = 1 S 𝕀 { ℳ judge ( 𝒫 judge , G p i , G g i ) = 1 } \mathcal{W}=\frac{1}{S}\sum_{i=1}^{S}\mathbb{I}\Big\{\mathcal{M}_{\text{judge}}(\mathcal{P}_{\text{judge}},G_{p}^{i},G_{g}^{i})=1\Big\}  -->

**EN** where ⟦SLOT_123⟧ is the indicator function that returns 1 if the predicted layout wins over the ground truth layout in the aesthetic comparison, and 0 otherwise. A higher win rate indicates that the layout model ⟦SLOT_124⟧ generates layouts that are aesthetically superior to the ground truth layouts.

**ZH** 其中 ⟦SLOT_123⟧ 为指示函数：若预测版面在美学比较中胜过真值版面则返回 1，否则返回 0。胜率越高，说明版面模型 ⟦SLOT_124⟧ 生成的版面在美学上优于真值版面。

**EN** 3.4 Pre-training to Enhance Layout Understanding

**ZH** 3.4 用预训练增强版面理解

**EN** To further explore the role of data size for pretraining data hungry MLLM’s, we trained our model on an 80,000 template dataset collected from an online design creation platform. This pretraining phase aims to imbue the model with foundational design principles, such as minimizing element overlap, enhancing alignment, and prioritizing salient regions for important elements. Our experiments reveal that pretraining before position-aware layout instruction tuning significantly boosts the model’s aesthetic sensitivity, as evidenced by improvements in alignment with design principles when compared to models trained without pretraining.

**ZH** 为探究数据规模对「数据饥渴」的多模态大语言模型预训练的作用，我们在从一个在线设计创作平台收集的 80,000 个模板数据集上训练了模型。这一预训练阶段旨在让模型习得基础设计原则，例如尽量减少元素重叠、增强对齐，以及让重要元素优先占据显著区域。实验表明，在位置感知的版面指令微调之前进行预训练，能显著提升模型的美学敏感度：与未经预训练的模型相比，其输出与设计原则的契合度明显改善。

**EN** 4 Experimental Details

**ZH** 4 实验细节

**EN** Datasets: We evaluate AesthetiQ on two benchmark graphic layout datasets: Crello [51] and WebUI [50], both posing unique challenges. Crello dataset contains 23,302 vector-based design templates across various formats (e.g., social media posts, banners), split into 19,479 training, 1,852 validation, and 1,971 test samples. Its primary challenge lies in handling diverse canvas sizes and aspect ratios while maintaining design consistency. WebUI dataset comprises 70k web page UIs, including visual screenshots and metadata. WebUI’s challenges stem from variability in web page structures across domains. Both datasets test the model’s ability to manage complex layouts and ensure semantic coherence across diverse design structures.

**ZH** 数据集：我们在 Crello [51] 与 WebUI [50] 两个图形版面基准数据集上评估 AesthetiQ，二者各有独特挑战。Crello 数据集包含 23,302 个矢量设计模板，涵盖社交媒体帖子、横幅等多种版式，划分为 19,479 个训练样本、1,852 个验证样本与 1,971 个测试样本；其主要挑战在于处理多样的画布尺寸与长宽比，同时保持设计一致性。WebUI 数据集包含 7 万个网页 UI，含视觉截图与元数据，其挑战源于不同领域网页结构的差异。两个数据集都检验模型管理复杂版面并保证跨多样设计结构语义连贯的能力。

**EN** Implementation Details: For our layout prediction model ⟦SLOT_125⟧, we use InternVL [9] as the backbone, given its robust spatial understanding and visual reasoning capabilities across diverse tasks like DocVQA [35], TextVQA [45], MME [13], MMMU [54], and MMVET [53]. InternVL’s multi-image training aligns well with layout prediction, where interpreting contextual relationships between multiple elements is crucial. For judging layouts based on aesthetics, we leverage VILA-7B [30] as ⟦SLOT_126⟧. We train AesthetiQ for 20 epochs on an effective batch size of 128 using 8 80GB A100 GPUs. Position coordinates are discretized with ⟦SLOT_127⟧ tokens, and ⟦SLOT_128⟧ is optimized using a learning rate of ⟦SLOT_129⟧, weight decay of ⟦SLOT_130⟧, and Cosine Annealing [33] with warmup ratio ⟦SLOT_131⟧ through the AdamW optimizer [34]. Layout preferences for AAPA are obtained by randomly choosing between comparing two model-predicted layouts or comparing a model-predicted layout with the ground truth.

**ZH** 实现细节：对于版面预测模型 ⟦SLOT_125⟧，我们采用 InternVL [9] 作为骨干网络，因其在 DocVQA [35]、TextVQA [45]、MME [13]、MMMU [54]、MMVET [53] 等多种任务上展现出稳健的空间理解与视觉推理能力。InternVL 的多图训练方式与版面预测高度契合，因为理解多个元素之间的上下文关系至关重要。在基于美学评判版面时，我们使用 VILA-7B [30] 作为 ⟦SLOT_126⟧。我们在 8 张 80GB A100 GPU 上以 128 的有效批大小训练 AesthetiQ 共 20 个轮次。位置坐标用 ⟦SLOT_127⟧ 个词元离散化；⟦SLOT_128⟧ 通过 AdamW 优化器 [34] 优化，学习率为 ⟦SLOT_129⟧，权重衰减为 ⟦SLOT_130⟧，并采用预热比例为 ⟦SLOT_131⟧ 的余弦退火 [33]。AAPA 所用的版面偏好通过随机选择两种方式获得：比较两个模型预测的版面，或比较模型预测版面与真值版面。

**EN** Evaluation Protocol: To assess the effectiveness of AAPA, including pre-training and quality-metric-based filtering, we evaluate two key metrics: Mean Intersection over Union (mIoU) and ⟦SLOT_132⟧ win rate. The mIoU is computed across three different inference settings: All (predicting the position of all elements), Single (predicting the position of a single text element), and Multiple (predicting the position of all text elements). This allows us to evaluate the model’s ability to accurately predict layout configurations under varying levels of complexity. The ⟦SLOT_133⟧ win rate is calculated in the All inference mode and evaluates the aesthetic quality of generated layouts by comparing them against ground truth using ⟦SLOT_134⟧. This dual-metric evaluation ensures a comprehensive assessment of both spatial accuracy and subjective visual appeal.

**ZH** 评测方案：为评估 AAPA（含预训练与基于质量指标的过滤）的效果，我们考察两个关键指标：平均交并比（mIoU）与 ⟦SLOT_132⟧ 胜率。mIoU 在三种推理设置下计算：All（预测所有元素的位置）、Single（预测单个文本元素的位置）与 Multiple（预测所有文本元素的位置），据此可以评估模型在不同复杂度下准确预测版面配置的能力。⟦SLOT_133⟧ 胜率在 All 推理模式下计算，用 ⟦SLOT_134⟧ 把生成版面与真值比较，评估其美学质量。这一双指标评测保证了对空间准确性与主观视觉吸引力两方面的综合考察。

<!-- [原子块 · table] Method Mean IoU (%) ℳ judge \mathcal{M}_{\text{judge}} All Single Multiple Win Rate (%) SmartText+ - 4.7 2.3 - Typography LMM - 40.2 17.2 - FlexDM 12.71 35.5 10.3 0.93 LACE 23.18 41.96 21.49 3.51 Post -->

**EN** Table 1: Comparison of layout generation methods based on Mean IoU (%) and Judge Win Rate (%) on Crello Dataset. AesthetiQ models outperform baselines, achieving higher IoU and Judge Win Rate, with AesthetiQ-8B showing the best overall performance.

**ZH** 表 1：在 Crello 数据集上按平均 IoU（%）与裁判胜率（%）比较各版面生成方法。AesthetiQ 系列模型优于基线，取得更高的 IoU 与裁判胜率，其中 AesthetiQ-8B 整体表现最佳。

<!-- [原子块 · table] Method Mean IoU (%) ℳ judge \mathcal{M}_{\text{judge}} Win Rate (%) Desigen 15.36 4.81 LACE 17.88 5.27 PosterLLaVa 30.19 14.73 LayoutNUWA 32.16 15.28 AesthetiQ-1B 38.47 19.29 AesthetiQ-8B 48.29 24.48 -->

**EN** Table 2: Comparison of AesthetiQ with baseline methods based on Mean IoU (%) and Judge Win Rate (%) on WebUI Dataset, showcasing significantly superior performance of AesthetiQ.

**ZH** 表 2：在 WebUI 数据集上按平均 IoU（%）与裁判胜率（%）比较 AesthetiQ 与基线方法，显示出 AesthetiQ 的显著优势。

<!-- [原子块 · img]  -->

**EN** Figure 3: Qualitative comparison of our model, AesthetiQ, against recent methods FlexDM, LACE, and LayoutNUWA. Despite the challenge of arranging numerous elements, AesthetiQ consistently achieves superior layout quality. In row (a), AesthetiQ effectively places text within salient regions, maintaining clear hierarchy and avoiding overlaps, which enhances readability and aesthetic appeal. In row (b), it achieves precise alignment across elements and optimally positions diverse shapes, preserving a cohesive visual structure. Row (c) showcases AesthetiQ’s advanced semantic understanding, generating a visually balanced and aesthetically pleasing layout. Overall, AesthetiQ consistently outperforms competitors in creating coherent, well-structured designs that align with human aesthetic preferences.

**ZH** 图 3：本文模型 AesthetiQ 与近期方法 FlexDM、LACE、LayoutNUWA 的定性比较。尽管排列大量元素颇具挑战，AesthetiQ 始终取得更优的版面质量。在 (a) 行，AesthetiQ 把文本有效放置在显著区域，保持清晰的层级并避免重叠，从而提升可读性与美学吸引力。在 (b) 行，它实现了元素之间的精确对齐，并对多样形状做出最优摆位，保持了连贯的视觉结构。(c) 行展示了 AesthetiQ 的高级语义理解，生成的版面视觉均衡、赏心悦目。总体而言，AesthetiQ 在生成连贯、结构良好且契合人类美学偏好的设计上持续领先于对比方法。

**EN** 5 Results and Analysis

**ZH** 5 结果与分析

**EN** Comparison of AesthetiQ with baselines: Table 1 compares layout generation methods on the Crello dataset, showcasing the superior performance of our AesthetiQ models across multiple metrics. AesthetiQ-8B achieves the highest Mean IoU scores, with 42.83% in the All setting, 52.67% in the Single setting, and 40.64% in the Multiple setting, significantly surpassing baselines like LACE [8] (23.18% in All) and LayoutNUWA [46] (25.74% in All). Additionally, AesthetiQ-8B achieves the best ⟦SLOT_135⟧ win rate of 17.19%, highlighting its ability to produce layouts that are both geometrically precise and aesthetically appealing. These consistent improvements in mIoU and judge win rate reflect AesthetiQ’s capacity to model intricate design structures while integrating aesthetic constraints, resulting in layouts that better align with judge preferences compared to other methods like FlexDM [20] and SmartText+ [26], which perform poorly across both metrics. Moreover, multi-modal LLM-based methods such as PosterLLaVa [52] and LayoutNUWA also fall short of AesthetiQ-8B, underscoring the robustness of our approach in handling diverse layout configurations while maintaining high visual quality.

**ZH** AesthetiQ 与基线的比较：表 1 在 Crello 数据集上比较了各版面生成方法，展示了 AesthetiQ 系列模型在多项指标上的优越表现。AesthetiQ-8B 取得最高的平均 IoU：All 设置下为 42.83%，Single 设置下为 52.67%，Multiple 设置下为 40.64%，显著超过 LACE [8]（All 为 23.18%）与 LayoutNUWA [46]（All 为 25.74%）等基线。此外，AesthetiQ-8B 取得 17.19% 的最佳 ⟦SLOT_135⟧ 胜率，说明它能生成既几何精确又具美学吸引力的版面。mIoU 与裁判胜率的同步提升，反映出 AesthetiQ 既善于建模复杂的设计结构，又能融入美学约束，因而生成的版面比其他方法更贴合裁判的偏好；FlexDM [20] 与 SmartText+ [26] 在两项指标上都表现不佳。此外，PosterLLaVa [52] 与 LayoutNUWA 等基于多模态大语言模型的方法同样不及 AesthetiQ-8B，说明本方法在处理多样版面配置并保持高视觉质量上更为稳健。

**EN** Table 3 further demonstrates that AesthetiQ models significantly outperform all baselines on the WebUI dataset across both metrics. For instance, AesthetiQ-8B achieves a remarkable Mean IoU of 48.29% and a judge win rate of 24.48%, well above LayoutNUWA, the top-performing baseline, which scores 32.16% in Mean IoU and 15.28% in win rate. Even smaller variants, like AesthetiQ-1B, exhibit strong performance with a Mean IoU of 38.47% and a judge win rate of 19.29%. In contrast, previous methods such as Desigen [50] (15.36% IoU, 4.81% win rate) and LACE (17.88% IoU, 5.27% win rate) perform significantly worse. These results highlight AesthetiQ’s strength in producing layouts that are not only more accurate but also more aesthetically pleasing.

**ZH** 表 3 进一步表明，AesthetiQ 系列模型在 WebUI 数据集上以两项指标显著优于所有基线。例如，AesthetiQ-8B 取得 48.29% 的平均 IoU 与 24.48% 的裁判胜率，远高于表现最好的基线 LayoutNUWA（平均 IoU 32.16%，胜率 15.28%）。即便是较小的 AesthetiQ-1B，也以 38.47% 的平均 IoU 与 19.29% 的裁判胜率展现出强劲表现。相比之下，Desigen [50]（IoU 15.36%，胜率 4.81%）与 LACE（IoU 17.88%，胜率 5.27%）等先前方法明显逊色。这些结果凸显了 AesthetiQ 的优势：它所生成的版面不仅更准确，而且更具美感。

**EN** Qualitative Results: Figure 3 presents a qualitative comparison of AesthetiQ against strong baselines. In row (a), AesthetiQ skillfully places text in prominent areas, establishing a clear hierarchy and avoiding overlaps, which improves readability and visual appeal. Row (b) highlights AesthetiQ’s precise alignment of elements and optimal positioning of various shapes, resulting in a unified visual layout. In row (c), AesthetiQ demonstrates its advanced semantic understanding, producing a balanced and aesthetically pleasing design. Overall, AesthetiQ consistently surpasses baselines by generating coherent, well-structured layouts that align with human aesthetic preferences. A user study, detailed in the Appendix, reveals that AesthetiQ was consistently the top choice for predicted layouts when compared to FlexDM, LACE, LayoutNUWA, and human preferences correlate well with the preference distribution of judge model ⟦SLOT_136⟧.

**ZH** 定性结果：图 3 给出了 AesthetiQ 与强劲基线的定性比较。在 (a) 行，AesthetiQ 巧妙地把文本放在醒目位置，建立起清晰的层级并避免重叠，从而提升可读性与视觉吸引力。(b) 行突出了 AesthetiQ 对元素的精确对齐以及对各种形状的最优摆位，形成统一的视觉版面。在 (c) 行，AesthetiQ 展现出高级的语义理解，生成均衡而美观的设计。总体而言，AesthetiQ 通过生成连贯、结构良好、契合人类美学偏好的版面，持续超越基线方法。附录中详述的用户研究表明，在与 FlexDM、LACE、LayoutNUWA 比较时，AesthetiQ 始终是预测版面中的首选，且人类偏好与裁判模型 ⟦SLOT_136⟧ 的偏好分布高度相关。

<!-- [原子块 · img]  -->

**EN** Figure 4: Performance improvement across scale (1B–8B parameters) for layout generation, showing effects of pretraining, quality filtering, and Aesthetic-Aware Preference Alignment (AAPA). Left: IoU progression under different training configurations. Middle: ⟦SLOT_137⟧ Win Rate improvements, emphasizing the impact of AAPA and pretraining. Right: Configuration table indicating settings for each experiment. The results underscore the impact of each design component in AesthetiQ, emphasizing their role in tackling layout generation challenges.

**ZH** 图 4：版面生成在模型规模（1B–8B 参数）上的性能提升，展示预训练、质量过滤与美学感知偏好对齐（AAPA）的作用。左：不同训练配置下的 IoU 变化。中：⟦SLOT_137⟧ 胜率的提升，突出 AAPA 与预训练的影响。右：标明各实验设置的配置表。这些结果凸显了 AesthetiQ 中每个设计组件的作用，强调它们对应对版面生成挑战的意义。

**EN** Larger Models Capture Aesthetics Better: Scaling up model size significantly improves layout generation performance. As seen in Fig 4, larger models outperform smaller ones in the metrics All, Single, Multiple IoU, and Judge Win Rate. For example, moving from 1B to 8B parameters boosts the Judge Win Rate from 2.43% to 17.19%, suggesting larger models better capture aesthetic nuances and complex spatial relationships. This trend indicates a strong alignment between model scale and the ability to reflect aesthetic preferences, making larger models more suited for aesthetic-aware layout generation. Further, this also showcases the difficulty of the layout generation task.

**ZH** 更大的模型更能捕捉美学：扩大模型规模显著改善版面生成性能。如图 4 所示，较大的模型在 All、Single、Multiple 的 IoU 以及裁判胜率上都优于较小的模型。例如，参数量从 1B 增至 8B 时，裁判胜率从 2.43% 提升到 17.19%，说明更大的模型能更好地捕捉美学细微之处与复杂空间关系。这一趋势表明模型规模与反映美学偏好的能力之间存在强相关，使更大的模型更适合美学感知的版面生成；同时也说明版面生成任务本身具有相当难度。

**EN** Pre-training Enhances Layout Understanding: Pretraining with a large dataset of 80,000 templates enhances the model’s grasp of layout structuring, providing a strong foundation for fine-tuning and AAPA. Models pretrained on this dataset show improvements across metrics. For instance, pretraining raises the 8B model’s IoU from 37.64% to 40.81%. This phase equips models with essential layout generation and understanding capabilities, which AAPA further refines to achieve aesthetic alignment.

**ZH** 预训练增强版面理解：在 80,000 个模板的大规模数据集上预训练，增强了模型对版面结构的把握，为微调与 AAPA 打下坚实基础。在该数据集上预训练的模型各项指标均有提升，例如预训练把 8B 模型的 IoU 从 37.64% 提高到 40.81%。这一阶段赋予模型必备的版面生成与理解能力，AAPA 随后加以精修，最终实现美学对齐。

**EN** Quality-metrics Based Layout Filtering Improves AAPA Training: Quality filtering, guided by alignment maximization and overlap minimization heuristics, enhances model performance by selecting high-quality layouts for training. Without filtering, aesthetic quality and layout coherence decline, as suboptimal samples impact learning. AAPA’s performance drops without filtering, with decreases in IoU across scales. Quality filtering boosts the 4B model’s IoU by 4.97% and Judge Win Rate by 2.56%, highlighting its importance in maintaining aesthetic standards.

**ZH** 基于质量指标的版面过滤改善 AAPA 训练：以对齐最大化与重叠最小化为启发式的质量过滤，通过筛选高质量版面用于训练，提升了模型性能。不过滤时，美学质量与版面连贯性会下降，因为次优样本会干扰学习；AAPA 的性能因此下滑，各规模的 IoU 均有降低。质量过滤使 4B 模型的 IoU 提升 4.97%、裁判胜率提升 2.56%，凸显了它在维持美学水准上的重要性。

**EN** Effect of AAPA on Performance: AAPA considerably enhances the aesthetic quality of generated layouts by aligning them with preferences derived from Multi-modal Large Language Models (VLMs). This preference-based alignment improves the Judge Win Rate, guiding the model towards aesthetically pleasing layouts rather than exact ground truth matches. AesthetiQ-1B model shows limited gains, as it faces challenges in producing high-quality layouts during sampling, limiting the effectiveness of preference optimization. However, AAPA-trained larger models demonstrate superior performance on Crello and WebUI benchmarks across metrics, underscoring the value of preference-based training in aesthetic-sensitive tasks.

**ZH** AAPA 对性能的影响：通过让版面与源自多模态大语言模型（VLM）的偏好对齐，AAPA 显著提升了生成版面的美学质量。这种基于偏好的对齐提高了裁判胜率，把模型引向美观的版面，而非与真值逐点吻合的版面。AesthetiQ-1B 的增益有限，因为它在采样阶段难以产出高质量版面，限制了偏好优化的效果。不过，经 AAPA 训练的更大规模模型在 Crello 与 WebUI 基准上的各项指标都表现更优，说明在美学敏感任务中基于偏好的训练确有价值。

<!-- [原子块 · img]  -->

**EN** Figure 5: Capability of AesthetiQ to generate templates in various aspect ratios by changing the canvas height and width

**ZH** 图 5：AesthetiQ 通过改变画布高度与宽度，生成各种长宽比模板的能力。

**EN** Generating Layouts with Different Aspect Ratios: Layouts must adapt to various aspect ratios across platforms. Our model maintains stable performance across common aspect ratios like 4:3, 16:9, and square formats, effectively rearranging elements to fit different dimensions. As shown in Fig 5, the model consistently produces visually balanced layouts for diverse aspect ratios, demonstrating its flexibility and robustness in generating aesthetically coherent layouts across various screen requirements.

**ZH** 生成不同长宽比的版面：版面必须适应不同平台的各种长宽比。我们的模型在 4:3、16:9 与方形等常见长宽比下保持稳定表现，能有效地重新排布元素以适应不同尺寸。如图 5 所示，模型对各种长宽比都能持续产出视觉均衡的版面，展现出在不同屏幕需求下生成美学连贯版面的灵活性与稳健性。

**EN** 6 Conclusion

**ZH** 6 结论

**EN** In this work, we introduced Aesthetic-Aware Preference Alignment (AAPA), a novel approach for training Multi-modal Large Language Models (MLLMs) in the task of aesthetic-driven layout prediction. By leveraging aesthetic preferences directly through a preference optimization mechanism, AAPA addresses critical limitations of existing generative models that lack contextual aesthetic understanding and alignment with human-like preferences. Our proposed data filtering protocol, based on layout-quality heuristics, ensures that only high-quality layouts contribute to training, further enhancing model performance. Additionally, we introduced a novel evaluation metric to assess the aesthetic superiority of generated layouts against ground-truth designs, supporting a more holistic evaluation of layout quality.

**ZH** 本文提出美学感知偏好对齐（AAPA），一种用于训练多模态大语言模型（MLLM）完成美学驱动版面预测任务的新方法。AAPA 通过偏好优化机制直接利用美学偏好，弥补了现有生成模型缺乏上下文美学理解、与类人偏好不相契合的关键缺陷。我们所提出的基于版面质量启发式的数据过滤流程，保证只有高质量版面参与训练，进一步提升了模型性能。此外，我们引入了一种新的评测指标，用于评估生成版面相对于真值设计的美学优势，从而支持对版面质量更整体的评价。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] [1] Diego Martín Arroyo, Janis Postels, and Federico Tombari. Variational transformer networks for layout generation. 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) , pages -->

<!-- [原子块 · verbatim] [2] Diego Martin Arroyo, Janis Postels, and Federico Tombari. Variational transformer networks for layout generation. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recogniti -->

<!-- [原子块 · verbatim] [3] Jacob Austin, Daniel D. Johnson, Jonathan Ho, Daniel Tarlow, and Rianne van den Berg. Structured denoising diffusion models in discrete state-spaces. In Advances in Neural Information Processing S -->

<!-- [原子块 · verbatim] [4] Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gre -->

<!-- [原子块 · verbatim] [5] Yunning Cao, Ye Ma, Min Zhou, Chuanbin Liu, Hongtao Xie, Tiezheng Ge, and Yuning Jiang. Geometry aligned variational transformer for image-conditioned layout generation. In Proceedings of the 30th -->

<!-- [原子块 · verbatim] [6] Shang Chai, Liansheng Zhuang, and Fengying Yan. LayoutDM: Transformer-based Diffusion Model for Layout Generation . In 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) ,  -->

<!-- [原子块 · verbatim] [7] Shang Chai, Liansheng Zhuang, and Fengying Yan. Layoutdm: Transformer-based diffusion model for layout generation. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognit -->

<!-- [原子块 · verbatim] [8] Jian Chen, Ruiyi Zhang, Yufan Zhou, and Changyou Chen. Towards aligned layout generation via diffusion model with aesthetic constraints. In The Twelfth International Conference on Learning Represe -->

<!-- [原子块 · verbatim] [9] Zhe Chen, Jiannan Wu, Wenhai Wang, Weijie Su, Guo Chen, Sen Xing, Zhong Muyan, Qinglong Zhang, Xizhou Zhu, Lewei Lu, Bin Li, Ping Luo, Tong Lu, Yu Qiao, and Jifeng Dai. Intern vl: Scaling up visio -->

<!-- [原子块 · verbatim] [10] Chin-Yi Cheng, Forrest Huang, Gang Li, and Yang Li. Play: parametrically conditioned layout generation using latent diffusion. In Proceedings of the 40th International Conference on Machine Learn -->

<!-- [原子块 · verbatim] [11] Biplab Deka, Zifeng Huang, Chad Franzen, Joshua Hibschman, Daniel Afergan, Yang Li, Jeffrey Nichols, and Ranjitha Kumar. Rico: A mobile app dataset for building data-driven design applications. I -->

<!-- [原子块 · verbatim] [12] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. Bert: Pre-training of deep bidirectional transformers for language understanding. In North American Chapter of the Association fo -->

<!-- [原子块 · verbatim] [13] Chaoyou Fu, Peixian Chen, Yunhang Shen, Yulei Qin, Mengdan Zhang, Xu Lin, Zhenyu Qiu, Wei Lin, Jinrui Yang, Xiawu Zheng, Ke Li, Xing Sun, and Rongrong Ji. Mme: A comprehensive evaluation benchmar -->

<!-- [原子块 · verbatim] [14] Tsu-Jui Fu, William Yang Wang, Daniel J. McDuff, and Yale Song. Doc2ppt: Automatic presentation slides generation from scientific documents. In AAAI Conference on Artificial Intelligence , 2021. -->

<!-- [原子块 · verbatim] [15] Shuyang Gu, Dong Chen, Jianmin Bao, Fang Wen, Bo Zhang, Dongdong Chen, Lu Yuan, and Baining Guo. Vector quantized diffusion model for text-to-image synthesis. In 2022 IEEE/CVF Conference on Compu -->

<!-- [原子块 · verbatim] [16] Kamal Gupta, Justin Lazarow, Alessandro Achille, Larry S. Davis, Vijay Mahadevan, and Abhinav Shrivastava. Layouttransformer: Layout generation and completion with self-attention. 2021 IEEE/CVF I -->

<!-- [原子块 · verbatim] [17] Liu He, Yijuan Lu, John Corring, Dinei Florencio, and Cha Zhang. Diffusion-based document layout generation. In Document Analysis and Recognition - ICDAR 2023: 17th International Conference, San  -->

<!-- [原子块 · verbatim] [18] Danqing Huang, Jiaqi Guo, Shizhao Sun, Hanling Tian, Jieru Lin, Zheng Hu, Chin-Yew Lin, Jian-Guang Lou, and Dongmei Zhang. A survey for graphic design intelligence, 2023. -->

<!-- [原子块 · verbatim] [19] Mude Hui, Zhizheng Zhang, Xiaoyi Zhang, Wenxuan Xie, Yuwang Wang, and Yan Lu. Unifying layout generation with a decoupled diffusion model. 2023 IEEE/CVF Conference on Computer Vision and Pattern  -->

<!-- [原子块 · verbatim] [20] Naoto Inoue, Kotaro Kikuchi, Edgar Simo-Serra, Mayu Otani, and Kota Yamaguchi. Towards Flexible Multi-modal Document Models. In Proceedings of the IEEE/CVF Conference on Computer Vision and Patte -->

<!-- [原子块 · verbatim] [21] Zhaoyun Jiang, Shizhao Sun, Jihua Zhu, Jian-Guang Lou, and Dongmei Zhang. Coarse-to-fine generative modeling for graphic layouts. Proceedings of the AAAI Conference on Artificial Intelligence , 3 -->

<!-- [原子块 · verbatim] [22] Kotaro Kikuchi, Edgar Simo-Serra, Mayu Otani, and Kota Yamaguchi. Constrained graphic layout generation via latent optimization. In Proceedings of the 29th ACM International Conference on Multime -->

<!-- [原子块 · verbatim] [23] Xiang Kong, Lu Jiang, Huiwen Chang, Han Zhang, Yuan Hao, Haifeng Gong, and Irfan Essa. Blt: Bidirectional layout transformer for controllable layout generation. In Computer Vision – ECCV 2022 , p -->

<!-- [原子块 · verbatim] [24] Hsin-Ying Lee, Lu Jiang, Irfan Essa, Phuong B. Le, Haifeng Gong, Ming-Hsuan Yang, and Weilong Yang. Neural design network: Graphic layout generation with constraints. In Computer Vision – ECCV 20 -->

<!-- [原子块 · verbatim] [25] Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer Levy, Veselin Stoyanov, and Luke Zettlemoyer. BART: Denoising sequence-to-sequence pre-training for natural la -->

<!-- [原子块 · verbatim] [26] Chenhui Li, Peiying Zhang, and Changbo Wang. Harmonious textual layout generation over natural images via deep aesthetics learning. IEEE Transactions on Multimedia , 24:3416–3428, 2022. -->

<!-- [原子块 · verbatim] [27] Jianan Li, Tingfa Xu, Jianming Zhang, Aaron Hertzmann, and Jimei Yang. LayoutGAN: Generating graphic layouts with wireframe discriminator. In International Conference on Learning Representations  -->

<!-- [原子块 · verbatim] [28] Jianan Li, Jimei Yang, Jianming Zhang, Chang Liu, Christina Wang, and Tingfa Xu. Attribute-conditioned layout gan for automatic graphic design. IEEE Transactions on Visualization and Computer Gra -->

<!-- [原子块 · verbatim] [29] Jiawei Lin, Jiaqi Guo, Shizhao Sun, Zijiang James Yang, Jian-Guang Lou, and Dongmei Zhang. Layoutprompter: awaken the design ability of large language models. In Proceedings of the 37th Internati -->

<!-- [原子块 · verbatim] [30] Ji Lin, Hongxu Yin, Wei Ping, Pavlo Molchanov, Mohammad Shoeybi, and Song Han. VILA: On Pre-training for Visual Language Models . In 2024 IEEE/CVF Conference on Computer Vision and Pattern Recogn -->

<!-- [原子块 · verbatim] [31] Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. Visual instruction tuning. ArXiv , abs/2304.08485, 2023a. -->

<!-- [原子块 · verbatim] [32] Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. Visual instruction tuning. In Thirty-seventh Conference on Neural Information Processing Systems , 2023b. -->

<!-- [原子块 · verbatim] [33] Ilya Loshchilov and Frank Hutter. SGDR: Stochastic gradient descent with warm restarts. In International Conference on Learning Representations , 2017. -->

<!-- [原子块 · verbatim] [34] Ilya Loshchilov and Frank Hutter. Decoupled weight decay regularization. In International Conference on Learning Representations , 2019. -->

<!-- [原子块 · verbatim] [35] Minesh Mathew, Dimosthenis Karatzas, and C. V. Jawahar. Docvqa: A dataset for vqa on document images. In 2021 IEEE Winter Conference on Applications of Computer Vision (WACV) , pages 2199–2208, 2 -->

<!-- [原子块 · verbatim] [36] Peter O’Donovan, Aseem Agarwala, and Aaron Hertzmann. Designscape: Design with interactive layout suggestions. In Proceedings of the 33rd Annual ACM Conference on Human Factors in Computing Syste -->

<!-- [原子块 · verbatim] [37] OpenAI, Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, and many more. Gpt-4 technical report, 2024. -->

<!-- [原子块 · verbatim] [38] Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob Hilton, Fraser Kelton, Luke Mil -->

<!-- [原子块 · verbatim] [39] Peter O’Donovan, Aseem Agarwala, and Aaron Hertzmann. Learning layouts for single-pagegraphic designs. IEEE Transactions on Visualization and Computer Graphics , 20(8):1200–1213, 2014. -->

<!-- [原子块 · verbatim] [40] Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and Chelsea Finn. Direct preference optimization: Your language model is secretly a reward model. In Advances  -->

<!-- [原子块 · verbatim] [41] Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and Chelsea Finn. Direct preference optimization: Your language model is secretly a reward model. In Thirty-se -->

<!-- [原子块 · verbatim] [42] Soliha Rahman, Vinoth Pandian Sermuga Pandian, and Matthias Jarke. Ruite: Refining ui layout aesthetics using transformer encoder. In Companion Proceedings of the 26th International Conference on -->

<!-- [原子块 · verbatim] [43] Baptiste Rozière, Jonas Gehring, Fabian Gloeckle, Sten Sootla, Itai Gat, Xiaoqing Tan, Yossi Adi, Jingyu Liu, Tal Remez, Jérémy Rapin, Artyom Kozhevnikov, I. Evtimov, Joanna Bitton, Manish P Bhat -->

<!-- [原子块 · verbatim] [44] Jaejung Seol, Seojun Kim, and Jaejun Yoo. Posterllama: Bridging design ability of language model to content-aware layout generation. In Computer Vision – ECCV 2024 , pages 451–468, Cham, 2025. Sp -->

<!-- [原子块 · verbatim] [45] Amanpreet Singh, Vivek Natarajan, Meet Shah, Yu Jiang, Xinlei Chen, Dhruv Batra, Devi Parikh, and Marcus Rohrbach. Towards vqa models that can read. In 2019 IEEE/CVF Conference on Computer Vision -->

<!-- [原子块 · verbatim] [46] Zecheng Tang, Chenfei Wu, Juntao Li, and Nan Duan. LayoutNUWA: Revealing the hidden layout expertise of large language models. In The Twelfth International Conference on Learning Representations  -->

<!-- [原子块 · verbatim] [47] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, Aurelien Rodriguez, Armand Joulin,  -->

<!-- [原子块 · verbatim] [48] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, and Illia Polosukhin. Attention is all you need. In Proceedings of the 31st International C -->

<!-- [原子块 · verbatim] [49] Chen Wei, Karttikeya Mangalam, Po-Yao (Bernie) Huang, Yanghao Li, Haoqi Fan, Hu Xu, Huiyu Wang, Cihang Xie, Alan Loddon Yuille, and Christoph Feichtenhofer. Diffusion models as masked autoencoder -->

<!-- [原子块 · verbatim] [50] Haohan Weng, Danqing Huang, Yu Qiao, Zheng Hu, Chin-Yew Lin, Tong Zhang, and C. L. Philip Chen. Desigen: A Pipeline for Controllable Design Template Generation . In 2024 IEEE/CVF Conference on Co -->

<!-- [原子块 · verbatim] [51] Kota Yamaguchi. Canvasvae: Learning to generate vector graphic documents. 2021 IEEE/CVF International Conference on Computer Vision (ICCV) , pages 5461–5469, 2021. -->

<!-- [原子块 · verbatim] [52] Tao Yang, Yingmin Luo, Zhongang Qi, Yang Wu, Ying Shan, and Chang Wen Chen. Posterllava: Constructing a unified multi-modal layout generator with llm, 2024. -->

<!-- [原子块 · verbatim] [53] Weihao Yu, Zhengyuan Yang, Linjie Li, Jianfeng Wang, Kevin Lin, Zicheng Liu, Xinchao Wang, and Lijuan Wang. Mm-vet: Evaluating large multimodal models for integrated capabilities. In Internationa -->

<!-- [原子块 · verbatim] [54] Xiang Yue, Yuansheng Ni, Kai Zhang, Tianyu Zheng, Ruoqi Liu, Ge Zhang, Samuel Stevens, Dongfu Jiang, Weiming Ren, Yuxuan Sun, Cong Wei, Botao Yu, Ruibin Yuan, Renliang Sun, Ming Yin, Boyuan Zheng -->

<!-- [原子块 · verbatim] [55] Junyi Zhang, Jiaqi Guo, Shizhao Sun, Jian-Guang Lou, and D. Zhang. Layoutdiffusion: Improving graphic layout generation by discrete diffusion probabilistic models. 2023 IEEE/CVF International Con -->

<!-- [原子块 · verbatim] [56] Xinru Zheng, Xiaotian Qiao, Ying Cao, and Rynson W. H. Lau. Content-aware generative modeling of graphic design layouts. ACM Trans. Graph. , 38(4), 2019. -->

<!-- [原子块 · verbatim] [57] Min Zhou, Chenchen Xu, Ye Ma, Tiezheng Ge, Yuning Jiang, and Weiwei Xu. Composition-aware graphic layout gan for visual-textual presentation designs. ArXiv , abs/2205.00303, 2022. -->

**EN** Supplementary Material

**ZH** 补充材料

<!-- [原子块 · img]  -->

**EN** Figure 6: Comparison of results from two user studies evaluating layout aesthetics. The bar plot (left) shows the preference of layout predictions across four methods: AesthetiQ, LayoutNUWA, LACE, and FlexDM, with AesthetiQ significantly outperforming others. The pie chart (right) evaluates alignment between human preferences and the VILA model, achieving a substantial agreement rate of 78.8%. Together, these results highlight the superiority of AesthetiQ in generating aesthetically pleasing layouts and the reliability of VILA as an evaluator.

**ZH** 图 6：两项评估版面美学的用户研究结果对比。左图柱状图展示了 AesthetiQ、LayoutNUWA、LACE 与 FlexDM 四种方法的版面预测偏好，AesthetiQ 显著优于其他方法。右图饼图评估人类偏好与 VILA 模型的一致程度，达到 78.8% 的可观一致率。两项结果共同凸显了 AesthetiQ 在生成美观版面方面的优势，以及 VILA 作为评估者的可靠性。

**EN** 7 User Study

**ZH** 7 用户研究

**EN** To evaluate the aesthetic quality of layouts generated by various methods and validate the alignment of human preferences with our approach, we conducted two user studies involving 22 diverse volunteers. The participants were selected to represent a broad spectrum of demographics, including variations in age, gender, occupation, and religion, ensuring a well-rounded and inclusive evaluation. Each participant was presented with a total of 30 questions, designed to capture their aesthetic preferences and opinions on the generated layouts.

**ZH** 为评估各方法生成版面的美学质量，并验证人类偏好与本方法的一致性，我们开展了两项用户研究，邀请 22 位背景多样的志愿者参与。参与者的选取覆盖了广泛的人口统计学特征，在年龄、性别、职业与宗教信仰上均有差异，以保证评估的全面与包容。每位参与者需回答共 30 道问题，用以采集他们对生成版面的美学偏好与看法。

**EN** User Study 1:

**ZH** 用户研究 1：

**EN** Participants were shown layout predictions from four methods: AesthetiQ, LayoutNUWA, LACE, and FlexDM. They were instructed to select the better layout based on aesthetics, alignment and overlap between text and images, and whether the text in the layout made sense. The results are as follows:

**ZH** 向参与者展示 AesthetiQ、LayoutNUWA、LACE 与 FlexDM 四种方法的版面预测结果，请他们依据美学、文本与图像之间的对齐与重叠情况，以及版面中的文字是否讲得通，来选出更好的版面。结果如下：

**EN** • AesthetiQ: 78.41%

**ZH** • AesthetiQ：78.41%

**EN** • LayoutNUWA [46]: 19.37%

**ZH** • LayoutNUWA [46]：19.37%

**EN** • LACE [8]: 2.22%

**ZH** • LACE [8]：2.22%

**EN** • FlexDM [20]: 0.00%

**ZH** • FlexDM [20]：0.00%

**EN** These results highlight the significant preference for layouts generated by AesthetiQ compared to the baselines, underscoring its ability to produce more visually appealing and coherent designs.

**ZH** 这些结果说明，与基线相比参与者显著偏好 AesthetiQ 生成的版面，印证了它产出更具视觉吸引力且更连贯设计的能力。

**EN** User Study 2:

**ZH** 用户研究 2：

**EN** Participants were shown pairs of model-generated layouts and asked to select the better one using the same instructions as in the first study. The same layouts were also evaluated by VILA, a Vision-Language Model (VLM) judge. We measured the agreement between human preferences and VILA’s outputs, which yielded an alignment score of 78.8%.

**ZH** 向参与者成对展示模型生成的版面，并使用与第一次研究相同的说明请他们选出更好的一个。同样的版面也交由视觉语言模型（VLM）裁判 VILA 评判。我们衡量人类偏好与 VILA 输出之间的一致程度，得到 78.8% 的对齐分数。

**EN** This result demonstrates that VILA’s aesthetic judgment aligns well with human preferences, further validating its use as an aesthetic evaluator in our framework.

**ZH** 这一结果表明 VILA 的美学判断与人类偏好高度吻合，进一步验证了它作为本框架中美学评估者的合理性。

**EN** 8 Complete Results on WebUI

**ZH** 8 WebUI 上的完整结果

<!-- [原子块 · table] Method Mean IoU (%) ℳ judge \mathcal{M}_{\text{judge}} Win Rate (%) Desigen [ 50 ] 15.36 4.81 LACE [ 8 ] 17.88 5.27 PosterLLaVa [ 52 ] 30.19 14.73 LayoutNUWA [ 46 ] 32.16 15.28 AesthetiQ-1B 38.47 19.2 -->

**EN** Table 3: Comparison of AesthetiQ with baseline methods on the WebUI dataset, evaluated using Mean IoU (%) and ⟦SLOT_138⟧ Win Rate (%). The results demonstrate the superior performance of AesthetiQ across all model scales, with notable gains in aesthetic and structural alignment metrics.

**ZH** 表 3：在 WebUI 数据集上用平均 IoU（%）与 ⟦SLOT_138⟧ 胜率（%）比较 AesthetiQ 与基线方法。结果展示了 AesthetiQ 在所有模型规模上的优越性能，在美学与结构对齐指标上均有显著增益。

**EN** Table 3 provides a detailed comparison of our approach, AesthetiQ, against baseline methods, including Desigen, LACE, PosterLLaVa, and LayoutNUWA. While previous methods like PosterLLaVa and LayoutNUWA achieve decent performance, they fall short in terms of both structural coherence and aesthetic alignment. In contrast, AesthetiQ shows consistent improvements across all metrics, achieving the highest Mean IoU and ⟦SLOT_139⟧ Win Rate.

**ZH** 表 3 详细比较了本方法 AesthetiQ 与 Desigen、LACE、PosterLLaVa、LayoutNUWA 等基线方法。PosterLLaVa 与 LayoutNUWA 等先前方法虽取得了尚可的表现，但在结构连贯性与美学对齐两方面都有所欠缺。相比之下，AesthetiQ 在全部指标上持续改进，取得了最高的平均 IoU 与 ⟦SLOT_139⟧ 胜率。

**EN** We observe a clear trend of performance scaling with model size. The Mean IoU improves progressively from 38.47% for the 1B model to 48.29% for the 8B model. Similarly, the Judge Win Rate increases from 19.29% to 24.48%, showcasing the model’s alignment with human aesthetic preferences as the scale grows. In the main paper, due to space constraints, we presented results for only the 1B and 8B variants of AesthetiQ. Here, we include results for the 2B and 4B variants to offer a comprehensive analysis of our model’s performance across different scales. The full results underscore the scalability and effectiveness of our approach, particularly in leveraging aesthetic preferences to optimize layout quality.These findings highlight the robustness of AesthetiQ in addressing the challenges of layout generation, establishing a new benchmark for performance on the WebUI dataset.

**ZH** 我们观察到性能随模型规模提升的清晰趋势：平均 IoU 从 1B 模型的 38.47% 逐步提升到 8B 模型的 48.29%；裁判胜率同样从 19.29% 上升到 24.48%，说明随着规模增长，模型与人类美学偏好的契合度不断提高。受篇幅所限，正文只给出了 AesthetiQ 的 1B 与 8B 变体结果；这里补充 2B 与 4B 变体的结果，以便对不同规模下模型性能做更全面的分析。完整结果凸显了本方法的可扩展性与有效性，尤其是在利用美学偏好优化版面质量方面。这些发现说明 AesthetiQ 在应对版面生成挑战上十分稳健，为 WebUI 数据集上的性能树立了新的基准。

**EN** In the paper, we primarily focus on showcasing qualitative results on the Crello dataset, as it contains individual elements, allowing for detailed analysis and visualization. In contrast, the WebUI dataset only includes category labels and their positions, making it impossible to generate the final rendered templates. For the AAPA evaluation, we render the bounding boxes of the predicted elements on a background, similar to the approach used in Desigen [50]. These renderings are then evaluated by the judge VLM, which selects the layout it deems superior between the two.

**ZH** 正文中我们主要展示 Crello 数据集上的定性结果，因为它包含独立元素，便于做细致的分析与可视化；相比之下，WebUI 数据集只有类别标签及其位置，无法生成最终渲染的模板。在 AAPA 评测中，我们把预测元素的边界框渲染到背景上，做法与 Desigen [50] 类似。这些渲染结果随后交由裁判 VLM评判，由它在两者之间选出自己认为更优的版面。

<!-- [原子块 · table] AAPA 𝒜 judge \mathcal{A}_{\text{judge}} Mean IoU (%) ↑ \uparrow Eval ℳ judge \mathcal{M}_{\text{judge}} ℳ judge \mathcal{M}_{\text{judge}} Win Rate (%) ↑ \uparrow All Single Multiple VILA (Paper) 42.8 -->

**EN** Table 4: Comparison of AesthetiQ-8B with different training (⟦SLOT_140⟧) & eval (⟦SLOT_141⟧) judges. mIoU is independent of ⟦SLOT_142⟧.

**ZH** 表 4：AesthetiQ-8B 在使用不同训练裁判（⟦SLOT_140⟧）与评测裁判（⟦SLOT_141⟧）时的比较。mIoU 与 ⟦SLOT_142⟧ 无关。

**EN** 9 Stronger MLLM training

**ZH** 9 使用更强的 MLLM 训练

**EN** We chose VILA-7B as the judge for its open-source, license-friendly nature. Training and evaluation with GPT-4o (Tab 4) improved all metrics with consistent trends in ⟦SLOT_143⟧ win rate across ablations (Paper Fig. 4).

**ZH** 我们选择 VILA-7B 作为裁判，是因为它开源且许可友好。用 GPT-4o 训练与评测（表 4）后，各项指标均有提升，⟦SLOT_143⟧ 胜率在各组消融中保持一致的趋势（正文图 4）。

**EN** Justification for MLLM as judge:

**ZH** 以 MLLM 作裁判的合理性：

**EN** We conduct a user study to measure VILA’s correlation with human aesthetic preferences, finding 78.8% agreement. GPT-4o achieves 88.6% correlation, & AesthetiQ-8B performs better with a stronger judge (Tab 4).

**ZH** 我们开展用户研究来衡量 VILA 与人类美学偏好的相关性，得到 78.8% 的一致率。GPT-4o 的相关性达到 88.6%，而 AesthetiQ-8B 在更强的裁判下表现更好（表 4）。

**EN** 10 Detailed Experimental Results

**ZH** 10 详细实验结果

**EN** This section provides the complete experimental results referenced in the main paper, presented in Table 5. The table details the performance of our models across various configurations, highlighting the effects of scaling, pretraining, VILA alignment, and quality filtering on layout generation tasks. Metrics include All IoU, Single Text IoU, Multiple Text IoU, and Judge Win Rate. These results support the analysis presented in Section 5 of the main paper, showcasing the effectiveness of Aesthetic-Aware Preference Alignment (AAPA) and other components in enhancing the quality and alignment of generated layouts.

**ZH** 本节给出正文中引用的完整实验结果，见表 5。该表详述了我们的模型在多种配置下的性能，突出规模化、预训练、VILA 对齐与质量过滤对版面生成任务的影响，指标包括 All IoU、单文本 IoU、多文本 IoU 与裁判胜率。这些结果支撑了正文第 5 节的分析，展示了美学感知偏好对齐（AAPA）及其他组件在提升生成版面质量与对齐度上的有效性。

<!-- [原子块 · table] Method LLM Pretraining VILA Alignment Data Filtering Mean IoU ℳ judge \mathcal{M}_{\text{judge}} Win Rate (%) All Single Multiple AesthetiQ -1B Qwen-0.5b No No No 22.06 40.14 24.88 2.18 AesthetiQ -1B  -->

**EN** Table 5: Performance of AesthetiQ across scales (1B, 2B, 4B, 8B) on the Crello dataset, evaluating the effects of pretraining, VILA alignment, and data filtering on IoU metrics and judge win rates. The results demonstrate the scalability and effectiveness of the aesthetic-aware preference alignment method.

**ZH** 表 5：AesthetiQ 在 Crello 数据集上跨规模（1B、2B、4B、8B）的性能，考察预训练、VILA 对齐与数据过滤对 IoU 指标和裁判胜率的影响。结果展示了美学感知偏好对齐方法的可扩展性与有效性。

**EN** 11 Direct Preference Optimization

**ZH** 11 直接偏好优化

**EN** Direct Preference Optimisation (DPO) [40] emerged as an alternative approach to Reinforcement Learning using Human Feedback (RLHF) [38], eliminating the requirement of training a reward model. While RLHF relies on a reward model to evaluate LLM outputs for fine-tuning through reinforcement learning to achieve human preference alignment, DPO takes a different approach. It converts the reward-function loss into a loss over the LLM policy, enabling implicit reward optimization through policy loss optimization. This is achieved using human preference data that pairs two LLM-generated outputs, where one is designated as the winner candidate - ⟦SLOT_144⟧ and the other as the loser candidate - ⟦SLOT_145⟧. Using a static dataset structured as ⟦SLOT_146⟧, where x represents the input, the loss is formulated as:

**ZH** 直接偏好优化（DPO）[40] 作为基于人类反馈的强化学习（RLHF）[38] 的替代方案出现，免去了训练奖励模型的需要。RLHF 依赖奖励模型评估 LLM 输出，再通过强化学习微调以实现人类偏好对齐；DPO 则另辟蹊径，把奖励函数上的损失转化为 LLM 策略上的损失，从而通过优化策略损失隐式地优化奖励。这一做法使用成对的人类偏好数据，其中两个 LLM 生成的输出分别被指定为胜出候选 ⟦SLOT_144⟧ 与落败候选 ⟦SLOT_145⟧。使用结构为 ⟦SLOT_146⟧ 的静态数据集（其中 x 表示输入），损失表述为：

<!-- [原子块 · table] ℒ R = − l ​ o ​ g ​ [ σ ⁡ ( r ⁡ ( x , y w ) − r ⁡ ( x , y l ) ) ] \displaystyle\mathcal{L}_{R}=-log[\sigma(r(x,y_{w})-r(x,y_{l}))] (11) r ⁡ ( x , y ) = β ​ l ​ o ​ g ​ ( π θ ​ ( y | x ) π r ​ e ​ f ​  -->

**EN** Here, ⟦SLOT_147⟧ denotes the probability of generating ⟦SLOT_148⟧ given input ⟦SLOT_149⟧ for model ⟦SLOT_150⟧, where ⟦SLOT_151⟧ typically represents the instruction fine-tuned model for LLMs to maintain policy proximity to the initial model, and ⟦SLOT_152⟧ represents the LLM policy being optimized through DPO. Additionally, ⟦SLOT_153⟧ represents the sigmoid activation, and ⟦SLOT_154⟧ is a parameter controlling the deviation extent from the reference model. In essence, this algorithm trains the LLM to develop output preferences among candidates without explicitly modeling rewards. Our algorithm Aesthetic-Aware Preference Alignment (AAPA) draws motivation from DPO and carries out preferential training across different layout configurations. For a more comprehensive understanding on DPO, readers are directed to the original publication [40].

**ZH** 其中 ⟦SLOT_147⟧ 表示生成 ⟦SLOT_148⟧ 的概率，给定输入为 ⟦SLOT_149⟧、模型为 ⟦SLOT_150⟧；⟦SLOT_151⟧ 通常代表经过指令微调的模型，用于使策略与初始模型保持接近，而 ⟦SLOT_152⟧ 表示通过 DPO 优化的 LLM 策略。此外，⟦SLOT_153⟧ 表示 sigmoid 激活函数，⟦SLOT_154⟧ 是控制与参考模型偏离程度的参数。本质上，该算法训练 LLM 在候选输出之间形成偏好，而无需显式地对奖励建模。我们的算法美学感知偏好对齐（AAPA）正是受 DPO 启发，并在不同的版面配置之间执行偏好训练。关于 DPO 的更全面理解，请读者参阅原始文献 [40]。

**EN** 12 Prompt Templates for Layout and Judge VLMs

**ZH** 12 版面模型与裁判 VLM 的提示模板

**EN** The following prompt template was used as input to our layout generation model ⟦SLOT_155⟧ to guide the generation of aesthetic poster layouts. The template specifies the canvas dimensions and provides a structured description of the elements to be placed, including their type (e.g., text or image), content, and category. This format allows the model to interpret the spatial constraints and semantic attributes of each element effectively, enabling systematic exploration of layout generation. The <image> token in the prompt is replaced with a sequence of image embeddings corresponding to the input images, ensuring that the model processes visual information in a compact and meaningful way. By explicitly defining these attributes, the template facilitates reproducibility and evaluation of layout designs. The prompt template is shown below:

**ZH** 以下提示模板用作版面生成模型 ⟦SLOT_155⟧ 的输入，用以指导美观海报版面的生成。模板指定画布尺寸，并对要摆放的元素给出结构化描述，包括类型（如文本或图像）、内容与类别。这一格式使模型能有效理解每个元素的空间约束与语义属性，从而系统地探索版面生成。提示中的 <image> 词元会被替换为与输入图像对应的一串图像嵌入，保证模型以紧凑而有意义的方式处理视觉信息。通过显式定义这些属性，该模板为版面设计的可复现性与评估提供了便利。提示模板如下：

**EN** Consider the image <image> with height and width of {canvas_height} and {canvas_width}. The following elements need to be placed on the image to obtain an aesthetic poster layout.

**ZH** 考虑图像 <image>，其高度与宽度分别为 {canvas_height} 与 {canvas_width}。需要在该图像上摆放以下元素，以获得一个美观的海报版面。

**EN** Element 1: Text: LOREM IPSUM Category: text

**ZH** 元素 1：文本：LOREM IPSUM 类别：text

**EN** Element 2: Image: <image> Category: image

**ZH** 元素 2：图像：<image> 类别：image

**EN** ...

**ZH** …

**EN** This structured input format ensures that the model can accurately process both visual and textual elements while adhering to aesthetic principles, making it particularly suitable for tasks in computer vision and graphics.

**ZH** 这种结构化输入格式确保模型既能准确处理视觉元素，也能准确处理文本元素，同时遵循美学原则，因而特别适用于计算机视觉与图形学中的任务。

**EN** The following prompt is used as input to the judge visual language model ⟦SLOT_156⟧ to evaluate and compare two visual templates based on predefined criteria: aesthetics, clarity, usability, creativity, and consistency. The model processes these criteria to determine which template is superior and outputs the result in a structured JSON format: {"better_layout": "answer"}, where the answer specifies the preferred template (image_1 or image_2). This structured approach ensures objective and standardized evaluation of visual designs. The prompt is shown below:

**ZH** 以下提示用作裁判视觉语言模型 ⟦SLOT_156⟧ 的输入，用于依据预设准则——美学、清晰度、可用性、创造力与一致性——评估并比较两个视觉模板。模型依据这些准则判定哪个模板更优，并以结构化 JSON 格式输出结果：{"better_layout": "answer"}，其中 answer 指明被偏好的模板（image_1 或 image_2）。这种结构化方式保证了对视觉设计做客观、规范的评估。提示如下：

**EN** You are a visual language model designed to evaluate and rate visual templates. You are presented with 2 visual templates, and your task is to choose the better template between these 2 based on the following criteria:

**ZH** 你是一个用于评估与评分视觉模板的视觉语言模型。现在向你展示 2 个视觉模板，你的任务是根据以下准则从中选出更好的一个：

**EN** Aesthetics: How visually appealing is the template, Clarity: How clear and easy to understand is the template, Usability: How practical and user-friendly is the template, Creativity: How unique and innovative is the design, Consistency: How consistent is the template with design principles and standards.

**ZH** 美学：模板在视觉上是否吸引人；清晰度：模板是否清晰易懂；可用性：模板是否实用、易用；创造力：设计是否独特新颖；一致性：模板与设计原则和规范是否一致。

**EN** Please provide your answer in the following JSON format and do not include any other details:

**ZH** 请按以下 JSON 格式给出你的回答，不要包含任何其他内容：

**EN** {"better_layout": "answer"}

**ZH** {"better_layout": "answer"}

**EN** where answer could either be image_1 or image_2.

**ZH** 其中 answer 可以是 image_1 或 image_2。

**EN** 13 Qualitative results

**ZH** 13 定性结果

**EN** Due to limited space, we included only a few examples of comparison in the main paper. In the following pages, we show more examples for a more comprehensive comparison.

**ZH** 受篇幅限制，正文中只收录了少量对比示例。在接下来的几页中，我们给出更多示例，以进行更全面的比较。

<!-- [原子块 · img]  -->

**EN** Figure 7: Qualitative comparison of various baselines for layout prediction

**ZH** 图 7：各基线方法在版面预测上的定性比较
