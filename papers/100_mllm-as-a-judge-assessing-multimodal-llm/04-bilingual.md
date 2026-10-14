# MLLM-as-a-Judge：用视觉—语言基准评估多模态大模型作为裁判的能力

> 原标题：MLLM-as-a-Judge: Assessing Multimodal LLM-as-a-Judge with Vision-Language Benchmark
> 作者：Dongping Chen, Ruoxi Chen, Shilin Zhang, Yinuo Liu, Yaochen Wang, Huichi Zhou, Qihui Zhang, Yao Wan, Pan Zhou, Lichao Sun · arXiv:2402.04788 · 2024-02-07

<!-- [原子块 · verbatim] MLLM-as-a-Judge: Assessing Multimodal LLM-as-a-Judge with Vision-Language Benchmark -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] Multimodal Large Language Models (MLLMs) have gained significant attention recently, showing remarkable potential in artificial general intelligence. However, assessing the utility of MLLMs presents c -->

**EN** 1 Introduction

**ZH** 1 引言

**EN** The advent of Large Language Models (LLMs), such as GPT-3 (OpenAI, 2023) and Llama (Touvron et al., 2023), has achieved substantial progress in content generation, including text generation (OpenAI, 2023), code generation (Roziere et al., 2023), and video synthesis (Wu et al., 2023a). The emergent abilities of LLMs, as demonstrated by the Chain-of-Thought (CoT) framework (Wei et al., 2022), present a promising avenue for their utilization as evaluators, also referred to as the LLM-as-a-Judge (Zheng et al., 2023b). Initial explorations indicate a better alignment with human preferences, emphasizing the considerable potential inherent in this approach.

**ZH** GPT-3（OpenAI, 2023）与 Llama（Touvron 等, 2023）等大语言模型（LLM）的出现在内容生成上取得了长足进展，涵盖文本生成（OpenAI, 2023）、代码生成（Roziere 等, 2023）与视频合成（Wu 等, 2023a）。如思维链（Chain-of-Thought, CoT）框架（Wei 等, 2022）所展示的那样，LLM 的涌现能力为把其用作评估者——即所谓 LLM-as-a-Judge（以大模型为裁判）（Zheng 等, 2023b）——提供了一条颇具前景的路径。初步探索显示它们与人类偏好有较好的一致性，凸显了这一路线所蕴含的可观潜力。

**EN** Recently, building upon LLMs, Multimodal Large Language Models (MLLMs) like GPT-4V (OpenAI, 2023) and LLaVA (Liu et al., 2023d) exhibit exceptional proficiency by incorporating multiple modalities (e.g., text, charts, images, and videos) and showcasing remarkable performance in multimodal applications, including text-to-video (Wu et al., 2023a) and visual dialog (Cai et al., 2023). Despite this, assessing the effectiveness of MLLMs remains challenging due to the limitations of traditional metrics, which hinge on text-based exact matches or embedding distances. These metrics fall short in adhering to the granular evaluation criteria of interest and fail to capture the rich context within the generated outputs. Drawing inspiration from the concept of LLM-as-a-Judge within LLMs, a pertinent research question arises: “Can MLLMs effectively serve as judges in the multimodal domain, and how closely do their evaluations align with human preferences?”

**ZH** 近来，在 LLM 之上构建的多模态大语言模型（MLLM），如 GPT-4V（OpenAI, 2023）与 LLaVA（Liu 等, 2023d），通过纳入文本、图表、图像与视频等多种模态展现出出色的能力，并在文本到视频（Wu 等, 2023a）与视觉对话（Cai 等, 2023）等多模态应用中表现优异。尽管如此，评估 MLLM 的有效性仍然困难：传统指标依赖基于文本的精确匹配或嵌入距离，既难以遵循我们所关心的细粒度评测准则，也无法捕捉生成输出中的丰富语境。受 LLM 领域中 LLM-as-a-Judge 概念的启发，一个切题的研究问题随之浮现：「MLLM 能否在多模态领域有效地充当裁判？它们的判定与人类偏好的契合程度如何？」

<!-- [原子块 · object]  -->

**EN** Figure 1: Comparative performance of different MLLMs across three judging settings in 10 datasets, each is the average of three iterations. As the CogVLM is unable to perform the batch ranking task, we show the other six MLLMs only.

**ZH** 图 1：不同 MLLM 在 10 个数据集、三种判定设定下的性能对比，每项均为三次迭代的平均。由于 CogVLM 无法完成批量排序任务，图中只展示其余六个 MLLM。

**EN** To answer this question, this paper undertakes an extensive study, introducing a groundbreaking benchmark, MLLM-as-a-Judge, specifically crafted to evaluate the efficacy of MLLMs in assisting judges across diverse modalities. To achieve this goal, we first thoughtfully curate a selection of 14 datasets across various tasks, including image captioning, math reasoning, text reading, and infographics understanding, culminating in acquiring a dataset comprising 4,414 image-instruction pairs. Subsequently, we utilize six main-stream MLLMs from a model pool which includes GPT-4V (OpenAI, 2023), Gemini (GeminiTeam, 2023)11 1 For conciseness, we refer to GPT-4V(ision) as GPT-4V, and Gemini-Pro-Vision as Gemini throughout this paper., LLaVA-1.5-13b, LLaVA-1.6-34b (Liu et al., 2023d), CogVLM (Wang et al., 2023c), Qwen-VL-Max (Bai et al., 2023a), to generate responses to each instruction across three distinct evaluation settings. The produced responses are subsequently gathered and undergo additional annotation by human evaluators, who apply stringent criteria to ensure an impartial and thorough assessment of the judgments made by the MLLMs.

**ZH** 为回答这一问题，本文开展了广泛研究，提出了一个开创性的基准 MLLM-as-a-Judge，专门用于评估 MLLM 在跨模态辅助判定中的效力。为实现这一目标，我们首先精心挑选了涵盖图像描述、数学推理、文本阅读与信息图理解等各类任务的 14 个数据集，最终得到包含 4,414 个图像—指令对的数据集。随后，我们从一个包含 GPT-4V（OpenAI, 2023）、Gemini（GeminiTeam, 2023）11、LLaVA-1.5-13b、LLaVA-1.6-34b（Liu 等, 2023d）、CogVLM（Wang 等, 2023c）、Qwen-VL-Max（Bai 等, 2023a）的模型池中调用六个主流 MLLM，在三种不同的评测设定下为每条指令生成回答。生成的回答随后被收集起来，并由人工评估者追加标注；后者采用严格的准则，以确保对 MLLM 所作判定作出公正而彻底的评估。

**EN** Furthermore, we assess the ability of MLLMs as judges in multimodal tasks by calculating the similarity between human and MLLMs judgment and measuring human agreement on the analysis and judgment made by those MLLMs. In particular, we target eleven widely-used MLLMs, i.e., GPT-4V and Gemini-Pro-1.0/1.5, CogVLM, LLaVA-1.5/1.6 family, and Qwen-VL family, across two settings (with, or without vision input), over three distinct tasks (i.e., Scoring Evaluation, Pair Comparison, and Batch Ranking). Figure 1 compares the performance of various MLLMs across different datasets and settings, illustrating that GPT-4V exhibits significantly superior capabilities as a judge compared to other MLLMs.

**ZH** 此外，我们通过计算人类与 MLLM 判定之间的相似度，并度量人类对 MLLM 所作分析与判定的认同度，来评估 MLLM 在多模态任务中作为裁判的能力。具体地，我们以 11 个被广泛使用的 MLLM 为目标，即 GPT-4V 与 Gemini-Pro-1.0/1.5、CogVLM、LLaVA-1.5/1.6 系列以及 Qwen-VL 系列，在两种设定下（有视觉输入与无视觉输入）、跨越三类任务（即评分评测、成对比较与批量排序）进行考察。图 1 比较了各 MLLM 在不同数据集与设定下的表现，说明 GPT-4V 作为裁判的能力显著优于其他 MLLM。

**EN** As a benchmark, we also release two curated datasets to facilitate further studies: MLLM-as-a-Judge-HQ, which showcases responses with a high level of concordance with human judgments, and MLLM-as-a-Judge-Hard, which includes responses marked by inconsistency with human preferences and instances of hallucination. Additionally, we address the limitations of MLLMs in judgment, such as egocentric bias, position bias, length bias, and hallucination. We demonstrate that integrating CoT (Wei et al., 2022) and a vision expert system can effectively mitigate some of these biases.

**ZH** 作为一个基准，我们还发布两个经过整理的数据集以促进后续研究：MLLM-as-a-Judge-HQ，展示与人类判断高度一致的回答；以及 MLLM-as-a-Judge-Hard，包含与人类偏好不一致的回答以及幻觉实例。此外，我们讨论了 MLLM 在判定中的局限，如自我中心偏差、位置偏差、长度偏差与幻觉，并证明引入 CoT（Wei 等, 2022）与视觉专家系统可以有效缓解其中部分偏差。

**EN** Take-Aways.

**ZH** 要点。

**EN** We evaluate the judgment performance of 11 MLLMs across 14 datasets under three settings: score evaluation, pair comparison, and batch ranking. Our findings reveal several key insights. First, while MLLMs demonstrate proficiency in aligning with human preferences in pair comparison tasks, they require further improvement in score evaluation and batch ranking, particularly in reasoning tasks. Secondly, GPT-4V consistently outperforms other models across all tasks and settings.

**ZH** 我们在 14 个数据集、三种设定（评分评测、成对比较与批量排序）下评估了 11 个 MLLM 的判定表现，得到若干关键认识。首先，MLLM 在成对比较任务中展现出与人类偏好对齐的能力，但在评分评测与批量排序上仍需改进，在推理类任务中尤为明显。其次，GPT-4V 在所有任务与设定下都一致地优于其他模型。

**EN** Finally, the presence of hallucinations, biases, and inconsistent judgments in MLLMs highlights significant challenges that must be addressed for these models to become a viable alternative to traditional human evaluations.

**ZH** 最后，MLLM 中存在的幻觉、偏差与不一致判定凸显出若干重大挑战；要使这些模型成为传统人工评估的可行替代，这些问题必须得到解决。

**EN** To summarize, our work provides three key contributions:

**ZH** 总而言之，我们的工作提供三项关键贡献：

**EN** • A Benchmark. We are the first to develop a comprehensive benchmark MLLM-as-a-Judge in multimodal domains, with human annotations to assess the judging capability of MLLMs in tasks of Scoring Evaluation, Pair Comparison and Batch Ranking.

**ZH** • 一个基准。我们率先在多模态领域构建了综合性基准 MLLM-as-a-Judge，并配以人工标注，用以评估 MLLM 在评分评测、成对比较与批量排序任务中的判定能力。

**EN** • Two Datasets. We curate two human preference datasets: MLLM-as-a-Judge-HQ, which contains high-quality questions, and MLLM-as-a-Judge-HARD, which includes instances of hallucination. These datasets can serve as rigorous testing grounds to facilitate the development of MLLMs in aligning human preferences.

**ZH** • 两个数据集。我们整理了两个人类偏好数据集：MLLM-as-a-Judge-HQ 包含高质量的问题，MLLM-as-a-Judge-HARD 包含幻觉实例。这两个数据集可作为严格的试验场，推动 MLLM 在对齐人类偏好上的发展。

**EN** • Findings and Implications. Our evaluation of mainstream MLLMs reveals that while MLLMs exhibit alignment with human judgments in Pair Comparison, notable discrepancies can be found in Scoring Evaluation and Batch Ranking. Furthermore, our findings reveal that MLLMs exhibit a range of biases and hallucinations, along with inconsistent judgments during the evaluation process, representing significant hurdles in establishing MLLMs as reliable judges.

**ZH** • 发现与启示。对主流 MLLM 的评测表明，尽管 MLLM 在成对比较上与人类判断相一致，在评分评测与批量排序上却存在显著差异。此外，我们的发现揭示 MLLM 在评测过程中表现出一系列偏差与幻觉，并伴随不一致的判定，这些构成了把 MLLM 确立为可靠裁判的重大障碍。

<!-- [原子块 · img]  -->

**EN** Figure 2: An overview of MLLM-as-a-Judge.

**ZH** 图 2：MLLM-as-a-Judge 概览。

**EN** 2 MLLM-as-a-Judge: A Benchmark to Assess Vision-Language Judging Ability

**ZH** 2 MLLM-as-a-Judge：一个评估视觉—语言判定能力的基准

**EN** Table 1: The statistics of responses in different steps for MLLM judging. In Step 3, under the w.o. vision input settings, we sample 10% from the original data and mainly proceed with GPT-4V and Gemini. We only list the amount of judgments generated by four models here. M-I: Image-Instruction.

**ZH** 表 1：MLLM 判定各步骤中回答的统计。在步骤 3 的无视觉输入设定下，我们从原始数据中抽取 10% 并主要使用 GPT-4V 与 Gemini 推进。此处仅列出四个模型生成的判定数量。M-I：图像—指令。

<!-- [原子块 · table] Step Setting Input Num. Output Num. 1 / Image 4,144 M-I Pairs 4,400 Instruction 4,414 2 / M-I Pairs 3,300 MLLMs 17,096 3 w. Vision Input Batch 1,470 Gemini 1,340 GPT-4V 1,454 Qwen-VL-Max 1,458 LLaVA 1 -->

**EN** Figure 2 shows an overview of our proposed MLLM-as-a-Judge, consisting of three steps: 1) image-instruction pair collection, 2) MLLM response collection, and 3) comparison with human annotation. Initially, we collect a dataset ⟦SLOT_0⟧, containing pairs of images ⟦SLOT_1⟧ and their corresponding instructions ⟦SLOT_2⟧ sourced from 10 diverse domains (e.g., math, chart, diffusion), ensuring comprehensive coverage for a wide array of downstream tasks. Subsequently, each pair ⟦SLOT_3⟧ is processed through several MLLMs, generating a set of responses ⟦SLOT_4⟧ for each pair. This process contributes to the formation of the dataset of image-instruction-responses pairs, denoted as ⟦SLOT_5⟧. Finally, the dataset ⟦SLOT_6⟧ is partitioned into three distinct subsets to facilitate diverse task evaluations: ⟦SLOT_7⟧ for Scoring Evaluation, ⟦SLOT_8⟧ for Pair Comparison, and ⟦SLOT_9⟧ for Batch Ranking. Each subset will be employed for specific judging tasks, with each of them being configured as follows.

**ZH** 图 2 展示了我们提出的 MLLM-as-a-Judge 的概览，它由三个步骤组成：1) 图像—指令对采集；2) MLLM 回答采集；3) 与人工标注的比对。首先，我们采集数据集 ⟦SLOT_0⟧，其中包含来自 10 个不同领域（例如数学、图表、扩散）的图像 ⟦SLOT_1⟧ 及其对应指令 ⟦SLOT_2⟧，以确保对各类下游任务的全面覆盖。随后，每一对 ⟦SLOT_3⟧ 被送入若干 MLLM 处理，为每一对生成一组回答 ⟦SLOT_4⟧。这一过程促成了图像—指令—回答对数据集 ⟦SLOT_5⟧ 的形成。最后，数据集 ⟦SLOT_6⟧ 被划分为三个互不相交的子集，以支持不同的任务评测：⟦SLOT_7⟧ 用于评分评测，⟦SLOT_8⟧ 用于成对比较，⟦SLOT_9⟧ 用于批量排序。每个子集将用于特定的判定任务，其配置如下。

**EN** • Scoring Evaluation: Each individual response is evaluated on a scale from 1 to 5, with the specific criteria for this rating system detailed in Appendix F.

**ZH** • 评分评测：对每条单独的回答在 1 到 5 的量表上评分，该评分体系的具体准则详见附录 F。

**EN** • Pair Comparison: It involves a direct comparison between two responses, culminating in the identification of the superior one. Following the principles outlined by (Deutsch et al., 2023), a tie option is incorporated to ensure a more equitable assessment.

**ZH** • 成对比较：对两条回答进行直接比较，最终指出更优的一条。遵循（Deutsch 等, 2023）提出的原则，我们纳入了平局选项，以确保评估更为公平。

**EN** • Batch Ranking: The responses are systematically arranged in descending order of quality based on a given instruction, without any tie option.

**ZH** • 批量排序：依据给定指令按质量降序对回答进行系统排列，不设平局选项。

**EN** 2.1 Step 1: Image-Instruction Pair Collection

**ZH** 2.1 步骤 1：图像—指令对采集

**EN** We meticulously curate a dataset consisting of 4,414 image-text pairs, gathered from a variety of downstream task datasets, as detailed in Table 8 in Appendix B. These pairs are carefully tailored into image-instruction pairs to suit a free-form response format. To illustrate, within the domain of diffusion tasks, our dataset incorporated pairs challenging models to adeptly recognize and articulate connections between provided images and user-specified keywords.

**ZH** 我们精心整理了一个包含 4,414 个图像—文本对的数据集，采集自多种下游任务数据集，详见附录 B 的表 8。这些对被仔细改写为图像—指令对，以适应自由形式的回答格式。举例来说，在扩散任务领域，我们的数据集纳入了要求模型娴熟识别并阐述所给图像与用户指定关键词之间联系的图像—指令对。

**EN** 2.2 Step 2: MLLM Response Collection

**ZH** 2.2 步骤 2：MLLM 回答采集

**EN** We employ six widely-used MLLMs – GPT-4V (OpenAI, 2023), Gemini (GeminiTeam, 2023), LLaVA (Liu et al., 2023d), Qwen-VL-Max (Bai et al., 2023a), LLaVA-1.6-34b (Liu et al., 2023d), and CogVLM (Wang et al., 2023c) – to generate responses based on the image-instruction pairs, obtaining approximately 17,000 responses. Responses that are either too brief or non-compliant with security regulations (e.g., “I’m sorry, but I cannot assist with this request”) from GPT-4V and Gemini are excluded. The number of responses and the length distributions for different MLLMs are shown in Table 1 and Figure 3, respectively. We show specific hyper-parameter settings in Appendix B.2. Besides, we segment these responses into three non-overlapping groups, to prevent response overlap.

**ZH** 我们采用六个被广泛使用的 MLLM——GPT-4V（OpenAI, 2023）、Gemini（GeminiTeam, 2023）、LLaVA（Liu 等, 2023d）、Qwen-VL-Max（Bai 等, 2023a）、LLaVA-1.6-34b（Liu 等, 2023d）与 CogVLM（Wang 等, 2023c）——基于图像—指令对生成回答，共获得约 17,000 条回答。来自 GPT-4V 与 Gemini 的回答中，过短或不符合安全规范（例如「抱歉，我无法协助处理这一请求」）的部分被剔除。各 MLLM 的回答数量与长度分布分别见表 1 与图 3。具体超参数设置见附录 B.2。此外，我们把这些回答切分为三个互不重叠的分组，以避免回答重叠。

<!-- [原子块 · object]  -->

**EN** Figure 3: Length distribution in responses for different MLLMs. Horizontal axis: length; Vertical axis: density.

**ZH** 图 3：不同 MLLM 回答的长度分布。横轴：长度；纵轴：密度。

**EN** 2.3 Step 3: Comparison with Human Annotations

**ZH** 2.3 步骤 3：与人工标注比对

**EN** The annotation is conducted by 6 authors of this paper independently. These annotators are proficient in this domain, with different genders, ages, and educational backgrounds to ensure diversity (Sun et al., 2020). They are required to give objective judgments without considering answer lengths, and certain names or positions of the response to minimize human bias. More details are referred to Appendix E.

**ZH** 标注由本文 6 位作者独立完成。这些标注者熟悉本领域，且性别、年龄与教育背景各异，以确保多样性（Sun 等, 2020）。他们被要求在不考虑回答长度、以及回答中特定名称或位置的前提下给出客观判定，以尽量降低人为偏差。更多细节见附录 E。

**EN** Table 2: The overall performance of different MLLMs in judging, compared with human annotations on different datasets. We sample all the data three times and took the average to mitigate the casualty. w. and w.o. tie represents tie and non-tie situations respectively. We omit Gemini’s results on the diffusion task for its challenges in processing AI-generated images. All presented data of Pearson similarity exhibit a ⟦SLOT_10⟧-value below 0.05, indicating a statistically significant level of confidence. Please refer to the Appendix D.1 for more results.

**ZH** 表 2：不同 MLLM 在判定上的总体表现，与各数据集上的人工标注相对照。我们对全部数据采样三次并取平均，以降低偶然性。w. 与 w.o. tie 分别表示有平局与无平局的情形。因 Gemini 在处理 AI 生成图像上存在困难，我们略去其在扩散任务上的结果。所有给出的皮尔逊相似度数据的 ⟦SLOT_10⟧ 值均低于 0.05，表明具有统计学显著水平的置信度。更多结果见附录 D.1。

<!-- [原子块 · table] Settings MLLM COCO C.C. Diff. Graphics Math Text WIT Chart VisIT CC-3M M2W SciQA Aes MM-Vet Ave. Score ( ↑ \uparrow ) LLaVA-1.5-13b 0.247 0.227 0.060 0.242 0.093 0.245 0.109 0.237 0.177 0.071 0.424 0. -->

**EN** 3 Experiment Settings

**ZH** 3 实验设置

**EN** 3.1 Settings of MLLM-as-a-Judge

**ZH** 3.1 MLLM-as-a-Judge 的设置

**EN** We evaluate the judging performance of eleven leading MLLMs – GPT-4V (OpenAI, 2023), Gemini-Pro-Vision-1.0 (GeminiTeam, 2023), LLaVA-1.5-13b, LLaVA-1.6-7b/13b/34b (Liu et al., 2023d), Qwen-VL-Plus/Max (Bai et al., 2023a) and CogVLM (Wang et al., 2023c) – across three distinct evaluation settings. Adapting the “Analyze-then-Judge” paradigm from Chiang & Lee (2023b), which is a one-step CoT approach (Wei et al., 2022), we first ask MLLMs to analyze responses and then provide a judgment based on their analysis. However, due to capability limitations to perform the “Analyze-then-Judge” setting for LLaVA and CogVLM, we prompt them to directly output their judgment. We also evaluate whether multi-step CoT will enhance the performance of MLLM serving as a judge.

**ZH** 我们在三种不同的评测设定下评估十一个领先 MLLM 的判定表现——GPT-4V（OpenAI, 2023）、Gemini-Pro-Vision-1.0（GeminiTeam, 2023）、LLaVA-1.5-13b、LLaVA-1.6-7b/13b/34b（Liu 等, 2023d）、Qwen-VL-Plus/Max（Bai 等, 2023a）与 CogVLM（Wang 等, 2023c）。我们沿用 Chiang & Lee（2023b）的「先分析后判定」（Analyze-then-Judge）范式，这是一种单步 CoT 方法（Wei 等, 2022）：先让 MLLM 分析回答，再基于其分析给出判定。然而，由于 LLaVA 与 CogVLM 在能力上难以执行「先分析后判定」的设定，我们提示它们直接输出判定。我们也评测了多步 CoT 是否会提升 MLLM 作为裁判的表现。

**EN** Furthermore, to extensively explore MLLMs judging capabilities, we conduct experiments on various settings, including scenarios without vision input, replacing vision input with a detailed description generated by GPT-4V as a vision expert, and employing multi-step CoT. Considering that the first two settings do not involve image inputs, we also include tests on the latest GPT-4 (OpenAI, 2023) Gemini (GeminiTeam, 2023), LLaMA-2-70b (Touvron et al., 2023), and Mixtral-8x7b (Jiang et al., 2024) to assess whether LLMs can effectively perform judging tasks without vision perception. Comprehensive details of these experimental setups are available in Appendix C, and the prompts can be found in Appendix F.

**ZH** 此外，为充分探索 MLLM 的判定能力，我们在多种设定下开展实验，包括无视觉输入的情形、把视觉输入替换为由 GPT-4V 作为视觉专家生成的详细描述，以及采用多步 CoT。考虑到前两种设定不涉及图像输入，我们还纳入了对最新的 GPT-4（OpenAI, 2023）、Gemini（GeminiTeam, 2023）、LLaMA-2-70b（Touvron 等, 2023）与 Mixtral-8x7b（Jiang 等, 2024）的测试，以评估 LLM 能否在没有视觉感知的情况下有效完成判定任务。这些实验设置的完整细节见附录 C，提示词见附录 F。

**EN** 3.2 Judging Metrics

**ZH** 3.2 判定指标

**EN** After collecting responses from MLLM judgments, we quantify their alignment with human annotations across three settings, employing distinct metrics as follows:

**ZH** 在收集到 MLLM 的判定回答后，我们在三种设定下用如下不同的指标量化它们与人工标注的一致程度：

**EN** ⟦SLOT_11⟧ Scoring Evaluation: Following LLM-as-a-Judge (Zheng et al., 2023b), we compute the Pearson similarity (Lee Rodgers & Nicewander, 1988) between the MLLMs’ judgments and human ratings across different sub-datasets.

**ZH** ⟦SLOT_11⟧ 评分评测：沿用 LLM-as-a-Judge（Zheng 等, 2023b）的做法，我们在各子数据集上计算 MLLM 判定与人类评分之间的皮尔逊相似度（Lee Rodgers & Nicewander, 1988）。

**EN** ⟦SLOT_12⟧ Pair Comparison: We assess the similarity between the MLLM judgments and human decisions using accuracy, F1-score (Goutte & Gaussier, 2005), and recall (Goutte & Gaussier, 2005) to assess the judging abilities of models.

**ZH** ⟦SLOT_12⟧ 成对比较：我们用准确率、F1 分数（Goutte & Gaussier, 2005）与召回率（Goutte & Gaussier, 2005）度量 MLLM 判定与人类决策之间的相似度，以评估模型的判定能力。

**EN** ⟦SLOT_13⟧ Batch Evaluation: We consolidate the ranking results into a singular sequence and employ the Normalized Levenshtein distance (Levenshtein et al., 1966) to evaluate the similarity between judgments from MLLMs and human annotation.

**ZH** ⟦SLOT_13⟧ 批量评测：我们把排序结果归并为单一序列，并用归一化 Levenshtein 距离（Levenshtein 等, 1966）评估 MLLM 判定与人工标注之间的相似度。

**EN** 3.3 Human Agreement in MLLM Judgment

**ZH** 3.3 MLLM 判定中的人类认同度

**EN** Apart from traditional metrics for similarity assessment between judgments from MLLMs and humans, we further evaluate the judgments provided by MLLMs to uncover latent bias and hallucination in 10 datasets. We also invite human annotators for further validation, focusing on the following aspects:

**ZH** 除用于度量 MLLM 与人类判定相似度的传统指标之外，我们进一步评估 MLLM 给出的判定，以揭示 10 个数据集中的潜在偏差与幻觉。我们还邀请人工标注者做进一步验证，重点关注以下方面：

**EN** ⟦SLOT_14⟧ Human Agreement: This involves a simple ‘yes’ or ‘no’ response to assess agreement with the MLLM judgments. While some judgments might appear reasonable, they may still be considered incorrect due to unique human perspectives. Hence, we conduct experiments on human agreement to address situations that traditional metrics may not adequately capture.

**ZH** ⟦SLOT_14⟧ 人类认同度：以简单的「是」或「否」回答来评估是否认同 MLLM 的判定。某些判定看似合理，却可能因人类视角的独特性而被判为不正确。因此我们开展人类认同度实验，以处理传统指标可能无法充分覆盖的情形。

**EN** ⟦SLOT_15⟧ Analysis Grading: Each MLLM analysis is assigned a score from 1 to 5, considering relevance, accuracy, creativity, and response granularity, detailed in Appendix F.

**ZH** ⟦SLOT_15⟧ 分析评分：对每条 MLLM 分析在 1 到 5 分之间打分，考量其相关性、准确性、创造性与回答粒度，详见附录 F。

**EN** ⟦SLOT_16⟧ Hallucination Detection: Given the propensity for hallucination issues in the complex reasoning chains and long-term vision-language contexts of MLLMs, we task human annotators with identifying any hallucinations in the analyses of MLLM judgments, adhering to established definitions of vision and language hallucination (Sun et al., 2024).

**ZH** ⟦SLOT_16⟧ 幻觉检测：鉴于 MLLM 在复杂推理链与长程视觉—语言语境中容易出现幻觉问题，我们让人工标注者识别 MLLM 判定分析中的任何幻觉，并遵循视觉与语言幻觉的既有定义（Sun 等, 2024）。

**EN** 4 Empirical Results and Analysis

**ZH** 4 实证结果与分析

**EN** Table 3: Human agreement percentage on MLLM-as-a-Judge in 10 datasets. Each judgment is independently reviewed three times by different annotators and consensus results are recorded. Gemini failed in diffusion tasks and its results are omitted.

**ZH** 表 3：10 个数据集上 MLLM-as-a-Judge 的人类认同度百分比。每条判定由不同标注者独立复核三次，并记录一致后的结果。Gemini 在扩散任务上失败，其结果被略去。

<!-- [原子块 · table] Settings MLLM COCO C.C. Diffusion Graphics Math Text WIT Chart VisIT CC-3M Average Score ( ↑ \uparrow ) Gemini 0.783 0.739 - 0.618 0.536 0.621 0.749 0.630 0.712 0.702 0.677 GPT-4V 0.799 0.725 0.506 0. -->

<!-- [原子块 · object]  -->

**EN** Figure 4: Pair Comparison density (Left) and Scoring Evaluation density (Right) of different MLLMs judgments and human annotations.

**ZH** 图 4：不同 MLLM 判定与人工标注的成对比较密度（左）与评分评测密度（右）。

**EN** 4.1 MLLM Judgment vs Human Annotation

**ZH** 4.1 MLLM 判定与人工标注的对比

**EN** As shown in Figure 1 and Table 3, judgments made by GPT-4V are closer to human annotations among all settings, while Gemini is far different, with LLaVA, CogVLM and Qwen-VL-Max are even worse. Overall, MLLM judgments perform better on Pair Comparison, while falling short in Scoring Evaluation and Batch Ranking, showing a huge gap between the model and human preferences. Under the “Analyze-then-Judge” setting, GPT-4V prefers to give a longer judge in all settings, convincing its ability to reason on long-term text.

**ZH** 如图 1 与表 3 所示，在所有设定下 GPT-4V 所作的判定都更接近人工标注，而 Gemini 相差甚远，LLaVA、CogVLM 与 Qwen-VL-Max 则更差。总体而言，MLLM 的判定在成对比较上表现更好，在评分评测与批量排序上则有欠缺，显示出模型与人类偏好之间存在巨大差距。在「先分析后判定」设定下，GPT-4V 倾向于在所有设定中给出更长的判定，印证了其对长文本进行推理的能力。

**EN** ⟦SLOT_17⟧ Scoring Evaluation: GPT-4V demonstrates the highest similarity to human scoring with a similarity score of 0.490. In contrast, Gemini achieves only 0.304, with LLaVA and CogVLM scoring even lower. This discrepancy is mainly due to Gemini’s tendency to assign scores around 4 points as depicted in Figure 4, seldom giving 1 or 2 points. LLaVA and CogVLM show a pattern similar to Gemini, predominantly assigning scores around 4 points. We attribute this to a ‘High-Score’ Bias, akin to the ‘Yes/No’ bias identified by Liu et al. (2023a), which may result from an imbalance in positive and negative judging instructions in their training data (Liu et al., 2023b), severely limits their ability to provide just and varied scores in scoring settings. In comparison, GPT-4V’s scores are more evenly distributed and align closely with human preferences.

**ZH** ⟦SLOT_17⟧ 评分评测：GPT-4V 与人类评分的相似度最高，达到 0.490。相比之下，Gemini 仅为 0.304，LLaVA 与 CogVLM 的得分更低。这一差异主要源于 Gemini 倾向于给出 4 分左右的分数（如图 4 所示），极少给出 1 分或 2 分。LLaVA 与 CogVLM 呈现出与 Gemini 相似的模式，主要给出 4 分左右的分数。我们把这归因于一种「高分」偏差，类似于 Liu 等（2023a）所识别的「是/否」偏差，它可能源自其训练数据中正负判定指令的不平衡（Liu 等, 2023b），严重限制了它们在评分设定下给出公正且多样分数的能力。相较之下，GPT-4V 的分数分布更均匀，与人类偏好契合得更紧密。

**EN** ⟦SLOT_18⟧ Pair Comparison: As illustrated in Figure 4, GPT-4V outshines other MLLMs in pair comparison tasks, achieving 0.636 in tie settings and 0.773 in non-tie settings, surpassing 0.8 in many datasets, which indicate a strong alignment with human preferences. Gemini, LLaVA, and CogVLM show a marked preference for declaring a clear winner, possibly due to a lack of tie situations in their training, leading to biased judgments. It’s also interesting that the frequency of ties given by GPT-4V closely mirrors that of human judges, suggesting similar thresholds for tie decisions.

**ZH** ⟦SLOT_18⟧ 成对比较：如图 4 所示，GPT-4V 在成对比较任务中胜过其他 MLLM，在有平局设定下达到 0.636、在无平局设定下达到 0.773，在多个数据集上超过 0.8，表明其与人类偏好高度一致。Gemini、LLaVA 与 CogVLM 明显倾向于判定出明确的胜者，这可能是因为它们的训练中缺少平局情形，导致判定带偏。同样有意思的是，GPT-4V 给出平局的频率与人类裁判高度接近，说明二者判定平局的阈值相似。

**EN** ⟦SLOT_19⟧ Batch Ranking: GPT-4V aligns more closely with human ranking results, indicating a significant lead with a mean Levenshtein Distance of 0.361. However, there is still substantial room for improvement in this task for all MLLMs. Notably, CogVLM is unable to provide a full ranking in this context, offering only the top choice; so it was excluded from this comparison; LLaVA also exhibits position bias influenced by prompt structure, often replicating judgments seen in example prompts, which complicates its ability to produce fair judgments.

**ZH** ⟦SLOT_19⟧ 批量排序：GPT-4V 与人类排序结果契合得更紧密，以 0.361 的平均 Levenshtein 距离显示出显著领先。然而，所有 MLLM 在该任务上都仍有很大的改进空间。值得注意的是，CogVLM 在此情境下无法给出完整排序，只给出首选，因此被排除在该比较之外；LLaVA 还表现出受提示结构影响的位置偏差，常常复现示例提示中见过的判定，这使其难以做出公平判定。

**EN** Table 4: Consistency comparisons of GPT-4V and Gemini in 10 datasets. Average means weighted average for consistency times, “MCC” stands for “Majority Consistency Criterion”, which deems responses consistent if over half of them are identical across our 6 repetitions of experiments.

**ZH** 表 4：GPT-4V 与 Gemini 在 10 个数据集上的一致性比较。Average 指一致性次数的加权平均，「MCC」代表「多数一致性准则」（Majority Consistency Criterion），即在我们的 6 次重复实验中，若超过半数的回答完全相同，则视为一致。

<!-- [原子块 · table] MLLM Score Pair Batch Average MCC Average MCC Average MCC Gemini 0.531 0.054 0.781 0.547 0.629 0.338 GPT-4V 0.796 0.611 0.836 0.675 0.679 0.418 -->

**EN** 4.2 MLLM Judging Consistency

**ZH** 4.2 MLLM 判定的一致性

**EN** To be a reliable judge, consistent decision-making across repeated evaluations of the same query is crucial. For this purpose, we conduct six repeated tests with MLLM judgments and calculated the weighted average consistency scores and Majority Consistency Criterion ratios for GPT-4V and Gemini, as shown in Table 4 and Figure 5. Despite a higher temperature setting, GPT-4V substantially outperforms Gemini across all tasks. Particularly in Pair Comparison, GPT-4V achieves a higher consistency score of 0.675, but it encounters difficulties in maintaining similar levels of consistency in Scoring and Batch Ranking tasks, with scores dropping to 0.611 and 0.418, indicating the challenge of producing qualified and convincing judgments.

**ZH** 要成为可靠的裁判，对同一查询在重复评测中作出一致的决策至关重要。为此，我们对 MLLM 的判定做了六次重复测试，并计算了 GPT-4V 与 Gemini 的加权平均一致性分数以及多数一致性准则比例，如表 4 与图 5 所示。尽管温度设置更高，GPT-4V 在所有任务上都大幅优于 Gemini。尤其在成对比较中，GPT-4V 取得 0.675 的较高一致性分数，但在评分与批量排序任务上难以维持相近水平，分数降至 0.611 与 0.418，说明产出合格且有说服力的判定具有挑战性。

<!-- [原子块 · object]  -->

**EN** Figure 5: Consistency checking on 6 repetitions of experiments on GPT-4V (Left) and Gemini (Right). GPT-4V outperforms Gemini with a relatively higher ratio for high consistency.

**ZH** 图 5：GPT-4V（左）与 Gemini（右）在 6 次重复实验下的一致性检验。GPT-4V 优于 Gemini，其高一致性比例相对更高。

**EN** Table 5: Results of GPT-4V and Gemini-Pro acting as a judge with a 3-step CoT approach in a selected subset.

**ZH** 表 5：GPT-4V 与 Gemini-Pro 在选定子集上以 3 步 CoT 方法充当裁判的结果。

<!-- [原子块 · table] Settings MLLM COCO C.C. Diffusion Graphics Math Text WIT Chart VisIT CC-3M Ave. Score ( ↑ \uparrow ) GPT-4V 0.454 0.507 0.458 0.645 0.606 0.624 0.579 0.645 0.620 0.431 0.557 GPT-4V (+CoT) 0.246 0.165  -->

**EN** 4.3 Human Agreement

**ZH** 4.3 人类认同度

**EN** Our manual evaluation of MLLMs on agreement and scoring, revealed notable findings. Table 3 shows that GPT-4V achieved around 70% human agreement across all settings, excelling in the Pair Comparison task with 79.3% agreement. Specifically, GPT-4V reached 78% in human agreement for Pair Comparison, with Gemini close at 72%, indicating strong performance in most sample pairs and supporting the idea that large models excel in pairwise distinctions (Zheng et al., 2023b), though improvements are needed in other judging settings.

**ZH** 我们对 MLLM 在认同度与评分上的手工评测揭示了若干值得注意的发现。表 3 显示，GPT-4V 在所有设定下取得约 70% 的人类认同度，在成对比较任务上以 79.3% 的认同度表现最佳。具体地，GPT-4V 在成对比较上达到 78% 的人类认同度，Gemini 以 72% 紧随其后，表明大模型在多数样本对上表现强劲，支持了大模型擅长成对区分的观点（Zheng 等, 2023b），尽管在其他判定设定上仍需改进。

**EN** In Scoring Evaluation, GPT-4V achieves a 70% human agreement rate, peaking at 79.9% in MS-COCO, while Gemini averaged 67.7%. To assess the consistency of MLLM judging quality across multiple responses to a single image-instruction pair, we use Mean Absolute Deviation (MAD) metric to measure the average absolute variance between individual scores and the mean. Figure 18 shows that GPT-4V exhibits lower variation in quality assessments, indicating more consistent and reliable judgment compared to Gemini. However, in Batch Ranking, both models exhibited decreased alignment with human judgments, especially in Maths and graphic information processing, suggesting that models may lack the capabilities to fully comprehend user instructions, leading to less reliable judgments.

**ZH** 在评分评测中，GPT-4V 达到 70% 的人类认同率，在 MS-COCO 上峰值达 79.9%，而 Gemini 平均为 67.7%。为评估 MLLM 对同一图像—指令对的多个回答在判定质量上的一致性，我们用平均绝对偏差（MAD）指标来度量各分数与均值之间的平均绝对离散程度。图 18 显示，GPT-4V 在质量评估上的变异更小，说明相比 Gemini 其判定更一致、更可靠。然而在批量排序中，两个模型与人类判断的契合度都下降，在数学与图形信息处理上尤为明显，这表明模型可能缺乏充分理解用户指令的能力，导致判定可靠性下降。

**EN** 4.4 Multi-steps CoT Do Not Enhance Performance

**ZH** 4.4 多步 CoT 并未提升表现

**EN** We have conducted additional tests using GPT-4V and Gemini with a 3-step CoT approach for judging, as detailed in Table 5. Our analysis reveals that while employing CoT with additional steps markedly reduces hallucinations in judgments, it does not align more closely with human preferences. On numerous datasets, this approach even diminishes judging performance. Specifically, Gemini’s effectiveness drops more drastically. With 3-step CoT, there is an increased likelihood that the judgment will be disturbed by its understanding of the figure and its own responses to the instruction, thereby undermining its final judgment if hallucinations exist in the previous chain.

**ZH** 我们使用 GPT-4V 与 Gemini 以 3 步 CoT 方法做判定，进行了额外测试，详见表 5。分析表明，尽管采用更多步骤的 CoT 显著减少了判定中的幻觉，它并未与人类偏好更加契合。在不少数据集上，该方法甚至降低了判定表现，其中 Gemini 的效果下降尤为剧烈。使用 3 步 CoT 时，判定更容易受到其对图像的理解以及自身对指令的回答的干扰；若前面的链条中存在幻觉，最终判定就会被动摇。

**EN** 4.5 Vision Perception Benefits MLLM Judging

**ZH** 4.5 视觉感知有助于 MLLM 判定

**EN** We explore the feasibility of using LLMs for judging text-based responses without directly analyzing the original images. This involves two approaches: omitting vision information entirely and providing a detailed description of the picture. We choose LLaMA-70b, Mixtral8x7b-v0.1 and GPT-3.5 to provide descriptions. Surprisingly, as illustrated in Table 6, we find that LLMs’ performance in multimodal judging tasks significantly improve with picture descriptions, achieving a Pearson similarity of 0.435 in Scoring Evaluation tasks, markedly outperformed judgments made without any vision perception. Notably, in no-tie Pair Comparison, MLLMs with detailed vision descriptions even exceed the standard performance of MLLMs in judging. This suggests that MLLMs may lack certain human-like judging capabilities, while LLMs can be potential judges for multimodal tasks when provided with comprehensive task-related descriptions.

**ZH** 我们探索了在不直接分析原始图像的情况下，用 LLM 判定基于文本的回答是否可行。这包括两种做法：完全省略视觉信息，以及提供图像的详细描述。我们选用 LLaMA-70b、Mixtral8x7b-v0.1 与 GPT-3.5 来提供描述。令人意外的是，如表 6 所示，我们发现 LLM 在多模态判定任务上的表现随图像描述的加入而显著提升，在评分评测任务上取得 0.435 的皮尔逊相似度，明显优于在毫无视觉感知下作出的判定。值得注意的是，在无平局的成对比较中，带有详细视觉描述的 MLLM 甚至超过了 MLLM 判定的标准表现。这说明 MLLM 可能缺乏某些类人的判定能力，而在获得与任务相关的完备描述时，LLM 有望成为多模态任务的裁判。

**EN** Table 6: How vision perception significantly enhances multimodal judging performance in traditional LLM-as-a-Judge setting, slightly outperforming MLLMs in judging. Vision Exp. stands for judging with a detailed image description.

**ZH** 表 6：视觉感知如何在传统 LLM-as-a-Judge 设定下显著提升多模态判定表现，并略微优于 MLLM 的判定。Vision Exp. 表示借助详细图像描述进行判定。

<!-- [原子块 · table] MLLM Settings Score ( ↑ \uparrow ) Pair ( ↑ \uparrow ) Batch ( ↓ \downarrow ) Pearson w. Tie w.o. Tie Edit Dis. LLaMA2-70b Vision Exp 0.060 0.404 0.550 0.643 No Vision 0.126 0.374 0.537 0.583 Mixtral- -->

**EN** 4.6 Bias and Hallucination

**ZH** 4.6 偏差与幻觉

<!-- [原子块 · object]  -->

**EN** Figure 6: Length bias in 10 datasets. The horizontal axis represents length, and the vertical axis represents density.

**ZH** 图 6：10 个数据集上的长度偏差。横轴表示长度，纵轴表示密度。

<!-- [原子块 · object]  -->

**EN** Figure 7: Length Bias in Different MLLM judgments.

**ZH** 图 7：不同 MLLM 判定中的长度偏差。

**EN** Egocentric Bias.

**ZH** 自我中心偏差。

**EN** Models tend to assign higher scores to their own responses while scoring others lower (Zheng et al., 2023b; Li et al., 2024). In Figures 19 and 20, GPT-4V exhibits a slight degree of Egocentricity. Conversely, Gemini maintains a uniform scoring distribution across different sources, demonstrating a more equitable approach to judgment. In contrast, GPT-4V shows self-preference, aligning its judgments with its predefined ethical guidelines. For example, GPT-4V consistently emphasizes privacy preservation, leading to higher scores for privacy-related questions based on its own metrics. Despite efforts in prompt engineering to ensure neutrality, these models still rely on judgment criteria set during post-alignment training (Ouyang et al., 2022). This bias can result in judgments that deviate from human preferences, highlighting the complexity of aligning MLLM judgments with humans’.

**ZH** 模型倾向于给自己的回答打高分，而给其他模型的回答打低分（Zheng 等, 2023b；Li 等, 2024）。在图 19 与图 20 中，GPT-4V 表现出轻微程度的自我中心倾向。相反，Gemini 在不同来源上保持均匀的评分分布，展现出更公平的判定方式。相比之下，GPT-4V 表现出自我偏好，使其判定与自身预设的伦理准则相一致。例如，GPT-4V 一贯强调隐私保护，因而依据自身标准会给隐私相关问题打更高分。尽管我们在提示工程上作出努力以确保中立，这些模型仍然依赖后对齐训练阶段设定的判定标准（Ouyang 等, 2022）。这种偏差可能导致判定偏离人类偏好，凸显了把 MLLM 判定与人类对齐的复杂性。

**EN** Position Bias.

**ZH** 位置偏差。

**EN** Model consistently favor answers in specific positions, often influenced by training data that typically places correct responses at the beginning or end of prompts (Liu et al., 2023e). Figure 4 illustrates bias in LLaVA and CogVLM during Pair Comparison tasks, where they consistently prefer answers in a specific position. This bias likely arises from their limited ability to follow complex instructions, leading them to be influenced by prompt structure. For example, if a Batch Ranking prompt includes a sequence like ‘ABCD’, LLaVA replicates this sequence in 88.2% of responses, significantly more than other sequences. However, this bias can be reduced by introducing multiple examples, suggesting that prompts with more examples can better direct these models to follow instructions accurately.

**ZH** 模型一贯偏爱处于特定位置的答案，这往往受训练数据影响——正确回答通常被放在提示的开头或结尾（Liu 等, 2023e）。图 4 展示了 LLaVA 与 CogVLM 在成对比较任务中的偏差：它们始终偏爱某个特定位置的答案。这一偏差很可能源于它们遵循复杂指令的能力有限，因而受提示结构左右。例如，若批量排序提示中包含形如「ABCD」的序列，LLaVA 会在 88.2% 的回答中复现该序列，显著高于其他序列。不过，引入多个示例可以降低这一偏差，说明含更多示例的提示能更好地引导这些模型准确遵循指令。

**EN** Length Bias.

**ZH** 长度偏差。

**EN** Models tend to prefer longer answers over concise but correct ones (Li et al., 2024), also known as verbosity bias (Zheng et al., 2023b). Figure 6 shows that both GPT-4V and Gemini assign higher scores to longer content. We conducted an expanded scoring experiment using GPT-4 (OpenAI, 2023) without vision, increasing the semantic length of answers without changing their original intent. In Figure 7, we observe noticeable score increases, with GPT-4V and Gemini showing average gains of 0.6 and 0.75 points, respectively. These results suggest that MLLMs may favor longer text for higher scores.

**ZH** 模型倾向于偏爱更长的答案，而非简洁但正确的答案（Li 等, 2024），这也被称为冗长偏差（verbosity bias）（Zheng 等, 2023b）。图 6 显示，GPT-4V 与 Gemini 都给更长的内容打更高分。我们用不带视觉的 GPT-4（OpenAI, 2023）开展了一项扩展评分实验，在保持原意不变的前提下增加回答的语义长度。在图 7 中，我们观察到分数明显上升，GPT-4V 与 Gemini 的平均增幅分别为 0.6 与 0.75 分。这些结果表明，MLLM 可能偏爱更长的文本并给出更高分数。

**EN** Hallucination Detection and Mitigation. We observe a higher frequency of hallucinations in Batch Ranking, compared to Pair Comparison and Scoring Evaluation. These hallucinations involved significant misinterpretations and retrieval errors, impacting judgment accuracy and reliability. To address this, we employed a multi-step CoT approach on MLLM-as-a-Judge-Hard, adding reasoning steps before the conventional “Analyze-then-Judge” process. This enhanced procedure included: 1) image-instruction, 2) image, and 3) instruction. In Table 7, this strategy effectively reduced hallucinations across all formats, with significant improvements in tasks involving image-related information. In the Batch Ranking task, which requires handling longer text sequences, the detailed reasoning steps were particularly effective in reducing hallucinations.

**ZH** 幻觉检测与缓解。我们观察到，相比成对比较与评分评测，批量排序中幻觉出现的频率更高。这些幻觉涉及严重的误解与检索错误，影响了判定的准确性与可靠性。为此，我们在 MLLM-as-a-Judge-Hard 上采用了多步 CoT 方法，在常规的「先分析后判定」流程之前增加推理步骤。这一增强流程包括：1) 图像—指令、2) 图像、3) 指令。表 7 显示，该策略在所有格式上都有效减少了幻觉，在涉及图像信息的任务上改善尤为显著。在需要处理更长文本序列的批量排序任务中，细致的推理步骤对减少幻觉尤其有效。

**EN** 4.7 Scaling Law for MLLM-as-a-Judge

**ZH** 4.7 MLLM-as-a-Judge 的缩放定律

**EN** We conduct two sets of experiments with models of different sizes, the LLaVA-1.6 series models and the Qwen series models in four newly added datasets, illustrated in Figure 10 and 11. In Score evaluation, LLaVA-1.6-34b and Qwen-VL-Max slightly outperform others in Math, Chart, and Text tasks, showing a relatively strong scaling law.

**ZH** 我们用不同规模的模型进行了两组实验，即 LLaVA-1.6 系列模型与 Qwen 系列模型，在四个新增数据集上进行，如图 10 与图 11 所示。在评分评测中，LLaVA-1.6-34b 与 Qwen-VL-Max 在数学、图表与文本任务上略胜其他模型，呈现出相对明显的缩放定律。

**EN** Table 7: Reduction of hallucinations in MLLM-as-a-Judge-Hard through additional CoT steps compared to normal setting.

**ZH** 表 7：相比常规设定，通过额外 CoT 步骤在 MLLM-as-a-Judge-Hard 上减少幻觉的情况。

<!-- [原子块 · table] Setting Figure- instruction Figure Instruction Score 46.15% 48.72% 33.33% Pair 28.21% 35.90% 33.33% Batch 43.59% 35.90% 35.90% -->

**EN** 5 Related Work

**ZH** 5 相关工作

**EN** LLM as a Judge.

**ZH** 以大模型为裁判。

**EN** The evolution of LLMs has made them increasingly effective evaluators in Natural Language Processing (NLP) tasks. Zhu et al. (2023) introduced JudgeLM for LLM evaluation, followed by AUTO-J (Li et al., 2023a), aligning closely with human judgment (Bai et al., 2023b; Li et al., 2023d; Kim et al., 2023). Advancements in CoT reasoning (Wei et al., 2022; Chu et al., 2023) and training-free instruction following (Brown et al., 2020; Wei et al., 2021) further extend LLMs’ judging capability in diverse tasks like translation quality assessment (Kocmi & Federmann, 2023) and story generation (Chiang & Lee, 2023a).

**ZH** LLM 的演进使其在自然语言处理（NLP）任务中成为越来越有效的评估者。Zhu 等（2023）提出 JudgeLM 用于 LLM 评测，随后 Li 等（2023a）提出 AUTO-J，二者都与人类判断高度契合（Bai 等, 2023b；Li 等, 2023d；Kim 等, 2023）。CoT 推理（Wei 等, 2022；Chu 等, 2023）与免训练指令遵循（Brown 等, 2020；Wei 等, 2021）方面的进展，进一步把 LLM 的判定能力拓展到翻译质量评估（Kocmi & Federmann, 2023）与故事生成（Chiang & Lee, 2023a）等多种任务上。

**EN** Hallucination and Bias in Judgments.

**ZH** 判定中的幻觉与偏差。

**EN** MLLMs suffer from vision and language hallucinations (Ji et al., 2023; Huang et al., 2023a; Cui et al., 2023; Wang et al., 2023a), often due to vision-language misalignments in training phase (Sun et al., 2024; Huang et al., 2023b). Recent research focuses on hallucination evaluation (Liu et al., 2023a), detection (Li et al., 2023e; Wang et al., 2023a), and mitigation (Yin et al., 2023; Gunjal et al., 2023; Zhou et al., 2023), noting that even GPT-4V suffer from these issues (Shi et al., 2023; Liu et al., 2023a; Cui et al., 2023). Besides, biases in MLLM-as-a-Judge, similar to those in human decision-making (Blunch, 1984; Raghubir & Valenzuela, 2006) and other ML domains (Wang et al., 2018; Liu et al., 2023e), such as position (Zheng et al., 2023a), egocentric (Li et al., 2024), and verbosity biases (Saito et al., 2023), are compounded by the integration of visual perception, necessitating further investigation.

**ZH** MLLM 受到视觉与语言幻觉的困扰（Ji 等, 2023；Huang 等, 2023a；Cui 等, 2023；Wang 等, 2023a），其成因往往是训练阶段的视觉—语言错位（Sun 等, 2024；Huang 等, 2023b）。近来的研究聚焦于幻觉的评测（Liu 等, 2023a）、检测（Li 等, 2023e；Wang 等, 2023a）与缓解（Yin 等, 2023；Gunjal 等, 2023；Zhou 等, 2023），并指出即便 GPT-4V 也受这些问题影响（Shi 等, 2023；Liu 等, 2023a；Cui 等, 2023）。此外，MLLM-as-a-Judge 中的偏差——与人类决策（Blunch, 1984；Raghubir & Valenzuela, 2006）及其他机器学习（ML）领域（Wang 等, 2018；Liu 等, 2023e）中的偏差类似，如位置偏差（Zheng 等, 2023a）、自我中心偏差（Li 等, 2024）与冗长偏差（Saito 等, 2023）——因视觉感知的引入而被放大，亟需进一步研究。

**EN** 6 Future Directions

**ZH** 6 未来方向

**EN** Multimodal RLHF/DPO.

**ZH** 多模态 RLHF/DPO。

**EN** Our work is highly connected with multimodal RLHF/DPO (Sun et al., 2023; Li et al., 2023c; Yu et al., 2023a). Our dataset includes extensive human annotations, such as manually assigned scores and preference on pairs, which could serve as invaluable training material for RLHF reward models and supply paired data essential for DPO (Rafailov et al., 2024; Zhang et al., 2024), paving the way for enhancing the training of MLLMs.

**ZH** 我们的工作与多模态 RLHF/DPO（Sun 等, 2023；Li 等, 2023c；Yu 等, 2023a）高度相关。我们的数据集包含大量人工标注，例如人工给出的分数与成对偏好，这些可作为 RLHF 奖励模型的宝贵训练素材，并为 DPO（Rafailov 等, 2024；Zhang 等, 2024）提供必需的成对数据，为改进 MLLM 的训练铺平道路。

**EN** Exploring the upper bound of MLLM-as-a-Judge.

**ZH** 探索 MLLM-as-a-Judge 的上界。

**EN** Beyond expanding the steps in the Chain of Thought prompting (Wei et al., 2022), we see significant potential in more sophisticated reasoning frameworks, such as multi-agent debating (Chan et al., 2023) when MLLM acts as a Judge, which could enhance the judging accuracy through improved reasoning capabilities. Additionally, addressing inherent biases in the model during the judgment process is crucial. For instance, position bias in Pair Comparison and Batch Ranking (Zheng et al., 2023a; Wang et al., 2024a), and the tendency to assign higher scores, as discussed in (Lee et al., 2024), are critical areas for improvement.

**ZH** 除了在思维链提示中扩展步骤（Wei 等, 2022）之外，我们认为更精密的推理框架——例如当 MLLM 充当裁判时的多智能体辩论（Chan 等, 2023）——具有可观潜力，可通过更强的推理能力提升判定准确性。此外，解决判定过程中模型的固有偏差至关重要。例如成对比较与批量排序中的位置偏差（Zheng 等, 2023a；Wang 等, 2024a），以及（Lee 等, 2024）所讨论的打高分倾向，都是需要改进的关键方向。

**EN** Incorporating a human-in-the-loop approach (Wang et al., 2023b) offers a promising solution to enhance judgment consistency and reliability. For example, if judgment results vary in more than half of several repeated judgments, it may need human intervention for consistency checking. When it’s challenging to discern the MLLM’s judgment due to non-compliance with the suggested output format or lack of a clear outcome, human intervention may be required to refine this process by manually verifying judgments.

**ZH** 引入人在回路（human-in-the-loop）的方法（Wang 等, 2023b）为提升判定的一致性与可靠性提供了颇具前景的方案。例如，若在若干次重复判定中有超过一半的结果发生变化，就可能需要人工介入做一致性检查。当 MLLM 的判定因不符合建议的输出格式或缺乏明确结论而难以辨识时，也可能需要人工介入，通过手工核验判定来完善这一流程。

**EN** 7 Conclusion

**ZH** 7 结论

**EN** In this paper, we have presented a new benchmark, termed MLLM-as-a-Judge, to assess the judging capabilities of MLLMs across three critical evaluation settings in the multimodal domain: Scoring Evaluation, Pair Comparison, and Batch Ranking. We further evaluate their agreement with humans. Our results reveal that advanced MLLMs can win significant human recognition in Pair Comparisons, but perform poorly in Scoring Evaluation and Batch Ranking tasks. Our work highlights potential areas for future refinement and improvement of MLLMs. We advocate for additional efforts dedicated to supporting the continuous development of MLLMs as judges.

**ZH** 本文提出了一个新的基准 MLLM-as-a-Judge，用以评估 MLLM 在多模态领域三种关键评测设定下的判定能力：评分评测、成对比较与批量排序。我们还评估了它们与人类的一致性。结果表明，先进的 MLLM 能在成对比较中赢得显著的人类认可，但在评分评测与批量排序任务上表现不佳。我们的工作指出了 MLLM 未来可加改进的潜在方向，并呼吁投入更多努力，支持 MLLM 作为裁判的持续发展。

**EN** Impact Statement

**ZH** 影响声明

**EN** In this paper, we introduce a novel benchmark, termed MLLM-as-a-Judge, designed to propel the evolution of MLLMs toward achieving judgments that align more closely with human perspectives. This benchmark establishes a heightened criterion for assessing MLLMs, emphasizing their proficiency in comprehending and processing information in a manner reflective of human cognitive processes. One limitation of our work lies in the bias in human annotation and MLLMs. We leave the exploration of more objectives, ethically principled, and socially beneficial MLLM-as-a-Judge systems as our future work.

**ZH** 本文提出了一个新基准 MLLM-as-a-Judge，旨在推动 MLLM 的演进，使其判定更贴近人类视角。该基准为评估 MLLM 确立了更高的标准，强调其以贴近人类认知过程的方式理解与处理信息的能力。本工作的一个局限在于人工标注与 MLLM 中存在的偏差。我们把探索目标更客观、更符合伦理原则且更具社会效益的 MLLM-as-a-Judge 系统留作未来工作。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] Antol et al. (2015) Antol, S., Agrawal, A., Lu, J., Mitchell, M., Batra, D., Zitnick, C. L., and Parikh, D. Vqa: Visual question answering. In Proceedings of the IEEE international conference on compu -->

<!-- [原子块 · verbatim] Bai et al. (2023a) Bai, J., Bai, S., Yang, S., Wang, S., Tan, S., Wang, P., Lin, J., Zhou, C., and Zhou, J. Qwen-vl: A versatile vision-language model for understanding, localization, text reading, an -->

<!-- [原子块 · verbatim] Bai et al. (2023b) Bai, S., Yang, S., Bai, J., Wang, P., Zhang, X., Lin, J., Wang, X., Zhou, C., and Zhou, J. Touchstone: Evaluating vision-language models by language models. arXiv preprint arXiv:230 -->

<!-- [原子块 · verbatim] Banerjee & Lavie (2005) Banerjee, S. and Lavie, A. Meteor: An automatic metric for mt evaluation with improved correlation with human judgments. In Proceedings of the acl workshop on intrinsic and ext -->

<!-- [原子块 · verbatim] Bitton et al. (2023) Bitton, Y., Bansal, H., Hessel, J., Shao, R., Zhu, W., Awadalla, A., Gardner, J., Taori, R., and Schimdt, L. Visit-bench: A benchmark for vision-language instruction following ins -->

<!-- [原子块 · verbatim] Blunch (1984) Blunch, N. J. Position bias in multiple-choice questions. Journal of Marketing Research , 21(2):216–220, 1984. -->

<!-- [原子块 · verbatim] Brown et al. (2020) Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J. D., Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G., Askell, A., et al. Language models are few-shot learners. Advances -->

<!-- [原子块 · verbatim] Cai et al. (2023) Cai, Y., Mao, S., Wu, W., Wang, Z., Liang, Y., Ge, T., Wu, C., You, W., Song, T., Xia, Y., et al. Low-code llm: Visual programming over llms. arXiv preprint arXiv:2304.08103 , 2023. -->

<!-- [原子块 · verbatim] Chan et al. (2023) Chan, C.-M., Chen, W., Su, Y., Yu, J., Xue, W., Zhang, S., Fu, J., and Liu, Z. Chateval: Towards better llm-based evaluators through multi-agent debate. arXiv preprint arXiv:2308.07 -->

<!-- [原子块 · verbatim] Chiang & Lee (2023a) Chiang, C.-H. and Lee, H.-y. Can large language models be an alternative to human evaluations? arXiv preprint arXiv:2305.01937 , 2023a. -->

<!-- [原子块 · verbatim] Chiang & Lee (2023b) Chiang, C.-H. and Lee, H.-y. A closer look into automatic evaluation using large language models. arXiv preprint arXiv:2310.05657 , 2023b. -->

<!-- [原子块 · verbatim] Chu et al. (2023) Chu, Z., Chen, J., Chen, Q., Yu, W., He, T., Wang, H., Peng, W., Liu, M., Qin, B., and Liu, T. A survey of chain of thought reasoning: Advances, frontiers and future. arXiv preprint  -->

<!-- [原子块 · verbatim] Cui et al. (2023) Cui, C., Zhou, Y., Yang, X., Wu, S., Zhang, L., Zou, J., and Yao, H. Holistic analysis of hallucination in gpt-4v (ision): Bias and interference challenges. arXiv preprint arXiv:2311 -->

<!-- [原子块 · verbatim] Deng et al. (2024) Deng, X., Gu, Y., Zheng, B., Chen, S., Stevens, S., Wang, B., Sun, H., and Su, Y. Mind2web: Towards a generalist agent for the web. Advances in Neural Information Processing Systems -->

<!-- [原子块 · verbatim] Deutsch et al. (2023) Deutsch, D., Foster, G., and Freitag, M. Ties matter: Meta-evaluating modern metrics with pairwise accuracy and tie calibration. In Proceedings of the 2023 Conference on Empirica -->

<!-- [原子块 · verbatim] GeminiTeam (2023) GeminiTeam. Gemini: A family of highly capable multimodal models, 2023. -->

<!-- [原子块 · verbatim] Goutte & Gaussier (2005) Goutte, C. and Gaussier, E. A probabilistic interpretation of precision, recall and f-score, with implication for evaluation. In European conference on information retrieval , -->

<!-- [原子块 · verbatim] Gunjal et al. (2023) Gunjal, A., Yin, J., and Bas, E. Detecting and preventing hallucinations in large vision language models. arXiv preprint arXiv:2308.06394 , 2023. -->

<!-- [原子块 · verbatim] Huang et al. (2023a) Huang, L., Yu, W., Ma, W., Zhong, W., Feng, Z., Wang, H., Chen, Q., Peng, W., Feng, X., Qin, B., et al. A survey on hallucination in large language models: Principles, taxonomy, c -->

<!-- [原子块 · verbatim] Huang et al. (2024a) Huang, S., Hu, J., Yang, Z., Yang, L., Luo, T., Chen, H., Sun, L., and Yang, B. Decision mamba: Reinforcement learning via hybrid selective sequence modeling, 2024a. -->

<!-- [原子块 · verbatim] Huang et al. (2023b) Huang, Y., Zhang, Q., Sun, L., et al. Trustgpt: A benchmark for trustworthy and responsible large language models. arXiv preprint arXiv:2306.11507 , 2023b. -->

<!-- [原子块 · verbatim] Huang et al. (2024b) Huang, Y., Yuan, Q., Sheng, X., Yang, Z., Wu, H., Chen, P., Yang, Y., Li, L., and Lin, W. Aesbench: An expert benchmark for multimodal large language models on image aesthetics pe -->

<!-- [原子块 · verbatim] Ji et al. (2023) Ji, Z., Lee, N., Frieske, R., Yu, T., Su, D., Xu, Y., Ishii, E., Bang, Y. J., Madotto, A., and Fung, P. Survey of hallucination in natural language generation. ACM Computing Surveys , -->

<!-- [原子块 · verbatim] Jiang et al. (2024) Jiang, A. Q., Sablayrolles, A., Roux, A., Mensch, A., Savary, B., Bamford, C., Chaplot, D. S., de las Casas, D., Hanna, E. B., Bressand, F., Lengyel, G., Bour, G., Lample, G., Lava -->

<!-- [原子块 · verbatim] Jin et al. (2023) Jin, P., Takanobu, R., Zhang, C., Cao, X., and Yuan, L. Chat-univi: Unified visual representation empowers large language models with image and video understanding. arXiv preprint ar -->

<!-- [原子块 · verbatim] Kim et al. (2023) Kim, S., Shin, J., Cho, Y., Jang, J., Longpre, S., Lee, H., Yun, S., Shin, S., Kim, S., Thorne, J., et al. Prometheus: Inducing fine-grained evaluation capability in language models. -->

<!-- [原子块 · verbatim] Kocmi & Federmann (2023) Kocmi, T. and Federmann, C. Large language models are state-of-the-art evaluators of translation quality. arXiv preprint arXiv:2302.14520 , 2023. -->

<!-- [原子块 · verbatim] Lee et al. (2024) Lee, S., Kim, S., Park, S. H., Kim, G., and Seo, M. Prometheus-vision: Vision-language model as a judge for fine-grained evaluation. arXiv preprint arXiv:2401.06591 , 2024. -->

<!-- [原子块 · verbatim] Lee Rodgers & Nicewander (1988) Lee Rodgers, J. and Nicewander, W. A. Thirteen ways to look at the correlation coefficient. The American Statistician , 42(1):59–66, 1988. -->

<!-- [原子块 · verbatim] Levenshtein et al. (1966) Levenshtein, V. I. et al. Binary codes capable of correcting deletions, insertions, and reversals. In Soviet physics doklady , volume 10, pp. 707–710. Soviet Union, 1966. -->

<!-- [原子块 · verbatim] Li et al. (2023a) Li, J., Sun, S., Yuan, W., Fan, R.-Z., Zhao, H., and Liu, P. Generative judge for evaluating alignment. arXiv preprint arXiv:2310.05470 , 2023a. -->

<!-- [原子块 · verbatim] Li et al. (2023b) Li, K., Wang, Y., He, Y., Li, Y., Wang, Y., Liu, Y., Wang, Z., Xu, J., Chen, G., Luo, P., et al. Mvbench: A comprehensive multi-modal video understanding benchmark. arXiv preprint ar -->

<!-- [原子块 · verbatim] Li et al. (2023c) Li, L., Xie, Z., Li, M., Chen, S., Wang, P., Chen, L., Yang, Y., Wang, B., and Kong, L. Silkie: Preference distillation for large visual language models. arXiv preprint arXiv:2312.10 -->

<!-- [原子块 · verbatim] Li et al. (2023d) Li, X., Zhang, T., Dubois, Y., Taori, R., Gulrajani, I., Guestrin, C., Liang, P., and Hashimoto, T. B. Alpacaeval: An automatic evaluator of instruction-following models. GitHub repo -->

<!-- [原子块 · verbatim] Li et al. (2023e) Li, Y., Du, Y., Zhou, K., Wang, J., Zhao, W. X., and Wen, J.-R. Evaluating object hallucination in large vision-language models. arXiv preprint arXiv:2305.10355 , 2023e. -->

<!-- [原子块 · verbatim] Li et al. (2024) Li, Z., Xu, X., Shen, T., Xu, C., Gu, J.-C., and Tao, C. Leveraging large language models for nlg evaluation: A survey. arXiv preprint arXiv:2401.07103 , 2024. -->

<!-- [原子块 · verbatim] Lin (2004) Lin, C.-Y. Rouge: A package for automatic evaluation of summaries. In Text summarization branches out , pp. 74–81, 2004. -->

<!-- [原子块 · verbatim] Lin et al. (2014) Lin, T.-Y., Maire, M., Belongie, S. J., Hays, J., Perona, P., Ramanan, D., Dollár, P., and Zitnick, C. L. Microsoft coco: Common objects in context. In European Conference on Compute -->

<!-- [原子块 · verbatim] Liu et al. (2023a) Liu, F., Guan, T., Li, Z., Chen, L., Yacoob, Y., Manocha, D., and Zhou, T. Hallusionbench: You see what you think? or you think what you see? an image-context reasoning benchmark ch -->

<!-- [原子块 · verbatim] Liu et al. (2023b) Liu, F., Lin, K., Li, L., Wang, J., Yacoob, Y., and Wang, L. Aligning large multi-modal model with robust instruction tuning. arXiv preprint arXiv:2306.14565 , 2023b. -->

<!-- [原子块 · verbatim] Liu et al. (2023c) Liu, H., Li, C., Li, Y., and Lee, Y. J. Improved baselines with visual instruction tuning, 2023c. -->

<!-- [原子块 · verbatim] Liu et al. (2023d) Liu, H., Li, C., Wu, Q., and Lee, Y. J. Visual instruction tuning, 2023d. -->

<!-- [原子块 · verbatim] Liu et al. (2023e) Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., and Liang, P. Lost in the middle: How language models use long contexts. arXiv preprint arXiv:2307.03172 -->

<!-- [原子块 · verbatim] Lu et al. (2022) Lu, P., Mishra, S., Xia, T., Qiu, L., Chang, K.-W., Zhu, S.-C., Tafjord, O., Clark, P., and Kalyan, A. Learn to explain: Multimodal reasoning via thought chains for science question a -->

<!-- [原子块 · verbatim] Lu et al. (2023) Lu, P., Bansal, H., Xia, T., Liu, J., yue Li, C., Hajishirzi, H., Cheng, H., Chang, K.-W., Galley, M., and Gao, J. Mathvista: Evaluating math reasoning in visual contexts with gpt-4v, -->

<!-- [原子块 · verbatim] Masry et al. (2022) Masry, A., Long, D., Tan, J. Q., Joty, S., and Hoque, E. ChartQA: A benchmark for question answering about charts with visual and logical reasoning. In Findings of the Association  -->

<!-- [原子块 · verbatim] Mathew et al. (2021) Mathew, M., Bagal, V., Tito, R. P., Karatzas, D., Valveny, E., and Jawahar, C. Infographicvqa. 2022 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV) , pp. 2582 -->

<!-- [原子块 · verbatim] OpenAI (2023) OpenAI. Gpt-4 technical report. 2023. -->

<!-- [原子块 · verbatim] OpenAI (2023) OpenAI. Openai models - gpt-4-vision. https://openai.com/research/gpt-4v-system-card , 2023. -->

<!-- [原子块 · verbatim] Ouyang et al. (2022) Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C., Mishkin, P., Zhang, C., Agarwal, S., Slama, K., Ray, A., et al. Training language models to follow instructions with hu -->

<!-- [原子块 · verbatim] Papineni et al. (2002) Papineni, K., Roukos, S., Ward, T., and Zhu, W.-J. Bleu: a method for automatic evaluation of machine translation. In Proceedings of the 40th annual meeting of the Association f -->

<!-- [原子块 · verbatim] Prendki (2023) Prendki, J. Are you spending too much money labeling data?, 2023. -->

<!-- [原子块 · verbatim] Rafailov et al. (2024) Rafailov, R., Sharma, A., Mitchell, E., Manning, C. D., Ermon, S., and Finn, C. Direct preference optimization: Your language model is secretly a reward model. Advances in Neura -->

<!-- [原子块 · verbatim] Raghubir & Valenzuela (2006) Raghubir, P. and Valenzuela, A. Center-of-inattention: Position biases in decision-making. Organizational Behavior and Human Decision Processes , 99(1):66–80, 2006. -->

<!-- [原子块 · verbatim] Roziere et al. (2023) Roziere, B., Gehring, J., Gloeckle, F., Sootla, S., Gat, I., Tan, X. E., Adi, Y., Liu, J., Remez, T., Rapin, J., et al. Code llama: Open foundation models for code. arXiv preprin -->

<!-- [原子块 · verbatim] Saito et al. (2023) Saito, K., Wachi, A., Wataoka, K., and Akimoto, Y. Verbosity bias in preference labeling by large language models. arXiv preprint arXiv:2310.10076 , 2023. -->

<!-- [原子块 · verbatim] Sharma et al. (2018) Sharma, P., Ding, N., Goodman, S., and Soricut, R. Conceptual captions: A cleaned, hypernymed, image alt-text dataset for automatic image captioning. In Annual Meeting of the Asso -->

<!-- [原子块 · verbatim] Shi et al. (2023) Shi, Y., Peng, D., Liao, W., Lin, Z., Chen, X., Liu, C., Zhang, Y., and Jin, L. Exploring ocr capabilities of gpt-4v (ision): A quantitative and in-depth evaluation. arXiv preprint a -->

<!-- [原子块 · verbatim] Singh et al. (2019) Singh, A., Natarajan, V., Shah, M., Jiang, Y., Chen, X., Batra, D., Parikh, D., and Rohrbach, M. Towards vqa models that can read. 2019 IEEE/CVF Conference on Computer Vision and P -->

<!-- [原子块 · verbatim] Srinivasan et al. (2021) Srinivasan, K., Raman, K., Chen, J., Bendersky, M., and Najork, M. Wit: Wikipedia-based image text dataset for multimodal multilingual machine learning. Proceedings of the 44t -->

<!-- [原子块 · verbatim] Sun et al. (2024) Sun, L., Huang, Y., Wang, H., Wu, S., Zhang, Q., Gao, C., Huang, Y., Lyu, W., Zhang, Y., Li, X., et al. Trustllm: Trustworthiness in large language models. arXiv preprint arXiv:2401. -->

<!-- [原子块 · verbatim] Sun et al. (2020) Sun, W., Nasraoui, O., and Shafto, P. Evolution and impact of bias in human and machine learning algorithm interaction. Plos one , 15(8):e0235502, 2020. -->

<!-- [原子块 · verbatim] Sun et al. (2023) Sun, Z., Shen, S., Cao, S., Liu, H., Li, C., Shen, Y., Gan, C., Gui, L.-Y., Wang, Y.-X., Yang, Y., et al. Aligning large multimodal models with factually augmented rlhf. arXiv prepri -->

<!-- [原子块 · verbatim] Touvron et al. (2023) Touvron, H., Lavril, T., Izacard, G., Martinet, X., Lachaux, M.-A., Lacroix, T., Rozière, B., Goyal, N., Hambro, E., Azhar, F., et al. Llama: Open and efficient foundation langua -->

<!-- [原子块 · verbatim] Vedantam et al. (2015) Vedantam, R., Lawrence Zitnick, C., and Parikh, D. Cider: Consensus-based image description evaluation. In Proceedings of the IEEE conference on computer vision and pattern reco -->

<!-- [原子块 · verbatim] Wang et al. (2023a) Wang, J., Zhou, Y., Xu, G., Shi, P., Zhao, C., Xu, H., Ye, Q., Yan, M., Zhang, J., Zhu, J., et al. Evaluation and analysis of hallucination in large vision-language models. arXiv p -->

<!-- [原子块 · verbatim] Wang et al. (2023b) Wang, P., Li, L., Chen, L., Zhu, D., Lin, B., Cao, Y., Liu, Q., Liu, T., and Sui, Z. Large language models are not fair evaluators. arXiv preprint arXiv:2305.17926 , 2023b. -->

<!-- [原子块 · verbatim] Wang et al. (2023c) Wang, W., Lv, Q., Yu, W., Hong, W., Qi, J., Wang, Y., Ji, J., Yang, Z., Zhao, L., Song, X., Xu, J., Xu, B., Li, J., Dong, Y., Ding, M., and Tang, J. Cogvlm: Visual expert for pretr -->

<!-- [原子块 · verbatim] Wang et al. (2018) Wang, X., Golbandi, N., Bendersky, M., Metzler, D., and Najork, M. Position bias estimation for unbiased learning to rank in personal search. In Proceedings of the eleventh ACM inte -->

<!-- [原子块 · verbatim] Wang et al. (2024a) Wang, X., Ma, B., Hu, C., Weber-Genzel, L., Röttger, P., Kreuter, F., Hovy, D., and Plank, B. ” my answer is c”: First-token probabilities do not match text answers in instruction- -->

<!-- [原子块 · verbatim] Wang et al. (2024b) Wang, X., Zhou, Y., Liu, X., Lu, H., Xu, Y., He, F., Yoon, J., Lu, T., Bertasius, G., Bansal, M., et al. Mementos: A comprehensive benchmark for multimodal large language model rea -->

<!-- [原子块 · verbatim] Wang et al. (2022) Wang, Z. J., Montoya, E., Munechika, D., Yang, H., Hoover, B., and Chau, D. H. Diffusiondb: A large-scale prompt gallery dataset for text-to-image generative models. ArXiv , abs/221 -->

<!-- [原子块 · verbatim] Wei et al. (2021) Wei, J., Bosma, M., Zhao, V. Y., Guu, K., Yu, A. W., Lester, B., Du, N., Dai, A. M., and Le, Q. V. Finetuned language models are zero-shot learners. arXiv preprint arXiv:2109.01652 , -->

<!-- [原子块 · verbatim] Wei et al. (2022) Wei, J., Wang, X., Schuurmans, D., Bosma, M., Xia, F., Chi, E., Le, Q. V., Zhou, D., et al. Chain-of-thought prompting elicits reasoning in large language models. Advances in Neural  -->

<!-- [原子块 · verbatim] Wu et al. (2023a) Wu, S., Fei, H., Qu, L., Ji, W., and Chua, T.-S. Next-gpt: Any-to-any multimodal llm. arXiv preprint arXiv:2309.05519 , 2023a. -->

<!-- [原子块 · verbatim] Wu et al. (2023b) Wu, Y., Wang, S., Yang, H., Zheng, T., Zhang, H., Zhao, Y., and Qin, B. An early evaluation of gpt-4v (ision). arXiv preprint arXiv:2310.16534 , 2023b. -->

<!-- [原子块 · verbatim] Yang et al. (2023) Yang, Z., Li, L., Lin, K., Wang, J., Lin, C.-C., Liu, Z., and Wang, L. The dawn of lmms: Preliminary explorations with gpt-4v (ision). arXiv preprint arXiv:2309.17421 , 9(1):1, 2023 -->

<!-- [原子块 · verbatim] Yin et al. (2023) Yin, S., Fu, C., Zhao, S., Xu, T., Wang, H., Sui, D., Shen, Y., Li, K., Sun, X., and Chen, E. Woodpecker: Hallucination correction for multimodal large language models. arXiv preprin -->

<!-- [原子块 · verbatim] Yu et al. (2023a) Yu, T., Yao, Y., Zhang, H., He, T., Han, Y., Cui, G., Hu, J., Liu, Z., Zheng, H.-T., Sun, M., et al. Rlhf-v: Towards trustworthy mllms via behavior alignment from fine-grained correc -->

<!-- [原子块 · verbatim] Yu et al. (2023b) Yu, W., Yang, Z., Li, L., Wang, J., Lin, K., Liu, Z., Wang, X., and Wang, L. Mm-vet: Evaluating large multimodal models for integrated capabilities. ArXiv , abs/2308.02490, 2023b. UR -->

<!-- [原子块 · verbatim] Zhang et al. (2024) Zhang, R., Gui, L., Sun, Z., Feng, Y., Xu, K., Zhang, Y., Fu, D., Li, C., Hauptmann, A., Bisk, Y., et al. Direct preference optimization of video large multimodal models from langu -->

<!-- [原子块 · verbatim] Zheng et al. (2023a) Zheng, C., Zhou, H., Meng, F., Zhou, J., and Huang, M. On large language models’ selection bias in multi-choice questions. arXiv preprint arXiv:2309.03882 , 2023a. -->

<!-- [原子块 · verbatim] Zheng et al. (2023b) Zheng, L., Chiang, W.-L., Sheng, Y., Zhuang, S., Wu, Z., Zhuang, Y., Lin, Z., Li, Z., Li, D., Xing, E., et al. Judging llm-as-a-judge with mt-bench and chatbot arena. arXiv prepri -->

<!-- [原子块 · verbatim] Zhou et al. (2023) Zhou, Y., Cui, C., Yoon, J., Zhang, L., Deng, Z., Finn, C., Bansal, M., and Yao, H. Analyzing and mitigating object hallucination in large vision-language models. arXiv preprint arX -->

<!-- [原子块 · verbatim] Zhu et al. (2023) Zhu, L., Wang, X., and Wang, X. Judgelm: Fine-tuned large language models are scalable judges. arXiv preprint arXiv:2310.17631 , 2023. -->

**EN** Appendix A Comprehensive Related Works

**ZH** 附录 A 相关工作的完整综述

**EN** A.1 Large Model as Judge

**ZH** A.1 以大模型为裁判

**EN** The rapid development of LLMs has significantly enhanced their capabilities in long-term context perception and reasoning, increasingly popularizing their use as evaluators in various Natural Language Processing (NLP) tasks. Zhu et al. (2023) were pioneers in this area, introducing JudgeLM, a fine-tuned LLM designed for evaluating other LLMs. Building on this, Li et al. (2023a) introduced AUTO-J, a system that evaluates LLMs through both pairwise comparisons and single-response assessments, demonstrating close alignment with human judgment (Bai et al., 2023b; Li et al., 2023d; Kim et al., 2023). Further advancements in LLMs, such as the development of Chain-of-Thought reasoning (Wei et al., 2022; Chu et al., 2023), training-free instruction following (Brown et al., 2020; Wei et al., 2021), and enhanced alignment with human preferences (Ouyang et al., 2022), have solidified their role in diverse tasks like translation quality assessment (Kocmi & Federmann, 2023) and story generation (Chiang & Lee, 2023a).

**ZH** LLM 的快速发展显著增强了其在长程语境感知与推理上的能力，使其作为各类自然语言处理（NLP）任务评估者的用法日益普及。Zhu 等（2023）是该方向的先驱，提出了 JudgeLM——一个为评测其他 LLM 而微调的 LLM。在此基础上，Li 等（2023a）提出 AUTO-J，一个通过成对比较与单回答评估来评测 LLM 的系统，展现出与人类判断的高度契合（Bai 等, 2023b；Li 等, 2023d；Kim 等, 2023）。LLM 的进一步进展——如思维链推理的发展（Wei 等, 2022；Chu 等, 2023）、免训练的指令遵循（Brown 等, 2020；Wei 等, 2021），以及与人类偏好的增强对齐（Ouyang 等, 2022）——巩固了它们在翻译质量评估（Kocmi & Federmann, 2023）与故事生成（Chiang & Lee, 2023a）等多样任务中的角色。

**EN** A.2 Hallucination and Bias in Judge

**ZH** A.2 裁判中的幻觉与偏差

**EN** MLLMs are known to exhibit both vision hallucination and hallucination originating from LLMs, a phenomenon typically characterized by responses containing information not present in the visual or natural language context (Ji et al., 2023; Huang et al., 2023a; Cui et al., 2023; Wang et al., 2023a). This issue often stems from misalignments in vision-language training (Sun et al., 2024; Huang et al., 2023b). Recent studies have begun to address these hallucination issues, focusing on evaluation (Liu et al., 2023a), detection (Li et al., 2023e; Wang et al., 2023a), and mitigation strategies (Yin et al., 2023; Gunjal et al., 2023; Zhou et al., 2023). Notably, GPT-4V (OpenAI, 2023), despite being a leading model in many fields (Yang et al., 2023; Wu et al., 2023b), has also demonstrated susceptibility to hallucinations (Shi et al., 2023; Liu et al., 2023a; Cui et al., 2023). This raises concerns about the reliability of MLLMs in evaluative roles.

**ZH** 已知 MLLM 既表现出视觉幻觉，也表现出源自 LLM 的幻觉，这一现象的典型特征是回答中包含视觉或自然语言语境中并不存在的信息（Ji 等, 2023；Huang 等, 2023a；Cui 等, 2023；Wang 等, 2023a）。该问题通常源于视觉—语言训练中的错位（Sun 等, 2024；Huang 等, 2023b）。近期研究开始应对这些幻觉问题，聚焦于评测（Liu 等, 2023a）、检测（Li 等, 2023e；Wang 等, 2023a）与缓解策略（Yin 等, 2023；Gunjal 等, 2023；Zhou 等, 2023）。值得注意的是，尽管 GPT-4V（OpenAI, 2023）在诸多领域处于领先地位（Yang 等, 2023；Wu 等, 2023b），它同样被证明易受幻觉影响（Shi 等, 2023；Liu 等, 2023a；Cui 等, 2023），这引发了人们对 MLLM 在评估角色上可靠性的担忧。

**EN** In terms of bias, MLLM judging is subject to issues not exclusive to our context of evaluation but also observed in human decision-making (Blunch, 1984; Raghubir & Valenzuela, 2006) and Machine Learning (ML) domains (Wang et al., 2018; Liu et al., 2023e; Huang et al., 2024a) such as position bias (Zheng et al., 2023a), egocentric bias (Li et al., 2024), and verbosity bias (Saito et al., 2023). The integration of visual perception in MLLMs introduces additional complexities, resulting in biases unique to the fusion of dual perceptions, an area that still demands thorough exploration.

**ZH** 在偏差方面，MLLM 判定所面临的问题并非本评测语境所独有，在人类决策（Blunch, 1984；Raghubir & Valenzuela, 2006）与机器学习（ML）领域（Wang 等, 2018；Liu 等, 2023e；Huang 等, 2024a）中同样存在，例如位置偏差（Zheng 等, 2023a）、自我中心偏差（Li 等, 2024）与冗长偏差（Saito 等, 2023）。视觉感知在 MLLM 中的引入带来了额外的复杂性，产生了双重感知融合所特有的偏差，这一领域仍需充分探索。

**EN** A.3 Evaluating Large Multimodal Models

**ZH** A.3 大型多模态模型的评测

**EN** Evaluating MLLMs typically involves diverse tasks and corresponding metrics, which reflect the models’ ability to comprehend and generate content based on both visual and textual information. For instance, in image captioning tasks, models are tasked with generating descriptive text for a given image. The effectiveness of these models is measured using metrics such as BLEU (Papineni et al., 2002), METEOR (Banerjee & Lavie, 2005), ROUGE (Lin, 2004), and CIDEr (Vedantam et al., 2015). In the context of Visual Question Answering (VQA), models are evaluated based on their ability to answer questions on an image’s content. Here, the accuracy of model responses is compared against human-annotated answers, serving as the primary metric (Antol et al., 2015) to ensure alignment with human preferences.

**ZH** 评测 MLLM 通常涉及多样的任务与相应的指标，反映模型基于视觉与文本信息理解和生成内容的能力。例如，在图像描述任务中，模型要为给定图像生成描述性文本，其效果用 BLEU（Papineni 等, 2002）、METEOR（Banerjee & Lavie, 2005）、ROUGE（Lin, 2004）与 CIDEr（Vedantam 等, 2015）等指标衡量。在视觉问答（VQA）情境下，模型的评测基于其回答有关图像内容问题的能力；这里把模型回答的准确率与人工标注答案作比较，作为主要指标（Antol 等, 2015），以确保与人类偏好相一致。

**EN** However, when tackling sophisticated visual-language tasks, conventional evaluation metrics often fail to accurately capture the nuanced responses generated by these models, especially in complex or subjective scenarios that involve both visual elements and extended textual content (Liu et al., 2023a). Additionally, while manual annotation offers a more comprehensive and human-like evaluation, it comes with significant challenges. These include high costs (Prendki, 2023), potential biases (Zheng et al., 2023b), and the difficulty of ensuring consistent replication (Chiang & Lee, 2023a). These limitations highlight the need for a more holistic approach to evaluation, one that combines human-like calibration with more fine-grained assessment methods.

**ZH** 然而，在处理复杂的视觉—语言任务时，常规评测指标往往无法准确捕捉这些模型生成的细致回答，在同时涉及视觉元素与长文本内容的复杂或主观场景中尤为如此（Liu 等, 2023a）。此外，尽管人工标注能提供更全面、更贴近人类的评估，它也伴随着重大挑战，包括高昂成本（Prendki, 2023）、潜在偏差（Zheng 等, 2023b）以及难以保证一致的可复现性（Chiang & Lee, 2023a）。这些局限凸显出对更整体化评测方法的需求——一种把类人校准与更细粒度评估手段结合起来的方法。

**EN** Appendix B Detailed Benchmark Construction

**ZH** 附录 B 基准构建细节

**EN** B.1 Step 1: Image-Instruction Collection

**ZH** B.1 步骤 1：图像—指令采集

**EN** To attain the outlined objectives, our approach begins with a detailed analysis of the capabilities of MLLMs. Specifically, we focus on the following abilities within MLLMs:

**ZH** 为达成既定目标，我们的方法始于对 MLLM 能力的细致分析。具体地，我们关注 MLLM 的以下能力：

**EN** • Recognition Ability: This encompasses general visual recognition capabilities, such as object recognition, Optical Character Recognition (OCR), and other high-level tasks in computer vision (Yu et al., 2023b).

**ZH** • 识别能力：涵盖通用的视觉识别能力，如目标识别、光学字符识别（OCR）以及计算机视觉中的其他高层任务（Yu 等, 2023b）。

**EN** • Comprehension Ability: This pertains to the model’s proficiency in spatial understanding and scenario comprehension.

**ZH** • 理解能力：指模型在空间理解与场景理解上的熟练程度。

**EN** • Inferential Ability: This involves the model’s capacity to process information and reasoning, a critical component in processing charts, graphs, and mathematics.

**ZH** • 推理能力：指模型处理信息与进行推理的能力，这是处理图表、图形与数学时的关键要素。

**EN** • Multilingual Ability: This assesses the model’s competence in understanding and processing multiple languages, especially focusing on their appearance in visual tasks such as text reading on images (Singh et al., 2019).

**ZH** • 多语言能力：评估模型理解和处理多种语言的能力，尤其关注它们在文本阅读等视觉任务中的表现（Singh 等, 2019）。

**EN** To ensure a robust and comprehensive assessment, we meticulously identify and incorporate 10 diverse datasets 8 into our evaluation framework. This strategic selection aims to enrich the diversity of our assessment tasks and enhance the breadth and depth of our evaluation capabilities, as well as prevent biases. These datasets are chosen based on their ability to effectively challenge the various aspects of MLLMs, via different downstream tasks, ensuring a thorough and nuanced understanding of their performance and potential.

**ZH** 为确保评估稳健而全面，我们仔细甄别并把 10 个多样化数据集 8 纳入评测框架。这一策略性选择旨在丰富评测任务的多样性、拓展评测能力的广度与深度，并防止偏差。这些数据集的选取依据是其能否通过不同的下游任务有效挑战 MLLM 的各个方面，以确保对其表现与潜力形成透彻而细致的认识。

**EN** To construct a robust and unbiased set of image-instruction pairs, we randomly select 300 images from each dataset, ensuring a diverse representation. Specifically, for the MathVista dataset, which includes the provision of hints, we extract 600 corresponding instructions, encompassing both scenarios: with and without hints. For the remaining datasets, we align 300 instructions with the sampled images. This process culminates in a comprehensive collection comprising 4,114 images corresponding with 4,414 instructions.

**ZH** 为构建稳健且无偏的图像—指令对集合，我们从每个数据集中随机选取 300 张图像，以确保表征的多样性。具体地，对提供提示的 MathVista 数据集，我们抽取 600 条相应指令，覆盖有提示与无提示两种情形。对其余数据集，我们为采样得到的图像匹配 300 条指令。这一过程最终形成了一个包含 4,114 张图像、对应 4,414 条指令的完整集合。

**EN** Table 8: Datasets and corresponding tasks in benchmark construction, each task is matched with several required abilities. (Rec.-Recognition, Comp.-Comprehension, Inf.-Inferential, Mul.-Multilingual)

**ZH** 表 8：基准构建中的数据集与对应任务，每个任务匹配若干所需能力。（Rec.-识别，Comp.-理解，Inf.-推理，Mul.-多语言）

<!-- [原子块 · table] Dataset Image #Images #Questions #Selected Task Ability Type Pairs Required Conceptual Captions Web image 3.3M – 300 Captioning Rec.&Comp. ( Sharma et al., 2018 ) ChartQA Chart 21K 33K 300 Chart reaso -->

**EN** B.2 Step 2: MLLM Responses Collection

**ZH** B.2 步骤 2：MLLM 回答采集

**EN** We engage with 4 mainstream MLLMs (i.e., GPT-4V, Gemini, LLaVA, CogVLM) by providing them with our assembled image-instruction pairs for the first 3,300 image-instruction pairs, each VLM generated a response, resulting in a comprehensive collection of 13,200 answers, with each of the 3,300 instructions receiving a distinct response from each of the four MLLMs. For the last 4 datasets, we added during the rebuttal, we leverage GPT-4V, Gemini, Qwen-VL-Max, and LLaVA-1.6-34b. For the sequential dataset Mementos (Wang et al., 2024b), we leverage GPT-4V, Qwen-VL-Max, ChatUnivi (Jin et al., 2023), VideoChat2 (Li et al., 2023b) to generate responses. Upon collecting a total of 17,656 responses from the MLLMs, we proceed to analyze the distribution of response lengths for each model. Figure 8 is a detailed illustration of length distribution in corresponding datasets.

**ZH** 我们调用了 4 个主流 MLLM（即 GPT-4V、Gemini、LLaVA、CogVLM），就前 3,300 个图像—指令对向它们提供我们组装好的数据，每个 VLM 生成一条回答，共形成 13,200 条回答的集合，3,300 条指令中的每一条都收到来自四个 MLLM 各自的一条不同回答。对我们在 rebuttal 期间新增的最后 4 个数据集，我们改用 GPT-4V、Gemini、Qwen-VL-Max 与 LLaVA-1.6-34b。对时序数据集 Mementos（Wang 等, 2024b），我们调用 GPT-4V、Qwen-VL-Max、ChatUnivi（Jin 等, 2023）与 VideoChat2（Li 等, 2023b）生成回答。在从 MLLM 处共收集到 17,656 条回答后，我们着手分析每个模型的回答长度分布。图 8 是各对应数据集中长度分布的详细图示。

<!-- [原子块 · object]  -->

**EN** Figure 8: Response length distribution in 10 datasets. The horizontal axis represents length, and the vertical axis represents density.

**ZH** 图 8：10 个数据集中的回答长度分布。横轴表示长度，纵轴表示密度。

**EN** Appendix C Detailed Experiment Settings

**ZH** 附录 C 实验设置细节

**EN** C.1 Response VLM Settings

**ZH** C.1 回答生成所用的 VLM 设置

**EN** We use GPT-4V, Gemini, LLaVA-1.5-13b, CogVLM, Qwen-VL-Max, LLaVA-1.6-34b to answer the image-instruction pair. We discuss their hyperparameter settings and problems encountered during inference respectively:

**ZH** 我们使用 GPT-4V、Gemini、LLaVA-1.5-13b、CogVLM、Qwen-VL-Max、LLaVA-1.6-34b 来回答图像—指令对。下面分别讨论它们的超参数设置与推理中遇到的问题：

**EN** • GPT-4V (OpenAI, 2023). We set the temperature and top-p as 0.9, max-token as 2048. However, we encounter some situations where it cannot answer accurately or refuses to answer due to ethical issues like Unfortunately, due to my programming, I’m unable to …, which brings some difficulties to us in defining its judging capability.

**ZH** • GPT-4V（OpenAI, 2023）。我们把温度与 top-p 设为 0.9，max-token 设为 2048。然而我们遇到一些情形：它无法准确作答，或因伦理问题拒答，例如「很遗憾，由于我的程序设计，我无法……」，这给我们界定其判定能力带来了一些困难。

**EN** • Gemini (GeminiTeam, 2023). We use the default settings, which set temperature as 0.4, top-p as 1, and max-token as 2048. It should be noted that Gemini will receive more ethical limitations than GPT-4V, and will refuse to answer on the diffusion data set. But for some more difficult questions, it can’t answer the questions, but it will ”forcibly answer” the user’s questions. In this case, GPT-4V will sincerely admit its shortcomings and give a possible answer.

**ZH** • Gemini（GeminiTeam, 2023）。我们使用默认设置，温度为 0.4，top-p 为 1，max-token 为 2048。需要指出的是，Gemini 会比 GPT-4V 受到更多伦理限制，并会在扩散数据集上拒答。但对某些更难的问题，它无法回答却又会「强行作答」。在同样的情形下，GPT-4V 会坦承自身不足并给出一个可能的答案。

**EN** • LLaVA-1.5-13b (Liu et al., 2023d). We set temperature as 0, tok-⟦SLOT_20⟧ as 1, max-token as 2048, and beam search number as 3. The reason why we select such a low temperature is that LLaVA cannot correctly output its judge in a specific format. We collect responses by inference on a dual-4090 local server.

**ZH** • LLaVA-1.5-13b（Liu 等, 2023d）。我们把温度设为 0，tok-⟦SLOT_20⟧ 设为 1，max-token 设为 2048，束搜索数设为 3。之所以选择如此低的温度，是因为 LLaVA 无法以特定格式正确输出其判定。我们通过在双 4090 的本地服务器上推理来收集回答。

**EN** • CogVLM (Wang et al., 2023c). For the hyper-parameter, we use the default setting and set max-token as 2048. We collect responses by inference on a dual-4090 local server.

**ZH** • CogVLM（Wang 等, 2023c）。超参数方面我们使用默认设置，并把 max-token 设为 2048。我们通过在双 4090 的本地服务器上推理来收集回答。

**EN** • Qwen-VL Family (Bai et al., 2023a). We use the default settings for Qwen-VL family, with top-p as 0.8 and max-token as 2048.

**ZH** • Qwen-VL 系列（Bai 等, 2023a）。我们对 Qwen-VL 系列使用默认设置，top-p 为 0.8，max-token 为 2048。

**EN** • LLaVA-1.6 Family (Liu et al., 2023c). We set the temperature as 0.4 and top-p as 0.9, max-token as 2048.

**ZH** • LLaVA-1.6 系列（Liu 等, 2023c）。我们把温度设为 0.4，top-p 设为 0.9，max-token 设为 2048。

**EN** C.2 GPT-4V as Judge

**ZH** C.2 以 GPT-4V 为裁判

**EN** We adopt GPT-4V without using JSON Mode mod based on our preliminary experiment in Appendix D.3, but required it to output in JSON format in our prompt. Following the hyper-parameter set in (Chiang & Lee, 2023b), we set the temperature to 0.9, top-⟦SLOT_21⟧ to 0.9, and max-token to 2048 in both cases with and without pictures. When there is a format error in the output or ethical settings are triggered, we will sample again. If it is still wrong, we will skip this piece of data.

**ZH** 基于附录 D.3 中的预备实验，我们采用未开启 JSON Mode 的 GPT-4V，但在提示中要求它以 JSON 格式输出。沿用（Chiang & Lee, 2023b）设定的超参数，在有图与无图两种情形下我们都把温度设为 0.9、top-⟦SLOT_21⟧ 设为 0.9、max-token 设为 2048。当输出出现格式错误或触发伦理设置时，我们会重新采样；若仍然错误，则跳过该条数据。

**EN** C.3 Gemini-Vision-Pro as Judge

**ZH** C.3 以 Gemini-Vision-Pro 为裁判

**EN** We call Gemini’s API on the Google Cloud Server and use the default settings for temperature and top-⟦SLOT_22⟧. It should be noted that even though Gemini is currently the only VLM that can perform Judge, it will occasionally speak Chinese or Japanese during the output process when using English text and English pictures, shown as Unicode in Figure 9. Although it is semantically continuous, that is, it can be used after translation, and it greatly affects the continuity of the judge. We believe that this is a capability issue, and it is speculated that it is affected by the multi-linguist in some training sets.

**ZH** 我们在 Google Cloud 服务器上调用 Gemini 的 API，并对温度与 top-⟦SLOT_22⟧ 使用默认设置。需要指出的是，尽管 Gemini 目前是唯一能够执行判定的 VLM，它在使用英文文本与英文图片时，偶尔会在输出过程中说出中文或日文，如图 9 中以 Unicode 显示。虽然其语义是连贯的，即翻译后仍可使用，但这严重影响了判定的连贯性。我们认为这是一个能力问题，并推测它受到了某些训练集中多语言数据的影响。

<!-- [原子块 · svg]  -->

**EN** Figure 9: Gemini speaks Japanese.

**ZH** 图 9：Gemini 说出日文。

**EN** C.4 Other MLLMs as Judge

**ZH** C.4 以其他 MLLM 为裁判

**EN** We also use other mainstream MLLMs such as CogVLM (Wang et al., 2023c) and LLaVA (Liu et al., 2023d) for judging, which hyper-parameters follow the response generation settings. Some issues arise when we use the basic ‘‘Analyze-then-Judge’’ setting, where they cannot follow the judging instructions very well. Therefore we do not put their results into the results of the text. Recently, we have also noticed the advent of GLM-4V 22 2 https://open.bigmodel.cn/, which has shown good performance on some benchmarks and can receive long-term text and follow the instructions for judging. However, due to the time constraints, we have not completed tests on GLM-4V in our work.

**ZH** 我们还使用 CogVLM（Wang 等, 2023c）与 LLaVA（Liu 等, 2023d）等其他主流 MLLM 做判定，其超参数沿用回答生成时的设置。当我们使用基础的「先分析后判定」设定时出现了一些问题，它们无法很好地遵循判定指令，因此我们没有把其结果纳入正文结果。近来我们也注意到 GLM-4V 22 的出现，它在若干基准上表现良好，能够接收长文本并遵循判定指令。但受限于时间，我们未能在工作中完成对 GLM-4V 的测试。

**EN** Appendix D Additional Experimental Results

**ZH** 附录 D 额外实验结果

<!-- [原子块 · object]  -->

**EN** Figure 10: Comparative performance of different MLLMs across three judging settings in four newly added datasets, each is the average of three iterations.

**ZH** 图 10：不同 MLLM 在四个新增数据集、三种判定设定下的性能对比，每项均为三次迭代的平均。

<!-- [原子块 · object]  -->

**EN** Figure 11: Comparative performance of different MLLMs across three judging settings in four newly added datasets, each is the average of three iterations.

**ZH** 图 11：不同 MLLM 在四个新增数据集、三种判定设定下的性能对比，每项均为三次迭代的平均。

**EN** D.1 Full Results on Judging Performance

**ZH** D.1 判定性能的完整结果

**EN** We provide full results of judging performance of different MLLMs in Table 9. Comparative performance for four newly added datasets are shown in Figures 10 and 11.

**ZH** 我们在表 9 中给出不同 MLLM 判定性能的完整结果。四个新增数据集上的性能对比见图 10 与图 11。

**EN** In Scoring Evaluation, all models demonstrated comparable performance levels on the original dataset presented in our study, with LLaVA-1.6-34b and Qwen-vl-max slightly outperforming others in Math, Chart, and Text tasks, yet none surpassing GPT-4V. Our analysis of Qwen-vl-max and Qwen-vl-plus revealed a propensity to assign higher scores, with 80% of their ratings falling between 4-5 points, and a noticeable absence of 1-2 point scores. This inclination towards higher scores is more pronounced compared to other models. The LLaVA-1.6 series, although slightly better, also tends to award scores within the 3-5. In Pair comparison, qwen-vl-plus and max performed better on certain datasets, distinguishing themselves from competitors. Notably, qwen-vl-max exhibited less positional bias than LLaVA models, which showed a strong predisposition to favor one position, typically rating ‘A’ as better. n Batch Ranking, the updated Gemini-Pro-Vision model outperforms others overall. Both Qwen and LLaVA series demonstrated that larger model sizes correlate with better outcomes, affirming a strong scaling law effect. Despite these findings, there remains a noticeable gap between these models and the top-performing GPT-4V, particularly concerning positional bias.

**ZH** 在评分评测中，所有模型在我们研究所用的原始数据集上表现出相近的水平，其中 LLaVA-1.6-34b 与 Qwen-vl-max 在数学、图表与文本任务上略胜一筹，但都未能超过 GPT-4V。我们对 Qwen-vl-max 与 Qwen-vl-plus 的分析显示，它们倾向于给出更高的分数：其 80% 的评分落在 4–5 分之间，且明显缺少 1–2 分的评分。这种打高分的倾向比其他模型更为突出。LLaVA-1.6 系列虽略好一些，也倾向于给出 3–5 分。在成对比较中，qwen-vl-plus 与 max 在部分数据集上表现更好，从竞争者中脱颖而出。值得注意的是，qwen-vl-max 表现出的位置偏差小于 LLaVA 模型，后者强烈倾向于偏爱某一位置，通常认为「A」更好。在批量排序中，更新后的 Gemini-Pro-Vision 模型总体优于其他模型。Qwen 与 LLaVA 两个系列都显示出模型规模越大结果越好，印证了显著的缩放定律效应。尽管有这些发现，这些模型与表现最好的 GPT-4V 之间仍存在明显差距，在位置偏差上尤为突出。

**EN** Table 9: The overall performance of different MLLMs in judging, compared with human annotations on different datasets. We sample all the data three times and took the average to mitigate the casualty. w. and w.o. tie represents tie and non-tie situations respectively. We omit Gemini’s results on the diffusion task for its challenges in processing AI-generated images. All presented data of Pearson similarity exhibit a ⟦SLOT_23⟧-value below 0.05, indicating a statistically significant level of confidence. Notice: Gemini-Pro∗ means Gemini-1.0-Pro-latest.

**ZH** 表 9：不同 MLLM 在判定上的总体表现，与各数据集上的人工标注相对照。我们对全部数据采样三次并取平均，以降低偶然性。w. 与 w.o. tie 分别表示有平局与无平局的情形。因 Gemini 在处理 AI 生成图像上存在困难，我们略去其在扩散任务上的结果。所有给出的皮尔逊相似度数据的 ⟦SLOT_23⟧ 值均低于 0.05，表明具有统计学显著水平的置信度。注意：Gemini-Pro∗ 表示 Gemini-1.0-Pro-latest。

<!-- [原子块 · table] Settings MLLM COCO C.C. Diff. Graphics Math Text WIT Chart VisIT CC-3M M2W SciQA Aes MM-Vet Ave. Score ( ↑ \uparrow ) CogVLM 0.107 -0.048 0.049 -0.158 0.065 0.097 -0.131 -0.135 0.278 0.157 - - - - 0.0 -->

**EN** D.2 Judging Results on Sequential Images

**ZH** D.2 序列图像上的判定结果

**EN** We incorporated the sequential image dataset Mementos, comprising picture sequences, to expand our MLLM-as-a-Judge framework into the video domain in a pioneering effort. Each sequence, featuring over four images, draws from daily life, comics, and robotics. For data generation in Step 3, we utilized GPT-4V, Qwen-VL-Max, Qwen-VL-Plus, and Video-LLM Chatunivi, obtaining 100 image-text pairs for batch evaluations, 381 for scoring, and 560 for pair comparisons. Beyond analyzing GPT-4V and Qwen-vl-max, we explored Video-LLM’s judging capabilities, specifically testing it with ChatUnivi.

**ZH** 我们纳入了由图片序列构成的时序图像数据集 Mementos，首次把 MLLM-as-a-Judge 框架拓展到视频领域。每个序列包含四张以上图像，取材自日常生活、漫画与机器人。在步骤 3 的数据生成中，我们使用了 GPT-4V、Qwen-VL-Max、Qwen-VL-Plus 与 Video-LLM Chatunivi，得到用于批量评测的图像—文本对 100 个、用于评分的 381 个、用于成对比较的 560 个。除分析 GPT-4V 与 Qwen-vl-max 之外，我们还探索了 Video-LLM 的判定能力，具体以 ChatUnivi 进行测试。

**EN** As illustrated in Table 10 for Batch Evaluation, Pair Comparison, and Score Evaluation respectively, our findings indicate that GPT-4V significantly outperforms other models on sequential data. Despite the high-quality responses generated by the Video-LLM ChatUnivi we evaluated, it fundamentally lacks the judging capability and consistency.

**ZH** 如表 10 中分别针对批量评测、成对比较与评分评测所示，我们的发现表明 GPT-4V 在序列数据上显著优于其他模型。尽管我们所评测的 Video-LLM ChatUnivi 生成了高质量的回答，它从根本上缺乏判定能力与一致性。

**EN** Table 10: Judging performance on image sequence dataset Mementos.

**ZH** 表 10：在图像序列数据集 Mementos 上的判定性能。

<!-- [原子块 · table] MLLM Score ( ↑ \uparrow ) Pair ( ↑ \uparrow ) Batch ( ↓ \downarrow ) Pearson w. Tie w.o. Tie Edit Dis. GPT-4V 0.361 0.721 0.836 0.411 ChatUnivi -0.094 0.158 0.168 0.556 Qwen-vl-plus 0.115 0.426 0.482  -->

**EN** D.3 Preliminary Experiment

**ZH** D.3 预备实验

**EN** Human Agreement on GPT-4V Output Mode. The recently introduced ‘Json Mode’33 3 https://openai.com/blog/new-models-and-developer-products-announced-at-devday in GPT-4V represents a significant advancement, particularly in structuring outputs in JSON format while restricting token usage. This mode has been observed to regularize responses, a feature particularly advantageous when dealing with structured data. However, this structuring tends to compartmentalize responses, potentially leading to a loss in the natural flow and contextual linkage typically inherent in human-like responses. This segmentation might inadvertently affect the readability and perceived coherence of the generated text.

**ZH** 关于 GPT-4V 输出模式的人类认同度。GPT-4V 中最近引入的「Json Mode」33 是一项重要进展，尤其在以 JSON 格式结构化输出并限制 token 用量方面。据观察，该模式能使回答更规整，这一特性在处理结构化数据时尤为有利。然而，这种结构化倾向会把回答切割成块，可能导致类人回答中固有的自然流畅与语境衔接有所损失。这种切分可能不经意间影响生成文本的可读性与感知连贯性。

**EN** To quantitatively assess the impact of Json Mode on output quality and its alignment with human preferences, we meticulously construct a test set. This set comprises 50 data instances, randomly selected from three distinct datasets used for evaluation purposes. The objective is to discern human evaluators’ predilection for the outputs generated in Json Mode by GPT-4V.

**ZH** 为定量评估 Json Mode 对输出质量及其与人类偏好契合度的影响，我们精心构建了一个测试集。该集合包含 50 条数据实例，随机选自用于评测的三个不同数据集。目标是辨明人类评估者对 GPT-4V 在 Json Mode 下生成输出的偏好。

**EN** For a comprehensive analysis, we engage three annotators, each responsible for labeling the data. Their assessments aim to discern the balance between structured, JSON-formatted responses and the inherently fluid nature of human judgment and preference in textual content, as shown in Figure 12.

**ZH** 为做全面分析，我们请三位标注者各自负责标注数据。他们的评估旨在辨明结构化的 JSON 格式回答与人类判断及文本偏好天然流畅性之间的平衡，如图 12 所示。

<!-- [原子块 · object]  -->

**EN** Figure 12: Json Mode Preference Analysis.

**ZH** 图 12：Json Mode 偏好分析。

**EN** Human Agreement Bias Checking Acknowledging the inherent variability in human annotations, we embark on an empirical study involving ten annotators to ascertain the reliability of derived statistical patterns, notwithstanding the subjective nature of human judgment. This study aims to mitigate the individual biases that might skew the evaluation of GPT-4’s outputs. A dataset comprising 50 entries, processed using the GPT-4 pair comparison setting, serves as the foundation for this investigation.

**ZH** 人类认同度偏差检验。考虑到人工标注固有的变异性，我们开展了一项涉及十位标注者的实证研究，以确定所导出统计模式的可靠性，尽管人类判断具有主观性。本研究旨在减轻可能扭曲对 GPT-4 输出评估的个体偏差。一个包含 50 条、经 GPT-4 成对比较设定处理的条目的数据集构成了这项检验的基础。

**EN** The results, detailed in Figure 13, underscore a noteworthy observation: while the annotators exhibit minimal variance in determining the correctness of GPT-4’s judgments, a discernible divergence emerged in the scoring of analytical responses. This divergence presumably stems from individual perceptual differences and inherent biases. However, it’s crucial to note that these discrepancies in scoring did not significantly compromise the overall integrity of the annotations.

**ZH** 如图 13 所示的结果凸显了一个值得注意的现象：尽管标注者在判断 GPT-4 判定是否正确上的差异很小，在对分析性回答打分时却出现了明显分歧。这种分歧大概源自个体感知差异与固有偏差。然而，关键在于这些评分上的差异并未显著损害标注的整体完整性。

**EN** A remarkable consensus is observed in the labeling of hallucinations. The employment of a meticulously defined decision tree for identifying hallucinations ensures a high degree of uniformity across the annotations. This structured approach substantially minimizes errors, underscoring the effectiveness of well-defined criteria in achieving consistent and reliable annotations across different individuals.

**ZH** 在幻觉标注上观察到了高度一致。由于采用了精心定义的决策树来识别幻觉，标注之间保持了高度统一。这一结构化方法大幅减少了错误，说明了定义良好的准则在跨个体实现一致、可靠标注上的有效性。

<!-- [原子块 · object]  -->

**EN** (a) The distribution of Human Annotators’ ratings for the data.

**ZH** (a) 人类标注者对数据的评分分布。

<!-- [原子块 · object]  -->

**EN** (b) Human Labeling and Agreement Bias Checking.

**ZH** (b) 人工标注与认同度偏差检验。

**EN** Figure 13: Human Labeling and Agreement Bias.

**ZH** 图 13：人工标注与认同度偏差。

**EN** D.4 Length Distribution on MLLM Judgments Analysis

**ZH** D.4 MLLM 判定中的长度分布分析

**EN** In our analysis, we have included length distribution diagrams that showcase the differences in the responses provided by GPT-4V and Gemini during their judgment tasks as illustrated in Figure 14. These diagrams reveal that GPT-4V typically generates longer responses than Gemini in both Scoring Evaluation (Figure 15) and Pair Comparison (Figure 16), whereas in the batch task (Figure 17), the output lengths from both models are comparatively similar.

**ZH** 在分析中，我们给出了长度分布图，展示 GPT-4V 与 Gemini 在判定任务中所提供回答的差异，如图 14 所示。这些图揭示：在评分评测（图 15）与成对比较（图 16）中，GPT-4V 通常生成比 Gemini 更长的回答；而在批量任务（图 17）中，两个模型的输出长度相对接近。

<!-- [原子块 · object]  -->

**EN** Figure 14: Length distribution in analysis collections.

**ZH** 图 14：分析集合中的长度分布。

<!-- [原子块 · object]  -->

**EN** Figure 15: Response length distribution in Scoring Evaluation. The horizontal axis represents length, and the vertical axis represents density.

**ZH** 图 15：评分评测中的回答长度分布。横轴表示长度，纵轴表示密度。

<!-- [原子块 · object]  -->

**EN** Figure 16: Response length distribution in Pair Comparison.

**ZH** 图 16：成对比较中的回答长度分布。

<!-- [原子块 · object]  -->

**EN** Figure 17: Response length distribution in Batch Ranking.

**ZH** 图 17：批量排序中的回答长度分布。

**EN** D.5 Results on Human Scoring and Ego Bias

**ZH** D.5 人类评分与自我偏差上的结果

**EN** We employ the Mean Absolute Deviation (MAD) metric to assess the consistency of MLLM judging quality across multiple responses to a single image-instruction pair, as shown in 18.

**ZH** 我们采用平均绝对偏差（MAD）指标来评估 MLLM 对同一图像—指令对的多个回答在判定质量上的一致性，如图 18 所示。

<!-- [原子块 · object]  -->

**EN** Figure 18: MAD of Human Scoring on MLLM Judgments Analysis.

**ZH** 图 18：MLLM 判定分析上人类评分的 MAD。

**EN** The Egocentric Bias of different models are shown in Figures 19 and 20.

**ZH** 不同模型的自我中心偏差见图 19 与图 20。

<!-- [原子块 · object]  -->

**EN** Figure 19: Scoring Density of Different MLLMs in Judging.

**ZH** 图 19：不同 MLLM 在判定中的评分密度。

<!-- [原子块 · object]  -->

**EN** Figure 20: The proportion of different responses chosen by humans and different MLLMs in Tie Scenario and Non-Tie Scenario.

**ZH** 图 20：在有平局与无平局情形下，人类与各 MLLM 选择不同回答的比例。

**EN** Appendix E Human Labeling and Agreement Collection

**ZH** 附录 E 人工标注与认同度采集

**EN** The annotation is conducted by 6 authors of this paper independently. As acknowledged, the diversity of annotators plays a crucial role in reducing bias and enhancing the reliability of the benchmark. These annotators have knowledge in this domain, with different genders, ages, and educational backgrounds. To ensure the annotators can proficiently mark the data, we provide them with detailed tutorials, teaching them how to evaluate model responses more objectively. Specifically, they are required to give judgments without considering answer lengths, and certain names or positions of the response. Besides, we implement cross-validation between different annotators and conduct continuous monitoring to ensure they are maintaining objectivity and fairness.

**ZH** 标注由本文 6 位作者独立完成。众所周知，标注者的多样性在降低偏差、提升基准可靠性方面起着关键作用。这些标注者具备本领域的知识，且性别、年龄与教育背景各异。为确保标注者能够熟练地标注数据，我们为他们提供了详细的教程，教他们如何更客观地评估模型回答。具体地，他们被要求在不考虑回答长度以及回答中特定名称或位置的情况下作出判定。此外，我们在不同标注者之间实施交叉验证，并持续监控，以确保他们保持客观与公正。

**EN** In the Human agreement experiment performed by humans on MLLM Judge, the prompt we give humans is presented in Figure 21 and Figure 22.

**ZH** 在由人类对 MLLM 裁判执行的人类认同度实验中，我们给人类使用的提示词见图 21 与图 22。

<!-- [原子块 · img]  -->

**EN** Figure 21: Human agreement

**ZH** 图 21：人类认同度

<!-- [原子块 · img]  -->

**EN** Figure 22: Human labeling

**ZH** 图 22：人工标注

<!-- [原子块 · svg]  -->

**EN** Appendix F Prompt Templates

**ZH** 附录 F 提示词模板

**EN** We first query Judge VLM to get their responses by the following prompts.

**ZH** 我们首先通过以下提示词查询裁判 VLM 以获得其回答。

<!-- [原子块 · svg]  -->

**EN** Following Chiang & Lee (2023b) and Li et al. (2024), we have designed prompts and presented the prompt template of VLM’s operation including score, pair comparison, and batch ranking judgments in a prompt template as system prompt, instruction, criteria, noticement, and desired output form:

**ZH** 沿用 Chiang & Lee（2023b）与 Li 等（2024），我们设计了提示词，并把 VLM 操作（包括评分、成对比较与批量排序判定）的提示模板呈现为系统提示、指令、准则、注意事项与期望输出形式：

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

**EN** Appendix G Case Study

**ZH** 附录 G 案例研究

**EN** We list several case studies. Assistant A, B, C, D represent LlaVA, CogVLM, GPT-4V and Gemini, respectively. Judge VLM 1 and 2 represent Gemini and GPT-4V, respectively. For pair comparison, the judge result “C” means a tie.

**ZH** 我们列出若干案例研究。助手 A、B、C、D 分别表示 LlaVA、CogVLM、GPT-4V 与 Gemini。裁判 VLM 1 与 2 分别表示 Gemini 与 GPT-4V。对成对比较，判定结果「C」表示平局。

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->
