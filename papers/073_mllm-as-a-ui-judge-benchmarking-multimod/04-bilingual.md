# MLLM 作为 UI 评判者：面向预测人类用户界面感知的多模态大语言模型基准评测

> 原标题：MLLM as a UI Judge: Benchmarking Multimodal LLMs for Predicting Human Perception of User Interfaces
> 作者：Reuben A. Luera, Ryan Rossi, Franck Dernoncourt, Samyadeep Basu, Sungchul Kim, Subhojyoti Mukherjee, Puneet Mathur, Ruiyi Zhang, Jihyung Kil, Nedim Lipka, Seunghyun Yoon, Jiuxiang Gu 等 · arXiv:2510.08783 · 2025-10-09

<!-- [原子块 · verbatim] MLLM as a UI Judge: Benchmarking Multimodal LLMs for Predicting Human Perception of User Interfaces -->

<!-- [原子块 · verbatim] Abstract. -->

<!-- [原子块 · verbatim] In an ideal design pipeline, user interface (UI) design is intertwined with user research to validate decisions, yet studies are often resource-constrained during early exploration. Recent advances in -->

**EN** Keywords:

**ZH** 关键词：

**EN** 1. Introduction

**ZH** 1. 引言

**EN** Design choices are inseparable from usability and experience. Nowhere is this more evident than in interface design, which shapes user perception of product usability and trustworthiness (Reinecke et al. 2013). It can even profoundly impact user productivity, and their emotional responses to products (Bhandari et al. 2017; Bailey et al. 1988). For this reason, user experience research to evaluate interface design is crucial for development (Steen et al. 2007; Baxter et al. 2015). Through research-informed iterations upon design choices, products can be refined to be more usable, engaging, and trustworthy.

**ZH** 设计选择与可用性和体验密不可分。这一点在界面设计中体现得最为明显——界面塑造了用户对产品可用性与可信度的感知（Reinecke et al. 2013），甚至能深刻影响用户的工作效率及其对产品的情绪反应（Bhandari et al. 2017; Bailey et al. 1988）。因此，用以评估界面设计的用户体验研究对产品开发至关重要（Steen et al. 2007; Baxter et al. 2015）。通过以研究为依据对设计选择作迭代，产品可以被打磨得更可用、更吸引人、更值得信赖。

**EN** However, many organizations face a persistent bottleneck, where too few researchers are available to keep pace with the growing scale of design and evaluation needs. In fact, according to a report from the Nielsen Norman Group, there is only one researcher for every five designers (Kaplan 2020). As a result, many organizations are forced to allocate their limited research capacity selectively, testing only a small subset of ideas rather than engaging in rapid, iterative evaluation, which has long been shown to significantly enhance design quality (Medlock 2018).

**ZH** 然而，许多组织面临一个长期存在的瓶颈：研究人员太少，跟不上设计与评估需求不断增长的规模。事实上，根据 Nielsen Norman Group 的一份报告，每五名设计师才对应一名研究人员（Kaplan 2020）。结果是，许多组织被迫有选择地分配有限的研究能力，只测试一小部分想法，而无法开展快速的迭代式评估——而后者早已被证明能显著提升设计质量（Medlock 2018）。

**EN** Existing work in this space simulates human behavior in domains like e-commerce and solely focuses on user metrics like click-through and conversion rates (Wang 2025), which can be limited because such metrics capture only general user outcomes and fail to provide diagnostic insights into design quality, usability, or user experience. To address this gap, artificial intelligence offers a promising avenue for building more efficient and scalable evaluation pipelines. Several existing works have examined how large language models (LLMs) can be used to evaluate UIs, such as generating feedback based on critiques and quality ratings from professional designers (Duan et al. 2024a; Duan et al. 2024b). While LLMs can be trained to generate feedback on UIs, prior work shows that they often struggle to faithfully capture human responses to visual interfaces (Wang et al. 2024; Stokes et al. 2025). We build on this work by systematically comparing LLM evaluations with human-generated UI evaluation data, in order to identify both reliable alignments and critical misalignments that highlight future research opportunities. Through this comparison, we identify the LLM prompting approach that most effectively approximates human judgments.

**ZH** 该领域现有的工作主要模拟电商等场景中的人类行为，只关注点击率、转化率等用户指标（Wang 2025），其局限在于这类指标只能捕捉笼统的用户结果，无法就设计质量、可用性或用户体验给出诊断性的洞察。为弥补这一缺口，人工智能为构建更高效、更可扩展的评估流水线提供了颇具前景的途径。已有若干工作考察了如何用大语言模型（LLM）评估 UI，例如基于专业设计师的评语与质量评分生成反馈（Duan et al. 2024a; Duan et al. 2024b）。虽然 LLM 可被训练成针对 UI 生成反馈，但前人工作表明，它们往往难以忠实捕捉人类对视觉界面的反应（Wang et al. 2024; Stokes et al. 2025）。本文在这条线上继续推进：系统地把 LLM 的评估结果与人类生成的 UI 评估数据作比较，以识别可靠的吻合之处与关键的错位之处，后者正凸显了未来的研究机会。通过这一比较，我们找出了最能逼近人类判断的 LLM 提示方法。

**EN** Further, the analysis presented in this paper, specifically how state-of-the-art models perform moderately well in UI judging tasks, can lay the groundwork for using multimodal large language models (MLLMs) to supplement early-stage user research. The results produced can be summarized in the following way: 1) Task 1, the Likert-scale task produced human and MLLM evaluation scores that, when compared to one another, show promise for MLLMs as UI judge approximators. The models we use (Claude 3.5 Sonnet, GPT-4o, and Llama-3.2-11B-Vision-Instruct) all have an accuracy ⟦SLOT_0⟧ score greater than 75%. Further, we evaluated performance using Pearson, Spearman, and Kendall tau correlation statistics that signify a moderately strong correlation between MLLM and human scores. 2) Task 2, the pairwise comparison task, reflected that MLLMs, when given questions that have large human score differences, can accurately simulate human data. In these pairwise experiments, we saw largely that models’ performance improved as the degree of difference between two screens increased. Given this, MLLMs are not at a stage where they should be seen as replacements for real-life human evaluation, but instead can be used to supplement early UI evaluations, especially in scenarios where UIs would remain untested.

**ZH** 此外，本文所呈现的分析——特别是当前最先进模型在 UI 评判任务上表现中等偏上的结论——可以为使用多模态大语言模型（MLLM）补充早期用户研究奠定基础。所得结果可概括如下：1）任务 1（Likert 量表任务）产出了人类与 MLLM 的评分，二者对比显示 MLLM 作为 UI 评判代理颇具前景。我们所用的模型（Claude 3.5 Sonnet、GPT-4o 与 Llama-3.2-11B-Vision-Instruct）的准确率 ⟦SLOT_0⟧ 得分均超过 75%。进一步地，我们用 Pearson、Spearman 与 Kendall tau 相关统计量评估性能，结果显示 MLLM 与人类分数之间存在中等偏强的相关性。2）任务 2（成对比较任务）反映出，当所给问题在人类分数上差异较大时，MLLM 能够准确模拟人类数据。在这些成对实验中，我们大体观察到模型的性能随两个界面之间差异程度的增大而提升。有鉴于此，MLLM 尚未成熟到可以替代真实的人类评估，而应被用于补充早期 UI 评估，尤其是在那些界面本来不会被测试的场景下。

**EN** Summary of Main Contributions. The key contributions of this work are as follows:

**ZH** 主要贡献概述。 本文的关键贡献如下：

**EN** • Novel MLLM as a judge evaluation tasks: We introduce a new task that can be used to evaluate whether large language multimodal models can approximate human preferences and provide reasonable justifications of those preferences in Likert scale evaluations of UIs and pairwise comparisons of real-world interfaces—moving beyond behavioral simulation to subjective UI alignment.

**ZH** • 新颖的「MLLM 作为评判者」评估任务：我们提出一项新任务，可用于评估多模态大语言模型能否逼近人类偏好，并在 UI 的 Likert 量表评分与真实世界界面的成对比较中就这些偏好给出合理依据——从行为模拟走向主观的 UI 一致性。

**EN** • Absolute Human/MLLM UI judgments benchmark11 1 See supplementary materials for benchmark data: Task 1 (Section 4.1) produced a benchmark dataset of user interface evaluations, derived from both MLLM and human evaluators. This dataset was created by showing humans and three state-of-the-art MLLMs (Claude 3.5 Sonnet, GPT-4o, and Llama-3.2-11B-Vision-Instruct) the same set of UIs and then asking them to use a list of cognitive, perceptual, and emotional factors to evaluate them on a scale from 1-7.

**ZH** • 绝对式人类／MLLM UI 判断基准11 1 基准数据见补充材料：任务 1（第 4.1 节）产出了一份用户界面评估基准数据集，来自 MLLM 与人类评估者双方。该数据集的构建方式是：向人类与三个当前最先进的 MLLM（Claude 3.5 Sonnet、GPT-4o 与 Llama-3.2-11B-Vision-Instruct）展示同一组 UI，然后要求他们依据一份认知、感知与情感因素清单，在 1–7 的量表上对其评分。

**EN** • Pairwise Human/MLLM UI judgments benchmark1: Task 2 (Section 4.2) produced a benchmark of pairwise MLLM and human evaluations of user interfaces. To create this data, we showed the same three state-of-the-art MLLMs two UIs at a time and prompted them to choose their preferred screen based on the same list of factors. The MLLM data was then compared to human pairwise data (generation techniques shown in Section 4.2) to calculate another dataset of agreement scores.

**ZH** • 成对式人类／MLLM UI 判断基准1：任务 2（第 4.2 节）产出了一份 UI 的成对 MLLM 与人类评估基准。为构建该数据，我们向同样的三个当前最先进的 MLLM 每次展示两个 UI，并提示它们依据同一份因素清单选出更偏好的界面；随后把 MLLM 数据与人类成对数据（生成方法见第 4.2 节）作比较，计算出另一组一致率数据。

**EN** • MLLM training data: The data produced in this study can be used as the benchmark to create a fine-tuned model. Training MLLMs and LLMs with novel datasets, such as the one created in this study, has proven to increase human accuracy in MLLM as a judge tasks (Kim et al. 2024; Ziegler et al. 2020; Lee et al. 2024).

**ZH** • MLLM 训练数据：本研究产出的数据可作为基准用于构建微调模型。用本研究这类新数据集训练 MLLM 与 LLM，已被证明能提升「MLLM 作为评判者」任务中与人类的一致性（Kim et al. 2024; Ziegler et al. 2020; Lee et al. 2024）。

**EN** • MLLM as a UI judge use cases: Data analysis that suggests that MLLMs are a capable tool to supplement user interface testing for both absolute score testing and pairwise comparison to gauge perception at early stages. Our data suggest that teams with limited resources can use MLLMs to supplement, rather than fully replace, human UI testing.

**ZH** • 「MLLM 作为 UI 评判者」的使用场景：数据分析表明，MLLM 是补充用户界面测试的有效工具，既可用于绝对分数测试，也可用于成对比较，以在早期阶段衡量感知。我们的数据提示，资源有限的团队可用 MLLM 来补充、而非完全替代人类 UI 测试。

**EN** The novelty of this research lies in the exploration of whether or not multimodal LLMs can evaluate visual user interfaces, not just text or other behavioral logs. Past LLM as a judge work has largely centered on comparing human and LLM textual evaluations (Das et al. 2025); we instead focus our work on visual UI evaluation. Through this study, we evaluate whether or not MLLMs are capable of emulating human UI judgments and report when they do so well and when they fail. In doing so, we explore to what degree MLLMs can be used as early-stage, low-cost approximators that act as a supplement, not as a replacement, to existing user research.

**ZH** 本研究的新颖之处在于探讨多模态 LLM 能否评估视觉用户界面，而不仅是文本或其他行为日志。以往的「LLM 作为评判者」工作主要聚焦于比较人类与 LLM 的文本评估（Das et al. 2025）；我们则把重心放在视觉 UI 评估上。通过本研究，我们评估 MLLM 是否有能力模拟人类的 UI 判断，并报告它们在何种情形下表现良好、在何种情形下失败。在此过程中，我们探究 MLLM 在多大程度上可被用作早期、低成本的近似器，作为现有用户研究的补充而非替代。

**EN** 2. Related Work

**ZH** 2. 相关工作

**EN** 2.1. LLM-as-a-Judge

**ZH** 2.1. LLM 作为评判者

**EN** Extensive work has been done in the field of ’LLM as a Judge’, and within this paper, we aim to build upon the existing literature. LLM as a judge is a concept that can be applied to a myriad of different domains (Gu et al. 2024) and consists of using LLMs to evaluate the outcomes of complex tasks. They can do so effectively because they can quickly and efficiently process extensive datasets that can then be used to make an informed decision (Achiam et al. 2023). LLMs have been used as judges to evaluate everything from other models (Li et al. 2023; Wang et al. 2023; Zhang et al. 2023; Zheng et al. 2023), natural language and information (Wang et al. 2022; Ramamurthy et al. 2022; Ouyang et al. 2022), charts (Kim et al. 2025), and reasoning and thinking (Achiam et al. 2023; Team et al. 2023; Guo et al. 2025). Despite this, related literature suggests that using LLMs as judges can offer cost-cutting and a flexible alternative to human evaluation, but warns that they often lack consistency while suffering from issues pertaining to bias and reliability (Gu et al. 2024).

**ZH** 「LLM 作为评判者」这一领域已有大量工作，本文旨在在既有文献之上继续推进。LLM 作为评判者是一个可应用于众多不同领域的概念（Gu et al. 2024），指的是用 LLM 来评估复杂任务的结果。它们之所以能有效地做到这一点，是因为可以快速高效地处理大量数据，进而据以作出有依据的判断（Achiam et al. 2023）。LLM 已被用作评判者，评估的对象包罗万象：从其他模型（Li et al. 2023; Wang et al. 2023; Zhang et al. 2023; Zheng et al. 2023），到自然语言与信息（Wang et al. 2022; Ramamurthy et al. 2022; Ouyang et al. 2022）、图表（Kim et al. 2025），再到推理与思维（Achiam et al. 2023; Team et al. 2023; Guo et al. 2025）。尽管如此，相关文献指出，用 LLM 作评判者虽能提供节省成本、灵活的人类评估替代方案，但也警告它们常缺乏一致性，并存在偏见与可靠性方面的问题（Gu et al. 2024）。

**EN** Across all studied domains, larger state-of-the art models (e.g., GPT-4o, Claude, etc.) perform better in LLM as a judge tasks than smaller models (Thakur et al. 2025; Zheng et al. 2023). Nonetheless, even well-performing models deviate by up to five points on a 10-point scale, and LLM evaluators are often excessively verbose, biased towards the existing positions, and prefer their own outputs (Liu et al. 2024; Panickssery et al. 2024). Given these limitations, LLMs often are capable as approximators, but are far from being human replacements in evaluation tasks.

**ZH** 在所考察的全部领域中，规模更大的当前最先进模型（如 GPT-4o、Claude 等）在「LLM 作为评判者」任务上的表现优于更小的模型（Thakur et al. 2025; Zheng et al. 2023）。尽管如此，即便表现良好的模型在 10 分制上也会有高达五分的偏差；而且 LLM 评估者往往过于冗长、偏向既有立场，并偏爱自己的输出（Liu et al. 2024; Panickssery et al. 2024）。鉴于这些局限，LLM 常常能胜任近似器的角色，但在评估任务中远不足以替代人类。

**EN** We aim to distinguish our work by using a method that specifically explores how MLLMs can be used to evaluate two distinct UIs. In the context of this paper, we use a pairwise MLLM evaluation method (Liu et al. 2024), which consists of having the MLLM compare two different options and selecting which is better aligned with a predetermined criterion (Gu et al. 2024; Qin et al. 2024). This method closely aligns with A/B testing, commonly used in user research to compare two interfaces. We aim to run a pairwise test with human users looking at UIs and a Likert-scale LLM evaluation with the same interfaces to explore how close LLMs are to simulating human results.

**ZH** 我们力求通过一种专门探究 MLLM 如何被用于评估两个不同 UI 的方法，来体现本工作与以往的区别。在本文中，我们采用成对 MLLM 评估方法（Liu et al. 2024），即让 MLLM 比较两个不同选项，并选出与预设准则更吻合的一个（Gu et al. 2024; Qin et al. 2024）。该方法与用户研究中常用于比较两个界面的 A/B 测试高度契合。我们的目标是：让人类用户对 UI 做成对测试，同时对同样的界面做 Likert 量表式 LLM 评估，以探究 LLM 在多大程度上接近人类的结果。

<!-- [原子块 · img]  -->

**EN** Figure 1. User interfaces split by domains: An overview of a sample of the UIs evaluated by humans and MLLMs can be divided into three domains: landing pages, digital receipts, and catalogs. Here we present low-fidelity versions of the screens that we presented to the users. The users saw high-fidelity, branded, and in-product versions of these screens that have been anonymized.

**ZH** 图 1. 按领域划分的用户界面：受人类与 MLLM 评估的 UI 样本概览，可分为三个领域——落地页、数字收据与商品目录。此处呈现的是展示给用户时所用界面的低保真版本；用户看到的是经过匿名化处理的高保真、带品牌标识的产品内版本。

**EN** 2.2. MLLMs in User Research and Design

**ZH** 2.2. 用户研究与设计中的 MLLM

**EN** As in many other domains, AI is becoming increasingly intertwined with user interface design and research (Bertão and Joo 2021; Luera et al. 2024). Designers and researchers alike are using MLLM to create and explore different interfaces for their respective products. Specifically in design research, LLMs are being used as assistants that are able to collaborate during UX evaluation sessions (Kuang et al. 2024). LLMs are occasionally being used to create synthetic data that emulates human users (Cao et al. 2025; Rosala and Moran 2024; Luera et al. 2025). For instance, Jansen et al. 2023 explain how LLMs can use simulated respondents to supplement the creation and analysis of survey research. Further, Hämäläinen et al. 2023 demonstrates that LLMs are capable of simulating user survey responses and creating responses that humans found plausible. Similarly, Li et al. 2024 found that in larger-scale market research surveys, LLM-generated survey responses achieved about a 75%-85% agreement with results from actual humans. However, this paper also highlights the importance of these models being trained on human data, as they cannot yet capture all of the nuances of human users.

**ZH** 与许多其他领域一样，AI 正日益与用户界面设计和研究交织在一起（Bertão and Joo 2021; Luera et al. 2024）。设计师与研究者都在用 MLLM 为各自的产品创建并探索不同的界面。具体在设计研究方面，LLM 正被用作能够在 UX 评估环节中协同工作的助手（Kuang et al. 2024）；LLM 偶尔也被用于创建模拟人类用户的合成数据（Cao et al. 2025; Rosala and Moran 2024; Luera et al. 2025）。例如，Jansen et al. 2023 说明了 LLM 如何利用模拟受访者来辅助调查研究的创建与分析；Hämäläinen et al. 2023 则证明 LLM 能够模拟用户调查回答，并生成人类认为合理的答复。类似地，Li et al. 2024 发现，在较大规模的市场调研问卷中，LLM 生成的问卷回答与真实人类的结果达到约 75%–85% 的一致率。不过该论文也强调，这些模型必须在人类数据上训练，因为它们尚无法捕捉人类用户的全部细微之处。

**EN** There have been some work focused on some aspect of UI evaluations (Duan et al. 2024b; Duan et al. 2024a; Wu et al. 2024; Schoop et al. 2022). In Duan et al. 2024b, a Figma plugin was created by assessing GPT-4’s alignment with a set of design heuristics. Similarly, Duan et al. 2024a utilized a dataset of design critiques from several experienced designers to improve LLM-generated UI feedback by 55%. Meanwhile Wu et al. 2024 creates a design tool based on several datasets and shows it performs closely to human ground truth. In addition, Xiang et al. 2024 created an LLM tool used to evaluate smartwatch interfaces using simulated users. Our work differs from these works as we create a benchmark that compares several different state-of-the-art MLLMs to each other and to the human judgments. Further, the benchmark reflects how MLLMs perform in both pairwise and absolute scoring tasks based on a list of nine UI factors. Agent A/B (Wang 2025) asks a similar question and explores whether or not its own model can complete A/B UX tests. They train their agent specifically on UX click-through rate, focusing solely on the filters and menus of e-commerce websites. We aim to focus on a broader question, exploring UI judgments at a higher level while testing an assortment of widely used MLLMs (e.g., GPT-4o, Claude, Gemini) on an assortment of UI screens from different domains.

**ZH** 也有一些工作聚焦于 UI 评估的某些方面（Duan et al. 2024b; Duan et al. 2024a; Wu et al. 2024; Schoop et al. 2022）。在 Duan et al. 2024b 中，作者通过评估 GPT-4 与一组设计启发式的吻合度，开发了一个 Figma 插件。类似地，Duan et al. 2024a 利用来自多位资深设计师的设计评语数据集，把 LLM 生成的 UI 反馈质量提升了 55%。与此同时，Wu et al. 2024 基于若干数据集创建了一个设计工具，并展示其性能接近人类真值。此外，Xiang et al. 2024 开发了一个用模拟用户评估智能手表界面的 LLM 工具。我们的工作与这些工作的不同之处在于：我们构建了一个基准，把若干不同的当前最先进 MLLM 相互比较，并与人类判断作比较；而且该基准反映的是 MLLM 在基于九项 UI 因素清单的成对与绝对评分任务上的表现。Agent A/B（Wang 2025）提出了类似的问题，探索其自身模型能否完成 A/B 用户体验测试；他们专门针对 UX 点击率训练智能体，只关注电商网站的筛选器与菜单。我们的目标是聚焦一个更宽泛的问题：在更高层面上探索 UI 判断，同时在来自不同领域的一系列 UI 界面上测试一批广泛使用的 MLLM（如 GPT-4o、Claude、Gemini）。

**EN** 3. Study Methodology

**ZH** 3. 研究方法

**EN** 3.1. UI Collection

**ZH** 3.1. UI 采集

**EN** In order to quickly curate a diverse set of user interfaces, we used pre-made interfaces from a professional UI dataset22 2 https://reallygoodemails.com/. We selectively identified 30 UIs (24 professionally made and 6 made from scratch) across three different categories: browsing & discovery, confirmation & feedback, and communication & engagement (Figure 1) to cover a diverse set of UI components, aesthetic styles, content complexity, quality, and purposes. For instance, communication & engagement UIs typically have large images and eye-catching text in order to grab the attention of the user. Meanwhile, screens from the confirmation & feedback category typically have more text because their purpose is to quickly provide payment information, and catalogs often have pairs of images and text. We aimed to choose UIs that could work on both mobile and desktop devices and put constraints on the height so that most screens were about similar dimensions. For the most part, all UIs were extracted as is from the dataset. Since these screens were made by professional designers, we reduced the build quality of some screens to maintain a diverse dataset of both high and low quality designs. Since the UIs were collected from a professionally made dataset, we anticipated that most scores, both human and AI, would skew higher and more positively. For this reason, we designed our pairwise and ranking tasks with stronger granularity to detect signals in our measurements.

**ZH** 为快速策管一组多样化的用户界面，我们使用了一个专业 UI 数据集22 2 https://reallygoodemails.com/ 中的预制界面。我们有选择地确定了 30 个 UI（24 个专业制作、6 个从零制作），横跨三个不同类别：浏览与发现、确认与反馈、以及沟通与互动（图 1），以覆盖多样化的 UI 组件、美学风格、内容复杂度、质量与用途。例如，沟通与互动类 UI 通常带有大图与醒目的文字，以吸引用户注意；而确认与反馈类的界面通常文字更多，因为其目的是快速提供支付信息；商品目录则常常图文成对出现。我们力求选出在移动端与桌面端都能使用的 UI，并对高度施加约束，使多数界面的尺寸大致相当。大体上，所有 UI 都按原样从数据集中提取。由于这些界面由专业设计师制作，我们降低了部分界面的制作质量，以维持一个兼有高、低质量设计的多样化数据集。由于 UI 采集自专业制作的数据集，我们预期人类与 AI 的评分大多会偏高、偏正面。为此，我们把成对与排序任务设计得更具粒度，以便在测量中捕捉到信号。

**EN** 3.2. Factors

**ZH** 3.2. 因素

**EN** Table 1. UI factors and corresponding statements.

**ZH** 表 1. UI 因素及相应陈述。

<!-- [原子块 · table] Category Factor Question Ease of Use The UI looks easy to use. Cognitive Clarity The layout is uncluttered . Visual Hierarchy The UI has a clear visual hierarchy . Memorable The UI is easily remembere -->

**EN** The UIs we gathered will be judged on nine UI factors on a Likert Scale from 1-7 (Kim et al. 2025). These factors were decided upon after consulting literature that explains how people react to designs and visualizations (Seeley 2012; Wang et al. 2019). The nine factors are clustered into three themes: Cognitive, Perceptual, and Emotional, following the design framework described by Seeley et al. (Seeley 2012).

**ZH** 我们所采集的 UI 将按九项 UI 因素在 1–7 的 Likert 量表上被评判（Kim et al. 2025）。这些因素是在查阅了阐释人们如何对设计与可视化作出反应的文献后确定的（Seeley 2012; Wang et al. 2019）。九项因素按 Seeley et al.（Seeley 2012）所述的设计框架归入三个主题：认知、感知与情感。

**EN** 3.2.1. Cognitive Factors:

**ZH** 3.2.1. 认知因素：

**EN** • Ease of use refers to how easy an interface appears to be. Ease of use can depend on factors like UI element placement, layout of a design, and design heuristics like the match between the system and the real world (Kumar et al. 2004; Nielsen 2005). A screen with high ease of use often does not make users think; its function is straightforward and obvious.

**ZH** • 易用性指界面看上去有多容易使用。易用性取决于 UI 元素的摆放、设计的布局，以及系统与现实世界相匹配之类的设计启发式（Kumar et al. 2004; Nielsen 2005）。易用性高的界面往往不让用户费神思考，其功能直白而明显。

**EN** • Clarity pertains how clear and uncluttered an interface looks. For example, if an interface has too many UI elements, it can overwhelm the user by increasing their cognitive load (Oviatt 2006; Darejeh et al. 2024). For this reason, (Nielsen 2005) highlights the importance of ensuring that designs remain minimalist in nature with enough white space. Doing so ensures the creation of a screen that is uncluttered and does not overwhelm the users. Visual Hierarchy consists of ensuring that there is a clear order of importance between all of the UI elements on a screen (Wang 2024; Still 2018). Doing so decreases the user’s cognitive load, as their attention is caught quickly by whatever is largest, most central, and most important. An interface with good visual hierarchy will have elements that are sized and placed based on their perceived importance and relevance to the user.

**ZH** • 清晰度指界面看上去有多清晰、多不杂乱。例如，若界面上的 UI 元素过多，会因增加用户的认知负荷而使其不堪重负（Oviatt 2006; Darejeh et al. 2024）。为此，（Nielsen 2005）强调了保证设计保持极简、留白充足的重要性；如此方能造就不杂乱、不会压垮用户的界面。视觉层级则指确保屏幕上所有 UI 元素之间存在明确的重要性次序（Wang 2024; Still 2018）。这样做能降低用户的认知负荷，因为其注意力会迅速被最大、最居中、最重要的元素抓住。视觉层级良好的界面，其元素会依据被感知到的重要性和与用户的相关度来确定大小与位置。

**EN** 3.2.2. Perceptual Factors:

**ZH** 3.2.2. 感知因素：

**EN** • Memorable pertains to how easily a UI can be remembered and speaks to the impact that a design has on a user. Memorability can be both negative and positive, and can be a result of attributes like color or recognizable elements (Borkin et al. 2013). Further, does the UI have a certain uniqueness that makes it stand out for the user. These elements, in total, contribute to making an interface memorable to the user.

**ZH** • 记忆度指一个 UI 有多容易被记住，反映设计对用户所产生的影响。记忆度可正可负，可能源自颜色或可辨识元素等属性（Borkin et al. 2013）。此外，还要看 UI 是否具有某种独特性，使其对用户而言脱颖而出。这些元素共同作用，令界面为用户所牢记。

**EN** • Trust pertains to the amount of confidence that the user interface elicits within the user. Headlines, text content, as well as even how well an interface is put together, strongly contribute to trust in interface design. A trustworthy interface will make users feel confident in the content, often because they are designed intentionally and carefully (Zieglmeier and Lehene 2021).

**ZH** • 信任感指用户界面在用户心中唤起的信心程度。标题、文字内容，乃至界面的整合完成度，都对界面设计中的信任感有很强的贡献。值得信赖的界面会让用户对内容感到放心，往往因为它们是被有意、用心地设计出来的（Zieglmeier and Lehene 2021）。

**EN** • Intuitive refers to how functional an interface looks to a user. Intuitiveness and functionality often are intertwined with user experience, so intuitiveness is a crucial factor when judging interfaces. An intuitive screen would be defined as one that users can look at and immediately understand the natural purpose and function (Bærentsen 2000; Blackler et al. 2005; Macaranas et al. 2015)

**ZH** • 直觉性指界面在用户看来有多强的功能性。直觉性与功能性常与用户体验交织在一起，因此在评判界面时，直觉性是一项关键因素。所谓直觉性强的界面，是指用户看一眼就能立刻理解其自然用途与功能（Bærentsen 2000; Blackler et al. 2005; Macaranas et al. 2015）

**EN** 3.2.3. Emotional Factors:

**ZH** 3.2.3. 情感因素：

**EN** • Aesthetic Pleasure refers to how visually attractive an interface is to a specific user. It is a largely subjective factor that often differs from user to user. For the most part, aesthetic pleasure is tightly tied by choices pertaining to color, font, content density, and overall structure. An aesthetically pleasing interface is able to integrate these elements well to create a larger design (Bollini 2017; Hartmann et al. 2008).

**ZH** • 审美愉悦指界面对特定用户的视觉吸引力。这是主观性很强的因素，往往因人而异。大体上，审美愉悦与颜色、字体、内容密度与整体结构方面的选择紧密相关。令人愉悦的界面能够把这些元素很好地整合起来，构成一个更大的设计（Bollini 2017; Hartmann et al. 2008）。

**EN** • Interest in terms of UIs, pertains to how eye-catching, inviting, and captivating an interface is. Interesting interfaces are capable of catching a user’s attention and keeping it. An interesting interface may have UI elements such as unique fonts, mood-inducing colors, or sensational text headlines (Shneiderman 2004).

**ZH** • 趣味性（就 UI 而言）指界面有多抢眼、多引人入胜、多令人着迷。有趣的界面能够抓住用户的注意力并维持住它。有趣的界面可能具备独特字体、营造氛围的配色或耸动的文字标题等 UI 元素（Shneiderman 2004）。

**EN** • Comfort pertains to the overall satisfaction and degree to which an interface makes a user feel at ease while in use (Dave et al. 2023). Designs and interfaces can increase comfort by maintaining a clean, straightforward, and low cognitive load design. A comfortable design may be more tonally consistent and use common fonts and colors.

**ZH** • 舒适感指界面在使用中带给用户的总体满意度与放松程度（Dave et al. 2023）。设计与界面可以通过保持整洁、直白、低认知负荷来提升舒适感。舒适的设计可能在调性上更一致，并使用常见的字体与配色。

<!-- [原子块 · img]  -->

**EN** Figure 2. Example survey question shown to users. Consists of instructions on top, the UI on the left, and the nine factor, Likert scale questions on the right.

**ZH** 图 2. 展示给用户的问卷题目示例。上方为说明，左侧为 UI，右侧为九项因素的 Likert 量表问题。

**EN** 3.3. Participants and Procedure

**ZH** 3.3. 参与者与流程

**EN** In total, we collected 15,000 responses from 500 participants using the online crowdsourcing platform Amazon’s Mechanical Turk. To ensure the quality of the dataset, we filtered for participants who had a greater than 98% approval rating and at least 500 responses to take part in our study. In total, we received feedback on 30 UIs and we asked for 500 unique responses from each. From there, we asked participants to evaluate each UI based on the nine UI Factors (Table 1). Each evaluation was expected to take about 45 seconds to a minute to complete. In total, it cost $75 to get 500 human evaluations for each UI. Before taxes and fees, the total cost of this part of the study was $2,250.

**ZH** 我们通过在线众包平台 Amazon Mechanical Turk，从 500 名参与者处共收集了 15,000 份回答。为保证数据集质量，我们筛选出好评率高于 98%、且至少有 500 份回答经历的参与者。我们共收到针对 30 个 UI 的反馈，并为每个 UI 征集 500 份独立回答。随后，我们请参与者依据九项 UI 因素（表 1）评估每个 UI。每次评估预计耗时约 45 秒到 1 分钟。为每个 UI 获取 500 份人类评估共花费 75 美元；在税费与手续费之前，该部分研究的总成本为 2,250 美元。

**EN** Each UI was presented as a standalone task to minimize order effects, and participants evaluated each UI in two stages. First, participants responded to nine Likert scale questions, one corresponding to each of the UI Factors (see Table 1). Each question asked participants to indicate their level of agreement on a 7-point scale (1 = strongly disagree, 7 = strongly agree). To support their evaluation, participants were able to resize the UI during this stage, allowing them to view it while responding to the questions. Next, participants were asked to provide a textual explanation describing the rationale behind their ratings. This qualitative input allowed for deeper insight into participants’ reactions to each UI.

**ZH** 每个 UI 作为独立任务呈现，以尽量降低顺序效应；参与者分两个阶段评估每个 UI。首先，参与者回答九道 Likert 量表问题，每道对应一项 UI 因素（见表 1）。每道题要求参与者在 7 点量表上表明自己的同意程度（1 = 强烈不同意，7 = 强烈同意）。为便于评估，参与者在此阶段可以调整 UI 的显示大小，以便在作答时查看它。接下来，参与者被要求提供一段文字说明，描述其评分背后的理由。这一质性输入使我们能更深入地了解参与者对每个 UI 的反应。

**EN** 3.4. Result of the Human Data Collection

**ZH** 3.4. 人类数据采集的结果

**EN** We compiled a dataset containing each worker’s ID, the corresponding image ID, the UI’s domain, and the participant’s scores for each of the nine evaluation factors. To ensure consistency across the benchmark, factor and domain names were standardized to align with the terminology used throughout the paper. We applied several data pre-processing steps to ensure data quality. We excluded responses that were completed in less than 45 seconds, based on the rationale that a thoughtful engagement with the task requires at least that amount of time. Additionally, we removed responses that were incomplete or that contained duplicate scores submitted by the same user. Further, we removed data for screens that were not professionally made to maintain consistent data. After the exclusion procedure, we are left with 9,296 human responses. Table 2 presents the mean scores and standard deviations for each of the nine UI factors, as rated by human participants, split by domain. The rightmost column shows the overall average score for each factor across all domains, while the bottom row reports the average score for each domain across all factors. We then compared these human-generated ratings to scores produced by multimodal large language models (MLLMs) to evaluate alignment and divergence in trust-related perceptions.

**ZH** 我们汇编了一份数据集，包含每位工作者的 ID、相应的图像 ID、UI 所属领域，以及参与者对九项评估因素各自的评分。为保证基准的一致性，因素名与领域名被标准化，以与全文所用术语一致。我们施加了若干数据预处理步骤以确保数据质量：剔除了完成时间少于 45 秒的回答，理由是认真投入该任务至少需要这么长时间；此外还删除了填写不完整或由同一用户重复提交相同分数的回答；并移除了非专业制作的界面所对应的数据，以维持数据的一致性。经上述剔除流程后，我们剩下 9,296 份人类回答。表 2 给出了人类参与者对九项 UI 因素各自的均值与标准差，按领域分列。最右列显示每个因素在所有领域上的总体平均分，最底行报告每个领域在所有因素上的平均分。随后我们把这些人类生成的评分与多模态大语言模型（MLLM）给出的分数作比较，以评估在信任相关感知上的吻合与分歧。

**EN** Table 2. Individual human and MLLM scores for all factors and domains. We report the average score over all UIs in the last column and over all factors in the last row. The closest MLLM score to the human is in bold. When the score is closer than ⟦SLOT_1⟧ (⟦SLOT_2⟧), its background is green (light green). The gray text is the standard deviation of the scores from which the average is computed.

**ZH** 表 2. 各因素与各领域上的人类与 MLLM 单独得分。我们在最后一列报告所有 UI 上的平均分，在最后一行报告所有因素上的平均分。与人类最接近的 MLLM 分数以粗体标示。当分数差值小于 ⟦SLOT_1⟧（⟦SLOT_2⟧）时，其底色为绿色（浅绿）。灰色文字为计算该均值所依据的分数标准差。

<!-- [原子块 · table] Domains Factor Evaluator Browsing & Disc. Conf. & Feedback Comm. & Engage. All UIs Ease of Use Human 6.20 (1.08) 6.21 (1.10) 6.21 (1.07) 6.21 (1.09) Claude-3.5 7.00 (0.00) 6.90 (0.32) 6.78 (0.67) 6.89 -->

**EN** 4. Evaluation of MLLM Judges for UIs

**ZH** 4. MLLM 作为 UI 评判者的评估

**EN** We evaluate the efficacy of MLLMs in assessing UIs by comparing their judgments to human evaluations collected through a crowdsourcing study (Section 3). Our analysis proceeds in two parts. In Section 4.1, we examine how well MLLMs predict absolute human scores (prompt shown in Figure 7), assessing both the accuracy of these predictions and their utility for estimating user preferences. In Section 4.2, we analyze pairwise comparisons of UIs based on human data, and evaluate how closely MLLM predictions of these comparisons align with human preferences (prompt shown in Figure 8). The analysis is conducted over all UI factors in Table 1. To avoid bias, and ensure generality and robustness of our findings, we leverage three diverse MLLMs, including GPT-4o, Claude 3.5 Sonnet, and Llama-3.2-11B-Vision.

**ZH** 我们通过把 MLLM 的判断与一项众包研究（第 3 节）所采集的人类评估作比较，来评估 MLLM 评估 UI 的效力。分析分两部分进行。在第 4.1 节中，我们考察 MLLM 预测人类绝对分数的能力（提示词见图 7），评估这些预测的准确率及其用于估计用户偏好的效用。在第 4.2 节中，我们分析基于人类数据的 UI 成对比较，并评估 MLLM 对这些比较的预测与人类偏好的吻合程度（提示词见图 8）。分析覆盖表 1 中的全部 UI 因素。为避免偏见并确保结论的通用性与稳健性，我们使用了三个不同的 MLLM，包括 GPT-4o、Claude 3.5 Sonnet 与 Llama-3.2-11B-Vision。

**EN** 4.1. Task 1: Absolute Score Prediction

**ZH** 4.1. 任务 1：绝对分数预测

**EN** We conduct three studies evaluating how closely MLLMs’ responses to UIs resemble those of humans. In Section 4.1.1, we first analyze MLLM and human scores separately. Results suggest that MLLMs are mostly well aligned to humans, with a few factors where they may significantly under or over predict human scores. In Section 4.1.2, we analyze prediction errors of MLLMs using four metrics: MSE, MAE, accuracy, and ⟦SLOT_3⟧-accuracy. Results suggest that MLLMs well-predict human responses, with Claude being the best judge overall. MLLMs on average overestimated factors like Ease of Use. While consistently underestimating factors like Aesthetic Pleasure, Interesting, and Comfort. Meanwhile, models showed they could reasonably predict scores (within 0.50 Likert points) for factors such as Clarity, Visual Hierarchy, Memorable, and Trustworthy, Intuitive. Finally in Section 4.1.3, we analyze how well MLLM scores predict the ranking of UIs by humans. The factor scan be well predicted, and the best judge overall is Llama. To reduce the randomness in our analysis due to random MLLM scores, we evaluate each UI and factor by each MLLM ⟦SLOT_4⟧ times and then take the median score. Our MLLM prompt is reported in Figure 7 in the Appendix.

**ZH** 我们开展三项研究，评估 MLLM 对 UI 的回答与人类的接近程度。在第 4.1.1 节中，我们首先分别分析 MLLM 与人类的分数；结果表明 MLLM 大体与人类吻合良好，只有少数因素上可能显著低估或高估人类分数。在第 4.1.2 节中，我们用四个指标分析 MLLM 的预测误差：MSE、MAE、准确率与 ⟦SLOT_3⟧-准确率；结果表明 MLLM 能较好地预测人类回答，其中 Claude 总体上是最优评判者。MLLM 平均高估了易用性等因素，同时一致地低估了审美愉悦、趣味性与舒适感等因素。与此同时，模型显示出能合理预测（误差在 0.50 个 Likert 点以内）清晰度、视觉层级、记忆度、可信度与直觉性等因素的分数。最后在第 4.1.3 节中，我们分析 MLLM 分数在多大程度上能预测人类对 UI 的排序；这些因素可被较好地预测，总体上最优的评判者是 Llama。为降低随机 MLLM 分数给分析带来的随机性，我们让每个 MLLM 对每个 UI 与因素评估 ⟦SLOT_4⟧ 次，然后取分数的中位数。我们的 MLLM 提示词见附录中的图 7。

**EN** 4.1.1. Individual Scores

**ZH** 4.1.1. 单项分数

**EN** We start by comparing individual human and MLLM scores. For each UI and factor, we report averaged human scores and median MLLM scores. These averages represent an average perception of a given UI in a given factor. We also included average scores from humans and MLLMs aggregated by the three domains and all UIs, see Table 2.

**ZH** 我们首先比较人类与 MLLM 的单项分数。对每个 UI 与因素，我们报告人类的平均分与 MLLM 分数的中位数。这些均值代表在给定因素上对一个给定 UI 的平均感知。我们也纳入了按三个领域以及全部 UI 汇总的人类与 MLLM 平均分，见表 2。

**EN** We make several observations. First, MLLM judges align reasonably well with humans. As an example, note the average human and MLLM scores over all factors and UIs in Table 2 (last four rows and last column). The human score is ⟦SLOT_5⟧, whereas Claude predicts ⟦SLOT_6⟧, GPT-4o predicts ⟦SLOT_7⟧, and Llama predicts ⟦SLOT_8⟧. Therefore, all MLLM scores are within ⟦SLOT_9⟧ of the human scores. Since this is significantly less than the range of our ⟦SLOT_10⟧-point Likert scale, we conclude that MLLMs reasonably mimic human scores. Second, MLLM scores are often closer to each other than those of humans, as indicated by smaller standard deviations of the scores in Table 2. We note this specifically for Claude and Llama. GPT-4o has sometimes a larger standard deviation and sometimes smaller.

**ZH** 我们得出若干观察。其一，MLLM 评判者与人类吻合得相当好。以表 2 中所有因素与所有 UI 上的人类与 MLLM 平均分为例（最后四行与最后一列）：人类分数为 ⟦SLOT_5⟧，而 Claude 预测 ⟦SLOT_6⟧、GPT-4o 预测 ⟦SLOT_7⟧、Llama 预测 ⟦SLOT_8⟧。因此，所有 MLLM 分数与人类分数的差距都在 ⟦SLOT_9⟧ 之内。由于这远小于我们 ⟦SLOT_10⟧ 点 Likert 量表的取值范围，我们得出结论：MLLM 相当程度上模拟出了人类的分数。其二，MLLM 的分数彼此之间往往比人类分数更接近，这从表 2 中更小的分数标准差可见一斑；我们特别注意到 Claude 与 Llama 如此，而 GPT-4o 的标准差时大时小。

**EN** When considering individual factors in Table 2, MLLMs tend to perform well on cognitive and perceptual factors. For instance, the human score for Trustworthy is ⟦SLOT_11⟧, whereas Claude predicts ⟦SLOT_12⟧, GPT-4o predicts ⟦SLOT_13⟧, and Llama predicts ⟦SLOT_14⟧. This is the only factor where all MLLM scores are within ⟦SLOT_15⟧ of the human score. MLLMs also perform well on Visual Hierarchy, where all MLLM scores are within ⟦SLOT_16⟧ of the human scores. The human score is ⟦SLOT_17⟧, while Claude predicts ⟦SLOT_18⟧, GPT-4o predicts ⟦SLOT_19⟧, and Llama predicts ⟦SLOT_20⟧. Overall, MLLMs likely approximate these scores effectively because the factors have concrete cues in the UI. These factors are correlated with layout, reassuring designs and phrases, and spacing; all of which MLLMs can gather from the UI screenshots.

**ZH** 考察表 2 中的单个因素时，MLLM 在认知与感知因素上往往表现良好。例如，可信度的人类分数为 ⟦SLOT_11⟧，而 Claude 预测 ⟦SLOT_12⟧、GPT-4o 预测 ⟦SLOT_13⟧、Llama 预测 ⟦SLOT_14⟧。这是唯一一个所有 MLLM 分数都落在人类分数 ⟦SLOT_15⟧ 之内的因素。MLLM 在视觉层级上也表现良好，所有 MLLM 分数都落在人类分数的 ⟦SLOT_16⟧ 之内：人类分数为 ⟦SLOT_17⟧，而 Claude 预测 ⟦SLOT_18⟧、GPT-4o 预测 ⟦SLOT_19⟧、Llama 预测 ⟦SLOT_20⟧。总体而言，MLLM 之所以可能有效地逼近这些分数，是因为这些因素在 UI 中有具体的线索可循——它们与布局、令人放心的设计与措辞、以及间距相关，而这些都是 MLLM 可以从 UI 截图中获取的。

**EN** MLLMs struggle with some emotional factors, such as Interesting. Specifically, all MLLM scores of this factor underestimate human scores. The human score is ⟦SLOT_21⟧, whereas Claude predicts ⟦SLOT_22⟧, GPT-4o predicts ⟦SLOT_23⟧, and Llama predicts ⟦SLOT_24⟧. The MLLMs likely struggle with this and other factors like Ease of Use because they are more difficult to quantify for MLLMs. Factors like ease of use are highly tied a users technical literacy and cannot be inferred from visual cues alone (Muzaffar et al. 2011; Hinton 2012).

**ZH** MLLM 在某些情感因素上表现吃力，例如趣味性。具体地，该因素上所有 MLLM 的分数都低估了人类分数：人类分数为 ⟦SLOT_21⟧，而 Claude 预测 ⟦SLOT_22⟧、GPT-4o 预测 ⟦SLOT_23⟧、Llama 预测 ⟦SLOT_24⟧。MLLM 之所以在这一因素以及易用性等其他因素上吃力，很可能是因为这些因素对 MLLM 来说更难量化。易用性这类因素与用户的技术素养高度相关，无法仅凭视觉线索推断（Muzaffar et al. 2011; Hinton 2012）。

**EN** Table 3. We report seven error metrics for all factors and MLLM judges. Four metrics measure the ability to predict scores (MSE, MAE, accuracy, and ⟦SLOT_25⟧-accuracy) and three measure their utility for ranking (Pearson correlation coefficient, Spearman’s ⟦SLOT_26⟧, and Kendall’s ⟦SLOT_27⟧). The last row contains metric values for all factors jointly. Higher correlation coefficients than ⟦SLOT_28⟧ are reported in bold.

**ZH** 表 3. 我们报告所有因素与 MLLM 评判者的七项误差指标。其中四项衡量分数预测能力（MSE、MAE、准确率与 ⟦SLOT_25⟧-准确率），三项衡量其排序效用（Pearson 相关系数、Spearman ⟦SLOT_26⟧ 与 Kendall ⟦SLOT_27⟧）。最后一行给出所有因素合计的指标值。高于 ⟦SLOT_28⟧ 的相关系数以粗体标示。

<!-- [原子块 · table] Factor Model MSE ↓ \downarrow MAE ↓ \downarrow Acc. ↑ \uparrow Acc. ± 1 \pm 1 Pearson ↑ \uparrow Spearman ↑ \uparrow Kendall ↑ \uparrow Cognitive Ease of Use Claude-3.5 0.83 0.87 0.42 0.76 -0.05 (0.82 -->

**EN** 4.1.2. Score Prediction

**ZH** 4.1.2. 分数预测

**EN** Next we analyze how well MLLMs predict human scores. We consider four error metrics: mean squared error (MSE), mean absolute error (MAE), accuracy, and ⟦SLOT_29⟧-accuracy. All metrics are computed on average human and median MLLM scores, for each UI and factor, as in Section 4.1.1. The MSE is the mean of squared differences between MLLM and human scores, over all UIs and for a given factor. The MAE is the mean of absolute differences between MLLM and human scores, over all UIs and for a given factor. The accuracy is the fraction of MLLM scores that matches rounded human scores, over all UIs and for a given factor. The ⟦SLOT_30⟧-accuracy is the fraction of MLLM scores that matches rounded human scores within ⟦SLOT_31⟧, over all UIs and for a given factor. The four metrics provide different views on our results. The MSE and MAE measure mean deviations in the MLLM and human scores, with the former penalizing larger deviations more. The accuracy measures the probability that the MLLM score matches the human score. The ⟦SLOT_32⟧-accuracy measures the probability of a sufficiently close match. All metrics are reported in Table 3.

**ZH** 接下来我们分析 MLLM 预测人类分数的能力。我们考察四项误差指标：均方误差（MSE）、平均绝对误差（MAE）、准确率与 ⟦SLOT_29⟧-准确率。与第 4.1.1 节相同，所有指标均在每个 UI 与因素上、基于人类平均分与 MLLM 分数中位数计算。MSE 是在给定因素下、跨所有 UI 的 MLLM 与人类分数之差的平方的均值；MAE 是在给定因素下、跨所有 UI 的 MLLM 与人类分数之差的绝对值的均值；准确率是在给定因素下、跨所有 UI，MLLM 分数与四舍五入后的人类分数相匹配的样本占比；⟦SLOT_30⟧-准确率是在给定因素下、跨所有 UI，MLLM 分数在 ⟦SLOT_31⟧ 范围内与四舍五入后的人类分数相匹配的样本占比。这四项指标从不同角度呈现我们的结果：MSE 与 MAE 衡量 MLLM 与人类分数的平均偏差，前者对较大偏差的惩罚更重；准确率衡量 MLLM 分数与人类分数相匹配的概率；⟦SLOT_32⟧-准确率衡量足够接近的匹配的概率。所有指标报告于表 3。

**EN** MSE and MAE of some factors are low, which indicates predictability. For instance, all MSEs of Comfort are lower than ⟦SLOT_33⟧ and the lowest of all factors, and all its MAEs are lower than ⟦SLOT_34⟧ and the lowest of all factors. On the other hand, MSE and MAE of some factors are high, which indicates unpredictability. For instance, both MSEs and MAEs of Interesting are higher than those of the other factors. Most other scores fall somewhere in the middle, with factors like Aesthetic Pleasure having lower errors and factors like Ease of Use having higher errors.

**ZH** 某些因素的 MSE 与 MAE 较低，说明可预测性较好。例如，舒适感的全部 MSE 都低于 ⟦SLOT_33⟧，且为所有因素中最低；其全部 MAE 都低于 ⟦SLOT_34⟧，同样为所有因素中最低。另一方面，某些因素的 MSE 与 MAE 较高，说明可预测性较差。例如，趣味性的 MSE 与 MAE 都高于其他因素。多数其他分数处于中间地带，例如审美愉悦的误差较低，而易用性的误差较高。

**EN** The average accuracy of MLLMs over all factors ranges from ⟦SLOT_35⟧ to ⟦SLOT_36⟧, with Claude having the highest accuracy of ⟦SLOT_37⟧. The average ⟦SLOT_38⟧-accuracy is significantly higher, from ⟦SLOT_39⟧ to ⟦SLOT_40⟧. Again, the highest value is achieved by Claude. While the accuracy can vary a lot between different factors, we note that the ⟦SLOT_41⟧-accuracy is relatively stable. In terms of individual factors, Claude is either the best MLLM or performs similarly to it. The model is followed by Llama while GPT-4o performs slightly worse.

**ZH** MLLM 在所有因素上的平均准确率介于 ⟦SLOT_35⟧ 到 ⟦SLOT_36⟧ 之间，其中 Claude 以 ⟦SLOT_37⟧ 取得最高准确率。平均 ⟦SLOT_38⟧-准确率显著更高，介于 ⟦SLOT_39⟧ 到 ⟦SLOT_40⟧ 之间，最高值同样由 Claude 取得。虽然准确率在不同因素之间可能差异很大，我们注意到 ⟦SLOT_41⟧-准确率相对稳定。就单个因素而言，Claude 要么是最优的 MLLM，要么与之表现相近；其后是 Llama，而 GPT-4o 略逊一筹。

**EN** 4.1.3. Ranking Prediction

**ZH** 4.1.3. 排序预测

**EN** Next, we analyze how well MLLMs predict the ranking of UIs by humans. All metrics are computed on average human and median MLLM scores, for each UI and factor, as in Section 4.1.1. The average scores are calculated by aggregating all evaluator scores by factor and UI, and taking the mean of those values. For ranking scores, we consider three most popular metrics of correlation: Pearson correlation coefficient, Spearman’s ⟦SLOT_42⟧, and Kendall’s ⟦SLOT_43⟧. The Pearson correlation coefficient is the covariance of MLLM and human scores divided by their standard deviations, over all UIs and for a given factor. The metric is in ⟦SLOT_44⟧, where ⟦SLOT_45⟧ is the maximum positive correlation, ⟦SLOT_46⟧ is the maximum negative correlation, and ⟦SLOT_47⟧ means no correlations. Spearman’s ⟦SLOT_48⟧ is the Pearson correlation coefficient applied to ranks of MLLM and human scores. Finally, Kendall’s ⟦SLOT_49⟧ measures the pairwise agreement between scores ordered by MLLMs and humans, over all pairs of UIs and for a given factor. The metric is in ⟦SLOT_50⟧, where ⟦SLOT_51⟧ is the maximum positive correlation, ⟦SLOT_52⟧ is the maximum negative correlation, and ⟦SLOT_53⟧ means no correlations. All metrics are reported in Table 3.

**ZH** 接下来，我们分析 MLLM 在多大程度上能预测人类对 UI 的排序。与第 4.1.1 节相同，所有指标均在每个 UI 与因素上、基于人类平均分与 MLLM 分数中位数计算。平均分的计算方式是：按因素与 UI 汇总所有评估者的分数，再对这些值取均值。对于排序分数，我们考察三类最常用的相关性指标：Pearson 相关系数、Spearman ⟦SLOT_42⟧ 与 Kendall ⟦SLOT_43⟧。Pearson 相关系数是在给定因素下、跨所有 UI，MLLM 与人类分数的协方差除以其标准差；该指标取值范围为 ⟦SLOT_44⟧，其中 ⟦SLOT_45⟧ 为最大正相关、⟦SLOT_46⟧ 为最大负相关、⟦SLOT_47⟧ 表示无相关。Spearman ⟦SLOT_48⟧ 是把 Pearson 相关系数应用于 MLLM 与人类分数的秩次。最后，Kendall ⟦SLOT_49⟧ 在给定因素下、跨所有 UI 对，衡量按 MLLM 与人类排序的分数之间的成对一致率；该指标取值范围为 ⟦SLOT_50⟧，其中 ⟦SLOT_51⟧ 为最大正相关、⟦SLOT_52⟧ 为最大负相关、⟦SLOT_53⟧ 表示无相关。所有指标报告于表 3。

**EN** Table 3 shows high correlation coefficients for multiple factors: Memorable, Aesthetic Pleasure, and Interesting. On average, Llama has the highest correlation coefficients, followed by Claude and then GPT-4o. Some results are quite strong. For instance, the Kendall’s ⟦SLOT_54⟧ of ⟦SLOT_55⟧, ⟦SLOT_56⟧, and ⟦SLOT_57⟧ means that the MLLM agrees with the human pairwise ranking ⟦SLOT_58⟧, ⟦SLOT_59⟧, and ⟦SLOT_60⟧ of the time, respectively.

**ZH** 表 3 显示多个因素具有较高的相关系数：记忆度、审美愉悦与趣味性。平均而言，Llama 的相关系数最高，其次是 Claude，再之后是 GPT-4o。部分结果相当强。例如，Kendall ⟦SLOT_54⟧ 为 ⟦SLOT_55⟧、⟦SLOT_56⟧ 与 ⟦SLOT_57⟧，意味着 MLLM 与人类的成对排序分别在 ⟦SLOT_58⟧、⟦SLOT_59⟧ 与 ⟦SLOT_60⟧ 的比例上达成一致。

**EN** Interestingly, high correlation metrics do not necessarily correlate with low prediction errors. As an example, factor Interesting has the highest MSE and MAE of all factors, and also low accuracy and ⟦SLOT_61⟧-accuracy. At the same time, it has the highest correlation metrics for all MLLMs. This reveals that although MLLMs cannot reliably predict the human score, they are effective at capturing relative preferences and thus useful for ranking UIs. This observation motivated us to take a deeper look at pairwise UI comparisons to examine whether these models are genuinely useful for ranking or preference-based tasks (Section 4.2). The opposite can also be true. Factor Comfort has the lowest MSE and MAE of all factors, and also high ⟦SLOT_62⟧-accuracy. At the same time, all correlation metrics are close to zero. To conclude, both prediction errors and ranking metrics provide different views on predicted scores, and therefore we discuss both.

**ZH** 有趣的是，高相关性指标并不一定对应低预测误差。例如，趣味性因素在所有因素中 MSE 与 MAE 最高，准确率与 ⟦SLOT_61⟧-准确率也低；与此同时，它在所有 MLLM 上的相关性指标却最高。这说明，尽管 MLLM 无法可靠地预测人类的分数，它们却能有效捕捉相对偏好，因而对 UI 排序是有用的。这一观察促使我们更深入地考察 UI 的成对比较，以检验这些模型在排序或基于偏好的任务上是否真正有用（第 4.2 节）。反之亦然：舒适感因素在所有因素中 MSE 与 MAE 最低，⟦SLOT_62⟧-准确率也高；与此同时，其全部相关性指标都接近于零。综上，预测误差与排序指标给出了对预测分数的不同视角，因此我们对两者都加以讨论。

**EN** 4.2. Task 2: Pairwise Preference Prediction

**ZH** 4.2. 任务 2：成对偏好预测

**EN** In Section 4.1, we evaluated the ability of MLLMs to predict human scores and their utility for estimating human preferences. In this section, we evaluate the ability of MLLMs to directly estimate human preferences. In Section 4.2.1, we show that MLLMs can predict human preferences in some factors better than in others, as in Table 3. In Section 4.2.2, we show that human preferences are easier to predict if the compared UIs are judged as more different by humans.

**ZH** 在第 4.1 节中，我们评估了 MLLM 预测人类分数的能力及其估计人类偏好的效用。在本节中，我们评估 MLLM 直接估计人类偏好的能力。在第 4.2.1 节中，我们表明 MLLM 对某些因素的偏好预测优于其他因素，如表 3 所示。在第 4.2.2 节中，我们表明：若被比较的两个 UI 在人类看来差异更大，则人类偏好更易预测。

**EN** Table 4. Accuracy in predicting pairwise human preferences over UIs, for all factors and MLLM judges. The last column shows the overall accuracy, averaged over all factors. The highest accuracy, for both individual factors and overall, is reported in bold.

**ZH** 表 4. 在 UI 上预测人类成对偏好的准确率，涵盖所有因素与 MLLM 评判者。最后一列给出在所有因素上平均后的总体准确率。单个因素与总体的最高准确率以粗体标示。

<!-- [原子块 · table] Model Ease Clar Vis Mem Trust Intui Aesth Intrst Comf ALL Claude-3.5 47.01 54.98 61.35 61.75 61.75 58.17 68.53 78.49 47.81 59.98 GPT-4o 50.99 54.55 56.92 64.82 58.89 59.68 64.03 75.10 51.38 59.60 Llam -->

<!-- [原子块 · img]  -->

**EN** Figure 3. Accuracy in predicting pairwise human preferences over UIs as a function of the absolute difference of their average human scores. A higher accuracy generally correlates with a larger difference in the human scores. The score-difference bin values were calculated as the difference between the average human ratings of the two UIs. This number is used to infer the difficulty of the question: smaller values indicate more difficult questions, while larger values imply easier ones.

**ZH** 图 3. 预测 UI 上人类成对偏好的准确率，作为其人类平均分绝对差值的函数。准确率越高，大体对应人类分数的差异越大。分差分箱的取值计算为两个 UI 的人类平均评分之差。该数值用于推断问题的难度：数值越小表示问题越难，数值越大表示问题越容易。

**EN** 4.2.1. Preference Prediction

**ZH** 4.2.1. 偏好预测

**EN** This experiment is conducted as follows. First, we estimate the ground-truth human preference using the average human scores in Section 4.1.1. Specifically, for each pair of UIs for a given factor, we take the average human scores and say that UI ⟦SLOT_63⟧ is preferred to UI ⟦SLOT_64⟧ if the average score of the former is higher than that of the latter. Second, we obtain the preference of the MLLM judge. Specifically, for each pair of UIs, we run the judge with the prompt in Figure 8 and record its preference in each of the nine UI factors. Finally, we say that the judge agrees with the human preference over two UIs in a given factor if it prefers the same UI. The accuracy of the MLLM judge in a given factor is the percentage of UI pairs with agreement, and the overall accuracy is the average of these accuracies.

**ZH** 本实验按如下方式进行。首先，我们用第 4.1.1 节中的人类平均分估计人类偏好的真值。具体地，对给定因素下的每一对 UI，我们取人类的平均分，并认为：若 UI ⟦SLOT_63⟧ 的平均分高于 UI ⟦SLOT_64⟧，则前者优于后者。其次，我们获取 MLLM 评判者的偏好：对每一对 UI，我们用图 8 中的提示词运行评判者，并记录其在九项 UI 因素各自的偏好。最后，若评判者在给定因素上偏好同一个 UI，我们便认为它与该因素上两个 UI 的人类偏好一致。MLLM 评判者在给定因素上的准确率是有一致性的 UI 对所占的百分比，总体准确率则取这些准确率的平均。

**EN** All accuracies are reported in Table 4. They can vary drastically among the factors. GPT-4o and Claude both perform best when asked which UI is more Interesting, with accuracies around ⟦SLOT_65⟧ and ⟦SLOT_66⟧, respectively. This is similar to Table 3, where factor Interesting has the highest correlation coefficients and thus is highly predictable. All models perform poorly when judging Ease of Use, with the accuracies around ⟦SLOT_67⟧ and effectively indicating unpredictability. This is similar to Table 3, where factor Ease of Use has near-zero correlation coefficients. Both Claude and GPT-4o stand out in some areas while falling short in others. Llama is close to random across all factors. The overall accuracy reflects this, with both Claude and GPT-4o being close to ⟦SLOT_68⟧ and Llama being close to a random ⟦SLOT_69⟧.

**ZH** 所有准确率报告于表 4，它们在不同因素之间可能差异悬殊。GPT-4o 与 Claude 在被问及哪个 UI 更有趣时表现最佳，准确率分别约为 ⟦SLOT_65⟧ 与 ⟦SLOT_66⟧。这与表 3 一致——趣味性因素的相关系数最高，因而高度可预测。所有模型在评判易用性时表现都很差，准确率约为 ⟦SLOT_67⟧，实际上说明其不可预测；这也与表 3 一致——易用性因素的相关系数接近于零。Claude 与 GPT-4o 在某些方面突出、在另一些方面不足；Llama 在所有因素上都接近随机。总体准确率反映了这一点：Claude 与 GPT-4o 都接近 ⟦SLOT_68⟧，而 Llama 接近随机的 ⟦SLOT_69⟧。

**EN** 4.2.2. Hardness of Preference Prediction

**ZH** 4.2.2. 偏好预测的难度

**EN** Although many of our UIs are professionally designed, humans can judge them very differently depending on the factor. This motivated us to study whether human preferences are easier to predict if the compared UIs are judged as more different by humans. Specifically, for all UI pairs and factors, we compute the absolute difference of their average human scores and bin them. For each bin, we report the accuracy of the MLLM judge to predict the human preference. We expect MLLMs to struggle more when predicting preferences for UI pairs that humans judged as more similar, but to perform more accurately when humans expressed a clear preference with larger rating differences.

**ZH** 尽管我们的许多 UI 由专业设计，人类的判断仍可能因因素不同而有很大差异。这促使我们研究：若被比较的 UI 在人类看来差异更大，人类偏好是否更易预测。具体地，我们对所有 UI 对与因素计算其人类平均分的绝对差值，并作分箱；对每个分箱，报告 MLLM 评判者预测人类偏好的准确率。我们预期：MLLM 在预测那些人类认为更相似的 UI 对的偏好时会更吃力，而在人类以更大的评分差表达出明确偏好时表现更准确。

**EN** Our results are reported in Figure 3. When the difference in human preferences between UI pairs is small, the accuracy of all MLLM judges is only slightly above ⟦SLOT_70⟧. This suggests that when humans expressed similar levels of preference for the two UIs, their choices were effectively unpredictable by MLLMs. However, as the human preference score difference increases, suggesting that the UIs are more distinguishable for humans, the accuracy of the MLLM judges increases. GPT-4o and Claude have the largest increases, starting near ⟦SLOT_71⟧ and ending close to ⟦SLOT_72⟧ and ⟦SLOT_73⟧, respectively. Llama performs poorly, and its accuracy increases to only about ⟦SLOT_74⟧.

**ZH** 我们的结果报告于图 3。当 UI 对之间的人类偏好差异较小时，所有 MLLM 评判者的准确率仅略高于 ⟦SLOT_70⟧。这说明，当人类对两个 UI 表达出相近的偏好程度时，他们的选择实际上无法被 MLLM 预测。然而，随着人类偏好分差增大（说明这些 UI 对人类而言更易区分），MLLM 评判者的准确率随之上升。GPT-4o 与 Claude 的增幅最大，分别从接近 ⟦SLOT_71⟧ 起步，最终接近 ⟦SLOT_72⟧ 与 ⟦SLOT_73⟧。Llama 表现不佳，其准确率仅升至约 ⟦SLOT_74⟧。

**EN** 5. Discussion

**ZH** 5. 讨论

**EN** 5.1. MLLMs as Approximators

**ZH** 5.1. MLLM 作为近似器

**EN** Across all three models, the benchmark data illustrate that models can achieve reasonably high accuracy within ⟦SLOT_75⟧ for absolute score tasks (Table 4) and GPT and Claude perform reasonably well in pairwise tasks where the two UIs have a significant degree of difference (Figure 3). However, the same models perform less effectively in terms of exact accuracy (Claude 48% and GPT 40%) and when there is a small degree of difference in pairwise tasks. In fact, the models performed near random on pairwise tasks with small degrees of difference. Further, MAE scores ranged from 0.53 to 0.64, and MSE scores ranged from 0.44 to 0.66. While these scores are moderate, they are also significant enough to reflect that state of the art models cannot fully replace human evaluation.

**ZH** 跨三个模型的基准数据表明，在绝对分数任务上，模型可以在 ⟦SLOT_75⟧ 范围内取得相当高的准确率（表 4）；而在两个 UI 差异显著时，GPT 与 Claude 在成对任务上表现相当不错（图 3）。然而，同样的模型在精确准确率上表现较差（Claude 48%、GPT 40%），在成对任务差异较小的情形下也是如此。事实上，在差异较小的成对任务上，模型的表现接近于随机。此外，MAE 分数介于 0.53 到 0.64，MSE 分数介于 0.44 到 0.66。这些分数虽属中等，却也足以说明当前最先进的模型无法完全替代人类评估。

**EN** For this reason, it is recommended that MLLMs be seen as UI testing approximators, not replacements. Essentially, given the results, MLLMs should be used to supplement existing research or be used in scenarios where research would not otherwise be used. The results of this study reflect that MLLMs struggled on fine-grained UI evaluation tasks. However, MLLMs have reasonable accuracy and reliability in generalized evaluations and when comparing UIs with larger disparities. Furthermore, results should be seen as approximations and are capable of giving designers general direction. However, they are not capable of acting as complete replacements for real human research.

**ZH** 为此，建议把 MLLM 视为 UI 测试的近似器，而非替代品。本质上，根据这些结果，MLLM 应用于补充既有研究，或用于那些本来不会开展研究的场景。本研究的结果反映出，MLLM 在细粒度的 UI 评估任务上表现吃力；然而在泛化的评估中、以及在比较差异较大的 UI 时，MLLM 具有尚可的准确率与可靠性。此外，结果应被视为近似值，能够为设计师提供大致方向；但它们不足以完全替代真实的人类研究。

**EN** 5.2. MLLMs’ Role in the Design Process

**ZH** 5.2. MLLM 在设计流程中的角色

**EN** Given the moderate strength in human emulating UI tasks, MLLMs show decent promise in acting as a proxy for early user testing. Given that overall correlation coefficients across all models (Table 4) were relatively decent, MLLMs show moderate promise for low-stakes user research. More specifically, designers should use them early in the design process in situations where they may be rapidly iterating through several different designs and not have the research resources to test and compare every single design. As seen in the results, MLLMs perform moderately well in these use cases as they can accurately score designs within ⟦SLOT_76⟧ Likert scale point. Furthermore, as seen in the pairwise testing, they are also able to strongly predict human preferences when there is a large difference in human scores. For this reason, MLLMs can responsibly be used in these early design process situations in order to get a sense of direction on early UI iterations.

**ZH** 鉴于 MLLM 在模拟人类的 UI 任务上具有中等强度的能力，它们作为早期用户测试的代理展现出可观的前景。鉴于所有模型的总体相关系数（表 4）相对不错，MLLM 在低风险用户研究中显示出中等程度的应用前景。更具体地，设计师应在设计流程的早期使用它们——那时他们可能在多个不同设计之间快速迭代，却没有研究资源去测试和比较每一个设计。如结果所示，MLLM 在这些使用场景中表现中等偏上，因为它们能把设计的打分控制在 ⟦SLOT_76⟧ 个 Likert 量表点以内。此外，如成对测试所示，当人类分数差异较大时，它们也能强有力地预测人类偏好。因此，MLLM 可以被负责任地用于这些早期设计流程场景，从而为早期 UI 迭代提供方向感。

**EN** However, these results also suggest that MLLMs are not accurate enough to be used as a permanent or effective standout when exact results are needed. There was significant variation when looking at the results on the factor level, and it is clear that these models are not precise across most factors. For this reason, it is not recommended that these models be used for validation testing towards the end of the design process or high-stakes user research scenarios.

**ZH** 然而，这些结果同样表明，MLLM 的精度不足以在需要精确结果时被用作永久性的或可靠的替代方案。从因素层面的结果看存在显著波动，显然这些模型在多数因素上并不精确。因此，不建议把这些模型用于设计流程末期的验证测试或高风险的用户研究场景。

**EN** 5.3. Benchmark for Fine-Tuned Models

**ZH** 5.3. 面向微调模型的基准

**EN** Another future direction for this work would be to create a fine-tuned model with stronger factor sensitivity than the state-of-the-art models presented in this study. Considering that the state-of-the-art models mostly struggled with several traits like ease-of-use and even clarity, there is clearly a gap in how these models handle different traits. This gap suggests an opportunity to create a fine-tuned model based on the benchmark scores that will be better able to predict and replicate human scores. This benchmark can be utilized in tandem with reinforcement learning with human feedback (RLHF) on factor-specific data or even chain of thought prompting. Given this, the fine-tuned tool would be more useful in general, being more applicable and reliable in the design process. Furthermore, the data could be used to fine-tune prompts used. Doing so would require less lift than creating a fine-tuned model while also potentially making a significant difference in the evaluation quality.

**ZH** 本工作的另一个未来方向，是创建一个在因素敏感度上强于本文所考察的最先进模型的微调模型。考虑到当前最先进的模型大多在易用性乃至清晰度等若干特质上表现吃力，这些模型处理不同特质的方式显然存在缺口。这一缺口提示了一个机会：基于本基准的分数构建一个微调模型，使其能更好地预测与复现人类分数。该基准可与因素特定数据上的基于人类反馈的强化学习（RLHF）结合使用，甚至可结合思维链提示。如此，微调所得的工具将更具通用性，在设计流程中更适用、更可靠。此外，这些数据也可用于微调所用的提示词；这样做比创建微调模型省力，却可能在评估质量上带来显著差异。

**EN** 5.4. Ethical Considerations

**ZH** 5.4. 伦理考量

**EN** While these results show encouraging reasons for using MLLMs as a UI judge, it should not be used to justify the complete replacement of human testing. In fact, it should do the opposite and reinforce the need for real human testing. The results presented expose key limitation that should give any design team pause when asking whether they should completely rely on MLLMs for user interface validation.

**ZH** 尽管这些结果给出了使用 MLLM 作为 UI 评判者的鼓舞人心的理由，但它不应被用来为完全取代人类测试辩护。事实上，它应当起到相反的作用——强化对真实人类测试的必要性。所呈现的结果暴露了关键局限，足以让任何设计团队在考虑是否完全依赖 MLLM 做用户界面验证时三思。

**EN** Again, we emphasize that these results reflect that MLLMs should be used solely for supplemental use. It should be used to fill gaps where no user research exists, not to replace real human research and testing. MLLMs should be seen as a source of low-cost, rapid iterative evaluations when it is not feasible to perform extensive user research. This will enable designers to identify common trends and larger flaws earlier on in the design process.

**ZH** 我们再次强调，这些结果反映出 MLLM 仅应用于补充性用途。它应被用于填补没有用户研究存在的空白，而不是替代真实的人类研究与测试。MLLM 应被视为在无法开展广泛用户研究时，一种低成本、可快速迭代的评估来源。这将使设计师能够在设计流程更早的阶段识别出常见趋势与较大的缺陷。

**EN** Despite the seemingly negative ethical considerations, there is a strong reason for why this method should be adopted. There is significant potential for using this dataset to increase design democratization for junior designers with little to no access to high-end design research. Specifically, there is a large opportunity for designers to use MLLMs to "fine-tune" their designs, using MLLMs as a sanity check of their design intuitions and a learning opportunity.

**ZH** 尽管上述伦理考量看似负面，采用这一方法却有一个强有力的理由：该数据集在提升设计民主化方面潜力巨大，可惠及几乎没有高端设计研究资源的初级设计师。具体地，设计师有大量机会用 MLLM 来“微调”自己的设计，把 MLLM 当作检验自身设计直觉的理性校验与学习机会。

**EN** 5.5. Future Work & Limitations

**ZH** 5.5. 未来工作与局限性

**EN** Building on our benchmark, we are extremely excited by the opportunities to expand AI’s capabilities as a judge for interface testing. Most notably, this benchmark can support fine-tuned models or alignment training—particularly reinforcement learning from human feedback (RLHF). Whether used alone or with similar datasets, it can help create models that better supplement user research. There is also the opportunity to expand the benchmark by adding more screens and tasks. For instance, this study focused on mobile and desktop UIs, but future work could include tablets, TVs, consoles, and more. A broader set of UIs would enable a more holistic benchmark. We also see potential to study more models and prompting methods—this work focused on GPT-4o, Claude 3.5 Sonnet, and Llama 3.2, but future studies could explore Gemini, Qwen, GPT-4o mini, and others using the same framework. Prompting strategies like chain-of-thought and few-shot learning also merit further exploration. Finally, because UI design is iterative, future work could compare versions of the same design, measuring how small changes—like color, text, or layout—affect human and MLLM judgments.

**ZH** 在我们的基准之上，我们对拓展 AI 作为界面测试评判者的能力感到极为振奋。最值得注意的是，该基准可支撑微调模型或对齐训练——尤其是基于人类反馈的强化学习（RLHF）。无论单独使用还是与类似数据集结合使用，它都有助于创建能更好地补充用户研究的模型。也有机会通过增加更多界面与任务来扩展该基准。例如，本研究聚焦于移动端与桌面端 UI，未来工作可纳入平板、电视、游戏主机等。更广泛的 UI 集合将带来更全面的基准。我们还看到研究更多模型与提示方法的潜力——本工作聚焦于 GPT-4o、Claude 3.5 Sonnet 与 Llama 3.2，而未来研究可用同一框架探索 Gemini、Qwen、GPT-4o mini 等。思维链与少样本学习等提示策略同样值得进一步探索。最后，由于 UI 设计是迭代式的，未来工作可以比较同一设计的不同版本，衡量颜色、文字或布局等微小改动带来的影响。

**EN** While our findings reveal MLLM’s capability to emulate human UI perceptions to a moderate degree, several limitations of this study still persist. Firstly, the entirety of both the human and Firstly, the entirety of both the human and MLLMs tasks was performed on static user interfaces. Secondly, the screens used in the study were primarily professionally made within the context of Western design standards. We leave it to future extending our line of work to the diverse, dynamic interactions that usually occur in user research.

**ZH** 虽然我们的发现揭示了 MLLM 以中等程度模拟人类 UI 感知的能力，本研究仍存在若干局限。其一，人类与 MLLM 的全部任务都在静态用户界面上进行。其二，本研究中所用的界面主要是在西方设计标准语境下专业制作的。我们把这条研究路线向用户研究中通常发生的多样化、动态交互延伸的任务，留给未来的工作。

**EN** 6. Conclusion

**ZH** 6. 结论

**EN** To evaluate the effectiveness of MLLMs as UI judges, this study facilitated the collection and testing of a set of user interfaces. The same UI studies were given to both human and MLLM evaluators, and the results were compared to analyze to what degree MLLM evaluators can emulate human results. This study was conducted using two unique tasks: 1) an absolute scoring task using a 1-7 Likert scale and 2) a pairwise evaluation. For task 1, the findings reveal that when asked to evaluate screens at an overall level, MLLMs do moderately well. However, when asked to judge them based on specific factors or criteria, they tend to struggle. For task 2, the MLLMs again performed reasonably on the pairwise comparisons. Naturally, MLLM evaluators performed better on pairwise questions that compared two screens that have a higher degree of difference. Lastly, we accumulated the results from these tests into a benchmark to be used in future studies. Future work offers the opportunity to use the benchmark to create a fine-tuned model that would perform better at UI judgment tasks compared to state-of-the-art models. For this reason, we recommend that MLLMs are used to supplement early, low stakes user research – not replace it. Finally, the benchmark provided in this paper is capable of laying the groundwork for future studies that can better explore MLLM as a UI judge.

**ZH** 为评估 MLLM 作为 UI 评判者的有效性，本研究促成了一组用户界面的采集与测试。我们把同样的 UI 研究分别交给人类与 MLLM 评估者，并比较结果，以分析 MLLM 评估者能在多大程度上模拟人类的结果。本研究通过两项独特的任务展开：1) 使用 1–7 Likert 量表的绝对评分任务；2) 成对评估。对于任务 1，研究结果显示：当要求从整体层面评估界面时，MLLM 表现中等偏上；但当要求依据特定因素或准则评判时，它们往往表现吃力。对于任务 2，MLLM 在成对比较上同样表现尚可；自然地，在比较两个差异程度更高的界面时，MLLM 评估者表现更好。最后，我们把这些测试的结果汇编为一个基准，供未来研究使用。未来工作有机会利用该基准创建一个在 UI 判断任务上优于当前最先进模型的微调模型。为此，我们建议把 MLLM 用于补充早期、低风险的用户研究，而非取代它。最后，本文提供的基准能够为未来更好地探索「MLLM 作为 UI 评判者」的研究奠定基础。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] (1) -->

<!-- [原子块 · verbatim] Achiam et al . (2023) Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al . 2023. Gpt-4  -->

<!-- [原子块 · verbatim] Bærentsen (2000) Klaus B Bærentsen. 2000. Intuitive user interfaces. Scandinavian Journal of Information Systems 12, 1 (2000), 4. -->

<!-- [原子块 · verbatim] Bailey et al . (1988) Wayne A Bailey, Stephen T Knox, and Eugene F Lynch. 1988. Effects of interface design upon user productivity. In Proceedings of the SIGCHI conference on Human factors in computin -->

<!-- [原子块 · verbatim] Baxter et al . (2015) Kathy Baxter, Catherine Courage, and Kelly Caine. 2015. Understanding your users: a practical guide to user research methods . Morgan Kaufmann. -->

<!-- [原子块 · verbatim] Bertão and Joo (2021) Renato Antonio Bertão and Jaewoo Joo. 2021. Artificial intelligence in UX/UI design: a survey on current adoption and [future] practices. Safe Harbors for Design Research (2021), -->

<!-- [原子块 · verbatim] Bhandari et al . (2017) Upasna Bhandari, Tillmann Neben, Klarissa Chang, and Wen Yong Chua. 2017. Effects of interface design factors on affective responses and quality evaluations in mobile applicati -->

<!-- [原子块 · verbatim] Blackler et al . (2005) Alethea Blackler, Vesna Popovic, and Douglas Mahar. 2005. Intuitive interaction applied to interface design. In New Design Paradigms: Proceedings of International Design Congre -->

<!-- [原子块 · verbatim] Bollini (2017) Letizia Bollini. 2017. Beautiful interfaces. From user experience to user interface design. The Design Journal 20, sup1 (2017), S89–S101. -->

<!-- [原子块 · verbatim] Borkin et al . (2013) Michelle A. Borkin, Azalea A. Vo, Zoya Bylinskii, Phillip Isola, Shashank Sunkavalli, Aude Oliva, and Hanspeter Pfister. 2013. What Makes a Visualization Memorable? IEEE Transact -->

<!-- [原子块 · verbatim] Cao et al . (2025) Renjie Cao, Mei Zhang, and Yu Huang. 2025. Learning to Simulate Survey Distributions with Fine-Tuned LLMs. In Proceedings of the 2025 Conference of the North American Chapter of the -->

<!-- [原子块 · verbatim] Darejeh et al . (2024) Ali Darejeh, Nadine Marcusa, Gelareh Mohammadi, and John Sweller. 2024. A critical analysis of cognitive load measurement methods for evaluating the usability of different types -->

<!-- [原子块 · verbatim] Das et al . (2025) Amit Kumar Das, Cindy Xiong Bearfield, and Klaus Mueller. 2025. Leveraging Large Language Models for Personalized Public Messaging. In Proceedings of the Extended Abstracts of the C -->

<!-- [原子块 · verbatim] Dave et al . (2023) Anjali Dave, Ankur Saxena, and Avdhesh Jha. 2023. Understanding User comfort and Expectations in AI-based Systems. (2023). -->

<!-- [原子块 · verbatim] Duan et al . (2024a) Peitong Duan, Chin-Yi Cheng, Gang Li, Bjoern Hartmann, and Yang Li. 2024a. UICrit: Enhancing Automated Design Evaluation with a UI Critique Dataset. In Proceedings of the 37th Ann -->

<!-- [原子块 · verbatim] Duan et al . (2024b) Peitong Duan, Jeremy Warner, Yang Li, and Bjoern Hartmann. 2024b. Generating automatic feedback on ui mockups with large language models. In Proceedings of the 2024 CHI Conference -->

<!-- [原子块 · verbatim] Gu et al . (2024) Jiawei Gu, Xuhui Jiang, Zhichao Shi, Hexiang Tan, Xuehao Zhai, Chengjin Xu, Wei Li, Yinghan Shen, Shengjie Ma, Honghao Liu, et al . 2024. A survey on llm-as-a-judge. arXiv preprint a -->

<!-- [原子块 · verbatim] Guo et al . (2025) Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al . 2025. Deepseek-r1: Incentivizing reasoning capability  -->

<!-- [原子块 · verbatim] Hämäläinen et al . (2023) Perttu Hämäläinen, Mikke Tavast, and Anton Kunnari. 2023. Evaluating Large Language Models in Generating Synthetic HCI Research Data: a Case Study. In Proceedings of the 2023 -->

<!-- [原子块 · verbatim] Hartmann et al . (2008) Jan Hartmann, Alistair Sutcliffe, and Antonella De Angeli. 2008. Towards a theory of user judgment of aesthetics and user interface quality. ACM Transactions on Computer-Human  -->

<!-- [原子块 · verbatim] Hinton (2012) Stephen Hinton. 2012. Using Recursive Distance Vector Methodology to Review Remote Desktop Solutions in the Small Business Consulting Environment. Issues in Information Systems 13, 1 (20 -->

<!-- [原子块 · verbatim] Jansen et al . (2023) Bernard J. Jansen, Soon-Gyo Jung, and Joni Salminen. 2023. Employing large language models in survey research. Nat. Lang. Process. J. 4 (2023), 100020. https://doi.org/10.1016/j. -->

<!-- [原子块 · verbatim] Kaplan (2020) Kate Kaplan. 2020. Typical Designer–to–Developer and Researcher–to–Designer Ratios. https://www.nngroup.com/articles/ux-developer-ratio/ -->

<!-- [原子块 · verbatim] Kim et al . (2024) Seungone Kim, Juyoung Suk, Shayne Longpre, Bill Yuchen Lin, Jamin Shin, Sean Welleck, Graham Neubig, Moontae Lee, Kyungjae Lee, and Minjoon Seo. 2024. Prometheus 2: An open source l -->

<!-- [原子块 · verbatim] Kim et al . (2025) Seon Gyeom Kim, Jae Young Choi, Ryan Rossi, Eunyee Koh, and Tak Yeon Lee. 2025. Chart-to-Experience: Benchmarking Multimodal LLMs for Predicting Experiential Impact of Charts. In 20 -->

<!-- [原子块 · verbatim] Kuang et al . (2024) Emily Kuang, Minghao Li, Mingming Fan, and Kristen Shinohara. 2024. Enhancing UX Evaluation Through Collaboration with Conversational AI Assistants: Effects of Proactive Dialogue  -->

<!-- [原子块 · verbatim] Kumar et al . (2004) Ram L Kumar, Michael Alan Smith, and Snehamay Bannerjee. 2004. User interface features influencing overall ease of use and personalization. Information & Management 41, 3 (2004),  -->

<!-- [原子块 · verbatim] Lee et al . (2024) Seongyun Lee, Seungone Kim, Sue Park, Geewook Kim, and Minjoon Seo. 2024. Prometheus-vision: Vision-language model as a judge for fine-grained evaluation. In Findings of the associa -->

<!-- [原子块 · verbatim] Li et al . (2023) Junlong Li, Shichao Sun, Weizhe Yuan, Run-Ze Fan, Hai Zhao, and Pengfei Liu. 2023. Generative judge for evaluating alignment. arXiv preprint arXiv:2310.05470 (2023). -->

<!-- [原子块 · verbatim] Li et al . (2024) Peiyao Li, Noah Castelo, Zsolt Katona, and Miklos Sarvary. 2024. Frontiers: Determining the validity of large language models for automated perceptual analysis. Marketing Science 43, -->

<!-- [原子块 · verbatim] Liu et al . (2024) Yinhong Liu, Han Zhou, Zhijiang Guo, Ehsan Shareghi, Ivan Vulić, Anna Korhonen, and Nigel Collier. 2024. Aligning with human judgement: The role of pairwise preference in large lang -->

<!-- [原子块 · verbatim] Luera et al . (2025) Reuben Luera, Ryan Rossi, Franck Dernoncourt, Alexa Siu, Sungchul Kim, Tong Yu, Ruiyi Zhang, Xiang Chen, Nedim Lipka, Zhehao Zhang, Seon Gyeom Kim, and Tak Yeon Lee. 2025. Persona -->

<!-- [原子块 · verbatim] Luera et al . (2024) Reuben Luera, Ryan A Rossi, Alexa Siu, Franck Dernoncourt, Tong Yu, Sungchul Kim, Ruiyi Zhang, Xiang Chen, Hanieh Salehy, Jian Zhao, et al . 2024. Survey of User Interface Design  -->

<!-- [原子块 · verbatim] Macaranas et al . (2015) Anna Macaranas, Alissa N Antle, and Bernhard E Riecke. 2015. What is intuitive interaction? Balancing users’ performance and satisfaction with natural user interfaces. Interac -->

<!-- [原子块 · verbatim] Medlock (2018) Michael C Medlock. 2018. The rapid iterative test and evaluation method (RITE). Games User Research (2018), 203–215. -->

<!-- [原子块 · verbatim] Muzaffar et al . (2011) Abdul Wahab Muzaffar, Farooque Azam, Hina Anwar, and Ali Saeed Khan. 2011. Usability aspects in pervasive computing: Needs and challenges. International Journal of Computer App -->

<!-- [原子块 · verbatim] Nielsen (2005) Jakob Nielsen. 2005. Ten usability heuristics. (2005). -->

<!-- [原子块 · verbatim] Ouyang et al . (2022) Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al . 2022. Training language mod -->

<!-- [原子块 · verbatim] Oviatt (2006) Sharon Oviatt. 2006. Human-centered design meets cognitive load theory: designing interfaces that help people think. In Proceedings of the 14th ACM international conference on Multimedia -->

<!-- [原子块 · verbatim] Panickssery et al . (2024) Arjun Panickssery, Samuel R. Bowman, and Shi Feng. 2024. LLM Evaluators Recognize and Favor Their Own Generations. arXiv:2404.13076 [cs.CL] https://arxiv.org/abs/2404.13076 -->

<!-- [原子块 · verbatim] Qin et al . (2024) Zhen Qin, Rolf Jagerman, Kai Hui, Honglei Zhuang, Junru Wu, Le Yan, Jiaming Shen, Tianqi Liu, Jialu Liu, Donald Metzler, Xuanhui Wang, and Michael Bendersky. 2024. Large Language Mo -->

<!-- [原子块 · verbatim] Ramamurthy et al . (2022) Rajkumar Ramamurthy, Prithviraj Ammanabrolu, Kianté Brantley, Jack Hessel, Rafet Sifa, Christian Bauckhage, Hannaneh Hajishirzi, and Yejin Choi. 2022. Is reinforcement learni -->

<!-- [原子块 · verbatim] Reinecke et al . (2013) Katharina Reinecke, Tom Yeh, Luke Miratrix, Rahmatri Mardiko, Yuechen Zhao, Jenny Liu, and Krzysztof Z Gajos. 2013. Predicting users’ first impressions of website aesthetics wi -->

<!-- [原子块 · verbatim] Rosala and Moran (2024) Tina Rosala and Kate Moran. 2024. Synthetic Users and AI Personas in UX Research: A Cautionary Note. Nielsen Norman Group Reports (2024). https://www.nngroup.com/articles/synth -->

<!-- [原子块 · verbatim] Schoop et al . (2022) Eldon Schoop, Xin Zhou, Gang Li, Zhourong Chen, Bjoern Hartmann, and Yang Li. 2022. Predicting and Explaining Mobile UI Tappability with Vision Modeling and Saliency Analysis. In -->

<!-- [原子块 · verbatim] Seeley (2012) William P Seeley. 2012. Hearing how smooth it looks: Selective attention and crossmodal perception in the arts. Essays in Philosophy 13, 2 (2012), 498–517. -->

<!-- [原子块 · verbatim] Shneiderman (2004) Ben Shneiderman. 2004. Designing for fun: how can we design user interfaces to be more fun? interactions 11, 5 (2004), 48–50. -->

<!-- [原子块 · verbatim] Steen et al . (2007) Marc Steen, Lottie Kuijt-Evers, and Jente Klok. 2007. Early user involvement in research and design projects–A review of methods and practices. In 23rd egos colloquium , Vol. 5. 1 -->

<!-- [原子块 · verbatim] Still (2018) Jeremiah D Still. 2018. Web page visual hierarchy: Examining Faraday’s guidelines for entry points. Computers in Human Behavior 84 (2018), 352–359. -->

<!-- [原子块 · verbatim] Stokes et al . (2025) Chase Stokes, Kylie Lin, and Cindy Xiong Bearfield. 2025. Write, Rank, or Rate: Comparing Methods for Studying Visualization Affordances. IEEE VIS (2025). -->

<!-- [原子块 · verbatim] Team et al . (2023) Gemini Team, Rohan Anil, Sebastian Borgeaud, Jean-Baptiste Alayrac, Jiahui Yu, Radu Soricut, Johan Schalkwyk, Andrew M Dai, Anja Hauth, Katie Millican, et al . 2023. Gemini: a fami -->

<!-- [原子块 · verbatim] Thakur et al . (2025) Aman Singh Thakur, Kartik Choudhary, Venkat Srinik Ramayapally, Sankaran Vaidyanathan, and Dieuwke Hupkes. 2025. Judging the Judges: Evaluating Alignment and Vulnerabilities in L -->

<!-- [原子块 · verbatim] Wang (2024) Di Wang. 2024. Research on Visual Hierarchy and Interactive Experience in Digital Media UI Design. In 2024 5th International Conference on Intelligent Design (ICID) . IEEE, 133–136. -->

<!-- [原子块 · verbatim] Wang (2025) Dakuo et al. Wang. 2025. AgentA/B: Automated and Scalable Web A/B Testing with Interactive LLM Agents. arXiv preprint arXiv:2504.09723 (2025). -->

<!-- [原子块 · verbatim] Wang et al . (2024) Huichen Will Wang, Jane Hoffswell, Victor S Bursztyn, Cindy Xiong Bearfield, et al . 2024. How aligned are human chart takeaways and llm predictions? a case study on bar charts wit -->

<!-- [原子块 · verbatim] Wang et al . (2023) Peiyi Wang, Lei Li, Liang Chen, Zefan Cai, Dawei Zhu, Binghuai Lin, Yunbo Cao, Qi Liu, Tianyu Liu, and Zhifang Sui. 2023. Large language models are not fair evaluators. arXiv prepr -->

<!-- [原子块 · verbatim] Wang et al . (2022) Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa Liu, Noah A Smith, Daniel Khashabi, and Hannaneh Hajishirzi. 2022. Self-instruct: Aligning language models with self-generated in -->

<!-- [原子块 · verbatim] Wang et al . (2019) Yun Wang, Adrien Segal, Roberta Klatzky, Daniel F. Keefe, Petra Isenberg, Jörn Hurtienne, Eva Hornecker, Tim Dwyer, and Stephen Barrass. 2019. An Emotional Response to the Value of -->

<!-- [原子块 · verbatim] Wu et al . (2024) Jason Wu, Yi-Hao Peng, Xin Yue Amanda Li, Amanda Swearngin, Jeffrey P Bigham, and Jeffrey Nichols. 2024. UICLIP: a data-driven model for assessing user interface design. In Proceedin -->

<!-- [原子块 · verbatim] Xiang et al . (2024) Wei Xiang, Hanfei Zhu, Suqi Lou, Xinli Chen, Zhenghua Pan, Yuping Jin, Shi Chen, and Lingyun Sun. 2024. SimUser: Generating Usability Feedback by Simulating Various Users Interact -->

<!-- [原子块 · verbatim] Zhang et al . (2023) Xinghua Zhang, Bowen Yu, Haiyang Yu, Yangyu Lv, Tingwen Liu, Fei Huang, Hongbo Xu, and Yongbin Li. 2023. Wider and deeper llm networks are fairer llm evaluators. arXiv preprint ar -->

<!-- [原子块 · verbatim] Zheng et al . (2023) Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric Xing, et al . 2023. Judging llm-as-a-judge with mt-benc -->

<!-- [原子块 · verbatim] Ziegler et al . (2020) Daniel M. Ziegler, Nisan Stiennon, Jeffrey Wu, Tom B. Brown, Alec Radford, Dario Amodei, Paul Christiano, and Geoffrey Irving. 2020. Fine-Tuning Language Models from Human Prefe -->

<!-- [原子块 · verbatim] Zieglmeier and Lehene (2021) Valentin Zieglmeier and Antonia Maria Lehene. 2021. Designing trustworthy user interfaces. In Proceedings of the 33rd Australian Conference on Human-Computer Interaction . -->

**EN** Appendix A Opportunities (Extended)

**ZH** 附录 A 机会（扩展）

**EN** Building on our benchmark, we are extremely excited by the possible opportunities to expand on the capabilities of MLLM as a judge for interface testing. Most notably, this benchmark can be used to create a fine-tuned model or in alignment training. Reinforcement learning from human feedback (RLHF) is a specialized fine-tuning technique that would most align with this benchmark. Whether using this benchmark in isolation or in tandem with other similar datasets, there is an opportunity to create a fine-tuned model that will better supplement user research.

**ZH** 在我们的基准之上，我们对拓展「MLLM 作为界面测试评判者」能力的各种可能机会感到极为振奋。最值得注意的是，该基准可被用于创建微调模型或用于对齐训练。基于人类反馈的强化学习（RLHF）是一种专门的微调技术，与本基准最为契合。无论是单独使用该基准，还是与其他类似数据集结合使用，都有机会创建一个能更好地补充用户研究的微调模型。

<!-- [原子块 · img]  -->

**EN** Figure 4. Results when pairwise data is created for MLLMs and humans in the same way. For both human and MLLM evaluation sets, we take the absolute value gathered in task 1, compare the two absolute values, and take the higher of the two. Then we compare the human results to the MLLM results to get the agreement score presented here.

**ZH** 图 4. 以相同方式为 MLLM 与人类构造成对数据时的结果。对人类与 MLLM 的评估集，我们都取任务 1 中收集的绝对值，比较这两个绝对值，并取其中较高者；随后把人类结果与 MLLM 结果作比较，得到此处呈现的一致率。

**EN** Secondly, there is also the opportunity to expand on the benchmark by adding more screens and/or more tasks. Increasing the amount and diversity of screens can uncover more trends that were not uncovered in this study. For example, this study focused on mobile and desktop first UIs, but UIs exist for tablets, televisions, entertainment consoles, and many other devices. Expanding the benchmark to include a diverse set of UIs will create a more holistic benchmark. Furthermore, user research is not limited to just Likert-scale scores and A/B testing. The benchmark can be expanded by adding usability studies, surveys, need-finding, etc. Expanding the data in such a way will further test MLLM’s efficacy in UI tasks and create a more expansive benchmark for fine-tuned models.

**ZH** 其次，也有机会通过增加更多界面和／或更多任务来扩展基准。增加界面的数量与多样性，可以揭示本研究未发现的一些趋势。例如，本研究聚焦于移动端与桌面端优先的 UI，但 UI 也存在于平板、电视、娱乐主机以及许多其他设备上。把基准扩展到涵盖多样化的 UI 集合，将创建出更全面的基准。此外，用户研究并不限于 Likert 量表评分与 A/B 测试；该基准可通过加入可用性研究、问卷调查、需求挖掘等内容而扩展。如此扩展数据将进一步检验 MLLM 在 UI 任务上的效力，并为微调模型创建更广博的基准。

<!-- [原子块 · img]  -->

**EN** Figure 5. Mean Absolute Error (lower is better): This result shows that the mean absolute error for all models consistently is less than 1, with "interesting" being the exception. These results show that the models can reliably score within one point of the human scores when given a Likert scale UI question.

**ZH** 图 5. 平均绝对误差（越低越好）：该结果显示，所有模型的平均绝对误差都始终小于 1，只有“趣味性”是例外。这些结果表明，当给定一个 Likert 量表的 UI 问题时，模型能够可靠地把分数控制在人类分数的 1 分以内。

**EN** There is also the opportunity to study the efficacy of more models and prompting methods. This study revolved mostly around GPT-4o, Claude 3.5 Sonnet, and Llama 3.2; running the same tasks on other models like Google’s Gemini, Qwen, or even GPT-4o mini could unveil even further outcomes and trends. Future studies can utilize the framework established in this study to test a wider range of models. Similarly, there is an opportunity to explore the role that prompting strategies can play in MLLM as a UI judge. For this reason, future studies can explore chain-of-thought and few shot learning methods to explore the impact that these methods have on outputs.

**ZH** 也有机会研究更多模型与提示方法的效力。本研究主要围绕 GPT-4o、Claude 3.5 Sonnet 与 Llama 3.2 展开；在 Google 的 Gemini、Qwen 乃至 GPT-4o mini 等其他模型上运行同样的任务，可能揭示出更多的结果与趋势。未来研究可利用本研究建立的框架去测试更广范围的模型。类似地，也有机会探索提示策略在「MLLM 作为 UI 评判者」中所起的作用。为此，未来研究可探索思维链与少样本学习方法，以考察这些方法对输出的影响。

**EN** Finally, considering that UI design is an iterative process, there is an opportunity for future studies to compare UI designs to their earlier iterations. In the pairwise portion of the study, different UI designs were compared with one another. Instead, there is an opportunity to explore the impact of changing a single color, text, or even the layout, and comparing it with an earlier iteration to measure the degree that small changes within the same design change human and MLLM judgments.

**ZH** 最后，考虑到 UI 设计是一个迭代过程，未来研究有机会把 UI 设计与其早期迭代作比较。在本研究的成对部分，不同的 UI 设计被相互比较；而另一种机会是探索改变单个颜色、文字乃至布局所产生的影响，并把它与此前的迭代版本作比较，以衡量同一设计内部的细微改动在多大程度上改变人类与 MLLM 的判断。

<!-- [原子块 · img]  -->

**EN** ((a)) Browsing & Discovery

**ZH** ((a)) 浏览与发现

<!-- [原子块 · img]  -->

**EN** ((b)) Confirmation & Feedback

**ZH** ((b)) 确认与反馈

<!-- [原子块 · img]  -->

**EN** ((c)) Communication & Engagement

**ZH** ((c)) 沟通与互动

**EN** Figure 6. Three grouped bar charts comparing mean factor scores from humans vs. each model. Human score marked with black line, model scores represented by different bars. Trends show that MLLMs are able to effectively approximate human scores. Also shows how model scoring distributions align with human scores across Browsing & Discovery, Confirmation & Feedback, and Communication & Engagement.

**ZH** 图 6. 三幅分组柱状图，比较人类与各模型的平均因素得分。人类得分以黑色线条标示，模型得分以不同的柱体表示。趋势显示 MLLM 能够有效地逼近人类分数；同时也展示了模型评分分布与人类分数在浏览与发现、确认与反馈、沟通与互动三个领域上的吻合情况。

**EN** Appendix B Additional Results & Prompts

**ZH** 附录 B 补充结果与提示词

**EN** The additional results shown reflect further visualizations of data presented in the main body of the paper. Figure 5 and Figure 6 represent how well MLLMs did on Task 1, with the former representing the mean absolute error (MAE) and the latter being a visual summary of Table 2. Furthermore works like Figure 4, represent potential ablation study data. Here we also present the prompts used to have the MLLMs evaluate the UIs in the same way that the humans did. Figure 7 asks the MLLMs to evaluate the UIs on a 7-point Likert scale on the UI factors presented in Table 1. Figure 8 prompts the MLLMs to compare two UIs to one another on the aforementioned factors and choos a "winner."

**ZH** 此处展示的补充结果，是对正文所呈现数据的进一步可视化。图 5 与图 6 呈现 MLLM 在任务 1 上的表现，前者为平均绝对误差（MAE），后者为表 2 的可视化摘要。此外，图 4 之类的作品展示了潜在的消融研究数据。我们还在此给出用于让 MLLM 以与人类相同方式评估 UI 的提示词。图 7 要求 MLLM 按表 1 所列的 UI 因素在 7 点 Likert 量表上评估 UI；图 8 则提示 MLLM 在上述因素上比较两个 UI 并选出一个“胜者”。

<!-- [原子块 · svg]  -->

**EN** Figure 7. Instructions provided to the MLLMs to evaluate the UI in Section 4.1

**ZH** 图 7. 第 4.1 节中提供给 MLLM 用于评估 UI 的指令。

<!-- [原子块 · svg]  -->

**EN** Figure 8. Instructions provided to the MLLMs for pairwise comparison in Section 4.2.

**ZH** 图 8. 第 4.2 节中提供给 MLLM 用于成对比较的指令。
