# 面向主观性 NLP 任务的两种对照数据标注范式

> 原标题：Two Contrasting Data Annotation Paradigms for Subjective NLP Tasks
> 作者：Paul Röttger, Bertie Vidgen, Dirk Hovy, Janet B. Pierrehumbert · arXiv:2112.07475 · 2021-12-14

<!-- [原子块 · verbatim] Two Contrasting Data Annotation Paradigms for Subjective NLP Tasks -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] Labelled data is the foundation of most natural language processing tasks. However, labelling data is difficult and there often are diverse valid beliefs about what the correct data labels should be.  -->

**EN** 1 Introduction

**ZH** 1 引言

**EN** Many natural language processing (NLP) tasks are subjective, in the sense that there are diverse valid beliefs about what the correct data labels should be. Some tasks, like hate speech detection, are highly subjective: different people have very different beliefs about what should or should not be labelled as hateful (Talat, 2016; Salminen et al., 2019; Davani et al., 2021a), and while some beliefs are more widely accepted than others, there is no single objective truth. Other examples include toxicity (Sap et al., 2019; Sap et al., 2021), harassment (Al Kuwatly et al., 2020), harmful content (Jiang et al., 2021) and stance detection (Luo et al., 2020; AlDayel and Magdy, 2021) as well as sentiment analysis (Kenyon-Dean et al., 2018; Poria et al., 2020). But even for seemingly objective tasks like part-of-speech tagging, there is subjective disagreement between annotators (Plank et al., 2014b).

**ZH** 许多自然语言处理（NLP）任务都具有主观性，也就是说，对于哪些才是正确的数据标签，存在多种同样成立的信念。有些任务主观性极强，例如仇恨言论检测：不同的人对于什么应当、什么不应当被标为仇恨内容，持有截然不同的看法（Talat，2016；Salminen 等，2019；Davani 等，2021a），虽然某些信念比另一些得到更广泛的接受，却并不存在唯一的客观真理。其他例子包括毒性检测（Sap 等，2019；Sap 等，2021）、骚扰（Al Kuwatly 等，2020）、有害内容（Jiang 等，2021）、立场检测（Luo 等，2020；AlDayel 与 Magdy，2021）以及情感分析（Kenyon-Dean 等，2018；Poria 等，2020）。然而即便是词性标注这类看似客观的任务，标注者之间也存在主观分歧（Plank 等，2014b）。

<!-- [原子块 · img]  -->

**EN** Figure 1: Two key questions for dataset creators.

**ZH** 图 1：数据集构建者需要回答的两个关键问题。

**EN** In this article, we argue that dataset creators should consider the role of annotator subjectivity in the annotation process and either explicitly encourage it or discourage it. Annotators may subjectively disagree about labels (e.g., for hate speech) but dataset creators can and should decide, based on the intended downstream use of their dataset, whether they want to a) capture different beliefs or b) encode one specific belief in their data.

**ZH** 在本文中，我们认为数据集构建者应当在标注流程中考虑标注者主观性所扮演的角色，并明确地要么鼓励它、要么抑制它。标注者可能在标签上产生主观分歧（例如仇恨言论的情形），但数据集构建者能够且应当依据数据集的预期下游用途，决定是要 a）捕捉不同的信念，还是 b）在数据中编码某一种特定信念。

**EN** As a framework, we propose two contrasting data annotation paradigms. Each paradigm facilitates a clear and distinct downstream use. The descriptive paradigm encourages annotator subjectivity to create datasets as granular surveys of individual beliefs. Descriptive data annotation thus allows for the capturing and modelling of different beliefs. The prescriptive paradigm, on the other hand, discourages annotator subjectivity and instead tasks annotators with encoding one specific belief, formulated in the annotation guidelines. Prescriptive data annotation thus enables the training of models that seek to consistently apply one belief. A researcher may, for example, want to model different beliefs about hate speech (⟦SLOT_0⟧ descriptive paradigm), while a content moderation engineer at a social media company may need models that apply their content policy (⟦SLOT_1⟧ prescriptive paradigm).

**ZH** 作为一个框架，我们提出两种相互对照的数据标注范式，每种范式都服务于一种清晰而独特的下游用途。描述性（descriptive）范式鼓励标注者主观性，把数据集构建为对个人信念的细粒度调查，因此描述性数据标注能够捕捉并建模不同的信念。规定性（prescriptive）范式则相反，它抑制标注者主观性，转而让标注者去编码一种在标注指南中加以阐明的特定信念；因此规定性数据标注能够训练出力求一贯地贯彻某一种信念的模型。举例来说，一位研究者可能希望建模关于仇恨言论的不同信念（⟦SLOT_0⟧ 描述性范式），而一家社交媒体公司的内容审核工程师需要的，则是能够执行其内容政策的模型（⟦SLOT_1⟧ 规定性范式）。

**EN** Neither paradigm is inherently superior, but explicitly aiming for one or the other is beneficial because it makes clear what an annotated dataset can and should be used for. For example, data annotated under the descriptive paradigm can provide insights into different beliefs (§2.1), but it cannot easily be used to train models with one pre-specified behaviour (§3.1). By contrast, leaving annotator subjectivity unaddressed, as has mostly been the case in NLP so far, leads to datasets that neither capture an interpretable diversity of beliefs nor consistently encode one specific belief; an undesirable middle ground without a clear downstream use.11 1 See Appx. A for a selective overview of existing datasets.

**ZH** 两种范式本身并无高下之分，但明确以其中之一为目标是有益的，因为它厘清了标注数据集能够且应当被用于什么。例如，在描述性范式下标注的数据可以揭示不同的信念（§2.1），却难以用来训练具备某种预设行为的模型（§3.1）。相反，若像迄今 NLP 中常见的那样对标注者主观性不加处理，得到的数据集既没有捕捉到可解释的信念多样性，也没有一贯地编码某一种特定信念，这是一种缺乏明确下游用途、并不理想的中间状态。11 1 已有数据集的选择性概览见附录 A。

**EN** The two paradigms are applicable to all data annotation. They can be used to compare existing datasets, and to make and communicate decisions about how new datasets are annotated as well as how annotator disagreement can be interpreted. We hope that by naming and explaining the two paradigms, and by discussing key benefits and challenges in their implementation, we can support more intentional annotation process design, which will result in more useful NLP datasets.

**ZH** 这两种范式适用于一切数据标注。它们既可以用来比较现有数据集，也可以用来做出并传达关于新数据集如何标注、以及标注者分歧应如何解释的决策。我们希望，通过为这两种范式命名并加以阐释、讨论其实施过程中的关键收益与挑战，能够促成更有意识的标注流程设计，从而产出更有用的 NLP 数据集。

**EN** Terminology

**ZH** 术语

**EN** Our use of the terms descriptive and prescriptive aligns with their use in both linguistics and ethics. In linguistics, descriptivism studies how language is used, whereas prescriptive grammar declares how language should be used (Justice, 2006). Descriptive ethics studies the moral judgments that people make, while prescriptive ethics considers how people ought to act (Thiroux and Krasemann, 2015). Accordingly, descriptive data annotation surveys annotators’ beliefs, whereas prescriptive data annotation aims to encode one specific belief, which is formulated in the annotation guidelines.

**ZH** 我们对“描述性”与“规定性”这两个术语的用法，与它们在语言学和伦理学中的用法一致。在语言学中，描写主义（descriptivism）研究语言实际如何被使用，而规定语法（prescriptive grammar）则规定语言应当如何使用（Justice，2006）。描述伦理学研究人们实际做出的道德判断，而规定伦理学考察人们应当如何行动（Thiroux 与 Krasemann，2015）。相应地，描述性数据标注调查标注者的信念，而规定性数据标注则力求编码一种在标注指南中加以阐明的特定信念。

**EN** 2 The Descriptive Annotation Paradigm: Encouraging Annotator Subjectivity

**ZH** 2 描述性标注范式：鼓励标注者主观性

**EN** 2.1 Key Benefits

**ZH** 2.1 主要收益

**EN** Insights into Diverse Beliefs

**ZH** 洞察多元信念

**EN** Descriptive data annotation captures a multiplicity of beliefs in data labels, much like a very granular survey would. The distribution of data labels across annotators and examples can therefore provide insights into the beliefs of annotators, or the larger population they may represent. For example, descriptive data annotation has shown that non-Black annotators are more likely to rate African American English as toxic (Sap et al., 2019; Sap et al., 2021), and that people who identify as LGBTQ+ or young adults are more likely to rate random social media comments as toxic (Kumar et al., 2021). Similar correlations between sociodemographic characteristics and annotation outcomes have been found in stance (Luo et al., 2020), sentiment (Diaz et al., 2018) and hate speech detection (Talat, 2016).

**ZH** 描述性数据标注在数据标签中捕捉到信念的多样性，其方式很像一份极为细粒度的调查。因此，标签在标注者与样本上的分布，能够揭示标注者的信念，或他们所代表的更大人群的信念。例如，描述性数据标注已表明：非黑人标注者更可能把非裔美国英语评为有毒（Sap 等，2019；Sap 等，2021）；自认为属于 LGBTQ+ 群体的人或年轻人更可能把随机的社交媒体评论评为有毒（Kumar 等，2021）。在立场检测（Luo 等，2020）、情感分析（Diaz 等，2018）与仇恨言论检测（Talat，2016）中，也发现了社会人口学特征与标注结果之间的类似相关性。

**EN** Even very subjective tasks may have clear-cut entries on which most annotators agree. For example, crowd workers tend to agree more on the extremes of a hate rating scale (Salminen et al., 2019), and datasets which consist of clear hate and non-hate can have very high levels of inter-annotator agreement, even with minimal guidelines (Röttger et al., 2021). Descriptive data annotation can help to identify which entries are more subjective. Jiang et al. (2021), for instance, find that perceptions about the harmfulness of sexually explicit language vary strongly across the eight countries in their sample, whereas support for mass murder or human trafficking is seen as very harmful across all countries.

**ZH** 即便是主观性很强的任务，也可能存在多数标注者意见一致的明确条目。例如，众包工作者在仇恨评分量表的两端往往更容易达成一致（Salminen 等，2019）；而由明确属于仇恨与非仇恨内容构成的数据集，即便指南极为简略，也可以达到很高的标注者间一致性（Röttger 等，2021）。描述性数据标注有助于识别哪些条目的主观性更强。例如 Jiang 等（2021）发现，在其抽样的八个国家中，对于露骨性语言之危害程度的看法差异极大，而对于大规模谋杀或人口贩卖的支持，在所有国家都被视为极具危害性。

**EN** Learning from Disagreement

**ZH** 从分歧中学习

**EN** Annotator-level labels from descriptive data annotation have been shown to be a rich source of information for model training. First, they can be used to separately model annotators’ beliefs. For less subjective tasks such as question answering, this has served to mitigate undesirable annotator biases (Geva et al., 2019). Davani et al. (2021b) reframe and expand on this idea for more subjective tasks like abuse detection, showing that multi-annotator model architectures outperform standard single-label approaches on single label prediction. Second, instead of modelling each annotator separately, other work has grouped them into clusters based on sociodemographic attributes (Al Kuwatly et al., 2020) or polarisation measures derived from annotator labels (Akhtar et al., 2020; Akhtar et al., 2021), with similar results. Third, models can be trained directly on soft labels (i.e., distributions of labels given by annotators), rather than hard one-hot ground truth vectors (Plank et al., 2014a; Jamison and Gurevych, 2015; Uma et al., 2020; Fornaciari et al., 2021).

**ZH** 已有研究表明，描述性数据标注得到的标注者级标签是模型训练的丰富信息来源。第一，它们可用于分别建模各个标注者的信念；在问答这类主观性较弱的任务上，这种做法已被用于缓解不受欢迎的标注者偏见（Geva 等，2019）。Davani 等（2021b）在辱骂检测等主观性更强的任务上重述并拓展了这一思路，表明多标注者模型架构在单标签预测上优于标准的单标签方法。第二，另一些工作并不逐个建模标注者，而是依据社会人口学属性（Al Kuwatly 等，2020）或由标注者标签导出的极化度量（Akhtar 等，2020；Akhtar 等，2021）把他们聚成簇，也得到了类似结果。第三，模型可以直接在软标签（即标注者给出的标签分布）上训练，而不必使用硬的 one-hot 真值向量（Plank 等，2014a；Jamison 与 Gurevych，2015；Uma 等，2020；Fornaciari 等，2021）。

**EN** Evaluating with Disagreement

**ZH** 借助分歧进行评测

**EN** Descriptive data annotation facilitates model evaluation that accounts for different beliefs about how a model should behave (Basile et al., 2021b; Uma et al., 2021). This is particularly relevant when deploying NLP systems for practical tasks such as content moderation, where user-facing performance needs to be considered (Gordon et al., 2021). To this end, comparing a model prediction to a descriptive label distribution, the crowd truth (Aroyo and Welty, 2015), can help estimate how acceptable the prediction would be to users (Alm, 2011). Gordon et al. (2022) operationalise this idea by introducing jury learning, a recommender system approach to predicting how a group of annotators with specified sociodemographic characteristics would judge different pieces of content.

**ZH** 描述性数据标注有助于开展这样一种模型评测：它把关于模型应当如何表现的不同信念都纳入考虑（Basile 等，2021b；Uma 等，2021）。这一点在为内容审核等实际任务部署 NLP 系统时尤为紧要，因为必须顾及面向用户的表现（Gordon 等，2021）。为此，把模型预测与描述性的标签分布即众包真值（crowd truth）（Aroyo 与 Welty，2015）相比较，有助于估计该预测对用户的可接受程度（Alm，2011）。Gordon 等（2022）将这一思路操作化，提出了陪审团学习（jury learning）——一种推荐系统式的方法，用于预测具有特定社会人口学特征的一组标注者会如何评判不同的内容。

**EN** 2.2 Key Challenges

**ZH** 2.2 主要挑战

**EN** Representativeness of Annotators

**ZH** 标注者的代表性

**EN** The survey-like benefits of descriptive data annotation correspond to survey-like challenges. First, dataset creators must decide who their data aims to represent, by establishing a clear population of interest. Arora et al. (2020), for example, ask women journalists to annotate harassment targeted at them. Talat (2016) recruits feminist activists as well as crowd workers. Second, dataset creators must consider whether representativeness can practically be achieved. To capture a representative distribution of beliefs for each entry requires dozens, if not hundreds of annotators recruited from the population of interest. Sap et al. (2021), for example, collect toxicity labels from 641 annotators, but only for 15 examples. Other datasets generally use much fewer annotators per entry (see Appx. A) and therefore cannot be considered representative in the sense that large (i.e., many-participant) surveys are. A potential approach to mitigating this issue in modelling annotator beliefs is by introducing information sharing across groups of annotators (e.g. based on sociodemographics), where annotator behaviour updates group-specific priors rather than being considered in isolation, and thus fewer annotations are needed from each annotator (Gordon et al., 2022).

**ZH** 描述性数据标注带来的调查式收益，也伴随着调查式的挑战。第一，数据集构建者必须通过明确界定目标人群，来决定其数据要代表谁。例如，Arora 等（2020）请女性记者来标注针对她们的骚扰；Talat（2016）同时招募女权主义活动者与众包工作者。第二，数据集构建者必须考虑代表性在实践中是否可达成。要为每个条目捕捉到具有代表性的信念分布，需要从目标人群中招募数十乃至数百名标注者。例如，Sap 等（2021）收集了 641 名标注者的毒性标签，但只覆盖 15 个样本。其他数据集每个条目通常使用的标注者要少得多（见附录 A），因而无法在大规模（即参与者众多）调查的意义上被视为具有代表性。在建模标注者信念时，一种可能的缓解办法是在标注者群体之间引入信息共享（例如按社会人口学特征分组），让标注者的行为更新各组的先验，而不是孤立地看待每一次标注，这样每位标注者所需的标注量就会减少（Gordon 等，2022）。

**EN** Interpretation of Disagreement

**ZH** 分歧的解读

**EN** In the descriptive paradigm, the absence of a (specified) ground truth label complicates the interpretation of any observed annotator disagreement: it may be due to a genuine difference in beliefs, which is desirable in this paradigm, or due to undesirable annotator error (Pavlick and Kwiatkowski, 2019; Basile et al., 2021a; Leonardelli et al., 2021). The same issue applies to inter-annotator agreement metrics like Fleiss’ Kappa. When subjectivity is encouraged, such metrics can at best measure task subjectiveness, but not task difficulty, annotator performance, or dataset quality (Zaenen, 2006; Alm, 2011).

**ZH** 在描述性范式下，由于不存在（被指定的）真值标签，对观察到的任何标注者分歧的解读都变得复杂：它可能源于信念的真实差异——这在该范式中正是所期望的——也可能源于不受欢迎的标注者错误（Pavlick 与 Kwiatkowski，2019；Basile 等，2021a；Leonardelli 等，2021）。同样的问题也适用于 Fleiss’ Kappa 这类标注者间一致性指标。当主观性被鼓励时，此类指标至多只能度量任务的主观程度，而无法度量任务难度、标注者表现或数据集质量（Zaenen，2006；Alm，2011）。

**EN** Label Aggregation

**ZH** 标签聚合

**EN** Descriptive annotation has clear downstream uses (§2.1) but it is fundamentally misaligned with standard NLP methods that rely on single gold standard labels. When datasets are constructed to be granular surveys of beliefs, reducing those beliefs to a single label, through majority voting or otherwise, goes directly against that purpose. Aggregating labels conceals informative disagreements (Leonardelli et al., 2021; Basile et al., 2021b) and risks discarding minority beliefs (Prabhakaran et al., 2021; Basile et al., 2021a).

**ZH** 描述性标注虽有清晰的下游用途（§2.1），却与依赖单一金标准标签的常规 NLP 方法在根本上不相契合。当数据集被构建为信念的细粒度调查时，通过多数投票或其他方式把这些信念压缩成单一标签，便与该目的背道而驰。聚合标签会掩盖富有信息量的分歧（Leonardelli 等，2021；Basile 等，2021b），并有丢弃少数派信念的风险（Prabhakaran 等，2021；Basile 等，2021a）。

**EN** 3 The Prescriptive Annotation Paradigm: Discouraging Annotator Subjectivity

**ZH** 3 规定性标注范式：抑制标注者主观性

**EN** 3.1 Key Benefits

**ZH** 3.1 主要收益

**EN** Specified Model Behaviour

**ZH** 明确规定的模型行为

**EN** Encoding one specific belief in a dataset through data annotation is difficult (§3.2) but advantageous for many practical applications. Social media companies, for example, moderate content on their platforms according to specific and extensive content policies.22 2 In March 2021, a whistleblower shared 300-page content guidelines used by Facebook moderators (Hern, 2021). Therefore, they need data annotated in accordance with those policies to train their content moderation models. This illustrates that even for highly subjective tasks, where different model behaviours are plausible and valid, one specific behaviour may be practically desirable. Prescriptive data annotation specifies such desired behaviours in datasets for model training and evaluation.

**ZH** 通过数据标注把某一种特定信念编码进数据集是困难的（§3.2），但对许多实际应用而言却很有价值。例如，社交媒体公司依据具体而详尽的内容政策来审核平台上的内容。22 2 2021 年 3 月，一名举报人公开了 Facebook 审核人员所使用的长达 300 页的内容指南（Hern，2021）。因此，它们需要依照这些政策标注的数据来训练内容审核模型。这说明，即便在主观性很强、多种模型行为都合理且成立的任务上，某一种特定行为在实践中仍可能是所期望的。规定性数据标注正是把这类期望行为在数据集里明确规定出来，供模型训练与评测使用。

**EN** Quality Assurance

**ZH** 质量保证

**EN** In the prescriptive paradigm, annotator disagreements are a call to action because they indicate that a) the annotation guidelines were not correctly applied by annotators or b) the guidelines themselves were inadequate. Annotator errors can be found using noise identification techniques (Hovy et al., 2013; Zhang et al., 2017; Paun et al., 2018; Northcutt et al., 2021, e.g.,), corrected by expert annotators (Vidgen and Derczynski, 2020; Vidgen et al., 2021a) or their impact mitigated by label aggregation. Guidelines which are unclear or incomplete need to be clarified or expanded by dataset creators, which may require iterative approaches to annotation (Founta et al., 2018; Zeinert et al., 2021). Therefore, quality assurance under the prescriptive paradigm is a laborious but structured process, with inter-annotator agreement as a useful, albeit noisy, measure of dataset quality.

**ZH** 在规定性范式下，标注者分歧是一种行动信号，它表明：a）标注者没有正确执行标注指南，或 b）指南本身有缺陷。标注者错误可以用噪声识别技术发现（例如 Hovy 等，2013；Zhang 等，2017；Paun 等，2018；Northcutt 等，2021），由专家标注者加以纠正（Vidgen 与 Derczynski，2020；Vidgen 等，2021a），或通过标签聚合来减轻其影响。不清楚或不完整的指南则需要由数据集构建者澄清或扩充，这可能需要迭代式的标注方法（Founta 等，2018；Zeinert 等，2021）。因此，规定性范式下的质量保证虽费力，却是一个有章可循的过程；标注者间一致性作为数据集质量的度量虽带有噪声，却仍然有用。

**EN** Visibility of Encoded Belief

**ZH** 所编码信念的可见性

**EN** In the prescriptive paradigm, the one belief that annotators are tasked with applying is made visible and explicit in the annotation guidelines. Well-formulated guidelines should give clear instructions on how to decide between different classes, along with explanations and illustrative examples. This creates accountability, in that people can review, challenge and disagree with the formulated belief. Like data statements (Bender and Friedman, 2018), prescriptive annotation guidelines can provide detailed insights into how datasets were created, which can then inform their downstream use.

**ZH** 在规定性范式下，标注者被要求贯彻的那一种信念，在标注指南中被明确地显明出来。表述良好的指南应当就如何在不同类别之间做出判断给出清晰指令，并附带解释与示例。这就形成了一种可问责性：人们可以审阅、质疑并反对这一被阐明的信念。与数据说明（data statements）（Bender 与 Friedman，2018）类似，规定性标注指南能够提供关于数据集如何构建的详细说明，从而为下游使用提供依据。

**EN** 3.2 Key Challenges

**ZH** 3.2 主要挑战

**EN** Creation of Annotation Guidelines

**ZH** 标注指南的制定

**EN** Creating guidelines for prescriptive data annotation is difficult because it requires topical knowledge and familiarity with the data that is to be annotated. Guidelines would ideally provide a clear judgment on every possible entry, but in practice, such perfectly comprehensive guidelines can only be approximated. Even extensive legal definitions of hate speech leave some room for subjective interpretation (Sellars, 2016). Further, creating guidelines for prescriptive data annotation requires deciding which one belief to encode in the dataset. This can be a complex process that risks disregarding non-majority beliefs if marginalised people are not included in it (Raji et al., 2020).

**ZH** 为规定性数据标注制定指南很困难，因为它需要关于待标注数据的专业知识与熟悉程度。理想的指南会对每一个可能出现的条目给出明确判断，但在实践中，这种完美周全的指南只能被逼近。即便是仇恨言论的详尽法律定义，也留有一定的主观解释空间（Sellars，2016）。此外，为规定性数据标注制定指南，还需要决定把哪一种信念编码进数据集。这可能是一个复杂的过程，若边缘化群体未被纳入其中，便有忽视非多数派信念的风险（Raji 等，2020）。

**EN** Application of Annotation Guidelines

**ZH** 标注指南的执行

**EN** Annotators need to be familiar with annotation guidelines to apply them correctly, which may require additional training, especially if guidelines are long and complex. This is reflected in an increasing shift in the literature towards using annotators with task-relevant experience over non-trained crowd workers (Basile et al., 2019; Röttger et al., 2021; Vidgen et al., 2021a, e.g.). During annotation, annotators will need to refer back to the guidelines, which requires giving them sufficient time per entry and providing a well-designed annotation interface.

**ZH** 标注者需要熟悉标注指南才能正确执行它们，这可能要求额外的培训，尤其当指南冗长而复杂时。这一点反映在文献中的一个日益增长的趋势上：相比未经培训的众包工作者，人们更倾向于选用具备任务相关经验的标注者（例如 Basile 等，2019；Röttger 等，2021；Vidgen 等，2021a）。在标注过程中，标注者需要反复查阅指南，这就要求为每个条目留出充足时间，并提供设计良好的标注界面。

**EN** Persistent Subjectivity

**ZH** 挥之不去的主观性

**EN** Annotator subjectivity can be discouraged, but not eliminated. Inevitable gaps in guidelines leave annotators no choice but to apply their personal judgement for some entries, and even when there is explicit guidance, implicit biases may persist. Sap et al. (2019), for example, demonstrate racial biases in hate speech annotation, and show that targeted annotation prompts can reduce these biases but not definitively eliminate them. To address this issue, dataset creators should work with groups of annotators that are diverse in terms of sociodemographic characteristics and personal experiences, even when annotator subjectivity is discouraged.

**ZH** 标注者主观性可以被抑制，却无法被消除。指南中不可避免的空白，使得标注者在面对某些条目时只能诉诸个人判断；即便有明确的指引，隐性偏见仍可能持续存在。例如，Sap 等（2019）揭示了仇恨言论标注中的种族偏见，并表明有针对性的标注提示语可以减轻却无法彻底消除这些偏见。针对这一问题，即便在抑制标注者主观性的情形下，数据集构建者也应当与社会人口学特征和个人经历各不相同的标注者群体合作。

**EN** 4 An Illustrative Annotation Experiment

**ZH** 4 一项示例性标注实验

**EN** Experimental Design

**ZH** 实验设计

**EN** To illustrate the contrast between the two paradigms, we conducted an annotation experiment. 60 annotators were randomly assigned to one of three groups of 20. Each group was given different guidelines to label the same 200 Twitter posts, taken from a corpus annotated for hate speech by Davidson et al. (2017), as either hateful or non-hateful. G1, the descriptive group, received a short prompt which directed them to apply their subjective judgement (‘Do you personally feel this post is hateful?’). G2, the prescriptive group, received a short prompt which discouraged subjectivity (‘Does this post meet the criteria for hate speech?’), along with detailed annotation guidelines. G3, the control group, received the prescriptive prompt and a short definition of hate speech but no further guidelines. This is to control for the difference in length and complexity of annotation guidelines between G1 and G2.

**ZH** 为说明两种范式之间的对照，我们开展了一项标注实验。60 名标注者被随机分入三个 20 人小组。每组拿到不同的指南，对取自 Davidson 等（2017）仇恨言论标注语料库的 200 条 Twitter 帖文作“仇恨”或“非仇恨”的二分类标注。G1 为描述性组，收到一段简短提示语，引导其运用主观判断（“你自己是否觉得这条帖子属于仇恨内容？”）。G2 为规定性组，收到一段抑制主观性的简短提示语（“这条帖子是否符合仇恨言论的判定标准？”），并附有详细的标注指南。G3 为对照组，收到规定性提示语与仇恨言论的简短定义，但没有更多指南。这样设置是为了控制 G1 与 G2 之间在标注指南长度与复杂度上的差异。

**EN** Results

**ZH** 结果

**EN** We evaluate average percentage agreement and Fleiss’ ⟦SLOT_2⟧ to measure dataset-level inter-annotator agreement in each group (Table 1). To test for significant differences in agreement between groups, we use confidence intervals computed with a 1000-sample bootstrap.

**ZH** 我们用平均百分比一致率与 Fleiss’ ⟦SLOT_2⟧ 来衡量各组在数据集层面的标注者间一致性（表 1）。为检验组间一致性的显著差异，我们使用以 1000 次抽样自助法计算出的置信区间。

<!-- [原子块 · table] Group Avg. % Agree. Fleiss’ κ \kappa G1 - Descriptive 73.90 0.20 G2 - Prescriptive 93.72 0.78 G3 - Control 72.50 0.15 -->

**EN** Table 1: Inter-annotator agreement metrics for the three groups of 20 annotators on our 200-post binary dataset.

**ZH** 表 1：三个 20 人标注者小组在 200 条帖文二分类数据集上的标注者间一致性指标。

**EN** Agreement is very low in the descriptive group G1 (⟦SLOT_3⟧), which suggests that annotators hold varied beliefs about which posts are hateful. However, agreement is significantly higher (⟦SLOT_4⟧) in G2 (⟦SLOT_5⟧), which suggests that a prescriptive approach with detailed annotation guidelines can successfully induce annotators to apply a specified belief rather than their subjective view. Further, agreement in the control group G3 (⟦SLOT_6⟧) is as low as in descriptive G1, which suggests that comprehensive guidelines are instrumental in facilitating high agreement in the prescriptive paradigm. G1 and G3 also do not differ systematically on which posts annotators disagree on, which suggests that annotators with little prescriptive instruction (G3) tend to apply their subjective views (like G1).

**ZH** 描述性组 G1 的一致率很低（⟦SLOT_3⟧），这说明标注者对于哪些帖子属于仇恨内容持有各不相同的信念。然而，一致率在 G2 中显著更高（⟦SLOT_4⟧），达到 ⟦SLOT_5⟧，这说明带有详细标注指南的规定性做法能够成功地引导标注者贯彻某一被指定的信念，而非诉诸个人主观看法。此外，对照组 G3（⟦SLOT_6⟧）的一致率与描述性组 G1 一样低，这说明完备的指南在规定性范式下对促成高一致性起着关键作用。G1 与 G3 在标注者产生分歧的帖子上也没有系统性差异，这说明几乎没有得到规定性指引的标注者（G3）往往会像 G1 那样诉诸主观看法。

**EN** Reproducibility

**ZH** 可复现性

**EN** For details on our dataset and annotators, see the data statement (Bender and Friedman, 2018) in Appendix B. Annotation prompts are given in Appendix C. Full guidelines, annotated data and code are available on GitHub.

**ZH** 关于我们的数据集与标注者的细节，见附录 B 中的数据说明（Bender 与 Friedman，2018）。标注提示语见附录 C。完整指南、标注数据与代码已在 GitHub 上公开。

**EN** 5 Conclusion

**ZH** 5 结论

**EN** In this article, we named and explained two contrasting paradigms for data annotation. The descriptive paradigm encourages annotator subjectivity to create datasets as granular surveys of individual beliefs, which can then be analysed and modelled. The prescriptive paradigm tasks annotators with encoding one specific belief formulated in the annotation guidelines, to enable the training of models that seek to apply that one belief to unseen data. Dataset creators should explicitly aim for one paradigm or the other to facilitate the intended downstream use of their dataset, and to document for the benefit of others how exactly their dataset was annotated. We discussed benefits and challenges in implementing both paradigms, and conducted an annotation experiment that illustrates the contrast between them. We hope that the two paradigms can support more intentional annotation process design and thus facilitate the creation of more useful NLP datasets.

**ZH** 在本文中，我们为两种相互对照的数据标注范式命名并加以阐释。描述性范式鼓励标注者主观性，把数据集构建为对个人信念的细粒度调查，从而可供分析与建模。规定性范式则要求标注者编码一种在标注指南中加以阐明的特定信念，以训练出力求将该信念贯彻到未见数据上的模型。数据集构建者应当明确地以两种范式之一为目标，以促进数据集预期下游用途的实现，并把数据集的具体标注方式记录下来以利他人。我们讨论了实施两种范式的收益与挑战，并开展了一项标注实验来展示二者之间的对照。我们希望这两种范式能促成更有意识的标注流程设计，进而推动更有用的 NLP 数据集的构建。

**EN** Acknowledgments

**ZH** 致谢

**EN** Paul Röttger was funded by the German Academic Scholarship Foundation. Bertie Vidgen and Paul Röttger were both supported by The Alan Turing Institute and Towards Turing 2.0 under the EPSRC Grant EP/W037211/1. Dirk Hovy received funding from the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation program (grant agreement No. 949944). He is a member of the Data and Marketing Insights (DMI) Unit of the Bocconi Institute for Data Science and Analysis (BIDSA). Janet B. Pierrehumbert was supported by EPSRC Grant EP/T023333/1. We thank the Milan NLP Group, the Groningen Computational Linguistics Group as well as the Pierrehumbert Language Modelling Group for helpful comments and all reviewers for their constructive feedback.

**ZH** Paul Röttger 由德国国家学术基金会（German Academic Scholarship Foundation）资助。Bertie Vidgen 与 Paul Röttger 均受艾伦·图灵研究所及 EPSRC 资助项目 EP/W037211/1 下的 Towards Turing 2.0 支持。Dirk Hovy 获得欧洲研究理事会（ERC）在欧盟“地平线 2020”研究与创新计划下的资助（协议号 949944）。他是博科尼数据科学与分析研究所（BIDSA）数据与营销洞察（DMI）部门的成员。Janet B. Pierrehumbert 受 EPSRC 资助项目 EP/T023333/1 支持。我们感谢米兰 NLP 小组、格罗宁根计算语言学小组以及 Pierrehumbert 语言建模小组提出的有益意见，也感谢所有评审者的建设性反馈。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] Akhtar et al. (2020) Sohail Akhtar, Valerio Basile, and Viviana Patti. 2020. Modeling annotator perspective and polarized opinions to improve hate speech detection. In Proceedings of the AAAI Conferen -->

<!-- [原子块 · verbatim] Akhtar et al. (2021) Sohail Akhtar, Valerio Basile, and Viviana Patti. 2021. Whose opinions matter? perspective-aware models to identify opinions of hate speech victims in abusive language detection.  -->

<!-- [原子块 · verbatim] Al Kuwatly et al. (2020) Hala Al Kuwatly, Maximilian Wich, and Georg Groh. 2020. Identifying and measuring annotator bias based on annotators’ demographic characteristics . In Proceedings of the Fourt -->

<!-- [原子块 · verbatim] AlDayel and Magdy (2021) Abeer AlDayel and Walid Magdy. 2021. Stance detection on social media: State of the art and trends. Information Processing & Management , 58(4):102597. -->

<!-- [原子块 · verbatim] Alm (2011) Cecilia Ovesdotter Alm. 2011. Subjective natural language problems: Motivations, applications, characterizations, and implications . In Proceedings of the 49th Annual Meeting of the Associa -->

<!-- [原子块 · verbatim] Arora et al. (2020) Ishaan Arora, Julia Guo, Sarah Ita Levitan, Susan McGregor, and Julia Hirschberg. 2020. A novel methodology for developing automatic harassment classifiers for Twitter . In Proceed -->

<!-- [原子块 · verbatim] Aroyo and Welty (2015) Lora Aroyo and Chris Welty. 2015. Truth is a lie: Crowd truth and the seven myths of human annotation. AI Magazine , 36(1):15–24. -->

<!-- [原子块 · verbatim] Basile et al. (2019) Valerio Basile, Cristina Bosco, Elisabetta Fersini, Debora Nozza, Viviana Patti, Francisco Manuel Rangel Pardo, Paolo Rosso, and Manuela Sanguinetti. 2019. Semeval-2019 task 5: Mu -->

<!-- [原子块 · verbatim] Basile et al. (2021a) Valerio Basile, Federico Cabitza, Andrea Campagner, and Michael Fell. 2021a. Toward a perspectivist turn in ground truthing for predictive computing. Conference of the Italian Ch -->

<!-- [原子块 · verbatim] Basile et al. (2021b) Valerio Basile, Michael Fell, Tommaso Fornaciari, Dirk Hovy, Silviu Paun, Barbara Plank, Massimo Poesio, and Alexandra Uma. 2021b. We need to consider disagreement in evaluation  -->

<!-- [原子块 · verbatim] Bender and Friedman (2018) Emily M. Bender and Batya Friedman. 2018. Data statements for natural language processing: Toward mitigating system bias and enabling better science . Transactions of the As -->

<!-- [原子块 · verbatim] Caselli et al. (2020) Tommaso Caselli, Valerio Basile, Jelena Mitrović, Inga Kartoziya, and Michael Granitzer. 2020. I feel offended, don’t be abusive! implicit/explicit messages in offensive and abus -->

<!-- [原子块 · verbatim] Cercas Curry et al. (2021) Amanda Cercas Curry, Gavin Abercrombie, and Verena Rieser. 2021. ConvAbuse: Data, analysis, and benchmarks for nuanced detection in conversational AI . In Proceedings of the -->

<!-- [原子块 · verbatim] Davani et al. (2021a) Aida Mostafazadeh Davani, Mohammad Atari, Brendan Kennedy, and Morteza Dehghani. 2021a. Hate speech classifiers learn human-like social stereotypes . -->

<!-- [原子块 · verbatim] Davani et al. (2021b) Aida Mostafazadeh Davani, Mark Díaz, and Vinodkumar Prabhakaran. 2021b. Dealing with disagreements: Looking beyond the majority vote in subjective annotations. arXiv preprint arX -->

<!-- [原子块 · verbatim] Davidson et al. (2017) Thomas Davidson, Dana Warmsley, Michael Macy, and Ingmar Weber. 2017. Automated hate speech detection and the problem of offensive language. In Proceedings of the 11th Internati -->

<!-- [原子块 · verbatim] Diaz et al. (2018) Mark Diaz, Isaac Johnson, Amanda Lazar, Anne Marie Piper, and Darren Gergle. 2018. Addressing Age-Related Bias in Sentiment Analysis , page 1–14. Association for Computing Machinery -->

<!-- [原子块 · verbatim] Fornaciari et al. (2021) Tommaso Fornaciari, Alexandra Uma, Silviu Paun, Barbara Plank, Dirk Hovy, and Massimo Poesio. 2021. Beyond black & white: Leveraging annotator disagreement via soft-label mult -->

<!-- [原子块 · verbatim] Founta et al. (2018) Antigoni Maria Founta, Constantinos Djouvas, Despoina Chatzakou, Ilias Leontiadis, Jeremy Blackburn, Gianluca Stringhini, Athena Vakali, Michael Sirivianos, and Nicolas Kourtellis -->

<!-- [原子块 · verbatim] Geva et al. (2019) Mor Geva, Yoav Goldberg, and Jonathan Berant. 2019. Are we modeling the task or the annotator? an investigation of annotator bias in natural language understanding datasets . In Pro -->

<!-- [原子块 · verbatim] Gordon et al. (2022) Mitchell L Gordon, Michelle S Lam, Joon Sung Park, Kayur Patel, Jeffrey T Hancock, Tatsunori Hashimoto, and Michael S Bernstein. 2022. Jury learning: Integrating dissenting voices -->

<!-- [原子块 · verbatim] Gordon et al. (2021) Mitchell L Gordon, Kaitlyn Zhou, Kayur Patel, Tatsunori Hashimoto, and Michael S Bernstein. 2021. The disagreement deconvolution: Bringing machine learning performance metrics in  -->

<!-- [原子块 · verbatim] Hern (2021) Alex Hern. 2021. Decoding emojis and defining ’support’: Facebook’s rules for content revealed. The Guardian . -->

<!-- [原子块 · verbatim] Hovy et al. (2013) Dirk Hovy, Taylor Berg-Kirkpatrick, Ashish Vaswani, and Eduard Hovy. 2013. Learning whom to trust with MACE . In Proceedings of the 2013 Conference of the North American Chapter of  -->

<!-- [原子块 · verbatim] Jamison and Gurevych (2015) Emily Jamison and Iryna Gurevych. 2015. Noise or additional information? leveraging crowdsource annotation item agreement for natural language tasks. In Proceedings of the  -->

<!-- [原子块 · verbatim] Jiang et al. (2021) Jialun Aaron Jiang, Morgan Klaus Scheuerman, Casey Fiesler, and Jed R Brubaker. 2021. Understanding international perceptions of the severity of harmful content online. PloS one ,  -->

<!-- [原子块 · verbatim] Justice (2006) Paul Justice. 2006. Relevant Linguistics , 2nd edition. Center for the Study of Language and Information, Stanford University. -->

<!-- [原子块 · verbatim] Kenyon-Dean et al. (2018) Kian Kenyon-Dean, Eisha Ahmed, Scott Fujimoto, Jeremy Georges-Filteau, Christopher Glasz, Barleen Kaur, Auguste Lalande, Shruti Bhanderi, Robert Belfer, Nirmal Kanagasabai, R -->

<!-- [原子块 · verbatim] Kumar et al. (2021) Deepak Kumar, Patrick Gage Kelley, Sunny Consolvo, Joshua Mason, Elie Bursztein, Zakir Durumeric, Kurt Thomas, and Michael Bailey. 2021. Designing toxic content classification for  -->

<!-- [原子块 · verbatim] Leonardelli et al. (2021) Elisa Leonardelli, Stefano Menini, Alessio Palmero Aprosio, Marco Guerini, and Sara Tonelli. 2021. Agreeing to disagree: Annotating offensive language datasets with annotator -->

<!-- [原子块 · verbatim] Luo et al. (2020) Yiwei Luo, Dallas Card, and Dan Jurafsky. 2020. Detecting stance in media on global warming . In Findings of the Association for Computational Linguistics: EMNLP 2020 , pages 3296–33 -->

<!-- [原子块 · verbatim] Northcutt et al. (2021) Curtis Northcutt, Lu Jiang, and Isaac Chuang. 2021. Confident learning: Estimating uncertainty in dataset labels. Journal of Artificial Intelligence Research , 70:1373–1411. -->

<!-- [原子块 · verbatim] Paun et al. (2018) Silviu Paun, Bob Carpenter, Jon Chamberlain, Dirk Hovy, Udo Kruschwitz, and Massimo Poesio. 2018. Comparing Bayesian models of annotation . Transactions of the Association for Compu -->

<!-- [原子块 · verbatim] Pavlick and Kwiatkowski (2019) Ellie Pavlick and Tom Kwiatkowski. 2019. Inherent disagreements in human textual inferences . Transactions of the Association for Computational Linguistics , 7:677–694. -->

<!-- [原子块 · verbatim] Plank et al. (2014a) Barbara Plank, Dirk Hovy, and Anders Søgaard. 2014a. Learning part-of-speech taggers with inter-annotator agreement loss . In Proceedings of the 14th Conference of the European Ch -->

<!-- [原子块 · verbatim] Plank et al. (2014b) Barbara Plank, Dirk Hovy, and Anders Søgaard. 2014b. Linguistically debatable or just plain wrong? In Proceedings of the 52nd Annual Meeting of the Association for Computational L -->

<!-- [原子块 · verbatim] Poria et al. (2020) Soujanya Poria, Devamanyu Hazarika, Navonil Majumder, and Rada Mihalcea. 2020. Beneath the tip of the iceberg: Current challenges and new directions in sentiment analysis research. -->

<!-- [原子块 · verbatim] Prabhakaran et al. (2021) Vinodkumar Prabhakaran, Aida Mostafazadeh Davani, and Mark Diaz. 2021. On releasing annotator-level labels and information in datasets . In Proceedings of The Joint 15th Ling -->

<!-- [原子块 · verbatim] Raji et al. (2020) Inioluwa Deborah Raji, Andrew Smart, Rebecca N. White, Margaret Mitchell, Timnit Gebru, Ben Hutchinson, Jamila Smith-Loud, Daniel Theron, and Parker Barnes. 2020. Closing the ai acc -->

<!-- [原子块 · verbatim] Röttger et al. (2021) Paul Röttger, Bertie Vidgen, Dong Nguyen, Zeerak Talat, Helen Margetts, and Janet Pierrehumbert. 2021. HateCheck: Functional tests for hate speech detection models . In Proceedin -->

<!-- [原子块 · verbatim] Salminen et al. (2019) Joni Salminen, Hind Almerekhi, Ahmed Mohamed Kamel, Soon-gyo Jung, and Bernard J. Jansen. 2019. Online hate ratings vary by extremes: A statistical analysis . In Proceedings of  -->

<!-- [原子块 · verbatim] Sap et al. (2019) Maarten Sap, Dallas Card, Saadia Gabriel, Yejin Choi, and Noah A. Smith. 2019. The risk of racial bias in hate speech detection . In Proceedings of the 57th Annual Meeting of the Ass -->

<!-- [原子块 · verbatim] Sap et al. (2021) Maarten Sap, Swabha Swayamdipta, Laura Vianna, Xuhui Zhou, Yejin Choi, and Noah A. Smith. 2021. Annotators with attitudes: How annotator beliefs and identities bias toxic language de -->

<!-- [原子块 · verbatim] Sellars (2016) Andrew Sellars. 2016. Defining hate speech. Berkman Klein Center Research Publication , 20(2016):16–48. -->

<!-- [原子块 · verbatim] Talat (2016) Zeerak Talat. 2016. Are you a racist or am I seeing things? Annotator influence on hate speech detection on Twitter . In Proceedings of the First Workshop on NLP and Computational Social  -->

<!-- [原子块 · verbatim] Talat and Hovy (2016) Zeerak Talat and Dirk Hovy. 2016. Hateful symbols or hateful people? Predictive features for hate speech detection on Twitter . In Proceedings of the NAACL Student Research Works -->

<!-- [原子块 · verbatim] Thiroux and Krasemann (2015) Jacques P Thiroux and Keith W Krasemann. 2015. Ethics: Theory and Practice , 11th edition. Pearson. -->

<!-- [原子块 · verbatim] Uma et al. (2021) Alexandra Uma, Tommaso Fornaciari, Anca Dumitrache, Tristan Miller, Jon Chamberlain, Barbara Plank, Edwin Simpson, and Massimo Poesio. 2021. SemEval-2021 task 12: Learning with disag -->

<!-- [原子块 · verbatim] Uma et al. (2020) Alexandra Uma, Tommaso Fornaciari, Dirk Hovy, Silviu Paun, Barbara Plank, and Massimo Poesio. 2020. A case for soft loss functions. Proceedings of the AAAI Conference on Human Comput -->

<!-- [原子块 · verbatim] Vidgen and Derczynski (2020) Bertie Vidgen and Leon Derczynski. 2020. Directions in abusive language training data, a systematic review: Garbage in, garbage out . PLOS ONE , 15(12):e0243300. -->

<!-- [原子块 · verbatim] Vidgen et al. (2021a) Bertie Vidgen, Dong Nguyen, Helen Margetts, Patricia Rossini, and Rebekah Tromble. 2021a. Introducing CAD: the contextual abuse dataset . In Proceedings of the 2021 Conference of -->

<!-- [原子块 · verbatim] Vidgen et al. (2021b) Bertie Vidgen, Tristan Thrush, Zeerak Talat, and Douwe Kiela. 2021b. Learning from the worst: Dynamically generated datasets to improve online hate detection . In Proceedings of  -->

<!-- [原子块 · verbatim] Zaenen (2006) Annie Zaenen. 2006. Mark-up barking up the wrong tree . Comput. Linguist. , 32(4):577–580. -->

<!-- [原子块 · verbatim] Zampieri et al. (2019) Marcos Zampieri, Shervin Malmasi, Preslav Nakov, Sara Rosenthal, Noura Farra, and Ritesh Kumar. 2019. Predicting the type and target of offensive posts in social media . In Proc -->

<!-- [原子块 · verbatim] Zeinert et al. (2021) Philine Zeinert, Nanna Inie, and Leon Derczynski. 2021. Annotating online misogyny . In Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics an -->

<!-- [原子块 · verbatim] Zhang et al. (2017) Jing Zhang, Victor S Sheng, Tao Li, and Xindong Wu. 2017. Improving crowdsourced label quality using noise correction. IEEE transactions on neural networks and learning systems , 2 -->

**EN** Appendix A Overview of Subjective Task Datasets

**ZH** 附录 A 主观性任务数据集概览

**EN** This appendix gives a selective overview of how existing NLP dataset work has (or has not) engaged with annotator subjectivity. For reasons of scope, we focus on 11 English-language datasets annotated for hate speech and other forms of abuse. Entries are sorted from most descriptive to most prescriptive annotation, based on our assessment of information made available by the dataset creators.

**ZH** 本附录选择性地概览了现有 NLP 数据集工作在多大程度上处理了标注者主观性。受篇幅所限，我们聚焦于 11 个面向仇恨言论及其他形式辱骂内容标注的英语数据集。依据我们对数据集构建者所公开信息的评估，条目按从最偏描述性到最偏规定性的顺序排列。

**EN** Sap et al. (2019) and Sap et al. (2021) annotate toxicity. They do not state explicitly that they encourage annotator subjectivity, but their annotation prompts clearly do. Each entry is labelled by up to 641 annotators. Overall, they are very aligned with the descriptive paradigm.

**ZH** Sap 等（2019）与 Sap 等（2021）标注毒性。他们并未明言鼓励标注者主观性，但其标注提示语显然如此。每个条目最多由 641 名标注者标注。总体上，它们与描述性范式高度契合。

**EN** Kumar et al. (2021) annotate toxicity and types of toxicity. They do not state explicitly that they encourage annotator subjectivity, but their annotation prompts clearly do. Each entry is labelled by five annotators. Overall, they are very aligned with the descriptive paradigm.

**ZH** Kumar 等（2021）标注毒性及毒性类型。他们并未明言鼓励标注者主观性，但其标注提示语显然如此。每个条目由五名标注者标注。总体上，它们与描述性范式高度契合。

**EN** Cercas Curry et al. (2021) annotate abuse. They gather ‘views of expert annotators’ based on guidelines that allow for significant subjectivity and do not attempt to resolve disagreements, but also do not explicitly encourage annotator subjectivity. On average, each entry is labelled by around three annotators. Overall, they are moderately aligned with the descriptive paradigm.

**ZH** Cercas Curry 等（2021）标注辱骂内容。他们依据容许较大主观性的指南收集“专家标注者的看法”，并不试图消解分歧，但也没有明确鼓励标注者主观性。平均而言，每个条目由约三名标注者标注。总体上，它们与描述性范式中等程度契合。

**EN** Talat and Hovy (2016) annotate hate speech. They provide annotators with 11 fine-grained criteria for hate speech, but several criteria invite subjective responses (e.g., ‘uses a problematic hashtag’). Each entry is labelled by up to three annotators. Overall, they are not clearly aligned with either paradigm.

**ZH** Talat 与 Hovy（2016）标注仇恨言论。他们为标注者提供了 11 条细粒度的仇恨言论判定标准，但其中若干标准会引出主观回答（例如“使用了有问题的标签”）。每个条目最多由三名标注者标注。总体上，它们与两种范式都算不上明确契合。

**EN** Davidson et al. (2017) annotate hate speech. They provide annotators with a brief definition of hate speech and an explanatory paragraph, but their definition also includes subjective criteria like perceived ‘intent’. Most entries are labelled by three annotators. Overall, they are not clearly aligned with either paradigm.

**ZH** Davidson 等（2017）标注仇恨言论。他们为标注者提供了仇恨言论的简要定义与一段说明文字，但其定义中也包含“意图”这类主观标准。多数条目由三名标注者标注。总体上，它们与两种范式都算不上明确契合。

**EN** Zampieri et al. (2019) annotate offensive content. They provide annotators with some formal criteria for offensiveness (e.g., ‘use of profanity’), but as a whole their guidelines are very brief. Each entry is labelled by up to three annotators. Overall, they are moderately aligned with the prescriptive paradigm.

**ZH** Zampieri 等（2019）标注冒犯性内容。他们为标注者提供了一些关于冒犯性的形式化标准（例如“使用脏话”），但总体而言其指南非常简略。每个条目最多由三名标注者标注。总体上，它们与规定性范式中等程度契合。

**EN** Founta et al. (2018) annotate abuse. They provide annotators with fine-grained definitions for each category and iterate on their taxonomy to facilitate more agreement, but do not share comprehensive guidelines. Each entry is labelled by five annotators. Overall, they are moderately aligned with the prescriptive paradigm.

**ZH** Founta 等（2018）标注辱骂内容。他们为每个类别提供了细粒度定义，并迭代调整其分类体系以促成更高的一致性，但没有公开完整的指南。每个条目由五名标注者标注。总体上，它们与规定性范式中等程度契合。

**EN** Caselli et al. (2020) annotate abuse. They provide annotators with a brief fine-grained decision tree with the explicit intent of reducing annotator subjectivity, and discuss disagreements to resolve them. Each entry is labelled by up to three annotators. Overall, they are moderately aligned with the prescriptive paradigm.

**ZH** Caselli 等（2020）标注辱骂内容。他们为标注者提供了一棵简短的细粒度决策树，明确意在降低标注者主观性，并通过讨论分歧加以消解。每个条目最多由三名标注者标注。总体上，它们与规定性范式中等程度契合。

**EN** Vidgen et al. (2021b) annotate hate speech. They provide annotators with fine-grained definitions for each category as well as very detailed annotation guidelines, and disagreements are resolved by an expert. Each entry is labelled by up to three annotators. Overall, they are very aligned with the prescriptive paradigm.

**ZH** Vidgen 等（2021b）标注仇恨言论。他们为每个类别提供了细粒度定义以及非常详细的标注指南，分歧由专家裁决。每个条目最多由三名标注者标注。总体上，它们与规定性范式高度契合。

**EN** Vidgen et al. (2021a) annotate abuse. They provide annotators with fine-grained definitions for each category as well as very detailed annotation guidelines, and they use expert-driven group adjudication to resolve disagreements. Each entry is labelled by up to three annotators. Overall, they are very aligned with the prescriptive paradigm.

**ZH** Vidgen 等（2021a）标注辱骂内容。他们为每个类别提供了细粒度定义以及非常详细的标注指南，并采用专家主导的小组裁定来消解分歧。每个条目最多由三名标注者标注。总体上，它们与规定性范式高度契合。

**EN** Appendix B Data Statement

**ZH** 附录 B 数据说明

**EN** Following Bender and Friedman (2018), we provide a data statement, which documents the generation and provenance of the dataset used for our annotation experiment.

**ZH** 遵循 Bender 与 Friedman（2018），我们提供一份数据说明，记录标注实验所用数据集的生成过程与来源。

**EN** A. CURATION RATIONALE

**ZH** A. 语料构建理由

**EN** To create our dataset, we sampled 200 Twitter posts from a larger corpus annotated for hateful content by Davidson et al. (2017). Of the posts we sampled, 100 were originally annotated as hateful and 100 as non-hateful by majority vote between three annotators. We sampled only from those posts that had some disagreement among their annotators (i.e., two out of three rather than unanimous agreement), to encourage disagreement in our experiment. The purpose of our 200-post dataset is to enable the annotation experiment presented in §1, which illustrates the contrast between the descriptive and prescriptive data annotation paradigms.

**ZH** 为构建我们的数据集，我们从 Davidson 等（2017）标注了仇恨内容的更大规模语料库中抽样了 200 条 Twitter 帖文。在我们抽样的帖文中，100 条最初由三名标注者以多数投票标为仇恨内容，100 条标为非仇恨。我们只从那些标注者之间存在一定分歧（即三人中有两人意见一致，而非全票一致）的帖子中抽样，以在实验中鼓励分歧的产生。这 200 条帖文数据集的用途，是支撑 §1 所介绍的标注实验，该实验展示了描述性与规定性数据标注范式之间的对照。

**EN** B. LANGUAGE VARIETY

**ZH** B. 语言变体

**EN** The dataset contains English-language text posts only.

**ZH** 数据集仅包含英语文本帖文。

**EN** C. SPEAKER DEMOGRAPHICS

**ZH** C. 发言者人口统计

**EN** All speakers are Twitter users. Davidson et al. (2017) do not share any information on their demographics.

**ZH** 所有发言者均为 Twitter 用户。Davidson 等（2017）未公开任何关于其人口统计特征的信息。

**EN** D. ANNOTATOR RECRUITMENT

**ZH** D. 标注者招募

**EN** We recruited three groups of 20 annotators using Amazon’s Mechanical Turk crowdsourcing marketplace.33 3 https://www.mturk.com/. Annotators were made aware that the task contained instances of offensive language before starting their work, and they could withdraw at any point throughout the work.

**ZH** 我们通过 Amazon 的 Mechanical Turk 众包平台招募了三组各 20 名标注者。33 3 https://www.mturk.com/. 标注者在开始工作前已被告知任务中包含攻击性语言的实例，且可在工作全程随时退出。

**EN** E. ANNOTATOR DEMOGRAPHICS

**ZH** E. 标注者人口统计

**EN** All annotators were at least 18 years old when they started their work, and we recruited only annotators that were based in the UK. This was to facilitate comparability across groups of annotators. For each group, we recruited 10 male and 10 female annotators, based on self-reported gender. This was to encourage disagreement within groups, based on the assumption that men would on average disagree more about hateful content with women than with other men, and vice versa. No further annotator demographics were recorded.

**ZH** 所有标注者在开始工作时均已年满 18 岁，且我们只招募身处英国的标注者，这是为了便于在标注者小组之间进行比较。每个小组我们招募了 10 名男性与 10 名女性标注者，性别依据自我报告确定。这样做是为了鼓励组内分歧，其假设是：男性与女性在仇恨内容上的平均分歧程度，会高于男性与男性之间的分歧，反之亦然。除此以外，未记录更多标注者人口统计信息。

**EN** F. ANNOTATOR COMPENSATION

**ZH** F. 标注者报酬

**EN** All annotators were compensated for their work at a rate of at least £16 per hour. The rate was set 50% above the London living wage (£10.85), although all work was completed remotely.

**ZH** 所有标注者获得的报酬不低于每小时 16 英镑。该标准被设定为比伦敦生活工资（10.85 英镑）高出 50%，尽管全部工作都是远程完成的。

**EN** G. SPEECH SITUATION

**ZH** G. 发言情境

**EN** All entries in our dataset were originally posted to Twitter and then collected by Davidson et al. (2017), who do not share when the posts were made.

**ZH** 我们数据集中的所有条目最初都发布于 Twitter，随后由 Davidson 等（2017）收集，而他们并未公开这些帖文的发布时间。

**EN** H. TEXT CHARACTERISTICS

**ZH** H. 文本特征

**EN** All entries in our dataset are individual Twitter text posts, with a length of 140 characters or less. We perform only minimal text cleaning, replacing user mentions (e.g., "@Obama") with "[USER]" and URLs with "[URL]".

**ZH** 我们数据集中的所有条目均为单条 Twitter 文本帖文，长度不超过 140 个字符。我们只做了最低限度的文本清洗，把用户提及（例如 “@Obama”）替换为 “[USER]”，把 URL 替换为 “[URL]”。

**EN** I. LICENSE

**ZH** I. 许可

**EN** Davidson et al. (2017) make the Twitter data they collected available for further research use via GitHub under an MIT license.44 4 https://github.com/t-davidson/hate-speech-and-offensive-language Our re-annotated subset of the data is made available under CC0-1.0 license at github.com/paul-rottger/annotation-paradigms, so that the results of our experiment can be reproduced.

**ZH** Davidson 等（2017）以 MIT 许可通过 GitHub 公开其收集的 Twitter 数据，供进一步研究使用。44 4 https://github.com/t-davidson/hate-speech-and-offensive-language 我们重新标注的数据子集以 CC0-1.0 许可发布于 github.com/paul-rottger/annotation-paradigms，以便复现实验结果。

**EN** J. ETHICS APPROVAL

**ZH** J. 伦理审批

**EN** We received approval for our experiment and the data annotation it entailed from our institution’s ethics review board.

**ZH** 我们的实验及其所涉及的数据标注已获得本单位伦理审查委员会的批准。

**EN** Appendix C Annotation Prompts

**ZH** 附录 C 标注提示语

**EN** The three groups of annotators in our experiment all annotated the same data in the same order, but each group received different annotation prompts. The full annotation guidelines for G2 are available at github.com/paul-rottger/annotation-paradigms.

**ZH** 实验中三组标注者以相同顺序标注同一批数据，但各组收到的标注提示语不同。G2 的完整标注指南见 github.com/paul-rottger/annotation-paradigms。

**EN** G1 - Descriptive Group

**ZH** G1——描述性组

**EN** “Imagine you come across the post below on social media. Do you personally feel this post is hateful? We want to understand your own opinions, so try to disregard any impressions you might have about whether other people would find it hateful.”

**ZH** “想象你在社交媒体上看到下面这条帖子。你自己是否觉得这条帖子属于仇恨内容？我们想了解你自己的看法，因此请尽量不去考虑别人会不会觉得它属于仇恨内容。”

**EN** G2 - Prescriptive Group

**ZH** G2——规定性组

**EN** “Imagine you come across the post below on social media. Does this post meet the criteria for hate speech? We are trying to collect objective judgments, so try to disregard any feelings you might have about whether you personally find it hateful.

**ZH** “想象你在社交媒体上看到下面这条帖子。这条帖子是否符合仇恨言论的判定标准？我们试图收集客观的判断，因此请尽量不去理会你自己是否觉得它属于仇恨内容。

**EN** Click here to view the criteria: LINK”

**ZH** 点击此处查看判定标准：链接”

**EN** G3 - Control Group

**ZH** G3——对照组

**EN** “Imagine you come across the post below on social media. Does this post meet the criteria for hate speech? A post is considered hate speech if it is 1) abusive and 2) targeted against a protected group (e.g., women) or at its members for being a part of that group.”

**ZH** “想象你在社交媒体上看到下面这条帖子。这条帖子是否符合仇恨言论的判定标准？一条帖子若 1）具有辱骂性且 2）针对某一受保护群体（例如女性）或其成员之所以属于该群体，则被视为仇恨言论。”
