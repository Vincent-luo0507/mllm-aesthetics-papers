# 评判评判者：LLM-as-a-Judge 中位置偏差的系统研究

> 原标题：Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge
> 作者：Lin Shi, Chiyu Ma, Wenhua Liang, Xingjian Diao, Weicheng Ma, Soroush Vosoughi · arXiv:2406.07791 · 2024-06-12

<!-- [原子块 · verbatim] Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] LLM-as-a-Judge has emerged as a promising alternative to human evaluators across various tasks, yet inherent biases—particularly position bias, the tendency to favor solutions based on their position  -->

**EN** 1 Introduction

**ZH** 1 引言

<!-- [原子块 · object]  -->

**EN** Figure 1: Overview of our experiment settings: (a) Position bias is observed when LLM judges consistently favor a specific position rather than evaluating the content, with repeated trials ensuring the deviations are not due to random variations. (b) Preference fairness is defined and measured through the distribution of choice pairs to assess the fairness of judgments. (c) The settings are extended from pairwise comparisons to list-wise comparisons, involving evaluations of more than two candidate models.

**ZH** 图 1：我们的实验设置概览。（a）当 LLM 评判者始终偏向某个特定位置、而非依据内容做评估时，即观察到位置偏差；通过重复试验可确保这些偏离并非随机波动所致。（b）偏好公平性通过选项对的分布来定义与度量，用以评估判断的公平程度。（c）设置从成对比较扩展到列表式比较，涉及对三个以上候选模型的评估。

**EN** In recent years, Large Language Models (LLMs) have emerged as evolutionary technologies, gathering global interest and stimulating substantial research into their applications. Evaluating LLMs has received increasing attention due to their advancing capabilities across diverse fields. While human assessment is considered the gold standard for aligning with human preferences, it lacks scalability in extensive evaluations Zeng et al. 2023; Karpinska et al. 2021. To automate evaluations and reduce reliance on costly human evaluators, the LLM-as-a-Judge methodology emerged as a promising alternative across various tasks. Despite a high level of agreement with human judgments Zheng et al. 2024b; Li et al. 2024a; Zhu et al. 2023, inherent biases, especially position bias, have undermined the accuracy, fairness, and reliability of these LLM evaluators.

**ZH** 近年来，大语言模型（LLM）作为一项变革性技术兴起，引发了全球关注，并推动了大量关于其应用的研究。由于 LLM 在多个领域的能力不断提升，如何评估 LLM 也日益受到重视。尽管人工评估被视为与人类偏好对齐的黄金标准，但在大规模评测中缺乏可扩展性（Zeng 等 2023；Karpinska 等 2021）。为使评估自动化、减少对昂贵人工评估者的依赖，LLM 作为评判者（LLM-as-a-Judge）方法应运而生，成为各类任务中颇具前景的替代方案。尽管它与人类判断有很高的一致性（Zheng 等 2024b；Li 等 2024a；Zhu 等 2023），但固有的偏差——尤其是位置偏差——削弱了这些 LLM 评估器的准确性、公平性与可靠性。

**EN** Position bias refers to the tendency of LLM judges to favor certain positions within prompt components rather than the content itself, as shown in Fig. 1 (a). This bias has been prevalent in all types of LLM judges Qin et al. 2024; Li et al. 2023d, raising concerns about their reliability. Previous studies Zheng et al. 2024a; Zheng et al. 2024b; Zeng et al. 2023 have identified position bias alongside other biases and assessed its impact. Although mitigation strategies have been proposed, they often fall short due to incomplete bias elimination Guo et al. 2024, increased complexity Li et al. 2024b; Khan et al. 2024; Chua et al. 2024, the introduction of new biases Ohi et al. 2024, inconsistent effectiveness Gallegos et al. 2024, or impracticality for closed-source models, as mechanistic solutions require modifications to model internals Wang et al. 2025; Yu et al. 2025. From an exploratory perspectives, despite empirical studies evaluating position bias in pairwise LLM-as-a-Judge settings Zheng et al. 2024b; Wang et al. 2023, the underlying factors contributing to this phenomenon and extended measurements in list-wise comparative paradigms remain incompletely explored.

**ZH** 位置偏差指的是 LLM 评判者倾向于偏好提示组成中某些特定位置、而非内容本身，如图 1（a）所示。这一偏差在各类 LLM 评判者中都普遍存在（Qin 等 2024；Li 等 2023d），引发了对它们可靠性的担忧。前人研究（Zheng 等 2024a；Zheng 等 2024b；Zeng 等 2023）已识别出位置偏差及其他偏差，并评估了其影响。尽管已有缓解策略被提出，它们往往因偏差消除不彻底（Guo 等 2024）、复杂度增加（Li 等 2024b；Khan 等 2024；Chua 等 2024）、引入新偏差（Ohi 等 2024）、效果不稳定（Gallegos 等 2024），或对闭源模型不可行而收效有限——因为机理层面的解决方案需要修改模型内部（Wang 等 2025；Yu 等 2025）。从探索性视角看，尽管已有实证研究在成对的 LLM-as-a-Judge 设置下评估位置偏差（Zheng 等 2024b；Wang 等 2023），导致该现象的深层因素，以及在列表式比较范式下的扩展度量，仍未被充分探索。

**EN** In this study, we provide an in-depth and systematic investigation into position bias within the context of LLM-as-a-Judge. While evaluating Position Consistency Zheng et al. 2024b, one of the most widely used methods for measuring position bias, we introduce two novel metrics: Preference Fairness and Repetition Stability. Specifically, we move beyond simply assessing Position Consistency by incorporating Preference Fairness, which provides deeper insights into the specific answer directions where models exhibit unfair preferences. Additionally, the measurement of Repetition Stability ensures that the observed position bias in the given model and tasks is not due to random variations, thus strengthening the reliability of the findings.

**ZH** 本研究对 LLM-as-a-Judge 背景下的位置偏差做了深入而系统的考察。在评估位置一致性（Position Consistency，一种最广泛使用的位置偏差度量方法）（Zheng 等 2024b）的同时，我们引入了两个新指标：偏好公平性（Preference Fairness）与重复稳定性（Repetition Stability）。具体而言，我们不止于评估位置一致性，还纳入偏好公平性，从而更深入地洞察模型在哪些具体的答案方向上表现出不公平偏好。此外，重复稳定性的度量可确保在给定模型与任务上观察到的位置偏差并非随机波动所致，从而强化研究发现的可靠性。

**EN** To investigate the underlying factors contributing to position bias, we categorized these factors into three levels: Judge-Level, Candidate-Level, and Task-Level. Our experiments are primarily conducted on pairwise comparisons, as LLM judges demonstrate superior performance in this setting. We further extend our study to more complicated list-wise comparison settings, involving evaluations of more than two candidate models by LLM judges. Our findings reveal several key insights: 1. The position bias of capable LLM judges is not a result of random variations. 2. There is a high volatility in the direction of preference, even within the same LLM judge when applied to different tasks. 3. Differences in answer quality among candidate models significantly influence position consistency. 4. Position bias is very weakly correlated with the length of prompts generated by the candidate models.

**ZH** 为探究导致位置偏差的深层因素，我们把这些因素归为三个层面：评判者层面、候选层面与任务层面。我们的实验主要在成对比较上进行，因为 LLM 评判者在该设置下表现更优；我们进一步把研究扩展到更复杂的列表式比较设置，涉及由 LLM 评判者评估三个以上候选模型。我们的发现揭示了若干关键洞察：1. 能力较强的 LLM 评判者的位置偏差并非随机波动的结果。2. 偏好方向具有高度波动性，即便同一 LLM 评判者应用于不同任务时也是如此。3. 候选模型之间的答案质量差异会显著影响位置一致性。4. 位置偏差与候选模型所生成提示的长度只有极弱的相关性。

**EN** Building on these findings, we conduct an agreement analysis among the LLM judges. The results reveal that, although measures of position consistency may appear similar in general, judgments on specific instances vary significantly among LLM judges, even when they demonstrate comparable capabilities. Instances where numerous LLMs agree are generally easier to judge, whereas instances with disagreements are more challenging to evaluate and more prone to position bias. This analysis provides insights into the distribution of judging difficulty across the dataset and highlights the potential for dataset modifications by incorporating more instances that are either easier or more difficult to judge. Future work could explore how to measure the likelihood of position bias arise from the datasets by identifying and quantifying such hard-to-judge instances before implementing LLM judges.

**ZH** 在这些发现的基础上，我们对 LLM 评判者之间做了一致性分析。结果表明，尽管位置一致性的度量在总体上看似相近，但 LLM 评判者在具体实例上的判断差异显著，即便它们表现出相当的能力。多数 LLM 意见一致的实例通常更容易判断，而存在分歧的实例则更难评估，也更容易受到位置偏差影响。这一分析揭示了数据集中判断难度的分布，并指出了通过纳入更多易判或难判实例来改造数据集的潜力。未来工作可探索如何在部署 LLM 评判者之前，通过识别并量化这类难判实例，来度量数据集引发位置偏差的可能性。

**EN** 2 Evaluation Settings & Definitions

**ZH** 2 评测设置与定义

**EN** We begin by outlining the settings for pairwise and list-wise comparisons employed in our experiments for LLM-as-a-Judge. Following this, we define the three metrics used in our evaluation: Position Consistency (PC), Preference Fairness (PF), and Repetition Stability (RS). Finally, we provide a detailed description of the factors we found that are related to position bias at the Judge-Level, Candidate-Level, and Task-Level. Our exploratory study was conducted post hoc, meaning the LLM judgments were collected first, and the factors influencing position bias were then identified and analyzed.

**ZH** 我们首先概述实验中用于 LLM-as-a-Judge 的成对比较与列表式比较设置；随后定义评测所用的三个指标：位置一致性（PC）、偏好公平性（PF）与重复稳定性（RS）；最后详细描述我们在评判者层面、候选层面与任务层面发现的与位置偏差相关的因素。我们的探索性研究是事后进行的，即先收集 LLM 判断，再识别并分析影响位置偏差的因素。

**EN** 2.1 Pairwise & List-wise Comparison

**ZH** 2.1 成对比较与列表式比较

**EN** Pairwise Comparison: In the context of pairwise comparison, LLM judges are tasked with selecting the better solution provided by two candidate models in response to a given task question. As shown in Fig. 1 (a), the system prompt, option choices, task question, and solutions from two candidate models (original prompt) are presented to the LLM judges to select the better solution. The experiment is conducted in a double-blind setting. The identities of the candidate models are hidden from the LLM judges, and the candidate models are unaware that their solutions will be compared to another model when answering the question. Then, the prompt with solutions in a swapped position (swapped prompt) is given to the same LLM judge again, which results in a judgment pair. If the LLM judge consistently favors the same solution regardless of the swapped position, it is considered position consistent. Conversely, if the LLM judge selects different winners, position bias is observed, with the preference direction being either primacy (e.g. always choose ⟦SLOT_0⟧) or recency (e.g. always choose ⟦SLOT_1⟧). Example of measuring preference fairness with specific choice pairs is shown in Fig. 1 (b). To accommodate the possibility of ties, various option modes are employed: Two-Option mode restricts LLM judges to choosing between two options, labeled A for the first candidate and B for the second. Three-Option mode introduces an additional choice, C, allowing LLM judges to indicate a tie if neither solution is preferable, as illustrated in Fig. 1 (a). These option modes were explicitly specified in the system prompts to ensure clear guidance for the decision-making process of the LLM judges.

**ZH** 成对比较：在成对比较中，LLM 评判者的任务是从两个候选模型针对给定任务问题给出的方案中选出更好的一个。如图 1（a）所示，系统提示、选项、任务问题以及两个候选模型的方案（原始提示）被呈现给 LLM 评判者以供其选择更好的方案。实验在双盲设置下进行：候选模型的身份对 LLM 评判者隐藏，且候选模型在回答问题时并不知晓自己的方案会与另一模型比较。随后，把方案位置交换后的提示（交换提示）再次交给同一个 LLM 评判者，由此得到一个判断对。若 LLM 评判者不论位置如何交换都始终选择同一方案，则被认为是位置一致的；反之，若 LLM 评判者选出不同的胜者，则观察到位置偏差，其偏好方向为首位偏好（例如始终选择 ⟦SLOT_0⟧）或末位偏好（例如始终选择 ⟦SLOT_1⟧）。用具体选项对度量偏好公平性的示例如图 1（b）所示。为兼顾平局的可能，我们采用多种选项模式：二选项模式限制 LLM 评判者在两个选项之间选择，第一个候选标为 A、第二个标为 B；三选项模式引入一个额外选项 C，允许 LLM 评判者在两个方案都不更优时表示平局，如图 1（a）所示。这些选项模式都在系统提示中明确指定，以确保为 LLM 评判者的决策过程提供清晰指引。

**EN** List-wise Comparison: Unlike pairwise settings, where LLM judges select the superior solution from two candidates, list-wise comparative approaches involve evaluating three or more candidates simultaneously, as shown in Fig. 1 (c). For efficiency, we prompt LLM judges to select the best candidate rather than ranking the entire list. The “swapped setting" used in pairwise evaluations is generalized to order permutations for list-wise judgments, ensuring that each candidate appears in every possible position exactly once. For a list of ⟦SLOT_2⟧ candidates, this results in ⟦SLOT_3⟧ permutations. In the ⟦SLOT_4⟧ permutation, the ⟦SLOT_5⟧ candidate is set to appear in the first position. Additionally, an option is provided to account for ties, allowing LLM judges to indicate if there is no certainly superior solution.

**ZH** 列表式比较：与成对设置中 LLM 评判者从两个候选中选出更优方案不同，列表式比较方法同时评估三个或更多候选，如图 1（c）所示。为提高效率，我们提示 LLM 评判者选出最佳候选，而非对整个列表排序。成对评估中所用的“交换设置”在列表式判断中被推广为顺序排列，确保每个候选恰好在每个位置出现一次。对于含 ⟦SLOT_2⟧ 个候选的列表，这会产生 ⟦SLOT_3⟧ 种排列。在第 ⟦SLOT_4⟧ 种排列中，⟦SLOT_5⟧ 候选被设定为出现在第一位。此外，还提供了一个用于平局的选项，允许 LLM 评判者表示不存在确定的更优方案。

**EN** 2.2 Evaluation Metrics

**ZH** 2.2 评测指标

**EN** In our study, we first verify whether capable LLM judges exhibit high repetition stability and then evaluate their position bias in terms of position consistency and preference fairness. The metrics are introduced as follows:

**ZH** 在我们的研究中，我们首先验证能力较强的 LLM 评判者是否表现出较高的重复稳定性，然后从位置一致性与偏好公平性两方面评估它们的位置偏差。各指标介绍如下：

**EN** Repetition Stability (⟦SLOT_6⟧) evaluates the reliability of LLM judges when presented with identical queries multiple times. It is essential to determine whether the judgments of LLMs, and consequently the observations of position bias, stem from a consistent evaluation pattern or by random variations. We measure this by calculating the percentage of the most frequent selections across multiple trials for each query, aggregated from all queries within each dataset. This metric is formalized as

**ZH** 重复稳定性（⟦SLOT_6⟧）评估 LLM 评判者在多次面对相同查询时的可靠性。判断 LLM 的判断以及由此观察到的位置偏差究竟源于一致的评估模式还是随机波动，这一点至关重要。我们通过计算每个查询在多次试验中最频繁被选中的选项所占百分比来度量该指标，并在每个数据集内对所有查询汇总。该指标的形式化定义如下

<!-- [原子块 · table] R ​ C \displaystyle RC = 1 N ​ ∑ j = 1 N 1 n j ​ max k ∈ S ​ { | C k j | } , \displaystyle=\frac{1}{N}\sum_{j=1}^{N}\frac{1}{n_{j}}\max_{k\in S}\left\{|C_{k}^{j}|\right\}, (1) -->

**EN** where ⟦SLOT_7⟧ refers to the set of choice options depending on the option mode, ⟦SLOT_8⟧ denotes the counts of each choice option selected by the judge for the ⟦SLOT_9⟧ query, ⟦SLOT_10⟧ represents the total number of repeating trials for that query, and ⟦SLOT_11⟧ is the total number of queries. The value of ⟦SLOT_12⟧ ranges from a small positive value depending on the option mode, indicating completely random decisions, to 1.0, indicating perfect stability.

**ZH** 其中 ⟦SLOT_7⟧ 指取决于选项模式的选项集合，⟦SLOT_8⟧ 表示评判者对 ⟦SLOT_9⟧ 查询选择各选项的计数，⟦SLOT_10⟧ 表示该查询的重复试验总次数，⟦SLOT_11⟧ 为查询总数。⟦SLOT_12⟧ 的取值范围从取决于选项模式的一个小正值（表示完全随机的决策）到 1.0（表示完全稳定）。

**EN** Position Consistency (⟦SLOT_13⟧) quantifies how frequently LLM judges prefer the same solution after the order of solutions is permuted. It is calculated as the ratio of consistent evaluation series to the total number of valid evaluations, where a series is deemed consistent if the LLM judge prefers the same winning solution across permutations. Formally, it is calculated as

**ZH** 位置一致性（⟦SLOT_13⟧）量化 LLM 评判者在方案顺序被置换后偏好同一方案的频繁程度。它计算为一致的评估序列占有效评估总数的比例：若 LLM 评判者在各种排列下都偏好同一个胜出方案，则该序列被视为一致。形式上，其计算方式为

<!-- [原子块 · table] P ​ C \displaystyle PC = 1 n ∑ j = 1 n 𝟏 { ( C 1 j , … , C p j , ) ∈ V } , \displaystyle=\frac{1}{n}\sum_{j=1}^{n}\mathbf{1}_{\{(C_{1}^{j},\dots,C_{p}^{j},)\in V\}}, (2) -->

**EN** where ⟦SLOT_14⟧ is the set of choices that correspond to position consistency, and ⟦SLOT_15⟧ denotes the judgment series for the ⟦SLOT_16⟧ query when there are ⟦SLOT_17⟧ candidate solutions in the list, and ⟦SLOT_18⟧ represents the number of prompt series. An example of such series of choices under pairwise comparison setting can be found in Fig. 1 (b). This formula aims to provide a direct measure of a LLM judge’s position bias and has been widely used in previous studies for its simplicity.

**ZH** 其中 ⟦SLOT_14⟧ 是与位置一致性相对应的选择集合，⟦SLOT_15⟧ 表示列表中含 ⟦SLOT_16⟧ 个候选方案时 ⟦SLOT_17⟧ 查询的判断序列，⟦SLOT_18⟧ 表示提示序列的数量。成对比较设置下这类选择序列的示例如图 1（b）所示。该公式旨在直接度量 LLM 评判者的位置偏差，因其简洁性而在前人研究中被广泛使用。

**EN** Preference Fairness (⟦SLOT_19⟧) measures the extent to which LLM judges favor certain solution positions. In pairwise comparisons, an LLM judge may exhibit a preference for either primacy or recency. These terms replace the more verbose “preference/bias for the first/second candidate model" used in previous studies Zheng et al. 2024b, ensuring clarity and generalization for future research. The examples of such preferences are demonstrated in Fig. 1 (b). Previous studies proposed two common ways to measure the preference fairness. One way is to count the primacy-preferred and recency-preferred judgment pairs, which we termed as primacy-count-number (⟦SLOT_20⟧) and recency-count-number (⟦SLOT_21⟧). The counts are then normalized by the total number of prompt pairs (Zheng et al. 2024b; Zhu et al. 2023). However, the sensitivity of this measurement highly depends on the size of dataset, making comparisons across datasets unreliable, especially when the number of questions and instances varies for each task.

**ZH** 偏好公平性（⟦SLOT_19⟧）度量 LLM 评判者偏好某些方案位置的程度。在成对比较中，LLM 评判者可能表现出首位偏好或末位偏好。这两个术语取代了前人研究（Zheng 等 2024b）中较为冗长的“对第一个/第二个候选模型的偏好或偏差”，以确保表述清晰并便于未来研究推广。这类偏好的示例如图 1（b）所示。前人研究提出了两种度量偏好公平性的常见方式：其一是统计偏好首位与偏好末位的判断对数量，我们称之为首位计数（⟦SLOT_20⟧）与末位计数（⟦SLOT_21⟧），随后按提示对总数归一化（Zheng 等 2024b；Zhu 等 2023）。然而，该度量的敏感度高度依赖数据集规模，使跨数据集的比较不可靠，尤其当每个任务的问题数与实例数各不相同的时候。

**EN** Alternatively, instead of normalizing over the complete dataset, studies like (Li et al. 2023c; Liusie et al. 2024) treat position inconsistent evaluation instances independently. They calculate the percentages of primacy-preferred and recency-preferred judgment pairs relative to the total number of position inconsistent pairs. We denote these as inconsistent primacy rates (⟦SLOT_22⟧) and inconsistent recency rates (⟦SLOT_23⟧), where ⟦SLOT_24⟧. However, this approach overlooks the fact that “position consistent judgments are also preference fair”, which leads to overly penalizing highly consistent LLM-judges.

**ZH** 另一种方式是，研究者（Li 等 2023c；Liusie 等 2024）不按整个数据集归一化，而是独立处理位置不一致的评测实例，计算偏好首位与偏好末位的判断对占位置不一致对总数的百分比。我们把它们记为不一致首位率（⟦SLOT_22⟧）与不一致末位率（⟦SLOT_23⟧），其中 ⟦SLOT_24⟧。然而，这种做法忽略了“位置一致的判断同样是偏好公平的”这一事实，从而对高度一致的 LLM 评判者造成过度惩罚。

**EN** To overcome these limitations, we introduce a more granular and scalable measurement that combines the strengths of both methods, to assess preference fairness. The ⟦SLOT_25⟧ score is formally calculated by

**ZH** 为克服这些局限，我们引入一种更细粒度、更具可扩展性的度量，兼取两种方法之长，用以评估偏好公平性。⟦SLOT_25⟧ 分数的形式化计算如下

<!-- [原子块 · table] P ​ F \displaystyle PF = P ​ F raw − S min − S max + − S min − × 2 − 1 , \displaystyle=\frac{PF_{\text{raw}}-S^{-}_{\min}}{S^{+}_{\max}-S^{-}_{\min}}\times 2-1, (3) P ​ F raw \displaystyle PF_{\text{r -->

**EN** where ⟦SLOT_26⟧ and ⟦SLOT_27⟧ are the minimum and maximum achievable ⟦SLOT_28⟧ scores for each judge on each task, respectively. This min-max scale ensures comparability across datasets by accounting for the range of achievable scores and centering the scale around zero. The ⟦SLOT_29⟧ score is interpreted as follows:

**ZH** 其中 ⟦SLOT_26⟧ 与 ⟦SLOT_27⟧ 分别为每个评判者、每个任务上可取得的 ⟦SLOT_28⟧ 分数的最小值与最大值。这种最小—最大缩放通过考虑可取得分数的极差并把尺度中心定在零附近，确保了跨数据集的可比性。⟦SLOT_29⟧ 分数的解释如下：

<!-- [原子块 · table] P ​ F = { 1 , if ​ P ​ C = 0 ​ and entirely recency-preferred x ∈ ( 0 , 1 ) , Recency-preferred 0 , Preference Fair x ∈ ( − 1 , 0 ) , Primacy-preferred − 1 , if ​ P ​ C = 0 ​ and entirely primacy-pref -->

**EN** To extend this metric to list-wise comparisons, we employed a ‘one vs. all’ approach, defining primacy preference as favoring the first candidate solution while classifying all others as recency-preferred. This straightforward extension of the ⟦SLOT_30⟧ computation maintains consistency with pairwise setups. By providing a single and comprehensive metric that applies to all evaluation instances and list-wise settings, our proposed ⟦SLOT_31⟧ score ensures sensitivity across datasets, regardless of variations in the number of questions or instances, offering a significant improvement over previous methods.

**ZH** 为把该指标扩展到列表式比较，我们采用了一种一对多的方式：把首位偏好定义为偏好第一个候选方案，而把其余所有情况归为末位偏好。这一对 ⟦SLOT_30⟧ 计算的直接扩展保持了与成对设置的一致性。通过提供一个适用于所有评测实例与列表式设置的单一综合指标，我们提出的 ⟦SLOT_31⟧ 分数确保了跨数据集的敏感度，而不受问题数或实例数变化的影响，相较此前方法有显著改进。

**EN** 2.3 Factors Affecting Position Bias

**ZH** 2.3 影响位置偏差的因素

**EN** To investigate the factors influencing position bias in LLM judges, we categorized these factors into three groups: Judge-level, Candidate-level, and Task-level factors. Each group includes specific factors, that we hypothesize, may impact position bias, which we explore through a series of experiments. Table 1 lists the five factors we analyzed in this study.

**ZH** 为考察影响 LLM 评判者位置偏差的因素，我们把这些因素归为三组：评判者层面、候选层面与任务层面的因素。每组包含我们假设可能影响位置偏差的具体因素，并通过一系列实验加以探索。表 1 列出了本研究分析的五个因素。

**EN** Among the influencing factors, we selected “familial property” for Judge-level factors, as it reflects similar model sizes or training specifics, which are often proprietary and not publicly accessible for closed-source capable models. The familial categories of the models used in our studies are (1) GPT, (2) Claude, (3) Gemini, and (4) Llama allowing for straightforward grouping by company and version. More details and discussions about the familial property can be found in Appendix Sec. C.

**ZH** 在这些影响因素中，我们为评判者层面因素选取了“家族属性”，因为它反映了相近的模型规模或训练细节——对于能力强但闭源的模型，这些信息通常是专有的、不公开的。我们研究中使用的模型家族类别为（1）GPT、（2）Claude、（3）Gemini 与（4）Llama，便于按公司与版本直接分组。关于家族属性的更多细节与讨论见附录 C 节。

**EN** Answer quality gap: While prior studies Wang et al. 2023 explored quality disparities using "score gaps" in score-based LLM-as-a-Judge, this factor remains under-explored in comparative settings, which we address by introducing "answer quality gap" for both pairwise and list-wise evaluations. We define the quality of a candidate’s solution by how effectively it addresses the question. Consequently, the answer quality gap refers to the disparity in quality between the solutions from one candidate model and the others to the same question and hence considered the Candidate-level factor. Ideally, when a reliable LLM judge is presented with a question and corresponding answer pairs or series, it would prefer the highest-quality answer, where the corresponding candidate is denoted as the winner selected by the LLM judge.

**ZH** 答案质量差距：尽管前人研究（Wang 等 2023）已在基于打分的 LLM-as-a-Judge 中用“分数差距”探索质量差异，该因素在比较式设置中仍未得到充分研究；我们通过为成对与列表式评估引入“答案质量差距”来弥补这一点。我们把候选方案的质量定义为它回答问题的有效程度。由此，答案质量差距指同一个问题下某一候选模型的方案与其他方案之间的质量落差，因而被视为候选层面的因素。理想情况下，当一个可靠的 LLM 评判者面对一个问题及相应的答案对或答案序列时，它会偏好质量最高的答案，其中对应的候选被称为 LLM 评判者选出的胜者。

**EN** Following this assumption, we measure the answer quality gap by the win rates of candidates over an expected baseline on a set of tasks and questions. However, if position bias occurs, the winner may be inconsistent when the order of candidate solutions is permuted in the query. Therefore, we categorize the LLM judgments into three groups: cases where the same winner is consistently chosen across all permutations (termed “consistent wins”), cases where there is no certain winner (termed “consistent ties”), and cases where different winners are selected after the solutions are permuted in the queries (termed “inconsistent judgment series"). We denote these counts as the number of consistent wins (⟦SLOT_32⟧), consistent ties (⟦SLOT_33⟧), and inconsistent judgment series (⟦SLOT_34⟧), respectively. Inspired by Zheng et al. 2024b, we count inconsistent judgment pairs as ties for all candidate models, which is later calculated as a down-scaled win rate depending on the number of candidate models.

**ZH** 依据这一假设，我们通过候选在一组任务与问题上相对于期望基线的胜率来度量答案质量差距。然而，若出现位置偏差，当查询中候选方案的顺序被置换时，胜者可能不一致。因此，我们把 LLM 判断分为三类：在所有排列中都稳定选出同一胜者的情形（称为“一致胜出”）、没有确定胜者的情形（称为“一致平局”），以及在查询中置换方案后选出不同胜者的情形（称为“不一致判断序列”）。我们把这三类计数分别记为一致胜出数（⟦SLOT_32⟧）、一致平局数（⟦SLOT_33⟧）与不一致判断序列数（⟦SLOT_34⟧）。受 Zheng 等 2024b 启发，我们把不一致判断对计为所有候选模型的平局，随后按候选模型数量折算为下调后的胜率。

**EN** To calculate the win rates of candidate models for all three cases, we define the overall win rate (⟦SLOT_35⟧) of a model’s solution over the other as: ⟦SLOT_36⟧, where we have ⟦SLOT_37⟧ candidates in the list and ⟦SLOT_38⟧ judgment series. Then the answer quality gap (⟦SLOT_39⟧) is calculated as ⟦SLOT_40⟧, where ⟦SLOT_41⟧ is the expected baseline when all judgments are “ties”. In contrast to using only consistent win rate (calculated as ⟦SLOT_42⟧, where ⟦SLOT_43⟧ is the number of position consistent judgment series) to quantify ⟦SLOT_44⟧ (Zheng et al. 2024b; Li et al. 2023b; Raina et al. 2024), the adoption of overall win rate incorporates all data points and captures the “comparable quality” cases, where responses in similar quality might lead to position biased judgments, a scenario that the consistent win rate might overlook.

**ZH** 为计算全部三种情形下候选模型的胜率，我们把某模型方案相对其他方案的总体胜率（⟦SLOT_35⟧）定义为：⟦SLOT_36⟧，其中列表中有 ⟦SLOT_37⟧ 个候选、⟦SLOT_38⟧ 个判断序列。随后，答案质量差距（⟦SLOT_39⟧）计算为 ⟦SLOT_40⟧，其中 ⟦SLOT_41⟧ 为所有判断都是“平局”时的期望基线。与仅使用一致胜率（计算为 ⟦SLOT_42⟧，其中 ⟦SLOT_43⟧ 为位置一致的判断序列数）来量化 ⟦SLOT_44⟧（Zheng 等 2024b；Li 等 2023b；Raina 等 2024）不同，采用总体胜率纳入了所有数据点，并能捕捉“质量相当”的情形——在这种情形下质量相近的回应可能导致带位置偏差的判断，而这正是一致胜率可能忽略的场景。

**EN** 3 Experiment

**ZH** 3 实验

**EN** 3.1 Experiment Settings

**ZH** 3.1 实验设置

**EN** In this study, we evaluated position bias of 15 models from the GPT (OpenAI 2023), Claude (Anthropic 2024), Gemini (Gemini Team 2024), and Llama (Touvron et al. 2023) series using our framework. For datasets, we adopted the modified MTBench (Zheng et al. 2024b) and DevBench (Li et al. 2024a) due to their demonstrated high human-LLM agreement and the validated reliability of state-of-the-art LLM judges on the evaluation tasks. For pairwise comparisons, We fixed one of the candidates as vicuna-13b-v1.3 for MTBench and human for DevBench to serve as baselines, ensuring decent quality of solutions to the given questions. MTBench consists of 30 candidate models, 8 tasks, and 10 questions per task; for DevBench, we divide the general metric into more detailed ones and consider them as different tasks, resulting in 10 candidate models, 14 tasks, and 8 questions per task. We then paired solutions of these candidate models with that of the baseline candidate for evaluation by the LLM judges.

**ZH** 本研究用我们的框架评估了来自 GPT（OpenAI 2023）、Claude（Anthropic 2024）、Gemini（Gemini Team 2024）与 Llama（Touvron 等 2023）系列的 15 个模型的位置偏差。数据集方面，我们采用经过改造的 MTBench（Zheng 等 2024b）与 DevBench（Li 等 2024a），因为它们在人类与 LLM 之间表现出高度一致性，且最先进的 LLM 评判者在这些评测任务上的可靠性已得到验证。在成对比较中，我们把其中一个候选固定为基线：MTBench 用 vicuna-13b-v1.3，DevBench 用 human，以确保对给定问题的方案具有体面的质量。MTBench 包含 30 个候选模型、8 个任务、每个任务 10 个问题；对 DevBench，我们把通用指标拆分为更细的指标并视作不同任务，由此得到 10 个候选模型、14 个任务、每个任务 8 个问题。随后我们把这些候选模型的方案与基线候选的方案配对，交由 LLM 评判者评估。

**EN** We adopted Two-option mode for MTBench, and Three-option mode for DevBench. For list-wise experiments, we randomly sampled 9 models to form three triple-candidate lists and evaluated four representative LLM judges on MTBench. The prompt templates we used are identical to those in the benchmarks for pairwise comparisons, with minor modifications to accommodate list-wise evaluations. More details about the models, tasks, and prompts can be found in Appendix. Sec. F.

**ZH** 我们对 MTBench 采用二选项模式，对 DevBench 采用三选项模式。在列表式实验中，我们随机采样 9 个模型构成三个三候选列表，并在 MTBench 上评估四个代表性 LLM 评判者。我们使用的提示模板与基准中成对比较所用的完全一致，仅做了少量修改以适应列表式评估。关于模型、任务与提示的更多细节见附录 F 节。

**EN** To compute repetition stability, we sampled 3 questions per task and 4 candidate models, paired with baseline candidates, for each LLM judge to evaluate across 3 repetitive trials. This resulted in 576 instances per judge for MTBench and 432 instances per judge for DevBench. The temperature hyperparameter was set to 1 for all LLM judges to generate nontrivial results. To compute position consistency and preference fairness, the number of instances increased to 4,800 and 2,240, covering the entire MTBench and DevBench datasets. In total, more than 100,000 evaluation instances were analyzed in this study.

**ZH** 为计算重复稳定性，我们为每个任务采样 3 个问题与 4 个候选模型，与基线候选配对，交由每个 LLM 评判者在 3 次重复试验中评估。这在 MTBench 上每个评判者产生 576 个实例，在 DevBench 上产生 432 个实例。所有 LLM 评判者的温度超参数均设为 1，以生成非平凡的结果。为计算位置一致性与偏好公平性，实例数增至 4,800 与 2,240，覆盖整个 MTBench 与 DevBench 数据集。本研究共分析了超过 100,000 个评测实例。

**EN** To identify significant factors contributing to position bias, we performed bidirectional stepwise regression on data from the two benchmarks. We used variables such as average lengths of input, output, and prompt; answer quality gap; LLM judge series; candidate identities; and task categories to predict ⟦SLOT_45⟧ and ⟦SLOT_46⟧, respectively. Each model prunes non-significant variables based on the Akaike Information Criterion (AIC) score. This process involves both forward selection and backward elimination, with each "step" testing whether including or excluding a variable improves the model’s AIC value. Further details about the process can be found in Appendix. Sec. E.

**ZH** 为识别导致位置偏差的显著因素，我们对两个基准上的数据做了双向逐步回归。我们使用输入、输出与提示的平均长度、答案质量差距、LLM 评判者系列、候选身份与任务类别等变量，分别预测 ⟦SLOT_45⟧ 与 ⟦SLOT_46⟧。每个模型依据赤池信息准则（AIC）分数剪除不显著的变量。该过程同时包含前向选择与后向剔除，每个“步”都检验纳入或剔除某个变量是否能改善模型的 AIC 值。该过程的更多细节见附录 E 节。

<!-- [原子块 · table] Factor Judge-level Candidate-level Task-level Familial Property ✓ \checkmark * × \times × \times Answer Quality Gap × \times ✓ \checkmark * × \times Task Input Length × \times × \times ✓ \checkmark Ta -->

**EN** Table 1: Factors influencing position bias. Significant factors, identified via bidirectional stepwise regression, are marked with * and highlighted in red based on empirical findings on both MTBench and DevBench results. Task Input refers to the question itself, while Task Output denotes the candidate model’s answers, serving as both Candidate-level and Task-level factors. Prompt includes the full query presented to LLM judges: Task Input, Task Output, and system prompts.

**ZH** 表 1：影响位置偏差的因素。通过双向逐步回归识别出的显著因素以 * 标记，并依据在 MTBench 与 DevBench 两个结果上的实证发现以红色高亮。任务输入指问题本身，任务输出指候选模型的答案，二者同时充当候选层面与任务层面的因素。提示包含呈现给 LLM 评判者的完整查询：任务输入、任务输出与系统提示。

**EN** 3.2 Empirical Results

**ZH** 3.2 实证结果

**EN** The evaluation results of 12 close-source and 3 open-source LLM judges in terms of repetition stability, position consistency, and preference fairness on MTBench and DevBench are listed in Table 2. For each judge, we calculate its average ⟦SLOT_47⟧, ⟦SLOT_48⟧, and ⟦SLOT_49⟧ across all candidates and tasks. For ⟦SLOT_50⟧ and ⟦SLOT_51⟧, higher values are preferable. A high ⟦SLOT_52⟧ value is particularly important as a prerequisite for meaningful computations of ⟦SLOT_53⟧ and ⟦SLOT_54⟧, ensuring the LLM judge’s choice patterns are not due to random variations. Fig. 2 (a)(b) demonstrate that position bias varies by judges and tasks significantly. Fig. 2 (c) explores the correlation between the metrics ⟦SLOT_55⟧ and ⟦SLOT_56⟧. Fig. (d) to (f) further investigate the impact of the answer quality gap on position bias. These analyses were conducted by considering all judges together on MTBench. More analyses can be found in Appendix. Sec. D.

**ZH** 表 2 列出了 12 个闭源与 3 个开源 LLM 评判者在 MTBench 与 DevBench 上关于重复稳定性、位置一致性与偏好公平性的评测结果。对每个评判者，我们计算其在所有候选与任务上的平均 ⟦SLOT_47⟧、⟦SLOT_48⟧ 与 ⟦SLOT_49⟧。对 ⟦SLOT_50⟧ 与 ⟦SLOT_51⟧ 而言，数值越高越好。较高的 ⟦SLOT_52⟧ 值尤其重要，它是有意义地计算 ⟦SLOT_53⟧ 与 ⟦SLOT_54⟧ 的前提，可确保 LLM 评判者的选择模式并非源于随机波动。图 2（a）（b）表明，位置偏差随评判者与任务而显著变化。图 2（c）探索了 ⟦SLOT_55⟧ 与 ⟦SLOT_56⟧ 两个指标之间的相关性。图（d）至（f）进一步考察答案质量差距对位置偏差的影响。这些分析是在 MTBench 上把所有评判者放在一起进行的。更多分析见附录 D 节。

**EN** Through bidirectional stepwise regression, as shown in Table 1, LLM judge series, candidate identities, and task categories significantly impact Position Consistency among all variables. Similarly, these factors also contribute significantly to Preference Fairness. Additionally, we found that average output length is a statistically significant predictor of ⟦SLOT_57⟧. This finding is not surprising, as longer outputs are generally perceived as higher quality and more preferred. Quantitative results and more discussions can be found in Appendix. Sec. E.

**ZH** 通过双向逐步回归，如表 1 所示，在所有变量中，LLM 评判者系列、候选身份与任务类别对位置一致性有显著影响；同样，这些因素对偏好公平性也有显著贡献。此外，我们发现平均输出长度是 ⟦SLOT_57⟧ 的统计显著预测变量。这一发现并不意外，因为更长的输出通常被认为质量更高、更受偏好。定量结果与更多讨论见附录 E 节。

<!-- [原子块 · table] Judge MTBench Pairwise DevBench Pairwise MTBench List-wise R ​ S RS P ​ C PC P ​ F PF Error R ​ S RS P ​ C PC P ​ F PF Error P ​ C PC P ​ F PF Error Claude-3.5-Sonnet 0.96 ± \pm 0.07 0.82 ± \pm 0.14 0 -->

**EN** Table 2: Evaluation results for Repetition Stability (⟦SLOT_58⟧), Position Consistency (⟦SLOT_59⟧), and Preference Fairness (⟦SLOT_60⟧) are presented for both pairwise and list-wise evaluation approaches, with the top 5 performances marked in bold. Errors arise from judgment failures (e.g., exceeding context window, not following output format). High error rates and low ⟦SLOT_61⟧ are marked red, rendering further evaluations invalid due to insufficient data. List-wise evaluation is conducted on four representative judges to validate scalability.

**ZH** 表 2：给出重复稳定性（⟦SLOT_58⟧）、位置一致性（⟦SLOT_59⟧）与偏好公平性（⟦SLOT_60⟧）在成对与列表式两种评测方式下的结果，前 5 名表现以粗体标记。误差来自判断失败（例如超出上下文窗口、未遵循输出格式）。高错误率与低 ⟦SLOT_61⟧ 以红色标记，表示因数据不足而使进一步评测无效。列表式评测在四个代表性评判者上进行，以验证可扩展性。

**EN** 4 Main Findings

**ZH** 4 主要发现

<!-- [原子块 · img]  -->

**EN** Figure 2: Judge performances on MTBench. Fig. (a)(b) are the radar charts for the ⟦SLOT_62⟧ comparison by family, judge, and task. Fig. (c) leverages linear regression to explore the general relationship between ⟦SLOT_63⟧ and ⟦SLOT_64⟧. Fig. (d) to (f) investigate the impact of answer quality gap on position bias using overall win rates. Fig. (a) to (e) are for pairwise comparative settings, while Fig. (f) are obtained under list-wise evaluations.

**ZH** 图 2：各评判者在 MTBench 上的表现。图（a）（b）是按家族、评判者与任务比较 ⟦SLOT_62⟧ 的雷达图。图（c）用线性回归探索 ⟦SLOT_63⟧ 与 ⟦SLOT_64⟧ 之间的总体关系。图（d）至（f）用总体胜率考察答案质量差距对位置偏差的影响。图（a）至（e）来自成对比较设置，图（f）则在列表式评估下获得。

**EN** Position Bias of Capable Judges are not Mere Random Variations: As shown in Table 2, the capable judges on the benchmark tasks, supported by minimal "Error" rates, generally exhibit ⟦SLOT_65⟧ values above 0.85. The most capable models, such as Claude-3.5-Sonnet, GPT-4, and Llama-3.3-70B, all achieve near-perfect ⟦SLOT_66⟧ scores over 0.95 on both benchmarks. These results confirm that judgments from capable LLM judges, and the resulting position bias, are not due to random variations. This strengthens confidence that one-time generated judgments by these validated LLMs accurately reflect their judging capabilities.

**ZH** 能力强评判者的位置偏差并非纯粹的随机波动：如表 2 所示，在基准任务上、且“误差”率极低的条件下，能力较强的评判者总体上表现出 0.85 以上的 ⟦SLOT_65⟧ 值。能力最强的模型，如 Claude-3.5-Sonnet、GPT-4 与 Llama-3.3-70B，在两个基准上都取得了 0.95 以上、接近完美的 ⟦SLOT_66⟧ 分数。这些结果确认，能力较强的 LLM 评判者所做出的判断以及由此产生的位置偏差并非随机波动所致。这增强了我们的信心：这些经过验证的 LLM 一次性生成的判断能准确反映其评判能力。

**EN** Position Bias Varies by Judge & Task: As shown in Fig. 2(a), position bias among LLM judges varies significantly across different judges and tasks. For instance, GPT-4o demonstrates higher position consistency when evaluating coding tasks but performs less consistently on other tasks compared to GPT-4. Similarly, Gemini-1.5-pro, while achieving higher ⟦SLOT_67⟧ than other Gemini models in most tasks, exhibits comparable consistency when judging extraction tasks. Similar findings can be observed in the DevBench results, as detailed in Appendix.Sec. D.2.

**ZH** 位置偏差随评判者与任务而异：如图 2（a）所示，LLM 评判者的位置偏差在不同评判者与不同任务之间差异显著。例如，GPT-4o 在评估编码任务时表现出更高的位置一致性，但与 GPT-4 相比在其他任务上一致性更差。类似地，Gemini-1.5-pro 虽然在多数任务上取得高于其他 Gemini 模型的 ⟦SLOT_67⟧，但在判断抽取类任务时表现出相当的一致性。在 DevBench 结果中也可观察到类似发现，详见附录 D.2 节。

**EN** Variations in preference fairness are also evident. As shown in Table 2, GPT-4 and GPT-3.5-Turbo display different preference biases across datasets and tasks—being recency-preferred on MTBench but primacy-preferred on DevBench. Likewise, Claude-3.5-Sonnet, which is nearly preference-fair on MTBench (⟦SLOT_68⟧), exhibits a strong recency-preferred position bias on DevBench (⟦SLOT_69⟧).

**ZH** 偏好公平性的差异同样明显。如表 2 所示，GPT-4 与 GPT-3.5-Turbo 在不同数据集与任务上表现出不同的偏好偏差——在 MTBench 上偏好末位，而在 DevBench 上偏好首位。同样，Claude-3.5-Sonnet 在 MTBench 上几乎偏好公平（⟦SLOT_68⟧），在 DevBench 上却表现出强烈的偏好末位的位置偏差（⟦SLOT_69⟧）。

**EN** While higher position consistency generally correlates with improved preference fairness (as demonstrated by the regression curve in Fig. 2(c)), consistency alone does not guarantee fairness. Certain LLM judges, despite achieving high ⟦SLOT_70⟧, still exhibit significant and varied preference directions across different tasks, underscoring the need to evaluate both consistency and fairness when assessing LLM judges.

**ZH** 虽然更高的位置一致性通常与更好的偏好公平性相关（如图 2（c）中的回归曲线所示），但仅有一致性并不能保证公平。某些 LLM 评判者尽管取得了较高的 ⟦SLOT_70⟧，在不同任务上仍表现出显著且各异的偏好方向，这说明在评估 LLM 评判者时需要同时考察一致性与公平性。

**EN** In list-wise comparisons, similar variations in position bias were observed across judges and tasks. Furthermore, Table 2 highlights that more capable models, such as GPT-4o and Claude-3.5-Sonnet, maintain high consistency when transitioning from pairwise to list-wise evaluations, while less capable models, such as GPT-3.5-Turbo, exhibit greater sensitivity to the increased number of candidates in list-wise tasks.

**ZH** 在列表式比较中，同样观察到位置偏差随评判者与任务而异。此外，表 2 显示，能力更强的模型（如 GPT-4o 与 Claude-3.5-Sonnet）在从成对评估转向列表式评估时仍保持较高的一致性，而能力较弱的模型（如 GPT-3.5-Turbo）则对列表式任务中候选数量增加表现出更强的敏感性。

**EN** Therefore, the position bias of LLM judges is both judge-dependent and task-dependent. This observation is further confirmed by the bidirectional stepwise regression where judge identities and task categories are statistically significant predictors of ⟦SLOT_71⟧ and ⟦SLOT_72⟧. In practice, when evaluating LLM judge’s reliability or selecting suitable LLM judges, considering the balance between consistency and fairness, as well as accounting for task-specific variations, may be beneficial.

**ZH** 因此，LLM 评判者的位置偏差既依赖评判者，也依赖任务。双向逐步回归进一步确认了这一观察：评判者身份与任务类别是 ⟦SLOT_71⟧ 与 ⟦SLOT_72⟧ 的统计显著预测变量。在实践中，评估 LLM 评判者的可靠性或挑选合适的 LLM 评判者时，考虑一致性与公平性之间的平衡，并顾及任务特有的差异，可能是有益的。

**EN** Position Bias Correlates to Answer Quality Gap: Intuitively, the difficulty of judging a pair of candidate answers is largely reflected by their difference in quality. In this study, as defined in Section 2.3, we quantify the quality gap (⟦SLOT_73⟧) between candidate solutions and expected baseline (calculated by ⟦SLOT_74⟧ for a ⟦SLOT_75⟧-candidate list) by the overall win rate (⟦SLOT_76⟧). Therefore, ⟦SLOT_77⟧ increases as ⟦SLOT_78⟧ extends from baseline to 0 or 1. Fig. 2 (e) and (f) exhibit significant parabolic shapes, indicating that ⟦SLOT_79⟧ is positively proportional to ⟦SLOT_80⟧. This aligns with our intuition that the answer pairs or series with larger quality disparities are easier to achieve judgment consistency, whereas those of similar quality are difficult to judge, increasing the likelihood of position bias that leads to lower ⟦SLOT_81⟧. The same relationship is observed for each individual judge and across benchmarks, as demonstrated in Appendix.Sec. D.

**ZH** 位置偏差与答案质量差距相关：直观上，判断一对候选答案的难度在很大程度上反映为二者质量上的差异。在本研究中，如 2.3 节所定义，我们量化候选方案与期望基线之间的质量差距（⟦SLOT_73⟧），它由 ⟦SLOT_74⟧ 针对含 ⟦SLOT_75⟧ 个候选的列表计算得到，所用度量为总体胜率（⟦SLOT_76⟧）。因此，⟦SLOT_77⟧ 随 ⟦SLOT_78⟧ 从基线向 0 或 1 延伸而增大。图 2（e）与（f）呈现显著的抛物线形状，表明 ⟦SLOT_79⟧ 与 ⟦SLOT_80⟧ 成正比。这与我们的直觉一致：质量差距更大的答案对或答案序列更容易达成判断一致，而质量相近的那些则更难判断，从而增加了出现位置偏差、进而降低 ⟦SLOT_81⟧ 的可能性。对每个单独的评判者以及跨基准都可以观察到同样的关系，如附录 D 节所示。

**EN** Similarly, as shown in Fig. 2 (d), judgments generally become more preference fair as ⟦SLOT_82⟧ increases. However, the extent is not as significant as for ⟦SLOT_83⟧. Also, the relationship varies by judge, as some LLMs maintain preference fairness regardless of ⟦SLOT_84⟧. For example, as shown in Appendix.Fig. 5, ⟦SLOT_85⟧ of GPT models centered closely around 0 consistently, whereas that of Claude and Gemini-pro models exhibit a conspicuous proportional relationship on MTBench. These observations align with the right-arrow shape as demonstrated in Fig. 2 (c), where there is a general trend that judgments become preference fairer as position consistency increases. It also justifies the reasonableness of our quantification of preference fairness, as highly position consistent judges are not overly penalized and a perfect ⟦SLOT_86⟧ should result in ⟦SLOT_87⟧.

**ZH** 类似地，如图 2（d）所示，随着 ⟦SLOT_82⟧ 增大，判断总体上变得更偏好公平，但程度不如 ⟦SLOT_83⟧ 那样显著。而且这一关系随评判者而异，因为某些 LLM 无论 ⟦SLOT_84⟧ 如何都保持偏好公平。例如，如附录图 5 所示，GPT 系列模型的 ⟦SLOT_85⟧ 始终紧密围绕 0，而 Claude 与 Gemini-pro 系列模型在 MTBench 上则呈现明显的比例关系。这些观察与图 2（c）中展示的右箭头形状一致：总体上存在一个趋势，即随着位置一致性提高，判断变得更偏好公平。这也印证了我们对偏好公平性的量化是合理的——位置高度一致的评判者不会受到过度惩罚，而完美的 ⟦SLOT_86⟧ 应当对应 ⟦SLOT_87⟧。

**EN** Together, we conclude that as the answer quality gap enlarges, judges generally become more position consistent and preference fair according to the regression curves. However, exceptions are common, as shown by the individual scatter points of these figures. This indicates that though the answer quality gap significantly influences the position bias of LLM judges, other factors also play important roles. Therefore, built on our findings, future studies may have better control over the answer quality gap when evaluating LLM judges, exploring other impacting factors on position bias, and seeking potential mitigation strategies.

**ZH** 综上我们得出结论：随着答案质量差距扩大，依据回归曲线，评判者总体上变得更位置一致、更偏好公平。但例外情况很常见，正如这些图中分散的单个数据点所示。这说明，尽管答案质量差距显著影响 LLM 评判者的位置偏差，其他因素同样发挥着重要作用。因此，在我们的发现之上，未来研究在评估 LLM 评判者时或可更好地控制答案质量差距，探索影响位置偏差的其他因素，并寻求潜在的缓解策略。

**EN** Position Bias is weakly Length-dependent We investigate the impact of three different lengths on the position bias of LLM judges: the length of the question (task input length), the solution length of candidate models (task output length), and the length of the entire prompt (prompt length). By stepwise regression, we discovered that average task output length is only significant in predicting ⟦SLOT_88⟧, adding a minimal change in AIC as shown in Appendix Table. 4. In other words, there is a very weak relationship between the lengths of prompt components and position bias.

**ZH** 位置偏差对长度的依赖很弱。我们考察了三种不同长度对 LLM 评判者位置偏差的影响：问题的长度（任务输入长度）、候选模型方案的长度（任务输出长度），以及整个提示的长度（提示长度）。通过逐步回归我们发现，平均任务输出长度仅在预测 ⟦SLOT_88⟧ 时显著，且如附录表 4 所示只带来极小的 AIC 变化。换言之，提示组成部分的长度与位置偏差之间的关系非常微弱。

**EN** LLM Agreement Analysis: We complement our investigation of position bias with an agreement and disagreement analysis among LLM judges. Rather than focusing exclusively on overall consistency or fairness, we examine how LLM judges converge and diverge in their assessments of individual instances. Agreement analysis quantifies the percentage of instances where two LLM judges mutually agree on the outcome. Disagreement analysis counts the number of choices deviating from the mode for each instance among all judges. This further complies a “distribution of disagreement” across the dataset.

**ZH** LLM 一致性分析：我们通过对 LLM 评判者之间的一致与分歧分析，补充了对位置偏差的考察。我们不只关注总体的一致性或公平性，还检视 LLM 评判者在单个实例的评估上如何趋同与分化。一致性分析量化两个 LLM 评判者在结果上相互一致的实例所占百分比；分歧分析统计每个实例上所有评判者中偏离众数的选择数量。这进一步构成了数据集上的“分歧分布”。

**EN** Our findings reveal that, despite exhibiting similar overall ⟦SLOT_89⟧ and ⟦SLOT_90⟧ scores, judges vary significantly in their judgments on individual instance. Disagreement analysis, in particular, highlights instances where consensus is either easily or difficultly achieved, reflecting the inherent complexity of the judgment task. For example, as shown in Fig. 3, more than half of the dataset can be considered relatively easy to judge, as over 80% of all 15 LLM judges agree with each other on these instances (disagreement ⟦SLOT_91⟧ 3). Conversely, fewer than 2% of instances represent the likely especially-hard-to-judge cases where a majority of LLM judges fail to reach consensus (disagreement ⟦SLOT_92⟧ 8).

**ZH** 我们的发现表明，尽管总体 ⟦SLOT_89⟧ 与 ⟦SLOT_90⟧ 分数相近，各评判者在单个实例上的判断差异显著。分歧分析尤其凸显出那些容易或难以达成共识的实例，反映出判断任务固有的复杂性。例如，如图 3 所示，数据集中超过一半可以认为相对容易判断，因为全部 15 个 LLM 评判者中有超过 80% 在这些实例上彼此一致（分歧度 ⟦SLOT_91⟧ 3）。相反，只有不到 2% 的实例属于可能特别难以判断的情形，其中多数 LLM 评判者未能达成共识（分歧度 ⟦SLOT_92⟧ 8）。

<!-- [原子块 · object]  -->

**EN** Figure 3: Distribution of disagreement on MTBench. The y-axis indicates the proportion of the dataset where the level of disagreement among LLM judges does not exceed a specific threshold.

**ZH** 图 3：MTBench 上的分歧分布。纵轴表示数据集中 LLM 评判者之间分歧程度不超过某一阈值的实例比例。

**EN** Based on our observations of answer quality gaps and LLM agreement/disagreement patterns, this study offers practical insights for designing evaluator benchmarks that account for the varying difficulty levels of judgment tasks. Specifically, the most challenging instances to evaluate are characterized by: (1) frequent disagreements among LLM judges, (2) closely matched win rates and minimal quality gaps among candidate models, and (3) significant position bias exhibited by the majority of LLM judges. Further discussions and analyses can be found in Appendix Sec. C.

**ZH** 基于我们对答案质量差距以及 LLM 一致与分歧模式的观察，本研究为设计考虑判断任务难度差异的评测基准提供了实践启示。具体而言，最难评估的实例具有以下特征：（1）LLM 评判者之间频繁出现分歧；（2）候选模型之间胜率接近、质量差距极小；（3）多数 LLM 评判者表现出显著的位置偏差。更多讨论与分析见附录 C 节。

**EN** 5 Conclusion

**ZH** 5 结论

**EN** In conclusion, this paper provides an in-depth analysis of position bias in LLM judges, a critical challenge in automated evaluation. Using metrics such as repetition stability, position consistency, and preference fairness, we identify significant variations in position bias across judges and tasks, consistent across pairwise and list-wise comparison settings. Our findings show that position bias is weakly influenced by prompt length but strongly impacted by the quality gap between solutions. Furthermore, agreement and disagreement analysis highlights variability in judgment reliability, providing valuable insights for refining benchmarks. This study enhances understanding of position bias and contributes to the development of fairer and more reliable LLM evaluation frameworks.

**ZH** 总之，本文对 LLM 评判者中的位置偏差——自动评测中的一项关键挑战——做了深入分析。借助重复稳定性、位置一致性与偏好公平性等指标，我们识别出位置偏差在评判者与任务之间存在显著差异，且在成对与列表式比较设置下表现一致。我们的发现表明，位置偏差受提示长度的影响很弱，但受方案之间质量差距的影响很强。此外，一致与分歧分析凸显了判断可靠性上的变异，为改进基准提供了有价值的洞察。本研究加深了对位置偏差的理解，并有助于构建更公平、更可靠的 LLM 评测框架。

**EN** 6 Limitations

**ZH** 6 局限

**EN** Despite proposing scalable metrics and investigating key factors influencing position bias, our study has several limitations.

**ZH** 尽管我们提出了可扩展的指标并考察了影响位置偏差的关键因素，本研究仍有若干局限。

**EN** First, we evaluated only 12 commercial closed-source LLM judges for pairwise settings and 4 for list-wise paradigms across two benchmarks, limiting the list-wise comparisons to three-candidate lists. Among open-source models, we assessed only three Llama 3.1+ models of varying sizes, as earlier versions or other smaller models lacked sufficient context window lengths, making them unsuitable given the length of evaluation instances in our study. Additionally, while we used original benchmark prompt templates, exploring alternative prompting techniques could offer further insights. Future work could expand on this by incorporating more models, tasks, prompting strategies, and larger list-wise candidate pools to enhance the generalizability of our findings.

**ZH** 首先，我们在成对设置下只评估了 12 个商用闭源 LLM 评判者，在列表式范式下只评估了 4 个，且跨两个基准，并把列表式比较限制为三候选列表。在开源模型中，我们只评估了三个规模各异的 Llama 3.1+ 模型，因为更早的版本或其他更小的模型缺乏足够的上下文窗口长度，鉴于本研究中评测实例的长度而不适用。此外，虽然我们使用了原始基准的提示模板，探索替代性提示技术可能带来更多洞察。未来工作可在此基础上纳入更多模型、任务、提示策略以及更大的列表式候选池，以提升我们发现的可泛化性。

**EN** Second, data accessibility limitations prevented a direct analysis of Judge-level factors like architecture and parameter size of closed-source models. Instead, we approximated these factors by grouping models by family properties. While open-source models offer accessible architectural details for deeper analysis, our assessment of only three Llama models may not provide sufficient evidence for broader conclusions. Additionally, our analyses were conducted post hoc, relying on completed judgments before analysis. Future work could explore methods to estimate or control these factors pre-judgment, reducing computational costs and enabling proactive mitigation strategies.

**ZH** 其次，数据可得性的限制使我们无法直接分析闭源模型的架构与参数规模等评判者层面因素，转而通过按家族属性对模型分组来近似这些因素。虽然开源模型提供了可访问的架构细节以支持更深入的分析，但我们只评估了三个 Llama 模型，可能不足以支撑更广泛的结论。此外，我们的分析是事后进行的，依赖于分析之前已完成的判断。未来工作可探索在判断之前估计或控制这些因素的方法，以降低计算成本并实现主动的缓解策略。

**EN** Lastly, our focus was on evaluating and understanding position bias rather than mitigating it. While our findings provide a foundation for effective mitigation, further research is needed to address issues like maintaining consistency and fairness when answer quality gaps are minimal, where position bias is most pronounced. Multivariate analyses exploring interactions between factors like prompt length, task complexity, and answer quality gaps could also yield deeper insights and enhance mitigation approaches.

**ZH** 最后，我们的重心是评估与理解位置偏差，而非缓解它。虽然我们的发现为有效缓解奠定了基础，但仍需更多研究来应对这类问题：当答案质量差距极小时——位置偏差最突出之处——如何保持一致性与公平性。探索提示长度、任务复杂度与答案质量差距等因素之间交互作用的多变量分析，也可能带来更深入的洞察并改进缓解方法。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] Anthropic (2024) Anthropic. 2024. The claude 3 model family: Opus, sonnet, haiku . -->

<!-- [原子块 · verbatim] Chen et al. (2024) Dongping Chen, Ruoxi Chen, Shilin Zhang, Yinuo Liu, Yaochen Wang, Huichi Zhou, Qihui Zhang, Pan Zhou, Yao Wan, and Lichao Sun. 2024. Mllm-as-a-judge: Assessing multimodal llm-as-a-j -->

<!-- [原子块 · verbatim] Chiang and Lee (2023a) Cheng-Han Chiang and Hung-yi Lee. 2023a. Can large language models be an alternative to human evaluations? In Proceedings of the 61st Annual Meeting of the Association for Compu -->

<!-- [原子块 · verbatim] Chiang and Lee (2023b) Cheng-Han Chiang and Hung-Yi Lee. 2023b. Can large language models be an alternative to human evaluations? In Proceedings of the 61st Annual Meeting of the Association for Compu -->

<!-- [原子块 · verbatim] Chua et al. (2024) James Chua, Edward Rees, Hunar Batra, Samuel R. Bowman, Julian Michael, Ethan Perez, and Miles Turpin. 2024. Bias-augmented consistency training reduces biased reasoning in chain-of -->

<!-- [原子块 · verbatim] Gallegos et al. (2024) Isabel O Gallegos, Ryan A Rossi, Joe Barrow, Md Mehrab Tanjim, Sungchul Kim, Franck Dernoncourt, Tong Yu, Ruiyi Zhang, and Nesreen K Ahmed. 2024. Bias and fairness in large lang -->

<!-- [原子块 · verbatim] Gemini Team (2024) Google Gemini Team. 2024. Gemini: A family of highly capable multimodal models . Preprint , arXiv:2312.11805. -->

<!-- [原子块 · verbatim] Guo et al. (2024) Yufei Guo, Muzhe Guo, Juntao Su, Zhou Yang, Mengqiu Zhu, Hongfei Li, Mengyang Qiu, and Shuo Shuo Liu. 2024. Bias in large language models: Origin, evaluation, and mitigation. arXiv p -->

<!-- [原子块 · verbatim] Hou et al. (2024) Yupeng Hou, Junjie Zhang, Zihan Lin, Hongyu Lu, Ruobing Xie, Julian McAuley, and Wayne Xin Zhao. 2024. Large language models are zero-shot rankers for recommender systems. In Europea -->

<!-- [原子块 · verbatim] Karpinska et al. (2021) Marzena Karpinska, Nader Akoury, and Mohit Iyyer. 2021. The perils of using mechanical turk to evaluate open-ended text generation. In Proceedings of the 2021 Conference on Emp -->

<!-- [原子块 · verbatim] Khan et al. (2024) Akbir Khan, John Hughes, Dan Valentine, Laura Ruis, Kshitij Sachan, Ansh Radhakrishnan, Edward Grefenstette, Samuel R Bowman, Tim Rocktäschel, and Ethan Perez. 2024. Debating with m -->

<!-- [原子块 · verbatim] Kocmi and Federmann (2023) Tom Kocmi and Christian Federmann. 2023. Large language models are state-of-the-art evaluators of translation quality . In Proceedings of the 24th Annual Conference of the E -->

<!-- [原子块 · verbatim] Li et al. (2024a) Bowen Li, Wenhan Wu, Ziwei Tang, Lin Shi, John Yang, Jinyang Li, Shunyu Yao, Chen Qian, Binyuan Hui, Qicheng Zhang, et al. 2024a. Devbench: A comprehensive benchmark for software dev -->

<!-- [原子块 · verbatim] Li et al. (2023a) Chengzu Li, Han Zhou, Goran Glavaš, Anna Korhonen, and Ivan Vulić. 2023a. On task performance and model calibration with supervised and self-ensembled in-context learning . Preprint  -->

<!-- [原子块 · verbatim] Li et al. (2023b) Junlong Li, Shichao Sun, Weizhe Yuan, Run-Ze Fan, Pengfei Liu, et al. 2023b. Generative judge for evaluating alignment. In The Twelfth International Conference on Learning Representa -->

<!-- [原子块 · verbatim] Li et al. (2023c) Ruosen Li, Teerth Patel, and Xinya Du. 2023c. Prd: Peer rank and discussion improve large language model based evaluations. arXiv preprint arXiv:2307.02762 . -->

<!-- [原子块 · verbatim] Li et al. (2023d) Zongjie Li, Chaozheng Wang, Pingchuan Ma, Daoyuan Wu, Shuai Wang, Cuiyun Gao, and Yang Liu. 2023d. Split and merge: Aligning position biases in large language model based evaluators. -->

<!-- [原子块 · verbatim] Li et al. (2024b) Zongjie Li, Chaozheng Wang, Pingchuan Ma, Daoyuan Wu, Shuai Wang, Cuiyun Gao, and Yang Liu. 2024b. Split and merge: Aligning position biases in llm-based evaluators. In Proceedings o -->

<!-- [原子块 · verbatim] Liu et al. (2024) Yinhong Liu, Han Zhou, Zhijiang Guo, Ehsan Shareghi, Ivan Vulić, Anna Korhonen, and Nigel Collier. 2024. Aligning with human judgement: The role of pairwise preference in large langu -->

<!-- [原子块 · verbatim] Liusie et al. (2024) Adian Liusie, Potsawee Manakul, and Mark Gales. 2024. Llm comparative assessment: Zero-shot nlg evaluation through pairwise comparisons using large language models. In Proceedings -->

<!-- [原子块 · verbatim] Ohi et al. (2024) Masanari Ohi, Masahiro Kaneko, Ryuto Koike, Mengsay Loem, and Naoaki Okazaki. 2024. Likelihood-based mitigation of evaluation bias in large language models. arXiv preprint arXiv:2402 -->

<!-- [原子块 · verbatim] OpenAI (2023) OpenAI(2023). 2024. Gpt-4 technical report . Preprint , arXiv:2303.08774. -->

<!-- [原子块 · verbatim] Qin et al. (2024) Zhen Qin, Rolf Jagerman, Kai Hui, Honglei Zhuang, Junru Wu, Le Yan, Jiaming Shen, Tianqi Liu, Jialu Liu, Donald Metzler, Xuanhui Wang, and Michael Bendersky. 2024. Large language mod -->

<!-- [原子块 · verbatim] Raina et al. (2024) Vyas Raina, Adian Liusie, and Mark Gales. 2024. Is llm-as-a-judge robust? investigating universal adversarial attacks on zero-shot llm assessment . Preprint , arXiv:2402.14016. -->

<!-- [原子块 · verbatim] Touvron et al. (2023) Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, Aurelien Rodriguez -->

<!-- [原子块 · verbatim] Wang et al. (2023) Peiyi Wang, Lei Li, Liang Chen, Zefan Cai, Dawei Zhu, Binghuai Lin, Yunbo Cao, Qi Liu, Tianyu Liu, and Zhifang Sui. 2023. Large language models are not fair evaluators . Preprint ,  -->

<!-- [原子块 · verbatim] Wang et al. (2025) Ziqi Wang, Hanlin Zhang, Xiner Li, Kuan-Hao Huang, Chi Han, Shuiwang Ji, Sham M. Kakade, Hao Peng, and Heng Ji. 2025. Eliminating position bias of language models: A mechanistic app -->

<!-- [原子块 · verbatim] Wei et al. (2022) Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al. 2022. Chain-of-thought prompting elicits reasoning in large language models. Ad -->

<!-- [原子块 · verbatim] Yu et al. (2025) Yijiong Yu, Huiqiang Jiang, Xufang Luo, Qianhui Wu, Chin-Yew Lin, Dongsheng Li, Yuqing Yang, Yongfeng Huang, and Lili Qiu. 2025. Mitigate position bias in large language models via sc -->

<!-- [原子块 · verbatim] Zeng et al. (2023) Zhiyuan Zeng, Jiatong Yu, Tianyu Gao, Yu Meng, Tanya Goyal, and Danqi Chen. 2023. Evaluating large language models at evaluating instruction following. In The Twelfth International  -->

<!-- [原子块 · verbatim] Zheng et al. (2024a) Chujie Zheng, Hao Zhou, Fandong Meng, Jie Zhou, and Minlie Huang. 2024a. Large language models are not robust multiple choice selectors . Preprint , arXiv:2309.03882. -->

<!-- [原子块 · verbatim] Zheng et al. (2024b) Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric Xing, et al. 2024b. Judging llm-as-a-judge with mt-benc -->

<!-- [原子块 · verbatim] Zhou et al. (2024) Han Zhou, Xingchen Wan, Lev Proleev, Diana Mincu, Jilin Chen, Katherine A Heller, and Subhrajit Roy. 2024. Batch calibration: Rethinking calibration for in-context learning and prom -->

<!-- [原子块 · verbatim] Zhu et al. (2023) Lianghui Zhu, Xinggang Wang, and Xinlong Wang. 2023. Judgelm: Fine-tuned large language models are scalable judges. arXiv preprint arXiv:2310.17631 . -->

**EN** Appendix Table of Contents

**ZH** 附录目录

**EN** Appendix A Reproducibility

**ZH** 附录 A 可复现性

**EN** Our experiments were conducted primarily using API access, with a total cost of approximately 3,000 USD. The code repository for reproducing our results is available:https://anonymous.4open.science/r/Position-Bias-Analyzer-Demo-F7E3

**ZH** 我们的实验主要通过 API 访问进行，总花费约 3,000 美元。用于复现我们结果的代码仓库见：https://anonymous.4open.science/r/Position-Bias-Analyzer-Demo-F7E3

**EN** Appendix B Related Work

**ZH** 附录 B 相关工作

**EN** B.1 LLM-as-a-Judge

**ZH** B.1 LLM-as-a-Judge

**EN** Large Language Models (LLMs) have become a transformative tool in automating evaluative tasks, offering scalability and reproducibility advantages over human assessments. The methodology of using LLMs as evaluators ("LLM-as-a-Judge") has been widely used for tasks such as open-ended story generation (Chiang and Lee 2023a), adversarial attacks (Chiang and Lee 2023b), summarization (Karpinska et al. 2021), machine translation (Kocmi and Federmann 2023), and instruction following (Zeng et al. 2023), where models are tasked with scoring or ranking outputs. Despite their potential, inherent biases—particularly position bias—pose significant challenges to their reliability and fairness, even in the most effective pairwise comparative settings.

**ZH** 大语言模型（LLM）已成为自动化评估任务中的变革性工具，相较人工评估具备可扩展性与可复现性的优势。把 LLM 用作评估器的方法（LLM-as-a-Judge）已广泛用于开放式故事生成（Chiang 和 Lee 2023a）、对抗攻击（Chiang 和 Lee 2023b）、摘要（Karpinska 等 2021）、机器翻译（Kocmi 和 Federmann 2023）与指令遵循（Zeng 等 2023）等任务，其中模型被要求为输出打分或排序。尽管潜力可观，固有偏差——尤其是位置偏差——即便在最有效的成对比较设置下，也对其可靠性与公平性构成重大挑战。

**EN** B.2 Position Bias

**ZH** B.2 位置偏差

**EN** However, position bias is a complex problem that is challenging to deal with or solve. The naive way is to exclude the position inconsistent judgments, which does not solve the fundamental issue and would likely result in data sparsity when position bias is frequently exhibited. Therefore, researchers proposed ‘inconsistency-as-a-tie’ for both models in pairwise comparative settings to consider all judgments for further analysis (Zheng et al. 2024b; Li et al. 2023c). This approach, while practically useful for evaluations, does not mitigate position bias.

**ZH** 然而，位置偏差是一个难以处理或解决的复杂问题。最朴素的做法是剔除位置不一致的判断，这并未解决根本问题，而且在位置偏差频繁出现时很可能导致数据稀疏。因此，研究者针对成对比较设置中的两个模型提出了“不一致即平局”的做法，以便把所有判断都纳入后续分析（Zheng 等 2024b；Li 等 2023c）。这一做法虽在评测中实用，却并未缓解位置偏差。

**EN** Given the significance of position bias, researchers have developed more sophisticated approaches to mitigate it, including bootstrapping (Hou et al. 2024), split-and-merge techniques (Li et al. 2023d), and multi-agent discussions (Li et al. 2023c; Khan et al. 2024). While these methods demonstrate potential, they are often costly, time-consuming, or insufficient. For example, multi-agent discussions and iterative reviews require extensive computational resources and human-like deliberation, while simpler techniques, such as order permutation (Wang et al. 2023; Zheng et al. 2024a) and batch calibration (Zhou et al. 2024), have limited effectiveness in addressing bias holistically. Furthermore, calibration methods like ensembling (Li et al. 2023a) or context decomposition (Li et al. 2023d) are often constrained by the inadequacy of supervised data to align LLM evaluators effectively (Liu et al. 2024). This highlights that addressing this crucial bias is complex and challenging.

**ZH** 鉴于位置偏差的重要性，研究者开发了更复杂的方法来缓解它，包括自助法（Hou 等 2024）、拆分合并技术（Li 等 2023d）与多智能体讨论（Li 等 2023c；Khan 等 2024）。这些方法虽展现出潜力，但往往代价高昂、耗时，或效果不足。例如，多智能体讨论与迭代评审需要大量计算资源和类似人类的审慎斟酌，而顺序置换（Wang 等 2023；Zheng 等 2024a）与批量校准（Zhou 等 2024）等较简单技术在整体解决偏差上效果有限。此外，集成（Li 等 2023a）或上下文分解（Li 等 2023d）等校准方法，常因缺乏足够的监督数据来有效对齐 LLM 评估器而受限（Liu 等 2024）。这说明，应对这一关键偏差既复杂又具挑战性。

**EN** The limitations of existing approaches underscore a critical gap in our understanding of position bias itself. A lack of clarity on the factors influencing this bias and their quantitative impacts hampers the development of effective solutions. For instance, while the PORTIA approach (Li et al. 2023d) demonstrates significant improvements in consistency for GPT-4 (from 93.44% to 97.03%), this success may be overestimated due to the selection of tasks with large answer quality gaps. As our study reveals, such gaps inherently reduce the likelihood of position bias, making these cases easier to calibrate. This example underscores the necessity of first comprehensively understanding the underlying factors contributing to position bias before proposing or refining mitigation strategies. Without this foundational understanding, the efficacy of current and future methods remains uncertain and potentially misjudged.

**ZH** 现有方法的局限凸显出我们在对位置偏差本身的理解上存在关键缺口。对影响该偏差的因素及其量化影响缺乏清晰认识，妨碍了有效解决方案的开发。例如，PORTIA 方法（Li 等 2023d）在 GPT-4 的一致性上展现出显著改进（从 93.44% 提升到 97.03%），但由于所选任务的答案质量差距较大，这一成功可能被高估。正如我们的研究揭示的，这类差距本身会降低位置偏差出现的可能性，使这些案例更容易校准。这个例子说明，在提出或改进缓解策略之前，必须先全面理解导致位置偏差的深层因素。缺少这一基础性理解，当前与未来方法的有效性就始终不确定，并可能被误判。

**EN** B.3 Research Gaps

**ZH** B.3 研究缺口

**EN** To enhance the understanding of position bias, our study builds on and extends prior work through the following dimensions.

**ZH** 为增进对位置偏差的理解，我们的研究在以下维度上继承并扩展了前人工作。

**EN** Repetition Stability: Previous studies on LLM-as-a-Judge often implicitly assume that single-instance judgments are sufficient to reflect the evaluating capabilities of judge models, thereby attributing observed biases entirely to systematic tendencies rather than random variations. These studies typically proceed directly to analyses on position bias or others without such verification. However, if judgments vary by chance or lack consistency across repetitions, the reliability and accuracy of downstream analyses are compromised. To avoid this issue, Chen et al. 2024 repeated evaluations multiple times and adopted the mode judgment as the representative, an approach that, while effective, is computationally expensive. Addressing this gap, our work introduces a method or metric for systematically evaluating the stability of LLM judgments across repetitions. This ensures that observed biases are systematic rather than artifacts of variability. By performing this validation on a sample dataset for cost-efficiency, researchers can establish a robust foundation for subsequent evaluations and analyses, ensuring the reliability of their conclusions.

**ZH** 重复稳定性：此前关于 LLM-as-a-Judge 的研究通常隐含地假设单次判断足以反映评判模型的评估能力，从而把观察到的偏差完全归因于系统性倾向而非随机波动。这些研究往往直接推进到对位置偏差或其他偏差的分析，而不做此类验证。然而，如果判断因偶然而变化，或在重复之间缺乏一致性，下游分析的可靠性与准确性就会受损。为避免这一问题，Chen 等 2024 多次重复评估并采用众数判断作为代表，这一做法虽有效但计算代价高昂。为填补这一缺口，我们的工作引入了一种系统评估 LLM 判断在重复之间稳定性的方法或指标，确保观察到的偏差是系统性的，而非变异性的产物。通过在样本数据集上做这一验证以节省成本，研究者可以为后续评估与分析奠定稳健基础，确保其结论的可靠性。

**EN** Preference Fairness: Prior studies on position bias often focus on the proportion of position consistent judgments, referred to as “position consistency”. Only a few have explored the preference directions of LLM evaluators in addition to consistency. However, traditional measurements either overly penalize highly consistent judges (Li et al. 2023c; Liusie et al. 2024) or rely on metrics whose sensitivity is highly dependent on dataset size (Zheng et al. 2024b; Zhu et al. 2023). To address these limitations, we proposed a refined metric, preference fairness (⟦SLOT_93⟧), which integrates the strengths of both approaches. This single, comprehensive metric ensures sensitivity across datasets, remains independent of the number of questions and tasks, and represents a significant improvement over previous metrics.

**ZH** 偏好公平性：此前关于位置偏差的研究通常关注位置一致判断所占的比例，即“位置一致性”，只有少数在一致性之外还考察了 LLM 评估器的偏好方向。然而，传统的度量要么对高度一致的评判者过度惩罚（Li 等 2023c；Liusie 等 2024），要么依赖敏感度高度取决于数据集规模的指标（Zheng 等 2024b；Zhu 等 2023）。为解决这些局限，我们提出了一种改进的指标——偏好公平性（⟦SLOT_93⟧），它兼取两种方法的长处。这一单一而综合的指标确保了跨数据集的敏感度，不受问题数与任务数影响，相较此前的指标有显著改进。

**EN** Answer Quality Gap: Intuitively, candidate solutions with significant quality disparities are easier to judge, likely resulting in reduced position bias. This suggests that the quality gap among answers is a potentially significant factor influencing position bias. However, this factor has been largely overlooked in prior works, both in evaluations and in the development of mitigation strategies, underscoring our limited understanding of position bias. While Wang et al. 2023 explored the answer quality gap in score-based LLM-as-a-Judge evaluations using judgment scores, quantifying this variable in comparative settings (pairwise or list-wise) remains an open research problem. To address this gap, we propose the use of win rates (Zheng et al. 2024b) of candidate solutions against an expected baseline to measure the answer quality gap. This approach offers a practical quantitative metric for subsequent analysis and deepens our understanding of the factors driving position bias.

**ZH** 答案质量差距：直观上，质量差距显著的候选方案更容易判断，很可能带来更少的位置偏差。这说明答案之间的质量差距可能是影响位置偏差的一个重要因素。然而，无论是在评测中还是在缓解策略的开发中，这一因素在前人工作中都被大量忽视，反映出我们对位置偏差的理解有限。虽然 Wang 等 2023 利用判断分数在基于打分的 LLM-as-a-Judge 评测中探索了答案质量差距，但在比较式设置（成对或列表式）下量化这一变量仍是一个开放的研究问题。为填补这一缺口，我们提出用候选方案相对于期望基线的胜率（Zheng 等 2024b）来度量答案质量差距。这一做法为后续分析提供了实用的量化指标，并深化了我们对驱动位置偏差的因素的理解。

**EN** List-wise Evaluations: Although LLM-as-a-Judge has been categorized into pointwise, pairwise, and list-wise paradigms (Qin et al. 2024), most research has focused on pairwise comparative assessments due to their demonstrated effectiveness (Zheng et al. 2024b; Liusie et al. 2024). However, this leaves a significant gap in measuring and understanding the position bias in list-wise settings, where LLMs are prompted to evaluate three or more candidate solutions simultaneously. With advancements in model capabilities, list-wise evaluations present a potentially more cost-effective alternative to pairwise approaches, requiring fewer comparisons while maintaining consistency and fairness. Our work bridges this gap by extending position bias assessments from pairwise to list-wise settings, enabling a more comprehensive evaluation of LLM-as-a-Judge across varied configurations.

**ZH** 列表式评估：尽管 LLM-as-a-Judge 已被划分为逐点式、成对式与列表式三种范式（Qin 等 2024），多数研究因成对比较的有效性已得到验证而聚焦于它（Zheng 等 2024b；Liusie 等 2024）。然而，这在度量与理解列表式设置下的位置偏差上留下了显著缺口——在列表式设置中，LLM 被提示同时评估三个或更多候选方案。随着模型能力的提升，列表式评估成为比成对方式更具成本效益的潜在替代：它需要更少的比较次数，同时保持一致性与公平性。我们的工作通过把位置偏差的评估从成对设置扩展到列表式设置，弥合了这一缺口，从而支持跨多种配置对 LLM-as-a-Judge 做更全面的评测。

**EN** These identified gaps - spanning from the validation of judgments to the evaluation of list-wise settings - highlight the need for a more comprehensive framework to evaluate and understand position bias. By addressing these dimensions collectively, our work provides a foundation for a deeper understanding of the consistency, fairness, and reliability of LLM evaluators.

**ZH** 这些被识别出的缺口——从判断的验证到列表式设置的评测——凸显出需要一个更全面的框架来评估与理解位置偏差。通过整体性地应对这些维度，我们的工作为更深入理解 LLM 评估器的一致性、公平性与可靠性奠定了基础。

**EN** Appendix C LLM Agreement Analysis

**ZH** 附录 C LLM 一致性分析

**EN** Besides the exploration of position bias with a broad lens by average ⟦SLOT_94⟧ and ⟦SLOT_95⟧, instance-wise agreement between LLM judges is also insightful. Even two judges with the same ⟦SLOT_96⟧ and ⟦SLOT_97⟧ scores may not reach consensus on each instance. Therefore, this session investigates (1) what percentage of a set of evaluations do two LLM judges agree on each other? (2) how do the choices of all judges on an instance vary?

**ZH** 除了用平均 ⟦SLOT_94⟧ 与 ⟦SLOT_95⟧ 从宏观视角考察位置偏差之外，LLM 评判者之间逐实例的一致性同样富有洞察。即便两个评判者的 ⟦SLOT_96⟧ 与 ⟦SLOT_97⟧ 分数相同，它们也未必在每个实例上达成共识。因此，本节考察：（1）在一组评估中，两个 LLM 评判者彼此一致的比例是多少？（2）所有评判者在某个实例上的选择如何分布？

<!-- [原子块 · img]  -->

**EN** Figure 4: Figures (a) to (c) are mutual agreement heatmap of LLM judges on MTBench and DevBench, where (b) is the agreement computation excluding the tie option {C}. Higher mutual agreement between two LLM judges is marked with brighter color. Figure (d), like Figure 3, is the distribution of disagreement on DevBench.

**ZH** 图 4：图（a）至（c）是 LLM 评判者在 MTBench 与 DevBench 上的相互一致率热力图，其中（b）为剔除平局选项 {C} 后计算的一致率。两个 LLM 评判者之间相互一致率越高，颜色越亮。图（d）与图 3 类似，是 DevBench 上的分歧分布。

**EN** C.1 Mutual Agreement & Familial Property

**ZH** C.1 相互一致率与家族属性

**EN** We compute the LLM judges’ mutual agreement on the instances to explore how “alike” or consistent they are across a set of evaluations. We denote two judges agree on an instance if their judgment choices are identical. Then the mutual agreement between two LLM judges on a benchmark is defined as the proportion of their agreed instances. Figs. 4(a) and (c) displays the mutual agreement heatmap for all judges on MTBench and DevBench, respectively. For MTBench that utilizes the 3-option mode, we also consider the “without tie" agreement since two judges are less disagreed when one chooses {C} while the other prefers a certain solution, compared to the case when they prefer different solutions. The “without tie” agreement heatmap of the twelve judges on MTBench is explored in Fig. 4(b).

**ZH** 我们计算 LLM 评判者在各实例上的相互一致率，以考察它们在一组评估中有多“相似”或一致。若两个评判者的判断选择完全相同，我们认定它们在该实例上一致。于是，两个 LLM 评判者在某个基准上的相互一致率定义为它们一致实例所占的比例。图 4（a）与（c）分别展示了所有评判者在 MTBench 与 DevBench 上的相互一致率热力图。对采用三选项模式的 MTBench，我们还考虑了“无平局”一致率，因为当一个评判者选 {C}、另一个偏好某个确定方案时，二者的分歧程度小于它们偏好不同方案的情形。十二个评判者在 MTBench 上的“无平局”一致率热力图在图 4（b）中展示。

**EN** The heatmaps reveal clear “familial patterns” in the judgment choices of these LLM judges. For instance, the GPT-4, GPT-4-Turbo, and GPT-4o series exhibit high agreement on MTBench, achieving over 70% with ties included and over 85% without. GPT-3.5-Turbo didn’t agree with the GPT-4 series and o1-mini for around 40% of the instances, indicating that they are considerably different in judging capabilities.

**ZH** 这些热力图揭示出 LLM 评判者判断选择中清晰的“家族模式”。例如，GPT-4、GPT-4-Turbo 与 GPT-4o 系列在 MTBench 上表现出高度一致，计入平局时超过 70%，不计平局时超过 85%。GPT-3.5-Turbo 在约 40% 的实例上与 GPT-4 系列及 o1-mini 不一致，说明它们在评判能力上差异相当大。

**EN** For Claude-3 models, similar familial patterns could be observed. Claude-3-Opus highly agrees with Claude-3.5-Sonnet, probably due to their similar capabilities, while it also highly agrees with Claude-3-Sonnet, likely due to their similar model structure within the same series. Interestingly, Claude-3.5-Sonnet and Claude-3-Sonnet do not exhibit a significantly high agreement, indicating that the upgrade from series 3 to 3.5 considerably impacts their judging capabilities.

**ZH** 对 Claude-3 系列模型，可以观察到类似的家族模式。Claude-3-Opus 与 Claude-3.5-Sonnet 高度一致，可能源于它们能力相近；它同时也与 Claude-3-Sonnet 高度一致，可能因为同一系列内模型结构相似。有趣的是，Claude-3.5-Sonnet 与 Claude-3-Sonnet 之间并未表现出显著高的一致率，说明从 3 系列到 3.5 系列的升级对它们的评判能力影响可观。

**EN** Gemini models exhibit rather low mutual agreement and “familial property" is minimal, but the most capable Gemini-1.5-pro aligns more closely with other capable models like the GPT-4 series and Claude-3-Opus.

**ZH** Gemini 模型表现出相当低的相互一致率，“家族属性”很弱，但能力最强的 Gemini-1.5-pro 与 GPT-4 系列、Claude-3-Opus 等其他能力较强的模型更接近。

**EN** Llama models demonstrate a high agreement among capable family members (Llama-3.3-70B and Llama-405B) and with GPT series. However, significantly smaller and less capable model like Llama-3.1-8B does not strong agree with them.

**ZH** Llama 模型在能力较强的家族成员（Llama-3.3-70B 与 Llama-405B）之间以及同 GPT 系列之间表现出较高一致率。然而，规模显著更小、能力更弱的模型（如 Llama-3.1-8B）与它们的一致度并不高。

**EN** These patterns suggest that familial similarities, possibly stemming from analogous model sizes, training data, and strategies, influence the positional preferences of these judges. In particular, the LLM judges could be primarily grouped by their capabilities; when judging capabilities are comparable, models within the same family series share a higher mutual agreement than across families.

**ZH** 这些模式说明，家族相似性——可能源于相近的模型规模、训练数据与训练策略——会影响这些评判者的位置偏好。特别是，LLM 评判者可以主要按能力分组；当评判能力相当时，同一家族系列内的模型比跨家族模型享有更高的相互一致率。

**EN** Identifying such groupings provides valuable insights, as comparisons between judges from different groups, both adept at assessing LLM-generated content, can reveal distinct position biases and enrich our understanding of this phenomenon.

**ZH** 识别这样的分组颇具价值：来自不同分组、但都擅长评估 LLM 生成内容的评判者之间的比较，可以揭示出各异的位置偏差，并丰富我们对这一现象的理解。

**EN** C.2 Disagreement & Benchmark Design Insight

**ZH** C.2 分歧与基准设计启示

**EN** Since the mutual agreement between LLM judges is not perfect and usually a considerable proportion of instances are difficult for them to reach a consensus, disagreement analysis becomes crucial and insightful. Therefore, we define the disagreement of an evaluation instance to be the number of judgments different from the majority. By this definition, an instance with all judges reaching a consensus on the better solution will have a disagreement of 0; in contrast, an instance where judgments are widely varied will result in a high disagreement. For our study where 15 judges are investigated, the maximum disagreement of an MTBench instance is 10, accounting for the 5{A}-5{B}-5{C} choice pattern by 3-option mode. On the other hand, for DevBench instances, since Gemini-1.5-flash is excluded due to insufficient data (as shown by high error rates in Tabel 2), the maximum possible disagreement for the remaining 14 judges is 7, representing the 7{A}-7{B} judgment distribution for the 2-option mode.

**ZH** 由于 LLM 评判者之间的相互一致率并不完美，且通常有相当比例的实例难以达成共识，分歧分析因而变得关键且富有洞察。我们把一个评测实例的分歧度定义为不同于多数意见的判断数量。按此定义，若所有评判者都对更优方案达成共识，该实例的分歧度为 0；反之，若判断高度分散，则会产生很高的分歧度。在我们考察 15 个评判者的研究中，MTBench 实例的最大分歧度为 10，对应三选项模式下 5{A}-5{B}-5{C} 的选择分布。另一方面，对 DevBench 实例，由于 Gemini-1.5-flash 因数据不足被剔除（如表 2 中高错误率所示），其余 14 个评判者的最大可能分歧度为 7，对应二选项模式下 7{A}-7{B} 的判断分布。

**EN** The distributions of instances with different disagreement values on MTBench and DevBench are shown in Fig. 3 and Fig. 4(d), respectively. From our disagreement analysis, at least 75% of the judges reached a choice consensus on more than half of the instances on both benchmarks. These are likely easy-to-evaluate instances, and the reliability of LLM judgments is enhanced by majority voting. In comparison, the instances with the highest disagreement are likely the ones that are difficult to evaluate and where the position bias is most likely to occur. However, luckily, these instances are rare, occupying only less than 5% for both benchmarks respectively. In other words, majority voting of multiple capable LLM judges could be practically useful for over 95% of evaluation instances on both benchmarks.

**ZH** MTBench 与 DevBench 上具有不同分歧度值的实例分布分别如图 3 与图 4（d）所示。由我们的分歧分析可见，在两个基准上，超过一半的实例有至少 75% 的评判者达成了选择共识。这些很可能是易于评估的实例，多数投票也提升了 LLM 判断的可靠性。相比之下，分歧度最高的那些实例很可能难以评估，且最容易出现位置偏差。不过所幸这些实例很罕见，在两个基准上都只占不到 5%。换言之，多个能力较强的 LLM 评判者做多数投票，对两个基准上超过 95% 的评测实例都是实用的。

**EN** Moreover, if we roughly consider the disagreement value of instances as their difficulty for judging, then Fig. 3 and Fig. 4(d) exhibit a balanced distribution of instances with varied difficulty. This is because, except for the instances with the highest disagreement, the numbers of other instances with varied disagreement do not vary significantly, indicating a smoothly increasing difficulty curve across the benchmark datasets.

**ZH** 此外，若我们把实例的分歧度值粗略视作其判断难度，那么图 3 与图 4（d）展现出不同难度实例的均衡分布。这是因为，除分歧度最高的实例外，其他各分歧度水平的实例数量并无显著变化，表明基准数据集上的难度曲线是平滑上升的。

**EN** To summarize, the practical implications of the disagreement analysis are three-fold. First, it helps identify the instances that are difficult or trivial to judge, benefiting benchmark designs to control the difficulty of evaluation by managing the number of these instances across the dataset. Second, it assists in filtering out instances where majority voting of LLM evaluators are likely to offer reliable judgments without direct comparison with human-annotated evaluations, enhancing the scalability of LLM judges especially when human evaluations are costly. In other words, if one-shot judgments from only one LLM judge are not enough reliable, multiple capable LLMs and the majoring voting strategy could be employed to make the evaluation more convincing. Last but not least, disagreement analysis provides a convenient way to make the difficulty variance of instances varied across the dataset tangible. Since the difficulty of an evaluation instance is closely related to the quality gap between the two solutions and hence position bias, the investigation of the instances where most judges particularly disagree with one another could provide more insights and inspiration for future benchmark designs and potential mitigation strategies for position bias.

**ZH** 总而言之，分歧分析的实践意义有三。其一，它有助于识别难判或易判的实例，使基准设计可以通过管理数据集中这类实例的数量来控制评测难度。其二，它有助于筛选出那些 LLM 评估者的多数投票很可能给出可靠判断的实例，无需与人工标注的评估直接比对，从而提升 LLM 评判者的可扩展性——尤其在人工评估成本高昂时。换言之，若仅由一个 LLM 评判者做一次性判断不够可靠，可以采用多个能力较强的 LLM 配合多数投票策略，使评估更具说服力。最后同样重要的是，分歧分析提供了一种便捷的途径，让数据集上实例难度的差异变得可感知。由于评测实例的难度与两个方案之间的质量差距、进而与位置偏差密切相关，考察那些多数评判者彼此分歧尤甚的实例，可以为未来的基准设计与位置偏差的潜在缓解策略提供更多洞察与启发。

**EN** Appendix D More Results of Position Bias and Answer Quality Gap Measurement

**ZH** 附录 D 位置偏差与答案质量差距度量的更多结果

**EN** D.1 MTBench

**ZH** D.1 MTBench

**EN** As shown in Fig. 2(c), considering all judges together, a larger answer quality gap generally leads to better position consistency and preference fairness. In this session, we explore whether the discovery is consistent for each individual judge. Same as Section 2.3, we apply the overall win rate to reflect the answer quality gap for visualization.

**ZH** 如图 2（c）所示，把所有评判者放在一起考虑时，更大的答案质量差距通常会带来更好的位置一致性与偏好公平性。本节我们探索这一发现是否对每个单独的评判者都成立。与 2.3 节相同，我们采用总体胜率来刻画答案质量差距以便可视化。

<!-- [原子块 · img]  -->

**EN** Figure 5: Position Consistency and Preference Fairness vs. overall win rate for each judge on MTBench. Figure (a) refers to the relationship investigation of ⟦SLOT_98⟧ and figure (b) for ⟦SLOT_99⟧.

**ZH** 图 5：MTBench 上每个评判者的位置一致性与偏好公平性相对总体胜率的关系。图（a）考察 ⟦SLOT_98⟧ 的关系，图（b）考察 ⟦SLOT_99⟧。

**EN** As shown in Fig. 5 (a), the “parabolic shape" is observed for all individual judges, indicating that the argument “a higher answer quality gap generally results in higher position consistency applies to all models. However, Fig. 5 (b) reveals that preference fairness is more judge-dependent and the impact of the answer quality gap is neglectable for certain judges. For example, while Claude-3-opus and Claude-3-sonnet exhibit conspicuous “parabolic shape", GPT-4 and GPT-3.5 present nearly linear curves. In other words, while the former models align with the general tendency that a larger answer quality gap improves preference fairness, the latter ones preserve fairness regardless of the answer quality gap. This further demonstrates the necessity to investigate preference fairness in addition to consistency when evaluating a judge model’s position bias.

**ZH** 如图 5（a）所示，所有单个评判者都呈现出“抛物线形状”，说明“答案质量差距越大，位置一致性越高”这一论断适用于所有模型。然而，图 5（b）揭示出偏好公平性更依赖评判者，且答案质量差距对某些评判者的影响可以忽略。例如，Claude-3-opus 与 Claude-3-sonnet 呈现出明显的“抛物线形状”，而 GPT-4 与 GPT-3.5 则呈现近乎线性的曲线。换言之，前者符合“答案质量差距越大、偏好公平性越好”的总体趋势，而后者则无论答案质量差距如何都保持公平。这进一步说明，在评估一个评判模型的位置偏差时，除一致性之外还有必要考察偏好公平性。

**EN** D.2 DevBench

**ZH** D.2 DevBench

**EN** This session includes a similar baseline comparison analysis on DevBench as on MTBench. As shown in Fig.6, position bias is judge-dependent and task-dependent on DevBench as well, as ⟦SLOT_100⟧ and ⟦SLOT_101⟧ vary significantly across judges and tasks. Similarly, although GPT-4 stands as the baseline model with a generally high ⟦SLOT_102⟧ across tasks, certain models achieve comparable or superior performances on certain tasks. For instance, for architecture design evaluations, GPT-4-Turbo, GPT-4o, and Gemini-1.5-pro all surpass GPT-4. Gemini-1.5-pro is especially outstanding, also exceeding GPT-4 in uml class evaluations. However, GPT-4 is still the best-performing model on UML sequence evaluations, with only GPT-3.5-Turbo can achieve comparable performance regarding certain detailed metrics (e.g., interaction complexity). These discoveries, aligning with the findings on MTBench, further necessitate the need to consider the trade-offs between positional consistency and fairness when selecting the optimal judge model for certain tasks.

**ZH** 本节在 DevBench 上做了与 MTBench 类似的基线比较分析。如图 6 所示，位置偏差在 DevBench 上同样依赖评判者与任务，因为 ⟦SLOT_100⟧ 与 ⟦SLOT_101⟧ 在不同评判者与任务之间差异显著。同样，尽管 GPT-4 作为基线模型在各任务上总体保持较高的 ⟦SLOT_102⟧，某些模型在特定任务上取得了相当或更优的表现。例如，在架构设计评估上，GPT-4-Turbo、GPT-4o 与 Gemini-1.5-pro 都超过了 GPT-4；Gemini-1.5-pro 尤为突出，在 UML 类图评估上也超过了 GPT-4。然而，在 UML 时序图评估上 GPT-4 仍是表现最好的模型，只有 GPT-3.5-Turbo 在某些细分指标（如交互复杂度）上能达到相当的表现。这些发现与 MTBench 上的结果一致，进一步说明在为特定任务挑选最优评判模型时，需要考量位置一致性与公平性之间的权衡。

<!-- [原子块 · object]  -->

**EN** Figure 6: Baseline comparisons of position bias of LLM judges across tasks on DevBench. An asterisk marks the statistical significance by Student’s t-tests. Figure (a) selects GPT-4 as the baseline, where asterisk demonstrates signficantly better or worse ⟦SLOT_103⟧ of other models compared to it. Figure (b) utilizes an absolute ⟦SLOT_104⟧ baseline of 0 and depicts preference fairness performances of LLM judges across tasks. Similar to findings on MTBench, position bias is significantly judge-dependent and task-dependent on DevBench as well.

**ZH** 图 6：DevBench 上各 LLM 评判者位置偏差跨任务的基线比较。星号标记经 Student t 检验得到的统计显著性。图（a）选取 GPT-4 作为基线，星号表示其他模型相较它在 ⟦SLOT_103⟧ 上显著更好或更差。图（b）采用 ⟦SLOT_104⟧ 的绝对值基线 0，刻画各 LLM 评判者在各任务上的偏好公平性表现。与 MTBench 上的发现类似，位置偏差在 DevBench 上也显著地依赖评判者与任务。

**EN** Appendix E Variable Selection and Tests

**ZH** 附录 E 变量选择与检验

**EN** E.1 Bidirectional Stepwise Regression with AIC

**ZH** E.1 带 AIC 的双向逐步回归

**EN** Bidirectional stepwise regression is a combination of forward selection and backward elimination techniques. It iteratively refines the model by adding or removing predictors based on a statistical criterion—commonly the Akaike Information Criterion (AIC). The objective is to select a model that balances goodness of fit and complexity, aiming for the lowest AIC value.

**ZH** 双向逐步回归是前向选择与后向剔除两种技术的结合。它依据某个统计准则——通常是赤池信息准则（AIC）——迭代地增删预测变量，从而改进模型。其目标是选出一个在拟合优度与复杂度之间取得平衡、AIC 值最低的模型。

**EN** The AIC is given by:

**ZH** AIC 由下式给出：

<!-- [原子块 · table] AIC = 2 ​ k − 2 ​ log ⁡ ( L ) , \text{AIC}=2k-2\log(L), (4) -->

**EN** where ⟦SLOT_105⟧ is the likelihood of the model and ⟦SLOT_106⟧ is the number of parameters in the model, including the error variance ⟦SLOT_107⟧. For a linear regression model with independent and identically distributed (iid) errors, ⟦SLOT_108⟧, fitted to ⟦SLOT_109⟧ observations, the log-likelihood can be written as:

**ZH** 其中 ⟦SLOT_105⟧ 为模型的似然，⟦SLOT_106⟧ 为模型中参数的个数，包含误差方差 ⟦SLOT_107⟧。对于误差独立同分布（iid）的线性回归模型 ⟦SLOT_108⟧，拟合于 ⟦SLOT_109⟧ 个观测，其 log 似然可写为：

<!-- [原子块 · table] log ⁡ ( L ) = − n 2 ​ log ⁡ ( 2 ​ π ) − n 2 ​ log ⁡ ( σ 2 ) − 1 2 ​ σ 2 ​ ∑ i = 1 n e ^ i 2 , \log(L)=-\frac{n}{2}\log(2\pi)-\frac{n}{2}\log(\sigma^{2})-\frac{1}{2\sigma^{2}}\sum_{i=1}^{n}\hat{e}_{i}^ -->

**EN** where ⟦SLOT_110⟧ is the residual for the ⟦SLOT_111⟧th observation, and ⟦SLOT_112⟧ is the variance of the errors. The AIC, in this context, becomes:

**ZH** 其中 ⟦SLOT_110⟧ 为第 ⟦SLOT_111⟧ 个观测的残差，⟦SLOT_112⟧ 为误差的方差。在此情形下，AIC 变为：

<!-- [原子块 · table] AIC = 2 ​ k + n ​ log ⁡ ( 2 ​ π ) + n ​ log ⁡ ( σ 2 ) + 1 σ 2 ​ ∑ i = 1 n e ^ i 2 . \text{AIC}=2k+n\log(2\pi)+n\log(\sigma^{2})+\frac{1}{\sigma^{2}}\sum_{i=1}^{n}\hat{e}_{i}^{2}. (6) -->

**EN** This form of the AIC balances the goodness of fit (as reflected by the residual sum of squares) and model complexity (as represented by ⟦SLOT_113⟧).

**ZH** 这种形式的 AIC 在拟合优度（由残差平方和反映）与模型复杂度（由 ⟦SLOT_113⟧ 表示）之间取得平衡。

**EN** The operation of Bidirectional stepwise regression starts with either no predictors (forward selection) or all predictors (backward elimination), where the model iteratively adds or removes variables. Each step evaluates the impact on the AIC score. In forward selection, variables are added one by one, starting from the null model, such that the addition of each variable results in the largest decrease in AIC. In backward elimination, all variables are included in the model initially, and variables are removed one at a time, with the variable whose removal causes the smallest increase in AIC being dropped.

**ZH** 双向逐步回归的运作从无预测变量（前向选择）或全部预测变量（后向剔除）开始，模型迭代地增删变量，每一步评估对 AIC 分数的影响。在前向选择中，从零模型出发逐个加入变量，使每次加入都带来 AIC 的最大下降。在后向剔除中，初始时所有变量都纳入模型，然后逐个剔除，每次剔除使 AIC 上升最小的那个变量被移除。

**EN** At each iteration, the change in AIC is computed as ⟦SLOT_114⟧, where ⟦SLOT_115⟧ refers to the AIC after adding or removing a variable, and ⟦SLOT_116⟧ is the AIC of the current model. If ⟦SLOT_117⟧, the model is improved by the addition or removal of the variable. The process terminates when neither adding nor removing variables results in a lower AIC, signifying that the most parsimonious model, based on AIC, has been reached.

**ZH** 在每次迭代中，AIC 的变化计算为 ⟦SLOT_114⟧，其中 ⟦SLOT_115⟧ 指增删某变量后的 AIC，⟦SLOT_116⟧ 为当前模型的 AIC。若 ⟦SLOT_117⟧，则加入或剔除该变量改进了模型。当加入与剔除变量都无法带来更低的 AIC 时，过程终止，表明已基于 AIC 达到最简约的模型。

**EN** E.2 Test results

**ZH** E.2 检验结果

**EN** We operated bidirectional stepwise regression on both benchmarks individually and together to identify the factors that are significantly contributing to position bias. Specifically, the variables include lengths (input, output, and prompt), answer quality gap, LLM judges, candidate models, and task categories to predict position consistency and preference fairness respectively. Table 5, 6 records the results of final step in stepwise regression for predicting ⟦SLOT_118⟧ and ⟦SLOT_119⟧, respectively. Table 7, 8 serves for DevBench, and Table 3, 4 is conducted on the integrated set of both benchmarks. The impact of variables on the model is ranked from highest to lowest, from bottom to top. Removed variables listed as None indicate the full model at this given step.

**ZH** 我们在两个基准上分别以及合并地运行了双向逐步回归，以识别对位置偏差有显著贡献的因素。具体而言，变量包括长度（输入、输出与提示）、答案质量差距、LLM 评判者、候选模型与任务类别，分别用于预测位置一致性与偏好公平性。表 5、6 记录了预测 ⟦SLOT_118⟧ 与 ⟦SLOT_119⟧ 时逐步回归最后一步的结果；表 7、8 对应 DevBench；表 3、4 则在两个基准的合并集上进行。变量对模型的影响自下而上由高到低排列。列为 None 的被剔除变量表示在该给定步骤下的全模型。

**EN** Through benchmark testing, we verified that LLM judges, task categories, and the answer quality gap significantly contribute to position bias in terms of both position consistency and preference fairness. These findings align with our empirical results, showing that position bias varies notably by judge and task, with the answer quality gap being a key influencing factor. The extent of this impact is reflected by the magnitude of change in AIC when the given variable is removed. It is worth noting that while task output length remains a significant predictor for ⟦SLOT_120⟧ and ⟦SLOT_121⟧ in both benchmarks, the change in AIC magnitude after removing this variable is very minimal. This is consistent across both benchmarks individually and combined. We therefore conclude that, although position bias is influenced by task output length, this dependency is minimal.

**ZH** 通过基准检验，我们确认了 LLM 评判者、任务类别与答案质量差距在位置一致性与偏好公平性两方面都对位置偏差有显著贡献。这些发现与我们的实证结果一致，表明位置偏差随评判者与任务显著变化，而答案质量差距是一个关键的影响因素。这种影响的程度由剔除给定变量时 AIC 变化的幅度反映。值得注意的是，尽管任务输出长度在两个基准上仍是 ⟦SLOT_120⟧ 与 ⟦SLOT_121⟧ 的显著预测变量，剔除该变量后 AIC 的变化幅度非常小。这在两个基准各自以及合并的情形下都成立。因此我们得出结论：尽管位置偏差受任务输出长度影响，这一依赖极为微弱。

<!-- [原子块 · table] Removed Variables DF Sum of Sq RSS AIC None 163.75 -18370 Task 20 2.832 166.59 -18319 Candidate 38 4.472 168.23 -18303 Quality gap 1 21.953 185.71 -17703 Judge 13 55.417 219.17 -16846 -->

**EN** Table 3: Final results of stepwise model selection for both benchmarks: Position Consistency

**ZH** 表 3：两个基准上逐步模型选择的最终结果：位置一致性

<!-- [原子块 · table] Removed Variables DF Sum of Sq RSS AIC None 254.28 -16103 Task output length 1 0.836 255.12 -16088 Quality gap 1 11.339 265.62 -15873 Task 21 16.177 270.46 -15817 Judge 13 82.069 336.35 -14641 -->

**EN** Table 4: Final results of stepwise model selection for both benchmarks: Preference Fairness

**ZH** 表 4：两个基准上逐步模型选择的最终结果：偏好公平性

<!-- [原子块 · table] Removed Variables DF Sum of Sq RSS AIC None 61.974 -13312 Task output length 1 0.0553 62.029 -13311 Candidate 29 1.6474 63.621 -13282 Task 7 1.5304 63.504 -13244 Judge 13 15.3637 77.338 -12594 Quality -->

**EN** Table 5: Final results of stepwise model selection for MTBench: Position Consistency

**ZH** 表 5：MTBench 上逐步模型选择的最终结果：位置一致性

<!-- [原子块 · table] Removed Variables DF Sum of Sq RSS AIC None 129.00 -10909.2 Quality gap 1 1.931 130.93 -10861.3 Task 7 9.295 138.29 -10689.4 Judge 13 58.847 187.85 -9672.5 -->

**EN** Table 6: Final results of stepwise model selection for MTBench: Preference Fairness

**ZH** 表 6：MTBench 上逐步模型选择的最终结果：偏好公平性

<!-- [原子块 · table] Removed Variables DF Sum of Sq RSS AIC None 55.382 -6940.2 Task output length 1 0.257 55.638 -6933.2 Candidate 9 1.514 56.896 -6905.4 Quality gap 1 13.128 68.510 -6525.3 Judge 13 84.760 140.141 -5146. -->

**EN** Table 7: Final results of stepwise model selection for DevBench: Position Consistency

**ZH** 表 7：DevBench 上逐步模型选择的最终结果：位置一致性

<!-- [原子块 · table] Removed Variables DF Sum of Sq RSS AIC None 60.104 -6753.9 Task output length 1 0.061 60.165 -6753.9 Candidate 9 0.731 60.834 -6748.2 Task 13 1.305 61.408 -6737.8 Quality gap 1 1.783 61.886 -6698.6 Ju -->

**EN** Table 8: Final results of stepwise model selection for DevBench: Preference Fairness

**ZH** 表 8：DevBench 上逐步模型选择的最终结果：偏好公平性

**EN** Appendix F Experiment Settings

**ZH** 附录 F 实验设置

**EN** This session specifies more detailed information about the judges, answer-generating models, tasks, and prompt templates used in this study. We choose to evaluate MTBench and DevBench for the following reasons: (1) all necessary information about the benchmark models, tasks, and questions is publicly available, making modifications convenient (2) they include a wide variety of answer-generating models, tasks, and task questions for a comprehensive evaluation (3) their human evaluations validated the reliability of state-of-the-art judging models (GPT-4 and GPT-4-Turbo) on their evaluation instances, hence model untested by prior work, if reaching high agreement with these validated judges, can be perceived reliable as well.

**ZH** 本节给出本研究中所用评判者、答案生成模型、任务与提示模板的更详细信息。我们选择评测 MTBench 与 DevBench，原因如下：（1）关于基准模型、任务与问题的所有必要信息都公开可得，便于改造；（2）它们包含种类丰富的答案生成模型、任务与任务问题，可支持全面评测；（3）它们的人工评估验证了最先进评判模型（GPT-4 与 GPT-4-Turbo）在其评测实例上的可靠性，因此未经前人工作检验的模型若与这些已验证的评判者高度一致，也可被视为可靠。

**EN** F.1 Judges, Candidates, and Tasks

**ZH** F.1 评判者、候选与任务

**EN** Judge

**ZH** 评判者

**EN** In this study, we choose seven GPT, four Claude, and three Gemini models as the judges. The specific versions for API call are specified as follows: o1-mini-2024-09-12 for o1-mini, gpt-4o-2024-05-13 for GPT-4o, gpt-4-1106-preview for GPT-4-Turbo, gpt-4-0613 for GPT-4, and gpt-3.5-turbo-1106 for GPT-3.5-turbo; claude-3-5-sonnet-20240620, claude-3-opus-20240229, claude-3-sonnet-20240229, and claude-3-haiku-20240307 for Claude series. The other model names and versions are as they are.

**ZH** 本研究中，我们选取七个 GPT、四个 Claude 与三个 Gemini 模型作为评判者。用于 API 调用的具体版本如下：o1-mini 对应 o1-mini-2024-09-12，GPT-4o 对应 gpt-4o-2024-05-13，GPT-4-Turbo 对应 gpt-4-1106-preview，GPT-4 对应 gpt-4-0613，GPT-3.5-turbo 对应 gpt-3.5-turbo-1106；Claude 系列对应 claude-3-5-sonnet-20240620、claude-3-opus-20240229、claude-3-sonnet-20240229 与 claude-3-haiku-20240307。其余模型的名称与版本保持原样。

**EN** Model

**ZH** 模型

**EN** The reference (or baseline) answer-generating models are vicuna-13b-v1.3 for MTBench and human for DevBench. They are chosen to ensure a baseline quality of responses and an expected widely spread quality gap across evaluations. The other models that are compared to the reference models, namely “Model" in our context, are listed as follows.

**ZH** 参照（或基线）答案生成模型在 MTBench 上为 vicuna-13b-v1.3，在 DevBench 上为 human。选取它们是为了确保回应的基线质量，以及在各次评估中形成预期上分布较广的质量差距。其余与参照模型比较的模型，即我们语境中的“模型”，列举如下。

**EN** • MTBench (30): alpaca-13b, baize-v2-13b, chatglm-6b, claude-instant-v1, claude-v1, dolly-v2-12b, falcon-40b-instruct, fastchat-t5-3b, gpt-3.5-turbo, gpt-4, gpt4all-13b-snoozy, guanaco-33b, guanaco-65b, h2ogpt-oasst-open-llama-13b, koala-13b, llama-13b, mpt-30b-chat, mpt-30b-instruct, mpt-7b-chat, nous-hermes-13b, oasst-sft-4-pythia-12b, oasst-sft-7-llama-30b, palm-2-chat-bison-001, rwkv-4-raven-14b, stablelm-tuned-alpha-7b, tulu-30b, vicuna-33b-v1.3, vicuna-7b-v1.3, wizardlm-13b, wizardlm-30b

**ZH** • MTBench（30）：alpaca-13b、baize-v2-13b、chatglm-6b、claude-instant-v1、claude-v1、dolly-v2-12b、falcon-40b-instruct、fastchat-t5-3b、gpt-3.5-turbo、gpt-4、gpt4all-13b-snoozy、guanaco-33b、guanaco-65b、h2ogpt-oasst-open-llama-13b、koala-13b、llama-13b、mpt-30b-chat、mpt-30b-instruct、mpt-7b-chat、nous-hermes-13b、oasst-sft-4-pythia-12b、oasst-sft-7-llama-30b、palm-2-chat-bison-001、rwkv-4-raven-14b、stablelm-tuned-alpha-7b、tulu-30b、vicuna-33b-v1.3、vicuna-7b-v1.3、wizardlm-13b、wizardlm-30b

**EN** • DevBench (10): codellama-7b-instruct, codellama-13b-instruct, codellama-34b-instruct, deepseek-coder-1.3b-instruct, deepseek-coder-6.7b-instruct, deepseek-coder-33b-instruct, gpt-3.5-turbo-1106, gpt-4-0125-preview, gpt-4-0613, gpt-4-1106-preview

**ZH** • DevBench（10）：codellama-7b-instruct、codellama-13b-instruct、codellama-34b-instruct、deepseek-coder-1.3b-instruct、deepseek-coder-6.7b-instruct、deepseek-coder-33b-instruct、gpt-3.5-turbo-1106、gpt-4-0125-preview、gpt-4-0613、gpt-4-1106-preview

**EN** The model names are exactly what MTBench Zheng et al. 2024b and DevBench Li et al. 2024a used in their studies. That is why for GPTs, DevBench specifies the exact version (e.g., gpt-4-0613) while MTBench doesn’t (e.g., gpt-4). In this study, we directly use the provided answers of these models to the task questions to form answer pairs and queries for the LLM judges.

**ZH** 这些模型名称与 MTBench（Zheng 等 2024b）和 DevBench（Li 等 2024a）在其研究中所用的完全一致。这正是 DevBench 对 GPT 指定了确切版本（如 gpt-4-0613）而 MTBench 没有（如 gpt-4）的原因。本研究中，我们直接使用这些模型对任务问题的既有答案来构造答案对与查询，供 LLM 评判者使用。

**EN** Task

**ZH** 任务

**EN** For tasks, we also follow the original studies of these two benchmarks, except for DevBench we separate the gerenal metrics into detailed ones and considered them as different tasks. In this sense, our study experiments on the following tasks to provide a comprehensive study on the positon bias of LLM-as-a-Judge:

**ZH** 任务方面，我们同样遵循这两个基准的原始研究，只是对 DevBench 把通用指标拆分为细分指标并视作不同任务。据此，我们的研究在以下任务上实验，以对 LLM-as-a-Judge 的位置偏差做全面考察：

**EN** • MTBench (8): coding, extraction, humanities, math, reasoning, roleplay, stem, and writing.

**ZH** • MTBench（8）：coding、extraction、humanities、math、reasoning、roleplay、stem 与 writing。

**EN** • Devbench (14): – UML class (4): cohesion_and_decoupling, complexity, practicability, and faithfulness – UML sequence (5): cohesion_and_decoupling, interaction_complexity, practicability, uniformity_and_integration, and faithfulness – architecture design (5): conformance, design_and_coding, practicability, uniformity_and_integration, and faithfulness

**ZH** • Devbench（14）：– UML 类图（4）：cohesion_and_decoupling、complexity、practicability 与 faithfulness – UML 时序图（5）：cohesion_and_decoupling、interaction_complexity、practicability、uniformity_and_integration 与 faithfulness – 架构设计（5）：conformance、design_and_coding、practicability、uniformity_and_integration 与 faithfulness

**EN** F.2 Prompt Settings

**ZH** F.2 提示设置

**EN** We follow the original prompt settings of MTBench and DevBench in our study of pairwise comparative LLM-as-a-Judge.

**ZH** 在我们对成对比较式 LLM-as-a-Judge 的研究中，我们遵循 MTBench 与 DevBench 的原始提示设置。

**EN** Though written differently, these prompts all share same key components:

**ZH** 尽管写法不同，这些提示都包含相同的关键组成部分：

**EN** • A system prompt explaining the judging task and the role the LLM should be playing.

**ZH** • 一条系统提示，说明评判任务以及 LLM 应当扮演的角色。

**EN** • Emphasized “should" and“shouldn’t"s.

**ZH** • 被强调的“应当”与“不应当”。

**EN** • A prompt structure with placeholders for specific questions and model answers

**ZH** • 带有占位符的提示结构，用于填入具体问题与模型答案。

**EN** • A specified output format for later judgment extraction

**ZH** • 指定的输出格式，便于后续提取判断。

**EN** • Chain-of-Thought Wei et al. 2022 prompts requiring the LLM judge to provide reasons for its judgment

**ZH** • 思维链（Wei 等 2022）提示，要求 LLM 评判者给出判断理由。

**EN** The detailed prompt templates are specified below.

**ZH** 详细的提示模板如下。

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->
