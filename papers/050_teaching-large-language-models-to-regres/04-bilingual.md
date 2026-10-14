# 用分数分布教大语言模型回归准确的图像质量分数

> 原标题：Teaching Large Language Models to Regress Accurate Image Quality Scores using Score Distribution
> 作者：Zhiyuan You, Xin Cai, Jinjin Gu, Tianfan Xue, Chao Dong · arXiv:2501.11561 · 2025-01-20

<!-- [原子块 · verbatim] Teaching Large Language Models to Regress Accurate Image Quality Scores Using Score Distribution -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] With the rapid advancement of Multi-modal Large Language Models (MLLMs), MLLM-based Image Quality Assessment (IQA) methods have shown promising performance in linguistic quality description. However,  -->

**EN** 1 Introduction

**ZH** 1 引言

<!-- [原子块 · img]  -->

**EN** Figure 1: Illustration of our distribution-based soft label. Image A is overexposed, while Image B and C are well-exposed with better and similar quality. “exce.” means “excellent”. To train an MLLM as a quality scorer, continuous scores need to be discretized to discrete level tokens as the training label. Q-Align [70] discretizes human-labeled mean score to a one-hot label, causing information loss. We discretize the score distribution, which is approximated as a Gaussian distribution, to obtain a more accurate soft label. Our soft label maintains better inter-image relationships that the Image B is better than A (⟦SLOT_0⟧), and Image B and C share similar quality (⟦SLOT_1⟧), while the one-hot label can not.

**ZH** 图 1：我们基于分布的软标签示意图。图像 A 过曝，而图像 B 与 C 曝光良好、质量更好且相近。“exce.”表示“excellent”（优秀）。要把 MLLM 训练成质量评分器，需要把连续分数离散化为离散等级词元作为训练标签。Q-Align [70] 把人工标注的平均分数离散为一个 one-hot 标签，造成信息损失。我们则把近似为高斯分布的分数分布离散化，得到更准确的软标签。我们的软标签更好地保持了图像间关系——图像 B 优于 A（⟦SLOT_0⟧），图像 B 与 C 质量相近（⟦SLOT_1⟧），而 one-hot 标签做不到这一点。

**EN** Image Quality Assessment (IQA) focuses on perceiving the visual quality of images [85, 26, 66, 41], and is widely adopted in various application scenarios, e.g., image compression and transmission [52, 5], processing smartphone-captured photos [17], and evaluating generation or restoration models [30, 99, 12, 11], etc. With the emergence of Multi-modal Large Language Models (MLLMs) [32, 75, 95, 44], MLLM-based IQA begins to attract more research interests [69, 71, 7, 80, 79]. These methods mainly leverage MLLMs to describe image quality using language, recognizing that language better mirrors human expression, and captures the multifaceted nature of IQA tasks [80].

**ZH** 图像质量评估（IQA）关注对图像视觉质量的感知 [85, 26, 66, 41]，并被广泛应用于各类场景，例如图像压缩与传输 [52, 5]、智能手机拍摄照片的处理 [17]，以及生成或复原模型的评估 [30, 99, 12, 11] 等。随着多模态大语言模型（MLLM）[32, 75, 95, 44] 的出现，基于 MLLM 的 IQA 开始吸引更多研究兴趣 [69, 71, 7, 80, 79]。这些方法主要利用 MLLM 以语言描述图像质量，因为语言更贴合人类的表达方式，并能捕捉 IQA 任务的多面性 [80]。

**EN** However, for quality scoring, which needs an accurate numerical score to quantify an image’s quality, existing description-centered MLLMs [69, 71, 80, 79] perform less accurately than traditional IQA methods. This hinders their applications on real-world IQA scenarios. Considering MLLMs’ good generalization ability on various downstream tasks and promising performance on quality description, it is possible for MLLMs to score the image quality. Therefore, in this work, we aim to explore how MLLMs can effectively regress accurate quality scores by leveraging their broad training and inherent adaptability.

**ZH** 然而，对于需要准确数值分数来量化图像质量的评分任务，现有以描述为中心的 MLLM [69, 71, 80, 79] 的准确性不如传统 IQA 方法，这阻碍了它们在真实 IQA 场景中的应用。考虑到 MLLM 在各类下游任务上良好的泛化能力以及在质量描述上的可观表现，让 MLLM 为图像质量打分是可行的。因此，本工作旨在探索 MLLM 如何借助其广博的训练与固有的适应性，有效地回归出准确的质量分数。

**EN** We find that the principal challenge in training MLLMs to predict accurate quality scores is the distribution gap between MLLMs’ outputs and quality scores. MLLMs generate outputs as discrete tokens, while the quality score is inherently continuous, usually approximated to a Gaussian distribution. Previous approaches, like Q-Align [70], attempte to address the distribution gap by directly discretizing the mean score (i.e., the expectation of estimated score distribution) into a one-hot label, as depicted in Fig. 1. However, such a one-hot discretization method introduces information loss, causing mismatches between the discretized labels and the original continuous scores. For instance, in Fig. 1, Image A is overexposed with a lower mean score than Image B, but their one-hot labels appear identical. Conversely, Image B and C are well-exposed with similar quality scores, yet their discretized labels are different.

**ZH** 我们发现，训练 MLLM 预测准确质量分数的主要挑战在于 MLLM 输出与质量分数之间的分布鸿沟：MLLM 以离散词元生成输出，而质量分数本质上是连续的，通常被近似为高斯分布。以往方法如 Q-Align [70] 试图通过把平均分数（即所估计分数分布的期望）直接离散为一个 one-hot 标签来弥合这一鸿沟，如图 1 所示。然而，这种 one-hot 离散化方法引入了信息损失，导致离散化标签与原始连续分数之间不匹配。例如在图 1 中，图像 A 过曝、平均分数低于图像 B，但二者的 one-hot 标签却完全相同；相反，图像 B 与 C 曝光良好、质量分数相近，其离散化标签却不同。

**EN** To overcome the distribution gap, we propose a novel soft label to bridge continuous and discrete distributions. As illustrated in Fig. 1, instead of discretizing the mean of score distribution, we discretize the continuous score distribution itself into a discrete distribution of different levels. During training, this discrete distribution is used as the soft training label. This enables effective training with minimal information loss. Also, our distribution-based soft label better preserves inter-image relationship. For example, in Fig. 1, Image B is better than Image A, and Image B and C share similar quality, while the simple one-hot label fails to capture such relationships. At inference, MLLMs output discrete token results, which can be recovered to continuous score distribution. This method ensures that the discrete outputs align well with the underlying continuous distribution, allowing to accurately predict the desired score.

**ZH** 为克服这一分布鸿沟，我们提出一种新颖的软标签来桥接连续分布与离散分布。如图 1 所示，我们不对分数分布的均值做离散化，而是把连续的分数分布本身离散化为不同等级上的离散分布。训练时，这一离散分布被用作软训练标签，从而在信息损失极小的情况下实现有效训练。此外，我们基于分布的软标签更好地保持了图像间关系：例如在图 1 中，图像 B 优于图像 A，图像 B 与 C 质量相近，而简单的 one-hot 标签无法捕捉这些关系。推理时，MLLM 输出离散词元结果，可被还原为连续的分数分布。该方法确保离散输出与底层连续分布良好对齐，从而准确预测所需分数。

**EN** Another key challenge is the dataset variation, where different IQA datasets exhibit distinct distributions, making it hard to simply combine them for co-training. Due to this variation, images from different datasets may have nearly the same quality scores (i.e., linearly re-scaled scores) but drastically different perceptual quality [88, 98]. A previous method, UNIQUE [88], has demonstrated that the fidelity loss [63] under the Thurstone’s model [60] can effectively capture the intra-dataset relationships, thus facilitating the joint training of multiple IQA datasets. However, the fidelity loss requires the model to predict an accurate score distribution, which MLLMs trained with the one-hot label cannot provide. Fortunately, MLLMs trained with our distribution-based soft label can predict such an accurate score distribution, allowing the adaptation of the fidelity loss. We apply this fidelity loss to our MLLM-based quality scorer and demonstrate its effectiveness in this new context.

**ZH** 另一项关键挑战是数据集差异：不同 IQA 数据集呈现不同的分布，难以简单地合并做联合训练。由于这种差异，来自不同数据集的图像可能具有几乎相同的质量分数（即线性重标定后的分数），感知质量却截然不同 [88, 98]。已有方法 UNIQUE [88] 证明，Thurstone 模型 [60] 下的保真损失（fidelity loss）[63] 能有效捕捉数据集内部关系，从而促进多个 IQA 数据集的联合训练。然而，保真损失要求模型预测准确的分数分布，而用 one-hot 标签训练的 MLLM 无法提供这一点。幸运的是，用我们基于分布的软标签训练的 MLLM 可以预测这样准确的分数分布，使得保真损失得以适配。我们把该保真损失应用于基于 MLLM 的质量评分器，并证明了它在新情境下的有效性。

**EN** Equipped with these designs, we successfully develop a distribution-based multi-modal image quality assessment model, termed DeQA-Score. DeQA-Score achieves better score regression results than baseline methods on both in-distribution (e.g., 1.3% in PLCC on KonIQ [21]) and out-of-distribution datasets (e.g., 4.6% in PLCC on LIVE-WILD [18]). The advantage of our DeQA-Score becomes more pronounced with the co-training across multiple IQA datasets. Moreover, our method can further predict the distribution of quality scores, which is closely aligned with the distribution derived from extensive human annotations. We hope that our DeQA-Score will inspire more research to explore the potential of quality score distribution.

**ZH** 借助这些设计，我们成功开发出一个基于分布的多模态图像质量评估模型，命名为 DeQA-Score。在分布内数据集（如在 KonIQ [21] 上 PLCC 提升 1.3%）与分布外数据集（如在 LIVE-WILD [18] 上 PLCC 提升 4.6%）上，DeQA-Score 都取得了优于基线方法的分数回归结果。随着跨多个 IQA 数据集的联合训练，DeQA-Score 的优势更加明显。此外，我们的方法还能进一步预测质量分数的分布，该分布与大量人工标注得到的分布高度吻合。我们希望 DeQA-Score 能激发更多研究去探索质量分数分布的潜力。

**EN** 2 Related Works

**ZH** 2 相关工作

**EN** Image Quality Assessment (IQA) methods mainly rely on quality scores to assess image quality. They can be categorized into full-reference and non-reference methods through whether there is a high-quality reference image.

**ZH** 图像质量评估（IQA）方法主要依赖质量分数来评价图像质量，可按是否存在高质量参考图像分为全参考方法与无参考方法。

**EN** Full-reference IQA methods compute a similarity score as the quality score between a distorted image and a high-quality reference. Classical works rely on human-designed metrics such as structural similarity [66], phase congruency with gradient magnitude [82], image information [53], etc. The rapid advancement of deep learning has also inspired learning-based IQA methods that measure image quality through data-driven training. Pioneered by LPIPS [85] and PieAPP [48], driven by large-scale IQA datasets [85, 24, 31, 52], deep-learning methods [4, 6, 16, 15, 19, 76, 94, 8] have exhibited quite high accuracy in quality score regression.

**ZH** 全参考 IQA 方法计算失真图像与高质量参考图像之间的相似度分数作为质量分数。经典工作依赖人工设计的度量，如结构相似度 [66]、相位一致性与梯度幅值 [82]、图像信息 [53] 等。深度学习的快速发展也催生了基于学习的 IQA 方法，通过数据驱动的训练来度量图像质量。以 LPIPS [85] 与 PieAPP [48] 为先驱，在大规模 IQA 数据集 [85, 24, 31, 52] 的驱动下，深度学习方法 [4, 6, 16, 15, 19, 76, 94, 8] 在质量分数回归上已展现出相当高的准确性。

**EN** Non-reference IQA methods directly regress a quality score without a reference image. Initially, hand-crafted natural image statistics are adopted [37, 40, 41, 42, 43, 50, 58]. Subsequently, deep-learning-based methods [25, 34, 46, 55, 56, 93, 96, 86, 78] replace hand-crafted statistics by learning quality priors from human-annotated IQA datasets [21, 17, 31, 30]. Recent works further improve the regression accuracy by introducing multi-dataset co-training strategy [88], multi-scale features [26], CLIP pre-training [64], multi-dimension attention [73], multitask learning [89], and so on.

**ZH** 无参考 IQA 方法在没有参考图像的情况下直接回归质量分数。早期采用手工设计的自然图像统计量 [37, 40, 41, 42, 43, 50, 58]；随后，基于深度学习的方法 [25, 34, 46, 55, 56, 93, 96, 86, 78] 用从人工标注 IQA 数据集 [21, 17, 31, 30] 中学到的质量先验取代了手工统计量。近期工作还通过引入多数据集联合训练策略 [88]、多尺度特征 [26]、CLIP 预训练 [64]、多维度注意力 [73]、多任务学习 [89] 等进一步提升了回归准确性。

**EN** Multi-modal Large Language Models (MLLMs) incorporate visual modality into Large Language Models (LLMs) [13, 1, 61, 59] to achieve general visual ability by leveraging the broad training and powerful generalization ability of LLMs. Existing MLLMs [3, 14, 32, 44, 67, 74, 77, 83, 84, 95] have demonstrated a general visual ability and can tackle a variety of multi-modality tasks, like visual question answering [20, 35, 36], document understanding [38, 39, 54], image captioning [2, 9, 81], etc. Given MLLMs’ advanced performance in these high-level perception tasks, it is natural to explore how MLLMs perform in low-level perception tasks that are highly related to IQA.

**ZH** 多模态大语言模型（MLLM）把视觉模态引入大语言模型（LLM）[13, 1, 61, 59]，借助 LLM 广博的训练与强大的泛化能力获得通用视觉能力。现有 MLLM [3, 14, 32, 44, 67, 74, 77, 83, 84, 95] 已展现出通用视觉能力，能够处理视觉问答 [20, 35, 36]、文档理解 [38, 39, 54]、图像描述生成 [2, 9, 81] 等多种多模态任务。鉴于 MLLM 在这些高层感知任务上的出色表现，自然会去探索 MLLM 在与 IQA 高度相关的低层感知任务上表现如何。

**EN** MLLM-based IQA methods leverages MLLMs’ foundational knowledge to achieve better IQA performance or more detailed assessment results [72, 92]. Q-Bench [68, 91] shows that general MLLMs have some low-level perception ability. [97] evaluates various MLLMs on the widely-adopted Two-Alternative Forced Choice (2AFC) task. Q-Instruct [69] enhances the low-level perception ability of MLLMs by introducing a large-scale dataset. Co-Instruct [71] concentrates on the quality comparison among multiple images. DepictQA [80, 79] performs single-image assessment and paired-image comparison in both full-reference and non-reference settings. Q-Ground [7] focuses on the visual quality grounding task, and performs fine-scale detailed visual quality analysis. Some of these works have proposed MLLM-based quality scoring methods, e.g., binary softmax strategy in [68, 91] and pair-wise voting in [80, 79]. Nonetheless, these works principally focus on the quality description ability using languages.

**ZH** 基于 MLLM 的 IQA 方法借助 MLLM 的基础知识，以获得更好的 IQA 性能或更细致的评估结果 [72, 92]。Q-Bench [68, 91] 表明通用 MLLM 具备一定的低层感知能力。[97] 在广泛采用的二选一强制选择（2AFC）任务上评估了多种 MLLM。Q-Instruct [69] 通过引入大规模数据集增强了 MLLM 的低层感知能力。Co-Instruct [71] 关注多张图像之间的质量比较。DepictQA [80, 79] 在全参考与无参考设定下执行单图评估与成对图像比较。Q-Ground [7] 聚焦视觉质量定位任务，并进行细粒度的细致视觉质量分析。其中部分工作提出了基于 MLLM 的质量评分方法，例如 [68, 91] 中的二值 softmax 策略与 [80, 79] 中的成对投票。尽管如此，这些工作主要关注的是用语言进行质量描述的能力。

**EN** MLLM-based quality scorer. Initially, Q-Bench [68, 91] proposes a binary softmax strategy, enabling MLLMs to generate quality scores by predicting two discrete quality levels (i.e., good or poor). This strategy is adopted by Q-Instruct [69] and Co-Instruct [71]. Compare2Score [98] achieves quality scoring by teaching MLLMs to compare pair-wise images. Inspired by humans’ annotation process, Q-Align [70] discretizes scores to five discrete levels using one-hot label to train MLLMs, resulting in more accurate score regression. Dog-IQA [33] adopts the one-hot label for training-free IQA by incorporating specific standards and local semantic objects. However, as discussed in Sec. 1, one-hot label causes some information loss and can not fully maintain the inter-image relationship.

**ZH** 基于 MLLM 的质量评分器。最初，Q-Bench [68, 91] 提出一种二值 softmax 策略，使 MLLM 通过预测两个离散质量等级（即好或差）来生成质量分数，该策略被 Q-Instruct [69] 与 Co-Instruct [71] 采用。Compare2Score [98] 通过教 MLLM 比较成对图像来实现质量评分。受人类标注过程启发，Q-Align [70] 用 one-hot 标签把分数离散为五个等级来训练 MLLM，得到更准确的分数回归。Dog-IQA [33] 采用 one-hot 标签，通过引入特定标准与局部语义对象实现免训练的 IQA。然而，如第 1 节所讨论的，one-hot 标签会造成一定的信息损失，且无法完整保持图像间关系。

**EN** 3 Soft Label Construction

**ZH** 3 软标签构造

**EN** 3.1 Revisiting One-hot Label

**ZH** 3.1 重访 one-hot 标签

**EN** Training with one-hot label. MLLMs only accept discrete tokens as inputs and outputs. Therefore, as shown in Fig. 2a, continuous scores11 1 Unless otherwise specified, the mean quality scores in all datasets will be normalized to ⟦SLOT_2⟧, and the variances will be normalized accordingly. must be discretized into discrete tokens to train the MLLMs. Q-Align [70] adopts a one-hot discretization method. Specifically, as depicted in Fig. 2b, the score range ⟦SLOT_3⟧ is uniformly divided into five intervals. These intervals represent five rating levels, {“bad”, “poor”, “fair”, “good”, “excellent”}, which is the rating standard defined by [51]. In Fig. 2a, the Mean Opinion Score (MOS) of the image, 4.30, fails into the fifth intervals, resulting in the discretized label “excellent”. Accordingly, the response is formulated as “The quality of this image is excellent”. Using the response as the training labels, following [61, 13], MLLMs can be trained with next token prediction loss, i.e., cross-entropy loss between predicted logits and labels.

**ZH** 用 one-hot 标签训练。MLLM 只接受离散词元作为输入与输出。因此，如图 2a 所示，连续分数11 1 除非另有说明，所有数据集中的平均质量分数都将被归一化到 ⟦SLOT_2⟧，方差也相应归一化。必须被离散化为离散词元才能训练 MLLM。Q-Align [70] 采用 one-hot 离散化方法。具体而言，如图 2b 所示，分数范围 ⟦SLOT_3⟧ 被均匀划分为五个区间，这些区间代表五个评分等级 {“bad”、“poor”、“fair”、“good”、“excellent”}，即 [51] 所定义的评分标准。在图 2a 中，该图像的平均意见分数（MOS）4.30 落入第五个区间，得到离散化标签“excellent”。相应地，回答被构造为“The quality of this image is excellent”。以该回答作为训练标签，沿用 [61, 13]，MLLM 可用下一词元预测损失进行训练，即预测 logits 与标签之间的交叉熵损失。

<!-- [原子块 · img]  -->

**EN** Figure 2: (a) MLLMs need discrete level tokens for training. Thus, continuous scores must be converted into discrete level tokens as training labels. (b) Comparison between one-hot label [70] and our soft label. One-hot label uniformly divides the score range into 5 intervals to discretize the mean score, i.e., the expectation of estimated score distribution. One-hot label assumes that different levels are identically independent, which is inaccurate. In contrast, we discretize the estimated Gaussian distribution of the score. Our soft label better preserves the relationships between levels, e.g., “fair” is closer to “good” than “excellent”.

**ZH** 图 2：（a）MLLM 训练需要离散等级词元，因此连续分数必须被转换为离散等级词元作为训练标签。（b）one-hot 标签 [70] 与我们的软标签对比。one-hot 标签把分数范围均匀划分为 5 个区间，以离散化平均分数（即所估计分数分布的期望）。one-hot 标签假定不同等级相互独立同分布，这是不准确的。相比之下，我们对分数所估计的高斯分布做离散化。我们的软标签更好地保持了等级之间的关系，例如“fair”比“excellent”更接近“good”。

**EN** Limitations of one-hot label. First, ideal training with cross-entropy loss using one-hot labels assumes that the five levels are independent (i.e., orthogonal in a latent space). However, intuitively, these levels are not truly independent, e.g., “fair” is closer to “good” than “excellent”. Second, one-hot discretization only considers the mean score, which is the expectation of the score distribution, ignoring the distribution’s uncertainty (i.e., variance). Third, near the border of two levels, images with similar quality can be divided into different levels. For example, in Fig. 1, Image B (MOS 3.38) and Image C (MOS 3.49) share similar mean scores, but are differently classified as “fair” and “good”, due to their proximity to the border of these two levels, i.e., 3.4 in Fig. 2b. Finally, one-hot label causes information loss. In Q-Align, the five levels are respectively assigned scores {1, 2, 3, 4, 5}, with which we calculate the discretization precision in Tab. 1. The discretization error is around ⟦SLOT_4⟧ to ⟦SLOT_5⟧ larger than our soft label that we will soon introduce, thus the one-hot label keeps lower correlation with MOS.

**ZH** one-hot 标签的局限。第一，用 one-hot 标签配合交叉熵损失做理想训练，隐含假定五个等级相互独立（即在潜空间中正交）。然而直观上这些等级并非真正独立，例如“fair”比“excellent”更接近“good”。第二，one-hot 离散化只考虑平均分数（即分数分布的期望），忽略了分布的不确定性（即方差）。第三，在两个等级的边界附近，质量相近的图像可能被划分到不同等级。例如在图 1 中，图像 B（MOS 3.38）与图像 C（MOS 3.49）平均分数相近，却因靠近这两个等级的边界（即图 2b 中的 3.4）而被分别归类为“fair”与“good”。最后，one-hot 标签会造成信息损失。在 Q-Align 中，五个等级分别被赋予分数 {1, 2, 3, 4, 5}，我们据此在表 1 中计算离散化精度。其离散化误差比我们即将介绍的软标签大约 ⟦SLOT_4⟧ 到 ⟦SLOT_5⟧，因此 one-hot 标签与 MOS 的相关性更低。

**EN** Table 1: Comparison of discretization precision between Q-Align’s one-hot label [70] and our soft label. The precision of MOS discretization is measured by L1 Error / RMSE and PLCC / SRCC. The distance of original distribution and recovered distribution is measured by JS divergence / Wasserstein distance.

**ZH** 表 1：Q-Align 的 one-hot 标签 [70] 与我们的软标签在离散化精度上的对比。MOS 离散化精度用 L1 误差 / RMSE 与 PLCC / SRCC 度量；原始分布与还原分布之间的距离用 JS 散度 / Wasserstein 距离度量。

<!-- [原子块 · table] Metrics Discretization KonIQ [ 21 ] SPAQ [ 17 ] KADID [ 31 ] L1 / RSME One-hot label 0.302 / 0.374 0.299 / 0.366 0.327 / 0.389 Soft label 0.008 / 0.018 0.011 / 0.025 0.024 / 0.038 PLCC / SRCC One-hot  -->

**EN** 3.2 Soft Label

**ZH** 3.2 软标签

**EN** Discretization using score distribution. As demonstrated in [88], the quality score of one image, ⟦SLOT_6⟧, is typically modeled as a Gaussian distribution, ⟦SLOT_7⟧, where ⟦SLOT_8⟧ and ⟦SLOT_9⟧ are the Mean Opinion Score (MOS) and variance of multiple human annotations, respectively. The distribution is represented by its probability density function, ⟦SLOT_10⟧. As shown in the second row of Fig. 2b, we select five central points, ⟦SLOT_11⟧, as the centers of the five discrete levels. The width of each level region, ⟦SLOT_12⟧, is set as 1. The possibility of the score falling into the ⟦SLOT_13⟧ level is denoted as ⟦SLOT_14⟧ and is calculated as:

**ZH** 使用分数分布做离散化。如 [88] 所示，一幅图像的质量分数 ⟦SLOT_6⟧ 通常被建模为高斯分布 ⟦SLOT_7⟧，其中 ⟦SLOT_8⟧ 与 ⟦SLOT_9⟧ 分别为多次人工标注的平均意见分数（MOS）与方差。该分布由其概率密度函数 ⟦SLOT_10⟧ 表示。如图 2b 第二行所示，我们选取五个中心点 ⟦SLOT_11⟧ 作为五个离散等级的中心，每个等级区域的宽度 ⟦SLOT_12⟧ 设为 1。分数落入第 ⟦SLOT_13⟧ 个等级的可能性记为 ⟦SLOT_14⟧，计算如下：

<!-- [原子块 · table] p i r ​ a ​ w = ∫ c i − d / 2 c i + d / 2 f ⁡ ( x ) ​ dx , i ∈ { 0 , 1 , 2 , 3 , 4 } . p_{i}^{raw}=\int_{c_{i}-d/2}^{c_{i}+d/2}f(x){\rm dx},\quad i\in\{0,1,2,3,4\}. (1) -->

**EN** We assign the five levels with the same textual tokens as Q-Align, i.e., {“bad”, “poor”, “fair”, “good”, “excellent”}. Correspondingly, the score of ⟦SLOT_15⟧ level is ⟦SLOT_16⟧. This defines a rough discrete distribution as ⟦SLOT_17⟧.

**ZH** 我们为五个等级赋予与 Q-Align 相同的文本词元，即 {“bad”、“poor”、“fair”、“good”、“excellent”}。相应地，第 ⟦SLOT_15⟧ 个等级的分数为 ⟦SLOT_16⟧。这定义了一个粗略的离散分布 ⟦SLOT_17⟧。

**EN** Post-adjustment. The discrete distribution is rough because of truncation errors. As shown in the second row of Fig. 2b, there are two truncation regions (i.e., ⟦SLOT_18⟧ and ⟦SLOT_19⟧), which are not considered in Eq. 1. This can cause two problems. First, the sum of ⟦SLOT_20⟧ does not equal 1, meaning ⟦SLOT_21⟧ is not strictly a discrete distribution. Second, the expectation of this discrete distribution does not equal the expectation of score distribution, ⟦SLOT_22⟧, leading to discretization errors.

**ZH** 后调整。该离散分布因截断误差而较为粗略。如图 2b 第二行所示，存在两个截断区域（即 ⟦SLOT_18⟧ 与 ⟦SLOT_19⟧），式 1 并未加以考虑。这会带来两个问题：第一，⟦SLOT_20⟧ 之和不等于 1，意味着 ⟦SLOT_21⟧ 并非严格意义上的离散分布；第二，该离散分布的期望不等于分数分布的期望 ⟦SLOT_22⟧，从而产生离散化误差。

**EN** To correct these truncation errors, we propose a post-adjustment method. Specifically, we apply a linear transformation to adjust ⟦SLOT_23⟧ to more accurate ⟦SLOT_24⟧ as:

**ZH** 为校正这些截断误差，我们提出一种后调整方法。具体而言，我们对 ⟦SLOT_23⟧ 施加线性变换，把它调整为更准确的 ⟦SLOT_24⟧：

<!-- [原子块 · table] p i \displaystyle p_{i} = α ​ p i r ​ a ​ w + β \displaystyle=\alpha p_{i}^{raw}+\beta s . t . ∑ i p i \displaystyle{\rm s.t.}\quad\sum\nolimits_{i}p_{i} = 1 , μ r ​ e ​ c = ∑ i p i ​ c i = μ , \displ -->

**EN** where ⟦SLOT_25⟧ means recovered expectation from discrete distribution. The parameters of the linear transformation, ⟦SLOT_26⟧ and ⟦SLOT_27⟧, can be determined by solving these two constraint conditions. One example of post-adjustment is given in Fig. 3. Moreover, the statistics of these two parameters in Sec. 3.2 show that the average values of ⟦SLOT_28⟧ and ⟦SLOT_29⟧ are quite close to 1 and 0, respectively, implying that the post-adjustment is minimal. This effectively defines our soft label, which follows the discrete distribution as ⟦SLOT_30⟧.

**ZH** 其中 ⟦SLOT_25⟧ 表示由离散分布还原出的期望。线性变换的两个参数 ⟦SLOT_26⟧ 与 ⟦SLOT_27⟧ 可通过求解这两个约束条件确定。图 3 给出了一个后调整的示例。此外，第 3.2 节中这两个参数的统计显示，⟦SLOT_28⟧ 与 ⟦SLOT_29⟧ 的平均值分别十分接近 1 和 0，说明后调整的幅度很小。这有效地定义了我们的软标签，它服从离散分布 ⟦SLOT_30⟧。

**EN** Ideally, the discretization error of the MOS will be 0. However, the possibility of some levels may slightly fall below zero after the linear transformation. We address this by simply clipping these values to zero. The impact of this clipping on accuracy is negligible, as shown in Tab. 1. After clipping, our discretization error for MOS remains around ⟦SLOT_31⟧ to ⟦SLOT_32⟧ smaller than Q-Align’s one-hot label. Also, our soft label maintains a perfect (i.e., 1.000) Pearson Linear Correlation Coefficient (PLCC) and Spearman Rank-order Correlation Coefficient (SRCC) with the original MOS.

**ZH** 理想情况下，MOS 的离散化误差应为 0。然而，线性变换后某些等级的可能性可能略低于零。我们通过把这些值简单裁剪到零来处理。如表 1 所示，这一裁剪对准确性的影响可以忽略。裁剪之后，我们对 MOS 的离散化误差仍比 Q-Align 的 one-hot 标签小约 ⟦SLOT_31⟧ 到 ⟦SLOT_32⟧；并且我们的软标签与原始 MOS 保持完美（即 1.000）的皮尔逊线性相关系数（PLCC）与斯皮尔曼秩相关系数（SRCC）。

<!-- [原子块 · img]  -->

**EN** Figure 3: Illustration of the soft label adjustment.

**ZH** 图 3：软标签调整示意图。

**EN** Table 2: Statistics of the label adjustment parameters. Averaged ⟦SLOT_33⟧ and ⟦SLOT_34⟧ are very approaching 1 and 0, respectively, meaning that the post-adjustment is quite small.

**ZH** 表 2：标签调整参数的统计。⟦SLOT_33⟧ 与 ⟦SLOT_34⟧ 的平均值分别非常接近 1 和 0，说明后调整的幅度很小。

<!-- [原子块 · table] KonIQ [ 21 ] SPAQ [ 17 ] KADID [ 31 ] α \alpha 1.036 ± \pm 0.041 1.033 ± \pm 0.085 1.118 ± \pm 0.091 β \beta -0.005 ± \pm 0.005 -0.005 ± \pm 0.014 -0.015 ± \pm 0.010 -->

**EN** Recovery from discrete to continuous score distribution. As shown in the second condition of Eq. 2, we can compute the expectation of discrete distribution, ⟦SLOT_35⟧, as the recovered expectation of original distribution. Besides the expectation, we can also recover the original variance using the variance of the discrete distribution, ⟦SLOT_36⟧, as:

**ZH** 从离散分数分布还原到连续分数分布。如式 2 的第二个条件所示，我们可以计算离散分布的期望 ⟦SLOT_35⟧，作为原始分布期望的还原值。除期望之外，我们还可以用离散分布的方差 ⟦SLOT_36⟧ 来还原原始方差：

<!-- [原子块 · table] μ r ​ e ​ c = ∑ i p i ​ c i , ( σ r ​ e ​ c ) 2 = ∑ i p i ​ ( c i − μ r ​ e ​ c ) 2 . \mu^{rec}=\sum\nolimits_{i}p_{i}c_{i},\quad(\sigma^{rec})^{2}=\sum\nolimits_{i}p_{i}(c_{i}-\mu^{rec})^{2}. (3) -->

**EN** Then we calculate the distance between recovered distribution, ⟦SLOT_37⟧, and original distribution, ⟦SLOT_38⟧, as provided in Tab. 1. Our recovered distribution is closely aligned with human-annotated score distribution. In contrast, one-hot label can not recover such a distribution.

**ZH** 随后我们计算还原分布 ⟦SLOT_37⟧ 与原始分布 ⟦SLOT_38⟧ 之间的距离，结果见表 1。我们还原出的分布与人工标注的分数分布高度吻合；相比之下，one-hot 标签无法还原这样的分布。

<!-- [原子块 · img]  -->

**EN** Figure 4: Framework of our DeQA-Score trained with soft label. For the “⟦SLOT_39⟧level⟦SLOT_40⟧” token, the KL divergence loss is calculated between predicted probabilities and our soft label. For other tokens, common cross-entropy loss for next token prediction is calculated.

**ZH** 图 4：用软标签训练的 DeQA-Score 框架。对“⟦SLOT_39⟧level⟦SLOT_40⟧”词元，在预测概率与我们的软标签之间计算 KL 散度损失；对其他词元，则计算用于下一词元预测的常规交叉熵损失。

**EN** 4 DeQA-Score Model

**ZH** 4 DeQA-Score 模型

**EN** 4.1 Training with Our Soft Label

**ZH** 4.1 用我们的软标签训练

**EN** Model architecture. As illustrated in Fig. 4, we follow the widely adopted MLLM architecture [32, 75] to construct our model. First, a vision encoder is adopted to represent the input image to visual tokens. Then, a vision-to-text connector projects the visual tokens into the textual space. Following [75], we use a vision abstractor as the connector. The abstractor can further reduce the number of visual tokens to 64. Finally, the visual and textual tokens are fused together and fed into an LLM for response prediction.

**ZH** 模型架构。如图 4 所示，我们沿用被广泛采用的 MLLM 架构 [32, 75] 来构建模型。首先用一个视觉编码器把输入图像表示为视觉词元；随后一个视觉到文本的连接器把视觉词元投影到文本空间中。沿用 [75]，我们使用视觉抽象器（vision abstractor）作为连接器，该抽象器还能进一步把视觉词元数量缩减到 64。最后，视觉词元与文本词元融合后送入 LLM 以预测回答。

**EN** Next token prediction loss for common response tokens. As described in Sec. 3.1 and illustrated in Fig. 4, the constructed response follows the template, “The quality of this image is ⟦SLOT_41⟧level⟦SLOT_42⟧”. For common response tokens other than the level token, we compute the next token prediction loss, i.e., the cross-entropy loss ⟦SLOT_43⟧, following [61, 45].

**ZH** 常规回答词元的下一词元预测损失。如第 3.1 节所述并如图 4 所示，构造出的回答遵循模板“The quality of this image is ⟦SLOT_41⟧level⟦SLOT_42⟧”。对除等级词元之外的常规回答词元，我们沿用 [61, 45] 计算下一词元预测损失，即交叉熵损失 ⟦SLOT_43⟧。

**EN** KL divergence loss for the level token. There are five candidate values for the level token: {“bad”, “poor”, “fair”, “good”, “excellent”}. Our soft label, ⟦SLOT_44⟧, assigns a ground-truth probability to each value. Let the predicted probabilities be ⟦SLOT_45⟧, the KL divergence loss is calculated through:

**ZH** 等级词元的 KL 散度损失。等级词元有五个候选值：{“bad”、“poor”、“fair”、“good”、“excellent”}。我们的软标签 ⟦SLOT_44⟧ 为每个值赋予一个真值概率。设预测概率为 ⟦SLOT_45⟧，KL 散度损失计算如下：

<!-- [原子块 · table] ℒ k ​ l = − ∑ i p i log ( p i p ​ r ​ e ​ d / p i ) . \mathcal{L}_{kl}=-\sum\nolimits_{i}p_{i}\log(p_{i}^{pred}/p_{i}). (4) -->

**EN** The predicted probabilities, ⟦SLOT_46⟧, are obtained by applying a softmax activation function on model’s output logits. Note that during training, this softmax function is applied across all textual tokens, not just across the five predefined levels. This approach encourages the model to reduce the possibilities of textual tokens outside the five levels.

**ZH** 预测概率 ⟦SLOT_46⟧ 由对模型输出 logits 施加 softmax 激活函数得到。注意训练时该 softmax 函数作用于所有文本词元，而非仅五个预定义等级。这一做法促使模型降低五个等级之外文本词元的概率。

**EN** The two terms of losses, ⟦SLOT_47⟧ and ⟦SLOT_48⟧, are both auto-regressive losses, and thus can be easily combined. During training, the cross-entropy loss, ⟦SLOT_49⟧, will decrease near to 0 fast, since it is quite easy to optimize by simply remembering the response template “The quality of this image is”.

**ZH** 两项损失 ⟦SLOT_47⟧ 与 ⟦SLOT_48⟧ 都是自回归损失，因而可以方便地组合。训练过程中，交叉熵损失 ⟦SLOT_49⟧ 会迅速下降到接近 0，因为只需记住回答模板“The quality of this image is”就很容易优化它。

**EN** 4.2 Score Estimation during Inference

**ZH** 4.2 推理时的分数估计

**EN** During inference, using the model-predicted probabilities of the five levels, ⟦SLOT_50⟧, we can estimate the expectation and variance of the score distribution the same as Eq. 3:

**ZH** 推理时，利用模型预测的五个等级概率 ⟦SLOT_50⟧，我们可以按与式 3 相同的方式估计分数分布的期望与方差：

<!-- [原子块 · table] μ p ​ r ​ e ​ d = ∑ i p i p ​ r ​ e ​ d ​ c i , ( σ p ​ r ​ e ​ d ) 2 = ∑ i p i p ​ r ​ e ​ d ​ ( c i − μ p ​ r ​ e ​ d ) 2 . \mu^{pred}=\sum\nolimits_{i}p_{i}^{pred}c_{i},\hskip 8.50012pt(\sigma^{pre -->

**EN** Here we follow Q-Align [70] to apply a close-set softmax on the five levels to obtain the probabilities, ⟦SLOT_51⟧, to prevent the influence of other textual tokens. Our statistics in Tab. A2 reveal that the trained MLLM will always predict the five levels, thus applying softmax on either the five levels or all textual tokens yields nearly identical results. As given in Tab. 5, our predicted score distribution, ⟦SLOT_52⟧, aligns well with human annotations.

**ZH** 这里沿用 Q-Align [70]，对五个等级施加闭集 softmax 来得到概率 ⟦SLOT_51⟧，以避免其他文本词元的影响。我们在表 A2 中的统计显示，训练后的 MLLM 总是会预测这五个等级，因此对五个等级或对所有文本词元施加 softmax 得到的结果几乎相同。如表 5 所示，我们预测的分数分布 ⟦SLOT_52⟧ 与人工标注高度吻合。

<!-- [原子块 · img]  -->

**EN** Figure 5: Fidelity loss to maintain intra-dataset relationships. Consider two images, Image A and B, sampled from the same dataset. Using our distribution-based soft label, DeQA-Score predicts the expectation, ⟦SLOT_53⟧, and variance, ⟦SLOT_54⟧, of each image’s score distribution, with which we can predict the probability that Image A is better than Image B, ⟦SLOT_55⟧. This predicted probability is then used to calculate the fidelity loss with the ground-truth probability. Fidelity loss preserves intra-dataset relationships, facilitating the co-training across multiple IQA datasets.

**ZH** 图 5：用于保持数据集内部关系的保真损失。考虑从同一数据集中采样的两幅图像 A 与 B。借助我们基于分布的软标签，DeQA-Score 预测每幅图像分数分布的期望 ⟦SLOT_53⟧ 与方差 ⟦SLOT_54⟧，据此可以预测图像 A 优于图像 B 的概率 ⟦SLOT_55⟧。该预测概率随后与真值概率一起用于计算保真损失。保真损失保持了数据集内部关系，从而促进跨多个 IQA 数据集的联合训练。

**EN** 4.3 Joint Training on Multiple IQA Datasets

**ZH** 4.3 在多个 IQA 数据集上联合训练

**EN** As demonstrated in [88, 98], different IQA datasets exhibit distinct distributions. Due to this dataset variation, images from different datasets with nearly identical scores (i.e., linearly re-scaled scores) can have drastically different perceptual quality (see examples in Fig. A1). The reason is that different datasets have different reflections between quality scores and visual quality. This disparity makes it infeasible to merely regress absolute quality scores for multi-dataset co-training. To address this challenge, UNIQUE [88] applies fidelity loss [63] based on Thurstone’s model [60]. The fidelity loss is based on the principal that IQA emphasizes the ranking relationships within the same dataset, rather than the absolute values of quality scores. Specifically, two images are sampled from the same dataset, whose quality scores can be comparable. These two images are then compared using human-annotated quality scores. The fidelity loss encourages the model to learn such comparison results, which facilitates the model to focus more on the ranking relationships in each dataset, instead of the absolute values of quality scores. Thus, the fidelity loss helps multi-dataset co-training. Our soft label is naturally compatible with the fidelity loss, since our method can predict the score distribution, which is what the fidelity loss needs.

**ZH** 如 [88, 98] 所示，不同 IQA 数据集呈现不同的分布。由于这种数据集差异，来自不同数据集、分数几乎相同（即线性重标定后的分数）的图像，其感知质量可能截然不同（示例见图 A1）。原因在于不同数据集在质量分数与视觉质量之间的映射关系不同。这一差异使得仅为多数据集联合训练回归绝对质量分数变得不可行。为应对这一挑战，UNIQUE [88] 应用了基于 Thurstone 模型 [60] 的保真损失 [63]。保真损失基于这样一个原则：IQA 侧重的是同一数据集内部的排序关系，而非质量分数的绝对值。具体而言，从同一数据集中采样两幅图像，其质量分数具有可比性；随后用人工标注的质量分数对这两幅图像作比较。保真损失促使模型学习这类比较结果，使模型更关注每个数据集内的排序关系，而非质量分数的绝对值。因此，保真损失有助于多数据集联合训练。我们的软标签与保真损失天然兼容，因为我们的方法能够预测保真损失所需的分数分布。

**EN** Ground-truth construction. As shown in Fig. 5, a pair of images, Image A and B, are sampled from the same dataset. We assume that the quality scores of the two images, ⟦SLOT_56⟧, follow the Gaussian distribution with means and variances collected by subjective testing, i.e., ⟦SLOT_57⟧. Assuming that their quality scores are uncorrelated, the score difference, ⟦SLOT_58⟧, also follows a Gaussian distribution, ⟦SLOT_59⟧. Then the possibility that Image A has a better perceptual quality than Image B can be calculated as:

**ZH** 真值构造。如图 5 所示，从同一数据集中采样一对图像 A 与 B。我们假定两幅图像的质量分数 ⟦SLOT_56⟧ 服从以主观测试收集到的均值与方差构成的高斯分布，即 ⟦SLOT_57⟧。假定二者质量分数互不相关，则分数之差 ⟦SLOT_58⟧ 也服从高斯分布 ⟦SLOT_59⟧。那么，图像 A 的感知质量优于图像 B 的可能性可计算为：

<!-- [原子块 · table] p ⁡ ( A > B ) = p ⁡ ( x A > x B ) = Φ ⁡ ( μ A − μ B σ A 2 + σ B 2 ) , p(A>B)=p(x_{A}>x_{B})=\Phi\left(\frac{\mu_{A}-\mu_{B}}{\sqrt{\sigma_{A}^{2}+\sigma_{B}^{2}}}\right), (6) -->

**EN** where ⟦SLOT_60⟧ is the Gaussian cumulative distribution function.

**ZH** 其中 ⟦SLOT_60⟧ 为高斯累积分布函数。

**EN** Model prediction. As described in Sec. 4.2, our model can predict the expectation and variance of the score distribution. Denoting the predicted expectation and variance of two images as ⟦SLOT_61⟧, ⟦SLOT_62⟧, ⟦SLOT_63⟧, ⟦SLOT_64⟧, same to Eq. 6, we can predict the possibility of Image A surpassing Image B in perceptual quality as:

**ZH** 模型预测。如第 4.2 节所述，我们的模型可以预测分数分布的期望与方差。记两幅图像的预测期望与方差为 ⟦SLOT_61⟧、⟦SLOT_62⟧、⟦SLOT_63⟧、⟦SLOT_64⟧，与式 6 相同，我们可以预测图像 A 在感知质量上超过图像 B 的可能性：

<!-- [原子块 · table] p p ​ r ​ e ​ d ​ ( A > B ) = Φ ⁡ ( μ A p ​ r ​ e ​ d − μ B p ​ r ​ e ​ d ( σ A p ​ r ​ e ​ d ) 2 + ( σ B p ​ r ​ e ​ d ) 2 ) . p^{pred}(A>B)=\Phi\left(\frac{\mu_{A}^{pred}-\mu_{B}^{pred}}{\sqrt{(\sig -->

**EN** Training with fidelity loss. Following [88], we choose fidelity loss as the similarity measure to train the model as:

**ZH** 用保真损失训练。沿用 [88]，我们选取保真损失作为相似度度量来训练模型：

<!-- [原子块 · table] ℒ f ​ d \displaystyle\mathcal{L}_{fd} = 1 − p ⁡ ( A > B ) ​ p p ​ r ​ e ​ d ​ ( A > B ) \displaystyle=1-\sqrt{p(A>B)p^{pred}(A>B)} − ( 1 − p ⁡ ( A > B ) ) ​ ( 1 − p p ​ r ​ e ​ d ​ ( A > B ) ) . \disp -->

**EN** Adding two auto-regressive losses, the final training loss is:

**ZH** 再加上两项自回归损失，最终的训练损失为：

<!-- [原子块 · table] ℒ = ℒ f ​ d + γ ⁡ ( ℒ c ​ e + ℒ k ​ l ) , \mathcal{L}=\mathcal{L}_{fd}+\gamma(\mathcal{L}_{ce}+\mathcal{L}_{kl}), (9) -->

**EN** where ⟦SLOT_65⟧ is a weighting term to adjust the loss scale.

**ZH** 其中 ⟦SLOT_65⟧ 是用于调整损失量级的权重项。

**EN** Table 3: Score regression results of single-dataset training with the PLCC / SRCC metrics. All methods except handcrafted ones are trained on the KonIQ dataset. DeQA-Score outperforms all baseline methods across nearly all benchmarks.

**ZH** 表 3：单数据集训练的分数回归结果（PLCC / SRCC 指标）。除手工设计方法外，所有方法均在 KonIQ 数据集上训练。DeQA-Score 在几乎所有基准上都优于所有基线方法。

<!-- [原子块 · table] Category Methods KonIQ SPAQ KADID PIPAL LIVE-Wild AGIQA-3K CSIQ FLIVE Handcrafted NIQE [ 41 ] 0.533 / 0.530 0.679 / 0.664 0.468 / 0.405 0.195 / 0.161 0.493 / 0.449 0.560 / 0.533 0.718 / 0.628 0.147 /  -->

**EN** Table 4: Score regression results of co-training on multiple IQA datasets with the PLCC / SRCC metrics. Our DeQA-Score consistently surpasses the baseline method, Q-Align, across all benchmarks with different training combinations.

**ZH** 表 4：在多个 IQA 数据集上联合训练的分数回归结果（PLCC / SRCC 指标）。在不同的训练组合下，我们的 DeQA-Score 在所有基准上都持续优于基线方法 Q-Align。

<!-- [原子块 · table] # Trained on Methods KonIQ SPAQ KADID PIPAL LIVE-Wild AGIQA-3K TID2013 CSIQ 0 KonIQ, SPAQ Q-Align [ 70 ] 0.943 / 0.940 0.933 / 0.931 0.692 / 0.708 0.401 / 0.411 0.883 / 0.879 0.795 / 0.727 0.671 / 0.5 -->

**EN** 5 Experiments

**ZH** 5 实验

**EN** 5.1 Datasets, Baselines, Metrics, and Details

**ZH** 5.1 数据集、基线、指标与细节

**EN** Datasets. For a comprehensive evaluation, we include a wide range of IQA datasets: (a) in-the-wild images: KonIQ [21], SPAQ [17], LIVE-Wild [18], and FLIVE [78]; (b) synthetic distortions: KADID [31], TID2013 [47], and CSIQ [29]; (c) model-processed distortions: PIPAL [24]; (d) AI-generated images: AGIQA-3K [30]. Among these datasets, KonIQ, SPAQ, KADID, and PIPAL are split into training and test sets. Other datasets are used to assess the out-of-distribution generalization ability. The Mean Opinion Scores (MOS) of these datasets are normalized to the range of [1,5], with the variances normalized accordingly.

**ZH** 数据集。为作全面评估，我们纳入了广泛的 IQA 数据集：（a）真实场景图像：KonIQ [21]、SPAQ [17]、LIVE-Wild [18] 与 FLIVE [78]；（b）合成失真：KADID [31]、TID2013 [47] 与 CSIQ [29]；（c）模型处理失真：PIPAL [24]；（d）AI 生成图像：AGIQA-3K [30]。其中 KonIQ、SPAQ、KADID 与 PIPAL 被划分为训练集与测试集，其余数据集用于评估分布外泛化能力。这些数据集的平均意见分数（MOS）被归一化到 [1,5] 区间，方差也相应归一化。

**EN** Baseline methods. To demonstrate the effectiveness of our distribution-based soft label, we primarily compare with Q-Align [70], which utilizes the one-hot label. The base models for DeQA-Score and Q-Align are kept identical for fair comparison. We also include previous IQA methods as baselines, including handcrafted methods: NIQE [41] and BRISQUE [40], and deep-learning-based methods: NIMA [57], HyperIQA [55], DBCNN [87], MUSIQ [26], CLIP-IQA+ [64], ManIQA [73], and Compare2Score [98].

**ZH** 基线方法。为证明我们基于分布的软标签的有效性，我们主要与使用 one-hot 标签的 Q-Align [70] 作比较。为保证公平比较，DeQA-Score 与 Q-Align 使用相同的基座模型。我们还纳入了此前的 IQA 方法作为基线，包括手工设计方法 NIQE [41] 与 BRISQUE [40]，以及基于深度学习的方法 NIMA [57]、HyperIQA [55]、DBCNN [87]、MUSIQ [26]、CLIP-IQA+ [64]、ManIQA [73] 与 Compare2Score [98]。

**EN** Metrics. Following [26, 70, 73], we use the Pearson Linear Correlation Coefficient (PLCC) and Spearman Rank-order Correlation Coefficient (SRCC) as metrics to evaluate the score regression performance. Additionally, we employ KL divergence, JS divergence, and Wasserstein distance to assess the results of score distribution prediction.

**ZH** 指标。沿用 [26, 70, 73]，我们使用皮尔逊线性相关系数（PLCC）与斯皮尔曼秩相关系数（SRCC）评估分数回归性能。此外，我们采用 KL 散度、JS 散度与 Wasserstein 距离评估分数分布预测的结果。

**EN** Implementation details. We use mPLUG-Owl2 [75] as our base model, with a CLIP-pretrained ViT-L [49] as the image encoder, a six-layer Q-Former as the visual abstractor, and LLaMA-2-7B [62] as the LLM. The number of visual tokens output by the vision abstractor is set to 64, and the hidden dimension of LLM is 4096. The pretrained weights of mPLUG-Owl2 are used for model initialization. The weighting term ⟦SLOT_66⟧ is empirically set to 0.05, adjusting the two loss terms roughly to the same scale. We adopt AdamW [23] as the optimizer. The initial learning rate is set to 2e-5 and decays gradually using the cosine decay strategy. Our model is trained with a batch size of 64 for 3 epochs. Using 8 NVIDIA RTX A6000 GPUs, the training process on KonIQ dataset is completed in around 1.5 hours.

**ZH** 实现细节。我们使用 mPLUG-Owl2 [75] 作为基座模型，以 CLIP 预训练的 ViT-L [49] 作为图像编码器，六层 Q-Former 作为视觉抽象器，LLaMA-2-7B [62] 作为 LLM。视觉抽象器输出的视觉词元数设为 64，LLM 的隐藏维度为 4096。模型用 mPLUG-Owl2 的预训练权重初始化。权重项 ⟦SLOT_66⟧ 经验性地设为 0.05，使两项损失大致处于同一量级。我们采用 AdamW [23] 作为优化器，初始学习率设为 2e-5，并以余弦衰减策略逐步衰减。模型以批大小 64 训练 3 轮。使用 8 张 NVIDIA RTX A6000 GPU，在 KonIQ 数据集上的训练过程约 1.5 小时完成。

**EN** 5.2 Results of Score Regression

**ZH** 5.2 分数回归结果

**EN** Score regression results of single-dataset training. We first train our model on a single dataset, i.e., KonIQ, and then evaluate the model on both in-distribution and out-of-distribution datasets, following [28, 70]. The score regression results are shown in Tab. 3. On the in-distribution KonIQ test set, our model achieves superior score regression results compared to all baseline methods, e.g., a 1.3% improvement in PLCC over Q-Align. Furthermore, on out-of-distribution datasets, our DeQA-Score maintains its advantage with the best overall results across nearly all benchmarks, e.g., a 4.6% improvement in PLCC on LIVE-Wild. These findings confirm the effectiveness of our method.

**ZH** 单数据集训练的分数回归结果。我们首先在单个数据集（即 KonIQ）上训练模型，随后沿用 [28, 70] 在分布内与分布外数据集上评估模型。分数回归结果见表 3。在分布内的 KonIQ 测试集上，我们的模型取得了优于所有基线方法的分数回归结果，例如相比 Q-Align 在 PLCC 上提升 1.3%。此外，在分布外数据集上，DeQA-Score 保持了优势，在几乎所有基准上都取得最佳的整体结果，例如在 LIVE-Wild 上 PLCC 提升 4.6%。这些发现证实了我们方法的有效性。

**EN** However, we observe that all models perform poorly on the PIPAL dataset. For instance, our best results reach only 0.462 on PLCC. The main reason is the distortion gap between the training dataset, KonIQ (in-the-wild distortions), and PIPAL (model-processed distortions). This highlights the necessity of co-training with multiple IQA datasets containing various distortion types. This observation motivates our subsequent experiments on multi-dataset co-training.

**ZH** 然而我们观察到，所有模型在 PIPAL 数据集上表现都较差。例如我们的最佳结果在 PLCC 上也仅达 0.462。主要原因是训练数据集 KonIQ（真实场景失真）与 PIPAL（模型处理失真）之间的失真鸿沟。这凸显了用包含多种失真类型的多个 IQA 数据集做联合训练的必要性，也促成了我们后续的多数据集联合训练实验。

**EN** Score regression results of multi-dataset co-training. As discussed above, co-training on multiple IQA datasets is necessary to obtain a unified model for various categories of distortions. Therefore, we conduct multi-dataset co-training experiments in Tab. 4. First, our DeQA-Score consistently outperforms Q-Align across different training combinations. The performance gain attributes to both the soft label and fidelity loss, as confirmed in Tab. 6. Second, comparing #0 to #1, when KADID (synthetic distortions) is added to the training set, the performance on TID2013 and CSIQ (both synthetic distortions) improves significantly (e.g., 33.1% in SRCC on TID2013), underscoring that distortion type is a major gap between training and testing. Third, from #1 to #2, adding PIPAL for training greatly enhances the results on PIPAL (from 0.495 to 0.724 in PLCC) but reduces the performance on several other datasets, e.g., from 0.900 to 0.863 in PLCC on CSIQ. This performance decline is likely due to the unique nature of model-processed distortions in PIPAL, which differ greatly from other distortions. Finally, despite never trained on AI-generated images, DeQA-Score performs well on AGIQA-3K with around 0.8 PLCC, reflecting the generalization ability enabled by MLLMs’ broad pre-training.

**ZH** 多数据集联合训练的分数回归结果。如上所述，为获得面向各类失真的统一模型，在多个 IQA 数据集上联合训练是必要的。因此我们在表 4 中开展了多数据集联合训练实验。第一，在不同的训练组合下，我们的 DeQA-Score 持续优于 Q-Align；性能增益来自软标签与保真损失两方面，表 6 证实了这一点。第二，比较 #0 与 #1，当把 KADID（合成失真）加入训练集后，在 TID2013 与 CSIQ（均为合成失真）上的性能显著提升（例如在 TID2013 上 SRCC 提升 33.1%），说明失真类型是训练与测试之间的主要鸿沟。第三，从 #1 到 #2，加入 PIPAL 训练大幅提升了 PIPAL 上的结果（PLCC 从 0.495 提升到 0.724），却降低了若干其他数据集上的性能，例如在 CSIQ 上 PLCC 从 0.900 降至 0.863。这一性能下降可能源于 PIPAL 中模型处理失真的独特性——它与其他失真差异很大。最后，尽管从未在 AI 生成图像上训练，DeQA-Score 在 AGIQA-3K 上仍取得约 0.8 的 PLCC，体现了 MLLM 广博预训练所带来的泛化能力。

**EN** More results on AIGC images are provided in Tab. A4.

**ZH** 关于 AIGC 图像的更多结果见表 A4。

**EN** 5.3 Results of Score Distribution Prediction

**ZH** 5.3 分数分布预测结果

**EN** Table 5: Score distribution prediction results with JS divergence / Wasserstein distance between the predicted Gaussian distribution and the human labeled Gaussian distribution as metrics. Models are trained on the KonIQ, SPAQ, and KADID datasets. DeQA-Score achieves a much closer alignment with human annotations.

**ZH** 表 5：分数分布预测结果，以预测高斯分布与人工标注高斯分布之间的 JS 散度 / Wasserstein 距离为指标。模型在 KonIQ、SPAQ 与 KADID 数据集上训练。DeQA-Score 与人工标注的吻合度要高得多。

<!-- [原子块 · table] Datasets Q-Align [ 70 ] DeQA-Score (Ours) KonIQ 0.415 / 0.611 0.014 / 0.186 SPAQ 0.192 / 0.455 0.070 / 0.332 KADID 0.519 / 0.723 0.029 / 0.304 LIVE-Wild 0.254 / 0.642 0.052 / 0.417 AGIQA-3K 0.558 / 0. -->

<!-- [原子块 · img]  -->

**EN** Figure 6: Qualitative results on KonIQ, SPAQ, AGIQA-3K, and KADID datasets. DeQA-Score predicts more accurate quality scores with more reasonable logits. Also, our method generates a score distribution that aligns better with humans, i.e., smaller KL divergence. However, Q-Align, which is trained on one-hot label, is more likely to predict a single label, resulting in higher KL divergence.

**ZH** 图 6：在 KonIQ、SPAQ、AGIQA-3K 与 KADID 数据集上的定性结果。DeQA-Score 以更合理的 logits 预测出更准确的质量分数；此外，我们的方法生成的分数分布与人类更吻合，即 KL 散度更小。相比之下，用 one-hot 标签训练的 Q-Align 更倾向于预测单一标签，导致 KL 散度更高。

**EN** Table 6: Ablation studies on soft label and fidelity loss with PLCC / SRCC metrics. Models are trained on KonIQ, SPAQ, and KADID.

**ZH** 表 6：关于软标签与保真损失的消融研究（PLCC / SRCC 指标）。模型在 KonIQ、SPAQ 与 KADID 上训练。

<!-- [原子块 · table] # One-hot Soft Uncertainty Fidelity KonIQ SPAQ KADID PIPAL LIVE-Wild AGIQA-3K TID2013 CSIQ 0 ✔ 0.945 / 0.938 0.933 / 0.931 0.935 / 0.934 0.409 / 0.420 0.887 / 0.883 0.788 / 0.733 0.829 / 0.808 0.876 / -->

**EN** Table 7: Effects of different level texts with PLCC / SRCC metrics. Models are trained on the KonIQ, SPAQ, and KADID datasets.

**ZH** 表 7：不同等级文本的影响（PLCC / SRCC 指标）。模型在 KonIQ、SPAQ 与 KADID 数据集上训练。

<!-- [原子块 · table] Category Level Texts KonIQ SPAQ KADID PIPAL LIVE-Wild AGIQA-3K TID2013 CSIQ Common exce. / good / far / poor / bad 0.957 / 0.944 0.938 / 0.934 0.955 / 0.953 0.495 / 0.496 0.900 / 0.887 0.808 / 0.745 0 -->

**EN** As stated in Sec. 4.2, the MLLM-output probabilities allow us to predict a score distribution, which can be evaluated against the human labeled ground-truth distribution. We calculate the distance between these two distributions and present the results in Tab. 5. The results illustrate that our predicted score distribution aligns much better with humans than Q-Align. As shown in Fig. 6, Q-Align tends to predict a single level token, bringing a quite small predicted variance, which compromises the distribution metrics.

**ZH** 如第 4.2 节所述，MLLM 输出的概率使我们能够预测分数分布，并可将其与人工标注的真值分布作比较。我们计算这两个分布之间的距离，结果见表 5。结果表明，我们预测的分数分布比 Q-Align 与人类的吻合度高得多。如图 6 所示，Q-Align 倾向于预测单一等级词元，导致预测方差很小，损害了分布指标。

**EN** Qualitative results are shown in Fig. 6. Across different image types: in-the-wild images (Fig. 6ab), AI-generated images (Fig. 6c), or synthetic distortions (Fig. 6d), and for varying quality levels: high-quality (Fig. 6ac), fair-quality (Fig. 6b), or poor-quality images (Fig. 6d), our method consistently predicts accurate quality scores. Additionally, our DeQA-Score provides a score distribution that aligns more closely with humans with smaller KL divergence. In contrast, Q-Align, which is trained with one-hot labels, tends to predict a single label, resulting in higher KL divergence.

**ZH** 定性结果如图 6 所示。跨越不同的图像类型——真实场景图像（图 6ab）、AI 生成图像（图 6c）或合成失真（图 6d），以及不同的质量水平——高质量（图 6ac）、中等质量（图 6b）或低质量（图 6d）图像，我们的方法都一致地预测出准确的质量分数。此外，DeQA-Score 提供的分数分布与人类更接近，KL 散度更小。相比之下，用 one-hot 标签训练的 Q-Align 倾向于预测单一标签，导致 KL 散度更高。

**EN** 5.4 Ablation Studies

**ZH** 5.4 消融研究

**EN** Table 8: Inference latency & throughput on RTX A6000 GPU.

**ZH** 表 8：在 RTX A6000 GPU 上的推理延迟与吞吐。

<!-- [原子块 · table] Batch Size 1 2 4 8 16 64 256 Latency ( s ) 0.089 0.121 0.182 0.315 0.588 2.114 7.929 Throughput ( image/s ) 11.24 16.53 21.98 25.40 27.21 30.27 32.29 -->

**EN** Effectiveness of soft label and fidelity loss is studied and shown in Tab. 6. In #1, “Uncertainty” is utilized to verify the effects of adding annotation variances without considering the score distortion. We directly append uncertainty within the responses, i.e., “The quality of this image is ⟦SLOT_67⟧level⟦SLOT_68⟧ with ⟦SLOT_69⟧uncertainty_level⟦SLOT_70⟧ uncertainty”. The ⟦SLOT_71⟧uncertainty_level⟦SLOT_72⟧ has five possible values: {“minimal”, “low”, “moderate”, “high”, “severe”}, derived by the one-hot discretization. In #2, model trained on one-hot label can not predict a reliable variance, thus we employ binary fidelity loss [89], which does not require predicted variance.

**ZH** 软标签与保真损失的有效性研究见表 6。在 #1 中，使用“Uncertainty”来验证在不考虑分数分布的情况下加入标注方差的效果：我们直接在回答中追加不确定性，即“The quality of this image is ⟦SLOT_67⟧level⟦SLOT_68⟧ with ⟦SLOT_69⟧uncertainty_level⟦SLOT_70⟧ uncertainty”。⟦SLOT_71⟧uncertainty_level⟦SLOT_72⟧ 有五个可能取值：{“minimal”、“low”、“moderate”、“high”、“severe”}，由 one-hot 离散化得到。在 #2 中，用 one-hot 标签训练的模型无法预测可靠的方差，因此我们采用不需要预测方差的二值保真损失 [89]。

**EN** Several conclusions can be drawn from Tab. 6. First, comparing #0 with #3, our soft label significantly outperforms the one-hot label across all benchmarks, validating its effectiveness. Second, from #3 to #4, the performance of our soft label further improves when combined with the fidelity loss. Third, comparing #0 with #2, the one-hot label does not incorporate well with the fidelity loss, as it lacks score distribution information. Finally, from #0 to #1, simply adding uncertainty without considering score distribution does not yield stable or significant improvements.

**ZH** 从表 6 可以得出若干结论。第一，比较 #0 与 #3，我们的软标签在所有基准上都显著优于 one-hot 标签，验证了其有效性。第二，从 #3 到 #4，我们的软标签与保真损失结合后性能进一步提升。第三，比较 #0 与 #2，one-hot 标签与保真损失结合得不好，因为它缺乏分数分布信息。最后，从 #0 到 #1，仅仅加入不确定性而不考虑分数分布，并不能带来稳定或显著的改进。

**EN** Effects of different level texts are studied in Tab. 7. Beside the commonly used level texts, we consider five alternatives: (a) random sorted common texts; (b) reversed common texts; (c) simple numbers like one, two, etc.; (d) irrelevant words about vehicle; (e) a mixture of various types. The results indicate that common level texts achieve the best performance, as they align closely with the MLLMs’ pre-training. Interestingly, with random sorted / reversed texts, even a mixture of various level texts, which are inconsistent with MLLMs’ prior knowledge, our model still learns these newly defined relationships and performs well. This shows the robust adaptability of MLLM-based IQA models.

**ZH** 表 7 研究了不同等级文本的影响。除常用的等级文本外，我们考虑了五种替代方案：（a）随机排序的常用文本；（b）反转的常用文本；（c）one、two 等简单数字；（d）与车辆无关的词；（e）多种类型的混合。结果表明，常用等级文本取得了最佳性能，因为它们与 MLLM 的预训练高度契合。有意思的是，即便使用随机排序/反转的文本，甚至是多种等级文本的混合——这些都与 MLLM 的先验知识不一致——我们的模型仍能学到这些新定义的关系并表现良好。这体现了基于 MLLM 的 IQA 模型具有很强的适应能力。

**EN** Ablation studies on level number and training / fixing components are provided in Tabs. A7 and A7, respectively.

**ZH** 关于等级数量以及训练/固定组件的消融研究分别见表 A7 与 A7。

**EN** 5.5 Inference Latency

**ZH** 5.5 推理延迟

**EN** We test the inference latency on one single RTX A6000 GPU. As shown in Tab. 8, with the optimal GPU utilization (i.e., batch size 256), our DeQA-Score can process as many as 32.29 images per second in average. This high throughput emphasizes its suitability for real-time deployment.

**ZH** 我们在单张 RTX A6000 GPU 上测试推理延迟。如表 8 所示，在最优 GPU 利用率（即批大小 256）下，我们的 DeQA-Score 平均每秒可处理多达 32.29 张图像。这一高吞吐说明它适合实时部署。

**EN** 6 Conclusions

**ZH** 6 结论

**EN** We develop DeQA-Score as a pioneering MLLM-based image quality scorer, empowered by distribution-based soft labels and fidelity loss, capable of both score regression and score distribution prediction, highlighting the importance of quality score distribution in MLLM-based IQA methods.

**ZH** 我们开发了 DeQA-Score——一个开创性的基于 MLLM 的图像质量评分器，它由基于分布的软标签与保真损失驱动，既能做分数回归，也能做分数分布预测，凸显了质量分数分布在基于 MLLM 的 IQA 方法中的重要性。

**EN** Acknowledgement. This work was sponsored by RGC Early Career Scheme (ECS) No. 24209224, National Natural Science Foundation of China (Grant No.62276251), and the Joint Lab of CAS-HK.

**ZH** 致谢。本工作受香港研究资助局优配研究金（ECS）No. 24209224、国家自然科学基金（批准号 62276251）与中科院—香港联合实验室资助。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] [1] J. Achiam, S. Adler, S. Agarwal, L. Ahmad, I. Akkaya, F. L. Aleman, D. Almeida, J. Altenschmidt, S. Altman, S. Anadkat, et al. (2023) GPT-4 technical report . arXiv preprint arXiv:2303.08774 . Cit -->

<!-- [原子块 · verbatim] [2] H. Agrawal, K. Desai, Y. Wang, X. Chen, R. Jain, M. Johnson, D. Batra, D. Parikh, S. Lee, and P. Anderson (2019) Nocaps: novel object captioning at scale . In ICCV , Cited by: §2 . -->

<!-- [原子块 · verbatim] [3] J. Alayrac, J. Donahue, P. Luc, A. Miech, I. Barr, Y. Hasson, K. Lenc, A. Mensch, K. Millican, M. Reynolds, et al. (2022) Flamingo: a visual language model for few-shot learning . In NeurIPS , Cit -->

<!-- [原子块 · verbatim] [4] S. Bosse, D. Maniry, K. Müller, T. Wiegand, and W. Samek (2018) Deep neural networks for no-reference and full-reference image quality assessment . IEEE TIP . Cited by: §2 . -->

<!-- [原子块 · verbatim] [5] X. Cai, Z. You, H. Zhang, W. Liu, J. Gu, and T. Xue (2024) PhoCoLens: photorealistic and consistent reconstruction in lensless imaging . In NeurIPS , Cited by: §1 . -->

<!-- [原子块 · verbatim] [6] Y. Cao, Z. Wan, D. Ren, Z. Yan, and W. Zuo (2022) Incorporating semi-supervised and positive-unlabeled learning for boosting full reference image quality assessment . In CVPR , Cited by: §2 . -->

<!-- [原子块 · verbatim] [7] C. Chen, Y. Sensen, H. Wu, L. Liao, Z. Zhang, A. Wang, W. Sun, Q. Yan, and W. Lin (2024) Q-Ground: image quality grounding with large multi-modality models . In ACM MM , Cited by: §1 , §2 . -->

<!-- [原子块 · verbatim] [8] D. Chen, T. Wu, K. Ma, and L. Zhang (2025) Toward generalized image quality assessment: relaxing the perfect reference quality assumption . In CVPR , Cited by: §2 . -->

<!-- [原子块 · verbatim] [9] X. Chen, H. Fang, T. Lin, R. Vedantam, S. Gupta, P. Dollár, and C. L. Zitnick (2015) Microsoft coco captions: data collection and evaluation server . arXiv preprint arXiv:1504.00325 . Cited by: §2 -->

<!-- [原子块 · verbatim] [10] Z. Chen, W. Sun, H. Wu, Z. Zhang, J. Jia, R. Huang, X. Min, G. Zhai, and W. Zhang (2024) Study of subjective and objective naturalness assessment of ai-generated images . IEEE TCSVT . Cited by: A -->

<!-- [原子块 · verbatim] [11] Z. Chen, Z. He, Z. Lu, X. Sun, and Z. Lu (2024) Prompt-based test-time real image dehazing: a novel pipeline . In ECCV , Cited by: §1 . -->

<!-- [原子块 · verbatim] [12] Z. Chen, Y. Wang, X. Cai, Z. You, Z. Lu, F. Zhang, S. Guo, and T. Xue (2025) UltraFusion: ultra high dynamic imaging using exposure fusion . In CVPR , Cited by: §1 . -->

<!-- [原子块 · verbatim] [13] W. Chiang, Z. Li, Z. Lin, Y. Sheng, Z. Wu, H. Zhang, L. Zheng, S. Zhuang, Y. Zhuang, J. E. Gonzalez, et al. (2023) Vicuna: an open-source chatbot impressing gpt-4 with 90%* chatgpt quality . http -->

<!-- [原子块 · verbatim] [14] W. Dai, J. Li, D. Li, A. M. H. Tiong, J. Zhao, W. Wang, B. Li, P. N. Fung, and S. Hoi (2023) InstructBLIP: towards general-purpose vision-language models with instruction tuning . In NeurIPS , Ci -->

<!-- [原子块 · verbatim] [15] K. Ding, Y. Liu, X. Zou, S. Wang, and K. Ma (2021) Locally adaptive structure and texture similarity for image quality assessment . In ACM MM , Cited by: §2 . -->

<!-- [原子块 · verbatim] [16] K. Ding, K. Ma, S. Wang, and E. P. Simoncelli (2020) Image quality assessment: unifying structure and texture similarity . IEEE TPAMI . Cited by: §2 . -->

<!-- [原子块 · verbatim] [17] Y. Fang, H. Zhu, Y. Zeng, K. Ma, and Z. Wang (2020) Perceptual quality assessment of smartphone photography . In CVPR , Cited by: §1 , §2 , §3.2 , Table 1 , §5.1 . -->

<!-- [原子块 · verbatim] [18] D. Ghadiyaram and C. B. Alan (2015) LIVE in the wild image quality challenge database . http://live.ece.utexas.edu/research/ChallengeDB/index.html . Cited by: §1 , §5.1 . -->

<!-- [原子块 · verbatim] [19] A. Ghildyal and F. Liu (2022) Shift-tolerant perceptual similarity metric . In ECCV , Cited by: §2 . -->

<!-- [原子块 · verbatim] [20] Y. Goyal, T. Khot, D. Summers-Stay, D. Batra, and D. Parikh (2017) Making the V in VQA matter: elevating the role of image understanding in visual question answering . In CVPR , Cited by: §2 . -->

<!-- [原子块 · verbatim] [21] V. Hosu, H. Lin, T. Sziranyi, and D. Saupe (2020) KonIQ-10K: an ecologically valid database for deep learning of blind image quality assessment . IEEE TIP . Cited by: §1 , §2 , §3.2 , Table 1 , § -->

<!-- [原子块 · verbatim] [22] E. J. Hu, Y. Shen, P. Wallis, Z. Allen-Zhu, Y. Li, S. Wang, L. Wang, and W. Chen (2021) LoRA: low-rank adaptation of large language models . In ICLR , Cited by: §B.2 , Table A7 , Table A7 , Appen -->

<!-- [原子块 · verbatim] [23] L. Ilya and H. Frank (2019) Decoupled weight decay regularization . In ICLR , Cited by: §B.3 , §5.1 . -->

<!-- [原子块 · verbatim] [24] G. Jinjin, C. Haoming, C. Haoyu, Y. Xiaoxing, J. S. Ren, and D. Chao (2020) PIPAL: a large-scale image quality assessment dataset for perceptual image restoration . In ECCV , Cited by: §2 , §5.1  -->

<!-- [原子块 · verbatim] [25] L. Kang, P. Ye, Y. Li, and D. Doermann (2014) Convolutional neural networks for no-reference image quality assessment . In CVPR , Cited by: §2 . -->

<!-- [原子块 · verbatim] [26] J. Ke, Q. Wang, Y. Wang, P. Milanfar, and F. Yang (2021) MUSIQ: multi-scale image quality transformer . In CVPR , Cited by: §1 , §2 , Table 3 , §5.1 , §5.1 . -->

<!-- [原子块 · verbatim] [27] T. Kudo and J. Richardson (2018) SentencePiece: a simple and language independent subword tokenizer and detokenizer for neural text processing . In Proceedings of the 2018 Conference on Empirical -->

<!-- [原子块 · verbatim] [28] D. Kwon, D. Kim, S. Ki, Y. Jo, H. Lee, and S. J. Kim (2024) ATTIQA: generalizable image quality feature extractor using attribute-aware pretraining . In ACCV , Cited by: §5.2 . -->

<!-- [原子块 · verbatim] [29] E. C. Larson and D. M. Chandler (2010) Most apparent distortion: full-reference image quality assessment and the role of strategy . Journal of electronic imaging . Cited by: §5.1 . -->

<!-- [原子块 · verbatim] [30] C. Li, Z. Zhang, H. Wu, W. Sun, X. Min, X. Liu, G. Zhai, and W. Lin (2023) AGIQA-3K: an open database for ai-generated image quality assessment . IEEE TCSVT . Cited by: Appendix C , §1 , §2 , §5. -->

<!-- [原子块 · verbatim] [31] H. Lin, V. Hosu, and D. Saupe (2019) KADID-10K: a large-scale artificially distorted iqa database . In International Conference on Quality of Multimedia Experience (QoMEX) , Cited by: §2 , §2 , § -->

<!-- [原子块 · verbatim] [32] H. Liu, C. Li, Q. Wu, and Y. J. Lee (2024) Visual instruction tuning . In NeurIPS , Cited by: §1 , §2 , §4.1 . -->

<!-- [原子块 · verbatim] [33] K. Liu, Z. Zhang, W. Li, R. Pei, F. Song, X. Liu, L. Kong, and Y. Zhang (2024) Dog-IQA: standard-guided zero-shot mllm for mix-grained image quality assessment . arXiv preprint arXiv:2410.02505 . -->

<!-- [原子块 · verbatim] [34] X. Liu, J. van de Weijer, and A. D. Bagdanov (2017) RankIQA: learning from rankings for no-reference image quality assessment . In ICCV , Cited by: §2 . -->

<!-- [原子块 · verbatim] [35] Y. Liu, H. Duan, Y. Zhang, B. Li, S. Zhang, W. Zhao, Y. Yuan, J. Wang, C. He, Z. Liu, et al. (2023) Mmbench: is your multi-modal model an all-around player? . arXiv preprint arXiv:2307.06281 . Ci -->

<!-- [原子块 · verbatim] [36] P. Lu, S. Mishra, T. Xia, L. Qiu, K. Chang, S. Zhu, O. Tafjord, P. Clark, and A. Kalyan (2022) Learn to explain: multimodal reasoning via thought chains for science question answering . In NeurIP -->

<!-- [原子块 · verbatim] [37] C. Ma, C. Yang, X. Yang, and M. Yang (2017) Learning a no-reference quality metric for single-image super-resolution . Computer Vision and Image Understanding . Cited by: §2 . -->

<!-- [原子块 · verbatim] [38] A. Masry, X. L. Do, J. Q. Tan, S. Joty, and E. Hoque (2022) ChartQA: a benchmark for question answering about charts with visual and logical reasoning . In ACL Findings , Cited by: §2 . -->

<!-- [原子块 · verbatim] [39] M. Mathew, D. Karatzas, and C. Jawahar (2021) DocVQA: a dataset for vqa on document images . In WACV , Cited by: §2 . -->

<!-- [原子块 · verbatim] [40] A. Mittal, A. K. Moorthy, and A. C. Bovik (2012) No-reference image quality assessment in the spatial domain . IEEE TIP . Cited by: §2 , Table 3 , §5.1 . -->

<!-- [原子块 · verbatim] [41] A. Mittal, R. Soundararajan, and A. C. Bovik (2012) Making a “completely blind” image quality analyzer . IEEE Sign. Process. Letters . Cited by: §1 , §2 , Table 3 , §5.1 . -->

<!-- [原子块 · verbatim] [42] A. K. Moorthy and A. C. Bovik (2010) A two-step framework for constructing blind image quality indices . IEEE Sign. Process. Letters . Cited by: §2 . -->

<!-- [原子块 · verbatim] [43] A. K. Moorthy and A. C. Bovik (2011) Blind image quality assessment: from natural scene statistics to perceptual quality . IEEE TIP . Cited by: §2 . -->

<!-- [原子块 · verbatim] [44] OpenAI (2023) GPT-4V(ision) system card . External Links: Link Cited by: §1 , §2 . -->

<!-- [原子块 · verbatim] [45] L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. Wainwright, P. Mishkin, C. Zhang, S. Agarwal, K. Slama, A. Ray, et al. (2022) Training language models to follow instructions with human feedback . In N -->

<!-- [原子块 · verbatim] [46] D. Pan, P. Shi, M. Hou, Z. Ying, S. Fu, and Y. Zhang (2018) Blind predicting similar quality map for image quality assessment . In CVPR , Cited by: §2 . -->

<!-- [原子块 · verbatim] [47] N. Ponomarenko, L. Jin, O. Ieremeiev, V. Lukin, K. Egiazarian, J. Astola, B. Vozel, K. Chehdi, M. Carli, F. Battisti, et al. (2015) Image database TID2013: peculiarities, results and perspectives -->

<!-- [原子块 · verbatim] [48] E. Prashnani, H. Cai, Y. Mostofi, and P. Sen (2018) PieAPP: perceptual image-error assessment through pairwise preference . In CVPR , Cited by: §2 . -->

<!-- [原子块 · verbatim] [49] A. Radford, J. W. Kim, C. Hallacy, A. Ramesh, G. Goh, S. Agarwal, G. Sastry, A. Askell, P. Mishkin, J. Clark, et al. (2021) Learning transferable visual models from natural language supervision . -->

<!-- [原子块 · verbatim] [50] M. A. Saad, A. C. Bovik, and C. Charrier (2012) Blind image quality assessment: a natural scene statistics approach in the dct domain . IEEE TIP . Cited by: §2 . -->

<!-- [原子块 · verbatim] [51] B. Series (2012) Methodology for the subjective assessment of the quality of television pictures . Recommendation ITU-R BT . Cited by: §3.1 . -->

<!-- [原子块 · verbatim] [52] H. Sheikh (2005) LIVE image quality assessment database release 2 . http://live.ece.utexas.edu/research/quality . Cited by: §1 , §2 . -->

<!-- [原子块 · verbatim] [53] H. R. Sheikh and A. C. Bovik (2006) Image information and visual quality . IEEE TIP . Cited by: §2 . -->

<!-- [原子块 · verbatim] [54] A. Singh, V. Natarajan, M. Shah, Y. Jiang, X. Chen, D. Batra, D. Parikh, and M. Rohrbach (2019) Towards VQA models that can read . In CVPR , Cited by: §2 . -->

<!-- [原子块 · verbatim] [55] S. Su, Q. Yan, Y. Zhu, C. Zhang, X. Ge, J. Sun, and Y. Zhang (2020) Blindly assess image quality in the wild guided by a self-adaptive hyper network . In CVPR , Cited by: §2 , Table 3 , §5.1 . -->

<!-- [原子块 · verbatim] [56] S. Sun, T. Yu, J. Xu, W. Zhou, and Z. Chen (2022) GraphIQA: learning distortion graph representations for blind image quality assessment . IEEE TMM . Cited by: §2 . -->

<!-- [原子块 · verbatim] [57] H. Talebi and P. Milanfar (2018) NIMA: neural image assessment . IEEE TIP . Cited by: Table 3 , §5.1 . -->

<!-- [原子块 · verbatim] [58] H. Tang, N. Joshi, and A. Kapoor (2011) Learning a blind measure of perceptual image quality . In CVPR , Cited by: §2 . -->

<!-- [原子块 · verbatim] [59] I. Team (2023) InternLM: a multilingual language model with progressively enhanced capabilities . https://github. com/InternLM/InternLM . Cited by: §2 . -->

<!-- [原子块 · verbatim] [60] L. L. Thurstone (1994) A law of comparative judgment . Psychological review . Cited by: §1 , §4.3 . -->

<!-- [原子块 · verbatim] [61] H. Touvron, T. Lavril, G. Izacard, X. Martinet, M. Lachaux, T. Lacroix, B. Rozière, N. Goyal, E. Hambro, F. Azhar, et al. (2023) LLaMA: open and efficient foundation language models . arXiv prepr -->

<!-- [原子块 · verbatim] [62] H. Touvron, L. Martin, K. Stone, P. Albert, A. Almahairi, Y. Babaei, N. Bashlykov, S. Batra, P. Bhargava, S. Bhosale, et al. (2023) LLaMA 2: open foundation and fine-tuned chat models . arXiv pre -->

<!-- [原子块 · verbatim] [63] M. Tsai, T. Liu, T. Qin, H. Chen, and W. Ma (2007) FRank: a ranking method with fidelity loss . In International ACM SIGIR Conference on Research and Development in Information Retrieval , Cited  -->

<!-- [原子块 · verbatim] [64] J. Wang, K. C. Chan, and C. C. Loy (2023) Exploring clip for assessing the look and feel of images . In AAAI , Cited by: §2 , Table 3 , §5.1 . -->

<!-- [原子块 · verbatim] [65] J. Wang, H. Duan, J. Liu, S. Chen, X. Min, and G. Zhai (2023) AIGCIQA2023: a large-scale image quality assessment database for ai generated images: from the perspectives of quality, authenticity  -->

<!-- [原子块 · verbatim] [66] Z. Wang, A. C. Bovik, H. R. Sheikh, and E. P. Simoncelli (2004) Image quality assessment: from error visibility to structural similarity . IEEE TIP . Cited by: §1 , §2 . -->

<!-- [原子块 · verbatim] [67] H. Wei, L. Kong, J. Chen, L. Zhao, Z. Ge, J. Yang, J. Sun, C. Han, and X. Zhang (2023) Vary: scaling up the vision vocabulary for large vision-language models . arXiv preprint arXiv:2312.06109 .  -->

<!-- [原子块 · verbatim] [68] H. Wu, Z. Zhang, E. Zhang, C. Chen, L. Liao, A. Wang, C. Li, W. Sun, Q. Yan, G. Zhai, et al. (2024) Q-Bench: a benchmark for general-purpose foundation models on low-level vision . In ICLR , Cite -->

<!-- [原子块 · verbatim] [69] H. Wu, Z. Zhang, E. Zhang, C. Chen, L. Liao, A. Wang, K. Xu, C. Li, J. Hou, G. Zhai, et al. (2024) Q-Instruct: improving low-level visual abilities for multi-modality foundation models . In CVPR  -->

<!-- [原子块 · verbatim] [70] H. Wu, Z. Zhang, W. Zhang, C. Chen, L. Liao, C. Li, Y. Gao, A. Wang, E. Zhang, W. Sun, et al. (2024) Q-Align: teaching LMMs for visual scoring via discrete text-defined levels . In ICML , Cited b -->

<!-- [原子块 · verbatim] [71] H. Wu, H. Zhu, Z. Zhang, E. Zhang, C. Chen, L. Liao, C. Li, A. Wang, W. Sun, Q. Yan, et al. (2024) Towards open-ended visual quality comparison . In ECCV , Cited by: §1 , §1 , §2 , §2 . -->

<!-- [原子块 · verbatim] [72] T. Wu, K. Ma, J. Liang, Y. Yang, and L. Zhang (2024) A comprehensive study of multimodal large language models for image quality assessment . In ECCV , Cited by: §2 . -->

<!-- [原子块 · verbatim] [73] S. Yang, T. Wu, S. Shi, S. Lao, Y. Gong, M. Cao, J. Wang, and Y. Yang (2022) MANIQA: multi-dimension attention network for no-reference image quality assessment . In CVPRW , Cited by: §2 , Table  -->

<!-- [原子块 · verbatim] [74] Q. Ye, H. Xu, G. Xu, J. Ye, M. Yan, Y. Zhou, J. Wang, A. Hu, P. Shi, Y. Shi, et al. (2023) mPLUG-Owl: modularization empowers large language models with multimodality . arXiv preprint arXiv:2304. -->

<!-- [原子块 · verbatim] [75] Q. Ye, H. Xu, J. Ye, M. Yan, A. Hu, H. Liu, Q. Qian, J. Zhang, and F. Huang (2024) mPLUG-Owl2: revolutionizing multi-modal large language model with modality collaboration . In CVPR , Cited by: § -->

<!-- [原子块 · verbatim] [76] G. Yin, W. Wang, Z. Yuan, C. Han, W. Ji, S. Sun, and C. Wang (2022) Content-variant reference image quality assessment via knowledge distillation . In AAAI , Cited by: §2 . -->

<!-- [原子块 · verbatim] [77] Z. Yin, J. Wang, J. Cao, Z. Shi, D. Liu, M. Li, L. Sheng, L. Bai, X. Huang, Z. Wang, et al. (2023) LAMM: language-assisted multi-modal instruction-tuning dataset, framework, and benchmark . In Ne -->

<!-- [原子块 · verbatim] [78] Z. Ying, H. Niu, P. Gupta, D. Mahajan, D. Ghadiyaram, and A. Bovik (2020) From patches to pictures (PaQ-2-PiQ): mapping the perceptual space of picture quality . In CVPR , Cited by: §2 , §5.1 . -->

<!-- [原子块 · verbatim] [79] Z. You, J. Gu, Z. Li, X. Cai, K. Zhu, C. Dong, and T. Xue (2024) Descriptive image quality assessment in the wild . arXiv preprint arXiv:2405.18842 . Cited by: §1 , §1 , §2 . -->

<!-- [原子块 · verbatim] [80] Z. You, Z. Li, J. Gu, Z. Yin, T. Xue, and C. Dong (2024) Depicting beyond scores: advancing image quality assessment through multi-modal language models . In ECCV , Cited by: §1 , §1 , §2 . -->

<!-- [原子块 · verbatim] [81] P. Young, A. Lai, M. Hodosh, and J. Hockenmaier (2014) From image descriptions to visual denotations: new similarity metrics for semantic inference over event descriptions . Transactions of the A -->

<!-- [原子块 · verbatim] [82] L. Zhang, L. Zhang, X. Mou, and D. Zhang (2011) FSIM: a feature similarity index for image quality assessment . IEEE TIP . Cited by: §2 . -->

<!-- [原子块 · verbatim] [83] P. Zhang, X. Dong, B. Wang, Y. Cao, C. Xu, L. Ouyang, Z. Zhao, S. Ding, S. Zhang, H. Duan, W. Zhang, H. Yan, X. Zhang, W. Li, J. Li, K. Chen, C. He, X. Zhang, Y. Qiao, D. Lin, and J. Wang (2023)  -->

<!-- [原子块 · verbatim] [84] R. Zhang, J. Han, C. Liu, A. Zhou, P. Lu, Y. Qiao, H. Li, and P. Gao (2024) LLaMA-Adapter: efficient fine-tuning of large language models with zero-initialized attention . In ICLR , Cited by: §2  -->

<!-- [原子块 · verbatim] [85] R. Zhang, P. Isola, A. A. Efros, E. Shechtman, and O. Wang (2018) The unreasonable effectiveness of deep features as a perceptual metric . In CVPR , Cited by: §1 , §2 . -->

<!-- [原子块 · verbatim] [86] W. Zhang, D. Li, C. Ma, G. Zhai, X. Yang, and K. Ma (2022) Continual learning for blind image quality assessment . IEEE TPAMI . Cited by: §2 . -->

<!-- [原子块 · verbatim] [87] W. Zhang, K. Ma, J. Yan, D. Deng, and Z. Wang (2020) Blind image quality assessment using a deep bilinear convolutional neural network . IEEE TCSVT . Cited by: Table 3 , §5.1 . -->

<!-- [原子块 · verbatim] [88] W. Zhang, K. Ma, G. Zhai, and X. Yang (2021) Uncertainty-aware blind image quality assessment in the laboratory and wild . IEEE TIP . Cited by: §1 , §2 , §3.2 , §4.3 , §4.3 . -->

<!-- [原子块 · verbatim] [89] W. Zhang, G. Zhai, Y. Wei, X. Yang, and K. Ma (2023) Blind image quality assessment via vision-language correspondence: a multitask learning perspective . In CVPR , Cited by: Table A5 , Appendix  -->

<!-- [原子块 · verbatim] [90] Z. Zhang, C. Li, W. Sun, X. Liu, X. Min, and G. Zhai (2023) A perceptual quality assessment exploration for aigc images . In ICME Workshops , Cited by: Appendix C . -->

<!-- [原子块 · verbatim] [91] Z. Zhang, H. Wu, E. Zhang, G. Zhai, and W. Lin (2024) A benchmark for multi-modal foundation models on low-level vision: from single images to pairs . IEEE TPAMI . Cited by: §2 , §2 . -->

<!-- [原子块 · verbatim] [92] Z. Zhang, Y. Zhou, C. Li, B. Zhao, X. Liu, and G. Zhai (2024) Quality assessment in the era of large models: a survey . arXiv preprint arXiv:2409.00031 . Cited by: §2 . -->

<!-- [原子块 · verbatim] [93] H. Zheng, J. Fu, Y. Zeng, Z. Zha, and J. Luo (2021) Learning conditional knowledge distillation for degraded-reference image quality assessment . ICCV . Cited by: §2 . -->

<!-- [原子块 · verbatim] [94] W. Zhou and Z. Wang (2022) Quality assessment of image super-resolution: balancing deterministic and statistical fidelity . In ACM MM , Cited by: §2 . -->

<!-- [原子块 · verbatim] [95] D. Zhu, J. Chen, X. Shen, X. Li, and M. Elhoseiny (2024) MiniGPT-4: enhancing vision-language understanding with advanced large language models . In ICLR , Cited by: §1 , §2 . -->

<!-- [原子块 · verbatim] [96] H. Zhu, L. Li, J. Wu, W. Dong, and G. Shi (2020) MetaIQA: deep meta-learning for no-reference image quality assessment . In CVPR , Cited by: §2 . -->

<!-- [原子块 · verbatim] [97] H. Zhu, X. Sui, B. Chen, X. Liu, P. Chen, Y. Fang, and S. Wang (2024) 2AFC prompting of large multimodal models for image quality assessment . arXiv preprint arXiv:2402.01162 . Cited by: §2 . -->

<!-- [原子块 · verbatim] [98] H. Zhu, H. Wu, Y. Li, Z. Zhang, B. Chen, L. Zhu, Y. Fang, G. Zhai, W. Lin, and S. Wang (2024) Adaptive image quality assessment via teaching large multimodal model to compare . arXiv preprint arX -->

<!-- [原子块 · verbatim] [99] K. Zhu, J. Gu, Z. You, Y. Qiao, and C. Dong (2024) An intelligent agentic system for complex image restoration problems . arXiv preprint arXiv:2410.17809 . Cited by: §1 . -->

**EN** Appendix

**ZH** 附录

**EN** Appendix A Overview

**ZH** 附录 A 概览

**EN** This Appendix is structured as follows. First, more methodology details are described in Appendix B, followed by more ablation studies and qualitative results in Appendix C. Then, some extensions are illustrated in Appendix D. Finally, we discuss the limitations in Appendix E.

**ZH** 本附录结构如下：附录 B 先描述更多方法细节，附录 C 给出更多消融研究与定性结果，附录 D 说明若干扩展，最后附录 E 讨论局限性。

**EN** Appendix B More Details

**ZH** 附录 B 更多细节

**EN** B.1 Details of Dataset Construction

**ZH** B.1 数据集构造细节

**EN** Special designs for PIPAL dataset. The PIPAL dataset is annotated using pair-wise comparisons and Elo ratings, instead of the conventional five-point standard rating. As a result, variance information is not provided. To integrate the PIPAL dataset into our training framework, we assign a pseudo variance derived from other datasets. The statistics of the other three training datasets are shown in Tab. A1. Based on these statistics, we manually set the ratio of the mean standard deviation (std) to the score range for the PIPAL dataset as 20%. The minimum and maximum scores in the PIPAL dataset are 934.95 and 1835.99, respectively, thus the pseudo std is set as ⟦SLOT_73⟧. Note that all scores are normalized to [1,5] during training, with the std / variance normalized accordingly.

**ZH** 针对 PIPAL 数据集的特殊设计。PIPAL 数据集采用成对比较与 Elo 评分进行标注，而非常规的五点标准评分，因此未提供方差信息。为把 PIPAL 数据集纳入我们的训练框架，我们为其赋予一个由其他数据集推导出的伪方差。另外三个训练数据集的统计见表 A1。基于这些统计，我们手动把 PIPAL 数据集的平均标准差（std）与分数范围之比设为 20%。PIPAL 数据集中的最低分与最高分分别为 934.95 与 1835.99，因此伪 std 设为 ⟦SLOT_73⟧。注意训练时所有分数都被归一化到 [1,5]，std / 方差也相应归一化。

**EN** Table A1: Statistics of score range and standard deviation (std).

**ZH** 表 A1：分数范围与标准差（std）的统计。

<!-- [原子块 · table] Datasets KonIQ SPAQ KADID score range (max - min) 2.91 91.67 3.93 mean std 0.57 13.93 0.86 mean std / score range 19.73% 15.20% 21.90% -->

**EN** Degradation to linear interpolation when the variance is quite small. When the variance is extremely small, integration calculations can introduce errors. These errors can lead to strange solutions when directly solving the two constraint conditions for post-adjustment, resulting in ⟦SLOT_74⟧ and ⟦SLOT_75⟧ values that deviate significantly from 1 and 0, respectively. Consequently, the adjusted “probabilities” can become substantially smaller than 0 or larger than 1, which is unreasonable as the training label. Recall that the quality score, ⟦SLOT_76⟧, is modeled as a Gaussian distribution, ⟦SLOT_77⟧. To address this chanllenge, when the variance is extremely small, we approximate the probability density function, ⟦SLOT_78⟧, of the score’s Gaussian distribution as a unit impulse function:

**ZH** 方差极小时退化为线性插值。当方差极小时，积分计算会引入误差。这些误差会导致在直接求解后调整的两个约束条件时出现异常解，使 ⟦SLOT_74⟧ 与 ⟦SLOT_75⟧ 分别显著偏离 1 和 0；进而使调整后的“概率”大幅小于 0 或大于 1，作为训练标签是不合理的。回顾一下，质量分数 ⟦SLOT_76⟧ 被建模为高斯分布 ⟦SLOT_77⟧。为应对这一挑战，当方差极小时，我们把分数高斯分布的概率密度函数 ⟦SLOT_78⟧ 近似为单位冲激函数：

<!-- [原子块 · table] lim σ → 0 f ⁡ ( x ) = δ ⁡ ( x − μ ) , \lim_{\sigma\rightarrow 0}f(x)=\delta(x-\mu), (A1) -->

**EN** where ⟦SLOT_79⟧ is the unit impulse function. In this case, the soft label is calculated through linear interpolation between the two nearest center points. Suppose that ⟦SLOT_80⟧, and recall that ⟦SLOT_81⟧, the soft label is obtained as:

**ZH** 其中 ⟦SLOT_79⟧ 为单位冲激函数。此时，软标签通过在两个最近的中心点之间做线性插值来计算。假设 ⟦SLOT_80⟧，并回顾 ⟦SLOT_81⟧，则软标签由下式得到：

<!-- [原子块 · table] p i = { c j + 1 − μ , if ​ i = j , μ − c j , if ​ i = j + 1 , 0 , otherwise . p_{i}=\left\{\begin{aligned} &c_{j+1}-\mu,&\text{if }i=j,\\ &\mu-c_{j},&\text{if }i=j+1,\\ &0,&\text{otherwise}.\end{align -->

**EN** According to the ⟦SLOT_82⟧ rule, nearly all samples fall within the range ⟦SLOT_83⟧. Thus, if ⟦SLOT_84⟧ is less than half of the level interval, only the two nearest levels have non-zero probabilities. This criterion provides a way to define the threshold for small variance as ⟦SLOT_85⟧, which simplifies to ⟦SLOT_86⟧. To allow for a slightly relaxed threshold, the threshold for small (normalized) variance is set to ⟦SLOT_87⟧.

**ZH** 根据 ⟦SLOT_82⟧ 准则，几乎所有样本都落在 ⟦SLOT_83⟧ 范围内。因此，若 ⟦SLOT_84⟧ 小于等级区间的一半，则只有两个最近的等级具有非零概率。这一准则提供了一种定义小方差阈值的方法，即 ⟦SLOT_85⟧，化简为 ⟦SLOT_86⟧。为留出略微宽松的阈值，小（归一化）方差的阈值被设为 ⟦SLOT_87⟧。

**EN** B.2 Details of Methodology

**ZH** B.2 方法细节

**EN** Model architecture. DeQA-Score adopts the architecture of mPLUG-Owl2 [75], structured as follows. Specifically, the input images and the question texts are first tokenized, then fused, finally processed by the Large Language Model (LLM) for response generation. (a) Tokenizing input images and texts. We use a pre-trained CLIP pre-trained ViT-L/14 [49] as the image encoder to convert the input images into visual tokens, with each token having a channel of 1024. The texts are tokenized into textual tokens using the SentencePiece tokenizer [27], with each token having a channel of 4096. To bridge the different embedding spaces of visual and textual tokens, a trainable image abstractor, which is a six-layer transformer network, is implemented to map the vision tokens to the hidden dimension of the LLM, which is 4096. The abstractor can also significantly reduce the number of vision tokens to 64, relieving the computing pressure. (b) Token fusion. We integrate the visual tokens into pre-defined positions within the textual tokens as token fusion. (c) Response generation using LLM. The fused tokens are fed into an LLM, which is LLaMA-2-7B [62], to generate the final response. The LLM can be either LoRA-tuned [22] or fully tuned, and their results are similar when the vision components are trainable, as shown in Tab. A7.

**ZH** 模型架构。DeQA-Score 采用 mPLUG-Owl2 [75] 的架构，结构如下。具体而言，输入图像与问题文本先被词元化，再融合，最后由大语言模型（LLM）处理以生成回答。（a）输入图像与文本的词元化。我们使用预训练的 CLIP 预训练 ViT-L/14 [49] 作为图像编码器，把输入图像转换为视觉词元，每个词元的通道数为 1024。文本用 SentencePiece 分词器 [27] 切分为文本词元，每个词元通道数为 4096。为弥合视觉词元与文本词元之间嵌入空间的差异，我们实现了一个可训练的图像抽象器——一个六层 transformer 网络——把视觉词元映射到 LLM 的隐藏维度 4096。该抽象器还能把视觉词元数量显著缩减到 64，缓解计算压力。（b）词元融合。我们把视觉词元插入到文本词元中预定义的位置来完成融合。（c）用 LLM 生成回答。融合后的词元被送入 LLM（即 LLaMA-2-7B [62]）以生成最终回答。LLM 可以采用 LoRA 微调 [22] 或全量微调；如表 A7 所示，当视觉组件可训练时，两者结果相近。

**EN** Examples of dataset variation. As discussed in the main paper, different IQA datasets have distinct distributions. To illustrate this, we present six images sampled from various IQA datasets in Fig. A1. Although these images share similar mean quality scores (i.e., linearly normalized scores), they exhibit significantly different visual quality.

**ZH** 数据集差异的示例。如正文所述，不同 IQA 数据集具有不同的分布。为说明这一点，我们在图 A1 中给出了采样自多个 IQA 数据集的六张图像。尽管这些图像的平均质量分数（即线性归一化后的分数）相近，它们的视觉质量却差异显著。

<!-- [原子块 · img]  -->

**EN** Figure A1: Examples of dataset variation. Images from different IQA datasets have similar mean quality scores (i.e., linearly normalized scores), but exhibit significantly different visual quality. The image from KonIQ dataset has the best quality than others.

**ZH** 图 A1：数据集差异示例。来自不同 IQA 数据集的图像平均质量分数（即线性归一化后的分数）相近，视觉质量却差异显著。其中来自 KonIQ 数据集的图像质量最好。

**EN** B.3 Details of Training and Inference

**ZH** B.3 训练与推理细节

**EN** Training Setup. The pre-trained weights of mPLUG-Owl2 are used for model initialization. The loss weighting term is set to 0.05, bringing the two loss terms to roughly the same scale. We adopt AdamW [23] as the optimizer, with an initial learning rate of 2e-5 that gradually decays using a cosine decay strategy. A warmup strategy is applied with a warmup ratio of 0.03. Our model is trained with a batch size of 64 for 3 epochs. Both the vision encoder and abstractor are trainable, and the LLM is fully tuned unless specified. As shown in Tab. A7, LoRA-tuned LLM achieves comparable performance to fully-tuned LLM, providing an alternative for scenarios with limited computation resources. Using 8 RTX A6000 GPUs, training on the KonIQ dataset is completed in about 1.5 hours, while training on the KonIQ, SPAQ, and KADID datasets takes around 4 hours.

**ZH** 训练设置。模型用 mPLUG-Owl2 的预训练权重初始化。损失权重项设为 0.05，使两项损失大致处于同一量级。我们采用 AdamW [23] 作为优化器，初始学习率 2e-5，以余弦衰减策略逐步衰减，并采用预热比例为 0.03 的预热策略。模型以批大小 64 训练 3 轮。视觉编码器与抽象器均可训练，除非另有说明，LLM 采用全量微调。如表 A7 所示，LoRA 微调的 LLM 取得与全量微调相当的性能，为计算资源受限的场景提供了替代方案。使用 8 张 RTX A6000 GPU，在 KonIQ 数据集上训练约 1.5 小时完成，而在 KonIQ、SPAQ 与 KADID 三个数据集上训练约需 4 小时。

**EN** Explanation of closed-set softmax during inference. In the main paper, we follow Q-Align [70] by applying a closed-set softmax on the five levels to compute the probabilities ⟦SLOT_88⟧, thereby avoiding the influence of other textual tokens. As shown in our statistics in Tab. A2, the probability sum of the five levels after training is very close to 1, indicating that the trained MLLM consistently predicts one of the five levels. Thus, applying softmax over the five levels or across all textual tokens yields nearly identical results.

**ZH** 推理时闭集 softmax 的说明。在正文中，我们沿用 Q-Align [70] 对五个等级施加闭集 softmax 来计算概率 ⟦SLOT_88⟧，从而避免其他文本词元的影响。如表 A2 中的统计所示，训练后五个等级的概率之和非常接近 1，说明训练后的 MLLM 一致地预测五个等级之一。因此，对五个等级或对所有文本词元施加 softmax 得到的结果几乎相同。

**EN** Table A2: Probability sum of the five levels when applying softmax function on all textual tokens.

**ZH** 表 A2：对所有文本词元施加 softmax 函数时五个等级的概率之和。

<!-- [原子块 · table] Datasets KonIQ SPAQ KADID PIPAL LIVE-Wild AGIQA-3K Prob. Sum 0.9998 0.9998 0.9996 0.9997 0.9997 0.9996 -->

**EN** Appendix C More Results

**ZH** 附录 C 更多结果

**EN** Results of score distribution prediction with KL divergence as metric. In Tab. 5, we provide the distribution prediction results with JS divergence and Wasserstein distance as metrics. Here we further add the KL divergence as metric. The KL divergence between two Gaussian distributions, ⟦SLOT_89⟧, ⟦SLOT_90⟧, is calculated as:

**ZH** 以 KL 散度为指标的分数分布预测结果。在表 5 中，我们给出了以 JS 散度与 Wasserstein 距离为指标的分布预测结果。这里我们进一步加入 KL 散度作为指标。两个高斯分布 ⟦SLOT_89⟧、⟦SLOT_90⟧ 之间的 KL 散度计算如下：

<!-- [原子块 · table] KL ( p 1 | | p 2 ) = log ( σ 2 σ 1 ) + σ 1 2 + ( μ 1 − μ 2 ) 2 2 ​ σ 2 2 − 1 2 . {\rm KL}(p_{1}||p_{2})=\log(\frac{\sigma_{2}}{\sigma_{1}})+\frac{\sigma_{1}^{2}+(\mu_{1}-\mu_{2})^{2}}{2\sigma_{2}^{2}} -->

**EN** The results are given in Tab. A3, where the KL divergence of Q-Align is quite large. We explain this as follows. As in Figs. 6, A4, A3 and A5, Q-Align tends to predict a single level token, bringing a quite small predicted variance. That means, the first variance, ⟦SLOT_91⟧ in Eq. A3, is quite small (⟦SLOT_92⟧), thus the KL divergence goes extremely large (⟦SLOT_93⟧).

**ZH** 结果见表 A3，其中 Q-Align 的 KL 散度相当大。我们解释如下：如图 6、A4、A3 与 A5 所示，Q-Align 倾向于预测单一等级词元，导致预测方差很小。这意味着式 A3 中的第一个方差 ⟦SLOT_91⟧ 非常小（⟦SLOT_92⟧），因而 KL 散度变得极大（⟦SLOT_93⟧）。

**EN** Table A3: Score distribution prediction results with KL divergence between the predicted Gaussian distribution and the human labeled Gaussian distribution as metric. Models are trained on the KonIQ, SPAQ, and KADID datasets. DeQA-Score achieves a much closer alignment with human annotations.

**ZH** 表 A3：以预测高斯分布与人工标注高斯分布之间的 KL 散度为指标的分数分布预测结果。模型在 KonIQ、SPAQ 与 KADID 数据集上训练。DeQA-Score 与人工标注的吻合度要高得多。

<!-- [原子块 · table] KonIQ SPAQ KADID LIVE-Wild AGIQA-3K Q-Align [ 70 ] 109.039 2.329 1229.530 3.980 76.414 DeQA-Score 0.058 0.241 0.142 0.249 0.534 -->

**EN** Results on more AI-generated images. In the main paper, we have included an IQA dataset with AI-generated images, AGIQA-3K [30], for evaluation. Here we further provide evaluation results on three additional AIGC datasets including AIGCIQA2023 [65], AGIN [10], and AGIQA-1K [90] in Tab. A4. Both Q-Align and our DeQA-Score are trained on the KonIQ, SPAQ, and KADID datasets, and then directly evaluated on these unseen AIGC datasets. Our DeQA-Score consistently outperforms the baseline method.

**ZH** 在更多 AI 生成图像上的结果。在正文中，我们已纳入一个包含 AI 生成图像的 IQA 数据集 AGIQA-3K [30] 用于评测。这里我们进一步给出在另外三个 AIGC 数据集上的评测结果，包括 AIGCIQA2023 [65]、AGIN [10] 与 AGIQA-1K [90]，见表 A4。Q-Align 与我们的 DeQA-Score 都在 KonIQ、SPAQ 与 KADID 数据集上训练，然后直接在这些未见过的 AIGC 数据集上评测。我们的 DeQA-Score 持续优于基线方法。

**EN** Table A4: Results on AI-generated images with PLCC / SRCC metrics. The models are trained on KonIQ, SPAQ, and KADID.

**ZH** 表 A4：在 AI 生成图像上的结果（PLCC / SRCC 指标）。模型在 KonIQ、SPAQ 与 KADID 上训练。

<!-- [原子块 · table] AIGCIQA2023 AGIN AGIQA-1K AGIQA-3K Q-Align [ 70 ] 0.809 / 0.783 0.655 / 0.615 0.650 / 0.442 0.788 / 0.733 DeQA-Score 0.826 / 0.799 0.674 / 0.626 0.715 / 0.514 0.808 / 0.745 -->

**EN** Table A5: Score regression results of co-training on multiple IQA datasets with the PLCC / SRCC metrics. The models are trained on the KonIQ, SPAQ, and KADID datasets.

**ZH** 表 A5：在多个 IQA 数据集上联合训练的分数回归结果（PLCC / SRCC 指标）。模型在 KonIQ、SPAQ 与 KADID 数据集上训练。

<!-- [原子块 · table] Methods KonIQ SPAQ KADID PIPAL LIVE-Wild AGIQA-3K TID2013 CSIQ LIQE [ 89 ] 0.907 / 0.922 0.916 / 0.921 0.928 / 0.929 0.503 / 0.493 0.855 / 0.822 0.689 / 0.650 0.881 / 0.854 0.792 / 0.794 Compare2Score -->

**EN** Table A6: Ablation studies on level numbers with PLCC / SRCC metrics. We use numerical names (one / two / three / four / five / …) as level names because they are easy to extend to different numbers. The models are trained on the KonIQ, SPAQ, and KADID datasets.

**ZH** 表 A6：关于等级数量的消融研究（PLCC / SRCC 指标）。我们使用数字名称（one / two / three / four / five / …）作为等级名称，因为它们易于扩展到不同数量。模型在 KonIQ、SPAQ 与 KADID 数据集上训练。

<!-- [原子块 · table] Level Number KonIQ SPAQ KADID PIPAL LIVE-Wild AGIQA-3K TID2013 CSIQ 5 0.945 / 0.932 0.934 / 0.930 0.955 / 0.952 0.421 / 0.424 0.873 / 0.857 0.766 / 0.712 0.820 / 0.794 0.882 / 0.835 6 0.947 / 0.935 0. -->

**EN** Table A7: Ablation studies on training / fixing various model components with PLCC / SRCC metrics. “Enc.” means vision encoder, and “Abs.” represents vision abstractor. “LLM LoRA” or “LLM Full” represents the LLM is LoRA-tuned [22] or fully tuned. “✔” means this component is trained. The models are trained on the KonIQ, SPAQ, and KADID datasets. The results show that training vision encoder and abstractor significantly improves the performance. When vision encoder and abstractor are trained, fully-tuned LLM only shows a slight advantage over LoRA-tuned LLM.

**ZH** 表 A7：关于训练/固定各模型组件的消融研究（PLCC / SRCC 指标）。“Enc.”指视觉编码器，“Abs.”指视觉抽象器。“LLM LoRA”或“LLM Full”分别表示 LLM 采用 LoRA 微调 [22] 或全量微调。“✔”表示该组件被训练。模型在 KonIQ、SPAQ 与 KADID 数据集上训练。结果表明，训练视觉编码器与抽象器能显著提升性能；而当视觉编码器与抽象器都被训练时，全量微调的 LLM 相比 LoRA 微调仅有轻微优势。

<!-- [原子块 · table] # Enc. Abs. LLM LoRA LLM Full KonIQ SPAQ KADID PIPAL LIVE-Wild AGIQA-3K TID2013 CSIQ 0 ✔ 0.826 / 0.797 0.871 / 0.867 0.814 / 0.803 0.440 / 0.427 0.728 / 0.695 0.804 / 0.750 0.740 / 0.692 0.818 / 0.751 -->

**EN** Table A8: Low-level perception results on Q-Bench [68] of co-training with or pre-training on score regression tasks. The results of #0, #1, and #2 are borrowed from [69]. Co-training with or pre-training on score regression tasks stably improves the performance.

**ZH** 表 A8：在 Q-Bench [68] 上的低层感知结果——与分数回归任务联合训练或在其上预训练。#0、#1 与 #2 的结果引自 [69]。与分数回归任务联合训练或在其上预训练都能稳定提升性能。

<!-- [原子块 · table] # Method Yes / No What How Distortion Other IC Distortion IC Other Overall 0 From the scratch [ 69 ] 0.7218 0.5796 0.5619 0.5668 0.6921 0.5329 0.7265 0.6161 1 High-level co-training [ 69 ] 0.7564 0.67 -->

**EN** Table A9: Co-training with Q-Instruct [69] leads to an obvious reduction in score regression performance. Exploring better strategies to combine language-based quality description tasks with score regression tasks is left as our future work.

**ZH** 表 A9：与 Q-Instruct [69] 联合训练会导致分数回归性能明显下降。探索更好的策略把基于语言的质量描述任务与分数回归任务结合起来，留作我们的未来工作。

<!-- [原子块 · table] KonIQ SPAQ KADID PIPAL LIVE-Wild AGIQA-3K TID2013 CSIQ Co-training with Q-Instruct 0.916 / 0.926 0.870 / 0.816 0.812 / 0.810 0.286 / 0.289 0.825 / 0.812 0.778 / 0.732 0.680 / 0.656 0.798 / 0.790 Only  -->

**EN** More baselines on multi-dataset training. In the main paper, we primarily compare with Q-Align. Here we add the comparison results with more baselines including LIQE [89] and Compare2Score [98] in Tab. A5. Our DeQA-Score consistently outperforms these baselines.

**ZH** 多数据集训练的更多基线。在正文中，我们主要与 Q-Align 作比较。这里我们补充了与更多基线的对比结果，包括 LIQE [89] 与 Compare2Score [98]，见表 A5。我们的 DeQA-Score 持续优于这些基线。

**EN** Ablation studies on level number are conducted in Tab. A7. The performance improves with moderately larger level numbers (i.e., 6⟦SLOT_94⟧8), as discretization becomes more accurate. However, the performance declines with much larger level numbers (i.e., 10⟦SLOT_95⟧12), due to the increased difficulty in level prediction (more classification categories).

**ZH** 关于等级数量的消融研究见表 A7。随着等级数量适度增大（即 6⟦SLOT_94⟧8），性能有所提升，因为离散化变得更准确。然而，当等级数量过大（即 10⟦SLOT_95⟧12）时性能下降，原因是等级预测变得更困难（分类类别更多）。

**EN** Ablation studies on training / fixing components are summarized in Tab. A7. The vision encoder and abstractor can be either fixed or trained, while the LLM can be LoRA-tuned [22] or fully tuned. First, comparing #0 with #1, or #3 with #4, training the vision abstractor significantly enhances performance. Second, similarly, from #1 to #2, or #4 to #5, training the vision encoder also leads to performance improvements. This improvement may be attributed to the fact that training either the vision encoder or abstractor helps extract more relevant features for IQA. Third, comparing #0 with #3, when the vision components are fixed, fully-tuned LLM shows a substantial advantage over LoRA-tuned LLM. Finally, from #1 to #4, or #2 to #5, when the vision components are trainable, fully-tuned LLM demonstrates similar performance to LoRA-tuned LLM. This provides an alternative if the computation resources are limited.

**ZH** 关于训练/固定组件的消融研究总结于表 A7。视觉编码器与抽象器可以固定或训练，LLM 可以采用 LoRA 微调 [22] 或全量微调。第一，比较 #0 与 #1，或 #3 与 #4，训练视觉抽象器显著提升了性能。第二，类似地，从 #1 到 #2，或 #4 到 #5，训练视觉编码器也带来性能提升；这一提升可能源于训练视觉编码器或抽象器有助于提取与 IQA 更相关的特征。第三，比较 #0 与 #3，当视觉组件固定时，全量微调的 LLM 相比 LoRA 微调有明显优势。最后，从 #1 到 #4，或 #2 到 #5，当视觉组件可训练时，全量微调的 LLM 与 LoRA 微调表现相近；这为计算资源受限的情况提供了替代方案。

**EN** Qualitative results are provided in Figs. A4, A3 and A5. Q-Align, which is trained on one-hot labels, tends to predict a single label, resulting in higher KL divergence. Our DeQA-Score can predict the score distribution that aligns well with human annotations under wide circumstances:

**ZH** 定性结果见图 A4、A3 与 A5。用 one-hot 标签训练的 Q-Align 倾向于预测单一标签，导致 KL 散度更高。我们的 DeQA-Score 能在广泛的情形下预测出与人工标注高度吻合的分数分布：

**EN** • Different categories of distortions, including in-the-wild images with authentic distortions in Fig. A3, artificial distortions in Fig. A4, AI-generated images in Fig. A5.

**ZH** • 不同类别的失真，包括图 A3 中带真实场景失真的真实图像、图 A4 中的人工失真、图 A5 中的 AI 生成图像。

**EN** • Multiple quality levels, such as, poor quality (Fig. A3f, Fig. A4ah), fair quality (Fig. A3e, Fig. A4g), and high quality (Fig. A3hj, Fig. A5c).

**ZH** • 多种质量水平，例如低质量（图 A3f、图 A4ah）、中等质量（图 A3e、图 A4g）与高质量（图 A3hj、图 A5c）。

**EN** • Various image contents, including animals (Fig. A3e, Fig. A4bd), humans (Fig. A3fg, Fig. A5ad), nature scenes (Fig. A4agh), urban scenes (Fig. A3ch, Fig. A4f), indoor scenes (Fig. A3abd), and sports (Fig. A3i, Fig. A4c).

**ZH** • 多样的图像内容，包括动物（图 A3e、图 A4bd）、人物（图 A3fg、图 A5ad）、自然场景（图 A4agh）、城市场景（图 A3ch、图 A4f）、室内场景（图 A3abd）与运动（图 A3i、图 A4c）。

**EN** Appendix D Extensions

**ZH** 附录 D 扩展

**EN** Score regression helps quality description. We investigate whether score regression tasks can enhance general low-level perception tasks, i.e., language-based quality description tasks. The low-level perception tasks are evaluated on Q-Bench [68]. For score regression, we adopt the same training techniques as in the main paper, and train the model on the KonIQ, SPAQ, and KADID datasets. The low-level perception tasks are trained using the next token prediction paradigm, with Q-Instruct [69] as the training dataset. Q-Instruct [69] has shown that co-training with or pre-training on high-level tasks can improve performance on low-level perception tasks. Similarly, we evaluate two strategies: (a) co-training with score regression tasks, and (b) pre-training on score regression tasks. Some questions in the Q-Instruct dataset are quite similar to the questions of score regression, which may confuse the model. Therefore, we append the questions of score regression with a specific suffix, “Answer the question with levels.”, to specify the task.

**ZH** 分数回归有助于质量描述。我们考察分数回归任务是否能增强通用的低层感知任务，即基于语言的质量描述任务。低层感知任务在 Q-Bench [68] 上评测。对分数回归，我们采用与正文相同的训练技术，在 KonIQ、SPAQ 与 KADID 数据集上训练模型。低层感知任务用下一词元预测范式训练，以 Q-Instruct [69] 作为训练数据集。Q-Instruct [69] 已表明，与高层任务联合训练或在其上预训练可以提升低层感知任务的性能。类似地，我们评估两种策略：（a）与分数回归任务联合训练；（b）在分数回归任务上预训练。Q-Instruct 数据集中的一些问题与分数回归的问题十分相似，可能使模型困惑。因此，我们为分数回归的问题追加一个特定后缀“Answer the question with levels.”以明确任务。

**EN** The experimental results are presented in Tab. A9. First, comparing #0 with #3 & #4, both co-training with and pre-training on score regression tasks consistently improve low-level perception performance. Second, comparing #1 with #3, or #2 with #4, the benefits from score regression tasks are greater than those from high-level tasks, likely because score regression is more closely related to low-level perception. Finally, from #3 to #4, pre-training on score regression tasks achieves better results than co-training.

**ZH** 实验结果见表 A9。第一，比较 #0 与 #3 和 #4，与分数回归任务联合训练或在其上预训练都持续提升了低层感知性能。第二，比较 #1 与 #3，或 #2 与 #4，来自分数回归任务的收益大于来自高层任务的收益，可能是因为分数回归与低层感知的关系更紧密。最后，从 #3 到 #4，在分数回归任务上预训练比联合训练取得更好的结果。

**EN** Quality description harms score regression. Considering the promising results in Tab. A9, we aim to explore whether it is possible to co-train a model for both accurate score regression and language-based quality description. We therefore evaluate the score regression results of the co-trained model in Tab. A9. These preliminary results indicate that co-training with the instruction-tuning dataset, Q-Instruct, leads to a noticeable decrease in score regression. The reason can be that, in quality description datasets, the words to describe the quality levels are very diverse, greatly beyond the pre-defined five levels for score regression. This may confuse the model when predicting the level tokens.

**ZH** 质量描述损害分数回归。鉴于表 A9 中可观的结果，我们希望探索是否有可能联合训练一个同时具备准确分数回归与基于语言的质量描述能力的模型。因此我们在表 A9 中评测了联合训练模型的分数回归结果。这些初步结果表明，与指令微调数据集 Q-Instruct 联合训练会导致分数回归明显下降。原因可能在于，质量描述数据集中用于描述质量等级的词语非常多样，远远超出分数回归预定义的五个等级，这可能使模型在预测等级词元时感到困惑。

<!-- [原子块 · img]  -->

**EN** Figure A2: Illustration of discretization errors when the variance is quite small. A score distribution, ⟦SLOT_96⟧, is discretized into a soft label, where both “fair” and “good” share a probability of 0.5. However, the recovered distribution from this soft label becomes ⟦SLOT_97⟧, resulting in a larger variance and, consequently, a flatter curve of the distribution density function.

**ZH** 图 A2：方差极小时离散化误差的示意图。一个分数分布 ⟦SLOT_96⟧ 被离散化为软标签，其中“fair”与“good”各占 0.5 的概率。然而，由该软标签还原出的分布变为 ⟦SLOT_97⟧，导致方差变大，进而使分布密度函数的曲线更加平坦。

**EN** Appendix E Limitations and Future Works

**ZH** 附录 E 局限性与未来工作

**EN** Simple co-training with quality description cannot improve score regression. As shown in Appendix D, score regression tasks can enhance quality description results, while co-training with quality description tasks reduces the score regression performance. How to better co-train these two tasks remains an open question. However, first, the performance of the co-training model is still reasonable and higher than many non-MLLM-based IQA methods. Second, with the rapid development of MLLM-based quality description research, better quality description datasets may help.

**ZH** 与质量描述的简单联合训练无法提升分数回归。如附录 D 所示，分数回归任务可以增强质量描述的结果，而与质量描述任务联合训练却会降低分数回归性能。如何更好地联合训练这两个任务仍是一个开放问题。不过，第一，联合训练模型的性能仍然合理，高于许多非 MLLM 的 IQA 方法；第二，随着基于 MLLM 的质量描述研究快速发展，更好的质量描述数据集可能有所帮助。

**EN** Our discretization introduces errors when the variance is very small. While our discretization method effectively handles most distributions, it still introduces errors in the variance of the distribution when the variance is very small. For instance, as shown in Fig. A2, a score distribution with a small variance, ⟦SLOT_98⟧, is discretized into a soft label where both “fair” and “good” share a probability of 0.5. The recovered distribution from this soft label becomes ⟦SLOT_99⟧, resulting in a larger variance and a flatter curve in the probability density function. However, samples with extremely small variance are rare, e.g., only 0.29% of samples in the KonIQ dataset have a variance smaller than ⟦SLOT_100⟧. Thus, the overall influence of this issue is relatively small. How to better preserve the distribution characteristics during discretization for such cases is our future work.

**ZH** 我们的离散化在方差极小时会引入误差。虽然我们的离散化方法能有效处理大多数分布，但当方差极小时，它仍会在分布的方差上引入误差。例如，如图 A2 所示，一个方差很小的分数分布 ⟦SLOT_98⟧ 被离散化为一个软标签，其中“fair”与“good”各占 0.5 的概率；由该软标签还原出的分布变为 ⟦SLOT_99⟧，方差变大，概率密度函数曲线更加平坦。然而，方差极小的样本十分罕见，例如 KonIQ 数据集中只有 0.29% 的样本方差小于 ⟦SLOT_100⟧，因此该问题的整体影响相对较小。如何在此类情形下更好地在离散化过程中保持分布特性，是我们的未来工作。

**EN** High memory consumption. As our DeQA-Score is based on an MLLM with 7B parameters, it requires 15.2G storage space (in bfloat16 format) and 15.8G (batch size 1) / 23.0G (batch size 64) CUDA memory for inference. Despite this, it remains deployable on consumer GPUs like 4090, and the memory consumption can be reduced through quantization.

**ZH** 显存占用较高。由于我们的 DeQA-Score 基于一个 7B 参数的 MLLM，它需要 15.2G 存储空间（bfloat16 格式），推理时需要 15.8G（批大小 1）/ 23.0G（批大小 64）CUDA 显存。尽管如此，它仍可部署在 4090 等消费级 GPU 上，且显存占用可通过量化进一步降低。

<!-- [原子块 · img]  -->

**EN** Figure A3: Qualitative results on in-the-wild IQA datasets, sampled from the KonIQ, SPAQ, and LIVE-Wild datasets.

**ZH** 图 A3：在真实场景 IQA 数据集上的定性结果，采样自 KonIQ、SPAQ 与 LIVE-Wild 数据集。

<!-- [原子块 · img]  -->

**EN** Figure A4: Qualitative results on IQA datasets with artificial distortions, sampled from the KADID and CSIQ datasets.

**ZH** 图 A4：在带人工失真的 IQA 数据集上的定性结果，采样自 KADID 与 CSIQ 数据集。

<!-- [原子块 · img]  -->

**EN** Figure A5: Qualitative results on IQA datasets with AI-generated images, sampled from the AGIQA-3K dataset.

**ZH** 图 A5：在含 AI 生成图像的 IQA 数据集上的定性结果，采样自 AGIQA-3K 数据集。
