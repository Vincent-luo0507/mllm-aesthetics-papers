# Design Theater：评估生成式 UI 工具中面向用户的设计推理与实现之间的落差

> 原标题：Design Theater: Evaluating the Gap Between User-Facing Design Reasoning and Implementation in Generative UI Tools
> 作者：Kashif Imteyaz, Kaif Imteyaz, Nakul Rajpal, Kaif Shaikh, Michael Muller, Saiph Savage · arXiv:2607.22928 · 2026-07-24

<!-- [原子块 · verbatim] Design Theater: Evaluating the Gap Between User-Facing Design Reasoning and Implementation in Generative UI Tools -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] Generative UI tools promise to democratize UI design by turning natural language descriptions into complete interfaces. Alongside the interface, these tools generate user-facing design rationales that -->

**EN** Introduction

**ZH** 引言

**EN** Generative UI tools are increasingly positioned as a way to lower barriers to interface design by allowing users to generate interface prototypes from natural-language prompts (66; 12; 83). Recent work describes such tools as valuable not only for UX designers, but also for adjacent roles such as developers and product managers (12). Generative UI tools such as Vercel v0, Claude Artifacts, ChatGPT Canvas, Firebase Studio, and Bolt support prompt-based workflows in which users describe an interface or application idea and receive generated code, previews, or deployable prototypes (70; 4; 49; 25; 62).

**ZH** 生成式 UI 工具正越来越多地被定位为降低界面设计门槛的一种途径：它让用户可以从自然语言提示生成界面原型（66; 12; 83）。近期工作认为，这类工具不仅对 UX 设计师有价值，对开发者与产品经理等相关角色同样有价值（12）。Vercel v0、Claude Artifacts、ChatGPT Canvas、Firebase Studio 与 Bolt 等生成式 UI 工具支持基于提示的工作流——用户描述一个界面或应用构想，即可获得生成的代码、预览或可部署的原型（70; 4; 49; 25; 62）。

**EN** Beyond generating interfaces, these tools often narrate their design process through what we call user-facing design reasoning: explanations of what they intend to create, why particular design decisions are appropriate, and how the output addresses layout, accessibility, color, interaction, or broader usability principles (48). For first-time creators, product managers, engineers, or other non-design stakeholders, such reasoning can function as a signal of design competence, making generated interfaces appear more deliberate, principled, and trustworthy (44; 64). As AI-generated interfaces move from experimentation into organizational design and development workflows, this reasoning may become part of how teams explain, review, and justify design decisions (61; 66). As a result, users may treat the tool’s reasoning as evidence that usability, accessibility, and interaction-design concerns were properly addressed, even when they lack the expertise to verify (38; 64). For example, when a generative UI tool states that it will create “a responsive three-column grid with accessible contrast ratios and keyboard-navigable tabs”, it creates the impression of careful, principle-driven design. Yet it remains unclear whether this reasoning is actually reflected in the generated interface. This is especially concerning as design work is increasingly delegated to AI tools and reviewed by product managers, engineers, or other stakeholders who may not have formal design training. Without methods for evaluating whether generative UI tools follow through on their user-facing design reasoning, teams may over-trust interfaces that appear professionally designed while failing to implement critical usability, accessibility, or responsiveness requirements (44).

**ZH** 除了生成界面，这些工具还常常通过我们所说的面向用户的设计推理来叙述其设计过程：解释它们打算创造什么、为何某些设计决策是恰当的，以及输出如何回应版面、无障碍、色彩、交互或更广泛可用性原则方面的考量（48）。对初次创作者、产品经理、工程师或其他非设计背景的利益相关方而言，这类推理可以充当设计能力的信号，使生成的界面显得更有章法、更有原则、更值得信赖（44; 64）。随着 AI 生成的界面从试验阶段进入组织内的设计与开发工作流，这类推理可能成为团队解释、评审与论证设计决策的一部分（61; 66）。结果是，用户可能把工具的推理当作可用性、无障碍与交互设计问题已被妥善处理的证据，即便他们并不具备验证所需的专业知识（38; 64）。例如，当一个生成式 UI 工具声称将创建「一个具有无障碍对比度、标签页可用键盘导航的响应式三栏网格」时，它营造出一种经过审慎、原则驱动设计的印象。然而，这种推理究竟是否真的反映在生成的界面中，仍不清楚。随着设计工作越来越多地被委托给 AI 工具，并由可能未受过正式设计训练的产品经理、工程师或其他利益相关方来评审，这一点尤其令人担忧。若缺乏评估生成式 UI 工具是否兑现其面向用户的设计推理的方法，团队可能会过度信任那些看起来专业、却未能实现关键可用性、无障碍或响应式要求的界面（44）。

**EN** To better understand and study this phenomenon, we introduce the concept of Design Theater: the production of user-facing design reasoning that bears little relationship to the actual design implementation. We define it by its effect on the reader. A rationale written in the language of professional design reads as evidence of deliberate, principle-driven decision-making, whether or not those commitments are realized in the artifact. Persuasive reasoning invites less scrutiny of the generated artifact, allowing overreliance to emerge before verification occurs (64).

**ZH** 为更好地理解并研究这一现象，我们提出 Design Theater 这一概念：产出与真实设计实现几乎无关的面向用户的设计推理。我们以其对读者的影响来界定它。一段用专业设计语言写就的理由陈述，无论这些承诺是否在产物中兑现，读起来都像是经过审慎、原则驱动决策的证据。富有说服力的推理会招致对生成产物更少的审视，使过度依赖在验证发生之前就已形成（64）。

**EN** However, defining Design Theater is not enough. We also need benchmarks and metrics that can measure how often generative UI tools produce mismatches between their user-facing design reasoning and actual implementations. Quantifying Design Theater allows researchers and practitioners to move beyond anecdotal examples, compare tools systematically, and identify when interfaces appear trustworthy despite failing to implement key usability, accessibility, or interaction-design requirements.

**ZH** 然而，仅仅定义 Design Theater 还不够。我们还需要基准与指标，能够衡量生成式 UI 工具在其面向用户的设计推理与真实实现之间产生错位的频率。量化 Design Theater 能让研究者与从业者超越轶事式例证，系统地比较各工具，并识别出那些看起来可信、却未能实现关键可用性、无障碍或交互设计要求的界面。

**EN** To address this need, this paper presents a benchmark and three metrics for measuring Design Theater in generative UI tools. The benchmark evaluates reasoning-to-implementation alignment and design homogenization across 120 UI designs generated by five state-of-the-art UI agent tools across 24 design tasks. These tasks span three tiers of design tasks: structural tasks, including layout and information architecture; styling tasks, including color, typography, and spacing; and functional tasks, including interactivity and user flows. We pair the benchmark with three metrics: Thinking Fidelity Score (TFS), Principle Adherence Score (PAS), and Design Homogeneity Index (DHI). Together, these metrics quantify whether tools’ user-facing design reasoning is reflected in their generated interfaces and whether different tools produce similar designs for the same prompt. Using this benchmark and set of metrics, we study the following research questions:

**ZH** 为满足这一需求，本文提出一个基准与三项指标，用于衡量生成式 UI 工具中的 Design Theater。该基准在 5 个当前最先进的 UI 智能体工具就 24 项设计任务生成的 120 个 UI 设计上，评估推理到实现的对齐程度以及设计同质化。这些任务覆盖三个层级的设计任务：结构类任务，包括版面与信息架构；样式类任务，包括色彩、字体排印与间距；功能类任务，包括交互性与用户流程。我们还为基准配上三项指标：思维保真度分数（TFS）、原则遵循度分数（PAS）与设计同质化指数（DHI）。这些指标共同量化了工具的面向用户的设计推理是否反映在其生成的界面中，以及不同工具针对同一提示是否会产出相似的设计。借助该基准与这套指标，我们研究以下问题：

**EN** 1. To what extent is the user-facing design reasoning produced by generative UI tools reflected in the interfaces they implement?

**ZH** 1. 生成式 UI 工具产出的面向用户的设计推理，在多大程度上反映在它们所实现的界面中？

**EN** 2. To what extent do generative UI tools recognize and implement UX principles that are implicitly embedded in natural-language prompts (tasks)?

**ZH** 2. 生成式 UI 工具在多大程度上识别并实现了隐式嵌入自然语言提示（任务）中的 UX 原则？

**EN** 3. How much do generated interfaces vary in their visual appearance, color schemes, and layouts when different generative UI tools are given the same task?

**ZH** 3. 当不同的生成式 UI 工具接到同一任务时，生成的界面在视觉外观、配色方案与版面上有多大差异？

**EN** Our findings suggest that, on average, roughly 25% of user-facing design reasoning is not implemented in the generated interface, with implementation failures increasing to 34% for functional requirements. Tools recognize roughly half of the UX principles implicitly embedded in prompts (mean PAS = 0.54), with four of the five tools implementing 6% or fewer functional principles. We also find convergence across tools: when given the same prompt, generated interfaces showed narrow pairwise differences in visual appearance and layout organization, while color choices varied more widely. Based on these findings, we discuss the implications for how generative UI tools are evaluated and for the stakeholders who increasingly review their output.

**ZH** 我们的发现表明：平均而言，约 25% 的面向用户的设计推理并未在生成的界面中实现，而在功能类要求上，实现失败率上升到 34%。工具能识别出提示中隐式嵌入的大约一半 UX 原则（PAS 均值 = 0.54），五个工具中有四个实现的功能类原则不超过 6%。我们还发现工具之间存在趋同：给定同一提示时，生成的界面在视觉外观与版面组织上呈现很小的成对差异，而色彩选择的差异更大。基于这些发现，我们讨论了这些结果对生成式 UI 工具的评估方式、以及对其产出进行评审的利益相关方意味着什么。

**EN** Our paper makes the following contributions:

**ZH** 本文的贡献如下：

**EN** • Conceptualization of Design Theater. We introduce the concept of Design Theater, describing how generative UI tools produce plausible design rationales that may not correspond to their implemented interfaces.

**ZH** • Design Theater 的概念化。我们提出 Design Theater 这一概念，描述生成式 UI 工具如何产出看似合理、却可能与其所实现界面不相对应的设计理由。

**EN** • A benchmark and metrics for evaluating Design Theater. We introduce a benchmark with 24 UI design tasks and three complementary metrics, TFS, PAS, and DHI, for evaluating reasoning-to-implementation alignment, implicit UX principle adherence, and cross-tool design homogenization.

**ZH** • 用于评估 Design Theater 的基准与指标。我们提出一个包含 24 项 UI 设计任务的基准，以及 TFS、PAS、DHI 三项互补指标，用于评估推理到实现的对齐、对隐式 UX 原则的遵循，以及跨工具的设计同质化。

**EN** • Empirical evaluation of generative UI tools. Through a systematic study of 120 interfaces generated by five UI tools across 24 design tasks, we show that misalignment between user-facing reasoning and implementation is widespread and concentrates in functional design. We find that designs converge in visual appearance and layout when tools are given the same prompt.

**ZH** • 对生成式 UI 工具的实证评估。通过对 5 个 UI 工具在 24 项设计任务上生成的 120 个界面所做的系统研究，我们表明面向用户的推理与实现之间的错位十分普遍，并集中在功能类设计上；我们还发现，当工具接到同一提示时，设计在视觉外观与版面上趋于趋同。

**EN** Related Work

**ZH** 相关工作

**EN** Vibe Coding and AI-Assisted Co-Creation

**ZH** 氛围编程与 AI 辅助共创

**EN** Vibe coding is an emerging practice in which developers build software by describing intent in natural language rather than writing code directly (43). Its recent rise aligns with coding tools such as OpenAI Codex, Claude Code, Cursor, and GitHub Copilot (50; 31; 3; 24), which promise to reduce barriers to software development. These coding agents can produce code that compiles and runs, though prior work suggests that generated code matches users’ intended outputs only at moderate rates (81).

**ZH** 氛围编程（vibe coding）是一种新兴实践：开发者用自然语言描述意图来构建软件，而非直接编写代码（43）。它的兴起与 OpenAI Codex、Claude Code、Cursor、GitHub Copilot 等编码工具的发展同步（50; 31; 3; 24），这些工具承诺降低软件开发的门槛。这类编码智能体可以产出能编译、能运行的代码，但先前工作表明，生成的代码与用户预期输出相符的比例只是中等（81）。

**EN** Researchers have therefore begun examining how users interact with coding agents. A common theme is the redistribution of effort from writing code to evaluating AI output and managing conversational context (60). In this workflow, users may skip quality assurance steps, reducing the reliability of the final output (22). These omissions can carry real consequences: studies have found that 40% of GitHub Copilot-generated code contained security weaknesses (53), and an analysis of production repositories found similar issues in 30% of Python and 24% of JavaScript snippets (23).

**ZH** 因此，研究者开始考察用户如何与编码智能体互动。一个共同的主题是：精力从编写代码重新分配到评估 AI 输出与管理对话上下文上（60）。在这一工作流中，用户可能跳过质量保证环节，从而降低最终产出的可靠性（22）。这些疏漏会带来实际后果：研究发现，GitHub Copilot 生成的代码中有 40% 含有安全弱点（53）；一项针对生产仓库的分析发现，Python 与 JavaScript 代码片段中分别有 30% 与 24% 存在类似问题（23）。

**EN** These concerns are not limited to code correctness. AI-assisted creation also raises questions about output diversity (18). In a large-scale writing experiment, access to a generative AI tool improved individual output quality but reduced collective output diversity across participants (18). Similar homogenization effects have been identified in design tasks (72) and creative ideation (2). Related work also shows that generative systems can default to Western cultural conventions (1), a concern that is relevant for interface design, where layout, color, typography, and interaction patterns are culturally situated.

**ZH** 这些担忧并不限于代码正确性。AI 辅助创作也引发了关于输出多样性的疑问（18）。在一项大规模写作实验中，使用生成式 AI 工具提升了个体产出质量，却降低了参与者之间产出的集体多样性（18）。在设计任务（72）与创意构思（2）中也发现了类似的同质化效应。相关研究还表明，生成式系统可能默认采用西方文化惯例（1）——这对界面设计而言事关紧要，因为版面、色彩、字体排印与交互模式都具有文化情境性。

**EN** Concerns about homogenization also build on a longer history of web design convergence. 26 found that web designs became more similar after 2007, with layout distance alone dropping over 30%, driven largely by the adoption of shared libraries and frameworks like Bootstrap. Our work asks whether generative UI tools extend this trajectory while obscuring it, layering rationales of deliberate design choice over outputs that may default to a narrow band of conventions.

**ZH** 对同质化的担忧还建立在网页设计趋同的更长历史上。26 发现，2007 年之后网页设计变得更加相似，仅版面距离就下降了 30% 以上，这主要由 Bootstrap 等共享库与框架的采用所驱动。我们的工作追问的是：生成式 UI 工具是否在延续这一轨迹的同时将其遮蔽——把「深思熟虑的设计选择」这类理由，叠加在那些本可能默认落入狭窄惯例区间的输出之上。

**EN** Beyond generating outputs, these systems increasingly narrate their process through user-facing reasoning that explain why particular choices were made. Prior work suggests that users may scan or rely on these traces instead of evaluating outputs directly (22). What remains unexamined is whether such traces accurately reflect what was built, and whether users can distinguish competent design from a persuasive description of competence.

**ZH** 除生成产出之外，这些系统还越来越多地通过面向用户的推理来叙述其过程，解释为何做出特定选择。先前工作表明，用户可能会扫读或依赖这些轨迹，而不是直接评估产出（22）。尚未被检视的是：这类轨迹是否如实反映了所构建的东西，以及用户能否区分真正称职的设计与对能力的有说服力描述。

**EN** From Design Templates to Generative UI Tools

**ZH** 从设计模板到生成式 UI 工具

**EN** Early low-code and template-based interface tools lowered the barrier to creating interactive systems by allowing users to assemble interfaces from predefined components rather than writing code from scratch. While simple and effective, these tools constrained users to the structures and interaction patterns provided by the template system. Subsequent research moved beyond templates toward machine-learning systems for translating interface images or sketches into code, detecting UI components, and recovering interface structure from screenshots (7; 33; 79; 77). These systems advanced computational interface understanding, but often remained tied to specific input modalities, datasets, or interaction domains.

**ZH** 早期的低代码与基于模板的界面工具，通过让用户从预定义组件组装界面、而非从零编写代码，降低了创建交互式系统的门槛。这些工具虽然简单有效，却把用户约束在模板系统所提供的结构与交互模式之内。后续研究超越了模板，转向机器学习系统，用于把界面图像或草图转换为代码、检测 UI 组件，以及从截图中恢复界面结构（7; 33; 79; 77）。这些系统推进了对界面的计算理解，但往往仍受限于特定的输入模态、数据集或交互领域。

**EN** The integration of large language models further expanded design-generation workflows beyond fixed templates and task-specific models. LLM-powered systems now support a range of creative design tasks, including text-to-image product design (67), animation design (68; 45), and interactive story generation (15), and the use of generated images as probes in co-design (30).

**ZH** 大语言模型的引入进一步把设计生成工作流拓展到固定模板与专用模型之外。由 LLM 驱动的系统现已支持一系列创意设计任务，包括文本到图像的产品设计（67）、动画设计（68; 45）、交互式故事生成（15），以及把生成图像用作共同设计中的探针（30）。

**EN** More recently, generative UI tools have extended this trajectory by producing interface artifacts from natural-language prompts. Tools such as Vercel v0 (32), Lovable (17), and Replit (57) support prompt-based workflows for generating interface code, previews, and deployable prototypes. Many also produce user-facing reasoning traces that explain the design choices behind the generated interface. This shift has prompted renewed attention to computational approaches for UI understanding, generation, and evaluation (36; 54), including work arguing that interfaces must increasingly be designed not only for human users but also for AI agents acting on users’ behalf (54).

**ZH** 更近期地，生成式 UI 工具通过从自然语言提示产出界面产物，延展了这一轨迹。Vercel v0（32）、Lovable（17）与 Replit（57）等工具支持基于提示的工作流，用于生成界面代码、预览与可部署原型。许多工具还会产出面向用户的推理轨迹，解释生成界面背后的设计选择。这一转变重新引发了对 UI 理解、生成与评估的计算方法的关注（36; 54），其中包括这样一种观点：界面的设计对象不再只是人类用户，还包括代表用户行事的 AI 智能体（54）。

**EN** Although these tools can produce visually plausible and functional artifacts, many evaluations of AI code-generation systems still emphasize functional or code-level correctness (11; 81). Design quality, however, is not reducible to functional correctness (63). A UI that renders without errors can still exhibit poor information architecture, incoherent visual hierarchy, inaccessible interaction patterns, or cultural and aesthetic biases embedded in training data (1). Current generative UI tools offer limited support for verifying whether these qualities are present in the generated output, particularly when the tool’s own reasoning traces suggest they have been addressed.

**ZH** 尽管这些工具能产出视觉上合理、功能上可用的产物，许多针对 AI 代码生成系统的评估仍侧重功能或代码层面的正确性（11; 81）。然而设计质量并不能还原为功能正确性（63）。一个渲染无报错的 UI 仍可能表现出糟糕的信息架构、混乱的视觉层次、不可用的交互模式，或是训练数据中嵌入的文化与审美偏见（1）。当前的生成式 UI 工具在验证这些性质是否出现在生成产出中方面支持有限，尤其是当工具自身的推理轨迹暗示它们已被处理时。

**EN** LLM Reasoning Traces and User Interpretation

**ZH** LLM 推理轨迹与用户解读

**EN** Chain-of-thought (CoT) prompting instructs language models to generate intermediate reasoning steps before producing a final answer, improving performance on arithmetic, common-sense, and symbolic reasoning tasks (74; 39; 73). Subsequent work has treated these generated rationales as both a performance enhancer and a possible window into model behavior.

**ZH** 思维链（CoT）提示指示语言模型在给出最终答案前先生成中间推理步骤，从而提升其在算术、常识与符号推理任务上的表现（74; 39; 73）。后续工作把这些生成的理由既当作性能增强手段，也当作窥探模型行为的可能窗口。

**EN** However, a separate line of work questions whether these traces faithfully reflect the model’s internal reasoning. When biased features are introduced into prompts, model answers can shift while the accompanying rationales fail to account for those shifts, producing plausible but unfaithful explanations (69). Other work finds that early reasoning steps can be modified without changing final outputs, further suggesting that generated rationales may function as post-hoc reconstructions rather than faithful process logs (41; 34).

**ZH** 然而，另一条研究线索质疑这些轨迹是否忠实反映了模型的内部推理。当提示中被引入偏置特征时，模型答案可能改变，而伴随的理由却无法解释这些变化，从而产生看似合理却不忠实的解释（69）。另有研究发现，早期的推理步骤可以在不改变最终输出的情况下被修改，这进一步表明生成的理由可能充当事后重构，而非忠实的过程记录（41; 34）。

**EN** The faithfulness of generated rationales is not only a model-centric concern; it also affects how users interpret and rely on AI systems. Empirical work shows that users treat reasoning traces as trust-calibration tools, using them to interpret code explanations and decide whether to accept or revise AI outputs (64). The presentation of rationales alone can shape trust in AI decisions, even when the underlying model behavior remains unchanged (64; 8).

**ZH** 生成理由的忠实性不仅是模型层面的关切，它也影响用户如何解读与依赖 AI 系统。实证工作表明，用户把推理轨迹当作信任校准工具，用它来解读代码解释，并决定接受还是修改 AI 输出（64）。仅仅是理由的呈现方式就能塑造对 AI 决策的信任，即便底层模型行为并未改变（64; 8）。

**EN** Most work on reasoning-trace faithfulness examines tasks with externally checkable answers, such as arithmetic, fact verification, and symbolic reasoning (74; 69; 13; 8). Design reasoning presents a different challenge. UI outputs are visual and interactive artifacts whose quality depends on contextual, multi-dimensional, and often subjective criteria, including usability, accessibility, visual hierarchy, and interaction flow. Unlike this literature, which asks whether rationales reflect the model’s internal reasoning process, we ask a downstream question: whether the rationale is consistent with the artifact the user actually receives. For non-expert stakeholders, who often read these rationales as design documentation, the key issue is whether the rationale accurately describes the resulting artifact. Whether this relationship holds in open-ended creative tasks such as UI generation remains unexplored.

**ZH** 多数关于推理轨迹忠实性的工作考察的是答案可被外部检验的任务，如算术、事实验证与符号推理（74; 69; 13; 8）。设计推理则提出了不同的挑战。UI 输出是视觉化、可交互的产物，其质量取决于情境化、多维度且往往主观的标准，包括可用性、无障碍性、视觉层次与交互流程。与这类文献追问「理由是否反映模型的内部推理过程」不同，我们追问的是一个下游问题：理由是否与用户实际拿到的产物一致。对常把这些理由当作设计文档来读的非专业利益相关方而言，关键问题在于理由是否准确描述了最终产物。在 UI 生成这类开放式创意任务中，这一关系是否成立仍未得到探索。

**EN** Automated Design Evaluation and UX Metrics

**ZH** 自动化设计评估与 UX 指标

**EN** Usability evaluation has a longer history than its current automated forms suggest. Before heuristic methods became central in HCI, human factors research developed standardized instruments for evaluating workload, usability, situation awareness, and readability in safety-critical domains (28; 10; 75). Heuristic evaluation entered this landscape as a deliberately lightweight alternative (48), valued for making usability problems inspectable without requiring full user studies. We draw on heuristic and guideline-based evaluation pragmatically: these frameworks do not exhaust design quality, but they provide inspectable commitments that can be checked against generated artifacts. Since design quality is situated and shaped by context, values, and power relations (27; 16), our benchmark evaluates whether tools implement the commitments they themselves make, without claiming that any checklist can fully determine design appropriateness. Contextual Inquiry (37) and Scandinavian Participatory Design (20) offer a complementary tradition, grounding design assessment in real work contexts and the expertise of affected users rather than expert inspection alone. This tradition reminds us that heuristic and guideline-based evaluation can be useful without fully capturing situated design quality.

**ZH** 可用性评估的历史比其当前的自动化形态更为久远。在启发式方法成为 HCI 的核心之前，人因研究已开发出标准化工具，用于在安全关键领域评估工作负荷、可用性、情境意识与可读性（28; 10; 75）。启发式评估作为一种刻意为之的轻量替代方案进入这一领域（48），其价值在于无需完整用户研究就能让可用性问题变得可检视。我们务实地借鉴启发式与基于指南的评估：这些框架并未穷尽设计质量，却提供了可对照生成产物加以检验的可检视承诺。由于设计质量是情境化的，并由语境、价值与权力关系所塑造（27; 16），我们的基准评估的是工具是否兑现了它们自己所做出的承诺，而不声称任何检查清单都能完全判定设计的恰当性。情境调查（Contextual Inquiry）（37）与斯堪的纳维亚参与式设计（20）提供了互补的传统：它们把设计评估扎根于真实工作语境与受影响用户的专业知识，而非仅依赖专家检视。这一传统提醒我们，启发式与基于指南的评估虽有用，却无法完整捕捉情境化的设计质量。

**EN** Alongside heuristic methods, design communities developed more implementable specifications, including platform interface guidelines (5) and the Web Content Accessibility Guidelines (71). Automated evaluation tools later operationalized some of these specifications and perceptual principles. Axe-core and Lighthouse evaluate accessibility and performance against established web standards (65; 14), while Aalto Interface Metrics computes perceptual measures such as visual clutter and learnability (51). More recent AI-driven methods provide design feedback on layout, color, and typography (42), predict visual attention on interfaces (35), or use LLMs as design critics grounded in heuristic and guideline-based datasets (19; 36).

**ZH** 与启发式方法并行，设计界还发展出更具可实施性的规范，包括平台界面指南（5）与《Web 内容无障碍指南》（71）。自动化评估工具后来把这些规范与感知原则中的一部分付诸操作：Axe-core 与 Lighthouse 依据既有的 Web 标准评估无障碍性与性能（65; 14），Aalto Interface Metrics 则计算视觉杂乱度与可学习性等感知度量（51）。更近期的 AI 驱动方法针对版面、色彩与字体排印提供设计反馈（42），预测界面上的视觉注意（35），或把 LLM 用作扎根于启发式与指南类数据集的设计评论者（19; 36）。

**EN** Across these approaches, evaluation criteria are typically grounded in external specifications such as Nielsen’s heuristics, WCAG, platform guidelines, perceptual models, or human-factors instruments. However, they generally do not examine whether a tool’s own stated design reasoning is reflected in its generated output. A tool may provide a rationale explaining that it prioritizes accessibility, describe its color choices in terms of WCAG contrast ratios, and narrate a deliberate information hierarchy, yet produce an interface that contradicts those commitments. Our work addresses this gap by treating usability, accessibility, and interaction-design principles as rationales that can be verified against generated artifacts, rather than assurances to be accepted.

**ZH** 在这些方法中，评估标准通常扎根于外部规范，如 Nielsen 的启发式准则、WCAG、平台指南、感知模型或人因量表。然而它们一般并不考察工具自身陈述的设计推理是否反映在其生成产出中。一个工具可能给出解释，声称自己优先考虑无障碍性、用 WCAG 对比度来描述其色彩选择、并叙述了一番深思熟虑的信息层次，却产出一个与这些承诺相矛盾的界面。我们的工作通过把可用性、无障碍性与交互设计原则当作可对照生成产物检验的理由、而非应当照单接受的保证，来填补这一空白。

**EN** Methodology

**ZH** 研究方法

**EN** Our methodology is designed to quantify Design Theater: mismatches between the user-facing design reasoning produced by generative UI tools and the interfaces they actually implement. To do so, we introduce a benchmark composed of 24 UI generation tasks and three evaluation metrics: Thinking Fidelity Score (TFS), Principle Adherence Score (PAS), and Design Homogeneity Index (DHI). Together, the benchmark and metrics allow us to assess whether generative UI tools follow through on their stated design reasoning, recognize UX principles embedded in natural-language prompts, and converge toward similar interface designs, revealing potential design homogenization.

**ZH** 我们的方法旨在量化 Design Theater：生成式 UI 工具产出的面向用户的设计推理与其实际实现的界面之间的错位。为此，我们提出一个由 24 项 UI 生成任务组成的基准，以及三项评估指标：思维保真度分数（TFS）、原则遵循度分数（PAS）与设计同质化指数（DHI）。基准与指标共同使我们能够评估生成式 UI 工具是否兑现其陈述的设计推理、能否识别自然语言提示中嵌入的 UX 原则，以及是否趋向于相似的界面设计，从而揭示潜在的设计同质化。

**EN** Generative UI Tools

**ZH** 生成式 UI 工具

**EN** We evaluate five widely used generative UI tools: ChatGPT, Claude, Firebase Studio, Vercel v0, and Bolt (70; 4; 49; 25; 62). We selected tools that: (1) accept natural-language descriptions as input; (2) generate HTML, CSS, JavaScript, or equivalent frontend code; and (3) produce user-facing reasoning traces that explain their design decisions.

**ZH** 我们评估了五个广泛使用的生成式 UI 工具：ChatGPT、Claude、Firebase Studio、Vercel v0 与 Bolt（70; 4; 49; 25; 62）。我们的选取标准是工具必须：（1）接受自然语言描述作为输入；（2）生成 HTML、CSS、JavaScript 或等价的前端代码；（3）产出解释其设计决策的面向用户的推理轨迹。

**EN** For each tool, we used its default user-facing configuration. We did not modify system-level or developer-level prompts, and we left each tool’s default model settings unchanged. This setup reflects how non-expert creators are likely to encounter and use these tools in practice.

**ZH** 对每个工具，我们都使用其默认的面向用户的配置。我们没有修改系统级或开发者级提示，也保持各工具的默认模型设置不变。这一设定反映了非专业创作者在实践中接触与使用这些工具的方式。

**EN** Benchmark Design

**ZH** 基准设计

**EN** We introduce a benchmark of 24 UI generation tasks designed to evaluate reasoning-to-implementation alignment in generative UI tools. In the benchmark, each task consists of a natural-language prompt that asks a generative UI tool to create a complete interface for a particular scenario. The prompts are designed to implicitly embed UX principles through user needs, contextual constraints, audience characteristics, and usage scenarios, rather than explicitly instructing the tool to implement specific design principles. This setup allows us to evaluate whether generative UI tools can recognize and operationalize fundamental UX requirements that are implied by the prompt, reflecting how novice designers and non-expert users are likely to request interfaces in practice (12; 55; 82).

**ZH** 我们提出一个包含 24 项 UI 生成任务的基准，用于评估生成式 UI 工具中推理到实现的对齐程度。在该基准中，每项任务由一条自然语言提示构成，要求生成式 UI 工具为特定场景创建一个完整界面。这些提示被设计为通过用户需求、情境约束、受众特征与使用场景来隐式嵌入 UX 原则，而不是明确指示工具去实现特定的设计原则。这一设定使我们能够评估生成式 UI 工具能否识别并落实提示所隐含的基本 UX 要求，这也反映了新手设计师与非专业用户在实践中可能如何提出界面需求（12; 55; 82）。

**EN** Our benchmark is organized into three tiers of design tasks that reflect core dimensions of UX design: structural organization, visual presentation, and functional interaction (58; 35; 48). Each tier foregrounds a different kind of design work, allowing us to examine where Design Theater might appear in the generated interfaces. Structural tasks help us to examine how generative UI tools organize information, styling tasks examine how tools make visual design decisions, and functional tasks examine how tools implement interactive behavior. This organization allows us to study whether reasoning-to-implementation gaps emerge differently across what an interface: 1) contains; 2) how it looks; and 3) how it behaves.

**ZH** 我们的基准按三个层级的设计任务组织，对应 UX 设计的核心维度：结构组织、视觉呈现与功能交互（58; 35; 48）。每个层级突出不同类型的设计工作，让我们得以考察 Design Theater 可能出现在生成界面的哪些地方。结构类任务用于考察生成式 UI 工具如何组织信息，样式类任务考察工具如何做出视觉设计决策，功能类任务考察工具如何实现交互行为。这一组织方式使我们能够研究：推理到实现的缺口在界面的 1) 包含什么；2) 看起来如何；3) 行为怎样这三个方面是否会以不同方式出现。

**EN** Tier 1: Structural Tasks

**ZH** 第一层级：结构类任务

**EN** Structural tasks ask generative UI tools to create interfaces where the central challenge is how information is structured (58). These tasks focus on whether tools can organize information in ways that help users understand what content exists, how different pieces of content relate to each other, where to find relevant information, and what actions to take next. We use these tasks to study whether tools can translate reasoning about information structure into concrete interface decisions, such as grouping related content, ordering sections meaningfully, creating navigation paths, routing different user groups, and surfacing high-priority information. The tasks progress from simple single-audience interfaces, such as a local business website, to more complex civic or institutional systems where multiple user groups must locate different types of information.

**ZH** 结构类任务要求生成式 UI 工具创建的界面，其核心挑战在于信息如何被组织（58）。这些任务关注工具能否以帮助用户理解「存在哪些内容、不同内容之间如何关联、到哪里去找相关信息、下一步该采取什么行动」的方式来组织信息。我们用这些任务研究工具能否把关于信息结构的推理转化为具体的界面决策，例如把相关内容分组、对章节做有意义的排序、创建导航路径、为不同用户群体分流，以及凸显高优先级信息。任务从面向单一受众的简单界面（如本地商户网站）逐步推进到更复杂的市政或机构系统——在那里，多类用户群体必须找到不同类型的信息。

**EN** Tier 2: Styling Tasks

**ZH** 第二层级：样式类任务

**EN** Styling tasks ask generative UI tools to create interfaces where the main design challenge is visual communication (35). These tasks help us study whether tools can translate visual design reasoning into concrete styling decisions, such as color choices, typography, spacing, visual hierarchy, brand expression, readability, accessibility, and emotional tone. The tasks progress from straightforward branding scenarios to more complex interfaces for users with constrained devices, varying literacy levels, or heightened emotional stress.

**ZH** 样式类任务要求生成式 UI 工具创建的界面，其主要设计挑战在于视觉传达（35）。这些任务帮助我们研究工具能否把视觉设计推理转化为具体的样式决策，例如色彩选择、字体排印、间距、视觉层次、品牌表达、可读性、无障碍性与情绪基调。任务从直白的品牌场景逐步推进到面向设备受限、识字水平不一或情绪压力更高的用户的更复杂界面。

**EN** Tier 3: Functional Tasks

**ZH** 第三层级：功能类任务

**EN** Functional tasks ask generative UI tools to create interfaces where the central challenge is how the interface behaves during user interaction (48). These tasks focus on whether tools can implement interactive behavior that supports users as they move through a workflow, encounter errors, change input states, navigate between roles, or use accessibility features. We use these tasks to study whether tools can translate interaction-design reasoning into working interface behavior. The tasks progress from simple workflows, such as a reservation flow where users select a date, choose a time, enter their information, and confirm a booking, to more complex interactive systems that must serve large and diverse user populations.

**ZH** 功能类任务要求生成式 UI 工具创建的界面，其核心挑战在于界面在用户交互过程中如何行为（48）。这些任务关注工具能否实现支持用户走完工作流、遇到错误、改变输入状态、在角色之间导航或使用无障碍功能的交互行为。我们用这些任务研究工具能否把交互设计推理转化为可工作的界面行为。任务从简单的工作流（如预订流程：用户选择日期、选择时间、填写信息并确认预订）逐步推进到必须服务庞大而异质用户群体的更复杂交互系统。

**EN** Within each tier, tasks increase in complexity along four dimensions. First, they vary in the number of user audiences, from interfaces designed for one group to interfaces that must serve multiple groups, such as residents, administrators, and visitors. Second, they vary in the number of competing design requirements, such as balancing simplicity, accessibility, branding, and detailed information. Third, they vary in the depth of domain-specific constraints, such as bilingual content, regulatory requirements, limited device access, or low literacy. Fourth, they vary in the severity of consequences if the design fails, ranging from confusion in a low-stakes website to missed emergency, health, or financial information in a high-stakes interface. This progression allows us to examine whether Design Theater becomes pronounced as design scenarios become more complex.

**ZH** 在每个层级内部，任务沿四个维度递增复杂度。第一是用户受众数量的变化，从面向单一群体设计的界面，到必须服务居民、管理员与访客等多类群体的界面。第二是相互竞争的设计要求数量的变化，例如在简洁性、无障碍性、品牌表达与信息详尽度之间取得平衡。第三是领域特定约束深度的变化，例如双语内容、监管要求、设备访问受限或低识字率。第四是设计失败后果严重程度的变化，从低风险网站中的困惑，到高风险界面中错过紧急、健康或财务信息。这一递进让我们得以考察：随着设计场景变得更复杂，Design Theater 是否变得更加明显。

**EN** Prompting and Generative UI Output Collection

**ZH** 提示与生成式 UI 输出的采集

**EN** We administered the 24 benchmark tasks, eight per tier, to each of the five generative UI tools in our study, producing 120 generated interfaces in total (⟦SLOT_0⟧ tools ⟦SLOT_1⟧ ⟦SLOT_2⟧ tasks). For each tool-task combination, the prompt included the same fixed implementation instruction: the tool had to generate the interface using only HTML, CSS, and JavaScript, without external frameworks, libraries, or web searches. We kept this instruction identical across all tools and tasks so that differences in the generated interfaces would reflect each tool’s interpretation of the task prompt, user-facing design reasoning, and implementation choices, rather than differences in external resources or selected libraries. For each output, we captured the generated code, the rendered interface, and the full user-facing reasoning trace, including design commentary, explanations, and any rationale produced before, during, or alongside code generation.

**ZH** 我们把 24 项基准任务（每个层级 8 项）分别交给研究中的五个生成式 UI 工具，共产出 120 个生成的界面（⟦SLOT_0⟧ 个工具 ⟦SLOT_1⟧ ⟦SLOT_2⟧ 项任务）。对每个工具—任务组合，提示中都包含同一条固定的实现指令：工具必须仅用 HTML、CSS 与 JavaScript 生成界面，不得使用外部框架、库或网页搜索。我们在所有工具与任务之间保持该指令完全一致，以使生成界面之间的差异反映的是每个工具对任务提示的解读、面向用户的设计推理与实现选择，而非外部资源或所选库的差异。对每个输出，我们采集了生成的代码、渲染出的界面，以及完整的面向用户的推理轨迹，包括设计点评、解释，以及在代码生成之前、期间或伴随其产生的任何理由陈述。

**EN** Metric 1: Thinking Fidelity Score (TFS)

**ZH** 指标 1：思维保真度分数（TFS）

**EN** TFS measures the extent to which a generative UI tool’s user-facing design reasoning is reflected in the interface it generates. TFS operationalizes Design Theater by quantifying how much of the concrete design reasoning articulated by the tool is fully, partially, or not implemented in the final interface. In order to calculate this metric, we conduct:

**ZH** TFS 衡量生成式 UI 工具面向用户的设计推理在多大程度上反映在它所生成的界面中。TFS 通过量化工具所阐述的具体设计推理中有多少被完整实现、部分实现或完全未实现，来把 Design Theater 操作化。为计算该指标，我们执行以下步骤：

**EN** 1) Reasoning Element Extraction.

**ZH** 1) 推理要素抽取。

**EN** For each reasoning trace, we extract every concrete and verifiable design reasoning element. A reasoning element must be specific enough to evaluate against the generated interface or code. For example, statements such as “I will use a three-column grid,” “I will include keyboard-navigable tabs,” or “I will add a dark mode toggle” are included. Vague reasoning, such as “I will make the design user-friendly,” is excluded because it cannot be reliably verified against the final interface.

**ZH** 对每条推理轨迹，我们抽取其中每一个具体且可验证的设计推理要素。一个推理要素必须具体到可以对照生成的界面或代码加以评估。例如，「我将使用三栏网格」「我将加入可键盘导航的标签页」或「我将添加一个深色模式开关」这类陈述会被纳入。而「我会让设计对用户友好」这类模糊推理则被排除，因为它无法对照最终界面被可靠地验证。

**EN** 2) Reasoning Verification.

**ZH** 2) 推理验证。

**EN** Two independent evaluators compare each extracted element of user-facing design reasoning against the generated interface. Each reasoning element is classified as Fully Implemented (1.0), Partially Implemented (0.5), or Not Implemented (0.0), depending on the extent to which the stated design reasoning is realized in the implemented interface. Each reasoning element is scored against the generated interface rather than the task prompt. An element is counted as Not Implemented when the interface does not contain what the reasoning described, including cases where the tool implemented a different approach. Whether the interface meets the prompt’s requirements is measured separately by PAS.

**ZH** 两名独立评估者把抽取出的每个面向用户的设计推理要素与生成的界面对照。每个推理要素被归类为完整实现（1.0）、部分实现（0.5）或未实现（0.0），取决于所述的设计推理在已实现界面中被落实的程度。每个推理要素是对照生成的界面、而非任务提示来打分的。当界面并不包含推理所描述的内容时（包括工具采用了另一种做法的情形），该要素记为未实现。界面是否满足提示要求，则由 PAS 单独衡量。

**EN** 3) TFS Metric Computation.

**ZH** 3) TFS 指标计算。

<!-- [原子块 · table] TFS = 1.0 ⋅ N full + 0.5 ⋅ N partial N total \text{TFS}=\frac{1.0\cdot N_{\text{full}}+0.5\cdot N_{\text{partial}}}{N_{\text{total}}} (1) -->

**EN** A lower TFS indicates greater Design Theater because the tool’s user-facing reasoning is less faithfully reflected in the generated interface. TFS measures the size of this gap, not its cause.

**ZH** TFS 越低表明 Design Theater 越严重，因为工具面向用户的推理在生成界面中的反映越不忠实。TFS 衡量的是这一缺口的大小，而非其成因。

**EN** Metric 2: Principle Adherence Score (PAS)

**ZH** 指标 2：原则遵循度分数（PAS）

**EN** PAS measures whether generative UI tools recognize and implement UX principles that are implicitly embedded in the prompt. Whereas TFS evaluates whether tools follow through on their own stated reasoning, PAS evaluates whether tools implement the underlying UX principles required by each prompt within a task (each task has two UX principles). To avoid defining these principles post hoc, we use a framework-first approach: we select UX principles from established HCI and design frameworks before evaluation, and then design each prompt to naturally embed those principles through user needs and contextual constraints. Structural tasks draw from information architecture principles (58), styling tasks draw from visual perception and WCAG-related accessibility principles (35; 76), and functional tasks draw from usability heuristics (48). To calculate PAS, we use:

**ZH** PAS 衡量生成式 UI 工具是否识别并实现了提示中隐式嵌入的 UX 原则。TFS 评估的是工具是否兑现自己所陈述的推理，而 PAS 评估的是工具是否实现了每项任务中提示所要求的底层 UX 原则（每项任务包含两条 UX 原则）。为避免事后定义这些原则，我们采用框架优先的做法：在评估之前先从既有的 HCI 与设计框架中选取 UX 原则，再设计每条提示，使其通过用户需求与情境约束自然地嵌入这些原则。结构类任务取自信息架构原则（58），样式类任务取自视觉感知与 WCAG 相关的无障碍原则（35; 76），功能类任务取自可用性启发式准则（48）。为计算 PAS，我们采用：

**EN** 1) Scoring Protocol.

**ZH** 1) 评分协议。

**EN** Each prompt (task) contains two target UX principles. For each generated interface, two independent evaluators score whether each principle was implemented: 1 if implemented and 0 if not implemented.

**ZH** 每条提示（任务）包含两条目标 UX 原则。对每个生成的界面，两名独立评估者就每条原则是否被实现打分：实现记 1 分，未实现记 0 分。

**EN** 2) PAS Metric Computation.

**ZH** 2) PAS 指标计算。

<!-- [原子块 · table] PAS = ∑ i = 1 2 P i 2 \text{PAS}=\frac{\sum_{i=1}^{2}P_{i}}{2} (2) -->

**EN** where ⟦SLOT_3⟧ indicates whether principle ⟦SLOT_4⟧ is implemented.

**ZH** 其中 ⟦SLOT_3⟧ 表示原则 ⟦SLOT_4⟧ 是否被实现。

**EN** For both TFS and PAS, evaluators first completed their ratings independently. Disagreements were then resolved through discussion, and any remaining unresolved cases were adjudicated by a third evaluator before final metric computation (52; 47). Inter-rater reliability on the independent ratings was substantial for TFS (linearly weighted Cohen’s κ = 0.70; per-tool range 0.53–0.85) and almost perfect for PAS (κ = 0.90; per-tool range 0.75–1.00). Weighted κ is used for TFS because the classification is ordinal, and disagreements were almost entirely adjacent.

**ZH** 对 TFS 与 PAS，评估者先独立完成评分，再通过讨论解决分歧；任何仍未解决的情形在最终指标计算前由第三名评估者裁定（52; 47）。独立评分的评分者间信度对 TFS 而言相当高（线性加权 Cohen's κ = 0.70；各工具区间 0.53–0.85），对 PAS 则接近完美（κ = 0.90；各工具区间 0.75–1.00）。TFS 采用加权 κ，是因为其分类为有序类别，且分歧几乎全部发生在相邻类别之间。

**EN** Metric 3: Design Homogeneity Index (DHI)

**ZH** 指标 3：设计同质化指数（DHI）

**EN** DHI measures design homogenization by examining how similar the generated interfaces are across tools, especially when those tools are given the same task prompt. Because UI similarity is multidimensional (35), we do not collapse DHI into a single aggregate score. Instead, we report DHI as an index composed of three sub-measures that capture different aspects of interface similarity: overall visual appearance, color usage, and layout structure.

**ZH** DHI 通过考察不同工具生成的界面彼此有多相似——尤其是当这些工具接到同一任务提示时——来衡量设计同质化。由于 UI 相似度是多维的（35），我们不把 DHI 压缩为单一的聚合分数，而是把它作为由三个子度量构成的指数来报告，分别刻画界面相似度的不同方面：整体视觉外观、色彩使用与版面结构。

**EN** To calculate DHI, we first render all 120 generated interfaces as standardized 1200 ⟦SLOT_5⟧ 1200 PNG screenshots. For each prompt, we compare the five interfaces generated by the five tools. This yields ten pairwise tool comparisons per prompt for each DHI sub-measure.

**ZH** 为计算 DHI，我们首先把全部 120 个生成的界面渲染为 1200 ⟦SLOT_5⟧ 1200 的标准 PNG 截图。对每条提示，我们比较五个工具生成的五个界面。这为每条提示在每个 DHI 子度量上产生十组成对的工具比较。

**EN** DHI-Visual Similarity.

**ZH** DHI-视觉相似度。

**EN** We encode each screenshot using UIClip and compute pairwise visual similarity across tools for the same prompt (78). This sub-measure captures the overall visual appearance of the interface, including stylistic patterns, component aesthetics, spacing tendencies, and the general visual impression produced by the design.

**ZH** 我们用 UIClip 对每张截图编码，并针对同一提示计算跨工具的成对视觉相似度（78）。该子度量刻画界面的整体视觉外观，包括风格模式、组件观感、间距倾向，以及设计所产生的总体视觉印象。

**EN** DHI-Color Similarity.

**ZH** DHI-色彩相似度。

**EN** We represent each screenshot as a color histogram in CIELCh color space and compute pairwise color distance using Earth Mover’s Distance (80; 59). This submeasure specifically captures how similar the interfaces are in their use of colors, including palettes, color balance, saturation, and color distribution throughout the interface.

**ZH** 我们把每张截图表示为 CIELCh 色彩空间中的颜色直方图，并用 Earth Mover's Distance（推土机距离）计算成对的色彩距离（80; 59）。该子度量专门刻画界面在色彩使用上的相似程度，包括调色板、色彩平衡、饱和度，以及色彩在整个界面中的分布。

**EN** DHI-Layout Similarity.

**ZH** DHI-版面相似度。

**EN** We parse each screenshot using OmniParser v2.0 to detect UI elements, and then compute structural similarity using tree edit distance (46). This submeasure captures how similarly interface components are organized and positioned, including section ordering, navigation placement, grouping of elements, and overall page structure.

**ZH** 我们用 OmniParser v2.0 解析每张截图以检测 UI 元素，再用树编辑距离计算结构相似度（46）。该子度量刻画界面组件在组织与位置上的相似程度，包括章节顺序、导航位置、元素分组与整体页面结构。

**EN** We report each DHI sub-measure separately because visual appearance, color usage, and layout structure can capture distinct dimensions of design homogenization. This allows us to identify not only whether generative UI tools converge, but also where that convergence occurs: in stylistic appearance, color choices, or interface layout organization.

**ZH** 我们分别报告每个 DHI 子度量，因为视觉外观、色彩使用与版面结构可能刻画设计同质化的不同维度。这使我们不仅能识别生成式 UI 工具是否趋同，还能识别趋同发生在何处：是风格外观、色彩选择，还是界面版面组织。

**EN** Results

**ZH** 结果

**EN** Metric 1: Thinking Fidelity Score (TFS)

**ZH** 指标 1：思维保真度分数（TFS）

**EN** Using our TFS metric, we measured the proportion of stated design reasoning that each generative UI tool actually implemented across its generated interfaces.

**ZH** 借助 TFS 指标，我们衡量了每个生成式 UI 工具在其生成的界面中实际实现了多大比例的所述设计推理。

**EN** Figure 1 shows the average TFS scores for each tool across its generated interfaces, while Table 1 in its second column reports the overall TFS results. No tool consistently delivered on its design reasoning, and the cross-tool mean TFS score was 0.75, indicating that roughly one in four stated design rationales did not fully appear in the generated interface. Four tools (Claude, Bolt, ChatGPT, and Vercel v0) clustered between 0.74 and 0.87, suggesting descriptively similar overall performance, with Claude achieving the highest alignment at 0.87. Firebase scored lowest, with a mean TFS of 0.53, below the range observed for the other four tools.

**ZH** 图 1 给出了每个工具在其生成界面上的平均 TFS，表 1 第二列报告了总体 TFS 结果。没有一个工具能始终兑现其设计推理；跨工具 TFS 均值为 0.75，意味着约有四分之一的所述设计理由并未完整出现在生成的界面中。四个工具（Claude、Bolt、ChatGPT 与 Vercel v0）聚集在 0.74 到 0.87 之间，从描述性角度看整体表现相近，其中 Claude 以 0.87 取得最高的对齐度。Firebase 得分最低，TFS 均值为 0.53，低于其余四个工具所处的区间。

<!-- [原子块 · img]  -->

**EN** Figure 1: Overall Thinking Fidelity Score by Tool

**ZH** 图 1：各工具的总体思维保真度分数

<!-- [原子块 · table] Tool Overall Tier 1 Tier 2 Tier 3 Structural Styling Functional Claude 0.87 [0.82, 0.91] 0.83 [0.74, 0.91] 0.93 [0.89, 0.96] 0.85 [0.78, 0.91] Bolt 0.84 [0.75, 0.91] 0.83 [0.70, 0.95] 0.95 [0.90, 0.99 -->

**EN** Table 1: Mean Thinking Fidelity Scores (TFS) by tool and tier. Best score in each column shown in bold.

**ZH** 表 1：按工具与层级划分的平均思维保真度分数（TFS）。每列最佳分数以粗体显示。

<!-- [原子块 · img]  -->

**EN** Figure 2: Thinking Fidelity Score across Tier, by Tools

**ZH** 图 2：按工具划分的各层级思维保真度分数

**EN** Figure 2 and Table 1 show that reasoning-to-implementation fidelity varied across both tools and task tiers. Functional tasks showed the weakest alignment across tools, with a cross-tool mean TFS of 0.66 compared with 0.79 for structural tasks and 0.81 for styling tasks. However, this decline was not uniform across tools. Claude maintained relatively stable fidelity across tiers, scoring 0.83 on structural tasks, 0.93 on styling tasks, and 0.85 on functional tasks. Bolt peaked on styling tasks before declining on functional tasks, while ChatGPT showed a gradual decline from structural to styling to functional tasks. Vercel v0 performed similarly on structural and styling tasks before dropping sharply on functional tasks, and Firebase remained the lowest-performing tool across all tiers. Together, these results suggest that Design Theater is not distributed evenly across task types: for some tools, reasoning-to-implementation gaps are broadly distributed, while for others they are concentrated especially in functional implementation.

**ZH** 图 2 与表 1 显示，推理到实现的保真度在工具与任务层级两个维度上都有变化。功能类任务在各工具中对齐度最弱，跨工具 TFS 均值为 0.66，而结构类任务为 0.79、样式类任务为 0.81。不过这一下降在各工具间并不一致。Claude 在各层级上保持了相对稳定的保真度，结构类任务得分为 0.83、样式类任务为 0.93、功能类任务为 0.85。Bolt 在样式类任务上达到峰值，随后在功能类任务上下降；ChatGPT 则从结构类到样式类再到功能类逐步下滑。Vercel v0 在结构类与样式类任务上表现相近，随后在功能类任务上急剧下滑；Firebase 则在所有层级上都处于最低水平。这些结果共同表明：Design Theater 并非在任务类型间均匀分布——对某些工具而言，推理到实现的缺口广泛分布，而对另一些工具则尤其集中在功能实现上。

**EN** Table 1 also shows that tools differed not only in average fidelity but also in the uncertainty around those estimates. Claude and ChatGPT had the narrowest overall bootstrap confidence intervals, with Claude ranging from 0.82 to 0.91 and ChatGPT from 0.75 to 0.84. In contrast, Vercel v0 and Bolt showed wider intervals, especially for Tier 3 functional tasks. For example, Vercel v0’s Tier 3 mean was 0.56, with a confidence interval from 0.36 to 0.77. This suggests greater variability in how reliably Vercel v0 translated functional design claims into implementation across tasks. In some cases, the tool appeared to follow through on its stated reasoning, while in others, much of the promised functionality was absent or incomplete. These results indicate that mean TFS alone can obscure differences in reliability: a tool with moderate but stable fidelity presents a different risk profile than one whose performance appears more variable across tasks.

**ZH** 表 1 还显示，各工具的差异不仅体现在平均保真度上，也体现在这些估计值周围的不确定性上。Claude 与 ChatGPT 的总体自助法置信区间最窄，Claude 为 0.82 至 0.91，ChatGPT 为 0.75 至 0.84。相比之下，Vercel v0 与 Bolt 的区间更宽，在第三层级的功能类任务上尤为明显。例如，Vercel v0 在第三层级的均值为 0.56，置信区间为 0.36 至 0.77。这说明 Vercel v0 在跨任务地把功能类设计主张转化为实现时的可靠性波动更大：在某些情况下，该工具似乎兑现了其所陈述的推理，而在另一些情况下，许多承诺的功能缺失或不完整。这些结果表明，TFS 均值本身可能掩盖可靠性上的差异：一个保真度中等但稳定的工具，与一个跨任务表现波动更大的工具，呈现出不同的风险画像。

**EN** Overall, from the perspective of a stakeholder reading a tool’s reasoning trace, the practical question is not which tool to trust most, but how any tool’s reasoning should be read as a description of what was actually built.

**ZH** 总体而言，从阅读工具推理轨迹的利益相关方的视角看，实际问题不是该最信任哪个工具，而是任何工具的推理都应被怎样解读——即把它当作对实际构建结果的描述来读。

**EN** Metric 2: Principle Adherence Score (PAS)

**ZH** 指标 2：原则遵循度分数（PAS）

<!-- [原子块 · img]  -->

**EN** Figure 3: Principle Adherence Score across five UI agent tools. Left: mean PAS with 95% confidence intervals. Right: PAS by principle tier, showing consistently poor performance on functional principles

**ZH** 图 3：五个 UI 智能体工具的原则遵循度分数。左：带 95% 置信区间的平均 PAS。右：按原则层级划分的 PAS，显示功能类原则上持续低迷的表现

**EN** Our PAS metric measures whether generative UI tools implement the UX principles implicitly required by each design task. Figure 3 (left) reports the mean PAS for each tool across tasks, while Table 2 in its second column reports these same means with 95% confidence intervals. These intervals capture uncertainty around each tool’s estimated average PAS across benchmark tasks. Overall, tools differed in how well they implemented the embedded UX principles. Mean PAS ranged from 0.29 for Firebase Studio to 0.73 for ChatGPT. In concrete terms, Firebase Studio implemented 14 of the 48 required principles, whereas ChatGPT implemented 35 of 48. Vercel v0 and Claude fell near the middle of the range, implementing only slightly more than half of the embedded UX principles. The non-overlapping 95% bootstrap confidence intervals between the highest- and lowest-performing tools provide descriptive evidence that ChatGPT and Firebase Studio occupied meaningfully different parts of the PAS range.

**ZH** 我们的 PAS 指标衡量生成式 UI 工具是否实现了每项设计任务隐式要求的 UX 原则。图 3（左）报告了各工具跨任务的平均 PAS，表 2 第二列以 95% 置信区间报告了同样的均值。这些区间刻画了各工具在基准任务上 PAS 估计均值周围的不确定性。总体上，各工具在实现所嵌入 UX 原则上的表现存在差异。平均 PAS 从 Firebase Studio 的 0.29 到 ChatGPT 的 0.73 不等。具体而言，Firebase Studio 实现了 48 条所需原则中的 14 条，而 ChatGPT 实现了 35 条。Vercel v0 与 Claude 处于区间中部附近，只实现了略多于一半的嵌入 UX 原则。表现最好与最差工具之间不重叠的 95% 自助法置信区间提供了描述性证据，说明 ChatGPT 与 Firebase Studio 处在 PAS 区间中明显不同的位置。

**EN** Figure 3 (right) reports each tool’s mean PAS across the three task tiers. The clearest pattern is a sharp drop in PAS for functional tasks. Tools implemented structural tasks at relatively high rates, with Tier 1 scores ranging from 0.50 to 0.94, and styling tasks at similarly high rates, with Tier 2 scores ranging from 0.38 to 0.88. By contrast, functional tasks were implemented much less reliably. Four of the five tools scored 0.06 or below on Tier 3, and Firebase Studio implemented none of the functional principles across the eight functional tasks. Even ChatGPT, which scored highest overall, reached only 0.38 on Tier 3, indicating that functionality-related UX principles were the most difficult for these tools to implement. This pattern suggests that current tools share systematic weaknesses in interaction design principles such as visibility of system status, user control and freedom, and error prevention and recovery (i.e., they struggle implementing functional UX principles).

**ZH** 图 3（右）报告了各工具在三个任务层级上的平均 PAS。最清晰的模式是功能类任务上 PAS 的急剧下降。工具在结构类任务上的实现率相对较高，第一层级得分区间为 0.50 至 0.94；样式类任务同样较高，第二层级得分区间为 0.38 至 0.88。相比之下，功能类任务的实现要不可靠得多。五个工具中有四个在第三层级得分不超过 0.06，而 Firebase Studio 在八项功能类任务中没有实现任何一条功能原则。即便总分最高的 ChatGPT，在第三层级也只达到 0.38，说明与功能相关的 UX 原则对这些工具而言最难实现。这一模式表明，当前工具在交互设计原则上存在共同的系统性短板，例如系统状态可见性、用户的控制与自由，以及错误预防与恢复——也就是说，它们难以实现功能类 UX 原则。

<!-- [原子块 · table] Tool Mean PAS [95% CI] Tier 1 Tier 2 Tier 3 ChatGPT 0.73 [0.59, 0.83] 0.94 0.88 0.38 Bolt 0.60 [0.46, 0.73] 0.88 0.88 0.06 Vercel v0 0.56 [0.42, 0.69] 0.81 0.81 0.06 Claude 0.54 [0.40, 0.67] 0.81 0.75 -->

**EN** Table 2: Principle Adherence Score (PAS) comparison across generative UI tools.

**ZH** 表 2：各生成式 UI 工具的原则遵循度分数（PAS）比较。

**EN** Table 2 reports the mean PAS score of each tool overall and separately for each task tier (columns 3–5). Because PAS measures whether a tool successfully implements the UX principles implicitly required by a task, higher PAS scores indicate that the generated interface more fully adheres to the expected UX principles. From Table 2, we observe more variability between tools on structural (Tier 1) and styling (Tier 2) principles. ChatGPT and Bolt consistently achieved the highest PAS scores on these tiers. For example, ChatGPT achieved a mean PAS of 0.94 on structural principles and 0.88 on styling principles. In contrast, Firebase Studio achieved the lower score of 0.50 on structural principles and 0.38 on styling principles. This represents gaps of approximately 0.44 and 0.50 PAS points respectively relative to ChatGPT, indicating larger differences in the extent to which tools implemented these two requested UX principles. By contrast, the differences between tools on functional principles (Tier 3) were much smaller, with PAS scores ranging only from 0.00 to 0.38. However, this narrower range did not indicate similar performance quality across tools. Instead, it reflected a broader collapse in the ability of nearly all tools to implement functional UX principles at all, even when those principles were implicitly required by the task. Four of the five tools achieved Tier 3 PAS scores of only 0.06 or lower, while Firebase Studio failed to implement any functional principles across the Tier 3 tasks.

**ZH** 表 2 报告了各工具的总体平均 PAS 分数，以及按任务层级分开的分数（第 3–5 列）。由于 PAS 衡量的是工具是否成功实现了任务隐式要求的 UX 原则，更高的 PAS 表示该生成界面更完整地遵循了预期的 UX 原则。由表 2 可见，各工具在结构类（第一层级）与样式类（第二层级）原则上的差异更大。ChatGPT 与 Bolt 在这些层级上始终取得最高的 PAS。例如，ChatGPT 在结构类原则上平均 PAS 为 0.94、在样式类原则上为 0.88。相比之下，Firebase Studio 在结构类原则上取得较低的 0.50、在样式类原则上为 0.38。相对 ChatGPT，这分别代表约 0.44 与 0.50 个 PAS 分的差距，说明各工具在实现这两类所要求的 UX 原则上的程度差异更大。相比之下，各工具在功能类原则（第三层级）上的差异要小得多，PAS 分数仅在 0.00 到 0.38 之间。然而，这一更窄的区间并不意味着各工具的表现质量相近；相反，它反映出几乎所有工具在实现功能类 UX 原则上的能力出现了更广泛的崩塌，即便这些原则为任务所隐式要求。五个工具中有四个在第三层级的 PAS 仅为 0.06 或更低，而 Firebase Studio 在第三层级任务中没有实现任何功能原则。

**EN** Metric 3: Design Homogeneity Index (DHI)

**ZH** 指标 3：设计同质化指数（DHI）

**EN** Our DHI metric studies how similar the interfaces generated by the different tools are to one another, particularly when the tools receive the same prompt. We examined this similarity across three submetrics: visual similarity, color similarity, and layout similarity.

**ZH** 我们的 DHI 指标研究不同工具生成的界面彼此有多相似，尤其是当这些工具接到同一提示时。我们在三个子度量上考察这种相似度：视觉相似度、色彩相似度与版面相似度。

<!-- [原子块 · img]  -->

**EN** Figure 4: Design Homogeneity Index Heat Map

**ZH** 图 4：设计同质化指数热力图

**EN** Figure 4 visualizes the DHI between pairs of generative UI tools across the three DHI submetrics. Each cell represents the mean distance between the interfaces produced by two tools when given the same prompts, pooled across all three task tiers. Lower values indicate that two tools tended to generate more similar interfaces, while higher values indicate greater divergence in their generated designs. From the heatmap, we observe that similarity patterns varied across submetrics. For example, Claude and Vercel v0 produced the most visually similar interfaces (DHI-Visual = 0.119) and the most similar color palettes (DHI-Color = 20.6), while ChatGPT and Claude produced the most different layouts (DHI-Layout = 0.211). The heatmap highlights how some tools converged toward similar design patterns, whereas others generated interfaces with different visual, color, and layout characteristics.

**ZH** 图 4 可视化了生成式 UI 工具两两之间在三个 DHI 子度量上的 DHI。每个单元格表示两个工具在接到相同提示时所生成界面之间的平均距离（在三个任务层级上合并计算）。数值越低表示两个工具倾向于生成更相似的界面，数值越高表示其生成设计差异更大。从热力图可见，相似模式在各子度量之间有所不同。例如，Claude 与 Vercel v0 生成的界面在视觉上最相似（DHI-Visual = 0.119），配色也最相近（DHI-Color = 20.6），而 ChatGPT 与 Claude 生成的版面差异最大（DHI-Layout = 0.211）。该热力图突出了部分工具如何趋向相似的设计模式，而另一些工具生成的界面则在视觉、色彩与版面特征上各不相同。

**EN** Table 3 summarizes the most and least similar tool pairs for each DHI submetric. Each value represents the mean pairwise distance between the interfaces generated by two tools across the 24 tasks. Lower values indicate that two tools tended to generate more similar interfaces, while higher values indicate greater divergence in the generated designs. From Table 3, we observe that Claude and Vercel v0 consistently produced some of the most similar interfaces, achieving the lowest distances on both visual similarity (0.119) and color similarity (20.6). In contrast, ChatGPT and Firebase produced the most visually different interfaces (0.151), while Bolt and ChatGPT produced the largest differences in color palettes (39.7). For layout similarity, Bolt and Claude generated the most similar layouts (0.181), whereas Claude and ChatGPT produced the most divergent layouts (0.211). The table also shows that the amount of variation differed across submetrics. DHI-Color exhibited the widest range of distances (20.6–39.7), indicating that overall tools varied in their color choices, while DHI-Visual and DHI-Layout showed narrower ranges, suggesting comparatively smaller differences in overall visual appearance and layout organization.

**ZH** 表 3 汇总了每个 DHI 子度量上最相似与最不相似的工具对。每个数值表示两个工具在 24 项任务上生成的界面之间的平均成对距离：数值越低表示两个工具倾向于生成更相似的界面，数值越高表示生成设计的差异更大。由表 3 可见，Claude 与 Vercel v0 持续产出最为相似的界面之一，在视觉相似度（0.119）与色彩相似度（20.6）上都取得最低距离。相比之下，ChatGPT 与 Firebase 生成的界面在视觉上差异最大（0.151），而 Bolt 与 ChatGPT 在配色上差异最大（39.7）。在版面相似度上，Bolt 与 Claude 生成的版面最相近（0.181），而 Claude 与 ChatGPT 生成的版面差异最大（0.211）。该表还显示，不同子度量的变异幅度各不相同。DHI-Color 的距离区间最宽（20.6–39.7），说明各工具在色彩选择上整体差异较大；而 DHI-Visual 与 DHI-Layout 的区间更窄，说明在整体视觉外观与版面组织上的差异相对更小。

<!-- [原子块 · table] Sub-metric Most similar pair Least similar pair Range Mean DHI-Visual Claude–v0 (0.119) ChatGPT–Firebase (0.151) 0.119–0.151 0.137 DHI-Color Claude–v0 (20.6) Bolt–ChatGPT (39.7) 20.6–39.7 31.9 DHI-Lay -->

**EN** Table 3: Pairwise tool similarity by sub-metric, averaged across 24 tasks.

**ZH** 表 3：按子度量划分的工具间成对相似度，在 24 项任务上取平均。

**EN** Discussion

**ZH** 讨论

**EN** Democratizing UI Generation Without Democratizing Evaluation

**ZH** 界面生成的民主化并未带来评估的民主化

**EN** Generative UI tools are often framed as democratizing design because they allow non-designers to rapidly prototype and generate functional interfaces from natural language (66; 12; 83). Yet this democratization also redistributes design labor. Activities that were once mediated by trained designers, such as prototyping, design justification, or preliminary design evaluation, are increasingly being taken up by product managers, clients, and other non-design stakeholders. This shift creates new challenges around evaluation of the designs. Prior work shows that UX practitioners already use generative AI in design workflows (66), but also report a need for better training to assess the quality of the interfaces. For novice users, this problem is even more pronounced: they may be able to generate an interface, but lack the expertise to judge whether it reflects their goals, satisfies requirements, or follows sound UX principles. The challenge becomes more consequential when generative UI tools also provide user-facing explanations of what was designed and why (64). By articulating layout decisions, invoking design principles, and describing tradeoffs in the language of trained designers (61), these systems can appear to perform design expertise on the user’s behalf. This may lead novice users to perceive generated interfaces as more complete, intentional, or correct than they actually are. In this way, generative UI tools can create a false sense of expertise: users may feel confident that an interface satisfies their design needs, but only because they lack the training to recognize usability problems, missing requirements, or flawed design assumptions.

**ZH** 生成式 UI 工具常被描述为在推进设计的民主化，因为它们让非设计师能够从自然语言快速原型化并生成可用的界面（66; 12; 83）。然而这种民主化也重新分配了设计劳动。曾经由受过训练的设计师所中介的活动——原型设计、设计论证或初步设计评估——正越来越多地由产品经理、客户与其他非设计背景的利益相关方承担。这一转变在设计的评估上带来了新挑战。先前工作表明，UX 从业者已经在设计工作流中使用生成式 AI（66），但也报告需要更好的培训来评估界面质量。对新手用户而言，这一问题更为突出：他们或许能生成界面，却缺乏判断它是否反映自身目标、满足要求或遵循合理 UX 原则的专业能力。当生成式 UI 工具还提供关于设计了什么、为何这样设计的面向用户的解释时，挑战变得更为紧要（64）。通过阐述版面决策、援引设计原则，并以受过训练的设计师的语言描述权衡（61），这些系统看起来是在代用户行使设计专业能力。这可能让新手用户觉得生成的界面比实际更完整、更有意图、更正确。如此一来，生成式 UI 工具会制造出一种虚假的专业感：用户可能对界面满足其设计需求充满信心，仅仅因为他们缺乏识别可用性问题、缺失需求或有缺陷设计假设的训练。

**EN** Across our evaluation, roughly one in four stated design rationales did not fully appear in the generated interface. This gap became especially pronounced for functional tasks, where tools achieved a Tier 3 TFS of 0.66. The PAS results were even more striking. Recall that PAS measured whether generative UI tools implemented the UX principles implicitly required by each task. On functional UX principles, four of the five tools scored ⟦SLOT_6⟧, meaning they implemented almost none of the interaction-design requirements embedded in the tasks, such as visibility of system status, user control and freedom, error prevention, and recovery. These functional failures are also the hardest for non-experts to detect. A missing color choice or layout inconsistency is often visible in the rendered interface. By contrast, missing state management, inaccessible interactions, weak error recovery, or absent user control may not be obvious from surface-level inspection. Thus, the most consequential failures are often the least visible, while the non-expert designers now responsible for evaluating generated interfaces may be the least equipped to identify these errors (66).

**ZH** 在我们的评估中，约有四分之一的所述设计理由并未完整出现在生成的界面中。这一缺口在功能类任务上尤为明显——工具在第三层级的 TFS 为 0.66。PAS 结果更为触目。回顾一下，PAS 衡量的是生成式 UI 工具是否实现了每项任务隐式要求的 UX 原则。在功能类 UX 原则上，五个工具中有四个得分为 ⟦SLOT_6⟧，意味着它们几乎没有实现任务中嵌入的交互设计要求，如系统状态可见性、用户的控制与自由、错误预防与恢复。这些功能上的失败也正是非专业者最难察觉的。缺失的色彩选择或版面不一致往往在渲染出的界面中一眼可见；相比之下，缺失的状态管理、不可用的交互、薄弱的错误恢复或缺失的用户控制，从表层检视中未必明显。因此，后果最严重的失败往往最不可见，而如今负责评估生成界面的非专业设计者，恰恰可能是最没有能力识别这些错误的人（66）。

**EN** Design evaluation depends on professional judgment developed through practice (40). This expertise is tacit, comparative, and built through repeated exposure to critique (6; 27). It does not transfer to non-experts simply because interface generation has become faster or more fluent. In fact, the ability to recognize when a design rationale sounds convincing but the interface does not behave correctly is precisely what may be lost when trained designers are removed from the loop (66). In this context, user-facing reasoning traces can begin to function like design documentation, but without the accountability structures that traditionally make such documentation meaningful. Prior work shows that users adjust their trust based on how rationales are presented, even when the underlying decision remains unchanged (64; 8). The central risk, then, is not simply that non-designers are using design tools. Rather, it is that the ease of generating interfaces may create a sense of competence in evaluating design decisions, even when users lack the expertise needed to distinguish sound design choices from hollow or problematic ones.

**ZH** 设计评估依赖于在实践中形成的专业判断（40）。这种专业能力是默会的、比较性的，并通过反复接受批评而建立（6; 27）。它不会因为界面生成变得更快、更流畅就转移给非专业者。事实上，当受过训练的设计师被移出环路时，恰恰可能失去的正是这种能力——识别「设计理由听起来令人信服、界面行为却并不正确」的能力（66）。在这一语境下，面向用户的推理轨迹可能开始充当设计文档，却不具备传统上使这类文档有意义的问责结构。先前工作表明，用户会根据理由的呈现方式调整信任，即便底层决策并未改变（64; 8）。因此，核心风险并不只是非设计师在使用设计工具，而在于：生成界面的便捷可能营造出一种「自己有能力评估设计决策」的感觉，即便用户并不具备区分合理设计选择与空洞或有问题设计所需的专业知识。

**EN** The Evaluation Bottleneck in Generative UI

**ZH** 生成式 UI 中的评估瓶颈

**EN** Our findings point to a broader evaluation bottleneck in generative UI workflows. Generative UI tools make interface production faster, cheaper, and rhetorically polished, but evaluating the resulting artifact remains slow, expert-dependent, and multidimensional. A generated interface cannot be assessed only by whether it renders or whether the accompanying rationale sounds plausible. It must be evaluated as an artifact that combines design principles like visual hierarchy, interaction flow, accessibility, responsiveness, and contextual fit. Prior work on generative AI evaluation has warned that static and model-centric evaluations often miss modality, context, deployment conditions, and downstream harms (56). In our study, this gap appears as a reasoning-to-artifact mismatch: generative UI tools can produce a professional-looking interface and a persuasive explanation in seconds, while the work of verifying whether the explanation is actually implemented remains externalized to users (29). Design Theater is therefore not only a failure of generation, but also a failure to produce artifacts that can be easily evaluated (21).

**ZH** 我们的发现指向生成式 UI 工作流中一个更广泛的评估瓶颈。生成式 UI 工具让界面生产更快、更廉价、修辞上更精美，但对最终产物的评估仍然缓慢、依赖专家且多维。一个生成的界面不能仅凭它能否渲染、或伴随的理由是否听起来合理来评判；它必须作为一个融合了视觉层次、交互流程、无障碍性、响应式与情境契合等设计原则的产物被评估。关于生成式 AI 评估的先前工作已警告：静态、以模型为中心的评估常常遗漏模态、语境、部署条件与下游危害（56）。在我们的研究中，这一缺口表现为推理到产物的错位：生成式 UI 工具能在数秒内产出一个看起来专业的界面与一段有说服力的解释，而验证该解释是否真正被实现的工作，仍被外部化给用户（29）。因此，Design Theater 不只是生成的失败，也是未能产出易于评估的产物（21）。

**EN** Our benchmark responds to this evaluation bottleneck by making three aspects of generated UI artifacts auditable. TFS evaluates whether an artifact implements the tool’s design rationale. PAS evaluates whether an artifact satisfies UX principles implied by the prompt. DHI evaluates whether tools converge toward similar visual, color, and layout defaults despite presenting their outputs as situated design choices. Together, these metrics do not claim to measure interface quality in full. Instead, following prior work that emphasizes construct clarity in AI measurement (9), we treat TFS, PAS, and DHI as targeted instruments for detecting three failure modes: unimplemented design rationales, missed implicit UX principles, and homogenized design defaults. We therefore position the benchmark not as a final ranking of generative UI tools, but as a reusable evaluation framework for asking whether user-facing design reasoning is grounded in implementation.

**ZH** 我们的基准通过让生成 UI 产物的三个方面变得可审计，来回应这一评估瓶颈：TFS 评估产物是否实现了工具的设计理由；PAS 评估产物是否满足提示所隐含的 UX 原则；DHI 评估各工具是否趋向相似的视觉、色彩与版面默认值，即便它们把自己的输出呈现为情境化的设计选择。这些指标合起来并不声称完整衡量了界面质量。相反，遵循强调 AI 测量中构念清晰性的先前工作（9），我们把 TFS、PAS 与 DHI 当作检测三类失效模式的针对性工具：未实现的设计理由、被遗漏的隐式 UX 原则，以及同质化的设计默认值。因此，我们把这个基准定位为可复用的评估框架，用于追问面向用户的设计推理是否扎根于实现，而非对生成式 UI 工具的最终排名。

**EN** Design Homogenization and the Loss of Situated Design

**ZH** 设计同质化与情境化设计的丧失

**EN** Our DHI results suggest that Design Theater is not only a problem of missing implementation but also of reduced variation in generated UI artifacts. Prior work has shown that AI-assisted creation can narrow the diversity of results in writing and ideation (1; 72). In generative UI, homogenization is not only an output-level pattern; it is an accountability problem because similar artifacts arrive with rationales that frame them as context-sensitive design decisions (29). Interfaces are not only expressive artifacts; they organize attention, access, trust, navigation, and user action. This matters because design knowledge is situated: what counts as clear, trustworthy, accessible, or safe depends on the users, institutions, communities, and power relations a design is meant to serve (16). When different users, domains, and stakes are repeatedly translated into similar visual and structural patterns, while being described as tailored design choices, generative systems risk flattening the contextual differences that design work is meant to preserve. This produces surface-level contextualization: the rationale names the audience, domain, or constraint, making the interface appear tailored, even when the rendered artifact relies on familiar defaults (69; 64). Convergence therefore carries stakes beyond aesthetics: when interfaces repeat the same patterns, they standardize where users look (35), how they navigate and interact (48), and who is included or excluded by design decisions (16). When generated interfaces cluster visually or structurally while being presented as situated design responses, generative UI risks making repeated conventions appear unique and professionally validated.

**ZH** 我们的 DHI 结果表明，Design Theater 不只是实现缺失的问题，也是生成 UI 产物变异减少的问题。先前工作已表明，AI 辅助创作会收窄写作与构思结果的多样性（1; 72）。在生成式 UI 中，同质化不只是输出层面的模式，它还是一个问责问题，因为相似的产物会附带把它们框定为情境敏感设计决策的理由（29）。界面不只是表达性产物，它们组织注意、访问、信任、导航与用户行动。这一点事关紧要，因为设计知识是情境化的：什么算清晰、可信、可访问或安全，取决于设计所服务的用户、机构、社群与权力关系（16）。当不同的用户、领域与风险被反复翻译成相似的视觉与结构模式，同时又被描述为量身定制的设计选择时，生成式系统就有可能抹平设计工作本应保留的情境差异。这就产生了表层情境化：理由点名了受众、领域或约束，使界面看起来是量身定制的，即便渲染出的产物依赖的是熟悉的默认值（69; 64）。因此，趋同的影响超出美学范畴：当界面重复相同的模式，它们就在标准化用户看哪里（35）、如何导航与交互（48），以及设计决策把谁纳入、把谁排除（16）。当生成的界面在视觉或结构上聚集、同时又被呈现为情境化的设计回应时，生成式 UI 就有风险让重复的惯例显得独特且经过专业验证。

**EN** Our DHI metric does not by itself determine whether a particular similarity is harmful, useful, or contextually appropriate. Rather, it makes visible when generated interfaces converge despite rationales that describe them as tailored to specific users and contexts. This allows us to ask whether AI-generated interfaces reflect meaningful adaptation to context or the repetition of dominant design defaults. Without design review, stakeholders may read a polished explanation as evidence that a generic interface has been meaningfully tailored (38; 64).

**ZH** 我们的 DHI 指标本身并不能判定某一种相似是有害的、有用的还是情境上恰当的。它所能做的是让「生成的界面在理由声称其为特定用户与情境量身定制的情况下仍然趋同」这一点变得可见。这使我们得以追问：AI 生成的界面反映的是对情境的有意义适配，还是对主流设计默认值的重复。若没有设计评审，利益相关方可能把一段精美的解释当作「一个通用界面已被有意义地定制」的证据（38; 64）。

**EN** Limitations and Future Work

**ZH** 局限性与未来工作

**EN** Our evaluation is artifact-centered. We inspect prompts, user-facing rationales, and rendered interfaces, but do not measure how designers, product managers, engineers, clients, or novice creators interpret these rationales. Our study therefore establishes that rationale-to-artifact mismatch exists, but not how often stakeholders detect it or how it affects trust, review, and deployment decisions. We evaluate Design Theater across five generative UI tools, enabling systematic comparison across tools, tiers, and metrics, but this scope should not be interpreted as an exhaustive account of generative UI behavior. These systems evolve rapidly, and outputs may vary across model versions, interface defaults, and repeated generations. Our benchmark required tools to generate interfaces using only HTML, CSS, and JavaScript, improving comparability while excluding component libraries used by some tools. Because tools were evaluated only against commitments they chose to make, this constraint does not explain TFS results. It may, however, affect PAS, where implementing functional principles without libraries requires additional effort, and DHI, where shared constraints may reduce output variation. Our metrics capture specific dimensions of Design Theater rather than overall design quality. TFS measures whether rationales are implemented, PAS measures whether selected implicit UX principles are recognized and implemented, and DHI measures visual, color, and layout convergence across tools. DHI also lacks a human-designed reference distribution, meaning our results describe convergence among the evaluated tools rather than deviation from human practice. These metrics do not capture aesthetic judgment, cultural fit, emotional resonance, accessibility in lived use, or user success in deployed contexts. Future work should extend this evaluation to additional tools, repeated samples, multi-screen flows, mobile interfaces, multi-turn workflows, accessibility audits, usability testing, participatory evaluation, and multilingual or culturally situated scenarios.

**ZH** 我们的评估以产物为中心。我们检视提示、面向用户的理由与渲染出的界面，但不衡量设计师、产品经理、工程师、客户或新手创作者如何解读这些理由。因此，我们的研究确立了「理由到产物错位确实存在」，却没有说明利益相关方多常发现它，或它如何影响信任、评审与部署决策。我们在五个生成式 UI 工具上评估 Design Theater，从而能够跨工具、跨层级、跨指标做系统比较，但这一范围不应被解读为对生成式 UI 行为的穷尽描述。这些系统演进迅速，输出可能随模型版本、界面默认值与重复生成而变化。我们的基准要求工具仅用 HTML、CSS 与 JavaScript 生成界面，这提升了可比性，同时排除了部分工具所使用的组件库。由于工具只对照它们自己选择做出的承诺被评估，这一约束并不能解释 TFS 的结果；但它可能影响 PAS——在不使用库的情况下实现功能类原则需要额外投入——以及 DHI——共享的约束可能减少输出变异。我们的指标捕捉的是 Design Theater 的特定维度，而非整体设计质量：TFS 衡量理由是否被实现，PAS 衡量所选的隐式 UX 原则是否被识别与实现，DHI 衡量跨工具在视觉、色彩与版面上的趋同。DHI 还缺少一个人类设计的参照分布，这意味着我们的结果描述的是所评估工具之间的趋同，而非相对人类实践的偏离。这些指标并不捕捉审美判断、文化契合、情感共鸣、真实使用中的无障碍性，或部署情境下的用户成效。未来工作应把该评估拓展到更多工具、重复采样、多屏流程、移动端界面、多轮工作流、无障碍审计、可用性测试、参与式评估，以及多语言或文化情境化的场景。

**EN** Conclusion

**ZH** 结论

**EN** Generative UI tools produce user-facing design rationales alongside generated interfaces, but whether these rationales reflect implementations remains unexamined. We introduce Design Theater to characterize this gap and propose a benchmark with three metrics: Thinking Fidelity Score, Principle Adherence Score, and Design Homogeneity Index. Across designs from five state-of-the-art tools, we identify three patterns. First, roughly one in four design rationales fails to appear in the generated interface. Second, tools recognize only about half of the UX principles required by their tasks, with near-universal failures on functional principles such as visibility of system status, user control and freedom, and error prevention and recovery. Third, generated interfaces converge across tools, showing narrow differences in visual appearance and layout organization, while color choices vary more widely. As reasoning traces become a primary signal of design competence for non-expert reviewers, measuring the gap between what tools say and what they build is critical for responsible deployment of generative UI tools.

**ZH** 生成式 UI 工具在生成界面的同时产出面向用户的设计理由，但这些理由是否反映实现仍未得到检验。我们提出 Design Theater 来刻画这一缺口，并提出一个带三项指标的基准：思维保真度分数、原则遵循度分数与设计同质化指数。在五个当前最先进工具的设计上，我们识别出三种模式。第一，约有四分之一的设计理由未能出现在生成的界面中。第二，工具只识别出任务所要求的大约一半 UX 原则，并在系统状态可见性、用户的控制与自由、错误预防与恢复等功能类原则上近乎普遍失败。第三，生成的界面在工具之间趋同，视觉外观与版面组织差异很小，而色彩选择差异更大。随着推理轨迹成为非专业评审者判断设计能力的主要信号，衡量工具「所说」与「所建」之间的缺口，对负责任地部署生成式 UI 工具至关重要。

**EN** Acknowledgments

**ZH** 致谢

**EN** Special thanks to the anonymous reviewers for their feedback. This work was partially supported by NSF grants 2339443 and 2403252. We used Claude Sonnet 4.6 and Grammarly to refine language and clarity under full author oversight; all study design, analysis, literature review, and writing were conducted and verified by the authors.

**ZH** 特别感谢匿名评审者的反馈。本工作得到 NSF 资助 2339443 与 2403252 的部分支持。我们在作者的全程监督下使用 Claude Sonnet 4.6 与 Grammarly 来打磨语言与清晰度；所有研究设计、分析、文献综述与写作均由作者完成并核实。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] Agarwal et al. (2025) D. Agarwal, M. Naaman, and A. Vashistha AI suggestions homogenize writing toward western styles and diminish cultural nuances . In Proceedings of the 2025 CHI Conference on Human -->

<!-- [原子块 · verbatim] Anderson et al. (2024) B. R. Anderson, J. H. Shah, and M. Kreminski Homogenization effects of large language models on human creative ideation . In Proceedings of the 16th conference on creativity & c -->

<!-- [原子块 · verbatim] Anthropic (2025) Anthropic Claude code: agentic coding system . Note: https://www.anthropic.com/product/claude-code Cited by: Vibe Coding and AI-Assisted Co-Creation . -->

<!-- [原子块 · verbatim] Anthropic (2026) Anthropic What are artifacts and how do i use them? . Note: https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them Accessed: 2026-05-19 Cited by: Intr -->

<!-- [原子块 · verbatim] Apple Inc. (2023) Apple Inc. Human interface guidelines . Note: https://developer.apple.com/design/human-interface-guidelines Cited by: Automated Design Evaluation and UX Metrics . -->

<!-- [原子块 · verbatim] Bardzell et al. (2014) J. Bardzell, S. Bardzell, and E. Stolterman Reading critical designs: supporting reasoned interpretations of critical design . In Proceedings of the SIGCHI Conference on Human F -->

<!-- [原子块 · verbatim] Beltramelli (2018) T. Beltramelli Pix2code: generating code from a graphical user interface screenshot . In Proceedings of the ACM SIGCHI Symposium on Engineering Interactive Computing Systems , EICS  -->

<!-- [原子块 · verbatim] Bertrand et al. (2022) A. Bertrand, R. Belloum, J. R. Eagan, and W. Maxwell How cognitive biases affect xai-assisted decision-making: a systematic review . In Proceedings of the 2022 AAAI/ACM Conferen -->

<!-- [原子块 · verbatim] Bommasani and Liang (2024) R. Bommasani and P. Liang Trustworthy social bias measurement . In Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society , Vol. 7 , pp. 210–224 . Cited by: The E -->

<!-- [原子块 · verbatim] Brooke et al. (1996) J. Brooke et al. SUS-a quick and dirty usability scale . Usability evaluation in industry 189 ( 194 ), pp. 4–7 . Cited by: Automated Design Evaluation and UX Metrics . -->

<!-- [原子块 · verbatim] Chen et al. (2021) M. Chen, J. Tworek, H. Jun, Q. Yuan, H. P. de Oliveira Pinto, J. Kaplan, H. Edwards, Y. Burda, N. Joseph, G. Brockman, A. Ray, R. Puri, G. Krueger, M. Petrov, H. Khlaaf, G. Sastry,  -->

<!-- [原子块 · verbatim] Chen et al. (2025a) X. Chen, T. Knearem, and Y. Li The genui study: exploring the design of generative ui tools to support ux practitioners and beyond . In Proceedings of the 2025 ACM Designing Intera -->

<!-- [原子块 · verbatim] Chen et al. (2025b) Y. Chen, J. Benton, C. Anil, N. Elhage, T. Nguyen, J. Esin, C. Olsson, T. Henighan, R. Grosse, et al. Reasoning models don’t always say what they think . Anthropic Research . Exter -->

<!-- [原子块 · verbatim] Chrome (2024) G. Chrome Lighthouse: automated auditing, performance metrics, and best practices . Note: https://github.com/GoogleChrome/lighthouse Cited by: Automated Design Evaluation and UX Metrics  -->

<!-- [原子块 · verbatim] Chung et al. (2022) J. J. Y. Chung, W. Kim, K. M. Yoo, H. Lee, E. Adar, and M. Chang TaleBrush: sketching stories with generative pretrained language models . In Proceedings of the 2022 CHI Conference -->

<!-- [原子块 · verbatim] Costanza-Chock (2020) S. Costanza-Chock Design justice: community-led practices to build the worlds we need . MIT press . Cited by: Automated Design Evaluation and UX Metrics , Design Homogenization a -->

<!-- [原子块 · verbatim] Dev (2025) Lovable: ai-powered full-stack application generator External Links: Link Cited by: From Design Templates to Generative UI Tools . -->

<!-- [原子块 · verbatim] Doshi and Hauser (2024) A. R. Doshi and O. P. Hauser Generative ai enhances individual creativity but reduces the collective diversity of novel content . Science advances 10 ( 28 ), pp. eadn5290 . Cit -->

<!-- [原子块 · verbatim] Duan et al. (2024) P. Duan, C. Cheng, G. Li, B. Hartmann, and Y. Li UICrit: enhancing automated design evaluation with a ui critique dataset . In Proceedings of the 37th Annual ACM Symposium on User I -->

<!-- [原子块 · verbatim] Ehn (2017) P. Ehn Scandinavian design: on participation and skill . In Participatory design , pp. 41–77 . Cited by: Automated Design Evaluation and UX Metrics . -->

<!-- [原子块 · verbatim] Eriksson et al. (2025) M. Eriksson, E. Purificato, A. Noroozian, J. Vinagre, G. Chaslot, E. Gomez, and D. Fernandez-Llorca Can we trust ai benchmarks? an interdisciplinary review of current issues in  -->

<!-- [原子块 · verbatim] Fawzy et al. (2025) A. Fawzy, A. Tahir, and K. Blincoe Vibe coding in practice: motivations, challenges, and a future outlook – a grey literature review . External Links: 2510.00328 , Link Cited by: V -->

<!-- [原子块 · verbatim] Fu et al. (2025) Y. Fu, P. Liang, A. Tahir, Z. Li, M. Shahin, J. Yu, and J. Chen Security weaknesses of copilot-generated code in github projects: an empirical study . ACM Trans. Softw. Eng. Methodol. -->

<!-- [原子块 · verbatim] GitHub (2021) GitHub GitHub copilot: your ai pair programmer . Note: https://github.com/features/copilotAccessed: 2026-04-14 Cited by: Vibe Coding and AI-Assisted Co-Creation . -->

<!-- [原子块 · verbatim] Google (2026) Google Firebase studio . Note: https://firebase.google.com/docs/studio Accessed: 2026-05-19 Cited by: Introduction , Generative UI Tools . -->

<!-- [原子块 · verbatim] Goree et al. (2021) S. Goree, B. Doosti, D. Crandall, and N. M. Su Investigating the homogenization of web design: a mixed-methods approach . In Proceedings of the 2021 CHI conference on human factors -->

<!-- [原子块 · verbatim] Haraway (2013) D. Haraway Situated knowledges: the science question in feminism and the privilege of partial perspective 1 . In Women, science, and technology , pp. 455–472 . Cited by: Automated Desig -->

<!-- [原子块 · verbatim] Hart (2006) S. G. Hart NASA-task load index (nasa-tlx); 20 years later . In Proceedings of the human factors and ergonomics society annual meeting , Vol. 50 , pp. 904–908 . Cited by: Automated Design  -->

<!-- [原子块 · verbatim] Ibrahim et al. (2025) L. Ibrahim, S. Huang, L. Ahmad, U. Bhatt, and M. Anderljung Towards interactive evaluations for interaction harms in human-ai systems . In Proceedings of the AAAI/ACM Conference  -->

<!-- [原子块 · verbatim] Imteyaz et al. (2026) K. Imteyaz, M. Muller, C. Flores-Saviaga, and S. Savage Co-designing collaborative generative ai tools for freelancers . In Proceedings of the 2026 CHI Conference on Human Factor -->

<!-- [原子块 · verbatim] Inc. (2024) A. Inc. Cursor: the ai code editor . Note: https://www.cursor.com/ Cited by: Vibe Coding and AI-Assisted Co-Creation . -->

<!-- [原子块 · verbatim] Inc. (2026) V. Inc. V0: generative ui by vercel . External Links: Link Cited by: From Design Templates to Generative UI Tools . -->

<!-- [原子块 · verbatim] Jain et al. (2019) V. Jain, P. Agrawal, S. Banga, R. Kapoor, and S. Gulyani Sketch2Code: transformation of sketches to ui in real-time using deep neural network . arXiv preprint arXiv:1910.08930 . Cit -->

<!-- [原子块 · verbatim] Ji et al. (2023) Z. Ji, N. Lee, R. Frieske, T. Yu, D. Su, Y. Xu, E. Ishii, Y. J. Bang, A. Madotto, and P. Fung Survey of hallucination in natural language generation . ACM computing surveys 55 ( 12 ), -->

<!-- [原子块 · verbatim] Jiang et al. (2023) Y. Jiang, L. A. Leiva, H. Rezazadegan Tavakoli, P. R. B. Houssel, J. Kylmälä, and A. Oulasvirta UEyes: understanding visual saliency across user interface types . In Proceedings of -->

<!-- [原子块 · verbatim] Jiang et al. (2024) Y. Jiang, Y. Lu, T. Knearem, C. E. Kliman-Silver, C. Lutteroth, T. J. Li, J. Nichols, and W. Stuerzlinger Computational methodologies for understanding, automating, and evaluating  -->

<!-- [原子块 · verbatim] Karen and Sandra (2017) H. Karen and J. Sandra Contextual inquiry: a participatory technique for system design . In Participatory design , pp. 177–210 . Cited by: Automated Design Evaluation and UX Me -->

<!-- [原子块 · verbatim] Kaur et al. (2020) H. Kaur, H. Nori, S. Jenkins, R. Caruana, H. Wallach, and J. Wortman Vaughan Interpreting interpretability: understanding data scientists’ use of interpretability tools for machine  -->

<!-- [原子块 · verbatim] Kojima et al. (2022) T. Kojima, S. S. Gu, M. Reid, Y. Matsuo, and Y. Iwasawa Large language models are zero-shot reasoners . Advances in neural information processing systems 35 , pp. 22199–22213 . Ci -->

<!-- [原子块 · verbatim] Koskinen et al. (2011) I. Koskinen, J. Zimmerman, T. Binder, J. Redström, and S. Wensveen Design research through practice: from the lab, field, and showroom . Elsevier . Cited by: Democratizing UI Ge -->

<!-- [原子块 · verbatim] Lanham et al. (2023) T. Lanham, A. Chen, A. Radhakrishnan, B. Steiner, C. Denison, D. Hernandez, D. Li, E. Durmus, E. Hubinger, J. Kernion, et al. Measuring faithfulness in chain-of-thought reasoning  -->

<!-- [原子块 · verbatim] Lee et al. (2020) C. Lee, S. Kim, D. Han, H. Yang, Y. Park, B. C. Kwon, and S. Ko GUIComp: a gui design assistant with real-time, multi-faceted feedback . In Proceedings of the 2020 CHI Conference on  -->

<!-- [原子块 · verbatim] Li et al. (2026) J. Li, Y. Hou, L. Lin, R. Zhu, H. Cao, and A. El Ali Vibe coding in product teams: reconfiguring ai-assisted workflows, prototyping, and collaboration . In Proceedings of the 5th Annu -->

<!-- [原子块 · verbatim] Liao and Sundar (2022) Q. V. Liao and S. S. Sundar Designing for responsible trust in ai systems: a communication perspective . In Proceedings of the 2022 ACM conference on fairness, accountability, a -->

<!-- [原子块 · verbatim] Liu et al. (2024) V. Liu, R. H. Kazi, L. Wei, M. Fisher, T. Langlois, S. Walker, and L. Chilton Logomotion: visually grounded code generation for content-aware animation . arXiv preprint arXiv:2405.07 -->

<!-- [原子块 · verbatim] Lu et al. (2024) Y. Lu, J. Yang, Y. Shen, and A. Awadallah Omniparser for pure vision based gui agent . arXiv preprint arXiv:2408.00203 . Cited by: DHI-Layout Similarity. . -->

<!-- [原子块 · verbatim] McDonald et al. (2019) N. McDonald, S. Schoenebeck, and A. Forte Reliability and inter-rater reliability in qualitative research: norms and guidelines for cscw and hci practice . Proceedings of the AC -->

<!-- [原子块 · verbatim] Nielsen (1994) J. Nielsen Usability inspection methods . In Conference companion on Human factors in computing systems , pp. 413–414 . Cited by: Introduction , Automated Design Evaluation and UX Metri -->

<!-- [原子块 · verbatim] OpenAI (2024) OpenAI Introducing canvas . Note: https://openai.com/index/introducing-canvas/ Accessed: 2026-05-19 Cited by: Introduction , Generative UI Tools . -->

<!-- [原子块 · verbatim] OpenAI (2025) OpenAI Codex . Note: https://openai.com/index/introducing-codex/ Cited by: Vibe Coding and AI-Assisted Co-Creation . -->

<!-- [原子块 · verbatim] Oulasvirta et al. (2018) A. Oulasvirta, S. De Pascale, J. Koch, T. Langerak, J. Jokinen, K. Todi, M. Laine, M. Kristhombuge, Y. Zhu, A. Miniukovich, G. Palmas, and T. Weinkauf Aalto interface metrics  -->

<!-- [原子块 · verbatim] O’Connor and Joffe (2020) C. O’Connor and H. Joffe Intercoder reliability in qualitative research: debates and practical guidelines . International journal of qualitative methods 19 , pp. 160940691989 -->

<!-- [原子块 · verbatim] Pearce et al. (2025) H. Pearce, B. Ahmad, B. Tan, B. Dolan-Gavitt, and R. Karri Asleep at the keyboard? assessing the security of github copilot’s code contributions . Communications of the ACM 68 ( 2 -->

<!-- [原子块 · verbatim] Peng et al. (2026) K. Peng, J. Nichols, C. Lutteroth, T. Knearem, F. Kretzer, J. P. Bigham, A. Maedche, and Y. Jiang Human-ai-ui interactions across modalities . In Proceedings of the Extended Abstrac -->

<!-- [原子块 · verbatim] Raees (2026) M. Raees Understanding and designing human-centered ai interactions for non-expert users . In Proceedings of the Extended Abstracts of the 2026 CHI Conference on Human Factors in Computin -->

<!-- [原子块 · verbatim] Rauh et al. (2024) M. Rauh, N. Marchal, A. Manzini, L. A. Hendricks, R. Comanescu, C. Akbulut, T. Stepleton, J. Mateos-Garcia, S. Bergman, J. Kay, et al. Gaps in the safety evaluation of generative ai -->

<!-- [原子块 · verbatim] Replit (2026) Inc. Replit Replit: the collaborative browser-based ide . External Links: Link Cited by: From Design Templates to Generative UI Tools . -->

<!-- [原子块 · verbatim] Rosenfeld et al. (2015) L. Rosenfeld, P. Morville, and J. Arango Information architecture: for the web and beyond . ” O’Reilly Media, Inc.” . Cited by: Tier 1: Structural Tasks , Benchmark Design , Me -->

<!-- [原子块 · verbatim] Rubner et al. (2000) Y. Rubner, C. Tomasi, and L. J. Guibas The earth mover’s distance as a metric for image retrieval . International journal of computer vision 40 ( 2 ), pp. 99–121 . Cited by: DHI-C -->

<!-- [原子块 · verbatim] Sarkar and Drosos (2025) A. Sarkar and I. Drosos Vibe coding: programming through conversation with artificial intelligence . External Links: 2506.23253 , Link Cited by: Vibe Coding and AI-Assisted Co -->

<!-- [原子块 · verbatim] Son et al. (2026) K. Son, D. Choi, T. S. Kim, Y. Kim, S. Yun, and J. Kim ClearFairy: capturing creative workflows through decision structuring, in-situ questioning, and rationale inference . In Procee -->

<!-- [原子块 · verbatim] StackBlitz (2026) StackBlitz Introduction to bolt . Note: https://support.bolt.new/building/intro-bolt Accessed: 2026-05-19 Cited by: Introduction , Generative UI Tools . -->

<!-- [原子块 · verbatim] Stone et al. (2005) D. Stone, C. Jarrett, M. Woodroffe, and S. Minocha User interface design and evaluation . Elsevier . Cited by: From Design Templates to Generative UI Tools . -->

<!-- [原子块 · verbatim] Sun et al. (2026) X. Sun, S. Wei, J. A. Bosch, I. Echizen, S. Sugawara, and A. El Ali Seeing the reasoning: how llm rationales influence user trust and decision-making in factual verification tasks .  -->

<!-- [原子块 · verbatim] Systems (2024) D. Systems Axe-core: accessibility testing engine . Note: https://github.com/dequelabs/axe-coreAccessed: 2025-06-01 Cited by: Automated Design Evaluation and UX Metrics . -->

<!-- [原子块 · verbatim] Takaffoli et al. (2024) M. Takaffoli, S. Li, and V. Mäkelä Generative ai in user experience design and research: how do ux practitioners, teams, and companies use genai in industry? . In Proceedings o -->

<!-- [原子块 · verbatim] Tao et al. (2025) S. Tao, I. Liang, C. Peng, Z. Wang, S. Palani, and S. P. Dow DesignWeaver: dimensional scaffolding for text-to-image product design . In Proceedings of the 2025 CHI Conference on Hum -->

<!-- [原子块 · verbatim] Tseng et al. (2024) T. Tseng, R. Cheng, and J. Nichols Keyframer: empowering animation design using large language models . arXiv preprint arXiv:2402.06071 . Cited by: From Design Templates to Generat -->

<!-- [原子块 · verbatim] Turpin et al. (2023) M. Turpin, J. Michael, E. Perez, and S. Bowman Language models don’t always say what they think: unfaithful explanations in chain-of-thought prompting . Advances in Neural Informa -->

<!-- [原子块 · verbatim] Vercel (2023) Vercel Announcing v0: generative ui . Note: https://vercel.com/blog/announcing-v0-generative-ui Accessed: 2026-05-19 Cited by: Introduction , Generative UI Tools . -->

<!-- [原子块 · verbatim] W3C (2024) W3C Web Content Accessibility Guidelines (WCAG) 2.2 . Note: World Wide Web ConsortiumAccessed: 2026-05-04 External Links: Link Cited by: Automated Design Evaluation and UX Metrics . -->

<!-- [原子块 · verbatim] Wadinambiarachchi et al. (2024) S. Wadinambiarachchi, R. M. Kelly, S. Pareek, Q. Zhou, and E. Velloso The effects of generative ai on design fixation and divergent thinking . In Proceedings of the 202 -->

<!-- [原子块 · verbatim] Wang et al. (2022) X. Wang, J. Wei, D. Schuurmans, Q. Le, E. Chi, S. Narang, A. Chowdhery, and D. Zhou Self-consistency improves chain of thought reasoning in language models . arXiv preprint arXiv:22 -->

<!-- [原子块 · verbatim] Wei et al. (2022) J. Wei, X. Wang, D. Schuurmans, M. Bosma, F. Xia, E. Chi, Q. V. Le, D. Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models . Advances in neural informa -->

<!-- [原子块 · verbatim] Wickens et al. (2021) C. D. Wickens, W. S. Helton, J. G. Hollands, and S. Banbury Engineering psychology and human performance . Routledge . Cited by: Automated Design Evaluation and UX Metrics . -->

<!-- [原子块 · verbatim] World Wide Web Consortium (2024) World Wide Web Consortium Web content accessibility guidelines (wcag) 2.2 . W3C Recommendation World Wide Web Consortium (W3C) . Note: Accessed: 2026-05-19 External Li -->

<!-- [原子块 · verbatim] Wu et al. (2023) J. Wu, R. Krosnick, E. Schoop, A. Swearngin, J. P. Bigham, and J. Nichols Never-ending learning of user interfaces . In Proceedings of the 36th Annual ACM Symposium on User Interface  -->

<!-- [原子块 · verbatim] Wu et al. (2024) J. Wu, Y. Peng, X. Y. A. Li, A. Swearngin, J. P. Bigham, and J. Nichols UIClip: a data-driven model for assessing user interface design . In Proceedings of the 37th Annual ACM Symposi -->

<!-- [原子块 · verbatim] Wu et al. (2021) J. Wu, X. Zhang, J. Nichols, and J. P. Bigham Screen parsing: towards reverse engineering of ui models from screenshots . In The 34th Annual ACM Symposium on User Interface Software a -->

<!-- [原子块 · verbatim] Wyszecki and Stiles (2000) G. Wyszecki and W. S. Stiles Color science: concepts and methods, quantitative data and formulae . John wiley & sons . Cited by: DHI-Color Similarity. . -->

<!-- [原子块 · verbatim] Yetiştiren et al. (2023) B. Yetiştiren, I. Özsoy, M. Ayerdem, and E. Tüzün Evaluating the code quality of ai-assisted code generation tools: an empirical study on github copilot, amazon codewhisperer, -->

<!-- [原子块 · verbatim] Zamfirescu-Pereira et al. (2023) J. D. Zamfirescu-Pereira, R. Y. Wong, B. Hartmann, and Q. Yang Why johnny can’t prompt: how non-ai experts try (and fail) to design llm prompts . In Proceedings of the -->

<!-- [原子块 · verbatim] Zhou et al. (2024) Z. Zhou, Y. Li, and J. Yu Exploring the application of llm-based ai in ux design: an empirical case study of chatgpt . Human–Computer Interaction , pp. 1–33 . Cited by: Introduction -->

**EN** Appendix A Appendix

**ZH** 附录 A 附录

**EN** Appendix B Data and Materials Availability

**ZH** 附录 B 数据与材料可用性

**EN** The full evaluation corpus, including the design task prompts, generated UI artifacts, user-facing reasoning traces, and outputs produced by each tool, is publicly available at:

**ZH** 完整的评估语料——包括设计任务提示、生成的 UI 产物、面向用户的推理轨迹以及每个工具的产出——公开获取于：

**EN** https://github.com/kashifimteyaza/design-theater.io

**ZH** https://github.com/kashifimteyaza/design-theater.io

**EN** The underlying models used by the tools during the study included GPT-5 Thinking (ChatGPT), Claude Sonnet 4.5 (Claude and Bolt), Claude Haiku 4.5 (Vercel v0), and Gemini 2.5 Pro (Firebase Studio).

**ZH** 研究期间各工具使用的底层模型包括 GPT-5 Thinking（ChatGPT）、Claude Sonnet 4.5（Claude 与 Bolt）、Claude Haiku 4.5（Vercel v0）与 Gemini 2.5 Pro（Firebase Studio）。
