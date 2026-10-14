# NIMA：神经图像评价

> 原标题：NIMA: Neural Image Assessment
> 作者：Hossein Talebi, Peyman Milanfar · arXiv:1709.05424 · 2017-09-15

<!-- [原子块 · verbatim] NIMA: Neural Image Assessment Thanks: H. Talebi and P. Milanfar are with Google Research, Mountain View, USA, Email: {htalebi, milanfar}@google.com. -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] Automatically learned quality assessment for images has recently become a hot topic due to its usefulness in a wide variety of applications such as evaluating image capture pipelines, storage techniqu -->

**EN** Index Terms:

**ZH** 索引词：

**EN** I Introduction

**ZH** I 引言

**EN** Quantification of image quality and aesthetics have been a long-standing problem in image processing and computer vision. While technical quality assessment deals with measuring low-level degradations such as noise, blur, compression artifacts, etc., aesthetic assessment quantifies semantic level characteristics associated with emotions and beauty in images. In general, image quality assessment can be categorized into full-reference and no-reference approaches. While availability of a reference image is assumed in the former (metrics such as PSNR, SSIM[3], etc.), typically blind (no-reference) approaches rely on a statistical model of distortions to predict image quality. The main goal of both categories is to predict a quality score that correlates well with human perception. Yet, the subjective nature of image quality remains the fundamental issue. Recently, more complex models such as deep convolutional neural networks (CNNs) have been used to address this problem[4, 5, 6, 7, 8, 9, 10, 11]. Emergence of labeled data from human ratings has encouraged these efforts [1, 2, 12, 13, 14]. In a typical deep CNN approach, weights are initialized by training on classification related datasets (e.g. ImageNet [15]), and then fine tuned on annotated data for perceptual quality assessment tasks.

**ZH** 图像质量与美感的量化一直是图像处理和计算机视觉中的长期难题。技术质量评价关注噪声、模糊、压缩伪影等低层退化的度量，美学评价则量化图像中与情感和美感相关的语义层特征。总体而言，图像质量评价可分为全参考与无参考两类：前者假定存在参考图像（如 PSNR、SSIM[3] 等指标），后者通常为盲评价，依赖退化的统计模型来预测图像质量。两类方法的共同目标是给出一个与人类感知高度相关的质量分数，而图像质量的主观性始终是根本难题。近来，深度卷积神经网络（CNN）等更复杂的模型被用于应对这一问题[4, 5, 6, 7, 8, 9, 10, 11]，来自人类评分的标注数据的出现也推动了这些工作[1, 2, 12, 13, 14]。典型的深度 CNN 做法是先在与分类相关的数据集（如 ImageNet [15]）上训练以初始化权重，再在带标注的感知质量评价数据上微调。

**EN** I-A Related Work

**ZH** I-A 相关工作

**EN** Machine learning has shown promising success in predicting technical quality of images [4, 5, 6, 7]. Kang et. al. [5] show that extracting high level features using CNNs can result in state-of-the-art blind quality assessment performance. It appears that replacing hand-crafted features with an end-to-end feature learning system is the main advantage of using CNNs for pixel-level quality assessment tasks [5, 6]. The proposed method in [5] is a shallow network with one convolutional layer and two fully-connected layers, and input patches are of size ⟦SLOT_0⟧. Bosse et al. [6] use a deep CNN with 12 layers to improve on image quality predictions of [5]. Given the small input size (⟦SLOT_1⟧ patch), both methods require score aggregation across the whole image. Bianco et al. in [7] propose a deep quality predictor based on AlexNet [15]. Multiple CNN features are extracted from image crops of size ⟦SLOT_2⟧, and then regressed to the human scores.

**ZH** 机器学习在预测图像技术质量方面已展现出可观的成效[4, 5, 6, 7]。Kang 等人[5]表明，用 CNN 提取高层特征可以达到盲质量评价的最优性能。以端到端的特征学习系统取代手工特征，似乎正是 CNN 用于像素级质量评价任务的主要优势[5, 6]。文献[5]的方法是含一个卷积层和两个全连接层的浅层网络，输入块大小为 ⟦SLOT_0⟧。Bosse 等人[6]使用 12 层的深度 CNN，改进了[5]的图像质量预测。由于输入尺寸较小（⟦SLOT_1⟧ 的块），两种方法都需要在整幅图像上聚合分数。Bianco 等人[7]提出基于 AlexNet [15] 的深度质量预测器：先从 ⟦SLOT_2⟧ 大小的图像裁剪中提取多个 CNN 特征，再回归到人类分数。

**EN** Success of CNNs on object recognition tasks has significantly benefited the research on aesthetic assessment. This seems natural, as semantic level qualities are directly related to image content. Recent CNN-based methods [8, 9, 11, 10, 16] show a significant performance improvement compared to earlier works based on hand-crafted features [1]. Murray et al. [1] is the benchmark on aesthetic assessment. They introduce the AVA dataset and propose a technique to use manually designed features for style classification. Later, Lu et al. [8, 17] show that deep CNNs are well suited to the aesthetic assessment task. Their double-column CNN [17] consists of four convolutional and two fully-connected layers, and its inputs are the resized image and cropped windows of size ⟦SLOT_3⟧. Predictions from these global and local image views are aggregated to an overall score by a fully-connected layer. Similar to Murray et al. [1], in [17] images are also categorized to low and high aesthetics based on mean human ratings. A regression loss and an AlexNet inspired architecture is used in [9] to predict the mean scores. In a similar approach to [9], Bin et al. [11] fine-tune a VGG network [18] to learn the human ratings of the AVA dataset. They use a regression framework to predict the histogram of ratings. A recent method by Zheng et al. [19] retrains AlexNet and ResNet CNNs to predict quality of photos. More recently, [10] uses an adaptive spatial pooling to allow for feeding multiple scales of the input image with fixed size aspect ratios to their CNN. This work presents a multi-net (each network a pre-trained VGG) approach which extracts features at multiple scales, and uses a scene aware aggregation layer to combine predictions of the sub-networks. Similarly, Ma et al. [20] propose a layout-aware framework in which a saliency map is used to select patches with highest impact on predicted aesthetic score. Overall, none of these methods reported correlation of their predictions with respect to ground truth ratings. Recently, Kong et al. in [14] proposed a method to aesthetically rank photos by training on AVA with a rank-based loss function. They trained an AlexNet-based CNN to learn the difference of the aesthetic scores from two input images, and as a result, indirectly optimize for rank correlation. To the best of our knowledge, [14] is the only work that performed a correlation evaluation against AVA ratings.

**ZH** CNN 在目标识别任务上的成功极大推动了美学评价研究。这并不意外，因为语义层质量与图像内容直接相关。近来基于 CNN 的方法[8, 9, 11, 10, 16]相比早期基于手工特征的工作[1]有显著性能提升。Murray 等人[1]是美学评价的基准工作，他们发布了 AVA 数据集，并提出一种用人工设计特征做风格分类的技术。此后，Lu 等人[8, 17]表明深度 CNN 十分适合美学评价任务。其双列 CNN [17]含四个卷积层和两个全连接层，输入为缩放后的整图以及 ⟦SLOT_3⟧ 大小的裁剪窗口；来自全局与局部视图的预测由一个全连接层聚合为总分。与 Murray 等人[1]类似，[17]也依据人类平均评分把图像分为低美感与高美感两类。文献[9]采用回归损失和受 AlexNet 启发的结构来预测平均分。Bin 等人[11]沿用类似思路，微调 VGG 网络[18]以学习 AVA 数据集上的人类评分，用回归框架预测评分直方图。Zheng 等人[19]重新训练 AlexNet 与 ResNet 来预测照片质量。更近期的工作[10]使用自适应空间池化，使固定长宽比的多尺度输入得以送入同一个 CNN；该工作采用多网络结构（每个子网络为预训练 VGG），在多尺度上提取特征，并用场景感知聚合层合并各子网络的预测。类似地，Ma 等人[20]提出布局感知框架，用显著性图挑选对预测美学分数影响最大的块。总的来看，这些方法都没有报告其预测相对真实评分的相关性。最近，Kong 等人[14]提出一种在 AVA 上以排序损失函数训练的美学照片排序方法：训练基于 AlexNet 的 CNN 学习两幅输入图像的美学分数之差，从而间接优化等级相关性。据我们所知，[14]是唯一针对 AVA 评分开展相关性评估的工作。

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

**EN** Fig. 1: Histograms of ratings from AVA dataset[1]. Left: Histogram of mean scores. Middle: Histogram of standard deviations. Right: Joint histogram of the mean and standard deviation.

**ZH** 图 1：AVA 数据集[1]的评分直方图。左：均分直方图；中：标准差直方图；右：均值与标准差的联合直方图。

<!-- [原子块 · img]  -->

**EN** (a) ⟦SLOT_4⟧

**ZH** (a) ⟦SLOT_4⟧

<!-- [原子块 · img]  -->

**EN** (b) ⟦SLOT_5⟧

**ZH** (b) ⟦SLOT_5⟧

<!-- [原子块 · img]  -->

**EN** (c) ⟦SLOT_6⟧

**ZH** (c) ⟦SLOT_6⟧

<!-- [原子块 · img]  -->

**EN** (d) ⟦SLOT_7⟧

**ZH** (d) ⟦SLOT_7⟧

**EN** Fig. 2: Some example images from AVA dataset[1] with quality score ⟦SLOT_8⟧, where ⟦SLOT_9⟧ and ⟦SLOT_10⟧ represent mean and standard deviation of score, respectively. (a) high aesthetics and low unconventionality (challenge name: “Best of 2007”, ⟦SLOT_11⟧, ⟦SLOT_12⟧), (b) high aesthetics and high unconventionality (challenge name: “Extreme super moon”, ⟦SLOT_13⟧, ⟦SLOT_14⟧), (c) low aesthetics and high unconventionality (challenge name: “Travel”, ⟦SLOT_15⟧, ⟦SLOT_16⟧), (d) low aesthetics and low unconventionality (challenge name: “Pieces of the human form”, ⟦SLOT_17⟧, ⟦SLOT_18⟧).

**ZH** 图 2：AVA 数据集[1]的若干示例图像，质量分数记为 ⟦SLOT_8⟧，其中 ⟦SLOT_9⟧ 与 ⟦SLOT_10⟧ 分别表示分数的均值与标准差。(a) 高美感、低非常规性（挑战主题：“Best of 2007”，⟦SLOT_11⟧，⟦SLOT_12⟧）；(b) 高美感、高非常规性（挑战主题：“Extreme super moon”，⟦SLOT_13⟧，⟦SLOT_14⟧）；(c) 低美感、高非常规性（挑战主题：“Travel”，⟦SLOT_15⟧，⟦SLOT_16⟧）；(d) 低美感、低非常规性（挑战主题：“Pieces of the human form”，⟦SLOT_17⟧，⟦SLOT_18⟧）。

**EN** I-B Our Contributions

**ZH** I-B 本文贡献

**EN** In this work, we introduce a novel approach to predict both technical and aesthetic qualities of images. We show that models with the same CNN architecture, trained on different datasets, lead to state-of-the-art performance for both tasks. Since we aim for predictions with higher correlation with human ratings, instead of classifying images to low/high score or regressing to the mean score, the distribution of ratings are predicted as a histogram. To this end, we use the squared EMD (earth mover’s distance) loss proposed in [21], which shows a performance boost in classification with ordered classes. Our experiments show that this approach also leads to more accurate prediction of the mean score. Also, as shown in aesthetic assessment case [1], non-conventionality of images is directly related to score standard deviations. Our proposed paradigm allows for predicting this metric as well.

**ZH** 本文提出一种同时预测图像技术质量与美学质量的新方法。我们表明，结构相同而训练数据集不同的模型可以在两项任务上都达到最优性能。为了让预测与人类评分的相关性更高，我们不把图像分为低分／高分两类，也不回归到均分，而是以直方图形式预测评分的分布。为此采用文献[21]提出的平方 EMD（推土机距离）损失，该损失在有序类别的分类任务中被证明能带来性能提升。实验表明，这一做法同时也让均分预测更加准确。此外，正如美学评价研究[1]所指出的，图像的非常规性与分数标准差直接相关，本文提出的范式同样能够预测这一指标。

**EN** It has recently been shown that perceptual quality predictors can be used as learning loss to train image enhancement models [22, 23]. Similarly, image quality predictors can be used to adjust parameters of enhancement techniques [24]. In this work we use our quality assessment technique to effectively tune parameters of image denoising and tone enhancement operators to produce perceptually superior results.

**ZH** 近期研究表明，感知质量预测器可作为学习损失用于训练图像增强模型[22, 23]；类似地，图像质量预测器也能用于调节增强技术的参数[24]。本文将所提质量评价方法用于高效调节图像去噪与色调增强算子的参数，以得到感知上更优的结果。

**EN** This paper begins with reviewing three widely used datasets for quality assessment. Then, our proposed method is explained in more detail. Finally, performance of this work is quantified and compared to the existing methods.

**ZH** 本文先回顾质量评价中三套广泛使用的数据集，随后详述所提方法，最后量化本工作的性能并与现有方法比较。

**EN** I-C A Large-Scale Database for Aesthetic Visual Analysis (AVA) [1]

**ZH** I-C 面向美学视觉分析的大规模数据库（AVA）[1]

**EN** The AVA dataset contains about 255,000 images, rated based on aesthetic qualities by amateur photographers11 1 AVA images are obtained from www.dpchallenge.com, which is an on-line community for amateur photographers.. Each photo is scored by an average of 200 people in response to photography contests. Each image is associated to a single challenge theme, with nearly 900 different contests in the AVA. The image ratings range from 1 to 10, with 10 being the highest aesthetic score associated to an image. Histograms of AVA ratings are shown in Fig. 1. As can be seen, mean ratings are concentrated around the overall mean score (⟦SLOT_19⟧5.5). Also, ratings of roughly half of the photos in AVA dataset have a standard deviation greater than 1.4. As pointed out in [1], presumably images with high score variance tend to be subject to interpretation, whereas images with low score variance seem to represent conventional styles or subject matter. A few examples with ratings associated with different levels of aesthetic quality and unconventionality are illustrated in Fig. 2. It seems that aesthetic quality of a photograph can be represented by the mean score, and unconventionality of it closely correlates to the score deviation. Given the distribution of AVA scores, typically, training a model on AVA data results in predictions with small deviations around the overall mean (5.5).

**ZH** AVA 数据集包含约 255,000 幅图像，由业余摄影者依据美学质量打分（AVA 图像取自 www.dpchallenge.com，一个面向业余摄影者的在线社区）。每幅照片平均由约 200 人在摄影比赛的语境下评分，并关联到某一挑战主题，AVA 中共有近 900 个不同的比赛。评分范围为 1 到 10，10 为图像可获得的最高美学分。AVA 评分的直方图见图 1。可以看到，平均分集中在全局均分（⟦SLOT_19⟧5.5）附近；约半数照片的评分标准差大于 1.4。正如[1]所指出的，方差大的图像往往见仁见智，方差小的图像则通常代表常规的风格或题材。图 2 给出若干具有不同美学质量与非常规性水平的示例及其评分。看来一幅照片的美学质量可由均分刻画，而其非常规性与分数的离散程度密切相关。鉴于 AVA 分数的分布形态，在 AVA 数据上训练模型，其预测通常落在全局均值（5.5）附近的窄区间内。

**EN** It is worth mentioning that the joint histogram in Fig. 1 shows higher deviations for very low/high ratings (compared to the overall mean 5.5, and mean standard deviation 1.43). In other words, divergence of opinion is more consistent in AVA images with extreme aesthetic qualities. As discussed in [1], distribution of ratings with mean value between 2 and 8 can be closely approximated by Gaussian functions, and highly skewed ratings can be modeled by Gamma distributions.

**ZH** 值得一提的是，图 1 的联合直方图显示，评分极低或极高的图像（相对全局均值 5.5 与平均标准差 1.43）偏差更大。换言之，在美学特质趋于极端的 AVA 图像上，意见分歧更为一致地出现。如[1]所讨论的，均值在 2 到 8 之间的评分分布可以很好地用高斯函数逼近，而高度偏斜的评分可用 Gamma 分布建模。

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

**EN** Fig. 3: Histograms of ratings from TID2013 dataset[2]. Left: Histogram of mean scores. Middle: Histogram of standard deviations. Right: Joint histogram of the mean and standard deviation.

**ZH** 图 3：TID2013 数据集[2]的评分直方图。左：均分直方图；中：标准差直方图；右：均值与标准差的联合直方图。

**EN** I-D Tampere Image Database 2013 (TID2013) [2]

**ZH** I-D 坦佩雷图像数据库 2013（TID2013）[2]

**EN** TID2013 is curated for evaluation of full-reference perceptual image quality. It contains 3000 images, from 25 reference (clean) images (Kodak images [25]), 24 types of distortions with 5 levels for each distortion. This leads to 120 distorted images for each reference image; including different types of distortions such as compression artifacts, noise, blur and color artifacts.

**ZH** TID2013 面向全参考感知图像质量评价而构建，包含 3000 幅图像，源自 25 幅参考（干净）图像（Kodak 图像[25]），涵盖 24 种失真类型、每种失真 5 个等级，即每幅参考图像对应 120 幅失真图像，失真类型包括压缩伪影、噪声、模糊和颜色伪影等。

**EN** Human ratings of TID2013 images are collected through a forced choice experiment, where observers select a better image between two distorted choices. Set up of the experiment allows raters to view the reference image while making a decision. In each experiment, every distorted image is used in 9 random pairwise comparisons. The selected image gets one point, and other image gets zero points. At the end of the experiment, sum of the points is used as the quality score associated with an image (this leads to scores ranging from 0 to 9). To obtain the overall mean scores, total of 985 experiments are carried out.

**ZH** TID2013 的人类评分通过强制选择实验采集：观察者在两幅失真图像中选择更优的一幅。实验设置允许评分者在决策时查看参考图像。每轮实验中，每幅失真图像参与 9 次随机两两比较；被选中的图像得 1 分，另一幅得 0 分。实验结束时以得分之和作为该图像的质量分数（因此分数范围为 0 到 9）。为得到总体均分，共进行了 985 轮实验。

**EN** Mean and standard deviation of TID2013 ratings are shown in Fig. 3. As can be seen in Fig. 3(c), the mean and score deviation values are weakly correlated. A few images from TID2013 are illustrated in Fig. 4 and Fig. 5. All five levels of JPEG compression artifacts and the respective ratings are illustrated in Fig. 4. Evidently higher distortion level leads to lower mean score22 2 This is a quite consistent trend for most of the other distortions too (namely noise, blur and color distortions). However, in case of the contrast change (Fig. 5), this trend is not obvious. This is due to the order of contrast compression/stretching from level 1 to level 5). Effect of contrast compression/stretching distortion on the human ratings is demonstrated in Fig. 5. Interestingly, stretch of contrast (Fig. 5(c) and Fig. 5(e)) leads to relatively higher perceptual quality.

**ZH** TID2013 评分的均值与标准差见图 3。从图 3(c) 可见，均值与分数离散度之间相关性较弱。图 4 与图 5 给出 TID2013 的若干示例图像：图 4 展示 JPEG 压缩伪影的全部五个等级及相应评分。显然，失真等级越高，均分越低（对噪声、模糊和颜色失真等大多数其他失真类型，这一趋势也相当一致；但在对比度变化（图 5）情形下趋势并不明显，这是由等级 1 到等级 5 的对比度压缩／拉伸顺序造成的）。图 5 给出对比度压缩／拉伸失真对人类评分的影响。有意思的是，对比度拉伸（图 5(c) 与图 5(e)）反而带来相对更高的感知质量。

**EN** I-E LIVE In the Wild Image Quality Challenge Database [26]

**ZH** I-E LIVE 真实场景图像质量挑战数据库 [26]

**EN** LIVE dataset contains 1162 photos captured by mobile devices. Each image is rated by an average of 175 unique subjects. Mean and standard deviation of LIVE ratings are shown in Fig. 6. As can be seen in the joint histogram, images that are rated near overall mean score show higher standard deviation. A few images from LIVE dataset are illustrated in Fig. 7. It is worth noting that in this paper, LIVE scores are scaled to ⟦SLOT_20⟧.

**ZH** LIVE 数据集包含 1162 幅由移动设备拍摄的照片，每幅图像平均由 175 名不同受试者评分。LIVE 评分的均值与标准差见图 6。由联合直方图可见，评分接近全局均值的图像标准差反而更高。图 7 给出 LIVE 数据集的若干示例图像。需要说明的是，本文将 LIVE 分数缩放到 ⟦SLOT_20⟧。

**EN** Unlike AVA, which includes distribution of ratings for each image, TID2013 and LIVE only provide mean and standard deviation of the opinion scores. Since our proposed method requires training on score probabilities, the score distributions are approximated through maximum entropy optimization [27].

**ZH** AVA 提供每幅图像的评分分布，而 TID2013 与 LIVE 只给出意见分数的均值与标准差。由于本文方法需要在分数概率上训练，评分分布通过最大熵优化[27]来逼近。

**EN** The rest of the paper is organized as follows. In Section II, a detailed explanation of the proposed method is described. Next, in SectionIII, applications of our algorithm in ranking photos and image enhancement are exemplified. We also provide details of our implementation. Finally, this paper is concluded in SectionIV.

**ZH** 本文其余部分安排如下：第二节详述所提方法；第三节给出该算法在照片排序与图像增强中的应用示例，并说明实现细节；第四节总结全文。

<!-- [原子块 · img]  -->

**EN** (a) clean image

**ZH** (a) 干净图像

<!-- [原子块 · img]  -->

**EN** (b) ⟦SLOT_21⟧

**ZH** (b) ⟦SLOT_21⟧

<!-- [原子块 · img]  -->

**EN** (c) ⟦SLOT_22⟧

**ZH** (c) ⟦SLOT_22⟧

<!-- [原子块 · img]  -->

**EN** (d) ⟦SLOT_23⟧

**ZH** (d) ⟦SLOT_23⟧

<!-- [原子块 · img]  -->

**EN** (e) ⟦SLOT_24⟧

**ZH** (e) ⟦SLOT_24⟧

<!-- [原子块 · img]  -->

**EN** (f) ⟦SLOT_25⟧

**ZH** (f) ⟦SLOT_25⟧

**EN** Fig. 4: JPEG artifact example images from TID2013 dataset[2] with quality score ⟦SLOT_26⟧, where ⟦SLOT_27⟧ and ⟦SLOT_28⟧ represent mean and standard deviation of score, respectively. Clean image and 5 levels of JPEG compression artifacts are shown here. (a) clean image, (b) compression artifact level 1, ⟦SLOT_29⟧, ⟦SLOT_30⟧, (c) compression artifact level 2, ⟦SLOT_31⟧, ⟦SLOT_32⟧, (d) compression artifact level 3, ⟦SLOT_33⟧, ⟦SLOT_34⟧, (e) compression artifact level 4, ⟦SLOT_35⟧, ⟦SLOT_36⟧, (f) compression artifact level 5, ⟦SLOT_37⟧, ⟦SLOT_38⟧.

**ZH** 图 4：TID2013 数据集[2]中 JPEG 伪影的示例图像，质量分数记为 ⟦SLOT_26⟧，其中 ⟦SLOT_27⟧ 与 ⟦SLOT_28⟧ 分别表示分数的均值与标准差。此处展示干净图像与 5 个等级的 JPEG 压缩伪影。(a) 干净图像；(b) 压缩伪影等级 1，⟦SLOT_29⟧，⟦SLOT_30⟧；(c) 压缩伪影等级 2，⟦SLOT_31⟧，⟦SLOT_32⟧；(d) 压缩伪影等级 3，⟦SLOT_33⟧，⟦SLOT_34⟧；(e) 压缩伪影等级 4，⟦SLOT_35⟧，⟦SLOT_36⟧；(f) 压缩伪影等级 5，⟦SLOT_37⟧，⟦SLOT_38⟧。

<!-- [原子块 · img]  -->

**EN** (a) clean image

**ZH** (a) 干净图像

<!-- [原子块 · img]  -->

**EN** (b) ⟦SLOT_39⟧

**ZH** (b) ⟦SLOT_39⟧

<!-- [原子块 · img]  -->

**EN** (c) ⟦SLOT_40⟧

**ZH** (c) ⟦SLOT_40⟧

<!-- [原子块 · img]  -->

**EN** (d) ⟦SLOT_41⟧

**ZH** (d) ⟦SLOT_41⟧

<!-- [原子块 · img]  -->

**EN** (e) ⟦SLOT_42⟧

**ZH** (e) ⟦SLOT_42⟧

<!-- [原子块 · img]  -->

**EN** (f) ⟦SLOT_43⟧

**ZH** (f) ⟦SLOT_43⟧

**EN** Fig. 5: Some example images from TID2013 dataset[2] with quality score ⟦SLOT_44⟧, where ⟦SLOT_45⟧ and ⟦SLOT_46⟧ represent mean and standard deviation of score, respectively. Clean image and 5 levels of contrast change distortions are shown here. (a) clean image, (b) contrast change distortion of level 1, ⟦SLOT_47⟧, ⟦SLOT_48⟧, (c) contrast change distortion of level 2, ⟦SLOT_49⟧, ⟦SLOT_50⟧, (d) contrast change distortion of level 3, ⟦SLOT_51⟧, ⟦SLOT_52⟧, (e) contrast change distortion of level 4, ⟦SLOT_53⟧, ⟦SLOT_54⟧, (f) contrast change distortion of level 5, ⟦SLOT_55⟧, ⟦SLOT_56⟧.

**ZH** 图 5：TID2013 数据集[2]的若干示例图像，质量分数记为 ⟦SLOT_44⟧，其中 ⟦SLOT_45⟧ 与 ⟦SLOT_46⟧ 分别表示分数的均值与标准差。此处展示干净图像与 5 个等级的对比度变化失真。(a) 干净图像；(b) 对比度变化失真等级 1，⟦SLOT_47⟧，⟦SLOT_48⟧；(c) 对比度变化失真等级 2，⟦SLOT_49⟧，⟦SLOT_50⟧；(d) 对比度变化失真等级 3，⟦SLOT_51⟧，⟦SLOT_52⟧；(e) 对比度变化失真等级 4，⟦SLOT_53⟧，⟦SLOT_54⟧；(f) 对比度变化失真等级 5，⟦SLOT_55⟧，⟦SLOT_56⟧。

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

**EN** Fig. 6: Histograms of ratings from LIVE dataset [26]. Left: Histogram of mean scores. Middle: Histogram of standard deviations. Right: Joint histogram of the mean and standard deviation. Note that LIVE scores are scaled to [1,10].

**ZH** 图 6：LIVE 数据集[26]的评分直方图。左：均分直方图；中：标准差直方图；右：均值与标准差的联合直方图。注意 LIVE 分数已缩放到 [1,10]。

<!-- [原子块 · img]  -->

**EN** (a) ⟦SLOT_57⟧

**ZH** (a) ⟦SLOT_57⟧

<!-- [原子块 · img]  -->

**EN** (b) ⟦SLOT_58⟧

**ZH** (b) ⟦SLOT_58⟧

<!-- [原子块 · img]  -->

**EN** (c) ⟦SLOT_59⟧

**ZH** (c) ⟦SLOT_59⟧

<!-- [原子块 · img]  -->

**EN** (d) ⟦SLOT_60⟧

**ZH** (d) ⟦SLOT_60⟧

<!-- [原子块 · img]  -->

**EN** (e) ⟦SLOT_61⟧

**ZH** (e) ⟦SLOT_61⟧

<!-- [原子块 · img]  -->

**EN** (f) ⟦SLOT_62⟧

**ZH** (f) ⟦SLOT_62⟧

**EN** Fig. 7: Some example images from LIVE dataset [26] with quality score ⟦SLOT_63⟧, where ⟦SLOT_64⟧ and ⟦SLOT_65⟧ represent mean and standard deviation of score, respectively. Note that LIVE scores are scaled to [1,10].

**ZH** 图 7：LIVE 数据集[26]的若干示例图像，质量分数记为 ⟦SLOT_63⟧，其中 ⟦SLOT_64⟧ 与 ⟦SLOT_65⟧ 分别表示分数的均值与标准差。注意 LIVE 分数已缩放到 [1,10]。

**EN** II Proposed Method

**ZH** II 本文方法

**EN** Fig. 8: Modified baseline image classifier network used in our framework. Last layer of classifier network is replaced by a fully-connected layer to output 10 classes of quality scores. Baseline network weights are initialized by training on ImageNet dataset [15], and the added fully-connected weights are initialized randomly.

**ZH** 图 8：本框架中使用的改造后基线图像分类网络。分类器网络的最后一层被替换为输出 10 类质量分数的全连接层。基线网络权重通过在 ImageNet 数据集[15]上训练来初始化，新增全连接层的权重随机初始化。

<!-- [原子块 · img]  -->

**EN** Our proposed quality and aesthetic predictor stands on image classifier architectures. More explicitly, we explore a few different classifier architectures such as VGG16 [18], Inception-v2 [28], and MobileNet [29] for image quality assessment task. VGG16 consists of 13 convolutional and 3 fully-connected layers. Small convolution filters of size ⟦SLOT_66⟧ are used in the deep VGG16 architecture [18]. Inception-v2 [28] is based on the Inception module [30] which allows for parallel use of convolution and pooling operations. Also, in the Inception architecture, traditional fully-connected layers are replaced by average pooling, which leads to a significant reduction in number of parameters. MobileNet [29] is an efficient deep CNN, mainly designed for mobile vision applications. In this architecture, dense convolutional filters are replaced by separable filters. This simplification results in smaller and faster CNN models.

**ZH** 本文的质量与美学预测器建立在图像分类器结构之上。具体地，我们考察了 VGG16 [18]、Inception-v2 [28] 和 MobileNet [29] 等多种分类器结构用于图像质量评价任务。VGG16 含 13 个卷积层和 3 个全连接层，其深层结构中使用 ⟦SLOT_66⟧ 的小卷积核[18]。Inception-v2 [28] 基于 Inception 模块[30]，允许卷积与池化操作并行使用；同时该结构以平均池化取代传统的全连接层，显著减少了参数量。MobileNet [29] 是主要为移动视觉应用设计的高效深度 CNN，以可分离滤波器取代密集卷积滤波器，从而得到更小更快的 CNN 模型。

**EN** We replaced the last layer of the baseline CNN with a fully-connected layer with 10 neurons followed by soft-max activations (shown in Fig. 8). Baseline CNN weights are initialized by training on the ImageNet dataset [15], and then an end-to-end training on quality assessment is performed. In this paper, we discuss performance of the proposed model with various baseline CNNs.

**ZH** 我们把基线 CNN 的最后一层替换为含 10 个神经元、后接 softmax 激活的全连接层（见图 8）。基线 CNN 权重先在 ImageNet 数据集[15]上训练初始化，随后执行质量评价的端到端训练。本文讨论了采用不同基线 CNN 时该模型的性能。

**EN** In training, input images are rescaled to ⟦SLOT_67⟧, and then a crop of size ⟦SLOT_68⟧ is randomly extracted. This lessens potential over-fitting issues, especially when training on relatively small datasets (e.g. TID2013). It is worth noting that we also tried training with random crops without rescaling. However, results were not compelling. This is due to the inevitable change in image composition. Another random data augmentation in our training process is horizontal flipping of the image crops.

**ZH** 训练时，输入图像先缩放到 ⟦SLOT_67⟧，再随机裁取 ⟦SLOT_68⟧ 大小的区域。这减轻了潜在的过拟合问题，在 TID2013 等较小数据集上尤为明显。值得一提的是，我们也尝试过不缩放而直接随机裁剪训练，但结果并不理想，原因是图像构图会不可避免地改变。训练中另一项随机数据增强是对图像块做水平翻转。

**EN** Our goal is to predict the distribution of ratings for a given image. Ground truth distribution of human ratings of a given image can be expressed as an empirical probability mass function ⟦SLOT_69⟧ with ⟦SLOT_70⟧, where ⟦SLOT_71⟧ denotes the ⟦SLOT_72⟧th score bucket, and ⟦SLOT_73⟧ denotes the total number of score buckets. In both AVA and TID2013 datasets ⟦SLOT_74⟧, in AVA, ⟦SLOT_75⟧ and ⟦SLOT_76⟧, and in TID ⟦SLOT_77⟧ and ⟦SLOT_78⟧. Since ⟦SLOT_79⟧, ⟦SLOT_80⟧ represents the probability of a quality score falling in the ⟦SLOT_81⟧th bucket. Given the distribution of ratings as p, mean quality score is defined as ⟦SLOT_82⟧, and standard deviation of the score is computed as ⟦SLOT_83⟧. As discussed in the previous section, one can qualitatively compare images by mean and standard deviation of scores.

**ZH** 我们的目标是预测给定图像的评分分布。该图像人类评分的真实分布可表示为经验概率质量函数 ⟦SLOT_69⟧，其中 ⟦SLOT_70⟧，⟦SLOT_71⟧ 表示第 ⟦SLOT_72⟧ 个分数区间，⟦SLOT_73⟧ 表示分数区间总数。AVA 与 TID2013 数据集中均有 ⟦SLOT_74⟧：AVA 中 ⟦SLOT_75⟧、⟦SLOT_76⟧，TID 中 ⟦SLOT_77⟧、⟦SLOT_78⟧。由于 ⟦SLOT_79⟧，⟦SLOT_80⟧ 表示质量分数落在第 ⟦SLOT_81⟧ 个区间内的概率。给定分布 p，平均质量分数定义为 ⟦SLOT_82⟧，分数标准差计算为 ⟦SLOT_83⟧。如上一节所述，可以借助分数的均值与标准差对图像做定性比较。

**EN** Each example in the dataset consists of an image and its ground truth (user) ratings p. Our objective is to find the probability mass function ⟦SLOT_84⟧ that is an accurate estimate of p. Next, our training loss function is discussed.

**ZH** 数据集中每个样本由一幅图像及其真实（用户）评分 p 构成。我们的目标是求得概率质量函数 ⟦SLOT_84⟧，使其成为 p 的准确估计。下面讨论训练损失函数。

**EN** II-A Loss Function

**ZH** II-A 损失函数

**EN** Soft-max cross-entropy is widely used as training loss in classification tasks. This loss can be represented as ⟦SLOT_85⟧ (where ⟦SLOT_86⟧ denotes estimated probability of ⟦SLOT_87⟧th score bucket) to maximize predicted probability of the correct labels. However, in the case of ordered-classes (e.g. aesthetic and quality estimation), cross-entropy loss lacks the inter-class relationships between score buckets. One might argue that ordered-classes can be represented by a real number, and consequently, can be learned through a regression framework. Yet, it has been shown that for ordered classes, the classification frameworks can outperform regression models [21, 31]. Hou et al. [21] show that training on datasets with intrinsic ordering between classes can benefit from EMD-based losses. These loss functions penalize mis-classifications according to class distances.

**ZH** softmax 交叉熵是分类任务中广泛使用的训练损失，可表示为 ⟦SLOT_85⟧（其中 ⟦SLOT_86⟧ 表示第 ⟦SLOT_87⟧ 个分数区间的估计概率），其作用是最大化正确标签的预测概率。但在有序类别（如美学与质量估计）情形下，交叉熵损失缺少分数区间之间的类别间关系。有人或许认为有序类别可以用实数表示，因而能够通过回归框架学习；然而研究表明，对有序类别，分类框架可以优于回归模型[21, 31]。Hou 等人[21]指出，在类别间存在内在顺序的数据集上训练，可受益于基于 EMD 的损失——这类损失依据类别距离惩罚误分类。

**EN** For image quality ratings, classes are inherently ordered as ⟦SLOT_88⟧, and ⟦SLOT_89⟧norm distance between classes is defined as ⟦SLOT_90⟧, where ⟦SLOT_91⟧. EMD is defined as the minimum cost to move the mass of one distribution to another. Given the ground truth and estimated probability mass functions p and ⟦SLOT_92⟧, with ⟦SLOT_93⟧ ordered classes of distance ⟦SLOT_94⟧, the normalized Earth Mover’s Distance can be expressed as [32]:

**ZH** 对图像质量评分而言，类别天然按 ⟦SLOT_88⟧ 排序，类别间的 ⟦SLOT_89⟧ 范数距离定义为 ⟦SLOT_90⟧，其中 ⟦SLOT_91⟧。EMD 定义为把一个分布的质量搬运到另一个分布所需的最小代价。给定真实与估计的概率质量函数 p 和 ⟦SLOT_92⟧，在 ⟦SLOT_93⟧ 个类别、类别距离为 ⟦SLOT_94⟧ 时，归一化的推土机距离可表示为[32]：

<!-- [原子块 · table] EMD ​ ( p , p ^ ) = ( 1 N ​ ∑ k = 1 N | CDF p ​ ( k ) − CDF p ^ ​ ( k ) | r ) 1 / r \mbox{EMD}(\textbf{p},\widehat{\textbf{p}})=\left(\frac{1}{N}\sum_{k=1}^{N}|\mbox{CDF}_{\textbf{p}}(k)-\mbox{CDF}_{\ -->

**EN** where ⟦SLOT_95⟧ is the cumulative distribution function as ⟦SLOT_96⟧. It is worth noting that this closed-form solution requires both distributions to have equal mass as ⟦SLOT_97⟧. As shown in Fig. 8, our predicted quality probabilities are fed to a soft-max function to guarantee that ⟦SLOT_98⟧. Similar to [21], in our training framework, ⟦SLOT_99⟧ is set as 2 to penalize the Euclidean distance between the CDFs. ⟦SLOT_100⟧ allows easier optimization when working with gradient descent.

**ZH** 其中 ⟦SLOT_95⟧ 为累积分布函数 ⟦SLOT_96⟧。值得注意的是，该闭式解要求两个分布质量相等，即 ⟦SLOT_97⟧。如图 8 所示，我们预测的质量概率会送入 softmax 函数，以保证 ⟦SLOT_98⟧。与[21]类似，本文训练框架取 ⟦SLOT_99⟧ 为 2，以惩罚累积分布函数之间的欧氏距离；⟦SLOT_100⟧ 使梯度下降下的优化更容易。

**EN** III Experimental Results

**ZH** III 实验结果

**EN** We train two separate models for aesthetics and technical quality assessment on AVA, TID2013, and LIVE. For each case, we split each dataset into train and test sets, such that 20% of the data is used for testing. In this section, performance of the proposed models on the test sets are discussed and compared to the existing methods. Then, applications of the proposed technique in photo ranking and image enhancement are explored. Before moving forward, details of our implementation are explained.

**ZH** 我们在 AVA、TID2013 与 LIVE 上分别训练美学评价与技术质量评价两个模型。每种情形下，数据集按 8:2 划分为训练集与测试集。本节讨论所提模型在测试集上的性能并与现有方法比较，随后探索该技术在照片排序与图像增强中的应用。在此之前，先说明实现细节。

**EN** The CNNs presented in this paper are implemented using TensorFlow [33, 34]. The baseline CNN weights are initialized by training on ImageNet [15], and the last fully-connected layer is randomly initialized. The weight and bias momentums are set to 0.9, and a dropout rate of 0.75 is applied on the last layer of the baseline network. The learning rate of the baseline CNN layers and the last fully-connected layers are set as ⟦SLOT_101⟧ and ⟦SLOT_102⟧, respectively. We observed that setting a low learning rate on baseline CNN layers results in easier and faster optimization when using stochastic gradient descent. Also, after every 10 epochs of training, an exponential decay with decay factor 0.95 is applied to all learning rates.

**ZH** 本文的 CNN 均用 TensorFlow [33, 34] 实现。基线 CNN 权重通过在 ImageNet [15] 上训练初始化，最后的全连接层随机初始化。权重与偏置的动量设为 0.9，基线网络最后一层施加 0.75 的 dropout 率。基线 CNN 层与最后全连接层的学习率分别设为 ⟦SLOT_101⟧ 与 ⟦SLOT_102⟧。我们发现，在基线 CNN 层上设置较小的学习率，能使随机梯度下降下的优化更轻松、更快速。此外，每训练 10 个轮次，对所有学习率施加衰减因子为 0.95 的指数衰减。

**EN** III-A Performance Comparisons

**ZH** III-A 性能比较

**EN** Accuracy, correlation and EMD values of our evaluations on the aesthetic assessment model on AVA are presented in Table I. Most methods in Table I are designed to perform binary classification on the aesthetic scores, and as a result, only accuracy evaluations of two-class quality categorization are reported. In this binary classification, predicted mean scores are compared to ⟦SLOT_103⟧ as cut-off score. Images with predicted scores above the cut-off score are categorized as high quality. In two-class aesthetic categorization task, results from [20], and NIMA(Inception-v2) show the highest accuracy. Also, in terms of rank correlation, NIMA(VGG16) and NIMA(Inception-v2) outperform [14]. NIMA is much cheaper: [20] applies multiple VGG16 nets on image patches to generate a single quality score, whereas computational complexity of NIMA(Inception-v2) is roughly one pass of Inception-v2 (see Table V).

**ZH** 表 I 给出美学评价模型在 AVA 上的准确率、相关系数与 EMD 值。表 I 中多数方法针对美学分数做二分类，因此只报告两类质量划分的准确率。该二分类以 ⟦SLOT_103⟧ 为 cut-off 分数比较预测均分，高于 cut-off 的判为高质量。在两类美学划分任务上，[20]与 NIMA(Inception-v2) 的准确率最高；就等级相关性而言，NIMA(VGG16) 与 NIMA(Inception-v2) 优于[14]。而 NIMA 的开销要低得多：[20]需在图像块上运行多个 VGG16 网络才能得到单个质量分数，NIMA(Inception-v2) 的计算量大致只相当于一次 Inception-v2 前向（见表 V）。

**EN** Our technical quality assessment model on TID2013 is compared to other existing methods in Table II. While most of these methods regress to the mean opinion score, our proposed technique predicts the distribution of ratings, as well as mean opinion score. Correlation between ground truth and results of NIMA(VGG16) are close to the state-of-the-art results in [35] and [7]. It is worth highlighting that Bianco et al. [7] feed multiple image crops to a deep CNN, whereas our method takes only the rescaled image.

**ZH** 表 II 将本文在 TID2013 上的技术质量评价模型与现有方法比较。这些方法多数回归到平均意见分数，而本文方法同时预测评分分布与平均意见分数。真实值与 NIMA(VGG16) 结果的相关性已接近[35]与[7]的最优结果。值得指出的是，Bianco 等人[7]需向深度 CNN 输入多个图像裁剪，而本文方法只需缩放后的整图。

**EN** The predicted distributions of AVA scores are presented in Fig. 9. We used NIMA(Inception-v2) model to predict the ground truth scores from our AVA test set. As can be seen, distribution of the ground truth mean scores is closely predicted by NIMA. However, predicting distribution of the ground truth standard deviations is a more challenging task. As we discussed previously, unconventionality of subject matter or style has a direct impact on score standard deviations.

**ZH** 图 9 给出 AVA 分数的预测分布。我们使用 NIMA(Inception-v2) 模型预测 AVA 测试集的真实分数。可以看到，NIMA 对真实均分分布的预测相当贴近；然而预测真实标准差的分布更具挑战性。正如前文所述，题材或风格的非常规性会直接影响分数的标准差。

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

**EN** Fig. 9: Histograms of the ground truth and predicted scores using NIMA(Inception-v2) applied on our AVA test set. Left: histograms of mean scores. Right: histograms of standard deviations.

**ZH** 图 9：用 NIMA(Inception-v2) 在 AVA 测试集上得到的真实分数与预测分数的直方图。左：均分直方图；右：标准差直方图。

**EN** TABLE I: Performance of the proposed method with various architectures in predicting AVA quality ratings [1] compared to the state-of-the-art. Reported accuracy values are based on classification of photos to two classes (column 2). LCC (linear correlation coefficient) and SRCC (Spearman’s rank correlation coefficient) are computed between predicted and ground truth mean scores (column 3 and 4) and standard deviation of scores (column 5 and 6). EMD measures closeness of the predicted and ground truth rating distributions with ⟦SLOT_104⟧ in Eq. 1. The accuracy, LCC, and SROC values are in ⟦SLOT_105⟧, ⟦SLOT_106⟧, and ⟦SLOT_107⟧ within ⟦SLOT_108⟧ confidence, respectively.

**ZH** 表 I：所提方法采用不同结构预测 AVA 质量评分[1]时与最优方法的性能比较。所列准确率基于将照片分为两类（第 2 列）。LCC（线性相关系数）与 SRCC（斯皮尔曼等级相关系数）分别在预测与真实均分（第 3、4 列）以及分数标准差（第 5、6 列）之间计算。EMD 用式 1 中 ⟦SLOT_104⟧ 度量预测与真实评分分布的接近程度。准确率、LCC 与 SRCC 值分别在 ⟦SLOT_105⟧、⟦SLOT_106⟧ 与 ⟦SLOT_107⟧ 范围内，置信度为 ⟦SLOT_108⟧。

<!-- [原子块 · table] Model Accuracy LCC SRCC LCC SRCC EMD (2 classes) (mean) (mean) (std.dev) (std.dev) Murray et al. [ 1 ] 66.70% – – – – – Kao et al. [ 9 ] 71.42% – – – – – Lu et al. [ 36 ] 74.46% – – – – – Lu et al. [  -->

**EN** III-B Cross Dataset Evaluation

**ZH** III-B 跨数据集评估

**EN** As a cross validation test, performance of our trained models are measured on other datasets. These results are presented in Table III and Table IV. We test NIMA(Inception-v2) model trained on AVA, TID2013 [2] and LIVE [26] across all three test sets. As can be seen, on average, training on AVA dataset shows the best performance. For instance, training on AVA and testing on LIVE results in ⟦SLOT_109⟧ and ⟦SLOT_110⟧ linear and rank correlations, respectively. However, training on LIVE and testing on AVA leads to ⟦SLOT_111⟧ and ⟦SLOT_112⟧ linear and rank correlation coefficients. We believe this observation shows that NIMA models trained on AVA can generalize to other test examples more effectively, whereas training on TID2013 results in poor performance on LIVE and AVA test sets. It is worth mentioning that AVA dataset contains roughly 250 times more examples (in comparison to the LIVE dataset), which allows training NIMA models without any significant overfitting.

**ZH** 作为交叉验证，我们在其他数据集上测量了所训模型的性能，结果见表 III 与表 IV。我们把在 AVA、TID2013 [2] 与 LIVE [26] 上训练的 NIMA(Inception-v2) 模型分别用于三套测试集。总体来看，在 AVA 上训练表现最佳：例如在 AVA 训练、LIVE 测试可得 ⟦SLOT_109⟧ 的线性相关与 ⟦SLOT_110⟧ 的等级相关；反之在 LIVE 训练、AVA 测试只有 ⟦SLOT_111⟧ 与 ⟦SLOT_112⟧ 的线性和等级相关系数。我们认为这说明在 AVA 上训练的 NIMA 模型能更有效地泛化到其他测试样本，而在 TID2013 上训练则在 LIVE 与 AVA 测试集上表现较差。值得一提的是，AVA 数据集的样本量约为 LIVE 的 250 倍，这使得 NIMA 模型训练时不会出现明显过拟合。

**EN** III-C Photo Ranking

**ZH** III-C 照片排序

**EN** Predicted mean scores can be used to rank photos, aesthetically. Some test photos from AVA dataset are ranked in Fig. 10 and Fig. 11. Predicted NIMA scores and ground truth AVA scores are shown below each image. Results in Fig. 10 suggest that in addition to image content, other factors such as tone, contrast and composition of photos are important aesthetic qualities. Also, as shown in Fig. 11, besides image semantics, framing and color palette are key qualities in these photos. These aesthetic attributes are closely predicted by our trained models on AVA.

**ZH** 预测的均分可用于照片的美学排序。图 10 与图 11 给出 AVA 数据集中若干测试照片的排序结果，每幅图像下方标注了 NIMA 预测分数与 AVA 真实分数。图 10 的结果说明，除图像内容外，色调、对比度与构图等因素也是重要的美学特质；图 11 则显示，除图像语义外，取景与色彩搭配是这些照片的关键特质。这些美学属性都被我们在 AVA 上训练的模型较好地预测出来。

**EN** Predicted mean scores are used to qualitatively rank photos in Fig. 12. These images are part of our TID2013 test set, which contain various types and levels of distortions. Comparing ground truth and predicted scores indicates that our trained model on TID2013 accurately ranks the test images.

**ZH** 图 12 用预测均分对照片做定性排序。这些图像来自 TID2013 测试集，包含不同类型与等级的失真。对比真实与预测分数可知，在 TID2013 上训练的模型能准确排序测试图像。

<!-- [原子块 · img]  -->

**EN** (a) 6.38 (7.16)

**ZH** (a) 6.38 (7.16)

<!-- [原子块 · img]  -->

**EN** (b) 6.24 (6.79)

**ZH** (b) 6.24 (6.79)

<!-- [原子块 · img]  -->

**EN** (c) 6.22 (6.64)

**ZH** (c) 6.22 (6.64)

<!-- [原子块 · img]  -->

**EN** (d) 6.16 (6.93)

**ZH** (d) 6.16 (6.93)

<!-- [原子块 · img]  -->

**EN** (e) 5.92 (6.23)

**ZH** (e) 5.92 (6.23)

<!-- [原子块 · img]  -->

**EN** (f) 5.71 (5.78)

**ZH** (f) 5.71 (5.78)

<!-- [原子块 · img]  -->

**EN** (g) 5.61 (5.54)

**ZH** (g) 5.61 (5.54)

<!-- [原子块 · img]  -->

**EN** (h) 5.28 (5.32)

**ZH** (h) 5.28 (5.32)

<!-- [原子块 · img]  -->

**EN** (i) 5.11 (5.23)

**ZH** (i) 5.11 (5.23)

<!-- [原子块 · img]  -->

**EN** (j) 5.03 (5.35)

**ZH** (j) 5.03 (5.35)

<!-- [原子块 · img]  -->

**EN** (k) 4.90 (4.91)

**ZH** (k) 4.90 (4.91)

<!-- [原子块 · img]  -->

**EN** (l) 4.83 (4.89)

**ZH** (l) 4.83 (4.89)

<!-- [原子块 · img]  -->

**EN** (m) 4.77 (4.55)

**ZH** (m) 4.77 (4.55)

<!-- [原子块 · img]  -->

**EN** (n) 4.48 (3.95)

**ZH** (n) 4.48 (3.95)

<!-- [原子块 · img]  -->

**EN** (o) 3.55 (3.53)

**ZH** (o) 3.55 (3.53)

**EN** Fig. 10: Ranking some examples labelled with “landscape” tag from AVA dataset[1] using our proposed aesthetic assessment model NIMA(VGG16). Predicted (and ground truth) scores are shown below each image.

**ZH** 图 10：用本文美学评价模型 NIMA(VGG16) 对 AVA 数据集[1]中标注为“landscape”的示例排序。每幅图像下方为预测分数（括号内为真实分数）。

**EN** TABLE II: Performance of the proposed method with various architectures in predicting TID2013 quality ratings [2] compared to the state-of-the-art. LCC (linear correlation coefficient) and SRCC (Spearman’s rank correlation coefficient) are computed between predicted and ground truth mean scores (column 2 and 3) and standard deviation of scores (column 4 and 5). EMD measures closeness of the predicted and ground truth rating distributions with ⟦SLOT_113⟧ in Eq. 1. The LCC, and SROC values are in ⟦SLOT_114⟧, and ⟦SLOT_115⟧ within ⟦SLOT_116⟧ confidence, respectively.

**ZH** 表 II：所提方法采用不同结构预测 TID2013 质量评分[2]时与最优方法的性能比较。LCC（线性相关系数）与 SRCC（斯皮尔曼等级相关系数）分别在预测与真实均分（第 2、3 列）以及分数标准差（第 4、5 列）之间计算。EMD 用式 1 中 ⟦SLOT_113⟧ 度量预测与真实评分分布的接近程度。LCC 与 SRCC 值分别在 ⟦SLOT_114⟧ 与 ⟦SLOT_115⟧ 范围内，置信度为 ⟦SLOT_116⟧。

<!-- [原子块 · table] Model LCC SRCC LCC SRCC EMD (mean) (mean) (std.dev) (std.dev) Kim et al. [ 16 ] 0.80 0.80 – – – Moorthy et al. [ 39 ] 0.89 0.88 – – – Mittal et al. [ 40 ] 0.92 0.89 – – – Saad et al. [ 41 ] 0.91 0.88  -->

<!-- [原子块 · img]  -->

**EN** (a) 6.88 (7.40)

**ZH** (a) 6.88 (7.40)

<!-- [原子块 · img]  -->

**EN** (b) 6.63 (6.89)

**ZH** (b) 6.63 (6.89)

<!-- [原子块 · img]  -->

**EN** (c) 6.29 (6.59)

**ZH** (c) 6.29 (6.59)

<!-- [原子块 · img]  -->

**EN** (d) 5.86 (6.16)

**ZH** (d) 5.86 (6.16)

<!-- [原子块 · img]  -->

**EN** (e) 5.77 (5.52)

**ZH** (e) 5.77 (5.52)

<!-- [原子块 · img]  -->

**EN** (f) 5.51 (5.47)

**ZH** (f) 5.51 (5.47)

<!-- [原子块 · img]  -->

**EN** (g) 5.46 (5.38)

**ZH** (g) 5.46 (5.38)

<!-- [原子块 · img]  -->

**EN** (h) 5.24 (4.74)

**ZH** (h) 5.24 (4.74)

<!-- [原子块 · img]  -->

**EN** (i) 4.96 (4.83)

**ZH** (i) 4.96 (4.83)

<!-- [原子块 · img]  -->

**EN** (j) 4.90 (4.71)

**ZH** (j) 4.90 (4.71)

<!-- [原子块 · img]  -->

**EN** (k) 4.60 (4.59)

**ZH** (k) 4.60 (4.59)

<!-- [原子块 · img]  -->

**EN** (l) 4.53 (5.05)

**ZH** (l) 4.53 (5.05)

**EN** Fig. 11: Ranking some examples labelled with “sky” tag from AVA dataset[1] using our proposed aesthetic assessment model NIMA(Inception-v2). Predicted (and ground truth) scores are shown below each image.

**ZH** 图 11：用本文美学评价模型 NIMA(Inception-v2) 对 AVA 数据集[1]中标注为“sky”的示例排序。每幅图像下方为预测分数（括号内为真实分数）。

<!-- [原子块 · img]  -->

**EN** (a) 5.31 (5.93)

**ZH** (a) 5.31 (5.93)

<!-- [原子块 · img]  -->

**EN** (b) 4.35 (4.64)

**ZH** (b) 4.35 (4.64)

<!-- [原子块 · img]  -->

**EN** (c) 4.00 (3.91)

**ZH** (c) 4.00 (3.91)

<!-- [原子块 · img]  -->

**EN** (d) 3.56 (3.61)

**ZH** (d) 3.56 (3.61)

<!-- [原子块 · img]  -->

**EN** (e) 3.05 (3.26)

**ZH** (e) 3.05 (3.26)

<!-- [原子块 · img]  -->

**EN** (f) 2.87 (2.86)

**ZH** (f) 2.87 (2.86)

<!-- [原子块 · img]  -->

**EN** (g) 2.33 (2.44)

**ZH** (g) 2.33 (2.44)

<!-- [原子块 · img]  -->

**EN** (h) 1.67 (0.73)

**ZH** (h) 1.67 (0.73)

**EN** Fig. 12: Ranking some examples from TID2013 dataset[2] using our proposed quality assessment model NIMA(VGG16). Predicted (and ground truth) scores are shown below each image.

**ZH** 图 12：用本文质量评价模型 NIMA(VGG16) 对 TID2013 数据集[2]的若干示例排序。每幅图像下方为预测分数（括号内为真实分数）。

**EN** III-D Image Enhancement

**ZH** III-D 图像增强

**EN** Quality and aesthetic scores can be used to perceptually tune image enhancement operators. In other words, maximizing NIMA score as a prior can increase the likelihood of enhancing perceptual quality of an image. Typically, parameters of enhancement operators such as image denoising and contrast enhancement are selected by extensive experiments under various photographic conditions. Perceptual tuning could be quite expensive and time consuming, especially when human opinion is required. In this section, our proposed models are used to tune a tone enhancement method [43], and an image denoiser [44]. A more detailed treatment is presented in [23].

**ZH** 质量与美学分数可用于在感知层面调节图像增强算子。换言之，把最大化 NIMA 分数作为先验，能提高增强图像感知质量的可能。通常，图像去噪与对比度增强等算子的参数需要在各种拍摄条件下大量实验才能确定，而依赖人类意见的感知调参既昂贵又耗时。本节用所提模型调节一种色调增强方法[43]和一个图像去噪器[44]，更详细的讨论见[23]。

**EN** The multi-layer Laplacian technique [43] enhances local and global contrast of images. Parameters of this method control the amount of detail, shadow, and brightness of an image. Fig. 13 shows a few examples of the multi-layer Laplacian with different sets of parameters. We observed that the predicted aesthetic ratings from training on the AVA dataset can be improved by contrast adjustments. Consequently, our model is able to guide the multi-layer Laplacian filter to find aesthetically near-optimal settings of its parameters. Examples of this type of image editing are represented in Fig. 14, where a combination of detail, shadow and brightness change is applied on each image. In each example, 6 levels of detail boost, 11 levels of shadow change, and 11 levels of brightness change account for a total of 726 variations. The aesthetic assessment model tends to prefer high contrast images with boosted details. This is consistent with the ground truth results from AVA illustrated in Fig. 10.

**ZH** 多层拉普拉斯技术[43]可增强图像的局部与全局对比度，其参数控制图像的细节量、阴影与亮度。图 13 给出不同参数组合下多层拉普拉斯的若干示例。我们发现，对比度调整可以提升在 AVA 数据集上训练所得的美学预测评分，因此该模型能够引导多层拉普拉斯滤波器找到接近美学最优的参数设置。图 14 给出这类图像编辑的示例，每幅图像同时施加细节、阴影与亮度的组合变化：细节增强 6 档、阴影变化 11 档、亮度变化 11 档，共 726 种组合。美学评价模型倾向于偏好高对比度、细节增强的图像，这与图 10 中 AVA 的真实结果一致。

**EN** Turbo denoising [44] is a technique which uses the domain transform [45] as its core filter. Performance of Turbo denoising depends on spatial and range smoothing parameters, and consequently, proper tuning of these parameters can effectively boost performance of the denoiser. We observed that varying the spatial smoothing parameter makes the most significant perceptual difference, and as a result, we use our quality assessment model trained on TID2013 dataset to tune this denoiser. Application of our no-reference quality metric as a prior in image denoising is similar to the work of Zhu et al. [46, 47]. Our results are shown in Fig. 15. Additive white Gaussian noise with standard deviation 30 is added to the clean image, and Turbo denoising with various spatial parameters is used to denoise the noisy image. To reduce the score deviation, 50 random crops are extracted from denoised image. These scores are averaged to obtain the plots illustrated in Fig. 15. As can be seen, although the same amount of noise is added to each image, maximum quality scores correspond to different denoising parameters in each example. For relatively smooth images such as (a) and (g), optimal spatial parameter of Turbo denoising is higher (which implies stronger smoothing) than the textured image in (j). This is probably due to the relatively high signal-to-noise ratio of (j). In other words, the quality assessment model tends to respect textures and avoid over-smoothing of details. Effect of the denoising parameter can be visually inspected in Fig. 16. While the denoised result in Fig. 16 (a) is under-smoothed, (c), (e) and (f) show undesirable over-smoothing effects. The predicted quality scores validate this perceptual observation.

**ZH** Turbo 去噪[44]是一种以域变换[45]为核心滤波器的技术，其性能取决于空间与值域平滑参数，因此恰当调节这些参数能有效提升去噪效果。我们发现改变空间平滑参数带来的感知差异最明显，于是用在 TID2013 上训练的质量评价模型来调节该去噪器。把无参考质量指标作为先验用于图像去噪，这一思路与 Zhu 等人[46, 47]的工作相近。结果见图 15：向干净图像加入标准差为 30 的加性高斯白噪声，再用不同空间参数的 Turbo 去噪处理。为降低分数离散度，从去噪图像中随机裁取 50 个块，取其平均分绘制图 15 的曲线。可以看到，尽管各图像加入的噪声量相同，取得最高质量分数的去噪参数却各不相同。对于 (a)、(g) 这类较平滑的图像，Turbo 去噪的最优空间参数较高（即平滑更强），高于 (j) 这类纹理丰富的图像，原因可能在于 (j) 的信噪比相对较高。换言之，质量评价模型倾向于保留纹理、避免过度平滑细节。去噪参数的影响可从图 16 直观看出：图 16(a) 的去噪结果平滑不足，而 (c)、(e)、(f) 则出现了不希望的过度平滑。预测的质量分数印证了这一感知观察。

**EN** TABLE III: LCC (linear correlation coefficient) of NIMA(Inception-v2) model for training and testing on various datasets.

**ZH** 表 III：NIMA(Inception-v2) 模型在不同数据集上训练与测试的 LCC（线性相关系数）。

<!-- [原子块 · table] Test Dataset Train Dataset LIVE [ 26 ] TID2013 [ 2 ] AVA [ 1 ] Average LIVE [ 26 ] 0.698 0.537 0.238 0.491 TID2013 [ 2 ] 0.178 0.827 0.101 0.369 AVA [ 1 ] 0.552 0.514 0.636 0.567 -->

**EN** TABLE IV: SRCC (Spearman’s rank correlation coefficient) of NIMA(Inception-v2) model for training and testing on various datasets.

**ZH** 表 IV：NIMA(Inception-v2) 模型在不同数据集上训练与测试的 SRCC（斯皮尔曼等级相关系数）。

<!-- [原子块 · table] Test Dataset Train Dataset LIVE [ 26 ] TID2013 [ 2 ] AVA [ 1 ] Average LIVE [ 26 ] 0.637 0.327 0.200 0.388 TID2013 [ 2 ] 0.155 0.750 0.087 0.331 AVA [ 1 ] 0.543 0.432 0.612 0.529 -->

<!-- [原子块 · img]  -->

**EN** (a) Input (5.52)

**ZH** (a) 输入（5.52）

<!-- [原子块 · img]  -->

**EN** (b) contrast compression (4.79)

**ZH** (b) 对比度压缩（4.79）

<!-- [原子块 · img]  -->

**EN** (c) boosting details (5.73)

**ZH** (c) 细节增强（5.73）

<!-- [原子块 · img]  -->

**EN** (d) increasing brightness (5.52)

**ZH** (d) 提高亮度（5.52）

<!-- [原子块 · img]  -->

**EN** (e) increasing shadows (5.95)

**ZH** (e) 增强阴影（5.95）

**EN** Fig. 13: Predicted aesthetic score (NIMA(VGG16)) for various parameter settings of multi-layer Laplacian technique [43]. Predicted aesthetic scores are shown below each image.

**ZH** 图 13：多层拉普拉斯技术[43]在不同参数设置下的美学分数预测（NIMA(VGG16)）。每幅图像下方为预测的美学分数。

<!-- [原子块 · img]  -->

**EN** (a) Input (5.80)

**ZH** (a) 输入（5.80）

<!-- [原子块 · img]  -->

**EN** (b) Enhanced (6.12)

**ZH** (b) 增强后（6.12）

<!-- [原子块 · img]  -->

**EN** (c) Input (5.52)

**ZH** (c) 输入（5.52）

<!-- [原子块 · img]  -->

**EN** (d) Enhanced (6.13)

**ZH** (d) 增强后（6.13）

<!-- [原子块 · img]  -->

**EN** (e) Input (4.87)

**ZH** (e) 输入（4.87）

<!-- [原子块 · img]  -->

**EN** (f) Enhanced (5.57)

**ZH** (f) 增强后（5.57）

<!-- [原子块 · img]  -->

**EN** (g) Input (5.59)

**ZH** (g) 输入（5.59）

<!-- [原子块 · img]  -->

**EN** (h) Enhanced (5.98)

**ZH** (h) 增强后（5.98）

**EN** Fig. 14: Tone enhancement by multi-layer Laplacian technique [43] along with our proposed aesthetic assessment model NIMA(VGG16). Predicted aesthetic scores are shown below each image. (Input photos are downloaded from www.farbspiel-photo.com)

**ZH** 图 14：多层拉普拉斯技术[43]结合本文美学评价模型 NIMA(VGG16) 的色调增强效果。每幅图像下方为预测的美学分数。（输入照片下载自 www.farbspiel-photo.com）

<!-- [原子块 · img]  -->

**EN** (a) Noisy Input

**ZH** (a) 含噪输入

<!-- [原子块 · img]  -->

**EN** (b) Optimized (denoising parameter=3.75)

**ZH** (b) 优化结果（去噪参数=3.75）

<!-- [原子块 · img]  -->

**EN** (c) Quality score vs. denoising parameter

**ZH** (c) 质量分数随去噪参数的变化

<!-- [原子块 · img]  -->

**EN** (d) Noisy Input

**ZH** (d) 含噪输入

<!-- [原子块 · img]  -->

**EN** (e) Optimized (denoising parameter=2.25)

**ZH** (e) 优化结果（去噪参数=2.25）

<!-- [原子块 · img]  -->

**EN** (f) Quality score vs. denoising parameter

**ZH** (f) 质量分数随去噪参数的变化

<!-- [原子块 · img]  -->

**EN** (g) Noisy Input

**ZH** (g) 含噪输入

<!-- [原子块 · img]  -->

**EN** (h) Optimized (denoising parameter=4.50)

**ZH** (h) 优化结果（去噪参数=4.50）

<!-- [原子块 · img]  -->

**EN** (i) Quality score vs. denoising parameter

**ZH** (i) 质量分数随去噪参数的变化

<!-- [原子块 · img]  -->

**EN** (j) Noisy Input

**ZH** (j) 含噪输入

<!-- [原子块 · img]  -->

**EN** (k) Optimized (denoising parameter=1.25)

**ZH** (k) 优化结果（去噪参数=1.25）

<!-- [原子块 · img]  -->

**EN** (l) Quality score vs. denoising parameter

**ZH** (l) 质量分数随去噪参数的变化

**EN** Fig. 15: Tuning spatial parameter of Turbo denoising [44] by using our proposed quality assessment model NIMA(VGG16). Standard deviation of the additive white Gaussian noise is set as 30. Denoised results are shown for maximum quality score.

**ZH** 图 15：用本文质量评价模型 NIMA(VGG16) 调节 Turbo 去噪[44]的空间参数。加性高斯白噪声的标准差设为 30。图中去噪结果对应最高质量分数。

<!-- [原子块 · img]  -->

**EN** (a) denoising parameter=1.25, score=5.06

**ZH** (a) 去噪参数=1.25，分数=5.06

<!-- [原子块 · img]  -->

**EN** (b) denoising parameter=3.0, score=5.15

**ZH** (b) 去噪参数=3.0，分数=5.15

<!-- [原子块 · img]  -->

**EN** (c) denoising parameter=9.75, score=4.76

**ZH** (c) 去噪参数=9.75，分数=4.76

<!-- [原子块 · img]  -->

**EN** (d) denoising parameter=1.25, score=4.97

**ZH** (d) 去噪参数=1.25，分数=4.97

<!-- [原子块 · img]  -->

**EN** (e) denoising parameter=3.0, score=4.62

**ZH** (e) 去噪参数=3.0，分数=4.62

<!-- [原子块 · img]  -->

**EN** (f) denoising parameter=9.75, score=3.64

**ZH** (f) 去噪参数=9.75，分数=3.64

**EN** Fig. 16: Effect of Turbo denoising [44] on our predicted quality scores. Input noisy images are shown in Fig. 15.

**ZH** 图 16：Turbo 去噪[44]对本文预测质量分数的影响。含噪输入图像见图 15。

**EN** III-E Computational Costs

**ZH** III-E 计算开销

**EN** Computational complexity of NIMA models are compared in Table V. Our inference TensorFlow implementation is tested on an Intel Xeon CPU @ 3.5 GHz with 32 GB memory and 12 cores, and NVIDIA Quadro K620 GPU. Timings of one pass of NIMA models on an image of size ⟦SLOT_117⟧ are reported in Table V. Evidently, NIMA(MobileNet) is significantly lighter and faster than other models. This comes at the expense of a slight performance drop (shown in Table I and Table II).

**ZH** 表 V 比较了 NIMA 各模型的计算复杂度。推理用的 TensorFlow 实现在配备 32 GB 内存、12 核的 Intel Xeon CPU @ 3.5 GHz 与 NVIDIA Quadro K620 GPU 上测试。表 V 报告了 NIMA 模型对 ⟦SLOT_117⟧ 大小图像单次前向的耗时。显然，NIMA(MobileNet) 比其他模型轻量且快得多，代价是性能略有下降（见表 I 与表 II）。

**EN** IV Conclusion

**ZH** IV 结论

**EN** In this work we introduced a CNN-based image assessment method, which can be trained on both aesthetic and pixel-level quality datasets. Our models effectively predict the distribution of quality ratings, rather than just the mean scores. This leads to a more accurate quality prediction with higher correlation to the ground truth ratings. We trained two models for high level aesthetics and low level technical qualities, and utilized them to steer parameters of a few image enhancement operators. Our experiments suggest that these models are capable of guiding denoising and tone enhancement to produce perceptually superior results.

**ZH** 本文提出一种基于 CNN 的图像评价方法，可同时在美学数据与像素级质量数据上训练。模型能有效预测质量评分的分布，而不只是均分，从而得到与真实评分相关性更高的质量预测。我们训练了分别面向高层美感与低层技术质量的两个模型，并用它们引导若干图像增强算子的参数。实验表明，这些模型能够引导去噪与色调增强，产生感知上更优的结果。

**EN** As part of our future work, we will exploit the trained models on other image enhancement applications. Our current experimental setup requires the enhancement operator to be evaluated multiple times. This limits real-time application of the proposed method. One might argue that in case of an enhancement operator with well-defined derivatives, using NIMA as the loss function is a more efficient approach.

**ZH** 后续工作将把训练好的模型用于其他图像增强应用。当前的实验设置要求增强算子被多次评估，限制了方法的实时应用。若增强算子具有良定义的导数，把 NIMA 直接作为损失函数或许是更高效的做法。

**EN** Acknowledgment

**ZH** 致谢

**EN** We would like to thank Dr. Pascal Getreuer for valuable discussions and helpful advice on approximation of score distributions.

**ZH** 感谢 Pascal Getreuer 博士就评分分布逼近问题给出的宝贵讨论与有益建议。

**EN** TABLE V: Comparison of the proposed quality assessment technique with various CNN architectures. Average timings are reported in ms for Xeon Intel CPU @ 3.5 GHz, and NVIDIA Quadro K620 GPU. Timings are reported for applying NIMA models on images of size ⟦SLOT_118⟧.

**ZH** 表 V：所提质量评价方法在不同 CNN 结构下的比较。平均耗时以毫秒为单位，测试平台为 Intel Xeon CPU @ 3.5 GHz 与 NVIDIA Quadro K620 GPU。耗时对应 NIMA 模型处理 ⟦SLOT_118⟧ 大小图像。

<!-- [原子块 · table] Million Billion CPU GPU Model Parameters Flops Timing (ms) Timing (ms) NIMA(MobileNet) 3.22 1.29 30.45 20.23 NIMA(Inception-v2) 10.16 4.37 70.49 39.11 NIMA(VGG16) 134.30 31.62 150.34 85.76 -->

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] [1] N. Murray, L. Marchesotti, and F. Perronnin, “AVA: A large-scale database for aesthetic visual analysis,” in Computer Vision and Pattern Recognition (CVPR), 2012 IEEE Conference on . IEEE, 2012, p -->

<!-- [原子块 · verbatim] [2] N. Ponomarenko, O. Ieremeiev, V. Lukin, K. Egiazarian, L. Jin, J. Astola, B. Vozel, K. Chehdi, M. Carli, F. Battisti et al. , “Color image database TID2013: Peculiarities and preliminary results,” -->

<!-- [原子块 · verbatim] [3] Z. Wang, A. C. Bovik, H. R. Sheikh, and E. P. Simoncelli, “Image quality assessment: from error visibility to structural similarity,” IEEE Transactions on Image Processing , vol. 13, no. 4, pp. 60 -->

<!-- [原子块 · verbatim] [4] W. Xue, L. Zhang, and X. Mou, “Learning without human scores for blind image quality assessment,” in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition , 2013, pp. 995–1 -->

<!-- [原子块 · verbatim] [5] L. Kang, P. Ye, Y. Li, and D. Doermann, “Convolutional neural networks for no-reference image quality assessment,” in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition  -->

<!-- [原子块 · verbatim] [6] S. Bosse, D. Maniry, T. Wiegand, and W. Samek, “A deep neural network for image quality assessment,” in Image Processing (ICIP), 2016 IEEE International Conference on . IEEE, 2016, pp. 3773–3777. -->

<!-- [原子块 · verbatim] [7] S. Bianco, L. Celona, P. Napoletano, and R. Schettini, “On the use of deep learning for blind image quality assessment,” arXiv preprint arXiv:1602.05531 , 2016. -->

<!-- [原子块 · verbatim] [8] X. Lu, Z. Lin, X. Shen, R. Mech, and J. Z. Wang, “Deep multi-patch aggregation network for image style, aesthetics, and quality estimation,” in Proceedings of the IEEE International Conference on  -->

<!-- [原子块 · verbatim] [9] Y. Kao, C. Wang, and K. Huang, “Visual aesthetic quality assessment with a regression model,” in Image Processing (ICIP), 2015 IEEE International Conference on . IEEE, 2015, pp. 1583–1587. -->

<!-- [原子块 · verbatim] [10] L. Mai, H. Jin, and F. Liu, “Composition-preserving deep photo aesthetics assessment,” in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition , 2016, pp. 497–506. -->

<!-- [原子块 · verbatim] [11] B. Jin, M. V. O. Segovia, and S. Süsstrunk, “Image aesthetic predictors based on weighted CNNs,” in Image Processing (ICIP), 2016 IEEE International Conference on . IEEE, 2016, pp. 2291–2295. -->

<!-- [原子块 · verbatim] [12] H. R. Sheikh, Z. Wang, L. Cormack, and A. C. Bovik, “Live image quality assessment database release 2,” 2005. -->

<!-- [原子块 · verbatim] [13] E. C. Larson and D. M. Chandler, “Most apparent distortion: full-reference image quality assessment and the role of strategy,” Journal of Electronic Imaging , vol. 19, no. 1, pp. 011 006–011 006, -->

<!-- [原子块 · verbatim] [14] S. Kong, X. Shen, Z. Lin, R. Mech, and C. Fowlkes, “Photo aesthetics ranking network with attributes and content adaptation,” in European Conference on Computer Vision . Springer, 2016, pp. 662–6 -->

<!-- [原子块 · verbatim] [15] A. Krizhevsky, I. Sutskever, and G. E. Hinton, “ImageNet classification with deep convolutional neural networks,” in Advances in neural information processing systems , 2012, pp. 1097–1105. -->

<!-- [原子块 · verbatim] [16] J. Kim, H. Zeng, D. Ghadiyaram, S. Lee, L. Zhang, and A. C. Bovik, “Deep convolutional neural models for picture-quality prediction: Challenges and solutions to data-driven image quality assessme -->

<!-- [原子块 · verbatim] [17] X. Lu, Z. Lin, H. Jin, J. Yang, and J. Z. Wang, “Rating image aesthetics using deep learning,” IEEE Transactions on Multimedia , vol. 17, no. 11, pp. 2021–2034, 2015. -->

<!-- [原子块 · verbatim] [18] K. Simonyan and A. Zisserman, “Very deep convolutional networks for large-scale image recognition,” arXiv preprint arXiv:1409.1556 , 2014. -->

<!-- [原子块 · verbatim] [19] H. Zeng, L. Zhang, and A. C. Bovik, “A probabilistic quality representation approach to deep blind image quality prediction,” arXiv preprint arXiv:1708.08190 , 2017. -->

<!-- [原子块 · verbatim] [20] S. Ma, J. Liu, and C. W. Chen, “A-lamp: Adaptive layout-aware multi-patch deep convolutional neural network for photo aesthetic assessment,” in Computer Vision and Pattern Recognition (CVPR), 201 -->

<!-- [原子块 · verbatim] [21] L. Hou, C.-P. Yu, and D. Samaras, “Squared earth mover’s distance-based loss for training deep neural networks,” arXiv preprint arXiv:1611.05916 , 2016. -->

<!-- [原子块 · verbatim] [22] R. Zhang, P. Isola, A. A. Efros, E. Shechtman, and O. Wang, “The unreasonable effectiveness of deep features as a perceptual metric,” IEEE conference on Computer Vision and Pattern Recognition (C -->

<!-- [原子块 · verbatim] [23] H. Talebi and P. Milanfar, “Learned perceptual image enhancement,” IEEE International Conference on Computational Photography (ICCP) , May 2018. -->

<!-- [原子块 · verbatim] [24] K. Gu, G. Zhai, W. Lin, and M. Liu, “The analysis of image contrast: From quality assessment to automatic enhancement,” IEEE transactions on cybernetics , vol. 46, no. 1, pp. 284–297, 2016. -->

<!-- [原子块 · verbatim] [25] Kodak, “Kodak lossless true color image suite,” http://r0k.us/graphics/kodak/ . -->

<!-- [原子块 · verbatim] [26] D. Ghadiyaram and A. C. Bovik, “Massive online crowdsourced study of subjective and objective picture quality,” IEEE Transactions on Image Processing , vol. 25, no. 1, pp. 372–387, 2016. -->

<!-- [原子块 · verbatim] [27] T. M. Cover and J. A. Thomas, Elements of information theory . John Wiley & Sons, 2012. -->

<!-- [原子块 · verbatim] [28] C. Szegedy, V. Vanhoucke, S. Ioffe, J. Shlens, and Z. Wojna, “Rethinking the inception architecture for computer vision,” in Proceedings of the IEEE Conference on Computer Vision and Pattern Reco -->

<!-- [原子块 · verbatim] [29] A. G. Howard, M. Zhu, B. Chen, D. Kalenichenko, W. Wang, T. Weyand, M. Andreetto, and H. Adam, “MobileNets: Efficient convolutional neural networks for mobile vision applications,” arXiv preprint -->

<!-- [原子块 · verbatim] [30] S. Ioffe and C. Szegedy, “Batch normalization: Accelerating deep network training by reducing internal covariate shift,” in International Conference on Machine Learning , 2015, pp. 448–456. -->

<!-- [原子块 · verbatim] [31] P. Golik, P. Doetsch, and H. Ney, “Cross-entropy vs. squared error training: a theoretical and experimental comparison,” in Interspeech , 2013, pp. 1756–1760. -->

<!-- [原子块 · verbatim] [32] E. Levina and P. Bickel, “The earth mover’s distance is the Mallows’ distance: Some insights from statistics,” in Computer Vision, 2001. ICCV 2001. Proceedings. Eighth IEEE International Conferen -->

<!-- [原子块 · verbatim] [33] M. Abadi, A. Agarwal, P. Barham, E. Brevdo, Z. Chen, C. Citro, G. S. Corrado, A. Davis, J. Dean, M. Devin et al. , “TensorFlow: Large-scale machine learning on heterogeneous distributed systems,” -->

<!-- [原子块 · verbatim] [34] M. Abadi, P. Barham, J. Chen, Z. Chen, A. Davis, J. Dean, M. Devin, S. Ghemawat, G. Irving, M. Isard et al. , “TensorFlow: A system for large-scale machine learning,” in Proceedings of the 12th U -->

<!-- [原子块 · verbatim] [35] J. Xu, P. Ye, Q. Li, H. Du, Y. Liu, and D. Doermann, “Blind image quality assessment based on high order statistics aggregation,” IEEE Transactions on Image Processing , vol. 25, no. 9, pp. 4444– -->

<!-- [原子块 · verbatim] [36] X. Lu, Z. Lin, H. Jin, J. Yang, and J. Z. Wang, “Rapid: Rating pictorial aesthetics using deep learning,” in Proceedings of the 22nd ACM international conference on Multimedia . ACM, 2014, pp. 45 -->

<!-- [原子块 · verbatim] [37] Y. Kao, R. He, and K. Huang, “Visual aesthetic quality assessment with multi-task deep learning,” arXiv preprint arXiv:1604.04970 , 2016. -->

<!-- [原子块 · verbatim] [38] Z. Wang, S. Chang, F. Dolcos, D. Beck, D. Liu, and T. S. Huang, “Brain-inspired deep networks for image aesthetics assessment,” arXiv preprint arXiv:1601.04155 , 2016. -->

<!-- [原子块 · verbatim] [39] A. K. Moorthy and A. C. Bovik, “Blind image quality assessment: From natural scene statistics to perceptual quality,” IEEE transactions on Image Processing , vol. 20, no. 12, pp. 3350–3364, 2011. -->

<!-- [原子块 · verbatim] [40] A. Mittal, A. K. Moorthy, and A. C. Bovik, “No-reference image quality assessment in the spatial domain,” IEEE Transactions on Image Processing , vol. 21, no. 12, pp. 4695–4708, 2012. -->

<!-- [原子块 · verbatim] [41] M. A. Saad, A. C. Bovik, and C. Charrier, “Blind image quality assessment: A natural scene statistics approach in the DCT domain,” IEEE Transactions on Image Processing , vol. 21, no. 8, pp. 3339 -->

<!-- [原子块 · verbatim] [42] N. K. Kottayil, I. Cheng, F. Dufaux, and A. Basu, “A color intensity invariant low-level feature optimization framework for image quality assessment,” Signal, Image and Video Processing , vol. 10 -->

<!-- [原子块 · verbatim] [43] H. Talebi and P. Milanfar, “Fast multilayer Laplacian enhancement,” IEEE Transactions on Computational Imaging , vol. 2, no. 4, pp. 496–509, 2016. -->

<!-- [原子块 · verbatim] [44] T.-S. Wong and P. Milanfar, “Turbo denoising for mobile photographic applications,” in Image Processing (ICIP), 2016 IEEE International Conference on . IEEE, 2016, pp. 988–992. -->

<!-- [原子块 · verbatim] [45] E. S. Gastal and M. M. Oliveira, “Domain transform for edge-aware image and video processing,” in ACM Transactions on Graphics (ToG) , vol. 30, no. 4. ACM, 2011, p. 69. -->

<!-- [原子块 · verbatim] [46] X. Zhu and P. Milanfar, “A no-reference sharpness metric sensitive to blur and noise,” in Quality of Multimedia Experience, 2009. QoMEx 2009. International Workshop on . IEEE, 2009, pp. 64–69. -->

<!-- [原子块 · verbatim] [47] ——, “Automatic parameter selection for denoising algorithms using a no-reference measure of image content,” IEEE Transactions on Image Processing , vol. 19, no. 12, pp. 3116–3132, 2010. -->
