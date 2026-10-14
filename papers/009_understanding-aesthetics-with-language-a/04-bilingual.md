# 以语言理解美学：面向美学评估的摄影评论数据集

> 原标题：Understanding Aesthetics with Language: A Photo Critique Dataset for Aesthetic Assessment
> 作者：Daniel Vera Nieto, Luigi Celona, Clara Fernandez-Labrador · arXiv:2206.08614 · 2022-06-17

<!-- [原子块 · verbatim] Understanding Aesthetics with Language: A Photo Critique Dataset for Aesthetic Assessment -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] Computational inference of aesthetics is an ill-defined task due to its subjective nature. Many datasets have been proposed to tackle the problem by providing pairs of images and aesthetic scores base -->

<!-- [原子块 · table]  -->

**EN** 1 Introduction

**ZH** 1 引言

**EN** Automated Image Aesthetic Assessment (IAA) is a widely discussed topic in the computer vision community and is receiving an increasing attention due to the explosive growth of digital photography. The literature reports mainly on predicting aesthetic preference in close agreement with human judgement. In particular, most studies deal with IAA in terms of high vs. low aesthetic quality [25], regression of the aesthetic score [14], and prediction of the distribution of the aesthetic ratings [37]. Various datasets were collected to contribute developing and evaluating the previous studies. These datasets consist of images annotated with aesthetic scores. However, summarizing the aesthetic judgment in a single value limits the representation of visual aesthetics. First, aesthetic scores are highly dependent on the voting procedure (i.e., voting scale, number of stimuli, questions and adjectives in the voting scale). Second, it has been shown that they might provide a variable or even negative impact on the prediction of human behavior and thus on the success of social content [33]. Third, aesthetic scores do not provide any interpretability of why an image is aesthetically pleasing or not. Thus, it makes sense to annotate images with richer high-level aesthetic attributes [20] or aesthetic criticism captions. Many image-sharing sites, e.g., Flickr, Photo.net, and Instagram, support user comments on images, allowing rating explanations. User comments usually introduce rationale about how and why users evaluate the aesthetics of an image. Comments such as “good composition”, “vivid colors”, or “a fine pose” are more informative than ratings for expressing pleasing photographic aspects. Similarly, comments such as “too dark” and “blurry” explain why low ratings occur.

**ZH** 自动图像美学评估（Image Aesthetic Assessment, IAA）是计算机视觉领域广受关注的课题，随着数字摄影的爆发式增长正获得越来越多关注。已有文献主要研究如何使美学偏好的预测与人类判断高度一致。具体而言，多数研究从三个角度处理 IAA：高/低美学质量的二分类 [25]、美学分数回归 [14]，以及美学评分分布的预测 [37]。为支撑上述研究的开发与评估，研究者采集了多个数据集，其中的图像均带有美学分数标注。然而，把美学判断压缩为单一数值会限制视觉美学的表达能力。其一，美学分数高度依赖投票流程（即投票量表、刺激样本数量、量表中的问题与形容词）。其二，已有研究表明，这类分数对人类行为预测乃至社交内容传播效果的影响可能是波动的，甚至是负面的 [33]。其三，美学分数无法解释一张图像为何悦目或不悦目。因此，用更丰富的高层美学属性 [20] 或美学评论文本来标注图像更为合理。Flickr、Photo.net、Instagram 等众多图像分享平台都支持用户对图像发表评论，从而可以对评分给出解释。用户评论通常会交代其评价图像美学的方式与原因。诸如“good composition”（构图出色）、“vivid colors”（色彩鲜艳）或“a fine pose”（姿态优美）的评论，比单纯的评分更能传达摄影作品令人愉悦之处；同样，“too dark”（太暗）、“blurry”（模糊）这类评论则解释了低分出现的原因。

**EN** On the basis of previous considerations, our first contribution is the Reddit Photo Critique Dataset RPCD, a collection of high resolution images associated with photo critiques (i.e., 74K images and 220K comments). The dataset has been obtained from a Reddit community22 2 www.reddit.com of photography amateurs whose purpose is to provide feedback to help amateurs and professional photographers improve. Figure 1 shows some samples from our RPCD. The dataset presented in this work differs in many ways from existing photo critic datasets. First, the images are mostly FullHD as they were captured with recent photo sensors and imaging systems. Secondly, the proposed dataset is among the largest in terms of the number of images-comments. Third, the comments of our dataset are on average longer and more informative (basing on the score proposed in [10]) than those of the previous datasets.

**ZH** 基于上述考量，我们的第一个贡献是 Reddit 摄影评论数据集（Reddit Photo Critique Dataset, RPCD），它是一组配有摄影评论的高分辨率图像集合（即 74K 图像与 220K 条评论）。该数据集采集自 Reddit 上一个摄影爱好者社区22 2 www.reddit.com，社区成员的目标是通过反馈帮助业余与专业摄影师提升水平。图 1 展示了 RPCD 的部分样本。本文提出的数据集在诸多方面区别于已有的摄影评论数据集：首先，图像大多为 FullHD 分辨率，因为它们由较新的图像传感器与成像系统拍摄；其次，就图像—评论的规模而言，本数据集位居前列；第三，按 [10] 提出的评分衡量，本数据集评论的平均长度与信息量均高于以往数据集。

**EN** In the literature, IAA models are trained on datasets in which each image is associated with a rating. However, the problem of how to obtain a rating for IAA without requiring human intervention given a dataset with image-comment pairs is not addressed. The degree of emotion and valence of critique comments is an excellent indicator of the success of contents on social media [33]. Therefore, together with the dataset, we present a new solution to rank images by exploiting the polarity of criticism as an indicator of aesthetic judgments. To the best of our knowledge, this is the first attempt to leverage image critiques to define a score for IAA.

**ZH** 已有文献中的 IAA 模型都在“每张图像对应一个评分”的数据集上训练。然而，对于只有图像—评论配对的数据集，如何在不引入人工干预的情况下得到 IAA 所需的评分，这一问题尚未被解决。评论所包含的情绪强度与效价是社交内容传播效果的良好指标 [33]。因此，在提出数据集的同时，我们还给出一种新的图像排序方案：利用评论的极性作为美学判断的指标。据我们所知，这是首次尝试借助图像评论来定义 IAA 分数。

**EN** Finally, we design a framework to evaluate different methods on the proposed dataset and other aesthetic critique datasets in the literature on the image aesthetic assessment and aesthetic image captioning tasks.

**ZH** 此外，我们设计了一套评测框架，用于在本文数据集及文献中其他美学评论数据集上比较不同方法在图像美学评估与美学图像描述两个任务上的表现。

**EN** We find that: (i) the aesthetic scores and the proposed sentiment scores are positively correlated on two photo critique datasets annotated with both comments and scores; (ii) Vision Transformer (ViT) surpasses state-of-the-art methods for image aesthetic assessment; (iii) learning aesthetics-aware features produces a significant increase in performance over using semantic features. This behavior also occurs for models with the same architecture but trained for different purposes.

**ZH** 我们发现：（i）在两个同时标注了评论与分数的摄影评论数据集上，美学分数与我们提出的情感分数呈正相关；（ii）Vision Transformer（ViT）在图像美学评估上超越了当前最优方法；（iii）学习美学感知特征相比使用语义特征能带来显著的性能提升；这一规律在架构相同但训练目标不同的模型上同样成立。

**EN** 2 Related Work

**ZH** 2 相关工作

**EN** In this section we briefly analyze the main datasets and methods for the two tasks of image aesthetic assessment and aesthetic critique captioning. We refer the reader to [42] for a comprehensive review on computational image aesthetics.

**ZH** 本节简要梳理图像美学评估与美学评论生成两项任务的主要数据集与方法。关于计算图像美学的系统性综述，可参阅 [42]。

**EN** Image Aesthetic Assessment.

**ZH** 图像美学评估。

**EN** For the design and evaluation of Image Aesthetic Assessment (IAA) methods, the construction of the aesthetic image evaluation benchmark dataset has become the fundamental prerequisite for the research. Many datasets were collected in which subjective aesthetic quality scores were acquired for each image. The acquisition of subjective scores can be realized through manually scoring experiments in the lab [25], online scoring on image sharing website [20, 28], and crowdsourcing evaluation [36]. Methods that exploit the previous datasets for aesthetic assessment can be divided into model-based [7, 27, 43] and data-driven [4, 14, 24, 37]. While model-based methods rely on hand-crafted features to model aspects such as the Rule of Thirds, depth of field, colour harmony, etc., the data-driven methods usually train CNNs on large-scale datasets to predict an overall aesthetic rating.

**ZH** 在图像美学评估（IAA）方法的设计与评估中，构建美学图像评测基准数据集已成为研究的基础前提。研究者采集了多个数据集，为每张图像获取主观美学质量分数。主观分数的获取途径包括实验室人工评分实验 [25]、图像分享网站上的在线评分 [20, 28]，以及众包评估 [36]。利用上述数据集进行美学评估的方法可分为基于模型的方法 [7, 27, 43] 与数据驱动方法 [4, 14, 24, 37]。基于模型的方法依靠手工设计特征来刻画三分法、景深、色彩和谐等要素，而数据驱动方法通常在大规模数据集上训练卷积神经网络以预测整体美学评分。

**EN** Aesthetic Critique Captioning.

**ZH** 美学评论生成。

**EN** The first work on Aesthetic Critique Captioning, also known as Aesthetic Image Captioning (AIC), presents the so called Photo Critique Captioning Dataset (PCCD) based on a professional photo critique website33 3 https://gurushots.com/ and a method for predicting aspect-centric captions [5]. The other AIC datasets in the literature are obtained by crawling images together with their comments from an on-line community of photography amateurs44 4 https://www.dpchallenge.com/. AVA-Comments [45] extends AVA to include all user comments for images, while AVA-Captions [10] filters original AVA photo comments to keep only the most useful. Finally, DPC-Captions [17] contains 154,384 images and 2,427,483 comments. Each comment is automatically annotated with one of the 5 aesthetic attributes of the PCCD through aesthetic knowledge transfer. Few AIC methods are present in the literature for predicting aesthetic comments [10, 41], aspect-centric aesthetic captions [5], or simultaneously the aesthetic rate and an aesthetic caption [38].

**ZH** 美学评论生成（Aesthetic Critique Captioning），亦称美学图像描述（Aesthetic Image Captioning, AIC），其首项工作基于一家专业摄影评论网站33 3 https://gurushots.com/ 提出了 Photo Critique Captioning Dataset（PCCD），并给出了一种面向维度的描述生成方法 [5]。文献中其他 AIC 数据集则是从一个摄影爱好者在线社区44 4 https://www.dpchallenge.com/ 爬取图像及其评论得到的。AVA-Comments [45] 在 AVA 基础上补充了图像的所有用户评论，AVA-Captions [10] 则对 AVA 原始评论进行筛选，只保留最有价值的部分。DPC-Captions [17] 包含 154,384 张图像与 2,427,483 条评论，每条评论通过美学知识迁移自动标注为 PCCD 的 5 类美学属性之一。文献中针对美学评论预测的方法较少，主要面向美学评论生成 [10, 41]、面向维度的美学描述生成 [5]，或同时预测美学评分与美学描述 [38]。

**EN** 3 Background and Theory

**ZH** 3 背景与理论

**EN** In this section we provide a formal definition for the classical image aesthetic assessment problem and describe our novel formulation of the problem.

**ZH** 本节给出经典图像美学评估问题的形式化定义，并描述我们提出的新问题形式。

**EN** Notations.

**ZH** 符号约定。

**EN** We represent sets and matrices with special Latin characters (e.g., ⟦SLOT_0⟧) or bold Latin characters (e.g., ⟦SLOT_1⟧). Lower or uppercase normal fonts, e.g., ⟦SLOT_2⟧ denote scalars. Lowercase bold Latin letters represent vectors as in ⟦SLOT_3⟧. We use lowercase Latin letters to represent indices (e.g., ⟦SLOT_4⟧).

**ZH** 我们用特殊拉丁字符（如 ⟦SLOT_0⟧）或粗体拉丁字符（如 ⟦SLOT_1⟧）表示集合与矩阵。正常字体的小写或大写字母（如 ⟦SLOT_2⟧）表示标量。小写粗体拉丁字母表示向量，如 ⟦SLOT_3⟧。我们用小写拉丁字母表示下标（如 ⟦SLOT_4⟧）。

**EN** 3.1 Image Aesthetic Assessment

**ZH** 3.1 图像美学评估

**EN** Image Aesthetic Assessment (IAA) methods aim at computationally judging the aesthetic value of images based on human ratings and photographic principles. These methods map an input image ⟦SLOT_5⟧ to an aesthetic score ⟦SLOT_6⟧ and can be divided into binary classification methods which predict a single binary score ⟦SLOT_7⟧, and regression methods which predict a single real score ⟦SLOT_8⟧ or a probability distribution of scores ⟦SLOT_9⟧. Classification methods are used to distinguish “good” from “bad” images whereas regression methods are preferred to rank collections of images. These methods typically rely on public datasets [20, 25, 28] that contain ⟦SLOT_10⟧ pairs of images and aesthetic scores such that ⟦SLOT_11⟧, where the ground truth score per image is computed as the average rating given by ⟦SLOT_12⟧ human raters:

**ZH** 图像美学评估（IAA）方法旨在基于人类评分与摄影法则，以计算方式评判图像的美学价值。这类方法将输入图像 ⟦SLOT_5⟧ 映射为美学分数 ⟦SLOT_6⟧，可分为预测单个二值分数 ⟦SLOT_7⟧ 的二分类方法，以及预测单个实数分数 ⟦SLOT_8⟧ 或分数概率分布 ⟦SLOT_9⟧ 的回归方法。二分类方法用于区分“好”图与“坏”图，回归方法则更适于对图像集合排序。这些方法通常依赖 [20, 25, 28] 等公开数据集，其中包含 ⟦SLOT_10⟧ 组图像—美学分数配对，满足 ⟦SLOT_11⟧，每张图像的真值分数由 ⟦SLOT_12⟧ 位评分者给出的平均评分计算得到：

<!-- [原子块 · table] s i = 1 K ​ ∑ k = 0 K s k , s_{i}=\frac{1}{K}\sum_{k=0}^{K}s_{k}, (1) -->

**EN** The scores are further thresholded by the mid-point of the rating scale for the classification task. However, asking people to evaluate the aesthetic value of an image with a single global score is very challenging and can be extremely biased by the content of the images. Additionally, these scores alone do not provide any explicit information about the reasons behind the voting.

**ZH** 在分类任务中，分数会进一步按评分量表的中位点进行阈值化。然而，要求人们用单一全局分数评价图像的美学价值非常困难，且极易受图像内容影响而产生偏差。此外，这些分数本身无法显式说明投票背后的原因。

**EN** 3.2 Aesthetic Critiques

**ZH** 3.2 美学评论

**EN** Recent datasets [5, 10, 17] extend the IAA problem including captions related to photo aesthetics and/or photography skills. These datasets contain ⟦SLOT_13⟧ images each described by ⟦SLOT_14⟧ aesthetic critiques ⟦SLOT_15⟧ such that ⟦SLOT_16⟧. Common critiqued aesthetic aspects are composition, subject of photo, use of camera or color. In this context, novel algorithms have been developed to generate aesthetic-oriented critiques for images. Therefore, these methods map an input image ⟦SLOT_17⟧ to an aesthetic critique ⟦SLOT_18⟧. While photo critiques give explicit feedback about why images are aesthetically pleasing or not, it has not been explored yet how to exploit such critiques for classification or image ranking, which is the ultimate goal of IAA. Furthermore, critique generative models present an additional challenge with respect to conventional captioning models due to the subjective nature of problem at hand. For this reason, many generated critiques tend to express critic’s preference (e.g., “I like the colors” and “nice photo”) rather than providing a detailed opinion or critique of the image aesthetics.

**ZH** 近期数据集 [5, 10, 17] 通过引入与摄影美学和/或摄影技法相关的描述，拓展了 IAA 问题。这些数据集包含 ⟦SLOT_13⟧ 张图像，每张图像由 ⟦SLOT_14⟧ 条美学评论 ⟦SLOT_15⟧ 描述，满足 ⟦SLOT_16⟧。常见的被评论美学维度包括构图、拍摄主体、相机运用与色彩。在此背景下，研究者已开发出若干面向美学的评论生成算法，这类方法将输入图像 ⟦SLOT_17⟧ 映射为美学评论 ⟦SLOT_18⟧。虽然摄影评论能够明确说明图像为何悦目或不悦目，但如何利用这些评论完成分类或图像排序——即 IAA 的最终目标——尚未被探索。此外，由于问题本身具有主观性，评论生成模型相比常规描述生成模型面临额外挑战。正因如此，许多生成的评论倾向于表达评论者的个人偏好（如“I like the colors”、“nice photo”），而非对图像美学给出细致见解或评论。

**EN** 3.3 Leveraging Aesthetic Critiques for Image Aesthetic Assessment

**ZH** 3.3 利用美学评论完成图像美学评估

**EN** Ranking images from aesthetic critiques comes as a natural extension of the problem. In this paper, we are interested in leveraging the interpretability given by image captions to automatically discover the aesthetic score that truly defines the images beauty. Given an input image ⟦SLOT_19⟧ and ⟦SLOT_20⟧ aesthetic critiques associated to the image, we propose to use sentiment polarity analysis on each critique ⟦SLOT_21⟧ to define the aesthetic score ⟦SLOT_22⟧ of the image. Sentiment polarity for a comment defines the orientation of the expressed sentiment, i.e., it determines if the text expresses the negative, neutral or positive sentiment of the user about the entity in consideration. A sentiment polarity model maps a given critique ⟦SLOT_23⟧ to a vector ⟦SLOT_24⟧ which can be interpreted as the probabilities of the given critique to express a negative, neutral or positive feeling with respect to the aesthetic value of the image. We define the sentiment score ⟦SLOT_25⟧ of a critique as follows:

**ZH** 由美学评论出发对图像排序，是这一问题的自然延伸。本文希望借助图像描述所提供的可解释性，自动发现真正定义图像美感的分数。给定输入图像 ⟦SLOT_19⟧ 及其关联的 ⟦SLOT_20⟧ 条美学评论，我们提出对每条评论 ⟦SLOT_21⟧ 做情感极性分析，由此定义该图像的美学分数 ⟦SLOT_22⟧。评论的情感极性刻画了所表达情绪的取向，即判定文本针对所考量对象表达的是负面、中性还是正面情绪。情感极性模型将给定评论 ⟦SLOT_23⟧ 映射为向量 ⟦SLOT_24⟧，可理解为该评论针对图像美学价值表达负面、中性或正面感受的概率。我们将一条评论的情感分数 ⟦SLOT_25⟧ 定义如下：

<!-- [原子块 · table] s k = ∑ l = 0 2 p l ​ l 2 , s_{k}=\frac{\sum_{l=0}^{2}p_{l}l}{2}, (2) -->

**EN** Where ⟦SLOT_26⟧ is the label for negative, neutral or positive sentiment respectively and ⟦SLOT_27⟧ the probability associated to the label. The sentiment scores for all the critiques of an image are then averaged to obtain an overall sentiment score ⟦SLOT_28⟧ as in Eq. 1. The proposed dataset can then be defined such that ⟦SLOT_29⟧.

**ZH** 其中 ⟦SLOT_26⟧ 分别为负面、中性、正面情感的标签，⟦SLOT_27⟧ 为对应标签的概率。随后，将一张图像所有评论的情感分数取平均，得到如式 1 所示的整体情感分数 ⟦SLOT_28⟧。所提出的数据集可由此定义为 ⟦SLOT_29⟧。

**EN** To the best of our knowledge, this is the first attempt to estimate the aesthetic quality of visuals directly from critiques rather than from human ratings. Our proposal is significant for several reasons. Critiques are an important indicator of human judgment, generally more valuable than simple ratings as they provide an explanation of why a visual is aesthetically pleasing or not [33]. However, critiques are unstructured data that do not directly indicate the level of aesthetic appreciation. Therefore, our proposed score is a way to obtain a compact and quantifiable representation of the level of appreciation of an image inferred from the critiques. Second, thanks to our proposal, two related aesthetic tasks are linked. Indeed, the datasets created for Aesthetic Image Captioning (AIC) can be applied to the design of models for both AIC and Image Aesthetic Assessment (IAA). The integration of the two tasks is useful because the critiques guarantee the explainability of a score; on the other hand, the ratings might allow the prediction of valence-sensitive critiques. Finally, our proposal consists of a weakly-supervised labeling approach which has the advantage of requiring human intervention solely to provide comments on the image. Existing datasets such as PCCD and AVA demanded intensive human effort to provide ratings and comments.

**ZH** 据我们所知，这是首次尝试直接从评论而非人类评分估计视觉内容的美学质量。我们的方案意义显著，原因如下。评论是人类判断的重要指征，由于能解释视觉内容为何悦目或不悦目，其价值通常高于简单评分 [33]。然而，评论属于非结构化数据，并不直接指示美学欣赏的程度。因此，我们提出的分数提供了一条途径，可将由评论推断出的图像欣赏程度压缩为紧凑、可量化的表示。其次，该方案把两项相关的美学任务联系起来：为美学图像描述（AIC）构建的数据集，可同时用于设计 AIC 与图像美学评估（IAA）模型。二者的结合是有益的——评论保证分数的可解释性，而评分则可能支持对效价敏感的评论生成。最后，本方案属于弱监督标注方法，其优势在于只需人工提供图像评论；PCCD、AVA 等既有数据集则需要大量人力同时提供评分与评论。

**EN** 4 RPCD: Reddit Photo Critique Dataset

**ZH** 4 RPCD：Reddit 摄影评论数据集

**EN** The Reddit Photo Critique Dataset (RPCD) is a collection of high-resolution images associated with photo critiques obtained by the Reddit communities. We first give a description of the dataset collection and statistics in Section 4.1. Section 4.2 details how we automatically rank the images following the criticism-based approach described in Section 3.3. Finally, in Section 4.3, we thoroughly analyze the images and comments present in our dataset.

**ZH** Reddit 摄影评论数据集（RPCD）是一组由 Reddit 社区获取、配有摄影评论的高分辨率图像集合。4.1 节先介绍数据集的采集方式与统计信息，4.2 节详述如何按照 3.3 节基于评论的方法对图像自动排序，最后 4.3 节对数据集中的图像与评论做细致分析。

**EN** 4.1 Dataset Collection and Statistics

**ZH** 4.1 数据集采集与统计

**EN** Collection Modality.

**ZH** 采集方式。

**EN** For the collection of the RPCD dataset, we identified Reddit communities used by amateur and professional photographers to upload their images or to discuss about photography. In particular, the following six communities (known as subreddits) were identified: /r/AskPhotography, /r/photocritique, /r/photographs, /r/portraits, /r/postprocessing, /r/shittyHDR. After a careful review of the different subreddits, we selected the /r/photocritique subreddit with a total of 168,222 posts and 731,772 comments. The decision was made based on the rules of the community55 5 https://www.reddit.com/r/photocritique/ which makes its content specially suitable for the task at hand. Namely, it mostly contains posts with amateur and professional images that get feedback from other photographers and hobbyists. We downloaded all the posts and comments from the selected subreddit between May 2009 and February 2022 using the Python Reddit API Wrapper (PRAW66 6 https://github.com/praw-dev/praw (Accessed on 06/05/2022).) and the Pushshift platform [2]. Nevertheless, we still note that the other subreddits may hold relevant information that can also be exploited in further works. See Appendix A.1 for more details regarding the number of posts/comments per year in the aforementioned subreddits.

**ZH** 为采集 RPCD 数据集，我们识别出业余与专业摄影师用于上传图像或讨论摄影的 Reddit 社区，具体确定了以下六个社区（称为子版块 subreddit）：/r/AskPhotography、/r/photocritique、/r/photographs、/r/portraits、/r/postprocessing、/r/shittyHDR。在仔细审阅各子版块后，我们选择了 /r/photocritique，该版块共有 168,222 条帖子与 731,772 条评论。这一选择依据的是社区规则55 5 https://www.reddit.com/r/photocritique/，其内容特别适合当前任务：其中大多是业余与专业摄影者的作品，能够获得其他摄影师与爱好者的反馈。我们使用 Python Reddit API Wrapper（PRAW66 6 https://github.com/praw-dev/praw（访问日期 2022/05/06）。）与 Pushshift 平台 [2]，下载了该子版块 2009 年 5 月至 2022 年 2 月间的全部帖子与评论。不过，其他子版块同样可能包含有价值的信息，可在后续工作中加以利用。关于上述各子版块每年帖子/评论数量的细节，参见附录 A.1。

**EN** Automatic Filtering.

**ZH** 自动过滤。

**EN** The selected posts are then filtered by using an automated pipeline designed to be reused over time or for other communities. It consists of the following steps. First, each post consists of an image along with a description provided by the photographer usually explaining the aesthetic intent of the photograph and the technical details of the camera used. Additionally, each post has comments from other users structured as layered conversations. As required by the subreddit rules, the first level comments must be a critique to the image in the post. Therefore, we keep the top level comments since they are actual critiques and they are not a follow up comment or part of the body of a conversation. The description and the comments under the first level are discarded, thus reducing the number of comments from 731,772 to 284,426. Secondly, we remove the posts with no comments or whose image is no longer available. As a result, the number of posts is reduced to 103,190. Finally, filtering posts with corrupted or placeholder images leads to the final dataset consisting of 73,965 posts, each of them consisting of an image and an average of 3 critiques to that image.

**ZH** 随后，我们用一条自动化流程筛选所得到的帖子，该流程在设计上可随时间推移复用到其他社区。流程包括以下步骤。首先，每篇帖子由一张图像及摄影者撰写的说明组成，说明通常交代照片的美学意图与所用相机的技术参数；此外，帖子还包含其他用户的评论，这些评论以分层对话的形式组织。按照子版块规则，一级评论必须是对帖子中图像的评论，因此我们保留顶层评论——它们是真正的评论，而非追问或对话正文的一部分。说明文字与一级评论之下的回复被丢弃，评论总数由此从 731,772 降至 284,426。其次，剔除无评论或图像已失效的帖子，帖子数降至 103,190。最后，过滤掉图像损坏或为占位图的帖子，得到最终数据集：73,965 篇帖子，每篇包含一张图像以及平均 3 条针对该图像的评论。

**EN** Statistics.

**ZH** 统计信息。

**EN** Our RPCD dataset consists of 73,965 images with a resolution of ⟦SLOT_30⟧ pixels on average. A total of 219,790 photo critique comments is available, with an average of 49.1 words per comment, a standard deviation of 55.5 and a maximum of 1286 words. Each image has an average of 2.9 comments associated with it, with a standard deviation of 3.7. The general information of our dataset and a comparison with related datasets is presented in Table 1. Several considerations can be made. First, our RPCD dataset is the first large-scale photo critique dataset, with a ⟦SLOT_31⟧ times and ⟦SLOT_32⟧ times increase in the number of images and comments, respectively, compared to the previously available photo critique dataset, PCCD [17]. Secondly, it has a slightly higher average length of comments with respect to PCCD and about 3 times that of AVA-Comments [45] (hereafter simply referred to as AVA). This increase in the amount of information opens the door to the use of large language models to exploit the unstructured information available in form of text. Third, our RPCD dataset consists of images with a much higher resolution than previous datasets (especially those obtained from DPChallenge.com). See Appendix A.2 for a detailed comparison. This may be due to the difference in the time periods of collection for the different datasets. For example, AVA dataset has images posted only until 2011, when the technical performance and availability of cameras were inferior to nowadays. Consequently, the aesthetic quality is very likely to depend on the perceived technical quality [18].

**ZH** 我们的 RPCD 数据集包含 73,965 张图像，平均分辨率为 ⟦SLOT_30⟧ 像素；共有 219,790 条摄影评论，平均每条 49.1 词，标准差 55.5，最长 1286 词；每张图像平均关联 2.9 条评论，标准差 3.7。表 1 给出了数据集的总体信息及与相关数据集的对比。由此可得出几点结论。第一，RPCD 是首个大规模摄影评论数据集，相比此前可用的 PCCD [17]，图像数与评论数分别提升 ⟦SLOT_31⟧ 倍与 ⟦SLOT_32⟧ 倍。第二，其评论平均长度略高于 PCCD，约为 AVA-Comments [45]（下文简称 AVA）的 3 倍；信息量的提升为使用大语言模型挖掘文本形式的非结构化信息创造了条件。第三，RPCD 的图像分辨率远高于以往数据集（尤其是来自 DPChallenge.com 的那些），详见附录 A.2 的细致对比。这可能源于各数据集采集年代的差异：例如 AVA 的图像仅发布至 2011 年，当时相机的技术性能与普及程度都逊于今日。因此，美学质量很可能依赖于所感知的技术质量 [18]。

**EN** Table 1: Comparison of the properties in different benchmark datasets on image aesthetic captioning.

**ZH** 表 1：多个图像美学描述基准数据集的属性对比。

<!-- [原子块 · table] Dataset AVA-Comments [ 45 ] DPC-Captions ∗∗ [ 17 ] PCCD [ 5 ] RPCD (Our) Images 253,961 117,132 4,235 73,965 Avg image resolution 607 × \times 537 606 × \times 534 1414 × \times 1202 2993 × \times 271 -->

**EN** ∗The aspect is obtained through machined-based annotation. See Appendix A.4.

**ZH** ∗该维度通过机器标注获得，参见附录 A.4。

**EN** ∗∗The figures reported on this table are produced using the code made available by the authors of the dataset and differ from those stated in the original paper.

**ZH** ∗∗表中数据由数据集作者提供的代码生成，与原始论文中的数值有所不同。

**EN** 4.2 Sentiment polarity prediction

**ZH** 4.2 情感极性预测

**EN** We propose to use sentiment polarity analysis on the aesthetic critiques to define the aesthetic scores, a.k.a sentiment scores, of the images as detailed in Section 3.3. Sentiment analysis methods can be categorized into lexicon-based methods [16, 35], machine learning methods [11, 44], and hybrid methods [29]. Recently, deep learning methods have enabled the design of sentiment analysis models that have achieved impressive performance over the previous methods [3, 23, 31, 34].

**ZH** 我们提出对美学评论做情感极性分析，以此定义图像的美学分数（亦称情感分数），详见 3.3 节。情感分析方法可分为基于词典的方法 [16, 35]、机器学习方法 [11, 44] 与混合方法 [29]。近年来，深度学习使得情感分析模型的设计取得突破，性能显著超越以往方法 [3, 23, 31, 34]。

**EN** In this work, we use TwitterRoBERTa [1], a deep learning based method inspired by RoBERTa [23], to extract the sentiment polarity on aesthetic critiques. TwitterRoBERTa achieved the best trade-off between performance and model complexity among all the models that participated in the Sentiment Analysis in the Twitter challenge [34]. Although the model is trained in a different domain (Twitter), we assume that the domain is similar enough (social media) to use this model. Future work could explore the use of models tailored for the Reddit sub-domain. Additionally, Transformer models fine-tuned for sentiment analysis are known to have their own set of bias 77 7 https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english#risks-limitations-and-biases. Hence, a deeper analysis of the bias introduced by the selected model, which was not present in the original work [1], would be beneficial. We exploit the implementation of TwitterRoBERTa finetuned for the sentiment prediction task vailable in the HuggingFace transformers library [39]. Figure 1 reports some samples of our dataset annotated with sentiment scores. Individual scores per critique are also included. It can be seen that most of the comments are focused on compositional and stylistic aspects of the photo.

**ZH** 本文采用 TwitterRoBERTa [1]——一种受 RoBERTa [23] 启发的深度学习方法——来提取美学评论的情感极性。TwitterRoBERTa 在参与 Twitter 情感分析挑战赛 [34] 的所有模型中，实现了性能与模型复杂度之间的最佳折中。尽管该模型在不同领域（Twitter）上训练，我们认为二者同属社交媒体，领域足够相近，可以使用。后续工作可探索面向 Reddit 子领域定制的模型。此外，为情感分析微调的 Transformer 模型本身带有一定偏见 77 7 https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english#risks-limitations-and-biases，因此更深入地分析所选模型引入的偏见会很有价值——原工作 [1] 并未涉及这一点。我们使用 HuggingFace transformers 库 [39] 中针对情感预测任务微调的 TwitterRoBERTa 实现。图 1 给出了标注了情感分数的数据集样本，并列出每条评论的单独分数。可以看到，多数评论聚焦于照片的构图与风格方面。

<!-- [原子块 · img]  -->

**EN** Figure 1: RPCD samples annotated with the proposed sentiment score. Sentiment scores are also reported for each comment.

**ZH** 图 1：标注了所提情感分数的 RPCD 样本，同时给出每条评论的情感分数。

**EN** We estimate the sentiment score of the comments of AVA and PCCD for comparison. Figure 2 shows the distribution of sentiment scores for the samples of AVA, PCCD and our RPCD. We observe that the vast majority of the AVA and PCCD dataset samples are characterized by high sentiment scores, which produce left-skewed score distributions. On the other hand, the samples of the proposed RPCD cover almost the entire range of values with two peaks close to the values 1 and 0.5. This difference between ours and the other datasets indicates that RPCD have a richer representation of the whole aesthetic taste spectrum, providing information about why an image have a specific score for high and low sentiment scores. This dissimilarity can be explained by the nature of the different sources of each dataset. While DPChallenge is a community where users score each image, they are not encouraged to critique them as in the r/photocritique subreddit. Consequently, we hypothesize, this produces that only those users with a praise would leave a comment. The fact that there are many more users giving a score than commenting supports this possible explanation. The case of the PCCD dataset is more difficult to analyze since the source website88 8 https://gurushots.com/ does not provide the critiques feature anymore, but the fact that the dataset is heavily imbalanced may explain why the sentiment score is also imbalanced.

**ZH** 我们还估计了 AVA 与 PCCD 评论的情感分数以作比较。图 2 展示了 AVA、PCCD 与 RPCD 样本的情感分数分布。可以看到，AVA 与 PCCD 的绝大多数样本情感分数偏高，分布呈左偏；而 RPCD 的样本几乎覆盖了整个取值区间，并在 1 与 0.5 附近形成两个峰值。这一差异说明 RPCD 对整体美学偏好谱系的刻画更为丰富，能够说明图像在高、低情感分数处为何得到某一特定分数。这种差异可由各数据集来源的性质解释：DPChallenge 社区鼓励用户为图像打分，却不鼓励像 r/photocritique 子版块那样给出评论。我们推测，这导致只有想要称赞的用户才会留言，而打分用户远多于评论用户的事实也支持了这一解释。PCCD 的情况较难分析，因为其来源网站88 8 https://gurushots.com/ 已不再提供评论功能，但该数据集严重不平衡，或许可以解释情感分数同样不平衡的现象。

<!-- [原子块 · object]  -->

**EN** Figure 2: Sentiment score distribution on AVA, PCCD and our RPCD dataset.

**ZH** 图 2：AVA、PCCD 与本文 RPCD 数据集上的情感分数分布。

**EN** We also estimate how the sentiment score correlates with the annotated human aesthetic judgment for the AVA and PCCD images. In particular, we measure Spearman’s Rank Correlation Coefficient (SRCC) and Pearson’s Linear Correlation Coefficient (PLCC). On the AVA dataset, the SRCC is equal to 0.6418 while PLCC corresponds to 0.6424. For PCCD, SRCC is 0.6066 and PLCC 0.6499. The positive correlation on both datasets indicates the effectiveness of the proposed score and, therefore, that it represents a trustworthy approximation of the aesthetic score. Figure 3 shows the scatter plots relating the aesthetic score and sentiment score for the two considered datasets. It can be seen that most of the AVA aesthetic scores were originally annotated around the average value of the rating scale, i.e. 5. In fact, it is worth noting that AVA sentiment scores span the whole rating scale for aesthetic scores equal to or close to 5. We deepen the latter case in Appendix A.1. PCCD original scores, on the other hand, are very positive with a high concentration of samples for values between 7 and 9. Generally, our sentiment scores take on less biased values than previous aesthetic scores.

**ZH** 我们还度量了情感分数与 AVA、PCCD 图像上人工美学判断之间的相关性，具体采用斯皮尔曼秩相关系数（SRCC）与皮尔逊线性相关系数（PLCC）。在 AVA 上，SRCC 为 0.6418，PLCC 为 0.6424；在 PCCD 上，SRCC 为 0.6066，PLCC 为 0.6499。两个数据集上均呈正相关，说明所提分数有效，可作为美学分数的可信近似。图 3 给出了两个数据集美学分数与情感分数的散点图。可以看到，AVA 的美学分数大多标注在评分区间的均值附近，即 5；值得注意的是，当美学分数等于或接近 5 时，AVA 的情感分数几乎跨越整个评分区间，我们在附录 A.1 中对这一情形做了深入分析。而 PCCD 的原始分数普遍偏高，样本集中在 7 到 9 之间。总体而言，我们的情感分数取值比以往美学分数的偏差更小。

<!-- [原子块 · table] (a) AVA (b) PCCD -->

**EN** Figure 3: Annotated aesthetic score vs. Sentiment polarity score for (a) AVA and (b) PCCD samples.

**ZH** 图 3：（a）AVA 与（b）PCCD 样本的标注美学分数与情感极性分数对比。

**EN** 4.3 Content Analysis

**ZH** 4.3 内容分析

**EN** In this section, we present an in-depth analysis of the images and comments in our dataset. This analysis is conducted by training different models to annotate aspects related to the semantics and composition of images and to estimate the usefulness and topics of the comments.

**ZH** 本节对数据集中的图像与评论做深入分析，具体做法是训练若干模型，对图像的语义与构图相关维度进行标注，并估计评论的有用性与主题。

**EN** Image Analysis.

**ZH** 图像分析。

**EN** For semantic content analysis, we group images into six categories, i.e., Animal, Architecture, Human, Landscape, Plant, and Static/Others. The semantic categories above are the same as CUHK-PQ, excluding the Night category. The latter is misleading as it represents the time of the shot and not a semantic category. Figure 4 shows the distribution of images per semantic category. As it is possible to see, most RPCD images contain landscapes. The second largest content category (approximately 15K images) includes human beings. The semantic class with the lowest number of instances is Plant. We also report results for shot scale classification, which determines the portion occupied by the main subject with respect to the frame. We distinguish five shot scale types defined in the training dataset MovieNet [15]: Extreme close-up, Close-up, Medium, Full, Long. Figure 4 shows that about 30K images have been labeled as Long shot scale. This result is in line with the fact that most images are of the semantic Landscape type. Very few images have been classified as Close-up or Medium range content, meaning photographers have preferred to capture subjects from very close or far away. Finally, we inspect images from the point of view of photographic composition. Specifically, images are categorized with respect to the main composition rule among the following eight: Rule-of-Thirds, Vertical, Horizontal, Diagonal, Curved, Triangle, Center, Symmetric, Pattern. The above composition rules are defined in the KU-PCP dataset [21]. Figure 4 presents the distribution of the images with respect to the composition rules. The images in our dataset are very bias on the Center category, indicating that in most images there is the main subject occupying the central region of the image. In Appendix A.4 we detail how we build the models for running the previous analysis and present some sample images for each of the analyzed aspects.

**ZH** 在语义内容分析方面，我们将图像分为六类：动物、建筑、人物、风景、植物与静物/其他。上述语义类别与 CUHK-PQ 一致，但去掉了“夜景”类别——后者具有误导性，因为它表示的是拍摄时段而非语义类别。图 4 给出了各语义类别的图像分布。可以看出，RPCD 中多数图像为风景；第二大内容类别（约 15K 张）为人物；样本最少的语义类别是植物。我们还给出了景别分类的结果，景别刻画主体在画面中所占的比例。我们区分 MovieNet [15] 训练集中定义的五种景别：极特写、特写、中景、全景、远景。图 4 显示约 30K 张图像被标注为远景，这与多数图像属于风景语义类别的事实相符。被划分为特写或中景的图像极少，说明摄影者更倾向于从极近或极远处拍摄主体。最后，我们从摄影构图角度审视图像，具体按以下主要构图规则分类：三分法、垂直、水平、对角、曲线、三角、居中、对称、图案，这些规则定义于 KU-PCP 数据集 [21]。图 4 给出了图像在各构图规则上的分布。数据集中图像严重偏向“居中”类别，说明多数图像中主体占据画面中央区域。附录 A.4 详述了如何构建模型完成上述分析，并给出各分析维度的样张。

<!-- [原子块 · img]  -->

**EN** Figure 4: RPCD analysis. Left: Shot scale. Center: Image Composition, Right: Image Content.

**ZH** 图 4：RPCD 分析。左：景别；中：图像构图；右：图像内容。

**EN** Comment Analysis.

**ZH** 评论分析。

**EN** We analyze the topics of the corpus of comments in our dataset using BERTopic [12], a topic modeling technique. The most common topics in the analyzed datasets regards semantic aspects such as face, tree, bird, flower, and stars. There are also topics related to technical aspects of photography, namely ISO, aperture, dynamic range, and HDR. We refer to Appendix A.6 for a deeper analysis. Additionally, we use the definition of informativeness score of a previous work [10] to estimate whether the comments of our dataset are meaningful and how do they compare to other datasets. In the Appendix A.7 we compare the results on our dataset with those of state-of-the-art datasets, finding that, on average, the proposed RPCD contains the most informative comments, with an informativeness score slightly higher than PCCD and more than double than AVA.

**ZH** 我们使用主题建模技术 BERTopic [12] 分析数据集中评论语料的主题。最常见的主题涉及语义方面，如人脸、树、鸟、花、星空；也有与摄影技术相关的主题，即 ISO、光圈、动态范围与 HDR，更深入的分析参见附录 A.6。此外，我们沿用 [10] 中信息量分数的定义，估计数据集评论是否有意义以及与其他数据集相比如何。附录 A.7 将本文数据集的结果与当前最优数据集做了对比，发现 RPCD 所含评论平均信息量最高，其信息量分数略高于 PCCD，是 AVA 的两倍多。

**EN** 5 Evaluation

**ZH** 5 实验评估

**EN** To illustrate the possible uses of the newly introduced dataset, we run several experiments around the image aesthetic assessment task, where our goal is to predict an aesthetic score given an image, as well as in the image captioning task, where our goal is to predict an aesthetic critique given an image. To this aim, we split the whole dataset into 70% training samples, 10% validation samples, and the remaining 20% for testing.

**ZH** 为展示新数据集的可能用途，我们围绕图像美学评估任务（给定图像预测美学分数）与图像描述任务（给定图像预测美学评论）开展了若干实验。为此，我们将整个数据集按 70% 训练、10% 验证、20% 测试划分。

**EN** 5.1 Image Aesthetic Assessment

**ZH** 5.1 图像美学评估

**EN** The main motivation to create this dataset is to perform Image Aesthetic Assessment with the interpretability of the aesthetic critiques. We use the scores computed using sentiment analysis and propose a method to predict such scores. We also run SOTA models on our dataset for comparison.

**ZH** 构建该数据集的主要动机，是借助美学评论的可解释性来完成图像美学评估。我们使用情感分析计算得到的分数，并提出一种预测这些分数的方法，同时在本文数据集上运行当前最优模型作为对比。

**EN** In Table 2 we report SRCC, LCC and Accuracy on our RPCD, PCCD [5] and AVA [28] datasets using the sentiment score, comparing the results of NIMA [37] and other experiments we carried out. We additionally perform an extensive evaluation of the family of ViT models in Appendix B to assess the suitability of such models for the aesthetic assessment task, evaluating its performance on AVA dataset. We highlight that ViT Large (we called AestheticViT) outperforms previous SOTA model [14] by a 4% in the correlation metrics on AVA dataset using the original scores. In the ViT + Linear probe experiments, we also study to what extent the results obtained to predict the aesthetic and sentiment scores are due to the knowledge already present in the pretrained model. The accuracy is computed defining as high quality images those with an score above 5, and poor quality otherwise. The results in Table 2 show that, although ViT + Linear probe and AestheticViT outperform a previous aesthetic model used as a baseline, it does not achieve a good enough performance in any of the benchmarks to predict the proposed sentiment score. Moreover, the training of the model on AVA deteriorate its performance. This results proofs how challenging the task is and may indicate that the main previous benchmark, AVA, may be biased towards the content of the images, reducing the importance of the actual aesthetics of the photo. We would like to support the reasoning of Hosu et al. [14] regarding the suitability of correlation metrics rather than accuracy to evaluate this task. While correlation metrics are representative of the entire range of scores, image labels (’good’ or ’bad’) are defined arbitrarily, which becomes an issue when the label distribution is imbalanced as in the case of AVA and PCCD datasets for both the original and sentiment scores.

**ZH** 表 2 给出了在 RPCD、PCCD [5] 与 AVA [28] 三个数据集上以情感分数为目标的 SRCC、LCC 与准确率，并与 NIMA [37] 以及我们开展的其他实验作对比。此外，附录 B 对 ViT 系列模型做了广泛评估，考察其是否适用于美学评估任务，并在 AVA 数据集上评测性能。我们指出，在使用原始分数时，ViT Large（我们称之为 AestheticViT）在 AVA 数据集上的相关性指标比此前最优模型 [14] 高出 4%。在 ViT + 线性探针实验中，我们还考察了预测美学分数与情感分数的结果在多大程度上源自预训练模型中已有的知识。准确率的计算把分数高于 5 的图像定义为高质量，其余为低质量。表 2 的结果显示，尽管 ViT + 线性探针与 AestheticViT 优于作为基线的已有美学模型，但在任何一个基准上预测所提情感分数时，性能都还不够好；而且在 AVA 上训练模型反而使其性能下降。这一结果说明该任务极具挑战性，也可能表明此前的主要基准 AVA 偏向图像内容，削弱了照片本身美学的重要性。我们支持 Hosu 等人 [14] 的观点：评估该任务应更看重相关性指标而非准确率。相关性指标能够反映整个分数区间，而“好”“坏”标签的定义是任意的，当标签分布不平衡时（AVA 与 PCCD 在原始分数和情感分数上均如此）就会产生问题。

**EN** Table 2: Sentiment score baseline on the three considered datasets.

**ZH** 表 2：三个所考察数据集上的情感分数基线结果。

<!-- [原子块 · table] Method AVA PCCD RPCD SRCC LCC Acc. (%) SRCC LCC Acc. (%) SRCC LCC Acc. (%) NIMA [ 37 ] 0.253 0.259 90.20 0.066 0.070 93.87 0.120 0.116 63.25 ViT + Linear probe ∗ 0.570 0.570 76.43 0.156 0.165 93.04 0. -->

**EN** ∗Best performing models. See Appendix B

**ZH** ∗性能最佳的模型，参见附录 B。

**EN** 5.2 Aesthetic Critiques

**ZH** 5.2 美学评论

**EN** We also evaluate our dataset on the task of Aesthetic Image Captioning (AIC), using a SOTA model [22]. To evaluate the results, we follow the procedure of [5] as our dataset also contains more than one reference caption that corresponds to a single image. Table 3 compares the obtained results with the previous work [5] we use as reference. We observe that the achievable performance is far lower than that obtained for the description of the image content (See COCO captions benchmark 99 9 https://paperswithcode.com/sota/image-captioning-on-coco-captions), and further work is necessary to produce meaningful aesthetic captions. More details on the aesthetic critique procedure can be found in Appendix B.2.

**ZH** 我们还在美学图像描述（AIC）任务上评估本数据集，采用当前最优模型 [22]。由于本数据集中一张图像对应多条参考描述，我们沿用 [5] 的流程评估。表 3 将所得结果与作为参照的 [5] 做了比较。可以看到，可达到的性能远低于图像内容描述任务（参见 COCO captions 基准 99 9 https://paperswithcode.com/sota/image-captioning-on-coco-captions），要生成有意义的美学描述还需进一步研究。美学评论流程的更多细节见附录 B.2。

**EN** Table 3: Aesthetic image captioning using BLIP [22] on PCCD and our RPCD.

**ZH** 表 3：在 PCCD 与本文 RPCD 上使用 BLIP [22] 做美学图像描述的结果。

<!-- [原子块 · table] Bleu1 Bleu2 Bleu3 Bleu4 METEOR ROUGE CIDEr SPICE PCCD 0.165 0.065 0.028 0.011 0.063 0.137 0.049 0.048 RPCD 0.211 0.088 0.038 0.017 0.077 0.157 0.048 0.040 -->

**EN** 6 Discussion and Future Work

**ZH** 6 讨论与未来工作

**EN** We presented the Reddit Photo Critique Dataset (RPCD) consisting of image and photo critiques tuples. This dataset is collected by crawling posts from a community where people are encouraged to criticize positive and negative image aesthetic aspects. Our dataset has approximately 18⟦SLOT_33⟧ the images and 7⟦SLOT_34⟧ the comments compared to the PCCD dataset. Compared to AVA, the best-known aesthetic assessment dataset, our RPCD has longer and more meaningful comments and higher resolution images. Together with the dataset, we have for the first time in the literature defined an approach to obtain the aesthetic ranking of images directly from the analysis of comments. The proposed approach is based on the sentiment analysis of the comments. The proposed score was shown to have a positive correlation with the aesthetic judgments of humans. Therefore, RPCD can be used both to predict aesthetic captions and to estimate an aesthetic score. We conducted several experiments for the image aesthetic assessment task in which we compared the results obtained from different methods on our dataset, AVA and PCCD. These experiments show that a ViT is able to obtain good performance on AVA while both PCCD and RPCD are more challenging. The use of content-aware (ViT + Linear Probe), instead of aesthetic-aware (Aesthetic ViT), features results in a significant drop in performance for those datasets that may be less content-biased. Experiments on aesthetic image captioning carried out on PCCD and RPCD datasets highlight that the achievable performance is far lower than that obtained for the description of the image content, and further work is necessary to produce meaningful aesthetic captions.

**ZH** 我们提出了 Reddit 摄影评论数据集（RPCD），它由图像与摄影评论构成的元组组成。该数据集采集自一个鼓励人们对图像美学优劣发表评论的社区。相比 PCCD 数据集，本数据集的图像数约为其 18⟦SLOT_33⟧ 倍，评论数约为其 7⟦SLOT_34⟧ 倍。相比最广为人知的美学评估数据集 AVA，RPCD 的评论更长、更有意义，图像分辨率也更高。在提出数据集的同时，我们还首次在文献中给出一种直接通过分析评论获得图像美学排序的方法，该方案基于对评论的情感分析。实验表明，所提分数与人类的美学判断呈正相关，因此 RPCD 既可用于预测美学描述，也可用于估计美学分数。我们在图像美学评估任务上开展了若干实验，比较不同方法在本文数据集、AVA 与 PCCD 上的结果。这些实验显示，ViT 能在 AVA 上取得良好性能，而 PCCD 与 RPCD 都更具挑战性。对于那些内容偏置较弱的数据集，使用内容感知特征（ViT + 线性探针）替代美学感知特征（Aesthetic ViT）会导致性能显著下降。在 PCCD 与 RPCD 上开展的美学图像描述实验则表明，可达到的性能远低于图像内容描述任务，要生成有意义的美学描述仍需进一步研究。

**EN** However, several limitations remain. First, the limited number of comments per image (i.e., 3 in average), although the comments are long and very informative, could make the evaluation biased by the few users and not sufficiently objective. Second, we encourage the Machine Learning community to work on alternative or complementary solutions to the proposed sentiment analysis as a proxy for aesthetics. Among other things, the fact that the sentiment score is automatically estimated could cause noisy annotations and the change in the data domain should be further studied. This noisy annotations could be influenced by the potential bias present in the selected model. Third, the aesthetic captioning task remains an open challenge. Finally, the concept of aesthetics expressed in our dataset must be understood limitedly to the Western cultural and geographical context on the basis of the demographic statistics of the Reddit users (see Appendix A.1). Additionally, other ethical considerations are discussed in Appendix D.

**ZH** 然而，仍存在若干局限。第一，每张图像的评论数量有限（平均 3 条），尽管评论较长且信息丰富，评估仍可能因少数用户而产生偏差，客观性不足。第二，我们鼓励机器学习社区研究替代或补充方案，以取代将情感分析作为美学代理的做法。其中，情感分数由自动估计得到，可能引入噪声标注，且数据领域变化的影响有待进一步研究；这些噪声标注还可能受到所选模型潜在偏见的影响。第三，美学描述生成仍是一项开放式挑战。最后，依据 Reddit 用户的人口统计特征（见附录 A.1），本数据集所表达的美学概念应被理解为局限于西方文化与地理语境。其他伦理考量在附录 D 中讨论。

**EN** Despite the above limitations, we believe RPCD is an important contribution for the design of multi-modal and explainable aesthetic assessment models. As a future work, we would like to deepen the ranking method based on the analysis of comments in order to make it more reliable and diversified for the different aspects that characterize the aesthetics: style, color, composition, etc. In addition we will be able to interpret which are the aspects that are evaluated more positively or negatively by users. Finally, exploiting new sources of available data may provide further benefits while training larger models.

**ZH** 尽管存在上述局限，我们认为 RPCD 对设计多模态、可解释的美学评估模型是一项重要贡献。未来工作中，我们希望深化基于评论分析的排序方法，使其在刻画美学的不同维度（风格、色彩、构图等）上更可靠、更具区分度，并进一步解读用户评价更正面或更负面的具体维度。此外，利用新的可用数据来源训练更大规模的模型也可能带来额外收益。

**EN** Acknowledgments

**ZH** 致谢

**EN** This project is supported by Ringier, TX Group, NZZ, SRG, VSM, Viscom, and the ETH Zurich Foundation.

**ZH** 本项目由 Ringier、TX Group、NZZ、SRG、VSM、Viscom 与苏黎世联邦理工学院基金会（ETH Zurich Foundation）支持。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] [1] Francesco Barbieri, Jose Camacho-Collados, Luis Espinosa Anke, and Leonardo Neves. TweetEval: Unified benchmark and comparative evaluation for tweet classification. In Findings of the Association  -->

<!-- [原子块 · verbatim] [2] Jason Baumgartner, Savvas Zannettou, Brian Keegan, Megan Squire, and Jeremy Blackburn. The pushshift reddit dataset. In International AAAI Conference on Web and Social Media , volume 14, pages 830 -->

<!-- [原子块 · verbatim] [3] Zhang Bingyu and Nikolay Arefyev. The document vectors using cosine similarity revisited. In Workshop on Insights from Negative Results in NLP , pages 129–133, 2022. -->

<!-- [原子块 · verbatim] [4] Luigi Celona, Marco Leonardi, Paolo Napoletano, and Alessandro Rozza. Composition and style attributes guided image aesthetic assessment. IEEE Transactions on Image Processing , 31:5009–5024, 2022 -->

<!-- [原子块 · verbatim] [5] Kuang-Yu Chang, Kung-Hung Lu, and Chu-Song Chen. Aesthetic critiques generation for photos. In International Conference on Computer Vision , pages 3514–3523. IEEE, 2017. -->

<!-- [原子块 · verbatim] [6] Qiuyu Chen, Wei Zhang, Ning Zhou, Peng Lei, Yi Xu, Yu Zheng, and Jianping Fan. Adaptive fractional dilated convolution network for image aesthetics assessment. In Computer Vision and Pattern Recog -->

<!-- [原子块 · verbatim] [7] Ritendra Datta, Dhiraj Joshi, Jia Li, and James Z Wang. Studying aesthetics in photographic images using a computational approach. In European Conference on Computer Vision , pages 288–301. Spring -->

<!-- [原子块 · verbatim] [8] Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, Jakob Uszkoreit, and N -->

<!-- [原子块 · verbatim] [9] Timnit Gebru, Jamie Morgenstern, Briana Vecchione, Jennifer Wortman Vaughan, Hanna Wallach, Hal Daumé Iii, and Kate Crawford. Datasheets for datasets. Communications of the ACM , 64(12):86–92, 202 -->

<!-- [原子块 · verbatim] [10] Koustav Ghosal, Aakanksha Rana, and Aljosa Smolic. Aesthetic image captioning from weakly-labelled photographs. In International Conference on Computer Vision Workshops , pages 0–0. IEEE/CVF, 201 -->

<!-- [原子块 · verbatim] [11] SR Gowda, BR Archana, Praajna Shettigar, and Kislay Kumar Satyarthi. Sentiment analysis of twitter data using naïve bayes classifier. In ICDSMLA 2020 , pages 1227–1234. Springer, 2022. -->

<!-- [原子块 · verbatim] [12] Maarten Grootendorst. Bertopic: Neural topic modeling with a class-based tf-idf procedure. arXiv preprint arXiv:2203.05794 , 2022. -->

<!-- [原子块 · verbatim] [13] Chaoyi Hong, Shuaiyuan Du, Ke Xian, Hao Lu, Zhiguo Cao, and Weicai Zhong. Composing photos like a photographer. In Conference on Computer Vision and Pattern Recognition , pages 7057–7066. IEEE/CV -->

<!-- [原子块 · verbatim] [14] Vlad Hosu, Bastian Goldlucke, and Dietmar Saupe. Effective aesthetics prediction with multi-level spatially pooled features. In Conference on Computer Vision and Pattern Recognition , pages 9375– -->

<!-- [原子块 · verbatim] [15] Qingqiu Huang, Yu Xiong, Anyi Rao, Jiaze Wang, and Dahua Lin. Movienet: A holistic dataset for movie understanding. In European Conference on Computer Vision , pages 709–727. Springer, 2020. -->

<!-- [原子块 · verbatim] [16] Mohammad Rezwanul Huq, Ali Ahmad, and Anika Rahman. Sentiment analysis on twitter data using knn and svm. International Journal of Advanced Computer Science and Applications , 8(6), 2017. -->

<!-- [原子块 · verbatim] [17] Xin Jin, Le Wu, Geng Zhao, Xiaodong Li, Xiaokun Zhang, Shiming Ge, Dongqing Zou, Bin Zhou, and Xinghui Zhou. Aesthetic attributes assessment of images. In International Conference on Multimedia , -->

<!-- [原子块 · verbatim] [18] Chen Kang, Giuseppe Valenzise, and Frédéric Dufaux. Eva: An explainable visual aesthetics dataset. In Joint Workshop on Aesthetic and Technical Quality Assessment of Multimedia and Media Analytic -->

<!-- [原子块 · verbatim] [19] Junjie Ke, Qifei Wang, Yilin Wang, Peyman Milanfar, and Feng Yang. Musiq: Multi-scale image quality transformer. In International Conference on Computer Vision , pages 5148–5157. IEEE/CVF, 2021. -->

<!-- [原子块 · verbatim] [20] Shu Kong, Xiaohui Shen, Zhe Lin, Radomir Mech, and Charless Fowlkes. Photo aesthetics ranking network with attributes and content adaptation. In European Conference on Computer Vision , pages 662 -->

<!-- [原子块 · verbatim] [21] Jun-Tae Lee, Han-Ul Kim, Chul Lee, and Chang-Su Kim. Photographic composition classification and dominant geometric element detection for outdoor scenes. Journal of Visual Communication and Image -->

<!-- [原子块 · verbatim] [22] Junnan Li, Dongxu Li, Caiming Xiong, and Steven Hoi. Blip: Bootstrapping language-image pre-training for unified vision-language understanding and generation. In International Conference on Machi -->

<!-- [原子块 · verbatim] [23] Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov. Roberta: A robustly optimized BERT pretraining approach. Co -->

<!-- [原子块 · verbatim] [24] Xin Lu, Zhe Lin, Hailin Jin, Jianchao Yang, and James Z Wang. Rapid: Rating pictorial aesthetics using deep learning. In International Conference on Multimedia , pages 457–466. ACM, 2014. -->

<!-- [原子块 · verbatim] [25] Wei Luo, Xiaogang Wang, and Xiaoou Tang. Content-based photo quality assessment. In International Conference on Computer Vision , volume 15, pages 2206–2213, 11 2011. -->

<!-- [原子块 · verbatim] [26] Shuang Ma, Jing Liu, and Chang Wen Chen. A-lamp: Adaptive layout-aware multi-patch deep convolutional neural network for photo aesthetic assessment. In Conference on Computer Vision and Pattern R -->

<!-- [原子块 · verbatim] [27] Luca Marchesotti, Florent Perronnin, Diane Larlus, and Gabriela Csurka. Assessing the aesthetic quality of photographs using generic image descriptors. In International Conference on Computer Vis -->

<!-- [原子块 · verbatim] [28] Naila Murray, Luca Marchesotti, and Florent Perronnin. Ava: A large-scale database for aesthetic visual analysis. In Conference on Computer Vision and Pattern Recognition , pages 2408–2415. IEEE, -->

<!-- [原子块 · verbatim] [29] Avinash Chandra Pandey, Dharmveer Singh Rajpoot, and Mukesh Saraswat. Twitter sentiment analysis using hybrid cuckoo search method. Information Processing & Management , 53(4):764–779, 2017. -->

<!-- [原子块 · verbatim] [30] F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, M. Blondel, P. Prettenhofer, R. Weiss, V. Dubourg, J. Vanderplas, A. Passos, D. Cournapeau, M. Brucher, M. Perrot, and E -->

<!-- [原子块 · verbatim] [31] NS Punith and Krishna Raketla. Sentiment analysis of drug reviews using transfer learning. In 2021 Third International Conference on Inventive Research in Computing Applications (ICIRCA) , pages  -->

<!-- [原子块 · verbatim] [32] Anyi Rao, Jiaze Wang, Linning Xu, Xuekun Jiang, Qingqiu Huang, Bolei Zhou, and Dahua Lin. A unified framework for shot type classification based on subject centric lens. In European Conference on -->

<!-- [原子块 · verbatim] [33] Matthew D Rocklage, Derek D Rucker, and Loran F Nordgren. Mass-scale emotionality reveals human behaviour and marketplace success. Nature human behaviour , 5(10):1323–1329, 2021. -->

<!-- [原子块 · verbatim] [34] Sara Rosenthal, Noura Farra, and Preslav Nakov. SemEval-2017 task 4: Sentiment analysis in Twitter. In International Workshop on Semantic Evaluation (SemEval-2017) , pages 502–518, Vancouver, Can -->

<!-- [原子块 · verbatim] [35] María del Pilar Salas-Zárate, Jose Medina-Moreira, Katty Lagos-Ortiz, Harry Luna-Aveiga, Miguel Angel Rodriguez-Garcia, and Rafael Valencia-Garcia. Sentiment analysis on tweets about diabetes: an -->

<!-- [原子块 · verbatim] [36] Rossano Schifanella, Miriam Redi, and Luca Maria Aiello. An image is worth more than a thousand favorites: Surfacing the hidden beauty of flickr pictures. In International AAAI Conference on Web  -->

<!-- [原子块 · verbatim] [37] Hossein Talebi and Peyman Milanfar. Nima: Neural image assessment. IEEE Transactions on Image Processing , 27(8):3998–4011, 2018. -->

<!-- [原子块 · verbatim] [38] Wenshan Wang, Su Yang, Weishan Zhang, and Jiulong Zhang. Neural aesthetic image reviewer. IET Comput. Vis. , 13(8):749–758, 2019. -->

<!-- [原子块 · verbatim] [39] Thomas Wolf, Lysandre Debut, Victor Sanh, Julien Chaumond, Clement Delangue, Anthony Moi, Pierric Cistac, Tim Rault, Remi Louf, Morgan Funtowicz, Joe Davison, Sam Shleifer, Patrick von Platen, Cl -->

<!-- [原子块 · verbatim] [40] Yifei Xu, Nuo Zhang, Pingping Wei, Genan Sang, Li Li, and Feng Yuan. Deep neural framework with visual attention and global context for predicting image aesthetics. IEEE Access , 2020. -->

<!-- [原子块 · verbatim] [41] Yong-Yaw Yeo, John See, Lai-Kuan Wong, and Hui-Ngo Goh. Generating aesthetic based critique for photographs. In International Conference on Image Processing , pages 2523–2527. IEEE, 2021. -->

<!-- [原子块 · verbatim] [42] Jiajing Zhang, Yongwei Miao, and Jinhui Yu. A comprehensive survey on computational aesthetic evaluation of visual art images: Metrics and challenges. IEEE Access , 2021. -->

<!-- [原子块 · verbatim] [43] Luming Zhang, Yue Gao, Roger Zimmermann, Qi Tian, and Xuelong Li. Fusion of multichannel local and global structural cues for photo aesthetics evaluation. IEEE Transactions on Image Processing ,  -->

<!-- [原子块 · verbatim] [44] Xueying Zhang and Xianghan Zheng. Comparison of text sentiment analysis based on machine learning. In International Symposium on Parallel and Distributed Computing (ISPDC) , pages 230–233. IEEE,  -->

<!-- [原子块 · verbatim] [45] Ye Zhou, Xin Lu, Junping Zhang, and James Z Wang. Joint image and text representation for aesthetics analysis. In International Conference on Multimedia , pages 262–266. ACM, 2016. -->

**EN** Checklist

**ZH** 检查清单

**EN** 1. For all authors… (a) Do the main claims made in the abstract and introduction accurately reflect the paper’s contributions and scope? [Yes] The main claims are listed at the end of Section 1. (b) Did you describe the limitations of your work? [Yes] The limitations are described in Section 6. (c) Did you discuss any potential negative societal impacts of your work? [Yes] The potential negative societal impacts are described in Section 6. (d) Have you read the ethics review guidelines and ensured that your paper conforms to them? [Yes] We additionally comment on different ethics consideration on Appendix D.

**ZH** 1. 对所有作者而言……（a）摘要与引言中的主要论断是否准确反映了论文的贡献与范围？[是] 主要论断列于第 1 节末尾。（b）是否说明了工作的局限性？[是] 局限性见第 6 节。（c）是否讨论了工作潜在的负面社会影响？[是] 潜在负面社会影响见第 6 节。（d）是否阅读了伦理审查指南并确认论文符合其要求？[是] 我们还在附录 D 中就多项伦理考量作了补充说明。

**EN** 2. If you are including theoretical results… (a) Did you state the full set of assumptions of all theoretical results? [N/A] (b) Did you include complete proofs of all theoretical results? [N/A]

**ZH** 2. 若包含理论结果……（a）是否陈述了所有理论结果的完整假设集？[不适用]（b）是否给出了所有理论结果的完整证明？[不适用]

**EN** 3. If you ran experiments (e.g. for benchmarks)… (a) Did you include the code, data, and instructions needed to reproduce the main experimental results (either in the supplemental material or as a URL)? [Yes] All necessary code is available on this repository https://github.com/mediatechnologycenter/aestheval. (b) Did you specify all the training details (e.g., data splits, hyperparameters, how they were chosen)? [Yes] See Appendix B. (c) Did you report error bars (e.g., with respect to the random seed after running experiments multiple times)? [No] Training are very compute intensive. We can only run the training once per experiment using a random seed (arbitrarily selected). (d) Did you include the total amount of compute and the type of resources used (e.g., type of GPUs, internal cluster, or cloud provider)? [Yes] See Appendix C

**ZH** 3. 若开展了实验（例如基准评测）……（a）是否提供了复现主要实验结果所需的代码、数据与说明（置于补充材料或以 URL 形式给出）？[是] 全部必需代码见仓库 https://github.com/mediatechnologycenter/aestheval。（b）是否说明了全部训练细节（如数据划分、超参数及其选取方式）？[是] 参见附录 B。（c）是否报告了误差范围（如在多次运行实验后针对随机种子的波动）？[否] 训练计算开销极大，每个实验只能在选定一个随机种子后运行一次。（d）是否给出了所用计算总量与资源类型（如 GPU 型号、内部集群或云服务商）？[是] 参见附录 C。

**EN** 4. If you are using existing assets (e.g., code, data, models) or curating/releasing new assets… (a) If your work uses existing assets, did you cite the creators? [Yes] (b) Did you mention the license of the assets? [Yes] We describe the license of used source of data in Appendix E (c) Did you include any new assets either in the supplemental material or as a URL? [Yes] (d) Did you discuss whether and how consent was obtained from people whose data you’re using/curating? [Yes] See Appendix D (e) Did you discuss whether the data you are using/curating contains personally identifiable information or offensive content? [Yes] See Appendix D

**ZH** 4. 若使用了既有资源（如代码、数据、模型）或整理/发布了新资源……（a）工作使用了既有资源时，是否引用了资源创建者？[是]（b）是否说明了资源的许可协议？[是] 我们在附录 E 中描述了所使用数据来源的许可协议。（c）是否以补充材料或 URL 形式提供了新资源？[是]（d）是否说明了是否以及如何取得数据提供者的同意？[是] 参见附录 D。（e）是否说明了所使用/整理的数据是否包含个人身份信息或冒犯性内容？[是] 参见附录 D。

**EN** 5. If you used crowdsourcing or conducted research with human subjects… (a) Did you include the full text of instructions given to participants and screenshots, if applicable? [N/A] (b) Did you describe any potential participant risks, with links to Institutional Review Board (IRB) approvals, if applicable? [N/A] (c) Did you include the estimated hourly wage paid to participants and the total amount spent on participant compensation? [N/A]

**ZH** 5. 若使用了众包或开展了涉及人类受试者的研究……（a）是否提供了向参与者给出的完整说明文本与截图（如适用）？[不适用]（b）是否描述了参与者的潜在风险，并给出机构审查委员会（IRB）审批链接（如适用）？[不适用]（c）是否给出了支付给参与者的估计时薪与参与者补偿总额？[不适用]

**EN** Appendix A Dataset Analysis

**ZH** 附录 A 数据集分析

**EN** A.1 Subreddits Analysis

**ZH** A.1 子版块分析

**EN** There are 1.5M members in the /r/photocritique subreddit. Since it is not possible to collect demographic information about subreddit members, we report the statistic related to a recent analysis about Reddit 1010 10 https://www.statista.com/topics/5672/reddit/#topicHeader (Accessed on 22/08/2022). Slight majority of Reddit users are male (61%). 48% of Reddit users are in the US, followed by the UK, Canada, Australia and Germany. People between the age of 18 and 29 make up Reddit’s largest user base (64%). The second biggest age group is 30 to 49 (29%). Teenagers below 15 are not very active on Reddit. Only 7% of Reddit users are over 50.

**ZH** /r/photocritique 子版块拥有 150 万名成员。由于无法采集子版块成员的人口统计信息，我们引用最近一项 Reddit 相关分析的统计数据 1010 10 https://www.statista.com/topics/5672/reddit/#topicHeader（访问日期 2022/08/22）。Reddit 用户中男性略占多数（61%）；48% 的 Reddit 用户位于美国，其后依次是英国、加拿大、澳大利亚与德国；18 至 29 岁人群构成 Reddit 最大的用户群（64%），第二大年龄组为 30 至 49 岁（29%）；15 岁以下青少年在 Reddit 上不太活跃；Reddit 用户中仅 7% 超过 50 岁。

**EN** In light of the previous statistics, it is necessary to underline that the data treated in our dataset, therefore the inferred concept of aesthetics, presents a bias due to the limited cultural and geographical integration of the people who produced the information.

**ZH** 鉴于上述统计，有必要指出：本数据集所处理的数据以及由此推断出的美学概念，存在因信息生产者文化与地域融合度有限而产生的偏差。

**EN** Here, it follows a deeper analysis of /r/photocritique subreddit. Figure 5 shows the number of posts and comments per year downloaded from the seven subreddits we have selected. We observe that the number of posts and comments increase over the course of time. Data from 2013 could not be retrieved due to problems with Pushshift 1111 11 https://www.reddit.com/r/pushshift/comments/sb982i/very_recent_data_missing/. Since 2015 there have been a number of posts over 20K and a number of comments that exceeds 100K until reaching the peak of 250K in 2021. Furthermore, although the posts are substantially fewer than the comments, the posts have reached a constant level of over 50,000 per year.

**ZH** 下面对 /r/photocritique 子版块做更深入的分析。图 5 给出了我们从所选七个子版块下载到的逐年帖子数与评论数。可以看到，帖子数与评论数随时间推移不断增长；2013 年的数据因 Pushshift 故障未能获取 1111 11 https://www.reddit.com/r/pushshift/comments/sb982i/very_recent_data_missing/。自 2015 年起，帖子数每年超过 20K，评论数每年超过 100K，并在 2021 年达到 250K 的峰值。此外，尽管帖子数明显少于评论数，但帖子数已稳定在每年 5 万条以上的水平。

<!-- [原子块 · object]  -->

**EN** Figure 5: The number of posts and comments between May 2009 and February 2022 for the 6 considered subreddits.

**ZH** 图 5：2009 年 5 月至 2022 年 2 月间 6 个所考察子版块的帖子数与评论数。

**EN** A.2 Image Resolution

**ZH** A.2 图像分辨率

**EN** We investigate the resolution of the images of three datasets, namely AVA, PCCD, and our RPCD. We categorize images into 4 common image resolutions in still camera photography, namely Standard Definition – SD (⟦SLOT_35⟧ pixels), High Definition – HD (⟦SLOT_36⟧ pixels), FullHD (⟦SLOT_37⟧ pixels), and UltraHD (⟦SLOT_38⟧ pixels). In Figure 6 the distributions of the images for the three datasets are plotted with respect to the four considered resolutions. As it is possible to see, our dataset it the only one that has UltraHD images. Most of the images are UltraHD resolution (51.20%), but there are also images for the other three resolutions. On the other hand, all AVA images have a resolution of ⟦SLOT_39⟧ pixels, while most PCCD images (i.e. 89.07%) have FullHD resolution.

**ZH** 我们考察 AVA、PCCD 与本文 RPCD 三个数据集的图像分辨率，将图像归入静态摄影中常见的 4 类分辨率：标准清晰度 SD（⟦SLOT_35⟧ 像素）、高清 HD（⟦SLOT_36⟧ 像素）、全高清 FullHD（⟦SLOT_37⟧ 像素）与超高清 UltraHD（⟦SLOT_38⟧ 像素）。图 6 绘制了三个数据集在四类分辨率上的图像分布。可以看到，本文数据集是唯一包含 UltraHD 图像的，其中大部分（51.20%）为 UltraHD 分辨率，同时也有其余三类分辨率的图像。AVA 的全部图像分辨率均为 ⟦SLOT_39⟧ 像素，而 PCCD 的多数图像（89.07%）为 FullHD 分辨率。

<!-- [原子块 · object]  -->

**EN** Figure 6: Image distribution of AVA, PCCD and our dataset, RPCD, for various standard image resolutions.

**ZH** 图 6：AVA、PCCD 与本文数据集 RPCD 在各标准图像分辨率上的图像分布。

**EN** A.3 Sentiment Polarity Classification

**ZH** A.3 情感极性分类

**EN** We delve into the analysis of the sentiment score distributions of our dataset and those of AVA and PCCD. Figure 7 shows the spreads of the sentiment scores for the three datasets. AVA and PCCD have very similar median and standard deviation, namely 0.77 and about 0.15. Our RPCD on the other hand has a median of 0.60 and a larger standard deviation (i.e., 0.25). This difference between ours and the other datasets indicates that RPCD have a richer representation of the whole aesthetic taste spectrum, providing information about why an image have a specific score for high and low sentiment scores.

**ZH** 我们深入分析了本文数据集与 AVA、PCCD 的情感分数分布。图 7 展示了三个数据集情感分数的离散程度。AVA 与 PCCD 的中位数与标准差非常接近，分别为 0.77 和约 0.15；而 RPCD 的中位数为 0.60，标准差更大（0.25）。这一差异说明 RPCD 对整体美学偏好谱系的刻画更为丰富，能够说明图像在高、低情感分数处为何得到某一特定分数。

<!-- [原子块 · object]  -->

**EN** Figure 7: Boxplots of sentiment score distributions for the three considered datasets, namely AVA, PCCD and our RPCD.

**ZH** 图 7：AVA、PCCD 与本文 RPCD 三个数据集情感分数分布的箱线图。

**EN** Figure 8 reports some samples of the AVA dataset whose aesthetic score given by the human raters is equal to 5 (i.e., average score of the distribution), while our sentiment score span almost the entire range. It can be seen that the comments concern different aspects of photography. For example, for the central image a user has concerns about the pose of the subject “I think this would have been much more effective if the flower was facing the camera.”, while another user would have preferred a different optical technique, i.e., “I would like more depth-of-field, so that the furthest petals are in focus also”. Sometimes there can be very conflicting opinions in the comments (see the first image on the left). In general, comments reveal many facets of judgment shaped by the polarity of sentiment. This therefore justifies the difference between the annotated aesthetic score and the estimated sentiment score.

**ZH** 图 8 给出了 AVA 数据集中的若干样本，人类评分者给出的美学分数均为 5（即分布的均值），而我们提出的情感分数几乎跨越整个区间。可以看到，评论涉及摄影的多个方面。例如，对中间那张图像，一位用户对主体姿态提出看法：“I think this would have been much more effective if the flower was facing the camera.”（我认为如果花朝向镜头，效果会好得多。），而另一位用户则更希望采用不同的光学技法：“I would like more depth-of-field, so that the furthest petals are in focus also”（我希望景深更大一些，让最远的花瓣也清晰）。评论中有时会出现截然相反的意见（见最左侧那张图像）。总体而言，评论揭示出由情感极性塑造的多面判断，这也解释了标注美学分数与估计情感分数之间存在差异的原因。

<!-- [原子块 · img]  -->

**EN** Figure 8: AVA samples annotated with an aesthetic score of 5, whose sentiment score we propose varies between 0.39 and 0.98. For each image we report the overall sentiment score (top of the image) and comments with the corresponding predicted sentiment score in bold.

**ZH** 图 8：标注美学分数为 5 的 AVA 样本，我们提出的情感分数在 0.39 到 0.98 之间变化。每张图像上方给出整体情感分数，各评论后以粗体标出其预测情感分数。

**EN** A.4 Content Analysis

**ZH** A.4 内容分析

**EN** We automatically analyze image content by using image classifiers for both semantic and composition aspects. In this section we detail the classifiers design and training and some qualitative results on our RPCD dataset.

**ZH** 我们使用图像分类器从语义与构图两方面自动分析图像内容。本节详述分类器的设计与训练，并给出在 RPCD 数据集上的部分定性结果。

**EN** Semantic Content and Composition Rule.

**ZH** 语义内容与构图规则。

**EN** To categorize the semantic content and composition of RPCD images, we use two classifiers based on the same backbone, namely the Vision Transformer (ViT) presented in [8]. In particular, we use the ViT parameters learned on ImageNet (keeping them freezed on the new tasks). The last linear classification layer is peculiar to each task and its parameters are trained. We use the same hyperparameters for the two classifiers, that is SGD with momentum equal to 0.9 and weight decay of 1⟦SLOT_40⟧-4. We train using batches of 32 images for 90 epochs with an initial learning rate of 0.01, that is then dropped every 30 epochs by a factor of 0.1.

**ZH** 为对 RPCD 图像的语义内容与构图分类，我们使用两个基于同一骨干网络的分类器，骨干即 [8] 提出的 Vision Transformer（ViT）。具体而言，我们采用在 ImageNet 上学习到的 ViT 参数（在新任务上保持冻结），仅训练各自任务特有的最后一层线性分类层。两个分类器使用相同超参数：动量 0.9、权重衰减 1⟦SLOT_40⟧-4 的 SGD；批大小 32 张图像，训练 90 轮，初始学习率 0.01，每 30 轮按 0.1 的因子衰减。

**EN** The semantic content classifier is trained to discriminate six different semantic content, namely Animal, Architecture, Human, Landscape, Plant, and Static. For this purpose, we use 15,981 images of the dataset CUHK-PQ [25] (i.e. all the images of the dataset apart from those of the Night category). We split the whole dataset int 80% training images and 20% test images. The resulting classifier achieved an accuracy of 87.08% on the test set. Figure 9 reports two images from RPCD for each semantic category.

**ZH** 语义内容分类器用于判别六类语义内容，即动物、建筑、人物、风景、植物与静物。为此，我们使用 CUHK-PQ [25] 数据集的 15,981 张图像（即去掉“夜景”类别后的全部图像），并按 80% 训练、20% 测试划分。所得分类器在测试集上达到 87.08% 的准确率。图 9 给出了 RPCD 中每个语义类别的两张图像。

<!-- [原子块 · table] Animal Architecture Human Landscape Plant Static -->

**EN** Figure 9: Images from our RCPD dataset categorized with respect to the semantic content.

**ZH** 图 9：按语义内容分类的 RCPD 数据集图像。

**EN** Our composition classifier is trained on the KU-PCP dataset [21], which consists of 4244 outdoor photographs. We exploit the data splits provided by the authors which comprise of a training set of 3169 images and 1075 validation images. Each image has been annotated by 18 human subject to categorize it into nine composition classes: Center, Curved, Diagonal, Horizontal, Pattern, Rule of Thirds (RoT), Symmetric, Triangle, and Vertical. Since an image may follow multiple composition rules, each sample is given with one or more (at most 3) composition labels. Following [13], images with more than one rule are trained multiple times for each ground-truth class. This training strategy is shown more effective than multi-label loss. The estimated accuracy on the test set is equal to 33.36%. Figure 10 shows some images from the RPCD categorized for each composition rule.

**ZH** 构图分类器在 KU-PCP 数据集 [21] 上训练，该数据集包含 4244 张户外照片。我们采用作者提供的数据划分，其中训练集 3169 张、验证集 1075 张。每张图像由 18 名受试者标注，归入九个构图类别：居中、曲线、对角、水平、图案、三分法（RoT）、对称、三角与垂直。由于一张图像可能同时遵循多条构图规则，每个样本带有 1 个或多个（最多 3 个）构图标签。沿用 [13] 的做法，含多条规则的图像会针对每个真值类别重复训练多次，这一训练策略被证明比多标签损失更有效。测试集上的准确率为 33.36%。图 10 给出了 RPCD 中各构图规则的样张。

<!-- [原子块 · table] Center Curved Diagonal Horizontal Pattern -->

<!-- [原子块 · table] RoT Symmetric Triangle Vertical -->

**EN** Figure 10: Images from our RCPD dataset categorized with respect to the main composition rule.

**ZH** 图 10：按主要构图规则分类的 RCPD 数据集图像。

**EN** Shot Scale.

**ZH** 景别。

**EN** We implement a Subject Guidance Network (SGNet) inspired by [32] to perform shot scale classification on images. The key idea is to use a subject map to determine the portion occupied by the subject with respect to the frame. We distinguish among five shot scale types, namely extreme close-up (ECS), close-up (CS), medium (MS), full (FS) and long (LS). The model is trained on the public MovieNet dataset [15] and optimized with stochastic gradient descent using cross-entropy loss. We use a learning rate of 1⟦SLOT_41⟧-3, batch size of 16 and we train for 60 epochs. We achieved 99.72⟦SLOT_42⟧ accuracy on the test set of the MovieNet dataset and observed a good generalization to the proposed RPCD dataset. The shot scale reveals information of how the photographer used the camera in order to emphasize either a location (long), an event (medium/full) or the identity of a subject (extreme close-up/close-up). Figure 11 reports some images annotated for each shot scale category.

**ZH** 我们实现了受 [32] 启发的主体引导网络（Subject Guidance Network, SGNet）来完成图像景别分类。其核心思想是利用主体图确定主体在画面中所占的比例。我们区分五种景别：极特写（ECS）、特写（CS）、中景（MS）、全景（FS）与远景（LS）。模型在公开的 MovieNet 数据集 [15] 上训练，以交叉熵损失和随机梯度下降优化，学习率 1⟦SLOT_41⟧-3、批大小 16、训练 60 轮。我们在 MovieNet 测试集上取得 99.72⟦SLOT_42⟧ 的准确率，并观察到其对本文 RPCD 数据集具有良好的泛化能力。景别揭示了摄影者如何运用相机来强调地点（远景）、事件（中景/全景）或主体身份（极特写/特写）。图 11 给出了各景别类别的标注样张。

<!-- [原子块 · table] ECS CS MS LS FS -->

**EN** Figure 11: Images from our RCPD dataset categorized with respect to the shot scale.

**ZH** 图 11：按景别分类的 RCPD 数据集图像。

**EN** Aesthetic Aspect Prediction.

**ZH** 美学维度预测。

**EN** The aesthetic aspect of each comment is predicted using a transformer model, DistilBERT, implemented using HugginFace’s transformers library [39]. This approach differs with previous attempts of automatically labeling the aesthetic attributes of comments, which were based on keywords [17]. Instead, we fine-tune the language model for the text classification task of predicting the aesthetic attribute of a text using the PCCD [5] dataset, where 7 different classes are available: general_impression, subject_of_photo, composition, use_of_camera, depth_of_field, color_lighting, and focus. We use a learning rate of 2⟦SLOT_43⟧-5, batch size of 16, weight decay of 0.01 and we train for 5 epochs. The rest of the parameters are left to the default ones in the HugginFace Trainer API. We randomly split the whole dataset in two folds: 90% for training, and the remaining 10% for validation and testing. Additionally, we clean URLs and escaped characters from the dataset. The fine-tuning converges at epoch 2, where the weighted metrics over the 7 different classes are: Precision, 0.8771; Recall, 0.8751; F1-score, 0.8755; and Accuracy, 0.8751.

**ZH** 每条评论的美学维度由一个 Transformer 模型 DistilBERT 预测，该模型通过 HugginFace 的 transformers 库 [39] 实现。这一做法不同于以往基于关键词自动标注评论美学属性的尝试 [17]：我们在 PCCD [5] 数据集上对语言模型做文本分类微调，以预测文本的美学属性，其中共有 7 个类别：general_impression（总体印象）、subject_of_photo（拍摄主体）、composition（构图）、use_of_camera（相机运用）、depth_of_field（景深）、color_lighting（色彩光照）与 focus（对焦）。学习率 2⟦SLOT_43⟧-5、批大小 16、权重衰减 0.01、训练 5 轮，其余参数沿用 HugginFace Trainer API 的默认值。我们将整个数据集随机划分为两份：90% 用于训练，其余 10% 用于验证与测试；此外还清洗了数据集中的 URL 与转义字符。微调在第 2 轮收敛，7 个类别上的加权指标为：精确率 0.8771、召回率 0.8751、F1 分数 0.8755、准确率 0.8751。

**EN** Figure 12 shows the correlation matrix of the classifier performance on the test set. The classifier is available on HuggingFace’s model hub 1212 12 https://huggingface.co/daveni/aesthetic_attribute_classifier.

**ZH** 图 12 给出了分类器在测试集上性能的相关矩阵。该分类器已在 HuggingFace 模型中心发布 1212 12 https://huggingface.co/daveni/aesthetic_attribute_classifier。

<!-- [原子块 · img]  -->

**EN** Figure 12: Correlation matrix of the aesthetic aspect classifier.

**ZH** 图 12：美学维度分类器的相关矩阵。

**EN** A.5 Explicit or offensive content

**ZH** A.5 露骨或冒犯性内容

**EN** We use Detoxify 1313 13 https://github.com/unitaryai/detoxify, a library to predict toxic comments, to carry out a preliminary analysis of the presence of offensive content in the dataset. We use the unbiased model, a model that recognizes toxicity and minimizes this type of unintended bias with respect to mentions of identities (for example, minimize the bias towards the toxic class when a mention to a minority, which are often the target of offensive comments, is mentioned and the comment is not actually offensive).

**ZH** 我们使用 Detoxify 1313 13 https://github.com/unitaryai/detoxify——一个用于预测毒性评论的库——对数据集中冒犯性内容的存在情况做初步分析。我们采用其中的 unbiased 模型，该模型在识别毒性的同时，尽量降低涉及身份指称时产生的此类非预期偏见（例如，当提及少数群体——后者常成为冒犯性评论的对象——但评论本身并无冒犯性时，尽量降低将其判为毒性类别的倾向）。

**EN** In Table 4 we show the results of this preliminary analysis of the presence of offensive content in the dataset using Detoxify to predict the "offensive probability" of the 216K comments in the dataset. We have considered a comment to be offensive if the predictions probability for any of the labels is higher than 0.5. In total, there are 8K comments with a predicted probability of being offensive greater that 0.5, which represent less than the 4% of the total of comments in the dataset.

**ZH** 表 4 给出了这项初步分析的结果：我们用 Detoxify 预测数据集中 216K 条评论的“冒犯概率”。若某条评论在任一标签上的预测概率高于 0.5，即判定为冒犯性。总计有 8K 条评论的冒犯预测概率大于 0.5，占数据集评论总数的不到 4%。

**EN** Table 4: Offensive content analysis of our RPCD using Detoxify.

**ZH** 表 4：使用 Detoxify 对本文 RPCD 的冒犯性内容分析。

<!-- [原子块 · table] Offensive label Predicted Probability Mean Total toxicity 2.889% 4369 severe_toxicity 0.019% 0 obscene 1.125% 2385 identity_attack 0.374% 336 insult 0.672% 742 threat 0.418% 287 sexual_explicit 0.259% -->

**EN** A.6 Topic Modeling

**ZH** A.6 主题建模

**EN** We use BERTopic [12] to clusterize the comments in all three datasets to compare the main topics being discussed. This method leverages on the document embeddings created using a text encoder to produce clusters after reducing the dimensionality of such embeddings. Then, TD-IDF is applied to the documents of the cluster to get the importance score of each word, obtaining the relevant topics in the cluster.

**ZH** 我们使用 BERTopic [12] 对三个数据集的评论做聚类，以比较其中讨论的主要主题。该方法利用文本编码器生成的文档嵌入，先对嵌入降维再进行聚类；随后对簇内文档施加 TD-IDF，得到每个词的重要性分数，从而提取出该簇的相关主题。

**EN** To generate the topics, we used the automatic topic reduction feature available in the library to reduce the number of topics, starting from the least frequent topic, as long as it exceeds a minimum similarity of 0.915. We additionally sample 100K comments from AVA and Reddit datasets to avoid memory constraints. We describe the datasets topics in the Table 5. It shows the top 30 topics together with the count of documents belonging to each of them and the most important words per topic. Topics related to aesthetic attributes are in bold. We observe that in all of them we can find topics regarding aesthetic aspects such as composition, exposure, focus or color; but also topics related to the subject of the image such as sky, bird or flower.

**ZH** 生成主题时，我们使用库中的自动主题缩减功能，从最不常见的主题开始合并，只要相似度超过 0.915 的最小值。为避免内存受限，我们还从 AVA 与 Reddit 数据集中各采样 100K 条评论。表 5 描述了各数据集的主题，列出前 30 个主题、各主题包含的文档数以及每类主题最重要的词，其中与美学属性相关的主题以粗体标出。可以看到，三个数据集中都能找到与构图、曝光、对焦、色彩等美学方面相关的主题，也有与天空、鸟、花等图像主体相关的主题。

**EN** Table 5: Top 30 detected Topics on AVA, PCCD, and our RPCD.

**ZH** 表 5：AVA、PCCD 与本文 RPCD 上检测出的前 30 个主题。

<!-- [原子块 · table] AVA PCCD RPCD Count Name Count Name Count Name 35798 focus_and_challenge_this 12585 the_and_of_to 43491 and_the_to_is 1417 her_she_face_shes 1256 hi_you_work_image 3441 her_she_face_hair 1170 flower_f -->

**EN** A.7 Informativeness Analysis

**ZH** A.7 信息量分析

**EN** We use the definition of informativeness score of a previous work [10] as a proxy of how meaningful are the comments in our dataset and how do they compare to other datasets. This definitions leverages on the relative frequency of unigrams and bigrams respect to the total vocabulary of the corpus. Then, a comment is represented as the union of its unigrams and bigrams and it is assigned an informativeness score ⟦SLOT_44⟧ as the average of the negative log probabilities of its unigrams (⟦SLOT_45⟧) and bigrams (⟦SLOT_46⟧):

**ZH** 我们沿用 [10] 中信息量分数的定义，以此衡量数据集评论的意义程度及与其他数据集的对比。该定义基于一元词与二元词相对语料总词表的频率：一条评论表示为其一元词与二元词的并集，其信息量分数 ⟦SLOT_44⟧ 定义为一元词（⟦SLOT_45⟧）与二元词（⟦SLOT_46⟧）负对数概率的平均值：

<!-- [原子块 · table] ρ = − 1 2 ​ [ l ​ o ​ g ​ ∏ i N P ⁡ ( u i ) + l ​ o ​ g ​ ∏ j M P ⁡ ( b j ) ] \rho=-\frac{1}{2}[log\prod_{i}^{N}P(u_{i})+log\prod_{j}^{M}P(b_{j})] (3) -->

**EN** The more frequent a word is, the less informative it will be. We observe that the proposed RPCD dataset have a slightly higher informativeness score than PCCD dataset, while both of them have a score twice as high as AVA dataset. The box plot shown in Figure 13 describes the informativeness score distribution among the different datasets, where the dataset with the highest average informativeness score is RPCD (78.61), followed by PCCD (72.96) and finally, with less than half the score, AVA (32.43).

**ZH** 一个词越常见，其信息量越低。我们观察到，RPCD 数据集的信息量分数略高于 PCCD，而二者均为 AVA 数据集的两倍左右。图 13 的箱线图展示了各数据集信息量分数的分布：平均信息量分数最高的是 RPCD（78.61），其次是 PCCD（72.96），最后是 AVA（32.43），不足前者的一半。

<!-- [原子块 · img]  -->

**EN** Figure 13: Informativeness score for each of the considered datasets.

**ZH** 图 13：各所考察数据集的信息量分数。

**EN** Appendix B Experiments and Implementation Details

**ZH** 附录 B 实验与实现细节

**EN** B.1 Image Aesthetic Assessment

**ZH** B.1 图像美学评估

**EN** AestheticViT.

**ZH** AestheticViT。

**EN** For ranking the images with respect to aesthetic or sentiment scores, we experiment with different models based on Vision Transformer (ViT) [8] as a baseline as this architecture has proved its effectiveness for several tasks. We run experiments with various versions of ViT in terms of model size (i.e., Tiny, Small, Base, and Large), input patch size, and pre-training dataset. In what follows we use brief notation to indicate the model size and the input patch size: for instance, ViT-L/16 means the “Large” variant with ⟦SLOT_47⟧ input patch size. We also consider the Data-efficient image Transformer (DeiT), a post-ViT model that improves the training process and performance.

**ZH** 为按美学分数或情感分数对图像排序，我们以 Vision Transformer（ViT）[8] 为基础模型开展实验——该架构已在多项任务中证明有效性。我们考察了模型规模（Tiny、Small、Base、Large）、输入 patch 大小与预训练数据集各不相同的多个 ViT 版本。下文用简记表示模型规模与输入 patch 大小，例如 ViT-L/16 指“Large”版本、输入 patch 大小为 ⟦SLOT_47⟧。我们还考察了 DeiT（Data-efficient image Transformer）——一个改进训练过程与性能的 post-ViT 模型。

**EN** On top of the pre-trained transformer, we add a fully-connected layer which is randomly initialized. The whole model is then trained to predict the final score using the mean square error as the loss function. We resize the input images to have the maximum input size of 700 pixels and adjust the other size to preserve the original aspect ratio. To handle images with varying resolutions, we scale input positional embedding accordingly with the image resolution by performing bilinear interpolation. During training we adopt a batch size of 1 because the images can have different resolutions. We finetune the models until convergence, for a maximum of 5 epochs (although convergence usually occurs on epoch 2 or 3). The learning rate is empirically set to 1⟦SLOT_48⟧-6 and we use Adam optimizer. We exploit the available model implementations and pre-trained weights of the PyTorch Image Models library1414 14 https://github.com/rwightman/pytorch-image-models.

**ZH** 在预训练 Transformer 之上，我们添加一个随机初始化的全连接层，随后以均方误差为损失函数训练整个模型预测最终分数。输入图像被缩放至最大边长 700 像素，另一边按比例调整以保持原始宽高比。为处理不同分辨率的图像，我们通过双线性插值按分辨率缩放输入的位置嵌入。训练时由于图像分辨率各异，批大小取 1。模型微调至收敛，最多 5 轮（尽管通常第 2 或第 3 轮即收敛）。学习率经验性设为 1⟦SLOT_48⟧-6，优化器为 Adam。我们使用 PyTorch Image Models 库1414 14 https://github.com/rwightman/pytorch-image-models 提供的模型实现与预训练权重。

**EN** We first perform experiments for estimating the aesthetic score of AVA [28] and PCCD [17] (i.e., the only two datasets with both comments and aesthetic scores). Table 6 reports performance on the test sets in terms of SRCC, and LCC for aesthetic score regression and accuracy for low-/high- aesthetic categorization. The accuracy is computed defining as high quality images those with an score above 5, and poor quality otherwise. The best results are achieved by the ViT-L/16 pre-trained on ImageNet-21k and other considerations can be made. First, the use of larger patches, that is ⟦SLOT_49⟧ pixels instead of ⟦SLOT_50⟧ pixels, causes a significant drop in performance for the same model size. In fact, we have that ViT-B/32 achieves 0.446 of SRCC, while ViT-B/16 obtains 0.759 of SRCC on AVA. Second, the performance increases as the model size grows. On AVA, the SRCC is equal to 0.725 for ViT-T/16 and 0.793 for ViT-L/16. Third, the DeiT models are slightly less performing than the basic ViT versions and pre-training on ImageNet-21k instead of ImageNet results in a minimal increase in results, i.e., about 0.02.

**ZH** 我们首先在 AVA [28] 与 PCCD [17]（即仅有的两个同时具备评论与美学分数的数据集）上估计美学分数。表 6 报告了测试集上美学分数回归的 SRCC 与 LCC，以及低/高美学分类的准确率。准确率的计算把分数高于 5 的图像定义为高质量，其余为低质量。最佳结果由在 ImageNet-21k 上预训练的 ViT-L/16 取得，此外还有几点观察。第一，在模型规模相同时，使用更大的 patch（即 ⟦SLOT_49⟧ 像素而非 ⟦SLOT_50⟧ 像素）会导致性能显著下降：在 AVA 上，ViT-B/32 的 SRCC 为 0.446，而 ViT-B/16 达到 0.759。第二，性能随模型规模增大而提升：在 AVA 上，ViT-T/16 的 SRCC 为 0.725，ViT-L/16 为 0.793。第三，DeiT 模型略逊于基础版 ViT，而在 ImageNet-21k 而非 ImageNet 上预训练带来的提升很小，约为 0.02。

**EN** Table 6: Comparison of various transformers for image aesthetic assessment on AVA and PCCD. In each column, the best and second-best results are marked in boldface and underlined, respectively.

**ZH** 表 6：多种 Transformer 在 AVA 与 PCCD 上做图像美学评估的对比。每列中最优与次优结果分别以粗体和下划线标出。

<!-- [原子块 · table] Model Pretrain dataset AVA PCCD SRCC LCC Acc. (%) SRCC LCC Acc. (%) DeiT-T/16 ImageNet 0.725 0.731 80.33 0.227 0.262 98.34 DeiT-S/16 ImageNet 0.746 0.750 80.90 0.289 0.296 98.34 DeiT-B/16 ImageNet 0.7 -->

**EN** Table 7 reports the comparison with state-of-the-art methods on the AVA dataset (for PCCD, there is no benchmark for aesthetic score assessment). Our ViT-L/16 pre-trained on ImageNet-21k (in the table named as ViT-L/16 - 21k) obtains better performance than Hosu et al. [14] for aesthetic score regression with an increment of 0.04 on both SRCC and LCC. On the other hand, we are in second place for the aesthetic classification with an accuracy of 0.35% lower than Chen et al. [6]. Correlation metrics are more adequate than accuracy [14], and exact score estimation is more challenging and representative of the full range of scores. Therefore, we can claim that we have achieved an excellent result.

**ZH** 表 7 给出了与当前最优方法在 AVA 数据集上的对比（PCCD 没有美学分数评估的基准）。我们的 ViT-L/16 - ImageNet-21k 预训练版本（表中记为 ViT-L/16 - 21k）在美学分数回归上优于 Hosu 等人 [14]，SRCC 与 LCC 各提升 0.04；在美学分类上排名第二，准确率比 Chen 等人 [6] 低 0.35%。如 [14] 所指出的，相关性指标比准确率更合适，精确估计分数更具挑战性，也更能代表整个分数区间。因此，我们可以说取得了出色的结果。

**EN** Table 7: Comparison of our baseline with state-of-the-art methods on the AVA dataset for image aesthetic assessment. In each column, the best and second-best results are marked in boldface and underlined, respectively. The “–” means that the result is not available.

**ZH** 表 7：本文基线方法与当前最优方法在 AVA 数据集上做图像美学评估的对比。每列中最优与次优结果分别以粗体和下划线标出。“–”表示结果不可得。

<!-- [原子块 · table] Model SRCC LCC Accuracy (%) Murray et al . [ 28 ] – – 66.70 Lu et al . [ 24 ] – – 74.46 Ma et al . [ 26 ] – – 81.70 Kong et al . [ 20 ] 0.558 – 77.33 Talebi et al . [ 37 ] 0.612 0.636 81.51 Chen et al -->

**EN** We perform experiments considering the previous backbones, apart from ViT-B/32 which produced the worst results, for the sentiment score estimation. Results on AVA, PCCD and our RPCD are reported in Table 8. We observe the same behavior as the aesthetic assessment, that the larger models outweigh the smaller ones. We also point out that ViT-L/16 - 21k achieves slightly higher performance than ViT-L/16 on AVA, vice versa on RPCD. Finally, on PCCD we get the worst results in terms of correlation and the best results for classification compared to the other two datasets.

**ZH** 我们在情感分数估计上使用了上述骨干网络，但去掉了结果最差的 ViT-B/32。在 AVA、PCCD 与本文 RPCD 上的结果见表 8。我们观察到与美学评估相同的规律：大模型优于小模型。我们还指出，ViT-L/16 - 21k 在 AVA 上略优于 ViT-L/16，而在 RPCD 上恰好相反。最后，在 PCCD 上，相比另外两个数据集，我们得到的相关性结果最差，而分类结果最好。

**EN** Table 8: Results obtained using ViT for estimating the sentiment score on AVA, PCCD, and RPCD. In each column, the best and second-best results are marked in boldface and underlined, respectively.

**ZH** 表 8：使用 ViT 估计 AVA、PCCD 与 RPCD 上情感分数的结果。每列中最优与次优结果分别以粗体和下划线标出。

<!-- [原子块 · table] Model AVA PCCD RPCD SRCC LCC Acc. (%) SRCC LCC Acc. (%) SRCC LCC Acc. (%) DeiT-T/16 0.492 0.507 90.46 0.187 0.220 93.87 0.188 0.189 64.68 DeiT-S/16 0.500 0.513 90.48 0.170 0.182 93.87 0.190 0.189 64.6 -->

**EN** ViT + Linear probe.

**ZH** ViT + 线性探针。

**EN** The goal of this experiments is to assess to what extent the results obtained to predict the aesthetic and sentiment scores are due to the knowledge already present in the pre-trained model. We use the pre-trained ViT models as feature extractors and then we fit a linear regressor on those extracted features to predict the aesthetic score. This linear regressor was implemented as a Stochastic Gradient Descent Regressor with Scikit-Learn [30]. In Table 9 are reported the results for image aesthetic assessment on AVA and PCCD.

**ZH** 该实验旨在评估：预测美学分数与情感分数的结果在多大程度上源自预训练模型中已有的知识。我们把预训练 ViT 模型当作特征提取器，再在提取的特征上拟合一个线性回归器来预测美学分数；该回归器用 Scikit-Learn [30] 实现的随机梯度下降回归器。表 9 给出了在 AVA 与 PCCD 上做图像美学评估的结果。

**EN** Table 9: Results obtained by using ViT as a feature extractor followed by a linear regressor (we called ViT + Linear probe) for estimating the aesthetic score on AVA and PCCD. In each column, the best and second-best results are marked in boldface and underlined, respectively.

**ZH** 表 9：以 ViT 为特征提取器、后接线性回归器（我们称之为 ViT + 线性探针）估计 AVA 与 PCCD 上美学分数的结果。每列中最优与次优结果分别以粗体和下划线标出。

<!-- [原子块 · table] Model AVA PCCD SRCC LCC Acc. (%) SRCC LCC Acc. (%) DeiT-T/16 0.345 0.355 71.66 0.185 0.191 98.34 DeiT-S/16 0.454 0.459 74.27 0.212 0.203 98.34 DeiT-B/16 0.506 0.510 74.89 0.203 0.205 98.22 ViT-S/16 0. -->

**EN** Table 10 presents the results of the same experiment but using the sentiment score instead. Table 11 and Table 12 show the difference in performance between the trained models and the linear probe experiments. We can observe how for every case and every metric (except for the accuracy of Vit-S and ViT-L-21k on PCCD dataset to predict the aesthetic score), training the models outperform the pre-trained models (linear probes). The increase in performance is higher on AVA dataset, while PCCD and RPCD datasets do not benefit that much of further training. This may suggest that there is room for better training procedures on this datasets.

**ZH** 表 10 给出了同一实验在以情感分数为目标时的结果。表 11 与表 12 展示了训练所得模型与线性探针实验之间的性能差异。可以看到，除了 ViT-S 与 ViT-L-21k 在 PCCD 数据集上预测美学分数的准确率外，在每种情形与每个指标上，训练模型都优于预训练模型（线性探针）。性能提升在 AVA 数据集上更明显，而 PCCD 与 RPCD 数据集从进一步训练中获益不多，这可能意味着这些数据集上还存在改进训练流程的空间。

**EN** Table 10: Results obtained by using ViT as a feature extractor followed by a linear regressor (we called ViT + Linear probe) for estimating the sentiment score on the three considered datasets. In each column, the best and second-best results are marked in boldface and underlined, respectively.

**ZH** 表 10：以 ViT 为特征提取器、后接线性回归器（我们称之为 ViT + 线性探针）估计三个所考察数据集上情感分数的结果。每列中最优与次优结果分别以粗体和下划线标出。

<!-- [原子块 · table] Model AVA PCCD RPCD SRCC LCC Acc. (%) SRCC LCC Acc. (%) SRCC LCC Acc. (%) DeiT-T/16 0.238 0.235 90.26 0.153 0.151 93.87 0.107 0.108 62.56 DeiT-S/16 0.300 0.303 90.27 0.139 0.135 93.40 0.128 0.128 63.0 -->

**EN** Table 11: Performance difference between ViT + Linear Probe and Aesthetic ViT (Table 6 - Table 9) for aesthetic score.

**ZH** 表 11：ViT + 线性探针与 Aesthetic ViT 在美学分数上的性能差异（表 6 − 表 9）。

<!-- [原子块 · table] Model AVA PCCD SRCC LCC Acc. (%) SRCC LCC Acc. (%) DeiT-T/16 +0.380 +0.376 +8.670 +0.042 +0.071 +0.000 DeiT-S/16 +0.292 +0.291 +6.630 +0.077 +0.093 +0.000 DeiT-B/16 +0.259 +0.258 +7.060 +0.000 +0.000  -->

**EN** Table 12: Performance difference between ViT + Linear Probe and Aesthetic ViT (Table 8 - Table 10) for sentiment score.

**ZH** 表 12：ViT + 线性探针与 Aesthetic ViT 在情感分数上的性能差异（表 8 − 表 10）。

<!-- [原子块 · table] Model AVA PCCD RPCD SRCC LCC Acc. (%) SRCC LCC Acc. (%) SRCC LCC Acc. (%) DeiT-T/16 +0.254 +0.272 +0.200 +0.034 +0.069 +0.000 +0.081 +0.081 +2.120 DeiT-S/16 +0.200 +0.210 +0.210 +0.031 +0.047 +0.470 + -->

**EN** NIMA.

**ZH** NIMA。

**EN** We compare the previous ViT models with a model from the literature, i.e., NIMA [37], for sentiment score prediction. NIMA is trained by us using the code released by its authors. We use an ImageNet-trained VGG-16 as the backbone. Input images are resized to a fixed spatial resolution of ⟦SLOT_51⟧ pixels. As in [37], for model optimization we exploit the Earth Mover’s Distance (EMD):

**ZH** 我们将上述 ViT 模型与文献中的 NIMA [37] 在情感分数预测上做比较。NIMA 由我们使用作者发布的代码训练，骨干为在 ImageNet 上训练的 VGG-16，输入图像缩放至固定的 ⟦SLOT_51⟧ 像素空间分辨率。与 [37] 一致，模型优化采用 Earth Mover's Distance（EMD）：

<!-- [原子块 · table] E ​ M ​ D ​ ( 𝗊 ^ , 𝗊 ) = ( 1 N ​ ∑ k = 1 N | C ​ D ​ F 𝗊 ^ ​ ( k ) − C ​ D ​ F 𝗊 ​ ( k ) | r ) 1 r , EMD(\mathsf{\hat{q}},\mathsf{q})=\left(\frac{1}{N}\sum_{k=1}^{N}{|CDF_{\mathsf{\hat{q}}}(k)-CDF_{\ -->

**EN** where ⟦SLOT_52⟧ and ⟦SLOT_53⟧ are the ground-truth and the predicted score distributions, respectively. Finally, ⟦SLOT_54⟧ is the cumulative distribution function, ⟦SLOT_55⟧ equal to 2 is used to penalize the Euclidean distance between the CDFs. We use the probability distribution on the three sentiment polarity classes ⟦SLOT_56⟧ as ground-truth. We optimize the model by using Stochastic Gradient Descent (SGD) with learning rate of 5⟦SLOT_57⟧-3 and batch size equal to 64 for 100 epochs. We use an early stopping policy based on validation loss with a patience term of 10 epochs.

**ZH** 其中 ⟦SLOT_52⟧ 与 ⟦SLOT_53⟧ 分别为真值与预测的分数分布，⟦SLOT_54⟧ 为累积分布函数，⟦SLOT_55⟧ 取 2 用于惩罚两个 CDF 之间的欧氏距离。我们以三分类情感极性上的概率分布 ⟦SLOT_56⟧ 作为真值。模型用随机梯度下降（SGD）优化，学习率 5⟦SLOT_57⟧-3、批大小 64、训练 100 轮，并采用基于验证损失、耐心值 10 轮的早停策略。

**EN** Summary.

**ZH** 小结。

**EN** Experiments with ViT + Linear probe have shown that pre-trained ViTs for image recognition do not work well for predicting aesthetic and sentiment scores. It is therefore necessary to train the model to learn the characteristics that best encode the various aspects of aesthetics. Table 11 and Table 12 report the difference in performance between ViT + Linear prob and AestheticViT models for aesthetic score estimation and sentiment score estimation, respectively. This way we highlight the gain obtained thanks to the training of the backbones.

**ZH** ViT + 线性探针实验表明，面向图像识别的预训练 ViT 在预测美学分数与情感分数上表现不佳，因此有必要训练模型去学习最能编码美学各方面特性的表征。表 11 与表 12 分别给出 ViT + 线性探针与 AestheticViT 模型在美学分数估计与情感分数估计上的性能差异，由此凸显训练骨干网络所带来的增益。

**EN** Among the various tested models, ViT-L/16 - 21k achieved the best results on both AVA and PCCD for aesthetic assessment. It also outperforms state-of-the-art aesthetic assessment methods on the AVA dataset. On the other hand, for the prediction of the sentiment score the ViT-L/16 model obtained the best performance regardless of the dataset used for pre-training.

**ZH** 在测试的多个模型中，ViT-L/16 - 21k 在 AVA 与 PCCD 的美学评估上均取得最佳结果，并在 AVA 数据集上超越了当前最优的美学评估方法。另一方面，在情感分数预测上，无论预训练数据集为何，ViT-L/16 都取得了最佳性能。

**EN** B.2 Image Aesthetic Critique Generation

**ZH** B.2 图像美学评论生成

**EN** We verify the use of the proposed dataset for the generation of aesthetic image critique by using Bootstrapping Language Image Pre-training (BLIP) [22]. It is a method for the unified understanding and generation of the visual language. A pre-trained ViT-B/16 on the COCO dataset is finetuned for aesthetic captioning by exploiting the AdamW optimizer with initial learning rate equal to 1⟦SLOT_58⟧-5, weight decay of 0.05, and a cosine learning rate schedule. We train for 5 epochs using a batch size of 16 samples. During inference, we use beam search with a beam size of 3, and set the minimum and maximum generation lengths as 20 and 50, respectively.

**ZH** 我们使用 Bootstrapping Language Image Pre-training（BLIP）[22] 验证本数据集在美学图像评论生成上的用途。BLIP 是一种统一视觉语言理解与生成的方法。我们用在 COCO 数据集上预训练的 ViT-B/16，采用 AdamW 优化器微调以完成美学描述生成，初始学习率 1⟦SLOT_58⟧-5、权重衰减 0.05、余弦学习率调度，批大小 16 个样本训练 5 轮。推理时采用束搜索，束宽为 3，生成长度的最小值与最大值分别设为 20 和 50。

**EN** Appendix C Resources Used

**ZH** 附录 C 所用计算资源

**EN** In this section we briefly list the resources used to carry out this work:

**ZH** 本节简要列出开展本工作所使用的资源：

**EN** • Host machines: The machines used by the authors, each of them with access to a GPU NVIDIA GeForce RTX 2080 Ti.

**ZH** • 主机：作者使用的机器，每台可访问一块 NVIDIA GeForce RTX 2080 Ti GPU。

**EN** • Access to internal cluster1515 15 https://scicomp.ethz.ch/wiki/Euler with access to various instances with the following GPUs: NVIDIA GeForce RTX 2080 Ti and NVIDIA TITAN RTX.

**ZH** • 内部集群1515 15 https://scicomp.ethz.ch/wiki/Euler 的使用权限，可访问配备以下 GPU 的多种实例：NVIDIA GeForce RTX 2080 Ti 与 NVIDIA TITAN RTX。

**EN** • A part of the experiments, but not all, were logged to Weights & Biases1616 16 https://wandb.ai/, which registered the time used for those experiments, summing up a total of 2500 hours.

**ZH** • 部分（非全部）实验记录到 Weights & Biases1616 16 https://wandb.ai/，该系统记录了这些实验的耗时，累计 2500 小时。

**EN** Appendix D Ethical considerations

**ZH** 附录 D 伦理考量

**EN** This section comments on the Ethics Guidelines 1717 17 https://nips.cc/public/EthicsGuidelines of NeuroIPS. In particular, we comment on various of the points brought on this guidelines:

**ZH** 本节针对 NeuroIPS 伦理指南 1717 17 https://nips.cc/public/EthicsGuidelines 作出说明，具体回应其中的若干要点：

**EN** • Personally identifiable information and data collection. The samples in our dataset are attached to the user ID. While this provides a first level of anonymity to the users, it is fairly straight forward to access the public user profile, which may contain identifiable information the user had previously agreed to share and may be identifiable. Every user consents the collection of this information and accepts the Reddit’s Privacy Policy 1818 18 https://www.reddit.com/policies/privacy-policy, where it is stated that "[…] Reddit also allows third parties to access public Reddit content via the Reddit API and other similar technologies. […]". Thus, not every user has been directly asked for consent to include data produced by them in this dataset, but this consent is comprised under the Privacy Policy and the Reddit API terms of Use. We expand on this in the Section F. However, we point out that, a priori, disclosing that a person has any activity or belongs to the r/photocritique subreddit does not involve degrading or embarrassing such person.

**ZH** • 个人身份信息与数据采集。数据集样本与用户 ID 绑定。虽然这为用户提供了第一层匿名性，但访问公开用户主页相当容易，而主页可能包含用户此前同意公开的、具有识别性的信息。每位用户都同意采集这些信息并接受 Reddit 隐私政策 1818 18 https://www.reddit.com/policies/privacy-policy，其中声明“[...] Reddit 也允许第三方通过 Reddit API 及其他类似技术访问公开的 Reddit 内容。[...]”。因此，我们并未逐一征求每位用户将其产生的数据纳入本数据集的同意，但该同意已包含在隐私政策与 Reddit API 使用条款之中。我们在 F 节对此作了展开说明。不过我们指出，事先来看，披露某人有活动或属于 r/photocritique 子版块，并不会使该人受到贬损或难堪。

**EN** • Data consent. As pointed out above, every user consents accepts the Reddit’s Privacy Policy, where it is stated that "[…] Reddit also allows third parties to access public Reddit content via the Reddit API and other similar technologies. […]". The use of Reddit as a source of data for a large variety of scientific research has had an important impact in several fields as described in The Pushshift Dataset work [2]. We acknowledge that there is not explicit consent of the users to use their data for scientific purposes. However, we considered this to be covered by Reddit’s Privacy Policy. Hence, instead of collecting and storing the metadata and data produced by users, we provide the identifiers necessary to access the data and the tools to construct the dataset.

**ZH** • 数据同意。如上所述，每位用户都同意接受 Reddit 隐私政策，其中声明“[...] Reddit 也允许第三方通过 Reddit API 及其他类似技术访问公开的 Reddit 内容。[...]”。如 The Pushshift Dataset 工作 [2] 所述，将 Reddit 作为数据来源用于各类科学研究已在多个领域产生重要影响。我们承认并未取得用户将其数据用于科学目的的明确同意，但认为这已为 Reddit 隐私政策所涵盖。因此，我们不采集和存储用户产生的元数据与数据，而是提供访问数据所需的标识符以及构建数据集的工具。

**EN** • Explicit content. Images may contain explicit content of people. The first of the community rules state 1. Post only photos you took. Do not post a photo unless you took it! […] Thus, it is assumed this rule implies that the user posting a new image is the owner of the photography and hence has the right to distribute it. The sensitive content is labeled as "NSFW" in the dataset.

**ZH** • 露骨内容。图像可能包含人物的露骨内容。社区规则第一条为“1. 只发布你自己拍摄的照片。除非是你拍的，否则不要发布！[...]”因此，可以认为该规则意味着发布新图像的用户是照片的所有者，从而有权分发该照片。敏感内容在数据集中被标记为“NSFW”。

**EN** • Bias against people of a certain gender, race, sexuality, or who have other protected characteristics. This is a multi-factor issue that must be addressed from different perspectives and is beyond the scope of the first analyses presented in this paper to show the usability of this new data source. For instance, questions such as the impact of gender, race or sexuality on the perceived aesthetics of an image or how these images are critiqued are completely out of the scope of this work. However, we must note and acknowledge the work of the team of moderators of the r/photocritique community. Not only they approve each of the posts published in the community, but it is clearly stated that inappropriate or disrespectful posts are banned. As stated in the rules of the community: Lewd comments or those deemed by the moderation team to be grossly inappropriate will result in a permanent ban. You have been warned.. And as stated in the critiques guidelines: We do not allow […] inappropriate/sexist/racist comments..

**ZH** • 针对特定性别、种族、性取向或具有其他受保护特征人群的偏见。这是一个多因素问题，需要从不同角度加以解决；本文旨在展示这一新数据源的可用性，首次分析并未涵盖该问题。例如，性别、种族或性取向对图像感知美学的影响，或这些图像如何被评论，都完全超出本文范围。不过，我们必须指出并认可 r/photocritique 社区版主团队的工作：他们不仅审核社区发布的每篇帖子，还明确规定不当或不尊重的帖子将被封禁。社区规则中写道：淫秽评论或被版主团队判定为极不妥当的评论将导致永久封禁，特此警告。评论指南中亦写明：我们不允许 [...] 不当/性别歧视/种族主义评论。

**EN** • Filtering of offensive content. Due to the scale of the dataset, it has not been feasible to double check every post complies with the community rules. However, we have included a preliminary analysis of the presence of offensive content in the dataset (See Appendix A.5), in which we found that the predicted offensive content in the comments of the dataset is under 4%.

**ZH** • 冒犯性内容的过滤。由于数据集规模庞大，逐一核查每篇帖子是否符合社区规则并不可行。不过，我们已对数据集中冒犯性内容的存在情况做了初步分析（见附录 A.5），发现数据集中评论被预测为冒犯性的比例低于 4%。

**EN** Appendix E License

**ZH** 附录 E 许可协议

**EN** We comply with Reddit User Agreement1919 19 https://www.redditinc.com/policies/user-agreement/, Reddit API terms of use 2020 20 https://docs.google.com/a/reddit.com/forms/d/e/1FAIpQLSezNdDNK1-P8mspSbmtC2r86Ee9ZRbC66u929cG2GX0T9UMyw/viewform and PushShift database Creative Commons License 2121 21 https://zenodo.org/record/3608135#.Yp3XEXZBw2w. In particular, we refer to the Section 2.d of Reddit API Terms of Use, which states: "User Content. Reddit user photos, text and videos ("User Content") are owned by the users and not by Reddit. Subject to the terms and conditions of these Terms, Reddit grants You a non-exclusive, non-transferable, non-sublicensable, and revocable license to copy and display the User Content using the Reddit API through your application, website, or service to end users. You may not modify the User Content except to format it for such display. You will comply with any requirements or restrictions imposed on usage of User Content by their respective owners, which may include "all rights reserved" notices, Creative Commons licenses or other terms and conditions that may be agreed upon between you and the owners." We do not provide access to any data directly, but a list of IDs associated with a post on Reddit. This information is then used to retrieve the images, comments and metadata using the provided tools after obtaining a license key for the official Reddit API. Moreover, we do not modify the original content by no means, while we provide the necessary tools to process the data and run the same experiments we carried out.

**ZH** 我们遵守 Reddit 用户协议1919 19 https://www.redditinc.com/policies/user-agreement/、Reddit API 2020 年使用条款 2020 20 https://docs.google.com/a/reddit.com/forms/d/e/1FAIpQLSezNdDNK1-P8mspSbmtC2r86Ee9ZRbC66u929cG2GX0T9UMyw/viewform 以及 PushShift 数据库的知识共享许可 2121 21 https://zenodo.org/record/3608135#.Yp3XEXZBw2w。我们特别参照 Reddit API 使用条款第 2.d 节，其中规定：“用户内容。Reddit 用户的照片、文本与视频（‘用户内容’）归用户所有，而非 Reddit 所有。在遵守本条款的前提下，Reddit 授予您一项非独占、不可转让、不可再许可且可撤销的许可，允许您通过 Reddit API 在您的应用、网站或服务中复制并向终端用户展示用户内容。除为展示目的进行格式调整外，您不得修改用户内容。您将遵守内容所有者对使用用户内容所施加的任何要求或限制，其中可能包括‘保留所有权利’声明、知识共享许可或用户与所有者之间约定的其他条款与条件。”我们不直接提供任何数据，仅提供与 Reddit 帖子关联的 ID 列表；在取得官方 Reddit API 许可密钥后，可据此用所提供的工具检索图像、评论与元数据。此外，我们绝不修改原始内容，只提供处理数据并复现我们所做实验的必要工具。

**EN** We release the dataset under the Creative Commons Attribution 4.0 International license.

**ZH** 我们以知识共享署名 4.0 国际许可协议发布该数据集。

**EN** Appendix F Datasheet for RPCD

**ZH** 附录 F RPCD 数据说明书

**EN** In this section we detail the datasheet presented in [9] for documenting the proposed dataset. Note that, while we do not provide any data other that the IDs associated to Reddit posts, we answer the questionnaire considering the constructed dataset resulted from using our code.

**ZH** 本节详述 [9] 提出的、用于记录所提数据集的数据表（datasheet）。需要说明：除 Reddit 帖子关联的 ID 外，我们不提供任何其他数据，因此问卷的回答是针对使用我们的代码所构建的数据集。

**EN** F.1 Motivation

**ZH** F.1 动机

**EN** • For what purpose was the dataset created? RPCD was created to drive the research progress in both image aesthetic assessment and aesthetic image captioning. The proposed dataset addresses the need for images acquired with modern acquisition devices and photo critiques that give a better understanding of how the aesthetic evaluation is carried out.

**ZH** • 数据集为何而创建？RPCD 的创建旨在推动图像美学评估与美学图像描述两个方向的研究进展。该数据集满足了如下需求：使用现代采集设备获取图像，并提供能更好解释美学评价如何开展的摄影评论。

**EN** • Who created this dataset (e.g., which team, research group) and on behalf of which entity (e.g., company, institution, organization)? This dataset was created by the authors on behalf of their respective institutions, ETH Media Technology Center and University of Milano-Biococca.

**ZH** • 数据集由谁创建（如哪个团队、研究组），代表哪个实体（如公司、机构、组织）？本数据集由作者代表各自机构创建，即 ETH 媒体技术中心与米兰比可卡大学（University of Milano-Biococca）。

**EN** • Who funded the creation of the dataset? The creation of this dataset was carried out as part of the Aesthetic Assessment of Image and Video Content project2222 22 https://mtc.ethz.ch/research/image-video-processing/aesthetics-assessment.html. The project is supported by Ringier, TX Group, NZZ, SRG, VSM, viscom, and the ETH Zurich Foundation on the ETH MTC side.

**ZH** • 数据集创建由谁资助？该数据集的创建是“图像与视频内容美学评估”项目2222 22 https://mtc.ethz.ch/research/image-video-processing/aesthetics-assessment.html 的一部分。在 ETH MTC 方面，该项目由 Ringier、TX Group、NZZ、SRG、VSM、viscom 与苏黎世联邦理工学院基金会支持。

**EN** F.2 Composition

**ZH** F.2 构成

**EN** • What do the instances that comprise the dataset represent (e.g., documents, photos, people, countries)? Each instance is represented as a tuple containing one image and several photo critiques, where the images are JPEG files and the photo critiques are in textual form.

**ZH** • 构成数据集的实例表示什么（如文档、照片、人物、国家）？每个实例表示为一个元组，包含一张图像与若干条摄影评论；图像为 JPEG 文件，摄影评论为文本形式。

**EN** • How many instances are there in total (of each type, if appropriate)? RPCD consists of 73,965 data instances. Specifically, there are 73,965 images and 219,790 photo critiques.

**ZH** • 总共有多少个实例（如适用，按类型分列）？RPCD 包含 73,965 个数据实例，具体为 73,965 张图像与 219,790 条摄影评论。

**EN** • Does the dataset contain all possible instances or is it a sample (not necessarily random) of instances from a larger set? The dataset contains all samples (posts) available at the moment of collection, from the origin of the forum until the moment of collection. Additionally, included posts had to meet the following criteria: – The post has at least an image which could be retrieved. – The post has at least one comment critiquing the image – The post is not a discussion thread, a type of post to encourage general discussion in the forum.

**ZH** • 数据集是否包含所有可能的实例，还是从更大集合中抽取的样本（未必随机）？数据集包含采集时刻论坛中可获得的全部样本（帖子），时间跨度从论坛创建直至采集时刻。此外，纳入的帖子需满足以下条件：– 帖子至少有一张可检索到的图像；– 帖子至少有一条评论该图像的评论；– 帖子不是讨论帖（一种鼓励论坛内一般性讨论的帖子类型）。

**EN** • What data does each instance consist of? Each data instance consists of an image and one or more textual photo critiques.

**ZH** • 每个实例包含哪些数据？每个数据实例由一张图像与一条或多条文本形式的摄影评论组成。

**EN** • Is there a label or target associated with each instance? If so, please provide a description. There is no label associated with each sample. However, in this work we propose a method to compute said label, which is calculated using the processing scripts.

**ZH** • 每个实例是否有关联的标签或目标？若有，请给出描述。每个样本没有关联标签。不过，本文提出了一种计算该标签的方法，它通过处理脚本计算得到。

**EN** • Is any information missing from individual instances? Some of the samples in the dataset might be missing at the moment of future retrievals due to the users removing the data from Reddit.

**ZH** • 单个实例是否存在信息缺失？由于用户可能从 Reddit 删除数据，数据集中部分样本在未来检索时可能会缺失。

**EN** • Are relationships between individual instances made explicit (e.g., users’ movie ratings, social network links)? Every image and comment in the dataset is associated with the user who created the post. Moreover, we build the tree of comments of the different users criticizing an image. However, the data is downloaded by using only the post IDs.

**ZH** • 实例之间的关系是否被显式给出（如用户的电影评分、社交网络链接）？数据集中每张图像与每条评论都关联到创建该帖子的用户；此外，我们还构建了不同用户评论同一张图像的评论树。不过，数据仅通过帖子 ID 下载。

**EN** • Are there recommended data splits (e.g., training, development/validation, testing)? We provide the data splits we used in our experiments in the repository and they are used to retrieve the posts we used, although we encourage the use of other splits. The splits were randomly generated to divide the dataset in 70% train, 10% validation and 20% test splits.

**ZH** • 是否有推荐的数据划分（如训练、开发/验证、测试）？我们在仓库中提供了实验所使用的数据划分，并用它们来检索所使用的帖子，但也鼓励使用其他划分。该划分随机生成，将数据集按 70% 训练、10% 验证、20% 测试划分。

**EN** • Are there any errors, sources of noise, or redundancies in the dataset? The source of data itself could be considered a source of noise. Additionally, we have not evaluated the case in which an image is posted by an user several times in different posts, although we consider this event to be non-existent or insignificant.

**ZH** • 数据集中是否存在错误、噪声来源或冗余？数据源本身即可视为一种噪声来源。此外，我们未评估同一用户在不同帖子中重复发布同一图像的情况，但认为这种情况不存在或影响可忽略。

**EN** • Is the dataset self-contained, or does it link to or otherwise rely on external resources (e.g., websites, tweets, other datasets)? The dataset links to resources available on Reddit and Pushshift. In particular, posts and their metadata (including the URLs to images) are retrieved from Pushshift, while the comments are retrieved directly from Reddit. There is no guarantee that the dataset will remain constant, as this depends on the users exercising their rights to remove their content from the dataset sources. For this same reason, there are not any archival versions of the complete dataset available online. In order to retrieve the dataset in the future, Reddit API credentials are needed. Please, refer to the instructions about how to obtain the credentials2323 23 https://www.reddit.com/wiki/api/.

**ZH** • 数据集是自包含的，还是链接到或依赖外部资源（如网站、推文、其他数据集）？数据集链接到 Reddit 与 Pushshift 上的资源：帖子及其元数据（包括图像 URL）从 Pushshift 检索，评论则直接从 Reddit 检索。数据集不保证保持不变，因为这取决于用户是否行使其从数据源删除内容的权利。同理，线上也没有完整数据集的归档版本。未来若要检索该数据集，需要 Reddit API 凭证，请参阅获取凭证的说明2323 23 https://www.reddit.com/wiki/api/。

**EN** • Does the dataset contain data that might be considered confidential (e.g., data that is protected by legal privilege or by doctor-patient confidentiality, data that includes the content of individuals’ non-public communications)? The dataset does not contain any confidential data as both images and comments are publicly available in Reddit.

**ZH** • 数据集是否包含可能被视为机密的数据（如受法律特权或医患保密保护的数据、包含个人非公开通信内容的数据）？数据集不包含任何机密数据，因为图像与评论在 Reddit 上均公开可查。

**EN** • Does the dataset contain data that, if viewed directly, might be offensive, insulting, threatening, or might otherwise cause anxiety? There are data samples depicting explicit nudity with aesthetics purposes, and we acknowledge that this may be problematic for some people. According to the subreddit rules, this content must be marked: "Not Suitable for Work (NSFW) must be marked. […] Please keep NSFW posts respectful. Nothing that would be considered pornography." For this reason, the dataset processing script creates a NSFW column in the dataframe to easily filter this content.

**ZH** • 数据集中是否有数据在被直接查看时可能令人感到冒犯、侮辱、威胁或引发焦虑？存在以美学为目的描绘裸露的数据样本，我们承认这可能对部分人群造成困扰。根据子版块规则，此类内容必须标记：“不适合在工作场所观看（NSFW）的内容必须标记。[...] NSFW 帖子请保持得体，不得包含可被视为色情的内容。”为此，数据集处理脚本会在数据框中创建 NSFW 列，便于过滤此类内容。

**EN** • Does the dataset relate to people? Yes, some of the images contain people or the main subject is a person.

**ZH** • 数据集是否涉及人物？是，部分图像包含人物，或主体是人物。

**EN** • Does the dataset identify any subpopulations (e.g., by age, gender)? No.

**ZH** • 数据集是否标识任何亚群体（如按年龄、性别）？否。

**EN** • Is it possible to identify individuals (i.e., one or more natural persons), either directly or indirectly (i.e., in combination with other data) from the dataset? All posts and comments are linked to users, which may be identifiable depending on the data made available by the user. Additionally, posts and comments may contain information linking to other social media which could serve to identify a certain user.

**ZH** • 是否可能从数据集中直接或间接（即结合其他数据）识别出个体（一个或多个自然人）？所有帖子与评论都关联到用户，而根据用户公开的信息，这些用户可能是可识别的。此外，帖子与评论可能包含指向其他社交媒体的信息，可用于识别特定用户。

**EN** • Does the dataset contain data that might be considered sensitive in any way (e.g., data that reveals racial or ethnic origins, sexual orientations, religious beliefs, political opinions or union memberships, or locations; financial or health data; biometric or genetic data; forms of government identification, such as social security numbers; criminal history)? The retrieved data might contain sensitive data publicly disclosed by the users. However, we do not expect this to be common at all, and we would be surprised that some kinds of sensitive information are present in the community (financial, health, biometric, genetic or governmental data).

**ZH** • 数据集是否包含任何可能被视为敏感的数据（如揭示种族或民族出身、性取向、宗教信仰、政治观点或工会成员身份、位置的数据；财务或健康数据；生物识别或基因数据；政府身份证明形式，如社会保险号；犯罪记录）？检索到的数据可能包含用户公开披露的敏感数据。不过，我们预计这种情况绝不常见，并且若社区中出现金融、健康、生物识别、基因或政府数据等类型的敏感信息，我们会感到意外。

**EN** F.3 Collection process

**ZH** F.3 采集流程

**EN** • How was the data associated with each instance acquired? The data was directly observable (posts in Reddit stored in Pushshift’s and Reddit’s servers).

**ZH** • 每个实例关联的数据是如何获取的？数据是直接可观测的（存储于 Pushshift 与 Reddit 服务器上的 Reddit 帖子）。

**EN** • What mechanisms or procedures were used to collect the data (e.g., hardware apparatus or sensor, manual human curation, software program, software API)? Software API to access both Reddit and Pushshift.

**ZH** • 采集数据使用了哪些机制或流程（如硬件装置或传感器、人工整理、软件程序、软件 API）？使用软件 API 访问 Reddit 与 Pushshift。

**EN** • If the dataset is a sample from a larger set, what was the sampling strategy (e.g., deterministic, probabilistic with specific sampling probabilities)? NA.

**ZH** • 若数据集是从更大集合中抽取的样本，采用的抽样策略是什么（如确定性抽样、按特定概率的概率抽样）？不适用。

**EN** • Who was involved in the data collection process (e.g., students, crowdworkers, contractors) and how were they compensated (e.g., how much were crowdworkers paid)? Nobody was involved in the data collection process since all data was already available and observable.

**ZH** • 谁参与了数据采集过程（如学生、众包工作者、承包商），其报酬如何（如众包工人的薪酬）？无人参与数据采集过程，因为所有数据本就公开可观测。

**EN** • Over what timeframe was the data collected? Tha data was collected in February 2022, and comprises posts and comments in the span from May 2009 (first posts in the subreddit) to February 2022 (collection date).

**ZH** • 数据采集的时间跨度如何？数据采集于 2022 年 2 月，涵盖 2009 年 5 月（子版块的首批帖子）至 2022 年 2 月（采集日期）之间的帖子与评论。

**EN** • Were any ethical review processes conducted (e.g., by an institutional review board)? No ethical review process was conducted previous to the ethical review of this conference.

**ZH** • 是否开展了伦理审查流程（如由机构审查委员会进行）？在本会议的伦理审查之前，未开展任何伦理审查流程。

**EN** • Does the dataset relate to people? Yes, but not exclusively.

**ZH** • 数据集是否涉及人物？是，但不仅限于人物。

**EN** • Did you collect the data from the individuals in question directly, or obtain it via third parties or other sources (e.g., websites)? Third party sources (Reddit and Pushshift).

**ZH** • 数据是直接从相关个体处采集，还是通过第三方或其他来源（如网站）获取？第三方来源（Reddit 与 Pushshift）。

**EN** • Were the individuals in question notified about the data collection? No.

**ZH** • 相关个体是否被告知了数据采集？否。

**EN** • Did the individuals in question consent to the collection and use of their data? According to Reddit’s Privacy Policy2424 24 https://www.reddit.com/policies/privacy-policy, which is accepted by every user upon registration, "Reddit also allows third parties to access public Reddit content via the Reddit API and other similar technologies." . Moreover, we note that no data from the users is made directly available in the dataset. It only contains the IDs of the posts and the tools to retrieve them from Reddit and Pushshift.

**ZH** • 相关个体是否同意采集并使用其数据？根据 Reddit 隐私政策2424 24 https://www.reddit.com/policies/privacy-policy（每位用户注册时即接受），“Reddit 也允许第三方通过 Reddit API 及其他类似技术访问公开的 Reddit 内容。”此外，我们指出数据集中并未直接提供用户的任何数据，只包含帖子 ID 以及从 Reddit 与 Pushshift 检索这些帖子的工具。

**EN** • If consent was obtained, were the consenting individuals provided with a mechanism to revoke their consent in the future or for certain uses? Users may remove their data from Reddit and Pushshift using their respective privacy enforcing mechanisms. Thus, they would be removing their data from the dataset.

**ZH** • 若已取得同意，是否为同意的个体提供了日后或针对特定用途撤回同意的机制？用户可使用 Reddit 与 Pushshift 各自的隐私保护机制删除其数据，从而将其数据从本数据集中移除。

**EN** • Has an analysis of the potential impact of the dataset and its use on data subjects (e.g., a data protection impact analysis) been conducted? As we note above, no data from the users is made directly available in the dataset. The dataset only contains the IDs of the posts and the tools to retrieve them from Reddit and Pushshift.

**ZH** • 是否针对数据集及其使用对数据主体的潜在影响开展过分析（如数据保护影响分析）？如前所述，数据集中并未直接提供用户的任何数据，只包含帖子 ID 以及从 Reddit 与 Pushshift 检索这些帖子的工具。

**EN** F.4 Processing/cleaning/labeling

**ZH** F.4 处理/清洗/标注

**EN** • Was any preprocessing/cleaning/labeling of the data done (e.g., discretization or bucketing, tokenization, part-of-speech tagging, SIFT feature extraction, removal of instances, processing of missing values)? We provide scrips to automatically process the downloaded raw posts. Only first level comments are kept, posts with no comments or whose image is no longer available are filtered.

**ZH** • 是否对数据进行过预处理/清洗/标注（如离散化或分桶、分词、词性标注、SIFT 特征提取、剔除实例、缺失值处理）？我们提供了脚本自动处理下载的原始帖子，只保留一级评论，过滤掉无评论或图像已失效的帖子。

**EN** • Was the "raw" data saved in addition to the preprocessed/cleaned/labeled data (e.g., to support unanticipated future uses)? The raw posts need to be downloaded for further processing.

**ZH** • 除预处理/清洗/标注后的数据外，是否保存了“原始”数据（以支持未来未预期的使用）？原始帖子需要下载后才能进一步处理。

**EN** • Is the software used to preprocess/clean/label the instances available? Yes. The software for downloading and preparing the dataset is available on our GitHub repository 2525 25 https://github.com/mediatechnologycenter/aestheval.

**ZH** • 用于预处理/清洗/标注实例的软件是否可用？是。用于下载与准备数据集的软件见我们的 GitHub 仓库 2525 25 https://github.com/mediatechnologycenter/aestheval。

**EN** F.5 Uses

**ZH** F.5 用途

**EN** • Has the dataset been used for any tasks already? RPCD is introduced and used in the paper Understanding Aesthetics with Language: A Photo Critique Dataset for Aesthetic Assessment.

**ZH** • 数据集是否已用于某些任务？RPCD 由论文《Understanding Aesthetics with Language: A Photo Critique Dataset for Aesthetic Assessment》提出并使用。

**EN** • Is there a repository that links to any or all papers or systems that use the dataset? Papers using RPCD will be listed on the PapersWithCode web page2626 26 https://paperswithcode.com/dataset/rpcd.

**ZH** • 是否有仓库收录使用该数据集的论文或系统？使用 RPCD 的论文将列于 PapersWithCode 网页2626 26 https://paperswithcode.com/dataset/rpcd。

**EN** • What (other) tasks could the dataset be used for? RPCD can be used for modelling works in the areas of knowledge retrieval and multimodal reasoning.

**ZH** • 数据集还可用于哪些（其他）任务？RPCD 可用于知识检索与多模态推理方向的建模研究。

**EN** • Is there anything about the composition of the dataset or the way it was collected and preprocessed/cleaned/labeled that might impact future uses? No, there are no known risks to the best of our knowledge.

**ZH** • 数据集的构成或其采集、预处理/清洗/标注方式是否存在可能影响未来使用的因素？据我们所知不存在已知风险。

**EN** • Are there tasks for which the dataset should not be used? RPCD should not be used for automatically judging a photographer’s skills based on the photo critiques. The latter, in fact, are to be understood as highly subjective judgments that depend on the emotions and background of the commentators and could go beyond the mere technical evaluation of the shot.

**ZH** • 是否存在不应使用该数据集的任务？RPCD 不应用于依据摄影评论自动评判摄影者的技术水平。后者应被理解为高度主观的判断，取决于评论者的情绪与背景，可能超出对拍摄本身的纯技术评价。

**EN** F.6 Distribution

**ZH** F.6 分发

**EN** • Will the dataset be distributed to third parties outside of the entity (e.g., company, institution, organization) on behalf of which the dataset was created? Yes, the dataset is made publicly accessible.

**ZH** • 数据集是否会分发给创建该数据集的实体（如公司、机构、组织）之外的第三方？是，该数据集公开可访问。

**EN** • How will the dataset will be distributed (e.g., tarball on website, API, GitHub)? See our GitHub repository 25 for downloading instructions. RPCD has the following DOI: 10.5281/zenodo.6985507.

**ZH** • 数据集将如何分发（如网站上的 tarball、API、GitHub）？下载说明见我们的 GitHub 仓库 25。RPCD 的 DOI 为：10.5281/zenodo.6985507。

**EN** • When will the dataset be distributed? RPCD will be released to the public in August 2022.

**ZH** • 数据集何时分发？RPCD 将于 2022 年 8 月公开发布。

**EN** • Will the dataset be distributed under a copyright or other intellectual property (IP) license, and/or under applicable terms of use (ToU)? We release the dataset under the Creative Commons Attribution 4.0 International license2727 27 https://creativecommons.org/licenses/by/4.0/.

**ZH** • 数据集是否将在版权或其他知识产权（IP）许可和/或适用使用条款（ToU）下分发？我们以知识共享署名 4.0 国际许可协议发布该数据集2727 27 https://creativecommons.org/licenses/by/4.0/。

**EN** • Have any third parties imposed IP-based or other restrictions on the data associated with the instances? No.

**ZH** • 是否有第三方对与实例关联的数据施加了基于知识产权或其他限制？否。

**EN** • Do any export controls or other regulatory restrictions apply to the dataset or to individual instances? No.

**ZH** • 数据集或单个实例是否适用出口管制或其他监管限制？否。

**EN** F.7 Maintenance

**ZH** F.7 维护

**EN** • Who is supporting/hosting/maintaining the dataset? RPCD is supported and maintained by ETH MTC and University of Milano-Bicocca. The post IDs are available on Zenodo, the posts are on Reddit and Pushshift, and the code for automatically retrieving the posts is on GitHub.

**ZH** • 谁在支持/托管/维护该数据集？RPCD 由 ETH MTC 与米兰比可卡大学支持和维护：帖子 ID 存放于 Zenodo，帖子存放于 Reddit 与 Pushshift，自动检索帖子的代码存放于 GitHub。

**EN** • How can the owner/curator/manager of the dataset be contacted (e.g., email address)? By emailing to {daniel.veranieto,clabrador}@inf.ethz.ch or luigi.celona@unimib.it. By opening an issue on our GitHub repository 25.

**ZH** • 如何联系数据集的所有者/管理者/负责人（如电子邮箱）？可发送邮件至 {daniel.veranieto,clabrador}@inf.ethz.ch 或 luigi.celona@unimib.it，也可在我们的 GitHub 仓库 25 上提交 issue。

**EN** • Is there an erratum? All changes to the dataset will be announced on our Zenodo repository 2828 28 https://doi.org/10.5281/zenodo.6985507.

**ZH** • 是否有勘误？数据集的所有变更都将在我们的 Zenodo 仓库 2828 28 https://doi.org/10.5281/zenodo.6985507 上公布。

**EN** • Will the dataset be updated (e.g., to correct labeling errors, add new instances, delete instances’)? All updates (if necessary) will be posted on our Zenodo repository 28.

**ZH** • 数据集是否会更新（如纠正标注错误、新增实例、删除实例）？所有更新（如有必要）都将发布在我们的 Zenodo 仓库 28 上。

**EN** • If the dataset relates to people, are there applicable limits on the retention of the data associated with the instances (e.g., were individuals in question told that their data would be retained for a fixed period of time and then deleted)? The data related to users is stored on Reddit and Pushshift servers, and their data retention policies apply.

**ZH** • 若数据集涉及人物，与实例关联的数据保留是否有适用限制（如是否告知相关个体其数据将保留固定期限后删除）？与用户相关的数据存储在 Reddit 与 Pushshift 的服务器上，适用其各自的数据保留政策。

**EN** • Will older versions of the dataset continue to be supported/hosted/maintained? All changes to the dataset will be announced on our Zenodo repository 28. Outdated versions will be kept around for consistency.

**ZH** • 旧版本数据集是否继续得到支持/托管/维护？数据集的所有变更都将在我们的 Zenodo 仓库 28 上公布，过时版本将保留以保证一致性。

**EN** • If others want to extend/augment/build on/contribute to the dataset, is there a mechanism for them to do so? Any extension/augmentation by an external party is allowed under the release license. The dataset could be easily extended with other communities and other time periods using the available scripts. In order to add the extended version to the existing repositories, please contact the authors.

**ZH** • 若他人希望扩展/增补/构建或贡献该数据集，是否有相应机制？在发布许可下，任何外部方都可进行扩展或增补。借助现有脚本，可以方便地用其他社区、其他时间段的样本扩展数据集。若希望将扩展版本加入现有仓库，请联系作者。
