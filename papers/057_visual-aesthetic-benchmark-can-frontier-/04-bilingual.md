# 视觉审美基准：前沿模型能判断美吗？

> 原标题：Visual Aesthetic Benchmark: Can Frontier Models Judge Beauty?
> 作者：Yichen Feng, Yuetai Li, Chunjiang Liu, Yuanyuan Chen, Fengqing Jiang, Yue Huang, Hang Hua, Zhengqing Yuan, Kaiyuan Zheng, Luyao Niu, Bhaskar Ramasubramanian, Basel Alomair 等 · arXiv:2605.12684 · 2026-05-12

<!-- [原子块 · verbatim] Visual Aesthetic Benchmark: Can Frontier Models Judge Beauty? -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] Multimodal large language models (MLLMs) are now routinely deployed for visual understanding, generation, and curation. A substantial fraction of these applications require an explicit aesthetic judgm -->

<!-- [原子块 · verbatim] Code BakeLab/Visual-Aesthetic-Benchmark Dataset BakeLab/Visual-Aesthetic-Benchmark Website vab.bakelab.ai -->

<!-- [原子块 · img]  -->

**EN** Figure 1: Overview of the VAB benchmark. VAB spans three visual domains — fine art, photography, and illustration — covering 24 topics across 400 evaluation tasks and 1,195 images. Each task presents a set of candidate images sharing a common subject.

**ZH** 图 1：VAB 基准总览。VAB 覆盖美术、摄影与插画三个视觉领域，包含 24 个主题、400 个评测任务与 1,195 张图像。每个任务给出一组主体内容相同的候选图像。

**EN** 1 Introduction

**ZH** 1 引言

**EN** Multimodal large language models (MLLMs) have become critical to a widening range of visual tasks such as image generation and curation (Liu et al., 2023, Team et al., 2023, Wang et al., 2024). Many of these applications require aesthetic judgment, asking models to compare visual works and identify differences in execution quality across composition, color harmony, technical execution, and cultural convention. This makes aesthetic judgment a demanding test of higher-order multimodal reasoning that is often omitted by existing visual benchmarks (Yu et al., 2023, Yue et al., 2024).

**ZH** 多模态大语言模型（MLLM）已成为图像生成与图像策展等日益广泛的视觉任务的关键支撑（Liu 等，2023；Team 等，2023；Wang 等，2024）。其中许多应用需要做出审美判断，要求模型比较视觉作品，识别其在构图、色彩和谐、技法完成度与文化惯例上的水准差异。这使审美判断成为对高阶多模态推理能力的严苛检验，而现有视觉基准往往将其遗漏（Yu 等，2023；Yue 等，2024）。

**EN** Existing image-aesthetics datasets and methods typically reduce aesthetic judgment to a mapping from an image to a scalar score (Murray et al., 2012, Kong et al., 2016, He et al., 2022, Lee and Kim, 2019, Hosu et al., 2019, Yi et al., 2023, He et al., 2023), an approach that we argue is poorly suited to the underlying decision being studied. Preference order is inferred from independent scores rather than measured through direct comparison; crowd-averaged labels mix expertise, taste, and annotation noise, so the aesthetic signal is difficult to isolate; and because images in such datasets often depict different subjects, a model can shortcut its way to high accuracy by exploiting content preferences instead of discriminating execution quality.

**ZH** 现有的图像美学数据集与方法通常把审美判断简化为从图像到标量分数的映射（Murray 等，2012；Kong 等，2016；He 等，2022；Lee 与 Kim，2019；Hosu 等，2019；Yi 等，2023；He 等，2023）。我们认为这一做法与所研究的决策本身并不匹配：偏好次序是由彼此独立的分数推断而来，而非通过直接比较测得；众包平均的标签把专业水平、个人趣味与标注噪声混在一起，审美信号因而难以分离；同时由于这类数据集中的图像常描绘不同主体，模型可以借内容偏好走捷径获得高准确率，而不必真正区分完成质量。

**EN** We first ask whether scoring faithfully captures comparative preference . Eight expert annotators evaluate the same images under both independent absolute scoring and direct comparative ranking, and the two protocols disagree. Comparative ranking yields 42 percentage points higher inter-annotator agreement on best-image selection than score-derived rankings (Talebi and Milanfar, 2018, Ma et al., 2017, Wu et al., 2023, Zhou et al., 2024a). The two protocols therefore elicit different preference signals from the same annotators, and direct comparison captures the underlying judgment more faithfully than the pointwise scoring used in most existing pipelines.

**ZH** 我们首先追问：评分是否忠实地刻画了比较偏好。八位专家标注者对同一批图像分别执行独立绝对评分与直接比较排序两种流程，结果两者并不一致。在最优图像选择上，比较排序带来的标注者间一致性比分数导出排序高出 42 个百分点（Talebi 与 Milanfar，2018；Ma 等，2017；Wu 等，2023；Zhou 等，2024a）。可见两种流程从同一批标注者身上引出了不同的偏好信号，而直接比较比多数现有流程采用的逐点评分更忠实地捕捉了底层判断。

**EN** Building on this finding, we introduce the Visual Aesthetic Benchmark (VAB), which formulates aesthetic judgment as a comparative selection problem over candidate sets with matched subject matter. VAB contains 400 tasks and 1,195 images across fine art, photography, and illustration, covering 24 topics (Figure 1). Each task presents two to six images sharing a common subject, and the model selects the best image and, under the stricter setting, also the worst image. Three design choices distinguish VAB from prior aesthetic benchmarks. Matched subject matter within each task isolates differences in execution from differences in content; each ground-truth label is the consensus of 10 independent expert judges, filtered through a dual-threshold criterion to remove ambiguous cases; and every task is evaluated under three independent random permutations of the candidate order. We report ap@1, the average accuracy across the three evaluations, and pass^3, which credits a task only when the model is correct in all three.

**ZH** 在上述发现的基础上，我们提出视觉审美基准（Visual Aesthetic Benchmark, VAB），把审美判断表述为在主体内容一致的候选集上做比较选择的问题。VAB 包含 400 个任务与 1,195 张图像，覆盖美术、摄影与插画三个领域的 24 个主题（图 1）。每个任务给出 2 至 6 张主体内容相同的图像，模型需选出最优图像；在更严格的设置下还需同时选出最差图像。有三项设计使 VAB 区别于此前的美学基准：任务内主体内容一致，把完成质量差异与内容差异分离开来；每条真值标签都是 10 位独立专家评审的共识，并经双阈值准则过滤以剔除含糊样本；每个任务在候选顺序的三次独立随机排列下各评测一次。我们报告 ap@1，即三次评测的平均准确率，以及 pass^3，即只在三次全部正确时才把任务计为通过。

**EN** We benchmark 20 frontier MLLMs and six dedicated visual-quality reward models on VAB. The strongest system, Claude Sonnet 4.6, reaches 26.5% on TB-1 pass^3, 42.4 points below the human baseline of 68.9%. Models are also highly sensitive to candidate order, retaining only 34–65% of their ap@1 accuracy when required to be correct across all three permutations, and they degrade much faster than humans as the candidate set grows: a ⟦SLOT_0⟧ drop from two-image to four-or-more-image tasks, against only ⟦SLOT_1⟧ for human experts. The contributions of this paper are as follows.

**ZH** 我们在 VAB 上评测了 20 个前沿 MLLM 与六个专用视觉质量奖励模型。最强的系统 Claude Sonnet 4.6 在 TB-1 pass^3 上仅达 26.5%，比人类基线的 68.9% 低 42.4 个百分点。模型对候选顺序也高度敏感：当要求在三次排列下全部正确时，它们只能保留 ap@1 准确率的 34%–65%；并且随着候选集增大，其退化速度远快于人类——从两图像任务到四图像及以上任务下降 ⟦SLOT_0⟧，人类专家仅下降 ⟦SLOT_1⟧。本文贡献如下。

**EN** • A controlled human study with eight expert annotators establishes that direct comparative ranking is substantially more reliable than independent scoring for subjective aesthetic annotation, and motivates the design of the benchmark.

**ZH** • 一项由八位专家标注者参与的控制实验表明，对于主观审美标注，直接比较排序远比独立评分可靠，这一结论构成了本基准设计的依据。

**EN** • VAB is, to our knowledge, the first set-based, expert-grounded, multi-domain aesthetic benchmark with permutation-robust evaluation, covering 400 tasks and 1,195 images across fine art, photography, and illustration.

**ZH** • 据我们所知，VAB 是首个基于集合、以专家标注为支撑、覆盖多领域并具备排列鲁棒评测的美学基准，包含美术、摄影与插画领域的 400 个任务与 1,195 张图像。

**EN** • A systematic evaluation of 20 frontier MLLMs and six dedicated reward models exposes a persistent 42.4-point gap to human experts on TB-1 pass^3 together with severe positional instability across permutations of the candidate order.

**ZH** • 对 20 个前沿 MLLM 与六个专用奖励模型的系统评测显示，它们在 TB-1 pass^3 上与人类专家存在 42.4 个百分点的持续差距，且在候选顺序的不同排列下表现出严重的位置不稳定。

**EN** • Fine-tuning on 2,000 expert examples brings a 35B-parameter model close to a 397B-parameter open-weight model, indicating that expert comparative judgments transfer effectively through lightweight adaptation.

**ZH** • 在 2,000 条专家样本上微调后，35B 参数模型的表现接近 397B 参数的开源权重模型，说明专家比较判断可通过轻量适配有效迁移。

**EN** 2 Human Annotation Study: Ranking vs. Scoring

**ZH** 2 人工标注研究：排序与评分

**EN** Existing aesthetic benchmarks rely on Scoring to collect ground truth labels (Murray et al., 2012, Kong et al., 2016, He et al., 2022, Cao et al., 2025). We conduct a controlled human study to explore the following research question regarding the annotation process:

**ZH** 现有美学基准依赖评分来收集真值标签（Murray 等，2012；Kong 等，2016；He 等，2022；Cao 等，2025）。我们开展了一项控制实验，以考察标注过程中的下述研究问题：

**EN** Which protocol yields a more scientifically sound signal for data annotation?

**ZH** 哪种流程能为数据标注提供更合乎科学依据的信号？

**EN** • Scoring: expert annotates each image independently on an absolute aesthetic scale.

**ZH** • 评分：专家按绝对美学量表为每张图像独立打分。

**EN** • Ranking: expert compares images and annotates their relative order.

**ZH** • 排序：专家比较各图像并标注其相对次序。

**EN** Setup and Metrics.

**ZH** 设置与指标。

**EN** Eight expert annotators evaluate the same images under two protocols: (1) scoring assigns each image an independent score ⟦SLOT_2⟧; (2) ranking orders images directly within groups of size ⟦SLOT_3⟧. We construct 119 homogeneous-content tasks, in which all candidates share the same underlying content, and 107 heterogeneous-content tasks formed by regrouping images across source groups while preserving topic consistency. We compare the two protocols along three dimensions:

**ZH** 八位专家标注者在两种流程下评估同一批图像：（1）评分为每张图像赋予独立分数 ⟦SLOT_2⟧；（2）排序在规模为 ⟦SLOT_3⟧ 的组内直接给出图像次序。我们构建了 119 个同质内容任务，其中所有候选共享相同底层内容；另构建 107 个异质内容任务，通过在保持主题一致的前提下跨源组重组图像得到。我们从三个维度比较两种流程：

**EN** • Fidelity (Kendall’s ⟦SLOT_4⟧ (Kendall, 1938)): we compute ⟦SLOT_5⟧, where ⟦SLOT_6⟧ and ⟦SLOT_7⟧ are the numbers of concordant and discordant pairs between an annotator’s score-derived ranking ⟦SLOT_8⟧ and the same annotator’s direct comparison. A low ⟦SLOT_9⟧ means the two protocols elicit different preference orderings from the same person. We additionally report the top-1 self-consistency (SC) rate: the fraction of annotator–task pairs for which ⟦SLOT_10⟧ and the direct comparison select the same top image.

**ZH** • 保真度（Kendall’s ⟦SLOT_4⟧（Kendall，1938））：我们计算 ⟦SLOT_5⟧，其中 ⟦SLOT_6⟧ 与 ⟦SLOT_7⟧ 分别是标注者的分数导出排序 ⟦SLOT_8⟧ 与其直接比较之间的一致对与不一致对数目。⟦SLOT_9⟧ 偏低意味着两种流程从同一个人身上引出了不同的偏好次序。我们还报告 top-1 自洽率（SC rate）：⟦SLOT_10⟧ 与直接比较选出同一张最优图像的标注者–任务对所占比例。

**EN** • Reproducibility (⟦SLOT_11⟧): ⟦SLOT_12⟧ is the proportion of tasks where a single image receives ⟦SLOT_13⟧ of 8 best-image votes; ⟦SLOT_14⟧ and ⟦SLOT_15⟧ are defined analogously. Higher accuracy means the protocol produces ground truth labels that different experts can independently reproduce.

**ZH** • 可复现性（⟦SLOT_11⟧）：⟦SLOT_12⟧ 是单张图像获得 ⟦SLOT_13⟧ 张（8 张中的）最优票的任务比例；⟦SLOT_14⟧ 与 ⟦SLOT_15⟧ 的定义类似。准确率越高，说明该流程产生的真值标签越能被不同专家独立复现。

**EN** • Distinguishability (top-1 entropy (Shannon, 1948)): we measure ⟦SLOT_16⟧, where ⟦SLOT_17⟧ is the fraction of annotators selecting image ⟦SLOT_18⟧ as best. Lower entropy means annotators concentrate on a single top choice rather than spreading votes.

**ZH** • 可区分度（top-1 熵（Shannon，1948））：我们测量 ⟦SLOT_16⟧，其中 ⟦SLOT_17⟧ 是选择图像 ⟦SLOT_18⟧ 为最优的标注者比例。熵越低，说明标注者集中于单一首选，而非把票分散到多张图像上。

**EN** Full protocol details, notations, formal definitions, and statistical tests are in Appendix F.

**ZH** 完整流程细节、符号、形式化定义与统计检验见附录 F。

**EN** Scoring does not faithfully preserve preference order.

**ZH** 评分不能忠实保留偏好次序。

**EN** Table 1 shows that score-derived rankings often diverge from the direct comparisons given by the same annotator. The mean Kendall’s ⟦SLOT_19⟧ is 0.188 for homogeneous-content and 0.351 for heterogeneous-content tasks; the top-1 self-consistency rates are 45.5% and 52.0%, respectively. In other words, nearly half of the numeric score annotations fail to recover the order that the same annotator expresses under direct comparison.

**ZH** 表 1 显示，分数导出排序常常偏离同一标注者给出的直接比较。同质内容任务的 Kendall’s ⟦SLOT_19⟧ 均值为 0.188，异质内容任务为 0.351；top-1 自洽率分别为 45.5% 与 52.0%。换言之，近一半的数值评分标注无法还原同一标注者在直接比较下所表达的次序。

**EN** Table 1: We report within-annotator agreement between expert’s score-derived rankings ⟦SLOT_20⟧ and direct comparison from 8 annotators, measured by Kendall’s ⟦SLOT_21⟧ (⟦SLOT_22⟧) and top-1 self-consistency rate (SC rate, ⟦SLOT_23⟧), defined as the fraction of annotator–task pairs where the score-derived top-1 matches the direct comparison top-1. The results show that nearly 50% of the numeric score annotations do not reliably preserve the order that the annotator would express in direct comparison.

**ZH** 表 1：我们报告八位专家标注者的分数导出排序 ⟦SLOT_20⟧ 与直接比较之间的标注者内一致性，以 Kendall’s ⟦SLOT_21⟧（⟦SLOT_22⟧）与 top-1 自洽率（SC rate，⟦SLOT_23⟧）衡量，后者定义为分数导出 top-1 与直接比较 top-1 一致的标注者–任务对比例。结果表明，近 50% 的数值评分标注无法可靠保留标注者在直接比较中会表达的次序。

**EN** (a) Results on homogeneous-content tasks.

**ZH** （a）同质内容任务上的结果。

<!-- [原子块 · table] n n N N tasks Mean τ \tau Std. τ \tau SC rate 2 28 0.098 0.511 54.9% 3 38 0.274 0.328 49.7% 4 35 0.126 0.243 34.3% 5 18 0.267 0.243 43.6% All 119 0.188 0.354 45.5% -->

**EN** (b) Results on heterogeneous-content tasks.

**ZH** （b）异质内容任务上的结果。

<!-- [原子块 · table] n n N N tasks Mean τ \tau Std. τ \tau SC rate 2 19 0.342 0.427 67.1% 3 37 0.286 0.300 48.0% 4 34 0.441 0.172 51.1% 5 17 0.324 0.256 45.6% All 107 0.351 0.291 52.0% -->

**EN** Ranking yields more reproducible labels.

**ZH** 排序产生可复现性更高的标签。

**EN** Table 2 shows that ranking yields substantially higher inter-annotator agreement on best and worst labels. On homogeneous-content tasks, ranking improves ⟦SLOT_24⟧ by 42.0 points, ⟦SLOT_25⟧ by 37.0 points, and ⟦SLOT_26⟧ by 51.3 points (all ⟦SLOT_27⟧, McNemar test (McNemar, 1947)); the same pattern holds for heterogeneous-content tasks. Independent experts can therefore reproduce best/worst labels far more reliably under ranking than under scoring.

**ZH** 表 2 显示，排序在最优与最差标签上带来显著更高的标注者间一致性。在同质内容任务上，排序使 ⟦SLOT_24⟧ 提升 42.0 个百分点，⟦SLOT_25⟧ 提升 37.0 个百分点，⟦SLOT_26⟧ 提升 51.3 个百分点（均 ⟦SLOT_27⟧，McNemar 检验（McNemar，1947））；异质内容任务呈现同样规律。因此，多位独立专家在排序流程下能够远比在评分流程下更可靠地复现最优／最差标签。

**EN** Table 2: We report inter-annotator consistency on best and worst decisions for 8 annotators, where a majority requires agreement from at least 5 of 8. Each row shows task-level accuracy ⟦SLOT_28⟧ (⟦SLOT_29⟧), improvement ⟦SLOT_30⟧, and the exact two-sided McNemar ⟦SLOT_31⟧-value (⟦SLOT_32⟧) (McNemar, 1947, Fagerland et al., 2013). The Significance level is marked as ⟦SLOT_33⟧. Results show that ranking is more likely to yield annotation labels that independent experts can reproduce.

**ZH** 表 2：我们报告八位标注者在最优与最差判断上的标注者间一致性，其中多数一致要求至少 5/8 的标注者意见相同。每行给出任务级准确率 ⟦SLOT_28⟧（⟦SLOT_29⟧）、提升幅度 ⟦SLOT_30⟧，以及精确双侧 McNemar ⟦SLOT_31⟧ 值（⟦SLOT_32⟧）（McNemar，1947；Fagerland 等，2013）。显著性水平标记为 ⟦SLOT_33⟧。结果表明，排序更有可能产生可被独立专家复现的标注标签。

**EN** Homogeneous-content (⟦SLOT_34⟧) Heterogeneous-content (⟦SLOT_35⟧) Metric Scoring Ranking ⟦SLOT_36⟧ ⟦SLOT_37⟧ Scoring Ranking ⟦SLOT_38⟧ ⟦SLOT_39⟧ ⟦SLOT_40⟧ 52.9% 95.0% ⟦SLOT_41⟧42.0% ⟦SLOT_42⟧0.001∗∗ 65.4% 94.4% ⟦SLOT_43⟧29.0% ⟦SLOT_44⟧0.001∗∗ ⟦SLOT_45⟧ 55.5% 92.4% ⟦SLOT_46⟧37.0% ⟦SLOT_47⟧0.001∗∗ 69.2% 93.5% ⟦SLOT_48⟧24.3% ⟦SLOT_49⟧0.001∗∗ ⟦SLOT_50⟧ 39.5% 90.8% ⟦SLOT_51⟧51.3% ⟦SLOT_52⟧0.001∗∗ 49.5% 90.7% ⟦SLOT_53⟧41.1% ⟦SLOT_54⟧0.001∗∗

**ZH** 同质内容（⟦SLOT_34⟧） 异质内容（⟦SLOT_35⟧） 指标 评分 排序 ⟦SLOT_36⟧ ⟦SLOT_37⟧ 评分 排序 ⟦SLOT_38⟧ ⟦SLOT_39⟧ ⟦SLOT_40⟧ 52.9% 95.0% ⟦SLOT_41⟧42.0% ⟦SLOT_42⟧0.001∗∗ 65.4% 94.4% ⟦SLOT_43⟧29.0% ⟦SLOT_44⟧0.001∗∗ ⟦SLOT_45⟧ 55.5% 92.4% ⟦SLOT_46⟧37.0% ⟦SLOT_47⟧0.001∗∗ 69.2% 93.5% ⟦SLOT_48⟧24.3% ⟦SLOT_49⟧0.001∗∗ ⟦SLOT_50⟧ 39.5% 90.8% ⟦SLOT_51⟧51.3% ⟦SLOT_52⟧0.001∗∗ 49.5% 90.7% ⟦SLOT_53⟧41.1% ⟦SLOT_54⟧0.001∗∗

**EN** Ranking makes the top choice stand out more clearly.

**ZH** 排序使首选更为突出。

**EN** Table 3 measures how concentrated their top-choice preference is within each task. It shows that ranking produces lower entropy over top-1 selections (Shannon, 1948) (0.729 vs. 1.213) and a much higher rate of unanimous choices (10.1% vs. 0.8%; Wilcoxon ⟦SLOT_55⟧ (Wilcoxon, 1945)). More generally, ranking concentrates votes on a single preferred image rather than spreading them across several plausible winners.

**ZH** 表 3 衡量每个任务内首选偏好的集中程度。结果显示，排序在 top-1 选择上产生更低的熵（Shannon，1948）（0.729 对 1.213），以及更高的一致选择率（10.1% 对 0.8%；Wilcoxon ⟦SLOT_55⟧（Wilcoxon，1945））。更一般地说，排序把票数集中到单一偏好图像上，而不是分散到若干同样合理的候选上。

**EN** Table 3: We report top-choice concentration in the homogeneous-content setting (119 tasks, 8 annotators), measured by entropy ⟦SLOT_56⟧ (Shannon, 1948) and the rate of unanimous tasks (⟦SLOT_57⟧). The 95% confidence intervals use a normal approximation for mean ⟦SLOT_58⟧ and a Wilson interval (Wilson, 1927) for the unanimous-task rate. A Wilcoxon signed-rank test (Wilcoxon, 1945) yields that the difference is statistically significant (⟦SLOT_59⟧).

**ZH** 表 3：我们报告同质内容设置（119 个任务，8 位标注者）下首选的集中程度，以熵 ⟦SLOT_56⟧（Shannon，1948）与一致任务率（⟦SLOT_57⟧）衡量。95% 置信区间对熵均值 ⟦SLOT_58⟧ 采用正态近似，对一致任务率采用 Wilson 区间（Wilson，1927）。Wilcoxon 符号秩检验（Wilcoxon，1945）表明差异具有统计显著性（⟦SLOT_59⟧）。

<!-- [原子块 · table] Metric Scoring Ranking Mean H H ( ↓ \downarrow ) [95% CI] 1.213 ​ [ 1.137 , 1.289 ] 1.213\ [1.137,\ 1.289] 0.729 ​ [ 0.665 , 0.793 ] 0.729\ [0.665,\ 0.793] Unanimous rate ( ↑ \uparrow ) 0.8 % ​ [ 0.1  -->

**EN** Interpretation.

**ZH** 解释。

**EN** Our findings align with conclusions from two complementary disciplines. Aesthetically, modern aesthetics favors a relational view of beauty (Goldman, 1995, Levinson, 2005): people judge preference more reliably when alternatives are juxtaposed than when items are assessed in isolation. Cognitively, comparative judgment is a more primitive operation than absolute evaluation (Thurstone, 1927). Absolute scoring requires maintaining an internal reference scale and converting qualitative impressions into numbers, imposing heavier cognitive load and greater instability (Stewart et al., 2005, Parducci, 1965).

**ZH** 我们的发现与两个互补学科中的结论相吻合。在美学上，现代美学倾向于关系性的美之观念（Goldman，1995；Levinson，2005）：当各选项并置呈现时，人们判断偏好的可靠性高于孤立评估单个对象。在认知上，比较判断比绝对评价更基础（Thurstone，1927）。绝对评分需要维持一个内在参照量表，并把质性印象转换为数字，认知负荷更重、波动更大（Stewart 等，2005；Parducci，1965）。

**EN** We therefore adopt ranking as the annotation protocol for VAB. Extended discussion is provided in Appendix F.2.

**ZH** 因此我们把 VAB 的标注流程定为排序。扩展讨论见附录 F.2。

**EN** 3 The VAB Benchmark

**ZH** 3 VAB 基准

**EN** Building on the findings of Section 2, we construct the Visual Aesthetic Benchmark (VAB) to test whether frontier multimodal models can make expert-aligned aesthetic judgments under a ranking-based protocol. In contrast with prior evaluations that aggregate scalar ratings from crowd annotators (Murray et al., 2012, Kong et al., 2016, He et al., 2022), VAB casts aesthetic evaluation as comparative selection over candidate sets with matched subject matter: each task asks the model to identify the best image and, in the stricter setting, also the worst. The remainder of this section describes the task layout, the data construction pipeline, and the ground-truth formation procedure.

**ZH** 在第 2 节发现的基础上，我们构建视觉审美基准（VAB），以检验前沿多模态模型能否在基于排序的流程下做出与专家一致的审美判断。与此前聚合众包标注者标量评分的评测不同（Murray 等，2012；Kong 等，2016；He 等，2022），VAB 把审美评测表述为在主体内容一致的候选集上做比较选择：每个任务要求模型找出最优图像，在更严格的设置下还要找出最差图像。本节其余部分介绍任务形式、数据构建流程与真值形成过程。

**EN** 3.1 Overview

**ZH** 3.1 总览

<!-- [原子块 · img]  -->

**EN** Figure 2: Detailed distribution of VAB.

**ZH** 图 2：VAB 的详细分布。

**EN** Task formulation. Each benchmark task presents a candidate set of images with matched subject matter, so performance depends on differences in execution rather than differences in depicted content. VAB contains 400 released tasks and 1,195 images across fine art, photography, and illustration, covering 24 topics with candidate set sizes from 2 to 6 images. We consider two settings: in Top-1, the model selects the best image in the set; in TB-1, it identifies both the best and the worst image. Figure 1 provides a visual overview, Figure 2 summarizes the released domain and topic distribution, and Appendix B.1 reports detailed benchmark statistics.

**ZH** 任务形式。每个基准任务给出一组主体内容一致的候选图像，因此表现取决于完成质量差异而非所绘内容的差异。VAB 包含 400 个已发布任务与 1,195 张图像，覆盖美术、摄影与插画三个领域的 24 个主题，候选集规模为 2 至 6 张图像。我们考察两种设置：Top-1 中模型从候选集选出最优图像；TB-1 中模型需同时找出最优与最差图像。图 1 给出可视化总览，图 2 汇总已发布的领域与主题分布，附录 B.1 报告详细的基准统计。

**EN** Evaluation protocol. Labels are derived from direct comparative judgments by independent experts rather than post hoc aggregation of absolute scores. Each task is evaluated three times, each under an independent random permutation of the candidate order. We report ap@1, the average accuracy across the three evaluations, and pass^3, which counts a task as correct only if the model is correct in all three. Representative topic-level examples are collected in Appendix I.

**ZH** 评测流程。标签来自独立专家的直接比较判断，而非对绝对分数的事后聚合。每个任务评测三次，每次使用候选顺序的一次独立随机排列。我们报告 ap@1，即三次评测的平均准确率，以及 pass^3，即只在三次全部正确时才计为通过。代表性主题级样例收录于附录 I。

**EN** 3.2 Data Construction

**ZH** 3.2 数据构建

<!-- [原子块 · img]  -->

**EN** Figure 3: Overview of the VAB data construction pipeline. Images are organized into candidate sets with matched subject matter and varying aesthetic execution, then passed through expert review and consensus filtering before entering the benchmark.

**ZH** 图 3：VAB 数据构建流程总览。图像被组织成主体内容一致、完成质量各异的候选集，再经专家评审与共识过滤后进入基准。

**EN** Because VAB is annotated through direct ranking over candidate sets, data construction is organized around matched image groups rather than standalone images: in every domain, the members of a set share subject matter but vary in execution quality. Figure 3 summarizes the pipeline; Appendix B.2 reports the full raw-pool statistics, and Appendix B.3 contains the domain-level construction details.

**ZH** 由于 VAB 通过对候选集直接排序来标注，数据构建围绕匹配的图像组而非单张图像展开：在每个领域内，一组内的成员主体内容相同而完成质量不同。图 3 概括了该流程；附录 B.2 报告原始素材池的完整统计，附录 B.3 给出领域级构建细节。

**EN** Fine Art. We commissioned 426 painting sets comprising 1,142 images. Each set is built from constrained artist prompts that preserve subject matter while allowing variation in composition, value structure, color handling, and finish. All works were commissioned specifically for VAB.

**ZH** 美术。我们委托创作了 426 组绘画，共 1,142 张图像。每组由受限的画家提示生成，这些提示在保持主体内容的同时，允许在构图、明度结构、色彩处理与完成度上有所变化。所有作品均为 VAB 专门委托创作。

**EN** Photography. We constructed 670 photography sets comprising 1,809 images. Each set originates from a single source photograph, many provided directly by professional photographers, and is expanded through two pipelines: an expert-edit pipeline based on professional retouching tools, which can produce either original/improved pairs or larger multi-expert sets, and a scalable agent-edit pipeline that generates improved and degraded variants. The agent-edit prompt sequence and runtime pipeline are recorded in Appendix H.1.

**ZH** 摄影。我们构建了 670 组摄影，共 1,809 张图像。每组源自单张源照片（其中许多由专业摄影师直接提供），并通过两条流程扩充：一条是基于专业修图工具的专家编辑流程，可产出原图／改进图对，也可产出更大的多专家候选集；另一条是可扩展的智能体编辑流程，生成改进变体与退化变体。智能体编辑的提示序列与运行时流程记录于附录 H.1。

**EN** Illustration. We constructed 271 illustration sets comprising 908 images. These sets are formed either by prompt-based generation with text-to-image models or by rendering CC0 3D assets under controlled viewpoint and presentation changes, producing multiple images with matched subject matter but varying execution. Prompt templates are in Appendix H.2.

**ZH** 插画。我们构建了 271 组插画，共 908 张图像。这些候选集或通过文生图模型的提示生成得到，或在受控的视角与呈现变化下渲染 CC0 三维资产得到，从而产出主体内容一致而完成质量各异的多张图像。提示模板见附录 H.2。

**EN** All collected sets are deduplicated and reviewed for semantic consistency before annotation.

**ZH** 所有收集到的候选集在标注前均经过去重与语义一致性审查。

**EN** 3.3 Expert Annotation and Ground Truth

**ZH** 3.3 专家标注与真值

**EN** Following Section 2, VAB uses ranking-based expert consensus for ground truth.

**ZH** 依循第 2 节，VAB 采用基于排序的专家共识作为真值。

**EN** Review setup. Creation and evaluation are strictly separated. In the raw pre-filter pool, each collected candidate set is reviewed by 10 independent expert judges drawn from a pool of more than 100 evaluators, yielding over 13,000 assessments and more than 300 hours of review. Judges remain blind to artist identity throughout annotation. Rubrics and interface examples are in Appendix C. Additional topic-level examples are in Appendix I.

**ZH** 评审设置。构建与评测严格分离。在原始预过滤素材池中，每个候选集由从 100 余名评测者池中抽取的 10 位独立专家评审审阅，累计超过 13,000 次评估与 300 余小时审阅。评审在标注全程对作者身份保持盲态。评判细则与界面示例见附录 C，更多主题级样例见附录 I。

**EN** Annotation protocol. Each task presents ⟦SLOT_60⟧ candidate images side by side. Judges first assess each image against the domain-specific rubric and then make a comparative selection over the full set. For ⟦SLOT_61⟧, a judge selects the best image. For ⟦SLOT_62⟧, a judge selects both the best and the worst image, with distinct choices required. Every task receives exactly 10 judgments. A representative annotation example is shown in Figure 4.

**ZH** 标注流程。每个任务将 ⟦SLOT_60⟧ 张候选图像并排呈现。评审先依据领域专属细则评估每张图像，再在整个候选集上做出比较选择。对于 ⟦SLOT_61⟧，评审选出最优图像；对于 ⟦SLOT_62⟧，评审同时选出最优与最差图像，且两者必须不同。每个任务恰好收到 10 次评判。一个代表性的标注示例如图 4 所示。

<!-- [原子块 · img]  -->

**EN** Figure 4: Example of a single VAB annotation task, illustrating the candidate set presented to expert judges and the resulting consensus decision. The consensus threshold is determined through statistical confidence; see Appendix D for details.

**ZH** 图 4：单个 VAB 标注任务的示例，展示呈现给专家评审的候选集以及由此产生的共识决策。共识阈值依据统计置信度确定，详见附录 D。

**EN** Consensus filter. A task is retained only if expert votes are sufficiently concentrated. For ⟦SLOT_63⟧, the best-image votes must meet the threshold; for ⟦SLOT_64⟧, the best-image and worst-image votes must both meet it, so satisfying only one is insufficient. The thresholds are chosen by statistical confidence under a uniform-random null, and the exact derivation and threshold table are provided in Appendix D.

**ZH** 共识过滤。只有当专家投票足够集中时，任务才被保留。对于 ⟦SLOT_63⟧，最优图像的票数须达到阈值；对于 ⟦SLOT_64⟧，最优图像与最差图像的票数都须达到阈值，仅满足其一并不充分。阈值依据均匀随机零假设下的统计置信度选定，精确推导与阈值表见附录 D。

**EN** 4 Experiments

**ZH** 4 实验

**EN** 4.1 Setup

**ZH** 4.1 设置

**EN** Evaluation scope. We evaluate 20 MLLMs and six reward models on VAB. Unless otherwise noted, each model is evaluated under its default inference configuration.

**ZH** 评测范围。我们在 VAB 上评测 20 个 MLLM 与六个奖励模型。除特别说明外，每个模型均按其默认推理配置评测。

**EN** We compare all systems against two baselines. The Human Expert baseline is obtained from a fresh round of annotation in which 10 expert judges evaluate each released task under the benchmark interface, and we report their average accuracy against the released labels. The Random Guess baseline is computed analytically for each task size ⟦SLOT_65⟧.

**ZH** 我们把所有系统与两条基线对比。人类专家基线来自新一轮标注：10 位专家评审在基准界面下评测每个已发布任务，我们报告其相对于已发布标签的平均准确率。随机猜测基线则针对每个任务规模 ⟦SLOT_65⟧ 解析计算得到。

**EN** MLLMs.

**ZH** MLLM。

**EN** Our MLLM evaluation covers 20 closed-source and open-weight models spanning the Claude family (Anthropic, 2026a, Anthropic, 2025a, Anthropic, 2026b, Anthropic, 2025b, Anthropic, 2026c), the Gemini family (Google DeepMind, 2025a, Google DeepMind, 2025c, Google DeepMind, 2026), GPT and o-series models (OpenAI, 2025a, OpenAI, 2025e, OpenAI, 2025c, OpenAI, 2025b, OpenAI, 2025d, OpenAI, 2025f), and additional systems from Doubao, Grok, GLM, Kimi, and Qwen (ByteDance Seed, 2026, xAI, 2025, Z.ai, 2025, Team et al., 2026, Bai et al., 2023, Qwen Team, 2026). For each task, the model selects either the best image (Top-1) or both the best and worst images (TB-1). We evaluate each task three times under independent random permutations of candidate order and report ap@1 and pass^3 as defined in Section 3. Prompts are provided in Appendix H.3.

**ZH** 我们的 MLLM 评测覆盖 20 个闭源与开源权重模型，涵盖 Claude 系列（Anthropic，2026a、2025a、2026b、2025b、2026c）、Gemini 系列（Google DeepMind，2025a、2025c、2026）、GPT 与 o 系列模型（OpenAI，2025a、2025e、2025c、2025b、2025d、2025f），以及来自 Doubao、Grok、GLM、Kimi 与 Qwen 的其他系统（ByteDance Seed，2026；xAI，2025；Z.ai，2025；Team 等，2026；Bai 等，2023；Qwen Team，2026）。对于每个任务，模型要么选出最优图像（Top-1），要么同时选出最优与最差图像（TB-1）。我们在候选顺序的独立随机排列下把每个任务评测三次，并按第 3 节的定义报告 ap@1 与 pass^3。提示见附录 H.3。

**EN** Reward Models.

**ZH** 奖励模型。

**EN** We additionally evaluate six reward models: ArtiMuse (Cao et al., 2025), PEAS-aes and PEAS-ava (Yun and Choo, 2024), Q-Align (Wu et al., 2023), Q-Instruct (Wu et al., 2024), and RealQA-ava (Li et al., 2025). Unlike MLLMs, these models assign scalar scores to images independently rather than selecting directly from a set. We therefore follow each model’s official scoring interface, score each image three times, average the scores, and then rank images within each task. The main text reports Top-1 and TB-1; model-specific scoring interfaces and full result tables, including Bot-1 and topic-level breakdowns, are deferred to Appendix H.4, Appendix E.2, and Appendix E.4.

**ZH** 我们还评测了六个奖励模型：ArtiMuse（Cao 等，2025）、PEAS-aes 与 PEAS-ava（Yun 与 Choo，2024）、Q-Align（Wu 等，2023）、Q-Instruct（Wu 等，2024）以及 RealQA-ava（Li 等，2025）。与 MLLM 不同，这些模型独立地为图像赋予标量分数，而非直接从候选集中选择。因此我们遵循各模型官方的评分接口，对每张图像评分三次并取平均，再在任务内排序。正文报告 Top-1 与 TB-1；各模型的评分接口以及包含 Bot-1 与主题级细分的完整结果表见附录 H.4、E.2 与 E.4。

**EN** 4.2 Results

**ZH** 4.2 结果

**EN** Tables 4 and 5 summarize the main results; Appendices E.1–E.4 provide the full tables, topic-level breakdowns, and auxiliary metrics.

**ZH** 表 4 与表 5 汇总了主要结果；附录 E.1–E.4 给出完整表格、主题级细分与辅助指标。

**EN** 4.2.1 Results for Multimodal Large Language Models

**ZH** 4.2.1 多模态大语言模型的结果

**EN** Table 4: Main VAB results for 20 frontier MLLMs. We report Top-1 and TB-1 accuracy under both ap@1 and pass^3 (%). Best result in each column is shown in bold.

**ZH** 表 4：20 个前沿 MLLM 在 VAB 上的主要结果。我们报告 ap@1 与 pass^3 下 Top-1 与 TB-1 的准确率（%）。每列最优结果以粗体显示。

<!-- [原子块 · table] Overall Fine Art Illustration Photography Top-1 TB-1 Top-1 TB-1 Top-1 TB-1 Top-1 TB-1 Model ap@1 p^3 ap@1 p^3 ap@1 p^3 ap@1 p^3 ap@1 p^3 ap@1 p^3 ap@1 p^3 ap@1 p^3 Random Guess 37.2 6.6 27.5 5.3 41.0  -->

**EN** Gap to experts. Current frontier models remain far below expert performance. On the strictest metric, TB-1 pass^3, Claude Sonnet 4.6 attains 26.5%, against 68.9% for human experts; even under the more lenient TB-1 ap@1, the strongest model, Doubao Seed 2.0 Pro, reaches 42.8%, still 26.1 points short of the expert baseline.

**ZH** 与专家的差距。当前前沿模型仍远低于专家水平。在最严格的指标 TB-1 pass^3 上，Claude Sonnet 4.6 达到 26.5%，而人类专家为 68.9%；即使在较宽松的 TB-1 ap@1 下，最强的 Doubao Seed 2.0 Pro 也只达到 42.8%，仍比专家基线低 26.1 个百分点。

**EN** Progress across families. Improvements are uneven across model families. Claude Sonnet 4.6 nearly doubles its predecessor on TB-1 pass^3 (14.5% ⟦SLOT_66⟧ 26.5%), whereas the GPT-5 series regresses from 21.8% (GPT-5) to 20.0% (GPT-5.1) and 15.5% (GPT-5.2). A clear closed/open gap persists under the stricter metric: the strongest open-weight system, Qwen3.5-397B-A17B, reaches 17.2% on TB-1 pass^3, compared with 26.5% for Claude Sonnet 4.6.

**ZH** 各系列的进展。不同模型系列的提升并不均衡。Claude Sonnet 4.6 在 TB-1 pass^3 上几乎比其前代翻倍（14.5% ⟦SLOT_66⟧ 26.5%），而 GPT-5 系列则从 21.8%（GPT-5）回落到 20.0%（GPT-5.1）与 15.5%（GPT-5.2）。在更严格的指标下，闭源与开源之间仍存在明显差距：最强的开源权重系统 Qwen3.5-397B-A17B 在 TB-1 pass^3 上为 17.2%，而 Claude Sonnet 4.6 为 26.5%。

**EN** Domain difficulty and stability. Accuracy varies strongly across domains and across repeated evaluations. Illustration is the most difficult domain, where Claude Sonnet 4.6 attains only 19.0% on TB-1 pass^3, while photography is comparatively more tractable, with o4-mini reaching 30.2%. The large ap@1-to-pass^3 gap—for example, GLM-4.6V drops from 34.1% to 11.5% on TB-1—indicates that sensitivity to candidate order and response instability remain major failure modes.

**ZH** 领域难度与稳定性。准确率在不同领域与重复评测之间波动很大。插画是最难的领域，Claude Sonnet 4.6 在 TB-1 pass^3 上仅为 19.0%；摄影相对更易处理，o4-mini 达到 30.2%。ap@1 与 pass^3 之间的巨大落差——例如 GLM-4.6V 在 TB-1 上从 34.1% 跌到 11.5%——说明对候选顺序的敏感与响应不稳定仍是主要失效模式。

**EN** 4.2.2 Results for Reward Models

**ZH** 4.2.2 奖励模型的结果

**EN** Table 5: Main reward-model results on VAB. We report overall and domain-level Top-1 and TB-1 accuracy (%). Best non-baseline result in each column is shown in bold.

**ZH** 表 5：奖励模型在 VAB 上的主要结果。我们报告整体与领域级的 Top-1 与 TB-1 准确率（%）。每列非基线的最优结果以粗体显示。

<!-- [原子块 · table] Overall Fine Art Illustration Photography Model Top-1 TB-1 Top-1 TB-1 Top-1 TB-1 Top-1 TB-1 Random Guess 37.2 27.5 41.0 36.0 31.5 19.2 36.8 23.7 Human Expert 77.7 68.9 80.4 74.7 70.3 54.4 79.9 72.4 Ar -->

**EN** Overall performance. Reward models also remain well below human experts, although some are competitive with MLLMs on Top-1. Q-Align is the strongest overall, reaching 52.2% on Top-1 and 38.2% on TB-1, against 77.7% and 68.9% for the human baseline.

**ZH** 整体表现。奖励模型同样远低于人类专家，不过其中一些在 Top-1 上可与 MLLM 竞争。Q-Align 整体最强，Top-1 达 52.2%，TB-1 达 38.2%，而人类基线分别为 77.7% 与 68.9%。

**EN** Domain trends and asymmetric failure modes. Domain trends broadly mirror the MLLM results. Appendix E.2 additionally reveals an asymmetry between best and worst predictions: Q-Instruct reaches 51.5% on overall Bot-1 and 77.0% on photography Bot-1, despite considerably weaker Top-1 scores of 38.5% overall and 43.9% in photography. This pattern suggests that detecting aesthetic failure is in some cases easier than identifying the strongest image in a set.

**ZH** 领域趋势与非对称失效模式。领域趋势大体与 MLLM 结果一致。附录 E.2 还揭示了最优预测与最差预测之间的不对称性：Q-Instruct 在整体 Bot-1 上达到 51.5%，在摄影 Bot-1 上达到 77.0%，但它的 Top-1 明显更弱（整体 38.5%，摄影 43.9%）。这一模式说明，在某些情况下察觉审美上的失败比找出候选集中最强的图像更容易。

**EN** Comparison with MLLMs. The best reward-model Top-1 result , 52.2%, is numerically close to the best MLLM Top-1 ap@1 result , 55.4%, but the comparison is not strictly like-for-like: MLLMs make a single comparative decision over a candidate set, whereas reward models score images independently and are then ranked within the set.

**ZH** 与 MLLM 的比较。最优奖励模型的 Top-1 结果（52.2%）在数值上接近最优 MLLM 的 Top-1 ap@1 结果（55.4%），但这一比较并非严格对等：MLLM 是在候选集上做一次比较决策，而奖励模型先独立为各图像打分，再在集合内排序。

**EN** 4.3 Ablations and Additional Analysis

**ZH** 4.3 消融与补充分析

**EN** Temperature ablation. For models with an exposed temperature parameter, greedy decoding improves Top-1 pass^3 by 1.1 points on average and TB-1 pass^3 by 2.3 points. Decoding stochasticity therefore contributes noise, but it does not explain the main performance gap; full model-by-model results are reported in Appendix E.5.

**ZH** 温度消融。对于暴露温度参数的模型，贪心解码使 Top-1 pass^3 平均提升 1.1 个百分点，TB-1 pass^3 提升 2.3 个百分点。解码随机性因而会引入噪声，但不足以解释主要的性能差距；逐模型的完整结果见附录 E.5。

**EN** Candidate set size. Performance degrades sharply as the candidate set grows. Under TB-1 pass^3, the best model falls from 47.3% on two-image tasks to 6.7% on four-image tasks, while human experts decline from 87.1% to 43.6%. Larger candidate sets therefore amplify both comparative difficulty and instability; the full breakdown is reported in Appendix E.6.

**ZH** 候选集规模。随着候选集增大，性能急剧下降。在 TB-1 pass^3 下，最优模型从两图像任务的 47.3% 降到四图像任务的 6.7%，而人类专家从 87.1% 降到 43.6%。更大的候选集因此同时放大了比较难度与不稳定性；完整细分见附录 E.6。

**EN** 5 Fine-Tuning on Expert Aesthetic Judgments

**ZH** 5 在专家审美判断上微调

**EN** Training Setup.

**ZH** 训练设置。

**EN** We fine-tune Qwen3.5-35B-A3B using Low-Rank Adaptation (LoRA) (Hu et al., 2022) with rank 64 and ⟦SLOT_67⟧, freezing the vision tower while updating the multimodal projector. Supervision comes from 2,000 additional expert-annotated examples collected with the same annotation pipeline described in Section 3.3; these examples are fully disjoint from the benchmark evaluation set. We train for three epochs with a learning rate of ⟦SLOT_68⟧ and cosine scheduling. Additional hyperparameters and full fine-tuning results are provided in Appendix G. The fine-tuned model is denoted as Kallisti-35B-A3B.

**ZH** 我们使用低秩适配（LoRA）（Hu 等，2022）对 Qwen3.5-35B-A3B 做微调，秩为 64、⟦SLOT_67⟧，冻结视觉塔并更新多模态投影器。监督信号来自 2,000 条额外的专家标注样本，这些样本用第 3.3 节所述的同一标注流程收集，与基准评测集完全不相交。我们训练三个周期，学习率为 ⟦SLOT_68⟧，采用余弦调度。更多超参数与完整微调结果见附录 G。微调后的模型记为 Kallisti-35B-A3B。

**EN** Table 6: Fine-tuning results on VAB. We compare open-weight baselines with Kallisti-35B-A3B, which is obtained by LoRA fine-tuning on 2,000 expert-annotated training examples. All models are evaluated under their default inference configuration. Best result in each column is shown in bold.

**ZH** 表 6：VAB 上的微调结果。我们把开源权重基线与 Kallisti-35B-A3B 对比，后者通过在 2,000 条专家标注训练样本上做 LoRA 微调得到。所有模型均在其默认推理配置下评测。每列最优结果以粗体显示。

<!-- [原子块 · table] Top-1 TB-1 Model ap@1 p^3 ap@1 p^3 Open-Weight Models GLM-4.6V 43.0 17.5 34.1 11.5 Kimi-K2.5 49.4 26.8 36.8 15.0 Qwen3-VL-235B-A22B 44.9 20.5 35.2 14.0 Qwen3.5-397B-A17B 50.1 29.8 38.9 17.2 Ours Qwen3 -->

**EN** Improvement over the base model.

**ZH** 相对基座模型的提升。

**EN** Table 6 compares Kallisti-35B-A3B against its base model and a set of open-weight baselines. Fine-tuning yields consistent gains across all four reported metrics: Top-1 pass^3 improves from 25.5% to 29.5%, TB-1 pass^3 from 15.8% to 17.5%, Top-1 ap@1 from 47.5% to 51.3%, and TB-1 ap@1 from 36.5% to 38.8%. The topic-level breakdown is reported in Appendix G.2.

**ZH** 表 6 把 Kallisti-35B-A3B 与其基座模型及一组开源权重基线对比。微调在四项指标上均带来一致增益：Top-1 pass^3 从 25.5% 提升到 29.5%，TB-1 pass^3 从 15.8% 到 17.5%，Top-1 ap@1 从 47.5% 到 51.3%，TB-1 ap@1 从 36.5% 到 38.8%。主题级细分见附录 G.2。

**EN** Scaling implication.

**ZH** 规模上的启示。

**EN** Kallisti-35B-A3B approaches the substantially larger Qwen3.5-397B-A17B on Top-1 pass^3, 29.5% versus 29.8%, and lies within roughly one point on the other metrics. This is preliminary evidence that the comparative supervision in VAB carries enough aesthetic signal to compensate for an order-of-magnitude reduction in parameter count under lightweight adaptation.

**ZH** Kallisti-35B-A3B 在 Top-1 pass^3 上逼近规模大得多的 Qwen3.5-397B-A17B（29.5% 对 29.8%），在其他指标上也落在约一个百分点之内。这是初步证据，表明 VAB 中的比较监督蕴含足够的审美信号，可以在轻量适配下弥补参数量一个数量级的削减。

**EN** 6 Conclusion

**ZH** 6 结论

**EN** We introduced VAB, a benchmark that recasts aesthetic evaluation as comparative selection over candidate sets with matched subject matter, with labels grounded in expert ranking rather than scalar scoring. VAB contains 400 tasks and 1,195 images spanning fine art, photography, and illustration. A controlled human study motivates the protocol: direct ranking yields 42 percentage points higher inter-annotator agreement than score-derived rankings. Across 20 frontier MLLMs and six reward models, the strongest system reaches 26.5% on TB-1 pass^3 against 68.9% for human experts, and accuracy drops sharply as the candidate set grows; models also exhibit pronounced positional instability across permutations of the candidate order. Fine-tuning a 35B-parameter model on 2,000 expert examples brings its accuracy close to that of a 397B-parameter open-weight model, suggesting that expert comparative supervision transfers efficiently with lightweight adaptation. We see several directions for future work: broadening domain and annotator diversity beyond the present three domains, improving robustness to candidate-order permutations, and scaling expert comparative supervision to larger training corpora. By making expert aesthetic judgment a measurable, comparative target, VAB establishes the foundation on which expert-aligned multimodal aesthetic judgment can now be systematically pursued.

**ZH** 我们提出 VAB，一个把审美评测重构为在主体内容一致的候选集上做比较选择、并以专家排序而非标量评分作为标签依据的基准。VAB 包含 400 个任务与 1,195 张图像，涵盖美术、摄影与插画。一项控制实验为该流程提供了依据：直接排序带来的标注者间一致性比分数导出排序高出 42 个百分点。在 20 个前沿 MLLM 与六个奖励模型上，最强系统在 TB-1 pass^3 上仅达 26.5%，人类专家为 68.9%；准确率随候选集增大而急剧下降，模型在候选顺序的不同排列下还表现出明显的位置不稳定。在 2,000 条专家样本上微调一个 35B 参数模型，可使其准确率接近 397B 参数的开源权重模型，说明专家比较监督在轻量适配下迁移效率很高。我们看到的未来方向包括：在现有三个领域之外拓展领域与标注者多样性，提升对候选顺序排列的鲁棒性，以及把专家比较监督扩展到更大规模的训练语料。通过把专家审美判断变成可度量、可比较的目标，VAB 为系统推进与专家对齐的多模态审美判断奠定了基础。

**EN** Ethics Statement

**ZH** 伦理声明

**EN** This study involved human participants providing aesthetic judgments through an online evaluation platform. The University of Washington Human Subjects Division (HSD) reviewed the protocol and determined that the research qualifies as exempt human subjects research (Category 2 and 3; minimal-risk behavioral research) under U.S. federal regulations. Participation was voluntary and participants could stop at any time. No sensitive personal information was collected. Only aggregated benchmark results are publicly released, and no identifiable participant data are included in any publications or datasets. The exempt determination letter is on file with the authors.

**ZH** 本研究涉及通过在线评测平台提供审美判断的人类参与者。华盛顿大学人体受试者部门（HSD）审查了该流程，认定本研究符合美国联邦法规下的豁免人体受试者研究（第 2 类与第 3 类；最小风险行为研究）。参与为自愿性质，参与者可随时退出。未收集敏感个人信息。只公开发布聚合后的基准结果，任何出版物或数据集中均不含可识别参与者身份的数据。豁免认定函由作者存档备查。

**EN** All fine art works were created as commissioned works for VAB, with participating artists informed of and consenting to the use of their work for research. Professional photographers whose images served as source material for the photography pipeline contributed their work under appropriate licensing terms. Agent-edited variants derived from these source photographs were produced within the scope of those agreements. Illustration sets generated through text-to-image models used structured prompts without reproducing copyrighted material, and 3D-rendered sets were constructed exclusively from CC0-licensed assets. We are committed to crediting and fairly compensating all human creators whose work contributed to this benchmark.

**ZH** 所有美术作品均为 VAB 委托创作，参与艺术家已被告知其作品用于研究并表示同意。作为摄影流程素材来源的专业摄影师，其作品按适当的许可条款提供。由这些源照片派生的智能体编辑变体在上述协议范围内制作。通过文生图模型生成的插画候选集使用结构化提示，不复制受版权保护的材料；三维渲染候选集则完全由 CC0 许可资产构建。我们承诺对所有为本基准作出贡献的人类创作者给予署名与合理报酬。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] Adobe (2026a) Adobe Adobe Lightroom . Note: Adobe Website External Links: Link Cited by: §B.3 . -->

<!-- [原子块 · verbatim] Adobe (2026b) Adobe Adobe Photoshop . Note: Adobe Website External Links: Link Cited by: §B.3 . -->

<!-- [原子块 · verbatim] Alayrac et al. (2022) J. Alayrac, J. Donahue, P. Luc, A. Miech, I. Barr, Y. Hasson, K. Lenc, A. Mensch, K. Millican, M. Reynolds, et al. Flamingo: a visual language model for few-shot learning . Advan -->

<!-- [原子块 · verbatim] Anthropic (2025a) Anthropic Introducing Claude Opus 4.5 . Note: Anthropic News External Links: Link Cited by: §4.1 . -->

<!-- [原子块 · verbatim] Anthropic (2025b) Anthropic Introducing Claude Sonnet 4.5 . Note: Anthropic News External Links: Link Cited by: §4.1 . -->

<!-- [原子块 · verbatim] Anthropic (2026a) Anthropic Introducing Claude Haiku 4.5 . Note: Anthropic News External Links: Link Cited by: §4.1 . -->

<!-- [原子块 · verbatim] Anthropic (2026b) Anthropic Introducing Claude Opus 4.6 . Note: Anthropic News External Links: Link Cited by: §4.1 . -->

<!-- [原子块 · verbatim] Anthropic (2026c) Anthropic Introducing Claude Sonnet 4.6 . Note: Anthropic News External Links: Link Cited by: §4.1 . -->

<!-- [原子块 · verbatim] Bai et al. (2023) J. Bai, S. Bai, Y. Chu, Z. Cui, K. Dang, X. Deng, Y. Fan, W. Ge, Y. Han, F. Huang, et al. Qwen technical report . arXiv preprint arXiv:2309.16609 . Cited by: §4.1 . -->

<!-- [原子块 · verbatim] Bonferroni (1936) C. Bonferroni Teoria statistica delle classi e calcolo delle probabilita . Pubblicazioni del R istituto superiore di scienze economiche e commericiali di firenze 8 , pp. 3–62 . Cited -->

<!-- [原子块 · verbatim] ByteDance Seed (2026) ByteDance Seed SEED2 . Note: ByteDance Seed Website External Links: Link Cited by: §4.1 . -->

<!-- [原子块 · verbatim] Cao et al. (2025) S. Cao, N. Ma, J. Li, X. Li, L. Shao, K. Zhu, Y. Zhou, Y. Pu, J. Wu, J. Wang, et al. Artimuse: Fine-grained image aesthetics assessment with joint scoring and expert-level understand -->

<!-- [原子块 · verbatim] Creative Commons (2009) Creative Commons CC0 1.0 Universal . Note: Creative Commons Website External Links: Link Cited by: §B.3 . -->

<!-- [原子块 · verbatim] Dai et al. (2023) W. Dai, J. Li, D. Li, A. Tiong, J. Zhao, W. Wang, B. Li, P. N. Fung, and S. Hoi Instructblip: Towards general-purpose vision-language models with instruction tuning . Advances in neu -->

<!-- [原子块 · verbatim] Fagerland et al. (2013) M. W. Fagerland, S. Lydersen, and P. Laake The McNemar test for binary matched-pairs data: mid-p and asymptotic are better than exact conditional . BMC medical research methodo -->

<!-- [原子块 · verbatim] Goldman (1995) A. H. Goldman Aesthetic Value . Westview Press . Cited by: §2 . -->

<!-- [原子块 · verbatim] Google DeepMind (2025a) Google DeepMind Gemini 3 Flash . Note: Google DeepMind Model Card External Links: Link Cited by: §4.1 . -->

<!-- [原子块 · verbatim] Google DeepMind (2025b) Google DeepMind Gemini 3 Pro Image (Nano Banana Pro) . Note: Google DeepMind Model Card External Links: Link Cited by: §B.3 . -->

<!-- [原子块 · verbatim] Google DeepMind (2025c) Google DeepMind Gemini 3 Pro . Note: Google DeepMind Model Card External Links: Link Cited by: §4.1 . -->

<!-- [原子块 · verbatim] Google DeepMind (2026) Google DeepMind Gemini 3.1 Pro . Note: Google DeepMind Model Card External Links: Link Cited by: §4.1 . -->

<!-- [原子块 · verbatim] He et al. (2023) S. He, A. Ming, Y. Li, J. Sun, S. Zheng, and H. Ma Thinking image color aesthetics assessment: Models, datasets and benchmarks . In Proceedings of the IEEE/CVF International Conferenc -->

<!-- [原子块 · verbatim] He et al. (2022) S. He, Y. Zhang, R. Xie, D. Jiang, and A. Ming Rethinking Image Aesthetics Assessment: Models, Datasets and Benchmarks. . In IJCAI , Vol. 6 , pp. 22 . Cited by: Appendix A , §1 , §2 , -->

<!-- [原子块 · verbatim] Hosu et al. (2019) V. Hosu, B. Goldlucke, and D. Saupe Effective aesthetics prediction with multi-level spatially pooled features . In proceedings of the IEEE/CVF conference on computer vision and pat -->

<!-- [原子块 · verbatim] Hu et al. (2022) E. J. Hu, Y. Shen, P. Wallis, Z. Allen-Zhu, Y. Li, S. Wang, L. Wang, W. Chen, et al. Lora: Low-rank adaptation of large language models. . Iclr 1 ( 2 ), pp. 3 . Cited by: §5 . -->

<!-- [原子块 · verbatim] Huang et al. (2024a) Y. Huang, X. Sheng, Z. Yang, Q. Yuan, Z. Duan, P. Chen, L. Li, W. Lin, and G. Shi Aesexpert: Towards multi-modality foundation model for image aesthetics perception . In Proceedin -->

<!-- [原子块 · verbatim] Huang et al. (2024b) Y. Huang, Q. Yuan, X. Sheng, Z. Yang, H. Wu, P. Chen, Y. Yang, L. Li, and W. Lin Aesbench: An expert benchmark for multimodal large language models on image aesthetics perception  -->

<!-- [原子块 · verbatim] Kendall and Smith (1939) M. G. Kendall and B. B. Smith The problem of m rankings . The annals of mathematical statistics 10 ( 3 ), pp. 275–287 . Cited by: §F.7 . -->

<!-- [原子块 · verbatim] Kendall (1938) M. G. Kendall A new measure of rank correlation . Biometrika 30 ( 1-2 ), pp. 81–93 . Cited by: §F.1 , 1st item . -->

<!-- [原子块 · verbatim] Kong et al. (2016) S. Kong, X. Shen, Z. Lin, R. Mech, and C. Fowlkes Photo aesthetics ranking network with attributes and content adaptation . In European conference on computer vision , pp. 662–679 . -->

<!-- [原子块 · verbatim] Lee and Kim (2019) J. Lee and C. Kim Image aesthetic assessment based on pairwise comparison a unified approach to score regression, binary classification, and personalization . In Proceedings of the  -->

<!-- [原子块 · verbatim] Levinson (2005) J. Levinson The Oxford handbook of aesthetics . Oxford University Press . Cited by: §2 . -->

<!-- [原子块 · verbatim] Li et al. (2023) J. Li, D. Li, S. Savarese, and S. Hoi Blip-2: Bootstrapping language-image pre-training with frozen image encoders and large language models . In International conference on machine l -->

<!-- [原子块 · verbatim] Li et al. (2025) M. Li, R. Wang, L. Sun, Y. Bai, and X. Chu Next token is enough: Realistic image quality and aesthetic scoring with multimodal large language model . arXiv preprint arXiv:2503.06141 . -->

<!-- [原子块 · verbatim] Liu et al. (2023) H. Liu, C. Li, Q. Wu, and Y. J. Lee Visual instruction tuning . Advances in neural information processing systems 36 , pp. 34892–34916 . Cited by: Appendix A , §1 . -->

<!-- [原子块 · verbatim] Ma et al. (2017) S. Ma, J. Liu, and C. Wen Chen A-lamp: Adaptive layout-aware multi-patch deep convolutional neural network for photo aesthetic assessment . In Proceedings of the IEEE conference on co -->

<!-- [原子块 · verbatim] McNemar (1947) Q. McNemar Note on the sampling error of the difference between correlated proportions or percentages . Psychometrika 12 ( 2 ), pp. 153–157 . Cited by: §F.6 , §2 , Table 2 , Table 2 . -->

<!-- [原子块 · verbatim] Midjourney (2026) Midjourney Version . Note: Midjourney Documentation External Links: Link Cited by: §B.3 . -->

<!-- [原子块 · verbatim] Murray et al. (2012) N. Murray, L. Marchesotti, and F. Perronnin AVA: A large-scale database for aesthetic visual analysis . In 2012 IEEE conference on computer vision and pattern recognition , pp. 24 -->

<!-- [原子块 · verbatim] OpenAI (2025a) OpenAI GPT-4.1 . Note: OpenAI API Documentation External Links: Link Cited by: §4.1 . -->

<!-- [原子块 · verbatim] OpenAI (2025b) OpenAI GPT-5.1 Codex . Note: OpenAI API Documentation External Links: Link Cited by: §4.1 . -->

<!-- [原子块 · verbatim] OpenAI (2025c) OpenAI Introducing GPT-5.1 . Note: OpenAI Website External Links: Link Cited by: §4.1 . -->

<!-- [原子块 · verbatim] OpenAI (2025d) OpenAI Introducing GPT-5.2 . Note: OpenAI Website External Links: Link Cited by: §4.1 . -->

<!-- [原子块 · verbatim] OpenAI (2025e) OpenAI Introducing GPT-5 . Note: OpenAI Website External Links: Link Cited by: §B.3 , §4.1 . -->

<!-- [原子块 · verbatim] OpenAI (2025f) OpenAI o4-mini . Note: OpenAI API Documentation External Links: Link Cited by: §4.1 . -->

<!-- [原子块 · verbatim] Parducci (1965) A. Parducci Category judgment: a range-frequency model. . Psychological review 72 ( 6 ), pp. 407 . Cited by: §2 . -->

<!-- [原子块 · verbatim] PixelLab (2026) PixelLab PixelLab . Note: PixelLab Website External Links: Link Cited by: §B.3 . -->

<!-- [原子块 · verbatim] Qi et al. (2025) D. Qi, H. Zhao, J. Shi, S. Jenni, Y. Fan, F. Dernoncourt, S. Cohen, and S. Li The Photographer’s Eye: Teaching Multimodal Large Language Models to See, and Critique Like Photographers -->

<!-- [原子块 · verbatim] Qwen Team (2026) Qwen Team Qwen3.5 . Note: Qwen Blog External Links: Link Cited by: §4.1 . -->

<!-- [原子块 · verbatim] Shannon (1948) C. E. Shannon A mathematical theory of communication . The Bell system technical journal 27 ( 3 ), pp. 379–423 . Cited by: §F.1 , 3rd item , §2 , Table 3 , Table 3 . -->

<!-- [原子块 · verbatim] Sketchfab (2026) Sketchfab Sketchfab . Note: Sketchfab Website External Links: Link Cited by: §B.3 . -->

<!-- [原子块 · verbatim] Stewart et al. (2005) N. Stewart, G. D. Brown, and N. Chater Absolute identification by relative judgment. . Psychological review 112 ( 4 ), pp. 881 . Cited by: §2 . -->

<!-- [原子块 · verbatim] Sun et al. (2024) P. Sun, Y. Jiang, S. Chen, S. Zhang, B. Peng, P. Luo, and Z. Yuan Autoregressive model beats diffusion: Llama for scalable image generation . arXiv preprint arXiv:2406.06525 . Cited  -->

<!-- [原子块 · verbatim] Talebi and Milanfar (2018) H. Talebi and P. Milanfar NIMA: Neural image assessment . IEEE transactions on image processing 27 ( 8 ), pp. 3998–4011 . Cited by: Appendix A , §1 . -->

<!-- [原子块 · verbatim] Team et al. (2023) G. Team, R. Anil, S. Borgeaud, J. Alayrac, J. Yu, R. Soricut, J. Schalkwyk, A. M. Dai, A. Hauth, K. Millican, et al. Gemini: a family of highly capable multimodal models . arXiv pre -->

<!-- [原子块 · verbatim] Team et al. (2026) K. Team, T. Bai, Y. Bai, Y. Bao, S. Cai, Y. Cao, Y. Charles, H. Che, C. Chen, G. Chen, et al. Kimi K2. 5: Visual Agentic Intelligence . arXiv preprint arXiv:2602.02276 . Cited by: § -->

<!-- [原子块 · verbatim] Thurstone (1927) L. L. Thurstone A Law of Comparative Judgment . Psychological Review 34 ( 4 ), pp. 273–286 . External Links: Document Cited by: §2 . -->

<!-- [原子块 · verbatim] Wang et al. (2024) P. Wang, S. Bai, S. Tan, S. Wang, Z. Fan, J. Bai, K. Chen, X. Liu, J. Wang, W. Ge, et al. Qwen2-vl: Enhancing vision-language model’s perception of the world at any resolution . arX -->

<!-- [原子块 · verbatim] Wang et al. (2019) W. Wang, S. Yang, W. Zhang, and J. Zhang Neural aesthetic image reviewer . IET Computer Vision 13 ( 8 ), pp. 749–758 . Cited by: Appendix A . -->

<!-- [原子块 · verbatim] Wilcoxon (1945) F. Wilcoxon Individual comparisons by ranking methods . Biometrics bulletin 1 ( 6 ), pp. 80–83 . Cited by: §F.6 , §2 , Table 3 , Table 3 . -->

<!-- [原子块 · verbatim] Wilson (1927) E. B. Wilson Probable inference, the law of succession, and statistical inference . Journal of the American Statistical Association 22 ( 158 ), pp. 209–212 . Cited by: Table 3 , Table 3  -->

<!-- [原子块 · verbatim] Wu et al. (2024) H. Wu, Z. Zhang, E. Zhang, C. Chen, L. Liao, A. Wang, K. Xu, C. Li, J. Hou, G. Zhai, et al. Q-instruct: Improving low-level visual abilities for multi-modality foundation models . In  -->

<!-- [原子块 · verbatim] Wu et al. (2023) H. Wu, Z. Zhang, W. Zhang, C. Chen, L. Liao, C. Li, Y. Gao, A. Wang, E. Zhang, W. Sun, et al. Q-align: Teaching lmms for visual scoring via discrete text-defined levels . arXiv prepri -->

<!-- [原子块 · verbatim] xAI (2025) xAI Grok 4.1 Fast . Note: xAI News External Links: Link Cited by: §4.1 . -->

<!-- [原子块 · verbatim] Yang et al. (2022) Y. Yang, L. Xu, L. Li, N. Qie, Y. Li, P. Zhang, and Y. Guo Personalized image aesthetics assessment with rich attributes . In Proceedings of the IEEE/CVF Conference on Computer Visi -->

<!-- [原子块 · verbatim] Yi et al. (2023) R. Yi, H. Tian, Z. Gu, Y. Lai, and P. L. Rosin Towards artistic image aesthetics assessment: a large-scale dataset and a new method . In Proceedings of the IEEE/CVF Conference on Comp -->

<!-- [原子块 · verbatim] Yu et al. (2023) W. Yu, Z. Yang, L. Li, J. Wang, K. Lin, Z. Liu, X. Wang, and L. Wang Mm-vet: Evaluating large multimodal models for integrated capabilities . arXiv preprint arXiv:2308.02490 . Cited b -->

<!-- [原子块 · verbatim] Yue et al. (2024) X. Yue, Y. Ni, K. Zhang, T. Zheng, R. Liu, G. Zhang, S. Stevens, D. Jiang, W. Ren, Y. Sun, et al. Mmmu: A massive multi-discipline multimodal understanding and reasoning benchmark fo -->

<!-- [原子块 · verbatim] Yun and Choo (2024) J. Yun and J. Choo Scaling up personalized image aesthetic assessment via task vector customization . In European Conference on Computer Vision , pp. 323–339 . Cited by: §4.1 , Tab -->

<!-- [原子块 · verbatim] Z.ai (2025) Z.ai GLM-4.6V . Note: Z.ai Blog External Links: Link Cited by: §4.1 . -->

<!-- [原子块 · verbatim] Zhou et al. (2024a) H. Zhou, L. Tang, R. Yang, G. Qin, Y. Zhang, Y. Li, X. Li, R. Hu, and G. Zhai UniQA: Unified vision-language pre-training for image quality and aesthetic assessment . arXiv preprin -->

<!-- [原子块 · verbatim] Zhou et al. (2024b) Z. Zhou, Q. Wang, B. Lin, Y. Su, R. Chen, X. Tao, A. Zheng, L. Yuan, P. Wan, and D. Zhang Uniaa: A unified multi-modal image aesthetic assessment baseline and benchmark . arXiv pre -->

**EN** Appendix

**ZH** 附录

**EN** Appendix A Related Work

**ZH** 附录 A 相关工作

**EN** Multimodal Large Language Models.

**ZH** 多模态大语言模型。

**EN** Recent MLLMs such as Flamingo, BLIP-2, InstructBLIP, LLaVA, Gemini, and Qwen2-VL have rapidly improved multimodal perception, instruction following, and reasoning (Alayrac et al., 2022, Li et al., 2023, Dai et al., 2023, Liu et al., 2023, Team et al., 2023, Wang et al., 2024). Their capabilities are typically assessed on broad benchmarks such as MM-Vet and MMMU (Yu et al., 2023, Yue et al., 2024), where each example usually admits a single correct answer. Aesthetic judgment is different: it is comparative, convention-sensitive, and not reducible to factual correctness alone. Our focus is therefore whether frontier MLLMs can make stable, expert-aligned selections over candidate sets with matched subject matter rather than pointwise judgments on isolated images.

**ZH** 近年的 MLLM，如 Flamingo、BLIP-2、InstructBLIP、LLaVA、Gemini 与 Qwen2-VL，在多模态感知、指令遵循与推理方面迅速进步（Alayrac 等，2022；Li 等，2023；Dai 等，2023；Liu 等，2023；Team 等，2023；Wang 等，2024）。它们的能力通常在 MM-Vet、MMMU 等宽泛基准上评估（Yu 等，2023；Yue 等，2024），其中每个样例通常只有一个正确答案。审美判断不同：它是比较性的、对惯例敏感的，不能还原为单纯的事实正确性。因此我们的关注点在于，前沿 MLLM 能否在主体内容一致的候选集上做出稳定且与专家一致的选择，而非对孤立图像给出逐点判断。

**EN** Image Aesthetics Assessment.

**ZH** 图像美学评估。

**EN** Image aesthetics assessment (IAA) has traditionally been posed as single-image score prediction. Canonical datasets such as AVA and AADB provide large-scale photographic images with scalar ratings. Later resources extend this paradigm through comments, theme-aware labels, and personalization, including AVA-Reviews, TAD66K, and PARA (Murray et al., 2012, Kong et al., 2016, Wang et al., 2019, He et al., 2022, Yang et al., 2022). These resources support a broad line of regression and ranking models, including NIMA, A-Lamp, theme-aware predictors, and more recent vision-language scorers such as Q-Align and UniQA (Talebi and Milanfar, 2018, Ma et al., 2017, He et al., 2022, Wu et al., 2023, Zhou et al., 2024a). Still, the dominant setup remains pointwise, mapping from one image to a score, with preference order inferred only indirectly from independent estimates.

**ZH** 图像美学评估（IAA）传统上被表述为单图像分数预测。AVA、AADB 等经典数据集提供了带标量评分的大规模摄影图像。后续资源通过评论、主题感知标签与个性化扩展了这一范式，包括 AVA-Reviews、TAD66K 与 PARA（Murray 等，2012；Kong 等，2016；Wang 等，2019；He 等，2022；Yang 等，2022）。这些资源支撑了回归与排序模型的广阔研究线，包括 NIMA、A-Lamp、主题感知预测器，以及 Q-Align、UniQA 等较新的视觉语言打分器（Talebi 与 Milanfar，2018；Ma 等，2017；He 等，2022；Wu 等，2023；Zhou 等，2024a）。尽管如此，主流设置仍是逐点的——从一张图像映射到一个分数，偏好次序只能从独立估计中间接推断。

**EN** More recently, MLLM-based efforts have moved toward richer aesthetic reasoning. AesBench evaluates aesthetic perception in frontier MLLMs; AesExpert and UNIAA build instruction-tuned systems for critique and assessment; and ArtiMuse and the photography-focused The Photographer’s Eye move closer to expert-style analysis (Huang et al., 2024b, Huang et al., 2024a, Zhou et al., 2024b, Cao et al., 2025, Qi et al., 2025). Nevertheless, existing resources remain largely single-image, score-centric, or domain-specific. In contrast, VAB is explicitly set-based: each example is a group with matched subject matter, and the task is to identify the strongest and weakest images under controlled content. This formulation targets relative aesthetic discrimination directly, derives labels from expert consensus rather than crowd averages, and spans fine art, photography, and illustration within a unified benchmark.

**ZH** 更近期的基于 MLLM 的工作转向更丰富的审美推理。AesBench 评测前沿 MLLM 的审美感知；AesExpert 与 UNIAA 构建了面向评论与评估的指令微调系统；ArtiMuse 与聚焦摄影的 The Photographer’s Eye 则更接近专家式分析（Huang 等，2024b、2024a；Zhou 等，2024b；Cao 等，2025；Qi 等，2025）。尽管如此，现有资源仍大体上是单图像的、以分数为中心的或领域专属的。相比之下，VAB 明确基于集合：每个样例都是一个主体内容一致的图像组，任务是在受控内容下找出最强与最弱的图像。这一表述直接面向相对审美判别，标签来自专家共识而非众包平均，并在统一基准内涵盖美术、摄影与插画。

**EN** Appendix B Benchmark Details

**ZH** 附录 B 基准细节

**EN** B.1 Final Benchmark Statistics

**ZH** B.1 最终基准统计

**EN** Table 7 reports the final benchmark statistics after expert annotation and consensus filtering.

**ZH** 表 7 报告经专家标注与共识过滤后的最终基准统计。

**EN** Table 7: Final benchmark statistics for VAB by domain and topic after expert consensus filtering. T/I denotes the number of tasks and images.

**ZH** 表 7：经专家共识过滤后 VAB 按领域与主题划分的最终基准统计。T/I 表示任务数与图像数。

<!-- [原子块 · table] Fine Art (161/458) Photography (139/389) Illustration (100/348) Topic ​​T / I Topic ​​T / I Topic ​​T / I Landscape Color 56/243 Landscape 45/130 Digital & AI Art 23/84 Portrait Sketch 33/66 Street &  -->

**EN** Table 8 shows the candidate set size distribution in the final benchmark by domain, and Table 9 provides the corresponding topic-level breakdown.

**ZH** 表 8 给出最终基准中按领域划分的候选集规模分布，表 9 给出相应的主题级细分。

**EN** Table 8: Candidate set size distribution in the final benchmark by domain.

**ZH** 表 8：最终基准中按领域划分的候选集规模分布。

<!-- [原子块 · table] Domain k = 2 k=2 k = 3 k=3 k = 4 k=4 k = 5 k=5 k = 6 k=6 Fine Art 109 4 13 34 1 Photography 30 107 2 0 0 Illustration 26 0 74 0 0 Total 165 111 89 34 1 -->

**EN** Table 9: Topic-level breakdown of the final benchmark after expert consensus filtering.

**ZH** 表 9：经专家共识过滤后最终基准的主题级细分。

<!-- [原子块 · table] Domain Topic k = 2 k=2 k = 3 k=3 k = 4 k=4 k = 5 k=5 k = 6 k=6 Tasks Avg. k k Fine Art Calligraphy 11 0 0 0 0 11 2.00 Fine Art Chinese Painting 9 0 0 0 0 9 2.00 Fine Art Ink and Wash 4 0 0 0 0 4 2.00  -->

**EN** B.2 Raw Collection Statistics Before Expert Filtering

**ZH** B.2 专家过滤前的原始采集统计

**EN** Before expert filtering, the collected pool contains 1,367 tasks and 3,859 images. Table 10 summarizes the raw collection by domain, Table 11 reports the corresponding topic-level breakdown, and Table 12 further decomposes the photography subset by collection pipeline.

**ZH** 在专家过滤之前，采集池包含 1,367 个任务与 3,859 张图像。表 10 按领域汇总原始采集情况，表 11 报告相应的主题级细分，表 12 进一步按采集流程分解摄影子集。

**EN** Table 10: Raw collection statistics by domain before expert filtering.

**ZH** 表 10：专家过滤前按领域划分的原始采集统计。

<!-- [原子块 · table] Domain Tasks Images Avg. k k Fine Art 426 1,142 2.68 Photography 670 1,809 2.70 Illustration 271 908 3.35 Total 1,367 3,859 2.82 -->

**EN** Table 11: Topic-level raw collection statistics before expert filtering.

**ZH** 表 11：专家过滤前的主题级原始采集统计。

<!-- [原子块 · table] Domain Topic Tasks Images k = 2 k=2 k = 3 k=3 k = 4 k=4 k = 5 k=5 k = 6 k=6 Avg. k k Fine Art Landscape Color 113 502 12 6 20 70 5 4.44 Fine Art Portrait Sketch 93 186 93 0 0 0 0 2.00 Fine Art Still L -->

**EN** Table 12: Raw photography collection statistics by topic and collection pipeline before expert filtering. Agent-Edit and Expert-Edit denote task counts from the automated editing pipeline and the expert retouching pipeline, respectively.

**ZH** 表 12：专家过滤前按主题与采集流程划分的原始摄影采集统计。Agent-Edit 与 Expert-Edit 分别表示来自自动编辑流程与专家修图流程的任务数。

<!-- [原子块 · table] Topic Tasks Images k = 2 k=2 k = 3 k=3 k = 4 k=4 Avg. k k Agent-Edit Expert-Edit Landscape 280 761 81 197 2 2.72 188 92 Street and City 165 450 45 120 0 2.73 115 50 Architecture 157 420 51 106 0 2.68  -->

**EN** B.3 Data Construction Details

**ZH** B.3 数据构建细节

**EN** Fine Art.

**ZH** 美术。

**EN** We commissioned 426 painting sets comprising 1,142 images across nine fine-art topics: calligraphy, Chinese painting, ink and wash, landscape color, portrait color, portrait sketch, quick sketch, still-life color, and still-life sketch. For each topic, artists received constrained prompts that fixed the subject and high-level compositional requirements while allowing variation in execution. The resulting sets preserve semantic intent while differing in composition, value structure, color harmony, and paint handling. All works were commissioned specifically for VAB rather than drawn from existing collections, which reduces the risk of contamination from publicly indexed art. Before annotation, we remove near-duplicates and discard sets with semantic mismatches or trivial cues.

**ZH** 我们委托创作了 426 组绘画，共 1,142 张图像，涵盖书法、中国画、水墨、风景色彩、肖像色彩、肖像速写、快速速写、静物色彩与静物速写九个美术主题。每个主题的画家收到受限提示，这些提示固定主体与高层构图要求，同时允许在完成质量上有所变化。所得候选集保持语义意图一致，而在构图、明度结构、色彩和谐与用笔处理上彼此不同。所有作品均为 VAB 专门委托创作，而非取自现有收藏，这降低了来自公开索引艺术品的污染风险。标注前我们去除近似重复项，并丢弃存在语义不符或琐碎线索的候选集。

**EN** Photography.

**ZH** 摄影。

**EN** We constructed 670 photography sets comprising 1,809 images across nine topics: architecture, food and product, landscape, macro, night and astrophotography, portrait, sports, street and city, and wildlife. Each set originates from a single source photograph, many provided directly by professional photographers. We transform these source images into controlled comparison sets through two pipelines.

**ZH** 我们构建了 670 组摄影，共 1,809 张图像，涵盖建筑、美食与产品、风景、微距、夜景与天文摄影、人像、运动、街头与城市、野生动物九个主题。每组源自单张源照片，其中许多由专业摄影师直接提供。我们通过两条流程把这些源图像转换为受控的比较集。

**EN** In the expert-edit pipeline, photographers and retouchers improve each source image using tools such as Adobe Photoshop and Lightroom (Adobe, 2026b, Adobe, 2026a), applying recomposition, color and tone correction, and content-aware expansion. The original photograph and its improved variant form a pair. For a subset of source images, multiple experts independently edit the same photograph, yielding larger candidate sets with matched subject matter and varying aesthetic quality.

**ZH** 在专家编辑流程中，摄影师与修图师使用 Adobe Photoshop、Lightroom 等工具（Adobe，2026b、2026a）改进每张源图像，施加重新构图、色彩与影调校正以及内容感知扩展。原始照片与其改进变体构成一对。对于一部分源图像，多位专家独立编辑同一张照片，从而得到主体内容一致而美学质量各异的更大候选集。

**EN** In the agent-edit pipeline, each source image is first sent to a critic model, ArtiMuse (Cao et al., 2025), which produces a detailed aesthetic review. The review and the original image are then passed to a general-purpose MLLM, GPT-5 (OpenAI, 2025e), to generate two editing prompts: one for improvement and one for degradation. These prompts, together with the original image, are fed to an image-to-image model, Gemini-3-Pro-Image (Nano Banana Pro) (Google DeepMind, 2025b), to generate an improved and a degraded variant. The original, improved, and degraded images form a three-image candidate set. The exact prompt sequence is recorded in Appendix H.1.

**ZH** 在智能体编辑流程中，每张源图像先送到一个评判模型 ArtiMuse（Cao 等，2025），由其生成详细的审美评述。该评述与原图随后送入通用 MLLM GPT-5（OpenAI，2025e），生成两条编辑提示：一条用于改进，一条用于退化。这些提示连同原图一起送入图生图模型 Gemini-3-Pro-Image（Nano Banana Pro）（Google DeepMind，2025b），生成一个改进变体与一个退化变体。原图、改进图与退化图构成三图像的候选集。确切的提示序列记录于附录 H.1。

**EN** All photography sets from both pipelines are deduplicated and reviewed for semantic consistency before annotation.

**ZH** 两条流程得到的全部摄影候选集在标注前均经过去重与语义一致性审查。

**EN** Illustration.

**ZH** 插画。

**EN** We constructed 271 illustration sets comprising 908 images across six topics: anime and manga, comic, concept art, digital and AI art, pixel art, and stylized 3D. The sets are derived from two distinct sources, prompt-based generation and 3D asset rendering.

**ZH** 我们构建了 271 组插画，共 908 张图像，涵盖动画与漫画、漫画、概念艺术、数字与 AI 艺术、像素艺术、风格化三维六个主题。这些候选集来自两个不同来源：提示生成与三维资产渲染。

**EN** In the generative pipeline, each set originates from a structured prompt that specifies subject identity, scene context, composition, camera viewpoint, lighting, and stylistic attributes. For each set, the prompt is instantiated using a single text-to-image model, such as Midjourney v7 (Midjourney, 2026), Pixellab.ai (Create M-XL) (PixelLab, 2026), or LlamaGen (Sun et al., 2024), to generate candidate images with matched subject matter and varying aesthetic quality. The prompt templates are provided in Appendix H.2.

**ZH** 在生成流程中，每组源自一条结构化提示，该提示规定主体身份、场景情境、构图、相机视角、光照与风格属性。每组的提示用单一文生图模型实例化，如 Midjourney v7（Midjourney，2026）、Pixellab.ai（Create M-XL）（PixelLab，2026）或 LlamaGen（Sun 等，2024），以生成主体内容一致而美学质量各异的候选图像。提示模板见附录 H.2。

**EN** In the 3D-rendering pipeline, each set is constructed from CC0-licensed assets sourced from Sketchfab (Creative Commons, 2009, Sketchfab, 2026). For each asset, we render multiple images by varying camera viewpoint while keeping object identity, scene semantics, lighting, and background conditions fixed. The resulting renders form candidate sets with matched subject matter and controlled variation in composition and visual presentation.

**ZH** 在三维渲染流程中，每组由取自 Sketchfab 的 CC0 许可资产构建（Creative Commons，2009；Sketchfab，2026）。对于每个资产，我们通过改变相机视角渲染多张图像，同时固定物体身份、场景语义、光照与背景条件。所得渲染构成主体内容一致、构图与视觉呈现受控变化的候选集。

**EN** All illustration sets from both pipelines are deduplicated and reviewed for semantic consistency before annotation.

**ZH** 两条流程得到的全部插画候选集在标注前均经过去重与语义一致性审查。

**EN** Appendix C Annotation Details

**ZH** 附录 C 标注细节

**EN** C.1 Annotation Rubrics

**ZH** C.1 评判细则

**EN** The rubric serves as a structured comparison guide rather than a separate numerical scoring form. Judges assess each image against domain-specific criteria before making their final comparative selection. The rubrics below describe the criteria used for each domain.

**ZH** 细则充当结构化的比较指南，而非独立的数值评分表。评审在做出最终比较选择之前，先依据领域专属标准评估每张图像。下列细则描述了各领域使用的标准。

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

**EN** C.2 Annotation Interface

**ZH** C.2 标注界面

**EN** Figure 5 shows an example annotation interface used by expert judges.

**ZH** 图 5 展示了专家评审使用的标注界面示例。

<!-- [原子块 · img]  -->

**EN** Figure 5: The annotation interface presents all ⟦SLOT_69⟧ candidate images side by side. Judges first review each image with respect to the rubric criteria, then make a final comparative selection: selecting the best image for ⟦SLOT_70⟧ and selecting both the best and worst images for ⟦SLOT_71⟧.

**ZH** 图 5：标注界面并排呈现全部 ⟦SLOT_69⟧ 张候选图像。评审先依据细则标准逐一审阅图像，再做最终比较选择：⟦SLOT_70⟧ 下选出最优图像，⟦SLOT_71⟧ 下同时选出最优与最差图像。

**EN** Appendix D Ground Truth Mathematical Details

**ZH** 附录 D 真值数学细节

**EN** This appendix provides additional mathematical details for the consensus filter described in Section 3.3.

**ZH** 本附录给出第 3.3 节所述共识过滤的更多数学细节。

**EN** D.1 Selected Thresholds

**ZH** D.1 选定阈值

**EN** Table 13 reports the consensus thresholds used in the benchmark together with their corresponding null pass probabilities.

**ZH** 表 13 报告基准中使用的共识阈值及其对应的零假设通过概率。

**EN** Table 13: Consensus thresholds and corresponding null pass probabilities by candidate set size ⟦SLOT_72⟧, with ⟦SLOT_73⟧ judges per task.

**ZH** 表 13：按候选集规模 ⟦SLOT_72⟧ 划分的共识阈值与对应的零假设通过概率，每个任务 ⟦SLOT_73⟧ 位评审。

<!-- [原子块 · table] k k Threshold m m p accept ​ ( k , m ) p_{\mathrm{accept}}(k,m) 2 8 10.94% 3 7 0.88% 4 6 0.95% 5 6 0.15% 6 6 0.03% -->

**EN** D.2 Derivation of Null Pass Probabilities

**ZH** D.2 零假设通过概率的推导

**EN** For ⟦SLOT_74⟧ candidates with ⟦SLOT_75⟧ judges, each judge’s response is modeled as a directed edge ⟦SLOT_76⟧ (selecting image ⟦SLOT_77⟧ as best and image ⟦SLOT_78⟧ as worst, with ⟦SLOT_79⟧) drawn uniformly from ⟦SLOT_80⟧ possibilities. Let ⟦SLOT_81⟧ denote the count of judges choosing the pair ⟦SLOT_82⟧. The probability of any configuration ⟦SLOT_83⟧ under the random null is:

**ZH** 对于 ⟦SLOT_74⟧ 个候选与 ⟦SLOT_75⟧ 位评审，每位评审的响应建模为一条有向边 ⟦SLOT_76⟧（选出图像 ⟦SLOT_77⟧ 为最优、图像 ⟦SLOT_78⟧ 为最差，且 ⟦SLOT_79⟧），从 ⟦SLOT_80⟧ 种可能中均匀抽取。记 ⟦SLOT_81⟧ 为选择组合 ⟦SLOT_82⟧ 的评审人数。随机零假设下任意配置 ⟦SLOT_83⟧ 的概率为：

<!-- [原子块 · table] Pr ⁡ ( C ) = n ! ∏ i ≠ j c i ​ j ! ​ ( 1 k ⁡ ( k − 1 ) ) n . \Pr(C)=\frac{n!}{\prod_{i\neq j}c_{ij}!}\left(\frac{1}{k(k-1)}\right)^{n}. -->

**EN** The exact by-chance pass probability is computed by summing over all configurations satisfying the consensus threshold:

**ZH** 精确的偶然通过概率通过对所有满足共识阈值的配置求和得到：

<!-- [原子块 · table] p accept ( k , m ) = ∑ C : c i ​ i = 0 , ∑ i ≠ j c i ​ j = n n ! ∏ i ≠ j c i ​ j ! ( 1 k ⁡ ( k − 1 ) ) n ( max i B i ≥ m ) ( max j W j ≥ m ) , p_{\mathrm{accept}}(k,m)=\sum_{\begin{subarray}{c}C:\,c_{ -->

**EN** where ⟦SLOT_84⟧ (votes for ⟦SLOT_85⟧ as best) and ⟦SLOT_86⟧ (votes for ⟦SLOT_87⟧ as worst). The exact probabilities were computed by exhaustive enumeration over all valid count configurations ⟦SLOT_88⟧ satisfying ⟦SLOT_89⟧ and ⟦SLOT_90⟧, summing the multinomial probability mass over the configurations that satisfy the acceptance condition. For ⟦SLOT_91⟧, this acceptance condition is conjunctive: a task passes only if the best-vote threshold and the worst-vote threshold are both met, so satisfying only one of the two is insufficient.

**ZH** 其中 ⟦SLOT_84⟧（⟦SLOT_85⟧ 的最优票）与 ⟦SLOT_86⟧（⟦SLOT_87⟧ 的最差票）。精确概率通过对全部有效计数配置 ⟦SLOT_88⟧（满足 ⟦SLOT_89⟧ 与 ⟦SLOT_90⟧）穷举枚举，并对满足接受条件的配置求多项式概率质量之和得到。对于 ⟦SLOT_91⟧，该接受条件是合取的：任务只有在最优票阈值与最差票阈值同时满足时才通过，仅满足二者之一并不充分。

**EN** D.3 Monte Carlo Verification

**ZH** D.3 蒙特卡洛验证

**EN** We verify the exact probabilities via Monte Carlo simulation with ⟦SLOT_92⟧ samples per ⟦SLOT_93⟧ configuration. Table 14 compares the exact values from Table 13 against Monte Carlo estimates and reports 95% Wald confidence intervals.

**ZH** 我们以 ⟦SLOT_92⟧ 个样本的蒙特卡洛模拟验证上述精确概率，每个 ⟦SLOT_93⟧ 配置独立进行。表 14 把表 13 的精确值与蒙特卡洛估计对比，并报告 95% Wald 置信区间。

**EN** Table 14: Monte Carlo verification of null pass probabilities (⟦SLOT_94⟧ samples).

**ZH** 表 14：零假设通过概率的蒙特卡洛验证（⟦SLOT_94⟧ 个样本）。

<!-- [原子块 · table] k k m m Exact MC Estimate 95% CI 2 8 10.94% 10.9496% [10.9303%, 10.9690%] 3 7 0.88% 0.8818% [0.8760%, 0.8876%] 4 6 0.95% 0.9507% [0.9447%, 0.9567%] 5 6 0.15% 0.1489% [0.1465%, 0.1513%] 6 6 0.03% 0.030 -->

**EN** D.4 Special Case for Binary Tasks

**ZH** D.4 二值任务的特例

**EN** For binary tasks (⟦SLOT_95⟧), the worst image is implied once the best is selected. The consensus filter reduces to requiring ⟦SLOT_96⟧ where ⟦SLOT_97⟧:

**ZH** 对于二值任务（⟦SLOT_95⟧），一旦选出最优图像，最差图像即被确定。共识过滤退化为要求 ⟦SLOT_96⟧，其中 ⟦SLOT_97⟧：

<!-- [原子块 · table] p accept ​ ( 2 , m ) = Pr ⁡ ( B ≥ m ) + Pr ⁡ ( B ≤ n − m ) = 2 ​ ∑ b = m n ( n b ) ​ ( 1 2 ) n . p_{\mathrm{accept}}(2,m)=\Pr\!\left(B\geq m\right)+\Pr\!\left(B\leq n-m\right)=2\sum_{b=m}^{n}\binom{n} -->

**EN** For ⟦SLOT_98⟧ and ⟦SLOT_99⟧, this gives ⟦SLOT_100⟧. We use this lower binary threshold because ⟦SLOT_101⟧ tasks provide only a single comparative decision per annotator; compared with ⟦SLOT_102⟧, demanding the same level of concentration would remove a disproportionate number of otherwise informative binary comparisons.

**ZH** 对于 ⟦SLOT_98⟧ 与 ⟦SLOT_99⟧，这给出 ⟦SLOT_100⟧。我们采用这一更低的二值阈值，是因为 ⟦SLOT_101⟧ 任务每位标注者只提供一次比较决策；与 ⟦SLOT_102⟧ 相比，要求同等程度的集中会剔除过多本可提供信息的二值比较。

**EN** Appendix E Detailed Experimental Results

**ZH** 附录 E 详细实验结果

**EN** This appendix supplements Section 4 with full result tables that are too large for the main text. We retain the same evaluation focus as in the main paper: overall performance relative to expert baselines, cross-domain variation, sensitivity to candidate order, and auxiliary analyses on decoding and task size.

**ZH** 本附录补充第 4 节中因篇幅过大而未列入正文的完整结果表。我们沿用与正文相同的评测关注点：相对专家基线的整体表现、跨领域差异、对候选顺序的敏感性，以及关于解码与任务规模的辅助分析。

**EN** E.1 Comprehensive MLLM Results

**ZH** E.1 MLLM 完整结果

**EN** Table 15 reports comprehensive MLLM results, including Bot-1, across overall and domain-level evaluations. These results complement Table 4 in the main text by making the asymmetry between identifying the strongest and weakest images explicit. They also make clear that the gap between ap@1 and pass^3 is pervasive rather than concentrated in a small subset of models, consistent with the interpretation in Section 4.2.1 that many MLLM predictions remain sensitive to candidate order and response instability.

**ZH** 表 15 报告 MLLM 的完整结果，包含 Bot-1，覆盖整体与领域级评测。这些结果通过把识别最强与最弱图像之间的不对称性显式呈现出来，补充了正文表 4。它们也表明 ap@1 与 pass^3 之间的落差是普遍存在的，而非集中于少数模型，这与第 4.2.1 节中许多 MLLM 预测仍对候选顺序与响应不稳定敏感的解释一致。

**EN** The full table also makes several model-level patterns easier to inspect. Within the Claude family, Claude Sonnet 4.6 improves substantially over Claude Sonnet 4.5 on the stricter TB-1 pass^3 metric, whereas the GPT-5 series declines monotonically from GPT-5 to GPT-5.2. The same table also makes the closed/open gap clearer under stability-sensitive metrics: Qwen3.5-397B-A17B is much closer to the strongest closed models under ap@1 than under pass^3, suggesting weaker consistency across repeated evaluations. Finally, the domain columns reinforce the main-text headline that illustration is the most difficult domain, photography is generally more tractable, and fine art lies between them.

**ZH** 完整表格还使若干模型层面的规律更易观察。在 Claude 系列内部，Claude Sonnet 4.6 在更严格的 TB-1 pass^3 指标上大幅优于 Claude Sonnet 4.5，而 GPT-5 系列从 GPT-5 到 GPT-5.2 单调下滑。同一表格也使闭源／开源差距在对稳定性敏感的指标下更加清晰：Qwen3.5-397B-A17B 在 ap@1 下远比在 pass^3 下更接近最强的闭源模型，说明其在重复评测中的一致性更弱。最后，领域列强化了正文的核心结论：插画最难，摄影通常更易处理，美术居中。

**EN** Table 15: Comprehensive VAB results for evaluated MLLMs and reference baselines. We report Top-1, Bot-1, and TB-1 accuracy under both ap@1 and pass^3 (%). Best result in each non-baseline column is shown in bold.

**ZH** 表 15：被测 MLLM 与参考基线在 VAB 上的完整结果。我们报告 ap@1 与 pass^3 下 Top-1、Bot-1 与 TB-1 的准确率（%）。每个非基线列的最优结果以粗体显示。

<!-- [原子块 · table] Overall Fine Art Illustration Photography Top-1 Bot-1 TB-1 Top-1 Bot-1 TB-1 Top-1 Bot-1 TB-1 Top-1 Bot-1 TB-1 Model ap@1 p^3 ap@1 p^3 ap@1 p^3 ap@1 p^3 ap@1 p^3 ap@1 p^3 ap@1 p^3 ap@1 p^3 ap@1 p^3 ap@ -->

**EN** E.2 Comprehensive Reward-Model Results

**ZH** E.2 奖励模型完整结果

**EN** Table 16 reports comprehensive reward-model results, including Bot-1, across overall and domain-level evaluations. In contrast to the condensed main-text presentation in Table 5, this table shows that some reward models are materially stronger at rejecting poor images than at identifying the best one. In particular, the detailed Bot-1 columns make the failure mode discussed in Section 4.2.2 directly visible, especially for Q-Instruct in photography.

**ZH** 表 16 报告奖励模型的完整结果，包含 Bot-1，覆盖整体与领域级评测。与正文表 5 的精简呈现不同，该表显示部分奖励模型在淘汰劣质图像上明显强于识别最优图像。特别是详细的 Bot-1 列使第 4.2.2 节讨论的失效模式直接可见，对 Q-Instruct 在摄影上尤其如此。

**EN** Table 16: Comprehensive reward-model results on VAB. Each image is scored independently three times and the scores are averaged before within-task ranking. We report Top-1, Bot-1, and TB-1 accuracy across overall and domain-level evaluations (%). Best result in each non-baseline column is shown in bold.

**ZH** 表 16：奖励模型在 VAB 上的完整结果。每张图像独立评分三次并取平均，再在任务内排序。我们报告整体与领域级评测下 Top-1、Bot-1 与 TB-1 的准确率（%）。每个非基线列的最优结果以粗体显示。

<!-- [原子块 · table] Overall Fine Art Illustration Photography Model Top-1 Bot-1 TB-1 Top-1 Bot-1 TB-1 Top-1 Bot-1 TB-1 Top-1 Bot-1 TB-1 Random Guess 37.2 37.2 27.5 41.0 41.0 36.0 31.5 31.5 19.2 36.8 36.8 23.7 Human Exper -->

**EN** E.3 Topic-Level MLLM Results

**ZH** E.3 主题级 MLLM 结果

**EN** To match the main-text MLLM table, we report topic-level results under all four metrics: Top-1 ap@1, Top-1 pass^3, TB-1 ap@1, and TB-1 pass^3. Together, these tables show that the domain-level trends in Section 4.2.1 are not driven by a single topic or a single evaluation metric. Illustration remains the hardest domain across all four views, while photography is generally more tractable but still highly uneven across topics.

**ZH** 为与正文 MLLM 表格对应，我们报告全部四项指标下的主题级结果：Top-1 ap@1、Top-1 pass^3、TB-1 ap@1 与 TB-1 pass^3。这些表格共同表明，第 4.2.1 节中的领域级趋势并非由单一主题或单一评测指标所驱动。插画在四种视角下始终是最难领域，摄影通常更易处理，但各主题之间仍高度不均衡。

**EN** Several topic effects recur across metrics. In fine art, Chinese painting and portrait-color tasks are often relatively tractable, whereas landscape-color and some sketch-based tasks become much less stable under the stricter criteria. In illustration, the remaining signal is concentrated mostly in anime-and-manga and comic tasks, while concept art, digital-and-AI art, and stylized 3D frequently collapse under pass^3. In photography, macro and sports tasks are often close to saturation for strong models, but night-and-astrophotography, architecture, and some street-and-city tasks remain much less stable, especially when consistency across repeated evaluations is required.

**ZH** 若干主题效应在各项指标上反复出现。在美术中，中国画与肖像色彩任务往往相对容易处理，而风景色彩与部分速写类任务在更严格的标准下稳定性明显下降。在插画中，剩余信号主要集中在动画与漫画、漫画任务上，而概念艺术、数字与 AI 艺术、风格化三维在 pass^3 下常常崩塌。在摄影中，微距与运动任务对强模型而言往往接近饱和，但夜景与天文摄影、建筑以及部分街头与城市任务仍很不稳定，尤其在要求跨重复评测一致时。

**EN** Top-1 ap@1.

**ZH** Top-1 ap@1。

**EN** Tables 17, 18, and 19 report topic-level Top-1 ap@1 results for fine art, illustration, and photography, respectively.

**ZH** 表 17、18、19 分别报告美术、插画与摄影任务的主题级 Top-1 ap@1 结果。

**EN** Table 17: Topic-level MLLM Top-1 ap@1 results on fine-art tasks. The final column reports the corresponding domain-level average (%).

**ZH** 表 17：美术任务上的主题级 MLLM Top-1 ap@1 结果。最后一列报告相应的领域级平均（%）。

<!-- [原子块 · table] Model Calligraphy Chinese Painting Ink & Wash Landscape Color Portrait Color Portrait Sketch Quick Sketch Still Life Color Still Life Sketch Avg. Random Guess 50.0 50.0 50.0 25.2 50.0 50.0 50.0 47.7 5 -->

**EN** Table 18: Topic-level MLLM Top-1 ap@1 results on illustration tasks. The final column reports the corresponding domain-level average (%).

**ZH** 表 18：插画任务上的主题级 MLLM Top-1 ap@1 结果。最后一列报告相应的领域级平均（%）。

<!-- [原子块 · table] Model Anime & Manga Comic Concept Art Digital & AI Art Pixel Art Stylized 3D Avg. Random Guess 50.0 47.5 25.0 29.3 25.0 25.0 31.5 Human Expert 87.7 82.0 66.8 65.2 62.4 71.8 70.3 Closed-Source Models C -->

**EN** Table 19: Topic-level MLLM Top-1 ap@1 results on photography tasks. The final column reports the corresponding domain-level average (%).

**ZH** 表 19：摄影任务上的主题级 MLLM Top-1 ap@1 结果。最后一列报告相应的领域级平均（%）。

<!-- [原子块 · table] Model Architecture Food & Product Landscape Macro Night & Astro Portrait Sports Street & City Wildlife Avg. Random Guess 37.0 36.7 35.4 33.3 33.3 41.7 33.3 38.0 39.8 36.8 Human Expert 81.6 78.0 78.9 7 -->

**EN** Top-1 pass^3.

**ZH** Top-1 pass^3。

**EN** Tables 20, 21, and 22 report topic-level Top-1 pass^3 results for fine art, illustration, and photography, respectively.

**ZH** 表 20、21、22 分别报告美术、插画与摄影任务的主题级 Top-1 pass^3 结果。

**EN** Table 20: Topic-level MLLM Top-1 pass^3 results on fine-art tasks. The final column reports the corresponding domain-level average (%).

**ZH** 表 20：美术任务上的主题级 MLLM Top-1 pass^3 结果。最后一列报告相应的领域级平均（%）。

<!-- [原子块 · table] Model Calligraphy Chinese Painting Ink & Wash Landscape Color Portrait Color Portrait Sketch Quick Sketch Still Life Color Still Life Sketch Avg. Random Guess 12.5 12.5 12.5 2.4 12.5 12.5 12.5 11.6 12 -->

**EN** Table 21: Topic-level MLLM Top-1 pass^3 results on illustration tasks. The final column reports the corresponding domain-level average (%).

**ZH** 表 21：插画任务上的主题级 MLLM Top-1 pass^3 结果。最后一列报告相应的领域级平均（%）。

<!-- [原子块 · table] Model Anime & Manga Comic Concept Art Digital & AI Art Pixel Art Stylized 3D Avg. Random Guess 12.5 11.4 1.6 3.5 1.6 1.6 4.4 Human Expert 87.7 82.0 66.8 65.2 62.4 71.8 70.3 Closed-Source Models Claude -->

**EN** Table 22: Topic-level MLLM Top-1 pass^3 results on photography tasks. The final column reports the corresponding domain-level average (%).

**ZH** 表 22：摄影任务上的主题级 MLLM Top-1 pass^3 结果。最后一列报告相应的领域级平均（%）。

<!-- [原子块 · table] Model Architecture Food & Product Landscape Macro Night & Astro Portrait Sports Street & City Wildlife Avg. Random Guess 5.6 5.5 4.8 3.7 3.7 8.1 3.7 6.2 7.4 5.6 Human Expert 81.6 78.0 78.9 75.0 80.0 8 -->

**EN** TB-1 ap@1.

**ZH** TB-1 ap@1。

**EN** Tables 23, 24, and 25 report topic-level TB-1 ap@1 results for fine art, illustration, and photography, respectively.

**ZH** 表 23、24、25 分别报告美术、插画与摄影任务的主题级 TB-1 ap@1 结果。

**EN** Table 23: Topic-level MLLM TB-1 ap@1 results on fine-art tasks. The final column reports the corresponding domain-level average (%).

**ZH** 表 23：美术任务上的主题级 MLLM TB-1 ap@1 结果。最后一列报告相应的领域级平均（%）。

<!-- [原子块 · table] Model Calligraphy Chinese Painting Ink & Wash Landscape Color Portrait Color Portrait Sketch Quick Sketch Still Life Color Still Life Sketch Avg. Random Guess 50.0 50.0 50.0 11.3 50.0 50.0 50.0 46.4 5 -->

**EN** Table 24: Topic-level MLLM TB-1 ap@1 results on illustration tasks. The final column reports the corresponding domain-level average (%).

**ZH** 表 24：插画任务上的主题级 MLLM TB-1 ap@1 结果。最后一列报告相应的领域级平均（%）。

<!-- [原子块 · table] Model Anime & Manga Comic Concept Art Digital & AI Art Pixel Art Stylized 3D Avg. Random Guess 50.0 45.8 8.3 15.6 8.3 8.3 19.2 Human Expert 87.7 79.0 42.3 49.1 43.3 49.1 54.4 Closed-Source Models Clau -->

**EN** Table 25: Topic-level MLLM TB-1 ap@1 results on photography tasks. The final column reports the corresponding domain-level average (%).

**ZH** 表 25：摄影任务上的主题级 MLLM TB-1 ap@1 结果。最后一列报告相应的领域级平均（%）。

<!-- [原子块 · table] Model Architecture Food & Product Landscape Macro Night & Astro Portrait Sports Street & City Wildlife Avg. Random Guess 24.0 23.3 20.9 16.7 16.7 33.3 16.7 26.1 30.6 23.7 Human Expert 73.8 72.0 71.3 6 -->

**EN** TB-1 pass^3.

**ZH** TB-1 pass^3。

**EN** Tables 26, 27, and 28 report topic-level TB-1 pass^3 results for fine art, illustration, and photography, respectively.

**ZH** 表 26、27、28 分别报告美术、插画与摄影任务的主题级 TB-1 pass^3 结果。

**EN** Table 26: Topic-level TB-1 pass^3 results on fine-art tasks. The final column reports the corresponding domain-level average (%).

**ZH** 表 26：美术任务上的主题级 TB-1 pass^3 结果。最后一列报告相应的领域级平均（%）。

<!-- [原子块 · table] Model Calligraphy Chinese Painting Ink & Wash Landscape Color Portrait Color Portrait Sketch Quick Sketch Still Life Color Still Life Sketch Avg. Random Guess 12.5 12.5 12.5 1.4 12.5 12.5 12.5 11.5 12 -->

**EN** Table 27: Topic-level TB-1 pass^3 results on illustration tasks. The final column reports the corresponding domain-level average (%).

**ZH** 表 27：插画任务上的主题级 TB-1 pass^3 结果。最后一列报告相应的领域级平均（%）。

<!-- [原子块 · table] Model Anime & Manga Comic Concept Art Digital & AI Art Pixel Art Stylized 3D Avg. Random Guess 12.5 11.3 0.1 2.2 0.1 0.1 3.3 Human Expert 87.7 79.0 42.3 49.1 43.3 49.1 54.4 Closed-Source Models Claude -->

**EN** Table 28: Topic-level TB-1 pass^3 results on photography tasks. The final column reports the corresponding domain-level average (%).

**ZH** 表 28：摄影任务上的主题级 TB-1 pass^3 结果。最后一列报告相应的领域级平均（%）。

<!-- [原子块 · table] Model Architecture Food & Product Landscape Macro Night & Astro Portrait Sports Street & City Wildlife Avg. Random Guess 3.1 2.9 2.1 0.5 0.5 6.5 0.5 3.9 5.8 3.1 Human Expert 73.8 72.0 71.3 60.0 60.0 8 -->

**EN** E.4 Topic-Level Reward-Model Results

**ZH** E.4 主题级奖励模型结果

**EN** To match the main-text reward-model table, we report topic-level results for both Top-1 and TB-1. As in the MLLM case, the domain-level averages in the main text mask substantial variation across topics. The topic-level reward-model tables show that relatively stronger domain-level results in photography are driven by a subset of topics, while illustration remains difficult across most topics for all six reward models.

**ZH** 为与正文奖励模型表格对应，我们报告 Top-1 与 TB-1 的主题级结果。与 MLLM 情形相同，正文中的领域级平均掩盖了主题间的巨大差异。主题级奖励模型表格显示，摄影上相对更强的领域级结果由一部分主题驱动，而插画对全部六个奖励模型而言在多数主题上依然困难。

**EN** The topic breakdown also clarifies where reward models do and do not transfer. Fine-art performance is mixed but not uniformly weak, with several models reaching competitive results on Chinese painting and portrait-color tasks. Illustration remains systematically difficult: outside anime-and-manga and, in a few cases, comic, most models stay close to random on concept art, digital-and-AI art, pixel art, and stylized 3D, especially under TB-1. Photography remains the strongest domain, but the gains are concentrated in a subset of topics and do not transfer uniformly to the harder best-and-worst selection setting.

**ZH** 主题细分也澄清了奖励模型在何处迁移、在何处不迁移。美术表现参差不齐但并非普遍偏弱，若干模型在中国画与肖像色彩任务上达到有竞争力的结果。插画依然系统性困难：除动画与漫画以及少数情形下的漫画之外，多数模型在概念艺术、数字与 AI 艺术、像素艺术与风格化三维上接近随机水平，在 TB-1 下尤其如此。摄影仍是最强领域，但增益集中于部分主题，且不会统一迁移到更难的最优与最差同时选择的设置上。

**EN** Top-1.

**ZH** Top-1。

**EN** Tables 29, 30, and 31 report topic-level Top-1 results for fine art, illustration, and photography, respectively.

**ZH** 表 29、30、31 分别报告美术、插画与摄影任务的主题级 Top-1 结果。

**EN** TB-1.

**ZH** TB-1。

**EN** Tables 32, 33, and 36 report topic-level TB-1 results for fine art, illustration, and photography, respectively.

**ZH** 表 32、33、36 分别报告美术、插画与摄影任务的主题级 TB-1 结果。

**EN** Table 29: Topic-level reward-model Top-1 results on fine-art tasks. The final column reports the corresponding domain-level average (%).

**ZH** 表 29：美术任务上的主题级奖励模型 Top-1 结果。最后一列报告相应的领域级平均（%）。

<!-- [原子块 · table] Model Calligraphy Chinese Painting Ink & Wash Landscape Color Portrait Color Portrait Sketch Quick Sketch Still Life Color Still Life Sketch Avg. Random Guess 50.0 50.0 50.0 25.2 50.0 50.0 50.0 47.7 5 -->

**EN** Table 30: Topic-level reward-model Top-1 results on illustration tasks. The final column reports the corresponding domain-level average (%).

**ZH** 表 30：插画任务上的主题级奖励模型 Top-1 结果。最后一列报告相应的领域级平均（%）。

<!-- [原子块 · table] Model Anime & Manga Comic Concept Art Digital & AI Art Pixel Art Stylized 3D Avg. Random Guess 50.0 47.5 25.0 29.3 25.0 25.0 31.5 Human Expert 87.7 82.0 66.8 65.2 62.4 71.8 70.3 Reward Models ArtiMuse -->

**EN** Table 31: Topic-level reward-model Top-1 results on photography tasks. The final column reports the corresponding domain-level average (%).

**ZH** 表 31：摄影任务上的主题级奖励模型 Top-1 结果。最后一列报告相应的领域级平均（%）。

<!-- [原子块 · table] Model Architecture Food & Product Landscape Macro Night & Astro Portrait Sports Street & City Wildlife Avg. Random Guess 37.0 36.7 35.4 33.3 33.3 41.7 33.3 38.0 39.8 36.8 Human Expert 81.6 78.0 78.9 7 -->

**EN** Table 32: Topic-level reward-model TB-1 results on fine-art tasks. The final column reports the corresponding domain-level average (%).

**ZH** 表 32：美术任务上的主题级奖励模型 TB-1 结果。最后一列报告相应的领域级平均（%）。

<!-- [原子块 · table] Model Calligraphy Chinese Painting Ink & Wash Landscape Color Portrait Color Portrait Sketch Quick Sketch Still Life Color Still Life Sketch Avg. Random Guess 50.0 50.0 50.0 11.3 50.0 50.0 50.0 46.4 5 -->

**EN** Table 33: Topic-level reward-model TB-1 results on illustration tasks. The final column reports the corresponding domain-level average (%).

**ZH** 表 33：插画任务上的主题级奖励模型 TB-1 结果。最后一列报告相应的领域级平均（%）。

<!-- [原子块 · table] Model Anime & Manga Comic Concept Art Digital & AI Art Pixel Art Stylized 3D Avg. Random Guess 50.0 45.8 8.3 15.6 8.3 8.3 19.2 Human Expert 87.7 79.0 42.3 49.1 43.3 49.1 54.4 Reward Models ArtiMuse 53 -->

**EN** E.5 Temperature Ablation

**ZH** E.5 温度消融

**EN** Table 34 reports the full model-by-model temperature ablation referenced in Section 4.3. The overall trend is that greedy decoding modestly improves stability, but the effect size varies substantially across models and does not alter the main conclusion that the dominant limitation is comparative judgment rather than decoding noise alone.

**ZH** 表 34 报告第 4.3 节引用的逐模型完整温度消融。总体趋势是贪心解码小幅提升稳定性，但效应量在模型间差异很大，且不改变主要结论：主导性限制是比较判断，而非单纯的解码噪声。

**EN** The gains are not uniform. Gemini 3.1 Pro and Claude Sonnet 4.5 benefit the most from greedy decoding, with especially visible improvements on the stricter TB-1 pass^3 metric. A small set of models, including Claude Sonnet 4.6, Doubao Seed 2.0 Pro, GLM-4.6V, and Qwen3.5-397B-A17B, are flat or slightly worse on at least one metric, reinforcing the point that decoding choice matters but does not dominate the benchmark outcome.

**ZH** 增益并不一致。Gemini 3.1 Pro 与 Claude Sonnet 4.5 从贪心解码中获益最多，在更严格的 TB-1 pass^3 指标上提升尤其明显。少数模型，包括 Claude Sonnet 4.6、Doubao Seed 2.0 Pro、GLM-4.6V 与 Qwen3.5-397B-A17B，在至少一项指标上持平或略有下降，这再次说明解码选择确有影响，但并不主导基准结果。

**EN** Table 34: Effect of decoding temperature on MLLM performance. We compare default decoding (⟦SLOT_103⟧) with greedy decoding (⟦SLOT_104⟧); ⟦SLOT_105⟧ denotes the change from ⟦SLOT_106⟧ to ⟦SLOT_107⟧ (%).

**ZH** 表 34：解码温度对 MLLM 表现的影响。我们比较默认解码（⟦SLOT_103⟧）与贪心解码（⟦SLOT_104⟧）；⟦SLOT_105⟧ 表示从 ⟦SLOT_106⟧ 到 ⟦SLOT_107⟧ 的变化（%）。

<!-- [原子块 · table] Top-1 p^3 TB-1 p^3 Model t = 1 t{=}1 t = 0 t{=}0 Δ \Delta t = 1 t{=}1 t = 0 t{=}0 Δ \Delta Closed-Source Models Claude-Haiku-4.5 18.8 21.2 +2.4 12.5 17.2 +4.7 Claude-Sonnet-4.5 24.2 27.3 +3.1 14.5 20. -->

**EN** Table 35: TB-1 results by candidate set size ⟦SLOT_108⟧ for the evaluated MLLMs and reference baselines. For each set size, we report pass^3 and ap@1 (%).

**ZH** 表 35：被测 MLLM 与参考基线按候选集规模 ⟦SLOT_108⟧ 划分的 TB-1 结果。对每个规模，我们报告 pass^3 与 ap@1（%）。

<!-- [原子块 · table] k = 2 k=2 k = 3 k=3 k = 4 k=4 k = 5 k=5 k = 6 k=6 Model p^3 ap@1 p^3 ap@1 p^3 ap@1 p^3 ap@1 p^3 ap@1 Random Guess 12.5 50.0 0.5 16.7 0.1 8.3 0.0 5.0 0.0 3.3 Human Expert 87.1 69.3 43.6 45.9 40.0 Claud -->

**EN** E.6 Results by Candidate Set Size

**ZH** E.6 按候选集规模划分的结果

**EN** Table 35 provides the full breakdown by candidate set size. Consistent with the summary in the main text, performance drops sharply as ⟦SLOT_109⟧ increases, and the decline is especially severe under the stricter TB-1 pass^3 criterion. The table also shows that the gap between models and human experts widens noticeably on larger candidate sets.

**ZH** 表 35 给出按候选集规模的完整细分。与正文摘要一致，随着 ⟦SLOT_109⟧ 增大，性能急剧下降，在更严格的 TB-1 pass^3 标准下衰减尤为严重。该表还显示，模型与人类专家之间的差距在更大的候选集上明显拉大。

**EN** Table 36: Topic-level reward-model TB-1 results on photography tasks. The final column reports the corresponding domain-level average (%).

**ZH** 表 36：摄影任务上的主题级奖励模型 TB-1 结果。最后一列报告相应的领域级平均（%）。

<!-- [原子块 · table] Model Architecture Food & Product Landscape Macro Night & Astro Portrait Sports Street & City Wildlife Avg. Random Guess 24.0 23.3 20.9 16.7 16.7 33.3 16.7 26.1 30.6 23.7 Human Expert 73.8 72.0 71.3 6 -->

**EN** Appendix F Human Study Details

**ZH** 附录 F 人工研究细节

**EN** F.1 Detailed Setup and Metric Definitions

**ZH** F.1 详细设置与指标定义

**EN** This subsection provides the full metric definitions summarized in Section 2.

**ZH** 本小节给出第 2 节概述的完整指标定义。

**EN** Eight expert annotators evaluate identical images under both protocols. Under scoring, each annotator independently assigns an absolute score ⟦SLOT_110⟧ to each image. Under ranking, annotators provide a complete within-task ordering when presented with groups of size ⟦SLOT_111⟧. We operationalize “more scientifically sound” along three dimensions: fidelity to human comparative preference, reproducibility across annotators, and sharpness of the resulting label signal.

**ZH** 八位专家标注者在两种流程下评估相同的图像。评分流程下，每位标注者独立为每张图像赋予绝对分数 ⟦SLOT_110⟧。排序流程下，标注者在面对规模为 ⟦SLOT_111⟧ 的组时给出完整的任务内次序。我们从三个维度把“更合乎科学依据”操作化：对人类比较偏好的保真度、跨标注者的可复现性，以及所得标签信号的锐度。

**EN** The study comprises 119 homogeneous-content tasks drawn directly from the curated benchmark, where all candidates share the same underlying content, and 107 heterogeneous-content tasks formed by regrouping 370 images from distinct homogeneous task groups while preserving topic consistency. Each image appears in at most one regrouped task. Examples of both settings are given in Appendix F.3.

**ZH** 该研究包含 119 个直接取自整理后基准的同质内容任务（其中所有候选共享相同底层内容），以及 107 个异质内容任务——后者通过在保持主题一致的前提下，从不同的同质任务组中重组 370 张图像得到。每张图像最多出现在一个重组任务中。两种设置的示例见附录 F.3。

**EN** Fidelity.

**ZH** 保真度。

**EN** We ask whether the ranking induced by absolute scores matches the direct ranking produced by the same annotator. Let ⟦SLOT_112⟧ and ⟦SLOT_113⟧ denote annotator ⟦SLOT_114⟧’s direct rankings for homogeneous-content and heterogeneous-content tasks, and let ⟦SLOT_115⟧ denote the ranking induced by the absolute scores. We report Kendall’s ⟦SLOT_116⟧ (Kendall, 1938),

**ZH** 我们追问：由绝对分数导出的排序，是否与同一标注者直接给出的排序一致。记 ⟦SLOT_112⟧ 与 ⟦SLOT_113⟧ 为标注者 ⟦SLOT_114⟧ 对同质内容与异质内容任务的直接排序，记 ⟦SLOT_115⟧ 为绝对分数导出的排序。我们报告 Kendall’s ⟦SLOT_116⟧（Kendall，1938），

<!-- [原子块 · table] τ = C − D ( n 2 ) , \tau=\frac{C-D}{\binom{n}{2}}, -->

**EN** where ⟦SLOT_117⟧ and ⟦SLOT_118⟧ are the numbers of concordant and discordant pairs. We compute ⟦SLOT_119⟧ for each annotator within each task, average across annotators to obtain a task-level value, and report the mean and standard deviation across tasks. We additionally report a top-1 self-consistency (SC) rate: the fraction of annotator–task pairs for which ⟦SLOT_120⟧ and the direct ranking select the same top image.

**ZH** 其中 ⟦SLOT_117⟧ 与 ⟦SLOT_118⟧ 分别为一致对与不一致对的数目。我们在每个任务内为每位标注者计算 ⟦SLOT_119⟧，跨标注者平均得到任务级取值，并报告跨任务的均值与标准差。我们还报告 top-1 自洽率（SC rate）：⟦SLOT_120⟧ 与直接排序选出同一张最优图像的标注者–任务对所占比例。

**EN** Reproducibility.

**ZH** 可复现性。

**EN** We define task-level accuracy ⟦SLOT_121⟧ as the fraction of tasks on which at least five of the eight annotators agree on the relevant label, and report ⟦SLOT_122⟧, ⟦SLOT_123⟧, and ⟦SLOT_124⟧ for both protocols.

**ZH** 我们把任务级准确率 ⟦SLOT_121⟧ 定义为八位标注者中至少五人在相关标签上达成一致的任务比例，并对两种流程报告 ⟦SLOT_122⟧、⟦SLOT_123⟧ 与 ⟦SLOT_124⟧。

**EN** Distinguishability.

**ZH** 可区分度。

**EN** Restricting to the 119 homogeneous-content tasks, where entropy reflects concentration of aesthetic preference rather than content mismatch, we measure the entropy of the eight annotators’ top-1 selections (Shannon, 1948),

**ZH** 限于 119 个同质内容任务（其中熵反映审美偏好的集中程度而非内容错配），我们测量八位标注者 top-1 选择的熵（Shannon，1948），

<!-- [原子块 · table] H = − ∑ i p i log 2 p i , H=-\sum_{i}p_{i}\log_{2}p_{i}, -->

**EN** where ⟦SLOT_125⟧ is the fraction of annotators selecting image ⟦SLOT_126⟧ as the top image in a task. Because the maximum entropy depends on task size ⟦SLOT_127⟧, we report the unnormalized quantity so that lower values directly indicate stronger concentration of top-choice judgments.

**ZH** 其中 ⟦SLOT_125⟧ 是在某任务中选择图像 ⟦SLOT_126⟧ 为最优的标注者比例。由于最大熵取决于任务规模 ⟦SLOT_127⟧，我们报告未归一化的量，使数值越低直接表示首选判断越集中。

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

**EN** Figure 6: Schematic examples of the two settings used in the human study. Left: a homogeneous-content task, where all candidates come from the same source task and share the same underlying content. Right: a heterogeneous-content task, where candidates are regrouped from different source tasks. In both settings, the scoring protocol rates images independently, whereas the ranking protocol orders the full set jointly.

**ZH** 图 6：人工研究中两种设置的示意样例。左：同质内容任务，所有候选来自同一源任务并共享相同底层内容。右：异质内容任务，候选由不同源任务重组而来。两种设置下，评分流程独立地为图像打分，而排序流程对整个集合联合排序。

**EN** F.2 Extended Interpretation

**ZH** F.2 扩展解释

**EN** Philosophical lens.

**ZH** 哲学视角。

**EN** Our results echo the long-standing debate between Aesthetic Absolutism, which posits a context-free, intrinsic standard of beauty, and Aesthetic Relativism, which holds that judgments arise from comparison and context. Modern philosophical aesthetics has largely moved toward the relational view: people can reliably tell which image they prefer when alternatives are juxtaposed.

**ZH** 我们的结果呼应了美学绝对主义与美学相对主义之间的长期争论：前者假定存在与语境无关的内在美之标准，后者认为判断产生于比较与语境。现代哲学美学已大步转向关系性观点：当各选项并置时，人们能可靠说出自己更偏好哪一张图像。

**EN** Statistical lens.

**ZH** 统计视角。

**EN** Scoring introduces an additional measurement layer. Annotators must first form an internal judgment and then translate it onto a numeric scale, after which pairwise preference is inferred from score differences. This pipeline adds calibration variance, scale-use heterogeneity, and extra measurement noise. Ranking measures the relative decision of interest more directly, which helps explain its higher consistency and sharper signal.

**ZH** 评分引入了额外的一层测量。标注者必须先形成内在判断，再把它映射到数字量表上，之后由分数之差推断成对偏好。这条流程增加了校准方差、量表使用异质性与额外的测量噪声。排序更直接地测量我们所关心的相对决策，这有助于解释它为何一致性更高、信号更锐利。

**EN** Cognitive lens.

**ZH** 认知视角。

**EN** Comparative judgment is a natural human operation. People can often say which of two images feels better before they can specify by how much. Absolute scoring is cognitively heavier because it requires maintaining an internal reference scale, calibrating intervals, and converting a qualitative impression into a number. That added abstraction likely makes scoring less stable than direct comparison.

**ZH** 比较判断是人类天然的操作。人们往往能说出两张图像中哪一张观感更好，却说不出好多少。绝对评分的认知负担更重，因为它需要维持内在参照量表、校准区间，并把质性印象转换为数字。这种额外的抽象化很可能使评分不如直接比较稳定。

**EN** F.3 Task Examples

**ZH** F.3 任务示例

**EN** Figure 6 provides schematic examples of the two task settings used in the human study.

**ZH** 图 6 给出人工研究中两种任务设置的示意样例。

**EN** F.4 Annotation Protocol

**ZH** F.4 标注流程

**EN** Scoring task.

**ZH** 评分任务。

**EN** Under the scoring protocol, each annotator independently assigned an absolute score ⟦SLOT_128⟧ to each of the 400 images in the base image pool. Images were presented individually, without access to the other members of the same task group. The resulting scores were later reused to derive score-derived rankings for both the 119 homogeneous-content tasks and the 107 heterogeneous-content regroupings. Domain-specific single-image scoring rubrics are given below.

**ZH** 在评分流程下，每位标注者独立为基础图像池中的 400 张图像各赋予一个绝对分数 ⟦SLOT_128⟧。图像逐个呈现，标注者看不到同一任务组中的其他成员。所得分数随后被复用于导出 119 个同质内容任务与 107 个异质内容重组的分数导出排序。领域专属的单图像评分细则如下。

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

**EN** When converting absolute scores into induced rankings, no exact within-task score ties were observed in the collected annotations, so no tie-breaking rule was required.

**ZH** 在把绝对分数转换为导出排序时，所采集的标注中未出现任务内分数完全持平的情形，因此无需制定打破并列的规则。

**EN** Ranking task.

**ZH** 排序任务。

**EN** Under the ranking protocol, each annotator provided a complete best-to-worst ordering of all ⟦SLOT_129⟧ images presented simultaneously within a group. Annotators were instructed to rank the images by overall aesthetic quality using the following domain-specific comparative rubrics.

**ZH** 在排序流程下，每位标注者对组内同时呈现的全部 ⟦SLOT_129⟧ 张图像给出完整的最优到最差次序。标注者被要求按整体美学质量，使用下述领域专属比较细则对图像排序。

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

**EN** F.5 Notation

**ZH** F.5 符号

<!-- [原子块 · table] Symbol Meaning A = 8 A=8 number of annotators n n number of images in a task, n ∈ { 2 , 3 , 4 , 5 } n\in\{2,3,4,5\} s i , a s_{i,a} absolute score assigned to image i i by annotator a a , s i , a ∈ [  -->

**EN** Task-level accuracy.

**ZH** 任务级准确率。

**EN** For the majority-agreement comparison, task-level accuracy is defined as follows:

**ZH** 对于多数一致的比较，任务级准确率定义如下：

**EN** • ⟦SLOT_130⟧: fraction of tasks on which at least five of the eight annotators select the same best label.

**ZH** • ⟦SLOT_130⟧：八位标注者中至少五人选出同一最优标签的任务比例。

**EN** • ⟦SLOT_131⟧: fraction of tasks on which at least five of the eight annotators select the same worst label.

**ZH** • ⟦SLOT_131⟧：八位标注者中至少五人选出同一最差标签的任务比例。

**EN** • ⟦SLOT_132⟧: fraction of tasks on which both majority conditions are satisfied simultaneously.

**ZH** • ⟦SLOT_132⟧：两个多数条件同时满足的任务比例。

**EN** F.6 Statistical Tests

**ZH** F.6 统计检验

**EN** We report two-sided paired tests over tasks to assess whether the ranking and scoring protocols differ systematically. Unless otherwise noted, ⟦SLOT_133⟧-values are uncorrected for multiple comparisons.

**ZH** 我们在任务上报告双侧配对检验，以评估排序与评分两种流程是否存在系统性差异。除特别说明外，⟦SLOT_133⟧ 值未做多重比较校正。

**EN** McNemar’s test for majority-agreement comparisons.

**ZH** 多数一致比较的 McNemar 检验。

**EN** For each task and each metric ⟦SLOT_134⟧, ⟦SLOT_135⟧, and ⟦SLOT_136⟧, we construct paired binary outcomes indicating whether the protocol achieves a five-of-eight majority hit. We then apply an exact two-sided McNemar test (McNemar, 1947, Fagerland et al., 2013) to the discordant pairs.

**ZH** 对于每个任务与每个指标 ⟦SLOT_134⟧、⟦SLOT_135⟧、⟦SLOT_136⟧，我们构造配对的二值结果，指示该流程是否达成五分之八的多数命中。随后我们对不一致对施加精确双侧 McNemar 检验（McNemar，1947；Fagerland 等，2013）。

**EN** • Homogeneous-content (⟦SLOT_137⟧ tasks): ⟦SLOT_138⟧ for ⟦SLOT_139⟧, ⟦SLOT_140⟧ for ⟦SLOT_141⟧, and ⟦SLOT_142⟧ for ⟦SLOT_143⟧.

**ZH** • 同质内容（⟦SLOT_137⟧ 个任务）：⟦SLOT_138⟧ 对应 ⟦SLOT_139⟧，⟦SLOT_140⟧ 对应 ⟦SLOT_141⟧，⟦SLOT_142⟧ 对应 ⟦SLOT_143⟧。

**EN** • Heterogeneous-content (⟦SLOT_144⟧ tasks): ⟦SLOT_145⟧ for ⟦SLOT_146⟧, ⟦SLOT_147⟧ for ⟦SLOT_148⟧, and ⟦SLOT_149⟧ for ⟦SLOT_150⟧.

**ZH** • 异质内容（⟦SLOT_144⟧ 个任务）：⟦SLOT_145⟧ 对应 ⟦SLOT_146⟧，⟦SLOT_147⟧ 对应 ⟦SLOT_148⟧，⟦SLOT_149⟧ 对应 ⟦SLOT_150⟧。

**EN** Wilcoxon signed-rank test for entropy comparison.

**ZH** 熵比较的 Wilcoxon 符号秩检验。

**EN** We compare the paired per-task entropies ⟦SLOT_151⟧ and ⟦SLOT_152⟧ over the 119 homogeneous-content tasks using a two-sided Wilcoxon signed-rank test (Wilcoxon, 1945), which yields ⟦SLOT_153⟧.

**ZH** 我们对 119 个同质内容任务上配对的逐任务熵 ⟦SLOT_151⟧ 与 ⟦SLOT_152⟧ 做双侧 Wilcoxon 符号秩检验（Wilcoxon，1945），得到 ⟦SLOT_153⟧。

**EN** Multiple comparisons.

**ZH** 多重比较。

**EN** After Bonferroni correction (Bonferroni, 1936) over the three metrics in each setting, all six tests remain significant at ⟦SLOT_154⟧.

**ZH** 经 Bonferroni 校正（Bonferroni，1936）后，每种设置下三项指标的检验中，全部六个检验在 ⟦SLOT_154⟧ 水平上仍显著。

**EN** F.7 Task Lists

**ZH** F.7 任务清单

**EN** Homogeneous-Content Tasks (119 Tasks)

**ZH** 同质内容任务（119 个任务）

**EN** Each homogeneous-content task groups images that share the same underlying content but differ in aesthetic treatment. The 119 tasks span four topics across three domains.

**ZH** 每个同质内容任务把底层内容相同而美学处理不同的图像归为一组。119 个任务涵盖三个领域下的四个主题。

**EN** Table 37: Homogeneous-content tasks (119 tasks).

**ZH** 表 37：同质内容任务（119 个任务）。

<!-- [原子块 · table] Task ID n n fine-art_landscape-color_61 4 fine-art_landscape-color_64 2 fine-art_landscape-color_65 4 fine-art_landscape-color_66 4 fine-art_landscape-color_68 5 fine-art_landscape-color_69 5 fine-art -->

**EN** Heterogeneous-Content Tasks (107 Tasks)

**ZH** 异质内容任务（107 个任务）

**EN** Each heterogeneous-content task is formed by regrouping images drawn from distinct homogeneous-content tasks, typically within the same topic. Of the original 119 regrouped tasks, 12 are excluded because the score-based Kendall’s ⟦SLOT_155⟧ (Kendall and Smith, 1939) is at least 0.825, indicating that the regrouped task already exhibits near-saturated consensus under the scoring protocol. The remaining 107 tasks are retained for analysis. The Source Task IDs column lists the originating homogeneous-content task for each image in the group, in label order A, B, C, ….

**ZH** 每个异质内容任务由取自不同同质内容任务的图像重组而成，通常在同一主题内。在最初的 119 个重组任务中，有 12 个被剔除，因为其基于分数的 Kendall’s ⟦SLOT_155⟧（Kendall 与 Smith，1939）不低于 0.825，说明该重组任务在评分流程下已呈现接近饱和的共识。其余 107 个任务保留用于分析。Source Task IDs 列按标签顺序 A、B、C……列出组内每张图像的来源同质内容任务。

**EN** Table 38: Heterogeneous-content task construction (107 tasks, after saturation filter).

**ZH** 表 38：异质内容任务的构建（107 个任务，经饱和过滤后）。

<!-- [原子块 · table] ID n n Source Task IDs 1 3 illustration_pixel-art_19, illustration_pixel-art_23, illustration_pixel-art_17 2 3 photograph_landscape_27, photograph_landscape_2, photograph_landscape_3 3 3 illustration_ -->

**EN** Appendix G Fine-Tuning Details

**ZH** 附录 G 微调细节

**EN** G.1 Hyperparameters

**ZH** G.1 超参数

**EN** Table 39 lists the hyperparameters used to fine-tune Kallisti-35B-A3B.

**ZH** 表 39 列出用于微调 Kallisti-35B-A3B 的超参数。

**EN** Table 39: Hyperparameters used for fine-tuning Kallisti-35B-A3B.

**ZH** 表 39：用于微调 Kallisti-35B-A3B 的超参数。

<!-- [原子块 · table] Parameter Value Base Model Qwen3.5-35B-A3B Fine-tuning Method LoRA LoRA Rank 64 LoRA Alpha 128 LoRA Target All layers Vision Tower Frozen MLP Projector Trainable Learning Rate 1 × 10 − 4 1\times 10^{- -->

**EN** G.2 Detailed Results

**ZH** G.2 详细结果

**EN** As in the main-text fine-tuning table, we report topic-level detailed results under all four metrics: Top-1 ap@1, Top-1 pass^3, TB-1 ap@1, and TB-1 pass^3. The full breakdown shows that the gains from fine-tuning are uneven across topics: Kallisti-35B-A3B improves most clearly on several fine-art topics, remains competitive with larger open-weight baselines on illustration, and does not uniformly dominate its base model in photography.

**ZH** 与正文微调表相同，我们报告全部四项指标下的主题级详细结果：Top-1 ap@1、Top-1 pass^3、TB-1 ap@1 与 TB-1 pass^3。完整细分显示，微调带来的增益在各主题间并不均衡：Kallisti-35B-A3B 在若干美术主题上提升最明显，在插画上与更大的开源权重基线保持竞争力，而在摄影上并未全面优于其基座模型。

**EN** Top-1 ap@1.

**ZH** Top-1 ap@1。

**EN** Tables 40, 41, and 42 report topic-level Top-1 ap@1 results for fine art, illustration, and photography, respectively.

**ZH** 表 40、41、42 分别报告美术、插画与摄影任务的主题级 Top-1 ap@1 结果。

**EN** Table 40: Topic-level fine-tuning Top-1 ap@1 results on fine-art tasks. The final column reports the corresponding domain-level average (%).

**ZH** 表 40：美术任务上的主题级微调 Top-1 ap@1 结果。最后一列报告相应的领域级平均（%）。

<!-- [原子块 · table] Model Calligraphy Chinese Painting Ink & Wash Landscape Color Portrait Color Portrait Sketch Quick Sketch Still Life Color Still Life Sketch Avg. Open-Weight Models GLM-4.6V 21.2 63.0 33.3 26.8 66.7 5 -->

**EN** Table 41: Topic-level fine-tuning Top-1 ap@1 results on illustration tasks. The final column reports the corresponding domain-level average (%).

**ZH** 表 41：插画任务上的主题级微调 Top-1 ap@1 结果。最后一列报告相应的领域级平均（%）。

<!-- [原子块 · table] Model Anime & Manga Comic Concept Art Digital & AI Art Pixel Art Stylized 3D Avg. Open-Weight Models GLM-4.6V 51.3 53.3 31.8 37.7 60.3 27.3 43.3 Kimi-K2.5 71.8 56.7 36.4 36.2 39.7 30.3 43.0 Qwen3-VL-2 -->

**EN** Table 42: Topic-level fine-tuning Top-1 ap@1 results on photography tasks. The final column reports the corresponding domain-level average (%).

**ZH** 表 42：摄影任务上的主题级微调 Top-1 ap@1 结果。最后一列报告相应的领域级平均（%）。

<!-- [原子块 · table] Model Architecture Food & Product Landscape Macro Night & Astro Portrait Sports Street & City Wildlife Avg. Open-Weight Models GLM-4.6V 35.4 53.3 39.3 58.3 16.7 0.0 100.0 48.7 63.0 43.2 Kimi-K2.5 49.0 -->

**EN** Top-1 pass^3.

**ZH** Top-1 pass^3。

**EN** Tables 43, 44, and 45 report topic-level Top-1 pass^3 results for fine art, illustration, and photography, respectively.

**ZH** 表 43、44、45 分别报告美术、插画与摄影任务的主题级 Top-1 pass^3 结果。

**EN** Table 43: Topic-level fine-tuning Top-1 pass^3 results on fine-art tasks. The final column reports the corresponding domain-level average (%).

**ZH** 表 43：美术任务上的主题级微调 Top-1 pass^3 结果。最后一列报告相应的领域级平均（%）。

<!-- [原子块 · table] Model Calligraphy Chinese Painting Ink & Wash Landscape Color Portrait Color Portrait Sketch Quick Sketch Still Life Color Still Life Sketch Avg. Open-Weight Models GLM-4.6V 9.1 55.6 0.0 5.4 50.0 21.2 -->

**EN** Table 44: Topic-level fine-tuning Top-1 pass^3 results on illustration tasks. The final column reports the corresponding domain-level average (%).

**ZH** 表 44：插画任务上的主题级微调 Top-1 pass^3 结果。最后一列报告相应的领域级平均（%）。

<!-- [原子块 · table] Model Anime & Manga Comic Concept Art Digital & AI Art Pixel Art Stylized 3D Avg. Open-Weight Models GLM-4.6V 23.1 20.0 9.1 17.4 38.1 0.0 19.0 Kimi-K2.5 53.8 30.0 13.6 21.7 9.5 9.1 21.0 Qwen3-VL-235B- -->

**EN** Table 45: Topic-level fine-tuning Top-1 pass^3 results on photography tasks. The final column reports the corresponding domain-level average (%).

**ZH** 表 45：摄影任务上的主题级微调 Top-1 pass^3 结果。最后一列报告相应的领域级平均（%）。

<!-- [原子块 · table] Model Architecture Food & Product Landscape Macro Night & Astro Portrait Sports Street & City Wildlife Avg. Open-Weight Models GLM-4.6V 6.2 20.0 15.6 50.0 0.0 0.0 100.0 15.4 33.3 15.8 Kimi-K2.5 18.8 6 -->

**EN** TB-1 ap@1.

**ZH** TB-1 ap@1。

**EN** Tables 46, 47, and 48 report topic-level TB-1 ap@1 results for fine art, illustration, and photography, respectively.

**ZH** 表 46、47、48 分别报告美术、插画与摄影任务的主题级 TB-1 ap@1 结果。

**EN** Table 46: Topic-level fine-tuning TB-1 ap@1 results on fine-art tasks. The final column reports the corresponding domain-level average (%).

**ZH** 表 46：美术任务上的主题级微调 TB-1 ap@1 结果。最后一列报告相应的领域级平均（%）。

<!-- [原子块 · table] Model Calligraphy Chinese Painting Ink & Wash Landscape Color Portrait Color Portrait Sketch Quick Sketch Still Life Color Still Life Sketch Avg. Open-Weight Models GLM-4.6V 21.2 63.0 33.3 17.3 66.7 5 -->

**EN** Table 47: Topic-level fine-tuning TB-1 ap@1 results on illustration tasks. The final column reports the corresponding domain-level average (%).

**ZH** 表 47：插画任务上的主题级微调 TB-1 ap@1 结果。最后一列报告相应的领域级平均（%）。

<!-- [原子块 · table] Model Anime & Manga Comic Concept Art Digital & AI Art Pixel Art Stylized 3D Avg. Open-Weight Models GLM-4.6V 51.3 50.0 13.6 20.3 28.6 15.2 27.0 Kimi-K2.5 71.8 53.3 18.2 20.3 17.5 18.2 29.0 Qwen3-VL-2 -->

**EN** Table 48: Topic-level fine-tuning TB-1 ap@1 results on photography tasks. The final column reports the corresponding domain-level average (%).

**ZH** 表 48：摄影任务上的主题级微调 TB-1 ap@1 结果。最后一列报告相应的领域级平均（%）。

<!-- [原子块 · table] Model Architecture Food & Product Landscape Macro Night & Astro Portrait Sports Street & City Wildlife Avg. Open-Weight Models GLM-4.6V 28.1 40.0 28.1 33.3 33.3 0.0 66.7 39.3 48.1 33.1 Kimi-K2.5 29.2  -->

**EN** TB-1 pass^3.

**ZH** TB-1 pass^3。

**EN** Tables 49, 50, and 51 report topic-level TB-1 pass^3 results for fine art, illustration, and photography, respectively.

**ZH** 表 49、50、51 分别报告美术、插画与摄影任务的主题级 TB-1 pass^3 结果。

**EN** Table 49: Topic-level TB-1 pass^3 fine-tuning results on fine-art tasks. The final column reports the corresponding domain-level average (%).

**ZH** 表 49：美术任务上的主题级微调 TB-1 pass^3 结果。最后一列报告相应的领域级平均（%）。

<!-- [原子块 · table] Model Calligraphy Chinese Painting Ink & Wash Landscape Color Portrait Color Portrait Sketch Quick Sketch Still Life Color Still Life Sketch Avg. Open-Weight Models GLM-4.6V 9.1 55.6 0.0 7.1 50.0 21.2 -->

**EN** Table 50: Topic-level TB-1 pass^3 fine-tuning results on illustration tasks. The final column reports the corresponding domain-level average (%).

**ZH** 表 50：插画任务上的主题级微调 TB-1 pass^3 结果。最后一列报告相应的领域级平均（%）。

<!-- [原子块 · table] Model Anime & Manga Comic Concept Art Digital & AI Art Pixel Art Stylized 3D Avg. Open-Weight Models GLM-4.6V 23.1 20.0 4.5 8.7 0.0 0.0 8.0 Kimi-K2.5 53.8 30.0 4.5 8.7 4.8 0.0 14.0 Qwen3-VL-235B-A22B  -->

**EN** Table 51: Topic-level TB-1 pass^3 fine-tuning results on photography tasks. The final column reports the corresponding domain-level average (%).

**ZH** 表 51：摄影任务上的主题级微调 TB-1 pass^3 结果。最后一列报告相应的领域级平均（%）。

<!-- [原子块 · table] Model Architecture Food & Product Landscape Macro Night & Astro Portrait Sports Street & City Wildlife Avg. Open-Weight Models GLM-4.6V 0.0 20.0 2.2 0.0 0.0 0.0 0.0 10.3 22.2 5.8 Kimi-K2.5 3.1 60.0 6. -->

**EN** Appendix H Prompt Templates and Scoring Interfaces

**ZH** 附录 H 提示模板与评分接口

**EN** This appendix records the prompt templates and scoring interfaces used in data construction and evaluation. We group them by usage: prompts for the photography pipeline, prompts for the illustration pipeline, prompts for MLLM evaluation, and scoring interfaces for reward-model evaluation.

**ZH** 本附录记录数据构建与评测中使用的提示模板与评分接口。我们按用途分组：摄影流程提示、插画流程提示、MLLM 评测提示，以及奖励模型评测的评分接口。

**EN** H.1 Photography Pipeline Prompts

**ZH** H.1 摄影流程提示

**EN** This subsection records the prompts used in the photography agent-edit pipeline described in Section 3. The pipeline consists of three stages: aspect-wise critique generation with ArtiMuse, edit planning with GPT through LiteLLM, and image editing with Gemini-3-Pro-Image (Nano Banana Pro). In Step 1, ArtiMuse is queried eight times independently with the same image, once per aesthetic aspect. The resulting responses are then concatenated into a single review string that is passed to the planning stage.

**ZH** 本小节记录第 3 节所述摄影智能体编辑流程中使用的提示。该流程包含三个阶段：用 ArtiMuse 做分维度评述生成、通过 LiteLLM 用 GPT 做编辑规划、用 Gemini-3-Pro-Image（Nano Banana Pro）做图像编辑。第 1 步中，ArtiMuse 以同一张图像按每个美学维度各查询一次，共独立查询八次。所得响应随后拼接为单一评述字符串，送入规划阶段。

**EN** H.1.1 Step 1: ArtiMuse Aspect-Wise Critique

**ZH** H.1.1 第 1 步：ArtiMuse 分维度评述

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

**EN** H.1.2 Step 2: Edit Planning

**ZH** H.1.2 第 2 步：编辑规划

**EN** The planning stage is executed with GPT through LiteLLM. Below we reproduce the literal runtime system and user messages. The placeholder {review} denotes the full ArtiMuse output obtained by concatenating the eight aspect-wise responses from Step 1. We retain the original runtime field names, including substyle.

**ZH** 规划阶段通过 LiteLLM 用 GPT 执行。下面原样复现运行时的系统与用户消息。占位符 {review} 表示由第 1 步八个分维度响应拼接得到的完整 ArtiMuse 输出。我们保留原始运行时字段名，包括 substyle。

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

**EN** H.1.3 Step 3: Image Editing

**ZH** H.1.3 第 3 步：图像编辑

**EN** The final stage uses Gemini-3-Pro-Image (Nano Banana Pro) to synthesize the edited variants. Round 1 generates the better image from the original image alone. Round 2 generates the worse image from the original image while conditioning on the better image as additional reference context. For Round 2, we report the file-backed with-context template actually used at runtime. This is the operative version loaded by the pipeline and therefore excludes the fallback sentence beginning with “Important: Apply this edit to the ORIGINAL image” that appears only in the default code path.

**ZH** 最后一阶段使用 Gemini-3-Pro-Image（Nano Banana Pro）合成编辑后的变体。第 1 轮仅由原图生成更好的图像。第 2 轮由原图生成更差的图像，同时以更好的图像作为附加参考上下文。对于第 2 轮，我们报告运行时实际使用的带上下文文件模板。这是流程加载的生效版本，因此不含仅出现在默认代码路径中、以“Important: Apply this edit to the ORIGINAL image”开头的回退句。

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

**EN** H.2 Illustration Pipeline Prompts

**ZH** H.2 插画流程提示

**EN** This subsection records the prompt templates used in the prompt-based illustration generation pipeline. We use one template for digital and AI art, concept art, and pixel art, and a separate storyboard-style template for anime and manga and comic generation. The stylized 3D subset is constructed through asset rendering rather than text-to-image prompting.

**ZH** 本小节记录基于提示的插画生成流程中使用的提示模板。我们对数字与 AI 艺术、概念艺术、像素艺术使用一个模板，对动画与漫画、漫画生成使用另一个分镜式模板。风格化三维子集通过资产渲染而非文生图提示构建。

**EN** H.2.1 Digital and AI Art / Concept Art / Pixel Art Generation

**ZH** H.2.1 数字与 AI 艺术／概念艺术／像素艺术生成

**EN** For digital and AI art, concept art, and pixel art generation, we use a structured template to control semantic content while allowing variation in visual execution. Each prompt is composed in a fixed order: subject or character, motion or action, environment or background, lighting condition, atmosphere or mood, camera or composition, and art style.

**ZH** 对于数字与 AI 艺术、概念艺术与像素艺术的生成，我们使用结构化模板，在控制语义内容的同时允许视觉呈现有所变化。每条提示按固定顺序组合：主体或角色、动作或行为、环境或背景、光照条件、氛围或情绪、相机或构图、艺术风格。

<!-- [原子块 · svg]  -->

**EN** H.2.2 Manga / Comic Storyboard Generation

**ZH** H.2.2 漫画／连环画分镜生成

**EN** For anime and manga and comic generation, we adopt a storyboard-style template with stronger structural constraints. Each prompt describes a short multi-panel narrative with consistent characters and environment, while each panel specifies shot type, character action, key props, and scene details.

**ZH** 对于动画与漫画、漫画的生成，我们采用结构约束更强的分镜式模板。每条提示描述一段包含多个分格的短叙事，角色与环境保持一致，每个分格指定景别、角色动作、关键道具与场景细节。

<!-- [原子块 · svg]  -->

**EN** H.3 MLLM Evaluation Prompts

**ZH** H.3 MLLM 评测提示

**EN** This subsection reports the generic prompts used to evaluate MLLMs on VAB. Depending on the task setting, the model is asked to identify the best image, the worst image, or both the best and the worst images in a candidate set.

**ZH** 本小节报告在 VAB 上评测 MLLM 所用的通用提示。根据任务设置，模型被要求找出候选集中的最优图像、最差图像，或同时找出最优与最差图像。

**EN** H.3.1 Best-Image Selection Prompt

**ZH** H.3.1 最优图像选择提示

<!-- [原子块 · svg]  -->

**EN** H.3.2 Worst-Image Selection Prompt

**ZH** H.3.2 最差图像选择提示

<!-- [原子块 · svg]  -->

**EN** H.3.3 Joint Best-and-Worst Selection Prompt

**ZH** H.3.3 最优与最差图像联合选择提示

<!-- [原子块 · svg]  -->

**EN** H.4 Reward-Model Scoring Interfaces

**ZH** H.4 奖励模型评分接口

**EN** This subsection records the model-specific scoring interfaces used to evaluate reward models on VAB. Unlike MLLMs, reward models do not share a single comparative prompt. Instead, each model scores images independently following its released evaluation method, and we convert the resulting per-image scores into within-task rankings. Across all reward models, each image is scored num_trials times, the scores are averaged, and the averaged scores are used to determine the predicted best and worst images. We use the following terminology: explicit prompt denotes prompt text exposed at the call site, implicit prompt denotes prompt text embedded inside the model library, and no prompt denotes a pure vision scorer with no language instruction.

**ZH** 本小节记录在 VAB 上评测奖励模型时所用、各模型专属的评分接口。与 MLLM 不同，奖励模型没有统一的比较提示，而是各自按其公开发布的评测方法独立为图像打分，我们再把得到的逐图像分数转换为任务内排序。对所有奖励模型，每张图像评分 num_trials 次，取平均后用平均分确定预测的最优与最差图像。我们使用如下术语：显式提示表示在调用处暴露的提示文本，隐式提示表示嵌入模型库内部的提示文本，无提示表示不含语言指令的纯视觉打分器。

**EN** H.4.1 ArtiMuse

**ZH** H.4.1 ArtiMuse

**EN** ArtiMuse uses an implicit prompt: the instruction is hardcoded inside the released library rather than passed from our evaluation script.

**ZH** ArtiMuse 使用隐式提示：指令硬编码在发布的库内部，而非由我们的评测脚本传入。

<!-- [原子块 · svg]  -->

**EN** At runtime, the library automatically prepends an image token before the instruction. The model outputs a two-letter code, which is then decoded back to a numerical score in ⟦SLOT_156⟧.

**ZH** 运行时，库会自动在指令前加上图像词元。模型输出一个双字母代码，再被解码回 ⟦SLOT_156⟧ 区间内的数值分数。

**EN** H.4.2 Q-Align

**ZH** H.4.2 Q-Align

**EN** Q-Align also uses an implicit prompt. In our experiments, we use the aesthetic scorer by default; the library additionally exposes a quality scorer.

**ZH** Q-Align 同样使用隐式提示。在我们的实验中默认使用美学打分器；该库另外还提供一个质量打分器。

<!-- [原子块 · svg]  -->

**EN** The scorer reads the last-token logits over the five words excellent, good, fair, poor, and bad, applies a softmax, and computes a weighted sum with weights ⟦SLOT_157⟧.

**ZH** 打分器读取 excellent、good、fair、poor、bad 五个词在末位词元上的 logits，施加 softmax，并以权重 ⟦SLOT_157⟧ 计算加权和。

**EN** H.4.3 Q-Instruct

**ZH** H.4.3 Q-Instruct

**EN** Q-Instruct uses an explicit prompt passed through the command-line interface.

**ZH** Q-Instruct 使用通过命令行接口传入的显式提示。

<!-- [原子块 · svg]  -->

**EN** The instruction is wrapped in the mplug_owl2 conversation format with a prepended DEFAULT_IMAGE_TOKEN. The default score is the logit difference between good and poor.

**ZH** 该指令被包装在 mplug_owl2 对话格式中，并在前面加上 DEFAULT_IMAGE_TOKEN。默认分数为 good 与 poor 的 logit 之差。

**EN** H.4.4 RealQA

**ZH** H.4.4 RealQA

**EN** RealQA uses an explicit prompt. Under the AVA adapter used in our experiments, the default instruction is:

**ZH** RealQA 使用显式提示。在我们实验所用的 AVA 适配器下，默认指令为：

<!-- [原子块 · svg]  -->

**EN** The model generates free text, from which a numerical score in ⟦SLOT_158⟧ is parsed. If parsing fails, the library issues a second constrained prompt:

**ZH** 模型生成自由文本，从中解析出 ⟦SLOT_158⟧ 区间内的数值分数。若解析失败，库会发出第二条约束提示：

<!-- [原子块 · svg]  -->

**EN** H.4.5 PEAS

**ZH** H.4.5 PEAS

**EN** PEAS-aes and PEAS-ava use no prompt. They are pure vision models with no language instruction. The scorer outputs a 10-bin distribution over scores from 1 to 10, and the final score is the expected value of that distribution.

**ZH** PEAS-aes 与 PEAS-ava 不使用提示。它们是不含语言指令的纯视觉模型。打分器输出 1 到 10 分上的 10 区间分布，最终分数为该分布的期望值。

<!-- [原子块 · svg]  -->

**EN** Appendix I Topic-Level Annotation Examples

**ZH** 附录 I 主题级标注示例

**EN** This appendix provides one representative annotation example for each of the 24 topics in VAB, grouped by domain.

**ZH** 本附录为 VAB 的 24 个主题各提供一个代表性标注示例，按领域分组。

**EN** I.1 Fine Art

**ZH** I.1 美术

**EN** Landscape Color

**ZH** 风景色彩

<!-- [原子块 · img]  -->

**EN** Still Life Color

**ZH** 静物色彩

<!-- [原子块 · img]  -->

**EN** Calligraphy

**ZH** 书法

<!-- [原子块 · img]  -->

**EN** Chinese Painting

**ZH** 中国画

<!-- [原子块 · img]  -->

**EN** Ink and Wash

**ZH** 水墨

<!-- [原子块 · img]  -->

**EN** Portrait Color

**ZH** 肖像色彩

<!-- [原子块 · img]  -->

**EN** Portrait Sketch

**ZH** 肖像速写

<!-- [原子块 · img]  -->

**EN** Quick Sketch

**ZH** 快速速写

<!-- [原子块 · img]  -->

**EN** Still Life Sketch

**ZH** 静物速写

<!-- [原子块 · img]  -->

**EN** I.2 Photography

**ZH** I.2 摄影

**EN** Architecture

**ZH** 建筑

<!-- [原子块 · img]  -->

**EN** Food and Product

**ZH** 美食与产品

<!-- [原子块 · img]  -->

**EN** Landscape

**ZH** 风景

<!-- [原子块 · img]  -->

**EN** Macro

**ZH** 微距

<!-- [原子块 · img]  -->

**EN** Night and Astrophotography

**ZH** 夜景与天文摄影

<!-- [原子块 · img]  -->

**EN** Portrait

**ZH** 人像

<!-- [原子块 · img]  -->

**EN** Sports

**ZH** 运动

<!-- [原子块 · img]  -->

**EN** Street and City

**ZH** 街头与城市

<!-- [原子块 · img]  -->

**EN** Wildlife

**ZH** 野生动物

<!-- [原子块 · img]  -->

**EN** I.3 Illustration

**ZH** I.3 插画

**EN** Anime and Manga

**ZH** 动画与漫画

<!-- [原子块 · img]  -->

**EN** Comic

**ZH** 漫画

<!-- [原子块 · img]  -->

**EN** Concept Art

**ZH** 概念艺术

<!-- [原子块 · img]  -->

**EN** Digital and AI Art

**ZH** 数字与 AI 艺术

<!-- [原子块 · img]  -->

**EN** Pixel Art

**ZH** 像素艺术

<!-- [原子块 · img]  -->

**EN** Stylized 3D

**ZH** 风格化三维

<!-- [原子块 · img]  -->
