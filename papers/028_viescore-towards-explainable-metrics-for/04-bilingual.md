# VIEScore：面向条件图像合成评估的可解释指标

> 原标题：VIEScore: Towards Explainable Metrics for Conditional Image Synthesis Evaluation
> 作者：Max Ku, Dongfu Jiang, Cong Wei, Xiang Yue, Wenhu Chen · arXiv:2312.14867 · 2023-12-22

<!-- [原子块 · verbatim] VIEScore: Towards Explainable Metrics for Conditional Image Synthesis Evaluation -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] In the rapidly advancing field of conditional image generation research, challenges such as limited explainability lie in effectively evaluating the performance and capabilities of various models. Thi -->

**EN** https://tiger-ai-lab.github.io/VIEScore/

**ZH** https://tiger-ai-lab.github.io/VIEScore/

<!-- [原子块 · img]  -->

**EN** Figure 1: Which method (VIEScore or traditional metrics) is “closer” to the human perspectives? Metrics in the future would provide not just the score but also the rationale, enabling the understanding of each judgment.

**ZH** 图 1：哪种方法（VIEScore 还是传统指标）更“接近”人类的视角？未来的指标不仅要给出分数，还要给出理由，使每一次判断都可被理解。

**EN** 1 Introduction

**ZH** 1 引言

**EN** Diffusion models have become a focal point in AI research for image synthesis. Over the past year, several new models (Kumari et al., 2023; Ruiz et al., 2023; Li et al., 2023c; Zhang and Agrawala, 2023) have been introduced to enhance control over image generation. However, comprehensively evaluating AI-synthesized images remains a challenging and unresolved issue. While metrics like LPIPS (Zhang et al., 2018), CLIP-Score (Hessel et al., 2021), and DreamSim (Fu et al., 2023b) were proposed, they have certain limitations: (1) these metrics are agnostic the end task, which can fail to measure the desired aspects of the generated images, (2) the score is opaque with limited explainability. These limitations heavily restrict their effectiveness in assessing conditional image generation. Some research work (Denton et al., 2015; Isola et al., 2017; Meng et al., 2021; Chen et al., 2023; Sheynin et al., 2023) relied on human-driven evaluation methods. While humans excel at understanding and interpreting visual content, such methods in the context are facing challenges such as scalability limits and preference subjectivity issues. This reliance on human judgment highlights the need for more uniform evaluation methods in the field. To solve the mentioned issues, we formulate the problem definition with our desired properties, as presented in equation 1. The function ⟦SLOT_0⟧ takes an instruction ⟦SLOT_1⟧, a synthesized image ⟦SLOT_2⟧, and ⟦SLOT_3⟧ which is a set of conditions (e.g. style, subject, background, canny-edge, etc). The score function should produce the intermediate rationale in the form of natural language before generating the final score according to the prompt instruction ⟦SLOT_4⟧:

**ZH** 扩散模型已成为图像合成领域人工智能研究的焦点。过去一年中出现了一批新模型（Kumari 等，2023；Ruiz 等，2023；Li 等，2023c；Zhang 和 Agrawala，2023），用于增强对图像生成的控制。然而，全面评估人工智能合成图像仍是一个悬而未决的难题。尽管已有 LPIPS（Zhang 等，2018）、CLIP-Score（Hessel 等，2021）与 DreamSim（Fu 等，2023b）等指标，但它们存在明显局限：（1）这些指标与最终任务无关，可能无法度量生成图像真正需要考察的方面；（2）分数不透明，可解释性有限。这些局限严重制约了它们在条件图像生成评估中的作用。部分工作（Denton 等，2015；Isola 等，2017；Meng 等，2021；Chen 等，2023；Sheynin 等，2023）依赖人工驱动的评估方法。人类虽擅长理解与解读视觉内容，但这类方法在本场景下面临可扩展性受限、偏好主观性强等挑战。对人类判断的依赖凸显出本领域对更统一评估方法的迫切需求。为解决上述问题，我们用所期望的性质对问题做出形式化定义，如式 1 所示。函数 ⟦SLOT_0⟧ 接受一条指令 ⟦SLOT_1⟧、一张合成图像 ⟦SLOT_2⟧，以及 ⟦SLOT_3⟧——一组条件（如风格、主体、背景、canny 边缘等）。该评分函数应先以自然语言形式给出中间评判理由，再根据提示词指令 ⟦SLOT_4⟧ 生成最终分数：

<!-- [原子块 · table] f VIE ​ ( I , O , C ∗ ) = ( rationale , score ) f_{\text{VIE}}(I,O,C^{*})=(\text{rationale},\text{score}) (1) -->

**EN** The function ⟦SLOT_5⟧ can be any Multimodal Large Language Model (MLLM) such as GPT-4 OpenAI (2023) and LLaVA (Liu et al., 2023a), which can take input images to generate human-like text responses. Unlike the automatic metrics, MLLM can receive human instructions and produce rationale. With such motivation, we introduce VIEScore (Visual Instruction-guided Explainable Score), a framework to assess synthetic images in different conditional image generation tasks. VIEScore has multiple advantages compared to auto-metrics and human evaluation. It includes:

**ZH** 函数 ⟦SLOT_5⟧ 可以是任意多模态大语言模型（MLLM），例如 GPT-4（OpenAI，2023）与 LLaVA（Liu 等，2023a），它们能接收输入图像并生成类人的文本回复。与自动指标不同，MLLM 能接收人类指令并给出评判理由。受此启发，我们提出 VIEScore（Visual Instruction-guided Explainable Score，视觉指令引导的可解释评分），一个用于评估不同条件图像生成任务中合成图像的框架。相比自动指标与人工评估，VIEScore 具备以下优势：

**EN** Task Awareness. Existing metrics were often designed to measure a certain aspect of generated images. For example, LPIPS measures the perceptual similarity of a pair of images, while CLIP-Score measures the text alignment of one single image. As a consequence, these metrics cannot be adapted to evaluate other tasks. VIEScore acts as a silver bullet to tackle all conditional image generation evaluation processes due to its instruction-guiding property. It can be carefully adjusted with different instruction requirements.

**ZH** 任务感知。现有指标通常只针对生成图像的某一方面设计。例如 LPIPS 度量一对图像的感知相似度，CLIP-Score 度量单张图像与文本的对齐程度。因此这些指标无法迁移到其他任务的评估中。VIEScore 凭借其指令引导特性，可作为应对所有条件图像生成评估流程的通用方案，并能依据不同的指令需求做细致调整。

**EN** Explainability. The existing metrics normally output a single float-point score, which cannot offer detailed insights into the ’rationale’ behind its evaluations. Such a score makes it difficult to interpret the decisions from the metric output. Instead, VIEScore can offer the rationale in the form of natural languages to help humans understand the reasoning process. As depicted in Figure 1, the rationale can significantly improve the trustworthiness of VIEScore.

**ZH** 可解释性。现有指标通常只输出一个浮点分数，无法揭示评估背后的“理由”，因而难以解读指标输出的决策依据。VIEScore 则能以自然语言给出评判理由，帮助人们理解推理过程。如图 1 所示，理由能显著提升 VIEScore 的可信度。

**EN** While the ultimate goal is to derive an MLLM that can rate images like humans, in this paper we also explore how well MLLMs can assess synthetic images compared to human evaluation and present insights and challenges on state-of-the-art MLLMs towards human evaluators, as shown in Figure 2.

**ZH** 最终目标是得到一个能像人类一样为图像打分的 MLLM；本文同时也考察现有 MLLM 在评估合成图像时与人类评估的接近程度，并给出当前最先进 MLLM 迈向人类评估者过程中的洞察与挑战，如图 2 所示。

**EN** 2 Related Works

**ZH** 2 相关工作

**EN** 2.1 Conditional Image Synthesis

**ZH** 2.1 条件图像合成

**EN** With recent advancements in Image Synthesis research (Goodfellow et al., 2016; Ho et al., 2020; Dhariwal and Nichol, 2021), researchers proposed different methods and contributed a large amount of controllable image synthesis models with conditional inputs. Conditional image synthesis can be categorized into conditional image generation and conditional image editing tasks. Prevalent tasks include Text-To-Image generation Saharia et al. (2022); Rombach et al. (2022); stability.ai (2023) (known as text-guided image generation), Inpainting (Avrahami et al., 2022; Lugmayr et al., 2022) (known as mask-guided image editing) and Text-guided image editing (Brooks et al., 2023; Couairon et al., 2022; Wu and la Torre, 2023).

**ZH** 随着图像合成研究的近期进展（Goodfellow 等，2016；Ho 等，2020；Dhariwal 和 Nichol，2021），研究者提出了不同方法，贡献了大量带条件输入的可控图像合成模型。条件图像合成可分为条件图像生成与条件图像编辑两类任务。主流任务包括文本到图像生成（Saharia 等，2022；Rombach 等，2022；stability.ai，2023）（又称文本引导的图像生成）、图像修复（Avrahami 等，2022；Lugmayr 等，2022）（又称掩膜引导的图像编辑）与文本引导的图像编辑（Brooks 等，2023；Couairon 等，2022；Wu 和 la Torre，2023）。

**EN** More recent works proposed new tasks such as Subject-driven image generation and editing (Gal et al., 2022; Ruiz et al., 2023; Li et al., 2023c) to inject one specific subject into a synthesized image, while Multi-concept image composition (Kumari et al., 2023; Liu et al., 2023b) allows multiple specific subjects into the synthesized image. Control-guided image generation (Zhang and Agrawala, 2023; Qin et al., 2023) allows additional conditions alongside the text prompt to guide the image synthesis. Our work uses MLLM to access all the discussed tasks on synthetic image evaluation.

**ZH** 更近期的工作提出了主体驱动的图像生成与编辑（Gal 等，2022；Ruiz 等，2023；Li 等，2023c）等新任务，用于把某个特定主体注入合成图像；多概念图像组合（Kumari 等，2023；Liu 等，2023b）则允许合成图像中同时出现多个特定主体；控制引导的图像生成（Zhang 和 Agrawala，2023；Qin 等，2023）允许在文本提示之外附加条件来引导图像合成。本文用 MLLM 对上述所有任务的合成图像评估进行考察。

**EN** 2.2 Synthetic Images Evaluation

**ZH** 2.2 合成图像评估

**EN** Various metrics are proposed to evaluate the quality of AI-generated images. Traditional measures like the Inception Score (IS) (Salimans et al., 2016) and the Frechet Inception Distance (FID) (Heusel et al., 2017) are commonly employed to measure image fidelity. On the other hand, to measure the alignment between the generated image and the text prompt, several metrics (Kim et al., 2022; Kynkäänniemi et al., 2019; Park et al., 2021; Sajjadi et al., 2018) have been introduced. The CLIP score (Hessel et al., 2021) and BLIP score (Li et al., 2022) are the most commonly used. Recently, approaches such as (Cho et al., 2023) and (Lu et al., 2023c) aim to provide a fine-grained evaluation framework, while the HEIM-benchmark (Lee et al., 2023) assesses text-to-image models across multiple aspects, such as toxicity and safety. Other methods, such as projective-geometry (Sarkar et al., 2023), evaluate images’ physical and geometric realism. However, these metrics are primarily focused on text-to-image generation and remain narrow in scope. General image generation tasks like subject-driven image generation and image editing (Ruiz et al., 2023; Li et al., 2023c) still lack effective automatic metrics. One traditional, yet effective method to evaluate AI-generated image performance is to have human annotators assess visual quality. Recent works like ImagenHub (Ku et al., 2023), and HEIM Lee et al. (2023) attempt to standardize human evaluation across various image generation tasks, though scalability remains a challenge. Our research aims to identify the challenges in mimicking human perception in synthetic image evaluation and address these gaps by developing auto-metrics that align with human judgment across common image evaluation tasks.

**ZH** 已有多种指标用于评估人工智能生成图像的质量。传统度量如 Inception Score（IS）（Salimans 等，2016）与 Frechet Inception Distance（FID）（Heusel 等，2017）常用于度量图像保真度。另一方面，为度量生成图像与文本提示的对齐程度，也出现了若干指标（Kim 等，2022；Kynkäänniemi 等，2019；Park 等，2021；Sajjadi 等，2018），其中 CLIP score（Hessel 等，2021）与 BLIP score（Li 等，2022）最为常用。近期，（Cho 等，2023）与（Lu 等，2023c）等方法试图提供细粒度的评估框架，HEIM 基准（Lee 等，2023）则从毒性、安全性等多个方面评估文本到图像模型。另一些方法，如射影几何方法（Sarkar 等，2023），评估图像的物理与几何真实感。然而这些指标主要聚焦文本到图像生成，覆盖范围偏窄。主体驱动的图像生成、图像编辑（Ruiz 等，2023；Li 等，2023c）等通用图像生成任务仍缺乏有效的自动指标。另一种传统却有效的评估方式是让人类标注者评判视觉质量。ImagenHub（Ku 等，2023）与 HEIM（Lee 等，2023）等近期工作尝试在多种图像生成任务上规范人工评估，但可扩展性仍是难题。本文旨在识别合成图像评估中模仿人类感知所面临的挑战，并通过开发与人类判断相契合的自动指标来弥补这些空白。

**EN** 2.3 Large Language Models as Evaluators

**ZH** 2.3 大语言模型作为评估者

**EN** Large language models (LLMs) are often used to evaluate the quality of model-generated outputs. Recent works used LLMs as an evaluator demonstrating their great ability in text generation evaluation (Zheng et al., 2023; Dubois et al., 2023). This ability for evaluation naturally emerges (Fu et al., 2023a) and stems from LLM’s great reasoning ability and instruction-following ability. Recent works also tried to devise a smaller but explicitly fine-tuned LLM(Touvron et al., 2023) that achieves similar evaluation results on natural language generation (Xu et al., 2023; Jiang et al., 2023; Li et al., 2023b). Besides text evaluation, LLMs with visual features have been used as evaluators on images (Lu et al., 2023d; Huang et al., 2023; Lee et al., 2020; Inan et al., 2021; Hu et al., 2023), mainly focused on evaluating text-to-image task. GPT-4v, regarded as the state-of-the-art LLM with visual features, also reported a decent ability on image evaluation, especially in text-image alignment (Zhang et al., 2023b). However, the GPT-4v is not perfect for image evaluation. A comprehensive study on GPT-4v’s vision ability reported that GPT-4v makes mistakes on image evaluation tasks (Yang et al., 2023). For example, it failed to provide proper reasonings for spotting the difference between two similar images.

**ZH** 大语言模型（LLM）常被用于评估模型生成输出的质量。近期工作把 LLM 用作评估者，证明其在文本生成评估中的出色能力（Zheng 等，2023；Dubois 等，2023）。这种评估能力是自然涌现的（Fu 等，2023a），源于 LLM 强大的推理能力与指令遵循能力。也有工作尝试设计更小但经过显式微调的 LLM（Touvron 等，2023），以在自然语言生成评估上取得相近结果（Xu 等，2023；Jiang 等，2023；Li 等，2023b）。除文本评估外，具备视觉能力的 LLM 也被用作图像评估者（Lu 等，2023d；Huang 等，2023；Lee 等，2020；Inan 等，2021；Hu 等，2023），主要聚焦文本到图像任务。被视为最先进视觉 LLM 的 GPT-4v 在图像评估上也表现出不错的能力，尤其在图文对齐方面（Zhang 等，2023b）。然而 GPT-4v 在图像评估上并不完美。一项关于 GPT-4v 视觉能力的综合研究指出，GPT-4v 会在图像评估任务中出错（Yang 等，2023），例如未能为发现两张相似图像之间的差异给出恰当理由。

**EN** 3 Preliminary

**ZH** 3 预备知识

**EN** 3.1 Evaluation Benchmark

**ZH** 3.1 评估基准

**EN** ImagenHub (Ku et al., 2023) is a standardized benchmark for evaluating conditional image generation models with human raters. The framework covered mainstream tasks, including image generation, editing, and several conditioned tasks. In this section, we visit how humans assess images in the ImagenHub framework. Images are rated in two aspects: (1) Semantic Consistency (SC) assesses how well the generated image aligns with the given conditions, such as prompts and subject tokens, ensuring coherence and relevance to the specified criteria according to the task. (2) Perceptual Quality (PQ) evaluates the extent to which the generated image appears visually authentic and conveys a sense of naturalness.

**ZH** ImagenHub（Ku 等，2023）是用人类评分者评估条件图像生成模型的标准化基准，覆盖了图像生成、编辑以及若干带条件的主流任务。本节考察 ImagenHub 框架中人类如何评估图像。图像从两个方面打分：（1）语义一致性（SC）衡量生成图像与给定条件（如提示词、主体词元）的契合程度，确保结果相对于任务规定的标准连贯且相关；（2）感知质量（PQ）衡量生成图像看起来视觉真实、传达自然感的程度。

**EN** ImagenHub curated a human evaluation dataset for each task, in which the dataset contains around 100 to 200 conditional inputs for generating synthesized images. Then each image was rated by three human raters according to the guidelines of the defined task, and a final score in the range [0.0, 1.0] was reported for the average score in semantic consistency (SC) and perceptual quality (PQ) respectively, with another overall score (O) derived from the geometric mean of semantic consistency and perceptual quality at the instance level. ImagenHub covered 30 image synthesis models and reported 0.4 Krippendorff’s alpha on the inter-worker agreement of their human rating.

**ZH** ImagenHub 为每个任务整理了一份人工评估数据集，每份数据集包含约 100 至 200 条用于生成合成图像的条件输入。随后每张图像由三名人类评分者依据任务定义的指南打分，并在 [0.0, 1.0] 区间内给出语义一致性（SC）与感知质量（PQ）各自的平均分；总体分数（O）由实例级上语义一致性与感知质量的几何平均得到。ImagenHub 覆盖了 30 个图像合成模型，其人工评分的评分者间一致性 Krippendorff's alpha 为 0.4。

**EN** 3.2 Multimodal Large Language Models

**ZH** 3.2 多模态大语言模型

**EN** Multimodal Large Language Models (MLLMs) typically denote LLMs with integrated visual capabilities (Yin et al., 2023). This visual proficiency opens up the potential to perform image analysis and evaluation. However, for a comprehensive assessment of synthetic images, multiple images may be examined in one pass due to complex conditions. The prompt will also be extensive to comprehensively describe the rating process. Therefore, the MLLM candidate should possess specific capabilities: (1) The model must efficiently process and interpret multiple images simultaneously. (2) The model needs to comprehend and respond to lengthy text prompts while matching all requirements.

**ZH** 多模态大语言模型（MLLM）通常指集成了视觉能力的 LLM（Yin 等，2023）。这种视觉能力为图像分析与评估提供了可能。然而，要对合成图像做全面评估，由于条件复杂，一次输入中可能需要考察多张图像，提示词也会变长，以完整描述评分流程。因此，MLLM 候选者需要具备以下能力：（1）能高效同时处理并理解多张图像；（2）能理解并响应长文本提示，同时满足其中的全部要求。

**EN** Recent popular open-source MLLMs, including LLaVA (Liu et al., 2023a), InstructBLIP (Dai et al., 2023), Fuyu (Bavishi et al., 2023), and CogVLM (Wang et al., 2023), can only accept a single image as input along with text instruction. To feed multiple images, a workaround is to merge and concatenate multiple images horizontally and feed as one image. More recent MLLMs such as Open-Flamingo (Awadalla et al., 2023), Kosmos-2 (Peng et al., 2023), and QwenVL (Bai et al., 2023) can accept multiple images in an interleaved image-text format. For closed-source MLLMs, OpenAI’s GPT-4v (OpenAI, 2023), GPT-4o (OpenAI, 2023) and Google’s Gemini (Team et al., 2024) are the most popular MLLMs that perform exceptionally.

**ZH** 近期流行的开源 MLLM，包括 LLaVA（Liu 等，2023a）、InstructBLIP（Dai 等，2023）、Fuyu（Bavishi 等，2023）与 CogVLM（Wang 等，2023），只能接受单张图像与文本指令作为输入。要输入多张图像，一种变通做法是把多张图像水平拼接为一张后输入。更近期的 MLLM，如 Open-Flamingo（Awadalla 等，2023）、Kosmos-2（Peng 等，2023）与 QwenVL（Bai 等，2023），则可以接受图文交错格式的多张图像。闭源 MLLM 中，OpenAI 的 GPT-4v（OpenAI，2023）、GPT-4o（OpenAI，2023）以及 Google 的 Gemini（Team 等，2024）是最受欢迎且表现优异的模型。

**EN** 3.3 Existing Auto-metrics

**ZH** 3.3 现有自动指标

**EN** Here we list some prominent automatic metrics:

**ZH** 下面列出若干主流自动指标：

**EN** Image-Text Alignment. CLIP-Score (Hessel et al., 2021) computes the average cosine similarities between prompt and generated image CLIP embeddings. One disadvantage of CLIP-Score is that the score is biased towards the training distribution (Kim et al., 2023). Moreover, in practical evaluation, the average CLIP-Score result of a decent method will always fall in the range [0.25, 0.35] even though a single CLIP-Score is within [0, 1]. Such a narrow range may not offer enough differentiation to know which model is better. Moreover, image-text alignment is not the only considered aspect of semantic consistency. For example, it cannot examine the degree of overediting in text or mask-guided image editing tasks.

**ZH** 图文对齐度。CLIP-Score（Hessel 等，2021）计算提示词与生成图像 CLIP 嵌入之间的平均余弦相似度。CLIP-Score 的一个缺点是分数偏向训练分布（Kim 等，2023）；而且在实际评估中，尽管单个 CLIP-Score 落在 [0, 1] 区间，一个尚可的方法的平均 CLIP-Score 却总落在 [0.25, 0.35] 区间，如此窄的范围可能不足以区分模型优劣。此外，图文对齐并不是语义一致性唯一需要考虑的方面，例如它无法考察文本或掩膜引导图像编辑任务中的过度编辑程度。

**EN** Perceptual Distance. LPIPS (Zhang et al., 2018) measures the resemblance between two images in a manner that aligns with human perception. With its sensitivity to distortions, it is an often used metric in image synthesis research such as image editing tasks and control-guided Image Generation task (Meng et al., 2021; Qin et al., 2023), to measure between the input (or ground truth) and the generated image. However, in the image editing context, the image’s naturalness (e.g. shadow, lighting, sense of distance) is often required in the human perspective of perceptual quality, which is missed in the LPIPS metric. It is also difficult to access a model’s performance by distortion level, as in the current state of research the models often can process high-quality editing without artifacts.

**ZH** 感知距离。LPIPS（Zhang 等，2018）以契合人类感知的方式度量两张图像的相似程度。由于对畸变敏感，它常被用于图像编辑、控制引导图像生成等图像合成研究（Meng 等，2021；Qin 等，2023），度量输入（或真值）与生成图像之间的差异。然而在图像编辑场景中，人类对感知质量的判断往往还要求图像具备自然感（如阴影、光照、距离感），而 LPIPS 并未覆盖这一点。此外，用畸变程度衡量模型表现也很困难，因为就当前研究水平而言，模型通常已能在不产生伪影的情况下完成高质量编辑。

**EN** Subject Fidelity. CLIP-I computes the average pairwise cosine similarities between CLIP embeddings of generated and real images, first proposed in Textual-Inversion (Gal et al., 2022). However, CLIP-I cannot distinguish between different subjects that may have highly similar text descriptions, and it is less sensitive to shape consistency as it compares the semantic similarity between images. DINO metric was proposed in DreamBooth Ruiz et al. (2023). The metric is computed by the mean cosine similarities calculated pairwise between the DINO embeddings of ViT-S/16 (Caron et al., 2021) for both synthesized and authentic images. In contrast to CLIP-I, the DINO metric is sensitive to differences between subjects of the same class due to the self-supervised training objective of DINO. These two became popular metrics reported in research on subject-driven image generation and editing tasks (Li et al., 2023c; Lu et al., 2023a).

**ZH** 主体保真度。CLIP-I 计算生成图像与真实图像 CLIP 嵌入之间的平均成对余弦相似度，最早在 Textual-Inversion（Gal 等，2022）中提出。但 CLIP-I 无法区分文本描述高度相似的不同主体，且由于它比较的是图像间的语义相似度，对形状一致性不够敏感。DINO 指标在 DreamBooth（Ruiz 等，2023）中提出，通过对合成图像与真实图像的 ViT-S/16（Caron 等，2021）DINO 嵌入两两计算余弦相似度再取平均得到。与 CLIP-I 不同，得益于 DINO 的自监督训练目标，该指标对同类主体之间的差异较为敏感。这两者已成为主体驱动图像生成与编辑任务（Li 等，2023c；Lu 等，2023a）研究中的常用指标。

**EN** 4 Method

**ZH** 4 方法

<!-- [原子块 · img]  -->

**EN** Figure 2: We study the correlation between MLLMs and human perspectives on rating images.

**ZH** 图 2：我们研究 MLLM 与人类在为图像打分时视角上的相关性。

<!-- [原子块 · img]  -->

**EN** Figure 3: Process of MLLM evaluation on one synthetic image. All input conditions, synthesized images, and rating instructions are fed together to the MLLM in one pass. Multi-concept image composition task is used here as an example. The final overall score of the image is derived with equation 2.

**ZH** 图 3：MLLM 评估单张合成图像的流程。所有输入条件、合成图像与评分指令一次性送入 MLLM。此处以多概念图像组合任务为例。图像的最终总体分数由式 2 得出。

**EN** During the experiment, we select 29 models evaluated in ImagenHub (Ku et al., 2023) to compare the correlations with human ratings. See Appendix B for the listed models.

**ZH** 实验中，我们选取 ImagenHub（Ku 等，2023）中评估过的 29 个模型，比较各模型与人类评分的相关性。模型列表见附录 B。

**EN** Rating instructions. In ImagenHub, each image in one rating aspect is rated by picking an option from List[0, 0.5, 1] by three human raters. While such simple rating instruction is human-friendly and offers enough granularity, the simplicity of the scale can lead to less accurate representations of opinions, as given the broad spectrum covered by the rating aspects of semantic consistency (SC) and perceptual quality (PQ). We propose a more rigorous rating instruction toward comprehensive evaluation for each type of task. We split the rating of semantic consistency (SC) and perceptual quality (PQ) into multiple sub-scores, which SC contains multiple scores according to the tasks.

**ZH** 评分指令。在 ImagenHub 中，每个评分方面由三名人类评分者从列表 [0, 0.5, 1] 中选择一项来打分。这种简单的评分指令对人类友好且粒度足够，但刻度过于简单，可能导致意见表达不够精确——毕竟语义一致性（SC）与感知质量（PQ）这两个评分方面所涵盖的范围相当宽泛。为此，我们针对每类任务提出更严谨的评分指令：把语义一致性与感知质量的评分拆分为多个子分数，其中 SC 依据任务不同包含若干子分数。

**EN** For example, in the multi-concept image composition task as shown in Figure 3, two images (known as concepts) and a text prompt are provided as input, and the desired synthesized image will contain the two concept objects in the image in actions according to the text prompt. Thus SC will be split into 3 sub-scores: (1) Is the image aligning with the prompt? (2) Does the object in the image resemble the first concept? (3) Does the object in the image resemble the second concept? For PQ, the naturalness level and distortion level will be accessed separately, resulting in 2 sub-scores: (i) Does the image give an unnatural feeling such as a wrong sense of distance, wrong shadow, or wrong lighting? (ii) Does the image contain a portion of distortion, watermark, scratches, etc.? Our proposed rating system enhances the evaluation of tasks by dividing SC and PQ into distinct sub-scores. The details of prompt templates are available in Appendix A.

**ZH** 以图 3 所示的多概念图像组合任务为例，输入为两张图像（即概念）与一条文本提示，期望的合成图像应当包含这两个概念物体，并让它们按文本提示做出相应动作。于是 SC 被拆为 3 个子分数：（1）图像是否与提示词相符？（2）图像中的物体是否像第一个概念？（3）图像中的物体是否像第二个概念？PQ 则分别考察自然感与畸变程度，得到 2 个子分数：（i）图像是否给人不自然之感，如距离感错误、阴影错误或光照错误？（ii）图像是否存在局部畸变、水印、划痕等？本文的评分体系通过把 SC 与 PQ 拆分为不同子分数，强化了对任务的评估。提示模板的细节见附录 A。

<!-- [原子块 · table] O = [ min ⁡ ( α 1 , … , α i ) ​ min ⁡ ( β 1 , … , β i ) ] 1 2 O=[\min(\alpha_{1},...,\alpha_{i})\min(\beta_{1},...,\beta_{i})]^{\frac{1}{2}} (2) -->

**EN** Our overall score is derived as shown in equation 2. We assume each sub-score weights the same and used ⟦SLOT_6⟧ operation to emphasize the importance of meeting all criteria without exception. ⟦SLOT_7⟧ is a sub-score in SC and ⟦SLOT_8⟧ is a sub-score in PQ. The final rating scores of SC and PQ provided by MLLMs are on a scale of 0 to 10. The design rationale is that in ImagenHub’s human rating method, the possible results when the answers of three human raters, each picking an option from List[0, 0.5, 1], are added together and then divided by 3, will fall into one of the options: List[0.0, 0.17, 0.33, 0.5, 0.67, 0.83, 1.0]. Thus we simply use a scale of 0 to 10 and normalized in the range [0.0, 1.0] when comparing with human ratings. Input conditions and synthetic image are fed into the MLLM together during the rating process of SC, while in the PQ rating process, only the synthetic image is fed into the MLLM. This is to avoid the model getting confused by the input conditions in the PQ rating process, as to be discussed in section 5.1.

**ZH** 总体分数按式 2 得出。我们假定各子分数权重相同，并用 ⟦SLOT_6⟧ 运算来强调必须无例外地满足所有准则。⟦SLOT_7⟧ 为 SC 中的一个子分数，⟦SLOT_8⟧ 为 PQ 中的一个子分数。MLLM 给出的 SC 与 PQ 最终评分采用 0 到 10 的量表。这样设计的理由是：在 ImagenHub 的人工评分方法中，三名评分者各从 [0, 0.5, 1] 中选一项，其答案相加再除以 3，可能的结果落在 List[0.0, 0.17, 0.33, 0.5, 0.67, 0.83, 1.0] 之一；因此我们直接采用 0 到 10 的量表，并在与人类评分比较时归一化到 [0.0, 1.0] 区间。在 SC 评分过程中，输入条件与合成图像一并送入 MLLM；而在 PQ 评分过程中，只把合成图像送入 MLLM。这样做是为了避免模型在 PQ 评分中被输入条件干扰，5.1 节将对此展开讨论。

**EN** 5 Experimental Results

**ZH** 5 实验结果

<!-- [原子块 · table] Backbone M-H corr S ​ C {}^{SC}_{\text{corr}} M-H corr P ​ Q {}^{PQ}_{\text{corr}} M-H corr O {}^{O}_{\text{corr}} Across All 7 Tasks Human Raters 0.4700 0.4124 0.4558 VIEScore GPT-4o 0shot {}_{\text{ -->

**EN** Table 1: Correlations across all tasks with different backbone models. We highlight the highest correlation numbers in green. See Appendix C for details.

**ZH** 表 1：不同骨干模型在各任务上的相关性。最高的相关性数值以绿色标出。细节见附录 C。

<!-- [原子块 · table] Method M-H corr S ​ C {}^{SC}_{\text{corr}} M-H corr P ​ Q {}^{PQ}_{\text{corr}} M-H corr O {}^{O}_{\text{corr}} Text-guided Image Generation (5 models) Human Raters 0.5044 0.3640 0.4652 CLIP-Score -0 -->

**EN** Table 2: Correlations comparison of available methods on the most common tasks. We highlight the best method and the correlation numbers closest to human raters. Continue in Table 3 and 4.

**ZH** 表 2：在最常见的任务上，各可用方法的相关性比较。我们标出最佳方法以及与人类评分者最接近的相关性数值。续见表 3 与表 4。

<!-- [原子块 · table] Method M-H corr S ​ C {}^{SC}_{\text{corr}} M-H corr P ​ Q {}^{PQ}_{\text{corr}} M-H corr O {}^{O}_{\text{corr}} Subject-driven Image Generation (4 models) Human Raters 0.4780 0.3565 0.4653 DINO 0.416 -->

**EN** Table 3: Correlations comparison of available methods on the subject-driven tasks.

**ZH** 表 3：主体驱动任务上各可用方法的相关性比较。

<!-- [原子块 · table] Method M-H corr S ​ C {}^{SC}_{\text{corr}} M-H corr P ​ Q {}^{PQ}_{\text{corr}} M-H corr O {}^{O}_{\text{corr}} Multi-concept Image Composition (3 models) Human Raters 0.5927 0.5145 0.5919 DINO 0.097 -->

**EN** Table 4: Correlations comparison of available methods on the control-guided and multi-concept tasks.

**ZH** 表 4：控制引导与多概念任务上各可用方法的相关性比较。

**EN** 5.1 Correlation Study

**ZH** 5.1 相关性研究

**EN** For all presented correlations, we applied Fisher Z-transformation to estimate the average Spearman correlation ⟦SLOT_9⟧ across models and tasks.

**ZH** 对于报告的所有相关性，我们采用 Fisher Z 变换来估计跨模型、跨任务的平均斯皮尔曼相关系数 ⟦SLOT_9⟧。

**EN** Metric-to-Human (M-H) correlations. In Table 2 and 3, we first verified the reliability of ImagenHub human ratings by computing the Human-to-Human (H-H) correlation, as the correlation goes around 0.5, expected to be the highest value compared to MLLMs. Then we benchmark the MLLMs according to our designed method to compute the Metric-to-Human (M-H) correlation. We noticed only GPT-4v, GPT4o, Gemini, and LLaVA were able to follow our instructions clearly while other MLLMs were not able to produce any meaningful results according to our setup. For example, BLIP-2, while able to output the correct format, the scores provided are constant zeros. Qwen-VL and InstructBLIP could only produce a portion of responses for semantic consistency but failed to generate any results for perceptual quality evaluation. From overall performance, we found that GPT-4o reports a significantly higher correlation than all other MLLMs, while LLaVA’s correlation is much less than human raters. It seems that LLaVA is less effective in these specific tasks compared to close-sourced MLLMs like GPT-4v. It is worth mentioning that GPT-4o achieves a very high correlation with human raters on different image generation and editing tasks. GPT-4v and Gemini also show satisfactory performance on nearly all tasks with a difference of less than 0.2 towards human correlations, even on par with humans in text-guide image generation tasks. Both GPT-4v, Gemini, and LLaVA demonstrated the weakest performance in the text-guided editing task and subject-driven image editing task.

**ZH** 指标—人类（M-H）相关性。在表 2 与表 3 中，我们首先通过计算人类—人类（H-H）相关性来验证 ImagenHub 人工评分的可靠性：该相关性在 0.5 左右，预期是所有结果中的最高值。随后我们按所设计的方法计算各 MLLM 的指标—人类（M-H）相关性并做基准比较。我们发现，只有 GPT-4v、GPT-4o、Gemini 与 LLaVA 能清楚地遵循我们的指令，其他 MLLM 在我们的设定下无法产出任何有意义的结果。例如 BLIP-2 虽能输出正确格式，但给出的分数恒为零；Qwen-VL 与 InstructBLIP 只能对语义一致性给出部分回复，在感知质量评估上则完全无法生成结果。从整体表现看，GPT-4o 的相关性显著高于其他所有 MLLM，而 LLaVA 的相关性远低于人类评分者。看来在这些特定任务上，LLaVA 不如 GPT-4v 等闭源 MLLM 有效。值得一提的是，GPT-4o 在各类图像生成与编辑任务上都与人类评分者取得了很高的相关性。GPT-4v 与 Gemini 在几乎所有任务上也表现令人满意，与人类相关性的差距小于 0.2，在文本引导的图像生成任务上甚至与人类持平。GPT-4v、Gemini 与 LLaVA 三者表现最弱的都是文本引导的编辑任务与主体驱动的图像编辑任务。

**EN** Extra visuals resulted in a decline in performance. Numerous studies (Brown et al., 2020; Parnami and Lee, 2022; Liu et al., 2021) have highlighted that In-Context Learning (ICL) allows LLMs to tackle novel tasks effectively without requiring the traditional fine-tuning process. We applied In-Context Learning in our prompting method with the expectation of increasing the correlation scores, but we observed the opposite. In Table 2 and 3, there is an observable general trend of diminishing correlation scores. The overall correlation score in subject-driven image generation and editing, and the multi-concept image composition task dropped significantly. Only the mask-guided image editing task and control-guided image generation task reported a subtle increase in correlation score.

**ZH** 额外的视觉输入导致性能下降。大量研究（Brown 等，2020；Parnami 和 Lee，2022；Liu 等，2021）指出，上下文学习（ICL）能让 LLM 在不经过传统微调的情况下有效应对新任务。我们在提示方法中应用了上下文学习，原本期望相关性分数提高，结果却相反。在表 2 与表 3 中可以看到相关性分数普遍下降的趋势：主体驱动的图像生成与编辑、多概念图像组合任务的总体相关性分数显著下滑，只有掩膜引导的图像编辑与控制引导的图像生成任务的相关性分数略有上升。

**EN** Looking into the rationale, we found that the MLLMs tend to get confused by the example images, as illustrated in Figure 4. Such behavior is observed in both GPT-4v, GPT-4o, Gemini, and LLaVA rationale. Another recent work (Lu et al., 2023b) also reported a similar issue where the model attempted to consider the example when answering the visual question. This explains the deterioration of the correlation on both GPT-4v, GPT-4o, Gemini, and LLaVA when the ICL prompting technique is used. This also implied the low correlation scores on image editing tasks were due to the limited capability of state-of-the-art MLLMs for multiple image understanding.

**ZH** 查看评判理由后发现，MLLM 容易被示例图像干扰，如图 4 所示。GPT-4v、GPT-4o、Gemini 与 LLaVA 给出的理由中都观察到了这一行为。另一项近期工作（Lu 等，2023b）也报告了类似问题：模型在回答视觉问题时会试图考虑示例。这解释了为何在使用 ICL 提示技术时，GPT-4v、GPT-4o、Gemini 与 LLaVA 的相关性都会变差，也说明图像编辑任务上相关性偏低源于当前最先进 MLLM 在多图像理解上的能力有限。

<!-- [原子块 · img]  -->

**EN** Figure 4: MLLM making mistakes on rationale when prompted with extra images as examples.

**ZH** 图 4：当提示中额外给出示例图像时，MLLM 在评判理由上出错。

**EN** Ablation study on PQ rating setting. As providing multiple images could potentially decrease the performance, we attempt to minimize the workload of MLLM by only providing the synthetic image in the PQ rating process instead of including the input conditions. We report the correlation score in the two different settings with GPT-4v in Table 5 to examine the impact. We spotted a significant improvement in correlation after taking away the inputs in the PQ rating process.

**ZH** PQ 评分设置的消融研究。既然提供多张图像可能降低性能，我们尝试减轻 MLLM 的负担：在 PQ 评分过程中只提供合成图像，而不包含输入条件。表 5 报告了 GPT-4v 在两种设置下的相关性分数，以考察其影响。我们发现，在 PQ 评分过程中去掉输入后，相关性显著提升。

<!-- [原子块 · table] TIE MCIC PQ Prompting Method M-H corr P ​ Q {}^{PQ}_{\text{corr}} M-H corr P ​ Q {}^{PQ}_{\text{corr}} Human (with inputs) 0.5052 0.5145 without inputs 0.4274 0.3025 with inputs 0.2256 0.0731 -->

**EN** Table 5: Correlations of GPT-4v when including inputs in the PQ prompt in TIE (Text-guided Image Editing) and MCIC (Multi-concept Image Composition) task. See 7 for detailed comparison in Appendix.

**ZH** 表 5：在 TIE（文本引导的图像编辑）与 MCIC（多概念图像组合）任务中，PQ 提示里包含输入时 GPT-4v 的相关性。详细比较见附录 7。

**EN** Ranking image models. Besides rating score correlations, we also compared the model ranking from the ImagenHub human evaluation leaderboard and the model ranking suggested by the MLLMs, shown in Table 6. We computed Spearman’s footrule ⟦SLOT_10⟧ and Spearman’s rho ⟦SLOT_11⟧ to examine the ranking correlation. Both GPT-4v and LLaVA can align to ImagenHub rankings on the multi-concept image composition task and control-guided image generation task, and with only one model difference in the subject-driven image editing task. While the results vary significantly across other tasks, GPT-4v generally maintains a stronger alignment with the ImagenHub rankings compared to LLaVA.

**ZH** 模型排序。除评分相关性外，我们还比较了 ImagenHub 人工评估排行榜给出的模型排序与 MLLM 建议的模型排序，如表 6 所示。我们计算斯皮尔曼 footrule 距离 ⟦SLOT_10⟧ 与斯皮尔曼 rho ⟦SLOT_11⟧ 来考察排序相关性。GPT-4v 与 LLaVA 都能在多概念图像组合任务与控制引导的图像生成任务上与 ImagenHub 的排序一致，在主体驱动的图像编辑任务上只相差一个模型。尽管其他任务上结果差异较大，总体上 GPT-4v 比 LLaVA 更贴合 ImagenHub 的排序。

<!-- [原子块 · table] d S ​ F ​ ( r Human , r Method ) d_{SF}(r_{\text{Human}},r_{\text{Method}}) ↓ ρ S ​ ( r Human , r Method ) \rho_{S}(r_{\text{Human}},r_{\text{Method}}) ↑ Task (Total number of Models) GPT-4v LLaVA LPI -->

**EN** Table 6: Ranking judgment from each metric method. ⟦SLOT_12⟧ is the Spearman’s footrule and ⟦SLOT_13⟧ is the Spearman’s rho (correlation). LPIPS is not available for the first task because there are no reference images.

**ZH** 表 6：各指标方法的排序判断。⟦SLOT_12⟧ 为斯皮尔曼 footrule 距离，⟦SLOT_13⟧ 为斯皮尔曼 rho（相关系数）。第一个任务没有参考图像，故 LPIPS 不适用。

**EN** 5.2 Insights and Challenges on VIEScore

**ZH** 5.2 关于 VIEScore 的洞察与挑战

**EN** MLLMs are weak at capturing image nuances in edited images. From Table 2, we noticed the correlation scores on editing tasks are generally lower than generation tasks. Upon investigation, it was found that MLLMs often fail to detect minor changes made in image editing, such as small patch edits. Consequently, MLLMs might perceive two images as identical even when humans recognize the edits as successful. This issue may stem from MLLMs focusing on high-level image features while overlooking finer details like color and texture differences, as illustrated in Figure 5. This limitation is apparent in both GPT-4v, GPT-4o, Gemini, and LLaVA, highlighting a challenge in synthetic image evaluation accuracy on image editing tasks.

**ZH** MLLM 不擅长捕捉编辑图像中的细微差别。从表 2 可以看到，编辑任务上的相关性分数普遍低于生成任务。经查，MLLM 常常无法察觉图像编辑中做出的细微改动，例如小范围的局部编辑。结果是，即便人类认为编辑是成功的，MLLM 也可能判定两张图像完全相同。这一问题可能源于 MLLM 关注高层图像特征，却忽略了颜色、纹理等更精细的差异，如图 5 所示。GPT-4v、GPT-4o、Gemini 与 LLaVA 都存在这一局限，凸显出图像编辑任务上合成图像评估准确性所面临的挑战。

<!-- [原子块 · img]  -->

**EN** Figure 5: Representative pairs that MLLMs misunderstood as identical images. Images in the first row are the inputs and in the second row are the edited.

**ZH** 图 5：MLLM 误判为相同图像的代表性图像对。第一行为输入图像，第二行为编辑后的图像。

**EN** Both MLLMs and human evaluators display a broader range of views regarding perceptual quality compared to semantic consistency. From Table 2 and Table 3, we can observe that the correlation scores of PQ are generally lower than the correlation scores of SC and Overall, even on human raters. This suggests the human raters’ perspective on evaluating perceptual quality is more diverse. Possible impacting factors include the rater’s eyesight condition, screen resolution, rating leniency, etc. In the context of MLLMs, we found that MLLMs while being able to correctly recognize the naturalness and artifacts of the image, the rating scores are as diverse as human rating scores even though we have provided a marking rubric.

**ZH** 与语义一致性相比，MLLM 与人类评估者在感知质量上的观点分布都更为宽泛。从表 2 与表 3 可以看到，即便在人类评分者之间，PQ 的相关性分数也普遍低于 SC 与总体分数，说明人类评分者在评估感知质量时视角更为多样。可能的影响因素包括评分者的视力状况、屏幕分辨率、评分宽严程度等。在 MLLM 方面，我们发现虽然 MLLM 能正确识别图像的自然感与伪影，但即便我们提供了评分细则，其评分的分散程度仍与人类评分相当。

**EN** 5.3 VIEScore and Auto-metrics vs Human

**ZH** 5.3 VIEScore 与自动指标对比人类

**EN** We report the human correlations in Table 2 and 3 to compare the performance between our VIEScore and popular auto-metrics. To ensure a fair comparison, we only included automatic metrics that have been previously reported in related research for the specific tasks under consideration.

**ZH** 我们在表 2 与表 3 中报告人类相关性，以比较 VIEScore 与常用自动指标的表现。为保证比较公平，我们只纳入了以往相关研究中针对相应任务报告过的自动指标。

**EN** DINO is an effective metric in subject-driven tasks. The DINO metric demonstrates sensitivity to variations within the same class of subjects, making it an effective metric for measuring whether the subject in the synthesized image aligns with the token subject. Our correlation result shows that DINO outperforms GPT-4v and CLIP-I on subject-driven image generation and editing tasks, suggesting that DINO highly aligns with human’s perspective on semantic consistency where subject fidelity is considered. However, multi-subject fidelity remains a challenge as DINO and CLIP-I only consider single subjects. However, GPT-4o still achieves the highest correlation to human annotations.

**ZH** DINO 在主体驱动任务上是有效的指标。DINO 指标对同类主体内部的差异较为敏感，因此适合度量合成图像中的主体是否与词元主体一致。我们的相关性结果显示，DINO 在主体驱动的图像生成与编辑任务上优于 GPT-4v 与 CLIP-I，说明在考虑主体保真度的语义一致性方面，DINO 与人类的视角高度吻合。然而多主体保真度仍是难题，因为 DINO 与 CLIP-I 都只考虑单个主体。尽管如此，GPT-4o 与人类标注的相关性仍然最高。

**EN** LPIPS metric proves to be effective in control-guided tasks, but less effective in image editing tasks. As discussed in section 3.3, LPIPS has great ability in detecting distortions. Since the control-guided task is a less mature research direction compared to image editing tasks, distortions are often found in the synthetic images from the control-guided task. On the other hand, current image editing models can synthesize images with less distortions. This explains the high correlation in the control-guided task. While GPT-4o still achieves the highest correlation to human annotations, LPIPS outperforms GPT-4v, Gemini, and LLaVA on this task.

**ZH** LPIPS 在控制引导任务上有效，但在图像编辑任务上效果欠佳。如 3.3 节所述，LPIPS 在检测畸变方面能力突出。由于控制引导相比图像编辑是更不成熟的研究方向，其合成图像中常出现畸变；而当前图像编辑模型已能生成畸变较少的图像。这解释了 LPIPS 在控制引导任务上相关性高的原因。虽然 GPT-4o 与人类标注的相关性仍然最高，LPIPS 在该任务上优于 GPT-4v、Gemini 与 LLaVA。

**EN** CLIP-Score has a much weaker correlation with human ratings in the text-guided image generation task than GPT-4v. We also noticed none of the synthetic images achieved higher than 0.3 CLIP-Score, even though most of the images are regarded as having high semantic consistency by human raters. This can be due to different evaluation focuses, as humans tend to grab the abstract idea from the prompt to access the image, but CLIP-Score considers the whole text prompt.

**ZH** 在文本引导的图像生成任务中，CLIP-Score 与人类评分的相关性远弱于 GPT-4v。我们还注意到，尽管大多数图像被人类评分者认为语义一致性很高，却没有一张合成图像的 CLIP-Score 超过 0.3。原因可能在于评估关注点不同：人类倾向于抓住提示词的抽象含义来评判图像，而 CLIP-Score 考察的是整条文本提示。

**EN** GPT-4v outperforms other auto-metrics with its correlation to the ImagenHub leaderboard rankings. The correlation of model rankings on ImagenHub was evaluated against CLIP Score and LPIPS metrics, as shown in Table 6, and compared with MLLMs in the VIEScore. We found that GPT-4v can achieve a positive correlation with the model rankings on every task. This shows the sign of capability for MLLMs as evaluators for image synthesis research.

**ZH** 在与 ImagenHub 排行榜排序的相关性上，GPT-4v 优于其他自动指标。我们在表 6 中把 ImagenHub 上的模型排序与 CLIP Score、LPIPS 指标做了相关性评估，并与 VIEScore 中的 MLLM 比较。结果发现，GPT-4v 在每个任务上都能与模型排序取得正相关，显示出 MLLM 作为图像合成研究评估者的能力迹象。

**EN** 6 Conclusion

**ZH** 6 结论

**EN** In this paper, we propose the VIEScore for synthetic image evaluation across seven popular image synthesis tasks and comprehensively access the efficacy using human ratings from ImagenHub. Our experiment reported that VIEScore with close-source MLLMs backbones like GPT-4o and GPT-4v are significantly more effective than other open-source MLLMs in assessing synthetic images, achieving a correlation of over 0.4 to human ratings most of the tasks. However, it notes a lower correlation in image editing tasks for most of the MLLMs, including GPT-4v. We also noticed Gemini has similar performance as GPT-4v, while GPT-4o stands superior. Comparing our VIEScore to existing auto-metrics, we found that GPT-4o is more effective than auto-metrics in all tasks, while DINO is more effective in subject-driven image generation and editing tasks than GPT-4v. GPT-4v also shows a higher ranking correlation with the ImagenHub leaderboard than other automatic metrics. This marked a milestone towards explainable metrics for conditional image synthesis evaluation. Our future research will focus on investigating the use of distillation models to replicate human-like performance in evaluating synthetic images.

**ZH** 本文提出用于合成图像评估的 VIEScore，覆盖七种主流图像合成任务，并借助 ImagenHub 的人工评分全面考察其有效性。实验表明，以 GPT-4o、GPT-4v 等闭源 MLLM 为骨干的 VIEScore 在评估合成图像时显著优于其他开源 MLLM，在大多数任务上与人类评分的相关性超过 0.4。同时我们也注意到，包括 GPT-4v 在内的大多数 MLLM 在图像编辑任务上相关性偏低。Gemini 的表现与 GPT-4v 相近，而 GPT-4o 更为出色。把 VIEScore 与现有自动指标比较后发现，GPT-4o 在所有任务上都优于自动指标，而 DINO 在主体驱动的图像生成与编辑任务上优于 GPT-4v；GPT-4v 与 ImagenHub 排行榜的排序相关性也高于其他自动指标。这标志着面向条件图像合成评估的可解释指标迈出了重要一步。未来的研究将聚焦于用蒸馏模型复现人类水平的合成图像评估能力。

**EN** 7 Limitations

**ZH** 7 局限性

**EN** OpenAI Security and Privacy Policy. Due to ChatGPT’s security and privacy policy, AI-generated images that resemble a real person or photograph will be refused by GPT-4v for evaluation. The model will return results similar to "I am sorry, but I cannot process these images as they contain real people.". We simply drop those results by keyword matching.

**ZH** OpenAI 安全与隐私策略。受 ChatGPT 安全与隐私策略限制，与真实人物或照片相似的人工智能生成图像会被 GPT-4v 拒绝评估，模型会返回类似“抱歉，我无法处理这些图像，因为它们包含真实人物。”的结果。我们通过关键词匹配直接丢弃这类结果。

**EN** OpenAI Playground vs API. While GPT-4v Playground allows the user to keep a session, the OpenAI API does not provide such a function. While we believe using GPT-4v playground might yield better performance, especially in an In-Context learning setting, we can only rely on API due to the large scale of the experiment.

**ZH** OpenAI Playground 与 API。GPT-4v Playground 允许用户保持会话，而 OpenAI API 不提供该功能。我们相信使用 GPT-4v Playground 可能取得更好的表现，尤其是在上下文学习设置下；但受限于实验规模，我们只能依赖 API。

**EN** 8 Potential Risks

**ZH** 8 潜在风险

**EN** Multimodal models can inadvertently perpetuate or amplify biases present in their training data. The interpretation and evaluation of synthetic images depend heavily on context. A multimodal model might not fully grasp certain images’ nuances or cultural sensitivities, leading to inappropriate or offensive outputs.

**ZH** 多模态模型可能无意中延续或放大训练数据中存在的偏见。合成图像的解读与评估高度依赖上下文，多模态模型未必能充分把握某些图像的细微之处或文化敏感性，从而产生不当甚至冒犯性的输出。

**EN** 9 Artifacts

**ZH** 9 制品

**EN** All datasets and models are publicly accessible for academic use, and the official OpenAI API is available for academic purposes.

**ZH** 所有数据集与模型均可公开获取用于学术研究，OpenAI 官方 API 也可用于学术用途。

**EN** 10 Computational Experiments

**ZH** 10 计算实验

**EN** All open-source model experiments were conducted on an NVIDIA RTX A6000 GPU. Approximately 500 US dollars were spent on an OpenAI API call for GPT-4v and GPT-4o experiments.

**ZH** 全部开源模型实验在一块 NVIDIA RTX A6000 GPU 上进行。GPT-4v 与 GPT-4o 实验的 OpenAI API 调用花费约 500 美元。

**EN** 11 Acknowledgement

**ZH** 11 致谢

**EN** We thank Kai Zhang, Yujie Lu, and Tianle Li for the discussion. We also thank Xueguang Ma and Tianle Li for sharing the quotas of GPT-4v and GPT-4o API calls from OpenAI.

**ZH** 感谢 Kai Zhang、Yujie Lu 与 Tianle Li 的讨论，也感谢 Xueguang Ma 与 Tianle Li 分享 OpenAI 的 GPT-4v 与 GPT-4o API 调用额度。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] Avrahami et al. (2022) Omri Avrahami, Dani Lischinski, and Ohad Fried. 2022. Blended diffusion for text-driven editing of natural images. In Proceedings of the IEEE/CVF Conference on Computer Vision a -->

<!-- [原子块 · verbatim] Awadalla et al. (2023) Anas Awadalla, Irena Gao, Josh Gardner, Jack Hessel, Yusuf Hanafy, Wanrong Zhu, Kalyani Marathe, Yonatan Bitton, Samir Gadre, Shiori Sagawa, Jenia Jitsev, Simon Kornblith, Pang  -->

<!-- [原子块 · verbatim] Bai et al. (2023) Jinze Bai, Shuai Bai, Shusheng Yang, Shijie Wang, Sinan Tan, Peng Wang, Junyang Lin, Chang Zhou, and Jingren Zhou. 2023. Qwen-vl: A versatile vision-language model for understanding, -->

<!-- [原子块 · verbatim] Bar-Tal et al. (2022) Omer Bar-Tal, Dolev Ofri-Amar, Rafail Fridman, Yoni Kasten, and Tali Dekel. 2022. Text2live: Text-driven layered image and video editing. In European Conference on Computer Visio -->

<!-- [原子块 · verbatim] Bavishi et al. (2023) Rohan Bavishi, Erich Elsen, Curtis Hawthorne, Maxwell Nye, Augustus Odena, Arushi Somani, and Sağnak Taşırlar. 2023. Introducing our multimodal models . -->

<!-- [原子块 · verbatim] Brooks et al. (2023) Tim Brooks, Aleksander Holynski, and Alexei A. Efros. 2023. Instructpix2pix: Learning to follow image editing instructions. In CVPR . -->

<!-- [原子块 · verbatim] Brown et al. (2020) Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel H -->

<!-- [原子块 · verbatim] Caron et al. (2021) Mathilde Caron, Hugo Touvron, Ishan Misra, Herv’e J’egou, Julien Mairal, Piotr Bojanowski, and Armand Joulin. 2021. Emerging properties in self-supervised vision transformers . 202 -->

<!-- [原子块 · verbatim] Chen et al. (2023) Wenhu Chen, Hexiang Hu, Yandong Li, Nataniel Rui, Xuhui Jia, Ming-Wei Chang, and William W Cohen. 2023. Subject-driven text-to-image generation via apprenticeship learning. arXiv pr -->

<!-- [原子块 · verbatim] Cho et al. (2023) Jaemin Cho, Yushi Hu, Roopal Garg, Peter Anderson, Ranjay Krishna, Jason Baldridge, Mohit Bansal, Jordi Pont-Tuset, and Su Wang. 2023. Davidsonian scene graph: Improving reliability  -->

<!-- [原子块 · verbatim] Couairon et al. (2022) Guillaume Couairon, Jakob Verbeek, Holger Schwenk, and Matthieu Cord. 2022. Diffedit: Diffusion-based semantic image editing with mask guidance. In The Eleventh International Co -->

<!-- [原子块 · verbatim] Dai et al. (2023) Wenliang Dai, Junnan Li, Dongxu Li, Anthony Meng Huat Tiong, Junqi Zhao, Weisheng Wang, Boyang Albert Li, Pascale Fung, and Steven C. H. Hoi. 2023. Instructblip: Towards general-purp -->

<!-- [原子块 · verbatim] deep floyd.ai (2023) deep floyd.ai. 2023. If by deepfloyd lab at stabilityai . -->

<!-- [原子块 · verbatim] Denton et al. (2015) Emily L Denton, Soumith Chintala, Rob Fergus, et al. 2015. Deep generative image models using a laplacian pyramid of adversarial networks. Advances in neural information processin -->

<!-- [原子块 · verbatim] Dhariwal and Nichol (2021) Prafulla Dhariwal and Alexander Nichol. 2021. Diffusion models beat gans on image synthesis . In Advances in Neural Information Processing Systems , volume 34, pages 8780–87 -->

<!-- [原子块 · verbatim] Dubois et al. (2023) Yann Dubois, Xuechen Li, Rohan Taori, Tianyi Zhang, Ishaan Gulrajani, Jimmy Ba, Carlos Guestrin, Percy Liang, and Tatsunori B. Hashimoto. 2023. Alpacafarm: A simulation framework  -->

<!-- [原子块 · verbatim] Fu et al. (2023a) Jinlan Fu, See-Kiong Ng, Zhengbao Jiang, and Pengfei Liu. 2023a. Gptscore: Evaluate as you desire . ArXiv , abs/2302.04166. -->

<!-- [原子块 · verbatim] Fu et al. (2023b) Stephanie Fu, Netanel Tamir, Shobhita Sundaram, Lucy Chai, Richard Zhang, Tali Dekel, and Phillip Isola. 2023b. Dreamsim: Learning new dimensions of human visual similarity using syn -->

<!-- [原子块 · verbatim] Gal et al. (2022) Rinon Gal, Yuval Alaluf, Yuval Atzmon, Or Patashnik, Amit Haim Bermano, Gal Chechik, and Daniel Cohen-or. 2022. An image is worth one word: Personalizing text-to-image generation usi -->

<!-- [原子块 · verbatim] Goodfellow et al. (2016) Ian Goodfellow, Yoshua Bengio, Aaron Courville, and Yoshua Bengio. 2016. Deep learning , volume 1. MIT Press. -->

<!-- [原子块 · verbatim] Gu et al. (2023) Jing Gu, Yilin Wang, Nanxuan Zhao, Tsu-Jui Fu, Wei Xiong, Qing Liu, Zhifei Zhang, He Zhang, Jianming Zhang, HyunJoon Jung, et al. 2023. Photoswap: Personalized subject swapping in ima -->

<!-- [原子块 · verbatim] Hessel et al. (2021) Jack Hessel, Ari Holtzman, Maxwell Forbes, Ronan Le Bras, and Yejin Choi. 2021. Clipscore: A reference-free evaluation metric for image captioning. In Proceedings of the 2021 Conf -->

<!-- [原子块 · verbatim] Heusel et al. (2017) Martin Heusel, Hubert Ramsauer, Thomas Unterthiner, Bernhard Nessler, and Sepp Hochreiter. 2017. Gans trained by a two time-scale update rule converge to a local nash equilibrium. -->

<!-- [原子块 · verbatim] Ho et al. (2020) Jonathan Ho, Ajay Jain, and Pieter Abbeel. 2020. Denoising diffusion probabilistic models . In Advances in Neural Information Processing Systems , volume 33, pages 6840–6851. Curran A -->

<!-- [原子块 · verbatim] Hu et al. (2021) Edward J Hu, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, Weizhu Chen, et al. 2021. Lora: Low-rank adaptation of large language models. In International Conferen -->

<!-- [原子块 · verbatim] Hu et al. (2023) Yushi Hu, Benlin Liu, Jungo Kasai, Yizhong Wang, Mari Ostendorf, Ranjay Krishna, and Noah A Smith. 2023. Tifa: Accurate and interpretable text-to-image faithfulness evaluation with qu -->

<!-- [原子块 · verbatim] Huang et al. (2023) Kaiyi Huang, Kaiyue Sun, Enze Xie, Zhenguo Li, and Xihui Liu. 2023. T2i-compbench: A comprehensive benchmark for open-world compositional text-to-image generation . ArXiv , abs/230 -->

<!-- [原子块 · verbatim] Inan et al. (2021) Mert Inan, Piyush Sharma, Baber Khalid, Radu Soricut, Matthew Stone, and Malihe Alikhani. 2021. COSMic: A coherence-aware generation metric for image descriptions . In Findings of t -->

<!-- [原子块 · verbatim] Isola et al. (2017) Phillip Isola, Jun-Yan Zhu, Tinghui Zhou, and Alexei A Efros. 2017. Image-to-image translation with conditional adversarial networks. In Proceedings of the IEEE conference on compu -->

<!-- [原子块 · verbatim] Jiang et al. (2023) Dongfu Jiang, Yishan Li, Ge Zhang, Wenhao Huang, Bill Yuchen Lin, and Wenhu Chen. 2023. Tigerscore: Towards building explainable metric for all text generation tasks. arXiv preprin -->

<!-- [原子块 · verbatim] Kim et al. (2022) Jin-Hwa Kim, Yunji Kim, Jiyoung Lee, Kang Min Yoo, and Sang-Woo Lee. 2022. Mutual information divergence: A unified metric for multimodal generative models. Advances in Neural Inform -->

<!-- [原子块 · verbatim] Kim et al. (2023) Younghyun Kim, Sangwoo Mo, Min-Kyung Kim, Kyungmin Lee, Jaeho Lee, and Jinwoo Shin. 2023. Bias-to-text: Debiasing unknown visual biases through language interpretation . ArXiv . -->

<!-- [原子块 · verbatim] Ku et al. (2023) Max Ku, Tianle Li, Kai Zhang, Yujie Lu, Xingyu Fu, Wenwen Zhuang, and Wenhu Chen. 2023. Imagenhub: Standardizing the evaluation of conditional image generation models. arXiv preprint  -->

<!-- [原子块 · verbatim] Kumari et al. (2023) Nupur Kumari, Bingliang Zhang, Richard Zhang, Eli Shechtman, and Jun-Yan Zhu. 2023. Multi-concept customization of text-to-image diffusion. In Proceedings of the IEEE/CVF Conferen -->

<!-- [原子块 · verbatim] Kynkäänniemi et al. (2019) Tuomas Kynkäänniemi, Tero Karras, Samuli Laine, Jaakko Lehtinen, and Timo Aila. 2019. Improved precision and recall metric for assessing generative models. Advances in Neura -->

<!-- [原子块 · verbatim] Lee et al. (2020) Hwanhee Lee, Seunghyun Yoon, Franck Dernoncourt, Doo Soon Kim, Trung Bui, and Kyomin Jung. 2020. ViLBERTScore: Evaluating image caption using vision-and-language BERT . In Proceeding -->

<!-- [原子块 · verbatim] Lee et al. (2023) Tony Lee, Michihiro Yasunaga, Chenlin Meng, Yifan Mai, Joon Sung Park, Agrim Gupta, Yunzhi Zhang, Deepak Narayanan, Hannah Benita Teufel, Marco Bellagente, et al. 2023. Holistic eval -->

<!-- [原子块 · verbatim] Li et al. (2023a) Dongxu Li, Junnan Li, and Steven CH Hoi. 2023a. Blip-diffusion: Pre-trained subject representation for controllable text-to-image generation and editing. arXiv preprint arXiv:2305.14 -->

<!-- [原子块 · verbatim] Li et al. (2023b) Junlong Li, Shichao Sun, Weizhe Yuan, Run-Ze Fan, Hai Zhao, and Pengfei Liu. 2023b. Generative judge for evaluating alignment. arXiv preprint arXiv:2310.05470 . -->

<!-- [原子块 · verbatim] Li et al. (2022) Junnan Li, Dongxu Li, Caiming Xiong, and Steven Hoi. 2022. Blip: Bootstrapping language-image pre-training for unified vision-language understanding and generation. In International C -->

<!-- [原子块 · verbatim] Li et al. (2023c) Tianle Li, Max Ku, Cong Wei, and Wenhu Chen. 2023c. Dreamedit: Subject-driven image editing. arXiv preprint arXiv:2306.12624 . -->

<!-- [原子块 · verbatim] Liu et al. (2023a) Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. 2023a. Visual instruction tuning . ArXiv , abs/2304.08485. -->

<!-- [原子块 · verbatim] Liu et al. (2021) Jiachang Liu, Dinghan Shen, Yizhe Zhang, Bill Dolan, Lawrence Carin, and Weizhu Chen. 2021. What makes good in-context examples for gpt-3? In Workshop on Knowledge Extraction and Int -->

<!-- [原子块 · verbatim] Liu et al. (2023b) Zhiheng Liu, Yifei Zhang, Yujun Shen, Kecheng Zheng, Kai Zhu, Ruili Feng, Yu Liu, Deli Zhao, Jingren Zhou, and Yang Cao. 2023b. Cones 2: Customizable image synthesis with multiple s -->

<!-- [原子块 · verbatim] Lu et al. (2023a) Lingxiao Lu, Bo Zhang, and Li Niu. 2023a. Dreamcom: Finetuning text-guided inpainting model for image composition . ArXiv , abs/2309.15508. -->

<!-- [原子块 · verbatim] Lu et al. (2023b) Yujie Lu, Xiujun Li, William Yang Wang, and Yejin Choi. 2023b. Vim: Probing multimodal large language models for visual embedded instruction following . ArXiv , abs/2311.17647. -->

<!-- [原子块 · verbatim] Lu et al. (2023c) Yujie Lu, Xianjun Yang, Xiujun Li, Xin Eric Wang, and William Yang Wang. 2023c. Llmscore: Unveiling the power of large language models in text-to-image synthesis evaluation. arXiv pr -->

<!-- [原子块 · verbatim] Lu et al. (2023d) Yujie Lu, Xianjun Yang, Xiujun Li, Xin Eric Wang, and William Yang Wang. 2023d. Llmscore: Unveiling the power of large language models in text-to-image synthesis evaluation . ArXiv , -->

<!-- [原子块 · verbatim] Lugmayr et al. (2022) Andreas Lugmayr, Martin Danelljan, Andrés Romero, Fisher Yu, Radu Timofte, and Luc Van Gool. 2022. Repaint: Inpainting using denoising diffusion probabilistic models . 2022 IEEE/ -->

<!-- [原子块 · verbatim] Meng et al. (2021) Chenlin Meng, Yutong He, Yang Song, Jiaming Song, Jiajun Wu, Jun-Yan Zhu, and Stefano Ermon. 2021. Sdedit: Guided image synthesis and editing with stochastic differential equations. -->

<!-- [原子块 · verbatim] Mokady et al. (2023) Ron Mokady, Amir Hertz, Kfir Aberman, Yael Pritch, and Daniel Cohen-Or. 2023. Null-text inversion for editing real images using guided diffusion models. In Proceedings of the IEEE -->

<!-- [原子块 · verbatim] OpenAI (2023) OpenAI. 2023. Gpt-4 technical report . -->

<!-- [原子块 · verbatim] openjourney.ai (2023) openjourney.ai. 2023. Openjourney is an open source stable diffusion fine tuned model on midjourney images . -->

<!-- [原子块 · verbatim] Park et al. (2021) Dong Huk Park, Samaneh Azadi, Xihui Liu, Trevor Darrell, and Anna Rohrbach. 2021. Benchmark for compositional text-to-image synthesis. In Thirty-fifth Conference on Neural Informati -->

<!-- [原子块 · verbatim] Parmar et al. (2023) Gaurav Parmar, Krishna Kumar Singh, Richard Zhang, Yijun Li, Jingwan Lu, and Jun-Yan Zhu. 2023. Zero-shot image-to-image translation. In ACM SIGGRAPH 2023 Conference Proceedings , -->

<!-- [原子块 · verbatim] Parnami and Lee (2022) Archit Parnami and Minwoo Lee. 2022. Learning from few examples: A summary of approaches to few-shot learning . ArXiv , abs/2203.04291. -->

<!-- [原子块 · verbatim] Peng et al. (2023) Zhiliang Peng, Wenhui Wang, Li Dong, Yaru Hao, Shaohan Huang, Shuming Ma, and Furu Wei. 2023. Kosmos-2: Grounding multimodal large language models to the world . ArXiv , abs/2306.14 -->

<!-- [原子块 · verbatim] Qin et al. (2023) Can Qin, Shu Zhang, Ning Yu, Yihao Feng, Xinyi Yang, Yingbo Zhou, Huan Wang, Juan Carlos Niebles, Caiming Xiong, Silvio Savarese, et al. 2023. Unicontrol: A unified diffusion model f -->

<!-- [原子块 · verbatim] Ramesh et al. (2022) Aditya Ramesh, Prafulla Dhariwal, Alex Nichol, Casey Chu, and Mark Chen. 2022. Hierarchical text-conditional image generation with clip latents. arXiv preprint arXiv:2204.06125 ,  -->

<!-- [原子块 · verbatim] Rombach et al. (2022) Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, and Björn Ommer. 2022. High-resolution image synthesis with latent diffusion models. In Proceedings of the IEEE/C -->

<!-- [原子块 · verbatim] Ruiz et al. (2023) Nataniel Ruiz, Yuanzhen Li, Varun Jampani, Yael Pritch, Michael Rubinstein, and Kfir Aberman. 2023. Dreambooth: Fine tuning text-to-image diffusion models for subject-driven generat -->

<!-- [原子块 · verbatim] runwayml (2023) runwayml. 2023. Stable diffusion inpainting . -->

<!-- [原子块 · verbatim] Saharia et al. (2022) Chitwan Saharia, William Chan, Saurabh Saxena, Lala Li, Jay Whang, Emily L Denton, Kamyar Ghasemipour, Raphael Gontijo Lopes, Burcu Karagol Ayan, Tim Salimans, et al. 2022. Photo -->

<!-- [原子块 · verbatim] Sajjadi et al. (2018) Mehdi SM Sajjadi, Olivier Bachem, Mario Lucic, Olivier Bousquet, and Sylvain Gelly. 2018. Assessing generative models via precision and recall. Advances in neural information pro -->

<!-- [原子块 · verbatim] Salimans et al. (2016) Tim Salimans, Ian Goodfellow, Wojciech Zaremba, Vicki Cheung, Alec Radford, and Xi Chen. 2016. Improved techniques for training gans. Advances in neural information processing s -->

<!-- [原子块 · verbatim] Sarkar et al. (2023) Ayush Sarkar, Hanlin Mai, Amitabh Mahapatra, Svetlana Lazebnik, David Forsyth, and Anand Bhattad. 2023. Shadows don’t lie and lines can’t bend! generative models don’t know projec -->

<!-- [原子块 · verbatim] Sheynin et al. (2023) Shelly Sheynin, Adam Polyak, Uriel Singer, Yuval Kirstain, Amit Zohar, Oron Ashual, Devi Parikh, and Yaniv Taigman. 2023. Emu edit: Precise image editing via recognition and gene -->

<!-- [原子块 · verbatim] stability.ai (2023) stability.ai. 2023. Stable diffusion xl . -->

<!-- [原子块 · verbatim] Team et al. (2024) Gemini Team, Machel Reid, Nikolay Savinov, Denis Teplyashin, Dmitry, Lepikhin, Timothy Lillicrap, Jean baptiste Alayrac, Radu Soricut, Angeliki Lazaridou, Orhan Firat, Julian Schrit -->

<!-- [原子块 · verbatim] Touvron et al. (2023) Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, Aurelien Rodriguez -->

<!-- [原子块 · verbatim] Wang et al. (2023) Weihan Wang, Qingsong Lv, Wenmeng Yu, Wenyi Hong, Ji Qi, Yan Wang, Junhui Ji, Zhuoyi Yang, Lei Zhao, Xixuan Song, Jiazheng Xu, Bin Xu, Juanzi Li, Yuxiao Dong, Ming Ding, and Jie Tan -->

<!-- [原子块 · verbatim] Wu and la Torre (2023) Chen Henry Wu and Fernando De la Torre. 2023. A latent space of stochastic diffusion models for zero-shot image editing and guidance. In ICCV . -->

<!-- [原子块 · verbatim] Xu et al. (2023) Wenda Xu, Danqing Wang, Liangming Pan, Zhenqiao Song, Markus Freitag, William Yang Wang, and Lei Li. 2023. Instructscore: Towards explainable text generation evaluation with automatic -->

<!-- [原子块 · verbatim] Yang et al. (2023) Zhengyuan Yang, Linjie Li, Kevin Lin, Jianfeng Wang, Chung-Ching Lin, Zicheng Liu, and Lijuan Wang. 2023. The dawn of lmms: Preliminary explorations with gpt-4v(ision) . -->

<!-- [原子块 · verbatim] Yin et al. (2023) Shukang Yin, Chaoyou Fu, Sirui Zhao, Ke Li, Xing Sun, Tong Xu, and Enhong Chen. 2023. A survey on multimodal large language models . ArXiv , abs/2306.13549. -->

<!-- [原子块 · verbatim] Zhang et al. (2023a) Kai Zhang, Lingbo Mo, Wenhu Chen, Huan Sun, and Yu Su. 2023a. Magicbrush: A manually annotated dataset for instruction-guided image editing. NeurIPS dataset and benchmark track . -->

<!-- [原子块 · verbatim] Zhang and Agrawala (2023) Lvmin Zhang and Maneesh Agrawala. 2023. Adding conditional control to text-to-image diffusion models. arXiv preprint arXiv:2302.05543 . -->

<!-- [原子块 · verbatim] Zhang et al. (2018) Richard Zhang, Phillip Isola, Alexei A Efros, Eli Shechtman, and Oliver Wang. 2018. The unreasonable effectiveness of deep features as a perceptual metric. In CVPR . -->

<!-- [原子块 · verbatim] Zhang et al. (2023b) Xinlu Zhang, Yujie Lu, Weizhi Wang, An Yan, Jun Yan, Lianke Qin, Heng Wang, Xifeng Yan, William Yang Wang, and Linda Ruth Petzold. 2023b. Gpt-4v(ision) as a generalist evaluator f -->

<!-- [原子块 · verbatim] Zheng et al. (2023) Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric. P Xing, Hao Zhang, Joseph E. Gonzalez, and Ion Stoica.  -->

**EN** Appendix A Prompt Templates

**ZH** 附录 A 提示模板

**EN** Prompt Engineering. We found that not all MLLMs can fully understand our prompt to give a desired output format consistently. Thus we required MLLMs to output a JSON format, which is supposed to be capable for most MLLMs.

**ZH** 提示工程。我们发现并非所有 MLLM 都能完全理解我们的提示并稳定地给出期望的输出格式，因此要求 MLLM 以 JSON 格式输出，这对大多数 MLLM 而言应当可行。

**EN** Prompt Design. The prompt is divided into two segments: the ‘context prompt’ and the ‘rating prompt’. The ultimate prompt provided to the model is a combination of these two segments.

**ZH** 提示设计。提示分为两段：“上下文提示”与“评分提示”，最终提供给模型的是这两段的组合。

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

**EN** Appendix B Supplementary Information

**ZH** 附录 B 补充信息

**EN** B.1 Human Correlation Study

**ZH** B.1 人类相关性研究

**EN** In our paper content, we only reported the Spearman correlations. Here we included the Pearson and Kendall correlation in Table 8 for comparative analysis of Human-to-Human (H-H) correlation.

**ZH** 正文中只报告了斯皮尔曼相关系数。此处在表 8 中补充皮尔逊与肯德尔相关系数，用于对人类—人类（H-H）相关性做对比分析。

**EN** B.2 Zero-shot vs One-shot on VIE

**ZH** B.2 VIE 上的零样本与单样本

**EN** We applied only zero-shot and one-shot experiments in this paper because not even GPT-4v can produce anything with few-shot setting in our context. We report full table of GPT-4v performance in Table 7 for zero-shot vs one-shot results.

**ZH** 本文只做了零样本与单样本实验，因为即便 GPT-4v 在我们的场景下也无法在少样本设置下产生任何结果。表 7 给出 GPT-4v 零样本与单样本结果的完整表格。

**EN** B.3 Autometrics vs Human Detail results

**ZH** B.3 自动指标与人类的详细结果

**EN** See Table 9, 10, 11, 12 for detail statistics of CLIP-Score, LPIPS, DINO, and CLIP-I correlation with human ratings.

**ZH** CLIP-Score、LPIPS、DINO 与 CLIP-I 与人类评分相关性的详细统计分别见表 9、10、11、12。

**EN** B.4 ImagenHub Models used

**ZH** B.4 使用的 ImagenHub 模型

**EN** • Text-guided Image Generation: Stable Diffusion (SD) (Rombach et al., 2022), SDXL (stability.ai, 2023), DALLE-2 (Ramesh et al., 2022), DeepFloydIF (deep floyd.ai, 2023), OpenJourney (openjourney.ai, 2023).

**ZH** • 文本引导的图像生成：Stable Diffusion（SD）（Rombach 等，2022）、SDXL（stability.ai，2023）、DALLE-2（Ramesh 等，2022）、DeepFloydIF（deep floyd.ai，2023）、OpenJourney（openjourney.ai，2023）。

**EN** • Mask-guided Image Editing: SD (runwayml, 2023), SDXL (stability.ai, 2023), GLIDE, BlendedDiffusion (Avrahami et al., 2022)

**ZH** • 掩膜引导的图像编辑：SD（runwayml，2023）、SDXL（stability.ai，2023）、GLIDE、BlendedDiffusion（Avrahami 等，2022）

**EN** • Text-guided Image Editing: MagicBrush (Zhang et al., 2023a), InstructPix2Pix (Brooks et al., 2023), Prompt-to-Prompt (Mokady et al., 2023), CycleDiffusion (Wu and la Torre, 2023), SDEdit (Meng et al., 2021), Text2Live (Bar-Tal et al., 2022), DiffEdit (Couairon et al., 2022), Pix2PixZero (Parmar et al., 2023).

**ZH** • 文本引导的图像编辑：MagicBrush（Zhang 等，2023a）、InstructPix2Pix（Brooks 等，2023）、Prompt-to-Prompt（Mokady 等，2023）、CycleDiffusion（Wu 和 la Torre，2023）、SDEdit（Meng 等，2021）、Text2Live（Bar-Tal 等，2022）、DiffEdit（Couairon 等，2022）、Pix2PixZero（Parmar 等，2023）。

**EN** • Subject-driven Image Generation: DreamBooth (Ruiz et al., 2023), DreamBooth-Lora (Hu et al., 2021), BLIP-Diffusion (Li et al., 2023a), TextualInversion (Gal et al., 2022).

**ZH** • 主体驱动的图像生成：DreamBooth（Ruiz 等，2023）、DreamBooth-Lora（Hu 等，2021）、BLIP-Diffusion（Li 等，2023a）、TextualInversion（Gal 等，2022）。

**EN** • Subject-driven Image Editing: PhotoSwap (Gu et al., 2023), DreamEdit (Li et al., 2023c), BLIP-Diffusion.

**ZH** • 主体驱动的图像编辑：PhotoSwap（Gu 等，2023）、DreamEdit（Li 等，2023c）、BLIP-Diffusion。

**EN** • Multi-concept Image Composition: CustomDiffusion (Kumari et al., 2023), DreamBooth, TextualInversion.

**ZH** • 多概念图像组合：CustomDiffusion（Kumari 等，2023）、DreamBooth、TextualInversion。

**EN** • Control-guided Image Generation: ControlNet (Zhang and Agrawala, 2023), UniControl (Qin et al., 2023).

**ZH** • 控制引导的图像生成：ControlNet（Zhang 和 Agrawala，2023）、UniControl（Qin 等，2023）。

**EN** B.5 ImagenHub Human data information

**ZH** B.5 ImagenHub 人工数据信息

**EN** We showed the total human rating data we used for each task in Table 13.

**ZH** 表 13 给出各任务所使用的人类评分数据总量。

<!-- [原子块 · table] Backbone: GPT-4v Zero-Shot One-Shot Image Model M-H 0shot S ​ C {}^{SC}_{\text{0shot}} M-H 0shot P ​ Q {}^{PQ}_{\text{0shot}} M-H 0shot O {}^{O}_{\text{0shot}} M-H 1shot S ​ C {}^{SC}_{\text{1shot}} M -->

**EN** Table 7: Comprehensive study on the Spearman correlation between GPT-4v-to-Human (GPT-4v-H) ratings across various models, in zero-shot (0shot) and one-shot (1shot) settings, across different test categories: Semantic Consistency (SC), Perceptual Quality (PQ), and Overall (O).

**ZH** 表 7：在零样本（0shot）与单样本（1shot）设置下，GPT-4v 与人类（GPT-4v-H）评分之间斯皮尔曼相关性的综合研究，涵盖语义一致性（SC）、感知质量（PQ）与总体（O）三个测试类别。

<!-- [原子块 · table] Image Model H-H pear S ​ C {}^{SC}_{\text{pear}} H-H pear P ​ Q {}^{PQ}_{\text{pear}} H-H pear O {}^{O}_{\text{pear}} H-H spea S ​ C {}^{SC}_{\text{spea}} H-H spea P ​ Q {}^{PQ}_{\text{spea}} H-H spea -->

**EN** Table 8: Comparative analysis of Human-to-Human (H-H) correlation ratings across various models. Metrics used include Pearson’s (pear), Spearman’s (spea), and Kendall’s (kend) correlation coefficients, across different test categories: Semantic Consistency (SC), Perceptual Quality (PQ), and Overall (O).

**ZH** 表 8：各模型上人类—人类（H-H）相关性评分的对比分析。所用指标包括皮尔逊（pear）、斯皮尔曼（spea）与肯德尔（kend）相关系数，涵盖语义一致性（SC）、感知质量（PQ）与总体（O）三个测试类别。

<!-- [原子块 · table] Metric: CLIP-Score Image Model M-H corr S ​ C {}^{SC}_{\text{corr}} M-H corr P ​ Q {}^{PQ}_{\text{corr}} M-H corr O {}^{O}_{\text{corr}} Text-guided Image Generation DeepFloydIF 0.0272 0.1025 0.0332 O -->

**EN** Table 9: CLIP-Score vs Human correlation on Text-guided image generation task.

**ZH** 表 9：文本引导的图像生成任务上 CLIP-Score 与人类的相关性。

<!-- [原子块 · table] Metric: LPIPS Image Model M-H corr S ​ C {}^{SC}_{\text{corr}} M-H corr P ​ Q {}^{PQ}_{\text{corr}} M-H corr O {}^{O}_{\text{corr}} Text-guided Image Editing InstructPix2Pix 0.1652 0.4717 0.2045 Cycle -->

**EN** Table 10: LPIPS (signs inverted) vs Human correlation on several tasks.

**ZH** 表 10：多个任务上 LPIPS（符号取反）与人类的相关性。

<!-- [原子块 · table] Metric: DINO Model M-H corr S ​ C {}^{SC}_{\text{corr}} M-H corr P ​ Q {}^{PQ}_{\text{corr}} M-H corr O {}^{O}_{\text{corr}} Multi-Concept Image Composition TextualInversion 0.0759 -0.2746 0.0754 Drea -->

**EN** Table 11: DINO vs Human correlation on several tasks.

**ZH** 表 11：多个任务上 DINO 与人类的相关性。

<!-- [原子块 · table] Metric: CLIP-I Image Model M-H corr S ​ C {}^{SC}_{\text{corr}} M-H corr P ​ Q {}^{PQ}_{\text{corr}} M-H corr O {}^{O}_{\text{corr}} Multi-Concept Image Composition TextualInversion 0.1511 -0.1847 0.1 -->

**EN** Table 12: CLIP-I vs Human correlation on several tasks.

**ZH** 表 12：多个任务上 CLIP-I 与人类的相关性。

<!-- [原子块 · table] Data amount per model Total Human rating data Task: Text-guided Image Generation 197 2955 Task: Mask-guided Image Editing 179 2148 Task: Text-guided Image Editing 179 4296 Task: Subject-driven Image G -->

**EN** Table 13: Number of human ratings from ImagenHub used in this paper.

**ZH** 表 13：本文使用的 ImagenHub 人类评分数量。

**EN** Appendix C Backbone Performances

**ZH** 附录 C 骨干模型表现

**EN** C.1 Parsing MLLM outputs

**ZH** C.1 解析 MLLM 输出

**EN** We tried to parse the output using Regex and modify the format requirement if the MLLM fail to do so. If the output failed to pass our parsing rules, we fill random value as output to penalize the correlation.

**ZH** 我们尝试用正则表达式解析输出，并在 MLLM 无法满足要求时调整格式要求。若输出未能通过解析规则，我们就填入随机值作为输出，以此对相关性施加惩罚。

**EN** C.2 Observations of GPT-4o.

**ZH** C.2 对 GPT-4o 的观察

**EN** GPT-4o-2024-05-13 tends to be the best MLLM in this context. It can understand every task instruction in VIEScore and produce reasonable scores and rationale.

**ZH** GPT-4o-2024-05-13 在该场景下表现最佳，能理解 VIEScore 中的每条任务指令，并给出合理的分数与评判理由。

**EN** C.3 Observations of Gemini-Pro.

**ZH** C.3 对 Gemini-Pro 的观察

**EN** Gemini-1.5-Pro can understand every task instruction in VIEScore and produce reasonable scores and rationale, achieving similar performance as GPT-4v.

**ZH** Gemini-1.5-Pro 能理解 VIEScore 中的每条任务指令并给出合理的分数与评判理由，表现与 GPT-4v 相近。

**EN** C.4 Observations of GPT-4v.

**ZH** C.4 对 GPT-4v 的观察

**EN** GPT-4-vision-preview tends to be the second best MLLM in this context. It can understand every task instruction in VIEScore and produce reasonable scores and rationale.

**ZH** GPT-4-vision-preview 在该场景下表现第二好，能理解 VIEScore 中的每条任务指令并给出合理的分数与评判理由。

**EN** C.5 Observations of LLaVA.

**ZH** C.5 对 LLaVA 的观察

**EN** LLaVA-1.5-7B can also understand every task instruction in VIEScore and produce reasonable rationale. However, the scores produced tend to be concentrated toward certain numbers.

**ZH** LLaVA-1.5-7B 也能理解 VIEScore 中的每条任务指令并给出合理的评判理由，但所给分数往往集中在某些数值上。

**EN** C.6 Observations of Qwen-VL.

**ZH** C.6 对 Qwen-VL 的观察

**EN** Qwen-VL-7B does not understand the meaning of delimiter. However, it was able to output a JSON-like dictionary following the instructions on both SC and PQ. The rationale produced is often not reasonable.

**ZH** Qwen-VL-7B 不理解分隔符的含义，但能按指令在 SC 与 PQ 上输出类似 JSON 的字典，其给出的评判理由常常不合理。

**EN** C.7 Observations of BLIP2.

**ZH** C.7 对 BLIP2 的观察

**EN** BLIP-2 FLAN-T5-XXL often failed to produce the result formats according to the instructions, especially in PQ. It also tend to give 0 score in SC. Prompt engineering in our context does not solve the issue.

**ZH** BLIP-2 FLAN-T5-XXL 经常无法按指令产生所需的结果格式，尤其是 PQ；并且在 SC 上倾向于给出 0 分。我们在此场景下的提示工程未能解决该问题。

**EN** C.8 Observations of InstructBLIP.

**ZH** C.8 对 InstructBLIP 的观察

**EN** InstructBLIP-T5-XL shares same observation as BLIP-2 FLAN-T5-XXL.

**ZH** InstructBLIP-T5-XL 的观察结果与 BLIP-2 FLAN-T5-XXL 相同。

**EN** C.9 Observations of Fuyu.

**ZH** C.9 对 Fuyu 的观察

**EN** Fuyu-8B always output 0 and failed to follow in our instruction.

**ZH** Fuyu-8B 总是输出 0，且无法遵循我们的指令。

**EN** C.10 Observations of CogVLM.

**ZH** C.10 对 CogVLM 的观察

**EN** CogVLM tends to output numbers fall off the range [0, 10] and often failed to follow the required format. Prompt engineering in our context does not solve the issue.

**ZH** CogVLM 输出的数值常常落在 [0, 10] 区间之外，且经常无法遵循要求的格式。我们在此场景下的提示工程未能解决该问题。

**EN** C.11 Observations of OpenFlamingo.

**ZH** C.11 对 OpenFlamingo 的观察

**EN** OpenFlamingo simply printing blank as the output in our context.

**ZH** OpenFlamingo 在我们的场景下只输出空白。
