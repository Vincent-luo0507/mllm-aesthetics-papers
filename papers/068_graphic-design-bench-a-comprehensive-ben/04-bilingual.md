# Graphic-Design-Bench：面向平面设计任务的 AI 综合评测基准

> 原标题：Graphic-Design-Bench: A Comprehensive Benchmark for Evaluating AI on Graphic Design Tasks
> 作者：Adrienne Deganutti, Elad Hirsch, Haonan Zhu, Jaejung Seol, Purvanshi Mehta · arXiv:2604.04192 · 2026-04-05

**EN** [Path=figures/fonts/] [Path=figures/fonts/] [Path=figures/fonts/] [Path=figures/fonts/]

**ZH** [Path=figures/fonts/] [Path=figures/fonts/] [Path=figures/fonts/] [Path=figures/fonts/]

<!-- [原子块 · verbatim] Graphic-Design-Bench: A Comprehensive Benchmark for Evaluating AI on Graphic Design Tasks -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] We introduce GraphicDesignBench (GDB), the first comprehensive benchmark suite designed specifically to evaluate AI models on the full breadth of professional graphic design tasks. Unlike existing ben -->

<!-- [原子块 · table]  -->

**EN** 1 Introduction

**ZH** 1 引言

**EN** Design shapes how humans interact with the world, from the layout of a webpage to the typography on a billboard, visual communication is embedded in nearly every product, brand, and piece of media we encounter. At its most structured, this manifests as graphic design: a high-dimensional creative task that integrates spatial layout, typography, color theory, brand identity, and communicative intent into a single visual artifact. Recent advances in vision-language models and diffusion-based image generators have raised the prospect of AI systems that can assist human designers [1, 2, 3, 4, 5], yet the evaluation landscape has not kept pace. Existing benchmarks either measure low-level perceptual quality on natural images [6, 7, 8] or probe generic visual question-answering, neither of which captures the structured, intent-driven, and multi-layered nature of professional design work.

**ZH** 设计塑造着人与世界的交互方式：从网页的版式到广告牌上的文字排布，视觉传达几乎嵌入我们接触的每一件产品、每一个品牌与每一种媒介。其最具结构性的形态便是平面设计——一项高维创造性任务，把空间版式、字体排印、色彩理论、品牌识别与传达意图整合为单一的视觉作品。视觉语言模型与基于扩散的图像生成器的近期进展，让「AI 系统辅助人类设计师」的前景变得可期 [1, 2, 3, 4, 5]，但评测体系并未同步跟进。现有基准要么度量自然图像的低层感知质量 [6, 7, 8]，要么考察通用视觉问答，二者都无法刻画专业设计工作中那种结构化、意图驱动、多层次的特性。

**EN** This gap matters because design tasks impose constraints that differ qualitatively from those in natural-image benchmarks, along several dimensions:

**ZH** 这一缺口之所以重要，是因为设计任务所施加的约束与自然图像基准中的约束存在质的差异，体现在以下几个方面：

**EN** • Multi-constraint satisfaction. A promotional banner is not merely an aesthetically pleasing image; it must render specific text strings legibly, respect a typographic hierarchy, place components within an established grid, and communicate a clear call to action, all simultaneously. Evaluating this requires tasks that test each constraint independently and in combination.

**ZH** • 多约束同时满足。一张促销横幅并非只要美观就行；它必须清晰呈现指定的文字串、遵循字体层级、把各组件摆在既定网格之内，并传达明确的行动号召，而且这些要求必须同时成立。评测它需要能独立地、也能组合地检验每一条约束的任务。

**EN** • Design-specific evaluation. Measuring whether a model meets these requirements demands task-specific metrics such as OCR-based readability, bounding-box IoU for component placement, and perceptually uniform color distance for style fidelity, none of which are captured by FID or CLIPScore.

**ZH** • 面向设计的评测。衡量模型是否满足这些要求，需要任务专属的指标，例如基于 OCR 的可读性、用于组件位置的边界框 IoU，以及用于风格保真的感知均匀色距；这些都不是 FID 或 CLIPScore 所能涵盖的。

**EN** • Continuously evolving standards. Visual trends shift continuously across cultures, platforms, and time, meaning that what constitutes good design is not a fixed target. A benchmark must account for this moving landscape rather than treating design quality as a static property.

**ZH** • 标准持续演化。视觉趋势随文化、平台与时间不断迁移，何谓好设计并非固定靶标。基准必须容纳这种变动的格局，而不是把设计质量当作静态属性。

**EN** • Brand and context dependence. Effective design is often deeply tied to a specific brand identity or creative voice. Unlike object recognition or depth estimation, there is rarely a single objectively correct design solution, making standardized evaluation fundamentally harder than in natural-image settings where ground truth is stable and context-independent.

**ZH** • 依赖品牌与语境。好的设计往往与特定品牌识别或创意调性深度绑定。与目标识别或深度估计不同，设计问题极少存在唯一客观正确的解，这使得标准化评测从根本上比自然图像场景更为困难——后者的真值稳定且与语境无关。

**EN** The latter two challenges represent open problems for the field at large. In this work, we focus on the first two: constructing tasks that jointly stress-test multi-constraint satisfaction and measuring performance with design-native metrics. Together, these form the foundation of GraphicDesignBench (GDB) a benchmark suite comprising 49 tasks that collectively evaluate the full spectrum of design-relevant capabilities. Our contributions are as follows:

**ZH** 后两项挑战属于整个领域尚未解决的开放问题。本文聚焦前两项：构造能同时压力测试多约束满足能力的任务，并用设计原生的指标度量性能。二者共同构成 GraphicDesignBench（GDB）的基础——一套包含 49 个任务的基准套件，整体上评估全部与设计相关的能力。本文贡献如下：

**EN** 1. The first comprehensive benchmark for graphic design AI. We introduce GDB, covering 49 tasks across layout, typography, SVG & vector, and animation, spanning both understanding and generation, and representing the broadest evaluation of AI design capabilities to date.

**ZH** 1. 首个面向平面设计 AI 的综合基准。我们提出 GDB，覆盖版式、排版、SVG 与矢量、动画等领域的 49 个任务，同时涵盖理解与生成两类设定，是迄今对 AI 设计能力最广泛的评测。

**EN** 2. A layered-composition evaluation framework. By grounding all tasks in the LICA dataset’s [9] full structural metadata (bounding boxes, z-ordering, typography specs, animation properties, SVG source), we enable evaluation settings that are fundamentally impossible with flat raster images, including partial layout completion, layer-aware inpainting, and template variant generation.

**ZH** 2. 分层合成评测框架。通过把所有任务锚定在 LICA 数据集 [9] 的完整结构元数据（边界框、层序、字体排印规格、动画属性、SVG 源码）之上，我们实现了平面位图根本无法支持的评测设定，包括部分版式补全、图层感知的图像补全与模板变体生成。

**EN** 3. Design-native metrics. We introduce a multi-faceted metric taxonomy purpose-built for design evaluation, combining spatial accuracy, typographic fidelity, structural validity, and human-aligned preference, moving beyond the perceptual quality scores (FID, CLIPScore) that dominate existing image benchmarks but fail to capture design-specific requirements.

**ZH** 3. 设计原生指标。我们提出一套专为设计评测构建的多维指标分类体系，综合空间精度、字体排印保真度、结构有效性与人类对齐的偏好，超越主导现有图像基准、却无法刻画设计专属要求的感知质量分数（FID、CLIPScore）。

**EN** 4. A reproducible framework for the community. Rather than a static leaderboard, GDB is designed as an extensible evaluation framework. We evaluate three state-of-the-art frontier model families to establish baselines, reveal persistent failure modes shared across all models, and provide a foundation for the community to benchmark future systems, including open-source models.

**ZH** 4. 面向社区的可复现框架。GDB 并非静态排行榜，而是一个可扩展的评测框架。我们评测三个前沿模型家族以建立基线，揭示所有模型共有的持续性失效模式，并为社区评测未来系统（包括开源模型）提供基础。

**EN** The remainder of this paper is organized as follows. Section 2 describes the dataset, evaluated models, and shared metric definitions. Sections 3–7 present tasks grouped by design domain, each covering both understanding and generation settings. Section 8 synthesizes cross-cutting findings, and Section 9 concludes with directions for future work.

**ZH** 本文其余部分组织如下。第 2 节介绍数据集、受评模型与共享指标定义。第 3～7 节按设计领域分组呈现任务，每个领域同时涵盖理解与生成设定。第 8 节综合跨领域的发现，第 9 节总结并给出未来工作方向。

**EN** 2 Benchmark Overview

**ZH** 2 基准概览

**EN** Dataset. All tasks in GDB are grounded in the LICA layered-composition dataset [9], a large-scale collection of real-world graphic design templates sourced from a commercial design platform. Unlike flat raster-image datasets, each LICA template preserves the full layered structure of the original design: individual components are annotated with their type (text, image, vector, group), bounding box, z-order, and styling properties. Text components carry typographic specifications including font family, size, weight, color, alignment, letter spacing, line height, curvature, rotation, and inline style ranges. Image and vector components include asset source references, rotation angles, clip paths, and opacity. Templates are further annotated with global metadata such as canvas aspect ratio, background color, category labels (parent and sub-category), user-intent descriptions, aesthetic tags, and color palettes. The animated subset additionally provides per-component entrance animation attributes: motion type (from 32 canonical categories), duration, start-time offset, and keyframe sequences. Each template may have multiple sibling layouts, instantiations that share the same structural theme but differ in content, color scheme, or imagery. This sibling structure enables evaluation settings such as template variant understanding (Section 6) and template variant generation, which cannot be constructed from isolated designs. Figure 1 shows examples from the data.

**ZH** 数据集。GDB 中的所有任务都锚定于 LICA 分层合成数据集 [9]——一个来自商业设计平台、规模庞大的真实平面设计模板集合。与平面位图数据集不同，每个 LICA 模板都保留原始设计的完整图层结构：各组件标注了类型（文本、图像、矢量、组）、边界框、层序与样式属性。文本组件带有字体排印规格，包括字族、字号、字重、颜色、对齐、字间距、行高、曲率、旋转与行内样式区间。图像与矢量组件包含素材来源引用、旋转角度、裁剪路径与不透明度。模板还带有全局元数据，如画布宽高比、背景色、类别标签（父类与子类）、用户意图描述、美学标签与调色板。动画子集额外提供逐组件的入场动画属性：运动类型（取自 32 个规范类别）、时长、起始时间偏移与关键帧序列。每个模板可有多个同源版式，即共享相同结构主题而在内容、配色或图像上有所差异的实例化版本。这种同源结构支撑了模板变体理解（第 6 节）与模板变体生成等评测设定，而这些设定无法由孤立的设计构造出来。图 1 给出了数据样例。

<!-- [原子块 · img]  -->

**EN** Figure 1: LICA samples [9]. Design layouts with structured, component-level annotations capturing full hierarchy and rich metadata beyond coarse bounding boxes, on which we benchmark models in this report.

**ZH** 图 1：LICA 样本 [9]。带有结构化组件级标注的设计版式，其层级与丰富元数据远超粗糙的边界框，本报告即在此基础上评测各模型。

**EN** Evaluation subsets. From the full dataset, we construct task-specific evaluation subsets with standardized filtering criteria. Table 1 summarizes the primary evaluation sets. Component-level tasks sample up to three elements per layout to control evaluation cost while maintaining coverage.

**ZH** 评测子集。我们从完整数据集中按标准化筛选标准构造了任务专属的评测子集。表 1 汇总了主要评测集。组件级任务在每个版式中最多采样三个元素，以在保持覆盖面的同时控制评测成本。

**EN** The evaluation sizes reflect the full scope of available annotated data at each level of granularity. Layout-level tasks use all 989 non-video layouts in the dataset; component-level tasks (typography, partial completion) further multiply the effective sample size by sampling up to three elements per layout, yielding ⟦SLOT_0⟧2,500 instances. Generation tasks use smaller evaluation sets (typically 100 samples, filtered for resolution and aspect-ratio compatibility) due to the cost and complexity of multiple inference calls per sample to closed-source generation APIs. Animation tasks are evaluated on all 100 compositions with complete temporal annotations; the 50-sample Lottie subset and the 10-brief video generation set reflect the smaller pool of animated assets with full structural metadata. In all cases, the sample sizes are sufficient to support the conclusions drawn: the inter-model performance gaps reported throughout the paper are typically an order of magnitude larger than the statistical uncertainty at the corresponding sample sizes.

**ZH** 评测规模反映了各粒度层级上可用标注数据的完整范围。版式级任务使用数据集中全部 989 个非视频版式；组件级任务（排版、部分补全）通过在每个版式中最多采样三个元素进一步放大有效样本量，得到 ⟦SLOT_0⟧2,500 个实例。生成任务使用更小的评测集（通常为 100 个样本，并按分辨率与宽高比兼容性筛选），因为对每个样本多次调用闭源生成 API 的成本与复杂度较高。动画任务在全部 100 个具备完整时序标注的合成作品上评测；50 个样本的 Lottie 子集与 10 个简报的视频生成子集，对应的是具备完整结构元数据的动画素材这一更小的池子。在所有情形下，样本量都足以支撑所给出的结论：全文报告的模型间性能差距，通常比相应样本量下的统计不确定性大一个数量级。

**EN** Table 1: Evaluation subsets used across GDB. Component-level tasks sample up to 3 elements per layout.

**ZH** 表 1：GDB 各任务使用的评测子集。组件级任务在每个版式中最多采样 3 个元素。

<!-- [原子块 · table] Task Group Section Samples Key Annotations Used Layout understanding 3 989 layouts Bboxes, z-order, aspect ratio, component types Typography understanding 4 2,568 text elems Font, color, size, weight, -->

**EN** Evaluated tasks. GDB comprises 49 tasks across five domains: layout, typography, SVG & vector, template semantics, and animation, each evaluated under understanding and generation modes (Table 2). These domains were chosen to reflect the core skill axes a professional designer exercises: arranging space, specifying type, working with vector code, interpreting design intent, and reasoning about motion.

**ZH** 受评任务。GDB 包含跨五个领域的 49 个任务：版式、排版、SVG 与矢量、模板语义、动画，每个领域都在理解与生成两种模式下评测（表 2）。选择这些领域是为了对应专业设计师所运用的核心技能轴：安排空间、指定字体、处理矢量代码、解读设计意图，以及对运动进行推理。

**EN** Each domain is evaluated under both understanding and generation settings. Understanding tasks ask whether a model can perceive and reason about an existing design, e.g., identifying fonts, counting components, parsing animation timing, while generation tasks ask whether it can produce or modify design artifacts that satisfy structured constraints. As the two settings may involve different model families (e.g. a vision-language model for understanding vs. a dedicated image-generation model from the same provider), we aim to explore what current AI systems can perceive about a design with what they can actually produce.

**ZH** 每个领域都在理解与生成两种设定下评测。理解任务考察模型能否感知并推理既有的设计，例如识别字体、清点组件、解析动画时序；生成任务则考察它能否产出或修改满足结构化约束的设计产物。由于两种设定可能涉及不同的模型家族（例如用视觉语言模型做理解，而用同一厂商的专用图像生成模型做生成），我们旨在把「当前 AI 系统能从设计中感知到什么」与「它们实际能产出什么」对照起来考察。

**EN** Table 2: GDB organizes its 49 tasks along two orthogonal axes: design domain (layout, typography, SVG & vector, template semantics, and animation) and capability mode (understanding vs. generation). Understanding tasks probe a model’s ability to perceive and reason about existing designs, while generation tasks evaluate whether a model can produce or edit design artifacts that satisfy structured constraints.

**ZH** 表 2：GDB 沿两条正交的轴组织其 49 个任务：设计领域（版式、排版、SVG 与矢量、模板语义、动画）与能力模式（理解 vs. 生成）。理解任务考察模型感知与推理既有设计的能力，生成任务则评测模型能否产出或编辑满足结构化约束的设计产物。

<!-- [原子块 · table] Domain Mode # Description Layout Understanding 8 Spatial reasoning over design canvases: aspect ratio, element counting, component type and detection, layer order, rotation, crop shape, and frame dete -->

**EN** Evaluated models. We evaluate models spanning three frontier model families, covering proprietary API-served systems. These families were selected because they represent the current state of the art across the broadest range of creative tasks, spanning text understanding, image generation, and video synthesis, making them the most natural candidates for assessing design capability in AI systems. Our goal is not simply to rank these models, but to use them as strong baselines to expose where the field as a whole falls short on design-specific tasks. Table 3 summarizes the models, their access methods, and the task groups in which each participates. Not every model is evaluated on every task: some tasks require image-generation capabilities (available only in GPT-Image-1.5, Gemini 3.1 Pro, and Gemini 3.1 Flash Image), while others require structured code output or video understanding. Although we compare model performance, the goal of the paper is to provide a benchmark and insights into current capabilities in this field, rather than highlight specific failure modes of each model.

**ZH** 受评模型。我们评测的模型覆盖三个前沿模型家族，均为通过专有 API 提供服务的系统。选择这些家族，是因为它们代表了当前在最广范围内覆盖创意任务的最高水平，横跨文本理解、图像生成与视频合成，因而成为评估 AI 系统设计能力最自然的候选。我们的目标并非简单地给这些模型排名，而是把它们作为强基线，暴露整个领域在设计专属任务上的短板。表 3 汇总了各模型、其访问方式以及各自参与的任务组。并非每个模型都参与每个任务：部分任务需要图像生成能力（仅 GPT-Image-1.5、Gemini 3.1 Pro 与 Gemini 3.1 Flash Image 具备），另一些则需要结构化代码输出或视频理解能力。尽管我们比较了模型性能，本文的目标是提供一套基准并揭示该领域当前的能力边界，而不是突出每个模型各自的失效模式。

**EN** Decoding and prompting. All models are evaluated with greedy decoding (temperature ⟦SLOT_1⟧) to ensure reproducibility. Each task uses a single fixed prompt template across all models; prompt templates are provided in Appendix B for reproducibility. Where a task defines multiple prompting conditions, such as open-vocabulary versus label-constrained (Sections 6), all models receive the same prompt variant.

**ZH** 解码与提示。所有模型均以贪心解码（temperature ⟦SLOT_1⟧）评测，以保证可复现性。每个任务在所有模型上使用同一个固定的提示模板；提示模板见附录 B。当某任务定义了多种提示条件（如第 6 节的开放词表与标签受限），所有模型都接收相同的提示变体。

**EN** Table 3: Models evaluated in GDB. “Modalities” indicates the input types accepted for the benchmark tasks.

**ZH** 表 3：GDB 中受评的模型。「模态」表示各基准任务所接受的输入类型。

<!-- [原子块 · table] Model Provider / Access Input Modalities Output Modality Gemini-3.1-Pro Google API Text, image, video Text Gemini-3.1-Flash-Image Google API Text, image Image GPT-5.4 OpenAI API Text, image Text GPT-I -->

**EN** Modality conditions. Several tasks are evaluated under multiple input modality conditions to disentangle the contribution of visual and structural signals: text-only (the model receives layout JSON or text metadata), image-only (the model receives rendered PNG), and both (JSON and PNG together). Not all modality conditions are available for every model; missing entries are marked in the per-task results tables. For animation tasks (Section 7), Gemini 3.1 Pro natively accepts video as a first-class input modality and processes the full rendered animation. GPT-5.4 and Claude Opus 4.6 do not support native video ingestion; for these models, we extract uniformly sampled keyframes from each animation and supply them as an ordered sequence of still images.

**ZH** 模态条件。部分任务在多种输入模态条件下评测，以分离视觉信号与结构信号的贡献：仅文本（模型接收版式 JSON 或文本元数据）、仅图像（模型接收渲染好的 PNG）以及两者兼有（JSON 与 PNG 同时给出）。并非所有模型都具备全部模态条件；缺失项在各任务结果表中标注。对于动画任务（第 7 节），Gemini 3.1 Pro 原生支持把视频作为一等输入模态，可处理完整渲染的动画；GPT-5.4 与 Claude Opus 4.6 不支持原生视频输入，对这两个模型，我们从每段动画中均匀采样关键帧，并以有序的静帧序列提供。

**EN** 2.1 Evaluation Metrics

**ZH** 2.1 评测指标

**EN** GDB tasks report metrics drawn from a shared taxonomy. We define all recurring metrics here; task-specific metrics are introduced in their respective sections. Unless otherwise noted, ⟦SLOT_2⟧ denotes higher-is-better and ⟦SLOT_3⟧ denotes lower-is-better.

**ZH** GDB 各任务报告的指标取自一套共享的分类体系。我们在此定义所有反复出现的指标；任务专属的指标在其所属小节中给出。除非另有说明，⟦SLOT_2⟧ 表示越高越好，⟦SLOT_3⟧ 表示越低越好。

**EN** Throughout the paper we assign each task one of three solvability labels. Mostly Solved: best-model performance exceeds 95% (or an equivalent metric-specific threshold), with limited room for improvement at the current evaluation granularity. Partially Solved: best-model performance falls between 80–95%, or the task exhibits a clear split where one sub-condition is tractable while another exposes a fundamental gap (e.g. single- vs. multi-element, coarse vs. fine-grained, open-vocab vs. constrained). Unsolved: best-model performance is below 80%, or the task remains structurally beyond current capabilities, e.g. an orders-of-magnitude gap relative to established baselines in other domains. We set this threshold in consultation with design experts to reflect practical usability, as even small errors (e.g., a few pixels) typically require manual correction.

**ZH** 全文为每个任务赋予三种可解性标签之一。基本解决（Mostly Solved）：最佳模型性能超过 95%（或该指标相应的等价阈值），在当前评测粒度下改进空间有限。部分解决（Partially Solved）：最佳模型性能落在 80～95% 之间，或该任务呈现明显分化——某一子条件可处理，另一子条件却暴露出根本性缺口（例如单元素 vs. 多元素、粗粒度 vs. 细粒度、开放词表 vs. 受限）。未解决（Unsolved）：最佳模型性能低于 80%，或该任务在结构上仍超出当前能力，例如相对其他领域的既有基线存在数量级差距。该阈值是与设计专家商议后设定的，以反映实际可用性——即便是很小的误差（例如几个像素）通常也需要人工修正。

**EN** Spatial accuracy.

**ZH** 空间精度。

**EN** mIoU (mean Intersection over Union) measures average overlap between predicted and ground-truth bounding boxes. bbox F1 is used as a complementary overlap-quality metric. When explicit target boxes are unavailable, we estimate boxes with an LLM-based detector; implementation details and detector selection are provided in Appendix C. mAP@0.5 and mAP@0.5:0.95 follow the COCO detection protocol [10]: mAP@0.5 counts a detection as correct if its IoU with the ground-truth box exceeds 50%; mAP@0.5:0.95 averages across IoU thresholds from 0.5 to 0.95 in steps of 0.05, rewarding tighter localization. MAE (mean absolute error) and MSE (mean squared error) are used for continuous regression targets such as element counts, font sizes, and animation durations.

**ZH** mIoU（平均交并比）度量预测边界框与真值边界框之间的平均重叠。bbox F1 作为互补的重叠质量指标。当缺少显式目标框时，我们用基于 LLM 的检测器估计框；实现细节与检测器选择见附录 C。mAP@0.5 与 mAP@0.5:0.95 遵循 COCO 检测协议 [10]：mAP@0.5 在检测框与真值框的 IoU 超过 50% 时判定为正确；mAP@0.5:0.95 在 0.5 至 0.95 之间以 0.05 为步长对 IoU 阈值取平均，奖励更紧致的定位。MAE（平均绝对误差）与 MSE（均方误差）用于连续回归目标，如元素计数、字号与动画时长。

**EN** Perceptual quality.

**ZH** 感知质量。

**EN** LPIPS [11] ⟦SLOT_4⟧ computes learned perceptual distance between two images using deep features; lower values indicate greater perceptual similarity. SSIM [12] ⟦SLOT_5⟧ measures structural similarity based on luminance, contrast, and structure. DreamSim [13] ⟦SLOT_6⟧ captures higher-level, human-aligned visual similarity beyond low-level pixel statistics. FID (Fréchet Inception Distance) [6] ⟦SLOT_7⟧ measures distributional distance between generated and reference image sets in Inception feature space. MSE (pixel-level) ⟦SLOT_8⟧ is the mean squared pixel error between rendered outputs and references, used primarily in SVG evaluation. PSNR (peak signal-to-noise ratio) ⟦SLOT_9⟧ measures reconstruction fidelity on a logarithmic scale.

**ZH** LPIPS [11] ⟦SLOT_4⟧ 用深度特征计算两幅图像之间的习得感知距离，数值越低表示感知上越相似。SSIM [12] ⟦SLOT_5⟧ 基于亮度、对比度与结构度量结构相似性。DreamSim [13] ⟦SLOT_6⟧ 捕捉超越低层像素统计的、与人类对齐的高层视觉相似性。FID（Fréchet Inception Distance）[6] ⟦SLOT_7⟧ 在 Inception 特征空间中度量生成图像集与参考图像集之间的分布距离。MSE（像素级）⟦SLOT_8⟧ 是渲染输出与参考之间像素误差的均方，主要用于 SVG 评测。PSNR（峰值信噪比）⟦SLOT_9⟧ 在对数尺度上度量重建保真度。

**EN** Semantic alignment.

**ZH** 语义对齐。

**EN** CLIP Score [8] ⟦SLOT_10⟧ computes cosine similarity between a text prompt and a generated image in CLIP embedding space, measuring text-image alignment. PickScore [14] ⟦SLOT_11⟧ is a learned human-preference metric trained on pick-a-pic data, providing a scalar alignment score. BERTScore [15] ⟦SLOT_12⟧ performs soft token-level alignment between generated and reference texts using contextual embeddings (we use the RoBERTa-large variant). Embedding cosine similarity ⟦SLOT_13⟧ computes cosine similarity between mean-pooled last hidden states of generated and reference texts using Llama-3.2-1B.

**ZH** CLIP Score [8] ⟦SLOT_10⟧ 在 CLIP 嵌入空间中计算文本提示与生成图像之间的余弦相似度，度量图文对齐程度。PickScore [14] ⟦SLOT_11⟧ 是在 pick-a-pic 数据上训练的习得人类偏好指标，给出一个标量对齐分数。BERTScore [15] ⟦SLOT_12⟧ 用上下文嵌入在生成文本与参考文本之间做软性的词元级对齐（我们采用 RoBERTa-large 变体）。嵌入余弦相似度 ⟦SLOT_13⟧ 用 Llama-3.2-1B 计算生成文本与参考文本的末层隐状态均值池化之间的余弦相似度。

**EN** Human-aligned preference.

**ZH** 人类对齐的偏好。

**EN** NIMA [16] ⟦SLOT_14⟧ predicts mean opinion scores for aesthetic quality. ImageReward [17] ⟦SLOT_15⟧ is a reward model trained on human preference data for text-to-image generation. HPSv3 [18] (Human Preference Score v3) ⟦SLOT_16⟧ provides a scalar human-preference prediction calibrated on recent generation models.

**ZH** NIMA [16] ⟦SLOT_14⟧ 预测美学质量的平均意见分。ImageReward [17] ⟦SLOT_15⟧ 是在文生图的人类偏好数据上训练的奖励模型。HPSv3 [18]（Human Preference Score v3）⟦SLOT_16⟧ 提供在近期生成模型上校准过的标量人类偏好预测。

**EN** Text fidelity.

**ZH** 文本保真度。

**EN** OCR Accuracy ⟦SLOT_17⟧ measures whether generated text is recognized as the intended target string by an off-the-shelf OCR system. Font Family Accuracy ⟦SLOT_18⟧ and Text Align Accuracy ⟦SLOT_19⟧ are discrete match rates for font-family and alignment predictions. Font Size MAE ⟦SLOT_20⟧ is the mean absolute error on predicted font sizes (in pixels). Color distance is reported as ⟦SLOT_21⟧ (CIEDE2000) ⟦SLOT_22⟧, a perceptually uniform color-difference metric, alongside RGB ⟦SLOT_23⟧ distance and hue-bucket accuracy (8-bucket quantisation). A prediction is considered perceptually acceptable when ⟦SLOT_24⟧. Letter Spacing MAE ⟦SLOT_25⟧ measures error in estimated letter spacing. When generating images or components, text-fidelity metrics rely on a custom Text-Params-Predictor, a lightweight model that recovers typographic parameters from rendered text patches for comparison against ground-truth specifications.

**ZH** OCR Accuracy ⟦SLOT_17⟧ 度量生成的文本是否被现成的 OCR 系统识别为预期目标串。Font Family Accuracy ⟦SLOT_18⟧ 与 Text Align Accuracy ⟦SLOT_19⟧ 分别是字族与对齐预测的离散匹配率。Font Size MAE ⟦SLOT_20⟧ 是预测字号的平均绝对误差（单位为像素）。色距以 ⟦SLOT_21⟧（CIEDE2000）⟦SLOT_22⟧ 报告，这是一种感知均匀的色差度量，同时给出 RGB ⟦SLOT_23⟧ 距离与色相分桶准确率（8 桶量化）。当 ⟦SLOT_24⟧ 时，认为该预测在感知上可接受。Letter Spacing MAE ⟦SLOT_25⟧ 度量字间距估计的误差。在生成图像或组件时，文本保真度指标依赖一个定制的 Text-Params-Predictor——一个从渲染文本图块中恢复字体排印参数、以便与真值规格比对的轻量模型。

**EN** Structural validity.

**ZH** 结构有效性。

**EN** JSON Valid ⟦SLOT_26⟧ is the fraction of model outputs that parse as valid JSON with the expected schema (used in template variant generation). SVG Valid ⟦SLOT_27⟧ is the fraction of generated SVGs that parse and render without error. Compression Ratio ⟦SLOT_28⟧ measures the byte-level ratio between an optimized SVG and the original, with lower values indicating more aggressive size reduction.

**ZH** JSON Valid ⟦SLOT_26⟧ 是能解析为符合预期模式的合法 JSON 的模型输出占比（用于模板变体生成）。SVG Valid ⟦SLOT_27⟧ 是能解析并无错渲染的生成 SVG 占比。Compression Ratio ⟦SLOT_28⟧ 度量优化后 SVG 与原始 SVG 的字节级比值，数值越低表示体积压缩越激进。

**EN** Rank correlation.

**ZH** 秩相关。

**EN** Kendall’s ⟦SLOT_29⟧ ⟦SLOT_30⟧ measures the fraction of correctly ordered element pairs (robust to local perturbations). Spearman’s ⟦SLOT_31⟧ ⟦SLOT_32⟧ is a rank correlation coefficient that penalizes large rank displacements. Both are used for layer-order and ranking tasks, where a score of 0.5 corresponds roughly to random ordering.

**ZH** Kendall’s ⟦SLOT_29⟧ ⟦SLOT_30⟧ 度量正确排序的元素对占比（对局部扰动稳健）。Spearman’s ⟦SLOT_31⟧ ⟦SLOT_32⟧ 是惩罚大幅秩位移的秩相关系数。二者都用于层序与排序任务，其中 0.5 的分数大致对应随机排序。

**EN** Clustering.

**ZH** 聚类。

**EN** ARI (Adjusted Rand Index) ⟦SLOT_33⟧ and AMI (Adjusted Mutual Information) ⟦SLOT_34⟧ are chance-corrected measures of cluster agreement. V-measure ⟦SLOT_35⟧ is the harmonic mean of homogeneity and completeness. FMI (Fowlkes–Mallows Index) ⟦SLOT_36⟧ is the geometric mean of precision and recall at the pair level.

**ZH** ARI（Adjusted Rand Index）⟦SLOT_33⟧ 与 AMI（Adjusted Mutual Information）⟦SLOT_34⟧ 是经机会校正的聚类一致性度量。V-measure ⟦SLOT_35⟧ 是同质性（homogeneity）与完整性（completeness）的调和平均。FMI（Fowlkes–Mallows Index）⟦SLOT_36⟧ 是对层面精确率与召回率的几何平均。

**EN** Set-based.

**ZH** 集合类。

**EN** For multi-label tasks such as aesthetic tag prediction, we report precision, recall, and F1 computed per sample and macro-averaged. We evaluate under two matching criteria: exact matching (string identity after normalization) and fuzzy matching (substring containment with greedy one-to-one assignment).

**ZH** 对美学标签预测等多标签任务，我们报告逐样本计算再做宏平均的精确率、召回率与 F1。我们在两种匹配准则下评测：精确匹配（归一化后的字符串全等）与模糊匹配（子串包含，配合贪心的一对一指派）。

**EN** Judge-based.

**ZH** 裁判类。

**EN** M-Judge[19] ⟦SLOT_37⟧ is an MLLM-based pairwise win-rate metric that compares a model output against the ground-truth layout under the sample-specific intent. The judge selects the better layout based on aesthetics, clarity, usability, creativity, and consistency. In our benchmark, we use M-Judge for layout generation (Section 3), where holistic design quality cannot be fully captured by coordinate- or pixel-level metrics alone. The prompt template is provided in Appendix 65.

**ZH** M-Judge[19] ⟦SLOT_37⟧ 是一种基于 MLLM 的成对胜率指标，在样本专属意图下把模型输出与真值版式做比较。裁判依据美学、清晰度、可用性、创意与一致性选择更好的版式。在本基准中，我们把 M-Judge 用于版式生成（第 3 节）——那里的整体设计质量无法仅由坐标级或像素级指标充分刻画。提示模板见附录 65。

**EN** 3 Composition Tasks

**ZH** 3 构成任务

**EN** 3.1 Layout Understanding

**ZH** 3.1 版式理解

**EN** A layout defines the spatial arrangement of visual components on a canvas, encompassing their positions, dimensions, z-order stacking, and type. It forms the structural backbone of any graphic design, and understanding it is the most fundamental capability a design-aware model must possess. A model that cannot reliably identify how many components a layout contains, what types they are, or how they are stacked cannot be expected to modify or extend that layout coherently. We evaluate eight progressively harder tasks (Table 4) on 989 designs from the LICA dataset (2). The evaluation set spans a realistic distribution of canvas formats — ⟦SLOT_38⟧ (34.8%), ⟦SLOT_39⟧ (26.2%), and ⟦SLOT_40⟧ (20.4%) together cover 80% of layouts, with rarer formats such as ⟦SLOT_41⟧ and ⟦SLOT_42⟧ appearing fewer than 10 times each — and a wide range of layout complexity, with layouts containing on average 15.7 top-level components (median = 12, ⟦SLOT_43⟧ = 14.0). This class imbalance is reflected in the gap between accuracy and macro-F1 reported below. Tasks range from global geometric inference to fine-grained component localization and depth reasoning, and results show that this capability remains largely unsolved by current frontier systems. Figure 2 shows example layouts illustrating the variance in layout properties.

**ZH** 版式定义了画布上各视觉组件的空间安排，涵盖其位置、尺寸、层序堆叠与类型。它构成任何平面设计的结构骨架，理解它是具备设计意识的模型必须具备的最基础能力。一个模型若无法可靠判断某个版式包含多少组件、这些组件属于何种类型、以及它们如何堆叠，就无法指望它能连贯地修改或扩展该版式。我们在 LICA 数据集（第 2 节）的 989 个设计上评测了八个难度递进的任务（表 4）。评测集覆盖符合真实分布的画布格式——⟦SLOT_38⟧（34.8%）、⟦SLOT_39⟧（26.2%）与 ⟦SLOT_40⟧（20.4%）合计覆盖 80% 的版式，⟦SLOT_41⟧ 与 ⟦SLOT_42⟧ 等更罕见的格式各出现不足 10 次——以及范围很广的版式复杂度：版式平均含 15.7 个顶层组件（中位数 = 12，⟦SLOT_43⟧ = 14.0）。这种类别不平衡反映在下文的准确率与宏 F1 的差距上。任务涵盖从全局几何推断到细粒度组件定位与深度推理，结果表明当前前沿系统基本尚未解决这一能力。图 2 给出了说明版式属性差异的示例版式。

**EN** Table 4: Spatial composition understanding task definitions and dataset statistics. All tasks draw from the same 989 layouts. Sample counts and distribution might vary across tasks because component-level tasks apply validity filters (e.g., minimum element size) and per-layout sampling caps.

**ZH** 表 4：空间构成理解任务定义与数据集统计。所有任务取自同一批 989 个版式。各任务的样本数与分布可能不同，因为组件级任务会施加有效性过滤（例如元素最小尺寸）与每版式采样上限。

<!-- [原子块 · table] Task Description N Classes Distribution Metrics Aspect Ratio Classification Predict the canvas aspect ratio from 9 categories. Tests whether the model can infer global geometric proportions from visua -->

**EN** (a) Layouts spanning multiple aspect ratios (e.g. ⟦SLOT_44⟧, ⟦SLOT_45⟧, ⟦SLOT_46⟧, ⟦SLOT_47⟧).

**ZH** (a) 跨越多种宽高比的版式（如 ⟦SLOT_44⟧、⟦SLOT_45⟧、⟦SLOT_46⟧、⟦SLOT_47⟧）。

**EN** (b) A layout containing a rotated image component.

**ZH** (b) 含旋转图像组件的版式。

**EN** (c) An image placed inside a decorative frame with a circular crop.

**ZH** (c) 置于装饰性画框内并做了圆形裁剪的图像。

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

**EN** Figure 2: Example design templates illustrating the variance of layout properties evaluated in this section. The layouts differ in aspect ratio, number and type of components, spatial composition, and visual complexity (a), and may contain rotated image elements (b) or images placed inside decorative frames with non-rectangular crops (c).

**ZH** 图 2：说明本节所评测版式属性差异的示例设计模板。这些版式在宽高比、组件数量与类型、空间构成与视觉复杂度上各不相同（a），并可能包含旋转的图像元素（b），或置于装饰性画框内、做了非矩形裁剪的图像（c）。

**EN** Results.

**ZH** 结果。

**EN** Tables 5 and 6 present the full results and all metrics are defined in Section 2.1. Figures 4 shows qualitative examples. The results reveal four distinct patterns across the spatial composition tasks:

**ZH** 表 5 与表 6 给出完整结果，所有指标定义见第 2.1 节。图 4 给出定性示例。结果在空间构成任务上揭示出四种截然不同的模式：

**EN** • Spatial reasoning is highly uneven across models. Aspect ratio classification (93.9% best accuracy), element counting (MAE = 5.81 best), and component type classification (46.1% best accuracy) show large performance gaps, with models trailing by up to ⟦SLOT_48⟧ on counting tasks.

**ZH** • 各模型的空间推理能力极不均衡。宽高比分类（最佳准确率 93.9%）、元素计数（最佳 MAE = 5.81）与组件类型分类（最佳准确率 46.1%）表现出巨大的性能差距，模型在计数任务上最多落后 ⟦SLOT_48⟧。

**EN** • Component detection remains effectively unsolved. The best model achieves only 6.4% mAP@0.5, orders of magnitude below natural-image benchmarks, indicating a fundamental gap in design-domain spatial grounding across all evaluated systems.

**ZH** • 组件检测实际上仍未解决。最佳模型仅取得 6.4% 的 mAP@0.5，比自然图像基准低若干个数量级，表明所有受评系统在设计域的空间定位上存在根本性缺口。

**EN** • Z-order inference is a distinct capability. Layer order prediction does not correlate with performance on other layout tasks, suggesting that depth and occlusion reasoning requires different visual capabilities than bounding-box prediction.

**ZH** • 层序推断是一项独立的能力。图层顺序预测与其他版式任务的性能不相关，说明深度与遮挡推理所需的视觉能力不同于边界框预测。

**EN** • Visual container reasoning is a separate skill. Crop shape detection and frame detection reveal a capability dimension orthogonal to other spatial tasks, with the best models achieving 76.9% and F1 = 0.504 respectively.

**ZH** • 视觉容器推理是另一项独立技能。裁剪形状检测与画框检测揭示出一个与其他空间任务正交的能力维度，最佳模型分别取得 76.9% 与 F1 = 0.504。

**EN** 3.2 Layout Generation

**ZH** 3.2 版式生成

**EN** Layout generation evaluates whether a model can synthesize or modify a graphic design under structured constraints, rather than only interpret an existing layout. Across the four tasks in this subsection, the model must generate a full design from intent, complete missing components, reinsert masked assets, or adapt a layout to a new canvas ratio. For intent-to-layout generation and layer-aware inpainting, we evaluate on 100 randomly sampled examples after filtering out images with extreme resolutions or aspect ratios.

**ZH** 版式生成评测模型能否在结构化约束下合成或修改平面设计，而不仅是解读既有版式。本小节四个任务中，模型需要依意图生成完整设计、补全缺失组件、重新插入被遮罩的素材，或把版式适配到新的画布比例。对于意图到版式的生成与图层感知补全，我们在滤除分辨率或宽高比极端的图像后，于 100 个随机采样样本上评测。

**EN** For the multi-aspect-ratio adaptation task, we additionally report three human-evaluated binary metrics that capture structural preservation more directly than generic preference models. TextAcc is 1 if the required text is preserved correctly and legibly in the adapted output, and 0 otherwise. Recall is 1 if all core assets from the source layout are retained appropriately after adaptation, and 0 otherwise. Hallucination is 1 if any unsupported text or visual element is introduced by the model, and 0 otherwise. All three metrics are averaged over evaluation samples.

**ZH** 对多宽高比适配任务，我们还额外报告三个人工评测的二元指标，它们比通用偏好模型更直接地刻画结构保持。TextAcc 在必需文本被正确、清晰地保留于适配结果中时取 1，否则取 0。Recall 在适配后源版式的全部核心素材都被妥当保留时取 1，否则取 0。Hallucination 在模型引入任何无依据的文本或视觉元素时取 1，否则取 0。三个指标均在评测样本上取平均。

**EN** Table 5: Layout understanding results. Best result per metric in bold. ⟦SLOT_49⟧ = higher is better; ⟦SLOT_50⟧ = lower is better.

**ZH** 表 5：版式理解结果。每个指标的最优结果以粗体标出。⟦SLOT_49⟧ = 越高越好；⟦SLOT_50⟧ = 越低越好。

<!-- [原子块 · table] Aspect Ratio Elem. Counting Comp. Type Clf. Model Acc ↑ \uparrow F1 ↑ \uparrow MAE ↓ \downarrow MSE ↓ \downarrow Acc ↑ \uparrow F1 ↑ \uparrow Gemini-3.1-Flash-Lite 0.236 0.105 12.50 375.7 0.252 0.224  -->

**EN** Table 6: Image rotation prediction results (⟦SLOT_51⟧ = 2,585). Best result per metric in bold.

**ZH** 表 6：图像旋转预测结果（⟦SLOT_51⟧ = 2,585）。每个指标的最优结果以粗体标出。

<!-- [原子块 · table] Model Rot. Acc ↑ \uparrow Angle MAE ↓ \downarrow Angle MAE rot ↓ \downarrow Gemini-3.1-Flash-Lite 0.716 17.07 74.93 Gemini-3.1-Pro 0.750 16.29 73.48 GPT-5.4 0.800 13.76 69.43 Claude-Opus-4.6 0.766 15. -->

**EN** Table 7: Image crop shape prediction (⟦SLOT_52⟧ = 2,585) and frame detection (⟦SLOT_53⟧ = 1,863) results. Best per metric in bold.

**ZH** 表 7：图像裁剪形状预测（⟦SLOT_52⟧ = 2,585）与画框检测（⟦SLOT_53⟧ = 1,863）结果。每个指标的最优结果以粗体标出。

<!-- [原子块 · table] Image Crop Shape Frame Detection Model is-crop ↑ \uparrow shape ↑ \uparrow shape crop ↑ \uparrow Acc ↑ \uparrow Prec ↑ \uparrow Rec ↑ \uparrow F1 ↑ \uparrow Gemini-3.1-Flash-Lite 0.557 0.531 0.066 0.7 -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

**EN** (a) Aspect Ratio Classification GT: 16:9 GPT-5.4: 2:3

**ZH** (a) 宽高比分类　真值：16:9　GPT-5.4：2:3

**EN** A wide-format banner is misclassified as a portrait ratio. GPT-5.4 confuses the dominant vertical text column for a portrait canvas, ignoring the actual image dimensions.

**ZH** 一张宽幅横幅被误判为纵向比例。GPT-5.4 把占主导的竖向文字栏误认为纵向画布，忽略了图像的实际尺寸。

**EN** (b) Element Counting GT: 5 GPT-5.4: 95

**ZH** (b) 元素计数　真值：5　GPT-5.4：95

**EN** A simple layout with 5 top-level components is predicted to contain 95 elements. The model appears to count individual characters or decorative sub-pixels rather than functional design components.

**ZH** 一个含 5 个顶层组件的简单版式被预测为含 95 个元素。模型似乎在数单个字符或装饰性子像素，而非功能性设计组件。

**EN** (c) Component Detection GT: 22 components (text, image, vector)

**ZH** (c) 组件检测　真值：22 个组件（文本、图像、矢量）

**EN** Gemini Pro: 14 boxes, all labelled “text”

**ZH** Gemini Pro：14 个框，全部标为「文本」

**EN** The model collapses images and vectors into text labels and produces bounding boxes in a rotated coordinate system unrelated to the actual layout.

**ZH** 该模型把图像与矢量都归并到文本标签之下，并在与实际版式无关的旋转坐标系中生成边界框。

**EN** Figure 3: Representative failure cases for layout understanding tasks. Models exhibit systematic errors including ratio confusion (a), order-of-magnitude overcounting (b), and type collapse (c).

**ZH** 图 3：版式理解任务的代表性失效案例。模型表现出系统性错误，包括比例混淆（a）、数量级级别的过度计数（b）与类型塌缩（c）。

**EN** (a) Original layout with correct layer ordering. All components are visible and correctly stacked.

**ZH** (a) 具有正确图层顺序的原始版式。所有组件均可见且堆叠正确。

**EN** (b) Layout re-rendered using the z-order predicted by GPT-5.4.

**ZH** (b) 按 GPT-5.4 预测的层序重新渲染的版式。

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

**EN** Figure 4: Layer order prediction failure case (GPT-5.4). The model predicts an incorrect z-order that buries foreground elements (text and decorative shape) behind the background, illustrating that even small rank errors can render a layout unusable.

**ZH** 图 4：层序预测失效案例（GPT-5.4）。该模型预测了错误的层序，把前景元素（文字与装饰形状）压到背景之下，说明即便很小的排序错误也会让版式变得不可用。

**EN** Table 8: Layout generation task definitions.

**ZH** 表 8：版式生成任务定义。

<!-- [原子块 · table] Task Description Samples Metrics Intent-to-Layout Generation Generate a complete layout image from communicative intent, layout description, style cues, required text, and target aspect ratio. 100 lay -->

**EN** Table 8 lists the tasks used to evaluate this subsection along with their primary settings and metrics.

**ZH** 表 8 列出用于评测本小节的任务及其主要设定与指标。

**EN** Results.

**ZH** 结果。

**EN** Tables 9, 10, 11, and 12 present the full results for the four generation settings, with qualitative examples in Figures 5, 6, and 7. The main takeaways are:

**ZH** 表 9、10、11、12 给出四种生成设定的完整结果，图 5、6、7 给出定性示例。主要结论如下：

**EN** 1. Intent-to-layout generation remains bottlenecked by text fidelity. The two evaluated models are closely matched on alignment and aesthetic metrics, but OCR remains in the 73–75% range, indicating that a substantial fraction of required strings are still rendered incorrectly or illegibly.

**ZH** 1. 意图到版式的生成仍受制于文本保真度。两个受评模型在对齐与美学指标上接近，但 OCR 仍停留在 73～75% 区间，说明仍有相当比例的必需字符串被渲染错误或无法辨识。

**EN** 2. Partial layout completion degrades sharply in the multi-element setting. Single-element completion is comparatively tractable, but jointly reasoning about several missing placements remains a substantially harder compositional problem.

**ZH** 2. 部分版式补全在多元素设定下急剧退化。单元素补全相对可处理，但联合推理若干处缺失位置仍是一个困难得多的组合问题。

**EN** 3. Layer-aware inpainting exposes a trade-off between identity preservation and global harmony. Models that stay closer to the reference asset do not necessarily produce the most coherent final composition, and the gap between image-conditioned and text-conditioned inputs remains relatively modest.

**ZH** 3. 图层感知补全暴露出身份保持与全局协调之间的权衡。更贴近参考素材的模型未必能产出最连贯的最终构成，而图像条件与文本条件输入之间的差距仍相对有限。

**EN** 4. Multi-aspect-ratio adaptation is not well captured by a single scalar metric. GPT-Image-1.5 better preserves text and achieves stronger preference-model scores, while Gemini preserves core assets more reliably and scores better on M-Judge and DreamSim, indicating complementary strengths.

**ZH** 4. 多宽高比适配无法由单一标量指标充分刻画。GPT-Image-1.5 更好地保留文本并取得更强的偏好模型分数，而 Gemini 更可靠地保留核心素材，在 M-Judge 与 DreamSim 上得分更高，显示出互补的优势。

**EN** Table 9: Intent-to-layout generation results. Metrics are grouped by text–image alignment, aesthetic quality, and text accuracy.

**ZH** 表 9：意图到版式的生成结果。指标按图文对齐、美学质量与文本准确率分组。

<!-- [原子块 · table] Alignment Aesthetic Quality Text Model Pick ↑ \uparrow CLIP ↑ \uparrow NIMA ↑ \uparrow ImgRwd ↑ \uparrow HPS ↑ \uparrow OCR ↑ \uparrow Gemini-3.1-Flash-Img 19.81 0.310 5.14 0.250 10.28 0.726 GPT-Image -->

**EN** Table 10: Partial layout completion results for single-element and multiple-element settings. Best result per metric in bold.

**ZH** 表 10：单元素与多元素设定下的部分版式补全结果。每个指标的最优结果以粗体标出。

<!-- [原子块 · table] Setting Model mIoU ↑ \uparrow LPIPS ↓ \downarrow DreamSim ↓ \downarrow M-Judge ↑ \uparrow Single GPT-5.4 0.2299 0.0582 0.0131 0.29 Claude-Opus-4.6 0.1878 0.0677 0.0164 0.26 Gemini-3.1-Pro 0.2413 0.051 -->

<!-- [原子块 · img]  -->

**EN** Figure 5: Partial layout completion visualization. From left to right, we show the composite input image, the multiple target assets with a checkerboard background, and the predictions from three models: Gemini, Opus, and GPT. Both rows illustrate the multiple-placement setting. In the first row, the models fail to account for the cropped nature of the object asset, leading to visually unnatural placements of truncated content, as indicated by the orange arrows. In the second row, the models fail to preserve the shared visual concept of related text elements such as “Jobs” and “About,” placing them too far apart or in the incorrect order, and potentially cropping or misplacing other shapes (GPT-5.4).

**ZH** 图 5：部分版式补全可视化。从左到右依次展示合成输入图像、带棋盘格背景的多个目标素材，以及三个模型（Gemini、Opus、GPT）的预测。两行都演示多元素放置设定。第一行中，模型未能考虑对象素材的裁剪特性，导致被截断的内容摆放得不自然，如橙色箭头所示。第二行中，模型未能保持相关文本元素（如「Jobs」与「About」）的共享视觉概念，把它们摆得过远或顺序错误，并可能裁剪或错放其他形状（GPT-5.4）。

**EN** Table 11: Layer-aware inpainting results for image-conditioned insertion and text-conditioned synthesis. Identity preservation metrics and reconstruction quality are computed on the inserted object crop; ImageReward and HPSv3 are computed on the final composite.

**ZH** 表 11：图像条件插入与文本条件合成下的图层感知补全结果。身份保持指标与重建质量在被插入对象的裁剪区域上计算；ImageReward 与 HPSv3 在最终合成图上计算。

<!-- [原子块 · table] Identity Preservation Reconstruction Design Quality Setting Model CLIP ↑ \uparrow DINOv2 ↑ \uparrow DreamSim ↓ \downarrow LPIPS ↓ \downarrow PSNR ↑ \uparrow SSIM ↑ \uparrow ImgRwd ↑ \uparrow HPS ↑ \up -->

**EN** (a) Image-conditioned

**ZH** (a) 图像条件

<!-- [原子块 · table] Masked Image Asset GT Gemini-3.1 Flash GPT-Image 1.5 -->

**EN** (b) Text-conditioned

**ZH** (b) 文本条件

<!-- [原子块 · table] Description: This image features a flat, minimalist illustration of a chocolate chip cookie on a transparent background. The main subject is a perfectly circular, medium brown cookie base, adorned wit -->

**EN** Figure 6: Layer-aware inpainting. (a) Image-conditioned inpainting uses the original RGBA asset as reference, yet both models fail to preserve it: GPT-Image-1.5 introduces unintended changes to background color and content, while Gemini-3.1-Flash-Image severely distorts the input asset. (b) Text-conditioned inpainting fails to satisfy the instruction, producing incorrect content and altering the surrounding layout. Orange arrows and boxes highlight these failures. Overall, both models fail to preserve background consistency and adhere to input constraints, resulting in incoherent designs.

**ZH** 图 6：图层感知补全。(a) 图像条件补全以原始 RGBA 素材为参考，但两个模型都没能保住它：GPT-Image-1.5 对背景颜色与内容引入了非预期的改动，而 Gemini-3.1-Flash-Image 严重扭曲了输入素材。(b) 文本条件补全未能满足指令，生成了错误内容并改动了周围的版式。橙色箭头与方框标示这些失效。总体而言，两个模型都没能保持背景一致性并遵守输入约束，导致设计不连贯。

<!-- [原子块 · table] Source Layout (9:16) Target Layout (1:1) Gemini-3.1 Flash Image GPT-Image 1.5 -->

**EN** Figure 7: Qualitative results for multi-aspect-ratio adaptation (9:16 ⟦SLOT_54⟧ 1:1). For each example, we show the original source layout, the ground-truth target layout, and the adapted outputs from Gemini-3.1 Flash Image and GPT-Image 1.5. The figure highlights whether each model preserves reading order, core assets, and text content while recomposing the design for a substantially different canvas ratio.

**ZH** 图 7：多宽高比适配（9:16 ⟦SLOT_54⟧ 1:1）的定性结果。每个示例展示原始源版式、真值目标版式，以及 Gemini-3.1 Flash Image 与 GPT-Image 1.5 的适配输出。该图突出显示各模型在为差异很大的画布比例重新构图时，是否保持了阅读顺序、核心素材与文本内容。

**EN** Table 12: Multi-aspect-ratio adaptation results (long-to-short) using direct image generation. Metrics are grouped into human-evaluated structural-preservation measures and automated aesthetic and preference scores. The best result for each metric is shown in bold.

**ZH** 表 12：使用直接图像生成的多宽高比适配（长到短）结果。指标分为人工评测的结构保持度量与自动化的美学与偏好分数。每个指标的最优结果以粗体标出。

<!-- [原子块 · table] Structural Preservation Aesthetic & Preference Model TextAcc ↑ \uparrow Recall ↑ \uparrow Halluc. ↓ \downarrow M-Judge ↑ \uparrow PickScore ↑ \uparrow HPSv3 ↑ \uparrow ImgRwd ↑ \uparrow DreamSim ↓ \do -->

**EN** Table 13: Summary of key findings across layout tasks.

**ZH** 表 13：版式任务的关键发现汇总。

<!-- [原子块 · table] Task Group Key Finding Best Performance Best Model Status Aspect Ratio & Counting Large performance gaps; counting errors are heavy-tailed on complex layouts 93.9% acc, MAE 5.81 GPT-5.4 Partially solv -->

**EN** 4 Typography Tasks

**ZH** 4 排版任务

**EN** 4.1 Typography Understanding

**ZH** 4.1 排版理解

**EN** In graphic design, text is not merely readable content but a visual element that conveys hierarchy, tone, and brand identity through its typographic specification. We evaluate whether models can perceive fine-grained text properties across ten tasks on 2,568 text elements extracted from 989 layouts (Section 2), spanning font identification, color estimation, property prediction, curved-text detection, inline style-span recovery, and rotation estimation. Table 14 lists the task definitions and dataset statistics for this domain. Visual examples of the different typographic properties appear in Figure 8.

**ZH** 在平面设计中，文字并非只是可读的内容，而是一种通过字体排印规格传达层级、调性与品牌识别的视觉元素。我们评测模型能否感知细粒度的文本属性，在取自 989 个版式的 2,568 个文本元素（第 2 节）上考察十项任务，涵盖字体识别、颜色估计、属性预测、曲排文本检测、行内样式区间恢复与旋转估计。表 14 列出该领域的任务定义与数据集统计。不同字体排印属性的视觉示例见图 8。

**EN** Results.

**ZH** 结果。

**EN** Tables 15–18 present the full results. The results reveal five key patterns across the typography understanding tasks:

**ZH** 表 15～18 给出完整结果。结果在排版理解任务上揭示出五种关键模式：

**EN** Table 14: Typography understanding task definitions and dataset statistics. All tasks draw from text components across 989 layouts, sampling up to 3 text elements per layout. For color prediction, 58 examples are excluded due to missing (optional) values.

**ZH** 表 14：排版理解任务定义与数据集统计。所有任务取自 989 个版式中的文本组件，每个版式最多采样 3 个文本元素。颜色预测中，因存在缺失的（可选）值而排除了 58 个样本。

<!-- [原子块 · table] Task Description Samples Classes Metrics Font Family Prediction Identify the font family used for a target text string. Evaluation set contains 167 distinct typefaces with a long-tail distribution ske -->

<!-- [原子块 · img]  -->

**EN** Figure 8: Typography Properties. From left to right: font family, font size, font weight, text color, alignment, line spacing & letter spacing, rotation and style ranges. An example for curved text appears in Figure 9.

**ZH** 图 8：字体排印属性。从左到右依次为：字族、字号、字重、文本颜色、对齐、行距与字间距、旋转与样式区间。曲排文本的示例见图 9。

**EN** Table 15: Font Family and Text Color results. Best result per metric in bold.

**ZH** 表 15：字族与文本颜色结果。每个指标的最优结果以粗体标出。

<!-- [原子块 · table] Font Family Text Color Model Acc ↑ \uparrow F1 ↑ \uparrow Δ \Delta E ↓ \downarrow RGB ℓ 2 \ell_{2} ↓ \downarrow Δ \Delta E < 5 {<}5 ↑ \uparrow HueAcc ↑ \uparrow Gemini-3.1-Flash-Lite 0.065 0.002 52.41 -->

**EN** Table 16: Typographic property results. Best result per metric in bold.

**ZH** 表 16：字体排印属性结果。每个指标的最优结果以粗体标出。

<!-- [原子块 · table] Font Size Weight Align Line Ht. Letter Sp. Model MAE ↓ \downarrow Acc ↑ \uparrow Acc ↑ \uparrow MAE ↓ \downarrow MAE ↓ \downarrow Gemini-3.1-Flash-Lite 38.42 0.390 0.428 43.88 0.045 Gemini-3.1-Pro 35. -->

**EN** Table 17: Curved text detection and text rotation results. Best per metric in bold. “Curv-only” columns restricted to the 26 curved elements.

**ZH** 表 17：曲排文本检测与文本旋转结果。每个指标的最优结果以粗体标出。「仅曲排」列限于 26 个曲排元素。

<!-- [原子块 · table] Curved Text ( n n =2,568) Text Rotation ( n n =2,568) Model Acc ↑ \uparrow MAE ↓ \downarrow Det curv ↑ \uparrow MAE curv ↓ \downarrow Acc ↑ \uparrow MAE ↓ \downarrow MAE rot ↓ \downarrow Gemini-3.1-Fl -->

**EN** Table 18: Style range detection: span IoU and exact match, stratified by number of ground-truth style ranges.

**ZH** 表 18：样式区间检测：区间 IoU 与精确匹配，按真值样式区间数量分层。

<!-- [原子块 · table] All ( n n =2,568) 1-range ( n n =2,549) ≥ \geq 2-range ( n n =19) Model IoU ↑ \uparrow EM ↑ \uparrow IoU ↑ \uparrow EM ↑ \uparrow IoU ↑ \uparrow EM ↑ \uparrow Gemini-3.1-Flash-Lite 0.376 0.000 0.377 0 -->

**EN** • Font recognition is weak across the board. The best model achieves only 23.7% top-1 accuracy (⟦SLOT_55⟧ over the next best), with Macro-F1 an order of magnitude lower, confirming that correct predictions concentrate on high-frequency typefaces while the vast majority of the 167 families score zero F1.

**ZH** • 字体识别整体薄弱。最佳模型的 top-1 准确率仅 23.7%（⟦SLOT_55⟧ 于次优模型），宏 F1 更是低一个数量级，说明正确预测集中在高频字体上，而 167 个字族中的绝大多数 F1 为零。

**EN** • Color perception varies dramatically across models. The best model achieves ⟦SLOT_56⟧E = 5.57 with 63.3% of predictions within the perceptually acceptable ⟦SLOT_57⟧E ⟦SLOT_58⟧ 5 threshold, while the weakest models produce ⟦SLOT_59⟧E ⟦SLOT_60⟧ 52, colors that are perceptually unrelated to the ground truth. Claude occupies an intermediate position (⟦SLOT_61⟧E = 14.05, hue accuracy 69.6%).

**ZH** • 各模型的颜色感知差异极大。最佳模型取得 ⟦SLOT_56⟧E = 5.57，63.3% 的预测落在感知可接受的 ⟦SLOT_57⟧E ⟦SLOT_58⟧ 5 阈值之内；而最弱的模型产生 ⟦SLOT_59⟧E ⟦SLOT_60⟧ 52 的结果，其颜色与真值在感知上毫不相干。Claude 居中（⟦SLOT_61⟧E = 14.05，色相准确率 69.6%）。

**EN** • Typographic property estimation is unevenly solved. Font size and line height show the largest gaps (up to ⟦SLOT_62⟧ difference; GPT-5.4 MAE = 8.97 px vs. Gemini ⟦SLOT_63⟧36 px), while letter spacing is the easiest property for all models (MAE ⟦SLOT_64⟧ 0.045 em). Text alignment is the most consistently predicted property, with the best model reaching 86.1%.

**ZH** • 字体排印属性估计的解决程度参差不齐。字号与行高的差距最大（相差可达 ⟦SLOT_62⟧；GPT-5.4 的 MAE = 8.97 px，而 Gemini 为 ⟦SLOT_63⟧36 px），而字间距是所有模型最容易的属性（MAE ⟦SLOT_64⟧ 0.045 em）。文本对齐是预测最稳定的属性，最佳模型达到 86.1%。

**EN** • Curved text and rotation expose a binary capability gap. The best models correctly identify 88.5–92.3% of the 26 curved elements, while some models score zero, classifying every element as straight. On text rotation, rotated-only MAE ranges from 18.67° to over 54° across models.

**ZH** • 曲排文本与旋转暴露出二值化的能力缺口。最佳模型能正确识别 26 个曲排元素中的 88.5～92.3%，而某些模型得分为零，把每个元素都判为直排。在文本旋转上，仅旋转样本的 MAE 在各模型间从 18.67° 到超过 54° 不等。

**EN** • Style range localization is achievable but exact recovery is not. The best models achieve span IoU of up to 0.982 (vs. ⟦SLOT_65⟧0.376 for Gemini), but exact match is 0% across all models and all stratifications, indicating that while models can localize styled spans, they cannot jointly recover the full typographic specification within those spans. For representative failure cases, see Figure 9.

**ZH** • 样式区间定位可以做到，精确恢复却做不到。最佳模型的区间 IoU 可达 0.982（Gemini 为 ⟦SLOT_65⟧0.376），但在所有模型与所有分层下精确匹配均为 0%，说明模型虽能定位带样式的区间，却无法在这些区间内联合恢复完整的字体排印规格。代表性失效案例见图 9。

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

**EN** (a) Font Family Prediction GT:

**ZH** (a) 字族预测　真值：

**EN** "Message" – Lora

**ZH** 「Message」– Lora

**EN** GPT-5.4:

**ZH** GPT-5.4：

**EN** "Message" – Cormorant Garamond

**ZH** 「Message」– Cormorant Garamond

**EN** Gemini Lite:

**ZH** Gemini Lite：

**EN** "Message" – Montserrat

**ZH** 「Message」– Montserrat

**EN** Gemini Pro:

**ZH** Gemini Pro：

**EN** "Message" – Bebas Neue

**ZH** 「Message」– Bebas Neue

**EN** GPT recognizes the serif style but picks the wrong family. Both Gemini variants predict fonts from entirely different categories.

**ZH** GPT 认出了衬线风格却选错了字族。两个 Gemini 变体则预测了分属完全不同类别的字体。

**EN** (b) Text Color Prediction GT: rgb(1,1,1)

**ZH** (b) 文本颜色预测　真值：rgb(1,1,1)

**EN** GPT-5.4: #FFFFFF

**ZH** GPT-5.4：#FFFFFF

**EN** The model predicts the exact opposite color. Gemini Pro returns empty strings on multiple color queries, while Gemini Lite defaults to #000000 regardless of the actual color.

**ZH** 该模型预测出了完全相反的颜色。Gemini Pro 在多次颜色查询中返回空字符串，而 Gemini Lite 无论实际颜色为何都默认为 #000000。

**EN** (c) Curved Text Detection GT:

**ZH** (c) 曲排文本检测　真值：

**EN** curved, curvature = 55

**ZH** 曲排，曲率 = 55

**EN** Gemini Lite:

**ZH** Gemini Lite：

**EN** straight, curvature = 0

**ZH** 直排，曲率 = 0

**EN** A clearly arced text element is classified as straight. Both Gemini models achieve zero detection rate on all 26 curved elements, predicting straight for every sample.

**ZH** 一个明显呈弧形的文本元素被判为直排。两个 Gemini 模型在全部 26 个曲排元素上的检测率均为零，对每个样本都预测为直排。

**EN** Figure 9: Representative failure cases for typography understanding tasks. Models confuse font categories (a), predict inverted colors (b), and miss curved text entirely (c). See task prompts in Table 53.

**ZH** 图 9：排版理解任务的代表性失效案例。模型混淆字体类别（a）、预测出反转的颜色（b），并完全漏掉曲排文本（c）。任务提示见表 53。

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

**EN** (a) Original layout

**ZH** (a) 原始版式

**EN** (b) Layout re-rendered using predicted font size and text position.

**ZH** (b) 按预测的字号与文本位置重新渲染的版式。

**EN** Figure 10: Text parameter prediction rendering effect. The model (Gemini-3.1-Pro) predicts an incorrect position and size for the text, causing mis-alignments and overlaps. (only font size and text box position were modified in this example).

**ZH** 图 10：文本参数预测的渲染效果。该模型（Gemini-3.1-Pro）预测的文本位置与字号有误，导致错位与重叠（本例仅修改了字号与文本框位置）。

**EN** 4.2 Styled Text Generation

**ZH** 4.2 样式化文本生成

**EN** Styled text generation evaluates a model’s ability to translate structured typographic constraints into visually accurate text rendering. In addition to producing the correct string, the model must faithfully reproduce the full typographic specification, including font family, size, color, alignment, and spacing. We evaluate two settings, with both restricted to 1:1 aspect-ratio samples built from Google open-source fonts to ensure evaluator reliability:

**ZH** 样式化文本生成评测模型把结构化字体排印约束转化为视觉准确文本渲染的能力。除了产出正确的字符串，模型还必须忠实复现完整的字体排印规格，包括字族、字号、颜色、对齐与间距。我们评测两种设定，二者都限于由 Google 开源字体构建的 1:1 宽高比样本，以保证评测器的可靠性：

**EN** • Styled text element generation: the model generates an isolated text patch from a target string and typography specification, without layout context.

**ZH** • 样式化文本元素生成：模型依据目标字符串与字体排印规格生成独立的文本图块，不提供版式上下文。

**EN** • Styled text rendering to layout: the model restores missing text into a masked layout image while preserving all surrounding unmasked pixels, with the masked layout provided as additional input.

**ZH** • 样式化文本渲染到版式：模型把缺失的文本还原进被遮罩的版式图像，同时保留周围所有未被遮罩的像素，被遮罩的版式作为额外输入提供。

**EN** Each model receives the target text content and a structured typography specification (font family, size, color, alignment, spacing); in the layout setting it additionally receives the masked layout image. Table 19 presents the results. The prompt templates used in this task are provided in Appendix B. In the layout setting, the editable text region is provided as a tight polygonal mask computed from the convex hull algorithm.

**ZH** 每个模型接收目标文本内容与结构化的字体排印规格（字族、字号、颜色、对齐、间距）；在版式设定下还额外接收被遮罩的版式图像。表 19 给出结果。该任务所用的提示模板见附录 B。在版式设定下，可编辑文本区域以凸包算法计算出的紧致多边形掩码提供。

**EN** Results.

**ZH** 结果。

**EN** Table 19 reports quantitative results for both element-level generation and layout-level rendering, while Figure 11 illustrates representative failures in the practical layout-editing setting. The central challenge is not simply rendering plausible styled text, but restoring it within the prescribed masked region without altering surrounding content. Across models, this requirement remains unmet: layout-level spatial fidelity is limited, and qualitative examples show that generated text often extends beyond the editable region or modifies nearby design elements. The main observations are as follows:

**ZH** 表 19 报告元素级生成与版式级渲染的定量结果，图 11 则展示实际版式编辑场景下的代表性失效。核心挑战不只是渲染出貌似合理的样式化文本，而是在规定的遮罩区域内还原它，同时不改变周围内容。各模型都未能满足这一要求：版式级的空间保真度有限，定性示例显示生成的文本常常溢出可编辑区域，或改动邻近的设计元素。主要观察如下：

**EN** • Mask-constrained text insertion remains unreliable. In the layout setting, even the best model achieves only IoU = 0.580 and F1 = 0.685, indicating limited agreement with the ground-truth text region. Figure 11 further illustrates that edits frequently overflow outside the input masks and modify the nearby contents. This suggests that current models do not reliably confine text generation to the intended region.

**ZH** • 受掩码约束的文本插入仍不可靠。在版式设定下，即便最佳模型也只取得 IoU = 0.580 与 F1 = 0.685，说明与真值文本区域的一致性有限。图 11 进一步表明，编辑常常溢出输入掩码之外并改动附近内容。这说明当前模型并不能可靠地把文本生成限制在目标区域内。

**EN** • Fine-grained typography recovery remains uneven even in the easier element setting. Gemini-3.1-Flash-Img achieves the best font family accuracy, alignment accuracy, and color MAE in the element setting, indicating stronger adherence to the requested typographic specification than GPT-Image-1.5. Nevertheless, font family accuracy remains low overall, indicating that faithful recovery of detailed typographic attributes remains unsolved.

**ZH** • 即便在更简单的元素设定下，细粒度字体排印的恢复仍参差不齐。Gemini-3.1-Flash-Img 在元素设定下取得最佳的字族准确率、对齐准确率与颜色 MAE，说明它比 GPT-Image-1.5 更贴合所要求的字体排印规格。不过字族准确率整体仍然偏低，表明对细粒度字体排印属性的忠实恢复仍未解决。

**EN** Table 19: Styled text generation results. Each model is evaluated on element-level generation (element) and layout-level rendering (layout). Font and Align denote accuracy; Size and Color denote MAE. IoU/F1, LPIPS, and SSIM are reported only for the layout task, where a full rendered target with spatial reference is available. Best result per metric and task in bold.

**ZH** 表 19：样式化文本生成结果。每个模型都在元素级生成（element）与版式级渲染（layout）上评测。Font 与 Align 表示准确率；Size 与 Color 表示 MAE。IoU/F1、LPIPS 与 SSIM 仅针对版式任务报告，因为该任务有带空间参照的完整渲染目标。每个指标与任务的最优结果以粗体标出。

<!-- [原子块 · table] Spatial Accuracy Font Style Fidelity Render Model Task IoU ↑ \uparrow F1 ↑ \uparrow Font ↑ \uparrow Align ↑ \uparrow Size ↓ \downarrow Color ↓ \downarrow LPIPS ↓ \downarrow SSIM ↑ \uparrow GPT-Image-1 -->

<!-- [原子块 · table] Text Prompt Masked Input GT Gemini-3.1 Flash Image GPT-Image 1.5 Instruction: Restore missing text Target text: “Setting SMART goals for personal and professional growth Creating action plans to achie -->

**EN** Figure 11: Layout-level styled text generation failures. Each example shows the target text and typography specification, the masked input layout, the ground-truth render, and outputs from Gemini-3.1 Flash Image and GPT-Image 1.5. Both models generate plausible text, but often fail to respect the intended text region: the restored content can extend beyond the masked area or deviate substantially from the prescribed extent. In the first example, both models overshoot the target region when reconstructing a multi-line paragraph; in the second, both render a readable headline, yet neither matches the intended placement and size within the editable area. These examples show that the main bottleneck is not merely rendering stylized text, but confining the edit to the prescribed mask while preserving surrounding content. GT bbox is shown in green, and the predicted text bbox is shown in red.

**ZH** 图 11：版式级样式化文本生成失效。每个示例展示目标文本与字体排印规格、被遮罩的输入版式、真值渲染结果，以及 Gemini-3.1 Flash Image 与 GPT-Image 1.5 的输出。两个模型都生成了看似合理的文本，却常常无法遵守预期的文本区域：还原出的内容可能超出遮罩区域，或与规定的范围大幅偏离。第一个例子中，两个模型在重建多段文字时都超出了目标区域；第二个例子中，两者都渲染出可读的标题，却都没有落在可编辑区域内预期的位置与尺寸上。这些例子表明，主要瓶颈不只是渲染风格化文本，而是把编辑限制在规定掩码之内并保留周围内容。真值边界框以绿色显示，预测的文本边界框以红色显示。

**EN** 4.3 Text Removal & Background Regeneration

**ZH** 4.3 文本移除与背景重建

**EN** Text removal evaluates whether a model can support practical design editing by erasing typography without leaving ghosting artefacts and faithfully reconstructing the hidden background structure so that the canvas remains reusable for subsequent editing. This capability is essential for template adaptation, multilingual translation, and iterative copy revision [4, 2, 3, 20, 21, 9, 5]. Each model receives a source design image together with a binary mask indicating the text regions (white = editable, black = preserved) and a unified instruction to remove all text and reconstruct the background naturally. We evaluate on 100 randomly sampled templates from the LICA dataset (Section 2), filtered to exclude low-resolution images (max side ⟦SLOT_66⟧ 1,024 px) and extreme aspect ratios (⟦SLOT_67⟧ 2.0). Since each model supports a different set of aspect ratios, inputs are resized to model-compatible resolutions before generation and resized back to the original dimensions for evaluation. Table 20 presents the results.

**ZH** 文本移除评测模型能否支持实际的设计编辑：擦除文字而不留下残影，并忠实重建被遮蔽的背景结构，使画布仍可复用于后续编辑。该能力对模板适配、多语言翻译与文案的迭代修订至关重要 [4, 2, 3, 20, 21, 9, 5]。每个模型接收一张源设计图像，以及指示文本区域的二值掩码（白色 = 可编辑，黑色 = 保留）和一条统一的指令：移除所有文字并自然地重建背景。我们在 LICA 数据集（第 2 节）随机采样的 100 个模板上评测，并滤除低分辨率图像（最长边 ⟦SLOT_66⟧ 1,024 px）与极端宽高比（⟦SLOT_67⟧ 2.0）。由于各模型支持的宽高比集合不同，输入在生成前被缩放到模型兼容的分辨率，评测时再缩放回原始尺寸。表 20 给出结果。

**EN** Results.

**ZH** 结果。

**EN** The results reveal two key patterns across the text removal task:

**ZH** 结果在文本移除任务上揭示出两种关键模式：

**EN** • Text erasure is effectively solved, but background reconstruction is not. Both models achieve high text removal rates (⟦SLOT_68⟧ 94%), confirming that the text itself is effectively erased. However, they diverge sharply on reconstruction fidelity, with PSNR ranging from 16.64 to 30.22 (⟦SLOT_69⟧13.6 dB difference) and SSIM from 0.743 to 0.944, indicating that faithfully reconstructing the occluded background remains a significant challenge.

**ZH** • 文本擦除已基本解决，背景重建则不然。两个模型都取得了很高的文本移除率（⟦SLOT_68⟧ 94%），证实文字本身被有效擦除。但它们在重建保真度上分歧明显：PSNR 从 16.64 到 30.22 不等（相差 ⟦SLOT_69⟧13.6 dB），SSIM 从 0.743 到 0.944，说明忠实重建被遮挡的背景仍是一项重大挑战。

**EN** • Higher removal rate does not imply better reconstruction. The model with a marginally higher raw removal rate (95.3% vs. 94.5%) produces substantially worse background reconstruction (LPIPS = 0.331 vs. 0.088; FID = 115.75 vs. 54.05), suggesting it over-generates or hallucinates content in the masked regions rather than faithfully reconstructing what was occluded.

**ZH** • 更高的移除率并不意味着更好的重建。原始移除率略高的那个模型（95.3% vs. 94.5%），其背景重建却明显更差（LPIPS = 0.331 vs. 0.088；FID = 115.75 vs. 54.05），说明它在遮罩区域内过度生成或产生了幻觉内容，而非忠实重建被遮挡的部分。

**EN** Table 20: Text removal and background regeneration results. Best result per metric in bold.

**ZH** 表 20：文本移除与背景重建结果。每个指标的最优结果以粗体标出。

<!-- [原子块 · table] Text Removal Perceptual Quality Reconstruction Model Remove FID ↓ \downarrow LPIPS ↓ \downarrow CLIP ↑ \uparrow DINO ↑ \uparrow PSNR ↑ \uparrow SSIM ↑ \uparrow Gemini-3.1-Flash-Img 0.945 54.05 0.088 0 -->

**EN** Input Image

**ZH** 输入图像

**EN** Input Mask

**ZH** 输入掩码

**EN** Gemini-3.1 Flash Image

**ZH** Gemini-3.1 Flash Image

**EN** GPT-Image 1.5

**ZH** GPT-Image 1.5

**EN** (a)

**ZH** (a)

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

**EN** (b)

**ZH** (b)

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

**EN** (c)

**ZH** (c)

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

**EN** Figure 12: Text erasing across aspect ratios. Given an input image and a text mask, the models shall remove the masked text and inpaint the removed regions. Both models fail to confine edits to the masked region: GPT-Image 1.5 alters background color and tone, while both models further modify non-target elements (e.g., removing or recoloring the box in (b)). These results show that design-aware erasing requires strict preservation of surrounding structure and style. Orange marks structural changes; blue marks unintended color shifts.

**ZH** 图 12：跨宽高比的文字擦除。给定输入图像与文本掩码，模型应当移除被遮罩的文字并补全被移除的区域。两个模型都没能把编辑限制在遮罩区域内：GPT-Image 1.5 改变了背景颜色与色调，而两个模型还进一步修改了非目标元素（例如在 (b) 中移除或重新着色了方框）。这些结果表明，具备设计意识的擦除要求严格保留周围的结构与风格。橙色标示结构改动，蓝色标示非预期的颜色偏移。

**EN** Table 21: Summary of key findings across typography tasks.

**ZH** 表 21：排版任务的关键发现汇总。

<!-- [原子块 · table] Task Group Key Finding Best Performance Best Model Status Font Recognition Weak across the board; correct predictions concentrate on high-frequency typefaces while the vast majority of 167 families sc -->

**EN** 5 Infographics Tasks

**ZH** 5 信息图任务

**EN** 5.1 SVG Understanding & Editing

**ZH** 5.1 SVG 理解与编辑

**EN** SVG is the native format for vector design assets such as icons, illustrations, decorative strokes, and background frames. Understanding and manipulating SVG code is distinct from raster-image reasoning, since it requires parsing structured markup, reasoning about geometric primitives, and producing syntactically valid code. We evaluate five tasks on 300 SVG assets from the LICA dataset (Section 2), each annotated with a complexity label (easy, medium, hard) based on structural features following the stratification approach of SVGenius [22].

**ZH** SVG 是矢量设计素材（如图标、插画、装饰描边与背景边框）的原生格式。理解与操作 SVG 代码不同于位图推理，因为它需要解析结构化标记、对几何图元进行推理，并产出语法合法的代码。我们在 LICA 数据集（第 2 节）的 300 个 SVG 素材上评测五项任务，每个素材依据结构特征按 SVGenius [22] 的分层方法标注了复杂度标签（简单、中等、困难）。

**EN** All tasks use code-only input with no rendered images, and span two capability modes: understanding and editing. Understanding tasks are perceptual and semantic multiple-choice Q&As generated by Claude Code agent (Opus-4.6) from the rendered SVG image, with four options and a verified answer. Editing tasks includes bug fixing, code optimization, and style editing, which are programmatically annotated and require the model to parse and reason about an existing SVG before perform the editing; since modifying SVG code presupposes understanding it, we treat editing as an extension of comprehension rather than generation. Bug fixing uses easy (⟦SLOT_70⟧5 errors), medium (⟦SLOT_71⟧7 with misspelled attributes), and hard (⟦SLOT_72⟧7 with path-data corruption) variants; code optimization is evaluated against ground truth generated by SVGO v4 (reference compression ratio 62.6%); and style editing applies 1–3 combined operations from a predefined vocabulary of fill, stroke, opacity, viewBox, transform, and color inversion commands. Table 22 summarizes the five understanding and editing tasks. Complexity labels are assigned by a rule-based scorer over structural features (path count, element depth, attribute diversity).

**ZH** 所有任务都采用纯代码输入、不提供渲染图像，并涵盖两种能力模式：理解与编辑。理解任务是感知与语义类的多项选择问答，由 Claude Code 智能体（Opus-4.6）依据渲染后的 SVG 图像生成，含四个选项与一个经过核实的答案。编辑任务包括缺陷修复、代码优化与样式编辑，均以程序化方式标注，要求模型先解析并推理既有 SVG 再执行编辑；由于修改 SVG 代码以理解为前提，我们把编辑视为理解能力的延伸而非生成。缺陷修复分为简单（⟦SLOT_70⟧5 处错误）、中等（⟦SLOT_71⟧7 处，含属性拼写错误）与困难（⟦SLOT_72⟧7 处，含路径数据损坏）三种变体；代码优化以 SVGO v4 生成的真值为参照（参考压缩率 62.6%）；样式编辑则从事先定义的 fill、stroke、opacity、viewBox、transform 与颜色反转命令词表中施加 1～3 个组合操作。表 22 汇总了这五项理解与编辑任务。复杂度标签由基于规则的打分器依据结构特征（路径数量、元素深度、属性多样性）给出。

**EN** Table 22: SVG understanding and editing task definitions. All tasks share the same 300 source SVGs; editing tasks generate multiple difficulty variants per SVG.

**ZH** 表 22：SVG 理解与编辑任务定义。所有任务共用同一批 300 个源 SVG；编辑任务为每个 SVG 生成多个难度变体。

<!-- [原子块 · table] Task Description Samples Metrics Perceptual Q&A Given SVG source code only (no rendered image), answer a multiple-choice question (A–D) about visual properties: dominant color, shape count, element pr -->

**EN** Results.

**ZH** 结果。

**EN** Table 23 presents the results with all metrics defined in Section 2.1. The results reveal three key patterns across the SVG understanding and editing tasks:

**ZH** 表 23 给出结果，所有指标定义见第 2.1 节。结果在 SVG 理解与编辑任务上揭示出三种关键模式：

**EN** • Perceptual reasoning about SVG code is harder than semantic interpretation. The gap between perceptual Q&A (87.0% best) and semantic Q&A (93.7% best) confirms empirically that inferring visual properties directly from SVG markup is harder than understanding what an SVG depicts.

**ZH** • 对 SVG 代码的感知推理比语义解释更难。感知问答（最佳 87.0%）与语义问答（最佳 93.7%）之间的差距从经验上证实：直接从 SVG 标记推断视觉属性，比理解一段 SVG 画的是什么更难。

**EN** • Understanding and editing strengths are complementary across models. The best model achieves repair similarity of 0.932 and leads on style editing (EditD = 0.183), while the other leads on semantic Q&A (93.7%) and code optimization (CompR = 0.870), suggesting that SVG tasks draw on different underlying capabilities: structured-code proficiency aids repair and editing, while perceptual grounding aids semantic interpretation and compression.

**ZH** • 各模型在理解与编辑上的优势互补。最佳模型取得 0.932 的修复相似度并在样式编辑上领先（EditD = 0.183），而另一个模型在语义问答（93.7%）与代码优化（CompR = 0.870）上领先，说明 SVG 任务依赖不同的底层能力：结构化代码的熟练度有助于修复与编辑，而感知基础有助于语义解释与压缩。

**EN** • Multi-operation geometric transforms remain challenging for all models. Failure cases on style editing reveal that combined rotation and scaling commands produce incorrect angles, positions, and displaced content across both models, indicating that composing multiple geometric operations in SVG space is largely unsolved. For representative failure cases, see Figure 13.

**ZH** • 多操作的几何变换对所有模型仍然困难。样式编辑的失效案例显示，组合的旋转与缩放命令会产生错误的角度、位置与错位的内容，两个模型皆是如此，说明在 SVG 空间中组合多个几何操作基本尚未解决。代表性失效案例见图 13。

**EN** Table 23: SVG understanding and editing results (code-only input). Best result per metric in bold. RepSim = repair similarity (⟦SLOT_73⟧); CompR = compression ratio (⟦SLOT_74⟧); EditD = edit distance (⟦SLOT_75⟧). Gemini-3.1† selects the best-performing Gemini-3.1 variant per task (Pro or Flash-Lite; see Appendix).

**ZH** 表 23：SVG 理解与编辑结果（纯代码输入）。每个指标的最优结果以粗体标出。RepSim = 修复相似度（⟦SLOT_73⟧）；CompR = 压缩率（⟦SLOT_74⟧）；EditD = 编辑距离（⟦SLOT_75⟧）。Gemini-3.1† 表示按任务选取表现最好的 Gemini-3.1 变体（Pro 或 Flash-Lite；见附录）。

<!-- [原子块 · table] Understanding Editing Model Perceptual Q&A Acc ↑ \uparrow Semantic Q&A Acc ↑ \uparrow Bug Fixing RepSim ↑ \uparrow Code Optim. CompR ↓ \downarrow Style Edit EditD ↓ \downarrow GPT-5.4 0.847 0.937 0.79 -->

<!-- [原子块 · img]  -->

**EN** Figure 13: SVG editing failures. Bug Fix (rows 1–2): GPT-5.4 corrupts the circle into a fan shape while Gemini repairs it correctly (row 1), yet GPT-5.4 succeeds where Gemini produces invalid output (row 2). Style Edit (row 3): both models produce incorrect scale or displaced content on the multi-step geometric transform.

**ZH** 图 13：SVG 编辑失效。缺陷修复（第 1～2 行）：GPT-5.4 把圆形破坏成扇形而 Gemini 修复正确（第 1 行），但在第 2 行中 GPT-5.4 成功而 Gemini 输出了非法结果。样式编辑（第 3 行）：两个模型在多步几何变换上都产生了错误的缩放或错位的内容。

**EN** 5.2 Infographics Generation

**ZH** 5.2 信息图生成

**EN** Generating valid SVG from a text description, reference image, or both is a code-generation task with visual considerations: the model shall produce syntactically correct vector markup whose rendering matches a target graphic. We evaluate three tasks on 300 SVG assets from the LICA dataset (Section 2), distinguished by input modality: Text-to-SVG (description only), Image-to-SVG (rendered PNG only), and Text+Image-to-SVG (both). Generated SVGs are rendered at ⟦SLOT_76⟧ pixels for evaluation. To further investigate SVG generation across different element types, we curated 50 additional samples for each of the following categories: chart (charts and data visualizations), stroke (decorative strokes and borders), and container (frames and backgrounds).

**ZH** 从文本描述、参考图像或两者兼有地生成合法 SVG，是一项带有视觉考量的代码生成任务：模型应产出语法正确的矢量标记，且其渲染结果与目标图形相符。我们在 LICA 数据集（第 2 节）的 300 个 SVG 素材上评测三项任务，按输入模态区分：文生 SVG（仅描述）、图生 SVG（仅渲染 PNG）与文本+图像生 SVG（两者兼有）。生成的 SVG 以 ⟦SLOT_76⟧ 像素渲染后评测。为进一步考察不同元素类型上的 SVG 生成，我们为以下类别各额外整理了 50 个样本：chart（图表与数据可视化）、stroke（装饰描边与边框）与 container（画框与背景）。

**EN** We additionally evaluate generation of Lottie animations using a curated subset of 50 animations (⟦SLOT_77⟧10 layers, ⟦SLOT_78⟧50 KB, mean duration 4.4 s), extending vector generation to the temporal domain. Generated Lottie files are rendered using the official LottieFiles player to ensure evaluation reflects real-world playback fidelity. Table 24 summarizes the five generation tasks.

**ZH** 我们还额外评测了 Lottie 动画的生成，使用一个精心整理的 50 个动画子集（⟦SLOT_77⟧10 个图层，⟦SLOT_78⟧50 KB，平均时长 4.4 s），把矢量生成扩展到时间域。生成的 Lottie 文件使用官方 LottieFiles 播放器渲染，以确保评测反映真实播放的保真度。表 24 汇总了这五项生成任务。

**EN** Table 24: SVG and Lottie generation task definitions. All SVG tasks share the same 300 assets; Lottie tasks use a curated 50-animation subset.

**ZH** 表 24：SVG 与 Lottie 生成任务定义。所有 SVG 任务共用同一批 300 个素材；Lottie 任务使用一个精心整理的 50 个动画的子集。

<!-- [原子块 · table] Task Description Samples Metrics Text-to-SVG Generate SVG code from a natural-language description only. Tests semantic-to-code translation without visual reference. 300 Valid, SSIM, LPIPS, MSE, Compl -->

**EN** Results.

**ZH** 结果。

**EN** For qualitative examples, see Figures 14, 15, and 16.

**ZH** 定性示例见图 14、15、16。

**EN** The results across static SVG and Lottie generation reveal three key patterns:

**ZH** 静态 SVG 与 Lottie 生成的结果揭示出三种关键模式：

**EN** • SVG generation quality is strongly modality-dependent. Image conditioning dramatically improves fidelity: the best model achieves 0.918 SSIM on image-to-SVG versus 0.733 on text-only (Table 25). GPT-5.4 and Claude-Opus-4.6 achieves near perfect validity (successful render) across all modalities, while Gemini-3.1’s validity drops to 81% (image-only)/84% (text+image) on image-conditioned tasks as output truncation becomes more frequent on complex SVGs.

**ZH** • SVG 生成质量强烈依赖输入模态。图像条件显著提升了保真度：最佳模型在图生 SVG 上取得 0.918 的 SSIM，而纯文本输入下为 0.733（表 25）。GPT-5.4 与 Claude-Opus-4.6 在所有模态下都达到近乎完美的有效性（成功渲染），而 Gemini-3.1 在图像条件任务上的有效性降至 81%（纯图像）／84%（文本+图像），因为在复杂 SVG 上输出截断更为频繁。

**EN** • Lottie animation generation is feasible but far from solved. Even the best result (FrameSSIM = 0.598) is far below static SVG performance (Table 27). Multimodal input provides large gains for GPT-5.4 but degrades Gemini’s output quality, dropping its validity from 100% to 66%.

**ZH** • Lottie 动画生成可行但远未解决。即便最佳结果（FrameSSIM = 0.598）也远低于静态 SVG 的表现（表 27）。多模态输入给 GPT-5.4 带来大幅提升，却降低了 Gemini 的输出质量，使其有效性从 100% 跌至 66%。

**EN** Table 25: SVG generation results across input modalities. Best result per metric in bold. Cmplx = weighted complexity. Gemini-3.1† selects the best-performing Gemini-3.1 variant per task.

**ZH** 表 25：跨输入模态的 SVG 生成结果。每个指标的最优结果以粗体标出。Cmplx = 加权复杂度。Gemini-3.1† 表示按任务选取表现最好的 Gemini-3.1 变体。

<!-- [原子块 · table] Input Model Valid ↑ \uparrow SSIM ↑ \uparrow LPIPS ↓ \downarrow MSE ↓ \downarrow Cmplx Text Claude-Opus-4.6 0.970 0.724 0.450 0.118 27.4 GPT-5.4 1.000 0.733 0.498 0.058 25.3 Gemini-3.1 † 0.977 0.723 0 -->

**EN** Table 26: SVG generation results stratified by SVG type (50 samples each). Best result per metric within each input modality in bold.

**ZH** 表 26：按 SVG 类型分层的 SVG 生成结果（每类 50 个样本）。每种输入模态下每个指标的最优结果以粗体标出。

<!-- [原子块 · table] Input SVG Type Model Valid ↑ \uparrow SSIM ↑ \uparrow LPIPS ↓ \downarrow MSE ↓ \downarrow Text chart Claude-Opus-4.6 0.98 0.687 0.526 0.084 GPT-5.4 1.00 0.757 0.551 0.078 Gemini-3.1 1.00 0.733 0.555 0 -->

**EN** Table 27: Lottie animation generation results (50 samples each). Best result per metric in bold. FrameSSIM and FrameMSE are averaged over five rendered keyframes. StructSim measures layer, type and dimension similarity.

**ZH** 表 27：Lottie 动画生成结果（每组 50 个样本）。每个指标的最优结果以粗体标出。FrameSSIM 与 FrameMSE 在五个渲染关键帧上取平均。StructSim 度量图层、类型与尺寸上的相似性。

<!-- [原子块 · table] Input Model Valid ↑ \uparrow FrameSSIM ↑ \uparrow FrameMSE ↓ \downarrow StructSim ↑ \uparrow Length Text Claude-Opus-4.6 0.600 0.324 0.596 0.372 12,443 GPT-5.4 0.980 0.242 0.666 0.612 4,933 Gemini-3.1 -->

<!-- [原子块 · img]  -->

**EN** Figure 14: SVG generation examples. From left to right: the text prompt, ground truth, and six model outputs for text-to-SVG and image-to-SVG from GPT-5.4, Gemini-3.1 and Claude-Opus-4.6. All models fail to follow the instruction of a black background in the text-to-SVG generation, and introduce artifacts in the image-to-SVG task.

**ZH** 图 14：SVG 生成示例。从左到右依次为：文本提示、真值，以及 GPT-5.4、Gemini-3.1 与 Claude-Opus-4.6 在文生 SVG 与图生 SVG 上的六个模型输出。在文生 SVG 生成中，所有模型都未能遵循黑色背景的指令；在图生 SVG 任务中则引入了伪影。

<!-- [原子块 · img]  -->

**EN** Figure 15: Qualitative image-to-SVG examples across SVG types. For the Chart element, GPT-5.4 achieves the closest reproduction (SSIM 0.90), whereas Gemini omits the central hole and labels (0.83) and Claude modifies the endpoints gap and labels (0.78). GPT-5.4 accurately reconstructs the stroke, while Claude-Opus-4.6 exaggerates its width and Gemini-3.1 reduces it. All model produce incorrect gradient values for the container type.

**ZH** 图 15：跨 SVG 类型的图生 SVG 定性示例。对 Chart 元素，GPT-5.4 的复现最接近（SSIM 0.90），而 Gemini 遗漏了中心的孔与标签（0.83），Claude 修改了端点间距与标签（0.78）。GPT-5.4 准确重建了描边，Claude-Opus-4.6 夸大了其宽度，Gemini-3.1 则收窄了它。所有模型在 container 类型上都产生了错误的渐变值。

<!-- [原子块 · img]  -->

**EN** Figure 16: Lottie generation failure (animated CTA click cursor). Top: ground-truth keyframes showing a pointing hand with animated blue sparks. Middle: GPT-5.4 produces a static, distorted hand with no spark layer and no animation. Bottom: Claude-Opus-4.6 miss the hand completely, and produce a moving cursor instead to represent the click animation instead. Gemini-3.1’s visual is excluded since output is invalid. All models fail to reproduce the multi-layer animated structure.

**ZH** 图 16：Lottie 生成失效（动画 CTA 点击光标）。上：真值关键帧，显示一只带蓝色火花动画的指向手势。中：GPT-5.4 生成了一只静态、变形的手，没有火花图层也没有动画。下：Claude-Opus-4.6 完全漏掉了手，改为生成一个移动的游标来表示点击动画。Gemini-3.1 的视觉结果因输出非法而未收录。所有模型都未能复现多层动画结构。

**EN** Table 28: Summary of key findings across SVG & vector tasks.

**ZH** 表 28：SVG 与矢量任务的关键发现汇总。

<!-- [原子块 · table] Task Group Key Finding Best Performance Best Model Status Perceptual Q&A Semantic questions are easier than perceptual ones across all models, suggesting that inferring what an SVG depicts from code i -->

**EN** 6 Template & Design Semantics

**ZH** 6 模板与设计语义

**EN** This section evaluates models on higher-level design semantics: classifying templates by purpose, predicting designer intent, and understanding and generating template variants. Table 29 lists the task definitions and dataset statistics for this domain.

**ZH** 本节在更高层的设计语义上评测模型：按用途对模板分类、预测设计师意图，以及理解与生成模板变体。表 29 列出该领域的任务定义与数据集统计。

**EN** Table 29: Template & design semantics task definitions and dataset statistics.

**ZH** 表 29：模板与设计语义任务定义与数据集统计。

<!-- [原子块 · table] Task Description Samples Classes Metrics Category Classification Predict the parent category and sub-category of a design template from a rendered image. Tested under open-vocabulary and label-constra -->

**EN** 6.1 Semantics Understanding: Category Classification

**ZH** 6.1 语义理解：类别分类

**EN** Category classification predicts the intended use of a visual design template from a rendered image alone. Each template is annotated with a two-level hierarchy: a parent category, denoting a broad template type (e.g. “business card”, “Instagram post”) and a sub-category describing the visual aesthetic or theme (e.g. “professional”, “skincare”). We test under open-vocabulary and label-constrained prompting (see Appendix Table 59).

**ZH** 类别分类要求仅凭渲染图像预测一个视觉设计模板的预期用途。每个模板标注了两级层级：父类表示宽泛的模板类型（如「名片」「Instagram 帖子」），子类描述视觉美学或主题（如「专业」「护肤」）。我们在开放词表与标签受限两种提示下测试（见附录表 59）。

**EN** Results.

**ZH** 结果。

**EN** Table 30 presents the results for both prompting strategies with all metrics defined in Section 2.1. Figure 17 illustrates the confusion matrices of the best performing model on label-constrained prompting.

**ZH** 表 30 给出两种提示策略的结果，所有指标定义见第 2.1 节。图 17 展示表现最佳模型在标签受限提示下的混淆矩阵。

<!-- [原子块 · img]  -->

**EN** (a) Open-vocabulary prompting

**ZH** (a) 开放词表提示

<!-- [原子块 · img]  -->

**EN** (b) Constrained prompting

**ZH** (b) 受限提示

**EN** Figure 17: Confusion matrices for top-10 highest recurring parent category classification on Claude Opus 4.6 (best overall model). (a) Under open-vocabulary prompting, nearly all predictions fall into the “other” bin, illustrating pervasive label aliasing. (b) Providing the closed label set recovers strong diagonal structure; well-delineated categories such as planner & calendar (.98) and resume (.94) are near-perfectly recognized, while visually overlapping categories such as education (.31) and social media (.40) remain challenging.

**ZH** 图 17：Claude Opus 4.6（整体最佳模型）在出现频次最高的前 10 个父类分类上的混淆矩阵。(a) 在开放词表提示下，几乎所有预测都落入「其他」这一格，说明标签别名现象普遍存在。(b) 提供封闭标签集后恢复了强对角结构；界定清晰的类别如 planner & calendar（.98）与 resume（.94）近乎被完美识别，而视觉上相互重叠的类别如 education（.31）与 social media（.40）仍然困难。

**EN** The results reveal three key patterns:

**ZH** 结果揭示出三种关键模式：

**EN** • Label constraining yields +30–62 pp gains on parent accuracy. Under open-vocabulary prompting, models frequently produce semantically reasonable but lexically mismatched labels (e.g. “social media graphic" instead of “Instagram post"), which are scored as incorrect. In practice, this also exposes a usability challenge: a user has no clear way to anticipate which label variants the model will recognize versus treat as mismatches, making effective prompting non-trivial. Providing the closed label set recovers strong diagonal structure in the confusion matrix (Figure 17b), with well-delineated categories.

**ZH** • 标签受限带来 +30～62 个百分点的父类准确率增益。在开放词表提示下，模型频繁产出语义合理但词典上不匹配的标签（例如用「social media graphic」而非「Instagram post」），这些被判为错误。实践中这也暴露出一个可用性难题：用户无法预判模型会识别哪些标签变体、又会把哪些视作不匹配，使得有效提示并不容易写。提供封闭标签集后，混淆矩阵恢复了强对角结构（图 17b），类别界定清晰。

**EN** • Model rankings shift between prompting conditions. Gemini 3.1 leads open-vocabulary (45.5%), suggesting stronger internalized design vocabulary, while Claude Opus leads label-constrained (78.7% Top-1). GPT 5.4’s open-vocabulary deficit is primarily a naming problem (91.0% Top-5 under constraining).

**ZH** • 模型排名在不同提示条件下会发生变化。Gemini 3.1 在开放词表下领先（45.5%），说明其内部化的设计词表更强；而 Claude Opus 在标签受限下领先（78.7% Top-1）。GPT 5.4 在开放词表下的劣势主要是命名问题（受限下 Top-5 达 91.0%）。

**EN** • Sub-category classification remains an open challenge, with the best Top-1 reaching only 10.13% even under label-constrained prompting.

**ZH** • 子类分类仍是开放难题，即便在标签受限提示下，最佳 Top-1 也只到 10.13%。

**EN** Table 30: Parent (⟦SLOT_79⟧) and sub-category (⟦SLOT_80⟧) classification accuracy and macro-F1 across prompting conditions. Claude Opus 4.6 leads label-constrained prompting, while Gemini 3.1 leads open-vocabulary prompting suggesting a stronger internalized design vocabulary.

**ZH** 表 30：父类（⟦SLOT_79⟧）与子类（⟦SLOT_80⟧）在各提示条件下的分类准确率与宏 F1。Claude Opus 4.6 在标签受限提示下领先，而 Gemini 3.1 在开放词表提示下领先，说明后者内部化的设计词表更强。

<!-- [原子块 · table] Model Prompt Parent Category Sub-Category Top-1 Acc. Top-5 Acc. Macro-F1 Top-1 Acc. Top-5 Acc. Macro-F1 Gemini-3.1 open-vocab. 45.50 64.00 0.339 03.72 19.58 0.049 label-const. 76.23 91.50 0.474 10.13  -->

**EN** 6.2 Semantics Understanding: User Intent Prediction

**ZH** 6.2 语义理解：用户意图预测

**EN** User intent prediction is a free-text generation task: given only a rendered image, the model shall describe the purpose, audience, and desired outcome that motivated the design. We evaluate on 989 templates, each paired with a human-authored single-sentence intent description, and report BERTScore (F1) and Llama embedding cosine similarity (Section 2.1).

**ZH** 用户意图预测是一项自由文本生成任务：仅给定一张渲染图像，模型应描述催生该设计的目的、受众与期望效果。我们在 989 个模板上评测，每个模板配一句人工撰写的意图描述，并报告 BERTScore（F1）与 Llama 嵌入余弦相似度（第 2.1 节）。

**EN** Table 31: Semantic similarity between model-generated and human-annotated user intents for design templates.22footnotemark: 2

**ZH** 表 31：模型生成的用户意图与人工标注的用户意图之间的语义相似度。22footnotemark: 2

<!-- [原子块 · table] Model BERTScore (F1) ↑ \uparrow Llama Cosine Similarity ↑ \uparrow Gemini-3.1-Flash-Lite 89.55 92.71 GPT-5.4 89.03 91.40 Opus-4.6 88.46 92.29 -->

**EN** Results.

**ZH** 结果。

**EN** Table 31 presents the results.

**ZH** 表 31 给出结果。

**EN** • All models converge within ⟦SLOT_81⟧1 pp (BERTScore 88.5–89.6, cosine similarity 91.4–92.7), suggesting that single-sentence intent prediction is near ceiling at this annotation granularity.

**ZH** • 所有模型的差距收敛在 ⟦SLOT_81⟧1 个百分点之内（BERTScore 88.5～89.6，余弦相似度 91.4～92.7），说明在这一标注粒度上，单句意图预测已接近上限。

**EN** • High scores reflect semantic overlap, not exact alignment: BERTScore and cosine similarity reward topical proximity, so a prediction that captures the right domain (e.g. “food promotion”) scores well even if it misidentifies the specific goal (e.g. “brand awareness” vs. “limited-time offer”).

**ZH** • 高分反映的是语义重叠而非精确对齐：BERTScore 与余弦相似度奖励话题接近度，因此一条抓住了正确领域（如「食品促销」）的预测即便误判了具体目标（如「品牌认知」与「限时优惠」之别）也能得高分。

**EN** • Intent is inherently underdetermined from a single image: multiple plausible intents can explain the same design, which compresses the score distribution and makes it difficult to distinguish genuinely superior reasoning from surface-level pattern matching.

**ZH** • 意图本身由单张图像无法唯一确定：多种合理的意图都能解释同一个设计，这压缩了分数分布，难以区分真正的优越推理与表层的模式匹配。

**EN** • Richer intent specifications: multi-sentence descriptions decomposing audience, platform, and emotional response would likely be needed to reveal meaningful differentiation.

**ZH** • 需要更丰富的意图规格：把受众、平台与情绪反应分解开来的多句描述，才可能揭示出有意义的差异。

**EN** 6.3 Template Variant Understanding

**ZH** 6.3 模板变体理解

**EN** Template variant understanding evaluates whether models can recognize that multiple designs originate from the same underlying template despite differing content. We define three progressively harder tasks: pairwise matching, ranking, and clustering, on sibling layouts from the dataset. Figure 18 illustrates the task structure.

**ZH** 模板变体理解评测模型能否识别出多个设计源自同一底层模板，即便内容不同。我们在数据集的同源版式上定义了三项难度递进的任务：成对匹配、排序与聚类。图 18 说明了任务结构。

<!-- [原子块 · img]  -->

**EN** Figure 18: Template variant understanding tasks, see Appendix B for the exact input prompts. All tasks receive rendered layout screenshots and a text prompt. Pairwise Matching: binary classification of template identity. Ranking: rank 20 candidates by similarity to a reference. Clustering: partition ⟦SLOT_82⟧ layouts into template-identity groups.

**ZH** 图 18：模板变体理解任务，精确的输入提示见附录 B。所有任务都接收渲染好的版式截图与一条文本提示。成对匹配：模板身份的二分类。排序：按与参照的相似度对 20 个候选排序。聚类：把 ⟦SLOT_82⟧ 个版式划分为按模板身份分组的簇。

**EN** Results.

**ZH** 结果。

**EN** Table 32 presents LLM and non-LLM baseline results (CLIP, DINOv2, LPIPS, color EMD, font Jaccard, and structural features) across all three tasks. Figure 19 illustrates failure modes across all three tasks: models confuse shared design language with content similarity in matching, rank by surface appearance rather than structural identity in ranking, and either merge visually similar clusters or violate cardinality constraints in clustering.

**ZH** 表 32 给出 LLM 与非 LLM 基线（CLIP、DINOv2、LPIPS、颜色 EMD、字体 Jaccard 与结构特征）在三项任务上的结果。图 19 说明三项任务各自的失效模式：模型在匹配中把共享的设计语言与内容相似性混为一谈，在排序中按表层外观而非结构身份排序，在聚类中要么合并视觉相似的簇，要么违反基数约束。

**EN** Table 32: Template variant understanding results (all metrics in %), across pairwise Matching (⟦SLOT_83⟧ pairs), ranking (⟦SLOT_84⟧ queries), and clustering (⟦SLOT_85⟧ problems, 914 layouts; ARI and AMI are chance-corrected). Best per metric in bold. Gemini-3.1†: best-performing variant per task.

**ZH** 表 32：模板变体理解结果（所有指标以 % 计），涵盖成对匹配（⟦SLOT_83⟧ 对）、排序（⟦SLOT_84⟧ 个查询）与聚类（⟦SLOT_85⟧ 个问题，914 个版式；ARI 与 AMI 经机会校正）。每个指标的最优结果以粗体标出。Gemini-3.1†：按任务选取表现最好的变体。

<!-- [原子块 · table] Matching Ranking Clustering Model / Baseline Acc ↑ \uparrow F1 ↑ \uparrow AUC ↑ \uparrow MRR ↑ \uparrow MAP ↑ \uparrow nDCG@10 ↑ \uparrow Rec@10 ↑ \uparrow ARI ↑ \uparrow AMI ↑ \uparrow V-m. ↑ \uparro -->

<!-- [原子块 · img]  -->

**EN** Figure 19: Template variant understanding failure cases. Pairwise matching: both models misclassify a same-template pair as “different” (distinct photos) and a different-template pair as “same” (shared warm palette). Ranking: GPT-5.4 identifies the correct mosaic-grid sibling despite different content; Gemini-3.1 ranks by surface content and places the sibling 20th. Clustering: colored tags show ground-truth membership. GPT-5.4 merges A+C (similar pink palettes); Gemini-3.1 separates them but violates the ⟦SLOT_86⟧ constraint, producing 4 clusters by splitting B on background color.

**ZH** 图 19：模板变体理解失效案例。成对匹配：两个模型都把同一模板的一对误判为「不同」（照片不同），又把不同模板的一对误判为「相同」（共享暖色调）。排序：GPT-5.4 找出了正确的马赛克网格同源版式（尽管内容不同）；Gemini-3.1 按表层内容排序，把同源版式排在第 20 位。聚类：彩色标签表示真值归属。GPT-5.4 把 A+C 合并（粉色调相近）；Gemini-3.1 把它们分开，却违反了 ⟦SLOT_86⟧ 约束，因按背景色拆分 B 而得到 4 个簇。

**EN** • Font Jaccard baseline matches or exceeds both LLMs on all three tasks (97.7% matching, 96.3% MRR, 92.8% ARI), indicating that font-family metadata captures most of the template identity signal in this corpus — yet LLMs, despite having access to both image and text inputs, fail to leverage this signal, suggesting they do not reliably attend to typographic consistency as a grouping cue.

**ZH** • 字体 Jaccard 基线在三项任务上都与两个 LLM 持平或更优（匹配 97.7%、MRR 96.3%、ARI 92.8%），说明字族元数据在本语料中捕获了大部分模板身份信号——然而 LLM 尽管同时拥有图像与文本输入，却未能利用这一信号，说明它们并不能可靠地把字体一致性当作分组线索来关注。

**EN** • Matching and clustering are dissociated from ranking: a model can achieve near-perfect ranking (MRR 99.4%) while failing at binary match decisions (62.6% accuracy), suggesting these sub-tasks probe fundamentally different similarity reasoning abilities.

**ZH** • 匹配与聚类同排序相分离：一个模型可以取得近乎完美的排序（MRR 99.4%），却在二值匹配判断上失败（准确率 62.6%），说明这些子任务考察的是根本不同的相似性推理能力。

**EN** • Binary match decisions are subject to strong prediction bias: one model predicts “different” for 874 of 1,000 pairs (precision 1.0, recall 0.25), revealing that pairwise classification collapses under conservative decision thresholds even when relative ordering is well-calibrated.

**ZH** • 二值匹配判断存在强烈的预测偏置：某模型对 1,000 对中的 874 对预测「不同」（精确率 1.0，召回率 0.25），说明即便相对排序校准良好，成对分类在保守的决策阈值下也会崩塌。

**EN** 6.4 Template Variant Generation

**ZH** 6.4 模板变体生成

**EN** The generation tasks evaluate whether models can produce design layouts that adhere to template conventions. We consider two output modalities. In structural generation, the model receives reference layout JSON file(s) and their rendered image(s) from LICA (Section 2) and shall generate a complete layout specification in JSON format, enabling explicit control over components and attributes. In image generation, the model instead receives rendered reference image(s) and directly produces a rasterized layout. Metrics span three tiers: JSON-level validity and adherence (Tier 1), aesthetic quality (Tier 2), and rendered-image similarity (Tier 3). Figure 20 illustrates the two structural-mode tasks across these modalities.

**ZH** 生成任务评测模型能否产出遵循模板惯例的设计版式。我们考虑两种输出模态。在结构化生成中，模型接收来自 LICA（第 2 节）的参考版式 JSON 文件及其渲染图像，并应生成 JSON 格式的完整版式规格，从而可对组件与属性做显式控制。在图像生成中，模型改为接收渲染好的参考图像，直接产出一个栅格化版式。指标分三层：JSON 层面的有效性与遵循度（第一层）、美学质量（第二层）与渲染图像相似度（第三层）。图 20 说明了这两种模态下的两项结构化模式任务。

**EN** Results.

**ZH** 结果。

**EN** Tables 33–36 present results. Figure 21 shows qualitative examples.

**ZH** 表 33～36 给出结果。图 21 给出定性示例。

**EN** • Validity is the primary differentiator. GPT-5.4 achieves at least 94% JSON validity across all tasks; Gemini-3.1-Pro achieves at most 83%, limiting the sample on which its style metrics are computed.

**ZH** • 有效性是首要区分因素。GPT-5.4 在所有任务上都达到至少 94% 的 JSON 有效性；Gemini-3.1-Pro 最高只到 83%，限制了其风格指标的计算样本。

**EN** • Pixel-level metrics are insufficient for transformation tasks. Figure 22 shows a style completion example where both structural generation predictions receive low SSIM (0.367 and 0.322) despite remaining stylistically plausible, indicating that image similarity metrics can penalize palette role swaps and do not capture style consistency;

**ZH** • 像素级指标不足以衡量变换类任务。图 22 展示了一个样式补全的例子：两个结构化生成的预测虽然风格上仍然合理，SSIM 却都很低（0.367 与 0.322），说明图像相似度指标会惩罚调色板角色的互换，并不能刻画风格一致性；

**EN** Table 33: Style Completion (⟦SLOT_87⟧). Font: per-component font-family match. color: per-component color match. FS: font-size MAE (px, ⟦SLOT_88⟧). Op.: opacity MAE (⟦SLOT_89⟧). BG: background ⟦SLOT_90⟧ (⟦SLOT_91⟧).

**ZH** 表 33：样式补全（⟦SLOT_87⟧）。Font：逐组件的字族匹配。color：逐组件的颜色匹配。FS：字号 MAE（px，⟦SLOT_88⟧）。Op.：不透明度 MAE（⟦SLOT_89⟧）。BG：背景 ⟦SLOT_90⟧（⟦SLOT_91⟧）。

<!-- [原子块 · table] Model Valid ↑ \uparrow Font ↑ \uparrow color ↑ \uparrow FS ↓ \downarrow Op. ↓ \downarrow BG ↓ \downarrow GPT-5.4 0.943 0.961 0.771 1.83 0.010 10.56 Gemini-3.1-Pro 0.550 0.968 0.782 2.47 0.023 8.42 -->

**EN** Table 34: Recoloring (⟦SLOT_92⟧). Pos.: position fidelity. Area: area fidelity. Pal.: palette adherence (⟦SLOT_93⟧). Cov.: palette coverage. BG: background ⟦SLOT_94⟧ (⟦SLOT_95⟧).

**ZH** 表 34：重新配色（⟦SLOT_92⟧）。Pos.：位置保真度。Area：面积保真度。Pal.：调色板遵循度（⟦SLOT_93⟧）。Cov.：调色板覆盖率。BG：背景 ⟦SLOT_94⟧（⟦SLOT_95⟧）。

<!-- [原子块 · table] Model Valid ↑ \uparrow Pos. ↑ \uparrow Area ↑ \uparrow Pal. ↑ \uparrow Cov. ↑ \uparrow BG ↓ \downarrow GPT-5.4 0.965 1.000 1.000 0.946 0.776 14.48 Gemini-3.1-Pro 0.635 1.000 1.00 0.929 0.690 17.76 -->

<!-- [原子块 · img]  -->

**EN** Figure 20: Template variant generation tasks, and see Appendix B for the exact input prompts. In structural generation, the model receives reference layout JSON file(s) and their rendered image(s) and shall generate a complete layout specification in JSON format. In image generation, the model receives rendered reference image(s) and directly produces a rasterized layout. Style Completion: infer style properties from styled siblings from the same template. Recoloring: recolor to match a target palette from a different template family (shown as color swatches).

**ZH** 图 20：模板变体生成任务，精确的输入提示见附录 B。在结构化生成中，模型接收参考版式 JSON 文件及其渲染图像，并应生成 JSON 格式的完整版式规格。在图像生成中，模型接收渲染好的参考图像，直接产出一个栅格化版式。样式补全：从同一模板的已样式化同源版式中推断样式属性。重新配色：重新着色以匹配来自另一模板族的目标调色板（以色卡形式给出）。

**EN** Table 35: Tier 2 aesthetic metrics (text+image input). All values in ⟦SLOT_96⟧.

**ZH** 表 35：第二层美学指标（文本+图像输入）。所有数值以 ⟦SLOT_96⟧ 计。

<!-- [原子块 · table] Model Task Harmony ↑ \uparrow Contrast ↑ \uparrow Hierarchy ↑ \uparrow GPT-5.4 Style Completion 0.888 0.703 1.000 Recoloring 0.904 0.573 1.000 Gemini-3.1-Pro Style Completion 0.848 0.768 1.000 Recolor -->

**EN** Table 36: Tier 3 image-level metrics. For Style Completion, reference is the ground-truth styled layout. For Recoloring, reference is the source layout before transformation (structural preservation). Structural: model outputs JSON, rendered for comparison. Image: model directly generates a rasterized layout image.⟦SLOT_97⟧: valid, renderable predictions.

**ZH** 表 36：第三层图像级指标。对样式补全，参照是真值的样式化版式。对重新配色，参照是变换前的源版式（结构保持）。结构化：模型输出 JSON，再渲染后比较。图像：模型直接生成栅格化版式图像。⟦SLOT_97⟧：有效、可渲染的预测。

<!-- [原子块 · table] Model Task N N SSIM ↑ \uparrow PSNR ↑ \uparrow LPIPS ↓ \downarrow Style Completion (ref. = ground-truth styled layout) Structural generation GPT-5.4 132 0.796 16.64 0.238 Gemini-3.1-Pro 77 0.810 17.98 -->

<!-- [原子块 · img]  -->

**EN** Figure 21: Template generation failure cases, and see Appendix B for the exact input prompts. Style Completion: GPT-5.4 fails to infer the proper text box size, while Gemini-3.1-Pro fails to generate valid JSON file;both image generation models fail to be text or content faithful. Recoloring: All models fail to correctly assign the colors based on the palette, which shows that models lack the understanding of color palette in design. The size differences reflect fixed output resolutions of image generation APIs.

**ZH** 图 21：模板生成失效案例，精确的输入提示见附录 B。样式补全：GPT-5.4 未能推断出合适的文本框尺寸，而 Gemini-3.1-Pro 未能生成合法的 JSON 文件；两个图像生成模型都做不到文本或内容上的保真。重新配色：所有模型都没能依据调色板正确分配颜色，说明模型缺乏对设计中调色板的理解。尺寸差异反映图像生成 API 的固定输出分辨率。

<!-- [原子块 · img]  -->

**EN** Figure 22: Failure of image similarity metrics to reflect stylistic validity. See Appendix B for the exact input prompts. In this style completion example, both structural generation predictions are visually coherent and preserve the sibling style language, but they assign a different palette from the reference. Although the outputs are style consistent, pixel-level similarity remains low (SSIM 0.367 and 0.322) in contrast to image generation results where GPT-Image-1.5 (0.529) preserves the content but generates inconsistent style and Gemini-3.1-Flash-Image (0.456) hallucinates the content, showing that image metrics can undervalue stylistically plausible alternatives. See Appendix B for the exact input prompts.

**ZH** 图 22：图像相似度指标无法反映风格有效性。精确的输入提示见附录 B。在这个样式补全的例子中，两个结构化生成的预测在视觉上都连贯，并保持了同源版式的风格语言，却分配了与参照不同的调色板。尽管输出在风格上一致，像素级相似度仍然很低（SSIM 0.367 与 0.322）；相比之下，图像生成的结果中 GPT-Image-1.5（0.529）保留了内容却生成了不一致的风格，Gemini-3.1-Flash-Image（0.456）则产生了内容幻觉，这说明图像指标会低估风格上合理的备选方案。精确的输入提示见附录 B。

**EN** Table 37: Summary of key findings across template & design semantics tasks.

**ZH** 表 37：模板与设计语义任务的关键发现汇总。

<!-- [原子块 · table] Task Key Finding Best Performance Best Model Status Category Classification Label constraining yields +30–62 pp gains; open-vocab difficulty is mostly label aliasing, not perceptual failure 78.7% Top- -->

**EN** 7 Animation & Temporal Tasks

**ZH** 7 动画与时序任务

**EN** This section evaluates models on animation understanding and generation tasks: temporal ordering, motion classification, property extraction, and animated video synthesis. Table 38 lists the task definitions and dataset statistics for this domain. All understanding tasks draw from 100 animated compositions. Gemini receives the full video as input; GPT and Claude receive uniformly sampled keyframe sequences.

**ZH** 本节在动画理解与生成任务上评测模型：时序排序、运动分类、属性提取与动画视频合成。表 38 列出该领域的任务定义与数据集统计。所有理解任务取自 100 个动画合成作品。Gemini 接收完整视频作为输入；GPT 与 Claude 接收均匀采样的关键帧序列。

**EN** Table 38: Animation & temporal task definitions and dataset statistics.

**ZH** 表 38：动画与时序任务定义与数据集统计。

<!-- [原子块 · table] Task Description Samples Classes Metrics Keyframe Ordering Recover the chronological sequence of four shuffled keyframes from an animated composition. 100 Permutation of 4 keyframes Exact Match, Kenda -->

**EN** 7.1 Temporal Understanding: Keyframe Ordering

**ZH** 7.1 时序理解：关键帧排序

**EN** Keyframe ordering evaluates temporal reasoning over design animations: given four shuffled keyframes from each of 100 videos, the model must recover the correct chronological sequence. Understanding temporal order is fundamental to animation comprehension, a model that cannot infer narrative or motion progression from visual snapshots cannot be a reliable collaborator in animated design workflows. We report exact match, Kendall’s ⟦SLOT_98⟧, pairwise accuracy, and first-frame accuracy (random baseline: 4.2%, 0.0, 50.0%, 25.0%).

**ZH** 关键帧排序考察对设计动画的时序推理：给定每段视频的四个被打乱的关键帧（共 100 段视频），模型必须还原正确的时间顺序。理解时序是动画理解的基础——一个无法从视觉快照中推断叙事或运动推进的模型，不可能成为动画设计工作流中可靠的协作者。我们报告精确匹配、Kendall’s ⟦SLOT_98⟧、成对准确率与首帧准确率（随机基线：4.2%、0.0、50.0%、25.0%）。

**EN** Results.

**ZH** 结果。

**EN** Table 39 presents the results.

**ZH** 表 39 给出结果。

**EN** Table 39: Keyframe ordering: models are given four shuffled keyframes from each of 100 animated compositions and must predict the correct chronological sequence.

**ZH** 表 39：关键帧排序：模型拿到每段动画合成作品的四个被打乱的关键帧（共 100 段），必须预测正确的时间顺序。

<!-- [原子块 · table] Model Exact Match ↑ \uparrow Kendall’s τ \tau ↑ \uparrow Pairwise Acc. ↑ \uparrow First-Frame Acc. ↑ \uparrow Random baseline 4.2% 0.000 50.0% 25.0% Gemini-3.1-Pro 14.00 17.66 58.83 67.00 GPT-5.4 16.0 -->

**EN** • All models beat the random baseline but remain weak: exact match ranges from 14–16%, with pairwise accuracy only ⟦SLOT_99⟧10 pp above chance (58.8–61.2%), indicating this as an unsolved task.

**ZH** • 所有模型都超过随机基线但仍然很弱：精确匹配在 14～16% 之间，成对准确率仅比随机高 ⟦SLOT_99⟧10 个百分点（58.8～61.2%），说明该任务尚未解决。

**EN** • First-frame identification is substantially easier than full ordering (67–80% vs. 14–16% exact match), suggesting models detect the initial state but struggle with fine-grained temporal progression.

**ZH** • 首帧识别比完整排序容易得多（67～80% vs. 14～16% 精确匹配），说明模型能检测到初始状态，却在细粒度的时序推进上力有不逮。

**EN** 7.2 Animation Understanding: Motion Type Classification

**ZH** 7.2 动画理解：运动类型分类

**EN** Motion type classification evaluates whether models can identify the entrance animation effect from 32 canonical types, e.g. rise, fade, pop, tumble) applied to individual elements in 100 LICA animated compositions (Section 2). Compositions contain 1–20 animated elements; we test under open-vocabulary and label-constrained prompting. Gemini receives full video; GPT and Claude receive keyframe sequences. See Figure 23 as an example for top motion types in the LICA dataset.

**ZH** 运动类型分类评测模型能否从 32 种规范类型（如 rise、fade、pop、tumble）中识别出施加于 100 个 LICA 动画合成作品（第 2 节）中单个元素上的入场动画效果。合成作品含 1～20 个动画元素；我们在开放词表与标签受限两种提示下测试。Gemini 接收完整视频；GPT 与 Claude 接收关键帧序列。LICA 数据集中主要运动类型的示例见图 23。

<!-- [原子块 · img]  -->

**EN** Figure 23: Example motion types. A full list of the 32 motion types are given in the Appendix Table 63).

**ZH** 图 23：运动类型示例。32 种运动类型的完整列表见附录表 63）。

**EN** Results.

**ZH** 结果。

**EN** Table 40 presents the results. We omit qualitative examples for this task as model outputs are too inaccurate to yield meaningful visual analysis. Key findings show:

**ZH** 表 40 给出结果。我们省略该任务的定性示例，因为模型输出过于不准确，无法产生有意义的视觉分析。关键发现如下：

**EN** • Motion type classification is largely unsolved: all models achieve below 13% accuracy, with most scoring 0% on single-component scenes.

**ZH** • 运动类型分类基本未解决：所有模型的准确率都低于 13%，多数在单组件场景上得 0%。

**EN** • Single-component accuracy is near-zero: five of six model/prompt combinations score 0% on single-component scenes (the exception being Claude constrained at 13.3%). Because these scenes contain only a single animated element and require no decomposition, scene segmentation alone cannot explain the failure. This points to a more fundamental inability to map perceived motion patterns. This is likely because UI motion-graphics primitives (e.g. tumble, pop, stomp) are underrepresented in pretraining data relative to natural-video motion, leaving models without a reliable basis for distinguishing them.

**ZH** • 单组件准确率接近于零：六种模型／提示组合中有五种在单组件场景上得 0%（唯一的例外是 Claude 在受限提示下的 13.3%）。由于这些场景只含一个动画元素、不需要分解，仅凭场景分割无法解释这一失败。这指向一种更根本的缺陷：无法把感知到的运动模式映射出来。原因可能是 UI 动效图元（如 tumble、pop、stomp）在预训练数据中的代表性远低于自然视频运动，使模型缺乏区分它们的可靠依据。

**EN** • Constrained prompting does not reliably help: providing the 32-label vocabulary improves Claude marginally on single-component scenes but degrades Gemini substantially, suggesting that models are not close to solving the task and simply guessing differently when the label set is supplied.

**ZH** • 受限提示并不能稳定地提供帮助：提供 32 个标签的词表后，Claude 在单组件场景上略有改善，Gemini 却大幅退化，说明模型远未解决该任务，在给定标签集时只是换了一种猜测方式。

**EN** Table 40: Motion type classification on each animated element. Results are stratified by scene complexity: Single (1 animated element) vs. Multi (⟦SLOT_100⟧2). Gemini receives the full animation video; GPT and Claude receive uniformly sampled keyframes.

**ZH** 表 40：各动画元素上的运动类型分类。结果按场景复杂度分层：单元素（1 个动画元素）vs. 多元素（⟦SLOT_100⟧2）。Gemini 接收完整动画视频；GPT 与 Claude 接收均匀采样的关键帧。

<!-- [原子块 · table] Model Input Prompt Acc. (All) ↑ \uparrow Acc. (Single) ↑ \uparrow Acc. (Multi) ↑ \uparrow Count MAE ↓ \downarrow Gemini-3.1 Video open 7.12 0.00 8.37 3.60 constrained 3.00 0.00 3.52 5.79 GPT-5.4 Keyfr -->

**EN** 7.3 Animation Understanding: Animation Property Extraction

**ZH** 7.3 动画理解：动画属性提取

**EN** Animation property extraction evaluates a model’s ability to perceive and quantify temporal characteristics of animated design compositions across three sub-tasks of increasing difficulty on 100 LICA compositions (Section 2): video-level duration prediction, component-level duration prediction, and component-level start-time prediction. Here, a component refers to an individual design element in the layout (e.g., text/image) that is animated independently. The latter two tasks therefore require identifying and tracking each element over time (implicit scene decomposition) as well as fine-grained temporal estimation. The latter two require implicit scene segmentation and fine-grained temporal estimation. Gemini receives full video; GPT and Claude receive keyframe sequences.

**ZH** 动画属性提取评测模型感知并量化动画设计合成作品时序特征的能力，在 100 个 LICA 合成作品（第 2 节）上涵盖三项难度递增的子任务：视频级时长预测、组件级时长预测与组件级起始时间预测。这里的组件指版式中被独立施加动画的单个设计元素（如文本／图像）。后两项任务因此需要在时间上识别并跟踪每个元素（隐式的场景分解），并做细粒度的时序估计。后两项需要隐式的场景分割与细粒度的时序估计。Gemini 接收完整视频；GPT 与 Claude 接收关键帧序列。

**EN** Results.

**ZH** 结果。

**EN** Tables 41 and 42 present the full results, stratified by scene complexity (single-component vs. multi-component). All metrics are defined in Section 2.1. Figure 24 illustrates an example of the entrance window predictions on Claude Opus 4.6.

**ZH** 表 41 与表 42 给出完整结果，按场景复杂度（单组件 vs. 多组件）分层。所有指标定义见第 2.1 节。图 24 给出 Claude Opus 4.6 上入场时间窗预测的一个示例。

**EN** Table 41: Video-level and Component-level duration prediction, stratified by scene complexity. ⟦SLOT_101⟧1 scores report the percentage of predictions within the given tolerance. MAE is in seconds. Count MAE measures the absolute error in predicting the number of animated components.

**ZH** 表 41：视频级与组件级的时长预测，按场景复杂度分层。⟦SLOT_101⟧1 分数报告落在给定容差之内的预测占比。MAE 以秒计。Count MAE 度量动画组件数量预测的绝对误差。

<!-- [原子块 · table] Model Input Video-level MAE ↓ \downarrow ≤ \leq 1 s ↑ \uparrow ≤ \leq 2 s ↑ \uparrow All Gemini 3.1 Video 6.21 25.00 46.00 GPT-5.4 Keyframes 6.44 9.00 28.00 Claude-Opus-4.6 Keyframes 6.28 14.00 25.00  -->

**EN** Table 42: Component-level start-time offset prediction, stratified by scene complexity. MAE is in seconds. The model predicts when each element’s entrance animation begins relative to the start of the video. Count MAE measures the absolute error in predicting the number of animated components.

**ZH** 表 42：组件级起始时间偏移预测，按场景复杂度分层。MAE 以秒计。模型预测每个元素的入场动画相对视频起点何时开始。Count MAE 度量动画组件数量预测的绝对误差。

<!-- [原子块 · table] Model Input MAE ↓ \downarrow ≤ \leq 0.5 s ↑ \uparrow ≤ \leq 1.0 s ↑ \uparrow Count MAE ↓ \downarrow All Gemini-3.1 Video 1.41 64.95 82.14 5.82 GPT-5.4 Keyframes 1.44 61.19 80.31 4.07 Claude-Opus-4.6 K -->

**EN** • Video-level duration is poorly estimated across the board: all models exhibit MAE ⟦SLOT_102⟧ 6 s, and the majority of predictions are off by more than two seconds, demonstrating that models lack a reliable internal clock for overall composition length.

**ZH** • 视频级时长整体上估计得很差：所有模型的 MAE 都 ⟦SLOT_102⟧ 6 s，多数预测的偏差超过两秒，说明模型缺乏可靠的内部时钟来衡量合成作品的总体长度。

**EN** • Scene decomposition is the primary bottleneck: single-to-multi performance gap is large and consistent across all sub-tasks, and models with lower component Count MAE estimate timing more accurately.

**ZH** • 场景分解是主要瓶颈：单组件到多组件的性能差距在所有子任务上都大且一致，而组件 Count MAE 更低的模型对时序的估计也更准确。

<!-- [原子块 · img]  -->

**EN** Figure 24: Ground-truth versus predicted entrance windows on one sample. Each bar spans from the component’s entrance start time to the end of its entrance animation (start + duration). Claude-Opus-4.6 correctly identifies the two short rise animations (0-1, 0-2) within 0.25s but substantially underestimates the longer burst and bounce durations (2.80 → 0.80s and 2.50 → 0.30s). The model also hallucinates staggered entrance times (0.0–0.8s offsets) when all four components enter simultaneously at t = 0. Duration MAE: 1.12s; start time MAE: 0.40s.

**ZH** 图 24：一个样本上真值与预测的入场时间窗。每根条形从该组件的入场起始时间延伸到其入场动画的结束时刻（起始 + 时长）。Claude-Opus-4.6 在 0.25 s 之内正确识别了两段较短的 rise 动画（0-1、0-2），却大幅低估了较长的 burst 与 bounce 时长（2.80 → 0.80 s 与 2.50 → 0.30 s）。该模型还幻觉出了交错的入场时间（0.0～0.8 s 的偏移），而实际上四个组件都在 t = 0 同时入场。时长 MAE：1.12 s；起始时间 MAE：0.40 s。

**EN** 7.4 Animation Generation: Parameter Generation

**ZH** 7.4 动画生成：参数生成

**EN** Animation parameter generation evaluates whether video generation models can produce correct animations when given a static design layout and explicit per-component animation specifications. The model receives the last frame of the ground-truth video as a static layout reference along with a text prompt that enumerates, for each component, the animation type (e.g. fade, rise, pan, tumble, flicker, rotate), duration, speed, direction, and animate phase (entrance, continuous, or both). Components are identified only by an integer index and their element type (image, group, or text); the model must resolve which visual region each index refers to using the layout image alone.

**ZH** 动画参数生成评测视频生成模型在给定静态设计版式与逐组件的显式动画规格时，能否产出正确的动画。模型接收真值视频的最后一帧作为静态版式参照，以及一条文本提示，其中逐组件列举了动画类型（如 fade、rise、pan、tumble、flicker、rotate）、时长、速度、方向与动画阶段（入场、持续或两者皆有）。组件仅以整数索引与元素类型（图像、组或文本）标识；模型必须仅凭版式图像判断每个索引对应哪个视觉区域。

**EN** Results.

**ZH** 结果。

**EN** Qualitative results on 10 samples comparing Sora and Veo are provided in the supplementary HTML33 3 https://lica.world/video-generation-benchmarks. Perceptual similarity scores are given in Table 43 and Figure 25 illustrates an example of the prompt and input static layout used in this task. Key findings:

**ZH** 对比 Sora 与 Veo 的 10 个样本的定性结果见补充 HTML33 3 https://lica.world/video-generation-benchmarks。感知相似度分数见表 43，图 25 给出本任务所用提示与输入静态版式的一个示例。关键发现：

**EN** • Grounding is the core failure: given only a static composite frame and a textual list of component indices, models have no reliable way to identify which image region corresponds to “Component ⟦SLOT_103⟧.” They must simultaneously parse the layout, segment it, assign consistent indices, and apply distinct animation parameters to each segment. Precisely controlling attributes such as speed, easing, and magnitude proves substantially harder in this setting.

**ZH** • 定位是核心失效：仅给定一张静态合成帧与一份组件索引的文本清单，模型没有可靠办法判断哪个图像区域对应「组件 ⟦SLOT_103⟧」。它们必须同时解析版式、分割它、指派一致的索引，并对每个片段施加不同的动画参数。在这种设定下，精确控制速度、缓动与幅度等属性要困难得多。

**EN** • Outputs diverge systematically from specifications: in practice, models either apply a single dominant motion globally, animate the wrong elements, or hallucinate motion unrelated to the prompt.

**ZH** • 输出系统性地偏离规格：实践中，模型要么在全局施加单一的主导运动，要么动画了错误的元素，要么幻觉出与提示无关的运动。

**EN** • Full video input does not resolve the problem: faithful animation parameter control would require richer conditioning, such as per-component image crops or masks, so that the model can unambiguously associate each instruction with its target region.

**ZH** • 完整视频输入并不能解决问题：忠实的动画参数控制需要更丰富的条件，例如逐组件的图像裁剪或掩码，使模型能无歧义地把每条指令关联到其目标区域。

**EN** • Automatic metrics are limited: frame-level similarity measures such as FID and LPIPS are uninformative when the layout itself is distorted, and per-component motion metrics presuppose correct component isolation, precisely the capability that is lacking. We report perceptual similarity (LPIPS, SSIM, PSNR) between the input static layout and generated frames to verify that models preserve the original composition, but these scores do not capture whether the correct animations were applied to the correct components. We therefore supplement with qualitative results and leave fine-grained quantitative evaluation to future work with component-level human evaluation.

**ZH** • 自动指标存在局限：当版式本身被扭曲时，FID 与 LPIPS 等帧级相似度度量无法提供信息；而逐组件的运动指标又以正确的组件隔离为前提——这恰恰是缺失的能力。我们报告输入静态版式与生成帧之间的感知相似度（LPIPS、SSIM、PSNR），以验证模型是否保留了原始构成，但这些分数并不能反映正确的动画是否被施加到了正确的组件上。因此我们以定性结果作为补充，并把细粒度的定量评测留给未来结合组件级人工评测的工作。

**EN** Table 43: Perceptual similarity measured between the input static layout and the first and last frames of the generated video. High similarity does not imply correct execution of the prompt: qualitative results show that both models fail to produce the correct motion types and component counts.

**ZH** 表 43：在输入静态版式与生成视频首帧、末帧之间测得的感知相似度。高相似度并不意味着提示被正确执行：定性结果显示两个模型都没能产出正确的运动类型与组件数量。

<!-- [原子块 · table] Evaluation Dimension Method Metric Sora Veo Perceptual Similarity Static → \rightarrow First Frame SSIM ↑ \uparrow 48.51 77.24 Static → \rightarrow Last Frame SSIM ↑ \uparrow 44.05 46.48 Static → \rig -->

<!-- [原子块 · img]  -->

**EN** Figure 25: Example outputs from Sora and Veo given a static design layout with explicit per-component animation instructions. The static input is the final frame of the ground-truth video, which fades to white in this example. Sora more faithfully follows the prompt specifications (e.g., correctly matching the described primary color), while Veo adheres more strongly to the input image, preserving its appearance and color scheme. In this example, both models fail to generate the correct number of components for groups 1–3 and 4–10. While the motion direction is generally correct, the motion type is incorrect for all components.

**ZH** 图 25：给定静态设计版式与逐组件显式动画指令时，Sora 与 Veo 的示例输出。静态输入是真值视频的最后一帧，在本例中淡出为白色。Sora 更忠实地遵循了提示规格（例如正确匹配了所描述的主色），而 Veo 更贴合输入图像，保留了其外观与配色。在本例中，两个模型对组 1–3 与 4–10 都未能生成正确数量的组件。运动方向大体正确，但所有组件的运动类型都是错的。

**EN** 7.5 Animation Generation: Motion Trajectory Generation

**ZH** 7.5 动画生成：运动轨迹生成

**EN** Motion trajectory generation evaluates whether video generation models can synthesize a specific motion primitive (e.g. wipe, fade, rise) given a static layout image and component metadata. The model receives the final resting state of a design, a motion-type label from the 32 LICA primitives, and component specifications (index, type, direction, speed, duration), and must produce keyframes or a video depicting the target transition. We measure motion type accuracy, mean LPIPS (transition smoothness), LPIPS variance (motion evenness), and mean SSIM.

**ZH** 运动轨迹生成评测视频生成模型在给定静态版式图像与组件元数据时，能否合成特定的运动图元（如 wipe、fade、rise）。模型接收一个设计的最终静止状态、来自 32 个 LICA 图元的运动类型标签，以及组件规格（索引、类型、方向、速度、时长），并须产出描绘目标转场的关键帧或视频。我们度量运动类型准确率、平均 LPIPS（转场平滑度）、LPIPS 方差（运动均匀性）与平均 SSIM。

**EN** Results.

**ZH** 结果。

**EN** Qualitative results on 10 samples comparing Sora and Veo are provided in the supplementary HTML3.

**ZH** 对比 Sora 与 Veo 的 10 个样本的定性结果见补充 HTML3。

**EN** Table 44: Human evaluated motion trajectory generation accuracy by motion type. Each sample tests whether the generated video depicts the requested motion primitive. Veo-2.0 and Sora-2 are evaluated on 10 samples spanning 7 of the 32 LICA motion primitives.

**ZH** 表 44：按运动类型划分的人工评测运动轨迹生成准确率。每个样本检验生成的视频是否描绘了所要求的运动图元。Veo-2.0 与 Sora-2 在 10 个样本上评测，覆盖 32 个 LICA 运动图元中的 7 个。

<!-- [原子块 · table] Motion Type No. Samples Veo-2.0 Sora-2 Motion Accuracy ↑ \uparrow Motion Accuracy ↑ \uparrow flicker 1 100.00 0.00 blur 1 0.00 0.00 baseline 1 100.00 0.00 rise 3 66.67 33.33 tumble 1 0.00 0.00 pan 2 1 -->

**EN** • Fine-grained parameter control remains elusive: even when a model successfully reproduces a motion type, precisely controlling attributes such as speed, easing, and magnitude proves substantially harder, indicating that coarse motion generation does not imply fine-grained controllability.

**ZH** • 细粒度参数控制仍然难以实现：即便模型成功复现了某种运动类型，精确控制速度、缓动与幅度等属性也要困难得多，说明粗粒度的运动生成并不意味着细粒度的可控性。

**EN** • Performance is highly motion-dependent: both models succeed on pan but fail on tumble and blur, suggesting that spatial trajectory primitives are easier to reproduce than visual-effect primitives.

**ZH** • 性能高度依赖具体运动：两个模型在 pan 上成功，却在 tumble 与 blur 上失败，说明空间轨迹图元比视觉效果图元更容易复现。

**EN** 7.6 Animation Generation: Short-Form Video Layout Generation

**ZH** 7.6 动画生成：短视频版式生成

**EN** Short-form video layout generation evaluates the model’s ability to produce a complete animated marketing video from a text brief alone, without any visual input. The model shall autonomously design the layout, author text, select a color theme, and animate the composition in 9:16 format. We evaluate on 10 marketing briefs spanning diverse industries via human evaluation (binary pass/fail per metric, ⟦SLOT_104⟧).

**ZH** 短视频版式生成评测模型仅凭文本简报、在无任何视觉输入的情况下产出完整动画营销视频的能力。模型须自主设计版式、撰写文案、选择色彩主题，并以 9:16 格式把该构成动起来。我们通过人工评测（每个指标二元通过与不通过，⟦SLOT_104⟧）在覆盖多个行业的 10 条营销简报上评测。

**EN** Results.

**ZH** 结果。

**EN** Table 45 presents the human evaluation results. Qualitative results on 10 samples comparing Sora and Veo are provided in the supplementary HTML3.

**ZH** 表 45 给出人工评测结果。对比 Sora 与 Veo 的 10 个样本的定性结果见补充 HTML3。

**EN** Table 45: Human evaluation results for short-form video layout generation. Each model receives only a text marketing brief and must generate a complete 9:16 video from scratch. Scores report average correctness percentages over ⟦SLOT_105⟧ samples. For Text Accuracy and Text Readability, we average the per-sample ratios of correct or readable text instances. Spatial Layout Accuracy is computed as the average proportion of correctly matched positioned elements, and Background Correctness is reported as pass rate.

**ZH** 表 45：短视频版式生成的人工评测结果。每个模型只接收一条文本营销简报，必须从零生成完整的 9:16 视频。分数报告 ⟦SLOT_105⟧ 个样本上的平均正确率。对文本准确率与文本可读性，我们对每样本中正确或可读文本实例的比例取平均。空间版式准确率按正确匹配位置的元素比例取平均，背景正确性以通过率报告。

<!-- [原子块 · table] Metric Accuracy ↑ \uparrow Veo-3.1 Sora-2 Text Accuracy 68.69 78.77 Text Readability 81.59 94.13 Spatial Layout Accuracy 80.00 80.00 Background Correctness 80.00 80.00 -->

**EN** • High-level accuracy falls short at finer granularity. While video generation models can adhere to prompts at a high level, performance degrades substantially when evaluation is decomposed into finer-grained criteria such as component-level positioning or text quality.

**ZH** • 高层准确率在更细粒度上失守。视频生成模型能在高层面上遵循提示，但当评测被分解为组件级定位或文本质量等更细的判据时，性能大幅下降。

**EN** • Text quality is a critical differentiator. Sora-2 renders accurate text in 79% of samples, compared to 69% for Veo-3.1. Even in terms of readability, neither model achieves perfect scores, limiting their usability.

**ZH** • 文本质量是关键的区分因素。Sora-2 在 79% 的样本中渲染出准确的文本，Veo-3.1 为 69%。即便只看可读性，两个模型都没能拿到满分，限制了它们的可用性。

<!-- [原子块 · img]  -->

**EN** Figure 26: Qualitative example of single-layout short-form video generation on Sora-2 and Veo-3.1. Each model receives only a text marketing brief describing a vertical fashion announcement and must design, lay out, and animate a complete 9:16 short-form video from scratch (no image input). The ground truth (top) shows components entering sequentially over 4 seconds: brand name, headline with star accents, tagline box, product photo, and social handle, all on a textured marble background. Veo-3.1 (bottom left) reproduces the layout hierarchy and marble background but does not render the video in the requested 9:16 portrait, generates incorrect text, produces the wrong number of star accents flanking the headline, and exhibits visual style inconsistency by the third frame as the layout shifts to a different color scheme. Sora-2 (bottom right) correctly produces a 9:16 portrait video and legible text, but collapses the staggered reveal into a near-simultaneous appearance of all elements, losing the sequential entrance timing specified in the brief. Neither faithfully reproduce the fine-grained compositional structure: Veo-3.1 fails on aspect ratio and animation style, while Sora-2 fails on temporal sequencing and component-level entrance control.

**ZH** 图 26：Sora-2 与 Veo-3.1 上单版式短视频生成的定性示例。每个模型只接收一段描述竖版时装发布会的文本营销简报，必须从零设计、排版并动起来一条完整的 9:16 短视频（不提供图像输入）。真值（上）显示各组件在 4 秒内依次入场：品牌名、带星形装饰的标题、标语框、产品照片与社交账号，全部置于带纹理的大理石背景上。Veo-3.1（左下）复现了版式层级与大理石背景，却没有按要求的 9:16 竖版渲染视频，生成了错误的文本，标题两侧的星形装饰数量不对，并且到第三帧出现视觉风格不一致——版式切换到了另一套配色。Sora-2（右下）正确生成了 9:16 竖版视频与清晰的文字，却把交错揭示压缩成了所有元素近乎同时出现，丢失了简报中规定的顺序入场时序。两者都没有忠实复现细粒度的构成结构：Veo-3.1 在宽高比与动画风格上失败，Sora-2 则在时序编排与组件级入场控制上失败。

**EN** While the present evaluation focuses on single-layout short-form videos, real-world marketing content frequently comprises multi-layout compositions in which distinct scenes or slides transition sequentially within a single video. Evaluating multi-layout generation introduces additional challenges beyond those observed here, including inter-layout coherence, consistent branding across scenes, transition quality, and correct allocation of content to the appropriate layout. We leave systematic evaluation of multi-layout short-form video generation to future work.

**ZH** 本评测聚焦单版式的短视频，而现实中的营销内容常由多版式构成——不同场景或幻灯片在一条视频内依次转场。评测多版式生成会引入超出本文观察之外的额外挑战，包括版式间的连贯性、跨场景的一致品牌呈现、转场质量，以及内容到合适版式的正确分配。我们把多版式短视频生成的系统评测留给未来工作。

**EN** Table 46: Summary of key findings across animation & temporal tasks.

**ZH** 表 46：动画与时序任务的关键发现汇总。

<!-- [原子块 · table] Task Key Finding Best Performance Best Model Status Keyframe Ordering Models beat the random baseline but remain weak; first-frame identification ( ∼ {\sim} 80%) is much easier than full ordering ( ∼  -->

**EN** 8 Discussion

**ZH** 8 讨论

**EN** 8.1 Task Solvability Landscape

**ZH** 8.1 任务可解性全景

**EN** Across the 49 tasks in GDB, a clear solvability hierarchy emerges. Table 47 organizes all task groups into three tiers based on best-model performance and the nature of remaining gaps.

**ZH** 在 GDB 的 49 个任务中，呈现出清晰的可解性层级。表 47 依据最佳模型性能与剩余缺口的性质，把所有任务组归入三个层级。

**EN** Table 47: Task solvability tiers across GDB. Count refers to the number of individual tasks classified in each tier (49 total).

**ZH** 表 47：GDB 上的任务可解性层级。Count 指归入各层级的单个任务数量（共 49 个）。

<!-- [原子块 · table] Tier Count Tasks Why Mostly Solved 2 Template pairwise matching (97.7%), template ranking (MRR = 99.4%) (§ 6 ) Both tasks require binary or ordinal similarity judgments over structured template pairs; -->

**EN** 8.2 Why Are the Unsolved Tasks Hard?

**ZH** 8.2 未解决的任务为何困难？

**EN** Nearly half of all tasks remain unsolved, and most of the rest are only partially solved. 22 of 49 tasks see no meaningful progress beyond chance, and 25 further tasks are only partially solved, meaning that even where models show some capability, outputs are too inconsistent or imprecise to be reliably acted upon. In a real design workflow, a partially correct layout suggestion or an almost-right font prediction is often worse than no suggestion at all: a designer must stop, identify the error, manually correct it, and re-evaluate, a process that can block progress for hours. The common thread across both unsolved and partially solved tasks is the same: any capability requiring precise, structured output or fine-grained discrimination exposes a hard ceiling in current models.

**ZH** 近半数任务仍未解决，其余多数也只是部分解决。49 个任务中有 22 个相对随机基线没有实质进展，另有 25 个只是部分解决——这意味着即便模型展现出某种能力，其输出也过于不稳定或不精确，无法被可靠地采纳。在真实的设计工作流中，一个部分正确的版式建议或一个差之毫厘的字体预测，往往比完全没有建议更糟：设计师必须停下来、找出错误、手工修正并重新评估，这一过程可能让进度停滞数小时。未解决与部分解决的任务有一条共同主线：任何要求精确的结构化输出或细粒度判别的能力，都会撞上当前模型的硬性天花板。

**EN** • Layout (8 unsolved tasks). Models cannot reliably count elements (MAE grows sharply with layout complexity), identify component types beyond coarse text/non-text distinctions, or localize components (6.4% mAP@0.5). Layer order prediction, crop shape detection, frame detection, intent-to-layout generation, and partial layout completion all remain intractable at the precision required for real editing workflows. In practice, this means a designer cannot ask an AI to “move the third image to the left” or “add a new element below the heading” and expect a spatially correct result. The model simply does not know where things are with sufficient confidence to act on them.

**ZH** • 版式（8 个未解决任务）。模型无法可靠地清点元素（MAE 随版式复杂度急剧上升）、无法在粗略的文本／非文本区分之外识别组件类型，也无法定位组件（6.4% mAP@0.5）。层序预测、裁剪形状检测、画框检测、意图到版式的生成与部分版式补全，在真实编辑工作流所需的精度下都仍不可处理。实际上，这意味着设计师无法让 AI「把第三张图往左移」或「在标题下方加一个新元素」并期待得到空间上正确的结果。模型根本不知道各元素在哪里，不足以据此行动。

**EN** • Typography (5 unsolved tasks). Font family recognition tops out at 23.7% across 167 families, with most typefaces scoring zero F1. Text color prediction degrades to ⟦SLOT_106⟧E ⟦SLOT_107⟧ 52 in the weakest models. Font size, weight, and line height estimation all show large absolute errors. For brand-sensitive workflows such as auditing whether a campaign asset uses the correct typeface, extracting a client’s typographic system from a reference design, or checking color compliance against brand guidelines, these failure rates are not acceptable margins of error. They are complete breakdowns. A model that cannot distinguish between two common sans-serif fonts cannot be trusted to maintain brand consistency at scale.

**ZH** • 排版（5 个未解决任务）。字族识别在 167 个字族上最高只到 23.7%，大多数字体的 F1 为零。文本颜色预测在最弱的模型上退化到 ⟦SLOT_106⟧E ⟦SLOT_107⟧ 52。字号、字重与行高的估计都表现出很大的绝对误差。对品牌敏感的工作流——例如审计某传播资产是否使用了正确字体、从参考设计中提取客户的字体排印体系，或依据品牌规范核查颜色合规——这样的失败率不是可接受的误差范围，而是彻底的失效。一个分不清两种常见无衬线字体的模型，无法被信任去规模化地维护品牌一致性。

**EN** • SVG & Vector (3 unsolved tasks). Text-to-SVG generation produces schematic interpretations rather than faithful reproductions. Text-to-Lottie and text+image-to-Lottie generation yield low frame similarity and largely unreproduced animated structure, with one model’s validity dropping from 100% to 66% when image input is added. For production workflows where scalable, editable vector assets are a hard requirement such as icon libraries, motion graphics, and brand illustration systems, the inability to generate faithful vector code from natural language means AI cannot yet participate in the creation pipeline, only in rough ideation.

**ZH** • SVG 与矢量（3 个未解决任务）。文生 SVG 生成产出的是示意性的解读，而非忠实的复现。文生 Lottie 与文本+图像生 Lottie 的帧相似度都很低，动画结构基本未被复现，其中某个模型在加入图像输入后有效性从 100% 跌至 66%。对可缩放、可编辑的矢量素材是硬性要求的生产工作流——图标库、动效图形与品牌插画体系——无法从自然语言生成忠实的矢量代码，意味着 AI 尚不能参与创作管线，只能做粗略的构思。

**EN** • Template Semantics (1 unsolved task). Category classification without label constraints remains difficult, with models assigning labels that are semantically adjacent but taxonomically incorrect. For platforms managing thousands of templates across dozens of categories, this makes automated tagging and search unreliable. The deeper issue is that different models carry different internal design vocabularies, meaning that a template a designer calls a “promotional banner” may be categorized inconsistently across tools, creating friction for any cross-platform design workflow.

**ZH** • 模板语义（1 个未解决任务）。无标签约束的类别分类仍然困难，模型给出的标签语义上相邻却在分类学上错误。对管理着数十个类别、成千上万个模板的平台而言，这使得自动打标与检索不可靠。更深的问题在于，不同模型携带不同的内部设计词表，设计师口中的「促销横幅」可能在不同工具中被不一致地归类，给任何跨平台的设计工作流带来阻力。

**EN** • Animation (6 unsolved tasks). Keyframe ordering exact match sits at 16%, motion type classification below 13% across all models, and component-level duration and start-time estimation degrades sharply as scene complexity grows. Animation parameter generation and motion trajectory synthesis both fail to produce controllable, component-faithful outputs. Full video input does not help as the bottleneck is scene decomposition, not temporal resolution. For designers producing social media content, presentations, or motion graphics at scale, this means AI cannot yet reliably replicate an animation style, extend an existing motion sequence, or apply consistent entrance effects across a set of elements. These are all routine tasks in professional motion design.

**ZH** • 动画（6 个未解决任务）。关键帧排序的精确匹配停在 16%，所有模型的运动类型分类都低于 13%，组件级的时长与起始时间估计随场景复杂度上升而急剧退化。动画参数生成与运动轨迹合成都没能产出可控、忠于组件的输出。完整视频输入也于事无补，因为瓶颈在于场景分解而非时序分辨率。对批量产出社交媒体内容、演示文稿或动效图形的设计师而言，这意味着 AI 尚不能可靠地复刻一种动画风格、延展既有的运动序列，或对一组元素施加一致的入场效果——而这些都是专业动效设计中的例行任务。

**EN** 8.3 Evaluation Gaps

**ZH** 8.3 评测缺口

**EN** Despite its breadth, GDB surfaces several limitations that point to open problems in how design AI should be measured and evaluated.

**ZH** 尽管覆盖面很广，GDB 仍暴露出若干局限，指向「设计 AI 应如何度量与评测」这一开放问题。

**EN** • Pixel metrics are insufficient for design. SSIM, PSNR, and LPIPS cannot distinguish a correct transformation from a hallucinated one when both diverge equally from the source in pixel space. Design evaluation needs structure-aware metrics that operate on extracted primitives such as bounding boxes, font properties, and color tokens rather than raw pixels.

**ZH** • 像素指标不足以衡量设计。当正确变换与幻觉变换在像素空间中与源图偏离程度相当时，SSIM、PSNR 与 LPIPS 无法区分二者。设计评测需要作用于所提取图元（如边界框、字体属性与色彩标记）而非原始像素的结构感知指标。

**EN** • Human evaluation is largely absent. Aside from a small set of preference judgments on generation tasks, GDB relies almost entirely on automatic metrics. Professional designer evaluation is missing: a trained designer can immediately judge whether a layout is usable, a typeface is on-brand, or an animation feels natural, signal that no current automatic metric captures. Large-scale human evaluation with domain experts remains an important missing piece.

**ZH** • 人工评测基本缺席。除生成任务上的少量偏好判断外，GDB 几乎完全依赖自动指标。专业设计师的评测是缺失的：训练有素的设计师能立刻判断一个版式是否可用、一款字体是否符合品牌、一段动画是否自然——这类信号是当前任何自动指标都无法捕捉的。联合领域专家开展大规模人工评测，仍是重要的一环缺失。

**EN** • Only closed-source frontier models are evaluated. All models in this benchmark are proprietary API-served systems. Open-source models, specialized design models, and fine-tuned task-specific systems are not represented, limiting the benchmark’s utility as a community-wide progress tracker. Establishing open-source baselines is a priority for future work.

**ZH** • 只评测了闭源前沿模型。本基准中的所有模型都是通过专有 API 提供服务的系统。开源模型、专用设计模型与针对具体任务微调的系统都未纳入，限制了该基准作为全社区进展追踪工具的效用。建立开源基线是未来工作的优先事项。

**EN** • Evaluation breaks down at near-zero performance. For tasks such as motion type classification and animation parameter generation, outputs are so far from ground truth that neither automatic metrics nor human evaluation can produce meaningful signal. The field needs evaluation frameworks that gracefully handle near-zero performance regimes rather than forcing a score onto outputs that bear no relationship to the target.

**ZH** • 评测在近零性能处失效。对运动类型分类与动画参数生成这类任务，输出与真值相去甚远，自动指标与人工评测都无法产生有意义的信号。该领域需要能从容应对近零性能区间的评测框架，而不是强行给与目标毫无关系的输出打一个分数。

**EN** • Diversity of design contexts is not fully modeled. GDB covers a broad range of template categories but does not capture the full spectrum of design contexts, including culturally specific aesthetics, platform-specific conventions, accessibility requirements, and domain-specific visual languages such as editorial, packaging, or environmental design. Expanding coverage across these dimensions is left to future work.

**ZH** • 设计语境的多样性建模不完整。GDB 覆盖了范围很广的模板类别，却未涵盖设计语境的完整谱系，包括特定文化的美学、特定平台的惯例、无障碍要求，以及编辑、包装或环境设计等特定领域的视觉语言。在这些维度上扩展覆盖留给未来工作。

**EN** 9 Conclusion

**ZH** 9 结论

**EN** We have presented GraphicDesignBench (GDB), a benchmark suite of 49 tasks across five design domains: layout, typography, infographics, template & design semantics, and animation, grounded in real-world layered templates from the LICA dataset. Our evaluation of various frontier model families yields a clear verdict: only 2 of 49 tasks are mostly solved, 25 are partially solved, and 22 remain unsolved. Every domain contributes unsolved tasks, with layout-level and animation the hardest hit, and the gap to practical reliability is large, e.g., component detection peaks at 6.4% mAP, font recognition at 23.7%, and motion type classification below 13%. Closing these gaps will likely require advances on both the modeling and evaluation fronts. On the modeling side, design-specialized pretraining with structural supervision on layered composition data is a promising direction, while architectures supporting longer structured outputs could address the SVG and Lottie truncation bottleneck. Looking ahead, we plan to evaluate open-source vision-language models, conduct a systematic prompt engineering study, release human performance references from a designer evaluation currently underway, expand the study to other open-source datasets, and conduct cross-task ablation studies to better understand whether capabilities transfer across design domains — for instance, whether models that excel at typography understanding also generalize to styled text generation, or whether spatial reasoning in layout tasks correlates with performance in animation decomposition.

**ZH** 我们提出了 GraphicDesignBench（GDB），一套覆盖版式、排版、信息图、模板与设计语义、动画五个设计领域、共 49 个任务的基准套件，其根基是 LICA 数据集中真实的分层模板。我们对若干前沿模型家族的评测给出了明确的结论：49 个任务中只有 2 个基本解决，25 个部分解决，22 个仍未解决。每个领域都有未解决的任务，其中版式层面与动画受创最重，而距实用可靠性的差距很大——组件检测的峰值是 6.4% mAP，字体识别是 23.7%，运动类型分类低于 13%。弥合这些差距很可能需要在建模与评测两条战线上同时推进。建模方面，在分层合成数据上加入结构监督的设计专用预训练是一个有前景的方向，而支持更长结构化输出的架构可以缓解 SVG 与 Lottie 的截断瓶颈。展望未来，我们计划评测开源视觉语言模型、开展系统的提示工程研究、发布正在进行的设计师评测所得到的人类表现参照、把研究扩展到其他开源数据集，并开展跨任务消融研究，以更好地理解能力是否会在设计领域之间迁移——例如擅长排版理解的模型是否也能泛化到样式化文本生成，或版式任务中的空间推理是否与动画分解中的表现相关。

**EN** We release GDB as an open benchmark with the goal of accelerating progress toward AI systems that can serve as capable, reliable collaborators in professional design workflows.

**ZH** 我们把 GDB 作为开放基准发布，目标是加速推进「让 AI 系统成为专业设计工作流中能干且可靠的协作者」这一进程。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] [1] Naoto Inoue, Kento Masui, Wataru Shimoda, and Kota Yamaguchi. Opencole: Towards reproducible automatic graphic design generation. In Proceedings of the IEEE/CVF Conference on Computer Vision and P -->

<!-- [原子块 · verbatim] [2] Yutao Cheng, Zhao Zhang, Maoke Yang, Hui Nie, Chunyuan Li, Xinglong Wu, and Jie Shao. Graphic design with large multimodal model. In Proceedings of the AAAI Conference on Artificial Intelligence , -->

<!-- [原子块 · verbatim] [3] Jiawei Lin, Shizhao Sun, Danqing Huang, Ting Liu, Ji Li, and Jiang Bian. From elements to design: A layered approach for automatic graphic design composition. arXiv preprint arXiv:2412.19712 , 202 -->

<!-- [原子块 · verbatim] [4] Peidong Jia, Chenxuan Li, Yuhui Yuan, Zeyu Liu, Yichao Shen, Bohan Chen, Xingru Chen, Yinglin Zheng, Dong Chen, Ji Li, Xiaodong Xie, Shanghang Zhang, and Baining Guo. Cole: A hierarchical generati -->

<!-- [原子块 · verbatim] [5] Jingye Chen, Zhaowen Wang, Nanxuan Zhao, Li Zhang, Difan Liu, Jimei Yang, and Qifeng Chen. Rethinking layered graphic design generation with a top-down approach. arXiv preprint arXiv:2507.05601 ,  -->

<!-- [原子块 · verbatim] [6] Martin Heusel, Hubert Ramsauer, Thomas Unterthiner, Bernhard Nessler, and Sepp Hochreiter. Gans trained by a two time-scale update rule converge to a local nash equilibrium. Advances in neural inf -->

<!-- [原子块 · verbatim] [7] Tim Salimans, Ian Goodfellow, Wojciech Zaremba, Vicki Cheung, Alec Radford, and Xi Chen. Improved techniques for training gans. Advances in neural information processing systems , 29, 2016. -->

<!-- [原子块 · verbatim] [8] Jack Hessel, Ari Holtzman, Maxwell Forbes, Ronan Le Bras, and Yejin Choi. Clipscore: A reference-free evaluation metric for image captioning. In Proceedings of the 2021 conference on empirical met -->

<!-- [原子块 · verbatim] [9] Elad Hirsch, Shubham Yadav, Mohit Garg, and Purvanshi Mehta. Lica: Layered image composition annotations for graphic design research. arXiv preprint arXiv:2603.16098 , 2026. -->

<!-- [原子块 · verbatim] [10] Tsung-Yi Lin, Michael Maire, Serge Belongie, James Hays, Pietro Perona, Deva Ramanan, Piotr Dollár, and C Lawrence Zitnick. Microsoft coco: Common objects in context. In European conference on co -->

<!-- [原子块 · verbatim] [11] Richard Zhang, Phillip Isola, Alexei A Efros, Eli Shechtman, and Oliver Wang. The unreasonable effectiveness of deep features as a perceptual metric. In Proceedings of the IEEE conference on comp -->

<!-- [原子块 · verbatim] [12] Zhou Wang, Alan C Bovik, Hamid R Sheikh, and Eero P Simoncelli. Image quality assessment: from error visibility to structural similarity. IEEE transactions on image processing , 13(4):600–612, 20 -->

<!-- [原子块 · verbatim] [13] Stephanie Fu, Netanel Tamir, Shobhita Sundaram, Lucy Chai, Richard Zhang, Tali Dekel, and Phillip Isola. Dreamsim: Learning new dimensions of human visual similarity using synthetic data. arXiv p -->

<!-- [原子块 · verbatim] [14] Yuval Kirstain, Adam Polyak, Uriel Singer, Shahbuland Matiana, Joe Penna, and Omer Levy. Pick-a-pic: An open dataset of user preferences for text-to-image generation. Advances in neural informati -->

<!-- [原子块 · verbatim] [15] Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q Weinberger, and Yoav Artzi. Bertscore: Evaluating text generation with bert. In International Conference on Learning Representations , 2019. -->

<!-- [原子块 · verbatim] [16] Hossein Talebi and Peyman Milanfar. Nima: Neural image assessment. IEEE transactions on image processing , 27(8):3998–4011, 2018. -->

<!-- [原子块 · verbatim] [17] Jiazheng Xu, Xiao Liu, Yuchen Wu, Yuxuan Tong, Qinkai Li, Ming Ding, Jie Tang, and Yuxiao Dong. Imagereward: Learning and evaluating human preferences for text-to-image generation. Advances in Ne -->

<!-- [原子块 · verbatim] [18] Yuhang Ma, Xiaoshi Wu, Keqiang Sun, and Hongsheng Li. Hpsv3: Towards wide-spectrum human preference score. In Proceedings of the IEEE/CVF International Conference on Computer Vision , pages 15086 -->

<!-- [原子块 · verbatim] [19] Sohan Patnaik, Rishabh Jain, Balaji Krishnamurthy, and Mausoom Sarkar. Aesthetiq: Enhancing graphic layout design via aesthetic-aware preference alignment of multi-modal large language models. In -->

<!-- [原子块 · verbatim] [20] Zhao Zhang, Yutao Cheng, Dexiang Hong, Maoke Yang, Gonglei Shi, Lei Ma, Hui Zhang, Jie Shao, and Xinglong Wu. Creatiposter: Towards editable and controllable multi-layer graphic design generation -->

<!-- [原子块 · verbatim] [21] Yadong Qu, Shancheng Fang, Yuxin Wang, Xiaorui Wang, Zhineng Chen, Hongtao Xie, and Yongdong Zhang. Igd: Instructional graphic design with multimodal layer generation. arXiv preprint arXiv:2507.0 -->

<!-- [原子块 · verbatim] [22] Siqi Chen, Xinyu Dong, Haolei Xu, Xingyu Wu, Fei Tang, Hang Zhang, Yuchen Yan, Linjuan Wu, Wenqi Zhang, Guiyang Hou, et al. Svgenius: Benchmarking llms in svg understanding, editing and generatio -->

<!-- [原子块 · verbatim] [23] Lawrence Hubert and Phipps Arabie. Comparing partitions. Journal of classification , 2(1):193–218, 1985. -->

<!-- [原子块 · verbatim] [24] Gaurav Sharma, Wencheng Wu, and Edul N Dalal. The CIEDE2000 color-difference formula: Implementation notes, supplementary test data, and mathematical observations. Color Research & Application ,  -->

<!-- [原子块 · verbatim] [25] W3C. Web Content Accessibility Guidelines (WCAG) 2.0. https://www.w3.org/TR/WCAG20/ , 2008. W3C Recommendation. -->

**EN** Appendix A Metric Definitions

**ZH** 附录 A 指标定义

**EN** Section 2.1 provides an overview of all metrics. This appendix gives formal definitions for the non-trivial metrics reported in the benchmark tables.

**ZH** 第 2.1 节概述了所有指标。本附录给出基准表格中那些非平凡的指标的形式化定义。

**EN** A.1 Standard Metrics

**ZH** A.1 标准指标

**EN** Table 48 summarizes the standard metrics used across multiple tasks.

**ZH** 表 48 汇总了跨多个任务使用的标准指标。

**EN** Table 48: Standard evaluation metrics. ⟦SLOT_108⟧ = higher is better; ⟦SLOT_109⟧ = lower is better.

**ZH** 表 48：标准评测指标。⟦SLOT_108⟧ = 越高越好；⟦SLOT_109⟧ = 越低越好。

<!-- [原子块 · table] Category Metric Dir. Definition Spatial mIoU ↑ \uparrow Mean intersection-over-union between predicted and ground-truth axis-aligned bounding boxes, averaged over all matched elements. mAP@ θ \theta ↑ -->

**EN** For Lottie tasks, MSE and SSIM are computed per keyframe and averaged across five rendered frames (0%, 25%, 50%, 75%, 100% of duration), reported as FrameMSE and FrameSSIM.

**ZH** 对 Lottie 任务，MSE 与 SSIM 逐关键帧计算，并在五个渲染帧（时长的 0%、25%、50%、75%、100%）上取平均，报告为 FrameMSE 与 FrameSSIM。

**EN** A.2 Task-Specific Metrics

**ZH** A.2 任务专属指标

**EN** Table 49 defines metrics specific to SVG, Lottie, and template generation tasks.

**ZH** 表 49 定义了 SVG、Lottie 与模板生成任务专属的指标。

**EN** Table 49: Task-specific evaluation metrics. All string comparisons apply whitespace normalization (collapsing runs to single spaces) before comparison.

**ZH** 表 49：任务专属评测指标。所有字符串比较在比较前都做空白归一化（把连续空白折叠为单个空格）。

<!-- [原子块 · table] Task Metric Dir. Definition SVG Editing RepSim ↑ \uparrow Repair similarity ∈ [ 0 , 1 ] \in[0,1] : the fraction of text shared as identical substrings between predicted and ground-truth SVG, after whi -->

**EN** Appendix B Task Prompts

**ZH** 附录 B 任务提示

**EN** Table 50: Prompt templates for layout understanding tasks (Section 3.1).

**ZH** 表 50：版式理解任务的提示模板（第 3.1 节）。

<!-- [原子块 · table] Task Prompt Expected Output Aspect Ratio You are a design layout analyst. Look at this rendered design template and predict the aspect ratio of the canvas. Choose exactly one from: 1:1, 16:9, 9:16, 4: -->

**EN** Table 51: Prompt templates for image understanding tasks (Section 3.1).

**ZH** 表 51：图像理解任务的提示模板（第 3.1 节）。

<!-- [原子块 · table] Task Prompt Expected Output Image Rotation You are a design expert. Look at this rendered design template. Focus on the image element described as: “{description}” Is this image rotated from its norma -->

**EN** Table 52: Prompt templates for layout generation tasks in Section 3.2.

**ZH** 表 52：第 3.2 节版式生成任务的提示模板。

<!-- [原子块 · table] Task Prompt Expected Output Intent-to-Layout You are an expert end-to-end layout designer. User intent: [Description of layout intent] Image description: [Detailed visual description] Aesthetic/style  -->

**EN** Table 53: Prompt templates for typography understanding tasks (Section 4.1).

**ZH** 表 53：排版理解任务的提示模板（第 4.1 节）。

<!-- [原子块 · table] Task Prompt Expected Output Font Family You are a typography expert. Look at this rendered design template. What font family is used for the text: “{target_text}”? Respond with ONLY the font family na -->

**EN** Table 54: Prompt template for the Partial Completion task (Section 3.2).

**ZH** 表 54：部分补全任务的提示模板（第 3.2 节）。

<!-- [原子块 · table] Task Prompt Expected Output Partial Completion (Section 3.2 ) [Input Images: image_1 (base composite), image_2, …, image_N (component assets)] You are an expert layout planner focused on high-fidelity -->

**EN** Table 55: Prompt template for styled text generation in Section 4.2.

**ZH** 表 55：第 4.2 节样式化文本生成的提示模板。

<!-- [原子块 · table] Task Prompt Expected Output Styled Text Generation You are an expert typography compositor for structured design layouts. Task: restore one missing text element in the local patch. Target text (exact, -->

**EN** Table 56: Prompt template for text removal in Section 4.3.

**ZH** 表 56：第 4.3 节文本移除的提示模板。

<!-- [原子块 · table] Task Prompt Expected Output Text Removal You are an expert design retoucher specialized in text removal and background inpainting. Task: remove all visible text while preserving non-text visual conten -->

**EN** Table 57: Prompt templates for SVG understanding and editing tasks (Section 5.1). All tasks receive SVG source code as input (code-only, no rendered images).

**ZH** 表 57：SVG 理解与编辑任务的提示模板（第 5.1 节）。所有任务都以 SVG 源码为输入（纯代码，不提供渲染图像）。

<!-- [原子块 · table] Task Prompt Expected Output Perceptual Q&A You are an SVG analysis expert. Analyse the given SVG code and answer the multiple-choice question about its visual properties. Output your answer in the exa -->

**EN** Table 58: Prompt templates for SVG generation tasks (Section 5.2).

**ZH** 表 58：SVG 生成任务的提示模板（第 5.2 节）。

<!-- [原子块 · table] Task Prompt Expected Output Text-to-SVG You are an SVG code generator. Given a description of a graphic, output ONLY valid SVG code. Do not include any explanation, markdown fences, or extra text. [Na -->

**EN** Table 59: Prompt templates for template & design semantics tasks (Sections 6.1 and 6.2). Input is a rendered design template PNG image.

**ZH** 表 59：模板与设计语义任务的提示模板（第 6.1 与 6.2 节）。输入是渲染好的设计模板 PNG 图像。

<!-- [原子块 · table] Task Prompt Expected Output Category Classification (Open-vocab) (Section 6.1 ) You are a design template classifier. Look at this rendered design template image and classify it into a single broad ca -->

**EN** Table 60: Prompt templates for template variant understanding tasks (Section 6.3). Input is layout JSON and/or rendered PNG depending on modality condition.

**ZH** 表 60：模板变体理解任务的提示模板（第 6.3 节）。输入依模态条件为版式 JSON 和／或渲染好的 PNG。

<!-- [原子块 · table] Task Prompt Expected Output Pairwise Matching You are given two layouts (A and B). Determine whether they originate from the same template. Answer with a single digit: 1 if same template, 0 if differe -->

**EN** Table 61: Prompt templates for template variant generation tasks (Section 6.4). All prompts receive structured JSON input and expect JSON output.

**ZH** 表 61：模板变体生成任务的提示模板（第 6.4 节）。所有提示接收结构化 JSON 输入并期望 JSON 输出。

<!-- [原子块 · table] Task Prompt Expected Output Style Completion You are a professional graphic designer. You are given several sibling layouts that share the same template (as JSON), plus a SKELETON of a new layout from -->

**EN** Table 62: Prompt templates for template variant generation (image generation) tasks (Section 6.4). Prompts receive rendered reference images and expect a single generated image as output.

**ZH** 表 62：模板变体生成（图像生成）任务的提示模板（第 6.4 节）。提示接收渲染好的参考图像，期望输出单张生成图像。

<!-- [原子块 · table] Task Prompt Expected Output Style Completion (Image) You are a professional graphic designer. You are given rendered images of layouts from a template family as style reference, plus a SKELETON wirefr -->

**EN** Table 63: Prompt templates for temporal understanding tasks (Sections 7.1, 7.2, and 7.3). Input is either shuffled keyframe images or an animation video depending on the task.

**ZH** 表 63：时序理解任务的提示模板（第 7.1、7.2 与 7.3 节）。输入依任务为被打乱的关键帧图像或一段动画视频。

<!-- [原子块 · table] Task Prompt Expected Output Keyframe Ordering (Section 7.1 ) You are an animation analyst. You are shown 4 keyframe images extracted from a single design animation video. The images are presented in a -->

**EN** Table 64: Prompt templates for video generation tasks (Sections 7.4, 7.5, and 7.6). Input varies by task: static layout PNG + text prompt, or text-only brief. Output is a generated video evaluated by human raters.

**ZH** 表 64：视频生成任务的提示模板（第 7.4、7.5 与 7.6 节）。输入依任务而异：静态版式 PNG + 文本提示，或纯文本简报。输出是由人工评分者评测的生成视频。

<!-- [原子块 · table] Task Prompt Expected Output Animation Parameter Generation (Section 7.4 ) Animate this static layout image. Apply the following entrance animations to the components. The total animation duration is [ -->

**EN** Table 65: Prompt template for M-Judge evaluation.

**ZH** 表 65：M-Judge 评测的提示模板。

<!-- [原子块 · table] Metric Prompt Expected Output M-Judge You are a visual language model designed to evaluate and rate visual templates. You are presented with 2 visual templates. The first attached image is image_1 and -->

**EN** Appendix C BBox Detector Selection for Typography Spatial Evaluation

**ZH** 附录 C 排版空间评测的边界框检测器选择

**EN** We report text-region spatial metrics using IoU and bbox F1. When explicit target text boxes are unavailable, we estimate text boxes with an LLM-based detector. Despite the significant challenges that artistic fonts in posters pose to traditional OCR algorithms, the LLM detector is more robust for this setting. To select a single detector, we benchmarked three LLM detectors on 100 ground-truth typography-layout samples. Detection rate is the fraction of evaluated samples for which the detector returns a valid text bounding box. As shown in Table 66, GPT-5.4 achieved the highest F1 and mIoU, so it is used as the default bbox detector.

**ZH** 我们用 IoU 与 bbox F1 报告文本区域的空间指标。当缺少显式目标文本框时，我们用基于 LLM 的检测器估计文本框。尽管海报中的艺术字体给传统 OCR 算法带来很大挑战，LLM 检测器在这种设定下更为稳健。为选定单一检测器，我们在 100 个真值排版版式样本上比对了三个 LLM 检测器。检测率指检测器返回合法文本边界框的受评样本占比。如表 66 所示，GPT-5.4 取得了最高的 F1 与 mIoU，因此被用作默认的边界框检测器。

**EN** Table 66: Text-bbox detector selection on GT typography-layout samples (⟦SLOT_110⟧). Best scores are in bold.

**ZH** 表 66：在真值排版版式样本上的文本边界框检测器选择（⟦SLOT_110⟧）。最优分数以粗体标出。

<!-- [原子块 · table] Detector Detection Rate ↑ \uparrow mIoU ↑ \uparrow Precision ↑ \uparrow Recall ↑ \uparrow F1 ↑ \uparrow GPT-5.4 1.000 0.863 0.946 0.905 0.919 Gemini-3.1-Pro 1.000 0.731 0.865 0.797 0.829 Claude Opus 4 -->
