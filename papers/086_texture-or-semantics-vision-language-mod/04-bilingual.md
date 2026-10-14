# 纹理还是语义？视觉语言模型在字体识别中迷失

> 原标题：Texture or Semantics? Vision-Language Models Get Lost in Font Recognition
> 作者：Zhecheng Li, Guoxian Song, Yujun Cai, Zhen Xiong, Junsong Yuan, Yiwei Wang · arXiv:2503.23768 · 2025-03-31

<!-- [原子块 · verbatim] Texture or Semantics? Vision-Language Models Get Lost in Font Recognition -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] Modern Vision-Language Models (VLMs) exhibit remarkable visual and linguistic capabilities, achieving impressive performance in various tasks such as image recognition and object localization. However -->

**EN** 1 Introduction

**ZH** 1 引言

**EN** Font recognition is a fundamental visual task with applications across various domains. It is particularly relevant to graphic design, publishing, advertising, and digital content creation, where typography plays a crucial role in visual communication (Zramdini & Ingold, 1998; Chen et al., 2014b; Zhu et al., 2001). For example, researchers may seek to identify aesthetically appealing fonts in academic papers or images, while designers sometimes encounter unique typefaces they wish to integrate into their projects. Statistics indicate that over 60% of websites utilize custom or non-system fonts, highlighting the significance of font identification in web design. Additionally, Google Fonts are used on more than 50 million websites, demonstrating the extensive adoption of diverse typefaces (Solomons, 2023). This widespread demand underscores the need for efficient and accurate font recognition tools.

**ZH** 字体识别是一项基础性的视觉任务，应用遍及多个领域，与平面设计、出版、广告以及数字内容创作尤为相关——在这些领域中，字体排印在视觉传达中起着关键作用（Zramdini 和 Ingold，1998；Chen 等，2014b；Zhu 等，2001）。例如，研究者可能希望识别学术论文或图像中赏心悦目的字体，设计师有时也会遇到想要引入自己项目的独特字体。统计显示，超过 60% 的网站使用自定义或非系统字体，凸显了字体识别在网页设计中的重要性。此外，Google Fonts 被超过 5,000 万个网站采用，表明各类字体已被广泛使用（Solomons，2023）。这种普遍的需求凸显出对高效、准确字体识别工具的迫切需要。

**EN** Traditionally, Convolutional Neural Networks (CNNs) have been the predominant architecture for font recognition (Chen et al., 2021; Li et al., 2022b). While CNNs achieve high accuracy, they rely on large and well-annotated datasets for training (Wang & Zong, 2023; Zhang, 2023; Tonmoy et al., 2024). The process of data collection, annotation, and

**ZH** 传统上，卷积神经网络（CNN）一直是字体识别的主流架构（Chen 等，2021；Li 等，2022b）。CNN 虽能达到较高准确率，却依赖大规模、标注良好的数据集进行训练（Wang 和 Zong，2023；Zhang，2023；Tonmoy 等，2024）。数据收集、标注与

<!-- [原子块 · img]  -->

**EN** Figure 1: An illustrative example where the image displays the word ’Arial’ rendered in the ’Monoton’ font. The vision-language model incorrectly predicts the font as ’Arial’, indicating an over-reliance on textual content and limited sensitivity to font semantics.

**ZH** 图 1：一个示例性案例。图像以 Monoton 字体呈现单词「Arial」，而视觉语言模型错误地把字体预测为 Arial，说明模型过度依赖文本内容、对字体语义缺乏敏感。

**EN** curation is time-consuming and resource-intensive, limiting the scalability and adaptability of CNN-based systems in real-world applications. In contrast, VLMs, pre-trained on large-scale multimodal datasets, have demonstrated remarkable capabilities in processing both visual and textual information (Zhang et al., 2024c; Bordes et al., 2024; OpenAI et al., 2024b; OpenAI, 2024; Team et al., 2024; Google, 2025). Their ability to generalize across diverse visual tasks without extensive task-specific training makes them highly versatile. Additionally, many VLMs are open-weight and freely accessible, positioning them as practical alternatives for everyday font recognition.

**ZH** 遴选既耗时又耗费资源，限制了基于 CNN 的系统在真实应用中的可扩展性与适应性。相比之下，在大规模多模态数据集上预训练的 VLM 已展现出处理视觉与文本信息的出色能力（Zhang 等，2024c；Bordes 等，2024；OpenAI 等，2024b；OpenAI，2024；Team 等，2024；Google，2025）。它们无需大量任务专属训练即可在多样视觉任务间泛化，因而具有高度通用性。此外，许多 VLM 开放权重且可自由获取，这使它们成为日常字体识别的实用替代方案。

**EN** Although VLMs have the potential to aid in font recognition, there has been no comprehensive analysis or systematic evaluation of their capabilities in this domain. In this paper, we introduce a font recognition benchmark comprising 15 commonly used fonts, with images containing textual content rendered in these typefaces. To ensure a rigorous evaluation, we construct two dataset versions: an easy version, where fonts are recognized from images containing sentences, and a hard version, which introduces the stroop effect (Besner et al., 1997; MacLeod, 1991; Verhaeghen & De Meersman, 1998) by displaying font names in mismatched typefaces, adding an additional layer of difficulty. This benchmark provides a systematic assessment of state-of-the-art VLMs’ font recognition abilities.

**ZH** 尽管 VLM 有潜力辅助字体识别，但迄今尚无针对其在该领域能力的全面分析或系统评估。本文提出一个包含 15 种常用字体的字体识别基准，图像中的文本内容均以这些字体渲染。为保证评估的严谨性，我们构建了两个数据集版本：简单版本从含句子的图像中识别字体；困难版本则以不匹配的字型显示字体名称，引入 Stroop 效应（Besner 等，1997；MacLeod，1991；Verhaeghen 和 De Meersman，1998），额外增加了一层难度。该基准为当前最先进 VLM 的字体识别能力提供了系统评估。

**EN** We conduct extensive evaluations on 13 open-weight and closed-source VLMs. All tested models are struggle to differentiate between font types and exhibit high sensitivity to the textual content within images, as illustrated in Figure 1. The best-performing model achieves only around 30% accuracy on the easy version of the benchmark, while performance on the hard version is even more challenging, with accuracy dropping to approximately 15%. Additionally, chain-of-thought (CoT) prompting (Wei et al., 2023; Kojima et al., 2023) provides limited performance gains in this task. Furthermore, we incorporate single-letter images as demonstrations in few-shot learning scenarios to help VLMs identify font similarities. Interestingly, despite the widespread familiarity of these fonts and the relatively low difficulty of the task for humans, where few-shot examples significantly aid in font recognition, current VLMs continue to exhibit poor performance.

**ZH** 我们对 13 个开放权重与闭源 VLM 开展了广泛评估。所有被测模型都难以区分字体类型，且对图像中的文本内容高度敏感，如图 1 所示。表现最好的模型在基准简单版本上仅取得约 30% 的准确率，困难版本上的表现更为吃力，准确率降至约 15%。此外，思维链（CoT）提示（Wei 等，2023；Kojima 等，2023）在该任务上带来的性能增益有限。我们还把单字母图像作为示例引入少样本学习场景，帮助 VLM 辨识字体相似度。有意思的是，尽管这些字体广为人知、对人类而言任务难度也相对较低——少样本示例对人类识别字体帮助显著——当前的 VLM 依旧表现不佳。

**EN** In summary, our contributions are threefold:

**ZH** 综上，我们的贡献有三：

**EN** (i) We propose a font recognition benchmark with two versions to systematically evaluate the capabilities of VLMs and conduct a comprehensive assessment of 13 different models.

**ZH** (i) 我们提出一个含两个版本的字体识别基准，用以系统评估 VLM 的能力，并对 13 个不同模型开展全面评测。

**EN** (ii) Our results reveal that current VLMs perform poorly in font recognition, with neither Chain-of-Thought prompting nor few-shot learning providing significant improvements.

**ZH** (ii) 我们的结果表明，当前 VLM 在字体识别上表现糟糕，思维链提示与少样本学习都未带来显著改善。

**EN** (iii) We analyze attention matrices across image patches to gain deeper insights into their failure modes and susceptibility to texture-based perturbations.

**ZH** (iii) 我们分析跨图像块的注意力矩阵，以更深入地理解其失败模式以及对基于纹理的扰动的易感性。

**EN** 2 Related Works

**ZH** 2 相关工作

**EN** 2.1 Vision-Language Models

**ZH** 2.1 视觉语言模型

**EN** With the foundation laid by Transformer and CLIP (Vaswani et al., 2023; Radford et al., 2021), Vision-Language Models (VLMs) have emerged as powerful multimodal systems that seamlessly integrate both visual and linguistic modalities. These models bridges the gap between image and text understanding, enabling them to process and interpret complex multimodal data efficiently (OpenAI et al., 2024a; Bai et al., 2025; Team et al., 2024; Li et al., 2024; Liu et al., 2023; Caffagni et al., 2024; Zhang et al., 2024a; Yin et al., 2024; Team et al., 2025; Chen et al., 2024).

**ZH** 在 Transformer 与 CLIP（Vaswani 等，2023；Radford 等，2021）奠定的基础之上，视觉语言模型（VLM）已成为强大的多模态系统，能够无缝融合视觉与语言两种模态。这些模型弥合了图像理解与文本理解之间的鸿沟，使其能高效处理与解释复杂的多模态数据（OpenAI 等，2024a；Bai 等，2025；Team 等，2024；Li 等，2024；Liu 等，2023；Caffagni 等，2024；Zhang 等，2024a；Yin 等，2024；Team 等，2025；Chen 等，2024）。

**EN** Recent advancements in large-scale image-text datasets and contrastive learning have significantly improved VLM performance. These models now exhibit strong general representation capabilities, effectively aligning visual and textual information and achieving state-of-the-art results across multiple benchmarks, establishing themselves as key technologies in multimodal AI research (Zhang et al., 2024c; Bordes et al., 2024; Schuhmann et al., 2022; Li et al., 2023; Chen et al., 2025; Chen et al., 2020).

**ZH** 大规模图文数据集与对比学习的最新进展显著提升了 VLM 的性能。这些模型现已展现出较强的通用表征能力，能有效对齐视觉与文本信息，并在多个基准上取得最先进的结果，确立了其在多模态 AI 研究中的关键技术地位（Zhang 等，2024c；Bordes 等，2024；Schuhmann 等，2022；Li 等，2023；Chen 等，2025；Chen 等，2020）。

**EN** The strong multimodal capabilities of VLMs make them valuable tools in real-world applications. Models such as BLIP (Li et al., 2022a), Flamingo (Alayrac et al., 2022) and later GPT-4o (OpenAI et al., 2024b) exhibit impressive performance in visual question answering, image captioning, and multimodal dialogue, enabling applications in interactive AI agents and assistive technologies for visually impaired individuals (Agrawal et al., 2016; Zhang et al., 2024b; Guo et al., 2024; Gao et al., 2024; Zhai et al., 2024). These advancements underscore the versatility of VLMs in handling complex multimodal tasks.

**ZH** VLM 强大的多模态能力使其成为真实应用中的得力工具。BLIP（Li 等，2022a）、Flamingo（Alayrac 等，2022）以及后来的 GPT-4o（OpenAI 等，2024b）等模型在视觉问答、图像描述与多模态对话上表现出色，支撑了交互式 AI 智能体与面向视障人士的辅助技术中的应用（Agrawal 等，2016；Zhang 等，2024b；Guo 等，2024；Gao 等，2024；Zhai 等，2024）。这些进展凸显了 VLM 处理复杂多模态任务的通用性。

**EN** 2.2 Font Recognition

**ZH** 2.2 字体识别

**EN** Font recognition, a critical task for people such as researchers and designers, inherently combines visual and textual components. However, it has received limited attention within the Vision-Language Models (VLMs) research community. Traditionally, it has been approached as a text-image classification problem, predominantly relying on CNN-based methods (Wang et al., 2015b; Tensmeyer et al., 2017; Qi et al., 2025; Wang & Zong, 2023; Mohammadian et al., 2022; Cui & Inoue, 2021). While these approaches achieve relatively high accuracy with their proposed CNN-based architectures on specific datasets, they typically require extensive fine-tuning on large-scale datasets. This requirement makes them time-consuming and also limits their generalization capabilities.

**ZH** 字体识别对研究者与设计师等人群而言是一项关键任务，天然融合了视觉成分与文本成分。然而，它在视觉语言模型（VLM）研究社群中获得的关注有限。传统上，它被当作文本图像分类问题处理，主要依赖基于 CNN 的方法（Wang 等，2015b；Tensmeyer 等，2017；Qi 等，2025；Wang 和 Zong，2023；Mohammadian 等，2022；Cui 和 Inoue，2021）。这些方法虽凭其提出的 CNN 架构在特定数据集上取得较高准确率，但通常需要在大规模数据集上做大量微调，既耗时也限制了泛化能力。

**EN** VLMs have recently emerged as versatile tools in visual tasks, offering strong adaptability through large-scale pretraining. They present a promising, convenient solution for font recognition. However, their capabilities in this task remain underexplored, motivating our study to provide a systematic evaluation and identify potential limitations.

**ZH** VLM 近来已成为视觉任务中的通用工具，凭借大规模预训练具备很强的适应性，为字体识别提供了一种前景良好且便捷的方案。然而，其在该任务上的能力仍未得到充分探索，这也促使我们开展系统评估并识别潜在局限。

**EN** 3 Font Recognition Benchmark

**ZH** 3 字体识别基准

**EN** We propose the Font Recognition Benchmark (FRB) to assess VLMs’ ability to recognize typographic styles from images. Unlike different versions or subsets of the VFR dataset, which contains more than 2,400 font classes and further categorizes the same font style into regular, bold, and other sub-types, the VFR dataset is more suitable for CNN-based model training rather than for basic capability exploration of VLMs in line with our objectives (Wang et al., 2015a; Chen et al., 2014a). In contrast, FRB follows three principles: practicality, using commonly encountered fonts; diversity, covering multiple font categories; and graduated challenge, testing different recognition scenarios. It includes two versions: an easy version, where sentences appear in various fonts, and a hard version, where font names are displayed in mismatched typefaces, creating a stroop effect.

**ZH** 我们提出字体识别基准（FRB），用以评估 VLM 从图像中识别字体排印风格的能力。VFR 数据集包含超过 2,400 种字体类别，并把同一字体样式进一步细分为常规体、粗体等子类型；与 VFR 数据集的不同版本或子集不同，VFR 更适合训练基于 CNN 的模型，而不适合按我们的目标去探索 VLM 的基础能力（Wang 等，2015a；Chen 等，2014a）。相比之下，FRB 遵循三条原则：实用性——采用日常常见的字体；多样性——覆盖多个字体类别；梯度式挑战——测试不同的识别场景。它包含两个版本：简单版本中句子以各种字体呈现；困难版本中字体名称以不匹配的字型显示，从而产生 Stroop 效应。

**EN** 3.1 Font Selection

**ZH** 3.1 字体选择

**EN** Fonts are generally categorized into three major types: Serif Fonts, Sans-Serif Fonts, and Script & Decorative Fonts. To ensure stylistic diversity in our experiments, we select 15 widely used fonts from these three categories, We choose these fonts based on responses from GPT-4o, Claude-3.5-Sonnet, and statistical data (as shown in Appendix A). The classification and corresponding font names are as follows:

**ZH** 字体通常分为三大类：衬线字体、无衬线字体，以及手写体与装饰字体。为保证实验中的风格多样性，我们从这三个类别中选取了 15 种广泛使用的字体；选择依据来自 GPT-4o、Claude-3.5-Sonnet 的回答以及统计数据（见附录 A）。分类与对应字体名称如下：

**EN** Serif Fonts: Baskerville SC, Georgia, Merriweather, Times New Roman, Roboto Slab.

**ZH** 衬线字体：Baskerville SC、Georgia、Merriweather、Times New Roman、Roboto Slab。

**EN** Sans-Serif Fonts: Arial, Calibri, Consola, Helvetica, Monoton, Vera.

**ZH** 无衬线字体：Arial、Calibri、Consola、Helvetica、Monoton、Vera。

**EN** Script & Decorative Fonts: Great Vibes, Lobster, Pacifico, Satisfy.

**ZH** 手写体与装饰字体：Great Vibes、Lobster、Pacifico、Satisfy。

<!-- [原子块 · img]  -->

**EN** Figure 2: An overview of the complete pipeline for constructing the font recognition benchmark, including the two-tier evaluation design. TTF files and corresponding codes ensure visual consistency across images. The easy task evaluates the basic font recognition ability of VLMs, while the hard task introduces stroop effect to assess robustness under semantic-visual conflict.

**ZH** 图 2：字体识别基准构建的完整流程概览，含双层评估设计。TTF 文件与相应代码保证了图像间的视觉一致性。简单任务评估 VLM 的基础字体识别能力，困难任务引入 Stroop 效应以评估其在语义—视觉冲突下的鲁棒性。

**EN** 3.2 Benchmark Image Construction

**ZH** 3.2 基准图像构建

**EN** We generate 10 images per font, each containing a distinct sentence designed to incorporate as many of the 26 English letters as possible. This results in a total of ⟦SLOT_0⟧ images, forming the easy version of the benchmark. These images are created using a consistent Python script that ensures uniform line breaks, font size, and background, maintaining a balanced aspect ratio aligned with the model’s input requirements. This easy version allows VLMs to focus exclusively on font recognition without interference from textual content.

**ZH** 我们为每种字体生成 10 张图像，每张包含一个不同的句子，句子在设计上尽可能多地涵盖 26 个英文字母。这共得到 ⟦SLOT_0⟧ 张图像，构成基准的简单版本。这些图像由统一的 Python 脚本生成，确保换行、字号与背景一致，并保持与模型输入要求相匹配的均衡宽高比。该简单版本使 VLM 能专注于字体识别而不受文本内容干扰。

**EN** For the hard version of the benchmark, we generate 15 additional images per font, each displaying its respective name. The image generation process employs a unified Python script utilizing the ImageDraw and ImageFont packages, ensuring consistency in font size and background dimensions across all images. This approach eliminates discrepancies associated with alternative methods such as screenshots. The inclusion of font names introduces the stroop effect, increasing the benchmark’s difficulty. In total, this results in ⟦SLOT_1⟧ images, constituting the complete hard version of the benchmark.

**ZH** 对于基准的困难版本，我们为每种字体额外生成 15 张图像，每张显示其自身的名称。图像生成过程使用统一的 Python 脚本，调用 ImageDraw 与 ImageFont 包，确保所有图像在字号与背景尺寸上一致；这种做法消除了截图等其他方法带来的差异。字体名称的引入带来了 Stroop 效应，提高了基准的难度。这共得到 ⟦SLOT_1⟧ 张图像，构成基准完整的困难版本。

**EN** Finally, to support few-shot learning experiments, we generate 52 additional images, each containing one uppercase or lowercase letter from the 26 English alphabets. These images serve as reference samples, allowing VLMs to leverage few-shot learning for feature comparison and adaptation in subsequent experiments.

**ZH** 最后，为支持少样本学习实验，我们额外生成 52 张图像，每张包含 26 个英文字母中的一个大写或小写形式。这些图像用作参考样本，使 VLM 能在后续实验中借助少样本学习进行特征比较与适配。

**EN** 3.3 Challenges

**ZH** 3.3 挑战

**EN** 3.3.1 Font Recognition

**ZH** 3.3.1 字体识别

**EN** When the text content in an image consists of sentences, this task simulates real-world scenarios where individuals capture screenshots of textual content to identify the font used. The primary objective is to assess the VLMs’ ability to recognize fonts. The presence of a greater number of letters enhances the models’ capacity to capture distinctive font characteristics, while the relatively small text size further challenges its ability to perform fine-grained recognition.

**ZH** 当图像中的文本内容由句子构成时，该任务模拟了这样一类真实场景：人们截取文本内容的截图以识别所用字体。其主要目标是评估 VLM 识别字体的能力。字母数量更多有助于模型捕捉字体的独特特征，而相对较小的文本尺寸则进一步考验其细粒度识别能力。

**EN** 3.3.2 Stroop Effect

**ZH** 3.3.2 Stroop 效应

**EN** When image text contains font names, a conflict between the textual meaning and the visual font triggers the stroop effect (MacLeod, 1991; Verhaeghen & De Meersman, 1998; Besner et al., 1997). For instance, the word “Times New Roman” rendered in Lobster font may mislead a model to predict the text’s meaning rather than the actual font. Even with clear visual differences, models often misclassify due to cognitive interference. This setup challenges VLMs to disentangle textual semantics from typographic appearance.

**ZH** 当图像文本包含字体名称时，文本含义与视觉字体之间的冲突会触发 Stroop 效应（MacLeod，1991；Verhaeghen 和 De Meersman，1998；Besner 等，1997）。例如，以 Lobster 字体渲染的「Times New Roman」一词，可能误导模型去预测文本的含义而非真实字体。即便视觉差异明显，模型也常因认知干扰而误判。该设置考验 VLM 能否把文本语义与排印外观分离开来。

**EN** 4 Experimental Setup

**ZH** 4 实验设置

**EN** 4.1 Vision Language Models

**ZH** 4.1 视觉语言模型

**EN** To effectively assess the capabilities of the latest VLMs, we conduct experiments on 13 widely recognized models. Detailed information about these models is provided in Appendix B.

**ZH** 为有效评估最新 VLM 的能力，我们在 13 个广受认可的模型上开展实验。这些模型的详细信息见附录 B。

**EN** 4.2 Few-Shot Selection

**ZH** 4.2 少样本选取

**EN** Given the large number of tokens required for image input and the common real-world practice of identifying fonts by analyzing individual letter styles, we construct a dataset comprising 52 images, each representing an uppercase or lowercase letter from the 26 English alphabets. To ensure consistency and fairness in selecting few-shot samples, we employ the CLIP model for image similarity retrieval. In this setup, the 52 single-letter images serve as the retrieval database, while the experimental images containing font names and sentences function as target samples. We design six experimental scenarios, ranging from 1-shot to 6-shot settings.

**ZH** 鉴于图像输入所需词元数量庞大，且现实中人们常通过观察单个字母的样式来识别字体，我们构建了一个包含 52 张图像的数据集，每张图像呈现 26 个英文字母中的一个大写或小写形式。为保证少样本选取的一致性与公平性，我们采用 CLIP 模型进行图像相似度检索：52 张单字母图像充当检索库，而含字体名称与句子的实验图像则作为目标样本。我们设计了从 1-shot 到 6-shot 的六种实验场景。

**EN** Base Model EASY-VERSION HARD-VERSION Zero-Shot Zero-Shot CoT Zero-ShotM Zero-Shot CoTM Zero-Shot Zero-Shot CoT Zero-ShotM Zero-Shot CoTM Closed-Source Models GPT-4o 24.67 30.67 66.67 46.67 12.44 15.11 27.11 25.78 Claude-3.5-Sonnet 31.33 29.33 28.67 29.33 8.44 7.11 7.11 6.67 Gemini-2.0-Flash-001 18.67 18.00 18.67 18.00 9.78 9.78 9.78 9.78 GPT-4o-mini 0.00 2.67 33.33 28.00 4.44 4.89 8.44 8.89 Open-Weight Models Llama-3.2-90B-Vision-Instruct 9.33 12.67 11.33 11.33 8.44 9.78 9.33 7.11 Llama-3.2-11B-Vision-Instruct 18.67 9.33 16.67 14.00 13.33 7.56 6.67 5.33 Phi-3.5-Vision-Instruct 4.67 0.00 6.67 3.33 2.67 2.22 6.67 6.22 Phi-3-Vision-128K-Instruct 0.67 0.00 10.00 4.67 0.00 0.89 6.67 5.33 Qwen2-VL-7B-Instruct 0.00 2.00 7.33 7.33 4.44 4.44 6.67 7.56 Qwen2.5-VL-7B-Instruct 12.00 5.33 17.33 12.00 5.33 5.33 6.67 8.00 Qwen2-VL-72B-Instruct 8.00 7.33 6.67 7.33 6.22 6.22 6.67 5.78 Idefics3-8B-Llama3 1.33 1.33 7.33 7.33 4.89 0.89 6.67 6.22 Idefics2-8B 8.00 11.33 9.33 8.00 8.44 7.11 6.22 6.22

**ZH** 基础模型 简单版本 困难版本 零样本 零样本 CoT 零样本M 零样本 CoTM 零样本 零样本 CoT 零样本M 零样本 CoTM 闭源模型 GPT-4o 24.67 30.67 66.67 46.67 12.44 15.11 27.11 25.78 Claude-3.5-Sonnet 31.33 29.33 28.67 29.33 8.44 7.11 7.11 6.67 Gemini-2.0-Flash-001 18.67 18.00 18.67 18.00 9.78 9.78 9.78 9.78 GPT-4o-mini 0.00 2.67 33.33 28.00 4.44 4.89 8.44 8.89 开放权重模型 Llama-3.2-90B-Vision-Instruct 9.33 12.67 11.33 11.33 8.44 9.78 9.33 7.11 Llama-3.2-11B-Vision-Instruct 18.67 9.33 16.67 14.00 13.33 7.56 6.67 5.33 Phi-3.5-Vision-Instruct 4.67 0.00 6.67 3.33 2.67 2.22 6.67 6.22 Phi-3-Vision-128K-Instruct 0.67 0.00 10.00 4.67 0.00 0.89 6.67 5.33 Qwen2-VL-7B-Instruct 0.00 2.00 7.33 7.33 4.44 4.44 6.67 7.56 Qwen2.5-VL-7B-Instruct 12.00 5.33 17.33 12.00 5.33 5.33 6.67 8.00 Qwen2-VL-72B-Instruct 8.00 7.33 6.67 7.33 6.22 6.22 6.67 5.78 Idefics3-8B-Llama3 1.33 1.33 7.33 7.33 4.89 0.89 6.67 6.22 Idefics2-8B 8.00 11.33 9.33 8.00 8.44 7.11 6.22 6.22

**EN** Table 1: The accuracy of 13 open-weight and closed-source vision-language models on both the easy and hard versions of the benchmark under different settings. M indicates the use of a MCQ setting for inference. The highest accuracy in each setting is highlighted in bold, while the second-best results are underlined.

**ZH** 表 1：13 个开放权重与闭源视觉语言模型在不同设置下于基准简单版本与困难版本上的准确率。M 表示推理时采用选择题（MCQ）设置。各设置下的最高准确率以粗体标出，次优结果加下划线。

**EN** 5 Experimental Results

**ZH** 5 实验结果

**EN** We evaluate multiple VLMs using our proposed font recognition benchmark. The inference methods include the standard zero-shot approach, as well as Chain-of-Thought (CoT) (Wei et al., 2023; Kojima et al., 2023) and few-shot methods, providing a comprehensive assessment of VLMs’ font recognition capabilities. All experimental prompts are provided in Appendix F.

**ZH** 我们用所提出的字体识别基准评估多个 VLM。推理方法包括标准零样本方式，以及思维链（CoT）（Wei 等，2023；Kojima 等，2023）与少样本方法，从而对 VLM 的字体识别能力作出全面评估。所有实验提示见附录 F。

**EN** 5.1 Vision-Language Models Fail on Font Recognition Task

**ZH** 5.1 视觉语言模型在字体识别任务上失败

**EN** Table 1 demonstrates that contemporary VLMs exhibit suboptimal performance on font recognition tasks, despite the selected 15 fonts being among the more commonly used ones across three major font categories. Under the easy version of the benchmark in a zero-shot setting, the Claude-3.5-Sonnet achieves the highest accuracy among the evaluated models but only reaches approximately 31%, while powerful GPT-4o-mini achieves even 0% accuracy. Among open-weight models, performance remains notably poor, with only Llama-3.2-11B-Vision-Instruct surpassing 10%, achieving an accuracy of nearly 19%.

**ZH** 表 1 显示，尽管所选的 15 种字体已属三大字体类别中较为常用者，当代 VLM 在字体识别任务上的表现仍不理想。在基准简单版本的零样本设置下，Claude-3.5-Sonnet 在被测模型中准确率最高，但也仅约 31%；而能力强大的 GPT-4o-mini 准确率甚至为 0%。在开放权重模型中，表现同样明显糟糕，只有 Llama-3.2-11B-Vision-Instruct 超过 10%，取得近 19% 的准确率。

**EN** Performance further deteriorates under the hard version of the benchmark, which incorporates the stroop effect. In this setting, almost all models fail to exceed 15% accuracy in a zero-shot scenario. The sole exception is GPT-4o, which attains around 15% accuracy while using zero-shot CoT. Even other powerful closed-source models fail to surpass 10% accuracy, regardless of whether CoT is applied. These findings underscore the fundamental limitations of existing VLMs in font recognition tasks.

**ZH** 在引入 Stroop 效应的困难版本上，表现进一步恶化：该设置下几乎所有模型在零样本场景中的准确率都未能超过 15%。唯一的例外是 GPT-4o，它在使用零样本 CoT 时达到约 15% 的准确率。其他强大的闭源模型无论是否使用 CoT，准确率都未能超过 10%。这些发现凸显了现有 VLM 在字体识别任务上的根本局限。

**EN** 5.2 Vision-Language Models Can Rely on Spurious Visual Cues

**ZH** 5.2 视觉语言模型可能依赖虚假视觉线索

<!-- [原子块 · object]  -->

**EN** Figure 3: Accuracy comparison on the hard version of the benchmark under two labeling conditions: whether the rendered content in the image conflicts with the actual font label. M denotes inference under a multiple-choice setting.

**ZH** 图 3：基准困难版本在两种标注条件下的准确率对比——图像中渲染的内容是否与真实字体标签冲突。M 表示在选择题设置下推理。

**EN** To further investigate whether contemporary VLMs possess font recognition capabilities, we conduct an experiment using multiple-choice questions (MCQ) under zero-shot setting, where models are explicitly instructed to select the correct font category from the 15 given options. The results of this experiment are also presented in Table 1. We now compare these experimental results under the setting that does not use CoT prompting:

**ZH** 为进一步考察当代 VLM 是否真的具备字体识别能力，我们在零样本设置下开展了一项选择题（MCQ）实验：明确要求模型从给定的 15 个选项中选出正确的字体类别。该实验结果同样列于表 1。下面我们在不使用 CoT 提示的设置下比较这些实验结果：

**EN** For the easy version of the benchmark, we observe that among the four powerful closed-source models, MCQ does not lead to a significant improvement for Claude-3.5-Sonnet and Gemini-2.0-Flash-001. However, it significantly improves the accuracy of the two GPT-series models. Among all open-weight models, MCQ improves accuracy by 6–10 percentage points for Idefics3-8B-Llama3, Qwen2-VL-7B-Instruct, and Phi-3-Vision-128K-Instruct. However, this improvement remains marginal, as their original accuracy is close to 0%, indicating that even with a constrained choice set, these models still perform poorly. For other models, the accuracy gains under the MCQ setting are smaller, remaining below 4 percentage points.

**ZH** 就基准的简单版本而言，我们观察到：在四个强大的闭源模型中，MCQ 并未给 Claude-3.5-Sonnet 与 Gemini-2.0-Flash-001 带来显著提升，却显著提高了两个 GPT 系列模型的准确率。在所有开放权重模型中，MCQ 使 Idefics3-8B-Llama3、Qwen2-VL-7B-Instruct 与 Phi-3-Vision-128K-Instruct 的准确率提升了 6～10 个百分点。不过这一提升仍属微弱，因为其原始准确率已接近 0%，说明即便在选项受限的情况下，这些模型依旧表现糟糕。至于其他模型，MCQ 设置下的准确率增益更小，均低于 4 个百分点。

**EN** For the hard version of the benchmark, among closed-source models, only GPT-4o exhibits a significant improvement in accuracy under the MCQ setting, while other models show little to no change. Among open-weight models, a notable finding is that after applying MCQ, all models achieve an accuracy close to 6.67% which is precisely the expected accuracy if a model correctly identifies the font only when the font style matches the font name in the image. Figure 3 demonstrates that applying MCQ to the hard version of the benchmark only further amplifies the influence of the stroop effect. However, it has minimal impact when the text in the image does not match its font type. This strongly suggests that these models lack the capability to discern the correct font under the stroop effect; instead, they are merely influenced by the textual content in the image. This result further underscores the susceptibility of VLMs to the stroop effect in this task. Given their inherent limitations in font recognition, even when provided with explicit answer choices, these models fail to leverage the constraints meaningfully. Instead, they appear to be even more influenced by the textual content, as evidenced by the accuracy drop observed in Llama-3.2-11B-Vision-Instruct on the hard version.

**ZH** 就基准的困难版本而言，在闭源模型中只有 GPT-4o 在 MCQ 设置下准确率显著提升，其他模型几乎无变化。在开放权重模型中，一个值得注意的发现是：应用 MCQ 后，所有模型的准确率都接近 6.67%——这恰是模型仅在字体样式与图像中字体名称一致时才能识别正确的期望准确率。图 3 表明，对困难版本应用 MCQ 只会进一步放大 Stroop 效应的影响；而当图像中的文本与其字体类型不匹配时，其影响却很小。这有力地说明，这些模型在 Stroop 效应下缺乏辨别正确字体的能力，只不过是被图像中的文本内容所左右。该结果进一步凸显了 VLM 在该任务中对 Stroop 效应的易感性。鉴于其在字体识别上的固有局限，即便给出了明确的答案选项，这些模型也无法有意义地利用这些约束；相反，它们似乎更易受文本内容影响——Llama-3.2-11B-Vision-Instruct 在困难版本上出现的准确率下降即是明证。

<!-- [原子块 · object]  -->

**EN** Figure 4: Few-shot accuracy (1-shot to 6-shot) on the hard benchmark setting, evaluated across six vision-language models from distinct model families.

**ZH** 图 4：困难基准设置下的少样本准确率（1-shot 至 6-shot），在来自不同模型家族的六个视觉语言模型上评估。

**EN** 5.3 Few-shot Learning Provides Limited Improvements

**ZH** 5.3 少样本学习带来的改善有限

**EN** In real-world scenarios, when given reference images of individual letters written in a specific font style, humans can carefully compare these samples with a test image to determine the font type. This raises the question of whether few-shot learning can enhance VLMs’ font recognition capabilities — specifically, whether VLMs can focus on the features provided in the demonstrations and leverage comparison-based reasoning to identify the correct font in the final test image.

**ZH** 在真实场景中，若给定以特定字体样式书写的单个字母的参考图像，人类可以仔细比对这些样本与测试图像来判断字体类型。这引出一个问题：少样本学习能否增强 VLM 的字体识别能力——具体而言，VLM 能否聚焦于示例所提供的特征，并借助基于比较的推理在最终测试图像中识别出正确字体。

**EN** To investigate this, we conduct few-shot experiments on six open-weight and closed-source VLMs under the setting described in Section 4.2. As shown in Figure 4, increasing the number of shots from 1 to 6 results in only a marginal improvement in model accuracy, with gains of less than 4 percentage points across all models. Given the dataset size for the hard version of the benchmark evaluation, this level of improvement is not ideal. Furthermore, we observe that, with the exception of the Qwen2-VL-72B-Instruct, whose accuracy either increases or remains stable as the number of shots increases, other models exhibit fluctuations in accuracy despite receiving more examples, which is counterintuitive. This instability further underscores the limited capabilities of VLMs in font recognition under few-shot settings. Notably, this contrasts sharply with human performance in fine-grained recognition tasks, where individuals effectively leverage reference samples to improve accuracy.

**ZH** 为此，我们在 4.2 节所述设置下对六个开放权重与闭源 VLM 开展少样本实验。如图 4 所示，把样本数从 1 增至 6 只带来微弱的准确率提升，所有模型的增益都不足 4 个百分点。考虑到困难版本评估所用的数据集规模，这样的提升幅度并不理想。此外我们观察到，除 Qwen2-VL-72B-Instruct 外（其准确率随样本数增加或升或持平），其他模型即便获得更多示例，准确率仍出现波动，这与直觉相悖。这种不稳定性进一步凸显了 VLM 在少样本设置下字体识别能力的局限。值得注意的是，这与人类在细粒度识别任务中的表现形成鲜明反差——人类能有效利用参考样本提升准确率。

**EN** 6 Categories of Errors

**ZH** 6 错误类别

<!-- [原子块 · table] Error Type Easy Version (%) Hard Version (%) Content-Biased Misattribution 0.00 70.11 Explicit Inability Acknowledgment 10.88 2.13 Indecisive Classification 64.87 14.46 Confidently Incorrect Predictio -->

**EN** Table 2: Error ratios for four distinct error categories, aggregated over all incorrect predictions by 13 vision-language models on both benchmark tiers (easy and hard).

**ZH** 表 2：四类不同错误的错误占比，汇总自 13 个视觉语言模型在基准两个层级（简单与困难）上的全部错误预测。

**EN** To investigate the reasons behind the suboptimal performance of VLMs in font recognition, we conduct a detailed analysis of model outputs to identify specific error patterns. Based on our observations, we classify the errors into four distinct categories and provide representative examples of each in Table 3.

**ZH** 为探究 VLM 在字体识别上表现欠佳的原因，我们对模型输出作细致分析以识别具体的错误模式。基于观察，我们把错误分为四个不同类别，并在表 3 中给出各自的代表性示例。

**EN** Content-Biased Misattribution: Error occurs primarily in the hard version of the benchmark, where the model mistakenly assumes that the font name appearing in the image corresponds to the actual font used for the text.

**ZH** 内容偏置型误判：该错误主要出现在困难版本中，模型误以为图像中出现的字体名称就是文本所用的真实字体。

**EN** Explicit Inability Acknowledgment: The model explicitly admits it cannot determine the font, often stating “more information is needed” or “I can’t determine the font”, reflecting awareness of its limitations.

**ZH** 明确承认无能为力：模型明确表示无法判断字体，常说「需要更多信息」或「我无法判断该字体」，反映出其对自身局限的察觉。

**EN** Indecisive Classification: The model analyzes font characteristics and distinguishes broad categories like Serif vs. Sans-Serif but fails to name a specific font, instead listing multiple candidates.

**ZH** 犹豫型分类：模型分析了字体特征并区分出衬线与无衬线等宽泛类别，却无法说出具体字体，而是列出多个候选。

**EN** Confidently Incorrect Prediction: The model gives a definitive but incorrect answer, sometimes with font analysis, displaying unjustified confidence and leading to misleading results.

**ZH** 自信的错误预测：模型给出确定但错误的答案，有时还附带字体分析，表现出缺乏依据的自信，导致结果具有误导性。

**EN** Table 2 presents the distribution of error types across two benchmark levels. Notably, in the easy version, where the image content consists of complete sentences, content-biased misattribution does not occur. Although the textual content in this setting does not pose a stroop effect challenge, a considerable portion of the model responses indicate either an explicit acknowledgment of their inability to perform the font recognition task or the provision of only a set of possible candidates or a broader font category, without a definitive prediction. This suggests that current VLMs lack the robustness required for accurate font recognition and often exhibit uncertainty when faced with this task.

**ZH** 表 2 给出了两个基准层级上错误类型的分布。值得注意的是，在图像内容由完整句子构成的简单版本中，并不存在内容偏置型误判。尽管该设置下的文本内容不构成 Stroop 效应挑战，仍有相当比例的模型回答要么明确承认自己无法完成字体识别任务，要么只给出一组可能候选或更宽泛的字体类别，而不作确定预测。这说明当前 VLM 缺乏准确字体识别所需的鲁棒性，面对该任务时常表现出不确定性。

**EN** In contrast, in the hard version, the presence of font names within the images introduces significant confusion. Even when utilizing Chain-of-Thought prompting, most models struggle to consistently analyze font features and instead rely heavily on the textual content. Only a few sufficiently strong models demonstrate the ability to reason in the correct direction. These findings indicate that current VLMs lack robustness and are not yet capable of reliably handling font recognition tasks.

**ZH** 相比之下，在困难版本中，图像内出现的字体名称引入了显著混乱。即便使用思维链提示，多数模型仍难以一贯地分析字体特征，转而严重依赖文本内容，只有少数足够强的模型展现出朝正确方向推理的能力。这些发现表明，当前 VLM 缺乏鲁棒性，尚不能可靠地处理字体识别任务。

<!-- [原子块 · table] Error Category Label Incorrect Model Prediction Content-Biased Misattribution Lobster The text in the image is ‘Georgia’. This is a font name, which is used to describe the style and appearance of the -->

**EN** Table 3: Examples of four different error types in both the easy and hard versions of the benchmark, displaying the incorrect model predictions alongside the corresponding ground-truth labels.

**ZH** 表 3：基准简单版本与困难版本中四类不同错误的示例，展示模型的错误预测及对应的真值标签。

**EN** 7 Do VLMs Truly Focus on Crucial Edge Regions?

**ZH** 7 VLM 是否真正聚焦于关键的边缘区域？

**EN** Different VLMs utilize distinct mechanisms for processing image inputs. Considering both their popularity and open-weight availability, we analyze the attention matrices from two models: Llama-3.2-11B-Vision-Instruct and Qwen2-VL-7B-Instruct.

**ZH** 不同 VLM 处理图像输入的机制各异。综合考虑其流行程度与权重可得性，我们分析了两个模型的注意力矩阵：Llama-3.2-11B-Vision-Instruct 与 Qwen2-VL-7B-Instruct。

**EN** Figure 5 presents the attention matrix of the final cross-attention layer for the Llama-3.2-11B-Vision-Instruct model on incorrect predictions from the hard version of the benchmark. All images in this figure share a common characteristic: the displayed font name does not match the actual font used. If VLMs truly possess the ability to identify fonts, their predictions should not be heavily influenced by this discrepancy. For instance, a human observer would easily recognize that the text displaying ‘Baskervville SC’ is not written in the Baskervville SC font, as the characteristics of the letters suggest a script-style font. However, as observed in the attention matrix, Llama-3.2-11B-Vision-Instruct fails to focus on the regions that capture distinctive font features, such as the edges of individual characters. Instead, across all six sub-images, the model exhibits misplaced attention, often focusing on irrelevant background regions rather than the critical font-defining elements. This misalignment in attention leads to the failure of the recognition task, highlighting the model’s limitations in accurately distinguishing font styles.

**ZH** 图 5 给出了 Llama-3.2-11B-Vision-Instruct 在基准困难版本上错误预测的最后一个交叉注意力层的注意力矩阵。图中所有图像都有一个共同特征：显示的字体名称与实际所用字体不一致。若 VLM 真的具备识别字体的能力，其预测就不该被这种不一致严重影响。例如，人类观察者很容易看出显示为「Baskervville SC」的文字并非以 Baskervville SC 字体书写，因为字母的特征表明它是一种手写体风格。然而从注意力矩阵可见，Llama-3.2-11B-Vision-Instruct 未能聚焦于捕捉字体独特特征的区域（如单个字符的边缘）；相反，在全部六幅子图中，模型的注意力都落错了位置，常常关注无关的背景区域而非决定字体的关键元素。这种注意力错位导致识别任务失败，凸显出模型在准确区分字体样式上的局限。

<!-- [原子块 · img]  -->

**EN** Figure 5: Attention heatmaps from the final cross-attention layer of Llama-3.2-11B-Vision-Instruct, illustrating how text tokens attend to image patches for six input images from the hard version of the benchmark, all of which the model fails to classify correctly. Attention weights are averaged across all heads.

**ZH** 图 5：Llama-3.2-11B-Vision-Instruct 最后一个交叉注意力层的注意力热力图，展示文本词元如何关注图像块——输入为困难版本中被模型误判的六张图像。注意力权重在所有注意力头上取平均。

<!-- [原子块 · img]  -->

**EN** Figure 6: Attention heatmaps from the middle cross-attention layer (⟦SLOT_2⟧) of Qwen2-VL-7B-Instruct, illustrating how text tokens attend to image patches for six input images from the easy version of the benchmark, all of which the model fails to classify correctly. Attention weights are averaged across all heads.

**ZH** 图 6：Qwen2-VL-7B-Instruct 中间交叉注意力层（⟦SLOT_2⟧）的注意力热力图，展示文本词元如何关注图像块——输入为简单版本中被模型误判的六张图像。注意力权重在所有注意力头上取平均。

**EN** Figure 6 presents the attention matrix for Qwen2-VL-7B-Instruct on the easy version of the benchmark. Compared to Llama-3.2-11B-Vision-Instruct, Qwen2-VL-7B-Instruct employs a larger merged patch size. However, regardless of patch size, a similar issue persists: the model’s attention does not sufficiently focus on the edges of the letters in the image. Instead, only a few letters receive more attention than other parts, and in many cases, the model assigns higher attention to the white background rather than the textual content. However, when comparing the attention matrices in Figure 6 with those in Figure 5, we observe that in the easy version of the benchmark, Qwen2-VL-7B-Instruct demonstrates a stronger tendency to focus on the textual regions. The red-highlighted areas in the attention matrix cover most of the text, even though the highest attention weights are not fully concentrated on the letters. Nevertheless, this represents a notable improvement over Llama-3.2-11B-Vision-Instruct ’s performance on the hard version of the benchmark, where attention is more poorly distributed.

**ZH** 图 6 给出了 Qwen2-VL-7B-Instruct 在基准简单版本上的注意力矩阵。与 Llama-3.2-11B-Vision-Instruct 相比，Qwen2-VL-7B-Instruct 采用了更大的合并块尺寸。然而无论块尺寸如何，类似问题依旧存在：模型的注意力没有充分聚焦在图像中字母的边缘上，只有少数字母比其他部分获得更多关注，且在很多情况下模型把更高的注意力分配给了白色背景而非文本内容。不过，把图 6 与图 5 的注意力矩阵对比可见，在简单版本上 Qwen2-VL-7B-Instruct 表现出更强的聚焦文本区域的倾向：注意力矩阵中的红色高亮区域覆盖了大部分文字，尽管最高注意力权重并未完全集中在字母上。相较 Llama-3.2-11B-Vision-Instruct 在困难版本上注意力分布更差的表现，这仍不失为一项明显改善。

**EN** Based on our analysis of the above two VLMs, we infer that current VLMs remain inadequate for font recognition tasks, even for widely used font styles. This limitation likely arises from their inability to focus on the critical regions of the textual input that are essential for accurate font identification. We posit that this shortcoming stems from an insufficient alignment between visual attention mechanisms and the subtle typographic features that define font identity. Consequently, advancing font recognition within VLMs demands a more targeted modeling of local visual regions and a deeper integration of typographic priors.

**ZH** 基于对上述两个 VLM 的分析，我们推断：即便面对广泛使用的字体样式，当前 VLM 仍不足以胜任字体识别任务。这一局限很可能源于它们无法聚焦于文本输入中那些对准确识别字体至关重要的区域。我们认为，该短板出自视觉注意力机制与决定字体身份的细微排印特征之间对齐不足。因此，要在 VLM 中推进字体识别，需要对局部视觉区域作更有针对性的建模，并把排印先验更深入地融合进来。

**EN** 8 Conclusion

**ZH** 8 结论

**EN** In this paper, we introduce a specially designed Font Recognition Benchmark (FRB) comprising 15 popular font styles, designed with both easy and hard versions to comprehensively assess the capabilities of contemporary VLMs in this fine-grained recognition task. We conduct extensive experiments with a range of VLMs and observe that these models consistently struggle with font recognition, particularly on the hard version of the benchmark, where the stroop effect substantially reduces accuracy. This finding highlights that VLMs remain susceptible to misleading visual cues even when performing semantically grounded tasks. To further examine the capacity of VLMs in this setting, we evaluate various inference strategies, including CoT prompting, Multiple-Choice Question answering, and Few-Shot Learning. However, our results demonstrate that these methods offer only marginal improvements in overall accuracy. Additionally, we categorize the error types exhibited by VLMs into four distinct categories and analyze the attention patterns of two publicly available VLMs. Our analysis reveals that these models fail to adequately focus on the edge information of characters in the input images, which impairs their ability to correctly identify font styles and renders them vulnerable to variations in texture content.

**ZH** 本文提出一个专门设计的字体识别基准（FRB），包含 15 种流行字体样式，设有简单与困难两个版本，用以全面评估当代 VLM 在这一细粒度识别任务上的能力。我们在一系列 VLM 上开展了大量实验，观察到这些模型在字体识别上一贯表现吃力，尤其在困难版本上——Stroop 效应大幅拉低了准确率。这一发现凸显出，即便在执行有语义依据的任务时，VLM 仍易受误导性视觉线索影响。为进一步检验 VLM 在该设置下的能力，我们评估了多种推理策略，包括 CoT 提示、选择题作答与少样本学习；然而结果表明，这些方法对整体准确率只有微弱改善。此外，我们把 VLM 表现出的错误类型归为四个不同类别，并分析了两个公开可得 VLM 的注意力模式。分析揭示，这些模型未能充分关注输入图像中字符的边缘信息，这削弱了它们正确识别字体样式的能力，并使它们易受纹理内容变化的影响。

**EN** 9 Limitation

**ZH** 9 局限性

**EN** In this paper, we propose a specially designed benchmark comprising two task versions to enable a comprehensive evaluation of VLMs’ performance on font recognition and analyze the factors contributing to their suboptimal performance. However, our study still has the following limitations: (i) Due to budget constraints, we are unable to conduct few-shot inference on more powerful models such as Claude-3.5-Sonnet and GPT-4o. (ii) As certain high-performing models are closed-source, we are unable to analyze their attention matrices, limiting our understanding of their decision-making processes. (iii) Our experiments rely on straightforward prompts for inference. Designing more sophisticated prompts, such as guiding models to focus on key regions in the input image, may enhance their performance on this task. We plan to explore these directions in future work.

**ZH** 本文提出一个专门设计的、包含两个任务版本的基准，以便全面评估 VLM 在字体识别上的表现，并分析导致其表现欠佳的因素。然而本研究仍存在以下局限：（i）受预算限制，我们无法在 Claude-3.5-Sonnet、GPT-4o 等更强大的模型上开展少样本推理；（ii）由于某些高性能模型闭源，我们无法分析其注意力矩阵，限制了对它们决策过程的理解；（iii）我们的实验依赖简单直接的提示进行推理，而设计更精巧的提示（例如引导模型关注输入图像中的关键区域）或可提升其在该任务上的表现。我们计划在未来工作中探索这些方向。

**EN** Acknowledgments

**ZH** 致谢

**EN** The work is partially supported by the NSF of the United States Grant CRII 2451683, an NVIDIA Academic Grants Program, the University of California, Merced, and a UC Merced Faculty Research Award. The views and conclusions are those of the authors and should not reflect the official policy or position of the U.S. Government.

**ZH** 本工作部分得到美国国家科学基金会（NSF）CRII 2451683 资助、NVIDIA 学术资助计划、加州大学默塞德分校以及 UC Merced 教师研究奖的支持。文中的观点与结论仅代表作者，不应被视为美国政府的官方政策或立场。

**EN** Ethics Statement

**ZH** 伦理声明

**EN** Ethical considerations play a central role in this research. All models used in this study are either open-weight or widely adopted within the scientific community, ensuring transparency and reproducibility. The proposed benchmark and evaluation framework aim to assess the capabilities of current VLMs on font recognition without introducing or reinforcing harmful biases. No personally identifiable information or sensitive data is involved in this work. We are committed to responsible research practices, and we advocate for the transparent reporting and ethical deployment of AI technologies in ways that serve the broader interests of society.

**ZH** 伦理考量在本研究中占据核心位置。本研究使用的所有模型均为开放权重或在科学社群中被广泛采用，保证了透明性与可复现性。所提出的基准与评估框架旨在评估当前 VLM 的字体识别能力，不会引入或强化有害偏置。本工作不涉及任何个人可识别信息或敏感数据。我们致力于负责任的研究实践，并倡导以服务于社会更广泛利益的方式透明地报告并合乎伦理地部署 AI 技术。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] Abdin et al. (2024) Marah Abdin, Jyoti Aneja, Hany Awadalla, Ahmed Awadallah, Ammar Ahmad Awan, Nguyen Bach, Amit Bahree, Arash Bakhtiari, Jianmin Bao, Harkirat Behl, Alon Benhaim, Misha Bilenko, Joha -->

<!-- [原子块 · verbatim] Agrawal et al. (2016) Aishwarya Agrawal, Jiasen Lu, Stanislaw Antol, Margaret Mitchell, C. Lawrence Zitnick, Dhruv Batra, and Devi Parikh. Vqa: Visual question answering, 2016. URL https://arxiv.org/a -->

<!-- [原子块 · verbatim] Alayrac et al. (2022) Jean-Baptiste Alayrac, Jeff Donahue, Pauline Luc, Antoine Miech, Iain Barr, Yana Hasson, Karel Lenc, Arthur Mensch, Katie Millican, Malcolm Reynolds, Roman Ring, Eliza Rutherford -->

<!-- [原子块 · verbatim] Anthropic (2024) Anthropic. Claude 3.5 sonnet. https://www.anthropic.com/news/claude-3-5-sonnet , June 2024. Accessed Jun 20, 2024. -->

<!-- [原子块 · verbatim] Bai et al. (2025) Shuai Bai, Keqin Chen, Xuejing Liu, Jialin Wang, Wenbin Ge, Sibo Song, Kai Dang, Peng Wang, Shijie Wang, Jun Tang, Humen Zhong, Yuanzhi Zhu, Mingkun Yang, Zhaohai Li, Jianqiang Wan,  -->

<!-- [原子块 · verbatim] Besner et al. (1997) Derek Besner, Jennifer A Stolz, and Clay Boutilier. The stroop effect and the myth of automaticity. Psychonomic bulletin & review , 4(2):221–225, 1997. -->

<!-- [原子块 · verbatim] Bordes et al. (2024) Florian Bordes, Richard Yuanzhe Pang, Anurag Ajay, Alexander C. Li, Adrien Bardes, Suzanne Petryk, Oscar Mañas, Zhiqiu Lin, Anas Mahmoud, Bargav Jayaraman, Mark Ibrahim, Melissa H -->

<!-- [原子块 · verbatim] Caffagni et al. (2024) Davide Caffagni, Federico Cocchi, Luca Barsellotti, Nicholas Moratelli, Sara Sarto, Lorenzo Baraldi, Lorenzo Baraldi, Marcella Cornia, and Rita Cucchiara. The revolution of mult -->

<!-- [原子块 · verbatim] Chen et al. (2014a) Guang Chen, Jianchao Yang, Hailin Jin, Jonathan Brandt, Eli Shechtman, Aseem Agarwala, and Tony X. Han. Large-scale visual font recognition. In 2014 IEEE Conference on Computer Vis -->

<!-- [原子块 · verbatim] Chen et al. (2014b) Guang Chen, Jianchao Yang, Hailin Jin, Jonathan Brandt, Eli Shechtman, Aseem Agarwala, and Tony X Han. Large-scale visual font recognition. In Proceedings of the IEEE Conference on -->

<!-- [原子块 · verbatim] Chen et al. (2021) Jingchao Chen, Shiyi Mu, Shugong Xu, and Youdong Ding. Henet: forcing a network to think more for font recognition. In Proceedings of the 3rd International Conference on Advanced In -->

<!-- [原子块 · verbatim] Chen et al. (2020) Ting Chen, Simon Kornblith, Mohammad Norouzi, and Geoffrey Hinton. A simple framework for contrastive learning of visual representations, 2020. URL https://arxiv.org/abs/2002.05709  -->

<!-- [原子块 · verbatim] Chen et al. (2024) Zhe Chen, Jiannan Wu, Wenhai Wang, Weijie Su, Guo Chen, Sen Xing, Muyan Zhong, Qinglong Zhang, Xizhou Zhu, Lewei Lu, Bin Li, Ping Luo, Tong Lu, Yu Qiao, and Jifeng Dai. Internvl: Sc -->

<!-- [原子块 · verbatim] Chen et al. (2025) Zhe Chen, Weiyun Wang, Yue Cao, Yangzhou Liu, Zhangwei Gao, Erfei Cui, Jinguo Zhu, Shenglong Ye, Hao Tian, Zhaoyang Liu, Lixin Gu, Xuehui Wang, Qingyun Li, Yimin Ren, Zixuan Chen, J -->

<!-- [原子块 · verbatim] Cui & Inoue (2021) Wenyi Cui and Kohei Inoue. Chinese calligraphy recognition system based on convolutional neural network. ICIC Express Letters , 15(11):1187–1195, 2021. -->

<!-- [原子块 · verbatim] Gao et al. (2024) Zhi Gao, Bofei Zhang, Pengxiang Li, Xiaojian Ma, Tao Yuan, Yue Fan, Yuwei Wu, Yunde Jia, Song-Chun Zhu, and Qing Li. Multi-modal agent tuning: Building a vlm-driven agent for efficie -->

<!-- [原子块 · verbatim] Google (2025) Google. Gemini 2.0. https://developers.googleblog.com/en/gemini-2-family-expands/ , February 2025. Accessed FEB. 5, 2025. -->

<!-- [原子块 · verbatim] Guo et al. (2024) Taicheng Guo, Xiuying Chen, Yaqi Wang, Ruidi Chang, Shichao Pei, Nitesh V Chawla, Olaf Wiest, and Xiangliang Zhang. Large language model based multi-agents: A survey of progress and  -->

<!-- [原子块 · verbatim] Kojima et al. (2023) Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yutaka Matsuo, and Yusuke Iwasawa. Large language models are zero-shot reasoners, 2023. URL https://arxiv.org/abs/2205.11916 . -->

<!-- [原子块 · verbatim] Li et al. (2024) Jian Li, Weiheng Lu, Hao Fei, Meng Luo, Ming Dai, Min Xia, Yizhang Jin, Zhenye Gan, Ding Qi, Chaoyou Fu, et al. A survey on benchmarks of multimodal large language models. arXiv prepr -->

<!-- [原子块 · verbatim] Li et al. (2022a) Junnan Li, Dongxu Li, Caiming Xiong, and Steven Hoi. Blip: Bootstrapping language-image pre-training for unified vision-language understanding and generation, 2022a. URL https://arxi -->

<!-- [原子块 · verbatim] Li et al. (2023) Junnan Li, Dongxu Li, Silvio Savarese, and Steven Hoi. Blip-2: Bootstrapping language-image pre-training with frozen image encoders and large language models, 2023. URL https://arxiv. -->

<!-- [原子块 · verbatim] Li et al. (2022b) Xudong Li, Jingyi Wang, Haiyang Zhang, Yongke Huang, and Huihui Huang. Swordnet: Chinese character font style recognition network. IEEE Access , 10:8388–8398, 2022b. -->

<!-- [原子块 · verbatim] Liu et al. (2023) Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. Visual instruction tuning, 2023. URL https://arxiv.org/abs/2304.08485 . -->

<!-- [原子块 · verbatim] MacLeod (1991) Colin M MacLeod. Half a century of research on the stroop effect: an integrative review. Psychological bulletin , 109(2):163, 1991. -->

<!-- [原子块 · verbatim] Meta AI (2024) Meta AI. Llama 3.2: Revolutionizing edge ai and vision with open, customizable models. Meta AI Blog , 2024. URL https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-device -->

<!-- [原子块 · verbatim] Mohammadian et al. (2022) Mehrdad Mohammadian, Neda Maleki, Tobias Olsson, and Fredrik Ahlgren. Persis: A persian font recognition pipeline using convolutional neural networks. In 2022 12th Internatio -->

<!-- [原子块 · verbatim] OpenAI (2024) OpenAI. Gpt-4o-mini. https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/ , July 2024. Accessed JUL. 18, 2024. -->

<!-- [原子块 · verbatim] OpenAI et al. (2024a) OpenAI, Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, Red Avila, I -->

<!-- [原子块 · verbatim] OpenAI et al. (2024b) OpenAI, Aaron Hurst, Adam Lerer, Adam P. Goucher, Adam Perelman, Aditya Ramesh, Aidan Clark, AJ Ostrow, Akila Welihinda, Alan Hayes, Alec Radford, Aleksander Madry, Alex Baker-Wh -->

<!-- [原子块 · verbatim] Qi et al. (2025) Hengnian Qi, Hao Yang, Zhaojiang Wang, Jiabin Ye, Qiuyi Xin, Chu Zhang, and Qing Lang. Ancientglyphnet: an advanced deep learning framework for detecting ancient chinese characters in -->

<!-- [原子块 · verbatim] Radford et al. (2021) Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, and Ilya Sut -->

<!-- [原子块 · verbatim] Schuhmann et al. (2022) Christoph Schuhmann, Romain Beaumont, Richard Vencu, Cade Gordon, Ross Wightman, Mehdi Cherti, Theo Coombes, Aarush Katta, Clayton Mullis, Mitchell Wortsman, et al. Laion-5b: A -->

<!-- [原子块 · verbatim] Solomons (2023) Monique Solomons. 75 font statistics: Usage and market analysis. Linearity Blog , 2023. URL https://www.linearity.io/blog/font-statistics/ . -->

<!-- [原子块 · verbatim] Team et al. (2024) Gemini Team, Petko Georgiev, Ving Ian Lei, Ryan Burnell, Libin Bai, Anmol Gulati, Garrett Tanzer, Damien Vincent, Zhufeng Pan, Shibo Wang, Soroosh Mariooryad, Yifan Ding, Xinyang Ge -->

<!-- [原子块 · verbatim] Team et al. (2025) Gemma Team, Aishwarya Kamath, Johan Ferret, Shreya Pathak, Nino Vieillard, Ramona Merhej, Sarah Perrin, Tatiana Matejovicova, Alexandre Ramé, Morgane Rivière, Louis Rouillard, Thoma -->

<!-- [原子块 · verbatim] Tensmeyer et al. (2017) Chris Tensmeyer, Daniel Saunders, and Tony Martinez. Convolutional neural networks for font classification. In 2017 14th IAPR international conference on document analysis and  -->

<!-- [原子块 · verbatim] Tonmoy et al. (2024) Moshiur Rahman Tonmoy, Akhtaruzzaman Adnan, Aloke Kumar Saha, MF Mridha, and Nilanjan Dey. Descriptor: Multilingual visual font recognition dataset (mvfr). IEEE Data Descriptions  -->

<!-- [原子块 · verbatim] Tronchon et al. (2024) Léo Tronchon, Hugo Laurençon, and Victor Sanh. Introducing idefics2: A powerful 8b vision-language model for the community. Hugging Face Blog , 2024. URL https://huggingface.co/ -->

<!-- [原子块 · verbatim] Vaswani et al. (2023) Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin. Attention is all you need, 2023. URL https://arxiv.o -->

<!-- [原子块 · verbatim] Verhaeghen & De Meersman (1998) Paul Verhaeghen and Lieve De Meersman. Aging and the stroop effect: a meta-analysis. Psychology and aging , 13(1):120, 1998. -->

<!-- [原子块 · verbatim] Wang et al. (2024) Peng Wang, Shuai Bai, Sinan Tan, Shijie Wang, Zhihao Fan, Jinze Bai, Keqin Chen, Xuejing Liu, Jialin Wang, Wenbin Ge, Yang Fan, Kai Dang, Mengfei Du, Xuancheng Ren, Rui Men, Dayihen -->

<!-- [原子块 · verbatim] Wang & Zong (2023) Yixuan Wang and Yanyi Zong. Calligraphy font recognition algorithm based on improved densenet network. In 2023 Global Conference on Information Technologies and Communications (GCIT -->

<!-- [原子块 · verbatim] Wang et al. (2015a) Zhangyang Wang, Jianchao Yang, Hailin Jin, Eli Shechtman, Aseem Agarwala, Jonathan Brandt, and Thomas S. Huang. Deepfont: Identify your font from an image, 2015a. URL https://arxiv -->

<!-- [原子块 · verbatim] Wang et al. (2015b) Zhangyang Wang, Jianchao Yang, Hailin Jin, Eli Shechtman, Aseem Agarwala, Jonathan Brandt, and Thomas S Huang. Real-world font recognition using deep network and domain adaptation. -->

<!-- [原子块 · verbatim] Wei et al. (2023) Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc Le, and Denny Zhou. Chain-of-thought prompting elicits reasoning in large language models, -->

<!-- [原子块 · verbatim] Yin et al. (2024) Shukang Yin, Chaoyou Fu, Sirui Zhao, Ke Li, Xing Sun, Tong Xu, and Enhong Chen. A survey on multimodal large language models. National Science Review , 11(12), November 2024. ISSN 20 -->

<!-- [原子块 · verbatim] Zhai et al. (2024) Simon Zhai, Hao Bai, Zipeng Lin, Jiayi Pan, Peter Tong, Yifei Zhou, Alane Suhr, Saining Xie, Yann LeCun, Yi Ma, et al. Fine-tuning large vision-language models as decision-making ag -->

<!-- [原子块 · verbatim] Zhang et al. (2024a) Duzhen Zhang, Yahan Yu, Jiahua Dong, Chenxing Li, Dan Su, Chenhui Chu, and Dong Yu. Mm-llms: Recent advances in multimodal large language models, 2024a. URL https://arxiv.org/abs/ -->

<!-- [原子块 · verbatim] Zhang et al. (2024b) Jingyi Zhang, Jiaxing Huang, Sheng Jin, and Shijian Lu. Vision-language models for vision tasks: A survey. IEEE Transactions on Pattern Analysis and Machine Intelligence , 2024b. -->

<!-- [原子块 · verbatim] Zhang et al. (2024c) Jingyi Zhang, Jiaxing Huang, Sheng Jin, and Shijian Lu. Vision-language models for vision tasks: A survey, 2024c. URL https://arxiv.org/abs/2304.00685 . -->

<!-- [原子块 · verbatim] Zhang (2023) Xiangyang Zhang. Design and implementation of the chinese character font recognition system based on binary convolutional encoding and decoding network. In 2023 IEEE 5th International Con -->

<!-- [原子块 · verbatim] Zhu et al. (2001) Yong Zhu, Tieniu Tan, and Yunhong Wang. Font recognition based on global texture analysis. IEEE Transactions on pattern analysis and machine intelligence , 23(10):1192–1200, 2001. -->

<!-- [原子块 · verbatim] Zramdini & Ingold (1998) Abdelwahab Zramdini and Rolf Ingold. Optical font recognition using typographical features. IEEE Transactions on pattern analysis and machine intelligence , 20(8):877–882, 199 -->

**EN** Appendix A Font Introduction

**ZH** 附录 A 字体介绍

**EN** Fonts are generally categorized into three major types: Serif Fonts, Sans-Serif Fonts, and Script & Decorative Fonts.

**ZH** 字体通常分为三大类：衬线字体、无衬线字体，以及手写体与装饰字体。

**EN** Serif fonts are well-suited for print materials, formal documents, and books, as their serifs help guide the reader’s eye, improving the readability of long passages of text. Sans-serif fonts are commonly used in web design, presentations, and modern typographic layouts due to their enhanced clarity on digital screens. Script and decorative fonts are typically employed in posters, logos, and invitations, where individuality and artistic expression are prioritized.

**ZH** 衬线字体非常适合印刷材料、正式文件与书籍，其衬线有助于引导读者视线，提升长段文本的可读性。无衬线字体常用于网页设计、演示文稿与现代排版布局，因其在数字屏幕上清晰度更佳。手写体与装饰字体多用于海报、标识与请柬等强调个性与艺术表达的场合。

**EN** We provide a brief introduction to all fonts used in this study. Additionally, Table 4 presents statistical data on several popular fonts analyzed in our experiments (Solomons, 2023).

**ZH** 我们对本研究使用的所有字体作简要介绍。此外，表 4 给出了实验中分析的若干流行字体的统计数据（Solomons，2023）。

<!-- [原子块 · table] Font Name Usage Percentage Popular in Industry Year Created Helvetica 25% Graphic Design 1957 Times New Roman 20% Publishing 1932 Arial 15% Business 1982 Roboto 10% Web Design 2011 Georgia 5% Digital  -->

**EN** Table 4: Some popular fonts used in the paper, along with their typical usage statistics.

**ZH** 表 4：本文使用的部分流行字体及其典型使用统计。

**EN** A.1 Serif Fonts

**ZH** A.1 衬线字体

**EN** Baskerville SC: A classic serif font with small caps styling, Baskerville SC exudes elegance and traditional sophistication. It is ideal for formal documents, book titles, and branding.

**ZH** Baskerville SC：一款采用小型大写字母样式的经典衬线字体，Baskerville SC 散发典雅与传统的高级感，非常适合正式文件、书名与品牌塑造。

**EN** Georgia: Designed for readability on screens, Georgia is a warm and robust serif font with a classic touch. Its sturdy letterforms make it suitable for both print and digital use.

**ZH** Georgia：专为屏幕可读性而设计，Georgia 是一款带有经典韵味的温暖而稳健的衬线字体，其结实的字形使其既适用于印刷也适用于数字场景。

**EN** Merriweather: A modern serif font with a slightly condensed design, Merriweather offers a pleasant reading experience. It is often used for digital content, thanks to its balanced contrast and legibility.

**ZH** Merriweather：一款略带紧缩设计的现代衬线字体，Merriweather 提供愉悦的阅读体验。凭借均衡的对比度与易读性，它常用于数字内容。

**EN** Times New Roman: A widely recognized serif font, Times New Roman is synonymous with formal and academic writing. Its narrow proportions make it efficient for fitting text into limited spaces.

**ZH** Times New Roman：一款广为人知的衬线字体，Times New Roman 几乎就是正式与学术写作的代名词。其窄长的比例使文本能高效排入有限空间。

**EN** Roboto Slab: A geometric slab-serif font, Roboto Slab combines a modern feel with a sturdy, industrial aesthetic. It is commonly used for branding, web design, and contemporary editorial layouts.

**ZH** Roboto Slab：一款几何化的粗衬线字体，Roboto Slab 把现代感与坚实、工业化的美学结合在一起，常用于品牌塑造、网页设计与当代编辑排版。

**EN** A.2 Sans-Serif Fonts

**ZH** A.2 无衬线字体

**EN** Arial: One of the most widely used sans-serif fonts, Arial is known for its clean and simple design. It is commonly used in digital and print media due to its high legibility.

**ZH** Arial：使用最广泛的无衬线字体之一，Arial 以简洁明快的设计著称。凭借高易读性，它被广泛用于数字与印刷媒体。

**EN** Calibri: A default font in Microsoft Office, Calibri features a modern and rounded design. It provides a smooth reading experience and is often used in professional documents.

**ZH** Calibri：Microsoft Office 的默认字体，Calibri 采用现代而圆润的设计，提供顺滑的阅读体验，常用于专业文档。

**EN** Consola: A monospaced sans-serif font, Consola is frequently used in coding environments. Its even spacing ensures clarity in programming and technical texts.

**ZH** Consola：一款等宽无衬线字体，Consola 常用于编程环境；其均匀的间距保证了程序与技术文本的清晰。

**EN** Helvetica: A timeless and versatile sans-serif font, Helvetica is known for its neutrality and balanced proportions. It is extensively used in corporate branding and signage.

**ZH** Helvetica：一款永恒而通用的无衬线字体，Helvetica 以中立性与均衡比例著称，被广泛用于企业品牌与标识系统。

**EN** Monoton: A decorative sans-serif font, Monoton features a retro, futuristic design with bold, high-contrast strokes. It is best suited for eye-catching headlines and artistic typography.

**ZH** Monoton：一款装饰性无衬线字体，Monoton 采用复古未来主义设计，笔画粗壮、对比强烈，最适合用于引人注目的标题与艺术化排印。

**EN** Vera: A clean and modern sans-serif font, Vera provides excellent readability and is commonly used in user interfaces. Its simplicity makes it adaptable to various design applications.

**ZH** Vera：一款干净现代的无衬线字体，Vera 具备出色的可读性，常用于用户界面；其简洁性使其能适应各种设计应用。

**EN** A.3 Script & Decorative Fonts

**ZH** A.3 手写体与装饰字体

**EN** Great Vibes: A flowing script font with elegant curves, Great Vibes is perfect for invitations and sophisticated branding. Its graceful letterforms add a touch of luxury to any design.

**ZH** Great Vibes：一款线条流畅、曲线优雅的手写体，Great Vibes 非常适合请柬与高端品牌塑造，其优美的字形为任何设计增添一抹奢华。

**EN** Lobster: A bold and stylish script font, Lobster features connected letterforms with a casual yet artistic feel. It is widely used in branding, menus, and creative projects.

**ZH** Lobster：一款粗壮而时髦的手写体，Lobster 采用连笔字形，兼具随性与艺术气息，被广泛用于品牌塑造、菜单与创意项目。

**EN** Pacifico: Inspired by 1950s American surf culture, Pacifico is a playful script font with a relaxed, handwritten feel. It is often used for casual branding, logos, and fun designs.

**ZH** Pacifico：灵感源自 1950 年代美国冲浪文化，Pacifico 是一款俏皮的手写体，带有放松的手写感，常用于休闲品牌、标识与趣味设计。

**EN** Satisfy: A charming script font, Satisfy strikes a balance between casual and elegant lettering. It works well for branding, invitations, and creative typography.

**ZH** Satisfy：一款迷人的手写体，Satisfy 在随性与优雅的字形之间取得平衡，适用于品牌塑造、请柬与创意排印。

**EN** Appendix B Vision-Language Models

**ZH** 附录 B 视觉语言模型

**EN** To effectively assess the font recognition capabilities of the latest VLMs, we conduct experiments on a selection of well-known models.

**ZH** 为有效评估最新 VLM 的字体识别能力，我们在一批知名模型上开展实验。

**EN** Closed-Source Models: We evaluate two multimodal models developed by OpenAI: GPT-4o and GPT-4o-mini (OpenAI et al., 2024b; OpenAI, 2024), along with two widely recognized models from Anthropic and Google: Claude-3.5-Sonnet and Gemini-2.0-Flash-001 (Anthropic, 2024; Google, 2025).

**ZH** 闭源模型：我们评估了 OpenAI 开发的两个多模态模型 GPT-4o 与 GPT-4o-mini（OpenAI 等，2024b；OpenAI，2024），以及来自 Anthropic 与 Google 的两个广受认可的模型 Claude-3.5-Sonnet 与 Gemini-2.0-Flash-001（Anthropic，2024；Google，2025）。

**EN** Open-Weight Models: Our experiments include a diverse range of open-weight VLMs, spanning nine models across multiple series. Specifically, we test:

**ZH** 开放权重模型：我们的实验涵盖多样化的开放权重 VLM，横跨多个系列共九个模型。具体地，我们测试了：

**EN** • Three models from the Qwen multimodal series: Qwen2-VL-7B-Instruct, Qwen2.5-VL-7B-Instruct and Qwen2-VL-72B-Instruct (Wang et al., 2024; Bai et al., 2025).

**ZH** • 来自 Qwen 多模态系列的三个模型：Qwen2-VL-7B-Instruct、Qwen2.5-VL-7B-Instruct 与 Qwen2-VL-72B-Instruct（Wang 等，2024；Bai 等，2025）。

**EN** • Two models from the latest Llama 3.2 Vision series: Llama-3.2-90B-Vision-Instruct and Llama-3.2-11B-Vision-Instruct (Meta AI, 2024).

**ZH** • 来自最新 Llama 3.2 Vision 系列的两个模型：Llama-3.2-90B-Vision-Instruct 与 Llama-3.2-11B-Vision-Instruct（Meta AI，2024）。

**EN** • Two models from the Phi series developed by Microsoft: Phi-3.5-Vision-Instruct and Phi-3-Vision-128K-Instruct (Abdin et al., 2024).

**ZH** • 来自微软 Phi 系列的两个模型：Phi-3.5-Vision-Instruct 与 Phi-3-Vision-128K-Instruct（Abdin 等，2024）。

**EN** • Two models from the Idefics series: Idefics3-8B-Llama3 and Idefics2-8B (Tronchon et al., 2024).

**ZH** • 来自 Idefics 系列的两个模型：Idefics3-8B-Llama3 与 Idefics2-8B（Tronchon 等，2024）。

**EN** Here we provide a brief introduction to all Vision-Language Models utilized in this study.

**ZH** 下面简要介绍本研究使用的所有视觉语言模型。

**EN** B.1 Closed-Source Models

**ZH** B.1 闭源模型

**EN** GPT-4o: Developed by OpenAI, GPT-4o is a state-of-the-art multimodal model capable of processing text and images efficiently. It enhances vision-language understanding with improved reasoning, speed, and adaptability.

**ZH** GPT-4o：由 OpenAI 开发，GPT-4o 是一款能够高效处理文本与图像的最先进多模态模型，凭借更强的推理、更快的速度与更高的适应性提升了视觉语言理解能力。

**EN** GPT-4o-mini: A compact version of GPT-4o, GPT-4o-mini is designed for faster inference while maintaining strong multimodal capabilities. It is optimized for applications requiring efficiency without sacrificing quality.

**ZH** GPT-4o-mini：作为 GPT-4o 的精简版本，GPT-4o-mini 专为更快的推理而设计，同时保持强大的多模态能力；它针对那些要求效率而不牺牲质量的应用作了优化。

**EN** Claude-3.5-Sonnet: Developed by Anthropic, Claude-3.5-Sonnet is a highly capable vision-language model known for its alignment with human intent. It provides strong contextual understanding and excels in multimodal reasoning tasks.

**ZH** Claude-3.5-Sonnet：由 Anthropic 开发，Claude-3.5-Sonnet 是一款能力很强的视觉语言模型，以契合人类意图著称。它具备强大的上下文理解能力，在多模态推理任务上表现出色。

**EN** Gemini-2.0-Flash-001: Created by Google, Gemini-2.0-Flash-001 is an optimized vision-language model focused on rapid image-text processing. It is designed for applications that demand fast and efficient multimodal comprehension.

**ZH** Gemini-2.0-Flash-001：由 Google 打造，Gemini-2.0-Flash-001 是一款面向快速图文处理的优化型视觉语言模型，专为要求快速高效多模态理解的应用而设计。

**EN** B.2 Open-Weight Models

**ZH** B.2 开放权重模型

**EN** Qwen2-VL-7B-Instruct: Part of the Qwen multimodal series, Qwen2-VL-7B-Instruct is an open-weight vision-language model by Alibaba. It provides a balance between efficiency and accuracy for multimodal reasoning tasks.

**ZH** Qwen2-VL-7B-Instruct：作为 Qwen 多模态系列的一员，Qwen2-VL-7B-Instruct 是阿里巴巴推出的开放权重视觉语言模型，在多模态推理任务上兼顾效率与准确性。

**EN** Qwen2.5-VL-7B-Instruct: A refined version of its predecessor, Qwen2.5-VL-7B-Instruct introduces improved visual understanding and stronger text-image alignment. It is designed for tasks requiring high accuracy in multimodal analysis.

**ZH** Qwen2.5-VL-7B-Instruct：作为前作的精修版本，Qwen2.5-VL-7B-Instruct 引入了改进的视觉理解与更强的图文对齐能力，专为要求高精度多模态分析的任务而设计。

**EN** Qwen2-VL-72B-Instruct: The most powerful model in the Qwen2 series, Qwen2-VL-72B-Instruct features a larger architecture for superior vision-language comprehension. It excels in complex tasks that require deep reasoning across modalities.

**ZH** Qwen2-VL-72B-Instruct：Qwen2 系列中最强大的模型，Qwen2-VL-72B-Instruct 采用更大的架构以获得更优的视觉语言理解，擅长需要跨模态深度推理的复杂任务。

**EN** Llama-3.2-90B-Vision-Instruct: A high-capacity model from Meta’s Llama series, Llama-3.2-90B-Vision-Instruct is designed for advanced vision-language interaction. Its large-scale architecture enhances performance in multimodal understanding.

**ZH** Llama-3.2-90B-Vision-Instruct：Meta Llama 系列中的高容量模型，Llama-3.2-90B-Vision-Instruct 专为高级视觉语言交互而设计，其大规模架构提升了多模态理解性能。

**EN** Llama-3.2-11B-Vision-Instruct: A smaller variant of the Llama 3.2 Vision series, Llama-3.2-11B-Vision-Instruct offers a balance between efficiency and capability. It is ideal for resource-constrained environments requiring vision-language processing.

**ZH** Llama-3.2-11B-Vision-Instruct：Llama 3.2 Vision 系列中的较小变体，Llama-3.2-11B-Vision-Instruct 在效率与能力之间取得平衡，非常适合资源受限但需视觉语言处理的环境。

**EN** Phi-3.5-Vision-Instruct: Developed by Microsoft, Phi-3.5-Vision-Instruct is a lightweight yet powerful model tailored for multimodal tasks. It is optimized for efficiency while maintaining strong vision-language reasoning.

**ZH** Phi-3.5-Vision-Instruct：由微软开发，Phi-3.5-Vision-Instruct 是一款为多模态任务定制的轻量而强大的模型，在保持强大多模态推理的同时针对效率作了优化。

**EN** Phi-3-Vision-128K-Instruct: A larger-scale version in the Phi series, Phi-3-Vision-128K-Instruct supports longer context lengths, making it suitable for detailed and complex multimodal tasks. It enhances vision-language applications with broader contextual awareness.

**ZH** Phi-3-Vision-128K-Instruct：Phi 系列中的更大版本，Phi-3-Vision-128K-Instruct 支持更长的上下文长度，适合处理细致而复杂的多模态任务，以更宽广的上下文感知增强了视觉语言应用。

**EN** Idefics3-8B-Llama3: A vision-language model from the Idefics series, Idefics3-8B-Llama3 focuses on open-ended multimodal reasoning. It is designed to handle diverse vision-language tasks with improved contextual understanding.

**ZH** Idefics3-8B-Llama3：来自 Idefics 系列的视觉语言模型，Idefics3-8B-Llama3 专注于开放式多模态推理，凭借改进的上下文理解来处理多样的视觉语言任务。

**EN** Idefics2-8B: Another model from the Idefics family, Idefics2-8B provides a strong foundation for vision-language applications. It is optimized for tasks requiring nuanced text-image comprehension.

**ZH** Idefics2-8B：Idefics 家族中的另一款模型，Idefics2-8B 为视觉语言应用提供了扎实的基础，针对需要细腻图文理解的任务作了优化。

**EN** Appendix C Implementation Details

**ZH** 附录 C 实现细节

**EN** C.1 Metric

**ZH** C.1 指标

**EN** We use the most straightforward metric: Accuracy. The model’s performance is assessed by extracting the predicted labels from the text output and comparing them to the ground truth labels using string matching. The accuracy of a model is calculated as follows:

**ZH** 我们使用最直接的指标：准确率。模型性能通过从文本输出中提取预测标签，并与真值标签作字符串匹配比较来评估。模型准确率计算如下：

<!-- [原子块 · table] Accuracy = 1 N ​ ∑ i = 1 N I ​ ( y i = y ^ i ) \text{Accuracy}=\frac{1}{N}\sum_{i=1}^{N}\text{I}(y_{i}=\hat{y}_{i}) (1) -->

**EN** where ⟦SLOT_3⟧ is an indicator function that is 1 if the condition is true and 0 otherwise, ⟦SLOT_4⟧ represents the true label, ⟦SLOT_5⟧ is the predicted label, and ⟦SLOT_6⟧ is the total number of samples.

**ZH** 其中 ⟦SLOT_3⟧ 为指示函数，条件成立时取 1、否则取 0；⟦SLOT_4⟧ 表示真实标签；⟦SLOT_5⟧ 为预测标签；⟦SLOT_6⟧ 为样本总数。

**EN** C.2 Model Implementation

**ZH** C.2 模型实现

**EN** For all VLMs used in the experiments, we set the temperature to 0.0 and top_p to 0.95 to ensure faithfulness and minimize generation randomness, thereby enhancing reproducibility.

**ZH** 对于实验中使用的所有 VLM，我们把温度设为 0.0、top_p 设为 0.95，以保证忠实性并最小化生成随机性，从而提升可复现性。

**EN** For open-weight models, we obtain the weights from HuggingFace and perform inference using bfloat16 precision. All experiments involving these models are mainly conducted on a setup with four NVIDIA A100 80GB GPUs.

**ZH** 对于开放权重模型，我们从 HuggingFace 获取权重，并以 bfloat16 精度执行推理。涉及这些模型的所有实验主要在配备四块 NVIDIA A100 80GB GPU 的环境上进行。

**EN** For closed-source models, we access the official API for inference. All experiments are conducted between January 25, 2025, and March 25, 2025. To compute the similarity between images for selecting few-shot demonstrations, we employ the openai/clip-vit-base-patch32 model on HuggingFace.

**ZH** 对于闭源模型，我们调用官方 API 进行推理。所有实验在 2025 年 1 月 25 日至 2025 年 3 月 25 日之间开展。为计算图像间相似度以选取少样本示例，我们采用 HuggingFace 上的 openai/clip-vit-base-patch32 模型。

**EN** Appendix D Capability Gaps Between Open-weight and Closed-source Models

**ZH** 附录 D 开放权重模型与闭源模型的能力差距

**EN** The experimental results indicate that contemporary VLMs struggle with font recognition tasks, with a significant accuracy gap persisting between open-weight and closed-source models.

**ZH** 实验结果表明，当代 VLM 在字体识别任务上表现吃力，且开放权重模型与闭源模型之间存在显著的准确率差距。

**EN** In the sentence-based font recognition task, which is more commonly encountered in real-world scenarios, three out of four closed-source VLMs achieve at least 18% accuracy across various inference settings, with the best-performing model reaching nearly 67% under the multiple-choice question (MCQ) setting. In contrast, among all open-weight VLMs evaluated in this study, only Llama-3.2-11B-Vision-Instruct and Qwen2-VL-72B-Instruct attain approximately 18% accuracy, while the remaining models fall below 10%, with some approaching 0% accuracy. These findings highlight the substantial performance disparity between open-weight and closed-source VLMs in font recognition.

**ZH** 在真实场景中更常见的基于句子的字体识别任务中，四个闭源 VLM 中有三个在各种推理设置下都至少取得 18% 的准确率，表现最好的模型在选择题（MCQ）设置下接近 67%。相比之下，本研究评估的所有开放权重 VLM 中，只有 Llama-3.2-11B-Vision-Instruct 与 Qwen2-VL-72B-Instruct 达到约 18% 的准确率，其余模型均低于 10%，有些甚至接近 0%。这些发现凸显了开放权重与闭源 VLM 在字体识别上的巨大性能落差。

**EN** For the more challenging version of the task, overall performance remains low across both open-weight and closed-source models. The hard version introduces the stroop effect, adding an additional cognitive challenge that negatively impacts nearly all VLMs. Under the MCQ setting, all closed-source models are able to achieve accuracy above 6.67%, indicating that, in some cases, they successfully identify font styles rather than being misled by the textual content in the image. In contrast, open-weight models fail to do so in almost all cases, with the only exception of Llama-3.2-90B-Vision-Instruct.

**ZH** 对于难度更高的版本，开放权重与闭源模型的整体表现都很低。困难版本引入 Stroop 效应，带来额外的认知挑战，对几乎所有 VLM 都产生负面影响。在 MCQ 设置下，所有闭源模型都能取得 6.67% 以上的准确率，说明它们在部分情况下成功识别了字体样式，而未被图像中的文本内容误导。相比之下，开放权重模型几乎在所有情况下都做不到，唯一的例外是 Llama-3.2-90B-Vision-Instruct。

**EN** Appendix E Comparative Analysis of Model Accuracy Across Different Fonts

**ZH** 附录 E 不同字体上模型准确率的对比分析

**EN** To demonstrate the capability gap of VLMs in recognizing different font types, we evaluate 10 models across 15 distinct fonts and report the overall number of correct predictions under the four inference methods described in Table 1, on both the easy and hard versions of the benchmark.

**ZH** 为展示 VLM 在识别不同字体类型上的能力差距，我们在 15 种不同字体上评估 10 个模型，并按表 1 所述的四种推理方法，报告基准简单版本与困难版本上正确预测的总数。

**EN** From the results presented in Figure 11 to Figure 30, it is evident that each model tends to perform well on one or two specific font types, but struggles significantly with the remaining fonts. Notably, there is no single font or even a small subset of fonts that all models consistently recognize with high accuracy. Among the tested fonts, Arial and Times New Roman appear to be relatively easier for many models, likely due to their widespread use and higher representation in training corpora. In contrast, other fonts yield highly variable performance across models. For instance, Llama-3.2-90B-Vision-Instruct correctly identifies 23 instances of the Pacifico font in the easy version of the benchmark, whereas Llama-3.2-11B-Vision-Instruct, despite belonging to the same model family, fails to recognize any instances under identical conditions. This highlights a critical limitation of current VLMs: they lack generalizable font recognition capabilities and exhibit substantial performance disparities across font types.

**ZH** 从图 11 至图 30 的结果可以明显看出，每个模型往往只在一两种特定字体上表现良好，在其余字体上则明显吃力。值得注意的是，并不存在某一种字体、甚至某一小部分字体能让所有模型都一致地高精度识别。在被测字体中，Arial 与 Times New Roman 对许多模型而言相对容易，可能因为二者使用广泛、在训练语料中的表征也更多。相比之下，其他字体在各模型上的表现差异很大。例如，Llama-3.2-90B-Vision-Instruct 在简单版本上正确识别了 23 个 Pacifico 实例，而同属一个模型家族的 Llama-3.2-11B-Vision-Instruct 在相同条件下却一个也未识别出来。这凸显了当前 VLM 的一项关键局限：它们缺乏可泛化的字体识别能力，且在不同字体类型上表现出巨大性能差异。

**EN** Appendix F Experimental Prompts

**ZH** 附录 F 实验提示

**EN** We present the simple prompts employed in the experiments shown in Figures 7 through 10.

**ZH** 我们给出图 7 至图 10 所示实验中使用的简单提示。

<!-- [原子块 · svg]  -->

**EN** Figure 7: Zero-Shot prompt for all experiments in this paper.

**ZH** 图 7：本文所有实验使用的零样本提示。

<!-- [原子块 · svg]  -->

**EN** Figure 8: Zero-Shot CoT prompt for all experiments in this paper.

**ZH** 图 8：本文所有实验使用的零样本 CoT 提示。

<!-- [原子块 · svg]  -->

**EN** Figure 9: Zero-Shot Multiple-Choice Questions prompt for all experiments in this paper.

**ZH** 图 9：本文所有实验使用的零样本选择题提示。

<!-- [原子块 · svg]  -->

**EN** Figure 10: Zero-Shot CoT Multiple-Choice Questions prompt for all experiments in this paper.

**ZH** 图 10：本文所有实验使用的零样本 CoT 选择题提示。

**EN** Appendix G Additional Attention Visualizations

**ZH** 附录 G 补充注意力可视化

**EN** Due to space constraints in the main part of the paper, we give additional visualizations for two open-weight models to illustrate their attention patterns on the same input image across different layers. For Llama-3.2-11B-Vision-Instruct, we present attention matrices from all cross-attention layers, highlighting how attention evolves throughout the network. These visualizations reveal that, regardless of whether a layer is shallow or deep, the model consistently struggles to attend to the edge regions of characters in the image, which are critical for accurate font recognition.

**ZH** 受正文篇幅限制，我们为两个开放权重模型给出补充可视化，展示它们对同一输入图像在不同层上的注意力模式。对于 Llama-3.2-11B-Vision-Instruct，我们给出所有交叉注意力层的注意力矩阵，凸显注意力在整个网络中的演化。这些可视化揭示：无论层浅层深，模型一贯难以关注图像中字符的边缘区域，而这些区域对准确识别字体至关重要。

<!-- [原子块 · object]  -->

**EN** Figure 11: Number of correct predictions made by Claude-3.5-Sonnet on the Easy Benchmark for different fonts. The model performs best on Roboto Slab (39 correct predictions) and Merriweather (27 correct predictions), while struggling with fonts like Helevetica (0 correct predictions), Monoton (0 correct predictions), and Vera (0 correct predictions). The total number of experimental trials for each font is 40.

**ZH** 图 11：Claude-3.5-Sonnet 在简单基准上对不同字体的正确预测数量。该模型在 Roboto Slab（39 次正确预测）与 Merriweather（27 次正确预测）上表现最好，而在 Helevetica（0 次正确预测）、Monoton（0 次正确预测）与 Vera（0 次正确预测）等字体上表现吃力。每种字体的实验总次数为 40。

<!-- [原子块 · object]  -->

**EN** Figure 12: Number of correct predictions made by Claude-3.5-Sonnet on the Hard Benchmark for different fonts. The model performs best on Helvetica (11 correct predictions) and Arial (9 correct predictions), while struggling with fonts like Satisfy (2 correct predictions), Vera (2 correct predictions), and Baskerville SC (0 correct predictions). The total number of experimental trials for each font is 60.

**ZH** 图 12：Claude-3.5-Sonnet 在困难基准上对不同字体的正确预测数量。该模型在 Helvetica（11 次正确预测）与 Arial（9 次正确预测）上表现最好，而在 Satisfy（2 次正确预测）、Vera（2 次正确预测）与 Baskerville SC（0 次正确预测）等字体上表现吃力。每种字体的实验总次数为 60。

<!-- [原子块 · object]  -->

**EN** Figure 13: Number of correct predictions made by GPT-4o on the Easy Benchmark for different fonts. The model performs best on Arial (40 correct predictions) and Times New Roman (40 correct predictions), while struggling with fonts like Helevetica (2 correct predictions), Roboto Slab (0 correct predictions), and Vera (0 correct predictions). The total number of experimental trials for each font is 40.

**ZH** 图 13：GPT-4o 在简单基准上对不同字体的正确预测数量。该模型在 Arial（40 次正确预测）与 Times New Roman（40 次正确预测）上表现最好，而在 Helevetica（2 次正确预测）、Roboto Slab（0 次正确预测）与 Vera（0 次正确预测）等字体上表现吃力。每种字体的实验总次数为 40。

<!-- [原子块 · object]  -->

**EN** Figure 14: Number of correct predictions made by GPT-4o on the Hard Benchmark for different fonts. The model performs best on Great Vibes (32 correct predictions) and Monoton (30 correct predictions), while struggling with fonts like Merriweather (4 correct predictions), Roboto Slab (4 correct predictions), and Vera (2 correct predictions). The total number of experimental trials for each font is 60.

**ZH** 图 14：GPT-4o 在困难基准上对不同字体的正确预测数量。该模型在 Great Vibes（32 次正确预测）与 Monoton（30 次正确预测）上表现最好，而在 Merriweather（4 次正确预测）、Roboto Slab（4 次正确预测）与 Vera（2 次正确预测）等字体上表现吃力。每种字体的实验总次数为 60。

<!-- [原子块 · object]  -->

**EN** Figure 15: Number of correct predictions made by GPT-4o-mini on the Easy Benchmark for different fonts. The model performs best on Great Vibes (21 correct predictions) and Arial (20 correct predictions), while struggling with fonts like Calibri (0 correct predictions), Lobster (0 correct predictions), and Pacifico (0 correct predictions). The total number of experimental trials for each font is 40.

**ZH** 图 15：GPT-4o-mini 在简单基准上对不同字体的正确预测数量。该模型在 Great Vibes（21 次正确预测）与 Arial（20 次正确预测）上表现最好，而在 Calibri（0 次正确预测）、Lobster（0 次正确预测）与 Pacifico（0 次正确预测）等字体上表现吃力。每种字体的实验总次数为 40。

<!-- [原子块 · object]  -->

**EN** Figure 16: Number of correct predictions made by GPT-4o-mini on the Hard Benchmark for different fonts. The model performs best on Great Vibes (12 correct predictions) and Lobster (5 correct predictions), while struggling with fonts like Consola (2 correct predictions), Vera (2 correct predictions), and Baskervville SC (0 correct predictions). The total number of experimental trials for each font is 60.

**ZH** 图 16：GPT-4o-mini 在困难基准上对不同字体的正确预测数量。该模型在 Great Vibes（12 次正确预测）与 Lobster（5 次正确预测）上表现最好，而在 Consola（2 次正确预测）、Vera（2 次正确预测）与 Baskervville SC（0 次正确预测）等字体上表现吃力。每种字体的实验总次数为 60。

<!-- [原子块 · object]  -->

**EN** Figure 17: Number of correct predictions made by Gemini-2.0-Flash-001 on the Easy Benchmark for different fonts. The model performs best on Arial (40 correct predictions) and Times New Roman (33 correct predictions), while struggling with fonts like Calibri (0 correct predictions), Pacifico (0 correct predictions), and Satisfy (0 correct predictions). The total number of experimental trials for each font is 40.

**ZH** 图 17：Gemini-2.0-Flash-001 在简单基准上对不同字体的正确预测数量。该模型在 Arial（40 次正确预测）与 Times New Roman（33 次正确预测）上表现最好，而在 Calibri（0 次正确预测）、Pacifico（0 次正确预测）与 Satisfy（0 次正确预测）等字体上表现吃力。每种字体的实验总次数为 40。

<!-- [原子块 · object]  -->

**EN** Figure 18: Number of correct predictions made by Gemini-2.0-Flash-001 on the Hard Benchmark for different fonts. The model performs best on Arial (24 correct predictions) and Times New Roman (20 correct predictions), while struggling with fonts like Baskervville SC (0 correct predictions), Satisfy (0 correct predictions), and Vera (0 correct predictions). The total number of experimental trials for each font is 60.

**ZH** 图 18：Gemini-2.0-Flash-001 在困难基准上对不同字体的正确预测数量。该模型在 Arial（24 次正确预测）与 Times New Roman（20 次正确预测）上表现最好，而在 Baskervville SC（0 次正确预测）、Satisfy（0 次正确预测）与 Vera（0 次正确预测）等字体上表现吃力。每种字体的实验总次数为 60。

<!-- [原子块 · object]  -->

**EN** Figure 19: Number of correct predictions made by Llama-3.2-90B-Vision-Instruct on the Easy Benchmark for different fonts. The model performs best on Pacifico (23 correct predictions) and Times New Roman (21 correct predictions), while struggling with fonts like Calibri (0 correct predictions), Consola (0 correct predictions), and Georgia (0 correct predictions). The total number of experimental trials for each font is 40.

**ZH** 图 19：Llama-3.2-90B-Vision-Instruct 在简单基准上对不同字体的正确预测数量。该模型在 Pacifico（23 次正确预测）与 Times New Roman（21 次正确预测）上表现最好，而在 Calibri（0 次正确预测）、Consola（0 次正确预测）与 Georgia（0 次正确预测）等字体上表现吃力。每种字体的实验总次数为 40。

<!-- [原子块 · object]  -->

**EN** Figure 20: Number of correct predictions made by Llama-3.2-90B-Vision-Instruct on the Hard Benchmark for different fonts. The model performs best on Arial (19 correct predictions) and Helvetica (12 correct predictions), while struggling with fonts like Baskervville SC (0 correct predictions), Satisfy (0 correct predictions), and Lobster (0 correct predictions). The total number of experimental trials for each font is 60.

**ZH** 图 20：Llama-3.2-90B-Vision-Instruct 在困难基准上对不同字体的正确预测数量。该模型在 Arial（19 次正确预测）与 Helvetica（12 次正确预测）上表现最好，而在 Baskervville SC（0 次正确预测）、Satisfy（0 次正确预测）与 Lobster（0 次正确预测）等字体上表现吃力。每种字体的实验总次数为 60。

<!-- [原子块 · object]  -->

**EN** Figure 21: Number of correct predictions made by Llama-3.2-11B-Vision-Instruct on the Easy Benchmark for different fonts. The model performs best on Times New Roman (24 correct predictions) and Monoton (18 correct predictions), while struggling with fonts like Calibri (0 correct predictions), Consola (0 correct predictions), and Vera (0 correct predictions). The total number of experimental trials for each font is 40.

**ZH** 图 21：Llama-3.2-11B-Vision-Instruct 在简单基准上对不同字体的正确预测数量。该模型在 Times New Roman（24 次正确预测）与 Monoton（18 次正确预测）上表现最好，而在 Calibri（0 次正确预测）、Consola（0 次正确预测）与 Vera（0 次正确预测）等字体上表现吃力。每种字体的实验总次数为 40。

<!-- [原子块 · object]  -->

**EN** Figure 22: Number of correct predictions made by Llama-3.2-11B-Vision-Instruct on the Hard Benchmark for different fonts. The model performs best on Arial (18 correct predictions) and Times New Roman (15 correct predictions), while struggling with fonts like Roboto Slab (2 correct predictions), Satisfy (2 correct predictions), and Vera (2 correct predictions). The total number of experimental trials for each font is 60.

**ZH** 图 22：Llama-3.2-11B-Vision-Instruct 在困难基准上对不同字体的正确预测数量。该模型在 Arial（18 次正确预测）与 Times New Roman（15 次正确预测）上表现最好，而在 Roboto Slab（2 次正确预测）、Satisfy（2 次正确预测）与 Vera（2 次正确预测）等字体上表现吃力。每种字体的实验总次数为 60。

<!-- [原子块 · object]  -->

**EN** Figure 23: Number of correct predictions made by Qwen2-VL-72B-Instruct on the Easy Benchmark for different fonts. The model performs best on Arial (40 correct predictions) and Times New Roman (4 correct predictions), while struggling with all remaining fonts. The total number of experimental trials for each font is 40.

**ZH** 图 23：Qwen2-VL-72B-Instruct 在简单基准上对不同字体的正确预测数量。该模型在 Arial（40 次正确预测）与 Times New Roman（4 次正确预测）上表现最好，而在其余所有字体上表现吃力。每种字体的实验总次数为 40。

<!-- [原子块 · object]  -->

**EN** Figure 24: Number of correct predictions made by Qwen2-VL-72B-Instruct on the Hard Benchmark for different fonts. The model performs best on Arial (9 correct predictions) and Helvetica (8 correct predictions), while struggling with fonts like Baskervville SC (0 correct predictions), Great Vibes (0 correct predictions), and Vera (0 correct predictions). The total number of experimental trials for each font is 60.

**ZH** 图 24：Qwen2-VL-72B-Instruct 在困难基准上对不同字体的正确预测数量。该模型在 Arial（9 次正确预测）与 Helvetica（8 次正确预测）上表现最好，而在 Baskervville SC（0 次正确预测）、Great Vibes（0 次正确预测）与 Vera（0 次正确预测）等字体上表现吃力。每种字体的实验总次数为 60。

<!-- [原子块 · object]  -->

**EN** Figure 25: Number of correct predictions made by Qwen2-VL-7B-Instruct on the Easy Benchmark for different fonts. The model performs best on Arial (14 correct predictions) and Great Vibes (6 correct predictions), while struggling with fonts like Calibri (0 correct predictions), Consola (0 correct predictions), and Georgia (0 correct predictions). The total number of experimental trials for each font is 40.

**ZH** 图 25：Qwen2-VL-7B-Instruct 在简单基准上对不同字体的正确预测数量。该模型在 Arial（14 次正确预测）与 Great Vibes（6 次正确预测）上表现最好，而在 Calibri（0 次正确预测）、Consola（0 次正确预测）与 Georgia（0 次正确预测）等字体上表现吃力。每种字体的实验总次数为 40。

<!-- [原子块 · object]  -->

**EN** Figure 26: Number of correct predictions made by Qwen2-VL-7B-Instruct on the Hard Benchmark for different fonts. The model performs best on Arial (5 correct predictions), while struggling with fonts like Baskervville SC (2 correct predictions), and Satisfy (2 correct predictions). The total number of experimental trials for each font is 60.

**ZH** 图 26：Qwen2-VL-7B-Instruct 在困难基准上对不同字体的正确预测数量。该模型在 Arial（5 次正确预测）上表现最好，而在 Baskervville SC（2 次正确预测）与 Satisfy（2 次正确预测）等字体上表现吃力。每种字体的实验总次数为 60。

<!-- [原子块 · object]  -->

**EN** Figure 27: Number of correct predictions made by Qwen2.5-VL-7B-Instruct on the Easy Benchmark for different fonts. The model performs best on Arial (23 correct predictions) and Pacifico (14 correct predictions), while struggling with fonts like Lobster (0 correct predictions), Monoton (0 correct predictions), and Vera (0 correct predictions). The total number of experimental trials for each font is 40.

**ZH** 图 27：Qwen2.5-VL-7B-Instruct 在简单基准上对不同字体的正确预测数量。该模型在 Arial（23 次正确预测）与 Pacifico（14 次正确预测）上表现最好，而在 Lobster（0 次正确预测）、Monoton（0 次正确预测）与 Vera（0 次正确预测）等字体上表现吃力。每种字体的实验总次数为 40。

<!-- [原子块 · object]  -->

**EN** Figure 28: Number of correct predictions made by Qwen2.5-VL-7B-Instruct on the Hard Benchmark for different fonts. The model performs best on Arial (7 correct predictions) and Pacifico (6 correct predictions), while struggling with fonts like Baskervville SC (2 correct predictions), Great Vibes (2 correct predictions), and Monoton (2 correct predictions). The total number of experimental trials for each font is 60.

**ZH** 图 28：Qwen2.5-VL-7B-Instruct 在困难基准上对不同字体的正确预测数量。该模型在 Arial（7 次正确预测）与 Pacifico（6 次正确预测）上表现最好，而在 Baskervville SC（2 次正确预测）、Great Vibes（2 次正确预测）与 Monoton（2 次正确预测）等字体上表现吃力。每种字体的实验总次数为 60。

<!-- [原子块 · object]  -->

**EN** Figure 29: Number of correct predictions made by Idefics3-8B-Llama3 on the Easy Benchmark for different fonts. The model performs best on Times New Roman (14 correct predictions) and Calibri (7 correct predictions), while struggling with fonts like Consola (0 correct predictions), Monoton (0 correct predictions), and Vera (0 correct predictions). The total number of experimental trials for each font is 40.

**ZH** 图 29：Idefics3-8B-Llama3 在简单基准上对不同字体的正确预测数量。该模型在 Times New Roman（14 次正确预测）与 Calibri（7 次正确预测）上表现最好，而在 Consola（0 次正确预测）、Monoton（0 次正确预测）与 Vera（0 次正确预测）等字体上表现吃力。每种字体的实验总次数为 40。

<!-- [原子块 · object]  -->

**EN** Figure 30: Number of correct predictions made by Idefics3-8B-Llama3 on the Hard Benchmark for different fonts. The model performs best on Times New Roman (6 correct predictions), while struggling with fonts like Baskervville SC (0 correct predictions). The total number of experimental trials for each font is 60.

**ZH** 图 30：Idefics3-8B-Llama3 在困难基准上对不同字体的正确预测数量。该模型在 Times New Roman（6 次正确预测）上表现最好，而在 Baskervville SC（0 次正确预测）等字体上表现吃力。每种字体的实验总次数为 60。

<!-- [原子块 · img]  -->

**EN** Figure 31: Visualization of attention weights from six cross-attention layers of Llama-3.2-11B-Vision-Instruct (averaged across all attention heads), illustrating the progression of attention across the model’s layers.

**ZH** 图 31：Llama-3.2-11B-Vision-Instruct 六个交叉注意力层的注意力权重可视化（在所有注意力头上取平均），展示注意力随模型层级的演变。

<!-- [原子块 · img]  -->

**EN** Figure 32: Visualization of attention weights from six cross-attention layers of Llama-3.2-11B-Vision-Instruct (averaged across all attention heads), illustrating the progression of attention across the model’s layers.

**ZH** 图 32：Llama-3.2-11B-Vision-Instruct 六个交叉注意力层的注意力权重可视化（在所有注意力头上取平均），展示注意力随模型层级的演变。

<!-- [原子块 · img]  -->

**EN** Figure 33: Visualization of attention weights from six cross-attention layers of Llama-3.2-11B-Vision-Instruct (averaged across all attention heads), illustrating the progression of attention across the model’s layers.

**ZH** 图 33：Llama-3.2-11B-Vision-Instruct 六个交叉注意力层的注意力权重可视化（在所有注意力头上取平均），展示注意力随模型层级的演变。

<!-- [原子块 · img]  -->

**EN** Figure 34: Visualization of attention weights from six cross-attention layers of Llama-3.2-11B-Vision-Instruct (averaged across all attention heads), illustrating the progression of attention across the model’s layers.

**ZH** 图 34：Llama-3.2-11B-Vision-Instruct 六个交叉注意力层的注意力权重可视化（在所有注意力头上取平均），展示注意力随模型层级的演变。

<!-- [原子块 · img]  -->

**EN** Figure 35: Visualization of attention weights from six cross-attention layers of Llama-3.2-11B-Vision-Instruct (averaged across all attention heads), illustrating the progression of attention across the model’s layers.

**ZH** 图 35：Llama-3.2-11B-Vision-Instruct 六个交叉注意力层的注意力权重可视化（在所有注意力头上取平均），展示注意力随模型层级的演变。

<!-- [原子块 · img]  -->

**EN** Figure 36: Visualization of attention weights from six cross-attention layers of Llama-3.2-11B-Vision-Instruct (averaged across all attention heads), illustrating the progression of attention across the model’s layers.

**ZH** 图 36：Llama-3.2-11B-Vision-Instruct 六个交叉注意力层的注意力权重可视化（在所有注意力头上取平均），展示注意力随模型层级的演变。

<!-- [原子块 · img]  -->

**EN** Figure 37: Visualization of attention weights from six cross-attention layers of Llama-3.2-11B-Vision-Instruct (averaged across all attention heads), illustrating the progression of attention across the model’s layers.

**ZH** 图 37：Llama-3.2-11B-Vision-Instruct 六个交叉注意力层的注意力权重可视化（在所有注意力头上取平均），展示注意力随模型层级的演变。

<!-- [原子块 · img]  -->

**EN** Figure 38: Visualization of attention weights from six cross-attention layers of Llama-3.2-11B-Vision-Instruct (averaged across all attention heads), illustrating the progression of attention across the model’s layers.

**ZH** 图 38：Llama-3.2-11B-Vision-Instruct 六个交叉注意力层的注意力权重可视化（在所有注意力头上取平均），展示注意力随模型层级的演变。

<!-- [原子块 · img]  -->

**EN** Figure 39: Visualization of attention weights from six cross-attention layers of Llama-3.2-11B-Vision-Instruct (averaged across all attention heads), illustrating the progression of attention across the model’s layers.

**ZH** 图 39：Llama-3.2-11B-Vision-Instruct 六个交叉注意力层的注意力权重可视化（在所有注意力头上取平均），展示注意力随模型层级的演变。

<!-- [原子块 · img]  -->

**EN** Figure 40: Visualization of attention weights from six cross-attention layers of Llama-3.2-11B-Vision-Instruct (averaged across all attention heads), illustrating the progression of attention across the model’s layers.

**ZH** 图 40：Llama-3.2-11B-Vision-Instruct 六个交叉注意力层的注意力权重可视化（在所有注意力头上取平均），展示注意力随模型层级的演变。

<!-- [原子块 · img]  -->

**EN** Figure 41: Visualization of attention weights from the 17th layer to the final attention layer of Qwen2-VL-7B-Instruct (averaged across all attention heads), illustrating the progression of attention across the model’s layers.

**ZH** 图 41：Qwen2-VL-7B-Instruct 从第 17 层到最后一个注意力层的注意力权重可视化（在所有注意力头上取平均），展示注意力随模型层级的演变。

<!-- [原子块 · img]  -->

**EN** Figure 42: Visualization of attention weights from the 17th layer to the final attention layer of Qwen2-VL-7B-Instruct (averaged across all attention heads), illustrating the progression of attention across the model’s layers.

**ZH** 图 42：Qwen2-VL-7B-Instruct 从第 17 层到最后一个注意力层的注意力权重可视化（在所有注意力头上取平均），展示注意力随模型层级的演变。

<!-- [原子块 · img]  -->

**EN** Figure 43: Visualization of attention weights from the 17th layer to the final attention layer of Qwen2-VL-7B-Instruct (averaged across all attention heads), illustrating the progression of attention across the model’s layers.

**ZH** 图 43：Qwen2-VL-7B-Instruct 从第 17 层到最后一个注意力层的注意力权重可视化（在所有注意力头上取平均），展示注意力随模型层级的演变。

<!-- [原子块 · img]  -->

**EN** Figure 44: Visualization of attention weights from the 17th layer to the final attention layer of Qwen2-VL-7B-Instruct (averaged across all attention heads), illustrating the progression of attention across the model’s layers.

**ZH** 图 44：Qwen2-VL-7B-Instruct 从第 17 层到最后一个注意力层的注意力权重可视化（在所有注意力头上取平均），展示注意力随模型层级的演变。

<!-- [原子块 · img]  -->

**EN** Figure 45: Visualization of attention weights from the 17th layer to the final attention layer of Qwen2-VL-7B-Instruct (averaged across all attention heads), illustrating the progression of attention across the model’s layers.

**ZH** 图 45：Qwen2-VL-7B-Instruct 从第 17 层到最后一个注意力层的注意力权重可视化（在所有注意力头上取平均），展示注意力随模型层级的演变。

<!-- [原子块 · img]  -->

**EN** Figure 46: Visualization of attention weights from the 17th layer to the final attention layer of Qwen2-VL-7B-Instruct (averaged across all attention heads), illustrating the progression of attention across the model’s layers.

**ZH** 图 46：Qwen2-VL-7B-Instruct 从第 17 层到最后一个注意力层的注意力权重可视化（在所有注意力头上取平均），展示注意力随模型层级的演变。

<!-- [原子块 · img]  -->

**EN** Figure 47: Visualization of attention weights from the 17th layer to the final attention layer of Qwen2-VL-7B-Instruct (averaged across all attention heads), illustrating the progression of attention across the model’s layers.

**ZH** 图 47：Qwen2-VL-7B-Instruct 从第 17 层到最后一个注意力层的注意力权重可视化（在所有注意力头上取平均），展示注意力随模型层级的演变。
