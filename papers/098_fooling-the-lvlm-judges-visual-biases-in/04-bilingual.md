# 欺骗 LVLM 裁判：基于 LVLM 评测中的视觉偏置

> 原标题：Fooling the LVLM Judges: Visual Biases in LVLM-Based Evaluation
> 作者：Yerin Hwang, Dongryeol Lee, Kyungmin Min, Taegwan Kang, Yong-il Kim, Kyomin Jung · arXiv:2505.15249 · 2025-05-21

<!-- [原子块 · verbatim] Fooling the LVLM Judges: Visual Biases in LVLM-Based Evaluation -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] Recently, large vision–language models (LVLMs) have emerged as the preferred tools for judging text–image alignment, yet their robustness along the visual modality remains underexplored. This work is  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

**EN** 1 Introduction

**ZH** 1 引言

**EN** Leveraging their dual capacities for generation and cross-modal understanding, large vision–language models (LVLMs) have been adopted as automated evaluators of text–image pairs, enabling nuanced assessments that capture semantic coherence beyond superficial matching Ku et al. 2024; Chen et al. 2024a; Chen et al. 2024b. This approach has proven particularly effective for evaluating text-to-image (T2I) generation models, where the model is presented with an image-generation prompt and its corresponding output, and is tasked with assessing their semantic alignment Zhang et al. 2023; Chen et al. 2024b. With expectations for consistent and fair assessments, LVLM-based judgments are now widely used as reward signals in the training of next-generation image generation models Zhou et al. 2024; Wang et al. 2024b.

**ZH** 凭借生成与跨模态理解的双重能力，大视觉语言模型（LVLM）已被用作文本—图像对的自动评测器，能够做出超越表层匹配、刻画语义连贯性的细致判断 Ku 等 2024; Chen 等 2024a; Chen 等 2024b。这一做法在评测文本到图像（T2I）生成模型时尤为有效：向模型呈现一条图像生成提示及其对应输出，由模型评估二者的语义对齐程度 Zhang 等 2023; Chen 等 2024b。由于人们期望这类评判一致且公平，基于 LVLM 的判断如今被广泛用于下一代图像生成模型训练中的奖励信号 Zhou 等 2024; Wang 等 2024b。

<!-- [原子块 · img]  -->

**EN** Figure 1: The LVLM judge is influenced by visual manipulations, resulting in an unfairly inflated evaluation score. Embedding the image generation instruction in the image (left) produces a manipulated image (right), leading to unfair assessment.

**ZH** 图 1：LVLM 裁判受视觉操纵影响，给出被不公平抬高的评测分数。把图像生成指令嵌入图像中（左），得到被操纵的图像（右），进而导致不公平的评估。

**EN** Despite this growing reliance, the robustness of LVLM evaluators to image variations remains largely underexplored. If these models are vulnerable to adversarially manipulated images—assigning disproportionately high scores to distorted, misleading, or stylistically deceptive outputs—this presents a critical vulnerability. Such susceptibility not only compromises the reliability of the evaluation process itself but also risks propagating flawed reward signals during the training of image generation systems.

**ZH** 尽管人们对 LVLM 评测器的依赖日深，它们面对图像变化时的稳健性却仍基本未被考察。如果这些模型容易受到对抗性操纵图像的影响——给失真、误导或风格上具有欺骗性的输出打出畸高的分数——这就构成一项严重缺陷。这种易感性不仅损害评测过程本身的可靠性，还有可能在图像生成系统的训练中传播有缺陷的奖励信号。

**EN** To address this gap, we present the first systematic study of image modality biases in T2I evaluation, revealing how they undermine the reliability of LVLM judges. Inspired by prior works on image perturbations Hendrycks and Dietterich 2019; Jia et al. 2020; Yang et al. 2023, we define a set of potential visual biases and investigate whether their introduction into an evaluated image leads LVLM judges to assign unfairly higher scores compared to the original. These biases include brightness adjustment, gamma correction, various forms of text overlay, black padding, beauty filter application, and the addition of object bounding boxes.

**ZH** 为填补这一空缺，我们首次系统研究了 T2I 评测中的图像模态偏置，揭示它们如何削弱 LVLM 裁判的可靠性。受此前关于图像扰动的工作启发 Hendrycks 与 Dietterich 2019; Jia 等 2020; Yang 等 2023，我们定义了一组潜在的视觉偏置，并考察把偏置引入被评测图像后，是否会让 LVLM 裁判给出高于原图的不公平分数。这些偏置包括亮度调整、伽马校正、多种形式的文字叠加、黑色填充、美颜滤镜的施加，以及物体边界框的添加。

**EN** Moreover, due to the absence of existing benchmarks for systematically evaluating LVLM judges, we introduce a novel fine-grained meta-evaluation benchmark FRAME (Fine-gRained Assessment of Multi-domain Evaluation), which spans five domains: Animals, People, Outdoor scenes, Indoor scenes, and Illustrations. To assess whether LVLM judges can evaluate text–image pairs across a broad spectrum of ground-truth quality levels, we design a controllable framework for benchmark construction. Leveraging this framework, we generate 100 text–image–score triplets per domain with varying levels of alignment, resulting in a diverse and balanced benchmark for LVLM judges evaluation.

**ZH** 此外，由于现有基准尚无法系统评测 LVLM 裁判，我们提出一个新的细粒度元评测基准 FRAME（Fine-gRained Assessment of Multi-domain Evaluation，多领域评测的细粒度评估），它覆盖五个领域：动物、人物、室外场景、室内场景与插画。为检验 LVLM 裁判能否在真值质量的宽广谱系上评测文本—图像对，我们设计了一套可控的基准构建框架。借助该框架，我们在每个领域生成 100 个对齐程度各异的「文本—图像—分数」三元组，从而得到一个多样且均衡的 LVLM 裁判评测基准。

**EN** By systematically incorporating predefined visual biases into our benchmark, we demonstrate that all evaluated LVLM judges are susceptible to such manipulations. Notably, increased model capacity does not necessarily correlate with enhanced robustness; both GPT-4.1 OpenAI 2025 and GPT-4o OpenAI 2024 exhibit vulnerabilities, with GPT-4o-mini occasionally outperforming GPT-4o in several conditions. Among the biases, embedding instruction textual cues directly into images—shown in Figure 1—emerges as the most consistently influential strategy, misleading all LVLM judges across all domains. Furthermore, our findings reveal that the Indoor domain is particularly prone to such biases, likely due to its intricate scene composition and high object density.

**ZH** 通过把预定义的视觉偏置系统地注入我们的基准，我们证明所有受评的 LVLM 裁判都易受这类操纵影响。值得注意的是，模型容量的提升并不必然带来稳健性的增强：GPT-4.1 OpenAI 2025 与 GPT-4o OpenAI 2024 都表现出脆弱性，GPT-4o-mini 在若干条件下甚至优于 GPT-4o。在各类偏置中，把指令的文字线索直接嵌入图像（如图 1 所示）是最为一致有效的策略，它误导了所有领域上的所有 LVLM 裁判。进一步的分析还显示，室内领域尤其容易受到这类偏置影响，很可能源于其场景构成的复杂性与较高的物体密度。

**EN** Building upon these findings, we conduct a detailed analysis based on key research questions concerning visual biases in LVLM evaluation. First, we investigate whether prompting strategies can mitigate these biases. While certain strategies lead to partial improvements, none fully eliminate the vulnerabilities, highlighting the need for more robust LVLM evaluation frameworks. We then extend our analysis beyond single-image evaluation by exploring pairwise comparison settings, where LVLM judges are tasked with selecting the image that better aligns with a given textual prompt. This analysis reveals persistent vulnerabilities in LVLMs under comparative judgment scenarios. Finally, we observe that combining multiple biases further exacerbates the vulnerability of LVLM judges.

**ZH** 在上述发现的基础上，我们围绕 LVLM 评测中的视觉偏置，针对若干关键研究问题展开细致分析。我们首先考察提示策略能否缓解这些偏置。虽然某些策略带来部分改善，但没有一种能彻底消除脆弱性，这说明需要更稳健的 LVLM 评测框架。随后我们把分析从单图评测扩展到成对比较设定：LVLM 裁判需要选出与给定文本提示更对齐的那张图像。这一分析揭示出 LVLM 在比较式判断场景下同样存在持续的脆弱性。最后我们观察到，把多种偏置组合起来会进一步加剧 LVLM 裁判的脆弱性。

**EN** 2 Related Works

**ZH** 2 相关工作

**EN** 2.1 Evaluation of Image Generation Models

**ZH** 2.1 图像生成模型的评测

**EN** To assess image-text alignment in text-to-image (T2I) generation, traditional metrics such as Fréchet Inception Distance (FID) Heusel et al. 2017 and Inception Score (IS) Salimans et al. 2016 have been widely adopted. Embedding-based methods, including CLIPScore Hessel et al. 2021 and BLIPScore Li et al. 2022, have improved evaluation by leveraging pretrained vision-language models to compute cross-modal similarity. Recent approaches incorporate human preference modeling—exemplified by PickScore Kirstain et al. 2023, ImageReward Xu et al. 2023, HPSv2 Wu et al. 2023, and Prometheus-Vision Lee et al. 2024b—to achieve better alignment with subjective judgments. Other studies have focused on compositional evaluation using question-answering frameworks Lin et al. 2024; Wu et al. 2024; Hu et al. 2023; Yarom et al. 2023, enabling more interpretable and fine-grained assessments.

**ZH** 为评估文本到图像（T2I）生成中的图文对齐，Fréchet Inception Distance（FID）Heusel 等 2017 与 Inception Score（IS）Salimans 等 2016 等传统指标被广泛采用。基于嵌入的方法，包括 CLIPScore Hessel 等 2021 与 BLIPScore Li 等 2022，利用预训练的视觉语言模型计算跨模态相似度，改进了评测效果。近期方法引入人类偏好建模——以 PickScore Kirstain 等 2023、ImageReward Xu 等 2023、HPSv2 Wu 等 2023 与 Prometheus-Vision Lee 等 2024b 为代表——以更好地契合主观判断。另一些工作则聚焦基于问答框架的组合理性评测 Lin 等 2024; Wu 等 2024; Hu 等 2023; Yarom 等 2023，使评估更具可解释性、更加细粒度。

<!-- [原子块 · table] Bias Definition Original → Biased Bounding Box Highlighting Drawing visible boxes around key objects in the image to emphasize their presence or location. → \rightarrow Authenticity Overlay Adding the -->

**EN** Table 1: Taxonomy of visual biases illustrated through comparisons between original and biased images.

**ZH** 表 1：通过原图与偏置图像的对照展示的视觉偏置分类体系。

**EN** 2.2 LLM and LVLM Judges

**ZH** 2.2 大语言模型与 LVLM 裁判

**EN** Recently, the LLM-as-a-judge paradigm has gained popularity Zheng et al. 2023; Gu et al. 2024, offering scalable and consistent evaluations Liu et al. 2023b; Zhu et al. 2023. However, these models have been shown to be vulnerable to biases and adversarial attacks Wang et al. 2024a; Liusie et al. 2024; Zeng et al. 2024; Raina et al. 2024; Lee et al. 2024a. Recently, this paradigm has been extended to multimodal scenarios through LVLM-as-a-judge frameworks Zhang et al. 2023; Ku et al. 2024; Chen et al. 2024b, although similar biases persist in these contexts as well Chen et al. 2024a. Despite these advances, visual biases in the context of T2I generation remain largely unexplored. To our knowledge, this study presents the first systematic analysis of their effects on LVLM judges in T2I tasks.

**ZH** 近来，「以大语言模型为裁判」的范式流行开来 Zheng 等 2023; Gu 等 2024，提供了可扩展且一致的评测 Liu 等 2023b; Zhu 等 2023。然而已有研究表明，这些模型容易受到偏置与对抗攻击的影响 Wang 等 2024a; Liusie 等 2024; Zeng 等 2024; Raina 等 2024; Lee 等 2024a。最近，这一范式经由「以 LVLM 为裁判」的框架被扩展到多模态场景 Zhang 等 2023; Ku 等 2024; Chen 等 2024b，但在这些情境下类似的偏置依然存在 Chen 等 2024a。尽管取得了上述进展，T2I 生成语境下的视觉偏置仍基本未被探索。据我们所知，本研究是首次系统分析这类偏置在 T2I 任务中对 LVLM 裁判的影响。

**EN** 3 Taxonomy of Visual Biases

**ZH** 3 视觉偏置的分类体系

**EN** Building on prior research on visual perturbations Hendrycks and Dietterich 2019; Jia et al. 2020; Yang et al. 2023; Yan et al. 2024; Shtedritski et al. 2023, we define visual biases as systematic manipulations of images designed to artificially enhance their perceived alignment with textual prompts. Such interventions can mislead LVLM judges, resulting in inflated evaluation scores that do not accurately reflect true semantic alignment. Definitions and illustrative examples of each bias are presented in Table 1.

**ZH** 在关于视觉扰动的已有研究基础上 Hendrycks 与 Dietterich 2019; Jia 等 2020; Yang 等 2023; Yan 等 2024; Shtedritski 等 2023，我们把视觉偏置定义为对图像施加的系统性操纵，其目的是人为提升图像与文本提示之间被感知到的对齐程度。这类干预会误导 LVLM 裁判，导致评测分数被抬高，无法准确反映真实的语义对齐。各类偏置的定义与示例见图注表 1。

**EN** Bounding Box Highlighting

**ZH** 边界框高亮

**EN** This technique manipulates images by enclosing generated objects within bounding boxes, which draws explicit attention to their presence and potentially signals successful object inclusion to the model—even when the object’s form, number, or position is inaccurate. This manipulation raises concerns that LVLMs may prioritize spatial saliency over holistic visual fidelity.

**ZH** 该技术通过把生成的物体框在边界框内来操纵图像，从而明确地把注意力引向这些物体的存在，并可能向模型传递「物体已成功包含」的信号——即便物体的形态、数量或位置并不准确。这种做法引发了一种担忧：LVLM 可能把空间显著性置于整体视觉保真度之上。

**EN** Authenticity Overlay

**ZH** 真实性叠加

**EN** This bias involves embedding the phrase "Reference Image" onto an image, introducing an implicit signal that suggests ground-truth authenticity. Although this phrase conveys no meaningful visual information, its presence may cause the model to overestimate the image’s authenticity, thereby inflating the evaluation score.

**ZH** 该偏置在图像上嵌入「Reference Image」这一短语，引入暗示真值真实性的隐含信号。尽管这个短语不携带任何有意义的视觉信息，它的出现却可能使模型高估图像的真实感，从而抬高评测分数。

**EN** Keyword Overlay

**ZH** 关键词叠加

**EN** In this manipulation, a keyword from the original textual prompt (e.g., "Cat") is overlaid on the image. Although it provides no visual evidence of alignment, this textual insertion can create an illusion of relevance and give the impression that the keyword is genuinely part of the image, encouraging the LVLM judge to assign a higher score based on superficial cross-modal coherence.

**ZH** 在这种操纵中，来自原始文本提示的某个关键词（例如「Cat」）被叠加到图像上。尽管它并未提供任何对齐的视觉证据，这种文字插入却能制造出相关性的错觉，让人以为该关键词确实属于图像内容，从而促使 LVLM 裁判基于表层的跨模态连贯性给出更高的分数。

**EN** Instruction Overlay

**ZH** 指令叠加

**EN** This bias involves overlaying the entire instruction (e.g., “generate a red dog.”) onto the image to create the illusion of strong text-image alignment. Even if the image does not accurately follow the instruction, the presence of the embedded text can mislead LVLMs by exploiting their reliance on textual cues within the image itself.

**ZH** 该偏置把整条指令（例如「generate a red dog.」）叠加到图像上，以制造图文高度对齐的错觉。即便图像并未准确遵循指令，嵌入的文字仍能利用 LVLM 对图像内部文字线索的依赖来误导它们。

**EN** Beauty Filter

**ZH** 美颜滤镜

**EN** This manipulation targets the people domain by applying aesthetic filters that enhance facial features—such as symmetry, smoothness, or brightness—in accordance with conventional attractiveness norms. Although unrelated to instruction fidelity, these enhancements can exploit aesthetic biases in LVLMs, raising fairness concerns in generative evaluation.

**ZH** 这种操纵针对人物领域，施加美化滤镜，按照惯常的吸引力标准强化面部特征——如对称性、平滑度或明亮度。尽管这些增强与指令保真度无关，它们却能利用 LVLM 中的审美偏置，在生成式评测中引发公平性方面的担忧。

**EN** Brightness Adjustment

**ZH** 亮度调整

**EN** By artificially increasing the image brightness, this manipulation enhances perceived illumination. LVLM judges may confuse visual clarity with semantic quality, leading to higher scores that do not necessarily reflect improved alignment with the instruction or the actual quality of the image.

**ZH** 通过人为提高图像亮度，这种操纵增强了被感知的照明感。LVLM 裁判可能把视觉清晰度与语义质量混为一谈，从而给出更高的分数，而这些分数未必反映出与指令的对齐度或图像真实质量的改善。

**EN** Gamma Correction

**ZH** 伽马校正

**EN** Gamma correction adjusts the tonal distribution of an image, particularly affecting the midtones. This alteration can create the perception of improved balance or sharpness, potentially directing the model’s attention toward specific regions of the image.

**ZH** 伽马校正调整图像的色调分布，对中间调的影响尤为明显。这种改动会营造出平衡感或锐度改善的印象，可能把模型的注意力导向图像的特定区域。

**EN** Black Padding

**ZH** 黑色填充

**EN** Adding black padding alters the image’s framing by isolating the core content. Though the visual semantics remain unchanged, this shift in composition can enhance the perceived focus or centrality of the subject, subtly influencing LVLM preferences.

**ZH** 加入黑色填充通过隔离核心内容来改变图像的取景。尽管视觉语义并未改变，这种构图上的变化却能增强主体被感知到的聚焦度或居中程度， 潜移默化地影响 LVLM 的偏好。

**EN** 4 FRAME Benchmark

**ZH** 4 FRAME 基准

**EN** Given the absence of a fine-grained, multi-domain meta-evaluation benchmark specifically tailored to assessing LVLMs in image generation tasks, we introduce a new benchmark, FRAME (Fine-gRained Assessment of Multi-domain Evaluation). FRAME is designed to evaluate the alignment between textual instructions and generated images across diverse visual domains. Section 4.1 describes our controllable benchmark construction methodology, which enables systematic score distribution adjustment. Section 4.2 presents key statistics of the benchmark.

**ZH** 鉴于目前缺少专门面向图像生成任务中 LVLM 评估的细粒度、多领域元评测基准，我们提出一个新基准 FRAME（Fine-gRained Assessment of Multi-domain Evaluation）。FRAME 旨在跨多个视觉领域评估文本指令与生成图像之间的对齐程度。4.1 节介绍我们可控的基准构建方法，它支持对分数分布做系统性调节。4.2 节给出该基准的关键统计。

**EN** 4.1 Benchmark Construction

**ZH** 4.1 基准构建

**EN** FRAME is a fine-grained, multi-domain meta-evaluation benchmark that supports a comprehensive assessment of image generation models. It spans five commonly used domains in image synthesis Yu et al. 2022: Animals, People, Outdoor Scenes, Indoor Scenes, and Illustrations. Each domain contains 100 evaluation instances, resulting in a total of 500 instances.

**ZH** FRAME 是一个细粒度、多领域的元评测基准，支持对图像生成模型做全面评估。它覆盖图像合成中常用的五个领域 Yu 等 2022：动物、人物、室外场景、室内场景与插画。每个领域包含 100 个评测实例，合计 500 个实例。

**EN** Each instance comprises (1) an image generation instruction, (2) a corresponding generated image, and (3) a human-annotated alignment score reflecting the degree of semantic consistency between the instruction and the image. Within each domain, we define four to five domain-specific visual concepts, carefully curated to capture distinctive visual elements. These concepts are systematically combined to create rich and contextually grounded generation instructions.

**ZH** 每个实例由三部分构成：（1）一条图像生成指令；（2）一张对应的生成图像；（3）一个人工标注的对齐分数，反映指令与图像之间语义一致的程度。在每个领域内，我们定义四到五个领域特有的视觉概念，经仔细挑选以捕捉该领域独特的视觉元素。这些概念被系统地组合，生成丰富且语境扎实的生成指令。

**EN** For instance, in the People domain, the five visual concepts are: object, number, color, background, and action. Background examples include a city street or a high school classroom, while actions range from typing on a laptop to riding a bicycle. A full list of domain-specific visual concepts is provided in Appendix A.

**ZH** 例如，在人物领域中，五个视觉概念是：物体、数量、颜色、背景与动作。背景示例包括城市街道或高中教室，动作则涵盖敲笔记本电脑到骑自行车。各领域视觉概念的完整清单见附录 A。

**EN** The benchmark is constructed through a multi-stage pipeline that includes instruction generation, controlled perturbation-based image synthesis, and human annotation.

**ZH** 该基准通过一条多阶段流程构建而成，包括指令生成、基于受控扰动的图像合成，以及人工标注。

**EN** Instruction Formulation

**ZH** 指令构造

**EN** The process begins with the random sampling of visual elements from a predefined set of domain-specific concepts. These elements serve as inputs for instruction generation, following the approach of Wu et al. 2024. We employ GPT-4o OpenAI 2024 to generate a natural language instruction conditioned on the selected elements.

**ZH** 流程始于从预定义的领域概念集合中随机采样视觉元素。这些元素作为指令生成的输入，做法沿用 Wu 等 2024。我们采用 GPT-4o OpenAI 2024，以所选元素为条件生成自然语言指令。

**EN** For example, in the Animal domain, concepts may include: object (Flamingo), number (Three), background (Meadow), and action (Drinking from a watering hole). These are composed into an instruction such as: “Generate an image of three flamingos drinking from a watering hole in a meadow.” This structured formulation ensures systematic and nuanced control over both compositional and contextual complexity.

**ZH** 例如，在动物领域中，概念可能包括：物体（火烈鸟）、数量（三只）、背景（草地）与动作（在水坑边饮水）。它们被组合成形如「Generate an image of three flamingos drinking from a watering hole in a meadow.」的指令。这种结构化的构造方式，保证了对构图复杂度与语境复杂度的系统而精细的控制。

**EN** Image Generation

**ZH** 图像生成

**EN** To produce a wide distribution of alignment scores, we apply a controllable generation framework. Rather than using only the original instructions, we introduce controlled perturbations by randomly modifying a subset of the visual concepts, yielding perturbed instructions. These perturbed prompts are then used to generate images.

**ZH** 为得到分布宽广的对齐分数，我们采用一套可控的生成框架。我们不只使用原始指令，而是通过随机修改一部分视觉概念引入受控扰动，得到扰动后的指令，再用这些扰动提示生成图像。

**EN** The number of altered concepts directly influences the expected image-text alignment: the more elements perturbed, the lower the anticipated alignment. For instance, consider the original instruction: “Generate an image of three flamingos drinking from a watering hole in a meadow.” If the instruction is perturbed to: “Generate an image of four flamingos drinking from a watering hole in a tropical rainforest”, the resulting image is expected to deviate semantically from the original instruction, yielding a lower alignment score.

**ZH** 被改动概念的数量直接影响预期的图文对齐程度：被扰动的元素越多，预期对齐度就越低。举例来说，原始指令为「Generate an image of three flamingos drinking from a watering hole in a meadow.」；若把它扰动为「Generate an image of four flamingos drinking from a watering hole in a tropical rainforest」，得到的图像在语义上预期会偏离原始指令，从而取得更低的对齐分数。

**EN** By varying the number and type of perturbed elements, we construct a benchmark that spans a broad range of semantic alignment. All images are generated using the DALL-E 3 model Betker et al. 2023 with a default setting.

**ZH** 通过改变被扰动元素的数量与类型，我们构建出一个覆盖宽广语义对齐范围的基准。所有图像均使用 DALL-E 3 模型 Betker 等 2023 的默认设置生成。

**EN** Human Annotation

**ZH** 人工标注

**EN** In the final stage, human annotators evaluate the semantic alignment between each generated image and its paired instruction. Each instance is scored based on how accurately the image reflects the instruction. Annotators are also instructed to identify and exclude cases involving unfeasible or incoherent instructions (e.g., impossible object-action combinations). Such instances are returned to the generation pipeline for regeneration. In addition, to ensure ethical integrity, any instruction that may produce harmful or inappropriate content is filtered out during this phase, guaranteeing that the resulting dataset is safe for evaluation. Further details on the human annotation procedure can be found in Appendix A

**ZH** 在最后阶段，人工标注者评估每张生成图像与其配对指令之间的语义对齐程度，依据图像反映指令的准确程度给每个实例打分。标注者还被要求识别并排除涉及不可行或自相矛盾指令的样本（例如不可能的物体—动作组合），这些实例会被退回生成流程重新生成。此外，为保证伦理上的正当性，任何可能产生有害或不当内容的指令都会在这一阶段被过滤掉，从而确保所得数据集可安全用于评测。人工标注流程的更多细节见附录 A

**EN** 4.2 Statistics

**ZH** 4.2 统计信息

**EN** Statistics of FRAME are presented in Table 2. Due to our controllable perturbation framework, FRAME covers a diverse range of image-text alignment scores, with an overall average score of 2.57 across the dataset. This wide score distribution enables robust and fine-grained evaluation of model sensitivity to both compositional and semantic variations.

**ZH** FRAME 的统计信息见表 2。得益于我们可控的扰动框架，FRAME 覆盖了范围宽广的图文对齐分数，数据集整体平均分为 2.57。这种宽分数分布使我们能稳健、细粒度地评估模型对构图变化与语义变化的敏感度。

<!-- [原子块 · table] 1-2 2-3 3-4 4-5 Total Avg. People 28 30 24 18 100 2.66 Animal 19 48 25 8 100 2.52 Illustration 27 51 12 10 100 2.36 Indoor 16 52 24 8 100 2.48 Outdoor 17 33 34 16 100 2.84 Total 107 214 119 60 500 2.5 -->

**EN** Table 2: Score distribution of the FRAME benchmark based on human evaluations. The "Avg." column shows the average alignment score per domain.

**ZH** 表 2：基于人工评估的 FRAME 基准分数分布。「Avg.」列给出各领域的平均对齐分数。

**EN** 5 Experiments

**ZH** 5 实验

**EN** We employ the FRAME benchmark and the predefined bias categories introduced in Section 3 to systematically evaluate the robustness of various LVLM judges against image-side biases. Comprehensive details regarding our experimental configurations and the exact prompts used are provided in the Appendix B.

**ZH** 我们运用 FRAME 基准与第 3 节引入的预定义偏置类别，系统评测各 LVLM 裁判面对图像侧偏置时的稳健性。实验配置与所用确切提示的完整细节见附录 B。

**EN** 5.1 Experimental Setting

**ZH** 5.1 实验设置

**EN** LVLM Judges

**ZH** LVLM 裁判

**EN** Our evaluation includes eight state-of-the-art LVLMs. This set comprises four proprietary models from the GPT family: GPT-4.1 OpenAI 2025, GPT-4.1-mini, GPT-4o OpenAI 2024, and GPT-4o-mini; three models from the LLaVA family: LLaVA-1.5-13B Liu et al. 2024, LlaVA-NEXT-8B Li et al. 2024a, and LLaVA-Onevision-7B Li et al. 2024b; and one model from the Qwen family: Qwen2.5-VL-32B-Instruct Bai et al. 2025.

**ZH** 我们的评测纳入八款先进的 LVLM。其中包括 GPT 系列的四款专有模型：GPT-4.1 OpenAI 2025、GPT-4.1-mini、GPT-4o OpenAI 2024 与 GPT-4o-mini；LLaVA 系列的三款模型：LLaVA-1.5-13B Liu 等 2024、LlaVA-NEXT-8B Li 等 2024a 与 LLaVA-Onevision-7B Li 等 2024b；以及 Qwen 系列的一款模型：Qwen2.5-VL-32B-Instruct Bai 等 2025。

**EN** Evaluation

**ZH** 评测方式

**EN** Each LVLM judge is prompted with a standardized evaluation instruction alongside a text-image pair. We first report the average scores assigned by the LVLM judges to unaltered (original) images, which serve as a baseline. Subsequently, for each bias category, we prompt the LVLM judges with the corresponding text-biased image pairs and record the average scores assigned. We then calculate and report the percentage changes in average scores relative to the original (unbiased) condition to quantify the impact of each bias on judging behavior.

**ZH** 向每个 LVLM 裁判提供标准化的评测指令以及一个文本—图像对。我们首先报告 LVLM 裁判给未经改动的（原始）图像打出的平均分，作为基线。随后，对每一类偏置，我们向 LVLM 裁判提供相应的文本—偏置图像对并记录平均分，再计算并报告平均分相对于原始（无偏置）条件的百分比变化，以量化各类偏置对评判行为的影响。

<!-- [原子块 · table] Domain Bias Orig. Bright. Gamma. Refer. Keyword. Inst. Padding. Bounding. GPT-4.1 People 1.65 1.72 (+4.2%) 1.70 (+2.7%) 1.72 (+3.9%) 1.76 (+6.4%) 1.77 (+7.0%) 1.77 (+7.3%) 1.90 (+14.9%) Animal 1.17 1. -->

**EN** Table 3: Evaluation results of five different LVLM judges assessing text-to-image generation under various image bias conditions across multiple domains. Reported values correspond to the average alignment scores assigned by each LVLM judge, with values in parentheses indicating the change relative to evaluations on original (Orig.), unmanipulated images. Number highlighted in RED signifies successful attacks, where the presence of image biases led LVLM judges to assign higher scores. Please refer to the Appendix C for more results.

**ZH** 表 3：五款不同 LVLM 裁判在多个领域、各种图像偏置条件下评测文本到图像生成的结果。报告的数值为各 LVLM 裁判给出的平均对齐分数，括号中的数值表示相对于对原始（Orig.）未操纵图像评测时的变化。标红的数字表示攻击成功，即图像偏置的存在使 LVLM 裁判给出了更高的分数。更多结果请参见附录 C。

<!-- [原子块 · object]  -->

**EN** Figure 2: Impact of visual biases across all LVLM judges. Left: Average attack success rates across five domains and seven types of visual bias. An attack is considered successful when the LVLM assigns a higher average score to the biased images than to the original counterparts. Right: Average percentage increase in score for successful attacks, reflecting the magnitude of the visual bias effect.

**ZH** 图 2：视觉偏置对所有 LVLM 裁判的影响。左图：五个领域、七类视觉偏置上的平均攻击成功率。当 LVLM 给偏置图像的平均分高于其原始对照图像时，即判定攻击成功。右图：攻击成功案例中的平均分数增幅，反映视觉偏置效应的强度。

**EN** 5.2 Results

**ZH** 5.2 结果

**EN** Table 3 presents the overall robustness results of LVLM judges when exposed to image-side biases across five distinct domains.22 2 Note that object-oriented Keyword Overlay and Bounding Box Highlighting manipulations are not applicable to the Outdoor domain, as it does not contain objects. The results reveal a consistent vulnerability to visual bias, as LVLM judges frequently assign inflated scores to image–text pairs containing visual manipulations. This susceptibility persists regardless of variations in (1) model type, (2) domain, and (3) bias category, indicating a systematic weakness in the current LVLM judge based evaluation.

**ZH** 表 3 给出 LVLM 裁判在五个不同领域上面临图像侧偏置时的整体稳健性结果。22 2 需注意，面向物体的关键词叠加与边界框高亮操纵不适用于室外领域，因为该领域不含物体。结果揭示出一种一贯的视觉偏置脆弱性：LVLM 裁判常常给含有视觉操纵的图文对打出被抬高的分数。这种易感性不因（1）模型类型、（2）领域、（3）偏置类别的变化而消失，说明当前基于 LVLM 裁判的评测存在系统性缺陷。

**EN** The vulnerability across models remains evident even as model capacity increases.

**ZH** 即便模型容量增大，跨模型的脆弱性依然明显。

**EN** As shown in Table 3, all LVLM judges, including GPT-4.1 OpenAI 2025, exhibit susceptibility to these vulnerabilities, indicating that even the advanced models are not immune to these biases. Notably, models with higher capacity are sometimes more vulnerable to certain biases; for instance, GPT-4.1 and GPT-4o show greater sensitivity to Bounding Box manipulations compared to their smaller counterparts, GPT-4.1-mini and GPT-4o-mini.

**ZH** 如表 3 所示，包括 GPT-4.1 OpenAI 2025 在内的所有 LVLM 裁判都表现出易感性，说明即便是先进模型也未能免于这些偏置。值得注意的是，容量更大的模型有时对某些偏置反而更脆弱；例如，与各自的小尺寸版本 GPT-4.1-mini 和 GPT-4o-mini 相比，GPT-4.1 与 GPT-4o 对边界框操纵更为敏感。

**EN** Figure 2 presents the attack success rate, defined as the proportion of domain–bias combinations in which manipulated images receive higher average scores, along with the average score increase in those successful cases. These results highlight how frequently and how strongly LVLM judges are influenced by visual biases. Interestingly, the results indicate that increased model capacity does not consistently correlate with improved robustness. For example, GPT-4o-mini demonstrates the strongest robustness in terms of attack success rate, with inflated scores observed in 64.71% of domain–bias combinations, compared to 67.65% for GPT-4o. Moreover, when considering the average percentage change in successful attacks, the Qwen2.5-VL-32B-Instruct model exhibits the highest robustness. Our findings reveal that larger model capacity alone does not guarantee increased resistance to visual biases. This trend may contrast with prior observations in other evaluation settings involving LLM judges Cantini et al. 2025; Howe et al. 2025, where larger models typically demonstrate greater robustness.

**ZH** 图 2 给出攻击成功率——定义为被操纵图像取得更高平均分的「领域—偏置」组合所占比例——以及这些成功案例中的平均分数增幅。这些结果说明了 LVLM 裁判受视觉偏置影响的频率与强度。有意思的是，结果表明模型容量的提升并不总是与稳健性改善相关。例如，GPT-4o-mini 在攻击成功率上表现出最强的稳健性，有 64.71% 的「领域—偏置」组合出现分数被抬高，而 GPT-4o 为 67.65%。此外，若考察攻击成功案例中的平均百分比变化，Qwen2.5-VL-32B-Instruct 模型的稳健性最高。我们的发现表明，仅靠更大的模型容量并不保证对视觉偏置有更强的抵抗力。这一趋势可能与其他评测设定中针对大语言模型裁判的既有观察形成对照 Cantini 等 2025; Howe 等 2025——在那些设定中，更大的模型通常表现出更强的稳健性。

<!-- [原子块 · table] Model Orig. Beauty. GPT-4.1 1.65 1.64 (-0.6%) GPT-4.1-mini 1.55 1.60 (+2.9%) Qwen2.5-32B-Inst. 2.14 2.21 (+3.2%) llava-1.5-13b 0.67 0.69 (+3.8%) GPT-4o 1.14 1.05 (-8.3%) GPT-4o-mini 2.32 2.31 (-0.5%)  -->

**EN** Table 4: Evaluation results of eight LVLM judges on beauty filter bias in the People domain.

**ZH** 表 4：八款 LVLM 裁判在人物领域上针对美颜滤镜偏置的评测结果。

**EN** Instruction Overlay exhibits the most pronounced impact.

**ZH** 指令叠加的影响最为显著。

**EN** Among all manipulation types, the Instruction Overlay—which directly embeds textual instructions onto the image—proves to be the most universally impactful. It consistently induces elevated scores across all LVLM judges and domains. Additionally, even subtle perturbations such as brightness adjustment (Bright.) and luminance shifts via gamma correction (Gamma.) are sufficient to mislead most LVLM judges, indicating a broad vulnerability to low-level visual changes.

**ZH** 在所有操纵类型中，把文本指令直接嵌入图像的指令叠加被证明是影响最普遍的一种，它在所有 LVLM 裁判与所有领域上都稳定地诱发更高的分数。此外，即便是亮度调整（Bright.）与经由伽马校正（Gamma.）的亮度偏移这类细微扰动，也足以误导多数 LVLM 裁判，说明模型对低层视觉变化存在广泛的脆弱性。

**EN** Table 4 presents results of the beauty filter applied to the People domain. Some models—particularly the majority of open-sourced evaluators—demonstrate a marked preference for images enhanced with beauty filters, consistently assigning them higher scores than their original versions. This finding raises ethical concerns, suggesting that current LVLMs may implicitly reinforce aesthetic biases by favoring filtered appearances.

**ZH** 表 4 给出在人物领域施加美颜滤镜的结果。部分模型——尤其是多数开源评测器——对经美颜滤镜增强的图像表现出明显偏好，稳定地给出高于原版的分数。这一发现引发伦理上的担忧：当前的 LVLM 可能通过偏爱经过滤镜处理的外观，在潜移默化中强化审美偏置。

**EN** The Indoor domain exhibits the highest susceptibility.

**ZH** 室内领域的易感性最高。

**EN** Across all models, the Indoor and Animal domains demonstrate the greatest sensitivity to visual perturbations, particularly those involving Bounding Boxes and Instruction Overlays. This elevated susceptibility likely stems from the complexity of the visual scenes and the increased reliance on accurate object recognition in these domains. In such settings, even minor visual modifications can disrupt the model’s perception of scene structure, leading to misleadingly inflated evaluation scores.

**ZH** 在所有模型上，室内与动物领域对视觉扰动最为敏感，尤其是涉及边界框与指令叠加的那些。这种更高的易感性很可能源于视觉场景的复杂性，以及这些领域对准确物体识别的更强依赖。在这样的设定下，即便是细微的视觉改动也可能扰乱模型对场景结构的感知，导致评测分数被误导性地抬高。

<!-- [原子块 · table] Bias Standard Bias-aware CoT Orig. 1.36 1.27 1.72 Bright. 1.44 (+5.9%) 1.35 (+6.2%) 1.82 (+5.7%) Gamma. 1.45 (+6.2%) 1.36 (+6.5%) 1.80 (+4.6%) Refer. 1.39 (+2.3%) 1.30 (+2.3%) 1.79 (+3.7%) Keyword. 1. -->

**EN** Table 5: Evaluation results of prompt-based mitigation strategies using GPT-4.1-mini as the LVLM judge.

**ZH** 表 5：以 GPT-4.1-mini 作为 LVLM 裁判时，基于提示的缓解策略的评测结果。

**EN** 6 Analysis

**ZH** 6 分析

**EN** In this section, we conduct a comprehensive analysis of the key research questions concerning visual biases in LVLM-based evaluation, using GPT-4.1-mini as the judge.

**ZH** 在本节中，我们以 GPT-4.1-mini 为裁判，围绕基于 LVLM 评测中的视觉偏置所对应的关键研究问题展开全面分析。

**EN** LVLM judge bias persists under counter-prompting conditions.

**ZH** 在反向提示条件下，LVLM 裁判的偏置依然存在。

**EN** Recent studies demonstrate that prompting techniques—such as Chain-of-Thought (CoT) prompting Wei et al. 2022 and explicit debiasing prompts Hwang et al. 2025 33 3 You must disregard any superficial or stylistic perturbations that do not materially affect the semantic alignment between the instruction and the generated image.—can partially mitigate biases in LLMs. To evaluate whether these techniques also reduce susceptibility to visual bias in LVLM judges, we compare their effectiveness against a standard evaluation prompt.

**ZH** 近期研究表明，思维链（CoT）提示 Wei 等 2022 与显式去偏提示 Hwang 等 2025 33 3 你必须忽略任何不会对指令与生成图像之间的语义对齐产生实质影响的表面化或风格化扰动。等提示技术能部分缓解大语言模型中的偏置。为检验这些技术是否也能降低 LVLM 裁判对视觉偏置的易感性，我们将其效果与标准评测提示作比较。

**EN** As shown in Table 5, while CoT and bias-aware prompting exhibit some efficacy in mitigating certain types of bias, they fail to eliminate the overall bias. 44 4 We report averages across four domains, excluding Outdoor where Keyword. and Bounding. are inapplicable. Interestingly, CoT prompting leads to elevated evaluation scores for images containing bounding boxes. This may be attributed to the fact that bounding boxes guide the model’s visual attention during reasoning steps, thereby facilitating object-centric reasoning and inflating evaluation scores in an unintended manner. This observation aligns with recent findings that bounding boxes can enhance the visual attention of LVLMs during CoT reasoning Sun et al. 2024; Shao et al. 2024.

**ZH** 如表 5 所示，尽管 CoT 与偏置感知提示在缓解某些类型偏置上显示出一定效果，它们并未能消除整体偏置。44 4 我们报告四个领域上的平均值，不含室外领域，因为关键词叠加与边界框高亮在该领域不适用。有意思的是，CoT 提示反而抬高了含边界框图像的评测分数。一种可能的解释是，边界框在推理步骤中引导了模型的视觉注意力，从而便利了以物体为中心的推理，并以一种非预期的方式抬高了评测分数。这一观察与近期发现相符：边界框能够在 CoT 推理过程中增强 LVLM 的视觉注意力 Sun 等 2024; Shao 等 2024。

<!-- [原子块 · object]  -->

**EN** Figure 3: Pairwise evaluation of group A vs. group B. Top: original results. Bottom: results after applying instruction overlay bias to set A.

**ZH** 图 3：A 组与 B 组的成对评测。上图：原始结果。下图：对 A 组施加指令叠加偏置后的结果。

**EN** LVLM Judge Biases are Valid in Pairwise Evaluation.

**ZH** LVLM 裁判的偏置在成对评测中同样成立。

**EN** We investigate whether the influences of visual biases persist under pairwise evaluation settings Chen et al. 2024a; Chen et al. 2024b; Lee et al. 2024a. Specifically, for each prompt in the FRAME benchmark, we generate a corresponding set of images (B) using identical generation settings as the original image set (A). In the primary comparison, the LVLM judge evaluates each original image (A) against its counterpart (B). Additionally, we prompt the LVLM judge to compare the manipulated version of an image from Group A against its unmanipulated counterpart from Group B.55 5 For each domain, we apply the bias that yielded the highest average score during the main experiments in Table 3. To control for position bias Chen et al. 2024a; Wang et al. 2023; Liu et al. 2023a, each pairwise comparison is conducted twice, with the image order reversed, and the preference scores are averaged.

**ZH** 我们考察视觉偏置的影响在成对评测设定下是否依然存在 Chen 等 2024a; Chen 等 2024b; Lee 等 2024a。具体地，对 FRAME 基准中的每条提示，我们使用与原始图像集（A）相同的生成设置生成一组对应的图像（B）。在主要比较中，LVLM 裁判逐一把原始图像（A）与其对照图像（B）作比较。此外，我们还提示 LVLM 裁判把 A 组中某张图像的被操纵版本与 B 组中未经操纵的对照图像作比较。55 5 对每个领域，我们施加表 3 主实验中平均分最高的那种偏置。为控制位置偏置 Chen 等 2024a; Wang 等 2023; Liu 等 2023a，每组成对比较都进行两次，两次的图像顺序相反，再对偏好分数取平均。

**EN** As shown in Figure 3, the introduction of visual biases consistently leads judges to favor the manipulated images. Notably, in the people, indoor, outdoor, and animal domains, baseline results show that A’s win rate is less than or equal to that of B. However, after manipulation, this ranking reverses, with A’s win rate surpassing that of B. This finding suggests that visual biases can be strategically exploited to mislead LVLM judges in pairwise evaluations, potentially resulting in unfair or inaccurate assessments of T2I generation models.

**ZH** 如图 3 所示，视觉偏置的引入使裁判一贯地偏爱被操纵的图像。值得注意的是，在人物、室内、室外与动物领域中，基线结果显示 A 的胜率小于或等于 B；而施加操纵后，这一排序发生反转，A 的胜率超过了 B。这一发现说明，视觉偏置可以被策略性地利用来误导成对评测中的 LVLM 裁判，从而可能导致对 T2I 生成模型的评估不公平或不准确。

<!-- [原子块 · table] Domain Orig. +Single bias +Combined bias People 1.55 1.68 (+8.4%) 1.71 (+10.3%) Animal 1.02 1.16 (+14.0%) 1.17 (+14.2%) Illustration 1.51 1.57 (+4.3%) 1.58 (+4.7%) Indoor 1.38 1.61 (+17.1%) 1.69 (+22. -->

**EN** Table 6: Evaluation results of combined visual manipulations using GPT-4.1-mini as the LVLM judge.

**ZH** 表 6：以 GPT-4.1-mini 作为 LVLM 裁判时，组合视觉操纵的评测结果。

**EN** Combined Visual Biases Exacerbate LVLM Judges’ Vulnerability.

**ZH** 组合视觉偏置会加剧 LVLM 裁判的脆弱性。

**EN** We investigate whether combining two visual manipulations further amplifies judgment errors made by LVLM judges. We explore all combinations of two distinct bias strategies and identify the most impactful pair per domain, as shown in Table 6. Interestingly, an instruction overlay bias is involved in four of the five most influential combinations, underscoring its predominant impact—an observation that aligns with our earlier findings.

**ZH** 我们考察把两种视觉操纵组合起来是否会进一步放大 LVLM 裁判的判断误差。我们穷举了两种不同偏置策略的所有组合，并找出每个领域上影响最大的一对，结果见表 6。有意思的是，在五个最具影响力的组合中，有四个涉及指令叠加偏置，凸显出它压倒性的影响——这与我们此前的发现一致。

**EN** As shown in the table, the application of dual biases results in a substantial increase in average evaluation scores, thereby amplifying the impact of the attack. Although the combined effect of two biases is less than the sum of their individual effects, the compounding pattern suggests that stacking additional biases, such as three or more, could lead to even greater distortions in model judgment.

**ZH** 如表中所示，施加双重偏置会显著提高平均评测分数，从而放大攻击的影响。尽管两种偏置的组合效应小于各自效应的简单相加，这种叠加模式提示我们：继续堆叠更多偏置（例如三种或以上），可能导致模型判断出现更大的扭曲。

**EN** 7 Conclusion

**ZH** 7 结论

**EN** This study uncovers a fundamental weakness in LVLM-based evaluation: susceptibility to visual biases that inflate scores without altering semantic content. Through eight defined manipulations—including brightness, overlays, and bounding boxes—we show that even state-of-the-art models are consistently misled. These vulnerabilities persist across evaluation formats and are only partially mitigated by prompting, highlighting the need for more robust assessment frameworks.

**ZH** 本研究揭示了基于 LVLM 的评测中一处根本性缺陷：它易受视觉偏置影响，在语义内容未变的情况下抬高分数。通过亮度、叠加与边界框等八种定义的操纵，我们表明即便是最先进的模型也会被一贯误导。这些脆弱性在各种评测形式下都存在，提示策略只能部分缓解，说明亟需更稳健的评估框架。

**EN** Limitations

**ZH** 局限性

**EN** As the first study to investigate the impact of image-side manipulations on LVLM-based evaluation, our work primarily focuses on representative visual modifications, including brightness adjustments and text overlays. Future research may explore more sophisticated attack strategies, including cross-model adversarial techniques or semantic-preserving perturbations. Moreover, as discussed in Section 6, the identified visual biases persist under the proposed prompting strategies. This highlights the need for future work to develop robust defense mechanisms specifically targeted at image-side manipulations.

**ZH** 作为首个研究图像侧操纵对基于 LVLM 评测之影响的工作，本文主要聚焦于代表性的视觉修改，包括亮度调整与文字叠加。未来研究可以探索更精细的攻击策略，包括跨模型的对抗技术或保持语义的扰动。此外，正如第 6 节所讨论的，已识别出的视觉偏置在本文提出的提示策略下依然存在，这说明未来工作需要专门针对图像侧操纵开发稳健的防御机制。

**EN** Moreover, since our study focuses on evaluating the robustness of LVLM judges rather than the performance of individual judges, we do not report correlation metrics between LVLM-generated scores and human judgments. However, to support future research in this area, our benchmark includes manually labeled scores provided by human annotators. These annotations can be readily used to assess human–model alignment or to train reward models in reinforcement learning with human feedback (RLHF).

**ZH** 另外，由于本文关注的是评测 LVLM 裁判的稳健性，而非单个裁判的性能，我们没有报告 LVLM 生成分数与人类判断之间的相关性指标。不过，为支持该方向的后续研究，我们的基准包含了由人工标注者提供的手工标注分数。这些标注可直接用于评估人机一致性，或用于训练人类反馈强化学习（RLHF）中的奖励模型。

**EN** Finally, our benchmark covers five domains that are commonly used in text-to-image generation tasks Yu et al. 2022. Future research could extend this framework by incorporating a broader range of domains—such as medical imaging or satellite imagery—to more comprehensively evaluate the generalizability of LVLM-based evaluators.

**ZH** 最后，我们的基准覆盖文本到图像生成任务中常用的五个领域 Yu 等 2022。未来研究可以纳入更广泛的领域——例如医学影像或卫星影像——来扩展该框架，从而更全面地评估基于 LVLM 的评测器的泛化能力。

**EN** Ethical Considerations

**ZH** 伦理考量

**EN** All models used in our study are obtained from official and publicly accessible sources. GPT models are accessed via OpenAI’s official platform, while Llava and Qwen models are acquired from their respective repositories with proper authorization. Our use of these models aligns with open science principles and adheres to the licensing terms under which they are released.

**ZH** 本研究中使用的所有模型均取自官方且可公开获取的来源。GPT 模型通过 OpenAI 官方平台访问，Llava 与 Qwen 模型则在获得适当授权后从各自的仓库获取。我们对这些模型的使用符合开放科学原则，并遵守其发布时所附的许可条款。

**EN** To ensure the ethical integrity of our benchmark, all images are manually reviewed. Any prompts or instructions that could potentially generate harmful, offensive, or inappropriate content are filtered out during this process, thereby ensuring that the final dataset is suitable for research and evaluation purposes. In the process of writing this paper, we utilize an AI assistant at the sentence level for drafting and refining individual sentences.

**ZH** 为保证基准的伦理正当性，所有图像都经过人工复核。任何可能生成有害、冒犯性或不当内容的提示或指令都在这一过程中被过滤掉，从而确保最终数据集适合研究与评测之用。在撰写本文的过程中，我们在句子层面使用了 AI 助手来起草与润色个别句子。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] Bai et al. (2025) Shuai Bai, Keqin Chen, Xuejing Liu, Jialin Wang, Wenbin Ge, Sibo Song, Kai Dang, Peng Wang, Shijie Wang, Jun Tang, Humen Zhong, Yuanzhi Zhu, Mingkun Yang, Zhaohai Li, Jianqiang Wan,  -->

<!-- [原子块 · verbatim] Betker et al. (2023) James Betker, Gabriel Goh, Li Jing, Tim Brooks, Jianfeng Wang, Linjie Li, Long Ouyang, Juntang Zhuang, Joyce Lee, Yufei Guo, Wesam Manassra, Prafulla Dhariwal, Casey Chu, Yunxin J -->

<!-- [原子块 · verbatim] Cantini et al. (2025) Riccardo Cantini, Alessio Orsino, Massimo Ruggiero, and Domenico Talia. 2025. Benchmarking adversarial robustness to bias elicitation in large language models: Scalable automated -->

<!-- [原子块 · verbatim] Chen et al. (2024a) Dongping Chen, Ruoxi Chen, Shilin Zhang, Yaochen Wang, Yinuo Liu, Huichi Zhou, Qihui Zhang, Yao Wan, Pan Zhou, and Lichao Sun. 2024a. Mllm-as-a-judge: Assessing multimodal llm-as-a -->

<!-- [原子块 · verbatim] Chen et al. (2024b) Zhaorun Chen, Yichao Du, Zichen Wen, Yiyang Zhou, Chenhang Cui, Zhenzhen Weng, Haoqin Tu, Chaoqi Wang, Zhengwei Tong, Qinglan Huang, and 1 others. 2024b. Mj-bench: Is your multimod -->

<!-- [原子块 · verbatim] Gu et al. (2024) Jiawei Gu, Xuhui Jiang, Zhichao Shi, Hexiang Tan, Xuehao Zhai, Chengjin Xu, Wei Li, Yinghan Shen, Shengjie Ma, Honghao Liu, and 1 others. 2024. A survey on llm-as-a-judge. arXiv prepr -->

<!-- [原子块 · verbatim] Hendrycks and Dietterich (2019) Dan Hendrycks and Thomas Dietterich. 2019. Benchmarking neural network robustness to common corruptions and perturbations. arXiv preprint arXiv:1903.12261 . -->

<!-- [原子块 · verbatim] Hessel et al. (2021) Jack Hessel, Ari Holtzman, Maxwell Forbes, Ronan Le Bras, and Yejin Choi. 2021. Clipscore: A reference-free evaluation metric for image captioning. In Proceedings of the 2021 Conf -->

<!-- [原子块 · verbatim] Heusel et al. (2017) Martin Heusel, Hubert Ramsauer, Thomas Unterthiner, Bernhard Nessler, and Sepp Hochreiter. 2017. Gans trained by a two time-scale update rule converge to a local nash equilibrium. -->

<!-- [原子块 · verbatim] Howe et al. (2025) Nikolaus Howe, Ian McKenzie, Oskar Hollinsworth, Michał Zajac, Tom Tseng, Aaron Tucker, Pierre-Luc Bacon, and Adam Gleave. 2025. Scaling trends in language model robustness . Prepri -->

<!-- [原子块 · verbatim] Hu et al. (2023) Yushi Hu, Benlin Liu, Jungo Kasai, Yizhong Wang, Mari Ostendorf, Ranjay Krishna, and Noah A Smith. 2023. Tifa: Accurate and interpretable text-to-image faithfulness evaluation with qu -->

<!-- [原子块 · verbatim] Hwang et al. (2025) Yerin Hwang, Yongil Kim, Jahyun Koo, Taegwan Kang, Hyunkyung Bae, and Kyomin Jung. 2025. Llms can be easily confused by instructional distractions. arXiv preprint arXiv:2502.04362  -->

<!-- [原子块 · verbatim] Jia et al. (2020) Xiaojun Jia, Xingxing Wei, Xiaochun Cao, and Xiaoguang Han. 2020. Adv-watermark: A novel watermark perturbation for adversarial examples. In Proceedings of the 28th ACM international -->

<!-- [原子块 · verbatim] Kirstain et al. (2023) Yuval Kirstain, Adam Polyak, Uriel Singer, Shahbuland Matiana, Joe Penna, and Omer Levy. 2023. Pick-a-pic: An open dataset of user preferences for text-to-image generation. Adva -->

<!-- [原子块 · verbatim] Ku et al. (2024) Max Ku, Dongfu Jiang, Cong Wei, Xiang Yue, and Wenhu Chen. 2024. Viescore: Towards explainable metrics for conditional image synthesis evaluation. In Proceedings of the 62nd Annual Me -->

<!-- [原子块 · verbatim] Lee et al. (2024a) Dongryeol Lee, Yerin Hwang, Yongil Kim, Joonsuk Park, and Kyomin Jung. 2024a. Are llm-judges robust to expressions of uncertainty? investigating the effect of epistemic markers on l -->

<!-- [原子块 · verbatim] Lee et al. (2024b) Seongyun Lee, Seungone Kim, Sue Park, Geewook Kim, and Minjoon Seo. 2024b. Prometheus-vision: Vision-language model as a judge for fine-grained evaluation. In Findings of the Associ -->

<!-- [原子块 · verbatim] Li et al. (2024a) Bo Li, Kaichen Zhang, Hao Zhang, Dong Guo, Renrui Zhang, Feng Li, Yuanhan Zhang, Ziwei Liu, and Chunyuan Li. 2024a. Llava-next: Stronger llms supercharge multimodal capabilities in t -->

<!-- [原子块 · verbatim] Li et al. (2024b) Bo Li, Yuanhan Zhang, Dong Guo, Renrui Zhang, Feng Li, Hao Zhang, Kaichen Zhang, Yanwei Li, Ziwei Liu, and Chunyuan Li. 2024b. Llava-onevision: Easy visual task transfer . Preprint , -->

<!-- [原子块 · verbatim] Li et al. (2022) Junnan Li, Dongxu Li, Caiming Xiong, and Steven Hoi. 2022. Blip: Bootstrapping language-image pre-training for unified vision-language understanding and generation. In International c -->

<!-- [原子块 · verbatim] Lin et al. (2024) Zhiqiu Lin, Deepak Pathak, Baiqi Li, Jiayao Li, Xide Xia, Graham Neubig, Pengchuan Zhang, and Deva Ramanan. 2024. Evaluating text-to-visual generation with image-to-text generation.  -->

<!-- [原子块 · verbatim] Liu et al. (2024) Haotian Liu, Chunyuan Li, Yuheng Li, and Yong Jae Lee. 2024. Improved baselines with visual instruction tuning. In Proceedings of the IEEE/CVF Conference on Computer Vision and Patte -->

<!-- [原子块 · verbatim] Liu et al. (2023a) Nelson F Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy Liang. 2023a. Lost in the middle: How language models use long contexts. arXiv p -->

<!-- [原子块 · verbatim] Liu et al. (2023b) Yang Liu, Dan Iter, Yichong Xu, Shuohang Wang, Ruochen Xu, and Chenguang Zhu. 2023b. G-eval: Nlg evaluation using gpt-4 with better human alignment. In Proceedings of the 2023 Confe -->

<!-- [原子块 · verbatim] Liusie et al. (2024) Adian Liusie, Potsawee Manakul, and Mark Gales. 2024. Llm comparative assessment: Zero-shot nlg evaluation through pairwise comparisons using large language models. In Proceedings -->

<!-- [原子块 · verbatim] OpenAI (2024) OpenAI. 2024. Hello gpt-4o. https://openai.com/index/hello-gpt-4o . Accessed: 2025-05-15. -->

<!-- [原子块 · verbatim] OpenAI (2025) OpenAI. 2025. Introducing gpt-4.1 in the api . -->

<!-- [原子块 · verbatim] Raina et al. (2024) Vyas Raina, Adian Liusie, and Mark Gales. 2024. Is llm-as-a-judge robust? investigating universal adversarial attacks on zero-shot llm assessment. In Proceedings of the 2024 Confer -->

<!-- [原子块 · verbatim] Salimans et al. (2016) Tim Salimans, Ian Goodfellow, Wojciech Zaremba, Vicki Cheung, Alec Radford, and Xi Chen. 2016. Improved techniques for training gans. Advances in neural information processing s -->

<!-- [原子块 · verbatim] Shao et al. (2024) Hao Shao, Shengju Qian, Han Xiao, Guanglu Song, Zhuofan Zong, Letian Wang, Yu Liu, and Hongsheng Li. 2024. Visual cot: Advancing multi-modal language models with a comprehensive dat -->

<!-- [原子块 · verbatim] Shtedritski et al. (2023) Aleksandar Shtedritski, Christian Rupprecht, and Andrea Vedaldi. 2023. What does clip know about a red circle? visual prompt engineering for vlms. In Proceedings of the IEEE/ -->

<!-- [原子块 · verbatim] Sun et al. (2024) Guangyan Sun, Mingyu Jin, Zhenting Wang, Cheng-Long Wang, Siqi Ma, Qifan Wang, Tong Geng, Ying Nian Wu, Yongfeng Zhang, and Dongfang Liu. 2024. Visual agents as fast and slow thinker -->

<!-- [原子块 · verbatim] Wang et al. (2024a) Peiyi Wang, Lei Li, Liang Chen, Zefan Cai, Dawei Zhu, Binghuai Lin, Yunbo Cao, Lingpeng Kong, Qi Liu, Tianyu Liu, and 1 others. 2024a. Large language models are not fair evaluators -->

<!-- [原子块 · verbatim] Wang et al. (2023) Peiyi Wang, Lei Li, Liang Chen, Zefan Cai, Dawei Zhu, Binghuai Lin, Yunbo Cao, Qi Liu, Tianyu Liu, and Zhifang Sui. 2023. Large language models are not fair evaluators. arXiv prepri -->

<!-- [原子块 · verbatim] Wang et al. (2024b) Xiyao Wang, Jiuhai Chen, Zhaoyang Wang, Yuhang Zhou, Yiyang Zhou, Huaxiu Yao, Tianyi Zhou, Tom Goldstein, Parminder Bhatia, Furong Huang, and 1 others. 2024b. Enhancing visual-lang -->

<!-- [原子块 · verbatim] Wei et al. (2022) Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, and 1 others. 2022. Chain-of-thought prompting elicits reasoning in large language mod -->

<!-- [原子块 · verbatim] Wu et al. (2023) Xiaoshi Wu, Yiming Hao, Keqiang Sun, Yixiong Chen, Feng Zhu, Rui Zhao, and Hongsheng Li. 2023. Human preference score v2: A solid benchmark for evaluating human preferences of text-to -->

<!-- [原子块 · verbatim] Wu et al. (2024) Xindi Wu, Dingli Yu, Yangsibo Huang, Olga Russakovsky, and Sanjeev Arora. 2024. Conceptmix: A compositional image generation benchmark with controllable difficulty. arXiv preprint arX -->

<!-- [原子块 · verbatim] Xu et al. (2023) Jiazheng Xu, Xiao Liu, Yuchen Wu, Yuxuan Tong, Qinkai Li, Ming Ding, Jie Tang, and Yuxiao Dong. 2023. Imagereward: Learning and evaluating human preferences for text-to-image generati -->

<!-- [原子块 · verbatim] Yan et al. (2024) An Yan, Zhengyuan Yang, Junda Wu, Wanrong Zhu, Jianwei Yang, Linjie Li, Kevin Lin, Jianfeng Wang, Julian McAuley, Jianfeng Gao, and 1 others. 2024. List items one by one: A new data  -->

<!-- [原子块 · verbatim] Yang et al. (2023) Jianwei Yang, Hao Zhang, Feng Li, Xueyan Zou, Chunyuan Li, and Jianfeng Gao. 2023. Set-of-mark prompting unleashes extraordinary visual grounding in gpt-4v. arXiv preprint arXiv:231 -->

<!-- [原子块 · verbatim] Yarom et al. (2023) Michal Yarom, Yonatan Bitton, Soravit Changpinyo, Roee Aharoni, Jonathan Herzig, Oran Lang, Eran Ofek, and Idan Szpektor. 2023. What you see is what you read? improving text-image  -->

<!-- [原子块 · verbatim] Yu et al. (2022) Jiahui Yu, Yuanzhong Xu, Jing Yu Koh, Thang Luong, Gunjan Baid, Zirui Wang, Vijay Vasudevan, Alexander Ku, and 1 others. 2022. Scaling autoregressive models for content-rich text-to-i -->

<!-- [原子块 · verbatim] Zeng et al. (2024) Zhiyuan Zeng, Jiatong Yu, Tianyu Gao, Yu Meng, Tanya Goyal, and Danqi Chen. 2024. Evaluating large language models at evaluating instruction following. In 12th International Confere -->

<!-- [原子块 · verbatim] Zhang et al. (2023) Xinlu Zhang, Yujie Lu, Weizhi Wang, An Yan, Jun Yan, Lianke Qin, Heng Wang, Xifeng Yan, William Yang Wang, and Linda Ruth Petzold. 2023. Gpt-4v (ision) as a generalist evaluator fo -->

<!-- [原子块 · verbatim] Zheng et al. (2023) Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric Xing, and 1 others. 2023. Judging llm-as-a-judge with mt -->

<!-- [原子块 · verbatim] Zhou et al. (2024) Yiyang Zhou, Zhiyuan Fan, Dongjie Cheng, Sihan Yang, Zhaorun Chen, Chenhang Cui, Xiyao Wang, Yun Li, Linjun Zhang, and Huaxiu Yao. 2024. Calibrated self-rewarding vision language mo -->

<!-- [原子块 · verbatim] Zhu et al. (2023) Lianghui Zhu, Xinggang Wang, and Xinlong Wang. 2023. Judgelm: Fine-tuned large language models are scalable judges. arXiv preprint arXiv:2310.17631 . -->

**EN** Appendix A Details of Benchmark Construction

**ZH** 附录 A 基准构建细节

**EN** The visual concepts associated with each domain used in the benchmark construction are listed in Table 7. For each domain, we randomly sample visual elements from the corresponding concept list and prompt GPT-4o to generate a natural language instruction conditioned on the selected elements. Subsequently, we use the DALL-E 3 model Betker et al. 2023, with its default configuration, to generate images based on the generated instructions. The interface used for human annotation of our dataset is shown in Figure 8.

**ZH** 基准构建中用到的各领域视觉概念列于表 7。对每个领域，我们从相应的概念清单中随机采样视觉元素，并提示 GPT-4o 以所选元素为条件生成自然语言指令。随后，我们使用 DALL-E 3 模型 Betker 等 2023 的默认配置，依据生成的指令生成图像。我们数据集人工标注所用的界面见图 8。

**EN** Appendix B Details of Experimental Setup

**ZH** 附录 B 实验设置细节

**EN** B.1 Model Choice

**ZH** B.1 模型选择

**EN** The specific versions of the GPT models used in our experiments are as follows: gpt-4.1-2025-04-14, gpt-4.1-mini-2025-04-14, gpt-4o-2024-08-06, and gpt-4o-mini-2024-07-18.

**ZH** 实验中所用 GPT 模型的具体版本如下：gpt-4.1-2025-04-14、gpt-4.1-mini-2025-04-14、gpt-4o-2024-08-06 与 gpt-4o-mini-2024-07-18。

**EN** For the open-source models, we utilize the following: Llava-1.5-13b66 6 https://huggingface.co/llava-hf/llava-1.5-13b-hf, Llava-next-8b77 7 https://huggingface.co/llava-hf/llama3-llava-next-8b-hf, Llava-onevision-7b88 8 https://huggingface.co/llava-hf/llava-onevision-qwen2-7b-ov-hf, and Qwen2.5-32B-Instruct99 9 https://huggingface.co/Qwen/Qwen2.5-VL-32B-Instruct. All models are retrieved from Hugging Face’s official repositories to ensure consistency and reproducibility.

**ZH** 开源模型方面，我们使用以下版本：Llava-1.5-13b66 6 https://huggingface.co/llava-hf/llava-1.5-13b-hf、Llava-next-8b77 7 https://huggingface.co/llava-hf/llama3-llava-next-8b-hf、Llava-onevision-7b88 8 https://huggingface.co/llava-hf/llava-onevision-qwen2-7b-ov-hf，以及 Qwen2.5-32B-Instruct99 9 https://huggingface.co/Qwen/Qwen2.5-VL-32B-Instruct。所有模型均取自 Hugging Face 官方仓库，以确保一致性与可复现性。

**EN** B.2 Evaluation Prompts

**ZH** B.2 评测提示

**EN** For the single evaluation setting used in the main experiment (Table 3), we adopt the prompt template presented in Figure 4. To facilitate the analysis of prompting strategies (Table 5), we employ two additional templates: a bias-aware prompt (Figure 5) and a Chain-of-Thought (CoT) prompt (Figure 6). Lastly, for the analysis involving pairwise evaluation (Table 3), we use the template illustrated in Figure 7.

**ZH** 主实验（表 3）所用的单图评测设定采用图 4 给出的提示模板。为便于分析提示策略（表 5），我们另用两个模板：偏置感知提示（图 5）与思维链（CoT）提示（图 6）。最后，成对评测（表 3）的分析采用图 7 所示模板。

**EN** B.3 Bias Recipe

**ZH** B.3 偏置配方

**EN** For brightness adjustment and gamma correction, we search over the following set of scaling factors: [0.9, 0.95, 1.03, 1.05, 1.1, 1.11, 1.15, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 2.0, 2.1, 2.3], and report the most impactful value per setting. For text overlay methods—including Authenticity, Keyword, and Instruction—we vary the overlay position among five predefined locations: bottom-right, bottom-left, top-right, top-left, and center. The font size is fixed at 30 for Authenticity and Keyword overlays, and at 20 for Instruction overlays, to account for the longer instruction text length. For the black padding bias, we test a range of padding thickness values: [10, 15, 20, 25, 30, 40, 50]. The beauty filter is applied using an open-source implementation from https://github.com/TencentARC/GFPGAN. Bounding boxes are manually annotated by one of the co-authors using the annotation tool at https://www.makesense.ai.

**ZH** 对于亮度调整与伽马校正，我们在如下缩放因子集合上搜索：[0.9, 0.95, 1.03, 1.05, 1.1, 1.11, 1.15, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 2.0, 2.1, 2.3]，并报告每种设定下影响最大的取值。对于真实性、关键词与指令这三类文字叠加方法，我们在五个预定义位置间变动叠加位置：右下、左下、右上、左上与居中。考虑到指令文本更长，真实性叠加与关键词叠加的字号固定为 30，指令叠加的字号固定为 20。对于黑色填充偏置，我们测试了一系列填充厚度值：[10, 15, 20, 25, 30, 40, 50]。美颜滤镜采用 https://github.com/TencentARC/GFPGAN 的开源实现。边界框由一位共同作者使用 https://www.makesense.ai 的标注工具手工标注。

**EN** Recipe for Main experiments

**ZH** 主实验的配方

**EN** We release the full set of bias configurations used in our experiments (Table 3 and C), including the most effective parameters for each model, domain, and manipulation type (Bright., Gamma., Refer., Keyword., Inst., Padding.). Detailed recipes are presented in Tables 8 and 9.

**ZH** 我们公开实验中所用的全部偏置配置（表 3 与附录 C），包括针对每个模型、每个领域与每种操纵类型（Bright.、Gamma.、Refer.、Keyword.、Inst.、Padding.）最有效的参数。详细配方见表 8 与表 9。

**EN** Recipe for Analysis

**ZH** 分析的配方

**EN** We employ the GPT-4.1-mini model for all analysis experiments. For the prompt-based mitigation experiments in Table 5, we use the most effective parameters identified for GPT-4.1-mini per domain and bias type, as shown in Table 8 (e.g., a value of 0.9 for Bright. in the People domain, and the ‘center’ position for Instruction Overlay in the Illustration domain).

**ZH** 所有分析实验均采用 GPT-4.1-mini 模型。对于表 5 中基于提示的缓解实验，我们使用表 8 中针对 GPT-4.1-mini 在各领域、各偏置类型上识别出的最有效参数（例如人物领域中 Bright. 取 0.9，插画领域中指令叠加取「center」位置）。

**EN** In the pairwise evaluation experiments (Figure 3), we apply the most impactful overlay positions for the Instruction Overlay bias, as determined from Table 8 (e.g., top-right’ in the People domain and bottom-right’ in the Animal domain).

**ZH** 在成对评测实验（图 3）中，我们采用表 8 所确定的、对指令叠加偏置影响最大的叠加位置（例如人物领域取「top-right」，动物领域取「bottom-right」）。

**EN** Lastly, in the combined visual biases experiment (Table 6), we evaluate all possible combinations of two biases based on the GPT-4.1-mini recipe in Table 8 and report the most effective combinations per domain in Table 10.

**ZH** 最后，在组合视觉偏置实验（表 6）中，我们基于表 8 中 GPT-4.1-mini 的配方评估了两种偏置的所有可能组合，并在表 10 中报告每个领域上最有效的组合。

**EN** Appendix C Additional Experimental Results

**ZH** 附录 C 补充实验结果

**EN** Additional experiment results using three additional models (GPT-4o-mini, llama3-llava-next-8b, and llava-onevision-qwen2-7b-ov) are shown in Table 11.

**ZH** 使用另外三款模型（GPT-4o-mini、llama3-llava-next-8b 与 llava-onevision-qwen2-7b-ov）得到的补充实验结果见表 11。

<!-- [原子块 · table] Domain Attribute Values Animals Object Dog, Cat, Lion, Tiger, Elephant, Giraffe, Zebra, Kangaroo, Panda, Gorilla, Eagle, etc. Number one, two, three, four, five Background Tropical Rainforest, Flower  -->

**EN** Table 7: Visual Concepts List used for Benchmark Construction

**ZH** 表 7：基准构建所用的视觉概念清单

<!-- [原子块 · svg]  -->

**EN** Figure 4: Prompt template used for single-image scoring evaluations reported in Table 3.

**ZH** 图 4：表 3 中单图打分评测所用的提示模板。

<!-- [原子块 · svg]  -->

**EN** Figure 5: Prompt template used for bias-aware promoting methods reported in Table 5.

**ZH** 图 5：表 5 中偏置感知提示方法所用的提示模板。

<!-- [原子块 · svg]  -->

**EN** Figure 6: Prompt template used for CoT prompting methods reported in Table 5.

**ZH** 图 6：表 5 中 CoT 提示方法所用的提示模板。

<!-- [原子块 · svg]  -->

**EN** Figure 7: Prompt template used for pairwise scoring evaluations reported in Figure 3.

**ZH** 图 7：图 3 中成对打分评测所用的提示模板。

<!-- [原子块 · table] Domain Bias Bright. Gamma. Refer. Keyword. Inst. Padding. GPT-4.1 People 1.7 1.5 top-right top-right bottom-right 50 Animal 1.5 2.3 center top-left bottom-left 20 Illustration 1.3 0.9 bottom-left bott -->

**EN** Table 8: Most impactful parameters for each bias type across domains and model types (Part 1).

**ZH** 表 8：各领域、各模型类型上各类偏置的最有效参数（第 1 部分）。

<!-- [原子块 · table] Domain Bias Bright. Gamma. Refer. Keyword. Inst. Padding. GPT-4o-mini People 1.2 1.3 top-left top-left top-right 20 Animal 1.2 1.7 bottom-left top-left top-right 50 Illustration 1.03 1.3 bottom-right  -->

**EN** Table 9: Most impactful parameters for each bias type across domains and model types (Part 2).

**ZH** 表 9：各领域、各模型类型上各类偏置的最有效参数（第 2 部分）。

<!-- [原子块 · table] Domain Combined bias recipe People Inst.: “top-right” + Beauty. Animal Refer.: “center” + Gamma.:“2.1” Illustration Inst.: “center” + Gamma.: “0.9” Indoor Inst.: “center” + Padding.: “40” Outdoor Inst -->

**EN** Table 10: Most impactful combinations of two visual biases for GPT-4.1-mini across different domains.

**ZH** 表 10：GPT-4.1-mini 在不同领域上两种视觉偏置的最有效组合。

<!-- [原子块 · table] Domain Bias Orig. Bright. Gamma. Refer. Keyword. Inst. Padding. Bounding. GPT-4o-mini People 2.32 2.32 (0.0%) 2.32 (0.0%) 2.30 (-1.0%) 2.42 (+4.3%) 2.60 (+11.8%) 2.29 (-1.3%) 3.07 (+32.2%) Animal 1.76 -->

**EN** Table 11: Evaluation results of three additional LVLM judges assessing text-to-image generation under various image bias conditions across multiple domains. Reported values correspond to the average alignment scores assigned by each LVLM judge, with values in parentheses indicating the change relative to evaluations on original (Orig.), unmanipulated images. Number highlighted in RED signifies successful attacks, where the presence of image biases led LVLM judges to assign higher scores.

**ZH** 表 11：另外三款 LVLM 裁判在多个领域、各种图像偏置条件下评测文本到图像生成的结果。报告的数值为各 LVLM 裁判给出的平均对齐分数，括号中的数值表示相对于对原始（Orig.）未操纵图像评测时的变化。标红的数字表示攻击成功，即图像偏置的存在使 LVLM 裁判给出了更高的分数。

<!-- [原子块 · img]  -->

**EN** Figure 8: Human annotation task interface.

**ZH** 图 8：人工标注任务界面。
