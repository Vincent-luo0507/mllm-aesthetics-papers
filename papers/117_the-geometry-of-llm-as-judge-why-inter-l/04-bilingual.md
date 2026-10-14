# 以大模型为裁判的几何学：为何裁判间共识并不等于与人类对齐

> 原标题：The Geometry of LLM-as-Judge: Why Inter-LLM Consensus Is Not Human Alignment
> 作者：Sourabrata Mukherjee, Hamna Hamna, Kalika Bali, Sunayana Sitaram · arXiv:2606.03043 · 2026-06-02

**EN** [Page 1]

**ZH** 第 1 页

**EN** The Geometry of LLM-as-Judge: Why Inter-LLM Consensus Is Not

**ZH** 以大模型为裁判的几何学：为何裁判间共识并不等于

**EN** Human Alignment

**ZH** 与人类对齐

**EN** Sourabrata MukherjeeHamna HamnaKalika BaliSunayana SitaramMicrosoft Researcht-somukherje@microsoft.com

**ZH** Sourabrata Mukherjee、Hamna Hamna、Kalika Bali、Sunayana Sitaram · Microsoft Research · t-somukherje@microsoft.com

**EN** Abstract

**ZH** 摘要

**EN** LLM judges now score most open-ended NLPoutput, and their mutual agreement is routinelyread as evidence that the scores can be trusted.That reading is unsafe: judges may agree be-cause they capture quality, or because theyshare the same blind spots, and agreementstatistics alone cannot tell these apart. We de-velop a geometric test that can. Treating eachjudge’s scores as a vector, we measure spread,eﬀective rank, the angle to human scores, andthe judge–judge, judge–human, and human–human agreement triple for 42 judges on twocommunity-built Indic benchmarks coveringfour domains and eight languages. Every com-parison is reference-matched: a judge and aheld-out rater are scored against the same two-rater mean, since an averaged reference other-wise ﬂatters judges by several degrees. On sub-jective rubrics, judges agree with one anotheras much as humans do yet reach only 58–66%of human agreement: consensus on an axis hu-mans do not weight. On the one rubric with averiﬁable answer, most of that gap closes. En-sembles converge on the judges’ shared axisrather than the human one, and training widensscores without rotating them. Inter-judge agree-ment is evidence of human alignment only afterthis check passes.1

**ZH** 如今，开放式 NLP 输出的打分大多由大模型裁判完成，而裁判之间的相互一致被习惯性地读作分数可信的证据。这种读法并不安全：裁判达成一致，可能是因为捕捉到了质量，也可能是因为共享同一片盲区，仅凭一致性统计量无法区分这两种情形。我们提出一种可以区分的几何检验。把每个裁判的分数视为一个向量，我们测量其展布、有效秩、与人类分数的夹角，以及裁判—裁判、裁判—人类、人类—人类的一致性三元组；对象为 42 个裁判、两个社区构建的印度语系基准，覆盖 4 个领域与 8 种语言。所有比较都做了参考匹配：裁判与一位留出的人类评分者对着相同的两位评分者均值计分，因为若改用平均后的参考，裁判会被抬高好几个角度。在主观评分维度上，裁判彼此的一致程度与人类相当，却只达到人类一致性的 58–66%，并且常常集中在一条人类并不加权的轴上。在唯一一个有可核验答案的评分维度上，这一差距大部分被弥合。集成收敛到裁判共享的那条轴，而非人类的轴；训练把分数拉宽，却没有转动它们。只有通过这项检验之后，裁判间一致性才算得上是与人类对齐的证据。1

**EN** 1Introduction

**ZH** 1 引言

**EN** LLMs are now the default raters for open-ended text(Zheng et al., 2023; Chiang and Lee, 2023; Duboiset al., 2023). They track people closely when arubric has a checkable answer, and far less closelyon the subjective, multilingual, culturally situatedjudgements that dominate real deployments (Wanget al., 2024; Liu et al., 2023; Hada et al., 2024;Watts et al., 2024). Across meta-evaluations, one

**ZH** 大模型如今已是开放式文本的默认评分者（Zheng 等，2023；Chiang 与 Lee，2023；Dubois 等，2023）。当评分维度存在可核验的答案时，它们与人类贴合得很紧；而在主观的、多语言的、深植于文化语境的判断上则差得多——后者恰恰主导着真实部署（Wang 等，2024；Liu 等，2023；Hada 等，2024；Watts 等，2024）。在各类元评测中，一种

**EN** lopsided pattern recurs: judges agree strongly withone another while agreeing only weakly with peo-ple (Hada et al., 2024; Watts et al., 2024). How

**ZH** 失衡的模式反复出现：裁判彼此高度一致，却只与人类弱一致（Hada 等，2024；Watts 等，2024）。

**EN** 1Code and resources are publicly available.

**ZH** 1 代码与资源已公开。

**EN** that pattern is read decides evaluation practice. Ifjudges agree because they capture quality, ensem-bling them is sound and human annotation can bescaled back; if they agree because they share a blindspot, ensembling ampliﬁes the error exactly wherehuman judgement is scarcest. Agreement statis-tics cannot separate the two readings, because bothproduce the same numbers (Calderon et al., 2025).

**ZH** 如何解读这一模式，决定了评测实践。若裁判一致是因为捕捉到了质量，那么把它们集成起来就是稳妥的，人类标注也可以缩减；若它们一致是因为共享盲区，那么集成恰恰会在人类判断最稀缺的地方放大误差。一致性统计量无法区分这两种解读，因为二者产生的是同一组数字（Calderon 等，2025）。

**EN** We separate them by measuring the shape of thedisagreement rather than its size. Suppose humanjudgement varies along many independent aspectsof quality, while each judge’s scores move along afew, largely shared directions (Schütze, 1992; Aroraet al., 2018; Raghu et al., 2017). Judges built onoverlapping pre-training corpora and similar post-training objectives (Ouyang et al., 2022; Bai et al.,2022) are exactly where this should occur, and ityields a prediction that agreement scores cannottest: judge and human scores should sit at a wideangle in score space, and averaging more judgesshould not close it. Throughout, “subspace,” “axis,”and “projection” name patterns in the scores weobserve, never computation inside a model.

**ZH** 我们通过测量分歧的形状而非大小来区分二者。假设人类判断沿质量的许多独立方面变化，而每个裁判的分数只沿少数几条、且大体共享的方向移动（Schütze，1992；Arora 等，2018；Raghu 等，2017）。建立在重叠预训练语料与相似后训练目标之上的裁判（Ouyang 等，2022；Bai 等，2022），正是这种情况最可能发生的地方；它给出了一致性分数无法检验的预测：裁判与人类的分数在分数空间中应呈大夹角，而平均更多裁判并不能把夹角合拢。全文中的“子空间”“轴”“投影”指的都是我们在分数中观察到的模式，绝非模型内部的计算。

**EN** We test this prediction on two community-builtIndic benchmarks: real-world cultural QA(Watts et al., 2024), with eight Indic languages,three domains, and three independent raters peritem, and community-health (Hamna et al., 2026;Bhat et al., 2025), judged by 14 base LLMs and27 trained variants of three open families (Brownet al., 2020; Rafailov et al., 2023). One measure-ment choice carries much of the weight. A judgecompared against the average of several raters hasan easier target than a rater compared against asingle colleague, and the diﬀerence is worth sev-eral degrees; wherever we compare a judge with aperson, we therefore hold out one rater and scoreboth against the remaining two. Under this matchedcomparison the prediction holds. On every subjec-tive rubric, judges agree with each other about asmuch as people do while reaching only 58–66% of

**ZH** 我们在两个社区构建的印度语系基准上检验这一预测：真实世界文化问答（Watts 等，2024），含 8 种印度语言、3 个领域、每条 3 位独立评分者；以及社区健康（Hamna 等，2026；Bhat 等，2025），由 14 个基座大模型与 3 个开放系列的 27 个训练变体担任裁判（Brown 等，2020；Rafailov 等，2023）。其中一项测量选择承担了大部分论证分量。把裁判对着若干评分者的均值比较，比把一位评分者对着一位同事比较要容易，二者相差好几个角度；因此凡是把裁判与人比较之处，我们都留出一位评分者，让双方都对着剩下两位计分。在这种匹配比较下，预测成立。在每一个主观评分维度上，裁判彼此的一致程度与人类相当，却只达到 58–66%

**EN** [Page 2]

**ZH** 第 2 页

**EN** CONSENSUS̸ = ALIGNMENT

**ZH** 共识 ≠ 对齐

**EN** judges agree with one an-other as much as people do(rll ≈rhh) yet reach only58–66% of human agreement

**ZH** 裁判彼此的一致程度与人类相当（rll ≈ rhh），却只达到人类一致性的 58–66%

**EN** VERIFIABILITY CLOSES IT

**ZH** 可核验性弥合了它

**EN** with a checkable answer thecohort lands 4.3◦from its ﬂoor

**ZH** 在有可核验答案处，裁判群体落在其基线的 4.3° 之内

**EN** and the best judge sits inside it

**ZH** 而最好的裁判落在基线之内

**EN** 90◦90◦angles open from the human axis

**ZH** 90° 90°：从人类轴张开的角

**EN** community-

**ZH** 社区

**EN** health

**ZH** 健康

**EN** real-worldcultural qa

**ZH** 真实世界文化问答

**EN** human axis

**ZH** 人类轴

**EN** FAIR COMPARISON

**ZH** 公平比较

**EN** every angle is reference-matched:judge and held-out rater are scoredagainst the same two-rater mean

**ZH** 每一个角都做了参考匹配：裁判与留出的人类评分者对着相同的两位评分者均值计分

**EN** OBJECTIVE · TASK QUALITY

**ZH** 客观 · 任务质量

**EN** cohort 60.7◦vs. ﬂoor 56.4◦

**ZH** 裁判群体 60.7°，基线 56.4°

**EN** gap 4.3◦· best judge 55.3◦: inside

**ZH** 差距 4.3° · 最佳裁判 55.3°：落在基线之内

**EN** SUBJECTIVE · LA, HAL

**ZH** 主观 · 语言可接受性、幻觉

**EN** judges 73.1–75.4◦· gap 9–11◦

**ZH** 裁判 73.1–75.4° · 差距 9–11°

**EN** ﬂoor 63.8–64.4◦

**ZH** 基线 63.8–64.4°

**EN** chance (null) 88.7◦

**ZH** 随机（零假设）88.7°

**EN** HOW TO READ

**ZH** 如何读图

**EN** solid arrows = the judges · dashedray = matched human ﬂoor · shadedwedge = the gap · grey dashes =chance

**ZH** 实线箭头 = 裁判 · 虚线射线 = 匹配的人类基线 · 阴影楔形 = 差距 · 灰色虚线 = 随机

**EN** COMMUNITY-HEALTH · 4RUBRICS

**ZH** 社区健康 · 4 个评分维度

**EN** judges 83.5–85.5◦from the mergedrater pool (no ﬂoor exists)only 2–4◦better than chance

**ZH** 裁判距合并评分者池 83.5–85.5°（无基线可画），仅比随机好 2–4°

**EN** chance (null) 87.7◦

**ZH** 随机（零假设）87.7°

**EN** THE DATA

**ZH** 数据

**EN** 42 LLM judges (15 base + 27 trained)· 2 Indic benchmarks · 4 domains · 8languages · 170,890 judge calls, 87,618human labels

**ZH** 42 个大模型裁判（15 个基座 + 27 个训练变体）· 2 个印度语系基准 · 4 个领域 · 8 种语言 · 170,890 次裁判调用，87,618 条人类标注

**EN** THE BOUNDARY

**ZH** 边界

**EN** a dimensionality dR read from thehuman raters alone predicts the regimebefore any LLM runs; rank alone doesnot (r 0.12)

**ZH** 仅从人类评分者读出的维度数 dR，可在任何大模型运行之前预测其所处机制；仅凭秩做不到（r = 0.12）

**EN** WHAT TRAINING MOVES

**ZH** 训练改变了什么

**EN** 18%residual 79%rotate 2.8%

**ZH** 拉伸 18% · 残差 79% · 旋转 2.8%

**EN** spread recovers 0.32 →1.08, yet θ isstuck at 87–88◦: almost nothing turnstoward the human axis

**ZH** 展布从 0.32 恢复到 1.08，但 θ 卡在 87–88°：几乎没有转向人类轴

**EN** THE RULE

**ZH** 规则

**EN** trust inter-LLM consensus only after thegeometric check passes – ensemblingstalls at the judges’ shared axis (App. B)

**ZH** 只有在几何检验通过之后才信任裁判间共识——集成会停滞在裁判共享的轴上（附录 B）

**EN** Figure 1: Angles open from the vertical human axis: solid arrows mark where LLM judges sit, dashed rays theirmatched human ﬂoor, and the shaded wedge between them, bracketed at the rim, is the gap this paper measures. Onthe one rubric with a checkable answer (teal) the cohort lands 4.3◦from its ﬂoor and the best judge inside it; onthe subjective rubrics (terracotta) the wedge opens to 9–11◦even though judges agree with one another as much aspeople do. On community-health (left half) a single merged rater pool leaves no ﬂoor to draw, and the judges landonly 2–4◦from chance. The plates below the baseline carry the data, the boundary result, what training moves, andthe rule. All quantities are observed score covariance, never model internals.

**ZH** 图 1：从竖直的人类轴张开的角：实线箭头标出各个大模型裁判所在的位置，虚线射线是它们各自匹配的人类基线，二者之间的阴影楔形（外缘以括号标出）就是本文测量的差距。在唯一一个有可核验答案的评分维度上（青色），裁判群体落在其基线的 4.3° 之内，最佳裁判落在基线之内；在主观评分维度上（赭红色），即便裁判彼此的一致程度与人类相当，楔形仍张开到 9–11°。左半部分的社区健康只有一个合并的评分者池，画不出基线，裁判距随机仅 2–4°。基线下方的几块牌面分别给出数据、边界结果、训练改变了什么，以及规则。所有量都来自观测到的分数协方差，绝非模型内部。

**EN** that agreement with people, sitting 9–11◦outsidethe human ﬂoor and using well under the humanscore range. The one rubric with a veriﬁable answercloses most of the gap. Training widens a judge’sscores but barely rotates them (Fig. 1).

**ZH** 与人类一致的水平：落在人类基线之外 9–11°，且用掉的分数区间远小于人类。唯一一个有可核验答案的评分维度弥合了大部分差距。训练拉宽了裁判的分数，却几乎没有转动它们（图 1）。

**EN** Contributions.This paper contributes: (1) a re-porting frame that separates judge–judge, judge–human, and human–human agreement on a matchedreference, with the geometric account scoped as adiagnostic over observed scores (Sec. 3); (2) fourscore-space diagnostics, validated by permutation,FDR, ordinal, human-reference, self-preference,and split-half controls that the collapse pattern sur-vives (Sec. 5.4); (3) a falsiﬁable boundary: a dimen-sionality computed from human raters alone, beforeany LLM is run, predicts which regime a rubricfalls in, with rank necessary and orientation deci-sive; (4) an anatomy of repair, showing that trainingrestores spread rather than orientation and that en-sembling converges on the judges’ shared axis; and(5) a complete release that reproduces every num-ber in this paper with one command (App. O). Agap to human judgement survives every trainingstage we tried, so multi-perspective human ratingremains necessary.

**ZH** 本文贡献如下：(1) 一种报告框架，在匹配参考之上把裁判—裁判、裁判—人类、人类—人类的一致性分开呈现，并把几何解释严格限定为对观测分数的诊断（第 3 节）；(2) 四项分数空间诊断指标，并用置换、错误发现率（FDR）、序数、人类参考、自我偏好与分半等控制检验确认坍缩模式依然成立（第 5.4 节）；(3) 一条可证伪的边界：一个在任何大模型运行之前、仅由人类评分者算出的维度数，可预测某个评分维度落入哪种机制，其中秩是必要条件而方向是决定性的；(4) 一份修复机制的解剖，表明训练恢复的是展布而非方向，且集成收敛到裁判共享的轴；以及 (5) 一份完整的发布物，一条命令即可复现本文的每一个数字（附录 O）。在我们尝试的每一个训练阶段之后，与人类判断的差距依然存在，因此多视角的人类评分仍然不可或缺。

**EN** 2Related Work

**ZH** 2 相关工作

**EN** LLM-as-judge was adopted because it tracks hu-mans on open-ended generation (Chiang and Lee,2023; Zheng et al., 2023; Kocmi and Federmann,2023; Dubois et al., 2023), and the reliability litera-ture documented where it does not: ﬂuency and ver-bosity bias, self-preference, and degradation on non-English and culturally situated content (Wang et al.,2024; Zheng et al., 2023; Hada et al., 2024; Wattset al., 2024; Hershcovich et al., 2022). Calderonet al. (2025) argue that agreement statistics alonecannot separate a reliable judge from a plausibleone. Our alternative is diagnostic: rather than askhow large the LLM–human gap is, we ask whatshape it has, and show the shape predicts whenconsensus may be trusted.

**ZH** 以大模型为裁判之所以被采用，是因为它在开放式生成上能跟踪人类（Chiang 与 Lee，2023；Zheng 等，2023；Kocmi 与 Federmann，2023；Dubois 等，2023），而可靠性文献则记录了它失效的地方：流畅度与冗长偏好、自我偏好，以及在非英语与深植于文化的内容上的退化（Wang 等，2024；Zheng 等，2023；Hada 等，2024；Watts 等，2024；Hershcovich 等，2022）。Calderon 等（2025）论证，仅凭一致性统计量无法区分一个可靠的裁判与一个貌似可信的裁判。我们的替代方案是诊断式的：不去问大模型—人类的差距有多大，而问它是什么形状，并表明形状可以预测共识何时可信。

**EN** Consensus is where this matters most. Ensembleand panel protocols treat inter-judge agreement asreliability (Zheng et al., 2023), assuming averagingcancels idiosyncratic bias. That fails if judges sharethe bias: models trained on overlapping corporawith similar post-training objectives (Ouyang et al.,2022; Bai et al., 2022) can covary strongly whilejointly missing a human-weighted direction. Wemake that failure measurable, and show ensembling

**ZH** 共识正是这一点最要紧的地方。集成与专家小组协议把裁判间一致性当作可靠性（Zheng 等，2023），假定平均可以抵消个体偏差。若裁判共享这一偏差，该假定就不成立：训练于重叠语料、后训练目标相似的模型（Ouyang 等，2022；Bai 等，2022）可能强相关，同时共同漏掉一个人类加权的方向。我们让这种失效变得可测量，并表明集成

**EN** [Page 3]

**ZH** 第 3 页

**EN** converges on the cohort’s own axis (Sec. 5.6).

**ZH** 收敛到裁判群体自身的轴上（第 5.6 节）。

**EN** Our instruments come from representationalanalysis: principal angles and canonical correlation(Björck and Golub, 1973; Knyazev and Argentati,2002; Raghu et al., 2017), applied to scores ratherthan activations, which keeps the analysis model-agnostic and usable on closed APIs at the cost of adiagnostic rather than mechanistic lens (Sec. 3).

**ZH** 我们的工具来自表示分析：主角度与典型相关（Björck 与 Golub，1973；Knyazev 与 Argentati，2002；Raghu 等，2017），但作用于分数而非激活，这使分析与模型无关、可用于闭源 API，代价是它只是一面诊断的透镜，而非机理性的（第 3 节）。

**EN** The setting is Indic NLP, a testbed for cross-lingual judge reliability (Watts et al., 2024; Hadaet al., 2024). Our benchmarks supply complemen-tary halves of what the diagnostics need: real-world cultural QA (Watts et al., 2024) givesthree independent raters per item, which makes ahuman ﬂoor measurable at all, while community-health (Hamna et al., 2026; Bhat et al., 2025) givesjudge breadth. We evaluate four standard repairs(Brown et al., 2020; Ouyang et al., 2022; Rafailovet al., 2023; Hu et al., 2022; Platt, 1999; Guo et al.,2017); new here is the decomposition (Sec. 5.8)separating ampliﬁcation of a judge’s ranking fromrotation toward humans.

**ZH** 实验场景是印度语系 NLP，它是跨语言裁判可靠性的试验场（Watts 等，2024；Hada 等，2024）。两个基准提供了诊断所需的互补两半：真实世界文化问答（Watts 等，2024）给出每条 3 位独立评分者，这才使人类基线可测；社区健康（Hamna 等，2026；Bhat 等，2025）则给出裁判的广度。我们评估四种常见修复手段（Brown 等，2020；Ouyang 等，2022；Rafailov 等，2023；Hu 等，2022；Platt，1999；Guo 等，2017）；本文新提出的是那一分解（第 5.8 节），它把“放大裁判自身的排序”与“朝人类方向旋转”区分开来。

**EN** 3A Geometric Lens on Judge ScoreMatrices

**ZH** 3 裁判分数矩阵的几何视角

**EN** This section deﬁnes what the paper measures. Itis a diagnostic lens over observed scores: “projec-tion,” “subspace,” and “axis” refer to structure inobserved score covariance, never to internal LLMcomputation. Every analysis operates on per-judgescore matrices SJ ∈Rn×m (n items, m rubrics;columns mean-centered). Two constructions re-cur: per-rubric, where a judge column s meetsa reference column h and the angle reduces ex-actly to θ = arccos |r(s, h)| for Pearson r; andstacked, the largest principal angle (Björck andGolub, 1973; Knyazev and Argentati, 2002) be-tween the 95%-energy singular bases of the fullmatrices. App. D expands this section with the ide-alised picture, the worked identity, and the bound-ary case analysis; App. L gives procedures, pre-processing/cutoﬀgrids, and the permutation-nullbaseline; App. N reconciles the constructions nu-merically.

**ZH** 本节定义本文测量什么。它是对观测分数的诊断透镜：“投影”“子空间”“轴”指的是观测分数协方差中的结构，与大模型内部计算无关。每一项分析都作用于单个裁判的分数矩阵 SJ ∈ Rn×m（n 个条目、m 个评分维度；各列已中心化）。两种构造反复出现：逐维度构造，即裁判的一列 s 与参考列 h 相对，角度恰好化为 θ = arccos |r(s, h)|，r 为 Pearson 相关系数；以及堆叠构造，即两个完整矩阵的 95% 能量奇异基之间的最大主角度（Björck 与 Golub，1973；Knyazev 与 Argentati，2002）。附录 D 展开本节的理想化图景、算通的恒等式与边界情形分析；附录 L 给出流程、预处理／截断网格与置换零假设基线；附录 N 从数值上调和两种构造。

**EN** We track four diagnostics.(i) Spread ratio σJ /σH:judge over human-reference score SD, per rubric.(ii) Effective rank

**ZH** 我们追踪四项诊断指标。(i) 展布比 σJ/σH：逐评分维度上裁判分数标准差与人类参考分数标准差之比。(ii) 有效秩

**EN** rJ

**ZH** rJ

**EN** 95 = min

**ZH** 95 = min

**EN** k : P

**ZH** k : P

**EN** i≤k λi

**ZH** i≤k λi

**EN** P

**ZH** P

**EN** i λi ≥0.95

**ZH** i λi ≥0.95

**EN** (Jolliﬀe and Cadima, 2016): how many inde-

**ZH** （Jolliffe 与 Cadima，2016）：裁判的分数动用了多少条

**EN** pendent directions the judge’s scores use.(iii) Principal angle θ(SJ , SH), always read against

**ZH** 独立方向。(iii) 主角度 θ(SJ, SH)，始终对着

**EN** a reference-matched inter-human ﬂoor (wheremultiple raters exist; Sec. 5) and a permuta-tion null: near-orthogonality is generic in highdimension, so an angle is informative only rel-ative to that null.(iv) The agreement triple rll, rlh, rhh, reported to-

**ZH** 一条参考匹配的人类间基线（在存在多位评分者之处；第 5 节）与一个置换零假设来读：高维下近似正交是常态，因此角度只有相对于该零假设才有信息量。(iv) 一致性三元组 rll、rlh、rhh，

**EN** gether, never as one aggregate.

**ZH** 一起报告，绝不合并成一个聚合值。

**EN** Boundary: rank necessary, orientation decisive.Let dR measure the dimensionality of human raterdisagreement under rubric R, computed from hu-man raters alone as the participation ratio of thecentered items×raters matrix,

**ZH** 边界：秩是必要条件，方向才是决定性的。设 dR 度量评分维度 R 下人类评分者分歧的维度数，它仅由人类评分者算出，取中心化后的“条目×评分者”矩阵的参与率，

**EN** dR =

**ZH** dR =

**EN** P

**ZH** （Σ

**EN** i λi

**ZH** i λi

**EN** 2. P

**ZH** ）² / Σ

**EN** i λ2

**ZH** i λi²

**EN** i ,(1)

**ZH** ，(1)

**EN** with λi the squared singular values. Note dR ≤Rfor R raters, so with three raters it is capped at 3 andreports disagreement dimensionality at that panelsize, not the intrinsic dimensionality of human qual-ity. A cohort with kJ < dR cannot represent thehuman variation, so kJ ≥dR is necessary, butnot suﬃcient, since a judge may spend its rank ondirections humans ignore. The decisive quantityis orientation. For a single direction the relation-ship is an identity rather than an analogy: sincecos θ = |r|,

**ZH** 其中 λi 为平方奇异值。注意 dR ≤ R（R 为评分者数），因此在三位评分者时它的上限为 3，报告的是该规模评分小组的分歧维度，而非人类质量的内在维度。若裁判群体的 kJ < dR，它就无法表示人类的变异，故 kJ ≥ dR 是必要的，但并不充分，因为裁判可能把秩花在人类并不在意的方向上。决定性的量是方向。对单一方向而言，这种关系是恒等式而不仅是类比：由于 cos θ = |r|，

**EN** 1 −cos2 θ(s, h) = 1 −r2,(2)

**ZH** 1 − cos²θ(s, h) = 1 − r²，(2)

**EN** which is exactly the fraction of human score vari-ance that direction leaves unexplained; App. Dworks the numbers through and connects them tothe ridge estimates. A stronger, rank-only gate isfalsiﬁed by our own measurements (r95 does notpredict alignment, r = 0.12; Sec. 5.4). A judgeis rank-matched on a rubric when its angle beatsthe permutation null and reaches the matched inter-human ﬂoor with rlh ≈rhh.

**ZH** 这恰好是该方向未能解释的人类分数方差比例；附录 D 把数字算通并与岭回归估计相连。一个更强、只看秩的判据被我们自己的测量所否证（r95 不能预测对齐，r = 0.12；第 5.4 节）。当某裁判在一个评分维度上的角度优于置换零假设，并在 rlh ≈ rhh 的意义上达到匹配的人类间基线时，我们称它在该维度上秩匹配。

**EN** Falsifiable predictions.Tested in Sec. 5: P1judges compress spread on subjective rubrics; P2judge eﬀective rank sits at or below the human ref-erence’s; P3 on the three-rater benchmark, judge–human angles exceed the matched inter-human ﬂooron subjective rubrics and approach it on the objec-tive one, signiﬁcantly below the permutation nullin both regimes; P4 rll >rlh on subjective rubricsvia a dominant shared score axis, measurable by co-hort PCA; P5 dR from humans alone separates theregimes; P6 rank alone does not predict alignment;

**ZH** 可证伪的预测。第 5 节检验如下：P1 裁判在主观评分维度上压缩展布；P2 裁判的有效秩不高于人类参考的；P3 在三评分者基准上，裁判—人类夹角在主观维度上超出匹配的人类间基线，而在客观维度上逼近它，两种机制下都显著低于置换零假设；P4 主观维度上 rll > rlh，由一条占主导的共享分数轴造成，可用裁判群体主成分分析测量；P5 仅由人类算出的 dR 能区分两种机制；P6 仅凭秩不能预测对齐；

**EN** [Page 4]

**ZH** 第 4 页

**EN** orientation does. The lens predicts which rubricsfail and the shape of failure, not which interventionrepairs it (Sec. 5.7).

**ZH** 方向则可以。该透镜预测哪些评分维度会失败以及失败的形态，而不预测哪种干预能修复它（第 5.7 节）。

**EN** 4Experimental Setup

**ZH** 4 实验设置

**EN** Thestudyspans170,890LLM-judgecalls(≈474,310 rubric-level scores and preferencelabels) over two community-built Indic benchmarkscovering four domains, eight Indic languages, and42 distinct LLM judges (15 base models plus 27ﬁne-tuned, preference-optimised, few-shot, orcalibrated variants), evaluated against four humanreference pools (≈87,618 human labels; App. E).Every roster, per-cell count, and event total isregenerated from the released data by one script(App. O).

**ZH** 本研究涵盖 170,890 次大模型裁判调用（约 474,310 个评分维度级分数与偏好标签），覆盖两个社区构建的印度语系基准、4 个领域、8 种印度语言，以及 42 个不同的大模型裁判（15 个基座模型加 27 个微调、偏好优化、少样本或校准变体），对照 4 个人类参考池（约 87,618 条人类标注；附录 E）。每一份名单、每个单元的计数与事件总量，都由发布的数据经一个脚本重新生成（附录 O）。

**EN** Datasets and languages.community-health(Samiksha (Hamna et al., 2026; Bhat et al., 2025);CH) is a medical-advisory benchmark in Hindi,Kannada, and Malayalam: 810 questions (270/lan-guage), each answered by three generator LLMs (=2,430 scored QA pairs) with paired standalone andcomparative human labels; all geometric/traininganalyses use its 405-item core (45×3×3, the subsetwith complete topic metadata), comparative agree-ment the full pair set. real-world cultural QA(Pariksha (Watts et al., 2024); DLQ, daily-life QA)contributes health & wellness, finance, and every-day life with three independent raters per item; weretain the 1,182 items all three raters completed(300 Hindi down to 60 Odia; Table 8), from 27answer generators. The eight analysed languages(Bengali, Hindi, Kannada, Malayalam, Marathi,Odia, Tamil, Telugu) span Indo-Aryan and Dravid-ian families; DLQ’s comparative split (which addsGujarati and Punjabi) is excluded from analysis (asingle LLM judge with a label-orientation artefact;App. M) and counted only in event totals.

**ZH** 数据集与语言。community-health（Samiksha，Hamna 等，2026；Bhat 等，2025；简称 CH）是一个印地语、卡纳达语、马拉雅拉姆语的医疗咨询基准：810 道问题（每语言 270 道），每道由 3 个生成式大模型作答（= 2,430 个待评问答对），并配成对的独立评分与对比评分人类标注；所有几何／训练分析使用其 405 条核心条目（45×3×3，即主题元数据完整的子集），对比一致性则用完整的问答对集。real-world cultural QA（Pariksha，Watts 等，2024；DLQ，日常生活问答）贡献了健康养生、金融与日常生活三个领域，每条 3 位独立评分者；我们保留三位评分者都评完的 1,182 条（印地语 300 条，最少的是奥里亚语 60 条；表 8），来自 27 个回答生成器。所分析的 8 种语言（孟加拉语、印地语、卡纳达语、马拉雅拉姆语、马拉地语、奥里亚语、泰米尔语、泰卢固语）横跨印度—雅利安语系与达罗毗荼语系；DLQ 的对比评分切分（额外包含古吉拉特语与旁遮普语）被排除在分析之外（只有一个大模型裁判，且存在标签方向性假象；附录 M），只计入事件总量。

**EN** Judges.15 base LLMs cover closed-API fron-tier, open multilingual, and Indic-focused families(open weights 12B–671B): 14 judge CH, 5 judgeDLQ (deepseek-r1, gpt-4, grok-4, mistral-large-3,llama-3.3-70b), four anchoring both. Three Indic-capable open families (sarvam-m-24b, gemma-3-27b, aya-expanse-32b) are exercised on CHunder six techniques:few-shot (Brown et al.,2020), LoRA SFT (Hu et al., 2022; Ouyang et al.,2022), DPO (Rafailov et al., 2023), SFT+DPO,demonstration-augmented SFT (demos baked intotraining prompts), and demonstration-anchored cal-

**ZH** 裁判。15 个基座大模型覆盖闭源 API 前沿、开放多语言与面向印度语系三个系列（开放权重 12B–671B）：14 个评 CH，5 个评 DLQ（deepseek-r1、gpt-4、grok-4、mistral-large-3、llama-3.3-70b），其中 4 个同时锚定两个基准。3 个具备印度语能力的开放系列（sarvam-m-24b、gemma-3-27b、aya-expanse-32b）在 CH 上接受六种技术的检验：

**EN** ibration (a frozen trained checkpoint scored withk human-rated demos in context); SFT/DPO trainon held-out CH-source labels with zero questionoverlap with the evaluation set. Rosters, recipes,hyper-parameters: Tables 10–15; API versions andcall dates: App. O.

**ZH** 少样本（Brown 等，2020）、LoRA SFT（Hu 等，2022；Ouyang 等，2022）、DPO（Rafailov 等，2023）、SFT+DPO、演示增强 SFT（把演示样例烘进训练提示），以及演示锚定校准（用冻结的训练检查点，在上下文中放入 k 个人类评过的演示样例后计分）；SFT／DPO 在留出的 CH 源标签上训练，与评测集零问题重叠。名单、配方与超参数见表 10–15；API 版本与调用日期见附录 O。

**EN** Every QA pair is scored under two paradigms.Standalone: per-rubric ordinal scores over foursubjective CH rubrics (clarity, helpfulness, accu-racy, completeness) plus three DLQ rubrics: taskquality (the single objective rubric: veriﬁable taskconstraints), linguistic acceptability, and hallucina-tions (Chiang and Lee, 2023; Watts et al., 2024).Comparative: judges pick the better of two an-swers. The paradigms separate calibration fromrank-ordering failures (Zheng et al., 2023; Liuet al., 2023); deﬁnitions and verbatim prompts inApp. G, I.

**ZH** 每个问答对在两种范式下计分。独立评分：逐评分维度的序数分数，覆盖 CH 的 4 个主观维度（清晰性、有用性、准确性、完整性）与 DLQ 的 3 个维度：任务质量（唯一的客观维度：可核验的任务约束）、语言可接受性与幻觉（Chiang 与 Lee，2023；Watts 等，2024）。对比评分：裁判在两个答案中挑出更好的一个。两种范式把校准失效与排序失效区分开来（Zheng 等，2023；Liu 等，2023）；定义与逐字提示见附录 G、I。

**EN** Measurement and inference.Per (judge, rubric,language, domain, eval type) slice we compute theSec. 3 diagnostics: the agreement triple (quadratic-weighted κ in App. M); Cohen’s κ (Cohen, 1960) oncomparative panels; σJ /σH; r95; and θ against thematched human ﬂoor and permutation null (App. L).The training analysis uses a paired item bootstrap(Efron, 1979), B = 1000 over the 405 core itemswith rows reused across (family, stage); with n=3trainable families the smallest one-sided Wilcoxon(Wilcoxon, 1945) p is 0.125, so Wilcoxon is only adirectional summary.

**ZH** 测量与推断。对每个（裁判、评分维度、语言、领域、评测类型）切片，我们计算第 3 节的诊断指标：一致性三元组（附录 M 中用二次加权 κ）、对比评分面板上的 Cohen's κ（Cohen，1960）、σJ/σH、r95，以及相对匹配人类基线与置换零假设的 θ（附录 L）。训练分析使用配对条目自助法（Efron，1979），在 405 条核心条目上取 B = 1000，且各（系列、阶段）之间复用同一组行；由于可训练系列只有 n = 3，单侧 Wilcoxon（Wilcoxon，1945）的最小 p 为 0.125，故 Wilcoxon 只作为方向性摘要。

**EN** 5Empirical Analysis

**ZH** 5 实证分析

**EN** Four analyses plus controls test the geometric ac-count: agreement, boundary, geometry, controls(testing P1–P6; Sec. 5.4), and training.

**ZH** 四项分析加控制检验构成对几何解释的检验：一致性、边界、几何、控制（检验 P1–P6；第 5.4 节）与训练。

**EN** One construction per comparison.Two conven-tions govern every number below, since mixingthem is the easiest way to manufacture a result. (i)All three legs of an agreement triple are pairwise(rater vs. rater): correlating a judge with the mean ofthree raters gives it a less noisy target than the othertwo legs face, which on task quality alone movesrlh from 0.418 to 0.519 and would lift judges abovethe human ﬂoor. (ii) Every angle compared witha human ﬂoor is reference-matched: one rater isheld out and the mean of the other two is the singlereference that this rater and each judge are scoredagainst. App. N reconciles the constructions.

**ZH** 每次比较只用一种构造。下面每个数字都受两条约定约束，因为混用构造是制造结果最容易的方式。(i) 一致性三元组的三条腿都是成对的（评分者对评分者）：把裁判与三位评分者的均值求相关，等于给它一个噪声更小的靶子，而另外两条腿面对的不是这个靶子；仅就任务质量而言，这会把 rlh 从 0.418 抬到 0.519，并使裁判显得高于人类基线。(ii) 凡是与人类基线比较的角度都做了参考匹配：留出一位评分者，其余两位的均值作为唯一参考，该留出者与每个裁判都对着它计分。附录 N 对两种构造作数值调和。

**EN** [Page 5]

**ZH** 第 5 页

**EN** 0.00.10.20.30.40.50.6Pearson r

**ZH** 0.0 0.1 0.2 0.3 0.4 0.5 0.6 Pearson r

**EN** CH·clarity

**ZH** CH·清晰性

**EN** CH·accuracy

**ZH** CH·准确性

**EN** CH·helpful

**ZH** CH·有用性

**EN** CH·complete

**ZH** CH·完整性

**EN** DLQ·task quality

**ZH** DLQ·任务质量

**EN** DLQ·ling. accept.

**ZH** DLQ·语言可接受性

**EN** DLQ·halluc.

**ZH** DLQ·幻觉

**EN** LLM–humanLLM–LLMhuman–human

**ZH** 大模型—人类、大模型—大模型、人类—人类

**EN** Figure 2: Segment length = the LL−LH gap, all legspairwise. Extended caption in Table 6.

**ZH** 图 2：线段长度 = 大模型间与大模型—人类之差，三条腿全部成对。扩展图注见表 6。

**EN** 5.1Inter-LLM consensus versusLLM–human agreement

**ZH** 5.1 裁判间共识与大模型—人类一致性

**EN** On real-world cultural QA’s subjective rubricsthe three legs separate cleanly: judges agree witheach other about as much as humans agree with eachother (rll 0.356 vs. rhh 0.357 on linguistic accept-ability; 0.349 vs. 0.364 on hallucinations) whileagreeing with humans far less (0.207, 0.239, i.e.58% and 66% of the inter-human level). Match-ing inter-human consensus without matching inter-human agreement is the paper’s central observation:consensus is reached on a diﬀerent axis. The col-lapse is strongest on community-health (41–64%of inter-LLM across four rubrics), and its compar-ative split sharpens it in preference space: LLM–LLM κ = 0.445 vs. LLM–human κ = 0.128, a3.5× gap (base judges, 2, 430 pairs, three-class κ).Table 1A gives the full triple and the matched an-gles; Fig. 2 maps every cell’s gap.

**ZH** 在真实世界文化问答的主观评分维度上，三条腿清晰分离：裁判彼此的一致程度与人类彼此的一致程度相当（语言可接受性上 rll 0.356 对 rhh 0.357；幻觉上 0.349 对 0.364），而与人类的一致程度则低得多（0.207、0.239，即人类间水平的 58% 与 66%）。达到了人类间的共识水平，却没达到人类间的一致水平，这是本文的核心观察：共识是在另一条轴上达成的。坍缩在社区健康上最强（四个维度上为裁判间一致性的 41–64%），其对比切分在偏好空间中把这一点锐化得更清楚：大模型—大模型 κ = 0.445 对大模型—人类 κ = 0.128，相差 3.5 倍（基座裁判，2,430 对，三分类 κ）。表 1A 给出完整的三元组与匹配角度；图 2 标出每个单元的差距。

**EN** 5.2The boundary is rubric-conditional

**ZH** 5.2 边界取决于评分维度

**EN** The strongest reading of consensual blindness, thatLLM judges are generically unreliable, is falsiﬁedby real-world cultural QA: with the same items,the same ﬁve judges (deepseek-r1, gpt-4, grok-4,mistral-large-3, llama-3.3-70b), and the same threehumans, task quality lifts LLM–human agreementto 0.418, or 88% of the inter-human level (0.474),against 58% and 66% on the two subjective rubrics.The angle tells the same story with the referencematched: judges sit 60.7◦from the two-rater ref-erence where a held-out human sits 56.4◦, a gapof 4.3◦, against 11.0◦and 9.3◦on the subjectiverubrics. The best single judge (55.3◦) is inside thehuman ﬂoor on task quality; on both subjectiverubrics the best judge (67.3◦, 70.8◦) remains welloutside it. Figure 3 shows this item by item: thesubjective clouds stay ﬂat against the identity line,task quality tracks it.

**ZH** 对“共谋式盲区”最强的解读——大模型裁判普遍不可靠——被真实世界文化问答所否证：在同样的条目、同样的五个裁判（deepseek-r1、gpt-4、grok-4、mistral-large-3、llama-3.3-70b）、同样三位人类评分者之下，任务质量把大模型—人类一致性抬到 0.418，即人类间水平（0.474）的 88%，而两个主观维度上只有 58% 与 66%。在参考匹配的条件下，角度讲出同一个故事：裁判距两位评分者参考 60.7°，而被留出的人类距它 56.4°，相差 4.3°；主观维度上则相差 11.0° 与 9.3°。最好的单个裁判（55.3°）在任务质量上落在人类基线之内；在两个主观维度上，最好的裁判（67.3°、70.8°）仍远在基线之外。图 3 逐条展示这一点：主观维度的点云贴着恒等线保持平坦，任务质量则跟踪它。

**EN** cohortn σJ/σH θ◦θ◦

**ZH** 裁判群体 n σJ/σH θ° θ°

**EN** hhrrrefrhh∆

**ZH** hh r rref rhh Δ

**EN** (A) Rubric×dataset matched θ; pairwise r; rref: inter-LLMCH subj. mean 140.4484.4–0.093 0.180–+0.087DLQ LA50.73475.4 64.4 0.207 0.356 0.357 +0.149DLQ HAL50.78473.1 63.8 0.239 0.349 0.364 +0.110DLQ TQ (obj.) 50.68760.7 56.4 0.418 0.530 0.474 +0.112

**ZH** (A) 评分维度×数据集的匹配 θ；成对 r；rref：裁判间 CH 主观 均值 14 0.448 84.4 – 0.093 0.180 – +0.087；DLQ 语言可接受性 5 0.734 75.4 64.4 0.207 0.356 0.357 +0.149；DLQ 幻觉 5 0.784 73.1 63.8 0.239 0.349 0.364 +0.110；DLQ 任务质量（客观）5 0.687 60.7 56.4 0.418 0.530 0.474 +0.112

**EN** (B) Base-judge strata on CHstacked; rref: pool meanFE40.63587.5–0.131 0.093–+0.039OXL40.36888.5–0.070 0.093–−0.023OM40.22288.3–0.082 0.093–−0.011IF20.64189.6–0.083 0.093–−0.010

**ZH** (B) CH 上的基座裁判分层，堆叠；rref：池均值 FE 4 0.635 87.5 – 0.131 0.093 – +0.039；OXL 4 0.368 88.5 – 0.070 0.093 – −0.023；OM 4 0.222 88.3 – 0.082 0.093 – −0.011；IF 2 0.641 89.6 – 0.083 0.093 – −0.010

**EN** (C) Training stage on CHstacked; rref: BASEBASE30.31987.7–0.081 0.081–0.000FS30.62488.3–0.122 0.081–+0.041FT31.07487.1–0.129 0.081–+0.048FT+PO31.07887.1–0.132 0.081–+0.051AT410.64988.0–0.177 0.081–+0.096CAL410.63388.1–0.184 0.081–+0.103

**ZH** (C) CH 上的训练阶段，堆叠；rref：BASE BASE 3 0.319 87.7 – 0.081 0.081 – 0.000；FS 3 0.624 88.3 – 0.122 0.081 – +0.041；FT 3 1.074 87.1 – 0.129 0.081 – +0.048；FT+PO 3 1.078 87.1 – 0.132 0.081 – +0.051；AT 4 1 0.649 88.0 – 0.177 0.081 – +0.096；CAL 4 1 0.633 88.1 – 0.184 0.081 – +0.103

**EN** Table 1: Consolidated results grid. ∆= rref −r inpanel A (how far LLM–human sits below inter-LLM)and r−rref in B–C. Panel A: all three r legs pairwise;θ and θhh reference-matched, so the judge and the held-out human face the same two-rater target (DLQ only:CH merges its annotators into one reference, so no ﬂoorexists there and its θ is against that single reference).Panels B–C: per-judge stacked angles (C: bootstrap stagemeans), which run higher than panel A by construction(Table 4; App. N). 4: lifts all four CH rubrics over BASE(unmarked trained rows do not; base judges take nomarker). Shaded cells mark the decisive numbers: sand= the worst case in a panel, mist = the relief case. Key,codes, strata: App. H.1.

**ZH** 表 1：合并结果网格。Δ 在 A 栏为 rref − r（大模型—人类低于裁判间多少），在 B–C 栏为 r − rref。A 栏：三条 r 腿全部成对；θ 与 θhh 均已参考匹配，因此裁判与被留出的人类面对相同的两位评分者靶子（仅 DLQ：CH 把标注者合并为一个参考，故那里不存在基线，其 θ 是相对该单一参考而言）。B–C 栏：逐裁判的堆叠角度（C 栏为自助法阶段均值），按构造它们高于 A 栏（表 4；附录 N）。标记 4：表示该阶段把 CH 全部四个维度都抬到 BASE 之上（未标记的已训练行做不到；基座裁判不加标记）。阴影格标出决定性的数字：沙色 = 该栏中的最坏情形，雾色 = 缓解情形。键、代号与分层见附录 H.1。

**EN** 012

**ZH** 0 1 2

**EN** LLM-judge score

**ZH** 大模型裁判分数

**EN** 0

**ZH** 0

**EN** 1

**ZH** 1

**EN** 2

**ZH** 2

**EN** mean-human score

**ZH** 人类平均分

**EN** r̄=0.27ling. accept. [subj.]

**ZH** r̄ = 0.27 语言可接受性［主观］

**EN** 01

**ZH** 0 1

**EN** LLM-judge score

**ZH** 大模型裁判分数

**EN** 0

**ZH** 0

**EN** 1r̄=0.32halluc. [subj.]

**ZH** 1 r̄ = 0.32 幻觉［主观］

**EN** 012

**ZH** 0 1 2

**EN** LLM-judge score

**ZH** 大模型裁判分数

**EN** 0

**ZH** 0

**EN** 1

**ZH** 1

**EN** 2r̄=0.52task quality [obj.]

**ZH** 2 r̄ = 0.52 任务质量［客观］

**EN** Figure 3: Three-rater mean human score against LLM-judge score for the ﬁve DLQ base judges, one panel perrubric (hexbin density, dashed identity line, solid least-squares ﬁt). Axes follow each rubric’s own ordinal scale({0, 1, 2}; hallucinations is binary). ¯r is the judge-vs-mean-human Pearson, the quantity these panels plot; thepairwise leg comparable with inter-human agreement islower (0.418/0.207/0.239) and is what Table 1A reports.The two subjective rubrics stay ﬂat against the identityline; task quality tracks it.

**ZH** 图 3：五个 DLQ 基座裁判的三评分者人类平均分对大模型裁判分数，每个评分维度一栏（六边形分箱密度、虚线为恒等线、实线为最小二乘拟合）。坐标轴遵循各维度自身的序数尺度（{0, 1, 2}；幻觉为二值）。r̄ 是裁判对“人类均值”的 Pearson 相关，即这些子图所画的量；可与人类间一致性比较的那条成对腿更低（0.418／0.207／0.239），表 1A 报告的是后者。两个主观维度贴着恒等线保持平坦，任务质量则跟踪它。

**EN** The boundary is a large change of degree, nota crossing: judges close most but not all of thegap where the rubric is veriﬁable. Scoring judgesagainst the three-rater mean while scoring humansagainst each other puts task quality above the hu-man ﬂoor, but that ordering is an artefact of themismatched reference and does not survive match-ing.

**ZH** 边界是程度上的巨大变化，而非一次跨越：在评分维度可核验之处，裁判弥合了大部分而非全部差距。把裁判对着三评分者均值计分，同时让人类彼此互评，会使任务质量显得高于人类基线，但这一排序是参考不匹配的假象，在匹配之后并不成立。

**EN** We do not claim that LLM-as-judge failsin general:subjective rubrics with high rater-

**ZH** 我们并不主张以大模型为裁判普遍失败：评分者

**EN** [Page 6]

**ZH** 第 6 页

**EN** 0.00.20.40.60.81.01.21.4σ-ratio (judge spread / human spread)

**ZH** 0.0 0.2 0.4 0.6 0.8 1.0 1.2 1.4 σ 比值（裁判展布／人类展布）

**EN** 85

**ZH** 85

**EN** 86

**ZH** 86

**EN** 87

**ZH** 87

**EN** 88

**ZH** 88

**EN** 89

**ZH** 89

**EN** 90

**ZH** 90

**EN** angle to human ( ∘)

**ZH** 与人类的夹角（°）

**EN** σJ = σH

**ZH** σJ = σH

**EN** trained variantsfrontier (closed)

**ZH** 训练变体、前沿（闭源）

**EN** open xlopen large

**ZH** 开放超大、开放大型

**EN** open midIndic-focused

**ZH** 开放中型、面向印度语系

**EN** Figure 4: All 40 judges in (σ-ratio, angle) space; po-sition and spread, not a ranking. Extended caption inTable 6.

**ZH** 图 4：(σ 比值, 角度) 空间中的全部 40 个裁判；展示的是位置与展布，不是排名。扩展图注见表 6。

**EN** disagreement dimensionality expose a mismatch be-tween the judge and human subspaces, whereas ob-jective rubrics can be rank-matched. Items illustrat-ing both regimes (factual recall and shared culturalknowledge on one side; healthcare access, aﬀord-ability, overmedicalisation, and emotional framingon the other) are in Tables 26–27 (App. P).

**ZH** 分歧维度高的主观评分维度暴露出裁判与人类子空间之间的错配，而客观评分维度则可以做到秩匹配。展示两种机制各自的条目（一边是事实性回忆与共有文化知识；另一边是医疗可及性、可负担性、过度医疗化与情感框架）见表 26–27（附录 P）。

**EN** 5.3Geometric signature of the disagreement

**ZH** 5.3 分歧的几何特征

**EN** The failure is not only a correlation gap; it has a char-acteristic geometry (Table 1): compressed spread,low rank, high angle, large unrecoverable humanvariance (Sec. 5.4). On CH the median base judgeuses under half the human spread (σ-ratio 0.454)at a stacked angle of 89.3◦. On DLQ, with the ref-erence matched, base judges sit 84.3–88.9◦fromthe two-rater reference while a held-out human sits73.9–78.1◦from it: a gap of roughly 10◦that Pear-son alone does not expose. Rank conﬁrms P2: hu-man references use the full basis (r95 = 4 CH, 3DLQ); 11 of 14 CH base judges sit at r95 ≤3. An-gles are comparable only within one construction(Table 4; App. N).

**ZH** 这种失效不只是一段相关性的差距，它有特征性的几何形态（表 1）：展布被压缩、秩很低、角度很大、大量人类方差无法复原（第 5.4 节）。在 CH 上，中位数意义上的基座裁判只用到人类展布的一半不到（σ 比值 0.454），堆叠角为 89.3°。在 DLQ 上，经参考匹配后，基座裁判距两位评分者参考 84.3–88.9°，而被留出的人类距它 73.9–78.1°：约 10° 的差距是单用 Pearson 看不出来的。秩印证了 P2：人类参考用满整组基（r95 = 4，CH；3，DLQ）；CH 的 14 个基座裁判中有 11 个处在 r95 ≤ 3。角度只有在同一构造内部才可比较（表 4；附录 N）。

**EN** Trainingreliablymovesjudgesrightward(spread) but not downward (angle); Fig. 4 plotsevery judge in that space.

**ZH** 训练可靠地把裁判往右推（展布），而不是往下推（角度）；图 4 把每个裁判画在这个空间里。

**EN** Task quality does not merely raise Pearson, itrotates the judge vectors: 4.3◦from the ﬂoor against9.3–11.0◦on the subjective rubrics, even thoughspread stays compressed (σ-ratio 0.687; σH is themean single-rater SD throughout, matching CH’ssingle merged reference). Alignment and spreadcalibration are separable: on the objective rubricjudges point close to the right way but under-usethe range (Fig. 5).

**ZH** 任务质量不只是抬高了 Pearson，它转动了裁判向量：距基线 4.3°，而主观维度上是 9.3–11.0°，尽管展布仍然被压缩（σ 比值 0.687；σH 全程为单评分者的平均标准差，与 CH 的单一合并参考一致）。对齐与展布校准是可分离的：在客观维度上裁判指向的方向大致正确，却没有用满量程（图 5）。

**EN** 0.51.0

**ZH** 0.5 1.0

**EN** σ-ratio

**ZH** σ 比值

**EN** 50

**ZH** 50

**EN** 60

**ZH** 60

**EN** 70

**ZH** 70

**EN** 80

**ZH** 80

**EN** angle to mean-human (°

**ZH** 与人类均值的夹角（°）

**EN** ling. accept. [subj.]

**ZH** 语言可接受性［主观］

**EN** 0.51.0

**ZH** 0.5 1.0

**EN** σ-ratio

**ZH** σ 比值

**EN** halluc. [subj.]

**ZH** 幻觉［主观］

**EN** 0.51.0

**ZH** 0.5 1.0

**EN** σ-ratio

**ZH** σ 比值

**EN** task quality [obj.]

**ZH** 任务质量［客观］

**EN** Figure 5: One panel per rubric, judges and held-outhumans on the matched two-rater reference. Extendedcaption in Table 6.

**ZH** 图 5：每个评分维度一栏，裁判与被留出的人类都对着匹配的两位评分者参考。扩展图注见表 6。

**EN** ControlOutcome

**ZH** 控制项　结果

**EN** Permutation nullDLQ per-rubric null 88.6–88.7◦; every judge×rubric anglebelow all 500 shuﬄes (p < 0.002 each)CH judge-level + FDRCH stacked null 88.8◦; 11/40 judges below at p < .05 and 6survive Benjamini–Hochberg at q < .05 (20,000 shuﬄes)Ordinal / scaleSpearman = Pearson within 0.02; remap onto human marginalmoves θ by ≤0.13◦(DLQ) / ≤0.31◦(CH)Self-preferencejudges from a generator’s own family rate it no diﬀerently than therest of the cohort does (|∆| ≤0.035 SD, all p ≥0.58)Split-halfitem-half angles agree to ≤2.5◦; DLQ judge ordering acrosshalves r = 0.74–0.97; CH judge ordering does not replicateUnrecoverable var.ridge CV: 55% (TQ), ≈80% (DLQ subj.), ≈100% (CH) ofhuman variance unrecoverable from the judge cohortdR separator (P5)human-only dimensionality splits objective (≈2.1) from subjec-tive (≈2.4) cells before any LLM runs; no graded trend withineither group

**ZH** 置换零假设：DLQ 逐维度零假设 88.6–88.7°；每个裁判×维度角度都低于全部 500 次置换（每个 p < 0.002）。CH 裁判级 + FDR：CH 堆叠零假设 88.8°；40 个裁判中 11 个在 p < .05 下低于零假设，6 个在 Benjamini–Hochberg 校正下存活于 q < .05（20,000 次置换）。序数／尺度：Spearman 与 Pearson 相差在 0.02 之内；重映射到人类边际分布使 θ 变化 ≤0.13°（DLQ）／≤0.31°（CH）。自我偏好：来自某生成模型自身系列的裁判给它的打分与群体其余成员没有差别（|Δ| ≤0.035 SD，所有 p ≥0.58）。分半：条目半区之间的角度一致到 ≤2.5°；DLQ 裁判在两半间的排序 r = 0.74–0.97；CH 裁判排序不具可复现性。不可复原方差：岭回归交叉验证显示，人类方差中 55%（任务质量）、约 80%（DLQ 主观）、约 100%（CH）无法从裁判群体复原。dR 分离器（P5）：仅由人类算出的维度数，在任何大模型运行之前就把客观单元（约 2.1）与主观单元（约 2.4）分开；两组内部都没有分级趋势。

**EN** Table 2: Controls summary. Procedures, per-rubricvalues, judge-level permutation results with q values,and caveats in App. L, M.

**ZH** 表 2：控制检验摘要。流程、逐维度数值、带 q 值的裁判级置换结果以及注意事项见附录 L、M。

**EN** 5.4Controls: is the geometry real?

**ZH** 5.4 控制检验：几何是真实的吗？

**EN** Control families, all on released scores with no newinference, test whether the geometry is an artefactand test P1–P6 (Table 2; procedures in App. L–M).

**ZH** 各类控制检验全部在已发布的分数上进行，不引入新的推断，目的是检验几何是否为假象，并检验 P1–P6（表 2；流程见附录 L–M）。

**EN** Against a permutation null (500 shuﬄes/judge;nulls 88.6–88.7◦), every DLQ judge×rubric anglebeats all shuﬄes (p < 0.002, all 15 tests), andthe weakest survives Bonferroni across all 15: taskquality at 60.7◦sits signiﬁcantly below the permu-tation null, and the subjective elevations above theﬂoor are consistent oﬀsets (P3). On CH the cohortsits nearest the null (88.1◦vs. 88.8◦), the strongestcollapse we report, yet individual judges still de-part from it: at 20,000 shuﬄes, 11 of 40 judges arebelow the null at p < .05 (2 expected by chance)and 6 survive Benjamini–Hochberg (Benjamini andHochberg, 1995) at q < .05, including two of thefour frontier closed judges (gpt-5.5, gpt-4o), llama-3.3-70b, and three ﬁne-tuned variants of the Indic-capable open families (Table 19).

**ZH** 相对置换零假设（每裁判 500 次置换；零假设 88.6–88.7°），DLQ 每个裁判×维度的角度都胜过全部置换（p < 0.002，共 15 项检验），其中最弱的一项也已通过全部 15 项的 Bonferroni 校正：任务质量在 60.7° 上显著低于置换零假设，而主观维度上高于基线的抬升是一致性的偏移（P3）。在 CH 上，裁判群体离零假设最近（88.1° 对 88.8°），这是我们报告的最强坍缩，但个体裁判仍然偏离它：在 20,000 次置换下，40 个裁判中有 11 个在 p < .05 下低于零假设（机遇下期望为 2 个），6 个在 Benjamini–Hochberg 校正下存活于 q < .05（Benjamini 与 Hochberg，1995），其中包括四个闭源前沿裁判中的两个（gpt-5.5、gpt-4o）、llama-3.3-70b，以及具备印度语能力的开放系列的三个微调变体（表 19）。

**EN** That is each judge against chance, not againsteach other. The permutation is paired, holding ajudge’s matrix ﬁxed while shuﬄing the human rows,so it removes item-sampling variance; an item boot-strap does not, and gives each CH angle a 95%interval 6.3◦wide against a between-judge SD ofonly 1.6◦. We therefore rank no CH judges by an-gle anywhere, and CH comparisons use stacked

**ZH** 那是每个裁判各自对机遇，而不是彼此互比。置换是配对的：固定裁判的矩阵，只置换人类的行，因此它消去了条目抽样方差；条目自助法做不到这一点，它给出的每个 CH 角度的 95% 区间宽 6.3°，而裁判之间的标准差只有 1.6°。因此我们不在任何地方按角度给 CH 裁判排名，CH 的比较改用堆叠

**EN** [Page 7]

**ZH** 第 7 页

**EN** Pearson (Sec. 5.7).

**ZH** Pearson（第 5.7 节）。

**EN** Nor is compression merely cautious scale use:Spearman tracks Pearson to within 0.02 per rubric,and monotone remapping onto the human marginalmoves angles by ≤0.13◦(DLQ) / ≤0.31◦(CH), sojudges occupy a different direction, not a narrowerstretch. We also report a magnitude rather than anall-or-nothing “null-space” claim: cross-validatedridge reconstruction from the entire cohort leaves55% of human variance unrecoverable on task qual-ity, ≈80% on subjective DLQ, essentially 100%on CH (CV R2 ≤0).

**ZH** 压缩也不只是保守地使用量表：各维度上 Spearman 与 Pearson 相差在 0.02 之内，而单调重映射到人类边际分布只让角度变化 ≤0.13°（DLQ）／≤0.31°（CH），所以裁判占据的是不同的方向，而不是更窄的一段。我们也报告一个量级，而不是一个非此即彼的“零空间”论断：用整个裁判群体做交叉验证的岭回归重建，在任务质量上留下 55% 的人类方差无法复原，DLQ 主观维度上约 80%，CH 上几乎 100%（CV R² ≤ 0）。

**EN** The regimes also separate before any LLM is run(P5). The participation ratio dR (Eq. 1), computedfrom the three human raters alone, tracks the LLM–human angle across the nine DLQ rubric×domaincells (ρ = 0.68, p = 0.042, R2 = 0.83, leave-one-cell-out stable). The relation is between regimes,not graded within them: objective cells cluster atdR ≈2.1 and ≈60◦, subjective at ≈2.4 and ≈74◦,while inside the six subjective cells the correlationvanishes (ρ = −0.03). We read dR as a two-regimeseparator, not a dose–response curve, and quote noslope; with three raters it is capped at 3, measuringrater disagreement at this panel size (see Limita-tions). The supported claim is the useful one: aquantity computable from humans alone tells youwhich regime a rubric is in.

**ZH** 两种机制在任何大模型运行之前就已分离（P5）。参与率 dR（式 1）仅由三位人类评分者算出，它在 DLQ 的九个“评分维度×领域”单元上跟踪大模型—人类夹角（ρ = 0.68，p = 0.042，R² = 0.83，留一单元稳定）。这一关系是机制之间的，而非机制内部的分级：客观单元聚集在 dR ≈ 2.1、约 60° 处，主观单元在约 2.4、约 74° 处，而在六个主观单元内部相关性消失（ρ = −0.03）。我们把 dR 读作两机制的分离器，而不是剂量—反应曲线，因此不给出斜率；在三位评分者下它上限为 3，度量的是该评分小组规模上的评分者分歧（见“局限性”）。被支持的断言恰恰是有用的那一个：一个仅由人类就能算出的量，可以告诉你某个评分维度处在哪种机制。

**EN** Self-preference is not the driver either. Two ofCH’s three answer generators (sarvam-m, qwen3)also serve as judges, and sarvam-m supplies theheadline calibrated judge, so family favouritismcould manufacture the training result. Within a(language, question) triple, a judge’s standardiseddeviation from its triple mean, minus the human’sand then the rest of the cohort’s, isolates familypreference from item diﬃculty and real quality dif-ferences. No family shows an eﬀect (|∆| ≤0.035SD; permutation p ≥0.58; App. M.8).

**ZH** 自我偏好也不是驱动因素。CH 的三个答案生成器中有两个（sarvam-m、qwen3）同时也担任裁判，而 sarvam-m 提供了头条数字背后的那个校准裁判，因此系列偏袒有可能制造出训练结果。在一个（语言、问题）三元组内部，取某裁判相对其自身三元组均值的标准化偏差，减去人类的偏差，再减去群体其余裁判的平均效应，就把系列偏好与条目难度和真实质量差异分离开来。没有任何一个系列表现出效应（|Δ| ≤0.035 SD；置换 p ≥0.58；附录 M.8）。

**EN** Finally, rank is necessary but orientation is deci-sive (P6): across the 40 CH judges eﬀective rankdoes not predict alignment (r = 0.12; r95 spans1–4, angles 85.0–89.9◦). With task quality stillcompressed (σ-ratio 0.69) yet rotated to within 4.3◦

**ZH** 最后，秩是必要而方向是决定性的（P6）：在 40 个 CH 裁判中，有效秩不能预测对齐（r = 0.12；r95 跨越 1–4，角度 85.0–89.9°）。在任务质量仍然被压缩（σ 比值 0.69）却旋转到距基线

**EN** of the ﬂoor, orientation, not rank or spread, carriesalignment (Eq. 2).

**ZH** 4.3° 之内的情况下，承载对齐的是方向，而不是秩或展布（式 2）。

**EN** 5.5Breadth: domains and languages

**ZH** 5.5 广度：领域与语言

**EN** The remaining diagnostics use DLQ, the only setupwith per-cell human ﬂoors. Across domains theboundary reproduces in all three (Fig. 6): on taskquality the LLM mean sits 60.6–63.3◦against a

**ZH** 其余诊断使用 DLQ，它是唯一具备逐单元人类基线的设置。跨领域看，边界在三个领域中都复现（图 6）：在任务质量上，大模型均值处在 60.6–63.3°，而匹配的基线为 57.7–58.2°，LH 的 Pearson 达到 H–H 的 85–92%；在主观维度上，差距扩大到 8.3–14.3°，LH 降到 49–66%。σ 压缩（0.67–0.82）不随领域变化；图 14（附录 H）按语言、领域与评分维度类型拆解全部四个领域数据集的一致性。

**EN** matched ﬂoor of 57.7–58.2◦, with LH Pearsonat 85–92% of H–H; on the subjective rubrics thegap widens to 8.3–14.3◦and LH falls to 49–66%.σ-compression (0.67–0.82) is domain-invariant;Fig. 14 (App. H) breaks agreement out by language,domain, and rubric kind across all four domaindatasets.

**ZH** 匹配的基线 57.7–58.2°，LH 的 Pearson 达到 H–H 的 85–92%；在主观维度上差距扩大到 8.3–14.3°，LH 降到 49–66%。σ 压缩（0.67–0.82）不随领域变化；图 14（附录 H）按语言、领域与评分维度类型拆解全部四个领域数据集的一致性。

**EN** Across the eight languages the robust ﬁndingsare compression and the agreement gap, not theangle. σ-compression is universal (0.43–0.76) andthe LL−LH gap is positive in all eight, but its sizeranges over two orders of magnitude, from +0.227(Bengali) to +0.005 (Telugu, eﬀectively closed).Per-language angles we do not read: at n=60–300per language the stacked angle saturates near 90◦

**ZH** 跨八种语言看，稳健的发现是压缩与一致性差距，而不是角度。σ 压缩是普遍的（0.43–0.76），LL−LH 差距在八种语言中全为正，但其大小跨越两个数量级，从 +0.227（孟加拉语）到 +0.005（泰卢固语，实际上已经闭合）。逐语言的角度我们不读：在每语言 n = 60–300 时，堆叠角饱和在接近 90°，

**EN** for judges and humans alike, and only 26 of 40judge×language cells sit above their own matchedﬂoor (Fig. 12).

**ZH** 裁判与人类皆然，且 40 个裁判×语言单元中只有 26 个处在各自匹配的基线之上（图 12）。

**EN** 0.51.0

**ZH** 0.5 1.0

**EN** 60

**ZH** 60

**EN** 80

**ZH** 80

**EN** health & wellness

**ZH** 健康养生

**EN** angle to H (°)

**ZH** 与人类的夹角（°）

**EN** ling. accept. [subj.]

**ZH** 语言可接受性［主观］

**EN** n=284

**ZH** n=284

**EN** 0.51.0

**ZH** 0.5 1.0

**EN** 60

**ZH** 60

**EN** 80

**ZH** 80

**EN** halluc. [subj.]

**ZH** 幻觉［主观］

**EN** n=284

**ZH** n=284

**EN** 0.51.0

**ZH** 0.5 1.0

**EN** 60

**ZH** 60

**EN** 80

**ZH** 80

**EN** task quality [obj.]

**ZH** 任务质量［客观］

**EN** n=284

**ZH** n=284

**EN** 0.51.0

**ZH** 0.5 1.0

**EN** 60

**ZH** 60

**EN** 80

**ZH** 80

**EN** finance

**ZH** 金融

**EN** angle to H (°)

**ZH** 与人类的夹角（°）

**EN** n=323

**ZH** n=323

**EN** 0.51.0

**ZH** 0.5 1.0

**EN** 60

**ZH** 60

**EN** 80n=323

**ZH** 80 n=323

**EN** 0.51.0

**ZH** 0.5 1.0

**EN** 60

**ZH** 60

**EN** 80n=323

**ZH** 80 n=323

**EN** 0.51.0

**ZH** 0.5 1.0

**EN** 60

**ZH** 60

**EN** 80

**ZH** 80

**EN** everyday life

**ZH** 日常生活

**EN** angle to H (°)

**ZH** 与人类的夹角（°）

**EN** n=575

**ZH** n=575

**EN** 0.51.0

**ZH** 0.5 1.0

**EN** 60

**ZH** 60

**EN** 80n=575

**ZH** 80 n=575

**EN** 0.51.0

**ZH** 0.5 1.0

**EN** 60

**ZH** 60

**EN** 80n=575

**ZH** 80 n=575

**EN** frontier (closed)open xl

**ZH** 前沿（闭源）、开放超大

**EN** open largeopen mid

**ZH** 开放大型、开放中型

**EN** Indic-focusedLLM mean

**ZH** 面向印度语系、大模型均值

**EN** human floor, held-out rater (DLQ)

**ZH** 人类基线，留出的评分者（DLQ）

**EN** Figure 6: Rows = domains, columns = rubrics; eachpanel plots base judges in (σJ /σH horizontally, anglevertically), both against the matched two-rater reference,with the dashed green line the held-out-rater ﬂoor andpale green marking the objective rubric. The objectivecolumn drops toward the ﬂoor in every domain; the twosubjective columns sit clearly above it. CH geometry isin Table 1A and Fig. 2.

**ZH** 图 6：行 = 领域，列 = 评分维度；每栏把基座裁判画在（横轴 σJ/σH、纵轴角度）空间中，两者都对着匹配的两位评分者参考，绿色虚线为留出评分者的基线，淡绿色标出客观维度。客观那一列在每个领域都向基线靠拢，两个主观列则明显位于其上方。CH 的几何见表 1A 与图 2。

**EN** 5.6Subspace topology of the judge cohort

**ZH** 5.6 裁判群体的子空间拓扑

**EN** Do judges sit in the same direction, or split intosub-clusters equally far from humans? Z-scoringeach judge’s per-rubric scores over the 405 CHcore items and taking cosines between the 1620-d item×rubric vectors measures pure orientation(cosll =0.16 vs. coslh =0.08; Fig. 7).

**ZH** 裁判是处在同一个方向上，还是分裂成若干同样远离人类的子簇？把每个裁判在 405 条 CH 核心条目上的逐维度分数做 Z 分数标准化，再取 1620 维“条目×维度”向量之间的余弦，就度量了纯粹的方向（cosll = 0.16 对 coslh = 0.08；图 7）。

**EN** Three features are invisible to per-judge angleplots. (i) The tightest pairs do not follow modelfamily: the three deepest cells are all cross-vendor,and the only same-family pair (qwen3, 0.50) ranksfourth against a 0.16 cohort mean (values in Ta-ble 6); scale and openness do not organise the map

**ZH** 有三个特征是逐裁判角度图看不见的。(i) 最紧密的配对并不遵循模型系列：最深的三个单元全是跨厂商的，而唯一同系列的配对（qwen3，0.50）在 0.16 的群体均值面前只能排第四（数值见表 6）；规模与开放性也组织不起这张图，

**EN** [Page 8]

**ZH** 第 8 页

<!-- [原子块 · img]  -->

**EN** Figure on page 8

**ZH** 第 8 页的图

<!-- [原子块 · img]  -->

**EN** Figure on page 8

**ZH** 第 8 页的图

**EN** aya

**ZH** aya

**EN** krutrim-2

**ZH** krutrim-2

**EN** llama-3.3-70b

**ZH** llama-3.3-70b

**EN** mistral-L2

**ZH** mistral-L2

**EN** human

**ZH** 人类

**EN** sarvam-m

**ZH** sarvam-m

**EN** deepseek-r1

**ZH** deepseek-r1

**EN** gpt-5.5

**ZH** gpt-5.5

**EN** grok-4

**ZH** grok-4

**EN** qwen3-235b

**ZH** qwen3-235b

**EN** qwen3-next-80b

**ZH** qwen3-next-80b

**EN** gpt-4o

**ZH** gpt-4o

**EN** gemma

**ZH** gemma

**EN** llama-4-scout

**ZH** llama-4-scout

**EN** mistral-L3

**ZH** mistral-L3

**EN** ayakrutrim-2llama-3.3-70b

**ZH** aya、krutrim-2、llama-3.3-70b

**EN** mistral-L2

**ZH** mistral-L2

**EN** humansarvam-mdeepseek-r1

**ZH** 人类、sarvam-m、deepseek-r1

**EN** gpt-5.5

**ZH** gpt-5.5

**EN** grok-4qwen3-235bqwen3-next-80b

**ZH** grok-4、qwen3-235b、qwen3-next-80b

**EN** gpt-4ogemmallama-4-scout

**ZH** gpt-4o、gemma、llama-4-scout

**EN** mistral-L3

**ZH** mistral-L3

**EN** cos LL = 0.16 cos LH = 0.08

**ZH** cos LL = 0.16，cos LH = 0.08

**EN** −0.6

**ZH** −0.6

**EN** −0.4

**ZH** −0.4

**EN** −0.2

**ZH** −0.2

**EN** 0.0

**ZH** 0.0

**EN** 0.2

**ZH** 0.2

**EN** 0.4

**ZH** 0.4

**EN** 0.6

**ZH** 0.6

**EN** cosine sim. (Z-scored)

**ZH** 余弦相似度（Z 分数标准化后）

**EN** Figure 7: Ward-reordered cosines; the human row staysuniformly pale. Extended caption in Table 6.

**ZH** 图 7：Ward 重排后的余弦；人类那一行始终均匀偏淡。扩展图注见表 6。

**EN** Rubrick=12345k→∞floor

**ZH** 评分维度 k=1 2 3 4 5 k→∞ 基线

**EN** task quality60.755.5 53.3 52.0 51.250.056.4ling. accept.75.471.2 69.4 68.3 67.666.564.4hallucinations73.169.1 67.2 66.2 65.564.663.8

**ZH** 任务质量 60.7 55.5 53.3 52.0 51.2 50.0 56.4；语言可接受性 75.4 71.2 69.4 68.3 67.6 66.5 64.4；幻觉 73.1 69.1 67.2 66.2 65.5 64.6 63.8

**EN** Table 3: Ensemble-size curve (DLQ, matched refer-ence). Mean angle◦over all

**ZH** 表 3：集成规模曲线（DLQ，匹配参考）。平均角度°，取遍

**EN** 5

**ZH** C(5,

**EN** k

**ZH** k

**EN** subsets of the ﬁve basejudges, each scored against the same held-out two-ratermean that deﬁnes the ﬂoor. k→∞sums the geometrictail of the decrements. Mist marks ensembles alreadyinside their ﬂoor, sand a limit that stays outside it: ontask quality two judges suﬃce, on both subjective rubricsno ensemble of any size reaches the ﬂoor. Caveats inApp. M.10.

**ZH** 基座裁判子集，每个子集都对着定义基线的同一留出两位评分者均值计分。k→∞ 对递减量的几何尾部求和，递减量按近乎恒定的因子（0.59–0.62）收缩。在任务质量上两个裁判就已越过基线，极限落在基线内 6°；而在两个主观维度上，任何可达规模的集成都够不到基线，外推的极限也留在基线之外。注意这个对我们不利的不对称：集成平均了五个裁判，而人类一侧只有一位评分者。

**EN** either, so the shared orientation is a cohort-wideproperty rather than siblings agreeing. (ii) The co-hort splits into a tight frontier+open block (intra0.27) and a looser mid-tier block (intra 0.11; across0.08): a single LL aggregate averages these intoa consensus no judge holds. (iii) The human rowstays uniformly pale after Z-scoring, so the collapsebelongs to the LLM-shared subspace, not to a scaleor single-judge artefact.

**ZH** 因此共享的方向是群体层面的属性，而不是同源模型之间的相互认同。(ii) 群体分裂成一个紧密的前沿+开放块（内部 0.27）与一个较松散的中层块（内部 0.11；跨块 0.08）：单一的 LL 聚合值把这些平均成一个没有任何单个裁判持有的“共识”。(iii) 人类那一行在 Z 分数标准化之后始终均匀偏淡，因此坍缩属于大模型共享的子空间，而不是尺度假象或单个裁判的假象。

**EN** The shared axis is directly measurable (P4): thecohort’s top three PCs explain 86.6–89.0% of judgevariance on DLQ (66–82% CH), and the dominantaxis sits 47.7◦from humans on task quality but64–66◦on the DLQ subjective rubrics (79–86◦onCH). Averaging moves toward that axis and stopsthere (Table 3): ensembling k judges lowers thematched angle monotonically, but the decrementsshrink by a near-constant factor (≈0.6), so the geo-metric tail bounds an unlimited ensemble of thesejudges outside the subjective ﬂoors. Ensemblingbuys variance reduction toward the shared axis, nota new direction (App. M.10).

**ZH** 共享轴是可以直接测量的（P4）：裁判群体的前三个主成分解释了 DLQ 上 86.6–89.0% 的裁判方差（CH 上 66–82%），而这条主导轴在任务质量上距人类 47.7°，在 DLQ 主观维度上为 64–66°（CH 上 79–86°）。平均只会朝这条轴移动，然后停在那里（表 3）：集成 k 个裁判会让匹配角单调下降，但递减量按近似恒定的因子（约 0.6）收缩，因此几何尾部把由这些裁判组成的无限集成界定在主观基线之外。集成买到的是朝共享轴的方差缩减，而不是一个新的方向（附录 M.10）。

**EN** 0

**ZH** 0

**EN** 1

**ZH** 1

**EN** σ-ratio

**ZH** σ 比值

**EN** sarvam-mgemma-3aya-expanse

**ZH** sarvam-m、gemma-3、aya-expanse

**EN** 80

**ZH** 80

**EN** 85

**ZH** 85

**EN** 90

**ZH** 90

**EN** angle (°)

**ZH** 角度（°）

**EN** base

**ZH** 基座

**EN** FS

**ZH** FS

**EN** AT

**ZH** AT

**EN** CAL

**ZH** CAL

**EN** FTFT+PO

**ZH** FT、FT+PO

**EN** 0.0

**ZH** 0.0

**EN** 0.2

**ZH** 0.2

**EN** Pearson r

**ZH** Pearson r

**EN** base

**ZH** 基座

**EN** FS

**ZH** FS

**EN** AT

**ZH** AT

**EN** CAL

**ZH** CAL

**EN** FTFT+PO

**ZH** FT、FT+PO

**EN** base

**ZH** 基座

**EN** FS

**ZH** FS

**EN** AT

**ZH** AT

**EN** CAL

**ZH** CAL

**EN** FTFT+PO

**ZH** FT、FT+PO

**EN** Figure 8: Bootstrap over B =1000 resamples. Spreadrises reliably; angle distributions overlap throughout.Extended caption in Table 6.

**ZH** 图 8：B = 1000 次重抽样的自助法。展布稳定上升；角度分布全程重叠。扩展图注见表 6。

**EN** baseFSATCALFTFT+PO

**ZH** 基座、FS、AT、CAL、FT、FT+PO

**EN** 0.0

**ZH** 0.0

**EN** 0.2

**ZH** 0.2

**EN** Pearson r

**ZH** Pearson r

**EN** gpt-5.5

**ZH** gpt-5.5

**EN** clarityhelpfulaccuracycomplete

**ZH** 清晰性、有用性、准确性、完整性

**EN** baseFSATCALFTFT+PO

**ZH** 基座、FS、AT、CAL、FT、FT+PO

**EN** 1

**ZH** 1

**EN** 2

**ZH** 2

**EN** σ-ratio

**ZH** σ 比值

**EN** σ_judge = σ_human

**ZH** σ裁判 = σ人类

**EN** Figure 9: Only the demonstration-anchored stages raiseevery rubric. Extended caption in Table 6.

**ZH** 图 9：只有演示锚定的两个阶段抬高了每一个评分维度。扩展图注见表 6。

**EN** 5.7Training restores spread beforeorientation

**ZH** 5.7 训练先恢复展布，再谈方向

**EN** Which part of the geometry can training change?

**ZH** 训练能改变几何的哪一部分？

**EN** On community-health we follow sarvam-m 24B,gemma-3 27B, and aya-expanse 32B throughbase, few-shot, ﬁne-tune, ﬁne-tune+pref-optim,and (sarvam-m only) demonstration-augmentedSFT (AT) and demonstration-anchored calibration(CAL), picking the best in-stage judge per fam-ily by stacked Pearson with paired item-bootstrapCIs. σ-ratio rises strongly under FT and FT+PO(0.32 →1.08) but the angle barely moves: stagemeans stay at 87–88◦with overlapping CIs (Ta-ble 1C; Fig. 8).

**ZH** 在社区健康上，我们跟踪 sarvam-m 24B、gemma-3 27B 与 aya-expanse 32B 经过基座、少样本、微调、微调+偏好优化，以及（仅 sarvam-m）演示增强 SFT（AT）与演示锚定校准（CAL），并按堆叠 Pearson 及配对条目自助置信区间为每个系列挑出阶段内最佳裁判。σ 比值在 FT 与 FT+PO 下大幅上升（0.32 → 1.08），角度却几乎不动：阶段均值停在 87–88°，置信区间互相重叠（表 1C；图 8）。

**EN** The aggregate masks per-rubric reversals (Fig. 9):FT/PO over-spreads accuracy (σ ≈2.2) and de-grades completeness (0.134 →0.079), and few-shot leaves completeness ﬂat, so only the twodemonstration-anchored stages lift all four rubrics.Both were run on sarvam-m alone, so this is awithin-family ordering, not a cross-family compar-ison. Calibration puts the best 24B Indic judge atr = 0.184, above gpt-5.5 (0.123; Fig. 13) yet far

**ZH** 聚合值掩盖了逐维度的反转（图 9）：FT／PO 让准确性过度展布（σ ≈ 2.2）并使完整性退化（0.134 → 0.079），而少样本让完整性原地不动，因此只有两个演示锚定阶段抬高了全部四个维度。两者都只在 sarvam-m 上运行，所以这是系列内部的排序，而非跨系列比较。校准把最好的 24B 印度语系裁判推到 r = 0.184，高于 gpt-5.5（0.123；图 13），却仍

**EN** [Page 9]

**ZH** 第 9 页

**EN** 0255075100

**ZH** 0 25 50 75 100

**EN** share of ‖Δs‖2 (%)

**ZH** ‖Δs‖² 的占比（%）

**EN** sarvam-m FS

**ZH** sarvam-m FS

**EN** sarvam-m FT

**ZH** sarvam-m FT

**EN** sarvam-m FT+PO

**ZH** sarvam-m FT+PO

**EN** sarvam-m AT

**ZH** sarvam-m AT

**EN** sarvam-m CAL

**ZH** sarvam-m CAL

**EN** gemma FS

**ZH** gemma FS

**EN** gemma FT

**ZH** gemma FT

**EN** gemma FT+PO

**ZH** gemma FT+PO

**EN** aya FS

**ZH** aya FS

**EN** aya FT

**ZH** aya FT

**EN** aya FT+PO

**ZH** aya FT+PO

**EN** 23

**ZH** 23

**EN** 20

**ZH** 20

**EN** 25

**ZH** 25

**EN** 21

**ZH** 21

**EN** 22

**ZH** 22

**EN** 17

**ZH** 17

**EN** 29

**ZH** 29

**EN** 30

**ZH** 30

**EN** Figure 10: Each bar splits ∥∆s∥2 into stretch along thebase axis (blue, labelled), rotation toward the human axis(green, labelled), and oﬀ-axis residual (grey). Rotationtoward the human axis is ≤3.5% in every stage cell.Extended caption in Table 6.

**ZH** 图 10：每根柱子把 ‖∆s‖² 拆成沿基座轴的拉伸（蓝色，已标注）、朝人类轴的旋转（绿色，已标注）与离轴残差（灰色）。朝人类轴的旋转在每个阶段单元中都 ≤3.5%。扩展图注见表 6。

**EN** below DLQ inter-human agreement (0.474).

**ZH** 远低于 DLQ 的人类间一致性（0.474）。

**EN** 5.8Decomposing the training delta: stretch,rotate, residual

**ZH** 5.8 训练增量的分解：拉伸、旋转、残差

**EN** The bootstrap says what training outputs, not whereeach unit of delta goes. Per (family, stage) we de-compose ∆s=sstage−sbase over the 405 core itemsinto orthogonal energies: stretch along the baseaxis, rotate→human (the only direction that canshrink the angle), and off-axis residual (Fig. 10).

**ZH** 自助法说的是训练产出了什么，而不是每一份增量去了哪里。对每个（系列、阶段），我们在 405 条核心条目上把 ∆s = s阶段 − s基座 分解成正交的能量成分：沿基座轴的拉伸、朝人类的旋转（唯一能缩小夹角的方向），以及离轴残差（图 10）。

**EN** Two ﬁndings give the orientation result ananatomy.First, rotation toward the humanaxis is uniformly tiny: ≤3.5% of ∥∆s∥2 inevery cell (stage means 1.1/2.3/2.8/1.8/1.9%for FS/FT/FT+PO/AT/CAL). The demonstration-anchored stages carrying the headline gain rotate nomore than the weight-updating ones, so their advan-tage is not a subspace correction. Second, the struc-tured part is stretch (17–30% on sarvam-m andgemma, tracking each stage’s σ-ratio gain: addedvariance is mostly a louder base ranking). Aya iso-lates the mechanism by exception: its stretch is≤0.1% and ∼97% of its update is oﬀ-axis reshuf-ﬂing, which is why it moves σ without converting itinto Pearson. Across cells the residual is 67–99%:training ampliﬁes then reshuffles, and the orienta-tion axis is essentially never moved.

**ZH** 两项发现给了方向性结果一副解剖图。第一，朝人类轴的旋转一律极小：在每个单元中都只占 ‖∆s‖² 的 ≤3.5%（FS／FT／FT+PO／AT／CAL 的阶段均值为 1.1／2.3／2.8／1.8／1.9%）。承载头条增益的两个演示锚定阶段，旋转量并不比更新权重的阶段更多，因此它们的优势并非来自子空间校正。第二，有结构的那部分是拉伸（sarvam-m 与 gemma 上为 17–30%，与各自阶段的 σ 比值增益同步：新增的方差多半只是把基座排序说得更响）。Aya 以例外的方式把机制孤立出来：它的拉伸 ≤0.1%，约 97% 的更新是离轴重排，这正是它抬高了 σ 却没能转化为 Pearson 的原因。各单元的残差为 67–99%：训练先放大，再重排，而方向轴几乎从未被推动。

**EN** A complementary check isolates what the demon-strations contribute: post-hoc aﬃne rescaling ofthe FT+PO judge onto human anchors never repro-duces the gains (Fig. 11, Table 23), so the lift needsthe demonstrations at inference, not a scale ﬁx.

**ZH** 一项互补的检验孤立出演示样例的贡献：把 FT+PO 裁判事后仿射重标到人类锚点上，永远无法复现那些增益（图 11，表 23），因此这一提升需要在推断时使用演示样例，而不是靠一次尺度修正。

**EN** 510204080160human-anchored items used

**ZH** 5 10 20 40 80 160 所用的人类锚定条目数

**EN** −0.10

**ZH** −0.10

**EN** −0.05

**ZH** −0.05

**EN** 0.00

**ZH** 0.00

**EN** 0.05

**ZH** 0.05

**EN** 0.10

**ZH** 0.10

**EN** 0.15

**ZH** 0.15

**EN** 0.20

**ZH** 0.20

**EN** held-out stacked Pearson r

**ZH** 留出集上的堆叠 Pearson r

**EN** demonstration-anchored CAL 0.184

**ZH** 演示锚定 CAL 0.184

**EN** dotted: same judge, uncalibrated

**ZH** 点线：同一裁判，未校准

**EN** sarvam-m FT+POgemma-3 FT+PO

**ZH** sarvam-m FT+PO、gemma-3 FT+PO

**EN** Figure 11: Held-out r vs. anchor count; rescalingplateaus below CAL (0.184) and its interval spans zerounder ∼40 anchors. Extended caption in Table 7.

**ZH** 图 11：留出集 r 对锚点数量；重标定在 CAL（0.184）之下就趋于平台，且在约 40 个锚点以下其区间跨越零点。扩展图注见表 7。

**EN** ConstructionCH baseDLQ base

**ZH** 构造　CH 基座　DLQ 基座

**EN** per-rubric, matchedref. (body)

**ZH** 逐维度，匹配参考（正文）

**EN** 83.5–85.560.7/73.1/75.4 vs. ﬂoor56.4/63.8/64.4per-rubric, 3-ratermean ref.

**ZH** 83.5–85.5　60.7/73.1/75.4，对基线 56.4/63.8/64.4；逐维度，三评分者均值参考

**EN** –58.5/71.6/74.0

**ZH** –　58.5/71.6/74.0

**EN** per-judge stacked88.384.3–88.9 vs. ﬂoor 73.9–78.1cohort stacked88.0858.54 obj.; 80.17 subj.cohort PCA axis →human

**ZH** 逐裁判堆叠　88.3　84.3–88.9，对基线 73.9–78.1；群体堆叠　88.08　客观 58.54；主观 80.17；群体 PCA 轴→人类

**EN** 79.0–85.947.7 (TQ); 64.3/65.5 (subj.)

**ZH** 79.0–85.9　47.7（任务质量）；64.3/65.5（主观）

**EN** Table 4:One cohort, four angle constructions(TQ/HAL/LA where three values are given). Stackedangles take the largest principal angle, so they upper-bound the picture; the cohort PCA axis is the judges’best shared direction, so it lower-bounds it; per-rubricangles sit between. Human ﬂoors exist only on DLQ,which has three raters. Every body claim compares likewith like inside one construction; the shaded row is theone the body uses. Full discussion in App. N.

**ZH** 表 4：同一群体，四种角度构造（给出三个值处依次为任务质量／幻觉／语言可接受性）。堆叠角取最大主角度，因此它给出图像的上界；群体 PCA 轴是裁判最好的共享方向，给出下界；逐维度角度居于其间。人类基线只在 DLQ 上存在，那里有三位评分者。正文的每个断言都在同一构造内部作同类比较；阴影行是正文所采用的那一行。完整讨论见附录 N。

**EN** 6Conclusion

**ZH** 6 结论

**EN** High inter-judge agreement is the de facto licensefor replacing human evaluation with LLM judges.We make that license checkable, and it fails where it

**ZH** 裁判间的一致性很高，这是用大模型裁判取代人类评测的事实上的许可证。我们让这张许可证变得可检验，而它在最被倚重的地方失效了：

**EN** is most relied upon: on subjective rubrics our judgesreach the human panel’s consensus level while re-covering only 58–66% of its agreement, collapsingonto a shared axis 64–66◦from the human one; onthe veriﬁable rubric the gap nearly closes, and train-ing restores spread but not orientation. Because thecheck needs only human-anchored items and judgescores already in hand, it runs as a four-step proto-col (App. B): test spread, rank, and angle againstpermutation nulls, reporting the three agreementlegs together; hold each rater out to build the ﬂoora judge must reach; trust an ensemble only if theshared axis itself passes; and on failure, anchor onhuman-rated demonstrations, not more judges. Con-sensus shows that judges share an axis; geometryshows whether it is the human one.

**ZH** 在主观评分维度上，我们的裁判达到了人类小组的共识水平，却只复原了其中 58–66% 的一致，坍缩到一条距人类轴 64–66° 的共享轴上；在可核验的维度上差距几近闭合，而训练恢复的是展布而非方向。由于该检验只需要人类锚定条目和手头已有的裁判分数，它可以作为一个四步协议来运行（附录 B）：对着置换零假设检验展布、秩与角度，并同时报告三条一致性腿；轮流留出每位评分者，构造裁判必须达到的基线；只有当共享轴本身通过检验时才信任集成；若失败，就在人类评过的演示样例上锚定，而不是增加更多裁判。共识表明裁判共享一条轴；几何则表明那是不是人类的轴。

**EN** [Page 10]

**ZH** 第 10 页

**EN** Limitations

**ZH** 局限性

**EN** The geometric account is a diagnostic abstractionover observed score covariance, not a mechanisticclaim about LLM internals (Sec. 3): we cannot tellwhether judges fail to perceive human-weighted di-mensions or perceive but down-weight them, andlabel noise, item ambiguity, and pretraining fa-miliarity remain compatible explanations of theobjective–subjective boundary, so our claim is pre-dictive rather than causal. Consistent with this, dRseparates the two regimes but is ﬂat within each(ρ = −0.03 over six subjective cells) and is entan-gled with inter-rater agreement at n=9 cells. Theobjective regime also rests on a single veriﬁablerubric, replicated across three domains and eightlanguages but still one rubric, and even there thecohort mean does not reach the human ﬂoor: thecrossing we report is for the best single judge andfor two-judge ensembles. Human references areuneven, since community-health merges 15 anno-tators into one pool without per-rater identiﬁers, sono inter-human ﬂoor or rater-level jackknife existsthere and every matched-ﬂoor claim is scoped to theDLQ subset with three independent raters; CH an-gles additionally carry bootstrap intervals 6.3◦wideagainst a 1.6◦between-judge SD, so we rank no CHjudges by angle. Claims are therefore scoped to thetested datasets, languages, and judge families: thedirection of every eﬀect held in all eight languagesbut its size varied by two orders of magnitude andeﬀectively vanished on Telugu, per-language anglesare underpowered at n = 60–300, training coversthree open Indic-capable families (24–32B) on onebenchmark with the demonstration-anchored resultsarvam-m-only, and the diagnostics assume a ﬁxedrubric basis. Finally, closed-API judges may changesilently; we tabulate versions and call dates and re-lease all raw outputs (App. O), but exact reproduc-tion of API-judge scores cannot be guaranteed.

**ZH** 几何解释是对观测分数协方差的诊断式抽象，而非关于大模型内部机制的断言（第 3 节）：我们无法区分裁判是没有感知到人类加权的维度，还是感知到了却下调其权重；标签噪声、条目歧义与预训练熟悉度也仍然是客观—主观边界的相容解释，因此我们的断言是预测性的而非因果性的。与此一致的是，dR 能分开两种机制，却在每种机制内部是平的（六个主观单元上 ρ = −0.03），并且在 n = 9 个单元上与评分者间一致性纠缠在一起。客观机制也只依赖一个可核验的评分维度——虽在三个领域、八种语言中复现，却仍只是一个维度——而且即便在那里，群体均值也没有达到人类基线：我们所报告的跨越只属于最佳单个裁判和两裁判集成。人类参考并不齐整：community-health 把 15 位标注者合并成一个池，没有逐标注者标识，因此那里不存在人类间基线或标注者层面的刀切法，每一条匹配基线的断言都被限定在有三位独立评分者的 DLQ 子集上；此外 CH 角度的自助区间宽 6.3°，而裁判之间的标准差只有 1.6°，故我们不按角度给 CH 裁判排名。因此各项断言都限定在所测试的数据集、语言与裁判系列之内：每个效应的方向在八种语言中都成立，但其大小跨越两个数量级，并在泰卢固语上实际上消失；逐语言角度在 n = 60–300 时效力不足；训练只覆盖三个开放的、具备印度语系能力的系列（24–32B），且只在一个基准上，演示锚定结果仅限 sarvam-m；诊断还假定一组固定的评分维度基。最后，闭源 API 裁判可能静默改变；我们列出版本与调用日期，并发布全部原始输出（附录 O），但 API 裁判分数的精确复现无法保证。

**EN** Ethics Statement

**ZH** 伦理声明

**EN** Our considerations follow Bender and Fried-man (2018).This study performs no newhuman-subjects data collection: we reuse two re-leased benchmarks, community-health (Samik-sha) (Hamna et al., 2026; Bhat et al., 2025) andreal-world cultural QA (Pariksha) (Watts et al.,2024), whose construction and data collection pro-tocols are documented in those papers. They con-tribute the benchmarks and their human labels; thepresent paper reuses that released data and con-

**ZH** 我们的考量遵循 Bender 与 Friedman（2018）。本研究没有开展任何新的人类受试者数据收集：我们复用两个已发布的基准——community-health（Samiksha）（Hamna 等，2026；Bhat 等，2025）与 real-world cultural QA（Pariksha）（Watts 等，2024），其构建与数据采集流程已在那些论文中说明。它们贡献了基准及其人类标注；本论文复用这些已发布的数据，并

**EN** tributes the geometric diagnostics and regime anal-ysis built on it, with no overlap in stated contribu-tions. The released data contain no sensitive per-sonal information, and the items are advisory ques-tions rather than patient records. The paper’s centralcaution is itself a risk-mitigation contribution: de-ploying LLM judges without the geometric check ofSec. 6 risks silently optimising community-facingsystems, such as health advice, toward a judge axisorthogonal to community needs. We used AI assis-tants as detailed in App. Q; all substantive analyses,evaluations, and interpretations were performed andveriﬁed manually by the authors.

**ZH** 贡献建立在其上的几何诊断与机制分析，与它们所声明的贡献没有重叠。发布的数据不含敏感个人信息，条目是咨询性问题而非病历。本论文的核心告诫本身就是一项风险缓解贡献：若不做第 6 节的几何检验就部署大模型裁判，就有可能把面向社区的系统（例如健康建议）静默地优化到一条与社区需求正交的裁判轴上。我们按附录 Q 所述使用了 AI 助手；所有实质性的分析、评测与解读均由作者手工完成并核实。

**EN** [Page 11]

**ZH** 第 11 页

**EN** References

**ZH** 参考文献

**EN** Sanjeev Arora, Yuanzhi Li, Yingyu Liang, Tengyu Ma,

**ZH** Sanjeev Arora、Yuanzhi Li、Yingyu Liang、Tengyu Ma

**EN** and Andrej Risteski. 2018. Linear algebraic struc-ture of word senses, with applications to polysemy.Transactions of the Association for ComputationalLinguistics, 6:483–495.

**ZH** 与 Andrej Risteski。2018。词义的线性代数结构及其在词义歧义中的应用。《计算语言学协会汇刊》，6:483–495。

**EN** Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda

**ZH** Yuntao Bai、Andy Jones、Kamal Ndousse、Amanda

**EN** Askell, Anna Chen, Nova DasSarma, Dawn Drain,Stanislav Fort, Deep Ganguli, Tom Henighan,Nicholas Joseph, Saurav Kadavath, Jackson Kernion,Tom Conerly, Sheer El-Showk, Nelson Elhage, ZacHatﬁeld-Dodds, Danny Hernandez, Tristan Hume,and 12 others. 2022. Training a helpful and harmlessassistant with reinforcement learning from humanfeedback.

**ZH** Askell、Anna Chen、Nova DasSarma、Dawn Drain、Stanislav Fort、Deep Ganguli、Tom Henighan、Nicholas Joseph、Saurav Kadavath、Jackson Kernion、Tom Conerly、Sheer El-Showk、Nelson Elhage、Zac Hatfield-Dodds、Danny Hernandez、Tristan Hume 等 12 人。2022。用人类反馈强化学习训练有用且无害的助手。

**EN** Emily M. Bender and Batya Friedman. 2018.Datastatements for natural language processing: Towardmitigating system bias and enabling better science.Transactions of the Association for ComputationalLinguistics, 6:587–604.

**ZH** Emily M. Bender 与 Batya Friedman。2018。自然语言处理的数据声明：缓解系统偏见、促成更好的科学。《计算语言学协会汇刊》，6:587–604。

**EN** Yoav Benjamini and Yosef Hochberg. 1995. Control-

**ZH** Yoav Benjamini 与 Yosef Hochberg。1995。错误

**EN** ling the false discovery rate: A practical and pow-erful approach to multiple testing. Journal of theRoyal Statistical Society: Series B (Methodological),57(1):289–300.

**ZH** 发现率的控制：一种实用而强大的多重检验方法。《皇家统计学会志：B 辑（方法学）》，57(1):289–300。

**EN** Gayatri Bhat, Hamna Hamna, Sourabrata Mukherjee,

**ZH** Gayatri Bhat、Hamna Hamna、Sourabrata Mukherjee，

**EN** Manan Uppadhyay, Brintha Chandrasekaran, Mon-ali Shelar, Faisal Lalani, Evan Heaﬁeld, Kavitha K,Vivek Seshadri, Manu Chopra, Divya Siddarth, Ka-lika Bali, and Sunayana Sitaram. 2025. Samiksha:What large-scale, community-driven evaluation re-veals about language models for India. TechnicalReport.

**ZH** Manan Uppadhyay、Brintha Chandrasekaran、Monali Shelar、Faisal Lalani、Evan Heafield、Kavitha K、Vivek Seshadri、Manu Chopra、Divya Siddarth、Kalika Bali 与 Sunayana Sitaram。2025。Samiksha：大规模社区驱动的评测揭示了印度语言模型的哪些问题。技术报告。

**EN** Åke Björck and Gene H Golub. 1973. Numerical meth-

**ZH** Åke Björck 与 Gene H Golub。1973。计算线性

**EN** ods for computing angles between linear subspaces.Mathematics of Computation, 27(123):579–594.

**ZH** 子空间之间角度的数值方法。《计算数学》，27(123):579–594。

**EN** Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie

**ZH** Tom B. Brown、Benjamin Mann、Nick Ryder、Melanie

**EN** Subbiah, Jared Kaplan, Prafulla Dhariwal, ArvindNeelakantan, Pranav Shyam, Girish Sastry, AmandaAskell, Sandhini Agarwal, Ariel Herbert-Voss,Gretchen Krueger, Tom Henighan, Rewon Child,Aditya Ramesh, Daniel M. Ziegler, Jeﬀrey Wu,Clemens Winter, and 12 others. 2020. Languagemodels are few-shot learners. In Proceedings of the34th International Conference on Neural InformationProcessing Systems, NIPS ’20, Red Hook, NY, USA.Curran Associates Inc.

**ZH** Subbiah、Jared Kaplan、Prafulla Dhariwal、Arvind Neelakantan、Pranav Shyam、Girish Sastry、Amanda Askell、Sandhini Agarwal、Ariel Herbert-Voss、Gretchen Krueger、Tom Henighan、Rewon Child、Aditya Ramesh、Daniel M. Ziegler、Jeffrey Wu、Clemens Winter 等 12 人。2020。语言模型是少样本学习者。见第 34 届神经信息处理系统国际会议论文集，NIPS '20，Red Hook, NY, USA。Curran Associates Inc.

**EN** Nitay Calderon, Roi Reichart, and Rotem Dror. 2025.

**ZH** Nitay Calderon、Roi Reichart 与 Rotem Dror。2025。

**EN** The alternative annotator test for LLM-as-a-judge:How to statistically justify replacing human anno-tators with LLMs.In Proceedings of the 63rdAnnual Meeting of the Association for Computa-tional Linguistics (Volume 1: Long Papers), pages16051–16081, Vienna, Austria. Association for Com-putational Linguistics.

**ZH** 以大模型为裁判的替代标注者检验：如何在统计上论证用大模型取代人类标注者。见第 63 届计算语言学协会年会论文集（第 1 卷：长文），第 16051–16081 页，Vienna, Austria。Association for Computational Linguistics.

**EN** Cheng-Han Chiang and Hung-yi Lee. 2023. Can large

**ZH** Cheng-Han Chiang 与 Hung-yi Lee。2023。大语言

**EN** language models be an alternative to human evalua-tions? In Proceedings of the 61st Annual Meeting ofthe Association for Computational Linguistics (Vol-ume 1: Long Papers), pages 15607–15631, Toronto,Canada. Association for Computational Linguistics.

**ZH** 模型能成为人类评测的替代者吗？见第 61 届计算语言学协会年会论文集（第 1 卷：长文），第 15607–15631 页，Toronto, Canada。Association for Computational Linguistics.

**EN** Jacob Cohen. 1960. A coeﬃcient of agreement for nom-

**ZH** Jacob Cohen。1960。称名尺度的一致性系数。《教育

**EN** inal scales. Educational and Psychological Measure-ment, 20(1):37–46.

**ZH** 与心理测量》，20(1):37–46。

**EN** John Dang, Shivalika Singh, Daniel D’souza, Arash

**ZH** John Dang、Shivalika Singh、Daniel D'souza、Arash

**EN** Ahmadian, and 1 others. 2024. Aya expanse: Com-bining research breakthroughs for a new multilingualfrontier. Preprint, arXiv:2412.04261.

**ZH** Ahmadian 等 1 人。2024。Aya expanse：融合研究突破开辟多语言新前沿。预印本，arXiv:2412.04261。

**EN** DeepSeek-AI. 2025. DeepSeek-R1 incentivizes reason-

**ZH** DeepSeek-AI。2025。DeepSeek-R1 通过强化学习激励

**EN** ing in LLMs through reinforcement learning. Nature,645(8081):633–638.

**ZH** 大模型中的推理。《自然》，645(8081):633–638。

**EN** Yann Dubois, Xuechen Li, Rohan Taori, Tianyi Zhang,

**ZH** Yann Dubois、Xuechen Li、Rohan Taori、Tianyi Zhang，

**EN** Ishaan Gulrajani, Jimmy Ba, Carlos Guestrin, PercyLiang, and Tatsunori B. Hashimoto. 2023. Alpaca-Farm: A simulation framework for methods that learnfrom human feedback. In Advances in Neural Infor-mation Processing Systems 36 (NeurIPS 2023).

**ZH** Ishaan Gulrajani、Jimmy Ba、Carlos Guestrin、Percy Liang 与 Tatsunori B. Hashimoto。2023。AlpacaFarm：一个用于学习人类反馈方法的仿真框架。见《神经信息处理系统进展 36》（NeurIPS 2023）。

**EN** Bradley Efron. 1979. Bootstrap methods: Another look

**ZH** Bradley Efron。1979。自助法：再论刀切法。《统计

**EN** at the jackknife. The Annals of Statistics, 7(1):1–26.

**ZH** 年刊》，7(1):1–26。

**EN** Gemma Team. 2025.Gemma 3 technical report.Preprint, arXiv:2503.19786. Google DeepMind.

**ZH** Gemma Team。2025。Gemma 3 技术报告。预印本，arXiv:2503.19786。Google DeepMind。

**EN** Aaron Grattaﬁori, Abhimanyu Dubey, Abhinav Jauhri,

**ZH** Aaron Grattafiori、Abhimanyu Dubey、Abhinav Jauhri，

**EN** Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle,Aiesha Letman, Akhil Mathur, Alan Schelten, AlexVaughan, Amy Yang, Angela Fan, Anirudh Goyal, An-thony Hartshorn, Aobo Yang, Archi Mitra, Archie Sra-vankumar, Artem Korenev, Arthur Hinsvark, and 540others. 2024. The llama 3 herd of models. Preprint,arXiv:2407.21783.

**ZH** Abhinav Pandey、Abhishek Kadian、Ahmad Al-Dahle、Aiesha Letman、Akhil Mathur、Alan Schelten、Alex Vaughan、Amy Yang、Angela Fan、Anirudh Goyal、Anthony Hartshorn、Aobo Yang、Archi Mitra、Archie Sravankumar、Artem Korenev、Arthur Hinsvark 等 540 人。2024。The llama 3 herd of models。预印本，arXiv:2407.21783。

**EN** Chuan Guo, GeoﬀPleiss, Yu Sun, and Kilian Q. Wein-

**ZH** Chuan Guo、Geoff Pleiss、Yu Sun 与 Kilian Q. Wein-

**EN** berger. 2017. On calibration of modern neural net-works.In Proceedings of the 34th InternationalConference on Machine Learning, volume 70 ofProceedings of Machine Learning Research, pages1321–1330. PMLR.

**ZH** berger。2017。论现代神经网络的校准。见第 34 届国际机器学习会议论文集，《机器学习研究论文集》第 70 卷，第 1321–1330 页。PMLR。

**EN** Rishav Hada, Varun Gumma, Adrian de Wynter,

**ZH** Rishav Hada、Varun Gumma、Adrian de Wynter，

**EN** Harshita Diddee, Mohamed Ahmed, Monojit Choud-hury, Kalika Bali, and Sunayana Sitaram. 2024. Arelarge language model-based evaluators the solutionto scaling up multilingual evaluation? In Findings ofthe Association for Computational Linguistics: EACL2024, pages 1051–1070, St. Julian’s, Malta. Associa-tion for Computational Linguistics.

**ZH** Harshita Diddee、Mohamed Ahmed、Monojit Choudhury、Kalika Bali 与 Sunayana Sitaram。2024。基于大语言模型的评测器是扩展多语言评测的出路吗？见《计算语言学协会 EACL 2024 会议成果》，第 1051–1070 页，St. Julian's, Malta。Association for Computational Linguistics.

**EN** Hamna Hamna, Gayatri Bhat, Sourabrata Mukherjee,

**ZH** Hamna Hamna、Gayatri Bhat、Sourabrata Mukherjee，

**EN** Faisal M. Lalani, Evan Hadﬁeld, Divya Siddarth,Kalika Bali, and Sunayana Sitaram. 2026. Build-ing benchmarks from the ground up: Community-centered evaluation of LLMs in healthcare chatbotsettings. In Proceedings of the 2026 CHI Conferenceon Human Factors in Computing Systems, CHI ’26,pages 1–19, New York, NY, USA. Association forComputing Machinery.

**ZH** Faisal M. Lalani、Evan Hadfield、Divya Siddarth、Kalika Bali 与 Sunayana Sitaram。2026。从零开始构建基准：医疗聊天机器人场景中以社区为中心的大模型评测。见 2026 年 CHI 计算系统中人的因素会议论文集，CHI '26，第 1–19 页，New York, NY, USA。Association for Computing Machinery.

**EN** [Page 12]

**ZH** 第 12 页

**EN** Daniel Hershcovich, Stella Frank, Heather Lent, Miryam

**ZH** Daniel Hershcovich、Stella Frank、Heather Lent、Miryam

**EN** de Lhoneux, Mostafa Abdou, Stephanie Brandl,Emanuele Bugliarello, Laura Cabello Piqueras, IliasChalkidis, Ruixiang Cui, Constanza Fierro, KaterinaMargatina, Phillip Rust, and Anders Søgaard. 2022.Challenges and strategies in cross-cultural NLP. InProceedings of the 60th Annual Meeting of the As-sociation for Computational Linguistics (Volume 1:Long Papers), pages 6997–7013, Dublin, Ireland. As-sociation for Computational Linguistics.

**ZH** de Lhoneux、Mostafa Abdou、Stephanie Brandl、Emanuele Bugliarello、Laura Cabello Piqueras、Ilias Chalkidis、Ruixiang Cui、Constanza Fierro、Katerina Margatina、Phillip Rust 与 Anders Søgaard。2022。跨文化 NLP 的挑战与策略。见第 60 届计算语言学协会年会论文集（第 1 卷：长文），第 6997–7013 页，Dublin, Ireland。Association for Computational Linguistics.

**EN** Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan

**ZH** Edward J. Hu、Yelong Shen、Phillip Wallis、Zeyuan

**EN** Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, andWeizhu Chen. 2022. LoRA: Low-rank adaptation oflarge language models. In International Conferenceon Learning Representations (ICLR).

**ZH** Allen-Zhu、Yuanzhi Li、Shean Wang、Lu Wang 与 Weizhu Chen。2022。LoRA：大语言模型的低秩适配。见国际学习表征会议（ICLR）。

**EN** Ian T. Jolliﬀe and Jorge Cadima. 2016. Principal com-

**ZH** Ian T. Jolliffe 与 Jorge Cadima。2016。主成分分

**EN** ponent analysis: a review and recent developments.Philosophical Transactions of the Royal Society A:Mathematical, Physical and Engineering Sciences,374(2065):20150202.

**ZH** 析：综述与近期进展。《皇家学会哲学汇刊 A：数学、物理与工程科学》，374(2065):20150202。

**EN** Andrew V Knyazev and Merico E Argentati. 2002.

**ZH** Andrew V Knyazev 与 Merico E Argentati。2002。

**EN** Principal angles between subspaces in an a-basedscalar product: Algorithms and perturbation esti-mates.SIAM Journal on Scientiﬁc Computing,23(6):2008–2040.

**ZH** a-基标量积下子空间之间的主角度：算法与扰动估计。《SIAM 科学计算杂志》，23(6):2008–2040。

**EN** Tom Kocmi and Christian Federmann. 2023. Large lan-

**ZH** Tom Kocmi 与 Christian Federmann。2023。大语言模

**EN** guage models are state-of-the-art evaluators of trans-lation quality. In Proceedings of the 24th AnnualConference of the European Association for MachineTranslation, pages 193–203, Tampere, Finland. Euro-pean Association for Machine Translation.

**ZH** 型是最先进的翻译质量评测器。见第 24 届欧洲机器翻译协会年会论文集，第 193–203 页，Tampere, Finland。European Association for Machine Translation.

**EN** Yang Liu, Dan Iter, Yichong Xu, Shuohang Wang,

**ZH** Yang Liu、Dan Iter、Yichong Xu、Shuohang Wang，

**EN** Ruochen Xu, and Chenguang Zhu. 2023. G-eval:NLG evaluation using GPT-4 with better human align-ment. In Proceedings of the 2023 Conference onEmpirical Methods in Natural Language Processing,pages 2511–2522, Singapore. Association for Com-putational Linguistics.

**ZH** Ruochen Xu 与 Chenguang Zhu。2023。G-eval：用 GPT-4 做自然语言生成评测以获得更好的人类对齐。见 2023 年经验方法自然语言处理会议论文集，第 2511–2522 页，Singapore。Association for Computational Linguistics.

**EN** OpenAI. 2024.GPT-4o system card.Preprint,arXiv:2410.21276.

**ZH** OpenAI。2024。GPT-4o system card。预印本，arXiv:2410.21276。

**EN** OpenAI, Josh Achiam, Steven Adler, Sandhini Agar-

**ZH** OpenAI、Josh Achiam、Steven Adler、Sandhini Agar-

**EN** wal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Ale-man, Diogo Almeida, Janko Altenschmidt, Sam Alt-man, Shyamal Anadkat, Red Avila, Igor Babuschkin,Suchir Balaji, Valerie Balcom, Paul Baltescu, Haim-ing Bao, Mohammad Bavarian, JeﬀBelgum, and261 others. 2023. Gpt-4 technical report. Preprint,arXiv:2303.08774.

**ZH** wal、Lama Ahmad、Ilge Akkaya、Florencia Leoni Aleman、Diogo Almeida、Janko Altenschmidt、Sam Altman、Shyamal Anadkat、Red Avila、Igor Babuschkin、Suchir Balaji、Valerie Balcom、Paul Baltescu、Haiming Bao、Mohammad Bavarian、Jeff Belgum 等 261 人。2023。Gpt-4 technical report。预印本，arXiv:2303.08774。

**EN** Long Ouyang, JeﬀWu, Xu Jiang, Diogo Almeida, Car-

**ZH** Long Ouyang、Jeff Wu、Xu Jiang、Diogo Almeida、Car-

**EN** roll L. Wainwright, Pamela Mishkin, Chong Zhang,Sandhini Agarwal, Katarina Slama, Alex Ray, JohnSchulman, Jacob Hilton, Fraser Kelton, Luke Miller,Maddie Simens, Amanda Askell, Peter Welinder,Paul Christiano, Jan Leike, and Ryan Lowe. 2022.Training language models to follow instructions withhuman feedback. In Advances in Neural Informa-tion Processing Systems 35 (NeurIPS 2022), pages27730–27744.

**ZH** roll L. Wainwright、Pamela Mishkin、Chong Zhang、Sandhini Agarwal、Katarina Slama、Alex Ray、John Schulman、Jacob Hilton、Fraser Kelton、Luke Miller、Maddie Simens、Amanda Askell、Peter Welinder、Paul Christiano、Jan Leike 与 Ryan Lowe。2022。用人类反馈训练语言模型遵循指令。见《神经信息处理系统进展 35》（NeurIPS 2022），第 27730–27744 页。

**EN** John C. Platt. 1999. Probabilistic outputs for support

**ZH** John C. Platt。1999。支持向量机的概率输出，以及

**EN** vector machines and comparisons to regularized like-lihood methods. In Alexander J. Smola, Peter Bartlett,Bernhard Schölkopf, and Dale Schuurmans, editors,Advances in Large Margin Classiﬁers, pages 61–74.MIT Press.

**ZH** 与正则化似然方法的比较。见 Alexander J. Smola、Peter Bartlett、Bernhard Schölkopf 与 Dale Schuurmans 编，《大间隔分类器进展》，第 61–74 页。MIT Press。

**EN** Qwen Team. 2025. Qwen3 technical report. Preprint,

**ZH** Qwen Team。2025。Qwen3 技术报告。预印本，

**EN** arXiv:2505.09388.

**ZH** arXiv:2505.09388。

**EN** Rafael Rafailov, Archit Sharma, Eric Mitchell, Stefano

**ZH** Rafael Rafailov、Archit Sharma、Eric Mitchell、Stefano

**EN** Ermon, Christopher D. Manning, and Chelsea Finn.2023. Direct preference optimization: Your languagemodel is secretly a reward model. In Advances inNeural Information Processing Systems 36 (NeurIPS2023).

**ZH** Ermon、Christopher D. Manning 与 Chelsea Finn。2023。直接偏好优化：你的语言模型其实是一个奖励模型。见《神经信息处理系统进展 36》（NeurIPS 2023）。

**EN** Maithra Raghu, Justin Gilmer, Jason Yosinski, and

**ZH** Maithra Raghu、Justin Gilmer、Jason Yosinski 与

**EN** Jascha Sohl-Dickstein. 2017. SVCCA: Singular vec-tor canonical correlation analysis for deep learningdynamics and interpretability. In Advances in Neu-ral Information Processing Systems 30 (NIPS 2017).Curran Associates, Inc.

**ZH** Jascha Sohl-Dickstein。2017。SVCCA：用于深度学习动态与可解释性的奇异向量典型相关分析。见《神经信息处理系统进展 30》（NIPS 2017）。Curran Associates, Inc.

**EN** Sarvam AI. 2025. Sarvam-m. https://www.sarv

**ZH** Sarvam AI。2025。Sarvam-m。https://www.sarv

**EN** am.ai/blogs/sarvam-m. Technical blog post, 23May 2025; model weights at https://huggingface.co/sarvamai/sarvam-m. Accessed 2026-08-28.

**ZH** am.ai/blogs/sarvam-m。技术博客，2025 年 5 月 23 日；模型权重见 https://huggingface.co/sarvamai/sarvam-m。访问日期 2026-08-28。

**EN** Hinrich Schütze. 1992. Dimensions of meaning. In

**ZH** Hinrich Schütze。1992。意义的维度。见 1992 年

**EN** Proceedings of the 1992 ACM/IEEE Conference onSupercomputing, pages 787–796.

**ZH** ACM/IEEE 超级计算会议论文集，第 787–796 页。

**EN** Peiyi Wang, Lei Li, Liang Chen, Zefan Cai, Dawei Zhu,

**ZH** Peiyi Wang、Lei Li、Liang Chen、Zefan Cai、Dawei Zhu，

**EN** Binghuai Lin, Yunbo Cao, Lingpeng Kong, Qi Liu,Tianyu Liu, and Zhifang Sui. 2024. Large languagemodels are not fair evaluators. In Proceedings of the62nd Annual Meeting of the Association for Compu-tational Linguistics (Volume 1: Long Papers), pages9440–9450, Bangkok, Thailand. Association for Com-putational Linguistics.

**ZH** Binghuai Lin、Yunbo Cao、Lingpeng Kong、Qi Liu、Tianyu Liu 与 Zhifang Sui。2024。大语言模型不是公平的评测者。见第 62 届计算语言学协会年会论文集（第 1 卷：长文），第 9440–9450 页，Bangkok, Thailand。Association for Computational Linguistics.

**EN** Ishaan Watts, Varun Gumma, Aditya Yadavalli, Vivek

**ZH** Ishaan Watts、Varun Gumma、Aditya Yadavalli、Vivek

**EN** Seshadri, Manohar Swaminathan, and SunayanaSitaram. 2024. PARIKSHA: A large-scale investi-gation of human-LLM evaluator agreement on mul-tilingual and multi-cultural data. In Proceedings ofthe 2024 Conference on Empirical Methods in Natu-ral Language Processing, pages 7900–7932, Miami,Florida, USA. Association for Computational Lin-guistics.

**ZH** Seshadri、Manohar Swaminathan 与 Sunayana Sitaram。2024。PARIKSHA：对多语言多文化数据上人类与大模型评测者一致性的大规模考察。见 2024 年经验方法自然语言处理会议论文集，第 7900–7932 页，Miami, Florida, USA。Association for Computational Linguistics.

**EN** Frank Wilcoxon. 1945. Individual comparisons by rank-

**ZH** Frank Wilcoxon。1945。用排序方法做个体比较。《生

**EN** ing methods. Biometrics Bulletin, 1(6):80–83.

**ZH** 物统计学公报》，1(6):80–83。

**EN** Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan

**ZH** Lianmin Zheng、Wei-Lin Chiang、Ying Sheng、Siyuan

**EN** Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin,Zhuohan Li, Dacheng Li, Eric P. Xing, Hao Zhang,Joseph E. Gonzalez, and Ion Stoica. 2023. JudgingLLM-as-a-judge with MT-bench and chatbot arena.In Advances in Neural Information Processing Sys-tems 36 (NeurIPS 2023), Datasets and BenchmarksTrack, pages 46595–46623.

**ZH** Zhuang、Zhanghao Wu、Yonghao Zhuang、Zi Lin、Zhuohan Li、Dacheng Li、Eric P. Xing、Hao Zhang、Joseph E. Gonzalez 与 Ion Stoica。2023。用 MT-bench 与 chatbot arena 评判以大模型为裁判的方法。见《神经信息处理系统进展 36》（NeurIPS 2023），数据集与基准轨道，第 46595–46623 页。

**EN** [Page 13]

**ZH** 第 13 页

**EN** AAppendix guide

**ZH** A 附录导览

**EN** The appendix is organised so that each part answersone kind of question. Readers checking a speciﬁcclaim can go directly to the relevant row of Table 5.

**ZH** 附录的组织方式使每一部分回答一类问题。想核对某条具体断言的读者，可以直接翻到表 5 中相应的那一行。

**EN** BExtended discussion: the pre-trustprotocol

**ZH** B 扩展讨论：预信任协议

**EN** Sec. 6 states the check in prose. This appendix givesthe reading of the results that motivates it, and thenthe procedure itself.

**ZH** 第 6 节以散文形式陈述了这项检验。本附录先给出支撑它的结果解读，再给出流程本身。

**EN** Subjective inter-LLM consensus is perspectivecollapse, not alignment.On real-world cul-tural QA’s subjective rubrics the cohort reachesthe human panel’s consensus level (rll 0.356/0.349vs. rhh 0.357/0.364) while agreeing with humans atonly 58–66% of it (Table 1A). Raters legitimatelydiﬀer on culturally embedded items; the LLMsmatch the consensus statistic not by recovering thatperspective variance but by collapsing onto a sharedaxis 64–66◦from the human one on DLQ (79–86◦

**ZH** 主观维度上的裁判间共识是视角坍缩，而非对齐。在真实世界文化问答的主观评分维度上，裁判群体达到了人类小组的共识水平（rll 0.356／0.349 对 rhh 0.357／0.364），而与人类的一致只有其 58–66%（表 1A）。在深植于文化的条目上，评分者之间有正当的分歧；大模型匹配上这个共识统计量，靠的不是复原那种视角方差，而是坍缩到一条在 DLQ 上距人类 64–66°

**EN** on CH), at eﬀective rank ≤3 where humans usethe full basis (Sec. 5.3, 5.6). In Table 27 the co-hort scores medical completeness while humansweight institutional vulnerability, aﬀordability, andemotional reassurance. Reporting the three legsseparately on one construction makes the collapselegible; an averaged human reference hides it.

**ZH** （CH 上 79–86°）的共享轴上，其有效秩 ≤3，而人类用满整组基（第 5.3、5.6 节）。在表 27 中，裁判群体按医学完整性打分，而人类在意的是制度性脆弱、可负担性与情感安抚。在同一构造上分别报告三条腿，坍缩才看得见；把人类参考平均起来则会把它藏起来。

**EN** Training corrects spread, not orientation, andaggregate gains hide per-rubric harm.Fine-tuning and FT+PO move σJ /σH from 0.32 to 1.08while the angle stays at 87–88◦: rotate-→-human is≤3.5% of ∥∆s∥2 in every stage cell, including thetwo demonstration-anchored stages that produce thelargest Pearson gains (Sec. 5.8). Those stages alsodegrade completeness while over-spreading accu-racy. On sarvam-m only, demonstration anchoringlifts all four rubrics, putting a calibrated 24B In-dic judge (0.184) above gpt-5.5 (0.123) yet still farbelow DLQ inter-human agreement (0.474).

**ZH** 训练修正的是展布，不是方向，而聚合增益掩盖了逐维度的损害。微调与 FT+PO 把 σJ/σH 从 0.32 推到 1.08，角度却停在 87–88°：朝人类的旋转在每个阶段单元中都只占 ‖∆s‖² 的 ≤3.5%，包括带来最大 Pearson 增益的那两个演示锚定阶段（第 5.8 节）。这两个阶段还会在过度展布准确性的同时损害完整性。仅在 sarvam-m 上，演示锚定抬高了全部四个维度，使一个校准后的 24B 印度语系裁判（0.184）超过 gpt-5.5（0.123），却仍远低于 DLQ 的人类间一致性（0.474）。

**EN** The protocol, step by step.The four-step checkbelow is the procedure that follows from the read-ings above; the commentary after it explains whyeach step matters.

**ZH** 协议，逐步说明。下面的四步检验是上述解读所推出的流程；其后的评注解释每一步为何重要。

**EN** Geometric check for LLM-judge consensus

**ZH** 面向大模型裁判共识的几何检验

**EN** 1. Compute σJ /σH, r95, θ against a permutation null;report rll, rlh, rhh together.2. With ≥3 raters, hold one out; score it and each judgeagainst the rest. Rank-matched only if θ beats the nulland nears that ﬂoor.3. Ensembling stalls at the cohort’s shared axis: it substi-tutes only if that axis passes.4. On failure, anchor on human-rated demonstrations;rescaling does not help.

**ZH** 1. 对着置换零假设计算 σJ/σH、r95 与 θ；同时报告 rll、rlh、rhh。2. 若有 ≥3 位评分者，留出一位；让它和每个裁判都对着其余几位计分。只有当 θ 优于零假设并逼近那条基线时，才算秩匹配。3. 集成会停滞在群体的共享轴上：只有当那条轴本身通过检验时，集成才能替代人类。4. 若失败，就在人类评过的演示样例上锚定；重标定无济于事。

**EN** Step 2 is the one most often skipped, and it is the onethat changes conclusions: scoring a judge againsta multi-rater mean while scoring humans againsteach other ﬂatters the judge by several degrees andcan place it above a ﬂoor it does not actually reach(App. N). Budget for it, too: at half our item countthe below-null verdict stopped replicating (App. M).Step 3 matters because a panel’s headline numberaverages over judges that may share one axis; onour subjective rubrics an unlimited ensemble of thetested judges is bounded at 66.5◦/64.6◦, still outsidethe 64.4◦/63.8◦ﬂoor (Table 3). Step 4 is demonstra-tion anchoring rather than rescaling: purely post-hoc aﬃne maps never reach the calibrated judge,and below ∼40 anchors their interval spans zero(Fig. 11).

**ZH** 第 2 步是最常被跳过的，却也是改变结论的那一步：把裁判对着多人均值计分、同时让人类彼此互评，会让裁判被抬高好几个角度，并可能把它放到一个它实际上并未达到的基线之上（附录 N）。也要为它留出预算：在条目数减半时，低于零假设的判定就不再复现（附录 M）。第 3 步重要，是因为一个小组的头条数字是对可能共享同一条轴的裁判取平均；在我们的主观维度上，由受测裁判组成的无限集成被界定在 66.5°／64.6°，仍处在 64.4°／63.8° 的基线之外（表 3）。第 4 步是演示锚定而不是重标定：纯事后仿射映射永远够不到那个校准裁判，且在约 40 个锚点以下其区间跨越零点（图 11）。

**EN** CExtended figure captions

**ZH** C 扩展图注

**EN** Main-body ﬁgures carry short captions to keep theanalysis compact. The full reading of each, in-cluding construction, references, and the caveatsattached to it, is given here.

**ZH** 正文的图都配短图注，以保持分析的紧凑。每一张图完整的读法——包括构造、参考与所附的注意事项——都在这里给出。

**EN** DThe geometric lens, expanded

**ZH** D 几何透镜，展开

**EN** This section expands Sec. 3. It adds the conceptualpicture that motivates the diagnostics, works thevariance identity through to the measured magni-tudes, and states what the lens does and does notclaim.

**ZH** 本节展开第 3 节。它补充了支撑这些诊断指标的概念图景，把方差恒等式算到实测的量级，并说明这面透镜声称什么、不声称什么。

**EN** An idealised picture (conceptual, not mechanis-tic).Imagine quality as a vector with stylistic, fac-tual, and culturally situated components, weightedrubric-conditionally by a rater: objective rubricsconcentrate weight on the factual component, sub-jective rubrics spread it onto culturally situated ones(Hershcovich et al., 2022). A judge whose scoresvary along few directions behaves, at the level ofits score matrix, like a low-rank map. The pictureorganises the predictions P1–P6 and nothing more:we do not model the judge as a literal projectionoperator, and no measurement in this paper dependson that reading. Where the text says a cohort “shares

**ZH** 一幅理想化的图景（概念性的，而非机理性的）。把质量想象成一个带有风格、事实与深植于文化三类分量的向量，由评分者按评分维度条件地加权：客观维度把权重集中在事实分量上，主观维度则把权重摊到文化情境分量上（Hershcovich 等，2022）。一个分数只沿少数几个方向变化的裁判，在其分数矩阵的层面上表现得像一个低秩映射。这幅图景的作用只是把预测 P1–P6 组织起来，别无其他：我们并没有把裁判建模成一个字面意义上的投影算子，本文的任何测量也不依赖这种读法。凡是文中说某个群体“共享

**EN** [Page 14]

**ZH** 第 14 页

**EN** App.ContentsAnswers the question

**ZH** 附录　内容　所回答的问题

**EN** AThis guideWhat is where in the appendix?BThe pre-trust protocol, in fullHow do I actually run the geometric check on my ownjudge and rubric?CExtended ﬁgure and table captionsWhat exactly do the main-body ﬁgures and tablesshow?DThe geometric lens, expandedWhat exactly does Sec. 3 claim, and what does it not?EPer-domain breakdown: datasets, languages, generators, judgesHow many items, languages, and judges are in eachcell, and how do the totals add up?FJudge roster, trained-variant rosterWhich models judge which benchmark, and what isevery trained variant?GRubric deﬁnitions and ordinal scalesWhat exactly was each rubric asking, and on whatscale?HResults-grid column key and codesHow do I read Table 1?IVerbatim evaluation promptsWhat were the judges actually shown?JVariant recipes and hyper-parametersHow was each trained judge produced?KBoundary condition and scopeWhich rubrics fall in which regime, and what does thelens not claim?LAngle methodology, permutation baselineHow is every angle computed, and against what null?MRobustness and control tablesDo the results survive ordinal, reference, FDR, self-preference, and split-half controls?NReconciling the four angle constructionsWhy do angles for the same cohort diﬀer by 30◦acrosstables?OReproducibility, artifact index, API versionsHow do I regenerate every number in this paper?PQualitative item studyWhat do the two regimes look like at the level of singleitems?QUse of AI assistantsWhere were LLM-based tools used, and how was theiroutput checked?

**ZH** A　本导览　附录各部分在哪里？｜B　完整的预信任协议　我该如何在自己的裁判与评分维度上真正跑一遍几何检验？｜C　扩展的图注与表注　正文各图各表究竟展示了什么？｜D　几何透镜，展开　第 3 节究竟断言了什么，又没有断言什么？｜E　按领域拆解：数据集、语言、生成器、裁判　每个单元有多少条目、语言与裁判，总数如何加总？｜F　裁判名单、训练变体名单　哪些模型评哪个基准，每一个训练变体是什么？｜G　评分维度定义与序数尺度　每个维度到底在问什么，用什么尺度？｜H　结果网格的列键与代号　表 1 怎么读？｜I　逐字的评测提示　裁判实际看到的是什么？｜J　变体配方与超参数　每个训练裁判是怎么做出来的？｜K　边界条件与适用范围　哪些评分维度落在哪种机制，透镜不声称什么？｜L　角度方法学与置换基线　每个角怎么算，对照什么零假设？｜M　鲁棒性与控制表　结果能否挺过序数、参考、FDR、自我偏好与分半控制？｜N　调和四种角度构造　为什么同一群体的角度在各表之间相差 30°？｜O　可复现性、产物索引、API 版本　我如何重新生成本文的每一个数字？｜P　条目质性研究　两种机制在单条层面是什么样子？｜Q　AI 助手的使用　在哪里用了基于大模型的工具，其产出如何被检查？

**EN** Table 5: Reader’s guide to the appendix.

**ZH** 表 5：附录阅读导览。

**EN** an axis,” the evidence is a principal-component de-composition of observed scores (Sec. 5.6), not aclaim about model internals.

**ZH** 一条轴”，其证据都是对观测分数做的主成分分解（第 5.6 节），而不是关于模型内部的断言。

**EN** From the identity to the measured magnitudes.Equation 2 is an identity, not an analogy: for a sin-gle direction cos θ = |r|, so 1 −cos2 θ = 1 −r2 isexactly the fraction of human score variance that thejudge direction leaves unexplained. This wires thelens to quantities we can measure. On task qualityone judge direction leaves 1−0.4182 = 83% of hu-man variance unexplained; the entire judge cohort,given a cross-validated ridge ﬁt, still leaves 55%(App. M). Aggregation therefore recovers part ofthe residual but not most of it, which is the same con-clusion the ensemble analysis reaches geometrically(Sec. 5.6). On the subjective DLQ rubrics the co-hort leaves ≈80% unexplained, and on community-health essentially all of it (CV R2 ≤0).

**ZH** 从恒等式到实测的量级。式 2 是恒等式，不是类比：对单一方向有 cos θ = |r|，故 1 − cos²θ = 1 − r² 恰好就是该裁判方向未能解释的人类分数方差比例。这把透镜接到了我们能测量的量上。在任务质量上，一条裁判方向留下 1 − 0.418² = 83% 的人类方差未解释；给定交叉验证的岭回归拟合，整个裁判群体仍留下 55%（附录 M）。因此聚合复原了残差的一部分，而不是大部分——这与集成分析从几何上得到的结论相同（第 5.6 节）。在 DLQ 的主观维度上，群体留下约 80% 未解释，在社区健康上则几乎全部（CV R² ≤ 0）。

**EN** Why rank is necessary but not sufficient.A co-hort whose scores span kJ directions cannot repro-duce human variation that needs dR of them whenkJ < dR, which makes kJ ≥dR necessary. It isnot suﬃcient because rank is a budget, not an aim:a judge may spend four directions on distinctions

**ZH** 为什么秩是必要而不充分的。当一个群体的分数只张成 kJ 个方向时，若 kJ < dR，它就无法复现需要 dR 个方向的人类变异，这使 kJ ≥ dR 成为必要条件。它并不充分，因为秩是预算而不是瞄准：裁判可能把四个方向花在人类并不作出的区分上。

**EN** humans do not make. Our data separate the twocleanly. Across the 40 CH judges eﬀective rank isuncorrelated with alignment (r = 0.12; r95 spans1–4 while angles span 85.0–89.9◦), whereas the ob-jective rubric stays compressed (σ-ratio 0.687) yetrotates to within 4.3◦of the matched human ﬂoor.Orientation, not capacity, is what tracks agreement,which is why we state the boundary as an overlapcondition and treat blindness risk as increasing with1 −overlap rather than with a rank deﬁcit alone.

**ZH** 我们的数据把两者分得很清楚。在 40 个 CH 裁判中，有效秩与对齐不相关（r = 0.12；r95 跨越 1–4，而角度跨越 85.0–89.9°），而客观维度仍然被压缩（σ 比值 0.687）却旋转到了匹配人类基线的 4.3° 之内。跟踪一致性的是方向而不是容量，这正是我们把边界表述为一个重叠条件、并把盲区风险视为随 1 − 重叠增大而非随秩亏增大而增大的原因。

**EN** EPer-domain breakdown of datasets,languages, generators, and judges

**ZH** E 数据集、语言、生成器与裁判的按领域拆解

**EN** Per-domain coverage (referenced from Sec. 4). Ta-ble 8 lists languages, item counts, and rubrics perdomain; Table 9 lists answer generators and judgevariants per domain. Trained judge variants applyonly to community-health. Every count in thesetables is regenerated from the released CSVs by onescript (App. O).

**ZH** 按领域的覆盖情况（由第 4 节引用）。表 8 列出每个领域的语言、条目数与评分维度；表 9 列出每个领域的答案生成器与裁判变体。训练得到的裁判变体只用于社区健康。这些表中的每一个计数都由发布的数据经一个脚本重新生成（附录 O）。

**EN** Human reference panels.community-health:the released labels carry no per-rater identiﬁers andhave only sparse per-rater overlap, so ratings aremerged into one human-community-health refer-

**ZH** 人类参考小组。community-health：发布的标签不带逐评分者标识，且评分者之间的重叠很稀疏，因此评分被合并成一个人类—社区健康参考

**EN** [Page 15]

**ZH** 第 15 页

**EN** FigureExtended caption

**ZH** 图　扩展图注

**EN** Fig. 2Agreement-gap mapOne row per rubric×dataset cell: red = mean LLM–human r, blue = mean inter-LLM r, black ticks = inter-human r (DLQ only); segment length = the LL−LHgap. All three legs are pairwise, so the three markers are directly comparable.Subjective CH rubrics gap widest; task quality narrows it most.Fig. 4Per-judge signature (CH)All 40 CH judges in (σ-ratio, angle-to-human) space, against the single mergedhuman reference (no inter-human ﬂoor exists on CH, so no ﬂoor line is drawn).Colour and marker give the judge family (same mapping as Figs. 12, 6), size scaleswith r95, grey dots are trained variants. Per-judge angles here are not separablefrom one another (Sec. 5.4); the ﬁgure shows the cohort’s position and spread, nota ranking.Fig. 5Rubric-conditional geometry (DLQ)One panel per rubric in (σ-ratio, angle) space, both against the matched two-raterreference: dots = the ﬁve base judges, × = the three held-out humans, + = theﬁve-judge ensemble mean, shaded = judge density. This is the domain-pooled viewof Fig. 6’s columns: task quality pulls the judges toward the human band while σstays below 1, and the subjective panels leave a clear separation.Fig. 12Per-language signature (DLQ)n = 60–300 per panel; total 1, 182. Each panel plots the ﬁve base judges in(σJ /σH, angle) space, both measured against the matched two-rater reference:

**ZH** 图 2　一致性差距图　每个“评分维度×数据集”单元一行：红色 = 平均大模型—人类 r，蓝色 = 平均裁判间 r，黑色刻度 = 人类间 r（仅 DLQ）；线段长度 = LL−LH 差距。三条腿全部成对，因此三个标记可直接比较。主观的 CH 维度差距最宽；任务质量把它收得最窄。｜图 4　逐裁判特征（CH）　(σ 比值, 与人类的夹角) 空间中的全部 40 个 CH 裁判，对着单一的合并人类参考（CH 上不存在人类间基线，故不画基线线）。颜色与标记给出裁判系列（与图 12、图 6 相同的映射），尺寸随 r95 缩放，灰点是训练变体。这里的逐裁判角度彼此不可分离（第 5.4 节）；该图展示的是群体的位置与展布，不是排名。｜图 5　取决于评分维度的几何（DLQ）　每个评分维度一栏，画在 (σ 比值, 角度) 空间中，两者都对着匹配的两位评分者参考：圆点 = 五个基座裁判，× = 三位被留出的人类，+ = 五裁判集成均值，阴影 = 裁判密度。这是图 6 各列的按领域汇总视图：任务质量把裁判拉向人类带，而 σ 仍低于 1，主观各栏则留下清晰的分离。｜图 12　逐语言特征（DLQ）　每栏 n = 60–300；合计 1,182。每栏把五个基座裁判画在 (σJ/σH, 角度) 空间中，两者都对着匹配的两位评分者参考测量：

**EN** colour = judge category, cream band = the σ <1 compression zone, dashed green= the held-out-rater human ﬂoor, open diamond = the ﬁve-judge ensemble mean.Compression is universal, but the angle axis is underpowered at these cell sizes andsaturates near 90◦for judges and humans alike, so we draw no per-language angleconclusions (Sec. 5.5); note also that the diamond averages ﬁve judges while theﬂoor is a single rater, so it is favoured by construction.Fig. 7Inter-judge subspace similarity (CH)Pairwise cosines between Z-scored item×rubric vectors of the 14 base judges +human, Ward-reordered; side strips = family; the human row is outlined and uni-formly pale. cosll =0.16 vs. coslh =0.08; the deepest cells are qwen3-next↔gpt-4o (0.72), llama-3.3↔mistral-L2 (0.67), llama-4-scout↔mistral-L3 (0.54), thenthe qwen3 pair (0.50) — the ﬁrst three cross-vendor, which is why Sec. 5.6 readsthe shared orientation as cohort-wide rather than familial.

**ZH** 颜色 = 裁判类别，米色带 = σ < 1 的压缩区，绿色虚线 = 留出评分者的人类基线，空心菱形 = 五裁判集成均值。压缩是普遍的，但角度轴在这些单元规模下效力不足，且在裁判与人类两侧都饱和在接近 90°，因此我们不给出任何逐语言的角度结论（第 5.5 节）；另需注意菱形平均了五个裁判而基线只是一位评分者，按构造它更占便宜。｜图 7　裁判间子空间相似度（CH）　14 个基座裁判 + 人类的 Z 分数化“条目×维度”向量之间的两两余弦，经 Ward 重排；侧边条 = 系列；人类那一行被描边且始终均匀偏淡。cosll = 0.16 对 coslh = 0.08；最深的单元是 qwen3-next↔gpt-4o（0.72）、llama-3.3↔mistral-L2（0.67）、llama-4-scout↔mistral-L3（0.54），然后才是 qwen3 那一对（0.50）——前三个都是跨厂商的，这正是第 5.6 节把共享方向读作群体层面而非家族层面属性的原因。

**EN** Table 6: Extended captions for the main-body figures (part 1).

**ZH** 表 6：正文各图的扩展图注（第 1 部分）。

**EN** ence (which is why no CH inter-human ﬂoor exists;see Limitations). real-world cultural QA: threeindependent raters (h1, h2, h3) per item per (domain,language), giving a measurable H–H reference.

**ZH** （这也是 CH 上不存在人类间基线的原因；见“局限性”）。real-world cultural QA：每个（领域、语言）每条有三位独立评分者（h1、h2、h3），因而给出一个可测量的人类—人类参考。

**EN** FJudge models

**ZH** F 裁判模型

**EN** Table 10 lists the 15 base LLM judges; Table 11enumerates the 27 trained variants over three Indic-capable families, plus the 4 human reference poolsused as anchors. Four judges (deepseek-r1, grok-4,mistral-large-3, llama-3.3-70b) act as cross-datasetanchors.

**ZH** 表 10 列出 15 个基座大模型裁判；表 11 枚举三个具备印度语系能力系列的 27 个训练变体，外加用作锚点的 4 个人类参考池。四个裁判（deepseek-r1、grok-4、mistral-large-3、llama-3.3-70b）充当跨数据集锚点。

**EN** GRubrics and scoring scales

**ZH** G 评分维度与计分尺度

**EN** Table 12 gives per-dataset rubric deﬁnitionsand ordinal scales (Sec. 4).The community-health comparative paradigm returns one of{A, B, Not Sure} per item with a one-sentenceEnglish rationale. Verbatim prompts in App. I.

**ZH** 表 12 给出各数据集的评分维度定义与序数尺度（第 4 节）。社区健康的对比范式对每条返回一个 {A, B, 不确定} 并附一句英文理由。逐字提示见附录 I。

**EN** HAdditional figures

**ZH** H 补充图

**EN** H.1Consolidated results grid: column keyand codes

**ZH** H.1 合并结果网格：列键与代号

**EN** Table 13 is a compact legend for Table 1. Per-panelnarrative summary in Table 14.

**ZH** 表 13 是表 1 的紧凑图例。逐栏的叙述性摘要见表 14。

**EN** IEvaluation prompts

**ZH** I 评测提示

**EN** Two prompts: standalone multi-rubric and com-parative pairwise. Both are language-agnostic;the judge evaluates within the answer’s languageand writes the explanation in English.

**ZH** 两个提示：独立多维度评分与对比成对比较。两者都与语言无关；裁判在答案自身的语言内评测，并用英文写解释。

**EN** Standalone Multi-Rubric Scoring Prompt

**ZH** 独立多维度评分提示

**EN** Task.Evaluate the answer to the question on fourrubrics.Audience. Internal evaluator. Do not browse. Use onlygeneral knowledge and the given text.Language. The (question, answer) pair may be in Hindi,Kannada, Malayalam, Bengali, Tamil, Telugu, Marathi,or Odia. Judge within the answer’s language. Write theexplanation in concise English.

**ZH** 任务。就四个评分维度对答案作出评价。受众。内部评测器。不要浏览。只使用常识与所给文本。语言。（问题、答案）对可能是印地语、卡纳达语、马拉雅拉姆语、孟加拉语、泰米尔语、泰卢固语、马拉地语或奥里亚语。在答案自身的语言内评判。用简洁的英文写解释。

**EN** Rubrics (one rating per rubric: Yes / Somewhat / No):

**ZH** 评分维度（每个维度一个评分：是／部分／否）：

**EN** i. Clarity & fluency: is the language clear, gram-

**ZH** i. 清晰性与流畅性：语言是否清晰、

**EN** matically correct, easy to understand?

**ZH** 语法正确、易于理解？

**EN** ii. Helpfulness & relevance: does the answer directly

**ZH** ii. 有用性与相关性：答案是否直接

**EN** [Page 16]

**ZH** 第 16 页

**EN** FloatExtended caption

**ZH** 图版　扩展图注

**EN** Fig. 8Stage-wise bootstrapB =1000 over the 405 CH core items: rows are the three diagnostics, columns the threefamilies; violins are bootstrap distributions, points stage means. Stages are groupedby intervention type — the prompt- and demonstration-based ones ﬁrst (base, FS, AT,CAL), then the weight-updating ones (FT, FT+PO) — which is neither pipeline ordernor the order of their Pearson gains; Fig. 10 instead uses pipeline order. Spread risesreliably; angle distributions overlap throughout.Fig. 9Per-rubric training progressionBest in-stage judge per family; one line per community-health rubric. Top: Pearson r,dotted line = the gpt-5.5 anchor. Bottom: σ-ratio, dotted line = judge spread equal tohuman spread. Fine-tuning lifts accuracy while pushing its spread past 2× the humanrange and dragging completeness down; only the demonstration-anchored stages (AT,CAL) raise every rubric with spread still inside the human range.Fig. 10Training-delta decompositionPer-(family, stage) decomposition of ∥∆s∥2 into stretch along the base axis (blue),rotation toward the human axis after the base direction is removed (green), andoﬀ-axis residual (grey);rubric-mean over the four CH rubrics.Stages runbase→FS→FT→FT+PO→AT→CAL, the pipeline order, which is not the order oftheir Pearson gains. Rotation toward human is ≤3.5% across all eleven stage cells, in-cluding both demonstration-anchored stages; aya’s near-zero stretch with ∼97% residualis the clearest case of variance added without alignment.Fig. 11Anchor-size curveHeld-out stacked Pearson r after ﬁtting per-rubric aﬃne maps of two FT+PO judges on nhuman-anchored items (500 resamples; bands are 95% intervals). Dotted lines: the samejudges uncalibrated. Dashed line: the demonstration-anchored calibrated judge (0.184).Rescaling improves monotonically with anchors but plateaus below the uncalibratedjudge on gemma-3 and below CAL on both, and under ∼40 anchors its interval spanszero: the calibration gain of Sec. 5.7 is not a scale correction that more anchors wouldbuy.Table 23Rescaling by anchor countHeld-out stacked Pearson r after ﬁtting per-rubric aﬃne maps of the FT+PO judge onton human-anchored items (500 resamples, seed 20260828; “–” = degenerate ﬁts at n=5).Rescaling never reaches the demonstration-anchored calibrated judge (0.184) and hurtsbelow ∼40–80 anchors; on gemma-3 it never beats the uncalibrated judge at all. Thecalibration lift therefore requires the human-rated demonstrations at inference, not ascale correction.Table 3Ensemble-size curveMean angle◦over all

**ZH** 图 8　分阶段自助法　B = 1000，在 405 条 CH 核心条目上：行是三项诊断指标，列是三个系列；小提琴是自助分布，圆点是阶段均值。阶段按干预类型分组——先是基于提示与演示的（base、FS、AT、CAL），再是更新权重的（FT、FT+PO）——这既不是流水线顺序，也不是它们 Pearson 增益的顺序；图 10 用的才是流水线顺序。展布稳定上升；角度分布全程重叠。｜图 9　逐维度训练进展　每个系列阶段内的最佳裁判；社区健康每个评分维度一条线。上图：Pearson r，点线 = gpt-5.5 锚点。下图：σ 比值，点线 = 裁判展布等于人类展布。微调抬高了准确性，同时把其展布推过人类区间的 2 倍并拖累完整性；只有演示锚定阶段（AT、CAL）在展布仍处于人类区间之内的同时抬高了每一个维度。｜图 10　训练增量分解　按（系列、阶段）把 ‖∆s‖² 分解为沿基座轴的拉伸（蓝色）、去掉基座方向后朝人类轴的旋转（绿色）与离轴残差（灰色）；取四个 CH 维度的均值。阶段顺序为 base→FS→FT→FT+PO→AT→CAL，即流水线顺序，而不是它们 Pearson 增益的顺序。在全部 11 个阶段单元中，朝人类的旋转都 ≤3.5%，两个演示锚定阶段也不例外；aya 近乎为零的拉伸配上约 97% 的残差，是“加了方差却没换来对齐”最清楚的例证。｜图 11　锚点规模曲线　在 n 条人类锚定条目上为两个 FT+PO 裁判拟合逐维度仿射映射后，留出集上的堆叠 Pearson r（500 次重抽样；色带为 95% 区间）。点线：同一批裁判未校准。虚线：演示锚定的校准裁判（0.184）。重标定随锚点数单调改善，但在 gemma-3 上平台低于未校准裁判、在两者上都低于 CAL，且在约 40 个锚点以下其区间跨越零点：第 5.7 节的校准增益并不是靠更多锚点就能买到的尺度修正。｜表 23　按锚点数的重标定　在 n 条人类锚定条目上把 FT+PO 裁判拟合逐维度仿射映射后，留出集上的堆叠 Pearson r（500 次重抽样，种子 20260828；“–” = n = 5 处拟合退化）。重标定永远够不到演示锚定的校准裁判（0.184），在约 40–80 个锚点以下反而是损害；在 gemma-3 上它甚至从未胜过未校准裁判。因此校准增益需要的是推断时的人类评分演示样例，而不是一次尺度修正。｜表 3　集成规模曲线　平均角度°，取遍所有

**EN** 5

**ZH** C(5,

**EN** k

**ZH** k

**EN** subsets of the ﬁve base judges, each scored against the sameheld-out two-rater mean that deﬁnes the ﬂoor in the last column. k→∞sums thegeometric tail of the decrements, which shrink by a near-constant factor (0.59–0.62).On task quality two judges already pass the ﬂoor and the limit is 6◦inside it; on bothsubjective rubrics no attainable ensemble reaches the ﬂoor, and the extrapolated limitstays outside it. Note the asymmetry that runs against us: the ensemble averages ﬁvejudges while the human side is a single rater.

**ZH** 个基座裁判子集，每个子集都对着定义最后一列基线的同一留出两位评分者均值计分。k→∞ 对递减量的几何尾部求和，递减量按近乎恒定的因子（0.59–0.62）收缩。在任务质量上两个裁判就已越过基线，极限落在基线之内 6°；在两个主观维度上，任何可达规模的集成都够不到基线，外推的极限也留在基线之外。注意这个对我们不利的不对称：集成平均了五个裁判，而人类一侧只有一位评分者。

**EN** Table 7: Extended captions for the main-body figures and tables (part 2).

**ZH** 表 7：正文图与表的扩展图注（第 2 部分）。

**EN** address the question and provide useful informa-tion?

**ZH** 回应问题并提供有用的信息？

**EN** iii. Accuracy (general perception): based on general

**ZH** iii. 准确性（总体印象）：基于常识，

**EN** knowledge, does the information seem trustworthyand factually correct?

**ZH** 这些信息是否看起来可信且事实正确？

**EN** iv. Completeness & conciseness: does the answer

**ZH** iv. 完整性与简洁性：答案是否

**EN** provide suﬃcient detail without being verbose orrepetitive?

**ZH** 提供了充分的细节，同时又不冗长、不重复？

**EN** Scoring. Yes= 2, Somewhat= 1, No= 0. Overall =sum of the four.

**ZH** 计分。是 = 2，部分 = 1，否 = 0。总分 = 四项之和。

**EN** Output schema (strict, single minified JSON, noprose, no code fences; line breaks below are for displayonly):

**ZH** 输出格式（严格：单个压缩后的 JSON，无散文本，无代码围栏；下面的换行仅为显示需要）：

**EN** {

**ZH** {

**EN** "clarity": {"rating":"Yes|Somewhat|No",

**ZH** "clarity": {"rating":"是|部分|否",

**EN** "explanation":"..."},"helpfulness": {"rating":"Yes|Somewhat|No",

**ZH** "explanation":"..."},"helpfulness": {"rating":"是|部分|否",

**EN** "explanation":"..."},"accuracy": {"rating":"Yes|Somewhat|No",

**ZH** "explanation":"..."},"accuracy": {"rating":"是|部分|否",

**EN** "explanation":"..."},"completeness": {"rating":"Yes|Somewhat|No",

**ZH** "explanation":"..."},"completeness": {"rating":"是|部分|否",

**EN** "explanation":"..."},"scores": {"clarity":int,"helpfulness":int,

**ZH** "explanation":"..."},"scores": {"clarity":整数,"helpfulness":整数,

**EN** "accuracy":int,"completeness":int,"overall":int}}

**ZH** "accuracy":整数,"completeness":整数,"overall":整数}}

**EN** Question: {{question}}Answer: {{answer}}

**ZH** 问题：{{question}}　答案：{{answer}}

**EN** Return the JSON now.

**ZH** 现在返回 JSON。

**EN** On real-world cultural QA the same tem-plate substitutes three rubrics: task quality, lin-guistic acceptability ({0, 1, 2}), hallucinations({0, 1}).

**ZH** 在真实世界文化问答上，同一模板换用三个评分维度：任务质量、语言可接受性（{0, 1, 2}）、幻觉（{0, 1}）。

**EN** Comparative (Pairwise Preference) Prompt

**ZH** 对比（成对偏好）提示

**EN** Task. Compare two answers to the same question andpick the better one overall.Audience. Internal evaluator. Use only the question, thetwo answers, and general world knowledge; no externalbrowsing.Languages. The (question, A, B) triple may be in Hindi,Kannada, or Malayalam. Judge within the answers’ lan-

**ZH** 任务。比较同一问题的两个答案，总体上挑出更好的一个。受众。内部评测器。只使用问题、两个答案与一般世界知识；不要外部浏览。语言。（问题、A、B）三元组可能是印地语、卡纳达语或马拉雅拉姆语。在答案自身的语

**EN** [Page 17]

**ZH** 第 17 页

**EN** Domain datasetLanguagesQsQARubrics (eval type)

**ZH** 领域数据集　语言　问题数　问答数　评分维度（评测类型）

**EN** community-health (Hamna et al., 2026; Bhat et al., 2025)Hi; Kn; Ml8102,430clarity,helpfulness,ac-curacy,completeness(standalone, {0, 1, 2}); A/B/NS(comparative, 2,430 pairs)DLQ: health & wellness (Watts et al., 2024)8 Indic†–284taskquality({0, 1, 2},obj.);linguisticacceptability({0, 1, 2});hallucinations({0, 1}) (standalone)DLQ: finance (Watts et al., 2024)8 Indic†–323same as aboveDLQ: everyday life (Watts et al., 2024)8 Indic†–575same as above

**ZH** community-health（Hamna 等，2026；Bhat 等，2025）　印地语；卡纳达语；马拉雅拉姆语　810　2,430　清晰性、有用性、准确性、完整性（独立评分，{0, 1, 2}）；A/B/不确定（对比评分，2,430 对）｜DLQ：健康养生（Watts 等，2024）　8 种印度语言†　–　284　任务质量（{0, 1, 2}，客观）；语言可接受性（{0, 1, 2}）；幻觉（{0, 1}）（独立评分）｜DLQ：金融（Watts 等，2024）　8 种印度语言†　–　323　同上｜DLQ：日常生活（Watts 等，2024）　8 种印度语言†　–　575　同上

**EN** Totals8 unique langs9683,6124 domain datasets;170,890LLM-judge calls

**ZH** 合计　8 种不同语言　968　3,612　4 个领域数据集；170,890 次大模型

**EN** Table 8: Per-domain breakdown (datasets, languages, items, rubrics). Hi/Kn/Ml = Hindi/Kannada/Malayalam.†DLQ languages: Bengali, Hindi, Kannada, Malayalam, Marathi, Odia, Tamil, Telugu; per-language item countsare uneven (Hindi 300, Telugu 166, Tamil 150, Bengali 144, Malayalam 130, Kannada 121, Marathi 111, Odia60). DLQ retains the 1,182 items with three complete human ratings, drawn from 158 questions across 27 answergenerators (per-question counts vary, so no per-domain question total is deﬁned). community-health: 270 questions× 3 languages × 3 answer generators = 2,430 QA pairs; all geometric/training analyses use its 405-item core(45 questions/language × 3 languages × 3 generators) with complete topic metadata (Sec. 4). DLQ’s separatelycollected comparative split (21,610 pairs over 10 languages, adding Gujarati and Punjabi) is excluded from analysis(App. M.12).

**ZH** 表 8：按领域拆解（数据集、语言、条目、评分维度）。印地语／卡纳达语／马拉雅拉姆语 = Hindi/Kannada/Malayalam。†DLQ 语言：孟加拉语、印地语、卡纳达语、马拉雅拉姆语、马拉地语、奥里亚语、泰米尔语、泰卢固语；各语言的条目数不均（印地语 300、泰卢固语 166、泰米尔语 150、孟加拉语 144、马拉雅拉姆语 130、卡纳达语 121、马拉地语 111、奥里亚语 60）。DLQ 保留三位人类都评完的 1,182 条，来自 158 个问题的 27 个答案生成器（每个问题下的条目数不等，故不定义按领域的问题总数）。community-health：270 个问题 × 3 种语言 × 3 个答案生成器 = 2,430 个问答对；所有几何／训练分析使用其 405 条核心条目（每语言 45 个问题 × 3 种语言 × 3 个生成器），这些条目具有完整的主题元数据（第 4 节）。DLQ 单独采集的对比切分（10 种语言上的 21,610 对，另含古吉拉特语与旁遮普语）被排除在分析之外（附录 M.12）。

**EN** Fieldcommunity-health

**ZH** 字段　community-health

**EN** Answer generators3: llama-3.1-405b, qwen3, sarvam-m (Hamna et al., 2026; Bhat et al., 2025)Judges, base (14)deepseek-r1; gpt-5.5; gpt-4o; grok-4; mistral-large-3; mistral-large-2; llama-4-scout-17b; llama-3.3-70b; qwen3-235b; qwen3-next-80b; krutrim-2-instruct;aya-expanse-32b; gemma-3-27b; sarvam-m-24bJudges, improved sarvam-m (12 standalone + 1)few-shot; ﬁne-tune v1/v2/v3; pref-optim v2 (v1 comparative-only); ﬁne-tune+pref-optim v1/v2; demo-SFT v1/v2; demo-SFT v1-inf3; calibratedv2/v3Judges, improved gemma-3 (7)few-shot; ﬁne-tune v1/v1-b128/v2; pref-optim v1/v2; ﬁne-tune+pref-optimv2Judges, improved aya-expanse (7)few-shot; ﬁne-tune v1/v2; pref-optim v1/v2; ﬁne-tune+pref-optim v1/v2

**ZH** 答案生成器　3 个：llama-3.1-405b、qwen3、sarvam-m（Hamna 等，2026；Bhat 等，2025）｜裁判，基座（14 个）　deepseek-r1；gpt-5.5；gpt-4o；grok-4；mistral-large-3；mistral-large-2；llama-4-scout-17b；llama-3.3-70b；qwen3-235b；qwen3-next-80b；krutrim-2-instruct；aya-expanse-32b；gemma-3-27b；sarvam-m-24b｜裁判，改进版 sarvam-m（12 个独立评分 + 1 个）　少样本；微调 v1/v2/v3；偏好优化 v2（v1 仅对比）；微调+偏好优化 v1/v2；演示 SFT v1/v2；演示 SFT v1-inf3；校准 v2/v3｜裁判，改进版 gemma-3（7 个）　少样本；微调 v1/v1-b128/v2；偏好优化 v1/v2；微调+偏好优化 v2｜裁判，改进版 aya-expanse（7 个）　少样本；微调 v1/v2；偏好优化 v1/v2；微调+偏好优化 v1/v2

**EN** FieldDLQ: health & wellness / finance / everyday life (identical rosteracross all three)

**ZH** 字段　DLQ：健康养生／金融／日常生活（三个领域名单完全相同）

**EN** Answer generators27 Indic and general instruction-tuned models (Watts et al., 2024)Judges, base (5)deepseek-r1; gpt-4; grok-4; mistral-large-3; llama-3.3-70bJudges, improvednone (trained variants not applied to DLQ)

**ZH** 答案生成器　27 个印度语系与通用指令微调模型（Watts 等，2024）｜裁判，基座（5 个）　deepseek-r1；gpt-4；grok-4；mistral-large-3；llama-3.3-70b｜裁判，改进版　无（训练变体不用于 DLQ）

**EN** Table 9: Answer generators and judge variants per domain. community-health totals 14 base + 27 trainedvariants (26 in the standalone paradigm; sarvam-m pref-optim v1 appears only in the comparative paradigm); thethree DLQ domains share the same 5 base judges, of which four (deepseek-r1, grok-4, mistral-large-3, llama-3.3-70b)also judge community-health. Combined: 42 distinct LLM judges (15 base + 27 trained) across the study.

**ZH** 表 9：各领域的答案生成器与裁判变体。community-health 合计 14 个基座 + 27 个训练变体（独立评分范式下 26 个；sarvam-m 偏好优化 v1 只出现在对比范式中）；三个 DLQ 领域共用同样的 5 个基座裁判，其中四个（deepseek-r1、grok-4、mistral-large-3、llama-3.3-70b）也评 community-health。合并计算：本研究共 42 个不同的大模型裁判（15 个基座 + 27 个训练变体）。

**EN** guage; write the explanation in concise English (≤40words).

**ZH** 言内评判；用简洁的英文写解释（≤40 词）。

**EN** Holistic criteria. Clarity & ﬂuency, helpfulness & rele-vance, factual accuracy / plausibility, completeness (nocritical omissions), and safety. Prefer the answer thatbetter serves the user overall; do not reward hallucinatedor unsafe content.

**ZH** 整体性准则。清晰性与流畅性、有用性与相关性、事实准确性／合理性、完整性（无关键遗漏）与安全性。总体上更服务用户的答案优先；不要奖励含幻觉或不安全的内容。

**EN** Decision rule. Choose A or B if one answer is evenslightly better overall. Choose Not sure only if bothare essentially equal or both are unintelligible/empty.

**ZH** 判定规则。若某个答案总体上哪怕略好，就选 A 或 B。只有当两者实质相当，或两者都无法理解／为空时，才选“不确定”。

**EN** Output (strict, single JSON, exact keys):

**ZH** 输出（严格：单个 JSON，键名精确）：

**EN** {

**ZH** {

**EN** "winner": "A" | "B" | "Not sure","explanation":

**ZH** "winner": "A" | "B" | "不确定", "explanation":

**EN** "<concise justification <=40 words>"}

**ZH** "<简洁理由 <=40 词>"}

**EN** Question: {{question}}Answer A: {{answer_a}}Answer B: {{answer_b}}

**ZH** 问题：{{question}}　答案 A：{{answer_a}}　答案 B：{{answer_b}}

**EN** Return only the JSON now.

**ZH** 现在只返回 JSON。

**EN** [Page 18]

**ZH** 第 18 页

**EN** ModelFamily / orientationSizeAccessData

**ZH** 模型　系列／定位　规模　访问方式　数据

**EN** gpt-5.5GPT (OpenAI), generaln/dAPICHgpt-4oGPT (OpenAI), general (OpenAI, 2024)n/dAPICHgpt-4GPT (OpenAI), general (OpenAI et al., 2023)n/dAPIDLQgrok-4Grok (xAI), generaln/dAPIbothdeepseek-r1DeepSeek (DeepSeek-AI, 2025), reasoning (open weights)671BAPIbothmistral-large-3Mistral, general123BAPIbothmistral-large-2Mistral, general123BlocalCHqwen3-235bQwen (Qwen Team, 2025), multilingual235BlocalCHqwen3-next-80bQwen (Qwen Team, 2025), multilingual80BlocalCHllama-3.3-70bLlama (Grattaﬁori et al., 2024), general70Bbothbothllama-4-scout-17bLlama, general (17B active)109BlocalCHaya-expanse-32bAya (Cohere) (Dang et al., 2024), multilingual32BlocalCHgemma-3-27bGemma (Gemma Team, 2025), multilingual27BlocalCHsarvam-m-24bSarvam (Sarvam AI, 2025), Indic-focused24BlocalCHkrutrim-2-instructKrutrim, Indic-focused12BlocalCH

**ZH** gpt-5.5　GPT（OpenAI），通用　未公开　API　CH｜gpt-4o　GPT（OpenAI），通用（OpenAI，2024）　未公开　API　CH｜gpt-4　GPT（OpenAI），通用（OpenAI 等，2023）　未公开　API　DLQ｜grok-4　Grok（xAI），通用　未公开　API　两者｜deepseek-r1　DeepSeek（DeepSeek-AI，2025），推理（开放权重）　671B　API　两者｜mistral-large-3　Mistral，通用　123B　API　两者｜mistral-large-2　Mistral，通用　123B　本地　CH｜qwen3-235b　Qwen（Qwen Team，2025），多语言　235B　本地　CH｜qwen3-next-80b　Qwen（Qwen Team，2025），多语言　80B　本地　CH｜llama-3.3-70b　Llama（Grattafiori 等，2024），通用　70B　两者　两者｜llama-4-scout-17b　Llama，通用（17B 激活）　109B　本地　CH｜aya-expanse-32b　Aya（Cohere）（Dang 等，2024），多语言　32B　本地　CH｜gemma-3-27b　Gemma（Gemma Team，2025），多语言　27B　本地　CH｜sarvam-m-24b　Sarvam（Sarvam AI，2025），面向印度语系　24B　本地　CH｜krutrim-2-instruct　Krutrim，面向印度语系　12B　本地　CH

**EN** Table 10: The 15 base LLM judges. Size = reported total parameters where disclosed (n/d = not disclosed).Access/Data “both” on the llama-3.3-70b row is not a repeated cell: that judge was served over the API for DLQ andlocally for CH, and it scores both benchmarks. llama-3.1-405b and qwen3 appear in the study only as CH answergenerators, never as judges. Per-domain coverage in Table 8; trained variants in App. J; API deployments and calldates in App. O.

**ZH** 表 10：15 个基座大模型裁判。规模 = 已披露的报告总参数量（未公开 = not disclosed）。llama-3.3-70b 那一行的访问方式／数据“两者”不是重复单元格：该裁判在 DLQ 上通过 API 提供、在 CH 上本地部署，并且它评两个基准。llama-3.1-405b 与 qwen3 在本研究中只作为 CH 的答案生成器出现，从不担任裁判。按领域的覆盖见表 8；训练变体见附录 J；API 部署与调用日期见附录 O。

**EN** 70

**ZH** 70

**EN** 80

**ZH** 80

**EN** 90

**ZH** 90

**EN** angle to H (°)

**ZH** 与人类的夹角（°）

**EN** Hindi (n=300)Telugu (n=166)

**ZH** 印地语（n=300）　泰卢固语（n=166）

**EN** 70

**ZH** 70

**EN** 80

**ZH** 80

**EN** 90

**ZH** 90

**EN** angle to H (°)

**ZH** 与人类的夹角（°）

**EN** Tamil (n=150)Bengali (n=144)

**ZH** 泰米尔语（n=150）　孟加拉语（n=144）

**EN** 70

**ZH** 70

**EN** 80

**ZH** 80

**EN** 90

**ZH** 90

**EN** angle to H (°)

**ZH** 与人类的夹角（°）

**EN** Malayalam (n=130)Kannada (n=121)

**ZH** 马拉雅拉姆语（n=130）　卡纳达语（n=121）

**EN** 0.40.60.81.01.2

**ZH** 0.4 0.6 0.8 1.0 1.2

**EN** σ/σH

**ZH** σJ/σH

**EN** 70

**ZH** 70

**EN** 80

**ZH** 80

**EN** 90

**ZH** 90

**EN** angle to H (°)

**ZH** 与人类的夹角（°）

**EN** Marathi (n=111)

**ZH** 马拉地语（n=111）

**EN** 0.40.60.81.01.2

**ZH** 0.4 0.6 0.8 1.0 1.2

**EN** σ/σH

**ZH** σJ/σH

**EN** Odia (n=60)

**ZH** 奥里亚语（n=60）

**EN** frontier (closed)open xl

**ZH** 前沿（闭源）　开放超大

**EN** open largeopen mid

**ZH** 开放大型　开放中型

**EN** Indic-focusedLLM mean

**ZH** 面向印度语系　大模型均值

**EN** human floor (held-out rater)

**ZH** 人类基线（留出的评分者）

**EN** Figure 12: Per-language signature (DLQ). Compres-sion is universal; angles are underpowered here, so weread none. Each panel plots the ﬁve base judges in(σJ /σH, angle) space against the matched two-rater ref-

**ZH** 图 12：逐语言特征（DLQ）。压缩是普遍的；这里的角度效力不足，故我们一个都不读。每栏把五个基座裁判画在 (σJ/σH, 角度)

**EN** erence; the dashed line is the held-out-rater ﬂoor and theopen diamond the ﬁve-judge ensemble. At n=60–300items per language the stacked angle saturates near 90◦

**ZH** 空间中，对着匹配的两位评分者参考；虚线是留出评分者的基线，空心菱形是五裁判集成。在每语言 n = 60–300 条时，堆叠角在裁判与人类两侧都饱和在接近 90°，

**EN** for judges and humans alike, which is why Sec. 5.5 drawsno per-language angle conclusion and reads the agree-ment gap instead.

**ZH** 这正是第 5.5 节不给出任何逐语言角度结论、而改读一致性差距的原因。

**EN** JJudge variant recipes

**ZH** J 裁判变体配方

**EN** Six recipes applied across three open base fami-lies on community-health. Per-family roster inTable 11. Common controls for all judge scor-

**ZH** 六个配方应用于三个开放基座系列，都在社区健康上。各系列的名单见表 11。所有裁判计分的共同控制项：

**EN** ing: greedy decoding (temperature 0.0, top-p 1.0),max 512 output tokens (1024–2048 on parse-retrypasses), vLLM 0.18.0 in bf16 on 8×B200; train-ing seed 42; bootstrap seed 20260525. SFT labelsare 5,683 per-rubric human judgements from theCH source study (train/val 5,114/569, stratiﬁed bylanguage×rubric×rating; v2 runs oversample rat-ing classes to balance), and DPO uses 2,935 strict-preference comparative triples (Not sure dropped;90/10 split); the training questions have zero over-lap with the 810 evaluation questions. Per-versionYAML conﬁgs and training logs ship in the release(App. O).

**ZH** 贪心解码（temperature 0.0，top-p 1.0），最多 512 个输出 token（解析重试时为 1024–2048），vLLM 0.18.0、bf16、8×B200；训练种子 42；自助法种子 20260525。SFT 标签是来自 CH 源研究的 5,683 条逐维度人类判断（训练／验证 5,114／569，按语言×维度×评分分层；v2 运行对评分类别过采样以平衡），DPO 使用 2,935 个严格偏好对比三元组（丢弃“不确定”；90/10 划分）；训练问题与 810 个评测问题零重叠。各版本的 YAML 配置与训练日志随发布物提供（附录 O）。

**EN** KBoundary condition and scope of theframework

**ZH** K 框架的边界条件与适用范围

**EN** Extends Sec. 3. Let dR be the participation ratioof the human score matrix under rubric R (Eq. 1,measured from human raters alone and capped atthe panel size, so it reports the dimensionality ofrater disagreement rather than of human qualityitself) and kJ the judge cohort’s eﬀective rank. Theboundary is rank-necessary, orientation-decisive(Eq. 2): kJ ≥dR is required for alignment to bepossible, but the decisive quantity is the orientationoverlap cos2 θ(SJ , SH); measured eﬀective rankdoes not predict alignment (r = 0.12 across 40CH judges; Sec. 5.4). Table 16 summarises whichregimes the framework does and does not cover.

**ZH** 本节延伸第 3 节。设 dR 为评分维度 R 下人类分数矩阵的参与率（式 1，仅由人类评分者测量，并受评分小组规模封顶，因此它报告的是评分者分歧的维度数，而非人类质量本身的维度数），kJ 为裁判群体的有效秩。边界是秩必要、方向决定性的（式 2）：kJ ≥ dR 是对齐得以可能的必要条件，但决定性的量是方向重叠 cos²θ(SJ, SH)；实测的有效秩并不能预测对齐（40 个 CH 裁判上 r = 0.12；第 5.4 节）。表 16 汇总该框架覆盖与不覆盖哪些机制。

**EN** [Page 19]

**ZH** 第 19 页

**EN** Variant IDRecipeDisplayStacked r

**ZH** 变体 ID　配方　显示名　堆叠 r

**EN** sarvammbasesarvam-m (24b)0.106sarvamm_fsfew-shotsarvam-m (fewshot)0.184sarvamm_ft_v1ﬁne-tunesarvam-m (FT v1)0.119sarvamm_ft_v2ﬁne-tunesarvam-m (FT v2)0.127sarvamm_ft_v3ﬁne-tunesarvam-m (FT v3)0.120sarvamm_po_v1pref-optimsarvam-m (PO v1; comparative-only)—sarvamm_po_v2pref-optimsarvam-m (PO v2)0.094sarvamm_ft_po_v1FT + POsarvam-m (FT+PO v1)0.112sarvamm_ft_po_v2FT + POsarvam-m (FT+PO v2)0.136sarvamm_ft_v3_demo1demo-SFTsarvam-m (demo-SFT v1; AT v1)0.106sarvamm_ft_v3_demo2demo-SFTsarvam-m (demo-SFT v2; AT v2)0.160sarvamm_ft_v3_demo1_infer3demo-SFTsarvam-m (demo-SFT v1-inf3; AT v1-inf3)0.177sarvamm_po_v3_cal_2democalibratedsarvam-m (CAL v2)0.178sarvamm_po_v3_cal_3democalibratedsarvam-m (CAL v3)0.184

**ZH** sarvamm　基座　sarvam-m（24b）　0.106｜sarvamm_fs　少样本　sarvam-m（少样本）　0.184｜sarvamm_ft_v1　微调　sarvam-m（FT v1）　0.119｜sarvamm_ft_v2　微调　sarvam-m（FT v2）　0.127｜sarvamm_ft_v3　微调　sarvam-m（FT v3）　0.120｜sarvamm_po_v1　偏好优化　sarvam-m（PO v1；仅对比）　—｜sarvamm_po_v2　偏好优化　sarvam-m（PO v2）　0.094｜sarvamm_ft_po_v1　FT + PO　sarvam-m（FT+PO v1）　0.112｜sarvamm_ft_po_v2　FT + PO　sarvam-m（FT+PO v2）　0.136｜sarvamm_ft_v3_demo1　演示 SFT　sarvam-m（演示 SFT v1；AT v1）　0.106｜sarvamm_ft_v3_demo2　演示 SFT　sarvam-m（演示 SFT v2；AT v2）　0.160｜sarvamm_ft_v3_demo1_infer3　演示 SFT　sarvam-m（演示 SFT v1-inf3；AT v1-inf3）　0.177｜sarvamm_po_v3_cal_2　演示校准　sarvam-m（CAL v2）　0.178｜sarvamm_po_v3_cal_3　演示校准　sarvam-m（CAL v3）　0.184

**EN** gemma-3-27b-itbasegemma-3 (27b)0.124gemma-3-27b-it_fsfew-shotgemma-3 (fewshot)0.166gemma-3-27b-it_ft_v1ﬁne-tunegemma-3 (FT v1)0.102gemma-3-27b-it_ft_v1_b128ﬁne-tunegemma-3 (FT v1-b128)0.090gemma-3-27b-it_ft_v2ﬁne-tunegemma-3 (FT v2)0.164gemma-3-27b-it_po_v1pref-optimgemma-3 (PO v1)0.115gemma-3-27b-it_po_v2pref-optimgemma-3 (PO v2)0.115gemma-3-27b-it_ft_po_v2FT + POgemma-3 (FT+PO v2)0.155

**ZH** gemma-3-27b-it　基座　gemma-3（27b）　0.124｜gemma-3-27b-it_fs　少样本　gemma-3（少样本）　0.166｜gemma-3-27b-it_ft_v1　微调　gemma-3（FT v1）　0.102｜gemma-3-27b-it_ft_v1_b128　微调　gemma-3（FT v1-b128）　0.090｜gemma-3-27b-it_ft_v2　微调　gemma-3（FT v2）　0.164｜gemma-3-27b-it_po_v1　偏好优化　gemma-3（PO v1）　0.115｜gemma-3-27b-it_po_v2　偏好优化　gemma-3（PO v2）　0.115｜gemma-3-27b-it_ft_po_v2　FT + PO　gemma-3（FT+PO v2）　0.155

**EN** aya-expanse-32bbaseaya-expanse (32b)0.011aya-expanse-32b_fsfew-shotaya-expanse (fewshot)0.019aya-expanse-32b_ft_v1ﬁne-tuneaya-expanse (FT v1)0.041aya-expanse-32b_ft_v2ﬁne-tuneaya-expanse (FT v2)0.098aya-expanse-32b_po_v1pref-optimaya-expanse (PO v1)0.072aya-expanse-32b_po_v2pref-optimaya-expanse (PO v2)0.072aya-expanse-32b_ft_po_v1FT + POaya-expanse (FT+PO v1)0.041aya-expanse-32b_ft_po_v2FT + POaya-expanse (FT+PO v2)0.107

**ZH** aya-expanse-32b　基座　aya-expanse（32b）　0.011｜aya-expanse-32b_fs　少样本　aya-expanse（少样本）　0.019｜aya-expanse-32b_ft_v1　微调　aya-expanse（FT v1）　0.041｜aya-expanse-32b_ft_v2　微调　aya-expanse（FT v2）　0.098｜aya-expanse-32b_po_v1　偏好优化　aya-expanse（PO v1）　0.072｜aya-expanse-32b_po_v2　偏好优化　aya-expanse（PO v2）　0.072｜aya-expanse-32b_ft_po_v1　FT + PO　aya-expanse（FT+PO v1）　0.041｜aya-expanse-32b_ft_po_v2　FT + PO　aya-expanse（FT+PO v2）　0.107

**EN** h_chhuman referenceCH human reference (merged pool)ref.h1human raterDLQ human h1—h2human raterDLQ human h2—h3human raterDLQ human h3—

**ZH** h_ch　人类参考　CH 人类参考（合并池）　参考｜h1　人类评分者　DLQ 人类 h1　—｜h2　人类评分者　DLQ 人类 h2　—｜h3　人类评分者　DLQ 人类 h3　—

**EN** Table 11: The three trainable families and their 27 trained variants (12 + 7 + 7 = 26 in the standalone paradigm;sarvamm_po_v1 appears only in the comparative paradigm), plus 4 human reference pools. Together with the15 base judges of Table 10 the study spans 42 distinct LLM judges. Stacked r is each variant’s stacked Pearsoncorrelation with the merged CH human pool over all four rubrics (n=1620 judge–item scores), the same quantityplotted in Fig. 13; higher is better, and even the top value is far below DLQ inter-human agreement (0.474). “ref.”marks the pool the correlation is taken against; “—” marks rows with no standalone CH score (the comparative-onlyvariant and the three DLQ annotators). Two cautions when reading this column. First, it is an aggregate: few-shot(0.1837) and CAL v3 (0.1845) are indistinguishable here, and the demonstration-anchored advantage is visible onlyper rubric, where few-shot leaves completeness ﬂat (Fig. 9). Second, identical entries within a family (e.g. gemmaPO v1/v2) are genuine rather than duplicated cells: those variants are so compressed that they place nearly everyitem in the top rating class. Recipe deﬁnitions and hyper-parameters in App. J.

**ZH** 表 11：三个可训练系列及其 27 个训练变体（独立评分范式下 12 + 7 + 7 = 26 个；sarvamm_po_v1 只出现在对比范式中），外加 4 个人类参考池。与表 10 的 15 个基座裁判合计，本研究共覆盖 42 个不同的大模型裁判。堆叠 r 是各变体在全部四个维度上与合并后的 CH 人类池的堆叠 Pearson 相关（n = 1620 个裁判—条目分数），即图 13 所画的同一个量；越高越好，而即便最高值也远低于 DLQ 的人类间一致性（0.474）。“参考”标记该相关所对照的池；“—”标记没有独立 CH 分数的行（仅对比的变体与三位 DLQ 标注者）。读这一列时有两点提醒。第一，它是聚合值：少样本（0.1837）与 CAL v3（0.1845）在这里无法区分，演示锚定的优势只有逐维度才看得出来——少样本让完整性原地不动（图 9）。第二，同一系列内的相同取值（例如 gemma 的 PO v1/v2）是真实的而非重复单元格：那些变体被压缩得极厉害，几乎把每个条目都放进最高评级类。配方定义与超参数见附录 J。

**EN** LAngle methodology and permutationbaseline

**ZH** L 角度方法学与置换基线

**EN** Matrices.For judge J , the score matrix SJ ∈Rn×m holds ordinal scores for n items and mrubrics (m=4 on community-health over the 405-item core; m=3 on real-world cultural QAover 1,182 items). The human reference is themerged pool on CH (a single reference, so no ﬂooris measurable there). On DLQ every comparisonthat is read against a human ﬂoor uses the matchedreference: one of the three raters is held out, themean of the other two is the reference, and the held-out rater and each judge are both scored againstit, averaged over the three folds. This keeps both

**ZH** 矩阵。对裁判 J，分数矩阵 SJ ∈ Rn×m 存放 n 个条目、m 个评分维度上的序数分数（社区健康在 405 条核心条目上 m = 4；真实世界文化问答在 1,182 条上 m = 3）。人类参考在 CH 上是合并池（单一参考，因此那里测不出基线）。在 DLQ 上，凡是要对着人类基线来读的比较都用匹配参考：三位评分者中留出一位，其余两位的均值作为参考，被留出的评分者与每个裁判都对着它计分，并在三个折上取平均。这使

**EN** sides a single rater facing the same two-rater target;scoring judges against the three-rater mean whilescoring humans against each other gives judges aless noisy target and shifts them several degrees intheir own favour (App. N). Where an unmatchedconstruction is reported for continuity with earliertables, it is labelled as such.

**ZH** 两侧都是单个评分者面对同一个两位评分者靶子；把裁判对着三评分者均值计分、同时让人类彼此互评，等于给裁判一个噪声更小的靶子，并使它们在自己有利的方向上偏移好几个角度（附录 N）。凡是为与早先表格保持连续而报告未匹配构造之处，都会明确标注。

**EN** Per-rubric angle.For one rubric, judge and refer-ence are vectors s, h ∈Rn. After mean-centering,cos θ = |⟨sc, hc⟩|/(∥sc∥∥hc∥) = |r(s, h)|, so theper-rubric angle is exactly θ = arccos |r| for Pear-son r: per-rubric angles restate correlations in ageometry that composes with the stacked construc-tion.

**ZH** 逐维度角度。对单个评分维度，裁判与参考是向量 s, h ∈ Rn。中心化之后，cos θ = |⟨sc, hc⟩|/(‖sc‖‖hc‖) = |r(s, h)|，因此逐维度角度恰好就是 θ = arccos |r|（r 为 Pearson 相关）：逐维度角度把相关性重述成一种可与堆叠构造复合的几何。

**EN** [Page 20]

**ZH** 第 20 页

**EN** DatasetRubricScaleDefinition

**ZH** 数据集　评分维度　尺度　定义

**EN** community-healthclarity & ﬂuency{0, 1, 2}language clear, grammatical, easy to understandcommunity-healthhelpfulness & relevance{0, 1, 2}directly addresses the question with useful infocommunity-healthaccuracy{0, 1, 2}trustworthy under general medical knowledgecommunity-healthcompleteness & concis.{0, 1, 2}suﬃcient detail without verbosity (short name: complete-ness)

**ZH** community-health　清晰性与流畅性　{0, 1, 2}　语言清晰、语法正确、易于理解｜community-health　有用性与相关性　{0, 1, 2}　直接回应问题并提供有用信息｜community-health　准确性　{0, 1, 2}　在一般医学知识下可信｜community-health　完整性与简洁性　{0, 1, 2}　细节充分而不冗长（简称：完整性）

**EN** real-world cultural QAtask quality (obj.){0, 1, 2}satisﬁes task constraints; veriﬁable ground truthreal-world cultural QAlinguistic acceptability{0, 1, 2}native-speaker grammaticality and naturalnessreal-world cultural QAhallucinations{0, 1}binary presence of unsupported content

**ZH** real-world cultural QA　任务质量（客观）　{0, 1, 2}　满足任务约束；有可核验的真值｜real-world cultural QA　语言可接受性　{0, 1, 2}　母语者的语法性与自然度｜real-world cultural QA　幻觉　{0, 1}　是否存在无依据内容的二值判断

**EN** Table 12: Rubric deﬁnitions and ordinal scales. Yes= 2 / Somewhat= 1 / No= 0 on community-health; taskquality is the single objective rubric in this study.

**ZH** 表 12：评分维度定义与序数尺度。community-health 上是 是 = 2／部分 = 1／否 = 0；任务质量是本研究中唯一的客观评分维度。

**EN** Symbol / codeMeaning

**ZH** 符号／代号　含义

**EN** njudges/humans in cohortσJ/σHscore-spread ratio (judge SD over human-reference SD, per rubric, item-level)θ◦angle to human reference (panel A: per-rubric arccos |r| against the matched two-raterreference; panels B–C: per-judge stacked; App. L)θ◦

**ZH** n　群体中的裁判／人类数量｜σJ/σH　分数展布比（逐评分维度、条目级的裁判标准差与人类参考标准差之比）｜θ°　与人类参考的夹角（A 栏：相对匹配的两位评分者参考的逐维度 arccos |r|；B–C 栏：逐裁判堆叠；附录 L）｜θ°

**EN** hh / rhhhuman ﬂoor: held-out rater vs. the same two-rater reference / pairwise inter-humanPearson (three DLQ raters; CH has one merged pool, so neither exists)r / rrefPearson vs. the panel’s stated reference; in panel A all three legs are pairwise∆gap to the panel referencerJ

**ZH** hh / rhh　人类基线：被留出的评分者对同一两位评分者参考／成对的人类间 Pearson（三位 DLQ 评分者；CH 只有一个合并池，故两者都不存在）｜r / rref　相对该栏所声明参考的 Pearson；A 栏中三条腿全部成对｜Δ　相对该栏参考的差距｜rJ

**EN** 95eﬀective rank (95% variance) of the item×rubric matrix4lifts all four CH rubrics over BASE (unmarked trained rows do not)

**ZH** 95　“条目×评分维度”矩阵的有效秩（95% 方差）｜标记 4　把全部四个 CH 维度抬到 BASE 之上（未标记的已训练行做不到）

**EN** CH / DLQcommunity-health (Samiksha) / real-world cultural QA (Pariksha)LA / HAL / TQlinguistic acceptability, hallucinations (subj.); task quality (obj.)FE / OXL / OM / IFCH base strata: FE API frontier = {gpt-5.5, gpt-4o, grok-4, deepseek-r1}; OXLopen ≥100B = {mistral-large-3, mistral-large-2, qwen3-235b, llama-4-scout}; OMopen 27–80B = {llama-3.3-70b, qwen3-next-80b, gemma-3-27b, aya-expanse-32b};IF Indic-focused = {sarvam-m-24b, krutrim-2}; ﬁgure legends use a ﬁner ﬁve-wayscheme that splits OM into open-large (70–80B) and open-mid (27–32B)BASE / FS / FT / FT+PO / AT / CALbase; few-shot; LoRA SFT; SFT+DPO; demonstration-augmented SFT; demonstration-anchored calibration (AT, CAL: sarvam-m only)

**ZH** CH / DLQ　community-health（Samiksha）／real-world cultural QA（Pariksha）｜LA / HAL / TQ　语言可接受性、幻觉（主观）；任务质量（客观）｜FE / OXL / OM / IF　CH 的基座分层：FE = API 前沿 {gpt-5.5, gpt-4o, grok-4, deepseek-r1}；OXL = 开放 ≥100B {mistral-large-3, mistral-large-2, qwen3-235b, llama-4-scout}；OM = 开放 27–80B {llama-3.3-70b, qwen3-next-80b, gemma-3-27b, aya-expanse-32b}；IF = 面向印度语系 {sarvam-m-24b, krutrim-2}；图例使用更细的五分方案，把 OM 拆成开放大型（70–80B）与开放中型（27–32B）｜BASE / FS / FT / FT+PO / AT / CAL　基座；少样本；LoRA SFT；SFT+DPO；演示增强 SFT；演示锚定校准（AT、CAL 仅用于 sarvam-m）

**EN** Table 13: Column key and code legend for the consolidated results grid.

**ZH** 表 13：合并结果网格的列键与代号图例。

**EN** PanelOne-line narrative

**ZH** 栏　一句话叙述

**EN** (A)the LLM–human shortfall below inter-LLM agreement is +0.087 on CH’s compressed scale and +0.110–+0.149across the DLQ rubrics; DLQ task quality closes most of the gap, reaching 88% of the inter-human band (r=0.418 vs.0.474) at a matched angle of 60.7◦against a 56.4◦ﬂoor, with the best single judge inside it.(B)no base stratum closes more than 0.04 of the CH gap; angles stay at 87.5–89.6◦across all strata: base-model choice isnot the lever.(C)σJ /σH rises 0.319→1.078 across FT/FT+PO; θ◦stays at 87–88◦; only the demonstration-anchored stages (AT, CAL)lift all four rubrics.

**ZH** (A)　大模型—人类低于裁判间一致性的缺口，在 CH 被压缩的尺度上是 +0.087，在 DLQ 各维度上是 +0.110–+0.149；DLQ 任务质量弥合了大部分差距，达到人类间带的 88%（r = 0.418 对 0.474），匹配角为 60.7°、基线 56.4°，且最佳单个裁判落在基线之内。｜(B)　没有一个基座分层弥合掉 CH 差距的 0.04 以上；各分层的角度都停在 87.5–89.6°：换基座模型不是那根杠杆。｜(C)　σJ/σH 在 FT／FT+PO 下从 0.319 升到 1.078；θ° 停在 87–88°；只有演示锚定阶段（AT、CAL）抬高了全部四个维度。

**EN** Table 14: Per-panel narrative of Table 1.

**ZH** 表 14：表 1 的逐栏叙述。

**EN** Stacked angle.Columns of SJ and SH aremean-centered; each matrix is reduced by SVDto the smallest basis capturing 95% of squaredsingular-value energy; the reported statistic isthe largest principal angle (Björck and Golub,1973; Knyazev and Argentati, 2002) between thetwo bases, truncated to the smaller of the tworanks.Sensitivity:at 90/95/99% energy theCH cohort angle is 88.0/88.1/88.6◦; raw, cen-tered, z-scored, and rank-normalised preprocessing

**ZH** 堆叠角。SJ 与 SH 的各列先中心化；每个矩阵经 SVD 约简到能捕获 95% 平方奇异值能量的最小基；所报告的统计量是两个基之间的最大主角度（Björck 与 Golub，1973；Knyazev 与 Argentati，2002），并截断到两者中较小的秩。敏感性：在 90／95／99% 能量下，CH 群体角为 88.0／88.1／88.6°；原始、中心化、Z 分数化与秩归一化的预处理

**EN** give 88.08/88.08/88.50/88.38◦; the DLQ subjec-tive and objective stacked angles (80.17◦, 58.54◦)are unchanged to two decimals under raw/cen-tered/z-scored preprocessing at every cutoﬀ(rank-normalised: 80.42◦, 59.65◦).

**ZH** 给出 88.08／88.08／88.50／88.38°；DLQ 的主观与客观堆叠角（80.17°、58.54°）在各截断阈值下经原始／中心化／Z 分数化预处理都保持两位小数不变（秩归一化：80.42°、59.65°）。

**EN** Permutation null.Because near-orthogonalityis generic in high dimension, every angle is readagainst a permutation null: the human vector (per-rubric; 500 permutations per judge, seed 20260710)

**ZH** 置换零假设。由于高维下近似正交是常态，每个角都对着一个置换零假设来读：把人类向量（逐维度；每裁判 500 次置换，种子 20260710）

**EN** [Page 21]

**ZH** 第 21 页

<!-- [原子块 · img]  -->

**EN** Figure on page 21

**ZH** 第 21 页的图

<!-- [原子块 · img]  -->

**EN** Figure on page 21

**ZH** 第 21 页的图

**EN** 0.000.050.100.150.200.250.30stacked Pearson r against the human reference

**ZH** 0.00 0.05 0.10 0.15 0.20 0.25 0.30　与人类参考的堆叠 Pearson r

**EN** 20 gemma-3 (pref-optim v2)19 sarvam-m (fine-tune v1)18 sarvam-m (fine-tune v3)17 gpt-5.516 gemma-3 (27b)15 sarvam-m (fine-tune v2)14 llama-4-scout13 gpt-4o12 mistral-large-311 sarvam-m (fine-tune+pref-optim v2)10 qwen3-next (80b) 9 gemma-3 (fine-tune+pref-optim v2)

**ZH** 20 gemma-3（偏好优化 v2）｜19 sarvam-m（微调 v1）｜18 sarvam-m（微调 v3）｜17 gpt-5.5｜16 gemma-3（27b）｜15 sarvam-m（微调 v2）｜14 llama-4-scout｜13 gpt-4o｜12 mistral-large-3｜11 sarvam-m（微调+偏好优化 v2）｜10 qwen3-next（80b）｜9 gemma-3（微调+偏好优化 v2）

**EN** 8 sarvam-m (demo-SFT v2)

**ZH** 8 sarvam-m（演示 SFT v2）

**EN** 7 gemma-3 (fine-tune v2)

**ZH** 7 gemma-3（微调 v2）

**EN** 6 gemma-3 (fewshot)

**ZH** 6 gemma-3（少样本）

**EN** 5 grok-4 4 sarvam-m (demo-SFT v1-inf3)

**ZH** 5 grok-4　4 sarvam-m（演示 SFT v1-inf3）

**EN** 3 sarvam-m (calibrated v2)

**ZH** 3 sarvam-m（校准 v2）

**EN** 2 sarvam-m (fewshot) 1 sarvam-m (calibrated v3)

**ZH** 2 sarvam-m（少样本）　1 sarvam-m（校准 v3）

**EN** gpt-5.5best calibrated 24B

**ZH** gpt-5.5　最佳校准 24B

**EN** frontier (closed)open XLopen largeopen midtrained variantper-rubric range

**ZH** 前沿（闭源）　开放超大　开放大型　开放中型　训练变体　逐维度范围

**EN** Figure 13: Judge ranking. Top 20 of the 40 community-health judges by stacked Pearson r over the 405-itemcore (nobs =1,620 item×rubric cells). Each marker is a judge’s aggregate r, coloured by family; the pale bar behindit spans that judge’s four per-rubric values. The dotted line marks gpt-5.5 (0.123) and the dashed line the bestcalibrated 24B judge (0.184). Fine-tune and pref-optim versions (v1/v2/v3) are labelled separately.

**ZH** 图 13：裁判排名。社区健康 40 个裁判中按 405 条核心条目上的堆叠 Pearson r 取前 20（nobs = 1,620 个条目×维度单元）。每个标记是一个裁判的聚合 r，按系列着色；其后的淡色条横跨该裁判的四个逐维度值。点线标出 gpt-5.5（0.123），虚线标出最佳校准 24B 裁判（0.184）。微调与偏好优化版本（v1/v2/v3）分别标注。

**EN** Hindi

**ZH** 印地语

**EN** Kannada

**ZH** 卡纳达语

**EN** Malayalam

**ZH** 马拉雅拉姆语

**EN** sarvam-m (calibrated v3)

**ZH** sarvam-m（校准 v3）

**EN** gpt-4o

**ZH** gpt-4o

**EN** sarvam-m (calibrated v2)

**ZH** sarvam-m（校准 v2）

**EN** sarvam-m (fewshot)

**ZH** sarvam-m（少样本）

**EN** sarvam-m (demo-SFT v1-inf3)

**ZH** sarvam-m（演示 SFT v1-inf3）

**EN** qwen3-next (80b)

**ZH** qwen3-next（80b）

**EN** grok-4

**ZH** grok-4

**EN** sarvam-m (24b)

**ZH** sarvam-m（24b）

**EN** mistral-large-3

**ZH** mistral-large-3

**EN** gemma-3 (pref-optim v1)

**ZH** gemma-3（偏好优化 v1）

**EN** gemma-3 (pref-optim v2)

**ZH** gemma-3（偏好优化 v2）

**EN** gemma-3 (fewshot)

**ZH** gemma-3（少样本）

**EN** sarvam-m (demo-SFT v2)

**ZH** sarvam-m（演示 SFT v2）

**EN** gemma-3 (fine-tune v2)

**ZH** gemma-3（微调 v2）

**EN** sarvam-m (demo-SFT v1)

**ZH** sarvam-m（演示 SFT v1）

**EN** community-health (3 languages, top 15 of 40 judges)

**ZH** community-health（3 种语言，40 个裁判中的前 15 个）

**EN** bengali

**ZH** 孟加拉语

**EN** hindi

**ZH** 印地语

**EN** kannada

**ZH** 卡纳达语

**EN** malayalam

**ZH** 马拉雅拉姆语

**EN** marathi

**ZH** 马拉地语

**EN** odia

**ZH** 奥里亚语

**EN** tamil

**ZH** 泰米尔语

**EN** telugu

**ZH** 泰卢固语

**EN** grok-4

**ZH** grok-4

**EN** deepseek-r1

**ZH** deepseek-r1

**EN** mistral-large-3

**ZH** mistral-large-3

**EN** gpt-4

**ZH** gpt-4

**EN** llama-3.3 (70b)

**ZH** llama-3.3（70b）

**EN** real-world cultural QA (8 languages, all 5 judges)

**ZH** real-world cultural QA（8 种语言，全部 5 个裁判）

**EN** −0.1

**ZH** −0.1

**EN** 0.0

**ZH** 0.0

**EN** 0.1

**ZH** 0.1

**EN** 0.2

**ZH** 0.2

**EN** 0.3

**ZH** 0.3

**EN** 0.4

**ZH** 0.4

**EN** 0.5

**ZH** 0.5

**EN** mean Pearson r against the mean human

**ZH** 与人类均值的平均 Pearson r

**EN** Figure 14: Per-language agreement, judge by judge. Mean Pearson r between each judge and the mean-humanreference, averaged over that dataset’s rubrics, with rows ordered by judge mean and both panels on one colour scale.community-health (3 languages; the top 15 of its 40 judges, so the rows stay legible) on the left, real-worldcultural QA (8 languages, all 5 judges) on the right. Agreement varies more across languages within a judge thanit does across judges within a language. Per-domain and rubric-kind contrasts are in Fig. 6 and Table 1A.

**ZH** 图 14：逐语言的一致性，逐个裁判。每个裁判与人类均值参考之间的平均 Pearson r，在该数据集的评分维度上取平均，行按裁判均值排序，两栏共用同一色标。左为 community-health（3 种语言；取其 40 个裁判中的前 15 个，以保持行清晰），右为 real-world cultural QA（8 种语言，全部 5 个裁判）。同一裁判跨语言的一致性的差异，大于同一语言内跨裁判的差异。按领域与维度类型的对比见图 6 与表 1A。

**EN** or the rows of the human matrix (stacked; 300permutations) are shuﬄed and the angle recom-puted. We report the null mean and the observedangle’s percentile within the null. On DLQ, all 15judge×rubric observed angles fall below all 500shuﬄes, i.e., p < 1/501 < 0.002 for each test sep-arately (nulls 88.6–88.7◦); the 15 tests share thesame item set, so they are not independent, but theweakest of them already survives a Bonferroni cor-rection across all 15 (0.002×15 < 0.05); the sameholds for all 5 judges on the stacked objective and

**ZH** 或人类矩阵的行（堆叠；300 次置换）被置换后重新计算角度。我们报告零假设均值，以及观测角在零假设分布中的百分位。在 DLQ 上，全部 15 个裁判×维度的观测角都低于全部 500 次置换，即每项检验分别有 p < 1/501 < 0.002（零假设 88.6–88.7°）；这 15 项检验共用同一组条目，因此并不独立，但其中最弱的一项已经通过全部 15 项的 Bonferroni 校正（0.002×15 < 0.05）；五个裁判在堆叠的客观与

**EN** subjective constructions. On CH the cohort mean(88.08◦) sits near the stacked null (88.80◦), thestrongest collapse in the study. Because Benjamini–Hochberg over 40 judges needs p ≤.00125 at rank1, below what 300 shuﬄes can resolve, we rerun theCH judge-level test at 20,000 shuﬄes: 11 judgesare below the null at p < .05 against 2 expectedby chance, 6 survive at q < .05 and 10 at q < .10(Table 19). The ten base judges not below the nullinclude every Indic-focused and open-mid judge.

**ZH** 主观构造上同样如此。在 CH 上，群体均值（88.08°）紧邻堆叠零假设（88.80°），这是本研究报告的最强坍缩。由于对 40 个裁判做 Benjamini–Hochberg 校正要求 p ≤ .00125（第 1 位），低于 300 次置换所能分辨的下限，我们把 CH 的裁判级检验重跑在 20,000 次置换上：11 个裁判在 p < .05 下低于零假设（机遇下期望为 2 个），6 个在 q < .05 下存活、10 个在 q < .10 下存活（表 19）。未低于零假设的十个基座裁判包含了每一个面向印度语系与开放中型的裁判。

**EN** [Page 22]

**ZH** 第 22 页

**EN** RecipeApplied toWhat & key hyper-parameters

**ZH** 配方　应用于　内容与关键超参数

**EN** few-shot (FS)all three familiesup to k =3 demos per (language × rubric), drawn from the held-out human-label pool,shortest-ﬁrst with rating-class round-robin; frozen weights; auto-shrink 3→2→1 underthe token budget; same decoding as base.ﬁne-tune (FT)all three familiesper-rubric LoRA SFT (Hu et al., 2022; Ouyang et al., 2022) on the 5,683-label corpus;LoRA rank 16–64 (α = 2r), target {q, k, v, o, gate, up, down}, AdamW, cosine schedule,bf16, 2–6 epochs with best-checkpoint selection on eval loss (e.g., sarvam-m v2: r=64,α=128, best checkpoint at ≈1.9 epochs).pref-optim (PO)all three familiesDPO (Rafailov et al., 2023) from the base model on the 2,935 strict-preference triples; v1:r=16/α=32, β=0.1, LR 8×10−6, 1 epoch; v2: r=32/α=64, β=0.05, LR 5×10−7, 2epochs.FT + POall three familiesstage-wise: merged FT checkpoint →DPO; dominant weight-updating signal in our repairanalysis.demo-SFT (AT)sarvam-m onlydemonstration-augmented SFT: K human-rated demos baked into every training prompt(self-demo excluded); AT-v1 (K=1), AT-v2 (K=3), AT-v1-inf3 (trained with 1 demo,scored with 3-demo prompts).calibrated (CAL)sarvam-m onlydemonstration-anchored calibration: the frozen best DPO checkpoint scored with Khuman-rated demonstrations in context at inference (CAL-v2: K=2; CAL-v3: K=3); noweight updates and no output-layer rescaling (a pure post-hoc aﬃne rescale is analysedseparately in App. M and does not reproduce the gains).

**ZH** 少样本（FS）　三个系列　每个（语言 × 评分维度）最多 k = 3 条演示样例，取自留出的人类标签池，按长度升序、评分类别轮转抽取；权重冻结；在 token 预算下自动收缩 3→2→1；解码与基座相同。｜微调（FT）　三个系列　在 5,683 条标签语料上做逐维度 LoRA SFT（Hu 等，2022；Ouyang 等，2022）；LoRA 秩 16–64（α = 2r），目标模块 {q, k, v, o, gate, up, down}，AdamW，余弦调度，bf16，2–6 轮，按验证损失选最佳检查点（例如 sarvam-m v2：r = 64，α = 128，最佳检查点在约 1.9 轮）。｜偏好优化（PO）　三个系列　在 2,935 个严格偏好三元组上从基座模型做 DPO（Rafailov 等，2023）；v1：r = 16／α = 32，β = 0.1，学习率 8×10⁻⁶，1 轮；v2：r = 32／α = 64，β = 0.05，学习率 5×10⁻⁷，2 轮。｜FT + PO　三个系列　分阶段：合并后的 FT 检查点 → DPO；我们的修复分析中占主导的权重更新信号。｜演示 SFT（AT）　仅 sarvam-m　演示增强 SFT：把 K 条人类评过的演示样例烘进每个训练提示（排除自身演示）；AT-v1（K = 1）、AT-v2（K = 3）、AT-v1-inf3（用 1 条演示训练，用 3 条演示的提示计分）。｜校准（CAL）　仅 sarvam-m　演示锚定校准：把冻结的最佳 DPO 检查点在推断时上下文中放入 K 条人类评过的演示样例后计分（CAL-v2：K = 2；CAL-v3：K = 3）；不更新权重，也不重标定输出层（纯事后仿射重标定另在附录 M 中分析，且不能复现这些增益）。

**EN** Table 15: Trained judge variant recipes. All variants share the base-judge JSON schema and decoding settings;demonstration pools are anchored to human-rated items disjoint from the evaluation questions.

**ZH** 表 15：训练裁判变体的配方。所有变体共用基座裁判的 JSON 模式与解码设置；演示池锚定在与评测问题不相交的人类评过条目上。

**EN** RegimeRubrics in this studyMeasured behaviour

**ZH** 机制　本研究中的评分维度　实测行为

**EN** small-dR (objective)DLQ task quality (dR ≈2.1)judges’ dominant shared axis is close to the human one (47.7◦);matched per-rubric angle 60.7◦against a 56.4◦ﬂoor, with thebest judge inside it; LLM–human agreement reaches 88% of theH–H band (Sec. 5.2).large-dR (subjective)CH all four (assigned by rubric type;dR is measurable only where multipleraters exist); DLQ LA, HAL (dR ≈2.3–2.5)

**ZH** 小 dR（客观）　DLQ 任务质量（dR ≈ 2.1）　裁判的主导共享轴接近人类的那条（47.7°）；匹配的逐维度角 60.7°，基线为 56.4°，最佳裁判落在基线之内；大模型—人类一致性达到 H–H 带的 88%（第 5.2 节）。

**EN** σ-compression, low eﬀective rank, angles above the inter-humanﬂoor yet below the permutation null, and inter-judge clustering,i.e., the four signatures of Sec. 3, quantitatively conﬁrmed withthe controls of Sec. 5.4.

**ZH** 大 dR（主观）　CH 全部四个（按维度类型指派；dR 只在存在多位评分者处可测）；DLQ 语言可接受性、幻觉（dR ≈ 2.3–2.5）　σ 压缩、有效秩低、角度高于人类间基线却低于置换零假设，以及裁判间聚类，即第 3 节的四项特征，并由第 5.4 节的控制检验定量确认。

**EN** Table 16: Boundary condition: which rubrics fall in which regime and what is measured there. The lens predictswhich rubrics fail, the shape of failure, and where it vanishes; it does not predict which repair technique closes thegap, a dissociation Sec. 5.7 measures.

**ZH** 表 16：边界条件——哪些评分维度落在哪种机制，以及在那里测到了什么。透镜预测哪些维度会失败、失败的形态，以及它在哪里消失；它不预测哪种修复技术能弥合差距，这一分离由第 5.7 节测量。

**EN** Participation ratio.dR (Eq. 1) is computed onthe centered items×raters matrix of the three DLQhumans, per rubric×domain cell; no LLM outputenters it.

**ZH** 参与率。dR（式 1）在三位 DLQ 人类的中心化“条目×评分者”矩阵上、按“评分维度×领域”单元计算；其中不掺入任何大模型输出。

**EN** MRobustness and control tables

**ZH** M 鲁棒性与控制表

**EN** M.1Per-rubric controls

**ZH** M.1 逐维度控制

**EN** Table 17 reports, per dataset and rubric, the Pear-son/Spearman pair, the raw, rank-transformed andremapped angles, and the permutation null.

**ZH** 表 17 按数据集与评分维度报告 Pearson／Spearman 配对、原始、秩变换与重映射后的角度，以及置换零假设。

**EN** M.2Human-reference stability

**ZH** M.2 人类参考的稳定性

**EN** Table 18 varies the human reference constructionand shows the objective-below-subjective orderingnever ﬂips.

**ZH** 表 18 变换人类参考的构造方式，表明“客观低于主观”这一排序从不翻转。

**EN** M.3Judge-level permutation results on CH

**ZH** M.3 CH 上的裁判级置换结果

**EN** M.4Quadratic-weighted κ

**ZH** M.4 二次加权 κ

**EN** Table 20 repeats the headline agreement compari-son under quadratic-weighted κ instead of Pearson.

**ZH** 表 20 用二次加权 κ 代替 Pearson，重做头条的一致性比较。

**EN** M.5Per-language human–human references(DLQ)

**ZH** M.5 逐语言的人类—人类参考（DLQ）

**EN** Table 21 gives the inter-human reference per lan-guage, showing the ﬂoor is measurable in everyone.

**ZH** 表 21 给出逐语言的人类间参考，表明基线在每一种语言中都可测。

**EN** M.6Unrecoverable human variance

**ZH** M.6 不可复原的人类方差

**EN** Cross-validated ridge regression (5-fold, α=1, stan-dardised inputs) reconstructing the mean-humanscore from the full judge cohort:CV R2=0.446 on task quality (55.4% unrecoverable),0.203/0.210 on linguistic acceptability/hallucina-tions (79.7%/79.0% unrecoverable), and ≤0 on allfour CH rubrics (≈100% unrecoverable; n=405,

**ZH** 用交叉验证的岭回归（5 折，α = 1，输入标准化）从整个裁判群体重建人类平均分：任务质量上 CV R² = 0.446（55.4% 不可复原），语言可接受性／幻觉上为 0.203／0.210（79.7%／79.0% 不可复原），CH 全部四个维度上 ≤ 0（约 100% 不可复原；n = 405，

**EN** [Page 23]

**ZH** 第 23 页

**EN** DatasetRubricrρθrawθrankθremapNull<null

**ZH** 数据集　评分维度　r　ρ　θ原始　θ秩变换　θ重映射　零假设　<零假设

**EN** DLQtask quality0.5190.50358.559.658.788.75/5DLQlinguistic acceptability0.2730.28674.073.273.988.75/5DLQhallucinations0.3160.30971.672.071.688.65/5

**ZH** DLQ　任务质量　0.519　0.503　58.5　59.6　58.7　88.7　5/5｜DLQ　语言可接受性　0.273　0.286　74.0　73.2　73.9　88.7　5/5｜DLQ　幻觉　0.316　0.309　71.6　72.0　71.6　88.6　5/5

**EN** CHclarity0.0810.07785.485.6–87.76/28CHhelpfulness0.1030.09384.184.784.487.714/39CHaccuracy0.1120.11383.683.5–87.721/40CHcompleteness0.1210.11883.083.2–87.721/37

**ZH** CH　清晰性　0.081　0.077　85.4　85.6　–　87.7　6/28｜CH　有用性　0.103　0.093　84.1　84.7　84.4　87.7　14/39｜CH　准确性　0.112　0.113　83.6　83.5　–　87.7　21/40｜CH　完整性　0.121　0.118　83.0　83.2　–　87.7　21/37

**EN** Table 17: Ordinal and permutation controls, per rubric. r/ρ = mean |Pearson|/|Spearman| over judges vs.the human reference; θraw/rank/remap = mean angle on raw scores, rank-transformed scores, and after monotonicallyremapping each judge onto the human score marginal; Null = permutation-null mean (500 shuﬄes); <null = judgesbelow the null at p < 0.05 (of judges with ≥50 complete items and non-degenerate variance; “–” = remap undeﬁnedfor degenerate judge marginals). Spearman tracks Pearson to within 0.02 (max gap 0.017, task quality) and the remapmoves angles by ≤0.13◦on DLQ (≤0.31◦on CH), so compression is not conservative scale use. Tabulated anglesare rounded to 0.1◦, while the remap deltas are computed before rounding (task quality: 58.54→58.67, i.e. 0.13◦).Cohorts diﬀer from Table 1A, which reports the 14 CH base judges: the <null column here spans up to all 40 CHjudges, so its CH angles (83.0–85.4, mean 84.0) and r (mean 0.104) diﬀer slightly from the base-only values there(84.4, 0.093). Human ﬂoors quoted here are pairwise (61.7/69.1/68.6◦); the reference-matched ﬂoors used in thebody are 56.4/64.4/63.8◦. The rubric-level pattern is itself a ﬁnding: the CH collapse is strongly rubric-dependent,worst on clarity (6/28 below null) and mildest on accuracy and completeness (21/40, 21/37).

**ZH** 表 17：逐维度的序数与置换控制。r/ρ = 各裁判相对人类参考的平均 |Pearson|／|Spearman|；θ原始／秩变换／重映射 = 在原始分数、秩变换分数，以及把每个裁判单调重映射到人类分数边际分布之后的平均角度；零假设 = 置换零假设均值（500 次置换）；<零假设 = 在 p < 0.05 下低于零假设的裁判数（在完整条目 ≥50 且方差非退化的裁判中统计；“–” = 裁判边际退化时重映射无定义）。Spearman 与 Pearson 相差在 0.02 之内（最大差距 0.017，任务质量），重映射使角度变化 ≤0.13°（DLQ）／≤0.31°（CH），因此压缩并不是保守地使用量表。表内角度四舍五入到 0.1°，而重映射的增量在舍入之前计算（任务质量：58.54→58.67，即 0.13°）。这里的群体与表 1A 不同，后者报告的是 14 个 CH 基座裁判：此处的 <零假设 列最多覆盖全部 40 个 CH 裁判，故其 CH 角度（83.0–85.4，均值 84.0）与 r（均值 0.104）与那里仅基座的值（84.4、0.093）略有差异。此处引用的人类基线是成对的（61.7／69.1／68.6°），正文所用的参考匹配基线是 56.4／64.4／63.8°。维度层面的模式本身就是一项发现：CH 的坍缩强烈依赖于维度，在清晰性上最严重（6/28 低于零假设），在准确性与完整性上最轻（21/40、21/37）。

**EN** Reference constructionObjective θSubjective θ

**ZH** 参考构造　客观 θ　主观 θ

**EN** 3-human mean58.572.8single h165.877.1single h266.578.2single h363.276.0leave-out h160.274.0leave-out h260.273.7leave-out h361.775.0

**ZH** 三人均值　58.5　72.8｜单个 h1　65.8　77.1｜单个 h2　66.5　78.2｜单个 h3　63.2　76.0｜留出 h1　60.2　74.0｜留出 h2　60.2　73.7｜留出 h3　61.7　75.0

**EN** Table 18:Human-reference stability (DLQ, per-rubric angles). Across all seven constructions the objec-tive angle stays ≤66.5◦and the subjective mean stays≥72.8◦: the objective-below-subjective ordering neverﬂips. The stacked 3-rubric analogue varies by only 1.83◦

**ZH** 表 18：人类参考的稳定性（DLQ，逐维度角度）。在所有七种构造下，客观角都保持在 ≤66.5°，主观均值都保持在 ≥72.8°：“客观低于主观”的排序从不翻转。三维度堆叠的对应量在各构造之间只变化 1.83°，

**EN** across constructions.

**ZH** 变化幅度很小。

**EN** 14 base judges). This measured magnitude is re-ported in place of any all-or-nothing “null-space”claim.

**ZH** 14 个基座裁判）。这一实测的量级被用来代替任何非此即彼的“零空间”论断。

**EN** M.7The dR regression: cells, stability, andentanglement

**ZH** M.7 dR 回归：单元、稳定性与纠缠

**EN** Across the nine cells (Fig. 15): Spearman ρ =0.68 (p = 0.042; one-sided label-permutationp = 0.0231 over 20,000 permutations), Pearsonr = 0.91, R2 = 0.83. Leave-one-cell-out: ρ ∈[0.55, 0.90], R2 ∈[0.78, 0.94]: no single cell car-ries the result.

**ZH** 在九个单元上（图 15）：Spearman ρ = 0.68（p = 0.042；单侧标签置换 p = 0.0231，20,000 次置换），Pearson r = 0.91，R² = 0.83。留一单元：ρ ∈ [0.55, 0.90]，R² ∈ [0.78, 0.94]：没有任何单个单元扛着这个结果。

**EN** The relation is between-regime, not graded.Pearson (0.91) far exceeding Spearman (0.68) isthe tell, and the within-group statistics conﬁrm it:across the six subjective cells alone ρ = −0.03,and the three objective cells show no usable trend(n=3). What the regression detects is the separation

**ZH** 这一关系是机制之间的，而非机制内部的分级。Pearson（0.91）远高于 Spearman（0.68）就是线索，组内统计也确认了这一点：仅在六个主观单元上 ρ = −0.03，三个客观单元则没有可用趋势（n = 3）。回归检测到的是客观簇（dR ≈ 2.1、θ ≈ 60°）与主观簇（dR ≈ 2.4、θ ≈ 74°）之间的分离，

**EN** between an objective cluster (dR ≈2.1, θ ≈60◦)and a subjective one (dR ≈2.4, θ≈74◦), not a dose–response curve inside either. We therefore reportdR as a regime separator and quote no degrees-per-dimension slope: ﬁtting one over a dR range of2.10–2.52, four tenths of a single dimension, invitesan extrapolation the data cannot support.

**ZH** 而不是任一簇内部的剂量—反应曲线。因此我们把 dR 报告为机制分离器，并不给出“每维度多少度”的斜率：在 dR 仅 2.10–2.52、即不到半个维度的范围内拟合斜率，会招致数据无法支持的外推。

**EN** The measure is capped by the panel size.With three raters the participation ratio of an

**ZH** 该度量受评分小组规模封顶。在三位评分者下，“条目×评分者”矩阵的参与率不可能超过 3，因此 dR 度量的是三位评分者所能表达的分歧维度数，

**EN** items×raters matrix cannot exceed 3, so dR mea-sures the dimensionality of rater disagreement asthree raters can express it, not the intrinsic dimen-sionality of the human quality manifold. A largerpanel would be needed for the latter, and wouldlikely shift the absolute values; what a three-raterpanel does support is the ordering, and that is allwe use.

**ZH** 而不是人类质量流形的内在维度。后者需要更大的评分小组，而且很可能改变绝对值；三位评分者的小组所能支持的是排序，而我们也只用到这一点。

**EN** Entanglement caveat. At n=9 cells, dR, inter-rater agreement, and label entropy are tightly cou-pled facets of human disagreement; agreement andentropy each predict the angle about as strongly(ρ = −0.78, −0.80), and rank-based partial corre-lations show the dR signal does not survive con-ditioning on rater agreement (partial ρ = −0.46)and shrinks under conditioning on entropy (partialρ = 0.12). The supported claim is therefore pre-dictive, not causal, and coarse rather than ﬁne: aquantity computable from human raters alone, be-fore any LLM is run, tells you which regime a rubricis in. Alternative readings (label noise, item ambi-guity, pretraining familiarity, prompt compatibility)

**ZH** 纠缠性提醒。在 n = 9 个单元时，dR、评分者间一致性与标签熵是人类分歧紧密耦合的几个侧面；一致性与熵各自对角度的预测强度相当（ρ = −0.78、−0.80），而基于秩的偏相关显示 dR 的信号在条件化于评分者一致性后不再存活（偏 ρ = −0.46），在条件化于熵后则收缩（偏 ρ = 0.12）。因此被支持的断言是预测性的而非因果性的，而且粗略而非精细：一个仅由人类评分者、在任何大模型运行之前就能算出的量，可以告诉你某个评分维度处在哪种机制。其他解释（标签噪声、条目歧义、预训练熟悉度、提示兼容性）

**EN** [Page 24]

**ZH** 第 24 页

**EN** Below nullθpqBHNot below nullθ

**ZH** 低于零假设　θ　p　qBH　不低于零假设　θ

**EN** sarvam-m (FT v1)85.1.0013.025sarvam-m (base)89.5gemma-3 (FT v2)85.3.0018.025gemma-3 (base)89.3sarvam-m (FT+PO v2)85.3.0022.025aya-expanse (base)89.3gpt-5.586.0.0025.025krutrim-289.6llama-3.3 (70b)85.1.0070.047grok-489.9gpt-4o85.0.0071.047deepseek-r189.2sarvam-m (FT v2)86.1.0090.051qwen3-235b89.3gemma-3 (FT+PO v2)86.4.0155.078qwen3-next (80b)89.6sarvam-m (CAL v3)87.0.0193.081llama-4-scout89.7mistral-large-286.3.0203.081mistral-large-388.7sarvam-m (FT+PO v1)86.8.0288.105

**ZH** 低于零假设：sarvam-m（FT v1）85.1°　p = .0013　qBH = .025；不低于零假设：sarvam-m（基座）89.5°｜低于零假设：gemma-3（FT v2）85.3°　p = .0018　qBH = .025；不低于零假设：gemma-3（基座）89.3°｜低于零假设：sarvam-m（FT+PO v2）85.3°　p = .0022　qBH = .025；不低于零假设：aya-expanse（基座）89.3°｜低于零假设：gpt-5.5　86.0°　p = .0025　qBH = .025；不低于零假设：krutrim-2　89.6°｜低于零假设：llama-3.3（70b）85.1°　p = .0070　qBH = .047；不低于零假设：grok-4　89.9°｜低于零假设：gpt-4o　85.0°　p = .0071　qBH = .047；不低于零假设：deepseek-r1　89.2°｜低于零假设：sarvam-m（FT v2）86.1°　p = .0090　qBH = .051；不低于零假设：qwen3-235b　89.3°｜低于零假设：gemma-3（FT+PO v2）86.4°　p = .0155　qBH = .078；不低于零假设：qwen3-next（80b）89.6°｜低于零假设：sarvam-m（CAL v3）87.0°　p = .0193　qBH = .081；不低于零假设：llama-4-scout　89.7°｜低于零假设：mistral-large-2　86.3°　p = .0203　qBH = .081；不低于零假设：mistral-large-3　88.7°｜低于零假设：sarvam-m（FT+PO v1）86.8°　p = .0288　qBH = .105

**EN** Table 19: CH stacked angles vs. a 20,000-shuffle permutation null, per judge (null mean 88.8◦). Exact p withBenjamini–Hochberg (Benjamini and Hochberg, 1995) q across all 40 tests; bold q survives q < .05. 11 judges arebelow at p < .05 (2 expected by chance), 6 at q < .05 and 10 at q < .10. The published 300-shuﬄe version couldnot attain q < .05 for any judge, since its smallest possible p (1/301) exceeds the rank-1 BH threshold .05/40; thattest was resolution-limited, not evidence-limited, which is why we rerun it here. The right column lists the ten basejudges not below the null; 19 trained variants are also not below and are omitted for space (full table in the release).These are paired tests of each judge against chance, not against each other: see the resolution caveat in Sec. 5.4.

**ZH** 表 19：CH 上各裁判的堆叠角对 20,000 次置换零假设的比较（零假设均值 88.8°）。精确 p 值配 Benjamini–Hochberg（Benjamini 与 Hochberg，1995）在全部 40 项检验上的 q；加粗的 q 表示存活于 q < .05。11 个裁判在 p < .05 下低于零假设（机遇下期望为 2 个），6 个在 q < .05 下存活、10 个在 q < .10 下存活。已发表的 300 次置换版本无法让任何裁判达到 q < .05，因为它可能的最小 p（1/301）超过了第 1 位的 BH 阈值 .05/40；那次检验是分辨率受限，而不是证据受限，这正是我们在这里重跑的原因。右列列出未低于零假设的十个基座裁判；另有 19 个训练变体也未被列入，因篇幅省略（完整表格在发布物中）。这些都是每个裁判各自对机遇的配对检验，不是彼此互比：见第 5.4 节的分辨率提醒。

**EN** 2.12.22.32.42.5dR (participation ratio, human raters only)

**ZH** 2.1 2.2 2.3 2.4 2.5　dR（参与率，仅人类评分者）

**EN** 55

**ZH** 55

**EN** 60

**ZH** 60

**EN** 65

**ZH** 65

**EN** 70

**ZH** 70

**EN** 75

**ZH** 75

**EN** 80

**ZH** 80

**EN** LLM–human angle ( ∘)

**ZH** 大模型—人类夹角（°）

**EN** task quality

**ZH** 任务质量

**EN** ling. accept.

**ZH** 语言可接受性

**EN** halluc.

**ZH** 幻觉

**EN** leave-one-cell-out fitsOLS fitobjectivesubjective

**ZH** 留一单元拟合、OLS 拟合、客观、主观

**EN** Figure 15: The dR boundary predictor over the nine DLQ rubric×domain cells of Table 22. dR (Eq. 1) is computedfrom the three human raters alone, before any LLM output is used; the angle is the mean over the ﬁve base judges.The band collects the nine leave-one-cell-out ﬁts, showing that no single cell carries the slope. Objective cellsoccupy the low-dR, low-angle corner and subjective cells the high-dR, high-angle one.

**ZH** 图 15：表 22 中九个 DLQ“评分维度×领域”单元上的 dR 边界预测量。dR（式 1）仅由三位人类评分者算出，在使用任何大模型输出之前；角度是五个基座裁判的均值。色带汇集了九条留一单元拟合的线，表明没有任何单个单元扛着这条斜率。客观单元占据低 dR、低角度的角落，主观单元则占据高 dR、高角度的角落。

**EN** DatasetRubricQWKLHQWKHH

**ZH** 数据集　评分维度　二次加权 κ（大模型—人类）　二次加权 κ（人类—人类）

**EN** DLQtask quality0.3390.464DLQlinguistic acceptability0.1850.355DLQhallucinations0.1970.350CHclarity0.030–CHhelpfulness0.048–CHaccuracy0.062–CHcompleteness0.071–

**ZH** DLQ　任务质量　0.339　0.464｜DLQ　语言可接受性　0.185　0.355｜DLQ　幻觉　0.197　0.350｜CH　清晰性　0.030　–｜CH　有用性　0.048　–｜CH　准确性　0.062　–｜CH　完整性　0.071　–

**EN** Table 20: Quadratic-weighted κ (mean over judge–human pairs; human–human where three raters exist).The ordinal-agreement view reproduces the Pearson pat-tern of Table 1A: near-human on task quality, clearlysub-human on subjective rubrics, near zero on CH.

**ZH** 表 20：二次加权 κ（裁判—人类配对上的均值；存在三位评分者处为人类—人类）。序数一致性的视角复现了表 1A 中 Pearson 的模式：在任务质量上接近人类，在主观维度上明显低于人类，在 CH 上接近于零。

**EN** remain compatible with the data (see Limitations).

**ZH** 都与数据相容（见“局限性”）。

**EN** LanguageTQ θhh / rhhLA θhh / rhhHAL θhh / rhh

**ZH** 语言　任务质量 θhh / rhh　语言可接受性 θhh / rhh　幻觉 θhh / rhh

**EN** bengali64.1 / 0.4463.2 / 0.4569.3 / 0.35hindi58.7 / 0.5260.0 / 0.5063.4 / 0.45kannada61.4 / 0.4779.3 / 0.1968.4 / 0.37malayalam62.1 / 0.4765.6 / 0.4157.9 / 0.53marathi51.8 / 0.6173.9 / 0.2859.4 / 0.51odia78.1 / 0.2068.8 / 0.3675.7 / 0.25tamil58.6 / 0.5265.2 / 0.4278.3 / 0.20telugu59.7 / 0.5071.4 / 0.3273.3 / 0.29

**ZH** 孟加拉语　64.1 / 0.44　63.2 / 0.45　69.3 / 0.35｜印地语　58.7 / 0.52　60.0 / 0.50　63.4 / 0.45｜卡纳达语　61.4 / 0.47　79.3 / 0.19　68.4 / 0.37｜马拉雅拉姆语　62.1 / 0.47　65.6 / 0.41　57.9 / 0.53｜马拉地语　51.8 / 0.61　73.9 / 0.28　59.4 / 0.51｜奥里亚语　78.1 / 0.20　68.8 / 0.36　75.7 / 0.25｜泰米尔语　58.6 / 0.52　65.2 / 0.42　78.3 / 0.20｜泰卢固语　59.7 / 0.50　71.4 / 0.32　73.3 / 0.29

**EN** Table 21: Per-language inter-human references (meanpairwise angle◦/ Pearson over the three rater pairs; itemcounts per language in Table 8). Per-cell human–humanreferences are noisy at small n (e.g., Odia, n=60), whichis why per-language claims in Sec. 5.5 are read againstthese cell-level references rather than one global ﬂoor.

**ZH** 表 21：逐语言的人类间参考（三对评分者上的平均成对角度°／Pearson；各语言的条目数见表 8）。逐单元的人类—人类参考在小 n 下噪声较大（例如奥里亚语，n = 60），这正是第 5.5 节的逐语言断言对着这些单元级参考、而不是对着一个全局基线来读的原因。

**EN** [Page 25]

**ZH** 第 25 页

**EN** RubricDomainndRθrhhH(labels)

**ZH** 评分维度　领域　n　dR　θ　rhh　H（标签熵）

**EN** task qualityhealth2842.09959.250.4531.38task qualityﬁnance3232.12058.310.4531.39task qualityeveryday5752.13561.260.4471.56ling. accept.health2842.30470.650.3841.14ling. accept.ﬁnance3232.30075.990.3761.03ling. accept.everyday5752.43374.490.3311.06hallucinationshealth2842.41475.960.3310.90hallucinationsﬁnance3232.51675.070.2990.88hallucinationseveryday5752.34571.290.3680.97

**ZH** 任务质量　健康养生　284　2.099　59.25　0.453　1.38｜任务质量　金融　323　2.120　58.31　0.453　1.39｜任务质量　日常生活　575　2.135　61.26　0.447　1.56｜语言可接受性　健康养生　284　2.304　70.65　0.384　1.14｜语言可接受性　金融　323　2.300　75.99　0.376　1.03｜语言可接受性　日常生活　575　2.433　74.49　0.331　1.06｜幻觉　健康养生　284　2.414　75.96　0.331　0.90｜幻觉　金融　323　2.516　75.07　0.299　0.88｜幻觉　日常生活　575　2.345　71.29　0.368　0.97

**EN** Table 22: The nine DLQ rubric×domain cells behind the dR regression: participation ratio dR (from the threehuman raters alone), mean LLM–human angle θ, mean inter-rater Pearson rhh, and mean human label entropy H(bits). θ here is measured against the three-rater mean reference, so these values run below the reference-matchedangles quoted in the body (Table 4). dR and θ are given to three and two decimals respectively because the within-subjective-group correlation (ρ = −0.03) is not recoverable from coarser rounding: two cells tie at dR =2.30 andtwo at θ=76.0, which alone would ﬂip the sign.

**ZH** 表 22：dR 回归背后的九个 DLQ“评分维度×领域”单元：参与率 dR（仅由三位人类评分者算出）、平均大模型—人类夹角 θ、平均评分者间 Pearson rhh、平均人类标签熵 H（比特）。这里的 θ 是对三评分者均值参考测量的，故其数值低于正文中引用的参考匹配角（表 4）。dR 与 θ 分别给到三位与两位小数，因为主观组内部的相关（ρ = −0.03）无法从更粗的舍入中复原：有两个单元在 dR = 2.30 处并列、有两个在 θ = 76.0 处并列，仅这一点就足以翻转符号。

**EN** M.8Self-preference by answer generator(CH)

**ZH** M.8 按答案生成器的自我偏好（CH）

**EN** CH answers come from three generators (llama-3.1-405b, qwen3, sarvam-m), and two of those fam-ilies also serve as judges; sarvam-m supplies thecalibrated judge behind the training headline. Ifjudges favoured their own family’s answers, thatalone could produce the result.

**ZH** CH 的答案来自三个生成器（llama-3.1-405b、qwen3、sarvam-m），其中两个系列同时也担任裁判；而 sarvam-m 提供了训练头条数字背后的那个校准裁判。若裁判偏袒自己系列的答案，单凭这一点就可能造出那个结果。

**EN** Within each (language, question) triple all threegenerators answer the same question, so we stan-dardise each rater’s scores per rubric over the 405core items, take each judge’s deviation from its owntriple mean, subtract the human’s deviation on thesame triple (removing item diﬃculty and any realquality diﬀerence between generators), and thensubtract the mean eﬀect of all judges outside thatfamily (removing anything about the generator thatthe whole cohort sees). The residual is the family-speciﬁc preference. Against a permutation null thatreassigns the same number of judges to each gen-erator (20,000 draws), no family shows an eﬀect:sarvam-m +0.028 SD (p = 0.58), qwen3 −0.035SD (p = 0.71), llama −0.008 SD (p = 0.95). Self-preference is not a plausible explanation for anyresult here.

**ZH** 在每个（语言、问题）三元组内部，三个生成器回答同一个问题，因此我们把每个评分者在 405 条核心条目上的逐维度分数标准化，取每个裁判相对其自身三元组均值的偏差，减去人类在同一三元组上的偏差（消掉条目难度与各生成器之间真实的质量差异），再减去该系列以外所有裁判的平均效应（消掉整个群体都能看到的、关于该生成器的任何东西）。剩下的残差就是特定于系列的偏好。对着一个把同样多的裁判重新指派给各生成器的置换零假设（20,000 次抽样），没有任何系列表现出效应：sarvam-m +0.028 SD（p = 0.58）、qwen3 −0.035 SD（p = 0.71）、llama −0.008 SD（p = 0.95）。自我偏好不足以解释本文的任何结果。

**EN** M.9Split-half reliability of angles

**ZH** M.9 角度的分半可靠性

**EN** Random item halves (200 draws): per-rubric DLQangles agree across halves to a mean |∆θ| of2.3–2.5◦, and the ordering of judges by angle is pre-served across halves (mean cross-half correlation0.96/0.97/0.74 on task quality/linguistic acceptabil-ity/hallucinations). On CH the mean cross-half|∆θ| is 2.2◦and the cross-half ordering of the 40judges is uninformative (r ≈0), because the cohort

**ZH** 随机条目半区（200 次抽样）：逐维度的 DLQ 角度在两半之间的平均 |∆θ| 为 2.3–2.5°，且裁判按角度的排序在两半之间得以保持（任务质量／语言可接受性／幻觉上的跨半区平均相关为 0.96／0.97／0.74）。在 CH 上，跨半区的平均 |∆θ| 为 2.2°，而 40 个裁判的跨半区排序不具信息量（r ≈ 0），因为整个群体

**EN** is uniformly collapsed into an 85–90◦band: thebetween-judge SD is 1.6◦while a per-judge boot-strap interval is 6.3◦wide. The coarser below-nullbinary does not rescue this at half size either: re-peating the full permutation test inside each half(30 draws, 300 shuﬄes per half) recovers about 6below-null judges per half but the two halves agreeon which ones at κ = 0.02. The full-item test doeshave power (6 judges survive FDR at q < .05 on all405 items), so this is a budget statement: resolvingindividual judges in a collapsed regime needs thefull item set, not half of it. The study accordinglymakes no CH claim that depends on angle ordering;CH judge comparisons use stacked Pearson, whoseleaderboard is bootstrap-stable (Sec. 5.7).

**ZH** 被均匀地压进 85–90° 的带里：裁判之间的标准差是 1.6°，而逐裁判的自助区间宽 6.3°。更粗的“低于零假设”二值在半量级下也救不了这一点：在每个半区内重跑完整的置换检验（30 次抽样，每半区 300 次置换），每半区能找回约 6 个低于零假设的裁判，但两半区在“是哪些”上只有 κ = 0.02 的一致性。全条目检验确实有效力（在全部 405 条上有 6 个裁判存活于 FDR 的 q < .05），所以这是一条预算陈述：在坍缩机制中分辨单个裁判需要完整的条目集，而不是一半。本研究因此不提出任何依赖角度排序的 CH 断言；CH 的裁判比较改用堆叠 Pearson，其排行榜在自助法下是稳定的（第 5.7 节）。

**EN** M.10Ensembling: how far can averaging go?

**ZH** M.10 集成：平均究竟能走多远？

**EN** An ensemble mean must be read against a humanreference built the same way. Scoring a k-judgemean against the three-rater human mean whilescoring a human against a single colleague com-pares an averaged quantity with an unaveraged one,and on that mismatched pairing the ﬁve-judge en-semble appears to sit below the human ﬂoor on allthree rubrics, which would say that ﬁve LLMs ap-proximate the human consensus better than one hu-man does. On the matched construction, where theheld-out human and the ensemble are both scoredagainst the same two-rater mean, the picture re-verses on exactly the rubrics the paper’s thesis con-cerns; Table 3 gives the curve.

**ZH** 集成均值必须对着以同样方式构建的人类参考来读。把一个 k 裁判均值对着三评分者人类均值计分，同时让一位人类对着一位同事计分，等于拿一个被平均过的量去比一个未被平均的量；在这种不匹配的配对下，五裁判集成在三个维度上看起来都低于人类基线，这就等于说五个大模型比一位人类更接近人类共识。而在匹配的构造下——被留出的人类与集成都对着同一个两位评分者均值计分——画面恰好在本文论点所关切的那些维度上反转；表 3 给出了这条曲线。

**EN** Two readings follow. First, ensembling is gen-uinely useful: it buys 7.6–9.5◦between one judgeand ﬁve. Second, what it buys is variance reductiontoward the cohort’s dominant axis, not a new direc-

**ZH** 由此有两种读法。第一，集成确实有用：它在一个裁判与五个裁判之间买到 7.6–9.5°。第二，它买到的是朝群体主导轴的方差缩减，

**EN** [Page 26]

**ZH** 第 26 页

**EN** tion: the k=5 angles land within ∼3.5◦of the co-hort PC1-to-human angles (47.7/64.3/65.5◦), andthe extrapolated limits (66.5◦, 64.6◦) remain out-side the subjective ﬂoors (64.4◦, 63.8◦). Where theshared axis misses the human axis, averaging morejudges from the same cohort converges to the miss.On CH the ensemble reaches 77.6–80.9◦, far out-side anything the single merged reference can becompared against.

**ZH** 而不是一个新的方向：k = 5 的角度落在群体第一主成分到人类角度（47.7／64.3／65.5°）的约 3.5° 之内，而外推的极限（66.5°、64.6°）仍处在主观基线（64.4°、63.8°）之外。共享轴偏离人类轴之处，从同一群体中平均更多裁判只会收敛到那个偏离上。在 CH 上集成达到 77.6–80.9°，远在单一合并参考所能比较的任何东西之外。

**EN** We ﬂag one asymmetry that runs against us andis worth stating: even in the matched constructionthe ensemble averages ﬁve judges while the humanside is a single rater. The subjective-rubric conclu-sion therefore holds despite giving the ensemble theadvantage, and the objective-rubric crossing is cor-respondingly easier to achieve than the table makesit look.

**ZH** 我们指出一个对我们不利、但值得说明的不对称：即便在匹配构造下，集成也平均了五个裁判，而人类一侧只有一位评分者。因此主观维度的结论是在让集成占便宜的情况下依然成立的，而客观维度上的跨越也比表中看起来更容易实现。

**EN** M.11Post-hoc rescaling vs. demonstrationanchoring

**ZH** M.11 事后重标定与演示锚定

**EN** Classic post-hoc calibration rescales scores againstlabelled anchors (Platt, 1999; Guo et al., 2017);we test whether such rescaling explains thedemonstration-anchored gains. The curve is inthe body (Fig. 11) and the per-anchor values inTable 23.Fits are per-rubric aﬃne maps esti-mated on n human-anchored items and evaluated onthe held-out remainder, over 500 resamples (seed20260828); at n=5 the gemma-3 ﬁts are degener-ate and are omitted. Below roughly 40 anchors the95% interval spans zero, so rescaling on a small an-chor set is not merely weak but unreliable, whereasthe demonstration-anchored judge uses the samehuman-rated items at inference and reaches 0.184.

**ZH** 经典的事后校准把分数对着有标签的锚点重标定（Platt，1999；Guo 等，2017）；我们检验这种重标定能否解释演示锚定的增益。曲线在正文（图 11），逐锚点数值见表 23。拟合是在 n 条人类锚定条目上估计逐维度仿射映射、并在留出的其余条目上评估，共 500 次重抽样（种子 20260828）；n = 5 时 gemma-3 的拟合退化，故略去。在约 40 个锚点以下，95% 区间跨越零点，因此小锚点集上的重标定不只是弱，而是不可靠；而演示锚定的裁判在推断时使用同样的人类评过条目，并达到 0.184。

**EN** M.12The excluded DLQ comparative split

**ZH** M.12 被排除的 DLQ 对比切分

**EN** The DLQ comparative split (21,610 pairs, 10 lan-guages) has exactly one LLM judge (gpt-4, fromthe source benchmark). Its labels are strongly anti-correlated with all three humans (κ = −0.193/ −0.197/ −0.187) while the humans agree with eachother (κ = 0.542/0.525/0.544), a pattern con-sistent with an A/B label-orientation artefact inthe inherited judgements rather than genuine anti-alignment. With a single judge and a suspect ori-entation, the split cannot support any LL-vs-LHcomparison, so it is excluded from analysis andcounted only in event totals.

**ZH** DLQ 的对比切分（21,610 对，10 种语言）只有一个大模型裁判（gpt-4，来自源基准）。它的标签与三位人类都强反相关（κ = −0.193／−0.197／−0.187），而人类彼此一致（κ = 0.542／0.525／0.544），这一模式提示继承来的判断中存在 A/B 标签方向性假象，而不是真正的反向对齐。只有一个裁判、且方向可疑，该切分无法支撑任何 LL 对 LH 的比较，因此被排除在分析之外，只计入事件总量。

**EN** NReconciling per-rubric and stackedangles

**ZH** N 调和逐维度与堆叠角度

**EN** The paper uses four angle constructions, which sitat systematically diﬀerent magnitudes for the samecohort. Two axes vary independently: what is com-pared (one rubric vector, a whole subspace, or thecohort’s dominant axis) and against which refer-ence (a single rater, a two-rater mean, or a three-rater mean). Body claims ﬁx both. Table 4 gives thefour constructions side by side; the per-constructionreading of “what it measures” is as follows. The per-rubric matched construction isolates one rubric’sscore direction with judge and held-out human onthe same target. The three-rater-mean variant is thesame comparison, except the judge gets a less noisytarget than any individual human does. The per-judge stacked statistic reports the worst-matcheddirection pair between the two 95%-energy sub-spaces; the cohort stacked variant does the samefor the judges pooled into one subspace rather thanany single judge. The cohort PCA axis reports thealignment of the judges’ best shared direction. Hu-man counterparts exist only on DLQ, which hasthree raters; CH merges its annotators into a singlereference, so no ﬂoor is measurable there and CHnumbers are never compared with one.

**ZH** 本文使用四种角度构造，对同一个群体而言它们处在系统性不同的量级上。两个轴各自独立地变化：被比较的是什么（一个维度的向量、整个子空间，还是群体的主导轴），以及所对照的参考是什么（一位评分者、两位评分者均值，还是三位评分者均值）。正文的断言把两者都固定下来。表 4 并排给出四种构造；逐构造的“它测量什么”的读法如下。逐维度匹配构造把单个维度的分数方向孤立出来，裁判与被留出的人类对着同一个靶子。三评分者均值变体是同一个比较，只是裁判得到一个比任何单个都不那么嘈杂的靶子。逐裁判堆叠统计量报告两个 95% 能量子空间之间匹配最差的那对方向；群体堆叠变体对把裁判汇成一个子空间（而非任一单个裁判）后做同样的事。群体 PCA 轴报告裁判最好的共享方向的对齐程度。人类的对应量只在 DLQ 上存在，那里有三位评分者；CH 把标注者合并进一个参考，因此那里测不出基线，CH 的数字从不与基线比较。

**EN** The orderings are forced, not accidental: thestacked statistic is the largest principal angle, i.e.,the worst-aligned pair of directions once each side’s95%-energy basis is taken, so it upper-bounds thepicture; the cohort-PCA angle takes the judges’ sin-gle dominant axis, the best-case direction, so itlower-bounds it; per-rubric angles sit in betweenbecause each rubric mixes the judge’s aligned dom-inant component with its misaligned remainder.Concretely, on DLQ task quality the judges’ bestshared direction is well aligned (47.7◦), each rubricvector moderately so (60.7◦), while the full sub-spaces still contain directions nearly orthogonal tothe human ones (84.3–88.9◦stacked), as do the hu-mans’ own (73.9–78.1◦): high stacked angles alonedo not distinguish judges from humans, which iswhy every headline contrast is drawn within oneconstruction against its own matched human refer-ence or permutation null.

**ZH** 这些排序是被强制出来的，而非偶然：堆叠统计量是最大主角度，即在取定双方 95% 能量基之后匹配最差的那对方向，因此它给出图像的上界；群体 PCA 角取裁判的单一主导轴，即最好的方向，因此给出下界；逐维度角度居于其间，因为每个维度都把裁判已对齐的主导分量与其未对齐的余部混合在一起。具体地说，在 DLQ 任务质量上，裁判最好的共享方向对齐良好（47.7°），每个维度向量对齐中等（60.7°），而完整子空间仍含有与人类近乎正交的方向（堆叠 84.3–88.9°），人类自己的子空间也是如此（73.9–78.1°）：单看高的堆叠角并不能把裁判与人类区分开，这正是每一处头条对比都在同一构造内部、对着其自身匹配的人类参考或置换零假设作出的原因。

**EN** The reference axis matters as much as the con-struction. On task quality the same ﬁve judges score0.519 against the three-rater mean but 0.418 againsta single rater; the inter-human value is 0.474. Read-ing the ﬁrst against the third puts judges above thehuman ﬂoor; reading like against like puts them

**ZH** 参考轴与构造同样重要。在任务质量上，同样的五个裁判对三评分者均值得 0.519，对单个评分者只得 0.418；人类间的值为 0.474。拿前者对后者读，会把裁判放到人类基线之上；同类对同类地读，则把它们放到

**EN** [Page 27]

**ZH** 第 27 页

**EN** FT+PO judgen=510204080160uncal.

**ZH** FT+PO 裁判　n=5　10　20　40　80　160　未校准

**EN** sarvam-m0.0440.0630.0860.1120.1310.1440.136gemma-3–0.0660.0860.1090.1320.1500.154

**ZH** sarvam-m　0.044　0.063　0.086　0.112　0.131　0.144　0.136｜gemma-3　–　0.066　0.086　0.109　0.132　0.150　0.154

**EN** Table 23: Post-hoc rescaling vs. anchor count. Held-out stacked Pearson r for the values plotted in Fig. 11;rescaling never reaches CAL (0.184) and hurts below ∼40–80 anchors.

**ZH** 表 23：事后重标定对锚点数量。图 11 所画各值的留出集堆叠 Pearson r；重标定永远达不到 CAL（0.184），且在约 40–80 个锚点以下反而有害。

**EN** 12% below it. Every comparison in the body usesthe matched pairing, and this is the single changethat most aﬀects the paper’s numbers relative to thesubmitted version.

**ZH** 低 12%。正文的每一次比较都使用匹配配对，而这是相对投稿版本而言对本文数字影响最大的那一项改动。

**EN** OReproducibility and artifact index

**ZH** O 可复现性与产物索引

**EN** Release.We release, in our public artifactrepository: (i) the two consolidated score CSVs (all170, 890 LLM-judge calls, raw model outputs asJSONL, and all human labels used); (ii) the exactjudge prompts (App. I); (iii) every metric, ﬁgure,and table generator (framing_analysis.py,extended_analysis.py,stage_progression_extended.py,analysis_plots/build_artifacts.py);(iv)thecontrolanalysesasonerunnablescripteach(run_rebuttal_perrubric.py,run_rebuttal_robustness.py,run_rebuttal_theory_tests.py);and(v) camera_ready/build_numbers.py, whichregenerates every roster count, event total, andcontrol statistic in this paper and emits themas the LaTeX macros used in the text, pluscamera_ready/build_control_figs.pyforthe two control ﬁgures, so each printed numberand control plot is reproducible by one command.Analysis code is released under the MIT license;judge outputs and annotations under CC BY 4.0,subject to the source benchmarks’ terms (Hamnaet al., 2026; Watts et al., 2024).

**ZH** 发布物。我们在公开产物仓库中发布：(i) 两份合并后的分数 CSV（全部 170,890 次大模型裁判调用、JSONL 形式的原始模型输出，以及所使用的全部人类标签）；(ii) 精确的裁判提示（附录 I）；(iii) 每一个指标、图与表的生成器（framing_analysis.py、extended_analysis.py、stage_progression_extended.py、analysis_plots/build_artifacts.py）；(iv) 每个控制分析各一个可运行脚本（run_rebuttal_perrubric.py、run_rebuttal_robustness.py、run_rebuttal_theory_tests.py）；以及 (v) camera_ready/build_numbers.py，它重新生成本文的每一份名单计数、事件总量与控制统计量，并以正文中所用的 LaTeX 宏输出，另有 camera_ready/build_control_figs.py 生成两张控制图，因此每一个印出来的数字与每一张控制图都能由一条命令复现。分析代码以 MIT 许可发布；裁判输出与标注以 CC BY 4.0 发布，并服从源基准的条款（Hamna 等，2026；Watts 等，2024）。

**EN** API judge versions and call dates.Table 24 pinsevery hosted judge to a deployment string and a calldate, so the closed-model results can be situatedeven after those endpoints change.

**ZH** API 裁判版本与调用日期。表 24 把每一个托管裁判钉到一个部署字符串与一个调用日期，因此即使那些端点日后改变，闭源模型的结果也能被定位。

**EN** Reproducibility checklist.Table 25 maps eachclaim class to the script and seed that regeneratesit.

**ZH** 可复现性清单。表 25 把每一类断言映射到重新生成它的脚本与种子。

**EN** Seeds and determinism.Training seed 42; item-bootstrap seed 20260525 (B=1000); permutationseeds 20260710 (500 per-rubric / 300 stacked shuf-ﬂes); camera-ready control analyses seed 20260828(20,000 label permutations; 200 split-half draws;500 anchor-curve resamples). All local decoding is

**ZH** 种子与确定性。训练种子 42；条目自助法种子 20260525（B = 1000）；置换种子 20260710（逐维度 500 次／堆叠 300 次置换）；定稿控制分析种子 20260828（20,000 次标签置换；200 次分半抽样；500 次锚点曲线重抽样）。所有本地解码都是

**EN** greedy (temperature 0.0), so local-judge scores aredeterministic up to serving nondeterminism.

**ZH** 贪心的（temperature 0.0），因此本地裁判的分数在服务非确定性之外是确定的。

**EN** Event accounting.LLM-judge calls: 97,200 CHstandalone (40 judges × 2,430 items, 4 rubricscores per call) + 46,170 CH comparative (19judges × 2,430 pairs) + 5,910 DLQ standalone(5×1,182, 3 rubric scores per call) + 21,610 DLQcomparative (1 × 21,610) = 170,890 calls, i.e.,474,310 rubric-level scores and preference labels;human labels total 87,618 (9,720 CH standalonescores, 2,430 CH preferences, 10,638 DLQ stan-dalone scores, 64,830 DLQ preferences).

**ZH** 事件核算。大模型裁判调用：CH 独立评分 97,200 次（40 个裁判 × 2,430 条，每次调用 4 个维度分数）+ CH 对比评分 46,170 次（19 个裁判 × 2,430 对）+ DLQ 独立评分 5,910 次（5×1,182，每次调用 3 个维度分数）+ DLQ 对比评分 21,610 次（1 × 21,610）= 170,890 次调用，即 474,310 个维度级分数与偏好标签；人类标注合计 87,618 条（9,720 个 CH 独立评分、2,430 个 CH 偏好、10,638 个 DLQ 独立评分、64,830 个 DLQ 偏好）。

**EN** PQualitative study: objective vs.subjective rubrics

**ZH** P 质性研究：客观与主观评分维度

**EN** This appendix grounds the quantitative geometryresults in concrete items drawn from the evaluationset. We separate items into two regimes:

**ZH** 本附录把定量的几何结果落到从评测集中抽出的具体条目上。我们把条目分成两种机制：

**EN** Objective rubrics.Items whose target answer isfact-based, veriﬁable, or grounded in widely sharedcultural knowledge. Phrasing may vary across re-sponders, but the underlying information is stable,so evaluation reduces to factual consistency andconcept matching. Human and LLM judges con-verge sharply on these items (Table 26).

**ZH** 客观评分维度。目标答案是事实性的、可核验的，或建立在广泛共有的文化知识之上的条目。不同回答者的措辞可能不同，但底层信息是稳定的，因此评测归结为事实一致性与概念匹配。人类与大模型裁判在这些条目上急剧收敛（表 26）。

**EN** Subjective rubrics.Items that require contex-tual interpretation, reasoning, advisory guidance,or sensitivity to the user’s situation. There is no sin-gle ﬁxed answer; evaluation depends on relevance,completeness, practical applicability, and contex-tual appropriateness rather than exact factual match.Healthcare items in particular carry emotional, ﬁ-nancial, and access-related context that LLM judgestend to overlook even when responses are medicallyaccurate (Table 27).

**ZH** 主观评分维度。需要情境化解读、推理、咨询性引导，或对使用者处境敏感的条目。不存在唯一固定的答案；评测取决于相关性、完整性、实际可适用性以及情境的恰当性，而不是精确的事实匹配。医疗类条目尤其带有情感、经济与可及性方面的语境，而大模型裁判即使在回答医学上准确时也常常忽略这些（表 27）。

**EN** Rubric dimensions assessed.Responses are eval-uated along four axes: (i) task quality / factuality(accuracy, expected details, direct address of thequestion); (ii) linguistic acceptability (grammar,word choice, spelling); (iii) clarity (well-formed, in-terpretable phrasing); and (iv) helpfulness and localrelevance (practical usefulness and ﬁt to the user’ssituational or local context). The objective regime

**ZH** 所评估的维度。回答沿四条轴评估：(i) 任务质量／事实性（准确性、应有细节、是否直接回应问题）；(ii) 语言可接受性（语法、用词、拼写）；(iii) 清晰性（表述是否规整、可解读）；以及 (iv) 有用性与本地相关性（实际用处，以及对使用者处境或本地语境的贴合度）。客观机制

**EN** [Page 28]

**ZH** 第 28 页

**EN** JudgeDeployment / versionCall datesNotes

**ZH** 裁判　部署／版本　调用日期　备注

**EN** gpt-5.5gpt-5.5_2026-04-242026-05-23CH standalone; responses API, no temperatureparameterdeepseek-r1DeepSeek-R1_12026-05-23CH + DLQ; no temperature parametergrok-4grok-4_12026-05-23CH + DLQ; no temperature parametermistral-large-3Mistral-Large-3_12026-05-23CH + DLQllama-3.3-70b (DLQ)Llama-3.3-70B-Instruct_52026-05-23API-hosted for DLQ; locally served for CHgpt-4o (CH)inherited from Hamna et al. (2026)–version as documented theregpt-4 (DLQ)inherited from Watts et al. (2024)–version as documented therelocal judgesHF snapshots, vLLM 0.18.02026-05-22/23bf16, temperature 0.0, top-p 1.0, max 512 to-kens (parse-retry: 1024–2048); 8×B200trained variantsLoRA/PEFT checkpoints (released)2026-05-23/24training seed 42; recipes in App. J

**ZH** gpt-5.5　gpt-5.5_2026-04-24　2026-05-23　CH 独立评分；responses API，无 temperature 参数｜deepseek-r1　DeepSeek-R1_1　2026-05-23　CH + DLQ；无 temperature 参数｜grok-4　grok-4_1　2026-05-23　CH + DLQ；无 temperature 参数｜mistral-large-3　Mistral-Large-3_1　2026-05-23　CH + DLQ｜llama-3.3-70b（DLQ）　Llama-3.3-70B-Instruct_5　2026-05-23　DLQ 走 API 托管；CH 本地部署｜gpt-4o（CH）　继承自 Hamna 等（2026）　–　版本如该文所述｜gpt-4（DLQ）　继承自 Watts 等（2024）　–　版本如该文所述｜本地裁判　HF 快照，vLLM 0.18.0　2026-05-22/23　bf16，temperature 0.0，top-p 1.0，最多 512 token（解析重试：1024–2048）；8×B200｜训练变体　LoRA/PEFT 检查点（已发布）　2026-05-23/24　训练种子 42；配方见附录 J

**EN** Table 24: API deployments and call dates for all judges. Scores from the two source benchmarks are used as releasedby those studies.

**ZH** 表 24：全部裁判的 API 部署与调用日期。两个源基准的分数按那些研究所发布的原样使用。

**EN** ItemStatus

**ZH** 条目　状态

**EN** Raw judge outputsreleased (JSONL per call + two consolidated CSVs)Human labelsreleased as used; provenance per the source studiesPromptsverbatim in App. I and in the releaseAnalysis / ﬁgure codereleased; one command regenerates every number (build_numbers.py) and every ﬁgure(build_artifacts.py)Training conﬁgs & logsper-variant YAMLs, trainer logs, and merged-checkpoint recipes releasedSeedstraining 42; bootstrap 20260525; permutations 20260710; camera-ready controls 20260828Compute8×B200 (vLLM 0.18.0, bf16) for local judges and LoRA training; controls are CPU-onlyAPI versions & datesTable 24Licensescode MIT; outputs/annotations CC BY 4.0, subject to source-benchmark terms

**ZH** 原始裁判输出　已发布（每次调用的 JSONL + 两份合并 CSV）｜人类标签　按使用原样发布；出处遵循源研究｜提示　逐字刊于附录 I，并在发布物中｜分析／绘图代码　已发布；一条命令即可重新生成每个数字（build_numbers.py）与每张图（build_artifacts.py）｜训练配置与日志　已发布各变体的 YAML、训练器日志与合并检查点配方｜种子　训练 42；自助法 20260525；置换 20260710；定稿控制 20260828｜算力　本地裁判与 LoRA 训练用 8×B200（vLLM 0.18.0，bf16）；控制分析仅用 CPU｜API 版本与日期　表 24｜许可　代码 MIT；输出／标注 CC BY 4.0，并服从源基准条款

**EN** Table 25: Reproducibility checklist for the release.

**ZH** 表 25：发布物的可复现性清单。

**EN** is dominated by axis (i); the subjective regime en-gages all four, and the failures in Table 27 concen-trate on axis (iv).

**ZH** 由轴 (i) 主导；主观机制则调动全部四条轴，而表 27 中的失效集中在轴 (iv) 上。

**EN** Why this matters for the geometry.The objec-tive items (Table 26, rows Obj-1–Obj-4) sit on alow-dimensional subspace that LLM judges alreadycover: the correctness axis is shared, and inter-LLMconsensus is genuine consensus with humans. Thesubjective items (Table 27, rows Subj-1–Subj-4)require additional axes (access, vulnerability, af-fordability, reassurance) along which LLM judges’scores underweight or do not vary at all. These fouritems are a qualitative analogue of the principal-angle gap (Sec. 5), consistent with judges sharing amedical-completeness direction while humans alsoweight others; four hand-picked items cannot es-tablish that decomposition, which is why we treatthem as grounding rather than evidence.

**ZH** 这一点为何对几何要紧。客观条目（表 26，Obj-1–Obj-4 行）落在一个低维子空间上，而大模型裁判已经覆盖它：正确性轴是共享的，裁判间共识是与人类的真实共识。主观条目（表 27，Subj-1–Subj-4 行）需要额外的轴（可及性、脆弱性、可负担性、安抚），而大模型裁判的分数在这些轴上权重偏低甚至完全不变。这四条是主角度差距的质性类比（第 5 节），与“裁判共享医学完整性方向、而人类同时还加权其他方向”一致；四条手工挑选的条目不足以确立这一分解，因此我们只把它们当作接地，而不是证据。

**EN** QUse of AI assistants

**ZH** Q AI 助手的使用

**EN** We used LLM-based assistants for language polish-

**ZH** 我们使用基于大模型的助手做语言润色、

**EN** ing, for literature search while surveying relatedwork, for arguing through framing and counter-arguments during drafting, and for writing anal-

**ZH** 在综述相关工作时做文献检索，在起草过程中推敲框架与反驳论证，并编写分析与绘图代码。

**EN** ysis and plotting code. Every claim, number, cita-tion, and line of code so produced was checked andvalidated manually by the authors, who take fullresponsibility for the content of this paper.

**ZH** 由此产生的每一条断言、每一个数字、每一条引用与每一行代码，都由作者手工检查与验证，并由作者对本文内容承担全部责任。

**EN** [Page 29]

**ZH** 第 29 页

**EN** IDLangQuestion (script + English gloss)Why human and LLM agree

**ZH** 编号　语言　问题（原文 + 英文释义）　人类与大模型为何一致

**EN** Obj-1Mlഒരുബാങ്ക്അക്കൗണ്ട്തുടങ്ങാനായിആവ-ശ്യമായരേഖകൾഎന്തൊക്കെയാണ്?(What documents are required to open a bank ac-count?)

**ZH** Obj-1　马拉雅拉姆语　ഒരുബാങ്ക്അക്കൗണ്ട്തുടങ്ങാനായിആവശ്യമായരേഖകൾഎന്തൊക്കെയാണ്?（开立银行账户需要哪些文件？）

**EN** Procedural recall with a canonical checklist (identityand address proof, photographs, PAN/Aadhaar). Allﬁve judges and all three human raters assign identicalfull-credit task-quality scores. Exact agreement.Obj-2Teతెలుగుసంప్రదాయంలోఆడపిల్లలతల్లితండ్రులుపిల్లలమొదటిజన్మకుఎందుకుడబ్బుచెల్లిస్తారు?(In Telugu tradition, why do the parents of a girl payfor the ﬁrst childbirth?)

**ZH** 带规范清单的程序性回忆（身份证明与地址证明、照片、PAN/Aadhaar）。五个裁判与三位人类评分者在任务质量上给出完全相同的满分。完全一致。｜Obj-2　泰卢固语　తెలుగుసంప్రదాయంలోఆడపిల్లలతల్లితండ్రులుపిల్లలమొదటిజన్మకుఎందుకుడబ్బుచెల్లిస్తారు?（在泰卢固传统中，女孩的父母为什么要为第一个孩子的出生付费？）

**EN** Cultural practice grounded in widely shared under-standing (e.g., Janmantara Kanuka). Responses varyin phrasing but capture the core intent; humans explic-itly accept the “gist” as suﬃcient, and LLM judgesscore accordingly. High agreement.Obj-3Hiडेबिटकार्डऔरक्रेडिटकार्डमेंक्याअंतरहै?(What is the difference between a debit card and acredit card?)

**ZH** 建立在广泛共有理解之上的文化习俗（例如 Janmantara Kanuka）。回答措辞各异但都抓住了核心意图；人类明确接受“大意”即算充分，大模型裁判也照此打分。高度一致。｜Obj-3　印地语　डेबिटकार्डऔरक्रेडिटकार्डमेंक्याअंतरहै?（借记卡与信用卡有什么区别？）

**EN** Conceptual but well-deﬁned knowledge: debit drawsfrom the user’s account; credit is borrowed and re-paid with interest. Whenever responses articulate thiscontrast, both humans and LLMs rate them correct.Consistent agreement.Obj-4Knಉತ್ತರಕರ್ನಾಟಕದಲ್ಲಿಬಳಕೆಯಲ್ಲಿರುವಕನ್ನಡಹಾಗುಬೆಂ-ಗಳೂರುಕನ್ನಡದಮಧ್ಯೆಇರುವವ್ಯತ್ಯಾಸಗಳೇೇನು?(What are the differences between the Kannada spokenin North Karnataka and Bengaluru Kannada?)

**ZH** 概念性但界定清晰的知识：借记卡从用户账户扣款；信用卡是借款，需连本带息归还。只要回答讲清了这一对比，人类与大模型都判为正确。一致。｜Obj-4　卡纳达语　ಉತ್ತರಕರ್ನಾಟಕದಲ್ಲಿಬಳಕೆಯಲ್ಲಿರುವಕನ್ನಡಹಾಗುಬೆಂಗಳೂರುಕನ್ನಡದಮಧ್ಯೆಇರುವವ್ಯತ್ಯಾಸಗಳೇೇನು?（北卡纳塔克邦通行的卡纳达语与班加罗尔卡纳达语之间有哪些差异？）

**EN** Widely shared dialectal knowledge with stable,veriﬁable contrasts (vocabulary,address forms,Marathi/Urdu vs. English inﬂuence). Responses varyin phrasing but the core contrasts are ﬁxed; all ﬁvejudges and all three raters assign identical scores.

**ZH** 广泛共有的方言知识，对比稳定且可核验（词汇、称呼形式、马拉地语／乌尔都语影响与英语影响）。回答措辞各异但核心对比是固定的；五个裁判与三位评分者给出完全相同的分数。

**EN** Table 26: Objective rubric, qualitative examples. For fact-based or canonically known items, LLM judges convergewith humans on near-identical scores. Referenced from Sec. 1 and Sec. 5 (boundary analysis).

**ZH** 表 26：客观评分维度的质性示例。对事实性的或规范已知的条目，大模型裁判与人类在近乎相同的分数上收敛。由第 1 节与第 5 节（边界分析）引用。

**EN** [Page 30]

**ZH** 第 30 页

**EN** IDLangThemeQuestion (script + English gloss)What the LLM emphasises vs. what hu-mans need

**ZH** 编号　语言　主题　问题（原文 + 英文释义）　大模型强调什么 vs. 人类需要什么

**EN** Subj-1KnHealthcareaccess,vulnerability,andpower dynamics

**ZH** Subj-1　卡纳达语　医疗可及性、脆弱性与权力关系

**EN** ನಮ್ಮನೆಹತ್ರಇರೋಪ್ರಾಥಮಿಕಆರೋಗ್ಯಕೇೇಂದ್ರದಲ್ಲಿತೋರ್ಸೋಕೆಹೋದ್ರೆಎಲ್ಲಾದಕ್ಕೂದುಡ್ಡುಕೇೇಳ್ತಾರೆನಾನ್ಇವ್ರ್ಮೇಲೆದೂರುಕೊಡ್ಬೇಕುಅಂದ್ರೆಏನ್ಮಾಡ್ಬೇಕು?(If the nearby primary health centre asksfor money to be seen, how do I ﬁle a com-plaint against them?)

**ZH** ನಮ್ಮನೆಹತ್ರಇರೋಪ್ರಾಥಮಿಕಆರೋಗ್ಯಕೇಂದ್ರದಲ್ಲಿತೋರ್ಸೋಕೆಹೋದ್ರೆಎಲ್ಲಾದಕ್ಕೂದುಡ್ಡುಕೇಳ್ತಾರೆನಾನ್ಇವ್ರ್ಮೇಲೆದೂರುಕೊಡ್ಬೇಕುಅಂದ್ರೆಏನ್ಮಾಡ್ಬೇಕು?（如果附近的初级卫生中心看病要收钱，我该如何投诉他们？）

**EN** LLM: detailed procedural guidance onﬁling complaints. Human-aligned: ac-knowledges fear of retaliation, dependenceon the same centre, and recommends sup-portive pathways (community health work-ers, local oﬃcials, collective reporting).The question is about institutional trust andsocial hierarchy, not paperwork.Subj-2MlMedicalrecom-mendationsvs.real-worldaccessi-bility

**ZH** 大模型：给出关于如何投诉的详细程序性指导。人类对齐的做法：承认对报复的恐惧、对同一中心的依赖，并推荐支持性路径（社区健康工作者、地方官员、集体举报）。这个问题关乎制度信任与社会层级，而不是走流程办手续。｜Subj-2　马拉雅拉姆语　医学建议 vs. 现实世界的可及性

**EN** എൻ്റെഒമ്പത്വയസ്സുള്ളമമോൾവീ-ണ്നെറ്റിമുറിഞ്ഞു, ഒരുപാട്വലിയപാട്വരാതെസ്റ്റിച്ചെയ്യാൻഏത്വിഭാഗത്തിലാണ്കുട്ടിയെകാണി-ക്കേണ്ടത്?(My nine-year-old daughter cut her fore-head in a fall; which department should Itake her to so it can be stitched without alarge scar?)

**ZH** എൻ്റെഒമ്പത്വയസ്സുള്ളമമോൾവീണ്നെറ്റിമുറിഞ്ഞു, ഒരുപാട്വലിയപാട്വരാതെസ്റ്റിച്ചെയ്യാൻഏത്വിഭാഗത്തിലാണ്കുട്ടിയെകാണിക്കേണ്ടത്?（我九岁的女儿跌倒磕破了额头；为不留大疤，该带孩子去哪个科室缝合？）

**EN** LLM: narrowly recommends a plastic sur-geon. Human-aligned: balances clinicaloptimality with accessibility and aﬀordabil-ity; many cuts are handled eﬀectively byemergency physicians, paediatric surgeons,or general surgeons if treated promptly.The user’s real concern is healing and min-imal scarring, not access to specialist cos-metic care.

**ZH** 大模型：狭窄地推荐整形外科医生。人类对齐的做法：在临床最优与可及性、可负担性之间取得平衡；许多伤口若处理及时，急诊医生、小儿外科医生或普通外科医生都能处理得当。使用者真正的关切是愈合与尽量少留疤，而不是获得专科美容医疗。

**EN** Subj-3HiOvermedicalisationof everyday living

**ZH** Subj-3　印地语　日常生活的过度医疗化

**EN** घरमेंबिल्लीऔरकुत्तेजैसेपालतूजानवरहैं।क्याउनकेसंपर्कसेबच्चोंऔरबड़ोंकोएलर्जीहोसकतीहै? रोज़मर्राकीज़िंदगीमेंक्याएहतियातरखनीचाहिए?(We keep pets like cats and dogs at home.Can contact cause allergies in children andadults? What everyday precautions shouldwe take?)

**ZH** घरमेंबिल्लीऔरकुत्तेजैसेपालतूजानवरहैं।क्याउनकेसंपर्कसेबच्चोंऔरबड़ोंकोएलर्जीहोसकतीहै? रोज़मर्राकीज़िंदगीमेंक्याएहतियातरखनीचाहिए?（家里养了猫狗之类的宠物。接触会不会让孩子和大人过敏？日常生活中该采取哪些预防措施？）

**EN** LLM: foregrounds HEPA ﬁlters, spe-cialised vacuum cleaners, furniture replace-ment. Human-aligned: starts from low-cost, household-level precautions (cleanli-ness, handwashing, ventilation, symptommonitoring) and escalates only if needed.The user wants to keep living with pets, notto medicalise their home.

**ZH** 大模型：突出 HEPA 滤网、专用吸尘器、更换家具。人类对齐的做法：从低成本的家庭层面预防做起（清洁、洗手、通风、症状观察），只在必要时升级。使用者想的是继续与宠物同住，而不是把自己的家医疗化。

**EN** Subj-4MlEmotionalreas-suranceandriskframing in maternalhealth

**ZH** Subj-4　马拉雅拉姆语　孕产健康中的情感安抚与风险框架

**EN** 6 വർഷംമുമ്പ്ഞാൻഎൻ്റെമകളെപ്രസവിച്ചത്സിസേറിയൻആയിരു-ന്നു. ഇനിഒരുകുട്ടിക്ക്ശ്രമിക്കേണ്ടസമയംആയെന്ന്എല്ലാവരുംപറ-ഞ്ഞുതുടങ്ങി. ഞങ്ങളുംഅതെതീ-രുമാനത്തിലാണ്.എന്നാലുംഎനി-ക്ക്ഇനിസുഖപ്രസവംആവാൻആണ്ആഗ്രഹിക്കുന്നത്. അതിനുഎന്തെങ്കിലുംബുദ്ധിമുട്ടുകൾഉണ്ടാ-വുമമോ?എന്തൊക്കെയാണ്അതി-നുവേണ്ടിമുൻകരുത്തേണ്ടത്?(My ﬁrst delivery 6 years ago was a Cae-sarean. Family is asking us to try for a sec-ond child and we are deciding the same;I want a normal delivery this time. Arethere difficulties? What precautions shouldI take?)

**ZH** 6 വർഷംമുമ്പ്ഞാൻഎൻ്റെമകളെപ്രസവിച്ചത്സിസേറിയൻആയിരുന്നു. ഇനിഒരുകുട്ടിക്ക്ശ്രമിക്കേണ്ടസമയംആയെന്ന്എല്ലാവരുംപറഞ്ഞുതുടങ്ങി. ഞങ്ങളുംഅതെതീരുമാനത്തിലാണ്.എന്നാലുംഎനിക്ക്ഇനിസുഖപ്രസവംആവാൻആണ്ആഗ്രഹിക്കുന്നത്. അതിനുഎന്തെങ്കിലുംബുദ്ധിമുട്ടുകൾഉണ്ടാവുമമോ?എന്തൊക്കെയാണ്അതിനുവേണ്ടിമുൻകരുത്തേണ്ടത്?（6 年前我生女儿时是剖宫产。现在大家都说该考虑再要一个孩子了，我们也正做此决定。但这次我希望顺产。会有什么困难吗？我需要提前做些什么？）

**EN** LLM: foregrounds uterine rupture, foetaldistress, and worst-case complications un-der VBAC. Human-aligned: ﬁrst vali-dates the desire for a normal delivery, notesthat many VBACs succeed under propercare, then discusses risks proportionately.The user is asking for reassurance and con-ﬁdence under family pressure, not a com-plications checklist.

**ZH** 大模型：突出子宫破裂、胎儿窘迫，以及 VBAC 下的最坏并发症。人类对齐的做法：先肯定顺产的愿望，指出在妥善照护下许多 VBAC 都能成功，然后按比例讨论风险。使用者要的是在家庭压力下的安抚与信心，而不是一张并发症清单。

**EN** Table 27: Subjective rubric, healthcare qualitative examples. On items that carry institutional, ﬁnancial, oremotional context, LLM judges score on medical-completeness while humans weight practical accessibility, vulner-ability, and reassurance. These items illustrate, rather than measure, the principal-angle gap reported in Sec. 5; asystematic per-axis test would need item-level coding of the community-relevance axes, which we do not attempthere. Referenced from Sec. 1 and Sec. 5.2.

**ZH** 表 27：主观评分维度的医疗质性示例。在带有制度、经济或情感语境的条目上，大模型裁判按医学完整性打分，而人类在意的是实际可及性、脆弱性与安抚。这些条目只是说明、而非测量第 5 节所报告的主角度差距；系统化的逐轴检验需要对社区相关性各轴做条目级编码，本文不作此尝试。由第 1 节与第 5.2 节引用。
