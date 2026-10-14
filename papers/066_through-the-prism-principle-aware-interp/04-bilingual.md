# 透过 PRISM：原则感知、可解释、多尺度的视觉设计评测

> 原标题：Through the PRISM: Principle-Aware, Interpretable, and Multi-Scale Evaluation of Visual Designs
> 作者：Mona Gandhi, KJ Joseph, Srinivasan Parthasarathy, Sayan Nag · arXiv:2606.00592 · 2026-05-30

<!-- [原子块 · verbatim] Through the PRISM: Principle-Aware, Interpretable, and Multi-Scale Evaluation of Visual Designs -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] Effective visual communication stems from the harmony of multiple design principles, such as readability, contrast, alignment, overlap, and coherence, which collectively govern clarity and intent of t -->

<!-- [原子块 · img]  -->

**EN** Figure 1: We introduce ⟦SLOT_0⟧ PRISM, a benchmark that operationalizes design evaluation through measurable principles of visual composition. Derived from professional layouts, PRISM systematically perturbs examples along five principles: coherence, readability, contrast, alignment, and overlap, isolating targeted violations while preserving other attributes. These controlled perturbations enable interpretable and principle-specific evaluation of models’ sensitivity to localised design degradations and their holistic reasoning about visual quality.

**ZH** 图 1：我们提出 ⟦SLOT_0⟧ PRISM——一个通过可度量的视觉构成原则来落实设计评测的基准。PRISM 源自专业版面，沿连贯性、可读性、对比度、对齐与遮挡五项原则对样本做系统性扰动，在保留其他属性的同时隔离出目标违规。这些受控扰动使我们能够以可解释、针对特定原则的方式，评测模型对局部设计退化的敏感度，以及模型关于视觉质量的整体推理。

**EN** 1 Introduction

**ZH** 1 引言

**EN** Designing is inherently a process of reasoning about perception and communication. When evaluating a visual composition, human designers do not typically rely on a single notion of “good design”. They often weigh multiple interacting principles such as coherence, readability, contrast, alignment, balance, and many more such design principles [46]. A designer might praise a layout’s overall theme yet still adjust text spacing for legibility or modify color contrast for accessibility. This layered reasoning, which moves fluidly between global intent and local detail, enables designers to make targeted refinements preserving the composition’s purpose while enhancing clarity and aesthetics [19].

**ZH** 设计本质上是一个关于感知与传播的推理过程。在评价一个视觉构成时，人类设计师通常不会依赖某一种「好设计」的单一概念，而往往会权衡多项相互作用的原则，例如连贯性、可读性、对比度、对齐、平衡等诸多设计原则 [46]。设计师可能赞赏某个版面的整体主题，同时仍会为易读性调整文字间距，或为无障碍性修改色彩对比度。这种在整体意图与局部细节之间自如切换的分层推理，使设计师能够在保持构成意图的同时做出有针对性的改进，提升清晰度与美感 [19]。

**EN** In contrast, existing computational evaluation methods reduce this multifaceted process to a single scalar score, such as aesthetic preference or layout similarity [13, 34, 38]. While convenient, these metrics cannot reveal which aspects of a design are successful or unsuccessful, and they offer little guidance for actionable improvement [30, 59] or provide end-to-end refiners [13]. Their aggregation of all principles into a single scalar is at odds with how human designers critique and refine, focusing on specific violations that can be iteratively addressed [30, 56].

**ZH** 相比之下，现有的计算评测方法把这一多面过程压缩为单个标量分数，例如美学偏好或版面相似度 [13, 34, 38]。这些指标虽然方便，却无法揭示设计中哪些方面成功、哪些方面失败，也很少为可执行的改进提供指导 [30, 59]，或只能提供端到端的修正器 [13]。它们把所有原则聚合为单个标量的做法，与人类设计师批评和改进设计的方式相悖——后者聚焦于那些可被逐项处理的具体违规 [30, 56]。

**EN** Recent large language and multimodal models (LLMs and MLLMs) can produce free-form critiques that appear similar to human reasoning [30, 10, 56]. However, their evaluations are stochastic, qualitative, and non-reproducible. Given the same poster, such models often generate inconsistent feedback, sometimes suggesting unnecessary global edits for well-designed layouts. Further, their responses lack grounding in explicit design principles and provide judgments without measurable justification. Thus, they behave more like subjective critics than consistent evaluators.

**ZH** 近来的大语言模型与多模态模型（LLM 与 MLLM）能够生成看似类似人类推理的自由形式评论 [30, 10, 56]。然而，它们的评测是随机的、定性的且不可复现的：面对同一张海报，这类模型常给出前后不一致的反馈，有时还会对设计良好的版面提出不必要的全局修改。此外，其回答并未立足于明确的设计原则，给出的判断缺乏可度量的依据。因此，它们的行为更接近主观的评论者，而非一致的评测者。

**EN** To bridge this gap, we introduce ⟦SLOT_1⟧ PRISM (PRinciple-aware, Interpretable, and Structure-guided Design Modifications), a curated perturbation dataset that systematically degrades professionally crafted designs from the Crello corpus [52] along controlled dimensions of coherence, readability, contrast, alignment, and overlap (ref Fig. 1). Each perturbation isolates a targeted violation, for example, text color blending into the background for readability, or a mismatch between the headline and imagery for coherence, thus providing principle-specific supervision for multimodal evaluation. These controlled degradations reflect how humans perceive drops in design quality: localised changes in text or contrast disrupt readability, while global inconsistencies undermine coherence and intent. Analysis on PRISM reveals a gap in current models: architectures like Qwen-2.5-VL [1] and GPT-4o-mini [32] often fail to register these controlled degradations, while GPT-4o [20] shows broad semantic sensitivity but lacks consistent separation between fine-grained principles.

**ZH** 为弥合这一差距，我们提出 ⟦SLOT_1⟧ PRISM（PRinciple-aware, Interpretable, and Structure-guided Design Modifications，即原则感知、可解释、结构引导的设计修改）——一个精心构建的扰动数据集，它沿连贯性、可读性、对比度、对齐与遮挡这些受控维度，对来自 Crello 语料库 [52] 的专业设计做系统性退化（参见图 1）。每次扰动都隔离出一种目标违规，例如让文字颜色融入背景以破坏可读性，或让标题与图像不匹配以破坏连贯性，从而为多模态评测提供针对特定原则的监督。这些受控退化反映了人类感知设计质量下降的方式：文字或对比度的局部变化会破坏可读性，而全局性的不一致则损害连贯性与意图传达。在 PRISM 上的分析揭示了当前模型的一个缺口：Qwen-2.5-VL [1] 与 GPT-4o-mini [32] 等架构常常察觉不到这些受控退化，而 GPT-4o [20] 虽表现出广泛的语义敏感度，却不能在细粒度原则之间做出一致的区分。

**EN** Building on PRISM, we propose a structured evaluation framework with principle-specific scorers and localisers. PRISM-scorer is a lightweight classifier built on a SigLIP-v2 [49] backbone fine-tuned on design data for each principle, trained to produce quantitative scores. For local principles such as readability, we pair these scorers with an instruction-tuned Qwen-2.5-VL model that not only detects issues but also explains where they occur, similar to how a designer highlights specific regions needing adjustment. For higher-level properties such as coherence, which involve semantic and thematic consistency, we use prompting-based evaluation with MLLMs. Finally, we illustrate how the scorer and localiser enable interpretable, iterative refinement using a lightweight beam search-based editing [44]. The editor proposes minimal adjustments that improve targeted principle scores while preserving the overall layout, offering controllable feedback beyond generative MLLMs [7, 20] that treat designs as static images.

**ZH** 在 PRISM 的基础上，我们提出一个带有原则专用打分器与定位器的结构化评测框架。PRISM-Scorer 是一个轻量级分类器，构建于在设计数据上微调的 SigLIP-v2 [49] 骨干之上，针对每个原则分别训练，用以产出定量分数。对可读性这类局部原则，我们把这些打分器与经指令微调的 Qwen-2.5-VL 模型配对，后者不仅能发现问题，还能解释问题出现在哪里，类似设计师标出需要调整的具体区域。对连贯性这类涉及语义与主题一致性的更高层属性，我们采用基于提示的评测，使用 MLLM。最后，我们展示打分器与定位器如何借助轻量级的集束搜索编辑 [44] 实现可解释的迭代式改进：编辑器提出最小幅度的调整，在保留整体版面的同时提升目标原则分数，从而提供超越生成式 MLLM [7, 20] 的可控反馈——后者把设计当作静态图像来处理。

<!-- [原子块 · object]  -->

**EN** Figure 2: PRISM-Scorer Performance. ⟦SLOT_2⟧-score bar plot comparing the sensitivity of different models to PRISM perturbations. Each axis shows the change in principle-specific scores between the original and perturbed posters, as assigned by each scorer. Higher values indicate stronger discrimination of principle violations. Refer to Section 4.3 for further details.

**ZH** 图 2：PRISM-Scorer 性能。⟦SLOT_2⟧ 分数柱状图，比较不同模型对 PRISM 扰动的敏感度。每条轴表示由各打分器给出的原始海报与扰动海报之间、针对特定原则的分数变化。数值越高，说明对原则违规的区分能力越强。详见第 4.3 节。

<!-- [原子块 · table] Unperturbed Coherence Readability Contrast Alignment Overlap Original composed layout from Crello. Text replaced with a different theme to break thematic consistency. Font attributes like size, color  -->

**EN** Figure 3: Illustration of PRISM perturbations. The composed layout (left) serves as the reference design. Each perturbed layout (right) isolates a violation of a specific design principle: coherence, alignment, readability, contrast, and overlap, while minimally affecting others. Descriptions below each image summarize the targeted modification. Bounding boxes highlight regions where local edits were applied, providing ground-truth supervision for principle-specific localisation.

**ZH** 图 3：PRISM 扰动示意。左侧的合成版面作为参考设计；右侧的每个扰动版面隔离出对某一特定设计原则的违规——连贯性、对齐、可读性、对比度与遮挡——同时把对其他原则的影响降到最低。每张图下方的描述概括了目标修改。边界框标出了施加局部编辑的区域，为针对特定原则的定位提供真值监督。

**EN** Our work makes three key contributions. We

**ZH** 我们的工作有三项关键贡献。

**EN** • Present ⟦SLOT_3⟧ PRISM, a controlled perturbation dataset that isolates principle-specific degradations in designs.

**ZH** • 提出 ⟦SLOT_3⟧ PRISM——一个隔离设计中针对特定原则退化的受控扰动数据集。

**EN** • Propose a principled evaluation framework where each principle has a scorer for quantitative assessment and a localiser for spatially grounded feedback.

**ZH** • 提出一个原则化的评测框架，其中每条原则都配有一个用于定量评估的打分器，以及一个用于给出空间定位反馈的定位器。

**EN** • Demonstrate that our SigLIP-based scorers cleanly separate principle-specific degradations, outperforming GPT-4o in disentanglement (See Fig.2) , and that our instruction-tuned Qwen-2.5-VL localiser aligns most closely with ground-truth annotations for local principles.

**ZH** • 证明我们基于 SigLIP 的打分器能清晰地分离出针对特定原则的退化，在解耦能力上优于 GPT-4o（见图 2）；并证明我们经指令微调的 Qwen-2.5-VL 定位器在局部原则上与真值标注最为吻合。

**EN** These advances establish a principled and interpretable pipeline for evaluating and refining visual design.

**ZH** 这些进展为评估与改进视觉设计确立了一条原则化、可解释的流水线。

**EN** 2 Related Works

**ZH** 2 相关工作

**EN** Design Evaluation. Design evaluation has been extensively studied across domains and development stages. Early heuristic-based methods [2, 15, 31, 36, 54] struggled to capture semantic design attributes. Subsequent approaches [9] enhanced evaluation capabilities but lacked comparative scoring mechanisms, motivating siamese-based approaches [57, 13]. Kong et al. [23] trained a model for aesthetic assessment, while Tabata et al. [48] perturbed layouts to synthesize poor designs for scoring. More recently, MLLM-based methods have focused on design generation [22], assessed only limited attributes [22, 14], or provided actionable feedback [10, 30]. However, such feedback is often stochastic, redundant, over-suggestive, or lacks contextual awareness - preventing principled, quantifiable and localised assessment of crucial design attributes.

**ZH** 设计评测。设计评测已在多个领域与多个开发阶段得到广泛研究。早期的启发式方法 [2, 15, 31, 36, 54] 难以捕捉语义层面的设计属性；随后的工作 [9] 增强了评测能力，却缺少比较式打分机制，从而催生了基于孪生网络的方法 [57, 13]。Kong 等人 [23] 训练了一个用于美学评价的模型，Tabata 等人 [48] 则通过扰动版面来合成劣质设计以供打分。更近期地，基于 MLLM 的方法聚焦于设计生成 [22]，只评估有限的属性 [22, 14]，或提供可执行的反馈 [10, 30]。然而，这类反馈往往是随机的、冗余的、过度建议的，或缺乏语境感知，因而无法对关键设计属性做出原则化、可量化且有定位的评估。

**EN** Design Principles. Core principles of graphic layout were established long ago and remain widely used [36, 37]. Since then they have been used for guiding layout generation [28, 45]. Recently, layout-generation methods [16, 17, 56, 25, 27] have adopted content based metrics: occulsion, unreadability and graphic metrics including overlay (IoU), non-alignment, using them to iteratively refine layouts toward structurally and visually plausible compositions. Other works also leverage design-related cues for downstream tasks, for example DocEdit-v2 [47] incorporates spatial coherence in multimodal document editing, and hybrid global–local segmentation models use spatial coherence and region–text alignment for grounding [51]. Even outside visual design, multimodal topic-modeling introduces metrics to capture visual coherence and topic separability [12]. Across these directions, design principles consistently operate as guidance signals for generation and multimodal reasoning, but they remain largely unused as explicit dimensions for assessing design quality.

**ZH** 设计原则。平面版面的核心原则确立已久，至今仍被广泛使用 [36, 37]，此后又被用于指导版面生成 [28, 45]。近来，版面生成方法 [16, 17, 56, 25, 27] 采用了基于内容的指标：遮挡、不可读性，以及包含重叠（IoU）、未对齐在内的图形指标，并用它们迭代地把版面改进为结构与视觉上合理的构成。另一些工作也把设计相关线索用于下游任务，例如 DocEdit-v2 [47] 在多模态文档编辑中引入空间连贯性，混合的全局—局部分割模型则利用空间连贯性与区域—文本对齐来实现定位 [51]。甚至在视觉设计之外，多模态主题建模也引入指标来刻画视觉连贯性与主题可分性 [12]。在这些方向中，设计原则一贯充当生成与多模态推理的引导信号，却基本未被用作评估设计质量的显式维度。

**EN** Visual grounding with MLLMs. Recent MLLMs [39, 42, 3, 40, 5, 24, 58, 50, 53] have substantially advanced the integration of visual and linguistic understanding, achieving impressive performance in tasks such as referring expression comprehension and segmentation. These models showcase the growing capability of LLMs to perform fine-grained localisation and complex reasoning over visual content. Approaches such as [39, 3, 50] emphasize language-driven grounding by constructing rich contextual representations. Whereas methods like [24, 40, 58, 42, 42] leverage joint vision-language embeddings to generate segmentation masks. Further, [29, 6] explore multi-modal grounding by incorporating audio-visual cues for spatial and temporal understanding. Despite these advances, visual grounding within MLLMs remains largely confined to image- and video-based applications and has yet to be extended to specialized domains such as defect localisation in designs.

**ZH** 基于 MLLM 的视觉定位。近来的 MLLM [39, 42, 3, 40, 5, 24, 58, 50, 53] 大幅推进了视觉与语言理解的融合，在指代表达理解与分割等任务上取得了令人印象深刻的表现。这些模型展示了 LLM 在视觉内容上进行细粒度定位与复杂推理的日益增长的能力。[39, 3, 50] 等方法通过构建丰富的语境表示来强调语言驱动的定位；而 [24, 40, 58, 42] 等方法则利用联合的视觉—语言嵌入来生成分割掩码。此外，[29, 6] 引入视听线索探索多模态定位，以实现空间与时间上的理解。尽管有这些进展，MLLM 中的视觉定位基本仍局限于图像与视频类应用，尚未扩展到设计缺陷定位这样的专门领域。

**EN** 3 Principle-Aware Design Evaluation

**ZH** 3 原则感知的设计评测

**EN** To enable interpretable and principle-specific evaluation of visual design quality, we introduce a principle-aware evaluation framework built upon a curated dataset of controlled layout perturbations. Section 3.1 presents PRISM, a principle-disentangled dataset derived from professional designs that isolates key visual composition principles through targeted modifications. Section 3.2 then describes the scorer and localiser modules that leverage PRISM to quantitatively and spatially assess design violations.

**ZH** 为实现对视觉设计质量的可解释、针对特定原则的评测，我们提出了一个建立在受控版面扰动数据集之上的原则感知评测框架。第 3.1 节介绍 PRISM——一个源自专业设计的原则解耦数据集，它通过有针对性的修改隔离出关键的视觉构成原则。第 3.2 节则描述利用 PRISM 对设计违规做定量与空间化评估的打分器与定位器模块。

<!-- [原子块 · img]  -->

**EN** Figure 4: Using ⟦SLOT_4⟧ PRISM, we build two modules for principle-aware design evaluation: (A) a scorer that quantifies quality across five design principles using controlled perturbations, and (B) a localiser that identifies regions responsible for readability or contrast degradations. A demonstrative editing pipeline (C) operates on the coherence module, where GPT-4o serves as a prompting-based localiser to identify global inconsistencies and propose edits. The pipeline employs a beam search strategy, generating candidate edits from the localiser and selecting the top two (beam size = 2) using the scorer. Together, these components establish a foundation for interpretable, end-to-end design assessment and refinement.

**ZH** 图 4：借助 ⟦SLOT_4⟧ PRISM，我们构建了两个用于原则感知设计评测的模块：(A) 打分器，利用受控扰动在五项设计原则上量化质量；(B) 定位器，识别造成可读性或对比度退化的区域。演示性编辑流水线 (C) 作用于连贯性模块，其中 GPT-4o 充当基于提示的定位器，识别全局不一致并提出编辑。该流水线采用集束搜索策略：由定位器生成候选编辑，再由打分器选出前两个（集束宽度 = 2）。这些组件共同奠定了可解释的端到端设计评估与改进的基础。

**EN** 3.1 ⟦SLOT_5⟧ PRISM: Principle-Disentangled Dataset

**ZH** 3.1 ⟦SLOT_5⟧ PRISM：原则解耦数据集

**EN** To enable interpretable and principle-specific evaluation of visual layouts, we introduce PRISM (PRinciple-aware, Interpretable, and Structure-guided Design Modifications), a curated dataset that disentangles five fundamental principles of design quality: coherence, readability, contrast, alignment, and overlap (See Fig. 1). PRISM is derived from the Crello corpus [52] of professional designs, which provides structured metadata describing each design’s geometry, text attributes, color palette, and so on. This metadata enables controlled perturbations of individual design components while preserving other aspects of composition.

**ZH** 为实现对视觉版面的可解释、针对特定原则的评测，我们提出 PRISM（PRinciple-aware, Interpretable, and Structure-guided Design Modifications）——一个把设计质量的五项基本原则解耦开来的精选数据集：连贯性、可读性、对比度、对齐与遮挡（见图 1）。PRISM 源自 Crello 语料库 [52] 中的专业设计，该语料库提供结构化元数据，描述每个设计的几何信息、文本属性、调色板等。这些元数据使得我们能够对单个设计组件做受控扰动，同时保留构成的其他方面。

**EN** Principle definitions. We define the principles as follows: Coherence measures semantic consistency between textual and visual elements; Readability measures typographic clarity and legibility; Contrast measures perceptual distinctness between overlapping or adjacent regions; Alignment measures geometric regularity of text and element placement; and Overlap measures unintended occlusions between visual components. These definitions serve as the organizing factors guiding the perturbations [46, 19, 26].

**ZH** 原则定义。我们把各项原则定义如下：连贯性衡量文本元素与视觉元素之间的语义一致性；可读性衡量排版的清晰度与易读性；对比度衡量重叠或相邻区域之间的感知可区分度；对齐衡量文本与元素摆放的几何规整性；遮挡衡量视觉组件之间的非预期遮蔽。这些定义构成了指导扰动操作的组织要素 [46, 19, 26]。

**EN** Perturbation methodology. For each principle ⟦SLOT_6⟧, we generate a perturbed layout ⟦SLOT_7⟧, where ⟦SLOT_8⟧ introduces a targeted violation of ⟦SLOT_9⟧ while keeping other principles approximately invariant. Global principles: coherence and alignment require semantic or structural modifications, whereas local principles: readability, contrast, and overlap involve perceptual or spatial adjustments. Across all principles, GPT-4o–based [20] prompting is used to modify textual content, replace icons or background imagery, and suggest RGB color values for altered text and elements. The prompt does not include the poster as a whole but only the required details for edits (Supp.A). In parallel, geometric and typographic attributes such as text-box coordinates, font size, etc are adjusted directly through the Crello metadata, scaled relative to their original values to ensure realistic, layout-consistent perturbations. For local principles, we additionally record the precise set of modified regions and corresponding changes, providing structured supervision that can be used to evaluate or guide localisation-based editing techniques (See Section 3.2.2).

**ZH** 扰动方法。对每个原则 ⟦SLOT_6⟧，我们生成一个扰动版面 ⟦SLOT_7⟧，其中 ⟦SLOT_8⟧ 引入对 ⟦SLOT_9⟧ 的目标违规，同时让其他原则大致保持不变。全局性原则（连贯性与对齐）需要语义或结构上的修改，而局部性原则（可读性、对比度与遮挡）则涉及感知或空间上的调整。在所有原则上，我们都使用基于 GPT-4o [20] 的提示来修改文本内容、替换图标或背景图像，并为改动后的文本与元素给出 RGB 颜色取值建议。提示中并不包含整张海报，只包含编辑所需的细节（附录 A）。与此同时，文本框坐标、字号等几何与排版属性则直接通过 Crello 元数据调整，并按相对原始值的比例缩放，以确保扰动真实且与版面一致。对局部性原则，我们还记录了被修改区域的精确集合及相应改动，提供可用于评估或引导基于定位的编辑技术的结构化监督（见第 3.2.2 节）。

**EN** Example. Figure 3 illustrates representative perturbations. In the coherence example, the text promotes a “dolphin show” while the icons and background depict wristwatches, violating thematic consistency. In the readability example, we intentionally reduced the font size for the word “onedito”, which reduces readability.

**ZH** 示例。图 3 展示了代表性的扰动。在连贯性示例中，文字宣传的是“dolphin show”，而图标与背景描绘的却是腕表，违反了主题一致性。在可读性示例中，我们刻意缩小了“onedito”一词的字号，从而降低了可读性。

**EN** Although complete independence among principles is inherently challenging; each perturbation is constructed to emphasize a single factor with minimal collateral impact on others. The resulting dataset comprises paired composed and perturbed layouts ⟦SLOT_10⟧, enabling quantitative and spatially grounded evaluation of design quality. PRISM is derived from the Crello corpus, which provides approximately 20K training and 2K validation professional designs. Each principle is perturbed independently over this split, yielding about 20K training and 2K validation per principle, and totaling roughly 100K training and 10K validation layout pairs across all five principles.

**ZH** 尽管各原则之间完全独立在本质上难以做到，每次扰动都被构造为突出单一因素、对其他原则的连带影响最小。最终数据集由成对的原始版面与扰动版面 ⟦SLOT_10⟧ 构成，支持对设计质量做定量的、有空间定位的评估。PRISM 源自 Crello 语料库，后者提供约 20K 训练与 2K 验证规模的专业设计。每个原则在该划分上独立施加扰动，每个原则产生约 20K 训练与 2K 验证样本，五项原则合计约 100K 训练与 10K 验证版面对。

**EN** 3.2 Scorer and Localiser Modules

**ZH** 3.2 打分器与定位器模块

**EN** Building on PRISM, we develop two complementary modules for design evaluation. The binary scorers quantitatively assess whether each principle is satisfied in a given layout, while the localiser provides spatially grounded feedback identifying regions responsible for the violation. Together, these components enable fine-grained, interpretable evaluation of visual layouts and serve as inputs for the editing pipeline described in Section 6.

**ZH** 在 PRISM 的基础上，我们开发了两个互补的设计评测模块。二值打分器定量评估给定版面是否满足各条原则；定位器则给出有空间定位的反馈，指出造成违规的区域。二者结合，可对视觉版面做细粒度、可解释的评估，并作为第 6 节所述编辑流水线的输入。

**EN** 3.2.1 Principle-Aware Scorer

**ZH** 3.2.1 原则感知打分器

**EN** We define a collection of principle-aware grounding functions ⟦SLOT_11⟧ that estimate the likelihood that a visual layout satisfies specific design principles, such as readability, contrast, alignment, overlap and coherence. Each grounding function ⟦SLOT_12⟧ operates over a design representation ⟦SLOT_13⟧ and outputs a probability ⟦SLOT_14⟧, quantifying adherence to principle ⟦SLOT_15⟧. Together, these functions provide an interpretable decomposition of overall design quality, mapping a layout’s multimodal embedding space into principle-specific probabilities. This formulation enables a structured and transparent evaluation framework that moves beyond a single, opaque score toward measurable reasoning aligned with human design intuition.

**ZH** 我们定义一组原则感知的评估函数 ⟦SLOT_11⟧，用于估计一个视觉版面满足特定设计原则（如可读性、对比度、对齐、遮挡与连贯性）的可能性。每个评估函数 ⟦SLOT_12⟧ 作用于设计表示 ⟦SLOT_13⟧ 并输出概率 ⟦SLOT_14⟧，量化对原则 ⟦SLOT_15⟧ 的遵循程度。这些函数共同提供了对整体设计质量的可解释分解，把版面的多模态嵌入空间映射为针对特定原则的概率。这一形式化建立起结构化、透明的评测框架，从单一不透明的分数走向与人类设计直觉相一致的可度量推理。

**EN** Design-Aware Fine-tuning. We begin by adapting a pretrained multi-modal encoder to become design-aware, ensuring its visual representations capture structural and compositional cues relevant to layout evaluation. At this stage, only the vision encoder is updated, while the text encoder remains frozen. The model is trained on multi-modal document-caption pairs, where the captions convey the overall design intent of the document. Through this adaptation, the encoder learns layout embeddings that capture spatial arrangement, visual balance, and typographic hierarchy. The resulting design-aware vision encoder produces fixed embeddings ⟦SLOT_16⟧ for all scorers, ensuring consistent and semantically grounded feature representations across principles.

**ZH** 设计感知微调。我们首先让一个预训练的多模态编码器具备设计感知能力，使其视觉表示能够捕捉与版面评估相关的结构和构成线索。这一阶段只更新视觉编码器，文本编码器保持冻结。模型在多模态文档—描述对上训练，其中的描述传达了文档的整体设计意图。通过这一适配，编码器学习到能够捕捉空间排布、视觉平衡与排版层级的版面嵌入。所得的设计感知视觉编码器为所有打分器产出固定的嵌入 ⟦SLOT_16⟧，确保跨原则的特征表示一致且有语义依据。

**EN** PRISM-Scorer. We train independent binary classifiers on top of the frozen design-aware embeddings to estimate whether each design principle ⟦SLOT_17⟧ is satisfied. Given a layout ⟦SLOT_18⟧, the encoder produces ⟦SLOT_19⟧, and the corresponding scorer predicts:

**ZH** PRISM-Scorer。我们在冻结的设计感知嵌入之上训练独立的二值分类器，用以估计每个设计原则 ⟦SLOT_17⟧ 是否被满足。给定版面 ⟦SLOT_18⟧，编码器产出 ⟦SLOT_19⟧，相应的打分器预测：

<!-- [原子块 · table] g p ​ ( x ) = σ ⁡ ( ϕ ​ ( x ) ⊤ ​ W p ) , g_{p}(x)=\sigma(\phi(x)^{\top}W_{p}), (1) -->

**EN** where ⟦SLOT_20⟧ are the learnable weights for principle ⟦SLOT_21⟧, and ⟦SLOT_22⟧ denotes the sigmoid activation. Training uses paired composed and perturbed examples, where each perturbation selectively violates a single design principle. Each scorer is optimized using binary supervision and learns to assign higher probabilities to principle-aligned layout designs and lower probabilities to those designs that are at odds with key design principles. The resulting outputs ⟦SLOT_23⟧ form probabilistic, interpretable scores indicating the degree of adherence to each principle, as illustrated in Fig. 4(A). Collectively, the set of principle-specific functions ⟦SLOT_24⟧ constitutes a structured, interpretable evaluation space that decomposes overall design quality into measurable dimensions aligned with human reasoning.

**ZH** 其中 ⟦SLOT_20⟧ 是原则 ⟦SLOT_21⟧ 的可学习权重，⟦SLOT_22⟧ 表示 sigmoid 激活。训练使用成对的原始与扰动样本，其中每次扰动有选择地违反单一设计原则。每个打分器用二值监督进行优化，学会给符合原则的版面设计赋予更高概率、给与关键设计原则相悖的设计赋予更低概率。所得的输出 ⟦SLOT_23⟧ 构成概率化的、可解释的分数，指示对各原则的遵循程度，如图 4(A) 所示。这些针对特定原则的函数 ⟦SLOT_24⟧ 共同构成了一个结构化的、可解释的评估空间，把整体设计质量分解为与人类推理相一致的可度量维度。

**EN** 3.2.2 Principle-specific Localisation of Errors

**ZH** 3.2.2 针对特定原则的错误定位

**EN** While the binary scorers provide quantitative assessments of whether a design adheres to each principle, they do not reveal where violations occur. To enable spatially and semantically grounded interpretability, we introduce a principle-specific localisation module that evaluates beyond scalar scores. This module identifies the precise visual or textual elements responsible for violating a given design principle, bridging quantitative scoring with qualitative explanation. Localisation is modeled at two complementary levels: (i) a localised component that detects fine-grained perceptual issues such as readability, contrast, and overlap, and (ii) a global component that reasons about higher-level semantic properties such as coherence and alignment.

**ZH** 二值打分器虽能定量评估设计是否遵循各条原则，却不能揭示违规发生在哪里。为实现有空间与语义依据的可解释性，我们引入一个针对特定原则的定位模块，使评估超越标量分数。该模块识别出导致违反某条设计原则的具体视觉或文本元素，在定量打分与定性解释之间架起桥梁。定位在两个互补层次上建模：(i) 局部分量，检测可读性、对比度与遮挡等细粒度感知问题；(ii) 全局分量，对连贯性与对齐等更高层的语义属性进行推理。

**EN** Localised Reasoning for Perceptual Principles. To localise design violations and provide interpretable feedback for perceptual principles such as readability, contrast, and overlap, we fine-tune a vision-language model using structured instruction prompts derived from localised perturbations in PRISM. This module identifies the specific elements within a layout that fail to satisfy a given principle.

**ZH** 面向感知原则的局部推理。为定位设计违规、并针对可读性、对比度与遮挡等感知原则给出可解释反馈，我们利用 PRISM 中局部化扰动导出的结构化指令提示，微调一个视觉语言模型。该模块识别出版面中未能满足给定原则的具体元素。

**EN** During training, each example is formulated as an instruction-based multiple-choice task with explicit candidate options from the metadata. For readability, the input includes the layout image and a list of text elements, each associated with a unique element identifier and its textual content. For contrast and overlap, the input contains pairs of elements that occupy intersecting regions in the design space, also represented by their corresponding IDs. The instruction then prompts the model to select which elements or element pairs violate the specified principle, for example: “Select the text with readability issues due to small font size.” To establish consistent reasoning behavior, we include a system prompt that defines the model’s role and context at the start of every interaction, shown in Fig. 4(B).

**ZH** 训练时，每个样本被表述为一个基于指令的多选题，候选项来自元数据中的显式选项。对可读性，输入包括版面图像与一组文本元素，每个元素关联唯一的元素标识符及其文本内容。对对比度与遮挡，输入包含在设计空间中占据相交区域的元素对，同样以相应 ID 表示。指令随后提示模型选择违反指定原则的元素或元素对，例如：“Select the text with readability issues due to small font size.”。为建立一致的推理行为，我们在每次交互的开头加入定义模型角色与语境的系统提示，如图 4(B) 所示。

**EN** Given an image–instruction pair ⟦SLOT_25⟧ and a finite candidate set ⟦SLOT_26⟧, where each ⟦SLOT_27⟧ denotes an element ID and its associated content, the model predicts a subset ⟦SLOT_28⟧ corresponding to the violating elements:

**ZH** 给定图像—指令对 ⟦SLOT_25⟧ 与有限候选集 ⟦SLOT_26⟧，其中每个 ⟦SLOT_27⟧ 表示一个元素 ID 及其关联内容，模型预测与违规元素相对应的子集 ⟦SLOT_28⟧：

<!-- [原子块 · table] 𝒪 ^ p = Model ​ ( x , c p , 𝒪 ) . \hat{\mathcal{O}}_{p}=\text{Model}(x,c_{p},\mathcal{O}). (2) -->

**EN** Training minimizes the cross-entropy loss between the predicted and ground-truth selections of violating element IDs.

**ZH** 训练最小化预测与真值的违规元素 ID 选择之间的交叉熵损失。

**EN** During inference, the fine-tuned model outputs the list of IDs of the elements that violate the queried principle, without generating free-form text. This design choice constrains the output space to a discrete set of candidates, improving reliability and reproducibility over generative responses.

**ZH** 推理时，微调后的模型输出违反所查询原则的元素 ID 列表，不生成自由文本。这一设计把输出空间约束到离散的候选集合，相比生成式回答提升了可靠性与可复现性。

**EN** Global Reasoning for Semantic Principles. While perceptual principles such as readability, contrast, and overlap can be localised to specific regions, global principles like coherence and alignment require reasoning over the entire layout. PRISM provides structured perturbations for these principles, but a definitive ground truth is not available since multiple valid revisions can achieve coherence or alignment. We therefore use a prompt-based evaluation that checks whether major visual components align with the layout’s inferred theme and structure, enabling holistic assessment of semantic and organizational fidelity.

**ZH** 面向语义原则的全局推理。可读性、对比度与遮挡等感知原则可以定位到具体区域，而连贯性与对齐这类全局原则则需要对整个版面做推理。PRISM 为这些原则提供了结构化扰动，但由于有多种合法修改都能实现连贯或对齐，因此不存在确定的真值。我们因此采用基于提示的评测，检查主要视觉组件是否与版面推断出的主题与结构相符，从而对语义与组织上的保真度做整体评估。

**EN** For instance, while examining coherence, the model first infers the design’s overarching theme (e.g., “Kid’s Birthday Party”) from its textual content and derives representative visual expectations for each component, such as a playful background, festive icons, and bold, cheerful typography. Each component (background, icons, font style, etc.) is then queried using structured prompts to verify alignment with these expectations. This procedure identifies components that visually differ from the inferred theme.

**ZH** 例如，在考察连贯性时，模型先从文本内容推断设计的总体主题（如“Kid’s Birthday Party”），再为每个组件推导出代表性的视觉预期，例如活泼的背景、节庆感的图标，以及醒目、欢快的排版。随后用结构化提示逐一查询每个组件（背景、图标、字体风格等），验证其是否符合这些预期。这一流程识别出在视觉上偏离所推断主题的组件。

**EN** An analogous formulation is applied to alignment, where the model verifies whether elements such as text boxes or icons deviate from the underlying structural grid. The resulting qualitative judgments provide interpretable indicators of global principle violations; not all require correction, and resolving one often restores multiple inconsistencies.

**ZH** 对齐采用类似的形式化：模型检验文本框、图标等元素是否偏离底层的结构网格。所得的定性判断为全局原则违规提供可解释的指示；并非所有违规都需要修正，且解决一处往往能同时消除多处不一致。

<!-- [原子块 · img]  -->

**EN** Figure 5: Human evaluation of principle disentanglement. Average ratings (1–7, 4 = neutral) across 10 poster pairs per principle show strong diagonal responses, confirming that PRISM perturbations primarily affect their intended design principles.

**ZH** 图 5：原则解耦的人工评测。对每项原则 10 对海报的平均评分（1–7，4 为中性）呈现出强烈的对角响应，证实 PRISM 扰动主要影响其预期的设计原则。

**EN** 4 Experimental Setup

**ZH** 4 实验设置

**EN** Our experiments evaluate whether PRISM produces clean, principle-specific degradations and examine how effectively our scorer–localiser framework and contemporary MLLMs detect and respond to these controlled violations.

**ZH** 我们的实验评估 PRISM 是否产生干净的、针对特定原则的退化，并检验我们的打分器—定位器框架以及当代 MLLM 检测并响应这些受控违规的有效程度。

**EN** 4.1 Validating Principle Disentanglement

**ZH** 4.1 验证原则解耦

**EN** To assess whether PRISM perturbations successfully isolate individual design principles, we conduct a controlled human study with 15 participants. Each participant is shown 10 paired examples, where each pair contains a professionally designed poster and its perturbed variant, without indicating which is which. For every pair, three independent participants rate which design better satisfies each of the five principles (coherence, readability, contrast, alignment, and overlap) on a 1–7 rating scale, where 1 indicates the original is much better, 7 indicates the perturbed is much better, and 4 indicates no clear preference. We get the average of three participants for each pair and calculate the mean across all pairs. This measures how selectively each perturbation affects its intended principle.

**ZH** 为评估 PRISM 扰动是否成功隔离出各条设计原则，我们开展了一项有 15 名参与者参加的受控人工研究。每位参与者看到 10 组成对样本，每组包含一张专业设计的海报及其扰动变体，且不指明哪张是原件。对每一组，由三名独立参与者就五项原则（连贯性、可读性、对比度、对齐与遮挡）分别评判哪个设计更好地满足该原则，评分采用 1–7 量表：1 表示原件明显更好，7 表示扰动版明显更好，4 表示无明显偏好。我们取三名参与者对每组的平均分，再对所有组求均值。这衡量了每次扰动影响其目标原则的选择性程度。

<!-- [原子块 · object]  -->

**EN** Figure 6: Qualitative results. (A) PRISM-Scorer outputs. The left image in each pair is the original layout and the right shows its PRISM perturbation, with scores indicating the predicted principle-specific degradation. (B) Localiser outputs from the Qwen-2.5-VL instruct-tuned model. The highlighted text specifies the targeted principle and the sub-aspect being queried. For example, in readability we prompt the model to attend specifically to small font-size regions that impair clarity.

**ZH** 图 6：定性结果。(A) PRISM-Scorer 的输出。每对图中左侧为原始版面，右侧为其 PRISM 扰动，分数指示预测出的针对特定原则的退化。(B) 经指令微调的 Qwen-2.5-VL 模型的定位器输出。高亮文本指明目标原则与被查询的子方面。例如在可读性上，我们提示模型专门关注损害清晰度的小字号区域。

**EN** 4.2 Training of Principle-Aware Scorers

**ZH** 4.2 原则感知打分器的训练

**EN** Each principle-specific scorer is trained on a design-aware SigLIP-v2 vision encoder [49], following the setup in Section 3.2.1. The encoder is adapted using the training splits of the Creatidesign [55] and Crello [52] datasets, containing 400K and 20K layout–caption pairs. Captions describing each poster’s theme and composition are generated with GPT-4o [20]. Only the vision encoder is updated in this stage, enabling it to capture structural, spatial, and typographic cues relevant to layout understanding.

**ZH** 每个针对特定原则的打分器都在设计感知的 SigLIP-v2 视觉编码器 [49] 上训练，设置遵循第 3.2.1 节。编码器用 Creatidesign [55] 与 Crello [52] 数据集的训练划分进行适配，二者分别包含 400K 与 20K 版面—描述对。描述每张海报主题与构成的说明文字由 GPT-4o [20] 生成。这一阶段只更新视觉编码器，使其能够捕捉与版面理解相关的结构、空间与排版线索。

**EN** Using the frozen encoder, we train five binary classifiers, one for each design principle, to distinguish between composed and perturbed layouts. Each scorer is trained and evaluated on balanced sets comprising composed layouts from the Crello dataset and their corresponding perturbations from the PRISM dataset, using 40K images for training and 4K for testing. A 90–10 split is used for validation within the training set. Training employs binary cross-entropy loss, with model selection based on validation AUC, and early stopping is applied after seven consecutive non-improving epochs. We report Precision, Recall, F1, and AUC to quantify scorer performance across principles.

**ZH** 在冻结编码器之上，我们训练五个二值分类器，每个对应一条设计原则，用于区分原始版面与扰动版面。每个打分器在平衡集合上训练与评估，集合由来自 Crello 数据集的原始版面与来自 PRISM 数据集的相应扰动构成，使用 40K 张图像训练、4K 张测试。训练集内部按 90–10 划分用于验证。训练采用二值交叉熵损失，依据验证集 AUC 选择模型，并在连续七个轮次无改善后早停。我们报告精确率、召回率、F1 与 AUC，以量化各原则上的打分器性能。

**EN** 4.3 Model Sensitivity to PRISM Perturbations

**ZH** 4.3 模型对 PRISM 扰动的敏感度

**EN** To assess how well different models capture principle-specific degradations, we evaluate four systems on PRISM: GPT-4o, GPT-4o-mini, Qwen-2.5-VL (7B) [1], and our principle-aware PRISM-scorer. For each design principle, we sample 200 examples (100 composed–perturbed pairs). Each model is queried to provide ratings for all five principles for every poster. We then compute the mean score for original and perturbed designs separately, and take their absolute difference (⟦SLOT_29⟧) as a measure of sensitivity to that perturbation. A higher ⟦SLOT_30⟧ indicates stronger discrimination between high- and low-quality designs for that principle. Refer to Supp. for prompt details.

**ZH** 为评估不同模型捕捉针对特定原则退化的能力，我们在 PRISM 上评测了四个系统：GPT-4o、GPT-4o-mini、Qwen-2.5-VL（7B）[1]，以及我们的原则感知 PRISM-Scorer。对每条设计原则，我们采样 200 个样本（100 组原始—扰动对）。每个模型被要求为每张海报的五项原则打分。我们分别计算原始设计与扰动设计的平均分，并取二者之差的绝对值（⟦SLOT_29⟧）作为对该扰动敏感度的度量。⟦SLOT_30⟧ 越高，说明该模型在该原则上区分高质量与低质量设计的能力越强。提示细节见补充材料。

**EN** 4.4 Training of Localiser

**ZH** 4.4 定位器的训练

**EN** We instruct-tune Qwen-2.5-VL (7B) using the localised annotations from the PRISM dataset, following the formulation described in Section 3.2.2. This experiment is conducted only for the readability, contrast, and overlap principles, as these can be spatially localised to specific text or visual elements within the layout. For each layout, the model predicts a set ⟦SLOT_31⟧ of elements that violate the targeted principle, which is compared against the ground-truth set ⟦SLOT_32⟧ from PRISM. True positives (⟦SLOT_33⟧) correspond to elements present in both ⟦SLOT_34⟧ and ⟦SLOT_35⟧, false positives (⟦SLOT_36⟧) to elements in ⟦SLOT_37⟧ but not in ⟦SLOT_38⟧, and false negatives (⟦SLOT_39⟧) to elements in ⟦SLOT_40⟧ but missing from ⟦SLOT_41⟧. We compute Precision, Recall, and F1-score based on these counts, and Intersection-over-Union (IoU) using the sets to evaluate localization accuracy. To ensure consistency across models, we use the same system prompt for all baselines and instruct-tuned variants. Instruct-tuning is performed with one LoRA adapter [18] per principle, allowing independent specialization for readability, contrast, and overlap. We compare the instruct-tuned Qwen-2.5-VL model against three baselines: the pretrained Qwen-2.5-VL (base) model, a few-shot (3-shot) prompted version using the same instruction template, GPT-4o-mini, and GPT-4o queried with equivalent localised prompts. This comparison evaluates how PRISM perturbations enhance localisation.

**ZH** 我们使用 PRISM 数据集中的局部化标注对 Qwen-2.5-VL（7B）做指令微调，形式化如第 3.2.2 节所述。该实验只针对可读性、对比度与遮挡三项原则，因为它们可以在版面内被空间定位到具体的文本或视觉元素。对每个版面，模型预测违反目标原则的元素集合 ⟦SLOT_31⟧，并与 PRISM 的真值集合 ⟦SLOT_32⟧ 比较。真阳性（⟦SLOT_33⟧）对应同时出现在 ⟦SLOT_34⟧ 与 ⟦SLOT_35⟧ 中的元素；假阳性（⟦SLOT_36⟧）对应出现在 ⟦SLOT_37⟧ 但不在 ⟦SLOT_38⟧ 中的元素；假阴性（⟦SLOT_39⟧）对应出现在 ⟦SLOT_40⟧ 但缺失于 ⟦SLOT_41⟧ 中的元素。我们基于这些计数计算精确率、召回率与 F1 分数，并用集合计算交并比（IoU）来评估定位精度。为保证各模型之间的一致性，我们对所有基线与指令微调变体使用相同的系统提示。指令微调为每条原则使用一个 LoRA 适配器 [18]，使可读性、对比度与遮挡能够各自独立地专门化。我们把指令微调后的 Qwen-2.5-VL 模型与三个基线比较：预训练的 Qwen-2.5-VL（base）模型、使用相同指令模板的少样本（3-shot）提示版本、GPT-4o-mini，以及用等价局部化提示查询的 GPT-4o。这一比较检验了 PRISM 扰动对定位能力的提升作用。

<!-- [原子块 · table] PRISM-scorer Precision ↑ \uparrow Recall ↑ \uparrow F1-score ↑ \uparrow AUC ↑ \uparrow Coherence 0.7243 0.7279 0.7262 0.7983 Readability 0.7336 0.7323 0.7329 0.8064 Contrast 0.7552 0.7486 0.7519 0.829 -->

**EN** Table 1: Performance of PRISM binary scorers. Results on the held-out validation set showing Precision, Recall, F1, and AUC for each design principle.

**ZH** 表 1：PRISM 二值打分器的性能。留出验证集上各设计原则的精确率、召回率、F1 与 AUC。

<!-- [原子块 · object]  -->

**EN** Figure 7: Model sensitivity to PRISM perturbations. Radar plots show average rating differences (⟦SLOT_42⟧) between composed and perturbed posters across principles. Our PRISM scorer demonstrates the strongest and most principle-specific sensitivity.

**ZH** 图 7：模型对 PRISM 扰动的敏感度。雷达图展示了各原则上原始海报与扰动海报之间的平均评分差异（⟦SLOT_42⟧）。我们的 PRISM 打分器表现出最强且最具原则针对性的敏感度。

<!-- [原子块 · table] Model Readability Contrast Overlap IoU ↑ \uparrow Precision ↑ \uparrow Recall ↑ \uparrow F1-score ↑ \uparrow IoU ↑ \uparrow Precision ↑ \uparrow Recall ↑ \uparrow F1-score ↑ \uparrow IoU ↑ \uparrow Pr -->

**EN** Table 2: Localisation performance across principles. Fine-tuning Qwen-2.5-VL with PRISM annotations leads to substantial improvements in IoU and F1 across readability, contrast, and overlap compared to base, prompted, GPT-4o-mini and GPT-4o.

**ZH** 表 2：各原则上的定位性能。用 PRISM 标注微调 Qwen-2.5-VL 后，在可读性、对比度与遮挡上的 IoU 与 F1 相比 base、提示版本、GPT-4o-mini 与 GPT-4o 均有大幅提升。

**EN** 5 Main Results

**ZH** 5 主要结果

**EN** All analyses use the PRISM held-out validation split to assess responses to principle-specific degradations.

**ZH** 所有分析都使用 PRISM 的留出验证划分，以评估模型对针对特定原则退化的响应。

**EN** 5.1 Principle Disentanglement: Human Evaluation

**ZH** 5.1 原则解耦：人工评测

**EN** Figure 5 displays average human ratings across perturbation types and design principles. Diagonal scores are below the neutral midpoint of 4, indicating a strong preference for original designs over perturbed ones. For instance, coherence perturbations averaged 1.3 (coherence score), confirming their impact on thematic consistency. Off-diagonal ratings remained near 4, showing minimal effects on unrelated principles. We also observe a correlation between readability and contrast, and between alignment and overlap, which reflects the natural perceptual coupling among these visual attributes. These results show that PRISM perturbations introduce controlled, interpretable degradations that are perceptually distinct across design principles.

**ZH** 图 5 展示了各扰动类型与各设计原则上的人工平均评分。对角线上的分数低于中性中点 4，表明参与者明显偏好原始设计而非扰动版本。例如，连贯性扰动在连贯性评分上平均为 1.3，证实其对主题一致性确有影响。非对角线上的评分则保持在 4 附近，说明对无关原则的影响很小。我们还观察到可读性与对比度之间、以及对齐与遮挡之间存在相关性，这反映了这些视觉属性之间天然的感知耦合。这些结果说明，PRISM 扰动引入了受控的、可解释的退化，并且在不同设计原则之间具有感知上的可区分性。

**EN** 5.2 PRISM Scorer: Performance & Sensitivity

**ZH** 5.2 PRISM 打分器：性能与敏感度

**EN** We first evaluate the PRISM binary scorers on the held-out validation set to assess their reliability across design principles. Qualitative examples illustrating these scorer responses are described in Figure 6(A). As shown in Table 1, the scorers achieve moderate but consistent performance, with F1-scores ranging between 0.72 and 0.76 and AUC values between 0.80 and 0.82. While these results do not reflect perfect classification accuracy, the objective of the scorers is to achieve stable and interpretable sensitivity to principle-specific degradations, rather than absolute predictive performance. This sensitivity makes the scorers reliable quantitative indicators of principle-specific degradations.

**ZH** 我们首先在留出验证集上评测 PRISM 二值打分器，以检验其在各设计原则上的可靠性。图 6(A) 描述了展示这些打分器响应的定性示例。如表 1 所示，打分器取得了中等但稳定的性能：F1 分数在 0.72 至 0.76 之间，AUC 在 0.80 至 0.82 之间。虽然这些结果并未反映完美的分类精度，但打分器的目标是获得对针对特定原则退化的稳定、可解释的敏感度，而非绝对的分类性能。这种敏感度使打分器成为针对特定原则退化的可靠定量指标。

**EN** Figure 7 visualizes model sensitivities across principles using radar plots. Each plot corresponds to one perturbation type and shows the absolute change in model ratings between composed and perturbed posters. The PRISM scorers exhibit the most principle-aligned behavior, responding strongly along the targeted dimension while remaining stable elsewhere. As each scorer is only trained on one specific principle, all other principles represent out-of-domain data. GPT-4o captures overall degradation trends but does not disentangle individual principles, and GPT-4o-mini and Qwen-2.5-VL show weaker, noisier responses. These findings indicate that the PRISM scorers capture fine-grained degradations and provide a basis for principle-aware evaluation of visual design quality. (Refer to Supp for additional OOD experiments).

**ZH** 图 7 用雷达图可视化了各模型在各原则上的敏感度。每张图对应一种扰动类型，展示模型在原始海报与扰动海报之间评分的绝对变化。PRISM 打分器表现出最符合原则预期的行为：在目标维度上响应强烈，同时在其他维度上保持稳定。由于每个打分器只在单一原则上训练，其余原则对它而言都是分布外数据。GPT-4o 能捕捉整体退化趋势，却无法把各条原则解耦开来；GPT-4o-mini 与 Qwen-2.5-VL 的响应更弱且噪声更大。这些发现说明，PRISM 打分器能够捕捉细粒度退化，并为视觉设计质量的原则感知评测提供依据。（更多分布外实验见补充材料。）

**EN** 5.3 PRISM: Localised Error Detection

**ZH** 5.3 PRISM：局部化错误检测

**EN** Table 2 presents the localisation performance across the readability, contrast, and overlap principles. Instruct-tuning Qwen-2.5-VL with PRISM annotations substantially improves performance over the base, prompted, and GPT-based models, achieving the highest IoU and F1-scores across all principles. The instruct-tuned model achieves an average F1 score of 0.80 for readability, 0.72 for contrast, and 0.77 for overlap, demonstrating its ability to identify localised design violations accurately substantially outperforming GPT-4o which demonstrates moderate localisation ability but tends to produce less precise predictions. GPT-4o-mini and prompted Qwen-2.5-VL exhibit weaker and noisier trends. These results show that principle-specific fine-tuning with PRISM supervision leads to more interpretable and spatially grounded reasoning for detecting localised degradations. We also provide qualitative localiser outputs for these principles in Figure 6(B).

**ZH** 表 2 给出了在可读性、对比度与遮挡三项原则上的定位性能。用 PRISM 标注对 Qwen-2.5-VL 做指令微调，相比 base、提示版本与基于 GPT 的模型有大幅提升，在所有原则上都取得最高的 IoU 与 F1。指令微调后的模型在可读性上平均 F1 为 0.80，对比度为 0.72，遮挡为 0.77，说明它能够准确识别局部化的设计违规，大幅优于 GPT-4o——后者表现出中等的定位能力，但预测往往不够精确。GPT-4o-mini 与提示版 Qwen-2.5-VL 呈现更弱、噪声更大的趋势。这些结果表明，借助 PRISM 监督做针对特定原则的微调，能够带来更可解释、更具空间依据的推理，用于检测局部化退化。我们还在图 6(B) 中给出了这些原则上的定性定位器输出。

<!-- [原子块 · table] Score:0.19 Score: 0.62 Score: 0.66 (a) Incoherent Design (b) Background replaced (c) Irrelevant Iconremoved -->

**EN** Figure 8: Demonstrative coherence editing pipeline. Starting from an incoherent design (a) from the PRISM dataset, the model iteratively refines the layout guided by the coherence scorer and localiser. The first edit (b) replaces the mismatched background with a theme-consistent image, while the second edit (c) removes the irrelevant watch icon. The coherence score increases from 0.19 ⟦SLOT_43⟧ 0.62 ⟦SLOT_44⟧ 0.66, reflecting improved thematic consistency.

**ZH** 图 8：连贯性编辑流水线演示。从 PRISM 数据集中一张不连贯的设计 (a) 出发，模型在连贯性打分器与定位器的引导下迭代改进版面。第一次编辑 (b) 把不匹配的背景替换为与主题一致的图像，第二次编辑 (c) 移除了无关的手表图标。连贯性分数从 0.19 ⟦SLOT_43⟧ 0.62 ⟦SLOT_44⟧ 0.66 逐步上升，反映出主题一致性的改善。

**EN** 6 Demonstrative Editing Pipeline

**ZH** 6 演示性编辑流水线

**EN** To illustrate a possible utility of our framework, we implement a demonstrative editing pipeline for the coherence principle using a beam search-based strategy [44]. The pipeline uses feedback from the scorer and localisation modules to propose and evaluate principle-aware refinements, as introduced in Fig. 4(C). At each iteration, the localisation module identifies elements contributing to incoherence and helping generate candidate edits through prompt-based reasoning. Each candidate layout addresses one of the identified inconsistencies, yielding multiple alternative paths for editing. The coherence scorer re-evaluates these candidates, and the top-⟦SLOT_45⟧ candidates (with a beam size ⟦SLOT_46⟧) achieving the highest coherence scores are retained for subsequent iterations. Unlike direct modifications from MLLMs, this pipeline preserves the underlying layout structure and retains the design’s editability throughout the refinement process. See Fig. 8 for an illustrative example, demonstrating how interpretable feedback enables targeted, principle-specific refinements in visual design.

**ZH** 为展示我们框架的一种可能用途，我们针对连贯性原则实现了一条演示性编辑流水线，采用基于集束搜索的策略 [44]。该流水线利用打分器与定位模块的反馈来提出并评估原则感知的改进，如图 4(C) 所示。在每一轮迭代中，定位模块识别出导致不连贯的元素，并通过基于提示的推理帮助生成候选编辑。每个候选版面针对所识别出的某一处不一致，从而产生多条可供选择的编辑路径。连贯性打分器对这些候选重新评估，保留连贯性分数最高的前 ⟦SLOT_45⟧ 个候选（集束宽度 ⟦SLOT_46⟧）进入下一轮迭代。与 MLLM 直接修改不同，这条流水线保留了底层版面结构，并在整个改进过程中维持设计的可编辑性。图 8 给出了一个示意性示例，展示可解释反馈如何实现视觉设计中有针对性的、针对特定原则的改进。

**EN** 7 Conclusions and Future Work

**ZH** 7 结论与未来工作

**EN** Conclusions. We introduce ⟦SLOT_47⟧ PRISM, a principle-disentangled benchmark and a multi-scale evaluation framework for interpretable reasoning of visual designs. PRISM enables consistent comparison of disentanglement skills by introducing a principle-aware perturbed dataset. We combine lightweight scorers and instruction-tuned models for localising errors, which can be used to propose targeted edits. These components lay a foundation for future multimodal systems that can diagnose, explain, and improve visual layouts aligned with human designers.

**ZH** 结论。我们提出 ⟦SLOT_47⟧ PRISM——一个原则解耦的基准，以及一个用于视觉设计可解释推理的多尺度评测框架。PRISM 通过引入原则感知的扰动数据集，使解耦能力的比较得以一致地开展。我们把轻量级打分器与用于定位错误的指令微调模型结合起来，它们可被用于提出有针对性的编辑。这些组件为未来的多模态系统奠定了基础，使其能够像人类设计师那样诊断、解释并改进视觉版面。

**EN** Future Work. While PRISM offers controlled principle-specific perturbations, there are several opportunities for improvement. First, the assumption of strict principle independence is inexact (for instance, readability and contrast can influence one another). A possible avenue for future work is to model such interactions more explicitly. Second, current coherence assessments rely on prompt-based judgments that vary across generative models; greater robustness may be achieved through multiple annotators, more stable prompting strategies, or the incorporation of theme-level annotations. Third, the editing pipeline could be extended to support vector-level edits. Finally, the scorer and localiser can double as reward functions for RLHF- or DPO-style [35, 41] training, allowing models to learn scoring, localisation, and editing, holistically.

**ZH** 未来工作。PRISM 虽提供了受控的、针对特定原则的扰动，仍有若干改进空间。第一，严格的原则独立性假设并不精确（例如可读性与对比度会相互影响），未来工作的一条可能路径是更显式地建模这类交互。第二，当前的连贯性评估依赖基于提示的判断，而这些判断随生成模型而变；可以通过引入多名标注者、更稳定的提示策略，或加入主题层级的标注来获得更强的稳健性。第三，编辑流水线可以扩展以支持矢量层级的编辑。最后，打分器与定位器可以兼作 RLHF 或 DPO 类 [35, 41] 训练的奖励函数，使模型整体地学习打分、定位与编辑。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] [1] S. Bai, K. Chen, X. Liu, J. Wang, W. Ge, S. Song, K. Dang, P. Wang, S. Wang, J. Tang, et al. (2025) Qwen2. 5-vl technical report . arXiv preprint arXiv:2502.13923 . Cited by: §1 , §4.3 . -->

<!-- [原子块 · verbatim] [2] M. Bauerly and Y. Liu (2006) Computational modeling and experimental investigation of effects of compositional elements on interface and design aesthetics . Int. J. Hum. Comput. Stud. 64 ( 8 ), pp -->

<!-- [原子块 · verbatim] [3] K. Chen, Z. Zhang, W. Zeng, R. Zhang, F. Zhu, and R. Zhao (2023) Shikra: unleashing multimodal llm’s referential dialogue magic . arXiv preprint arXiv:2306.15195 . Cited by: §2 . -->

<!-- [原子块 · verbatim] [4] X. Chen, X. Wang, S. Changpinyo, A. Piergiovanni, P. Padlewski, D. Salz, S. Goodman, A. Grycner, B. Mustafa, L. Beyer, A. Kolesnikov, J. Puigcerver, N. Ding, K. Rong, H. Akbari, G. Mishra, L. Xue, -->

<!-- [原子块 · verbatim] [5] S. Chowdhury, M. Elmoghany, Y. Abeysinghe, J. Fei, S. Nag, S. Khan, M. Elhoseiny, and D. Manocha (2025) MAGNET: a multi-agent framework for finding audio-visual needles by reasoning over multi-vid -->

<!-- [原子块 · verbatim] [6] S. Chowdhury, S. Nag, S. Dasgupta, J. Chen, M. Elhoseiny, R. Gao, and D. Manocha (2024) Meerkat: audio-visual large language model for grounding in space and time . In European Conference on Compu -->

<!-- [原子块 · verbatim] [7] C. Deng, D. Zhu, K. Li, C. Gou, F. Li, Z. Wang, S. Zhong, W. Yu, X. Nie, Z. Song, G. Shi, and H. Fan (2025) Emerging properties in unified multimodal pretraining . External Links: 2505.14683 , Lin -->

<!-- [原子块 · verbatim] [8] A. Dosovitskiy, L. Beyer, A. Kolesnikov, D. Weissenborn, X. Zhai, T. Unterthiner, M. Dehghani, M. Minderer, G. Heigold, S. Gelly, J. Uszkoreit, and N. Houlsby (2021) An image is worth 16x16 words: -->

<!-- [原子块 · verbatim] [9] Q. Dou, X. S. Zheng, T. Sun, and P. Heng (2019) Webthetics: quantifying webpage aesthetics with deep learning . Int. J. Hum. Comput. Stud. 124 , pp. 56–66 . External Links: Link , Document Cited b -->

<!-- [原子块 · verbatim] [10] P. Duan, C. Cheng, G. Li, B. Hartmann, and Y. Li (2024) Uicrit: enhancing automated design evaluation with a ui critique dataset . In Proceedings of the 37th Annual ACM Symposium on User Interfac -->

<!-- [原子块 · verbatim] [11] H. et al. Can gpts evaluate graphic design based on design principles? . In SIGGRAPH Asia 2024 , T. Igarashi and R. Hu (Eds.) , External Links: Link , Document Cited by: Appendix E . -->

<!-- [原子块 · verbatim] [12] F. Gonz’alez-Pizarro and G. Carenini (2024) Neural multimodal topic modeling: a comprehensive evaluation . ArXiv abs/2403.17308 . External Links: Link Cited by: §2 . -->

<!-- [原子块 · verbatim] [13] S. Goyal, A. Mahajan, S. Mishra, P. Udhayanan, T. Shukla, K. Joseph, and B. V. Srinivasan (2025) Design-o-meter: towards evaluating and refining graphic designs . Cited by: §1 , §2 . -->

<!-- [原子块 · verbatim] [14] D. Haraguchi, N. Inoue, W. Shimoda, H. Mitani, S. Uchida, and K. Yamaguchi (2024) Can gpts evaluate graphic design based on design principles? . In SIGGRAPH Asia 2024 Technical Communications, SA -->

<!-- [原子块 · verbatim] [15] S. J. Harrington, J. F. Naveda, R. P. Jones, P. G. Roetling, and N. Thakkar (2004) Aesthetic measures for automated document layout . In Proceedings of the 2004 ACM Symposium on Document Engineer -->

<!-- [原子块 · verbatim] [16] D. Horita, N. Inoue, K. Kikuchi, K. Yamaguchi, and K. Aizawa (2023) Retrieval-augmented layout transformer for content-aware layout generation . 2024 IEEE/CVF Conference on Computer Vision and Pa -->

<!-- [原子块 · verbatim] [17] H. Hsu, X. He, Y. Peng, H. Kong, and Q. Zhang (2023) PosterLayout: a new benchmark and approach for content-aware visual-textual presentation layout . External Links: 2303.15937 , Link Cited by:  -->

<!-- [原子块 · verbatim] [18] E. J. Hu, Y. Shen, P. Wallis, Z. Allen-Zhu, Y. Li, S. Wang, L. Wang, and W. Chen (2021) LoRA: low-rank adaptation of large language models . External Links: 2106.09685 , Link Cited by: §4.4 . -->

<!-- [原子块 · verbatim] [19] D. Huang, J. Guo, S. Sun, H. Tian, J. Lin, Z. Hu, C. Lin, J. Lou, and D. Zhang (2023) A survey for graphic design intelligence . arXiv preprint arXiv:2309.01371 . Cited by: §1 , §3.1 . -->

<!-- [原子块 · verbatim] [20] A. Hurst, A. Lerer, A. P. Goucher, A. Perelman, A. Ramesh, A. Clark, A. Ostrow, A. Welihinda, A. Hayes, A. Radford, et al. (2024) Gpt-4o system card . arXiv preprint arXiv:2410.21276 . Cited by:  -->

<!-- [原子块 · verbatim] [21] G. Ilharco, M. Wortsman, R. Wightman, C. Gordon, N. Carlini, R. Taori, A. Dave, V. Shankar, B. Recht, S. Kumar, L. Schmidt, and A. Ross (2021) OpenCLIP . Zenodo . External Links: Document , Link  -->

<!-- [原子块 · verbatim] [22] P. Jia, C. Li, Z. Liu, Y. Shen, X. Chen, Y. Yuan, Y. Zheng, D. Chen, J. Li, X. Xie, S. Zhang, and B. Guo (2023) COLE: A hierarchical generation framework for graphic design . CoRR abs/2311.16974  -->

<!-- [原子块 · verbatim] [23] W. Kong, Z. Jiang, S. Sun, Z. Guo, W. Cui, T. Liu, J. Lou, and D. Zhang (2023) Aesthetics++: refining graphic designs by exploring design principles and human preference . IEEE Trans. Vis. Comput -->

<!-- [原子块 · verbatim] [24] X. Lai, Z. Tian, Y. Chen, Y. Li, Y. Yuan, S. Liu, and J. Jia (2023) Lisa: reasoning segmentation via large language model . arXiv preprint arXiv:2308.00692 . Cited by: §2 . -->

<!-- [原子块 · verbatim] [25] J. Li, J. Yang, J. Zhang, C. Liu, C. Wang, and T. Xu (2020) Attribute-conditioned layout gan for automatic graphic design . IEEE Transactions on Visualization and Computer Graphics 27 , pp. 4039– -->

<!-- [原子块 · verbatim] [26] W. Lidwell, K. Holden, and J. Butler (2010) Universal principles of design . Second Edition edition , Rockport Publishers . Cited by: §3.1 . -->

<!-- [原子块 · verbatim] [27] C. Lin, Y. Lin, P. Pan, X. Zhang, and Y. Mu (2024) InstructLayout: instruction-driven 2d and 3d layout synthesis with semantic graph prior . IEEE Transactions on Pattern Analysis and Machine Inte -->

<!-- [原子块 · verbatim] [28] S. Lok and S. K. Feiner (2005) A survey of automated layout techniques for information presentations . External Links: Link Cited by: §2 . -->

<!-- [原子块 · verbatim] [29] S. Munasinghe, R. Thushara, M. Maaz, H. A. Rasheed, S. Khan, M. Shah, and F. Khan (2023) Pg-video-llava: pixel grounding large video-language models . arXiv preprint arXiv:2311.13435 . Cited by:  -->

<!-- [原子块 · verbatim] [30] S. Nag, K. Joseph, K. Goswami, V. I. Morariu, and B. V. Srinivasan (2025) Agentic design review system . arXiv preprint arXiv:2508.10745 . Cited by: §1 , §1 , §2 . -->

<!-- [原子块 · verbatim] [31] D. C. L. Ngo, L. S. Teo, and J. G. Byrne (2000) A mathematical theory of interface aesthetics . In Visual mathematics , Vol. 2 . Cited by: §2 . -->

<!-- [原子块 · verbatim] [32] OpenAI (2024) GPT-4o mini . Note: https://openai.com Accessed: 2025-02-13 Cited by: §1 . -->

<!-- [原子块 · verbatim] [33] M. Oquab, T. Darcet, T. Moutakanni, H. Vo, M. Szafraniec, V. Khalidov, P. Fernandez, D. Haziza, F. Massa, A. El-Nouby, M. Assran, N. Ballas, W. Galuba, R. Howes, P. Huang, S. Li, I. Misra, M. Rab -->

<!-- [原子块 · verbatim] [34] M. Otani, N. Inoue, K. Kikuchi, and R. Togashi (2024) Ltsim: layout transportation-based similarity measure for evaluating layout generation . arXiv preprint arXiv:2407.12356 . Cited by: §1 . -->

<!-- [原子块 · verbatim] [35] L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. L. Wainwright, P. Mishkin, C. Zhang, S. Agarwal, K. Slama, A. Ray, J. Schulman, J. Hilton, F. Kelton, L. Miller, M. Simens, A. Askell, P. Welinder, P. C -->

<!-- [原子块 · verbatim] [36] P. O’Donovan, A. Agarwala, and A. Hertzmann (2014) Learning layouts for single-pagegraphic designs . IEEE transactions on visualization and computer graphics 20 ( 8 ), pp. 1200–1213 . Cited by: § -->

<!-- [原子块 · verbatim] [37] P. O’Donovan, A. Agarwala, and A. Hertzmann (2015) DesignScape: design with interactive layout suggestions . Proceedings of the 33rd Annual ACM Conference on Human Factors in Computing Systems .  -->

<!-- [原子块 · verbatim] [38] S. Patnaik, R. Jain, B. Krishnamurthy, and M. Sarkar (2025) AesthetiQ: enhancing graphic layout design via aesthetic-aware preference alignment of multi-modal large language models . External Lin -->

<!-- [原子块 · verbatim] [39] Z. Peng, W. Wang, L. Dong, Y. Hao, S. Huang, S. Ma, and F. Wei (2023) Kosmos-2: grounding multimodal large language models to the world . arXiv preprint arXiv:2306.14824 . Cited by: §2 . -->

<!-- [原子块 · verbatim] [40] S. Pramanick, G. Han, R. Hou, S. Nag, S. Lim, N. Ballas, Q. Wang, R. Chellappa, and A. Almahairi (2024) Jack of all tasks master of many: designing general-purpose coarse-to-fine vision-language  -->

<!-- [原子块 · verbatim] [41] R. Rafailov, A. Sharma, E. Mitchell, S. Ermon, C. D. Manning, and C. Finn (2024) Direct preference optimization: your language model is secretly a reward model . External Links: 2305.18290 , Link -->

<!-- [原子块 · verbatim] [42] H. Rasheed, M. Maaz, S. Shaji, A. Shaker, S. Khan, H. Cholakkal, R. M. Anwer, E. Xing, M. Yang, and F. S. Khan (2023) GLaMM: pixel grounding large multimodal model . arXiv preprint arXiv:2311.033 -->

<!-- [原子块 · verbatim] [43] O. Russakovsky, J. Deng, H. Su, J. Krause, S. Satheesh, S. Ma, Z. Huang, A. Karpathy, A. Khosla, M. Bernstein, A. C. Berg, and L. Fei-Fei (2015) ImageNet large scale visual recognition challenge  -->

<!-- [原子块 · verbatim] [44] C. Shi, H. Yang, D. Cai, Z. Zhang, Y. Wang, Y. Yang, and W. Lam (2024) A thorough examination of decoding methods in the era of llms . arXiv preprint arXiv:2402.06925 . Cited by: §1 , §6 . -->

<!-- [原子块 · verbatim] [45] Y. Shi, M. Shang, and Z. Qi (2023) Intelligent layout generation based on deep generative models: a comprehensive survey . Inf. Fusion 100 , pp. 101940 . External Links: Link Cited by: §2 . -->

<!-- [原子块 · verbatim] [46] K. Son, D. Choi, T. S. Kim, and J. Kim (2024) Demystifying tacit knowledge in graphic design: characteristics, instances, approaches, and guidelines . In Proceedings of the 2024 CHI Conference on -->

<!-- [原子块 · verbatim] [47] M. Suri, P. Mathur, F. Dernoncourt, R. Jain, V. I. Morariu, R. Sawhney, P. Nakov, and D. Manocha (2024) DocEdit-v2: document structure editing via multimodal llm grounding . In Conference on Empi -->

<!-- [原子块 · verbatim] [48] S. Tabata, H. Yoshihara, H. Maeda, and K. Yokoyama (2019) Automatic layout generation for graphical design magazines . In Special Interest Group on Computer Graphics and Interactive Techniques Co -->

<!-- [原子块 · verbatim] [49] M. Tschannen, A. Gritsenko, X. Wang, M. F. Naeem, I. Alabdulmohsin, N. Parthasarathy, T. Evans, L. Beyer, Y. Xia, B. Mustafa, et al. (2025) Siglip 2: multilingual vision-language encoders with im -->

<!-- [原子块 · verbatim] [50] W. Wang, M. Shi, Q. Li, W. Wang, Z. Huang, L. Xing, Z. Chen, H. Li, X. Zhu, Z. Cao, et al. (2023) The all-seeing project: towards panoptic visual recognition and understanding of the open world . -->

<!-- [原子块 · verbatim] [51] S. Xue, B. Jin, J. Jiang, L. Guo, and J. Liu (2024) A hybrid local-global neural network for visual classification using raw eeg signals . Scientific Reports 14 . External Links: Link Cited by: § -->

<!-- [原子块 · verbatim] [52] K. Yamaguchi (2021) Canvasvae: learning to generate vector graphic documents . In Proceedings of the IEEE/CVF International Conference on Computer Vision , pp. 5481–5489 . Cited by: Appendix C ,  -->

<!-- [原子块 · verbatim] [53] H. You, H. Zhang, Z. Gan, X. Du, B. Zhang, Z. Wang, L. Cao, S. Chang, and Y. Yang (2023) Ferret: refer and ground anything anywhere at any granularity . arXiv preprint arXiv:2310.07704 . Cited by -->

<!-- [原子块 · verbatim] [54] M. Zen and J. Vanderdonckt (2014) Towards an evaluation of graphical user interfaces aesthetics based on metrics . In IEEE 8th International Conference on Research Challenges in Information Scien -->

<!-- [原子块 · verbatim] [55] H. Zhang, D. Hong, M. Yang, Y. Cheng, Z. Zhang, J. Shao, X. Wu, Z. Wu, and Y. Jiang (2025) CreatiDesign: a unified multi-conditional diffusion transformer for creative graphic design . External L -->

<!-- [原子块 · verbatim] [56] J. Zhang, R. Yoshihashi, S. Kitada, A. Osanai, and Y. Nakashima (2024) Vascar: content-aware layout generation via visual-aware self-correction . arXiv preprint arXiv:2412.04237 . Cited by: §1 ,  -->

<!-- [原子块 · verbatim] [57] N. Zhao, Y. Cao, and R. W. H. Lau (2018) What characterizes personalities of graphic designs? . ACM Trans. Graph. 37 ( 4 ), pp. 116 . External Links: Link , Document Cited by: §2 . -->

<!-- [原子块 · verbatim] [58] Y. Zhao, Z. Lin, D. Zhou, Z. Huang, J. Feng, and B. Kang (2023) Bubogpt: enabling visual grounding in multi-modal llms . arXiv preprint arXiv:2307.08581 . Cited by: §2 . -->

<!-- [原子块 · verbatim] [59] X. Zou, W. Zhang, and N. Zhao (2025) From fragment to one piece: a review on ai-driven graphic design . Journal of Imaging 11 ( 9 ), pp. 289 . Cited by: §1 . -->

**EN** Supplementary Material

**ZH** 补充材料

**EN** The supplementary is organised as follows: A PRISM Perturbations B Prompting Setup for Model Sensitivity C Backbone Ablation D Localised Error Detection Details E Scorer Out-of-Domain Generalization F Additional Examples from Editing Pipeline

**ZH** 补充材料的组织如下：A PRISM 扰动；B 模型敏感度评测的提示设置；C 骨干网络消融；D 局部化错误检测细节；E 打分器的分布外泛化；F 编辑流水线的补充示例。

**EN** Appendix A PRISM Perturbations

**ZH** 附录 A PRISM 扰动

**EN** In this section we provide additional details about how each perturbation in PRISM is constructed. The main paper introduces the framework and motivation in Section 3.1. Below, we describe the procedures used to isolate each design principle while keeping all other aspects of the poster unchanged so that each variant reflects a targeted violation of only one dimension. For the perturbations that provide localized supervision (readability, contrast, and overlap), we also record the elements involved so they can be used during instruction-tuning (Section 3.2.2).

**ZH** 本节提供 PRISM 中每种扰动如何构造的补充细节。正文第 3.1 节介绍了框架与动机。下面描述为隔离各条设计原则所采用的流程，同时保持海报的其他方面不变，使每个变体只反映单一维度上的目标违规。对提供局部化监督的扰动（可读性、对比度与遮挡），我们还记录所涉及的元素，以便在第 3.2.2 节的指令微调中使用。

**EN** A.1 Coherence

**ZH** A.1 连贯性

**EN** For coherence perturbation, we reassign each poster a new semantic theme sampled from a different category. We apply either a text-based or element-based modification selected at random. In the text perturbation, all textual content is rewritten using a few-shot LLM prompt so that the new text reflects the target theme while maintaining similar length. Only the text in the metadata is modified, thus preserving attributes such as font style, boldness, alignment, spacing, and color. For element modification, we identify visually prominent components using a vision-language query over the composed layout and check their relevance to the original theme using a lightweight LLM-based relevance classifier. We remove or replace elements determined to be theme-specific, and important background regions are regenerated using an image editor conditioned on the new theme while maintaining the color family. The new design preserves structure but conveys a different semantic theme.

**ZH** 对连贯性扰动，我们为每张海报重新指派一个采样自不同类别的新语义主题，并随机采用基于文本或基于元素的修改。在文本扰动中，所有文本内容都用少样本 LLM 提示重写，使新文本反映目标主题，同时保持相近的长度。只修改元数据中的文本，从而保留字体风格、粗细、对齐、间距与颜色等属性。在元素修改中，我们通过对合成版面做视觉—语言查询来识别视觉上突出的组件，并用一个轻量级的基于 LLM 的相关性分类器检查它们与原始主题的相关性。被判定为特定于主题的元素会被移除或替换；重要的背景区域则用一个以新主题为条件的图像编辑器重新生成，同时保持色系。新设计保留了结构，却传达了不同的语义主题。

**EN** A.2 Readability

**ZH** A.2 可读性

**EN** Readability perturbation reduces the legibility of text while keeping the overall layout intact. For each poster, we randomly select a subset of text elements and apply one or more readability changes. These include shrinking text that is unusually large, adjusting the line height of multi-line text blocks so that spacing becomes compressed, and shifting of text color toward the dominant background color behind it. Each poster receives only a subset of these modifications, and the perturbations applied to each text block are recorded so that the dataset includes explicit supervision about how readability was degraded.

**ZH** 可读性扰动在保持整体版面不变的前提下降低文字的易读性。对每张海报，我们随机选取一部分文本元素，并施加一项或多项可读性改动，包括：把异常大的文字缩小；调整多行文本块的行高使间距变紧；把文字颜色向其背后的主色背景色偏移。每张海报只接受这些修改的一个子集，并且施加到每个文本块上的扰动都会被记录下来，使数据集包含关于可读性如何被降级的显式监督。

**EN** A.3 Contrast

**ZH** A.3 对比度

**EN** Contrast perturbation weakens the visual separation between foreground and background while preserving the original structural layout. We randomly select a subset of text, icons, or decorative elements and apply one or more transformations. Text contrast perturbation is similar to readability perturbation with contrast. We edit icons and other graphical components using a diffusion-based tool that adjusts their color distributions so that they blend more closely with surrounding areas. For each modification, we record the specific foreground–background pairs where contrast was intentionally reduced.

**ZH** 对比度扰动在保留原始结构版面的前提下削弱前景与背景之间的视觉分离。我们随机选取一部分文本、图标或装饰元素，并施加一项或多项变换。文字的对比度扰动与可读性扰动中的对比度处理类似。对于图标及其他图形组件，我们使用基于扩散的工具调整其颜色分布，使其与周围区域更接近地融合。对每一处修改，我们记录对比度被有意降低的具体前景—背景对。

**EN** A.4 Alignment

**ZH** A.4 对齐

**EN** Alignment perturbation introduces positional shifts that disrupt the structural consistency of the design. For each poster, we randomly select a small set of elements and shift them horizontally or vertically so that they break expected alignment patterns such as column structure or centered grouping. When a text block has an element, that is not the overall background, just below it, we move both together so that the perturbation affects alignment without introducing unintended overlap or contrast issues. These modifications do not map cleanly onto specific localised pairs but instead makes changes to the poster on a global level.

**ZH** 对齐扰动引入位置偏移，破坏设计的结构一致性。对每张海报，我们随机选取少量元素并做水平或垂直位移，使其打破预期的对齐模式，例如分栏结构或居中分组。当某个文本块正下方存在一个并非整体背景的元素时，我们把两者一起移动，使扰动只影响对齐而不引入意外的遮挡或对比度问题。这些修改无法干净地映射到具体的局部化元素对，而是在全局层面上改动海报。

**EN** A.5 Overlap

**ZH** A.5 遮挡

**EN** Overlap perturbation introduces unintended occlusions between non-text elements while keeping all other aspects of the layout unchanged. We randomly select a small number of icons, shapes, or decorative components and position them so that they partially cover other elements while maintaining the overall alignment. This produced cases such as icon overlapping with icon or shape overlapping with another object, hence reducing visual separability. For each overlap introduced, we record the specific element pairs involved for explicit supervision.

**ZH** 遮挡扰动在非文本元素之间引入非预期的遮蔽，同时保持版面的其他方面不变。我们随机选取少量图标、形状或装饰组件，将它们放置到部分覆盖其他元素的位置，同时维持整体对齐。这产生了图标压图标、形状压另一物体等情形，从而降低了视觉可分性。对每一处引入的遮挡，我们记录所涉及的具体元素对，以提供显式监督。

**EN** Appendix B Prompting Setup for Model Sensitivity

**ZH** 附录 B 模型敏感度评测的提示设置

**EN** To evaluate model sensitivity to PRISM perturbations (Section 4.3), we query each model under a consistent rubric-based prompting setup. The system prompt defines the scoring criteria for all five design principles and the overall score, each on a continuous scale between 0 and 1. The user prompt requests that the model return a JSON response without any explanation. For every composed or perturbed poster, the corresponding image is supplied directly to the model using its multimodal interface. For reproducibility, we include the exact prompts used for GPT-4o, GPT-4o-mini, and Qwen-2.5-VL in Figure 9. We also include average scores and sensitivity (⟦SLOT_48⟧) from each model across design principles in Table 4.

**ZH** 为评估模型对 PRISM 扰动的敏感度（第 4.3 节），我们在一致的、基于评分量表的提示设置下查询每个模型。系统提示定义了五项设计原则及总体分数的评分标准，各项均采用 0 到 1 的连续量表。用户提示要求模型返回 JSON 响应且不作任何解释。对每张原始或扰动海报，相应图像通过模型的多模态接口直接提供。为便于复现，我们在图 9 中给出了用于 GPT-4o、GPT-4o-mini 与 Qwen-2.5-VL 的确切提示。表 4 还给出了各模型在各设计原则上的平均分与敏感度（⟦SLOT_48⟧）。

<!-- [原子块 · object]  -->

**EN** Figure 9: Prompts for evaluating model sensitivity to PRISM Perturbations. For results, see Fig 3.

**ZH** 图 9：用于评测模型对 PRISM 扰动敏感度的提示。结果见图 3。

<!-- [原子块 · table] Backbone Precision ↑ \uparrow Recall ↑ \uparrow F1-score ↑ \uparrow AUC ↑ \uparrow Frozen ViT-B/16 0.528 0.522 0.524 0.554 DINOv2 0.539 0.531 0.535 0.563 OpenCLIP ViT-B/16 0.551 0.544 0.547 0.577 SigL -->

**EN** Table 3: Backbone comparison for PRISM-scorer. Untrained backbones show limited design-sensitivity, while pretrained contrastive models (CLIP, SigLIP-v2) demonstrate strong performance. SigLIP-v2 (Ours) achieves the best overall scores across all metrics.

**ZH** 表 3：PRISM-Scorer 的骨干网络对比。未经训练的骨干表现出有限的设计敏感度，而预训练的对比式模型（CLIP、SigLIP-v2）表现强劲。SigLIP-v2（ ours）在所有指标上取得最佳总体成绩。

<!-- [原子块 · table] Model Coherence Readability Contrast Alignment Overlap Org Perturb Δ \Delta Org Perturb Δ \Delta Org Perturb Δ \Delta Org Perturb Δ \Delta Org Perturb Δ \Delta Qwen-2.5-VL 0.739 0.678 0.061 0.807 0.73 -->

**EN** (a) Coherence Results.

**ZH** （a）连贯性结果。

<!-- [原子块 · table] Model Coherence Readability Contrast Alignment Overlap Org Perturb Δ \Delta Org Perturb Δ \Delta Org Perturb Δ \Delta Org Perturb Δ \Delta Org Perturb Δ \Delta Qwen-2.5-VL 0.744 0.690 0.054 0.830 0.72 -->

**EN** (b) Readability Results.

**ZH** （b）可读性结果。

<!-- [原子块 · table] Model Coherence Readability Contrast Alignment Overlap Org Perturb Δ \Delta Org Perturb Δ \Delta Org Perturb Δ \Delta Org Perturb Δ \Delta Org Perturb Δ \Delta Qwen-2.5-VL 0.751 0.691 0.06 0.810 0.730 -->

**EN** (c) Contrast Results.

**ZH** （c）对比度结果。

<!-- [原子块 · table] Model Coherence Readability Contrast Alignment Overlap Org Perturb Δ \Delta Org Perturb Δ \Delta Org Perturb Δ \Delta Org Perturb Δ \Delta Org Perturb Δ \Delta Qwen-2.5-VL 0.748 0.690 0.058 0.804 0.73 -->

**EN** (d) Alignment Results.

**ZH** （d）对齐结果。

<!-- [原子块 · table] Model Coherence Readability Contrast Alignment Overlap Org Perturb Δ \Delta Org Perturb Δ \Delta Org Perturb Δ \Delta Org Perturb Δ \Delta Org Perturb Δ \Delta Qwen-2.5-VL 0.732 0.672 0.06 0.821 0.746 -->

**EN** (e) Overlap Results.

**ZH** （e）遮挡结果。

**EN** Table 4: Average Model Sensitivity Scores. The table shows the scores from different models on original vs perturbed layouts across design principles, ⟦SLOT_49⟧ denotes the difference between the averages showing sensitivity. While GPT-4o shows sensitivity, PRISM-Scorer is able to disentangle the principles better than any other model.

**ZH** 表 4：模型平均敏感度分数。表中展示了不同模型在原始版面与扰动版面上、跨设计原则的分数；⟦SLOT_49⟧ 表示平均值之差，反映敏感度。GPT-4o 虽表现出敏感度，但 PRISM-Scorer 能比其他任何模型更好地解耦各条原则。

**EN** Appendix C Backbone Ablation

**ZH** 附录 C 骨干网络消融

**EN** Table 3 compares several visual backbones. This ablation evaluates whether architectural choice or multimodal pretraining affects a model’s ability to detect principle-specific design degradations. In the frozen setting, each backbone is initialized with its standard pretrained weights: ViT-B/16 [8] trained on ImageNet [43], SigLIP-v2 [49] trained on WebLI [4], and the self-supervised DINOv2 model [33], but we freeze the entire backbone and train only an identical lightweight two-layer binary classifier on top for all models, ensuring that differences arise solely from the backbone representations. We then report averaged PRISM-scorer performance across all five principles. These frozen models provide limited but non-trivial sensitivity to design perturbations, with vision-only backbones (ViT-B/16, DINOv2) performing the weakest and frozen vision–language architectures (OpenCLIP [21], SigLIP-v2) offering slightly stronger baselines due to their multimodal structure. In the fine-tuned setting, we update all backbone weights using the principle-aware fine-tuning procedure described in Section 3.2.1, leveraging paired image–caption data from Crello [52] and CreatiDesign [55]. This multimodal contrastive supervision leads to substantial improvements: fine-tuned OpenCLIP ViT-B/16 significantly outperforms all frozen variants, and SigLIP-v2 (Ours) achieves the strongest performance across precision, recall, F1, and AUC. These findings underscore the importance of principle-aware multimodal fine-tuning and motivate our use of SigLIP-v2 as the backbone for PRISM-scorer.

**ZH** 表 3 比较了若干视觉骨干网络。该消融考察架构选择或多模态预训练是否影响模型检测针对特定原则的设计退化的能力。在冻结设定下，每个骨干都以标准预训练权重初始化：在 ImageNet [43] 上训练的 ViT-B/16 [8]、在 WebLI [4] 上训练的 SigLIP-v2 [49]，以及自监督的 DINOv2 模型 [33]；但我们冻结整个骨干，只在顶部为所有模型训练一个相同的轻量级两层二值分类器，确保差异完全来自骨干表示。随后我们报告 PRISM-Scorer 在五项原则上的平均性能。这些冻结模型对设计扰动表现出有限但不可忽略的敏感度：纯视觉骨干（ViT-B/16、DINOv2）最弱，而冻结的视觉—语言架构（OpenCLIP [21]、SigLIP-v2）因具备多模态结构而基线略强。在微调设定下，我们用第 3.2.1 节所述的原则感知微调流程更新全部骨干权重，并利用来自 Crello [52] 与 CreatiDesign [55] 的成对图像—描述数据。这种多模态对比式监督带来显著提升：微调后的 OpenCLIP ViT-B/16 大幅优于所有冻结变体，而 SigLIP-v2（ ours）在精确率、召回率、F1 与 AUC 上取得最强性能。这些发现凸显了原则感知的多模态微调的重要性，也说明我们选用 SigLIP-v2 作为 PRISM-Scorer 骨干的理由。

**EN** We also compare the simple linear head on top of this design-aware architecture with other variants. Averaged across principles, the test F1 scores are: linear head (⟦SLOT_50⟧), two-layer MLP (⟦SLOT_51⟧), and multi-head attention (⟦SLOT_52⟧). These results show that a simpler linear layer is sufficient to achieve the required performance gains.

**ZH** 我们还比较了在这一设计感知架构之上使用简单线性头与其他变体的差异。跨原则平均的测试 F1 分数为：线性头（⟦SLOT_50⟧）、两层 MLP（⟦SLOT_51⟧）与多头注意力（⟦SLOT_52⟧）。这些结果表明，更简单的线性层已足以取得所需的性能增益。

**EN** We compare a unified scorer–localizer model, evaluated by training Qwen-2.5-VL end-to-end. The unified model achieves an average F1 score of ⟦SLOT_53⟧ as a scorer and mean IoU scores of ⟦SLOT_54⟧ across principles. The unified model performs worse than our expert PRISM scorer and localizer models. This explains the need for experts instead of one unified model trained for multiple tasks.

**ZH** 我们还比较了一个统一的打分器—定位器模型，通过端到端训练 Qwen-2.5-VL 来评估。该统一模型作为打分器取得平均 F1 ⟦SLOT_53⟧，跨原则的平均 IoU 为 ⟦SLOT_54⟧。统一模型的表现不如我们专用的 PRISM 打分器与定位器模型，这解释了为何需要各司其职的专用模型，而不是一个为多任务训练的统一模型。

<!-- [原子块 · object]  -->

**EN** Figure 10: Prompts for Localising Error Detection. The figure shows the prompts used for instruct-tuning and evaluating models for local principles (Readability (A), Contrast (B), Overlap (C)). Results comparing different models using this prompt can be seen in Table 2.

**ZH** 图 10：用于局部化错误检测的提示。图中给出了针对局部原则（可读性 (A)、对比度 (B)、遮挡 (C)）做指令微调与评测时使用的提示。使用该提示比较不同模型的结果见表 2。

**EN** Appendix D Localised Error Detection Details

**ZH** 附录 D 局部化错误检测细节

**EN** We get the data required for instruction-tuning as described in Section A. To train the model on localised supervision from readability, contrast and overlap perturbations, we use the prompts as shown in Figure 10. For readability, the corresponding image input is simply the design, whereas for contrast and overlap, we annotate the design using the metadata to include IDs for each non-textual element. For readability, the model is asked to choose from a list of texts present in the design, while for contrast and overlap, we provide pairs of elements to choose from. The list only contains pairs which have some overlapping components in order to contain the combinations to a reasonable number. We use the same prompt for evaluating and comparing different models on the held-out set. We use the training and evaluating methods as mentioned in Section 4.4 and 5.3, respectively, for the results refer to Figure 2.

**ZH** 我们按附录 A 所述获取指令微调所需的数据。为利用来自可读性、对比度与遮挡扰动的局部化监督训练模型，我们使用图 10 所示的提示。对可读性，相应的图像输入就是设计本身；而对对比度与遮挡，我们用元数据对设计加以标注，为每个非文本元素加入 ID。对可读性，模型被要求从设计中出现的一组文本里做选择；而对对比度与遮挡，我们提供元素对供其选择。该列表只包含存在某些重叠组件的元素对，以把组合数量控制在合理范围内。我们在留出集上用同一提示对不同模型做评测与比较。训练与评测方法分别如第 4.4 节与第 5.3 节所述，结果见图 2。

<!-- [原子块 · img]  -->

**EN** Figure 11: Coherence-based editing examples. The grid shows perturbed posters and the editing path (See Section 5.4). Since the pipeline focuses only on coherence, edits target the background, elements, and font for thematic consistency, while other principles remain unchanged. Scores reflect the scorer’s coherence predictions at each step.

**ZH** 图 11：基于连贯性的编辑示例。网格展示了扰动后的海报与编辑路径（见第 5.4 节）。由于流水线只关注连贯性，编辑针对背景、元素与字体以求主题一致，而其他原则保持不变。分数反映了打分器在每一步的连贯性预测。

**EN** Appendix E Scorer Out-of-domain generalization

**ZH** 附录 E 打分器的分布外泛化

**EN** As observed in Figure 7, the PRISM scorer is able to disentangle design principles. We evaluate the coherence scorer with all other perturbations that it has not seen during training, giving us insights into the scorer’s generalization performance. While the scorer can generalize to all types of PRISM perturbations, we test the potential of the scorer on a different perturbation style from the GDE dataset [11]. This dataset only contains overlap and alignment perturbations. We evaluate our scorers using human annotations from the GDE dataset as ground truth. The PRISM scorer for overlap and alignment achieves F1 scores of ⟦SLOT_55⟧ and ⟦SLOT_56⟧, respectively, showing generalization to other types of perturbations as well.

**ZH** 如图 7 所示，PRISM 打分器能够解耦各条设计原则。我们用训练时未见过的所有其他扰动来评测连贯性打分器，以了解打分器的泛化性能。打分器虽能泛化到所有类型的 PRISM 扰动，我们还在来自 GDE 数据集 [11] 的一种不同扰动风格上测试了打分器的潜力。该数据集只包含遮挡与对齐两类扰动。我们用 GDE 数据集的人工标注作为真值来评估我们的打分器。PRISM 的遮挡打分器与对齐打分器分别取得 F1 分数 ⟦SLOT_55⟧ 与 ⟦SLOT_56⟧，说明其也能泛化到其他类型的扰动。

**EN** Appendix F Additional Examples from Editing Pipeline

**ZH** 附录 F 编辑流水线的补充示例

**EN** As shown in Figure 11, we present additional examples from our demonstrative editing pipeline, which operates exclusively using the coherence module. Candidate edits are proposed by the coherence localizer and ranked at each step by the coherence scorer, resulting in refinements that focus solely on restoring thematic and stylistic consistency (See Section 5.4). These examples only look at coherence-driven changes, while keeping the other principles untouched. A natural next step is to extend the editing pipeline to all design principles and explore ways to combine these principle-specific refinements. A unified system that can coordinate edits across principles would enable more comprehensive and well-rounded layout improvement.

**ZH** 如图 11 所示，我们给出演示性编辑流水线的补充示例，该流水线只使用连贯性模块运行。候选编辑由连贯性定位器提出，并在每一步由连贯性打分器排序，得到的改进只专注于恢复主题与风格的一致性（见第 5.4 节）。这些示例只关注由连贯性驱动的改动，其他原则保持不变。自然的下一步是把编辑流水线扩展到全部设计原则，并探索组合这些针对特定原则的改进方式。一个能够跨原则协调编辑的统一系统，将带来更全面、更完善的版面改进。
