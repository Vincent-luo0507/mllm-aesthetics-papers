# 融合属性与内容自适应的照片美学排序网络

> 原标题：Photo Aesthetics Ranking Network with Attributes and Content Adaptation
> 作者：Shu Kong, Xiaohui Shen, Zhe Lin, Radomir Mech, Charless Fowlkes · arXiv:1606.01621 · 2016-06-06

<!-- [原子块 · verbatim] Photo Aesthetics Ranking Network with Attributes and Content Adaptation -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] Real-world applications could benefit from the ability to automatically generate a fine-grained ranking of photo aesthetics. However, previous methods for image aesthetics analysis have primarily focu -->

<!-- [原子块 · verbatim] To train and analyze this model, we have assembled a new aesthetics and attributes database (AADB) which contains aesthetic scores and meaningful attributes assigned to each image by multiple human ra -->

**EN** Keywords:

**ZH** 关键词：

**EN** 1 Introduction

**ZH** 1 引言

<!-- [原子块 · img]  -->

**EN** Figure 1: Classification-based methods for aesthetic analysis can distinguish high- and low-quality images shown in the leftmost and rightmost columns, but fail to provide useful insights about borderline images displayed in the middle column. This observation motivates us to consider rating and ranking images w.r.t aesthetics rather than simply assigning binary labels. We observe that the contribution of particular photographic attributes to making an image aesthetically pleasing depends on the thematic content (shown in different rows), so we develop a model for rating that incorporates joint attributes and content. The attributes and ratings of aesthetics on a scale 1 to 5 are predicted by our model (displayed on top and right of each image, respectively).

**ZH** 图 1：基于分类的美学分析方法能够区分最左列与最右列所示的高质量与低质量图像，却难以对中间列展示的边界图像给出有效判断。这一观察促使我们考虑对图像的美学进行评分与排序，而非简单地赋予二值标签。我们观察到，特定摄影属性对图像是否具有美感的贡献取决于其主题内容（图中按行展示），因此构建了一个联合属性与内容的评分模型。图中每幅图像的上方与右侧分别给出了模型预测的属性与 1 至 5 分制的美学评分。

**EN** Automatically assessing image aesthetics is increasingly important for a variety of applications [20, 17], including personal photo album management, automatic photo editing, and image retrieval. While judging image aesthetics is a subjective task, it has been an area of active study in recent years and substantial progress has been made in identifying and quantifying those image features that are predictive of favorable aesthetic judgements by most individuals [20, 17, 16, 18, 5].

**ZH** 自动评估图像美学在诸多应用中正变得日益重要 [20, 17]，涉及个人相册管理、自动照片编辑与图像检索等。尽管图像美学判断带有主观性，近年来该方向研究活跃，且在识别与量化那些能够预测多数人正向美学判断的图像特征方面已取得实质性进展 [20, 17, 16, 18, 5]。

**EN** Early works formulate aesthetic analysis as a classification or a regression problem of mapping images to aesthetic ratings provided by human raters [5, 11, 18, 6, 26]. Some approaches have focused on designing hand-crafted features that encapsulate standard photographic practice and rules of visual design, utilizing both low-level statistics (e.g. color histogram and wavelet analysis) and high-level cues based on traditional photographic rules (e.g. region composition and rule of thirds). Others have adopted generic image content features, which are originally designed for recognition (e.g. SIFT [14] and Fisher Vector [28, 27]), that have been found to outperform methods using rule-based features [21]. With the advance of deep Convolutional Neural Network (CNN) [12], recent works propose to train end-to-end models for image aesthetics classification [10, 16, 17], yielding state-of-the-art performance on a recently released Aesthetics Visual Analysis dataset (AVA) [23].

**ZH** 早期工作将美学分析建模为分类或回归问题，即把图像映射到人类评分者给出的美学评分 [5, 11, 18, 6, 26]。部分方法致力于设计手工特征以刻画标准摄影实践与视觉设计法则，既利用底层统计量（如颜色直方图与小波分析），也利用基于传统摄影法则的高层线索（如区域构成与三分法）。另一些方法则采用最初为识别任务设计的通用图像内容特征（如 SIFT [14] 与 Fisher Vector [28, 27]），其效果已被证明优于基于规则特征的方法 [21]。随着深度卷积神经网络（CNN）[12] 的发展，近期工作提出端到端训练的图像美学分类模型 [10, 16, 17]，在新发布的 Aesthetics Visual Analysis（AVA）数据集 [23] 上取得了当时最佳性能。

**EN** Despite notable recent progress towards computational image aesthetics classification (e.g. [16, 20, 17]), judging image aesthetics is still a subjective task, and it is difficult to learn a universal scoring mechanism for various kinds of images. For example, as demonstrated in Fig. 1, images with obviously visible high- or low- aesthetics are relatively easy to classify, but existing methods cannot generate reliable labels for borderline images. Therefore, instead of formulating image aesthetics analysis as an overall binary classification or regression problem, we argue that it is far more practical and useful to predict relative aesthetic rankings among images with similar visual content along with generating richer descriptions in terms of aesthetic attributes [7, 29].

**ZH** 尽管计算图像美学分类近期取得了显著进展（如 [16, 20, 17]），图像美学判断本质上仍是主观任务，很难学到适用于各类图像的通用打分机制。例如，如图 1 所示，美学质量明显偏高或偏低的图像相对容易分类，但现有方法无法为边界图像生成可靠标签。因此，我们主张：与其把图像美学分析表述为整体的二分类或回归问题，不如预测视觉内容相近的图像之间的相对美学排序，并同时给出更丰富的美学属性描述 [7, 29]，这更为实用，也更有价值。

**EN** To this end, we propose to train a model through a Siamese network [3] that takes a pair of images as input and directly predicts relative ranking of their aesthetics in addition to their overall aesthetic scores. Such a structure allows us to deploy different sampling strategies of image pairs and leverage auxiliary side-information to regularize the training, including aesthetic attributes [6, 16, 20] and photo content [18, 23, 15]. For example, Fig. 1 demonstrates that photos with different contents convey different attributes to make them aesthetically pleasing. While such side information has been individually adopted to improve aesthetics classification [16, 20], it remains one open problem to systematically incorporate all the needed components in a single end-to-end framework with fine-grained aesthetics ranking. Our model and training procedure naturally incorporates both attributes and content information by sampling image pairs with similar content to learn the specific relations of attributes and aesthetics for different content sub-categories. As we show, this results in more comparable and consistent aesthetics estimation results.

**ZH** 为此，我们提出通过孪生网络（Siamese network）[3] 训练模型：该网络以图像对为输入，除预测各自的整体美学分数外，还直接预测两者美学的相对排序。这种结构使我们能够采用不同的图像对采样策略，并利用辅助的旁支信息来正则化训练过程，包括美学属性 [6, 16, 20] 与照片内容 [18, 23, 15]。例如，图 1 表明不同内容的照片依赖不同的属性来获得美感。尽管此类旁支信息已被分别用于改进美学分类 [16, 20]，但如何在一个端到端框架中系统地整合全部所需组件并实现细粒度美学排序，仍是一个开放问题。我们的模型与训练流程通过对内容相近的图像对采样，自然地同时纳入属性与内容信息，从而学习不同内容子类别下属性与美学之间的特定关系。实验表明，这一做法带来了更具可比性与一致性的美学估计结果。

**EN** Moreover, as individuals have different aesthetics tastes, we argue that it is important to compare ratings assigned by an individual across multiple images in order to provide a more consistent training signal. To this end, we have collected and will publicly release a new dataset in which each image is associated with a detailed score distribution, meaningful attributes annotation and (anonymized) raters’ identities. We refer to this dataset as the “Aesthetics with Attributes Database”, or AADB for short. AADB not only contains a much more balanced distribution of professional and consumer photos and a more diverse range of photo qualities than available in the exiting AVA dataset, but also identifies ratings made by the same users across multiple images. This enables us to develop novel sampling strategies for training our model which focuses on relative rankings by individual raters. Interestingly, this rater-related information also enables us to compare the trained model to each individual’s rating results by computing the ranking correlation over test images rated by that individual. Our experiments show the effectiveness of the proposed model in rating image aesthetics compared to human individuals. We also show that, by simply thresholding rated aesthetics scores, our model achieves state-of-the-art classification performance on the AVA dataset, even though we do not explicitly train or tune the model for the aesthetic classification task.

**ZH** 此外，由于个体的审美偏好存在差异，我们认为有必要对同一评分者在多幅图像上的打分进行比较，以提供更一致的训练信号。为此，我们收集并将公开一个新数据集，其中每幅图像都配有详细的分数分布、有意义的属性标注以及（匿名化的）评分者身份。我们将该数据集命名为“美学与属性数据库”（Aesthetics with Attributes Database），简称 AADB。与已有的 AVA 数据集相比，AADB 不仅在专业照片与消费级照片的分布上更为均衡、照片质量的跨度更大，还记录了同一用户在多幅图像上的评分。这使我们能够设计新的采样策略来训练关注个体评分者相对排序的模型。有意思的是，这些与评分者相关的信息还让我们可以计算模型与某位个体在测试图像上排序的相关性，从而将训练好的模型与每位个体的评分结果逐一比较。实验表明，与人类个体相比，所提模型在图像美学评分上是有效的。我们还证明，只需对估计出的美学分数做简单阈值化，模型便能在 AVA 数据集上取得最佳分类性能——尽管我们并未针对美学分类任务显式训练或调参。

**EN** In summary, our main contributions are three-fold:

**ZH** 综上，本文的主要贡献包括三方面：

**EN** 1. We release a new dataset containing not only score distributions, but also informative attributes and anonymized rater identities. These annotations enable us to study the use of individuals’ aesthetics ratings for training our model and analyze how the trained model performs compared to individual human raters.

**ZH** 1. 我们发布了一个新数据集，其中不仅包含分数分布，还包含富有信息量的属性与匿名化的评分者身份。这些标注使我们得以研究如何利用个体的美学评分为模型提供训练信号，并分析训练所得模型相对于人类个体评分者的表现。

**EN** 2. We propose a new CNN architecture that unifies aesthetics attributes and photo content for image aesthetics rating and achieves state-of-the-art performance on existing aesthetics classification benchmark.

**ZH** 2. 我们提出一种新的 CNN 结构，将美学属性与照片内容统一用于图像美学评分，并在现有的美学分类基准上取得最佳性能。

**EN** 3. We propose a novel sampling strategy that utilizes mixed within- and cross-rater image pairs for training models. We show this strategy, in combination with pair-wise ranking loss, substantially improves the performance w.r.t. the ranking correlation metric.

**ZH** 3. 我们提出一种新的采样策略，在训练时混合使用评分者内与评分者间的图像对。实验表明，该策略与成对排序损失相结合，显著提升了排序相关性指标下的性能。

**EN** 2 Related Work

**ZH** 2 相关工作

**EN** CNN for aesthetics classification: In [16, 10, 17], CNN-based methods are proposed for classifying images into high- or low- aesthetic categories. The authors also show that using patches from the original high-resolution images largely improves the performance. In contrast, our approach formulates aesthetic prediction as a combined regression and ranking problem. Rather than using patches, our architecture warps the whole input image in order to minimize the overall network size and computational workload while retaining compositional elements in the image, e.g. rule of thirds, which are lost in patch-based approaches.

**ZH** 面向美学分类的 CNN：文献 [16, 10, 17] 提出基于 CNN 的方法，将图像划分为高美学或低美学类别。作者还指出，使用原始高分辨率图像中的图像块可大幅提升性能。相比之下，我们把美学预测表述为回归与排序相结合的问题；同时不使用图像块，而是对整幅输入图像做形变缩放，以此在控制网络总体规模与计算量的同时保留图像中的构图要素（例如三分法），而这些要素在基于图像块的方法中会丢失。

**EN** Attribute-adaptive models: Some recent works have explored the use of high-level describable attributes [6, 20, 16] for image aesthetics classification. In early work, these attributes were modeled using hand-crafted features [6]. This introduces some intrinsic problems, since (1) engineering features that capture high-level semantic attributes is a difficult task, and (2) the choice of describable attributes may ignore some aspects of the image which are relevant to the overall image aesthetics. For these reasons, Marchesotti et al. propose to automatically select a large number of useful attributes based on textual comments from raters [22] and model these attributes using generic features [21]. Despite good performance, many of the discovered textual attributes (e.g. ⟦SLOT_0⟧, ⟦SLOT_1⟧, ⟦SLOT_2⟧, ⟦SLOT_3⟧, ⟦SLOT_4⟧) do not correspond to well defined visual characteristics which hinders their detectability and utility in applications. Perhaps the closest work to our approach is that of Lu et al. , who propose to learn several meaningful style attributes [16] in a CNN framework and use the hidden features to regularize aesthetics classification network training.

**ZH** 属性自适应模型：近期一些工作探索了将高层可描述属性 [6, 20, 16] 用于图像美学分类。早期工作中，这些属性用手工特征建模 [6]，这带来了一些固有困难：（1）构造能够刻画高层语义属性的特征本身就很困难；（2）可描述属性的选取可能忽略图像中与整体美学相关的某些方面。为此，Marchesotti 等人提出依据评分者的文字评论自动筛选出大量有用属性 [22]，并用通用特征对这些属性建模 [21]。尽管效果不错，但挖掘出的许多文本属性（如 ⟦SLOT_0⟧、⟦SLOT_1⟧、⟦SLOT_2⟧、⟦SLOT_3⟧、⟦SLOT_4⟧）并不对应定义良好的视觉特征，这削弱了它们的可检测性与实用价值。与我们思路最接近的或许是 Lu 等人的工作，他们在 CNN 框架中学习若干有意义的风格属性 [16]，并用隐层特征正则化美学分类网络的训练。

**EN** Content-adaptive models: To make use of image content information such as scene categories or choice of photographic subject, Luo et al. propose to segment regions and extract visual features based on the categorization of photo content [18]. Other work, such as [23, 15], has also demonstrated that image content is useful for aesthetics analysis. However, it has been assumed that the category labels are provided both during training and testing. To our knowledge, there is only one paper [24] that attempts to jointly predict content semantics and aesthetics labels. In [24], Murray et al. propose to rank images w.r.t aesthetics in a three-way classification problem (high-, medium- and low-aesthetics quality). However, their work has some limitations because (1) deciding the thresholds between nearby classes is non-trivial, and (2) the final classification model outputs a hard label which is less useful than a continuous rating.

**ZH** 内容自适应模型：为利用场景类别或拍摄主体等图像内容信息，Luo 等人提出先分割区域，再依据照片内容的类别提取视觉特征 [18]。文献 [23, 15] 等工作同样证明了图像内容对美学分析的有效性。然而，这些方法假定类别标签在训练与测试阶段均已提供。据我们所知，只有文献 [24] 尝试联合预测内容语义与美学标签：Murray 等人在三分类（高、中、低美学质量）问题中按美学对图像排序。但该工作存在两点局限：（1）相邻类别之间阈值的确定并不容易；（2）最终分类模型输出的是硬标签，其有用性不及连续评分。

**EN** Our work is thus unique in presenting a unified framework that is trained by jointly incorporating the photo content, the meaningful attributes and the aesthetics rating in a single CNN model. We train a category-level classification layer on top of our aesthetics rating network to generate soft weights of category labels, which are used to combine scores predicted by multiple content-adaptive branches. This allows category-specific subnets to complement each other in rating image aesthetics with shared visual content information while efficiently re-using front-end feature computations. While our primary focus is on aesthetic rating prediction, we believe that the content and attribute predictions (as displayed on the right side of images in Fig. 1) represented in hidden layers of our architecture could also be surfaced for use in other applications such as automatic image enhancement and image retrieval.

**ZH** 因此，本文的独特之处在于提出一个统一框架，在单个 CNN 模型中联合纳入照片内容、有意义的属性与美学评分进行训练。我们在美学评分网络之上训练一个类别级分类层，用以生成类别标签的软权重，再用这些权重去组合多个内容自适应分支预测的分数。这使得各类别子网络能够借助共享的视觉内容信息在图像美学评分上互补，同时高效地复用前端特征计算。尽管我们的重点是美学评分预测，但我们相信，该结构隐层中所表示的内容与属性预测（如图 1 中图像右侧所示）也可输出供其他应用使用，例如自动图像增强与图像检索。

**EN** 3 Aesthetics and Attributes Database

**ZH** 3 美学与属性数据库

<!-- [原子块 · table] AADB AVA [ 23 ] PN [ 5 ] CUHKPQ [ 11 , 19 ] Rater’s ID Y N N N All Real Photo Y N Y Y Attribute Label Y Y N N Score Dist. Y Y Y N -->

**EN** Table 1: Comparison of the properties of current image aesthetics datasets. In addition to score distribution and meaningful style attributes, AADB also tracks raters’ identities across images which we exploit in training to improve aesthetic ranking models.

**ZH** 表 1：现有图像美学数据集的性质对比。除分数分布与有意义的风格属性外，AADB 还跨图像追踪评分者的身份，我们在训练中利用这一点来改进美学排序模型。

<!-- [原子块 · img]  -->

**EN** Figure 2: Our AADB dataset consists of a wide variety of photographic imagery of real scenes collected from Flickr. This differs from AVA which contains significant numbers of professional images that have been highly manipulated, overlayed with advertising text, etc.

**ZH** 图 2：我们的 AADB 数据集包含从 Flickr 收集的丰富多样的真实场景摄影图像。这一点与 AVA 不同，后者含有大量经过高度处理、叠加广告文字等的专业图像。

**EN** To collect a large and varied set of photographic images, we download images from the Flickr website11 1 www.flickr.com which carry a Creative Commons license and manually curate the data set to remove non-photographic images (e.g. cartoons, drawings, paintings, ads images, adult-content images, etc.). We have five different workers then independently annotate each image with an overall aesthetic score and a fixed set of eleven meaningful attributes using Amazon Mechanical Turk (AMT)22 2 www.mturk.com. The AMT raters work on batches, each of which contains ten images. For each image, we average the ratings of five raters as the ground-truth aesthetic score. The number of images rated by a particular worker follows long tail distribution, as shown later in Fig. 6 in the experiment.

**ZH** 为收集规模大、种类丰富的摄影图像，我们从 Flickr 网站11 1 www.flickr.com 下载带有 Creative Commons 许可的图像，并人工筛除漫画、素描、油画、广告图、成人内容等非摄影图像。随后，我们请五位不同的工作者通过 Amazon Mechanical Turk（AMT）22 2 www.mturk.com 独立地为每幅图像标注一个总体美学分数和一组固定的十一项有意义的属性。AMT 评分者按批次工作，每批包含十幅图像。对每幅图像，我们将五位评分者的打分取平均作为真实美学分数。某位工作者评分的图像数量呈长尾分布，后文实验中的图 6 将给出说明。

**EN** After consulting professional photographers, we selected eleven attributes that are closely related to image aesthetic judgements: ⟦SLOT_5⟧, ⟦SLOT_6⟧, ⟦SLOT_7⟧, ⟦SLOT_8⟧, ⟦SLOT_9⟧, ⟦SLOT_10⟧, ⟦SLOT_11⟧, ⟦SLOT_12⟧, ⟦SLOT_13⟧, ⟦SLOT_14⟧, and ⟦SLOT_15⟧. These attributes span traditional photographic principals of color, lighting, focus and composition, and provide a natural vocabulary for use in applications, such as auto photo editing and image retrieval. The final AADB dataset contains 10,000 images in total, each of which have aesthetic quality ratings and attribute assignments provided by five different individual raters. Aggregating multiple raters allows us to assign a confidence score to each attribute, unlike, e.g., AVA where attributes are binary. Similar to previous rating datasets [23], we find that average ratings are well fit by a Gaussian distribution. For evaluation purposes, we randomly split the dataset into validation (500), testing (1,000) and training sets (the rest). The supplemental material provides additional details about dataset collection and statistics of the resulting data.

**ZH** 在咨询专业摄影师后，我们选取了与图像美学判断密切相关的十一项属性：⟦SLOT_5⟧、⟦SLOT_6⟧、⟦SLOT_7⟧、⟦SLOT_8⟧、⟦SLOT_9⟧、⟦SLOT_10⟧、⟦SLOT_11⟧、⟦SLOT_12⟧、⟦SLOT_13⟧、⟦SLOT_14⟧ 和 ⟦SLOT_15⟧。这些属性覆盖了色彩、光照、对焦与构图等传统摄影要领，并为自动照片编辑、图像检索等应用提供了自然的描述词汇。最终的 AADB 数据集共包含 10,000 幅图像，每幅图像均由五位不同的评分者给出美学质量评分与属性标注。聚合多位评分者的结果使我们能够为每项属性赋予一个置信度分数，这一点有别于 AVA 等数据集中属性的二值标注。与已有评分数据集 [23] 类似，我们发现平均评分可以很好地用高斯分布拟合。为便于评估，我们将数据集随机划分为验证集（500 幅）、测试集（1,000 幅）与训练集（其余部分）。补充材料给出了数据集采集的更多细节以及所得数据的统计信息。

**EN** Table 1 provides a summary comparison of AADB to other related public databases for image aesthetics analysis. Except for our AADB and the existing AVA dataset, many existing datasets have two intrinsic problems (as discussed in [23]), (1) they do not provide full score distributions or style attribute annotation, and (2) images in these datasets are either biased or consist of examples which are particularly easy for binary aesthetics classification. Datasets such as CUHKPQ [11, 19] only provide binary labels (low or high aesthetics) which cannot easily be used for rating prediction. A key difference between our dataset and AVA is that many images in AVA are heavily edited or synthetic (see Fig. 2) while AADB contains a much more balanced distribution of professional and consumer photos. More importantly, AVA does not provide any way to identify ratings provided by the same individual for multiple images. We report results of experiments, showing that rater identity on training data provides useful side information for training improved aesthetic predictors.

**ZH** 表 1 概括对比了 AADB 与其他相关公开图像美学分析数据库。除我们的 AADB 与已有的 AVA 数据集外，许多现有数据集存在两个固有缺陷（如 [23] 所讨论）：（1）不提供完整的分数分布或风格属性标注；（2）数据集中的图像要么存在偏差，要么由特别易于二值美学分类的样本构成。CUHKPQ [11, 19] 等数据集只提供二值标签（低美学或高美学），难以用于评分预测。我们的数据集与 AVA 的一个关键区别在于，AVA 中许多图像经过重度编辑或为合成图像（见图 2），而 AADB 中专业照片与消费级照片的分布更为均衡。更重要的是，AVA 无法识别同一评分者对多幅图像给出的评分。我们报告的实验结果显示，训练数据上的评分者身份为改进美学预测器提供了有用的旁支信息。

**EN** Consistency Analysis of the Annotation: One concern is that the annotations provided by five AMT workers for each image may not be reliable given the subjective nature of the task. Therefore, we conduct consistency analysis on the annotations. Since the same five workers annotate a batch of ten images, we study the consistency at batch level. We use Spearman’s rank correlation ⟦SLOT_16⟧ between pairs of workers to measure consistency within a batch and estimate ⟦SLOT_17⟧-values to evaluate statistical significance of the correlation relative to a null hypothesis of uncorrelated responses. We use the Benjamini-Hochberg procedure to control the false discovery rate (FDR) for multiple comparisons [1]. At an FDR level of ⟦SLOT_18⟧, we find ⟦SLOT_19⟧ batches have significant agreement among raters. This shows that the annotations are reliable for scientific research. Further consistency analysis of the dataset can be found in the supplementary material.

**ZH** 标注的一致性分析：由于该任务具有主观性，一个可能的疑虑是五位 AMT 工作者对每幅图像的标注未必可靠。为此，我们对标注进行了一致性分析。由于同一批十幅图像由相同的五位工作者标注，我们在批次层面考察一致性：用工作者两两之间的斯皮尔曼秩相关 ⟦SLOT_16⟧ 度量批次内的一致性，并估计 ⟦SLOT_17⟧ 值以评估该相关性相对于“响应互不相关”这一零假设的统计显著性。我们采用 Benjamini-Hochberg 程序来控制多重比较下的错误发现率（FDR）[1]。在 FDR 水平 ⟦SLOT_18⟧ 下，我们发现 ⟦SLOT_19⟧ 个批次中评分者之间具有显著一致性。这表明标注对于科学研究是可靠的。数据集的进一步一致性分析见补充材料。

**EN** 4 Fusing Attributes and Content for Aesthetics Ranking

**ZH** 4 融合属性与内容的美学排序

**EN** Inspired by [31, 17], we start by fine-tuning AlexNet [12] using regression loss to predict aesthetic ratings. We then fine-tune a Siamese network [3] which takes image pairs as input and is trained with a joint Euclidean and ranking loss (Section 4.2). We then append attribute (Section 4.3) and content category classification layers (Section 4.4) and perform joint optimization.

**ZH** 受 [31, 17] 启发，我们首先用回归损失微调 AlexNet [12] 以预测美学评分；随后微调一个孪生网络（Siamese network）[3]，该网络以图像对为输入，采用欧氏损失与排序损失的联合目标进行训练（第 4.2 节）；最后追加属性分类层（第 4.3 节）与内容类别分类层（第 4.4 节），并执行联合优化。

**EN** 4.1 Regression Network for Aesthetics Rating

**ZH** 4.1 用于美学评分的回归网络

**EN** The network used in our image aesthetics rating is fine-tuned from AlexNet [12] which is used for image classification. Since our initial model predicts a continuous aesthetic score other than category labels, we replace the softmax loss with the Euclidean loss given by ⟦SLOT_20⟧, where ⟦SLOT_21⟧ is the average ground-truth rating for image-⟦SLOT_22⟧, and ⟦SLOT_23⟧ is the estimated score by the CNN model. Throughout our work, we re-scale all the ground-truth ratings to be in the range of ⟦SLOT_24⟧ when preparing the data. Consistent with observations in [17], we find that fine-tuning the pre-trained AlexNet [12] model performs better than that training the network from scratch.

**ZH** 图像美学评分所用的网络由用于图像分类的 AlexNet [12] 微调而来。由于我们的初始模型预测的是连续美学分数而非类别标签，我们将 softmax 损失替换为由 ⟦SLOT_20⟧ 给出的欧氏损失，其中 ⟦SLOT_21⟧ 是第 ⟦SLOT_22⟧ 幅图像的平均真实评分，⟦SLOT_23⟧ 是 CNN 模型估计的分数。在准备数据时，我们统一将所有真实评分重新缩放到 ⟦SLOT_24⟧ 区间。与 [17] 中的观察一致，我们发现微调预训练的 AlexNet [12] 模型优于从零开始训练网络。

<!-- [原子块 · object]  -->

**EN** Figure 3: Architectures for our different models. All models utilize the AlexNet front-end architecture which we augment by (a) replacing the top softmax layer with a regression net and adopting ranking loss in addition to Euclidean loss for training, (b) adding an attribute predictor branch which is then fused with the aesthetic branch to produce a final attribute-adapted rating and (c) incorporating image content scores that act as weights to gate the combination of predictions from multiple content-specific branches.

**ZH** 图 3：我们不同模型的结构。所有模型均以 AlexNet 前端结构为基础，并在此基础上做了三处扩展：（a）将顶部的 softmax 层替换为回归网络，并在训练中除欧氏损失外引入排序损失；（b）增加属性预测分支，与美学分支融合以产生最终的属性自适应评分；（c）引入图像内容分数作为权重，对多个内容特定分支的预测进行门控组合。

**EN** 4.2 Pairwise Training and Sampling Strategies

**ZH** 4.2 成对训练与采样策略

**EN** A model trained solely to minimize the Euclidean loss may still make mistakes in the relative rankings of images that have similar average aesthetic scores. However, more accurate fine-grained ranking of image aesthetics is quite important in applications (e.g. in automating photo album management [4]). Therefore, based on the Siamese network [3], we adopt a pairwise ranking loss to explicitly exploit relative rankings of image pairs available in the AADB data (see Fig. 3 (a)). The ranking loss is given by:

**ZH** 仅以最小化欧氏损失为目标训练的模型，仍可能在平均美学分数相近的图像之间给出错误的相对排序。然而，更精确的细粒度美学排序在应用中相当重要（例如相册自动管理 [4]）。因此，我们基于孪生网络 [3] 采用成对排序损失，显式利用 AADB 数据中可用的图像对相对排序信息（见图 3（a））。排序损失定义为：

<!-- [原子块 · table] l ​ o ​ s ​ s r ​ a ​ n ​ k = 1 2 ​ N ​ ∑ i , j max ⁡ ( 0 , α − δ ⁡ ( y i ≥ y j ) ​ ( y ^ i − y ^ j ) ) \small\begin{split}loss_{rank}=&\frac{1}{2N}\sum_{i,j}\max\big(0,\alpha-\delta(y_{i}\geq y_{j})( -->

**EN** where ⟦SLOT_25⟧, and ⟦SLOT_26⟧ is a specified margin parameter. By adjusting this margin and the sampling of image pairs, we can avoid the need to sample triplets as done in previous work on learning domain-specific similarity metrics [3, 32, 30]. Note that the regression alone focuses the capacity of the network on predicting the commonly occurring range of scores, while ranking penalizes mistakes for extreme scores more heavily.

**ZH** 其中 ⟦SLOT_25⟧，⟦SLOT_26⟧ 是指定的间隔参数。通过调节该间隔以及图像对的采样方式，我们可以避免像此前学习领域特定相似度度量的工作 [3, 32, 30] 那样去采样三元组。需要说明的是，回归损失使网络能力集中于预测常见分数区间，而排序损失则对极端分数上的错误施加更重的惩罚。

**EN** In order to anchor the scores output by the ranker to the same scale as user ratings, we utilize a joint loss function that includes both ranking and regression:

**ZH** 为使排序器输出的分数与用户评分保持在同一尺度上，我们采用同时包含排序损失与回归损失的联合损失函数：

<!-- [原子块 · table] l ​ o ​ s ​ s r ​ e ​ g + r ​ a ​ n ​ k = l ​ o ​ s ​ s r ​ e ​ g + ω r ​ l ​ o ​ s ​ s r ​ a ​ n ​ k , \small loss_{reg+rank}=loss_{reg}+\omega_{r}loss_{rank}, (2) -->

**EN** where the parameter ⟦SLOT_27⟧ controls the relative importance of the ranking loss and is set based on validation data. The network structure is shown in Fig. 3 (a).

**ZH** 其中参数 ⟦SLOT_27⟧ 控制排序损失的相对重要性，其取值依据验证数据确定。网络结构如图 3（a）所示。

**EN** Such a structure allows us to utilize different pair-sampling strategies to narrow the scope of learning and provide more consistent training. In our work, we investigate two strategies for selecting pairs of images used in computing the ranking loss. First, we can bias sampling towards pairs of images with a relatively large difference in their average aesthetic scores. For these pairs, the ground-truth rank order is likely to be stable (agreed upon by most raters). Second, as we have raters’ identities across images, we can sample image pairs that have been scored by the same individual. While different raters may have different aesthetics tastes which erode differences in the average aesthetic score, we expect a given individual should have more consistent aesthetic judgements across multiple images. We show the empirical effectiveness of these sampling strategies in Section 5.

**ZH** 这种结构使我们能够采用不同的图像对采样策略，从而收窄学习范围并提供更一致的训练信号。本文考察了两种用于计算排序损失的图像对选取策略。其一，偏向采样平均美学分数差异较大的图像对；对于这些图像对，真实的排序关系很可能稳定（为多数评分者所认同）。其二，由于我们掌握了跨图像的评分者身份，可以采样由同一位评分者打分的图像对。不同评分者的审美偏好差异会削弱平均美学分数上的差别，而我们预期同一个体在多幅图像上的美学判断应当更为一致。第 5 节将展示这些采样策略的实际效果。

**EN** 4.3 Attribute-Adaptive Model

**ZH** 4.3 属性自适应模型

**EN** Previous work on aesthetic prediction has investigated the use of attribute labels as input features for aesthetics classification (e.g. [6]). Rather than independently training attribute classifiers, we propose to include additional activation layers in our ranking network that are trained to encode informative attributes. We accomplish this by including an additional term in the loss function that encourages the appropriate attribute activations. In practice, annotating attributes for each training image is expensive and time consuming. This approach has the advantage that it can be used even when only a subset of training data comes with attribute annotations. Our approach is inspired by [16] which also integrates attribute classifiers, but differs in that the attribute-related layer shares the same front-end feature extraction with the aesthetic score predictor (see Fig. 3(b)). The attribute prediction task can thus be viewed as a source of side-information or “deep supervision” [13] that serves to regularize the weights learned during training even though it is not part of the test-time prediction, though could be enabled when needed.

**ZH** 此前的美学预测工作研究了把属性标签作为输入特征用于美学分类（如 [6]）。我们不对属性分类器做独立训练，而是在排序网络中额外加入激活层，并将其训练为编码有信息量的属性。具体做法是在损失函数中增加一项，鼓励产生恰当的属性激活。在实际应用中，为每幅训练图像标注属性既昂贵又耗时，而该方法的优势在于即便只有一部分训练数据带有属性标注也可使用。我们的思路受 [16] 启发——该工作同样整合了属性分类器，但不同之处在于我们的属性相关层与美学分数预测器共享同一套前端特征提取（见图 3（b））。因此，属性预测任务可视为一种旁支信息或“深度监督”[13]，用于正则化训练中学到的权重；它虽不属于测试时的预测环节，但在需要时可以启用。

**EN** We add an attribute prediction branch on top of the second fully-connected layer in the aesthetics-rating network described previously. The attribute predictions from this layer are concatenated with the base model to predict the final aesthetic score. When attribute annotations are available, we utilize a ⟦SLOT_28⟧-way softmax loss or Euclidean loss, denoted by ⟦SLOT_29⟧, for the attribute activations and combine it with the rating and ranking losses

**ZH** 我们在前述美学评分网络第二个全连接层之上增加一个属性预测分支，该层输出的属性预测与基础模型拼接后用于预测最终的美学分数。当属性标注可用时，我们对属性激活采用 ⟦SLOT_28⟧ 路 softmax 损失或欧氏损失（记作 ⟦SLOT_29⟧），并将其与评分损失、排序损失合并

<!-- [原子块 · table] l ​ o ​ s ​ s = l ​ o ​ s ​ s r ​ e ​ g + ω r ​ l ​ o ​ s ​ s r ​ a ​ n ​ k + ω a ​ l ​ o ​ s ​ s a ​ t ​ t \begin{split}loss=&loss_{reg}+\omega_{r}loss_{rank}+\omega_{a}loss_{att}\end{split} (3) -->

**EN** where ⟦SLOT_30⟧ controls relative importance of attribute fine-tuning. If we do not have enough data with attribute annotations, we can freeze the attribute layer and only fine-tune through the other half of the concatenation layer.

**ZH** 其中 ⟦SLOT_30⟧ 控制属性微调的相对重要性。若带属性标注的数据不足，我们可以冻结属性层，仅通过拼接层的另一半进行微调。

**EN** 4.4 Content-Adaptive Model

**ZH** 4.4 内容自适应模型

**EN** The importance of particular photographic attributes depends strongly on image content [18]. For example, as demonstrated by Fig. 1, vivid color and rule of thirds are highly relevant in rating landscapes but not for closeup portraits. In [23, 15], contents at the category level are assumed to be given in both training and testing stages, and category-specific models are then trained or fine-tuned. Here we propose to incorporate the category information into our model for joint optimization and prediction, so that the model can also work on those images with unknown category labels.

**ZH** 特定摄影属性的重要程度在很大程度上取决于图像内容 [18]。例如，如图 1 所示，鲜艳色彩与三分法在评价风景照时密切相关，但在评价特写人像时并非如此。在 [23, 15] 中，类别级的内容在训练与测试阶段均被假定为已知，随后训练或微调特定于类别的模型。我们则提出将类别信息纳入模型做联合优化与预测，使模型也能处理类别标签未知的图像。

**EN** We fine-tune the top two layers of AlexNet [12] with softmax loss to train a content-specific branch to predict category labels33 3 Even though category classification uses different features from those in aesthetics rating, we assume the low-level features can be shared across aesthetics and category levels. (as shown by ContClass layer in Fig. 3 (c)). Rather than making a hard category selection, we use the softmax output as a weighting vector for combining the scores produced by the category specific branches, each of which is a concatenation of attribute feature and content-specific features (denoted by Att⟦SLOT_31⟧fea and Cont⟦SLOT_32⟧fea respectively in Fig. 3 (c)). This allows for content categories to be non-exclusive (e.g. a photo of an individual in a nature scene can utilize attributes for either portrait and scenery photos). During training, When fine-tuning the whole net as in Fig. 3 (c), we freeze the content-classification branch and fine-tune the rest network.

**ZH** 我们用 softmax 损失微调 AlexNet [12] 的顶部两层，训练内容特定分支以预测类别标签33 3 尽管类别分类所用的特征与美学评分所用特征不同，我们假定底层特征可以在美学层面与类别层面之间共享。（如图 3（c）中的 ContClass 层所示）。我们不做硬性的类别选择，而是把 softmax 输出作为权重向量，用于组合各类别特定分支产生的分数；每个分支都是属性特征与内容特定特征的拼接（在图 3（c）中分别记作 Att⟦SLOT_31⟧fea 与 Cont⟦SLOT_32⟧fea）。这样一来，内容类别之间可以互不排斥（例如，一幅人物处于自然场景中的照片，可以同时利用人像与风景两类照片的属性）。训练时，在按图 3（c）微调整个网络的过程中，我们冻结内容分类分支，只微调网络的其余部分。

**EN** 4.5 Implementation Details

**ZH** 4.5 实现细节

**EN** We warp images to ⟦SLOT_33⟧ and randomly crop out a ⟦SLOT_34⟧ window to feed into the network. The initial learning rate is set at 0.0001 for all layers, and periodically annealed by 0.1. We set weight decay ⟦SLOT_35⟧ and momentum ⟦SLOT_36⟧. We use Caffe toolbox [9] extended with our ranking loss for training all the models.

**ZH** 我们将图像形变为 ⟦SLOT_33⟧，并随机裁剪出 ⟦SLOT_34⟧ 的窗口送入网络。所有层的初始学习率设为 0.0001，并按 0.1 的因子周期性衰减。权重衰减设为 ⟦SLOT_35⟧，动量设为 ⟦SLOT_36⟧。所有模型均使用扩展了我们排序损失的 Caffe 工具箱 [9] 进行训练。

**EN** To train attribute-adaptive layers, we use softmax loss on AVA dataset which only has binary labels for attributes, and the Euclidean loss on the AADB dataset which has finer-level attribute scores. We notice that, on the AVA dataset, our attribute-adaptive branch yields ⟦SLOT_37⟧ AP and ⟦SLOT_38⟧ mAP for attribute prediction, which are comparable to the reported results of style-classification model fine-tuned from AlexNet [17]. When learning content-adaptive layers on the AVA dataset for classifying eight categories, we find the content branch yields ⟦SLOT_39⟧ content classification accuracy on the testing set. If we fine-tune the whole AlexNet, we obtain ⟦SLOT_40⟧ classification accuracy. Note that we are not pursuing the best classification performance on either attributes or categories. Rather, our aim is to train reasonable branches that perform well enough to help with image aesthetics rating.

**ZH** 训练属性自适应层时，我们在仅含属性二值标签的 AVA 数据集上采用 softmax 损失，而在属性分数更精细的 AADB 数据集上采用欧氏损失。我们注意到，在 AVA 数据集上，属性自适应分支取得 ⟦SLOT_37⟧ 的 AP 与 ⟦SLOT_38⟧ 的 mAP，与从 AlexNet 微调的 style 分类模型 [17] 所报告结果相当。在 AVA 数据集上学习用于八类分类的内容自适应层时，内容分支在测试集上取得 ⟦SLOT_39⟧ 的内容分类准确率；若微调整个 AlexNet，则分类准确率为 ⟦SLOT_40⟧。需要说明的是，我们的目标并非在属性或类别上取得最佳分类性能，而是训练出足够好、能够助力图像美学评分的分支。

**EN** 5 Experimental Results

**ZH** 5 实验结果

**EN** To validate our model for rating image aesthetics, we first compare against several baselines including the intermediate models presented in Section 4, then analyze the dependence of model performance on the model parameters and structure, and finally compare performance of our model with human annotation in rating image aesthetics.

**ZH** 为验证模型在图像美学评分上的有效性，我们首先与若干基线方法（包括第 4 节给出的中间模型）比较，然后分析模型性能对参数与结构的依赖，最后将模型与人类标注在图像美学评分上的表现进行对比。

**EN** 5.1 Benchmark Datasets

**ZH** 5.1 基准数据集

**EN** AADB dataset contains 10,000 images in total, with detailed aesthetics and attribute ratings, and anonymized raters’ identity for specific images. We split the dataset into training (8,500), validation (500) and testing (1,000) sets. Since our dataset does not include ground-truth image content tags, we use clustering to find semantic content groups prior to training content adaptive models. Specifically, we represent each image using the fc7 features, normalize the feature vector to be unit Euclidean length, and use unsupervised ⟦SLOT_41⟧-means for clustering. In our experimental comparison, we cluster training images into ⟦SLOT_42⟧ content groups, and transform the distances between a testing image and the centroids into prediction weights using a softmax. The value of ⟦SLOT_43⟧ was chosen using validation data (see Section 5.3). Fig. 4 shows samples from four of these clusters, from which we observe consistencies within each cluster and distinctions across clusters.

**ZH** AADB 数据集共含 10,000 幅图像，提供细致的美学与属性评分，以及特定图像的匿名评分者身份。我们将数据集划分为训练集（8,500）、验证集（500）与测试集（1,000）。由于该数据集不含图像内容的真实标注，我们在训练内容自适应模型之前先用聚类找出语义内容分组。具体地，我们用 fc7 特征表示每幅图像，将特征向量归一化为单位欧氏长度，再用无监督的 ⟦SLOT_41⟧-means 聚类。在实验对比中，我们把训练图像聚为 ⟦SLOT_42⟧ 个内容组，并用 softmax 将测试图像到各聚类中心的距离转换为预测权重。⟦SLOT_43⟧ 的取值依据验证数据确定（见第 5.3 节）。图 4 给出了其中四个聚类的样本，从中可以观察到聚类内部的一致性与聚类之间的差异。

**EN** AVA dataset contains approximately 250,000 images, each of which has about 200 aesthetic ratings ranging on a one-to-ten scale. For fair comparison, we follow the experimental practices and train/test split used in literature [16, 17, 23] which results in about 230,000 training and 20,000 test images. When fine-tuning AlexNet for binary aesthetics classification, we divide the training set into two categories (low- and high-aesthetic category), with a score threshold of 5 as used in [16, 17, 23]. We use the subset of images which contain style attributes and content tags for training and testing the attribute-adaptive and content-adaptive branches.

**ZH** AVA 数据集约含 250,000 幅图像，每幅图像约有 200 个 1 到 10 分制的美学评分。为保证公平比较，我们沿用文献 [16, 17, 23] 的实验做法与训练／测试划分，得到约 230,000 幅训练图像与 20,000 幅测试图像。在微调 AlexNet 做二值美学分类时，我们按 [16, 17, 23] 的做法以 5 分为阈值将训练集划分为低美学与高美学两类。训练与测试属性自适应和内容自适应分支时，我们使用带有风格属性与内容标签的图像子集。

**EN** 5.2 Performance Evaluation

**ZH** 5.2 性能评估

**EN** To evaluate the aesthetic scores predicted by our model, we report the ranking correlation measured by Spearman’s ⟦SLOT_44⟧ between the estimated aesthetics scores and the ground-truth scores in the test set [25]. Let ⟦SLOT_45⟧ indicate the rank of the ⟦SLOT_46⟧th item when we sort the list by scores ⟦SLOT_47⟧ and ⟦SLOT_48⟧ indicate the rank when ordered by ⟦SLOT_49⟧. We can compute the disagreement in the two rankings of a particular element ⟦SLOT_50⟧ as ⟦SLOT_51⟧. The Spearman’s ⟦SLOT_52⟧ rank correlation statistic is calculated as ⟦SLOT_53⟧, where ⟦SLOT_54⟧ is the total number of images ranked. This correlation coefficient lies in the range of ⟦SLOT_55⟧, with larger values corresponding to higher correlation in the rankings. The ranking correlation is particularly useful since it is invariant to monotonic transformations of the aesthetic score predictions and hence avoids the need to precisely calibrate output scores against human ratings. For purposes of comparing to existing classification accuracy results reported on the AVA dataset, we simply threshold the estimated scores ⟦SLOT_56⟧ to produce a binary prediction where the threshold ⟦SLOT_57⟧ is determined on the validation set.

**ZH** 为评估模型预测的美学分数，我们报告测试集上估计美学分数与真实分数之间由斯皮尔曼 ⟦SLOT_44⟧ 度量的排序相关性 [25]。记 ⟦SLOT_45⟧ 表示第 ⟦SLOT_46⟧ 个样本在按分数 ⟦SLOT_47⟧ 排序时的秩，⟦SLOT_48⟧ 表示按 ⟦SLOT_49⟧ 排序时的秩。对某个元素 ⟦SLOT_50⟧，两种排序的不一致程度可计算为 ⟦SLOT_51⟧。斯皮尔曼 ⟦SLOT_52⟧ 秩相关统计量按 ⟦SLOT_53⟧ 计算，其中 ⟦SLOT_54⟧ 为参与排序的图像总数。该相关系数取值位于 ⟦SLOT_55⟧ 区间，数值越大表示排序相关性越高。排序相关性之所以特别有用，是因为它对美学分数预测的单调变换保持不变，因而无需将输出分数与人类评分做精确校准。为了与 AVA 数据集上已有的分类准确率结果比较，我们只需对估计分数 ⟦SLOT_56⟧ 做阈值化即可得到二值预测，其中阈值 ⟦SLOT_57⟧ 在验证集上确定。

<!-- [原子块 · img]  -->

**EN** Figure 4: Example images from four content clusters found in the training set. These clusters capture thematic categories of image content present in AADB without requiring additional manual labeling of training data.

**ZH** 图 4：训练集中找到的四个内容聚类的示例图像。这些聚类捕捉了 AADB 中图像内容的主题类别，且无需对训练数据做额外的手工标注。

**EN** 5.3 Results

**ZH** 5.3 结果

**EN** Table 2: Performance comparison of different models on AADB dataset.

**ZH** 表 2：不同模型在 AADB 数据集上的性能比较。

<!-- [原子块 · table] Methods ρ \rho AlexNet _ \_ FT _ \_ Conf 0.5923 Reg 0.6239 Reg+Rank (cross-rater) 0.6308 Reg+Rank (within-rater) 0.6450 Reg+Rank (within- & \& cross-) 0.6515 Reg+Rank+Att 0.6656 Reg+Rank+Cont 0.6737 R -->

**EN** Table 3: Performance comparison of different models on AVA dataset.

**ZH** 表 3：不同模型在 AVA 数据集上的性能比较。

<!-- [原子块 · table] Methods ρ \rho ACC ( % \% ) Murray et al. [ 23 ] - 68.00 SPP [ 8 ] - 72.85 AlexNet _ \_ FT _ \_ Conf 0.4807 71.52 DCNN [ 16 ] - 73.25 RDCNN [ 16 ] - 74.46 RDCNN _ \_ semantic [ 15 ] - 75.42 DMA [ 17 ] -->

**EN** For comparison, we also train a model for binary aesthetics classification by fine-tuning AlexNet (AlexNet⟦SLOT_58⟧FT⟦SLOT_59⟧Conf). This has previously been shown to be a strong baseline for aesthetic classification [17]. We use the softmax confidence score corresponding of the high-aesthetics class as the predicted aesthetic rating. As described in Section 4, we consider variants of our architecture including the regression network alone (Reg), along with the addition of the pairwise ranking loss (Reg+Rank), attribute-constraint branches (Reg+Rank+Att) and content-adaptive branches (Reg+Rank+Cont). We also evaluate different pair-sampling strategies including within- and cross-rater sampling.

**ZH** 作为对比，我们还通过微调 AlexNet 训练了一个二值美学分类模型（AlexNet⟦SLOT_58⟧FT⟦SLOT_59⟧Conf），此前已被证明是美学分类的强基线 [17]。我们取高美学类别对应的 softmax 置信度分数作为预测的美学评分。如第 4 节所述，我们考察了结构的若干变体：仅用回归网络（Reg）、加入成对排序损失（Reg+Rank）、加入属性约束分支（Reg+Rank+Att）以及加入内容自适应分支（Reg+Rank+Cont）。我们还评估了不同的图像对采样策略，包括评分者内采样与评分者间采样。

**EN** Model Architecture and Loss Functions: Table 3 and 3 list the performance on AADB and AVA datasets, respectively. From these tables, we notice several interesting observations. First, AlexNet⟦SLOT_60⟧FT⟦SLOT_61⟧Conf model yields good ranking results measured by ⟦SLOT_62⟧. This indicates that the confidence score in softmax can provide information about relative rankings. Second, the regression net outperforms the AlexNet⟦SLOT_63⟧FT⟦SLOT_64⟧Conf model, and ranking loss further improves the ranking performance on both datasets. This shows the effectiveness of our ranking loss which considers relative aesthetics ranking of image pairs in training the model. More specifically, we can see from Table 3 that, by sampling image pairs according to the the averaged ground-truth scores, i.e. cross-rater sampling only, Reg+Rank (cross-rater) achieves the ranking coefficient ⟦SLOT_65⟧; whereas if only sampling image pairs within each raters, we have ⟦SLOT_66⟧ by by Reg+Rank (within-rater). This demonstrates the effectiveness of sampling image pairs within the same raters, and validates our idea that the same individual has consistent aesthetics ratings. When using both strategies to sample image pairs, the performance is even better by Reg+Rank (within- ⟦SLOT_67⟧ cross-), leading to ⟦SLOT_68⟧. This is possibly due to richer information contained in more training pairs. By comparing the results in Table 3 between “Reg” (0.4995) and “Reg+Rank” (0.5126), and between “Reg+Att” (0.5331) and “Reg+Rank+Att” (0.5445) , we clearly observe that the ranking loss improves the ranking correlation. In this case, we can only exploit the cross-rater sampling strategy since rater’s identities are not available in AVA for the stronger within-rater sampling approach. We note that for values of ⟦SLOT_69⟧ near ⟦SLOT_70⟧ computed over ⟦SLOT_71⟧ test images on AVA dataset, differences in rank correlation of ⟦SLOT_72⟧ are highly statistically significant. These results clearly show that the ranking loss helps enforce overall ranking consistency.

**ZH** 模型结构与损失函数：表 3 与表 3 分别列出了各模型在 AADB 与 AVA 数据集上的性能。由这些表格可以观察到若干有意思的现象。首先，AlexNet⟦SLOT_60⟧FT⟦SLOT_61⟧Conf 模型在以 ⟦SLOT_62⟧ 度量的排序结果上表现不错，说明 softmax 的置信度分数能够提供相对排序信息。其次，回归网络优于 AlexNet⟦SLOT_63⟧FT⟦SLOT_64⟧Conf 模型，而排序损失进一步提升了两个数据集上的排序性能，证明了在训练中考虑图像对相对美学排序的排序损失是有效的。更具体地，由表 3 可见：若按平均真实分数采样图像对，即仅用评分者间采样，Reg+Rank（cross-rater）取得的排序系数为 ⟦SLOT_65⟧；而若仅在各评分者内部采样图像对，Reg+Rank（within-rater）则达到 ⟦SLOT_66⟧。这证明了在同一评分者内部采样图像对的有效性，也验证了我们对同一个体美学评分具有一致性的判断。同时使用两种策略采样图像对时，Reg+Rank（within- ⟦SLOT_67⟧ cross-）的表现更好，达到 ⟦SLOT_68⟧，这可能是因为更多的训练图像对蕴含了更丰富的信息。通过比较表 3 中“Reg”（0.4995）与“Reg+Rank”（0.5126）、以及“Reg+Att”（0.5331）与“Reg+Rank+Att”（0.5445），可以清楚地看到排序损失提升了排序相关性。在此情形下，我们只能利用评分者间采样策略，因为 AVA 不提供评分者身份，无法使用效果更强的评分者内采样。需要说明的是，当 ⟦SLOT_69⟧ 取值在 ⟦SLOT_70⟧ 附近（在 AVA 数据集的 ⟦SLOT_71⟧ 幅测试图像上计算得到）时，排序相关性上 ⟦SLOT_72⟧ 的差异具有高度统计显著性。这些结果清楚地表明，排序损失有助于强化整体的排序一致性。

**EN** To show that improved performance is due to the side information (e.g. attributes) other than a wider architecture, we first train an ensemble of eight rating networks (Reg) and average the results, leading to a rho=0.5336 (c.f. Reg+Rank+Att which yields rho=0.5445). Second, we try directly training the model with a single Euclidean loss using a wider intermediate layer with eight times more parameters. In this case we observed severe overfitting. This suggests for now that the side-supervision is necessary to effectively train such an architecture.

**ZH** 为证明性能提升来自属性等旁支信息而不仅仅是更宽的网络结构，我们首先训练八个评分网络（Reg）做集成并取平均，得到 rho=0.5336（对比 Reg+Rank+Att 的 rho=0.5445）；其次，我们尝试用参数量扩大八倍的更宽中间层、仅以单一欧氏损失直接训练模型，此时观察到严重过拟合。这表明就目前而言，旁支监督对于有效训练这样的结构是必要的。

**EN** Third, when comparing Reg+Rank with Reg+Rank+Att, and Reg+Rank with Reg+ Rank+Cont, we can see that both attributes and content further improve ranking performance. While image content is not annotated on the AADB dataset, our content-adaptive model based on unsupervised ⟦SLOT_73⟧-means clustering still outperforms the model trained without content information. The performance benefit of adding attributes is substantially larger for AVA than AADB. We expect this is due to (1) differences in the definitions of attributes between the two datasets, and (2) the within-rater sampling for AADB, which already provides a significant boost making further improvement using attributes more difficult. The model trained with ranking loss, attribute-constraint and content-adaptive branches naturally performs the best among all models. It is worth noting that, although we focus on aesthetics ranking during training, we also achieve the state-of-the-art binary classification accuracy in AVA. This further validates our emphasis on relative ranking, showing that learning to rank photo aesthetics can naturally lead to good classification performance.

**ZH** 第三，比较 Reg+Rank 与 Reg+Rank+Att、以及 Reg+Rank 与 Reg+Rank+Cont 可见，属性与内容都能进一步提升排序性能。尽管 AADB 数据集没有图像内容标注，我们基于无监督 ⟦SLOT_73⟧-means 聚类的内容自适应模型仍然优于未使用内容信息的模型。加入属性带来的收益在 AVA 上明显大于 AADB，我们推测原因有两点：（1）两个数据集对属性的定义不同；（2）AADB 使用了评分者内采样，已带来显著提升，使得再用属性改进更加困难。综合排序损失、属性约束与内容自适应分支的模型在所有模型中自然表现最佳。需要说明的是，尽管训练时聚焦于美学排序，我们仍在 AVA 上取得了最佳的二分类准确率，这进一步印证了我们对相对排序的重视：学习对照片美学排序可以自然地带来良好的分类性能。

**EN** Table 4: Ranking performance ⟦SLOT_74⟧ vs. rank loss weighting ⟦SLOT_75⟧ in Eq. 2.

**ZH** 表 4：排序性能 ⟦SLOT_74⟧ 随式 2 中排序损失权重 ⟦SLOT_75⟧ 的变化。

<!-- [原子块 · table] ω r \omega_{r} 0.0 0.0 0.1 1 1 2 2 AADB 0.6382 0.6382 0.6442 0.6442 0.6515 0.6515 0.6276 0.6276 AVA 0.4995 0.4995 0.5126 0.4988 0.4988 0.4672 0.4672 -->

**EN** Table 5: Ranking performance (⟦SLOT_76⟧) of “Reg+Rank” with different numbers of sampled image pairs on AADB dataset.

**ZH** 表 5：AADB 数据集上“Reg+Rank”在不同图像对采样数量下的排序性能（⟦SLOT_76⟧）。

<!-- [原子块 · table] # \# ImgPairs 2 million 5 million cross-rater 0.6346 0.6286 within-rater 0.6450 0.6448 within- & \& cross-rater 0.6487 0.6515 -->

**EN** Model Hyperparameters: In training our content-adaptive model on the AADB dataset which lacks supervised content labels, the choice of cluster number is an important parameter. Fig. 6 plots the ⟦SLOT_77⟧ on validation data as a function of the number of clusters ⟦SLOT_78⟧ for the Reg+Cont model (without ranking loss). We can see the finer clustering improves performance as each content specific model can adapt to a sub-category of images. However, because the total dataset is fixed, performance eventually drops as the amount of training data available for tuning each individual content-adaptive branch decreases. We thus fixed ⟦SLOT_79⟧ for training our unified network on AADB.

**ZH** 模型超参数：在没有监督式内容标签的 AADB 数据集上训练内容自适应模型时，聚类数的选择是一个重要参数。图 6 给出了 Reg+Cont 模型（不含排序损失）在验证数据上的 ⟦SLOT_77⟧ 随聚类数 ⟦SLOT_78⟧ 的变化曲线。可以看到，更细的聚类能够提升性能，因为每个内容特定模型可以适配一个图像子类别；但由于数据集总量固定，随着可用于微调各内容自适应分支的训练数据减少，性能最终会下降。因此，在 AADB 上训练统一网络时，我们将 ⟦SLOT_79⟧ 固定下来。

**EN** The relative weightings of the loss terms (specified by ⟦SLOT_80⟧ in Eq. 2) is another important parameter. Table 5 shows the ranking correlation test performance on both datasets w.r.t. different choices of ⟦SLOT_81⟧. We observe that larger ⟦SLOT_82⟧ is favored in AADB than that in AVA, possibly due to the contribution from the within-rater image pair sampling strategy. We set ⟦SLOT_83⟧ (in Eq. 3) to ⟦SLOT_84⟧ for jointly fine-tuning attribute regression and aesthetic rating. For the rank loss, we used validation performance to set the margin ⟦SLOT_85⟧ to ⟦SLOT_86⟧ and ⟦SLOT_87⟧ on AVA and AADB respectively.

**ZH** 各损失项的相对权重（由式 2 中的 ⟦SLOT_80⟧ 指定）是另一个重要参数。表 5 给出了两个数据集上不同 ⟦SLOT_81⟧ 取值对应的排序相关性测试性能。我们观察到 AADB 更偏好较大的 ⟦SLOT_82⟧，这或许源于评分者内图像对采样策略的贡献。我们将式 3 中的 ⟦SLOT_83⟧ 设为 ⟦SLOT_84⟧，用于联合微调属性回归与美学评分。对于排序损失，我们依据验证性能将间隔 ⟦SLOT_85⟧ 在 AVA 与 AADB 上分别设为 ⟦SLOT_86⟧ 与 ⟦SLOT_87⟧。

**EN** Number of Sampled Image Pairs: Is it possible that better performance can be obtained through more sampled pairs instead of leveraging rater’s information? To test this, we sample 2 and 5 million image pairs given the fixed training images on the AADB dataset, and report in Table 5 the performance of model “Reg+Rank” using different sampling strategies, i.e. within-rater only, cross-rater only and within-⟦SLOT_88⟧cross-rater sampling. It should be noted the training image set remains the same, we just sample more pairs from them. We can see that adding more training pairs yields little differences in the final results, and even declines slightly when using higher cross-rater sampling rates. These results clearly emphasize the effectiveness of our proposed sampling strategy which (perhaps surprisingly) yields much bigger gains than simply increasing the number of training pairs by 2.5x.

**ZH** 图像对采样数量：是否有可能通过采样更多图像对而非利用评分者信息来获得更好的性能？为检验这一点，在 AADB 数据集训练图像固定的条件下，我们分别采样 200 万与 500 万图像对，并在表 5 中报告“Reg+Rank”模型在不同采样策略（仅评分者内、仅评分者间、评分者内⟦SLOT_88⟧评分者间）下的性能。需要说明的是，训练图像集保持不变，我们只是从中采样了更多图像对。可以看到，增加训练图像对数量对最终结果影响甚微，在提高评分者间采样比例时甚至略有下降。这些结果清楚地表明，我们所提采样策略的有效性远高于将训练图像对数量提升 2.5 倍这一简单做法，其收益之差令人意外。

**EN** Classification Benchmark Performance: Our model achieves state-of-the-art classification performance on the AVA dataset simply by thresholding the estimated score (Table 3). It is worth noting that our model uses only the whole warped down-sampled images for both training and testing, without using any high-resolution patches from original images. Considering the fact that the fine-grained information conveyed by high-resolution image patches is especially useful for image quality assessment and aesthetics analysis [16, 10, 17], it is quite promising to see our model performing so well. The best reported results [17] for models that use low resolution warped images for aesthetics classification are based on Spatial Pyramid Pooling Networks (SPP) [8] and achieves an accuracy of ⟦SLOT_89⟧. Compared to SPP, our model achieves ⟦SLOT_90⟧, a gain of ⟦SLOT_91⟧, even though our model is not tuned for classification. Previous work [10, 16, 17] has shown that leveraging the high-resolution patches could lead to additional ⟦SLOT_92⟧ potential accuracy improvement. We expect a further accuracy boost would be possible by applying this strategy with our model.

**ZH** 分类基准性能：我们的模型只需对估计分数做阈值化，便在 AVA 数据集上取得了最佳分类性能（表 3）。需要说明的是，模型在训练与测试中仅使用整幅形变降采样后的图像，未使用原始图像中的任何高分辨率图像块。考虑到高分辨率图像块所承载的细粒度信息对图像质量评估与美学分析尤为有用 [16, 10, 17]，我们的模型能取得如此成绩相当可期。在 [17] 报告的、使用低分辨率形变图像做美学分类的模型中，最好结果基于空间金字塔池化网络（SPP）[8]，准确率为 ⟦SLOT_89⟧。与 SPP 相比，我们的模型达到 ⟦SLOT_90⟧，提升 ⟦SLOT_91⟧——尽管模型并未针对分类任务调优。已有工作 [10, 16, 17] 表明，利用高分辨率图像块可带来额外的 ⟦SLOT_92⟧ 准确率提升空间；我们预期将该策略与本文模型结合还能进一步提高准确率。

<!-- [原子块 · object]  -->

**EN** Figure 5: Dependence of model performance by varying the number of content clusters. We select ⟦SLOT_93⟧ clusters in our experiments on AADB.

**ZH** 图 5：模型性能随内容聚类数的变化。我们在 AADB 实验中选取 ⟦SLOT_93⟧ 个聚类。

<!-- [原子块 · object]  -->

**EN** Figure 6: Panels show (left) the number of images labeled by each worker, and the performance of each individual rater w.r.t Spearman’s ⟦SLOT_94⟧ (Right). Red line shows our model’s performance.

**ZH** 图 6：各图分别显示（左）每位工作者标注的图像数量，以及（右）每位个体评分者相对于斯皮尔曼 ⟦SLOT_94⟧ 的表现。红线为本文模型的性能。

**EN** Table 6: Human perf. on the AADB dataset.

**ZH** 表 6：人类在 AADB 数据集上的表现。

<!-- [原子块 · table] # \# images # \# workers ρ \rho > > 0 190 0.6738 > > 100 65 0.7013 > > 200 42 0.7112 Our best – 0.6782 -->

**EN** Table 7: Cross dataset train/test evaluation.

**ZH** 表 7：跨数据集训练／测试评估。

<!-- [原子块 · table] Spearman’s ρ \rho test AADB AVA train AADB 0.6782 0.1566 AVA 0.3191 0.5154 -->

**EN** 5.4 Further Comparison with Human Rating Consistency

**ZH** 5.4 与人类评分一致性的进一步比较

**EN** We have shown that our model achieves a high level of agreement with average aesthetic ratings and outperforms many existing models. The raters’ identities and ratings for the images in our AADB dataset enable us to further analyze agreement between our model each individual as well as intra-rater consistency. While human raters produce rankings which are similar with high statistical significance, as evaluated in Section 3, there is variance in the numerical ratings between them.

**ZH** 我们已证明模型与平均美学评分具有较高的一致性，并优于许多现有模型。AADB 数据集中记录的评分者身份与评分，使我们能够进一步分析模型与每位个体之间的一致性，以及评分者内部的一致性。如第 3 节所评估，人类评分者产生的排序具有高度统计显著的相似性，但他们给出的数值评分之间存在差异。

**EN** To this end, we calculate ranking correlation ⟦SLOT_95⟧ between each individual’s ratings and the ground-truth average score. When comparing an individual to the ground-truth, we do not exclude that individual’s rating from the ground-truth average for the sake of comparable evaluations across all raters. Fig. 6 shows the number of images each rater has rated and their corresponding performance with respect to other raters. Interestingly, we find that the hard workers tend to provide more consistent ratings. In Table 7, we summarize the individuals’ performance by choosing a subset raters based on the number of images they have rated. This clearly indicates that the different human raters annotate the images consistently, and when labeling more images, raters contribute more stable rankings of the aesthetic scores.

**ZH** 为此，我们计算每位个体评分与真实平均分数之间的排序相关性 ⟦SLOT_95⟧。在将某个体与真实值比较时，为便于跨评分者公平比较，我们不把该个体的评分从真实平均值中剔除。图 6 给出了每位评分者评分的图像数量及其相对于其他评分者的表现。有意思的是，我们发现标注量大的工作者往往给出更一致的评分。在表 7 中，我们按评分者已标注图像数量选取子集，汇总了这些个体的表现。这清楚地表明，不同人类评分者对图像的标注是一致的，并且在标注更多图像时，评分者给出的美学分数排序更为稳定。

**EN** Interestingly, from Table 7, we can see that our model actually performs above the level of human consistency (as measured by ⟦SLOT_96⟧) averaged across all workers. However, when concentrating on the “power raters” who annotate more images, we still see a gap between machine and human level performance in terms of rank correlation ⟦SLOT_97⟧.

**ZH** 有意思的是，由表 7 可见，本文模型的表现实际上超过了全体工作者平均意义上的人类一致性水平（以 ⟦SLOT_96⟧ 度量）。然而，若把注意力集中在标注图像更多的“重度评分者”上，以排序相关性 ⟦SLOT_97⟧ 衡量，机器与人类水平之间仍存在差距。

**EN** 5.5 Cross-Dataset Evaluation

**ZH** 5.5 跨数据集评估

**EN** As discussed in Section 3, AVA contains professional images downloaded from a community based rating website; while our AADB contains a much more balanced distribution of consumer photos and professional photos rated by AMT workers, so has better generalizability to wide range of real-world photos.

**ZH** 如第 3 节所述，AVA 包含从社区评分网站下载的专业图像；而我们的 AADB 由 AMT 工作者评分，消费级照片与专业照片的分布更为均衡，因而能更好地泛化到广泛的真实照片。

**EN** To quantify the differences between these datasets, we evaluate whether models trained on one dataset perform well on the other. Table 7 provides a comparison of the cross-dataset performance. Interestingly, we find the models trained on either dataset have very limited “transferability”. We conjecture there are two reasons. First, different groups of raters have different aesthetics tastes. This can be verified that, when looking at the DPChallenge website where images and ratings in the AVA dataset were taken from. DPChallenge provides a breakdown of scores which shows notable differences between the average scores among commenters, participants and non-participants. Second, the two datasets contain photos with different distributions of visual characteristics. For example, many AVA photos are professionally photographed or heavily edited; while AADB contains many daily photos from casual users. This observation motivates the need for further exploration into mechanisms for learning aesthetic scoring that is adapted to the tastes of specific user groups or photo collections [2].

**ZH** 为量化这些数据集之间的差异，我们评估在一个数据集上训练的模型在另一个数据集上的表现。表 7 给出了跨数据集性能的比较。有意思的是，我们发现无论在哪一个数据集上训练，模型的“可迁移性”都非常有限。我们推测有两方面原因：其一，不同评分者群体的审美偏好不同。这一点可以在 DPChallenge 网站（AVA 数据集的图像与评分来源）得到验证，该网站提供了分数细分，显示评论者、参与者与非参与者之间的平均分存在明显差异。其二，两个数据集中照片的视觉特征分布不同，例如 AVA 中许多照片为专业拍摄或经过重度编辑，而 AADB 包含大量普通用户的日常照片。这一观察提示我们，需要进一步探索能够适配特定用户群体或照片集合品味的美学打分机制 [2]。

**EN** 6 Conclusion

**ZH** 6 结论

**EN** We have proposed a CNN-based method that unifies photo style attributes and content information to rate image aesthetics. In training this architecture, we leverage individual aesthetic rankings which are provided by a novel dataset that includes aesthetic and attribute scores of multiple images by individual users. We have shown that our model is also effective on existing classification benchmarks for aesthetic judgement. Despite not using high-resolution image patches, the model achieves state-of-the-art classification performance on the AVA benchmark by simple thresholding. Comparison to individual raters suggests that our model performs as well as the “average” mechanical turk worker but still lags behind more consistent workers who label large batches of images. These observations suggest future work in developing aesthetic rating systems that can adapt to individual user preferences.

**ZH** 我们提出了一种基于 CNN 的方法，将照片风格属性与内容信息统一起来对图像美学进行评分。在训练该结构时，我们利用了一个新数据集提供的个体美学排序，其中包含了个体用户对多幅图像给出的美学分数与属性分数。我们还表明，该模型在现有的美学判断分类基准上同样有效。尽管没有使用高分辨率图像块，模型仅通过简单阈值化便在 AVA 基准上取得了最佳分类性能。与个体评分者的比较显示，本文模型的表现与“平均”水平的 Mechanical Turk 工作者相当，但仍落后于那些标注大批图像、一致性更高的工作者。这些观察为未来研究指明了方向：开发能够适配个体用户偏好的美学评分系统。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] [1] Benjamini, Y., Yekutieli, D.: The control of the false discovery rate in multiple testing under dependency. Annals of statistics pp. 1165–1188 (2001) -->

<!-- [原子块 · verbatim] [2] Caicedo, J.C., Kapoor, A., Kang, S.B.: Collaborative personalization of image enhancement. In: Computer Vision and Pattern Recognition (CVPR), 2011 IEEE Conference on. pp. 249–256. IEEE (2011) -->

<!-- [原子块 · verbatim] [3] Chopra, S., Hadsell, R., LeCun, Y.: Learning a similarity metric discriminatively, with application to face verification. In: Computer Vision and Pattern Recognition, 2005. CVPR 2005. IEEE Compute -->

<!-- [原子块 · verbatim] [4] Cui, J., Wen, F., Xiao, R., Tian, Y., Tang, X.: Easyalbum: an interactive photo annotation system based on face clustering and re-ranking. In: Proceedings of the SIGCHI conference on Human factors -->

<!-- [原子块 · verbatim] [5] Datta, R., Joshi, D., Li, J., Wang, J.Z.: Studying aesthetics in photographic images using a computational approach. In: ECCV. pp. 288–301. Springer (2006) -->

<!-- [原子块 · verbatim] [6] Dhar, S., Ordonez, V., Berg, T.L.: High level describable attributes for predicting aesthetics and interestingness. In: Computer Vision and Pattern Recognition (CVPR), 2011 IEEE Conference on. pp. -->

<!-- [原子块 · verbatim] [7] Geng, B., Yang, L., Xu, C., Hua, X.S., Li, S.: The role of attractiveness in web image search. In: Proceedings of the 19th ACM International Conference on Multimedia. pp. 63–72. ACM (2011) -->

<!-- [原子块 · verbatim] [8] He, K., Zhang, X., Ren, S., Sun, J.: Spatial pyramid pooling in deep convolutional networks for visual recognition. In: ECCV, pp. 346–361. Springer (2014) -->

<!-- [原子块 · verbatim] [9] Jia, Y., Shelhamer, E., Donahue, J., Karayev, S., Long, J., Girshick, R., Guadarrama, S., Darrell, T.: Caffe: Convolutional architecture for fast feature embedding. arXiv preprint arXiv:1408.5093  -->

<!-- [原子块 · verbatim] [10] Kang, L., Ye, P., Li, Y., Doermann, D.: Convolutional neural networks for no-reference image quality assessment. In: Computer Vision and Pattern Recognition (CVPR), 2014 IEEE Conference on. pp. 1 -->

<!-- [原子块 · verbatim] [11] Ke, Y., Tang, X., Jing, F.: The design of high-level features for photo quality assessment. In: Computer Vision and Pattern Recognition, 2006 IEEE Computer Society Conference on. vol. 1, pp. 419– -->

<!-- [原子块 · verbatim] [12] Krizhevsky, A., Sutskever, I., Hinton, G.E.: Imagenet classification with deep convolutional neural networks. In: Advances in neural information processing systems. pp. 1097–1105 (2012) -->

<!-- [原子块 · verbatim] [13] Lee, C., Xie, S., Gallagher, P.W., Zhang, Z., Tu, Z.: Deeply-supervised nets. In: AISTATS (2015) -->

<!-- [原子块 · verbatim] [14] Lowe, D.G.: Distinctive image features from scale-invariant keypoints. International journal of computer vision 60(2), 91–110 (2004) -->

<!-- [原子块 · verbatim] [15] Lu, X., Lin, Z., Jin, H., Yang, J., Wang, J.: Rating pictorial aesthetics using deep learning. IEEE Transactions on Multimedia (2015) -->

<!-- [原子块 · verbatim] [16] Lu, X., Lin, Z., Jin, H., Yang, J., Wang, J.Z.: Rapid: Rating pictorial aesthetics using deep learning. In: Proceedings of the ACM International Conference on Multimedia. pp. 457–466. ACM (2014) -->

<!-- [原子块 · verbatim] [17] Lu, X., Lin, Z., Shen, X., Mech, R., Wang, J.Z.: Deep multi-patch aggregation network for image style, aesthetics, and quality estimation. ICCV (2015) -->

<!-- [原子块 · verbatim] [18] Luo, W., Wang, X., Tang, X.: Content-based photo quality assessment. In: Computer Vision (ICCV), 2011 IEEE International Conference on. pp. 2206–2213. IEEE (2011) -->

<!-- [原子块 · verbatim] [19] Luo, Y., Tang, X.: Photo and video quality evaluation: Focusing on the subject. In: ECCV, pp. 386–399. Springer (2008) -->

<!-- [原子块 · verbatim] [20] Marchesotti, L., Murray, N., Perronnin, F.: Discovering beautiful attributes for aesthetic image analysis. International Journal of Computer Vision pp. 1–21 (2014) -->

<!-- [原子块 · verbatim] [21] Marchesotti, L., Perronnin, F., Larlus, D., Csurka, G.: Assessing the aesthetic quality of photographs using generic image descriptors. In: ICCV. pp. 1784–1791. IEEE (2011) -->

<!-- [原子块 · verbatim] [22] Marchesotti, L., Perronnin, F., Meylan, F.: Learning beautiful (and ugly) attributes. BMVC (2013) -->

<!-- [原子块 · verbatim] [23] Murray, N., Marchesotti, L., Perronnin, F.: Ava: A large-scale database for aesthetic visual analysis. In: Computer Vision and Pattern Recognition (CVPR), 2012 IEEE Conference on. pp. 2408–2415.  -->

<!-- [原子块 · verbatim] [24] Murray, N., Marchesotti, L., Perronnin, F., Meylan, F.: Learning to rank images using semantic and aesthetic labels. In: BMVC. pp. 1–10 (2012) -->

<!-- [原子块 · verbatim] [25] Myers, J.L., Well, A., Lorch, R.F.: Research design and statistical analysis. Routledge (2010) -->

<!-- [原子块 · verbatim] [26] Nishiyama, M., Okabe, T., Sato, I., Sato, Y.: Aesthetic quality classification of photographs based on color harmony. In: Computer Vision and Pattern Recognition (CVPR), 2011 IEEE Conference on.  -->

<!-- [原子块 · verbatim] [27] Perronnin, F., Dance, C.: Fisher kernels on visual vocabularies for image categorization. In: Computer Vision and Pattern Recognition, 2007. CVPR’07. IEEE Conference on. pp. 1–8. IEEE (2007) -->

<!-- [原子块 · verbatim] [28] Perronnin, F., Sánchez, J., Mensink, T.: Improving the fisher kernel for large-scale image classification. In: ECCV, pp. 143–156. Springer (2010) -->

<!-- [原子块 · verbatim] [29] San Pedro, J., Yeh, T., Oliver, N.: Leveraging user comments for aesthetic aware image search reranking. In: Proceedings of the 21st international conference on World Wide Web. pp. 439–448. ACM ( -->

<!-- [原子块 · verbatim] [30] Schroff, F., Kalenichenko, D., Philbin, J.: Facenet: A unified embedding for face recognition and clustering. In: CVPR. pp. 815–823 (2015) -->

<!-- [原子块 · verbatim] [31] Simonyan, K., Zisserman, A.: Very deep convolutional networks for large-scale image recognition. arXiv preprint arXiv:1409.1556 (2014) -->

<!-- [原子块 · verbatim] [32] Wang, J., Song, Y., Leung, T., Rosenberg, C., Wang, J., Philbin, J., Chen, B., Wu, Y.: Learning fine-grained image similarity with deep ranking. In: Computer Vision and Pattern Recognition (CVPR) -->

**EN** Appendix: Aesthetics and Attributes Database (AADB)

**ZH** 附录：美学与属性数据库（AADB）

**EN** Attributes in AADB

**ZH** AADB 中的属性

**EN** We select eleven attributes that are highly related to image aesthetics after consulting professional photographers, which are

**ZH** 在咨询专业摄影师后，我们选取了与图像美学高度相关的十一项属性，分别是

**EN** 1. “balancing element” – whether the image contains balanced elements;

**ZH** 1.“balancing element”（平衡元素）——图像是否包含平衡的元素；

**EN** 2. “content” – whether the image has good/interesting content;

**ZH** 2.“content”（内容）——图像是否具有好的／有趣的内容；

**EN** 3. “color harmony” – whether the overall color of the image is harmonious;

**ZH** 3.“color harmony”（色彩和谐）——图像整体色彩是否和谐；

**EN** 4. “depth of field” – whether the image has shallow depth of field;

**ZH** 4.“depth of field”（景深）——图像是否具有浅景深；

**EN** 5. “lighting” – whether the image has good/interesting lighting;

**ZH** 5.“lighting”（光照）——图像是否具有好的／有趣的光照；

**EN** 6. “motion blur” – whether the image has motion blur;

**ZH** 6.“motion blur”（运动模糊）——图像是否存在运动模糊；

**EN** 7. “object emphasis” – whether the image emphasizes foreground objects;

**ZH** 7.“object emphasis”（主体突出）——图像是否突出前景主体；

**EN** 8. “rule of thirds” – whether the photography follows rule of thirds;

**ZH** 8.“rule of thirds”（三分法）——拍摄是否遵循三分法；

**EN** 9. “vivid color” – whether the photo has vivid color, not necessarily harmonious color;

**ZH** 9.“vivid color”（色彩鲜艳）——照片色彩是否鲜艳，不要求色彩和谐；

**EN** 10. “repetition” – whether the image has repetitive patterns;

**ZH** 10.“repetition”（重复）——图像是否存在重复图案；

**EN** 11. “symmetry” – whether the photo has symmetric patterns.

**ZH** 11.“symmetry”（对称）——照片是否具有对称图案。

**EN** These attributes span traditional photographic principals of color, lighting, focus and composition, and provide a natural vocabulary for use in applications, such as auto photo editing and image retrieval. To visualize images containing these attributes, please refer to the attached our AMT instruction in the end of this supplementary material. The instruction is used for teaching raters to pass the qualification test.

**ZH** 这些属性覆盖了色彩、光照、对焦与构图等传统摄影要领，并为自动照片编辑、图像检索等应用提供了自然的描述词汇。若想查看包含这些属性的图像，请参阅本补充材料末尾所附的 AMT 说明，该说明用于培训评分者通过资格测试。

**EN** Data Collection By Amazon Mechanical Turk

**ZH** 基于 Amazon Mechanical Turk 的数据采集

<!-- [原子块 · object]  -->

**EN** Figure 7: Long tail distribution of AMT workers: number of rated images vs. each worker.

**ZH** 图 7：AMT 工作者的长尾分布：每位工作者标注的图像数量。

**EN** To collect a varied set of photographic images, we download images from Flickr website44 4 www.flickr.com, which carry a Creative Commons license. We manually curate the dataset to remove non-photographic images (e.g. cartoons, drawings, paintings, ads images, adult-content images, etc.). We have multiple workers independently annotate each image with an overall aesthetic score and the eleven meaningful attributes using Amazon Mechanical Turk55 5 www.mturk.com.

**ZH** 为收集种类丰富的摄影图像，我们从 Flickr 网站44 4 www.flickr.com 下载带有 Creative Commons 许可的图像，并人工筛除漫画、素描、油画、广告图、成人内容等非摄影图像。随后，我们请多位工作者通过 Amazon Mechanical Turk55 5 www.mturk.com 独立地为每幅图像标注一个总体美学分数与上述十一项有意义的属性。

<!-- [原子块 · img]  -->

**EN** Figure 8: Interface of data collection by AMT.

**ZH** 图 8：通过 AMT 采集数据所用的界面。

**EN** For each attribute, we allow workers to click “positive” if this attribute conveyed by the image can enhance the image aesthetic quality, or “negative” if the attribute degrades image aesthetics. The default is “null”, meaning the attribute does not effect image aesthetics. For example, “positive” vivid color means the vividness of the color presented in the image has a positive effect on the image aesthetics; while the counterpart “negative” means, for example, there is dull color composition. Note that we do not let workers tag negative repetition and symmetry, as for the two attributes negative values do not make sense.

**ZH** 对于每个属性，若图像所呈现的该属性能够提升图像美学质量，工作者可勾选“positive”；若该属性损害图像美学，则勾选“negative”。默认值为“null”，表示该属性对图像美学没有影响。例如，“positive”的 vivid color 表示图像所呈现色彩的鲜艳程度对图像美学有正向作用；与之相对，“negative”则表示色彩构成沉闷等情形。需要说明的是，我们不让工作者标注 repetition 与 symmetry 的负值，因为对这两项属性而言负值没有意义。

**EN** We launch a task consisting of 10,000 images on AMT, and let five different workers label each image. All the workers must read instructions and pass a qualification exam before they become qualified to do our task. The images are split into batches, each of which contains ten images. Therefore, raters will annotate different numbers of batches. There are 190 workers in total doing our AMT task, and the workers follow long tail distribution, as demonstrated by Figure 7. Figure 8 shows the interface of our AMT task.

**ZH** 我们在 AMT 上发布了一个包含 10,000 幅图像的任务，并请五位不同的工作者标注每幅图像。所有工作者必须先阅读说明并通过资格考试，才有资格执行我们的任务。图像被划分为批次，每批包含十幅图像，因此评分者标注的批次数各不相同。共有 190 位工作者参与了该 AMT 任务，其分布呈长尾形态，如图 7 所示。图 8 展示了该 AMT 任务的界面。

**EN** Note that even though judging these attributes is also subjective, the averaged scores of these attributes indeed reflect good information if we visualize the ranked images w.r.t averaged scores. Therefore, we use the averaged score as the ground truth, for both aesthetic score and attributes. Furthermore, we normalize aesthetic score to the range of ⟦SLOT_98⟧, as shown by Figure 9, from which we can see that ratings are well fit by a Gaussian distribution. This observation is consistent with that reported in [23]. In our experiments we normalize the attributes’ scores to the range of ⟦SLOT_99⟧. The images are split into testing set (1,000 images), validation set (500 images) and training set (the rest).

**ZH** 需要说明的是，尽管判断这些属性同样带有主观性，但当我们按平均分数对图像排序并可视化时，属性的平均分数确实反映了有意义的信息。因此，无论对美学分数还是属性，我们都采用平均分数作为真实值。此外，我们将美学分数归一化到 ⟦SLOT_98⟧ 区间，如图 9 所示，从中可以看到评分很好地服从高斯分布，这一观察与 [23] 的报告一致。在实验中，我们将属性分数归一化到 ⟦SLOT_99⟧ 区间。图像被划分为测试集（1,000 幅）、验证集（500 幅）与训练集（其余部分）。

<!-- [原子块 · object]  -->

**EN** Figure 9: The distribution of rated image aesthetic scores by the AMT workers follows a Gaussian distribution.

**ZH** 图 9：AMT 工作者给出的图像美学评分分布服从高斯分布。

**EN** Appendix: Statistics of AADB

**ZH** 附录：AADB 统计信息

<!-- [原子块 · object]  -->

**EN** Figure 10: The distributions of all the eleven attributes. Note that for attributes repetition and symmetry, we do not let AMT workers annotate negative labels, as these attributes are of neutral meaning. Instead, we only allow them to point out whether there exist repetition or symmetry. To solve the data imbalance problem in training attribute classifiers, we adopt some data augmentation tricks to sample more rare cases.

**ZH** 图 10：全部十一项属性的分布。需要说明的是，对于 repetition 与 symmetry 两项属性，我们不要求 AMT 工作者标注负标签，因为这两项属性属于中性含义，只要求他们指出是否存在重复或对称。为解决训练属性分类器时的数据不平衡问题，我们采用了一些数据增强技巧来采样更多罕见样本。

**EN** The final AADB dataset contains 10,000 images in total, each of which has aesthetic quality ratings and attribute assignments provided by five different individual raters. Therefore, we have rating scores for attributes as well, which is different from AVA dataset [23] in which images only have binary labels for the attributes. Figure 10 shows the distribution of each attributes.

**ZH** 最终的 AADB 数据集共包含 10,000 幅图像，每幅图像的美学质量评分与属性标注均由五位不同的评分者给出。因此，我们也得到了属性的评分分数，这与 AVA 数据集 [23] 中图像仅含属性二值标签的做法不同。图 10 给出了各项属性的分布。

**EN** Appendix: Consistency Analysis

**ZH** 附录：一致性分析

<!-- [原子块 · object]  -->

**EN** Figure 11: Permutation test on Kendall’s ⟦SLOT_100⟧: ⟦SLOT_101⟧ vs. ⟦SLOT_102⟧.

**ZH** 图 11：关于 Kendall ⟦SLOT_100⟧ 的置换检验：⟦SLOT_101⟧ 对 ⟦SLOT_102⟧。

<!-- [原子块 · object]  -->

**EN** Figure 12: Permutation test on Kendall’s ⟦SLOT_103⟧: ⟦SLOT_104⟧ vs. ⟦SLOT_105⟧.

**ZH** 图 12：关于 Kendall ⟦SLOT_103⟧ 的置换检验：⟦SLOT_104⟧ 对 ⟦SLOT_105⟧。

**EN** As there are five individuals rating each image, one may argue that the annotations are not reliable for this subjective task. Therefore, we carry out consistency analysis. We use both Kendall’s ⟦SLOT_106⟧ and Spearman’s ⟦SLOT_107⟧ for the analysis. Kendall’s ⟦SLOT_108⟧ directly measures the agreement among multiple raters, and accounts for tied ranks. It ranges from 0 (no agreement) to 1 (complete agreement). Spearman’s ⟦SLOT_109⟧ is used in our paper that compares a pair of ranking lists.

**ZH** 由于每幅图像由五位个体评分，有人可能会质疑：对这样一个主观任务，标注是否可靠。为此，我们使用 Kendall ⟦SLOT_106⟧ 与斯皮尔曼 ⟦SLOT_107⟧ 两种指标做一致性分析。Kendall ⟦SLOT_108⟧ 直接度量多位评分者之间的一致程度，并考虑并列秩，取值范围为 0（完全不一致）到 1（完全一致）。斯皮尔曼 ⟦SLOT_109⟧ 则在本文中用于比较两个排序列表。

**EN** First, we conduct a permutation test over global ⟦SLOT_110⟧ to obtain the distribution of ⟦SLOT_111⟧ under the null hypothesis. We plot the curve of ⟦SLOT_112⟧: ⟦SLOT_113⟧ vs. ⟦SLOT_114⟧ in Fig. 11 and ⟦SLOT_115⟧ vs. ⟦SLOT_116⟧ in Fig 12. We can easily see that the empirical Kendall’s ⟦SLOT_117⟧ on our AADB dataest is statistically significant.

**ZH** 首先，我们对全局 ⟦SLOT_110⟧ 做置换检验，以获得零假设下 ⟦SLOT_111⟧ 的分布。我们在图 11 中绘制了 ⟦SLOT_112⟧ 的曲线：⟦SLOT_113⟧ 对 ⟦SLOT_114⟧；在图 12 中绘制了 ⟦SLOT_115⟧ 对 ⟦SLOT_116⟧。可以清楚地看到，AADB 数据集上的经验 Kendall ⟦SLOT_117⟧ 具有统计显著性。

**EN** Then, for each batch, we can also evaluate the annotation consistency with Kendall’s ⟦SLOT_118⟧, which directly calculates the agreement among multiple raters, and accounts for tied ranks. As there are ten images and only five possible ratings for each image, tied ranks may happen in a batch. The average Kendall’s ⟦SLOT_119⟧ over all batches is ⟦SLOT_120⟧. This shows significant consistency of the batches annotated by the AMT workers. To test the statistical significance of Kendall’s ⟦SLOT_121⟧ at batch level, we adopt the Benjamini-Hochberg procedure to control the false discovery rate (FDR) for multiple comparisons [1]. At level ⟦SLOT_122⟧, ⟦SLOT_123⟧ batches from ⟦SLOT_124⟧ in total have significant agreement. This shows that almost all the batches annotated by AMT workers have consistent labels and are reliable for scientific use.

**ZH** 其次，对每个批次，我们也可以用 Kendall ⟦SLOT_118⟧ 评估标注一致性，它直接计算多位评分者之间的一致程度并考虑并列秩。由于每批有十幅图像而每幅图像只有五种可能的评分，批次内可能出现并列秩。所有批次上 Kendall ⟦SLOT_119⟧ 的平均值为 ⟦SLOT_120⟧，表明 AMT 工作者标注的批次具有显著一致性。为检验批次层面 Kendall ⟦SLOT_121⟧ 的统计显著性，我们采用 Benjamini-Hochberg 程序控制多重比较下的错误发现率（FDR）[1]。在水平 ⟦SLOT_122⟧ 下，⟦SLOT_123⟧ 个批次具有显著一致性（全部批次共 ⟦SLOT_124⟧ 个）。这表明 AMT 工作者标注的几乎所有批次标签一致，可供科研使用。

**EN** Furthermore, we can also test the statistical significance w.r.t Spearman’s ⟦SLOT_125⟧ at batch levels using Benjamini-Hochberg procedure. The ⟦SLOT_126⟧-values of pairwise ranks of raters in a batch can be computed by the exact permutation distributions. We average the pairwise ⟦SLOT_127⟧-values as the ⟦SLOT_128⟧-value for the batch. With the FDR level ⟦SLOT_129⟧, we find that ⟦SLOT_130⟧ batches have significant agreement. This further demonstrates the reliability of the annotations.

**ZH** 此外，我们也可以用 Benjamini-Hochberg 程序检验批次层面斯皮尔曼 ⟦SLOT_125⟧ 的统计显著性。批次内评分者两两排序的 ⟦SLOT_126⟧ 值可通过精确置换分布计算得到，我们将两两 ⟦SLOT_127⟧ 值取平均作为该批次的 ⟦SLOT_128⟧ 值。在 FDR 水平 ⟦SLOT_129⟧ 下，我们发现 ⟦SLOT_130⟧ 个批次具有显著一致性，进一步证明了标注的可靠性。

**EN** Appendix: Analysis of Content-Aware Model

**ZH** 附录：内容感知模型的分析

**EN** Table 8: Analysis of content-aware model on AVA dataset.

**ZH** 表 8：AVA 数据集上内容感知模型的分析。

<!-- [原子块 · table] method concatGT concatPred avg. weightedSum weightedSum _ \_ FT Spearman’s ρ \rho 0.5367 0.5327 0.5336 0.5335 0.5426 accuracy( % \% ) 75.41 75.33 75.39 75.33 75.57 -->

**EN** To show the effectiveness of utilizing content information as a weights for output scores by different content-specific aesthetics rating branches, we report the performance on AVA dataset of different methods in Table 8. Our first method is named “concatGT”, which means we use the ground-truth content label of an image, and get the estimated aesthetic score by the content-specific branch; then we put all the estimated scores together to get the global Spearman’s ⟦SLOT_131⟧ and classification accuracy. In method “concatPred”, we use the predicted content label to choose which category-specific branch to use for estimating aesthetic score, then use the same procedure as in “concatGT”. In method “avg.”, we use all the content-specific aesthetics rating branches to get multiple scores, and average them to a single score as the final estimation. In “weightedSum”, we use the classification confidence score output by softmax of the content classification branch to do weighted sum for the final score. In “weightedSum⟦SLOT_132⟧FT”, we fine-tune the whole network but freezing the classification branch, and use the fine-tuned model to do weighted sum on the scores for the final aesthetics rating. From this table, we can clearly observe that “weightedSum⟦SLOT_133⟧FT” performs the best, which is the one described in the paper.

**ZH** 为证明把内容信息用作各内容特定美学评分分支输出分数的权重是有效的，我们在表 8 中报告了不同方法在 AVA 数据集上的表现。第一种方法称为“concatGT”，即使用图像的内容真实标签，由内容特定分支得到估计的美学分数，再把所有估计分数汇总计算全局斯皮尔曼 ⟦SLOT_131⟧ 与分类准确率。“concatPred”方法则用预测的内容标签来选择使用哪个类别特定分支估计美学分数，其余步骤与“concatGT”相同。“avg.”方法用所有内容特定美学评分分支得到多个分数，取平均作为最终估计。“weightedSum”方法用内容分类分支 softmax 输出的分类置信度分数对最终分数做加权求和。“weightedSum⟦SLOT_132⟧FT”方法微调整个网络但冻结分类分支，并用微调后的模型对分数做加权求和以得到最终美学评分。由该表可以清楚地看到，“weightedSum⟦SLOT_133⟧FT”表现最好，也正是本文所描述的方法。

**EN** Appendix: Demonstration of Our Model

**ZH** 附录：模型效果展示

**EN** In this section, we test our model on personal photos qualitatively, in which these photos are downloaded online and not part of our AADB dataset. As our model can predicts all the eleven attributes, we show the attributes’ estimation as well as the rated aesthetic scores. For better visualization, we simple set thresholds as ⟦SLOT_134⟧ and ⟦SLOT_135⟧ to characterize “negative”, “null” and “positive” attributes, respectively. Figure 13 – 15 show the results for images with high, low and medium estimated scores. We can see, in general, our model reasonably captures attributes and gives aesthetic scores.

**ZH** 本节我们在个人照片上对模型做定性测试，这些照片下载自网络，不属于 AADB 数据集。由于模型可以预测全部十一项属性，我们同时展示属性的估计结果与美学评分。为便于可视化，我们简单地设定阈值 ⟦SLOT_134⟧ 与 ⟦SLOT_135⟧，分别刻画“negative”“null”与“positive”属性。图 13 至图 15 给出了估计分数为高、低、中三档的图像结果。可以看到，总体而言模型能够合理地捕捉属性并给出美学分数。

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

**EN** Figure 13: Some images outside our database with high estimated scores.

**ZH** 图 13：数据库外估计分数较高的部分图像。

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

**EN** Figure 14: Some images outside our database with low estimated scores.

**ZH** 图 14：数据库外估计分数较低的部分图像。

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

**EN** Figure 15: Some images outside our database with medium estimated scores.

**ZH** 图 15：数据库外估计分数居中的部分图像。
