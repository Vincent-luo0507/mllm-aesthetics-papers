# PosterIQ：面向海报理解与生成的设计视角基准

> 原标题：PosterIQ: A Design Perspective Benchmark for Poster Understanding and Generation
> 作者：Yuheng Feng, Wen Zhang, Haodong Duan, Xingxing Zou · arXiv:2603.24078 · 2026-03-25

<!-- [原子块 · verbatim] PosterIQ: A Design Perspective Benchmark for Poster Understanding and Generation -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] We present PosterIQ, a design-driven benchmark for poster understanding and generation, annotated across composition structure, typographic hierarchy, and semantic intent. It includes 7,765 image–anno -->

**EN** 1 Introduction

**ZH** 1 引言

**EN** Multimodal large language models (MLLMs) [5, 28, 2] have recently advanced in visual understanding—from object and scene recognition to cross-modal alignment, fine-grained parsing, and open-vocabulary detection—enabling high-level semantics and robust reasoning in complex contexts. In parallel, generative models have progressed across text-to-image, image-to-image, and interactive co-creation, with emerging strengths in style control, layout composition, and semantic consistency. These gains are especially evident in creative applications, where models show tangible innovation and practical utility in advertising, branding, and visual metaphor, while LLMs increasingly aid story ideation, tone transfer and narrative structuring.

**ZH** 多模态大语言模型（MLLM）[5, 28, 2] 近期在视觉理解上持续进步——从物体与场景识别，到跨模态对齐、细粒度解析与开放词汇检测——使模型得以在复杂语境中把握高层语义并稳健推理。与此同时，生成模型在文生图、图生图与人机协同创作方面不断推进，在风格控制、版面构成与语义一致性上展现出新的优势。这些进展在创意应用中尤为明显：模型在广告、品牌塑造与视觉隐喻方面体现出切实的创新能力与实用价值，而大语言模型也越来越多地辅助故事构思、语调迁移与叙事结构设计。

**EN** Despite benchmarks like [7], evaluations remain largely text-centric. Image-generation assessments often prioritize aesthetics and overlook the compositional, constraint-driven nature of design. This omission is most acute in posters—a tightly integrated medium where visual understanding and content generation must align under strict constraints. Here, theme interpretation, information hierarchy, typographic rules, text–image coupling, theme consistency, and audience preference interact in ways single-dimensional metrics fail to capture as “genuine creativity.” Posters are not merely about visual appeal; they are visual communication media designed to ensure key messages are perceived, understood, and remembered with minimal cognitive load. Design without communicative purpose yields only superficial elegance. Effective poster design integrates robust text recognition, semantic understanding, faithful rendering, and hierarchical layout to keep critical elements legible in dense compositions; typographic choices must balance readability and beauty; overall style must align with audience and theme; and visual devices such as metaphor, symbolism, and whitespace should reinforce messages and aid memory through visual rhetoric. Accordingly, key assessment dimensions include accurate text understanding, goal-directed typography and layout, coherent text–image coordination, style control under audience and thematic constraints, and creative expression through metaphor—all grounded in understanding of design rules and theory, plus good taste and creative thinking, whose integration separates strong design from the merely adequate.

**ZH** 尽管已有 [7] 等基准，现有评测仍以文本为中心。图像生成评测往往偏重美学，忽略设计的构成性与约束驱动本质。这一缺失在海报上最为突出——海报是一种高度整合的媒介，其视觉理解与内容生成必须在严格约束下达成一致。在其中，主题解读、信息层次、字体排印规则、图文耦合、主题一致性与受众偏好相互作用，单维指标无法将其刻画为“真正的创造力”。海报不止关乎视觉吸引力，它还是一种视觉传达媒介，旨在以最小的认知负荷确保关键信息被看见、被理解并被记住。缺乏传达目的的设计只能得到表面的精致。有效的海报设计需要融合稳健的文字识别、语义理解、忠实渲染与层次化版面，使关键元素在密集构成中保持清晰可读；字体排印的选择须兼顾可读性与美感；整体风格须与受众和主题相称；隐喻、象征与留白等视觉手法应通过视觉修辞强化信息、辅助记忆。据此，核心评测维度包括：准确的文本理解、目标导向的字体排印与版面、连贯的图文协同、受众与主题约束下的风格控制，以及通过隐喻实现的创造性表达——这些维度均以对设计规则与理论的理解为基础，再加上良好的品味与创造性思维，其融合程度正是优秀设计与平庸设计的分野。

**EN** From a modeling perspective, poster-oriented understanding and generation systems must jointly satisfy: (1) text understanding and readability via robust OCR and font recognition, readability prediction (glyph shape, weight, size, contrast) with constraint-aware optimization, and automatic text hierarchy and structured layout; (2) layout reasoning and hierarchical organization through explicit modeling of grids, whitespace, alignment, layering, and figure–ground relationships for global optimization across elements, sizes, and densities; (3) semantic–style consistency with task- and audience-aware style retrieval or transfer under target constraints, suppressing style noise that could obscure key information; (4) text–image coordination and saliency control that transforms key messages into semantically aligned visuals and directs attention so core information is perceived first; and (5) rhetorical modeling and metaphor generation that produce decodable visual metaphors via semantic association and analogy while balancing novelty against misinterpretation risks.

**ZH** 从建模角度看，面向海报的理解与生成系统必须同时满足以下要求：（1）文本理解与可读性——依靠稳健的 OCR 与字体识别、可读性预测（字形、字重、字号、对比度）并结合约束感知的优化，以及自动的文本层级与结构化版面；（2）版面推理与层级组织——显式建模网格、留白、对齐、分层及图形—背景关系，在元素、尺寸与密度之间实现全局优化；（3）语义—风格一致性——在目标约束下进行任务与受众感知的风格检索或迁移，抑制可能遮蔽关键信息的风格噪声；（4）图文协同与显著性控制——把关键信息转化为语义对齐的视觉元素，并引导注意力，使核心信息被优先感知；（5）修辞建模与隐喻生成——通过语义联想与类比产生可解码的视觉隐喻，同时在新颖性与误读风险之间取得平衡。

**EN** To address this, we introduce PosterIQ: a systematic benchmark for highly constrained poster creation that spans the full pipeline—from understanding and ideation to composition and generation—and more comprehensively characterizes MLLMs’ creative capabilities in poster understanding and synthesis. As shown in Fig. 1, it comprises two tightly coupled, design–oriented components: an understanding module with a global quality assessment (overall rating) and four decoupled task families—(i) OCR and text readability, (ii) font shape perception and attribute understanding, (iii) multidimensional layout and hierarchy perception, and (iv) high-level style recognition, visual deconstruction, and semantic communication—and a generation module that exceeds existing benchmarks by (i) generating and organizing high-density visual content, (ii) accurately generating dense text with diverse fonts, (iii) enabling controllable poster style and thematic tone, (iv) supporting challenging structural decomposition and recomposition of visual elements, and (v) facilitating intention communication and creative evaluation via metaphor and visual rhetoric; overall, PosterIQ advances verifiable creativity in real-world design scenarios through actionable tasks, reproducible metrics, and decoupled evaluation dimensions. From a broad empirical analysis, it reveals systematic gaps between open-source and proprietary models. Frontier commercial systems generally perform better on high-level tasks such as layout reasoning, composition understanding, and intention interpretation. However, when used as automatic raters for poster quality, their scores often lack sensitivity and fail to clearly separate strong and weak designs. In the generation setting, current models already demonstrate strong visual synthesis and text rendering capabilities, but still struggle with composition-aware generation and clear expression of design intentions. A cross-model comparison further shows noticeable differences in the richness and diversity of generated typography across systems. All in all, our contributions are:

**ZH** 为此，我们提出 PosterIQ：一个面向强约束海报创作的系统化基准，覆盖从理解与构思到构图与生成的完整流程，更全面地刻画 MLLM 在海报理解与合成中的创造能力。如图 1 所示，它包含两个紧密耦合、面向设计的组成部分：其一是理解模块，含全局质量评估（整体评分）与四类解耦的任务族——（i）OCR 与文本可读性，（ii）字体形态感知与属性理解，（iii）多维版面与层次感知，（iv）高层风格识别、视觉解构与语义传达；其二是生成模块，相较现有基准更进一步：（i）生成并组织高密度视觉内容，（ii）以多样字体精确生成密集文本，（iii）支持可控的海报风格与主题基调，（iv）支持视觉元素具有挑战性的结构分解与重组，（v）借助隐喻与视觉修辞促进意图传达与创意评价。整体而言，PosterIQ 通过可执行的任务、可复现的指标与解耦的评测维度，推进真实设计场景中可验证的创造力。大规模实证分析揭示了开源模型与闭源模型之间的系统性差距：前沿商用系统在版面推理、构图理解与意图解读等高层任务上整体表现更好；然而当它们充当海报质量的自动评分器时，其分数往往缺乏敏感度，无法明确区分设计的优劣。在生成场景下，现有模型已展现出较强的视觉合成与文本渲染能力，但在构图感知的生成与设计意图的清晰表达上仍有困难。跨模型对比还显示，各系统所生成字体排印的丰富度与多样性存在明显差异。综上，我们的贡献如下：

**EN** • Data. We build a comprehensive poster-centric benchmark with 7,765 image–annotation instances for understanding and 822 prompts for generation, combining real-world posters, professionally designed layouts, and synthetic cases for typography, layout, and metaphor.

**ZH** • 数据。我们构建了一个以海报为核心的综合基准，包含 7,765 个图像—标注实例用于理解，822 条提示词用于生成，融合真实海报、专业设计版面与合成案例，覆盖字体排印、版式与隐喻。

**EN** • Task Coverage. We provide an in-depth and systematic evaluation of poster-related abilities, covering OCR robustness, font perception, multi-dimensional layout and spatial reasoning, high-level style and intention understanding, as well as dense, style-aware, composition-aware, and metaphor-driven generation.

**ZH** • 任务覆盖。我们对海报相关能力进行了系统而细致的评测，涵盖 OCR 鲁棒性、字体感知、多维版面与空间推理、高层风格与意图理解，以及密集、风格感知、构图感知与隐喻驱动的生成。

**EN** • Evaluation Benchmark. We introduce PosterIQ as a rigorous, task-specific evaluation framework with reproducible metrics tailored to each challenge. Our analysis offers fine-grained insights into accuracy, robustness, aesthetic judgement, and creative intent.

**ZH** • 评测基准。我们把 PosterIQ 设计为一个严谨的、面向具体任务的评测框架，为每项挑战配设可复现的指标。我们的分析针对准确率、鲁棒性、美学判断与创意意图提供了细粒度洞察。

<!-- [原子块 · img]  -->

**EN** Figure 1: Overview of the benchmark, which includes over a dozen tasks

**ZH** 图 1：基准概览，包含十余项任务。

**EN** 2 Related Work

**ZH** 2 相关工作

**EN** 2.1 Multimodal Benchmarks

**ZH** 2.1 多模态基准

**EN** A growing range of benchmarks evaluates MLLMs across diverse tasks [12, 31, 36, 3, 17]. Concurrently, some studies explicitly investigate cross-modal diversity and complex semantic alignment [37, 38, 13]. As visual modality emerged, vision–language benchmarks such as MMBench [23], Creation-MMBench [7], and Seed-Bench-2-Plus [21] began testing multimodal understanding and instruction following from everyday recognition to complex reasoning. OCR-focused suites [24, 9] target scene text recognition and structured extraction. Image generation is now systematically assessed: ELLA’s DPG measures fine-grained prompt adherence under dense descriptions [15], while GenEval evaluates text–image alignment for multi-object, multi-attribute, and relational prompts [11]. For text rendering within images, TextCrafter’s CVTG-2K tests readability and fidelity in complex scenes [6], and X-Omni’s LongText-Bench (English/Chinese) probes paragraph-level rendering and layout consistency [10]. Specialized evaluations cover narrower domains—VGBench [44], ChartQA [25], and InfographicVQA [26] for vector graphics and chart reasoning; LiveIdeaBench [32] and DesignProbe [22] for ideation-centric evaluation; and UI-Vision [27] for desktop GUIs.

**ZH** 越来越多的基准在多样任务上评测 MLLM [12, 31, 36, 3, 17]。同时，一些研究专门考察跨模态多样性与复杂语义对齐 [37, 38, 13]。随着视觉模态的兴起，MMBench [23]、Creation-MMBench [7]、Seed-Bench-2-Plus [21] 等视觉—语言基准开始检验多模态理解与指令遵循，范围从日常识别延伸至复杂推理。面向 OCR 的测试集 [24, 9] 针对场景文字识别与结构化抽取。图像生成也已被系统评测：ELLA 的 DPG 在密集描述下度量细粒度的提示词遵循度 [15]，GenEval 则针对多物体、多属性与关系型提示词评测图文对齐 [11]。针对图像内文字渲染，TextCrafter 的 CVTG-2K 检验复杂场景下的可读性与保真度 [6]，X-Omni 的 LongText-Bench（英文/中文）考察段落级渲染与版面一致性 [10]。面向更窄领域的专门评测包括：面向矢量图形与图表推理的 VGBench [44]、ChartQA [25] 与 InfographicVQA [26]；面向创意构思评测的 LiveIdeaBench [32] 与 DesignProbe [22]；以及面向桌面图形界面的 UI-Vision [27]。

**EN** In contrast, PosterIQ adopts a visual design perspective, emphasizing creative poster design, making it more challenging and closer to real-world design practice.

**ZH** 与之不同，PosterIQ 采用视觉设计视角，强调创意海报设计，因而更具挑战性，也更贴近真实的设计实践。

**EN** 2.2 Poster Design and Generative Models

**ZH** 2.2 海报设计与生成模型

**EN** Diffusion models are emerging as the leading approach for high-quality image synthesis [43, 1, 20], lowering the barrier for non-experts to engage in creative design. Beyond static images, diffusion-based methods support controllable pipelines for structured manipulation of layout, typography, and style. Recent multimodal image generators—Qwen-Image [39], Seedream 4.0 [35], GPT-Image-1 [29], and Gemini 2.5 Flash Image [8]—improve efficiency in T2I and image-editing. As these models advance, interest grows in poster design. Hierarchical frameworks like instruction-tuned models like PosterLLaVA [40] and COLE [18] enable automatic poster generation, while VASCAR [42] targets content-aware layout. FontCLIP [34], ControlText [19], and FontTS [33] advance semantic typography and font control, building on early crowdsourced studies of font attributes [30]. Pipeline-based automation is realized in systems such as OpenCOLE [16]. PosterCraft [4] uses Gemini to generate training captions, and DreamPoster [14] uses a specialized captioner for glyph- and layout-level descriptions. Our benchmark shifts the focus to the evaluation of understanding and generation in poster design.

**ZH** 扩散模型正成为高质量图像合成的主流方案 [43, 1, 20]，降低了非专业人士参与创意设计的门槛。除静态图像外，基于扩散的方法还支持对版式、字体排印与风格进行结构化操控的可控流程。近期的多模态图像生成器——Qwen-Image [39]、Seedream 4.0 [35]、GPT-Image-1 [29] 与 Gemini 2.5 Flash Image [8]——提升了文生图与图像编辑的效率。随着这些模型进步，海报设计受到越来越多的关注。PosterLLaVA [40] 与 COLE [18] 等经指令微调的层次化框架实现了海报自动生成，VASCAR [42] 则面向内容感知的版式。FontCLIP [34]、ControlText [19] 与 FontTS [33] 在早期字体属性众包研究 [30] 的基础上推进了语义字体排印与字体控制。OpenCOLE [16] 等系统实现了基于流程的自动化。PosterCraft [4] 使用 Gemini 生成训练字幕，DreamPoster [14] 则采用专用字幕器生成字形级与版面级的描述。我们的基准把重心转向海报设计中理解与生成的评测。

**EN** 3 Benchmark

**ZH** 3 基准

**EN** 3.1 Understanding Tasks

**ZH** 3.1 理解任务

**EN** OCR Tasks. To support poster understanding and design-oriented reasoning, MLLMs must first show reliable visual text recognition. Our benchmark targets poster-specific traits and evaluates OCR across five sub-tasks: 1) Logo OCR—recognizing highly stylized, distorted, or abstracted logo typography with irregular character shapes; 2) Real-World Poster OCR—handling complex scenes with diverse fonts, scales, dense layouts, and textured backgrounds where text–graphic interactions raise difficulty; 3) Simple OCR—estimating upper-bound performance by rendering Oxford 3000 words with varied fonts and casing as length-balanced sequences on white backgrounds; 4) Hard OCR—testing robustness via unordered letter sequences (excluding ambiguous “l”/“I”) rendered in varied fonts, slight rotations, random colors, and placed on highly textured, colorful backgrounds from real images; 5) Multi-Size OCR—assessing stability under scale variation by generating unordered letter sequences in 14 font sizes with a base font on white, repeated across multiple fonts.

**ZH** OCR 任务。为支持海报理解与面向设计的推理，MLLM 首先须具备可靠的视觉文字识别能力。我们的基准针对海报的独有特征，在五个子任务上评测 OCR：1）Logo OCR——识别高度风格化、变形或抽象的标识字体，其字符形状不规则；2）真实海报 OCR——处理字体多样、尺度多变、版面密集且背景带纹理的复杂场景，其中文字与图形的相互作用抬高了难度；3）简单 OCR——把 Oxford 3000 词以不同字体与大小写渲染为长度均衡的序列置于白底之上，用以估计性能上界；4）困难 OCR——以乱序字母序列（排除易混淆的“l”/“I”）考察鲁棒性，字母以不同字体渲染、带轻微旋转与随机颜色，并置于取自真实图像的强纹理彩色背景上；5）多字号 OCR——以基础字体在白底上生成 14 种字号的乱序字母序列，并在多种字体上重复，以评估尺度变化下的稳定性。

**EN** Font Understanding Tasks.

**ZH** 字体理解任务。

**EN** Typography is central to poster design: font styles convey both theme and aesthetics, and require accurate perception. We evaluate these capabilities with four sub-tasks: 1) Font Matching—fine-grained style identification without font-name priors; given a target text in one font, the model selects the matching font from nine candidates showing different text, forcing reliance on visual style rather than character identity; 2) Font Attribute Perception—using 37 human-derived attributes from [30]. (31 relative, 6 binary such as serif/italic), the model sees a pair of font-rendered texts and chooses the one best matching a target attribute, with accuracy reflecting agreement with human judgments; 3) Traditional Font Effect Recognition—recognition of nine common effects (bold, italic, underline, etc.) by selecting the correct effect from four options; 4) Advanced Font Effect Recognition—on highly stylized, model-generated and curated effects, the model first identifies the text’s dominant color, then selects the correct effect from 48 candidates spanning styles such as rock.

**ZH** 字体排印是海报设计的核心：字体风格同时传达主题与美感，因而需要被准确感知。我们用四个子任务评测这些能力：1）字体匹配——在没有字体名称先验的条件下做细粒度风格辨识；给定以一种字体渲染的目标文本，模型须从展示不同文本的九个候选字体中选出匹配者，迫使模型依赖视觉风格而非字符本身；2）字体属性感知——使用源自 [30] 的 37 个人工归纳属性（31 个相对属性、6 个二值属性，如衬线、斜体），模型观看一对字体渲染文本，并选出与目标属性最匹配的一个，准确率反映其与人类判断的一致程度；3）传统字体效果识别——识别九种常见效果（粗体、斜体、下划线等），从四个选项中选出正确效果；4）高级字体效果识别——针对高度风格化、由模型生成或人工筛选的效果，模型先识别文本的主色，再从涵盖摇滚等风格的 48 个候选中选出正确效果。

**EN** Spatial Reasoning Tasks. Effective perception and generation of layout structures are vital for poster design, reflecting an MLLM’s grasp of aesthetics, spatial balance, and composition. We evaluate layout understanding, aesthetic judgment, and spatial planning with five sub-tasks: 1) Text Localization—given a list of target phrases, the model returns a bounding box for each; coordinates are normalized to [0,1] to handle varying resolutions and aspect ratios, emphasizing precise detection of small or dense text; 2) Text Alignment and Rotation—the model infers alignment and rotation for each text sample, capturing typographic structure beyond position; 3) Empty-Space Perception—using partially completed posters divided into a ⟦SLOT_0⟧ grid, annotators label suitable regions for new elements; their intersection defines the consensus empty space, and the model outputs region IDs for a requested count, evaluated by IoU with the consensus set; 4) Layout Comparison—given a professional layout and a version deliberately violating design principles, the model selects the more coherent and aesthetically sound design, testing high-level layout judgment; 5) Layout Generation—given a textual specification of relative sizes and placements (⟦SLOT_1⟧ elements), the model produces bounding boxes forming a coherent layout, evaluated on positional and area accuracy, thereby assessing instruction following and multimodal reasoning.

**ZH** 空间推理任务。对版式结构的有效感知与生成对海报设计至关重要，体现了 MLLM 对美学、空间平衡与构图的把握。我们用五个子任务评测版面理解、美学判断与空间规划：1）文字定位——给定目标短语列表，模型为每个短语返回一个边界框；坐标归一化到 [0,1] 以适应不同的分辨率与宽高比，重点考察对细小或密集文字的精确检测；2）文字对齐与旋转——模型推断每个文字样本的对齐方式与旋转角度，捕捉位置之外的字体排印结构；3）留白感知——使用被划分为 ⟦SLOT_0⟧ 网格的部分完成海报，标注员标出适合放置新元素的区域，其交集定义为共识留白，模型按请求数量输出区域编号，以与共识集合的 IoU 评价；4）版面比较——给定专业版面与刻意违反设计原则的版本，模型须选出更连贯、更美观的设计，考察高层版面判断力；5）版面生成——给定描述相对尺寸与位置的文字说明（⟦SLOT_1⟧ 个元素），模型生成构成连贯版面的边界框，按位置与面积准确率评价，从而考察指令遵循与多模态推理能力。

**EN** Advanced Visual Design Understanding. High-quality poster design goes beyond basic layout and elements, often employing sophisticated styles, visual deconstruction, and conceptual metaphors. We evaluate advanced design understanding with three sub-tasks: 1) Poster Style Classification—identify one of 17 curated styles (e.g., Minimalist, Diffuse Glow, Memphis) based on holistic cues spanning color, effects, typography, and imagery; 2) Composition Structure Understanding—describe each poster’s visual construction using operations such as misalignment, segmentation, nesting, cutouts, repetition, extension, focus shifting, and mirroring, with coverage judged by an LLM against human-annotated key concepts; 3) Intention and Metaphor Interpretation—explain metaphor-rich posters (e.g., stacked smartphones evoking a hamburger, toy soldiers forming a dove, circuit-board textures fused with leaf veins), with success measured by capturing manually annotated explanatory elements and intended messages.

**ZH** 高级视觉设计理解。高质量海报设计不止于基础版式与元素，往往运用精妙的风格、视觉解构与概念隐喻。我们用三个子任务评测高级设计理解：1）海报风格分类——依据覆盖色彩、效果、字体排印与图像的整体线索，从 17 种精选风格（如极简、弥散发光、孟菲斯）中识别其一；2）构图结构理解——用错位、分割、嵌套、抠图、重复、延展、焦点转移、镜像等操作描述每张海报的视觉构造，覆盖率由大语言模型对照人工标注的关键概念判定；3）意图与隐喻解读——解释富含隐喻的海报（例如堆叠的智能手机唤起汉堡意象、玩具士兵组成鸽子、电路板纹理与叶脉融合），成功与否取决于是否捕捉到人工标注的解释性元素与预期信息。

**EN** Rating Task. Finally, we further assess aesthetic judgment by asking models to assign each poster a quality score from 0 to 10. After normalizing scores, we measure alignment with human preferences by computing the correlation between model predictions and human rating distributions.

**ZH** 评分任务。最后，我们进一步考察美学判断，要求模型为每张海报打出 0 到 10 的质量分。分数归一化后，通过计算模型预测与人类评分分布之间的相关性来衡量其与人类偏好的一致程度。

**EN** 3.2 Generation Tasks

**ZH** 3.2 生成任务

**EN** Dense Generation. Real-world themes (e.g., film IP) demand many characters, objects, and fine details in one image. We curate themes with 10 entities and specify actions, attributes, or orientations for each; given a prompt, the model must render all required elements. An MLLM verifies each item and reports overall matching accuracy.

**ZH** 密集生成。真实世界的主题（如影视 IP）要求单张图像容纳众多人物、物体与精细细节。我们筛选含 10 个实体的主题，并为每个实体指定动作、属性或朝向；给定提示词，模型须渲染出全部必需元素。由 MLLM 逐项核验并给出整体匹配准确率。

**EN** Font Generation. To assess control over typography, we ask for text-centric posters across varied scenarios while explicitly encouraging font diversity. An MLLM infers latent font attributes (e.g., bold, elegant, friendly), and the count of distinct attributes measures font-style diversity.

**ZH** 字体生成。为考察对字体排印的掌控力，我们要求模型在多种场景下生成以文字为主体的海报，并明确鼓励字体多样化。由 MLLM 推断潜藏的字体属性（如粗壮、优雅、亲和），以不同属性的数量度量字体风格的丰富度。

**EN** Style Generation. The model generates posters in 17 mainstream styles (matching our style-understanding benchmark, e.g., Memphis). An MLLM predicts each poster’s style, and accuracy is computed against the target.

**ZH** 风格生成。模型需生成 17 种主流风格的海报（与我们的风格理解基准一致，如孟菲斯）。由 MLLM 预测每张海报的风格，并与目标风格比对计算准确率。

**EN** Composition Generation. Advanced design often employs structured compositional techniques—such as misalignment, segmentation, nesting, cutouts, repetition, extension, focus shifting, and mirroring—to create visual tension and sophistication. We provide prompts describing these composition strategies and require the model to generate images accordingly. An MLLM evaluates whether each compositional element appears in the output, using the same criteria as in the composition-understanding task, and computes matching rate across all required points.

**ZH** 构图生成。高级设计常采用结构化的构成手法——如错位、分割、嵌套、抠图、重复、延展、焦点转移与镜像——以制造视觉张力与精致感。我们提供描述这些构图策略的提示词，要求模型据此生成图像。由 MLLM 依据与构图理解任务相同的标准评判每个构成元素是否在输出中出现，并对全部要求要点计算匹配率。

**EN** Intention Generation. We prompt metaphor- and concept-rich posters (e.g., dual-meaning imagery or abstract symbols). An MLLM evaluates whether key intention elements—essential visual cues and intended semantics, as defined by human annotations—are present, reusing the labels from the understanding task.

**ZH** 意图生成。我们以富含隐喻与概念的海报作为提示（如双关意象或抽象符号）。由 MLLM 评判关键意图元素——即人工标注所定义的核心视觉线索与预期语义——是否呈现，标签沿用理解任务中的标注。

**EN** 4 Experiment

**ZH** 4 实验

**EN** Table 1: Comprehensive OCR benchmark results across multiple visual text recognition tasks. ⟦SLOT_2⟧ denotes the accuracy, and ⟦SLOT_3⟧ denotes the word-level recall rate. ⟦SLOT_4⟧ represents the performance gap between the simple and hard OCR settings, reflecting model robustness. ⟦SLOT_5⟧ denotes the standard deviation of ⟦SLOT_6⟧ across different font sizes, indicating stability.

**ZH** 表 1：跨多个视觉文字识别任务的综合 OCR 基准结果。⟦SLOT_2⟧ 表示准确率，⟦SLOT_3⟧ 表示词级召回率。⟦SLOT_4⟧ 表示简单与困难 OCR 设置之间的性能差距，反映模型鲁棒性。⟦SLOT_5⟧ 表示 ⟦SLOT_6⟧ 在不同字号下的标准差，反映稳定性。

<!-- [原子块 · table] Logo OCR Poster OCR Simple OCR hard OCR Δ \Delta Font Size OCR Model A ​ C AC ↑ \uparrow A ​ C AC ↑ \uparrow W ​ R WR ↑ \uparrow W ​ R WR ↑ \uparrow δ \delta ↓ \downarrow W ​ R WR ↑ \uparrow S ​ t ​ d -->

**EN** Data. PosterIQ consists of 7,765 annotated instances for understanding and 822 prompts for generation, spanning 24 task types in total. The understanding part covers five OCR tasks (3,005 items: logo, poster, simple, hard, and font-size OCR), four font perception tasks (2,788 items: font matching, font attributes, and two levels of font effects), six spatial reasoning tasks (1,178 items: text localization, rotation, alignment, empty-space perception, layout comparison, and layout generation), three advanced visual design tasks (575 items: style, composition, and intention understanding), and an overall rating task (219 items). The generation part includes five task families with 822 prompts: dense content generation (114), font generation (135), style generation (256), composition generation (117), and intention generation (200), jointly supporting a comprehensive evaluation of both poster understanding and generation.

**ZH** 数据。PosterIQ 由 7,765 个用于理解的标注实例与 822 条用于生成的提示词组成，共覆盖 24 种任务类型。理解部分包括五类 OCR 任务（3,005 项：Logo、海报、简单、困难与字号 OCR），四类字体感知任务（2,788 项：字体匹配、字体属性与两级字体效果），六类空间推理任务（1,178 项：文字定位、旋转、对齐、留白感知、版面比较与版面生成），三类高级视觉设计任务（575 项：风格、构图与意图理解），以及整体评分任务（219 项）。生成部分包含五个任务族共 822 条提示词：密集内容生成（114）、字体生成（135）、风格生成（256）、构图生成（117）与意图生成（200），共同支撑对海报理解与生成的全面评测。

**EN** Metric. We use task-specific metrics to capture both accuracy and robustness. For Logo OCR and Poster OCR, we report item-level accuracy. For Simple, Hard, and Font-Size OCR, we use a word-level recall rate (WR) over fixed-length segments, together with the standard deviation (Std) across font sizes and the gap ⟦SLOT_7⟧ between simple and hard settings. For the font tasks, we adopt a normalized multiple-choice score (Score) in ⟦SLOT_8⟧: values near 0 indicate near-random predictions, and 1 indicates all answers are correct. For layout tasks, we use IoU-based metrics and discrete-choice accuracy. Top-1 IoU denotes the maximum IoU over predicted regions, while Alignment and Rotation are evaluated by multiple-choice accuracy. In the Empty Space task, Matching Acc. measures whether the returned region IDs match the requested count and target regions. For Layout Generation, we measure the center offset and area ratio between predicted and ground-truth boxes. For Advanced Visual Design Understanding, Score is again a multiple-choice accuracy, and Points Score measures the coverage of annotated key points in the model’s description. In the overall rating task, we compute the cosine similarity between the vector of model scores and the vector of human ratings. Generation experiments are evaluated with analogous metrics (e.g., option correctness, style agreement, and key-point coverage); find full metric definitions in the supplementary material.

**ZH** 指标。我们采用面向具体任务的指标，同时刻画准确率与鲁棒性。对 Logo OCR 与海报 OCR，报告实例级准确率。对简单、困难与字号 OCR，采用固定长度片段上的词级召回率（WR），以及跨字号的标准差（Std）与简单、困难设置之间的差距 ⟦SLOT_7⟧。对字体类任务，采用归一化到 ⟦SLOT_8⟧ 的多选得分（Score）：取值接近 0 表示接近随机猜测，1 表示全部答对。对版式任务，采用基于 IoU 的指标与离散选择准确率。Top-1 IoU 表示预测区域上的最大 IoU，对齐与旋转则以多选准确率评价。在留白任务中，匹配准确率（Matching Acc.）度量返回的区域编号是否与请求数量及目标区域相符。对版面生成，我们度量预测框与真值框之间的中心偏移与面积比。对高级视觉设计理解，Score 同样为多选准确率，要点得分（Points Score）度量模型描述对标注关键点的覆盖程度。在整体评分任务中，我们计算模型分数向量与人类评分向量之间的余弦相似度。生成实验采用类似的指标（如选项正确性、风格一致性与关键点覆盖）；完整指标定义见补充材料。

**EN** 4.1 Understanding Task

**ZH** 4.1 理解任务

**EN** OCR Tasks. As shown in Tab. 1, all models, except Grok-4-fast, achieve accuracy close to 0.9 on both Logo OCR and Poster OCR, indicating that most MLLMs can reliably handle standard text recognition in design-oriented imagery. In the synthetic setting, the gap between the simple and hard OCR reveals notable differences in robustness: Claude-Sonnet-4.5 and the Qwen family exhibit the most stable performance under heavy visual interference. Meanwhile, Claude-Sonnet-4.5[2], Gemini-2.5-Pro[5], and MiniCPM-V-4.5[41] show minimal performance degradation across scales, suggesting stronger invariance to font-size variation.

**ZH** OCR 任务。如表 1 所示，除 Grok-4-fast 外，所有模型在 Logo OCR 与海报 OCR 上的准确率都接近 0.9，说明多数 MLLM 已能可靠处理设计类图像中的常规文字识别。在合成设置中，简单与困难 OCR 之间的差距揭示了鲁棒性上的显著差异：Claude-Sonnet-4.5 与 Qwen 系列在强视觉干扰下表现最为稳定。同时，Claude-Sonnet-4.5[2]、Gemini-2.5-Pro[5] 与 MiniCPM-V-4.5[41] 在不同尺度上的性能衰减最小，说明它们对字号变化具有更强的不变性。

**EN** Table 2: Comparison of Font tasks across models.

**ZH** 表 2：各模型在字体类任务上的对比。

<!-- [原子块 · table] Font Matching Font Attributes Font Effect 1 Font Effect 2 Model Score ↑ \uparrow Score ↑ \uparrow Effect Score ↑ \uparrow Color Score ↑ \uparrow Effect Score ↑ \uparrow Closed GPT-5 0.668 0.664 0.805  -->

**EN** Table 3: Results of Understanding.

**ZH** 表 3：理解任务结果。

<!-- [原子块 · table] Style Understanding Composition Understanding Intention Understanding Model Score ↑ \uparrow Points Score ↑ \uparrow Points Score ↑ \uparrow Closed GPT-5 0.851 0.730 0.824 Claude-Sonnet-4.5 0.813 0.60 -->

**EN** Font Understanding Benchmark Analysis. Across the four font-related tasks, we observe large capability gaps among current MLLMs from Tab. 3. In the font matching task, only GPT-5, Claude-Sonnet-4.5, and Gemini-2.5-Pro demonstrate meaningful discrimination of typographic styles, while most other models perform at a near-chance level. For perceptual font attributes, Gemini-2.5-Pro aligns most closely with human judgments, followed by GPT-5. In recognizing traditional and advanced font effects—including style-specific color cues—Gemini-2.5-Pro consistently achieves the strongest overall performance.

**ZH** 字体理解基准分析。由表 3 可见，在四类字体相关任务上，现有 MLLM 之间存在巨大的能力差距。在字体匹配任务中，只有 GPT-5、Claude-Sonnet-4.5 与 Gemini-2.5-Pro 表现出对字体排印风格的有效区分能力，其余多数模型仅处于接近随机的水平。在感知性字体属性上，Gemini-2.5-Pro 与人类判断最为接近，GPT-5 次之。在传统与高级字体效果（含特定风格的颜色线索）的识别上，Gemini-2.5-Pro 的整体表现始终最强。

**EN** Advanced Visual Design Understanding. On the style understanding task in Tab. 3, GPT-5, Claude-Sonnet-4.5, Gemini-2.5-Pro, and Qwen3-VL-4B correctly identify over 80% of poster styles, indicating that current MLLMs can reliably capture global stylistic cues. For more complex tasks, Gemini-2.5-Pro achieves the best performance on visual composition understanding (0.802), while GPT-5 performs best on intention understanding (0.824). These suggest that proprietary models currently exhibit stronger design literacy than open-source counterparts, especially when higher-level composition and conceptual intent are involved.

**ZH** 高级视觉设计理解。在表 3 的风格理解任务上，GPT-5、Claude-Sonnet-4.5、Gemini-2.5-Pro 与 Qwen3-VL-4B 对海报风格的识别正确率超过 80%，说明现有 MLLM 已能可靠捕捉全局风格线索。在更复杂的任务上，Gemini-2.5-Pro 在视觉构图理解上表现最佳（0.802），GPT-5 在意图理解上表现最佳（0.824）。这表明闭源模型当前比开源模型具备更强的设计素养，在涉及更高层构图与概念意图时尤为明显。

**EN** Table 4: Comparison of layout reasoning tasks across models.

**ZH** 表 4：各模型在版面推理任务上的对比。

<!-- [原子块 · table] Text Localization Text Positioning Empty-Space Layout Comparison Layout Generation Model Top-1 IoU ↑ \uparrow Top-3 IoU ↑ \uparrow Mean IoU ↑ \uparrow Recall ↑ \uparrow Alignment ↑ \uparrow Rotation ↑ -->

**EN** Layout Tasks. Our layout benchmark primarily tests spatial recognition and layout intuition (Tab. 4). On the Text Localization, Qwen3-VL-8B achieves the best performance among open-source models, with a mean IoU of 0.45, followed by the Closed Gemini-2.5-Pro (0.295), as also illustrated in Fig. 2. For Text Position (alignment), Closed models generally outperform open-source ones, and Gemini-2.5-Pro further leads on Text Rotation recognition. In the Empty Space task, which requires spatial reasoning over potential placement regions, Gemini-2.5-Pro again shows superior performance. For Layout Comparison, GPT-5, Claude-Sonnet-4.5, and Gemini-2.5-Pro consistently outperform other models. Finally, Layout Generation requires joint reasoning over visual context and textual instructions; here, Closed models overall outperform open-source counterparts, with Gemini-2.5-Pro achieving best results.

**ZH** 版式任务。我们的版面基准主要考察空间识别与版面直觉（表 4）。在文字定位上，Qwen3-VL-8B 在开源模型中表现最好，平均 IoU 为 0.45，其次是闭源模型 Gemini-2.5-Pro（0.295），如图 2 所示。在文字位置（对齐）上，闭源模型整体优于开源模型，而 Gemini-2.5-Pro 在文字旋转识别上进一步领先。在需要对潜在放置区域做空间推理的留白任务中，Gemini-2.5-Pro 同样表现最优。在版面比较上，GPT-5、Claude-Sonnet-4.5 与 Gemini-2.5-Pro 持续优于其他模型。最后，版面生成需要同时对视觉上下文与文字指令做联合推理；在此任务上闭源模型整体优于开源模型，其中 Gemini-2.5-Pro 结果最佳。

**EN** Table 5: Comparison of Overall Rating

**ZH** 表 5：整体评分对比

<!-- [原子块 · table] Overall Rating Model Sim ↑ \uparrow Closed GPT-5 0.347 Claude-Sonnet-4.5 0.384 Gemini-2.5-Pro 0.399 Grok-4-fast 0.465 Open MiniCPM-V 4.5 0.095 Gemma 3N-E4B-IT 0.483 Qwen3-VL-4B 0.172 Qwen3-VL-8B 0.237 -->

**EN** Overall Rating. Asking MLLMs to assign a single holistic quality score to posters is a challenging task. Although most models can produce reasonable scores, Tab. 5 shows that their predicted ratings exhibit relatively low correlation with human judgments. This gap highlights the importance of our decoupled evaluation setting, where fine-grained understanding and design dimensions are assessed separately rather than relying solely on a global score.

**ZH** 整体评分。要求 MLLM 为海报给出一个整体质量分是一项具有挑战性的任务。尽管多数模型能给出合理的分数，表 5 显示其预测评分与人类判断的相关性偏低。这一差距凸显了我们解耦式评测设置的价值：细粒度的理解与设计维度被分别评估，而非仅依赖一个全局分数。

<!-- [原子块 · img]  -->

**EN** Figure 2: Qualitative comparison of four models on three layout-related tasks. For Text Localization and Layout Generation, the predicted bounding boxes are shown in red. For the Empty Space task, the selected patch IDs are highlighted in the image.

**ZH** 图 2：四个模型在三类版面相关任务上的定性对比。对于文字定位与版面生成，预测的边界框以红色标出。对于留白任务，被选中的图块编号在图中高亮显示。

**EN** 4.2 Generation Task

**ZH** 4.2 生成任务

**EN** We evaluate four models (Seedream-4.0[35], Gemini-2.5-Flash-Image[8], GPT-Image-1[29], Qwen-Image[39]) on five generation tasks: Dense Generation, Font Generation, Style Generation, Composition Generation, and Intention Generation.

**ZH** 我们在五个生成任务上评测四个模型（Seedream-4.0[35]、Gemini-2.5-Flash-Image[8]、GPT-Image-1[29]、Qwen-Image[39]）：密集生成、字体生成、风格生成、构图生成与意图生成。

**EN** Quantitative Results. Averaged across five tasks, Gemini-2.5-Flash-Image leads overall. Per-task results show differentiated strengths: Gemini excels in Composition and Intention, indicating strong global layout planning and instruction–semantics alignment, while GPT-Image-1 leads in Style and Intention but trails on Dense and Font, revealing weaknesses in micro-structure fidelity and text readability. Structural patterns emerge: Font and Dense are partially decoupled (e.g., Seedream-4.0 is strong on Dense but middling on Font), implying distinct capability axes and a need for targeted supervision on stroke closure, spacing, ligatures, and variant-shape modeling. A global–local trade-off is evident—models dominating Composition and Intention generally do not lead on Style and Font—suggesting training favors global planning over local precision. Font remains the bottleneck, with uniformly low scores (best 0.391) versus high Composition (up to 0.866), posing risks for multilingual scripts, small sizes, complex fonts, and low-contrast backgrounds.

**ZH** 定量结果。在五项任务的平均表现上，Gemini-2.5-Flash-Image 整体领先。分任务结果呈现差异化的优势：Gemini 在构图与意图上表现出色，说明其具备较强的全局版面规划与指令—语义对齐能力；GPT-Image-1 在风格与意图上领先，但在密集与字体上落后，暴露出微观结构保真度与文本可读性方面的不足。结构性规律随之显现：字体与密集在一定程度上相互解耦（例如 Seedream-4.0 在密集上强势而在字体上居中），意味着二者属于不同的能力轴，需要针对笔画闭合、字距、连字与变体字形建模施加专门的监督。全局—局部的权衡同样明显——主导构图与意图的模型通常不在风格与字体上领先，说明训练更偏重全局规划而非局部精度。字体仍是瓶颈，得分普遍偏低（最佳 0.391），而构图得分可高达 0.866，这给多语言字符、小字号、复杂字体与低对比度背景带来了风险。

**EN** Table 6: Performance of image generation models across five evaluation tasks. Point Score(⟦SLOT_9⟧), Score(⟦SLOT_10⟧), Richness(⟦SLOT_11⟧)

**ZH** 表 6：图像生成模型在五项评测任务上的表现。要点得分（⟦SLOT_9⟧）、得分（⟦SLOT_10⟧）、丰富度（⟦SLOT_11⟧）

<!-- [原子块 · table] Dense Font Style Composition Intention Model P ​ S PS ↑ \uparrow R R ↑ \uparrow S S ↑ \uparrow P ​ S PS ↑ \uparrow P ​ S PS ↑ \uparrow Average ↑ \uparrow Seedream-4.0 0.618 0.342 0.591 0.848 0.645 0.6 -->

**EN** Qualitative Results. The Dense Generation task targets crowded scenes with many subjects, rich local detail, and strong interactions, emphasizing facial fidelity, hands, textures, and clean edges (Fig. 3, cols. 1–2). Gemini-2.5-Flash-Image delivers the most stable faces and skin; GPT-Image-1 is close behind; Qwen-Image often over-brightens, yielding unnatural texture; Seedream-4.0 is weakest, with frequent collapses and distortions. In cartoons, Gemini-2.5-Flash-Image preserves crisp edges and stylistic consistency; GPT-Image-1 drifts under complexity. For Font Generation (Fig. 3, cols. 3–4), Seedream-4.0 explores the boldest styles; Gemini-2.5-Flash-Image also varies fonts; GPT-Image-1 and Qwen-Image prefer conservative, upright forms. Seedream-4.0 has the lowest text sharpness and breaks strokes under layered effects. In Style Generation, all models broadly match targets, but dispersion style (Fig. 3, col. 5) remains difficult; Qwen-Image stays overly sharp and saturated, and often misses vintage tone; Gemini-2.5-Flash-Image and GPT-Image-1 skew more vintage, with GPT-Image-1 leaning comic and toward colored backgrounds; Seedream-4.0 tends toward naturalistic renderings with moderate completeness; Gemini-2.5-Flash-Image shows a Western bias. Compared with ground-truth designs (Fig. 3, col. 6), all converge to safe, low-creativity styles. In Composition Task, Gemini-2.5-Flash-Image shows stronger grasp of nested structures, yet advanced layouts—intentional misalignment, whitespace, figure–ground play, cutouts—generally fail (Fig. 3, col. 7); fusion/collage exhibits seams and fragmentation; complex spatial relations with whitespace lead to poor saliency and attention allocation. Results in Intention Task reveal that existing models manage surface associations but rarely convey deeper concepts. All in all, end-to-end image synthesis remains insufficient for highly constrained poster design; a full pipeline—understand ⟦SLOT_12⟧ ideate ⟦SLOT_13⟧ compose ⟦SLOT_14⟧ generate—is needed to meet high-level design constraints.

**ZH** 定性结果。密集生成任务针对主体众多、局部细节丰富且交互强烈的拥挤场景，重点考察人脸保真度、手部、纹理与干净的边缘（图 3，第 1–2 列）。Gemini-2.5-Flash-Image 生成的人脸与肤色最为稳定；GPT-Image-1 紧随其后；Qwen-Image 常过度提亮，导致纹理失真；Seedream-4.0 最弱，频繁出现结构崩坏与变形。在卡通场景中，Gemini-2.5-Flash-Image 保持了锐利的边缘与风格一致性；GPT-Image-1 在复杂度上升时出现偏移。在字体生成（图 3，第 3–4 列）中，Seedream-4.0 探索的风格最为大胆；Gemini-2.5-Flash-Image 同样会变换字体；GPT-Image-1 与 Qwen-Image 则偏好保守、端正的字体。Seedream-4.0 的文字锐度最低，在叠加效果下还会出现断笔。在风格生成中，所有模型大体都能匹配目标，但弥散风格（图 3，第 5 列）依然困难；Qwen-Image 始终保持过锐、过饱和，且常常缺失复古色调；Gemini-2.5-Flash-Image 与 GPT-Image-1 更偏向复古，其中 GPT-Image-1 倾向漫画感与彩色背景；Seedream-4.0 倾向自然主义渲染，完整度适中；Gemini-2.5-Flash-Image 显示出西方偏好。与真值设计（图 3，第 6 列）相比，所有模型都收敛到安全、低创造力的风格。在构图任务上，Gemini-2.5-Flash-Image 对嵌套结构的把握更强，但刻意错位、留白、图形—背景游戏、抠图等高级版式普遍失败（图 3，第 7 列）；融合与拼贴会出现接缝与碎裂；涉及留白的复杂空间关系导致显著性与注意力分配不佳。意图任务的结果显示，现有模型能处理表层联想，却很少传达更深层的概念。总而言之，端到端图像合成对强约束的海报设计仍显不足；需要“理解 ⟦SLOT_12⟧ 构思 ⟦SLOT_13⟧ 构图 ⟦SLOT_14⟧ 生成”的完整流程，才能满足高层设计约束。

<!-- [原子块 · img]  -->

**EN** Figure 3: Qualitative comparison of four models on five generation tasks.

**ZH** 图 3：四个模型在五项生成任务上的定性对比。

**EN** Understanding and Generation. We investigate how improved understanding benefits generation and validate the soundness of our benchmark. To this end, we design an iterative setup where a VLM supervises a T2I generator. We simulate a realistic use case: the input is a vague, brief requirement as the prompt. A T2I model first produces a poster. We then feed the generated poster and the original prompt into a VLM. Based on its interpretation of the poster, the VLM diagnoses issues and returns a revised prompt, which is fed back to the generator for re-generation. Notably, the VLM only receives the image and the original prompt; the enhanced prompt without any human or domain-specific design hints. By iterating this loop, we directly observe how understanding affects poster quality. As shown in Fig. 4, the two T2I models are GPT-Image-1 and Qwen-Image, and the two VLMs are GPT-5 and Qwen3-VL. From the first T2I outputs under ambiguous requirements, both models capture the main content, but GPT-Image exhibits stronger intent understanding than Qwen-Image. It conveys a cautionary message to young people about excessive play, whereas Qwen-Image attends to surface keywords such as “Halloween” and “children,” without deeper inference. After the first round of VLM-guided analysis, the VLM flags issues in visual style, mood, and typography. The regenerated results from the revised prompt address these issues and improve overall poster quality. A second iteration yields further gains, confirming that stronger understanding improves generation. At round 0 (no understanding intervention), the models tend to produce visually appealing images that neglect efficient communication. After VLM intervention, the system begins to prioritize effective information transmission. The clearest evidence is the adjustment of emotional tone to match communication goals. Without intervention, round-0 results often include elements unsuitable for the audience, such as frightening skulls or uncanny faces. With deeper understanding, these issues are corrected. These findings suggest a practical paradigm for poster generation: iteratively coupling understanding and generation—without human design hints.

**ZH** 理解与生成。我们考察理解的提升如何惠及生成，并以此验证基准的合理性。为此设计了一个迭代设置，由视觉语言模型监督文生图生成器。我们模拟一个真实用例：输入是一条模糊而简短的需求，用作提示词。文生图模型先产出一张海报，随后把该海报与原始提示词一起输入视觉语言模型。视觉语言模型基于对海报的解读诊断问题并返回修订后的提示词，再反馈给生成器重新生成。值得注意的是，视觉语言模型只接收图像与原始提示词；增强后的提示词不含任何人工或领域专用的设计提示。通过迭代这一循环，我们直接观察理解如何影响海报质量。如图 4 所示，两个文生图模型为 GPT-Image-1 与 Qwen-Image，两个视觉语言模型为 GPT-5 与 Qwen3-VL。从模糊需求下的首轮文生图输出看，两个模型都捕捉到了主要内容，但 GPT-Image 表现出比 Qwen-Image 更强的意图理解：它向年轻人传达了关于过度玩乐的警示信息，而 Qwen-Image 只关注“Halloween”“children”等表层关键词，未做更深推断。在第一轮视觉语言模型引导的分析之后，视觉语言模型指出了视觉风格、氛围与字体排印方面的问题。依修订提示词重新生成的结果解决了这些问题，海报整体质量得到提升。第二轮迭代带来进一步增益，证实了更强的理解能改善生成。在第 0 轮（无理解干预）时，模型倾向于生成视觉上讨喜却忽视高效传达的图像。经视觉语言模型干预后，系统开始优先保证信息的有效传递。最明显的证据是情感基调被调整以匹配传达目标：未经干预时，第 0 轮结果常包含不适合受众的元素，如骇人的骷髅或怪异的面孔；随着理解加深，这些问题得到纠正。这些发现提示了一种实用的海报生成范式：在无需人工设计提示的条件下迭代地耦合理解与生成。

<!-- [原子块 · img]  -->

**EN** Figure 4: Qualitative comparison of model outputs over supervision-guided iterations.

**ZH** 图 4：监督引导下多轮迭代的模型输出定性对比。

**EN** Table 7: Average scores across understanding tasks. The average is computed by aggregating only these positively correlated scores.

**ZH** 表 7：各理解任务的平均分。该平均分仅对呈正相关的分数进行聚合后计算。

<!-- [原子块 · table] Model OCR Font Layout Understanding Overall Rating Average GPT-5 0.838 0.615 0.511 0.801 0.347 0.622 Claude-Sonnet-4.5 0.838 0.603 0.453 0.727 0.384 0.601 Gemini-2.5-Pro 0.855 0.606 0.571 0.806 0.399  -->

**EN** Overall Evaluation. Finally, we aggregate model performance into an overall score. For each understanding tasks, we first average all positively oriented metrics to obtain group-wise scores for OCR, Font, Layout, Understanding, and Overall Rating. We then take the mean of these five group scores to derive the final score for each model, as reported in Tab. 7. The three proprietary models GPT-5, Claude-Sonnet-4.5, and Gemini-2.5-Pro exhibit stronger poster understanding capabilities than the open-source models. Combined with the generation results in Tab. 6, this suggests that Gemini-2.5 achieves a consistently strong balance between understanding and generation.

**ZH** 总体评测。最后，我们把模型的表现汇总为一个总分。对每项理解任务，先对全部正向指标取平均，得到 OCR、字体、版式、理解与整体评分的分组得分；再对这五个分组得分取均值，得到每个模型的最终分数，如表 7 所示。GPT-5、Claude-Sonnet-4.5 与 Gemini-2.5-Pro 三个闭源模型展现出比开源模型更强的海报理解能力。结合表 6 的生成结果可见，Gemini-2.5 在理解与生成之间取得了持续而均衡的强劲表现。

**EN** 5 Conclusion

**ZH** 5 结论

**EN** PosterIQ delivers a rigorous benchmark for poster design. By decoupling core capabilities, our tasks expose where current MLLMs and generators succeed and where they fail, from saliency control to intention communication. Empirical studies reveal that frontier models excel at high-level reasoning yet remain insensitive as automatic raters and struggle with composition-aware synthesis and typographic diversity. We hope this work catalyzes multimodal intelligence and guides future models toward fidelity to design constraints, communicative intent, and creativity in real-world poster scenes.

**ZH** PosterIQ 为海报设计提供了一个严谨的基准。通过解耦核心能力，我们的任务揭示了当前 MLLM 与生成器在何处成功、何处失败，范围从显著性控制到意图传达。实证研究表明，前沿模型擅长高层推理，但作为自动评分器仍缺乏敏感度，且在构图感知的合成与字体排印多样性上表现不佳。我们希望这项工作能推动多模态智能的发展，并引导未来模型在真实海报场景中忠实于设计约束、传达意图与创造力。

**EN** Acknowledgement

**ZH** 致谢

**EN** The work described in this paper was substantially supported by a grant from the Research Grants Council of the Hong Kong Special Administrative Region, China (Project No. PolyU/RGC Project 25211424) and partially supported by a grant from PolyU University Start-Up Fund (Project No. P0047675).

**ZH** 本论文所述工作主要由香港特别行政区研究资助委员会的资助支持（项目编号 PolyU/RGC Project 25211424），并得到香港理工大学启动基金的部分资助（项目编号 P0047675）。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] [1] S. AI (2024) Stable diffusion 3: research paper . Cited by: §2.2 . -->

<!-- [原子块 · verbatim] [2] Anthropic (2025) Claude sonnet 4.5 . Note: Anthropic Claude Sonnet 4.5 model. Accessed: 2025-11-14 Cited by: §1 , §4.1 . -->

<!-- [原子块 · verbatim] [3] M. Chen, J. Tworek, H. Jun, Q. Yuan, H. P. D. O. Pinto, J. Kaplan, H. Edwards, Y. Burda, N. Joseph, G. Brockman, et al. (2021) Evaluating large language models trained on code . arXiv preprint arX -->

<!-- [原子块 · verbatim] [4] S. Chen, J. Lai, J. Gao, T. Ye, H. Chen, H. Shi, S. Shao, Y. Lin, S. Fei, Z. Xing, Y. Jin, J. Luo, X. Wei, and L. Zhu (2025) PosterCraft: rethinking high-quality aesthetic poster generation in a u -->

<!-- [原子块 · verbatim] [5] G. Comanici, E. Bieber, M. Schaekermann, I. Pasupat, N. Sachdeva, I. Dhillon, M. Blistein, O. Ram, D. Zhang, E. Rosen, et al. (2025) Gemini 2.5: pushing the frontier with advanced reasoning, multi -->

<!-- [原子块 · verbatim] [6] N. Du, Z. Chen, S. Gao, Z. Chen, X. Chen, Z. Jiang, J. Yang, and Y. Tai (2025) Textcrafter: accurately rendering multiple texts in complex visual scenes . arXiv preprint arXiv:2503.23461 . Cited b -->

<!-- [原子块 · verbatim] [7] X. Fang, Z. Chen, K. Lan, S. Ding, Y. Liang, X. Zhao, F. Wen, Z. Zhang, G. Zhang, H. Duan, et al. (2025) Creation-mmbench: assessing context-aware creative intelligence in mllm . arXiv preprint ar -->

<!-- [原子块 · verbatim] [8] A. Fortin, G. Vernade, K. Kampf, and A. Reshi (2025) Introducing gemini 2.5 flash image, our state-of-the-art image model . Note: Google Developers Blog, Accessed: 2025-11-14 Cited by: §2.2 , §4.2 -->

<!-- [原子块 · verbatim] [9] L. Fu, B. Yang, Z. Kuang, J. Song, Y. Li, L. Zhu, Q. Luo, X. Wang, H. Lu, M. Huang, et al. (2024) OCRBench v2: an improved benchmark for evaluating large multimodal models on visual text localizat -->

<!-- [原子块 · verbatim] [10] Z. Geng, Y. Wang, Y. Ma, C. Li, Y. Rao, S. Gu, Z. Zhong, Q. Lu, H. Hu, X. Zhang, et al. (2025) X-omni: reinforcement learning makes discrete autoregressive image generative models great again . a -->

<!-- [原子块 · verbatim] [11] D. Ghosh, H. Hajishirzi, and L. Schmidt (2023) Geneval: an object-focused framework for evaluating text-to-image alignment . Advances in Neural Information Processing Systems 36 , pp. 52132–52152 -->

<!-- [原子块 · verbatim] [12] D. Hendrycks, C. Burns, S. Kadavath, A. Arora, S. Basart, E. Tang, D. Song, and J. Steinhardt (2021) Measuring mathematical problem solving with the math dataset . arXiv preprint arXiv:2103.03874 -->

<!-- [原子块 · verbatim] [13] B. Hu and Y. Zhang (2026) How ai and humans express comfort differently: a corpus-based appraisal analysis . Corpus Pragmatics 10 ( 1 ), pp. 16 . Cited by: §2.1 . -->

<!-- [原子块 · verbatim] [14] X. Hu, H. Chen, Z. Qi, H. Zhang, D. Hong, J. Shao, and X. Wu (2025) DreamPoster: a unified framework for image-conditioned generative poster design . arXiv preprint arXiv:2507.04218 . Cited by: § -->

<!-- [原子块 · verbatim] [15] X. Hu, R. Wang, Y. Fang, B. Fu, P. Cheng, and G. Yu (2024) ELLA: equip diffusion models with llm for enhanced semantic alignment . arXiv preprint arXiv:2403.05135 . Cited by: §2.1 . -->

<!-- [原子块 · verbatim] [16] N. Inoue, K. Masui, W. Shimoda, and K. Yamaguchi (2024) OpenCOLE: towards reproducible automatic graphic design generation . In Proceedings of the IEEE/CVF Conference on Computer Vision and Patte -->

<!-- [原子块 · verbatim] [17] N. Jain, K. Han, A. Gu, W. Li, F. Yan, T. Zhang, S. Wang, A. Solar-Lezama, K. Sen, and I. Stoica (2024) Livecodebench: holistic and contamination free evaluation of large language models for code -->

<!-- [原子块 · verbatim] [18] P. Jia, C. Li, Y. Yuan, Z. Liu, Y. Shen, B. Chen, X. Chen, Y. Zheng, D. Chen, J. Li, et al. (2023) COLE: a hierarchical generation framework for multi-layered and editable graphic design . arXiv  -->

<!-- [原子块 · verbatim] [19] B. Jiang, Y. Yuan, X. Bai, Z. Hao, A. Yin, Y. Hu, W. Liao, L. Ungar, and C. J. Taylor (2025) ControlText: unlocking controllable fonts in multilingual text rendering without font annotations . ar -->

<!-- [原子块 · verbatim] [20] B. F. Labs (2024) FLUX . Cited by: §2.2 . -->

<!-- [原子块 · verbatim] [21] B. Li, Y. Ge, Y. Ge, G. Wang, R. Wang, R. Zhang, and Y. Shan (2024) Seed-bench: benchmarking multimodal large language models . In Proceedings of the IEEE/CVF Conference on Computer Vision and Pa -->

<!-- [原子块 · verbatim] [22] J. Lin, D. Huang, T. Zhao, D. Zhan, and C. Lin (2024) Designprobe: a graphic design benchmark for multimodal large language models . arXiv preprint arXiv:2404.14801 . Cited by: §2.1 . -->

<!-- [原子块 · verbatim] [23] Y. Liu, H. Duan, Y. Zhang, B. Li, S. Zhang, W. Zhao, Y. Yuan, J. Wang, C. He, Z. Liu, et al. (2024) Mmbench: is your multi-modal model an all-around player? . In European conference on computer v -->

<!-- [原子块 · verbatim] [24] Y. Liu, Z. Li, M. Huang, B. Yang, W. Yu, C. Li, X. Yin, C. Liu, L. Jin, and X. Bai (2024) OCRBench: on the hidden mystery of ocr in large multimodal models . Science China Information Sciences 67 -->

<!-- [原子块 · verbatim] [25] A. Masry, D. X. Long, J. Q. Tan, S. Joty, and E. Hoque (2022) Chartqa: a benchmark for question answering about charts with visual and logical reasoning . arXiv preprint arXiv:2203.10244 . Cited  -->

<!-- [原子块 · verbatim] [26] M. Mathew, V. Bagal, R. Tito, D. Karatzas, E. Valveny, and C. Jawahar (2022) Infographicvqa . In Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision , pp. 1697–1706 . -->

<!-- [原子块 · verbatim] [27] S. Nayak, X. Jian, K. Q. Lin, J. A. Rodriguez, M. Kalsi, R. Awal, N. Chapados, M. T. Özsu, A. Agrawal, D. Vazquez, et al. (2025) Ui-vision: a desktop-centric gui benchmark for visual perception a -->

<!-- [原子块 · verbatim] [28] OpenAI (2025) GPT-5 . Note: Large multimodal model. Accessed: 2025-11-14 Cited by: §1 . -->

<!-- [原子块 · verbatim] [29] OpenAI (2025) GPT-image-1 . Note: Accessed: 2025-11-14 Cited by: §2.2 , §4.2 . -->

<!-- [原子块 · verbatim] [30] P. O’Donovan, J. Lībeks, A. Agarwala, and A. Hertzmann (2014) Exploratory font selection using crowdsourced attributes . ACM transactions on graphics (TOG) 33 ( 4 ), pp. 1–9 . Cited by: §2.2 , §3 -->

<!-- [原子块 · verbatim] [31] D. Rein, B. L. Hou, A. C. Stickland, J. Petty, R. Y. Pang, J. Dirani, J. Michael, and S. R. Bowman (2024) Gpqa: a graduate-level google-proof q&a benchmark . In First Conference on Language Model -->

<!-- [原子块 · verbatim] [32] K. Ruan, X. Wang, J. Hong, P. Wang, Y. Liu, and H. Sun (2024) LiveIdeaBench: evaluating llms’ scientific creativity and idea generation with minimal context . arXiv preprint arXiv:2412.17596 . Ci -->

<!-- [原子块 · verbatim] [33] W. Shi, Y. Song, D. Zhang, J. Liu, and X. Zou (2024) FonTS: text rendering with typography and style controls . arXiv preprint arXiv:2412.00136 . Cited by: §2.2 . -->

<!-- [原子块 · verbatim] [34] Y. Tatsukawa, I. Shen, A. Qi, Y. Koyama, T. Igarashi, and A. Shamir (2024) FontCLIP: a semantic typography visual-language model for multilingual font applications . Computer Graphics Forum 43 (  -->

<!-- [原子块 · verbatim] [35] Team Seedream (2025) Seedream 4.0: toward next-generation multimodal image generation . arXiv preprint arXiv:2509.20427 . External Links: Link Cited by: §2.2 , §4.2 . -->

<!-- [原子块 · verbatim] [36] Y. Wang, X. Ma, G. Zhang, Y. Ni, A. Chandra, S. Guo, W. Ren, A. Arulraj, X. He, Z. Jiang, et al. (2024) Mmlu-pro: a more robust and challenging multi-task language understanding benchmark . In Th -->

<!-- [原子块 · verbatim] [37] C. Wen, G. Jia, and J. Yang (2023) Dip: dual incongruity perceiving network for sarcasm detection . In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition , pp. 2540 -->

<!-- [原子块 · verbatim] [38] C. Wen, Z. Peng, Y. Huang, X. Yang, and W. Shen (2025) Domain generalization in clip via learning with diverse text prompts . In Proceedings of the IEEE/CVF Conference on Computer Vision and Patt -->

<!-- [原子块 · verbatim] [39] C. Wu, J. Li, J. Zhou, J. Lin, K. Gao, K. Yan, S. Yin, S. Bai, X. Xu, Y. Chen, et al. (2025) Qwen-image technical report . arXiv preprint arXiv:2508.02324 . Cited by: §2.2 , §4.2 . -->

<!-- [原子块 · verbatim] [40] T. Yang, Y. Luo, Z. Qi, Y. Wu, Y. Shan, and C. W. Chen (2024) Posterllava: constructing a unified multi-modal layout generator with llm . arXiv preprint arXiv:2406.02884 . Cited by: §2.2 . -->

<!-- [原子块 · verbatim] [41] T. Yu, Z. Wang, C. Wang, F. Huang, W. Ma, Z. He, T. Cai, W. Chen, Y. Huang, Y. Zhao, et al. (2025) Minicpm-v 4.5: cooking efficient mllms via architecture, data, and training recipe . arXiv prepr -->

<!-- [原子块 · verbatim] [42] J. Zhang, R. Yoshihashi, S. Kitada, A. Osanai, and Y. Nakashima (2024) VASCAR: content-aware layout generation via visual-aware self-correction . arXiv preprint arXiv:2412.04237 . Cited by: §2.2  -->

<!-- [原子块 · verbatim] [43] S. Zhao, Q. Wu, X. Li, B. Zhang, M. Li, Q. Qin, D. Liu, K. Zhang, H. Li, Y. Qiao, et al. (2025) LeX-art: rethinking text generation via scalable high-quality data synthesis . arXiv preprint arXiv -->

<!-- [原子块 · verbatim] [44] B. Zou, M. Cai, J. Zhang, and Y. J. Lee (2024) Vgbench: evaluating large language models on vector graphics understanding and generation . arXiv preprint arXiv:2407.10972 . Cited by: §2.1 . -->

**EN** Supplementary Material

**ZH** 补充材料

**EN** We first present the statistical details of PosterIQ, followed by a description of how we obtain the evaluation results for each task. To validate the automatic evaluation, we also conduct a human evaluation and provide the annotator guideline used to construct the benchmark. Finally, we provide visual examples for each task to aid understanding.

**ZH** 我们先给出 PosterIQ 的统计细节，随后说明各项任务评测结果的获得方式。为验证自动评测的可靠性，我们还开展了人工评测，并提供了构建基准所使用的标注员指南。最后给出每个任务的视觉示例以辅助理解。

**EN** Appendix A Benchmark Statistics

**ZH** 附录 A 基准统计

**EN** Figure 5 summarizes the data distribution of our benchmark. For the understanding part (top), the dataset contains 7,765 items in total, with font-related tasks taking the largest share: Font Attributes (1,813, 23.3%) and Font Size OCR (1,400, 18.0%) together account for over 40% of all instances. OCR and layout–related tasks, including Logo OCR, Poster OCR, Simple/Hard OCR, Text Localization, Layout Comparison, Empty Space, and Layout Generation, form the bulk of the remaining samples, while Style Understanding, Composition Understanding, Intention Understanding, and Overall Rating provide higher-level assessments of visual design and semantics.

**ZH** 图 5 总结了本基准的数据分布。理解部分（上图）共含 7,765 项，其中字体相关任务占比最大：字体属性（1,813，23.3%）与字号 OCR（1,400，18.0%）合计占全部实例的 40% 以上。OCR 与版面相关任务——包括 Logo OCR、海报 OCR、简单与困难 OCR、文字定位、版面比较、留白与版面生成——构成其余样本的主体，而风格理解、构图理解、意图理解与整体评分则提供了对视觉设计与语义的更高层评估。

**EN** For the generation part (bottom), the 822 instances are evenly distributed: Style Generation (256, 31.1%) and Intention Generation (200, 24.3%) dominate the set, whereas Font Generation (135), Composition Generation (117), and Dense Generation (114) each contribute roughly 14–16% of the total, ensuring balanced coverage across different aspects of poster synthesis.

**ZH** 生成部分（下图）的 822 个实例分布较为均衡：风格生成（256，31.1%）与意图生成（200，24.3%）占据主导，字体生成（135）、构图生成（117）与密集生成（114）各占总量的约 14–16%，确保了对海报合成各个方面的均衡覆盖。

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

**EN** Figure 5: Benchmark statistics for understanding tasks (top) and generation tasks (bottom).

**ZH** 图 5：理解任务（上图）与生成任务（下图）的基准统计。

**EN** Appendix B Task Evaluation

**ZH** 附录 B 任务评测

**EN** OCR Accuracy (Text Instance Level): For logo OCR and poster OCR, we evaluate accuracy at the text-instance level. Invisible characters (e.g., spaces and line breaks) are stripped from both prediction and ground truth, and an instance is counted as correct only under exact match. The overall accuracy (AC) is then given by the average proportion of correctly recognized text instances:

**ZH** OCR 准确率（文本实例级）：对 Logo OCR 与海报 OCR，我们在文本实例级别评测准确率。预测与真值均先剥离不可见字符（如空格与换行），只有在完全匹配时才计为正确。整体准确率（AC）由正确识别的文本实例平均占比给出：

<!-- [原子块 · table] AC = 1 N ​ ∑ i = 1 N 𝟙 ​ ( T ^ i = T i ) , \textit{AC}=\frac{1}{N}\sum_{i=1}^{N}\mathbbm{1}\left(\hat{T}_{i}=T_{i}\right), (1) -->

**EN** where ⟦SLOT_15⟧ is the total number of text instances, ⟦SLOT_16⟧ is the predicted text for instance ⟦SLOT_17⟧, and ⟦SLOT_18⟧ is the corresponding ground-truth text. The function ⟦SLOT_19⟧ is an indicator that returns 1 if the condition holds and 0 otherwise. Each logo is counted as a single text instance, while a poster can contain multiple text instances.

**ZH** 其中 ⟦SLOT_15⟧ 为文本实例总数，⟦SLOT_16⟧ 为第 ⟦SLOT_17⟧ 个实例的预测文本，⟦SLOT_18⟧ 为对应的真值文本。函数 ⟦SLOT_19⟧ 为指示函数，条件成立时返回 1，否则返回 0。每个标识计为一个文本实例，而一张海报可包含多个文本实例。

**EN** Word-level Recall for Robust OCR: This metric is used for the synthetic OCR tasks: Simple OCR, Hard OCR, and Font-Size OCR. Given a ground-truth text string, we split it into consecutive units ⟦SLOT_20⟧, each consisting of five characters. For each unit ⟦SLOT_21⟧, we check whether it appears as a substring in the model-predicted long text output. This normalization makes scores comparable across texts of different lengths. The word-level recall (⟦SLOT_22⟧) is then defined as the proportion of ground-truth units that are recovered in the prediction:

**ZH** 鲁棒 OCR 的词级召回率：该指标用于合成类 OCR 任务，即简单 OCR、困难 OCR 与字号 OCR。给定真值文本串，我们把它切分为连续的单元 ⟦SLOT_20⟧，每个单元由五个字符组成。对每个单元 ⟦SLOT_21⟧，检查其是否作为子串出现在模型预测的长文本输出中。这一归一化使不同长度文本之间的分数可比。词级召回率（⟦SLOT_22⟧）定义为在预测中被恢复的真值单元所占比例：

<!-- [原子块 · table] W ​ R = ∑ g ∈ G 𝟙 ​ ( g ⊆ o ​ u ​ t ​ p ​ u ​ t ) | G | , \textit{$WR$}=\frac{\sum_{g\in G}\mathbbm{1}\left(g\subseteq output\right)}{|G|}, (2) -->

**EN** where ⟦SLOT_23⟧ denotes the set of all five-character units extracted from the ground-truth text, and ⟦SLOT_24⟧ is an indicator function that returns 1 when the condition is satisfied and 0 otherwise. Before segmentation, spaces and escape characters are stripped, and each word is guaranteed to appear at most once in a given image.

**ZH** 其中 ⟦SLOT_23⟧ 表示从真值文本中抽取的全部五字符单元的集合，⟦SLOT_24⟧ 为指示函数，条件满足时返回 1，否则返回 0。切分之前会剥离空格与转义字符，且每个词保证在给定图像中最多出现一次。

**EN** We define ⟦SLOT_25⟧ as the difference between the WR scores on Simple OCR and Hard OCR. This gap reflects the robustness of the model to noise: a larger ⟦SLOT_26⟧ indicates higher sensitivity to background clutter, missing context, rotation, and other perturbations.

**ZH** 我们把 ⟦SLOT_25⟧ 定义为简单 OCR 与困难 OCR 上 WR 分数之差。该差距反映模型对噪声的鲁棒性：⟦SLOT_26⟧ 越大，说明模型对背景杂乱、上下文缺失、旋转等扰动越敏感。

**EN** For the Font-Size OCR task, we additionally report the standard deviation Std of the WR scores across 14 different font sizes. This metric captures the robustness of the model’s OCR performance with respect to changes in font size: lower Std indicates more stable recognition across scales.

**ZH** 对字号 OCR 任务，我们额外报告 14 种不同字号下 WR 分数的标准差 Std。该指标刻画模型 OCR 性能随字号变化的鲁棒性：Std 越低，说明跨尺度的识别越稳定。

**EN** K-Option Scoring for Multiple-Choice Tasks: For tasks where the model predicts a label from a finite set of options, we use multiple-choice style metrics. This applies to the font-related tasks (Font Matching, Font Attributes, and Font Effects), where we report Score, Effect Score, and Color Score; to the Style Understanding task, where we report a style classification Score; to the Text Position task, where Alignment and Rotation are cast as discrete choices; and to Layout Comparison, where we also use a multiple-choice Score. For multiple-choice tasks with ⟦SLOT_27⟧ answer options, let the model’s accuracy be ⟦SLOT_28⟧, where ⟦SLOT_29⟧. The scoring formula normalizes the score such that random guessing results in a score of zero, and perfect accuracy results in a score of one:

**ZH** 多选任务的 K 选项计分：对模型需从有限选项集中预测标签的任务，我们采用多选式指标。这适用于字体相关任务（字体匹配、字体属性与字体效果），其中报告 Score、Effect Score 与 Color Score；风格理解任务，其中报告风格分类 Score；文字位置任务，其中对齐与旋转被转化为离散选择；以及版面比较，同样采用多选 Score。对于含 ⟦SLOT_27⟧ 个答案选项的多选任务，设模型准确率为 ⟦SLOT_28⟧，其中 ⟦SLOT_29⟧。计分公式把分数归一化，使得随机猜测得分为零，完全答对得分为一：

<!-- [原子块 · table] Score = max ⁡ ( 0 , k ⋅ a − 1 k − 1 ) . \text{Score}=\max\left(0,\frac{k\cdot a-1}{k-1}\right). (3) -->

**EN** Under random guessing, the expected accuracy is ⟦SLOT_30⟧, which maps to a score of zero in our formulation. When the model attains perfect accuracy ⟦SLOT_31⟧, the score reaches one.

**ZH** 在随机猜测下，期望准确率为 ⟦SLOT_30⟧，在我们的公式中对应分数零。当模型达到完全准确率 ⟦SLOT_31⟧ 时，分数为一。

**EN** This scoring scheme is used for the font-related tasks, the text positioning task, and the layout comparison task.

**ZH** 该计分方案用于字体相关任务、文字定位任务与版面比较任务。

**EN** Bbox-Related Metrics: For the Text Localization task, ground-truth bounding boxes are first sorted in descending order by area. We then evaluate the average Intersection over Union (IoU) over the top-⟦SLOT_32⟧ predicted boxes:

**ZH** 边界框相关指标：对文字定位任务，真值边界框先按面积降序排列。随后我们在前 ⟦SLOT_32⟧ 个预测框上计算平均交并比（IoU）：

<!-- [原子块 · table] IoU = 1 n ​ ∑ j = 1 n | B j pred ∩ B j gt | | B j pred ∪ B j gt | , \text{IoU}=\frac{1}{n}\sum_{j=1}^{n}\frac{\lvert B_{j}^{\text{pred}}\cap B_{j}^{\text{gt}}\rvert}{\lvert B_{j}^{\text{pred}}\cup B_{ -->

**EN** where ⟦SLOT_33⟧ and ⟦SLOT_34⟧ denote the predicted and ground-truth boxes for the ⟦SLOT_35⟧-th instance.

**ZH** 其中 ⟦SLOT_33⟧ 与 ⟦SLOT_34⟧ 分别表示第 ⟦SLOT_35⟧ 个实例的预测框与真值框。

**EN** To further assess prompt-following behavior, we examine how well the number of predicted boxes matches the number of queried text instances. For each sample, if the model predicts fewer boxes than requested, we compute the recall as the ratio between the number of predicted boxes and the number of queried objects. If it predicts more boxes than requested, we assign a recall of 1. The final recall score is the average over all samples:

**ZH** 为进一步评估提示词遵循情况，我们考察预测框数量与被查询文本实例数量的匹配程度。对每个样本，若模型预测的框数少于请求数量，则把召回率计算为预测框数与查询物体数之比；若预测的框数多于请求数量，则赋予召回率 1。最终的召回分数为所有样本上的平均值：

<!-- [原子块 · table] Recall Rate = 1 N ​ ∑ i = 1 N { n i pred n i query , if ​ n i pred ≤ n i query , 1 , otherwise , \text{Recall Rate}=\frac{1}{N}\sum_{i=1}^{N}\begin{cases}\frac{n_{i}^{\text{pred}}}{n_{i}^{\text{query} -->

**EN** where ⟦SLOT_36⟧ is the total number of evaluation samples, ⟦SLOT_37⟧ is the number of predicted boxes for sample ⟦SLOT_38⟧, and ⟦SLOT_39⟧ is the number of query objects specified in the prompt.

**ZH** 其中 ⟦SLOT_36⟧ 为评测样本总数，⟦SLOT_37⟧ 为样本 ⟦SLOT_38⟧ 的预测框数，⟦SLOT_39⟧ 为提示词中指定的查询物体数。

**EN** In the Layout Generation task, there is no uniquely correct placement of layout boxes, so standard IoU-based matching is not directly applicable. Instead, we evaluate the predicted layout by comparing the relative positions and areas of predicted boxes with those of the ground truth. Higher-quality layouts exhibit smaller Center Bias and an Area Ratio closer to 1.

**ZH** 在版面生成任务中，版面框不存在唯一正确的摆放方式，因此基于 IoU 的标准匹配无法直接适用。我们改为比较预测框与真值框的相对位置与面积来评价预测版面。质量更高的版面表现为更小的中心偏移（Center Bias）和更接近 1 的面积比（Area Ratio）。

**EN** Center Bias quantifies the normalized Euclidean distance between the centers of the predicted and ground-truth boxes:

**ZH** 中心偏移量化预测框与真值框中心之间的归一化欧氏距离：

<!-- [原子块 · table] Center Bias = 1 N ​ ∑ i = 1 N ‖ C i pred − C i gt ‖ 2 , \text{Center Bias}=\frac{1}{N}\sum_{i=1}^{N}\bigl\|C_{i}^{\text{pred}}-C_{i}^{\text{gt}}\bigr\|_{2}, (6) -->

**EN** where ⟦SLOT_40⟧ and ⟦SLOT_41⟧ are the normalized center coordinates of the predicted and ground-truth box for the ⟦SLOT_42⟧-th element.

**ZH** 其中 ⟦SLOT_40⟧ 与 ⟦SLOT_41⟧ 分别为第 ⟦SLOT_42⟧ 个元素的预测框与真值框的归一化中心坐标。

**EN** Area Ratio measures how similar the box areas are by taking the ratio between the smaller and larger area:

**ZH** 面积比通过取较小面积与较大面积之比来度量两个框面积的相近程度：

<!-- [原子块 · table] Area Ratio = 1 N ​ ∑ i = 1 N min ⁡ ( A i pred , A i gt ) max ⁡ ( A i pred , A i gt ) , \text{Area Ratio}=\frac{1}{N}\sum_{i=1}^{N}\frac{\min\!\bigl(A_{i}^{\text{pred}},A_{i}^{\text{gt}}\bigr)}{\max\!\ -->

**EN** where ⟦SLOT_43⟧ and ⟦SLOT_44⟧ denote the areas of the predicted and ground-truth boxes, respectively.

**ZH** 其中 ⟦SLOT_43⟧ 与 ⟦SLOT_44⟧ 分别表示预测框与真值框的面积。

**EN** Empty-Space Evaluation. In the Empty-Space task, both the ground truth and the model output are represented as sets of patch IDs. The ground truth set corresponds to the patches annotated as suitable empty regions, and the model is asked to predict a set of patch IDs for placing new content. We first measure the agreement between these sets using Intersection over Union (IoU):

**ZH** 留白评测。在留白任务中，真值与模型输出均表示为图块编号的集合。真值集合对应被标注为适宜留白区域的图块，模型则被要求预测一组用于放置新内容的图块编号。我们先用交并比（IoU）度量两个集合的一致程度：

<!-- [原子块 · table] Patch IoU = 1 N ​ ∑ i = 1 N | 𝒫 pred ∩ 𝒫 gt | | 𝒫 pred ∪ 𝒫 gt | , \text{Patch IoU}=\frac{1}{N}\sum_{i=1}^{N}\frac{\lvert\mathcal{P}_{\text{pred}}\cap\mathcal{P}_{\text{gt}}\rvert}{\lvert\mathcal{P}_{\ -->

**EN** where ⟦SLOT_45⟧ and ⟦SLOT_46⟧ denote the predicted and ground-truth patch ID sets, respectively.

**ZH** 其中 ⟦SLOT_45⟧ 与 ⟦SLOT_46⟧ 分别表示预测与真值的图块编号集合。

**EN** Match Accuracy. The prompt also specifies how many patch IDs should be returned. We therefore evaluate prompt-following behavior by checking whether the predicted set size matches the requested size. Match Accuracy is defined as the proportion of samples that satisfy this constraint:

**ZH** 匹配准确率。提示词中还指定了应返回的图块编号个数。因此我们通过检查预测集合大小是否与请求大小相符来评估提示词遵循情况。匹配准确率定义为满足该约束的样本占比：

<!-- [原子块 · table] Match Accuracy = 1 N ​ ∑ i = 1 N 𝟙 ​ ( | 𝒫 pred | = | 𝒫 gt | ) , \text{Match Accuracy}=\frac{1}{N}\sum_{i=1}^{N}\mathbbm{1}\bigl(\lvert\mathcal{P}_{\text{pred}}\rvert=\lvert\mathcal{P}_{\text{gt}}\rve -->

**EN** where ⟦SLOT_47⟧ is the number of evaluation samples, ⟦SLOT_48⟧ is the predicted patch set for sample ⟦SLOT_49⟧, ⟦SLOT_50⟧ is the number of patch IDs requested in the prompt, and ⟦SLOT_51⟧ is an indicator function that returns 1 if the condition holds and 0 otherwise.

**ZH** 其中 ⟦SLOT_47⟧ 为评测样本数，⟦SLOT_48⟧ 为样本 ⟦SLOT_49⟧ 的预测图块集合，⟦SLOT_50⟧ 为提示词请求的图块编号个数，⟦SLOT_51⟧ 为指示函数，条件成立时返回 1，否则返回 0。

**EN** Point Score for Advanced Understanding Metrics: For intention understanding, each creative advertisement poster is paired with a set of manually annotated key elements that summarize the intended semantic or conceptual message of the design. To evaluate whether an MLLM can correctly capture and verbalize these elements, we use GPT-5 as an automatic judge. Given a model-generated caption, the judge checks for each key element whether it is correctly identified and explicitly mentioned. For a given poster, the prediction is labeled Yes if all annotated key points are covered, and No otherwise. The resulting Point Score is defined as the fraction of posters judged as Yes:

**ZH** 高级理解指标的要点得分：对意图理解，每张创意广告海报都配有一组人工标注的关键元素，用以概括设计所要传达的语义或概念信息。为评估 MLLM 能否正确捕捉并用语言表述这些元素，我们使用 GPT-5 作为自动评审模型。给定模型生成的描述，评审模型逐一检查每个关键元素是否被正确识别并明确提及。对某张海报，若全部标注要点都被覆盖，则预测标记为“是”，否则为“否”。由此得到的要点得分定义为被判为“是”的海报占比：

<!-- [原子块 · table] Point Score = N Yes N Total , \text{Point Score}=\frac{N_{\text{Yes}}}{N_{\text{Total}}}, (10) -->

**EN** where ⟦SLOT_52⟧ is the number of posters whose model-generated captions successfully cover all key points, and ⟦SLOT_53⟧ is the total number of evaluated posters.

**ZH** 其中 ⟦SLOT_52⟧ 为模型生成的描述成功覆盖全部要点的海报数，⟦SLOT_53⟧ 为被评测的海报总数。

**EN** For Composition Understanding, we adopt the same Point Score metric.

**ZH** 对构图理解，我们采用相同的要点得分指标。

**EN** Overall Rating Metric: In the Overall Rating task, both humans and MLLMs assign a quality score in the range 0–10 for each poster. We first normalize human and model scores to have zero mean, and then measure their agreement via cosine similarity. Formally, let ⟦SLOT_54⟧ and ⟦SLOT_55⟧ denote the human and model score vectors over ⟦SLOT_56⟧ posters. We compute the zero-mean versions

**ZH** 整体评分指标：在整体评分任务中，人类与 MLLM 都为每张海报打出 0–10 的质量分。我们先把人类与模型的分数归一化为零均值，再通过余弦相似度度量二者的一致程度。形式化地，设 ⟦SLOT_54⟧ 与 ⟦SLOT_55⟧ 分别表示 ⟦SLOT_56⟧ 张海报上的人类与模型分数向量，我们计算其零均值版本

<!-- [原子块 · table] 𝐡 ~ = 𝐡 − h ¯ ​ 𝟏 , 𝐦 ~ = 𝐦 − m ¯ ​ 𝟏 , \tilde{\mathbf{h}}=\mathbf{h}-\bar{h}\mathbf{1},\quad\tilde{\mathbf{m}}=\mathbf{m}-\bar{m}\mathbf{1}, (11) -->

**EN** where ⟦SLOT_57⟧ and ⟦SLOT_58⟧ are the mean human and model scores, and ⟦SLOT_59⟧ is an all-ones vector. The final metric is the cosine similarity between the two normalized vectors:

**ZH** 其中 ⟦SLOT_57⟧ 与 ⟦SLOT_58⟧ 分别为人类与模型分数的均值，⟦SLOT_59⟧ 为全一向量。最终指标为两个归一化向量之间的余弦相似度：

<!-- [原子块 · table] Overall Rating = 𝐡 ~ ⊤ ​ 𝐦 ~ ‖ 𝐡 ~ ‖ 2 ​ ‖ 𝐦 ~ ‖ 2 . \text{Overall Rating}=\frac{\tilde{\mathbf{h}}^{\top}\tilde{\mathbf{m}}}{\|\tilde{\mathbf{h}}\|_{2}\,\|\tilde{\mathbf{m}}\|_{2}}. (12) -->

**EN** Point Score for Poster Generation: For the Dense Generation, Composition Generation, and Intention Generation tasks, we use the Point Score to evaluate whether the generated image covers all required key elements. Each generated poster is associated with multiple checkpoints (e.g., required objects, layout cues, or semantic intentions), and a MLLM judge determines for each checkpoint whether it is correctly realized in the image.

**ZH** 海报生成的要点得分：对密集生成、构图生成与意图生成任务，我们使用要点得分评估生成的图像是否覆盖全部必需的关键元素。每张生成的海报关联多个检查点（如必需的物体、版面线索或语义意图），由 MLLM 评审模型逐项判定每个检查点是否在图像中被正确实现。

**EN** Concretely, we use GPT-5 as the automatic judge for Dense Generation and Intention Generation, and Gemini-2.5-Pro as the judge for Composition Generation. The Point Score is then computed as in Eq. (10), i.e., as the fraction of images whose generated content is judged to cover all annotated key points.

**ZH** 具体地，我们使用 GPT-5 作为密集生成与意图生成的自动评审模型，使用 Gemini-2.5-Pro 作为构图生成的评审模型。要点得分的计算同式（10），即被判定为覆盖全部标注关键点的图像所占比例。

**EN** Score for Style Generation. In the Style Generation task, the generative model is instructed (via a textual prompt) to produce a poster in a specified target style. A MLLM is then asked to classify the generated poster into one of the predefined style labels. We compare the predicted style label with the ground-truth target label and compute a style generation score as the accuracy over all evaluated samples:

**ZH** 风格生成的得分。在风格生成任务中，生成模型被指示（通过文字提示词）产出指定目标风格的海报。随后要求 MLLM 把生成的海报分类到预定义的风格标签之一。我们把预测的风格标签与真值目标标签比较，并计算风格生成得分为全部被评测样本上的准确率：

<!-- [原子块 · table] Style Score = 1 N ​ ∑ i = 1 N 𝟙 ​ ( s ^ i = s i gt ) , \text{Style Score}=\frac{1}{N}\sum_{i=1}^{N}\mathbbm{1}\bigl(\hat{s}_{i}=s_{i}^{\text{gt}}\bigr), (13) -->

**EN** where ⟦SLOT_60⟧ is the number of generated posters, ⟦SLOT_61⟧ is the style label predicted by the MLLM (GPT-5) for the ⟦SLOT_62⟧-th poster, ⟦SLOT_63⟧ is the corresponding ground-truth style label, and ⟦SLOT_64⟧ is the indicator function.

**ZH** 其中 ⟦SLOT_60⟧ 为生成的海报数，⟦SLOT_61⟧ 为 MLLM（GPT-5）对第 ⟦SLOT_62⟧ 张海报预测的风格标签，⟦SLOT_63⟧ 为对应的真值风格标签，⟦SLOT_64⟧ 为指示函数。

**EN** Font Richness for Font Generation. In the Font Generation task, the generative model is prompted to produce posters with diverse typography, where the prompt explicitly specifies the target text and encourages the use of varied font styles. After generation, we ask an MLLM with strong font understanding ability (GPT-5) to describe the typography of each poster using a fixed vocabulary of font attributes (e.g., modern, playful, serif, italic, etc.).

**ZH** 字体生成的字体丰富度。在字体生成任务中，生成模型被提示生成字体排印多样的海报，提示词明确指定目标文字并鼓励使用多样的字体风格。生成之后，我们请具备较强字体理解能力的 MLLM（GPT-5）用固定的字体属性词表（如现代、活泼、衬线、斜体等）描述每张海报的字体排印。

**EN** Let ⟦SLOT_65⟧ be the set of all font attributes (e.g., the 37 attributes in our implementation), and ⟦SLOT_66⟧. For a batch of ⟦SLOT_67⟧ generated posters, we define a binary indicator ⟦SLOT_68⟧ that equals 1 if GPT-5 assigns attribute ⟦SLOT_69⟧ to the ⟦SLOT_70⟧-th poster, and 0 otherwise. For each attribute ⟦SLOT_71⟧, we first compute its coverage ratio over the batch:

**ZH** 设 ⟦SLOT_65⟧ 为全部字体属性的集合（在我们的实现中为 37 个属性），且 ⟦SLOT_66⟧。对于一批 ⟦SLOT_67⟧ 张生成的海报，我们定义二值指示变量 ⟦SLOT_68⟧，当 GPT-5 把属性 ⟦SLOT_69⟧ 赋予第 ⟦SLOT_70⟧ 张海报时取 1，否则取 0。对每个属性 ⟦SLOT_71⟧，先计算其在该批次上的覆盖率：

<!-- [原子块 · table] R a = 1 N ​ ∑ i = 1 N x i , a , R_{a}=\frac{1}{N}\sum_{i=1}^{N}x_{i,a}, (14) -->

**EN** which measures how frequently attribute ⟦SLOT_72⟧ appears across generated posters.

**ZH** 该值度量属性 ⟦SLOT_72⟧ 在生成的海报中出现的频繁程度。

**EN** The overall Font Richness Score is then defined as the average coverage ratio over all attributes:

**ZH** 整体的字体丰富度得分则定义为所有属性上覆盖率的平均值：

<!-- [原子块 · table] Richness = 1 M ​ ∑ a ∈ 𝒜 R a = 1 N ​ M ​ ∑ a ∈ 𝒜 ∑ i = 1 N x i , a . \text{Richness}=\frac{1}{M}\sum_{a\in\mathcal{A}}R_{a}=\frac{1}{NM}\sum_{a\in\mathcal{A}}\sum_{i=1}^{N}x_{i,a}. (15) -->

**EN** Intuitively, this metric reflects how widely the generator explores the font attribute space: higher values indicate that a broader range of font attributes is realized across the generated posters.

**ZH** 直观地说，该指标反映生成器对字体属性空间的探索广度：取值越高，说明生成的海报覆盖的字体属性范围越广。

**EN** Appendix C Human Evaluation

**ZH** 附录 C 人工评测

**EN** To verify the reliability of our automatic evaluation, we conduct a series of human studies on both understanding and generation tasks. For several understanding tasks that rely on LLM-based textual judgments (e.g., Composition Understanding and Intention Understanding), we compare the decisions of the automatic judge with those of human annotators. On a subset, the agreement between the LLM judge and human evaluation reaches approximately 92%, indicating that our LLM-as-judge protocol is largely consistent with human judgments.

**ZH** 为验证自动评测的可靠性，我们针对理解与生成任务开展了一系列人工研究。对若干依赖大语言模型文本判断的理解任务（如构图理解与意图理解），我们把自动评审模型的判定与人工标注员的判定进行比对。在子集上，大语言模型评审与人工评测的一致率达到约 92%，说明我们的“以大语言模型为评审”的方案与人类判断大体一致。

**EN** For the Generation tasks, we employ MLLMs to repeatedly assess the quality and faithfulness of generated images. Specifically, in Dense Generation, Composition Generation, and Intention Generation, the judge verifies whether multiple key pieces of information are correctly rendered in the image, while in Font Generation and Style Generation, the judge directly assigns font or style labels to each poster. To validate these automatic scores, we randomly sample 30 generated images per task and obtain human ratings under the same criteria. We observe that the relative ranking of generative models remains largely consistent across different MLLM judges and human annotators, suggesting that our automatic evaluation provides a stable and trustworthy proxy for human assessment.

**ZH** 对生成任务，我们采用 MLLM 反复评估生成图像的质量与忠实度。具体地，在密集生成、构图生成与意图生成中，评审模型核验多个关键信息是否被正确渲染到图像中；在字体生成与风格生成中，评审模型直接为每张海报赋予字体或风格标签。为验证这些自动分数，我们在每个任务上随机抽取 30 张生成的图像，并在相同标准下获取人工评分。我们观察到，生成模型的相对排序在不同的 MLLM 评审模型与人工标注员之间大体保持一致，说明我们的自动评测为人类评估提供了稳定可信的替代。

**EN** Appendix D Annotator Guideline

**ZH** 附录 D 标注员指南

**EN** We adopt a multi–stage pipeline for data collection and annotation. First, we gather poster images from free sources that explicitly permit research use. All raw images are manually cleaned to remove samples with blurry content, severe artifacts, or copyright concerns. For OCR-related understanding tasks, we rely on reliable digital sources as ground-truth text. Human annotation is mainly required for layout-related tasks, advanced understanding tasks, and the overall rating task.

**ZH** 我们采用多阶段流程进行数据采集与标注。首先，从明确允许研究使用的免费来源收集海报图像。全部原始图像都经过人工清洗，去除内容模糊、存在严重瑕疵或有版权顾虑的样本。对与 OCR 相关的理解任务，我们依赖可靠的数字来源作为真值文本。人工标注主要用于版面相关任务、高级理解任务与整体评分任务。

**EN** For each such task, at least three expert annotators independently label every sample. A senior annotator (the leader) then cross-checks all submissions, resolves disagreements, and filters out ambiguous cases, retaining only samples with high inter-annotator agreement. Below we summarize the concrete annotation guidelines for representative tasks.

**ZH** 对每一项此类任务，至少由三名专家标注员独立标注每个样本。随后由一名资深标注员（组长）交叉核对全部提交结果，裁定分歧并剔除含糊的样本，只保留标注员间一致度高的样本。下面概述代表性任务的具体标注指南。

**EN** Empty Space Task. We begin from partially edited poster designs, where some design elements have been intentionally removed from the original PSD files. The resulting posters are rendered with an overlaid grid, and the grid patch indices are visible to annotators. Each poster is sent to three annotators with the following instruction: “This is an unfinished poster. New design elements need to be added. Please identify all patch IDs that you consider suitable empty regions for placing new content.” The leader aggregates the proposed patch sets and retains only those samples whose recommended regions achieve more than 90% agreement across annotators, making a final decision when minor discrepancies occur.

**ZH** 留白任务。我们从经过部分编辑的海报设计出发，其中一些设计元素被有意从原始 PSD 文件中移除。生成的海报渲染时叠加网格，网格图块的编号对标注员可见。每张海报分发给三名标注员，指令如下：“这是一张未完成的海报，需要加入新的设计元素。请找出你认为适合放置新内容的全部留白区域的图块编号。”组长汇总各方提出的图块集合，只保留推荐区域在标注员间一致度超过 90% 的样本，出现细微分歧时由组长做出最终裁定。

**EN** Composition Understanding Task. We collect posters that exhibit strong visual reconstruction or structural composition (e.g., displacement, nesting, segmentation). Each poster is distributed to multiple annotators with the instruction: “Using concise natural language, list the visual design techniques used in this poster (such as displacement, nesting, segmentation, extension, focus, mirroring, cut-out, arrangement, etc.). Describe only the necessary composition cues in bullet points.” The leader reviews and consolidates all descriptions, and keeps only those posters for which different annotators provide highly consistent composition cues.

**ZH** 构图理解任务。我们收集具有强烈视觉重构或结构构成特征的海报（如位移、嵌套、分割）。每张海报分发给多名标注员，指令如下：“用简洁的自然语言，列出这张海报所使用的视觉设计手法（如位移、嵌套、分割、延展、聚焦、镜像、抠图、排布等）。以要点形式只描述必要的构图线索。”组长审阅并整合所有描述，只保留不同标注员给出高度一致构图线索的海报。

**EN** Intention Understanding Task. We curate posters that contain clear visual metaphors or conceptual designs. Each poster is assigned to several annotators with the instruction: “First, carefully read the content in the poster. Then, search for the original source or explanation of this poster online. If the external explanation aligns with your own understanding, keep this sample and decompose its core metaphor or concept into several key pieces of information. If the external explanation conflicts with your interpretation, discard this sample.” The leader then collects and refines the key-intention annotations, merging overlapping items and removing noisy or inconsistent samples.

**ZH** 意图理解任务。我们筛选包含明确视觉隐喻或概念设计的海报。每张海报分配给若干标注员，指令如下：“先仔细阅读海报中的内容。然后在网上检索该海报的原始出处或阐释。若外部阐释与你的理解一致，则保留该样本，并把其核心隐喻或概念拆解为若干条关键信息。若外部阐释与你的解读相冲突，则丢弃该样本。”组长随后收集并精炼关键意图标注，合并重叠项，剔除噪声与不一致的样本。

**EN** Overall Rating Task. For the overall quality assessment, we distribute each poster to multiple annotators with the instruction: “Please rate the overall design quality of this poster on a scale from 0 to 10, where 0 is the worst and 10 is the best. Consider font properties, layout, textual communication, and creative concept in your score.” Because different annotators may use different scoring ranges, we first standardize their score distributions (zero-mean and variance normalization), and then discard posters whose inter-annotator score range exceeds a predefined threshold. The remaining posters, which exhibit high rating consistency, are averaged to obtain a stable ground-truth score used in our benchmark.

**ZH** 整体评分任务。对整体质量评估，我们把每张海报分发给多名标注员，指令如下：“请按 0 到 10 分评价这张海报的整体设计质量，0 分为最差，10 分为最好。评分时请考虑字体属性、版式、文字传达与创意概念。”由于不同标注员可能使用不同的评分区间，我们先对各自的分数分布做标准化（零均值与方差归一化），再剔除标注员间分数极差超过预设阈值的海报。剩余评分一致性高的海报取平均，得到本基准使用的稳定真值分数。

**EN** Appendix E Task Illustration

**ZH** 附录 E 任务示例

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

**EN** Appendix F Generation Task Results

**ZH** 附录 F 生成任务结果

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->
