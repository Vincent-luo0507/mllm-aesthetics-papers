# GraphicBench：面向语言智能体平面设计的规划基准

> 原标题：GraphicBench: A Planning Benchmark for Graphic Design with Language Agents
> 作者：Dayeon Ki, Tianyi Zhou, Marine Carpuat, Gang Wu, Puneet Mathur, Viswanathan Swaminathan · arXiv:2504.11571 · 2025-04-15

<!-- [原子块 · verbatim] GraphicBench : A Planning Benchmark for Graphic Design with Language Agents -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] Large Language Model (LLM)-powered agents have unlocked new possibilities for automating human tasks. While prior work has focused on well-defined tasks with specified goals, the capabilities of agent -->

**EN** 1 Introduction

**ZH** 1 引言

**EN** Recent advances of Large Language Models (LLM) agents have expanded the potential for automating various human tasks. Prior research has explored different aspects of LLM agent capabilities (Sumers et al. 2024), including tool use (Schick et al. 2023; Qin et al. 2023; Shen et al. 2023; Qin et al. 2024; Liang et al. 2024), reasoning strategies (Wei et al. 2022; Yao et al. 2022; Shinn et al. 2023), and evaluation methods (Zhuge et al. 2024). However, most studies focus on tasks with predefined end-goal states, such as filling out spreadsheets and generating charts (Wu et al. 2024b), or adding items to a shopping cart (Koh et al. 2024).

**ZH** 大语言模型（LLM）智能体的近期进展，拓展了自动化各类人类任务的想象空间。已有研究从多个侧面考察了 LLM 智能体的能力（Sumers et al. 2024），包括工具使用（Schick et al. 2023; Qin et al. 2023; Shen et al. 2023; Qin et al. 2024; Liang et al. 2024）、推理策略（Wei et al. 2022; Yao et al. 2022; Shinn et al. 2023）与评测方法（Zhuge et al. 2024）。然而，多数研究集中于具备预定义终止状态的任务，例如填写电子表格、生成图表（Wu et al. 2024b），或向购物车添加商品（Koh et al. 2024）。

**EN** On the other hand, research on the planning capabilities of LLM agents for creative design tasks remains limited, primarily due to underspecified open-ended goals from users (Guo et al. 2024b; Ge et al. 2025). They require delicate planning that translates a high-level user request into a structured workflow composed of executable sub-tasks that collectively produce the final design. This is inherently complex, posing multiple challenges: (1) A complex design often requires collaborations among multiple experts; (2) A design workflow is usually long-horizon, involving a sequence of decisions for expert selection, action calls, and tool uses, which constitute an expansive action space to explore (Xie et al. 2024); (3) A design plan must accommodate both explicit constraints from user queries (e.g., “the title text color must be white”) and implicit constraints inferred through commonsense reasoning (e.g., “the background should contrast with the color of text elements”) since user queries are often incomplete with unspecified details (Qian et al. 2024b); (4) Assessing design outcomes is inherently subjective, as the notion of better design varies among individuals. These challenges raise a key question: Can LLM agents generate cohesive workflow plans for creative design tasks with only high-level or open-ended user queries provided?

**ZH** 另一方面，关于 LLM 智能体在创意设计任务上规划能力的研究仍然有限，主要原因在于用户的目标往往是欠指定的开放式目标（Guo et al. 2024b; Ge et al. 2025）。这类任务需要精细的规划，把高层用户需求转译为一个由可执行子任务构成的结构化工作流，这些子任务共同产出最终设计。这本质上很复杂，带来多重挑战：（1）一个复杂设计往往需要多位专家协作；（2）设计工作流通常是长时程的，涉及专家选择、动作调用与工具使用的一系列决策，构成一片需要探索的广阔动作空间（Xie et al. 2024）；（3）设计方案必须同时容纳用户查询中的显式约束（如“标题文字颜色必须为白色”）与通过常识推理推断出的隐式约束（如“背景应与文字元素的颜色形成对比”），因为用户查询常常不完整、细节未指明（Qian et al. 2024b）；（4）设计结果的评估本质上是主观的，因为何为更好的设计因人而异。这些挑战引出一个关键问题：在只提供高层或开放式用户查询的情况下，LLM 智能体能否为创意设计任务生成连贯的工作流方案？

<!-- [原子块 · img]  -->

**EN** Figure 1: Overview of the GraphicTown framework. The user query and input image captions are from GraphicBench. The same LLM is used across all steps.

**ZH** 图 1：GraphicTown 框架概览。用户查询与输入图像的说明文字取自 GraphicBench。所有步骤使用同一个 LLM。

**EN** In this paper, we focus on graphic design, a task that is challenging even for humans as it requires specialized knowledge of design tools, cost, and effort (Bedford et al. 2006). We introduce GraphicBench as a testbed (§2), consisting of 1,079 user queries paired with input images, covering four design types – book covers, business cards, postcards, and posters – capturing a broad range of design concepts. We further propose an LLM agent framework, GraphicTown (Figure 1, §3), to evaluate the planning abilities of LLM agents for creative design on GraphicBench. GraphicTown consists of the following steps: (1) generate a design outline based on the user query and image captions; (2) recruit expert agents; (3) generate a workflow for each expert; (4) integrate experts’ workflows into a cohesive plan; (5) retrieve appropriate actions for each step in the plan, and (6) execute the plan to produce a final outcome of the design. For action retrieval, we define a set of 46 actions executable within three environments of web-based design tools.

**ZH** 本文聚焦于平面设计——这是一项即便对人类也颇具挑战的任务，因为它需要设计工具方面的专门知识，并耗费成本与精力（Bedford et al. 2006）。我们提出 GraphicBench 作为测试平台（§2），它包含 1,079 条用户查询及配对的输入图像，覆盖书籍封面、名片、明信片与海报四种设计类型，捕捉了广泛的设计概念。我们进一步提出一个 LLM 智能体框架 GraphicTown（图 1、§3），用以评测 LLM 智能体在 GraphicBench 上面向创意设计的规划能力。GraphicTown 包含以下步骤：（1）依据用户查询与图像说明生成设计提纲；（2）招募专家智能体；（3）为每位专家生成工作流；（4）把各专家的工作流整合为一个连贯的方案；（5）为方案中的每一步检索合适的动作；（6）执行方案以产出最终设计结果。在动作检索方面，我们定义了 46 个可在三套基于网页的设计工具环境中执行的动作。

**EN** We comprehensively evaluate six LLMs, ranging from smaller open-weights models to larger closed-source models, on their ability to deliver a plan of design workflow based on the user query and images. Our key findings are as follows:

**ZH** 我们全面评测了六个 LLM——从较小的开放权重模型到较大的闭源模型——考察它们依据用户查询与图像给出设计工作流方案的能力。主要发现如下：

**EN** • All tested LLM agents can plan design workflows that incorporate both explicit design constraints from user queries and implicit commonsense constraints.

**ZH** • 所有被测的 LLM 智能体都能规划出同时纳入用户查询显式设计约束与隐式常识约束的设计工作流。

**EN** • LLM-generated design workflows often include action sequences that closely align with those in human-developed workflows.

**ZH** • LLM 生成的设计工作流所包含的动作序列，常常与人类编写的工作流高度接近。

**EN** • However, these planned workflows often fail to yield successful execution outcomes. Further error analysis reveals three common failure modes: (1) difficulty in spatial reasoning between design components, (2) lack of coordination across experts to manage global dependencies, and (3) retrieval of invalid actions.

**ZH** • 然而，这些规划出的工作流往往无法产出成功的执行结果。进一步的错误分析揭示出三种常见失效模式：（1）难以对设计构件之间的空间关系做推理；（2）缺乏跨专家的协调来管理全局依赖；（3）检索到无效动作。

**EN** 2 ⟦SLOT_0⟧ GraphicBench

**ZH** 2 ⟦SLOT_0⟧ GraphicBench

**EN** In this section, we outline our dataset curation pipeline for GraphicBench, which contains 1,079 pairs of diverse user queries and input images across four types of graphic design: book covers, business cards, postcards, and posters. The dataset is divided into training and test sets, with the training set containing 5 instances per design type with human-annotated reference plans (20 pairs in total) and the test set comprising 1,059 instances. Detailed distributions and examples are shown in Table 1.

**ZH** 本节概述 GraphicBench 的数据集构建流程。该基准包含 1,079 组多样化的用户查询与输入图像，覆盖书籍封面、名片、明信片与海报四类平面设计。数据集划分为训练集与测试集：训练集包含每种设计类型各 5 个实例，并配有人工标注的参考方案（共 20 组）；测试集包含 1,059 个实例。详细分布与示例见表 1。

<!-- [原子块 · table] Design Type User Query Images & Captions # Train/Test Book Cover Please help me create a travel guide cover design titled ‘Exploring Tuscany’ with a blue sky background, featuring rolling vineyards in -->

**EN** Table 1: Examples of the four design types in GraphicBench. Images & Captions: Input images with associated captions. Appendix B.1 provides the distribution of design concepts.

**ZH** 表 1：GraphicBench 中四种设计类型的示例。图像与说明文字：输入图像及其对应说明。设计概念的分布见附录 B.1。

**EN** Reference Plan Annotation.

**ZH** 参考方案标注。

**EN** We first generate human-annotated user queries and plans for five instances per design type, totaling 20 pairs serving as the training set. To ensure the dataset reflects real-world design needs, we collect screenshots of various design projects shared on the Behance platform22 2 https://www.behance.net/, created by designers using Adobe Creative Cloud (CC) design tools.33 3 https://www.adobe.com/creativecloud Using each screenshot as a reference, we invite three graduate students with experience in Adobe CC tools to collaboratively craft realistic user queries, write workflows, and execute each step in the workflow to produce a final design resembling the reference screenshot. Through this process, we identify key design components associated with each design type, as detailed in Appendix Table 6. Examples of human-annotated user queries, corresponding workflows, and the design outputs are further detailed in Appendix B.2.

**ZH** 我们首先为每种设计类型各生成 5 个实例的人工标注用户查询与方案，共 20 组，作为训练集。为使数据集反映真实的设计需求，我们收集了设计师使用 Adobe Creative Cloud（CC）设计工具创作、并发布在 Behance 平台（https://www.behance.net/）上的各类设计项目截图（Adobe Creative Cloud 参见 https://www.adobe.com/creativecloud）。以每张截图为参考，我们邀请三名熟悉 Adobe CC 工具的研究生协作撰写真实的用户查询、编写工作流，并执行工作流中的每一步，产出与参考截图相近的最终设计。通过这一过程，我们识别出与各设计类型相关联的关键设计要素，详见附录表 6。人工标注的用户查询、相应工作流与设计输出的示例详见附录 B.2。

**EN** Query Construction.

**ZH** 查询构建。

**EN** We incorporate the identified design components as placeholders to form the skeleton of user queries for each design type, which serve as prompt templates (Qian et al. 2024b; Xie et al. 2024; Yoran et al. 2024). For each design type, we prompt GPT-4 (Achiam et al. 2023) to randomly populate the design components in the skeleton queries, as shown in Appendix A.1. Subsequently, we manually give variations in query headers (e.g., “Please help me create a design”, “Could you provide me a design”) to capture diverse phrasing styles in user queries, as illustrated in Table 1.

**ZH** 我们把识别出的设计要素作为占位符，构成每种设计类型的用户查询骨架，用作提示模板（Qian et al. 2024b; Xie et al. 2024; Yoran et al. 2024）。对每种设计类型，我们提示 GPT-4（Achiam et al. 2023）随机填充骨架查询中的设计要素，如附录 A.1 所示。随后，我们手工为查询开头加入变化（如“请帮我做一个设计”“能否给我一个设计”），以捕捉用户查询中多样的措辞风格，如表 1 所示。

**EN** Diversity Check.

**ZH** 多样性检查。

**EN** We observe that directly using the queries generated by GPT-4 presents a challenge, as many queries tend to share similar design concepts (i.e., multiple postcard queries are related to “Happy Birthday”, differing only in trivial aspects such as color choice). To ensure the diversity of the generated user queries and their associated design components, we perform the following steps:

**ZH** 我们发现，直接使用 GPT-4 生成的查询会带来一个问题：许多查询倾向于共享相似的设计概念（例如多条明信片查询都与“生日快乐”有关，仅在颜色选择等细枝末节上不同）。为确保生成的用户查询及其关联设计要素具有多样性，我们执行以下步骤：

**EN** 1. Discard redundant queries with a bi-gram match in any of the design components.

**ZH** 1. 丢弃在任一设计要素上存在二元组匹配的冗余查询。

**EN** 2. Discard highly similar queries with a semantic similarity above 0.8, measured using SentenceBERT (Reimers & Gurevych 2019).

**ZH** 2. 丢弃语义相似度高于 0.8 的高度相似查询，相似度用 SentenceBERT（Reimers & Gurevych 2019）度量。

**EN** Image Pairing.

**ZH** 图像配对。

**EN** Each validated user query includes a short description of the image(s) needed in their design, as shown in Table 1. To map each image description to an image file, we first compile a search pool by collecting images from OpenCLIPArt44 4 https://openclipart.org/ and Public Domain Vectors.55 5 https://publicdomainvectors.org/ Both platforms offer a large collection of vector illustrations suitable for graphic design. We collect 179K and 95K image URL-caption pairs from the websites, forming a 274K image pool for retrieval. From this pool, we retrieve the top-3 images with the highest semantic similarity between the image description in the query and the collected captions, using SentenceBERT for similarity scoring.66 6 We will release the images under the Creative Commonsense Zero (CC0) license.

**ZH** 每条通过校验的用户查询都包含一段对其设计中所需图像的简短描述，如表 1 所示。为把每条图像描述映射到图像文件，我们首先从 OpenCLIPArt（https://openclipart.org/）与 Public Domain Vectors（https://publicdomainvectors.org/）收集图像，汇编成一个检索池。两个平台都提供大量适用于平面设计的矢量插画。我们从这两个网站分别收集了 179K 与 95K 条图像 URL—说明文字配对，构成一个 274K 规模的图像池用于检索。针对查询中的图像描述与所收集说明文字之间的语义相似度，我们用 SentenceBERT 打分，从该池中检索相似度最高的前 3 张图像（我们将以 Creative Commonsense Zero（CC0）许可发布这些图像）。

**EN** Human-LLM Evaluation.

**ZH** 人工—LLM 评测。

**EN** We begin with an automatic evaluation to assess the quality of user queries and the top-3 retrieved images. For each query, we prompt GPT-o177 7 https://openai.com/o1/ to: 1) identify key design components and rate how well each contributes to the overall coherence of the final design on a 5-point Likert scale (1: Not aligned at all, 5: Completely aligned), and 2) rank the three image candidates from 1 (best fit) to 3 (least fit) based on their relevance to the query. To validate the automatic evaluation, we conduct a manual study on a stratified random sample of 200 user queries, with 50 from each design type. Each annotator reviews 25 queries and answers the same questions. Given high inter-annotator agreement between GPT-o1 and human annotations (Cohen’s Kappa88 8 https://en.wikipedia.org/wiki/Cohens_kappa is 0.586 for the first question and Kendall’s ⟦SLOT_1⟧99 9 https://en.wikipedia.org/wiki/Kendall_rank_correlation_coefficient is 0.671 for the second question), we rely on GPT-o1 annotations for filtering. We discard queries that receive a rating of 1 or 2 for any design components and retain only the image ranked as best fit. Further details on the annotation setup are provided in Appendix B.3.

**ZH** 我们首先做自动评测，以评估用户查询与检索到的前 3 张图像的质量。对每条查询，我们提示 GPT-o1（https://openai.com/o1/）完成两件事：1）识别关键设计要素，并在 5 点 Likert 量表上评价每个要素对最终设计整体连贯性的贡献程度（1：完全不契合，5：完全契合）；2）依据与查询的相关性把三个候选图像从 1（最契合）排到 3（最不契合）。为验证自动评测，我们对分层随机抽样的 200 条用户查询（每种设计类型各 50 条）开展人工研究。每位标注员审阅 25 条查询并回答同样的问题。鉴于 GPT-o1 与人工标注之间具有较高的一致性（第一个问题的 Cohen's Kappa（https://en.wikipedia.org/wiki/Cohens_kappa）为 0.586，第二个问题的 Kendall's ⟦SLOT_1⟧（https://en.wikipedia.org/wiki/Kendall_rank_correlation_coefficient）为 0.671），我们采用 GPT-o1 的标注进行过滤。我们丢弃在任一设计要素上得分为 1 或 2 的查询，并只保留排名最契合的那张图像。标注设置的更多细节见附录 B.3。

**EN** 3 GraphicTown

**ZH** 3 GraphicTown

**EN** We present an overview of the GraphicTown framework in Figure 1, which consists of six key steps: 1) generating a design outline based on the user query and image captions from GraphicBench, 2) recruiting experts, 3) generating workflow plans, 4) integrating individual workflows into a cohesive plan, 5) retrieving appropriate action for each step, and 6) executing the plan. All prompts are detailed in Appendix A.2.

**ZH** 我们在图 1 中给出 GraphicTown 框架的概览，它包含六个关键步骤：1）依据 GraphicBench 中的用户查询与图像说明生成设计提纲；2）招募专家；3）生成工作流方案；4）把各工作流整合为一个连贯方案；5）为每个步骤检索合适的动作；6）执行方案。全部提示词详见附录 A.2。

**EN** Design Outline.

**ZH** 设计提纲。

**EN** The first step in effective design involves users providing clear and precise outcome specifications to ensure that generated outputs align with their needs (Weisz et al. 2024). These specifications serve as a foundational framework for guiding subsequent design stages (Li et al. 2024a; Ma et al. 2025). However, user queries might often be vague or lack detail in practice (Qian et al. 2024b). To this end, a particular LLM agent ⟦SLOT_2⟧ is prompted as the “supervisor” to first craft a design outline based on the user query and fill in any missing design components identified during the reference plan annotation process (Appendix Table 6). ⟦SLOT_3⟧ infers unspecified information autonomously, ensuring all necessary details are established before proceeding to the planning phase.

**ZH** 有效设计的第一步，是用户提供清晰而精确的结果规格，以确保生成的输出契合其需求（Weisz et al. 2024）。这些规格构成指导后续设计阶段的基础框架（Li et al. 2024a; Ma et al. 2025）。然而在实践当中，用户查询往往含糊或缺少细节（Qian et al. 2024b）。为此，我们把一个特定的 LLM 智能体 ⟦SLOT_2⟧ 提示为“监督者”，先依据用户查询拟定一份设计提纲，并补全在参考方案标注过程中识别出的、缺失的设计要素（附录表 6）。⟦SLOT_3⟧ 自主推断未指定的信息，确保在进入规划阶段之前一切必要的细节都已确立。

**EN** Expert Recruitment.

**ZH** 专家招募。

**EN** For each user query, ⟦SLOT_4⟧ forms an expert group ⟦SLOT_5⟧ based on the design outline and predefined expert descriptions, and assigns a high-level goal to each expert agent in ⟦SLOT_6⟧. Specifically, we introduce three design expert agents, each with distinct expertise and responsibilities aligned with Adobe CC design tools, which are widely used by professional designers (Son et al. 2024; Yuan et al. 2024b).1010 10 We consider the three most commonly used Adobe CC design tools among designers on the Behance platform (https://www.behance.net/). Each expert agent is outlined below, with detailed descriptions in Appendix A.2:

**ZH** 对每条用户查询，⟦SLOT_4⟧ 依据设计提纲与预定义的专家描述组建一个专家组 ⟦SLOT_5⟧，并为 ⟦SLOT_6⟧ 中的每个专家智能体分派一个高层目标。具体地，我们引入三个设计专家智能体，各自具备不同的专长与职责，并与专业设计师广泛使用的 Adobe CC 设计工具相对应（Son et al. 2024; Yuan et al. 2024b）（我们选取 Behance 平台（https://www.behance.net/）上设计师最常用的三款 Adobe CC 设计工具）。各专家智能体概述如下，详细描述见附录 A.2：

**EN** • ⟦SLOT_7⟧ Photo Editor: An agent with an expertise in Adobe Photoshop,1111 11 https://www.adobe.com/products/photoshop responsible for image editing, color correction, and applying filters.

**ZH** • ⟦SLOT_7⟧ 图像编辑师：精通 Adobe Photoshop 的智能体（https://www.adobe.com/products/photoshop），负责图像编辑、色彩校正与滤镜应用。

**EN** • ⟦SLOT_8⟧ Vector Graphic Editor: An agent with an expertise in Adobe Illustrator,1212 12 https://www.adobe.com/products/illustrator focused on creating and editing vector illustrations.

**ZH** • ⟦SLOT_8⟧ 矢量图形编辑师：精通 Adobe Illustrator 的智能体（https://www.adobe.com/products/illustrator），专注于矢量插画的创建与编辑。

**EN** • ⟦SLOT_9⟧ Layout Designer: An agent with an expertise in Adobe InDesign,1313 13 https://www.adobe.com/products/indesign responsible for customizing layout templates, exporting files, and integrating text with visual elements.

**ZH** • ⟦SLOT_9⟧ 版式设计师：精通 Adobe InDesign 的智能体（https://www.adobe.com/products/indesign），负责定制版式模板、导出文件，以及把文字与视觉元素加以整合。

**EN** Workflow Generation.

**ZH** 工作流生成。

**EN** Planning a design workflow is inherently a long-horizon task, requiring a large number of sequential steps to complete a single design. To this end, instead of generating the entire workflow plan in one step, we distribute the process across agents in the recruited expert group, denoted as ⟦SLOT_10⟧. Each ⟦SLOT_11⟧ plans its own workflow ⟦SLOT_12⟧ based on the design outline and assigned high-level goal. To emulate human problem-solving process (Zhu et al. 2023), ⟦SLOT_13⟧ is instructed to decompose its high-level goal into a sequence of actionable sub-goals (Yang et al. 2024; Wu et al. 2024b; Zheng et al. 2025), which further facilitates accurate retrieval of actions (Huang et al. 2024).

**ZH** 规划一个设计工作流本质上是一项长时程任务，完成单个设计往往需要大量顺序步骤。为此，我们没有一步生成整份工作流方案，而是把这一过程分摊到所招募专家组中的各个智能体上，记为 ⟦SLOT_10⟧。每个 ⟦SLOT_11⟧ 依据设计提纲与分派到的高层目标，规划自己的工作流 ⟦SLOT_12⟧。为模拟人类解决问题的过程（Zhu et al. 2023），⟦SLOT_13⟧ 被指示把其高层目标分解为一系列可执行的子目标（Yang et al. 2024; Wu et al. 2024b; Zheng et al. 2025），这也有助于更准确地检索动作（Huang et al. 2024）。

**EN** Workflow Supervision.

**ZH** 工作流监督。

**EN** Since the workflow generation step is conducted independently for each ⟦SLOT_14⟧, dependencies between agents are not explicitly considered. Simply aggregating individual workflow plans can lead to issues such as: 1) multiple agents might perform the same task or 2) when one agent relies on files generated by another, file names may be inconsistently used. To address these challenges, we adopt a hierarchical agentic structure, where a lead agent (⟦SLOT_15⟧) directs one or more specialized agents (⟦SLOT_16⟧) to perform tasks as needed by independently communicating with them (Ahilan & Dayan 2019; Guo et al. 2024a; Fourney et al. 2024; Zhang et al. 2025). Therefore, ⟦SLOT_17⟧ integrates the individual workflows ⟦SLOT_18⟧ from each ⟦SLOT_19⟧ into a single cohesive workflow ⟦SLOT_20⟧, ensuring that interdependencies within and between agents are properly resolved.

**ZH** 由于工作流生成步骤是就每个 ⟦SLOT_14⟧ 独立进行的，智能体之间的依赖关系并未被显式考虑。简单地把各份工作流方案汇总，可能导致如下问题：1）多个智能体可能重复执行同一任务；2）当一个智能体依赖另一个智能体生成的文件时，文件名可能被不一致地使用。为应对这些挑战，我们采用一种层次化的智能体结构：由一个主导智能体（⟦SLOT_15⟧）按需指示一个或多个专用智能体（⟦SLOT_16⟧）执行任务，并独立地与它们通信（Ahilan & Dayan 2019; Guo et al. 2024a; Fourney et al. 2024; Zhang et al. 2025）。因此，⟦SLOT_17⟧ 把个体工作流 ⟦SLOT_18⟧——它们分别来自各个 ⟦SLOT_19⟧——整合为单一连贯的工作流 ⟦SLOT_20⟧，确保智能体内部与智能体之间的相互依赖得到妥善解决。

**EN** Action Retrieval+Execution.

**ZH** 动作检索与执行。

**EN** For each step in ⟦SLOT_21⟧, ⟦SLOT_22⟧ retrieves an appropriate action and infers parameter values to generate ⟦SLOT_23⟧ for execution within the Adobe CC scripting environment.1414 14 Adobe CC design tools do not support direct API calls. As shown in Table 2, we define 46 available actions across the three expert agents, categorized into four basic operations, 13 drawing functions, 11 text-related functions, and 18 object manipulation functions.1515 15 We identify common actions based on Adobe’s tutorial videos (https://www.adobe.com/learn). Each agent has access to a subset of these actions, with each action corresponding to a single mouse or keyboard operation (e.g., Create a new document) (He et al. 2024) and is linked to an executable JavaScript code that takes a list of parameter values.1616 16 Since current models struggle to generate executable code directly from long, complex plans (Ge et al. 2024), we provide manually written JavaScript codes that only require parameter values as inputs. Parameter keys for each action are defined based on Adobe’s scripting guides. We show an example of JavaScript code snippet in Appendix Figure 11. When ⟦SLOT_24⟧ involves multiple expert agents, actions are executed sequentially within their respective environments, leading to the final design outcome ⟦SLOT_25⟧.

**ZH** 对于 ⟦SLOT_21⟧ 中的每一步，⟦SLOT_22⟧ 检索一个合适的动作并推断参数取值，生成 ⟦SLOT_23⟧ 以在 Adobe CC 脚本环境中执行（Adobe CC 设计工具不支持直接 API 调用）。如表 2 所示，我们为三个专家智能体定义了 46 个可用动作，分为四类基本操作、13 个绘图函数、11 个文字相关函数与 18 个对象操作函数（我们依据 Adobe 的教学视频（https://www.adobe.com/learn）确定常用动作）。每个智能体只能访问这些动作的一个子集；每个动作对应一次鼠标或键盘操作（例如“新建文档”）（He et al. 2024），并链接到一段以参数值列表为输入的可执行 JavaScript 代码（由于当前模型难以直接从冗长复杂的方案生成可执行代码（Ge et al. 2024），我们提供人工编写的 JavaScript 代码，它们只需要参数值作为输入）。每个动作的参数键依据 Adobe 的脚本指南定义。我们在附录图 11 中给出一段 JavaScript 代码示例。当 ⟦SLOT_24⟧ 涉及多个专家智能体时，动作在各自环境中顺序执行，最终产出设计结果 ⟦SLOT_25⟧。

<!-- [原子块 · table] Category Action Parameters Description Experts Basic CreateDocument docType Create new document with pre-defined dimensions. SetBackgroundColor red, green, blue Set the background color to desired RGB -->

**EN** Table 2: Actions in GraphicTown. Each action requires specific parameters for execution. Experts: The expert(s) which supports the execution of a specific action. The complete list of 46 available actions is provided in Table 8 of Appendix.

**ZH** 表 2：GraphicTown 中的动作。每个动作的执行需要特定参数。专家：支持执行某一动作的专家智能体。46 个可用动作的完整列表见附录表 8。

**EN** 4 Experiment Setup

**ZH** 4 实验设置

**EN** 4.1 Models

**ZH** 4.1 模型

**EN** We evaluate the design planning abilities of various LLMs on GraphicBench using the GraphicTown framework. Due to the extensive textual information involved in the planning process, we limit our evaluation to LLMs capable of processing inputs exceeding 8K in length. We benchmark five open-weights models across different model sizes and families: LLaMA-3.1 8b (Grattafiori et al. 2024), Gemma-2 9b and 27b (Team et al. 2024), and Qwen-2.5 7b and 14b (Qwen et al. 2025), and one closed-source model: GPT-3.5.1717 17 https://openai.com/index/chatgpt/ For open-weights models, we set the sampling temperature to 0.0.1818 18 HuggingFace model names for open-weights models are listed in Appendix Table 5.

**ZH** 我们用 GraphicTown 框架评测各 LLM 在 GraphicBench 上的设计规划能力。由于规划过程涉及的文本信息量很大，我们只评测能够处理长度超过 8K 输入的 LLM。我们基准测试了五个不同规模与系列的开放权重模型：LLaMA-3.1 8b（Grattafiori et al. 2024）、Gemma-2 9b 与 27b（Team et al. 2024）、Qwen-2.5 7b 与 14b（Qwen et al. 2025），以及一个闭源模型：GPT-3.5（https://openai.com/index/chatgpt/）。对开放权重模型，我们把采样温度设为 0.0（开放权重模型的 HuggingFace 模型名列于附录表 5）。

**EN** 4.2 Evaluation Metrics

**ZH** 4.2 评测指标

**EN** To ensure a comprehensive evaluation of workflow plans ⟦SLOT_26⟧ and execution outcomes ⟦SLOT_27⟧, we assess them across multiple dimensions. Detailed prompts are provided in Appendix A.3.

**ZH** 为全面评测工作流方案 ⟦SLOT_26⟧ 与执行结果 ⟦SLOT_27⟧，我们从多个维度加以评估。详细提示词见附录 A.3。

**EN** Workflow Evaluation.

**ZH** 工作流评测。

**EN** To evaluate ⟦SLOT_28⟧, we define four evaluation criteria:

**ZH** 为评估 ⟦SLOT_28⟧，我们定义四项评测标准：

**EN** • Delivery Rate: This metric measures whether agents can successfully deliver a workflow within a limited number of steps. The step limit is determined by the difficulty level, based on the number of expert agents involved: 1) Easy: 1 expert, max 10 steps; 2) Medium: 2 experts, max 20 steps; 3) Hard: 3 experts, max 30 steps.1919 19 The maximum number of steps is determined by the average steps in human-annotated workflows. Workflow that fall into dead loops or exceed the step limit are considered as failures (Xie et al. 2024).

**ZH** • 交付率（Delivery Rate）：该指标度量智能体能否在限定步数内成功交付一份工作流。步数上限依难度等级而定，难度由所涉及的专家智能体数量决定：1）简单：1 位专家，最多 10 步；2）中等：2 位专家，最多 20 步；3）困难：3 位专家，最多 30 步（最大步数由人工标注工作流中的平均步数确定）。陷入死循环或超出步数上限的工作流被判为失败（Xie et al. 2024）。

**EN** • Design Pass Rate: This metric assesses whether agents can correctly incorporate both explicit design components specified in the user query and implicit commonsense constraints. We prompt GPT-4 to provide a score from 1 to 5 for each of the three aspects: color, text, and images.

**ZH** • 设计通过率（Design Pass Rate）：该指标评估智能体能否正确纳入用户查询中指定的显式设计要素与隐式常识约束。我们提示 GPT-4 对颜色、文字、图像三个方面各给出 1 至 5 的分数。

**EN** • Step Efficiency: We measure the ratio of non-duplicate steps to the total number of steps.

**ZH** • 步骤效率（Step Efficiency）：我们度量非重复步骤数占总步数的比例。

**EN** • Expert Use Efficiency: Since a single workflow might involve multiple expert agents, we define efficiency as minimizing the frequency of switching between expert agents. A higher efficiency score indicates fewer transitions and better expert utilization. Formally, for a workflow ⟦SLOT_29⟧ with ⟦SLOT_30⟧ steps and ⟦SLOT_31⟧ unique experts:

**ZH** • 专家使用效率（Expert Use Efficiency）：由于单个工作流可能涉及多位专家智能体，我们把效率定义为最小化专家智能体之间的切换频率。效率得分越高，说明切换越少、专家利用越充分。形式化地，对于一个工作流 ⟦SLOT_29⟧，若它含 ⟦SLOT_30⟧ 个步骤、涉及 ⟦SLOT_31⟧ 位不同专家：

<!-- [原子块 · table] 𝐄𝐱𝐩𝐞𝐫𝐭𝐔𝐬𝐞𝐄𝐟𝐟 . ( W ) = E − 1 ∑ i = 1 N 𝟙 ​ ( expert i ≠ expert i − 1 ) \mathbf{ExpertUseEff.}(W)=\frac{E-1}{\sum^{N}_{i=1}\mathds{1}(\mathrm{expert}_{i}\neq\mathrm{expert}_{i-1})} (1) -->

**EN** Execution Evaluation.

**ZH** 执行评测。

**EN** To evaluate ⟦SLOT_32⟧, we define five evaluation criteria:

**ZH** 为评估 ⟦SLOT_32⟧，我们定义五项评测标准：

**EN** • Execution Success Rate: This metric measures the success rate of execution attempts, calculated as the percentage of successful executions out of the total executions performed.

**ZH** • 执行成功率（Execution Success Rate）：该指标度量执行尝试的成功率，计算为成功执行次数占全部执行次数的百分比。

**EN** • Fidelity: A successful design should correctly incorporate the input images specified in the user query. We quantify fidelity using template matching from opencv library.2020 20 https://docs.opencv.org/4.x/d4/dc6/tutorial_py_template_matching.html

**ZH** • 保真度（Fidelity）：一次成功的设计应正确纳入用户查询中指定的输入图像。我们用 opencv 库的模板匹配来量化保真度（https://docs.opencv.org/4.x/d4/dc6/tutorial_py_template_matching.html）。

**EN** • Content Similarity: We measure the semantic similarity between the user query and the execution outcome using CLIPScore (Hessel et al. 2021).

**ZH** • 内容相似度（Content Similarity）：我们用 CLIPScore（Hessel et al. 2021）度量用户查询与执行结果之间的语义相似度。

**EN** • VQA Pass Rate: We measure whether the execution outcome aligns with the design components in the user query using Visual Question Answering (VQA) (Agrawal et al. 2016). We generate questions for each query by prompting GPT-4.2121 21 On average, 9.07, 10.0, 7.89, 8.70 questions are generated per user query for book covers, business cards, postcards, and posters, respectively. Examples of questions are detailed in Appendix Table 4. We use a recent multimodal model LLaVA-1.5 7b (Liu et al. 2024) to generate answers as Yes or No (Zhao et al. 2024a). The final pass rate is the average accuracy across all questions.

**ZH** • VQA 通过率（VQA Pass Rate）：我们用视觉问答（VQA）（Agrawal et al. 2016）度量执行结果是否契合用户查询中的设计要素。我们通过提示 GPT-4 为每条查询生成问题（平均而言，书籍封面、名片、明信片与海报每类每条用户查询分别生成 9.07、10.0、7.89、8.70 个问题）。问题示例详见附录表 4。我们使用较新的多模态模型 LLaVA-1.5 7b（Liu et al. 2024）生成是/否答案（Zhao et al. 2024a）。最终通过率为所有问题上的平均准确率。

**EN** • Creativity: Following Torrance 1966; Runco & Jaeger 2012; Zhao et al. 2024b, we assess the creativity of our design outcomes along two axes: 1) Originality, which measures the uniqueness of the design, and 2) Elaboration, which measures the extent to which the design expands on the information in the user query by adding meaningful details. We prompt GPT-o1 to provide a score from 1 to 5 for each axis.

**ZH** • 创造性（Creativity）：沿用 Torrance 1966; Runco & Jaeger 2012; Zhao et al. 2024b，我们沿两个轴评估设计结果的创造性：1）独创性（Originality），度量设计的独特性；2）精细度（Elaboration），度量设计在用户查询信息之上通过增添有意义的细节所作的延展程度。我们提示 GPT-o1 为每个轴给出 1 至 5 的分数。

**EN** 5 Results

**ZH** 5 结果

**EN** In this section, we discuss the performance of various LLMs in terms of planning design workflows and the executed design outcomes. We highlight several main findings below:

**ZH** 本节讨论各 LLM 在规划设计工作流方面以及所执行设计结果上的表现。我们重点给出以下几项主要发现：

<!-- [原子块 · img]  -->

**EN** Figure 2: Workflow evaluation results for each model. We normalize color, text, and images pass rates to [0,1].

**ZH** 图 2：各模型的工作流评测结果。我们把颜色、文字与图像的通过率归一化到 [0,1]。

**EN** LLM agents can generate workflow plans that meet design constraints.

**ZH** LLM 智能体能生成满足设计约束的工作流方案。

**EN** As shown in Figure 2, all tested models plan for design workflows that efficiently utilize expert agents, achieving an average efficiency score of 1.0 and a high average step efficiency of 0.947. Interestingly, larger models are not the top performers in terms of design pass rate. GPT-3.5 and Gemma-2 27b, despite their size, exhibit relatively lower performance across all three design aspects compared to smaller models. In contrast, larger models outperform their smaller 7-9b counterparts in terms of delivery rate. Overall, the models demonstrate strong performance across tested workflow evaluation metrics, indicating that their generated plans efficiently utilize expert agents, decompose high-level goals to distinct steps, and well-incorporate both explicit design constraints from user queries and implicit commonsense constraints. Full numerical results by model and design type are provided in Appendix C.1.

**ZH** 如图 2 所示，所有被测模型规划出的设计工作流都能高效利用专家智能体，平均效率得分为 1.0，平均步骤效率高达 0.947。有趣的是，在设计通过率上，较大的模型并非表现最好。GPT-3.5 与 Gemma-2 27b 尽管规模更大，在三个方面上的表现都相对低于更小的模型。相比之下，较大的模型在交付率上优于其 7–9b 的同类。总体而言，各模型在被测的工作流评测指标上表现良好，说明它们生成的方案能高效利用专家智能体、把高层目标分解到不同步骤，并较好地同时纳入用户查询的显式设计约束与隐式常识约束。按模型与设计类型分列的完整数值结果见附录 C.1。

**EN** Specific expert agent sequences are preferred.

**ZH** 存在偏好的专家智能体序列。

**EN** On average, 2.05 expert agents are recruited per user query. All LLMs, except Qwen-2.5 7b, predominately use the Photo Editor and Layout Designer combination during planning, regardless of design type. This is likely due to the complementary expertise of these two agents and the specialized role of the Vector Graphic Editor, which focuses on creating vector illustrations. Since user queries in GraphicBench already have associated input images, only few require generating from scratch. The workload distribution also varies across expert agents, with the Layout Designer handling the most workflow steps on average (12.2), followed by the Vector Graphic Editor (9.87), and the Photo Editor (7.92). Additionally, LLMs tend to follow a preferred sequence of agents in their plans, most commonly Photo Editor → Layout Designer. Detailed results are provided in Appendix C.2.

**ZH** 平均而言，每条用户查询会招募 2.05 位专家智能体。除 Qwen-2.5 7b 外，所有 LLM 在规划时都主要使用图像编辑师与版式设计师的组合，与设计类型无关。这很可能源于二者专长的互补性，以及矢量图形编辑师专注于创建矢量插画的专门角色——由于 GraphicBench 中的用户查询已配有相关输入图像，只有少数需要从零开始生成。各专家智能体的工作量分布也不均衡：版式设计师平均承担的工作流步骤最多（12.2），其次是矢量图形编辑师（9.87），再次是图像编辑师（7.92）。此外，LLM 在其方案中倾向于遵循某种偏好的智能体顺序，最常见的是图像编辑师 ⟶ 版式设计师。详细结果见附录 C.2。

**EN** Specific type and sequence of actions are preferred.

**ZH** 存在偏好的动作类型与序列。

**EN** In Appendix C.3, we present the distribution of retrieved actions across models. We observe that each expert agent tends to use only a limited set of actions, despite having access to a broader range: the Photo Editor agent primarily performs object manipulation (e.g., ImportObject, ResizeObject), while the Layout Designer agent frequently applies text-related operations (e.g., AlignText, ColorText). We further show that the most common action sequences in planned workflows closely mirror human-annotated workflows (Appendix B.2), typically starting with document creation, setting the background color, importing and manipulating images, and concluding with text modifications. This suggests that prior findings that models resemble human reasoning process (Wei et al. 2023) extend to more open-ended, creative tasks such as graphic design generation.

**ZH** 我们在附录 C.3 中给出各模型检索动作的分布。我们观察到，尽管可访问的动作范围更广，每个专家智能体往往只使用其中有限的一组：图像编辑师智能体主要执行对象操作（如 ImportObject、ResizeObject），而版式设计师智能体则频繁应用文字相关操作（如 AlignText、ColorText）。我们还表明，规划工作流中最常见的动作序列与人工标注的工作流高度相似（附录 B.2），通常从创建文档开始，接着设置背景色、导入并操作图像，最后以文字修改收尾。这说明“模型与人类推理过程相似”这一既有发现（Wei et al. 2023），同样适用于平面设计生成这类更开放、更具创造性的任务。

**EN** Planned workflows do not lead to successful design outcomes.

**ZH** 规划出的工作流无法带来成功的设计结果。

**EN** We detail the execution results in Table 3, which shows that despite high scores on workflow evaluation metrics, the resulting design workflows actually fail to produce successful design outcomes. In most cases, models correctly import the required images but misplace them, frequently causing overflow beyond document boundaries, which contributes to low fidelity rate. This aligns with prior findings that LLMs struggle with spatial reasoning and object positioning within a given space (Yamada et al. 2024; Wu et al. 2024a). Content similarity and VQA pass rates are also generally low, with Gemma-2 27b outperforming other models on both metrics, yet still achieving only 20.79 and 39.64, respectively. All models also exhibit similarly low creativity scores in both originality and elaboration, averaging 1.88 and 1.63. This shows that they struggle to introduce novel elements or expand on the provided details. We provide several case studies of failed executions in Appendix C.5. Taken together, these results suggest that while LLM agents effectively incorporate high-level design constraints in their planned workflows, they often fail to capture finer-grained details, such as spatial relationships between different design components.

**ZH** 我们在表 3 中详列执行结果，该表显示：尽管工作流评测指标得分很高，所得到的设计工作流实际上却无法产出成功的设计结果。在多数情况下，模型能正确导入所需图像，却把它们放错位置，常常导致图像溢出文档边界，这造成了较低的保真率。这与既有发现一致：LLM 在空间推理与在给定空间内定位物体上存在困难（Yamada et al. 2024; Wu et al. 2024a）。内容相似度与 VQA 通过率同样普遍偏低，其中 Gemma-2 27b 在两个指标上都优于其他模型，但也仅分别为 20.79 与 39.64。所有模型在独创性与精细度两项创造性得分上也同样偏低，平均为 1.88 与 1.63。这说明它们难以引入新颖元素，也难以在给定细节之上作延展。我们在附录 C.5 中给出若干执行失败的案例研究。综合来看，这些结果表明：虽然 LLM 智能体能有效地把高层设计约束纳入其规划的工作流，它们却常常无法捕捉更细粒度的细节，例如不同设计构件之间的空间关系。

<!-- [原子块 · table] Model Success Rate (%) Fidelity Content Similarity VQA Pass Rate Creativity (O) Creativity (E) LLaMA-3.1 8b 85.14 0.161 20.20 39.27 1.81 1.55 Gemma-2 9b 82.23 0.178 19.71 37.60 1.93 1.60 Gemma-2 27b 5 -->

**EN** Table 3: Execution results for each model. Full results per design type are provided in Appendix C.4. Best scores for each column is bold. Creativity (O): Originality, (E): Elaboration.

**ZH** 表 3：各模型的执行结果。按设计类型分列的完整结果见附录 C.4。每列最优得分以粗体标出。创造性（O）：独创性；（E）：精细度。

**EN** 6 Error Analysis

**ZH** 6 错误分析

<!-- [原子块 · img]  -->

**EN** Figure 3: Error distribution per model. Most errors arise from models failing to resolve dependencies or retrieving invalid actions.

**ZH** 图 3：各模型的错误分布。多数错误源自模型未能解决依赖关系或检索到无效动作。

**EN** In this section, we aim to understand the underlying reasons why the planned workflows often fail to produce successful design outcomes. We automatically categorize errors for each step in the workflow into the following types: 1) Format: the workflow has formatting issues (e.g., not in proper JSON list format) and cannot be loaded for execution; 2) Invalid Expert: the workflow step assigns an invalid expert agent (e.g., Text Editor); 3) Invalid Action: the retrieved action is not defined in the available action set (e.g., ApplyArialFont); 4) Invalid Parameters: the provided parameter keys do not match the expected inputs for the action (e.g., doc for CreateDocument); 5) Dependency: the workflow step cannot be executed due to a broken dependency from a previous step (e.g., attempting to ImportObject a file that has not been previously saved). We show the distribution of error types per model in Figure 3, from which we have the following observations:

**ZH** 本节旨在理解规划出的工作流为何常常无法产出成功设计结果的深层原因。我们把工作流中每一步的错误自动归类为以下几种类型：1）格式（Format）：工作流存在格式问题（例如不符合规范的 JSON 列表格式），无法加载执行；2）无效专家（Invalid Expert）：该工作流步骤指派了一个无效的专家智能体（例如 Text Editor）；3）无效动作（Invalid Action）：检索到的动作未在可用动作集中定义（例如 ApplyArialFont）；4）无效参数（Invalid Parameters）：所提供的参数键与该动作的预期输入不匹配（例如 CreateDocument 的 doc）；5）依赖（Dependency）：由于前序步骤的依赖断裂，该工作流步骤无法执行（例如试图 ImportObject 一个此前尚未保存的文件）。我们在图 3 中给出各模型错误类型的分布，由此得到以下观察：

**EN** 1. The majority of errors stem from dependency issues, accounting for an average of 53.0% of errors. Dependency errors can be categorized into 1) local dependencies, which occur between steps within a single workflow, and 2) global dependencies, which occur between expert agents. We observe that all models particularly struggle with handling global dependencies, such as correctly using an expert agent’s output as input for the next agent or avoiding redundant steps across different expert agents.

**ZH** 1. 多数错误源自依赖问题，平均占错误的 53.0%。依赖错误可分为两类：1）局部依赖，出现在单个工作流内部的步骤之间；2）全局依赖，出现在专家智能体之间。我们观察到，所有模型在处理全局依赖上尤其吃力，例如正确地把一个专家智能体的输出用作下一个智能体的输入，或避免不同专家智能体之间的冗余步骤。

**EN** 2. In models such as Gemma-2 9b and Qwen-2.5 14b, invalid functions contribute the most to errors. Despite having access to the full list of available actions and parameters during retrieval, agents still fail to use the correct function names in their workflow plans. This motivates further exploration into more reliable action retrieval methods.

**ZH** 2. 在 Gemma-2 9b 与 Qwen-2.5 14b 等模型中，无效函数对错误的贡献最大。尽管在检索时可以访问完整的可用动作与参数列表，智能体仍未能在其工作流方案中使用正确的函数名。这促使人们进一步探索更可靠的动作检索方法。

**EN** 3. Other errors, invalid parameters, invalid expert assignments, and formatting issues, have smaller impact, contributing an average of 5.96%, 0.77%, and 0.17% of errors, respectively.

**ZH** 3. 其他错误——无效参数、无效专家指派与格式问题——影响较小，平均分别占错误的 5.96%、0.77% 与 0.17%。

**EN** As a whole, these results highlight the challenges LLM agents face in global planning and retrieving correct actions, which underscores the need for new strategies to enhance multi-step reasoning and dependency resolution during design planning.

**ZH** 总体而言，这些结果凸显了 LLM 智能体在全局规划与检索正确动作上所面临的挑战，也说明需要新的策略来强化设计规划中的多步推理与依赖求解。

**EN** 7 Related Work

**ZH** 7 相关工作

**EN** LLM-Based Agents.

**ZH** 基于 LLM 的智能体。

**EN** Leveraging the strengths of Large Language Models (LLMs), LLM-based agents have demonstrated strong performance in automating human tasks through tool use (Schick et al. 2023; Qin et al. 2023; Shen et al. 2023; Qin et al. 2024; Liang et al. 2024) and reasoning (Yao et al. 2022; Shinn et al. 2023). Further inspired by human society and the goal of improving work efficiency through collaboration (O’Reilly et al. 1997; Woolley et al. 2015), recent research has explored frameworks involving multiple agents (Ding et al. 2023; Shen et al. 2023; Dong et al. 2024; Chen et al. 2024). In particular, studies suggest that assigning specialized roles to agents improves their effectiveness in solving complex tasks (Li et al. 2023; Chen et al. 2023; Talebirad & Nadiri 2023; Du et al. 2024; Hong et al. 2024; Qian et al. 2024a). Similarly, we adapt an LLM-based agentic framework, but for a previously unexplored task in this research space: graphic design generation.

**ZH** 借助大语言模型（LLM）的优势，基于 LLM 的智能体已在通过工具使用（Schick et al. 2023; Qin et al. 2023; Shen et al. 2023; Qin et al. 2024; Liang et al. 2024）与推理（Yao et al. 2022; Shinn et al. 2023）自动化人类任务方面表现出强劲实力。进一步地，受人类社会与通过协作提升工作效率这一目标启发（O'Reilly et al. 1997; Woolley et al. 2015），近期研究探索了涉及多个智能体的框架（Ding et al. 2023; Shen et al. 2023; Dong et al. 2024; Chen et al. 2024）。特别地，有研究表明，为智能体分派专门角色能提升其解决复杂任务的有效性（Li et al. 2023; Chen et al. 2023; Talebirad & Nadiri 2023; Du et al. 2024; Hong et al. 2024; Qian et al. 2024a）。我们也采用了一个基于 LLM 的智能体框架，但面向的是这一研究空间中此前未被探索的任务：平面设计生成。

**EN** Graphic Design Generation.

**ZH** 平面设计生成。

**EN** Graphic design is a form of visual art that combines multimodal elements (e.g., images, texts, and vector symbols) to create aesthetic compositions that effectively comunicate the intent of a user query (Cheng et al. 2024). Prior work has explored various design sub-tasks, including layout generation (Li et al. 2019; Gupta et al. 2021; Jiang et al. 2023), typography generation (Zhao et al. 2018; Jiang et al. 2019), and colorization (Yuan et al. 2021; Qiu et al. 2023). However, limited attention has been given to planning the entire graphic design process (Inoue et al. 2024), particularly in the context of agents, and our work aims to fill this gap.

**ZH** 平面设计是一种视觉艺术形式，它把多模态元素（如图像、文字与矢量符号）组合起来，创造出能有效传达用户查询意图的美学构成（Cheng et al. 2024）。已有工作探索了设计的各个子任务，包括版式生成（Li et al. 2019; Gupta et al. 2021; Jiang et al. 2023）、字体排印生成（Zhao et al. 2018; Jiang et al. 2019）与上色（Yuan et al. 2021; Qiu et al. 2023）。然而，对平面设计全流程的规划关注有限（Inoue et al. 2024），在智能体语境下尤其如此，而我们的工作正是要填补这一空白。

**EN** 8 Conclusion

**ZH** 8 结论

**EN** We introduce ⟦SLOT_33⟧ GraphicBench, a benchmark for graphic design generation that evaluates the design planning abilities of LLM agents (§2). We further present GraphicTown, an LLM agent framework designed to emulate human group planning process for creative design tasks (§3). Our evaluation with six LLMs show that while models can plan for workflows that incorporate both explicit and implicit design constraints, these planned workflows fall short in (1) understanding spatial relationships and positioning of design components, (2) recognizing global dependencies between expert agents, and (3) retrieving appropriate actions at each step. We envision GraphicBench as a valuable stepping stone for future work on enhancing design planning and reasoning in LLM agents.

**ZH** 我们提出 ⟦SLOT_33⟧ GraphicBench——一个面向平面设计生成的基准，用于评测 LLM 智能体的设计规划能力（§2）。我们进一步提出 GraphicTown，一个旨在模拟人类团队在创意设计任务上规划过程的 LLM 智能体框架（§3）。我们对六个 LLM 的评测表明：虽然模型能规划出同时纳入显式与隐式设计约束的工作流，这些规划出的工作流却在以下三方面不足：（1）理解设计构件的空间关系与摆放位置；（2）识别专家智能体之间的全局依赖；（3）在每一步检索到合适的动作。我们希望 GraphicBench 能成为一块有价值的铺路石，推动未来在强化 LLM 智能体设计规划与推理方面的研究。

**EN** 9 Limitations

**ZH** 9 局限性

**EN** GraphicBench assumes a scenario in which user queries explicitly specify the text and image content, as well as the precise attributes such as color and text position. However, in realistic settings, users may not always specify or even know exactly what images to include in a design, or they may express their requests at a very high-level (Ge et al. 2025). Future works can explore scenarios where user input is limited, requiring models to seek clarification or request additional details through interactions with users (Qian et al. 2024b; Li et al. 2024b). Additionally, the number of actions available for GraphicTown agents is currently limited to a fixed set of 46, as each corresponding JavaScript code was manually written by the authors. This set is not exhaustive of all possible actions within the Adobe CC scripting environment. Future works could investigate automated methods for dynamically generating and retrieving actions (Yuan et al. 2024a).

**ZH** GraphicBench 假定这样一种场景：用户查询会明确指定文字与图像内容，以及颜色与文字位置等精确属性。然而在真实场景中，用户未必总能指明、甚至未必清楚设计中要包含哪些图像，也可能只以非常高层的方式表达需求（Ge et al. 2025）。未来工作可以探索用户输入受限的场景，要求模型通过与用户的交互来寻求澄清或请求更多细节（Qian et al. 2024b; Li et al. 2024b）。此外，GraphicTown 智能体可用的动作数量目前限于固定的 46 个，因为每段对应的 JavaScript 代码都由作者手工编写。这一集合并未穷尽 Adobe CC 脚本环境中所有可能的动作。未来工作可以研究动态生成与检索动作的自动化方法（Yuan et al. 2024a）。

**EN** Our experiments primarily focus on evaluating the performance of LLMs with GraphicBench, as the amount of textual information involved in the planning process outweighs the image content. Therefore, a key complementary study still remains – evaluating GraphicBench with visual language models. This would require modifying our current setup to directly prompt models with raw image files instead of using image captions as input, which we leave for future work.

**ZH** 我们的实验主要聚焦于用 GraphicBench 评测 LLM 的表现，因为规划过程涉及的文本信息量远超图像内容。因此，一项关键的补充研究仍然缺失——用视觉语言模型评测 GraphicBench。这需要我们改造现有设置，直接以原始图像文件而非图像说明作为模型输入，我们把这一点留待未来工作。

**EN** Acknowledgments

**ZH** 致谢

**EN** We would like to thank our collaborators at Adobe Research for their valuable feedback, including Alexa Siu, Tong Sun, Saayan Mitra, and Stefano Petrangeli. Dayeon is especially grateful for the Adobe Research intern cohort for making the internship experience memorable, including Nishant Balepur, Dang Nguyen, Vishakh Padmakumar, Paiheng Xu, Hyunji Lee, and Yoonjoo Lee.

**ZH** 我们感谢 Adobe Research 的合作者提出的宝贵反馈，包括 Alexa Siu、Tong Sun、Saayan Mitra 与 Stefano Petrangeli。Dayeon 特别感谢 Adobe Research 实习同期伙伴，让这段实习经历难以忘怀，包括 Nishant Balepur、Dang Nguyen、Vishakh Padmakumar、Paiheng Xu、Hyunji Lee 与 Yoonjoo Lee。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] Achiam et al. (2023) Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. Gpt-4 technica -->

<!-- [原子块 · verbatim] Agrawal et al. (2016) Aishwarya Agrawal, Jiasen Lu, Stanislaw Antol, Margaret Mitchell, C. Lawrence Zitnick, Dhruv Batra, and Devi Parikh. Vqa: Visual question answering, 2016. URL https://arxiv.org/a -->

<!-- [原子块 · verbatim] Ahilan & Dayan (2019) Sanjeevan Ahilan and Peter Dayan. Feudal multi-agent hierarchies for cooperative reinforcement learning. arXiv preprint arXiv:1901.08492 , 2019. -->

<!-- [原子块 · verbatim] Bedford et al. (2006) Tim Bedford, John Quigley, and Lesley Walls. Expert elicitation for reliable system design. Statistical Science , 21(4), November 2006. ISSN 0883-4237. doi: 10.1214/0883423060000 -->

<!-- [原子块 · verbatim] Chen et al. (2024) Guangyao Chen, Siwei Dong, Yu Shu, Ge Zhang, Jaward Sesay, Börje Karlsson, Jie Fu, and Yemin Shi. Autoagents: a framework for automatic agent generation. In Proceedings of the Thirt -->

<!-- [原子块 · verbatim] Chen et al. (2023) Weize Chen, Yusheng Su, Jingwei Zuo, Cheng Yang, Chenfei Yuan, Chi-Min Chan, Heyang Yu, Yaxi Lu, Yi-Hsin Hung, Chen Qian, Yujia Qin, Xin Cong, Ruobing Xie, Zhiyuan Liu, Maosong Sun, -->

<!-- [原子块 · verbatim] Cheng et al. (2024) Yutao Cheng, Zhao Zhang, Maoke Yang, Hui Nie, Chunyuan Li, Xinglong Wu, and Jie Shao. Graphic design with large multimodal model, 2024. URL https://arxiv.org/abs/2404.14368 . -->

<!-- [原子块 · verbatim] Ding et al. (2023) Shiying Ding, Xinyi Chen, Yan Fang, Wenrui Liu, Yiwu Qiu, and Chunlei Chai. Designgpt: Multi-agent collaboration in design, 2023. URL https://arxiv.org/abs/2311.11591 . -->

<!-- [原子块 · verbatim] Dong et al. (2024) Yubo Dong, Xukun Zhu, Zhengzhe Pan, Linchao Zhu, and Yi Yang. Villageragent: A graph-based multi-agent framework for coordinating complex task dependencies in minecraft, 2024. URL h -->

<!-- [原子块 · verbatim] Du et al. (2024) Zhuoyun Du, Chen Qian, Wei Liu, Zihao Xie, Yifei Wang, Yufan Dang, Weize Chen, and Cheng Yang. Multi-agent software development through cross-team collaboration, 2024. URL https://arx -->

<!-- [原子块 · verbatim] Fourney et al. (2024) Adam Fourney, Gagan Bansal, Hussein Mozannar, Cheng Tan, Eduardo Salinas, Erkang, Zhu, Friederike Niedtner, Grace Proebsting, Griffin Bassman, Jack Gerrits, Jacob Alber, Peter Ch -->

<!-- [原子块 · verbatim] Ge et al. (2024) Jiaxin Ge, Sanjay Subramanian, Baifeng Shi, Roei Herzig, and Trevor Darrell. Recursive visual programming, 2024. URL https://arxiv.org/abs/2312.02249 . -->

<!-- [原子块 · verbatim] Ge et al. (2025) Jiaxin Ge, Zora Zhiruo Wang, Xuhui Zhou, Yi-Hao Peng, Sanjay Subramanian, Qinyue Tan, Maarten Sap, Alane Suhr, Daniel Fried, Graham Neubig, and Trevor Darrell. Autopresent: Designing  -->

<!-- [原子块 · verbatim] Grattafiori et al. (2024) Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Alex Vaughan, Amy Yang, Angel -->

<!-- [原子块 · verbatim] Guo et al. (2024a) Taicheng Guo, Xiuying Chen, Yaqi Wang, Ruidi Chang, Shichao Pei, Nitesh V. Chawla, Olaf Wiest, and Xiangliang Zhang. Large language model based multi-agents: A survey of progress an -->

<!-- [原子块 · verbatim] Guo et al. (2024b) Yuxuan Guo, Shaohui Peng, Jiaming Guo, Di Huang, Xishan Zhang, Rui Zhang, Yifan Hao, Ling Li, Zikang Tian, Mingju Gao, Yutai Li, Yiming Gan, Shuai Liang, Zihao Zhang, Zidong Du, Qi  -->

<!-- [原子块 · verbatim] Gupta et al. (2021) Kamal Gupta, Justin Lazarow, Alessandro Achille, Larry S Davis, Vijay Mahadevan, and Abhinav Shrivastava. Layouttransformer: Layout generation and completion with self-attention. I -->

<!-- [原子块 · verbatim] He et al. (2024) Hongliang He, Wenlin Yao, Kaixin Ma, Wenhao Yu, Yong Dai, Hongming Zhang, Zhenzhong Lan, and Dong Yu. WebVoyager: Building an end-to-end web agent with large multimodal models. In Lun -->

<!-- [原子块 · verbatim] Hessel et al. (2021) Jack Hessel, Ari Holtzman, Maxwell Forbes, Ronan Le Bras, and Yejin Choi. CLIPScore: A reference-free evaluation metric for image captioning. In Marie-Francine Moens, Xuanjing Hua -->

<!-- [原子块 · verbatim] Hong et al. (2024) Sirui Hong, Mingchen Zhuge, Jiaqi Chen, Xiawu Zheng, Yuheng Cheng, Ceyao Zhang, Jinlin Wang, Zili Wang, Steven Ka Shing Yau, Zijuan Lin, Liyang Zhou, Chenyu Ran, Lingfeng Xiao, Chen -->

<!-- [原子块 · verbatim] Huang et al. (2024) Tenghao Huang, Dongwon Jung, Vaibhav Kumar, Mohammad Kachuee, Xiang Li, Puyang Xu, and Muhao Chen. Planning and editing what you retrieve for enhanced tool learning. In Kevin Duh,  -->

<!-- [原子块 · verbatim] Inoue et al. (2024) Naoto Inoue, Kento Masui, Wataru Shimoda, and Kota Yamaguchi. Opencole: Towards reproducible automatic graphic design generation, 2024. URL https://arxiv.org/abs/2406.08232 . -->

<!-- [原子块 · verbatim] Jiang et al. (2019) Shuhui Jiang, Zhaowen Wang, Aaron Hertzmann, Hailin Jin, and Yun Fu. Visual font pairing. IEEE Transactions on Multimedia , 22(8):2086–2097, 2019. -->

<!-- [原子块 · verbatim] Jiang et al. (2023) Zhaoyun Jiang, Jiaqi Guo, Shizhao Sun, Huayu Deng, Zhongkai Wu, Vuksan Mijovic, Zijiang James Yang, Jian-Guang Lou, and Dongmei Zhang. Layoutformer++: Conditional graphic layout ge -->

<!-- [原子块 · verbatim] Koh et al. (2024) Jing Yu Koh, Robert Lo, Lawrence Jang, Vikram Duvvur, Ming Lim, Po-Yu Huang, Graham Neubig, Shuyan Zhou, Russ Salakhutdinov, and Daniel Fried. VisualWebArena: Evaluating multimodal a -->

<!-- [原子块 · verbatim] Li et al. (2023) Guohao Li, Hasan Abed Al Kader Hammoud, Hani Itani, Dmitrii Khizbullin, and Bernard Ghanem. Camel: communicative agents for ”mind” exploration of large language model society. In Proc -->

<!-- [原子块 · verbatim] Li et al. (2019) Jianan Li, Jimei Yang, Aaron Hertzmann, Jianming Zhang, and Tingfa Xu. Layoutgan: Generating graphic layouts with wireframe discriminators. arXiv preprint arXiv:1901.06767 , 2019. -->

<!-- [原子块 · verbatim] Li et al. (2024a) Mengming Li, Wenji Fang, Qijun Zhang, and Zhiyao Xie. Specllm: Exploring generation and review of vlsi design specification with large language model, 2024a. URL https://arxiv.org/ab -->

<!-- [原子块 · verbatim] Li et al. (2024b) Shuyue Stella Li, Vidhisha Balachandran, Shangbin Feng, Jonathan S. Ilgen, Emma Pierson, Pang Wei Koh, and Yulia Tsvetkov. Mediq: Question-asking LLMs and a benchmark for reliable in -->

<!-- [原子块 · verbatim] Liang et al. (2024) Yaobo Liang, Chenfei Wu, Ting Song, Wenshan Wu, Yan Xia, Yu Liu, Yang Ou, Shuai Lu, Lei Ji, Shaoguang Mao, et al. Taskmatrix. ai: Completing tasks by connecting foundation models w -->

<!-- [原子块 · verbatim] Liu et al. (2024) Haotian Liu, Chunyuan Li, Yuheng Li, and Yong Jae Lee. Improved baselines with visual instruction tuning. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Rec -->

<!-- [原子块 · verbatim] Ma et al. (2025) Lezhi Ma, Shangqing Liu, Yi Li, Xiaofei Xie, and Lei Bu. Specgen: Automated generation of formal program specifications via large language models, 2025. URL https://arxiv.org/abs/2401 -->

<!-- [原子块 · verbatim] O’Reilly et al. (1997) Charles O’Reilly, Katherine Phillips, and Sigal Barsade. Group demography and innovation: Does diversity help? Research on managing groups and teams , 1, 01 1997. -->

<!-- [原子块 · verbatim] Qian et al. (2024a) Chen Qian, Wei Liu, Hongzhang Liu, Nuo Chen, Yufan Dang, Jiahao Li, Cheng Yang, Weize Chen, Yusheng Su, Xin Cong, Juyuan Xu, Dahai Li, Zhiyuan Liu, and Maosong Sun. ChatDev: Commun -->

<!-- [原子块 · verbatim] Qian et al. (2024b) Cheng Qian, Bingxiang He, Zhong Zhuang, Jia Deng, Yujia Qin, Xin Cong, Zhong Zhang, Jie Zhou, Yankai Lin, Zhiyuan Liu, and Maosong Sun. Tell me more! towards implicit user intentio -->

<!-- [原子块 · verbatim] Qin et al. (2023) Yujia Qin, Shihao Liang, Yining Ye, Kunlun Zhu, Lan Yan, Yaxi Lu, Yankai Lin, Xin Cong, Xiangru Tang, Bill Qian, et al. Toolllm: Facilitating large language models to master 16000+ r -->

<!-- [原子块 · verbatim] Qin et al. (2024) Yujia Qin, Shengding Hu, Yankai Lin, Weize Chen, Ning Ding, Ganqu Cui, Zheni Zeng, Xuanhe Zhou, Yufei Huang, Chaojun Xiao, et al. Tool learning with foundation models. ACM Computing  -->

<!-- [原子块 · verbatim] Qiu et al. (2023) Qianru Qiu, Xueting Wang, and Mayu Otani. Multimodal color recommendation in vector graphic documents. In Proceedings of the 31st ACM International Conference on Multimedia , pp. 400 -->

<!-- [原子块 · verbatim] Qwen et al. (2025) Qwen, :, An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan Li, Dayiheng Liu, Fei Huang, Haoran Wei, Huan Lin, Jian Yang, Jianhong Tu, Jianwei Zhang, J -->

<!-- [原子块 · verbatim] Reimers & Gurevych (2019) Nils Reimers and Iryna Gurevych. Sentence-BERT: Sentence embeddings using Siamese BERT-networks. In Kentaro Inui, Jing Jiang, Vincent Ng, and Xiaojun Wan (eds.), Proceedings  -->

<!-- [原子块 · verbatim] Runco & Jaeger (2012) Mark A Runco and Garrett J Jaeger. The standard definition of creativity. Creativity research journal , 24(1):92–96, 2012. -->

<!-- [原子块 · verbatim] Schick et al. (2023) Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Eric Hambro, Luke Zettlemoyer, Nicola Cancedda, and Thomas Scialom. Toolformer: Language models can te -->

<!-- [原子块 · verbatim] Shen et al. (2023) Yongliang Shen, Kaitao Song, Xu Tan, Dongsheng Li, Weiming Lu, and Yueting Zhuang. Hugginggpt: Solving ai tasks with chatgpt and its friends in hugging face, 2023. URL https://arxiv -->

<!-- [原子块 · verbatim] Shinn et al. (2023) Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. Reflexion: Language agents with verbal reinforcement learning, 2023. URL https://a -->

<!-- [原子块 · verbatim] Son et al. (2024) Kihoon Son, DaEun Choi, Tae Soo Kim, and Juho Kim. Demystifying tacit knowledge in graphic design: Characteristics, instances, approaches, and guidelines. In Proceedings of the 2024  -->

<!-- [原子块 · verbatim] Sumers et al. (2024) Theodore R. Sumers, Shunyu Yao, Karthik Narasimhan, and Thomas L. Griffiths. Cognitive architectures for language agents, 2024. URL https://arxiv.org/abs/2309.02427 . -->

<!-- [原子块 · verbatim] Talebirad & Nadiri (2023) Yashar Talebirad and Amirhossein Nadiri. Multi-agent collaboration: Harnessing the power of intelligent llm agents, 2023. URL https://arxiv.org/abs/2306.03314 . -->

<!-- [原子块 · verbatim] Team et al. (2024) Gemma Team, Morgane Riviere, Shreya Pathak, Pier Giuseppe Sessa, Cassidy Hardin, Surya Bhupatiraju, Léonard Hussenot, Thomas Mesnard, Bobak Shahriari, Alexandre Ramé, Johan Ferret,  -->

<!-- [原子块 · verbatim] Torrance (1966) E Paul Torrance. Torrance tests of creative thinking. Educational and psychological measurement , 1966. -->

<!-- [原子块 · verbatim] Wei et al. (2022) Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models. Advances -->

<!-- [原子块 · verbatim] Wei et al. (2023) Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc Le, and Denny Zhou. Chain-of-thought prompting elicits reasoning in large language models, -->

<!-- [原子块 · verbatim] Weisz et al. (2024) Justin D. Weisz, Jessica He, Michael Muller, Gabriela Hoefer, Rachel Miles, and Werner Geyer. Design principles for generative ai applications. In Proceedings of the 2024 CHI Confe -->

<!-- [原子块 · verbatim] Woolley et al. (2015) Anita Williams Woolley, Christopher F. Chabris, Alex Pentland, Nada Hashmi, and Thomas W. Malone. Collective intelligence and group performance. Current Directions in Psychologic -->

<!-- [原子块 · verbatim] Wu et al. (2024a) Wenshan Wu, Shaoguang Mao, Yadong Zhang, Yan Xia, Li Dong, Lei Cui, and Furu Wei. Mind’s eye of LLMs: Visualization-of-thought elicits spatial reasoning in large language models. In  -->

<!-- [原子块 · verbatim] Wu et al. (2024b) Zhiyong Wu, Chengcheng Han, Zichen Ding, Zhenmin Weng, Zhoumianze Liu, Shunyu Yao, Tao Yu, and Lingpeng Kong. Os-copilot: Towards generalist computer agents with self-improvement, 20 -->

<!-- [原子块 · verbatim] Xie et al. (2024) Jian Xie, Kai Zhang, Jiangjie Chen, Tinghui Zhu, Renze Lou, Yuandong Tian, Yanghua Xiao, and Yu Su. Travelplanner: A benchmark for real-world planning with language agents. In Forty- -->

<!-- [原子块 · verbatim] Yamada et al. (2024) Yutaro Yamada, Yihan Bao, Andrew Kyle Lampinen, Jungo Kasai, and Ilker Yildirim. Evaluating spatial understanding of large language models. Transactions on Machine Learning Resear -->

<!-- [原子块 · verbatim] Yang et al. (2024) Ruihan Yang, Jiangjie Chen, Yikai Zhang, Siyu Yuan, Aili Chen, Kyle Richardson, Yanghua Xiao, and Deqing Yang. Selfgoal: Your language agents already know how to achieve high-level  -->

<!-- [原子块 · verbatim] Yao et al. (2022) Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao. React: Synergizing reasoning and acting in language models. arXiv preprint arXiv:2210.0362 -->

<!-- [原子块 · verbatim] Yoran et al. (2024) Ori Yoran, Samuel Joseph Amouyal, Chaitanya Malaviya, Ben Bogin, Ofir Press, and Jonathan Berant. Assistantbench: Can web agents solve realistic and time-consuming tasks?, 2024. UR -->

<!-- [原子块 · verbatim] Yuan et al. (2024a) Lifan Yuan, Yangyi Chen, Xingyao Wang, Yi R. Fung, Hao Peng, and Heng Ji. Craft: Customizing llms by creating and retrieving from specialized toolsets, 2024a. URL https://arxiv.org -->

<!-- [原子块 · verbatim] Yuan et al. (2021) Lin-Ping Yuan, Ziqi Zhou, Jian Zhao, Yiqiu Guo, Fan Du, and Huamin Qu. Infocolorizer: Interactive recommendation of color palettes for infographics. IEEE Transactions on Visualizati -->

<!-- [原子块 · verbatim] Yuan et al. (2024b) Mingyue Yuan, Jieshan Chen, Yongquan Hu, Sidong Feng, Mulong Xie, Gelareh Mohammadi, Zhenchang Xing, and Aaron Quigley. Towards human-ai synergy in ui design: Enhancing multi-agent -->

<!-- [原子块 · verbatim] Zhang et al. (2025) Cong Zhang, Xin Deik Goh, Dexun Li, Hao Zhang, and Yong Liu. Planning with multi-constraints via collaborative language agents. In Owen Rambow, Leo Wanner, Marianna Apidianaki, Hen -->

<!-- [原子块 · verbatim] Zhao et al. (2024a) Hengyuan Zhao, Pan Zhou, Difei Gao, Zechen Bai, and Mike Zheng Shou. LOVA3: Learning to visual question answering, asking and assessment. In The Thirty-eighth Annual Conference on  -->

<!-- [原子块 · verbatim] Zhao et al. (2018) Nanxuan Zhao, Ying Cao, and Rynson WH Lau. Modeling fonts in context: Font prediction on web designs. In Computer Graphics Forum , volume 37, pp. 385–395. Wiley Online Library, 2018 -->

<!-- [原子块 · verbatim] Zhao et al. (2024b) Yunpu Zhao, Rui Zhang, Wenyi Li, Di Huang, Jiaming Guo, Shaohui Peng, Yifan Hao, Yuanbo Wen, Xing Hu, Zidong Du, Qi Guo, Ling Li, and Yunji Chen. Assessing and understanding creati -->

<!-- [原子块 · verbatim] Zheng et al. (2025) Xinyue Zheng, Haowei Lin, Kaichen He, Zihao Wang, Zilong Zheng, and Yitao Liang. Mcu: An evaluation framework for open-ended game agents, 2025. URL https://arxiv.org/abs/2310.08367 -->

<!-- [原子块 · verbatim] Zhu et al. (2023) Xizhou Zhu, Yuntao Chen, Hao Tian, Chenxin Tao, Weijie Su, Chenyu Yang, Gao Huang, Bin Li, Lewei Lu, Xiaogang Wang, Yu Qiao, Zhaoxiang Zhang, and Jifeng Dai. Ghost in the minecraft:  -->

<!-- [原子块 · verbatim] Zhuge et al. (2024) Mingchen Zhuge, Changsheng Zhao, Dylan Ashley, Wenyi Wang, Dmitrii Khizbullin, Yunyang Xiong, Zechun Liu, Ernie Chang, Raghuraman Krishnamoorthi, Yuandong Tian, Yangyang Shi, Vikas -->

**EN** Appendix A Prompt Templates

**ZH** 附录 A 提示词模板

**EN** We show prompt templates used for constructing queries in GraphicBench (§A.1), prompting LLMs for each step in GraphicTown (§A.2), and evaluating for design pass rate using GPT-4 as a judge (§A.3).

**ZH** 我们给出构建 GraphicBench 查询所用的提示词模板（§A.1）、在 GraphicTown 各步骤提示 LLM 所用的模板（§A.2），以及以 GPT-4 为评审评测设计通过率所用的模板（§A.3）。

**EN** A.1 GraphicBench Prompts

**ZH** A.1 GraphicBench 提示词

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

<!-- [原子块 · table] Design Type User Query Questions Book Cover Please create a self-help book cover design titled ‘Achieve Your Dreams’ with the author’s name ‘Nathan White’, featuring a person climbing a mountain cente -->

**EN** Table 4: Examples of the generated questions using GPT-4 per design type. We use the questions for computing the VQA pass rate as part of execution evaluation (§4.2).

**ZH** 表 4：按设计类型列出用 GPT-4 生成的问题示例。我们把这些问题用于计算 VQA 通过率，作为执行评测的一部分（§4.2）。

**EN** A.2 GraphicTown Prompts

**ZH** A.2 GraphicTown 提示词

<!-- [原子块 · table] Model HuggingFace Name LLaMA-3.1 8b meta-llama/Llama-3.1-8B-Instruct Gemma-2 9b google/gemma-2-9b-it Gemma-2 27b google/gemma-2-27b-it Qwen-2.5 7b Qwen/Qwen2.5-7B-Instruct Qwen-2.5 14b Qwen/Qwen2.5-14 -->

**EN** Table 5: HuggingFace model names for the tested open-weights models.

**ZH** 表 5：被测开放权重模型的 HuggingFace 模型名。

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

**EN** A.3 Evaluation Prompts

**ZH** A.3 评测提示词

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

**EN** Appendix B Details on GraphicBench

**ZH** 附录 B GraphicBench 细节

**EN** B.1 Design Concept Distribution

**ZH** B.1 设计概念分布

**EN** We provide a detailed distribution of design concepts by design type in Figure 4. We prompt GPT-4 to identify the main theme or event outlined in the user query and categorize into predefined categories. We show that the distribution spans a diverse range of categories, which highlights the benchmark’s breadth and variety.

**ZH** 我们在图 4 中给出按设计类型划分的设计概念详细分布。我们提示 GPT-4 识别用户查询中概述的主题或事件，并将其归入预定义类别。结果显示该分布跨越了多样的类别，凸显了本基准的广度与多样性。

<!-- [原子块 · img]  -->

**EN** (a) Book Cover

**ZH** (a) 书籍封面

<!-- [原子块 · img]  -->

**EN** (b) Business Card

**ZH** (b) 名片

<!-- [原子块 · img]  -->

**EN** (c) Postcard

**ZH** (c) 明信片

<!-- [原子块 · img]  -->

**EN** (d) Poster

**ZH** (d) 海报

**EN** Figure 4: Distribution of design concepts by design type in GraphicBench. We automatically extract the main theme (e.g., postcard) or event (e.g., poster) from each user query and categorize it based on predefined categories.

**ZH** 图 4：GraphicBench 中按设计类型划分的设计概念分布。我们自动从每条用户查询中抽取主要主题（如明信片）或事件（如海报），并依预定义类别归类。

**EN** B.2 Reference Plan Annotation

**ZH** B.2 参考方案标注

**EN** We detail examples of human-annotated user queries and design outputs in Table 7 and their corresponding workflow plans in Figures 5 to 8. We use the same Adobe CC design tool combinations as specified by the designers of the references from the Behance platform. We show the identified key design components for each design type in Table 6. The average number of text and image elements included in each query are 3.05, 1.33 for book covers, 2.15 and 1.00 for business cards, 1.03 and 1.28 for postcards, and 1.99 and 1.04 for posters.

**ZH** 我们在表 7 中详列人工标注的用户查询与设计输出示例，其对应的工作流方案见图 5 至图 8。我们使用与 Behance 平台上参考设计的设计师所指定的相同的 Adobe CC 设计工具组合。我们在表 6 中给出为每种设计类型识别出的关键设计要素。每条查询中包含的文字与图像元素的平均数量为：书籍封面 3.05 与 1.33，名片 2.15 与 1.00，明信片 1.03 与 1.28，海报 1.99 与 1.04。

<!-- [原子块 · table] Design Type Design Components Required? Book Cover Background color ✓ Title (content, size, color, position) ✓ Author Name (content, size, color, position) ✓ Subtitle (content, size, color, position)  -->

**EN** Table 6: Design components for each design type (book cover, business card, postcard, poster), which are associated with sub-components listed in parentheses. Required?: Indicates whether the component is explicitly required in the user query during query construction. Note that even when a component is required, its sub-component details may be missing from the user query.

**ZH** 表 6：各设计类型（书籍封面、名片、明信片、海报）的设计要素，及其括号中所列的子要素。是否必需：指示该要素在查询构建时是否被用户查询显式要求。请注意，即便某要素为必需，其子要素细节也可能未出现在用户查询中。

<!-- [原子块 · table] Design Type User Query Reference Design Generated Design App Book Cover Create a book cover design for a romance novel titled ‘Love \n Story’ featuring a silhouette illustration of a couple in a roman -->

**EN** Table 7: Example of human-annotated user queries and corresponding design outputs along with their reference outputs for each design type. Tool: Adobe CC design tool(s) used to generate the design output. We use the same combination of tools specified by the designers of the reference designs from the Behance platform.

**ZH** 表 7：按设计类型列出人工标注的用户查询示例、相应设计输出及其参考输出。工具：生成设计输出所用的 Adobe CC 设计工具。我们使用与 Behance 平台上参考设计的设计师所指定的相同的工具组合。

<!-- [原子块 · svg]  -->

**EN** Figure 5: Human-annotated workflow plan for the book cover example in Table 7.

**ZH** 图 5：表 7 中书籍封面示例的人工标注工作流方案。

<!-- [原子块 · svg]  -->

**EN** Figure 6: Human-annotated workflow plan for the business card example in Table 7.

**ZH** 图 6：表 7 中名片示例的人工标注工作流方案。

<!-- [原子块 · svg]  -->

**EN** Figure 7: Human-annotated workflow plan for the postcard example in Table 7.

**ZH** 图 7：表 7 中明信片示例的人工标注工作流方案。

<!-- [原子块 · svg]  -->

**EN** Figure 8: Human-annotated workflow plan for the poster example in Table 7.

**ZH** 图 8：表 7 中海报示例的人工标注工作流方案。

**EN** B.3 Human Annotation

**ZH** B.3 人工标注

**EN** We detail the human annotation process as part of constructing GraphicBench. We built our custom annotation interface as illustrated in Figure 9. We invited 8 students to participate and provide a compensation of $10 gift card each. Before the survey, we show examples of both successful and failed cases to provide some context of annotation standards to annotators.

**ZH** 我们详述作为 GraphicBench 构建一环的人工标注过程。我们搭建了自定义的标注界面，如图 9 所示。我们邀请了 8 名学生参与，并向每人提供 10 美元礼品卡作为报酬。在调查开始前，我们展示成功与失败案例的示例，让标注员对标注标准有所了解。

**EN** As part of the pre-survey, annotators were asked two questions on a 5-point Likert scale: (1) Design tool usage: How often do you use design tools in daily work and life? (1: Never, 5: Always) and (2) Adobe Creative Cloud application usage: How familiar are you in using Adobe Creative Cloud Applications (e.g., Photoshop, Illustrator)? (1: Not familiar at all, 5: Extremely familiar). Of the 8 annotators, for design tool usage, 3 responded “Never” (Never in the past month), 4 “Rarely” (Fewer than once a week), and 1 “Sometimes” (two or three times a week). For Adobe Creative Cloud application usage, 3 were “Not familiar at all” (have never used it before), 2 “Slightly familiar” (have some basic knowledge but have rarely used it), and 3 “Moderately familiar” (can perform simple tasks but may need guidance for more complex features).

**ZH** 作为调查前的一部分，标注员被要求在 5 点 Likert 量表上回答两个问题：（1）设计工具使用：你在日常工作与生活中使用设计工具的频率如何？（1：从不，5：总是）；（2）Adobe Creative Cloud 应用使用：你对使用 Adobe Creative Cloud 应用（例如 Photoshop、Illustrator）的熟悉程度如何？（1：完全不熟悉，5：极其熟悉）。在 8 名标注员中，就设计工具使用而言，3 人回答“从不”（过去一个月内从未使用），4 人“很少”（每周少于一次），1 人“有时”（每周两到三次）。就 Adobe Creative Cloud 应用使用而言，3 人“完全不熟悉”（此前从未使用过），2 人“略有了解”（具备一些基础知识但很少使用），3 人“中等熟悉”（能完成简单任务，但在更复杂的功能上可能需要指导）。

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

**EN** Figure 9: Screenshot of human annotation interface. For each query, annotators are asked to 1) evaluate how well each design component aligns with the user query on a 5-point Likert scale and 2) rank the 3 image from 1 to 3 based on their relevance to the query. Additionally, they have the option to provide free-form feedback.

**ZH** 图 9：人工标注界面截图。对每条查询，标注员被要求：1）在 5 点 Likert 量表上评价每个设计要素与用户查询的契合程度；2）依据与查询的相关性把 3 张图像从 1 排到 3。此外，他们还可以选择提供自由形式的反馈。

<!-- [原子块 · table] Category Action Parameters Description Experts Basic CreateDocument docType Create new document with pre-defined dimensions. CreateDocumentCustom width, height Create new document with desired width a -->

**EN** Table 8: Complete list of available actions in GraphicTown. Each action requires specific parameters for execution. Experts: The expert agent(s) which supports the execution of a specific action. For numerical parameters, we provide reference ranges (e.g., angle as [0, 360], brightness as [-150, +150]). For parameters in filter-related functions, we provide a short description for each (e.g., rippleSize in OcenRippleFilter means “the size of the ripples created, where lower means smaller and finer ripples that creates more subtle water effect”).

**ZH** 表 8：GraphicTown 中可用动作的完整列表。每个动作的执行需要特定参数。专家：支持执行某一动作的专家智能体。对数值型参数，我们提供参考范围（例如 angle 为 [0, 360]，brightness 为 [-150, +150]）。对滤镜相关函数中的参数，我们为每个参数提供简短描述（例如 OcenRippleFilter 中的 rippleSize 表示“所产生的涟漪尺寸，取值越小则涟漪越小越细密，形成更微妙的水面效果”）。

**EN** Appendix C Detailed Results

**ZH** 附录 C 详细结果

**EN** C.1 Workflow Plan Evaluation

**ZH** C.1 工作流方案评测

**EN** We provide the full numerical results by model and design type in Table 9. Each component of the design pass rate (color, text, and images) is later normalized to the range [0,1] in Figure 1. Our results show that most tested models perform well in expert use efficiency and design pass rate, while larger models outperform smaller ones in delivery rate.

**ZH** 我们在表 9 中给出按模型与设计类型分列的完整数值结果。设计通过率的各个分量（颜色、文字、图像）在图 1 中被归一化到 [0,1] 区间。我们的结果表明，多数被测模型在专家使用效率与设计通过率上表现良好，而较大的模型在交付率上优于较小的模型。

<!-- [原子块 · table] Model Design Type Delivery Rate Step Eff. Expert Use Eff. Design Pass Rate Color Text Image LLaMA-3 8b Book Cover 0.092 0.941 1.00 0.938 4.508 4.773 4.792 Business Card 0.148 0.922 1.00 0.948 4.813 4. -->

**EN** Table 9: Workflow plan evaluation results per model and design type. The range for Delivery Rate, Expert Use Efficiency, and Design Pass Rate are [0,1] while the ranges for Color, Text, Visual Pass Rates are [1,5]. Best scores for each column is bold.

**ZH** 表 9：按模型与设计类型分列的工作流方案评测结果。交付率、专家使用效率与设计通过率的取值区间为 [0,1]，而颜色、文字与视觉通过率的区间为 [1,5]。每列最优得分以粗体标出。

**EN** C.2 Expert Distribution

**ZH** C.2 专家分布

**EN** In Table 10, we show detailed results on expert recruitment ratios and workload distribution across models and design types. The expert recruitment ratio is computed as the number of times an expert is recruited per user query, divided by the total number of queries. Workload distribution represented the average number of steps assigned to each expert agent in the workflow plan ⟦SLOT_34⟧. Additionally, we present the distribution of expert agent usage sequences in Table 11. The most common order of sequence across models is Photo Editor → Layout Designer with the highest number of occurrence (4,207 in total), followed by Layout Designer → Photo Editor (504) and Photo Editor → Vector Graphic Editor (262).

**ZH** 我们在表 10 中给出各模型与设计类型上专家招募比例与工作量分布的详细结果。专家招募比例的计算方式为：每位专家被每条用户查询招募的次数除以查询总数。工作量分布表示工作流方案 ⟦SLOT_34⟧ 中分派给每个专家智能体的平均步骤数。此外，我们在表 11 中给出专家智能体使用顺序的分布。跨模型最常见的顺序是图像编辑师 ⟶ 版式设计师，出现次数最高（共 4,207 次），其次是版式设计师 ⟶ 图像编辑师（504）与图像编辑师 ⟶ 矢量图形编辑师（262）。

<!-- [原子块 · table] Model Design Type Ratio Workload Avg. # Agents Avg. # Steps LLaMA-3 8b Book Cover 1.00 0.02 1.00 11.8 9.67 18.3 2.15 31.3 Business Card 1.00 0.01 1.00 10.6 18.0 14.6 2.46 26.0 Postcard 1.00 0.00 1.00  -->

**EN** Table 10: Expert recruitment ratios (Ratio) and workload distribution (Workload) per model and design type. Avg. # Agents: Average number of expert agents recruited per user query; Avg. # Steps: Average number of steps in the workflow plan per user query; ⟦SLOT_35⟧: Photo Editor; ⟦SLOT_36⟧: Vector Graphic Editor; ⟦SLOT_37⟧: Layout Designer.

**ZH** 表 10：按模型与设计类型分列的专家招募比例（Ratio）与工作量分布（Workload）。平均智能体数：每条用户查询平均招募的专家智能体数；平均步骤数：每条用户查询的工作流方案平均步骤数；⟦SLOT_35⟧：图像编辑师；⟦SLOT_36⟧：矢量图形编辑师；⟦SLOT_37⟧：版式设计师。

<!-- [原子块 · table] # of Agents Sequence LLaMA-3 8b Gemma-2 9b Gemma-2 27b Qwen-2.5 7b Qwen-2.5 14b GPT-3.5 1 0 0 1 59 30 10 0 0 0 27 0 0 0 1 0 193 18 3 2 → 0 0 0 262 0 0 → 647 922 622 171 914 931 → 0 0 1 24 0 0 → 0 0 0  -->

**EN** Table 11: Distribution of expert agent usage sequence per model. ⟦SLOT_38⟧: Photo Editor; ⟦SLOT_39⟧: Vector Graphic Editor; ⟦SLOT_40⟧: Layout Designer.

**ZH** 表 11：按模型分列的专家智能体使用顺序分布。⟦SLOT_38⟧：图像编辑师；⟦SLOT_39⟧：矢量图形编辑师；⟦SLOT_40⟧：版式设计师。

**EN** C.3 Action Distribution

**ZH** C.3 动作分布

**EN** We detail results for action distribution across models and expert agents, aggregated over all design types. As shown in Figure 10, each expert agent exhibits clear preferences for specific actions. The Photo Editor agent primarily utilizes object manipulation functions such as ImportObject, ResizeObject, and RepositionObject. Notably, GPT-3.5 frequently applies color correction functions (AdjustHSL, AdjustBC), reflecting the agent’s expertise. The common actions used by the Vector Graphic Editor agent vary by model. LLaMA-3 8b, Gemma-2 27b and GPT-3.5 predominately use object manipulation functions, whereas Gemma-2 9b and Qwen-2.5 7b uses text-related functions. Meanwhile, the Layout Designer agent primarily uses text-related operations such as CreateText, AlignText, and ColorText. Overall, expert agents struggle to utilize advanced text and object manipulation functions, such as OpacityText and PhotoFilter, regardless of the model.

**ZH** 我们给出跨模型与专家智能体、在所有设计类型上聚合的动作分布结果。如图 10 所示，每个专家智能体都对特定动作表现出明确的偏好。图像编辑师智能体主要使用 ImportObject、ResizeObject、RepositionObject 等对象操作函数。值得注意的是，GPT-3.5 频繁应用色彩校正函数（AdjustHSL、AdjustBC），体现了该智能体的专长。矢量图形编辑师智能体常用的动作因模型而异：LLaMA-3 8b、Gemma-2 27b 与 GPT-3.5 主要使用对象操作函数，而 Gemma-2 9b 与 Qwen-2.5 7b 使用文字相关函数。与此同时，版式设计师智能体主要使用 CreateText、AlignText、ColorText 等文字相关操作。总体而言，无论哪个模型，专家智能体都难以利用 OpacityText、PhotoFilter 等高级文字与对象操作函数。

**EN** We present the top-3 most common action sequences per model in Table 12. We observe that most sequences closely follow human-annotated workflows, typically starting with document creation (CreateDocument or CreateDocumentCustom), setting the background color (SetBackgroundColor), importing images as objects (ImportObject), manipulating the imported object (ResizeObject, RepositionObject, etc.), saving the document (SaveDocument), and manipulating text elements (CreateText, ApplyFont, ColorText, etc.).

**ZH** 我们在表 12 中给出各模型最常见的三类动作序列。我们观察到，多数序列与人工标注的工作流高度一致：通常从创建文档（CreateDocument 或 CreateDocumentCustom）开始，接着设置背景色（SetBackgroundColor）、把图像作为对象导入（ImportObject）、操作导入的对象（ResizeObject、RepositionObject 等）、保存文档（SaveDocument），最后操作文字元素（CreateText、ApplyFont、ColorText 等）。

<!-- [原子块 · table] Model Occurrence Action Sequence LLaMA-3 8b 13 CreateDocumentCustom → SetBackgroundColor → ImportObject → ResizeObject → RepositionObject → CreateText → ApplyFont → ColorText → AlignText → ResizeText  -->

**EN** Table 12: Top-3 most common action sequences per model, ordered by frequency. Occurrence: Number of times each specific sequence occurs.

**ZH** 表 12：按模型分列、按频次排序的三类最常见动作序列。出现次数：某一特定序列出现的次数。

<!-- [原子块 · img]  -->

**EN** (a) LLaMA-3 8b ⟦SLOT_41⟧

**ZH** (a) LLaMA-3 8b ⟦SLOT_41⟧

<!-- [原子块 · img]  -->

**EN** (b) LLaMA-3 8b ⟦SLOT_42⟧

**ZH** (b) LLaMA-3 8b ⟦SLOT_42⟧

<!-- [原子块 · img]  -->

**EN** (c) LLaMA-3 8b ⟦SLOT_43⟧

**ZH** (c) LLaMA-3 8b ⟦SLOT_43⟧

<!-- [原子块 · img]  -->

**EN** (d) Gemma-2 9b ⟦SLOT_44⟧

**ZH** (d) Gemma-2 9b ⟦SLOT_44⟧

<!-- [原子块 · img]  -->

**EN** (e) Gemma-2 9b ⟦SLOT_45⟧

**ZH** (e) Gemma-2 9b ⟦SLOT_45⟧

<!-- [原子块 · img]  -->

**EN** (f) Gemma-2 9b ⟦SLOT_46⟧

**ZH** (f) Gemma-2 9b ⟦SLOT_46⟧

<!-- [原子块 · img]  -->

**EN** (g) Gemma-2 27b ⟦SLOT_47⟧

**ZH** (g) Gemma-2 27b ⟦SLOT_47⟧

<!-- [原子块 · img]  -->

**EN** (h) Gemma-2 27b ⟦SLOT_48⟧

**ZH** (h) Gemma-2 27b ⟦SLOT_48⟧

<!-- [原子块 · img]  -->

**EN** (i) Gemma-2 27b ⟦SLOT_49⟧

**ZH** (i) Gemma-2 27b ⟦SLOT_49⟧

<!-- [原子块 · img]  -->

**EN** (j) Qwen-2.5 7b ⟦SLOT_50⟧

**ZH** (j) Qwen-2.5 7b ⟦SLOT_50⟧

<!-- [原子块 · img]  -->

**EN** (k) Qwen-2.5 7b ⟦SLOT_51⟧

**ZH** (k) Qwen-2.5 7b ⟦SLOT_51⟧

<!-- [原子块 · img]  -->

**EN** (l) Qwen-2.5 7b ⟦SLOT_52⟧

**ZH** (l) Qwen-2.5 7b ⟦SLOT_52⟧

<!-- [原子块 · img]  -->

**EN** (m) Qwen-2.5 14b ⟦SLOT_53⟧

**ZH** (m) Qwen-2.5 14b ⟦SLOT_53⟧

<!-- [原子块 · img]  -->

**EN** (n) Qwen-2.5 14b ⟦SLOT_54⟧

**ZH** (n) Qwen-2.5 14b ⟦SLOT_54⟧

<!-- [原子块 · img]  -->

**EN** (o) GPT-3.5 ⟦SLOT_55⟧

**ZH** (o) GPT-3.5 ⟦SLOT_55⟧

<!-- [原子块 · img]  -->

**EN** (p) GPT-3.5 ⟦SLOT_56⟧

**ZH** (p) GPT-3.5 ⟦SLOT_56⟧

<!-- [原子块 · img]  -->

**EN** (q) GPT-3.5 ⟦SLOT_57⟧

**ZH** (q) GPT-3.5 ⟦SLOT_57⟧

**EN** Figure 10: Action distribution per model and expert agent. Actions under 5.0% of usage are grouped as “Others”. ⟦SLOT_58⟧: Photo Editor; ⟦SLOT_59⟧: Vector Graphic Editor; ⟦SLOT_60⟧: Layout Designer.

**ZH** 图 10：按模型与专家智能体分列的动作分布。使用比例低于 5.0% 的动作被归为“其他”。⟦SLOT_58⟧：图像编辑师；⟦SLOT_59⟧：矢量图形编辑师；⟦SLOT_60⟧：版式设计师。

**EN** C.4 Execution Evaluation

**ZH** C.4 执行评测

**EN** We present the detailed numerical results for execution evaluation by model and design type in Table 13.

**ZH** 我们在表 13 中给出按模型与设计类型分列的执行评测详细数值结果。

<!-- [原子块 · table] Model Design Type Success Rate (%) Fidelity Content Similarity VQA Pass Rate Creativity (O) Creativity (E) LLaMA-3 8b Book Cover 90.42 0.157 15.93 34.72 1.79 1.52 Business Card 86.41 0.133 16.71 36.35 -->

**EN** Table 13: Execution results per model and design type. Best scores for each column is bold. Creativity (O): Originality; Creativity (E): Elaboration

**ZH** 表 13：按模型与设计类型分列的执行结果。每列最优得分以粗体标出。创造性（O）：独创性；创造性（E）：精细度

**EN** C.5 Case Studies

**ZH** C.5 案例研究

**EN** In Table 14, we present cases studies of failed executions across design types. We conclude with similar observations from the error analysis (§6):

**ZH** 我们在表 14 中给出跨设计类型的执行失败案例研究。我们得出与错误分析（§6）相似的观察：

**EN** LLM agents lack spatial understanding of design elements.

**ZH** LLM 智能体缺乏对设计元素的空间理解。

**EN** A qualitative analysis of execution outcomes reveals that most failures stem from agents’ lack of spatial understanding and object positioning within a given space. For instance, in the second book cover example by LLaMA-3 8b, the postcard example by Gemma-2 9b, and the first poster example by Qwen-2.5 7b, agents struggle to correctly position text. Additionally, we observe some cases where they fail to correctly position both text and images, such as the second poster example by GPT-3.5.

**ZH** 对执行结果的定性分析显示，多数失败源自智能体缺乏空间理解、无法在给定空间内定位物体。例如，在 LLaMA-3 8b 的第二个书籍封面示例、Gemma-2 9b 的明信片示例，以及 Qwen-2.5 7b 的第一个海报示例中，智能体都难以正确摆放文字。此外，我们还观察到一些文字与图像都没能正确摆放的案例，如 GPT-3.5 的第二个海报示例。

**EN** LLM agents struggle to understand global dependencies.

**ZH** LLM 智能体难以理解全局依赖。

**EN** As shown in Table 14, many failed executions result from failing to recognize global dependencies between expert agents. Consequently, they generate incomplete outcomes, executing only a subset of actions – either text-related (e.g., the first book cover example by LLaMA-3 8b) or image-related operations (e.g., the first business card example by Gemma-2 27b).

**ZH** 如表 14 所示，许多执行失败源于未能识别专家智能体之间的全局依赖。其结果是不完整的输出——只执行了动作的一个子集：要么是文字相关操作（例如 LLaMA-3 8b 的第一个书籍封面示例），要么是图像相关操作（例如 Gemma-2 27b 的第一个名片示例）。

<!-- [原子块 · table] Design Type User Query Execution Outcome Comments (Model) Book Cover Can you assist in creating a historical novel cover design titled ‘Secrets of the Pharaohs’ with the author’s name ‘Liam Hunter’, f -->

**EN** Table 14: Case studies of failed execution outcomes per design type across models. Failures primarily stem from lack of spatial understanding, resulting in incorrect parameter values and misunderstanding of global dependencies between expert agents.

**ZH** 表 14：跨模型、按设计类型分列的执行失败结果案例研究。失败主要源于缺乏空间理解，导致参数取值错误，以及对专家智能体之间全局依赖的误解。

<!-- [原子块 · svg]  -->

**EN** Figure 11: JavaScript code snippet for AdjustBC for the Photo Editor agent.

**ZH** 图 11：图像编辑师智能体的 AdjustBC 所对应的 JavaScript 代码片段。
