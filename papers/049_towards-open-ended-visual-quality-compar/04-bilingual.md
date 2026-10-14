# 面向开放式视觉质量比较

> 原标题：Towards Open-ended Visual Quality Comparison
> 作者：Haoning Wu, Hanwei Zhu, Zicheng Zhang, Erli Zhang, Chaofeng Chen, Liang Liao, Chunyi Li, Annan Wang, Wenxiu Sun, Qiong Yan, Xiaohong Liu, Guangtao Zhai 等 · arXiv:2402.16641 · 2024-02-26

<!-- [原子块 · verbatim] Towards Open-ended Visual Quality Comparison -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] Comparative settings ( e.g . pairwise choice, listwise ranking ) have been adopted by a wide range of subjective studies for image quality assessment (IQA), as it inherently standardizes the evaluatio -->

**EN** Keywords:

**ZH** 关键词：

<!-- [原子块 · img]  -->

**EN** Figure 1: The proposed Co-Instruct, first-of-its-kind open-source LMM with capability on open-question & detailed-reasoning visual quality comparison. It outperforms existing LMMs on the proposed MICBench as well as existing quality evaluation benchmarks.

**ZH** 图 1：本文提出的 Co-Instruct——首个具备开放式提问与详细推理能力的开源大型多模态模型（LMM）视觉质量比较器。它在本文提出的 MICBench 以及已有质量评测基准上均优于现有 LMM。

<!-- [原子块 · img]  -->

**EN** Figure 2: The motivation of open-ended visual quality comparison: comparative settings can effectively avoid the ambiguity on absolute evaluations for single images, and provide more clear-cut judgements to serve as downstream guidances [53, 65].

**ZH** 图 2：开放式视觉质量比较的动机：比较式设定能有效避免单图像绝对评价中的歧义，并提供更明确的判断，以作为下游指导 [53, 65]。

**EN** 1 Introduction

**ZH** 1 引言

**EN** Image quality assessment (IQA) has been an important domain in visual computing, as it provides effective recommendation [57] on high-quality visual contents and valuable guidance [53, 61, 65] for potential improvements. Most recently, several pioneer studies [50, 49, 51] have explored large multi-modality models (LMMs, e.g. GPT-4V) [34, 9, 25, 56, 4, 5], on expanding IQA from giving a scalar score (e.g. 3.457) to the open-ended scenarios, that allows evaluations in response to open-range questions, and provide detailed reasonings beyond an overall score.

**ZH** 图像质量评价（IQA）一直是视觉计算中的重要领域，它为高质量视觉内容提供有效的推荐 [57]，并为潜在的改进提供有价值的指导 [53, 61, 65]。近来，若干开创性研究 [50, 49, 51] 探索了把大型多模态模型（LMM，例如 GPT-4V）[34, 9, 25, 56, 4, 5] 用于把 IQA 从给出一个标量分数（如 3.457）拓展到开放式场景——既能针对开放式问题给出评价，也能在整体分数之外提供详细推理。

**EN** While these studies sufficiently emulate human ability on IQA, they also suffer from the same drawback as human: ambiguity on absolute evaluations. For instance, as shown in Fig. 2 (a), different human observers hold different standards on the exposure level on single images, and henceforth provide diversified absolute evaluations. Nevertheless, while asked to compare the exposure level of the images, all observers agree with the rank (1)>(2)>(3)>(4) (Fig. 2(b)); all observers also agree that (1) has the highest exposure, though not all choose the option high while evaluating it independently. Given this observation, comparison has been a traditional human study setting for quality evaluation [43] and adopted by a wide range of existing subjective studies [35, 62, 10, 53, 52]. Furthermore, to avoid the ambiguity, the comparative settings are also predomintantly adopted [65, 53] while applying IQA algorithms for improvement guidance.

**ZH** 这些研究虽已充分模拟人类的 IQA 能力，却也带有人类自身的同一缺陷：绝对评价上的歧义。例如，如图 2(a) 所示，不同观察者对单张图像的曝光水平持有不同标准，因而给出各异的绝对评价。然而，当被要求比较这些图像的曝光水平时，所有观察者都认同 (1)>(2)>(3)>(4) 这一排序（图 2(b)）；所有观察者也都认同 (1) 的曝光最高，尽管在独立评价时并非所有人都选择「高」这一选项。基于这一观察，比较一直是质量评价中传统的人类研究设定 [43]，并被大量已有主观研究所采用 [35, 62, 10, 53, 52]。此外，为避免歧义，在把 IQA 算法用于改进指导时，比较式设定同样被普遍采用 [65, 53]。

<!-- [原子块 · img]  -->

**EN** Figure 3: The construction methodology of Co-Instruct-562K, a combination of (a) Merge2Compare (LLM comparison from human-labeled single image quality descriptions) and (b) Teach2Compare (GPT-4V comparison on multiple unlabeled images).

**ZH** 图 3：Co-Instruct-562K 的构建方法，由 (a) Merge2Compare（把人工标注的单图像质量描述交由 LLM 合并成比较）与 (b) Teach2Compare（由 GPT-4V 对多张无标注图像进行比较）组合而成。

**EN** While comparison has widely-recognized significance for IQA, existing related datasets [35] and methods [63, 28] are generally based on overall quality comparison and have not extended to the open-ended scenarios; on the other hand, open-source LMMs [50, 25, 4] are usually only fine-tuned with single image instruction tuning datasets [26, 13, 1] and proved to lack enough capability even on two image comparison settings [67, 69]. While these gaps have clearly indicated the need of a specific instruction tuning dataset for visual quality comparison, it is too expensive to collect such a dataset from human. To avoid costly human labors, we propose an alternative strategy to collect the training dataset, named Collaborative Instruction Tuning from Weak Supervisors (Co-Instruct). Specifically, we adopt two non-perfect supervisors: 1) Merge2Compare (Fig. 3(a)). Originated from single image quality descriptions on 19K images as labeled by human in the Q-Pathway [50] dataset, we randomly match them into 100K groups (2-4 images per group) with removing the most similar descriptions with an text embedding model [44]. Then, we prompt a single-modal large language model (LLM) [16] to compare multiple human descriptions in a group, and “merge” them into 100K pseudo comparisons. 2) Teach2Compare (Fig. 3(b)). Observing that GPT-4V has especially high accuracy on pairwise settings [69, 67] among existing LMMs, following existing practices [2, 17], we leverage GPT-4V responses to further expand our dataset. We collect 9K unlabeled images and randomly match into 30K image groups (also 2-4 images per group), and obtain GPT-4V responses on both caption-like general comparisons and question-answer pairs for comparisons. By integrating Q-Instruct-200K [50] (on single images), Merge2Compare, and Teach2Compare, we construct the Co-Instruct-562K, the first instruction tuning dataset for open-ended visual quality comparison.

**ZH** 尽管比较对 IQA 的意义已获广泛认可，已有的相关数据集 [35] 与方法 [63, 28] 通常只基于整体质量比较，尚未拓展到开放式场景；另一方面，开源 LMM [50, 25, 4] 通常只用单图像指令微调数据集 [26, 13, 1] 微调，已被证明甚至在两图像比较设定下也能力不足 [67, 69]。这些空白清楚地表明，需要专门面向视觉质量比较的指令微调数据集，而从人类那里采集这样的数据集过于昂贵。为避开高昂的人力成本，我们提出一种替代性的训练数据采集策略，称为「来自弱监督者的协同指令微调」（Collaborative Instruction Tuning from Weak Supervisors, Co-Instruct）。具体地，我们采用两个并不完美的监督者：1）Merge2Compare（图 3(a)）。源自 Q-Pathway [50] 数据集中人工标注的 19K 张图像上的单图像质量描述，我们先用文本嵌入模型 [44] 剔除最相似的描述，再把它们随机匹配成 100K 组（每组 2–4 张图像）。随后，我们提示单模态大语言模型（LLM）[16] 比较组内多条人类描述，并把它们「合并」为 100K 条伪比较数据。2）Teach2Compare（图 3(b)）。鉴于 GPT-4V 在现有 LMM 中于成对设定下准确率尤其高 [69, 67]，我们沿用已有做法 [2, 17]，利用 GPT-4V 的回答进一步扩展数据集。我们采集 9K 张无标注图像，随机匹配为 30K 个图像组（同样每组 2–4 张），并获取 GPT-4V 在类描述的通用比较以及比较类问答对上的回答。通过整合 Q-Instruct-200K [50]（单图像）、Merge2Compare 与 Teach2Compare，我们构建了 Co-Instruct-562K——首个面向开放式视觉质量比较的指令微调数据集。

**EN** To correctly refer to each specific image during conversation, we define a specific image-text interleaved format [5] to handle multi-image cases, as follows: User: The first image: <img⟦SLOT_0⟧> The second image: <img⟦SLOT_1⟧> ... <query> Assistant: <response>

**ZH** 为在对话中正确指代每一张具体图像，我们定义了一种特定的图文交错格式 [5] 来处理多图像情形，如下所示：User: The first image: <img⟦SLOT_0⟧> The second image: <img⟦SLOT_1⟧> ... <query> Assistant: <response>

**EN** Moreover, as we need to feed multiple images together to the LLM decoder, adopting the most popular LLaVA [26, 39, 25] structure that linearly projects visual embeddings will exceed the context window of the language models [42] and cause errors. Henceforth, we adopt an alternative visual abstractor structure [56] to first reduce visual token length (from 1,025 to 65 tokens per image), and then concatenate them with text embeddings to pass to language decoders. By learning from the Co-Instruct-562K dataset and the specially-designed input structure, we present the Co-Instruct, with up to 86% improvements than its baseline [56], and 61% better than the state-of-the-art open-source LMM. More importantly, despite using GPT-4V as one of its teachers, it still surpasses the GPT-4V teacher in a variety of multi-choice question (MCQ) benchmarks, and matches GPT-4V ability in scenarios requiring detailed language reasonings.

**ZH** 此外，由于我们需要把多张图像一并输入 LLM 解码器，采用最流行的 LLaVA [26, 39, 25] 结构（对视觉嵌入做线性投影）会超出语言模型的上下文窗口 [42] 并导致错误。因此，我们改用另一种视觉抽象器结构 [56]，先把视觉词元长度压缩（每张图像从 1,025 个词元减到 65 个），再与文本嵌入拼接后送入语言解码器。通过在 Co-Instruct-562K 数据集上学习、并配合专门设计的输入结构，我们提出了 Co-Instruct：相比其基线 [56] 提升最多 86%，比当前最优的开源 LMM 高出 61%。更重要的是，尽管以 GPT-4V 作为其教师之一，它在多种多选题（MCQ）基准上仍超过教师 GPT-4V，并在需要详细语言推理的场景中与 GPT-4V 的能力相当。

**EN** After training the model Co-Instruct, our another concern is the lack of abundant evaluation settings on multi-image comparison: while Q-Bench [49, 67] series have covered multiple formats on single images and image pairs, there is no existing evaluation scenario for quality comparison beyond two images. To complement this evaluation setting, we construct the MICBench. Specifically, the MICBench contains 2,000 multi-choice questions (MCQ) comparing the quality or related attributes among a group of three or four images (each half), in which over half of the questions are Which questions (e.g. which image has highest clarity?). Aiming to extract an image with a specific quality-related appearance from a group, Which questions are the most important questions related to image comparison. Despite Which questions, the MICBench also includes Yes-or-No questions and other question types (What/How/How-Many, etc) to provide a holistic benchmark setting for multi-image quality comparison.

**ZH** 训练出 Co-Instruct 模型之后，我们的另一重顾虑是多图像比较评测设定的匮乏：Q-Bench [49, 67] 系列虽已覆盖单图像与图像对上的多种形式，却不存在针对两张以上图像的质量比较评测场景。为补足这一评测设定，我们构建了 MICBench。具体地，MICBench 包含 2,000 道比较一组三张或四张图像（各占一半）的质量或相关属性的多选题（MCQ），其中超过一半是 Which 类问题（例如「哪张图像清晰度最高？」）。Which 类问题旨在从一组图像中找出具有特定质量相关外观的那一张，是与图像比较相关的最重要问题类型。除 Which 类问题外，MICBench 还包含是/否类问题以及其他问题类型（What/How/How-Many 等），从而为多图像质量比较提供整体性的基准设定。

**EN** In summary, we conduct a systematical study towards open-ended visual quality comparison. Our contributions can be summarized as three-fold:

**ZH** 综上，我们对开放式视觉质量比较开展了系统性研究。我们的贡献可概括为三方面：

**EN** 1. We construct the first instruction-tuning dataset for visual quality comparison, the Co-Instruct-562K. With data collected from two “weak supervisors”, Merge2Compare (LLM-merged comparisons) and Teach2Compare (GPT-4V pseudo-labeled comparisons), our public dataset significantly expands the capabilities of open-source LMMs on visual comparative settings.

**ZH** 1. 我们构建了首个面向视觉质量比较的指令微调数据集 Co-Instruct-562K。数据来自两个「弱监督者」——Merge2Compare（LLM 合并的比较）与 Teach2Compare（GPT-4V 伪标注的比较）；这一公开数据集显著扩展了开源 LMM 在视觉比较设定下的能力。

**EN** 2. We propose the most capable model for open-ended visual comparison, the Co-Instruct. With image-text interleaved input format and fine-tuned with the Co-Instruct-562K dataset, it significantly outperforms existing methods (and even GPT-4V) in multiple open-ended visual comparison tasks. With open weights, it allows for broader application than proprietary models.

**ZH** 2. 我们提出当前最强的开放式视觉比较模型 Co-Instruct。它采用图文交错的输入格式，并在 Co-Instruct-562K 数据集上微调，在多个开放式视觉比较任务上显著优于现有方法（甚至包括 GPT-4V）。由于权重开源，它比专有模型更便于广泛应用。

**EN** 3. We construct the benchmark, the MICBench, as the first benchmark to evaluate LMMs for quality comparison on multiple images (more than two). It covers 2,000 diverse-type open-range MCQs related to visual quality comparison among three or four images. The MICBench contributes to more holistic evaluation studies on the visual quality comparison problem.

**ZH** 3. 我们构建了基准 MICBench——首个评测 LMM 在两张以上图像上进行质量比较的基准。它涵盖 2,000 道与三张或四张图像的视觉质量比较相关的、类型多样的开放式多选题。MICBench 有助于推动视觉质量比较问题上更具整体性的评测研究。

**EN** 2 Related Works

**ZH** 2 相关工作

**EN** 2.1 Visual Quality Comparison

**ZH** 2.1 视觉质量比较

**EN** Visual quality comparison (especially paired comparison) is a widely used subjective quality assessment methodology, serving as the most reliable way to collect human opinions [31]. However, when the number of images increases, the experiments become infeasible because of the exponential growth of pairwise comparisons [14]. While many active sampling methods have been proposed to reduce the number of pairs [54, 21, 33], they are computationally expensive and unsuitable for large-scale experiments. Despite subjective studies, learning to rank quality is widely proven as effective by many objective approaches [27, 30, 8, 63, 46, 48, 64]. Nonetheless, they typically only predict a scalar score or a binary judgement for overall comparison, limiting their ability to provide meaningful feedbacks into specific types of distortions or preferences.

**ZH** 视觉质量比较（尤其是成对比较）是一种被广泛使用的主观质量评价方法，被视为收集人类意见最可靠的途径 [31]。然而，当图像数量增加时，由于成对比较数量呈指数增长 [14]，实验会变得不可行。尽管已有许多主动采样方法被提出以减少配对数量 [54, 21, 33]，它们计算开销大，不适合大规模实验。除主观研究之外，学习对质量排序的有效性也已被大量客观方法所证实 [27, 30, 8, 63, 46, 48, 64]。不过，这些方法通常只预测一个标量分数，或对整体比较给出二值判断，限制了它们针对具体失真类型或偏好提供有意义反馈的能力。

**EN** 2.2 LMMs for Visual Quality Evaluation

**ZH** 2.2 用于视觉质量评价的 LMM

**EN** Several recent studies have explored LMMs for visual quality evaluation. The Q-Bench [49] proposes a holistic benchmark for LMMs on low-level perception (quality-related MCQs), description (quality-related captioning) and assessment (predicting scores). Following this path, Q-Instruct [50] advances the ability of LMMs with a large-scale human-annotated dataset, and Q-Align [51] designs a text-guided instruction tuning for score predictions and outperforms non-LMM approaches. However, these explorations are based on single images and have not covered comparative settings. While most recent benchmarks [67, 69] suggest that open-source LMMs trained with single image datasets cannot perform well on comparative settings, to bridge this gap, we collect the first instruction tuning dataset to teach LMMs to compare visual quality, the Co-Instruct-562K, and our model significantly improves the ability of open-source LMMs on comparative settings, moving a step forward on the basis of existing explorations.

**ZH** 若干近期研究探索了把 LMM 用于视觉质量评价。Q-Bench [49] 提出了一个面向 LMM 的整体性基准，涵盖底层感知（质量相关多选题）、描述（质量相关描述生成）与评价（分数预测）。沿此路径，Q-Instruct [50] 用大规模人工标注数据集提升了 LMM 的能力，Q-Align [51] 则为分数预测设计了文本引导的指令微调，并超过了非 LMM 方法。然而，这些探索都基于单张图像，尚未覆盖比较式设定。尽管最近的基准 [67, 69] 表明，用单图像数据集训练的开源 LMM 在比较式设定下表现不佳，为弥合这一空白，我们收集了首个教 LMM 比较视觉质量的指令微调数据集 Co-Instruct-562K；我们的模型显著提升了开源 LMM 在比较式设定下的能力，在已有探索的基础上又前进了一步。

**EN** Table 1: Statistics of our Co-Instruct-562K dataset. ‘#’ denotes “the number of”.

**ZH** 表 1：Co-Instruct-562K 数据集的统计。‘#’ 表示「数量」。

<!-- [原子块 · table] Subsets Q-Instruct-200K [ 50 ] Merge2Compare Teach2Compare - general Teach2Compare - Q&A All Instruction Type Detailed Reasoning, Question Answering Detail Reasoning Detail Reasoning Question Answerin -->

**EN** 3 Data Construction

**ZH** 3 数据构建

**EN** In this section, we elaborate on the construction process of the Co-Instruct-562K dataset. Though human annotation is the most direct approach to collect data, as is widely acknowledged [21, 54], acquiring sufficient comparative data on a large set of images demands a markedly increased volume of human annotations [10, 35] in contrast to gathering opinions on the same set of individual images. To avoid this unbearable cost, we propose an alternative data construction strategy without additional human annotation, by following three key principles:

**ZH** 本节详述 Co-Instruct-562K 数据集的构建过程。人工标注虽是采集数据最直接的途径，但正如被广泛认同的那样 [21, 54]，要在大量图像上获得充分的比较数据，所需的人工标注量 [10, 35] 相对采集同批单张图像的意见而言会显著增加。为避开这一难以承受的成本，我们提出一种无需额外人工标注的替代数据构建策略，遵循三条关键原则：

**EN** 1. Convert: Utilize reliable information from existing datasets.

**ZH** 1. Convert（转换）：利用已有数据集中的可靠信息。

**EN** 2. Learn-from-Model: Leverage the verified capabilities of models.

**ZH** 2. Learn-from-Model（从模型中学习）：借助已被验证的模型能力。

**EN** 3. Co-Instruct: Collecting diverse subsets that complement each other.

**ZH** 3. Co-Instruct（协同指令微调）：采集彼此互补的多样化子集。

**EN** Under the principles, we collect two different subsets for instruction tuning: Merge2Compare (Sec. 3.1), which converts information from human quality descriptions on single images, and the ability of single-modal LLMs on comparing and analyzing texts; and Teach2Compare (Sec. 3.2), which leverages the verified ability of GPT-4V on comparing images. Finally, we discuss how the two subsets complement each other (Sec. 3.3) under a co-instruct scheme.

**ZH** 在这些原则下，我们采集了两个不同的指令微调子集：Merge2Compare（第 3.1 节），它把单图像上的人类质量描述信息与单模态 LLM 比较、分析文本的能力加以转换；以及 Teach2Compare（第 3.2 节），它借助 GPT-4V 已被验证的图像比较能力。最后，我们在第 3.3 节讨论这两个子集如何在协同指令微调（co-instruct）方案下彼此互补。

**EN** 3.1 Merge2Compare.

**ZH** 3.1 Merge2Compare。

**EN** In this part, we define the construction process for Merge2Compare includes three steps: 1) pair/group matching; 2) top-similarity pair removal; and 3) LLM merging. An examplar illustration of the process is shown in Fig. 4.

**ZH** 本节定义 Merge2Compare 的构建过程，包含三个步骤：1）配对/分组匹配；2）高相似度配对剔除；3）LLM 合并。该过程的示例说明见图 4。

<!-- [原子块 · img]  -->

**EN** Figure 4: The pipeline of constructing Merge2Compare: images are first matched into groups (a), and then filtered via top-similarity removal (b). After filtering, the single image quality descriptions are merged (c) into comparisons by the LLM [16].

**ZH** 图 4：Merge2Compare 的构建流程：图像先被匹配为组（a），随后通过高相似度剔除进行过滤（b）。过滤之后，单图像质量描述由 LLM [16] 合并（c）为比较文本。

**EN** Step 1: Pair/Group Matching (Fig. 4(a)).

**ZH** 步骤 1：配对/分组匹配（图 4(a)）。

**EN** To best utilize information from existing single image quality descriptions, following the empirical rule to sample ⟦SLOT_2⟧ pairwise combinations to effectively rank among all individual items in a set [37, 45], we randomly sample 81K image pairs from all 19K images in the Q-Pathway. Despite pairs, we further sample 27K groups with three images and 18K groups with four images to cover the scenarios of more images.

**ZH** 为最充分地利用已有单图像质量描述中的信息，我们遵循经验规则，采样 ⟦SLOT_2⟧ 个成对组合以在一个集合内对各个样本有效排序 [37, 45]，从 Q-Pathway 的全部 19K 张图像中随机采样 81K 个图像对。除二元组外，我们还采样 27K 个三图像组与 18K 个四图像组，以覆盖更多图像的场景。

**EN** Step 2: Top-Similarity Pair Removal (Fig. 4(b)).

**ZH** 步骤 2：高相似度配对剔除（图 4(b)）。

**EN** The effectiveness of the merge comes from the differences among descriptions, e.g. between The quality is acceptable for <img⟦SLOT_3⟧> and The quality is poor for <img⟦SLOT_4⟧>. However, if descriptions in a pair/group contains almost the same information (e.g. both images with The clarity is good, but lighting is dark), the merged comparisons will lack enough information or even with false predictions. Henceforth, we use E5-Mistral [44] text embedding model to compute similarities among descriptions, and remove if any high-similarity description pairs exist in the group. After removal, 70K image pairs (86% of initial samples), 20K groups of three (74% of initial) and 10K groups of four (55% of initial) are preserved and fed into the LLM for merging.

**ZH** 合并之所以有效，源于描述之间的差异，例如 <img⟦SLOT_3⟧> 的「质量尚可」与 <img⟦SLOT_4⟧> 的「质量较差」之间。然而，若一个配对或分组内的描述包含几乎相同的信息（例如两张图像都是「清晰度不错，但光线偏暗」），合并出的比较就会信息不足，甚至包含错误判断。因此，我们用 E5-Mistral [44] 文本嵌入模型计算描述之间的相似度，并在组内存在高相似度描述对时予以剔除。剔除之后，保留 70K 个图像对（占初始样本的 86%）、20K 个三图像组（占初始的 74%）与 10K 个四图像组（占初始的 55%），送入 LLM 进行合并。

**EN** Step 3: LLM Merging (Fig. 4(c)).

**ZH** 步骤 3：LLM 合并（图 4(c)）。

**EN** The key step for the Merge2Compare is to prompt LLMs to convert the single image evaluations to comparative texts. Specifically, following many existing practices [26, 68, 58], we put the descriptions as alternates of images in the context. Denote the description for image <img⟦SLOT_5⟧> as <desc⟦SLOT_6⟧>, the user query for LLM merging is formulated as follows: (Pairs) The first image: <desc⟦SLOT_7⟧> The second image: <desc⟦SLOT_8⟧> Which image has better quality, and why? (Groups of Three/Four) ⟦SLOT_9⟧The ⟦SLOT_10⟧ image: <desc⟦SLOT_11⟧> ⟦SLOT_12⟧ Please rank the quality of the images and justify your rankings. where ⟦SLOT_13⟧ represents the ordinal form of ⟦SLOT_14⟧, e.g. ⟦SLOT_15⟧ is first, ⟦SLOT_16⟧ is second.

**ZH** Merge2Compare 的关键步骤是提示 LLM 把单图像评价转换为比较性文本。具体地，沿用许多已有做法 [26, 68, 58]，我们把描述作为图像的替身放入上下文。记图像 <img⟦SLOT_5⟧> 的描述为 <desc⟦SLOT_6⟧>，则用于 LLM 合并的用户查询形式如下：（成对）The first image: <desc⟦SLOT_7⟧> The second image: <desc⟦SLOT_8⟧> Which image has better quality, and why?（三/四图像组）⟦SLOT_9⟧The ⟦SLOT_10⟧ image: <desc⟦SLOT_11⟧> ⟦SLOT_12⟧ Please rank the quality of the images and justify your rankings. 其中 ⟦SLOT_13⟧ 表示 ⟦SLOT_14⟧ 的序数形式，例如 ⟦SLOT_15⟧ 为 first，⟦SLOT_16⟧ 为 second。

**EN** The merged comparisons are overall comparisons with reasonings (Fig. 4 right). To validate their reliability, we conducted a human examination on 250 random samples from Merge2Compare mixed with merged comparisons from 250 random removed groups. The correctness rate in Merge2Compare is 96%, while it is only 72% in the removed groups, demonstrating the effects of the top-similarity removal process in ensuring the quality of training data.

**ZH** 合并得到的比较是带有推理的整体比较（图 4 右）。为验证其可靠性，我们从 Merge2Compare 中随机抽取 250 个样本，并与 250 个被剔除组所生成的合并比较混合，进行人工检验。Merge2Compare 中的正确率为 96%，而被剔除组中仅为 72%，说明高相似度剔除过程对保证训练数据质量确有作用。

<!-- [原子块 · img]  -->

**EN** Figure 5: The pipeline of constructing Teach2Compare: 9K diverse images are collected and matched into 30K groups (a). The groups are then fed to GPT-4V to obtain general quality comparisons (b) and question-answering (c) related to quality comparisons.

**ZH** 图 5：Teach2Compare 的构建流程：采集 9K 张多样图像并匹配为 30K 个组（a）。随后把这些组送入 GPT-4V，获得通用质量比较（b）以及与质量比较相关的问答（c）。

**EN** 3.2 Teach2Compare.

**ZH** 3.2 Teach2Compare。

**EN** Given existing evaluations [69, 67] suggesting that GPT-4V is decent at comparing visual quality (Tab. 2/3/4), we propose to collect GPT-4V responses as pseudo labels for quality comparison. As shown in Fig. 5, we collect diverse unlabeled images and feed them to GPT-4V with different prompts to obtain Teach2Compare-general (overall quality comparison) and Teach2Compare-Q&A (question-answer pairs related to quality comparison). Details as follows.

**ZH** 鉴于已有评测 [69, 67] 表明 GPT-4V 在比较视觉质量上表现不俗（表 2/3/4），我们提出采集 GPT-4V 的回答作为质量比较的伪标签。如图 5 所示，我们采集多样的无标注图像，用不同的提示词送入 GPT-4V，得到 Teach2Compare-general（整体质量比较）与 Teach2Compare-Q&A（与质量比较相关的问答对）。细节如下。

**EN** Collection of Images (Fig. 5(a)).

**ZH** 图像采集（图 5(a)）。

**EN** For Teach2Compare, we collect 9K images from various sources to cover different quality concerns and visual appearances: 1) 5.4K in-the-wild images from YFCC-100M [41] database; 2) 1.8K images artificially-distorted images from COCO [3] (with 15 types of distortions via ImageCorruptions [32]) and KADIS-700K [24] (25 types of distortions); 3) 1.8K AI-generated images from ImageRewardDB [53]. These 9K diverse unlabeled images are further grouped into 18K pairs, 6K groups of three, and 6K groups of four, for GPT-4V to provide pseudo labels under two formats, as follows.

**ZH** 为构建 Teach2Compare，我们从多个来源采集 9K 张图像，以覆盖不同的质量关注点与视觉外观：1）来自 YFCC-100M [41] 数据库的 5.4K 张真实场景图像；2）来自 COCO [3]（经 ImageCorruptions [32] 施加 15 类失真）与 KADIS-700K [24]（25 类失真）的 1.8K 张人工失真图像；3）来自 ImageRewardDB [53] 的 1.8K 张 AI 生成图像。这 9K 张多样的无标注图像进一步被编为 18K 个二元组、6K 个三元组与 6K 个四元组，供 GPT-4V 以两种格式提供伪标签，具体如下。

**EN** Teach2Compare-general (Fig. 5(b)).

**ZH** Teach2Compare-general（图 5(b)）。

**EN** Similar to Merge2Compare, the general subset also consists of overall comparison with reasonings. Specifically, we substitute the <desc⟦SLOT_17⟧> in the Merge2Compare prompt template to respective real images <img⟦SLOT_18⟧> to feed to GPT-4V. After collection, we also conduct a similar 250-sample spot check on the output pseudo labels, which reports around 94% correctness. Though slightly less accurate than Merge2Compare (96%), examiners also report that GPT-4V labels contain more content information which has been observed to enhance quality understandings of models [47, 19, 20]. The two subsets are expected to complement each other for better learning outcomes.

**ZH** 与 Merge2Compare 类似，通用子集同样由带推理的整体比较构成。具体地，我们把 Merge2Compare 提示模板中的 <desc⟦SLOT_17⟧> 替换为相应的真实图像 <img⟦SLOT_18⟧>，再送入 GPT-4V。采集完成后，我们同样对输出的伪标签做 250 个样本的抽查，报告的正确率约为 94%。虽然比 Merge2Compare（96%）略低，检验者也报告说 GPT-4V 的标签包含更多内容信息，而这一点已被观察到能增强模型对质量的理解 [47, 19, 20]。两个子集有望彼此互补，带来更好的学习效果。

**EN** Teach2Compare-Q&A (Fig. 5(c)).

**ZH** Teach2Compare-Q&A（图 5(c)）。

**EN** Despite general comparisons, for GPT-4V, we also collect a specific subset to improve LMM ability on responding to open-range questions. To achieve this, we first list reference aspects (clarity, lighting, color, etc) and then ask GPT-4V to generate questions (and respective correct answers, and false answers for the questions) on comparing these aspects among the images. After removing failed generations, we obtain 230K question-answers from 30K image groups. These question-answers are converted to both direct question-answering and multi-choice questions (as A-OKVQA[38]) for training.

**ZH** 除通用比较之外，我们还为 GPT-4V 采集了一个专门子集，以提升 LMM 回答开放式问题的能力。为此，我们先列出参考方面（清晰度、光照、色彩等），再让 GPT-4V 生成关于在这些方面上比较图像的问题（以及相应的正确答案与错误答案）。剔除生成失败的样本后，我们从 30K 个图像组中获得 230K 条问答。这些问答被转换为直接问答与多选题（参照 A-OKVQA [38]）两种形式用于训练。

<!-- [原子块 · img]  -->

**EN** Figure 6: The structure of Co-Instruct. (a) Images are encoded by visual embedding layers and then passsed through an abstractor module to reduce token numbers, and then (c) fused with text embeddings into under the image-text interleaved format.

**ZH** 图 6：Co-Instruct 的结构。(a) 图像先由视觉嵌入层编码，再经过一个抽象器模块压缩词元数量，随后 (c) 以图文交错格式与文本嵌入融合。

**EN** 3.3 Rationale of Combinations.

**ZH** 3.3 组合的合理性。

**EN** As discussed in principle 3, our motivation is to collect subsets that can complement each other. This complementarity is reflected in the following two aspects. Firstly, in terms of general comparisons, Merge2Compare has higher accuracy but lacks fine-grained comparison (excluded by Top-similarity Pair Removal), while Teach2Compare-general, although slightly less accurate, offers more diverse scenarios and includes content information as background. Joint training of both contributes to a more comprehensive quality comparison by our model. Additionally, Teach2Compare includes a unique Q&A subset, which significantly enhances the model’s ability to answer open-range questions.

**ZH** 正如原则 3 所述，我们的动机是采集能够彼此互补的子集。这种互补性体现在两个方面。其一，在通用比较上，Merge2Compare 准确率更高，但缺少细粒度比较（已被高相似度配对剔除所排除）；而 Teach2Compare-general 虽略欠准确，却提供更多样的场景，并包含内容信息作为背景。两者联合训练使我们的模型获得更全面的质量比较能力。此外，Teach2Compare 还包含独有的 Q&A 子集，显著增强了模型回答开放式问题的能力。

**EN** 4 The Co-Instruct Model

**ZH** 4 Co-Instruct 模型

**EN** In this section, we discuss the proposed model, Co-Instruct. Specifically, we have made two non-trivial adaptations for the multi-image comparative setting:

**ZH** 本节讨论所提出的模型 Co-Instruct。具体地，我们为多图像比较设定做了两处非平凡的改造：

**EN** Visual Token Reduction (Fig. 6 (a)).

**ZH** 视觉词元压缩（图 6(a)）。

**EN** Most state-of-the-art LMMs [25, 39, 5] have adopted the simple projector that keeps a large number of tokens (e.g. 1,025). This structure is not friendly to multi-image scenarios: passing only two images will exceed the max length of LLaVA [26] (2,048), and four images will exceed the context window of LLaMA-2 [42] (4,096). Thus, we adopt another widely-used abstractor [4, 55, 56] structure to reduce token numbers before feeding the visual embeddings to LLM, so as to easily adapt to multi-image scenarios.

**ZH** 多数当前最优的 LMM [25, 39, 5] 采用保留大量词元（如 1,025 个）的简单投影器。这种结构对多图像场景并不友好：仅输入两张图像就会超出 LLaVA [26] 的最大长度（2,048），输入四张则会超出 LLaMA-2 [42] 的上下文窗口（4,096）。因此，我们采用另一种被广泛使用的抽象器结构 [4, 55, 56]，在把视觉嵌入送入 LLM 之前先压缩词元数量，以便轻松适配多图像场景。

**EN** Image-text Interleaved Format (Fig. 6 (c)).

**ZH** 图文交错格式（图 6(c)）。

**EN** Typical single-image instruction tuning usually does not care about “position of images”. Most approaches [68, 25, 4] directly pile all images before texts (<img⟦SLOT_19⟧>(<img⟦SLOT_20⟧>⟦SLOT_21⟧)<text>). Under this piling, multiple images are not separates and LMMs might confuse the information from different images and fail to compare well (see baseline result in Fig. 8). To solve this, we propose an image-text interleaved format for multi-image training, that each image is started with explicit text to identify its nominal:

**ZH** 典型的单图像指令微调通常不关心「图像的位置」。多数方法 [68, 25, 4] 直接把所有图像堆叠在文本之前（<img⟦SLOT_19⟧>(<img⟦SLOT_20⟧>⟦SLOT_21⟧)<text>）。在这种堆叠下，多张图像彼此不加分隔，LMM 可能混淆来自不同图像的信息，从而无法很好地比较（见图 8 中的基线结果）。为解决这一问题，我们提出用于多图像训练的图文交错格式：每张图像前都带有显式文本以标明其序号：

**EN** User: The first image: <img⟦SLOT_22⟧> The second image: <img⟦SLOT_23⟧> (⟦SLOT_24⟧) <query> Assistant: <response>

**ZH** User: The first image: <img⟦SLOT_22⟧> The second image: <img⟦SLOT_23⟧> (⟦SLOT_24⟧) <query> Assistant: <response>

**EN** In our experiments, we demonstrated that this interleaved format significantly enhances the performance of Co-Instruct (Tab. 8), notably better than using learnable special tokens (<img_st> and <img_end>) to divide images.

**ZH** 在实验中我们证明，这种交错格式显著提升了 Co-Instruct 的性能（表 8），明显优于用可学习的特殊词元（<img_st> 与 <img_end>）来分隔图像。

<!-- [原子块 · img]  -->

**EN** Figure 7: Dataset Card of MICBench, made up of (a) Which questions (60%), (b) Yes-or-No questions (22%), and (c) Other types of questions (18%) on three/four images.

**ZH** 图 7：MICBench 的数据集卡片，由针对三张/四张图像的 (a) Which 类问题（60%）、(b) 是/否类问题（22%）与 (c) 其他类型问题（18%）构成。

**EN** 5 The MICBench

**ZH** 5 MICBench

**EN** In this section, we discuss the proposed MICBench to cover the open-ended evaluation settings on groups of three or four images, as a complementary of existing evaluation settings (Sec. 6.3). It contains 2,000 groups of open-range questions equipped with multiple candidates, with details elaborated as follows:

**ZH** 本节讨论所提出的 MICBench，用于覆盖三张或四张图像上的开放式评测设定，作为对已有评测设定（第 6.3 节）的补充。它包含 2,000 组配备多个候选答案的开放式问题，细节如下：

**EN** Sourcing Diverse Image Groups.

**ZH** 采集多样的图像组。

**EN** To improve the diversity of the benchmark, in the MICBench, we sample image groups from two sources: (1) 400 groups of three and 400 groups of four from the images in LLVisionQA [49], which are originally sourced from 9 datasets [18, 66, 6, 12, 59, 7, 24, 15, 3]; (2) 600 groups of three and 600 groups of four on 1,000 random images sampled from unlabeled databases [41, 24, 3, 53] (zero overlap with training-set images). With in-total 2,000 groups, the MICBench contains a wide variety of quality issues and low-level appearances, providing a non-biased evaluation on quality comparison.

**ZH** 为提升基准的多样性，MICBench 中的图像组来自两个来源：（1）从 LLVisionQA [49] 的图像中取 400 个三图像组与 400 个四图像组，这些图像原始来自 9 个数据集 [18, 66, 6, 12, 59, 7, 24, 15, 3]；（2）从无标注数据库 [41, 24, 3, 53] 中随机采样 1,000 张图像，构成 600 个三图像组与 600 个四图像组（与训练集图像零重叠）。MICBench 合计 2,000 个组，涵盖了丰富多样的质量问题与底层外观，可对质量比较开展无偏评测。

**EN** Evaluation Form: Multi-choice Questions (MCQs).

**ZH** 评测形式：多选题（MCQ）。

**EN** As the most popular evaluation form for LLM/LMM benchmarks [11, 60, 29, 49], multi-choice question (MCQ) is adopted as the evaluation form of MICBench. As is shown in Fig. 7, each image group is associated with a expert-crafted question that compare quality or related attributes among the images. Despite common question types (Yes-or-No/What/How, etc), the MICBench also introduces a special type of question, the Which questions (Fig. 7(a)), to cover this common type of human query on comparison. In total 10 human experts participate in annotating the MICBench, and the answer of each MCQ is cross-examined by another expert. Similar as existing benchmarks [29, 49], MICBench is further divided into a dev set (1,004) for method development (answers will be public), and a test set (996) to evaluate performance of LMMs (answers will be hidden from public).

**ZH** 作为 LLM/LMM 基准中最流行的评测形式 [11, 60, 29, 49]，多选题（MCQ）被采纳为 MICBench 的评测形式。如图 7 所示，每个图像组都配有一道专家编写的问题，用于比较这些图像的质量或相关属性。除常见的问题类型（是/否、What、How 等）之外，MICBench 还引入了一类特殊问题——Which 类问题（图 7(a)），以覆盖这一常见的人类比较提问方式。共有 10 位人类专家参与 MICBench 的标注，每道多选题的答案都由另一位专家复核。与已有基准 [29, 49] 类似，MICBench 进一步划分为开发集（1,004）用于方法开发（答案将公开），以及测试集（996）用于评测 LMM 性能（答案不对外公开）。

**EN** 6 Evaluation

**ZH** 6 评测

**EN** 6.1 Implementation Details

**ZH** 6.1 实现细节

**EN** The Co-Instruct is fine-tuned after the released checkpoint of mPLUG-Owl2 [56], with LLaMA-2 [42] as LLM and CLIP-ViT-L14 [36] as visual embedding module. Images are padded to square and then resized to ⟦SLOT_25⟧ before fed into the model. The learning rate is set as ⟦SLOT_26⟧-⟦SLOT_27⟧, with two epochs under batch size ⟦SLOT_28⟧. The final checkpoint is used for evaluation. To avoid over-fitting, only dev subsets of evaluation datasets are used to choose best training hyper-parameters, where the final reported results are from non-overlapped test subsets. All parameters are updated during training, costing in total 25 hours on 8*NVIDIA A100 GPUs.

**ZH** Co-Instruct 在 mPLUG-Owl2 [56] 已发布的检查点之上微调，以 LLaMA-2 [42] 作为 LLM，以 CLIP-ViT-L14 [36] 作为视觉嵌入模块。图像被填充为正方形，并在输入模型前缩放至 ⟦SLOT_25⟧。学习率设为 ⟦SLOT_26⟧-⟦SLOT_27⟧，批大小为 ⟦SLOT_28⟧，训练两个轮次。评测使用最终检查点。为避免过拟合，只用评测数据集的开发子集来选择最佳训练超参数，最终报告的结果来自不重叠的测试子集。训练期间更新全部参数，在 8 张 NVIDIA A100 GPU 上共耗时 25 小时。

**EN** 6.2 Baseline Models

**ZH** 6.2 基线模型

**EN** We choose five open-source recent state-of-the-art LMMs that supports multi-image inputs to compare with: LLaVA-v1.5-13B [25], InternLM-XComposer2 [5], BakLLaVA [39], EMU2-Chat [40], mPLUG-Owl2 [56] (baseline of Co-Instruct). Additionally, we also compare with three well-recognized proprietary close-source models: Qwen-VL-Max, Gemini-Pro, and GPT-4V (teacher of Co-Instruct).

**ZH** 我们选取五个支持多图像输入的近期开源最优 LMM 进行比较：LLaVA-v1.5-13B [25]、InternLM-XComposer2 [5]、BakLLaVA [39]、EMU2-Chat [40]、mPLUG-Owl2 [56]（Co-Instruct 的基线）。此外，我们还与三个广受认可的闭源专有模型比较：Qwen-VL-Max、Gemini-Pro 与 GPT-4V（Co-Instruct 的教师）。

**EN** 6.3 Results on Existing Evaluation Settings

**ZH** 6.3 在已有评测设定上的结果

**EN** Despite the MICBench (Sec. 5), we also evaluate the proposed Co-Instruct against baseline models on several existing visual quality evaluation/comparison benchmarks for LMMs. The evaluation settings and results are as follows.

**ZH** 除 MICBench（第 5 节）外，我们还在若干已有的面向 LMM 的视觉质量评价/比较基准上，把 Co-Instruct 与基线模型进行比较。评测设定与结果如下。

**EN** Table 2: Results on Q-Bench⟦SLOT_29⟧-A1. Co-Instruct is remarkably 51% better than the variant without comparative data, and the only LMM that surpasses human capability.

**ZH** 表 2：在 Q-Bench⟦SLOT_29⟧-A1 上的结果。Co-Instruct 比不含比较数据的变体高出 51%，并且是唯一超越人类能力的 LMM。

<!-- [原子块 · table] Sub-categories Question Types Low-level Concerns Pairwise Settings Overall ↑ \uparrow Model Yes-or-No ↑ \uparrow What ↑ \uparrow How ↑ \uparrow Distortion ↑ \uparrow Other ↑ \uparrow Compare ↑ \uparro -->

**EN** Q-Bench⟦SLOT_30⟧-A1[67] is a benchmark for visual quality comparison with 1,999 expert-crafted open-range quality-related MCQs on image pairs. In Tab. 2, we compare Co-Instruct against existing open-source and proprietary models on this benchmark. Co-Instruct shows far superior accuracy than open-source LMMs: it is 64% better than its baseline (mPLUG-Owl2), 51% better than the variant without our multi-image subsets (Merge2Compare and Teach2Compare), and also 23% better than the best of them. It also outperforms Qwen-VL-Max and Gemini-Pro by a large margin (21%/33%). Additionally, though its all MCQ training data are from GPT-4V, the student (Co-Instruct) still outperforms its teacher on this MCQ evaluation set by notable 2.7%, suggesting the effectiveness of the collaborative teaching strategy. Our model is also the only LMM that surpasses the accuracy of a non-expert human (esp. on Compare subset) in this benchmark, strongly supporting the meaningful vision of using models to relieve human labors on real-world visual quality comparisons in the future.

**ZH** Q-Bench⟦SLOT_30⟧-A1 [67] 是一个面向视觉质量比较的基准，包含 1,999 道专家编写的、与质量相关的开放式多选题，针对图像对。在表 2 中，我们把 Co-Instruct 与现有开源及专有模型在该基准上比较。Co-Instruct 的准确率远超开源 LMM：比其基线（mPLUG-Owl2）高 64%，比不含我们多图像子集（Merge2Compare 与 Teach2Compare）的变体高 51%，也比其中最好的模型高 23%。它还以大幅优势超过 Qwen-VL-Max 与 Gemini-Pro（21%/33%）。此外，尽管其全部多选题训练数据都来自 GPT-4V，学生（Co-Instruct）在该多选题评测集上仍以显著的 2.7% 超过其教师，说明协同教学策略的有效性。我们的模型也是该基准中唯一准确率超过非专家人类（尤其在 Compare 子集上）的 LMM，有力地支持了用模型减轻真实世界视觉质量比较中人力负担这一有意义的前景。

**EN** Table 3: Results on Q-Bench⟦SLOT_31⟧-A2. ⟦SLOT_32⟧ denotes frequency for score ⟦SLOT_33⟧ (score in ⟦SLOT_34⟧). While slightly inferior to GPT-4V, Co-Instruct has significantly improved over both the variant without comparative data (+31%), especially for Precision metric (+59%).

**ZH** 表 3：在 Q-Bench⟦SLOT_31⟧-A2 上的结果。⟦SLOT_32⟧ 表示分数 ⟦SLOT_33⟧ 的频数（分数位于 ⟦SLOT_34⟧ 中）。Co-Instruct 虽略逊于 GPT-4V，但相比不含比较数据的变体显著提升（+31%），尤其在 Precision 指标上（+59%）。

<!-- [原子块 · table] Dimensions Completeness Precision Relevance Sum. ↑ \uparrow Model P 0 P_{0} P 1 P_{1} P 2 P_{2} score ↑ \uparrow P 0 P_{0} P 1 P_{1} P 2 P_{2} score ↑ \uparrow P 0 P_{0} P 1 P_{1} P 2 P_{2} score ↑ \u -->

<!-- [原子块 · img]  -->

**EN** Figure 8: Qualitative Visualization on Q-Bench⟦SLOT_35⟧-A2. GPT-4V gives longest outputs and achieves high precision score even if it includes incorrect information.

**ZH** 图 8：在 Q-Bench⟦SLOT_35⟧-A2 上的定性可视化。GPT-4V 给出的输出最长，即便其中包含错误信息，仍取得了较高的 precision 分数。

**EN** Q-Bench⟦SLOT_36⟧-A2 is a benchmark setting for general and detailed visual quality comparison with detailed reasonings on image pairs. Consisting of 499 image pairs, it employs GPT to evaluate LMM responses against the golden expert-labeled comparisons on Completeness, Precision, and Relevance. As listed in Tab. 3, the Co-Instruct can remarkably improve the Completeness (+57%) and Precision (+59%) of the comparative outputs than the w/o comparative data version, but still falls a little bit behind GPT-4V on the quantitative metrics. This might be because outputs from GPT-4V are more than twice as long as Co-Instruct outputs, while GPT evaluation used here is observed [22] to be in favor of longer text outputs. To further analyze this potential bias, we qualitatively visualize the result of different LMMs in Fig. 8. As shown in the figure, the baseline open-source LMM even confuses the information from the two images, and Gemini-Pro makes rather poor detailed reasonings. For GPT-4V, it generates the longest outputs among all LMMs, which might be the reason that it gets a relatively high precision score even its outputs are not totally correct. In short, the capability of Co-Instruct in reasoning-related comparisons can match that of GPT-4V, while significantly surpassing other existing LMMs.

**ZH** Q-Bench⟦SLOT_36⟧-A2 是一个针对图像对、要求给出通用且详细的视觉质量比较与详细推理的评测设定。它包含 499 个图像对，用 GPT 对照专家标注的黄金比较，从 Completeness、Precision 与 Relevance 三个维度评估 LMM 的回答。如表 3 所列，相比不含比较数据的版本，Co-Instruct 显著提升了比较输出的 Completeness（+57%）与 Precision（+59%），但在定量指标上仍略落后于 GPT-4V。这可能是因为 GPT-4V 的输出长度是 Co-Instruct 的两倍以上，而这里所用的 GPT 评测已被观察到 [22] 偏向更长的文本输出。为进一步分析这一潜在偏差，我们在图 8 中定性展示了不同 LMM 的结果。如图所示，基线开源 LMM 甚至混淆了两张图像的信息，而 Gemini-Pro 的详细推理相当糟糕。对 GPT-4V 而言，它在所有 LMM 中生成最长的输出，这可能是即便其输出并非完全正确、仍获得相对较高 precision 分数的原因。简言之，Co-Instruct 在与推理相关的比较上能力可与 GPT-4V 匹敌，同时显著超过其他现有 LMM。

**EN** Table 4: Results on 2AFC-LMM. ⟦SLOT_37⟧ denotes binary judgment consistency while swapping first image and second image; ⟦SLOT_38⟧ denotes Pearson’s linear correlation.

**ZH** 表 4：在 2AFC-LMM 上的结果。⟦SLOT_37⟧ 表示交换第一张与第二张图像后的二值判断一致性，⟦SLOT_38⟧ 表示 Pearson 线性相关系数。

<!-- [原子块 · table] Dataset CSIQ MM21 KADID-10k LIVEC KonIQ-10k SPAQ weighted avg. Model κ \kappa ρ \rho κ \kappa ρ \rho κ \kappa ρ \rho κ \kappa ρ \rho κ \kappa ρ \rho κ \kappa ρ \rho κ \kappa ρ \rho ( Aug/2023 ) IDEFIC -->

**EN** 2AFC-LMM[69] is a benchmark setting for general quality comparison on image pairs. It prompts LMMs to make a two-alternative forced choice (2AFC) on a pair of images. The maximum a posterior estimation is utilized to aggregate comparative preferences to single-image quality scores [43]. Then, it computes Peason’s linear correlation (⟦SLOT_39⟧) between regressed scores and ground truth MOS. As shown in Tab. 4, Co-Instruct outperforms all existing models in 2AFC-LMM, including GPT-4V. Co-Instruct also shows very high consistency ⟦SLOT_40⟧ while swapping two images. Among all datasets, the proposed model is only inferior on the MM21 [23]. Nonetheless, we observe that the Co-Instruct has higher direct comparison accuracy than GPT-4V (Co-Instruct: 55.2%, GPT-4V: 54.4%, see supplementary for full results) on it, yet the dataset contains a large proportion of extremely similar pairs, for which Co-Instruct responds a forced choice but GPT-4V will answer “two images have similar quality” (tie), which impacts the aggregated single-image quality scores. We hope this observation can inspire further research to design better evaluation settings for fine-grained comparisons.

**ZH** 2AFC-LMM [69] 是一个针对图像对通用质量比较的评测设定，它提示 LMM 在一对图像上做二选一强制选择（2AFC），并用最大后验估计把比较偏好聚合为单图像质量分数 [43]，随后计算回归分数与真值 MOS 之间的 Pearson 线性相关系数（⟦SLOT_39⟧）。如表 4 所示，Co-Instruct 在 2AFC-LMM 上优于所有现有模型，包括 GPT-4V；在交换两张图像时也表现出很高的一致性 ⟦SLOT_40⟧。在所有数据集中，所提模型仅在 MM21 [23] 上处于劣势。不过我们观察到，Co-Instruct 在该数据集上的直接比较准确率高于 GPT-4V（Co-Instruct：55.2%，GPT-4V：54.4%，完整结果见补充材料）；但该数据集包含大量极为相似的图像对，Co-Instruct 会给出强制选择，而 GPT-4V 会回答「两张图像质量相近」（平局），这影响了聚合出的单图像质量分数。我们希望这一观察能启发后续研究，为细粒度比较设计更好的评测设定。

**EN** Table 5: Results on Q-Bench⟦SLOT_41⟧-A1, proving that the comparative data (Sec. 3) can also effectively boost the capability of LMMs on single image quality evaluation.

**ZH** 表 5：在 Q-Bench⟦SLOT_41⟧-A1 上的结果，证明比较数据（第 3 节）同样能有效提升 LMM 在单图像质量评价上的能力。

<!-- [原子块 · table] Sub-categories Question Types Quadrants of Low-level Concerns Overall ↑ \uparrow Model Yes-or-No ↑ \uparrow What ↑ \uparrow How ↑ \uparrow Distortion ↑ \uparrow Other ↑ \uparrow In-context In-context  -->

**EN** Q-Bench⟦SLOT_42⟧-A1. Despite the comparative benchmarks above, we also evaluate Co-Instruct on single image MCQs from Q-Bench⟦SLOT_43⟧-A1 to verify the influences of comparative tuning on single-image quality perception. As shown in Tab. 5, Co-Instruct shows 5% improvement over the variant trained with single images only, leading GPT-4V by 4%, and marks the only LLM that surpasses non-expert human. These results have demonstrated the contribution of comparative training on general quality-related understanding of LMMs, and suggested that single-image quality evaluation does not conflict with multi-image quality comparison for LMMs and can be improved together under a unified model.

**ZH** Q-Bench⟦SLOT_42⟧-A1。除上述比较类基准外，我们还在 Q-Bench⟦SLOT_43⟧-A1 的单图像多选题上评测 Co-Instruct，以验证比较式微调对单图像质量感知的影响。如表 5 所示，Co-Instruct 比只用单图像训练的变体提升 5%，领先 GPT-4V 4%，并且是唯一超过非专家人类的 LMM。这些结果证明了比较式训练对 LMM 通用质量相关理解的贡献，也说明对 LMM 而言，单图像质量评价与多图像质量比较并不冲突，可以在统一模型下共同提升。

**EN** 6.4 Results on MICBench

**ZH** 6.4 在 MICBench 上的结果

**EN** Table 6: Results on MICBench. Co-Instruct is 60% better than the variant without comparative data, and also notably better than GPT-4V (+5.7%) and human (+6.4%).

**ZH** 表 6：在 MICBench 上的结果。Co-Instruct 比不含比较数据的变体高出 60%，也明显高于 GPT-4V（+5.7%）与人类（+6.4%）。

<!-- [原子块 · table] Sub-categories Question Types Number of Images Overall ↑ \uparrow Model Yes-or-No ↑ \uparrow Which ↑ \uparrow Others ↑ \uparrow Three ↑ \uparrow Four ↑ \uparrow #questions 220 594 182 503 493 996 rand -->

**EN** As is shown in Tab. 6, Co-Instruct provides very competitive accuracy on open-question quality comparison among three/four images, 5.7% better than GPT-4V (best existing) and 6.4% more accurate than non-expert human; open-source LMMs even struggle to obtain 50% accuracy on this setting. It is also noteworthy that LLaVA series and XComposer2-VL’s original context lengths are not enough for four images as they have not reduced visual token numbers, so we have to extend their context windows to evaluate them for MICBench. Consequentially, all these models have experienced notably worse accuracy on groups of four (on extended context length) than groups of three (within original context length), as noted in * in Tab. 6. This degradation highlights the importance to reduce visual tokens (Sec. 4) to adapt to multi-image scenarios.

**ZH** 如表 6 所示，Co-Instruct 在三张/四张图像的开放式质量比较上给出了极具竞争力的准确率，比 GPT-4V（现有最佳）高 5.7%，比非专家人类高 6.4%；开源 LMM 在这一设定下甚至难以达到 50% 的准确率。同样值得注意的是，LLaVA 系列与 XComposer2-VL 的原始上下文长度不足以容纳四张图像，因为它们没有压缩视觉词元数量，我们不得不扩展其上下文窗口才能在 MICBench 上评测。结果如表 6 中 * 所示，所有这些模型在四图像组（在扩展后的上下文长度下）的准确率都明显低于三图像组（在原始上下文长度内）。这一退化凸显了压缩视觉词元（第 4 节）对适配多图像场景的重要性。

**EN** 6.5 Ablation Studies

**ZH** 6.5 消融实验

**EN** Ablation on Training Data. As the proposed dataset is composed of three parts, we discuss the effects on different subsets of data on the six evaluation scenarios in Tab. 8. Through the results, we have arrived at several important conclusions: A) Even with all information from Q-Instruct-200K, the incorporation of Merge2Compare (variant (2)) still notably enhances the capability across various settings; B) Only involving the Teach2Compare (i.e. GPT-4V labels, variant (5)) cannot outperform its teacher GPT-4V; C) instead, the superiority towards GPT-4V on question-answering benchmarks is benefited from the co-instruction on hetero-sourced training subsets (variants (6) and (7)).

**ZH** 训练数据消融。由于所提数据集由三部分组成，我们在表 8 中讨论了不同数据子集对六个评测场景的影响。由结果可得出若干重要结论：A）即便已包含 Q-Instruct-200K 的全部信息，加入 Merge2Compare（变体 (2)）仍能显著提升各设定下的能力；B）仅使用 Teach2Compare（即 GPT-4V 标签，变体 (5)）无法超越其教师 GPT-4V；C）相反，在问答类基准上相对 GPT-4V 的优势，得益于在异源训练子集上的协同指令微调（变体 (6) 与 (7)）。

**EN** Table 7: Ablation Study on data. Abbreviation: Merge: Merge2Compare; Teach⟦SLOT_44⟧: Teach2Compare-general; Teach⟦SLOT_45⟧: Teach2Compare-Q&A; QIn: Q-Instruct-200K.

**ZH** 表 7：数据消融实验。缩写说明：Merge：Merge2Compare；Teach⟦SLOT_44⟧：Teach2Compare-general；Teach⟦SLOT_45⟧：Teach2Compare-Q&A；QIn：Q-Instruct-200K。

<!-- [原子块 · table] Training Subset Evaluation Scenario Variant No. QIn Merge Teach G {}^{\textit{G}} Teach QA {}^{\textit{QA}} Q-Bench PAIR {}^{\texttt{PAIR}} -A1 Q-Bench PAIR {}^{\texttt{PAIR}} -A2 Q-Bench SINGLE {}^{\ -->

**EN** Table 8: Ablation Study on the text-image interleaved format for the Co-Instruct.

**ZH** 表 8：Co-Instruct 在图文交错格式上的消融实验。

<!-- [原子块 · table] Format Q-Bench PAIR {}^{\texttt{PAIR}} -A1 Q-Bench PAIR {}^{\texttt{PAIR}} -A2 Q-Bench SINGLE {}^{\texttt{SINGLE}} -A1 2AFC-LMM MICBench <img 0 {}_{\texttt{0}} >(<img 1 {}_{\texttt{1}} > ...) ( baseli -->

<!-- [原子块 · img]  -->

**EN** Figure 9: Effects of Data Scaling for (a) detailed reasoning and (b) question answering.

**ZH** 图 9：数据规模对 (a) 详细推理与 (b) 问答的影响。

**EN** Besides the composition of three subsets, we also explore the effects of data scale: in Fig. 9(a), we confirm that more general comparison data contributes to an increase in detailed reasoning capabilities, and mixed data has a better effect than homogenous data at the same scale; in Fig. 9(b), we also validate that scaling up the Q&A subset helps to improve multiple MCQ metrics.

**ZH** 除三个子集的构成之外，我们还探索了数据规模的影响：在图 9(a) 中，我们确认更多通用比较数据有助于提升详细推理能力，且同等规模下混合数据优于同质数据；在图 9(b) 中，我们也验证了扩大 Q&A 子集规模有助于提升多项多选题指标。

**EN** Ablation on Interleaved Format. As shown in Tab. 8, the proposed text-image interleaved format has proved non-negligible advantages than the baseline, as well as other variants without explicitly noting image orders. The results suggest the rationale of the format on multi-image comparative settings.

**ZH** 交错格式消融。如表 8 所示，所提出的图文交错格式相比基线、以及其他未显式标明图像顺序的变体，具有不可忽略的优势。这些结果说明该格式在多图像比较设定上的合理性。

**EN** 7 Conclusion

**ZH** 7 结论

**EN** In this work, we investigate the open-ended visual quality comparison problem, with the aim of a model that provides answers and detailed reasonings on open-range questions that compares quality among multiple images. To achieve this, we collect the first instruction-tuning dataset to fine-tune large multi-modality models (LMMs) for comparison, the Co-Instruct-562K, with two subsets from human annotations on single images (merged by LLMs), and GPT-4V responses. With the dataset, we propose the Co-Instruct, which not only outperforms all existing LMMs (including its teacher, GPT-4V) on visual quality comparison, but also marks the first LMM with the capability to surpass human accuracy on related settings. We further construct the MICBench, the first benchmark that evaluates multi-image quality comparison for LMMs on three and four images. We expect our work to motivate future studies on visual quality comparison.

**ZH** 本文研究开放式视觉质量比较问题，目标是得到一个能对「比较多张图像质量」的开放式问题给出答案与详细推理的模型。为此，我们收集了首个用于微调大型多模态模型（LMM）进行比较的指令微调数据集 Co-Instruct-562K，其中包含两个子集：一个来自单图像上的人工标注（由 LLM 合并），另一个来自 GPT-4V 的回答。借助该数据集，我们提出 Co-Instruct：它不仅在视觉质量比较上优于所有现有 LMM（包括其教师 GPT-4V），也是首个在相关设定上准确率超过人类的 LMM。我们进一步构建了 MICBench——首个评测 LMM 在三张与四张图像上进行多图像质量比较的基准。我们期待本工作能激发未来关于视觉质量比较的研究。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] [1] Antol, S., Agrawal, A., Lu, J., Mitchell, M., Batra, D., Zitnick, C.L., Parikh, D.: VQA: Visual Question Answering. In: IEEE ICCV. pp. 2425–2433 (2015) -->

<!-- [原子块 · verbatim] [2] Chen, L., Li, J., Dong, X., Zhang, P., He, C., Wang, J., Zhao, F., Lin, D.: ShareGPT4V: Improving large multi-modal models with better captions. CoRR abs/2311.12793 (2023) -->

<!-- [原子块 · verbatim] [3] Chen, X., Fang, H., Lin, T.Y., Vedantam, R., Gupta, S., Dollár, P., Zitnick, C.L.: Microsoft COCO captions: Data collection and evaluation server. CoRR abs/1504.00325 (2015) -->

<!-- [原子块 · verbatim] [4] Dai, W., Li, J., Li, D., Tiong, A.M.H., Zhao, J., Wang, W., Li, B., Fung, P., Hoi, S.: InstructBLIP: Towards general-purpose vision-language models with instruction tuning. CoRR abs/2305.06500 (20 -->

<!-- [原子块 · verbatim] [5] Dong, X., Zhang, P., Zang, Y., Cao, Y., Wang, B., Ouyang, L., Wei, X., Zhang, S., Duan, H., Cao, M., Zhang, W., Li, Y., Yan, H., Gao, Y., Zhang, X., Li, W., Li, J., Chen, K., He, C., Zhang, X., Qi -->

<!-- [原子块 · verbatim] [6] Fang, Y., Zhu, H., Zeng, Y., Ma, K., Wang, Z.: Perceptual quality assessment of smartphone photography. In: IEEE CVPR. pp. 3677–3686 (2020) -->

<!-- [原子块 · verbatim] [7] Ghadiyaram, D., Bovik, A.C.: Massive online crowdsourced study of subjective and objective picture quality. IEEE TIP 25 (1), 372–387 (2016) -->

<!-- [原子块 · verbatim] [8] Golestaneh, S.A., Dadsetan, S., Kitani, K.M.: No-reference image quality assessment via transformers, relative ranking, and self-consistency. In: IEEE WACV. pp. 3209–3218 (2022) -->

<!-- [原子块 · verbatim] [9] Google: Gemini Pro (2023), https://deepmind.google/technologies/gemini -->

<!-- [原子块 · verbatim] [10] Gu, J., Cai, H., Chen, H., Ye, X., Ren, J., Dong, C.: PIPAL: A large-scale image quality assessment dataset for perceptual image restoration. In: ECCV. pp. 633–651 (2020) -->

<!-- [原子块 · verbatim] [11] Hendrycks, D., Burns, C., Basart, S., Zou, A., Mazeika, M., Song, D., Steinhardt, J.: Measuring massive multitask language understanding. In: ICLR. pp. 1–10 (2021) -->

<!-- [原子块 · verbatim] [12] Hosu, V., Lin, H., Sziranyi, T., Saupe, D.: Koniq-10k: An ecologically valid database for deep learning of blind image quality assessment. IEEE TIP 29 , 4041–4056 (2020) -->

<!-- [原子块 · verbatim] [13] Hudson, D.A., Manning, C.D.: GQA: A new dataset for real-world visual reasoning and compositional question answering. In: IEEE CVPR. pp. 6700–6709 (2019) -->

<!-- [原子块 · verbatim] [14] ITU-R, B.T.: Methodology for the subjective assessment of the quality of television pictures. https://www.itu.int/rec/R-REC-BT.500 (2002) -->

<!-- [原子块 · verbatim] [15] Jayaraman, D., Mittal, A., Moorthy, A.K., Bovik, A.C.: Objective quality assessment of multiply distorted images. In: ASILOMAR. pp. 1693–1697 (2012) -->

<!-- [原子块 · verbatim] [16] Jiang, A.Q., Sablayrolles, A., Roux, A., Mensch, A., Savary, B., Bamford, C., Chaplot, D.S., de las Casas, D., Hanna, E.B., Bressand, F., Lengyel, G., Bour, G., Lample, G., Lavaud, L.R., Saulnier -->

<!-- [原子块 · verbatim] [17] LAION: LAION GPT-4V dataset. https://huggingface.co/datasets/laion/gpt4v-dataset (2023) -->

<!-- [原子块 · verbatim] [18] Li, C., Zhang, Z., Wu, H., Sun, W., Min, X., Liu, X., Zhai, G., Lin, W.: AGIQA-3K: An open database for ai-generated image quality assessment. CoRR 2306.04717 (2023) -->

<!-- [原子块 · verbatim] [19] Li, D., Jiang, T., Jiang, M.: Quality assessment of in-the-wild videos. In: ACM MM. pp. 2351–2359 (2019) -->

<!-- [原子块 · verbatim] [20] Li, D., Jiang, T., Lin, W., Jiang, M.: Which has better visual quality: The clear blue sky or a blurry animal? IEEE TMM 21 (5), 1221–1234 (2019) -->

<!-- [原子块 · verbatim] [21] Li, J., Mantiuk, R., Wang, J., Ling, S., Le Callet, P.: Hybrid-MST: A hybrid active sampling strategy for pairwise preference aggregation. In: NeurIPS. pp. 1–11 (2018) -->

<!-- [原子块 · verbatim] [22] Li, X., Zhang, T., Dubois, Y., Taori, R., Gulrajani, I., Guestrin, C., Liang, P., Hashimoto, T.B.: AlpacaEval: An automatic evaluator of instruction-following models. https://github.com/tatsu-lab -->

<!-- [原子块 · verbatim] [23] Li, Y., Wang, S., Zhang, X., Wang, S., Ma, S., Wang, Y.: Quality assessment of end-to-end learned image compression: The benchmark and objective measure. In: ACM MM. pp. 4297–4305 (2021) -->

<!-- [原子块 · verbatim] [24] Lin, H., Hosu, V., Saupe, D.: KADID-10k: A large-scale artificially distorted iqa database. In: QoMEX. pp. 1–3 (2019) -->

<!-- [原子块 · verbatim] [25] Liu, H., Li, C., Li, Y., Lee, Y.J.: Improved baselines with visual instruction tuning. CoRR abs/2310.03744 (2023) -->

<!-- [原子块 · verbatim] [26] Liu, H., Li, C., Wu, Q., Lee, Y.J.: Visual instruction tuning. CoRR abs/2304.08485 (2023) -->

<!-- [原子块 · verbatim] [27] Liu, X., Van De Weijer, J., Bagdanov, A.D.: RankIQA: Learning from rankings for no-reference image quality assessment. In: IEEE ICCV. pp. 1040–1049 (2017) -->

<!-- [原子块 · verbatim] [28] Liu, X., Van De Weijer, J., Bagdanov, A.D.: Exploiting unlabeled data in cnns by self-supervised learning to rank. IEEE TPAMI 41 (8), 1862–1878 (2019) -->

<!-- [原子块 · verbatim] [29] Liu, Y., Duan, H., Zhang, Y., Li, B., Zhang, S., Zhao, W., Yuan, Y., Wang, J., He, C., Liu, Z., Chen, K., Lin, D.: MMBench: Is your multi-modal model an all-around player? CoRR abs/2307.06281 (20 -->

<!-- [原子块 · verbatim] [30] Ma, K., Liu, W., Liu, T., Wang, Z., Tao, D.: dipIQ: Blind image quality assessment by learning-to-rank discriminable image pairs. IEEE TIP 26 (8), 3951–3964 (2017) -->

<!-- [原子块 · verbatim] [31] Mantiuk, R.K., Tomaszewska, A., Mantiuk, R.: Comparison of four subjective methods for image quality assessment. In: Computer Graphics Forum. vol. 31, pp. 2478–2491 (2012) -->

<!-- [原子块 · verbatim] [32] Michaelis, C., Mitzkus, B., Geirhos, R., Rusak, E., Bringmann, O., Ecker, A.S., Bethge, M., Brendel, W.: Benchmarking robustness in object detection: Autonomous driving when winter is coming. CoR -->

<!-- [原子块 · verbatim] [33] Mikhailiuk, A., Wilmot, C., Perez-Ortiz, M., Yue, D., Mantiuk, R.K.: Active sampling for pairwise comparisons via approximate message passing and information gain maximization. In: IEEE ICPR. pp. -->

<!-- [原子块 · verbatim] [34] OpenAI: Gpt-4 technical report (2023) -->

<!-- [原子块 · verbatim] [35] Prashnani, E., Cai, H., Mostofi, Y., Sen, P.: PieAPP: Perceptual image-error assessment through pairwise preference. In: IEEE CVPR. pp. 1808–1817 (2018) -->

<!-- [原子块 · verbatim] [36] Radford, A., Kim, J.W., Hallacy, C., Ramesh, A., Goh, G., Agarwal, S., Sastry, G., Askell, A., Mishkin, P., Clark, J., et al.: Learning transferable visual models from natural language supervisio -->

<!-- [原子块 · verbatim] [37] Rajkumar, A., Agarwal, S.: When can we rank well from comparisons of o (nlog (n)) non-actively chosen pairs? In: Conference on Learning Theory. pp. 1376–1401 (2016) -->

<!-- [原子块 · verbatim] [38] Schwenk, D., Khandelwal, A., Clark, C., Marino, K., Mottaghi, R.: A-OKVQA: A benchmark for visual question answering using world knowledge. In: ECCV. pp. 146–162 (2022) -->

<!-- [原子块 · verbatim] [39] SkunkworksAI: BakLLaVA (2024), https://github.com/SkunkworksAI/BakLLaVA -->

<!-- [原子块 · verbatim] [40] Sun, Q., Cui, Y., Zhang, X., Zhang, F., Yu, Q., Luo, Z., Wang, Y., Rao, Y., Liu, J., Huang, T., et al.: Generative multimodal models are in-context learners. CoRR abs/2312.13286 (2023) -->

<!-- [原子块 · verbatim] [41] Thomee, B., Shamma, D.A., Friedland, G., Elizalde, B., Ni, K., Poland, D., Borth, D., Li, L.J.: YFCC100M: The new data in multimedia research. Commun. ACM 59 (2), 64–73 (2016) -->

<!-- [原子块 · verbatim] [42] Touvron, H., Martin, L., Stone, K., Albert, P., Almahairi, A., Babaei, Y., Bashlykov, N., Batra, S., Bhargava, P., Bhosale, S., Bikel, D., Blecher, L., Ferrer, C.C., Chen, M., Cucurull, G., Esiob -->

<!-- [原子块 · verbatim] [43] Tsukida, K., Gupta, M.R.: How to analyze paired comparison data (Technical Report UWEETR-2011-0004, University of Washington, 2011), https://api.semanticscholar.org/CorpusID:15425240 -->

<!-- [原子块 · verbatim] [44] Wang, L., Yang, N., Huang, X., Yang, L., Majumder, R., Wei, F.: Improving text embeddings with large language models. CoRR abs/2401.00368 (2024) -->

<!-- [原子块 · verbatim] [45] Wauthier, F., Jordan, M., Jojic, N.: Efficient ranking from pairwise comparisons. In: ICML. pp. 109–117 (2013) -->

<!-- [原子块 · verbatim] [46] Wu, H., Chen, C., Hou, J., Liao, L., Wang, A., Sun, W., Yan, Q., Lin, W.: FAST-VQA: Efficient end-to-end video quality assessment with fragment sampling. In: ECCV. pp. 538–554 (2022) -->

<!-- [原子块 · verbatim] [47] Wu, H., Chen, C., Liao, L., Hou, J., Sun, W., Yan, Q., Gu, J., Lin, W.: Neighbourhood representative sampling for efficient end-to-end video quality assessment. IEEE TPAMI (2023) -->

<!-- [原子块 · verbatim] [48] Wu, H., Zhang, E., Liao, L., Chen, C., Hou, J., Wang, A., Sun, W., Yan, Q., Lin, W.: Exploring video quality assessment on user generated contents from aesthetic and technical perspectives. In: I -->

<!-- [原子块 · verbatim] [49] Wu, H., Zhang, Z., Zhang, E., Chen, C., Liao, L., Wang, A., Li, C., Sun, W., Yan, Q., Zhai, G., Lin, W.: Q-Bench: A benchmark for general-purpose foundation models on low-level vision. In: ICLR ( -->

<!-- [原子块 · verbatim] [50] Wu, H., Zhang, Z., Zhang, E., Chen, C., Liao, L., Wang, A., Xu, K., Li, C., Hou, J., Zhai, G., et al.: Q-instruct: Improving low-level visual abilities for multi-modality foundation models. CoRR  -->

<!-- [原子块 · verbatim] [51] Wu, H., Zhang, Z., Zhang, W., Chen, C., Liao, L., Li, C., Gao, Y., Wang, A., Zhang, E., Sun, W., et al.: Q-Align: Teaching lmms for visual scoring via discrete text-defined levels. CoRR abs/2312. -->

<!-- [原子块 · verbatim] [52] Wu, X., Sun, K., Zhu, F., Zhao, R., Li, H.: Better aligning text-to-image models with human preference. CoRR abs/2303.14420 (2023) -->

<!-- [原子块 · verbatim] [53] Xu, J., Liu, X., Wu, Y., Tong, Y., Li, Q., Ding, M., Tang, J., Dong, Y.: ImageReward: Learning and evaluating human preferences for text-to-image generation. CoRR abs/2304.05977 (2023) -->

<!-- [原子块 · verbatim] [54] Ye, P., Doermann, D.: Active sampling for subjective image quality assessment. In: IEEE CVPR. pp. 4249–4256 (2014) -->

<!-- [原子块 · verbatim] [55] Ye, Q., Xu, H., Xu, G., Ye, J., Yan, M., Zhou, Y., Wang, J., Hu, A., Shi, P., Shi, Y., Jiang, C., Li, C., Xu, Y., Chen, H., Tian, J., Qi, Q., Zhang, J., Huang, F.: mPLUG-Owl: Modularization empow -->

<!-- [原子块 · verbatim] [56] Ye, Q., Xu, H., Ye, J., Yan, M., Liu, H., Qian, Q., Zhang, J., Huang, F., Zhou, J.: mPLUG-Owl2: Revolutionizing multi-modal large language model with modality collaboration. CoRR abs/2311.04257 ( -->

<!-- [原子块 · verbatim] [57] Yim, J.G., Wang, Y., Birkbeck, N., Adsumilli, B.: Subjective quality assessment for youtube UGC dataset. In: IEEE ICIP. pp. 1–5 (2020) -->

<!-- [原子块 · verbatim] [58] Yin, Z., Wang, J., Cao, J., Shi, Z., Liu, D., Li, M., Sheng, L., Bai, L., Huang, X., Wang, Z., et al.: LAMM: Language-assisted multi-modal instruction-tuning dataset, framework, and benchmark. Co -->

<!-- [原子块 · verbatim] [59] Ying, Z., Niu, H., Gupta, P., Mahajan, D., Ghadiyaram, D., Bovik, A.: From patches to pictures (PaQ-2-PiQ): Mapping the perceptual space of picture quality. In: IEEE CVPR. pp. 3575–3585 (2020) -->

<!-- [原子块 · verbatim] [60] Yue, X., Ni, Y., Zhang, K., Zheng, T., Liu, R., Zhang, G., Stevens, S., Jiang, D., Ren, W., Sun, Y., et al.: MMMU: A massive multi-discipline multimodal understanding and reasoning benchmark for  -->

<!-- [原子块 · verbatim] [61] Zhang, C., Su, S., Zhu, Y., Yan, Q., Sun, J., Zhang, Y.: Exploring and evaluating image restoration potential in dynamic scenes. In: IEEE CVPR. pp. 2057–2066 (2022) -->

<!-- [原子块 · verbatim] [62] Zhang, R., Isola, P., Efros, A.A., Shechtman, E., Wang, O.: The unreasonable effectiveness of deep features as a perceptual metric. In: IEEE CVPR. pp. 586–595 (2018) -->

<!-- [原子块 · verbatim] [63] Zhang, W., Ma, K., Zhai, G., Yang, X.: Uncertainty-aware blind image quality assessment in the laboratory and wild. IEEE TIP 30 , 3474–3486 (2021) -->

<!-- [原子块 · verbatim] [64] Zhang, W., Zhai, G., Wei, Y., Yang, X., Ma, K.: Blind image quality assessment via vision-language correspondence: A multitask learning perspective. In: IEEE CVPR. pp. 14071–14081 (2023) -->

<!-- [原子块 · verbatim] [65] Zhang, W., Liu, Y., Dong, C., Qiao, Y.: RankSRGan: Generative adversarial networks with ranker for image super-resolution. In: ICCV. pp. 3096–3105 (2019) -->

<!-- [原子块 · verbatim] [66] Zhang, Z., Sun, W., Wang, T., Lu, W., Zhou, Q., Wang, Q., Min, X., Zhai, G., et al.: Subjective and objective quality assessment for in-the-wild computer graphics images. ACM TOMM 20 (4), 1–22 (2 -->

<!-- [原子块 · verbatim] [67] Zhang, Z., Wu, H., Zhang, E., Zhai, G., Lin, W.: A benchmark for multi-modal foundation models on low-level vision: from single images to pairs. CoRR abs/2402.07116 (2024) -->

<!-- [原子块 · verbatim] [68] Zhu, D., Chen, J., Shen, X., Li, X., Elhoseiny, M.: MiniGPT-4: Enhancing vision-language understanding with advanced large language models. CoRR abs/2304.10592 (2023) -->

<!-- [原子块 · verbatim] [69] Zhu, H., Sui, X., Chen, B., Liu, X., Chen, P., Fang, Y., Wang, S.: 2AFC prompting of large multimodal models for image quality assessment. CoRR abs/2402.01162 (2024) -->
