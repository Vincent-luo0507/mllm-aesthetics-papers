# GalleryGPT：用大多模态模型分析绘画作品

> 原标题：GalleryGPT: Analyzing Paintings with Large Multimodal Models
> 作者：Yi Bin, Wenhao Shi, Yujuan Ding, Zhiqiang Hu, Zheng Wang, Yang Yang, See-Kiong Ng, Heng Tao Shen · arXiv:2408.00491 · 2024-08-01

<!-- [原子块 · verbatim] GalleryGPT: Analyzing Paintings with Large Multimodal Models -->

<!-- [原子块 · verbatim] Abstract. -->

<!-- [原子块 · verbatim] Artwork analysis is important and fundamental skill for art appreciation, which could enrich personal aesthetic sensibility and facilitate the critical thinking ability. Understanding artworks is chal -->

**EN** Keywords:

**ZH** 关键词：

<!-- [原子块 · img]  -->

**EN** Figure 1. An example of existing LMMs for art analysis. The painting (a nameless painting to avoid the knowledge memorized in LLMs) on the left-top corner is the target image to be analyzed, and the bottom one, “The Astronomer” by Johannes Vermeer, is wrongly recognized by GPT-4V. The red texts indicate wrong analysis, mainly belong to wrong recognition by Gemini and GPT-4V. The green texts are good parts for “formal analysis”. The purple texts denote the factual description of the painting content, which is more similar with the image captioning task.

**ZH** 图 1. 现有 LMM 用于艺术分析的一个示例。左上角的画作（为避开 LLM 中记忆的知识，选用一幅无名画作）是待分析的目标图像；下方一幅为 Johannes Vermeer 的《The Astronomer》，被 GPT-4V 错误识别。红色文字表示错误的分析，主要来自 Gemini 与 GPT-4V 的错误识别；绿色文字是“形式分析”中较好的部分；紫色文字表示对画作内容的事实性描述，更接近图像描述任务。

**EN** 1. Introduction

**ZH** 1. 引言

**EN** Artwork analysis and composition are integral aspects of art appreciation and creation, often requiring a deep understanding of artistic techniques, styles, and historical contexts. In the past decades, AI systems have been evolving rapidly and demonstrating remarkable success in many fields, even surpass humans (Bai et al., 2023; Chen et al., 2023c; Li et al., 2023). However, it still cannot understand and analyze an artwork like humans since it involves very high-level joint understanding of culture, symbolism, abstractionism, and other aesthetics knowledge, beyond the basic semantic understanding of objects, attributes and relations in natural image understanding. Motivated by the superior ability of deep learning, researchers have employed several advanced techniques, such as convolutional neural networks (CNN) (Jia et al., 2014; Krizhevsky et al., 2012), recurrent neural networks (Hochreiter and Schmidhuber, 1997), and Transformer (Bin et al., 2022; Vaswani et al., 2017) in style classification, object detection, multimodal retrieval, art visual question answering, and artwork captioning (Sheng and Moens, 2019; Liu et al., 2023; Bin et al., 2021). Despite these advancements, there is still a lack of research on composing comprehensive and in-depth analysis for artworks, limited by the model capacity of visual perception and language generation.

**ZH** 艺术品分析与写作是艺术鉴赏与创作不可或缺的组成部分，通常要求对艺术技法、风格与历史语境有深入理解。过去几十年中，人工智能系统快速发展并在诸多领域取得瞩目成就，甚至超越人类（Bai 等，2023；Chen 等，2023c；Li 等，2023）。然而，它仍无法像人类那样理解与分析一件艺术品，因为这涉及对文化、象征、抽象主义以及其他美学知识的高度综合理解，超出了自然图像理解中对物体、属性与关系的基本语义理解。受深度学习优越能力的驱动，研究者采用了卷积神经网络（CNN）（Jia 等，2014；Krizhevsky 等，2012）、循环神经网络（Hochreiter 和 Schmidhuber，1997）与 Transformer（Bin 等，2022；Vaswani 等，2017）等多种先进技术，用于风格分类、目标检测、多模态检索、艺术视觉问答与艺术品描述生成（Sheng 和 Moens，2019；Liu 等，2023；Bin 等，2021）。尽管取得这些进展，受限于模型的视觉感知与语言生成能力，针对艺术品撰写全面而深入的分析仍然缺乏研究。

**EN** The emergence of large foundation models, such large language models (LLMs) (Brown et al., 2020; Ding et al., 2024a; Touvron et al., 2023a; Touvron et al., 2023b) and large multimodal models (LMMs) (Li et al., 2022; Shi et al., 2024; Li et al., 2023; Chen et al., 2023c), has facilitated the progress across numerous research areas, including text summarization, open-ended question answering, and long-context reasoning, and led to significant advancements (Ding et al., 2024a; Nguyen et al., 2024; Ding et al., 2024b). This also makes it possible to enable machine to perceive and understand visual content and generate detail descriptions, such as visual storytelling (Huang et al., 2016). However, despite the achievements on natural image understanding, we observe that existing LMMs still cannot comprehend the high-level concepts and generate comprehensive analysis for artworks. As the example illustrated in Figure 1, we test several powerful LMMs, i.e., GPT-4V (Inc, 2023b), Gemini (Inc, 2023a), and ShareGPT4V (Chen et al., 2023a), with a nameless painting11 1 We choose a nameless painting to avoid the knowledge about the painting has been seen during pre-training and Supervised-Fine-Tuning (SFT), since the knowledge about famous ones is memorized by the LLMs. This nameless painting is downloaded from: https://darksky.org/app/uploads/2015/11/8_Florinus_Astronomy.png by asking them to compose a paragraph of formal analysis. From the outputs, we can observe that the GPT-4V and Gemini wrongly recognized this painting to another, and then give the analysis based on the knowledge recalled from their language-part memories, which means they function as LLMs in this part. We call this phenomenon as “LLM-biased visual hallucination”. This phenomenon suggests that in this task, existing LMMs tend to first recognize the given painting is and then give analysis accordingly, while do not focus on the visual content of the painting at the stage of analysis generation. Such a recognize-then-analyze procedure highly relies on the accuracy of the recognition, and will fail when the given painting is unknown. Although we have noticed that GPT-4V tries to analyze this painting based on the visual content (green part shown analysis shown in Figure 1), it still cannot completely escape from the recognize-then-analyze procedure. Meanwhile, some effort has been devoted to enhance the visual understanding of LMMs. For example, ShareGPT4V (Chen et al., 2023a) contributes a dataset with high-quality image and description pairs to fine-tune the LLaVA model (Liu et al., 2024). Despite of the effectiveness, these methods still fail to make professional artistic, aesthetic and technical analysis on artworks or paintings, meaning that existing LMMs so far cannot satisfy the requirements of artwork analysis. They may face particular challenges to get generalized into unknown or unseen subjects, thereby calling for better solutions.

**ZH** 大语言模型（LLM）（Brown 等，2020；Ding 等，2024a；Touvron 等，2023a；Touvron 等，2023b）与大多模态模型（LMM）（Li 等，2022；Shi 等，2024；Li 等，2023；Chen 等，2023c）等大型基础模型的涌现，推动了文本摘要、开放式问答与长上下文推理等众多研究领域的进展，并带来了显著提升（Ding 等，2024a；Nguyen 等，2024；Ding 等，2024b）。这也使机器有可能感知并理解视觉内容、生成细节描述，例如视觉故事讲述（Huang 等，2016）。然而，尽管在自然图像理解上成果斐然，我们观察到现有 LMM 仍无法理解高层概念并为艺术品生成全面分析。以图 1 所示示例为例，我们测试了若干强大的 LMM，即 GPT-4V（Inc，2023b）、Gemini（Inc，2023a）与 ShareGPT4V（Chen 等，2023a），用一幅无名画作（脚注 1：我们选择一幅无名画作，以避免该画作的知识在预训练与监督微调（SFT）阶段被见过，因为著名画作的知识已被 LLM 记忆。该无名画作下载自：https://darksky.org/app/uploads/2015/11/8_Florinus_Astronomy.png）要求它们撰写一段形式分析。从输出可以看出，GPT-4V 与 Gemini 把这幅画错认成另一幅，并基于从其语言部分记忆中召回的知识给出分析，这意味着它们在此环节只是充当 LLM。我们把这一现象称为“LLM 偏置的视觉幻觉”。该现象说明，在这项任务中，现有 LMM 倾向于先识别给定画作是什么、再据此给出分析，而在分析生成阶段并不关注画作本身的视觉内容。这种“先识别再分析”的流程高度依赖识别的准确性，当给定画作不为人知时便会失效。尽管我们注意到 GPT-4V 试图基于视觉内容分析这幅画（图 1 中绿色部分所示的分析），它仍无法完全摆脱“先识别再分析”的流程。与此同时，也有一些工作致力于增强 LMM 的视觉理解。例如 ShareGPT4V（Chen 等，2023a）贡献了一个高质量图像—描述配对数据集，用于微调 LLaVA 模型（Liu 等，2024）。尽管有效，这些方法仍无法对艺术品或绘画做出专业的艺术、美学与技术分析，意味着现有 LMM 尚不能满足艺术品分析的要求。它们在泛化到未知或未见过的对象时可能面临特殊挑战，因而需要更好的解决方案。

**EN** To fill the research gap, this paper focuses on generating formal analysis for painting images, relying on the LMMs but pushing them to perceive and comprehend the artistic skills or other professional visual aspects shown in an artwork itself. A comprehensive artwork analysis includes many parts, e.g., introduction, cultural, formal analysis, historical context, interpretation, etc. Although most of artwork analysis may be done relying only on the external knowledge or subjective opinions, the “form” of the artwork, including color, composition, line, shape, light and shadow, and other visual aspects , still requires vision-based understanding. Therefore, it is necessary to develop a professional LMM specialized for making formal analysis for artworks.

**ZH** 为填补这一研究空白，本文聚焦于为画作图像生成形式分析，依托 LMM 但推动其去感知与理解艺术品自身所呈现的艺术技法或其他专业视觉面向。一篇完整的艺术品分析包含多个部分，例如引言、文化、形式分析、历史语境、阐释等。尽管艺术品分析的大部分内容可以只依靠外部知识或主观看法完成，但艺术品的“形式”——包括色彩、构图、线条、形状、光影以及其他视觉面向——仍需要基于视觉的理解。因此，有必要开发一个专门面向艺术品形式分析的专业 LMM。

**EN** However, there does not exist any formal analysis dataset. It is also time- and labour-expensive to make annotations because writing a formal analysis for an painting requires professional expertise in art analyzing. Motivated by the aforementioned observed LLMs bias by GPT4 and Gemini, we try to access the knowledge memorized in LLMs to produce analyses for known artworks. Specifically, we first collect about 19k famous painting images and corresponding meta data from the Internet. Then, apply LLMs to provide a paragraph analysis only focusing on visual characteristics based on the title and artist of the painting, thereby generating the formal analysis. We also prompt the LLMs to compose the formal analysis from some specific form perspectives, such as composition, color, light and shadow, to enhance the richness and diversity of the data. We finally obtain about 50k formal analyses for the paintings we collect and name this dataset as PaintingForm.

**ZH** 然而，目前并不存在任何形式分析数据集。而为一件画作撰写形式分析需要具备艺术分析的专业知识，标注既费时又费人力。受前述 GPT-4 与 Gemini 表现出的 LLM 偏置现象启发，我们尝试利用 LLM 中记忆的知识来为已知艺术品生成分析。具体而言，我们首先从互联网收集约 19k 幅著名画作图像及相应元数据；随后让 LLM 基于画作的标题与艺术家，给出只聚焦于视觉特征的段落分析，由此生成形式分析。我们还提示 LLM 从构图、色彩、光影等若干特定形式视角撰写形式分析，以提升数据的丰富度与多样性。最终我们为所收集的画作获得约 50k 条形式分析，并将该数据集命名为 PaintingForm。

**EN** Leveraging the PaintingForm dataset, we present GalleryGPT, a large multi-modal model with a LLaVA architecture fine-tuned based on ShareGPT4V-7B (Chen et al., 2023a). As ShareGPT4V is boosted for image understanding and performs well in visual description generation, we freeze the parameters in vision encoder to retain its superb visual perception ability. Meanwhile, we add a LoRA component to LLM to learn the specific analyzing patterns of paintings. To evaluate the effectiveness of our GalleryGPT, we conduct zero-shot learning on several classic painting analysis datasets, including AQUA (Garcia et al., 2020), ArtQuest (Bleidt et al., 2024), and ArtQuest-Type (Bleidt et al., 2024) for art visual question answering, and ArtBench (Liao et al., 2022) for style classification. The results show that our GalleryGPT outperforms several off-the-shelf and adaptive LMMs, demonstrating the superiority of our collected data and impressive performance of GalleryGPT.

**ZH** 借助 PaintingForm 数据集，我们提出 GalleryGPT——一个基于 ShareGPT4V-7B（Chen 等，2023a）微调、采用 LLaVA 架构的大多模态模型。由于 ShareGPT4V 在图像理解上得到增强、在视觉描述生成上表现良好，我们冻结视觉编码器中的参数，以保留其出色的视觉感知能力；同时在大语言模型上加入 LoRA 组件，用于学习画作特有的分析模式。为验证 GalleryGPT 的有效性，我们在若干经典画作分析数据集上做零样本实验，包括用于艺术视觉问答的 AQUA（Garcia 等，2020）、ArtQuest（Bleidt 等，2024）与 ArtQuest-Type（Bleidt 等，2024），以及用于风格分类的 ArtBench（Liao 等，2022）。结果表明，我们的 GalleryGPT 优于若干现成的与经过适配的 LMM，显示出所收集数据的优越性与 GalleryGPT 的出色性能。

**EN** In summary, the contributions of this work are as follows:

**ZH** 综上，本工作的贡献如下：

**EN** • We propose to empower the perception ability of LMMs for subtle and specific visual characteristics of artworks, and introduce the task of generating formal analysis to enable the ability by supervised fine-tuning.

**ZH** • 我们提出增强 LMM 对艺术品细微而特定视觉特征的感知能力，并引入形式分析生成任务，通过监督微调来赋予模型这一能力。

**EN** • To support the research, we contribute a large-scale and high-quality dataset PaintingForm, acquired by two powerful LLMs, i.e., GPT-4 and Gemini, based on the learnt knowledge about famous paintings. To avoid the leakage of prior knowledge, we ask the LLMs only focus on visual characteristics and do not mention the title and artist in the formal analysis annotation.

**ZH** • 为支撑该研究，我们贡献了一个大规模、高质量的数据集 PaintingForm，它由 GPT-4 与 Gemini 两个强大的 LLM 基于其对著名画作习得的知识生成。为避免先验知识泄露，我们要求 LLM 只关注视觉特征，且在形式分析标注中不提及标题与艺术家。

**EN** • Leveraging the collected dataset, we devise an advanced large multimodal model for painting formal analysis generation, dubbed GalleryGPT, which employs ShareGPT4V as backbone. We evaluate its ability on several painting analysis tasks, and the results demonstrate the impressive performance of it.

**ZH** • 利用所收集的数据集，我们以 ShareGPT4V 为骨干，设计了一个用于绘画形式分析生成的先进大多模态模型 GalleryGPT。我们在若干画作分析任务上评估其能力，结果证明了它的出色表现。

**EN** 2. Related Works

**ZH** 2. 相关工作

**EN** 2.1. Large Language Models (LLMs)

**ZH** 2.1. 大语言模型（LLM）

**EN** In the past decade, language modelling has been evolving rapidly and achieved impressive progress (Pennington et al., 2014; Bahdanau et al., 2014; Vaswani et al., 2017; Devlin et al., 2018). Transformer (Vaswani et al., 2017) employed multiple attention blocks and positional embedding to accelerate the recurrent models and made breakthrough in language models. Delvin et al.(Devlin et al., 2018) designed a bidirectional transfomer to learn the contextual embedding of words and made the beginning the era of pre-training language model (PLM) (Liu et al., 2019; Lewis et al., 2019; Radford et al., 2018; Radford et al., 2019; Raffel et al., 2020). With the large scale tokens pre-training, deep neural models, especially the large language models (LLMs) (Brown et al., 2020; Chowdhery et al., 2023) based on the Transformer (Vaswani et al., 2017) structure, demonstrate superb understanding and generation ability, as well as generalizing to downstream tasks, even without any fine-tuning. LaMDA(Thoppilan et al., 2022) focused on conversational applications and aims to generate more natural and logically-rich dialogue text. InstructGPT(Ouyang et al., 2022) designed an effective fine-tuning method that allows LLMs to operate according to desired instructions, leveraging Reinforcement Learning from Human Feedback(RLHF). It incorporates humans into the training loop using carefully designed annotation strategies. With the instruction fine-tuning based on large foundation models, LLMs, especially the ChatGPT system (Inc, 2022) of OpenAI, also demonstrate emergent capacity of generation (Team, 2023; Touvron et al., 2023a). The LLaMA(Touvron et al., 2023a; Touvron et al., 2023b) model released by Meta, with its open-source nature and smaller parameter size, has provided an opportunity for many researchers to participate in large language model research and led to rapid research progress in LLMs.

**ZH** 过去十年中，语言建模快速发展并取得令人瞩目的进展（Pennington 等，2014；Bahdanau 等，2014；Vaswani 等，2017；Devlin 等，2018）。Transformer（Vaswani 等，2017）采用多个注意力块与位置嵌入来加速循环模型，并在语言模型上取得突破。Devlin 等（Devlin 等，2018）设计了一个双向 Transformer 来学习词的上下文嵌入，开启了预训练语言模型（PLM）的时代（Liu 等，2019；Lewis 等，2019；Radford 等，2018；Radford 等，2019；Raffel 等，2020）。随着大规模词元预训练的开展，深度神经模型——尤其是基于 Transformer（Vaswani 等，2017）结构的大语言模型（LLM）（Brown 等，2020；Chowdhery 等，2023）——展现出卓越的理解与生成能力，并能泛化到下游任务，甚至无需任何微调。LaMDA（Thoppilan 等，2022）聚焦对话应用，旨在生成更自然、逻辑更丰富的对话文本。InstructGPT（Ouyang 等，2022）设计了一种有效的微调方法，利用基于人类反馈的强化学习（RLHF）使 LLM 能按期望指令运作，并通过精心设计的标注策略把人类纳入训练闭环。在基于大型基础模型的指令微调之下，LLM——尤其是 OpenAI 的 ChatGPT 系统（Inc，2022）——也展现出涌现的生成能力（Team，2023；Touvron 等，2023a）。Meta 发布的 LLaMA（Touvron 等，2023a；Touvron 等，2023b）模型凭借其开源性质与较小的参数规模，为众多研究者参与大语言模型研究提供了机会，并推动了 LLM 研究的快速进展。

**EN** 2.2. Large Multimodal Models (LMMs)

**ZH** 2.2. 大多模态模型（LMM）

**EN** The blooming of large language models has attracted a great amount of research attention on vision-language interaction and injecting visual knowledge into LLMs. As a paradigm of visual language modal alignment, CLIP (Radford et al., 2021) implemented contrastive learning on extensive image-text pairs. Subsequent improvements (Li et al., 2022; Li et al., 2023) over CLIP utilized enhanced data strategies with greater data diversity for basic visual tasks. Recent research has increasingly focused on pre-traning alignment and visual instruction tuning on top of the LLMs for more complex tasks such as visual question answering and reasoning. MiniGPT-4 (Chen et al., 2023c) demonstrated capabilities in image-text dialogues by aligning queried visual feature with text and feeding queried embedding to LLM. Other prominent examples including LLaVA (Liu et al., 2024), Qwen-VL (Bai et al., 2023), InstructBLIP (Dai et al., 2024), and ShareGPT4V (Chen et al., 2023a) interacted visual features with LLM using a learnable projector or query embeddings, which focus on utilizing more and high quality pre-training and fine-tuning data to understand complex instructions. mPLUG-Owl (Ye et al., 2023), Shikra (Chen et al., 2023b), and KOSMOS-2 (Peng et al., 2023) introduced grounding data types and new modularization training to minimize hallucinations and enhance grounding ability. Despite these advancements, exploration for quality and format of images-instructions highlights a critical area for future large multimodal models improvement.

**ZH** 大语言模型的蓬勃发展吸引了大量研究关注投向视觉—语言交互，以及把视觉知识注入 LLM。作为视觉语言模态对齐的范式，CLIP（Radford 等，2021）在大规模图文对上实现对比学习。在 CLIP 基础上的后续改进（Li 等，2022；Li 等，2023）采用了数据多样性更强的增强数据策略，用于基础视觉任务。近期研究越来越关注在 LLM 之上做预训练对齐与视觉指令微调，以处理视觉问答与推理等更复杂的任务。MiniGPT-4（Chen 等，2023c）通过把查询到的视觉特征与文本对齐、并将查询到的嵌入送入 LLM，展现出图文对话能力。其他代表性工作包括 LLaVA（Liu 等，2024）、Qwen-VL（Bai 等，2023）、InstructBLIP（Dai 等，2024）与 ShareGPT4V（Chen 等，2023a），它们用可学习的投影器或查询嵌入把视觉特征与 LLM 交互，侧重于用更多、更高质量的预训练与微调数据来理解复杂指令。mPLUG-Owl（Ye 等，2023）、Shikra（Chen 等，2023b）与 KOSMOS-2（Peng 等，2023）引入定位数据类型与新的模块化训练，以最小化幻觉并增强定位能力。尽管取得这些进展，对图像—指令的质量与形式的探索仍凸显出未来大多模态模型改进的一个关键方向。

<!-- [原子块 · img]  -->

**EN** Figure 2. The overall pipeline of constructing our PaintingForm collection. Our annotation process only depends on the language model, without vision information. The prompt illustrated here just a simple version for exhibition, we actually elaborately designed the prompts.

**ZH** 图 2. 构建 PaintingForm 数据集的整体流程。我们的标注过程只依赖语言模型，不涉及视觉信息。此处展示的提示仅为简化版，实际使用的提示经过精心设计。

**EN** 2.3. AI for Art Analysis

**ZH** 2.3. 面向艺术分析的 AI

**EN** With the great success of deep learning in CV and NLP in the past decade, AI for art analysis has also been evolving with rapid progress. Early works most depended on hand-crafted features and explored the classification and recognition problem (Johnson et al., 2008; Khan et al., 2014; Carneiro et al., 2012; Shamir et al., 2010; Gatys et al., 2016). With the great success of pre-trained language models (PLM) (Kenton and Toutanova, 2019; Yang et al., 2019) and visual-language pre-training (VLP) (Li et al., 2020; Radford et al., 2021), research on artwork analysis also achieves significant progress. CLIP-Art (Conde and Turgutlu, 2021) leveraged the image-text pairs of artworks in SemArt (Garcia and Vogiatzis, 2018) to fine-tune the CLIP and gains impressive improvements. Garcia et al. (Garcia et al., 2020) contributed a dataset of art visual question answering, named AQUA, and proposed a knowledge-based VIKING model, which achieves the best performance. Bleidt et al. (Bleidt et al., 2024) pointed out there exists language bias hidden in the question-answer pair, which may induce the model to ignore the visual information. To address this issue, they further proposed a strategy to eliminate the bias and introduced an ArtQuest dataset and implemented PrefixLM to learn the patterns between paintings and questions.

**ZH** 随着深度学习过去十年在 CV 与 NLP 上的巨大成功，面向艺术分析的 AI 也在快速演进。早期工作多依赖手工特征，探索分类与识别问题（Johnson 等，2008；Khan 等，2014；Carneiro 等，2012；Shamir 等，2010；Gatys 等，2016）。随着预训练语言模型（PLM）（Kenton 和 Toutanova，2019；Yang 等，2019）与视觉—语言预训练（VLP）（Li 等，2020；Radford 等，2021）的巨大成功，艺术品分析研究也取得显著进展。CLIP-Art（Conde 和 Turgutlu，2021）利用 SemArt（Garcia 和 Vogiatzis，2018）中艺术品的图文对微调 CLIP，取得了令人印象深刻的提升。Garcia 等（Garcia 等，2020）贡献了一个艺术视觉问答数据集 AQUA，并提出基于知识的 VIKING 模型，取得了最佳性能。Bleidt 等（Bleidt 等，2024）指出问答对中潜藏语言偏置，可能诱导模型忽略视觉信息。为解决该问题，他们进一步提出消除偏置的策略，引入 ArtQuest 数据集，并实现 PrefixLM 来学习画作与问题之间的模式。

**EN** Despite these simple tasks investigated in deep learning era, people also expect the AI system could provide comprehensive analysis for artworks, which may benefit the art education and assist human writing the commentary. Recently, LLMs and LMMs have been demonstrating superb understanding and generation ability in many areas, which raise the potentials to compose comprehensive analysis for artworks. However, we argue current LMMs might be biased by the knowledge memorized in language and cannot generalized to nameless artworks. In this work, we try to implement formal analysis with LLMs to make them focusing on visual elements in art analysis.

**ZH** 尽管深度学习时代研究的是这些简单任务，人们仍期待 AI 系统能为艺术品提供全面分析，这有望惠及艺术教育并辅助人类撰写评论。近来，LLM 与 LMM 在诸多领域展现出卓越的理解与生成能力，为撰写全面的艺术品分析带来可能。然而我们认为，当前的 LMM 可能被语言中所记忆的知识带偏，无法泛化到无名的艺术品。本工作尝试用 LLM 实现形式分析，使其在艺术分析中聚焦于视觉要素。

**EN** 3. Data Collection

**ZH** 3. 数据采集

<!-- [原子块 · object]  -->

**EN** Figure 3. An statistic illustration of the distribution of paintings by each artist in Most Popular Artists. Valid paintings denote the reserved paintings after the filtering rules in Section 3.2, and the invalid paintings are the discarded ones. We finally filter 769 and reserve 18,026 paintings for this part (not include the 500 most popular paintings). We do not include the 500 paintings for illustration because: 1) all the 500 popular paintings are reserved, and 2) there exist about 150 artists have only one paintings in this gallery, resulting in severe long-tail distribution here.

**ZH** 图 3. “最受欢迎艺术家”中各艺术家画作分布的统计示意。有效画作指经 3.2 节过滤规则后保留的画作，无效画作则为被丢弃者。我们最终在该部分过滤掉 769 幅、保留 18,026 幅画作（不含 500 幅最受欢迎画作）。我们未把这 500 幅画作纳入统计，原因有二：1）这 500 幅受欢迎画作全部被保留；2）该画廊中约有 150 位艺术家仅有一幅画作，此处呈现严重的长尾分布。

<!-- [原子块 · object]  -->

**EN** Figure 4. Statistics of elements of formal analysis. Only very few paintings (8 in total) contain the elements Scale and Proportion.

**ZH** 图 4. 形式分析要素的统计。只有极少数画作（共 8 幅）包含“尺度与比例”要素。

**EN** 3.1. Primary Philosophy

**ZH** 3.1. 基本理念

**EN** A successful artwork analysis, as been discussed before, needs to cover multiple types of content including background introduction, formal analysis, historical context, etc, most of which rely on external knowledge and subjective opinions except formal analysis. As we have known, existing of-the-shelf LMMs have been capable of providing factual information and description with relevant knowledge while tend to ignore visual analysis, we want to enhance the existing artwork analysis models to focus more on visual elements. The research purpose in this work is to make the developed model to emphasize on visual comprehension rather than recognizing the artwork and retrieving knowledge from their language memory, in other word, to twist the recognize-then-analyze procedure of existing LMMs on artwork analysis which may cause “LLM-biased visual hallucination”.

**ZH** 如前所述，一篇成功的艺术品分析需要涵盖背景介绍、形式分析、历史语境等多类内容，其中除形式分析外大多依赖外部知识与主观看法。我们知道，现有现成的 LMM 已能结合相关知识提供事实信息与描述，却往往忽视视觉分析；我们希望增强现有的艺术品分析模型，使其更聚焦于视觉要素。本工作的研究目的是让所开发的模型强调视觉理解，而不是去识别艺术品并从其语言记忆中检索知识；换言之，扭转现有 LMM 在艺术品分析上“先识别再分析”的流程，该流程可能导致“LLM 偏置的视觉幻觉”。

**EN** To support the development of such a professional LMM specialized for artwork analysis, we try to construct a large-scale artwork analysis dataset, including images and corresponding analysis, so that we can fine-tune the pre-trained LMMs. More importantly, to push the LMMs to focus on visual comprehending of the artworks through fine-tuning, we need high-quality formal analysis annotations in our dataset. However, manually annotating artworks with comprehensive analysis requires professional expertise in artwork analyzing and it is hard and expensive to recruit so many professional art critics. Besides, even with experts, it is still time-consuming to annotate large number of artworks.

**ZH** 为支撑这样一个专门面向艺术品分析的 LMM 的开发，我们尝试构建一个大规模艺术品分析数据集，包含图像与相应分析，以便对预训练 LMM 做微调。更重要的是，为通过微调推动 LMM 聚焦于对艺术品的视觉理解，我们的数据集中需要有高质量的形式分析标注。然而，为艺术品手工标注全面分析需要具备艺术品分析的专业知识，而招募如此多的专业艺术评论家既困难又昂贵。此外，即便有专家参与，标注大量艺术品仍然耗时。

**EN** Based on these motivations and challenges, we collect a painting dataset, named PaintingForm, consisting of paintings and associated formal analyses annotations for each painting. Since manual labeling is affordably expensive in terms of both timing and economic cost, we elaborately leverage the powerful LLMs to produce formal analysis on famous paintings, ensuring they have enough knowledge to support them producing high-quality analysis. The overall pipeline of our data collection process is shown in Figure 2 and more details are described in subsequent sections.

**ZH** 基于上述动机与挑战，我们收集了一个绘画数据集，命名为 PaintingForm，由画作及每幅画作对应的形式分析标注构成。由于人工标注在时间与经济成本上都难以承受，我们精心利用强大的 LLM 为著名画作生成形式分析，确保它们有足够知识支撑其产出高质量分析。数据采集流程的整体管线如图 2 所示，更多细节见后续小节。

**EN** 3.2. Painting Source

**ZH** 3.2. 画作来源

**EN** With the development of digital technology in recent years, large collections of artworks have been digitized and stored, and easily to accessed via the Internet. We focus on famous paintings and choose 1st Art Gallery22 2 https://www.1st-art-gallery.com/ as our painting source. To make the LMMs, e.g., GPT-4 and Gemini, able to provide accurate and comprehensive formal analyses, we choose the paintings of 500 Most Popular Paintings33 3 https://www.1st-art-gallery.com/most-popular-paintings.html and Most Popular Artists44 4 https://www.1st-art-gallery.com/browse-by-artist-a-z.html. Note that here we only use the most popular artists, not all, resulting in 48 artists in total. to ensure the LLMs knowing the paintings. With such condition, we obtain 19,295 paintings (including 18,795 of most popular artists). To ensure the LLMs know the paintings, we first ask Gemini to answer if it knows the painting with title and artist name. We also filter out some paintings without certain title and annotated as ‘‘unknown’’, and obtain 18,526 paintings in the end. We select 5000 less popular paintings for test and reserve 13,526 for training, test samples of which are identified by the wishlist count from source website, and the distribution across artists is also considered. We illustrate the statistics of artist distribution of the Most Popular Artists55 5 We do not include the 500 most popular paintings in this statistics because about 150 artists only contribute one painting in the whole gallery. in Figure 3. From the statistics, we observe that the dataset includes most paintings of Vincent Van Gogh, resulting in 1458 retained and 225 filtered, and Jacques Louis David with the fewest paintings included in the dataset, about 100 paintings. We have also verified that all the paintings are free to use without copyright concerns, as provided by the website66 6 https://www.1st-art-gallery.com/copyrights.html, The copyright contents are as [Accessed on 4 April, 2024.]: “All images on our site are either licensed or in public domain because their copyright has expired. This applies to the United States, Canada, the European Union and the countries with a copyright term of life of the author plus 70 years.”.

**ZH** 近年来随着数字技术的发展，大量艺术品收藏已被数字化存储，并可通过互联网便捷获取。我们聚焦著名画作，选择 1st Art Gallery（脚注 2：https://www.1st-art-gallery.com/）作为画作来源。为使 GPT-4、Gemini 等 LMM 能提供准确而全面的形式分析，我们选取“500 幅最受欢迎画作”（脚注 3：https://www.1st-art-gallery.com/most-popular-paintings.html）与“最受欢迎艺术家”（脚注 4：https://www.1st-art-gallery.com/browse-by-artist-a-z.html。注意此处只取最受欢迎的艺术家而非全部，共 48 位。）中的画作，以确保 LLM 认识这些画作。在此条件下，我们获得 19,295 幅画作（其中 18,795 幅来自最受欢迎艺术家）。为确保 LLM 认识这些画作，我们首先让 Gemini 依据标题与艺术家姓名回答是否知道该画作；我们还会滤除部分没有确定标题、被标注为“unknown”的画作，最终得到 18,526 幅画作。我们选取 5000 幅较不受欢迎的画作用于测试，保留 13,526 幅用于训练；测试样本依据来源网站的收藏清单计数确定，同时也考虑了跨艺术家的分布。我们在图 3 中给出“最受欢迎艺术家”（脚注 5：我们未把 500 幅最受欢迎画作纳入该统计，因为整个画廊中约有 150 位艺术家仅贡献一幅画作。）的画家分布统计。从统计可以看出，数据集中包含最多的是 Vincent Van Gogh 的画作，保留 1458 幅、过滤 225 幅；包含最少的是 Jacques Louis David，约 100 幅。我们也已核实所有画作均可免费使用、不存在版权问题，正如网站（脚注 6：https://www.1st-art-gallery.com/copyrights.html）所声明，版权内容如下［访问日期：2024 年 4 月 4 日］：“本站所有图像均已获得授权，或因其版权已过期而进入公有领域。这适用于美国、加拿大、欧盟，以及版权期限为作者终身加 70 年的国家。”

**EN** 3.3. Formal Analysis Annotation

**ZH** 3.3. 形式分析标注

**EN** As aforementioned, we employ powerful LLMs to generate high quality formal analysis, after ensuring the paintings are known by the LLMs. Note that we only provide the LLMs the title and artist name of the paintings, and do not input any visual information, i.e., the painting image, to the LLMs. Specifically, we employ two powerful LLMs, GPT-4 and Gemini in this work, to retrieve the learnt knowledge with the title and artist name of a certain painting and generate a paragraph of formal analysis only focusing on visual characteristics. To make the formal analyses more diverse, we ask the LLMs to generate two-level formal analyses: 1) overall formal analysis, and 2) formal analysis from a certain perspective, e.g., color, composition, and etc. To avoid the “LLM-biased visual hallucination”, we ask the LLMs do not mention the title and artist name in the generated formal analysis. In other words, one cannot easily identify the corresponding painting solely depending on a specific formal analysis. For the perspective specified formal analysis annotation, we first ask GPT-4 and Gemini to provide up to 5 most important perspectives of the given painting independently, and utilize the intersection of GPT-4 and Gemini predictions as the final perspectives. The statistics of perspectives is shown in Figure 4, from which we observe that Composition, Light and Shadow, Color Palette, Form and Shape are the most common perspectives of the paintings. Finally, based on the selected perspectives, we employ LLMs to annotate the formal analysis only focusing on a specific perspectives similar with the overall setting.

**ZH** 如前所述，在确认 LLM 认识这些画作之后，我们利用强大的 LLM 生成高质量的形式分析。注意我们只向 LLM 提供画作的标题与艺术家姓名，不输入任何视觉信息（即画作图像）。具体地，本文采用 GPT-4 与 Gemini 两个强大的 LLM，用某幅画作的标题与艺术家姓名检索其习得的知识，生成一段只聚焦视觉特征的形式分析。为使形式分析更多样，我们要求 LLM 生成两级形式分析：1）整体形式分析；2）从某一特定视角出发的形式分析，例如色彩、构图等。为避免“LLM 偏置的视觉幻觉”，我们要求 LLM 在生成的形式分析中不提及标题与艺术家姓名；换言之，仅凭某一条形式分析无法轻易辨认出对应的画作。对于指定视角的形式分析标注，我们首先让 GPT-4 与 Gemini 各自独立给出给定画作最多 5 个最重要的视角，并取两者预测的交集作为最终视角。视角统计如图 4 所示，从中可以看到构图、光影、配色、形态与形状是画作最常见的视角。最后，基于选定的视角，我们让 LLM 以与整体设定类似的方式，标注只聚焦某一特定视角的形式分析。

**EN** 4. The Proposed GalleryGPT

**ZH** 4. 本文提出的 GalleryGPT

**EN** To verify if our proposed PaintingForm dataset could empower LMMs more superior painting analyzing ability, we develop a large multimodal model, GalleryGPT, based on ShareGPT4V-7B that has demonstrated impressive performance across several multimodal tasks. We conduct supervised fine-tuning (SFT) on our PaintingForm dataset to enable the LLMs to analyze paintings focusing on visual elements.

**ZH** 为验证所提出的 PaintingForm 数据集能否赋予 LMM 更优越的画作分析能力，我们基于在多个多模态任务上表现出色的 ShareGPT4V-7B 开发了一个大多模态模型 GalleryGPT。我们在 PaintingForm 数据集上做监督微调（SFT），使模型能够聚焦于视觉要素来分析画作。

**EN** 4.1. Architecture

**ZH** 4.1. 架构

**EN** As pointed out before, our goal is enabling LMMs to analyze artworks focusing more on visual elements, rather to design a new architecture or model. Therefore, we introduce the GalleryGPT employing ShareGPT4V-7B as backbone, which follows the LLaVA (Liu et al., 2024) architecture and consists of three components: 1) The visual encoder, which is a vision transformer (ViT) (Dosovitskiy et al., 2020) borrowed from the CLIP-Large (Radford et al., 2021). Similar with CLIP-Large, the visual encoder takes 336*336 shape as input size and divides it into 14 patches, resulting in 576 input tokens; 2) The projector, a two-layer MLP to project the visual representation into the language semantic space, LLMs space in specific; 3) The LLM, which is based on Vicuna-v1.5 (Team, 2023) and LLaMA2 (Touvron et al., 2023a), employing the decoder-only architecture. For the whole setting, we follow ShareGPT4V-7B focusing on the 7B model. Besides, to keep the superior visual perception and describing ability of ShareGPT4V-7B, we slightly modify the LLM in our GalleryGPT. Specifically, we add several LoRA (Hu et al., 2021) modules to learn the formal analysis specific patterns and freeze the LLM in ShareGPT4V-7B to keep its superb content describing ability.

**ZH** 如前所述，我们的目标是让 LMM 在分析艺术品时更聚焦于视觉要素，而非设计新的架构或模型。因此，我们提出的 GalleryGPT 以 ShareGPT4V-7B 为骨干，遵循 LLaVA（Liu 等，2024）架构，包含三个组件：1）视觉编码器，是一个取自 CLIP-Large（Radford 等，2021）的视觉 Transformer（ViT）（Dosovitskiy 等，2020）；与 CLIP-Large 类似，视觉编码器以 336*336 的尺寸为输入，并将其划分为 14 个块，得到 576 个输入词元；2）投影器，一个两层 MLP，把视觉表示投影到语言语义空间，具体即 LLM 空间；3）大语言模型，基于 Vicuna-v1.5（Team，2023）与 LLaMA2（Touvron 等，2023a），采用仅解码器架构。整体设置上，我们沿用 ShareGPT4V-7B，聚焦 7B 模型。此外，为保持 ShareGPT4V-7B 出色的视觉感知与描述能力，我们对 GalleryGPT 中的大语言模型做了小幅修改：具体地，我们加入若干 LoRA（Hu 等，2021）模块来学习形式分析特有的模式，并冻结 ShareGPT4V-7B 中的大语言模型，以保留其出色的内容描述能力。

**EN** 4.2. Supervised Fine-Tuning

**ZH** 4.2. 监督微调

**EN** Numbers of previous works (Touvron et al., 2023a; Ouyang et al., 2022; Inc, 2023b; Yang et al., 2023; Team, 2023) have demonstrated that based on billions or trillions of tokens pre-training and elaborate supervised fine-tuning, the LLMs exhibit creative emergent ability and is able to generalize to multiple tasks without further training. Following this inspiration, we implement supervised fine-tuning (SFT) with our LLM-generated formal analyses, paired with the corresponding painting. During SFT stage, we set the learning rate as 2e-5, batch size as 16, and fine-tune 10k steps on an A100 GPU with 80G memory. For the LoRA module, we set the lower rank as 128 and the alpha is 256. Since our analysis texts do not contain any identifying information of the paintings, the LMMs cannot retrieve the learnt knowledge to associate with the paintings. Instead, with our SFT optimization, the LMM tries to perceive the subtle elements and art skills presented in the painting, and matches them with the corresponding descriptions in the formal analysis. Through such fine-tuning, our GalleryGPT could be empowered artwork analyzing ability and generalized to other art analyzing tasks, e.g., style classification.

**ZH** 大量先前工作（Touvron 等，2023a；Ouyang 等，2022；Inc，2023b；Yang 等，2023；Team，2023）已证明，经数十亿乃至数万亿词元的预训练与精心设计的监督微调，LLM 会表现出创造性的涌现能力，并能在无需进一步训练的情况下泛化到多种任务。受此启发，我们用 LLM 生成的形式分析及其对应画作配对实施监督微调（SFT）。在 SFT 阶段，我们把学习率设为 2e-5、批量大小设为 16，在一块显存 80G 的 A100 GPU 上微调 10k 步。对于 LoRA 模块，我们把低秩设为 128、alpha 设为 256。由于我们的分析文本不包含任何可用于识别画作的信息，LMM 无法检索习得的知识来与画作关联；相反，在 SFT 优化下，LMM 会努力感知画作中呈现的细微要素与艺术技法，并将其与形式分析中相应的描述相匹配。通过这样的微调，我们的 GalleryGPT 可获得艺术品分析能力，并能泛化到风格分类等其他艺术分析任务。

**EN** 5. Experiments

**ZH** 5. 实验

**EN** 5.1. Formal Analysis Generation

**ZH** 5.1. 形式分析生成

**EN** Since our data and optimization goal are for painting formal analysis generation, we first directly evaluate the quality of generated formal analyses on our reserved test set, with 5000 paintings. We also test with several popular and powerful open-source LMMs, including LLaVA-1.5 (Liu et al., 2024), Qwen-VL-Chat (Bai et al., 2023), and ShareGPT4V77 7 Here we implement 7B model for fair comparison for all baseline and omit 7B in the table. Note that in (Chen et al., 2023a), ShareGPT4V indicates the dataset and ShareGPT4V-7B is the model, but in this table we omit 7B for unifying all the model names. (Chen et al., 2023a), and all the LLMs employ the same prompt: “Please compose a coherent paragraph of formal analysis focusing on visual characteristics”. We combine the formal analyses annotated by GPT-4 and Gemini for each painting to formulate the ground truth descriptions. Finally, we employ image captioning metrics to evaluate the generated formal analyses because formal analysis is also a kind of description. As the evaluation results shown in Table 1, we observe that our GalleryGPT outperforms all the other LMMs with a remarkable improvement. Among all the baseline LLMs, LLaVA-1.5 performs the worst and is significantly lower than others, while Qwen-VL and ShareGPT4V achieve similar performance. From these observations, we can conclude that, benefiting from the SFT with PaintingForm, the GalleryGPT achieves impressive improvements comparing with ShareGPT4V-7B, which mainly focuses on natural image-text pairs (only a few art data). This verifies the effectiveness of our high quality art analysis data collections.

**ZH** 由于我们的数据与优化目标面向绘画形式分析生成，我们首先在保留的测试集（5000 幅画作）上直接评估所生成形式分析的质量。我们也测试了若干流行且强大的开源 LMM，包括 LLaVA-1.5（Liu 等，2024）、Qwen-VL-Chat（Bai 等，2023）与 ShareGPT4V（脚注 7：此处为实现公平比较，所有基线均采用 7B 模型，并在表中省略 7B。注意在（Chen 等，2023a）中 ShareGPT4V 指数据集、ShareGPT4V-7B 指模型，但本表中为统一所有模型名称而省略 7B。）（Chen 等，2023a），所有模型使用相同的提示：“请撰写一段连贯的形式分析，聚焦于视觉特征”。我们把每幅画作由 GPT-4 与 Gemini 标注的形式分析合并，构成真值描述。最后，我们采用图像描述指标来评估生成的形式分析，因为形式分析本身也是一种描述。如表 1 的评估结果所示，我们的 GalleryGPT 以显著优势超过所有其他 LMM。在所有基线模型中，LLaVA-1.5 表现最差，明显低于其他模型；而 Qwen-VL 与 ShareGPT4V 表现相近。从这些观察可以得出结论：得益于用 PaintingForm 做 SFT，GalleryGPT 相比主要面向自然图文对（仅含少量艺术数据）的 ShareGPT4V-7B 取得了令人印象深刻的提升，这验证了我们高质量艺术分析数据收集的有效性。

**EN** Table 1. Performance comparison of formal analysis generation measured by the captioning metrics, evaluated on our test set with 5000 paintings.

**ZH** 表 1. 以描述指标衡量的形式分析生成性能比较，在包含 5000 幅画作的测试集上评估。

<!-- [原子块 · table] Model BLEU GLEU METEOR ROUGE LLaVA-1.5 ( Liu et al., 2024 ) 9.87 14.59 26.19 26.37 Qwen-VL-Chat ( Bai et al., 2023 ) 13.65 16.42 29.78 26.72 ShareGPT4V ( Chen et al., 2023a ) 12.38 16.14 31.53 26.63 G -->

**EN** Table 2. Zero-shot performance comparison on several artwork analysis tasks, including question answering and classification. SoTA-1 and SoTA-2 denote previous state of the arts without and with PLM (including fine-tuning on corresponding datasets). Both SoTA-1 and SoTA-2 denote different methods for different tasks.

**ZH** 表 2. 在若干艺术品分析任务（含问答与分类）上的零样本性能比较。SoTA-1 与 SoTA-2 分别表示未使用与使用预训练语言模型（PLM）（含在相应数据集上微调）的既往最先进方法。SoTA-1 与 SoTA-2 在不同任务上指代不同的方法。

<!-- [原子块 · table] Model AQUA ArtQuest ArtQuest-Type ArtBench SoTA-1 22.40 2.40 - - SoTA-2 55.50 50.2 81.8 - LLaVA-1.5 22.13 8.66 34.82 28.1 Qwen-VL-Chat 18.67 7.86 26.29 28.0 ShareGPT4V 23.62 7.91 38.07 31.7 GalleryGPT -->

<!-- [原子块 · img]  -->

**EN** Figure 5. An example for qualitative comparison of formal analysis generation by several powerful LMMs. Purple texts denote the factual content description, and the Blue texts are for formal analysis. The formal analysis generated by our GalleryGPT covers more visual elements, e.g., color, light and shadow, depth, composition, and perspective, than other LLMs, even the powerful GPT-4V.

**ZH** 图 5. 若干强大 LMM 的形式分析生成定性比较示例。紫色文字表示事实性内容描述，蓝色文字表示形式分析。我们的 GalleryGPT 生成的形式分析比其他 LLM（甚至是强大的 GPT-4V）覆盖更多视觉要素，例如色彩、光影、纵深、构图与透视。

**EN** 5.2. Generalizing to Other Art Analysis Tasks

**ZH** 5.2. 泛化到其他艺术分析任务

**EN** LLMs and LMMs have demonstrated superior generalizing ability to many downstream tasks. To verify the generalization of our GalleryGPT, we conduct visual question answering and style classification for paintings on several existing datasets. The details of the dataset are as following:

**ZH** LLM 与 LMM 已展现出对众多下游任务的优越泛化能力。为验证 GalleryGPT 的泛化性，我们在若干现有数据集上做绘画的视觉问答与风格分类。数据集详情如下：

**EN** • AQUA (Garcia et al., 2020): is an Art Question Answering dataset based on SemArt (Garcia and Vogiatzis, 2018). The question-answer pairs are generated by powerful question generation models based on paintings and comments provided in SemArt. The dataset contains 29,568, 1,507, and 1,270 samples in training, validation, and test splits, respectively.

**ZH** • AQUA（Garcia 等，2020）：是一个基于 SemArt（Garcia 和 Vogiatzis，2018）的艺术问答数据集。问答对由强大的问题生成模型基于 SemArt 中提供的画作与评论生成。该数据集的训练、验证与测试划分分别包含 29,568、1,507 与 1,270 个样本。

**EN** • ArtQuest (Bleidt et al., 2024): is the debiased version of AQUA, including 6414 test cases, which mainly focuses on eliminating the bias hidden in language. With such debias operation, most question cannot be answered without visual content.

**ZH** • ArtQuest（Bleidt 等，2024）：是 AQUA 的去偏版本，包含 6414 条测试用例，主要致力于消除语言中隐藏的偏置。经此去偏操作后，大多数问题在没有视觉内容的情况下无法作答。

**EN** • ArtQuest-Type (Bleidt et al., 2024): is simple setting of ArtQuest, which requires the model only answer the type of the painting. The test set contains 1069 samples.

**ZH** • ArtQuest-Type（Bleidt 等，2024）：是 ArtQuest 的简化设定，要求模型只回答画作的类型。测试集包含 1069 个样本。

**EN** • ArtBench (Liao et al., 2022): is originally for Artwork generation. We random sample 1000 paintings from the test set (10000 paintings in total), and use the provided style labels for classification.

**ZH** • ArtBench（Liao 等，2022）：原本用于艺术品生成。我们从测试集（共 10000 幅画作）中随机采样 1000 幅画作，并使用其提供的风格标签做分类。

**EN** We exhibit the results in Table 2, from which we can see that our GalleryGPT also significantly outperforms all the baseline LMMs and demonstrates its generalizing ability for downstream art analysis tasks. An interesting observation is that LLaVA-1.5 performs much better than Qwen-VL-Chat, showing an opposite result to the task of formal analysis generation. We have checked and analyzed the results, and hypothesize that may come from the output format mismatching. Since all the three QA datasets follow the open-ended answering setting, and then extract the matching strings from the outputs. Another piece of evidence is that Qwen-VL-Chat achieves similar performance to LLaVA-1.5 when the output strictly adheres to the given labels.

**ZH** 我们在表 2 中展示结果，可以看到我们的 GalleryGPT 同样显著优于所有基线 LMM，展现出其在下游艺术分析任务上的泛化能力。一个有趣的观察是，LLaVA-1.5 的表现远好于 Qwen-VL-Chat，这与形式分析生成任务上的结果相反。我们核查并分析了结果，推测这可能源于输出格式不匹配：三个问答数据集都采用开放式作答设定，再从输出中抽取匹配字符串。另一个佐证是，当输出严格遵循给定标签时，Qwen-VL-Chat 能达到与 LLaVA-1.5 相近的性能。

**EN** To comprehensively analyze the ability of our GalleryGPT, we also compare it with several state of the arts and show the results in the top block in Table 2, which are specific trained on the corresponding datasets. SoTA-1 denotes the models without pre-training language model (PLM), e.g., BERT, and SoTA-2 denotes the models leveraging PLM features or fine-tuning based on PLMs. From the results we can see, almost all the current LMMs only achieve the performance around SoTA-1 on AQUA, i.e., specifically training on this dataset, while they can significantly outperform SoTA-1 on ArtQuest. This reason may come from the language bias hidden in AQUA dataset (Bleidt et al., 2024). For all the dataset, the performances of LMMs are far from the SoTA-2, which means the generalization ability of LMMs on art analysis is still weak and there exists a large space for them to get improved. Our hypothesis on such results is that artworks may contain high-level and abstract concepts to be perceived more subtly, which also motivates us to make further endeavour on this in the future work.

**ZH** 为全面分析 GalleryGPT 的能力，我们还将其与若干最先进方法比较，结果见表 2 顶部区块——这些方法是在相应数据集上专门训练的。SoTA-1 表示未使用预训练语言模型（PLM）（如 BERT）的模型，SoTA-2 表示利用 PLM 特征或在 PLM 基础上微调的模型。从结果可以看到，当前几乎所有 LMM 在 AQUA 上只达到 SoTA-1（即在该数据集上专门训练）左右的性能，而在 ArtQuest 上则能显著超过 SoTA-1。原因可能来自 AQUA 数据集中潜藏的语言偏置（Bleidt 等，2024）。在所有数据集上，LMM 的性能都远不及 SoTA-2，这意味着 LMM 在艺术分析上的泛化能力仍然较弱，还有很大提升空间。我们对这些结果的假设是：艺术品可能包含需要更细腻感知的高层抽象概念，这也激励我们在未来工作中继续投入。

**EN** 5.3. Multimodal Benchmarks

**ZH** 5.3. 多模态基准

**EN** Since GalleryGPT is implemented based on ShareGPT4V-7B, it inherently remains an LMM. Therefore, we also conduct experiments on several LLM benchmarks and compare it with baseline LLMs88 8 Instead of listing all the baselines in (Chen et al., 2023a), here we only list the superior and representative ones for comparison. to evaluate the multimodal understanding ability. As the comparison results illustrated in Table 3, we can see our GalleryGPT exhibits comparable performance with ShareGPT4V, i.e., achieving improvements and reducements in slight fluctuations. In other words, our GalleryGPT, further fine-tuned with elaborately collected painting-analysis pairs, not only achieves better painting analysis performance, including formal analysis generation (Table 1) and other downstream tasks (Table 2), and also retains its superior multimodal understanding ability. These observations further verify the effectiveness and contributions of our collected PaintingForm and developed GalleryGPT.

**ZH** 由于 GalleryGPT 基于 ShareGPT4V-7B 实现，它本质上仍是一个 LMM。因此，我们也在若干 LLM 基准上做实验，并与基线 LMM（脚注 8：我们没有列出（Chen 等，2023a）中的所有基线，此处只列出优秀且具有代表性者用于比较。）比较，以评估其多模态理解能力。如表 3 的比较结果所示，我们的 GalleryGPT 与 ShareGPT4V 表现相当，即在小幅波动中既有提升也有下降。换言之，我们的 GalleryGPT 经精心收集的绘画—分析配对进一步微调后，不仅取得了更好的绘画分析性能（包括形式分析生成（表 1）与其他下游任务（表 2）），也保留了其优越的多模态理解能力。这些观察进一步验证了所收集 PaintingForm 与所开发 GalleryGPT 的有效性与贡献。

**EN** Table 3. Comparisons with powerful baselines on several LMM Benchmarks. The best and 2nd-best results are in bold and underlined, respectively. All the results of baselines are referred from (Chen et al., 2023a).

**ZH** 表 3. 在若干 LMM 基准上与强大基线的比较。最优与次优结果分别以粗体与下划线标出。所有基线结果均引自（Chen 等，2023a）。

<!-- [原子块 · table] Model MMB LLaVA-W MM-Vet SQA LLaVA-1.5 64.3 63.4 30.5 66.8 Qwen-VL-Chat 60.6 - - 68.2 ShareGPT4V 68.8 72.6 37.6 68.4 GalleryGPT (ours) 70.8 69.9 35.5 69.1 -->

<!-- [原子块 · img]  -->

**EN** Figure 6. Multimodal dialogue examples with our GalleryGPT. Blue texts denote high quality formal analysis. We also test dialoguing in Chinese, even we do not fine-tune GalleryGPT with Chinese painting-analysis pairs. The English translation of Chinese conversation can be found in Supplementary.

**ZH** 图 6. 与我们的 GalleryGPT 的多模态对话示例。蓝色文字表示高质量的形式分析。我们还测试了用中文对话，尽管我们并未用中文绘画—分析配对微调 GalleryGPT。该中文对话的英文翻译见补充材料。

**EN** 5.4. Qualitative Analyses

**ZH** 5.4. 定性分析

**EN** To visually and straightforwardly compare our GalleryGPT with other LMMs, inncluding LLaVA-1.5, ShareGPT4V-7B, and GPT-4V, we test some unpopular paintings in our test split. As illustrated in Figure 5, we observe that LLaVA tends to describe the factual content (in purple color) presented in the painting, and fails to analyze the paintings from the perspective of art criticism. ShareGPT4V-7B, the backbone of our model, also pays more attention on the content description, because the SFT data it utilized for fine-tuning is focusing on describing the images in detail. Thanks to the small subset of art data in ShareGPT4V, it also exhibits some capacity for art analysis, albeit limited to general analyses and overlooking the subtle visual characteristics. GPT4V, as the most famous and capable LMM at current stage, demonstrates much better analyzing ability on paintings in terms of their form, while still fails to capture some subtle artistic aspects, such as composition and depth. Obviously, our GalleryGPT demonstrates superb capability of comprehensively analyzing the artworks, which not only briefly describe the factual content of the painting, but also focuses more attention on analyzing the subtle artistic elements, including color, light and shadow, depth, composition, and perspective. These observations have definitely verified the superiority of our GalleryGPT for artwork analyzing.

**ZH** 为直观、直接地把 GalleryGPT 与其他 LMM（包括 LLaVA-1.5、ShareGPT4V-7B 与 GPT-4V）做比较，我们在测试划分中选取了一些不太知名的画作进行测试。如图 5 所示，我们观察到 LLaVA 倾向于描述画作中呈现的事实性内容（紫色部分），未能从艺术批评的视角分析画作。作为本模型骨干的 ShareGPT4V-7B 也更偏重内容描述，因为其微调所用的 SFT 数据聚焦于详细描述图像；得益于 ShareGPT4V 中少量艺术数据，它也展现出一定的艺术分析能力，但仅限于泛泛而谈、忽略了细微的视觉特征。GPT-4V 作为当前最著名、能力最强的 LMM，在画作的形式分析上表现出明显更好的能力，但仍未能捕捉构图、纵深等某些细微的艺术面向。显然，我们的 GalleryGPT 展现出全面分析艺术品的出色能力：既简要描述画作的事实性内容，又把更多注意力放在分析色彩、光影、纵深、构图与透视等细微的艺术要素上。这些观察充分验证了 GalleryGPT 在艺术品分析上的优越性。

**EN** We also investigate the dialogue capability of our GalleryGPT. We show several dialogue examples in Figure 6. The examples demonstrate that our GalleryGPT is able to follow the user intention in the conversation. As shown in the second case, for instance, we ask it to give “essential aspects” for formal analysis, it just provides us a brief analysis with essential content, which is much shorter than the one provided in Figure 5. Besides, we further explore the multilingual capabilities of GalleryGPT, even though we have not provided any multilingual painting analyses for supervised fine-tuning99 9 Actually, the foundation models, LLaMA and LLaVA, are pre-trained and fine-tuned with several multilingual corpuses.. As shown at the bottom in Figure 6, we chat with GalleryGPT in Chinese1010 10 A reviewer pointed out that the “前途” and “后途” are typos and should be “前景” and “后景”, since this analysis is generated by our GalleryGPT and we have not modified it. As the English translation in Figure. 6 in Supplementary, the meanings are the same with the suggestions of the reviewer. We sincerely appreciate the reviewer providing such careful and helpful comments and suggestions., it still generates high quality answer focusing on “composition” and exhibits strong multilingual ability.

**ZH** 我们还考察了 GalleryGPT 的对话能力，并在图 6 中给出若干对话示例。这些示例表明 GalleryGPT 能够遵循用户在对话中的意图。例如第二个案例中，我们要求它给出形式分析的“关键面向”，它就提供了一段内容精炼的简短分析，远短于图 5 中的那一段。此外，我们进一步探索了 GalleryGPT 的多语言能力，尽管我们并未为监督微调提供任何多语言的绘画分析（脚注 9：实际上，基础模型 LLaMA 与 LLaVA 在预训练与微调时使用了若干多语语料。）。如图 6 底部所示，我们用中文与 GalleryGPT 交谈（脚注 10：一位审稿人指出“前途”与“后途”是错别字，应为“前景”与“后景”；由于该分析由我们的 GalleryGPT 生成且我们未作修改，而补充材料图 6 中的英文翻译与审稿人的建议含义一致。我们衷心感谢审稿人提出如此细致而有益的意见与建议。），它仍能生成聚焦“构图”的高质量回答，展现出较强的多语言能力。

**EN** In summary, these qualitative comparisons and dialogue examples have verified the superior art analysis ability of our GalleryGPT, as well as illustrating the quality of our PaintingForm dataset. For more examples of this part, qualitative comparison and chat conversation, could be found in Supplementary.

**ZH** 总之，这些定性比较与对话示例验证了 GalleryGPT 卓越的艺术分析能力，也说明了 PaintingForm 数据集的质量。本部分更多示例、定性比较与对话内容见补充材料。

**EN** 6. Conclusions and Future Works

**ZH** 6. 结论与未来工作

**EN** In this work, we targeted at artwork analyzing with large multimodal models (LLMs). We first tested several LLMs and pointed out that current LLMs may suffering from “LLM-biased visual hallucination” issue, resulting in weak generalization ability to nameless paintings. To make the LMMs to analyze artworks focusing on visual elements and easy to generalize, we proposed to conduct SFT of LMMs with formal analysis. To support this research, we first elaborately designed an LLM-based data collection pipeline to construct high quality painting-analysis pairs. We also employed ShareGPT4V to implement SFT on the collected data, derived our GalleryGPT. We conducted extensive experiments to verify the effectiveness regarding to formal analysis generation, generalizing to down stream tasks, and LMM benchmarking. The results demonstrated the effectiveness of the collected data and introduced GalleryGPT.

**ZH** 本工作以大多模态模型（LLM）进行艺术品分析为目标。我们首先测试了若干 LLM，指出现有 LLM 可能存在“LLM 偏置的视觉幻觉”问题，导致其对无名画作的泛化能力较弱。为使 LMM 聚焦于视觉要素来分析艺术品并易于泛化，我们提出用形式分析对 LMM 做 SFT。为支撑该研究，我们首先精心设计了一条基于 LLM 的数据采集管线，用以构建高质量的绘画—分析配对；并采用 ShareGPT4V 在所收集数据上实施 SFT，得到我们的 GalleryGPT。我们开展了大量实验，从形式分析生成、泛化到下游任务以及 LMM 基准测试三方面验证有效性，结果证明了所收集数据与所提出 GalleryGPT 的有效性。

**EN** For future works, on one hand, we will step further to investigate the generalization issue mentioned in Section 5.2 to explore the ability of LMMs in art analyzing. For example, devising a ChatGPT-like art assistant to help more people appreciate or learn to appreciate artworks. On the other hand, we only collect paintings in this work, while artworks consist of multiple types, e.g., ceramics (paintings on a curved surface) and sculptural in 3D. Therefore, we will try to make the research more widely and empower LMMs to assist human in artwork analyzing, e.g., drafting formal analysis, classifying the unseen artworks, etc. We also hope that our work can inspire more researchers to explore AI, especially for LMMs, within the field of art analysis.

**ZH** 在未来工作中，一方面我们将进一步研究 5.2 节提到的泛化问题，探索 LMM 在艺术分析中的能力，例如打造一个类似 ChatGPT 的艺术助手，帮助更多人欣赏或学会欣赏艺术品。另一方面，本工作只收集了绘画，而艺术品包含多种类型，例如瓷器（曲面上的绘画）与三维雕塑。因此，我们将努力把研究拓展得更广，使 LMM 能辅助人类进行艺术品分析，例如起草形式分析、对未见过的艺术品分类等。我们也希望本工作能激励更多研究者探索艺术分析领域中的 AI，尤其是 LMM。

**EN** Acknowledgements.

**ZH** 致谢。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] Bahdanau et al . (2014) Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Bengio. 2014. Neural machine translation by jointly learning to align and translate. arXiv preprint arXiv:1409.0473 (2014). -->

<!-- [原子块 · verbatim] Bai et al . (2023) Jinze Bai, Shuai Bai, Shusheng Yang, Shijie Wang, Sinan Tan, Peng Wang, Junyang Lin, Chang Zhou, and Jingren Zhou. 2023. Qwen-vl: A versatile vision-language model for understanding -->

<!-- [原子块 · verbatim] Bin et al . (2021) Yi Bin, Xindi Shang, Bo Peng, Yujuan Ding, and Tat-Seng Chua. 2021. Multi-perspective video captioning. In Proceedings of the 29th ACM International Conference on Multimedia . 5110– -->

<!-- [原子块 · verbatim] Bin et al . (2022) Yi Bin, Wenhao Shi, Jipeng Zhang, Yujuan Ding, Yang Yang, and Heng Tao Shen. 2022. Non-autoregressive cross-modal coherence modelling. In Proceedings of the 30th ACM International C -->

<!-- [原子块 · verbatim] Bleidt et al . (2024) Tibor Bleidt, Sedigheh Eslami, and Gerard de Melo. 2024. ArtQuest: Countering Hidden Language Biases in ArtVQA. In Proceedings of the IEEE/CVF Winter Conference on Applications o -->

<!-- [原子块 · verbatim] Brown et al . (2020) Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al . 2020. Language mo -->

<!-- [原子块 · verbatim] Carneiro et al . (2012) Gustavo Carneiro, Nuno Pinho Da Silva, Alessio Del Bue, and João Paulo Costeira. 2012. Artistic image classification: An analysis on the printart database. In Computer Vision–E -->

<!-- [原子块 · verbatim] Chen et al . (2023c) Jun Chen, Deyao Zhu, Xiaoqian Shen, Xiang Li, Zechun Liu, Pengchuan Zhang, Raghuraman Krishnamoorthi, Vikas Chandra, Yunyang Xiong, and Mohamed Elhoseiny. 2023c. Minigpt-v2: large -->

<!-- [原子块 · verbatim] Chen et al . (2023b) Keqin Chen, Zhao Zhang, Weili Zeng, Richong Zhang, Feng Zhu, and Rui Zhao. 2023b. Shikra: Unleashing Multimodal LLM’s Referential Dialogue Magic. arXiv preprint arXiv:2306.15195 ( -->

<!-- [原子块 · verbatim] Chen et al . (2023a) Lin Chen, Jisong Li, Xiaoyi Dong, Pan Zhang, Conghui He, Jiaqi Wang, Feng Zhao, and Dahua Lin. 2023a. Sharegpt4v: Improving large multi-modal models with better captions. arXiv pr -->

<!-- [原子块 · verbatim] Chowdhery et al . (2023) Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung, Charles Sutton, Sebastian Gehrmann, et al . 2023. P -->

<!-- [原子块 · verbatim] Conde and Turgutlu (2021) Marcos V Conde and Kerem Turgutlu. 2021. CLIP-Art: Contrastive pre-training for fine-grained art classification. In Proceedings of the IEEE/CVF Conference on Computer Vision  -->

<!-- [原子块 · verbatim] Dai et al . (2024) Wenliang Dai, Junnan Li, Dongxu Li, Anthony Meng Huat Tiong, Junqi Zhao, Weisheng Wang, Boyang Li, Pascale N Fung, and Steven Hoi. 2024. Instructblip: Towards general-purpose vision -->

<!-- [原子块 · verbatim] Devlin et al . (2018) Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2018. Bert: Pre-training of deep bidirectional transformers for language understanding. arXiv preprint arXiv:181 -->

<!-- [原子块 · verbatim] Ding et al . (2024a) Yujuan Ding, Wenqi Fan, Liangbo Ning, Shijie Wang, Hengyun Li, Dawei Yin, Tat-Seng Chua, and Qing Li. 2024a. A survey on rag meets llms: Towards retrieval-augmented large language -->

<!-- [原子块 · verbatim] Ding et al . (2024b) Yujuan Ding, Yunshan Ma, Wenqi Fan, Yige Yao, Tat-Seng Chua, and Qing Li. 2024b. Fashionregen: Llm-empowered fashion report generation. In Companion Proceedings of the ACM on Web  -->

<!-- [原子块 · verbatim] Dosovitskiy et al . (2020) Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, -->

<!-- [原子块 · verbatim] Garcia and Vogiatzis (2018) Noa Garcia and George Vogiatzis. 2018. How to read paintings: semantic art understanding with multi-modal retrieval. In Proceedings of the European Conference on Computer V -->

<!-- [原子块 · verbatim] Garcia et al . (2020) Noa Garcia, Chentao Ye, Zihua Liu, Qingtao Hu, Mayu Otani, Chenhui Chu, Yuta Nakashima, and Teruko Mitamura. 2020. A dataset and baselines for visual question answering on art. I -->

<!-- [原子块 · verbatim] Gatys et al . (2016) Leon Gatys, Alexander Ecker, and Matthias Bethge. 2016. A Neural Algorithm of Artistic Style. Journal of Vision 16, 12 (2016), 326–326. -->

<!-- [原子块 · verbatim] Hochreiter and Schmidhuber (1997) Sepp Hochreiter and Jürgen Schmidhuber. 1997. Long short-term memory. Neural computation 9, 8 (1997), 1735–1780. -->

<!-- [原子块 · verbatim] Hu et al . (2021) Edward J Hu, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, Weizhu Chen, et al . 2021. LoRA: Low-Rank Adaptation of Large Language Models. In International Confer -->

<!-- [原子块 · verbatim] Huang et al . (2016) Ting-Hao Huang, Francis Ferraro, Nasrin Mostafazadeh, Ishan Misra, Aishwarya Agrawal, Jacob Devlin, Ross Girshick, Xiaodong He, Pushmeet Kohli, Dhruv Batra, et al . 2016. Visual s -->

<!-- [原子块 · verbatim] Inc (2023a) Google Inc. 2023a. Gemini. https://gemini.google.com [Accessed: 4 Feb, 2024]. -->

<!-- [原子块 · verbatim] Inc (2022) OpenAI Inc. 2022. ChatGPT. https://chat.openai.com [Accessed: 4 Feb, 2024]. -->

<!-- [原子块 · verbatim] Inc (2023b) OpenAI Inc. 2023b. GPT-4V(ision). https://openai.com/research/gpt-4v-system-card [Accessed: 4 Feb, 2024]. -->

<!-- [原子块 · verbatim] Jia et al . (2014) Yangqing Jia, Evan Shelhamer, Jeff Donahue, Sergey Karayev, Jonathan Long, Ross Girshick, Sergio Guadarrama, and Trevor Darrell. 2014. Caffe: Convolutional architecture for fast fea -->

<!-- [原子块 · verbatim] Johnson et al . (2008) C Richard Johnson, Ella Hendriks, Igor J Berezhnoy, Eugene Brevdo, Shannon M Hughes, Ingrid Daubechies, Jia Li, Eric Postma, and James Z Wang. 2008. Image processing for artist  -->

<!-- [原子块 · verbatim] Kenton and Toutanova (2019) Jacob Devlin Ming-Wei Chang Kenton and Lee Kristina Toutanova. 2019. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. In Proceedings of NAA -->

<!-- [原子块 · verbatim] Khan et al . (2014) Fahad Shahbaz Khan, Shida Beigpour, Joost Van de Weijer, and Michael Felsberg. 2014. Painting-91: a large scale database for computational painting categorization. Machine vision a -->

<!-- [原子块 · verbatim] Krizhevsky et al . (2012) Alex Krizhevsky, Ilya Sutskever, and Geoffrey E Hinton. 2012. Imagenet classification with deep convolutional neural networks. Advances in neural information processing syste -->

<!-- [原子块 · verbatim] Lewis et al . (2019) Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer Levy, Ves Stoyanov, and Luke Zettlemoyer. 2019. Bart: Denoising sequence-to-sequence pre-train -->

<!-- [原子块 · verbatim] Li et al . (2023) Junnan Li, Dongxu Li, Silvio Savarese, and Steven Hoi. 2023. Blip-2: Bootstrapping language-image pre-training with frozen image encoders and large language models. In International  -->

<!-- [原子块 · verbatim] Li et al . (2022) Junnan Li, Dongxu Li, Caiming Xiong, and Steven Hoi. 2022. Blip: Bootstrapping language-image pre-training for unified vision-language understanding and generation. In International  -->

<!-- [原子块 · verbatim] Li et al . (2020) Xiujun Li, Xi Yin, Chunyuan Li, Pengchuan Zhang, Xiaowei Hu, Lei Zhang, Lijuan Wang, Houdong Hu, Li Dong, Furu Wei, et al . 2020. Oscar: Object-semantics aligned pre-training for vis -->

<!-- [原子块 · verbatim] Liao et al . (2022) Peiyuan Liao, Xiuyu Li, Xihui Liu, and Kurt Keutzer. 2022. The artbench dataset: Benchmarking generative models with artworks. arXiv preprint arXiv:2206.11404 (2022). -->

<!-- [原子块 · verbatim] Liu et al . (2023) Fang Liu, Mohan Zhang, Baoying Zheng, Shenglan Cui, Wentao Ma, and Zhixiong Liu. 2023. Feature fusion via multi-target learning for ancient artwork captioning. Information Fusion 97 -->

<!-- [原子块 · verbatim] Liu et al . (2024) Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. 2024. Visual instruction tuning. Advances in neural information processing systems 36 (2024). -->

<!-- [原子块 · verbatim] Liu et al . (2019) Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov. 2019. Roberta: A robustly optimized bert pret -->

<!-- [原子块 · verbatim] Nguyen et al . (2024) Thong Nguyen, Yi Bin, Junbin Xiao, Leigang Qu, Yicong Li, Jay Zhangjie Wu, Cong-Duy Nguyen, See-Kiong Ng, and Luu Anh Tuan. 2024. Video-Language Understanding: A Survey from Mode -->

<!-- [原子块 · verbatim] Ouyang et al . (2022) Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al . 2022. Training language mod -->

<!-- [原子块 · verbatim] Peng et al . (2023) Zhiliang Peng, Wenhui Wang, Li Dong, Yaru Hao, Shaohan Huang, Shuming Ma, and Furu Wei. 2023. Kosmos-2: Grounding multimodal large language models to the world. arXiv preprint arXi -->

<!-- [原子块 · verbatim] Pennington et al . (2014) Jeffrey Pennington, Richard Socher, and Christopher D Manning. 2014. Glove: Global vectors for word representation. In Proceedings of the 2014 conference on empirical methods -->

<!-- [原子块 · verbatim] Radford et al . (2021) Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, et al . 2021. Learning transf -->

<!-- [原子块 · verbatim] Radford et al . (2018) Alec Radford, Karthik Narasimhan, Tim Salimans, Ilya Sutskever, et al . 2018. Improving language understanding by generative pre-training. (2018). -->

<!-- [原子块 · verbatim] Radford et al . (2019) Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, Ilya Sutskever, et al . 2019. Language models are unsupervised multitask learners. OpenAI blog 1, 8 (2019), 9. -->

<!-- [原子块 · verbatim] Raffel et al . (2020) Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter J Liu. 2020. Exploring the limits of transfer learning with  -->

<!-- [原子块 · verbatim] Shamir et al . (2010) Lior Shamir, Tomasz Macura, Nikita Orlov, D Mark Eckley, and Ilya G Goldberg. 2010. Impressionism, expressionism, surrealism: Automated recognition of painters and schools of art -->

<!-- [原子块 · verbatim] Sheng and Moens (2019) Shurong Sheng and Marie-Francine Moens. 2019. Generating captions for images of ancient artworks. In Proceedings of the 27th ACM international conference on multimedia . 2478–24 -->

<!-- [原子块 · verbatim] Shi et al . (2024) Wenhao Shi, Zhiqiang Hu, Yi Bin, Junhua Liu, Yang Yang, See-Kiong Ng, Lidong Bing, and Roy Ka-Wei Lee. 2024. Math-LLaVA: Bootstrapping Mathematical Reasoning for Multimodal Large La -->

<!-- [原子块 · verbatim] Team (2023) The Vicuna Team. 2023. Vicuna: An open-source chatbot impressing gpt-4 with 90%* chatgpt quality. https://lmsys.org/blog/2023-03-30-vicuna [Accessed: 4 Feb, 2024]. -->

<!-- [原子块 · verbatim] Thoppilan et al . (2022) Romal Thoppilan, Daniel De Freitas, Jamie Hall, Noam Shazeer, Apoorv Kulshreshtha, Heng-Tze Cheng, Alicia Jin, Taylor Bos, Leslie Baker, Yu Du, et al . 2022. Lamda: Language m -->

<!-- [原子块 · verbatim] Touvron et al . (2023a) Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al . 2023a. Llama -->

<!-- [原子块 · verbatim] Touvron et al . (2023b) Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al . 2023b. Llama -->

<!-- [原子块 · verbatim] Vaswani et al . (2017) Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, and Illia Polosukhin. 2017. Attention is all you need. Advances in neural  -->

<!-- [原子块 · verbatim] Yang et al . (2023) Aiyuan Yang, Bin Xiao, Bingning Wang, Borong Zhang, Ce Bian, Chao Yin, Chenxu Lv, Da Pan, Dian Wang, Dong Yan, et al . 2023. Baichuan 2: Open large-scale language models. arXiv pre -->

<!-- [原子块 · verbatim] Yang et al . (2019) Zhilin Yang, Zihang Dai, Yiming Yang, Jaime Carbonell, Russ R Salakhutdinov, and Quoc V Le. 2019. Xlnet: Generalized autoregressive pretraining for language understanding. Advances -->

<!-- [原子块 · verbatim] Ye et al . (2023) Qinghao Ye, Haiyang Xu, Guohai Xu, Jiabo Ye, Ming Yan, Yiyang Zhou, Junyang Wang, Anwen Hu, Pengcheng Shi, Yaya Shi, et al . 2023. mplug-owl: Modularization empowers large language m -->

**EN** Appendix A Introduction

**ZH** 附录 A 引言

**EN** Due to the page limit, we omit some details in the main paper, e.g., the detail prompts for data collection, and only illustrate one example for some parts. In this supplementary materials, we will first give the prompting details and then illustrate more examples to make the qualitative analysis more comprehensive and convincing.

**ZH** 受篇幅限制，我们在正文中省略了部分细节（例如数据采集所用的详细提示），部分内容只给出了一个示例。在本补充材料中，我们将首先给出提示的细节，然后展示更多示例，以使定性分析更加全面、更具说服力。

**EN** Appendix B Detail Prompts for Data Collection

**ZH** 附录 B 数据采集的详细提示

**EN** As described in Section 3.1 and the pipeline shown in Figure 2, our formal analysis annotation process consists of three stages: 1) verifying if the LLMs know the painting, 2) extracting essential elements presented in the painting, and 3) generating a paragraph formal analysis for each painting. For each stage, we use different instructions to prompt the LLMs. Limited by the space, we omit the details prompts in the main part, and illustrate them here for details. For the third stage, we ask the LLMs to annotate two kinds of formal analysis: overall formal analysis (prompt for stage 3-1) and specified aspect formal analysis (prompt for stage 3-2).

**ZH** 如 3.1 节所述以及图 2 所示管线，我们的形式分析标注过程包含三个阶段：1）验证 LLM 是否知道该画作；2）提取画作中呈现的关键要素；3）为每幅画作生成一段形式分析。每个阶段我们使用不同的指令来提示 LLM。受篇幅限制，正文省略了详细的提示，此处逐一给出。在第三阶段，我们要求 LLM 标注两类形式分析：整体形式分析（阶段 3-1 的提示）与指定面向的形式分析（阶段 3-2 的提示）。

**EN** Prompt for Stage 1: You are a professional art critic. Do you know the painting titled [Painting Title] by [Artist Name]? Respond with only ’YES’ or ’NO’.

**ZH** 阶段 1 的提示：你是一位专业的艺术评论家。你是否知道由［艺术家姓名］创作的题为［画作标题］的画作？请只回答“是”或“否”。

**EN** Prompt for Stage 2: You are a professional art critic. Please select up to five essential aspects for the formal analysis of the [Painting Title] by [Artist Name] from the provided list. You may choose fewer if preferred. The list is: ["Composition", "Color Palette", "Line Quality", "Texture", "Light and Shadow", "Perspective", "Form and Shape", "Movement and Gesture", "Symbolism and Iconography", "Scale and Proportion"]. Please list the aspects in descending order of importance in a LIST. Your output should be in the format: "The essential aspects are: [YOUR SELECTED CHARACTERISTICS].

**ZH** 阶段 2 的提示：你是一位专业的艺术评论家。请从下列清单中为［艺术家姓名］的《［画作标题］》的形式分析选取至多五个关键面向，也可以少选。清单为：［“构图”、“配色”、“线条质量”、“质感”、“光影”、“透视”、“形态与形状”、“动态与姿态”、“象征与图像志”、“尺度与比例”］。请以列表形式按重要性降序列出这些面向。输出格式为：“关键面向为：［你所选择的特征］。”

**EN** Prompt for Stage 3-1: Overall formal analysis annotation: You are a professional art critic. Please compose a coherent paragraph, approximately [Number of Words] words, providing a professional formal analysis of the [Painting Title] by [Artist Name] ONLY focusing on the VISUAL CHARACTERISTICS of this painting. DO NOT mention the painting title and artist’s name in your analysis. You may use conjunctions as needed to ensure coherence in semantics and logic in your analysis.

**ZH** 阶段 3-1 的提示：整体形式分析标注：你是一位专业的艺术评论家。请撰写一段约［词数］词的连贯段落，对［艺术家姓名］的《［画作标题］》给出专业的形式分析，只聚焦于该画作的视觉特征。分析中不要提及画作标题与艺术家姓名。可按需使用连接词，以保证分析在语义与逻辑上的连贯。

**EN** Prompt for Stage 3-2: Specified aspect formal analysis annotation: You are a professional art critic. Please write a paragraph about [Number of Words] words of formal analysis of the [Painting Title] by [Artist Name] ONLY focusing on the [Specified Aspect]. DO NOT mention the painting title and artist’s name in your analysis.

**ZH** 阶段 3-2 的提示：指定面向的形式分析标注：你是一位专业的艺术评论家。请撰写一段约［词数］词的形式分析，针对［艺术家姓名］的《［画作标题］》，只聚焦于［指定面向］。分析中不要提及画作标题与艺术家姓名。

**EN** Appendix C More Cases for Qualitative Analysis

**ZH** 附录 C 定性分析的更多案例

<!-- [原子块 · img]  -->

**EN** Figure 7. Example for qualitative comparison of formal analysis generation by several powerful LMMs. Purple texts denote the factual content description, and the Blue texts are for formal analysis.

**ZH** 图 7. 若干强大 LMM 的形式分析生成定性比较示例。紫色文字表示事实性内容描述，蓝色文字表示形式分析。

**EN** C.1. More Cases for Comparison

**ZH** C.1. 更多比较案例

**EN** We first illustrate more cases for comparison with other LMMs in Figure 7, Figure 8, and a failure case in Figure 9. From the former two cases, we can see the similar observations in Figure 5 in main part. Here we focus on the failure case in Figure 9, from which we can observe that our GalleryGPT incorrectly recognized a vase as a candlestick (text with red color in Figure 9). This implies that the vision perceptron in our GalleryGPT needs to be improved to ensure the accurate visual encoding.

**ZH** 我们首先在图 7、图 8 中给出更多与其他 LMM 的比较案例，并在图 9 中给出一个失败案例。从前两个案例中可以看到与正文图 5 相似的观察。这里重点看图 9 的失败案例：我们的 GalleryGPT 把一个花瓶错误地识别为烛台（图 9 中红色文字）。这说明 GalleryGPT 中的视觉感知部分有待改进，以保证准确的视觉编码。

**EN** Then we illustrate more dialogue case with our GalleryGPT in Figure 10 and 11. From Figure 10, we can see that when the GalleryGPT is generating overall formal analysis, it would briefly analyze the main visual elements in the painting, while when we ask it to generate formal analysis focusing on specific aspect, e.g., Light and Shadow in Figure 10, it could give more in-depth analysis from this aspect and also consistent with the brief one.

**ZH** 随后我们在图 10 与图 11 中给出更多与 GalleryGPT 的对话案例。从图 10 可以看到，当 GalleryGPT 生成整体形式分析时，它会简要分析画作中的主要视觉要素；而当我们要求它生成聚焦特定面向（例如图 10 中的光影）的形式分析时，它能就该面向给出更深入的分析，且与简要版本保持一致。

**EN** C.2. The English Translation for The Chinese Case

**ZH** C.2. 中文案例的英文翻译

**EN** Finally, we give the English translation for the case in Chinese illustrated in Figure 6. To further investigate the multilingual capacity, we also test the same chat content in English with our GalleryGPT, and it outputs similar formal analysis in high-level semantics and concepts, but very different words and aspects in low-level semantics. This implies that our GalleryGPT is able to understand and generate the formal analysis with multiple languages.

**ZH** 最后，我们给出图 6 中所示中文案例的英文翻译。为进一步考察多语言能力，我们还用相同的聊天内容以英文测试了 GalleryGPT，它输出的形式分析在高层语义与概念上相似，但在低层语义上的用词与面向差别很大。这说明我们的 GalleryGPT 能够理解并以多种语言生成形式分析。

<!-- [原子块 · img]  -->

**EN** Figure 8. Example for qualitative comparison of formal analysis generation by several powerful LMMs. Purple texts denote the factual content description, and the Blue texts are for formal analysis.

**ZH** 图 8. 若干强大 LMM 的形式分析生成定性比较示例。紫色文字表示事实性内容描述，蓝色文字表示形式分析。

<!-- [原子块 · img]  -->

**EN** Figure 9. A failure case of our GalleryGPT. Purple texts denote the factual content description, and the Blue texts are for formal analysis. Red texts denote the wrong analyses.

**ZH** 图 9. 我们 GalleryGPT 的一个失败案例。紫色文字表示事实性内容描述，蓝色文字表示形式分析，红色文字表示错误的分析。

<!-- [原子块 · img]  -->

**EN** Figure 10. Multimodal dialogue examples with our GalleryGPT. Blue texts denote high quality formal analysis. We also test dialoguing in Chinese, even we do not fine-tune GalleryGPT with Chinese painting-analysis pairs. The English translation of Chinese conversation can be found in Supplementary.

**ZH** 图 10. 与我们的 GalleryGPT 的多模态对话示例。蓝色文字表示高质量的形式分析。我们还测试了用中文对话，尽管我们并未用中文绘画—分析配对微调 GalleryGPT。该中文对话的英文翻译见补充材料。

<!-- [原子块 · img]  -->

**EN** Figure 11. Multimodal dialogue examples with our GalleryGPT. Blue texts denote high quality formal analysis. We also test dialoguing in Chinese, even we do not fine-tune GalleryGPT with Chinese painting-analysis pairs. The English translation of Chinese conversation can be found in Supplementary.

**ZH** 图 11. 与我们的 GalleryGPT 的多模态对话示例。蓝色文字表示高质量的形式分析。我们还测试了用中文对话，尽管我们并未用中文绘画—分析配对微调 GalleryGPT。该中文对话的英文翻译见补充材料。

<!-- [原子块 · img]  -->

**EN** Figure 12. English Translation of Figure 6 in main part and the output of directly chatting with our GalleryGPT in English.

**ZH** 图 12. 正文图 6 的英文翻译，以及直接用英文与我们的 GalleryGPT 对话的输出。
