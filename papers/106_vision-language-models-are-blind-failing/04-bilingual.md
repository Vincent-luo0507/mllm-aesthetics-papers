# 视觉语言模型是「盲」的：无法把精细的视觉特征转译为文字

> 原标题：Vision language models are blind: Failing to translate detailed visual features into words
> 作者：Pooyan Rahmanzadehgervi, Logan Bolton, Mohammad Reza Taesiri, Anh Totti Nguyen · arXiv:2407.06581 · 2024-07-09

<!-- [原子块 · verbatim] Vision language models are blind: Failing to translate detailed visual features into words -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] While large language models with vision capabilities (VLMs), e.g . , GPT- 4o and Gemini- 1.5 Pro , score high on many vision-understanding benchmarks, they are still struggling with low-level vision t -->

**EN** Keywords:

**ZH** 关键词：

**EN** 1 Introduction

**ZH** 1 引言

**EN** The advent of VLMs, starting with GPT-4V(ision) [39], has enabled numerous, unprecedented image-text processing applications [53]. VLMs can accurately identify objects in a scene [42, 9, 53] and perform complex tasks based on these detected objects, e.g., calculating the cost of beers on a table from an image of the scene and an image of the menu [54]. Interestingly, VLMs advance so quickly that describing unusual activities in an image [46] (e.g., a man ironing on a moving taxi) has become a standard sanity check [10].

**ZH** 自 GPT-4V(ision) [39] 问世以来，视觉语言模型（VLM）催生了大量前所未有的图文处理应用 [53]。VLM 能准确识别场景中的物体 [42, 9, 53]，并基于这些被检测到的物体完成复杂任务，例如根据场景照片与菜单照片计算桌上啤酒的价格 [54]。有意思的是，VLM 的进展之快，以至于描述图像中的异常活动 [46]（例如一名男子在行驶的出租车上熨衣服）已经成为一种常规的有效性检验 [10]。

**EN** Existing VLM benchmarks cover a wide range of tasks [57, 18, 30]. However, they often assess a high-level human-vs-machine performance gap conflating both visual and non-visual abilities. Interestingly, the input images in so many questions, e.g., 42.9% of MMMU [57], are not even necessary [6] for determining the correct answer. Many answers (1) can be inferred from the textual question and choices alone [6, 13]; and (2) are memorized by VLMs from their Internet-scale training [6]. In contrast, it is important to exclusively measure the visual capabilities of VLMs, independent of their strong language abilities.

**ZH** 现有的 VLM 基准覆盖了广泛的任务 [57, 18, 30]。然而，它们衡量的往往是人与机器之间的高层性能差距，把视觉能力与非视觉能力混为一谈。有意思的是，在如此多的问题中——例如 MMMU [57] 中的 42.9%——输入图像对判定正确答案而言甚至并非必要 [6]。许多答案（1）仅凭文本问题与选项即可推出 [6, 13]；（2）由 VLM 从互联网规模的训练中记住 [6]。相比之下，独立于其强大的语言能力、专门度量 VLM 视觉能力，就显得十分重要。

**EN** In this paper, we test VLMs’ ability to see (not reasoning) on low-level vision tasks inspired by the “visual acuity” tests [5] given to humans by optometrists. We test four state-of-the-art (SOTA) VLMs: GPT-4o [38], Gemini-1.5 Pro [43], Claude-3 Sonnet [4], and Claude-3.5 Sonnet [2] on our suite of 7 extremely simple visual tasks that involve only 2D geometric primitives (e.g., lines and circles) [14] and require minimal world knowledge. Our key findings are:

**ZH** 本文受验光师为人类所做的「视敏度」测试 [5] 启发，用低层视觉任务来检验 VLM「看见」（而非推理）的能力。我们在 7 项极简单的视觉任务上测试四款当前最优（SOTA）的 VLM：GPT-4o [38]、Gemini-1.5 Pro [43]、Claude-3 Sonnet [4] 与 Claude-3.5 Sonnet [2]。这些任务只涉及二维几何图元（例如直线与圆）[14]，且只需极少的世界知识。我们的核心发现如下：

**EN** 1. Despite excellent performance on chart and diagram benchmarks [38, 4], VLMs cannot reliably tell whether two lines (or two circles) are intersecting, especially when close together. Accuracy in detecting 0, 1 or 2 intersections in a line chart ⟦SLOT_0⟧ of two 2-segment piecewise-linear functions ranges from ⟦SLOT_1⟧41% to 76% (Sec. 4.1). For the two-circle ⟦SLOT_2⟧ ⟦SLOT_3⟧ task, VLMs perform better (⟦SLOT_4⟧75–93% accuracy), but still far from the expected 100% (Sec. 4.2).

**ZH** 1. 尽管在图表与示意图基准上表现出色 [38, 4]，VLM 却无法可靠判断两条线（或两个圆）是否相交，尤其当二者靠得很近时。在折线图 ⟦SLOT_0⟧ 中判断两条两段分段线性函数的交点为 0、1 还是 2，准确率介于 ⟦SLOT_1⟧41% 到 76% 之间（第 4.1 节）。对两圆 ⟦SLOT_2⟧ ⟦SLOT_3⟧ 任务，VLM 表现更好（⟦SLOT_4⟧75–93% 准确率），但仍远未达到预期的 100%（第 4.2 节）。

**EN** 2. VLMs can perfectly recognize a circle (⟦SLOT_5⟧) and a word ( Subdermatoglyphic ) separately. Yet, when the circle is superimposed on the word (⟦SLOT_6⟧), models tend to struggle to identify which letter is being circled (Sec. 4.3).

**ZH** 2. VLM 能分别完美识别一个圆（⟦SLOT_5⟧）和一个单词（ Subdermatoglyphic ）。然而，一旦把圆叠加到单词上（⟦SLOT_6⟧），模型往往难以辨认被圈出的是哪个字母（第 4.3 节）。

**EN** 3. VLMs can accurately count shapes, e.g., circles ( ○ ), that are disjoint and far apart. However, all VLMs struggle to count intersecting circles ⟦SLOT_7⟧ (like the Olympic logo), and, generally, primitive shapes ( ○ , ⟦SLOT_8⟧ , ⬠ ) that are overlapping or nested (Sec. 4.4).

**ZH** 3. VLM 能准确清点彼此分离、相距较远的形状，例如圆（ ○ ）。然而，所有 VLM 都难以清点相交的圆 ⟦SLOT_7⟧（如奥运标志那样），也难以清点一般意义上相互重叠或嵌套的图元形状（ ○ ，⟦SLOT_8⟧ ， ⬠ ）（第 4.4 节）。

**EN** 4. Tiling up squares into a grid ⟦SLOT_9⟧ , we find VLMs to fail to count the number of rows or columns in the grid, whether empty or containing text (Sec. 4.5). This is in stark contrast to VLM high performance (⟦SLOT_10⟧ 90% accuracy) [38, 43] on DocVQA [31], which includes many questions with tables.

**ZH** 4. 把正方形平铺成网格 ⟦SLOT_9⟧ 后，我们发现 VLM 无法数清网格的行数或列数，无论格子为空还是含有文字（第 4.5 节）。这与 VLM 在 DocVQA [31] 上的高表现（⟦SLOT_10⟧ 90% 准确率）[38, 43] 形成鲜明反差——DocVQA 包含大量涉及表格的问题。

**EN** 5. When tasked with tracing colored paths in a simplified subway map of only 2 to 8 paths and a total of 4 stations, VLMs often fail to count the paths between two stations, i.e., with an accuracy of ⟦SLOT_11⟧31% to 58% (Sec. 4.6).

**ZH** 5. 在仅有 2 至 8 条线路、共 4 个车站的简化地铁图里追踪彩色线路时，VLM 常常数错两站之间的线路数，准确率仅为 ⟦SLOT_11⟧31% 到 58%（第 4.6 节）。

**EN** 6. GPT-4o is better than Gemini-1.5 Pro on 7 existing complex VLM benchmarks [38, 43] but worse on BlindTest. On average across all 7 tasks, VLMs perform at 58.07% accuracy with Sonnet-3.5 being the best (77.84% accuracy), which is still far lower than the expected 100% accuracy of humans (see Tab. 1). In sum, BlindTest reveals some remarkable VLM limitations that are not measured in prior benchmarks.

**ZH** 6. GPT-4o 在 7 个现有复杂 VLM 基准上优于 Gemini-1.5 Pro [38, 43]，在 BlindTest 上却更差。在全部 7 项任务上平均，VLM 的准确率为 58.07%，Sonnet-3.5 最好（77.84% 准确率），仍远低于人类预期的 100%（见表 1）。总之，BlindTest 揭示出一些此前的基准未能度量的、颇为显著的 VLM 局限。

**EN** 7. The SOTA “slow-thinking” VLMs are at best on par with the regular VLMs on BlindTest (71.59% vs. 72.75%; Sec. 4.7), i.e., longer inference is not immediately addressing the low-level visual challenge posed by BlindTest.

**ZH** 7. 在 BlindTest 上，当前最优的「慢思考」VLM 至多与常规 VLM 持平（71.59% 对 72.75%；第 4.7 节），即更长的推理并不能立刻解决 BlindTest 提出的低层视觉挑战。

**EN** 8. Most VLMs perform better (with some reaching ⟦SLOT_12⟧100% accuracy) on simplified versions of BlindTest (Sec. 5) where we increasingly add more space between letters (Sec. 5.1) or between shapes (Sec. 5.2), and gradually reduce the number of turns in subway maps (Sec. 5.3). For instance, LLaVA-OneV-72B-ov and Sonnet-3’s accuracy is increased by +20 and +63 on the circled-letter task and counting overlapping circles, respectively, when the images are simplified.

**ZH** 8. 在 BlindTest 的简化版本中（第 5 节），多数 VLM 表现更好（部分达到 ⟦SLOT_12⟧100% 准确率）——我们逐步增加字母之间（第 5.1 节）或形状之间（第 5.2 节）的间距，并逐步减少地铁图中的转折数（第 5.3 节）。例如，当图像被简化后，LLaVA-OneV-72B-ov 与 Sonnet-3 在被圈字母任务与清点重叠圆任务上的准确率分别提升了 +20 与 +63。

**EN** 9. Linear-probing the features of the vision encoders before and after the projection layer in the smallest open-source VLMs (LLaVA-OneV-S and Phi-3.5) shows that these vision encoders already contain sufficient information to solve the two-circle ⟦SLOT_13⟧ and counting the intersections in the line chart ⟦SLOT_14⟧ tasks with ⟦SLOT_15⟧99.47% accuracy (Sec. 6). That is, the challenge lies in decoding the visual information into the correct language outputs.

**ZH** 9. 对最小的开源 VLM（LLaVA-OneV-S 与 Phi-3.5）在投影层前后的视觉编码器特征做线性探测显示，这些视觉编码器已包含足以解决两圆 ⟦SLOT_13⟧ 与折线图交点计数 ⟦SLOT_14⟧ 任务的信息，准确率达 ⟦SLOT_15⟧99.47%（第 6 节）。也就是说，挑战在于把视觉信息解码为正确的语言输出。

<!-- [原子块 · svg]  -->

**EN** Figure 1: VLMs fail on the simple tasks of BlindTest.

**ZH** 图 1：VLM 在 BlindTest 的简单任务上失败。

**EN** 2 Vision language models

**ZH** 2 视觉语言模型

**EN** Our goal is to evaluate how SOTA VLMs perceive simple images composed of interacting geometric primitives.

**ZH** 我们的目标是评估当前最优的 VLM 如何感知由相互作用的几何图元构成的简单图像。

**EN** 4 commercial We test four SOTA models: GPT-4o ( ), Gemini-1.5 Pro ( Gemini-1.5), Claude-3 Sonnet ( Sonnet-3), and Claude-3.5 Sonnet (⟦SLOT_16⟧ Sonnet-3.5) that are ranking highest on 7 recent vision-language benchmarks (see [38] and Table 10 in [43]), which cover multi-discipline, college-level subjects in MMMU [57], science diagrams in AI2D [18], mathematics in MathVista [27], charts in ChartQA [30], documents in DocVQA [31], and videos in ActivityNet-QA [56] & EgoSchema [28]. We initially run experiments with Claude 3 Opus [3] but swap it with Sonnet-3.5, which performs more accurately on BlindTest and costs 5⟦SLOT_17⟧ less. All models tested are described in App. 0.A.

**ZH** 4 款商用模型：我们测试四款 SOTA 模型：GPT-4o（ ）、Gemini-1.5 Pro（ Gemini-1.5）、Claude-3 Sonnet（ Sonnet-3）与 Claude-3.5 Sonnet（⟦SLOT_16⟧ Sonnet-3.5），它们在 7 个近期视觉语言基准上排名最高（见 [38] 与 [43] 中的表 10），涵盖 MMMU [57] 的多学科大学水平科目、AI2D [18] 的科学示意图、MathVista [27] 的数学、ChartQA [30] 的图表、DocVQA [31] 的文档，以及 ActivityNet-QA [56] 与 EgoSchema [28] 的视频。我们最初用 Claude 3 Opus [3] 做实验，后换成 Sonnet-3.5——后者在 BlindTest 上更准确，且成本仅为其 5⟦SLOT_17⟧ 分之一。所有受测模型的说明见附录 0.A。

**EN** 8 open-source For completeness, we also test 8 open-source models of varying sizes (from 0.5B to 72B parameters) across three different families: LLaVA OneVision-qwen2 (⟦SLOT_18⟧ LLaVA-OneV) [20], Phi-3.5-vision-instruct (⟦SLOT_19⟧ Phi-3.5) [1], and InternVL-2 [7]. Yet, they underperform the four closed-source models described above (see results in App. 0.C).

**ZH** 8 款开源模型：为完备起见，我们还测试了 8 款不同规模（参数量从 0.5B 到 72B）、分属三个系列的开源模型：LLaVA OneVision-qwen2（⟦SLOT_18⟧ LLaVA-OneV）[20]、Phi-3.5-vision-instruct（⟦SLOT_19⟧ Phi-3.5）[1] 与 InternVL-2 [7]。不过它们的表现不及上述四款闭源模型（结果见附录 0.C）。

**EN** 2 slow-thinking Given that BlindTest intuitively does not require slow, iterative thinking, our main goal is to evaluate standard VLMs (e.g., GPT-4o instead of GPT-o1). However, for completeness, we also test two slow-thinking models [17]: A closed-source Gemini 2.0 Flash-Thinking and an open-source QVQ-Preview (QVQ) [51, 48] (Sec. 4.7). However, these models generally do not outperform standard ones on BlindTest, supporting our hypothesis that BlindTest is a low-level visual task that does not require high-level reasoning.

**ZH** 2 款慢思考模型：鉴于 BlindTest 直观上并不需要缓慢、迭代式的思考，我们的主要目标是评估标准 VLM（例如 GPT-4o 而非 GPT-o1）。不过为完备起见，我们也测试了两款慢思考模型 [17]：闭源的 Gemini 2.0 Flash-Thinking 与开源的 QVQ-Preview（QVQ）[51, 48]（第 4.7 节）。然而，这些模型在 BlindTest 上总体并未超过标准模型，支持了我们的假设：BlindTest 是一项不需要高层推理的低层视觉任务。

**EN** 3 BlindTest benchmark of 7 tasks

**ZH** 3 含 7 项任务的 BlindTest 基准

**EN** Eye exams Like humans’ visual acuity tests [5], we design a set of 7 very simple, yet novel tasks that are composed of common geometric primitives. We do not use the existing tests designed for human-eye exams for two reasons. First, we avoid using the questions that exist on the Internet, which may provide an inflated measure of vision capabilities [55, 6, 13]. Second, our preliminary experiments show that GPT-4o already performs very well on humans’ eye exams, which typically contain single, separate symbols—e.g., the Snellen chart [5], tumbling E [5], and contrast sensitivity charts [29, 15]. Motivation Our BlindTest benchmark tests VLMs on identifying known geometric primitives when they are close together, overlapping, or intersecting. We hypothesize that VLMs will struggle because they mostly rely on “late fusion” [25, 47], i.e., first extracting visual representations without considering the textual question, and then feeding them to a large language model (LLM) for processing. Therefore, while geometric primitives in BlindTest are well known, their exact spatial information on a white canvas (e.g., the size and position of a ○ ) is typically not describable in natural language, even for humans, and may not be captured by the vision encoders trained mostly on natural images. Controls For each test image, we prompt VLMs using two different, yet semantically equivalent questions. Furthermore, we test VLMs on multiple versions of each task across three different image sizes (Secs. 3.1, 3.2, 3.4, 3.6 and 3.7) and two to three line thickness values (Secs. 3.1, 3.5, 3.4, 3.6 and 3.7).

**ZH** 视力检查：如同人类的视敏度测试 [5]，我们设计了一组 7 项非常简单却新颖的任务，它们由常见的几何图元构成。我们没有采用为人类视力检查设计的现成测试，原因有二。第一，我们避免使用互联网上已有的题目，因为那可能给出被抬高的视觉能力度量 [55, 6, 13]。第二，我们的初步实验显示，GPT-4o 在人类视力检查上的表现已经很好，而这类检查通常只含单个、彼此分离的符号——例如斯内伦视力表 [5]、翻滚 E 字表 [5] 与对比敏感度图 [29, 15]。动机：我们的 BlindTest 基准检验 VLM 在几何图元彼此靠近、重叠或相交时识别它们的能力。我们假设 VLM 会表现吃力，因为它们大多依赖「后期融合」[25, 47]，即先在不考虑文本问题的情况下提取视觉表征，再将其送入大语言模型（LLM）处理。因此，尽管 BlindTest 中的几何图元广为人知，它们在白色画布上的精确空间信息（例如一个 ○ 的大小与位置）通常无法用自然语言描述——即便对人类也是如此——也可能未被主要用自然图像训练的视觉编码器所捕捉。控制项：对每张测试图像，我们用两种措辞不同但语义等价的问题提示 VLM。此外，我们在三种不同图像尺寸（第 3.1、3.2、3.4、3.6 与 3.7 节）与两到三种线条粗细取值（第 3.1、3.5、3.4、3.6 与 3.7 节）下，对每项任务的多个版本测试 VLM。

**EN** 3.1 Task 1: Counting line intersections ⟦SLOT_20⟧

**ZH** 3.1 任务 1：数直线交点 ⟦SLOT_20⟧

**EN** Given the impressive accuracy of VLMs on answering questions on diagrams and charts (e.g., Sonnet-3.5 scoring 94.7% on AI2D and 90.8% on ChartQA) [2], a reasonable hypothesis is that VLMs must be able to see if two graphs intersect in a chart. Here, we test this hypothesis by asking VLMs to count the number of intersections (0, 1 or 2) between two 2-segment piece-wise linear functions.

**ZH** 鉴于 VLM 在回答示意图与图表问题上的准确率令人印象深刻（例如 Sonnet-3.5 在 AI2D 上得 94.7%、在 ChartQA 上得 90.8%）[2]，一个合理的假设是：VLM 必定能看出图表中两条曲线是否相交。这里我们通过让 VLM 数两条两段分段线性函数之间交点（0、1 或 2）的个数来检验这一假设。

**EN** Images We create 1,800 images (Fig. F21) of 2D line plots drawn on an image of size of ⟦SLOT_21⟧, where ⟦SLOT_22⟧. Each line plot consists of two line segments, defined by three points whose x-coordinates are fixed at ⟦SLOT_23⟧px (see Fig. F21). The y-coordinates are randomly sampled from a pre-defined, invisible 12⟦SLOT_24⟧12 grid to ensure there is sufficient spacing between two plots and that there are exactly 0, 1 or 2 intersections. See Sec. 0.H.1 for more details.

**ZH** 图像：我们生成 1,800 张二维折线图（图 F21），绘制在尺寸为 ⟦SLOT_21⟧ 的图像上，其中 ⟦SLOT_22⟧。每张折线图由两条线段构成，由 x 坐标固定为 ⟦SLOT_23⟧px 的三个点定义（见图 F21）。y 坐标从一个预定义的、不可见的 12⟦SLOT_24⟧12 网格中随机采样，以保证两张图之间有足够的间距，且恰好存在 0、1 或 2 个交点。详见第 0.H.1 节。

**EN** 3.2 Task 2: Two circles ⟦SLOT_25⟧

**ZH** 3.2 任务 2：两个圆 ⟦SLOT_25⟧

**EN** In the task of counting line intersections (Sec. 3.1), each image contains two long, thin colored lines on a large white canvas. Here, we test models in a complementary setting where the two interacting objects (here, two same-sized filled circles ⟦SLOT_26⟧) are larger while their gap is smaller. This task evaluates VLM ability in detecting (1) a small gap between two circles; and (2) that two circles are overlapping, i.e., no gaps. We vary circle and gap sizes and ask VLMs if two circles are (a) overlapping or (b) touching each other.

**ZH** 在数直线交点的任务（第 3.1 节）中，每张图在大幅白色画布上包含两条细长的彩色线。这里我们在互补的设定下测试模型：两个相互作用的物体（此处为两个等大的实心圆 ⟦SLOT_26⟧）更大，而它们之间的间隙更小。该任务考察 VLM 检测（1）两圆之间细小间隙；（2）两圆重叠（即无间隙）的能力。我们改变圆与间隙的大小，询问 VLM 两圆是（a）重叠还是（b）相切。

**EN** Images Given a blank image of size ⟦SLOT_27⟧, we draw two same-sized circles of diameter ⟦SLOT_28⟧ with a boundary-to-boundary distance ⟦SLOT_29⟧ where ⟦SLOT_30⟧ {-0.25, -0.2, -0.15, -0.1, -0.05, 0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5} to cover all three cases: overlapping, tangent, and disjoint (see Fig. F4a). The two circles are arranged in four different orientations, making a ⟦SLOT_31⟧, ⟦SLOT_32⟧, ⟦SLOT_33⟧, and ⟦SLOT_34⟧ angle with the x-axis (Fig. F4b). The whole grid sampling generates 224 images per image size. We replicate the procedure for 3 image sizes, i.e., ⟦SLOT_35⟧ px to create a total of 3⟦SLOT_36⟧224 = 768 images. See Sec. 0.F.1 for more details.

**ZH** 图像：给定一张尺寸为 ⟦SLOT_27⟧ 的空白图像，我们绘制两个直径为 ⟦SLOT_28⟧ 的等大圆，边界到边界的距离为 ⟦SLOT_29⟧，其中 ⟦SLOT_30⟧ 取自 {-0.25, -0.2, -0.15, -0.1, -0.05, 0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5}，以覆盖重叠、相切与分离三种情形（见图 F4a）。两个圆按四种不同朝向排列，与 x 轴分别成 ⟦SLOT_31⟧、⟦SLOT_32⟧、⟦SLOT_33⟧ 与 ⟦SLOT_34⟧ 角（图 F4b）。整套网格采样对每种图像尺寸生成 224 张图像。我们对 3 种图像尺寸（即 ⟦SLOT_35⟧ px）重复该流程，共生成 3⟦SLOT_36⟧224 = 768 张图像。详见第 0.F.1 节。

**EN** 3.3 Task 3: The circled letter ⟦SLOT_37⟧

**ZH** 3.3 任务 3：被圈住的字母 ⟦SLOT_37⟧

**EN** Consistent with prior reports [54, 53, 44], we find that VLMs can 100% accurately identify a primitive shape (e.g., a red circle ⟦SLOT_38⟧) [44] and can perfectly read an English word (e.g., Subdermatoglyphic ) alone. Here, we superimpose the red circle on every letter, one at a time, in the word, and ask VLMs to identify which letter is being circled. While the task is easy to humans, our hypothesis is that if a VLM’s vision is “blurry”, it might not be able to identify the exact letter being circled since there is tiny spacing between the adjacent letters.

**ZH** 与此前报告一致 [54, 53, 44]，我们发现 VLM 能 100% 准确地识别一个图元形状（例如红色圆圈 ⟦SLOT_38⟧）[44]，也能完美读出单独呈现的英文单词（例如 Subdermatoglyphic ）。这里，我们把红圈逐个叠加到单词的每个字母上，并要求 VLM 辨认被圈住的是哪个字母。虽然该任务对人类轻而易举，我们的假设是：若 VLM 的视觉是「模糊」的，它可能无法识别被圈住的究竟是哪个字母，因为相邻字母之间的间距极小。

**EN** Images We choose three strings Acknowledgement , Subdermatoglyphic , and tHyUiKaRbNqWeOpXcZvM because they contain characters of variable widths and heights. Furthermore, all four tested VLMs can read out all characters in these strings when they are input to the models as an image. While Acknowledgement is a common English word, Subdermatoglyphic is the longest word without repetitive letters. We also test VLMs on the random string tHyUiKaRbNqWeOpXcZvM to estimate how much model accuracy is due to its familiarity with the word.

**ZH** 图像：我们选取三个字符串 Acknowledgement 、 Subdermatoglyphic 与 tHyUiKaRbNqWeOpXcZvM ，因为它们包含宽度与高度各异的字符。此外，当这些字符串以图像形式输入时，四款受测 VLM 都能读出其中的所有字符。Acknowledgement 是常见英文单词，Subdermatoglyphic 则是不含重复字母的最长单词。我们还用随机字符串 tHyUiKaRbNqWeOpXcZvM 测试 VLM，以估计模型准确率中有多少来自对该单词的熟悉度。

**EN** For each (string, circled-letter) pair, we render a 512⟦SLOT_39⟧512 image by choosing among 3 red oval line-thickness levels, 2 font families, and 4 different values of image padding for a total of 24 images. That is, we generate 360, 408, and 480 images for Acknowledgement (15 letters), Subdermatoglyphic (17 letters), and tHyUiKaRbNqWeOpXcZvM (20 letters), respectively. We ensure each letter to be circled fits completely the oval ⟦SLOT_40⟧ (see Fig. F10). See Sec. 0.G.1 for more details.

**ZH** 对每个（字符串，被圈字母）组合，我们从 3 档红色椭圆线条粗细、2 种字体族与 4 种不同图像留白取值中选取，渲染出一张 512⟦SLOT_39⟧512 图像，共 24 张。也就是说，我们分别为 Acknowledgement （15 个字母）、 Subdermatoglyphic （17 个字母）与 tHyUiKaRbNqWeOpXcZvM （20 个字母）生成 360、408 与 480 张图像。我们确保每个待圈字母都完整容纳于椭圆 ⟦SLOT_40⟧ 之内（见图 F10）。详见第 0.G.1 节。

**EN** 3.4 Task 4: Counting overlapping shapes ○ ○ ○

**ZH** 3.4 任务 4：清点重叠的形状 ○ ○ ○

**EN** Aligned with prior research [54], we also find VLMs to be able to count disjoint circles ( ○ ○ ○ ). Yet, here, we test VLMs on counting circles that are intersecting ( ○ ○ ○ ) like in the Olympic logo—a common cognitive development exercise for preschoolers [45, 37]. Our hypothesis is that a “blurry” vision may not see the intersection between two circles clearly and therefore unable to trace circles and count them. For generalization of our findings, we repeat the experiment with pentagons ( ⬠ ) as well (instead of circles).

**ZH** 与此前研究一致 [54]，我们也发现 VLM 能够清点彼此分离的圆（ ○ ○ ○ ）。然而在这里，我们测试 VLM 清点相交圆（ ○ ○ ○ ）的能力——如同奥运标志那样，这也是学龄前儿童常见的认知发展练习 [45, 37]。我们的假设是：「模糊」的视觉可能看不清两个圆之间的相交处，因而无法追踪圆并清点它们。为检验结论的泛化性，我们也用五边形（ ⬠ ）重复了该实验（取代圆形）。

**EN** Images In an image of size ⟦SLOT_41⟧, where ⟦SLOT_42⟧px. We draw ⟦SLOT_43⟧ overlapping, same-sized circles arranged in two rows like the Olympic logo (see Fig. F30). A circle diameter ⟦SLOT_44⟧. We repeat the images with two different line thicknesses for rendering circles. This procedure renders 3 resolutions ⟦SLOT_45⟧ 5 values of ⟦SLOT_46⟧ ⟦SLOT_47⟧ 2 diameters ⟦SLOT_48⟧ 2 line widths ⟦SLOT_49⟧ 2 color options = 120 images. We also vertically flip all 120 images, resulting in a total of 240 images. We repeat for pentagons ( ⬠ ) in addition to circles ( ○ ), resulting in 240⟦SLOT_50⟧2 shapes = 480 images in total. For pentagons, their side length ⟦SLOT_51⟧. See Sec. 0.J.1 for more details.

**ZH** 图像：在尺寸为 ⟦SLOT_41⟧ 的图像中，其中 ⟦SLOT_42⟧px。我们绘制 ⟦SLOT_43⟧ 个相互重叠、等大的圆，像奥运标志那样排成两行（见图 F30）。圆的直径为 ⟦SLOT_44⟧。我们用两种不同的线条粗细渲染圆，重复生成图像。该流程产出 3 种分辨率 ⟦SLOT_45⟧、⟦SLOT_46⟧ 的 5 个取值 ⟦SLOT_47⟧、2 种直径 ⟦SLOT_48⟧、2 种线宽 ⟦SLOT_49⟧、2 种配色选项，共 120 张图像。我们又把这 120 张图像全部垂直翻转，得到 240 张。对五边形（ ⬠ ）与圆形（ ○ ）各重复一遍，共 240⟦SLOT_50⟧2 种形状 = 480 张图像。五边形的边长为 ⟦SLOT_51⟧。详见第 0.J.1 节。

**EN** 3.5 Task 5: Counting the nested squares

**ZH** 3.5 任务 5：清点嵌套的正方形

**EN** In addition to testing VLMs on counting the intersecting circles (Sec. 3.4), here, we test a complementary setting by arranging the shapes so that their edges do not intersect. That is, each shape is nested entirely inside another (see Fig. F26). For completeness, we test squares ( ⟦SLOT_52⟧ ) in this task.

**ZH** 除测试 VLM 清点相交圆（第 3.4 节）之外，这里我们通过让形状彼此不产生边相交来测试互补的设定，即每个形状完整嵌套在另一个形状内部（见图 F26）。为完备起见，本任务中我们测试正方形（ ⟦SLOT_52⟧ ）。

**EN** Images In an image of size 1000⟦SLOT_53⟧1000px, we render ⟦SLOT_54⟧ nested squares one at a time from the largest to the smallest. First, the outermost square is rendered using a random edge length ⟦SLOT_55⟧. And each subsequent smaller square is placed randomly inside the previous one and has an edge length of 75% of that of the outer square. We render squares using a line width of ⟦SLOT_56⟧px and ensure no squares touch by edges. For each line width, we generate 10 images (where squares have different, random locations) to create 3 ⟦SLOT_57⟧ 10 = 30 images. Repeating the process for all ⟦SLOT_58⟧ values results in 4 ⟦SLOT_59⟧ 30 = 120 images. See Sec. 0.I.1 for more details.

**ZH** 图像：在 1000⟦SLOT_53⟧1000px 的图像中，我们一次渲染 ⟦SLOT_54⟧ 个嵌套正方形，由大到小。首先，用随机边长 ⟦SLOT_55⟧ 渲染最外层的正方形；随后每个更小的正方形被随机放置在前一个之内，边长为外层正方形的 75%。我们用 ⟦SLOT_56⟧px 的线宽渲染正方形，并确保正方形之间不因边缘而接触。对每种线宽，我们生成 10 张图像（正方形位置各不相同且随机），得到 3 ⟦SLOT_57⟧ 10 = 30 张图像。对所有 ⟦SLOT_58⟧ 取值重复该流程，得到 4 ⟦SLOT_59⟧ 30 = 120 张图像。详见第 0.I.1 节。

**EN** 3.6 Task 6: Counting the rows and columns of a grid ⟦SLOT_60⟧

**ZH** 3.6 任务 6：数网格的行数与列数 ⟦SLOT_60⟧

**EN** The results from prior tasks show VLMs cannot always count shapes that are overlapping (Sec. 3.4) or nested (Sec. 3.5). What about adjacent shapes ⟦SLOT_61⟧ ⟦SLOT_62⟧ ? Here, we tile up shapes (specifically, ⟦SLOT_63⟧ ) into a grid and challenge VLMs to count—a task that is supposedly simple to VLMs given their remarkable performance (⟦SLOT_64⟧ 90% accuracy) [38, 43] on DocVQA [31], which includes many questions with tables. To simplify the task, we ask models to count the number of rows and columns in a given table (either empty or text-containing).

**ZH** 先前任务的结果表明，VLM 并不总能清点相互重叠（第 3.4 节）或嵌套（第 3.5 节）的形状。那么相邻的形状 ⟦SLOT_61⟧ ⟦SLOT_62⟧ 又如何？这里我们把形状（具体地，⟦SLOT_63⟧ ）平铺成网格，并要求 VLM 清点——鉴于 VLM 在 DocVQA [31] 上的出色表现（⟦SLOT_64⟧ 90% 准确率）[38, 43]，而该基准包含大量涉及表格的问题，这理应是一项对 VLM 而言简单的任务。为简化任务，我们让模型数出给定表格的行数与列数（表格可为空或含文字）。

**EN** Images A grid may have ⟦SLOT_65⟧⟦SLOT_66⟧⟦SLOT_67⟧, ⟦SLOT_68⟧⟦SLOT_69⟧⟦SLOT_70⟧, or ⟦SLOT_71⟧⟦SLOT_72⟧⟦SLOT_73⟧ cells, where ⟦SLOT_74⟧ and ⟦SLOT_75⟧. We also include grids of size 10⟦SLOT_76⟧10 to balance the benchmark with the row and column sizes. Each grid is rendered with two different line widths on a canvas of size ⟦SLOT_77⟧ where ⟦SLOT_78⟧px. Besides empty grids, we also replicate the procedure to make grids contain text (which is more common in real-world tables) where each cell contains a single random English word (see Fig. F36). Both versions (empty and text-containing) combined have 2⟦SLOT_79⟧132 = 264 images. See Sec. 0.K.1 for more details.

**ZH** 图像：一个网格可以有 ⟦SLOT_65⟧⟦SLOT_66⟧⟦SLOT_67⟧、⟦SLOT_68⟧⟦SLOT_69⟧⟦SLOT_70⟧ 或 ⟦SLOT_71⟧⟦SLOT_72⟧⟦SLOT_73⟧ 个单元格，其中 ⟦SLOT_74⟧ 且 ⟦SLOT_75⟧。我们还纳入 10⟦SLOT_76⟧10 的网格，以使基准在行、列规模上保持均衡。每个网格以两种线宽渲染在尺寸为 ⟦SLOT_77⟧ 的画布上，其中 ⟦SLOT_78⟧px。除空网格外，我们也复制该流程生成含文字的网格（这在真实表格中更常见），每个单元格含一个随机英文单词（见图 F36）。两个版本（空网格与含文字网格）合计 2⟦SLOT_79⟧132 = 264 张图像。详见第 0.K.1 节。

**EN** 3.7 Task 7: Following single-colored paths

**ZH** 3.7 任务 7：追踪单色路径

**EN** It is important for VLMs to be able to follow paths in order to read maps or charts [30], interpret graphs [19], and user annotations (e.g., arrows) in input images [54]. To assess path-following capability, this task asks models to count the unique-color paths between two given stations in a simplified subway map.

**ZH** 对 VLM 而言，能够追踪路径是读取地图或图表 [30]、理解图结构 [19]，以及理解输入图像中用户标注（例如箭头）[54] 的重要前提。为评估路径追踪能力，本任务要求模型数出简化地铁图中两个给定站点之间单色路径的条数。

**EN** Images We create each subway map on an image of size ⟦SLOT_80⟧, where ⟦SLOT_81⟧px (see Fig. F41). We write 4 station names (A, B, C, D) at 4 fixed coordinates ⟦SLOT_82⟧, respectively. We divide the canvas into an invisible grid of 18⟦SLOT_83⟧18 cells and initialize 3 path-starting points ⟦SLOT_84⟧px away from each station. We draw a path, using the depth-first search algorithm starting from a random station and a random starting point, where a valid move is one cell in any direction: North, south, east or west. We repeat the process so that each station has exactly ⟦SLOT_85⟧ outgoing paths, for a total of 180 maps. See Sec. 0.L.1 for details.

**ZH** 图像：我们在尺寸为 ⟦SLOT_80⟧ 的图像上生成每张地铁图，其中 ⟦SLOT_81⟧px（见图 F41）。我们把 4 个站名（A、B、C、D）分别写在 4 个固定坐标 ⟦SLOT_82⟧ 处。我们把画布划分为 18⟦SLOT_83⟧18 的不可见网格，并在距每个车站 ⟦SLOT_84⟧px 处初始化 3 个路径起点。我们采用深度优先搜索算法，从一个随机车站与一个随机起点出发绘制路径，其中一次合法移动是朝北、南、东、西任一方向移动一格。我们重复该流程，使每个车站恰好有 ⟦SLOT_85⟧ 条出边，共得到 180 张地图。详见第 0.L.1 节。

**EN** 4 Results

**ZH** 4 结果

**EN** Table 1: The mean accuracy (%) of all four VLMs over 7 BlindTest tasks is 58.07%, substantially higher than random chance (24%), which is computed considering each task as a single-label, ⟦SLOT_86⟧-way classification problem. Sonnet-3.5 is the best (77.84%) but still far from the expected 100% accuracy. Note that the best open-source VLM (Tab. T1) is only on par with and the best slow-thinking VLM is slightly worse than ⟦SLOT_87⟧ (Sec. 4.7).

**ZH** 表 1：四款 VLM 在 7 项 BlindTest 任务上的平均准确率为 58.07%，显著高于随机猜测（24%）；后者把每项任务视为一个单标签的 ⟦SLOT_86⟧ 类分类问题计算得出。Sonnet-3.5 最好（77.84%），但仍远未达到预期的 100% 准确率。需注意，最好的开源 VLM（表 T1）仅与之持平，而最好的慢思考 VLM 略逊于 ⟦SLOT_87⟧（第 4.7 节）。

<!-- [原子块 · table] a. b. c. d. e. f. g. h. i. Model ○ ○ ○ ⬠ ⬠ ⬠ Task mean Random 33.33 50.00 5.77 20.00 20.00 25.00 4.55 33.33 24.00 GPT- 4o 41.61 75.91 74.23 41.25 20.21 55.83 39.58 53.19 50.23 Gemini- 1.5 66.94 93.62  -->

**EN** 4.1 VLMs cannot reliably count line intersections ⟦SLOT_88⟧

**ZH** 4.1 VLM 无法可靠地数清直线交点 ⟦SLOT_88⟧

**EN** Experiment We parse every model’s response to extract the final answer and then compare it to the groundtruth. We report the mean accuracy of every model on two prompts and analyze how accuracy changes as we vary hyperparameters (e.g., line widths and image sizes).

**ZH** 实验：我们解析每个模型的回答以抽取最终答案，再与真值比较。我们报告每个模型在两种提示下的平均准确率，并分析准确率随超参数（例如线宽与图像尺寸）变化的情况。

<!-- [原子块 · table] Line width 0.005 × C 0.005\times C 45.00 67.55 45.22 75.83 0.010 × C 0.010\times C 38.22 66.33 41.61 74.88 Mean 41.61 66.94 43.41 75.36 -->

**EN** Table 2: The accuracy breakdown by line width in pixels (where ⟦SLOT_89⟧ = image width), averaged over two prompts, shows that VLMs cannot reliably count the intersections between two simple 2D line plots.

**ZH** 表 2：按线宽（单位为像素，其中 ⟦SLOT_89⟧ = 图像宽度）细分的准确率，对两种提示取平均，显示 VLM 无法可靠地数清两条简单二维折线之间的交点。

<!-- [原子块 · table]  -->

**EN** Figure 2: As a line-plot image is divided into a 12⟦SLOT_90⟧12 grid, the x-axis shows the mean distance (in grid cells) over 3 pairs of points of two 2-segment plots. VLMs are often more confused when two plots are closer together (left) than when they are further apart (right).

**ZH** 图 2：折线图图像被划分为 12⟦SLOT_90⟧12 网格后，x 轴表示两条两段折线在三对点上的平均距离（以网格单元计）。当两张折线图靠得更近时（左），VLM 往往比它们相距较远时（右）更容易混淆。

**EN** Results First, across two prompts and two line widths, all VLMs are 56.84% accurate (Tab. 1a), far from the expected 100% accuracy on this easy task (Fig. F24). The best accuracy is only 75.36% (Sonnet-3.5) (Tab. 2). Specifically, VLMs tend to perform worse when the distance between two plots narrows (Fig. 2). As each line plot is composed of three key points, the distance between two plots is computed as the mean distance over three corresponding point pairs. See Figs. 1 and 0.H.4 for more samples of VLM predictions. VLMs perform similarly across three image sizes (Sec. 0.H.2).

**ZH** 结果：首先，在两种提示与两种线宽下，所有 VLM 的准确率为 56.84%（表 1a），远未达到这项简单任务上预期的 100%（图 F24）。最好的准确率仅为 75.36%（Sonnet-3.5）（表 2）。具体地，当两张折线图之间的距离变小时，VLM 的表现往往更差（图 2）。由于每条折线由三个关键点构成，两张折线图之间的距离取三对对应点距离的平均值。更多 VLM 预测样例见图 1 与图 0.H.4。VLM 在三种图像尺寸上表现相近（第 0.H.2 节）。

**EN** Our findings are in stark contrast to the high accuracy of VLMs on ChartQA [43, 38], suggesting that VLMs can recognize the overall trend of a line plot but unable to “zoom in” to extract details, e.g., seeing which lines are intersecting.

**ZH** 我们的发现与 VLM 在 ChartQA [43, 38] 上的高准确率形成鲜明反差，提示 VLM 能识别折线图的整体趋势，却无法「放大」以提取细节，例如看清哪些线在相交。

**EN** 4.2 VLMs cannot clearly see if two circles overlap or not ⟦SLOT_91⟧

**ZH** 4.2 VLM 无法看清两个圆是否重叠 ⟦SLOT_91⟧

**EN** Motivated by VLM poor performance in counting line intersections (Sec. 4.1), here, we replace lines by large, filled circles and ask VLMs explicitly if the two circles are touching (or overlapping).

**ZH** 受 VLM 在数直线交点上表现不佳（第 4.1 节）的启发，这里我们把直线换成大的实心圆，并明确询问 VLM 两个圆是相切还是重叠。

**EN** Experiment Since we instruct VLMs to output a binary answer (Yes/No), we use Python to extract VLMs’ formatted answer from their responses for comparing with groundtruth.

**ZH** 实验：由于我们指示 VLM 输出二元答案（是/否），我们用 Python 从回答中抽取 VLM 的格式化答案，以便与真值比较。

**EN** Results Surprisingly, even on this task where objects (⟦SLOT_92⟧ ⟦SLOT_93⟧ ) are large and clearly visible to humans, no VLMs are able to solve it perfectly—their mean accuracy is 86.70% (Tab. 1b). The best accuracy is 93.62% (Gemini-1.5) over all images and two prompts (Tab. 3). A common trend is when two circles are closer together, VLMs tend to perform more poorly, making educated guesses, e.g., Sonnet-3.5 often answers “No” conservatively (Fig. F8). GPT-4o performs the worst and shockingly is not 100% accurate even when the distance between two circles is as large as one radius (Fig. 3; ⟦SLOT_94⟧). That is, consistent with the results from Sec. 4.1, VLMs seem to be unable to always detect the gap or intersection between two filled circles (Figs. 1 and F8).

**ZH** 结果：令人意外的是，即便在这项物体（⟦SLOT_92⟧ ⟦SLOT_93⟧ ）大且对人类清晰可见的任务上，也没有任何 VLM 能完美解决——它们的平均准确率为 86.70%（表 1b）。在所有图像与两种提示上，最好的准确率为 93.62%（Gemini-1.5）（表 3）。一个共同趋势是：当两个圆靠得更近时，VLM 的表现往往更差，做出经验性猜测——例如 Sonnet-3.5 常常保守地回答「否」（图 F8）。GPT-4o 表现最差，且令人震惊的是，即便两圆间距已大到一个半径，它仍达不到 100% 准确（图 3；⟦SLOT_94⟧）。也就是说，与第 4.1 节的结果一致，VLM 似乎并不总能检测出两个实心圆之间的间隙或相交（图 1 与图 F8）。

<!-- [原子块 · table] Model Overlapping Touching Mean GPT- 4o 74.74 77.08 75.91 Gemini- 1.5 94.01 93.23 93.62 Sonnet- 3 89.58 83.33 86.46 Sonnet- 3.5 86.46 95.18 90.82 -->

**EN** Table 3: and perform more consistently over the two different prompts (“overlapping” and “touching”) than and ⟦SLOT_95⟧.

**ZH** 表 3： 与 在两种不同提示（「重叠」与「相切」）下比 与 ⟦SLOT_95⟧ 表现更为一致。

<!-- [原子块 · table]  -->

**EN** Figure 3: VLMs perform poorly when two circles are tangent (⟦SLOT_96⟧) or close together (⟦SLOT_97⟧). Yet, ⟦SLOT_98⟧ is better at ⟦SLOT_99⟧. (perhaps due to its tendency to answer “No”).

**ZH** 图 3：当两个圆相切（⟦SLOT_96⟧）或靠得很近（⟦SLOT_97⟧）时，VLM 表现很差。然而，⟦SLOT_98⟧ 在 ⟦SLOT_99⟧ 上更好（或许是因为它倾向于回答「否」）。

**EN** An explanation is that due to the late-fusion mechanism [47], VLMs extract visual features from the image before even looking at the question, causing this “blindness”. In contrast, if a model first knows that the question asks it to focus on the area between the two circles, it then might be able to extract accurate visual information to answer such simple questions.

**ZH** 一种解释是：由于后期融合机制 [47]，VLM 在看问题之前就已从图像中提取视觉特征，从而造成了这种「失明」。相反，如果模型先知道问题要求它聚焦于两圆之间的区域，它就可能提取出准确的视觉信息来回答这类简单问题。

**EN** While VLMs perform similarly across three image resolutions (Sec. 0.F.2), every model performs the best at a specific circle orientation (Sec. 0.F.5). Moreover, VLMs’ performance does not change substantially (⟦SLOT_100⟧ points for Sonnet-3.5 and ⟦SLOT_101⟧10.81 for GPT-4o) when tested against different colors (Sec. 0.F.6), ruling out the impact of color on their performance on the task. More examples of VLMs’ answers are in Sec. 0.F.8.

**ZH** 虽然 VLM 在三种图像分辨率上表现相近（第 0.F.2 节），但每个模型都在某个特定的圆朝向上表现最好（第 0.F.5 节）。此外，当用不同颜色测试时，VLM 的表现没有实质变化（对 Sonnet-3.5 为 ⟦SLOT_100⟧ 个点，对 GPT-4o 为 ⟦SLOT_101⟧10.81）（第 0.F.6 节），排除了颜色对该任务表现的影响。更多 VLM 回答样例见第 0.F.8 节。

**EN** 4.3 VLMs do not always see the letter inside the red circle ⟦SLOT_102⟧

**ZH** 4.3 VLM 并不总能看见红圈内的字母 ⟦SLOT_102⟧

**EN** Experiment To evaluate the models’ ability to recognize individual characters in an image, we place a red circle over one character in a word. We prompt VLMs to put their prediction in {curly braces} and then we compare the lowercase version of this character to the lowercase version of the groundtruth character.

**ZH** 实验：为评估模型识别图像中单个字符的能力，我们把一个红圈覆盖在单词的某个字符上。我们提示 VLM 把预测结果放在 {花括号} 中，然后把该字符的小写形式与真值字符的小写形式作比较。

<!-- [原子块 · svg]  -->

**EN** Figure 4: Identifying the letter being circled is non-trivial for VLMs across both English words ( Acknowledgement & Subdermatoglyphic ) and a random string ( tHyUiKaRbNqWeOpXcZvM ). When making mistakes, VLMs tend to predict letters adjacent to the one being circled.

**ZH** 图 4：对 VLM 而言，辨认被圈住的字母并非易事，无论是对两个英文单词（ Acknowledgement 与 Subdermatoglyphic ）还是对一个随机字符串（ tHyUiKaRbNqWeOpXcZvM ）。出错时，VLM 倾向于预测被圈字母的相邻字母。

**EN** Results All VLMs can accurately spell out the string when there is a red oval ⟦SLOT_103⟧ superimposed on the image. Yet, interestingly, reading out which letter is being circled turns out to be a challenge (mean model accuracy: 79.7%; Tab. 1c).

**ZH** 结果：当没有红色椭圆 ⟦SLOT_103⟧ 叠加在图像上时，所有 VLM 都能准确拼出字符串。然而有意思的是，读出哪个字母被圈住却成了一项挑战（模型平均准确率：79.7%；表 1c）。

**EN** When the letters are close together, VLMs often predict letters adjacent to the one being circled (see the confusion matrix in Fig. F13 and more results in Figs. 1 and 0.G.2). Sometimes models hallucinate, e.g., coming up with characters non-existent in Subdermatoglyphic (e.g., “9”, “n”, “©”) despite having the ability to accurately spell out the word (see Fig. F13). We also observe that VLMs, on average, fail to see the circled letter across various common English words (mean accuracy is 86.43% in Sec. 0.G.6). However, as the words get shorter in length and there is no repetitive letters in them, VLMs tend to perform better. More failure cases are reported in Secs. 0.G.3 and 0.G.8.

**ZH** 当字母彼此靠近时，VLM 常常预测被圈字母的相邻字母（见图 F13 的混淆矩阵，以及图 1 与图 0.G.2 中的更多结果）。有时模型会产生幻觉，例如凭空造出 Subdermatoglyphic 中不存在的字符（如「9」「n」「©」），尽管它们有能力准确拼出该单词（见图 F13）。我们还观察到，VLM 在各种常见英文单词上平均也无法看清被圈的字母（第 0.G.6 节中平均准确率为 86.43%）。不过，随着单词变短且不含重复字母，VLM 的表现往往更好。更多失败案例见第 0.G.3 与 0.G.8 节。

**EN** On average, models perform better (+0.46 to +13 points) on the two English words compared to the random string (Tab. T8), suggesting that familiarity with the word help VLMs make better educated guesses, slightly improving accuracy.

**ZH** 平均而言，模型在两个英文单词上的表现优于随机字符串（+0.46 至 +13 个点）（表 T8），说明对单词的熟悉有助于 VLM 做出更好的经验性猜测，略微提升准确率。

**EN** Sonnet-3.5 and Gemini-1.5 are the top-2 models (87.88% and 83.29%) and are better than GPT-4o and Sonnet-3 by a large margin of nearly +15 points (Tab. T8). VLMs perform similarly across two prompts (Sec. 0.G.5) and two font families (Sec. 0.G.4). See also Fig. F1 for an example of GPT-4o and Gemini-1.5 making educated guesses on the color of the overlapping area between two overlapping circles (Task 2).

**ZH** Sonnet-3.5 与 Gemini-1.5 是前两名（87.88% 与 83.29%），并以近 +15 个点的较大幅度优于 GPT-4o 与 Sonnet-3（表 T8）。VLM 在两种提示（第 0.G.5 节）与两种字体族（第 0.G.4 节）下表现相近。另见图 F1 中 GPT-4o 与 Gemini-1.5 对两个重叠圆之间重叠区域颜色做出经验性猜测的例子（任务 2）。

**EN** 4.4 VLMs struggle to count overlapped and nested shapes

**ZH** 4.4 VLM 难以清点重叠与嵌套的形状

**EN** Experiment We run all VLMs on images of overlapping shapes ( ○ and ⬠ ) (Sec. 3.4) and nested squares (Sec. 3.5). We prompt VLMs to output the predicted number of shapes in a formatted answer (which is extracted and compared with groundtruth). For each shape ( ○ , ⬠ or ⟦SLOT_104⟧ ), we run two different prompts.

**ZH** 实验：我们在重叠形状（ ○ 与 ⬠ ）（第 3.4 节）与嵌套正方形（第 3.5 节）的图像上运行所有 VLM。我们提示 VLM 以格式化答案输出预测的形状数量（随后抽取并与真值比较）。对每种形状（ ○ 、 ⬠ 或 ⟦SLOT_104⟧ ），我们运行两种不同的提示。

**EN** Results On counting overlapping circles, pentagons, and nested squares, VLM mean accuracy is 39.44%, 30.99%, and 74.99%, respectively (Tab. 1d–f). That is, counting shapes is not easy to models regardless of whether the shapes are overlapped or nested (Figs. 1 and F34). On nested squares, model accuracies vary widely—GPT-4o (55.83%) and Sonnet-3 (65.00%) are at least -25 points behind Gemini-1.5 (87.08%) and Sonnet-3.5 (92.08%). This gap is even larger on overlapped circles and pentagons—Sonnet-3.5 outperforms other models by multiple times (e.g., 77.71% vs. 1.87% of Sonnet-3; Tab. 1).

**ZH** 结果：在清点重叠圆、五边形与嵌套正方形上，VLM 的平均准确率分别为 39.44%、30.99% 与 74.99%（表 1d–f）。也就是说，无论形状是重叠还是嵌套，清点形状对模型都不容易（图 1 与图 F34）。在嵌套正方形上，各模型准确率差异很大——GPT-4o（55.83%）与 Sonnet-3（65.00%）至少落后 Gemini-1.5（87.08%）与 Sonnet-3.5（92.08%）25 个点。这一差距在重叠圆与五边形上更大——Sonnet-3.5 以数倍于其他模型的表现胜出（例如 77.71% 对 Sonnet-3 的 1.87%；表 1）。

**EN** All four models are at least 83% accurate in counting 5 circles. Yet, surprisingly, increasing the number of circles by only one causes accuracy to dip substantially to near zero for all models, except Sonnet-3.5 (Fig. 5; column 6–9). In counting pentagons, all VLMs (except Sonnet-3.5) perform poorly even at 5 pentagons. Overall, counting from 6 to 9 shapes (both circles and pentagons) is hard for all models.

**ZH** 四款模型在清点 5 个圆时准确率都至少为 83%。然而令人意外的是，只把圆的数量增加一个，就会使所有模型的准确率大幅下滑至接近零，Sonnet-3.5 除外（图 5；第 6–9 列）。在清点五边形时，即便只有 5 个五边形，所有 VLM（Sonnet-3.5 除外）也表现很差。总的来看，清点 6 到 9 个形状（圆与五边形皆然）对所有模型都很困难。

<!-- [原子块 · table] (a) Circles ○ ○ ○ (b) Pentagons ⬠ ⬠ ⬠ (c) Squares Number of shapes -->

**EN** Figure 5: All four VLMs can count 5 circles well (leftmost; 0.83), but only ⟦SLOT_105⟧ can count 5 overlapping pentagons well at 0.9 accuracy (b). Counting from 6–9 shapes (either ○ or ⬠ ) is challenging to VLMs.

**ZH** 图 5：四款 VLM 都能很好地清点 5 个圆（最左；0.83），但只有 ⟦SLOT_105⟧ 能以 0.9 的准确率很好地清点 5 个重叠五边形（b）。清点 6–9 个形状（ ○ 或 ⬠ ）对 VLM 而言颇具挑战。

**EN** Why are VLMs nearly perfect at counting 5 circles (Fig. 5a), but struggle to count 5 pentagons or more than 5 shapes? When there are more than 5 circles ( ○ ) and VLMs predict an incorrect count, Gemini-1.5 predicts “5” 99.74% of the time regardless of the actual number of circles (Tab. T13). For other models, this frequency is also much higher than that in the case of pentagons. Our results show strong evidence for an explanation that VLMs are biased towards the well-known 5-circle Olympic logo (more results on this bias in Sec. 0.J.4).

**ZH** 为什么 VLM 在清点 5 个圆时近乎完美（图 5a），却难以清点 5 个五边形或多于 5 个形状？当圆（ ○ ）多于 5 个且 VLM 给出错误计数时，Gemini-1.5 有 99.74% 的情况预测为「5」，而不论实际的圆数是多少（表 T13）。对其他模型而言，这一频率也远高于五边形情形。我们的结果为如下解释提供了有力证据：VLM 对广为人知的奥运五环标志存在偏差（关于该偏差的更多结果见第 0.J.4 节）。

**EN** Note that there are only 2 to 5 squares in each image in the task of counting nested squares, and these squares do not intersect (Fig. F28). Surprisingly, GPT-4o and Sonnet-3 are still unable to perfectly count two and three nested squares (Fig. 5c). When the count increases to four and five, most models are far from 100% accurate (Fig. 5c).

**ZH** 需注意，在清点嵌套正方形的任务中，每张图像只有 2 到 5 个正方形，且这些正方形互不相交（图 F28）。令人意外的是，GPT-4o 与 Sonnet-3 仍无法完美清点两个与三个嵌套正方形（图 5c）。当数量增至四个与五个时，多数模型远未达到 100% 准确（图 5c）。

**EN** GPT-4o performs better on colored shapes than on black shapes, and Sonnet-3.5 is increasingly better as the image size increases. However, the accuracy of the three other models only changes marginally as colors (Sec. 0.J.3) and image resolutions (Sec. 0.J.2) change.

**ZH** GPT-4o 在彩色形状上的表现优于黑色形状，而 Sonnet-3.5 随图像尺寸增大而越来越好。不过，随着颜色（第 0.J.3 节）与图像分辨率（第 0.J.2 节）变化，其余三款模型的准确率仅有微小变动。

**EN** 4.5 VLMs cannot reliably count rows and columns in a grid ⟦SLOT_106⟧

**ZH** 4.5 VLM 无法可靠地数清网格的行与列 ⟦SLOT_106⟧

**EN** Since VLMs struggle with counting simple shapes when the shape edges intersect (Sec. 3.4) or separate (Sec. 3.5), here, we test the remaining case where these shapes are adjacent and share edges. That is, multiple squares tile up into a single grid. Given the impressive accuracy of VLMs [38, 43, 2] on questions involving tables and spreadsheets in DocVQA [31], we hypothesize that VLMs must be able to count rows and columns of a grid.

**ZH** 既然 VLM 在形状边缘相交（第 3.4 节）或分离（第 3.5 节）时都难以清点简单形状，这里我们测试剩下的一种情形：这些形状相邻且共享边。也就是说，多个正方形平铺成一个网格。鉴于 VLM 在 DocVQA [31] 中涉及表格与电子表格的问题上准确率惊人 [38, 43, 2]，我们假设 VLM 必定能数出网格的行数与列数。

**EN** Experiment We run all four VLMs on all images of empty grids and text-containing grids (Sec. 3.6) and analyze their formatted answers.

**ZH** 实验：我们在空网格与含文字网格（第 3.6 节）的全部图像上运行四款 VLM，并分析它们的格式化答案。

**EN** Results VLMs surprisingly perform poorly (34.37% accuracy) in counting rows and columns in an empty grid (see Tab. T15). Specifically, they are often off by one or two (e.g., GPT-4o predicts 4⟦SLOT_107⟧4 and Gemini-1.5 predicts 5⟦SLOT_108⟧5 for a 4⟦SLOT_109⟧5 grid; Figs. F37 and 1). This finding suggests that VLMs can extract important content from a table to answer table-related questions in DocVQA [31] but do not clearly “see” a table cell-by-cell as a human does.

**ZH** 结果：VLM 在数空网格的行与列时表现之差令人意外（34.37% 准确率）（见表 T15）。具体地，它们常常相差一或二（例如，GPT-4o 预测为 4⟦SLOT_107⟧4，Gemini-1.5 预测为 5⟦SLOT_108⟧5，而实际网格为 4⟦SLOT_109⟧5；图 F37 与图 1）。这一发现说明，VLM 能从表格中抽取重要内容以回答 DocVQA [31] 中与表格相关的问题，却不能像人类那样逐格清晰地「看见」一张表格。

<!-- [原子块 · table] (a) Empty (b) Text-containing (c) Rows (d) Columns -->

**EN** Figure 6: Accuracy of counting rows (c) vs. columns (d) (here, analyzed separately) when the grids are empty (a) vs. contain text (b). VLMs (especially, and ) generally count much more accurately when grids contain text vs. empty grids (b vs. a). Interestingly, columns are also easier for VLMs to count than rows (d vs. c).

**ZH** 图 6：分别考察数行（c）与数列（d）的准确率，以及网格为空（a）与含文字（b）时的情形。VLM（尤其是 与 ）在网格含文字时普遍比空网格时数得更准（b 对 a）。有意思的是，对 VLM 而言，数列也比数行更容易（d 对 c）。

**EN** This might be because tables in documents are often non-empty, which are more familiar to VLMs. Aligned with that hypothesis, after adding a single word to each cell, we observe the accuracy of all VLMs to almost double (e.g., from 26.13% to 53.03% for GPT-4o) (Tab. T15). Yet, no models can solve this task with the best model (Sonnet-3.5) performing at 88.68% on text-containing grids and 59.84% on empty grids (Fig. 6a vs. b).

**ZH** 这可能是因为文档中的表格往往非空，对 VLM 而言更为熟悉。与这一假设相符的是，在每个单元格加入一个单词后，我们观察到所有 VLM 的准确率几乎翻倍（例如 GPT-4o 从 26.13% 升至 53.03%）（表 T15）。然而，没有模型能完美解决该任务——最好的模型（Sonnet-3.5）在含文字网格上为 88.68%，在空网格上为 59.84%（图 6a 对 b）。

**EN** Interestingly, VLMs are better at counting columns than rows—70.53% vs. 60.83% accuracy (Fig. 6c vs. d). However, these numbers are still far from 100% showing that VLMs currently cannot count neither rows or columns in a table reliably. See Secs. 0.K.2 and 0.K.3 for more results.

**ZH** 有意思的是，VLM 数列比数行更准——70.53% 对 60.83% 准确率（图 6c 对 d）。不过这些数字仍远未达到 100%，说明当前的 VLM 尚不能可靠地数清表格中的行或列。更多结果见第 0.K.2 与 0.K.3 节。

**EN** 4.6 VLMs struggle to count single-colored paths

**ZH** 4.6 VLM 难以清点单色路径

**EN** This path-counting task tests a VLM’s ability in recognizing a path of a unique color and trace it from a given starting station to the destination, an important task in reading maps and graphs in general [30].

**ZH** 这项路径计数任务考察 VLM 识别某一独特色彩的路径、并从给定起点站追踪到终点站的能力，这是广义上阅读地图与图结构的重要任务 [30]。

**EN** Experiment From a subway map (Sec. 3.7), we randomly sample 2 connected stations and prompt every model to count the single-colored paths that connect them. We extract numbers from VLM templated responses and compare them with the groundtruth.

**ZH** 实验：在一张地铁图（第 3.7 节）上，我们随机采样两个相连的站点，并提示每个模型数出连接它们的单色路径条数。我们从 VLM 的模板化回答中抽取数字，与真值比较。

**EN** Results Overall, VLMs perform poorly at a mean accuracy of 48.90% (Tab. 1h). Even when there is only one path between two stations, no models can reach 100% accuracy (the best is Sonnet-3.5 at 93.33% and the worst is 20%; Fig. F42). VLM predicted counts are often off by 1 to 3 paths (Fig. F45). VLM accuracy reduces substantially, e.g., Sonnet-3.5 from 93.33% to 58.33% and 22.91% as the complexity of the maps increases from 1, 2 to 3 paths, respectively (Fig. F42). More samples of VLM responses are in Figs. 1 and 0.L.4.

**ZH** 结果：总体来看，VLM 表现很差，平均准确率为 48.90%（表 1h）。即便两站之间只有一条路径，也没有模型能达到 100% 准确率（最好的是 Sonnet-3.5，93.33%；最差的是 20%；图 F42）。VLM 预测的条数常常偏差 1 到 3 条（图 F45）。随着地图复杂度从 1 条增至 2 条、3 条路径，VLM 的准确率大幅下降，例如 Sonnet-3.5 从 93.33% 降至 58.33% 与 22.91%（图 F42）。更多 VLM 回答样例见图 1 与图 0.L.4。

**EN** 4.7 Long-inference, slow-thinking VLMs perform similarly to regular VLMs on BlindTest

**ZH** 4.7 长推理的慢思考 VLM 在 BlindTest 上与常规 VLM 表现相当

**EN** From math to coding, spending more time thinking before responding enables LLMs to perform substantially better in many tasks [16]. Here, we aim to test whether such slow thinking also enables VLMs to perform better on BlindTest where we argue that reasoning in the text space might not help. We perform this test for two SOTA models by comparing them with their corresponding slow-thinking versions.

**ZH** 从数学到编程，回答前多花时间思考能让大语言模型在许多任务上表现显著更好 [16]。这里我们要检验：在我们主张文本空间中的推理可能无济于事的 BlindTest 上，这种慢思考是否也能让 VLM 表现更好。我们用两款 SOTA 模型，与其对应的慢思考版本作比较，来实施这一检验。

**EN** Experiment We run 2 SOTA slow-thinking VLMs: Gemini 2.0 Flash-Thinking and QVQ on BlindTest, and compare them with their non-thinking, regular versions, i.e., Gemini 2.0 Flash and Qwen2-VL.

**ZH** 实验：我们在 BlindTest 上运行两款 SOTA 慢思考 VLM：Gemini 2.0 Flash-Thinking 与 QVQ，并把它们与各自的非思考、常规版本（即 Gemini 2.0 Flash 与 Qwen2-VL）作比较。

**EN** Table 4: SOTA slow-thinking models (bottom) perform even worse than their regular counterpart (top) BlindTest, showing that the longer inference has no positive impact on BlindTest tasks. QVQ is the slow-thinking counterpart of Qwen2-VL.

**ZH** 表 4：当前最优的慢思考模型（下）在 BlindTest 上甚至比对应的常规版本（上）更差，说明更长的推理对 BlindTest 任务没有正面影响。QVQ 是 Qwen2-VL 的慢思考对应版本。

<!-- [原子块 · table] Model Size ○ ○ ○ ⬠ ⬠ ⬠ Task mean Gemini 2.0 Flash n/a 85.44 80.95 81.73 55.62 44.16 96.25 66.85 70.97 72.75 Qwen2-VL 72B 64.97 76.41 73.56 28.12 35.42 74.58 20.64 59.31 54.13 Gemini 2.0 Flash-Thinking -->

**EN** Results On average over 7 tasks, Gemini 2.0 Flash-Thinking, is on par with its non-thinking counterpart, Gemini 2.0 Flash (Tab. 4; 71.59 vs 72.75%). This shows that the “slow-thinking” capability (i.e., long, scaled-up inference) does not address the main challenge that BlindTest poses to VLMs. Qualitatively examining the thinking tokens of Gemini 2.0 Flash-Thinking shows that the hidden thoughts are in text space and have no benefits on BlindTest (see Figs. 7 and 8). Moreover, QVQ, the SOTA open-source slow-thinking model is also -11.65 points behind its non-thinking counterpart, Qwen2-VL (Tab. 4).

**ZH** 结果：在 7 项任务上平均，Gemini 2.0 Flash-Thinking 与其非思考对应版本 Gemini 2.0 Flash 持平（表 4；71.59% 对 72.75%）。这说明「慢思考」能力（即长时间的、规模化扩展的推理）并未解决 BlindTest 给 VLM 带来的主要挑战。定性考察 Gemini 2.0 Flash-Thinking 的思考 token 显示，其隐藏的思考处于文本空间，对 BlindTest 毫无助益（见图 7 与图 8）。此外，QVQ——当前最优的开源慢思考模型——也比其非思考对应版本 Qwen2-VL 低 11.65 个点（表 4）。

<!-- [原子块 · svg]  -->

**EN** Figure 7: Gemini 2.0 Flash-Thinking cannot count the circles in the image even during its thought process and responds similarly to its non-thinking version (Gemini 2.0 Flash).

**ZH** 图 7：Gemini 2.0 Flash-Thinking 即使在思考过程中也无法数清图像中的圆，其回答与其非思考版本（Gemini 2.0 Flash）相似。

<!-- [原子块 · svg]  -->

**EN** Figure 8: While Gemini 2.0 Flash-Thinking makes an effort to follow the lines in the subway-like map, it fails to see all the single-color lines connected to point C, providing the same incorrect final answer as Gemini 2.0 Flash.

**ZH** 图 8：尽管 Gemini 2.0 Flash-Thinking 努力追踪类地铁图中的线路，它仍未看见所有连接到 C 点的单色线，给出了与 Gemini 2.0 Flash 相同的错误最终答案。

**EN** 5 VLMs can solve most tasks when there is more space between shapes and letters

**ZH** 5 当形状与字母之间有更多空间时，VLM 能解决多数任务

**EN** Since none of the tested SOTA VLMs, including the slow-thinking ones, is capable of solving any task at near-100% accuracy (Sec. 4), there are two hypotheses to explain this result: (1) prompts may be suboptimal (no prompt-engineering performed); (2) the questions are out-of-distribution for VLMs and they are not capable of solving them, e.g., counting to 10; (3) the shapes being so close together that they are overlapping or nesting or adjacent causes challenges to VLMs in extracting accurate features (and therefore answering questions).

**ZH** 既然受测的 SOTA VLM（包括慢思考模型）无一能以接近 100% 的准确率解决任何任务（第 4 节），对这一结果有两种解释假说：（1）提示可能不够理想（未做提示工程）；（2）这些问题对 VLM 而言属于分布外，它们没有能力解决，例如数到 10；（3）形状靠得如此之近，以至于相互重叠、嵌套或相邻，造成 VLM 难以提取准确特征（进而难以回答问题）。

**EN** To tease apart hypotheses (1) & (2) from (3), we increasingly add more space between letters and shapes to hopefully make the tasks easier (e.g., space between characters in ⟦SLOT_110⟧ or between circles ○ ○ ○ ) and report model-accuracy changes (i.e., how a VLM would reach near 100% accuracy).

**ZH** 为把假说（1）与（2）同（3）区分开，我们逐步在字母与形状之间加入更多的空间，以期降低任务难度（例如 ⟦SLOT_110⟧ 中字符之间的间距，或圆 ○ ○ ○ 之间的间距），并报告模型准确率的变化（即 VLM 如何接近 100% 准确率）。

**EN** 5.1 VLMs perform better as the spacing between letters in the circled letter task increases

**ZH** 5.1 随着被圈字母任务中字母间距增大，VLM 表现更好

**EN** Experiment On the circled-letter task ○ , VLMs often cannot reliably tell which letter is being circled among adjacent ones (see Fig. F13). Here, we add 1 to 3 ASCII space characters between adjacent letters of a string and evaluate VLMs using the exact same prompts as done in Sec. 4.3.

**ZH** 实验：在被圈字母任务 ○ 上，VLM 常常无法可靠判断相邻字母中被圈住的是哪一个（见图 F13）。这里我们在字符串的相邻字母之间加入 1 至 3 个 ASCII 空格字符，并用与第 4.3 节完全相同的提示评估 VLM。

<!-- [原子块 · table] 0 (baseline) 1 2 3 # of spaces example image Number of spaces (a) (b) -->

**EN** Figure 9: (a) By adding more space ⟦SLOT_111⟧ to baseline images in the circled letter task, we create a simpler version of them. (b) VLMs generally perform better when there is ⟦SLOT_112⟧1 space between letters of the words (⟦SLOT_113⟧ for Sonnet-3 and GPT-4o is +21 and +13 from 0 to 3 spaces, respectively).

**ZH** 图 9：（a）通过在被圈字母任务的基线图像中加入更多空格 ⟦SLOT_111⟧，我们得到它们的简化版本。（b）当单词字母之间有 ⟦SLOT_112⟧1 个空格时，VLM 普遍表现更好（⟦SLOT_113⟧ 对 Sonnet-3 与 GPT-4o，从 0 个空格到 3 个空格分别为 +21 与 +13）。

**EN** Results All VLMs perform better on this task when there is ⟦SLOT_114⟧1 extra space between characters compared to when there is no extra space (Fig. 9b). However, the increase (⟦SLOT_115⟧) in accuracy varies across models. For instance, and ⟦SLOT_116⟧ accuracies increase by over +20 points to 92% and 72% from 72% and 46%, respectively (Fig. 9b).

**ZH** 结果：与没有额外空格时相比，当字符之间多出 ⟦SLOT_114⟧1 个空格时，所有 VLM 在该任务上表现更好（图 9b）。不过，准确率的提升幅度（⟦SLOT_115⟧）因模型而异。例如， 与 ⟦SLOT_116⟧ 的准确率提升了 20 个点以上，分别从 72% 与 46% 升至 92% 与 72%（图 9b）。

**EN** Out of 7 tested VLMs, Sonnet-3.5 reaches the highest accuracy of 95% when there are 3 extra spaces between letters (Fig. 9a). Qualitatively, the remaining 5% error (40 samples) includes: (1) 12 mispredictions of adjacent letters and (2) 13 instances of confusing the red circle as part of the letter, e.g., ‘@’ for ‘a’, and (3) 15 cases of predicting ‘g’ instead of ‘q’.

**ZH** 在 7 款受测 VLM 中，当字母之间有 3 个额外空格时，Sonnet-3.5 达到最高准确率 95%（图 9a）。定性地看，剩余 5% 的错误（40 个样本）包括：（1）12 例误判为相邻字母；（2）13 例把红圈误认为字母的一部分，例如把「a」认作「@」；（3）15 例把「q」预测为「g」。

**EN** Note that while the vision encoders in LLaVA-OneV with 72B (⟦SLOT_117⟧) and 0.5B (⟦SLOT_118⟧) are identical (400M SigLIP), the VLM with a larger Qwen2 language decoder (72B) substantially outperforms the counterpart with smaller decoder (Fig. 9b). This interestingly suggests that, at least in LLaVA-OneV family, the language decoder plays a major role in “reading out” which letter is being circled. On this task there is no slow-thinking [17] required and therefore, the language model (Qwen2) may act as an extended “vision” encoder on top of the SigLIP vision encoder, bottlenecking the accuracy of the LLaVA OneVision-qwen2-si-0.5B (⟦SLOT_119⟧ LLaVA-OneV-S).

**ZH** 需注意，尽管 72B（⟦SLOT_117⟧）与 0.5B（⟦SLOT_118⟧）版本的 LLaVA-OneV 使用相同的视觉编码器（400M SigLIP），但配备更大 Qwen2 语言解码器（72B）的 VLM 大幅优于配备更小解码器的对应版本（图 9b）。这有意思地提示：至少在 LLaVA-OneV 系列中，语言解码器在「读出」哪个字母被圈住这一点上起着主要作用。该任务不需要慢思考 [17]，因此语言模型（Qwen2）可能充当了 SigLIP 视觉编码器之上的一层扩展「视觉」编码器，成为 LLaVA OneVision-qwen2-si-0.5B（⟦SLOT_119⟧ LLaVA-OneV-S）准确率的瓶颈。

**EN** 5.2 VLMs can more accurately count disjoint shapes

**ZH** 5.2 VLM 能更准确地清点分离的形状

**EN** Inspired by the results of adding spaces to the circled letter task (Sec. 5.1), where VLMs see the letters better when there is more space between them, we also study the effects of the overlap area, i.e., the space between shapes, in counting overlapping shapes (for both ○ ○ ○ and ⬠ ⬠ ⬠ ). We aim to evaluate whether reducing the overlap area between shapes would improve VLM accuracy in counting them.

**ZH** 受在被圈字母任务中加入空格（第 5.1 节）的结果启发——当字母之间空间更大时 VLM 看得更清楚——我们也研究重叠面积（即形状之间的空间）对清点重叠形状的影响（对 ○ ○ ○ 与 ⬠ ⬠ ⬠ 二者）。我们旨在评估缩小形状之间的重叠面积是否会提升 VLM 清点的准确率。

**EN** Experiment The overlapping shapes in the baseline images (Sec. 3.4) are distanced in X and Y directions. To generate simplified versions of the images, we gradually increase these distances such that it reduces the overlapping area between the shapes. Specifically, the boundary-to-boundary distance between circles in the original images along the X and Y directions is ⟦SLOT_120⟧, where ⟦SLOT_121⟧ is the diameter of the circles and ⟦SLOT_122⟧ and ⟦SLOT_123⟧ are multipliers (see Fig. 10). We push the shapes away by increasing ⟦SLOT_124⟧ and ⟦SLOT_125⟧ for circles. We repeat the same procedure for pentagons with the boundary-to-boundary distance of ⟦SLOT_126⟧, where ⟦SLOT_127⟧ is the side length of the pentagons (see Fig. 11). We use the same prompts as in Sec. 3.4 to evaluate VLMs on the new pushed-away sets and compare their accuracy to the baseline results (in Sec. 4).

**ZH** 实验：基线图像（第 3.4 节）中的重叠形状在 X 与 Y 方向上存在间距。为生成图像的简化版本，我们逐步增大这些间距，以缩小形状之间的重叠面积。具体地，原始图像中圆在 X 与 Y 方向上的边界到边界距离为 ⟦SLOT_120⟧，其中 ⟦SLOT_121⟧ 是圆的直径，⟦SLOT_122⟧ 与 ⟦SLOT_123⟧ 是乘数（见图 10）。对圆，我们通过增大 ⟦SLOT_124⟧ 与 ⟦SLOT_125⟧ 把形状推开。对五边形我们重复同样的流程，其边界到边界距离为 ⟦SLOT_126⟧，其中 ⟦SLOT_127⟧ 是五边形的边长（见图 11）。我们用与第 3.4 节相同的提示，在推开后的新图像集上评估 VLM，并把准确率与基线结果（第 4 节）作比较。

<!-- [原子块 · table] ( d ​ y dy , d ​ x dx ) baseline: (-1.0, 0.1) (-0.75, 0.1) (-0.5, 0.1) (-0.25, 0.1) (0.0, 0.1) (0.25, 0.25) (0.5, 0.5) (0.75, 0.75) (1.0, 1.0) -->

**EN** Figure 10: We reduce the overlap area between circles by increasing the boundary-to-boundary distances along the X and Y axes, i.e., ⟦SLOT_128⟧ and ⟦SLOT_129⟧, respectively.

**ZH** 图 10：我们通过增大沿 X 轴与 Y 轴的边界到边界距离（即分别为 ⟦SLOT_128⟧ 与 ⟦SLOT_129⟧）来缩小圆之间的重叠面积。

<!-- [原子块 · table] ( d ​ y dy , d ​ x dx ) baseline: (-0.58, 0.1) (-0.5, 0.1) (-0.25, 0.1) (0.0, 0.1) (0.25, 0.25) (0.5, 0.5) (0.75, 0.75) (1.0, 1.0) -->

**EN** Figure 11: We increase the boundary-to-boundary distances between pentagons along the X and Y axes, i.e., ⟦SLOT_130⟧ and ⟦SLOT_131⟧, respectively.

**ZH** 图 11：我们增大五边形之间沿 X 轴与 Y 轴的边界到边界距离，即分别为 ⟦SLOT_130⟧ 与 ⟦SLOT_131⟧。

**EN** Results VLMs, in general, can count shapes more accurately when there is no overlapping area between shapes (Fig. 12). Yet, accuracy increases vary between models. For example, both Sonnet-3 and Sonnet-3.5 reach ⟦SLOT_132⟧96% (Fig. 12; ⟦SLOT_133⟧). Similarly, 72B-LLaVA-OneV (⟦SLOT_134⟧) achieves 72% accuracy on counting disjoint circles (Fig. 12; ⟦SLOT_135⟧).

**ZH** 结果：总的来看，当形状之间没有重叠区域时，VLM 能更准确地清点形状（图 12）。不过准确率的提升因模型而异。例如，Sonnet-3 与 Sonnet-3.5 都达到 ⟦SLOT_132⟧96%（图 12；⟦SLOT_133⟧）。类似地，72B-LLaVA-OneV（⟦SLOT_134⟧）在清点分离圆上达到 72% 准确率（图 12；⟦SLOT_135⟧）。

**EN** This shows that most VLMs struggle to count the shapes in the baseline images (Fig. 12; ⟦SLOT_136⟧ and ⟦SLOT_137⟧) because the shapes overlap, which poses a challenge to VLMs in counting.

**ZH** 这说明多数 VLM 难以清点基线图像中的形状（图 12；⟦SLOT_136⟧ 与 ⟦SLOT_137⟧），原因在于形状相互重叠，而这给 VLM 的清点带来挑战。

**EN** All closed-source VLMs, except for Gemini-1.5, consistently benefit from increasing the distance along both directions in counting overlapping shapes. The most significant improvement is for Sonnet-3 with ⟦SLOT_138⟧=91% and the least is for GPT-4o with ⟦SLOT_139⟧=22% (Fig. 12b). Qualitatively, this is mainly because counting more than 6 shapes is “hard” for Gemini-1.5 regardless of the amount of space between them due to its strong bias towards the Olympic logo (Sec. 4.4).

**ZH** 除 Gemini-1.5 外，所有闭源 VLM 都一致地受益于在两个方向上增大间距来清点重叠形状。提升最大的是 Sonnet-3（⟦SLOT_138⟧=91%），最小的是 GPT-4o（⟦SLOT_139⟧=22%）（图 12b）。定性地看，这主要是因为对 Gemini-1.5 而言，无论形状之间留有多少空间，清点 6 个以上形状都是「困难」的，因为它对奥运标志存在很强的偏差（第 4.4 节）。

**EN** Similarly to the circled letter task (Sec. 5.1), 72B LLaVA-OneV performs much better than 0.5B LLaVA-OneV-S on the simplified versions (Fig. 12). This further suggests that the language decoder in LLaVA-OneV significantly affects the VLM’s ability to see, count, and speak the number of shapes in the image.

**ZH** 与被圈字母任务（第 5.1 节）类似，72B 的 LLaVA-OneV 在简化版本上的表现远好于 0.5B 的 LLaVA-OneV-S（图 12）。这进一步说明，LLaVA-OneV 中的语言解码器显著影响着 VLM 看见、清点并说出图像中形状数量的能力。

<!-- [原子块 · table] (a) Circles ○ ○ ○ (b) Pentagons ⬠ ⬠ ⬠ d ​ y dy ↔ \leftrightarrow , d ​ x ↔ dx\leftrightarrow -->

**EN** Figure 12: As we increase the distance between the shapes along the X and Y axis for both circles and pentagons, VLMs’ accuracy improves. For example, Sonnet-3.5 (⟦SLOT_140⟧) accuracy increases from 0.66 to 1.0 on ○ ○ ○ (a) and from 0.78 to 1.0 on ⬠ ⬠ ⬠ (b).

**ZH** 图 12：随着我们沿 X 轴与 Y 轴增大圆与五边形之间的间距，VLM 的准确率提升。例如，Sonnet-3.5（⟦SLOT_140⟧）的准确率在 ○ ○ ○ 上从 0.66 升至 1.0（a），在 ⬠ ⬠ ⬠ 上从 0.78 升至 1.0（b）。

**EN** 5.3 VLMs can count simplified, more straight paths

**ZH** 5.3 VLM 能清点简化、更笔直的路径

**EN** VLMs’ ability to count can also affect the overall accuracy of SOTA models on counting single-colored paths ( ) in subway-like maps. To investigate whether VLMs are not able to count in general or whether the zigzag patterns of paths (Fig. 13a) poses the main challenge to VLMs, we render simplified versions of the original maps, where each path in the map contains fewer intersections with other paths. We evaluate the VLMs on the new set and compare their performance with the baseline images.

**ZH** VLM 的清点能力也会影响 SOTA 模型在清点类地铁图（ ）中单色路径上的整体准确率。为探究 VLM 究竟是一般而言不会清点，还是路径的锯齿形态（图 13a）才是对 VLM 的主要挑战，我们渲染原图的简化版本，其中每条路径与其他路径的相交更少。我们在新图像集上评估 VLM，并与基线图像上的表现作比较。

**EN** Experiment We re-render the images by forcing each path to have fewer ⟦SLOT_141⟧ turns than the baseline. The baseline images (Sec. 3.7) are implemented by choosing a direction on a grid using a random depth-first algorithm, where the probability (⟦SLOT_142⟧) of choosing a straight direction is 0.33. Therefore, we gradually increase the ⟦SLOT_143⟧ from the baseline (⟦SLOT_144⟧=0.33) to 0.6 and 0.9, such that it yields images with fewer intersections and turns (Fig. 13a). We use the prompts in Sec. 3.7 and compare VLMs’ performance with the baseline accuracy.

**ZH** 实验：我们通过强制每条路径的 ⟦SLOT_141⟧ 转折数少于基线来重新渲染图像。基线图像（第 3.7 节）通过在网格上用随机深度优先算法选择方向实现，其中选择直行方向的概率（⟦SLOT_142⟧）为 0.33。因此，我们把 ⟦SLOT_143⟧ 从基线（⟦SLOT_144⟧=0.33）逐步提高到 0.6 与 0.9，从而得到相交与转折更少的图像（图 13a）。我们使用第 3.7 节的提示，并把 VLM 的表现与基线准确率作比较。

**EN** Results On average, all VLMs more accurately count the single-colored paths when there are fewer turns, i.e., as ⟦SLOT_145⟧ increases (see Fig. 13b). The accuracy gain significantly varies between models, e.g., +2 points for GPT-4o and +30 for Sonnet-3.5 (Sec. 0.L.3). This shows that SOTA VLMs mostly struggle to count the paths in original images (Sec. 4) due to the visual complexity of zigzag patterns of paths and their intersection.

**ZH** 结果：平均而言，当转折更少时（即 ⟦SLOT_145⟧ 增大时），所有 VLM 都能更准确地清点单色路径（见图 13b）。准确率增益在模型之间差异显著，例如 GPT-4o 为 +2 个点，Sonnet-3.5 为 +30（第 0.L.3 节）。这说明 SOTA VLM 之所以难以清点原始图像（第 4 节）中的路径，主要是因为路径锯齿形态及其相交带来的视觉复杂性。

**EN** Analyzing the accuracy by the number of paths connected to each station, we find that some VLMs even score near-100 accuracy (e.g., 0.95, 0.99, and 0.95 for , , and ⟦SLOT_146⟧, respectively at ⟦SLOT_147⟧; Fig. 13). This substantially better accuracy on simplified images is in stark contrast to the poor accuracy reported for the original subway maps (⟦SLOT_148⟧), confirming that the visual complexity of the paths poses challenges to VLMs.

**ZH** 按连接到每个车站的路径条数分析准确率，我们发现部分 VLM 甚至取得接近 100 的准确率（例如 、 、 与 ⟦SLOT_146⟧ 在 ⟦SLOT_147⟧ 下分别为 0.95、0.99 与 0.95；图 13）。这种在简化图像上好得多的准确率，与原始地铁图上报告的糟糕准确率（⟦SLOT_148⟧）形成鲜明反差，印证了路径的视觉复杂性给 VLM 带来了挑战。

<!-- [原子块 · table] (a) P P values 0.33 (baseline) 0.6 0.9 -->

<!-- [原子块 · table] (b) 1 path 2 paths 3 paths -->

**EN** Figure 13: We increase the probability ⟦SLOT_149⟧ of choosing a straight next move (as opposed to making a turn) and generate two simplified versions of subway-like maps (a). As we increase the probability ⟦SLOT_150⟧ from 0.33 to 0.6 and 0.9 (b), some VLMs can reach a near-perfect accuracy (0.99 for Gemini-1.5 on 1 path).

**ZH** 图 13：我们提高选择直行（而非转弯）的概率 ⟦SLOT_149⟧，生成类地铁图的两个简化版本（a）。当把概率 ⟦SLOT_150⟧ 从 0.33 提高到 0.6 与 0.9 时（b），部分 VLM 能达到近乎完美的准确率（Gemini-1.5 在 1 条路径上为 0.99）。

**EN** 6 The vision encoder in open-source VLMs can extract sufficient information to solve BlindTest

**ZH** 6 开源 VLM 的视觉编码器能提取出足以解决 BlindTest 的信息

**EN** We find that VLMs surprisingly fail at simple tasks, e.g., determining whether two circles overlap or not (Sec. 4). Furthermore, our results in Sec. 5 show supporting evidence that these failures are not due to the uncommon nature of the questions in BlindTest or insufficient prompt engineering. Specifically, VLMs achieve near-100% accuracy when there is much more space between shapes and letters (Sec. 5). Therefore, here, we question whether VLMs can “see” the key visual information in BlindTest images, e.g., the gap between two circles ⟦SLOT_151⟧ in order to decide whether they overlap. Specifically, we run linear probing experiments to test whether the visual encoders of open-source VLMs extract sufficient information for solving BlindTest.

**ZH** 我们发现 VLM 在简单任务上意外地失败，例如判断两个圆是否重叠（第 4 节）。此外，第 5 节的结果提供了支持性证据，表明这些失败并非源于 BlindTest 中问题的非常规性质，也非提示工程不足。具体地，当形状与字母之间有更多空间时，VLM 能达到接近 100% 的准确率（第 5 节）。因此，这里我们要追问：VLM 能否「看见」BlindTest 图像中的关键视觉信息——例如两个圆之间的间隙 ⟦SLOT_151⟧，以判断它们是否重叠。具体地，我们运行线性探测实验，检验开源 VLM 的视觉编码器是否提取出足以解决 BlindTest 的信息。

**EN** Models From the SOTA open-source VLM families that we test in Tab. T1, we select two models, 0.5B LLaVA-OneV-S (⟦SLOT_152⟧) and 4.2B Phi-3.5 (⟦SLOT_153⟧) for two reasons. First, these two VLMs use the two most common vision encoders (VEs)—⟦SLOT_154⟧ uses SigLIP [59] while ⟦SLOT_155⟧ uses CLIP [41]. That is, our findings on these two VEs would generalize to most VLMs. Second, ⟦SLOT_156⟧ and ⟦SLOT_157⟧ are among the smallest VLMs, and therefore, if their VEs contain sufficient information, the same is likely true with larger and commercial VLMs.

**ZH** 模型：从表 T1 中我们所测试的 SOTA 开源 VLM 系列中，我们选出两个模型：0.5B 的 LLaVA-OneV-S（⟦SLOT_152⟧）与 4.2B 的 Phi-3.5（⟦SLOT_153⟧），原因有二。第一，这两款 VLM 使用最常见的两种视觉编码器（VE）——⟦SLOT_154⟧ 使用 SigLIP [59]，而 ⟦SLOT_155⟧ 使用 CLIP [41]。也就是说，我们关于这两种 VE 的发现可推广到多数 VLM。第二，⟦SLOT_156⟧ 与 ⟦SLOT_157⟧ 属于最小的 VLM 之列，因此若它们的 VE 含有充足信息，更大、商用的 VLM 很可能同样如此。

**EN** Tasks We choose (1) the two circles (⟦SLOT_158⟧) and (2) the counting line-intersections (⟦SLOT_159⟧) for this experiment because they represent arguably the simplest images and questions in BlindTest (the two circles and the line intersections tasks are 2-way and 3-way classification problems).

**ZH** 任务：我们选择（1）两个圆（⟦SLOT_158⟧）与（2）数直线交点（⟦SLOT_159⟧）用于本实验，因为它们可以说是 BlindTest 中最简单的图像与问题（两圆任务与直线交点任务分别是二分类与三分类问题）。

**EN** We generate 11,100 two-circle ⟦SLOT_160⟧ images with a uniform distribution of images over circle distances (⟦SLOT_161⟧, ⟦SLOT_162⟧). We divide these images into (8880, 1110, 1110) images for train, val, and test sets, respectively. Repeating this generation process for the line-intersection task (⟦SLOT_163⟧) with an equal distribution of mean distances between the y coordinates of the red and blue lines (similar to Fig. 2) for a total of 6,300 images, i.e., divided into (4410, 945, 945) for train, val, and test sets.

**ZH** 我们生成 11,100 张两圆 ⟦SLOT_160⟧ 图像，图像在圆的间距（⟦SLOT_161⟧、⟦SLOT_162⟧）上呈均匀分布。我们把这些图像划分为训练集、验证集与测试集，分别为（8880、1110、1110）张。对直线交点任务（⟦SLOT_163⟧）重复同样的生成流程，红蓝两线 y 坐标之间的平均距离均匀分布（类似图 2），共 6,300 张图像，划分为（4410、945、945）用于训练、验证与测试。

<!-- [原子块 · object]  -->

**EN** Figure 14: We train a linear-probing classifier on the frozen features extracted from the (1) vision encoder and the (2) projection layer for the two circles ⟦SLOT_164⟧ and the line chart ⟦SLOT_165⟧ tasks separately. Evaluating the linear classifiers shows that the information necessary to solve these two tasks exists before and after the project layer but is lost in the LLM, resulting in poor VLM accuracy in Sec. 4.

**ZH** 图 14：我们分别在两圆 ⟦SLOT_164⟧ 与折线图 ⟦SLOT_165⟧ 任务上，基于（1）视觉编码器与（2）投影层提取的冻结特征训练线性探测分类器。对线性分类器的评估显示，解决这两项任务所需的信息在投影层前后都存在，却在 LLM 中丢失，导致第 4 节中 VLM 的糟糕准确率。

**EN** Method We average-pool the image-patch features at the layer right before the projection layer (Fig. 14). Then, we train a logistic-regression linear classifier on top of the frozen features on each task. We train each classifier for 1,000 epochs with ⟦SLOT_166⟧ regularization weight of 1.0 (Tab. T18) and choose the best model based on the validation set. The dimensions of the features are described in Sec. 0.N.1. For completeness, we repeat the experiment for the layer right after the projection layer to understand the impact of the projection layer.

**ZH** 方法：我们在投影层前一层的图像块特征上做平均池化（图 14）。随后，在每个任务的冻结特征之上训练一个逻辑回归线性分类器。每个分类器训练 1,000 轮，⟦SLOT_166⟧ 正则化权重为 1.0（表 T18），并依据验证集选择最佳模型。特征维度见第 0.N.1 节。为完备起见，我们也在投影层后一层重复该实验，以理解投影层的影响。

**EN** Results The linear-probing accuracy of the CLIP features, before projection layer, in ⟦SLOT_167⟧ is ⟦SLOT_168⟧ 99.47% on both tasks (Tab. 5). This suggests that the necessary low-level information to solve these tasks is preserved in CLIP. Similarly, the same conclusion holds for the VE in ⟦SLOT_169⟧, a variant of SigLIP, that performs 100% on both tasks (Tab. 5). Moreover, using the frozen features after the projection layer in both ⟦SLOT_170⟧ and ⟦SLOT_171⟧ yields a linear classification accuracy of ⟦SLOT_172⟧ 99.58% on both tasks (Tab. 5). This result shows that most visual information from VEs is preserved before and after the projection layer. Contrasting these high linear-classification VE accuracy scores with fairly lower accuracy of both VLMs on BlindTest (see Tab. 5; rightmost column), we conclude that the language models in these VLMs have access to the necessary visual information to solve BlindTest tasks but fail to decode it into correct language outputs.

**ZH** 结果：在 ⟦SLOT_167⟧ 中，投影层之前的 CLIP 特征线性探测准确率在两项任务上均为 ⟦SLOT_168⟧ 99.47%（表 5）。这说明解决这些任务所需的低层信息在 CLIP 中得以保留。同样，⟦SLOT_169⟧（SigLIP 的一个变体）中的 VE 也得出同样结论——它在两项任务上都达到 100%（表 5）。此外，在 ⟦SLOT_170⟧ 与 ⟦SLOT_171⟧ 中使用投影层之后的冻结特征，线性分类准确率在两项任务上均为 ⟦SLOT_172⟧ 99.58%（表 5）。这一结果表明，来自 VE 的大部分视觉信息在投影层前后都得以保留。把这些很高的 VE 线性分类准确率与两款 VLM 在 BlindTest 上相当低的准确率作对比（见表 5；最右列），我们得出结论：这些 VLM 中的语言模型能够获取解决 BlindTest 任务所需的视觉信息，却未能把它解码为正确的语言输出。

**EN** Interestingly, in the two-circles ⟦SLOT_173⟧ task, training on frozen features of images, where the two circles are close (⟦SLOT_174⟧) produces a linear classifier that performs perfectly at 100% accuracy not only on that training distribution but also on splits containing circles that are farther apart (e.g., ⟦SLOT_175⟧) regardless of the VE (⟦SLOT_176⟧ and ⟦SLOT_177⟧). However, the opposite does not hold—training on the images where circles are farther apart (⟦SLOT_178⟧) results in a classifier that performs poorly on circles that are closer. More details in Sec. 0.N.2. This result shows evidence that (1) training on the harder cases (⟦SLOT_179⟧) results in a more robust classifier and (2) our classifiers do not overfit to training data.

**ZH** 有意思的是，在两圆 ⟦SLOT_173⟧ 任务中，用两个圆靠得较近（⟦SLOT_174⟧）的图像的冻结特征训练出的线性分类器，不但在该训练分布上达到 100% 的完美表现，在包含相距更远（例如 ⟦SLOT_175⟧）的圆的划分上也同样完美，且与所用 VE（⟦SLOT_176⟧ 与 ⟦SLOT_177⟧）无关。反之则不成立——用圆相距更远（⟦SLOT_178⟧）的图像训练出的分类器，在圆靠得更近时表现很差。详见第 0.N.2 节。这一结果为两点提供了证据：（1）在更困难的样本（⟦SLOT_179⟧）上训练能得到更稳健的分类器；（2）我们的分类器并未过拟合训练数据。

**EN** Table 5: The output features from the vision encoders right before (a) the projection layer in LLaVA-OneV-S (⟦SLOT_180⟧) and Phi-3.5 (⟦SLOT_181⟧), i.e., CLIP and SigLIP, respectively, contain sufficient information to solve the ⟦SLOT_182⟧ and ⟦SLOT_183⟧ (linear-probing accuracy is ⟦SLOT_184⟧ 99.47%). The same conclusion holds for after (b) the projection layer. However, the language model in these VLMs fails to decode this information into correct answers, resulting in poor accuracy on the tasks (c).

**ZH** 表 5：LLaVA-OneV-S（⟦SLOT_180⟧）与 Phi-3.5（⟦SLOT_181⟧）中投影层（a）之前的视觉编码器输出特征（分别为 CLIP 与 SigLIP）含有足以解决 ⟦SLOT_182⟧ 与 ⟦SLOT_183⟧ 的信息（线性探测准确率为 ⟦SLOT_184⟧ 99.47%）。投影层之后（b）也成立同样的结论。然而，这些 VLM 中的语言模型未能把这些信息解码为正确答案，导致任务上的准确率很差（c）。

<!-- [原子块 · table] (a) Before (b) After (c) VLM Model 99.47 99.82 99.58 99.73 33.14 73.21 100.0 100.0 100.0 100.0 37.78 83.63 -->

**EN** 7 Related Work

**ZH** 7 相关工作

**EN** Benchmarking VLM vision understanding College-level topics [57], charts [30], documents [31] or videos [56] are among the common benchmarks for assessing VLM vision understanding [38, 4, 43, 2] and are witnessing VLMs’ recent rapid progress—e.g., Sonnet-3.5 is reaching 95.2% on DocVQA, 90.8% on ChartQA, and 94.7% on AI2D [2]. However, most of the vision benchmarks attempt to evaluate VLMs on real-world, topic-specific data that require extensive prior knowledge [21, 50, 6], which has a “data leakage” problem, i.e., VLMs many times can answer accurately without even the input image [6]. Furthermore, most benchmarks test VLMs on the data that humans have to deal with to provide a high-level sense of the human-machine intelligence gap [55, 26]. In contrast, our BlindTest benchmark differs significantly from prior benchmarks because it is (1) extremely easy to humans and can be solved by a 5-year-old (unlike [57, 30, 31]); (2) the first low-level, visual sanity check for VLMs; (3) requiring minimal to zero prior knowledge; (4) requiring minimal commonsense or complex reasoning (unlike [8, 58])—i.e., a strong language model is of little use here when it is non-natural for humans to describe BlindTest images in language.

**ZH** VLM 视觉理解的基准评测：大学水平的学科 [57]、图表 [30]、文档 [31] 或视频 [56] 是评估 VLM 视觉理解的常见基准 [38, 4, 43, 2]，也见证了 VLM 近期的快速进展——例如 Sonnet-3.5 在 DocVQA 上达到 95.2%、在 ChartQA 上达到 90.8%、在 AI2D 上达到 94.7% [2]。然而，多数视觉基准试图在需要大量先验知识的真实世界、特定领域数据上评估 VLM [21, 50, 6]，这存在「数据泄露」问题，即 VLM 很多时候甚至不需要输入图像就能准确作答 [6]。此外，多数基准在人类必须处理的数据上测试 VLM，以给出人机智能差距的高层印象 [55, 26]。相比之下，我们的 BlindTest 基准与此前基准显著不同，因为它（1）对人类极其简单，五岁小孩即可解决（不同于 [57, 30, 31]）；（2）是首个面向 VLM 的低层视觉有效性检验；（3）只需极少乃至零先验知识；（4）只需极少的常识或复杂推理（不同于 [8, 58]）——也就是说，当人类难以用语言描述 BlindTest 图像时，强大的语言模型在此用处不大。

**EN** The ARC benchmark [36, 8] also contains abstract images made up of simple shapes; however, it challenges VLMs to understand and reason based on those patterns. That is, ARC assumes VLMs can identify the abstract shapes in order to reason. In contrast, our BlindTest directly evaluates VLM capabilities in recognizing these primitive shapes.

**ZH** ARC 基准 [36, 8] 同样包含由简单形状构成的抽象图像；不过它要求 VLM 理解这些图案并据此推理，即 ARC 假定 VLM 能够识别这些抽象形状以便推理。相比之下，我们的 BlindTest 直接评估 VLM 识别这些图元形状的能力。

**EN** Improving VLM vision capabilities Most recent recipes for improving SOTA VLMs involve finetuning a pretrained LLM coupled with vision encoders to solve high-level vision tasks [24]. Such late-fusion approaches fuse visual representations learned from the tokenized image with a powerful thinking brain [33, 23, 22]. However, current vision approaches for VLMs are facing challenges as models sometimes are “blind”—unable to see natural objects exist in a real photo [49]. In contrast, we are showing VLMs are visually impaired at low-level abstract images, e.g., inability to count 6 overlapping circles or 3 nested squares.

**ZH** 提升 VLM 视觉能力：近期改进 SOTA VLM 的多数方案，都是微调一个预训练 LLM 并配以视觉编码器，以解决高层视觉任务 [24]。这类后期融合方法把从图像 token 化后学到的视觉表征与一个强大的「思考大脑」融合 [33, 23, 22]。然而，当前 VLM 的视觉方案正面临挑战，因为模型有时是「盲」的——看不见真实照片中存在的自然物体 [49]。相比之下，我们表明 VLM 在低层抽象图像上存在视觉缺陷，例如无法清点 6 个重叠圆或 3 个嵌套正方形。

**EN** Our circled-letter task (Sec. 3.3) is inspired by VLM abilities in recognizing content inside a red circle over real objects in natural images [53, 44, 54]. In contrast, we show that VLMs can fail at a low-level, optical character recognition as opposed to recognizing real objects. To the best of our knowledge, no prior attempts have been made to address the exact limitations raised in our paper: (1) identifying and counting simple lines, shapes and geometric primitives when they interact (Sec. 4.1 to Sec. 4.5); (2) following colored paths (Sec. 4.6). Solving these limitations may be the foundation for VLMs to progress on some existing vision benchmarks on graphs, e.g., [19], visual math [27] and some existing blind-spots in natural images (e.g., understanding the direction an object is facing [49]).

**ZH** 我们的被圈字母任务（第 3.3 节）受启发于 VLM 识别自然图像中真实物体上红圈内内容的能力 [53, 44, 54]。相比之下，我们表明 VLM 会在低层的光学字符识别上失败，而非在识别真实物体上失败。据我们所知，此前尚无工作针对本文提出的确切局限：（1）在直线、形状与几何图元相互作用时识别并清点它们（第 4.1 至 4.5 节）；（2）追踪彩色路径（第 4.6 节）。解决这些局限，可能是 VLM 在图结构相关既有视觉基准（例如 [19]）、视觉数学 [27]，以及自然图像中某些既有盲区（例如理解物体所朝的方向 [49]）上取得进展的基础。

**EN** 8 Discussion and Conclusion

**ZH** 8 讨论与结论

**EN** We propose BlindTest, a benchmark of seven novel low-level visual tasks for testing VLM ability to “see” simple geometric primitives (such as line, circles, squares, intersections) that are the basic building blocks for many image tasks. The tasks are designed from scratch and require minimal to zero knowledge. As the tasks did not exist on the Internet before and require minimal world knowledge, there is minimal chance that VLMs can solve BlindTest by memorization or by not using the input image—an issue in some prior benchmarks [6, 13].

**ZH** 我们提出 BlindTest——一个包含七项新颖低层视觉任务的基准，用于测试 VLM「看见」简单几何图元（如直线、圆、正方形、交点）的能力，这些图元是许多图像任务的基本构件。这些任务从零开始设计，只需极少乃至零知识。由于这些任务此前不存在于互联网上，且只需极少的常识性知识，VLM 靠记忆或不使用输入图像来解决 BlindTest 的可能性极小——而后者正是某些既有基准存在的问题 [6, 13]。

**EN** Furthermore, we also test common prompting techniques (Sec. 0.D.1) including 2-shot, chain-of-thought [52], and meta-prompting [34] but do not obtain better accuracy, which (1) suggests that VLMs understand BlindTest questions and (2) confirms that these visual tasks do not benefit from thinking aloud [52].

**ZH** 此外，我们还测试了常见的提示技术（第 0.D.1 节），包括 2-shot、思维链 [52] 与元提示 [34]，但并未获得更好的准确率，这（1）说明 VLM 理解 BlindTest 的问题；（2）印证了这些视觉任务并不能从「出声思考」[52] 中获益。

**EN** The poor performance of VLMs on BlindTest suggests that models will perform poorly on the real-world visual tasks that require them to follow arrow directions or paths, (e.g., reading subway maps in Fig. F46, street maps or directed graphs in Fig. F47), perceive lines and intersections (e.g., reading music sheets; Fig. F47), identify and counts objects in a crowded scene.

**ZH** VLM 在 BlindTest 上的糟糕表现提示，模型在需要追踪箭头方向或路径的真实视觉任务上也会表现不佳（例如阅读图 F46 中的地铁图、街道地图或图 F47 中的有向图）、在感知线条与交点上表现不佳（例如阅读乐谱；图 F47），以及在拥挤场景中识别与清点物体上表现不佳。

**EN** Acknowledgement

**ZH** 致谢

**EN** We thank Hung H. Nguyen, Thang Pham, Ali Yildirim, Giang Nguyen, and Tin Nguyen at Auburn University for feedback and discussions of the earlier results. We are also thankful for the API research credits from Anthropic and together.ai to MRT. AN was supported by the NSF Grant No. 1850117 & 2145767, and donations from NaphCare Foundation & Adobe Research.

**ZH** 我们感谢奥本大学的 Hung H. Nguyen、Thang Pham、Ali Yildirim、Giang Nguyen 与 Tin Nguyen 对早期结果的反馈与讨论。我们也感谢 Anthropic 与 together.ai 向 MRT 提供的 API 研究额度。AN 受 NSF 资助 No. 1850117 与 2145767，以及 NaphCare 基金会与 Adobe Research 的捐赠支持。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] [1] Abdin, M., Jacobs, S.A., Awan, A.A., Aneja, J., Awadallah, A., Awadalla, H., Bach, N., Bahree, A., Bakhtiari, A., Behl, H., et al.: Phi-3 technical report: A highly capable language model locally  -->

<!-- [原子块 · verbatim] [2] Anthropic: Introducing claude 3.5 sonnet \ anthropic. https://www.anthropic.com/news/claude-3-5-sonnet , (Accessed on 07/03/2024) -->

<!-- [原子块 · verbatim] [3] Anthropic: Introducing the next generation of claude \ anthropic. https://www.anthropic.com/news/claude-3-family , (Accessed on 07/23/2024) -->

<!-- [原子块 · verbatim] [4] Anthropic, A.: The claude 3 model family: Opus, sonnet, haiku. Claude-3 Model Card (2024) -->

<!-- [原子块 · verbatim] [5] Bailey, I.L., Lovie-Kitchin, J.E.: Visual acuity testing. from the laboratory to the clinic. Vision research 90 , 2–9 (2013) -->

<!-- [原子块 · verbatim] [6] Chen, L., Li, J., Dong, X., Zhang, P., Zang, Y., Chen, Z., Duan, H., Wang, J., Qiao, Y., Lin, D., et al.: Are we on the right way for evaluating large vision-language models? arXiv preprint arXiv: -->

<!-- [原子块 · verbatim] [7] Chen, Z., Wu, J., Wang, W., Su, W., Chen, G., Xing, S., Zhong, M., Zhang, Q., Zhu, X., Lu, L., Li, B., Luo, P., Lu, T., Qiao, Y., Dai, J.: Internvl: Scaling up vision foundation models and alignin -->

<!-- [原子块 · verbatim] [8] Chollet, F.: On the measure of intelligence. arXiv preprint arXiv:1911.01547 (2019) -->

<!-- [原子块 · verbatim] [9] Custer, G.: Gemini spatial example. https://gemini-spatial-example.grantcuster.com/ , (Accessed on 05/31/2024) -->

<!-- [原子块 · verbatim] [10] Dai, W., Li, J., Li, D., Tiong, A.M.H., Zhao, J., Wang, W., Li, B., Fung, P., Hoi, S.: Instructblip: Towards general-purpose vision-language models with instruction tuning (2023) -->

<!-- [原子块 · verbatim] [11] Gou, C., Felemban, A., Khan, F.F., Zhu, D., Cai, J., Rezatofighi, H., Elhoseiny, M.: How well can vision language models see image details? arXiv preprint arXiv:2408.03940 (2024) -->

<!-- [原子块 · verbatim] [12] He, M., Liu, Y., Wu, B., Yuan, J., Wang, Y., Huang, T., Zhao, B.: Efficient multimodal learning from data-centric perspective. arXiv preprint arXiv:2402.11530 (2024) -->

<!-- [原子块 · verbatim] [13] Hegde, N., Paul, S., Madan, G., Aggarwal, G.: Analyzing the efficacy of an llm-only approach for image-based document question answering. arXiv preprint arXiv:2309.14389 (2023) -->

<!-- [原子块 · verbatim] [14] Hughes, J.F.: Computer graphics: principles and practice. Pearson Education (2014) -->

<!-- [原子块 · verbatim] [15] Inc., C.Z.V.: Vision screening. https://www.zeiss.com/vision-care/us/eye-health-and-care/vision-screening.html , (Accessed on 07/03/2024) -->

<!-- [原子块 · verbatim] [16] Jaech, A., Kalai, A., Lerer, A., Richardson, A., El-Kishky, A., Low, A., Helyar, A., Madry, A., Beutel, A., Carney, A., et al.: Openai o1 system card. arXiv preprint arXiv:2412.16720 (2024) -->

<!-- [原子块 · verbatim] [17] Kahneman, D.: Thinking, fast and slow. macmillan (2011) -->

<!-- [原子块 · verbatim] [18] Kembhavi, A., Salvato, M., Kolve, E., Seo, M., Hajishirzi, H., Farhadi, A.: A diagram is worth a dozen images. In: Computer Vision–ECCV 2016: 14th European Conference, Amsterdam, The Netherlands, -->

<!-- [原子块 · verbatim] [19] yunxin li, Hu, B., Shi, H., Wang, W., Wang, L., Zhang, M.: Visiongraph: Leveraging large multimodal models for graph theory problems in visual context. In: Forty-first International Conference on -->

<!-- [原子块 · verbatim] [20] Li, B., Zhang, Y., Guo, D., Zhang, R., Li, F., Zhang, H., Zhang, K., Li, Y., Liu, Z., Li, C.: Llava-onevision: Easy visual task transfer. arXiv preprint arXiv:2408.03326 (2024) -->

<!-- [原子块 · verbatim] [21] Liang, Z., Guo, K., Liu, G., Guo, T., Zhou, Y., Yang, T., Jiao, J., Pi, R., Zhang, J., Zhang, X.: Scemqa: A scientific college entrance level multimodal question answering benchmark. arXiv prepri -->

<!-- [原子块 · verbatim] [22] Liu, H., Li, C., Li, Y., Lee, Y.J.: Improved baselines with visual instruction tuning (2023) -->

<!-- [原子块 · verbatim] [23] Liu, H., Li, C., Li, Y., Li, B., Zhang, Y., Shen, S., Lee, Y.J.: Llava-next: Improved reasoning, ocr, and world knowledge (January 2024), https://llava-vl.github.io/blog/2024-01-30-llava-next/ -->

<!-- [原子块 · verbatim] [24] Liu, H., Li, C., Wu, Q., Lee, Y.J.: Visual instruction tuning. arXiv preprint arXiv:2304.08485 (2023) -->

<!-- [原子块 · verbatim] [25] Liu, H., Li, C., Wu, Q., Lee, Y.J.: Visual instruction tuning. Advances in neural information processing systems 36 (2024) -->

<!-- [原子块 · verbatim] [26] Liu, Y., Duan, H., Zhang, Y., Li, B., Zhang, S., Zhao, W., Yuan, Y., Wang, J., He, C., Liu, Z., et al.: Mmbench: Is your multi-modal model an all-around player? arXiv preprint arXiv:2307.06281 (2 -->

<!-- [原子块 · verbatim] [27] Lu, P., Bansal, H., Xia, T., Liu, J., Li, C., Hajishirzi, H., Cheng, H., Chang, K.W., Galley, M., Gao, J.: Mathvista: Evaluating mathematical reasoning of foundation models in visual contexts. In -->

<!-- [原子块 · verbatim] [28] Mangalam, K., Akshulakov, R., Malik, J.: Egoschema: A diagnostic benchmark for very long-form video language understanding. Advances in Neural Information Processing Systems 36 (2024) -->

<!-- [原子块 · verbatim] [29] Mäntyjärvi, M., Laitinen, T.: Normal values for the pelli-robson contrast sensitivity test. Journal of Cataract & Refractive Surgery 27 (2), 261–266 (2001) -->

<!-- [原子块 · verbatim] [30] Masry, A., Do, X.L., Tan, J.Q., Joty, S., Hoque, E.: ChartQA: A benchmark for question answering about charts with visual and logical reasoning. In: Muresan, S., Nakov, P., Villavicencio, A. (eds -->

<!-- [原子块 · verbatim] [31] Mathew, M., Karatzas, D., Jawahar, C.: Docvqa: A dataset for vqa on document images. In: Proceedings of the IEEE/CVF winter conference on applications of computer vision. pp. 2200–2209 (2021) -->

<!-- [原子块 · verbatim] [32] McGuinness, P.: Gpt-4 system prompt revealed - by patrick mcguinness. https://patmcguinness.substack.com/p/gpt-4-system-prompt-revealed , (Accessed on 06/06/2024) -->

<!-- [原子块 · verbatim] [33] McKinzie, B., Gan, Z., Fauconnier, J.P., Dodge, S., Zhang, B., Dufter, P., Shah, D., Du, X., Peng, F., Weers, F., Belyi, A., Zhang, H., Singh, K., Kang, D., Jain, A., He, H., Schwarzer, M., Gunte -->

<!-- [原子块 · verbatim] [34] Mirza, M.J., Karlinsky, L., Lin, W., Doveh, S., Micorek, J., Kozinski, M., Kuhene, H., Possegger, H.: Meta-prompting for automating zero-shot visual recognition with llms. arXiv preprint arXiv:24 -->

<!-- [原子块 · verbatim] [35] Mirza, M.J., Karlinsky, L., Lin, W., Doveh, S., Micorek, J., Kozinski, M., Kuhene, H., Possegger, H.: Meta-prompting for automating zero-shot visual recognition with llms. arXiv preprint arXiv:24 -->

<!-- [原子块 · verbatim] [36] Mitchell, M., Palmarini, A.B., Moskvichev, A.K.: Comparing humans, GPT-4, and GPT-4v on abstraction and reasoning tasks. In: AAAI 2024 Workshop on ”Are Large Language Models Simply Causal Parrots -->

<!-- [原子块 · verbatim] [37] Olya.by@mail.ru: How many counting game with color simple geometric shapes for kids, educational maths task for the development of logical thinking, preschool worksheet activity, count and write  -->

<!-- [原子块 · verbatim] [38] OpenAI: Hello gpt-4o | openai. https://openai.com/index/hello-gpt-4o/ , (Accessed on 05/31/2024) -->

<!-- [原子块 · verbatim] [39] OpenAI: Gpt-4 technical report (2023) -->

<!-- [原子块 · verbatim] [40] Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C., Mishkin, P., Zhang, C., Agarwal, S., Slama, K., Ray, A., et al.: Training language models to follow instructions with human feedback. A -->

<!-- [原子块 · verbatim] [41] Radford, A., Kim, J.W., Hallacy, C., Ramesh, A., Goh, G., Agarwal, S., Sastry, G., Askell, A., Mishkin, P., Clark, J., Krueger, G., Sutskever, I.: Learning transferable visual models from natural -->

<!-- [原子块 · verbatim] [42] Rasheed, H., Maaz, M., Shaji, S., Shaker, A., Khan, S., Cholakkal, H., Anwer, R.M., Xing, E., Yang, M.H., Khan, F.S.: Glamm: Pixel grounding large multimodal model. The IEEE/CVF Conference on Com -->

<!-- [原子块 · verbatim] [43] Reid, M., Savinov, N., Teplyashin, D., Lepikhin, D., Lillicrap, T., Alayrac, J.b., Soricut, R., Lazaridou, A., Firat, O., Schrittwieser, J., et al.: Gemini 1.5: Unlocking multimodal understanding -->

<!-- [原子块 · verbatim] [44] Shtedritski, A., Rupprecht, C., Vedaldi, A.: What does clip know about a red circle? visual prompt engineering for vlms. In: 2023 IEEE/CVF International Conference on Computer Vision (ICCV). pp.  -->

<!-- [原子块 · verbatim] [45] Station, M.T.: Count shapes printables | myteachingstation.com. https://www.myteachingstation.com/preschool/math/numbers/count-shapes-printables , (Accessed on 07/05/2024) -->

<!-- [原子块 · verbatim] [46] Taesiri, M.R., Feng, T., Bezemer, C.P., Nguyen, A.: Glitchbench: Can large multimodal models detect video game glitches? In: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern  -->

<!-- [原子块 · verbatim] [47] Team, C.: Chameleon: Mixed-modal early-fusion foundation models. arXiv preprint arXiv:2405.09818 (2024) -->

<!-- [原子块 · verbatim] [48] Team, Q.: Qvq: To see the world with wisdom (December 2024), https://qwenlm.github.io/blog/qvq-72b-preview/ -->

<!-- [原子块 · verbatim] [49] Tong, S., Liu, Z., Zhai, Y., Ma, Y., LeCun, Y., Xie, S.: Eyes wide shut? exploring the visual shortcomings of multimodal llms. In: Proceedings of the IEEE/CVF Conference on Computer Vision and Pa -->

<!-- [原子块 · verbatim] [50] Wang, K., Pan, J., Shi, W., Lu, Z., Zhan, M., Li, H.: Measuring multimodal mathematical reasoning with math-vision dataset (2024) -->

<!-- [原子块 · verbatim] [51] Wang, P., Bai, S., Tan, S., Wang, S., Fan, Z., Bai, J., Chen, K., Liu, X., Wang, J., Ge, W., Fan, Y., Dang, K., Du, M., Ren, X., Men, R., Liu, D., Zhou, C., Zhou, J., Lin, J.: Qwen2-vl: Enhancing -->

<!-- [原子块 · verbatim] [52] Wei, J., Wang, X., Schuurmans, D., Bosma, M., Xia, F., Chi, E., Le, Q.V., Zhou, D., et al.: Chain-of-thought prompting elicits reasoning in large language models. Advances in Neural Information P -->

<!-- [原子块 · verbatim] [53] Yang, J., Zhang, H., Li, F., Zou, X., Li, C., Gao, J.: Set-of-mark prompting unleashes extraordinary visual grounding in gpt-4v (2023), https://arxiv.org/abs/2310.11441 -->

<!-- [原子块 · verbatim] [54] Yang, Z., Li, L., Lin, K., Wang, J., Lin, C., Liu, Z., Wang, L.: The dawn of lmms: Preliminary explorations with gpt-4v(ision). CoRR abs/2309.17421 (2023). https://doi.org/10.48550/ARXIV.2309.174 -->

<!-- [原子块 · verbatim] [55] Yu, W., Yang, Z., Li, L., Wang, J., Lin, K., Liu, Z., Wang, X., Wang, L.: Mm-vet: Evaluating large multimodal models for integrated capabilities. In: International conference on machine learning. -->

<!-- [原子块 · verbatim] [56] Yu, Z., Xu, D., Yu, J., Yu, T., Zhao, Z., Zhuang, Y., Tao, D.: Activitynet-qa: a dataset for understanding complex web videos via question answering. In: Proceedings of the Thirty-Third AAAI Conf -->

<!-- [原子块 · verbatim] [57] Yue, X., Ni, Y., Zhang, K., Zheng, T., Liu, R., Zhang, G., Stevens, S., Jiang, D., Ren, W., Sun, Y., Wei, C., Yu, B., Yuan, R., Sun, R., Yin, M., Zheng, B., Yang, Z., Liu, Y., Huang, W., Sun, H., -->

<!-- [原子块 · verbatim] [58] Zellers, R., Bisk, Y., Farhadi, A., Choi, Y.: From recognition to cognition: Visual commonsense reasoning. In: Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. p -->

<!-- [原子块 · verbatim] [59] Zhai, X., Mustafa, B., Kolesnikov, A., Beyer, L.: Sigmoid loss for language image pre-training. In: Proceedings of the IEEE/CVF International Conference on Computer Vision. pp. 11975–11986 (2023) -->

**EN** Appendix for: Vision language models are blind: Failing to translate detailed visual features into words

**ZH** 附录：视觉语言模型是「盲」的：无法把精细的视觉特征转译为文字

**EN** Appendix 0.A Description of models tested

**ZH** 附录 0.A 受测模型的说明

**EN** On our benchmark, we find that some chat interfaces perform worse than their API counterparts (e.g., the system on gemini.google.com is worse than Gemini-1.5 Pro on aistudio.google.com) perhaps due to their extra finetuning [40] or specific system prompts [32] that attempt to align VLMs with a company’s policies. Similarly, we find GPT-4o and Claude 3 models in perplexity.ai to perform worse than the original API models. To make sure we test the best VLMs available, we access all four models via their available APIs on OpenAI, Google, and Anthropic.

**ZH** 在我们的基准上，我们发现某些聊天界面的表现不如其 API 对应版本（例如 gemini.google.com 上的系统不如 aistudio.google.com 上的 Gemini-1.5 Pro），或许是因为它们额外的微调 [40]，或旨在使 VLM 与某公司策略保持一致的特定系统提示 [32]。类似地，我们发现 perplexity.ai 中的 GPT-4o 与 Claude 3 模型表现不如原始 API 模型。为确保我们测试的是当前可用的最佳 VLM，我们通过 OpenAI、Google 与 Anthropic 各自提供的 API 访问全部四款模型。

**EN** We describe below the exact API versions and settings for each model.

**ZH** 下面说明每个模型的确切 API 版本与设置。

**EN** 0.A.1 GPT-4o

**ZH** 0.A.1 GPT-4o

**EN** We access the API for GPT-4o (gpt-4o-2024-05-13) via platform.openai.com and use all default settings including:

**ZH** 我们通过 platform.openai.com 访问 GPT-4o（gpt-4o-2024-05-13）的 API，并使用包括下列各项在内的全部默认设置：

**EN** • temperature: 1.0

**ZH** • temperature：1.0

**EN** • detail: auto (see API doc), i.e., the system will automatically decide whether to use the “low-res” (85 tokens) or “high-res” mode (85 tokens and a set of 170 tokens for every 512⟦SLOT_185⟧512 tile).

**ZH** • detail：auto（见 API 文档），即系统将自动决定使用「低分辨率」（85 个 token）还是「高分辨率」模式（85 个 token，并为每个 512⟦SLOT_185⟧512 图块追加一组 170 个 token）。

**EN** 0.A.2 Gemini-1.5 Pro

**ZH** 0.A.2 Gemini-1.5 Pro

**EN** Gemini-1.5 (gemini-1.5-pro-latest) API is accessible via aistudio.google.com, and we use all default settings.

**ZH** Gemini-1.5（gemini-1.5-pro-latest）的 API 可通过 aistudio.google.com 访问，我们使用全部默认设置。

**EN** 0.A.3 Claude-3 Sonnet

**ZH** 0.A.3 Claude-3 Sonnet

**EN** We access the anthropic API via console.anthropic.com to use Sonnet-3 (claude-3-sonnet-20240229) with default settings.

**ZH** 我们通过 console.anthropic.com 访问 Anthropic API，以默认设置使用 Sonnet-3（claude-3-sonnet-20240229）。

**EN** 0.A.4 Claude-3.5 Sonnet

**ZH** 0.A.4 Claude-3.5 Sonnet

**EN** We follow the same process as for Sonnet-3 and use console.anthropic.com to access Sonnet-3.5 (claude-3-5-sonnet-20240620) API with default settings.

**ZH** 我们沿用与 Sonnet-3 相同的流程，通过 console.anthropic.com 以默认设置访问 Sonnet-3.5（claude-3-5-sonnet-20240620）API。

**EN** 0.A.5 LLaVA OneVision-qwen2

**ZH** 0.A.5 LLaVA OneVision-qwen2

**EN** We run the publicly available code of LLaVA OneVision-qwen2 locally with temperature=0.2.

**ZH** 我们在本地运行 LLaVA OneVision-qwen2 的公开代码，temperature=0.2。

**EN** 0.A.6 Phi-3.5-vision-instruct

**ZH** 0.A.6 Phi-3.5-vision-instruct

**EN** We host Phi-3.5-vision-instruct on a local machine via their Hugging Face page with temperature=1.0.

**ZH** 我们通过其 Hugging Face 页面在本地机器上部署 Phi-3.5-vision-instruct，temperature=1.0。

**EN** 0.A.7 InternVL-2

**ZH** 0.A.7 InternVL-2

**EN** We access InternVL-2 via their Hugging Face repository, and use the temperature=0.2.

**ZH** 我们通过其 Hugging Face 仓库访问 InternVL-2，并使用 temperature=0.2。

**EN** 0.A.8 Qwen2-VL

**ZH** 0.A.8 Qwen2-VL

**EN** We use the publicly available codebase on Huggingface, and run the evaluation with the temperature=0.7.

**ZH** 我们使用 Huggingface 上公开的代码库，以 temperature=0.7 运行评测。

**EN** 0.A.9 Gemini 2.0 Flash

**ZH** 0.A.9 Gemini 2.0 Flash

**EN** We use the API via aistudio.google.com with temperature=0.7.

**ZH** 我们通过 aistudio.google.com 使用该 API，temperature=0.7。

**EN** 0.A.10 Gemini 2.0 Flash-Thinking

**ZH** 0.A.10 Gemini 2.0 Flash-Thinking

**EN** We use the model available via aistudio.google.com with temperature=0.7.

**ZH** 我们使用 aistudio.google.com 上提供的该模型，temperature=0.7。

**EN** 0.A.11 QVQ-Preview

**ZH** 0.A.11 QVQ-Preview

**EN** We run the publicly available model on Huggingface, with the temperature=0.7.

**ZH** 我们运行 Huggingface 上公开提供的该模型，temperature=0.7。

**EN** Appendix 0.B Hallucinations and educated guesses are among VLMs’ common failures

**ZH** 附录 0.B 幻觉与经验性猜测是 VLM 常见的失败类型

<!-- [原子块 · svg]  -->

**EN** Figure F1: Sometimes VLMs ( and ) fail to see clearly and make educated guesses.

**ZH** 图 F1：有时 VLM（ 与 ）看不清楚，从而做出经验性猜测。

**EN** Appendix 0.C Evaluating open-source models on BlindTest

**ZH** 附录 0.C 在 BlindTest 上评测开源模型

**EN** On average, 8 well-known open-source models perform worse than the commercial, closed-source VLMs on BlindTest. However, the best-performing open-source model (LLaVA-OneV-72B-ov), performs on-par with Sonnet-3 (45.92 vs. 45.73; Tab. T1). As model size increases, VLMs tend to perform better. For instance, the accuracy increase from LLaVA-OneV-ov 0.5B to 72B is +27.1 (18.82 ⟦SLOT_186⟧ 45.92; Tab. T1). In sum, open-source VLMs exhibit similar limitations to closed-source models on BlindTest.

**ZH** 平均而言，8 款知名开源模型在 BlindTest 上的表现不如商用闭源 VLM。不过表现最好的开源模型（LLaVA-OneV-72B-ov）与 Sonnet-3 持平（45.92 对 45.73；表 T1）。随着模型规模增大，VLM 的表现往往更好。例如，从 LLaVA-OneV-ov 0.5B 到 72B，准确率提升了 +27.1（18.82 ⟦SLOT_186⟧ 45.92；表 T1）。总之，开源 VLM 在 BlindTest 上表现出与闭源模型相似的局限。

**EN** Table T1: Open-source VLMs underperform the closed-source ones on BlindTest.

**ZH** 表 T1：开源 VLM 在 BlindTest 上不及闭源模型。

<!-- [原子块 · table] Model Size ○ ○ ○ ⬠ ⬠ ⬠ Task mean Random 33.33 50.00 5.77 20.00 20.00 25.00 4.55 33.33 24.00 GPT- 4o n/a 41.61 75.91 74.23 41.25 20.21 55.83 39.58 53.19 50.23 Gemini- 1.5 n/a 66.94 93.62 83.29 20.25 24 -->

**EN** Appendix 0.D Advanced prompting techniques

**ZH** 附录 0.D 高级提示技术

**EN** 0.D.1 Finding: Meta-prompting and 2-shot examples do not improve the VLMs’ performance on the two circles task (⟦SLOT_187⟧)

**ZH** 0.D.1 发现：元提示与 2-shot 示例并未提升 VLM 在两圆任务（⟦SLOT_187⟧）上的表现

**EN** We run GPT-4o and Sonnet-3.5 on the two circle task (⟦SLOT_188⟧) with 2-shot (providing 2 example images with answers) and meta-prompting11 1 Describe the image in detail first, and then answer: Are the two circles overlapping? Y/N. [35]. We find them to perform worse than our baseline prompts (Tab. T2). An explanation is that the VLMs already understand the questions but are limited by the ability to “see”. These techniques are not helpful perhaps because BlindTest tasks intuitively do not benefit from thinking aloud.

**ZH** 我们在两圆任务（⟦SLOT_188⟧）上用 2-shot（提供 2 张带答案的示例图像）与元提示11 1 先详细描述图像，然后回答：两个圆是否重叠？是/否。 [35] 运行 GPT-4o 与 Sonnet-3.5。我们发现它们的表现不如我们的基线提示（表 T2）。一种解释是，VLM 已经理解了问题，只是受限于「看见」的能力。这些技术之所以无益，或许是因为 BlindTest 任务直观上并不能从出声思考中获益。

**EN** Table T2: In-context examples and meta-prompting do not improve the overall accuracy of the Sonnet-3.5 and GPT-4o on the ⟦SLOT_189⟧ task.

**ZH** 表 T2：上下文示例与元提示并未提升 Sonnet-3.5 与 GPT-4o 在 ⟦SLOT_189⟧ 任务上的整体准确率。

<!-- [原子块 · table] Prompt Baseline 91.66 72.69 Meta-prompting [ 35 ] 90.53 65.62 2-shot 77.93 68.00 -->

**EN** Appendix 0.E Image reconstruction using Sonnet-3.5

**ZH** 附录 0.E 用 Sonnet-3.5 做图像重建

**EN** Inspired by Pixel Value Prediction [11] task in VLMs, we formulate the tasks in BlindTest as a reconstruction problem. However, we rely on VLMs’ existing capabilities, such as coding, to reform our tasks. Specifically, instead of framing the prompts into question answering, given the input image, we ask the best performing VLM (Sonnet-3.5) to explicitly use its coding ability and reconstruct the input images.

**ZH** 受 VLM 中的像素值预测 [11] 任务启发，我们把 BlindTest 中的任务表述为一个重建问题。不过我们倚重 VLM 已有的能力（例如编程）来重构我们的任务。具体地，我们不再把提示框定为问答，而是给定输入图像，要求表现最好的 VLM（Sonnet-3.5）显式运用其编程能力来重建输入图像。

**EN** 0.E.1 Sonnet-3.5 cannot use its coding ability to regenerate the images from BlindTest

**ZH** 0.E.1 Sonnet-3.5 无法用其编程能力重现 BlindTest 中的图像

**EN** Experiment We ask Sonnet-3.5 to generate various formats of the 6 samples from each of 7 tasks in BlindTest, specifically SVG, HTML/CSS, Javascript (using the canvas HTML element to draw the image), and the Python PIL package. We aim to see if the model can maintain the key features of the input image in its generated image, e.g., if Sonnet-3.5 can reconstruct images of the ⟦SLOT_190⟧ task with the same number of intersections as in the input image.

**ZH** 实验：我们要求 Sonnet-3.5 为 BlindTest 中 7 项任务各 6 个样本生成多种格式的代码，具体为 SVG、HTML/CSS、Javascript（用 canvas HTML 元素绘制图像）与 Python PIL 包。我们意在考察模型能否在其生成的图像中保留输入图像的关键特征，例如 Sonnet-3.5 能否重建出 ⟦SLOT_190⟧ 任务中交点数与原图一致的图像。

**EN** Results Overall, the coding ability does not help Sonnet-3.5 to reconstruct the images from BlindTest (see Fig. F2). Furthermore, across various tasks, Sonnet-3.5 often cannot faithfully recreate the important features such as the number of intersections, number of shapes, and touching vs. non-touching circles. This shows that Sonnet-3.5 can see the overall shapes in the image, but it is not sufficient for code generation.

**ZH** 结果：总的来看，编程能力并未帮助 Sonnet-3.5 重建 BlindTest 中的图像（见图 F2）。此外，在各任务中，Sonnet-3.5 常常无法忠实再现交点数、形状数以及圆相切与否等重要特征。这说明 Sonnet-3.5 能看出图像中的整体形状，但这对代码生成而言并不充分。

<!-- [原子块 · table] (a) Input image (b) SVG (c) HTML/CSS (d) JavaScript (e) Python -->

**EN** Figure F2: Sonnet-3.5 cannot recreate images from BlindTest (a) using its coding ability and different programming languages.

**ZH** 图 F2：Sonnet-3.5 无法（a）用其编程能力与不同编程语言重现 BlindTest 中的图像。

**EN** Appendix 0.F Two touching circles task

**ZH** 附录 0.F 两圆相切任务

**EN** 0.F.1 Benchmark Construction Details

**ZH** 0.F.1 基准构建细节

**EN** To create our benchmark, we use 5 parameters to control the diversity of the samples.

**ZH** 为构建基准，我们用 5 个参数控制样本的多样性。

**EN** • Color: We fix the colors for each circle to use {magenta, dodgerblue}.

**ZH** • 颜色：我们把每个圆的颜色固定为 {magenta, dodgerblue}。

**EN** • Image size: We use the physical size, and the DPI arguments in matplotlib to initialize the image size. The physical size is fixed to ⟦SLOT_191⟧, and the DPI ⟦SLOT_192⟧. The output image sizes are {384, 769, 1155}px.

**ZH** • 图像尺寸：我们用 matplotlib 中的物理尺寸与 DPI 参数初始化图像尺寸。物理尺寸固定为 ⟦SLOT_191⟧，DPI 为 ⟦SLOT_192⟧。输出图像尺寸为 {384, 769, 1155}px。

**EN** • Diameter: We use uniform diameters for both circles and choose the value proportional to the image size, where the diameter is ⟦SLOT_193⟧ of the image size.

**ZH** • 直径：我们对两个圆使用统一的直径，取值与图像尺寸成比例，直径为图像尺寸的 ⟦SLOT_193⟧。

**EN** • Distance: The boundary-to-boundary distance between circles is a fraction of the diameter chosen from {-0.25, -0.2, -0.15, -0.1, -0.05, 0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5}. Based on our definition, center-to-center distance is (2⟦SLOT_194⟧distance)⟦SLOT_195⟧diameter.

**ZH** • 距离：两圆之间的边界到边界距离是直径的一个分数，取自 {-0.25, -0.2, -0.15, -0.1, -0.05, 0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5}。按我们的定义，圆心距为 (2⟦SLOT_194⟧距离)⟦SLOT_195⟧直径。

**EN** • Rotation: We include 2 main rotations (vertical and horizontal), and 2 diagonal rotations.

**ZH** • 旋转：我们纳入 2 种主要旋转（垂直与水平）与 2 种对角旋转。

**EN** We use the center of the image as the origin so that it always aligns with the midpoint of distances between two circles. This systematic process results in a benchmark comprising 768 images (see Tabs. T3 and F3).

**ZH** 我们以图像中心为原点，使其始终与两圆间距的中点对齐。这一系统化流程得到一个含 768 张图像的基准（见表 T3 与图 F3）。

**EN** Code The code is available at https://github.com/anguyen8/vision-llms-are-blind/blob/main/src/TouchingCircle/TwoTouchingCircles.ipynb.

**ZH** 代码：代码见 https://github.com/anguyen8/vision-llms-are-blind/blob/main/src/TouchingCircle/TwoTouchingCircles.ipynb。

**EN** Prompts

**ZH** 提示

**EN** 1. Are the two circles touching each other? Answer with Yes/No.

**ZH** 1. 两个圆是否彼此相切？请用是/否回答。

**EN** 2. Are the two circles overlapping? Answer with Yes/No.

**ZH** 2. 两个圆是否重叠？请用是/否回答。

**EN** Groundtruth We consider two circles overlapping and touching (⟦SLOT_196⟧, ⟦SLOT_197⟧) if ⟦SLOT_198⟧; non-overlapping but touching (⟦SLOT_199⟧, ⟦SLOT_200⟧) if ⟦SLOT_201⟧; and non-overlapping & non-touching (⟦SLOT_202⟧, ⟦SLOT_203⟧) when ⟦SLOT_204⟧ (Fig. F4). Random-baseline accuracy: 50%.

**ZH** 真值：我们把两圆重叠且相切记为（⟦SLOT_196⟧、⟦SLOT_197⟧），其条件为 ⟦SLOT_198⟧；不重叠但相切记为（⟦SLOT_199⟧、⟦SLOT_200⟧），其条件为 ⟦SLOT_201⟧；不重叠且不相切记为（⟦SLOT_202⟧、⟦SLOT_203⟧），其条件为 ⟦SLOT_204⟧（图 F4）。随机基线准确率：50%。

**EN** Table T3: Number of samples for each category is the same in our benchmark, where they sum to 768.

**ZH** 表 T3：本基准中每个类别的样本数相同，合计 768。

<!-- [原子块 · table] Parameter Values Samples Total Samples Image size ( C C ) 384px 256 768 769px 256 1155px 256 Diameter ( ϕ \phi ) C 4 \frac{C}{4} 192 768 C 5 \frac{C}{5} 192 C 6 \frac{C}{6} 192 C 7 \frac{C}{7} 192 Dis -->

<!-- [原子块 · table] (a) Rotation (b) Diameter (c) Distance -->

**EN** Figure F3: Samples in the benchmark include various settings for drawing two circles. We start with choosing a rotation (a) and change other parameters of each plot, e.g., the diameter (b), the distance between perimeters (c), and the image size (in pixels). We show the parameters that can be changed to generate different samples inside the legend.

**ZH** 图 F3：基准中的样本包含绘制两个圆的各种设置。我们先选择一种旋转（a），再改变每张图的其他参数，例如直径（b）、周长之间的距离（c）与图像尺寸（以像素计）。我们在图例中展示了可改变以生成不同样本的参数。

<!-- [原子块 · table] (a) 4 diameter ϕ \phi (b) 4 orientations d d -0.15 -0.05 0.0 +0.05 +0.15 +0.25 +0.35 +0.50 GT labels O {O} , T {T} O {O} , T {T} O ¯ \mkern 1.5mu\overline{\mkern-1.5muO\mkern-1.5mu}\mkern 1.5mu , T {T -->

**EN** Figure F4: For each image size and distance ⟦SLOT_205⟧, we vary diameter (a) and orientation (b). Groundtruth: ⟦SLOT_206⟧: overlapping. ⟦SLOT_207⟧: touching. ⟦SLOT_208⟧: non-overlapping. ⟦SLOT_209⟧: non-touching.

**ZH** 图 F4：对每种图像尺寸与距离 ⟦SLOT_205⟧，我们改变直径（a）与朝向（b）。真值：⟦SLOT_206⟧：重叠。⟦SLOT_207⟧：相切。⟦SLOT_208⟧：不重叠。⟦SLOT_209⟧：不相切。

**EN** 0.F.2 Finding: image resolution does not affect VLMs performance

**ZH** 0.F.2 发现：图像分辨率不影响 VLM 的表现

**EN** Fig. F5-left shows that VLMs are almost invariant to the image resolution. For example, GPT-4o and Sonnet-3’s performance saturates at 769px, and Sonnet-3.5 slightly performs worse at 769 and 1155px compared to 384px. Gemini-1.5, however, is fairly consistent across different resolutions. Based off these results, we conclude that VLMs’ ability to see the intersection of two circles does not depend on the quality of the image.

**ZH** 图 F5 左图显示，VLM 对图像分辨率几乎不敏感。例如，GPT-4o 与 Sonnet-3 的表现饱和于 769px，而 Sonnet-3.5 在 769 与 1155px 上略逊于 384px。不过 Gemini-1.5 在不同分辨率下相当稳定。基于这些结果，我们得出结论：VLM 看出两个圆是否相交的能力并不取决于图像质量。

**EN** 0.F.3 Finding: the vertical rotation closes the gap between models’ performance

**ZH** 0.F.3 发现：垂直旋转缩小了模型之间的性能差距

**EN** As shown in Fig. F5-middle, arranging the circles in vertical rotation causes the models to perform similarly on the benchmark. Although Gemini-1.5 slightly performs better at diagonal and Sonnet-3.5 at horizontal rotation, VLMs perform relatively better at vertical rotation. This suggests that the task complexity due to various rotations is not the main source of low performance in VLMs.

**ZH** 如图 F5 中图所示，把圆按垂直方向排列会使各模型在基准上表现相近。虽然 Gemini-1.5 在对角旋转上略好、Sonnet-3.5 在水平旋转上略好，VLM 在垂直旋转上表现相对更好。这说明由各种旋转带来的任务复杂性并非 VLM 表现不佳的主因。

**EN** 0.F.4 Finding: Increasing the distance improves the VLMs’ accuracy

**ZH** 0.F.4 发现：增大间距会提升 VLM 的准确率

**EN** VLMs perform better when the distance increases from zero to positive values (see Fig. F5-right). However, Sonnet-3.5 is more conservative than other VLMs that mostly answer “Yes”, which results in its lowest performance at negative distances.

**ZH** 当距离从零增至正值时，VLM 表现更好（见图 F5 右图）。不过 Sonnet-3.5 比多数回答「是」的其他 VLM 更为保守，这导致它在负距离上表现最低。

<!-- [原子块 · object]  -->

**EN** Figure F5: There is no correlation between the resolution of the image (left) and VLMs’ performance. Across various rotations (middle), VLMs perform almost the same at vertical. Most failure cases are at boundary distances (right).

**ZH** 图 F5：图像的分辨率（左）与 VLM 表现之间没有相关性。在各种旋转下（中），VLM 在垂直方向上的表现几乎相同。多数失败案例出现在临界距离处（右）。

**EN** 0.F.5 Finding: VLMs prefer a specific rotation

**ZH** 0.F.5 发现：VLM 偏好某一种特定的旋转

**EN** Tab. T4 shows that VLMs prefer different rotations. For example, GPT-4o performs best at vertical, Gemini-1.5 at diagonal, Sonnet-3.5 at horizontal, and Sonnet-3 at vertical.

**ZH** 表 T4 显示，VLM 偏好不同的旋转。例如，GPT-4o 在垂直方向表现最好，Gemini-1.5 在对角方向最好，Sonnet-3.5 在水平方向最好，Sonnet-3 在垂直方向最好。

**EN** Table T4: VLM accuracy is often best at a specific two-circle orientation. Across three different resolutions, GPT-4o and Sonnet-3 perform much better when two circles are arranged vertically. In contrast, Gemini-1.5 and Sonnet-3.5 prefer the diagonal and horizontal orientations, respectively.

**ZH** 表 T4：VLM 的准确率常常在某个特定的两圆朝向上最高。在三种不同分辨率下，当两个圆垂直排列时，GPT-4o 与 Sonnet-3 的表现好得多。相比之下，Gemini-1.5 与 Sonnet-3.5 分别偏好对角与水平朝向。

<!-- [原子块 · table] Resolution Rotation a 384px vertical 82.03 93.75 96.09 90.62 horizontal 71.87 89.84 75.78 96.87 diagonal 69.97 95.70 78.90 94.92 b 769px vertical 89.84 95.31 92.97 84.37 horizontal 80.47 85.94 83.59 9 -->

**EN** 0.F.6 Finding: Various coloring of the two circles has minimal effects on the overall accuracy

**ZH** 0.F.6 发现：两圆的不同着色对整体准确率影响甚微

**EN** VLMs’ performance in the ⟦SLOT_210⟧ task does not change substantially (⟦SLOT_211⟧ for Sonnet-3.5 and ⟦SLOT_212⟧10.81% for GPT-4o) when tested against different colors (Tab. T5).

**ZH** 在 ⟦SLOT_210⟧ 任务上，当用不同颜色测试时，VLM 的表现没有实质变化（对 Sonnet-3.5 为 ⟦SLOT_211⟧，对 GPT-4o 为 ⟦SLOT_212⟧10.81%）（表 T5）。

**EN** Table T5: The small ⟦SLOT_213⟧ in VLMs’ performance by changing the colors of the circles suggests that coloring does not significantly impact the VLMs’ vision capabilities.

**ZH** 表 T5：改变圆的颜色所引起的 VLM 表现上的微小 ⟦SLOT_213⟧ 说明，着色并不会显著影响 VLM 的视觉能力。

<!-- [原子块 · table] Color Magenta - Blue (baseline) 90.93 76.10 Red - Black 96.72 86.91 Yellow - Green 94.39 80.52 Dark gray - Light gray 93.62 82.25 -->

**EN** 0.F.7 Results for fine-tuning Bunny on the two touching circle

**ZH** 0.F.7 在两圆相切任务上微调 Bunny 的结果

**EN** In order to determine if fine-tuning could improve the model’s performance on this task we attempted to fine-tune Bunny [12] (Bunny-v1.1-Llama-3-8B-V with the original weights) on the two touching circles task. We fine-tuned Bunny using datasets of sizes: 10K, 20K, 50K, and 100K samples, each containing a balanced number of instances where the circles are either overlapping or separate (equal number of YES/NO answers in the training set).

**ZH** 为判断微调能否提升模型在该任务上的表现，我们尝试在两圆相切任务上微调 Bunny [12]（Bunny-v1.1-Llama-3-8B-V，使用原始权重）。我们用规模为 10K、20K、50K 与 100K 样本的数据集微调 Bunny，每个数据集中圆重叠与圆分离的样本数量均衡（训练集中「是」与「否」答案数量相等）。

**EN** The baseline model, without any fine-tuning, achieved 17.1% accuracy for task overlap and 11.7% for touching circles. After fine-tuning, we observed improvements with smaller datasets, such as 10K and 20K cases, where accuracy reached up to 36.8%. However, increasing the number of samples did not lead to better performance. In some instances, such as with the 50K dataset, the model failed to predict anything and only generated the end-of-text token.

**ZH** 未做任何微调的基线模型在重叠任务上取得 17.1% 准确率，在相切圆任务上取得 11.7%。微调后，我们在较小的数据集（如 10K 与 20K 样本）上观察到改进，准确率最高达到 36.8%。然而，增加样本数并未带来更好的表现。在若干情形下（例如使用 50K 数据集时），模型无法做出任何预测，只生成文本结束 token。

**EN** The loss values for all these experiments were very close to zero, indicating that the model overfits the training set but fails to generalize. This suggests that training on this task is not straightforward and may require a combination of multiple tasks or that this problem does not have a simple solution.

**ZH** 所有这些实验的损失值都非常接近于零，说明模型过拟合了训练集却无法泛化。这表明在该任务上训练并非易事，可能需要多个任务的组合，或者该问题本就没有简单的解法。

**EN** Fig. F6 shows the accuracy breakdown by distance of the two circles. The model’s performance improves when the circles are overlapping, but when there is a long distance between them, the model does not generalize well and cannot provide accurate answers.

**ZH** 图 F6 展示了按两圆距离细分的准确率。当圆重叠时模型表现提升，但当两圆相距较远时，模型泛化不佳，无法给出准确答案。

<!-- [原子块 · img]  -->

**EN** (a) Accuracy by distance without fine-tuning

**ZH** (a) 未微调时按距离划分的准确率

<!-- [原子块 · img]  -->

**EN** (b) Accuracy by distance with 10K samples

**ZH** (b) 用 10K 样本时按距离划分的准确率

<!-- [原子块 · img]  -->

**EN** (c) Accuracy by distance with 20K samples

**ZH** (c) 用 20K 样本时按距离划分的准确率

<!-- [原子块 · img]  -->

**EN** (d) Accuracy by distance with 50K samples

**ZH** (d) 用 50K 样本时按距离划分的准确率

<!-- [原子块 · img]  -->

**EN** (e) Accuracy by distance with 100K samples

**ZH** (e) 用 100K 样本时按距离划分的准确率

**EN** Figure F6: Comparison of Bunny’s accuracy by distance with and without fine-tuning

**ZH** 图 F6：Bunny 在微调与未微调时按距离划分的准确率对比

**EN** 0.F.8 Additional examples

**ZH** 0.F.8 补充示例

**EN** We show examples of models’ responses to the prompts on the two touching circles task in Fig. F7.

**ZH** 我们在图 F7 中展示模型对两圆相切任务提示的回答示例。

<!-- [原子块 · svg]  -->

**EN** Figure F7: Some VLMs consistently fail by not seeing the distance between the two circles at large distances and resolutions (GPT-4o and Sonnet-3–rightmost). Gemini-1.5 and Sonnet-3 also struggle to see the small gaps between circles (distance=0.05)

**ZH** 图 F7：某些 VLM 在大间距与各种分辨率下始终无法看清两圆之间的距离（GPT-4o 与 Sonnet-3——最右）。Gemini-1.5 与 Sonnet-3 也难以看清圆之间的小间隙（距离 = 0.05）

<!-- [原子块 · svg]  -->

**EN** Figure F8: VLMs consistently fail at smaller distances. However, when the gap is large and clearly visible, GPT-4o remains unreliable. Sonnet-3.5 tends to conservatively answer “No” regardless of the actual distance between the two circles.

**ZH** 图 F8：VLM 在间距较小时始终失败。然而，当间隙很大且清晰可见时，GPT-4o 仍不可靠。Sonnet-3.5 倾向于保守地回答「否」，而不论两圆之间的实际距离是多少。

**EN** Appendix 0.G Task 3: Identifying the circled letter in a string

**ZH** 附录 0.G 任务 3：识别字符串中被圈住的字母

**EN** 0.G.1 Task construction

**ZH** 0.G.1 任务构建

**EN** Each image is created using a combination of the below variables.

**ZH** 每张图像由下列变量组合生成。

**EN** • String: We test three strings { Acknowledgement , Subdermatoglyphic , tHyUiKaRbNqWeOpXcZvM }. While they all have letters of varying widths and heights, the first two are English words while the latter is a string of random characters. Subdermatoglyphic is the longest English word that has no letter repetitions.

**ZH** • 字符串：我们测试三个字符串 { Acknowledgement ， Subdermatoglyphic ， tHyUiKaRbNqWeOpXcZvM }。虽然它们的字母宽度与高度各异，但前两个是英文单词，最后一个是随机字符组成的字符串。Subdermatoglyphic 是不含字母重复的最长英文单词。

**EN** • Letter: We draw the oval (⟦SLOT_214⟧) over every letter, one at a time, in each string.

**ZH** • 字母：我们在每个字符串中把椭圆（⟦SLOT_214⟧）逐个绘制在每个字母上。

**EN** • Font: We use 2 different font families for each word, OpenSans and Helvetica.

**ZH** • 字体：我们为每个单词使用 2 种不同的字体族，OpenSans 与 Helvetica。

**EN** • Oval (⟦SLOT_215⟧) thickness: We generate the ⟦SLOT_216⟧ with 3 various line thicknesses.

**ZH** • 椭圆（⟦SLOT_215⟧）粗细：我们用 3 种不同的线条粗细生成 ⟦SLOT_216⟧。

**EN** • Scaling factor: Since each letter has a unique size, we use a scaling factor to control the size of the ⟦SLOT_217⟧.

**ZH** • 缩放因子：由于每个字母尺寸各异，我们用一个缩放因子控制 ⟦SLOT_217⟧ 的大小。

**EN** Finally, we render the text on a white canvas with a size of 1250⟦SLOT_218⟧1250 pixels, and we produce 90 images for Acknowledgement , 102 for Subdermatoglyphic , and 120 samples for tHyUiKaRbNqWeOpXcZvM (see Tabs. T6 and F9).

**ZH** 最后，我们把文本渲染在 1250⟦SLOT_218⟧1250 像素的白色画布上，并为 Acknowledgement 生成 90 张、 Subdermatoglyphic 生成 102 张、 tHyUiKaRbNqWeOpXcZvM 生成 120 张样本（见表 T6 与图 F9）。

**EN** Evaluation

**ZH** 评测

**EN** To determine the models’ prediction, we extract the character enclosed in {curly braces} in the models’ response.

**ZH** 为判定模型的预测，我们抽取模型回答中 {花括号} 内的字符。

**EN** Code

**ZH** 代码

**EN** The code is available at https://github.com/anguyen8/vision-llms-are-blind/blob/main/src/CircledWord/GenerateSamples.ipynb.

**ZH** 代码见 https://github.com/anguyen8/vision-llms-are-blind/blob/main/src/CircledWord/GenerateSamples.ipynb。

**EN** Prompts

**ZH** 提示

**EN** 1. Which letter is being circled? Please provide your answer in curly brackets, e.g. {a}

**ZH** 1. 哪个字母被圈住了？请把答案放在花括号中，例如 {a}。

**EN** 2. Which character is being highlighted with a red oval? Please provide your answer in curly brackets, e.g. {a}

**ZH** 2. 哪个字符被红色椭圆高亮了？请把答案放在花括号中，例如 {a}。

**EN** Groundtruth letters must match predicted letters exactly (case-insensitive).

**ZH** 真值字母必须与预测字母完全一致（不区分大小写）。

**EN** Table T6: The breakdown of our benchmark based on the number of different parameters shows our data is balanced for each word.

**ZH** 表 T6：基于不同参数数量的基准细分显示，我们的数据对每个单词都是均衡的。

<!-- [原子块 · table] Parameter Values Samples Total Samples Word Acknowledgement 90 312 Subdermatoglyphic 102 tHyUiKaRbNqWeOpXcZvM 120 Font OpenSans 156 312 Helvetica 156 Image size ( C C ) 1250x1250 pixels 312 312 Oval t -->

<!-- [原子块 · table] (a) Acknowledgement (b) Subdermatoglyphic (c) tHyUiKaRbNqWeOpXcZvM -->

**EN** Figure F9: Our benchmark comprises three different words, of which one letter is circled by the red oval in each image.

**ZH** 图 F9：我们的基准包含三个不同的单词，每张图像中都有一个字母被红色椭圆圈住。

<!-- [原子块 · table]  -->

**EN** Figure F10: Which letter is being red circled?

**ZH** 图 F10：哪个字母被红圈圈住了？

**EN** 0.G.2 Finding: VLMs mostly confuse the adjacent character for the circled letter

**ZH** 0.G.2 发现：VLM 多半把相邻字符误认为被圈住的字母

**EN** Models often mistake the neighboring characters as actual circled letters. For example, Fig. F11 shows that for Sonnet-3.5 in the word Acknowledgement , all of the incorrect predictions for “n” are the neighboring letter “t”. For Gemini-1.5, in the word tHyUiKaRbNqWeOpXcZvM , where letters “K” and “a” are adjacent, 100% of the mispredictions for “K” are the letter “a” (see Fig. F12).

**ZH** 模型常把相邻字符误当作真正被圈住的字母。例如，图 F11 显示，对 Sonnet-3.5 在单词 Acknowledgement 中，针对「n」的全部错误预测都是相邻字母「t」。对 Gemini-1.5 在 tHyUiKaRbNqWeOpXcZvM 中，字母「K」与「a」相邻，针对「K」的错误预测 100% 都是字母「a」（见图 F12）。

<!-- [原子块 · img]  -->

**EN** Figure F11: Adjacent letters are the most common wrong prediction for Sonnet-3.5 in Acknowledgement , e.g., letter “e” is predicted instead of “m” 20.83% of the time, or letter “t” is predicted instead of “n” 27.08% of the time.

**ZH** 图 F11：相邻字母是 Sonnet-3.5 在 Acknowledgement 中最常见的错误预测，例如有 20.83% 的情况把「m」预测为「e」，或 27.08% 的情况把「n」预测为「t」。

<!-- [原子块 · img]  -->

**EN** Figure F12: Gemini-1.5 tends to confuse adjacent letters like “a” and “K”. Gemini-1.5 also hallucinates the circled letter “a” as being the character “@” and it confuses the letter “q” for the letter “g”.

**ZH** 图 F12：Gemini-1.5 倾向于混淆「a」与「K」等相邻字母。Gemini-1.5 还会把被圈住的字母「a」幻觉为字符「@」，并把字母「q」误认为字母「g」。

<!-- [原子块 · img]  -->

**EN** Figure F13: Aggregate confusion matrix summed over all 4 VLMs and 12 responses for each letter in the word Subdermatoglyphic . Models mostly mispredict characters near the circled letter. VLMs sometimes hallucinate characters that do not even exist in the word, e.g., “@” (right panel).

**ZH** 图 F13：对单词 Subdermatoglyphic 中每个字母，汇总四款 VLM 各 12 条回答得到的混淆矩阵。模型多半误预测被圈字母附近的字符。VLM 有时会幻觉出该单词中根本不存在的字符，例如「@」（右图）。

**EN** 0.G.3 Finding: GPT-4o and Gemini-1.5 confuse the red oval as part of the letter

**ZH** 0.G.3 发现：GPT-4o 与 Gemini-1.5 把红色椭圆误认为字母的一部分

**EN** Figs. F14 and F15 show that Gemini-1.5 and GPT-4o sometimes fail to recognize that the red oval is not part of the letter. Gemini-1.5 tends to predict that the circled letter “a” is actually the “@” sign (see Fig. F14). GPT-4o on the other hand tends to predict “o” regardless of which letter is circled (Fig. F15).

**ZH** 图 F14 与图 F15 显示，Gemini-1.5 与 GPT-4o 有时无法识别红色椭圆并非字母的一部分。Gemini-1.5 倾向于把被圈住的字母「a」预测为「@」符号（见图 F14）。GPT-4o 则倾向于不论哪个字母被圈住都预测「o」（图 F15）。

<!-- [原子块 · img]  -->

**EN** Figure F14: Random samples for different words, and Gemini-1.5’s predictions, where Gemini-1.5 mostly predicts the adjacent letters or confuses the red oval as part of the circled letter.

**ZH** 图 F14：不同单词的随机样本及 Gemini-1.5 的预测，其中 Gemini-1.5 多半预测相邻字母，或把红色椭圆误认为被圈字母的一部分。

<!-- [原子块 · img]  -->

**EN** Figure F15: GPT-4o is the most sensitive to confuse the red oval as part of the letter, where it often predicts “o” instead of “l”, “y”, “p”, and “c” in the word Subdermatoglyphic .

**ZH** 图 F15：GPT-4o 最容易把红色椭圆误认为字母的一部分，在单词 Subdermatoglyphic 中，它常把「l」「y」「p」「c」预测为「o」。

**EN** 0.G.4 Finding: Models perform similarly across two common font families

**ZH** 0.G.4 发现：模型在两种常见字体族上表现相近

**EN** As shown in Fig. F16, models do not show a significant variance over different fonts, suggesting our choice of font is not a reason for their unreliable performance.

**ZH** 如图 F16 所示，模型在不同字体上没有表现出显著差异，说明我们的字体选择并非它们表现不可靠的原因。

<!-- [原子块 · img]  -->

<!-- [原子块 · equation]  -->

**EN** Figure F16: VLMs do not show a consistent trend between fonts. This suggests that using different spacing between letters, letter styles, and letter size has minimal effects on the VLMs’ ability to see the content of the red oval.

**ZH** 图 F16：VLM 在字体之间未呈现一致的趋势。这说明采用不同的字母间距、字母样式与字母大小，对 VLM 看清红色椭圆内容的能力影响甚微。

**EN** 0.G.5 Finding: models are invariant to our choice of prompts

**ZH** 0.G.5 发现：模型对我们提示的选取不敏感

**EN** Our choice of prompts has little impact on the performance of the models as depicted in Fig. F17.

**ZH** 如图 F17 所示，我们的提示选取对模型表现影响很小。

<!-- [原子块 · img]  -->

<!-- [原子块 · equation]  -->

**EN** Figure F17: Model performance breakdown for different prompts P1: "Which letter is being circled? Please provide your answer in curly brackets, e.g. {a}" and P2: "Which character is being highlighted with a red oval? Please provide your answer in curly brackets, e.g. {a}". Regardless of the prompts, VLMs perform similarly in seeing the contents of the red oval.

**ZH** 图 F17：模型在两种提示下的表现细分——P1：「哪个字母被圈住了？请把答案放在花括号中，例如 {a}」与 P2：「哪个字符被红色椭圆高亮了？请把答案放在花括号中，例如 {a}」。不论使用哪种提示，VLM 在看清红色椭圆内容上表现相近。

**EN** 0.G.6 Finding: VLMs fail to see the circled letter on various English words

**ZH** 0.G.6 发现：VLM 在各种英文单词上都无法看清被圈住的字母

**EN** On average, SOTA VLMs show the same limitations across various English words (see Tab. T7). However, the mean accuracy over words with less and non-repetitive letters is higher than others (the mean accuracy over the word question is 90.36% while it is 79.86% on the word civilization ).

**ZH** 平均而言，各 SOTA VLM 在各种英文单词上表现出同样的局限（见表 T7）。不过，在字母较少且无重复字母的单词上，平均准确率高于其他单词（单词 question 上的平均准确率为 90.36%，而单词 civilization 上为 79.86%）。

**EN** Table T7: Overall, VLMs perform better on short words without repetitive letters, e.g., question . Yet, the mean accuracy of four SOTA VLMs (86.43%) is far from being 100% accurate.

**ZH** 表 T7：总的来看，VLM 在不含重复字母的短单词（如 question ）上表现更好。然而，四款 SOTA VLM 的平均准确率（86.43%）仍远未达到 100%。

<!-- [原子块 · table] String Mean question 98.96 100.00 62.50 100.00 90.36 syndrome 91.67 91.67 70.83 91.58 86.44 environmental 82.69 89.10 73.72 89.74 83.81 civilization 79.17 87.50 61.80 90.97 79.86 tournament 89.17 92.5 -->

**EN** Table T8: Except for GPT-4o, all other models have a higher accuracy (%) on the two English words than on the random string, suggesting that VLMs might leverage their familiarity with a known word to make educated guesses.

**ZH** 表 T8：除 GPT-4o 外，其余所有模型在两个英文单词上的准确率（%）都高于在随机字符串上的准确率，说明 VLM 可能利用对已知单词的熟悉度做出经验性猜测。

<!-- [原子块 · table] String Mean Acknowledgement 77.22 96.67 87.22 91.11 88.06 Subdermatoglyphic 64.42 74.02 68.14 94.10 75.25 tHyUiKaRbNqWeOpXcZvM 81.25 79.17 60.83 77.92 74.79 Mean accuracy 74.23 83.29 72.06 87.88 79.37 -->

**EN** 0.G.7 Adding white space between letters consistently improves the accuracy across all words

**ZH** 0.G.7 在字母之间加入空白能一致地提升所有单词上的准确率

**EN** As shown in Fig. F18, VLMs perform better when we add more white space between letters of a word, e.g., ⟦SLOT_225⟧ for GPT-4o on the words Acknowledgement and Subdermatoglyphic from 0 to 3 spaces are 11% and 21%, respectively.

**ZH** 如图 F18 所示，当我们在单词的字母之间加入更多空白时，VLM 表现更好，例如 ⟦SLOT_225⟧ 对 GPT-4o 在 Acknowledgement 与 Subdermatoglyphic 上从 0 个空格到 3 个空格分别为 11% 与 21%。

<!-- [原子块 · table] (a) Acknowledgement (b) Subdermatoglyphic (c) tHyUiKaRbNqWeOpXcZvM (d) syndrome -->

<!-- [原子块 · table] (e) civilization (f) question (g) tournament (h) environmental -->

**EN** Figure F18: VLMs tend to be significantly more accurate when there are white spaces between letters.

**ZH** 图 F18：当字母之间存在空白时，VLM 的准确率往往显著更高。

**EN** 0.G.8 Additional Examples

**ZH** 0.G.8 补充示例

**EN** Examples from our evaluation of VLMs on the circled letter task are shown in Fig. F19.

**ZH** 图 F19 给出我们在被圈字母任务上评测 VLM 的示例。

<!-- [原子块 · svg]  -->

**EN** Figure F19: Most failure cases consist of predicting the adjacent letters (predicting “e” instead of “m” in GPT-4o, Sonnet-3, and Sonnet-3.5 leftmost), and confusing the red oval as part of the circled letter (predicting “©” instead of “c” in Sonnet-3.5).

**ZH** 图 F19：多数失败案例包括预测相邻字母（GPT-4o、Sonnet-3 与 Sonnet-3.5 最左图把「m」预测为「e」），以及把红色椭圆误认为被圈字母的一部分（Sonnet-3.5 把「c」预测为「©」）。

**EN** Appendix 0.H Counting the number of line intersections task

**ZH** 附录 0.H 数直线交点数量任务

**EN** 0.H.1 Benchmark Construction Details

**ZH** 0.H.1 基准构建细节

**EN** To create our benchmark, we use 5 parameters to control the diversity of the samples.

**ZH** 为构建基准，我们用 5 个参数控制样本的多样性。

**EN** • Color: We fix the colors for each line to use {blue, red}

**ZH** • 颜色：我们把每条线的颜色固定为 {蓝，红}。

**EN** • Image size: We generate 3 different image resolutions, {384, 768, 1152}px, to include high and low-resolution samples in our tests.

**ZH** • 图像尺寸：我们生成 3 种不同的图像分辨率 {384, 768, 1152}px，以在测试中包含高分辨率与低分辨率样本。

**EN** • Grid size: We divide the whole image into a 12⟦SLOT_226⟧12 grid with 144 equal sized cells. Then, we choose 3 points for each (blue and red) line on the grid to draw the line plots. To make sure the line plots do not overlap and the intersections are well distanced from the edges, we fix the x-coordinates, and randomly sample y-coordinates from the invisible 12⟦SLOT_227⟧12 grid. The grid sampling also avoids picking the same coordinates for both blue and red line.

**ZH** • 网格尺寸：我们把整幅图像划分为 12⟦SLOT_226⟧12 的网格，含 144 个等大单元格。然后，我们为每条（蓝、红）线在网格上选取 3 个点以绘制折线。为确保折线不重叠、且交点与边缘保持充分距离，我们固定 x 坐标，并从不可见的 12⟦SLOT_227⟧12 网格中随机采样 y 坐标。网格采样也避免为蓝线与红线选中相同坐标。

**EN** • X-coordinate: For each point, we choose x⟦SLOT_228⟧ px.

**ZH** • X 坐标：对每个点，我们取 x⟦SLOT_228⟧ px。

**EN** • Y-coordinate: For each x-coordinate above, we randomly sample a y-coordinate from 12 pre-defined rows in the 12⟦SLOT_229⟧12 grid. We also ensure that no blue and red points share the exact same (x,y) coordinates.

**ZH** • Y 坐标：对上面每个 x 坐标，我们从 12⟦SLOT_229⟧12 网格中预定义的 12 行里随机采样一个 y 坐标。我们还确保蓝点与红点不共用完全相同的 (x, y) 坐标。

**EN** • Line thickness: We vary the line widths with standard matplotlib values (2 and 4), which renders into a width of ⟦SLOT_230⟧ and ⟦SLOT_231⟧ pixels, respectively.

**ZH** • 线条粗细：我们用 matplotlib 的标准取值（2 与 4）改变线宽，分别渲染为 ⟦SLOT_230⟧ 与 ⟦SLOT_231⟧ 像素的宽度。

**EN** • Number of intersections: We count the intersections based on the three points defined for each line (⟦SLOT_232⟧, ⟦SLOT_233⟧, and ⟦SLOT_234⟧).

**ZH** • 交点数量：我们依据为每条线定义的三个点（⟦SLOT_232⟧、⟦SLOT_233⟧ 与 ⟦SLOT_234⟧）统计交点。

**EN** We repeat the process until we have 2 line widths⟦SLOT_235⟧3 image sizes⟦SLOT_236⟧100 samples of 0, 1, and 2 intersections, resulting in 1800 images (see Tabs. T9 and F20).

**ZH** 我们重复该流程，直到得到 2 种线宽⟦SLOT_235⟧3 种图像尺寸⟦SLOT_236⟧ 各 100 个含 0、1、2 个交点的样本，共 1800 张图像（见表 T9 与图 F20）。

**EN** Code The code to generate the images is at https://github.com/anguyen8/vision-llms-are-blind/blob/main/src/LineIntersection/2dline.ipynb.

**ZH** 代码：生成图像的代码见 https://github.com/anguyen8/vision-llms-are-blind/blob/main/src/LineIntersection/2dline.ipynb。

**EN** Prompts We ask each question using two different wordings:

**ZH** 提示：我们用两种不同的措辞提问：

**EN** 1. How many times do the blue and red lines touch each other? Answer with a number in curly brackets, e.g., {5}.

**ZH** 1. 蓝线与红线彼此接触了多少次？请用花括号中的数字回答，例如 {5}。

**EN** 2. Count the intersection points where the blue and red lines meet. Put your answer in curly brackets, e.g., {2}.

**ZH** 2. 数一数蓝线与红线相交的交点。把答案放在花括号中，例如 {2}。

**EN** Groundtruth answers are ⟦SLOT_237⟧ (random-baseline accuracy: 33.33%).

**ZH** 真值答案为 ⟦SLOT_237⟧（随机基线准确率：33.33%）。

<!-- [原子块 · table] (a) zero intersection (b) one intersection (c) two intersections -->

**EN** Figure F20: Samples from the two intersecting lines benchmark that contain 0, 1, or 2 line intersections.

**ZH** 图 F20：来自两条相交直线基准的样本，分别含 0、1 或 2 个直线交点。

<!-- [原子块 · table] GT = 0 GT = 1 GT = 1 GT = 2 -->

**EN** Figure F21: Count intersections

**ZH** 图 F21：数交点

**EN** Table T9: We generate the same number of images based on various parameters to have a balanced benchmark.

**ZH** 表 T9：我们基于各种参数生成相同数量的图像，以得到均衡的基准。

<!-- [原子块 · table] Parameter Values Samples Total Samples Image size ( C C ) 384px 600 1800 768px 600 1152px 600 Line thickness 0.005 × C 0.005\times C 900 1800 0.01 × C 0.01\times C 900 Number of intersections 0 600 18 -->

**EN** 0.H.2 Finding: image resolution does not influence VLM’s ability to count the line intersections

**ZH** 0.H.2 发现：图像分辨率不影响 VLM 数直线交点的能力

**EN** Fig. F22 depicts that increasing the resolution in our plots does not help the VLMs see and count the intersections of 2D lines.

**ZH** 图 F22 显示，提高我们绘图的分辨率并不能帮助 VLM 看见并数清二维直线的交点。

**EN** 0.H.3 Finding: VLMs perform similarly when the lines intersect twice

**ZH** 0.H.3 发现：当直线相交两次时，VLM 表现相近

**EN** Our benchmark consists of images with 0 to 1 line intersections with an identical number of samples in each category. We break down the performance of each model based on the groundtruth in Fig. F22-right to analyze where VLMs mostly fail in their overall performance. As depicted in Fig. F22-right, VLMs perform relatively better on 2 intersections (except Sonnet-3.5 that is best on 1 intersection) and perform worse on 0 intersections (Sonnet-3 is the worst).

**ZH** 我们的基准由含 0 到 1 个直线交点的图像组成，每个类别的样本数相同。我们在图 F22 右图中按真值细分每个模型的表现，以分析 VLM 的整体表现主要失分于何处。如图 F22 右图所示，VLM 在 2 个交点上表现相对更好（Sonnet-3.5 除外，它在 1 个交点上最好），在 0 个交点上表现更差（Sonnet-3 最差）。

<!-- [原子块 · object]  -->

**EN** Figure F22: VLMs are not sensitive to the image resolution to see and count the number of intersections (left). When the lines intersect twice, VLMs perform similarly, while Sonnet-3.5 has the least variance over different numbers of intersections (right).

**ZH** 图 F22：VLM 对图像分辨率并不敏感，无法据此看见并数清交点个数（左）。当直线相交两次时，VLM 表现相近，而 Sonnet-3.5 在不同交点数量上的方差最小（右）。

**EN** 0.H.4 Additional Examples

**ZH** 0.H.4 补充示例

**EN** We show examples of models’ responses to the prompts on the counting the number of line intersections task in Fig. F23.

**ZH** 我们在图 F23 中展示模型对数直线交点数量任务提示的回答示例。

<!-- [原子块 · svg]  -->

**EN** Figure F23: All VLMs, except Sonnet-3.5, fail at counting when there is no intersection, even when the gap between 2 lines is large (second image on the left).

**ZH** 图 F23：除 Sonnet-3.5 外，所有 VLM 在没有交点时都会数错，即便两条线之间的间隙很大（左起第二张图像）。

<!-- [原子块 · svg]  -->

**EN** Figure F24: VLMs cannot reliably count the intersections between the blue and red plots.

**ZH** 图 F24：VLM 无法可靠地数清蓝色与红色折线之间的交点。

**EN** Appendix 0.I Counting the number of nested squares

**ZH** 附录 0.I 数嵌套正方形的数量

**EN** 0.I.1 Benchmark Construction Details

**ZH** 0.I.1 基准构建细节

**EN** We use 5 parameters to create the images of nested squares.

**ZH** 我们用 5 个参数生成嵌套正方形的图像。

**EN** • Depth: For each image, we draw ⟦SLOT_238⟧ nested squares on the image. We refer to each square in this collection as a depth.

**ZH** • 层数：对每张图像，我们绘制 ⟦SLOT_238⟧ 个嵌套正方形。我们把该集合中的每个正方形称为一层。

**EN** • Initial size: We choose a random size for the first square in the bounds of the image size.

**ZH** • 初始尺寸：我们在图像尺寸的边界内为第一个正方形随机选取一个尺寸。

**EN** • Reduction factor: We draw squares such that each depth is entirely contained by its previous depth. We use a reduction factor to scale the square sizes.

**ZH** • 缩减因子：我们绘制正方形，使每一层都完整包含于其前一层之内。我们用一个缩减因子来缩放正方形的尺寸。

**EN** • Center: The first square’s center is chosen to ensure it is entirely visible in the image. For the remaining squares, we choose the center based on the space between the previous square and the new reduced size.

**ZH** • 中心：第一个正方形的中心被选取为使其在图像中完整可见。对余下的正方形，我们依据前一个正方形与新的缩减尺寸之间的空间来选择中心。

**EN** • Line thickness: We use standard matplotlib line width parameter of (2=3px, 3=4px, 4=6px).

**ZH** • 线条粗细：我们使用 matplotlib 的标准线宽参数（2=3px、3=4px、4=6px）。

**EN** We continue to generate images until we have 30 samples for each depth, resulting in 120 images overall (see Tabs. T10 and F25).

**ZH** 我们持续生成图像，直到每层各有 30 个样本，共 120 张图像（见表 T10 与图 F25）。

**EN** Code The code is available at https://github.com/anguyen8/vision-llms-are-blind/blob/main/src/NestedSquares/GenerateSamples.ipynb.

**ZH** 代码：代码见 https://github.com/anguyen8/vision-llms-are-blind/blob/main/src/NestedSquares/GenerateSamples.ipynb。

**EN** Post-processing: To determine the model’s answer, we use Python to extract the number from curly braces in the response e.g. {3}.

**ZH** 后处理：为判定模型的答案，我们用 Python 从回答的花括号中抽取数字，例如 {3}。

**EN** Prompts

**ZH** 提示

**EN** 1. How many squares are in the image? Please answer with a number in curly brackets e.g., {10}.

**ZH** 1. 图像中有多少个正方形？请用花括号中的数字回答，例如 {10}。

**EN** 2. Count total number of squares in the image. Answer with only the number in numerical format in curly brackets e.g. {3}.

**ZH** 2. 数出图像中正方形的总数。只用数字格式作答，放在花括号中，例如 {3}。

**EN** Groundtruth answers are ⟦SLOT_239⟧ (random-baseline accuracy: 25%).

**ZH** 真值答案为 ⟦SLOT_239⟧（随机基线准确率：25%）。

<!-- [原子块 · table] (a) 2 squares (b) 3 squares (c) 4 squares (d) 5 squares -->

**EN** Figure F25: Random examples from the nested square task that have 2, 3, 4 or 5 squares in the image.

**ZH** 图 F25：来自嵌套正方形任务的随机示例，图像中含 2、3、4 或 5 个正方形。

<!-- [原子块 · table] GT = 2 GT = 3 GT = 4 GT = 5 -->

**EN** Figure F26: Count squares

**ZH** 图 F26：数正方形

**EN** Table T10: Nested squares include the same number of samples for each parameter value in our benchmark.

**ZH** 表 T10：嵌套正方形在本基准中对每个参数取值都包含相同数量的样本。

<!-- [原子块 · table] Parameter Values Samples Total Samples Image size 1000px 120 120 Line thickness 3px 40 120 4px 40 6px 40 Number of Squares 2 30 120 3 30 4 30 5 30 -->

**EN** 0.I.2 Finding: the best-performing model is affected by line width

**ZH** 0.I.2 发现：表现最好的模型受线宽影响

**EN** Tab. T11 shows that the best VLM on the nested square task (Sonnet-3.5) is more accurate as line width increases. In contrast, the worst model (GPT-4o) shows the opposite trend as the line thickness changes, suggesting that GPT-4o confuses squares when the borderline is thick.

**ZH** 表 T11 显示，嵌套正方形任务上最好的 VLM（Sonnet-3.5）随线宽增大而更准确。相比之下，最差的模型（GPT-4o）随线条粗细变化呈现相反趋势，说明 GPT-4o 在边框较粗时会混淆正方形。

**EN** Table T11: Line thickness has minimal effect on VLMs’ performance, suggesting that visual attributes of shapes are not critical to VLMs when asked to count the shapes.

**ZH** 表 T11：线条粗细对 VLM 表现影响甚微，说明在被要求清点形状时，形状的视觉属性对 VLM 并不关键。

<!-- [原子块 · table] Line width 2 58.75 86.25 61.25 90.00 3 56.25 85.00 67.50 91.25 4 52.50 90.00 66.25 95.00 Average 55.83 87.08 65.00 92.08 -->

**EN** 0.I.3 Additional Examples

**ZH** 0.I.3 补充示例

**EN** We show examples of models’ responses to the counting the number of nested squares task in Fig. F27.

**ZH** 我们在图 F27 中展示模型对数嵌套正方形数量任务提示的回答示例。

<!-- [原子块 · svg]  -->

**EN** Figure F27: VLMs fail to reliably count the number of nested squares in an image.

**ZH** 图 F27：VLM 无法可靠地数出图像中嵌套正方形的数量。

<!-- [原子块 · svg]  -->

**EN** Figure F28: Counting nested squares is not easy for VLMs even when there are only two squares (leftmost). The task becomes harder as the count increases from 2 to 5. Sonnet-3.5 performs the best (92.08%) but still not at the 100% by humans.

**ZH** 图 F28：即便只有两个正方形（最左），数清嵌套正方形对 VLM 也不容易。随着数量从 2 增至 5，任务变得更难。Sonnet-3.5 表现最好（92.08%），但仍未达到人类的 100%。

**EN** Appendix 0.J Counting the shapes in an Olympic-like logo

**ZH** 附录 0.J 清点类奥运标志中的形状

**EN** 0.J.1 Benchmark Construction Details

**ZH** 0.J.1 基准构建细节

**EN** We create the benchmark by generating images containing shapes resembling the Olympic logo by choosing a combination of settings.

**ZH** 我们通过选取一组设置的组合，生成含有类似奥运标志形状的图像来构建基准。

**EN** • Image size: We fix the physical size of the image in matplotlib to 5⟦SLOT_240⟧5, and change the resolution by changing the DPI value, which is ⟦SLOT_241⟧ to get images with sizes ⟦SLOT_242⟧px.

**ZH** • 图像尺寸：我们把 matplotlib 中图像的物理尺寸固定为 5⟦SLOT_240⟧5，并通过改变 DPI 值（即 ⟦SLOT_241⟧）来改变分辨率，得到尺寸为 ⟦SLOT_242⟧px 的图像。

**EN** • Number of shapes: We choose a number from {5, 6, 7, 8, 9}.

**ZH** • 形状数量：我们从 {5, 6, 7, 8, 9} 中选取一个数字。

**EN** • Color: Each image is generated using two different coloring schemes. We generate an all-black version and a second version by randomly sampling colors from a colormap in matplotlib.

**ZH** • 颜色：每张图像用两种不同配色方案生成。我们生成一个全黑版本，以及第二个版本——从 matplotlib 的色图中随机采样颜色。

**EN** • Distance: To generate the interlaced shapes, we use a small boundary-to-boundary distance factor for each row of the shapes. We fix this value to 0.1 proportional to the diameter of circles or side length of pentagons.

**ZH** • 距离：为生成交错的形状，我们为每一行形状使用一个小的边界到边界距离因子。我们把该值固定为圆直径或五边形边长的 0.1 倍。

**EN** • Diameter: We choose a uniform diameter for all the circles in each image from ⟦SLOT_243⟧ proportional to the image size.

**ZH** • 直径：我们为每张图像中的所有圆选取统一的直径，取值为图像尺寸的 ⟦SLOT_243⟧。

**EN** • Side length: We follow the same policy for the diameter to choose the side length of the pentagons.

**ZH** • 边长：我们对五边形的边长采取与直径相同的策略选取。

**EN** • Line thickness: We generate each image with {0.5, 1.0} line width of matplotlib standard. This results in {1px, 2px} lines in 384px images, {2px, 3px} lines in 769px images and {3px, 5px} lines in 1155px images.

**ZH** • 线条粗细：我们用 matplotlib 标准的 {0.5, 1.0} 线宽生成每张图像。这在 384px 图像中产生 {1px, 2px} 线条，在 769px 图像中产生 {2px, 3px} 线条，在 1155px 图像中产生 {3px, 5px} 线条。

**EN** We center the shape collection on the center of the image in two rows, and generate 480 images (see Figs. F29 and T12), 240 images of circles, and 240 images of pentagons.

**ZH** 我们把形状集合分两行居中置于图像中心，生成 480 张图像（见图 F29 与表 T12），其中圆 240 张、五边形 240 张。

**EN** Code The code is available at https://github.com/anguyen8/vision-llms-are-blind/blob/main/src/CountingCircles/OlympicCircles.ipynb for circles and at https://github.com/anguyen8/vision-llms-are-blind/blob/main/src/CountingCircles/OlympicPentagons.ipynb for pentagons.

**ZH** 代码：圆的生成代码见 https://github.com/anguyen8/vision-llms-are-blind/blob/main/src/CountingCircles/OlympicCircles.ipynb，五边形的生成代码见 https://github.com/anguyen8/vision-llms-are-blind/blob/main/src/CountingCircles/OlympicPentagons.ipynb。

**EN** Prompts

**ZH** 提示

**EN** 1. How many {shapes} are in the image? Answer with only the number in numerical format.

**ZH** 1. 图像中有多少个 {形状}？只以数字格式回答。

**EN** 2. Count the {shapes} in the image. Answer with a number in curly brackets e.g. {3}.

**ZH** 2. 数一数图像中的 {形状}。用花括号中的数字回答，例如 {3}。

**EN** where {shapes} = circles or pentagons.

**ZH** 其中 {形状} = 圆或五边形。

**EN** Groundtruth answers are ⟦SLOT_244⟧ (random-baseline accuracy: 20%).

**ZH** 真值答案为 ⟦SLOT_244⟧（随机基线准确率：20%）。

<!-- [原子块 · table] (a) Number of circles (b) Linewidth (c) Color (d) Pentagons -->

**EN** Figure F29: We generate images of (a) different numbers of circles with various parameter changes, e.g., the diameter, (b) the linewidth (in points) (c) colorings, and the image size (in pixels). For the pentagons, we vary the side length instead of the diameter.

**ZH** 图 F29：我们生成含（a）不同数量圆的图像，并改变各种参数，例如直径、（b）线宽（单位为点）、（c）配色与图像尺寸（像素）。对五边形，我们改变的是边长而非直径。

<!-- [原子块 · table] (a) diameter ϕ \phi (b) color: black vs. colorful (c) shape: ○ vs. ⬠ # shapes 5 6 7 8 9 9 -->

**EN** Figure F30: Images span across three sizes and shapes span across two diameters (and two side lengths for ⬠ ), two color options (black vs. colored), and two line widths.

**ZH** 图 F30：图像涵盖三种尺寸，形状涵盖两种直径（ ⬠ 还涵盖两种边长）、两种配色选项（黑色与彩色）与两种线宽。

**EN** Table T12: We create 480 images containing circles and pentagons that are uniformly distributed over various parameters.

**ZH** 表 T12：我们生成 480 张含圆与五边形的图像，在各种参数上均匀分布。

<!-- [原子块 · table] Parameter Values Samples Total Samples Shape Circles 240 480 Pentagons 240 Image size ( C C ) 384px 80 240 769px 80 1155px 80 Line thickness 0.0025 × C 0.0025\times C pixels 120 240 0.005 × C 0.005\ti -->

**EN** 0.J.2 Finding: different resolutions have no impact on most VLMs’ performance

**ZH** 0.J.2 发现：不同分辨率对多数 VLM 的表现没有影响

**EN** Fig. F31-a shows that VLMs are invariant to the resolution when asked to count the overlapping shapes. This suggests that the image quality has almost no effect on the performance, and VLMs cannot see the shapes.

**ZH** 图 F31-a 显示，当被要求清点重叠形状时，VLM 对分辨率不敏感。这说明图像质量对表现几乎没有影响，VLM 就是看不见这些形状。

<!-- [原子块 · table] Counting overlapping circles ○ ○ ○ (a) Resolution (b) Color (c) Number of shapes Counting overlapping pentagons ⬠ ⬠ ⬠ -->

**EN** Figure F31: VLMs perform better on counting overlapping circles ○ ○ ○ (top) than overlapping pentagons ⬠ ⬠ ⬠ (bottom). For most models, resolution (a) and colors (b) have minimal impact on performance. Sonnet-3.5 performs better as the image size increases (a). GPT-4o performs better on colored shapes than on black shapes.

**ZH** 图 F31：VLM 在清点重叠圆 ○ ○ ○ （上）时比清点重叠五边形 ⬠ ⬠ ⬠ （下）表现更好。对多数模型而言，分辨率（a）与颜色（b）对表现影响甚微。Sonnet-3.5 随图像尺寸增大而表现更好（a）。GPT-4o 在彩色形状上比在黑色形状上表现更好。

**EN** 0.J.3 Finding: color-coding does not generally help the VLMs

**ZH** 0.J.3 发现：颜色编码总体上无助于 VLM

**EN** While we expect the color-coding to make the shapes more distinct for the models, Fig. F31-b suggests that, except for GPT-4o, coloring the shapes has an opposite effect on the performance of the models.

**ZH** 虽然我们预期颜色编码能让形状对模型而言更易区分，图 F31-b 却表明，除 GPT-4o 外，给形状着色对模型表现产生了相反的效果。

**EN** 0.J.4 Finding: Gemini-1.5 has the most biased predictions to the Olympic logo

**ZH** 0.J.4 发现：Gemini-1.5 对奥运标志的预测偏差最大

**EN** Fig. F32 shows the overall trend of the predictions among SOTA VLMs. Gemini-1.5 (see Fig. 32(b)) tends to predict “5” significantly more often when asked to count the circles, while its predictions are more random for pentagons. This suggests the model’s bias toward the Olympic logo.

**ZH** 图 F32 展示了各 SOTA VLM 预测的总体趋势。Gemini-1.5（见图 32(b)）在被要求数圆时明显更常预测「5」，而它对五边形的预测则更为随机。这说明该模型存在对奥运标志的偏差。

<!-- [原子块 · object]  -->

**EN** (a) GPT-4o

**ZH** (a) GPT-4o

<!-- [原子块 · object]  -->

**EN** (b) Gemini-1.5

**ZH** (b) Gemini-1.5

<!-- [原子块 · object]  -->

**EN** (c) Sonnet-3

**ZH** (c) Sonnet-3

<!-- [原子块 · object]  -->

**EN** (d) Sonnet-3.5

**ZH** (d) Sonnet-3.5

**EN** Figure F32: Prediction trend for each VLM shows (a) GPT-4o has less variance in counting circles versus pentagons, (b) Gemini-1.5 is biased to predicting the number of circles to be 5, (c) Sonnet-3 tends to under count the number of shapes, and (d) Sonnet-3.5 has the least relative variance over both shapes.

**ZH** 图 F32：各 VLM 的预测趋势显示，（a）GPT-4o 在数圆与数五边形上的方差较小；（b）Gemini-1.5 倾向于把圆的数量预测为 5；（c）Sonnet-3 倾向于低估形状数量；（d）Sonnet-3.5 在两种形状上的相对方差最小。

**EN** Table T13: Frequency (%) of predicting “5” when there are more than 5 circles ( ○ ) or pentagons ( ⬠ ), i.e., ⟦SLOT_245⟧ shapes in the image. For example, Gemini-1.5 predicts “5” circles 99.74% of the time but this tendency disappears in the case of ⬠ (10.94%), showing a strong bias towards the 5-circle Olympic logo (among four models).

**ZH** 表 T13：当图像中的圆（ ○ ）或五边形（ ⬠ ）多于 5 个（即 ⟦SLOT_245⟧ 个形状）时预测为「5」的频率（%）。例如，Gemini-1.5 有 99.74% 的情况预测「5」个圆，但这一倾向在 ⬠ 情形下消失（10.94%），显示出（四款模型中）对五环奥运标志的强烈偏差。

<!-- [原子块 · table] ○ ⬠ ○ ⬠ ○ ⬠ ○ ⬠ 13.54 5.47 99.74 10.94 64.32 5.73 15.89 10.16 -->

**EN** 0.J.5 Additional Examples

**ZH** 0.J.5 补充示例

**EN** We provide examples of VLMs’ responses in Fig. F33.

**ZH** 我们在图 F33 中提供 VLM 回答的示例。

<!-- [原子块 · svg]  -->

**EN** Figure F33: VLMs tend only count the correct number of shapes when the image includes 5 circles. This shows that their predictions are biased toward the actual Olympic logo.

**ZH** 图 F33：VLM 往往只在图像含 5 个圆时才数对形状数量。这说明它们的预测偏向于真实的奥运标志。

<!-- [原子块 · svg]  -->

**EN** Figure F34: Counting overlapped circles is not easy to VLMs regardless of circle colors, line widths, and resolutions. Gemini-1.5 often predicts “5” regardless of the actual circle count, suggesting a strong bias towards the well-known Olympic logo.

**ZH** 图 F34：无论圆的颜色、线宽与分辨率如何，清点重叠圆对 VLM 都不容易。Gemini-1.5 常常不论实际圆数是多少都预测「5」，显示出对广为人知的奥运标志的强烈偏差。

**EN** Appendix 0.K Counting the rows and columns of a grid task

**ZH** 附录 0.K 数网格行与列的任务

**EN** 0.K.1 Benchmark Construction Details

**ZH** 0.K.1 基准构建细节

**EN** Our benchmark specifications consist of various parameters for the grid generation process.

**ZH** 我们的基准规格包含网格生成过程中的各种参数。

**EN** • Image size: We include three different sizes {500, 1250, 2000} to create the grids on the image.

**ZH** • 图像尺寸：我们纳入三种不同尺寸 {500, 1250, 2000} 来在图像上创建网格。

**EN** • Number of rows/columns: We choose a base size ⟦SLOT_246⟧, and initialize the sizes to ⟦SLOT_247⟧, ⟦SLOT_248⟧, and ⟦SLOT_249⟧ where ⟦SLOT_250⟧. We also create 10⟦SLOT_251⟧10 grids to balance the square grids.

**ZH** • 行数/列数：我们选取一个基准尺寸 ⟦SLOT_246⟧，并把尺寸初始化为 ⟦SLOT_247⟧、⟦SLOT_248⟧ 与 ⟦SLOT_249⟧，其中 ⟦SLOT_250⟧。我们也创建 10⟦SLOT_251⟧10 网格，以与方形网格保持均衡。

**EN** • Line thickness: We use a line thickness of 1% of the image size and 0.5% of the image size.

**ZH** • 线条粗细：我们使用为图像尺寸 1% 与 0.5% 的线条粗细。

**EN** • Entry: Each table is generated in two versions, one that includes blank entries, and the second with random text entries.

**ZH** • 内容：每张表格生成两个版本，一个含空白单元格，另一个含随机文字内容。

**EN** We divide the image size by the number of rows and columns to find the coordinates for drawing the borderlines. Then, we draw the lines on the four edges of the image and draw the remaining lines in between. Our benchmark comprises 264 images of blank and text-containing grids (see Tabs. T14 and F35).

**ZH** 我们用图像尺寸除以行数与列数，求得绘制边框线的坐标。然后我们在图像的四条边上画线，并在其间绘制余下的线。我们的基准包含 264 张空白与含文字网格的图像（见表 T14 与图 F35）。

**EN** Code The code is available at https://github.com/anguyen8/vision-llms-are-blind/blob/main/src/CountingRowsAndColumns/Grids.ipynb.

**ZH** 代码：代码见 https://github.com/anguyen8/vision-llms-are-blind/blob/main/src/CountingRowsAndColumns/Grids.ipynb。

**EN** Prompts

**ZH** 提示

**EN** 1. Count the number of rows and columns and answer with numbers in curly brackets. For example, rows={5} columns={6}

**ZH** 1. 数出行的数量与列的数量，并用花括号中的数字回答。例如，行={5} 列={6}。

**EN** 2. How many rows and columns are in the table? Answer with only the numbers in a pair (row, column), e.g., (5,6).

**ZH** 2. 表格中有多少行与多少列？只用一对数字作答，例如 (5,6)。

**EN** Groundtruth answers include both the number of rows and columns. An answer is correct when both column and row counts are correctly predicted (random-chance accuracy is 1/22, i.e., 4.55%).

**ZH** 真值答案同时包含行数与列数。只有当行数与列数都被预测正确时，答案才算正确（随机猜测准确率为 1/22，即 4.55%）。

**EN** Table T14: BlindTest consists of 264 empty and text-containing grids. We create equal number of images for each subcategory.

**ZH** 表 T14：BlindTest 包含 264 个空白与含文字的网格。我们为每个子类创建相同数量的图像。

<!-- [原子块 · table] Parameter Values Samples Total Samples Cell Empty 132 264 Text 132 Image size ( C C ) 500px 44 132 1250px 44 2000px 44 Line thickness 0.005 × C 0.005\times C 66 132 0.01 × C 0.01\times C 66 Dimensions -->

<!-- [原子块 · table] (a) blank (b) text -->

**EN** Figure F35: We create grids with various sizes and line thicknesses. Each grid has a blank (a) and text (b) version.

**ZH** 图 F35：我们创建具有各种尺寸与线宽的网格。每个网格都有空白（a）与文字（b）两个版本。

<!-- [原子块 · table] with text empty (4,4) (4,5) (5,4) -->

**EN** Figure F36: Empty and text-containing grids are generated with various image sizes.

**ZH** 图 F36：空白与含文字的网格以各种图像尺寸生成。

**EN** 0.K.2 Finding: VLMs cannot reliably count either rows or columns

**ZH** 0.K.2 发现：VLM 无法可靠地数清行或列

**EN** We expect counting rows and columns separately to be hard for the VLMs, thus we analyze counting the rows and grids individually to see how VLMs perform. As shown in Tab. T16, VLMs cannot count either rows or columns alone.

**ZH** 我们预期分别数行与数列对 VLM 会很困难，因此单独分析数行与数网格，以观察 VLM 的表现。如表 T16 所示，VLM 单独数行或数列都做不到。

**EN** Table T15: Including text inside grids improves all model accuracies. Sonnet-3.5, yet, outperforms other models on both empty and text-containing grids.

**ZH** 表 T15：在网格中加入文字能提升所有模型的准确率。不过 Sonnet-3.5 在空白与含文字网格上都优于其他模型。

<!-- [原子块 · table] Grid Mean Empty 26.13 26.51 25.00 59.84 34.37 Text 53.03 52.27 47.34 88.68 60.33 Mean 39.58 39.39 36.17 74.26 47.35 -->

**EN** Table T16: Average row and column counting accuracy (%) of VLMs. VLMs perform better at counting columns (70.53% accuracy) than counting rows (60.83%)—both of which are far from the expected 100% accuracy.

**ZH** 表 T16：VLM 数行与数列的平均准确率（%）。VLM 数列（70.53% 准确率）比数行（60.83%）更准——两者都远未达到预期的 100% 准确率。

<!-- [原子块 · table] Axis Mean Rows 65.54 52.95 42.19 82.64 60.83 Columns 58.42 58.50 74.65 90.54 70.53 -->

**EN** 0.K.3 Additional Examples

**ZH** 0.K.3 补充示例

**EN** We show examples of models’ responses to the counting the number of rows and columns task in Figs. F38 and F39.

**ZH** 我们在图 F38 与图 F39 中展示模型对数行与列数量任务的回答示例。

<!-- [原子块 · svg]  -->

**EN** Figure F37: VLMs are often off by one or two in counting rows and columns in an empty grid. The same is true when a grid is small (e.g., 3⟦SLOT_252⟧4) and contains a word in each cell.

**ZH** 图 F37：VLM 在数空网格的行与列时常常相差一或二。当网格较小（例如 3⟦SLOT_252⟧4）且每个单元格含一个单词时，情况同样如此。

<!-- [原子块 · svg]  -->

**EN** Figure F38: Examples from the benchmark show that models consistently fail at counting rows and columns of empty grids. Sonnet-3.5, however, is more consistent in the lower number of rows and columns.

**ZH** 图 F38：来自基准的示例显示，模型在数空网格的行与列时始终失败。不过 Sonnet-3.5 在行数与列数较少时更为稳定。

<!-- [原子块 · svg]  -->

**EN** Figure F39: When text is included in the cells of the grid, the performance of all VLMs improves, especially Sonnet-3.5.

**ZH** 图 F39：当单元格中加入文字时，所有 VLM 的表现都有提升，尤其是 Sonnet-3.5。

**EN** Appendix 0.L Following single-colored paths task

**ZH** 附录 0.L 追踪单色路径任务

**EN** 0.L.1 Benchmark Construction Details

**ZH** 0.L.1 基准构建细节

**EN** Our subway-like graphs are generated using a set of parameters defining the characteristics of the plot.

**ZH** 我们的类地铁图由一组定义图形特征的参数生成。

**EN** • Image size: We use two different sizes {512, 1024}px for the images to include various resolutions.

**ZH** • 图像尺寸：我们用两种不同的尺寸 {512, 1024}px 生成图像，以涵盖各种分辨率。

**EN** • Grid size: We assume a hypothetical grid on the image that determines the position of the paths. We used an 18⟦SLOT_253⟧18 grid, which means each path segment is ⟦SLOT_254⟧ of the image size.

**ZH** • 网格尺寸：我们在图像上假设一个决定路径位置的网格。我们使用 18⟦SLOT_253⟧18 的网格，这意味着每段路径为图像尺寸的 ⟦SLOT_254⟧。

**EN** • Number of stations: We use four station labels, {A, B, C, D}.

**ZH** • 车站数量：我们使用四个车站标签 {A, B, C, D}。

**EN** • Starting points: Each station in our maps has three different starting points which are exactly ⟦SLOT_255⟧ of the image size to one side of the stations.

**ZH** • 起点：我们地图中的每个车站有三个不同的起点，恰好位于距车站一侧 ⟦SLOT_255⟧ 图像尺寸处。

**EN** • Path thickness: We use two line thicknesses, 10 and 20 pixels to have bold and light visualizations of the same path.

**ZH** • 路径粗细：我们使用 10 与 20 像素两种线宽，以呈现同一路径的粗、细两种可视化效果。

**EN** • Number of paths: Considering the number of starting points in our setup, each image can include stations from which exactly 1, 2, or 3 paths exit.

**ZH** • 路径数量：考虑到我们设置中的起点数量，每张图像可以包含恰好发出 1、2 或 3 条路径的车站。

**EN** We keep generating the images until we have 15 samples for each number of paths which results in 180 images (see Tabs. T17 and F40).

**ZH** 我们持续生成图像，直到每种路径数量各有 15 个样本，共 180 张图像（见表 T17 与图 F40）。

**EN** Code The code is available at https://github.com/anguyen8/vision-llms-are-blind/blob/main/src/SubwayMap/SubwayMap.ipynb

**ZH** 代码：代码见 https://github.com/anguyen8/vision-llms-are-blind/blob/main/src/SubwayMap/SubwayMap.ipynb

**EN** Prompts

**ZH** 提示

**EN** 1. How many single-colored paths go from {station 1} to {station 2}? Answer with a number in curly brackets, e.g., {3}.

**ZH** 1. 从 {车站 1} 到 {车站 2} 有多少条单色路径？请用花括号中的数字回答，例如 {3}。

**EN** 2. Count the one-colored routes that go from {station 1} to {station 2}. Answer with a number in curly brackets, e.g., {3}.

**ZH** 2. 数一数从 {车站 1} 到 {车站 2} 的单色路线。用花括号中的数字回答，例如 {3}。

**EN** where the two stations are different and sampled from ⟦SLOT_256⟧.

**ZH** 其中两个车站不同，且从 ⟦SLOT_256⟧ 中采样。

**EN** Groundtruth answers are ⟦SLOT_257⟧ (random-baseline accuracy: 33.33%). Note that, to make the task easier, 0 is excluded from the groundtruth set (i.e., we never ask VLMs to count when no path exists between two given stations).

**ZH** 真值答案为 ⟦SLOT_257⟧（随机基线准确率：33.33%）。需注意，为使任务更简单，0 被排除在真值集合之外（即我们从不要求 VLM 在两站之间不存在路径时去数）。

**EN** Table T17: We create 2 different image resolutions, and 3 various line widths to have balanced number of colored paths.

**ZH** 表 T17：我们创建 2 种不同的图像分辨率与 3 种不同的线宽，以得到数量均衡的彩色路径。

<!-- [原子块 · table] Parameter Values Samples Total Samples Image size 512px 90 180 1024px 90 Line thickness 10px 90 180 20px 90 Paths 1 60 180 2 60 3 60 -->

<!-- [原子块 · table]  -->

**EN** Figure F40: Images in our benchmark (left) have exactly 1, 2, or 3 paths exiting each station. The hypothetical grids (right) are used when generating the paths.

**ZH** 图 F40：我们基准中的图像（左）中，每个车站恰好发出 1、2 或 3 条路径。生成路径时会用到假想网格（右）。

<!-- [原子块 · table]  -->

**EN** Figure F41: On an invisible 18⟦SLOT_258⟧18 grid (bottom right), we randomly generate random paths from one station to another. All stations have an equal ⟦SLOT_259⟧ = 1, 2 or 3 outgoing paths.

**ZH** 图 F41：在一个不可见的 18⟦SLOT_258⟧18 网格（右下）上，我们从一个车站到另一个车站随机生成随机路径。所有车站都有相等的 ⟦SLOT_259⟧ = 1、2 或 3 条出边路径。

**EN** 0.L.2 Finding: VLMs fail to see the colored paths across various map complexities

**ZH** 0.L.2 发现：VLM 在各种地图复杂度下都看不见彩色路径

**EN** All VLMs, except Sonnet-3, start to perform worse as the number of paths per station increases in the images of subway-like maps (Fig. F42).

**ZH** 在类地铁图图像中，随着每个车站的路径数量增加，除 Sonnet-3 外的所有 VLM 表现都开始变差（图 F42）。

<!-- [原子块 · table]  -->

**EN** Figure F42: VLM accuracy decreases as the number of paths increases from 1 to 3. Overall, counting colored paths poses a challenge to VLMs.

**ZH** 图 F42：随着路径数量从 1 增至 3，VLM 的准确率下降。总的来看，清点彩色路径对 VLM 构成挑战。

**EN** 0.L.3 Sonnet-3.5 can more accurately count subway paths on simplified images compared to other VLMs

**ZH** 0.L.3 Sonnet-3.5 在简化图像上比其他 VLM 更能准确定位地铁路径

**EN** Sonnet-3.5 consistently benefits from increasing the probability of choosing the straight path across all image settings (Fig. F43), suggesting its counting ability is generally better than other VLMs, and perhaps the complexity of images is the reason for its initial low performance.

**ZH** Sonnet-3.5 在所有图像设置下都一致地受益于提高选择直行路径的概率（图 F43），说明其清点能力总体优于其他 VLM，而图像复杂性或许正是它起初表现不佳的原因。

<!-- [原子块 · table]  -->

**EN** Figure F43: Sonnet-3.5 has the largest mean performance gain (+27) from ⟦SLOT_260⟧ 0.33 to 0.9 when we increase the probability of choosing a straight path.

**ZH** 图 F43：当我们把选择直行路径的概率从 ⟦SLOT_260⟧ 0.33 提高到 0.9 时，Sonnet-3.5 的平均性能增益最大（+27）。

**EN** 0.L.4 Additional Examples

**ZH** 0.L.4 补充示例

**EN** We show examples of models’ responses to the counting the number of single-colored connecting paths in Fig. F44.

**ZH** 我们在图 F44 中展示模型对清点单色连接路径数量的回答示例。

<!-- [原子块 · svg]  -->

**EN** Figure F44: VLMs generally fail at images with more intersecting paths. As the number of paths increases, models tend to make an educated guess, especially Gemini-1.5 and Sonnet-3.5.

**ZH** 图 F44：VLM 普遍在相交路径更多的图像上失败。随着路径数量增加，模型倾向于做出经验性猜测，Gemini-1.5 与 Sonnet-3.5 尤甚。

<!-- [原子块 · svg]  -->

**EN** Figure F45: Some VLMs (, , ) surprisingly fail in even extremely easy cases across both line widths (leftmost). VLMs tend to perform worse as the number of paths connecting stations increases.

**ZH** 图 F45：某些 VLM（ 、 、 ）竟在极其简单的情形中也失败，两种线宽下皆然（最左）。随着连接车站的路径数量增加，VLM 的表现往往更差。

**EN** Appendix 0.M VLM failures on real-world data

**ZH** 附录 0.M VLM 在真实数据上的失败

<!-- [原子块 · svg]  -->

**EN** Figure F46: Examples of how VLMs fail on real-world data.

**ZH** 图 F46：VLM 在真实数据上失败的示例。

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

**EN** Figure F47: Examples of how VLMs fail on real-world data.

**ZH** 图 F47：VLM 在真实数据上失败的示例。

**EN** Appendix 0.N Linear Probing Experiment for ⟦SLOT_261⟧ and ⟦SLOT_262⟧ tasks

**ZH** 附录 0.N ⟦SLOT_261⟧ 与 ⟦SLOT_262⟧ 任务的线性探测实验

**EN** 0.N.1 Implementation details

**ZH** 0.N.1 实现细节

**EN** We use identical hyperparameters for all probing experiments and provide their values in Tab. T18. We also provide the feature dimensions of each model in Tab. T19.

**ZH** 我们对所有探测实验使用相同的超参数，并在表 T18 中给出其取值。我们还在表 T19 中提供每个模型的特征维度。

**EN** Table T18: The list of hyperparameters for training the linear classifier on frozen features of ⟦SLOT_263⟧ and ⟦SLOT_264⟧ in scikit-learn.

**ZH** 表 T18：在 scikit-learn 中基于 ⟦SLOT_263⟧ 与 ⟦SLOT_264⟧ 的冻结特征训练线性分类器所用的超参数列表。

<!-- [原子块 · table] Config Value Model Logistic Regression Regularization L2 Regularization Weight 1.0 Random seed 42 Training epochs 1000 -->

**EN** Table T19: LLaVA-OneV-S generates features with various dimensions for each input size. However, after the average pooling the frozen features for different image sizes have identical dimensions.

**ZH** 表 T19：LLaVA-OneV-S 对不同输入尺寸生成的特征维度各异。不过在平均池化之后，不同图像尺寸的冻结特征具有相同的维度。

<!-- [原子块 · table] Model Stage input dim. output dim. after pooling vision encoder 384 × \times 385 [3, 729, 1152] [1, 1152] 769 × \times 770 [10, 729, 1152] 1155 × \times 1155 [17, 729, 1152] projection layer 384 × \ti -->

**EN** 0.N.2 Additional results

**ZH** 0.N.2 补充结果

**EN** The linear classifier, i.e., logistic regression, performs with 99% accuracy on the two circles (Fig. F48) and the line charts tasks (Fig. F49), when trained and tested on the images with the same visual complexities (Figs. F48 and F49; diagonal axis highlighted with black outline).

**ZH** 当在视觉复杂度相同的图像上训练与测试时（图 F48 与图 F49；对角线轴以黑色轮廓高亮），线性分类器（即逻辑回归）在两圆（图 F48）与折线图（图 F49）任务上达到 99% 的准确率。

**EN** Moreover, transferring the classifier trained in small to large gaps shows an accuracy comparable to the baseline accuracy of these VLMs, suggesting the sufficiency of frozen features for solving the selected tasks from BlindTest.

**ZH** 此外，把在小间距上训练的分类器迁移到大间距上，其准确率与这些 VLM 的基线准确率相当，说明冻结特征足以解决 BlindTest 中所选定的任务。

<!-- [原子块 · table] vision encoder projection layer -->

**EN** Distance between circles:

**ZH** 圆之间的距离：

**EN** ⟦SLOT_265⟧-axis ⟦SLOT_266⟧ training sets.

**ZH** ⟦SLOT_265⟧ 轴 ⟦SLOT_266⟧ 训练集。

**EN** ⟦SLOT_267⟧-axis ⟦SLOT_268⟧ test sets

**ZH** ⟦SLOT_267⟧ 轴 ⟦SLOT_268⟧ 测试集

**EN** Figure F48: The linear classifier trained on frozen features of images, where objects (⟦SLOT_269⟧) are close (⟦SLOT_270⟧), performs well (100%) on images that contain objects that are far apart (⟦SLOT_271⟧), for both models and stages. Conversely, the classifier performs worse (at least 18%), when transferred from large to small distances.

**ZH** 图 F48：在物体（⟦SLOT_269⟧）靠得较近（⟦SLOT_270⟧）的图像冻结特征上训练的线性分类器，在含相距较远（⟦SLOT_271⟧）物体的图像上表现良好（100%），两个模型与两个阶段皆然。反之，当从大间距迁移到小间距时，分类器表现更差（至少下降 18%）。

<!-- [原子块 · table] vision encoder projection layer -->

**EN** Mean distance brackets: ⟦SLOT_272⟧ training sets ⟦SLOT_273⟧ testing sets

**ZH** 平均距离区间：⟦SLOT_272⟧ 训练集 ⟦SLOT_273⟧ 测试集

**EN** Figure F49: The frozen features of both the projection layer and the VE output contain sufficient information to count the intersections between the line charts ⟦SLOT_274⟧. Moreover, the mean distance between the y coordinates of line charts controls the visual complexity of the images, where transferring the trained classifier from small (⟦SLOT_275⟧) to large (⟦SLOT_276⟧) distances, compared to transfer from large to small distances, has lower impacts on the classification performance (24% vs. 39%; the first and last row in the top-right heatmap).

**ZH** 图 F49：投影层与 VE 输出二者的冻结特征都含有足以数清折线图 ⟦SLOT_274⟧ 之间交点的信息。此外，折线图 y 坐标之间的平均距离控制着图像的视觉复杂度，其中把训练好的分类器从小间距（⟦SLOT_275⟧）迁移到大间距（⟦SLOT_276⟧），相比从大间距迁移到小间距，对分类性能的影响更小（24% 对 39%；右上热力图的首行与末行）。
