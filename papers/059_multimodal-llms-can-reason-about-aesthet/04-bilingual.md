# 多模态大语言模型可在零样本条件下进行审美推理

> 原标题：Multimodal LLMs Can Reason about Aesthetics in Zero-Shot
> 作者：Ruixiang Jiang, Changwen Chen · arXiv:2501.09012 · 2025-01-15

<!-- [原子块 · verbatim] Multimodal LLMs Can Reason about Aesthetics in Zero-Shot DOI: XXXXXXX.XXXXXXX Conference: Arxiv; 2025; NY ISBN: 978-1-4503-XXXX-X/2018/06 CCS: Applied computing Fine arts CCS: Computing methodologies  -->

<!-- [原子块 · verbatim] Abstract. -->

<!-- [原子块 · verbatim] The rapid progress of generative art has democratized the creation of visually pleasing imagery. However, achieving genuine artistic impact – the kind that resonates with viewers on a deeper, more mea -->

**EN** Keywords:

**ZH** 关键词：

**EN** 1. Introduction

**ZH** 1. 引言

**EN** Human aesthetic perception is a multifaceted decision-making process that extends beyond mere visual appeal. It encompasses factors including, but not limited to, originality, cultural background, emotional resonance, and visual narrative, all of which contribute to the unique aesthetic value of artworks (Gombrich and Gombrich 1995; Kant 2024; Hume 1757; Joshi et al. 2011). The importance of understanding this complex process is widely acknowledged by art practitioners and scholars, as it not only deepens our theoretical understanding of beauty but also informs and inspires art creation (Gombrich and Gombrich 1995; Sibley 2017). In the era of rapidly advancing generative arts, an algorithmic understanding of aesthetics is also crucial to producing truly unique and impactful artistic representations (Samo and Highhouse 2023; Bo et al. 2018; Guo et al. 2025b; Chamberlain et al. 2018).

**ZH** 人类审美知觉是一个超越单纯视觉吸引力的多面向决策过程。它所涵盖的因素包括但不限于原创性、文化背景、情感共鸣与视觉叙事，这些因素共同造就了艺术品独特的审美价值（Gombrich 与 Gombrich，1995；Kant，2024；Hume，1757；Joshi 等，2011）。艺术从业者与学者普遍承认理解这一复杂过程的重要性：它既加深我们关于美的理论认识，也为艺术创作提供启示与滋养（Gombrich 与 Gombrich，1995；Sibley，2017）。在生成式艺术飞速发展的时代，对审美的算法化理解同样是产出真正独特而有感染力的艺术表达的关键（Samo 与 Highhouse，2023；Bo 等，2018；Guo 等，2025b；Chamberlain 等，2018）。

<!-- [原子块 · img]  -->

**EN** Figure 1. Existing models assess aesthetics as a black-box, which is oversimplified and can misinterpret the aesthetic value. The complex, multifaceted human aesthetic judging process must be captured for human-aligned aesthetic evaluation. Credit: Girl with a Mandolin (1910), by Pablo Picasso

**ZH** 图 1. 现有模型把审美评估当作黑箱处理，这种做法过于简化，并可能误读审美价值。要实现与人类对齐的审美评估，必须刻画人类复杂而多面的审美判断过程。图片来源：Pablo Picasso《弹曼陀林的女孩》（1910）

**EN** Despite its complexity and importance, a majority of existing computational approaches have oversimplified the concept of aesthetics. They predominantly employ end-to-end learning to obtain black-box models that predict a score. Specifically, systems like traditional Image Quality Assessment (IQA) (Zhu et al. 2024; Wang et al. 2023), AI-Generated IQA (AGIQA) (Yang et al. 2024), and more recent human preference models (e.g., PickScore (Kirstain et al. 2023), VisionPrefer (Wu et al. 2024)) follow this limited paradigm—regressing human preference based on visual feature maps, without engaging with the complex cognitive processes underlying aesthetic judgment. While these scoring models may be effective in assessing image quality in certain cases, they provide no insights and interpretation for their prediction. More importantly, the measurement of quality or visual appeal is a fundamentally superficial understanding (i.e., a kistch) of aesthetics (Sibley 2017; Kant 2024; Schelling et al. 2008; Gombrich and Gombrich 1995; Hume 1757; Isik and Vessel 2021), and this limited view can lead to misalignment with human aesthetic perception in practice (So 2023; Ioannou and Maddock 2024; Barnet 2015; Chen et al. 2024; Ortlieb and Carbon 2019; Samo and Highhouse 2023; Black et al. 2023). For instance, impactful paintings that are not immediately visually pleasing but involve more in-depth artistic expression may be mis-classified by these models. Therefore, modeling and mimicking the multifaceted cognitive process in human aesthetic judgment is essential to build a truly human-aligned aesthetic evaluator, as illustrated in Fig. 1.

**ZH** 尽管审美既复杂又重要，多数现有计算方法仍把这一概念过度简化。它们主要依靠端到端学习得到预测分数的黑箱模型。具体而言，传统图像质量评估（IQA）（Zhu 等，2024；Wang 等，2023）、AI 生成图像质量评估（AGIQA）（Yang 等，2024），以及较新的人类偏好模型（如 PickScore（Kirstain 等，2023）、VisionPrefer（Wu 等，2024））都遵循这一局限范式——基于视觉特征图回归人类偏好，而不涉及审美判断背后的复杂认知过程。这类打分模型在某些情况下或许能有效评估图像质量，却不为自己的预测提供任何洞见与解释。更重要的是，对质量或视觉吸引力的度量本质上只是对审美的表层理解（即一种媚俗）（Sibley，2017；Kant，2024；Schelling 等，2008；Gombrich 与 Gombrich，1995；Hume，1757；Isik 与 Vessel，2021），这种狭隘视角在实践中会导致与人类审美知觉的错位（So，2023；Ioannou 与 Maddock，2024；Barnet，2015；Chen 等，2024；Ortlieb 与 Carbon，2019；Samo 与 Highhouse，2023；Black 等，2023）。例如，那些并不一眼悦目、却蕴含更深艺术表达的有感染力画作，可能被这些模型误判。因此，建模并模仿人类审美判断中多面的认知过程，是构建真正与人类对齐的审美评估器的必要条件，如图 1 所示。

**EN** In seeking to capture the ineffable nature of human aesthetic perception, we draw broad inspiration from art and philosophy. In particular, the practice of “formal analysis” (Barnet 2015; Kim et al. 2022; Van Leeuwen and Jewitt 2000) in art criticism offers valuable insights to formulate our goal. It is a structured approach where critics methodically describe their observations in terms of visual elements, critically interpret compositional choices, and connect these observations to broader aesthetic principles for objective aesthetic judgment. This analysis does not merely catalog visual features; it actively weaves perception, emotion, cultural context, and artistic knowledge into a coherent evaluative narrative. This multifaceted narrative connects observation and interpretation, mapping the cognitive activity of our art experience into words, a holistic capability that bears a striking resemblance to the inference-time reasoning paradigm of recent multimodal large language models (MLLMs) (OpenAI 2023; Team et al. 2023; Anthropic [n. d.]; Wei et al. 2022). This parallel presents an opportunity to address the long-standing challenge of modeling human aesthetic judgment, inspiring our central research question:

**ZH** 为捕捉人类审美知觉那种难以言说的性质，我们从艺术与哲学中汲取了广泛启发。其中，艺术批评中的“形式分析”（formal analysis）实践（Barnet，2015；Kim 等，2022；Van Leeuwen 与 Jewitt，2000）为确立我们的目标提供了有益启示。它是一种结构化方法：批评者以视觉要素为线索条理化地描述观察，批判性地解读构图选择，并把这些观察与更广泛的审美原则相连，从而做出客观的审美判断。这种分析不只是罗列视觉特征，而是把知觉、情感、文化语境与艺术知识主动编织成连贯的评价性叙事。这条多面叙事把观察与阐释连接起来，把艺术体验中的认知活动映射为语言——这种整体能力与近期多模态大语言模型（MLLM）在推理时展开推理的范式（OpenAI，2023；Team 等，2023；Anthropic，[n. d.]；Wei 等，2022）惊人地相似。这一平行关系为攻克建模人类审美判断这一长期难题提供了契机，并引出我们的核心研究问题：

**EN** Can reasoning facilitate MLLMs perform human-aligned aesthetic judgments in zero-shot?

**ZH** 推理能否让 MLLM 在零样本条件下做出与人类对齐的审美判断？

**EN** Answering this question requires understanding both human aesthetic judgment and how reasoning can be effectively performed in MLLMs. For the human aspect, this paper proposes a rank-based human aesthetic perception model, designed to suppress inter-person subjectivity through philosophy-inspired principles (Tatarkiewicz 1963; Kant 2024; Tatarkiewicz 2012). Human expert judgment is collected on a newly proposed dataset, FineArtBench, with large-scale and semantically labeled styles to facilitate statistically unbiased correlation studies. We leverage chain-of-thought (CoT) prompting to enable the reasoning of MLLMs. The reasoning traces are tracked to facilitate judgment and perform quantitative correlation analysis with human decisions.

**ZH** 回答这个问题既需要理解人类审美判断，也需要理解如何在 MLLM 中有效执行推理。就人类一侧而言，本文提出一种基于排序的人类审美知觉模型，通过受哲学启发的原则抑制个体间主观性（Tatarkiewicz，1963；Kant，2024；Tatarkiewicz，2012）。我们在新提出的数据集 FineArtBench 上采集人类专家判断，该数据集带有大规模且具语义标注的风格，便于开展统计上无偏的相关性研究。我们借助思维链（CoT）提示来激发 MLLM 的推理。推理轨迹被记录下来，用于形成判断并与人类决策做定量相关性分析。

**EN** By experimenting with different prompting techniques across MLLMs, we identify a key challenge in applying them for artistic evaluation: hallucination. Specifically, we observe a high tendency for MLLMs to reason subjectively with unsubstantiated artistic interpretations. Our analysis further underscores that the bottleneck lies in the reasoning process itself, rather than in the base model. We argue that evidence-based and objective reasoning is essential to suppress these hallucinations. With these valuable insights, we demonstrate that a simple baseline, ArtCoT, can produce exceptionally in-depth and multifaceted aesthetic reasoning. Judgments conditioned with such objective and critical reasoning demonstrate a substantial improvement in correlation with human decision. It also significantly outperforms existing IQA and preference models. Overall, our findings not only envision future directions for aesthetic reasoning but also have direct applications in human-computer interaction (HCI) and generative art, such as AI art tutors (Ghose 2017; Xu 2024) and reinforcement learning from AI feedback (RLAIF)-enhanced art generation (Black et al. 2023; Clark et al. 2023; Guo et al. 2025b; Wu et al. 2024).

**ZH** 通过在多个 MLLM 上试验不同的提示技术，我们识别出将其用于艺术评估时的一个关键难题：幻觉。具体而言，我们观察到 MLLM 高度倾向于以主观方式推理，并给出缺乏依据的艺术阐释。我们的分析进一步指出，瓶颈在于推理过程本身，而非基座模型。我们认为，基于证据的客观推理是抑制这些幻觉的关键。基于这些有价值的认识，我们证明一个简单的基线 ArtCoT 能够产生异常深入且多面的审美推理。以这种客观而批判性的推理为条件的判断，与人类决策的相关性大幅提升，并显著优于现有 IQA 与偏好模型。总体而言，我们的发现不仅为审美推理指明了未来方向，也在人机交互（HCI）与生成式艺术中有直接应用，例如 AI 艺术导师（Ghose，2017；Xu，2024）以及基于 AI 反馈的强化学习（RLAIF）增强的艺术生成（Black 等，2023；Clark 等，2023；Guo 等，2025b；Wu 等，2024）。

**EN** We summarize our contributions as follows:

**ZH** 我们把贡献概括如下：

**EN** (1) We introduce the task of aesthetic reasoning.

**ZH** （1）提出审美推理这一任务。

**EN** (2) We propose a philosophy-inspired principled approach for objectively modeling human aesthetic judgment.

**ZH** （2）提出一种受哲学启发的原则性方法，用于客观建模人类审美判断。

**EN** (3) We introduce FineArtBench, the first large-scale semantically annotated dataset for broad tasks related to art.

**ZH** （3）提出 FineArtBench，首个面向广义艺术相关任务的大规模语义标注数据集。

**EN** (4) Our analysis provides valuable insights into the hallucination bottleneck of MLLMs in aesthetic reasoning.

**ZH** （4）我们的分析为 MLLM 在审美推理中的幻觉瓶颈提供了有价值的认识。

**EN** (5) Our baseline ArtCoT points out a promising way for human-aligned aesthetic reasoning in zero-shot.

**ZH** （5）我们的基线 ArtCoT 为零样本下与人类对齐的审美推理指出了一条可行路径。

**EN** 2. Related Works

**ZH** 2. 相关工作

**EN** 2.1. Generative Art, Fine Art and Aesthetics

**ZH** 2.1. 生成式艺术、美术与美学

**EN** Generative art is nothing special but a new medium for artistic expression. Neural style transfer (NST) (Deng et al. 2022; Huang and Belongie 2017; Gatys et al. 2016; An et al. 2021; Jiang and Chen 2024) and image generation methods (Elgammal et al. 2017; Rombach et al. 2022) are two central techniques in this field. Initially, research focused primarily on fidelity challenges, and the goal was to distill the distribution of real artworks, utilizing feature-level metrics such as Gram Loss (Gatys et al. 2016) and FID (Heusel et al. 2017; Wright and Ommer 2022) to quantify the alignment between generated and real artworks. More recently, the focus has shifted towards the affective challenge (Samo and Highhouse 2023; Li et al. 2024; Wu et al. 2024; Hullman et al. 2023): ensuring that the generated results are not only accurate but also visually pleasing. Preference models, such as PickScore (Kirstain et al. 2023) and HPS (Wu et al. 2023), are employed to address this aspect. With the rapid scaling of generative models, the acquisition of artistic images has become democratized. This progression allows us to pursue the ultimate challenge of art: striving for artistically meaningful and impactful artworks rather than mere visual appeal. This tri-stage progression was articulated at least 300 years ago by philosophers such as Hegel (Hegel and Hegel 1998). It is contextualized by the transition in art history from technical execution to artistic expression (Gombrich and Gombrich 1995). Just as aesthetics played a central role in that transition, an algorithmic understanding of aesthetics is key to advancing generative art. In this paper, we present a comprehensive study to this critical issue.

**ZH** 生成式艺术并无特别之处，它只是艺术表达的一种新媒介。神经风格迁移（NST）（Deng 等，2022；Huang 与 Belongie，2017；Gatys 等，2016；An 等，2021；Jiang 与 Chen，2024）与图像生成方法（Elgammal 等，2017；Rombach 等，2022）是该领域的两项核心技术。早期研究主要关注保真度问题，目标是蒸馏真实艺术品的分布，并用 Gram Loss（Gatys 等，2016）与 FID（Heusel 等，2017；Wright 与 Ommer，2022）等特征层指标来量化生成作品与真实作品的贴合程度。近来，重心转向了情感层面的挑战（Samo 与 Highhouse，2023；Li 等，2024；Wu 等，2024；Hullman 等，2023）：确保生成结果不仅准确，而且悦目。PickScore（Kirstain 等，2023）与 HPS（Wu 等，2023）等偏好模型被用于应对这一方面。随着生成模型迅速规模化，艺术图像的获取已被普及化。这一进程使我们可以去追求艺术的终极挑战：创作具有艺术意义与感染力的作品，而不只是悦目的图像。这一三阶段进程至少在 300 年前就由黑格尔（Hegel 与 Hegel，1998）等哲学家阐明，其背景则是艺术史上从技术执行到艺术表达的转折（Gombrich 与 Gombrich，1995）。正如美学在那次转折中居于核心地位，对审美的算法化理解也是推进生成式艺术的关键。本文围绕这一关键问题展开全面研究。

<!-- [原子块 · img]  -->

**EN** Figure 2. Overview of our correlation evaluation pipeline. First, (a) we sample content and style from FineArtBench, and construct 2AFC comparison sets by sampling from all possible candidate (artwork) comparisons. (b) Human judgment data is collected and filtered with two heuristic indicators, which are finally aggregated as global rankings. (c) We leverage different reasoning methods to derive the judgment from MLLMs. Finally, we calculate the correlation of rankings from MLLMs and humans as indicators of aesthetic alignment.

**ZH** 图 2. 我们的相关性评测流程总览。首先，（a）从 FineArtBench 中采样内容与风格，并通过在所有可能的候选（作品）比较中采样来构建 2AFC 比较集。（b）采集人类判断数据，用两个启发式指标过滤，最终聚合为全局排名。（c）用不同的推理方法从 MLLM 得到判断。最后，我们计算 MLLM 与人类排名的相关性，作为审美对齐程度的指标。

**EN** 2.2. Computational Evaluation of Artworks

**ZH** 2.2. 艺术品的计算式评估

**EN** Early aesthetic evaluation algorithms were primarily rule-based, assessing the visual quality of paintings or photos using different principles (Bo et al. 2018; Gips and Stiny 1975). While simple and interpretable, these principles lack the generality to explain all cases. With the development of deep learning, data-driven methods (Schuhmann et al. 2022; Hentschel et al. 2022) have emerged, attempting to directly learn aesthetic evaluators from image collections labeled with human preferences. In parallel to these explorations, a highly related line of works is the development of quantitative metrics for NST. ArtFID (Wright and Ommer 2022) and Art Score (Chen et al. 2024) are two notable examples of this trend. Despite their different focus, they share the same underlying design philosophy: measuring the distance between input and human-preferred images within the vision feature space. This black-box inference, however, oversimplifies the complex aesthetic judgment process and is often misaligned with human perception (So 2023; Ioannou and Maddock 2024; Barnet 2015; Black et al. 2023). Recent methods (Zhang et al. 2023a; Huang et al. 2024a; Ke et al. 2023) attempt to incorporate MLLMs for more interpretable aesthetic perception. Nevertheless, most of these approaches require costly instruction-tuning and still focus on characterizing the visual appeal. This paper demonstrates that reasoning can make general-purpose MLLMs human-aligned aesthetic reasoners in zero-shot.

**ZH** 早期的审美评估算法主要基于规则，用不同的原则评估绘画或照片的视觉质量（Bo 等，2018；Gips 与 Stiny，1975）。这些原则虽然简单可解释，却缺乏足以解释所有情形的普适性。随着深度学习的发展，出现了数据驱动的方法（Schuhmann 等，2022；Hentschel 等，2022），试图从带有人类偏好标注的图像集合中直接学出审美评估器。与这些探索并行的一条紧密相关的研究线，是 NST 定量指标的发展。ArtFID（Wright 与 Ommer，2022）与 Art Score（Chen 等，2024）是这一趋势的两个代表性例子。尽管侧重不同，它们共享相同的设计理念：在视觉特征空间中度量输入与人类偏好图像之间的距离。然而这种黑箱推理过度简化了复杂的审美判断过程，且常与人类知觉错位（So，2023；Ioannou 与 Maddock，2024；Barnet，2015；Black 等，2023）。近期方法（Zhang 等，2023a；Huang 等，2024a；Ke 等，2023）尝试引入 MLLM 以获得更可解释的审美知觉。尽管如此，这些方法大多需要昂贵的指令微调，并且仍聚焦于刻画视觉吸引力。本文表明，推理可以让通用 MLLM 在零样本条件下成为与人类对齐的审美推理者。

**EN** 2.3. CoT Reasoning and Hallucinations

**ZH** 2.3. CoT 推理与幻觉

**EN** CoT prompting (Wei et al. 2022; Kojima et al. 2022; Hao et al. 2024) is a simple yet powerful technique for both LLMs and MLLMs. It functions by enabling the model to “think aloud,” generating a trace of its reasoning process before arriving at a final answer. CoT has proven effective for a variety of tasks that benefit from enhanced logical reasoning (Mitra et al. 2024; Sprague et al. 2024). Despite this progress, CoT is also susceptible to hallucinations, where the generated reasoning trace can be misleading (Lindsey et al. 2025; Huang et al. 2025). This paper investigates the application of CoT to aesthetics evaluation, a domain that extends beyond strict logical reasoning. Our analysis reveals an inherent and special hallucination issue when CoT is applied to this task, and the proposed method overcomes challenge.

**ZH** CoT 提示（Wei 等，2022；Kojima 等，2022；Hao 等，2024）是一项简单而强大的技术，对 LLM 与 MLLM 同样适用。它的作用是让模型“把思考说出来”，在给出最终答案之前先生成一条推理轨迹。CoT 已被证明对一系列受益于强化逻辑推理的任务有效（Mitra 等，2024；Sprague 等，2024）。尽管如此，CoT 也容易受到幻觉影响，其生成的推理轨迹可能具有误导性（Lindsey 等，2025；Huang 等，2025）。本文研究 CoT 在审美评估中的应用，这是一个超越严格逻辑推理的领域。我们的分析揭示了 CoT 应用于该任务时固有而特殊的幻觉问题，所提方法克服了这一挑战。

**EN** 3. Methodology

**ZH** 3. 方法

**EN** 3.1. Problem Definition

**ZH** 3.1. 问题定义

**EN** Motivation. Despite the subjective nature of aesthetic taste, philosophers (Hume 1757; Tatarkiewicz 2012; Kant 2024; Tatarkiewicz 1963; Sircello 1968) and psychologists (Lindell and Mueller 2011; Palmer et al. 2013) generally acknowledge a degree of consensus regarding aesthetic judgments exists across cultures and historical periods, suggesting the possibility of objective comparative evaluation. This consensus, however, is not absolute. Comparing vastly different artworks, such as “Mona Lisa” and “Guernica” highlights the challenge of objective judgment without resorting to personal preference due to divergent content and style. In contrast, a controlled scenario, such as an art lesson where students draw porcelain vases using the cross-hatching technique, offers a more robust basis for objective aesthetics comparison. This approach aligns with established practices in art criticism and art education (Groenendijk et al. 2020; Andrade et al. 2014). With these observations, we explore aesthetic judgment within comparable contextual and stylistic frameworks for objective comparison.

**ZH** 研究动机。尽管审美趣味天然主观，哲学家（Hume，1757；Tatarkiewicz，2012；Kant，2024；Tatarkiewicz，1963；Sircello，1968）与心理学家（Lindell 与 Mueller，2011；Palmer 等，2013）普遍承认，审美判断在不同文化与历史时期之间存在一定程度的共识，这提示了客观比较评估的可能性。但这种共识并非绝对。比较差异极大的作品，例如《蒙娜丽莎》与《格尔尼卡》，凸显了在内容与风格分歧显著时，不诉诸个人偏好而做出客观判断的困难。相对地，在受控场景下——例如美术课上学生用交叉排线技法描绘瓷瓶——客观的美学比较就有了更稳固的基础。这一做法与艺术批评、艺术教育中的既定实践一致（Groenendijk 等，2020；Andrade 等，2014）。基于这些观察，我们在可比的语境与风格框架内考察审美判断，以实现客观比较。

**EN** Objective. From a computational perspective, we aim to derive a statistically robust global ranking of a set of artists (or art generators) or artworks (or generated art) from human feedback. Formally, let ⟦SLOT_0⟧, ⟦SLOT_1⟧, and ⟦SLOT_2⟧ denote the sets of all content, styles, and artists, respectively (within the studied scope). Each combination ⟦SLOT_3⟧ constitutes a task presented to the artists. The resulting artworks from artists ⟦SLOT_4⟧, denoted as ⟦SLOT_5⟧, form the set of candidates for this task: ⟦SLOT_6⟧. We model human aesthetic judgment as a partial ordering on the set ⟦SLOT_7⟧:

**ZH** 目标。从计算角度看，我们的目标是从人类反馈中导出一组艺术家（或艺术生成器）或艺术品（或生成艺术）在统计上稳健的全局排名。形式化地，令 ⟦SLOT_0⟧、⟦SLOT_1⟧ 与 ⟦SLOT_2⟧ 分别表示全部内容、风格与艺术家的集合（在所研究范围内）。每种组合 ⟦SLOT_3⟧ 构成一个呈现给艺术家的任务。艺术家 ⟦SLOT_4⟧ 产出的作品记为 ⟦SLOT_5⟧，构成该任务的候选集 ⟦SLOT_6⟧。我们把人类审美判断建模为集合 ⟦SLOT_7⟧ 上的一个偏序：

<!-- [原子块 · table] (1) y π ⁡ ( 1 ) ≻ y π ⁡ ( 2 ) ≻ ⋯ ≻ y π ⁡ ( k ) , \displaystyle y_{\pi(1)}\succ y_{\pi(2)}\succ\cdots\succ y_{\pi(k)}, -->

**EN** where ⟦SLOT_8⟧ maps the candidate index to its global rank, and ⟦SLOT_9⟧ means ⟦SLOT_10⟧ is judged to be superior than ⟦SLOT_11⟧. We measure the alignment as the correlation between the ranks constructed from human experts and the MLLM(s), and we are interested in studying the effectiveness and potential challenges of reasoning in enhancing this alignment.

**ZH** 其中 ⟦SLOT_8⟧ 把候选索引映射到其全局排名，⟦SLOT_9⟧ 表示 ⟦SLOT_10⟧ 被判断为优于 ⟦SLOT_11⟧。我们把对齐度度量为由人类专家与 MLLM 所构造排名之间的相关性，并关注推理在提升这种对齐度上的有效性及潜在挑战。

<!-- [原子块 · img]  -->

**EN** Figure 3. The FineArtBench dataset. Left: The label distribution and semantic attributes for both content and style. Right: examples of two content (top) and two style (bottom).

**ZH** 图 3. FineArtBench 数据集。左：内容与风格的标签分布与语义属性。右：两个内容（上）与两个风格（下）的示例。

**EN** 3.2. Modeling Human Aesthetic Perception

**ZH** 3.2. 人类审美知觉建模

**EN** Judgment Collection. Directly deriving the partial ordering as in Eq. 1 requires an exhaustive comparison, which can be cognitively demanding and impair human decision-making. Inspired by findings in psychometrics and HCI (Sullivan and Artino Jr 2013; So 2023), we instead employ a two-alternative forced choice (2AFC) task for more efficient decision collection. Specifically, we present users with the task specification ⟦SLOT_12⟧, along with two candidate artworks ⟦SLOT_13⟧. Users are required to judge the relatively superior artwork without the option to indicate a tie or skip the comparison. We model the (judged) aesthetic superiority relationship probabilistically:

**ZH** 判断采集。如式 1 那样直接导出偏序需要穷举比较，认知负担过重并会损害人类决策。受心理测量学与 HCI 中发现的启发（Sullivan 与 Artino Jr，2013；So，2023），我们改用二选一强制选择（2AFC）任务来更高效地采集决策。具体而言，我们向用户呈现任务说明 ⟦SLOT_12⟧ 与两件候选作品 ⟦SLOT_13⟧，要求用户判断相对更优的作品，且不允许表示平局或跳过比较。我们把（被判断的）审美优劣关系建模为概率形式：

<!-- [原子块 · table] (2) P ⁡ ( y i ≻ y j | c , s ) = Q i Q i + Q j , P(y_{i}\succ y_{j}|c,s)=\frac{Q_{i}}{Q_{i}+Q_{j}}, -->

**EN** where ⟦SLOT_14⟧ represents the latent competence of ⟦SLOT_15⟧, conditioned on the task of ⟦SLOT_16⟧.

**ZH** 其中 ⟦SLOT_14⟧ 表示 ⟦SLOT_15⟧ 的潜在能力值，条件为任务 ⟦SLOT_16⟧。

**EN** Sampling Strategies for 2AFC. Given the combinatorial complexity of ⟦SLOT_17⟧ (⟦SLOT_18⟧ in our case), exhaustive pairwise comparisons is infeasible. Therefore, we generate 2AFC comparisons by sampling, which reduce to a classical tournament scheduling problem. For a specific candidate set ⟦SLOT_19⟧, all possible comparisons can be modeled as complete graph ⟦SLOT_20⟧, where the node ⟦SLOT_21⟧ is the set of candidate results and ⟦SLOT_22⟧ stand for pair-wise comparison. We consider two strategies for sampling ⟦SLOT_23⟧, corresponding to two real-world scenarios:

**ZH** 2AFC 的采样策略。考虑到 ⟦SLOT_17⟧ 的组合复杂度（本例中为 ⟦SLOT_18⟧），穷举两两比较不可行。因此我们通过采样生成 2AFC 比较，这归结为一个经典的赛程编排问题。对于特定候选集 ⟦SLOT_19⟧，所有可能的比较可建模为完全图 ⟦SLOT_20⟧，其中节点 ⟦SLOT_21⟧ 是候选结果的集合，⟦SLOT_22⟧ 表示两两比较。我们考虑两种采样 ⟦SLOT_23⟧ 的策略，对应两种真实场景：

**EN** (1) Global sampling: Uniformly sample arbitrary number of edges without replacement. This approach is suitable for covering a wider range of content and style to facilitate the ranking of artists.

**ZH** （1）全局采样：无放回地均匀采样任意数量的边。这种方法适合覆盖更广的内容与风格范围，便于对艺术家排序。

**EN** (2) Per-task sampling: Sample edges ⟦SLOT_24⟧ such that the sub-graph is connective with maximum node degree uniformness, meaning that each candidates shall be compared with for similar times. This is suitable for determining the ranks within specific task.

**ZH** （2）按任务采样：采样边 ⟦SLOT_24⟧，使子图连通且节点度数尽可能均匀，即每个候选被比较的次数相近。这适合确定具体任务内的排名。

**EN** We design a novel greedy algorithm (described in Appendix. A.2) to efficiently achieve the requirements of per-task sampling.

**ZH** 我们设计了一种新的贪心算法（见附录 A.2）来高效满足按任务采样的要求。

**EN** Dealing with Subjectivity in Human judgment. Due to the inherent subjectivity of aesthetic perception, human judgment can vary even within the constrained scenario. This variation can arise from inherent annotation noise and is particularly prevalent when the artists perform equally good or bad. While addressing these challenging edge cases could be valuable, in this paper, given that this is an initial exploration of aesthetic reasoning, we focus on modeling the universality of aesthetics (Kant 2024; Tatarkiewicz 1963; Sircello 1968) with suppressed inter-personal subjectivity. This allows us to create an unbiased testbed for evaluation. To this end, we employ the following two heuristics to mitigate subjectivity during annotation collection:

**ZH** 处理人类判断中的主观性。由于审美知觉固有的主观性，即便在受控场景下人类判断也会存在差异。这种差异可能来自固有的标注噪声，在艺术家表现同样出色或同样糟糕时尤为常见。处理这些棘手的边界情形固然有价值，但鉴于本文是对审美推理的初步探索，我们把重点放在建模审美的普遍性（Kant，2024；Tatarkiewicz，1963；Sircello，1968），并抑制个体间主观性。这使我们能够构建一个无偏的评测环境。为此，我们在标注采集阶段采用下述两条启发式规则来缓解主观性：

**EN** (1) 2AFC disagreement: We exclude the 2AFC questions where judgments tie (⟦SLOT_25⟧).

**ZH** （1）2AFC 分歧：我们剔除判断打平（⟦SLOT_25⟧）的 2AFC 问题。

**EN** (2) Non-transitive relationship: To deal with non-transitive judgment, such as ⟦SLOT_26⟧, we apply a feedback arc set (FAS) algorithm (Younger 1963) to detect feedback arcs ⟦SLOT_27⟧ and drop the whole task when ⟦SLOT_28⟧.

**ZH** （2）非传递关系：为处理 ⟦SLOT_26⟧ 这类非传递判断，我们采用反馈弧集（FAS）算法（Younger，1963）检测反馈弧 ⟦SLOT_27⟧，并在 ⟦SLOT_28⟧ 时丢弃整个任务。

**EN** Global Rank Derivation. We utilize Bradley-Terry (BT) model (Bradley and Terry 1952) and Elo (Elo and Sloan 1978) algorithm. In the BT model, ⟦SLOT_29⟧, where the latent parameter ⟦SLOT_30⟧ is optimized with maximum likelihood estimation (MLE). The Elo algorithm utilize ⟦SLOT_31⟧, where ⟦SLOT_32⟧ is the rating of candidate-i that is updated on-line. The rank within a task is the sorted by the competence ⟦SLOT_33⟧ of each candidate result, and we leverage the averaged competence among all tasks as the competence of an artist.

**ZH** 全局排名推导。我们使用 Bradley-Terry（BT）模型（Bradley 与 Terry，1952）与 Elo 算法（Elo 与 Sloan，1978）。在 BT 模型中，⟦SLOT_29⟧，其中潜在参数 ⟦SLOT_30⟧ 通过极大似然估计（MLE）优化。Elo 算法使用 ⟦SLOT_31⟧，其中 ⟦SLOT_32⟧ 是在线更新的候选 i 的评分。任务内的排名按各候选结果的能力值 ⟦SLOT_33⟧ 排序，我们把所有任务上的平均能力值作为一位艺术家的能力值。

**EN** Table 1. Quantitative comparison of aesthetic judgment correlation. This table presents the statistical correlation (spearman’s ⟦SLOT_34⟧) and significance (⟦SLOT_35⟧ value, ⟦SLOT_36⟧) between rankings generated by different aesthetic evaluators and expert judgments. Both conventional models and MLLMs with different reasoning methods are compared. Performance improvement and decline is calculated as normalized changes relative to the base prompt method for each of the corresponding MLLM. MLLMs reasoned with ArtCoT consistently demonstrates strong alignment with human judgment.

**ZH** 表 1. 审美判断相关性的定量比较。本表给出不同审美评估器生成的排名与专家判断之间的统计相关性（Spearman’s ⟦SLOT_34⟧）与显著性（⟦SLOT_35⟧ 值，⟦SLOT_36⟧）。常规模型与采用不同推理方法的 MLLM 都被纳入比较。提升与下降按相对于各 MLLM 对应基础提示方法的归一化变化计算。以 ArtCoT 推理的 MLLM 始终表现出与人类判断的强对齐。

<!-- [原子块 · table] Model Reasoning Per-Artist Alignment Per-Task Alignment Elo Bradley-Terry Elo Bradley-Terry ρ \rho ↑ \uparrow p p -value ↓ \downarrow ρ \rho ↑ \uparrow p p -value ↓ \downarrow ρ \rho ↑ \uparrow p p -v -->

**EN** 3.3. Zero-shot Aesthetics Reasoning via CoT

**ZH** 3.3. 基于 CoT 的零样本审美推理

**EN** Recent inference-time scaling paradigms, in particular the CoT prompting (Wei et al. 2022; Kojima et al. 2022) demonstrate impressive zero-shot task-solving capability. However, CoT is more widely studied for commonsense and logical reasoning. Applying CoT reasoning to the task of aesthetic-level art evaluation, which is not a direct logical task, presents significant challenges and may lead to diminished alignment with the human judgment (Sprague et al. 2024; Liu et al. 2024), as will be detailed in the Sec. 5.1. Specifically, a key issue is hallucination, where judgments are made prematurely, relying on subjective and superficial justifications. In other words, during aesthetics reasoning, MLLMs inherently exhibit a tendency to “feel” rather than to “reason”, and this hallucinated feeling often severely degrades the MLLM’s aesthetic judgment.

**ZH** 近期的推理时扩展范式，特别是 CoT 提示（Wei 等，2022；Kojima 等，2022），展现出令人印象深刻的零样本任务求解能力。但 CoT 的研究主要集中在常识与逻辑推理。把 CoT 推理应用于艺术层面的审美评估——一个并非直接逻辑任务的问题——面临重大挑战，并可能导致与人类判断的对齐度下降（Sprague 等，2024；Liu 等，2024），详见第 5.1 节。具体而言，一个关键问题是幻觉：判断过早做出，依赖主观而表层的理由。换言之，在审美推理过程中，MLLM 天然倾向于“感受”而非“推理”，而这种被幻觉化的感受常常严重损害 MLLM 的审美判断。

**EN** Motivated by the formal analysis in art criticism (Barnet 2015; Kim et al. 2022; Van Leeuwen and Jewitt 2000), our key insight is to explicitly ground the MLLMs’ decision-making with evidence and domain knowledge in art. Based on this principle, we propose a simple yet effective baseline, ArtCoT, which frames aesthetic perception as an evidence-based reasoning task.

**ZH** 受艺术批评中形式分析（Barnet，2015；Kim 等，2022；Van Leeuwen 与 Jewitt，2000）的启发，我们的核心认识是：用证据与艺术领域知识显式地锚定 MLLM 的决策。基于这一原则，我们提出一个简单而有效的基线 ArtCoT，把审美知觉框定为基于证据的推理任务。

**EN** ArtCoT features a two-hop reasoning process. In the initial stage, the MLLM acts as a CS Analyzer, providing a detailed and concrete description of the input task ⟦SLOT_37⟧, as well as the paired 2AFC images ⟦SLOT_38⟧. In the second phase, acting as an Art Critic, the MLLM is prompted to critically evaluate its previous observation and critically argue about the aesthetic quality. This analysis is linked to domain knowledge in art, encompassing a multifaced discussion that is not limited to stylistic features of ⟦SLOT_39⟧, aesthetic principles, technical execution of the two candidates, and potential emotional impact. These two stages link observation, knowledge, and artistic value, mirroring the essence of formal analysis. Effectively, it establishes a rubric (Groenendijk et al. 2020; Andrade et al. 2014), translating the subjective perception of beauty into more well-defined sub-tasks that can be objectively reasoned with logical reasoning (Christensen and Ball 2016; Coleman 1966; Li et al. 2023).

**ZH** ArtCoT 采用两跳推理过程。第一阶段，MLLM 充当 CS Analyzer（内容／风格分析器），对输入任务 ⟦SLOT_37⟧ 以及配对的 2AFC 图像 ⟦SLOT_38⟧ 给出细致具体的描述。第二阶段，MLLM 充当 Art Critic（艺术批评者），被提示批判性地评估先前的观察，并就审美质量进行批判性论证。这一分析被连接到艺术领域知识，涵盖多方面的讨论，不限于 ⟦SLOT_39⟧ 的风格特征、审美原则、两件候选作品的技术执行以及潜在的情感影响。这两个阶段把观察、知识与艺术价值连接起来，呼应了形式分析的精髓。它实际上确立了一套评判细则（Groenendijk 等，2020；Andrade 等，2014），把对美的主观知觉转译为可以用逻辑推理客观处理的、定义更清晰的子任务（Christensen 与 Ball，2016；Coleman，1966；Li 等，2023）。

**EN** During this structured CoT reasoning process, MLLMs perform a multi-faceted and in-depth aesthetic evaluation that mimics the deliberation of an art critic. (Note that our goal is to capture such reasoning trace, not simply the 2AFC result.) This reasoning trace can benefit a wide range of downstream applications. In this paper, we aim to assess the correlation with human judgment during 2AFC. Therefore, we further employ a summarizer that takes the reasoning trace as input and outputs a binary answer indicating the winner. The overall workflow is visualized in Fig. 2.

**ZH** 在这一结构化的 CoT 推理过程中，MLLM 执行多面而深入的审美评估，模仿艺术批评者的审慎思考。（注意，我们的目标是捕捉这样的推理轨迹，而不只是 2AFC 的结果。）这条推理轨迹可惠及大量下游应用。本文中，我们旨在评估 2AFC 上与人类判断的相关性，因此进一步使用一个汇总器：它以推理轨迹为输入，输出指示胜者的二值答案。整体流程如图 2 所示。

**EN** 3.4. FineArtBench

**ZH** 3.4. FineArtBench

**EN** The collection of content and style (i.e., ⟦SLOT_40⟧) is most widely studied in NST literature (Jiang and Chen 2024; Huang et al. 2024b; Deng et al. 2022). However, these papers mainly rely on ad-hoc sampling from datasets such as MS-COCO (Lin et al. 2014) and WikiART (Wikiart [n. d.]). The limitation of this approach is at least in two folds: (1) limited in size and diversity, which cannot cover the wide range of art styles in real-world scenarios. (2) Limited semantic annotation, as most of the existing datasets do not provide semantic-level labeling of style and content, which impedes a fine-grained understanding of the methods’ strengths and weaknesses.

**ZH** 内容与风格（即 ⟦SLOT_40⟧）的采集在 NST 文献中研究最为广泛（Jiang 与 Chen，2024；Huang 等，2024b；Deng 等，2022）。但这些论文主要依赖从 MS-COCO（Lin 等，2014）与 WikiART（Wikiart，[n. d.]）等数据集中临时采样。这种做法的局限至少有两方面：（1）规模与多样性有限，无法覆盖真实场景中的宽广艺术风格范围；（2）语义标注有限，因为多数现有数据集不提供风格与内容的语义级标注，妨碍了对方法优缺点的细粒度理解。

**EN** To circumvent these challenges, we propose FineArtBench, a dataset for generative art with unprecedented scale, diversity and quality. First, FineArtBench contains 1,000, and 1,000 densely annotated content and styles, respectively. The data is harvested from diverse sources (Kirillov et al. 2023; Lin et al. 2014; Wikiart [n. d.]; Wang et al. 2022), and further diversified using MLLMs, enabling comprehensive comparison for downstream tasks related to art. Moreover, we provide both content and style in two modalities (text and image), further expanding its versatility. Second, we perform a semi-automated annotation process (detailed in Appendix. A.3) where both content and style are annotated from diverse perspectives, such as scene in content (e.g., nature, portrait) and abstractness of style (e.g., figurative, abstract). These annotations enable a semantic-level understanding for downstream tasks. A comparison of FineArtBench with existing datasets is presented in Tab. 2, and an overview is given in Fig. 3.

**ZH** 为绕过这些难题，我们提出 FineArtBench，一个在规模、多样性与质量上都前所未有的生成式艺术数据集。首先，FineArtBench 各包含 1,000 条经过密集标注的内容与风格。数据取自多种来源（Kirillov 等，2023；Lin 等，2014；Wikiart，[n. d.]；Wang 等，2022），并借助 MLLM 进一步多样化，从而支持艺术相关下游任务的全面比较。此外，我们以文本与图像两种模态提供内容与风格，进一步拓展其适用性。其次，我们执行半自动标注流程（详见附录 A.3），从多个视角标注内容与风格，例如内容中的场景（如自然、肖像）与风格的抽象程度（如具象、抽象）。这些标注为下游任务提供了语义级理解。FineArtBench 与现有数据集的比较见表 2，总览见图 3。

**EN** Table 2. Comparison of representative stylization benchmark datasets. The proposed FineArtBench offers significantly more content and style instance, with fine-grained multimodal annotations.

**ZH** 表 2. 代表性风格化基准数据集的比较。所提出的 FineArtBench 提供更多的内容与风格实例，并带有细粒度的多模态标注。

<!-- [原子块 · table] Dataset/Protocol # Content # Style Multimodal Semantic Labeling StyleID ( Chung et al. 2024 ) 20 40 ✗ ✗ LAION-Aesthetics ( Schuhmann et al. 2022 ) - ∼ \sim 50 ✗ ✗ ArtBench ( Liao et al. 2022 ) - 10 ✗  -->

**EN** 4. Experiments

**ZH** 4. 实验

**EN** 4.1. Experiment Setup

**ZH** 4.1. 实验设置

**EN** Stylization models. Considering the size of ⟦SLOT_41⟧, it is infeasible to hire real human artists for scalable dataset collection: a single painting requires days of expertise. On the other hand, existing publicly-available artworks have limited style that only covers a small subset of ⟦SLOT_42⟧. Even if we collect some paired paintings, the MLLMs are prone to memorization than reasoning. To this end, we primarily rely on neural style transfer (NST) models as our “artists.” We evaluated total of 10 NST models, all executed with the default configurations suggested by respective authors. The methods include AdaIN (Huang and Belongie 2017), ArtFlow (An et al. 2021), ControlNet (Zhang et al. 2023b), DDIM (Song et al. 2020), DiffArtist (Jiang and Chen 2024), DiffStyler (Huang et al. 2024b), InstantStyle (Wang et al. 2024), Instruct-pix2pix (Brooks et al. 2023), StyleID (Chung et al. 2024), and Sty-Tr2 (Deng et al. 2022). These stylization models encompass a wide range of architectures and exhibit varying degrees of artistic stylization capability. This diversity provides a robust testbed for evaluating the performance of MLLMs in art evaluation.

**ZH** 风格化模型。考虑到 ⟦SLOT_41⟧ 的规模，雇用真实人类艺术家做可扩展的数据集采集并不可行：一幅画需要数天的专业技能。另一方面，现有的公开艺术品风格有限，只覆盖 ⟦SLOT_42⟧ 的一小部分。即使我们收集到一些配对的画作，MLLM 也更倾向于记忆而非推理。因此，我们主要依靠神经风格迁移（NST）模型充当“艺术家”。我们共评测 10 个 NST 模型，均按各自作者建议的默认配置运行。这些方法包括 AdaIN（Huang 与 Belongie，2017）、ArtFlow（An 等，2021）、ControlNet（Zhang 等，2023b）、DDIM（Song 等，2020）、DiffArtist（Jiang 与 Chen，2024）、DiffStyler（Huang 等，2024b）、InstantStyle（Wang 等，2024）、Instruct-pix2pix（Brooks 等，2023）、StyleID（Chung 等，2024）与 Sty-Tr2（Deng 等，2022）。这些风格化模型涵盖广泛的架构，并表现出不同程度的艺术风格化能力。这种多样性为评估 MLLM 在艺术评估中的表现提供了稳健的测试平台。

**EN** Alignment Metrics. Following (Jiang and Chen 2024; Chen et al. 2024; Zhang et al. 2023a), we use the spearman’s correlation coefficient (Spearman 1987) to quantify the alignment between judgment from experts and MLLMs. A spearman’s ⟦SLOT_43⟧ closer to 1 indicates a stronger positive linear correlation of ranking, which suggests better alignment. To ensure robustness, we calculate averaged ⟦SLOT_44⟧ from five random and independent splits for the global (per-artist) sampling scheme, while for per-task sampling, we correlate each independent task. Considering the size of independent test and typical ⟦SLOT_45⟧ values, we combine ⟦SLOT_46⟧ using Pearson’s and Fisher’s method for per-artist and per-task scenario, respectively, as suggested by (Heard and Rubin-Delanchy 2018). A lower ⟦SLOT_47⟧ value means stronger statistical significance.

**ZH** 对齐度指标。沿用（Jiang 与 Chen，2024；Chen 等，2024；Zhang 等，2023a），我们使用 Spearman 相关系数（Spearman，1987）来量化专家判断与 MLLM 判断之间的对齐度。Spearman’s ⟦SLOT_43⟧ 越接近 1，表示排名的正线性相关越强，即对齐度越好。为保证稳健性，在全局（按艺术家）采样方案下，我们从五次随机独立的划分中计算平均的 ⟦SLOT_44⟧；在按任务采样下，则对每个独立任务分别求相关。考虑到独立检验的规模与典型的 ⟦SLOT_45⟧ 取值，我们按（Heard 与 Rubin-Delanchy，2018）的建议，分别用 Pearson 方法与 Fisher 方法合并 ⟦SLOT_46⟧，对应按艺术家与按任务两种场景。⟦SLOT_47⟧ 值越低表示统计显著性越强。

**EN** Compared Methods As the first exploration on MLLMs for aesthetic reasoning, finding direct comparisons can be challenging. Therefore we broadly compare three groups of methods. (a), IQA methods: including CLIP-IQA (Wang et al. 2023) and Compare2Score (Zhu et al. 2024); (b) Text-image alignment and preference scores: CLIP Score (Radford et al. 2021), Aesthetic Predictor (Schuhmann et al. 2022), PickScore (Kirstain et al. 2023) and HPSv2 (Wu et al. 2023). Despite ArtScore (Chen et al. 2024) share the most similar objective with this paper, we exclude it due to the unavailability of code at the time this paper was written. We consider (3) Zero-shot MLLMs, where we use three mainstream MLLMs as base model, including GPT-4o (OpenAI 2023), Gemini 1.5 (Team et al. 2023), and Claude 3.5 (Anthropic [n. d.]). We apply different MLLM reasoning methods, including base (directly output the winner), zero-shot CoT and the proposed ArtCoT. We also consider recent reasoning MLLMs, including Claude-3.7-sonnet-reasoning and Gemini-2.0-flash-thinking. The experiment of all MLLMs are repeated thrice with default hyper-parameters to ensure robustness.

**ZH** 对比方法。作为 MLLM 用于审美推理的首次探索，找到直接可比的方法并不容易。因此我们宽泛地比较三组方法。（a）IQA 方法：包括 CLIP-IQA（Wang 等，2023）与 Compare2Score（Zhu 等，2024）；（b）图文对齐与偏好分数：CLIP Score（Radford 等，2021）、Aesthetic Predictor（Schuhmann 等，2022）、PickScore（Kirstain 等，2023）与 HPSv2（Wu 等，2023）。尽管 ArtScore（Chen 等，2024）与本文目标最为接近，由于本文撰写时代码不可用，我们将其排除。我们还考虑（3）零样本 MLLM，使用三个主流 MLLM 作为基座模型，包括 GPT-4o（OpenAI，2023）、Gemini 1.5（Team 等，2023）与 Claude 3.5（Anthropic，[n. d.]）。我们应用不同的 MLLM 推理方法，包括基础方法（直接输出胜者）、零样本 CoT 与所提出的 ArtCoT。我们还考虑近期的推理型 MLLM，包括 Claude-3.7-sonnet-reasoning 与 Gemini-2.0-flash-thinking。所有 MLLM 的实验均使用默认超参数重复三次，以保证稳健性。

**EN** 4.2. Human Judgment Collection

**ZH** 4.2. 人类判断采集

**EN** We recruit 18 human experts with general knowledge of fine art for annotation. We collected a total of 80,000 initial judgments. For per-task sampling, we sample ⟦SLOT_48⟧ for each task. We prune uncertain human feedback with ⟦SLOT_49⟧, and remove non-transitive task with ⟦SLOT_50⟧. As a result, 20.1% of the feedback is filtered out due to pairwise divergence, while the remaining 15.3% are removed due to a high non-transitivity. To quantify the inter-annotation agreement, we use McFadden’s ⟦SLOT_51⟧ (McFadden 1972) to assess the transitivity of global ranking constructed from BT and Elo, reported in Tab. 3. A ⟦SLOT_52⟧ is generally considered as a good fit, which implies the judgment are statistically consistent.

**ZH** 我们招募 18 位具备美术通识的人类专家进行标注，共采集 80,000 条初始判断。在按任务采样下，我们为每个任务采样 ⟦SLOT_48⟧。我们用 ⟦SLOT_49⟧ 剪除不确定的人类反馈，并用 ⟦SLOT_50⟧ 移除非传递任务。结果，20.1% 的反馈因成对分歧被过滤，另有 15.3% 因高非传递性被移除。为量化标注者间一致性，我们使用 McFadden’s ⟦SLOT_51⟧（McFadden，1972）评估由 BT 与 Elo 构造的全局排名的传递性，结果见表 3。⟦SLOT_52⟧ 通常被视为拟合良好，意味着判断在统计上是一致的。

**EN** Table 3. Inter-Annotator Agreement. Higher goodness-of-fit ⟦SLOT_53⟧ indicate more concordant global ranking.

**ZH** 表 3. 标注者间一致性。拟合优度 ⟦SLOT_53⟧ 越高，表示全局排名越一致。

<!-- [原子块 · table] Raw + prune uncertain + drop non-transitive R 2 ↑ R^{2}\uparrow 0.17 0.26 0.31 -->

**EN** 4.3. Main Result: Human Alignment

**ZH** 4.3. 主要结果：与人类的对齐度

**EN** We compare the correlation and statistical significance of different MLLMs and prompts using two sampling strategies. The results in Tab. 1 demonstrate a substantial advantage of aesthetic reasoning for enhancing MLLMs’ ability to judge aesthetics, achieving average improvements of 44%, 30% in the per-artist and per-task setup, respectively. When compared with other specialized IQA or preference models, MLLMs prompted with ArtCoT demonstrate state-of-the-art alignment even without any targeted optimization. By contrast, we observe that zero-shot CoT adversely affects alignment, decreasing it by 16% and 18% on average. Overall, these results prove that (1) reasoning can indeed make MLLMs human-aligned aesthetic evaluators, and (2) conditioned on proper elicitation of their reasoning capability.

**ZH** 我们用两种采样策略比较不同 MLLM 与提示的相关性及统计显著性。表 1 的结果显示，审美推理在提升 MLLM 审美判断能力上具有显著优势，在按艺术家与按任务设置下分别取得 44% 与 30% 的平均提升。与专用的 IQA 或偏好模型相比，以 ArtCoT 提示的 MLLM 即便未做任何针对性优化，也达到了最优的对齐度。相反，我们观察到零样本 CoT 对对齐度有负面影响，平均使其下降 16% 与 18%。总体而言，这些结果证明：（1）推理确实能使 MLLM 成为与人类对齐的审美评估器；（2）这以其推理能力得到恰当激发为条件。

**EN** 5. Analysis and Discussion

**ZH** 5. 分析与讨论

**EN** Table 4. Response subjectivity and hallucination from different prompting methods. We report the average length of thinking trace (in words), two subjectivity metrics, and human-annotated hallucination score (normalized) from four perspectives. Reasoning traces generated with ArtCoT contain less subjectivity and hallucination. (*): Trace from Claude-3.7-sonnet-thinking.

**ZH** 表 4. 不同提示方法下的响应主观性与幻觉。我们报告思考轨迹的平均长度（词数）、两项主观性指标，以及从四个视角人工标注的幻觉分数（归一化）。用 ArtCoT 生成的推理轨迹主观性与幻觉更少。（*）来自 Claude-3.7-sonnet-thinking 的轨迹。

<!-- [原子块 · table] Method Avg. length Response Subjectivity Hallucination (Factuality) Hallucination (Extrinsic) TextBlob ↓ \downarrow Word frequency ( % \% ) ↓ \downarrow Visual ↓ \downarrow Textual ↓ \downarrow Opinio -->

<!-- [原子块 · img]  -->

**EN** Figure 4. A minimal example of the hallucination issue. In particular, the frequent use of opinionated and artistic interpretation words degrades MLLM’s aesthetic judgment.

**ZH** 图 4. 幻觉问题的最小示例。特别是，主观性词语与艺术阐释类词语的频繁使用损害了 MLLM 的审美判断。

**EN** 5.1. Zero-shot CoT Reinforces Hallucination

**ZH** 5.1. 零样本 CoT 会强化幻觉

**EN** During aesthetic reasoning of artworks, MLLMs exhibit a bias towards subjective "feeling" rather than objective "reasoning." This tendency can significantly degrade an MLLM’s aesthetic judgment, leading to the counter-intuitive result where zero-shot CoT negatively impacts alignment with human perception. Our findings suggest that this issue stems from hallucination, particularly concerning the use of subjective language during the reasoning process.

**ZH** 在对艺术品做审美推理时，MLLM 表现出偏向主观“感受”而非客观“推理”的倾向。这种倾向会显著损害 MLLM 的审美判断，导致零样本 CoT 反而降低与人类知觉的对齐度这一反直觉结果。我们的发现表明，问题源于幻觉，尤其是推理过程中主观语言的使用。

**EN** Specifically, in the zero-shot CoT setting, we observe that MLLMs tend to arrive at rapid conclusions, employing subjective and less concrete language to justify their judgments. This hallucination is distinctive and can be broadly categorized into two types. The first is the use of opinionated and subjective words. For instance, opinion verbs (e.g., “feels”, “senses”) and hedge words (e.g., “appears”, “seemingly”) are frequently employed. These terms often indicate a lack of in-depth consideration, weak logical connection to the given task and are less supportive for aesthetic judgment (Sircello 1968). Furthermore, the MLLMs may generate ostensible “artistic interpretations” that are superficial and not substantiated with facts or explanations. These hallucinations are consistently observed across different MLLMs when prompted with zero-shot CoT, which is broadly in line with recent findings (Liu et al. 2024; Huang et al. 2025). Illustrative conversation examples are provided in Appendix B. Our analysis in the subsequent section further corroborates this observation.

**ZH** 具体而言，在零样本 CoT 设置下，我们观察到 MLLM 倾向于迅速得出结论，并用主观、不够具体的语言来论证其判断。这种幻觉特征鲜明，可大致归为两类。第一类是主观与意见性词语的使用。例如，意见动词（如“feels”“senses”）与模糊限定词（如“appears”“seemingly”）被频繁使用。这些表述往往表明思考不够深入、与给定任务的逻辑联系薄弱，对审美判断的支持作用有限（Sircello，1968）。此外，MLLM 可能生成表面化的“艺术阐释”，它们流于表层且没有事实或解释支撑。在以零样本 CoT 提示时，这类幻觉在不同 MLLM 上一致出现，这与近期发现（Liu 等，2024；Huang 等，2025）大体吻合。示例对话见附录 B，后续小节的分析进一步佐证了这一观察。

**EN** 5.2. Evidence-based Reasoning Suppress Subjectivity and Hallucination

**ZH** 5.2. 基于证据的推理抑制主观性与幻觉

**EN** Compared with the base prompting and zero-shot CoT, the thinking traces produced by ArtCoT are more concise, objective, and closely aligned with the input, as exemplified in Fig. 4. To quantify this improvement, we analyze the thinking traces in detail. Specifically, we first (1) measure the subjectivity of responses by calculating the frequency of subjective verbs in the lemmatized responses of MLLMs. We also follow established practices in natural language processing (NLP) by performing lexicon-based subjectivity analysis using the TextBlob package, which provides a score in the range of 0 to 1 (with a higher score indicating greater subjectivity).

**ZH** 与基础提示和零样本 CoT 相比，ArtCoT 产生的思考轨迹更简洁、更客观，也更贴合输入，如图 4 所示。为量化这一改进，我们对思考轨迹做了细致分析。具体而言，我们首先（1）通过计算 MLLM 词形还原后响应中主观动词的出现频率来度量响应的主观性。我们还沿用自然语言处理（NLP）中的既定做法，使用 TextBlob 工具包进行基于词典的主观性分析，该工具给出 0 到 1 区间内的分数（分数越高表示主观性越强）。

**EN** Moreover, (2) during human annotation, we present the misaligned 2AFC questions to users for fine-grained hallucination labeling. Similarly, we categorize hallucinations into two types: (a) Factual Errors, which include incorrect image recognition (visual) and inaccurate style explanations (textual) — often referred to as intrinsic hallucinations, as they can be directly deduced from the input; and (b) Extrinsic Hallucinations, comprising opinionated responses and artistic interpretations. Users are tasked with reading the MLLM’s thinking trace and rating the severity of hallucinations on a scale of [0,1,2] for each of the four factors. We summarize the results for both experiments in Tab. 4.

**ZH** 此外，（2）在人工标注环节，我们把错位的 2AFC 问题呈现给用户做细粒度的幻觉标注。同样地，我们把幻觉分为两类：（a）事实性错误，包括错误的图像识别（视觉）与不准确的风格解释（文本）——通常称为内在幻觉，因为它们可直接由输入推断；（b）外在幻觉，包括意见性回应与艺术阐释。用户需阅读 MLLM 的思考轨迹，并就四个因素各自在 [0,1,2] 量表上评定幻觉严重程度。两项实验的结果汇总于表 4。

**EN** The experiment results offer insights into the hallucination challenge faced by MLLMs. Firstly, human evaluation reveals that all models exhibit relatively less severe hallucinations in terms of visual and textual aspects. This suggests that factual inaccuracies are not the primary source of hallucinations in this context. Instead, the prevalent use of subjective language, characterized by opinionated expressions and unsubstantiated artistic interpretations, significantly impedes the ability of MLLMs to align their aesthetic judgments with those of humans. Moreover, the elevated response subjectivity observed in zero-shot CoT, as evidenced by the remarkably consistent TextBlob scores (⟦SLOT_54⟧) and the frequency of subjective words, provides further support for this assertion.

**ZH** 实验结果为 MLLM 面临的幻觉难题提供了洞见。首先，人工评估显示，所有模型在视觉与文本方面的幻觉都相对较轻。这说明事实性不准确并非此情境下幻觉的主要来源。相反，主观语言的普遍使用——表现为意见性表达与缺乏依据的艺术阐释——显著阻碍了 MLLM 把审美判断与人类对齐。此外，零样本 CoT 中观察到的响应主观性升高，由高度一致的 TextBlob 分数（⟦SLOT_54⟧）与主观词频所佐证，进一步支持了这一论断。

**EN** In other words, this experiment reinforces our finding that the bottleneck for MLLMs in art evaluation does not reside in their recognition capabilities—as all models demonstrate a relatively clear comprehension of the input. Rather, the challenge lies in effectively eliciting their reasoning capability by mitigating the hallucinations stemming from subjective expressions. We have also shown that this challenge is surmountable, as an evidence-based and reflective reasoning approach like ArtCoT enables a substantial suppression of subjectivity and hallucination, bringing a significant improvement in human alignment.

**ZH** 换言之，该实验强化了我们的发现：MLLM 在艺术评估中的瓶颈并不在识别能力——所有模型都表现出对输入相对清晰的理解——而在于如何通过缓解源自主观表达的幻觉来有效激发其推理能力。我们也证明这一挑战可以被克服：像 ArtCoT 这样基于证据、带反思的推理方法能够大幅抑制主观性与幻觉，从而显著提升与人类的对齐度。

<!-- [原子块 · img]  -->

**EN** Figure 5. Fine-grained comparison of different MLLM prompting scheme. We show the spearman’s ⟦SLOT_55⟧ for per-instance alignment, grouped by representative attribute in FineArtBench. ArtCoT elicits aesthetic reasoning in all scenarios, especially for tasks with a specific style instruction.

**ZH** 图 5. 不同 MLLM 提示方案的细粒度比较。我们按 FineArtBench 中的代表性属性分组，展示逐实例对齐的 Spearman’s ⟦SLOT_55⟧。ArtCoT 在所有场景下都激发了审美推理，对带有具体风格指令的任务尤其明显。

**EN** 5.3. Multifaceted Aesthetic Reasoning is Versatile

**ZH** 5.3. 多面的审美推理具有通用性

**EN** The semantic label in FineArtBench enables finegrained understanding of MLLM’s performance. For instance, in Fig. 5 , we visualize the alignment performance on different content image complexity and style prompt categories.

**ZH** FineArtBench 中的语义标签使我们可以细粒度地理解 MLLM 的表现。例如，在图 5 中，我们可视化了在不同内容图像复杂度与风格提示类别上的对齐表现。

**EN** The proposed ArtCoT outperforms both base and zero-shot CoT prompting in all examined sub-classes, demonstrating its versatility. The most notable improvements are observed in tasks that with concrete style instructions. For example, we notice a significant improvement of “long prompt” and prompts specifying particular “art movement”. We posit that longer prompts and mentioning of art movement set a more concrete objective for both the art creation evaluation (Bai et al. 2024). Compared with obscure instructions, this specificity facilitates the MLLM to more objectively perform the two-hop reasoning, resulting in reduced hallucination and improved human alignment (Huang et al. 2025; Wei et al. 2022; Guo et al. 2025a; Bai et al. 2024).

**ZH** 所提出的 ArtCoT 在所有被考察的子类上都优于基础提示与零样本 CoT，展现了其通用性。最显著的提升出现在带有具体风格指令的任务上。例如，我们注意到“长提示”与指定特定“艺术运动”的提示有明显改善。我们认为，更长的提示与对艺术运动的提及为艺术创作评估设定了更具体的目标（Bai 等，2024）。与含糊的指令相比，这种具体性有助于 MLLM 更客观地执行两跳推理，从而减少幻觉并提升与人类的对齐度（Huang 等，2025；Wei 等，2022；Guo 等，2025a；Bai 等，2024）。

**EN** 5.4. Ablations.

**ZH** 5.4. 消融实验。

**EN** Components of ArtCoT. We ablate the key components of ArtCoT, specifically the CS analyzer and the art critic, and report the results in Tab. 5. The complete ArtCoT prompt achieves the highest aesthetic alignment. Particularly, removing the art critic phase induces the most significant decline, underscoring its critical role. This provides further evidence that reasoning is the key bottleneck.

**ZH** ArtCoT 的组成部分。我们对 ArtCoT 的关键组件——CS Analyzer 与 Art Critic——做消融，结果见表 5。完整的 ArtCoT 提示取得最高的审美对齐度。其中，移除 Art Critic 阶段造成的下降最为显著，凸显了它的关键作用。这进一步证明推理是关键瓶颈。

**EN** Input to MLLM. We ablate input modalities and image resolutions, with results reported in Tab. 6. The full resolution achieves the best result. This is because the details in artworks, such as strokes, are important factors of aesthetics. For input modalities, providing style information is important in per-artist alignment, while including the reference image affects per-instance alignment the most. For either setting, providing all input modalities achieves the best alignment, meaning that task-constrained 2AFC aids objective aesthetic reasoning and judgment to be human-aligned.

**ZH** MLLM 的输入。我们对输入模态与图像分辨率做消融，结果见表 6。全分辨率取得最佳结果，因为作品中的细节（如笔触）是审美的重要因素。就输入模态而言，提供风格信息对按艺术家对齐很重要，而包含参考图像对逐实例对齐影响最大。在两种设置下，提供全部输入模态都能取得最佳对齐，说明受任务约束的 2AFC 有助于客观的审美推理，并使判断与人类对齐。

**EN** Table 5. Ablation on component of ArtCoT. We ablate the content/style analyzer and the art critic. The full two-hop aesthetics reasoning facilitates human-aligned judgment.

**ZH** 表 5. ArtCoT 组件的消融。我们对内容／风格分析器与艺术批评者做消融。完整的两跳审美推理促成了与人类对齐的判断。

<!-- [原子块 · table] CS-analyzer Art Critic Per-artist ρ \rho ↑ \uparrow Per-task ρ \rho ↑ \uparrow ✗ ✓ 0.630 0.532 ✓ ✗ 0.531 0.366 ✓ ✓ 0.739 0.607 -->

**EN** Table 6. Ablation on image resolution and source information. We report the correlation ⟦SLOT_56⟧ (averaged from BT and Elo) of different input setups: content image, style prompt, and image sub-sampling factor.

**ZH** 表 6. 图像分辨率与来源信息的消融。我们报告不同输入设置下的相关性 ⟦SLOT_56⟧（由 BT 与 Elo 平均得到）：内容图像、风格提示与图像子采样因子。

<!-- [原子块 · table] Content Style Resolution Per-artist ρ \rho ↑ \uparrow Per-task ρ \rho ↑ \uparrow ✓ ✓ 1/2 0.630 -42% 0.432 -44% ✓ ✓ 1/4 0.502 -91% 0.285 -82% ✗ ✗ full 0.476 -100% 0.416 -49% ✗ ✓ full 0.678 -23% 0.465 - -->

**EN** 5.5. Boarder Impact

**ZH** 5.5. 更广泛的影响

**EN** We have demonstrated that evidence-based reasoning makes MLLMs human-aligned art evaluators. A lot of applications can benefit from this exploration, both in terms of RLAIF and HCI. Fig. 6 provides an illustration of how generative art may benefit from the reward signals with aesthetic reasoners to improve the generation, utilizing a pipeline akin to (Guo et al. 2025b). A similar pipeline may also be employed for human-centered and interactive art education.

**ZH** 我们已证明，基于证据的推理使 MLLM 成为与人类对齐的艺术评估器。大量应用可从这一探索中获益，无论就 RLAIF 还是 HCI 而言。图 6 展示了生成式艺术如何利用带审美推理者的奖励信号来改进生成，其流程类似于（Guo 等，2025b）。类似的流程也可用于以人为中心、可交互的艺术教育。

<!-- [原子块 · img]  -->

**EN** Figure 6. A minimal illustration of ArtCoT-enhanced art generation.

**ZH** 图 6. ArtCoT 增强的艺术生成的最小示意。

**EN** 5.6. Limitations and Future Works

**ZH** 5.6. 局限与未来工作

**EN** Aesthetics, as a subject studied for centuries, possesses complexities that cannot be fully addressed in a single paper. Numerous avenues for improvement exist, with the most significant challenge being the computational modeling of inter-person subjectivity. One possible technical direction involves conditioning Eq. 2 with the audience identity to enable personalized aesthetic models. A deeper understanding of the human part provides valuable insights, such as the philosophical theories and discussion on aesthetic judgment (Kant 2024; Sircello 1968; Hullman et al. 2023).

**ZH** 美学作为一门被研究了数个世纪的学科，其复杂性无法在单篇论文中穷尽。可改进的方向很多，其中最大的挑战是对个体间主观性做计算建模。一个可能的技术方向是把式 2 以受众身份为条件，从而实现个性化的审美模型。对人类一侧的更深入理解也能带来有价值的认识，例如关于审美判断的哲学理论与讨论（Kant，2024；Sircello，1968；Hullman 等，2023）。

**EN** 6. Conclusion

**ZH** 6. 结论

**EN** The concept of aesthetics has been largely simplified in existing algorithms. Without explicitly modeling the cognitive process underlying human aesthetic judgment, computational models can never truly align how humans perceive beauty and produce artistically impactful artworks. This paper pioneers this exploration by capturing such aesthetic reasoning process with MLLMs. Our experiments reveal a key bottleneck in applying MLLMs for aesthetic reasoning: the proper elicitation of reasoning capability during inference rather than relying solely on the base model. In-depth analysis further highlights the hallucination issues stemming from subjective opinions and unsubstantiated interpretations, leading to misaligned judgments. We further identify a promising solution through an evidence-based and objective reasoning process. These valuable findings can inspire future AI models to align with human aesthetic perception.

**ZH** 审美的概念在现有算法中被大幅简化。若不显式建模人类审美判断背后的认知过程，计算模型永远无法真正对齐人类对美的知觉，也无法产出具有艺术感染力的作品。本文通过用 MLLM 捕捉这一审美推理过程，开创了这一探索。我们的实验揭示了把 MLLM 用于审美推理时的关键瓶颈：推理时能否恰当激发模型的推理能力，而非仅仅依赖基座模型。深入的分析进一步凸显了源自主观意见与缺乏依据的阐释的幻觉问题，它们导致判断错位。我们还指出了一条有前景的解决路径：基于证据的客观推理过程。这些有价值的发现可启发未来的 AI 模型与人类审美知觉对齐。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] (1) -->

<!-- [原子块 · verbatim] An et al . (2021) Jie An, Siyu Huang, Yibing Song, Dejing Dou, Wei Liu, and Jiebo Luo. 2021. Artflow: Unbiased image style transfer via reversible neural flows. In Proceedings of the IEEE/CVF Conferen -->

<!-- [原子块 · verbatim] Andrade et al . (2014) Heidi Andrade, Joanna Hefferen, and Maria Palma. 2014. Formative assessment in the visual arts. Art Education 67, 1 (2014), 34–40. -->

<!-- [原子块 · verbatim] Anthropic ([n. d.]) Anthropic. [n. d.]. Meet Claude. https://www.anthropic.com/claude . -->

<!-- [原子块 · verbatim] Bai et al . (2024) Zechen Bai, Pichao Wang, Tianjun Xiao, Tong He, Zongbo Han, Zheng Zhang, and Mike Zheng Shou. 2024. Hallucination of multimodal large language models: A survey. arXiv preprint arXiv -->

<!-- [原子块 · verbatim] Barnet (2015) Sylvan Barnet. 2015. A short guide to writing about art . Pearson Upper Saddle River, NJ. -->

<!-- [原子块 · verbatim] Black et al . (2023) Kevin Black, Michael Janner, Yilun Du, Ilya Kostrikov, and Sergey Levine. 2023. Training diffusion models with reinforcement learning. arXiv preprint arXiv:2305.13301 (2023). -->

<!-- [原子块 · verbatim] Bo et al . (2018) Yihang Bo, Jinhui Yu, and Kang Zhang. 2018. Computational aesthetics and applications. Visual computing for industry, biomedicine, and art 1 (2018), 1–19. -->

<!-- [原子块 · verbatim] Bradley and Terry (1952) Ralph Allan Bradley and Milton E Terry. 1952. Rank analysis of incomplete block designs: I. The method of paired comparisons. Biometrika 39, 3/4 (1952), 324–345. -->

<!-- [原子块 · verbatim] Brooks et al . (2023) Tim Brooks, Aleksander Holynski, and Alexei A Efros. 2023. Instructpix2pix: Learning to follow image editing instructions. In Proceedings of the IEEE/CVF Conference on Computer V -->

<!-- [原子块 · verbatim] Chamberlain et al . (2018) Rebecca Chamberlain, Caitlin Mullin, Bram Scheerlinck, and Johan Wagemans. 2018. Putting the art in artificial: Aesthetic responses to computer-generated art. Psychology of  -->

<!-- [原子块 · verbatim] Chen et al . (2024) Junyu Chen, Jie An, Hanjia Lyu, Christopher Kanan, and Jiebo Luo. 2024. Learning to Evaluate the Artness of AI-generated Images. IEEE Transactions on Multimedia (2024). -->

<!-- [原子块 · verbatim] Christensen and Ball (2016) Bo T Christensen and Linden J Ball. 2016. Dimensions of creative evaluation: Distinct design and reasoning strategies for aesthetic, functional and originality judgments. D -->

<!-- [原子块 · verbatim] Chung et al . (2024) Jiwoo Chung, Sangeek Hyun, and Jae-Pil Heo. 2024. Style injection in diffusion: A training-free approach for adapting large-scale diffusion models for style transfer. In Proceedin -->

<!-- [原子块 · verbatim] Clark et al . (2023) Kevin Clark, Paul Vicol, Kevin Swersky, and David J Fleet. 2023. Directly fine-tuning diffusion models on differentiable rewards. arXiv preprint arXiv:2309.17400 (2023). -->

<!-- [原子块 · verbatim] Coleman (1966) Francis J Coleman. 1966. A phenomenology of aesthetic reasoning. The Journal of Aesthetics and Art Criticism 25, 2 (1966), 197–203. -->

<!-- [原子块 · verbatim] Deng et al . (2022) Yingying Deng, Fan Tang, Weiming Dong, Chongyang Ma, Xingjia Pan, Lei Wang, and Changsheng Xu. 2022. Stytr2: Image style transfer with transformers. In Proceedings of the IEEE/CVF  -->

<!-- [原子块 · verbatim] Elgammal et al . (2017) Ahmed Elgammal, Bingchen Liu, Mohamed Elhoseiny, and Marian Mazzone. 2017. Can: Creative adversarial networks, generating" art" by learning about styles and deviating from styl -->

<!-- [原子块 · verbatim] Elo and Sloan (1978) Arpad E Elo and Sam Sloan. 1978. The rating of chessplayers: Past and present. (No Title) (1978). -->

<!-- [原子块 · verbatim] Gao et al . (2024) Junyao Gao, Yanchen Liu, Yanan Sun, Yinhao Tang, Yanhong Zeng, Kai Chen, and Cairong Zhao. 2024. Styleshot: A snapshot on any style. arXiv preprint arXiv:2407.01414 (2024). -->

<!-- [原子块 · verbatim] Gatys et al . (2016) Leon A Gatys, Alexander S Ecker, and Matthias Bethge. 2016. Image style transfer using convolutional neural networks. In Proceedings of the IEEE conference on computer vision and  -->

<!-- [原子块 · verbatim] Ghose (2017) Tia Ghose. 2017. This AI Helps You Paint Like Van Gogh. https://www.livescience.com/60536-ai-helps-you-paint-like-van-gogh.html . Live Science (sep 2017). Accessed: 2025-04-09. -->

<!-- [原子块 · verbatim] Gips and Stiny (1975) James Gips and George Stiny. 1975. An investigation of algorithmic aesthetics. Leonardo 8, 3 (1975), 213–220. -->

<!-- [原子块 · verbatim] Gombrich and Gombrich (1995) Ernst Hans Gombrich and EH Gombrich. 1995. The story of art . Vol. 12. Phaidon London. -->

<!-- [原子块 · verbatim] Groenendijk et al . (2020) Talita Groenendijk, Andrea Kárpáti, and Folkert Haanstra. 2020. Self-Assessment in art education through a visual rubric. International Journal of Art & Design Education 39, -->

<!-- [原子块 · verbatim] Guo et al . (2025a) Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al . 2025a. Deepseek-r1: Incentivizing reasoning capabilit -->

<!-- [原子块 · verbatim] Guo et al . (2025b) Ziyu Guo, Renrui Zhang, Chengzhuo Tong, Zhizheng Zhao, Peng Gao, Hongsheng Li, and Pheng-Ann Heng. 2025b. Can We Generate Images with CoT? Let’s Verify and Reinforce Image Generati -->

<!-- [原子块 · verbatim] Hao et al . (2024) Shibo Hao, Sainbayar Sukhbaatar, DiJia Su, Xian Li, Zhiting Hu, Jason Weston, and Yuandong Tian. 2024. Training large language models to reason in a continuous latent space. arXiv p -->

<!-- [原子块 · verbatim] Heard and Rubin-Delanchy (2018) Nicholas A Heard and Patrick Rubin-Delanchy. 2018. Choosing between methods of combining-values. Biometrika 105, 1 (2018), 239–246. -->

<!-- [原子块 · verbatim] Hegel and Hegel (1998) Georg Wilhelm Friedrich Hegel and GWF Hegel. 1998. Aesthetics: Lectures on fine art . Vol. 1. Oxford University Press. -->

<!-- [原子块 · verbatim] Hentschel et al . (2022) Simon Hentschel, Konstantin Kobs, and Andreas Hotho. 2022. CLIP knows image aesthetics. Frontiers in Artificial Intelligence 5 (2022), 976235. -->

<!-- [原子块 · verbatim] Heusel et al . (2017) Martin Heusel, Hubert Ramsauer, Thomas Unterthiner, Bernhard Nessler, and Sepp Hochreiter. 2017. Gans trained by a two time-scale update rule converge to a local nash equilibrium -->

<!-- [原子块 · verbatim] Huang et al . (2025) Lei Huang, Weijiang Yu, Weitao Ma, Weihong Zhong, Zhangyin Feng, Haotian Wang, Qianglong Chen, Weihua Peng, Xiaocheng Feng, Bing Qin, et al . 2025. A survey on hallucination in la -->

<!-- [原子块 · verbatim] Huang et al . (2024b) Nisha Huang, Yuxin Zhang, Fan Tang, Chongyang Ma, Haibin Huang, Weiming Dong, and Changsheng Xu. 2024b. Diffstyler: Controllable dual diffusion for text-driven image stylization. -->

<!-- [原子块 · verbatim] Huang and Belongie (2017) Xun Huang and Serge Belongie. 2017. Arbitrary style transfer in real-time with adaptive instance normalization. In Proceedings of the IEEE international conference on compute -->

<!-- [原子块 · verbatim] Huang et al . (2024a) Yipo Huang, Xiangfei Sheng, Zhichao Yang, Quan Yuan, Zhichao Duan, Pengfei Chen, Leida Li, Weisi Lin, and Guangming Shi. 2024a. Aesexpert: Towards multi-modality foundation model -->

<!-- [原子块 · verbatim] Hullman et al . (2023) Jessica Hullman, Ari Holtzman, and Andrew Gelman. 2023. Artificial intelligence and aesthetic judgment. arXiv preprint arXiv:2309.12338 (2023). -->

<!-- [原子块 · verbatim] Hume (1757) David Hume. 1757. Of the Standard of Taste. Essays, Moral, Political, and Literary (1757). https://oll.libertyfund.org/titles/hume-essays-moral-political-literary-lf-ed -->

<!-- [原子块 · verbatim] Ioannou and Maddock (2024) Eleftherios Ioannou and Steve Maddock. 2024. Evaluation in Neural Style Transfer: A Review. In Computer Graphics Forum . Wiley Online Library, e15165. -->

<!-- [原子块 · verbatim] Isik and Vessel (2021) Ayse Ilkay Isik and Edward A Vessel. 2021. From visual perception to aesthetic appeal: Brain responses to aesthetically appealing natural landscape movies. Frontiers in Human Ne -->

<!-- [原子块 · verbatim] Jiang and Chen (2024) Ruixiang Jiang and Changwen Chen. 2024. Artist: Aesthetically Controllable Text-Driven Stylization without Training. arXiv preprint arXiv:2407.15842 (2024). -->

<!-- [原子块 · verbatim] Joshi et al . (2011) Dhiraj Joshi, Ritendra Datta, Elena Fedorovskaya, Quang-Tuan Luong, James Z Wang, Jia Li, and Jiebo Luo. 2011. Aesthetics and emotions in images. IEEE Signal Processing Magazine 2 -->

<!-- [原子块 · verbatim] Kant (2024) Immanuel Kant. 2024. Critique of judgment . Vol. 10. Minerva Heritage Press. -->

<!-- [原子块 · verbatim] Ke et al . (2023) Junjie Ke, Keren Ye, Jiahui Yu, Yonghui Wu, Peyman Milanfar, and Feng Yang. 2023. Vila: Learning image aesthetics from user comments with vision-language pretraining. In Proceedings  -->

<!-- [原子块 · verbatim] Kim et al . (2022) Diana Kim, Ahmed Elgammal, and Marian Mazzone. 2022. Formal analysis of art: Proxy learning of visual concepts from style through language models. arXiv preprint arXiv:2201.01819 (2 -->

<!-- [原子块 · verbatim] Kirillov et al . (2023) Alexander Kirillov, Eric Mintun, Nikhila Ravi, Hanzi Mao, Chloe Rolland, Laura Gustafson, Tete Xiao, Spencer Whitehead, Alexander C Berg, Wan-Yen Lo, et al . 2023. Segment anyt -->

<!-- [原子块 · verbatim] Kirstain et al . (2023) Yuval Kirstain, Adam Polyak, Uriel Singer, Shahbuland Matiana, Joe Penna, and Omer Levy. 2023. Pick-a-pic: An open dataset of user preferences for text-to-image generation. Adv -->

<!-- [原子块 · verbatim] Kojima et al . (2022) Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yutaka Matsuo, and Yusuke Iwasawa. 2022. Large language models are zero-shot reasoners. Advances in neural information processing  -->

<!-- [原子块 · verbatim] Li et al . (2024) Daiqing Li, Aleks Kamko, Ehsan Akhgari, Ali Sabet, Linmiao Xu, and Suhail Doshi. 2024. Playground v2. 5: Three insights towards enhancing aesthetic quality in text-to-image generatio -->

<!-- [原子块 · verbatim] Li et al . (2023) Leida Li, Yipo Huang, Jinjian Wu, Yuzhe Yang, Yaqian Li, Yandong Guo, and Guangming Shi. 2023. Theme-aware visual attribute reasoning for image aesthetics assessment. IEEE Transactio -->

<!-- [原子块 · verbatim] Liao et al . (2022) Peiyuan Liao, Xiuyu Li, Xihui Liu, and Kurt Keutzer. 2022. The artbench dataset: Benchmarking generative models with artworks. arXiv preprint arXiv:2206.11404 (2022). -->

<!-- [原子块 · verbatim] Lin et al . (2014) Tsung-Yi Lin, Michael Maire, Serge Belongie, James Hays, Pietro Perona, Deva Ramanan, Piotr Dollár, and C Lawrence Zitnick. 2014. Microsoft coco: Common objects in context. In Compu -->

<!-- [原子块 · verbatim] Lindell and Mueller (2011) Annukka K Lindell and Julia Mueller. 2011. Can science account for taste? Psychological insights into art appreciation. Journal of Cognitive Psychology 23, 4 (2011), 453–475 -->

<!-- [原子块 · verbatim] Lindsey et al . (2025) Jack Lindsey, Wes Gurnee, Emmanuel Ameisen, Brian Chen, Adam Pearce, Nicholas L. Turner, Craig Citro, David Abrahams, Shan Carter, Basil Hosmer, Jonathan Marcus, Michael Sklar,  -->

<!-- [原子块 · verbatim] Liu et al . (2024) Ryan Liu, Jiayi Geng, Addison J Wu, Ilia Sucholutsky, Tania Lombrozo, and Thomas L Griffiths. 2024. Mind your step (by step): Chain-of-thought can reduce performance on tasks where  -->

<!-- [原子块 · verbatim] McFadden (1972) Daniel McFadden. 1972. Conditional logit analysis of qualitative choice behavior. Frontiers in Econometrics (1972). -->

<!-- [原子块 · verbatim] Mitra et al . (2024) Chancharik Mitra, Brandon Huang, Trevor Darrell, and Roei Herzig. 2024. Compositional chain-of-thought prompting for large multimodal models. In Proceedings of the IEEE/CVF Confer -->

<!-- [原子块 · verbatim] OpenAI (2023) R OpenAI. 2023. Gpt-4 technical report. arxiv 2303.08774. View in Article 2, 5 (2023). -->

<!-- [原子块 · verbatim] Ortlieb and Carbon (2019) Stefan A Ortlieb and Claus-Christian Carbon. 2019. A functional model of kitsch and art: linking aesthetic appreciation to the dynamics of social motivation. Frontiers in psy -->

<!-- [原子块 · verbatim] Palmer et al . (2013) Stephen E Palmer, Karen B Schloss, and Jonathan Sammartino. 2013. Visual aesthetics and human preference. Annual review of psychology 64, 1 (2013), 77–107. -->

<!-- [原子块 · verbatim] Radford et al . (2021) Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, et al . 2021. Learning transf -->

<!-- [原子块 · verbatim] Rombach et al . (2022) Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, and Björn Ommer. 2022. High-resolution image synthesis with latent diffusion models. In Proceedings of the IEEE/ -->

<!-- [原子块 · verbatim] Samo and Highhouse (2023) Andrew Samo and Scott Highhouse. 2023. Artificial intelligence and art: Identifying the aesthetic judgment factors that distinguish human-and machine-generated artwork. Psych -->

<!-- [原子块 · verbatim] Schelling et al . (2008) Friedrich Wilhelm Joseph Schelling, Douglas W Stott, and David Simpson. 2008. The philosophy of art . University of Minnesota Press. -->

<!-- [原子块 · verbatim] Schuhmann et al . (2022) Christoph Schuhmann, Romain Beaumont, Richard Vencu, Cade Gordon, Ross Wightman, Mehdi Cherti, Theo Coombes, Aarush Katta, Clayton Mullis, Mitchell Wortsman, et al . 2022. Lai -->

<!-- [原子块 · verbatim] Sibley (2017) Frank Sibley. 2017. Aesthetic concepts. In Aesthetics . Routledge, 501–505. -->

<!-- [原子块 · verbatim] Sircello (1968) Guy Sircello. 1968. Subjectivity and Justification in Aesthetic Judgments. The Journal of Aesthetics and Art Criticism 27, 1 (1968), 3–12. -->

<!-- [原子块 · verbatim] So (2023) Chaehan So. 2023. Measuring aesthetic preferences of neural style transfer: More precision with the two-alternative-forced-choice task. International Journal of Human–Computer Interaction 39 -->

<!-- [原子块 · verbatim] Song et al . (2020) Jiaming Song, Chenlin Meng, and Stefano Ermon. 2020. Denoising diffusion implicit models. arXiv preprint arXiv:2010.02502 (2020). -->

<!-- [原子块 · verbatim] Spearman (1987) Charles Spearman. 1987. The proof and measurement of association between two things. The American journal of psychology 100, 3/4 (1987), 441–471. -->

<!-- [原子块 · verbatim] Sprague et al . (2024) Zayne Sprague, Fangcong Yin, Juan Diego Rodriguez, Dongwei Jiang, Manya Wadhwa, Prasann Singhal, Xinyu Zhao, Xi Ye, Kyle Mahowald, and Greg Durrett. 2024. To cot or not to cot?  -->

<!-- [原子块 · verbatim] Sullivan and Artino Jr (2013) Gail M Sullivan and Anthony R Artino Jr. 2013. Analyzing and interpreting data from Likert-type scales. Journal of graduate medical education 5, 4 (2013), 541–542. -->

<!-- [原子块 · verbatim] Tatarkiewicz (1963) Wladyslaw Tatarkiewicz. 1963. Objectivity and Subjectivity in the History of Aesthetics. Philosophy and phenomenological research 24, 2 (1963), 157–173. -->

<!-- [原子块 · verbatim] Tatarkiewicz (2012) Władysław Tatarkiewicz. 2012. A history of six ideas: An essay in aesthetics . Vol. 5. Springer Science & Business Media. -->

<!-- [原子块 · verbatim] Team et al . (2023) Gemini Team, Rohan Anil, Sebastian Borgeaud, Jean-Baptiste Alayrac, Jiahui Yu, Radu Soricut, Johan Schalkwyk, Andrew M Dai, Anja Hauth, Katie Millican, et al . 2023. Gemini: a fami -->

<!-- [原子块 · verbatim] Van Leeuwen and Jewitt (2000) Theo Van Leeuwen and Carey Jewitt. 2000. The handbook of visual analysis . Sage. -->

<!-- [原子块 · verbatim] Wang et al . (2024) Haofan Wang, Matteo Spinelli, Qixun Wang, Xu Bai, Zekui Qin, and Anthony Chen. 2024. Instantstyle: Free lunch towards style-preserving in text-to-image generation. arXiv preprint a -->

<!-- [原子块 · verbatim] Wang et al . (2023) Jianyi Wang, Kelvin CK Chan, and Chen Change Loy. 2023. Exploring clip for assessing the look and feel of images. In Proceedings of the AAAI conference on artificial intelligence , -->

<!-- [原子块 · verbatim] Wang et al . (2022) Zijie J Wang, Evan Montoya, David Munechika, Haoyang Yang, Benjamin Hoover, and Duen Horng Chau. 2022. Diffusiondb: A large-scale prompt gallery dataset for text-to-image generativ -->

<!-- [原子块 · verbatim] Wei et al . (2022) Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al . 2022. Chain-of-thought prompting elicits reasoning in large language models.  -->

<!-- [原子块 · verbatim] Wikiart ([n. d.]) volunteer team Wikiart. [n. d.]. WikiArt dataset. https://www.wikiart.org . -->

<!-- [原子块 · verbatim] Wright and Ommer (2022) Matthias Wright and Björn Ommer. 2022. Artfid: Quantitative evaluation of neural style transfer. In DAGM German Conference on Pattern Recognition . Springer, 560–576. -->

<!-- [原子块 · verbatim] Wu et al . (2024) Xun Wu, Shaohan Huang, Guolong Wang, Jing Xiong, and Furu Wei. 2024. Multimodal large language models make text-to-image generative models align better. Advances in Neural Informatio -->

<!-- [原子块 · verbatim] Wu et al . (2023) Xiaoshi Wu, Keqiang Sun, Feng Zhu, Rui Zhao, and Hongsheng Li. 2023. Human preference score: Better aligning text-to-image models with human preference. In Proceedings of the IEEE/CV -->

<!-- [原子块 · verbatim] Xu (2024) Jianing Xu. 2024. Exploration of the Applications of Image-based AIGC in Art Education. Advances in Social Development and Education Research 1, 3 (2024), 60–65. -->

<!-- [原子块 · verbatim] Yang et al . (2024) Junfeng Yang, Jing Fu, Wei Zhang, Wenzhi Cao, Limei Liu, and Han Peng. 2024. Moe-agiqa: Mixture-of-experts boosted visual perception-driven and semantic-aware quality assessment fo -->

<!-- [原子块 · verbatim] Younger (1963) D Younger. 1963. Minimum feedback arc sets for a directed graph. IEEE Transactions on Circuit Theory 10, 2 (1963), 238–245. -->

<!-- [原子块 · verbatim] Zhang et al . (2023b) Lvmin Zhang, Anyi Rao, and Maneesh Agrawala. 2023b. Adding conditional control to text-to-image diffusion models. In Proceedings of the IEEE/CVF International Conference on Compu -->

<!-- [原子块 · verbatim] Zhang et al . (2023a) Xinlu Zhang, Yujie Lu, Weizhi Wang, An Yan, Jun Yan, Lianke Qin, Heng Wang, Xifeng Yan, William Yang Wang, and Linda Ruth Petzold. 2023a. Gpt-4v (ision) as a generalist evaluator -->

<!-- [原子块 · verbatim] Zhu et al . (2024) Hanwei Zhu, Haoning Wu, Yixuan Li, Zicheng Zhang, Baoliang Chen, Lingyu Zhu, Yuming Fang, Guangtao Zhai, Weisi Lin, and Shiqi Wang. 2024. Adaptive image quality assessment via teach -->

**EN** Appendix A Additional Experiment Details

**ZH** 附录 A 补充实验细节

**EN** A.1. Human Aesthetic Judgment Collection

**ZH** A.1. 人类审美判断采集

<!-- [原子块 · img]  -->

**EN** Figure 7. UI for 2AFC annotation. We present user with the source image (top), 2AFC (middle) and style prompt (bottom). The user is required to choose the preferred one by clicking on the “left" or “right" button.

**ZH** 图 7. 2AFC 标注界面。我们向用户呈现源图像（上）、2AFC（中）与风格提示（下）。用户需点击“left”或“right”按钮选择更偏好的一张。

<!-- [原子块 · img]  -->

**EN** Figure 8. UI for hallucination annotation. Users are presented with the original 2AFC task and the response of MLLM, when the answer are not aligned. User shall drag discrete-valued slider to determine the hallucination strength from four perspectives.

**ZH** 图 8. 幻觉标注界面。当 MLLM 的答案与人类不一致时，我们向用户呈现原始的 2AFC 任务与 MLLM 的响应。用户需拖动离散值滑块，从四个视角判定幻觉强度。

**EN** User Interface For the main judgment collection in Sec.3.2, we develop a web-based application to collect responses from human-expert annotators. We present users with the 2AFC question and reference content and style. The content is presented as a reference image, while we present the style as a prompt. The name of the stylization model is tracked but not visible to the user during annotation. The screenshot of the user interface (UI) can be found in Fig. 7.

**ZH** 用户界面。针对第 3.2 节中的主要判断采集，我们开发了一个基于网页的应用来收集人类专家标注者的回答。我们向用户呈现 2AFC 问题以及参考的内容与风格。内容以参考图像呈现，风格则以提示呈现。风格化模型的名称被记录，但在标注过程中对用户不可见。用户界面（UI）截图见图 7。

**EN** For the hallucination labeling, we also designed a UI, visualized in Fig. 8. We record the user’s response during the 2AFC annotation and present them with the misaligned comparisons. The user shall read the MLLM’s response (the prompting method and the model name is not visible) and determine the hallucination issue from the four aspects. The image on left will be enlarged on mouse hover.

**ZH** 针对幻觉标注，我们也设计了一个界面，见图 8。我们记录用户在 2AFC 标注中的回答，并向他们呈现不一致的比较。用户需阅读 MLLM 的响应（提示方法与模型名称不可见），并从四个方面判定幻觉问题。鼠标悬停时左侧图像会放大。

**EN** The annotation tools will be open-sourced to benefit future research.

**ZH** 标注工具将开源，以惠及后续研究。

**EN** Preference Collection The participants (n=18, 7 female, 11 male) all have at least a tertiary education background. All participants have basic knowledge about Western and oriental art history, 14 participants have at least basic experience in painting, while 7 participants have experience in generative art, either as creative media or research. All participants are at least 18 and consent to the potential naked human body present in the dataset. Participants are allowed to search when they encounter unfamiliar art styles. The average time spent (measured as the time the author stays on the annotation page) per 2AFC annotation comparison is 13.3 sec, and the hallucination annotation is 63.5 sec. The physical setup is visualized in Fig. 9

**ZH** 偏好采集。参与者（n=18，女性 7 人，男性 11 人）均至少受过高等教育。所有参与者都具备西方与东方艺术史的基础知识，14 人有至少基础的绘画经验，7 人有生成式艺术经验（作为创作媒介或研究对象）。所有参与者均年满 18 岁，并同意数据集中可能出现人体裸像。参与者在遇到不熟悉的艺术风格时可以检索。每次 2AFC 标注比较的平均耗时（以标注者停留在标注页面的时间计）为 13.3 秒，幻觉标注为 63.5 秒。物理布置如图 9 所示。

<!-- [原子块 · img]  -->

**EN** Figure 9. A illustrative diagram for the physical setup of human data collection.

**ZH** 图 9. 人类数据采集物理布置的示意图。

**EN** A.2. Sampling algorithm

**ZH** A.2. 采样算法

**EN** We formally describe the proposed degree-uniform sub-graph sampling algorithm in Algorithm below.

**ZH** 我们在下面的算法中形式化描述所提出的度数均匀子图采样算法。

**EN** Algorithm 1 Sample a Connected Subgraph with Uniform Degree Distribution

**ZH** 算法 1 采样具有均匀度数分布的连通子图

**EN** Input:

**ZH** 输入：

**EN** ⟦SLOT_57⟧ ;

**ZH** ⟦SLOT_57⟧；

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

<!-- [原子块 · table] B ​ e ​ s ​ t ​ E ​ d ​ g ​ e ​ s ← { e ∈ E ∖ E ′ | min ⁡ max ⁡ { d ⁡ ( u ) + 1 , d ⁡ ( v ) + 1 } } BestEdges\leftarrow\left\{e\in E\setminus E^{\prime}\ \bigg|\ \min\max\{d(u)+1,d(v)+1\}\right\} -->

<!-- [原子块 · table] B e s t E d g e s ← { e ∈ B e s t E d g e s | min ∑ { d ( u ) + 1 , d ( v ) + 1 } } BestEdges\leftarrow\left\{e\in BestEdges\ \bigg|\ \min\sum\{d(u)+1,d(v)+1\}\right\} -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

**EN** A.3. Detail on FineArtBench

**ZH** A.3. FineArtBench 的细节

**EN** We construct FineArtBench by harvesting from existing open-source datasets with the help of MLLMs.

**ZH** 我们借助 MLLM，从现有开源数据集中采集素材构建 FineArtBench。

**EN** For the Content category, 50% of the content images are generated using the Ideogram-v1 text-to-image (T2I) diffusion model with diverse prompts produced by GPT-4. The remaining 50% are randomly sampled from the SA-1B (Kirillov et al. 2023) and MS-COCO (Lin et al. 2014) datasets, with captions generated by Gemini-v1.5 pro (Team et al. 2023). Images from SA-1B are downsampled by a factor of two, while those from MS-COCO retain their original resolution. Overall, all images have an average height and width of 895.7 and 811.9 pixels, respectively. The 5th percentiles for height and width are 480 and 427 pixels, respectively, and the 95th percentiles for both dimensions are 1248 pixels.

**ZH** 在内容类别上，50% 的内容图像由 Ideogram-v1 文生图（T2I）扩散模型配合 GPT-4 生成的多样化提示产生。其余 50% 从 SA-1B（Kirillov 等，2023）与 MS-COCO（Lin 等，2014）数据集中随机采样，说明文字由 Gemini-v1.5 pro（Team 等，2023）生成。来自 SA-1B 的图像按因子二下采样，而来自 MS-COCO 的图像保留原始分辨率。总体上，所有图像的平均高度与宽度分别为 895.7 与 811.9 像素；高度与宽度的第 5 百分位分别为 480 与 427 像素，两个维度的第 95 百分位均为 1248 像素。

**EN** To synthesize fine-grained attribute annotations for the content images and their associated prompts, we first employ Gemini v1.5-pro to automate the annotation process based on a predefined attribute set. The Style subset of FineArtBench is derived from WikiArt (Wikiart [n. d.]) and DiffusionDB (Wang et al. 2022). The process involves two main steps:

**ZH** 为合成内容图像及其关联提示的细粒度属性标注，我们首先使用 Gemini v1.5-pro 基于预定义属性集自动执行标注。FineArtBench 的风格子集源自 WikiArt（Wikiart，[n. d.]）与 DiffusionDB（Wang 等，2022），包含两个主要步骤：

**EN** (1) WikiArt Processing: We extract keywords from WikiArt, focusing on specifications such as art movement, artist, and genre. These base keywords are then expanded and combined using GPT-4 (OpenAI 2023) to create a diverse set of style descriptors.

**ZH** （1）WikiArt 处理：我们从 WikiArt 中抽取关键词，聚焦艺术运动、艺术家与体裁等规格说明。这些基础关键词随后用 GPT-4（OpenAI，2023）扩展与组合，形成多样化的风格描述词集合。

**EN** (2) DiffusionDB Processing: Given the high noise level in DiffusionDB annotations, we utilize an MLLM to preprocess the text prompts within the dataset. Specifically, we extract the style descriptions from each prompt and merge those with similar style specifications. Subsequently, we subsample from these processed style prompts to ensure quality and diversity.

**ZH** （2）DiffusionDB 处理：鉴于 DiffusionDB 标注噪声较高，我们用 MLLM 对数据集中的文本提示做预处理。具体而言，我们抽取每条提示中的风格描述，并合并风格规格相近者。随后从这些处理后的风格提示中做子采样，以保证质量与多样性。

**EN** For both the WikiArt and DiffusionDB prompts, style reference images are generated using StableDiffusion-v2 (Rombach et al. 2022), with all images standardized to a resolution of 512⟦SLOT_58⟧512 pixels. Similar to content annotations, we employ MLLMs to annotate the attributes of style prompts.

**ZH** 对于 WikiArt 与 DiffusionDB 的提示，风格参考图像均使用 StableDiffusion-v2（Rombach 等，2022）生成，所有图像统一为 512⟦SLOT_58⟧512 像素的分辨率。与内容标注类似，我们使用 MLLM 标注风格提示的属性。

**EN** All annotations are manually validated by at least two human annotators to ensure quality. The actual number of sampled content and style images is summarized in Table 7. We will open-source FineArtBench to facilitate reproducibility and support future research endeavors.

**ZH** 所有标注均由至少两位人工标注者手工校验以保证质量。实际采样的内容图像与风格图像数量汇总于表 7。我们将开源 FineArtBench，以促进可复现性并支持后续研究。

**EN** Table 7. Content and Style Sources FineArtBench is built from diverse sources to eliminate bias.

**ZH** 表 7. 内容与风格来源。FineArtBench 由多种来源构建，以消除偏差。

<!-- [原子块 · table] Content Style Source Generated MS-COCO SA-1B WikiArt DiffusionDB Number 500 250 250 764 236 -->

**EN** A.4. Prompt Design

**ZH** A.4. 提示设计

**EN** We summarize the full prompt of base prompt, zero-shot CoT prompting and the proposed ArtCoT prompt in Tab. 8. We did not attempt to optimize the prompt design of ArtCoT as it just act as a strong baseline method to identify the key issue and inspire future works.

**ZH** 我们在表 8 中汇总了基础提示、零样本 CoT 提示与所提 ArtCoT 提示的完整提示。我们没有尝试优化 ArtCoT 的提示设计，因为它只是作为一个强有力的基线方法，用于识别关键问题并启发后续工作。

**EN** Table 8. Template for different prompting methods. [STYLE] stands for placeholder for the style prompt, and [IMAGE] stands for placeholder for image tokens.

**ZH** 表 8. 不同提示方法的模板。[STYLE] 表示风格提示的占位符，[IMAGE] 表示图像词元的占位符。

<!-- [原子块 · table] Base Prompt Zero-Shot CoT ArtCoT CS Analyzer Art Critic Summarizer ‘[IMAGE]‘ You are an expert in fine art. A source image (top) and two different stylized images (bottom) in the style of ‘[STYLE]‘ ar -->

**EN** Appendix B Example conversations

**ZH** 附录 B 示例对话

**EN** We present several quantitative comparisons of MLLM’s response generated using different prompt in the following pages. We highlight the subjective words and unsubstantiated interpretation of zero-shot CoT. Compared with zero-shot CoT, the responses from ArtCoT is much more detailed and contain less hallucination.

**ZH** 我们在随后的页面中给出若干 MLLM 使用不同提示所生成响应的定量比较。我们突出显示了零样本 CoT 中的主观词与缺乏依据的阐释。与零样本 CoT 相比，ArtCoT 的响应详尽得多，且幻觉更少。

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

**EN** Appendix C Samples of FineArtBench

**ZH** 附录 C FineArtBench 样例

**EN** Examples of content image and style prompt is in Fig. 10, Tab. 9, respectively

**ZH** 内容图像与风格提示的示例分别见图 10 与表 9。

<!-- [原子块 · img]  -->

**EN** Figure 10. Random sample of content images from FineArtBench

**ZH** 图 10. FineArtBench 内容图像的随机样例

**EN** Table 9. Examples of style prompt

**ZH** 表 9. 风格提示示例

<!-- [原子块 · table] Randomly Sampled Style Prompts Bauhaus geometric abstraction with primary colors and clean lines The Blue Boy by Thomas Gainsborough Alphonse Mucha, Vincent van Gogh, Egon Schiele-inspired artwork wit -->
