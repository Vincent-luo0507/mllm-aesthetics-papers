# AesCanvas：一个面向美学评论与上下文适配性的大规模数据集与基准

> 原标题：AesCanvas: A Large-Scale Dataset and Benchmark for Aesthetic Critique and Contextual Suitability
> 作者：Xuanwei Hu, Haoyu Dong, Kejun Wu, Tianyi Liu, Jianjun Gao · arXiv:2608.26713 · 2026-08-27

<!-- [原子块 · verbatim] AesCanvas: A Large-Scale Dataset and Benchmark for Aesthetic Critique and Contextual Suitability -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] Recent advances in Multimodal Large Language Models (MLLMs) have extended Image Aesthetic Assessment (IAA) beyond scalar scores toward interpretable critique and guidance. Yet existing benchmarks main -->

**EN** 1School of Electronic Information and Communications, Huazhong University of Science and Technology, Wuhan, China

**ZH** 1华中科技大学电子信息与通信学院，中国武汉

**EN** 2School of Electrical and Electronic Engineering, Nanyang Technological University, Singapore

**ZH** 2南洋理工大学电气与电子工程学院，新加坡

**EN** kjwu@hust.edu.cn

**ZH** kjwu@hust.edu.cn

**EN** I Introduction

**ZH** I 引言

**EN** Image Aesthetic Assessment (IAA) has progressed from scalar prediction and preference modeling (Murray et al. 2012; Talebi and Milanfar 2018; Yi et al. 2023) toward language-based aesthetic perception, critique, diagnosis, and guidance (Huang et al. 2024b; Huang et al. 2024a; Zhou et al. 2024; Zhang et al. 2025; Qi et al. 2025b; Cao et al. 2025b). In practical use, however, visual appeal alone is insufficient: an image must also suit a particular purpose, audience, and convention. Cultural knowledge is therefore not auxiliary to aesthetic judgment, since symbols, styles, dress, and genre conventions can directly change whether an image is an appropriate visual choice. Related multimodal studies likewise show that models remain fragile when judgments require criterion-sensitive reasoning, visual grounding, or culturally situated evidence (Xiong et al. 2026; Li et al. 2026; Wu et al. 2026b; Satar et al. 2025; Singh et al. 2026).

**ZH** 图像美学评估（IAA）已从标量预测与偏好建模（Murray et al. 2012; Talebi and Milanfar 2018; Yi et al. 2023）推进到基于语言的美学感知、评论、诊断与指导（Huang et al. 2024b; Huang et al. 2024a; Zhou et al. 2024; Zhang et al. 2025; Qi et al. 2025b; Cao et al. 2025b）。然而在实际应用中，仅有视觉吸引力并不够：图像还必须契合特定的目的、受众与惯例。文化知识因此并非美学判断的辅助项，因为符号、风格、服饰与体裁惯例会直接改变一张图像是否构成恰当的视觉选择。相关的多模态研究同样表明，当判断需要准则敏感的推理、视觉定位或文化情境化的证据时，模型依然脆弱（Xiong et al. 2026; Li et al. 2026; Wu et al. 2026b; Satar et al. 2025; Singh et al. 2026）。

<!-- [原子块 · img]  -->

**EN** Figure 1: Fluent aesthetic critique does not guarantee contextually valid judgment. The top example shows an evidence-grounded critique, whereas the bottom shows a suitability error in which visually appealing attributes are mistaken for appropriateness in a mismatched use context. This contrast motivates evaluating critique grounding and contextual suitability as complementary capabilities.

**ZH** 图 1：流畅的美学评论并不能保证上下文有效的判断。上方示例给出一段有证据支撑的评论，下方则给出一个适配性错误：视觉上吸引人的属性被误当作在错配使用场景下的恰当性。这一对比促使我们把评论的定位与上下文适配性作为互补能力来评测。

**EN** Figure 1 makes this distinction concrete: a model may produce a plausible aesthetic critique yet approve a mourning dress as festive evening wear by emphasizing its silhouette and material while ignoring its social function. Figure 2 further reveals two failure levels: critiques may rely on fabricated evidence or inappropriate domain priors, while suitability judgments may privilege surface appeal or stylistic plausibility over cultural fit. We call the latter tendency aesthetic context bias: following generic aesthetic priors while

**ZH** 图 1 把这一区别具体化：模型可能产出一段貌似合理的美学评论，却因为强调廓形与材质而忽视社会功能，把一件丧服认可为喜庆的晚宴着装。图 2 进一步揭示了两类失败层次：评论可能依赖编造的证据或不恰当的领域先验，而适配性判断则可能把表面吸引力或风格上的合理性置于文化契合之上。我们把后一种倾向称为美学上下文偏置：遵循通用美学先验，

<!-- [原子块 · img]  -->

**EN** Figure 2: Four recurring failure modes in practical aesthetic evaluation. Models may generate critiques that are visually ungrounded or rely on inappropriate domain priors, and may judge real-world suitability from surface aesthetics or stylistic plausibility rather than communicative and contextual fit.

**ZH** 图 2：实际美学评测中四种反复出现的失败模式。模型可能生成缺乏视觉依据的评论，或依赖不恰当的领域先验；也可能依据表面美学或风格上的合理性、而非传播与上下文契合，来判断真实场景中的适配性。

**EN** neglecting contextual evidence that should alter the decision. This task is not generic cultural question answering; contextual knowledge matters because it determines whether the image works as a visual choice.

**ZH** 却忽视本应改变判断的上下文证据。这一任务并非泛化的文化问答；上下文知识之所以重要，是因为它决定了图像作为视觉选择能否成立。

**EN** To study both capabilities, we introduce AesCanvas, a unified suite with two complementary components. CritiqueCanvas provides large-scale, multi-domain supervision for long-form critique across photography, painting, and virtual imagery, while ContextCanvas contains expert-reviewed use scenarios that distinguish visual appeal from contextual suitability. Across closed-source, open-weight, and aesthetic-specific MLLMs, we observe a clear capability gap: aesthetic specialists remain competitive on selected critique metrics, yet all score below 30% on ContextCanvas, compared with 91.69% for the strongest evaluated general-purpose model. Further analyses show that reference-based metrics only partially capture critique quality, aesthetic specialization does not reliably transfer to contextual judgment, and correct decisions may still lack grounding in decisive visual evidence.

**ZH** 为研究这两种能力，我们提出 AesCanvas，一个包含两个互补组件的统一套件。CritiqueCanvas 提供跨摄影、绘画与虚拟图像的大规模多领域监督，用于长篇评论；ContextCanvas 则包含经专家评审的使用场景，用于区分视觉吸引力与上下文适配性。在闭源、开源权重与美学专用 MLLM 上，我们观察到一道清晰的能力鸿沟：美学专用模型在部分评论指标上仍有竞争力，但在 ContextCanvas 上全部低于 30%，而最强的通用模型达到 91.69%。进一步分析表明，基于参考的指标只能部分刻画评论质量，美学专精并不能可靠迁移到上下文判断，并且正确的决策也可能缺乏对决定性视觉证据的定位。

**EN** Contributions. (1) We introduce CritiqueCanvas, comprising 519,136 aesthetic instruction–response pairs built from 54,300 multi-domain images for instruction-tuning MLLMs on fine-grained image aesthetic assessment; (2) we construct ContextCanvas, a 301-case expert-curated benchmark for contextual aesthetic suitability judgment; (3) we evaluate closed-source, open-weight, and aesthetic-specific MLLMs, revealing a clear gap between producing fluent aesthetic critiques and correctly judging suitability under cultural, functional, and domain-specific constraints; and (4) we release the data, prompts, rationales, provenance records, and evaluation code.

**ZH** 贡献如下。（1）我们提出 CritiqueCanvas，包含由 54,300 张多领域图像构建的 519,136 组美学指令-回答对，用于对 MLLM 做细粒度图像美学评估的指令微调；（2）我们构建 ContextCanvas，一个含 301 个案例、由专家策划的上下文美学适配性判断基准；（3）我们评测闭源、开源权重与美学专用 MLLM，揭示了「生成流畅的美学评论」与「在文化、功能与领域特定约束下正确判断适配性」之间的明显差距；（4）我们发布数据、提示、推理依据、来源记录与评测代码。

**EN** II Related Work

**ZH** II 相关工作

<!-- [原子块 · img]  -->

**EN** Figure 3: Construction of AesCanvas. (a) A shared multi-domain image pool is collected and filtered. (b) CritiqueCanvas is generated through dimension-aware prompt planning, MLLM-assisted annotation, and quality filtering. (c) ContextCanvas is constructed from realistic aesthetic-use scenarios followed by expert review.

**ZH** 图 3：AesCanvas 的构建流程。（a）采集并筛选一个共享的多领域图像池。（b）CritiqueCanvas 通过维度感知的提示规划、MLLM 辅助标注与质量过滤生成。（c）ContextCanvas 由真实的美学使用场景出发构建，随后经专家评审。

**EN** A Image Aesthetic Assessment

**ZH** A 图像美学评估

**EN** Image Aesthetic Assessment (IAA) predicts human judgments of visual aesthetic quality. Early work formulated IAA as classification, ranking, or score-distribution prediction from crowd preferences, while incorporating photographic attributes, composition-preserving representations, and individual taste variation (Murray et al. 2012; Kong et al. 2016; Mai et al. 2016; Yang et al. 2022). Recent studies extend IAA to artistic images, fine-grained comparison within image series, and open-world criteria that vary across themes (Yi et al. 2023; Yang et al. 2026b; Liao et al. 2026). Nevertheless, these methods primarily assess aesthetic strength under intrinsic or task-fixed criteria, rather than whether an image is appropriate for a particular purpose, audience, cultural setting, or domain convention. Our work addresses this complementary problem of contextual aesthetic suitability.

**ZH** 图像美学评估（IAA）预测人类对视觉美学质量的判断。早期工作把 IAA 形式化为分类、排序或分数分布预测，数据来源是众包偏好，并引入了摄影属性、保持构图的表示以及个体品味差异（Murray et al. 2012; Kong et al. 2016; Mai et al. 2016; Yang et al. 2022）。近期研究把 IAA 扩展到艺术图像、图像序列内的细粒度比较，以及随主题变化的开放世界准则（Yi et al. 2023; Yang et al. 2026b; Liao et al. 2026）。然而，这些方法主要在内在准则或任务固定准则下评估美学强度，而非判断一张图像是否适合特定的目的、受众、文化语境或领域惯例。本文关注的正是上下文美学适配性这一互补问题。

**EN** B Aesthetic Multimodal Models

**ZH** B 美学多模态模型

**EN** Aesthetic multimodal models extend conventional IAA from scalar prediction to language-based recognition, description, interpretation, scoring, and critique. Early studies benchmarked the aesthetic perception of general-purpose MLLMs and explored aesthetic instruction tuning (Huang et al. 2024b; Huang et al. 2024a; Zhou et al. 2024). Subsequent work connected textual supervision with visual scoring through language-defined rating levels or joint scoring-and-interpretation objectives (Wu et al. 2024; Zhang et al. 2025), while more recent models support professional critique, multi-attribute analysis, and unified perceptual assessment (Qi et al. 2025b; Cao et al. 2025b; Cao et al. 2025a). Existing evaluation, however, remains centered on aesthetic perception, scoring, reference-aligned critique, or domain-specific analysis. AesCanvas instead examines whether aesthetic articulation transfers to contextual decisions in which an attractive or stylistically plausible image may still conflict with its intended use. Beyond conventional visual inputs, recent multimodal foundation models have also explored semantic understanding and language generation over specialized or corrupted visual representations (Wu et al. 2026a; Liang et al. 2026).

**ZH** 美学多模态模型把传统 IAA 从标量预测扩展到基于语言的识别、描述、解读、评分与评论。早期工作对通用 MLLM 的美学感知做基准测试，并探索美学指令微调（Huang et al. 2024b; Huang et al. 2024a; Zhou et al. 2024）。后续工作通过语言定义的评分等级或评分与解读的联合目标，把文本监督与视觉评分连接起来（Wu et al. 2024; Zhang et al. 2025）；更近期的模型支持专业评论、多属性分析与统一的感知评估（Qi et al. 2025b; Cao et al. 2025b; Cao et al. 2025a）。然而现有评测仍以美学感知、评分、与参考对齐的评论或领域特定分析为中心。AesCanvas 转而考察美学表述能否迁移到上下文决策中——在这些决策里，一张好看的或风格上合理的图像仍可能与其预期用途相冲突。除常规视觉输入外，近期的多模态基础模型还探索了对专用或受损视觉表示的语义理解与语言生成（Wu et al. 2026a; Liang et al. 2026）。

**EN** C Contextual Multimodal Reasoning

**ZH** C 上下文多模态推理

**EN** Contextual multimodal reasoning requires models to combine visual evidence with task conditions, external knowledge, cultural conventions, and criterion-specific constraints. Recent benchmarks study real-world visual reasoning, context-dependent functional inference, and flexible judgment under varying criteria (Yin et al. 2026; Zhang et al. 2026; Xiong et al. 2026; Gao et al. 2024). Grounding-focused work further evaluates whether intermediate reasoning and final answers are supported by localized image evidence (Li et al. 2026; Wu et al. 2026b; Cai et al. 2024), while other studies expose failures under visual illusions, counterfactual or adversarial evidence, and conflicts between knowledge and images (Hou et al. 2026; Zhou et al. 2026; Moratelli et al. 2026). Culturally situated benchmarks likewise reveal fragility on region-specific artifacts and multilingual cultural evidence (Satar et al. 2025; Singh et al. 2026). However, these works primarily assess factual correctness, grounding, functional inference, or adherence to specified criteria, rather than whether contextual evidence should outweigh surface aesthetic appeal in a concrete visual-use decision. ContextCanvas targets this intersection through use-oriented aesthetic suitability judgments grounded in both visual and contextual evidence.

**ZH** 上下文多模态推理要求模型把视觉证据与任务条件、外部知识、文化惯例以及准则特定约束结合起来。近期基准研究真实世界的视觉推理、依赖上下文的功能推断，以及在变化准则下的灵活判断（Yin et al. 2026; Zhang et al. 2026; Xiong et al. 2026; Gao et al. 2024）。以定位为核心的工作进一步评估中间推理与最终答案是否得到局部化图像证据的支持（Li et al. 2026; Wu et al. 2026b; Cai et al. 2024）；另一些研究则暴露了模型在视觉错觉、反事实或对抗性证据，以及知识与图像冲突下的失败（Hou et al. 2026; Zhou et al. 2026; Moratelli et al. 2026）。文化情境化基准同样揭示了模型在区域特定器物与多语言文化证据上的脆弱性（Satar et al. 2025; Singh et al. 2026）。然而，这些工作主要评估事实正确性、定位、功能推断或对给定准则的遵循，而非在具体视觉使用决策中，上下文证据是否应当压过表面美学吸引力。ContextCanvas 正是通过同时基于视觉证据与上下文证据的、面向使用的美学适配性判断来瞄准这一交汇点。

**EN** III Dataset

**ZH** III 数据集

**EN** A Dataset Overview

**ZH** A 数据集概览

**EN** We introduce AesCanvas, a unified suite built from 54,300 images to study two complementary aspects of aesthetic intelligence: articulating visual qualities and judging their suitability in context. CritiqueCanvas contains 519,136 instruction–response pairs across photography, painting, and virtual imagery for long-form, multi-dimensional critique generation. ContextCanvas comprises 301 expert-designed and reviewed cases that evaluate contextual aesthetic suitability—whether an image is an appropriate visual choice for a specified purpose, audience, cultural setting, or domain convention, beyond its intrinsic visual appeal. Together, the two components test whether models that can identify and articulate aesthetic evidence can also translate it into contextually valid decisions.

**ZH** 我们提出 AesCanvas，一个由 54,300 张图像构建的统一套件，用于研究美学智能的两个互补侧面：表述视觉品质，以及在上下文中判断其适配性。CritiqueCanvas 包含跨摄影、绘画与虚拟图像的 519,136 组指令-回答对，用于长篇、多维度的评论生成。ContextCanvas 包含 301 个由专家设计并评审的案例，评估上下文美学适配性——即一张图像在超越其内在视觉吸引力之外，是否是针对特定目的、受众、文化语境或领域惯例的恰当视觉选择。两个组件共同检验：能够识别并表述美学证据的模型，是否也能把这些证据转化为上下文有效的决策。

**EN** B Dataset Curation

**ZH** B 数据整理

**EN** As illustrated in Fig. 3, our pipeline branches from a shared multi-domain image pool into CritiqueCanvas for structured aesthetic critique and ContextCanvas for closed-form contextual suitability judgment.

**ZH** 如图 3 所示，我们的流程从一个共享的多领域图像池分出两支：一支进入 CritiqueCanvas 做结构化美学评论，另一支进入 ContextCanvas 做封闭形式的上下文适配性判断。

**EN** Image Collection and Filtering.

**ZH** 图像采集与过滤。

**EN** We collect candidate images from three visual domains: photography (e.g., natural scenes, architecture, portraiture, and commercial imagery), painting (primarily Western classical and related works), and virtual imagery (e.g., game scenes, animation-style images, and AI-generated content). Images are drawn from publicly accessible web sources and online museum and cultural-heritage collections, with available source URLs and provenance metadata retained. After removing low-quality, semantically uninformative, non-compliant, and duplicate samples, the pool contains 21,294 photographs, 17,939 paintings, and 15,067 virtual images, for a total of 54,300.

**ZH** 我们从三个视觉域采集候选图像：摄影（如自然场景、建筑、肖像与商业影像）、绘画（主要为西方古典及相关作品）与虚拟图像（如游戏场景、动画风格图像与 AI 生成内容）。图像取自可公开访问的网络来源以及在线博物馆与文化遗产收藏，并保留可获得的来源 URL 与出处元数据。在剔除低质量、语义无信息量、不合规与重复的样本后，图像池包含 21,294 张照片、17,939 幅绘画与 15,067 张虚拟图像，合计 54,300。

**EN** CritiqueCanvas Annotation and Construction.

**ZH** CritiqueCanvas 的标注与构建。

**EN** As shown in Fig. 3(b), we use a prompt-based pipeline that combines shared aesthetic dimensions with domain-specific criteria. The shared dimensions include Content and Narrative, Composition, Color, Lighting, Lines and Brushstrokes, Style, Emotion, Technique, Symbolism, and Visual Appeal. Annotating models select only the dimensions most relevant to each image rather than addressing all dimensions uniformly.

**ZH** 如图 3(b) 所示，我们采用一条基于提示的流程，把共享的美学维度与领域特定准则结合起来。共享维度包括内容与叙事、构图、色彩、光影、线条与笔触、风格、情绪、技法、象征与视觉吸引力。标注模型只挑选与每张图像最相关的维度，而不是对所有维度做统一处理。

**EN** Prompts are further conditioned on the visual domain. Photography emphasizes exposure, perspective, depth of field, focus, motion, and compositional control; painting emphasizes line, brushwork, genre, style, symbolism, and emotional expression; and virtual imagery emphasizes character design, scene construction, rendering consistency, narrative setting, and stylization. Multiple MLLMs generate structured annotations, which are converted into multi-turn instruction–response conversations covering description, evaluation, interpretation, technical analysis, and constructive improvement.

**ZH** 提示进一步以视觉域为条件。摄影强调曝光、透视、景深、对焦、动态与构图控制；绘画强调线条、笔法、体裁、风格、象征与情绪表达；虚拟图像强调角色设计、场景构建、渲染一致性、叙事设定与风格化。多个 MLLM 生成结构化标注，这些标注被转换为多轮指令-回答对话，覆盖描述、评价、解读、技术分析与建设性改进。

**EN** An independent Claude Opus 5 verifier screens generated pairs for instruction consistency, visual grounding, and response quality. A stratified audit of 1,000 retained pairs yields 95.3% acceptance and 97% raw agreement; full criteria and statistics appear in the supplement.

**ZH** 一个独立的 Claude Opus 5 校验器对生成的配对筛查指令一致性、视觉定位与回答质量。对 1,000 组保留配对的分层审计得到 95.3% 的接受率与 97% 的原始一致率；完整准则与统计见补充材料。

**EN** ContextCanvas Construction and Review.

**ZH** ContextCanvas 的构建与评审。

**EN** As shown in Fig. 3(c), ContextCanvas is constructed from a selected subset of the shared image pool. Four PhD-level researchers with interdisciplinary backgrounds developed and reviewed 1,060 candidate cases. Each places an image in a plausible use scenario—such as exhibition, publication, advertising, education, commemoration, or public communication—and asks whether it is an appropriate visual choice for the stated purpose, audience, and context. Some cases include a curator- or designer-proposed assessment that the model must independently evaluate.

**ZH** 如图 3(c) 所示，ContextCanvas 从共享图像池的一个精选子集构建。四位具有跨学科背景的博士级研究者开发并评审了 1,060 个候选案例。每个案例把一张图像置于一个可信的使用场景——如展览、出版、广告、教育、纪念或公共传播——并询问它对于所述目的、受众与语境是否是恰当的视觉选择。部分案例还包含一段由策展人或设计师提出的评估，模型须独立加以评判。

**EN** A case is retained only when it satisfies seven prespecified criteria: (1) aesthetic centrality, requiring a judgment about the image as a visual choice; (2) context dependence, such that intrinsic quality alone is insufficient; (3) visual necessity, such that the task cannot be reduced to text-only factual or cultural knowledge; (4) decisive evidence, such that relevant cultural, historical, or narrative evidence materially affects the answer; (5) scenario naturalness, requiring a plausible design or communication use; (6) answerability, requiring a unique closed-form answer from perceptible evidence; and (7) anti-shortcut validity, preventing wording, option length, or label priors from revealing the answer.

**ZH** 一个案例只有在满足七项预设准则时才被保留：（1）美学中心性，要求对图像作为视觉选择做出判断；（2）上下文依赖性，即仅凭内在品质不足以定论；（3）视觉必要性，即任务不能退化为纯文本的事实或文化知识；（4）决定性证据，即相关的文化、历史或叙事证据实质影响答案；（5）场景自然性，要求一个可信的设计或传播用途；（6）可回答性，要求从可感知证据得出唯一的封闭形式答案；（7）反捷径有效性，防止措辞、选项长度或标签先验泄露答案。

**EN** All candidates were reviewed against these criteria, with borderline cases resolved through discussion. Qwen3.7-Plus was used only as a development-time probe for trivial, ambiguous, or shortcut-prone cases; model failure alone never determined retention. All inclusion decisions, gold labels, rationales, and source records were finalized solely by human reviewers, and its reported score is therefore marked as a development-model diagnostic.

**ZH** 所有候选都对照这些准则评审，边界案例通过讨论裁决。Qwen3.7-Plus 仅作为开发期的探针，用于筛查过于简单、含糊或易走捷径的案例；模型失败本身从不决定保留与否。所有纳入决策、金标签、推理依据与来源记录均由人工评审者最终确定，因此其报告的分数被标注为开发模型诊断值。

**EN** The final benchmark contains 301 cases (28.40%): 300 single-image and one paired-image case, covering 302 images, 291 binary questions, and 10 three-way questions. Each includes the visual input, use scenario, context, answer options, gold label, source-grounded rationale, and provenance. The cases span painting, sculpture, illustration and comics, animation and digital imagery, photography, and film.

**ZH** 最终基准包含 301 个案例（28.40%）：300 个单图案例与 1 个成对图像案例，覆盖 302 张图像、291 道二元问题与 10 道三选一问题。每个案例都包含视觉输入、使用场景、上下文、答案选项、金标签、基于来源的推理依据与出处信息。案例横跨绘画、雕塑、插画与漫画、动画与数字图像、摄影与电影。

<!-- [原子块 · table] Task Metric Family Metrics Critique Lexical overlap BLEU, ROUGE-L, METEOR Semantic similarity BERT-F1, SBERT-Cos Image–text alignment CLIPScore Descriptive statistics Avg. Length, Avg. Dim. Hits, Top- -->

**EN** Table 1: Metrics used for the two evaluation tasks.

**ZH** 表 1：两项评测任务所使用的指标。

**EN** C Evaluation Protocol

**ZH** C 评测协议

**EN** We evaluate critique generation on CritiqueCanvas and contextual suitability on ContextCanvas. Models receive identical inputs and instructions without web search, retrieval, or auxiliary recognition tools; Table 1 summarizes the metrics.

**ZH** 我们在 CritiqueCanvas 上评测评论生成，在 ContextCanvas 上评测上下文适配性。模型接收相同的输入与指令，不使用网络搜索、检索或辅助识别工具；表 1 汇总了所用指标。

<!-- [原子块 · table] Model Acc. Macro-F1 Yes (%) Closed-source MLLMs Claude Opus 5 91.69 90.45 30.24 Gemini 3.1 Pro 85.71 83.06 26.12 GPT-5.5 83.06 80.13 27.49 Claude Opus 4.6 72.76 67.96 27.15 GPT-5.2 71.43 64.51 20.96 G -->

**EN** Table 2: Contextual aesthetic suitability results. Acc. is exact-match accuracy on all 301 cases. Macro-F1 and Yes (%) are computed on the 291 binary cases; the gold Yes rate is 38.14%. Best Acc. and Macro-F1 are bolded. ⟦SLOT_0⟧ denotes the development model used for difficulty screening.

**ZH** 表 2：上下文美学适配性结果。Acc. 为全部 301 个案例上的精确匹配准确率。Macro-F1 与 Yes (%) 在 291 个二元案例上计算，金标准 Yes 率为 38.14%。最佳 Acc. 与 Macro-F1 以粗体标出。⟦SLOT_0⟧ 表示用于难度筛查的开发模型。

**EN** Long-form Aesthetic Critique Generation.

**ZH** 长篇美学评论生成。

**EN** We evaluate models on 6,000 open-ended samples balanced across photography, painting, and virtual imagery, requiring aesthetic analysis or image-grounded improvement suggestions. Image-level splits keep related conversations together.

**ZH** 我们在 6,000 个开放式样本上评测模型，样本在摄影、绘画与虚拟图像间均衡分布，要求给出美学分析或基于图像的改进建议。图像级划分把相关对话保持在一起。

**EN** Because valid critiques may differ substantially in wording, we report complementary metric families. BLEU (Papineni et al. 2002), ROUGE-L (Lin 2004), and METEOR (Banerjee and Lavie 2005) measure lexical overlap; BERT-F1 (Zhang et al. 2020) and SBERT-Cos (Reimers and Gurevych 2019) measure token- and sentence-level semantic similarity; and CLIPScore (Hessel et al. 2021) measures image–text relevance. These metrics are interpreted jointly rather than as complete measures of aesthetic reasoning.

**ZH** 由于有效的评论在措辞上可能差别很大，我们报告互补的多族指标。BLEU（Papineni et al. 2002）、ROUGE-L（Lin 2004）与 METEOR（Banerjee and Lavie 2005）度量词汇重叠；BERT-F1（Zhang et al. 2020）与 SBERT-Cos（Reimers and Gurevych 2019）度量词元级与句子级的语义相似度；CLIPScore（Hessel et al. 2021）度量图文相关性。这些指标需联合解读，而非作为美学推理的完整度量。

**EN** To further characterize response behavior, we report average response length, average aesthetic-dimension coverage, and the three most frequently addressed dimensions in the supplementary material. Specifically, let ⟦SLOT_1⟧ denote the predefined set of aesthetic dimensions, and let ⟦SLOT_2⟧ indicate whether response ⟦SLOT_3⟧ explicitly addresses dimension ⟦SLOT_4⟧. The average number of dimensions addressed per response is

**ZH** 为进一步刻画回答行为，我们在补充材料中报告平均回答长度、平均美学维度覆盖率，以及被提及最多的三个维度。具体地，令 ⟦SLOT_1⟧ 表示预定义的美学维度集合，⟦SLOT_2⟧ 指示回答 ⟦SLOT_3⟧ 是否明确涉及维度 ⟦SLOT_4⟧。每条回答涉及的维度平均数为

<!-- [原子块 · table] DimHits = 1 N ​ ∑ i = 1 N ∑ d ∈ 𝒟 m ⁡ ( r ^ i , d ) . \mathrm{DimHits}=\frac{1}{N}\sum_{i=1}^{N}\sum_{d\in\mathcal{D}}m(\hat{r}_{i},d). (1) -->

**EN** This statistic measures the breadth of explicit aesthetic coverage rather than its correctness: a higher value does not necessarily indicate that the identified dimensions are relevant, accurate, or well grounded.

**ZH** 该统计量度量的是美学覆盖的广度而非其正确性：取值更高并不必然意味着所识别的维度相关、准确或有据可依。

**EN** Contextual Aesthetic Suitability Judgment.

**ZH** 上下文美学适配性判断。

**EN** For each ContextCanvas case, the model receives an image, a realistic use scenario, and fixed answer options, and returns a single option label. Explanations are retained for qualitative analysis but do not affect the primary score. A prediction is correct only if a unique option is parsed and matches the gold answer; missing, conflicting, or unparsable responses are counted as incorrect.

**ZH** 对每个 ContextCanvas 案例，模型接收一张图像、一个真实使用场景与固定的答案选项，并返回一个选项标签。解释内容会保留用于定性分析，但不影响主分数。只有当解析出唯一选项且与金答案匹配时，预测才计为正确；缺失、冲突或无法解析的回答计为错误。

**EN** We report exact-match accuracy over all 301 cases. Macro-F1 and predicted Yes Rate are computed on the 291 binary cases after mapping the options to canonical Yes/No labels; the remaining 10 three-way cases are included only in accuracy. The gold Yes Rate is 38.14%, against which the predicted rate indicates a model’s tendency toward over-acceptance or over-rejection.

**ZH** 我们报告全部 301 个案例上的精确匹配准确率。Macro-F1 与预测 Yes 率在 291 个二元案例上计算，计算时把选项映射到规范的 Yes/No 标签；其余 10 道三选一问题只计入准确率。金标准 Yes 率为 38.14%，把预测率与之对照可反映模型过度接受或过度拒绝的倾向。

**EN** IV Experiments

**ZH** IV 实验

**EN** A Experimental Setup

**ZH** A 实验设置

**EN** Evaluated Models.

**ZH** 评测模型。

**EN** We compare closed-source frontier MLLMs, open-weight general MLLMs, and aesthetic-specific models, separating general visual-language capability from specialization for aesthetic assessment or critique. Exact model variants are listed in Tables 2 and 3. Qwen3-VLFT denotes a variant adapted on CritiqueCanvas and evaluated only on critique generation.

**ZH** 我们比较闭源前沿 MLLM、开源权重通用 MLLM 与美学专用模型，以区分通用视觉语言能力与面向美学评估或评论的专精化。具体模型变体列于表 2 与表 3。Qwen3-VLFT 表示在 CritiqueCanvas 上适配的变体，只参与评论生成评测。

**EN** Implementation Details.

**ZH** 实现细节。

**EN** All models follow the protocol in Section III.C. Locally deployed models receive images resized or padded to ⟦SLOT_5⟧ pixels. We use deterministic decoding whenever supported and a maximum of 256 tokens for critique generation; model-specific settings are reported in the supplementary material.

**ZH** 所有模型遵循第 III.C 节的协议。本地部署的模型接收缩放或填充到 ⟦SLOT_5⟧ 像素的图像。只要支持，我们一律使用确定性解码，评论生成最多 256 个词元；各模型的专属设置见补充材料。

<!-- [原子块 · table] Model BLEU ROUGE-L METEOR BERT-F1 SBERT-Cos CLIPScore Closed-source MLLMs Gemini 3.1 Pro 7.15 0.250 0.281 0.699 0.848 0.303 GPT-5.2 2.84 0.210 0.209 0.669 0.818 0.301 Open-weight General MLLMs GLM-4.6 -->

**EN** Table 3: Quantitative evaluation of long-form aesthetic critique generation on CritiqueCanvas. The reported metrics assess complementary aspects of generated critiques, including reference alignment through lexical and semantic similarity, and image–text relevance.

**ZH** 表 3：CritiqueCanvas 上长篇美学评论生成的定量评测。所报告的指标评估生成评论的互补侧面，包括通过词汇与语义相似度衡量的参考对齐度，以及图文相关性。

**EN** B Main Results

**ZH** B 主要结果

**EN** Contextual Aesthetic Suitability Judgment

**ZH** 上下文美学适配性判断

**EN** Table 2 reports results on ContextCanvas. The benchmark clearly separates model capability levels. Accuracy among closed-source MLLMs ranges from ⟦SLOT_6⟧ to ⟦SLOT_7⟧, while the strongest evaluated open-weight model, Qwen3-VL-Instruct, reaches only ⟦SLOT_8⟧. Within the Claude and GPT families, newer variants substantially outperform their predecessors: Claude Opus 5 improves over Claude Opus 4.6 by ⟦SLOT_9⟧ accuracy points and ⟦SLOT_10⟧ Macro-F1 points, while GPT-5.5 improves over GPT-5.2 by ⟦SLOT_11⟧ and ⟦SLOT_12⟧ points, respectively. These within-family gains are consistent with improved contextual aesthetic judgment in newer frontier models.

**ZH** 表 2 报告了 ContextCanvas 上的结果。该基准清晰地区分了模型的能力层级。闭源 MLLM 的准确率介于 ⟦SLOT_6⟧ 到 ⟦SLOT_7⟧ 之间，而最强的开源权重模型 Qwen3-VL-Instruct 只达到 ⟦SLOT_8⟧。在 Claude 与 GPT 系列内部，较新的变体大幅优于其前代：Claude Opus 5 相对 Claude Opus 4.6 提升 ⟦SLOT_9⟧ 个准确率点与 ⟦SLOT_10⟧ 个 Macro-F1 点，GPT-5.5 相对 GPT-5.2 分别提升 ⟦SLOT_11⟧ 与 ⟦SLOT_12⟧ 个点。这些系列内的增益与较新前沿模型上下文美学判断能力的提升相一致。

**EN** Most notably, all evaluated aesthetic-specific models achieve below ⟦SLOT_13⟧ accuracy. ArtQuant-APDD, the strongest model in this group, obtains ⟦SLOT_14⟧, compared with ⟦SLOT_15⟧ for Qwen3-VL-Instruct and ⟦SLOT_16⟧ for Claude Opus 5. ArtiMuse, Q-SiT, and AesExpert achieve only ⟦SLOT_17⟧, ⟦SLOT_18⟧, and ⟦SLOT_19⟧, respectively. Thus, specialization for aesthetic scoring, perception, or critique does not reliably transfer to judging suitability under cultural, communicative, or domain-specific constraints.

**ZH** 最值得注意的是，所有被评测的美学专用模型的准确率都低于 ⟦SLOT_13⟧。该组中最强的 ArtQuant-APDD 取得 ⟦SLOT_14⟧，而 Qwen3-VL-Instruct 为 ⟦SLOT_15⟧，Claude Opus 5 为 ⟦SLOT_16⟧。ArtiMuse、Q-SiT 与 AesExpert 分别只取得 ⟦SLOT_17⟧、⟦SLOT_18⟧ 与 ⟦SLOT_19⟧。因此，面向美学评分、感知或评论的专精化并不能可靠迁移到在文化、传播或领域特定约束下判断适配性。

**EN** The Yes-rate column further reveals a shared prediction tendency. Against the gold rate of ⟦SLOT_20⟧, aesthetic-specific models predict Yes in ⟦SLOT_21⟧–⟦SLOT_22⟧ of the binary cases, indicating pronounced over-acceptance despite contextual mismatch. This pattern is consistent with aesthetic context bias, although similar marginal rates may arise from different instance-level failures. We examine these failure modes through category-level and qualitative analyses in the following section. Although the binary subset has a ⟦SLOT_23⟧ always-No majority baseline, weaker models often fall below it because they over-accept visually plausible but contextually unsuitable images. Meanwhile, frontier models achieve up to ⟦SLOT_24⟧ accuracy on the full benchmark, suggesting that ContextCanvas rewards context-sensitive judgment rather than majority-label guessing.

**ZH** Yes 率一栏进一步揭示了一种共同的预测倾向。相对 ⟦SLOT_20⟧ 的金标准率，美学专用模型在二元案例中预测 Yes 的比例达 ⟦SLOT_21⟧–⟦SLOT_22⟧，说明即便存在上下文错配也呈现出明显的过度接受。这一模式与美学上下文偏置相符，尽管相近的边缘比例也可能源自不同的实例级失败。我们将在下一节通过类别级与定性分析考察这些失败模式。虽然二元子集存在 ⟦SLOT_23⟧ 的「恒为 No」多数基线，较弱的模型常常低于它，因为它们会过度接受视觉上合理但上下文不适用的图像。与此同时，前沿模型在完整基准上最高达到 ⟦SLOT_24⟧ 的准确率，说明 ContextCanvas 奖励的是上下文敏感的判断，而非猜测多数标签。

**EN** Long-form Aesthetic Critique Generation

**ZH** 长篇美学评论生成

**EN** Table 3 reports results on CritiqueCanvas. No model dominates across all metric families. Gemini 3.1 Pro achieves the highest SBERT-Cos (⟦SLOT_25⟧), while LLaVA-OneVision leads BERT-F1 (⟦SLOT_26⟧) and CLIPScore (⟦SLOT_27⟧). The adapted Qwen3-VLFT instead obtains the strongest lexical scores: ⟦SLOT_28⟧ BLEU, ⟦SLOT_29⟧ ROUGE-L, and ⟦SLOT_30⟧ METEOR. Compared with the base Qwen3-VL, these correspond to gains of ⟦SLOT_31⟧, ⟦SLOT_32⟧, and ⟦SLOT_33⟧, respectively. However, its SBERT-Cos decreases from ⟦SLOT_34⟧ to ⟦SLOT_35⟧, and CLIPScore from ⟦SLOT_36⟧ to ⟦SLOT_37⟧, showing that adaptation improves reference-style matching without uniform gains in semantic similarity or image grounding.

**ZH** 表 3 报告了 CritiqueCanvas 上的结果。没有哪个模型在所有指标族上都占优。Gemini 3.1 Pro 取得最高的 SBERT-Cos（⟦SLOT_25⟧），LLaVA-OneVision 在 BERT-F1（⟦SLOT_26⟧）与 CLIPScore（⟦SLOT_27⟧）上领先。适配后的 Qwen3-VLFT 则取得最强的词汇类分数：BLEU ⟦SLOT_28⟧、ROUGE-L ⟦SLOT_29⟧、METEOR ⟦SLOT_30⟧。相比基座 Qwen3-VL，这分别对应 ⟦SLOT_31⟧、⟦SLOT_32⟧ 与 ⟦SLOT_33⟧ 的增益。然而其 SBERT-Cos 从 ⟦SLOT_34⟧ 降至 ⟦SLOT_35⟧，CLIPScore 从 ⟦SLOT_36⟧ 降至 ⟦SLOT_37⟧，说明适配改善了与参考风格的匹配，却没有在语义相似度或图像定位上带来一致提升。

**EN** Aesthetic-specific models remain competitive on selected critique metrics. ArtiMuse reaches ⟦SLOT_38⟧ BERT-F1, close to the best score of ⟦SLOT_39⟧, while UniPercept obtains a CLIPScore of ⟦SLOT_40⟧, only ⟦SLOT_41⟧ below the overall best. ArtQuant also reaches ⟦SLOT_42⟧ BLEU and ⟦SLOT_43⟧ ROUGE-L, whereas AesExpert and Q-SiT perform weakly across most metrics. Overall critique performance is heterogeneous across lexical, semantic, and image-grounding criteria.

**ZH** 美学专用模型在部分评论指标上仍有竞争力。ArtiMuse 达到 ⟦SLOT_38⟧ 的 BERT-F1，接近 ⟦SLOT_39⟧ 的最佳值；UniPercept 取得 ⟦SLOT_40⟧ 的 CLIPScore，仅比全局最佳低 ⟦SLOT_41⟧。ArtQuant 也达到 ⟦SLOT_42⟧ 的 BLEU 与 ⟦SLOT_43⟧ 的 ROUGE-L，而 AesExpert 与 Q-SiT 在多数指标上表现较弱。总体而言，评论性能在词汇、语义与图像定位三类准则上呈现出异质性。

**EN** Together, the two tasks reveal a gap between reference-aligned critique generation and contextually valid aesthetic judgment. Additional response-level statistics are provided in the supplementary material.

**ZH** 两项任务共同揭示了「与参考对齐的评论生成」与「上下文有效的美学判断」之间的鸿沟。更多的回答级统计见补充材料。

**EN** C Analysis

**ZH** C 分析

**EN** Beyond aggregate scores, we examine why aesthetic competence fails to transfer to culturally situated judgment. In the compact tables, GPT, Gem., Qwen+, Qwen-FT, AQ, and AM abbreviate GPT-5.2, Gemini 3.1 Pro, Qwen3.7-Plus, the CritiqueCanvas-adapted Qwen3-VL, ArtQuant-APDD, and ArtiMuse, respectively; vertical rules follow the model groups in Section IV.A.

**ZH** 除总分之外，我们考察美学能力为何无法迁移到文化情境化的判断中。在简表中，GPT、Gem.、Qwen+、Qwen-FT、AQ 与 AM 分别是 GPT-5.2、Gemini 3.1 Pro、Qwen3.7-Plus、在 CritiqueCanvas 上适配的 Qwen3-VL、ArtQuant-APDD 与 ArtiMuse 的缩写；竖线分隔遵循第 IV.A 节的模型分组。

<!-- [原子块 · table] Rating GPT Gem. Qwen3-VL FT AM AQ Human 3.9 4.1 2.5 2.6 2.3 MLLM 5.0 4.5 2.5 2.6 2.2 -->

**EN** Table 4: Human and MLLM ratings of overall critique quality.

**ZH** 表 4：人类与 MLLM 对评论整体质量的评分。

<!-- [原子块 · table] Metric GPT Gem. Qwen+ AQ AM Correct ↑ \uparrow 13 10 11 3 6 Reverse ↓ \downarrow 2 1 1 2 0 NCU ↑ \uparrow 30.56 25.00 27.78 2.78 16.67 -->

**EN** Table 5: Results of the 36-pair counterfactual audit.

**ZH** 表 5：36 对反事实审计的结果。

**EN** Validity of Critique Metrics

**ZH** 评论指标的有效性

**EN** We evaluate whether reference-based metrics reflect practical critique quality on 100 randomly sampled CritiqueCanvas cases. 2 human evaluators rate five representative models on visual grounding, aesthetic specificity, criterion appropriateness, and analytical usefulness, with Claude Opus 5 as the MLLM judge providing a complementary assessment.

**ZH** 我们在 100 个随机抽样的 CritiqueCanvas 案例上评估基于参考的指标是否反映实用的评论质量。2 位人类评估者对五个代表性模型在视觉定位、美学具体性、准则恰当性与分析有用性上打分，并由 Claude Opus 5 作为 MLLM 裁判提供互补评估。

**EN** As shown in Table 5, direct quality ratings do not consistently track the reference-similarity metrics in Table 3. Since valid critiques may emphasize different evidence and interpretations, lexical and semantic overlap capture only part of critique quality and should be complemented by direct judgments of grounding, specificity, and usefulness.

**ZH** 如表 5 所示，直接质量评分并不能一贯地跟随表 3 中的参考相似度指标。由于有效的评论可能强调不同的证据与解读，词汇与语义重叠只捕获了评论质量的一部分，还应当辅以对定位、具体性与有用性的直接判断。

**EN** Culture-Grounded Counterfactual Sensitivity

**ZH** 文化定位的反事实敏感性

**EN** We further examine whether contextual aesthetic decisions are grounded in culture-bearing visual evidence. We construct 36 paired counterfactual variants from ContextCanvas, keeping the evaluation scenario and overall visual presentation fixed while changing the decisive cue such that the intended judgment changes from No to Yes. These synthetic variants neither revise the original annotations nor constitute an additional accuracy split; they are used only as a matched diagnostic of directional decision updating. We report the numbers of correct (No⟦SLOT_44⟧ Yes) and reverse (Yes⟦SLOT_45⟧No) updates, as well as Net Correct Update computed as ⟦SLOT_46⟧.

**ZH** 我们进一步考察上下文美学决策是否以承载文化的视觉证据为依据。我们从 ContextCanvas 构造了 36 组配对的反事实变体：保持评测场景与整体视觉呈现不变，只改变决定性线索，使预期判断由 No 变为 Yes。这些合成变体既不修订原始标注，也不构成额外的准确率划分；它们仅用作方向性决策更新的配对诊断。我们报告正确（No⟦SLOT_44⟧Yes）与反向（Yes⟦SLOT_45⟧No）更新的数量，以及按 ⟦SLOT_46⟧ 计算的净正确更新（Net Correct Update）。

**EN** As shown in Table 5, all three general-purpose MLLMs show positive net updating, with NCU values concentrated between 25.00 and 30.56 despite their substantially different benchmark accuracies. This suggests that absolute contextual competence and responsiveness to decisive visual evidence are related but separable. More importantly, both evaluated aesthetic specialists show weaker net updating than every general-purpose model, with ArtQuant exhibiting almost no measurable response. The results indicate that aesthetic specialization alone does not establish the visual–cultural binding required for reliable contextual aesthetic judgment.

**ZH** 如表 5 所示，三个通用 MLLM 都表现出正的净更新，NCU 值集中在 25.00 到 30.56 之间，尽管它们的基准准确率相差很大。这说明绝对的上下文能力与对决定性视觉证据的响应能力相关但可分离。更重要的是，两个被评测的美学专用模型的净更新都弱于每一个通用模型，其中 ArtQuant 几乎没有可测量的响应。结果表明，仅有美学专精并不能建立可靠上下文美学判断所需的视觉-文化绑定。

**EN** Transfer from Aesthetic Specialization

**ZH** 美学专精化的迁移

**EN** To test whether specialization for conventional aesthetic tasks transfers to contextual suitability judgment, we compare each aesthetic specialist with its corresponding base model on the same ContextCanvas cases.

**ZH** 为检验面向传统美学任务的专精化能否迁移到上下文适配性判断，我们在相同的 ContextCanvas 案例上，把每个美学专用模型与其对应的基座模型做比较。

<!-- [原子块 · object]  -->

**EN** Figure 4: Cross-task analysis. (a) Base–specialist transfer on ContextCanvas; * denotes Bonferroni-corrected McNemar ⟦SLOT_47⟧. (b) ContextCanvas accuracy against the mean percentile over six CritiqueCanvas metrics.

**ZH** 图 4：跨任务分析。（a）ContextCanvas 上的基座-专用模型迁移；* 表示经 Bonferroni 校正的 McNemar ⟦SLOT_47⟧。（b）ContextCanvas 准确率相对 CritiqueCanvas 六项指标平均百分位的关系。

**EN** As shown in Figure 4, specialization significantly improves ArtQuant and AesExpert over their respective base models, but yields no measurable gain for ArtiMuse or Q-SiT. Moreover, strong CritiqueCanvas metric alignment does not consistently translate into ContextCanvas accuracy.

**ZH** 如图 4 所示，专精化显著改善了 ArtQuant 与 AesExpert（相对各自基座），但对 ArtiMuse 或 Q-SiT 没有可测量的增益。此外，在 CritiqueCanvas 指标上对齐度高并不能一贯地转化为 ContextCanvas 上的准确率。

<!-- [原子块 · table] Metric Gem. GPT Qwen+ AM Accuracy ↑ \uparrow 83 65 42 21 EGA ↑ \uparrow 79 55 31 3 Unsupported ↓ \downarrow 4.82 15.38 26.19 85.71 -->

**EN** Table 6: Decisive-cue attribution on 100 balanced cases.

**ZH** 表 6：100 个均衡案例上的决定性线索归因。

**EN** Decisive-Cue Grounding

**ZH** 决定性线索定位

**EN** Binary accuracy does not show whether a model is correct for the right visual reason. We therefore evaluate 100 balanced ContextCanvas cases using human judgments of answer correctness, decisive-cue identification, and contextual explanation. Evidence-Grounded Accuracy (EGA) requires all three.

**ZH** 二元准确率并不能说明模型是否出于正确的视觉理由而答对。因此我们在 100 个均衡的 ContextCanvas 案例上，用人类判断评估答案正确性、决定性线索识别与上下文解释。证据定位准确率（EGA）要求三者同时满足。

**EN** As shown in Table 6, general-purpose models preserve much of their accuracy under the stricter grounding criterion, whereas ArtiMuse drops from 21% accuracy to 3% EGA. Unsupported is the percentage of correct predictions that fail the decisive-cue grounding criterion. This gap indicates that fluent aesthetic rationales may still fail to identify the culture-bearing evidence that determines contextual suitability.

**ZH** 如表 6 所示，通用模型在更严格的定位准则下保留了其大部分准确率，而 ArtiMuse 则从 21% 的准确率跌到 3% 的 EGA。Unsupported 指未能通过决定性线索定位准则的正确预测所占百分比。这一差距说明，流畅的美学推理仍可能未能识别出决定上下文适配性的、承载文化的证据。

**EN** V Conclusion

**ZH** V 结论

**EN** We introduced AesCanvas, comprising CritiqueCanvas and ContextCanvas, to evaluate aesthetic critique and contextual suitability. Across closed-source, open-weight, and aesthetic-specific models, strong critique performance does not reliably translate into context-sensitive judgment: aesthetic specialists may remain competitive on critique metrics yet achieve low accuracy and exhibit over-acceptance on ContextCanvas. Paired and diagnostic analyses further reveal inconsistent benefits from aesthetic tuning and limited use of decisive contextual evidence. These findings support treating culturally situated suitability as a distinct training and evaluation objective that requires models to integrate visual evidence with cultural knowledge, intended use, and domain-specific constraints.

**ZH** 我们提出 AesCanvas（包含 CritiqueCanvas 与 ContextCanvas），用于评测美学评论与上下文适配性。在闭源、开源权重与美学专用模型上，强劲的评论性能并不能可靠转化为上下文敏感的判断：美学专用模型可能在评论指标上仍有竞争力，却在 ContextCanvas 上准确率偏低并表现出过度接受。配对分析与诊断分析进一步揭示了美学微调收益的不一致，以及对决定性上下文证据的有限使用。这些发现支持把文化情境化的适配性作为一个独立的训练与评测目标，它要求模型把视觉证据与文化知识、预期用途及领域特定约束结合起来。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] An et al. (2025) X. An, Y. Xie, K. Yang, W. Zhang, X. Zhao, Z. Cheng, Y. Wang, S. Xu, C. Chen, D. Zhu, C. Wu, H. Tan, C. Li, J. Yang, J. Yu, X. Wang, B. Qin, Y. Wang, Z. Yan, Z. Feng, Z. Liu, B. Li, a -->

<!-- [原子块 · verbatim] Bai et al. (2025) S. Bai, Y. Cai, R. Chen, K. Chen, X. Chen, Z. Cheng, L. Deng, W. Ding, C. Gao, C. Ge, W. Ge, Z. Guo, Q. Huang, J. Huang, F. Huang, B. Hui, S. Jiang, Z. Li, M. Li, M. Li, K. Li, Z. Li -->

<!-- [原子块 · verbatim] Banerjee and Lavie (2005) S. Banerjee and A. Lavie METEOR: an automatic metric for MT evaluation with improved correlation with human judgments . In Proceedings of the ACL Workshop on Intrinsic and Ex -->

<!-- [原子块 · verbatim] Bird et al. (2009) S. Bird, E. Klein, and E. Loper Natural language processing with python . O’Reilly Media . Cited by: §S2.3.2 . -->

<!-- [原子块 · verbatim] Cai et al. (2024) C. Cai, R. Zhang, J. Gao, K. Wu, K. Yap, and Y. Wang Temporal sentence grounding with temporally global textual knowledge . In 2024 IEEE International Conference on Multimedia and Ex -->

<!-- [原子块 · verbatim] Cao et al. (2025a) S. Cao, J. Li, X. Li, Y. Pu, K. Zhu, Y. Gao, S. Luo, Y. Xin, Q. Qin, Y. Zhou, X. Chen, W. Zhang, B. Fu, Y. Qiao, and Y. Liu UniPercept: towards unified perceptual-level image unders -->

<!-- [原子块 · verbatim] Cao et al. (2025b) S. Cao, N. Ma, J. Li, X. Li, L. Shao, K. Zhu, Y. Zhou, Y. Pu, J. Wu, J. Wang, B. Qu, W. Wang, Y. Qiao, D. Yao, and Y. Liu ArtiMuse: fine-grained image aesthetics assessment with joi -->

<!-- [原子块 · verbatim] Cao et al. (2025c) S. Cao, N. Ma, J. Li, X. Li, L. Shao, K. Zhu, Y. Zhou, Y. Pu, J. Wu, J. Wang, B. Qu, W. Wang, Y. Qiao, D. Yao, and Y. Liu ArtiMuse: Fine-Grained Image Aesthetics Assessment with Joi -->

<!-- [原子块 · verbatim] Chen et al. (2024) D. Chen, R. Chen, S. Zhang, Y. Liu, Y. Wang, H. Zhou, Q. Zhang, Y. Wan, P. Zhou, and L. Sun MLLM-as-a-Judge: assessing multimodal LLM-as-a-judge with vision-language benchmark . arX -->

<!-- [原子块 · verbatim] Chen et al. (2020) L. Chen, X. Yan, J. Xiao, H. Zhang, S. Pu, and Y. Zhuang Counterfactual samples synthesizing for robust visual question answering . In Proceedings of the IEEE/CVF Conference on Comp -->

<!-- [原子块 · verbatim] Dunn (1961) O. J. Dunn Multiple comparisons among means . Journal of the American Statistical Association 56 ( 293 ), pp. 52–64 . External Links: Document Cited by: §S2.3.3 . -->

<!-- [原子块 · verbatim] Efron and Tibshirani (1993) B. Efron and R. J. Tibshirani An introduction to the bootstrap . Chapman and Hall/CRC . External Links: Document Cited by: §S2.3.3 . -->

<!-- [原子块 · verbatim] Gao et al. (2024) J. Gao, K. Yap, K. Wu, D. T. Phan, K. Garg, and B. S. Han Contextual human object interaction understanding from pre-trained large language model . In ICASSP 2024-2024 IEEE Internati -->

<!-- [原子块 · verbatim] GLM-V Team et al. (2026) GLM-V Team, W. Hong, W. Yu, X. Gu, G. Wang, et al. GLM-4.5V and GLM-4.1V-Thinking: towards versatile multimodal reasoning with scalable reinforcement learning . arXiv preprint -->

<!-- [原子块 · verbatim] Hessel et al. (2021) J. Hessel, A. Holtzman, M. Forbes, R. Le Bras, and Y. Choi CLIPScore: a reference-free evaluation metric for image captioning . In Proceedings of the 2021 Conference on Empirical  -->

<!-- [原子块 · verbatim] Hou et al. (2026) W. Hou, W. Liu, H. Hu, X. Sun, S. Yeung-Levy, and H. Fan Seeing is believing? a benchmark for multimodal large language models on visual illusions and anomalies . arXiv preprint arXi -->

<!-- [原子块 · verbatim] Huang et al. (2024a) Y. Huang, X. Sheng, Z. Yang, Q. Yuan, Z. Duan, P. Chen, L. Li, W. Lin, and G. Shi AesExpert: towards multi-modality foundation model for image aesthetics perception . External Lin -->

<!-- [原子块 · verbatim] Huang et al. (2024b) Y. Huang, Q. Yuan, X. Sheng, Z. Yang, H. Wu, P. Chen, Y. Yang, L. Li, and W. Lin AesBench: an expert benchmark for multimodal large language models on image aesthetics perception  -->

<!-- [原子块 · verbatim] Huang et al. (2024c) Y. Huang, Q. Yuan, X. Sheng, Z. Yang, H. Wu, P. Chen, Y. Yang, L. Li, and W. Lin AesBench: An expert benchmark for multimodal large language models on image aesthetics perception  -->

<!-- [原子块 · verbatim] Kong et al. (2016) S. Kong, X. Shen, Z. Lin, R. Mech, and C. C. Fowlkes Photo aesthetics ranking network with attributes and content adaptation . In Computer Vision – ECCV 2016 , Lecture Notes in Comp -->

<!-- [原子块 · verbatim] Li et al. (2024) C. Li, Z. Zhang, H. Wu, W. Sun, X. Min, X. Liu, G. Zhai, and W. Lin AGIQA-3K: an open database for ai-generated image quality assessment . IEEE Transactions on Circuits and Systems fo -->

<!-- [原子块 · verbatim] Li et al. (2026) R. Li, L. Li, S. Ren, H. Tian, S. Gu, S. Li, Z. Yue, Y. Wang, W. Ma, Z. Yang, J. Ma, Z. Sui, and F. Luo GroundingME: exposing the visual grounding gap in MLLMs through multi-dimension -->

<!-- [原子块 · verbatim] Liang et al. (2026) J. Liang, K. Wu, X. Hu, and T. Liu Cibic: pixel-free foundation model for robust corrupted image bitstream captioning . Pattern Recognition , pp. 114238 . Cited by: §II.B . -->

<!-- [原子块 · verbatim] Liao et al. (2026) M. Liao, T. Ma, and X. Zhang Open world image aesthetic assessment . In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition Findings , pp. 9791–9801 .  -->

<!-- [原子块 · verbatim] Lin (2004) C. Lin ROUGE: a package for automatic evaluation of summaries . In Text Summarization Branches Out , Barcelona, Spain , pp. 74–81 . External Links: Link Cited by: §III.C , §S2.3.2 . -->

<!-- [原子块 · verbatim] Liu et al. (2024) H. Liu, C. Li, Y. Li, and Y. J. Lee Improved baselines with visual instruction tuning . In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition , pp. 262 -->

<!-- [原子块 · verbatim] Liu et al. (2026) H. Liu, N. Huang, C. Liu, J. Yan, H. Huang, J. Ying, T. Lee, P. Wan, and X. Ji Bridging cognitive gap: Hierarchical description learning for artistic image aesthetics assessment . Ex -->

<!-- [原子块 · verbatim] Liu et al. (2023) Y. Liu, D. Iter, Y. Xu, S. Wang, R. Xu, and C. Zhu G-Eval: NLG evaluation using GPT-4 with better human alignment . In Proceedings of the 2023 Conference on Empirical Methods in Natu -->

<!-- [原子块 · verbatim] Mai et al. (2016) L. Mai, H. Jin, and F. Liu Composition-preserving deep photo aesthetics assessment . In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition , pp. 497–506 .  -->

<!-- [原子块 · verbatim] McNemar (1947) Q. McNemar Note on the sampling error of the difference between correlated proportions or percentages . Psychometrika 12 ( 2 ), pp. 153–157 . External Links: Document Cited by: §S2.3.3  -->

<!-- [原子块 · verbatim] Moratelli et al. (2026) N. Moratelli, C. Davis, L. F. R. Ribeiro, B. Byrne, and G. Iglesias Benchmarking deflection and hallucination in large vision-language models . arXiv preprint arXiv:2604.12033  -->

<!-- [原子块 · verbatim] Murray et al. (2012) N. Murray, L. Marchesotti, and F. Perronnin AVA: a large-scale database for aesthetic visual analysis . In Proceedings of the IEEE Conference on Computer Vision and Pattern Recogn -->

<!-- [原子块 · verbatim] Papineni et al. (2002) K. Papineni, S. Roukos, T. Ward, and W. Zhu Bleu: a method for automatic evaluation of machine translation . In Proceedings of the 40th Annual Meeting of the Association for Com -->

<!-- [原子块 · verbatim] Post (2018) M. Post A call for clarity in reporting BLEU scores . In Proceedings of the Third Conference on Machine Translation: Research Papers , pp. 186–191 . External Links: Document Cited by: §S2. -->

<!-- [原子块 · verbatim] Qi et al. (2025a) D. Qi, H. Zhao, J. Shi, S. Jenni, Y. Fan, F. Dernoncourt, S. Cohen, and S. Li The photographer eye: teaching multimodal large language models to see and critique like photographers . -->

<!-- [原子块 · verbatim] Qi et al. (2025b) D. Qi, H. Zhao, J. Shi, S. Jenni, Y. Fan, F. Dernoncourt, S. Cohen, and S. Li The photographer’s eye: teaching multimodal large language models to see, and critique like photographer -->

<!-- [原子块 · verbatim] Reimers and Gurevych (2019) N. Reimers and I. Gurevych Sentence-BERT: sentence embeddings using Siamese BERT-networks . In Proceedings of the 2019 Conference on Empirical Methods in Natural Language P -->

<!-- [原子块 · verbatim] Satar et al. (2025) B. Satar, Z. Ma, P. A. Irawan, W. A. Mulyawan, J. Jiang, E. Lim, and C. Ngo Seeing culture: a benchmark for visual reasoning and grounding . In Proceedings of the 2025 Conference o -->

<!-- [原子块 · verbatim] Singh et al. (2026) D. Singh, A. Nagrani, K. Manikantan, H. Singh, D. Tewari, T. Weyand, C. Schmid, A. Angelova, and S. Dave CURVE: a benchmark for cultural and multilingual long video reasoning . arX -->

<!-- [原子块 · verbatim] Talebi and Milanfar (2018) H. Talebi and P. Milanfar NIMA: neural image assessment . IEEE Transactions on Image Processing 27 ( 8 ), pp. 3998–4011 . External Links: Document Cited by: §I . -->

<!-- [原子块 · verbatim] Wang et al. (2023) J. Wang, H. Duan, J. Liu, S. Chen, X. Min, and G. Zhai AIGCIQA2023: a large-scale image quality assessment database for ai generated images: from the perspectives of quality, authen -->

<!-- [原子块 · verbatim] Wang et al. (2025) W. Wang, Z. Gao, L. Gu, H. Pu, L. Cui, X. Wei, Z. Liu, L. Jing, S. Ye, J. Shao, Z. Wang, Z. Chen, H. Zhang, G. Yang, H. Wang, Q. Wei, J. Yin, W. Li, E. Cui, G. Chen, Z. Ding, C. Tia -->

<!-- [原子块 · verbatim] Wu et al. (2024) H. Wu, Z. Zhang, W. Zhang, C. Chen, L. Liao, C. Li, Y. Gao, A. Wang, E. Zhang, W. Sun, Q. Yan, X. Min, G. Zhai, and W. Lin Q-Align: teaching LMMs for visual scoring via discrete text- -->

<!-- [原子块 · verbatim] Wu et al. (2026a) K. Wu, F. Li, W. Liu, Q. Liu, and Y. Yang Corrupted bitstream semantic understanding by adaptive-modal large language models . Pattern Recognition 180 , pp. 114151 . Cited by: §II.B  -->

<!-- [原子块 · verbatim] Wu et al. (2026b) Q. Wu, X. Yang, Y. Zhou, C. Fang, B. Song, X. Sun, and R. Ji Grounded chain-of-thought for multimodal large language models . In Proceedings of the IEEE/CVF Conference on Computer Vi -->

<!-- [原子块 · verbatim] Xiong et al. (2026) T. Xiong, Y. Ge, M. Li, Z. Zhang, P. Kulkarni, K. Wang, Q. He, Z. Zhu, C. Liu, R. Chen, T. Zheng, Y. Chen, X. Wang, R. Zhang, W. Chen, and H. Huang Multi-Crit: benchmarking multimo -->

<!-- [原子块 · verbatim] Yang et al. (2026a) S. Yang, Y. Liu, B. Zhai, X. Sun, Z. Liu, E. Barsoum, M. Li, and C. Xu CaptionQA: is your caption as useful as the image itself? . In Proceedings of the IEEE/CVF Conference on Comp -->

<!-- [原子块 · verbatim] Yang et al. (2022) Y. Yang, L. Xu, L. Li, N. Qie, Y. Li, P. Zhang, and Y. Guo Personalized image aesthetics assessment with rich attributes . In Proceedings of the IEEE/CVF Conference on Computer Visi -->

<!-- [原子块 · verbatim] Yang et al. (2026b) Z. Yang, J. Wang, Z. Zhang, P. Xie, X. Sheng, P. Chen, and L. Li Fine-grained image aesthetic assessment: learning discriminative scores from relative ranks . In Proceedings of the -->

<!-- [原子块 · verbatim] Ye et al. (2024) Q. Ye, H. Xu, J. Ye, M. Yan, A. Hu, H. Liu, Q. Qian, J. Zhang, and F. Huang Mplug-owl2: revolutionizing multi-modal large language model with modality collaboration . In Proceedings o -->

<!-- [原子块 · verbatim] Yi et al. (2023) R. Yi, H. Tian, Z. Gu, Y. Lai, and P. L. Rosin Towards artistic image aesthetics assessment: a large-scale dataset and a new method . In Proceedings of the IEEE/CVF Conference on Comp -->

<!-- [原子块 · verbatim] Yin et al. (2026) Y. Yin, H. Krishnakumar, C. P. Lee, B. Zeng, W. Chai, S. Tong, W. Chen, H. Xu, X. Fu, G. Sarch, A. Korolova, and Z. Liu WorldBench: a challenging and visually diverse multimodal reas -->

<!-- [原子块 · verbatim] Zhang et al. (2026) L. Zhang, J. Yang, S. Krishnan, J. Majmudar, X. Ge, P. Puri, P. Saraf, S. Bhargava, D. Piraviperumal, Y. Ling, C. Pan, H. Yu, A. Agrawal, and B. Tseng From where things are to what -->

<!-- [原子块 · verbatim] Zhang et al. (2020) T. Zhang, V. Kishore, F. Wu, K. Q. Weinberger, and Y. Artzi BERTScore: evaluating text generation with bert . External Links: 1904.09675 , Link Cited by: §III.C , §S2.3.2 . -->

<!-- [原子块 · verbatim] Zhang et al. (2025) Z. Zhang, H. Wu, Z. Jia, W. Lin, and G. Zhai Teaching LMMs for image quality scoring and interpreting . External Links: 2503.09197 Cited by: §I , §II.B , Table 2 , Table 3 . -->

<!-- [原子块 · verbatim] Zhou et al. (2026) S. Zhou, B. Jia, K. Wu, Y. Shen, T. Li, Y. Wu, and S. Lin ReactBench: a cause-driven benchmark for multimodal hallucination via systematic evaluation . arXiv preprint arXiv:2605.295 -->

<!-- [原子块 · verbatim] Zhou et al. (2024) Z. Zhou, Q. Wang, B. Lin, Y. Su, R. Chen, X. Tao, A. Zheng, L. Yuan, P. Wan, and D. Zhang UNIAA: a unified multi-modal image aesthetic assessment baseline and benchmark . External L -->

<!-- [原子块 · verbatim] Zhu et al. (2025) J. Zhu, W. Wang, Z. Chen, Z. Liu, S. Ye, L. Gu, H. Tian, Y. Duan, W. Su, J. Shao, Z. Gao, E. Cui, X. Wang, Y. Cao, Y. Liu, X. Wei, H. Zhang, H. Wang, W. Xu, H. Li, J. Wang, N. Deng,  -->

**EN** Supplementary Material

**ZH** 补充材料

**EN** Supplementary Material

**ZH** 补充材料

**EN** AesCanvas: A Large-Scale Dataset and Benchmark for Aesthetic Critique and Contextual Suitability

**ZH** AesCanvas：一个面向美学评论与上下文适配性的大规模数据集与基准

**EN** S1 Supplement Overview and Positioning

**ZH** S1 补充材料概览与定位

**EN** This supplement documents AesCanvas and additional diagnostics. Section S2 provides the dataset, prompt, evaluation, and implementation materials; Section S3 presents model-output, robustness, and transfer analyses.

**ZH** 本补充材料记录了 AesCanvas 及额外的诊断分析。第 S2 节提供数据集、提示、评测与实现方面的材料；第 S3 节给出模型输出、稳健性与迁移分析。

**EN** S1.1 Positioning Relative to Prior Datasets

**ZH** S1.1 相对既有数据集的定位

**EN** Table S1 compares published dataset and supervision affordances. A checkmark requires explicit support in the corresponding paper or dataset documentation; a triangle denotes limited or indirect support. Use-context judgment specifically requires an auditable decision about whether an image is appropriate for a stated purpose, audience, or convention, rather than generic context reasoning or intrinsic aesthetic scoring.

**ZH** 表 S1 比较了已发布数据集与监督能力。打勾要求相应论文或数据集文档中有明确支持；三角表示支持有限或间接。使用语境判断特指就可审计地判定一张图像是否适合所述目的、受众或惯例，而非泛化的语境推理或内在美学打分。

**EN** The comparison covers established photographic-aesthetics datasets (Murray et al., 2012; Kong et al., 2016; Yang et al., 2022), AI-generated-image quality datasets (Li et al., 2024; Wang et al., 2023), and recent multimodal aesthetic-critique and assessment resources (Huang et al., 2024c; Huang et al., 2024a; Qi et al., 2025a; Cao et al., 2025c; Liu et al., 2026).

**ZH** 比较覆盖既有摄影美学数据集（Murray et al., 2012; Kong et al., 2016; Yang et al., 2022）、AI 生成图像质量数据集（Li et al., 2024; Wang et al., 2023），以及近期的多模态美学评论与评估资源（Huang et al., 2024c; Huang et al., 2024a; Qi et al., 2025a; Cao et al., 2025c; Liu et al., 2026）。

**EN** Table S1: Comparison of media coverage and aesthetic supervision.

**ZH** 表 S1：媒介覆盖与美学监督能力的比较。

<!-- [原子块 · table] Dataset Scale Photo- graphy Painting / art AIGC / virtual Long-form critique Structured dimensions Grounded explanation Use-context judgment AVA > > 250K images ✓ \checkmark – – – △ \triangle – – AADB -->

**EN** Note. –denotes that the affordance is not established in the published dataset design. AVA provides score distributions and semantic/style labels; AGIQA-3K provides perceptual-quality and text–image-alignment scores; and PhotoCritique provides broad photographic feedback rather than a fixed multi-dimensional annotation schema. “Painting / art” includes broader artistic imagery, while “AIGC / virtual” includes generated and other virtual imagery.

**ZH** 注。–表示该项能力在已发布的数据集设计中未得到确立。AVA 提供分数分布与语义/风格标签；AGIQA-3K 提供感知质量与图文对齐分数；PhotoCritique 提供宽泛的摄影反馈，而非固定的多维标注模式。「绘画/艺术」涵盖更广的艺术图像，而「AIGC/虚拟」涵盖生成图像与其他虚拟图像。

**EN** Prior resources already provide substantial supervision for intrinsic aesthetic perception and critique. AesCanvas complements them by coupling long-form critique with a closed-form benchmark in which cultural, narrative, functional, or domain-specific evidence can change whether an image is suitable for a concrete use.

**ZH** 既有资源已经为内在的美学感知与评论提供了大量监督。AesCanvas 对它们的补充在于：把长篇评论与一个封闭形式的基准结合起来，在该基准中，文化、叙事、功能或领域特定的证据可以改变一张图像是否适合某个具体用途。

**EN** S2 Dataset and Evaluation Materials

**ZH** S2 数据集与评测材料

**EN** This section documents the record schemas, prompt templates and representative intervention specifications, evaluation procedures, and implementation details needed to interpret AesCanvas and the reported measurements.

**ZH** 本节记录理解 AesCanvas 与所报告测量所需的记录模式、提示模板与代表性干预说明、评测流程以及实现细节。

**EN** S2.1 Dataset Documentation

**ZH** S2.1 数据集文档

**EN** S2.1.1 AesCanvas Overview

**ZH** S2.1.1 AesCanvas 概览

**EN** AesCanvas contains two complementary components derived from a shared image pool. Table S2 summarizes their data units, scales, outputs, and evaluation roles.

**ZH** AesCanvas 包含两个源自共享图像池的互补组件。表 S2 汇总了它们的数据单位、规模、输出与评测角色。

**EN** Table S2: Suite-level data card for the two AesCanvas components.

**ZH** 表 S2：AesCanvas 两个组件的套件级数据卡。

<!-- [原子块 · table] Field CritiqueCanvas ContextCanvas Primary task Long-form, multi-dimensional aesthetic critique Contextual aesthetic suitability judgment Data unit Image, instruction, selected dimensions, and respons -->

**EN** The shared pool comprises 21,294 photographs, 17,939 paintings, and 15,067 virtual images. Photography includes natural scenes, architecture, portraiture, commercial imagery, and other camera-based work; painting contains primarily Western classical and related painted work; and virtual imagery includes game scenes, animation-style illustration, and AI-generated content. Images were collected from publicly accessible web sources, museums, and cultural-heritage collections. Low-quality, semantically uninformative, non-compliant, duplicate, and near-duplicate candidates were removed. CritiqueCanvas conversations derived from the same image are grouped before splitting so that related records do not cross its train/evaluation partitions. ContextCanvas is used as a fixed diagnostic set rather than a training split.

**ZH** 共享图像池包含 21,294 张照片、17,939 幅绘画与 15,067 张虚拟图像。摄影包括自然场景、建筑、肖像、商业影像及其他基于相机的作品；绘画主要为西方古典及相关绘画作品；虚拟图像包括游戏场景、动画风格插画与 AI 生成内容。图像采集自可公开访问的网络来源、博物馆与文化遗产收藏。低质量、语义无信息量、不合规、重复与近似重复的候选被剔除。源自同一图像的 CritiqueCanvas 对话在划分前先归组，以免相关记录跨越其训练/评测分区。ContextCanvas 用作固定的诊断集，而非训练划分。

**EN** For documentation clarity, we provide the dataset cards, record schemas, prompts, metric definitions, evaluation and parsing procedures, and representative examples for both components. Task-specific model inputs, supervision fields, rationales, and provenance metadata are described below.

**ZH** 为便于文档化，我们提供两个组件的数据卡、记录模式、提示、指标定义、评测与解析流程以及代表性示例。下面描述任务特定的模型输入、监督字段、推理依据与出处元数据。

**EN** S2.1.2 CritiqueCanvas

**ZH** S2.1.2 CritiqueCanvas

**EN** CritiqueCanvas uses ten shared dimensions: Content/Narrative, Composition, Color, Lighting, Lines/Brushstrokes, Style, Emotion, Technique, Symbolism, and Visual Appeal. Only image-relevant dimensions are selected for a given record. The shared dimensions are complemented by domain-conditioned criteria: photography emphasizes exposure, perspective, depth of field, focus, motion, and compositional control; painting emphasizes line, brushwork, genre, style, symbolism, and emotion; and virtual imagery emphasizes character design, scene construction, rendering consistency, narrative setting, and stylization.

**ZH** CritiqueCanvas 使用十个共享维度：内容/叙事、构图、色彩、光影、线条/笔触、风格、情绪、技法、象征与视觉吸引力。对给定记录只挑选与该图像相关的维度。共享维度由领域条件化的准则加以补充：摄影强调曝光、透视、景深、对焦、动态与构图控制；绘画强调线条、笔法、体裁、风格、象征与情绪；虚拟图像强调角色设计、场景构建、渲染一致性、叙事设定与风格化。

**EN** The CritiqueCanvas record schema identifies the image and domain, selected dimensions, instruction, target response, conversation group, split, and associated provenance/governance metadata. The evaluation loader consumes a compact conversation form with id, image, and conversations; it takes the first user/human turn as the instruction and the first assistant/GPT turn as the reference. The image and instruction form the model input, while the reference is withheld until scoring. Each row records sample_id, relative and resolved image paths, the exact rendered prompt, reference, prediction, model, task, and timestamp. Each six-pair construction dialogue was converted into six pair-level records sharing a conversation-group identifier; the evaluation export therefore contains one human–assistant pair per record. Source, license, selected-dimension, split, audit, and governance fields are retained as metadata but are never supplied as model input. Representative examples spanning photography, illustration, and painting, as well as both open-ended and dimension-focused instruction functions, are shown in Fig. S1.

**ZH** CritiqueCanvas 的记录模式标识图像与领域、所选维度、指令、目标回答、对话组、划分以及相关的出处/治理元数据。评测加载器消费一种紧凑的对话形式，含 id、图像与对话；它取第一个 user/human 轮次作为指令，取第一个 assistant/GPT 轮次作为参考答案。图像与指令构成模型输入，参考答案在打分前不予提供。每行记录 sample_id、相对与解析后的图像路径、实际渲染的提示、参考答案、预测、模型、任务与时间戳。每条六配对的构建对话被转换为共享同一对话组标识符的六条配对级记录；因此评测导出中每条记录包含一组 human–assistant 配对。来源、许可、所选维度、划分、审计与治理字段作为元数据保留，但从不作为模型输入提供。图 S1 给出了涵盖摄影、插画与绘画，以及开放式与维度聚焦两类指令功能的代表性示例。

<!-- [原子块 · img]  -->

**EN** Figure S1: Representative CritiqueCanvas examples across photography, illustration, and painting. Each example pairs an image with its rendered query and the corresponding aesthetic focus. The examples include both broad image-appreciation prompts and prompts targeting specific dimensions such as light and shadow, atmosphere, tonal treatment, and formal analysis.

**ZH** 图 S1：CritiqueCanvas 在摄影、插画与绘画上的代表性示例。每个示例把一张图像与其渲染后的查询及相应的美学焦点配对。示例既包括宽泛的图像欣赏类提示，也包括针对光影、氛围、色调处理与形式分析等具体维度的提示。

**EN** Gemini performs dimension-aware planning, GLM generates the corresponding domain-conditioned critique annotations, and an independent Claude Opus 5 verification stage screens instruction consistency, visual grounding, and response quality. Five human reviewers then independently inspected a stratified sample of 1,000 retained pairs using the rubric detailed below. The audit yielded 95.3% acceptance and 97.0% raw agreement.

**ZH** Gemini 执行维度感知的规划，GLM 生成相应的领域条件化评论标注，随后由一个独立的 Claude Opus 5 校验阶段筛查指令一致性、视觉定位与回答质量。之后五位人类评审者依据下述评分细则，独立检查了 1,000 组保留配对的分层样本。审计得到 95.3% 的接受率与 97.0% 的原始一致率。

**EN** S2.1.3 ContextCanvas

**ZH** S2.1.3 ContextCanvas

**EN** ContextCanvas was sampled from the same 54,300-image pool. The 1,060 initial candidate cases were collected primarily through a call circulated within the university. Graduate research assistants, doctoral researchers, and faculty spanning computer science and electrical engineering, visual arts and art history, design and visual communication, and cultural and media studies contributed source ideas and image–use proposals. A separate multidisciplinary panel of four PhD-level researchers developed these contributions into formal candidate cases and reviewed them through iterative refinement, standardization, cross-disciplinary checking, and final adjudication. A candidate was retained only if it satisfied aesthetic centrality, context dependence, visual necessity, decisive evidence, scenario naturalness, answerability, and anti-shortcut validity. Qwen3.7-Plus was used only as a development-time probe for trivial, ambiguous, or shortcut-prone candidates; model failure was never an inclusion condition. The four-person review panel finalized all questions, options, gold labels, source-grounded rationales, and source records.

**ZH** ContextCanvas 从同一个 54,300 张图像的池中采样。最初的 1,060 个候选案例主要通过在校内流传的征集获得。来自计算机科学与电气工程、视觉艺术与艺术史、设计与视觉传播、文化与媒体研究等领域的研究生助理、博士研究人员与教师贡献了原始创意与图像-使用提案。一个由四位博士级研究者组成的独立跨学科小组把这些投稿发展为正式候选案例，并通过迭代精修、标准化、跨学科核对与最终裁决加以评审。候选只有在满足美学中心性、上下文依赖性、视觉必要性、决定性证据、场景自然性、可回答性与反捷径有效性时才被保留。Qwen3.7-Plus 仅作为开发期探针，用于筛查过于简单、含糊或易走捷径的候选；模型失败从不作为纳入条件。四人评审小组最终确定了所有问题、选项、金标签、基于来源的推理依据与来源记录。

**EN** The 301 retained cases comprise 300 single-image cases and one paired-image case, covering 302 unique images. Each case record stores the stable evaluation ID, original case ID, image descriptor(s), question, options, gold option ID and text, source-grounded rationale, source basis, and provenance/rights fields. Only the image(s), question, and fixed options are model input; labels, rationales, source titles, URLs, development metadata, and model-probe results are excluded.

**ZH** 保留的 301 个案例包含 300 个单图案例与 1 个成对图像案例，覆盖 302 张唯一图像。每个案例记录存储稳定的评测 ID、原始案例 ID、图像描述符、问题、选项、金选项 ID 与文本、基于来源的推理依据、来源依据以及出处/权利字段。只有图像、问题与固定选项作为模型输入；标签、推理依据、来源标题、URL、开发元数据与模型探针结果均被排除。

**EN** A label-balanced demonstration of retained cases is shown in Fig. S2. The examples are organized by the mechanism that makes the aesthetic-use decision non-trivial: cultural or historical alignment; narrative meaning that reverses attractive, serene, or balanced surface qualities; apparent visual mismatch that strengthens a communicative purpose; and medium- or story-specific framing. Every example distinguishes the visible cue, the contextual knowledge it activates, and the resulting visual-use decision. This presentation makes clear that the task is neither artwork-title recall nor context-free cultural question answering.

**ZH** 图 S2 给出了保留案例的标签均衡展示。示例按「使美学使用决策变得非平凡」的机制组织：文化或历史对齐；能够反转吸引力、宁静感或平衡感等表面品质的叙事含义；强化传播目的的表观视觉错配；以及媒介或故事特定的框定方式。每个示例都区分可见线索、它所激活的上下文知识，以及由此得出的视觉使用决策。这一呈现清楚表明，该任务既不是艺术作品标题回忆，也不是脱离上下文的文化问答。

<!-- [原子块 · img]  -->

**EN** Figure S2: Representative retained ContextCanvas cases. Top row, from left to right: HB208 (Mid-Autumn cultural fit), HB014 (historical military identity), and HB159 (restorative return versus the Lotus-Eaters’ withdrawal). Bottom row: HB155 (fiction–reality confusion), HB181 (teamwork under visual tension), and HB186 (addiction in a refined setting). Each card separates visible form, use scenario, contextual evidence, decision, and gold label.

**ZH** 图 S2：代表性的保留 ContextCanvas 案例。上排从左至右：HB208（中秋文化契合）、HB014（历史军事身份）与 HB159（复原式回归 versus 食莲者的退隐）。下排：HB155（虚构与现实的混淆）、HB181（视觉张力下的团队协作）与 HB186（精致场景中的成瘾主题）。每张卡片分别列出可见形式、使用场景、上下文证据、决策与金标签。

**EN** Expert review also removed coherent human-drafted questions that failed one of the retention requirements. Figure S3 shows three such boundaries: a bridal image whose conspicuous negative affect makes the answer available through coarse emotion recognition; The Wolf and the Crane, whose decisive betrayal occurs outside the depicted moment and therefore weakens visual necessity; and the historical “DON’T MIX ’EM” poster, for which a contemporary campaign can defensibly reject the sensational design, preventing a uniquely compelled gold label. These examples demonstrate that professional wording and a plausible intended answer were insufficient for retention. They are illustrative and are not used to estimate a distribution of rejection reasons.

**ZH** 专家评审还剔除了一些表述连贯、但未能满足保留要求之一的人工起草问题。图 S3 给出了三类这样的边界：一幅新娘图像因其显著的负面情绪使人可通过粗粒度情绪识别得到答案；《狼与鹤》的决定性背叛发生在所描绘时刻之外，因而削弱了视觉必要性；而历史海报「DON’T MIX ’EM」，当代活动可以合理地拒绝其煽情设计，从而无法唯一确定金标签。这些例子说明，专业的措辞与看似合理的预期答案并不足以构成保留理由。它们仅作示例，不用于估计拒绝原因的分布。

<!-- [原子块 · img]  -->

**EN** Figure S3: Human-drafted candidates excluded after expert review. From left to right: R41Q05 was insufficiently challenging because conspicuous negative affect enabled a coarse shortcut; R41Q08 weakened visual necessity because the decisive betrayal occurs outside the depicted moment; and R69Q06 lacked a uniquely compelled gold label for a contemporary campaign.

**ZH** 图 S3：经专家评审后排除的人工起草候选。从左至右：R41Q05 挑战性不足，因为显著的负面情绪使粗粒度捷径可行；R41Q08 削弱了视觉必要性，因为决定性背叛发生在所描绘时刻之外；R69Q06 对当代活动缺乏唯一确定的金标签。

**EN** S2.1.4 Provenance and Governance

**ZH** S2.1.4 出处与治理

**EN** For each ContextCanvas image, provenance metadata include the known title, creator, provider, source URL, license note, and redistribution status. Missing creator names are preserved as unknown rather than inferred. Synthetic counterfactual edits are clearly labeled as research diagnostics and are not treated as natural benchmark images or training annotations.

**ZH** 对每张 ContextCanvas 图像，出处元数据包括已知标题、创作者、提供方、来源 URL、许可说明与再分发状态。缺失的创作者姓名保留为未知，而非加以推断。合成的反事实编辑被明确标注为研究诊断用途，不被视为自然的基准图像或训练标注。

**EN** The datasets necessarily reflect the source pool and the expertise of the case contributors and review panel. ContextCanvas is an expert diagnostic benchmark rather than exhaustive coverage of cultures, audiences, or design practice, and a source-grounded rationale does not eliminate every historically or culturally contestable interpretation. CritiqueCanvas similarly permits multiple valid analyses of the same image; its reference response is supervision, not the only legitimate critique.

**ZH** 这些数据集必然反映来源池以及案例贡献者与评审小组的专业背景。ContextCanvas 是一个专家诊断基准，而非对文化、受众或设计实践的穷尽覆盖；一段基于来源的推理依据也不排除每一种在历史或文化上可争议的解读。CritiqueCanvas 同样允许多种对同一图像的有效分析；其参考回答是监督信号，而非唯一合法的评论。

**EN** S2.2 Prompts

**ZH** S2.2 提示

**EN** We report the prompts used in dataset construction and in the experiments described in the main paper.

**ZH** 我们报告数据构建过程与正文所述实验中使用的提示。

**EN** S2.2.1 CritiqueCanvas Prompts

**ZH** S2.2.1 CritiqueCanvas 提示

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

**EN** S2.2.2 ContextCanvas Prompts

**ZH** S2.2.2 ContextCanvas 提示

<!-- [原子块 · svg]  -->

**EN** Where supported, provider-side structured-output enforcement was requested for the required JSON schema. The reason and confidence fields are retained for qualitative analysis but do not affect exact-match grading, which is based solely on the predicted option ID.

**ZH** 在支持的情况下，我们请求提供方侧的结构化输出强制，以符合所需 JSON 模式。reason 与 confidence 字段保留用于定性分析，但不影响精确匹配评分——后者仅依据预测的选项 ID。

**EN** Counterfactual editing prompts. Each of the 36 edits replaces the decisive incompatible cue with a scenario-compatible alternative while aiming to preserve the source medium, composition, palette, viewpoint, and non-target content as closely as possible. We use GPT Image 2 for all edits. Pair-specific interventions were specified individually. For example, CF01 replaces Japanese-inspired wafuku and tea props with Chinese hanfu, a Chinese tea set, mooncakes, and a palace lantern; CF18 replaces the governess’s distressing letter with an open lesson book and makes the children engage with her while retaining the painted nursery and period style. All edited images were manually checked for successful cue replacement and preservation of non-target content; invalid edits were regenerated.

**ZH** 反事实编辑提示。36 处编辑各自把决定性的不兼容线索替换为与场景兼容的替代物，同时尽量保持源媒介、构图、色调、视点与非目标内容不变。所有编辑均使用 GPT Image 2。配对专属的干预逐个指定。例如，CF01 把日式风格的和服与茶具替换为中式汉服、中国茶具、月饼与宫灯；CF18 把家庭教师那封令人不安的信替换为摊开的课本，并让孩童与她互动，同时保留画中的育儿室与时代风格。所有编辑后的图像都经人工检查，确认线索替换成功且非目标内容得以保留；无效编辑会被重新生成。

**EN** Modality diagnostic. Motivated by caption-utility evaluation that treats captions as image surrogates (Yang et al., 2026a), we additionally evaluate text-only, identity- and verdict-free neutral-caption, and decisive-visible-cue conditions using the same questions, options, output schema, and scoring protocol. The condition construction and aggregate results are reported below.

**ZH** 模态诊断。受把字幕视为图像替代物的字幕效用评测启发（Yang et al., 2026a），我们还使用相同的问题、选项、输出模式与评分协议，评估纯文本条件、无身份与无结论的中性字幕条件，以及决定性可见线索条件。条件构造与汇总结果见下文。

**EN** S2.2.3 Evaluation and Judge Prompts

**ZH** S2.2.3 评测与裁判提示

**EN** Human critique-rating instructions. Two human evaluators independently assessed five anonymous critiques for each image without access to model identities or to each other’s ratings. For each critique, they assigned a binary judgment on four criteria: visual grounding, aesthetic specificity, criterion appropriateness, and analytical usefulness. A criterion received one point when the critique was comparatively strong on that dimension within the same image–prompt batch, and zero points when it was comparatively weak. The final human score was one plus the number of satisfied criteria, yielding a score from 1 to 5. Thus, a zero on an individual criterion denotes relative weakness among responses to the same prompt rather than the complete absence of that quality.

**ZH** 人类评论评分说明。两位人类评估者在不知道模型身份、也看不到对方评分的情况下，独立评估每张图像的五份匿名评论。对每份评论，他们就四项准则给出二元判断：视觉定位、美学具体性、准则恰当性与分析有用性。某项准则在「同一图像-提示批次内相对更强」时得一分，「相对更弱」时得零分。最终人类分数为 1 加上满足的准则数，取值从 1 到 5。因此，单项准则上的零分表示在同一提示的若干回答中相对较弱，而非该品质完全缺失。

**EN** MLLM critique judge. Following rubric-based model evaluation (Liu et al., 2023; Chen et al., 2024), Claude Opus 5 provides a complementary assessment. The judge assigns four criterion-specific scores and one holistic overall-quality score, each from 1 to 5. For each case, the five candidate critiques are anonymized and randomly permuted before evaluation, then assigned temporary aliases A–E; the alias-to-model mapping is restored after scoring. The reference critique is withheld. The fifth, holistic score is reported as the MLLM score in Table 4 of the main paper.

**ZH** MLLM 评论裁判。遵循基于评分细则的模型评测做法（Liu et al., 2023; Chen et al., 2024），Claude Opus 5 提供互补评估。裁判给出四项准则专属分数与一项整体质量分，每项取值 1 到 5。对每个案例，五份候选评论在评测前匿名化并随机打乱，然后被赋予临时别名 A–E；打完分后恢复别名到模型的映射。参考评论不予提供。第五项整体分数作为正文表 4 中的 MLLM 分数报告。

<!-- [原子块 · svg]  -->

**EN** The Claude Opus 5 judge is run at temperature 0 with returned reasoning disabled. Each image is resized to ⟦SLOT_48⟧ and JPEG-encoded at quality 90. The runner requests a strict JSON schema and permits at most 320 output tokens.

**ZH** Claude Opus 5 裁判在温度 0、关闭返回推理的条件下运行。每张图像缩放到 ⟦SLOT_48⟧ 并以质量 90 的 JPEG 编码。运行器请求严格的 JSON 模式，最多允许 320 个输出词元。

**EN** Evidence-grounded human evaluation. Motivated by multi-dimensional visual-grounding evaluation (Li et al., 2026), two human evaluators assessed model responses on 100 ContextCanvas cases. Model identities were concealed. For each case, evaluators were shown the image, scenario, answer options, gold decision, expert decisive-cue rationale, and an anonymized response. They independently judged whether the response selected the correct answer, identified the decisive visible cue or a visually warranted equivalent, and correctly linked that cue to the stated use. Valid equivalent reasoning was accepted without requiring lexical overlap with the expert rationale. Disagreements were resolved through discussion. Evidence-Grounded Accuracy requires all three conditions.

**ZH** 证据定位的人工评测。受多维度视觉定位评测启发（Li et al., 2026），两位人类评估者在 100 个 ContextCanvas 案例上评估模型回答。模型身份被隐匿。对每个案例，评估者会看到图像、场景、答案选项、金决策、专家给出的决定性线索推理依据，以及一份匿名回答。他们独立判断该回答是否选择了正确答案、是否识别出决定性的可见线索或视觉上站得住脚的等价物，以及是否把该线索正确关联到所述用途。只要推理等价且成立，即使与专家推理依据没有词汇重叠也予以接受。分歧通过讨论解决。证据定位准确率（EGA）要求三项条件同时满足。

**EN** S2.3 Evaluation Rubrics and Metrics

**ZH** S2.3 评测评分细则与指标

**EN** S2.3.1 Dataset-Quality Rubrics

**ZH** S2.3.1 数据集质量评分细则

**EN** For CritiqueCanvas, five human reviewers independently inspected a stratified sample of 1,000 retained instruction–response pairs spanning photography, painting, and virtual imagery. The audit assessed instruction consistency, visual grounding, image-specific aesthetic analysis, and overall coherence and usefulness. Blocking issues include an instruction–image mismatch, failure to perform the requested task, material visual hallucination, an essentially generic or incomplete response, or a safety, rights, or compliance failure. Non-blocking issues are localized weaknesses, such as minor imprecision, awkward wording, limited repetition, or omission of a secondary point, that do not by themselves invalidate the pair. Blocking issues require rejection, whereas non-blocking issues alone do not.

**ZH** 对 CritiqueCanvas，五位人类评审者独立检查了 1,000 组保留的指令-回答对的分层样本，覆盖摄影、绘画与虚拟图像。审计评估指令一致性、视觉定位、针对具体图像的美学分析，以及整体连贯性与有用性。阻断性问题包括指令与图像不匹配、未执行所要求的任务、实质性的视觉幻觉、本质上泛泛或不完整的回答，或安全、权利与合规方面的失败。非阻断性问题是局部的弱点，例如轻微不准确、措辞生硬、少量重复或遗漏某个次要要点，它们本身不足以使该配对失效。阻断性问题需要拒收，而仅有非阻断性问题则不必。

**EN** Of the 1,000 audited pairs, 970 received no blocking-issue flag from any of the five independent reviewers. The 97.0% “raw agreement” reported in the main paper denotes this unanimous no-blocking-issue rate, not a chance-corrected inter-rater reliability coefficient. A subsequent asset-level validation, conducted separately from response-quality voting, removed 17 otherwise acceptable pairs whose source images did not meet the final clarity threshold. The resulting 953 pairs constitute the reported 95.3% accepted set.

**ZH** 在审计的 1,000 组配对中，970 组没有被五位独立评审者中的任何一位标出阻断性问题。正文中报告的 97.0%「原始一致率」指的正是这一「无人标出阻断性问题」的比例，而非经机会校正的评分者间信度系数。随后开展的一项资产级验证（与回答质量投票分开进行）剔除了 17 组本可接受的配对，其源图像未达到最终的清晰度阈值。由此得到的 953 组配对构成所报告的 95.3% 接受集。

**EN** For ContextCanvas, four PhD-level researchers rechecked and adjudicated the candidate cases. A case was retained only when all seven criteria held: aesthetic centrality requires judgment of the image as a visual choice; context dependence requires the use, audience, or convention to affect the decision; visual necessity prevents reduction to text-only factual recall; decisive evidence requires the cultural, historical, narrative, or functional evidence to materially affect the answer; scenario naturalness requires a plausible design or communication use; answerability requires a uniquely supportable closed-form label; and anti-shortcut validity prevents wording, option length, or label priors from exposing the answer. Figure S3 supplies boundary examples for target difficulty, visual necessity, and answerability.

**ZH** 对 ContextCanvas，四位博士级研究者重新核对并裁决候选案例。案例只有在七项准则全部成立时才被保留：美学中心性要求把图像作为视觉选择来评判；上下文依赖性要求用途、受众或惯例影响决策；视觉必要性防止退化为纯文本的事实回忆；决定性证据要求文化、历史、叙事或功能证据实质影响答案；场景自然性要求一个可信的设计或传播用途；可回答性要求唯一可支持的封闭形式标签；反捷径有效性防止措辞、选项长度或标签先验泄露答案。图 S3 提供了目标难度、视觉必要性与可回答性方面的边界示例。

**EN** S2.3.2 Critique Evaluation

**ZH** S2.3.2 评论评测

**EN** We use BLEU (Papineni et al., 2002), ROUGE-L (Lin, 2004), and METEOR (Banerjee and Lavie, 2005) for lexical overlap; BERT-F1 (Zhang et al., 2020) and SBERT cosine similarity (Reimers and Gurevych, 2019) for token- and sentence-level semantic similarity; and a CLIP image–text cosine score (Hessel et al., 2021) for image relevance. Let ⟦SLOT_49⟧ and ⟦SLOT_50⟧ denote the generated and reference critiques for item ⟦SLOT_51⟧.

**ZH** 我们用 BLEU（Papineni et al., 2002）、ROUGE-L（Lin, 2004）与 METEOR（Banerjee and Lavie, 2005）度量词汇重叠；用 BERT-F1（Zhang et al., 2020）与 SBERT 余弦相似度（Reimers and Gurevych, 2019）度量词元级与句子级语义相似度；用 CLIP 图文余弦分数（Hessel et al., 2021）度量图像相关性。令 ⟦SLOT_49⟧ 与 ⟦SLOT_50⟧ 表示条目 ⟦SLOT_51⟧ 的生成评论与参考评论。

**EN** BLEU is SacreBLEU corpus BLEU (Post, 2018) with maximum order four and effective_order=True. With clipped corpus precision ⟦SLOT_52⟧ and brevity penalty ⟦SLOT_53⟧ if ⟦SLOT_54⟧, otherwise ⟦SLOT_55⟧, and SacreBLEU’s default exponential smoothing for zero higher-order counts, the percentage-form value in the main table is

**ZH** BLEU 采用 SacreBLEU 语料级 BLEU（Post, 2018），最大阶数为四，effective_order=True。记截断后的语料精确率为 ⟦SLOT_52⟧，简短惩罚 ⟦SLOT_53⟧ 在 ⟦SLOT_54⟧ 时取该值，否则取 ⟦SLOT_55⟧；对高阶计数为零的情形使用 SacreBLEU 默认的指数平滑。主表中以百分数形式给出的值为

<!-- [原子块 · table] BLEU = 100 ​ BP ​ exp ⁡ ( 1 4 ​ ∑ n = 1 4 log ⁡ p n ) . \mathrm{BLEU}=100\,\mathrm{BP}\exp\!\left(\frac{1}{4}\sum_{n=1}^{4}\log p_{n}\right). (S1) -->

**EN** The evaluation output stores this value divided by 100; the paper multiplies it by 100 for presentation. ROUGE-L is computed per item with stemming enabled. If ⟦SLOT_56⟧ is the longest-common-subsequence length, ⟦SLOT_57⟧, and ⟦SLOT_58⟧, then

**ZH** 评测输出保存的是该值除以 100 的结果；论文为呈现需要把它乘以 100。ROUGE-L 逐条目计算，启用词干化。若 ⟦SLOT_56⟧ 为最长公共子序列长度，⟦SLOT_57⟧，⟦SLOT_58⟧，则

<!-- [原子块 · table] ROUGE ​ - ​ L = 1 N ​ ∑ i 2 ​ P i ​ R i P i + R i , \mathrm{ROUGE\mbox{-}L}=\frac{1}{N}\sum_{i}\frac{2P_{i}R_{i}}{P_{i}+R_{i}}, (S2) -->

**EN** with a zero contribution when the denominator is zero.

**ZH** 分母为零时贡献为零。

**EN** METEOR uses NLTK’s default English matcher (Bird et al., 2009) on whitespace-tokenized texts. For the matcher-selected unigram alignment with ⟦SLOT_59⟧ matches and ⟦SLOT_60⟧ chunks,

**ZH** METEOR 使用 NLTK 默认的英文匹配器（Bird et al., 2009），作用于按空白分词的文本。对于匹配器选出的、含 ⟦SLOT_59⟧ 个匹配与 ⟦SLOT_60⟧ 个块的 unigram 对齐，

<!-- [原子块 · table] P i \displaystyle P_{i} = m i / | h i | , \displaystyle=m_{i}/|h_{i}|, (S3) R i \displaystyle R_{i} = m i / | r i | , \displaystyle=m_{i}/|r_{i}|, (S4) F i \displaystyle F_{i} = P i ​ R i 0.9 ​ P i +  -->

**EN** Items with no alignment contribute zero. The implementation also inherits NLTK’s exact, stemmed, and WordNet-based synonym matching behavior.

**ZH** 无对齐的条目贡献为零。该实现还继承了 NLTK 的精确匹配、词干匹配与基于 WordNet 的同义词匹配行为。

**EN** BERTScore uses microsoft/deberta-base-mnli, no IDF weighting, and no baseline rescaling. For contextual token embeddings, its item-level precision and recall are the mean maximum cosine matches from hypothesis to reference and reference to hypothesis; BERT-F1 is the corpus mean of ⟦SLOT_61⟧. SBERT-Cos uses sentence-transformers/all-mpnet-base-v2; masked mean pooling over the last hidden state is ⟦SLOT_62⟧, followed by ⟦SLOT_63⟧ normalization and

**ZH** BERTScore 使用 microsoft/deberta-base-mnli，不做 IDF 加权，也不做基线重标定。对于上下文词元嵌入，其条目级精确率与召回率分别是从假设到参考、从参考到假设的最大余弦匹配的均值；BERT-F1 是 ⟦SLOT_61⟧ 的语料均值。SBERT-Cos 使用 sentence-transformers/all-mpnet-base-v2；对最后隐状态做掩码均值池化得到 ⟦SLOT_62⟧，随后做 ⟦SLOT_63⟧ 归一化并

<!-- [原子块 · table] SBERT ​ - ​ Cos = 1 N ​ ∑ i e ​ ( h i ) ⊤ ​ e ​ ( r i ) . \mathrm{SBERT\mbox{-}Cos}=\frac{1}{N}\sum_{i}e(h_{i})^{\top}e(r_{i}). (S8) -->

**EN** Both text encoders truncate at 512 tokens.

**ZH** 两个文本编码器都在 512 个词元处截断。

**EN** The reported CLIP value uses openai/clip-vit-base-patch32. For normalized CLIP text and image features ⟦SLOT_64⟧ and ⟦SLOT_65⟧,

**ZH** 所报告的 CLIP 值使用 openai/clip-vit-base-patch32。对于归一化后的 CLIP 文本特征 ⟦SLOT_64⟧ 与图像特征 ⟦SLOT_65⟧，

<!-- [原子块 · table] CLIPCos = 1 N ​ ∑ i t ​ ( h i ) ⊤ ​ v ​ ( I i ) . \mathrm{CLIPCos}=\frac{1}{N}\sum_{i}t(h_{i})^{\top}v(I_{i}). (S9) -->

**EN** This implementation is the raw mean cosine: it does not apply the ⟦SLOT_66⟧ truncation or ⟦SLOT_67⟧ scaling sometimes used by the named CLIPScore metric. We retain the main-table column name for continuity but make the operational definition explicit here. All six metrics are interpreted jointly because no single reference exhausts the valid analyses of an image.

**ZH** 该实现是原始的平均余弦：它没有应用具名 CLIPScore 指标有时会使用的 ⟦SLOT_66⟧ 截断或 ⟦SLOT_67⟧ 缩放。我们为保持连续性沿用主表中的列名，但在此明确给出可操作的定义。全部六项指标需联合解读，因为没有任何单一参考能穷尽对一张图像的有效分析。

**EN** For response-level statistics, text is lowercased and tokenized with the regular expression [a-z]+; lightweight Markdown headings and markers are removed before dimension matching. For generated response ⟦SLOT_68⟧, average length and explicit dimension coverage are

**ZH** 就回答级统计而言，文本先转为小写并用正则表达式 [a-z]+ 分词；在维度匹配之前会移除轻量级的 Markdown 标题与标记。对于生成的回答 ⟦SLOT_68⟧，平均长度与显式维度覆盖率为

<!-- [原子块 · table] AvgLen \displaystyle\mathrm{AvgLen} = 1 N ​ ∑ i = 1 N | words ⁡ ( r ^ i ) | , \displaystyle=\frac{1}{N}\sum_{i=1}^{N}|\operatorname{words}(\hat{r}_{i})|, (S10) DimHits \displaystyle\mathrm{DimHits} =  -->

**EN** where ⟦SLOT_69⟧ only when response ⟦SLOT_70⟧ explicitly addresses dimension ⟦SLOT_71⟧. Top-3 Dimensions are those with the largest corpus-level ⟦SLOT_72⟧. The ten categories and their fixed lexical/phrase triggers are Content, Composition, Color, Lighting, Brushstroke/Texture, Style, Emotion, Technique, Symbolism, and Visual Appeal. If ⟦SLOT_73⟧ counts all matched lexical/phrase occurrences and ⟦SLOT_74⟧ and ⟦SLOT_75⟧ are the prompt-focused and response-matched dimension sets, respectively, then

**ZH** 其中 ⟦SLOT_69⟧ 仅当回答 ⟦SLOT_70⟧ 明确涉及维度 ⟦SLOT_71⟧ 时成立。Top-3 维度是语料级 ⟦SLOT_72⟧ 最大的那些。十个类别及其固定的词汇/短语触发词为内容、构图、色彩、光影、笔触/质感、风格、情绪、技法、象征与视觉吸引力。若 ⟦SLOT_73⟧ 统计所有匹配到的词汇/短语出现次数，⟦SLOT_74⟧ 与 ⟦SLOT_75⟧ 分别是提示聚焦的维度集合与回答匹配的维度集合，则

<!-- [原子块 · table] Density \displaystyle\mathrm{Density} = 100 ​ ∑ i q ⁡ ( r ^ i ) ∑ i | words ⁡ ( r ^ i ) | , \displaystyle=100\frac{\sum_{i}q(\hat{r}_{i})}{\sum_{i}|\operatorname{words}(\hat{r}_{i})|}, (S12) PromptAli -->

**EN** Thus density counts repeated mentions rather than merely distinct categories. Generic Top-3 excludes prompts in which the current question explicitly names an aesthetic dimension; few-shot examples are removed before focus detection. These lexical diagnostics measure verbosity, breadth, and controllability rather than correctness, relevance, or grounding.

**ZH** 因此密度统计的是重复提及，而不仅仅是不同的类别。Generic Top-3 会排除那些当前问题已明确点出某个美学维度的提示；在焦点检测之前会先移除少样本示例。这些词汇层面的诊断度量的是啰嗦程度、广度与可控性，而非正确性、相关性或定位。

**EN** The human critique-quality evaluation applies four binary criteria: visual grounding, aesthetic specificity, criterion appropriateness, and analytical usefulness. For critique ⟦SLOT_76⟧, evaluator ⟦SLOT_77⟧, and criterion ⟦SLOT_78⟧, the item-level score is

**ZH** 人类评论质量评测采用四项二元准则：视觉定位、美学具体性、准则恰当性与分析有用性。对于评论 ⟦SLOT_76⟧、评估者 ⟦SLOT_77⟧ 与准则 ⟦SLOT_78⟧，条目级分数为

<!-- [原子块 · table] H i ​ j = 1 + ∑ k = 1 4 b i ​ j ​ k , b i ​ j ​ k ∈ { 0 , 1 } . H_{ij}=1+\sum_{k=1}^{4}b_{ijk},\qquad b_{ijk}\in\{0,1\}. (S14) -->

**EN** With two evaluators, Table 4 reports

**ZH** 在两名评估者下，表 4 报告

<!-- [原子块 · table] HumanScore = 1 2 ​ N ​ ∑ i = 1 N ∑ j = 1 2 H i ​ j . \mathrm{HumanScore}=\frac{1}{2N}\sum_{i=1}^{N}\sum_{j=1}^{2}H_{ij}. (S15) -->

**EN** The MLLM judge assigns four criterion-specific scores and a fifth holistic overall_quality score, each from 1 to 5. Table 4 in the main paper reports the mean of the fifth score:

**ZH** MLLM 裁判给出四项准则专属分数与第五项整体 overall_quality 分数，每项取值 1 到 5。正文表 4 报告第五项分数的均值：

<!-- [原子块 · table] MLLMScore = 1 N ​ ∑ i = 1 N s i overall . \mathrm{MLLMScore}=\frac{1}{N}\sum_{i=1}^{N}s_{i}^{\mathrm{overall}}. (S16) -->

**EN** The human and MLLM protocols for the 100-case critique-metric validity analysis, including anonymization, response permutation, rating criteria, and score aggregation, are specified in Section S2.2.3.

**ZH** 100 案例评论指标有效性分析的人类与 MLLM 协议，包括匿名化、回答打乱、评分准则与分数聚合，在第 S2.2.3 节中给出。

**EN** S2.3.3 Contextual-Suitability Evaluation

**ZH** S2.3.3 上下文适配性评测

**EN** Exact-match accuracy uses all 301 cases:

**ZH** 精确匹配准确率使用全部 301 个案例：

<!-- [原子块 · table] Accuracy = 1 301 ∑ i = 1 301 𝟏 [ y ^ i = y i ] . \mathrm{Accuracy}=\frac{1}{301}\sum_{i=1}^{301}\mathbf{1}[\hat{y}_{i}=y_{i}]. (S17) -->

**EN** Macro-F1 and predicted Yes Rate are computed on the 291 two-option cases; the 10 three-option cases contribute only to Accuracy. The scorer operates on option IDs A and B. In 287 cases these are explicitly Yes and No; four cases use context-specific binary alternatives and retain the same A/B class mapping. The paper therefore reports A as the canonical Yes/target-aligned class and B as No/non-target class. For class ⟦SLOT_79⟧,

**ZH** Macro-F1 与预测 Yes 率在 291 个双选项案例上计算；10 个三选项案例只贡献给准确率。打分器作用于选项 ID A 与 B。在其中 287 个案例里，A 与 B 明确对应 Yes 与 No；有 4 个案例使用上下文特定的二元替代选项，但保持相同的 A/B 类别映射。因此论文把 A 报告为规范的 Yes/目标对齐类，B 为 No/非目标类。对于类别 ⟦SLOT_79⟧，

<!-- [原子块 · table] P k = T ​ P k T ​ P k + F ​ P k , R k = T ​ P k T ​ P k + F ​ N k , F ​ 1 k = 2 ​ P k ​ R k P k + R k , P_{k}=\frac{TP_{k}}{TP_{k}+FP_{k}},\quad R_{k}=\frac{TP_{k}}{TP_{k}+FN_{k}},\quad F1_{k}=\frac{2 -->

**EN** and

**ZH** 以及

<!-- [原子块 · table] MacroF1 = F ​ 1 A + F ​ 1 B 2 , YesRate = 1 291 ∑ i 𝟏 [ y ^ i = A ] . \mathrm{MacroF1}=\frac{F1_{A}+F1_{B}}{2},\qquad\mathrm{YesRate}=\frac{1}{291}\sum_{i}\mathbf{1}[\hat{y}_{i}=A]. (S19) -->

**EN** The gold Yes Rate is 38.14%. Missing, conflicting, ambiguous, and unparseable answers are incorrect.

**ZH** 金标准 Yes 率为 38.14%。缺失、冲突、含糊与无法解析的答案计为错误。

**EN** Evidence-Grounded Accuracy requires a correct label, identification of the decisive visible cue or a warranted equivalent, and a correct link from that cue to the stated use:

**ZH** 证据定位准确率要求标签正确、识别出决定性可见线索或站得住脚的等价物，并把该线索正确关联到所述用途：

<!-- [原子块 · table] EGA = 1 N ​ ∑ i 𝟏 ​ [ correct i ∧ grounded i ∧ contextLink i ] . \mathrm{EGA}=\frac{1}{N}\sum_{i}\mathbf{1}[\mathrm{correct}_{i}\land\mathrm{grounded}_{i}\land\mathrm{contextLink}_{i}]. (S20) -->

**EN** Among correct predictions, the unsupported rate is

**ZH** 在正确预测中，无支撑率（unsupported rate）为

<!-- [原子块 · table] Unsupported = 100 × # ​ { correct ​ but ​ not ​ grounded } # ​ { correct } . \mathrm{Unsupported}=100\times\frac{\#\{\mathrm{correct\ but\ not\ grounded}\}}{\#\{\mathrm{correct}\}}. (S21) -->

**EN** For the 36 matched counterfactual pairs, Net Correct Update is

**ZH** 对于 36 组配对的反事实，净正确更新（Net Correct Update）为

<!-- [原子块 · table] NCU = 100 × N correct ​ change − N reverse ​ change 36 . \mathrm{NCU}=100\times\frac{N_{\mathrm{correct\ change}}-N_{\mathrm{reverse\ change}}}{36}. (S22) -->

**EN** NCU is reported together with correct, reverse, unchanged-correct, and unchanged-wrong counts and original/edit accuracies; it is not interpreted as a standalone causal score. Bootstrap 95% confidence intervals (Efron and Tibshirani, 1993) are used for accuracy and diagnostic rates. Base–specialist comparisons use exact two-sided McNemar tests (McNemar, 1947) on paired predictions with Bonferroni correction (Dunn, 1961) across the four reported pairs. Descriptive case studies receive no significance claim.

**ZH** NCU 与正确、反向、未变-正确、未变-错误的计数以及原始/编辑准确率一并报告；它不被解释为独立的因果分数。准确率与诊断率使用 bootstrap 95% 置信区间（Efron and Tibshirani, 1993）。基座-专用模型的比较在配对预测上使用精确双侧 McNemar 检验（McNemar, 1947），并在四组报告配对间做 Bonferroni 校正（Dunn, 1961）。描述性案例研究不做显著性断言。

**EN** S2.4 Implementation Details

**ZH** S2.4 实现细节

**EN** S2.4.1 Model and Inference Configuration

**ZH** S2.4.1 模型与推理配置

**EN** All models receive the same task content—the image(s), record-level question or scenario, and fixed options where applicable—without web search, retrieval, reverse-image search, metadata access, or auxiliary recognition tools. Images are converted to RGB and resized or padded to ⟦SLOT_80⟧ before being serialized with each checkpoint’s native multimodal chat template. This model-specific serialization does not alter the task content.

**ZH** 所有模型接收相同的任务内容——图像、记录级问题或场景，以及在适用时的固定选项——不使用网络搜索、检索、反向图像搜索、元数据访问或辅助识别工具。图像转换为 RGB 并缩放或填充到 ⟦SLOT_80⟧，然后用各检查点原生的多模态对话模板序列化。这种模型特定的序列化不改变任务内容。

**EN** Evaluation uses deterministic decoding whenever supported. Local runs decode greedily with at most 256 new tokens. Closed-API runs use temperature 0, four concurrent requests, a 180-second timeout, and at most three transport retries. The ContextCanvas evaluator permits up to 800 output tokens for GPT-5.2 and Gemini 3.1 Pro and 500 for Qwen3.7-Plus. For the single paired-image item, checkpoints accepting only one image tensor receive a labeled horizontal contact sheet.

**ZH** 评测在支持时一律使用确定性解码。本地运行以贪婪解码、最多 256 个新词元。闭源 API 运行使用温度 0、4 个并发请求、180 秒超时与最多三次传输重试。ContextCanvas 评测器允许 GPT-5.2 与 Gemini 3.1 Pro 最多输出 800 个词元，Qwen3.7-Plus 最多 500 个。对于那一条成对图像条目，只接受单个图像张量的检查点会收到一张带标注的水平拼接图。

**EN** Table S3 summarizes the CritiqueCanvas inference configurations used in evaluation.

**ZH** 表 S3 汇总了评测中使用的 CritiqueCanvas 推理配置。

**EN** Table S3: CritiqueCanvas inference configurations. “Native” means the checkpoint’s own processor and chat template after the common ⟦SLOT_81⟧ RGB resize.

**ZH** 表 S3：CritiqueCanvas 推理配置。「Native」指在统一的 ⟦SLOT_81⟧ RGB 缩放之后，使用检查点自身的处理器与对话模板。

<!-- [原子块 · table] Model Requested model/checkpoint Precision Generation Adapter details GPT-5.2 openai/gpt-5.2 API T = 0 T=0 , 256 OpenRouter; reasoning excluded Gemini 3.1 Pro google/gemini-3.1-pro-preview API T = 0 T -->

**EN** S2.4.2 Fine-Tuning Configuration

**ZH** S2.4.2 微调配置

**EN** Qwen3-VL-FT is adapted on CritiqueCanvas and evaluated on critique generation in the main paper. At evaluation time, the resulting PEFT adapter is loaded onto Qwen3-VL-8B-Instruct without merging. Evaluation uses bfloat16 precision and SDPA, applies the base processor’s multimodal chat template to the image and record question, resizes the image to ⟦SLOT_82⟧, and decodes greedily for at most 256 new tokens.

**ZH** Qwen3-VL-FT 在 CritiqueCanvas 上适配，并在正文中参与评论生成评测。评测时，所得的 PEFT 适配器被加载到 Qwen3-VL-8B-Instruct 上而不做合并。评测使用 bfloat16 精度与 SDPA，对图像与记录问题应用基座处理器的多模态对话模板，把图像缩放到 ⟦SLOT_82⟧，并以贪婪解码生成最多 256 个新词元。

**EN** S2.4.3 Output Processing and Aggregation

**ZH** S2.4.3 输出处理与聚合

**EN** The ContextCanvas parser first accepts schema-valid JSON and verifies that the answer belongs to the supplied option IDs. Narrow compatibility fallbacks accept one unambiguous answer field, a single leading option ID, or an exact Yes/No string for specialist outputs. Rationales and confidence never change the grade. The evaluator permits at most four transport attempts; retries recover a missing transport or model response and never allow revision of a valid answer.

**ZH** ContextCanvas 解析器首先接受模式合法的 JSON，并验证答案属于所提供的选项 ID。较窄的兼容性回退会接受一个无歧义的答案字段、单个前导选项 ID，或（对专用模型输出）精确的 Yes/No 字符串。推理依据与置信度从不改变评分。评测器最多允许四次传输尝试；重试只用于恢复缺失的传输或模型响应，绝不允许修改一个已经有效的答案。

**EN** The evaluation pipeline performs answer parsing and computes Accuracy, Macro-F1, Yes Rate, counterfactual directional counts, EGA, and the reported critique metrics from prediction files. Its output schema and aggregation rules are specified above.

**ZH** 评测流水线执行答案解析，并从预测文件计算准确率、Macro-F1、Yes 率、反事实方向性计数、EGA 以及所报告的评论指标。其输出模式与聚合规则见上文。

**EN** S3 Additional Analyses and Insights

**ZH** S3 补充分析与洞察

**EN** This section complements the main tables with response-level evidence and paired diagnostics. We first examine acceptance tendency and decisive-cue grounding, then combine visual counterfactuals, modality decomposition, and base–specialist comparisons to distinguish surface aesthetic fluency, visual evidence extraction, and context-sensitive judgment.

**ZH** 本节以回答级证据与配对诊断补充主表。我们先考察接受倾向与决定性线索定位，然后把视觉反事实、模态分解与基座-专用模型比较结合起来，以区分表面的美学流畅度、视觉证据提取与上下文敏感的判断。

**EN** S3.1 Model-Output Analysis

**ZH** S3.1 模型输出分析

**EN** S3.1.1 Aggregate Behavioral Patterns

**ZH** S3.1.1 聚合行为模式

**EN** The main ContextCanvas table shows differences not only in exact-match accuracy but also in the direction of errors. Against a 38.14% gold Yes rate, the four aesthetic-specific models predict Yes for 59.11–76.98% of the 291 two-option cases. The strongest closed-source models instead predict Yes for 20.96–30.24% of cases. These rates expose a systematic difference in decision tendency: aesthetic specialists more often accept images whose formal or surface qualities appear plausible despite a contextual mismatch.

**ZH** 正文中的 ContextCanvas 表格显示，差异不仅体现在精确匹配准确率上，也体现在错误方向上。相对 38.14% 的金标准 Yes 率，四个美学专用模型在 291 个双选项案例中有 59.11–76.98% 预测 Yes。最强的闭源模型则只在 20.96–30.24% 的案例中预测 Yes。这些比例暴露了决策倾向上的系统性差异：美学专用模型更常接受那些形式或表面品质看似合理、实则与上下文错配的图像。

**EN** Table S4 expands the main results into class-specific F1. The strongest closed-source models remain effective on both labels, whereas several open-weight and aesthetic-specific models have very low No-class F1. Q-SiT is the clearest example: its 76.98% Yes rate is accompanied by only 4.05 No-class F1. Conversely, GPT-5.2 is conservative, with a 20.96% Yes rate and a much larger gap between Yes- and No-class F1. Thus similar overall scores can conceal different failure profiles.

**ZH** 表 S4 把主结果展开为按类别的 F1。最强的闭源模型在两个标签上都保持有效，而若干开源权重与美学专用模型的 No 类 F1 极低。Q-SiT 是最典型的例子：它 76.98% 的 Yes 率伴随的 No 类 F1 只有 4.05。反之，GPT-5.2 较为保守，Yes 率为 20.96%，Yes 类与 No 类 F1 之间的差距也大得多。因此，相近的总体分数可能掩盖不同的失败剖面。

**EN** Table S4: Class-specific behavior on the 291 two-option ContextCanvas cases. All values are percentages. The gold Yes rate is 38.14%.

**ZH** 表 S4：291 个双选项 ContextCanvas 案例上的类别特定行为。所有数值均为百分比。金标准 Yes 率为 38.14%。

<!-- [原子块 · table] Model Yes F1 No F1 Pred. Yes Claude Opus 5 87.44 93.47 30.24 Gemini 3.1 Pro 77.01 89.11 26.12 GPT-5.5 73.30 86.96 27.49 Claude Opus 4.6 56.84 79.08 27.15 GPT-5.2 50.00 79.02 20.96 GLM-5V-Turbo 47.06 6 -->

**EN** Prediction tendency does not by itself reveal whether the rationale uses the decisive image evidence. On the 100-case grounding audit, Gemini retains 79 of 83 correct decisions under EGA, while GPT-5.2 retains 55 of 65 and Qwen3.7-Plus retains 31 of 42. ArtiMuse falls from 21 correct labels to only three answers that are also grounded and correctly linked to the use scenario. The Accuracy-to-EGA reduction therefore complements predicted Yes rate by separating label tendency from grounded success.

**ZH** 预测倾向本身并不能说明推理是否使用了决定性的图像证据。在 100 案例的定位审计中，Gemini 在 83 个正确决策中有 79 个在 EGA 下保留，GPT-5.2 为 65 个中保留 55 个，Qwen3.7-Plus 为 42 个中保留 31 个。ArtiMuse 则从 21 个正确标签跌到只有 3 个同时有据且正确关联到使用场景的回答。因此，准确率到 EGA 的下降补充了预测 Yes 率，把标签倾向与有据的正确区分开来。

**EN** S3.1.2 Cross-Model Case Studies

**ZH** S3.1.2 跨模型案例研究

**EN** Cultural-aesthetic alignment. Figure S4 compares five models on HB208. The image has an attractive moon-centered composition, but its characters and visual language are tied to Japanese Touhou fan culture rather than an unqualified Chinese Mid-Autumn identity. Gemini 3.1 Pro and GPT-5.2 reject the image. Qwen3.7-Plus instead maps the full moon, tea, bamboo, and rabbits directly to Chinese Mid-Autumn symbolism. ArtiMuse repeats the positive formal framing and accepts it. ArtQuant-APDD also predicts Yes, accompanied only by the title-like phrase “A Serene Moment in a Chinese Landscape,” which misidentifies the cultural setting. The disagreement is therefore not whether the image is appealing, but whether that aesthetic reading is culturally valid for the stated use.

**ZH** 文化-美学对齐。图 S4 比较了五个模型在 HB208 上的表现。该图像构图以月亮为中心、颇为美观，但其人物与视觉语言隶属于日本东方同人文化，而非无条件的中国中秋身份。Gemini 3.1 Pro 与 GPT-5.2 拒绝了该图像。Qwen3.7-Plus 则把满月、茶、竹与兔子直接映射到中国中秋象征。ArtiMuse 重复了正面的形式化框定并予以接受。ArtQuant-APDD 也预测 Yes，只附上一句类似标题的短语「A Serene Moment in a Chinese Landscape」，误认了文化语境。因此，分歧不在于图像是否好看，而在于这种美学解读对于所述用途是否在文化上成立。

<!-- [原子块 · img]  -->

**EN** Figure S4: Cross-model outputs for ContextCanvas case HB208 (gold: No). GPT-5.2 and Gemini 3.1 Pro reject the image, whereas Qwen3.7-Plus, ArtiMuse, and ArtQuant-APDD accept it. The displayed responses illustrate whether models recognize the culturally specific visual identity rather than relying only on surface festival cues.

**ZH** 图 S4：五个模型在 ContextCanvas 案例 HB208（金标签：No）上的输出。GPT-5.2 与 Gemini 3.1 Pro 拒绝该图像，而 Qwen3.7-Plus、ArtiMuse 与 ArtQuant-APDD 予以接受。所展示的回答反映了模型是否识别出具有文化特定性的视觉身份，而非仅依赖表面的节庆线索。

**EN** Aesthetic valence versus communicative function. Figure S5 compares five models on HB181, which tests whether models can distinguish pleasant appearance from effective visual rhetoric. Several models reject the painting because its rough water, dark tonal range, tilted boat, and forceful diagonal net produce instability and tension rather than a conventionally uplifting image. Yet these formal qualities intensify the visible coordination of the two workers: their aligned bodies and shared control of the net make cooperation legible precisely under pressure. The case shows that contextual aesthetic suitability may depend on how composition, tone, and visual tension serve a communicative purpose, rather than on positive surface affect alone.

**ZH** 美学效价与传播功能。图 S5 比较了五个模型在 HB181 上的表现，该案例检验模型能否区分「外观悦目」与「视觉修辞有效」。若干模型拒绝这幅画，理由是它的汹涌水面、暗色调、倾斜的小船与有力的对角线渔网营造出不稳定与紧张，而非一幅惯常意义上令人振奋的图像。然而这些形式品质恰恰强化了两位劳动者协作的可见性：他们对齐的身体与对渔网的共同控制，正是在压力下使协作变得可读。该案例表明，上下文美学适配性可能取决于构图、色调与视觉张力如何服务于传播目的，而非仅取决于正面的表面情绪。

<!-- [原子块 · img]  -->

**EN** Figure S5: ArtQuant-APDD returns a bare Yes response without an explanatory rationale;

**ZH** 图 S5：ArtQuant-APDD 只返回一个光秃秃的 Yes，没有给出解释性推理依据；

**EN** Critique quality. Figure S6 supplies a complementary generation-side comparison. Valid critiques of the same image may emphasize different visual evidence or aesthetic criteria, so low overlap with one reference does not necessarily imply low practical quality. The three selected cases contrast grounded image-specific analysis with hallucinated subjects, medium-inappropriate criteria, and fluent but generic interpretations.

**ZH** 评论质量。图 S6 提供了生成侧的互补比较。对同一图像的有效评论可能强调不同的视觉证据或美学准则，因此与某一参考的重叠度低并不必然意味着实用质量低。所选的三个案例把有据的、针对具体图像的分析，与幻觉出的主体、媒介不当的准则，以及流畅但泛泛的解读做了对比。

<!-- [原子块 · img]  -->

**EN** Figure S6: Three CritiqueCanvas cases compared across five models. From top to bottom: CC001 (illustration), CC003 (photograph), and CC002 (painting). The panel preserves each prompt and representative output excerpt, exposing differences in visual grounding, medium specificity, and analytical focus.

**ZH** 图 S6：五个模型在三个 CritiqueCanvas 案例上的比较。从上到下：CC001（插画）、CC003（照片）与 CC002（绘画）。该图保留了每条提示与代表性输出摘录，暴露出模型在视觉定位、媒介专属性与分析焦点上的差异。

**EN** S3.1.3 Failure Modes and Representative Outputs

**ZH** S3.1.3 失败模式与代表性输出

**EN** The qualitative outputs instantiate the four failure levels introduced in the main paper. Fluent but visually ungrounded critiques invent objects or properties absent from the image. Domain-blind quality priors apply a photographic defect vocabulary, such as blur or noise, to intentional painterly texture. Surface aesthetics over communicative fit treats attractive or unattractive affect as sufficient evidence of suitability. Stylistic plausibility over contextual fit accepts an image because its palette, composition, or period atmosphere appears coherent while overlooking the identity, convention, or narrative that determines the use.

**ZH** 定性输出具体化了正文提出的四类失败层次。流畅但缺乏视觉依据的评论会编造图像中不存在的物体或属性。盲视领域的质量先验会把模糊、噪点等摄影缺陷词汇套用于有意为之的绘画质感。以表面美学取代传播契合，则把吸引人或令人不适的情绪当作适配性的充分证据。以风格合理性取代上下文契合，会因图像的色调、构图或时代氛围显得自洽而接受它，却忽视了决定用途的身份、惯例或叙事。

**EN** The ContextCanvas casebook further illustrates three recurrent subtypes without claiming corpus-wide frequencies. In cultural-neighbor substitution, a nearby visual convention is mapped to the wrong occasion or identity (HB208, HB014). In aesthetic-halo errors, refinement or spectacle is treated as proof of contextual appropriateness (HB037, HB186). In salient-composition myopia, a dominant formal cue suppresses a smaller but decisive action or relation (HB106, HB181). These labels summarize reviewed examples; a frequency claim would require an independent coding pass over all 301 cases.

**ZH** ContextCanvas 案例集还呈现了三种反复出现的子类型，但不声称其语料级频率。在「文化近邻替换」中，一个相近的视觉惯例被映射到错误的场合或身份（HB208、HB014）。在「美学光环错误」中，精致感或奇观性被当作上下文恰当性的证明（HB037、HB186）。在「显著构图短视」中，一个占主导的形式线索压制了更小但具决定性的动作或关系（HB106、HB181）。这些标签是对已评审示例的概括；若要给出频率断言，则需要对全部 301 个案例做一次独立的编码。

**EN** Figure S7 distinguishes a correct grounded response, a correct but unsupported label, a fluent but incorrect rationale, and a free-form response illustrating output-format sensitivity.

**ZH** 图 S7 区分了四种情形：正确且有据的回答、正确但无支撑的标签、流畅但错误的推理，以及一个展示输出格式敏感性的自由形式回答。

<!-- [原子块 · img]  -->

**EN** Figure S7: Response-level scoring diagnostics on E004 (top) and HB208 (bottom). E004 contrasts a grounded GPT-5.2 rationale with an unsupported ArtQuant-APDD label. HB208 contrasts fluent but incorrect Qwen3.7-Plus reasoning with an ArtQuant-APDD free-form response that illustrates output-format and parser sensitivity.

**ZH** 图 S7：E004（上）与 HB208（下）上的回答级评分诊断。E004 对比了 GPT-5.2 有据的推理与 ArtQuant-APDD 无支撑的标签。HB208 对比了 Qwen3.7-Plus 流畅但错误的推理，与 ArtQuant-APDD 展示输出格式与解析器敏感性的自由形式回答。

**EN** S3.2 Extended and Robustness Analyses

**ZH** S3.2 扩展与稳健性分析

**EN** S3.2.1 Extended Main Results

**ZH** S3.2.1 扩展主结果

**EN** The binary error decomposition in Table S4 explains why Macro-F1 is lower than exact-match accuracy for many models: the gold set is No-majority, while several models disproportionately predict Yes. In particular, matching the marginal gold Yes rate is not sufficient—Grok’s 37.80% predicted Yes rate is close to 38.14%, but its Macro-F1 is only 39.09%. Contextual competence depends on instance-level alignment rather than calibration of the marginal label count.

**ZH** 表 S4 中的二元错误分解解释了为何许多模型的 Macro-F1 低于精确匹配准确率：金标签集以 No 为多数，而若干模型不成比例地预测 Yes。特别地，仅仅匹配边缘的金标准 Yes 率是不够的——Grok 37.80% 的预测 Yes 率接近 38.14%，但其 Macro-F1 只有 39.09%。上下文能力取决于实例级的对齐，而非边缘标签计数的校准。

**EN** The main paper also promises response-level statistics beyond reference-matching metrics. Table S5 reports output length, average dimension coverage, dimension density, adherence to dimension-focused prompts, and the most frequent dimensions in otherwise generic critiques. As defined in Section S2.3, these are descriptive measures of response form and explicit coverage rather than direct measures of correctness or critique quality.

**ZH** 正文还承诺给出参考匹配指标之外的回答级统计。表 S5 报告输出长度、平均维度覆盖、维度密度、对维度聚焦提示的遵循程度，以及其他情况下泛泛而谈的评论中最常出现的维度。如第 S2.3 节所定义，这些都是对回答形式与显式覆盖的描述性度量，而非对正确性或评论质量的直接度量。

**EN** Table S5: Generation style and aesthetic-dimension coverage on CritiqueCanvas. Len/Ref is average output length relative to the reference; DimHits is the average number of explicitly addressed dimensions; aesthetic-term density is the number of matched lexical/phrase occurrences per 100 words. Prompt Align requires every dimension detected in a focused prompt to be detected in the response. Generic Top 3 excludes prompts that explicitly request a dimension.

**ZH** 表 S5：CritiqueCanvas 上的生成风格与美学维度覆盖。Len/Ref 是输出长度相对参考的平均值；DimHits 是明确涉及的维度平均数；美学术语密度是每 100 词中匹配到的词汇/短语出现次数。Prompt Align 要求聚焦提示中检测到的每个维度都在回答中被检测到。Generic Top 3 排除那些明确要求某一维度的提示。

<!-- [原子块 · table] Model Length Len/Ref DimHits Density Prompt Align Generic Top 3 Dimensions Closed-source Models Gemini 3.1 Pro 166.58 1.241 6.53 11.87 90.8% Composition, Emotion, Lighting GPT-5.2 141.52 1.054 5.71 8. -->

**EN** The statistics expose three complementary patterns. First, response length is not a proxy for useful aesthetic analysis: Qwen3-VL produces the longest critiques (199.07 words under the evaluation tokenizer), whereas UniPercept is substantially shorter (102.12) but has the highest dimension density (13.26). Second, breadth and controllability vary independently. Gemini obtains the broadest dimension coverage (6.53 dimensions), while Qwen3-VL has the strongest focused-prompt alignment (95.2%); by contrast, ArtQuant and AesExpert follow such prompts much less reliably (66.7% and 34.4%). Third, generic critiques concentrate heavily on composition, content, and emotion across model families. Lighting, color, and brushstrokes appear among the top dimensions for only a few models, while technique, symbolism, and style never enter the generic top three. Thus, models differ markedly in verbosity and response concentration, but their open-ended critiques still rely on a relatively narrow set of salient aesthetic concepts. These patterns complement—rather than replace—the direct quality audit below, since greater length or dimension coverage does not establish that the corresponding claims are relevant, correct, or visually grounded.

**ZH** 这些统计揭示了三个互补的模式。其一，回答长度并不是有用美学分析的代理：Qwen3-VL 生成的评论最长（在评测分词器下为 199.07 词），而 UniPercept 短得多（102.12），却有着最高的维度密度（13.26）。其二，广度与可控性各自独立变化。Gemini 取得最宽的维度覆盖（6.53 个维度），而 Qwen3-VL 的聚焦提示对齐最强（95.2%）；相比之下，ArtQuant 与 AesExpert 对这类提示的遵循可靠度低得多（66.7% 与 34.4%）。其三，泛泛的评论在各模型系列中都高度集中于构图、内容与情绪。光影、色彩与笔触只在少数模型中进入前列维度，而技法、象征与风格从未进入泛泛评论的前三。因此，各模型在啰嗦程度与回答集中度上差异明显，但其开放式评论仍依赖一组相对狭窄的显著美学概念。这些模式是对下文直接质量审计的补充而非替代，因为更长的篇幅或更广的维度覆盖并不意味着相应论断相关、正确或有视觉依据。

**EN** S3.2.2 Critique Metric Validity

**ZH** S3.2.2 评论指标有效性

**EN** Using the 100-case audit protocol described in Section S2.3.2, Table S6 reproduces the aggregate direct ratings reported in the main paper.

**ZH** 使用第 S2.3.2 节描述的 100 案例审计协议，表 S6 复现了正文中报告的聚合直接评分。

**EN** Table S6: Aggregate human and MLLM ratings of critique quality on 100 randomly sampled CritiqueCanvas cases.

**ZH** 表 S6：100 个随机抽样 CritiqueCanvas 案例上人类与 MLLM 对评论质量的聚合评分。

<!-- [原子块 · table] Model Human MLLM judge GPT-5.2 3.9 5.0 Gemini 3.1 Pro 4.1 4.5 Qwen3-VL-FT 2.5 2.5 ArtiMuse 2.6 2.6 ArtQuant-APDD 2.3 2.2 -->

**EN** The human ordering is consistent with the complementary judge at the group level: GPT-5.2 and Gemini receive higher direct-quality ratings than the adapted or aesthetic-specific models, although they do not dominate all reference-similarity metrics. This supports a narrow conclusion. Lexical and semantic reference alignment captures similarity to one expert answer but only partially reflects grounding, image specificity, criterion choice, and practical usefulness when multiple analyses are defensible. It does not show that BLEU, SBERT, or CLIPScore is generally invalid. Figure S6 provides illustrative examples of this mismatch: critiques with lower reference similarity can remain visually grounded and analytically useful, whereas closer stylistic alignment does not necessarily prevent generic analysis or unsupported visual claims.

**ZH** 人类的排序在组别层面与互补裁判一致：GPT-5.2 与 Gemini 获得的直接质量评分高于适配后的或美学专用的模型，尽管它们并未在所有参考相似度指标上占优。这支持一个狭义的结论。词汇与语义的参考对齐刻画的是与某一个专家答案的相似度，而当多种分析都能成立时，它只能部分反映定位、图像专属性、准则选择与实用有用性。这并不意味着 BLEU、SBERT 或 CLIPScore 一般而言无效。图 S6 给出了这种错配的示例性说明：参考相似度较低的评论仍可能视觉上有据且分析上有用，而风格上更接近的对齐也未必能避免泛泛的分析或无支撑的视觉断言。

**EN** S3.2.3 Counterfactual and Grounding Analyses

**ZH** S3.2.3 反事实与定位分析

**EN** Visual counterfactual sensitivity.

**ZH** 视觉反事实敏感性。

**EN** Controlled visual counterfactuals can diagnose reliance on decisive image evidence (Chen et al., 2020). We construct 36 matched No-to-Yes pairs by replacing a decisive incompatible visual cue with a scenario-compatible alternative while keeping the use scenario fixed.

**ZH** 受控的视觉反事实可用于诊断模型对决定性图像证据的依赖（Chen et al., 2020）。我们通过把决定性的不兼容视觉线索替换为与场景兼容的替代物、同时保持使用场景不变，构造了 36 组由 No 到 Yes 的配对。

**EN** Table S7 reports original and edited accuracy, Pair Accuracy, directional updates, and the NCU defined in Section S2.3.3. Pair Accuracy requires both the incompatible original and compatible edit to be classified correctly.

**ZH** 表 S7 报告原始与编辑后的准确率、配对准确率、方向性更新，以及第 S2.3.3 节定义的 NCU。配对准确率要求不兼容的原始图像与兼容的编辑图像都被正确分类。

**EN** Table S7: Counterfactual audit on 36 pairs. Full and Orig. are accuracies on the complete benchmark and selected incompatible originals; Edit is accuracy on compatible edits. Pair requires both labels to be correct. C/R are correct and reverse directional updates. NCU confidence intervals are paired bootstrap intervals.

**ZH** 表 S7：36 组配对上的反事实审计。Full 与 Orig. 分别是完整基准与所选不兼容原始图像上的准确率；Edit 是兼容编辑图像上的准确率。Pair 要求两个标签都正确。C/R 是正确与反向的方向性更新。NCU 置信区间为配对 bootstrap 区间。

<!-- [原子块 · table] Model Full Orig. Edit Pair C/R NCU 95% CI GPT-5.2 71.43 72.22 58.33 36.11 13/2 30.56 [11.11, 50.00] Gemini 3.1 Pro 85.71 86.11 38.89 27.78 10/1 25.00 [8.33, 41.67] Qwen3.7-Plus 51.83 52.78 75.00 30.56 -->

**EN** The three general-purpose models occupy a narrow 25.00–30.56 NCU range despite substantially different original accuracy. ArtQuant changes its decision on only five pairs, with three correct and two reverse updates, producing an NCU of 2.78 whose interval includes zero. ArtiMuse makes six correct and no reverse updates, but predicts Yes for 64 of the 72 original/edit images. Its 97.22% edited accuracy therefore largely reflects an acceptance tendency; Pair Accuracy and NCU provide the more discriminative diagnosis. The mean NCU is 27.78 for the three general-purpose models and 9.72 for the two specialists.

**ZH** 三个通用模型尽管原始准确率相差很大，NCU 却集中在 25.00–30.56 这一狭窄区间。ArtQuant 只在五组上改变了决策，其中三次正确、两次反向，NCU 为 2.78，其区间包含零。ArtiMuse 有六次正确更新、零次反向更新，但在 72 张原始/编辑图像中有 64 张预测 Yes。因此它 97.22% 的编辑准确率在很大程度上反映的是一种接受倾向；配对准确率与 NCU 提供了更具区分力的诊断。三个通用模型的平均 NCU 为 27.78，两个专用模型为 9.72。

**EN** The rationale audit additionally reveals source-scene anchoring: some responses repeat a canonical narrative even after its supporting visual cue is removed.

**ZH** 推理依据审计还揭示了「源场景锚定」现象：一些回答在其支撑视觉线索被移除后，仍在复述某个经典叙事。

**EN** Figure S8 presents representative interventions with each model’s before–after prediction.

**ZH** 图 S8 给出了代表性干预及各模型干预前后的预测。

<!-- [原子块 · img]  -->

**EN** Figure S8: Four No-to-Yes counterfactual interventions. From left to right: CF20/HB163 (coercion to reassurance), CF18/HB084 (isolation to inclusion), CF28/E108 (incomplete to completed journey), and CF35/HB075 (incompatibility to friendliness). Each column shows the original and edited image, the targeted intervention, and each model’s before–after prediction; colored boxes indicate agreement or disagreement with the corresponding gold label.

**ZH** 图 S8：四组由 No 到 Yes 的反事实干预。从左至右：CF20/HB163（从胁迫到安抚）、CF18/HB084（从孤立到融入）、CF28/E108（从未完成到完成的旅程）与 CF35/HB075（从不相容到友善）。每一列给出原始与编辑后的图像、所针对的干预，以及每个模型干预前后的预测；彩色框表示与相应金标签的一致或不一致。

**EN** Evidence-grounded accuracy.

**ZH** 证据定位准确率。

**EN** Using the EGA and Unsupported definitions in Section S2.3.3, Table S8 expands the 100-case audit.

**ZH** 使用第 S2.3.3 节中的 EGA 与 Unsupported 定义，表 S8 展开了 100 案例审计。

**EN** Table S8: Decisive-cue grounding on 100 ContextCanvas cases.

**ZH** 表 S8：100 个 ContextCanvas 案例上的决定性线索定位。

<!-- [原子块 · table] Model Accuracy EGA Unsupported (%) Gemini 3.1 Pro 83 79 4.82 GPT-5.2 65 55 15.38 Qwen3.7-Plus 42 31 26.19 ArtiMuse 21 3 85.71 ArtQuant-APDD 27 0 100.00 -->

**EN** ArtiMuse is the cleaner specialist diagnosis because it always generates a substantive rationale: its fall from 21 correct labels to 3 grounded correct answers cannot be attributed to missing explanation text. Its prose is often fluent and aesthetically framed, but it seldom identifies and correctly binds the culture- or context-bearing cue. The audit therefore addresses the concern that binary accuracy alone may reward lucky labels or unsupported agreement.

**ZH** ArtiMuse 是更干净的专用模型诊断对象，因为它总会生成实质性的推理：它从 21 个正确标签跌到 3 个有据的正确回答，不能归因于缺少解释文本。它的行文往往流畅且以美学框定，但很少识别并正确绑定承载文化或上下文的线索。因此，该审计回应了「二元准确率可能奖励侥幸标签或无支撑的一致」这一担忧。

**EN** Perception–reasoning decomposition.

**ZH** 感知-推理分解。

**EN** Following the view of captions as task-facing visual surrogates (Yang et al., 2026a), Table S9 evaluates a 100-case diagnostic subset distinct from the 100 cases used for the evidence-grounding audit. Four conditions are compared: question and options only (Text); an identity- and verdict-free description of visible content (Neutral); the same description with the decisive visible cue made explicit (Evidence); and the original image (Image).

**ZH** 遵循把字幕视为面向任务的视觉替代物这一观点（Yang et al., 2026a），表 S9 在一个与证据定位审计所用 100 个案例不同的 100 案例诊断子集上做评测。比较四种条件：仅问题与选项（Text）；对可见内容的、无身份与无结论的描述（Neutral）；同一描述但把决定性可见线索显式化（Evidence）；以及原始图像（Image）。

**EN** Table S9: Accuracy under different visual-information conditions on 100 ContextCanvas cases.

**ZH** 表 S9：100 个 ContextCanvas 案例上不同视觉信息条件下的准确率。

<!-- [原子块 · table] Model Text Neutral Evidence Image GPT-5.2 45 77 84 71 Gemini 3.1 Pro 58 86 90 86 Qwen3.7-Plus 44 78 88 52 ArtQuant-APDD 16 20 19 27 ArtiMuse 16 32 47 20 -->

**EN** Text-only performance does not exceed the 61% majority baseline. Supplying a neutral visual description improves the three general-purpose models by 28–34 points; for each model, the paired exact two-sided McNemar test gives ⟦SLOT_83⟧. This confirms that the judgments depend materially on visual content. The modality gap is model-specific: Gemini matches its image accuracy from a neutral description, whereas Qwen rises from 52% with images to 78% with neutral descriptions and 88% when the decisive cue is explicit. ArtiMuse is partly rescued by explicit evidence but remains far below the general-purpose models; ArtQuant remains weak across all conditions. Together with the counterfactual and EGA results, these conditions provide a diagnostic of whether errors are more consistent with limited visual-evidence extraction or with failure to use explicitly supplied contextual evidence; they are not a definitive causal decomposition.

**ZH** 纯文本性能不超过 61% 的多数基线。提供中性的视觉描述使三个通用模型提升 28–34 个点；对每个模型，配对精确双侧 McNemar 检验给出 ⟦SLOT_83⟧。这确认了这些判断实质依赖视觉内容。模态差距是模型特定的：Gemini 仅凭中性描述就追平了它的图像准确率，而 Qwen 从图像条件下的 52% 上升到中性描述的 78%，并在决定性线索显式化时达到 88%。ArtiMuse 在显式证据下得到部分改善，但仍远低于通用模型；ArtQuant 在所有条件下都表现疲弱。结合反事实与 EGA 结果，这些条件提供了一项诊断，用于判断错误更符合「视觉证据提取受限」还是「未能使用显式提供的上下文证据」；它们并非确定性的因果分解。

**EN** S3.2.4 Base-to-Specialist Transfer

**ZH** S3.2.4 基座到专用模型的迁移

**EN** Table S10 compares four aesthetic specialists with the base checkpoint identified by their implementation and model documentation. Because every pair is evaluated on the same 301 cases, we report the two discordant counts, a paired bootstrap interval for the accuracy change, an exact two-sided McNemar test, and the Bonferroni-adjusted value across four lineages.

**ZH** 表 S10 把四个美学专用模型与由其实现与模型文档确定的基座检查点做比较。由于每一对都在相同的 301 个案例上评测，我们报告两个不一致的计数、准确率变化的配对 bootstrap 区间、精确双侧 McNemar 检验，以及跨四条谱系的 Bonferroni 校正值。

**EN** Table S10: Paired base-to-specialist ContextCanvas transfer. ⟦SLOT_84⟧ counts cases correct only for the base and ⟦SLOT_85⟧ cases correct only for the specialist. Raw McNemar ⟦SLOT_86⟧-values and Bonferroni-adjusted values are both shown.

**ZH** 表 S10：配对的基座到专用模型 ContextCanvas 迁移。⟦SLOT_84⟧ 统计只有基座答对的案例，⟦SLOT_85⟧ 统计只有专用模型答对的案例。同时给出原始 McNemar ⟦SLOT_86⟧ 值与 Bonferroni 校正后的值。

<!-- [原子块 · table] Base → \rightarrow specialist Base Spec. Δ \Delta b / c b/c 95% CI p / p adj p/p_{\mathrm{adj}} mPLUG-Owl2 → \rightarrow ArtQuant 20.27 29.57 +9.30 29/57 [3.32, 15.28] .0034/.0134 InternVL3-8B → \righ -->

**EN** Specialization has a heterogeneous effect. ArtQuant and AesExpert significantly improve over their corresponding bases after correction, while ArtiMuse and Q-SiT show no measurable ContextCanvas gain. Thus, specialization does not produce consistent gains in contextual judgment.

**ZH** 专精化的效果是异质的。经校正后，ArtQuant 与 AesExpert 相对各自基座显著提升，而 ArtiMuse 与 Q-SiT 在 ContextCanvas 上没有可测量的增益。因此，专精化并不能在上下文判断上带来一致的提升。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] An et al. (2025) X. An, Y. Xie, K. Yang, W. Zhang, X. Zhao, Z. Cheng, Y. Wang, S. Xu, C. Chen, D. Zhu, C. Wu, H. Tan, C. Li, J. Yang, J. Yu, X. Wang, B. Qin, Y. Wang, Z. Yan, Z. Feng, Z. Liu, B. Li, a -->

<!-- [原子块 · verbatim] Bai et al. (2025) S. Bai, Y. Cai, R. Chen, K. Chen, X. Chen, Z. Cheng, L. Deng, W. Ding, C. Gao, C. Ge, W. Ge, Z. Guo, Q. Huang, J. Huang, F. Huang, B. Hui, S. Jiang, Z. Li, M. Li, M. Li, K. Li, Z. Li -->

<!-- [原子块 · verbatim] Banerjee and Lavie (2005) S. Banerjee and A. Lavie METEOR: an automatic metric for MT evaluation with improved correlation with human judgments . In Proceedings of the ACL Workshop on Intrinsic and Ex -->

<!-- [原子块 · verbatim] Bird et al. (2009) S. Bird, E. Klein, and E. Loper Natural language processing with python . O’Reilly Media . Cited by: §S2.3.2 . -->

<!-- [原子块 · verbatim] Cai et al. (2024) C. Cai, R. Zhang, J. Gao, K. Wu, K. Yap, and Y. Wang Temporal sentence grounding with temporally global textual knowledge . In 2024 IEEE International Conference on Multimedia and Ex -->

<!-- [原子块 · verbatim] Cao et al. (2025a) S. Cao, J. Li, X. Li, Y. Pu, K. Zhu, Y. Gao, S. Luo, Y. Xin, Q. Qin, Y. Zhou, X. Chen, W. Zhang, B. Fu, Y. Qiao, and Y. Liu UniPercept: towards unified perceptual-level image unders -->

<!-- [原子块 · verbatim] Cao et al. (2025b) S. Cao, N. Ma, J. Li, X. Li, L. Shao, K. Zhu, Y. Zhou, Y. Pu, J. Wu, J. Wang, B. Qu, W. Wang, Y. Qiao, D. Yao, and Y. Liu ArtiMuse: fine-grained image aesthetics assessment with joi -->

<!-- [原子块 · verbatim] Cao et al. (2025c) S. Cao, N. Ma, J. Li, X. Li, L. Shao, K. Zhu, Y. Zhou, Y. Pu, J. Wu, J. Wang, B. Qu, W. Wang, Y. Qiao, D. Yao, and Y. Liu ArtiMuse: Fine-Grained Image Aesthetics Assessment with Joi -->

<!-- [原子块 · verbatim] Chen et al. (2024) D. Chen, R. Chen, S. Zhang, Y. Liu, Y. Wang, H. Zhou, Q. Zhang, Y. Wan, P. Zhou, and L. Sun MLLM-as-a-Judge: assessing multimodal LLM-as-a-judge with vision-language benchmark . arX -->

<!-- [原子块 · verbatim] Chen et al. (2020) L. Chen, X. Yan, J. Xiao, H. Zhang, S. Pu, and Y. Zhuang Counterfactual samples synthesizing for robust visual question answering . In Proceedings of the IEEE/CVF Conference on Comp -->

<!-- [原子块 · verbatim] Dunn (1961) O. J. Dunn Multiple comparisons among means . Journal of the American Statistical Association 56 ( 293 ), pp. 52–64 . External Links: Document Cited by: §S2.3.3 . -->

<!-- [原子块 · verbatim] Efron and Tibshirani (1993) B. Efron and R. J. Tibshirani An introduction to the bootstrap . Chapman and Hall/CRC . External Links: Document Cited by: §S2.3.3 . -->

<!-- [原子块 · verbatim] Gao et al. (2024) J. Gao, K. Yap, K. Wu, D. T. Phan, K. Garg, and B. S. Han Contextual human object interaction understanding from pre-trained large language model . In ICASSP 2024-2024 IEEE Internati -->

<!-- [原子块 · verbatim] GLM-V Team et al. (2026) GLM-V Team, W. Hong, W. Yu, X. Gu, G. Wang, et al. GLM-4.5V and GLM-4.1V-Thinking: towards versatile multimodal reasoning with scalable reinforcement learning . arXiv preprint -->

<!-- [原子块 · verbatim] Hessel et al. (2021) J. Hessel, A. Holtzman, M. Forbes, R. Le Bras, and Y. Choi CLIPScore: a reference-free evaluation metric for image captioning . In Proceedings of the 2021 Conference on Empirical  -->

<!-- [原子块 · verbatim] Hou et al. (2026) W. Hou, W. Liu, H. Hu, X. Sun, S. Yeung-Levy, and H. Fan Seeing is believing? a benchmark for multimodal large language models on visual illusions and anomalies . arXiv preprint arXi -->

<!-- [原子块 · verbatim] Huang et al. (2024a) Y. Huang, X. Sheng, Z. Yang, Q. Yuan, Z. Duan, P. Chen, L. Li, W. Lin, and G. Shi AesExpert: towards multi-modality foundation model for image aesthetics perception . External Lin -->

<!-- [原子块 · verbatim] Huang et al. (2024b) Y. Huang, Q. Yuan, X. Sheng, Z. Yang, H. Wu, P. Chen, Y. Yang, L. Li, and W. Lin AesBench: an expert benchmark for multimodal large language models on image aesthetics perception  -->

<!-- [原子块 · verbatim] Huang et al. (2024c) Y. Huang, Q. Yuan, X. Sheng, Z. Yang, H. Wu, P. Chen, Y. Yang, L. Li, and W. Lin AesBench: An expert benchmark for multimodal large language models on image aesthetics perception  -->

<!-- [原子块 · verbatim] Kong et al. (2016) S. Kong, X. Shen, Z. Lin, R. Mech, and C. C. Fowlkes Photo aesthetics ranking network with attributes and content adaptation . In Computer Vision – ECCV 2016 , Lecture Notes in Comp -->

<!-- [原子块 · verbatim] Li et al. (2024) C. Li, Z. Zhang, H. Wu, W. Sun, X. Min, X. Liu, G. Zhai, and W. Lin AGIQA-3K: an open database for ai-generated image quality assessment . IEEE Transactions on Circuits and Systems fo -->

<!-- [原子块 · verbatim] Li et al. (2026) R. Li, L. Li, S. Ren, H. Tian, S. Gu, S. Li, Z. Yue, Y. Wang, W. Ma, Z. Yang, J. Ma, Z. Sui, and F. Luo GroundingME: exposing the visual grounding gap in MLLMs through multi-dimension -->

<!-- [原子块 · verbatim] Liang et al. (2026) J. Liang, K. Wu, X. Hu, and T. Liu Cibic: pixel-free foundation model for robust corrupted image bitstream captioning . Pattern Recognition , pp. 114238 . Cited by: §II.B . -->

<!-- [原子块 · verbatim] Liao et al. (2026) M. Liao, T. Ma, and X. Zhang Open world image aesthetic assessment . In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition Findings , pp. 9791–9801 .  -->

<!-- [原子块 · verbatim] Lin (2004) C. Lin ROUGE: a package for automatic evaluation of summaries . In Text Summarization Branches Out , Barcelona, Spain , pp. 74–81 . External Links: Link Cited by: §III.C , §S2.3.2 . -->

<!-- [原子块 · verbatim] Liu et al. (2024) H. Liu, C. Li, Y. Li, and Y. J. Lee Improved baselines with visual instruction tuning . In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition , pp. 262 -->

<!-- [原子块 · verbatim] Liu et al. (2026) H. Liu, N. Huang, C. Liu, J. Yan, H. Huang, J. Ying, T. Lee, P. Wan, and X. Ji Bridging cognitive gap: Hierarchical description learning for artistic image aesthetics assessment . Ex -->

<!-- [原子块 · verbatim] Liu et al. (2023) Y. Liu, D. Iter, Y. Xu, S. Wang, R. Xu, and C. Zhu G-Eval: NLG evaluation using GPT-4 with better human alignment . In Proceedings of the 2023 Conference on Empirical Methods in Natu -->

<!-- [原子块 · verbatim] Mai et al. (2016) L. Mai, H. Jin, and F. Liu Composition-preserving deep photo aesthetics assessment . In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition , pp. 497–506 .  -->

<!-- [原子块 · verbatim] McNemar (1947) Q. McNemar Note on the sampling error of the difference between correlated proportions or percentages . Psychometrika 12 ( 2 ), pp. 153–157 . External Links: Document Cited by: §S2.3.3  -->

<!-- [原子块 · verbatim] Moratelli et al. (2026) N. Moratelli, C. Davis, L. F. R. Ribeiro, B. Byrne, and G. Iglesias Benchmarking deflection and hallucination in large vision-language models . arXiv preprint arXiv:2604.12033  -->

<!-- [原子块 · verbatim] Murray et al. (2012) N. Murray, L. Marchesotti, and F. Perronnin AVA: a large-scale database for aesthetic visual analysis . In Proceedings of the IEEE Conference on Computer Vision and Pattern Recogn -->

<!-- [原子块 · verbatim] Papineni et al. (2002) K. Papineni, S. Roukos, T. Ward, and W. Zhu Bleu: a method for automatic evaluation of machine translation . In Proceedings of the 40th Annual Meeting of the Association for Com -->

<!-- [原子块 · verbatim] Post (2018) M. Post A call for clarity in reporting BLEU scores . In Proceedings of the Third Conference on Machine Translation: Research Papers , pp. 186–191 . External Links: Document Cited by: §S2. -->

<!-- [原子块 · verbatim] Qi et al. (2025a) D. Qi, H. Zhao, J. Shi, S. Jenni, Y. Fan, F. Dernoncourt, S. Cohen, and S. Li The photographer eye: teaching multimodal large language models to see and critique like photographers . -->

<!-- [原子块 · verbatim] Qi et al. (2025b) D. Qi, H. Zhao, J. Shi, S. Jenni, Y. Fan, F. Dernoncourt, S. Cohen, and S. Li The photographer’s eye: teaching multimodal large language models to see, and critique like photographer -->

<!-- [原子块 · verbatim] Reimers and Gurevych (2019) N. Reimers and I. Gurevych Sentence-BERT: sentence embeddings using Siamese BERT-networks . In Proceedings of the 2019 Conference on Empirical Methods in Natural Language P -->

<!-- [原子块 · verbatim] Satar et al. (2025) B. Satar, Z. Ma, P. A. Irawan, W. A. Mulyawan, J. Jiang, E. Lim, and C. Ngo Seeing culture: a benchmark for visual reasoning and grounding . In Proceedings of the 2025 Conference o -->

<!-- [原子块 · verbatim] Singh et al. (2026) D. Singh, A. Nagrani, K. Manikantan, H. Singh, D. Tewari, T. Weyand, C. Schmid, A. Angelova, and S. Dave CURVE: a benchmark for cultural and multilingual long video reasoning . arX -->

<!-- [原子块 · verbatim] Talebi and Milanfar (2018) H. Talebi and P. Milanfar NIMA: neural image assessment . IEEE Transactions on Image Processing 27 ( 8 ), pp. 3998–4011 . External Links: Document Cited by: §I . -->

<!-- [原子块 · verbatim] Wang et al. (2023) J. Wang, H. Duan, J. Liu, S. Chen, X. Min, and G. Zhai AIGCIQA2023: a large-scale image quality assessment database for ai generated images: from the perspectives of quality, authen -->

<!-- [原子块 · verbatim] Wang et al. (2025) W. Wang, Z. Gao, L. Gu, H. Pu, L. Cui, X. Wei, Z. Liu, L. Jing, S. Ye, J. Shao, Z. Wang, Z. Chen, H. Zhang, G. Yang, H. Wang, Q. Wei, J. Yin, W. Li, E. Cui, G. Chen, Z. Ding, C. Tia -->

<!-- [原子块 · verbatim] Wu et al. (2024) H. Wu, Z. Zhang, W. Zhang, C. Chen, L. Liao, C. Li, Y. Gao, A. Wang, E. Zhang, W. Sun, Q. Yan, X. Min, G. Zhai, and W. Lin Q-Align: teaching LMMs for visual scoring via discrete text- -->

<!-- [原子块 · verbatim] Wu et al. (2026a) K. Wu, F. Li, W. Liu, Q. Liu, and Y. Yang Corrupted bitstream semantic understanding by adaptive-modal large language models . Pattern Recognition 180 , pp. 114151 . Cited by: §II.B  -->

<!-- [原子块 · verbatim] Wu et al. (2026b) Q. Wu, X. Yang, Y. Zhou, C. Fang, B. Song, X. Sun, and R. Ji Grounded chain-of-thought for multimodal large language models . In Proceedings of the IEEE/CVF Conference on Computer Vi -->

<!-- [原子块 · verbatim] Xiong et al. (2026) T. Xiong, Y. Ge, M. Li, Z. Zhang, P. Kulkarni, K. Wang, Q. He, Z. Zhu, C. Liu, R. Chen, T. Zheng, Y. Chen, X. Wang, R. Zhang, W. Chen, and H. Huang Multi-Crit: benchmarking multimo -->

<!-- [原子块 · verbatim] Yang et al. (2026a) S. Yang, Y. Liu, B. Zhai, X. Sun, Z. Liu, E. Barsoum, M. Li, and C. Xu CaptionQA: is your caption as useful as the image itself? . In Proceedings of the IEEE/CVF Conference on Comp -->

<!-- [原子块 · verbatim] Yang et al. (2022) Y. Yang, L. Xu, L. Li, N. Qie, Y. Li, P. Zhang, and Y. Guo Personalized image aesthetics assessment with rich attributes . In Proceedings of the IEEE/CVF Conference on Computer Visi -->

<!-- [原子块 · verbatim] Yang et al. (2026b) Z. Yang, J. Wang, Z. Zhang, P. Xie, X. Sheng, P. Chen, and L. Li Fine-grained image aesthetic assessment: learning discriminative scores from relative ranks . In Proceedings of the -->

<!-- [原子块 · verbatim] Ye et al. (2024) Q. Ye, H. Xu, J. Ye, M. Yan, A. Hu, H. Liu, Q. Qian, J. Zhang, and F. Huang Mplug-owl2: revolutionizing multi-modal large language model with modality collaboration . In Proceedings o -->

<!-- [原子块 · verbatim] Yi et al. (2023) R. Yi, H. Tian, Z. Gu, Y. Lai, and P. L. Rosin Towards artistic image aesthetics assessment: a large-scale dataset and a new method . In Proceedings of the IEEE/CVF Conference on Comp -->

<!-- [原子块 · verbatim] Yin et al. (2026) Y. Yin, H. Krishnakumar, C. P. Lee, B. Zeng, W. Chai, S. Tong, W. Chen, H. Xu, X. Fu, G. Sarch, A. Korolova, and Z. Liu WorldBench: a challenging and visually diverse multimodal reas -->

<!-- [原子块 · verbatim] Zhang et al. (2026) L. Zhang, J. Yang, S. Krishnan, J. Majmudar, X. Ge, P. Puri, P. Saraf, S. Bhargava, D. Piraviperumal, Y. Ling, C. Pan, H. Yu, A. Agrawal, and B. Tseng From where things are to what -->

<!-- [原子块 · verbatim] Zhang et al. (2020) T. Zhang, V. Kishore, F. Wu, K. Q. Weinberger, and Y. Artzi BERTScore: evaluating text generation with bert . External Links: 1904.09675 , Link Cited by: §III.C , §S2.3.2 . -->

<!-- [原子块 · verbatim] Zhang et al. (2025) Z. Zhang, H. Wu, Z. Jia, W. Lin, and G. Zhai Teaching LMMs for image quality scoring and interpreting . External Links: 2503.09197 Cited by: §I , §II.B , Table 2 , Table 3 . -->

<!-- [原子块 · verbatim] Zhou et al. (2026) S. Zhou, B. Jia, K. Wu, Y. Shen, T. Li, Y. Wu, and S. Lin ReactBench: a cause-driven benchmark for multimodal hallucination via systematic evaluation . arXiv preprint arXiv:2605.295 -->

<!-- [原子块 · verbatim] Zhou et al. (2024) Z. Zhou, Q. Wang, B. Lin, Y. Su, R. Chen, X. Tao, A. Zheng, L. Yuan, P. Wan, and D. Zhang UNIAA: a unified multi-modal image aesthetic assessment baseline and benchmark . External L -->

<!-- [原子块 · verbatim] Zhu et al. (2025) J. Zhu, W. Wang, Z. Chen, Z. Liu, S. Ye, L. Gu, H. Tian, Y. Duan, W. Su, J. Shao, Z. Gao, E. Cui, X. Wang, Y. Cao, Y. Liu, X. Wei, H. Zhang, H. Wang, W. Xu, H. Li, J. Wang, N. Deng,  -->
