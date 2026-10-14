# 面向图像质量评估的大型多模态模型 2AFC 提示方法

> 原标题：2AFC Prompting of Large Multimodal Models for Image Quality Assessment
> 作者：Hanwei Zhu, Xiangjie Sui, Baoliang Chen, Xuelin Liu, Peilin Chen, Yuming Fang, Shiqi Wang · arXiv:2402.01162 · 2024-02-02

<!-- [原子块 · verbatim] 2AFC Prompting of Large Multimodal Models for Image Quality Assessment -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] While abundant research has been conducted on improving high-level visual understanding and reasoning capabilities of large multimodal models (LMMs), their visual quality assessment (IQA) ability has  -->

**EN** Index Terms:

**ZH** 索引词：

**EN** I Introduction

**ZH** I 引言

**EN** The recent breakthroughs in large language models (LLMs) [1] have inspired the development of large multimodal models (LMMs) [2, 3, 4, 5], aiming to simulate human-like processing of multimodal information. Three representative abilities—instruction tuning [6], in-context learning [7], and chain-of-thought prompting [8]—highlight the impressive strides made in this field. With the growing interest in LMMs, especially with the emergence phenomenon of models like GPT-4V [5], it becomes crucial to understand their comprehensive capabilities and limitations.

**ZH** 大语言模型（LLM）[1] 的近期突破推动了大型多模态模型（LMM）[2, 3, 4, 5] 的发展，其目标是模拟人类对多模态信息的处理方式。指令微调[6]、上下文学习[7]与思维链提示[8]这三项代表性能力，彰显了这一领域取得的长足进步。随着人们对 LMM 的兴趣日增，尤其是在 GPT-4V[5] 等模型涌现出新能力之后，厘清其综合能力与局限变得十分关键。

<!-- [原子块 · img]  -->

**EN** Fig. 1: Probing the IQA capability of LMMs via two-alternative forced choice. (a) A pair of images with the corresponding normalized mean opinion scores (MOSs), which is in the range of ⟦SLOT_0⟧. A larger value indicates better visual quality. (b) An order reversed version of (a). Humans can effortlessly select the “Train” image with better visual quality regardless of presentation order, but it is unclear whether the LMMs can make the same right choice. In this example, IDEFICS-Instruct [2] gives the incorrect prediction. mPULG-Owl [3] XComposer-VL [4], and Q-Instruct [9] are indifferent to presentation order, and biased towards selecting the second and the first image, respectively. The proprietary GPT-4V [5] is well aligned with human perception of visual quality.

**ZH** 图 1：通过二选一强制选择探查 LMM 的 IQA 能力。(a) 一对图像及其对应的归一化平均意见分数（MOS），取值范围为 ⟦SLOT_0⟧，数值越大表示视觉质量越好。(b) (a) 的顺序颠倒版本。无论呈现顺序如何，人类都能轻松选出视觉质量更好的「Train」图像，但 LMM 能否做出同样正确的选择尚不明朗。在本例中，IDEFICS-Instruct[2] 给出了错误预测。mPULG-Owl[3]、XComposer-VL[4] 与 Q-Instruct[9] 对呈现顺序不敏感，分别偏向选择第二张与第一张图像。闭源的 GPT-4V[5] 则与人类的视觉质量感知高度吻合。

**EN** The high-level visual understanding and reasoning abilities of LMMs have been extensively evaluated across numerous benchmarks utilizing popular vision-language tasks [10], such as image captioning, visual question answering, and cross-modality grounding. However, the low-level visual processing and analysis aspects of LMMs remain relatively under-explored. Image quality assessment (IQA), with the goal of evaluating the perceived quality of visual content, serves as a representative low-level visual task, and holds paramount importance in various image processing [11, 12], computer graphics [13], and computer vision applications [14]. As such, it is highly desirable to evaluate the applicability of LMMs for the IQA task.

**ZH** LMM 的高层视觉理解与推理能力，已在众多基于图像描述、视觉问答、跨模态定位等流行视觉—语言任务的基准上得到充分评测[10]。然而，LMM 在低层视觉处理与分析方面的表现仍相对缺乏考察。图像质量评估（IQA）以评价视觉内容的感知质量为目标，是一项代表性的低层视觉任务，在各类图像处理[11, 12]、计算机图形学[13]与计算机视觉应用中都具有至关重要的地位[14]。因此，评估 LMM 在 IQA 任务上的适用性十分必要。

<!-- [原子块 · img]  -->

**EN** (a) AWGN_Level-⟦SLOT_1⟧

**ZH** (a) AWGN_等级-⟦SLOT_1⟧

<!-- [原子块 · img]  -->

**EN** (b) AWGN_Level-⟦SLOT_2⟧

**ZH** (b) AWGN_等级-⟦SLOT_2⟧

<!-- [原子块 · img]  -->

**EN** (c) JP2K_Level-⟦SLOT_3⟧

**ZH** (c) JP2K_等级-⟦SLOT_3⟧

<!-- [原子块 · img]  -->

**EN** (d) Pink_Level-⟦SLOT_4⟧

**ZH** (d) Pink_等级-⟦SLOT_4⟧

<!-- [原子块 · img]  -->

**EN** (e) MOS = ⟦SLOT_5⟧

**ZH** (e) MOS = ⟦SLOT_5⟧

<!-- [原子块 · img]  -->

**EN** (f) MOS = ⟦SLOT_6⟧

**ZH** (f) MOS = ⟦SLOT_6⟧

**EN** Fig. 2: Illustration of three pairing rules for fine-grained quality comparison. (a)&(b) Two synthetically distorted images with identical visual content and distortion type but different distortion levels. (c)&(d) Two synthetically distorted images with identical visual content and distortion level but different distortion types. (e)&(f) Two realistically distorted images in the MOS interval of ⟦SLOT_7⟧.

**ZH** 图 2：细粒度质量比较的三种配对规则示意。(a)&(b) 两张合成失真图像，视觉内容与失真类型相同，但失真等级不同。(c)&(d) 两张合成失真图像，视觉内容与失真等级相同，但失真类型不同。(e)&(f) 两张真实失真图像，处于 ⟦SLOT_7⟧ 的 MOS 区间内。

**EN** Q-Bench [15] presents an early attempt to assess the visual quality understanding abilities of LMMs through binary quality-relevant question answering, standard quality rating, and quality description. Most recently, You et al. [16] emphasized on the importance of more human-like quality description over “contrived” quality rating, and decomposed IQA into three subtasks: quality description, quality comparison, and comparison reasoning. Although these studies may seem appealing at first glance, they require human-verified quality descriptions, which is a more costly and time-consuming process than collecting scalar quality ratings. Moreover, the subjective nature of visual quality adds complexity to aggregating descriptions from various users. Last, the semantic comparison of two quality descriptions [6] represents an unresolved challenge in natural language processing.

**ZH** Q-Bench[15] 是早期的一次尝试，通过二值质量相关问答、标准质量打分与质量描述来评估 LMM 的视觉质量理解能力。最近，You 等人[16]强调，相比「人为设定」的质量打分，更贴近人类的质量描述更为重要，并把 IQA 分解为质量描述、质量比较与比较推理三个子任务。这些研究初看颇为吸引人，但它们需要人工校验的质量描述，而获取这类描述的代价高于收集标量质量打分，也更为耗时。此外，视觉质量的主观性使得汇聚不同用户的描述变得复杂。最后，两段质量描述之间的语义比较[6]在自然语言处理中本身就是尚未解决的难题。

**EN** The research in visual quality assessment has a long history, and there are many well-established human-rated image quality databases [17, 18, 19, 20, 21, 22, 23, 24, 23], readily available to test this perceptual aspect of LMMs. In this paper, we propose to adopt the two-alternative forced choice (2AFC) method, also known as the paired comparison to comprehensively evaluate the IQA capability of LMMs on existing image quality datasets. We devise coarse-to-fine pairing rules, and use the maximum a posterior (MAP) estimation [25] to convert pairwise preferences of different LLMs to the global ranking scores. Additionally, we introduce three evaluation criteria, namely consistency, accuracy, and correlation, to quantify different and complementary aspects of the IQA capability of LMMs. These criteria offer deeper insights into the strengths and weaknesses of LMMs in discriminating image quality variations. Extensive experiments on subsets of eight existing image quality datasets reveal many “interesting” behaviors of LMMs (see Fig. 1). Most notably, we find that LMMs generally struggle with the IQA task, some of which exhibit strong biases. On the contrary, the proprietary model GPT-4V has exhibited outstanding performance, surpassing the majority of other models by a significant margin. Further testing on more challenging fine-grained pairs reveals that there remains room for improvement.

**ZH** 视觉质量评估研究历史悠久，已有众多成熟的人工评分图像质量数据库[17, 18, 19, 20, 21, 22, 23, 24, 23]，可直接用于检验 LMM 的这一感知维度。本文提出采用二选一强制选择（2AFC）方法（又称成对比较），在已有图像质量数据集上全面评估 LMM 的 IQA 能力。我们设计了由粗到细的配对规则，并用最大后验（MAP）估计[25]把不同大语言模型的成对偏好转换为全局排序分数。此外，我们引入一致性、准确性与相关性三项评价指标，从互补的不同侧面量化 LMM 的 IQA 能力，为理解 LMM 在辨别图像质量差异上的长短提供更深层的洞察。在八个已有图像质量数据集子集上的大量实验揭示了 LMM 的诸多「有趣」行为（见图 1）。最值得注意的是，我们发现 LMM 总体上难以胜任 IQA 任务，其中一些模型表现出强烈的偏好偏差；相反，闭源模型 GPT-4V 表现突出，以显著优势超过绝大多数其他模型。在更具挑战性的细粒度配对上进一步测试表明，仍有改进空间。

**EN** II Ingredients of Probingg Pipeline

**ZH** II 探查流程的构成要素

**EN** In this section, we first introduce the coarse-to-fine pairing rules, and then detail the maximum a posterior estimation (MAP) [25] for multiple options. We last introduce three evaluation criteria to benchmark LMMs.

**ZH** 本节先介绍由粗到细的配对规则，随后详述面向多选项的最大后验（MAP）估计[25]，最后给出用于评测 LMM 的三项评价指标。

**EN** II-A Coarse-to-fine Pairing

**ZH** II-A 由粗到细的配对

**EN** To evaluate the IQA capability of LMMs, we devise a set of coarse-to-fine pairing rules. For coarse-grained quality comparison, different images from the same dataset are randomly paired. For fine-grained quality comparison, we propose three pairing rules, as illustrated in Fig. 2. The first rule involves pairing synthetically distorted images with identical visual content and distortion type but different distortion levels. The second rule suggests pairing synthetically distorted images with identical visual content and distortion level but different distortion types. The third rule entails pairing realistically distorted images within the same mean opinion score (MOS) interval (i.e., of similar visual quality).

**ZH** 为评估 LMM 的 IQA 能力，我们设计了一套由粗到细的配对规则。粗粒度质量比较中，从同一数据集内随机配对不同图像。细粒度质量比较中，我们提出三条配对规则，如图 2 所示：第一条是把视觉内容与失真类型相同、但失真等级不同的合成失真图像配对；第二条是把视觉内容与失真等级相同、但失真类型不同的合成失真图像配对；第三条是把处于同一平均意见分数（MOS）区间（即视觉质量相近）的真实失真图像配对。

**EN** II-B Maximum a Posterior Estimation

**ZH** II-B 最大后验估计

**EN** For a complete 2AFC design, ⟦SLOT_8⟧ test stimuli require ⟦SLOT_9⟧ paired comparison to derive the global ranking results, which is infeasible when ⟦SLOT_10⟧ gets large. As such, we opt for the maximum a posterior estimation (MAP), which is able to handle ⟦SLOT_11⟧ options with fewer needed pairs by solving an optimization problem based on Thurstone’s case V model [25]. We denote a set of images as ⟦SLOT_12⟧ and their MOSs as ⟦SLOT_13⟧. The LMM is represented by a parametric function ⟦SLOT_14⟧, which takes a textual prompt ⟦SLOT_15⟧ and two images ⟦SLOT_16⟧ as inputs, and produces a binary output to indicate whether ⟦SLOT_17⟧ is perceived better than ⟦SLOT_18⟧. MAP estimation aggregates the quality preference entries ⟦SLOT_19⟧, which is computed by counting the number of times image ⟦SLOT_20⟧ preferred over ⟦SLOT_21⟧, into global ranking scores ⟦SLOT_22⟧. The log-likelihood of the quality preference matrix ⟦SLOT_23⟧ can be defined as

**ZH** 在完整的 2AFC 设计中，⟦SLOT_8⟧ 个测试刺激需要 ⟦SLOT_9⟧ 次成对比较才能导出全局排序结果，当 ⟦SLOT_10⟧ 变大时这是不可行的。因此我们选择最大后验（MAP）估计，它通过求解基于 Thurstone Case V 模型[25]的优化问题，能以更少的配对数处理 ⟦SLOT_11⟧ 个选项。我们把一组图像记为 ⟦SLOT_12⟧，其 MOS 记为 ⟦SLOT_13⟧。LMM 由参数化函数 ⟦SLOT_14⟧ 表示，它以文本提示 ⟦SLOT_15⟧ 与两张图像 ⟦SLOT_16⟧ 为输入，输出二值结果以指示 ⟦SLOT_17⟧ 是否被认为优于 ⟦SLOT_18⟧。MAP 估计把质量偏好项 ⟦SLOT_19⟧（由图像 ⟦SLOT_20⟧ 被判定优于 ⟦SLOT_21⟧ 的次数统计得到）聚合为全局排序分数 ⟦SLOT_22⟧。质量偏好矩阵 ⟦SLOT_23⟧ 的对数似然可定义为

<!-- [原子块 · table] ℒ ⁡ ( q θ | C ) = ∑ i , j C i , j ​ log ⁡ ( Φ ⁡ ( q θ ( i ) − q θ ( j ) ) ) , \displaystyle\mathcal{L}(q_{\theta}|C)=\sum_{i,j}C_{i,j}\log(\Phi(q_{\theta}^{(i)}-q_{\theta}^{(j)})), (1) -->

**EN** where ⟦SLOT_24⟧ is the the standard Normal cumulative distribution function (CDF). The MAP estimation can be formed by solving the above maximum likelihood function with a ridge regularization on the scale values ⟦SLOT_25⟧:

**ZH** 其中 ⟦SLOT_24⟧ 是标准正态累积分布函数（CDF）。MAP 估计可通过对上述极大似然函数附加对尺度值 ⟦SLOT_25⟧ 的岭正则化求解得到：

<!-- [原子块 · table] arg max q θ \displaystyle\underset{q_{\theta}}{\text{arg max}} ∑ i , j C i , j ​ log ⁡ ( Φ ⁡ ( q θ ( i ) − q θ ( j ) ) ) − ∑ i ( q θ ( i ) ) 2 2 \displaystyle\sum_{i,j}C_{i,j}\log(\Phi(q_{\theta}^{(i) -->

<!-- [原子块 · object]  -->

**EN** (a)

**ZH** (a)

**EN** Fig. 3: Validation of MAP estimation in aggregating pairwise rankings from the human observer, NIQE, and DBCNN, respectively. MAP estimation quickly converges as the number of pairing rounds increases, where each round consists of ⟦SLOT_26⟧ paired comparisons for ⟦SLOT_27⟧ test images. Performance on sampled images from SPAQ (⟦SLOT_28⟧).

**ZH** 图 3：MAP 估计在聚合来自人类观察者、NIQE 与 DBCNN 的成对排序时的有效性验证。随着配对轮次增加，MAP 估计迅速收敛；每轮包含 ⟦SLOT_27⟧ 张测试图像的 ⟦SLOT_26⟧ 次成对比较。测试对象为从 SPAQ 中采样的图像（⟦SLOT_28⟧）。

**EN** Herein, to verify the reliability and effectiveness of MAP estimation, we adopt MOS (to represent the golden human observer), and two no-reference IQA models NIQE [26] and DBCNN [27] as the judges to rank image pairs in the SPAQ dataset [22]. In particular, each image in sampled SPAQ (⟦SLOT_29⟧) is randomly paired with another image in each round, and such pairing process is repeated ⟦SLOT_30⟧ rounds until convergence. The winning image shall receive a higher quality score from the judge. We compute the Pearson linear correlation coefficient (PLCC) between the average ranking scores by MAP estimation and MOSs, as shown in Fig. 3. We find that for different judges, MAP estimation quickly converges to the respective upper bounds (represented by the dashed lines), which are calculated using the raw quality scores. Therefore, we conclude that if the outcome of the pairwise comparison is accurate, MAP estimation will produce reliable global quality ranking scores with a manageable number of paired comparison. By employing LMMs as the judges in the MAP estimation, we are able to quantify the capability of LMMs in perceiving visual quality like humans do.

**ZH** 为验证 MAP 估计的可靠性与有效性，我们采用 MOS（代表「黄金」人类观察者）以及两个无参考 IQA 模型 NIQE[26] 与 DBCNN[27] 作为评判者，对 SPAQ 数据集[22]中的图像对排序。具体地，采样得到的 SPAQ（⟦SLOT_29⟧）中每张图像在每轮与另一张图像随机配对，这样的配对过程重复 ⟦SLOT_30⟧ 轮直至收敛。胜出的图像将从评判者处获得更高的质量分数。我们计算 MAP 估计所得平均排序分数与 MOS 之间的皮尔逊线性相关系数（PLCC），结果如图 3 所示。我们发现，对不同评判者，MAP 估计都迅速收敛到各自的上界（以虚线表示，该上界由原始质量分数算出）。因此可以得出结论：若成对比较的结果准确，MAP 估计只需可控数量的成对比较就能产出可靠的全局质量排序分数。把 LMM 作为 MAP 估计中的评判者，我们便能量化 LMM 像人类一样感知视觉质量的能力。

**EN** II-C Evaluation Criteria

**ZH** II-C 评价指标

**EN** We propose to quantify the IQA capability of LLMs using the three evaluation criteria.

**ZH** 我们提出用三项评价指标来量化大语言模型的 IQA 能力。

**EN** Consistency (⟦SLOT_31⟧) measures whether the LLM’s prediction is robust to the presentation order of two images:

**ZH** 一致性（⟦SLOT_31⟧）衡量大语言模型的预测是否对两张图像的呈现顺序稳健：

<!-- [原子块 · table] κ = 1 | 𝒫 | ∑ ( x , y ) ∈ 𝒫 𝕀 [ f θ ( ( x , y ) , t ) + f θ ( ( y , x ) , t ) = 1 ] , \displaystyle\kappa=\frac{1}{|\mathcal{P}|}\sum_{(x,y)\in\mathcal{P}}\mathbb{I}\left[f_{\theta}\left(({x},{y}),{t} -->

**EN** where ⟦SLOT_32⟧ denotes the total number of pairs, and ⟦SLOT_33⟧ is the indicator function. ⟦SLOT_34⟧ ranges from ⟦SLOT_35⟧ with a larger value indicating higher consistency.

**ZH** 其中 ⟦SLOT_32⟧ 表示配对总数，⟦SLOT_33⟧ 为指示函数。⟦SLOT_34⟧ 的取值范围为 ⟦SLOT_35⟧，数值越大表示一致性越高。

**EN** TABLE I: Overview of the image subset sampled from eight existing image quality datasets. The two numbers separated by “/” in the last two columns represent the number of reference and distorted images, respectively. We emphasize in the third section two datasets—KADIS-700k and SQAD—that are less likely to be included for training LMMs due to the absence of MOSs. We equip them with MOSs from a formal subjective experiment to test LMMs while minimizing the potential data contamination risk

**ZH** 表 I：从八个已有图像质量数据集采样的图像子集概览。最后两列中以「/」分隔的两个数字分别表示参考图像与失真图像的数量。我们在第三节特别强调 KADIS-700k 与 SQAD 两个数据集——由于缺少 MOS，它们被纳入 LMM 训练的可能性较低。我们通过正式的主观实验为它们补上 MOS，用以在尽量降低数据污染风险的前提下测试 LMM

<!-- [原子块 · table] Dataset Distortion # images # samples Coarse- grained CSIQ [ 17 ] Synthetic 30 / 866 30/866 30 30 KADID-10k [ 18 ] Synthetic 81 / 10,125 81/10,125 81 81 MM21 [ 19 ] Synthetic 129 / 5,031 129/5,031 129 -->

**EN** Accuracy (⟦SLOT_36⟧) measures the accuracy rate of the LLM, provided that the consistency constraint (i.e., ⟦SLOT_37⟧) is met:

**ZH** 准确性（⟦SLOT_36⟧）衡量在满足一致性约束（即 ⟦SLOT_37⟧）的前提下，大语言模型的正确率：

<!-- [原子块 · table] α = 1 | 𝒫 s | ∑ ( x , y ) ∈ 𝒫 s 𝕀 [ f ( ( x , y ) , t ) = 𝕀 [ q ( x ) ≥ q ( y ) ] ] , \displaystyle\alpha=\frac{1}{|\mathcal{P}_{s}|}\sum_{(x,y)\in\mathcal{P}_{s}}\mathbb{I}\left[f\left(({x},{y}),{t}\ -->

**EN** where ⟦SLOT_38⟧ contains the subset of image pairs that the LLM makes consistent prediction.

**ZH** 其中 ⟦SLOT_38⟧ 包含大语言模型给出一致预测的配对子集。

**EN** Correlation (⟦SLOT_39⟧) measures the linear correlation between the global ranking scores aggregated by MAP and the MOSs:

**ZH** 相关性（⟦SLOT_39⟧）衡量 MAP 聚合所得全局排序分数与 MOS 之间的线性相关程度：

<!-- [原子块 · table] ρ = ∑ i = 1 N ( q ( i ) − q ¯ ) ​ ( q θ ( i ) − q ¯ θ ) ∑ i = 1 N ( q ( i ) − q ¯ ) 2 ​ ∑ i = 1 N ( q θ ( i ) − q ¯ θ ) 2 , \displaystyle\rho=\frac{\sum_{i=1}^{N}(q^{(i)}-\overline{q})(q_{\theta}^{(i) -->

**EN** where ⟦SLOT_40⟧ and ⟦SLOT_41⟧ represent the mean MOS and ranking score, respectively. Before computing ⟦SLOT_42⟧, a simple monotonic function is commonly applied to map the model prediction to the MOS range as a way of compensating prediction nonlinearity [28].

**ZH** 其中 ⟦SLOT_40⟧ 与 ⟦SLOT_41⟧ 分别表示 MOS 均值与排序分数均值。在计算 ⟦SLOT_42⟧ 之前，通常会施加一个简单的单调函数，把模型预测映射到 MOS 区间，以补偿预测的非线性[28]。

**EN** TABLE II: VQA capability comparisons of the LMMs in terms of consistency (⟦SLOT_43⟧), accuracy (⟦SLOT_44⟧), and correlation (⟦SLOT_45⟧) with the coarse-grained setting. The weighted average is computed by the average values weighted by the number of samples of the corresponding subsets. The best two results are highlighted in boldface and underline, respectively

**ZH** 表 II：粗粒度设置下各 LMM 在一致性（⟦SLOT_43⟧）、准确性（⟦SLOT_44⟧）与相关性（⟦SLOT_45⟧）上的视觉问答能力对比。加权平均按各子集样本数加权求得。最优与次优结果分别以粗体与下划线标出

<!-- [原子块 · table] IDEFICS-Instruct [ 2 ] mPLUG-Owl [ 3 ] XComposer-VL [ 4 ] Q-Instruct [ 9 ] GPT-4V [ 5 ] Dataset Distortion κ ↑ \kappa\uparrow α ↑ \alpha\uparrow ρ ↑ \rho\uparrow κ ↑ \kappa\uparrow α ↑ \alpha\uparrow  -->

**EN** III Experiments

**ZH** III 实验

**EN** In this section, we first provide the experimental setups, and then present the coarse-grained and fine-grained IQA results of four LMMs with in-depth analysis. Last, other global ranking aggregation methods are applied to conduct the ablation experiments.

**ZH** 本节先给出实验设置，随后呈现四个 LMM 在粗粒度与细粒度下的 IQA 结果并作深入分析，最后用其他全局排序聚合方法开展消融实验。

**EN** III-A Experimental Setups

**ZH** III-A 实验设置

**EN** We assess five LMMs that accept multiple images as input. These include four open-source models: IDEFICS-Instruct (based on LLaMA-9B) [2], mPLUG-Owl (based on LLaMA-7B) [3], XComposer-VL (based on InternLM-7B) [4], and Q-Instruct (based on LLaVA_v1.5-7B) [9] and one closed-source model: GPT-4V [5]. We initialize the open-source models with their default pretrained weights and use the official API to call GPT-4V. We sample a total of ⟦SLOT_46⟧ images from eight image quality datasets to conduct experiments. Synthetically distorted images are selected from CSIQ [17], KADID-10k [18], KADIS-700k [24], and MM21 [19] datasets. Realistically distorted images are chosen from CLIVE [20], KonIQ-10k [21], SPAQ [22], and SQAD [23] datasets. As listed in Table I, the sampled images form two subsets for coarse-grained and fine-grained quality assessment, respectively. It is worth noting that we manually curate ⟦SLOT_47⟧ images from KADIS-700k and SQAD datasets, which do not contain MOSs. This selection is to avoid data contamination, considering that closed-source LMM, such as GPT-4V, may have been trained on these image quality datasets. To assign MOSs to images from KADIS-700k and SQAD datasets, we conduct subjective testing using the single stimulus continuous methodology [29]. We invite ⟦SLOT_48⟧ subjects to participate in subjective testing in a controlled laboratory environment, ensuring the ambient illumination does not directly reflect off the displays. We apply the outlier rejection strategy recommended by ITU-T BT.500 [29] to filter noisy data. Finally, the mean value of the valid scores for each image is taken as the ground truth quality score.

**ZH** 我们评估了五个接受多图输入的 LMM，其中包括四个开源模型：IDEFICS-Instruct（基于 LLaMA-9B）[2]、mPLUG-Owl（基于 LLaMA-7B）[3]、XComposer-VL（基于 InternLM-7B）[4] 与 Q-Instruct（基于 LLaVA_v1.5-7B）[9]，以及一个闭源模型 GPT-4V[5]。开源模型均使用默认预训练权重初始化，GPT-4V 则通过官方 API 调用。我们从八个图像质量数据集共采样 ⟦SLOT_46⟧ 张图像开展实验：合成失真图像取自 CSIQ[17]、KADID-10k[18]、KADIS-700k[24] 与 MM21[19]；真实失真图像取自 CLIVE[20]、KonIQ-10k[21]、SPAQ[22] 与 SQAD[23]。如表 I 所示，采样得到的图像分别构成用于粗粒度与细粒度质量评估的两个子集。需要说明的是，我们从不含 MOS 的 KADIS-700k 与 SQAD 数据集中人工挑选了 ⟦SLOT_47⟧ 张图像，这一选择旨在避免数据污染，因为 GPT-4V 等闭源 LMM 可能在这些图像质量数据集上训练过。为给 KADIS-700k 与 SQAD 的图像赋予 MOS，我们采用单刺激连续质量标度法[29]开展主观测试，邀请 ⟦SLOT_48⟧ 名受试者在受控实验室环境中参与，确保环境光照不会在显示屏上形成直接反射。我们按 ITU-T BT.500[29] 推荐的异常值剔除策略过滤噪声数据，最后取每张图像有效评分的均值作为真值质量分数。

**EN** For image pairs with inconsistent predictions (see Eq. (3)), we exclude them from updating the quality preference matrix ⟦SLOT_49⟧. It is worth noting that global ranking scores are re-scale to the range of ⟦SLOT_50⟧. A larger score indicates better visual quality. We set the round number ⟦SLOT_51⟧ to ⟦SLOT_52⟧ in our experiments, which is sufficient for the MAP estimation to converge, as shown in Fig. 3. The pre-defined prompts ⟦SLOT_53⟧ are given as follows: prompt = [ ‘This is the first image:’, <Image x>, ‘This is the second image:’, <Image y>, ‘Which image has better visual quality?’ ]

**ZH** 对于预测不一致的图像对（见式 (3)），我们把它们排除在质量偏好矩阵 ⟦SLOT_49⟧ 的更新之外。需要说明的是，全局排序分数被重新缩放到 ⟦SLOT_50⟧ 区间，分数越大表示视觉质量越好。实验中我们把轮数 ⟦SLOT_51⟧ 设为 ⟦SLOT_52⟧，如图 3 所示，这足以让 MAP 估计收敛。预定义提示 ⟦SLOT_53⟧ 如下：prompt = [ 'This is the first image:', <Image x>, 'This is the second image:', <Image y>, 'Which image has better visual quality?' ]

**EN** III-B Coarse-grained IQA Performance

**ZH** III-B 粗粒度 IQA 表现

**EN** We collect a total of ⟦SLOT_54⟧ images for the coarse-grained quality comparison from eight IQA datasets. There are three sampling strategies. 1) We ensure the distorted images selected from the synthetic datasets are content-independent; 2) The mean opinion score (MOS) distribution of these images of each dataset is maintained as a roughly uniform distribution across five quality levels (excellent, good, fair, poor bad); 3) We compute the spatial information and colorfulness attributes of the chosen images to ensure the content balance [30].

**ZH** 我们从八个 IQA 数据集共收集 ⟦SLOT_54⟧ 张图像用于粗粒度质量比较。采样遵循三条策略：1) 确保从合成数据集中选出的失真图像在内容上互不重复；2) 使各数据集所选图像的平均意见分数（MOS）分布在优、良、中、差、劣五个质量等级上大致均匀；3) 计算所选图像的空间信息量与色彩丰富度属性，以保证内容均衡[30]。

**EN** TABLE III: VQA capability comparisons in terms of consistency (⟦SLOT_55⟧) and accuracy (⟦SLOT_56⟧) with the fine-grained setting

**ZH** 表 III：细粒度设置下在一致性（⟦SLOT_55⟧）与准确性（⟦SLOT_56⟧）上的视觉问答能力对比

<!-- [原子块 · table] IDEFICS-Instruct [ 2 ] mPLUG-Owl [ 3 ] XCompose-VL [ 4 ] Q-Instruct [ 9 ] GPT-4V [ 5 ] Single subject Dataset Type κ ↑ \kappa\uparrow α ↑ \alpha\uparrow κ ↑ \kappa\uparrow α ↑ \alpha\uparrow κ ↑ \kapp -->

**EN** TABLE IV: VQA capability comparisons in terms of correlation (⟦SLOT_57⟧) with the fine-grained setting

**ZH** 表 IV：细粒度设置下在相关性（⟦SLOT_57⟧）上的视觉问答能力对比

<!-- [原子块 · table] IDEFICS- mPLUG- XCompose- Q- GPT- Single Instruct Owl VL Instruct 4V subject AWGN 0.000 0.000 0.543 0.543 0.586 0.586 0.449 0.449 0.815 0.815 0.919 0.919 JPEG 0.000 0.000 0.482 0.482 0.148 0.148 0.560 -->

**EN** We conduct the experiments with the images from the same dataset owing to the varying MOS scales across different datasets. The results are shown in Table II, from which we can obtain several interesting observations. First, all open-source LMMs, i.e., IDEFICS-Instruct, mPLUG-Owl, XComposer-VL, and Q-Instruct, show poor performance in terms of prediction consistency, suggesting a tendency to provide biased responses regardless of image content. For instance, we count IDEFICS-Instruct and mPLUG-Owl to demonstrate a percentage exceeding ⟦SLOT_58⟧ of choosing the “second” image, while the XComposer-VL exhibits a preference for the “first” image with approximately ⟦SLOT_59⟧. Such biased predictions significantly impact the accuracy and consistency of model inference, leading to inferior performance in IQA. In addition, while Q-Instruct claims to achieve competitive low-level instruction performance for individual images, it shows subpar performance on comparing the visual quality of a pair of images and indicates the model may suffer from over-fitting issues. Subsequently, GPT-4V outperforms other LMMs across all datasets according to the three proposed evaluation criteria, suggesting its inherent capability to quantify visual quality. To mitigate potential data contamination issues associated with GPT-4V, we strategically select images from the KADIS-700k dataset, which lacks quality-related labels, and the recently released SQAD dataset. Despite these constraints, GPT-4V continues to demonstrate superior performance across these datasets. Notably, the accuracy ⟦SLOT_60⟧ of consistent pairs surpasses ⟦SLOT_61⟧ when compared to human preferences. Moreover, GPT-4V performs better on datasets with realistic distortion compared with synthetic distortion, as shown in Table II. This could be attributed to the fact that LMMs are trained on the pairs of text and images with realistic distortions. Last but not least, despite the increased complexity presented by pairs that contain mixed distortions, GPT-4V still obtains promising results, outperforming the majority of remaining LMMs.

**ZH** 由于不同数据集的 MOS 标度不同，我们在同一数据集内的图像上开展实验。结果见表 II，从中可以得到若干有价值的观察。第一，IDEFICS-Instruct、mPLUG-Owl、XComposer-VL 与 Q-Instruct 等所有开源 LMM 的预测一致性都较差，说明它们倾向于给出与图像内容无关的偏倚回答。例如，我们统计到 IDEFICS-Instruct 与 mPLUG-Owl 选择「第二张」图像的比例超过 ⟦SLOT_58⟧，而 XComposer-VL 则偏好「第一张」图像，比例约为 ⟦SLOT_59⟧。这种偏倚预测严重影响了模型推理的准确性与一致性，导致 IQA 表现不佳。此外，尽管 Q-Instruct 宣称在单张图像的低层指令任务上具有竞争力，它在比较一对图像的视觉质量时表现平庸，说明该模型可能存在过拟合问题。其次，按三项评价指标衡量，GPT-4V 在所有数据集上都优于其他 LMM，说明它具备量化视觉质量的内在能力。为缓解 GPT-4V 潜在的数据污染问题，我们特意从缺少质量标签的 KADIS-700k 数据集以及近期发布的 SQAD 数据集中选图。即便在这些限制下，GPT-4V 依旧在相应数据集上表现最优。值得注意的是，在与人类偏好对比时，一致配对的准确率 ⟦SLOT_60⟧ 超过 ⟦SLOT_61⟧。此外，如表 II 所示，GPT-4V 在真实失真数据集上的表现优于合成失真数据集，这可能是因为 LMM 的训练图文对多为真实失真图像。最后同样重要的是，尽管包含混合失真的配对复杂度更高，GPT-4V 仍取得了可观的结果，优于其余大多数 LMM。

**EN** TABLE V: Quantitative comparison of GPT-4V aggregated by different global ranking methods in terms of PLCC

**ZH** 表 V：GPT-4V 经不同全局排序方法聚合后在 PLCC 上的定量对比

<!-- [原子块 · table] Method CSIQ KADID-10k MM21 CLIVE KonIQ-10k SPAQ KADIS-700k SQAD MLE [ 25 ] 0.757 0.757 0.575 0.575 0.472 0.472 0.745 0.745 0.734 0.734 0.828 0.828 0.667 0.667 0.676 0.676 Perron [ 31 ] 0.708 0.708 0.5 -->

**EN** III-C Fine-grained IQA Performance

**ZH** III-C 细粒度 IQA 表现

**EN** We utilize sampled images from CSIQ and SPAQ to carry out the fine-grained quality assessment. Specifically, we sample four scenes from the CSIQ dataset. Each of them is degraded by five classical distortion types, including additive white Gaussian noise (AWGN), JPEG, JPEG 2000 (JP2K), pink noise, and blur, and five distortion levels. For realistic distortion, we select SPAQ as our target database, partition the normalized MOS scores at the range of ⟦SLOT_62⟧ into four equidistant intervals, and strictly limit the sampling to ⟦SLOT_63⟧ images per MOS interval.

**ZH** 我们利用从 CSIQ 与 SPAQ 采样的图像开展细粒度质量评估。具体地，从 CSIQ 数据集中采样四个场景，每个场景施加五类经典失真——加性高斯白噪声（AWGN）、JPEG、JPEG 2000（JP2K）、粉红噪声与模糊——以及五个失真等级。真实失真方面，我们选择 SPAQ 作为目标数据库，把 ⟦SLOT_62⟧ 范围内的归一化 MOS 划分为四个等距区间，并严格限制每个 MOS 区间采样 ⟦SLOT_63⟧ 张图像。

**EN** Since fine-grained quality comparisons are more challenging, we invite one subject to conduct the experiment in the same setting as the four LMMs. We present the consistency and accuracy in Table III. The correlation results are shown in Table IV. For the synthetically distorted images from the CSIQ dataset, we first compare the images with the same content and identical distortion types but varied distortion levels. From Tables III, IV and Fig. 2 (a)&(b), we observe that the existing LMMs struggle to distinguish the image with superior quality in such fine-grained comparisons. Although GPT-4V outperforms other LMMs, the average consistency and accuracy values are far from human performance. The AWGN is the most difficult distortion type compared with other distortions for the existing LMMs, possibly due to its rarity in the training data. The correlation of Q-Instruct underperforms IDEFICS-Instruct, indicating that the low-level information of single images does not improve the visual quality comparison capability of the Q-Instruct. Subsequently, we compare the images with the same content and distortion levels but different distortion types. We find that it is challenging to compare a pair of images with slight distortions (e.g., Level-1 and Level-2), and the LMMs recognize them as the same image. However, as the level of distortion increases, different distortions demonstrate distinct visual appearances, making it easier to discern the superior quality image (see Fig. 2 (c)&(d)). Additionally, mPLUG-Owl outperforms GPT-4V in terms of the consistency criterion and achieves the second-best average accuracy value, which reveals that mPLUG-Owl demonstrates better fine-grained IQA capability compared with other open-source LMMs. For realistically distorted images from the SPAQ dataset, we present four normalized MOS intervals to conduct the fine-grained comparison. Most LMMs perform better for realistic distortions than synthetic distortions. Subjects and LMMs can more readily discern preferences within the quality interval of ⟦SLOT_64⟧. It is reasonable for LMMs to exhibit inferior performance in the quality interval of ⟦SLOT_65⟧ and ⟦SLOT_66⟧ as they represent either severe distortion or high-quality visual appearance, both of which pose significant challenges for human observers in selecting an image of superior quality. Overall, GPT-4V demonstrates the best performance in the fine-grained IQA experiment, but there remains ample room for improvement.

**ZH** 由于细粒度质量比较更具挑战性，我们邀请一名受试者在与四个 LMM 相同的设置下完成实验。一致性与准确性结果见表 III，相关性结果见表 IV。对来自 CSIQ 数据集的合成失真图像，我们首先比较内容相同、失真类型相同但失真等级不同的图像。由表 III、表 IV 与图 2 (a)&(b) 可见，现有 LMM 难以在此类细粒度比较中分辨出质量更优的图像。虽然 GPT-4V 优于其他 LMM，其平均一致性与准确性数值仍远不及人类。AWGN 是现有 LMM 最难处理的失真类型，可能因为它在训练数据中较为罕见。Q-Instruct 的相关性不如 IDEFICS-Instruct，说明单张图像的低层信息并未提升 Q-Instruct 的视觉质量比较能力。随后，我们比较内容相同、失真等级相同但失真类型不同的图像，发现比较一对轻微失真（如等级 1 与等级 2）的图像相当困难，LMM 会把它们认作同一张图像；但随着失真等级提高，不同失真呈现出各异的视觉外观，辨别质量更优的图像也随之变得容易（见图 2 (c)&(d)）。此外，mPLUG-Owl 在一致性指标上优于 GPT-4V，并取得第二好的平均准确性，说明它比其他开源 LMM 具备更强的细粒度 IQA 能力。对来自 SPAQ 数据集的真实失真图像，我们给出四个归一化 MOS 区间用于细粒度比较，多数 LMM 在真实失真上的表现优于合成失真。受试者与 LMM 更容易在 ⟦SLOT_64⟧ 质量区间内辨别偏好。LMM 在 ⟦SLOT_65⟧ 与 ⟦SLOT_66⟧ 质量区间表现较差也在情理之中，因为这两个区间分别对应严重失真与高质量视觉外观，人类观察者同样难以从中选出质量更优的图像。总体而言，GPT-4V 在细粒度 IQA 实验中表现最佳，但仍有很大的改进空间。

**EN** III-D Ablation Experiments

**ZH** III-D 消融实验

**EN** In this subsection, we compare the MAP estimation to other global aggregation methods, including the maximum likelihood estimation (MLE) [25], the Perron rank method [31], and the TrueSkill rating system [32]. In contrast to MAP estimation, MLE directly optimizes the log-likelihood function to derive the global ranking scores. The Perron rank method uses the principal eigenvector of a pairwise comparison matrix to generate the global ranking, providing a robust and efficient solution for ranking problems [31]. TrueSkill rating system is a video game ranking algorithm that models the skill of each player as a univariate Gaussian random variable, with mean and variance representing the average skill of each player and the degree of uncertainty, respectively. As shown in Table V, we can observe MAP and TrueSkill perform better than other methods. While TrueSkill demonstrates competitive results to MAP, we continue to choose MAP estimation as our default method owing to its mathematically appealing properties.

**ZH** 在本小节中，我们把 MAP 估计与其他全局聚合方法对比，包括极大似然估计（MLE）[25]、Perron 排序法[31]与 TrueSkill 评分系统[32]。与 MAP 估计不同，MLE 直接优化对数似然函数以导出全局排序分数；Perron 排序法利用成对比较矩阵的主特征向量生成全局排序，为排序问题提供了一种稳健而高效的解法[31]；TrueSkill 评分系统是一种电子游戏排名算法，把每位玩家的技能建模为单变量高斯随机变量，其均值与方差分别表示玩家的平均技能水平与不确定程度。如表 V 所示，MAP 与 TrueSkill 的表现优于其他方法。尽管 TrueSkill 的结果与 MAP 相当，我们仍选择 MAP 估计作为默认方法，因为它具备更为优雅的数学性质。

**EN** IV Conclusions

**ZH** IV 结论

**EN** In this work, we have probed the low-level IQA capabilities of LMMs, an area that has been relatively under-explored. We devise coarse-grained and fine-grained pairing rules to evaluate the IQA ability of the state-of-the-art LMMs. The MAP estimation is used for aggregating global ranking scores of different LMMs. We further propose three evaluation criteria, providing a comprehensive evaluation of the LMM’s IQA abilities. Our analysis has revealed that most LMMs generally lack IQA capabilities and tend to exhibit biased preferences. The proprietary LMM, GPT-4V, shows promising performance in the coarse-grained subset, indicating potential applicability in IQA. However, there is still considerable room for improvement in the IQA ability of existing LMMs, particularly in the fine-grained subset. We hope that our benchmark and analysis will serve as a catalyst for the development of more advanced and versatile LMMs in the field of visual quality assessment.

**ZH** 本文探查了 LMM 的低层 IQA 能力——一个此前相对缺乏研究的领域。我们设计了粗粒度与细粒度配对规则，用以评估当前最优 LMM 的 IQA 能力，并用 MAP 估计聚合不同 LMM 的全局排序分数；进一步提出三项评价指标，对 LMM 的 IQA 能力做出综合评测。分析表明，多数 LMM 总体上不具备 IQA 能力，且倾向于表现出偏倚偏好。闭源 LMM GPT-4V 在粗粒度子集上表现可期，显示出在 IQA 中的应用潜力。然而现有 LMM 的 IQA 能力仍有相当大的提升空间，尤其是在细粒度子集上。我们希望本文的基准与分析能推动视觉质量评估领域出现更先进、更通用的 LMM。

**EN** Acknowledgements

**ZH** 致谢

**EN** The authors thank Kede Ma for his insightful discussions and diligent efforts in revising the paper.

**ZH** 作者感谢 Kede Ma 在本文修改过程中富有洞见的讨论与付出的辛勤努力。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] [1] OpenAI, “GPT-4 technical report,” CoRR , vol. abs/2303.08774, 2023. -->

<!-- [原子块 · verbatim] [2] H. Face, “Introducing IDEFICS: An open reproduction of state-of-the-art visual language model,” https://huggingface.co/blog/idefics/ , 2023. -->

<!-- [原子块 · verbatim] [3] Q. Ye, H. Xu, G. Xu, J. Ye, M. Yan, Y. Zhou, J. Wang, A. Hu, P. Shi, Y. Shi, and et al. , “mPLUG-Owl: Modularization empowers large language models with multimodality,” CoRR , vol. abs/2304.14178, -->

<!-- [原子块 · verbatim] [4] P. Zhang, X. D. B. Wang, Y. Cao, C. Xu, L. Ouyang, Z. Zhao, S. Ding, S. Zhang, and et al. , “InternLM-XComposer: A vision-language large model for advanced text-image comprehension and composition -->

<!-- [原子块 · verbatim] [5] OpenAI, “GPT-4V(ision) system card,” https://cdn.openai.com/papers/GPTV_System_Card.pdf/ , 2023. -->

<!-- [原子块 · verbatim] [6] H. Touvron, T. Lavril, G. Izacard, X. Martinet, M. Lachaux, T. Lacroix, B. Rozière, N. Goyal, and et al. , “LLaMA: Open and efficient foundation language models,” CoRR , vol. abs/2302.13971, 2023. -->

<!-- [原子块 · verbatim] [7] T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, P. Dhariwal, A. Neelakantan, P. Shyam, G. Sastry, A. Askell, and et al. , “Language models are few-shot learners,” in Neural Information Proc -->

<!-- [原子块 · verbatim] [8] J. Wei, X. Wang, D. Schuurmans, M. Bosma, F. Xia, E. Chi, Q. V. Le, D. Zhou, and et al. , “Chain-of-thought prompting elicits reasoning in large language models,” in Neural Information Processing  -->

<!-- [原子块 · verbatim] [9] H. Wu, Z. Zhang, E. Zhang, C. Chen, L. Liao, A. Wang, K. Xu, C. Li, J. Hou, G. Zhai et al. , “Q-Instruct: Improving low-level visual abilities for multi-modality foundation models,” CoRR , vol. ab -->

<!-- [原子块 · verbatim] [10] R. Cai, Z. Song, D. Guan, Z. Chen, X. Luo, C. Yi, and A. Kot, “BenchLMM: Benchmarking cross-style visual capability of large multimodal models,” CoRR , vol. abs/2312.02896, 2023. -->

<!-- [原子块 · verbatim] [11] Q. Wu, H. Li, K. N. Ngan, and K. Ma, “Blind image quality assessment using local consistency aware retriever and uncertainty aware evaluator,” IEEE Trans. Circuits and Systems for Video Tech. , v -->

<!-- [原子块 · verbatim] [12] W. Yang, H. Huang, J. Liu, and A. C. Kot, “Facial image compression via neural image manifold compression,” IEEE Trans. Circuits and Systems for Video Tech. , to appear 2023. -->

<!-- [原子块 · verbatim] [13] L. Zhao, W. Zheng, Y. Duan, J. Zhou, and J. Lu, “SPTR: Structure-preserving transformer for unsupervised indoor depth completion,” IEEE Trans. Circuits and Systems for Video Tech. , to appear 202 -->

<!-- [原子块 · verbatim] [14] H. Zhu, B. Chen, L. Zhu, and S. Wang, “Learning spatiotemporal interactions for user-generated video quality assessment,” IEEE Trans. Circuits and Systems for Video Tech. , vol. 33, no. 3, pp. 10 -->

<!-- [原子块 · verbatim] [15] H. Wu, Z. Zhang, E. Zhang, C. Chen, L. Liao, A. Wang, C. Li, W. Sun, Q. Yan, G. Zhai, and W. Lin, “Q-Bench: A benchmark for general-purpose foundation models on low-level vision,” CoRR , vol. abs -->

<!-- [原子块 · verbatim] [16] Z. You, Z. Li, J. Gu, Z. Yin, T. Xue, and C. Dong, “Depicting beyond scores: Advancing image quality assessment through multi-modal language models,” CoRR , vol. abs/2312.08962, 2023. -->

<!-- [原子块 · verbatim] [17] E. C. Larson and D. M. Chandler, “Most apparent distortion: Full-reference image quality assessment and the role of strategy,” Journal of Electronic Imaging , vol. 19, no. 1, pp. 011 006–011 027, -->

<!-- [原子块 · verbatim] [18] H. Lin, V. Hosu, and D. Saupe, “KADID-10k: A large-scale artificially distorted IQA database,” in IEEE Int. Conf. Multimedia and Expo , 2019, pp. 1–3. -->

<!-- [原子块 · verbatim] [19] Y. Li, S. Wang, X. Zhang, S. Wang, S. Ma, and Y. Wang, “Quality assessment of end-to-end learned image compression: The benchmark and objective measure,” in ACM Int. Conf. on Multimedia , 2021, p -->

<!-- [原子块 · verbatim] [20] D. Ghadiyaram and A. C. Bovik, “Massive online crowdsourced study of subjective and objective picture quality,” IEEE Trans. Image Processing , vol. 25, no. 1, pp. 372–387, 2016. -->

<!-- [原子块 · verbatim] [21] V. Hosu, H. Lin, T. Sziranyi, and D. Saupe, “KonIQ-10k: An ecologically valid database for deep learning of blind image quality assessment,” IEEE Trans. Image Processing , vol. 29, pp. 4041–4056, -->

<!-- [原子块 · verbatim] [22] Y. Fang, H. Zhu, Y. Zeng, K. Ma, and Z. Wang, “Perceptual quality assessment of smartphone photography,” in IEEE Int. Conf. Computer Vision and Pattern Recognition , 2020, pp. 3677–3686. -->

<!-- [原子块 · verbatim] [23] Z. Fang, A. Ignatov, E. Zamfir, and R. Timofte, “SQAD: Automatic smartphone camera quality assessment and benchmarking,” in IEEE Int. Conf. on Computer Vision , 2023, pp. 20 532–20 542. -->

<!-- [原子块 · verbatim] [24] H. Lin, V. Hosu, and D. Saupe, “DeepFL-IQA: Weak supervision for deep IQA feature learning,” CoRR , vol. abs/2001.08113, 2020. -->

<!-- [原子块 · verbatim] [25] K. Tsukida and M. R. Gupta, “How to analyze paired comparison data,” Technical Report UWEETR-2011-0004, University of Washington, 2011. -->

<!-- [原子块 · verbatim] [26] A. Mittal, R. Soundararajan, and A. C. Bovik, “Making a ‘completely blind’ image quality analyzer,” IEEE Signal Processing Letters , vol. 20, no. 3, pp. 209–212, 2013. -->

<!-- [原子块 · verbatim] [27] W. Zhang, K. Ma, J. Yan, D. Deng, and Z. Wang, “Blind image quality assessment using a deep bilinear convolutional neural network,” IEEE Trans. Circuits and Systems for Video Tech. , vol. 30, no. -->

<!-- [原子块 · verbatim] [28] VQEG, “Final report from the video quality experts group on the validation of objective models of video quality assessment,” 2000. [Online]. Available: http://www.vqeg.org -->

<!-- [原子块 · verbatim] [29] B. T. ITU-R, “Methodology for the subjective assessment of the quality of television pictures,” https://www.itu.int/rec/R-REC-BT.500 , 2002. -->

<!-- [原子块 · verbatim] [30] S. Winkler, “Analysis of public image and video databases for quality assessment,” IEEE Journal of Selected Topics in Signal Processing , vol. 6, no. 6, pp. 616–625, 2012. -->

<!-- [原子块 · verbatim] [31] T. L. Saaty and L. G. Vargas, “Inconsistency and rank preservation,” Journal of Mathematical Psychology , vol. 28, no. 2, pp. 205–214, 1984. -->

<!-- [原子块 · verbatim] [32] R. Herbrich, T. Minka, and T. Graepel, “Trueskill tm {}^{\textsc{tm}} : A bayesian skill rating system,” in Neural Information Processing Systems , 2007, pp. 569–576. -->
