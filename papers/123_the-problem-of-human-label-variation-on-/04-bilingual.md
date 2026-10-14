# 人类标注变异这一“问题”：数据、建模与评测中的真值

> 原标题：The 'Problem' of Human Label Variation: On Ground Truth in Data, Modeling and Evaluation
> 作者：Barbara Plank · arXiv:2211.02570 · 2022-11-04

<!-- [原子块 · verbatim] The “Problem” of Human Label Variation: On Ground Truth in Data, Modeling and Evaluation -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] Human variation in labeling is often considered noise. Annotation projects for machine learning (ML) aim at minimizing human label variation, with the assumption to maximize data quality and in turn o -->

**EN** 1 Introduction

**ZH** 1 引言

**EN** In Natural Language Processing (NLP) much progress today is driven by fine-tuning large pre-trained language models using an annotated dataset, assumed to be representative for a target language task of interest Schlangen (2021). This is analogously so in Machine Learning (ML) and Computer Vision (CV), where the target tasks differ, yet the conceptual pipeline remains the same: data, modeling, evaluation. Despite the importance of annotated data—as it fuels all steps in this pipeline—a crucial assumption of today’s learning systems is to rely on a single gold label per instance. The gold label is obtained by aggregation (e.g. majority vote) of labels crucially provided by humans.

**ZH** 在自然语言处理（NLP）中，当下的多数进展由这样一种做法驱动：用标注数据集微调大规模预训练语言模型，并假定该数据集足以代表所关注的目标语言任务 Schlangen（2021）。机器学习（ML）与计算机视觉（CV）中的情形类似，目标任务虽不相同，概念流程却保持一致：数据、建模、评测。标注数据支撑着这条流程的每一步，然而当今学习系统的一项关键假设是，每个实例只取用单一的金标签（gold label）。该金标签由人类给出的标注聚合而成，例如多数投票。

**EN** @goptd@color\pc@hyenc@colorpdfcommentcolor\HyColor@XZeroOneThreeFour\pc@goptd@fontcolor\pc@hyenc@fontcolorpdfcommentcolor\HyColor@XZeroOneThreeFour\pc@goptd@icolor\pc@hyenc@icolorpdfcommentcolor\pdfmark[⟦SLOT_0⟧ ]pdfmark=/ANN,Subtype=/Widget,Raw=/TU (Screenreader caption: Schematic of human label variation vs annotation errors. Disagreement in annotation can be due to genuine annotator disagreement, subjectivity or simply because two (or more) views are plausible. \textCR(\pc@goptd@deadline)) /T (tooltip zref@0) /C [ ] /FT/Btn /F 768 /Ff 65536 /H/N /BS << /W 0 >>

**ZH** （原文此处为 LaTeX 排版宏与 PDF 注释源码，其中的屏幕阅读器说明文字为：人类标注变异与标注错误的示意图。标注中的不一致可能源于标注者真实的分歧、主观性，或仅仅因为两种（或多种）看法都成立。）⟦SLOT_0⟧

**EN** Figure 1: We propose the term human label variation to capture the fact that inherent disagreement in annotation can be due to genuine disagreement, subjectivity or simply because two (or more) views are plausible.

**ZH** 图 1：我们提出“人类标注变异”这一术语，用以刻画如下事实：标注中固有的不一致可能源于真实的分歧、主观性，或仅仅因为两种（或多种）看法都成立。

**EN** The assumption of a ground truth (and taking the majority vote or the ‘mode’ of the human judgement distribution) makes sense when humans involved in labeling highly agree on the answer to the questions, such as “Does this image contain a bird?”, “Is ‘learn’ a verb?”, “What is the capital of Italy?". However, this assumption often does not make sense—especially when language is involved. For example, on questions determining a word sense, questions such as “Is this comment toxic?” or questions involving understanding indirect answers to polar questions like “Q: Hey. Everything ok?” “A: I’m just mad at my agent” (see more examples in Figure 2). While some disagreement is due to human labeling errors (cf. Figure 1 arrow to the left and § 3), an increasing body of work has shown that irreconcilable variation between annotations is plausible and abundant Plank et al. (2014b); Aroyo and Welty (2015); Pavlick and Kwiatkowski (2019); Uma et al. (2021b) (illustrated in Figure 1). The observed variation can indeed be disagreement due to difficult cases, subjectivity or cases where multiple answers are plausible (cf. § 2). We argue that human label variation (Hlv) provides rich information that should not be discarded. Critically, to rely on a ground truth means we tacitly agree to continue: i) to create datasets that encode a single ground truth, ii) to develop models that are optimized towards a single preferred output, and iii) to evaluate models against a single ground truth. By continuing to do so, we might ask ourselves if we are climbing the right hill–or whether continuing to model a single ground truth hampers progress.

**ZH** 当参与标注者对问题答案高度一致时，例如“这张图里有鸟吗？”“learn 是动词吗？”“意大利的首都是什么？”，假定存在真值（ground truth）并取人类判断分布的众数或多数票，是合理的。然而一旦牵涉语言，这一假定往往就不再成立，比如判定词义的问题、“这条评论有毒吗？”这类问题，以及需要理解极性问句间接回答的问题，如“Q：嘿，一切都还好吗？”“A：我只是生我经纪人的气”（更多示例见图 2）。部分分歧确实来自人工标注错误（参见图 1 中向左的箭头与第 3 节），但越来越多的研究表明，标注之间不可调和的差异既合理又普遍 Plank 等（2014b）；Aroyo 与 Welty（2015）；Pavlick 与 Kwiatkowski（2019）；Uma 等（2021b）（图 1 给出了示意）。观察到的变异确实可能源自困难样例、主观性，或多个答案皆成立的情形（参见第 2 节）。我们认为，人类标注变异（HLV）蕴含丰富信息，不应被丢弃。关键在于，依赖真值意味着我们默认继续三件事：其一，构建只编码单一真值的数据集；其二，开发朝单一偏好输出优化的模型；其三，以单一真值为准绳评测模型。长此以往，我们应当自问是否在攀登正确的山峰，抑或继续围绕单一真值建模反而阻碍了进步。

**EN** In this position paper, we argue that neglecting variation in labeling is problematic, as it impacts all steps of the pipeline. Traditionally, this variation has been considered a problem. We underline emerging works that instead believe this issue to be an opportunity. In fact, we believe it is essential to take human label variation into account for progress. Human labels are bound to be scarce yet at the same time critical as they provide human interpretations and values. Therefore, embracing it is necessary for human-facing NLP, i.e., technology which is by and for humans; inclusive and reliable. However, the research landscape is fragmented, and approaches often focus on either steps of the pipeline. Therefore, in this paper we focus on the three core aspects of the pipeline: data, modeling and evaluation. In particular, i) we distill some of the on-going discussions in disparate (sub-)fields and propose a unified term; ii) we present and work out suggestions for each for the future; and iii) we provide a comprehensive repository of publicly-available data sets that allow studying human label variation, and invite the community to contribute.

**ZH** 在这篇立场论文中，我们认为忽视标注变异会带来问题，因为它影响流程的每一个环节。传统上，这种变异被视为一个问题；我们则着重指出那些新兴工作，它们反将其视为机遇。事实上，要想取得进展，就必须把人类标注变异纳入考量。人类标注注定稀缺，却又至关重要，因为其中承载了人的解读与价值。因此，接纳这种变异是面向人类的 NLP 的必要条件，即那种由人创造、为人服务、兼具包容性与可靠性的技术。然而当前研究格局十分零散，各类方法往往只针对流程中的某一个环节。因此，本文聚焦于流程的三个核心方面：数据、建模与评测。具体而言：其一，提炼不同（子）领域正在进行的讨论，并提出一个统一的术语；其二，针对上述三方面分别给出建议并加以阐发；其三，提供一个全面的公开数据集清单，供研究人类标注变异之用，并邀请学界共同贡献。

**EN** 2 Data and Human Label Variation

**ZH** 2 数据与人类标注变异

**EN** High-quality data is essential for any empirical scientific inquiry and has to satisfy the requirements of validity and reliability Krippendorff (2018); Pustejovsky and Stubbs (2012); Schlangen (2021). However, for almost all tasks in NLP and CV irreconcilable disagreement between annotators has been observed Uma et al. (2021b). In light of this, the original definition of data reliability is questionable—it assumes labels follow a given standard. We might ask which standard?

**ZH** 高质量数据对任何实证科学探究都不可或缺，且必须满足效度与信度的要求 Krippendorff（2018）；Pustejovsky 与 Stubbs（2012）；Schlangen（2021）。然而，在 NLP 与 CV 的几乎所有任务中，都观察到了标注者之间不可调和的分歧 Uma 等（2021b）。如此一来，数据信度的原有定义便值得怀疑：它假定标注遵循某个既定标准。问题在于，是哪个标准？

**EN** Human annotations are needed to ground and make sense of language, images, speech etc. However, labelling data is difficult, particularly when dealing with an object of study as complex as language. Take the illustration in Figure 2 as example. While categories exist, their boundaries are fluid, or simply multiple options are plausible.

**ZH** 人类标注是理解语言、图像、语音等并为其赋予意义的基础。然而，数据标注本身困难重重，尤其当研究对象像语言这样复杂时。以图 2 的示例来看：类别虽然存在，其边界却是流动的，或者干脆有多个选项同时成立。

**EN** Disagreement or variation?

**ZH** 分歧还是变异？

**EN** We define human label variation (Hlv) as plausible variation in annotation, see Figure 1, to reconcile different notions found in the literature (discussed next). We prefer ‘variation’, because ‘disagreement’ implies that two (or more) views involved cannot all hold. In contrast, errors are annotation differences, due to amongst others attention slips. Crucially, Hlv assumes humans usually provide their best judgements, and variation emerges due to, e.g., ambiguity of the instance, uncertainty of the annotator, genuine disagreement, or simply the fact that multiple options are correct. Aggregation obfuscates this real-world complexity.

**ZH** 我们将人类标注变异（HLV）定义为标注中合理的变异（见图 1），以此来调和文献中的不同说法。我们偏好“变异”而非“分歧”，因为后者暗示所涉的两种（或多种）看法不可能同时成立。相反，错误指的是因注意力疏漏等原因造成的标注差异。关键的一点在于，HLV 假定标注者通常已给出其最佳判断，变异的产生源于实例本身的歧义、标注者的不确定、真实存在的分歧，或仅仅因为多个选项都正确。聚合操作掩盖了现实世界的这种复杂性。

**EN** @goptd@color\pc@hyenc@colorpdfcommentcolor\HyColor@XZeroOneThreeFour\pc@goptd@fontcolor\pc@hyenc@fontcolorpdfcommentcolor\HyColor@XZeroOneThreeFour\pc@goptd@icolor\pc@hyenc@icolorpdfcommentcolor\pdfmark[⟦SLOT_1⟧]pdfmark=/ANN,Subtype=/Widget,Raw=/TU (Screenreader caption: The figure illustrates three hard cases. Case 1: What is the sentiment (positive, neutral, negative) of ‘This was an excellent offer and i didn’t not enjoy it’. Case 2: Does A entail B? ‘A: Paola drinks oat milk’ ‘B: Paolo drinks milk.’. Case 3: It shows a low-resolution image, the question is whether it is a cat or a dog or another animal.\textCR(\pc@goptd@deadline)) /T (tooltip zref@1) /C [ ] /FT/Btn /F 768 /Ff 65536 /H/N /BS << /W 0 >>

**ZH** （原文此处为 LaTeX 排版宏与 PDF 注释源码，其中的屏幕阅读器说明文字为：该图展示了三个困难样例。样例 1：‘This was an excellent offer and i didn’t not enjoy it’ 的情感是什么（正面、中性、负面）？样例 2：A 是否蕴含 B？‘A: Paola drinks oat milk’、‘B: Paolo drinks milk.’。样例 3：图中是一张低分辨率图像，问题是它究竟是猫、狗还是其他动物。）⟦SLOT_1⟧

**EN** Figure 2: Hard cases. Image from Uma et al. (2021b).

**ZH** 图 2：困难样例。图片取自 Uma 等（2021b）。

**EN** Hlv has been studied in CV, where it is dubbed human uncertainty Peterson et al. (2019), as well as in human-computer interaction (HCI) as disagreement or contested labels Gordon et al. (2021). In NLP, variation has been acknowledged as annotator disagreement already in early works on resolving disagreement Poesio and Artstein (2005), particularly in pragmatics and discourse de Marneffe et al. (2012); Webber and Joshi (2012); Das et al. (2017). Hlv in NLP is discussed both from the linguistic side as hard cases Zeman (2010); Plank et al. (2014b), difficult linguistic cases Manning (2011), as judgements which are not always categorical de Marneffe et al. (2012), inherent disagreement Pavlick and Kwiatkowski (2019); Davani et al. (2022) and justified and informative disagreement Sommerauer et al. (2020). Variation in NLP is also discussed in connection to subjectivity, e.g., as a range of reasonable interpretations (CrowdTruth) Aroyo and Welty (2015), as one or many beliefs Rottger et al. (2022), the social dimensions of annotators like their demographic Sap et al. (2019); Larimore et al. (2021); Sap et al. (2022) and cultural backgrounds Hershcovich et al. (2022), often discussed more generally as different perceptions in data perspectivisim Basile et al. (2021a); Wich et al. (2021). Moreover, there is work that acknowledges that multiple plausible answers are correct, such as works on the collective human opinion Nie et al. (2020) influenced by seminal work that looks at the human judgement distribution Pavlick and Kwiatkowski (2019) who found plausible variation in at least 20% of their data. Earlier work on veridicality also made this point de Marneffe et al. (2012). The fact that multiple plausible annotations exist has also been put forward as a range of acceptable annotations Palomaki et al. (2018). The known variation in annotation for subjective tasks is at least a decade old Alm (2011). They suggest that in the absence of a real ‘ground truth’, acceptability may be a more useful concept than ‘right’ and ‘wrong’. Capturing the Hlv, instead of the global majority, aligns with this viewpoint.

**ZH** HLV 在 CV 中已有研究，那里称之为人类不确定性（human uncertainty）Peterson 等（2019）；在人机交互（HCI）领域则以分歧或争议性标签（contested labels）的面目出现 Gordon 等（2021）。在 NLP 中，早在消解分歧的早期工作里，变异就被承认为标注者分歧 Poesio 与 Artstein（2005），语用学与篇章研究尤其如此 de Marneffe 等（2012）；Webber 与 Joshi（2012）；Das 等（2017）。NLP 中的 HLV 也从语言学角度得到讨论：困难样例 Zeman（2010）；Plank 等（2014b）、困难的语言学样例 Manning（2011）、并非总是范畴性的判断 de Marneffe 等（2012）、固有分歧 Pavlick 与 Kwiatkowski（2019）；Davani 等（2022），以及有据可循且富有信息量的分歧 Sommerauer 等（2020）。NLP 中的变异还与主观性联系在一起加以讨论，例如被视为一系列合理解读（CrowdTruth）Aroyo 与 Welty（2015）、一种或多种信念 Rottger 等（2022），以及与标注者的社会维度相关，如人口统计特征 Sap 等（2019）；Larimore 等（2021）；Sap 等（2022）和文化背景 Hershcovich 等（2022），更一般地则被讨论为数据中的不同感知，即视角主义（perspectivism）Basile 等（2021a）；Wich 等（2021）。此外，也有工作承认多个合理答案同时成立，例如关于集体人类意见的研究 Nie 等（2020），其受考察人类判断分布的开创性工作影响 Pavlick 与 Kwiatkowski（2019）——后者发现其数据中至少 20% 存在合理变异。更早的真实性（veridicality）研究也已指出这一点 de Marneffe 等（2012）。存在多种合理标注这一事实，还被表述为可接受的标注区间 Palomaki 等（2018）。主观性任务中标注变异的已知存在至少已有十年 Alm（2011）。他们提出，在真正的“真值”缺席时，可接受性也许是比“对”与“错”更有用的概念。捕捉 HLV 而非全局多数，正与这一观点相合。

**EN** Open issues and our suggestions

**ZH** 开放问题与我们的建议

**EN** To make progress, we need to i) collect and release annotator-level (un-aggregated) labels, ii) document dataset creation, and iii) include as much meta-data as possible. In particular, we urge the community to release annotator-level (un-aggregated) labels–even if only for a small subset of the data–and thus we echo Basile et al. (2021b) and Prabhakaran et al. (2021) (also in Denton et al. (2021)) who independently raised this point as well.

**ZH** 要取得进展，我们需要做到三点：其一，收集并发布标注者层面（未聚合）的标签；其二，记录数据集的构建过程；其三，尽可能纳入更多元数据。我们尤其呼吁学界发布标注者层面的未聚合标签——哪怕只针对一小部分数据——这也呼应了 Basile 等（2021b）与 Prabhakaran 等（2021）（另见 Denton 等（2021））各自独立提出的同样主张。

**EN** As a concrete starting point, we provide a comprehensive overview of existing datasets with multiple annotations in the appendix, which we release as a github repository to encourage uptake. Moreover, if possible to release responsibly, besides making data statements of datasets available Bender and Friedman (2018), we encourage the community to include annotator-level background information Prabhakaran et al. (2021) and document the annotation process Geiger et al. (2020). In general, we believe there is high value in releasing any meta-data available (ideally on the instance level, e.g. source, time of document, annotator ids, annotation completion time etc). For example, in a recent study we created a new relation extraction corpus with instance-level flags of annotator uncertainty proving valuable for evaluation Bassignana and Plank (2022). Similarly, we asked the annotator to provide free-text rationales of relations, which recently was also put forward in Borin (2022), referring to earlier work on collecting annotator rationals during annotation McDonnell et al. (2016).

**ZH** 作为一个具体的起点，我们在附录中给出已有多重标注数据集的全面概览，并以 GitHub 仓库的形式发布，以促进其被采用。此外，在能够负责任地公开的前提下，除提供数据集的数据说明（data statements）Bender 与 Friedman（2018）外，我们还鼓励学界纳入标注者层面的背景信息 Prabhakaran 等（2021），并记录标注过程 Geiger 等（2020）。一般而言，我们认为公开任何可得的元数据都很有价值，且最好细化到实例层面，例如来源、文档的发布时间、标注者 ID、标注完成时间等。举例来说，在最近的一项研究中，我们构建了一个新的关系抽取语料库，其中带有实例级的标注者不确定性标记，这些标记在评测中被证明很有价值 Bassignana 与 Plank（2022）。类似地，我们要求标注者以自由文本说明关系的判定理由；这一做法最近也在 Borin（2022）中被提出，并援引了更早关于在标注过程中收集标注者理由的工作 McDonnell 等（2016）。

**EN** We believe that the more, richer datasets become available, the more insights can be generated into the capabilities of models and their limitations. New algorithms may emerge capable of learning from fewer but richer sources. On a related line, collecting multiple annotations calls for research in estimating data quality and revisiting agreement measures; e.g., new measures for multiple-labels were recently proposed Marchal et al. (2022).

**ZH** 我们认为，可得的数据集越丰富、越多，就越能洞察模型的能力与局限。能够用更少但更丰富的来源进行学习的新算法也可能随之出现。与此相关的一个方向是，收集多重标注会带动数据质量估计与一致性度量研究的重新审视；例如，最近已有针对多标签的新度量被提出 Marchal 等（2022）。

**EN** 3 Modeling and Human Label Variation

**ZH** 3 建模与人类标注变异

**EN** There is a growing literature on methods on how to deal with Hlv in learning. We categorize them into two camps: those that resolve variation, and those that embrace it. We will draw connections to surveys and the emerging literature, and discuss adoption of methods as well as gaps.

**ZH** 关于如何在学习中处理 HLV，文献正在增长。我们将其划分为两大阵营：消解变异的一派与接纳变异的一派。下文将建立与相关综述及新兴文献的联系，并讨论各类方法的采用情况与空白。

**EN** The first big camp of research aims at resolving human label variation and includes: 1) Aggregation and 2) Filtering. It considers Hlv as “problematic” or “noisy”. Consequently, a single (aggregated) label is obtained with presumably high agreement as the ground truth. Aggregation is performed via majority voting or probabilistic aggregation methods, see Paun et al. (2022) for a survey and seminal works Dawid and Skene (1979); Qing et al. (2014); Artstein and Poesio (2008). Aggregation is still the most widely-adopted solution for the problem today. However, aggregation by definition allows only one belief/label/category. This is very limiting, as often it is not just about disagreement or matter of subjectivity, but multiple options being plausible. Filtering methods are advocated by some with the idea to remove data instances with low agreement Reidsma and Carletta (2008); Reidsma and op den Akker (2008); Beigman Klebanov et al. (2008); Beigman and Beigman-Klebanov (2009). However, only using high-agreement instances can yield worse performance Jamison and Gurevych (2015) and it wastes data.

**ZH** 第一大阵营的研究旨在消解人类标注变异，包括两类做法：1）聚合与 2）过滤。它将 HLV 视为“有问题”或“有噪声”，进而以假定一致性较高的单一（聚合）标签作为真值。聚合通过多数投票或概率聚合方法实现，相关综述见 Paun 等（2022），开创性工作见 Dawid 与 Skene（1979）；Qing 等（2014）；Artstein 与 Poesio（2008）。聚合至今仍是这一问题上采用最广的解决方案。然而聚合在定义上只允许一种信念、标签或类别，这限制极大，因为问题往往不只是分歧或主观性，而是多个选项都成立。也有研究者主张过滤，即移除一致性低的数据实例 Reidsma 与 Carletta（2008）；Reidsma 与 op den Akker（2008）；Beigman Klebanov 等（2008）；Beigman 与 Beigman-Klebanov（2009）。然而，只使用高一致性实例可能导致性能下降 Jamison 与 Gurevych（2015），也浪费了数据。

**EN** The second camp of research instead aims at embracing human label variation. Two broad directions include: 3) Learning from un-aggregated labels (directly), or 4) Enriching gold with human label variation. With regard to learning from un-aggregated labels, methods of varying complexity exist, from model-agnostic methods such as repeated labeling Sheng et al. (2008) used by e.g. de Marneffe et al. (2012), to architecture-specific choices, e.g., adding a crowd layer Rodrigues and Pereira (2018), learning from soft labels Peterson et al. (2019) and more; see the survey of Uma et al. (2021b). So far learning from un-aggregated labels directly has shown greater promise in classification tasks in CV than in NLP Uma et al. (2021b) (evidence is scarce, see open issues). Within NLP, a more studied direction is currently to enrich the gold label with human label variation, i.e., to learn from both the gold and the un-aggregated labels. Methods in this category can be seen as part of the broader set of well-known regularization methods in ML, and for NLP include e.g., cost-sensitive loss weighting Plank et al. (2014a), variants of multi-task learning Cohn and Specia (2013); Fornaciari et al. (2021); Davani et al. (2022), or sequential fine-tuning Lalor et al. (2017). These methods further differ in how they use un-aggregated labels, i.e., as confusion matrices estimated from a small sample Plank et al. (2014a), as annotator-level auxiliary tasks requiring the full data with multiple labels Cohn and Specia (2013); Davani et al. (2022), or as single “soft-label” auxiliary task that captures the per-instance human label distribution Fornaciari et al. (2021).

**ZH** 第二大阵营则致力于接纳人类标注变异，包含两个宽泛方向：3）直接从未聚合标签学习，或 4）用人类标注变异来丰富金标签。就从未聚合标签学习而言，现有方法的复杂度不一，既有重复标注 Sheng 等（2008）这类与模型无关的方法（如 de Marneffe 等（2012）所采用），也有针对特定架构的选择，例如增加众包层（crowd layer）Rodrigues 与 Pereira（2018）、从软标签学习 Peterson 等（2019）等，详见 Uma 等（2021b）的综述。迄今，直接从未聚合标签学习在 CV 的分类任务上比在 NLP 中展现出更大前景 Uma 等（2021b）（相关证据仍然稀缺，见开放问题）。在 NLP 内部，目前研究较多的是用人类标注变异丰富金标签，即同时从金标签与未聚合标签中学习。这一类方法可视为 ML 中广为人知的正则化方法的延伸，在 NLP 中包括代价敏感的损失加权 Plank 等（2014a）、多任务学习的变体 Cohn 与 Specia（2013）；Fornaciari 等（2021）；Davani 等（2022），以及序贯微调 Lalor 等（2017）。这些方法的进一步差异在于如何使用未聚合标签：作为由小样本估计出的混淆矩阵 Plank 等（2014a）、作为需要全部数据带多重标签的标注者级辅助任务 Cohn 与 Specia（2013）；Davani 等（2022），或作为刻画逐实例人类标签分布的单一“软标签”辅助任务 Fornaciari 等（2021）。

**EN** @goptd@color\pc@hyenc@colorpdfcommentcolor\HyColor@XZeroOneThreeFour\pc@goptd@fontcolor\pc@hyenc@fontcolorpdfcommentcolor\HyColor@XZeroOneThreeFour\pc@goptd@icolor\pc@hyenc@icolorpdfcommentcolor\pdfmark[⟦SLOT_2⟧]pdfmark=/ANN,Subtype=/Widget,Raw=/TU (Screenreader caption: The graph shows a bar chat with counts of NLP paper per year that release unaggregated labels. The plot suggests an upward trend.\textCR(\pc@goptd@deadline)) /T (tooltip zref@2) /C [ ] /FT/Btn /F 768 /Ff 65536 /H/N /BS << /W 0 >>

**ZH** （原文此处为 LaTeX 排版宏与 PDF 注释源码，其中的屏幕阅读器说明文字为：该图是一幅柱状图，按年份统计发布未聚合标签的 NLP 论文数量，图中呈现上升趋势。）⟦SLOT_2⟧

**EN** Figure 3: NLP Resource papers per publication year, counting publicly-available datasets released with human label variation (multiple annotator-labels per instance), cf. details in Table 1 in the Appendix.

**ZH** 图 3：按发表年份统计的 NLP 资源论文数量，统计对象为公开发布的、带有 HLV 数据（每个实例有多个标注者标签）的数据集，详见附录表 1。

**EN** Open issues and our suggestions

**ZH** 开放问题与我们的建议

**EN** Undoubtedly, there is increasing interest in studying methods to learn with human label variation (see Figure 3 for our analysis of research papers). However, existing research is fragmented across (sub)-disciplines. We identify at least three diverse areas within NLP, with little to no overlap (as shown in Table 1 in the Appendix), focusing respectively on: subjectivity Basile et al. (2021a) (pdai.info, SemEval 23), natural language inference (NLI) Pavlick and Kwiatkowski (2019); Nie et al. (2020), and both NLP and CV (JAIR & SemEval 21). To the best of our knowledge, only the latter work and shared task so far bridges across disciplines Uma et al. (2021b); Uma et al. (2021a). Still, they focus on complementary NLP tasks to the two previous initiatives. It is thus an open issue to see whether tasks might need to have specific properties to be suitable for one kind of method over another. A comprehensive evaluation is lacking. Studying transferability of methods across problems is another interesting open issue.

**ZH** 研究如何借助人类标注变异进行学习的兴趣无疑在增长（我们对研究论文的统计见图 3）。然而现有研究在各个（子）学科间呈碎片化。我们识别出 NLP 内部至少三个几乎毫无交集的领域（如附录表 1 所示），分别聚焦于：主观性 Basile 等（2021a）（pdai.info、SemEval 23）、自然语言推理（NLI）Pavlick 与 Kwiatkowski（2019）；Nie 等（2020），以及同时覆盖 NLP 与 CV 的工作（JAIR 与 SemEval 21）。据我们所知，迄今只有后者及其共享任务跨越了学科边界 Uma 等（2021b）；Uma 等（2021a），而且它们关注的 NLP 任务又与前两项工作互补。因此，任务是否需要具备特定性质才更适合某一类方法，仍是一个开放问题；目前尚缺乏全面的评测。考察方法在各类问题间的可迁移性，是另一个值得关注的开放问题。

**EN** Learning from Hlv heavily depends on data labeled with multiple annotators. In some settings, it might be difficult to obtain sizeable amounts of such data (however, as seen in Section 2, more datasets are emerging). Regarding learning, Lalor et al. (2017) find that even small amounts of data can be helpful in a sequential fine-tuning setup, as also early work indicates Plank et al. (2014a). An open challenge is to find the right balance between the amount of data collected and the number of annotators. Overall, we hypothesize that the richness of information captured by human label variation has the potential to reduce data size requirements (possibly fewer instances but with more information captured in the human label distribution). It remains an open issue to connect with emerging works on learning with different amounts of annotation Zhang et al. (2021), which can also lead to novel architectures.

**ZH** 从 HLV 学习高度依赖带有多个标注者标注的数据。在某些场景下，获取足量此类数据可能并不容易（不过如第 2 节所示，越来越多的数据集正在出现）。在学习方面，Lalor 等（2017）发现，在序贯微调的设置下即便少量数据也能发挥作用，早期工作亦有同样指示 Plank 等（2014a）。一个开放性挑战是，在收集的数据量与标注者人数之间找到恰当的平衡。总体上我们假设，HLV 所捕获信息的丰富性有潜力降低对数据规模的要求——实例可以更少，但人类标签分布中蕴含的信息更多。如何与新兴的、关于不同标注量下学习的工作建立联系 Zhang 等（2021），仍是开放问题，这也可能催生新的架构。

**EN** A related important challenge is to tease apart errors from signal (Reidsma and Carletta, 2008; Gordon et al., 2021, e.g.). Work on annotation error detection exists, cf. the very recent survey by Klie et al. (2022) or Zhang and de Marneffe (2021). It is though largely overlooked. This calls further for theoretical work on the notion of an what constitutes an error versus a hard case Manning (2011); Webber and Joshi (2012); Plank et al. (2014b). This bears connections to emerging work in HCI, in particular social computing Gordon et al. (2021); Gordon et al. (2022), who look at the perception of system errors by humans, see also Section 4, and earlier work in HCI on crowdsourcing that allows for some errors Krishna et al. (2016).

**ZH** 一个相关的重要挑战是把错误与信号区分开来（例如 Reidsma 与 Carletta，2008；Gordon 等，2021）。标注错误检测方面已有工作，参见 Klie 等（2022）最新的综述或 Zhang 与 de Marneffe（2021），但这些工作在很大程度上被忽视。这进一步呼唤关于“什么构成错误、什么构成困难样例”的理论研究 Manning（2011）；Webber 与 Joshi（2012）；Plank 等（2014b）。这一点与 HCI 尤其是社会计算（social computing）中的新兴工作相呼应 Gordon 等（2021）；Gordon 等（2022），后者考察人类如何感知系统错误，另见第 4 节；也与 HCI 中更早期关于容忍一定错误的众包工作相关 Krishna 等（2016）。

**EN** While embracing human label variation helps to regularize learning, the connection to a broader range of ML methods such as noise labeling or calibration remains highly relevant and a source of further inspiration Goldberger and Ben-Reuven (2016); Han et al. (2018b); Han et al. (2018a); Meister et al. (2020). There are some initial studies that compare human disagreement with model confidence Davani et al. (2022). Overall, interest in calibration methods Naeini et al. (2015); Guo et al. (2017) is increasing Desai and Durrett (2020); Kong et al. (2020); Jiang et al. (2021) to counter overconfidence of neural classifiers Meister et al. (2020). In contemporary work to this, we show that measuring calibration to human majority given inherent disagreements is theoretically and empirically problematic Baan et al. (2022). As a first step, we propose instance-level measures of calibration that better capture the human label distribution. In future, it remains to be seen how to best use human label variation to make systems more trustworthy.

**ZH** 接纳人类标注变异虽有助于正则化学习，但与噪声标注、校准等更广泛的 ML 方法之间的联系依然紧密，也是进一步汲取灵感的来源 Goldberger 与 Ben-Reuven（2016）；Han 等（2018b）；Han 等（2018a）；Meister 等（2020）。已有若干初步研究将人类分歧与模型置信度加以比较 Davani 等（2022）。总体上，学界的兴趣正转向校准方法 Naeini 等（2015）；Guo 等（2017），以对抗神经分类器的过度自信 Meister 等（2020），相关研究不断增多 Desai 与 Durrett（2020）；Kong 等（2020）；Jiang 等（2021）。在与本文同期的一项工作中，我们表明：在存在固有分歧时，以人类多数为参照衡量校正在理论与经验两方面都存在问题 Baan 等（2022）。作为第一步，我们提出了实例级的校准度量，以更好地刻画人类标签分布。未来如何最好地利用人类标注变异来提升系统的可信度，仍有待观察。

**EN** Finally, there is relevant interesting work that more deeply looks at data during learning. In NLP, recent seminal work by Swayamdipta et al. (2020) proposes data maps to investigate the behavior of a model on individual instances during training (training dynamics). They show that training a system on ambiguous instances identified via data maps helps to generalizes better in out-of-distribution evaluation Swayamdipta et al. (2020). Building on top of this work, Zhang and Plank (2021) show that the instances at the boundary of hard and ambiguous cases derived from small data maps aids active learning. This is further evidence that human uncertainty in labeling is beneficial for learning. It remains to be seen whether training dynamics can yield novel architectures for learning from Hlv.

**ZH** 最后，还有一些值得关注的工作更深入地考察了学习过程中的数据。在 NLP 中，Swayamdipta 等（2020）的开创性工作提出用数据地图（data maps）考察模型在训练期间对单个实例的行为，即训练动态。他们表明，在数据地图所识别的歧义实例上训练系统，有助于在分布外评测中获得更好的泛化 Swayamdipta 等（2020）。在此基础上，Zhang 与 Plank（2021）表明，由小规模数据地图导出的、处于困难与歧义边界上的实例有助于主动学习。这进一步证明，标注中的人类不确定性对学习有益。训练动态能否催生出面向 HLV 学习的新型架构，仍有待观察。

**EN** 4 Evaluation and Human Label Variation

**ZH** 4 评测与人类标注变异

**EN** Evaluation is of critical importance in empirical research fields such as ML, NLP and CV. It helps to choose one system over another, and to measure progress. However, current evaluation practices typically use accuracy against a gold standard. In many tasks this common practice is severely flawed. It obfuscates the truth about the state of ML models. It leaves a large gap between in-vitro and in-vivo evaluation. HCI research has shown that metrics are not aligned with reality; audits of algorithms’ performance have uncovered very poor results in practice, and that this disconnect is indicative of a larger disconnect on how ML and HCI researchers evaluate their work Gordon et al. (2021). We believe this is an important take-away for NLP. We too often focus on single metrics, single components of the pipeline, in other words, on myopic in-vitro experimentation.

**ZH** 在 ML、NLP 与 CV 这类实证研究领域中，评测至关重要：它帮助我们在系统之间做出取舍，也衡量着进展。然而，当前的评测实践通常是以准确率为指标、与金标准对照。在许多任务中，这一通行做法存在严重缺陷。它模糊了 ML 模型的真实状况，并在实验室评测（in-vitro）与真实环境评测（in-vivo）之间留下巨大鸿沟。HCI 研究表明，各类指标与现实并不吻合；对算法表现的审计发现，实践中的结果相当糟糕，而这种脱节折射出 ML 与 HCI 研究者在如何评价自身工作这一更大层面上的割裂 Gordon 等（2021）。我们认为这是 NLP 应当重视的一条经验：我们过于频繁地只盯着单一指标、只盯着流程中的单个部件，换言之，沉迷于目光短浅的实验室评测。

**EN** Open issues and our suggestions

**ZH** 开放问题与我们的建议

**EN** Despite the increasing body of literature on methods for learning with Hlv, a majority of the papers introducing new methods strikingly evaluate against hard labels (gold labels) (Rodrigues and Pereira, 2018; Fornaciari et al., 2021, e.g.). If we want to take human label variation seriously, we need to shift our attention to evaluation that goes beyond hard labels (accuracy). As accuracy of all models can be high (at times), looking at only one metric (and, in fact a single—argmax—prediction) gives no indication on how reasonable a model is, yet alone how confident and trustworthy it is.

**ZH** 尽管关于借助 HLV 学习的方法的文献不断增加，引人注目的是，提出新方法的大多数论文仍以硬标签（金标签）为评测对象（例如 Rodrigues 与 Pereira，2018；Fornaciari 等，2021）。若真要认真对待人类标注变异，我们就必须把注意力转向超越硬标签（准确率）的评测。既然所有模型的准确率都可能相当高，只考察单一指标、乃至只考察单次 argmax 预测，就无法说明模型有多合理，更遑论其置信度与可信度如何。

**EN** Research in ML, CV and NLP has started to incentivize hard and soft label evaluation. Soft labels compare the human label distribution to model outputs. Proposed soft metrics include: cross entropy, to capture how well the model captures humans’ assessment not just of the top label, which is used in both CV Peterson et al. (2019) and NLP Pavlick and Kwiatkowski (2019); entropy correlation proposed by Uma et al. (2020), to compute Pearson’s correlation between instance-level entropy scores of human soft labels and model predictions; Kullback-Leibler divergence-based evaluation Nie et al. (2020) (either KL or Jensen-Shannon). Others instead started to evaluate against individual annotators Resnick et al. (2021); Davani et al. (2022), measure F1 scores against data splits by different annotator agreement levels Leonardelli et al. (2021); Damgaard et al. (2021), data splits based on annotator clustering Basile et al. (2021a), data splits based on item difficulty based on entropy of the label distribution and semantic distance Jolly et al. (2021), and data splits based on annotator uncertainty flags Bassignana and Plank (2022). Analogously as in Section 3, it is an open issue to see whether tasks might need to have specific properties to be more suitable for one kind of evaluation over another. In general, we need better evaluation practices (besides soft and hard evaluation), particularly in light of the complexity of human label variation—and the reasons it arises, which might be due to uncertainty, background, task complexity, intra-coder reliability etc; see Basile et al. (2021b) and in particular Jiang and de Marneffe (2022) for a discussion on disagreement sources; the latter recently developed a taxonomy for disagreement in natural language inference data.

**ZH** ML、CV 与 NLP 的研究已开始推动硬标签与软标签评测。软标签评测将人类标签分布与模型输出加以比较。已提出的软指标包括：交叉熵，用以衡量模型在多大程度上捕捉了人类对非最高标签的判断，CV Peterson 等（2019）与 NLP Pavlick 与 Kwiatkowski（2019）均有使用；熵相关性，由 Uma 等（2020）提出，计算人类软标签与模型预测的逐实例熵之间的 Pearson 相关系数；基于 Kullback-Leibler 散度的评测 Nie 等（2020）（KL 或 Jensen-Shannon 散度）。另一些工作则改为针对单个标注者评测 Resnick 等（2021）；Davani 等（2022），按标注者一致程度划分数据子集后计算 F1 值 Leonardelli 等（2021）；Damgaard 等（2021），按标注者聚类划分子集 Basile 等（2021a），按项目难度（依据标签分布熵与语义距离）划分子集 Jolly 等（2021），以及按标注者不确定性标记划分子集 Bassignana 与 Plank（2022）。与第 3 节类似，任务是否需要具备特定性质才更适合某一类评测，仍是开放问题。总体而言，我们需要更好的评测实践（不止于软评测与硬评测），尤其要考虑到人类标注变异的复杂性及其成因——不确定性、背景、任务复杂度、标注者自身一致性等；相关讨论见 Basile 等（2021b），特别是 Jiang 与 de Marneffe（2022）对分歧来源的探讨，后者最近还为自然语言推理数据中的分歧建立了一套分类体系。

**EN** 5 Conclusions

**ZH** 5 结论

**EN** In this paper, we outline that human label variation impacts all steps of the traditional ML pipeline, and is an opportunity, not a problem. To move forward, we argue for a more comprehensive treatment of Hlv, which considers all steps, to enable innovation: data, modeling and evaluation. To do so, and truly move beyond the current in-vitro setups, we need an open, inter-disciplinary discussion. We hope to contribute to this discussion, and stipulate research with the released repository: https://github.com/mainlp/awesome-human-label-variation.11 1 The repository contains the datasets in Appendix 1 as a starting point. This is, to the best of our knowledge, the most comprehensive list of datasets with un-aggregated labels available today. We encourage readers to contribute. They are further invited to join the SemEval 2023 shared task LeWiDi: https://le-wi-di.github.io/

**ZH** 本文阐明，人类标注变异影响传统 ML 流程的每一个环节，它是一次机遇而非问题。为了向前推进，我们主张对 HLV 采取更全面的处理方式，将数据、建模与评测各个环节一并纳入，以此促成创新。要真正做到这一点、真正超越当下的实验室设置，我们需要一场开放的跨学科讨论。我们希望为这场讨论贡献一份力量，并通过发布的仓库推动相关研究：https://github.com/mainlp/awesome-human-label-variation。11 1 该仓库以附录 1 中的数据集为起点。据我们所知，这是目前可得的、最全面的未聚合标签数据集清单。我们欢迎读者贡献，也邀请大家参加 SemEval 2023 共享任务 LeWiDi：https://le-wi-di.github.io/。

**EN** Limitations

**ZH** 局限性

**EN** This position paper tries to be succinct while aiming at synthesizing a very broad notion—human label variation—that affects all steps dealing with learning from annotated data. Therefore, this position paper is necessarily incomplete, as is the dataset repository that is provided. However, we hope that the repository and paper will lead to an open discussion and community uptake, as this is a big open issue and necessitates a broader, inter-disciplinary treatment.

**ZH** 这篇立场论文力求简洁，同时尝试综合“人类标注变异”这一极为宽泛的概念——它影响着从标注数据中学习的每一个环节。因此，本文必然是不完备的，所提供的数据集仓库同样如此。然而我们希望，这份仓库与这篇论文能引发开放的讨论并获得学界的采纳，因为这是一个重大的开放议题，需要更广泛的跨学科探讨。

**EN** Ethics Statement

**ZH** 伦理声明

**EN** Modeling human label variation is connected to social bias, as annotator backgrounds influence annotations and consequently both machine learning and evaluation. Therefore it is important to be aware of possible social implications of some of the technologies discussed here. Inevitably there is potential for dual use, as amplifying the voice of some might harm others. However, there are social opportunities, as modeling human label variation allows to include the voices of more groups, and even the very underrepresented. In a world where the majority view dominates, these would otherwise be left behind.

**ZH** 对人类标注变异建模与社会偏见相关，因为标注者的背景会影响标注，进而同时影响机器学习与评测。因此，有必要意识到本文所讨论的某些技术可能带来的社会影响。双重用途的风险不可避免：放大某些群体的声音，可能损害另一些群体。但同样存在社会层面的机遇——对人类标注变异建模让我们能够纳入更多群体、乃至极弱势群体的声音。在一个多数意见占据主导的世界里，这些声音本会被抛在后面。

**EN** Acknowledgements

**ZH** 致谢

**EN** We thank the reviewers for their feedback. Special thanks to Bonnie Webber, Massimo Poesio and Raffaella Bernardi for invaluable feedback on drafts of this paper and discussions on this topic, in parts at the Insights workshop@ACL 2022. Thanks to members of the NLPnorth & MaiNLP lab for feedback on this paper. BP is supported by ERC Consolidator Grant DIALECT 101043235.

**ZH** 我们感谢评审者的反馈。特别感谢 Bonnie Webber、Massimo Poesio 与 Raffaella Bernardi 就本文草稿提出的宝贵意见，以及围绕该主题的讨论，其中部分讨论发生在 ACL 2022 的 Insights 研讨会上。感谢 NLPnorth 与 MaiNLP 实验室成员对本文的反馈。BP 受 ERC Consolidator Grant DIALECT 101043235 资助。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] Akhtar et al. (2021) Sohail Akhtar, Valerio Basile, and Viviana Patti. 2021. Whose opinions matter? Perspective-aware models to identify opinions of hate speech victims in abusive language detection.  -->

<!-- [原子块 · verbatim] Alm (2011) Cecilia Ovesdotter Alm. 2011. Subjective natural language problems: Motivations, applications, characterizations, and implications. In Proceedings of the 49th Annual Meeting of the Associat -->

<!-- [原子块 · verbatim] Almanea and Poesio (2022) Dina Almanea and Massimo Poesio. 2022. The ARMIS dataset of misogyny in arabic tweets. In Proc. of LREC . -->

<!-- [原子块 · verbatim] Aroyo and Welty (2015) Lora Aroyo and Chris Welty. 2015. Truth is a lie: Crowd truth and the seven myths of human annotation. AI Magazine , 36(1):15–24. -->

<!-- [原子块 · verbatim] Artstein and Poesio (2008) Ron Artstein and Massimo Poesio. 2008. Inter-coder agreement for computational linguistics. Computational linguistics , 34(4):555–596. -->

<!-- [原子块 · verbatim] Baan et al. (2022) Joris Baan, Wilker Aziz, Barbara Plank, and Raquel Fernandez. 2022. Stop measuring calibration when humans disagree. In Empirical Methods of Natural Language Processing: EMNLP 2022  -->

<!-- [原子块 · verbatim] Basile et al. (2021a) Valerio Basile, Federico Cabitza, Andrea Campagner, and Michael Fell. 2021a. Toward a perspectivist turn in ground truthing for predictive computing. arXiv preprint arXiv:2109.04 -->

<!-- [原子块 · verbatim] Basile et al. (2021b) Valerio Basile, Michael Fell, Tommaso Fornaciari, Dirk Hovy, Silviu Paun, Barbara Plank, Massimo Poesio, Alexandra Uma, et al. 2021b. We need to consider disagreement in evaluati -->

<!-- [原子块 · verbatim] Bassignana and Plank (2022) Elisa Bassignana and Barbara Plank. 2022. CrossRE: A Cross-Domain Dataset for Relation Extraction. In Findings of the Association for Computational Linguistics: EMNLP 2022  -->

<!-- [原子块 · verbatim] Beigman and Beigman-Klebanov (2009) Eyal Beigman and Beata Beigman-Klebanov. 2009. Learning with annotation noise . In Proceedings of the Joint Conference of the 47th Annual Meeting of the ACL and the -->

<!-- [原子块 · verbatim] Beigman Klebanov et al. (2008) Beata Beigman Klebanov, Eyal Beigman, and Danie Diermaier. 2008. Analyzing disagreements. In Proceedings of the Coling 2008 workshop on Human Judgements in Computational -->

<!-- [原子块 · verbatim] Bender and Friedman (2018) Emily M Bender and Batya Friedman. 2018. Data statements for natural language processing: Toward mitigating system bias and enabling better science. Transactions of the Asso -->

<!-- [原子块 · verbatim] Berzak et al. (2016) Yevgeni Berzak, Yan Huang, Andrei Barbu, Anna Korhonen, and Boris Katz. 2016. Anchoring and agreement in syntactic annotations . In Proceedings of the 2016 Conference on Empirical -->

<!-- [原子块 · verbatim] Borin (2022) Lars Borin. 2022. All that glitters… interannotator agreement in natural language processing. Morfologi, målstrev og maskinar – Trond Trosterud 60 , 46(1). -->

<!-- [原子块 · verbatim] Bryant and Ng (2015) Christopher Bryant and Hwee Tou Ng. 2015. How far are we from fully automatic high quality grammatical error correction? In Proceedings of the 53rd Annual Meeting of the Associati -->

<!-- [原子块 · verbatim] Cercas Curry et al. (2021) Amanda Cercas Curry, Gavin Abercrombie, and Verena Rieser. 2021. ConvAbuse: Data, analysis, and benchmarks for nuanced abuse detection in conversational AI . In Proceedings  -->

<!-- [原子块 · verbatim] Cheplygina and Pluim (2018) Veronika Cheplygina and Josien PW Pluim. 2018. Crowd disagreement about medical images is informative. In Intravascular imaging and computer assisted stenting and large-sca -->

<!-- [原子块 · verbatim] Cohn and Specia (2013) Trevor Cohn and Lucia Specia. 2013. Modelling annotator bias with multi-task Gaussian processes: An application to machine translation quality estimation . In Proceedings of the -->

<!-- [原子块 · verbatim] Dagan et al. (2005) Ido Dagan, Oren Glickman, and Bernardo Magnini. 2005. The pascal recognising textual entailment challenge. In Machine learning challenges workshop , pages 177–190. Springer. -->

<!-- [原子块 · verbatim] Damgaard et al. (2021) Cathrine Damgaard, Paulina Toborek, Trine Eriksen, and Barbara Plank. 2021. “I’ll be there for you”: The one with understanding indirect answers . In Proceedings of the 2nd Work -->

<!-- [原子块 · verbatim] Das et al. (2017) Debopam Das, Manfred Stede, and Maite Taboada. 2017. The good, the bad, and the disagreement: Complex ground truth in rhetorical structure analysis . In Proceedings of the 6th Worksh -->

<!-- [原子块 · verbatim] Davani et al. (2022) Aida Mostafazadeh Davani, Mark Díaz, and Vinodkumar Prabhakaran. 2022. Dealing with disagreements: Looking beyond the majority vote in subjective annotations. Transactions of the  -->

<!-- [原子块 · verbatim] Dawid and Skene (1979) Alexander Philip Dawid and Allan M Skene. 1979. Maximum likelihood estimation of observer error-rates using the em algorithm. Journal of the Royal Statistical Society: Series C  -->

<!-- [原子块 · verbatim] de Marneffe et al. (2012) Marie-Catherine de Marneffe, Christopher D. Manning, and Christopher Potts. 2012. Did it happen? the pragmatic complexity of veridicality assessment . Computational Linguisti -->

<!-- [原子块 · verbatim] de Marneffe et al. (2019) Marie-Catherine de Marneffe, Mandy Simons, and Judith Tonhauser. 2019. The commitmentbank: Investigating projection in naturally occurring discourse. In proceedings of Sinn u -->

<!-- [原子块 · verbatim] Demszky et al. (2020) Dorottya Demszky, Dana Movshovitz-Attias, Jeongwoo Ko, Alan Cowen, Gaurav Nemade, and Sujith Ravi. 2020. GoEmotions: A dataset of fine-grained emotions . In Proceedings of the 58 -->

<!-- [原子块 · verbatim] Denton et al. (2021) Emily Denton, Mark Díaz, Ian Kivlichan, Vinodkumar Prabhakaran, and Rachel Rosen. 2021. Whose ground truth? accounting for individual and collective identities underlying dataset  -->

<!-- [原子块 · verbatim] Derczynski et al. (2016) Leon Derczynski, Kalina Bontcheva, and Ian Roberts. 2016. Broad Twitter corpus: A diverse named entity recognition resource . In Proceedings of COLING 2016, the 26th Internati -->

<!-- [原子块 · verbatim] Desai and Durrett (2020) Shrey Desai and Greg Durrett. 2020. Calibration of pre-trained transformers . In Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP) -->

<!-- [原子块 · verbatim] Dinu et al. (2021) Liviu P. Dinu, Ioan-Bogdan Iordache, Ana Sabina Uban, and Marcos Zampieri. 2021. A computational exploration of pejorative language in social media . In Findings of the Association  -->

<!-- [原子块 · verbatim] Dumitrache et al. (2018) Anca Dumitrache, Lora Aroyo, and Chris Welty. 2018. Crowdsourcing semantic label propagation in relation classification . In Proceedings of the First Workshop on Fact Extracti -->

<!-- [原子块 · verbatim] Dumitrache et al. (2019) Anca Dumitrache, Lora Aroyo, and Chris Welty. 2019. A crowdsourced frame disambiguation corpus with ambiguity. In Annual Conference of the North American Chapter of the Associ -->

<!-- [原子块 · verbatim] Ferracane et al. (2021) Elisa Ferracane, Greg Durrett, Junyi Jessy Li, and Katrin Erk. 2021. Did they answer? subjective acts and intents in conversational discourse . In Proceedings of the 2021 Confe -->

<!-- [原子块 · verbatim] Fornaciari et al. (2021) Tommaso Fornaciari, Alexandra Uma, Silviu Paun, Barbara Plank, Dirk Hovy, and Massimo Poesio. 2021. Beyond black & white: Leveraging annotator disagreement via soft-label mult -->

<!-- [原子块 · verbatim] Geiger et al. (2020) R Stuart Geiger, Kevin Yu, Yanlai Yang, Mindy Dai, Jie Qiu, Rebekah Tang, and Jenny Huang. 2020. Garbage in, garbage out? do machine learning application papers in social computin -->

<!-- [原子块 · verbatim] Goldberger and Ben-Reuven (2016) Jacob Goldberger and Ehud Ben-Reuven. 2016. Training deep neural-networks using a noise adaptation layer. ICLR 2017 . -->

<!-- [原子块 · verbatim] Gordon et al. (2022) Mitchell L Gordon, Michelle S Lam, Joon Sung Park, Kayur Patel, Jeff Hancock, Tatsunori Hashimoto, and Michael S Bernstein. 2022. Jury learning: Integrating dissenting voices into -->

<!-- [原子块 · verbatim] Gordon et al. (2021) Mitchell L Gordon, Kaitlyn Zhou, Kayur Patel, Tatsunori Hashimoto, and Michael S Bernstein. 2021. The disagreement deconvolution: Bringing machine learning performance metrics in  -->

<!-- [原子块 · verbatim] Guo et al. (2017) Chuan Guo, Geoff Pleiss, Yu Sun, and Kilian Q. Weinberger. 2017. On calibration of modern neural networks. In Proceedings of the 34th International Conference on Machine Learning - V -->

<!-- [原子块 · verbatim] Han et al. (2018a) Bo Han, Jiangchao Yao, Gang Niu, Mingyuan Zhou, Ivor Tsang, Ya Zhang, and Masashi Sugiyama. 2018a. Masking: A new perspective of noisy supervision. In Advances in Neural Information -->

<!-- [原子块 · verbatim] Han et al. (2018b) Bo Han, Quanming Yao, Xingrui Yu, Gang Niu, Miao Xu, Weihua Hu, Ivor Tsang, and Masashi Sugiyama. 2018b. Co-teaching: Robust training of deep neural networks with extremely noisy la -->

<!-- [原子块 · verbatim] Hershcovich et al. (2022) Daniel Hershcovich, Stella Frank, Heather Lent, Miryam de Lhoneux, Mostafa Abdou, Stephanie Brandl, Emanuele Bugliarello, Laura Cabello Piqueras, Ilias Chalkidis, Ruixiang Cu -->

<!-- [原子块 · verbatim] Jamison and Gurevych (2015) Emily Jamison and Iryna Gurevych. 2015. Noise or additional information? leveraging crowdsource annotation item agreement for natural language tasks. In Proceedings of the  -->

<!-- [原子块 · verbatim] Jiang and de Marneffe (2022) Nan-Jiang Jiang and Marie-Catherine de Marneffe. 2022. Investigating reasons for disagreement in natural language inference. Transactions of the Association for Computatio -->

<!-- [原子块 · verbatim] Jiang et al. (2021) Zhengbao Jiang, Jun Araki, Haibo Ding, and Graham Neubig. 2021. How Can We Know When Language Models Know? On the Calibration of Language Models for Question Answering . Transactio -->

<!-- [原子块 · verbatim] Jolly et al. (2021) Shailza Jolly, Sandro Pezzelle, and Moin Nabi. 2021. EaSe: A diagnostic tool for VQA based on answer diversity . In Proceedings of the 2021 Conference of the North American Chapter -->

<!-- [原子块 · verbatim] Kennedy et al. (2020) Chris J Kennedy, Geoff Bacon, Alexander Sahn, and Claudia von Vacano. 2020. Constructing interval variables via faceted rasch measurement and multitask deep learning: a hate spee -->

<!-- [原子块 · verbatim] Klie et al. (2022) Jan-Christoph Klie, Bonnie Webber, and Iryna Gurevych. 2022. Annotation error detection: Analyzing the past and present for a more coherent future. Computational Linguistics . -->

<!-- [原子块 · verbatim] Kong et al. (2020) Lingkai Kong, Haoming Jiang, Yuchen Zhuang, Jie Lyu, Tuo Zhao, and Chao Zhang. 2020. Calibrated language model fine-tuning for in- and out-of-distribution data . In Proceedings of t -->

<!-- [原子块 · verbatim] Krippendorff (2018) Klaus Krippendorff. 2018. Content analysis: An introduction to its methodology . Sage publications. -->

<!-- [原子块 · verbatim] Krishna et al. (2016) Ranjay A Krishna, Kenji Hata, Stephanie Chen, Joshua Kravitz, David A Shamma, Li Fei-Fei, and Michael S Bernstein. 2016. Embracing error to enable rapid crowdsourcing. In Proceed -->

<!-- [原子块 · verbatim] Lalor et al. (2017) John P Lalor, Hao Wu, and Hong Yu. 2017. Soft label memorization-generalization for natural language inference. arXiv preprint arXiv:1702.08563 . -->

<!-- [原子块 · verbatim] Larimore et al. (2021) Savannah Larimore, Ian Kennedy, Breon Haskett, and Alina Arseniev-Koehler. 2021. Reconsidering annotator disagreement about racist language: Noise or signal? In Proceedings of t -->

<!-- [原子块 · verbatim] Leonardelli et al. (2021) Elisa Leonardelli, Stefano Menini, Alessio Palmero Aprosio, Marco Guerini, and Sara Tonelli. 2021. Agreeing to disagree: Annotating offensive language datasets with annotator -->

<!-- [原子块 · verbatim] Liu et al. (2016) Tong Liu, Christopher Homan, Cecilia Ovesdotter Alm, Megan Lytle, Ann Marie White, and Henry Kautz. 2016. Understanding discourse on work and job-related well-being in public social  -->

<!-- [原子块 · verbatim] Manning (2011) Christopher D Manning. 2011. Part-of-speech tagging from 97% to 100%: is it time for some linguistics? In International conference on intelligent text processing and computational lingu -->

<!-- [原子块 · verbatim] Marchal et al. (2022) Marian Marchal, Merel Scholman, Frances Yung, and Vera Demberg. 2022. Establishing annotation quality in multi-label annotations . In Proceedings of the 29th International Confer -->

<!-- [原子块 · verbatim] Martínez Alonso et al. (2016) Héctor Martínez Alonso, Anders Johannsen, and Barbara Plank. 2016. Supersense tagging with inter-annotator disagreement . In Proceedings of the 10th Linguistic Annotation -->

<!-- [原子块 · verbatim] McDonnell et al. (2016) Tyler McDonnell, Matthew Lease, Mucahid Kutlu, and Tamer Elsayed. 2016. Why is that relevant? collecting annotator rationales for relevance judgments. In Proceedings of the AAA -->

<!-- [原子块 · verbatim] Meister et al. (2020) Clara Meister, Elizabeth Salesky, and Ryan Cotterell. 2020. Generalized entropy regularization or: There’s nothing special about label smoothing. arXiv preprint arXiv:2005.00820  -->

<!-- [原子块 · verbatim] Naeini et al. (2015) Mahdi Pakdaman Naeini, Gregory F. Cooper, and Milos Hauskrecht. 2015. Obtaining Well Calibrated Probabilities Using Bayesian Binning. In Proceedings of the Twenty-Ninth AAAI Confe -->

<!-- [原子块 · verbatim] Nie et al. (2020) Yixin Nie, Xiang Zhou, and Mohit Bansal. 2020. What can we learn from collective human opinions on natural language inference data? In Proceedings of the 2020 Conference on Empirical -->

<!-- [原子块 · verbatim] Palomaki et al. (2018) Jennimaria Palomaki, Olivia Rhinehart, and Michael Tseng. 2018. A case for a range of acceptable annotations. In SAD/CrowdBias@ HCOMP , pages 19–31. -->

<!-- [原子块 · verbatim] Passonneau et al. (2010) Rebecca J Passonneau, Ansaf Salleb-Aouissi, Vikas Bhardwaj, and Nancy Ide. 2010. Word sense annotation of polysemous words by multiple annotators. In Proceedings of the Sevent -->

<!-- [原子块 · verbatim] Paun et al. (2022) Silviu Paun, Ron Artstein, and Massimo Poesio. 2022. Statistical methods for annotation analysis. Synthesis Lectures on Human Language Technologies , 15(1):1–217. -->

<!-- [原子块 · verbatim] Pavlick and Kwiatkowski (2019) Ellie Pavlick and Tom Kwiatkowski. 2019. Inherent disagreements in human textual inferences . Transactions of the Association for Computational Linguistics , 7:677–694. -->

<!-- [原子块 · verbatim] Peng et al. (2022) Siyao Peng, Yang Janet Liu, and Amir Zeldes. 2022. Gcdt: A chinese rst treebank for multigenre and multilingual discourse parsing. In Proceedings of the 2nd Conference of the Asia-P -->

<!-- [原子块 · verbatim] Peterson et al. (2019) Joshua C. Peterson, Ruairidh M. Battleday, Thomas L. Griffiths, and Olga Russakovsky. 2019. Human uncertainty makes classification more robust. 2019 IEEE/CVF International Confe -->

<!-- [原子块 · verbatim] Plank et al. (2014a) Barbara Plank, Dirk Hovy, and Anders Søgaard. 2014a. Learning part-of-speech taggers with inter-annotator agreement loss . In Proceedings of the 14th Conference of the European Ch -->

<!-- [原子块 · verbatim] Plank et al. (2014b) Barbara Plank, Dirk Hovy, and Anders Søgaard. 2014b. Linguistically debatable or just plain wrong? In Proceedings of the 52nd Annual Meeting of the Association for Computational L -->

<!-- [原子块 · verbatim] Poesio and Artstein (2005) Massimo Poesio and Ron Artstein. 2005. The reliability of anaphoric annotation, reconsidered: Taking ambiguity into account . In Proc. of ACL Workshop on Frontiers in Corpus -->

<!-- [原子块 · verbatim] Poesio et al. (2019) Massimo Poesio, Jon Chamberlain, Silviu Paun, Juntao Yu, Alexandra Uma, and Udo Kruschwitz. 2019. A crowdsourced corpus of multiple judgments and disagreement on anaphoric interpr -->

<!-- [原子块 · verbatim] Prabhakaran et al. (2021) Vinodkumar Prabhakaran, Aida Mostafazadeh Davani, and Mark Diaz. 2021. On releasing annotator-level labels and information in datasets . In Proceedings of The Joint 15th Ling -->

<!-- [原子块 · verbatim] Pustejovsky and Stubbs (2012) James Pustejovsky and Amber Stubbs. 2012. Natural Language Annotation for Machine Learning: A guide to corpus-building for applications . O’Reilly Media. -->

<!-- [原子块 · verbatim] Qing et al. (2014) Ciyang Qing, Ulle Endriss, Raquel Fernández, and Justin Kruger. 2014. Empirical analysis of aggregation methods for collective annotation. In COLING . -->

<!-- [原子块 · verbatim] Reidsma and Carletta (2008) Dennis Reidsma and Jean Carletta. 2008. Reliability measurement without limits. Computational Linguistics , 34(3):319–326. -->

<!-- [原子块 · verbatim] Reidsma and op den Akker (2008) Dennis Reidsma and Rieks op den Akker. 2008. Exploiting ‘subjective’ annotations . In Proc. of the Workshop on Human Judgments in Computational Linguistics , pages 8–16 -->

<!-- [原子块 · verbatim] Resnick et al. (2021) Paul Resnick, Yuqing Kong, Grant Schoenebeck, and Tim Weninger. 2021. Survey equivalence: A procedure for measuring classifier accuracy against human labels. arXiv preprint arXiv -->

<!-- [原子块 · verbatim] Rodrigues and Pereira (2018) Filipe Rodrigues and Francisco Pereira. 2018. Deep learning from crowds. In Proceedings of the AAAI conference on artificial intelligence , volume 32. -->

<!-- [原子块 · verbatim] Rottger et al. (2022) Paul Rottger, Bertie Vidgen, Dirk Hovy, and Janet Pierrehumbert. 2022. Two contrasting data annotation paradigms for subjective NLP tasks . In Proceedings of the 2022 Conference  -->

<!-- [原子块 · verbatim] Sap et al. (2019) Maarten Sap, Dallas Card, Saadia Gabriel, Yejin Choi, and Noah A. Smith. 2019. The risk of racial bias in hate speech detection . In Proceedings of the 57th Annual Meeting of the Ass -->

<!-- [原子块 · verbatim] Sap et al. (2022) Maarten Sap, Swabha Swayamdipta, Laura Vianna, Xuhui Zhou, Yejin Choi, and Noah A. Smith. 2022. Annotators with attitudes: How annotator beliefs and identities bias toxic language de -->

<!-- [原子块 · verbatim] Schlangen (2021) David Schlangen. 2021. Targeting the benchmark: On methodology in current natural language processing research . In Proceedings of the 59th Annual Meeting of the Association for Compu -->

<!-- [原子块 · verbatim] Sheng et al. (2008) Victor S. Sheng, Foster Provost, and Panagiotis G. Ipeirotis. 2008. Get another label? improving data quality and data mining using multiple, noisy labelers . In Proceedings of the -->

<!-- [原子块 · verbatim] Simpson et al. (2019) Edwin Simpson, Erik-Lân Do Dinh, Tristan Miller, and Iryna Gurevych. 2019. Predicting humorousness and metaphor novelty with Gaussian process preference learning . In Proceedings -->

<!-- [原子块 · verbatim] Snow et al. (2008) Rion Snow, Brendan O’connor, Dan Jurafsky, and Andrew Y Ng. 2008. Cheap and fast–but is it good? evaluating non-expert annotations for natural language tasks. In Proceedings of the  -->

<!-- [原子块 · verbatim] Sommerauer et al. (2020) Pia Sommerauer, Antske Fokkens, and Piek Vossen. 2020. Would you describe a leopard as yellow? evaluating crowd-annotations with justified and informative disagreement . In Pr -->

<!-- [原子块 · verbatim] Swayamdipta et al. (2020) Swabha Swayamdipta, Roy Schwartz, Nicholas Lourie, Yizhong Wang, Hannaneh Hajishirzi, Noah A. Smith, and Yejin Choi. 2020. Dataset cartography: Mapping and diagnosing dataset -->

<!-- [原子块 · verbatim] Uma et al. (2021a) Alexandra Uma, Tommaso Fornaciari, Anca Dumitrache, Tristan Miller, Jon Chamberlain, Barbara Plank, Edwin Simpson, and Massimo Poesio. 2021a. SemEval-2021 task 12: Learning with dis -->

<!-- [原子块 · verbatim] Uma et al. (2020) Alexandra Uma, Tommaso Fornaciari, Dirk Hovy, Silviu Paun, Barbara Plank, and Massimo Poesio. 2020. A case for soft-loss functions. In Proc. of HCOMP . -->

<!-- [原子块 · verbatim] Uma et al. (2021b) Alexandra Uma, Tommaso Fornaciari, Dirk Hovy, Silviu Paun, Barbara Plank, and Massimo Poesio. 2021b. Learning from disagreement: A survey. Journal of Artificial Intelligence Researc -->

<!-- [原子块 · verbatim] Webber and Joshi (2012) Bonnie Webber and Aravind Joshi. 2012. Discourse structure and computation: Past, present and future . In Proceedings of the ACL-2012 Special Workshop on Rediscovering 50 Years -->

<!-- [原子块 · verbatim] Wich et al. (2021) Maximilian Wich, Christian Widmer, Gerhard Hagerer, and Georg Groh. 2021. Investigating annotator bias in abusive language datasets . In Proceedings of the International Conference  -->

<!-- [原子块 · verbatim] Zeman (2010) Daniel Zeman. 2010. Hard problems of tagset conversion. In Proceedings of the Second International Conference on Global Interoperability for Language Resources , pages 181–185. -->

<!-- [原子块 · verbatim] Zhang and Plank (2021) Mike Zhang and Barbara Plank. 2021. Cartography active learning . In Findings of the Association for Computational Linguistics: EMNLP 2021 , pages 395–406, Punta Cana, Dominican -->

<!-- [原子块 · verbatim] Zhang et al. (2021) Shujian Zhang, Chengyue Gong, and Eunsol Choi. 2021. Learning with different amounts of annotation: From zero to many labels. arXiv preprint arXiv:2109.04408 . -->

<!-- [原子块 · verbatim] Zhang and de Marneffe (2021) Xinliang Frederick Zhang and Marie-Catherine de Marneffe. 2021. Identifying inherent disagreement in natural language inference . In Proceedings of the 2021 Conference of  -->

**EN** Appendix A Datasets with Multiple Annotations

**ZH** 附录 A 具有多重标注的数据集

<!-- [原子块 · table] Field Reference Name/Description URL Jair PDAI SemEval21 TACL22 SemEval23 NLP Passonneau et al. (2010) Word sense disambiguation (WSD) https://anc.org/ Plank et al. (2014a) POS tagging (500 tweets fro -->

**EN** Table 1: Overview of publicly-available datasets with Hlv data (see repository for updates and to contribute: https://github.com/mainlp/awesome-human-label-variation). ⟦SLOT_3⟧: whether the source was used in broader empirical evaluations, e.g., the JAIR survey on learning from disagreement Uma et al. (2021b), is listed on pdai.info Basile et al. (2021a) (as of June, 2022), is part of the SemEval 2021 task on learning from disagreement Uma et al. (2021a), is used in a TACL paper on learning beyond majority vote Davani et al. (2022), is used in the SemEval 2023 shared task on Learning With Disagreement LeWiDi https://le-wi-di.github.io/.

**ZH** 表 1：公开可得的、带有 HLV 数据的数据集概览（更新与贡献请见仓库：https://github.com/mainlp/awesome-human-label-variation）。⟦SLOT_3⟧：该来源是否被用于更广泛的实证评测，例如关于从分歧中学习的 JAIR 综述 Uma 等（2021b）、是否列于 pdai.info Basile 等（2021a）（截至 2022 年 6 月）、是否属于 SemEval 2021 从分歧中学习任务 Uma 等（2021a）、是否被关于超越多数投票学习的 TACL 论文采用 Davani 等（2022）、是否用于 SemEval 2023 共享任务 Learning With Disagreement（LeWiDi）https://le-wi-di.github.io/。
