# ArtifactsBench：弥合 LLM 代码生成评测中的视觉—交互鸿沟

> 原标题：ArtifactsBench: Bridging the Visual-Interactive Gap in LLM Code Generation Evaluation
> 作者：Chenchen Zhang, Yuhang Li, Can Xu, Jiaheng Liu, Ao Liu, Changzhi Zhou, Ken Deng, Dengpeng Wu, Guanhua Huang, Kejiao Li, Qi Yi, Ruibin Xiong 等 · arXiv:2507.04952 · 2025-07-07

<!-- [原子块 · verbatim] ArtifactsBench: Bridging the Visual-Interactive Gap in LLM Code Generation Evaluation -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] The generative capabilities of Large Language Models (LLMs) are rapidly expanding from static code to dynamic, interactive visual artifacts. This progress is bottlenecked by a critical evaluation gap: -->

**EN** 1 Introduction

**ZH** 1 引言

**EN** Large Language Models (LLMs) are reshaping software creation, extending from conventional code/text to interactive visual artifacts (Jaech et al., 2024; Anthropic, 2025; Guo et al., 2025). These enable responsive web interfaces, data visualizations, and mini-games (Jiang et al., 2024; Lu et al., 2025a). We term an “Artifact” a self-contained, model-generated, executable unit (e.g., web widget, visualization) that integrates code, visuals, and interaction. Despite strong generative capability, rigorous evaluation lags: current tools do not holistically judge visual fidelity and dynamics, forming a bottleneck. WebDev Arena captures human preferences via voting but requires manual evaluation and is difficult to scale (LMSYS Org, 2024). Specifically, the “multimodal instructions” encompass text, images, and interaction logic, while the “interactive visual artifacts” refer to the executable outputs designed and generated based upon these instructions.

**ZH** 大语言模型（LLM）正在重塑软件创作，其能力已从传统的代码与文本扩展到交互式视觉制品（Jaech et al., 2024; Anthropic, 2025; Guo et al., 2025）。这些模型能够生成响应式网页界面、数据可视化与小游戏（Jiang et al., 2024; Lu et al., 2025a）。我们把“Artifact”（制品）定义为一个自包含的、由模型生成的、可执行的单元（如网页组件、可视化图表），它把代码、视觉与交互融为一体。尽管生成能力强大，严谨的评测却相对滞后：现有工具无法对视觉保真度与动态行为做出整体性判断，由此形成瓶颈。WebDev Arena 通过投票捕捉人类偏好，但需要人工评测，难以规模化（LMSYS Org, 2024）。具体地，“多模态指令”涵盖文本、图像与交互逻辑，而“交互式视觉制品”指基于这些指令设计并生成的可执行输出。

**EN** Prevailing benchmarks emphasize static correctness (e.g., pass@k in HumanEval (Chen et al., 2021)) or non-visual functionality (e.g., SWE-Bench (Jimenez et al., 2023)); visual code generation is typically judged via screenshot replication (Wüst et al., 2024; Yun et al., 2024; Wu et al., 2024) or DOM proxies (Xu et al., 2025). None capture the holistic quality of interactive artifacts—layout/aesthetics and dynamic behaviors (responses, state transitions, animations) are under-measured, so evaluation often falls back to costly, subjective manual inspection or unreliable LLM self-evaluation, lacking scale and objectivity. This gap is critical because high-fidelity, functional interactive visual artifacts are central to user experience in modern applications; their quality directly affects real-world adoption.

**ZH** 主流基准强调静态正确性（如 HumanEval 中的 pass@k（Chen et al., 2021））或非视觉功能（如 SWE-Bench（Jimenez et al., 2023））；视觉代码生成通常通过截图复现（Wüst et al., 2024; Yun et al., 2024; Wu et al., 2024）或 DOM 代理指标（Xu et al., 2025）来评判。这些方法都无法刻画交互式制品的整体质量——版式与美学、动态行为（响应、状态转移、动画）都被低估，评测因而常常退回昂贵且主观的人工检查，或不可靠的 LLM 自评，既缺乏规模也缺乏客观性。这一缺口至关重要，因为高保真、可用的交互式视觉制品是现代应用用户体验的核心，其质量直接影响真实场景中的采纳。

**EN** We ask a central question: How can we automatically, holistically, and reliably evaluate an LLM’s ability to transform multimodal instructions—spanning text, images, and interaction logic—into high-quality, executable interactive visual artifacts across diverse prompts? Existing efforts provide partial answers. WebBench emphasizes DOM alignment and task automation; WebGen-Bench and FullFront target web comprehension/generation and the development process; and WebDev Arena captures human preferences through head-to-head voting (Xu et al., 2025; Lu et al., 2025b; Sun et al., 2025; LMSYS Org, 2024). Yet none jointly assess visual fidelity and interaction dynamics in a fully automated, scalable, and code-aware manner, nor do they provide reproducible, fine-grained diagnostics that reveal strengths and failure modes. A viable framework must therefore go beyond static code to assess functionality, visual presentation, and interactive behavior captured via staged execution (e.g., three-step screenshots), and provide fine-grained diagnostics to guide progress.

**ZH** 我们提出一个核心问题：如何自动、整体且可靠地评测 LLM 把多模态指令（涵盖文本、图像与交互逻辑）转化为高质量、可执行的交互式视觉制品的能力，并覆盖多样化的提示？已有工作给出了部分答案。WebBench 强调 DOM 对齐与任务自动化；WebGen-Bench 与 FullFront 面向网页理解/生成与开发流程；WebDev Arena 通过对抗式投票捕捉人类偏好（Xu et al., 2025; Lu et al., 2025b; Sun et al., 2025; LMSYS Org, 2024）。然而它们都没有以全自动、可扩展且代码感知的方式联合评估视觉保真度与交互动态性，也未提供可复现的细粒度诊断来揭示优势与失效模式。因此，一个可行的框架必须超越静态代码，去评估功能性、视觉呈现，以及通过分阶段执行（如三步截图）捕捉到的交互行为，并提供细粒度诊断以指引改进方向。

**EN** Therefore, we introduce ArtifactsBench, a benchmark for evaluating LLMs on interactive visual artifacts. Our design couples deterministic execution with staged visual evidence and checklist-guided, dual-referee judging, enabling holistic, automated, and reproducible evaluation with strong human alignment. We curate 1,825 tasks via a multi-stage pipeline combining expert sourcing with LLM generation and refinement. As shown in Figure 1 and Table 1, tasks span nine domains and are stratified by complexity for fine-grained capability analysis. Our contributions are threefold:

**ZH** 为此，我们提出 ArtifactsBench，一个面向交互式视觉制品的 LLM 评测基准。我们的设计把确定性执行、分阶段视觉证据与清单引导的双评审机制结合起来，使评测具备整体性、自动化、可复现性，并与人类判断高度一致。我们通过融合专家采集与 LLM 生成—精修的多阶段流程，构建了 1,825 个任务。如图 1 与表 1 所示，任务覆盖九个领域，并按复杂度分层，以支持细粒度的能力分析。我们的贡献有三个方面：

**EN** • The first large-scale, hierarchical benchmark for interactive visual artifacts. ArtifactsBench contains 1,825 queries across nine domains (e.g., web, SVG, games, simulations; Figure 1), stratified into Easy/Medium/Hard tiers for discriminative evaluation. This design supports fine-grained capability analysis rather than a single static-correctness score.

**ZH** • 首个面向交互式视觉制品的大规模层次化基准。ArtifactsBench 包含覆盖九个领域（如网页、SVG、游戏、仿真；图 1）的 1,825 条查询，并划分为简单/中等/困难三个层级，以获得有区分度的评测结果。这一设计支持细粒度的能力分析，而非给出一个静态正确性的总分。

**EN** • A multimodal, automated evaluation pipeline with checklist-guided MLLM-as-Judge. We execute artifacts in a sandbox, capture three sequential screenshots of interaction, and score against task-specific 10-dimension checklists using an MLLM referee (dual-referee: Gemini-2.5-Pro and Qwen2.5-VL-72B) (Zheng et al., 2023; Ge et al., 2023; Zhang et al., 2025). The pipeline measures visual fidelity, interactive correctness, and code quality.

**ZH** • 具备清单引导的“以多模态大语言模型为评审”的多模态自动评测流程。我们在沙箱中执行制品，捕捉交互过程中的三张连续截图，并由多模态大语言模型评审（双评审：Gemini-2.5-Pro 与 Qwen2.5-VL-72B）依据任务专属的十维检查清单打分（Zheng et al., 2023; Ge et al., 2023; Zhang et al., 2025）。该流程度量视觉保真度、交互正确性与代码质量。

**EN** • Strong human alignment and diagnostic insights. We evaluate 30+ LLMs, conduct a 280-instance expert study with pairwise agreement up to 90.95%, and achieve 94.4% ranking consistency with WebDev Arena. The analysis reveals systematic failure modes on intensive-interactive tasks and the insight that instruction-tuned generalist models often outperform specialist ones in this multimodal creative setting.

**ZH** • 强人类一致性与诊断性洞察。我们评测了 30 余个 LLM，开展了包含 280 个实例的专家研究，两两一致率最高达 90.95%，并与 WebDev Arena 取得 94.4% 的排名一致性。分析揭示了模型在强交互任务上的系统性失效模式，并给出了一个洞见：在这一多模态创作场景中，经指令微调的通用模型往往优于专用模型。

<!-- [原子块 · img]  -->

**EN** Figure 1: Distribution of ArtifactsBench

**ZH** 图 1：ArtifactsBench 的分布。

<!-- [原子块 · table] Statistics Number Statistics Number #Problems 1825 Length Primary Topics Question Length ◦ Game 413 - max length 32726 ◦ SVG Generation 123 - min length 184 ◦ Web Application 441 - avg length 524.9 ◦  -->

**EN** Table 1: Dataset statistics of ArtifactsBench.

**ZH** 表 1：ArtifactsBench 的数据集统计。

**EN** 2 ArtifactsBench: A Benchmark for Visual Code Generation

**ZH** 2 ArtifactsBench：面向视觉代码生成的基准

**EN** 2.1 Overview

**ZH** 2.1 概览

**EN** ArtifactsBench comprises 1,825 executable queries covering nine primary topics (Figure 1): “Game Development”, “SVG Generation”, “Web Applications”, “Simulations”, “Data Science”, “Management Systems”, “Multimedia Editing”, “Quick Tools”, and “Others”.

**ZH** ArtifactsBench 由 1,825 条可执行查询组成，覆盖九大主题（图 1）：“游戏开发”“SVG 生成”“Web 应用”“仿真模拟”“数据科学”“管理系统”“多媒体编辑”“快捷工具”与“其他”。

**EN** Tasks are stratified into Easy/Medium/Hard with a target 30%/40%/30% split, assigned post hoc by aggregated performance of 30+ LLMs to preserve discriminative power. Sub-categories enable finer-grained analysis; prompts appear in Appendix 13.

**ZH** 任务被划分为简单/中等/困难三档，目标比例为 30%/40%/30%，该划分由 30 余个 LLM 的聚合表现事后确定，以保留区分度。子类别支持更细粒度的分析；提示词见附录 13。

<!-- [原子块 · table] Benchmark Data Size Data Source Primary Task GR CHA AF VE Humaneval ( Chen et al., 2021 ) 164 Human-Written Algorithmic Tasks Low High ✓ × \times SWE-Bench ( Jimenez et al., 2023 ) 2,294 GitHub Issues -->

**EN** Table 2: Comparison with prior benchmarks. ArtifactsBench is the first to combine high-granularity (GR), strong human consistency (CHA), automation (AF), and direct visual evaluation (VE).

**ZH** 表 2：与已有基准的对比。ArtifactsBench 首次同时实现高细粒度（GR）、强人类一致性（CHA）、自动化（AF）与直接视觉评测（VE）。

**EN** 2.2 Dataset Construction Pipeline

**ZH** 2.2 数据集构建流程

<!-- [原子块 · img]  -->

**EN** Figure 2: An overview of the data construction process of ArtifactsBench.

**ZH** 图 2：ArtifactsBench 数据构建流程概览。

**EN** We aim for ArtifactsBench to be diverse, interactive-first, and rigorously calibrated. Our pipeline (Figure 2) is designed to ensure (i) rich dynamics and real interactivity, (ii) clean and traceable provenance, (iii) strict de-duplication/contamination control, and (iv) reproducibility via standardized execution and checklist-guided judging.

**ZH** 我们希望 ArtifactsBench 具备多样性、交互优先与严格校准三个特性。我们的流程（图 2）旨在确保：（i）丰富的动态性与真实的交互性；（ii）干净可追溯的来源；（iii）严格的去重与污染控制；（iv）通过标准化执行与清单引导的评审实现可复现性。

**EN** Sourcing & filtering. We aggregate candidates from expert showcases, open SVG/web-snippet datasets, web case studies, and LLM visual-to-query from screenshots. Automated filters drop incomplete, non-visual, license-violating, duplicate, trivial, or non-interactive items, prioritizing dynamics (state changes, animations, responsiveness). The curated pool seeds further expansion.

**ZH** 来源采集与过滤。我们从专家示例、开放的 SVG/网页片段数据集、网页案例研究，以及由截图生成查询的 LLM 视觉转查询通道汇集成候选集。自动过滤器剔除不完整、非视觉、违反许可、重复、过于简单或无交互的条目，并优先保留动态性（状态变化、动画、响应式）。经筛选的候选池进一步用于扩充。

**EN** De-duplication & contamination control. Two-stage filtering: (i) MinHash + semantic similarity over prompts, checklists, and normalized DOM/CSS/JS; (ii) screenshot perceptual hashing to catch visually near-identical artifacts. Flagged items are re-authored or discarded.

**ZH** 去重与污染控制。采用两阶段过滤：（i）对提示词、检查清单以及归一化后的 DOM/CSS/JS 做 MinHash 与语义相似度计算；（ii）对截图做感知哈希，以捕捉视觉上近乎相同的制品。被标记的题目会被重新改写或丢弃。

**EN** Prompt rewriting & difficulty calibration. Experts rewrite for clarity/completeness/executability; LLM rewriting adds diverse styles; humans verify. Difficulty is assigned post hoc by aggregated performance of 30+ models to enforce 30%/40%/30%; realized split 559/611/655, stable under leave-family-out resampling. Sub-categories are tagged by a lightweight classifier with human spot-checks (Appendix 13, 14).

**ZH** 提示词改写与难度校准。专家对提示词做改写，以提升清晰性、完整性与可执行性；LLM 改写则增添多样的表述风格；最后由人工核验。难度由 30 余个模型的聚合表现事后确定，强制满足 30%/40%/30% 的比例；实际划分为 559/611/655，在“留一族”重采样下保持稳定。子类别由轻量分类器标注，并进行人工抽检（附录 13、14）。

**EN** Checklist generation & calibration. Each query is paired with a 10-dimension checklist covering visual, interactional, and code qualities. We LLM-draft and then human-refine for specificity and screenability. A 10% manually curated seed anchors calibration and achieves Cohen’s ⟦SLOT_0⟧ among annotators; the seed is reused as few-shot references to keep difficulty high and rubrics consistent. The 10 items are grouped into five vision-oriented and five code-oriented dimensions to support diagnostic analysis (Sec. 3).

**ZH** 检查清单生成与校准。每条查询都配有一份十维检查清单，覆盖视觉、交互与代码三方面的质量。清单先由 LLM 起草，再由人工精修，以确保具体且可筛查。10% 的人工精选种子集用于锚定校准，标注员间的 Cohen's ⟦SLOT_0⟧ 达到要求水平；该种子集被复用为少样本参考，以保持较高难度与评分标准的一致性。这 10 个条目被归为五个视觉导向维度与五个代码导向维度，以支持诊断分析（第 3 节）。

**EN** Solvability validation & ambiguity repair. To ensure tasks are answerable and unambiguous, we collect candidate solutions from multiple families and prune underspecified items. Tasks solved only by brittle hacks (e.g., hard-coded coordinates that break under minor viewport changes) are revised or removed. We prefer prompts that admit multiple acceptable yet checkable implementations.

**ZH** 可解性验证与歧义修复。为确保任务可作答且无歧义，我们从多个模型族收集候选解答，并剪除定义不充分的题目。那些只有靠脆弱技巧才能通过的任务（例如硬编码坐标，在视口发生微小变化时即失效）会被修订或移除。我们更偏好允许多种可接受且可核验实现的提示词。

**EN** Execution harness & screenshot policy. We standardize execution with headless Chromium (Playwright) at ⟦SLOT_1⟧ resolution and deterministic seeds. We capture three staged screenshots (before/during/after scripted interaction) to summarize interaction trajectories so that dynamic feedback and state transitions are evidenced compactly. The same harness is used across models.

**ZH** 执行环境与截图策略。我们以无头 Chromium（Playwright）在 ⟦SLOT_1⟧ 分辨率下配合确定性随机种子来标准化执行。我们捕捉三张分阶段截图（脚本化交互之前/之中/之后）以概括交互轨迹，从而用紧凑的方式为动态反馈与状态转移提供证据。所有模型共用同一套执行环境。

**EN** Statistics & coverage. ArtifactsBench totals 1,825 queries across nine topics (Figure 1; Table 1), with a target Easy/Medium/Hard 30/40/30 split materialized as 559/611/655. Prompts and checklists emphasize executable code and observable interaction; purely static items are retained when visual fidelity or structured graphics are the primary goals (e.g., SVG posters).

**ZH** 统计与覆盖。ArtifactsBench 共含 1,825 条查询，覆盖九个主题（图 1、表 1），简单/中等/困难的目标比例 30/40/30 落实为 559/611/655。提示词与检查清单强调可执行代码与可观测的交互；当视觉保真度或结构化图形本身就是主要目标时（如 SVG 海报），纯静态条目也会被保留。

**EN** 3 Evaluation Methodology

**ZH** 3 评测方法

**EN** To overcome single-metric bias and faithfully capture interaction, we introduce an automated, multi-faceted evaluation framework (Figure 3). The framework targets (i) score consistency, defined as stable, reproducible per-query judgments across runs and referees, and (ii) rank fidelity, defined as agreement of model orderings with human preferences, evaluated over ⟦SLOT_2⟧ queries spanning multiple model families. Concretely, we execute each artifact in a standardized sandbox and capture three staged screenshots that summarize the interaction trajectory. We first validate the automatic referee via a 280-instance, six-model human study, demonstrating high pairwise agreement (targeting ⟦SLOT_3⟧90%). After establishing referee reliability, we evaluate all models at scale and verify that the resulting rankings align strongly with WebDev Arena (Figures 7, 8); full settings, cross-judge analysis (including Gemini-2.5-Pro and Qwen2.5-VL-72B), and ablations appear in the appendix.

**ZH** 为克服单一指标的偏差并忠实捕捉交互过程，我们提出一个自动化的多面评测框架（图 3）。该框架追求两个目标：（i）分数一致性，指同一查询在多次运行与不同评审之间得到稳定、可复现的判断；（ii）排序保真度，指模型排序与人类偏好的一致程度，评测覆盖跨多个模型族的 ⟦SLOT_2⟧ 条查询。具体地，我们在标准化沙箱中执行每个制品，并捕捉三张分阶段截图来概括交互轨迹。我们先通过一项包含 280 个实例、6 个模型的人工研究验证自动评审的可靠性，证明其具有很高的两两一致率（目标 ⟦SLOT_3⟧90%）。在确立评审可信度之后，我们再对所有模型做规模化评测，并验证所得排序与 WebDev Arena 高度吻合（图 7、8）；完整设置、跨评审分析（含 Gemini-2.5-Pro 与 Qwen2.5-VL-72B）以及消融实验见附录。

<!-- [原子块 · img]  -->

**EN** Figure 3: The ArtifactsBench evaluation pipeline. The process hinges on a two-stage evaluation: (Step 5) we first validate our MLLM-as-Judge by confirming its high pairwise scoring agreement with human experts on a controlled set of tasks. (Step 6) Once its reliability is established, the automated judge is deployed at scale to evaluate all model outputs across the entire benchmark. The final rankings are then cross-validated against WebDev Arena to ensure alignment with real-world user preferences for visual quality.

**ZH** 图 3：ArtifactsBench 评测流程。该流程以两阶段评测为核心：（第 5 步）先在一组受控任务上确认“以多模态大语言模型为评审”的方案与人类专家具有很高的两两打分一致率，从而验证其可靠性；（第 6 步）在可靠性确立后，再把自动评审大规模部署到整个基准上，评测所有模型的输出。最终的排名会与 WebDev Arena 交叉验证，以确保其与真实用户在视觉质量上的偏好相一致。

**EN** 3.1 Fine-Grained Checklists

**ZH** 3.1 细粒度检查清单

**EN** We use bespoke checklists covering ten dimensions (e.g., functionality, robustness, engineering practices, redundancy, creativity, aesthetics, user experience). Checklists are generated by Hunyuan-Turbos and human-refined; checklist-generation prompts appear in Appendix Figures 15, 16, and final scoring prompts in Figure 17. Each dimension is scored on 10-point scales with detailed rubrics, penalizing redundancy and rewarding innovation; code-level checks (robustness, scalability, performance) reveal issues beyond visual inspection. For balanced assessment and clearer diagnostics, we group ten items into five vision-oriented and five code-oriented dimensions. Concretely, vision-oriented criteria refer to qualities manifesting in rendered appearance and interaction affordances (layout structure, visual fidelity, motion timing, feedback, UX clarity), while code-oriented criteria evaluate properties visible from code behavior or structure (correctness of logic, robustness to inputs, modularity/engineering hygiene, scalability/performance, and redundancy avoidance).

**ZH** 我们为每条查询定制检查清单，覆盖十个维度（如功能性、鲁棒性、工程实践、冗余、创造性、美观性、用户体验）。清单由 Hunyuan-Turbos 生成并经人工精修；清单生成提示见附录图 15、16，最终打分提示见图 17。每个维度采用 10 分制并配详细评分细则，对冗余予以扣分，对创新予以加分；代码层面的检查（鲁棒性、可扩展性、性能）能揭示肉眼观察无法发现的问题。为实现均衡评估与更清晰的诊断，我们把这十个条目归为五个视觉导向维度与五个代码导向维度。具体地，视觉导向标准指在渲染外观与交互可供性上表现出来的性质（版式结构、视觉保真度、动效时序、反馈、用户体验清晰度），而代码导向标准则评价从代码行为或结构可见的性质（逻辑正确性、对输入的鲁棒性、模块化与工程规范性、可扩展性/性能、以及冗余规避）。

**EN** 3.2 Automated Evaluation and Referees

**ZH** 3.2 自动评测与评审模型

**EN** In contrast to conventional evaluations relying on static code or a single screenshot, our protocol couples interactive evidence with code-aware judging. To make assessment both interactive and reliable, we (i) robustly isolate executable snippets from the model’s raw output; (ii) execute in a sandbox and capture three staged screenshots (before/during/after interaction) that summarize the interaction trajectory; and (iii) provide temporal evidence, the original task, the model’s full answer, and a fine-grained checklist to the referee model to produce holistic, reproducible scores. The referee aligns visual evidence with task intent and, informed by answer content, audits properties that screenshots alone cannot reveal (e.g., logic correctness, robustness to inputs, modularity/engineering hygiene, and redundancy). This yields consistent judgments across vision- and code-oriented dimensions.

**ZH** 与依赖静态代码或单张截图的常规评测不同，我们的方案把交互证据与代码感知的判断结合起来。为使评测兼具交互性与可靠性，我们：（i）从模型原始输出中稳健地隔离出可执行代码片段；（ii）在沙箱中执行，并捕捉三张分阶段截图（交互前/中/后）以概括交互轨迹；（iii）把时序证据、原始任务、模型的完整回答以及细粒度检查清单一并交给评审模型，以产生整体、可复现的分数。评审模型把视觉证据与任务意图对齐，并借助回答内容审查单靠截图无法揭示的性质（如逻辑正确性、对输入的鲁棒性、模块化与工程规范性、冗余情况）。如此可在视觉导向与代码导向两类维度上得到一致的判断。

**EN** To enhance reproducibility and robustness, we adopt a dual-referee setup: the open-source Qwen2.5-VL-72B and the proprietary Gemini-2.5-Pro. The two referees induce highly consistent partial-order constraints over model rankings, and replacing the deprecated Gemini-2.5-Pro-Preview-0506 preview with the stable Gemini-2.5-Pro leaves our conclusions unchanged. Full settings, cross-judge comparisons, and leaderboards appear in Sec. 4 and the appendix.

**ZH** 为提升可复现性与鲁棒性，我们采用双评审设置：开源的 Qwen2.5-VL-72B 与闭源的 Gemini-2.5-Pro。两名评审在模型排名上导出的偏序约束高度一致；把已弃用的 Gemini-2.5-Pro-Preview-0506 预览版替换为稳定的 Gemini-2.5-Pro 后，我们的结论保持不变。完整设置、跨评审对比与排行榜见第 4 节与附录。

**EN** 4 Experiments

**ZH** 4 实验

**EN** 4.1 Settings

**ZH** 4.1 设置

**EN** We conduct all evaluations in a sandboxed environment with deterministic seeds and fixed rendering settings. Execution uses Playwright (headless Chromium) to render artifacts at a resolution of ⟦SLOT_4⟧, capturing three staged screenshots (before, during, and after interaction). Each model is prompted with identical instructions; we apply consistent decoding parameters (temperature and top-p tuned per official recommendations; max tokens sufficient to prevent truncation) and enforce a uniform per-query time budget. Baselines are selected to span (i) multiple families (Qwen2.5/3 (Yang et al., 2024; Yang et al., 2025), DeepSeek (Guo et al., 2025; Liu et al., 2024a), Gemma/GPT/Claude/Gemini (Team et al., 2025; OpenAI, 2023; Anthropic, 2025; Gemini Team & Google, 2023), Seed (Seed et al., 2025), Hunyuan (Liu et al., 2025)), (ii) a range of sizes (from small to flagship), and (iii) modality/training styles (instruction-tuned generalists, coder-specialized, and VL-capable models), ensuring breadth, recency, and reproducibility.

**ZH** 全部评测都在带有确定性随机种子与固定渲染设置的沙箱环境中进行。执行环节使用 Playwright（无头 Chromium）以 ⟦SLOT_4⟧ 分辨率渲染制品，并捕捉三张分阶段截图（交互前、交互中、交互后）。各模型使用完全相同的指令；我们采用一致的解码参数（temperature 与 top-p 按官方建议调整；max tokens 足够长以避免截断），并对每条查询施行统一的时间预算。基线模型的选择覆盖三个维度：（i）多个模型族（Qwen2.5/3（Yang et al., 2024; Yang et al., 2025）、DeepSeek（Guo et al., 2025; Liu et al., 2024a）、Gemma/GPT/Claude/Gemini（Team et al., 2025; OpenAI, 2023; Anthropic, 2025; Gemini Team & Google, 2023）、Seed（Seed et al., 2025）、Hunyuan（Liu et al., 2025））；（ii）从小型到旗舰的多种规模；（iii）不同的模态与训练风格（指令微调的通用模型、代码专用模型与具备视觉语言能力的模型），以保证覆盖面、时效性与可复现性。

**EN** Building on Sec. 3, we evaluate over 30 models using our automated pipeline and dual-referee protocol, analyzing performance across interactivity levels and task categories.

**ZH** 在第 3 节的基础上，我们用自动评测流程与双评审方案评测了 30 余个模型，并分析其在不同交互强度与任务类别上的表现。

<!-- [原子块 · table] MODEL IFLEN SCORE SV MMD HD II GAME SVG WEB SI MS AVG Open-Source Large Language Models Qwen2.5-7B-Instruct 7905.21 29.60 26.92 29.68 24.65 24.26 23.22 29.99 23.86 28.31 27.35 Qwen2.5-14B-Instruct 633 -->

**EN** Table 3: Main results for 30+ LLMs on ArtifactsBench, scored by Gemini-2.5-Pro-Preview-0506 referee. Performance detailed across interactivity levels (SV: Static Visual, MMD: Mild-to-Moderate Dynamics, HD: High Dynamics, II: Intensive Interactive) and task categories (GAME, SVG, WEB, SI: Simulation, MS: Management System). AVG is global average. IFLEN represents answer length. Since reasoning chain length cannot be obtained for some closed-source models, it is left empty. Top proprietary models show a significant lead, and performance scales with model size.

**ZH** 表 3：30 余个 LLM 在 ArtifactsBench 上的主要结果，由 Gemini-2.5-Pro-Preview-0506 担任评审。性能按交互强度（SV：静态视觉；MMD：轻中度动态；HD：高动态；II：强交互）与任务类别（GAME、SVG、WEB、SI：仿真；MS：管理系统）细分。AVG 为全局平均分，IFLEN 表示回答长度。由于部分闭源模型无法获取推理链长度，该项留空。头部闭源模型优势显著，且性能随模型规模提升。

**EN** 4.2 Main Results and Analysis

**ZH** 4.2 主要结果与分析

**EN** Proprietary multimodal models (e.g., Gemini-2.5-Pro, Claude 4.0-Sonnet) lead; scores scale with model size and deliberation across families. The largest deficits occur on Intensive Interactive tasks and complex Management System scenarios, while instruction-tuned generalists consistently outperform specialist coder/VL models. Table 3 and Appendix Figure 9 summarize all baselines scored by our MLLM referee. We report (1) interaction-level metrics across interactivity classes and (2) category metrics across task types, aggregated into one overall score.

**ZH** 闭源多模态模型（如 Gemini-2.5-Pro、Claude 4.0-Sonnet）领先；在各模型族内部，分数随模型规模与思考时长提升。最大的短板出现在强交互任务与复杂的管理系统场景，而经指令微调的通用模型持续优于代码专用或视觉专用模型。表 3 与附录图 9 汇总了由我们的多模态大语言模型评审打分的全部基线。我们报告两类指标：（1）跨交互强度类别的交互层级指标；（2）跨任务类型的类别指标，二者聚合为一个总分。

**EN** Proprietary multimodal models show clear advantage.

**ZH** 闭源多模态模型优势明显。

**EN** As shown in Table 3, Gemini-2.5-Pro achieves the highest overall score across both open- and closed-source evaluations. Claude 4.0-Sonnet likewise approaches state-of-the-art performance, underscoring the substantial lead that top-tier proprietary multimodal systems currently maintain in this challenging domain.

**ZH** 如表 3 所示，Gemini-2.5-Pro 在开源与闭源两类评测中均取得最高总分。Claude 4.0-Sonnet 同样逼近最先进水平，凸显了顶级闭源多模态系统当前在这一高难度领域所保持的显著领先。

**EN** Performance scales with model size and deliberation time.

**ZH** 性能随模型规模与思考时长提升。

**EN** Within the Qwen2.5 and Qwen3 families, performance on ArtifactsBench rises with model capacity. Models with longer inference (sometimes termed “slow thinkers”) also score higher, indicating that intricate planning benefits from deeper computation.

**ZH** 在 Qwen2.5 与 Qwen3 系列内部，模型在 ArtifactsBench 上的表现随容量上升。推理时间更长的模型（有时被称为“慢思考”模型）得分也更高，说明复杂的规划受益于更深的计算。

**EN** Analysis of open-source model performance.

**ZH** 开源模型表现分析。

**EN** Among open-source contenders, DeepSeek-R1-0528 sets a new benchmark, indicating that strong code generation and general reasoning aid code-centric visualization. Distillation on limited data yields modest gains: DeepSeek-distill-qwen-32B improves only 3 points over Qwen-2.5-32B yet remains 5 points below Qwen3-32B, consistent with dynamic distillation findings (Liu et al., 2024b).

**ZH** 在开源竞争者中，DeepSeek-R1-0528 树立了新的标杆，说明强劲的代码生成能力与通用推理能力有助于代码中心的视觉化任务。在有限数据上做蒸馏带来的增益有限：DeepSeek-distill-qwen-32B 仅比 Qwen-2.5-32B 高出 3 分，却仍比 Qwen3-32B 低 5 分，这与动态蒸馏的已有发现相符（Liu et al., 2024b）。

**EN** Opportunities remain in challenging scenarios.

**ZH** 高难度场景仍有提升空间。

**EN** All models score lowest on Intensive Interactive tasks and complex, project-level visualization (e.g., Management System), pointing to clear avenues for improvement.

**ZH** 所有模型在强交互任务与复杂的项目级可视化（如管理系统）上得分最低，指明了明确的改进方向。

**EN** Generalist skills outperform specialist expertise.

**ZH** 通用能力胜过专用专长。

**EN** Instruction-tuned generalist models outperform domain-specific counterparts: Qwen-2.5-Instruct surpasses both Qwen-2.5-coder and Qwen2.5-VL-72B. Producing high-quality visual artifacts requires a synthesis of reasoning, instruction following, and design sense beyond isolated code generation or visual understanding.

**ZH** 经指令微调的通用模型优于领域专用模型：Qwen-2.5-Instruct 同时超过 Qwen-2.5-coder 与 Qwen2.5-VL-72B。产出高质量视觉制品需要推理、指令遵循与设计感知力的综合，而非孤立的代码生成或视觉理解能力。

**EN** 4.3 Fine-grained Analysis

**ZH** 4.3 细粒度分析

**EN** Vision–Code correlation and difficulty stratification. We categorize the 10 checklist items into five vision-oriented and five code-oriented criteria. Figure 4 shows a strong positive correlation between vision and code scores, indicating capability improvements are holistic rather than siloed. We further split the benchmark into three tiers; as shown in Figure 5, even the best models struggle on the hardest subset, while relative rankings remain stable across tiers, demonstrating strong discriminative power.

**ZH** 视觉—代码相关性与难度分层。我们把 10 个检查清单条目划分为五个视觉导向标准与五个代码导向标准。图 4 显示视觉分数与代码分数之间存在强正相关，说明能力提升是整体性的，而非局限于某一方面。我们进一步把基准划分为三个层级；如图 5 所示，即便是最强的模型在最难子集上也表现吃力，而各层级间的相对排名保持稳定，体现出很强的区分度。

<!-- [原子块 · img]  -->

**EN** Figure 4: Correlation between vision- and code-oriented scores on ArtifactsBench. The strong positive trend indicates holistic capability and motivates assessing both dimensions.

**ZH** 图 4：ArtifactsBench 上视觉导向分数与代码导向分数的相关性。强正相关说明能力是整体性的，也说明有必要同时评估这两个维度。

<!-- [原子块 · img]  -->

**EN** Figure 5: Scores across difficulty tiers on ArtifactsBench.

**ZH** 图 5：ArtifactsBench 各难度层级上的分数。

<!-- [原子块 · img]  -->

**EN** Figure 6: Relationship between model performance and response length on ArtifactsBench (Gemini-2.5-Pro as referee). The trend is broadly positive, but concise, well-structured outputs can remain competitive.

**ZH** 图 6：ArtifactsBench 上模型性能与回答长度的关系（以 Gemini-2.5-Pro 为评审）。整体呈正相关，但简洁、结构良好的输出仍可保持竞争力。

**EN** Human validation and ablations. We run a double-blind study on 280 queries and 6 models, judged by multiple front-end engineers. Agreement is measured by Pair ACC. Incorporating execution screenshots markedly improves agreement, and multiple screenshots better capture dynamics (Table 4). Replacing images with captions helps but remains inferior when visual capability is strong; removing the answer degrades quality, confirming the need for code-aware judging (Table 5).

**ZH** 人工验证与消融实验。我们在 280 条查询、6 个模型上开展双盲研究，由多名前端工程师评判。一致程度用 Pair ACC 度量。引入执行截图显著提升了与人类的一致率，多张截图能更好地捕捉动态变化（表 4）。用文字描述替代图像有所助益，但在视觉能力较强时仍不及直接看图；去掉回答则使质量下降，证实了代码感知评审的必要性（表 5）。

**EN** Table 4: Ablation study on multimodal referees with and without images.

**ZH** 表 4：关于有无图像的多模态评审消融实验。

<!-- [原子块 · table] Referee Models w/o img Pair ACC Referee Models w/ img Pair ACC Referee Models w/ imgs Pair ACC Qwen2.5-VL-72B 61.80% Qwen2.5-VL-72B 68.08% Qwen2.5-VL-72B 71.34% GPT-o4-mini 72.41% GPT-o4-mini 76.25% G -->

**EN** Table 5: Ablation study on visual description vs. images and the role of answers.

**ZH** 表 5：关于视觉描述与图像、以及回答作用的消融实验。

<!-- [原子块 · table] Referee Models w/o img Pair ACC Referee Models w/ imgs Pair ACC Qwen3-32B-Instruct 64.12 Qwen3-32B-Instruct w/ caption 68.78 Qwen2.5-VL-72B 61.80 Qwen2.5-VL-72B w/ caption 66.14 Gemini-2.5-pro 79.06 G -->

**EN** In addition, Figure 6 illustrates the relationship between model performance and response length. While longer responses broadly correlate with higher scores (suggesting deeper planning helps), notable efficient models remain competitive with concise outputs—indicating quality over verbosity and the value of compact, well-structured solutions.

**ZH** 此外，图 6 展示了模型性能与回答长度之间的关系。虽然更长的回答大体对应更高的分数（说明更深的规划有帮助），但仍有若干高效模型凭借简洁的输出保持竞争力——这表明质量比篇幅更重要，紧凑且结构良好的解法同样有价值。

**EN** Cross-judge robustness and version stability. We adopt two SOTA referees with complementary strengths: the open-source Qwen2.5-VL-72B (transparent and reproducible) and the proprietary Gemini-2.5-Pro (higher-capacity reference). They induce highly consistent partial-order constraints over model rankings; residual differences concentrate among top systems, where the stronger referee offers finer resolution. Moreover, replacing the deprecated preview Gemini-2.5-Pro-0506 with the stable Gemini-2.5-Pro yields identical ordering constraints, confirming version stability (see Appendix Figure 11 and Appendix Figure 10).

**ZH** 跨评审鲁棒性与版本稳定性。我们采用两个优势互补的最先进评审：开源的 Qwen2.5-VL-72B（透明可复现）与闭源的 Gemini-2.5-Pro（容量更高的参照）。二者在模型排名上导出的偏序约束高度一致；残余差异集中在头部系统，其中更强的评审具有更细的分辨力。此外，把已弃用的预览版 Gemini-2.5-Pro-0506 替换为稳定的 Gemini-2.5-Pro 后，得到的排序约束完全相同，证实了版本稳定性（见附录图 11 与附录图 10）。

**EN** 4.4 Alignment with WebDev Arena

**ZH** 4.4 与 WebDev Arena 的一致性

<!-- [原子块 · img]  -->

**EN** Figure 7: Ranking correlation between ArtifactsBench (judged by Gemini-2.5-pro) and the human-preference-based WebDev Arena. The strong alignment validates that our automated evaluation framework captures qualities that correlate with real-world user perceptions of performance.

**ZH** 图 7：ArtifactsBench（由 Gemini-2.5-pro 评审）与基于人类偏好的 WebDev Arena 之间的排名相关性。二者的高度吻合验证了我们的自动评测框架所捕捉的性质，与真实用户对性能的感知相关。

<!-- [原子块 · img]  -->

**EN** Figure 8: Ranking correlation between WebBench and WebDev Arena. The weaker alignment, compared to ArtifactsBench (Figure 7), suggests that prior static benchmarks may not fully capture the interactive and dynamic qualities prioritized by human users.

**ZH** 图 8：WebBench 与 WebDev Arena 的排名相关性。相比 ArtifactsBench（图 7），其吻合度更弱，说明此前的静态基准可能未能充分捕捉人类用户所看重的交互与动态特性。

**EN** WebDev Arena (Zhou et al., 2023)—a de-facto human-preference gold standard—validates alignment. ArtifactsBench attains 94.4% normalized Footrule consistency11 1 Based on the ⟦SLOT_5⟧ distance between rank vectors; closer to 1 is better. versus 69.4% for WebBench (Figures 7, 8), indicating stronger reflection of human priorities at scale. Beyond agreement, ArtifactsBench yields actionable diagnostics: for instance, o3-mini ranks slightly higher than human voting because it excels on static code-centric qualities (extensibility, robustness, runtime performance), surfacing strengths that human preference may underweight. We additionally include full leaderboards with both Gemini-2.5-Pro and Qwen2.5-VL-72B referees in the appendix for completeness, while key findings are reported here without deferral.

**ZH** WebDev Arena（Zhou et al., 2023）作为事实上的黄金标准，用于验证一致性。ArtifactsBench 取得 94.4% 的归一化 Footrule 一致性（基于排序向量之间的 ⟦SLOT_5⟧ 距离；越接近 1 越好），而 WebBench 为 69.4%（图 7、8），说明前者在规模化场景下更能反映人类的优先关切。除一致性之外，ArtifactsBench 还能给出可操作的诊断：例如 o3-mini 的排名略高于人类投票，因为它在静态代码导向的性质（可扩展性、鲁棒性、运行时性能）上表现突出，揭示了人类偏好可能低估的优势。我们还把以 Gemini-2.5-Pro 与 Qwen2.5-VL-72B 为评审的完整排行榜一并列入附录，而关键发现均在此给出，不作延后。

**EN** 5 Related Work

**ZH** 5 相关工作

**EN** Benchmarks for Visual Code Generation. Foundational benchmarks (HumanEval (Chen et al., 2021), SWE-Bench (Jimenez et al., 2023)) assess algorithms/repositories but not visual fidelity, dynamics, and interaction. Visual-code efforts such as pix2code (Wüst et al., 2024) and Web2Code (Yun et al., 2024) target screenshot-to-code; WebBench (Xu et al., 2025) targets DOM alignment; FullFront (Sun et al., 2025) evaluates the development process; WebDev Arena (LMSYS Org, 2024) captures human preference. ArtifactsBench complements these by evaluating live, operable artifacts with complex dynamics via a checklist-driven protocol that yields interpretable diagnostics beyond a single score. It also covers structured graphics (StarVector (Rodriguez et al., 2023), LLM4SVG (Xing et al., 2025)) and dynamic scenes: instead of navigating existing environments (Open CaptchaWorld (Luo et al., 2025)), we assess generating such dynamics via snapshot-based checks (e.g., physics-based mini-games). Our snapshot-based check is designed to verify that required state transitions and interactive feedback truly occur, and to provide compact, reviewable evidence that enables consistent judging across models and tasks.

**ZH** 视觉代码生成基准。基础性基准（HumanEval（Chen et al., 2021）、SWE-Bench（Jimenez et al., 2023））评估的是算法与代码仓库，不涉及视觉保真度、动态性与交互。视觉代码方向的工作，如 pix2code（Wüst et al., 2024）与 Web2Code（Yun et al., 2024）面向截图转代码；WebBench（Xu et al., 2025）面向 DOM 对齐；FullFront（Sun et al., 2025）评估开发流程；WebDev Arena（LMSYS Org, 2024）捕捉人类偏好。ArtifactsBench 与之互补：通过清单驱动的协议评测具有复杂动态的、可实际操作的制品，并提供超越单一分数的可解释诊断。它还覆盖结构化图形（StarVector（Rodriguez et al., 2023）、LLM4SVG（Xing et al., 2025））与动态场景：不同于在既有环境中导航（Open CaptchaWorld（Luo et al., 2025）），我们评估的是通过基于快照的检查生成此类动态效果的能力（如基于物理的小游戏）。我们基于快照的检查旨在验证所需的状态转移与交互反馈确实发生，并提供紧凑、可复核的证据，使不同模型与任务之间的判断保持一致。

**EN** Evaluation Paradigms for Interactive Visual Artifacts. DOM/pixel similarity misses high-level semantics and interaction flow. Multimodal LLMs (Gemini Team & Google, 2023; OpenAI, 2023) enable code-aware visual judging within a structured protocol. While these models have shown promising results in perception and QA, they can suffer from hallucination, prompt sensitivity, limited awareness of engineering/code quality, and version drift (Zheng et al., 2023; Ge et al., 2023). Accordingly, ArtifactsBench adds structured safeguards—temporal snapshot evidence coupled with fine-grained, task-tailored checklists and a dual-referee protocol (Gemini-2.5-Pro and Qwen2.5-VL-72B)—to improve reliability and interpretability, while keeping this section focused on prior art.

**ZH** 交互式视觉制品的评测范式。DOM 或像素相似度无法捕捉高层语义与交互流程。多模态大语言模型（Gemini Team & Google, 2023; OpenAI, 2023）使得在结构化协议内做代码感知的视觉评判成为可能。尽管这些模型在感知与问答上表现不俗，却可能受到幻觉、提示敏感、工程与代码质量意识有限以及版本漂移的困扰（Zheng et al., 2023; Ge et al., 2023）。因此，ArtifactsBench 增加了结构化的保障措施——把时序快照证据与细粒度、任务定制的检查清单以及双评审方案（Gemini-2.5-Pro 与 Qwen2.5-VL-72B）结合起来，以提升可靠性与可解释性；本节则聚焦于已有工作本身。

**EN** 6 Conclusion

**ZH** 6 结论

**EN** We present ArtifactsBench, an automated benchmark for evaluating LLMs on dynamic visual artifacts, addressing static/non-visual gaps. Contributions: (i) a diverse, difficulty-calibrated set of 1,825 tasks; (ii) an automated, checklist-guided MLLM referee scoring code, visuals, and interaction. Across 30+ LLMs, scores align strongly with expert judgments and Web-Dev Arena, offering diagnostics on strengths/failure modes and advancing artifact generation.

**ZH** 我们提出 ArtifactsBench，一个用于评测 LLM 生成动态视觉制品的自动化基准，弥补了静态与非视觉评测的缺口。贡献包括：（i）一套多样且经过难度校准的 1,825 个任务；（ii）一个自动化的、由检查清单引导的多模态大语言模型评审，对代码、视觉与交互同时打分。在 30 余个 LLM 上，评分与专家判断及 WebDev Arena 高度吻合，并给出关于优势与失效模式的诊断，推动制品生成的发展。

**EN** 7 Contributions and Acknowledgements

**ZH** 7 贡献与致谢

**EN** Our team members contribute to the development of ArtifactsBench from the following perspectives:

**ZH** 团队成员从以下方面参与 ArtifactsBench 的建设：

**EN** First Autors

**ZH** 第一作者

<!-- [原子块 · table] ∙ \bullet Chenchen Zhang, Tencent ∙ \bullet Yuhang Li, Tencent -->

**EN** Core Contributors — Algorithm Support

**ZH** 核心贡献者——算法支持

<!-- [原子块 · table] ∙ \bullet Can Xu, Tencent ∙ \bullet Jiaheng Liu, NJU ∙ \bullet Ao Liu, Tencent ∙ \bullet Changzhi Zhou, Tencent ∙ \bullet Ken Deng, Independent ∙ \bullet Dengpeng Wu, Tencent ∙ \bullet Guanhua Huang,  -->

**EN** Corresponding Authors

**ZH** 通讯作者

<!-- [原子块 · table] ∙ \bullet Wiggin Zhou, Tencent ∙ \bullet Chayse Zhou, Tencent ∙ \bullet Fengzong Lian, Tencent wigginzhou,chaysezhou,faxonlian@tencent.com -->

**EN** Acknowledgements — Data and Front-End Technical Support (Alphabet Order)

**ZH** 致谢——数据与前端技术支持（按字母顺序）

<!-- [原子块 · table] ∙ \bullet Bohui Zhai, Tencent ∙ \bullet Guoxiang He, Tencent ∙ \bullet Haotian Zhu, Tencent ∙ \bullet Hebin Li, Tencent ∙ \bullet Jie Zhao, Tencent ∙ \bullet Le Zhang, Tencent ∙ \bullet Lingyun Tan, T -->

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] Anthropic (2025) Anthropic. System Card: Claude Opus 4 & Claude Sonnet 4. https://www-cdn.anthropic.com/6be99a52cb68eb70eb9572b4cafad13df32ed995.pdf , May 2025. Accessed: 2024-05-22. -->

<!-- [原子块 · verbatim] Chen et al. (2021) Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde De Oliveira Pinto, Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman, et al. Evaluating large  -->

<!-- [原子块 · verbatim] Ge et al. (2023) Wentao Ge, Shunian Chen, Guiming Hardy Chen, Junying Chen, Zhihong Chen, Nuo Chen, Wenya Xie, Shuo Yan, Chenghao Zhu, Ziyue Lin, et al. Mllm-bench: evaluating multimodal llms with per -->

<!-- [原子块 · verbatim] Gemini Team & Google (2023) Gemini Team and Google. Gemini: A family of highly capable multimodal models, 2023. -->

<!-- [原子块 · verbatim] Guo et al. (2025) Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al. Deepseek-r1: Incentivizing reasoning capability in llms  -->

<!-- [原子块 · verbatim] Jaech et al. (2024) Aaron Jaech, Adam Kalai, Adam Lerer, Adam Richardson, Ahmed El-Kishky, Aiden Low, Alec Helyar, Aleksander Madry, Alex Beutel, Alex Carney, et al. Openai o1 system card. arXiv prepr -->

<!-- [原子块 · verbatim] Jiang et al. (2024) Juyong Jiang, Fan Wang, Jiasi Shen, Sungju Kim, and Sunghun Kim. A survey on large language models for code generation. arXiv preprint arXiv:2406.00515 , 2024. -->

<!-- [原子块 · verbatim] Jimenez et al. (2023) Carlos E Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik Narasimhan. Swe-bench: Can language models resolve real-world github issues? arXiv p -->

<!-- [原子块 · verbatim] Liu et al. (2024a) Aixin Liu, Bei Feng, Bing Xue, Bingxuan Wang, Bochao Wu, Chengda Lu, Chenggang Zhao, Chengqi Deng, Chenyu Zhang, Chong Ruan, et al. Deepseek-v3 technical report. arXiv preprint arXi -->

<!-- [原子块 · verbatim] Liu et al. (2025) Ao Liu, Botong Zhou, Can Xu, Chayse Zhou, ChenChen Zhang, Chengcheng Xu, Chenhao Wang, Decheng Wu, Dengpeng Wu, Dian Jiao, et al. Hunyuan-turbos: Advancing large language models thro -->

<!-- [原子块 · verbatim] Liu et al. (2024b) Jiaheng Liu, Chenchen Zhang, Jinyang Guo, Yuanxing Zhang, Haoran Que, Ken Deng, Jie Liu, Ge Zhang, Yanan Wu, Congnan Liu, et al. Ddk: Distilling domain knowledge for efficient large -->

<!-- [原子块 · verbatim] LMSYS Org (2024) LMSYS Org. Chatbot Arena Leaderboard. https://web.lmarena.ai/leaderboard , 2024. Accessed: 2024-05-23. -->

<!-- [原子块 · verbatim] Lu et al. (2025a) Fanbin Lu, Zhisheng Zhong, Shu Liu, Chi-Wing Fu, and Jiaya Jia. Arpo: End-to-end policy optimization for gui agents with experience replay. arXiv preprint arXiv:2505.16282 , 2025a. -->

<!-- [原子块 · verbatim] Lu et al. (2025b) Zimu Lu, Yunqiao Yang, Houxing Ren, Haotian Hou, Han Xiao, Ke Wang, Weikang Shi, Aojun Zhou, Mingjie Zhan, and Hongsheng Li. Webgen-bench: Evaluating llms on generating interactive a -->

<!-- [原子块 · verbatim] Luo et al. (2025) Yaxin Luo, Zhaoyi Li, Jiacheng Liu, Jiacheng Cui, Xiaohan Zhao, and Zhiqiang Shen. Open captchaworld: A comprehensive web-based platform for testing and benchmarking multimodal llm a -->

<!-- [原子块 · verbatim] Miyai et al. (2025) Atsuyuki Miyai, Zaiying Zhao, Kazuki Egashira, Atsuki Sato, Tatsumi Sunada, Shota Onohara, Hiromasa Yamanishi, Mashiro Toyooka, Kunato Nishina, Ryoma Maeda, et al. Webchorearena: E -->

<!-- [原子块 · verbatim] OpenAI (2023) OpenAI. Gpt-4v(ision) system card. https://cdn.openai.com/papers/GPTV_System_Card.pdf , 2023. -->

<!-- [原子块 · verbatim] Rodriguez et al. (2023) Juan A Rodriguez, Shubham Agarwal, Issam H Laradji, Pau Rodriguez, David Vazquez, Christopher Pal, and Marco Pedersoli. Starvector: Generating scalable vector graphics code fro -->

<!-- [原子块 · verbatim] Seed et al. (2025) ByteDance Seed, Yufeng Yuan, Yu Yue, Mingxuan Wang, Xiaochen Zuo, Jiaze Chen, Lin Yan, Wenyuan Xu, Chi Zhang, Xin Liu, et al. Seed-thinking-v1. 5: Advancing superb reasoning models  -->

<!-- [原子块 · verbatim] Sun et al. (2025) Haoyu Sun, Huichen Will Wang, Jiawei Gu, Linjie Li, and Yu Cheng. Fullfront: Benchmarking mllms across the full front-end engineering workflow. arXiv preprint arXiv:2505.17399 , 2025 -->

<!-- [原子块 · verbatim] Team et al. (2025) Gemma Team, Aishwarya Kamath, Johan Ferret, Shreya Pathak, Nino Vieillard, Ramona Merhej, Sarah Perrin, Tatiana Matejovicova, Alexandre Ramé, Morgane Rivière, et al. Gemma 3 technic -->

<!-- [原子块 · verbatim] Wu et al. (2024) Chengyue Wu, Yixiao Ge, Qiushan Guo, Jiahao Wang, Zhixuan Liang, Zeyu Lu, Ying Shan, and Ping Luo. Plot2code: A comprehensive benchmark for evaluating multi-modal large language model -->

<!-- [原子块 · verbatim] Wüst et al. (2024) Antonia Wüst, Wolfgang Stammer, Quentin Delfosse, Devendra Singh Dhami, and Kristian Kersting. Pix2code: Learning to compose neural visual concepts as programs. arXiv preprint arXiv -->

<!-- [原子块 · verbatim] Xing et al. (2025) Ximing Xing, Juncheng Hu, Guotao Liang, Jing Zhang, Dong Xu, and Qian Yu. Empowering llms to understand and generate complex vector graphics. In Proceedings of the Computer Vision a -->

<!-- [原子块 · verbatim] Xu et al. (2025) Kai Xu, YiWei Mao, XinYi Guan, and ZiLong Feng. Web-bench: A llm code benchmark based on web standards and frameworks. arXiv preprint arXiv:2505.07473 , 2025. -->

<!-- [原子块 · verbatim] Yang et al. (2024) An Yang, Baosong Yang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Zhou, Chengpeng Li, Chengyuan Li, Dayiheng Liu, Fei Huang, et al. Qwen2 technical report. arXiv preprint arXiv:2407.106 -->

<!-- [原子块 · verbatim] Yang et al. (2025) An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao, Chengen Huang, Chenxu Lv, et al. Qwen3 technical report. arXiv preprint arXiv:2505.09388 -->

<!-- [原子块 · verbatim] Yun et al. (2024) Sukmin Yun, Haokun Lin, Rusiru Thushara, Mohammad Qazim Bhat, Yongxin Wang, Zutao Jiang, Mingkai Deng, Jinhong Wang, Tianhua Tao, Junbo Li, et al. Web2code: A large-scale webpage-to- -->

<!-- [原子块 · verbatim] Zhang et al. (2025) Alexander Zhang, Marcus Dong, Jiaheng Liu, Wei Zhang, Yejie Wang, Jian Yang, Ge Zhang, Tianyu Liu, Zhongyuan Peng, Yingshui Tan, et al. Codecriticbench: A holistic code critique be -->

<!-- [原子块 · verbatim] Zheng et al. (2023) Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric Xing, et al. Judging llm-as-a-judge with mt-bench and ch -->

<!-- [原子块 · verbatim] Zhou et al. (2023) Shuyan Zhou, Frank F Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Tianyue Ou, Yonatan Bisk, Daniel Fried, et al. Webarena: A realistic web environment for buil -->

**EN** Appendix A Appendix

**ZH** 附录 A 附录

**EN** A.1 Limitations and Future Work

**ZH** A.1 局限性与未来工作

**EN** While ArtifactsBench represents a significant step forward in the automated evaluation of LLM-generated visual code, we recognize its limitations, which in turn open up exciting avenues for future research.

**ZH** 尽管 ArtifactsBench 在 LLM 生成视觉代码的自动评测上迈出了重要一步，我们也认识到其局限，而这些局限正为未来研究打开了令人期待的方向。

**EN** Deepening the Evaluation of Interactivity.

**ZH** 深化交互性评测。

**EN** Our current methodology evaluates dynamic behavior by capturing and analyzing a sequence of screenshots at fixed intervals. This approach effectively assesses many forms of interactivity. However, for highly complex, long-horizon, or state-dependent interactions (e.g., multi-step user workflows in a web application, or the nuanced physics in a game), this discrete sampling may not fully capture the fluidity, correctness, and robustness of the entire interactive experience. Future work could explore more sophisticated dynamic analysis techniques, such as programmatically interacting with the Document Object Model (DOM) to verify state transitions or employing video-based analysis to evaluate the entire user session, thereby enabling a more profound understanding of complex interaction logic.

**ZH** 我们当前的方法通过以固定间隔捕捉并分析一组截图来评估动态行为。这一做法能有效评估多种形式的交互性。然而，对于高度复杂、长时程或依赖状态的交互（例如 Web 应用中的多步用户工作流，或游戏中精细的物理效果），这种离散采样可能无法完整捕捉整个交互体验的流畅性、正确性与鲁棒性。未来工作可探索更精细的动态分析技术，例如以程序化方式与文档对象模型（DOM）交互以验证状态转移，或采用基于视频的分析来评估完整的用户会话，从而更深入地理解复杂的交互逻辑。

**EN** Exploring Agentic and Iterative Development.

**ZH** 探索智能体式与迭代式开发。

**EN** ArtifactsBench currently focuses on evaluating the quality of the final artifact generated in a single turn from a given prompt. This scope does not assess an LLM’s capability to function as an autonomous agent that can iteratively refine an artifact based on feedback, debug its own code in response to errors, or plan and execute a multi-step development process. These agentic capabilities are crucial for tackling real-world software engineering challenges. A promising direction for future research is to extend ArtifactsBench into an agentic evaluation framework. In such a setup, the model would need to engage in a multi-turn dialogue with a simulated environment (e.g., a user, a linter, or a debugger) to incrementally build, test, and enhance the visual artifact. This would provide a more realistic testbed for evaluating the end-to-end problem-solving abilities required for truly intelligent and collaborative code generation.

**ZH** ArtifactsBench 目前聚焦于评测模型在单轮内依据给定提示所生成的最终制品的质量。这一范围并未考察 LLM 作为自主智能体的能力——即依据反馈迭代改进制品、针对错误调试自身代码，或规划并执行多步开发流程的能力。这些智能体能力对应对真实软件工程挑战至关重要。一个有前景的未来方向是把 ArtifactsBench 扩展为智能体式评测框架：在这一设置中，模型需要与模拟环境（如用户、代码检查工具或调试器）进行多轮对话，以增量地构建、测试并完善视觉制品。这将为评估真正智能且可协作的代码生成所需的端到端问题解决能力提供更加真实的试验场。

**EN** A.2 Detailed Analysis of the Results

**ZH** A.2 结果的详细分析

**EN** Proprietary multimodal models demonstrate a clear advantage.

**ZH** 闭源多模态模型优势明显。

**EN** As shown in Table 3, Gemini-2.5-Pro achieves the highest overall score across both our open-source and proprietary human evaluations. Claude 4.0-Sonnet likewise approaches state-of-the-art performance, underscoring the substantial lead that top-tier proprietary multimodal systems currently maintain in this challenging domain.

**ZH** 如表 3 所示，Gemini-2.5-Pro 在我们的开源与闭源人工评测中均取得最高总分。Claude 4.0-Sonnet 同样逼近最先进水平，凸显了顶级闭源多模态系统当前在这一高难度领域所保持的显著领先。

**EN** Performance scales with model size and deliberation time.

**ZH** 性能随模型规模与思考时长提升。

**EN** Within the Qwen2.5 and Qwen3 model families, we observe a consistent trend: performance on ArtifactsBench scales positively with model capacity. Moreover, models engaging in extended inference—so-called “slow-thinkers”—tend to score higher, indicating that the intricate planning required for visual code generation benefits appreciably from deeper computational reasoning.

**ZH** 在 Qwen2.5 与 Qwen3 模型族内部，我们观察到一致的趋势：模型在 ArtifactsBench 上的表现随容量正向提升。此外，进行更长推理的模型——即所谓“慢思考”模型——得分往往更高，说明视觉代码生成所需的复杂规划明显受益于更深的计算推理。

**EN** Analysis of open-source model performance.

**ZH** 开源模型表现分析。

**EN** Among the open-source contenders, DeepSeek-R1-0528 sets a new benchmark, demonstrating that models with robust code generation and general reasoning capabilities can excel in code-centric visualization tasks. We also note an important knowledge-distillation finding: DeepSeek-R1-Distill-Qwen-32B improves by only 3 percentage points over its base Qwen-2.5-32B, yet remains 5 points below Qwen3-32B. This suggests that distillation on a limited dataset may be insufficient to endow models with the robust, generalizable skills required for advanced visual-code synthesis. This result is in line with recent findings in knowledge distillation research, where it has been shown that dynamically adjusting the distillation data to focus on areas of large performance gaps between teacher and student models is more effective than using a static dataset (Liu et al., 2024b).

**ZH** 在开源竞争者中，DeepSeek-R1-0528 树立了新的标杆，表明具备强劲代码生成能力与通用推理能力的模型可以在代码中心的视觉化任务上表现出色。我们还注意到一项关于知识蒸馏的重要发现：DeepSeek-R1-Distill-Qwen-32B 相比其基座 Qwen-2.5-32B 仅提升 3 个百分点，却仍比 Qwen3-32B 低 5 分。这说明在有限数据集上做蒸馏，可能不足以赋予模型高级视觉代码合成所需的稳健、可泛化能力。该结果与知识蒸馏领域的近期发现一致：动态调整蒸馏数据、使其聚焦师生表现差距较大的方面，比使用静态数据集更为有效（Liu et al., 2024b）。

**EN** Opportunities remain in challenging scenarios.

**ZH** 高难度场景仍有提升空间。

**EN** All models record their lowest scores on the Intensive Interactive cases within the static–dynamic classification tasks. They also perform worst on complex, project-level visualization scenarios—such as “Management System” cases—highlighting clear avenues for future improvement in these demanding settings.

**ZH** 在静态—动态分类任务中，所有模型的分数都在强交互类样例上跌至最低。它们在复杂的项目级可视化场景——例如“管理系统”类样例上也表现最差，凸显出在这些高要求场景中明确的未来改进方向。

**EN** Generalist skills outperform specialist expertise.

**ZH** 通用能力胜过专用专长。

**EN** Perhaps our most striking finding is that instruction-tuned generalist models outperform domain-specific counterparts. Specifically, Qwen-2.5-Instruct surpasses both the code-focused Qwen-2.5-coder and the vision-specialized Qwen2.5-VL-72B. This compellingly illustrates that producing high-quality visual artifacts is not a simple sum of isolated code generation and visual understanding abilities. Rather, it demands a higher-order synthesis of capabilities—including robust reasoning, nuanced instruction following, and an implicit sense of design aesthetics. These are precisely the holistic, meta-level skills that top-tier generalist models acquire through vast and diverse training, and which benchmarks like ArtifactsBench are uniquely poised to evaluate.

**ZH** 我们最引人注目的发现或许是：经指令微调的通用模型优于领域专用模型。具体地，Qwen-2.5-Instruct 同时超过了面向代码的 Qwen-2.5-coder 与面向视觉的 Qwen2.5-VL-72B。这有力说明，产出高质量视觉制品并非孤立的代码生成能力与视觉理解能力的简单相加。它要求一种更高阶的能力综合——包括稳健的推理、细腻的指令遵循，以及对设计美学的潜在感知。这些恰恰是顶级通用模型在海量而多样的训练中所获得的整体性、元层面技能，也正是 ArtifactsBench 这类基准最适合加以评测的对象。

<!-- [原子块 · img]  -->

**EN** Figure 9: An overview of the competitive landscape on ArtifactsBench, scored by the Gemini-2.5-Pro-0506 referee. This chart summarizes the overall scores (AVG) of leading models, highlighting the current state-of-the-art and the performance distribution across different model families.

**ZH** 图 9：ArtifactsBench 竞争格局概览，由 Gemini-2.5-Pro-0506 评审打分。该图汇总了领先模型的总分（AVG），呈现当前最先进水平以及不同模型族之间的性能分布。

**EN** Visual and Code-Based Analysis

**ZH** 视觉与代码维度分析

**EN** We categorize the 10 checklist items into two groups based on their evaluation dependencies: 5 vision-oriented checklists and 5 code-oriented checklists. As shown in Figure 4, The results demonstrate a positive correlation between vision and code scores, suggesting that model improvements tend to be comprehensive rather than isolated to specific capabilities. Focusing solely on visual scores or interactive experience may overlook critical strengths or weaknesses in the underlying code generation. Conversely, exclusive attention to code quality risks missing important visual aspects, leading to incomplete assessments. Furthermore, as model capabilities advance, they increasingly prioritize the visual presentation of generated code, thereby enhancing real-world usability.

**ZH** 我们按评测依据把 10 个检查清单条目分为两组：5 个视觉导向清单与 5 个代码导向清单。如图 4 所示，结果表明视觉分数与代码分数之间存在正相关，说明模型能力的提升往往是全面的，而非局限于某项特定能力。只关注视觉分数或交互体验，可能遗漏底层代码生成中的关键优劣；反之，只盯住代码质量，则可能错失重要的视觉方面，导致评估不完整。此外，随着模型能力演进，它们愈发重视所生成代码的视觉呈现，从而提升了真实可用性。

**EN** Difficulty Analysis

**ZH** 难度分析

**EN** We split the benchmark into three tiers of increasing difficulty. As illustrated in Figure 5, even the best-performing models struggle to surpass 50 points on the most challenging subset, indicating that our benchmark remains far from saturation. Moreover, the models’ relative rankings remain consistent across all tiers, and each tier continues to offer strong discriminative power—demonstrating that our benchmark reliably differentiates model capabilities at every level of difficulty.

**ZH** 我们把基准划分为难度递增的三个层级。如图 5 所示，即便表现最好的模型在最难子集上也难以超过 50 分，说明本基准远未饱和。此外，各模型的相对排名在所有层级上保持一致，且每一层级仍保持很强的区分度——这表明本基准能在每个难度水平上可靠地区分模型能力。

**EN** A.3 Validation with Human Experts

**ZH** A.3 与人类专家的验证

**EN** To validate the fidelity of our automated MLLM-based evaluation, we conduct a rigorous human evaluation study. We randomly selected 280 queries, along with the corresponding data from 6 models, and have them independently scored by multiple engineers with extensive front-end development experience. The process follows a double-blind protocol: annotators remain unaware of the MLLM’s scores, and the samples appear in randomized order to mitigate bias. The final human ground-truth score represents the median of the individual annotators’ ratings.

**ZH** 为验证我们基于多模态大语言模型的自动评测的保真度，我们开展了一项严格的人工评测研究。我们随机抽取 280 条查询以及 6 个模型的对应数据，交由多名具备丰富前端开发经验的工程师独立打分。该过程遵循双盲协议：标注员不知道多模态大语言模型给出的分数，样本以随机顺序呈现以减轻偏差。最终的人类真值分数取各标注员评分的中位数。

**EN** To quantify the agreement between our automated referee and human experts, we compute the pairwise consistency rate, denoted as Pair ACC. For a given query with ⟦SLOT_6⟧ model responses, we can form ⟦SLOT_7⟧ unique pairs of responses. We then count the number of pairs for which the MLLM referee and the human judges agree on the rank ordering (i.e., which response is better). The consistency rate is the ratio of these concordant pairs to the total number of pairs. This metric allows us to select the most reliable MLLM referee and robustly demonstrates the strong correlation between our automated evaluation and expert human judgment.

**ZH** 为量化自动评审与人类专家的一致程度，我们计算两两一致率，记为 Pair ACC。对某条查询，若存在 ⟦SLOT_6⟧ 个模型回答，则可构成 ⟦SLOT_7⟧ 个不同的回答对。我们统计多模态大语言模型评审与人类评判在排序上（即哪个回答更好）达成一致的对数。一致率即这些一致对占总对数的比例。该指标既可用于挑选最可靠的多模态大语言模型评审，也稳健地证明了我们的自动评测与专家人类判断之间存在强相关。

**EN** Cross-judge ranking consistency

**ZH** 跨评审排名一致性

**EN** We further compare the partial-order ranking induced by two state-of-the-art referee models: the closed-source Gemini-2.5-Pro-Preview-0506 and the open-source Qwen2.5-VL-72B. As illustrated in Figure 11, the two referees yield largely consistent order constraints over model performance. Residual differences are concentrated among top-tier systems, where the stronger referee exhibits finer discriminative power. This observation supports two conclusions: (1) our findings are robust to the choice of MLLM referee, and (2) stronger referees provide higher resolution at the head of the leaderboard without altering the overall competitive landscape.

**ZH** 我们进一步比较两个最先进评审模型所导出的偏序排名：闭源的 Gemini-2.5-Pro-Preview-0506 与开源的 Qwen2.5-VL-72B。如图 11 所示，两名评审在模型表现上给出的顺序约束大体一致。残余差异集中在头部系统，其中更强的评审展现出更细的分辨力。这一观察支持两点结论：（1）我们的发现对多模态大语言模型评审的选择是鲁棒的；（2）更强的评审能在排行榜头部提供更高分辨率，而不会改变整体竞争格局。

**EN** Version stability of the Gemini referee

**ZH** Gemini 评审的版本稳定性

**EN** Given that Gemini-2.5-Pro-Preview-0506 has been deprecated, we additionally compare it with the stable Gemini-2.5-Pro release. As shown in Appendix Figure 10, the two versions induce identical partial-order constraints over model rankings on ArtifactsBench. This means every pairwise ordering decision is the same, and replacing the preview with the stable version does not change any leaderboard conclusions.

**ZH** 鉴于 Gemini-2.5-Pro-Preview-0506 已被弃用，我们额外将其与稳定的 Gemini-2.5-Pro 正式版作了比较。如附录图 10 所示，两个版本在 ArtifactsBench 上对模型排名导出的偏序约束完全相同。这意味着每一对排序判定都一致，用正式版替换预览版不会改变排行榜的任何结论。

<!-- [原子块 · img]  -->

**EN** Figure 10: Version stability: Gemini-2.5-Pro-Preview-0506 vs. stable Gemini-2.5-Pro. The induced partial-order constraints are identical, preserving leaderboard conclusions.

**ZH** 图 10：版本稳定性：Gemini-2.5-Pro-Preview-0506 与稳定的 Gemini-2.5-Pro。二者导出的偏序约束完全相同，排行榜结论得以保持。

<!-- [原子块 · img]  -->

**EN** Figure 11: Cross-judge comparison (Gemini-2.5-Pro-Preview-0506 vs. Qwen2.5-VL-72B): highly consistent partial orders; minor top-tier differences.

**ZH** 图 11：跨评审对比（Gemini-2.5-Pro-Preview-0506 与 Qwen2.5-VL-72B）：偏序高度一致，头部存在细微差异。

**EN** Ablation studies.

**ZH** 消融实验。

**EN** We present ablation studies in Tables 4 and 5 to examine the alignment between different referee models and human judgments. The experimental configurations include: (1) “w/o img” - inputting only the query and answer to the LLM without images; (2) “w/ img” - leveraging the model’s visual capability by providing the query, answer, and one execution screenshot; (3) “w/ imgs” - extending the “w/ img” configuration with multiple screenshots to capture dynamic visual effects; (4) “w/ caption” - replacing images with MLLM-generated descriptions; and (5) “only w/ imgs”/“only w/ caption” - removing the answer from the “w/ imgs” and “w/ caption” input configurations respectively.

**ZH** 我们在表 4 与表 5 中给出消融实验，以考察不同评审模型与人类判断的吻合程度。实验配置包括：（1）“w/o img”——只向 LLM 输入查询与回答，不含图像；（2）“w/ img”——利用模型的视觉能力，提供查询、回答与一张执行截图；（3）“w/ imgs”——在“w/ img”配置基础上扩展为多张截图，以捕捉动态视觉效果；（4）“w/ caption”——用多模态大语言模型生成的描述替换图像；（5）“only w/ imgs”/“only w/ caption”——分别在“w/ imgs”与“w/ caption”的输入配置中去掉回答。

**EN** Table 4 reveals two key findings: First, the significant improvement in pair accuracy when including execution screenshots demonstrates that multimodal LLMs effectively utilize visual information for more reasonable evaluation. Second, comparing columns 2 and 3 shows that multiple screenshots help models capture dynamic effects, further enhancing prediction accuracy. However, since referee models can extract additional strengths and weaknesses from the code-level perspective, their evaluation criteria may diverge from human judgments. This explains why even the strongest referee model, Gemini, shows some discrepancy in scoring consistency with human assessments, which simultaneously demonstrates ArtifactsBench’s advantage of comprehensively evaluating answers from multiple dimensions.

**ZH** 表 4 揭示了两项关键发现：其一，加入执行截图后两两准确率显著提升，说明多模态大语言模型能有效地利用视觉信息做出更合理的评测。其二，对比第 2 列与第 3 列可见，多张截图有助于模型捕捉动态效果，进一步提升预测准确率。然而，由于评审模型还能从代码层面挖掘额外的优势与不足，其评判标准可能与人类判断有所分歧。这也解释了为何即便是最强的评审模型 Gemini，在打分一致性上与人类评估仍存在一定差距，同时也体现了 ArtifactsBench 从多个维度综合评估回答的优势。

**EN** The first three rows of Table 5 reveal that describing execution screenshots as text inputs can improve the evaluation accuracy of large models. Nevertheless, when the model itself has strong visual analysis capabilities, directly inputting screenshots yields better performance. The last two rows of Table 5 indicate that evaluation effectiveness decreases when only providing the query and execution screenshots, confirming the necessity of including the answer in the input. In addition, we provide a detailed analysis of the consistency analysis between ArtifactsBench and WebDev Arena in the appendix.

**ZH** 表 5 的前三行显示，把执行截图转写为文本输入可以提升大模型的评测准确率。不过，当模型本身具备较强的视觉分析能力时，直接输入截图效果更好。表 5 的最后两行表明，只提供查询与执行截图时评测效果下降，证实了在输入中包含回答的必要性。此外，我们还在附录中给出了 ArtifactsBench 与 WebDev Arena 一致性分析的详细内容。

**EN** A.4 Reproducibility and future directions

**ZH** A.4 可复现性与未来方向

**EN** We release dataset specs, checklist templates, evaluation scripts, and referee settings; future work targets richer dynamics beyond discrete screenshots, agentic multi-turn self-debugging, and broader artifact domains.

**ZH** 我们公开数据集规格、检查清单模板、评测脚本与评审设置；未来工作面向超越离散截图的更丰富动态性、智能体式的多轮自调试，以及更广的制品领域。

**EN** A.5 Evaluation Results from Additional Scoring Referees

**ZH** A.5 其他打分评审的评测结果

**EN** Table 6 and 7 present the detailed evaluation results from two distinct MLLM-as-a-Judge referees, Gemini-2.5-Pro and Qwen2.5-VL-72B, respectively, assessing multiple mainstream large language models on the ArtifactsBench benchmark. Gemini-2.5-Pro, as a leading closed-source multimodal model, provides a high-accuracy benchmarking standard, while the open-source Qwen2.5-VL-72B offers a more cost-effective alternative.

**ZH** 表 6 与表 7 分别给出两个不同的“以多模态大语言模型为评审”的评审——Gemini-2.5-Pro 与 Qwen2.5-VL-72B——在 ArtifactsBench 基准上评测多个主流大语言模型的详细结果。Gemini-2.5-Pro 作为领先的闭源多模态模型，提供了高精度的基准参照；而开源的 Qwen2.5-VL-72B 则提供了更具性价比的替代方案。

**EN** The results demonstrate a high degree of consistency in the model rankings computed by these two referee models, despite differences in their architectures and capabilities. This consistency not only validates the stability of the ArtifactsBench evaluation metrics but also indicates a convergent consensus among multimodal experts in judging code generation quality. Nevertheless, minor discrepancies are observed in the fine-grained scoring of certain complex interactive tasks, reflecting potential cognitive biases in how different MLLMs interpret long-horizon interaction logic and dynamic visual feedback.

**ZH** 结果表明，尽管两个评审模型的架构与能力不同，它们计算出的模型排名具有很高的一致性。这种一致性既验证了 ArtifactsBench 评测指标的稳定性，也说明多模态专家在评判代码生成质量上正趋于共识。不过，在某些复杂交互任务的细粒度打分上仍存在细微差异，反映出不同多模态大语言模型在理解长时程交互逻辑与动态视觉反馈时可能存在认知偏差。

<!-- [原子块 · table] MODEL IFLEN SCORE SV MMD HD II GAME SVG WEB SI MS AVG Closed-Source Large Language Models GPT-5 – 72.24 79.82 75.17 69.81 77.89 73.40 71.31 79.41 64.95 72.55 Claude-opus-4-1 – 58.07 60.47 61.35 59.42  -->

**EN** Table 6: Detailed evaluation results on ArtifactsBench, scored by the Gemini-2.5-Pro referee. Performance is detailed across interactivity levels (SV: Static Visual, MMD: Mild-to-Moderate Dynamics, HD: High Dynamics, II: Intensive Interactive) and task categories (GAME, SVG, WEB, SI: Simulation, MS: Management System). AVG is the global average. IFLEN represents the average response length. Top proprietary multimodal models lead overall, and performance scales with model capacity.

**ZH** 表 6：由 Gemini-2.5-Pro 评审打分的 ArtifactsBench 详细评测结果。性能按交互强度（SV：静态视觉；MMD：轻中度动态；HD：高动态；II：强交互）与任务类别（GAME、SVG、WEB、SI：仿真；MS：管理系统）细分。AVG 为全局平均分，IFLEN 表示平均回答长度。头部闭源多模态模型整体领先，性能随模型容量提升。

<!-- [原子块 · table] RANK MODEL INSTITUTION AVG RESPONSE LENGTH QWEN2.5-VL-72B SCORE Open-Source Large Language Models 1 Qwen2.5 7B-Instruct Qwen 7905.21 42.72 2 Qwen2.5 14B-Instruct Qwen 6334.34 44.76 3 Qwen2.5 32B-Instr -->

**EN** Table 7: Evaluation results on ArtifactsBench using Qwen2.5-VL-72B as the MLLM referee. The table presents model rankings based on comprehensive assessment across various dimensions. RANK indicates the position in evaluation order, AVG RESPONSE LENGTH represents the average length of model responses, and QWEN2.5-VL-72B SCORE shows the evaluation score when using Qwen2.5-VL-72B as the multimodal referee.

**ZH** 表 7：以 Qwen2.5-VL-72B 作为多模态大语言模型评审时在 ArtifactsBench 上的评测结果。表中给出基于多维度综合评估的模型排名。RANK 表示评测顺序中的位次，AVG RESPONSE LENGTH 表示模型回答的平均长度，QWEN2.5-VL-72B SCORE 表示以 Qwen2.5-VL-72B 作为多模态评审时的评测分数。

**EN** A.6 Quality Filtering of Queries

**ZH** A.6 查询的质量过滤

**EN** We use the following prompt to filter the quality of queries, with the aim of selecting high-quality, practical, complete, and privacy-free queries.

**ZH** 我们使用如下提示词对查询质量进行过滤，目的是筛选出高质量、实用、完整且不涉及隐私的查询。

<!-- [原子块 · svg]  -->

**EN** Figure 12: The prompt for query quality filtering.

**ZH** 图 12：查询质量过滤所用的提示词。

**EN** A.7 Classification of Queries

**ZH** A.7 查询的分类

**EN** We use Gemini-2.5-Pro to classify queries, and the specific prompt is shown in Figures 13 and 14. They only require a query as input.

**ZH** 我们使用 Gemini-2.5-Pro 对查询进行分类，具体提示词如图 13、14 所示。它们只需要一条查询作为输入。

<!-- [原子块 · svg]  -->

**EN** Figure 13: The prompt for category classification.

**ZH** 图 13：类别分类所用的提示词。

<!-- [原子块 · svg]  -->

**EN** Figure 14: The prompt for visual classification.

**ZH** 图 14：视觉分类所用的提示词。

**EN** A.8 The Prompt for Model Scoring

**ZH** A.8 模型打分所用的提示词

**EN** We present the prompt for generating the checklist in Figures 15 and 16, which takes a query as input. After manual review, it will be put into use. The final scoring prompt, shown in Figure 17, requires the query, answer, and checklist as input.

**ZH** 我们在图 15、16 中给出生成检查清单所用的提示词，其输入为一条查询。经人工审核后投入使用。最终打分提示词如图 17 所示，需要查询、回答与检查清单作为输入。

<!-- [原子块 · svg]  -->

**EN** Figure 15: The first part of the prompt for visual classification

**ZH** 图 15：视觉分类提示词的第一部分

<!-- [原子块 · svg]  -->

**EN** Figure 16: The second part of the prompt for visual classification.

**ZH** 图 16：视觉分类提示词的第二部分。

<!-- [原子块 · svg]  -->

**EN** Figure 17: The final scoring prompt.

**ZH** 图 17：最终打分提示词。
