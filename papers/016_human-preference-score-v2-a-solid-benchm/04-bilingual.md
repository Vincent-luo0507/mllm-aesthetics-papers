# 人类偏好分数 v2：评测文本到图像合成中人类偏好的可靠基准

> 原标题：Human Preference Score v2: A Solid Benchmark for Evaluating Human Preferences of Text-to-Image Synthesis
> 作者：Xiaoshi Wu, Yiming Hao, Keqiang Sun, Yixiong Chen, Feng Zhu, Rui Zhao, Hongsheng Li · arXiv:2306.09341 · 2023-06-15

<!-- [原子块 · verbatim] Human Preference Score v2: A Solid Benchmark for Evaluating Human Preferences of Text-to-Image Synthesis -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] Recent text-to-image generative models can generate high-fidelity images from text inputs, but the quality of these generated images cannot be accurately evaluated by existing evaluation metrics. To a -->

**EN** 1 Introduction

**ZH** 1 引言

**EN** Recent advances in text-to-image synthesis [22, 21, 23, 17, 2] have made it possible to generate high-fidelity images based on text prompts. However, images generated with different random seed often have varying quality, and previous works [32, 33, 10] demonstrate that popular metrics, such as Inception Score (IS) [25], Fréchet Inception Distance (FID) [7], and CLIP Score [20], do not correlate well with human preferences on these images. Therefore, human preference is an important but poorly tracked aspect of text-to-image generative models. To facilitate research in this area, we construct a large-scale dataset annotated with human preferences, namely Human Preference Dataset v2 (HPD v2). We also established a benchmark based on a preference prediction model, Human Preference Score v2 (HPS v2), which is trained on HPD v2, to validate algorithmic developments for human-aligned image synthesis.

**ZH** 文本到图像合成[22, 21, 23, 17, 2] 的最新进展已能基于文本提示词生成高保真图像。然而，用不同随机种子生成的图像质量往往参差不齐，而前人工作[32, 33, 10]表明，Inception Score（IS）[25]、弗雷歇 inception 距离（FID）[7] 和 CLIP Score [20] 等流行指标在这些图像上与人类偏好的相关性并不好。因此，人类偏好是文本到图像生成模型中一个重要却缺乏追踪的方面。为推动该方向的研究，我们构建了一个带人类偏好标注的大规模数据集——人类偏好数据集 v2（HPD v2），并在其上训练偏好预测模型人类偏好分数 v2（HPS v2），建立基准，用以检验面向人类对齐图像合成的算法进展。

<!-- [原子块 · object]  -->

**EN** Figure 1: Overview of this work. We firstly collect Human Preference Dataset v2 (HPD v2) and then train a preference prediction model, Human Preference Score v2 (HPS v2), on it.

**ZH** 图 1：本工作概览。我们先采集人类偏好数据集 v2（HPD v2），再在其上训练偏好预测模型人类偏好分数 v2（HPS v2）。

**EN** HPD v2 is a comprehensive dataset of human preferences comparing images from various sources, including 9 text-to-image generative models and the COCO Captions dataset [1]. It comprises 798k human-annotated pairwise comparisons of images generated from the same prompt, making it the largest dataset of its kind. The dataset addresses issues of bias that occurs in previous datasets [32, 33, 10]. The first type of bias derives from the image source. Previous datasets [32, 33, 10] mainly contain images generated from Stable Diffusion [23] and its variants. Therefore, we cannot verify whether the models trained and evaluated exclusively on these datasets can generalize to other image distributions. HPD v2 incorporates images generated from 9 recent models [2, 17, 3, 13, 39, 23, 4, 22], as well as real images from the COCO Captions dataset [1], enabling better evaluation on the generalization capability. Another source of bias is in text prompts. User-written prompts, such as prompts in DiffusionDB [31], often follow a specific organization of description plus several style words, where the style words often contain contradictions, making it harder for annotators to understand. (see Tab. 1 for examples) The style words are also highly biased, leading to issues in training and evaluation. To tackle this bias, we employ ChatGPT to remove style words and organize prompts into a clearly written sentence.

**ZH** HPD v2 是一个综合的人类偏好数据集，比较来自多种来源的图像，包括 9 个文本到图像生成模型和 COCO Captions 数据集[1]。它包含 798k 条人类标注的两两比较，比较对象是由同一提示词生成的图像，是同类数据集中规模最大的一个。该数据集还解决了此前数据集[32, 33, 10] 中存在的偏差问题。第一类偏差来自图像来源：此前的数据集[32, 33, 10] 主要包含由 Stable Diffusion [23] 及其变体生成的图像，因此我们无法验证仅在这些数据集上训练和评测的模型能否泛化到其他图像分布。HPD v2 纳入了 9 个近期模型[2, 17, 3, 13, 39, 23, 4, 22] 生成的图像，以及来自 COCO Captions 数据集[1] 的真实图像，从而能更好地评测泛化能力。另一类偏差来自文本提示词。用户撰写的提示词（如 DiffusionDB [31] 中的提示词）常遵循“描述 + 若干风格词”的固定结构，而风格词之间往往自相矛盾，使标注者更难理解（示例见表 1）。这些风格词本身也带有很强偏差，给训练和评测带来问题。为消除这类偏差，我们用 ChatGPT 去除风格词，并把提示词整理成一句书写清晰的句子。

**EN** Based on HPD v2, a preference prediction model, Human Preference Score v2 (HPS v2), is trained to score generated images based on its likelihood to be preferred by humans. Experiments show that HPS v2 generalizes better than previous models, including HPS v1 [32], ImageReward [33] and PickScore [10].

**ZH** 基于 HPD v2，我们训练了偏好预测模型人类偏好分数 v2（HPS v2），用以按图像受人类偏好的可能性对生成图像打分。实验表明，HPS v2 的泛化能力优于此前模型，包括 HPS v1 [32]、ImageReward [33] 和 PickScore [10]。

**EN** We further study how to evaluate text-to-image generative models using HPS v2, and set up a benchmark for them. This is mainly about choosing a proper set of prompts. Pick-a-Pic [10] proposes to use prompt in its dataset. However, they did not study which set of prompts to choose, and how many prompts need to be included. DrawBench is a list of prompts introduced in Imagen [24], but we find that it is not large enough for stable evaluation. DiffusionDB [31] is a large scale database of user-written prompts and images generated from them. However, a large portion of these prompts are biased towards certain dataset-specific style words, and is not fair for models trained with other data. To mitigate this issue, we use ChatGPT to clean prompts from DiffusionDB [31]. We carefully study the number of prompts for evaluation to ensure that the average score is statistically stable. Finally, we obtain 4 lists of prompts for evaluation and benchmarking, which are categorized by styles: “Animation”, “Concept-art”, “Painting”, and “Photo”.

**ZH** 我们进一步研究如何用 HPS v2 评测文本到图像生成模型，并为其建立基准，核心在于选定合适的提示词集合。Pick-a-Pic [10] 提出使用其数据集中的提示词，但并未研究应选取哪一组提示词、以及需要包含多少条。DrawBench 是 Imagen [24] 中给出的一组提示词，但我们发现其规模不足以支撑稳定的评测。DiffusionDB [31] 是一个包含大量用户撰写提示词及其生成图像的大型数据库，但其中相当一部分提示词偏向某些数据集特有的风格词，对用其他数据训练的模型并不公平。为缓解这一问题，我们用 ChatGPT 清洗 DiffusionDB [31] 的提示词，并仔细研究了评测所用提示词的数量，以保证平均分在统计上稳定。最终我们得到 4 组用于评测与基准的提示词，按风格划分为“Animation”、“Concept-art”、“Painting”和“Photo”。

**EN** We also show that HPS v2 is sensitive to algorithmic improvements. Firstly, we evaluate the effectiveness of a straightforward test-time trick of blending the input noise for a diffusion model with a prior image. We also conduct experiments to validate the quantitative improvements of a method proposed by Wu et al. [32]. Our experiments show that HPS v2 is sensitive to algorithmic improvements, and can be used to evaluate text-to-image generative models.

**ZH** 我们还展示了 HPS v2 对算法改进的敏感性。首先，我们评测了一项简单的测试时技巧的有效性：把扩散模型的输入噪声与一幅先验图像混合。我们也做了实验，验证 Wu 等人[32] 所提方法的量化改进。实验表明 HPS v2 对算法改进敏感，可用于评测文本到图像生成模型。

**EN** Our contributions are as follows: 1) HPD v2, a large-scale, well-annotated dataset for researches of human preferences on images generated by text-to-image generative models. 2) HPS v2, a better human preference prediction model against existing ones, for which we show several example usages to demonstrate its sensitivity and accuracy. 3) A fair, stable and easy-to-use set of evaluation prompts for text-to-image generative models.

**ZH** 本文贡献如下：1) HPD v2，一个大规模、标注精良的数据集，用于研究人类对文本到图像生成模型所生成图像的偏好；2) HPS v2，一个优于现有模型的偏好预测模型，我们给出若干用例以展示其敏感性与准确性；3) 一套公平、稳定且易用的文本到图像生成模型评测提示词集合。

**EN** 2 Related Work

**ZH** 2 相关工作

**EN** 2.1 Text-to-image generative models

**ZH** 2.1 文本到图像生成模型

**EN** Text-to-image generative models enable users to create images based on textual input. DALL·E [22] was the first to achieve high-quality open-domain text-to-image generation. Since then, various architectures and modeling have been explored to enhance image quality. These include autoregressive models [22, 2], GANs [27], and diffusion models [23, 21, 24]. Among them, diffusion models have demonstrated superior computational efficiency and the ability to produce high-quality samples [21]. However, despite the capability of current text-to-image diffusion models to generate high-fidelity images, they often fail to align well with human preferences. Recent researches in this field has attempted to improve the image quality of diffusion models [32, 11], but the evaluation of these improvements remains challenging due to the lack of appropriate metrics and benchmarks. Therefore, there is a need to develop new evaluation metrics and benchmarks to effectively validate algorithmic enhancements.

**ZH** 文本到图像生成模型让用户能够基于文本输入创作图像。DALL·E [22] 首次实现了高质量的开放域文本到图像生成。此后，人们探索了多种结构与建模方式来提升图像质量，包括自回归模型[22, 2]、GAN [27] 和扩散模型[23, 21, 24]。其中扩散模型展现出更优的计算效率和生成高质量样本的能力[21]。然而，尽管当前的文本到图像扩散模型已能生成高保真图像，它们往往仍不能很好地契合人类偏好。该领域近期研究尝试提升扩散模型的图像质量[32, 11]，但由于缺乏合适的指标与基准，这些改进的评测依然困难。因此需要新的评测指标与基准，以有效验证算法上的增强。

**EN** 2.2 Image quality evaluation for generative models

**ZH** 2.2 生成模型的图像质量评测

**EN** Inception Score (IS) [25] and Fréchet Inception Distance (FID) [7] are widely used in the evaluation of image generative models. However, they do not correlate well with human preferences for images generated by recent text-to-image models [10, 32]. LPIPS [36] measures perceptual similarity between image pairs by fitting a pretrained model on a dataset of human perception on similarity. Similar methodology is used in HYPE [38] for evaluating generated human faces. Several recent works [32, 33, 10] propose to fine-tune visual-language models (VLM) on human choices on images generated with the same prompt, and use fine-tuned VLMs to serve as proxies for human evaluation, but these models are tuned exclusively on images from Stable Diffusion [23] and its variants, their generalization capabilities are not yet validated.

**ZH** Inception Score（IS）[25] 与弗雷歇 inception 距离（FID）[7] 被广泛用于图像生成模型的评测，但它们与人类对近期文本到图像模型所生成图像的偏好相关性不佳[10, 32]。LPIPS [36] 通过在人类相似度感知数据集上拟合预训练模型，度量图像对之间的感知相似度；HYPE [38] 用类似方法评测生成的人脸。近来的若干工作[32, 33, 10] 提出在“同一提示词生成图像上的人类选择”数据上微调视觉语言模型（VLM），并用微调后的 VLM 作为人类评测的代理；但这些模型只在 Stable Diffusion [23] 及其变体的图像上调优，其泛化能力尚未得到验证。

**EN** 2.3 Image quality dataset

**ZH** 2.3 图像质量数据集

**EN** AVA [16] is a dataset of human ratings given to photographs. Similar to AVA, Simulacra [19] collects human ratings, but instead for images generated from text. Both AVA and Simulacra are datasets of image ratings, which are absolute scores for images. They have been used to train the Aesthetic Score Predictor [28], which participates in the data cleaning pipeline of Stable Diffusion [23]. InstructGPT [18] proposes to align a pre-trained language model with human feedback. The idea of Reinforcement Learning from Human Feedback (RLHF) is also explored for visual content creation [11, 32]. This requires comparison between images generated from the same prompt. HPD v1 [32] was collected under this context, and it improves the image quality by aligning text-to-image models with human preference. Similar to HPD v1, ImageReward [33] and Pick-a-Pic [10] are datasets of comparison between paired images, focusing on evaluation of generated images. AGIQA-1K [37] and AGIQA-3K [12] are collected similarly, but the dataset size is considerably smaller. Our HPD v2 includes more images from a wider range of sources than existing works, enabling a more comprehensive evaluation of these preference prediction models. A head-to-head comparison with other datasets is presented in Tab. 5. Fake2M [15] is another related dataset that focuses on visual Turing test of distinguishing generated images.

**ZH** AVA [16] 是一个针对照片的人类评分数据集。与 AVA 类似，Simulacra [19] 也收集人类评分，但对象是文本生成的图像。AVA 与 Simulacra 都属于图像评分数据集，给出的是图像的绝对分数，它们被用于训练美学分数预测器[28]，该预测器参与了 Stable Diffusion [23] 的数据清洗流程。InstructGPT [18] 提出用人类反馈对齐预训练语言模型；从人类反馈中强化学习（RLHF）的思路也被引入视觉内容创作[11, 32]，这需要对同一提示词生成的图像作比较。HPD v1 [32] 正是在这一背景下采集的，它通过让文生图模型与人类偏好对齐来提升图像质量。与 HPD v1 类似，ImageReward [33] 和 Pick-a-Pic [10] 也是成对图像比较的数据集，侧重生成图像的评测。AGIQA-1K [37] 与 AGIQA-3K [12] 的采集方式相近，但规模明显更小。我们的 HPD v2 比现有工作纳入了更多来源、更多数量的图像，从而能更全面地评测这些偏好预测模型，表 5 给出了与其他数据集的逐项比较。Fake2M [15] 是另一个相关数据集，专注于区分生成图像的视觉图灵测试。

**EN** 3 Human Preference Dataset v2

**ZH** 3 人类偏好数据集 v2

**EN** Human Preference Dataset v2 (HPD v2) is a large-scale, cleanly-annotated dataset of human preferences for images generated from text prompts. In total, the dataset contains 798k pairs of binary preference choices for 434k images. Each pair contains two images generated by different models using the same prompt, and is annotated with a binary choice made by one annotator. The collection pipeline of HPD v2 includes prompt collection (Sec.3.1), image collection (Sec.3.2), and preference annotation (Sec.3.3). Detailed statistics about the dataset are presented in Sec.3.4. A head-to-head comparison with previous datasets is made in Sec. 3.5.

**ZH** 人类偏好数据集 v2（HPD v2）是一个大规模、标注干净的数据集，记录人类对文本提示词所生成图像的偏好。数据集共包含 434k 幅图像上的 798k 对二元偏好选择。每一对包含由不同模型用同一提示词生成的两幅图像，并由一位标注者给出二元选择。HPD v2 的采集流程包括提示词采集（第 3.1 节）、图像采集（第 3.2 节）和偏好标注（第 3.3 节）。数据集的详细统计见第 3.4 节，与已有数据集的逐项比较见第 3.5 节。

**EN** Table 1: Examples of prompts cleaned by ChatGPT.

**ZH** 表 1：经 ChatGPT 清洗的提示词示例。

<!-- [原子块 · table] Prompts from DiffusionDB [ 31 ] Prompts cleaned by ChatGPT queen goddess isis, high fantasy, by john berkey, by peter mohrbacher, renaissance oil painting, realism, master study, hyperrealist. The ima -->

**EN** 3.1 Prompt collection

**ZH** 3.1 提示词采集

**EN** Prompt sources. A naive idea is to use captions from image-caption datasets, such as COCO Captions [1] and LAION [28]. However, these captions are mostly for describing real images, which may not reflect the general interest of generative model users. Many “fiction” content can only be created from the imagination of generative model users.

**ZH** 提示词来源。一个朴素的想法是使用图像字幕数据集（如 COCO Captions [1] 和 LAION [28]）的字幕。但这些字幕多用于描述真实图像，未必反映生成模型用户的普遍兴趣；许多“虚构”内容只能来自生成模型用户的想象。

**EN** There are two recent sources containing user-written prompts. DrawBench is a list of prompts proposed in Imagen [24] to evaluate text-to-image generative models. It is a collection of 200 prompts organized into 11 categories, designed to test various aspects of a model’s capabilities. However, the size only supports the purpose of evaluation. DiffusionDB [31] is a database containing a wide range of user-written prompts and generated images. However, a significant portion of the prompts in the database is biased towards certain styles. For instance, around 15.0% of the prompts in DiffusionDB include the name “Greg Rutkowski”, 28.5% include “artstation”. Note that the effectiveness of these words is highly dependent on the training data of generative models. A model trained without images from artstation, or at least without “artstation” in its training prompts, may not respond to such style words. It is unfair to test these models on the biased prompts. There are also conflict contents in these prompts. For example, consider the first prompt in Tab.1, “renaissance oil painting” is conflict with “realism” and “hyper realistic”. These conflicts may confuse annotators in evaluating image-text alignment.

**ZH** 近期有两处包含用户撰写提示词的来源。DrawBench 是 Imagen [24] 中提出的一组提示词，用于评测文本到图像生成模型，包含 200 条提示词，分为 11 个类别，旨在检验模型能力的各个方面，但其规模只够支撑评测这一用途。DiffusionDB [31] 是一个包含大量用户撰写提示词及其生成图像的数据库，但其中相当比例的提示词偏向某些风格。例如 DiffusionDB 中约 15.0% 的提示词包含“Greg Rutkowski”，28.5% 包含“artstation”。要注意的是，这些词的有效性高度依赖生成模型的训练数据：一个训练时没有 artstation 图像、或至少训练提示词中没有“artstation”的模型，可能不会对这些风格词作出响应，用带偏差的提示词测试这些模型并不公平。这些提示词中还存在内容冲突，例如表 1 的第一条提示词中，“renaissance oil painting”与“realism”、“hyper realistic”相互冲突，这类冲突会干扰标注者对图文对齐的判断。

**EN** We collect three groups of prompts for different purposes: training a preference prediction model, testing a preference prediction model, and benchmarking generative models. All three groups consist of prompts from COCO Captions [1] and prompts from DiffusionDB [31] cleaned by ChatGPT. Detailed statistics will be introduced in Sec. 3.4 and Sec. 7.

**ZH** 我们为三个不同用途采集了三组提示词：训练偏好预测模型、测试偏好预测模型、以及为生成模型建立基准。三组都由 COCO Captions [1] 的提示词和经 ChatGPT 清洗的 DiffusionDB [31] 提示词构成。详细统计见第 3.4 节与第 7 节。

<!-- [原子块 · object]  -->

**EN** Figure 2: Histogram of NSFW score distribution. The first bucket counting “safe” prompts is omitted for better visualization.

**ZH** 图 2：NSFW 分数分布直方图。为便于可视化，省略了统计“安全”提示词的第一个区间。

<!-- [原子块 · object]  -->

**EN** Figure 3: Frequencies of certain style words and conflict prompt. Confliction is judged by ChatGPT.

**ZH** 图 3：特定风格词与冲突提示词的出现频次。冲突由 ChatGPT 判定。

**EN** Prompt cleaning using ChatGPT. To address the above issues, we utilize ChatGPT to rewrite prompts in DiffusionDB [31]. The instruction for ChatGPT is elaborated in Appendix A. Prompts for image generation and benchmarking generative models are all cleaned with the same pipeline. In Tab. 1, we show examples of prompts before and after cleaning. The output prompts are clearly written in one sentence with less style words, which are easier for our annotators to understand. Fig. 3 shows the histogram of NSFW score [5] distribution before and after cleaned by ChatGPT. The effect is significant for buckets of high NSFW score. Fig. 3 shows frequencies of certain style words and conflict prompt, where confliction is judged by ChatGPT. The frequency of platform names and artist names decreases, and there are less conflict prompts after cleaning.

**ZH** 用 ChatGPT 清洗提示词。为解决上述问题，我们利用 ChatGPT 改写 DiffusionDB [31] 中的提示词，给 ChatGPT 的指令详见附录 A。用于图像生成和为生成模型建立基准的提示词都经过同一流程清洗。表 1 给出清洗前后的提示词示例：输出的提示词以一句清晰的话写成，风格词更少，标注者更容易理解。图 2 显示了经 ChatGPT 清洗前后 NSFW 分数[5] 的分布直方图，在高 NSFW 分数区间效果显著。图 3 给出特定风格词与冲突提示词的频次（冲突由 ChatGPT 判定）：清洗后平台名与艺术家名的频次下降，冲突提示词也更少。

**EN** Table 2: Image sources of HPD v2.

**ZH** 表 2：HPD v2 的图像来源。

<!-- [原子块 · table] Source Split # Param. Type # images CogView2 train & test 24B Autoregressive 73697 DALL·E 2 train & test 3.5B Diffusion 101869 GLIDE test 0.94B Diffusion 400 SD v1.4 train & test 0.89B Diffusion 10186 -->

**EN** 3.2 Image collection

**ZH** 3.2 图像采集

**EN** In order to train and evaluate a preference prediction model, we generate images using different models and the same prompt for human preference annotation. For each prompt, we generate several images using different models. We also add the real image for prompts in COCO Captions. Tab. 2 summarizes image sources of HPD v2. The dataset comprises images generated by models of different architectures, scales, resulting in a high degree of diversity. This diversity allows for a comprehensive evaluation of a preference prediction model’s generalization capability and facilitates the training of a more generalizable model. The training set contains images from 4 models + COCO images, while the test set contains 9 models + COCO images. The 5 unseen models enable us to validate the generalization capability of the trained preference prediction model. For information on the inference parameters of each model, please refer to Appendix D.

**ZH** 为了训练和评测偏好预测模型，我们用不同模型、针对同一提示词生成图像，供人类偏好标注使用。对每个提示词，我们用不同模型生成若干图像；对 COCO Captions 中的提示词，还加入对应的真实图像。表 2 汇总了 HPD v2 的图像来源。数据集包含由不同结构、不同规模的模型生成的图像，因而具有高度多样性，既能全面评测偏好预测模型的泛化能力，也有助于训练泛化性更强的模型。训练集包含 4 个模型的图像加 COCO 图像，测试集包含 9 个模型的图像加 COCO 图像；那 5 个未见过的模型使我们能够验证所训偏好预测模型的泛化能力。各模型的推理参数见附录 D。

**EN** 3.3 Preference annotation

**ZH** 3.3 偏好标注

**EN** To gather preference rankings for a given prompt and its corresponding generated images, we employ annotators to assess and rank the images based on their preference. The preference may be influenced by factors such as image-text alignment and visual attractiveness. While these two factors can sometimes conflict with each other, understanding the trade-off is crucial.

**ZH** 为获得给定提示词及其对应生成图像的偏好排序，我们请标注者依据自身偏好对图像进行评判与排序。偏好可能受图文对齐、视觉吸引力等因素影响。这两个因素有时相互冲突，而理解其中的权衡至关重要。

**EN** Table 3: Annotator statistics.

**ZH** 表 3：标注者统计信息。

<!-- [原子块 · table] Gender Male 25 Female 32 Education University 8 College 42 Before college 7 Age 18-25 13 25-35 37 35 or above 7 Employment Full time 35 Part time 22 Total - 57 -->

<!-- [原子块 · object]  -->

**EN** Figure 4: Distribution of inter-annotator agreement. The agreement is computed on pairwise comparison between images in HPD v2 test set.

**ZH** 图 4：标注者间一致性的分布。一致性在 HPD v2 测试集的图像两两比较上计算。

**EN** Table 4: Inter-annotator agreement of HPD v2 annotation between different models.

**ZH** 表 4：HPD v2 标注中不同模型之间的标注者间一致性。

<!-- [原子块 · table] Model SD v1.4 SD v2.0 VQ-Diffusion LAFITE GLIDE CogView2 VQGAN+CLIP DALL·E2 COCO FuseDream 79.1% 83.6% 63.1% 69.1% 80.6% 78.1% 61.6% 82.2% 85.2% SD v1.4 - 65.2% 82.4% 88.3% 92.2% 62.1% 81.9% 66.0% 71. -->

**EN** Figure 5: Inter-annotator agreement between models plotted against absolute difference in HPS v2.

**ZH** 图 5：模型间的标注者间一致性相对 HPS v2 绝对差值作图。

<!-- [原子块 · object]  -->

**EN** We have assembled a team of 57 contractors, consisting of 50 labelers and 7 quality control checkers, to annotate our data. Each labeler undergoes an orientation to familiarize themselves with our requirements and the annotation system. Detailed guidelines regarding our requirements are documented in Appendix B. Following the orientation, labelers are required to complete a test, which involves a task of ranking 300 groups of images. The checkers evaluate the annotation quality based on these tests. At least 10% of the tasks are cross-checked by the checkers, who examine the top-ranked choice made by the labeler and calculate the recall @ 2 compared to the checkers’ answer.

**ZH** 我们组建了一支 57 人的合同制团队来标注数据，其中 50 名标注员、7 名质检员。每位标注员都要参加一次岗前培训，熟悉我们的要求和标注系统；要求的详细指南记录在附录 B。培训之后，标注员须完成一项测试，任务是对 300 组图像排序。质检员依据这些测试评估标注质量；至少 10% 的任务会被质检员交叉复核，质检员检查标注员给出的首位选择，并计算相对质检员答案的 recall@2。

**EN** As preference is subjective, there is no fixed standard for acceptance. Decisions are made on a case-by-case basis. Even if a labeler has low recall during the test, they may still be hired if they can adequately explain their decisions. The overall hiring rate is 61%. Tab. 3 presents statistical information about our annotators. It is worth noting that our annotators do not possess specialized training in art appreciation. They are a group of average annotators rather than experts in the field. Spot tests continue to be conducted after the labeler is hired to ensure ongoing quality.

**ZH** 由于偏好具有主观性，并没有固定的录用标准，决策逐案作出。即便某位标注员在测试中 recall 较低，只要能充分解释自己的判断，仍可能被录用。整体录用率为 61%。表 3 给出了标注者的统计信息。值得一提的是，我们的标注者没有接受过艺术鉴赏的专门训练，是一组普通标注者，而非该领域专家。标注员入职后仍会持续进行抽检，以保证长期质量。

**EN** In Tab. 4, we present the inter-labeler agreement for preferences on each pair of models in our test set. As depicted in Figure 5, we observe that the agreement between models with similar quality is relatively lower, whereas the agreement is higher for comparisons between models with substantial disparities.

**ZH** 表 4 给出测试集中每一对模型上偏好的标注员间一致性。如图 5 所示，质量相近的模型之间一致性相对较低，而差异悬殊的模型之间一致性更高。

**EN** 3.4 Statistics

**ZH** 3.4 统计信息

**EN** HPD v2 comprises a test split and a training split. The test split consists of 400 groups of images. Among them, 300 groups use prompts from DiffusionDB [31], and 100 groups use prompts from COCO Captions [1]. Each group contains 9 images generated from a text-to-image generative model. For the 100 groups using prompts from COCO Captions [1], we add one more real image from the COCO Captions dataset [1]. Each group in the test set is annotated by 10 distinct annotators to ensure more stable evaluation and to enable the study of diversity in human preference, resulting in 153,000 binary comparisons. The training split of HPD v2 contains 107,515 groups of images, each containing 4 images from 4 models (or real image), ranked by one annotator, which corresponds to 645,090 human binary comparisons. 28,172 prompts in the training set are from COCO Captions [1], while others are from DiffusionDB [31].

**ZH** HPD v2 由测试划分和训练划分组成。测试划分包含 400 组图像，其中 300 组使用 DiffusionDB [31] 的提示词，100 组使用 COCO Captions [1] 的提示词；每组包含由文本到图像生成模型生成的 9 幅图像。对于使用 COCO Captions [1] 提示词的 100 组，我们额外加入一幅来自 COCO Captions 数据集[1] 的真实图像。测试集中每组由 10 位不同标注者标注，以保证评测更稳定，并便于研究人类偏好的多样性，共产生 153,000 条二元比较。HPD v2 的训练划分包含 107,515 组图像，每组含来自 4 个模型（或真实图像）的 4 幅图像，由一位标注者排序，对应 645,090 条人类二元比较。训练集中的提示词有 28,172 条来自 COCO Captions [1]，其余来自 DiffusionDB [31]。

**EN** Table 5: Comparison with related datasets.

**ZH** 表 5：与相关数据集的比较。

<!-- [原子块 · table] Name Annotator Data Format Prompt Source Image Source # Prompts # Choices HPD v1 [ 32 ] Discord users Top-1 choice Discord users Stable Diffusion 25k 25k ImageReward [ 33 ] Expert Pairwise comparison  -->

**EN** 3.5 Comparison with related datasets

**ZH** 3.5 与相关数据集的比较

**EN** A head-to-head statistical comparison with HPD v1 [32], ImageReward [33], and Pick-a-Pic [10] is presented in Tab. 5. HPD v1 and Pick-a-Pic collect preference data from the internet, while ImageReward and HPD v2 are collected from contract workers. Although it is easier to distribute a survey via online platforms like the Discord channel or web applications, the anonymous nature of the internet poses difficulty for quality control and analysis on potential bias. For example, 34.9% of instances in Pick-a-Pic has a prompt that repeats for more than 50 times, these repeated prompts only take up 4.7% of total unique prompts. On the contrary, we have detailed statistics about the background of our annotators, which guarantees a better transparency for our dataset. Prompts from HPD v1 and ImageReward are collected from Discord channels, which show a strong bias towards certain styles. The bias problem is less severe in HPD v2.

**ZH** 表 5 给出了与 HPD v1 [32]、ImageReward [33] 和 Pick-a-Pic [10] 的逐项统计比较。HPD v1 与 Pick-a-Pic 从互联网采集偏好数据，而 ImageReward 与 HPD v2 来自合同制工作者。尽管通过 Discord 频道或网页应用等在线平台分发问卷更便捷，但互联网的匿名性给质量控制和潜在偏差分析带来困难。例如，Pick-a-Pic 中 34.9% 的样本其提示词重复出现超过 50 次，而这些重复提示词只占全部不同提示词的 4.7%。相反，我们掌握标注者背景的详细统计，保证了数据集更高的透明度。HPD v1 与 ImageReward 的提示词采集自 Discord 频道，表现出对某些风格的强烈偏差；HPD v2 的偏差问题较轻。

**EN** 4 Human Preference Score v2

**ZH** 4 人类偏好分数 v2

**EN** In this section, we introduce the training of Human Preference Score v2 (HPS v2), and present a comprehensive evaluation of existing preference prediction models on the test set of HPD v2 and ImageReward [33].

**ZH** 本节介绍人类偏好分数 v2（HPS v2）的训练，并在 HPD v2 与 ImageReward [33] 的测试集上对现有偏好预测模型作全面评测。

**EN** 4.1 Training

**ZH** 4.1 训练

**EN** CLIP [20] is a base-model that aligns image and text to the same embedding space. It has an image encoder to encode an image into a visual feature, and a text encoder to encode a caption into a text feature. The cosine similarity between the visual and text features measures the alignment between the input image and caption. However, CLIP [20] does not work well for zero-shot human preference prediction, as shown in Tab. 6. For more background information about the CLIP model, please refer to Appendix F.

**ZH** CLIP [20] 是一个把图像与文本对齐到同一嵌入空间的基座模型，含一个把图像编码为视觉特征的图像编码器和一个把字幕编码为文本特征的文本编码器；视觉特征与文本特征的余弦相似度度量输入图像与字幕的对齐程度。然而如表 6 所示，CLIP [20] 在零样本人类偏好预测上表现不佳。关于 CLIP 模型的更多背景见附录 F。

**EN** HPS v2 is trained by fine-tuning CLIP [20] on HPD v2. Each instance in the training set contains a pair of images ⟦SLOT_0⟧ with prompt ⟦SLOT_1⟧, which is labeled with ⟦SLOT_2⟧ if image ⟦SLOT_3⟧ is preferred over ⟦SLOT_4⟧, otherwise ⟦SLOT_5⟧. The CLIP model can be viewed as a score function ⟦SLOT_6⟧ that computes the similarity between prompt ⟦SLOT_7⟧ and image ⟦SLOT_8⟧:

**ZH** HPS v2 通过在 HPD v2 上微调 CLIP [20] 得到。训练集中每条样本包含一对图像 ⟦SLOT_0⟧ 及提示词 ⟦SLOT_1⟧，标签为 ⟦SLOT_2⟧（当图像 ⟦SLOT_3⟧ 相对 ⟦SLOT_4⟧ 更受偏好），否则为 ⟦SLOT_5⟧。CLIP 模型可视为一个分数函数 ⟦SLOT_6⟧，计算提示词 ⟦SLOT_7⟧ 与图像 ⟦SLOT_8⟧ 之间的相似度：

<!-- [原子块 · table] s θ ​ ( p , x ) = Enc txt ​ ( p ) ⋅ Enc img ​ ( x ) τ , s_{\theta}(p,x)=\frac{\mathrm{Enc}_{\rm txt}(p)\cdot\mathrm{Enc}_{\rm img}(x)}{\tau}, (1) -->

**EN** where ⟦SLOT_9⟧ is the learned temperature scalar of the CLIP model, and ⟦SLOT_10⟧ is the parameters in CLIP. The predicted preference ⟦SLOT_11⟧ is calculated as:

**ZH** 其中 ⟦SLOT_9⟧ 是 CLIP 模型学习得到的温度标量，⟦SLOT_10⟧ 是 CLIP 中的参数。预测的偏好 ⟦SLOT_11⟧ 计算如下：

<!-- [原子块 · table] y i ^ = exp ⁡ ( s θ ​ ( p , x i ) ) ∑ j = 1 2 exp ⁡ ( s θ ​ ( p , x j ) ) . \hat{y_{i}}=\frac{\exp(s_{\theta}(p,x_{i}))}{\sum_{j=1}^{2}\exp(s_{\theta}(p,x_{j}))}. (2) -->

**EN** ⟦SLOT_12⟧ is optimized by minimizing the KL-divergence:

**ZH** ⟦SLOT_12⟧ 通过最小化 KL 散度来优化：

<!-- [原子块 · table] L pref = ∑ j = 1 2 y i ​ ( log ⁡ y i − log ⁡ y j ^ ) . L_{\rm pref}=\sum_{j=1}^{2}y_{i}(\log y_{i}-\log\hat{y_{j}}). (3) -->

**EN** We fine-tune ViT-H/14 trained by OpenCLIP [20, 8] by optimizing ⟦SLOT_13⟧ on HPD v2 for 4,000 steps with the AdamW optimizer [9, 14], a learning rate of ⟦SLOT_14⟧, a weight decay of 0.35, a batch size of 128 and a warm-up period of 500 steps, following a cosine learning rate schedule. When fine-tuning a pre-trained model on limited data, a common practice is to freeze or decrease the learning rate of the first few layers [6, 30, 35]. We train the last 20 layers of the CLIP image encoder and the last 11 layers of the CLIP text encoder. Hyper-parameters are determined by Bayesian optimization with the target of accuracy on the HPD v2 test set.

**ZH** 我们用 AdamW 优化器[9, 14] 在 HPD v2 上优化 ⟦SLOT_13⟧，对 OpenCLIP [20, 8] 训练的 ViT-H/14 微调 4,000 步，学习率 ⟦SLOT_14⟧，权重衰减 0.35，批大小 128，预热 500 步，之后按余弦学习率调度衰减。在有限数据上微调预训练模型时，常见做法是冻结或降低前几层的学习率[6, 30, 35]；我们训练 CLIP 图像编码器的最后 20 层和文本编码器的最后 11 层。超参数由贝叶斯优化确定，优化目标为 HPD v2 测试集上的准确率。

**EN** Table 6: Preference prediction accuracy on test sets of ImageReward and HPD v2.

**ZH** 表 6：在 ImageReward 与 HPD v2 测试集上的偏好预测准确率。

<!-- [原子块 · table] Model ImageReward HPD v2 CLIP ViT-H/14 [ 20 , 8 ] 57.1 65.1 ImageReward [ 33 ] 65.1 74.0 Aesthetic Score Predictor [ 28 ] 57.4 76.8 HPS [ 32 ] 61.2 77.6 PickScore [ 10 ] 62.9 79.8 Single Human vs. Sin -->

**EN** 4.2 Experiments

**ZH** 4.2 实验

**EN** In Tab. 6, we report the accuracy of the baseline models on test sets of ImageReward [33] and HPD v2, the consistency between human annotators, and the performance of HPS v2. Different from the test set of ImageReward [33] that only contains images generated by Stable Diffusion, the images of HPD v2 test set cover a much wider range of image distribution, as demonstrated in Tab. 2, and can more comprehensively evaluate a preference prediction model’s generalization capability. HPS v2 exhibits better accuracy on both benchmarks, demonstrating its strong capability of generalization. In Appendix E, we report the decomposed accuracy between models. In Appendix F, we report ablation experiments on hyper-parameter choices.

**ZH** 表 6 报告了基线模型在 ImageReward [33] 与 HPD v2 测试集上的准确率、人类标注者之间的一致性，以及 HPS v2 的性能。与只含 Stable Diffusion 生成图像的 ImageReward [33] 测试集不同，HPD v2 测试集的图像覆盖更广的分布（如表 2 所示），因而能更全面地评测偏好预测模型的泛化能力。HPS v2 在两个基准上都取得更好的准确率，展现出强大的泛化能力。附录 E 报告了按模型分解的准确率，附录 F 报告了超参数选择的消融实验。

**EN** It should be noted that although human preferences are generally diverse, the average preference of multiple humans can reflect humans’ general tendency. Since HPS v2 is trained on preferences from many annotators, it is able to learn humans’ average preferences, which can exceed a single person’s accuracy (Single Human vs. Single Human). Besides a single person’s accuracy, we also report the accuracy of a single person compared to an averaged ranking, which is still higher than HPS v2.

**ZH** 需要说明的是，尽管人类偏好通常是多样的，多人的平均偏好仍能反映人类的总体倾向。由于 HPS v2 在众多标注者的偏好上训练，它得以学习人类的平均偏好，因而能超过单个人的准确率（单人对单人）。除单个人的准确率外，我们还报告了单个人相对平均排序的准确率，该值仍高于 HPS v2。

**EN** 5 Benchmarking Text-to-Image Generative Models

**ZH** 5 文本到图像生成模型基准测试

**EN** Table 7: HPS v2 benchmark. We also provide HPS v2 evaluated on DrawBench for reference.

**ZH** 表 7：HPS v2 基准。我们同时给出 HPS v2 在 DrawBench 上的评测结果以供参考。

<!-- [原子块 · table] HPS v2 Model Animation Concept-art Painting Photo DrawBench [ 24 ] GLIDE [ 17 ] 23.34 ± 0.198 23.34\pm 0.198 23.08 ± 0.174 23.08\pm 0.174 23.27 ± 0.178 23.27\pm 0.178 24.50 ± 0.290 24.50\pm 0.290 25.0 -->

**EN** Similar to HPS v1, HPS v2 evaluates the preference score of a generated image ⟦SLOT_15⟧ given a reference prompt ⟦SLOT_16⟧ as follows:

**ZH** 与 HPS v1 类似，HPS v2 按如下方式评测生成图像 ⟦SLOT_15⟧ 在给定参考提示词 ⟦SLOT_16⟧ 下的偏好分数：

<!-- [原子块 · table] s θ ​ ( p , x ) = Enc txt ​ ( p ) ⋅ Enc img ​ ( x ) × 100 , s_{\theta}(p,x)=\mathrm{Enc}_{\rm txt}(p)\cdot\mathrm{Enc}_{\rm img}(x)\times 100, (4) -->

**EN** where the notation is the same as Equation 1. We evaluate models separately for different styles using prompts obtained from ChatGPT, as described in Sec. 3.1. To this end, we use a set of evaluation prompts that involves testing a model on a total of 3200 prompts, with 800 prompts for each of the following styles: “Animation”, “Concept-art”, “Painting”, and “Photo”. The first 3 styles are popular in DiffusionDB [31] based on our observation. For each style, 800 prompts are divided into groups of 80, and evaluated separately. We report the mean and standard deviation of 10 groups. The size of 800 prompts ensures that HPS v2 is statistically stable across all evaluated models, while also avoiding excessive computational overhead.

**ZH** 其中记号与式 1 相同。我们用第 3.1 节所述由 ChatGPT 得到的提示词，按不同风格分别评测模型。为此我们使用一组评测提示词，共在 3200 条提示词上测试一个模型，“Animation”、“Concept-art”、“Painting”、“Photo” 四种风格各 800 条。前 3 种风格据我们观察在 DiffusionDB [31] 中较为流行。每种风格的 800 条提示词被分为 80 条一组分别评测，我们报告 10 组的均值与标准差。800 条这一规模既保证 HPS v2 在所有被测模型上统计稳定，又避免了过大的计算开销。

**EN** Tab. 7 shows a benchmark of recent text-to-image generative models from the academic, community and industry. It’s an interesting trend that popular models from the community are consistently out-performing models from the academic. We also plotted HPS v2 against existing evaluation metrics, CLIP Score [20] and Aesthetic Score [28]. An interesting data point is CogView2 [2]. It generates images with high aesthetic quality, but has worse controllability. Inference details of each model on the benchmark are elaborated in Appendix D.

**ZH** 表 7 给出了来自学术界、社区和工业界的近期文本到图像生成模型的基准结果。一个有意思的趋势是，社区的热门模型持续优于学术界的模型。我们还把 HPS v2 与现有评测指标 CLIP Score [20] 和美学分数[28] 对照作图。一个有意思的数据点是 CogView2 [2]：它生成的图像美学质量高，但可控性较差。基准中各模型的推理细节见附录 D。

**EN** In Appendix G, we show more example usages of HPS v2 other than benchmarking text-to-image models.

**ZH** 附录 G 给出了 HPS v2 除文本到图像模型基准测试之外的更多用例。

**EN** Figure 6: Correlation between HPS v2 and other models.

**ZH** 图 6：HPS v2 与其他模型之间的相关性。

<!-- [原子块 · object]  -->

<!-- [原子块 · object]  -->

**EN** 6 Limitations

**ZH** 6 局限性

**EN** There are several potential limitations about this work. The prompts are sourced from DiffusionDB [31] and COCO Captions [1], and the choice of the 3 styles of our benchmark except “Photo” is summarized based on the general interest we observed in DiffusionDB. Although DiffusionDB provides a massive collection of prompts that reflects community users’ demands, there are indeed some overlooked topics, such as logo and graphic design. These demands also play a crucial role in design industries and have unique criteria or preferences compared to general image creation. Using ChatGPT for prompt cleaning may also introduce potential bias, although currently we did not find such patterns. Also, this dataset is annotated by 57 annotators, and thus it may suffer from bias of them. Another limitation is that this work did not study the effect of image resolution on human preferences, though this can make a big impact as the resolution of generated images keeps increasing.

**ZH** 本工作存在若干潜在局限。提示词来自 DiffusionDB [31] 与 COCO Captions [1]，基准中除“Photo”外的 3 种风格是依据我们在 DiffusionDB 中观察到的普遍兴趣归纳而来。尽管 DiffusionDB 提供了海量提示词、反映了社区用户的需求，其中确实也存在一些被忽视的主题，例如标志与平面设计；这些需求在设计行业中同样重要，且相比一般图像创作有独特的标准或偏好。用 ChatGPT 清洗提示词也可能引入潜在偏差，尽管目前我们尚未发现此类模式。此外，该数据集由 57 名标注者标注，因而可能带有他们的偏差。另一项局限是，本工作没有研究图像分辨率对人类偏好的影响，而随着生成图像分辨率不断提升，这一点可能产生很大影响。

**EN** Generative models potentially have negative social impacts by their nature. The advancement in generative models often means more plausible generated content, which may be maliciously utilized for the spread of more convincing misinformation and fake content. Additionally, there is a risk of amplifying existing biases and stereotypes present in the training data.

**ZH** 生成模型就其性质而言可能带来负面社会影响。生成模型的进步通常意味着更逼真的生成内容，这可能被恶意用于传播更具说服力的虚假信息与伪造内容。此外还存在放大训练数据中既有偏见与刻板印象的风险。

**EN** 7 Conclusion

**ZH** 7 结论

**EN** In this work, we design a less biased pipeline for collecting prompts and images for human preference annotations. With collected data, we present Human Preference Dataset v2, a human preference dataset containing 798k carefully annotated comparison pairs, enabling the training of Human Preference Score v2, the state-of-art preference prediction model, to better align text-to-image generation models’ evaluation with human values and judgments. We also provide a more stable and fair group of prompts for text-to-image generative models’ evaluation, and set up a benchmark that compares a wide range of recent models. Finally, we illustrate the accuracy of HPS v2 by demonstrating some example usages. There are still many opportunities for further advancement and expansion based on our HPD v2 and HPS v2. We hope our work can inspire and facilitate future researches in this area.

**ZH** 本工作设计了一套偏差更小的流程，用于采集供人类偏好标注的提示词与图像。基于所采集的数据，我们提出人类偏好数据集 v2——一个包含 798k 条精心标注比较对的人类偏好数据集，并借此训练出当前最优的偏好预测模型人类偏好分数 v2，使文本到图像生成模型的评测更贴近人类的价值与判断。我们还提供了一组更稳定、更公平的提示词用于文生图模型评测，并建立了覆盖大量近期模型的基准。最后，我们通过若干用例展示了 HPS v2 的准确性。基于 HPD v2 与 HPS v2 仍有大量进一步推进与扩展的机会，希望本工作能为该领域的后续研究带来启发与便利。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] [1] Xinlei Chen, Hao Fang, Tsung-Yi Lin, Ramakrishna Vedantam, Saurabh Gupta, Piotr Dollar, and C. Lawrence Zitnick. Microsoft COCO Captions: Data Collection and Evaluation Server, 2015. -->

<!-- [原子块 · verbatim] [2] Ming Ding, Wendi Zheng, Wenyi Hong, and Jie Tang. Cogview2: Faster and better text-to-image generation via hierarchical transformers. NeurIPS , 35:16890–16902, 2022. -->

<!-- [原子块 · verbatim] [3] Patrick Esser, Robin Rombach, and Bjorn Ommer. Taming transformers for high-resolution image synthesis. In CVPR , pages 12873–12883, 2021. -->

<!-- [原子块 · verbatim] [4] Shuyang Gu, Dong Chen, Jianmin Bao, Fang Wen, Bo Zhang, Dongdong Chen, Lu Yuan, and Baining Guo. Vector quantized diffusion model for text-to-image synthesis. In CVPR , pages 10696–10706, 2022. -->

<!-- [原子块 · verbatim] [5] Laura Hanu and Unitary team. Detoxify. Github. https://github.com/unitaryai/detoxify, 2020. -->

<!-- [原子块 · verbatim] [6] Kaiming He, Xinlei Chen, Saining Xie, Yanghao Li, Piotr Dollár, and Ross Girshick. Masked autoencoders are scalable vision learners. In CVPR , pages 16000–16009, 2022. -->

<!-- [原子块 · verbatim] [7] Martin Heusel, Hubert Ramsauer, Thomas Unterthiner, Bernhard Nessler, and Sepp Hochreiter. GANs Trained by a Two Time-Scale Update Rule Converge to a Local Nash Equilibrium. In NeurIPS , 2017. -->

<!-- [原子块 · verbatim] [8] Gabriel Ilharco, Mitchell Wortsman, Ross Wightman, Cade Gordon, Nicholas Carlini, Rohan Taori, Achal Dave, Vaishaal Shankar, Hongseok Namkoong, John Miller, Hannaneh Hajishirzi, Ali Farhadi, and L -->

<!-- [原子块 · verbatim] [9] Diederik P Kingma and Jimmy Ba. Adam: A method for stochastic optimization. arXiv preprint arXiv:1412.6980 , 2014. -->

<!-- [原子块 · verbatim] [10] Yuval Kirstain, Adam Polyak, Uriel Singer, Shahbuland Matiana, Joe Penna, and Omer Levy. Pick-a-Pic: An Open Dataset of User Preferences for Text-to-Image Generation. arXiv preprint arXiv:2305.01 -->

<!-- [原子块 · verbatim] [11] Kimin Lee, Hao Liu, Moonkyung Ryu, Olivia Watkins, Yuqing Du, Craig Boutilier, Pieter Abbeel, Mohammad Ghavamzadeh, and Shixiang Shane Gu. Aligning text-to-image models using human feedback. arXi -->

<!-- [原子块 · verbatim] [12] Chunyi Li, Zicheng Zhang, Haoning Wu, Wei Sun, Xiongkuo Min, Xiaohong Liu, Guangtao Zhai, and Weisi Lin. AGIQA-3K: An Open Database for AI-Generated Image Quality Assessment, 2023. -->

<!-- [原子块 · verbatim] [13] Xingchao Liu, Chengyue Gong, Lemeng Wu, Shujian Zhang, Hao Su, and Qiang Liu. Fusedream: Training-free text-to-image generation with improved clip+ gan space optimization. arXiv preprint arXiv:21 -->

<!-- [原子块 · verbatim] [14] Ilya Loshchilov and Frank Hutter. Decoupled weight decay regularization. arXiv preprint arXiv:1711.05101 , 2017. -->

<!-- [原子块 · verbatim] [15] Zeyu Lu, Di Huang, Lei Bai, Jingjing Qu, Chengyue Wu, Xihui Liu, and Wanli Ouyang. Seeing is not always believing: Benchmarking Human and Model Perception of AI-Generated Images, 2023. -->

<!-- [原子块 · verbatim] [16] Naila Murray, Luca Marchesotti, and Florent Perronnin. AVA: A large-scale database for aesthetic visual analysis. CVPR , pages 2408–2415, 2012. -->

<!-- [原子块 · verbatim] [17] Alex Nichol, Prafulla Dhariwal, Aditya Ramesh, Pranav Shyam, Pamela Mishkin, Bob McGrew, Ilya Sutskever, and Mark Chen. GLIDE: Towards Photorealistic Image Generation and Editing with Text-Guided -->

<!-- [原子块 · verbatim] [18] Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. Training language models to follow instructio -->

<!-- [原子块 · verbatim] [19] John David Pressman, Katherine Crowson, and Simulacra Captions Contributors. Simulacra Aesthetic Captions. Technical Report Version 1.0, Stability AI, 2022. -->

<!-- [原子块 · verbatim] [20] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, and Ilya Sutskever. Learning  -->

<!-- [原子块 · verbatim] [21] Aditya Ramesh, Prafulla Dhariwal, Alex Nichol, Casey Chu, and Mark Chen. Hierarchical Text-Conditional Image Generation with CLIP Latents. ArXiv , abs/2204.06125, 2022. -->

<!-- [原子块 · verbatim] [22] Aditya Ramesh, Mikhail Pavlov, Gabriel Goh, Scott Gray, Chelsea Voss, Alec Radford, Mark Chen, and Ilya Sutskever. Zero-Shot Text-to-Image Generation. ArXiv , abs/2102.12092, 2021. -->

<!-- [原子块 · verbatim] [23] Robin Rombach, A. Blattmann, Dominik Lorenz, Patrick Esser, and Björn Ommer. High-Resolution Image Synthesis with Latent Diffusion Models. CVPR , pages 10674–10685, 2022. -->

<!-- [原子块 · verbatim] [24] Chitwan Saharia, William Chan, Saurabh Saxena, Lala Li, Jay Whang, Emily L Denton, Kamyar Ghasemipour, Raphael Gontijo Lopes, Burcu Karagol Ayan, Tim Salimans, et al. Photorealistic text-to-image -->

<!-- [原子块 · verbatim] [25] Tim Salimans, Ian Goodfellow, Wojciech Zaremba, Vicki Cheung, Alec Radford, and Xi Chen. Improved techniques for training gans. Advances in neural information processing systems , 29, 2016. -->

<!-- [原子块 · verbatim] [26] Dvir Samuel, Rami Ben-Ari, Simon Raviv, Nir Darshan, and Gal Chechik. It is all about where you start: Text-to-image generation with seed selection. arXiv preprint arXiv:2304.14530 , 2023. -->

<!-- [原子块 · verbatim] [27] Axel Sauer, Tero Karras, Samuli Laine, Andreas Geiger, and Timo Aila. StyleGAN-T: Unlocking the power of gans for fast large-scale text-to-image synthesis. arXiv preprint arXiv:2301.09515 , 2023. -->

<!-- [原子块 · verbatim] [28] Christoph Schuhmann, Romain Beaumont, Richard Vencu, Cade Gordon, Ross Wightman, Mehdi Cherti, Theo Coombes, Aarush Katta, Clayton Mullis, Mitchell Wortsman, et al. Laion-5b: An open large-scale  -->

<!-- [原子块 · verbatim] [29] Christoph Schuhmann, Romain Beaumont, Richard Vencu, Cade W Gordon, Ross Wightman, Mehdi Cherti, Theo Coombes, Aarush Katta, Clayton Mullis, Mitchell Wortsman, Patrick Schramowski, Srivatsa R Kun -->

<!-- [原子块 · verbatim] [30] Cristina Vasconcelos, Vighnesh Birodkar, and Vincent Dumoulin. Proper reuse of image classification features improves object detection. In CVPR , pages 13628–13637, 2022. -->

<!-- [原子块 · verbatim] [31] Zijie J Wang, Evan Montoya, David Munechika, Haoyang Yang, Benjamin Hoover, and Duen Horng Chau. DiffusionDB: A Large-scale Prompt Gallery Dataset for Text-to-Image Generative Models. arXiv prepr -->

<!-- [原子块 · verbatim] [32] Xiaoshi Wu, Keqiang Sun, Feng Zhu, Rui Zhao, and Hongsheng Li. Better Aligning Text-to-Image Models with Human Preference, 2023. -->

<!-- [原子块 · verbatim] [33] Jiazheng Xu, Xiao Liu, Yuchen Wu, Yuxuan Tong, Qinkai Li, Ming Ding, Jie Tang, and Yuxiao Dong. ImageReward: Learning and Evaluating Human Preferences for Text-to-Image Generation, 2023. -->

<!-- [原子块 · verbatim] [34] Xingqian Xu, Zhangyang Wang, Eric Zhang, Kai Wang, and Humphrey Shi. Versatile Diffusion: Text, Images and Variations All in One Diffusion Model. arXiv preprint arXiv:2211.08332 , 2022. -->

<!-- [原子块 · verbatim] [35] Zhai, Xiaohua and Wang, Xiao and Mustafa, Basil and Steiner, Andreas and Keysers, Daniel and Kolesnikov, Alexander and Beyer, Lucas. LiT: Zero-Shot Transfer With Locked-Image Text Tuning. In CVPR -->

<!-- [原子块 · verbatim] [36] Richard Zhang, Phillip Isola, Alexei A Efros, Eli Shechtman, and Oliver Wang. The unreasonable effectiveness of deep features as a perceptual metric. In CVPR , pages 586–595, 2018. -->

<!-- [原子块 · verbatim] [37] Zicheng Zhang, Chunyi Li, Wei Sun, Xiaohong Liu, Xiongkuo Min, and Guangtao Zhai. A Perceptual Quality Assessment Exploration for AIGC Images, 2023. -->

<!-- [原子块 · verbatim] [38] Sharon Zhou, Mitchell Gordon, Ranjay Krishna, Austin Narcomey, Li F Fei-Fei, and Michael Bernstein. Hype: A benchmark for human eye perceptual evaluation of generative models. NeurIPS , 32, 2019. -->

<!-- [原子块 · verbatim] [39] Y Zhou, R Zhang, C Chen, C Li, C Tensmeyer, T Yu, J Gu, J Xu, and T Sun. LAFITE: Towards Language-Free Training for Text-to-Image Generation. arXiv 2021. arXiv preprint arXiv:2111.13792 . -->

**EN** Checklist

**ZH** 检查清单

**EN** The checklist follows the references. Please read the checklist guidelines carefully for information on how to answer these questions. For each question, change the default [TODO] to [Yes] , [No] , or [N/A] . You are strongly encouraged to include a justification to your answer, either by referencing the appropriate section of your paper or providing a brief inline description. For example:

**ZH** 检查清单置于参考文献之后。请仔细阅读检查清单指南，了解如何回答这些问题。对每个问题，把默认的 [TODO] 改为 [Yes]、[No] 或 [N/A]。强烈建议你为答案附上理由，可引用论文相应章节，或给出简短的行内说明。例如：

**EN** • Did you include the license to the code and datasets? [Yes] Both the code and dataset is released under Apache 2.0 License.

**ZH** • 你是否包含了代码与数据集的许可？[Yes] 代码与数据集均以 Apache 2.0 许可发布。

**EN** • Did you include the license to the code and datasets? [No] The code and the data are proprietary.

**ZH** • 你是否包含了代码与数据集的许可？[No] 代码与数据为专有。

**EN** • Did you include the license to the code and datasets? [N/A]

**ZH** • 你是否包含了代码与数据集的许可？[N/A]

**EN** Please do not modify the questions and only use the provided macros for your answers. Note that the Checklist section does not count towards the page limit. In your paper, please delete this instructions block and only keep the Checklist section heading above along with the questions/answers below.

**ZH** 请勿修改问题，只使用提供的宏填写答案。注意检查清单部分不计入页数限制。请在论文中删除本说明块，只保留上方的检查清单标题及以下的问题与答案。

**EN** 1. For all authors… (a) Do the main claims made in the abstract and introduction accurately reflect the paper’s contributions and scope? [Yes] (b) Did you describe the limitations of your work? [Yes] (c) Did you discuss any potential negative societal impacts of your work? [N/A] (d) Have you read the ethics review guidelines and ensured that your paper conforms to them? [Yes]

**ZH** 1. 对所有作者而言……（a）摘要与引言中的主要主张是否准确反映了论文的贡献与范围？[Yes]（b）你是否描述了工作的局限性？[Yes]（c）你是否讨论了工作潜在的负面社会影响？[N/A]（d）你是否已阅读伦理审查指南并确保论文符合其要求？[Yes]

**EN** 2. If you are including theoretical results… (a) Did you state the full set of assumptions of all theoretical results? [N/A] (b) Did you include complete proofs of all theoretical results? [N/A]

**ZH** 2. 若包含理论结果……（a）你是否陈述了所有理论结果的完整假设集合？[N/A]（b）你是否给出了所有理论结果的完整证明？[N/A]

**EN** 3. If you ran experiments (e.g. for benchmarks)… (a) Did you include the code, data, and instructions needed to reproduce the main experimental results (either in the supplemental material or as a URL)? [Yes] Please see the supplemental material. (b) Did you specify all the training details (e.g., data splits, hyperparameters, how they were chosen)? [Yes] see Sec. 4.1 (c) Did you report error bars (e.g., with respect to the random seed after running experiments multiple times)? [Yes] In Tab. 7, we report the mean and standard deviation of 10 runs to demonstrate the stability and reliability of our benchmark. (d) Did you include the total amount of compute and the type of resources used (e.g., type of GPUs, internal cluster, or cloud provider)? [Yes] The resource consumption will be reported in our GitHub repository.

**ZH** 3. 若你开展了实验（例如基准测试）……（a）你是否包含了复现主要实验结果所需的代码、数据与说明（在补充材料中或以 URL 形式）？[Yes] 请参见补充材料。（b）你是否说明了全部训练细节（如数据划分、超参数及其选择方式）？[Yes] 见第 4.1 节。（c）你是否报告了误差范围（例如多次实验后关于随机种子的误差）？[Yes] 在表 7 中我们报告了 10 次运行的均值与标准差，以展示基准的稳定性与可靠性。（d）你是否说明了所用算力的总量与资源类型（如 GPU 型号、内部集群或云服务商）？[Yes] 资源消耗将在我们的 GitHub 仓库中报告。

**EN** 4. If you are using existing assets (e.g., code, data, models) or curating/releasing new assets… (a) If your work uses existing assets, did you cite the creators? [Yes] (b) Did you mention the license of the assets? [N/A] (c) Did you include any new assets either in the supplemental material or as a URL? [Yes] We will release our dataset and pre-train model. (d) Did you discuss whether and how consent was obtained from people whose data you’re using/curating? [Yes] Please see Sec. 3.3. (e) Did you discuss whether the data you are using/curating contains personally identifiable information or offensive content? [N/A]

**ZH** 4. 若你使用了既有资产（代码、数据、模型）或整理／发布新资产……（a）你的工作若使用了既有资产，是否引用了创建者？[Yes]（b）你是否提及资产的许可？[N/A]（c）你是否以补充材料或 URL 的形式包含了新资产？[Yes] 我们将发布数据集与预训练模型。（d）你是否讨论过是否以及如何获得所使用／整理数据的相关人员的同意？[Yes] 请参见第 3.3 节。（e）你是否讨论过所使用／整理的数据是否包含个人身份信息或冒犯性内容？[N/A]

**EN** 5. If you used crowdsourcing or conducted research with human subjects… (a) Did you include the full text of instructions given to participants and screenshots, if applicable? [Yes] We will show our instructions given to the workers in the supplemental material. (b) Did you describe any potential participant risks, with links to Institutional Review Board (IRB) approvals, if applicable? [N/A] (c) Did you include the estimated hourly wage paid to participants and the total amount spent on participant compensation? [Yes] Yes, the hourly wage for the works is 20CNY/hour for annotators and 25CNY/hour for checkers.

**ZH** 5. 若你使用了众包或开展了涉及人类受试者的研究……（a）你是否包含了提供给参与者的完整说明文本与截图（如适用）？[Yes] 我们将在补充材料中展示提供给工作者的说明。（b）你是否描述了参与者的潜在风险，并在适用时附上机构审查委员会（IRB）审批链接？[N/A]（c）你是否说明了支付给参与者的估计时薪与报酬总额？[Yes] 是，工作者时薪为标注员 20 元／小时、质检员 25 元／小时。

**EN** Appendix A Prompt Cleaning

**ZH** 附录 A 提示词清洗

**EN** In this section we show details in prompt cleaning, categorization and annotation. As illustrated in Sec. 3.1, we task ChatGPT to clean and categorize prompts by posing the following questions.

**ZH** 本节给出提示词清洗、分类与标注的细节。如第 3.1 节所述，我们通过提出以下问题，让 ChatGPT 完成提示词的清洗与分类。

**EN** - I will give you a description about an image.Remove modifiers from text that have nothing to do with the main content of the image, for example resolution, sharpness, light, image quality, authors and online platform, and describe it succinctly in one sentence.

**ZH** ——我会给你一段关于图像的描述。请去除与图像主要内容无关的修饰语，例如分辨率、锐度、光线、图像质量、作者和在线平台，并用一句话简洁地描述它。

**EN** - Next, I will use text to describe a picture. Please reply to me according to the following rules: 1. If the picture belongs to the style of “paintings”, reply only with “paintings”; 2. If the picture belongs to the style of “anime and cartoon”, reply only with “anime and cartoon”; 3. If the picture belongs to the style of “real photo”, reply only with “real photo”; 4. If the picture belongs to the style of “concept-art”, reply only with “concept-art”; 5. If the picture doesn’t belong to any styles of above, reply only with “others”; You must reply with only on word.

**ZH** ——接下来，我会用文字描述一幅图片。请按以下规则回复：1. 若图片属于“绘画”风格，只回复“paintings”；2. 若图片属于“动漫与卡通”风格，只回复“anime and cartoon”；3. 若图片属于“真实照片”风格，只回复“real photo”；4. 若图片属于“概念艺术”风格，只回复“concept-art”；5. 若图片不属于上述任何风格，只回复“others”。你必须只回复一个词。

**EN** Even though prompts of “Photo” category in HPD v2 are from COCO Captions [1], we retain “Photo” in the classification process to mitigate the potential mistakes made by ChatGPT. The category distribution of HPD v2 is illustrated in Fig. 7.

**ZH** 尽管 HPD v2 中“Photo”类别的提示词来自 COCO Captions [1]，我们仍在分类流程中保留“Photo”，以缓解 ChatGPT 可能犯的错误。HPD v2 的类别分布见图 7。

**EN** Figure 7: Category Distribution.

**ZH** 图 7：类别分布。

<!-- [原子块 · img]  -->

**EN** Additionally, when processing data from DiffusionDB [31], we apply a filter to remove prompts with a NSFW threshold of 0.4. During the subsequent image generation step, we refine the selection of prompts by subjecting them to a stricter safety checker of DALL·E 2 [21]. This helps to further eliminate inappropriate vocabularies.

**ZH** 此外，在处理 DiffusionDB [31] 的数据时，我们用过滤器按 NSFW 阈值 0.4 去除提示词。在随后的图像生成步骤中，我们把提示词交给 DALL·E 2 [21] 更严格的安全检查器再作筛选，以进一步剔除不当词汇。

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

**EN** Figure 8: Prompt: A pair of skis standing up against a gate.

**ZH** 图 8：提示词：A pair of skis standing up against a gate。

**EN** Appendix B Annotation

**ZH** 附录 B 标注

**EN** To ensure the quality of annotation, we provide a basic guidance document for our annotators:

**ZH** 为保证标注质量，我们为标注者提供了一份基础指南文档：

**EN** Basic rules and regulations

**ZH** 基本规则与规范

**EN** We will provide you groups of images for ranking, which consists of images generated from different AI models. Please consider the prompts and rank images from the perspectives of universal and personal aesthetic appeal. This task mainly involves two aspects: text-image alignment and image quality. Although we encourage and value personal preference, it’s important to consider the following fundamental principles when balancing the two aspects or facing a dilemma:

**ZH** 我们将向你提供若干组用于排序的图像，这些图像由不同的 AI 模型生成。请结合提示词，从普适审美与个人审美吸引力的角度对图像排序。该任务主要涉及两个方面：图文对齐与图像质量。尽管我们鼓励并重视个人偏好，在权衡这两个方面或面临两难时，请务必考虑以下基本原则：

**EN** 1. When Image (A) surpasses Image (B) in terms of aesthetic appeal and fidelity, or Image (B) suffers from severe distortion and blurriness, even if Image (B) aligns better with the prompt, Image (A) should take precedence over Image (B). For example, in Fig. 8, Fig. 8 lacks clear outlines and details of the ski board, resulting in an unattractive appearance and significant blurriness. However, Fig. 8 exhibits excellent fidelity and quality. Therefore, the ordering of the figures should place Fig. 8 before Fig. 8. ⟦SLOT_17⟧ ⟦SLOT_18⟧ Figure 9: Prompt: A cat with two horns on its head. Similarly, in Fig. 9, although in Fig. 9 the required horns are mistakenly generated as elf ears, Fig. 9 suffers severe structural issues, repetitive generation problems, and blurriness. Therefore, the ordering of the figures should place Fig. 9 before Fig. 9.

**ZH** 1. 当图像（A）在美感与保真度上优于图像（B），或图像（B）存在严重畸变与模糊时，即便图像（B）与提示词更对齐，图像（A）也应排在图像（B）之前。例如在图 8 中，第一幅图像缺乏滑雪板清晰的轮廓与细节，外观欠佳且明显模糊；而第二幅图像保真度与质量俱佳，因此排序应将第二幅置于第一幅之前。⟦SLOT_17⟧ ⟦SLOT_18⟧ 图 9：提示词：A cat with two horns on its head。类似地，在图 9 中，尽管其中一幅把所需的角误生成为精灵耳，另一幅存在严重的结构问题、重复生成问题与模糊，因此排序应将前者置于后者之前。

**EN** 2. When facing a dilemma that images are relatively similar in terms of aesthetics and personal preference, please carefully read and consider the prompt for sorting based more on the text-image alignment. For example, if you cannot make a choice based on personal preference, as in Fig. 10, please pay attention to the description, which refers to a mouse mechanic. Therefore, the ordering of the figures should place Fig. 10 before Fig. 10. ⟦SLOT_19⟧ ⟦SLOT_20⟧ Figure 10: Prompt: A ginger haired mouse mechanic in blue overalls in a cyberpunk scene with neon slums in the background.

**ZH** 2. 当面临图像在美感与个人偏好上较为接近的两难时，请仔细阅读并考虑提示词，更多地依据图文对齐排序。例如，若你无法依据个人偏好作出选择，如图 10 所示，请留意描述中提到的是一位老鼠机械师，因此排序应将更符合描述的一幅置于另一幅之前。⟦SLOT_19⟧ ⟦SLOT_20⟧ 图 10：提示词：A ginger haired mouse mechanic in blue overalls in a cyberpunk scene with neon slums in the background。

**EN** 3. It is crucial to pay special attention to the capitalized names, as these names may lead to misunderstandings during the machine translation process. If there is any incorrectly translated proprietary term or content you are not familiar with, we recommend you to search for sample images and explanations online.

**ZH** 3. 务必特别注意大写的名称，因为这些名称在机器翻译过程中可能导致误解。若遇到翻译有误的专有术语或你不熟悉的内容，建议上网检索示例图像与解释。

**EN** Appendix C CLIP Details

**ZH** 附录 C CLIP 细节

**EN** CLIP [20] is a vision-language model trained on massive, noisy image-text pairs from the internet to model the joint distribution between images and texts. They demonstrate that the simple pre-training task of predicting which caption corresponds to which image is an efficient and scalable way to learn image representations from scratch [20]. The learned feature demonstrates impressive zero-shot image classification accuracy on various tasks. Our task of predicting human preference can also be viewed as an image classification task, so it can naturally take advantage of the CLIP pre-training. We use the ViT-H/14 variant of CLIP pre-trained by the OpenClip [8] project on LAION-2B [29]. The model consists of an image transformer and a text transformer as encoders for both modality. Details about the model architecture is listed in Tab. 8.

**ZH** CLIP [20] 是一个视觉语言模型，在来自互联网的海量噪声图文对上训练，用以建模图像与文本的联合分布。他们证明，“预测哪条字幕对应哪幅图像”这一简单的预训练任务是高效、可扩展地从零学习图像表示的方式[20]。学到的特征在多种任务上展现出令人印象深刻的零样本图像分类准确率。我们预测人类偏好的任务也可视为一种图像分类任务，因而自然能利用 CLIP 的预训练。我们使用 OpenClip [8] 项目在 LAION-2B [29] 上预训练的 CLIP ViT-H/14 变体，该模型由一个图像 transformer 和一个文本 transformer 分别作为两种模态的编码器。模型结构细节列于表 8。

**EN** Table 8: Model card of HPS v2.

**ZH** 表 8：HPS v2 的模型卡。

<!-- [原子块 · table] Embedding dimension 1024 Input image size 224 Input patch size 14 # image transformer layers 32 Image transformer width 1280 Image transformer # heads 16 Context length 77 Vocabulary size 49408 # text -->

**EN** Appendix D Generation Details

**ZH** 附录 D 生成细节

**EN** We provide image generation details for each model when constructing the HPS v2 benchmark. The images are also released with HPD v2.

**ZH** 我们在构建 HPS v2 基准时给出各模型的图像生成细节，这些图像也随 HPD v2 一并发布。

**EN** Stable Diffusion. For Stable Diffusion v1.4 and v2.0, we generate images of size ⟦SLOT_21⟧ using a guidance scale of 7.5 for 50 steps with DDIM sampler.

**ZH** Stable Diffusion。对 Stable Diffusion v1.4 与 v2.0，我们用 DDIM 采样器以 7.5 的引导尺度、50 步生成 ⟦SLOT_21⟧ 大小的图像。

**EN** GLIDE. Images of size ⟦SLOT_22⟧ are generated from the official mini-glide model with a guidance scale of 3.0 for 27 steps with DDIM sampler.

**ZH** GLIDE。⟦SLOT_22⟧ 大小的图像由官方 mini-glide 模型以 3.0 的引导尺度、27 步 DDIM 采样器生成。

**EN** LAFITE. Images of size ⟦SLOT_23⟧ are generated following default configuration using model** * https://drive.google.com/file/d/1tMD6MWydRDMaaM7iTOKsUK-Wv2YNDRRt/view?usp=sharing.

**ZH** LAFITE。⟦SLOT_23⟧ 大小的图像按默认配置生成，使用模型** * https://drive.google.com/file/d/1tMD6MWydRDMaaM7iTOKsUK-Wv2YNDRRt/view?usp=sharing。

**EN** VQ-Diffusion. Images of size ⟦SLOT_24⟧ are generated with a guidance scale of 5.0 and 100 sampling steps with VQ-Diffusion sampler using model†† † https://huggingface.co/microsoft/vq-diffusion-ithq.

**ZH** VQ-Diffusion。⟦SLOT_24⟧ 大小的图像以 5.0 的引导尺度、100 步 VQ-Diffusion 采样器生成，使用模型†† † https://huggingface.co/microsoft/vq-diffusion-ithq。

**EN** FuseDream. Images of size ⟦SLOT_25⟧ are generated with 1000 initialization iterations, 1000 optimization iterations and basis image number is set to 5.

**ZH** FuseDream。⟦SLOT_25⟧ 大小的图像以 1000 次初始化迭代、1000 次优化迭代生成，基图像数设为 5。

**EN** Latent Diffusion. Images are generated from the official LDM model with the DPM Solver sampler, 25 sampling steps, ⟦SLOT_26⟧, and a guidance scale of 6.0.

**ZH** Latent Diffusion。图像由官方 LDM 模型以 DPM Solver 采样器、25 步采样、⟦SLOT_26⟧、6.0 的引导尺度生成。

**EN** CogView2. Images of size ⟦SLOT_27⟧ are generated with default hyper-parameters. For category “animation”, “concept-art”, “painting” and “photo” in HPD v2, we set the “style” in Cogview2 to “none”, “none”, “oil” and “photo” respectively.

**ZH** CogView2。⟦SLOT_27⟧ 大小的图像以默认超参数生成。对 HPD v2 中的“animation”、“concept-art”、“painting”和“photo”类别，我们分别把 CogView2 的“style”设为“none”、“none”、“oil”和“photo”。

**EN** DALL·E 2. Images are directly collected by requesting the official API‡‡ ‡ https://openai.com/.

**ZH** DALL·E 2。图像通过请求官方 API‡‡ ‡ https://openai.com/ 直接采集。

**EN** Versatile Diffusion. Images are generated from the official model using the DPM Solver sampler, 25 sampling steps, and a guidance scale of 7.5.

**ZH** Versatile Diffusion。图像由官方模型以 DPM Solver 采样器、25 步采样、7.5 的引导尺度生成。

**EN** VQGAN+CLIP. Images of size ⟦SLOT_28⟧ are generated with 500 iterations and Adam optimizer with a learning rate of 0.1.

**ZH** VQGAN+CLIP。⟦SLOT_28⟧ 大小的图像以 500 次迭代、Adam 优化器、学习率 0.1 生成。

**EN** Community Models based on Stable Diffusion (Epic Diffusion, Openjourney, MajicMix Realistic, ChilloutMix, Deliberate, Realistic Vision, Dreamlike Photoreal 2.0) Images of size ⟦SLOT_29⟧ are generated from the publicly released model with the DPM Solver sampler, 25 sampling steps, and a guidance scale of 7.5.

**ZH** 基于 Stable Diffusion 的社区模型（Epic Diffusion、Openjourney、MajicMix Realistic、ChilloutMix、Deliberate、Realistic Vision、Dreamlike Photoreal 2.0）：⟦SLOT_29⟧ 大小的图像由公开发布的模型以 DPM Solver 采样器、25 步采样、7.5 的引导尺度生成。

**EN** DeepFloyd-XL Stages 1 and 2 are set to use DDPM noise schedulers with 25 sampling steps and the default samplers and guidance scales. Then the generated ⟦SLOT_30⟧ images are resized to ⟦SLOT_31⟧. For the upsampling stage, we use Stable Diffusion upscaler, with the DPM Solver sampler and 25 steps to generate ⟦SLOT_32⟧ images.

**ZH** DeepFloyd-XL 第 1 阶段与第 2 阶段均设为使用 DDPM 噪声调度器，25 步采样，采样器与引导尺度取默认值。随后生成的 ⟦SLOT_30⟧ 图像被缩放至 ⟦SLOT_31⟧。上采样阶段使用 Stable Diffusion 上采样器，以 DPM Solver 采样器和 25 步生成 ⟦SLOT_32⟧ 图像。

**EN** DALL·E mini We use the fast and minimal reproduction of the model§§ § https://huggingface.co/kuprel/min-dalle and all hyper-parameters are set to default except ⟦SLOT_33⟧.

**ZH** DALL·E mini 我们使用该模型的快速最小复现§§ § https://huggingface.co/kuprel/min-dalle，除 ⟦SLOT_33⟧ 外所有超参数取默认值。

**EN** Table 9: Pairwise Preference Prediction Accuracy of HPSv2

**ZH** 表 9：HPSv2 的两两偏好预测准确率

<!-- [原子块 · table] Model SD v1.4 SD v2.0 VQ-Diffusion LAFITE GLIDE CogView2 VQGAN+CLIP DALL·E2 COCO FuseDream 87.3% 92.5% 67.8% 79.3% 90.2% 85.5% 51.5% 90.3% 92.0% SD v1.4 - 72.0% 90.3% 92.0% 96.5% 67.5% 70.5% 78.5% 85. -->

**EN** Appendix E Pairwise Accuracy

**ZH** 附录 E 两两准确率

**EN** To further illustrate the accuracy of HPS v2, we evaluate its agreement with human choices between all pairs of generative models in test split. As shown in Tab. 9, the predictions of our model align closely with human choices between most models. We also show the chrominance and luminance distribution of each model in HPD v2 test split in Fig. 13 as a reference.

**ZH** 为进一步说明 HPS v2 的准确性，我们在测试划分中评测它与人类在所有生成模型两两组合上选择的一致程度。如表 9 所示，我们的模型预测与大多数模型组合上的人类选择高度吻合。我们还在图 13 中给出 HPD v2 测试划分中各模型的色度与亮度分布，以供参考。

**EN** Appendix F Ablation Study

**ZH** 附录 F 消融实验

**EN** We ablate hyper-parameter choices of training HPS v2 on Tab. 12, Tab. 12, Tab. 12.

**ZH** 我们在表 12、表 12、表 12 中消融了训练 HPS v2 的超参数选择。

**EN** Table 10: Ablation studies on learning rates.

**ZH** 表 10：关于学习率的消融实验。

<!-- [原子块 · table] LR/ × 10 − 6 \times 10^{-6} HPD v2 7.5 82.93 5.6 82.93 4.6 83.13 3.6 83.19 3.0 83.13 2.5 83.13 2.0 83.05 0.5 81.79 3.3 83.27 -->

**EN** Table 11: Ablation studies on # of free layers in the image encoder.

**ZH** 表 11：关于图像编码器中可训练层数的消融实验。

<!-- [原子块 · table] Image Layers HPD v2 30 83.14 25 83.23 15 82.99 10 82.73 5 82.30 0 78.37 20 83.27 -->

**EN** Table 12: Ablation studies on # of free layers in the text encoder.

**ZH** 表 12：关于文本编码器中可训练层数的消融实验。

<!-- [原子块 · table] Text Layers HPD v2 22 83.07 16 83.29 13 83.26 9 83.15 6 83.01 0 82.89 11 83.27 -->

**EN** Appendix G Example Usages of HPS v2

**ZH** 附录 G HPS v2 的用例

**EN** We show 2 example usages of HPS v2 in this section to show its sensitivity and accuracy.

**ZH** 本节给出 HPS v2 的 2 个用例，以展示其敏感性与准确性。

<!-- [原子块 · img]  -->

**EN** Figure 11: Examples of HPS v2 evaluated on community models.

**ZH** 图 11：HPS v2 在社区模型上的评测示例。

<!-- [原子块 · img]  -->

**EN** Figure 12: Left: the standard denoising inference. Right: blending the random initial noise with a prior image. The input random noise has strong influence on the layout of the generated image.

**ZH** 图 12：左：标准去噪推理。右：把随机初始噪声与一幅先验图像混合。输入的随机噪声对生成图像的布局影响很大。

**EN** G.1 Retrieval initialization

**ZH** G.1 检索初始化

**EN** Method. Many recent works [26] suggest that the latent feature initialization has a great influence on the output image quality of Stable Diffusion. We observe that this may relate to a misalignment between the noise schedule of training and inference process. We find that when training Stable Diffusion, there isn’t a timestep at which the input latent feature is fully random, but at inference time the image is recovered from random noise, which is inconsistent with the training stage. This implies that the inference of Stable Diffusion can be potentially improved by initializing with better latent features. With this observation, we try a straightforward idea of blending the latent feature of a reference image with random noise to initialize the latent features.

**ZH** 方法。近来的许多工作[26]表明，潜特征初始化对 Stable Diffusion 的输出图像质量影响很大。我们观察到这可能与训练和推理过程噪声调度的不一致有关：训练 Stable Diffusion 时，并不存在某个时间步使输入潜特征完全随机；而推理时图像却从随机噪声中恢复，这与训练阶段不一致。这意味着用更好的潜特征初始化有可能改进 Stable Diffusion 的推理。基于这一观察，我们尝试了一个直接的想法：把一幅参考图像的潜特征与随机噪声混合，用以初始化潜特征。

**EN** Given a prompt, a prior image is generated by a powerful community model Dreamlike Photoreal 2.0, and then the image is encoded into latent space with noise level similar to the training stage. The noisy latent feature is used to initialize the inference of Stable Diffusion, which is previously sampled from ⟦SLOT_34⟧ without prior.

**ZH** 给定提示词，先由一个强大的社区模型 Dreamlike Photoreal 2.0 生成一幅先验图像，再把该图像编码到潜空间，使其噪声水平与训练阶段相近。该带噪潜特征用于初始化 Stable Diffusion 的推理，而此前推理是从 ⟦SLOT_34⟧ 采样、不含先验。

**EN** Results. We verify the effectiveness of this method by comparing it with the default initialization of Stable Diffusion. Tab.13 demonstrates that the improvement brought by initializing via retrieved images can be verified by HPS v2. Visualizations in Fig.12 also show that the noise initialization has a strong impact on the global layout of the generated image, thus randomly initializing it may lead to undesired image layouts.

**ZH** 结果。我们通过与 Stable Diffusion 的默认初始化作比较来验证该方法的有效性。表 13 表明，用检索图像初始化带来的提升可以被 HPS v2 检出。图 12 的可视化也显示，噪声初始化对生成图像的全局布局影响很大，因而随机初始化可能导致不理想的图像布局。

**EN** G.2 Evaluating adapted model in HPS v1

**ZH** G.2 评测 HPS v1 中的适配模型

**EN** Wu et al.[32] improves Stable Diffusion to better align it with human preference, as introduced in HPS v1. However, the improvement is only validated through user studies. There are two reasons that prevent the authors from evaluating via HPS v1. Firstly, the bias of HPS v1 and the evaluation prompts are under-studied, so HPS v1 is not ready for serving as an evaluation metric. Secondly, HPS v1 also incorporates the training of the adapted model. With HPS v2, we are now able to quantify the actual improvement of the method, as shown in Tab.13.

**ZH** Wu 等人[32] 改进了 Stable Diffusion，使其更好地与人类偏好对齐（如 HPS v1 中所介绍）。但该改进只通过用户研究验证。有两个原因使作者无法用 HPS v1 评测：其一，HPS v1 的偏差与评测提示词研究不足，尚不足以充当评测指标；其二，HPS v1 本身也包含了该适配模型的训练。有了 HPS v2，我们如今能够量化该方法的实际改进，如表 13 所示。

**EN** Table 13: Example usages of HPS v2.

**ZH** 表 13：HPS v2 的用例。

<!-- [原子块 · table] Method Animation Concept-art Painting Photo Stable Diffusion v1.4 [ 23 ] 27.26 26.61 26.66 27.27 Retrieval initialization 27.39 26.59 26.71 27.46 Human-aligned tuning [ 32 ] 27.80 27.16 27.24 27.60 -->

**EN** Figure 13: Chrominance and luminance distribution of images in HPD v2 test split

**ZH** 图 13：HPD v2 测试划分中图像的色度与亮度分布

<!-- [原子块 · object]  -->

<!-- [原子块 · object]  -->

<!-- [原子块 · object]  -->

**EN** Appendix H Datasheet

**ZH** 附录 H 数据说明书

**EN** H.1 Motivation

**ZH** H.1 动机

**EN** Why was the dataset created?

**ZH** 为何创建该数据集？

**EN** The dataset was created to facilitate future academic Computer Vision research about human aesthetic preference.

**ZH** 该数据集的创建旨在促进未来关于人类审美偏好的计算机视觉学术研究。

**EN** Who created this dataset (e.g.which team, research group) and on behalf of which entity (e.g.company, institution, organization)?

**ZH** 该数据集由谁创建（例如哪个团队、研究组），代表哪个实体（例如公司、机构、组织）？

**EN** The dataset was created by researchers at MMLab, The Chinese University of Hong Kong and Centre for Perceptual and Interactive Intelligence (CPII).

**ZH** 该数据集由香港中文大学 MMLab 与感知与交互智能中心（CPII）的研究人员创建。

**EN** H.2 Composition

**ZH** H.2 构成

**EN** What do the instances that comprise the dataset represent (e.g.documents, photos, people, countries)? Are there multiple types of instances? (e.g.movies, users, ratings; people, interactions between them; nodes, edges)

**ZH** 构成数据集的实例代表什么（例如文档、照片、人物、国家）？是否存在多种类型的实例（例如电影、用户、评分；人物及其交互；节点、边）？

**EN** The instances are prompts and generated images, along with human preference choices among the images generated by the same prompt.

**ZH** 实例为提示词与生成图像，以及人类在同一提示词所生成图像之间的偏好选择。

**EN** Are relationships between instances made explicit in the data (e.g.social network links, user/movie ratings, etc.)?

**ZH** 实例之间的关系是否在数据中显式给出（例如社交网络链接、用户／电影评分等）？

**EN** No, we did not track the annotator identity of each instance.

**ZH** 否，我们没有追踪每条实例所对应的标注者身份。

**EN** How many instances are there? (of each type, if appropriate)?

**ZH** 有多少个实例？（如适用，请按类型分别说明）

**EN** There are 789,090 instances in the dataset, standing for 789,090 comparisons between image pairs. Specifically, our dataset has 433,760 images and 107,515 prompts. The benchmark contains 3200 unique prompts without paired images.

**ZH** 数据集中有 789,090 条实例，代表图像对之间的 789,090 次比较。具体地，我们的数据集有 433,760 幅图像和 107,515 条提示词。基准包含 3200 条不配对图像的独立提示词。

**EN** What data does each instance consist of? “Raw” data (e.g.unprocessed text or images) or Features/attributes? Is there a label/target associated with instances? If the instances related to people, are sub-populations identified (e.g.by age, gender, etc.) and what is their distribution?

**ZH** 每条实例由哪些数据构成？是“原始”数据（例如未处理的文本或图像）还是特征／属性？实例是否带标签／目标？若实例与人相关，是否标识了子群体（例如按年龄、性别等）及其分布？

**EN** Each instance consists of two images, one prompt and one human choice.

**ZH** 每条实例由两幅图像、一条提示词和一个人类选择构成。

**EN** Is any information missing from individual instances? If so, please provide a description, explaining why this information is missing (e.g.because it was unavailable). This does not include intentionally removed information, but might include, e.g.redacted text.

**ZH** 单条实例是否缺失某些信息？若有，请给出说明，解释这些信息为何缺失（例如因为无法获取）。这不包括有意移除的信息，但可能包括例如被涂黑的文本。

**EN** Yes, we omit the specific parameters for generating the images, such as diffusion steps and guidance scale. They are omitted because we are more interested in the users’ preference about the generated images, rather than how they are created. Instead, we illustrate the hyper-parameters used for generation in Appendix D.

**ZH** 是，我们省略了生成图像的具体参数，例如扩散步数与引导尺度。之所以省略，是因为我们更关注用户对生成图像本身的偏好，而非图像如何生成。我们把生成所用超参数的说明放在附录 D。

**EN** Is everything included or does the data rely on external resources?

**ZH** 数据是否全部包含在内，还是依赖外部资源？

**EN** The dataset is self-contained.

**ZH** 该数据集是自包含的。

**EN** Are there recommended data splits and evaluation measures? (e.g.training, development, testing; accuracy or AUC)

**ZH** 是否有推荐的数据划分与评测度量（例如训练、开发、测试；准确率或 AUC）？

**EN** For the preference model training, we use a training set of 645,090 instances and a validation set of 153,000 instances. We recommend using accuracy (%) with 1 decimal place. For evaluating text-to-image generative models, we recommend reporting HPS v2 with 4 decimal place, as well as the standard deviation.

**ZH** 训练偏好模型时，我们使用含 645,090 条实例的训练集和含 153,000 条实例的验证集。我们推荐使用保留 1 位小数的准确率（%）。评测文本到图像生成模型时，我们建议报告保留 4 位小数的 HPS v2 以及标准差。

**EN** Are there any errors, sources of noise, or redundancies in the dataset?

**ZH** 数据集中是否存在错误、噪声来源或冗余？

**EN** There is potential noise in the dataset. Since human preference is highly diverse, in most cases, it’s hard to tell whether the divergence in human choice is due to noise or disagreement of aesthetic criterion.

**ZH** 数据集中存在潜在噪声。由于人类偏好高度多样，多数情况下很难判断人类选择的分歧究竟源于噪声，还是源于审美标准的不同。

**EN** Is the dataset self-contained, or does it link to or otherwise rely on external resources (e.g.websites, tweets, other datasets)?

**ZH** 该数据集是否自包含，是否链接或依赖外部资源（例如网站、推文、其他数据集）？

**EN** The dataset is self-contained.

**ZH** 该数据集是自包含的。

**EN** Does the dataset contain data that might be considered confidential (e.g.data that is protected by legal privilege or by doctorpatient confidentiality, data that includes the content of individuals non-public communications)?

**ZH** 数据集是否包含可能被视为机密的数据（例如受法律特权或医患保密保护的数据、包含个人非公开通信内容的数据）？

**EN** No, both prompt sources (DiffusionDB and COCO Captions) and image generative models are publicly available.

**ZH** 否，两处提示词来源（DiffusionDB 与 COCO Captions）以及图像生成模型都是公开可用的。

**EN** Does the dataset contain data that, if viewed directly, might be offensive, insulting, threatening, or might otherwise cause anxiety? If so, please describe why.

**ZH** 数据集是否包含直接查看时可能令人不适、侮辱性、威胁性或可能引发焦虑的内容？若有，请说明原因。

**EN** We retained the prompts with NSFW scores below a threshold and accepted by DALL·E2. However, there may still be an extremely small portion of inappropriate content that were not removed by our policy.

**ZH** 我们保留了 NSFW 分数低于阈值、且被 DALL·E2 接受的提示词。不过仍可能有极小部分不当内容未被我们的策略剔除。

**EN** Does the dataset relate to people?

**ZH** 该数据集是否与人相关？

**EN** Yes, the choices are made by human annotators.

**ZH** 是，这些选择由人类标注者作出。

**EN** Does the dataset identify any subpopulations (e.g.by age, gender)?

**ZH** 数据集是否标识了任何子群体（例如按年龄、性别）？

**EN** No, but we report the statistics of subpopulations by age, gender and occupancy.

**ZH** 否，但我们报告了按年龄、性别和职业划分的子群体统计。

**EN** Is it possible to identify individuals (i.e.one or more natural persons), either directly or indirectly (i.e.in combination with other data) from the dataset?

**ZH** 是否可能从数据集中直接或间接（即结合其他数据）识别出个体（一个或多个自然人）？

**EN** No.

**ZH** 否。

**EN** Does the dataset contain data that might be considered sensitive in any way (e.g.data that reveals racial or ethnic origins, sexual orientations, religious beliefs, political opinions or union memberships, or locations; financial or health data; biometric or genetic data; forms of government identification, such as social security numbers; criminal history)?

**ZH** 数据集是否包含任何可能被视为敏感的数据（例如揭示种族或族裔出身、性取向、宗教信仰、政治观点或工会成员身份、地理位置的数据；财务或健康数据；生物识别或基因数据；政府身份标识如社会保障号；犯罪记录）？

**EN** The dataset may contain sensitive data, because the prompts are sourced from DiffusionDB, which are collected from users. Thus, it may contain sensitive information, such as public figures and religious beliefs.

**ZH** 数据集可能包含敏感数据，因为提示词来自 DiffusionDB，而后者采集自用户，因此可能包含公众人物、宗教信仰等敏感信息。

**EN** What experiments were initially run on this dataset? Have a summary of those results.

**ZH** 最初在该数据集上开展了哪些实验？请给出结果摘要。

**EN** We firstly collected the test split to evaluate existing preference prediction models and found that they do not align well with human choices. Details are illustrated in Tab. 6. Based on this, we collected the large scale training split of HPD v2 and train a more aligned preference prediction model.

**ZH** 我们先采集了测试划分，用于评测现有偏好预测模型，发现它们与人类选择吻合不佳，详见表 6。在此基础上，我们采集了 HPD v2 的大规模训练划分，并训练出对齐程度更高的偏好预测模型。

**EN** H.3 Data Collection Process

**ZH** H.3 数据采集过程

**EN** How was the data associated with each instance acquired?

**ZH** 每条实例关联的数据是如何获取的？

**EN** Each instance contain two images generated from the same prompt, and a human choice annotation.

**ZH** 每条实例包含由同一提示词生成的两幅图像，以及一个人类选择标注。

**EN** What mechanisms or procedures were used to collect the data (e.g.hardware apparatus or sensor, manual human curating, software program, software API)?

**ZH** 采集数据使用了哪些机制或流程（例如硬件装置或传感器、人工整理、软件程序、软件 API）？

**EN** We use ChatGPT API provided by OpenAI to process prompts from DiffusionDB and an annotation system.

**ZH** 我们使用 OpenAI 提供的 ChatGPT API 处理 DiffusionDB 的提示词，并使用一套标注系统。

**EN** If the dataset is a sample from a larger set, what was the sampling strategy (e.g.deterministic, probabilistic with specific sampling probabilities)?

**ZH** 若该数据集是从更大集合中采样得到的，采样策略是什么（例如确定性采样，或按特定概率的概率采样）？

**EN** The dataset is not a sample of a larger set.

**ZH** 该数据集并非某个更大集合的样本。

**EN** Who was involved in the data collection process (e.g.students, crowd-workers, contractors) and how were they compensated (e.g.how much were crowdworkers paid)?

**ZH** 谁参与了数据采集过程（例如学生、众包工作者、合同工），他们如何获得报酬（例如众包工作者获得多少报酬）？

**EN** We hire 57 annotators for human preference annotation, but they prefer not to disclose their salary information due to personal privacy reasons.

**ZH** 我们雇用了 57 名标注者进行人类偏好标注，但出于个人隐私原因，他们不愿披露薪酬信息。

**EN** Over what time-frame was the data collected?

**ZH** 数据采集的时间跨度是多久？

**EN** The dataset was collected between 2023-03-15 and 2023-06-03.

**ZH** 数据集采集于 2023-03-15 至 2023-06-03 之间。

**EN** Were any ethical review processes conducted (e.g.by an institutional review board)?

**ZH** 是否开展了伦理审查流程（例如由机构审查委员会）？

**EN** No official process is conducted.

**ZH** 未开展任何官方流程。

**EN** Does the dataset relate to people?

**ZH** 该数据集是否与人相关？

**EN** No. Although crowdsourcing was used for annotation, we didn’t perform any kind of intervention or interaction during data collection and didn’t collect any personal information or biospecimens of annotators. It’s not possible to identify individuals from our dataset. In addition, according to the definition of ‘‘Human Subjects Research’’ given by NIH(National Institutes of Health of USA)¶¶ ¶ https://grants.nih.gov/policy/humansubjects/research.htm, our research is not regarded as “research with human subjects”.

**ZH** 否。尽管标注采用了众包方式，我们在数据采集过程中没有进行任何干预或交互，也没有收集标注者的任何个人信息或生物样本，无法从我们的数据集中识别个体。此外，按照美国国立卫生研究院（NIH）¶¶ ¶ https://grants.nih.gov/policy/humansubjects/research.htm 对“人类受试者研究”的定义，我们的研究不属于“涉及人类受试者的研究”。

**EN** Did you collect the data from the individuals in question directly, or obtain it via third parties or other sources (e.g.websites)?

**ZH** 你是直接从相关个人处采集数据，还是通过第三方或其他来源（例如网站）获得？

**EN** We collected human choices directly from annotators in question.

**ZH** 我们直接从相关标注者处采集人类选择。

**EN** Has an analysis of the potential impact of the dataset and its use on data subjects (e.g.a data protection impact analysis) been conducted?

**ZH** 是否针对数据集及其使用对数据主体的潜在影响开展过分析（例如数据保护影响分析）？

**EN** No analysis has been conducted.

**ZH** 未开展任何分析。

**EN** H.4 Data Preprocessing

**ZH** H.4 数据预处理

**EN** What preprocessing/cleaning was done? (e.g.discretization or bucketing, tokenization, part-of-speech tagging, SIFT feature extraction, removal of instances, processing of missing values)?

**ZH** 做了哪些预处理／清洗（例如离散化或分桶、分词、词性标注、SIFT 特征提取、移除实例、缺失值处理）？

**EN** We conducted prompt cleaning process using ChatGPT to remove biased functional words. Please see Sec. A and Sec. 3.1 for details.

**ZH** 我们用 ChatGPT 进行了提示词清洗，以去除带偏差的功能词。详见第 A 节与第 3.1 节。

**EN** H.5 Uses

**ZH** H.5 用途

**EN** Has the dataset been used for any tasks already? If so, please provide a description.

**ZH** 该数据集是否已用于某些任务？若有，请给出说明。

**EN** As described in the paper, this dataset has been used for training HPS v2.

**ZH** 如论文所述，该数据集已用于训练 HPS v2。

**EN** Is there a repository that links to any or all papers or systems that use the dataset?

**ZH** 是否存在链接到使用该数据集的论文或系统的仓库？

**EN** No.

**ZH** 否。

**EN** What (other) tasks could the dataset be used for?

**ZH** 该数据集还可用于哪些（其他）任务？

**EN** It can be used for tasks related to human preference on generated images.

**ZH** 可用于与生成图像上的人类偏好相关的任务。

**EN** Is there anything about the composition of the dataset or the way it was collected and preprocessed/cleaned/labeled that might impact future uses?

**ZH** 数据集的构成方式，或其采集、预处理／清洗／标注方式，是否存在可能影响未来使用的因素？

**EN** Yes. As discussed in Sec. 6, there might be bias induced by the limited number of annotators.

**ZH** 是。如第 6 节所讨论，标注者数量有限可能引入偏差。

**EN** Are there tasks for which the dataset should not be used?

**ZH** 是否存在不应使用该数据集的任务？

**EN** No.

**ZH** 否。

**EN** H.6 Data Distribution

**ZH** H.6 数据分发

**EN** Will the dataset be distributed to third parties outside of the entity (e.g.company, institution, organization) on behalf of which the dataset was created? If so, please provide a description

**ZH** 数据集是否会分发给创建该数据集的实体之外的第三方（例如公司、机构、组织）？若是，请给出说明。

**EN** Yes. Anyone can access the dataset via the internet.

**ZH** 是。任何人都可以通过互联网访问该数据集。

**EN** How will the dataset be distributed? (e.g.tarball on website, API, GitHub; does the data have a DOI and is it archived redundantly?)

**ZH** 数据集将如何分发（例如网站上的压缩包、API、GitHub；数据是否有 DOI，是否做了冗余归档）？

**EN** We will provide a download link in a GitHub repository.

**ZH** 我们将在 GitHub 仓库中提供下载链接。

**EN** When will the dataset be distributed?

**ZH** 数据集将于何时分发？

**EN** When the paper is accepted.

**ZH** 论文被录用之时。

**EN** Will the dataset be distributed under a copyright or other intellectual property (IP) license, and/or under applicable terms of use (ToU)?

**ZH** 数据集是否将在版权或其他知识产权（IP）许可、和／或适用的使用条款（ToU）下分发？

**EN** We will provide a terms-of-use agreement with the dataset. The dataset as a whole is distributed under Apache 2.0 license.

**ZH** 我们将随数据集提供一份使用条款协议。数据集整体以 Apache 2.0 许可分发。

**EN** Have any third parties imposed IP-based or other restrictions on the data associated with the instances? If so, please describe these restrictions, and provide a link or other access point to, or otherwise reproduce, any relevant licensing terms, as well as any fees associated with these restrictions.

**ZH** 是否有第三方对与实例相关的数据施加了基于 IP 或其他限制？若有，请说明这些限制，并提供相关许可条款的链接或其他获取途径，或以其他方式复现这些条款，以及这些限制涉及的费用。

**EN** No.

**ZH** 否。

**EN** Do any export controls or other regulatory restrictions apply to the dataset or to individual instances? If so, please describe these restrictions, and provide a link or other access point to, or otherwise reproduce, any supporting documentation.

**ZH** 是否有出口管制或其他法规限制适用于该数据集或个别实例？若有，请说明这些限制，并提供支持性文件的链接或其他获取途径，或以其他方式复现这些文件。

**EN** Unknown.

**ZH** 未知。

**EN** H.7 Dataset Maintenance

**ZH** H.7 数据集维护

**EN** Who is supporting/hosting/maintaining the dataset?

**ZH** 谁在支持／托管／维护该数据集？

**EN** The authors of this paper are maintainers of this dataset.

**ZH** 本论文的作者是该数据集的维护者。

**EN** How can the owner/curator/manager of the dataset be contacted (e.g.email address)?

**ZH** 如何联系数据集的所有者／管理者／负责人（例如电子邮件地址）？

**EN** By email: wuxiaoshi@link.cuhk.edu.hk.

**ZH** 通过电子邮件：wuxiaoshi@link.cuhk.edu.hk。

**EN** Is there an erratum?

**ZH** 是否存在勘误？

**EN** At this time, we are not aware of errors in our dataset. However, we will create an erratum as errors are identified.

**ZH** 目前我们尚未发现数据集中的错误。不过一旦发现错误，我们将发布勘误。

**EN** Will the dataset be updated? If so, how often and by whom? How will updates be communicated? (e.g.mailing list, GitHub)

**ZH** 数据集是否会更新？若是，更新频率如何、由谁更新？更新将如何告知（例如邮件列表、GitHub）？

**EN** Yes, the dataset will be updated when necessary. The dataset will be updated when:

**ZH** 会，数据集将在必要时更新。更新的时机包括：

**EN** • inappropriate content is spotted in the dataset.

**ZH** • 在数据集中发现不当内容。

**EN** • HPS v2 loses consistency with human preferences for new generative models.

**ZH** • HPS v2 与人类偏好在新的生成模型上失去一致性。

**EN** • other improvements are available.

**ZH** • 出现其他改进。

**EN** Updates will be recorded in the GitHub repository∥∥ ∥ https://github.com/tgxs002/HPSv2.

**ZH** 更新将记录在 GitHub 仓库∥∥ ∥ https://github.com/tgxs002/HPSv2 中。

**EN** Will older versions of the dataset continue to be supported/hosted/maintained?

**ZH** 旧版本数据集是否继续获得支持／托管／维护？

**EN** Yes.

**ZH** 是。

**EN** If others want to extend/augment/build on this dataset, is there a mechanism for them to do so? If so, is there a process for tracking/assessing the quality of those contributions. What is the process for communicating/distributing these contributions to users?

**ZH** 若他人希望扩展／增补／在此数据集上构建，是否有相应机制？若有，是否存在跟踪／评估这些贡献质量的流程？这些贡献通过何种流程告知并分发给用户？

**EN** The authors reserve the right to maintain the dataset.

**ZH** 作者保留维护该数据集的权利。
