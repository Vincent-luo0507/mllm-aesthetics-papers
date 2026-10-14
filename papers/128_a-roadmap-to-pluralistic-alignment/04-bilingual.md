# 通向多元对齐的路线图

> 原标题：A Roadmap to Pluralistic Alignment
> 作者：Taylor Sorensen, Jared Moore, Jillian Fisher, Mitchell Gordon, Niloofar Mireshghallah, Christopher Michael Rytting, Andre Ye, Liwei Jiang, Ximing Lu, Nouha Dziri, Tim Althoff, Yejin Choi · arXiv:2402.05070 · 2024-02-07

<!-- [原子块 · verbatim] Position: A Roadmap to Pluralistic Alignment -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] With increased power and prevalence of AI systems, it is ever more critical that AI systems are designed to serve all , i.e., people with diverse values and perspectives. However, aligning models to s -->

**EN** Keywords:

**ZH** 关键词：

<!-- [原子块 · img]  -->

**EN** Figure 1: Three kinds of pluralism in models.

**ZH** 图 1：模型中三种类型的多元性。

**EN** 1 Introduction

**ZH** 1 引言

**EN** AI alignment aims to ensure that a system works with human intentions and values (Leike et al., 2018; Ji et al., 2024; Gabriel, 2020). However, even within a single task or prompt, individual people vary widely in their goals, intentions, and values. As a broader set of people use and rely upon AI systems, we need systems that can understand and cater to a broader set of needs. In other words, we need systems that are pluralistic, or capable of representing a diverse set of human values and perspectives. While many in the community have argued for this (Bai et al., 2022b; Gordon et al., 2022; Sorensen et al., 2023), at least two important questions remain: How, concretely, can a system be pluralistic? and How might benchmarks be designed to measure pluralism?

**ZH** AI 对齐旨在确保系统按照人类的意图与价值观运作（Leike 等，2018；Ji 等，2024；Gabriel，2020）。然而，即便在单一任务或提示之内，个体在目标、意图与价值观上也差异巨大。随着越来越多的人使用并依赖 AI 系统，我们需要能够理解并满足更广泛需求的系统。换言之，我们需要具备多元性的系统，即能够表征多样化的人类价值观与视角的系统。尽管社区中已有许多人对此提出主张（Bai 等，2022b；Gordon 等，2022；Sorensen 等，2023），至少仍有两个重要问题悬而未决：一个系统具体地如何做到多元？以及基准应如何设计以度量多元性？

**EN** In this piece, we advocate for explicit pluralistic considerations in aligning AI systems (§2). In particular, we use large language models (LLMs) as a testbed for alignment (Askell et al., 2021), though we believe the concepts can generalize to other AI systems (§6.3). Because pluralism may look different in different contexts, we formalize three distinct ways of operationalizing pluralism for AI systems/models: 1) providing comprehensive, high-coverage responses (Overton pluralism, §3.1), 2) an ability to be faithfully steered to represent particular attributes (steerable pluralism, §3.2), and 3) distributional representation of a population (distributional pluralism, §3.3). Each form of pluralism has cases where they may be desirable to maximize. We also define three types of pluralistic benchmarks: multi-objective benchmarks (§4.1), benchmarks of models’ steerability across objectives (trade-off steerable benchmarks, §4.2), and benchmarks that explicitly model individuals (jury-pluralistic benchmarks, §4.3). We also outline the situations for which each would be useful.

**ZH** 在这篇文章中，我们主张在 AI 系统对齐中显式考虑多元性（§2）。具体地，我们以大语言模型（LLM）作为对齐的试验场（Askell 等，2021），不过我们相信这些概念可推广到其他 AI 系统（§6.3）。由于多元性在不同语境下可能呈现不同形态，我们形式化了三种在 AI 系统／模型中落实多元性的不同方式：1）提供全面、高覆盖的回答（Overton 多元性，§3.1）；2）能够被忠实引导以表征特定属性的能力（可引导多元性，§3.2）；3）对某个人群的分布化表征（分布多元性，§3.3）。每种多元性形态都有值得最大化的场景。我们还定义了三类多元基准：多目标基准（§4.1）、度量模型在多个目标间可引导性的基准（权衡可引导基准，§4.2），以及显式建模个体的基准（陪审团多元基准，§4.3）。我们也勾勒了各自适用的情形。

**EN** We then discuss the relationship between current alignment approaches and pluralism (§5) and provide initial findings that current alignment techniques reduce distributional pluralism. We advocate and lay out a plan for future work toward pluralistic evaluations and alignment.

**ZH** 随后我们讨论当前对齐方法与多元性之间的关系（§5），并给出初步发现：当前的对齐技术会降低分布多元性。我们倡导面向多元评测与对齐的未来工作，并为其规划了路线。

**EN** 2 Arguments for Pluralism in AI Systems

**ZH** 2 在 AI 系统中支持多元性的理由

**EN** In this section, we argue for the importance of pluralism in aligning AI models.

**ZH** 本节论述在 AI 模型对齐中多元性的重要性。

**EN** Customization necessitates pluralism. Any guardrails placed on AI systems will require customization, within the bounds of those guardrails, to serve diverse use cases and values (Chen et al., 2023; Jang et al., 2023). Pluralism can illuminate the set of values or attributes that users may customize to, and provide an understanding of how well a system can be steered (§3.2, 4.2).

**ZH** 定制化必然要求多元性。给 AI 系统设置的任何护栏，在这些护栏的边界之内都需要定制化，以服务多样的用例与价值观（Chen 等，2023；Jang 等，2023）。多元性能够照亮用户可能定制到的价值观或属性的集合，并提供对系统可被引导程度的认识（§3.2、4.2）。

**EN** Pluralistic systems have technical benefits. Implicit to current preference-based methods like reinforcement learning with human feedback (RLHF) is the assumption that models should fit to the “average” human preference. However, this treats human variation as noise instead of signal (Aroyo et al., 2023; Siththaranjan et al., 2023) – pluralism, however, recognizes this as signal. Modeling pluralism also may increase interpretability by enabling a clearer relationship between decisions and their source (§3.2, 4.2).

**ZH** 多元系统具有技术上的好处。RLHF 等当前基于偏好的方法内含一个假设：模型应当拟合「平均」的人类偏好。然而这把人类差异当作噪声而非信号（Aroyo 等，2023；Siththaranjan 等，2023）——多元性则承认它是信号。对多元性建模还可能提升可解释性，因为它使决策与其来源之间的关系更为清晰（§3.2、4.2）。

**EN** Pluralistic evaluations enable generalist systems. Recently, AI/NLP has trended away from specialist systems and towards generalist systems (foundation models) for use in a diverse set of tasks by a diverse set of users. Yet, current alignment optimizes these generalist systems for a single objective – averaged human preferences. To understand the strengths and weaknesses of these systems, we must measure how they perform across a variety of objectives (§4.1) (Ethayarajh & Jurafsky, 2022) and users (§3.2, 3.3, 4.3).

**ZH** 多元评测成就通用系统。近来，AI／NLP 的趋势是从专用系统转向由多样化用户用于多样化任务的通用系统（基础模型）。然而当前的对齐只针对单一目标——平均化的人类偏好——来优化这些通用系统。要理解这些系统的优势与短板，我们必须度量它们在多种目标（§4.1）（Ethayarajh & Jurafsky，2022）与多种用户（§3.2、3.3、4.3）上的表现。

**EN** Pluralism as a value itself. Many modern societies view accepting competing values and perspectives as a core value in and of itself. Theorists have extolled the benefits of political pluralism (de Tocqueville, 1835; Berlin, 1969; Rawls, 1996), moral and value pluralism (Nagel, 1979; Kekes, 1993; Raz, 1999), and pluralist theories of truth (Wright, 1992; Sher, 1998). While this piece primarily focuses on surfacing differing ideas, perspectives, and values (§3, 4), our scaffolding for technical measurements and implementations of value can also apply to other notions of pluralism. This stands in contrast to current alignment procedures such as RLHF which have been characterized as implementing “preference-based utilitarianism.” (Tasioulas, 2022).

**ZH** 多元性本身即一种价值。许多现代社会把接纳相互竞争的价值观与视角视为一项核心价值。理论家们已阐明政治多元主义（de Tocqueville，1835；Berlin，1969；Rawls，1996）、道德与价值多元主义（Nagel，1979；Kekes，1993；Raz，1999）以及真理的多元主义理论（Wright，1992；Sher，1998）的益处。尽管本文主要关注呈现不同的想法、视角与价值观（§3、4），我们为价值的技术度量与实现搭建的脚手架同样可适用于其他多元性概念。这与 RLHF 等当前对齐程序形成对照，后者被刻画为实现「基于偏好的功利主义」（Tasioulas，2022）。

**EN** AI systems should reflect human diversity. We contend that AI systems should reflect and support the diversity amongst humans and their values, as it is both a feature and a desired quality of human societies (§3.3, 4.3). Exposure to diverse ideas (§3.1) also improves deliberation (Bowman et al., 2022; Landemore & Page, 2015). Furthermore, algorithmic monocultures lead to increased unfairness when applied by many decision makers (Bommasani et al., 2021).

**ZH** AI 系统应反映人类的多样性。我们主张 AI 系统应反映并支持人类及其价值观之间的多样性，因为这既是人类社会的特征，也是其被期许的品质（§3.3、4.3）。接触多样的想法（§3.1）也能改善审议（Bowman 等，2022；Landemore & Page，2015）。此外，当被众多决策者采用时，算法单一化会带来更大的不公（Bommasani 等，2021）。

**EN** 3 Pluralism for AI Models/Systems

**ZH** 3 面向 AI 模型／系统的多元性

**EN** In this section, we formalize three definitions for how a single model or system can be pluralistic. Specifically, we outline Overton pluralism, wherein a model outputs the whole spectrum of reasonable responses; Steerable pluralism, wherein a model is faithfully steered to reflect certain properties or perspectives; and Distributional pluralism, wherein a model’s distribution over answers matches that of a given target population (see Figure 1). For each, we will also discuss relevant applications and potential evaluations, along with limitations and recommendations for future research.

**ZH** 本节形式化单个模型或系统如何做到多元的三种定义。具体地，我们勾勒 Overton 多元性（模型输出全部合理回答的谱系）、可引导多元性（模型被忠实引导以反映特定属性或视角），以及分布多元性（模型在答案上的分布与给定目标人群相匹配）（见图 1）。对每一种，我们还讨论相关的应用与可能的评测，以及局限与未来研究建议。

**EN** Throughout, we will consider a model or system ⟦SLOT_0⟧, a query ⟦SLOT_1⟧, and a response ⟦SLOT_2⟧. While we specifically focus on natural language queries and responses with ⟦SLOT_3⟧ being an LLM, our definitions can nevertheless generalize to other inputs, outputs, and models as well.

**ZH** 全文通篇考虑一个模型或系统 ⟦SLOT_0⟧、一个查询 ⟦SLOT_1⟧ 与一个回答 ⟦SLOT_2⟧。尽管我们专门聚焦自然语言查询与回答，且 ⟦SLOT_3⟧ 是一个 LLM，我们的定义仍可推广到其他输入、输出与模型。

**EN** 3.1 Overton Pluralistic Models

**ZH** 3.1 Overton 多元模型

**EN** Given an input, there are often many potential types (or modes) of answers a model can produce. For example, if a user poses a query to an LLM for which there is no single established correct answer, the LLM may answer with any one of several reasonable answers.

**ZH** 给定一个输入，模型往往能产生多种潜在类型（或模态）的回答。例如，如果用户向 LLM 提出一个没有唯一既定正确答案的查询，LLM 可能以若干合理回答中的任意一个作答。

**EN** Definitions Given a query ⟦SLOT_4⟧, consider possible answers ⟦SLOT_5⟧.

**ZH** 定义 给定一个查询 ⟦SLOT_4⟧，考虑可能的回答 ⟦SLOT_5⟧。

**EN** (1) Correct Answer in ⟦SLOT_6⟧:

**ZH** （1）⟦SLOT_6⟧ 中的正确答案：

**EN** An answer which can be conclusively verified or with which the overwhelming majority of people across various backgrounds would agree.

**ZH** 一个可被确证的回答，或来自不同背景的绝大多数人都会认同的回答。

**EN** (2) Reasonable Answer in ⟦SLOT_7⟧:

**ZH** （2）⟦SLOT_7⟧ 中的合理回答：

**EN** An answer for which there is suggestive, but inconclusive, evidence, or one with which significant swaths of the population would agree. Additional top-down restrictions (e.g., safety) may apply.

**ZH** 一个具有提示性但不确证证据的回答，或相当一部分人群会认同的回答。可能附加自上而下的限制（例如安全性）。

**EN** (3) Overton window:

**ZH** （3）Overton 窗口：

**EN** The set of all reasonable answers: ⟦SLOT_8⟧.11 1 Our terminology generalizes the concept of an “Overton window” as used in political science: “the spectrum of ideas on public policy and social issues considered acceptable or viable by the general public at a given time.” (OED, 2023)

**ZH** 所有合理回答的集合：⟦SLOT_8⟧。（脚注 1：我们的术语推广了政治学中「Overton 窗口」的概念：「在特定时刻被公众认为可接受或可行的、关于公共政策与社会议题的观点谱系。」（OED，2023））

**EN** (4) A response set ⟦SLOT_9⟧ to a query ⟦SLOT_10⟧ is Overton-pluralistic:

**ZH** （4）回答集合 ⟦SLOT_9⟧ 相对于查询 ⟦SLOT_10⟧ 是 Overton 多元的：

**EN** ⟦SLOT_11⟧ contains all potentially reasonable answers in the Overton window. This is in contrast to picking just one answer in the Overton window, or presenting an unreasonable answer which would lie outside the Overton window. A single response may be Overton-pluralistic if it synthesizes the whole response set ⟦SLOT_12⟧.

**ZH** ⟦SLOT_11⟧ 包含 Overton 窗口中所有潜在合理的回答。这与只挑选窗口中的一个回答，或给出落在窗口之外的不合理回答形成对照。如果单个回答综合了整个回答集合 ⟦SLOT_12⟧，它也可以是 Overton 多元的。

**EN** (5) Model ⟦SLOT_13⟧ is Overton-pluralistic:

**ZH** （5）模型 ⟦SLOT_13⟧ 是 Overton 多元的：

**EN** ⟦SLOT_14⟧ gives Overton-pluralistic responses to queries, that is for a given input ⟦SLOT_15⟧, the output of ⟦SLOT_16⟧.

**ZH** ⟦SLOT_14⟧ 对查询给出 Overton 多元的回答，即对于给定输入 ⟦SLOT_15⟧，⟦SLOT_16⟧ 的输出。

**EN** Motivation In many situations, there are many reasonable answers to a question (Min et al., 2020; Scherrer et al., 2023). Rather than outputting a single reasonable answer, which may be selected idiosyncratically or in a biased fashion, Overton-pluralistic models output all reasonable answers.

**ZH** 动机 在许多情形中，一个问题有许多个合理回答（Min 等，2020；Scherrer 等，2023）。与其输出一个可能以特异或有偏方式选出的合理回答，Overton 多元模型输出所有合理回答。

**EN** Potential Implementation We outline two ways to operationalize Overton pluralism. In order to determine an Overton window for a set of queries ⟦SLOT_17⟧, one could survey a population for responses to a question and identify clusters (e.g., using semantic similarity) of candidate reasonable answers. Then, one could narrow down the window to reasonable answers ⟦SLOT_18⟧ with additional polling for reasonableness, defining a minimum threshold of support, or some other top-down way of filtering out unreasonable responses. One could define a way to extract the set of “answers" ⟦SLOT_19⟧ from a model response and compare it to the window. Alternatively, one could enumerate a list of unreasonable answers ⟦SLOT_20⟧ and detect which reasonable or unreasonable answers the response entails with an entailment model (Shajalal et al., 2023; Liu et al., 2022). With both methods, metrics like precision/recall/accuracy can be calculated.

**ZH** 可能的实现 我们勾勒两种落实 Overton 多元性的方式。为确定一组查询 ⟦SLOT_17⟧ 的 Overton 窗口，可以就某个问题调查人群，并识别候选合理回答的聚类（例如使用语义相似度）。随后可以通过额外的合理性投票、定义支持度的最低阈值，或其他自上而下过滤不合理回答的方式，把窗口收窄到合理回答 ⟦SLOT_18⟧。也可以定义一种从模型回答中抽取「回答」集合 ⟦SLOT_19⟧ 的方法，并将其与窗口比较。另一种做法是枚举不合理回答的清单 ⟦SLOT_20⟧，并用蕴含模型检测回答蕴含了哪些合理或不合理的回答（Shajalal 等，2023；Liu 等，2022）。两种方法都可以计算精确率／召回率／准确率等指标。

**EN** Applications Many relevant domains fall under advice-giving. Current LLMs often give advice confidently but inconsistently or in an opinionated manner, affecting users’ downstream judgments (Krügel et al., 2023; Jakesch et al., 2023). Overton-pluralism requires consideration of multiple heterogeneous judgements, encouraging deliberation over spontaneous judgement (Kant, 1788; Rawls, 1971). It could also aid in scalable oversight (Bowman et al., 2022) to help users annotate model outputs, in the single ground truth case (Michael et al., 2023) or when we want a diversity of views. Further examples include settings where we want to encourage multiple approaches, such as mathematical proof writing.

**ZH** 应用 许多相关领域都属于建议给出这一类。当前的 LLM 常常自信却前后不一致地、或以固执己见的方式给出建议，影响用户的下游判断（Krügel 等，2023；Jakesch 等，2023）。Overton 多元性要求考虑多种异质判断，鼓励审慎思考而非自发判断（Kant，1788；Rawls，1971）。它也有助于可扩展监督（Bowman 等，2022），帮助用户在单一真值情形（Michael 等，2023）或我们希望获得多样观点时标注模型输出。另一些例子包括我们希望鼓励多种解法的场景，如数学证明写作。

**EN** Limitations Defining and operationalizing the Overton window may present a challenge. If a reasonable answer is determined by a set of expert annotators, it may be difficult to scale. If the Overton window is not properly defined, models may contribute to bothsidesism / false balance (Imundo & Rapp, 2021; Boykoff & Boykoff, 2004). One remedy may be to present the support or certainty for each reasonable answer in addition to its content, although current LLMs struggle with this (Zhou et al., 2024). Also, while pluralism may never be completely neutral, it can be considered a fairer response to queries (Haraway, 1988). Finally, this framework requires long-form responses with multiple answers; other concepts of pluralism may be required for distributions over short answers (see §3.3).

**ZH** 局限 定义并落实 Overton 窗口可能构成挑战。如果合理回答由一组专家标注者确定，可能难以规模化。如果 Overton 窗口定义不当，模型可能助长两面主义／虚假平衡（Imundo & Rapp，2021；Boykoff & Boykoff，2004）。一种补救办法是在内容之外同时呈现每个合理回答所获的支持度或确定性，尽管当前 LLM 在此上仍有困难（Zhou 等，2024）。此外，尽管多元性可能永远无法完全中立，它仍可被视为对查询更公平的回应（Haraway，1988）。最后，这一框架要求包含多个答案的长文本回答；对于短答案上的分布，可能需要其他多元性概念（见 §3.3）。

**EN** Alignment Procedures and Recommendations While RLHF may implicitly steer models to Overton pluralism to the extent that users prefer it, further study into this is needed. Alternatively, one approach to explicitly encourage Overton pluralism is taking multiple samples from a model (Long, 2023; Jung et al., 2022), potentially prompting for diverse outputs (Hayati et al., 2023), to simulate an Overton window. Alternatively, one could manually create the batch of reasonable responses. A model can be trained to output a synthesis of the entire batch. Datasets which identify human values (Hendrycks et al., 2020; Sorensen et al., 2023) can be used to evaluate Overton-pluralism. We recommend further study into models’ current degree of Overton-pluralism and how it can be amplified for relevant applications.

**ZH** 对齐程序与建议 尽管 RLHF 可能在用户偏好的程度上隐式地把模型引向 Overton 多元性，这一点仍需进一步研究。另一种显式鼓励 Overton 多元性的做法是从模型中多次采样（Long，2023；Jung 等，2022），并可能提示生成多样的输出（Hayati 等，2023），以模拟一个 Overton 窗口。也可以人工创建一批合理回答，再训练模型输出对整批回答的综合。识别人类价值观的数据集（Hendrycks 等，2020；Sorensen 等，2023）可用于评估 Overton 多元性。我们建议进一步研究模型当前的 Overton 多元性程度，以及如何在相关应用中放大它。

**EN** 3.2 Steerable Pluralistic Models

**ZH** 3.2 可引导多元模型

**EN** A pluralistic model might instead faithfully steer (or align) its responses to a given attribute or perspective, such as a value, framework, or population.

**ZH** 另一种可能是：一个多元模型忠实地把回答引导（或对齐）到给定的属性或视角，例如某种价值、框架或人群。

**EN** Definitions With this in mind, let us consider:

**ZH** 定义 有鉴于此，让我们考虑：

**EN** (6) Steering attributes ⟦SLOT_21⟧:

**ZH** （6）引导属性 ⟦SLOT_21⟧：

**EN** Attributes/properties/perspecti-ves which we wish a model to faithfully reflect. Examples include groups of people from a shared culture, philosophical/political schools of thought, or particular values. To reflect multiple attributes simultaneously, the elements of ⟦SLOT_22⟧ could be construed as sets of attributes.

**ZH** 我们希望模型忠实反映的属性／性质／视角。例子包括来自共同文化的群体、哲学／政治思想流派，或特定的价值观。为同时反映多个属性，⟦SLOT_22⟧ 的元素可被理解为属性的集合。

**EN** (7) Response ⟦SLOT_23⟧ faithfully reflects attribute ⟦SLOT_24⟧:

**ZH** （7）回答 ⟦SLOT_23⟧ 忠实反映属性 ⟦SLOT_24⟧：

**EN** The response ⟦SLOT_25⟧ to the query ⟦SLOT_26⟧ is consistent with, or follows from, attribute ⟦SLOT_27⟧.

**ZH** 回答 ⟦SLOT_25⟧ 针对查询 ⟦SLOT_26⟧ 与属性 ⟦SLOT_27⟧ 一致，或从该属性推得。

**EN** (8) Model ⟦SLOT_28⟧ is steerably-pluralistic with respect to attributes ⟦SLOT_29⟧:

**ZH** （8）模型 ⟦SLOT_28⟧ 关于属性 ⟦SLOT_29⟧ 是可引导多元的：

**EN** Given an input ⟦SLOT_30⟧ and an attribute ⟦SLOT_31⟧, the model ⟦SLOT_32⟧ conditioned on ⟦SLOT_33⟧ produces a response ⟦SLOT_34⟧ which faithfully reflects ⟦SLOT_35⟧.

**ZH** 给定输入 ⟦SLOT_30⟧ 与属性 ⟦SLOT_31⟧，模型 ⟦SLOT_32⟧ 以 ⟦SLOT_33⟧ 为条件产生的回答 ⟦SLOT_34⟧ 忠实地反映 ⟦SLOT_35⟧。

**EN** Motivation In many instances, we want models to respond to queries in a consistent and specifiable manner. Models which have been so heavily “aligned” towards a specific attribute such that they cannot be steered to other attributes fail to be useful (or usable) to populations who may not share that value or attribute. We see evidence of this in the “Silicon Valley” and “WEIRD” (Henrich et al., 2010) bias of many LLMs, which often skew male, White, American, liberal, and wealthy in perspective (Santurkar et al., 2023; Hartmann et al., 2023; Perez et al., 2022; Santy et al., 2023).

**ZH** 动机 在许多情形中，我们希望模型以一致且可指定的方式回应查询。被过度「对齐」到某个特定属性、以致无法被引导到其他属性的模型，对并不共享该价值或属性的人群而言是无用（或不可用）的。我们在许多 LLM 的「硅谷」与「WEIRD」（Henrich 等，2010）偏置中看到了这一点的证据：它们的视角往往偏向男性、白人、美国、自由派与富裕阶层（Santurkar 等，2023；Hartmann 等，2023；Perez 等，2022；Santy 等，2023）。

**EN** Potential Implementation Given queries ⟦SLOT_36⟧ and attributes ⟦SLOT_37⟧, one needs a way to condition the model on attributes at inference. To measure whether a response reflects ⟦SLOT_38⟧, one could either use direct human annotations or reward models that are tuned specifically to the attributes, such as a value-specific reward (Sorensen et al., 2023). These attribute-specific faithfulness scores would be the degree to which a model is steerably pluralistic.

**ZH** 可能的实现 给定查询 ⟦SLOT_36⟧ 与属性 ⟦SLOT_37⟧，需要一种在推理时以属性为条件约束模型的方法。为度量回答是否反映 ⟦SLOT_38⟧，可以使用直接的人工标注，或使用专门针对这些属性调优的奖励模型，例如特定价值的奖励（Sorensen 等，2023）。这些属性专属的忠实度分数，就是模型可引导多元性的程度。

**EN** Different attributes may require different metrics for faithfulness, depending on the kind of attribute and level of ambiguity. For example, for a particular difficult moral quandary, there may be no ambiguity given a particular ethical framework (e.g., only one “correct" or faithful answer). However, if you condition instead on a population, there may still be disagreement or ambiguity - other approaches like an Overton window may apply here.

**ZH** 不同属性可能需要不同的忠实度度量，取决于属性的类型与模糊程度。例如，对于某个棘手的道德困境，若给定特定的伦理框架，可能并不存在模糊性（即只有一个「正确」或忠实的回答）。然而如果以人群为条件，仍可能存在分歧或模糊性——此时 Overton 窗口等其他方法可能适用。

**EN** Several previous works have measured forms of steerable pluralism, particularly with respect to moral, political, and cultural perspectives (Argyle et al., 2023; Jiang et al., 2022; Simmons, 2023; Ramezani & Xu, 2023; Santy et al., 2023). However, previous work suggests that conditional pluralism is far from solved (Santurkar et al., 2023).

**ZH** 若干先前工作已度量过可引导多元性的某些形式，特别是关于道德、政治与文化视角（Argyle 等，2023；Jiang 等，2022；Simmons，2023；Ramezani & Xu，2023；Santy 等，2023）。然而先前工作表明，条件多元性远未解决（Santurkar 等，2023）。

**EN** Applications An important application of steerable-pluralism is customization. Users often want to personalize models towards characteristic properties and perspectives (Chen et al., 2023), in tasks such as writing assistance (Li et al., 2023a) and ideation (Girotra et al., 2023; Ma et al., 2023). Steering towards therapeutic values can help in the mental health domain (Song et al., 2024; Sharma et al., 2023a). Steering models to represent multiple different perspectives can be valuable in creative production (Shanahan & Clarke, 2023), psychological inquiry (Shanahan et al., 2023), simulating social systems (Park et al., 2022), and deliberative discourse (Danry et al., 2023; Landemore & Page, 2015; Page, 2019; Page, 2008).

**ZH** 应用 可引导多元性的一个重要应用是定制化。用户常常希望把模型个性化到特定的性质与视角（Chen 等，2023），用于写作辅助（Li 等，2023a）与创意构思（Girotra 等，2023；Ma 等，2023）等任务。向治疗性价值引导可在心理健康领域提供帮助（Song 等，2024；Sharma 等，2023a）。把模型引导到代表多种不同视角，在创意生产（Shanahan & Clarke，2023）、心理学探究（Shanahan 等，2023）、社会系统模拟（Park 等，2022）与审议性话语（Danry 等，2023；Landemore & Page，2015；Page，2019；Page，2008）中都可能很有价值。

**EN** Moreover, steerably pluralistic models may have useful representations in a variety of settings, such as hate speech detection (Feng et al., 2023) and negative thought reframing (Sharma et al., 2023b; Sharma et al., 2023c). In general, this may allow varying “cognitive architectures” for more structured and generally intelligent systems (Sumers et al., 2023).

**ZH** 此外，可引导多元模型在多种场景中可能具备有用的表示，例如仇恨言论检测（Feng 等，2023）与消极想法重构（Sharma 等，2023b；Sharma 等，2023c）。一般而言，这可能允许为更结构化、更通用的智能系统提供可变的「认知架构」（Sumers 等，2023）。

**EN** Limitations Steerable pluralism requires deciding which attributes are acceptable to steer the model. We may want to disallow some attributes (e.g., hate speech). The challenges here are similar to those in determining which answers are “reasonable” in Overton-pluralism, such as subjectivity or arbitrariness in the selection of steerable attributes. Moreover, if attributes are defined too broadly, there is a risk of stereotyping or “flattening” the nuances of the complex perspectives and people that attributes are intended to represent (Durmus et al., 2023). In some cases, an intersectional evaluation (Crenshaw, 1989), in which attributes are not considered independently but in conjunction with each other, may be necessary.

**ZH** 局限 可引导多元性需要决定哪些属性是可接受用于引导模型的。我们可能希望禁止某些属性（例如仇恨言论）。这里的挑战与 Overton 多元性中判断哪些回答「合理」所面临的挑战相似，例如在选择可引导属性时的主观性或任意性。此外，如果属性定义得过于宽泛，存在刻板化或「压平」那些属性本欲代表的复杂视角与人群之细微差别的风险（Durmus 等，2023）。在某些情况下，可能需要交叉性评估（Crenshaw，1989），即不独立地、而是相互结合地考察各属性。

**EN** Alignment Procedures and Recommendations There are a variety of ways to induce particular values at inference time. These include conditioning on certain groups (Argyle et al., 2023; Hwang et al., 2023) and studying which conditions (responses, demographics, etc.) yield the best agreement. Li et al. (2023b); Kim & Lee (2023) learn user embeddings which they use to induce certain values from LLMs. Zhao et al. (2023) add a module to base LLMs which aims to predict group responses in a few-shot manner. Fleisig et al. (2023) predict annotator ratings for specific groups. Sharma et al. (2023c); Sharma et al. (2023d) rewrite responses for specific audiences.

**ZH** 对齐程序与建议 有多种方式可在推理时诱导特定价值。包括以某些群体为条件（Argyle 等，2023；Hwang 等，2023），并研究哪些条件（回答、人口统计特征等）能产生最佳一致度。Li 等（2023b）；Kim & Lee（2023）学习用户嵌入，用以从 LLM 中诱导特定价值。Zhao 等（2023）在基础 LLM 上添加一个模块，旨在以少样本方式预测群体回答。Fleisig 等（2023）预测特定群体的标注者评分。Sharma 等（2023c）；Sharma 等（2023d）为特定受众改写回答。

**EN** We believe that steerability research will become increasingly important as users desire more customizability. While there may be certain behaviors to which a model should not be aligned, we advocate for systems that can be aligned to many attributes within an acceptable range.

**ZH** 我们相信，随着用户对可定制性提出更高要求，可引导性研究将变得越来越重要。尽管可能存在某些模型不应被对齐到的行为，我们倡导构建可在可接受范围内对齐到多种属性的系统。

**EN** 3.3 Distributionally Pluralistic Models

**ZH** 3.3 分布多元模型

**EN** Another way to operationalize pluralism is in the distribution over answers compared to a given population.

**ZH** 落实多元性的另一种方式，是与给定人群相比，在答案上的分布。

**EN** Definitions In this framework, we consider:

**ZH** 定义 在这一框架下，我们考虑：

**EN** (9) A population or group of people ⟦SLOT_39⟧:

**ZH** （9）人群或人的群体 ⟦SLOT_39⟧：

**EN** A set of people which we want the model to represent.

**ZH** 我们希望模型加以表征的一群人。

**EN** (10) Model ⟦SLOT_40⟧ is distributionally-pluralistic with respect to a reference population ⟦SLOT_41⟧:

**ZH** （10）模型 ⟦SLOT_40⟧ 关于参照人群 ⟦SLOT_41⟧ 是分布多元的：

**EN** For a given prompt ⟦SLOT_42⟧, ⟦SLOT_43⟧ is as likely to provide response ⟦SLOT_44⟧ as the reference population ⟦SLOT_45⟧. In other words, ⟦SLOT_46⟧ is well-calibrated w.r.t. the distribution over answers from ⟦SLOT_47⟧.

**ZH** 对于给定提示 ⟦SLOT_42⟧，⟦SLOT_43⟧ 给出回答 ⟦SLOT_44⟧ 的可能性与参照人群 ⟦SLOT_45⟧ 相同。换言之，⟦SLOT_46⟧ 关于来自 ⟦SLOT_47⟧ 的答案分布是良好校准的。

**EN** Motivation and Applications Distributional pluralism in an LLM is crucial for any application where ⟦SLOT_48⟧ is used to simulate, interface with, or otherwise model the views of a population, e.g., simulating populations via agent-based modeling (Törnberg et al., 2023; Park et al., 2022; Park et al., 2023), piloting subject/user responses to surveys (Argyle et al., 2023; Aher et al., 2023), survey design (Ziems et al., 2023), or studying the internet as a cultural artifact (Buttrick, 2024).

**ZH** 动机与应用 LLM 中的分布多元性，对任何用 ⟦SLOT_48⟧ 来模拟、交互或以其他方式建模人群观点的应用都至关重要，例如通过基于智能体的建模模拟人群（Törnberg 等，2023；Park 等，2022；Park 等，2023）、预演受试者／用户对调查的回答（Argyle 等，2023；Aher 等，2023）、问卷设计（Ziems 等，2023），或把互联网作为文化人工制品加以研究（Buttrick，2024）。

**EN** Potential Implementation Let ⟦SLOT_49⟧ be a set of queries to which ⟦SLOT_50⟧ gives a distribution ⟦SLOT_51⟧. For example, a census survey or public opinion poll. ⟦SLOT_52⟧’s estimate, ⟦SLOT_53⟧, can be compared to the population distribution using any distributional divergence metrics, such as Jensen-Shannon divergence, KL-divergence, or Wasserstein distance (Santurkar et al., 2023; Durmus et al., 2023), or hard measures like accuracy or tetrachoric correlation (Argyle et al., 2023).

**ZH** 可能的实现 令 ⟦SLOT_49⟧ 为 ⟦SLOT_50⟧ 给出分布 ⟦SLOT_51⟧ 的一组查询。例如一次人口普查或民意调查。⟦SLOT_52⟧ 的估计 ⟦SLOT_53⟧ 可用任何分布散度指标与人群分布比较，如 Jensen-Shannon 散度、KL 散度或 Wasserstein 距离（Santurkar 等，2023；Durmus 等，2023），或用准确率、四分相关等硬指标（Argyle 等，2023）。

**EN** Limitations One potential limitation of distributional pluralism is its proportional nature. This means that more frequent opinions will be output by a model with higher frequency, even if this response is harmful - although might be mitigated by defining a window of reasonableness as in Overton pluralism. Another limitation is the need for a predetermined target distribution–a population. In creation of a general LLM, like ChatGPT, who is the target distribution? Furthermore, for many open-ended queries, it is not clear whether there is any response frequency data.

**ZH** 局限 分布多元性的一个潜在局限是它的比例性质。这意味着更常见的意见会被模型以更高频率输出，即便该回答有害——尽管可以通过像 Overton 多元性那样定义一个合理窗口来缓解。另一个局限是需要预先确定的目标分布——即一个人群。在创建 ChatGPT 这样的通用 LLM 时，目标分布是谁？此外，对于许多开放式查询，并不清楚是否存在任何回答频率数据。

**EN** Alignment procedures While, to our knowledge, there are no alignment procedures to explicitly increase distributional calibration, there are a couple promising directions. One is to simply (pre)train a model on more data from the target population. As the cross entropy objective encourages a model to learn the distributions of speech of a training population, simply providing more data from that population ought to lead to better representation. Another promising direction is to train on the data from a population (e.g., survey data) that one could use to evaluate distributional pluralism, although it is unclear how well this will generalize to novel questions/domains. Further research is needed here.

**ZH** 对齐程序 据我们所知，目前没有显式提升分布校准的对齐程序，但有若干有前景的方向。其一是简单地在（预）训练时使用更多来自目标人群的数据。由于交叉熵目标鼓励模型学习训练人群的话语分布，只提供来自该人群的更多数据理应带来更好的表征。另一个有前景的方向是在可用于评估分布多元性的人群数据（例如调查数据）上训练，尽管这能多好地推广到新问题／新领域尚不清楚。这方面需要进一步研究。

**EN** Recommendations Oftentimes when researchers measure to which group of people a model best aligns, they compare average responses. In contrast, we advocate for comparing distributions because it leads to clearer results: groups of people have distributions over answers, and probabilistic models do as well. We advocate for more distributionally pluralistic evaluations with respect to clearly specified groups of people to better characterize current models. Nonetheless, the stochasticity in distributional pluralism is not desirable in all cases–for example, when the behavior of a model needs to be tightly controlled.

**ZH** 建议 研究者在度量模型最贴合哪一群人时，常常比较平均回答。相反，我们主张比较分布，因为它能带来更清晰的结果：人群在答案上有分布，概率模型同样如此。我们主张针对明确界定的人群开展更多分布多元性评测，以更好地刻画当前模型。尽管如此，分布多元性中的随机性并非在所有情形下都是可取的——例如当模型的行为需要被严格控制时。

**EN** 4 Pluralism for Benchmarks

**ZH** 4 面向基准的多元性

<!-- [原子块 · img]  -->

**EN** Figure 2: Three kinds of pluralistic benchmarks.

**ZH** 图 2：三类多元基准。

**EN** While the last section defined how a model can be pluralistic, here we explore how a benchmark can be pluralistic. Most current benchmarks are monistic (focused on a single objective). Pluralistic benchmarks have more than one objective to maximize. Importantly, each is measured separately.

**ZH** 上一节定义了模型如何做到多元，本节探讨基准如何做到多元。当前多数基准都是一元的（聚焦单一目标）。多元基准有不止一个需要最大化的目标；重要的是，每个目标被分别度量。

**EN** 4.1 Multi-Objective Benchmarks

**ZH** 4.1 多目标基准

**EN** Definitions Define:

**ZH** 定义 定义：

**EN** (11) Objectives to maximize ⟦SLOT_54⟧:

**ZH** （11）需要最大化的目标 ⟦SLOT_54⟧：

**EN** A set of multiple objectives to evaluate a model ⟦SLOT_55⟧, each of which which we desire to maximize. Each ⟦SLOT_56⟧ maps from a model ⟦SLOT_57⟧ to a scalar in ⟦SLOT_58⟧.

**ZH** 用于评估模型 ⟦SLOT_55⟧ 的多个目标构成的集合，其中每个目标我们都希望最大化。每个 ⟦SLOT_56⟧ 把模型 ⟦SLOT_57⟧ 映射到 ⟦SLOT_58⟧ 中的一个标量。

**EN** (12) Model ⟦SLOT_59⟧ is a Pareto improvement to model ⟦SLOT_60⟧.:

**ZH** （12）模型 ⟦SLOT_59⟧ 是对模型 ⟦SLOT_60⟧ 的 Pareto 改进：

**EN** ⟦SLOT_61⟧. In other words, ⟦SLOT_62⟧ is at least as good as ⟦SLOT_63⟧ for all objectives and strictly better for some objective ⟦SLOT_64⟧.

**ZH** ⟦SLOT_61⟧。换言之，⟦SLOT_62⟧ 在所有目标上至少与 ⟦SLOT_63⟧ 一样好，并且在某个目标 ⟦SLOT_64⟧ 上严格更优。

**EN** (13) Function ⟦SLOT_65⟧ is a commensurating function over objectives ⟦SLOT_66⟧:

**ZH** （13）函数 ⟦SLOT_65⟧ 是目标 ⟦SLOT_66⟧ 上的通约函数：

**EN** ⟦SLOT_67⟧ is a function which combines multiple objectives into a single scalar meta-objective of the form ⟦SLOT_68⟧.

**ZH** ⟦SLOT_67⟧ 是把多个目标组合成形如 ⟦SLOT_68⟧ 的单一标量元目标的函数。

**EN** (14) Benchmark ⟦SLOT_69⟧ is a multi-objective benchmark over ⟦SLOT_70⟧:

**ZH** （14）基准 ⟦SLOT_69⟧ 是关于 ⟦SLOT_70⟧ 的多目标基准：

**EN** ⟦SLOT_71⟧ reports the entire spectrum of model performances on all objectives and can be flexibly adapted to multiple commensurating functions. The “top" of the leaderboard is the set of solutions (models) for which there is no Pareto improvement.

**ZH** ⟦SLOT_71⟧ 报告模型在所有目标上的完整表现谱系，并可灵活适配多种通约函数。排行榜的「顶部」是不存在 Pareto 改进的解（模型）集合。

**EN** In practice, the set of solutions for which there is no Pareto improvement can be quite large. Therefore, it may be convenient to define a commensurating function ⟦SLOT_72⟧ to determine a ranking for a given use case. The important part of a Pareto benchmark is that if objectives are combined, it is done explicitly, reporting all objectives for all solutions. This makes it possible to propose alternative explicit trade-offs.

**ZH** 在实践中，不存在 Pareto 改进的解集合可能相当大。因此，定义一个通约函数 ⟦SLOT_72⟧ 来确定给定用例下的排序可能更方便。Pareto 基准的关键在于：如果要把各目标合并，必须显式地进行，并报告所有解在所有目标上的表现。这使得提出替代性的显式权衡成为可能。

**EN** Motivation and Applications Implicit trade-offs are everywhere. For example, there is a fundamental tension between helpfulness and harmlessness for LLMs (Askell et al., 2021; Bai et al., 2022a). However, these two attributes often get clumped together and are implicitly traded-off through data mixtures or vague human preferences. Through explicit multi-objective benchmarks, we can better understand how they trade-off and make informed decisions when selecting a model for a given application or domain (Liang et al., 2023; Srivastava et al., 2023; Hendrycks et al., 2023).

**ZH** 动机与应用 隐式权衡无处不在。例如，对 LLM 而言，有用性与无害性之间存在根本张力（Askell 等，2021；Bai 等，2022a）。然而这两个属性常常被混在一起，并通过数据混合或模糊的人类偏好被隐式地权衡。通过显式的多目标基准，我们可以更好地理解它们如何权衡，并在为给定应用或领域选择模型时做出有依据的决定（Liang 等，2023；Srivastava 等，2023；Hendrycks 等，2023）。

**EN** Potential Implementation There are many ways to operationalize these objectives, such as evaluation on test sets, outputs of a reward model, preference/ELO scores, model properties and more. Other objectives might include adherence to individual rules such as “Do not offer financial advice" (Glaese et al., 2022) or principles (Bai et al., 2022b).

**ZH** 可能的实现 落实这些目标有许多方式，例如在测试集上评测、奖励模型的输出、偏好／ELO 分数、模型性质等。其他目标可以包括对个体规则的遵循，例如「不要提供财务建议」（Glaese 等，2022）或各项原则（Bai 等，2022b）。

**EN** Limitations If the set of metrics is very large, it may be costly to compare models across a large number of dimensions. The choice of which objectives and the granularity of benchmarks to include will influence the strength of the evaluation. Choosing the correct number and level of abstraction of the objectives can be a difficult design decision.

**ZH** 局限 如果指标集合非常大，在大量维度上比较模型的成本可能很高。选择纳入哪些目标以及基准的粒度，会影响评测的效力。选择目标的正确数量与抽象层次可能是一项困难的设计决策。

**EN** Alignment Procedures and Recommendations Most alignment techniques optimize a single objective instead of a group of objectives, requiring a commensurating function. To avoid this, we can look to techniques from multi-objective RL (Hayes et al., 2022; Yang et al., 2019; Tozer et al., 2017). While several multi-objective benchmarks exist (Liang et al., 2023; Srivastava et al., 2023; Pan et al., 2023) and it is common practice to evaluate LLMs on a range of evaluations, we encourage the continued use, research, and development of these benchmarks. Single-value benchmarks can often lead to “reward-hacking” and exploiting spurious features, such as annotators’ preference for more verbose responses (Wang et al., 2023a). Multiple objectives allow for a more diverse set of model strengths (Ethayarajh & Jurafsky, 2020) and mitigate over-optimization.

**ZH** 对齐程序与建议 多数对齐技术优化单一目标而非一组目标，因而需要一个通约函数。为避免这一点，我们可以借鉴多目标强化学习的技术（Hayes 等，2022；Yang 等，2019；Tozer 等，2017）。尽管已有若干多目标基准（Liang 等，2023；Srivastava 等，2023；Pan 等，2023），且在一系列评测上评估 LLM 已是常见做法，我们仍鼓励持续使用、研究并开发这类基准。单值基准常常导致「奖励 hacking」与利用虚假特征，例如标注者对更冗长回答的偏好（Wang 等，2023a）。多个目标允许更多样的模型优势（Ethayarajh & Jurafsky，2020），并缓解过度优化。

**EN** 4.2 Trade-Off Steerable Benchmarks

**ZH** 4.2 权衡可引导基准

**EN** In the multi-objective benchmark section, we assumed that the model was static, occupying a single point in the objective space. However, it is useful to consider a benchmark which encourages models to be steerable to trade off objectives in different ways at inference time.

**ZH** 在多目标基准一节中，我们假定模型是静态的，在目标空间中占据单点。然而，考虑一种鼓励模型在推理时以不同方式被引导去权衡目标的基准是有益的。

**EN** Many of the takeaways from the previous section apply here, so we will focus our discussion on what is unique about trade-off steerable benchmarks.

**ZH** 上一节的许多结论在此同样适用，因此我们把讨论聚焦于权衡可引导基准的独特之处。

**EN** Definitions Building on the definitions from Section 4.1,

**ZH** 定义 在 4.1 节定义的基础上，

**EN** (15) Steering commensurating (or trade-off) functions ⟦SLOT_73⟧:

**ZH** （15）引导通约（或权衡）函数 ⟦SLOT_73⟧：

**EN** A set of commensurating functions to steer a model towards.

**ZH** 用于把模型引导过去的一组通约函数。

**EN** (16) Model ⟦SLOT_74⟧ is steerable to functions ⟦SLOT_75⟧:

**ZH** （16）模型 ⟦SLOT_74⟧ 对函数 ⟦SLOT_75⟧ 是可引导的：

**EN** For ⟦SLOT_76⟧, the model steered to ⟦SLOT_77⟧ (denoted ⟦SLOT_78⟧) maximizes ⟦SLOT_79⟧: ⟦SLOT_80⟧

**ZH** 对于 ⟦SLOT_76⟧，被引导到 ⟦SLOT_77⟧（记作 ⟦SLOT_78⟧）的模型最大化 ⟦SLOT_79⟧：⟦SLOT_80⟧

**EN** (17) Benchmark ⟦SLOT_81⟧ is a trade-off steerable benchmark with respect to ⟦SLOT_82⟧:

**ZH** （17）基准 ⟦SLOT_81⟧ 是关于 ⟦SLOT_82⟧ 的权衡可引导基准：

**EN** ⟦SLOT_83⟧ attempts to measure 1) a model’s ability to maximize objectives ⟦SLOT_84⟧ and 2) a model’s steerability to various commensurating functions ⟦SLOT_85⟧.

**ZH** ⟦SLOT_83⟧ 试图度量 1）模型最大化目标 ⟦SLOT_84⟧ 的能力，以及 2）模型对多种通约函数 ⟦SLOT_85⟧ 的可引导性。

**EN** Motivation and Applications A trade-off steerable benchmark measures whether a single model can represent solutions across a spectrum of objectives, allowing for tuning to trade-off functions of choice at deployment time. Any application where customization is desirable could benefit from this kind of benchmark.

**ZH** 动机与应用 权衡可引导基准度量单一模型能否表征跨目标谱系上的解，从而允许在部署时按所选的权衡函数进行调节。任何需要定制化的应用都可从这类基准中获益。

**EN** Potential Implementation Many commensurating functions are possible, including linear combinations (e.g., ⟦SLOT_86⟧) and selecting a single objective.

**ZH** 可能的实现 许多通约函数都是可能的，包括线性组合（例如 ⟦SLOT_86⟧）与选择单一目标。

**EN** Given ⟦SLOT_87⟧, one implementation of a trade-off steerable benchmark could be a reward which tries to maximize the steerability and overall objective values, as follows:

**ZH** 给定 ⟦SLOT_87⟧，权衡可引导基准的一种实现可以是一个试图最大化可引导性与总体目标值的奖励，如下所示：

<!-- [原子块 · table] ∑ f ∈ ℱ f ⁡ ( ℳ f ) \sum_{f\in\mathcal{F}}f(\mathcal{M}_{f}) -->

**EN** Maximizing requires the model to increase the overall value of each ⟦SLOT_88⟧ and also match the aligned model to the corresponding objective function. Related concepts include the hypervolume indicator (Guerreiro et al., 2020) and expected utility metric (Zintgraf et al., 2015).

**ZH** 最大化要求模型提升每个 ⟦SLOT_88⟧ 的总体价值，并让被对齐的模型匹配相应的目标函数。相关概念包括超体积指标（Guerreiro 等，2020）与期望效用指标（Zintgraf 等，2015）。

**EN** Limitations This framework assumes a set of commensurating functions. However, many philosophers who subscribe to value pluralism believe that values are incommensurable and cannot be traded off (Hsieh & Andersson, 2021). Trade-off sterable benchmarks (and most of machine learning) are incompatible with that view. It is also important for generalization that the kind of commensurating functions desired for use at test time are present in the benchmark.

**ZH** 局限 这一框架假定存在一组通约函数。然而，许多信奉价值多元主义的哲学家认为，价值是不可通约的，无法被权衡（Hsieh & Andersson，2021）。权衡可引导基准（以及多数机器学习方法）与这一观点不相容。同样重要的是，为泛化起见，测试时期望使用的那类通约函数应当出现在基准中。

**EN** Alignment Procedures and Recommendations Some promising procedures to steer models include controllable decoding (Liu et al., 2024; Qin et al., 2022; Lu et al., 2020), prefix tokens/custom instructions (Chen et al., 2021; Lu et al., 2022), and model soups (Wortsman et al., 2022; Jang et al., 2023; Ramé et al., 2023). To our knowledge, however, there are no standard LLM trade-off steerable benchmarks. We advocate for increased development of such benchmarks to spur more development in steerable AI systems.

**ZH** 对齐程序与建议 一些有前景的模型引导方法包括可控解码（Liu 等，2024；Qin 等，2022；Lu 等，2020）、前缀词元／自定义指令（Chen 等，2021；Lu 等，2022）与 model soups（模型汤）（Wortsman 等，2022；Jang 等，2023；Ramé 等，2023）。然而据我们所知，目前尚无标准的 LLM 权衡可引导基准。我们倡导加大此类基准的开发力度，以推动可引导 AI 系统的发展。

**EN** 4.3 Jury-Pluralistic Benchmarks

**ZH** 4.3 陪审团多元基准

**EN** While multi-objective benchmarks deal with an arbitrary objective type, it is also useful to talk about the specific case when there is a population of annotators (or jury) to which we wish to align. Here, we formalize a type of benchmark which separately and explicitly models a jury (Gordon et al., 2022) to maximize an overall welfare function.

**ZH** 多目标基准处理任意类型的目标，而讨论我们希望对齐到的标注者（或陪审团）人群这一特定情形同样有益。这里，我们形式化一类基准，它分别且显式地对一个陪审团（Gordon 等，2022）建模，以最大化总体福利函数。

**EN** Definitions We define:

**ZH** 定义 我们定义：

**EN** (18) Jury/Population/Annotators ⟦SLOT_89⟧:

**ZH** （18）陪审团／人群／标注者 ⟦SLOT_89⟧：

**EN** Some population which we wish to represent in our evaluation. Each annotator/person/jury member ⟦SLOT_90⟧ maps from an query and response to a scalar reward or utility ⟦SLOT_91⟧.

**ZH** 我们希望在评测中加以表征的某个人群。每个标注者／人／陪审团成员 ⟦SLOT_90⟧ 把查询与回答映射到一个标量奖励或效用 ⟦SLOT_91⟧。

**EN** (19) Function ⟦SLOT_92⟧ is a welfare function over jury ⟦SLOT_93⟧:

**ZH** （19）函数 ⟦SLOT_92⟧ 是陪审团 ⟦SLOT_93⟧ 上的福利函数：

**EN** ⟦SLOT_94⟧ is a function which combines the jury’s utilities into a single scalar welfare objective of the form ⟦SLOT_95⟧.

**ZH** ⟦SLOT_94⟧ 是把陪审团的效用组合成形如 ⟦SLOT_95⟧ 的单一标量福利目标的函数。

**EN** (20) Benchmark ⟦SLOT_96⟧ is jury-pluralistic:

**ZH** （20）基准 ⟦SLOT_96⟧ 是陪审团多元的：

**EN** ⟦SLOT_97⟧ explicitly measures each juror ⟦SLOT_98⟧ to maximize a welfare function ⟦SLOT_99⟧.

**ZH** ⟦SLOT_97⟧ 显式度量每个陪审员 ⟦SLOT_98⟧，以最大化福利函数 ⟦SLOT_99⟧。

**EN** Motivation and Applications Jury-pluralistic benchmarks can serve as a concrete approach for democratic AI alignment (Koster et al., 2022; Ovadya, 2023; Mishra, 2023). They allow us to explicitly reason over which users or groups models are being aligned to, and potentially obtain fairer outcomes as people are included and social welfare functions are selected. Consensus-seeking applications benefit from this approach. For instance, Deepmind trained an LLM to find consensus statements that users preferred to any individual human-written statement (Bakker et al., 2022) and Twitter’s Community Notes has moderated misinformation by leveraging consensus between users who often disagree (Wojcik et al., 2022). These approaches help to integrate a diverse set of user preferences, which have been found to vary globally in perceptions such as safety judgments (Aroyo et al., 2023).

**ZH** 动机与应用 陪审团多元基准可作为民主化 AI 对齐的具体路径（Koster 等，2022；Ovadya，2023；Mishra，2023）。它们让我们能够显式地推演模型正被对齐到哪些用户或群体，并在人们被纳入、社会福利函数被选定后潜在地获得更公平的结果。寻求共识的应用可从这一路径中获益。例如，Deepmind 训练了一个 LLM 来寻找用户比任何单条人类撰写陈述都更偏好的共识陈述（Bakker 等，2022）；Twitter 的 Community Notes 则利用常常意见相左的用户之间的共识来治理错误信息（Wojcik 等，2022）。这些做法有助于整合多样化的用户偏好——研究发现，在安全判断等感知上，用户偏好在全球范围内存在差异（Aroyo 等，2023）。

**EN** Potential Implementation One could construct a representative jury (e.g., of a particular country, population, or expertise) using established social science methods (Flanigan et al., 2021; Arnesen & Peters, 2018). One could also construct a jury designed to amplify specific perspectives. For instance, in online communities, under-represented users sometimes face extra harassment (Pew Research Center, 2021). To combat this, community-specific moderation algorithms could be aligned to a jury featuring their voices. Once a jury is selected, jury member functions ⟦SLOT_100⟧ can be approximated in several ways. For example, a separate preference/reward model could be trained for each jury member (Gordon et al., 2022), or they could be estimated using entailment from some user-written statement (Bakker et al., 2022). These computational jury functions may be necessary for alignment, but evaluation would ideally be validated by human annotators.

**ZH** 可能的实现 可以用既有的社会科学方法构建具有代表性的陪审团（例如代表某个国家、人群或专长）（Flanigan 等，2021；Arnesen & Peters，2018）。也可以构建一个旨在放大特定视角的陪审团。例如，在线社区中，代表性不足的用户有时会面临额外的骚扰（Pew Research Center，2021）。为应对这一点，社区专属的内容治理算法可以被对齐到一个包含他们声音的陪审团。陪审团选定后，陪审团成员函数 ⟦SLOT_100⟧ 可用几种方式近似。例如，可以为每个陪审团成员训练一个单独的偏好／奖励模型（Gordon 等，2022），或借助从某些用户撰写陈述出发的蕴含关系来估计（Bakker 等，2022）。这些计算化的陪审团函数对对齐可能是必要的，但评测最好由人类标注者验证。

**EN** Different welfare function choices can lead to explicit tradeoffs between the juror utilities as well. For example, using a class of social welfare functions (Moulin, 2004; Bakker et al., 2022)–

**ZH** 不同的福利函数选择也可以在陪审员效用之间带来显式权衡。例如，使用一类社会福利函数（Moulin，2004；Bakker 等，2022）——

<!-- [原子块 · table] w α ​ ( j 1 , … , j n ) = { ( 1 n ​ ∑ i = 1 n j i 1 − α ) 1 1 − α if ​ α ≥ 0 , α ≠ 1 OPEN ∏ i = 1 n j i ) n if ​ α = 1 w_{\alpha}(j_{1},\ldots,j_{n})=\begin{cases}\left(\frac{1}{n}\sum_{i=1}^{n}j_{i}^ -->

**EN** –one can sweep the parameter ⟦SLOT_101⟧ to change the inequality aversion from a fully Utilitarian objective (⟦SLOT_102⟧) to a max-min/Rawlsian objective (⟦SLOT_103⟧) (Bakker et al., 2022). Alternatively, one could modify the utility functions as follows ⟦SLOT_104⟧ to reduce the objective to a MAX-SAT problem. Equilibria and minimax solutions (Harsanyi et al., 1988) are also possible, e.g. (Swamy et al., 2024).

**ZH** ——可以扫描参数 ⟦SLOT_101⟧，把不平等厌恶从完全功利主义的目标（⟦SLOT_102⟧）改变为最大最小／罗尔斯式的目标（⟦SLOT_103⟧）（Bakker 等，2022）。或者，可以按如下方式修改效用函数 ⟦SLOT_104⟧，把目标归约为一个 MAX-SAT 问题。均衡与极小极大解（Harsanyi 等，1988）也是可能的，例如（Swamy 等，2024）。

**EN** Limitations The main limitation to this approach is that precisely estimating the individual juror’s functions may require a large amount of data, although this could be mitigated by grouping by salient characteristics (e.g., nationality (Aroyo et al., 2023)) or using sample efficient methods (Liu et al., 2023). Depending on the choice of welfare function, other limitations may apply: e.g., majoritarian welfare functions could be susceptible to tyranny of the majority and Utilitarian welfare functions to fanatical influence (MacAskill, 2016). This approach also assumes commensurability. Reported values also might not be comparable on the same scale (Ethayarajh & Jurafsky, 2022).

**ZH** 局限 这一路径的主要局限是，精确估计个体陪审员的函数可能需要大量数据，尽管可以通过按显著特征（例如国籍（Aroyo 等，2023））分组或使用高样本效率的方法（Liu 等，2023）来缓解。根据福利函数的选择，还可能适用其他局限：例如，多数主义福利函数可能易受多数暴政影响，功利主义福利函数则易受狂热影响（MacAskill，2016）。这一路径也假定了可通约性。报告的值也可能无法在同一尺度上比较（Ethayarajh & Jurafsky，2022）。

**EN** Alignment Procedures and Recommendations Once we have our jury ⟦SLOT_105⟧ and a welfare function ⟦SLOT_106⟧ defined, the problem reduces to one of reward maximization, and we can leverage established alignment techniques. The main novelty of the framework is in the reward modeling through a jury. We therefore recommend further research into the questions of 1) who to represent on a jury, 2) how to estimate juror functions, and 3) establishing jury-pluralistic benchmarks to spur further innovation.

**ZH** 对齐程序与建议 一旦我们定义了陪审团 ⟦SLOT_105⟧ 与福利函数 ⟦SLOT_106⟧，问题就归约为奖励最大化，我们可以沿用既有的对齐技术。该框架的主要新颖之处在于通过陪审团进行奖励建模。因此我们建议进一步研究以下问题：1）陪审团中应代表谁；2）如何估计陪审员函数；3）建立陪审团多元基准以推动更多创新。

**EN** 5 Current Alignment Approaches and Pluralism

**ZH** 5 当前对齐路径与多元性

**EN** 5.1 Current Alignment Approaches

**ZH** 5.1 当前对齐路径

**EN** AI alignment aims to guide a LLM in the direction of human intentions and values, such as safety and accuracy (Leike et al., 2018; Ji et al., 2024). In supervised fine-tuning, models are trained to improve instruction following (Touvron et al., 2023; Brown et al., 2020; Achiam et al., 2023) or express certain values (Solaiman & Dennison, 2021). RLHF uses a reward model trained on human ratings of model-generated data to steer a model to maximize human preferences (Ouyang et al., 2022; Anthropic, 2023). Controllable decoding steers an LLM’s output towards an objective at inference (Liu et al., 2024; Liu et al., 2021; Qin et al., 2022), but often fall short of learning-based methods on alignment benchmarks and have not been explored with pluralism. The degree of pluralism of models resulting from these approaches depends on many factors, including: the representativeness of the people building the models, from designers to annotators (Cotra, 2021; Perez et al., 2022; Bobu et al., 2023; Peng et al., 2023); the richness of a dataset/LM/reward model (Casper et al., 2023); and other factors. Mishra (2023) argues that monistic approaches to RLHF cannot meet certain democratic properties and Siththaranjan et al. (2023) find that RLHF underweights outliers.

**ZH** AI 对齐旨在把 LLM 引导到人类意图与价值观的方向，例如安全性与准确性（Leike 等，2018；Ji 等，2024）。在监督微调中，模型被训练以提升指令遵循能力（Touvron 等，2023；Brown 等，2020；Achiam 等，2023）或表达某些价值（Solaiman & Dennison，2021）。RLHF 使用一个在人类对模型生成数据的评分上训练的奖励模型，引导模型最大化人类偏好（Ouyang 等，2022；Anthropic，2023）。可控解码在推理时把 LLM 的输出导向某个目标（Liu 等，2024；Liu 等，2021；Qin 等，2022），但在对齐基准上往往逊于基于学习的方法，且尚未在多元性语境下被探索。这些方法所得模型的多元性程度取决于许多因素，包括：构建模型的人群（从设计者到标注者）是否具有代表性（Cotra，2021；Perez 等，2022；Bobu 等，2023；Peng 等，2023）；数据集／语言模型／奖励模型的丰富程度（Casper 等，2023）；以及其他因素。Mishra（2023）认为，RLHF 的一元化路径无法满足某些民主属性；Siththaranjan 等（2023）发现 RLHF 低估离群者。

**EN** 5.2 Current Approaches and Pluralism

**ZH** 5.2 当前路径与多元性

<!-- [原子块 · table] Model Class LLaMA LLaMA2 (7B) LLaMA2 (13B) Gemma (7B) GPT-3 Dataset Pre Alpaca Tulu Pre Post Pre Post Pre Post Pre Post GlobalQA (Japan) 0.40 0.45 0.54 0.47 0.57 0.40 0.55 0.33 0.51 0.42 0.43 GlobalQA -->

**EN** Table 1: Jensen-Shannon distance (similarity) between human and model distributions on GlobalQA (target human distributions of Japan, US, and Germany) and MPI. Note that we compare two “post" RLHF models for LLaMA (Alpaca and Tulu). Smaller (more similar) values are in bold.

**ZH** 表 1：人类分布与模型分布在 GlobalQA（目标人类分布为日本、美国与德国）与 MPI 上的 Jensen-Shannon 距离（相似度）。注意我们对 LLaMA 比较了两个「对齐后」的 RLHF 模型（Alpaca 与 Tulu）。数值越小（越相似）以粗体显示。

**EN** Hypothesis: Current LLM alignment techniques can reduce distributional pluralism w.r.t. the population of internet users.

**ZH** 假设：当前的 LLM 对齐技术可能降低相对于互联网用户人群的分布多元性。

**EN** Theoretical aspect: The language modeling cross entropy objective may help models learn distributional pluralism. If query ⟦SLOT_107⟧ with response ⟦SLOT_108⟧ appears many times in the training data written by a random internet users, cross entropy encourages the model to output ⟦SLOT_109⟧ in proportion to the population (Ji et al., 2021) 22 2 This may be complicated by factors such as overfitting (with ⟦SLOT_110⟧ epoch) or textual features which hint at the response; however, within tolerance, we believe this to be a descriptive analogy.. Moreover, we postulate that current alignment techniques can reduce distributional pluralism, as the alignment procedure does not have this property.

**ZH** 理论方面：语言建模的交叉熵目标可能帮助模型学习分布多元性。如果查询 ⟦SLOT_107⟧ 连同回答 ⟦SLOT_108⟧ 在由随机互联网用户书写的训练数据中多次出现，交叉熵会鼓励模型按人群比例输出 ⟦SLOT_109⟧（Ji 等，2021）（脚注 2：这可能被过拟合（⟦SLOT_110⟧ 个周期）或提示回答的文本特征等因素复杂化；不过在容差范围内，我们相信这是一个描述性的类比。）。此外，我们假定当前的对齐技术会降低分布多元性，因为对齐程序并不具备这一性质。

**EN** Empirical aspect: We rely on three empirical findings that provide an initial indication of support for our hypothesis. Firstly, in work by Santurkar et al. (2023), questions from Pew Research’s American Trends Panels survey data (OpinionQA) were utilized to compare the distribution of LLM responses to those of US citizens. Two different model classes (Jurassic/GPT-3) with both pre- and post-aligned models were compared. The results revealed that post-aligned models exhibited less similarity to human populations compared to pre-aligned models. Expanding beyond the U.S., Durmus et al. (2023) introduced GlobalOpinionQA, an aggregation of multinational World Values similar to OpinionQA. Although their focus was solely on post-aligned models, they observed that these models tended to concentrate the probability mass on a few answer choices, in contrast to the dispersed answers seen in their human distributions.

**ZH** 实证方面：我们依赖三项实证发现，为我们的假设提供初步支持。首先，在 Santurkar 等（2023）的工作中，研究者利用皮尤研究中心美国趋势面板调查数据（OpinionQA）中的问题，比较 LLM 回答的分布与美国公民的分布。他们比较了两类不同的模型（Jurassic／GPT-3），各含对齐前与对齐后版本。结果显示，对齐后的模型相比对齐前的模型，与人群的相似度更低。除美国之外，Durmus 等（2023）提出了 GlobalOpinionQA，一个类似 OpinionQA 的跨国世界价值观聚合数据集。尽管他们只关注对齐后的模型，他们观察到这些模型倾向于把概率质量集中在少数几个答案选项上，与人类分布的分散回答形成对照。

**EN** In an effort to expand on these works, we further tested33 3 Code can be found at: https://github.com/jfisher52/AI_Pluralistic_Alignment a suite of vanilla pretrained LLMs in comparison to their corresponding “aligned" counterparts (RLHFed, finetuned LLMs) from three model classes, LLaMA(2), Gemma, and GPT-3. These evaluations were conducted on two distinct multiple-choice datasets: GlobalOpinionQA, as utilized in the study by Durmus et al. (2023), and the Machine Personality Inventory (MPI), comprising 120 questions designed to assess human personality traits (Jiang et al., 2023). 44 4 An analysis’s strength of distributional pluralism w.r.t. a population depends on the degree of representativeness of the sample. We refer interested readers to the original dataset documentation. Our target distributions were Japan and the US citizens for GlobalOpinionQA 55 5 We included the U.S. due to LLMs being largely trained on English from the U.S. and selected Japan as a nation with a somewhat distinct culture (JS-distance of .26). The choice of two nations was made due to incomplete overlap between country pairs. and a global population for the MPI. We calculate Jensen-Shannon distance between the human the model distributions, averaged over 5 prompts.

**ZH** 为拓展这些工作，我们进一步测试了（脚注 3：代码见：https://github.com/jfisher52/AI_Pluralistic_Alignment）一组原始预训练 LLM，与来自 LLaMA(2)、Gemma 与 GPT-3 三个模型类别的对应「已对齐」版本（经 RLHF、微调的 LLM）作比较。这些评测在两个不同的多项选择数据集上进行：Durmus 等（2023）研究中使用的 GlobalOpinionQA，以及机器人格量表（MPI）——后者包含 120 道用于评估人类人格特质的问题（Jiang 等，2023）。（脚注 4：一项关于某人群的分布多元性分析的强度，取决于样本的代表性程度。我们请感兴趣的读者参阅原始数据集文档。）我们的目标分布是 GlobalOpinionQA 的日本与美国公民（脚注 5：我们纳入美国，是因为 LLM 主要在来自美国的英语上训练；选择日本则是因为它是一个文化上较为独特的国家（JS 距离为 .26）。选择两个国家是因为国家两两之间的重叠不完整。），以及 MPI 的全球人群。我们计算人类分布与模型分布之间的 Jensen-Shannon 距离，在 5 个提示上取平均。

**EN** As shown in Table 1, almost all pre-aligned models have lower Jensen-Shannon distance to the target human distribution than the post-aligned models for both datasets.66 6 The only exception is for GPT-3 on MPI. However, OpenAI now only provides ”davinci-02” and ”gpt-3.5-turbo” as opposed to the original ”davinci” and ”*-instruct” series models, so it is difficult to confirm if ”davinci-002” is indeed the base model or what procedure was done to ”gpt-3.5-turbo”. Thus, we encourage interpretion of the GPT-3 results with caution. Additionally, we also observed a post-alignment reduction in entropy, as reported in previous work (Santurkar et al., 2023; Durmus et al., 2023). More details can be found in App. A and B.

**ZH** 如表 1 所示，在两个数据集上，几乎所有对齐前的模型到目标人类分布的 Jensen-Shannon 距离都低于对齐后的模型。（脚注 6：唯一的例外是 GPT-3 在 MPI 上。然而 OpenAI 现在只提供 “davinci-02” 与 “gpt-3.5-turbo”，而非原始的 “davinci” 与 “*-instruct” 系列模型，因此难以确认 “davinci-002” 是否确为基础模型，或对 “gpt-3.5-turbo” 做了何种处理。因此我们建议谨慎解读 GPT-3 的结果。）此外，我们也观察到对齐后熵的下降，这与先前工作一致（Santurkar 等，2023；Durmus 等，2023）。更多细节见附录 A 与 B。

**EN** These studies reveal a consistent pattern of reduced distributional variance following alignment across various domains. Therefore, when the target distribution is diverse, such as internet users, current alignment techniques may potentially limit distributional pluralism. However, a more comprehensive investigation of this hypothesis requires large-scale experimentation across a broader range of domains, along with further exploration into the role of entropy.

**ZH** 这些研究揭示了一个一致的模式：在多个领域上，对齐之后分布方差都会降低。因此，当目标分布是多样的（例如互联网用户），当前的对齐技术可能会限制分布多元性。不过，对这一假设更全面的考察需要跨更广领域的大规模实验，以及对熵的作用做进一步探索。

**EN** Current alignment techniques and other forms of pluralism. Overton pluralism may emerge to the degree that users prefer it, but people’s preference bias for assertiveness (Hosking et al., 2023; Zhou et al., 2024) may work against this, causing models to express support inconsistently (Krügel et al., 2023). LLMs may have a degree of steerable pluralism via prompting, but this needs to be further evaluated. Alignment techniques for all kinds of pluralistic benchmarks warrant further investigation.

**ZH** 当前对齐技术与其他形态的多元性。Overton 多元性可能在用户偏好的程度上出现，但人们对自信断言的偏好偏置（Hosking 等，2023；Zhou 等，2024）可能与之相悖，导致模型表达支持的方式前后不一（Krügel 等，2023）。LLM 通过提示可能具备一定程度的可引导多元性，但这需要进一步评估。面向各类多元基准的对齐技术都值得进一步研究。

**EN** 6 Discussion

**ZH** 6 讨论

**EN** 6.1 Limitations

**ZH** 6.1 局限

**EN** In this work, we 1) argue that current approaches are unclear regarding to whom/what is being aligned and 2) formalize and discuss a set of frameworks to operationalize how to better align models to a set of values, characteristics, or perspectives. However, the goal of this work is not to delineate exactly to whom or what to align, but rather to argue for clearer, more pluralistic approaches in alignment.

**ZH** 在这项工作中，我们 1）论证当前路径在对齐对象（对谁／对什么）上不清晰，2）形式化并讨论一组框架，以落实如何把模型更好地对齐到一组价值、特征或视角。然而，本文的目标不是精确划定对齐的对象，而是倡导在对齐中采用更清晰、更多元的路径。

**EN** Nevertheless, several of our definitions are hard to operationalize (e.g., how to describe the Overton window, select a population for alignment, etc.). We acknowledge this and believe that this is a necessary difficulty in order to be precise in measuring pluralism. We attempted to make our definitions a useful abstraction: “as simple as possible, but not simpler" (Ratcliffe, 2016). Further abstracting away these details would remove the required nuance of the evaluations. Any design decisions, along with their limitations and assumptions, must be carefully justified. Although some alignment techniques may require automatic methods (e.g., jury functions), we advocate for human-centered evaluations whenever possible.

**ZH** 尽管如此，我们的若干定义难以落实（例如如何描述 Overton 窗口、如何选择对齐的人群等）。我们承认这一点，并认为这是为了精确度量多元性而必须承受的困难。我们试图把定义做成一种有用的抽象：「尽可能简单，但不能更简单」（Ratcliffe，2016）。进一步抽象掉这些细节会剥夺评测所需的细微之处。任何设计决策及其局限与假设都必须被仔细论证。尽管某些对齐技术可能需要自动化方法（例如陪审团函数），我们仍倡导尽可能采用以人为中心的评测。

**EN** We recognize that not all of our definitions of pluralism are necessarily desirable in all cases. For example, distributional pluralism may be helpful in using LLMs to study culture (Buttrick, 2024) or creative domains (Shanahan & Clarke, 2023), but may not be desirable in controlled environments such as customer support. Additionally, it may not be possible for a single model to satisfy all conditions: e.g., Overton pluralism may be at odds with distributional pluralism. Rather, our definitions are useful abstractions to understand how models and benchmarks can be pluralistic, and each applies in a different domain.

**ZH** 我们认识到，并非我们所有的多元性定义在所有情形下都是可取的。例如，分布多元性在把 LLM 用于研究文化（Buttrick，2024）或创意领域（Shanahan & Clarke，2023）时可能有益，但在客户服务等受控环境中可能并不理想。此外，单一模型可能无法满足所有条件：例如 Overton 多元性可能与分布多元性相冲突。相反，我们的定义是有用的抽象，用于理解模型与基准如何做到多元，各自适用于不同领域。

**EN** 6.2 Relation to Prior Work

**ZH** 6.2 与先前工作的关系

**EN** There has been a growing sense in the community of the importance of measuring which values and to whom we are trying to align LLMs (Kasirzadeh & Gabriel, 2022; Wang et al., 2023b). While some previous work has shed valuable light on these questions (Santurkar et al., 2023), our work goes further in 1) unifying disparate approaches under concrete definitions of pluralism (e.g., distributional), 2) proposing previously unexplored (to our knowledge) kinds of pluralism (e.g., Overton), and 3) arguing that, in many cases, it may actually be desirable to increase certain measures of pluralism as opposed to merely using them as probes, in contrast to other work (Santurkar et al., 2023; Durmus et al., 2023; Feng et al., 2023).

**ZH** 社区中日益形成共识：度量我们试图把 LLM 对齐到哪些价值、对齐给谁，十分重要（Kasirzadeh & Gabriel，2022；Wang 等，2023b）。尽管一些先前工作为这些问题提供了有价值的启示（Santurkar 等，2023），我们的工作进一步做到了：1）在具体的多元性定义（例如分布多元性）之下统一了各不相同的路径；2）提出了（据我们所知）此前未被探索的多元性类型（例如 Overton 多元性）；3）论证在许多情形下，提升某些多元性度量可能确实是可取的，而不只是把它们当作探针使用——这一点与其他工作形成对照（Santurkar 等，2023；Durmus 等，2023；Feng 等，2023）。

**EN** 6.3 Pluralism in Broader AI Systems

**ZH** 6.3 更广泛 AI 系统中的多元性

**EN** In this work, we focused largely on LLMs. However, we believe that our definitions generalize broadly to other AI systems. In general, the query/response framework may be applied to any set of inputs/outputs, whether actions, images, audio, or any other modality. For example, it may be desirable for agents to be steerably pluralistic to be able to customize to users needs. Distributional pluralism may be useful in modeling potential actions that agents may take, such as drivers on a road. There may be less of a need for pluralism in areas where there is a single correct objective to optimize - e.g., efficiency of a system, performance in a 2-player game. However, there is a broad set of subjective tasks where pluralism is a valuable consideration.

**ZH** 本工作中我们主要聚焦 LLM。然而我们相信，我们的定义可广泛推广到其他 AI 系统。一般而言，查询／回答框架可应用于任何输入／输出集合，无论是动作、图像、音频还是其他模态。例如，智能体可能需要在可引导多元性上有所表现，以便定制到用户需求。分布多元性在建模智能体可能采取的潜在动作时可能有用，例如道路上的驾驶员。在只有单一正确目标需要优化的领域（例如系统效率、双人博弈中的表现），对多元性的需求可能较小。然而，在大量主观性任务中，多元性是一项值得考虑的要素。

**EN** 7 Conclusion

**ZH** 7 结论

**EN** In this work, we have argued for increased and more precisely-directed attention on pluralism and the alignment of AI systems. We also formalized three definitions of pluralistic models and three forms of pluralistic benchmarks. We argue that while current alignment techniques have made remarkable progress, new methodologies for measuring and aligning are needed.

**ZH** 在本工作中，我们主张对多元性与 AI 系统对齐给予更多、更精准定向的关注。我们还形式化了多元模型的三个定义与多元基准的三种形态。我们认为，尽管当前的对齐技术已取得长足进步，仍需要用于度量与对齐的新方法。

**EN** While we thread specific recommendations for each kind of pluralism throughout the work, we sketch some broad recommendations here: 1) more research into finegrained pluralistic evaluations to better characterize current models; 2) continued normative discussions about to what we want to align and desirable customization bounds; 3) additional alignment techniques to create more pluralistic models.

**ZH** 尽管我们在全文针对每类多元性穿插了具体建议，这里仍勾勒若干宏观建议：1）更多研究细粒度的多元评测，以更好地刻画当前模型；2）持续就我们希望对齐到什么、可取的定制化边界开展规范性讨论；3）提出额外的对齐技术，以创造更具多元性的模型。

**EN** Impact Statement

**ZH** 影响声明

**EN** We hope that this work leads to positive impact in encouraging work in AI systems that work better with a diverse set of people. Throughout the work, we have discussed potential limitations and risks for each proposed definition. Additionally, this work, along with any other work in machine learning, has potential for dual use: aligning to attributes which may cause harm, etc. However, as our work is more theoretical, we believe that the positive impact to discussions around pluralism in alignment outweigh any marginal potential for dual use, which we believe to be minimal.

**ZH** 我们希望本工作带来积极影响，推动 AI 系统更好地服务多样化人群的研究。全文我们已针对每个提出的定义讨论了潜在局限与风险。此外，本工作与任何其他机器学习工作一样，存在双重用途的可能：例如对齐到可能造成伤害的属性。然而，由于我们的工作更偏理论性，我们认为它对围绕对齐中多元性的讨论所产生的积极影响，超过了任何微小的双重用途可能，而我们相信后者是极小的。

**EN** Acknowledgments

**ZH** 致谢

**EN** The authors thank Ben Newman, Joongwon Kim, Victoria Ebert, Zaid Harchaoui, and Iason Gabriel for helpful feedback. This research was supported in part by DARPA under the ITM program (FA8650-23-C-7316), the Office of Naval Research (N00014-24-1-2207), the Institute for Humane Studies (IHS018186), and the Allen Institute for AI.

**ZH** 作者感谢 Ben Newman、Joongwon Kim、Victoria Ebert、Zaid Harchaoui 与 Iason Gabriel 提供的有益反馈。本研究部分由 DARPA 的 ITM 项目（FA8650-23-C-7316）、海军研究办公室（N00014-24-1-2207）、人文研究所（IHS018186）与艾伦人工智能研究所资助。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] OED (2023) Oxford English Dictionary, s.v. “Overton window (n.)”, July 2023. URL https://doi.org/10.1093/OED/1985277434 . -->

<!-- [原子块 · verbatim] Achiam et al. (2023) Achiam, O. J., Adler, S., Agarwal, S., Ahmad, L., Akkaya, I., Aleman, F. L., Almeida, D., Altenschmidt, J., Altman, S., Anadkat, S., Avila, R., Babuschkin, I., Balaji, S., Balcom, -->

<!-- [原子块 · verbatim] Aher et al. (2023) Aher, G. V., Arriaga, R. I., and Kalai, A. T. Using large language models to simulate multiple humans and replicate human subject studies. In International Conference on Machine Lea -->

<!-- [原子块 · verbatim] Anthropic (2023) Anthropic. Introducing claude, 2023. URL https://www.anthropic.com/index/introducing-claude . -->

<!-- [原子块 · verbatim] Argyle et al. (2023) Argyle, L., Busby, E., Fulda, N., Gubler, J., Rytting, C., and Wingate, D. Out of one, many: Using language models to simulate human samples. Political Analysis , 31:1–15, 02 2023 -->

<!-- [原子块 · verbatim] Arnesen & Peters (2018) Arnesen, S. and Peters, Y. The legitimacy of representation: How descriptive, formal, and responsiveness representation affect the acceptability of political decisions. Compara -->

<!-- [原子块 · verbatim] Aroyo et al. (2023) Aroyo, L., Taylor, A. S., Diaz, M., Homan, C. M., Parrish, A., Serapio-Garcia, G., Prabhakaran, V., and Wang, D. Dices dataset: Diversity in conversational ai evaluation for safety -->

<!-- [原子块 · verbatim] Askell et al. (2021) Askell, A., Bai, Y., Chen, A., Drain, D., Ganguli, D., Henighan, T., Jones, A., Joseph, N., Mann, B., DasSarma, N., Elhage, N., Hatfield-Dodds, Z., Hernandez, D., Kernion, J., Ndo -->

<!-- [原子块 · verbatim] Bai et al. (2022a) Bai, Y., Jones, A., Ndousse, K., Askell, A., Chen, A., DasSarma, N., Drain, D., Fort, S., Ganguli, D., Henighan, T., Joseph, N., Kadavath, S., Kernion, J., Conerly, T., El-Showk, S. -->

<!-- [原子块 · verbatim] Bai et al. (2022b) Bai, Y., Kadavath, S., Kundu, S., Askell, A., Kernion, J., Jones, A., Chen, A., Goldie, A., Mirhoseini, A., McKinnon, C., Chen, C., Olsson, C., Olah, C., Hernandez, D., Drain, D., G -->

<!-- [原子块 · verbatim] Bakker et al. (2022) Bakker, M. A., Chadwick, M. J., Sheahan, H. R., Tessler, M. H., Campbell-Gillingham, L., Balaguer, J., McAleese, N., Glaese, A., Aslanides, J., Botvinick, M. M., and Summerfield,  -->

<!-- [原子块 · verbatim] Berlin (1969) Berlin, I. Two concepts of liberty. In Four Essays on Liberty , pp. 118–172. Oxford University Press, Oxford, 1969. -->

<!-- [原子块 · verbatim] Bobu et al. (2023) Bobu, A., Peng, A., Agrawal, P., Shah, J., and Dragan, A. D. Aligning robot and human representations. arXiv preprint arXiv:2302.01928 , 2023. -->

<!-- [原子块 · verbatim] Bommasani et al. (2021) Bommasani, R., Hudson, D. A., Adeli, E., Altman, R., Arora, S., von Arx, S., Bernstein, M. S., Bohg, J., Bosselut, A., Brunskill, E., Brynjolfsson, E., Buch, S., Card, D., Cast -->

<!-- [原子块 · verbatim] Bowman et al. (2022) Bowman, S. R., Hyun, J., Perez, E., Chen, E., Pettit, C., Heiner, S., Lukošiūtė, K., Askell, A., Jones, A., Chen, A., Goldie, A., Mirhoseini, A., McKinnon, C., Olah, C., Amodei, D -->

<!-- [原子块 · verbatim] Boykoff & Boykoff (2004) Boykoff, M. T. and Boykoff, J. M. Balance as bias: global warming and the us prestige press. Global Environmental Change , 14(2):125–136, 2004. ISSN 0959-3780. doi: https://do -->

<!-- [原子块 · verbatim] Brown et al. (2020) Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G., Askell, A., Agarwal, S., Herbert-Voss, A., Krueger, G., Henighan,  -->

<!-- [原子块 · verbatim] Buttrick (2024) Buttrick, N. Studying large language models as compression algorithms for human culture. Trends in Cognitive Sciences , S1364-6613(24):00001–9, 2024. doi: 10.1016/j.tics.2024.01.001 .  -->

<!-- [原子块 · verbatim] Casper et al. (2023) Casper, S., Davies, X., Shi, C., Gilbert, T. K., Scheurer, J., Rando, J., Freedman, R., Korbak, T., Lindner, D., Freire, P., Wang, T., Marks, S., Ségerie, C.-R., Carroll, M., Peng -->

<!-- [原子块 · verbatim] Chen et al. (2023) Chen, J., Liu, Z., Huang, X., Wu, C., Liu, Q., Jiang, G., Pu, Y., Lei, Y., Chen, X., Wang, X., Lian, D., and Chen, E. When large language models meet personalization: Perspectives o -->

<!-- [原子块 · verbatim] Chen et al. (2021) Chen, L., Lu, K., Rajeswaran, A., Lee, K., Grover, A., Laskin, M., Abbeel, P., Srinivas, A., and Mordatch, I. Decision transformer: Reinforcement learning via sequence modeling, 202 -->

<!-- [原子块 · verbatim] Cotra (2021) Cotra, A. Why ai alignment could be hard with modern deep learning. https://www.cold-takes.com/why-ai-alignment-could-be-hard-with-modern-deep-learning/ , 2021. -->

<!-- [原子块 · verbatim] Crenshaw (1989) Crenshaw, K. Demarginalizing the intersection of race and sex: A black feminist critique of antidiscrimination doctrine, feminist theory and antiracist politics. The University of Chic -->

<!-- [原子块 · verbatim] Danry et al. (2023) Danry, V., Pataranutaporn, P., Mao, Y., and Maes, P. Don’t just tell me, ask me: Ai systems that intelligently frame explanations as questions improve human logical discernment acc -->

<!-- [原子块 · verbatim] de Tocqueville (1835) de Tocqueville, A. Democracy in America . 1835. -->

<!-- [原子块 · verbatim] Durmus et al. (2023) Durmus, E., Nyugen, K., Liao, T. I., Schiefer, N., Askell, A., Bakhtin, A., Chen, C., Hatfield-Dodds, Z., Hernandez, D., Joseph, N., Lovitt, L., McCandlish, S., Sikder, O., Tamkin -->

<!-- [原子块 · verbatim] Ethayarajh & Jurafsky (2020) Ethayarajh, K. and Jurafsky, D. Utility is in the eye of the user: A critique of nlp leaderboard design. In Conference on Empirical Methods in Natural Language Processing  -->

<!-- [原子块 · verbatim] Ethayarajh & Jurafsky (2022) Ethayarajh, K. and Jurafsky, D. The authenticity gap in human evaluation. In Goldberg, Y., Kozareva, Z., and Zhang, Y. (eds.), Proceedings of the 2022 Conference on Empiri -->

<!-- [原子块 · verbatim] Feng et al. (2023) Feng, S., Park, C. Y., Liu, Y., and Tsvetkov, Y. From pretraining data to language models to downstream tasks: Tracking the trails of political biases leading to unfair nlp models,  -->

<!-- [原子块 · verbatim] Flanigan et al. (2021) Flanigan, B., Gölz, P., Gupta, A., Hennig, B., and Procaccia, A. D. Fair algorithms for selecting citizens’assemblies. Nature , 596(7873):548–552, 2021. doi: 10.1038/s41586-021- -->

<!-- [原子块 · verbatim] Fleisig et al. (2023) Fleisig, E., Abebe, R., and Klein, D. When the Majority is Wrong: Modeling Annotator Disagreement for Subjective Tasks, November 2023. URL http://arxiv.org/abs/2305.06626 . arXiv -->

<!-- [原子块 · verbatim] Gabriel (2020) Gabriel, I. Artificial intelligence, values, and alignment. Minds and Machines , 30(3):411–437, 2020. doi: 10.1007/s11023-020-09539-2 . URL https://doi.org/10.1007/s11023-020-09539-2 . -->

<!-- [原子块 · verbatim] Girotra et al. (2023) Girotra, K., Meincke, L., Terwiesch, C., and Ulrich, K. T. Ideas are dimes a dozen: Large language models for idea generation in innovation. https://ssrn.com/abstract=4526071 , J -->

<!-- [原子块 · verbatim] Glaese et al. (2022) Glaese, A., McAleese, N., Trębacz, M., Aslanides, J., Firoiu, V., Ewalds, T., Rauh, M., Weidinger, L., Chadwick, M., Thacker, P., Campbell-Gillingham, L., Uesato, J., Huang, P.-S. -->

<!-- [原子块 · verbatim] Gordon et al. (2022) Gordon, M. L., Lam, M. S., Park, J. S., Patel, K., Hancock, J., Hashimoto, T., and Bernstein, M. S. Jury learning: Integrating dissenting voices into machine learning models. In C -->

<!-- [原子块 · verbatim] Guerreiro et al. (2020) Guerreiro, A. P., Fonseca, C. M., and Paquete, L. The hypervolume indicator. ACM Computing Surveys (CSUR) , 54:1–42, 2020. URL https://api.semanticscholar.org/CorpusID:21847018 -->

<!-- [原子块 · verbatim] Haraway (1988) Haraway, D. Situated knowledges: The science question in feminism and the privilege of partial perspective. Feminist Studies , 14(3):575–599, 1988. ISSN 00463663. URL http://www.jstor.o -->

<!-- [原子块 · verbatim] Harsanyi et al. (1988) Harsanyi, J. C., Selten, R., et al. A general theory of equilibrium selection in games. MIT Press Books , 1, 1988. -->

<!-- [原子块 · verbatim] Hartmann et al. (2023) Hartmann, J., Schwenzow, J., and Witte, M. The political ideology of conversational ai: Converging evidence on chatgpt’s pro-environmental, left-libertarian orientation, 2023. -->

<!-- [原子块 · verbatim] Hayati et al. (2023) Hayati, S. A., Lee, M., Rajagopal, D., and Kang, D. How far can we extract diverse perspectives from large language models? criteria-based diversity prompting! ArXiv , abs/2311.09 -->

<!-- [原子块 · verbatim] Hayes et al. (2022) Hayes, C. F., Rădulescu, R., Bargiacchi, E., Källström, J., Macfarlane, M., Reymond, M., Verstraeten, T., Zintgraf, L. M., Dazeley, R., Heintz, F., Howley, E., Irissappane, A. A.,  -->

<!-- [原子块 · verbatim] Hendrycks et al. (2020) Hendrycks, D., Burns, C., Basart, S., Critch, A., Li, J., Song, D., and Steinhardt, J. Aligning ai with shared human values. arXiv preprint arXiv:2008.02275 , 2020. -->

<!-- [原子块 · verbatim] Hendrycks et al. (2023) Hendrycks, D., Burns, C., Basart, S., Critch, A., Li, J., Song, D., and Steinhardt, J. Aligning ai with shared human values, 2023. -->

<!-- [原子块 · verbatim] Henrich et al. (2010) Henrich, J., Heine, S. J., and Norenzayan, A. The weirdest people in the world? Behavioral and Brain Sciences , 33(2-3):61–83, 2010. URL http://www2.psych.ubc.ca/~henrich/audiofi -->

<!-- [原子块 · verbatim] Hosking et al. (2023) Hosking, T., Blunsom, P., and Bartolo, M. Human feedback is not gold standard. ArXiv , abs/2309.16349, 2023. URL https://api.semanticscholar.org/CorpusID:263134280 . -->

<!-- [原子块 · verbatim] Hsieh & Andersson (2021) Hsieh, N.-h. and Andersson, H. Incommensurable Values. In Zalta, E. N. (ed.), The Stanford Encyclopedia of Philosophy . Metaphysics Research Lab, Stanford University, Fall 202 -->

<!-- [原子块 · verbatim] Hwang et al. (2023) Hwang, E., Majumder, B. P., and Tandon, N. Aligning Language Models to User Opinions. 2023. doi: 10.48550/ARXIV.2305.14929 . URL https://arxiv.org/abs/2305.14929 . Publisher: arXiv -->

<!-- [原子块 · verbatim] Imundo & Rapp (2021) Imundo, M. and Rapp, D. When fairness is flawed: Effects of false balance reporting and weight-of-evidence statements on beliefs and perceptions of climate change. Journal of Appl -->

<!-- [原子块 · verbatim] Jakesch et al. (2023) Jakesch, M., Bhat, A., Buschek, D., Zalmanson, L., and Naaman, M. Co-writing with opinionated language models affects users’ views. In Proceedings of the 2023 CHI Conference on H -->

<!-- [原子块 · verbatim] Jang et al. (2023) Jang, J., Kim, S., Lin, B. Y., Wang, Y., Hessel, J., Zettlemoyer, L., Hajishirzi, H., Choi, Y., and Ammanabrolu, P. Personalized soups: Personalized large language model alignment v -->

<!-- [原子块 · verbatim] Ji et al. (2024) Ji, J., Qiu, T., Chen, B., Zhang, B., Lou, H., Wang, K., Duan, Y., He, Z., Zhou, J., Zhang, Z., Zeng, F., Ng, K. Y., Dai, J., Pan, X., O’Gara, A., Lei, Y., Xu, H., Tse, B., Fu, J., Mc -->

<!-- [原子块 · verbatim] Ji et al. (2021) Ji, Z., Li, J. D., and Telgarsky, M. Early-stopped neural networks are consistent, 2021. -->

<!-- [原子块 · verbatim] Jiang et al. (2023) Jiang, G., Xu, M., Zhu, S.-C., Han, W., Zhang, C., and Zhu, Y. Evaluating and inducing personality in pre-trained language models, 2023. URL https://api.semanticscholar.org/CorpusI -->

<!-- [原子块 · verbatim] Jiang et al. (2022) Jiang, H., Beeferman, D., Roy, B., and Roy, D. Communitylm: Probing partisan worldviews from language models, 2022. -->

<!-- [原子块 · verbatim] Jung et al. (2022) Jung, J., Qin, L., Welleck, S., Brahman, F., Bhagavatula, C., Bras, R. L., and Choi, Y. Maieutic prompting: Logically consistent reasoning with recursive explanations, 2022. -->

<!-- [原子块 · verbatim] Kant (1788) Kant, I. Kant: Critique of Practical Reason . Cambridge Texts in the History of Philosophy. Cambridge University Press, 2 edition, 1788. doi: 10.1017/CBO9781316136478 . -->

<!-- [原子块 · verbatim] Kasirzadeh & Gabriel (2022) Kasirzadeh, A. and Gabriel, I. In conversation with artificial intelligence: aligning language models with human values, 2022. -->

<!-- [原子块 · verbatim] Kekes (1993) Kekes, J. The Morality of Pluralism . Princeton University Press, Princeton, 1993. -->

<!-- [原子块 · verbatim] Kim & Lee (2023) Kim, J. and Lee, B. Ai-augmented surveys: Leveraging large language models for opinion prediction in nationally representative surveys. arXiv preprint arXiv:2305.09620 , 2023. -->

<!-- [原子块 · verbatim] Kirk et al. (2024) Kirk, R., Mediratta, I., Nalmpantis, C., Luketina, J., Hambro, E., Grefenstette, E., and Raileanu, R. Understanding the effects of rlhf on llm generalisation and diversity, 2024. -->

<!-- [原子块 · verbatim] Koster et al. (2022) Koster, R., Balaguer, J., Tacchetti, A., Weinstein, A., Zhu, T., Hauser, O., Williams, D., Campbell-Gillingham, L., Thacker, P., Botvinick, M., and Summerfield, C. Human-centred m -->

<!-- [原子块 · verbatim] Krügel et al. (2023) Krügel, S., Ostermaier, A., and Uhl, M. Chatgpt’s inconsistent moral advice influences users’judgment. Scientific Reports , 13(1):4569, Apr 2023. ISSN 2045-2322. doi: 10.1038/s415 -->

<!-- [原子块 · verbatim] Landemore & Page (2015) Landemore, H. and Page, S. E. Deliberation and disagreement: Problem solving, prediction, and positive dissensus. Politics, philosophy & economics , 14(3):229–254, 2015. -->

<!-- [原子块 · verbatim] Leike et al. (2018) Leike, J., Krueger, D., Everitt, T., Martic, M., Maini, V., and Legg, S. Scalable agent alignment via reward modeling: a research direction, 2018. -->

<!-- [原子块 · verbatim] Li et al. (2023a) Li, C., Zhang, M., Mei, Q., Wang, Y., Hombaiah, S. A., Liang, Y., and Bendersky, M. Teach llms to personalize – an approach inspired by writing education, 2023a. -->

<!-- [原子块 · verbatim] Li et al. (2023b) Li, J., Mehrabi, N., Peris, C., Goyal, P., Chang, K.-W., Galstyan, A., Zemel, R., and Gupta, R. On the steerability of large language models toward data-driven personas. 2023b. doi:  -->

<!-- [原子块 · verbatim] Liang et al. (2023) Liang, P., Bommasani, R., Lee, T., Tsipras, D., Soylu, D., Yasunaga, M., Zhang, Y., Narayanan, D., Wu, Y., Kumar, A., Newman, B., Yuan, B., Yan, B., Zhang, C., Cosgrove, C., Mannin -->

<!-- [原子块 · verbatim] Liu et al. (2021) Liu, A., Sap, M., Lu, X., Swayamdipta, S., Bhagavatula, C., Smith, N. A., and Choi, Y. Dexperts: Decoding-time controlled text generation with experts and anti-experts. In Annual Mee -->

<!-- [原子块 · verbatim] Liu et al. (2022) Liu, A., Swayamdipta, S., Smith, N. A., and Choi, Y. Wanli: Worker and ai collaboration for natural language inference dataset creation, 2022. -->

<!-- [原子块 · verbatim] Liu et al. (2024) Liu, A., Han, X., Wang, Y., Tsvetkov, Y., Choi, Y., and Smith, N. A. Tuning language models by proxy, 2024. -->

<!-- [原子块 · verbatim] Liu et al. (2023) Liu, N. F., Kumar, A., Liang, P., and Jia, R. Are sample-efficient nlp models more robust?, 2023. -->

<!-- [原子块 · verbatim] Long (2023) Long, J. Large language model guided tree-of-thought. arXiv preprint arXiv:2305.08291 , 2023. -->

<!-- [原子块 · verbatim] Lu et al. (2020) Lu, X., West, P., Zellers, R., Bras, R. L., Bhagavatula, C., and Choi, Y. Neurologic decoding: (un)supervised neural text generation with predicate logic constraints. ArXiv , abs/2010 -->

<!-- [原子块 · verbatim] Lu et al. (2022) Lu, X., Welleck, S., Hessel, J., Jiang, L., Qin, L., West, P., Ammanabrolu, P., and Choi, Y. Quark: Controllable text generation with reinforced unlearning, 2022. -->

<!-- [原子块 · verbatim] Ma et al. (2023) Ma, X., Mishra, S., Liu, A., Su, S., Chen, J., Kulkarni, C., Cheng, H.-T., Le, Q., and Chi, E. Beyond chatbots: Explorellm for structured thoughts and personalized model responses, 20 -->

<!-- [原子块 · verbatim] MacAskill (2016) MacAskill, W. Normative Uncertainty as a Voting Problem. Mind , 125(500):967–1004, October 2016. ISSN 0026-4423. doi: 10.1093/mind/fzv169 . URL https://doi.org/10.1093/mind/fzv169 . -->

<!-- [原子块 · verbatim] Michael et al. (2023) Michael, J., Mahdi, S., Rein, D., Petty, J., Dirani, J., Padmakumar, V., and Bowman, S. R. Debate helps supervise unreliable experts. arXiv preprint arXiv:2311.08702 , 2023. -->

<!-- [原子块 · verbatim] Min et al. (2020) Min, S., Michael, J., Hajishirzi, H., and Zettlemoyer, L. AmbigQA: Answering ambiguous open-domain questions. In Webber, B., Cohn, T., He, Y., and Liu, Y. (eds.), Proceedings of the  -->

<!-- [原子块 · verbatim] Mishra (2023) Mishra, A. Ai alignment and social choice: Fundamental limitations and policy implications, 2023. -->

<!-- [原子块 · verbatim] Moulin (2004) Moulin, H. Fair Division and Collective Welfare . MIT Press, 2004. -->

<!-- [原子块 · verbatim] Nagel (1979) Nagel, T. The fragmentation of value. In Mortal Questions . Cambridge University Press, Cambridge, 1979. -->

<!-- [原子块 · verbatim] OpenAI (2023a) OpenAI. Openai davinci-002 model. https://www.openai.com , 2023a. Accessed on Date 06/2023. -->

<!-- [原子块 · verbatim] OpenAI (2023b) OpenAI. Openai gpt3.5-turbo. https://www.openai.com , 2023b. Accessed on Date 06/2023. -->

<!-- [原子块 · verbatim] Ouyang et al. (2022) Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C. L., Mishkin, P., Zhang, C., Agarwal, S., Slama, K., Ray, A., Schulman, J., Hilton, J., Kelton, F., Miller, L., Simens, M -->

<!-- [原子块 · verbatim] Ovadya (2023) Ovadya, A. Reimagining democracy for ai. Journal of Democracy , 34(4):162–170, Oct 2023. -->

<!-- [原子块 · verbatim] Page (2008) Page, S. The difference: How the power of diversity creates better groups, firms, schools, and societies-new edition . Princeton University Press, 2008. -->

<!-- [原子块 · verbatim] Page (2019) Page, S. E. The diversity bonus: How great teams pay off in the knowledge economy . Princeton University Press, 2019. -->

<!-- [原子块 · verbatim] Pan et al. (2023) Pan, A., Chan, J. S., Zou, A., Li, N., Basart, S., Woodside, T., Ng, J., Zhang, H., Emmons, S., and Hendrycks, D. Do the rewards justify the means? measuring trade-offs between rewar -->

<!-- [原子块 · verbatim] Park et al. (2022) Park, J. S., Popowski, L., Cai, C. J., Morris, M. R., Liang, P., and Bernstein, M. S. Social simulacra: Creating populated prototypes for social computing systems, 2022. -->

<!-- [原子块 · verbatim] Park et al. (2023) Park, J. S., O’Brien, J., Cai, C. J., Morris, M. R., Liang, P., and Bernstein, M. S. Generative agents: Interactive simulacra of human behavior. In Proceedings of the 36th Annual AC -->

<!-- [原子块 · verbatim] Peng et al. (2023) Peng, A., Netanyahu, A., Ho, M. K., Shu, T., Bobu, A., Shah, J., and Agrawal, P. Diagnosis, feedback, adaptation: A human-in-the-loop framework for test-time policy adaptation. In P -->

<!-- [原子块 · verbatim] Perez et al. (2022) Perez, E., Ringer, S., Lukošiūtė, K., Nguyen, K., Chen, E., Heiner, S., Pettit, C., Olsson, C., Kundu, S., Kadavath, S., et al. Discovering language model behaviors with model-writ -->

<!-- [原子块 · verbatim] Pew Research Center (2021) Pew Research Center. The state of online harassment. Technical report, Washington, D.C., January 2021. URL https://www.pewresearch.org/internet/2021/01/13/the-state-of-onlin -->

<!-- [原子块 · verbatim] Qin et al. (2022) Qin, L., Welleck, S., Khashabi, D., and Choi, Y. Cold decoding: Energy-based constrained text generation with langevin dynamics. ArXiv , abs/2202.11705, 2022. URL https://api.semanti -->

<!-- [原子块 · verbatim] Ramezani & Xu (2023) Ramezani, A. and Xu, Y. Knowledge of cultural moral norms in large language models, 2023. -->

<!-- [原子块 · verbatim] Ramé et al. (2023) Ramé, A., Couairon, G., Shukor, M., Dancette, C., Gaya, J.-B., Soulier, L., and Cord, M. Rewarded soups: towards pareto-optimal alignment by interpolating weights fine-tuned on dive -->

<!-- [原子块 · verbatim] Ratcliffe (2016) Ratcliffe, S. Albert einstein, 2016. URL https://www.oxfordreference.com/view/10.1093/acref/9780191826719.001.0001/q-oro-ed4-00003988 . -->

<!-- [原子块 · verbatim] Rawls (1971) Rawls, J. A Theory of Justice: Original Edition . Harvard University Press, 1971. ISBN 9780674880108. URL http://www.jstor.org/stable/j.ctvjf9z6v . -->

<!-- [原子块 · verbatim] Rawls (1996) Rawls, J. Political Liberalism . Columbia University Press, New York, 1996. -->

<!-- [原子块 · verbatim] Raz (1999) Raz, J. Engaging Reason: On the Theory of Value and Action . Oxford University Press, Oxford, 1999. -->

<!-- [原子块 · verbatim] Santurkar et al. (2023) Santurkar, S., Durmus, E., Ladhak, F., Lee, C., Liang, P., and Hashimoto, T. Whose opinions do language models reflect?, 2023. -->

<!-- [原子块 · verbatim] Santy et al. (2023) Santy, S., Liang, J. T., Bras, R. L., Reinecke, K., and Sap, M. Nlpositionality: Characterizing design biases of datasets and models, 2023. -->

<!-- [原子块 · verbatim] Scherrer et al. (2023) Scherrer, N., Shi, C., Feder, A., and Blei, D. M. Evaluating the moral beliefs encoded in llms, 2023. -->

<!-- [原子块 · verbatim] Shajalal et al. (2023) Shajalal, M., Atabuzzaman, M., Baby, M. B., Karim, M. R., and Boden, A. Textual Entailment Recognition with Semantic Features from Empirical Text Representation , pp. 183–195. S -->

<!-- [原子块 · verbatim] Shanahan & Clarke (2023) Shanahan, M. and Clarke, C. Evaluating large language model creativity from a literary perspective, 2023. -->

<!-- [原子块 · verbatim] Shanahan et al. (2023) Shanahan, M., McDonell, K., and Reynolds, L. Role-play with large language models, 2023. -->

<!-- [原子块 · verbatim] Sharma et al. (2023a) Sharma, A., Lin, I. W., Miner, A. S., Atkins, D. C., and Althoff, T. Human–ai collaboration enables more empathic conversations in text-based peer-to-peer mental health support.  -->

<!-- [原子块 · verbatim] Sharma et al. (2023b) Sharma, A., Rushton, K., Lin, I., Wadden, D., Lucas, K., Miner, A., Nguyen, T., and Althoff, T. Cognitive reframing of negative thoughts through human-language model interaction. -->

<!-- [原子块 · verbatim] Sharma et al. (2023c) Sharma, A., Rushton, K., Lin, I. W., Nguyen, T., and Althoff, T. Facilitating self-guided mental health interventions through human-language model interaction: A case study of co -->

<!-- [原子块 · verbatim] Sharma et al. (2023d) Sharma, A., Rushton, K., Lin, I. W., Wadden, D., Lucas, K. G., Miner, A. S., Nguyen, T., and Althoff, T. Cognitive reframing of negative thoughts through human-language model int -->

<!-- [原子块 · verbatim] Sher (1998) Sher, G. On the possibility of a substantive theory of truth. Synthese , 117:133–172, 1998. -->

<!-- [原子块 · verbatim] Simmons (2023) Simmons, G. Moral mimicry: Large language models produce moral rationalizations tailored to political identity. In Padmakumar, V., Vallejo, G., and Fu, Y. (eds.), Proceedings of the 61s -->

<!-- [原子块 · verbatim] Siththaranjan et al. (2023) Siththaranjan, A., Laidlaw, C., and Hadfield-Menell, D. Distributional preference learning: Understanding and accounting for hidden context in rlhf, 2023. -->

<!-- [原子块 · verbatim] Solaiman & Dennison (2021) Solaiman, I. and Dennison, C. Process for adapting language models to society (palms) with values-targeted datasets, 2021. -->

<!-- [原子块 · verbatim] Song et al. (2024) Song, I., Pendse, S. R., Kumar, N., and Choudhury, M. D. The typing cure: Experiences with large language model chatbots for mental health support, 2024. -->

<!-- [原子块 · verbatim] Sorensen et al. (2023) Sorensen, T., Jiang, L., Hwang, J., Levine, S., Pyatkin, V., West, P., Dziri, N., Lu, X., Rao, K., Bhagavatula, C., Sap, M., Tasioulas, J., and Choi, Y. Value kaleidoscope: Enga -->

<!-- [原子块 · verbatim] Srivastava et al. (2023) Srivastava, A., Rastogi, A., Rao, A., Shoeb, A. A. M., Abid, A., Fisch, A., Brown, A. R., Santoro, A., Gupta, A., Garriga-Alonso, A., Kluska, A., Lewkowycz, A., Agarwal, A., P -->

<!-- [原子块 · verbatim] Sumers et al. (2023) Sumers, T. R., Yao, S., Narasimhan, K., and Griffiths, T. L. Cognitive architectures for language agents, 2023. -->

<!-- [原子块 · verbatim] Swamy et al. (2024) Swamy, G., Dann, C., Kidambi, R., Wu, Z. S., and Agarwal, A. A minimaximalist approach to reinforcement learning from human feedback, 2024. -->

<!-- [原子块 · verbatim] Taori et al. (2023) Taori, R., Gulrajani, I., Zhang, T., Dubois, Y., Li, X., Guestrin, C., Liang, P., and Hashimoto, T. B. Stanford alpaca: An instruction-following llama model. https://github.com/tat -->

<!-- [原子块 · verbatim] Tasioulas (2022) Tasioulas, J. Artificial Intelligence, Humanistic Ethics. Daedalus , 151(2):232–243, 05 2022. ISSN 0011-5266. doi: 10.1162/daed_a_01912 . URL https://doi.org/10.1162/daed_a_01912 . -->

<!-- [原子块 · verbatim] Team et al. (2024) Team, G., Mesnard, T., Hardin, C., Dadashi, R., Bhupatiraju, S., Pathak, S., Sifre, L., Rivière, M., Kale, M. S., Love, J., Tafti, P., Hussenot, L., Chowdhery, A., Roberts, A., Baru -->

<!-- [原子块 · verbatim] Törnberg et al. (2023) Törnberg, P., Valeeva, D., Uitermark, J., and Bail, C. Simulating social media using large language models to evaluate alternative news feed algorithms. arXiv preprint arXiv:231 -->

<!-- [原子块 · verbatim] Touvron et al. (2023) Touvron, H., Martin, L., Stone, K., Albert, P., Almahairi, A., Babaei, Y., Bashlykov, N., Batra, S., Bhargava, P., Bhosale, S., Bikel, D., Blecher, L., Ferrer, C. C., Chen, M., C -->

<!-- [原子块 · verbatim] Tozer et al. (2017) Tozer, B., Mazzuchi, T., and Sarkani, S. Many-objective stochastic path finding using reinforcement learning. Expert Systems with Applications , 72:371–382, 2017. ISSN 0957-4174. d -->

<!-- [原子块 · verbatim] Wang et al. (2023a) Wang, Y., Ivison, H., Dasigi, P., Hessel, J., Khot, T., Chandu, K. R., Wadden, D., MacMillan, K., Smith, N. A., Beltagy, I., and Hajishirzi, H. How far can camels go? exploring the -->

<!-- [原子块 · verbatim] Wang et al. (2023b) Wang, Y., Zhong, W., Li, L., Mi, F., Zeng, X., Huang, W., Shang, L., Jiang, X., and Liu, Q. Aligning large language models with human: A survey, 2023b. -->

<!-- [原子块 · verbatim] Wojcik et al. (2022) Wojcik, S., Hilgard, S., Judd, N., Mocanu, D., Ragain, S., Hunzaker, M. B. F., Coleman, K., and Baxter, J. Birdwatch: Crowd wisdom and bridging algorithms can inform understanding -->

<!-- [原子块 · verbatim] Wortsman et al. (2022) Wortsman, M., Ilharco, G., Gadre, S. Y., Roelofs, R., Gontijo-Lopes, R., Morcos, A. S., Namkoong, H., Farhadi, A., Carmon, Y., Kornblith, S., and Schmidt, L. Model soups: averag -->

<!-- [原子块 · verbatim] Wright (1992) Wright, C. Truth and Objectivity . Harvard University Press, Cambridge, MA, 1992. -->

<!-- [原子块 · verbatim] Yang et al. (2019) Yang, R., Sun, X., and Narasimhan, K. A generalized algorithm for multi-objective reinforcement learning and policy adaptation, 2019. -->

<!-- [原子块 · verbatim] Zhao et al. (2023) Zhao, S., Dang, J., and Grover, A. Group Preference Optimization: Few-Shot Alignment of Large Language Models. 2023. doi: 10.48550/ARXIV.2310.11523 . URL https://arxiv.org/abs/2310. -->

<!-- [原子块 · verbatim] Zhou et al. (2024) Zhou, K., Hwang, J. D., Ren, X., and Sap, M. Relying on the unreliable: The impact of language models’ reluctance to express uncertainty, 2024. -->

<!-- [原子块 · verbatim] Ziems et al. (2023) Ziems, C., Held, W., Shaikh, O., Chen, J., Zhang, Z., and Yang, D. Can large language models transform computational social science? arXiv preprint arXiv:2305.03514 , 2023. -->

<!-- [原子块 · verbatim] Zintgraf et al. (2015) Zintgraf, L. M., Kanters, T. V., Roijers, D. M., Oliehoek, F. A., and Beau, P. Quality assessment of morl algorithms: A utility-based approach. 2015. URL https://api.semanticsch -->

**EN** Appendix A Experimentation Details

**ZH** 附录 A 实验细节

**EN** In section 5.2 we explore Claim 1 using experimentation. This section outlines the details of these experiments.

**ZH** 在第 5.2 节中，我们通过实验考察论断 1。本节概述这些实验的细节。

**EN** Dataset

**ZH** 数据集

**EN** We use two diverse multiple choices datasets, the GlobalOpinionQA (GlobalQA) dataset which is an aggregation of cross-national surveys designed to capture opinions on global issues (Durmus et al., 2023) and the Machine Personality Inventory (MPI) which is a collection of 120 questions designed to evaluate human personality traits (Jiang et al., 2023). GlobalQA human responses were collected using strict protocols which required that each country to have a nationally representative sample of at least ⟦SLOT_111⟧ people (⟦SLOT_112⟧ years of age). For our experimentation, we only used questions which had responses from both the United States and Japan (⟦SLOT_113⟧ questions total). The MPI consisted of a collection of ⟦SLOT_114⟧ responses from ⟦SLOT_115⟧ countries. Examples of these two datasets can be found in Table 2.

**ZH** 我们使用两个不同的多项选择数据集：GlobalOpinionQA（GlobalQA）数据集，它是为捕捉对全球议题的意见而设计的跨国调查的聚合（Durmus 等，2023）；以及机器人格量表（MPI），它是一组用于评估人类人格特质的 120 道问题（Jiang 等，2023）。GlobalQA 的人类回答采用严格的规程收集，要求每个国家具有至少 ⟦SLOT_111⟧ 人（⟦SLOT_112⟧ 岁）的全国代表性样本。在我们的实验中，我们只使用同时有美国与日本回答的问题（共 ⟦SLOT_113⟧ 道题）。MPI 由 ⟦SLOT_114⟧ 份回答构成，这些回答来自 ⟦SLOT_115⟧ 个国家。这两个数据集的示例见表 2。

<!-- [原子块 · table] Dataset Question Answer Choices GlobalQA Do you personally believe that getting a divorce is morally acceptable, morally unacceptable, or is it not a moral issue? [’Morally acceptable’,’Morally unacce -->

**EN** Table 2: Example of GlobalQA and MIP dataset.

**ZH** 表 2：GlobalQA 与 MIP 数据集的示例。

**EN** Models

**ZH** 模型

**EN** We used three different model classes: LLaMA, LLaMA2, and GPT-3. For each model class, we used a pre and post aligned model. We refer to Table 3 for the exact models used and the type of alignment.

**ZH** 我们使用了三个不同的模型类别：LLaMA、LLaMA2 与 GPT-3。对于每个模型类别，我们使用一个对齐前与一个对齐后的模型。具体使用的模型与对齐类型见表 3。

<!-- [原子块 · table] Model Class Model Name Type Alignment LLaMA LLaMA ( Touvron et al., 2023 ) Pre N/A LLaMA Alpaca ( Taori et al., 2023 ) Post Instruction FT LLaMA Tulu ( Wang et al., 2023a ) Post Instruction FT LLaMA2  -->

**EN** Table 3: A list of models used in experimentation. We list the overall model class, the exact name of the mode, whether it is pre- or post-alignment, and if it is post-aligned we indicate the type of alignment used (fine-tuning (FT), reinforcement learning with human feedback (RLHF), or unknown

**ZH** 表 3：实验中所用模型的清单。我们列出总体模型类别、模型的确切名称、它是对齐前还是对齐后；若是对齐后，我们指明所用的对齐类型（微调（FT）、基于人类反馈的强化学习（RLHF）或未知）。

**EN** Model Distribution

**ZH** 模型分布

**EN** To create the ‘‘model distribution", we extracted the probability of next token response (logit) for each answer choice selection. Since we were using pre-aligned models, we utilized the technique of in-context learning to steer the model to output the letter of the multiple choice answer it wanted to select as the first, next token. In order to remove any bias these in-context examples might implicitly have, we prompted the model with the same prompt a total of 5 times, each time randomly selecting the ‘‘correct" answer shown in the in-context examples. We then averaged the probabilities over these five distributions. The in-context examples are given below77 7 The answer choice was randomized for each sample:

**ZH** 为构造「模型分布」，我们抽取每个答案选项的下一词元回答概率（logit）。由于我们使用的是对齐前的模型，我们采用上下文学习技术，引导模型把它想选的多项选择答案的字母作为第一个下一词元输出。为消除这些上下文示例可能隐含的任何偏置，我们用同一提示对模型提示共 5 次，每次随机选取上下文示例中显示的「正确」答案。随后我们在这五个分布上取概率平均。上下文示例如下（脚注 7：每个样本的答案选项被随机化：）

**EN** GlobalQA Prefix How much, if at all, do you think people should vote? A. Every election B. Some elections C. No elections Answer Choice:A. Please tell use whether you are satisfied or dissatisfied with your current class? A. Very satisfied B. Somewhat Satisfied C. Somewhat dissatisfied D. Very dissatisfied Answer Choice:A. How often, if ever, do you clean your house? A. Often B. Sometimes C. Rarely D. Never E. Refused Answer Choice:C.

**ZH** GlobalQA 前缀 你认为人们应该在多大程度上投票（如果有投票的话）？A. 每次选举 B. 部分选举 C. 不投票 答案选项：A. 请告诉我们你对当前阶层满意还是不满意？A. 非常满意 B. 比较满意 C. 比较不满意 D. 非常不满意 答案选项：A. 如果有的话，你多久打扫一次房子？A. 经常 B. 有时 C. 很少 D. 从不 E. 拒绝回答 答案选项：C.

**EN** MPI Prefix Given a statement of you: Ask for help from a friend Please choose from the following options to identify how accurately this statement describes you. A. Very Accurate B. Moderately Accurate C.Neither Accurate Nor Inaccurate D.Moderately Inaccurate E.Very Inaccurate Answer Choice:B. Given a statement of you: Celebrate accomplishments of family members Please choose from the following options to identify how accurately this statement describes you. A. Very Accurate B. Moderately Accurate C.Neither Accurate Nor Inaccurate D.Moderately Inaccurate E.Very Inaccurate Answer Choice:A. Given a statement of you: Wonder about the stars and space Please choose from the following options to identify how accurately this statement describes you. A. Very Accurate B. Moderately Accurate C.Neither Accurate Nor Inaccurate D.Moderately Inaccurate E.Very Inaccurate Answer Choice:E.

**ZH** MPI 前缀 给你一段关于你的陈述：向朋友求助 请从下列选项中选择，指出这段陈述描述你的准确程度。A. 非常准确 B. 比较准确 C. 既不准确也不不准确 D. 比较不准确 E. 非常不准确 答案选项：B. 给你一段关于你的陈述：庆祝家人的成就 请从下列选项中选择，指出这段陈述描述你的准确程度。A. 非常准确 B. 比较准确 C. 既不准确也不不准确 D. 比较不准确 E. 非常不准确 答案选项：A. 给你一段关于你的陈述：思索星辰与太空 请从下列选项中选择，指出这段陈述描述你的准确程度。A. 非常准确 B. 比较准确 C. 既不准确也不不准确 D. 比较不准确 E. 非常不准确 答案选项：E.

**EN** Evaluation Metrics

**ZH** 评测指标

**EN** We compare the model distribution to the target human population using the Jensen-Shannon distance (lower values indicate more similar distributions) over each question and then average the values. We also calculate the entropy of each distribution as well.

**ZH** 我们使用 Jensen-Shannon 距离（数值越低表示分布越相似）在每个问题上比较模型分布与目标人群，然后对这些值取平均。我们也计算每个分布的熵。

**EN** A.1 Further Analysis

**ZH** A.1 进一步分析

**EN** To test the extent to which our claim holds, we test a suite of vanilla pretrained LLMs compared to a set of “aligned" (RLHFed, finetuned) on two diverse multiple choices datasets, the GlobalOpinionQA (GlobalQA) dataset which is an aggregation of cross-national surveys designed to capture opinions on global issues (Durmus et al., 2023) and the Machine Personality Inventory (MPI) which is a collection of 120 questions designed to evaluate human personality traits (Jiang et al., 2023). Both datasets area accompanied by large and nationally representative 88 8 GlobalQA results were collected using strict protocols which required each country to have a nationally representative sample of at least ⟦SLOT_116⟧ people (⟦SLOT_117⟧ years of age). MPI consisted of a collection of ⟦SLOT_118⟧ responses from ⟦SLOT_119⟧ countries. human responses. For the GlobalQA dataset, we included questions which had responses from citizens of the United States and Japan (⟦SLOT_120⟧) as our target population. To create each model’s distribution, we extracted the probability of next token response (logit) for each answer choice selection and averaged these results over ⟦SLOT_121⟧ prompts of the model. We then compared the model distribution to the target human population using the Jensen-Shannon distance (lower values indicate more similar distributions).

**ZH** 为检验我们的论断在多大程度上成立，我们在两个不同的多项选择数据集上测试一组原始预训练 LLM 与一组「已对齐」（经 RLHF、微调）的模型作比较：GlobalOpinionQA（GlobalQA）数据集，它是为捕捉对全球议题的意见而设计的跨国调查的聚合（Durmus 等，2023）；以及机器人格量表（MPI），它是一组用于评估人类人格特质的 120 道问题（Jiang 等，2023）。两个数据集都配有大规模、具全国代表性的人类回答（脚注 8：GlobalQA 的结果采用严格的规程收集，要求每个国家具有至少 ⟦SLOT_116⟧ 人（⟦SLOT_117⟧ 岁）的全国代表性样本。MPI 由 ⟦SLOT_118⟧ 份回答构成，这些回答来自 ⟦SLOT_119⟧ 个国家。）。对于 GlobalQA 数据集，我们纳入了同时有美国与日本公民回答的问题（⟦SLOT_120⟧）作为我们的目标人群。为构造每个模型的分布，我们抽取每个答案选项的下一词元回答概率（logit），并在模型的 ⟦SLOT_121⟧ 个提示上取平均。随后我们用 Jensen-Shannon 距离（数值越低表示分布越相似）比较模型分布与目标人群。

**EN** Both datasets area accompanied by large and nationally representative 99 9 GlobalQA results were collected using strict protocols which required each country to have a nationally representative sample of at least ⟦SLOT_122⟧ people (⟦SLOT_123⟧ years of age). MPI consisted of a collection of ⟦SLOT_124⟧ responses from ⟦SLOT_125⟧ countries. human responses. For the GlobalQA dataset, we included questions which had responses from citizens of the United States and Japan (⟦SLOT_126⟧) as our target population. To create each model’s distribution, we extracted the probability of next token response (logit) for each answer choice selection and averaged these results over ⟦SLOT_127⟧ prompts of the model. We then compared the model distribution to the target human population using the Jensen-Shannon distance (lower values indicate more similar distributions). More details of the experimentation can be found in Appendix A.

**ZH** 两个数据集都配有大规模、具全国代表性的人类回答（脚注 9：GlobalQA 的结果采用严格的规程收集，要求每个国家具有至少 ⟦SLOT_122⟧ 人（⟦SLOT_123⟧ 岁）的全国代表性样本。MPI 由 ⟦SLOT_124⟧ 份回答构成，这些回答来自 ⟦SLOT_125⟧ 个国家。）。对于 GlobalQA 数据集，我们纳入了同时有美国与日本公民回答的问题（⟦SLOT_126⟧）作为我们的目标人群。为构造每个模型的分布，我们抽取每个答案选项的下一词元回答概率（logit），并在模型的 ⟦SLOT_127⟧ 个提示上取平均。随后我们用 Jensen-Shannon 距离（数值越低表示分布越相似）比较模型分布与目标人群。实验的更多细节见附录 A。

**EN** As you can see in our results in Table 1, almost all pre-aligned models are more similar to the target human distribution than the post-aligned models for both datasets. This is even more pronounced in models with more training data and higher context length with the gap between pre- and post-models more than doubling when comparing LLaMA and LLaMA2. This is even more pronounced in models with more training data and higher context length with the gap between pre- and post-models more than doubling when comparing LLaMA and LLaMA2. We also note that the size of the model does not have a large impact on the results, as seen in comparing LLaMA2 7b vs. 13b. From qualitative analysis we did see the pre-aligned models had more variance in their distributional spread than post-aligned models and this was confirmed by looking at the average entropy of each distribution. On average, the pre-aligned model has ⟦SLOT_128⟧ more entropy compared to the post-aligned models.

**ZH** 正如我们在表 1 的结果中所见，在两个数据集上，几乎所有对齐前的模型都比对齐后的模型更接近目标人类分布。这在训练数据更多、上下文长度更长的模型中更为明显：比较 LLaMA 与 LLaMA2 时，对齐前后模型之间的差距翻了一倍以上。这在训练数据更多、上下文长度更长的模型中更为明显：比较 LLaMA 与 LLaMA2 时，对齐前后模型之间的差距翻了一倍以上。我们还注意到，模型规模对结果影响不大，如比较 LLaMA2 7b 与 13b 所见。通过定性分析，我们发现对齐前的模型在分布展开上比对齐后的模型方差更大，这一点通过查看各分布的平均熵得到了确认。平均而言，对齐前的模型比对齐后的模型多出 ⟦SLOT_128⟧ 的熵。

**EN** As additional support for this hypothesis, (Santurkar et al., 2023; Durmus et al., 2023) both find that “aligned" models have much lower entropy in their response distribution compared to any reference population (even compared to subgroups, like Democrats). Prior work also finds that RLHFed models “tend to be less well-calibrated than pre-trained models." (Durmus et al., 2023) and have reduced textual diversity (Kirk et al., 2024).

**ZH** 作为对这一假设的额外支持，（Santurkar 等，2023；Durmus 等，2023）都发现「已对齐」模型在回答分布上的熵远低于任何参照人群（甚至低于民主党人等子群体）。先前工作还发现，经 RLHF 的模型「往往不如预训练模型校准良好」（Durmus 等，2023），且文本多样性降低（Kirk 等，2024）。

**EN** Appendix B Additional Experimentation

**ZH** 附录 B 补充实验

**EN** In section 5.2 we explore the claim that pre-aligned models might perform better in distributional pluralism than post-RLHF models. We test this hypothesis using two datasets, GlobalOpinionQA and the Machine Personality Inventory. In these experiments, we compare the model distributions to multiple choice questions to target human populations. We found that for both datasets, the pre-aligned model was closer to the human distribution than the post-aligned models. From qualitative analysis we noticed that in the majority of cases the distributions for the pre-aligned models were more variable across the answer choices, in contrast to the post-aligned models which showed more spiked distributions with probability mass centered on only one or two answer choices. This was reflected in our analysis of entropy, which showed that all pre-aligned models had higher average entropy across their distributions than post-aligned models. See Table 4 and Figure 3 for these results.

**ZH** 在第 5.2 节中，我们考察这样一个论断：对齐前的模型在分布多元性上可能优于 RLHF 后的模型。我们用两个数据集 GlobalOpinionQA 与机器人格量表检验这一假设。在这些实验中，我们把模型在多项选择问题上的分布与目标人群作比较。我们发现，在两个数据集上，对齐前的模型都比对齐后的模型更接近人类分布。通过定性分析我们注意到，在多数情形中，对齐前模型在各答案选项上的分布更具变异性，而对齐后的模型则呈现更尖锐的分布，概率质量集中在仅一两个答案选项上。这反映在我们对熵的分析中：所有对齐前的模型在其分布上的平均熵都高于对齐后的模型。相关结果见表 4 与图 3。

<!-- [原子块 · table] Model Human LLaMA LLaMA2 (7B) LLaMA2 (13B) Gemma (7B) GPT-3 Dataset Japan/US/Germany Global Pre Alpaca Tulu Pre Post Pre Post Pre Post Pre Post GlobalQA 0.96/0.99/0.96 NA 1.38 1.15 0.67 1.20 0.61 1.19 -->

**EN** Table 4: Results comparing entropy of each human distributions and model distributions on opinion multiple choice questions over two datasets, GlobalQA (target human distribution of Japan and US) and MPI. Each model class included comparison of models that are pre and post RLHF. Note that we compare two “post" RLHF models for LLaMA (Alpaca and Tulu).

**ZH** 表 4：在两个数据集 GlobalQA（目标人类分布为日本与美国）与 MPI 上，比较各人类分布与模型分布在意见类多项选择问题上的熵的结果。每个模型类别都包含对齐前与 RLHF 后模型的比较。注意我们对 LLaMA 比较了两个「后」RLHF 模型（Alpaca 与 Tulu）。

<!-- [原子块 · table] a. GlobalQA b. MPI -->

**EN** Figure 3: Distribution of entropy scores across datasets for each model. Top shows results over GlobalQA and bottom shows results for MPI.

**ZH** 图 3：每个模型在各数据集上熵分数的分布。上方为 GlobalQA 的结果，下方为 MPI 的结果。

**EN** Although this supported our hypothesis, we were wanted to further investigate how much entropy alone accounted for the similarities in the model distribution and the human distributions. To analyze this, we randomly shuffled the labels of the model distributions, resulting in a separate distribution that had the exact same entropy. We then compared these “shuffled" model distribution to the same human distribution using the Jensen-Shannon distance metric. Table 11 shows the result of these calculations. Here we see larger similarity scores in general across models and datasets. This indicates that although some of the similarity between model and human models is due to entropy, there might some effect of similarity as well. Further investigation is needed to substantiate these hypotheses, though.

**ZH** 尽管这支持了我们的假设，我们还想进一步调查熵本身在多大程度上解释了模型分布与人类分布之间的相似性。为此，我们随机打乱模型分布的标签，得到一个熵完全相同的独立分布。随后我们用 Jensen-Shannon 距离把这些「打乱后」的模型分布与同一人类分布比较。表 11 给出了这些计算的结果。这里我们总体上看到各模型与各数据集的相似度分数更大。这表明，尽管模型与人类模型之间的部分相似性源于熵，相似性本身也可能存在一定效应。不过，要证实这些假设仍需进一步研究。

<!-- [原子块 · table] Model Class LLaMA LLaMA2 (7B) LLaMA2 (13B) Gemma (7B) GPT-3 Dataset Pre Alpaca Tulu Pre Post Pre Post Pre Post Pre Post GlobalQA (Japan) 0.45 0.51 0.62 0.51 0.67 0.51 0.68 0.45 0.61 0.50 0.59 GlobalQA -->

**EN** Table 5: Results comparing human distributions to shuffled model distributions on opinion multiple choice questions over two datasets, GlobalQA (target human distribution of Japan and US) and MPI using the Jensen-Shannon distance. Each model class included comparison of models that are pre and post RLHF1111 11 Model detials, including exact models used, can be found in Appendix A.. Note that we compare two “post" RLHF models for LLaMA (Alpaca and Tulu). These results are used to investigate how much entropy alone accounts for the similarity of these distributions. We bold the smaller (more similar) value.

**ZH** 表 5：在两个数据集 GlobalQA（目标人类分布为日本与美国）与 MPI 上，使用 Jensen-Shannon 距离比较人类分布与打乱后模型分布在意见类多项选择问题上的结果。每个模型类别都包含对齐前与 RLHF 后模型的比较（脚注 11：模型细节，包括所用确切模型，见附录 A。）。注意我们对 LLaMA 比较了两个「后」RLHF 模型（Alpaca 与 Tulu）。这些结果用于考察熵本身在多大程度上解释了这些分布的相似性。我们把更小（更相似）的数值加粗。
