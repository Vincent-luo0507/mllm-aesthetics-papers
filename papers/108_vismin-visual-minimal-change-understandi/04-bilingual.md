# VisMin：视觉最小改动理解

> 原标题：VisMin: Visual Minimal-Change Understanding
> 作者：Rabiul Awal, Saba Ahmadi, Le Zhang, Aishwarya Agrawal · arXiv:2407.16772 · 2024-07-23

<!-- [原子块 · verbatim] VisMin: Visual Minimal-Change Understanding -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] Fine-grained understanding of objects, attributes, and relationships between objects is crucial for visual-language models (VLMs). To evaluate VLMs’ fine-grained understanding, existing benchmarks pri -->

**EN** 1 Introduction

**ZH** 1 引言

<!-- [原子块 · img]  -->

**EN** Figure 1: Overview of our VisMin benchmark. VisMin consists of four types of minimal-changes – object, attribute, count and spatial relation – between two image-captions pairs. The evaluation task requires a model to predict the correct image-caption match given: 1) two images and one caption, 2) two captions and one image.

**ZH** 图 1：VisMin 基准概览。VisMin 包含物体、属性、计数与空间关系四类最小改动，分布于两对图文之间。评测任务要求模型在给定条件下预测正确的图文匹配：1) 两张图像与一条描述；2) 两条描述与一张图像。

**EN** Fine-grained understanding of objects, attributes, and their relationships is critical for Visual-Language Models (VLMs) to generalize effectively to new, unseen scenes and compositions. Previous studies such as ARO [43] and Sugarcrepe [8], highlighting the deficiencies of VLMs in this domain predominantly focus on understanding fine-grained differences between two very similar captions -- a human-written caption and an automatically generated hard-negative11 1 In the context of contrastive learning, a hard-negative is a specific type of negative example that is particularly challenging to distinguish from the positive example. caption, where the hard-negative caption differs from the original caption only with respect to an object, or an attribute or a relationship between two objects. While such hard-negative examples for captions can be synthesized using rule-based approaches, synthesizing such hard-negative examples for images is very challenging. Existing benchmarks presenting visual hard-negatives suffer from two main limitations: 1) Limited Difficulty: In benchmarks such as Winoground [36], MMVP[37], the original images and their hard-negative counterparts differ in multiple aspects (objects, attributes of objects, image background, etc.). This multiplicity limits the difficulty of the benchmark and makes it challenging to precisely evaluate the models’ fine-grained understanding of specific aspects. 2) Limited Complexity: Although benchmarks such as EQBEN [38], SPEC [28] have controlled hard-negatives, the visual domain is limited to graphic engines, a few video domains or reliance on purely synthetic images depicting simplistic scenes.

**ZH** 对物体、属性及其相互关系的细粒度理解，是视觉—语言模型（VLM）有效泛化到未见新场景与新组合的关键。ARO[43] 与 Sugarcrepe[8] 等已有工作揭示了 VLM 在这一领域的不足，但它们主要关注两条高度相似描述之间的细粒度差异——一条人工撰写的描述与一条自动生成的难负例11 1 在对比学习的语境下，难负例指特别难以与正例区分的一类负例。描述，其中难负例描述只在物体、属性或两个物体间的关系上与原描述不同。这类描述层面的难负例可以用基于规则的方法合成，但合成图像层面的难负例则极具挑战。已有提供视觉难负例的基准存在两方面局限：1) 难度有限：在 Winoground[36]、MMVP[37] 等基准中，原始图像与其难负例在多个方面（物体、物体属性、图像背景等）同时存在差异。这种多重差异限制了基准的难度，也使精确评估模型对特定方面的细粒度理解变得困难。2) 复杂度有限：尽管 EQBEN[38]、SPEC[28] 等基准具备受控的难负例，其视觉领域局限于图形引擎、少数视频领域，或依赖描绘简单场景的纯合成图像。

**EN** Motivated by these observations, we propose a new benchmark, Visual Minimal-Change Understanding (VisMin ), built on top of the images from the COCO [22] dataset that consists of complex everyday scene images. VisMin is designed to measure VLMs’ ability to comprehend minimal changes, i.e., changes with respect to only one aspect (see Fig. 1), from among the following aspects: object, attribute, count, and spatial relation, while keeping other aspects unchanged as much as possible.

**ZH** 受这些观察启发，我们提出一个新的基准——视觉最小改动理解（VisMin），它构建在 COCO[22] 数据集中复杂日常场景图像的基础之上。VisMin 旨在衡量 VLM 理解最小改动的能力，即只在一个方面发生变化（见图 1）的改动，这些方面包括：物体、属性、计数与空间关系，同时尽可能保持其他方面不变。

**EN** The evaluation task for a model is to predict the correct image-caption match given: 1) two images and one caption, 2) two captions and one image. To curate VisMin , we built an automated pipeline using large language models and diffusion models. To ensure the quality of our benchmark, the synthetic data generated using the automated pipeline undergoes a rigorous 4-step verification process by human annotators, with data retained in the benchmark only if it passes all four steps. We meticulously designed the benchmark ensuring uniformity across various categories to the extent possible. We conduct a detailed analysis of our benchmark, which enables a more transparent assessment of the various strengths and weaknesses of the models.

**ZH** 模型的评测任务是：在给定 1) 两张图像与一条描述，或 2) 两条描述与一张图像的条件下，预测正确的图文匹配。为构建 VisMin，我们用大语言模型与扩散模型搭建了一条自动化流程。为保证基准质量，自动流程生成的合成数据需经过标注人员严格的四步验证，只有全部四步都通过的数据才会保留在基准中。我们精心设计基准，尽可能保证各类别之间的均衡，并对基准做了细致分析，从而更透明地评估模型的各项长处与短板。

**EN** We conducted empirical tests on eight open-source VLMs, including foundational models like CLIP [31] and Multimodal Large Language Models (MLLMs) such as Llava[24] and Idefics2[15]. We also evaluated two closed-source APIs, GPT-4 and Gemini. Our findings suggest that both foundational models and MLLMs perform relatively well in understanding minimal changes in objects and attributes. Surprisingly, MLLMs underperform foundational VLMs in object and attribute understanding! For spatial relation understanding, although MLLMs perform better than VLMs, both families of models perform below random chance! Similarly, both families of models show considerable room for improvement in counting capabilities. Our results underscore the need for a emphasis on spatial reasoning and counting understanding over attribute/object recognition in VLM evaluations. We anticipate that our benchmark will catalyze advancements in these critical areas within the community.

**ZH** 我们在八个开源 VLM 上做了实证测试，包括 CLIP[31] 等基座型模型，以及 Llava[24]、Idefics2[15] 等多模态大语言模型（MLLM）；同时评估了两个闭源 API：GPT-4 与 Gemini。我们发现，基座型模型与 MLLM 在理解物体与属性的最小改动上表现都相对不错。令人意外的是，MLLM 在物体与属性理解上竟不如基座型 VLM！在空间关系理解上，尽管 MLLM 优于 VLM，两类模型的表现都低于随机猜测水平！同样，两类模型在计数能力上都还有相当大的提升空间。这些结果说明，VLM 评测应当把重心从属性/物体识别转向空间推理与计数理解。我们期待本基准能推动学界在这些关键方向上取得进展。

**EN** Lastly, owing to the automated nature of our synthetic data creation process, we generated a large-scale (64,392 samples) minimal-change image-text data for fine-tuning the VLMs to enhance their fine-grained understanding. Fine-tuning CLIP (a foundational VLM) and Idefics2 (a MLLM) on our minimal-change data, without any additional modifications to the model architecture or loss functions, results in significant improvements in fine-grained understanding across various benchmarks. Notably, such fine-tuning also enhances foundational VLMs’ general image-text alignment capabilities as evident by marked improvements in CLIP’s image-text retrieval performance on COCO. These observations suggest that our minimal-change dataset can serve as model-agnostic, general-purpose resource to enhance the capabilities of VLMs.

**ZH** 最后，由于合成数据生成过程是自动化的，我们进一步生成了大规模（64,392 个样本）的最小改动图文数据，用于微调 VLM 以增强其细粒度理解。在不改动模型架构与损失函数的前提下，用我们的最小改动数据微调 CLIP（基座型 VLM）与 Idefics2（MLLM），可在多个基准上显著提升细粒度理解。值得注意的是，这种微调也增强了基座型 VLM 的通用图文对齐能力——CLIP 在 COCO 上图文检索性能的大幅提升即是明证。这些观察说明，我们的最小改动数据集可以作为一种与模型无关的通用资源，用于提升 VLM 的能力。

**EN** To summarize, our contributions are threefold: 1) A controlled and challenging benchmark. We introduce the VisMin benchmark, which challenges models to detect semantic differences between visually similar but semantically different images. Extensive testing on foundational VLMs and MLLMs reveals their difficulties with this task, highlighting areas for improvement. 2) A pipeline for automated data creation and benchmark development. We create an automated pipeline to generate visual minimal-change data at scale using large language models and diffusion models, with a rigorous four-step human verification system to ensure high data quality. 3) Enhancement of VLMs’ fine-grained understanding with fine-tuning on minimal-change data. We improve the fine-grained understanding of CLIP and Idefics2 by fine-tuning them on our large-scale minimal-change image-text data, demonstrating improved image-text alignment and overall performance.

**ZH** 综上，我们的贡献有三个方面：1) 一个受控且富有挑战性的基准。我们提出 VisMin 基准，要求模型识别视觉上相似但语义不同的图像之间的语义差异。在基座型 VLM 与 MLLM 上的大量测试揭示了它们在该任务上的困难，指出了有待改进的方向。2) 一条自动化数据生成与基准构建流程。我们构建了一条自动化流程，用大语言模型与扩散模型规模化生成视觉最小改动数据，并配有严格的四步人工验证体系以保证数据质量。3) 通过在最小改动数据上微调增强 VLM 的细粒度理解。我们在大规模最小改动图文数据上微调 CLIP 与 Idefics2，提升了它们的细粒度理解，并展现出更好的图文对齐与整体性能。

**EN** 2 Related work

**ZH** 2 相关工作

**EN** Fine-grained understanding benchmarks: Most existing benchmarks focus on understanding fine-grained textual differences, such as VL-checklist [47], ARO [43], and Sugarcrepe [8]. Benchmarks presenting visual hard-negatives, such as EQBEN [38], Winoground [36], ImageCode [14], SPEC [28], either lack minimal changes or have limited visual complexity – graphic engines, a few video domains or purely synthetic images depicting simplistic scenes. Our benchmark addresses these gaps by utilizing the advances in LLMs [10] and diffusion models [30, 20, 21] to achieve minimal changes in complex COCO-like scenes without compromising the naturalness of the images, thus providing a more robust evaluation of fine-grained visual understanding in VLMs. Detailed comparisons of benchmarks are provided in section 4.

**ZH** 细粒度理解基准：现有基准大多关注文本层面的细粒度差异，如 VL-checklist[47]、ARO[43] 与 Sugarcrepe[8]。提供视觉难负例的基准，如 EQBEN[38]、Winoground[36]、ImageCode[14]、SPEC[28]，要么缺少最小改动，要么视觉复杂度有限——局限于图形引擎、少数视频领域或描绘简单场景的纯合成图像。我们的基准利用 LLM[10] 与扩散模型[30, 20, 21] 的进展，在类似 COCO 的复杂场景中实现最小改动，同时不损害图像的自然度，从而填补了上述空白，为 VLM 的细粒度视觉理解提供了更稳健的评估。基准之间的详细对比见第 4 节。

**EN** Automatic approach to generate visual hard negatives: Existing approaches to automatically generate visual hard negatives fall into three broad categories: (i) using nearby video frames with semantic changes [14, 38], (ii) using graphic engines [38], (iii) using diffusion models [28, 38, 17]. Our proposed framework falls in the third category. DEMON[17] is the closest to our work, creating training data using diffusion models to improve the learning of a given vision-language model. They use diffusion models to perform local editing on the images given the target object mask. However, this approach requires attention masks from the vision-language model being studied. SPEC [28] proposes a diffusion-based canvas-filling method for generating minimally-different image pairs limited to four types of minimal changes: size, position, count and existence. Compared to these existing methods, our automated pipeline to generate minimal-change data is more involved in order to achieve minimal-changes in complex scenes while maintaining the photo-realism of the scene and controlling changes across diverse categories. Our pipeline also has more a comprehensive automated filtering mechanism compared to previous pipelines that mainly rely on CLIP-based filtering.

**ZH** 自动生成视觉难负例的方法：现有自动生成视觉难负例的方法大致分为三类：(i) 利用存在语义变化的邻近视频帧[14, 38]；(ii) 利用图形引擎[38]；(iii) 利用扩散模型[28, 38, 17]。我们的框架属于第三类。DEMON[17] 与我们的工作最为接近，它用扩散模型生成训练数据以改进给定视觉—语言模型的学习：给定目标物体的掩码，用扩散模型对图像做局部编辑。但该方法需要从所研究的视觉—语言模型中获取注意力掩码。SPEC[28] 提出一种基于扩散的画布填充方法，用于生成最小差异图像对，但只覆盖四类最小改动：尺寸、位置、计数与存在性。与这些已有方法相比，我们生成最小改动数据的自动化流程更为精细，以便在复杂场景中实现最小改动，同时保持场景的照片真实感，并跨多种类别控制改动。与以往主要依赖 CLIP 过滤的流程相比，我们的流程还具备更完善的自动过滤机制。

**EN** Enhancing fine-grained understanding in VLMs with hard negatives: Most methods to enhance fine-grained understanding in VLMs like CLIP focus on fine-tuning with caption-based hard negatives and optimizing loss functions to better use these signals [42, 46, 33]. Common strategies for generating textual hard negatives include heuristic rules [43], language models [46, 5], scene-graph information [7, 33], and LLMs integrated with semantic segmentation [6]. In contrast, fewer works explore visual hard negatives; methods like NegCLIP [42] and General Scene Difference [16] rely on nearest-neighbor images, which often differ too much or too little in context, limiting fine-grained learning. Our approach is closest to SPEC [28] and CounterCurate [45], which also fine-tune VLMs using minimal-change visual hard negatives. Unlike SPEC, we and CounterCurate extend this to multimodal large language models, but our work evaluates performance on 10 out-of-distribution benchmarks (compared to 1 or 2 in SPEC and CounterCurate) and outperforms baseline models in most cases, demonstrating the strength of our approach (see Tables 3 and 4).

**ZH** 用难负例增强 VLM 的细粒度理解：增强 CLIP 等 VLM 细粒度理解的方法，大多聚焦于用基于描述的难负例微调，并优化损失函数以更好地利用这些信号[42, 46, 33]。生成文本难负例的常见策略包括启发式规则[43]、语言模型[46, 5]、场景图信息[7, 33]，以及与语义分割相结合的 LLM[6]。相比之下，探索视觉难负例的工作较少；NegCLIP[42] 与 General Scene Difference[16] 等方法依赖最近邻图像，而这些图像在语境上往往差异过大或过小，限制了细粒度学习。我们的方法与 SPEC[28] 和 CounterCurate[45] 最为接近，二者同样用最小改动的视觉难负例微调 VLM。与 SPEC 不同，我们与 CounterCurate 都把这一思路扩展到了多模态大语言模型；而且我们的工作在 10 个分布外基准上评估性能（SPEC 与 CounterCurate 只用了 1 到 2 个），并在多数情况下优于基线模型，体现了本方法的优势（见表 3 与表 4）。

**EN** 3 Minimal-Change Image-Text Dataset Creation

**ZH** 3 最小改动图文数据集的构建

**EN** We devised a framework to synthesize large-scale minimal-change data and introduce the VisMin benchmark (see overview fig. 2). The pipeline includes three stages: Minimal-Change Pairs Synthesis, where we minimally edit image and text pairs; Automatic Filtering, which verifies the faithfulness of the texts and synthesized images; and Human Verification, a four-step process to ensure that only data meeting all quality criteria is included. We will discuss each stage in detail.

**ZH** 我们设计了一套框架来合成大规模最小改动数据，并由此提出 VisMin 基准（概览见图 2）。流程包含三个阶段：最小改动对合成，即最小化地编辑图像与文本对；自动过滤，校验文本与合成图像的忠实度；人工验证，通过四步流程确保只有满足全部质量标准的数据才会被收录。下面逐一详述各阶段。

**EN** Figure 2: Our dataset creation pipeline includes three stages: (i) Minimal-Change Pairs Synthesis: We develop methods for synthesizing minimal-change image-caption pairs involving Objects & Attributes and Counting & Spatial Relations. (ii) Automatic Filtering: An LLM generates questions and answers based on captions, and a VQA model predicts answers from images. Synthetically generated minimal-change data are excluded if answers don’t match. (iii) Human Verification: Synthetically generated minimal-change data undergoes a rigorous 4-steps human verification, and only examples passing all stages are included in the benchmark.

**ZH** 图 2：我们的数据集构建流程包含三个阶段：(i) 最小改动对合成：我们针对物体与属性、计数与空间关系分别开发了合成最小改动图文对的方法。(ii) 自动过滤：由 LLM 依据描述生成问答，再由 VQA 模型从图像中预测答案；若答案不匹配，则剔除该合成最小改动数据。(iii) 人工验证：合成最小改动数据需经过严格的四步人工验证，只有全部阶段都通过的样本才会收录进基准。

<!-- [原子块 · img]  -->

**EN** Stage 1: Minimal-Change Pairs Synthesis In the first stage of our pipeline, we focus on synthesizing minimal-change image-text pairs across four strategic categories: objects, attributes, counting, and spatial relations. These categories are specifically chosen to test various levels of visual-linguistic comprehension. We generate minimal-change text pairs using LLM and then generate minimal-change image pairs using diffusion models. Our synthesis process distinctly tailors the creation of image-text pairs to the specific needs of each category, depicted in Stage 1 in Figure 2 (Object & Attribute Edit and Count & Spatial Relation Edit blocks).

**ZH** 阶段 1：最小改动对合成 在流程的第一阶段，我们聚焦在物体、属性、计数与空间关系四个策略性类别上合成最小改动图文对。选择这些类别是为了检验不同层次的视觉—语言理解能力。我们先用 LLM 生成最小改动文本对，再用扩散模型生成最小改动图像对。合成过程针对每个类别的具体需求分别定制图文对的生成方式，如图 2 阶段 1 所示（物体与属性编辑、计数与空间关系编辑两个模块）。

**EN** LLM-guided Edit Instructions Generation To generate minimal-change text pairs, we start with source captions and then prompt an LLM (Mistral 47B [10]) to generate both the edit instructions specific to each edit category and the corresponding edited caption (see Appendix A.2.1 for the prompt used). For Object and Attribute edits, we use human-written captions from COCO [22] and VSR [23] datasets as our source captions. The LLM processes these captions to suggest edits targeting specific objects or attributes. For example, given the source caption “A dog in the middle of the couch”, the LLM generates the edit instruction “change dog to doll” which contains both the source phrase (“dog”) and the edited phrase (“doll”). The LLM also generates the edited caption “A doll in the middle of the couch”. We generate five plausible (based on the criteria outlined for LLM prompting) edit instructions and edited captions per source caption. To ensure the edited captions are minimally changed w.r.t the source caption and contain visually plausible changes, we prompt the LLM again for filtering, removing ⟦SLOT_0⟧ of the total LLM outputs that do not meet those criteria (see section A.2.2 for details on the criteria). For Counting and Spatial Relation edits, we generate the source captions synthetically due to the absence of a suitable human-written captions dataset containing descriptions of counts and spatial relations of objects. We prompt the LLM to create captions and outline object layouts and bounding boxes. For instance, the LLM might generate a caption like “A plate of cookies on a table and a cup of coffee to its right,” with the corresponding bounding boxes: {“plate of cookies”: ⟦SLOT_1⟧; “cup of coffee”: ⟦SLOT_2⟧}. The LLM generates a large pool of such synthetic captions. The edit instructions and the corresponding edited captions are generated using a rule-based method aimed at swapping the object positions for spatial relation edits (e.g. edited caption: “A cup of coffee on a table and a plate of cookies to its right”, swapped bounding boxes: {“1st crop”: ⟦SLOT_3⟧; “2nd crop”: ⟦SLOT_4⟧) or adjusting the object counts for counting edits (e.g. edited caption: “A cup of coffee on a table”), removed bounding boxes: {⟦SLOT_5⟧}, in this example removing the plate of cookies from the image.

**ZH** LLM 引导的编辑指令生成 为生成最小改动文本对，我们从源描述出发，提示 LLM（Mistral 47B[10]）生成针对各编辑类别的编辑指令及相应的编辑后描述（所用提示见附录 A.2.1）。对于物体与属性编辑，我们使用 COCO[22] 与 VSR[23] 数据集中的人工撰写描述作为源描述，LLM 处理这些描述后给出针对特定物体或属性的编辑建议。例如，给定源描述「沙发中间有一只狗」，LLM 生成编辑指令「把狗换成玩偶」，其中同时包含源短语（「狗」）与编辑后短语（「玩偶」）；LLM 还生成编辑后的描述「沙发中间有一个玩偶」。我们为每条源描述生成五条合理（依据 LLM 提示中列出的标准）的编辑指令与编辑后描述。为确保编辑后描述相对源描述改动最小、且包含视觉上合理的改动，我们再次提示 LLM 进行过滤，剔除占 LLM 总输出 ⟦SLOT_0⟧ 的不满足上述标准的结果（标准细节见 A.2.2 节）。对于计数与空间关系编辑，由于缺乏包含物体计数与空间关系描述的合适人工撰写描述数据集，我们改为合成源描述：提示 LLM 生成描述并给出物体布局与边界框。例如，LLM 可能生成描述「桌上有一盘饼干，右边有一杯咖啡」，并给出对应的边界框：{「一盘饼干」: ⟦SLOT_1⟧; 「一杯咖啡」: ⟦SLOT_2⟧}。LLM 会生成大量此类合成描述。编辑指令与相应的编辑后描述则用基于规则的方法生成：空间关系编辑旨在交换物体的位置（例如编辑后描述：「桌上有一杯咖啡，右边有一盘饼干」，交换后的边界框：{「第 1 个裁剪块」: ⟦SLOT_3⟧; 「第 2 个裁剪块」: ⟦SLOT_4⟧）；计数编辑则旨在调整物体数量（例如编辑后描述：「桌上有一杯咖啡」，移除的边界框：{⟦SLOT_5⟧}，本例中即从图像中移除那盘饼干）。

**EN** Diffusion-guided Image Synthesis We modify images according to the edit instructions generated by the LLM in the previous step. For Object and Attribute edits, we first mask the object to be edited in the source image using the Grounding-DINO model [25]. We obtain the source images from the COCO dataset. The object to be edited is specified in the source phrase of the edit instruction (e.g., “a dog” in the edit instruction “change dog to doll”). We then apply the SDXL inpainting model [30], using the input image, masked region, and edited phrase (obtained from the edit instruction, e.g., “a doll” in the edit instruction “change dog to doll”) to alter the masked image region to match the desired outcome, e.g., changing “a dog" to “a doll.” For Counting and Spatial Relation edits, we create a synthetically generated source image dataset based on LLM-suggested layouts from the previous step, using the LLM-grounded Diffusion (LMD) model [21] for image synthesis. To create an edited image, for the spatial relation edits, we first reposition the source image’s bounding boxes using a rule-based method. We then obtain image crops from the source image corresponding to the objects which we need to reposition w.r.t each other. Lastly, we use the GLIGEN layout-diffusion model [20] to smoothly insert the obtained crops into the source image at the repositioned bounding box locations. For counting edits, we obtain the edited image by always removing one or multiple objects from the source image. The object to be removed is specified by masking and we use the Lama model [34] to carry out the object removal. We employ layout-based diffusion models [21, 20] instead of using end-to-end diffusion models like Stable diffusion [30] as the layout-based model facilitates precise control over the object positions and counts and thus ensures the changes are faithful to the edit instruction as well as minimal. Unfortunately, end-to-end models such as Stable Diffusion are not good at precisely editing object positions and counts.

**ZH** 扩散模型引导的图像合成 我们依据上一步 LLM 生成的编辑指令修改图像。对于物体与属性编辑，先用 Grounding-DINO 模型[25] 在源图像中掩码待编辑的物体，源图像取自 COCO 数据集。待编辑物体由编辑指令中的源短语指定（如编辑指令「把狗换成玩偶」中的「狗」）。随后我们应用 SDXL 修复模型[30]，以输入图像、掩码区域与编辑后短语（取自编辑指令，如「把狗换成玩偶」中的「玩偶」）为条件，把掩码区域修改为期望的结果，例如把「一只狗」变成「一个玩偶」。对于计数与空间关系编辑，我们先基于上一步 LLM 建议的布局，用 LLM grounded 扩散（LMD）模型[21] 合成源图像数据集。生成编辑后图像时，空间关系编辑先用基于规则的方法重新排布源图像的边界框，再从源图像中裁出需要相互重新定位的物体图像块，最后用 GLIGEN 布局扩散模型[20] 把这些图像块平滑地插回源图像中重新定位后的边界框位置。计数编辑则一律通过从源图像中移除一个或多个物体来得到编辑后图像：待移除的物体由掩码指定，并用 Lama 模型[34] 完成物体移除。我们采用基于布局的扩散模型[21, 20]，而非 Stable Diffusion[30] 这类端到端扩散模型，因为基于布局的模型便于精确控制物体位置与数量，从而保证改动既忠实于编辑指令、又足够小。遗憾的是，Stable Diffusion 这类端到端模型并不擅长精确编辑物体的位置与数量。

**EN** Stage 2: Automatic Filtering To ensure consistency of synthesized hard-negative images, we use a VQA-based filtering system, which is more effective than object detection (see Stage 2 in Figure 2). Questions generated by an LLM [10] based on the edit instruction and caption (following TIFA [9]) verify that edits align with the caption and that the positive caption no longer applies to the negative image. We use LLaVa 7B [24] to answer these questions, with region-specific questions for object/attribute edits and global questions for background consistency. This process removes ⟦SLOT_6⟧% of synthesized images, ensuring dataset quality.

**ZH** 阶段 2：自动过滤 为保证合成的难负例图像保持一致，我们采用基于 VQA 的过滤系统，它比目标检测更有效（见图 2 阶段 2）。由 LLM[10] 依据编辑指令与描述生成问题（沿用 TIFA[9] 的做法），以校验编辑是否与描述一致、以及正例描述是否不再适用于负例图像。我们用 LLaVa 7B[24] 回答这些问题：对物体/属性编辑提出区域相关问题，对背景一致性提出全局问题。该过程剔除了 ⟦SLOT_6⟧% 的合成图像，保证了数据集质量。

**EN** Stage 3: Human Verification To ensure high-quality of the benchmark, on top of automated filtering, we conduct human verification using the Amazon Mechanical Turk platform. The images and captions undergo four steps of verification, requiring agreement from at least four out of five annotators at each step to pass the human verification. The steps are: 1) Naturalness and Image-Text Matching Verification: Annotators assess if (a) the image looks natural, (b) the caption is sensical, and (c) the image matches the caption. Only 26% of synthetic images pass this step, mainly due to the criterion (a), where counting and spatial relation images often look unnatural. See Appendix Table 7 for detailed acceptance rates. 2) Visual Edit Verification: Annotators assess if the images faithfully reflect the specified minimal edits without additional changes, with an acceptance rate of 80%. 3) Edit Instruction Verification: Annotators assess if the LLM-generated edit instructions are minimal, i.e., the suggested edit modifies only one aspect of the sentence (out of object, attribute, counting, or spatial relation), with an 84% acceptance rate. 4) Textual Edit Verification: Annotators assess if the edited sentence faithfully reflects the specified minimal edits without additional changes, with a 95% acceptance rate. Annotators also verify the LLM’s categorization of the types of edits (object, attribute, counting, or spatial relation). These steps ensure precise, minimal changes in images and captions, delivering a high-quality benchmark for fine-grained visual understanding. See Appendix A.4.1 for annotator instructions.

**ZH** 阶段 3：人工验证 为保证基准的高质量，在自动过滤之外，我们还通过 Amazon Mechanical Turk 平台开展人工验证。图像与描述需经过四步验证，每一步都要求五名标注者中至少四人达成一致方可通过。四步分别是：1) 自然度与图文匹配验证：标注者评估 (a) 图像是否看起来自然、(b) 描述是否通顺合理、(c) 图像是否与描述匹配。只有 26% 的合成图像通过这一步，主要卡在标准 (a)——计数与空间关系类图像往往显得不自然。各标准的详细接受率见附录表 7。2) 视觉编辑验证：标注者评估图像是否忠实反映了指定的最小改动、未引入额外变化，接受率为 80%。3) 编辑指令验证：标注者评估 LLM 生成的编辑指令是否为最小改动，即所建议的编辑只改动句子中的某一个方面（物体、属性、计数或空间关系之一），接受率为 84%。4) 文本编辑验证：标注者评估编辑后的句子是否忠实反映指定的最小改动、未引入额外变化，接受率为 95%。标注者还需核验 LLM 对改动类型（物体、属性、计数或空间关系）的分类。这些步骤确保图像与描述中的改动精确且最小，从而为细粒度视觉理解提供高质量基准。标注者说明见附录 A.4.1。

**EN** 4 Training and Benchmark sets

**ZH** 4 训练集与基准集

**EN** In our study, we create training and benchmark sets to improve and assess fine-grained understanding in VLMs. The training data is generated through a scalable pipeline with automatic filtering, while the benchmark data undergoes additional rigorous human verification to ensure high quality (as explained above). For object and attribute edit types, that make use of natural images, the training data is sourced from VSR (images sourced from COCO) and the COCO 2017 training split (118K images), while the benchmark data is sourced from the COCO 2017 validation split (5K images). This ensures benchmark images are unseen during training, maintaining evaluation reliability by community standards. The Training dataset has 64,392 samples (37,017 objects, 10,352 attributes, 10,050 counting, 6,973 relations), while the VisMin benchmark has 2,084 samples (579 objects, 294 attributes, 589 counting, 622 relations).

**ZH** 本研究中，我们构建了训练集与基准集，分别用于提升和评估 VLM 的细粒度理解。训练数据由可规模化的流程生成并经过自动过滤；基准数据则额外经过严格的人工验证以保证高质量（如上所述）。对于使用自然图像的物体与属性编辑类型，训练数据来自 VSR（图像源自 COCO）与 COCO 2017 训练划分（118K 张图像），基准数据来自 COCO 2017 验证划分（5K 张图像）。这保证了基准图像在训练时未被见过，按学界通行标准维持了评测的可靠性。训练集有 64,392 个样本（物体 37,017、属性 10,352、计数 10,050、关系 6,973），而 VisMin 基准有 2,084 个样本（物体 579、属性 294、计数 589、关系 622）。

<!-- [原子块 · object]  -->

**EN** Figure 3: VisMin categories and subcategories.

**ZH** 图 3：VisMin 的类别与子类别。

**EN** We aimed for a balanced benchmark across categories. However, the number of attribute samples in VisMin is relatively low because the LLM suggested attribute edits for only 2000 samples in the COCO 5K validation set. Moreover, most of these suggested edits were color edits. So we further downsampled the color edit instances to balance the distribution of the types of attribute edits. Figure 3 shows subcategories of the changes in VisMin . For detailed training set subcategories, see Appendix15. For qualitative samples, refer to Appendix 13 and 14.

**ZH** 我们力求基准在各类别间保持均衡。但 VisMin 中属性样本数量相对较少，因为 LLM 只对 COCO 5K 验证集中的 2000 个样本提出了属性编辑建议；而且这些建议大多是颜色编辑，因此我们又对颜色编辑实例做了下采样，以平衡各类属性编辑的分布。图 3 展示了 VisMin 中改动的各子类别。训练集子类别的细节见附录15，定性样本见附录 13 与 14。

**EN** In table 1, we compare VisMin with related benchmarks. Visual Minimal HN: This criterion evaluates if the visual hard negatives contain minimal changes. In Winoground and MMVP, hard negatives differ across multiple aspects (object, attribute, background, etc.). In contrast, VisMin’s hard negatives vary only in one aspect, keeping others unchanged as much as possible. This minimal-change property is also present in What’sUp, EQBEN, SPEC, and in a subset of images from ImageCoDe and CounterCurate. Visual Complexity: This criterion assesses the complexity of visual scenes. ImageCoDe and EQBEN mainly feature images from limited video domains and graphic engines, while What’sUp uses simple household and tabletop images. SPEC generates simplistic scenes using diffusion models. In contrast, Winoground uses expert-curated Getty Images, and MMVP uses ImageNet and LAIONAesthetics. VisMin and CounterCurate (concurrent work) stand out by using diverse, complex everyday scenes from COCO [22] and Flicker30K Entities [29], featuring common objects in natural contexts.

**ZH** 表 1 中我们把 VisMin 与相关基准做了对比。视觉最小改动难负例：该标准评估视觉难负例是否只包含最小改动。在 Winoground 与 MMVP 中，难负例在多个方面（物体、属性、背景等）同时存在差异；相比之下，VisMin 的难负例只在一个方面有变化，其他方面尽可能保持不变。What'sUp、EQBEN、SPEC 以及 ImageCoDe 与 CounterCurate 的部分图像也具备这一最小改动特性。视觉复杂度：该标准评估视觉场景的复杂程度。ImageCoDe 与 EQBEN 主要使用来自有限视频领域与图形引擎的图像，What'sUp 使用简单的家居与桌面图像，SPEC 用扩散模型生成简单场景。相比之下，Winoground 使用专家整理的 Getty Images，MMVP 使用 ImageNet 与 LAIONAesthetics。VisMin 与 CounterCurate（同期工作）则突出地使用了来自 COCO[22] 与 Flicker30K Entities[29] 的多样、复杂的日常场景，呈现自然语境中的常见物体。

**EN** Table 1: Comparison of benchmarks offering visual hard negatives (HN) across: minimal HN, visual complexity, textual complexity, human-approved captions ( ) and images ( ), and size. ✓ – : criterion holds for a subset of the benchmark.

**ZH** 表 1：提供视觉难负例（HN）的各基准在以下维度的对比：最小改动难负例、视觉复杂度、文本复杂度、人工审核的描述与图像，以及规模。✓ –：该标准只在基准的一个子集上成立。

**EN** Benchmark ImageCoDe [14] ✓ – Limited video domains, Open Images Free-form (Human) ✓ ✓ 2,306 What’sUp (A/B) [11] ✓ Household, Tabletop Template ✓ ✓ 1,232 Winoground [36] × Expert curated using Getty Images API Free-form (Human) ✓ ✓ 400 EQBEN [38] ✓ Limited video domains, Graphic engine, Synthetic-diffusion Free-form (Human), Template × ✓ – 250,612 SPEC [28] ✓ Synthetic-diffusion (limited objects) Template × × 3,000 MMVP [37] × ImageNet, LAIONAesthetics Free-form (Human) ✓ ✓ 150 CounterCurate [45] ✓ – Flicker30K Entities, Synthetic-diffusion Free-form(Human, LLM), Template ✓ – ✓ – 45,400 VisMin (Ours) ✓ COCO, Synthetic-diffusion Free-form (Human, LLM) ✓ ✓ 2,084

**ZH** 基准 ImageCoDe[14] ✓ – 有限的视频领域、Open Images 自由形式（人工）✓ ✓ 2,306 What'sUp (A/B)[11] ✓ 家居、桌面 模板 ✓ ✓ 1,232 Winoground[36] × 使用 Getty Images API 由专家整理 自由形式（人工）✓ ✓ 400 EQBEN[38] ✓ 有限的视频领域、图形引擎、合成扩散 自由形式（人工）、模板 × ✓ – 250,612 SPEC[28] ✓ 合成扩散（物体有限）模板 × × 3,000 MMVP[37] × ImageNet、LAIONAesthetics 自由形式（人工）✓ ✓ 150 CounterCurate[45] ✓ – Flicker30K Entities、合成扩散 自由形式（人工、LLM）、模板 ✓ – ✓ – 45,400 VisMin（ ours）✓ COCO、合成扩散 自由形式（人工、LLM）✓ ✓ 2,084

**EN** Textual Complexity: Benchmarks like ImageCoDe, Winoground, and MMVP use free-form human-written captions. In contrast, What’sUp (focused on spatial changes) and SPEC (focused on controlled changes) use template-based captions, which often lack diversity. EQBEN and CounterCurate mix free-form (human or LLM-generated) and template-based captions. VisMin combines human-written and LLM-generated free-form captions, , yielding sufficient textual complexity to the benchmark. Human Verification: For benchmarks using synthetic images like EQBEN, SPEC, CounterCurate, and VisMin, human evaluation is essential to ensure images look natural. It’s also crucial for benchmarks with automatically generated hard negative captions, as these may be nonsensical unless well-defined templates like What’sUp are used. Nonsensical captions make it easier for VLMs to identify them as incorrect [8]. VisMin is notably the only benchmark with full human verification, ensuring both captions and images are high quality. CounterCurate also conducts human verification but only checks for image-caption consistency (on 300 examples), without verifying image naturalness or caption sensibility. Size: This criterion assesses the dataset’s size. VisMin excels by combining controlled minimal changes with complex, natural scenes and captions, providing an optimal balance for robust evaluation.

**ZH** 文本复杂度：ImageCoDe、Winoground 与 MMVP 等基准使用人工撰写的自由形式描述；相比之下，What'sUp（聚焦空间变化）与 SPEC（聚焦受控变化）使用模板化描述，多样性往往不足。EQBEN 与 CounterCurate 混合使用自由形式（人工或 LLM 生成）与模板化描述。VisMin 结合人工撰写与 LLM 生成的自由形式描述，为基准提供了足够的文本复杂度。人工验证：对于 EQBEN、SPEC、CounterCurate 与 VisMin 这类使用合成图像的基准，人工评估对确保图像自然度至关重要；对于难负例描述自动生成的基准同样关键，因为除非像 What'sUp 那样使用定义良好的模板，这些描述可能不通顺。而不通顺的描述会让 VLM 更容易识别其为错误[8]。VisMin 是唯一经过完整人工验证的基准，确保描述与图像都具备高质量。CounterCurate 也做了人工验证，但只检查图文一致性（在 300 个样本上），并未验证图像自然度或描述合理性。规模：该标准评估数据集大小。VisMin 把受控的最小改动与复杂自然的场景、描述相结合，为稳健评测提供了最佳平衡。

**EN** 5 Benchmarking VLMs on VisMin Benchmark

**ZH** 5 在 VisMin 基准上评测 VLM

**EN** Setup

**ZH** 设置

**EN** We have comprehensively benchmarked existing state-of-the-art VLMs on VisMin, encompassing both foundational VLMs–such as CLIP [31], SigLip [44], BLIP [18], and Coca [40] and generative MLLMs including Llava [24], Idefics2 [15] and InternVL1.5 [2]. Additionally, closed-source MLLMs such as GPT4-o [1] and Gemini1.0 Pro [35] are also evaluated.

**ZH** 我们在 VisMin 上全面评测了现有最优的 VLM，涵盖 CLIP[31]、SigLip[44]、BLIP[18]、Coca[40] 等基座型 VLM，以及 Llava[24]、Idefics2[15]、InternVL1.5[2] 等生成式 MLLM；此外还评估了 GPT4-o[1] 与 Gemini1.0 Pro[35] 等闭源 MLLM。

**EN** For foundational models like CLIP, we conducted an image-text matching task using cosine similarity, following [36]. The tasks involved two settings: choosing the correct image from two captions and selecting the correct caption from two images. In VisMin examples (see Fig. 1) with pairs ⟦SLOT_7⟧, the text score is 1 if ⟦SLOT_8⟧, and the image score is 1 if ⟦SLOT_9⟧; the group score is 1 when both scores are 1. For MLLMs, we adapted these tasks to a visual question answering format with binary questions about the matching relationship between images and captions ⟦SLOT_10⟧. To calculate the text score, we presented the model with one image and two captions, using the prompt “Does this image depict: {⟦SLOT_11⟧ or ⟦SLOT_12⟧}?”.22 2 For single-image models, such as Llava, we combine the two images vertically with a clear border. To calculate the image score, we presented the model with two images and one caption, using the prompt “Which image better aligns with the description: ‘{C}’? The first or the second image?”. The score is 1 if the predicted answer matches the ground truth. Once both scores are obtained, the group score is 1 if both individual scores are 1.

**ZH** 对于 CLIP 等基座型模型，我们沿用[36] 的做法，用余弦相似度执行图文匹配任务。任务包含两种设置：从两条描述中选出正确的图像，以及从两张图像中选出正确的描述。在 VisMin 样本（见图 1）中，给定配对 ⟦SLOT_7⟧，若 ⟦SLOT_8⟧ 则文本分数为 1，若 ⟦SLOT_9⟧ 则图像分数为 1；两项分数都为 1 时，分组分数为 1。对于 MLLM，我们把这些任务改造为视觉问答形式，就图像与描述之间的匹配关系 ⟦SLOT_10⟧ 提出二值问题。计算文本分数时，我们向模型呈现一张图像与两条描述，使用提示「Does this image depict: {⟦SLOT_11⟧ or ⟦SLOT_12⟧}?」。22 2 对于 Llava 等单图模型，我们把两张图像上下拼接并加上清晰的边界。计算图像分数时，我们向模型呈现两张图像与一条描述，使用提示「Which image better aligns with the description: '{C}'? The first or the second image?」。若预测答案与真值一致则得 1 分。两项分数都得到后，若两者均为 1，则分组分数为 1。

**EN** Table 2: Performance of foundational variants and MLLMs across categories on the VisMin Dataset. Columns ‘I,’ ‘T,’ and ‘G’ denote Image, Text, and Group scores from Winoground [36]. AVG denotes the average across columns. The best results are highlighted in bold.

**ZH** 表 2：基座型模型变体与 MLLM 在 VisMin 数据集各类别上的表现。列「I」「T」「G」分别表示来自 Winoground[36] 的图像、文本与分组分数。AVG 表示各列的平均值。最优结果以粗体标出。

**EN** Object Attribute S. Relation Count AVG T I G T I G T I G T I G Random Chance 25 25 16.67 25 25 16.67 25 25 16.67 25 25 16.67 22.22 MTurk Human 86.87 95.50 83.07 82.31 91.15 76.87 81.67 92.76 76.20 88.96 96.77 86.41 86.54 CLIP (ViT-B/32) [31] 79.62 77.89 67.53 72.11 65.99 55.1 8.2 4.34 0.48 31.24 20.71 10.53 41.15 CLIP (ViT-B/16) 86.53 79.1 71.68 70.75 65.31 52.38 8.84 3.22 0.8 34.3 22.58 13.58 42.42 CLIP (ViT-L/14) 87.56 83.59 78.07 74.49 69.73 57.82 9.16 4.66 1.45 37.01 30.56 18.17 46.42 NegCLIP [42] 87.74 87.05 80.66 81.63 80.27 71.77 10.13 4.66 1.13 55.01 57.72 42.28 48.96 SigLip (ViT-B/16)[44] 90.5 88.95 83.25 86.05 79.25 73.13 11.58 6.43 1.77 60.95 47.03 38.37 55.61 SigLip (ViT-L/16) 93.44 88.43 84.46 84.35 78.23 68.37 10.29 4.82 1.29 61.8 57.05 44.14 56.39 Flava [32] 81.69 75.12 66.66 74.49 60.54 52.04 6.75 5.79 0.96 35.99 27.5 15.45 41.91 BLIP [18] 92.4 92.57 87.05 88.44 86.73 78.57 11.25 4.98 2.09 52.97 46.01 33.28 56.36 Coca [40] 84.97 81.52 73.58 78.57 66.33 57.82 11.25 5.95 1.77 60.1 35.82 28.52 48.85 LlaVa1.6 (7B) [24] 93.0 32.8 32.2 92.2 34.4 33.3 91.8 7.8 7.4 73.6 25.0 20.2 38.28 Idefics2 (8B) [15] 95.4 69.4 67.6 89.1 71.4 67.0 18.6 18.8 4.8 72.2 50.6 47.0 55.99 CogVLM (7B) [39] 94.64 89.63 87.56 89.11 88.43 81.63 21.70 11.09 2.25 58.40 6.45 3.56 52.87 InternVL1.5 (25B) [2] 94.65 40.24 39.72 91.16 42.86 41.16 74.28 14.79 11.74 73.51 31.58 27.5 48.60 Gemini1.0 Pro 94.99 79.97 78.76 91.84 74.83 72.45 52.57 15.43 9.81 67.74 44.14 37.52 49.63 GPT4-o 95.51 96.2 93.44 92.18 90.48 87.07 89.07 50.48 46.78 77.42 78.27 68.42 73.93

**ZH** 物体 属性 空间关系 计数 平均 T I G T I G T I G T I G 随机猜测 25 25 16.67 25 25 16.67 25 25 16.67 25 25 16.67 22.22 MTurk 人类 86.87 95.50 83.07 82.31 91.15 76.87 81.67 92.76 76.20 88.96 96.77 86.41 86.54 CLIP (ViT-B/32) [31] 79.62 77.89 67.53 72.11 65.99 55.1 8.2 4.34 0.48 31.24 20.71 10.53 41.15 CLIP (ViT-B/16) 86.53 79.1 71.68 70.75 65.31 52.38 8.84 3.22 0.8 34.3 22.58 13.58 42.42 CLIP (ViT-L/14) 87.56 83.59 78.07 74.49 69.73 57.82 9.16 4.66 1.45 37.01 30.56 18.17 46.42 NegCLIP [42] 87.74 87.05 80.66 81.63 80.27 71.77 10.13 4.66 1.13 55.01 57.72 42.28 48.96 SigLip (ViT-B/16)[44] 90.5 88.95 83.25 86.05 79.25 73.13 11.58 6.43 1.77 60.95 47.03 38.37 55.61 SigLip (ViT-L/16) 93.44 88.43 84.46 84.35 78.23 68.37 10.29 4.82 1.29 61.8 57.05 44.14 56.39 Flava [32] 81.69 75.12 66.66 74.49 60.54 52.04 6.75 5.79 0.96 35.99 27.5 15.45 41.91 BLIP [18] 92.4 92.57 87.05 88.44 86.73 78.57 11.25 4.98 2.09 52.97 46.01 33.28 56.36 Coca [40] 84.97 81.52 73.58 78.57 66.33 57.82 11.25 5.95 1.77 60.1 35.82 28.52 48.85 LlaVa1.6 (7B) [24] 93.0 32.8 32.2 92.2 34.4 33.3 91.8 7.8 7.4 73.6 25.0 20.2 38.28 Idefics2 (8B) [15] 95.4 69.4 67.6 89.1 71.4 67.0 18.6 18.8 4.8 72.2 50.6 47.0 55.99 CogVLM (7B) [39] 94.64 89.63 87.56 89.11 88.43 81.63 21.70 11.09 2.25 58.40 6.45 3.56 52.87 InternVL1.5 (25B) [2] 94.65 40.24 39.72 91.16 42.86 41.16 74.28 14.79 11.74 73.51 31.58 27.5 48.60 Gemini1.0 Pro 94.99 79.97 78.76 91.84 74.83 72.45 52.57 15.43 9.81 67.74 44.14 37.52 49.63 GPT4-o 95.51 96.2 93.44 92.18 90.48 87.07 89.07 50.48 46.78 77.42 78.27 68.42 73.93

**EN** Results

**ZH** 结果

**EN** Insights from Table 2 highlight key capabilities and limitations of current models. Text scores generally surpass image scores, especially in MLLMs, where text scores are often two to three times higher. In contrast, foundational VLMs show a modest discrepancy between image and text scores. We hypothesize that for MLLMs, the image score is lower compared to the text score because they lack training with multiple images, and simple vertical concatenation does not provide sufficient visual signals, leading to suboptimal alignment with captions. Notably, Idefics2, which supports multi-image processing, performs similarly on text and image scores, underscoring the importance of multi-image data during pretraining. Foundational VLMs’ higher text scores suggest that distinguishing between captions is easier than between images, highlighting the need for our visual minimal change benchmark. Interestingly, foundational VLMs generally outperform MLLMs due to the latter’s lower image scores.

**ZH** 表 2 揭示了当前模型的关键能力与局限。文本分数普遍高于图像分数，在 MLLM 上尤为明显，其文本分数常常是图像分数的两到三倍；相比之下，基座型 VLM 的图像与文本分数差距不大。我们推测，MLLM 的图像分数低于文本分数，是因为它们缺乏多图训练，而简单的纵向拼接又无法提供足够的视觉信号，导致与描述的对齐不佳。值得注意的是，支持多图处理的 Idefics2 在文本与图像分数上表现接近，凸显了预训练阶段多图数据的重要性。基座型 VLM 的文本分数更高，说明区分描述比区分图像更容易，这也凸显了我们这个视觉最小改动基准的必要性。有趣的是，基座型 VLM 总体上优于 MLLM，原因正在于后者的图像分数偏低。

**EN** All models perform well on Object and Attribute splits, indicating that understanding semantic changes correlates strongly with recognition capabilities. Models excelling in image classification tend to perform better, reflecting a foundational understanding that does not require advanced reasoning. For instance, Idefics2, using the SigLip (ViT-L/16) vision encoder, performs worse with strong LLMs compared to its foundational VLM counterpart, likely due to limited multi-image understanding in MLLMs. Notably, CogVLM shows superior performance over other MLLMs in understanding object and attribute changes. This advantage likely stems from its integration of grounding tasks and high-quality human-annotated datasets like Flickr30K Entities [29], RefCOCO [12], and VisualGenome [13] in its pretraining. On the other hand, the Spatial Relation split relies heavily on reasoning capabilities, with MLLMs outperforming foundational models. This suggests that LLMs can parse object relationships through reasoning. However, existing VLMs struggle with spatial relations, often scoring below random chance, indicating potential biases in models and highlighting an area for further research.

**ZH** 所有模型在物体与属性子集上表现都不错，说明理解语义变化与识别能力高度相关：图像分类能力强的模型往往表现更好，反映的是一种不需要高级推理的基础理解。例如以 SigLip（ViT-L/16）为视觉编码器的 Idefics2，在搭配强大 LLM 时反而不如对应的基座型 VLM，很可能受限于 MLLM 的多图理解能力。值得注意的是，CogVLM 在理解物体与属性变化上优于其他 MLLM，这一优势可能来自它在预训练中整合了定位任务以及 Flickr30K Entities[29]、RefCOCO[12]、VisualGenome[13] 等高质量人工标注数据集。另一方面，空间关系子集高度依赖推理能力，MLLM 在此优于基座型模型，说明 LLM 能够通过推理解析物体间的关系。然而现有 VLM 在空间关系上仍很吃力，常常低于随机猜测水平，说明模型可能存在偏差，也指出了一个值得进一步研究的方向。

**EN** We document human baseline performance on our benchmark via Amazon Mechanical Turk (see Appendix A.4.2). Humans generally outperform models on image scores, except in the attribute category where GPT4-o excels. Models typically surpass humans in text scores, especially with attributes and objects. However, in spatial relations and counting, humans significantly outperform models in group scores, highlighting areas for model improvement and the robustness of human scene comprehension.

**ZH** 我们通过 Amazon Mechanical Turk 记录了人类在本基准上的基线表现（见附录 A.4.2）。人类在图像分数上普遍优于模型，只有属性类别例外——GPT4-o 在该类别上表现突出。模型在文本分数上通常超过人类，尤其是在属性与物体类别。但在空间关系与计数上，人类的分组分数显著高于模型，凸显了模型有待改进之处，也体现了人类场景理解的稳健性。

**EN** 6 Enhancing fine-grained understanding in VLMs

**ZH** 6 增强 VLM 的细粒度理解

**EN** We use a synthetic minimal-change dataset to enhance fine-grained understanding through additional fine-tuning of VLMs. Training with pairs of images and captions with minimal differences provides a richer training signal, improving model performance in fine-grained understanding tasks. We demonstrate improvements on top of both foundational VLMs and MLLMs by conducting extensive evaluations across various benchmarks: (1) Single image benchmarks test the alignment between single images and multiple captions: VSR [23], CountBench [26], VALSE [27], SPEC [28], and Sugarcrepe [8]. (2) Multiple image benchmarks test the alignment between multiple images and captions: ImageCode [14], MMVP [37], Whatsup [11], Winoground [36], EQBEN [38], and our VisMin benchmark.

**ZH** 我们用一个合成的最小改动数据集，通过对 VLM 做额外微调来增强其细粒度理解。用差异极小的图像对与描述对训练，能提供更丰富的训练信号，从而提升模型在细粒度理解任务上的表现。我们在多个基准上做了大量评估，展示了在基座型 VLM 与 MLLM 两类模型之上的改进：(1) 单图基准检验单张图像与多条描述之间的对齐：VSR[23]、CountBench[26]、VALSE[27]、SPEC[28] 与 Sugarcrepe[8]。(2) 多图基准检验多张图像与描述之间的对齐：ImageCode[14]、MMVP[37]、Whatsup[11]、Winoground[36]、EQBEN[38] 以及我们的 VisMin 基准。

**EN** 6.1 Fine-tuning Foundational VLMs

**ZH** 6.1 微调基座型 VLM

**EN** Enhancement with Minimal-Change Data

**ZH** 用最小改动数据增强

**EN** Our approach uses a synthetic minimal-change dataset to improve visual representation without altering the training methodology. We construct training batches with both source and edited image-text pairs: In the original CLIP training, a mini-batch is ⟦SLOT_13⟧, with pairs randomly sampled from the dataset as random negatives. With minimal-change data, we add edited image-text pairs as hard negatives, resulting in ⟦SLOT_14⟧, where ⟦SLOT_15⟧ is the edited pair of ⟦SLOT_16⟧. We use a total batch size of 128 with ⟦SLOT_17⟧ A100 GPUs and retain other training protocols and hyperparameters as default from OpenCLIP [3], including a learning rate of ⟦SLOT_18⟧, weight decay of ⟦SLOT_19⟧, Adam ⟦SLOT_20⟧ of ⟦SLOT_21⟧, ⟦SLOT_22⟧ of ⟦SLOT_23⟧, an eps of ⟦SLOT_24⟧, and a cosine scheduler. The training runs for ⟦SLOT_25⟧ epochs, and we select checkpoints based on a separate VisMin validation set.

**ZH** 我们的方法用合成的最小改动数据集改进视觉表示，而不改变训练方式。我们把源图文对与编辑后图文对一起构建训练批次：在原始 CLIP 训练中，一个小批次为 ⟦SLOT_13⟧，其中配对从数据集中随机采样，彼此互为随机负例；引入最小改动数据后，我们把编辑后的图文对作为难负例加入，形成 ⟦SLOT_14⟧，其中 ⟦SLOT_15⟧ 是 ⟦SLOT_16⟧ 的编辑后配对。我们使用 ⟦SLOT_17⟧ 张 A100 GPU、总批大小 128，并沿用 OpenCLIP[3] 的默认训练协议与超参数，包括学习率 ⟦SLOT_18⟧、权重衰减 ⟦SLOT_19⟧、Adam ⟦SLOT_20⟧ 为 ⟦SLOT_21⟧、⟦SLOT_22⟧ 为 ⟦SLOT_23⟧、eps 为 ⟦SLOT_24⟧，以及余弦调度器。训练运行 ⟦SLOT_25⟧ 个轮次，我们依据独立的 VisMin 验证集选择检查点。

**EN** We fine-tuned pre-trained CLIP on our minimal-change data, calling it VisMin-CLIP. For comparison, we implemented three models using the same pre-trained CLIP: NegCLIP [42], CounterCurate-CLIP [45], and SPEC-CLIP [28]. In NegCLIP, we fine-tuned CLIP with automatically generated hard-negative captions and nearest-neighbor images paired with human-written captions. For CounterCurate-CLIP, we used hard-negative data (attribute, position, counting) but trained one model on all three types, unlike the original approach of training separate models. SPEC-CLIP was fine-tuned on six combined category-specific splits (size, spatial, existence, count). Hard-negatives were included in all batch constructions, with excess negatives rolled into the next batch if needed. All models used ViT-L/14 as the backbone and the original CLIP loss, initialized from OpenAI checkpoints. Best checkpoints were selected from validation sets for NegCLIP and CounterCurate-CLIP, and from average benchmark performance for SPEC-CLIP. This controlled comparison evaluates the impact of different hard-negative data approaches on improving CLIP’s fine-grained understanding.

**ZH** 我们在最小改动数据上微调预训练 CLIP，称之为 VisMin-CLIP。为作对比，我们用同一个预训练 CLIP 复现了三个模型：NegCLIP[42]、CounterCurate-CLIP[45] 与 SPEC-CLIP[28]。NegCLIP 中，我们用自动生成的难负例描述以及与人工撰写描述配对的最近邻图像微调 CLIP。CounterCurate-CLIP 使用难负例数据（属性、位置、计数），但我们把三类数据合在一起训练一个模型，而不像原方法那样分别训练三个模型。SPEC-CLIP 则在六个类别专属划分（尺寸、空间、存在性、计数）的组合上微调。所有批次构建都包含难负例，多余的负例按需顺延到下一批次。所有模型都以 ViT-L/14 为骨干网络，沿用原始 CLIP 损失，并从 OpenAI 检查点初始化。NegCLIP 与 CounterCurate-CLIP 从各自验证集选出最佳检查点，SPEC-CLIP 则按基准平均表现选取。这一受控对比评估了不同难负例数据方案对提升 CLIP 细粒度理解的作用。

**EN** Table 3: Performance of fine-tuned CLIP and Idefics2 across categories on the VisMin Dataset. The † symbol indicates the reproduced model checkpoints based on their respective training data.

**ZH** 表 3：微调后的 CLIP 与 Idefics2 在 VisMin 数据集各类别上的表现。† 符号表示基于各自训练数据复现出的模型检查点。

**EN** Object Attribute S. Relation Count AVG T I G T I G T I G T I G CLIP(ViT-L/14) 87.56 83.59 78.07 74.49 69.73 57.82 9.16 4.66 1.45 37.01 30.56 18.17 46.02 NegCLIP† 87.74 87.05 80.66 81.63 80.27 71.77 10.13 4.66 1.13 55.01 57.72 42.28 55.00 CounterCurate-CLIP† 89.81 91.02 84.46 82.99 80.27 72.79 20.1 11.41 7.4 49.24 45.16 31.92 55.54 SPEC-CLIP† 86.53 86.01 78.58 78.57 71.77 63.95 9.16 5.31 1.13 45.5 47.71 32.43 50.55 VisMin-CLIP 91.54 91.19 86.36 85.03 83.67 75.85 11.9 3.38 1.29 82.34 79.97 72.33 63.74 Idefics2 95.4 69.4 67.6 89.1 71.4 67.0 18.6 18.8 4.8 72.2 50.6 47.0 55.99 VisMin-Idefics2 96.5 95.7 93.3 91.2 91.8 86.7 83.0 76.0 69.3 85.4 87.8 80.5 86.43

**ZH** 物体 属性 空间关系 计数 平均 T I G T I G T I G T I G CLIP(ViT-L/14) 87.56 83.59 78.07 74.49 69.73 57.82 9.16 4.66 1.45 37.01 30.56 18.17 46.02 NegCLIP† 87.74 87.05 80.66 81.63 80.27 71.77 10.13 4.66 1.13 55.01 57.72 42.28 55.00 CounterCurate-CLIP† 89.81 91.02 84.46 82.99 80.27 72.79 20.1 11.41 7.4 49.24 45.16 31.92 55.54 SPEC-CLIP† 86.53 86.01 78.58 78.57 71.77 63.95 9.16 5.31 1.13 45.5 47.71 32.43 50.55 VisMin-CLIP 91.54 91.19 86.36 85.03 83.67 75.85 11.9 3.38 1.29 82.34 79.97 72.33 63.74 Idefics2 95.4 69.4 67.6 89.1 71.4 67.0 18.6 18.8 4.8 72.2 50.6 47.0 55.99 VisMin-Idefics2 96.5 95.7 93.3 91.2 91.8 86.7 83.0 76.0 69.3 85.4 87.8 80.5 86.43

**EN** Results We evaluated these models on the VisMin benchmark (results in Table 3). Fine-tuning with minimal-change data significantly improves CLIP’s performance on the Object, Attribute, and Count categories, demonstrating the usefulness of our minimal-change data in enhancing the fine-grained understanding of foundational VLMs such as CLIP. VisMin-CLIP consistently outperforms NegCLIP, CounterCurate-CLIP and SPEC-CLIP across all categories except spatial relations. This suggests that the visual minimal-change data is more helpful in improving the fine-grained understanding capabilities of the CLIP model compared to the nearest neighbor images in NegCLIP and not fully minimally-changed CounterCurate and SPEC data. W

**ZH** 结果 我们在 VisMin 基准上评估了这些模型（结果见表 3）。用最小改动数据微调显著提升了 CLIP 在物体、属性与计数类别上的表现，说明我们的最小改动数据确实有助于增强 CLIP 等基座型 VLM 的细粒度理解。除空间关系外，VisMin-CLIP 在所有类别上都一致优于 NegCLIP、CounterCurate-CLIP 与 SPEC-CLIP。这说明，相比 NegCLIP 中的最近邻图像，以及改动并不彻底最小的 CounterCurate 与 SPEC 数据，视觉最小改动数据更能有效提升 CLIP 模型的细粒度理解能力。W

**EN** Table 4: Evaluation on other single and mult-image visual fine-grained understanding benchmarks. All models adopt ViT-L-14 as the vision encoder. CB refers CountBench, SG refers to Sugarcrepe, IC refers to Imagecode. I2T and T2I indicate standard standard image-to-text and text-to-image retrieval metrics. Best-performing models in the CLIP-family are highlighted in blue, and best-performing MLLM models are highlighted in green.

**ZH** 表 4：在其他单图与多图视觉细粒度理解基准上的评测。所有模型均采用 ViT-L-14 作为视觉编码器。CB 指 CountBench，SG 指 Sugarcrepe，IC 指 Imagecode。I2T 与 T2I 表示标准的图到文与文到图检索指标。CLIP 系列中表现最好的模型以蓝色标出，MLLM 中表现最好的以绿色标出。

**EN** #Samples Single-Image Multi-Image VSR CB VALSE SG Whatsup SPEC IC MMVP Winoground EQBEN VisMin I2T T2I T I G T I G T I G CLIP (ViT-L/14) - 58.33 33.65 69.1 73.0 37.7 32.85 30.86 61.47 19.26 27.5 11.0 8.5 35.71 33.57 21.43 52.05 47.13 38.88 NegCLIP† 118K 56.56 40.0 75.41 85.73 41.2 37.73 35.45 67.33 29.63 25.25 12.0 7.0 42.86 40.0 30.0 58.63 57.42 48.96 CounterCurate-CLIP† 241k 56.74 30.79 68.47 83.66 44.29 37.99 35.24 65.81 25.19 28.0 13.25 9.0 45.0 33.57 28.57 60.88 56.68 49.1 SPEC-CLIP† 637k 64.54 32.06 68.75 79.34 43.35 87.04 88.08 66.25 30.37 22.5 7.75 4.75 41.43 40.0 30.71 54.94 52.7 44.02 VisMin-CLIP 65k 58.69 49.84 72.24 81.44 43.99 44.28 39.98 66.81 32.59 32.75 14.75 9.75 54.29 40.71 33.57 67.7 64.55 58.96 Idefics2 - 77.3 91.11 88.91 90.45 68.04 74.37 60.5 64.4 48.15 47.25 33.75 22.5 62.88 33.33 25.76 68.83 52.56 46.6 Vismin-Idefics2 - 80.32 93.97 86.08 91.14 74.42 76.2 76.58 70.7 48.89 47.0 35.75 22.5 64.39 54.55 49.24 89.01 87.83 82.44

**ZH** #样本 单图 多图 VSR CB VALSE SG Whatsup SPEC IC MMVP Winoground EQBEN VisMin I2T T2I T I G T I G T I G CLIP (ViT-L/14) - 58.33 33.65 69.1 73.0 37.7 32.85 30.86 61.47 19.26 27.5 11.0 8.5 35.71 33.57 21.43 52.05 47.13 38.88 NegCLIP† 118K 56.56 40.0 75.41 85.73 41.2 37.73 35.45 67.33 29.63 25.25 12.0 7.0 42.86 40.0 30.0 58.63 57.42 48.96 CounterCurate-CLIP† 241k 56.74 30.79 68.47 83.66 44.29 37.99 35.24 65.81 25.19 28.0 13.25 9.0 45.0 33.57 28.57 60.88 56.68 49.1 SPEC-CLIP† 637k 64.54 32.06 68.75 79.34 43.35 87.04 88.08 66.25 30.37 22.5 7.75 4.75 41.43 40.0 30.71 54.94 52.7 44.02 VisMin-CLIP 65k 58.69 49.84 72.24 81.44 43.99 44.28 39.98 66.81 32.59 32.75 14.75 9.75 54.29 40.71 33.57 67.7 64.55 58.96 Idefics2 - 77.3 91.11 88.91 90.45 68.04 74.37 60.5 64.4 48.15 47.25 33.75 22.5 62.88 33.33 25.76 68.83 52.56 46.6 Vismin-Idefics2 - 80.32 93.97 86.08 91.14 74.42 76.2 76.58 70.7 48.89 47.0 35.75 22.5 64.39 54.55 49.24 89.01 87.83 82.44

**EN** We further conduct a zero-shot evaluation of the fine-tuned CLIP models on other fine-grained understanding benchmarks (beyond our VisMin benchmark) to test their generalization capabilities (see Table 4). VisMin-CLIP performs best in ⟦SLOT_26⟧ out of 18 tasks, while NegCLIP, CounterCurate-CLIP, and SPEC-CLIP lead in ⟦SLOT_27⟧, ⟦SLOT_28⟧, and ⟦SLOT_29⟧ tasks, respectively. All models outperform the pre-trained CLIP model across benchmarks. For counting and spatial reasoning tasks, VisMin training data shows significant improvements. On CountBench, we observed ⟦SLOT_30⟧, ⟦SLOT_31⟧, and ⟦SLOT_32⟧ gains over NegCLIP, CounterCurate-CLIP, and SPEC-CLIP, respectively. Similarly, on spatial reasoning benchmarks (SPEC, Whatsup, VSR), VisMin-CLIP showed an average ⟦SLOT_33⟧ improvement over NegCLIP and ⟦SLOT_34⟧ over CounterCurate-CLIP. While SPEC-CLIP performed best on the in-distribution SPEC benchmark, VisMin-CLIP still outperformed other models, indicating its effectiveness in improving fine-grained understanding. For VALSE and SugarCrepe, NegCLIP performed best, likely due to similarities in the textual hard-negative generation process used in those benchmarks and NegCLIP’s fine-tuning data.

**ZH** 我们进一步在其他细粒度理解基准（除 VisMin 之外）上对微调后的 CLIP 做零样本评估，以检验其泛化能力（见表 4）。VisMin-CLIP 在 18 项任务中有 ⟦SLOT_26⟧ 项表现最好，NegCLIP、CounterCurate-CLIP 与 SPEC-CLIP 分别在 ⟦SLOT_27⟧、⟦SLOT_28⟧ 与 ⟦SLOT_29⟧ 项任务上领先。所有模型在各基准上都优于预训练 CLIP。在计数与空间推理任务上，VisMin 训练数据带来了显著提升：在 CountBench 上，我们观察到相对 NegCLIP、CounterCurate-CLIP 与 SPEC-CLIP 分别有 ⟦SLOT_30⟧、⟦SLOT_31⟧ 与 ⟦SLOT_32⟧ 的增益；同样，在空间推理基准（SPEC、Whatsup、VSR）上，VisMin-CLIP 相对 NegCLIP 平均提升 ⟦SLOT_33⟧，相对 CounterCurate-CLIP 提升 ⟦SLOT_34⟧。虽然 SPEC-CLIP 在同分布的 SPEC 基准上表现最佳，VisMin-CLIP 仍优于其他模型，说明它在提升细粒度理解上确有成效。至于 VALSE 与 SugarCrepe，NegCLIP 表现最好，可能是因为这些基准所用的文本难负例生成过程与 NegCLIP 的微调数据较为相似。

**EN** Furthermore, our minimal-change data significantly outperforms others in multi-image understanding benchmarks. Fine-tuning on this data enhances the model’s ability to distinguish between similar images, showing improvements on challenging benchmarks like Winoground, MMVP, and EQBEN, which test compositional reasoning and fine-grained understanding. VisMin-CLIP improved Text scores by ⟦SLOT_35⟧ on Winoground and ⟦SLOT_36⟧ on EQBEN over baseline CLIP, demonstrating effective alignment of visual and textual feature spaces. VisMin-CLIP also outperforms other models on most tasks and achieves comparable results on remaining benchmarks (except SPEC), despite using fewer samples (e.g., ⟦SLOT_37⟧ in VisMin vs. ⟦SLOT_38⟧ in SPEC).

**ZH** 此外，我们的最小改动数据在多图理解基准上显著优于其他数据。在其上微调增强了模型区分相似图像的能力，在 Winoground、MMVP、EQBEN 等考察组合推理与细粒度理解的高难度基准上均有提升。相对基线 CLIP，VisMin-CLIP 在 Winoground 上把文本分数提升了 ⟦SLOT_35⟧，在 EQBEN 上提升了 ⟦SLOT_36⟧，说明视觉与文本特征空间得到了有效对齐。尽管使用的样本更少（例如 VisMin 为 ⟦SLOT_37⟧，而 SPEC 为 ⟦SLOT_38⟧），VisMin-CLIP 在多数任务上仍优于其他模型，并在其余基准（除 SPEC 外）上取得可比的结果。

**EN** Figure 4: VisMin fine-tuned models show greater improvements with larger models. The circle radius reflects the number of model parameters.

**ZH** 图 4：VisMin 微调模型在更大的模型上展现出更大的提升。圆圈半径反映模型参数量。

<!-- [原子块 · object]  -->

**EN** Figure 5: (left) Recall results with ViT-L/14 on COCO benchmark (right) standard benchmark results on Idefics2.

**ZH** 图 5：（左）在 COCO 基准上以 ViT-L/14 得到的召回结果；（右）在 Idefics2 上的标准基准结果。

<!-- [原子块 · object]  -->

**EN** Additional Findings

**ZH** 补充发现

**EN** Further experiments reveal several key findings: (1) Scalability: As illustrated in fig. 5, we evaluated varying sizes of OpenAI’s CLIP models– B/32 and L/16. Larger models demonstrated improved performance across both single-image and multi-image benchmarks after training on our synthetic data. This improvement is likely because understanding minimal changes is a complex task, demanding robust model capabilities. For instance, the smallest tested model, ViT-B/32 (149.62M parameters), exhibited improvements of ⟦SLOT_39⟧ and ⟦SLOT_40⟧ in single and multiple image benchmarks, respectively, when comparing VisMin-CLIP against the baseline CLIP. When the model’s capacity was expanded to ViT-L/14 (427.62M parameters), the improvements increased to ⟦SLOT_41⟧ and ⟦SLOT_42⟧, respectively. These results highlight the scalability and efficacy of our data in enhancing model performance. (2) Enhanced Original Capabilities: In addition to improvements in fine-grained understanding tasks, training on our data also enhances performance in standard retrieval tasks, as shown in fig. 5. This suggests that models achieve better alignment from training on minimal change tasks, indicating that our data is generally applicable across various cross-modal tasks.

**ZH** 进一步的实验揭示了若干关键发现：(1) 可扩展性：如图 5 所示，我们评估了 OpenAI CLIP 的不同规模模型——B/32 与 L/16。在合成数据上训练后，更大的模型在单图与多图基准上都表现出更好的性能。这很可能是因为理解最小改动本身是一项复杂任务，需要模型具备较强的能力。例如，在参与测试的最小模型 ViT-B/32（149.62M 参数）上，VisMin-CLIP 相对基线 CLIP 在单图与多图基准上分别提升 ⟦SLOT_39⟧ 与 ⟦SLOT_40⟧；当模型容量扩大到 ViT-L/14（427.62M 参数）时，提升幅度分别增至 ⟦SLOT_41⟧ 与 ⟦SLOT_42⟧。这些结果凸显了本数据在提升模型性能上的可扩展性与有效性。(2) 原有能力的增强：除细粒度理解任务上的改进外，在我们的数据上训练也提升了标准检索任务的性能，如图 5 所示。这说明模型通过在最小改动任务上训练获得了更好的对齐，表明我们的数据普遍适用于各类跨模态任务。

**EN** 6.2 Fine-tuning Multimodal Large Language Models (MLLMs)

**ZH** 6.2 微调多模态大语言模型（MLLM）

**EN** We utilized Idefics2 [15] to improve fine-grained understanding, employing our instruction-formatted dataset. Given its proficiency in multimodal interactions and advanced multi-image processing, Idefics2 was chosen for its open-source accessibility, model size and leading zero-shot performance.

**ZH** 我们利用 Idefics2[15] 来提升细粒度理解，采用我们指令格式的数据集。鉴于 Idefics2 在多模态交互上的熟练程度与先进的多图处理能力，加上其开源可获取性、模型规模与领先的零样本表现，我们选择了它。

**EN** Dataset and QLoRa Fine-tuning Our dataset, VisMin Instruct-IT, includes image-text pairs created using a rule-based approach (see A.2.3 for details). We reformulated these pairs for MLLMs, where the task is to select the correct image from two options based on a given caption or choose the appropriate caption for an image from two possibilities. While the base Idefics2 model was trained with a variable number of images in a sequence, we limited it to two images to include one positive and one hard negative example from VisMin. We fine-tuned the Idefics2-8B model using the QLoRa technique [4], updating adapters in the language model and modality connector including perceiver resampler with 1 A100 80GB GPU. We used ⟦SLOT_43⟧-bit quantization, with ⟦SLOT_44⟧ and ⟦SLOT_45⟧ for LoRa, and a learning rate of ⟦SLOT_46⟧. The model was fine-tuned for one epoch with an accumulated batch size of ⟦SLOT_47⟧.

**ZH** 数据集与 QLoRa 微调 我们的数据集 VisMin Instruct-IT 包含以基于规则的方式构建的图文对（细节见 A.2.3）。我们为 MLLM 重新表述了这些配对：任务是根据给定描述从两张图像中选出正确的图像，或根据给定图像从两条描述中选出合适的描述。虽然基座 Idefics2 模型在训练时序列中的图像数量可变，我们把它限制为两张，以便包含一个正例与一个来自 VisMin 的难负例。我们用 QLoRa 技术[4] 微调 Idefics2-8B 模型，在语言模型与模态连接器（含 perceiver 重采样器）中更新适配器，使用 1 张 A100 80GB GPU。我们采用 ⟦SLOT_43⟧ 位量化，LoRa 的 ⟦SLOT_44⟧ 与 ⟦SLOT_45⟧，学习率为 ⟦SLOT_46⟧。模型微调一个轮次，累积批大小为 ⟦SLOT_47⟧。

**EN** Results The fine-tuned Idefics2 model shows significant improvement on VisMin (see Table 3) across all categories, comparable to GPT4-o (see Table 2), demonstrating the effectiveness of our minimal-change data in enhancing MLLM fine-grained understanding. Notably, in the Spatial Relation category, gains of ⟦SLOT_48⟧, ⟦SLOT_49⟧, and ⟦SLOT_50⟧ were observed for Text, Image, and Group, respectively, unlike CLIP, where fine-tuning did not improve spatial understanding. Fine-tuning Idefics2 also transfers well to other fine-grained benchmarks, achieving over ⟦SLOT_51⟧ overall improvement (see Table 4). To assess generalization, we evaluated its zero-shot performance on non-fine-grained tasks (MMMU [41] and POPE [19]; results in Fig. 5 (right)). The model maintained comparable performance on POPE but dropped on MMMU, likely due to the binary-choice format in our fine-tuning data. This suggests further gains could be made by combining our data with instruction-tuning datasets, though this wasn’t pursued due to the GPU demands of fine-tuning an 8B model with additional data.

**ZH** 结果 微调后的 Idefics2 模型在 VisMin 上各品类均有显著提升（见表 3），与 GPT4-o 相当（见表 2），说明我们的最小改动数据在增强 MLLM 细粒度理解上确有成效。值得注意的是，在空间关系类别上，文本、图像与分组分数分别提升了 ⟦SLOT_48⟧、⟦SLOT_49⟧ 与 ⟦SLOT_50⟧；而 CLIP 的微调并未改善空间理解。微调 Idefics2 也能很好地迁移到其他细粒度基准，整体提升超过 ⟦SLOT_51⟧（见表 4）。为评估泛化性，我们在非细粒度任务（MMMU[41] 与 POPE[19]，结果见图 5 右）上做了零样本评测：模型在 POPE 上性能基本持平，但在 MMMU 上有所下降，可能是因为我们微调数据采用了二选一的格式。这说明把我们的数据与指令微调数据集结合还可能带来进一步提升，不过由于额外数据微调 8B 模型的 GPU 开销，我们没有继续推进。

**EN** In addition to our main results, we provide further analysis in the Appendix A.3, including detailed evaluations on additional multimodal benchmarks, zero-shot image classification task, and video understanding tasks.

**ZH** 除主要结果外，我们在附录 A.3 中给出了进一步分析，包括在更多多模态基准上的详细评测、零样本图像分类任务以及视频理解任务。

**EN** 7 Conclusion and Limitations

**ZH** 7 结论与局限性

**EN** We present VisMin , a benchmark for evaluating fine-grained visual understanding in VLMs such as CLIP, SigLIP, LLaVA, and Idefics2. While these models perform well in object and attribute recognition, they struggle with counting and spatial relationships. To address this, we fine-tuned CLIP and Idefics2 on our minimal-change dataset, yielding significant improvements in objects, attributes, and counting. For spatial relations, CLIP showed limited gains, while Idefics2 made notable progress. Fine-tuning also enhanced CLIP’s image-text alignment, demonstrated in COCO retrieval tasks, underscoring our dataset’s value as a training resource for VLMs. Limitations: Despite automatic filtering, the dataset contains noise, including image deformations and text-image mismatches due to diffusion model limitations. Future diffusion model advancements should improve minimal-change editing. Additionally, our model may inherit social biases from the base models (CLIP/Idefics2), as no specific mitigation measures were applied during fine-tuning. Our use of uniform prompts for evaluation may have influenced performance variably.

**ZH** 我们提出 VisMin，一个用于评估 CLIP、SigLIP、LLaVA、Idefics2 等 VLM 细粒度视觉理解的基准。这些模型在物体与属性识别上表现良好，却在计数与空间关系上十分吃力。为此，我们在最小改动数据集上微调 CLIP 与 Idefics2，在物体、属性与计数上取得显著提升；在空间关系上，CLIP 的提升有限，而 Idefics2 进步明显。微调还增强了 CLIP 的图文对齐能力，这在 COCO 检索任务中得到体现，凸显了本数据集作为 VLM 训练资源的价值。局限性：尽管有自动过滤，受扩散模型能力所限，数据集仍包含噪声，如图像形变与图文不匹配。未来扩散模型的进步应能改善最小改动编辑。此外，由于微调中未采取专门的缓解措施，我们的模型可能继承了基座模型（CLIP/Idefics2）的社会偏见。我们在评测中使用了统一的提示，这可能对性能产生了不同程度的影响。

**EN** Acknowledgments and Disclosure of Funding

**ZH** 致谢与经费披露

**EN** We express our gratitude to Mojtaba Faramarzi and Yash Goyal for their constructive feedback throughout the different stages of the project. We also acknowledge the valuable feedback provided by Qian Yang, Kanish Jain, and Oscar Manas on the early draft. The technical support extended by the Mila IDT team in managing the computational infrastructure is greatly appreciated. Additionally, Aishwarya Agrawal received support from the Canada CIFAR AI Chair award throughout this project.

**ZH** 我们感谢 Mojtaba Faramarzi 与 Yash Goyal 在项目各阶段提出的建设性意见，也感谢 Qian Yang、Kanish Jain 与 Oscar Manas 对初稿的宝贵反馈。Mila IDT 团队在计算基础设施管理上提供的技术支持同样令我们受益良多。此外，Aishwarya Agrawal 在本项目期间获得了 Canada CIFAR AI Chair 的支持。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] Achiam et al. [2023] Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. Gpt-4 technica -->

<!-- [原子块 · verbatim] Chen et al. [2023] Zhe Chen, Jiannan Wu, Wenhai Wang, Weijie Su, Guo Chen, Sen Xing, Zhong Muyan, Qinglong Zhang, Xizhou Zhu, Lewei Lu, et al. Internvl: Scaling up vision foundation models and alignin -->

<!-- [原子块 · verbatim] Cherti et al. [2023] Mehdi Cherti, Romain Beaumont, Ross Wightman, Mitchell Wortsman, Gabriel Ilharco, Cade Gordon, Christoph Schuhmann, Ludwig Schmidt, and Jenia Jitsev. Reproducible scaling laws for -->

<!-- [原子块 · verbatim] Dettmers et al. [2024] Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, and Luke Zettlemoyer. Qlora: Efficient finetuning of quantized llms. Advances in Neural Information Processing Systems , 36, 2024. -->

<!-- [原子块 · verbatim] Doveh et al. [2023] Sivan Doveh, Assaf Arbelle, Sivan Harary, Eli Schwartz, Roei Herzig, Raja Giryes, Rogerio Feris, Rameswar Panda, Shimon Ullman, and Leonid Karlinsky. Teaching structured vision & l -->

<!-- [原子块 · verbatim] Doveh et al. [2024] Sivan Doveh, Assaf Arbelle, Sivan Harary, Roei Herzig, Donghyun Kim, Paola Cascante-Bonilla, Amit Alfassy, Rameswar Panda, Raja Giryes, Rogerio Feris, et al. Dense and aligned capt -->

<!-- [原子块 · verbatim] Herzig et al. [2023] Roei Herzig, Alon Mendelson, Leonid Karlinsky, Assaf Arbelle, Rogerio Feris, Trevor Darrell, and Amir Globerson. Incorporating structured representations into pretrained vision &  -->

<!-- [原子块 · verbatim] Hsieh et al. [2023] Cheng-Yu Hsieh, Jieyu Zhang, Zixian Ma, Aniruddha Kembhavi, and Ranjay Krishna. Sugarcrepe: Fixing hackable benchmarks for vision-language compositionality. arXiv preprint arXiv:23 -->

<!-- [原子块 · verbatim] Hu et al. [2023] Yushi Hu, Benlin Liu, Jungo Kasai, Yizhong Wang, Mari Ostendorf, Ranjay Krishna, and Noah A Smith. Tifa: Accurate and interpretable text-to-image faithfulness evaluation with question -->

<!-- [原子块 · verbatim] Jiang et al. [2024] Albert Q Jiang, Alexandre Sablayrolles, Antoine Roux, Arthur Mensch, Blanche Savary, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Emma Bou Hanna, Florian Bressand, et -->

<!-- [原子块 · verbatim] Kamath et al. [2023] Amita Kamath, Jack Hessel, and Kai-Wei Chang. What’s “up” with vision-language models? investigating their struggle with spatial reasoning. In Houda Bouamor, Juan Pino, and Kalika -->

<!-- [原子块 · verbatim] Kazemzadeh et al. [2014] Sahar Kazemzadeh, Vicente Ordonez, Mark Matten, and Tamara Berg. Referitgame: Referring to objects in photographs of natural scenes. In Proceedings of the 2014 conference on e -->

<!-- [原子块 · verbatim] Krishna et al. [2017] Ranjay Krishna, Yuke Zhu, Oliver Groth, Justin Johnson, Kenji Hata, Joshua Kravitz, Stephanie Chen, Yannis Kalantidis, Li-Jia Li, David A Shamma, et al. Visual genome: Connecting -->

<!-- [原子块 · verbatim] Krojer et al. [2022] Benno Krojer, Vaibhav Adlakha, Vibhav Vineet, Yash Goyal, Edoardo Ponti, and Siva Reddy. Image retrieval from contextual descriptions. In Smaranda Muresan, Preslav Nakov, and Alin -->

<!-- [原子块 · verbatim] Laurençon et al. [2024] Hugo Laurençon, Lucile Saulnier, Léo Tronchon, Stas Bekman, Amanpreet Singh, Anton Lozhkov, Thomas Wang, Siddharth Karamcheti, Alexander Rush, Douwe Kiela, et al. Obelics: An o -->

<!-- [原子块 · verbatim] Li et al. [2023a] Bo Li, Yuanhan Zhang, Liangyu Chen, Jinghao Wang, Fanyi Pu, Jingkang Yang, Chunyuan Li, and Ziwei Liu. Mimic-it: Multi-modal in-context instruction tuning. arXiv preprint arXiv:2306. -->

<!-- [原子块 · verbatim] Li et al. [2024] Juncheng Li, Kaihang Pan, Zhiqi Ge, Minghe Gao, Hanwang Zhang, Wei Ji, Wenqiao Zhang, Tat seng Chua, Siliang Tang, and Yueting Zhuang. Fine-tuning multimodal LLMs to follow zero-shot  -->

<!-- [原子块 · verbatim] Li et al. [2022] Junnan Li, Dongxu Li, Caiming Xiong, and Steven Hoi. Blip: Bootstrapping language-image pre-training for unified vision-language understanding and generation. In International confere -->

<!-- [原子块 · verbatim] Li et al. [2023b] Yifan Li, Yifan Du, Kun Zhou, Jinpeng Wang, Wayne Xin Zhao, and Ji-Rong Wen. Evaluating object hallucination in large vision-language models. arXiv preprint arXiv:2305.10355 , 2023b. -->

<!-- [原子块 · verbatim] Li et al. [2023c] Yuheng Li, Haotian Liu, Qingyang Wu, Fangzhou Mu, Jianwei Yang, Jianfeng Gao, Chunyuan Li, and Yong Jae Lee. Gligen: Open-set grounded text-to-image generation. ArXiv , abs/2301.0709 -->

<!-- [原子块 · verbatim] Lian et al. [2023] Long Lian, Boyi Li, Adam Yala, and Trevor Darrell. Llm-grounded diffusion: Enhancing prompt understanding of text-to-image diffusion models with large language models. arXiv preprin -->

<!-- [原子块 · verbatim] Lin et al. [2014] Tsung-Yi Lin, Michael Maire, Serge Belongie, James Hays, Pietro Perona, Deva Ramanan, Piotr Dollár, and C Lawrence Zitnick. Microsoft coco: Common objects in context. In Computer Vis -->

<!-- [原子块 · verbatim] Liu et al. [2023a] Fangyu Liu, Guy Emerson, and Nigel Collier. Visual spatial reasoning. Transactions of the Association for Computational Linguistics , 11:635–651, 2023a. -->

<!-- [原子块 · verbatim] Liu et al. [2024] Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. Visual instruction tuning. Advances in neural information processing systems , 36, 2024. -->

<!-- [原子块 · verbatim] Liu et al. [2023b] Shilong Liu, Zhaoyang Zeng, Tianhe Ren, Feng Li, Hao Zhang, Jie Yang, Chunyuan Li, Jianwei Yang, Hang Su, Jun Zhu, et al. Grounding dino: Marrying dino with grounded pre-training fo -->

<!-- [原子块 · verbatim] Paiss et al. [2023] Roni Paiss, Ariel Ephrat, Omer Tov, Shiran Zada, Inbar Mosseri, Michal Irani, and Tali Dekel. Teaching clip to count to ten, 2023. -->

<!-- [原子块 · verbatim] Parcalabescu et al. [2022] Letitia Parcalabescu, Michele Cafagna, Lilitta Muradjan, Anette Frank, Iacer Calixto, and Albert Gatt. VALSE: A task-independent benchmark for vision and language models cen -->

<!-- [原子块 · verbatim] Peng et al. [2023] Wujian Peng, Sicheng Xie, Zuyao You, Shiyi Lan, and Zuxuan Wu. Synthesize, diagnose, and optimize: Towards fine-grained vision-language understanding, 2023. -->

<!-- [原子块 · verbatim] Plummer et al. [2017] Bryan A. Plummer, Liwei Wang, Christopher M. Cervantes, Juan C. Caicedo, Julia Hockenmaier, and Svetlana Lazebnik. Flickr30k entities: Collecting region-to-phrase correspondences -->

<!-- [原子块 · verbatim] Podell et al. [2023] Dustin Podell, Zion English, Kyle Lacey, Andreas Blattmann, Tim Dockhorn, Jonas Müller, Joe Penna, and Robin Rombach. Sdxl: Improving latent diffusion models for high-resolution i -->

<!-- [原子块 · verbatim] Radford et al. [2021] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, et al. Learning transferable v -->

<!-- [原子块 · verbatim] Singh et al. [2022] Amanpreet Singh, Ronghang Hu, Vedanuj Goswami, Guillaume Couairon, Wojciech Galuba, Marcus Rohrbach, and Douwe Kiela. Flava: A foundational language and vision alignment model. In  -->

<!-- [原子块 · verbatim] Singh et al. [2023] Harman Singh, Pengchuan Zhang, Qifan Wang, Mengjiao Wang, Wenhan Xiong, Jingfei Du, and Yu Chen. Coarse-to-fine contrastive learning in image-text-graph space for improved vision-l -->

<!-- [原子块 · verbatim] Suvorov et al. [2021] Roman Suvorov, Elizaveta Logacheva, Anton Mashikhin, Anastasia Remizova, Arsenii Ashukha, Aleksei Silvestrov, Naejin Kong, Harshith Goka, Kiwoong Park, and Victor Lempitsky. Reso -->

<!-- [原子块 · verbatim] Team [2024] Gemini Team. Gemini: A family of highly capable multimodal models, 2024. -->

<!-- [原子块 · verbatim] Thrush et al. [2022] Tristan Thrush, Ryan Jiang, Max Bartolo, Amanpreet Singh, Adina Williams, Douwe Kiela, and Candace Ross. Winoground: Probing vision and language models for visio-linguistic compos -->

<!-- [原子块 · verbatim] Tong et al. [2024] Shengbang Tong, Zhuang Liu, Yuexiang Zhai, Yi Ma, Yann LeCun, and Saining Xie. Eyes wide shut? exploring the visual shortcomings of multimodal llms, 2024. -->

<!-- [原子块 · verbatim] Wang et al. [2023a] Tan Wang, Kevin Lin, Linjie Li, Chung-Ching Lin, Zhengyuan Yang, Hanwang Zhang, Zicheng Liu, and Lijuan Wang. Equivariant similarity for vision-language foundation models. In Proce -->

<!-- [原子块 · verbatim] Wang et al. [2023b] Weihan Wang, Qingsong Lv, Wenmeng Yu, Wenyi Hong, Ji Qi, Yan Wang, Junhui Ji, Zhuoyi Yang, Lei Zhao, Xixuan Song, et al. Cogvlm: Visual expert for pretrained language models. arXiv -->

<!-- [原子块 · verbatim] Yu et al. [2022] Jiahui Yu, Zirui Wang, Vijay Vasudevan, Legg Yeung, Mojtaba Seyedhosseini, and Yonghui Wu. Coca: Contrastive captioners are image-text foundation models. arXiv preprint arXiv:2205.019 -->

<!-- [原子块 · verbatim] Yue et al. [2023] Xiang Yue, Yuansheng Ni, Kai Zhang, Tianyu Zheng, Ruoqi Liu, Ge Zhang, Samuel Stevens, Dongfu Jiang, Weiming Ren, Yuxuan Sun, et al. Mmmu: A massive multi-discipline multimodal under -->

<!-- [原子块 · verbatim] Yuksekgonul et al. [2022] Mert Yuksekgonul, Federico Bianchi, Pratyusha Kalluri, Dan Jurafsky, and James Zou. When and why vision-language models behave like bags-of-words, and what to do about it? In -->

<!-- [原子块 · verbatim] Yuksekgonul et al. [2023] Mert Yuksekgonul, Federico Bianchi, Pratyusha Kalluri, Dan Jurafsky, and James Zou. When and why vision-language models behave like bags-of-words, and what to do about it? In -->

<!-- [原子块 · verbatim] Zhai et al. [2023] Xiaohua Zhai, Basil Mustafa, Alexander Kolesnikov, and Lucas Beyer. Sigmoid loss for language image pre-training. In Proceedings of the IEEE/CVF International Conference on Computer -->

<!-- [原子块 · verbatim] Zhang et al. [2024] Jianrui Zhang, Mu Cai, Tengyang Xie, and Yong Jae Lee. Countercurate: Enhancing physical and semantic visio-linguistic compositional reasoning via counterfactual examples. arXiv pr -->

<!-- [原子块 · verbatim] Zhang et al. [2023] Le Zhang, Rabiul Awal, and Aishwarya Agrawal. Contrasting intra-modal and ranking cross-modal hard negatives to enhance visio-linguistic fine-grained understanding. arXiv preprint  -->

<!-- [原子块 · verbatim] Zhao et al. [2022] Tiancheng Zhao, Tianqi Zhang, Mingwei Zhu, Haozhan Shen, Kyusong Lee, Xiaopeng Lu, and Jianwei Yin. An explainable toolbox for evaluating pre-trained vision-language models. In Proc -->

**EN** Appendix A Appendix

**ZH** 附录 A 附录

**EN** A.1 Societal Impact

**ZH** A.1 社会影响

**EN** Our work shares the broader positive societal implications of vision-language research, particularly in improving the accuracy of vision-language models (VLMs). These advancements could benefit various applications, such as helping visually impaired individuals better interpret their surroundings, creating interactive learning tools for children, and enabling more effective interaction with in-home robots. However, like most technologies, accurate vision-language systems also present potential risks. For instance, they could be misused to extract sensitive information from public CCTV footage or inadvertently leak personal data, such as credit card information, when assisting visually impaired users. To address these concerns, robust privacy safeguards are essential to mitigate these risks.

**ZH** 我们的工作具有视觉—语言研究普遍具有的积极社会意义，尤其是在提升视觉—语言模型（VLM）准确性方面。这些进展有望惠及诸多应用，例如帮助视障人士更好地理解周围环境、为儿童打造交互式学习工具，以及实现与家用机器人更有效的交互。然而，与大多数技术一样，准确的视觉—语言系统也存在潜在风险：它们可能被滥用于从公共监控录像中提取敏感信息，或在辅助视障用户时无意泄露信用卡信息等个人数据。为应对这些担忧，必须建立稳健的隐私保护措施以降低风险。

**EN** A.2 Prompt Templates

**ZH** A.2 提示模板

**EN** A.2.1 Prompts Used for Edit Instruction Generation

**ZH** A.2.1 用于生成编辑指令的提示

**EN** We utilize the Mixtral ⟦SLOT_52⟧B LLM to generate edit suggestions across selected categories: objects, attributes, counting, and spatial relations. The specific prompts used for each category are detailed in the Boxes below. These prompts guide the LLM in creating minimal, precise modifications to captions, ensuring the generation of high-quality hard-negative instances.

**ZH** 我们使用 Mixtral ⟦SLOT_52⟧B LLM 在选定的类别（物体、属性、计数与空间关系）上生成编辑建议。各类别所用的具体提示详见下方各框。这些提示引导 LLM 对描述做出最小而精确的修改，从而保证生成高质量的难负例样本。

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

**EN** A.2.2 Prompts Used for Edit Instruction Verification

**ZH** A.2.2 用于校验编辑指令的提示

**EN** We employ the Mixtral47B LLM to verify edit suggestions in the object and attribute categories. The specific prompts used for this verification process are illustrated in the Box A.2.2. Verification is crucial because initial suggestions by the LLM can occasionally be implausible or violate the intended edit category. By thoroughly verifying the edits, we ensure the generation of accurate and high-quality hard-negative instances, which are essential for effectively testing and improving VLMs.

**ZH** 我们使用 Mixtral47B LLM 校验物体与属性类别的编辑建议，校验过程所用的具体提示见框 A.2.2。校验之所以关键，是因为 LLM 的初始建议偶尔会不合理或违背预期的编辑类别。通过彻底校验这些编辑，我们确保生成准确、高质量的难负例样本，这对有效检验和改进 VLM 至关重要。

<!-- [原子块 · svg]  -->

**EN** A.2.3 VisMin Instruct-It Dataset

**ZH** A.2.3 VisMin Instruct-It 数据集

**EN** In the VisMin Instruction dataset, a sample consists of a source image-caption pair ⟦SLOT_53⟧ and its minimally edited version ⟦SLOT_54⟧. To construct the VisMin Instruct-IT dataset, we create four instruction samples from each VisMin sample:

**ZH** 在 VisMin 指令数据集中，一个样本由源图文对 ⟦SLOT_53⟧ 及其最小编辑版本 ⟦SLOT_54⟧ 组成。为构建 VisMin Instruct-IT 数据集，我们从每个 VisMin 样本生成四个指令样本：

**EN** • Two samples for the Image-Task (selecting the best matching image given a caption): 1. Given ⟦SLOT_55⟧, select between ⟦SLOT_56⟧ and ⟦SLOT_57⟧ 2. Given ⟦SLOT_58⟧, select between ⟦SLOT_59⟧ and ⟦SLOT_60⟧

**ZH** • 图像任务（给定描述选出最匹配的图像）的两个样本：1. 给定 ⟦SLOT_55⟧，在 ⟦SLOT_56⟧ 与 ⟦SLOT_57⟧ 之间选择 2. 给定 ⟦SLOT_58⟧，在 ⟦SLOT_59⟧ 与 ⟦SLOT_60⟧ 之间选择

**EN** • Two samples for the Text-Task (selecting the best matching caption given an image): 1. Given ⟦SLOT_61⟧, select between ⟦SLOT_62⟧ and ⟦SLOT_63⟧ 2. Given ⟦SLOT_64⟧, select between ⟦SLOT_65⟧ and ⟦SLOT_66⟧

**ZH** • 文本任务（给定图像选出最匹配的描述）的两个样本：1. 给定 ⟦SLOT_61⟧，在 ⟦SLOT_62⟧ 与 ⟦SLOT_63⟧ 之间选择 2. 给定 ⟦SLOT_64⟧，在 ⟦SLOT_65⟧ 与 ⟦SLOT_66⟧ 之间选择

**EN** Please refer to Table 5 in the rebuttal PDF for the exact set of instruction templates used. We randomly sample one template for each task type when creating the instruction samples.

**ZH** 具体使用的指令模板集合请参考 rebuttal PDF 中的表 5。创建指令样本时，我们为每种任务类型随机采样一个模板。

**EN** In total, we create 65k instruction samples for training. Additionally, we include 16k randomly selected image-caption pairs (either ⟦SLOT_67⟧ or ⟦SLOT_68⟧) to retain the model’s general image captioning ability.

**ZH** 我们共创建了 6.5 万条指令样本用于训练。此外，还加入了 1.6 万条随机选取的图文对（⟦SLOT_67⟧ 或 ⟦SLOT_68⟧），以保留模型通用的图像描述能力。

**EN** Table 5: VisMin Instruct-It dataset creation templates

**ZH** 表 5：VisMin Instruct-It 数据集的构建模板

**EN** Template Type Template Examples Image-Task “You are given two images. Which one better aligns with the description: {caption}? The first or the second image?” “Question: You are given two images. Which one better aligns with the description? {caption} Choices: First, Second.” “Based on the description: {caption}, please select one of the given options that best matches the image. Choices: First, Second.” Text-Task “Question: Does this image depict: (A) {candidate text A}, or (B) {candidate text B}? Choices: A, B.” “Does this image best represent: (A) {candidate text A}, or (B) {candidate text B}?” “Which of the following best matches the image: (A) {candidate text A}, or (B) {candidate text B}?”

**ZH** 模板类型 模板示例 图像任务 “You are given two images. Which one better aligns with the description: {caption}? The first or the second image?” “Question: You are given two images. Which one better aligns with the description? {caption} Choices: First, Second.” “Based on the description: {caption}, please select one of the given options that best matches the image. Choices: First, Second.” 文本任务 “Question: Does this image depict: (A) {candidate text A}, or (B) {candidate text B}? Choices: A, B.” “Does this image best represent: (A) {candidate text A}, or (B) {candidate text B}?” “Which of the following best matches the image: (A) {candidate text A}, or (B) {candidate text B}?”

**EN** A.3 Additional Results

**ZH** A.3 补充结果

**EN** We report additional results to demonstrate the impact of fine-tuning on our dataset across different aspects of scene understanding. We evaluated our fine-tuned models, VisMin-CLIP and VisMin-Idefics2, on various tasks designed to assess distinct elements of multimodal comprehension.

**ZH** 我们报告补充结果，以展示在我们的数据集上微调对场景理解各个方面的影响。我们在多个任务上评估了微调后的 VisMin-CLIP 与 VisMin-Idefics2，这些任务旨在考察多模态理解的不同要素。

**EN** Table 6: Performance breakdown of EQBEN video splits for both CLIP fine-tuned and Idefics2 models. The table also includes results on additional multimodal benchmarks for Idefics2 family of models and ImageNet results for various CLIP models. We leave the CLIP results on the additional multimodal benchmarks and the Idefics2 results on ImageNet blank due to the task-format not being suitable for evaluation.

**ZH** 表 6：CLIP 微调模型与 Idefics2 模型在 EQBEN 视频划分上的性能分解。表中还包含 Idefics2 系列模型在更多多模态基准上的结果，以及各 CLIP 模型在 ImageNet 上的结果。由于任务格式不适合评测，我们留空了 CLIP 在补充多模态基准上的结果，以及 Idefics2 在 ImageNet 上的结果。

**EN** EQ-YouCook2 EQ-GEBC EQ-AG Additional Multimodal Benchmarks ImageNet T I G T I G T I G MathVista MMBench TextVQA VQAv2 top1 top5 CLIP(ViT-L/14) 50.00 65.00 40.00 15.00 10.00 0.00 15.00 25.00 10.00 - - - - 75.53 94.59 NegCLIP 65.00 60.00 50.00 20.00 20.00 0.00 15.00 35.00 10.00 - - - - 65.50 90.00 VisMin-CLIP 80.00 70.00 65.00 30.00 10.00 5.00 30.00 25.00 10.00 - - - - 68.20 91.81 Idefics2 84.62 53.85 53.85 25.00 40.00 15.00 52.63 47.37 31.58 53.00 76.18 73.40 78.82 - - VisMin-Idefics2 69.23 84.62 61.54 35.00 20.00 15.00 57.89 36.84 31.58 47.80 72.74 71.89 79.75 - -

**ZH** EQ-YouCook2 EQ-GEBC EQ-AG 补充多模态基准 ImageNet T I G T I G T I G MathVista MMBench TextVQA VQAv2 top1 top5 CLIP(ViT-L/14) 50.00 65.00 40.00 15.00 10.00 0.00 15.00 25.00 10.00 - - - - 75.53 94.59 NegCLIP 65.00 60.00 50.00 20.00 20.00 0.00 15.00 35.00 10.00 - - - - 65.50 90.00 VisMin-CLIP 80.00 70.00 65.00 30.00 10.00 5.00 30.00 25.00 10.00 - - - - 68.20 91.81 Idefics2 84.62 53.85 53.85 25.00 40.00 15.00 52.63 47.37 31.58 53.00 76.18 73.40 78.82 - - VisMin-Idefics2 69.23 84.62 61.54 35.00 20.00 15.00 57.89 36.84 31.58 47.80 72.74 71.89 79.75 - -

**EN** Multimodal Benchmarks: We assessed performance of multimodal LLMs (Idefics2 and Vismin-Idefics2) on benchmarks like MathVista, MMBench, TextVQA, and VQAv2 to understand how fine-tuning on our data impacts tasks requiring both general scene understanding and specialized skills (e.g., OCR and math) (see Table 6, middle block).33 3 Contrastive models with two-tower encodings are not suitable for these benchmarks, as these benchmarks require generating text outputs rather than just measuring similarity between encoded images and texts. Results show slight declines on specialized tasks (MathVista, MMBench, TextVQA) but notable improvements on VQAv2 that tests for general scene understanding, supporting our hypothesis that our dataset strengthens general scene comprehension while not losing performance much on more specialized tasks.

**ZH** 多模态基准：我们在 MathVista、MMBench、TextVQA 与 VQAv2 等基准上评估了多模态 LLM（Idefics2 与 Vismin-Idefics2），以了解在我们的数据上微调会如何影响那些既需要通用场景理解、又需要专门技能（如 OCR 与数学）的任务（见表 6 中间部分）。33 3 采用双塔编码的对比式模型不适合这些基准，因为这类基准要求生成文本输出，而不仅仅是度量编码后图像与文本之间的相似度。结果显示，在专门任务（MathVista、MMBench、TextVQA）上略有下降，但在考察通用场景理解的 VQAv2 上有明显提升，这支持了我们的假设：本数据集强化了通用场景理解，同时在更专门的任务上性能损失不大。

**EN** Zero-Shot Image Classification: To evaluate the robustness of learned representations of the contrastive models, we included evaluation on zero-shot image classification on ImageNet (see Table 6, last block). Both NegCLIP and VisMin-CLIP underperform compared to the base CLIP model. However, VisMin-CLIP shows a smaller performance drop compared to NegCLIP, indicating that it retains a stronger generalization capability even after fine-tuning.

**ZH** 零样本图像分类：为评估对比式模型所学表示的鲁棒性，我们加入了 ImageNet 上的零样本图像分类评测（见表 6 最后部分）。NegCLIP 与 VisMin-CLIP 都不如基座 CLIP 模型；但 VisMin-CLIP 的性能下降幅度小于 NegCLIP，说明它在微调后仍保有更强的泛化能力。

**EN** Performance on Video Understanding Tasks: Finally, we tested if fine-tuning the models on our minimal-change dataset also improves their performance on video understanding tasks since video understanding tasks require identifying subtle frame-to-frame variations (see Fig. 6 for some examples). To test this, we evaluated the models on the EQBEN [38] benchmark, particularly the following splits: EQ-YouCook2, which focuses on cooking procedures from instructional videos; EQ-GEBC, which identifies event boundaries in kinetic videos; and EQ-AG, which captures changes between objects and their pairwise relationships during actions.

**ZH** 视频理解任务上的表现：最后，我们测试了在我们的最小改动数据集上微调是否也能提升模型在视频理解任务上的表现，因为视频理解需要识别帧与帧之间的细微变化（部分示例见图 6）。为此，我们在 EQBEN[38] 基准上评估模型，具体选取以下划分：EQ-YouCook2，聚焦教学视频中的烹饪流程；EQ-GEBC，识别动态视频中的事件边界；EQ-AG，捕捉动作过程中物体及其两两关系的变化。

**EN** We would like to note that our fine-tuned models excel at discerning subtle semantic differences, but neighboring video frames often exhibit low-level rather than semantic changes. Abrupt changes between frames, like a bus turning into a car, a shirt changing color, or objects swapping positions, are rare. Additionally, our dataset does not cover action changes, which are typical in videos. Therefore, we expect finetuning on our dataset to result in limited improvements for nearby video frames.

**ZH** 需要说明的是，我们的微调模型擅长辨别细微的语义差异，而相邻视频帧之间往往是低层次而非语义层面的变化。帧间的突变（例如公交车变成汽车、衬衫换颜色或物体交换位置）十分罕见；此外，我们的数据集未覆盖视频中常见的动作变化。因此我们预期，在我们的数据集上微调对相邻视频帧带来的提升有限。

**EN** This was confirmed in our results (see Table 6, first block), where fine-tuning CLIP and Idefics2 showed significant improvements on EQ-YouCook2 (in group scores) due to its higher presence of object-based changes, while performance remained similar on EQ-GBEC and EQ-AG, which mostly feature action shifts. Thus, our dataset is most effective for enhancing video understanding in scenarios involving subtle semantic adjustments rather than dynamic actions.

**ZH** 我们的结果印证了这一点（见表 6 第一部分）：由于 EQ-YouCook2 中基于物体的变化更多，微调 CLIP 与 Idefics2 在其分组分数上有显著提升；而在以动作转换为主要内容的 EQ-GBEC 与 EQ-AG 上性能基本持平。因此，我们的数据集最适用于增强涉及细微语义调整而非动态动作的视频理解场景。

<!-- [原子块 · object]  -->

**EN** Figure 6: Examples from different video splits from the EQBEN benchmark.

**ZH** 图 6：来自 EQBEN 基准不同视频划分的示例。

**EN** A.4 Annotation Platform and Benchmark Quality

**ZH** A.4 标注平台与基准质量

**EN** A.4.1 Human Verification of Benchmark

**ZH** A.4.1 基准的人工验证

**EN** The human verification process involves four main steps. 1) Naturalness and Image-Text Matching Verification: in this step, humans evaluate the data samples using the following three criteria: a) whether the image looks natural or not, b) whether the caption sounds sensical or not, and c) whether the image matches the caption or not, addressing limitations of automatic filtering and maintaining robustness against manipulation [8] (see Figure 7). Only 26% of synthetic images pass this step, highlighting the need for human verification. The low acceptance rate is mainly associated with the high rejection rate of criterion a, where most counting and spatial relation synthetic images do not appear natural. Please refer to Appendix Table 7 for detailed acceptance rates for each criterion. Please note that we aimed for a balanced benchmark. To address the higher rejection rates for the categories of counting and spatial relation, we began with a larger number of samples in these categories. 2) Visual Edit Verification confirms that the edited images accurately reflect the specified edits without additional changes, ensuring visual minimal change, with an acceptance rate of 80% (see Figure 8). 3) Edit Instruction Verification checks that LLM-generated edit instructions are minimal and targeted, altering only one aspect of the object, attribute, counting, or spatial relation in captions and images, with an acceptance rate of 84%. (see Figure 9). 4) Textual Edit Verification ensures the edited sentence accurately reflects the specified edit instruction without additional changes and classifies the change type, with an acceptance rate of 95% (see Figure 10).

**ZH** 人工验证过程包含四个主要步骤。1) 自然度与图文匹配验证：这一步中，人工依据以下三条标准评估数据样本：a) 图像是否看起来自然，b) 描述是否通顺合理，c) 图像是否与描述匹配，以此弥补自动过滤的不足，并抵御操纵带来的影响[8]（见图 7）。只有 26% 的合成图像通过这一步，凸显了人工验证的必要性。接受率低主要与标准 a 的高拒绝率有关——多数计数与空间关系类合成图像看起来不自然。各标准的详细接受率见附录表 7。请注意，我们的目标是构建均衡的基准：为应对计数与空间关系类别更高的拒绝率，我们在这些类别上准备了更多的初始样本。2) 视觉编辑验证：确认编辑后的图像准确反映了指定的改动且未引入额外变化，从而保证视觉上的最小改动，接受率为 80%（见图 8）。3) 编辑指令验证：检查 LLM 生成的编辑指令是否为最小且目标明确——只改动描述与图像中物体、属性、计数或空间关系中的一个方面，接受率为 84%（见图 9）。4) 文本编辑验证：确保编辑后的句子准确反映指定的编辑指令、未引入额外变化，并对改动类型做出分类，接受率为 95%（见图 10）。

**EN** Table 7: Acceptance rates for all criteria across different categories.

**ZH** 表 7：各标准在不同类别上的接受率。

**EN** Criterion Object Attribute Counting S. Relation Overall Step 1-a: Naturalness of Image 64% 80% 41% 22% 37% Step 1-b: Sensicality of Caption 84% 79% 75% 70% 74% Step 1-c: Image-Text Matching 83% 89% 52% 65% 65% Step 2: Visual Edit Verification 81% 79% 81% 78% 80% Step 3: Edit Instruction Verification 81% 86% 85% 84% 84% Step 4: Textual Edit Verification 95% 94% 94% 95% 95% Step 4: Automatic Categorization Verification 95% 91% 99% 100% 97%

**ZH** 标准 物体 属性 计数 空间关系 总体 步骤 1-a：图像自然度 64% 80% 41% 22% 37% 步骤 1-b：描述合理性 84% 79% 75% 70% 74% 步骤 1-c：图文匹配 83% 89% 52% 65% 65% 步骤 2：视觉编辑验证 81% 79% 81% 78% 80% 步骤 3：编辑指令验证 81% 86% 85% 84% 84% 步骤 4：文本编辑验证 95% 94% 94% 95% 95% 步骤 4：自动分类验证 95% 91% 99% 100% 97%

<!-- [原子块 · img]  -->

**EN** Figure 7: Instructions for naturalness and image-text matching verification.

**ZH** 图 7：自然度与图文匹配验证的说明。

<!-- [原子块 · img]  -->

**EN** Figure 8: Instructions for visual edit verification after applying edit instructions.

**ZH** 图 8：施加编辑指令后进行视觉编辑验证的说明。

<!-- [原子块 · img]  -->

**EN** Figure 9: Instructions for edit instruction verification.

**ZH** 图 9：编辑指令验证的说明。

<!-- [原子块 · img]  -->

**EN** Figure 10: Instructions for textual edit verification.

**ZH** 图 10：文本编辑验证的说明。

**EN** A.4.2 Human baseline

**ZH** A.4.2 人类基线

**EN** We gather human annotations using Amazon Mechanical Turk (AMT) to determine human performance on our benchmark, replicating the exact tasks given to models as described in Section 5. Additionally, annotators can choose “none” or “both” options (please see Figure 11 and Figure 12); we deliberately included these options to accurately estimate the best model performance when tasks are difficult for humans. We collect five annotations per sample for each of the four scenarios in the image-text matching task. We compute image score, text score, and group score as described in Section 5. If the answer “both” or “none” is chosen by three or more annotators, or if one annotator chooses “none" or “both" while the other options each receive exactly two votes, we randomly assign a 50% match to maintain consistency with the model evaluation setup.

**ZH** 我们通过 Amazon Mechanical Turk（AMT）收集人工标注，以确定人类在本基准上的表现，任务与第 5 节中给模型的完全一致。此外，标注者可以选择「none」或「both」选项（见图 11 与图 12）；我们特意加入这些选项，是为了在任务对人类而言过于困难时，仍能准确估计模型的最佳表现。我们对图文匹配任务的四种情形，各收集每条样本五份标注，并按第 5 节所述计算图像分数、文本分数与分组分数。若三名及以上标注者选择「both」或「none」，或一名标注者选择「none」或「both」而其余选项各得两票，我们随机赋予 50% 的匹配结果，以与模型评测设置保持一致。

<!-- [原子块 · img]  -->

**EN** Figure 11: Instructions for choosing the best matching image.

**ZH** 图 11：选择最匹配图像的说明。

<!-- [原子块 · img]  -->

**EN** Figure 12: Instructions for choosing the best matching description.

**ZH** 图 12：选择最匹配描述的说明。

**EN** A.5 Random qualitative samples from training and VisMin benchmark

**ZH** A.5 来自训练集与 VisMin 基准的随机定性样本

**EN** In this section, we present random qualitative samples from both the training set and the VisMin benchmark to illustrate the quality and diversity of data used in our experiments. Specifically, we provide examples across object, attribute, relation, and counting categories to highlight the four strategic categories represented in our dataset.

**ZH** 本节展示来自训练集与 VisMin 基准的随机定性样本，以说明我们实验所用数据的质量与多样性。具体地，我们给出物体、属性、关系与计数类别的示例，凸显数据集中所体现的四个策略性类别。

<!-- [原子块 · img]  -->

**EN** Figure 13: Random qualitative samples from VisMin.

**ZH** 图 13：来自 VisMin 的随机定性样本。

<!-- [原子块 · img]  -->

**EN** Figure 14: Random qualitative samples from the training set.

**ZH** 图 14：来自训练集的随机定性样本。

<!-- [原子块 · object]  -->

**EN** Figure 15: Categories and subcategories distribution in the training split.

**ZH** 图 15：训练划分中的类别与子类别分布。

**EN** NeurIPS Paper Checklist

**ZH** NeurIPS 论文检查清单

**EN** The checklist is designed to encourage best practices for responsible machine learning research, addressing issues of reproducibility, transparency, research ethics, and societal impact. Do not remove the checklist: The papers not including the checklist will be desk rejected. The checklist should follow the references and follow the (optional) supplemental material. The checklist does NOT count towards the page limit.

**ZH** 该检查清单旨在鼓励负责任的机器学习研究中的最佳实践，涵盖可复现性、透明度、研究伦理与社会影响等问题。请勿删除该检查清单：未包含检查清单的论文将被直接拒稿。检查清单应置于参考文献之后、补充材料（可选）之后。检查清单不计入页数限制。

**EN** Please read the checklist guidelines carefully for information on how to answer these questions. For each question in the checklist:

**ZH** 请仔细阅读检查清单指南，了解如何回答这些问题。对于检查清单中的每一个问题：

**EN** • You should answer [Yes] , [No] , or [N/A] .

**ZH** • 应回答 [Yes]、[No] 或 [N/A]。

**EN** • [N/A] means either that the question is Not Applicable for that particular paper or the relevant information is Not Available.

**ZH** • [N/A] 表示该项问题对该论文不适用，或相关信息不可得。

**EN** • Please provide a short (1–2 sentence) justification right after your answer (even for NA).

**ZH** • 请在答案后紧接给出简短（1–2 句话）的理由（即便回答 N/A 也要给出）。

**EN** The checklist answers are an integral part of your paper submission. They are visible to the reviewers, area chairs, senior area chairs, and ethics reviewers. You will be asked to also include it (after eventual revisions) with the final version of your paper, and its final version will be published with the paper.

**ZH** 检查清单的答案是论文投稿的组成部分，审稿人、领域主席、资深领域主席与伦理审稿人都能看到。在论文最终版本（经修改后）中，你也需要将其附上；最终版本将随论文一同发表。

**EN** The reviewers of your paper will be asked to use the checklist as one of the factors in their evaluation. While "[Yes] " is generally preferable to "[No] ", it is perfectly acceptable to answer "[No] " provided a proper justification is given (e.g., "error bars are not reported because it would be too computationally expensive" or "we were unable to find the license for the dataset we used"). In general, answering "[No] " or "[N/A] " is not grounds for rejection. While the questions are phrased in a binary way, we acknowledge that the true answer is often more nuanced, so please just use your best judgment and write a justification to elaborate. All supporting evidence can appear either in the main paper or the supplemental material, provided in appendix. If you answer [Yes] to a question, in the justification please point to the section(s) where related material for the question can be found.

**ZH** 论文审稿人会被要求把检查清单作为评估的因素之一。虽然「[Yes]」通常比「[No]」更可取，但只要给出恰当的理由，回答「[No]」也完全可以接受（例如「未报告误差棒，因为其计算开销过大」或「我们未能找到所用数据集的许可协议」）。一般而言，回答「[No]」或「[N/A]」并不构成拒稿理由。虽然问题以二选一的方式表述，我们承认真实答案往往更为细致，因此请自行判断并撰写理由加以说明。所有支撑性证据可出现在正文或附录中的补充材料里。若对某个问题回答 [Yes]，请在理由中指明可找到相关内容的章节。

**EN** IMPORTANT, please:

**ZH** 重要提示，请：

**EN** • Delete this instruction block, but keep the section heading “NeurIPS paper checklist",

**ZH** • 删除本说明块，但保留章节标题「NeurIPS paper checklist」，

**EN** • Keep the checklist subsection headings, questions/answers and guidelines below.

**ZH** • 保留检查清单的小节标题、问题/答案与下方指南。

**EN** • Do not modify the questions and only use the provided macros for your answers.

**ZH** • 不要修改问题，且只使用所提供的宏来填写答案。

**EN** 1. Claims

**ZH** 1. 主张

**EN** Question: Do the main claims made in the abstract and introduction accurately reflect the paper’s contributions and scope?

**ZH** 问题：摘要与引言中的主要主张是否准确反映了论文的贡献与范围？

**EN** Answer: [Yes]

**ZH** 答案：[Yes]

**EN** Justification: Yes, the abstract is summary of the content of the paper.

**ZH** 理由：是的，摘要是对论文内容的概括。

**EN** Guidelines: • The answer NA means that the abstract and introduction do not include the claims made in the paper. • The abstract and/or introduction should clearly state the claims made, including the contributions made in the paper and important assumptions and limitations. A No or NA answer to this question will not be perceived well by the reviewers. • The claims made should match theoretical and experimental results, and reflect how much the results can be expected to generalize to other settings. • It is fine to include aspirational goals as motivation as long as it is clear that these goals are not attained by the paper.

**ZH** 指南：• 回答 NA 表示摘要与引言未包含论文所提出的主张。• 摘要和/或引言应清楚陈述所提出的主张，包括论文的贡献与重要假设、局限。对该问题回答 No 或 NA 不会给审稿人留下好印象。• 所提出的主张应与理论与实验结果相符，并反映结果在其他设置下可预期的泛化程度。• 只要明确说明这些目标并未由本论文达成，把愿景性目标作为动机写入是可以的。

**EN** 2. Limitations

**ZH** 2. 局限性

**EN** Question: Does the paper discuss the limitations of the work performed by the authors?

**ZH** 问题：论文是否讨论了作者所完成工作的局限性？

**EN** Answer: [Yes]

**ZH** 答案：[Yes]

**EN** Justification: In the last paragraph of Conclusion section.

**ZH** 理由：在结论部分的最后一段。

**EN** Guidelines: • The answer NA means that the paper has no limitation while the answer No means that the paper has limitations, but those are not discussed in the paper. • The authors are encouraged to create a separate "Limitations" section in their paper. • The paper should point out any strong assumptions and how robust the results are to violations of these assumptions (e.g., independence assumptions, noiseless settings, model well-specification, asymptotic approximations only holding locally). The authors should reflect on how these assumptions might be violated in practice and what the implications would be. • The authors should reflect on the scope of the claims made, e.g., if the approach was only tested on a few datasets or with a few runs. In general, empirical results often depend on implicit assumptions, which should be articulated. • The authors should reflect on the factors that influence the performance of the approach. For example, a facial recognition algorithm may perform poorly when image resolution is low or images are taken in low lighting. Or a speech-to-text system might not be used reliably to provide closed captions for online lectures because it fails to handle technical jargon. • The authors should discuss the computational efficiency of the proposed algorithms and how they scale with dataset size. • If applicable, the authors should discuss possible limitations of their approach to address problems of privacy and fairness. • While the authors might fear that complete honesty about limitations might be used by reviewers as grounds for rejection, a worse outcome might be that reviewers discover limitations that aren’t acknowledged in the paper. The authors should use their best judgment and recognize that individual actions in favor of transparency play an important role in developing norms that preserve the integrity of the community. Reviewers will be specifically instructed to not penalize honesty concerning limitations.

**ZH** 指南：• 回答 NA 表示论文没有局限性，回答 No 表示论文存在局限性但未在文中讨论。• 鼓励作者在论文中单独设立「局限性」一节。• 论文应指出任何强假设，以及结果对这些假设被违背时的稳健程度（例如独立性假设、无噪声设定、模型设定正确、渐近近似仅在局部成立）。作者应反思这些假设在实践中可能被如何违背及其影响。• 作者应反思所提出主张的适用范围，例如该方法是否只在少数数据集上测试过或只运行了少数几次。一般而言，实证结果往往依赖隐含假设，这些假设应被阐明。• 作者应反思影响该方法性能的因素。例如，当图像分辨率较低或拍摄光照不足时，人脸识别算法可能表现不佳；又如，语音转文字系统可能因无法处理专业术语而不能可靠地为在线讲座生成字幕。• 作者应讨论所提出算法的计算效率及其随数据集规模的扩展情况。• 如适用，作者应讨论其方法在解决隐私与公平性问题上可能存在的局限。• 尽管作者可能担心坦诚说明局限性会被审稿人当作拒稿理由，但更糟的结果是审稿人发现了论文未承认的局限性。作者应自行判断，并认识到支持透明度的个人行动对维护学界规范具有重要作用。审稿人会被明确告知，不得因作者坦诚说明局限性而予以惩罚。

**EN** 3. Theory Assumptions and Proofs

**ZH** 3. 理论假设与证明

**EN** Question: For each theoretical result, does the paper provide the full set of assumptions and a complete (and correct) proof?

**ZH** 问题：对每一项理论结果，论文是否给出了完整的假设集合以及完整（且正确）的证明？

**EN** Answer: [N/A]

**ZH** 答案：[N/A]

**EN** Justification: No theoretical results.

**ZH** 理由：没有理论结果。

**EN** Guidelines: • The answer NA means that the paper does not include theoretical results. • All the theorems, formulas, and proofs in the paper should be numbered and cross-referenced. • All assumptions should be clearly stated or referenced in the statement of any theorems. • The proofs can either appear in the main paper or the supplemental material, but if they appear in the supplemental material, the authors are encouraged to provide a short proof sketch to provide intuition. • Inversely, any informal proof provided in the core of the paper should be complemented by formal proofs provided in appendix or supplemental material. • Theorems and Lemmas that the proof relies upon should be properly referenced.

**ZH** 指南：• 回答 NA 表示论文不包含理论结果。• 论文中的所有定理、公式与证明都应编号并交叉引用。• 所有假设都应在任何定理的陈述中被清楚说明或引用。• 证明可出现在正文或补充材料中；若出现在补充材料，鼓励作者提供简短的证明思路以给出直观理解。• 反之，正文中的任何非形式化证明都应由附录或补充材料中的形式化证明加以补充。• 证明所依赖的定理与引理应被恰当引用。

**EN** 4. Experimental Result Reproducibility

**ZH** 4. 实验结果的可复现性

**EN** Question: Does the paper fully disclose all the information needed to reproduce the main experimental results of the paper to the extent that it affects the main claims and/or conclusions of the paper (regardless of whether the code and data are provided or not)?

**ZH** 问题：论文是否充分披露了复现其主要实验结果所需的全部信息（无论代码与数据是否提供），只要这些信息影响到论文的主要主张和/或结论？

**EN** Answer: [Yes]

**ZH** 答案：[Yes]

**EN** Justification: We provide details of training and inference in section 6.

**ZH** 理由：我们在第 6 节提供了训练与推理的细节。

**EN** Guidelines: • The answer NA means that the paper does not include experiments. • If the paper includes experiments, a No answer to this question will not be perceived well by the reviewers: Making the paper reproducible is important, regardless of whether the code and data are provided or not. • If the contribution is a dataset and/or model, the authors should describe the steps taken to make their results reproducible or verifiable. • Depending on the contribution, reproducibility can be accomplished in various ways. For example, if the contribution is a novel architecture, describing the architecture fully might suffice, or if the contribution is a specific model and empirical evaluation, it may be necessary to either make it possible for others to replicate the model with the same dataset, or provide access to the model. In general. releasing code and data is often one good way to accomplish this, but reproducibility can also be provided via detailed instructions for how to replicate the results, access to a hosted model (e.g., in the case of a large language model), releasing of a model checkpoint, or other means that are appropriate to the research performed. • While NeurIPS does not require releasing code, the conference does require all submissions to provide some reasonable avenue for reproducibility, which may depend on the nature of the contribution. For example (a) If the contribution is primarily a new algorithm, the paper should make it clear how to reproduce that algorithm. (b) If the contribution is primarily a new model architecture, the paper should describe the architecture clearly and fully. (c) If the contribution is a new model (e.g., a large language model), then there should either be a way to access this model for reproducing the results or a way to reproduce the model (e.g., with an open-source dataset or instructions for how to construct the dataset). (d) We recognize that reproducibility may be tricky in some cases, in which case authors are welcome to describe the particular way they provide for reproducibility. In the case of closed-source models, it may be that access to the model is limited in some way (e.g., to registered users), but it should be possible for other researchers to have some path to reproducing or verifying the results.

**ZH** 指南：• 回答 NA 表示论文不包含实验。• 若论文包含实验，对该问题回答 No 不会给审稿人留下好印象：无论代码与数据是否提供，论文的可复现性都很重要。• 若贡献是数据集和/或模型，作者应描述为使结果可复现或可验证所采取的步骤。• 依贡献不同，可复现性可通过多种方式实现。例如，若贡献是新颖的架构，充分描述该架构可能已足够；若贡献是特定模型与实证评估，则可能需要让他人能够用同一数据集复现该模型，或提供对该模型的访问。一般而言，发布代码与数据往往是实现这一点的一个好办法，但可复现性也可通过如下方式提供：如何复现结果的详细说明、对托管模型的访问（如大语言模型的情形）、发布模型检查点，或其他适合该研究的方式。• 尽管 NeurIPS 不要求发布代码，会议确实要求所有投稿提供某种合理的可复现途径，这可能取决于贡献的性质。例如：(a) 若贡献主要是新算法，论文应清楚说明如何复现该算法。(b) 若贡献主要是新的模型架构，论文应清楚、完整地描述该架构。(c) 若贡献是新模型（例如某个大语言模型），那么应当要么提供访问该模型以复现结果的途径，要么提供复现该模型的途径（例如开源数据集或如何构建该数据集的说明）。(d) 我们承认在某些情况下可复现性可能较为棘手，此时欢迎作者描述其提供的特定可复现方式。对于闭源模型，模型的访问可能受到某种限制（例如仅限注册用户），但其他研究者仍应有途径复现或验证结果。

**EN** 5. Open access to data and code

**ZH** 5. 数据与代码的开放获取

**EN** Question: Does the paper provide open access to the data and code, with sufficient instructions to faithfully reproduce the main experimental results, as described in supplemental material?

**ZH** 问题：论文是否如补充材料所述，提供了对数据与代码的开放访问，并附有足以忠实复现主要实验结果的说明？

**EN** Answer: [Yes]

**ZH** 答案：[Yes]

**EN** Justification: We will release the data and code and benchmark once accepted.

**ZH** 理由：论文被接收后我们将发布数据、代码与基准。

**EN** Guidelines: • The answer NA means that paper does not include experiments requiring code. • Please see the NeurIPS code and data submission guidelines (https://nips.cc/public/guides/CodeSubmissionPolicy) for more details. • While we encourage the release of code and data, we understand that this might not be possible, so “No” is an acceptable answer. Papers cannot be rejected simply for not including code, unless this is central to the contribution (e.g., for a new open-source benchmark). • The instructions should contain the exact command and environment needed to run to reproduce the results. See the NeurIPS code and data submission guidelines (https://nips.cc/public/guides/CodeSubmissionPolicy) for more details. • The authors should provide instructions on data access and preparation, including how to access the raw data, preprocessed data, intermediate data, and generated data, etc. • The authors should provide scripts to reproduce all experimental results for the new proposed method and baselines. If only a subset of experiments are reproducible, they should state which ones are omitted from the script and why. • At submission time, to preserve anonymity, the authors should release anonymized versions (if applicable). • Providing as much information as possible in supplemental material (appended to the paper) is recommended, but including URLs to data and code is permitted.

**ZH** 指南：• 回答 NA 表示论文不包含需要代码的实验。• 更多细节请参见 NeurIPS 代码与数据提交指南（https://nips.cc/public/guides/CodeSubmissionPolicy）。• 尽管我们鼓励发布代码与数据，我们也理解这并非总能实现，因此回答「No」也是可接受的；论文不能仅因未包含代码而被拒稿，除非代码对贡献而言是核心的（例如一个新的开源基准）。• 说明中应包含复现结果所需的确切命令与环境，详见 NeurIPS 代码与数据提交指南。• 作者应提供数据访问与准备的说明，包括如何获取原始数据、预处理数据、中间数据与生成数据等。• 作者应提供脚本以复现所提新方法基线的所有实验结果；若只有部分实验可复现，应说明哪些被省略及原因。• 投稿时为保持匿名，作者应发布匿名版本（如适用）。• 建议在补充材料（附于论文后）中提供尽可能多的信息，但也允许包含数据与代码的 URL。

**EN** 6. Experimental Setting/Details

**ZH** 6. 实验设置/细节

**EN** Question: Does the paper specify all the training and test details (e.g., data splits, hyperparameters, how they were chosen, type of optimizer, etc.) necessary to understand the results?

**ZH** 问题：论文是否说明了理解结果所需的全部训练与测试细节（如数据划分、超参数、超参数的选择方式、优化器类型等）？

**EN** Answer: [Yes]

**ZH** 答案：[Yes]

**EN** Justification: yes, provided in section 5 and 6.

**ZH** 理由：是的，见第 5 节与第 6 节。

**EN** Guidelines: • The answer NA means that the paper does not include experiments. • The experimental setting should be presented in the core of the paper to a level of detail that is necessary to appreciate the results and make sense of them. • The full details can be provided either with the code, in appendix, or as supplemental material.

**ZH** 指南：• 回答 NA 表示论文不包含实验。• 实验设置应在正文中以达到理解结果、读懂结果所必需的详尽程度呈现。• 完整细节可随代码提供、置于附录，或作为补充材料。

**EN** 7. Experiment Statistical Significance

**ZH** 7. 实验的统计显著性

**EN** Question: Does the paper report error bars suitably and correctly defined or other appropriate information about the statistical significance of the experiments?

**ZH** 问题：论文是否恰当、正确地报告了误差棒，或其他关于实验统计显著性的适当信息？

**EN** Answer: [No]

**ZH** 答案：[No]

**EN** Justification: We simply benchmark existing available models, with greedy decoding for MLLMs e.g. Idefics2 and fixing seed for foundation models e.g. CLIP.

**ZH** 理由：我们只是对现有可用模型做基准评测，对 Idefics2 等 MLLM 采用贪心解码，对 CLIP 等基座型模型固定随机种子。

**EN** Guidelines: • The answer NA means that the paper does not include experiments. • The authors should answer "Yes" if the results are accompanied by error bars, confidence intervals, or statistical significance tests, at least for the experiments that support the main claims of the paper. • The factors of variability that the error bars are capturing should be clearly stated (for example, train/test split, initialization, random drawing of some parameter, or overall run with given experimental conditions). • The method for calculating the error bars should be explained (closed form formula, call to a library function, bootstrap, etc.) • The assumptions made should be given (e.g., Normally distributed errors). • It should be clear whether the error bar is the standard deviation or the standard error of the mean. • It is OK to report 1-sigma error bars, but one should state it. The authors should preferably report a 2-sigma error bar than state that they have a 96% CI, if the hypothesis of Normality of errors is not verified. • For asymmetric distributions, the authors should be careful not to show in tables or figures symmetric error bars that would yield results that are out of range (e.g. negative error rates). • If error bars are reported in tables or plots, The authors should explain in the text how they were calculated and reference the corresponding figures or tables in the text.

**ZH** 指南：• 回答 NA 表示论文不包含实验。• 若结果附有误差棒、置信区间或统计显著性检验，作者应回答「Yes」，至少对支撑论文主要主张的实验如此。• 误差棒所刻画的可变性因素应被清楚说明（例如训练/测试划分、初始化、某些参数的随机抽样，或在给定实验条件下的整体运行）。• 误差棒的计算方法应加以解释（闭式公式、调用库函数、自助法等）。• 应给出所作假设（例如误差服从正态分布）。• 应明确误差棒是标准差还是均值的标准误。• 报告 1-sigma 误差棒是可以的，但应加以说明；若误差正态性假设未经验证，作者最好报告 2-sigma 误差棒，而不是声称 96% 置信区间。• 对于非对称分布，作者应注意不要在表格或图中展示会超出取值范围的对称误差棒（例如负的错误率）。• 若在表格或图中报告误差棒，作者应在正文中说明其计算方式，并引用相应的图或表。

**EN** 8. Experiments Compute Resources

**ZH** 8. 实验计算资源

**EN** Question: For each experiment, does the paper provide sufficient information on the computer resources (type of compute workers, memory, time of execution) needed to reproduce the experiments?

**ZH** 问题：对每个实验，论文是否提供了复现实验所需计算资源（计算节点类型、内存、执行时间）的充分信息？

**EN** Answer: [No]

**ZH** 答案：[No]

**EN** Justification: We perform the task with one gpu, as it’s simple benchmarking and finetuning.

**ZH** 理由：我们用一块 GPU 完成该任务，因为它只是简单的基准评测与微调。

**EN** Guidelines: • The answer NA means that the paper does not include experiments. • The paper should indicate the type of compute workers CPU or GPU, internal cluster, or cloud provider, including relevant memory and storage. • The paper should provide the amount of compute required for each of the individual experimental runs as well as estimate the total compute. • The paper should disclose whether the full research project required more compute than the experiments reported in the paper (e.g., preliminary or failed experiments that didn’t make it into the paper).

**ZH** 指南：• 回答 NA 表示论文不包含实验。• 论文应说明计算节点的类型：CPU 还是 GPU、内部集群还是云服务商，包括相关的内存与存储。• 论文应提供每次单独实验运行所需的计算量，并估算总计算量。• 论文应披露整个研究项目所需的计算是否超过论文所报告的实验（例如未收入论文的预研或失败实验）。

**EN** 9. Code Of Ethics

**ZH** 9. 伦理准则

**EN** Question: Does the research conducted in the paper conform, in every respect, with the NeurIPS Code of Ethics https://neurips.cc/public/EthicsGuidelines?

**ZH** 问题：论文所开展的研究是否在各方面都符合 NeurIPS 伦理准则 https://neurips.cc/public/EthicsGuidelines？

**EN** Answer: [Yes]

**ZH** 答案：[Yes]

**EN** Justification: Yes, we do.

**ZH** 理由：是的，我们符合。

**EN** Guidelines: • The answer NA means that the authors have not reviewed the NeurIPS Code of Ethics. • If the authors answer No, they should explain the special circumstances that require a deviation from the Code of Ethics. • The authors should make sure to preserve anonymity (e.g., if there is a special consideration due to laws or regulations in their jurisdiction).

**ZH** 指南：• 回答 NA 表示作者未审阅 NeurIPS 伦理准则。• 若作者回答 No，应解释需要偏离伦理准则的特殊情况。• 作者应确保保持匿名（例如因所在司法辖区的法律法规而有特殊考量时）。

**EN** 10. Broader Impacts

**ZH** 10. 更广泛的影响

**EN** Question: Does the paper discuss both potential positive societal impacts and negative societal impacts of the work performed?

**ZH** 问题：论文是否讨论了所完成工作潜在的积极与消极社会影响？

**EN** Answer: [N/A]

**ZH** 答案：[N/A]

**EN** Justification: No relevant.

**ZH** 理由：不相关。

**EN** Guidelines: • The answer NA means that there is no societal impact of the work performed. • If the authors answer NA or No, they should explain why their work has no societal impact or why the paper does not address societal impact. • Examples of negative societal impacts include potential malicious or unintended uses (e.g., disinformation, generating fake profiles, surveillance), fairness considerations (e.g., deployment of technologies that could make decisions that unfairly impact specific groups), privacy considerations, and security considerations. • The conference expects that many papers will be foundational research and not tied to particular applications, let alone deployments. However, if there is a direct path to any negative applications, the authors should point it out. For example, it is legitimate to point out that an improvement in the quality of generative models could be used to generate deepfakes for disinformation. On the other hand, it is not needed to point out that a generic algorithm for optimizing neural networks could enable people to train models that generate Deepfakes faster. • The authors should consider possible harms that could arise when the technology is being used as intended and functioning correctly, harms that could arise when the technology is being used as intended but gives incorrect results, and harms following from (intentional or unintentional) misuse of the technology. • If there are negative societal impacts, the authors could also discuss possible mitigation strategies (e.g., gated release of models, providing defenses in addition to attacks, mechanisms for monitoring misuse, mechanisms to monitor how a system learns from feedback over time, improving the efficiency and accessibility of ML).

**ZH** 指南：• 回答 NA 表示所完成的工作没有社会影响。• 若作者回答 NA 或 No，应解释其工作为何没有社会影响，或论文为何不涉及社会影响。• 消极社会影响的例子包括潜在的恶意或意外用途（例如虚假信息、生成伪造账号、监控）、公平性考量（例如所部署技术的决策可能对特定群体产生不公影响）、隐私考量与安全考量。• 会议预期许多论文属于基础研究，并不与特定应用挂钩，更遑论部署。但若存在通向任何消极应用的直接路径，作者应予以指出。例如，指出生成模型质量提升可能被用于制造深度伪造以传播虚假信息是合理的；但无需指出某个通用的神经网络优化算法可能让人更快地训练出可生成深度伪造的模型。• 作者应考虑技术按预期用途正确运行时可能产生的危害、按预期用途使用但给出错误结果时可能产生的危害，以及技术被（有意或无意）滥用所导致的危害。• 若存在消极社会影响，作者还可讨论可能的缓解策略（例如模型的受限发布、在攻击之外提供防御、监控滥用的机制、监控系统随时间推移如何从反馈中学习的机制、提升机器学习的可及性与效率）。

**EN** 11. Safeguards

**ZH** 11. 保障措施

**EN** Question: Does the paper describe safeguards that have been put in place for responsible release of data or models that have a high risk for misuse (e.g., pretrained language models, image generators, or scraped datasets)?

**ZH** 问题：论文是否描述了为负责任地发布具有高滥用风险的数据或模型（例如预训练语言模型、图像生成器或抓取的数据集）所采取的保障措施？

**EN** Answer: [N/A]

**ZH** 答案：[N/A]

**EN** Justification: No relevant.

**ZH** 理由：不相关。

**EN** Guidelines: • The answer NA means that the paper poses no such risks. • Released models that have a high risk for misuse or dual-use should be released with necessary safeguards to allow for controlled use of the model, for example by requiring that users adhere to usage guidelines or restrictions to access the model or implementing safety filters. • Datasets that have been scraped from the Internet could pose safety risks. The authors should describe how they avoided releasing unsafe images. • We recognize that providing effective safeguards is challenging, and many papers do not require this, but we encourage authors to take this into account and make a best faith effort.

**ZH** 指南：• 回答 NA 表示论文不存在此类风险。• 具有较高滥用或双重用途风险的已发布模型，应配备必要的保障措施以实现受控使用，例如要求用户遵守使用准则或限制对模型的访问，或实施安全过滤。• 从互联网抓取的数据集可能带来安全风险，作者应说明如何避免发布不安全的图像。• 我们认识到提供有效的保障措施具有挑战性，许多论文也并不要求如此，但我们鼓励作者考虑这一点并尽最大努力。

**EN** 12. Licenses for existing assets

**ZH** 12. 已有资产的许可

**EN** Question: Are the creators or original owners of assets (e.g., code, data, models), used in the paper, properly credited and are the license and terms of use explicitly mentioned and properly respected?

**ZH** 问题：论文所用资产（如代码、数据、模型）的创作者或原始所有者是否得到了恰当的署名，许可与使用条款是否被明确提及并得到妥善遵守？

**EN** Answer: [Yes]

**ZH** 答案：[Yes]

**EN** Justification: We follow protocol.

**ZH** 理由：我们遵循了规范。

**EN** Guidelines: • The answer NA means that the paper does not use existing assets. • The authors should cite the original paper that produced the code package or dataset. • The authors should state which version of the asset is used and, if possible, include a URL. • The name of the license (e.g., CC-BY 4.0) should be included for each asset. • For scraped data from a particular source (e.g., website), the copyright and terms of service of that source should be provided. • If assets are released, the license, copyright information, and terms of use in the package should be provided. For popular datasets, paperswithcode.com/datasets has curated licenses for some datasets. Their licensing guide can help determine the license of a dataset. • For existing datasets that are re-packaged, both the original license and the license of the derived asset (if it has changed) should be provided. • If this information is not available online, the authors are encouraged to reach out to the asset’s creators.

**ZH** 指南：• 回答 NA 表示论文未使用已有资产。• 作者应引用产出该代码包或数据集的原始论文。• 作者应说明所使用资产的版本，如可能还应包含 URL。• 应为每项资产给出许可名称（例如 CC-BY 4.0）。• 对于从特定来源（例如网站）抓取的数据，应提供该来源的版权与服务条款。• 若发布了资产，应在包中提供许可、版权信息与使用条款。对于热门数据集，paperswithcode.com/datasets 已整理部分数据集的许可，其许可指南可帮助确定数据集的许可。• 对于重新打包的已有数据集，应同时提供原始许可与衍生资产的许可（若有变更）。• 若这些信息无法在线获得，鼓励作者联系资产的创作者。

**EN** 13. New Assets

**ZH** 13. 新资产

**EN** Question: Are new assets introduced in the paper well documented and is the documentation provided alongside the assets?

**ZH** 问题：论文引入的新资产是否有完善的文档，且文档是否与资产一同提供？

**EN** Answer: [Yes]

**ZH** 答案：[Yes]

**EN** Justification: We provide comprehensive analysis of our new benchmark and will release soon.

**ZH** 理由：我们对新基准做了全面分析，并将很快发布。

**EN** Guidelines: • The answer NA means that the paper does not release new assets. • Researchers should communicate the details of the dataset/code/model as part of their submissions via structured templates. This includes details about training, license, limitations, etc. • The paper should discuss whether and how consent was obtained from people whose asset is used. • At submission time, remember to anonymize your assets (if applicable). You can either create an anonymized URL or include an anonymized zip file.

**ZH** 指南：• 回答 NA 表示论文未发布新资产。• 研究者应在投稿中通过结构化模板传达数据集/代码/模型的细节，包括训练、许可、局限等。• 论文应讨论是否以及如何获得了资产使用者的同意。• 投稿时请记得对资产做匿名化处理（如适用）：可以创建匿名 URL，或提供匿名压缩包。

**EN** 14. Crowdsourcing and Research with Human Subjects

**ZH** 14. 众包与涉及人类受试者的研究

**EN** Question: For crowdsourcing experiments and research with human subjects, does the paper include the full text of instructions given to participants and screenshots, if applicable, as well as details about compensation (if any)?

**ZH** 问题：对于众包实验与涉及人类受试者的研究，论文是否包含了提供给参与者的完整说明文本、截图（如适用），以及报酬细节（如有）？

**EN** Answer: [Yes]

**ZH** 答案：[Yes]

**EN** Justification: We provide in Appendix.

**ZH** 理由：我们在附录中提供。

**EN** Guidelines: • The answer NA means that the paper does not involve crowdsourcing nor research with human subjects. • Including this information in the supplemental material is fine, but if the main contribution of the paper involves human subjects, then as much detail as possible should be included in the main paper. • According to the NeurIPS Code of Ethics, workers involved in data collection, curation, or other labor should be paid at least the minimum wage in the country of the data collector.

**ZH** 指南：• 回答 NA 表示论文不涉及众包或人类受试者研究。• 把这些信息放在补充材料中是可以的；但如果论文的主要贡献涉及人类受试者，则应在正文中尽可能详细地呈现。• 根据 NeurIPS 伦理准则，参与数据采集、整理或其他劳动的工作者，应获得不低于数据收集者所在国最低工资的报酬。

**EN** 15. Institutional Review Board (IRB) Approvals or Equivalent for Research with Human Subjects

**ZH** 15. 机构审查委员会（IRB）批准或涉及人类受试者研究的等效审批

**EN** Question: Does the paper describe potential risks incurred by study participants, whether such risks were disclosed to the subjects, and whether Institutional Review Board (IRB) approvals (or an equivalent approval/review based on the requirements of your country or institution) were obtained?

**ZH** 问题：论文是否描述了研究参与者可能面临的风险、这些风险是否已向受试者披露，以及是否获得了机构审查委员会（IRB）批准（或依据所在国家/机构要求的等效批准/审查）？

**EN** Answer: [N/A]

**ZH** 答案：[N/A]

**EN** Justification: Not relevant.

**ZH** 理由：不相关。

**EN** Guidelines: • The answer NA means that the paper does not involve crowdsourcing nor research with human subjects. • Depending on the country in which research is conducted, IRB approval (or equivalent) may be required for any human subjects research. If you obtained IRB approval, you should clearly state this in the paper. • We recognize that the procedures for this may vary significantly between institutions and locations, and we expect authors to adhere to the NeurIPS Code of Ethics and the guidelines for their institution. • For initial submissions, do not include any information that would break anonymity (if applicable), such as the institution conducting the review.

**ZH** 指南：• 回答 NA 表示论文不涉及众包或人类受试者研究。• 依研究开展所在国家的不同，任何人类受试者研究都可能需要 IRB 批准（或等效审批）。若已获得 IRB 批准，应在论文中明确说明。• 我们认识到相关程序在不同机构与地区之间可能差异很大，我们期望作者遵守 NeurIPS 伦理准则及其所在机构的规定。• 初次投稿时，请勿包含任何会破坏匿名性的信息（如适用），例如实施审查的机构名称。
