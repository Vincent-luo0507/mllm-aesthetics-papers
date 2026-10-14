# 看见即改进：面向迭代式文本版式优化的视觉反馈

> 原标题：Seeing is Improving: Visual Feedback for Iterative Text Layout Refinement
> 作者：Junrong Guo, Shancheng Fang, Yadong Qu, Hongtao Xie · arXiv:2603.22187 · 2026-03-23

<!-- [原子块 · verbatim] Seeing is Improving: Visual Feedback for Iterative Text Layout Refinement -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] Recent advances in Multimodal Large Language Models (MLLMs) have enabled automated generation of structured layouts from natural language descriptions. Existing methods typically follow a code-only pa -->

**EN** 1 Introduction

**ZH** 1 引言

**EN** The emergence of Large Language Models (LLMs) [1, 9, 51] and Multimodal Large Language Models (MLLMs) [18, 32, 4, 42] has unlocked new possibilities for automated content generation, particularly for structured visual layouts. By generating structured representations (e.g., SVG code, custom JSON) [11, 52, 8, 35] that define the position, size, and style of each element [22, 20], LLMs can translate natural language descriptions directly into complex designs such as typographic posters, social media graphics, and documents. MLLMs further enhance this by leveraging cross-modal understanding, allowing generation to be conditioned on both text and visual inputs.

**ZH** 大语言模型（LLM）[1, 9, 51] 与多模态大语言模型（MLLM）[18, 32, 4, 42] 的出现，为自动化内容生成——尤其是结构化视觉版式——开启了新的可能。通过生成定义每个元素位置、尺寸与样式的结构化表示（如 SVG 代码、自定义 JSON）[11, 52, 8, 35] [22, 20]，LLM 可以把自然语言描述直接翻译成字体海报、社交媒体图与文档等复杂设计。MLLM 则借助跨模态理解进一步强化了这一能力，使生成可以同时以文本与视觉输入为条件。

<!-- [原子块 · img]  -->

**EN** Figure 1: Method comparison. Traditional methods only generate through text code and have no perception of the generated results; our Visual Feedback method can iteratively reflect on the generated result and optimize the layout effect.

**ZH** 图 1：方法对比。传统方法只通过文本代码生成，对生成结果没有感知；我们的视觉反馈方法可以对生成结果进行迭代反思，并优化版式效果。

**EN** However, existing methods are limited to the code-only paradigm and can only generate codes for layout without considering visual feedback. For instance, COLE [22] and OpenCOLE [20] leverage LLMs to generate typography JSON files, while LGGPT [57] produces customized layout output formats, which are then composed into the final images by a graphic renderer. As shown in Fig. 1(A), while these models can produce layout structures that meet formal specifications, they remain unable to perceive the visual outcomes of their designs. Effective text layout design, however, depends on visual properties such as aesthetic balance, readability, and image–text coherence, which cannot be fully encoded by programmatic rules. Consequently, a model may generate syntactically valid SVG layouts that still suffer from overlapping elements, poor contrast, or misaligned components.

**ZH** 然而现有方法局限于纯代码范式，只能生成版式代码而不考虑视觉反馈。例如 COLE [22] 与 OpenCOLE [20] 利用 LLM 生成排版 JSON 文件，LGGPT [57] 产出定制的版式输出格式，再由图形渲染器合成为最终图像。如图 1(A) 所示，这些模型虽能产出符合形式规范的版式结构，却始终无法感知其设计的视觉结果。而有效的文本版式设计依赖于美学平衡、可读性与图文连贯性等视觉属性，这些无法被程序化规则完全编码。因此，一个模型可能生成句法上合法的 SVG 版式，却仍然存在元素重叠、对比度过差或组件错位的问题。

**EN** Recent advances in LLMs [9, 21, 32, 12] research demonstrate that reflection, backtracking, and self-validation mechanisms can substantially improve performance on complex reasoning tasks. Moreover, Reinforcement Learning (RL) [34, 38, 40] techniques have proven effective in activating the reflective reasoning capabilities of LLMs. This motivates our core research question: Can such reflection capabilities be transferred to text layout generation to overcome the visual perception gap in existing approaches? We argue that the solution lies in incorporating visual feedback into the text layout generation process, leveraging MLLMs’ inherent cross-modal understanding capabilities. As illustrated in Fig. 1, models should not only generate layout code but also perceive the rendered results to evaluate quality, diagnose visual issues, and devise optimization strategies through iterative refinement.

**ZH** LLM [9, 21, 32, 12] 研究的近期进展表明，反思、回溯与自验证机制能显著提升复杂推理任务上的性能。此外，强化学习（RL）[34, 38, 40] 技术已被证明能有效激活 LLM 的反思推理能力。这引出了我们的核心研究问题：这类反思能力能否迁移到文本版式生成中，以克服现有方法的视觉感知缺口？我们认为，解决方案在于把视觉反馈引入文本版式生成过程，利用 MLLM 固有的跨模态理解能力。如图 1 所示，模型不仅应生成版式代码，还应感知渲染结果以评估质量、诊断视觉问题，并通过迭代优化制定改进策略。

**EN** In this paper, we propose Visual Feedback Layout Model (VFLM), a novel self-improving framework for text layout generation that establishes a closed-loop process guided by RL. As shown in Fig. 1, VFLM first generates initial SVG layout code, which is rendered into a visual image. This rendered image is fed back to the same model for visual inspection and reflection. If issues are identified or the layout is unsatisfactory, VFLM generates revised code and repeats the process, creating a continuous loop of “generation, rendering, reflection and refinement” until a satisfactory layout is achieved.

**ZH** 本文提出视觉反馈版式模型（VFLM），一种用于文本版式生成的自改进框架，建立了由 RL 引导的闭环流程。如图 1 所示，VFLM 先生成初始 SVG 版式代码，再将其渲染为视觉图像。该渲染图像被反馈给同一模型做视觉检查与反思。若发现问题或版式不理想，VFLM 生成修订后的代码并重复该过程，形成「生成—渲染—反思—优化」的持续循环，直至得到令人满意的版式。

**EN** VFLM utilizes a two-stage training pipeline. Firstly, we construct a multi-stage generation-reflection-refinement trajectory dataset by distilling advanced MLLMs, followed by Supervised Fine-Tuning (SFT) to endow model the ability of iterative generation. Secondly, we employ RL to enhance the model’s reflective capabilities. We utilize a reward model trained to evaluate layout quality holistically and incorporate text accuracy via Optical Character Recognition (OCR). While recent research on Agentic RL research [41, 10, 25] often relies on meticulously designed, complex, process-oriented reward mechanisms to guide each intermediate step, our analysis reveals this approach can lead to “reward hacking”. We demonstrate, counter-intuitively, that a simple outcome-based reward, which only assesses the final generated layout, is significantly more effective. This simpler signal compels the VFLM to leverage its inherent visual understanding to holistically balance initial generation quality and iterative refinement, enabling robust and stable performance improvements through visual feedback.

**ZH** VFLM 采用两阶段训练流程。第一，我们通过蒸馏先进 MLLM 构造多阶段的「生成—反思—优化」轨迹数据集，随后做监督微调（SFT），赋予模型迭代生成的能力。第二，我们用 RL 增强模型的反思能力。我们使用一个经训练、用于整体评估版式质量的奖励模型，并通过光学字符识别（OCR）纳入文本准确率。近期关于智能体 RL 的研究 [41, 10, 25] 往往依赖精心设计的、复杂的、面向过程的奖励机制来引导每一个中间步骤，而我们的分析表明这种做法会导致「奖励劫持」。我们反直觉地证明：只评估最终生成版式的、简单的基于结果的奖励，效果显著更好。这一更简单的信号促使 VFLM 利用其固有的视觉理解，整体地平衡初始生成质量与迭代优化，从而借助视觉反馈实现稳健、稳定的性能提升。

**EN** We validate this framework through extensive experiments based on Qwen2.5-VL-7B model [4] for the task of laying out target text on background images. Both quantitative and qualitative evaluations show VFLM significantly outperforms state-of-the-art layout generation approaches, advanced MLLMs, and image editing models. Furthermore, our ablation studies, which provide fair comparisons against multiple code-only generation methods, confirm the significant and critical advantage of our VFLM. This superiority effectively validates visual feedback as a crucial component in generative text layout, establishing a practical framework for developing self-improving, MLLM-based design agents.

**ZH** 我们以 Qwen2.5-VL-7B 模型 [4] 为基础，在把目标文本排版到背景图像这一任务上，通过大量实验验证了该框架。定量与定性评测都显示，VFLM 显著优于当前最优的版式生成方法、先进 MLLM 与图像编辑模型。此外，我们的消融研究与多种纯代码生成方法做了公平比较，证实了 VFLM 显著而关键的优势。这一优势有效验证了视觉反馈在生成式文本版式中的关键作用，为开发自改进的、基于 MLLM 的设计智能体建立了实用框架。

**EN** This work’s contributions can be summarized as follows:

**ZH** 本文贡献可概括如下：

**EN** • We propose VFLM, a self-improving framework that, to our knowledge, is the first to apply visual feedback to layout generation. It equips MLLMs with a “generation, rendering, reflection, refinement” cycle, using visual feedback to overcome the limitations of code-only methods.

**ZH** • 我们提出 VFLM，一个自改进框架，据我们所知是首个把视觉反馈应用于版式生成的工作。它为 MLLM 装备了「生成—渲染—反思—优化」的循环，用视觉反馈克服纯代码方法的局限。

**EN** • We design a two-stage SFT+RL training method, including a novel reward model for text layout, that successfully activates the model’s iterative refinement capabilities. Extensive experiments validate that our approach consistently outperforms strong existing methods.

**ZH** • 我们设计了两阶段 SFT+RL 训练方法，包含一个面向文本版式的新型奖励模型，成功激活了模型的迭代优化能力。大量实验验证了本方法持续优于已有的强方法。

**EN** • We demonstrate a key finding that simple, outcome-based rewards are more effective and robust for activating the model’s self-improvement capabilities than complex, process-oriented reward functions.

**ZH** • 我们证明了一项关键发现：在激活模型自改进能力方面，简单的基于结果的奖励比复杂的面向过程的奖励函数更有效、更稳健。

**EN** 2 Related Work

**ZH** 2 相关工作

**EN** 2.1 Multimodal Large Language Model

**ZH** 2.1 多模态大语言模型

**EN** Recent progress in Multimodal Large Language Models (MLLMs) is driven by integrating pretrained vision encoders [36, 54] with LLMs. The two modalities are typically aligned via lightweight projectors or Q-Former [24] structures, a paradigm that has spurred a suite of powerful models. This includes open-source series like LLaVA [31, 29, 30], Qwen-VL [3, 45, 4], and Intern-VL [7, 13, 61, 46], as well as large-scale proprietary systems such as GPT-4o [18], Gemini [43], and Claude [2], which continue to advance the state of the art through massive scaling and enhanced reasoning techniques [47, 58].

**ZH** 多模态大语言模型（MLLM）的近期进展由「把预训练视觉编码器 [36, 54] 与 LLM 集成」所驱动。两种模态通常通过轻量投影器或 Q-Former [24] 结构对齐，这一范式催生了一系列强大的模型，包括 LLaVA [31, 29, 30]、Qwen-VL [3, 45, 4]、Intern-VL [7, 13, 61, 46] 等开源系列，以及 GPT-4o [18]、Gemini [43]、Claude [2] 等大规模专有系统——后者通过大规模扩展与增强的推理技术 [47, 58] 持续推进技术前沿。

**EN** 2.2 Graphic Layout Generation

**ZH** 2.2 图形版式生成

**EN** Graphic layout generation has evolved from early Transformer-based architectures [60, 28] to methods centered on LLMs and MLLMs. Many approaches prompts LLMs to output structured formats like SVG [44], HTML [39], or JSON [26, 22, 20, 6, 15]. Others employ MLLMs to decompose the design process into ordered layers or sub-tasks [8, 27, 22, 35], often coordinating with multi-modal inputs [52, 19]. However, these methods operate in an open-loop, lacking visual perception of the rendered output. While some recent pipelines incorporate visual feedback, they typically rely on non-trainable, inference-only strategies with external advisors [53, 55], or decouple generation and reflection into separately trained models [22]. In contrast, our work introduces visual feedback via RL, unifying these capabilities into a single, self-evolving policy with learnable autonomous judgment.

**ZH** 图形版式生成已从早期的基于 Transformer 的架构 [60, 28]，演化为以 LLM 与 MLLM 为中心的方法。许多方法提示 LLM 输出 SVG [44]、HTML [39] 或 JSON [26, 22, 20, 6, 15] 等结构化格式；另一些则用 MLLM 把设计过程分解为有序的图层或子任务 [8, 27, 22, 35]，并常与多模态输入协同 [52, 19]。然而这些方法都在开环下运作，缺少对渲染输出的视觉感知。尽管部分近期管线纳入了视觉反馈，它们通常依赖不可训练、仅用于推理的带外部顾问的策略 [53, 55]，或把生成与反思解耦为分别训练的模型 [22]。与之不同，本工作通过 RL 引入视觉反馈，把这些能力统一到单一、自演化的策略中，使其具备可习得的自主判断力。

**EN** 2.3 Reinforcement Learning

**ZH** 2.3 强化学习

**EN** Reinforcement learning is a cornerstone for aligning LLMs with human preferences, standardized by the RLHF [34] pipeline which typically uses Proximal Policy Optimization (PPO) [38]. To mitigate the instability and high cost associated with PPO, recent alternatives like Direct Preference Optimization (DPO) [37] and Group Relative Policy Optimization (GRPO) [40] offer more direct and efficient optimization strategies. This alignment paradigm extends naturally to multimodal settings to improve visual grounding and reasoning. Works such as Vision-R1 [17], R1VL [56], and DeepEyes [59] adapt RL to MLLMs by incorporating multimodal rewards, chain-of-thought signals, and specialized replay mechanisms, demonstrating the power of RL in enhancing multimodal alignment and capability.

**ZH** 强化学习是把 LLM 与人类偏好对齐的基石，其标准化流程是 RLHF [34]，通常使用权近策略优化（PPO）[38]。为缓解 PPO 的不稳定性与高昂成本，近期出现了直接偏好优化（DPO）[37] 与组相对策略优化（GRPO）[40] 等替代方案，提供更直接、更高效的优化策略。这一对齐范式自然地延伸到多模态场景，以改善视觉定位与推理。Vision-R1 [17]、R1VL [56] 与 DeepEyes [59] 等工作通过引入多模态奖励、思维链信号与专门的重放机制，把 RL 适配到 MLLM 上，展示了 RL 在增强多模态对齐与能力上的威力。

**EN** 3 Method

**ZH** 3 方法

<!-- [原子块 · img]  -->

**EN** Figure 2: Pipeline of Visual Feedback Method, including Data Construction for Cold-Start SFT and RL with Modified Advantages.

**ZH** 图 2：视觉反馈方法的流程，包括用于冷启动 SFT 的数据构造与带改进优势函数的 RL。

**EN** This work aims to develop a self-improving VFLM for text layout generation that optimizes outputs through visual feedback. We achieve this with a two-stage training framework: (1) Cold-Start SFT to instill basic iterative generation and reflection capabilities, and (2) Reinforcement Learning to enhance performance using vision-based reward signals.

**ZH** 本工作旨在开发一种用于文本版式生成的自改进 VFLM，通过视觉反馈优化输出。我们以两阶段训练框架实现：（1）冷启动 SFT，注入基本的迭代生成与反思能力；（2）强化学习，利用基于视觉的奖励信号提升性能。

**EN** 3.1 Visual Feedback Layout Model

**ZH** 3.1 视觉反馈版式模型

**EN** As illustrated in Fig. 1, VFLM establishes a multi-round interaction mechanism between VFLM and a rendering environment. As shown in Algorithm 1, given a background image and target text, VFLM executes an iterative generation, rendering, reflection, refinement cycle:

**ZH** 如图 1 所示，VFLM 在自身与渲染环境之间建立了多轮交互机制。如算法 1 所示，给定背景图像与目标文本，VFLM 执行迭代的「生成—渲染—反思—优化」循环：

**EN** 1. Initial Generation: The VFLM first analyzes the input through reasoning, then generates initial layout code through a structured tool call.

**ZH** 1. 初始生成：VFLM 先通过推理分析输入，再通过结构化工具调用生成初始版式代码。

**EN** 2. Rendering: The rendering tool converts the SVG code into a visual image and feeds it back to the same VFLM.

**ZH** 2. 渲染：渲染工具把 SVG 代码转换为视觉图像，并反馈给同一个 VFLM。

**EN** 3. Visual Reflection: The VFLM examines the rendered layout visual image through reasoning to evaluate whether the quality is satisfactory to it.

**ZH** 3. 视觉反思：VFLM 通过推理检查渲染出的版式视觉图像，评估其质量是否令自己满意。

**EN** 4. Iterative Refinement: If unsatisfied, the VFLM reasons about necessary modifications and a revised layout code is generated. The process repeats until the model determines satisfaction with the layout quality.

**ZH** 4. 迭代优化：若不满意，VFLM 推理所需的修改并生成修订后的版式代码。该过程不断重复，直至模型判定版式质量令人满意。

**EN** Algorithm 1 Visual Feedback for Text Layout Self-Improvement

**ZH** 算法 1 面向文本版式自改进的视觉反馈

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

<!-- [原子块 · math]  -->

**EN** 3.2 Cold-Start Supervised Fine-Tuning

**ZH** 3.2 冷启动监督微调

**EN** The cold-start SFT stage enables the model to acquire iterative reflection capabilities, and tool usage specifications through distillation from an advanced teacher MLLM.

**ZH** 冷启动 SFT 阶段通过从先进教师 MLLM 蒸馏，使模型获得迭代反思能力与工具使用规范。

**EN** Data Construction Due to the absence of natural multi-round reflection data, we employ Doubao-Seed-1.6 [5] as a teacher model for data synthesis. As illustrated in Fig. 2(A), the systhesis pipeline is divided into the following stages:

**ZH** 数据构造　由于缺少天然的多轮反思数据，我们采用 Doubao-Seed-1.6 [5] 作为教师模型做数据合成。如图 2(A) 所示，合成流程分为以下阶段：

**EN** 1. Initial reasoning synthesis: First, The teacher model is prompted with background images and ground-truth layouts to generate the reasoning processes for SVG code generation.

**ZH** 1. 初始推理合成：首先以背景图像与真值版式提示教师模型，生成 SVG 代码生成的推理过程。

**EN** 2. Suboptimal layout generation: This distilled reasoning data is used to fine-tune Qwen2.5-VL-7B. The inference outputs from this model are then collected to serve as the suboptimal initial attempts for the next stage.

**ZH** 2. 次优版式生成：用这批蒸馏得到的推理数据微调 Qwen2.5-VL-7B，再收集该模型的推理输出，作为下一阶段的次优初始尝试。

**EN** 3. Multi-round reflection synthesis: The suboptimal attempts (from Stage 2) are paired with their ground-truth layouts and fed back to the teacher model. The teacher is then instructed to perform iterative reflection and modification to reach the ground-truth solution. This process simulates realistic human design refinement and generates complete multi-round reflection trajectories.

**ZH** 3. 多轮反思合成：把（第 2 阶段的）次优尝试与其真值版式配对后反馈给教师模型，并指示教师执行迭代反思与修改，直至达到真值解。该过程模拟真实的人工设计优化，生成完整的多轮反思轨迹。

**EN** 4. Data combination: Finally, the synthesized data from the above stages are combined and organized using structured tags: intermediate rounds use <think> and <tool_call>, while the final round uses <think> and <answer> (See supplementary materials for specific data samples.).

**ZH** 4. 数据组合：最后把上述各阶段合成的数据组合起来，并用结构化标签组织：中间轮使用 <think> 与 <tool_call>，最后一轮使用 <think> 与 <answer>（具体数据样本见补充材料）。

**EN** Training Objective We fine-tune Qwen2.5-VL-7B using causal language modeling on the synthesized multi-round reflection trajectories data. To prevent the model from learning suboptimal outputs, the loss for initial responses in improvement sequences is masked, ensuring the model learns from the correction process rather than initial errors.

**ZH** 训练目标　我们在合成的多轮反思轨迹数据上以因果语言建模微调 Qwen2.5-VL-7B。为防止模型学到次优输出，改进序列中初始回答的损失被掩码，确保模型从修正过程中学习，而不是从初始错误中学习。

**EN** 3.3 Iterative Reflection Reinforcement Learning

**ZH** 3.3 迭代反思强化学习

**EN** 3.3.1 RL Algorithm

**ZH** 3.3.1 RL 算法

**EN** We adopt the Group Relative Policy Optimization (GRPO) [40] algorithm for RL and make certain improvements to the advantage function. Compared with traditional policy optimization methods, GRPO performs policy gradient optimization within sample groups, enabling the model to learn in the direction of maximizing rewards. The optimization objectives of GRPO are as follows:

**ZH** 我们采用组相对策略优化（GRPO）[40] 算法做 RL，并对优势函数做了若干改进。相比传统的策略优化方法，GRPO 在样本组内执行策略梯度优化，使模型朝最大化奖励的方向学习。GRPO 的优化目标如下：

<!-- [原子块 · table] 𝒥 GRPO ​ ( θ ) = 𝔼 ⁡ [ q ∼ P ⁡ ( Q ) , { o i } i = 1 G ∼ π θ old ​ ( O ∣ q ) ] 1 G ∑ i = 1 G 1 | o i | ∑ t = 1 | o i | { min [ π θ ​ ( o i , t ∣ q , o i , < t ) π θ old ​ ( o i , t ∣ q , o i , < t ) A -->

**EN** where ⟦SLOT_0⟧ and ⟦SLOT_1⟧ are the clipping hyperparameters and the KL divergence penalty coefficient, respectively.

**ZH** 其中 ⟦SLOT_0⟧ 与 ⟦SLOT_1⟧ 分别为裁剪超参数与 KL 散度惩罚系数。

**EN** For the reward function, we design a three-component reward function to score the layout effect: (1) ⟦SLOT_2⟧(Sec. 3.3.2), a specialized reward model trained to evaluate overall layout quality; (2) ⟦SLOT_3⟧, which evaluates text accuracy based on OCR results from the rendered layout; and (3) ⟦SLOT_4⟧, which measures text accuracy at the code level by comparing the extracted SVG strings with the target text. The total reward is the weighted sum of the three components:

**ZH** 奖励函数方面，我们设计了一个三组件的奖励函数来为版式效果打分：（1）⟦SLOT_2⟧（第 3.3.2 节），一个经训练、用于评估整体版式质量的专用奖励模型；（2）⟦SLOT_3⟧，依据渲染版式的 OCR 结果评估文本准确率；（3）⟦SLOT_4⟧，通过比对抽取出的 SVG 字符串与目标文本，在代码层面度量文本准确率。总奖励是三个分量的加权和：

<!-- [原子块 · table] R score = R layout + α ⋅ ( R ocr + R svg ) , R_{\text{score}}=R_{\text{layout}}+\alpha\cdot\left(R_{\text{ocr}}+R_{\text{svg}}\right), (2) -->

**EN** where ⟦SLOT_5⟧ balance aesthetic quality against functional accuracy. In addition, we incorporate a format reward to constrain the output format of the model:

**ZH** 其中 ⟦SLOT_5⟧ 用于平衡美学质量与功能准确率。此外，我们引入一个格式奖励来约束模型的输出格式：

<!-- [原子块 · table] R format = { 1.0 , if format is correct , − 1.0 , if format is incorrect . R_{\text{format}}=\begin{cases}1.0,&\text{if format is correct},\\ -1.0,&\text{if format is incorrect}.\end{cases} (3) -->

**EN** For the advantage function, since the multi-round nature of our approach, the format rewards are applied separately in each round, resulting in inconsistent rewards between rounds for a sequence. Referring to REINFORCE++ [16], we use the mean value of ⟦SLOT_6⟧ within a group as baseline to reshape the reward. The format rewards are then incorporated with a scaling factor ⟦SLOT_7⟧. Finally, the advantages in the global batch are normalized and used for GRPO training:

**ZH** 对优势函数，由于本方法具有多轮性质，格式奖励在每一轮分别施加，导致一个序列的各轮之间奖励不一致。参照 REINFORCE++ [16]，我们把组内 ⟦SLOT_6⟧ 的均值作为基线来重塑奖励，格式奖励再以缩放因子 ⟦SLOT_7⟧ 纳入。最后，对全局批次中的优势做归一化并用于 GRPO 训练：

<!-- [原子块 · table] A raw = R score − mean group ​ ( R score ) + γ ⋅ R format , A_{\text{raw}}=R_{\text{score}}-\mathrm{mean}_{\text{group}}(R_{\text{score}})+\gamma\cdot R_{\text{format}}, (4) -->

<!-- [原子块 · table] A = A raw − mean batch ​ ( A raw ) std batch ​ ( A raw ) . A=\frac{A_{\text{raw}}-\mathrm{mean}_{\text{batch}}(A_{\text{raw}})}{\mathrm{std}_{\text{batch}}(A_{\text{raw}})}. (5) -->

**EN** 3.3.2 Layout Reward Model

**ZH** 3.3.2 版式奖励模型

**EN** Training a robust reward model for text layout is uniquely challenging. Unlike tasks with binary correctness, layout quality is a holistic and fine-grained judgment of aesthetics, readability, and coherence. A high-quality preference dataset is crucial for training a model that can guide a stable RL without falling into reward hacking. However, no existing datasets or methodologies are specifically designed for layout generation reward modeling. To address this gap, we train a specialized reward model ⟦SLOT_8⟧ that takes triplets ⟦SLOT_9⟧ as input and outputs a scalar score ⟦SLOT_10⟧, where ⟦SLOT_11⟧ denotes the background image, ⟦SLOT_12⟧ denotes the target text, and ⟦SLOT_13⟧ denotes the rendered layout image.

**ZH** 为文本版式训练一个稳健的奖励模型具有独特的挑战性。与有二元正确性判据的任务不同，版式质量是对美学、可读性与连贯性的整体性、细粒度判断。高质量的偏好数据集，对训练出一个能引导稳定 RL 而不陷入奖励劫持的模型至关重要。然而现有数据集与方法学都不是专为版式生成的奖励建模而设计的。为填补这一空白，我们训练了一个专用奖励模型 ⟦SLOT_8⟧，它以三元组 ⟦SLOT_9⟧ 为输入、输出标量分数 ⟦SLOT_10⟧，其中 ⟦SLOT_11⟧ 表示背景图像，⟦SLOT_12⟧ 表示目标文本，⟦SLOT_13⟧ 表示渲染出的版式图像。

**EN** Dataset: To create the necessary preference data, we introduce a novel hierarchical data construction method that creates fine-grained quality distinctions across multiple layout quality levels.

**ZH** 数据集：为构造所需的偏好数据，我们提出一种新颖的分层数据构造方法，在多个版式质量层级之间制造细粒度的质量区分。

**EN** To equip the reward model with comprehensive and robust evaluation capabilities, we construct four distinct quality levels to capture fine-grained layout performance:

**ZH** 为使奖励模型具备全面而稳健的评估能力，我们构造了四个不同的质量层级，以捕捉细粒度的版式表现：

**EN** • Level-I: High-quality ground-truth layouts serving as gold standards for design excellence.

**ZH** • Level-I：高质量的真值版式，作为设计优秀的金标准。

**EN** • Level-II: Layouts generated by Qwen2.5-VL-7B after fine-tuning on 200K samples exhibit reasonable quality with minor imperfections.

**ZH** • Level-II：在 200K 样本上微调后的 Qwen2.5-VL-7B 生成的版式，质量合理但带有轻微瑕疵。

**EN** • Level-III: Layouts from the Level-II model subjected to systematic spatial perturbations applied to layout elements, including random positional offsets that moderately compromise design coherence.

**ZH** • Level-III：对 Level-II 模型的版式元素施加系统性空间扰动后得到的版式，包括会适度损害设计连贯性的随机位置偏移。

**EN** • Level-IV: Severely degraded layouts stem from the Level-II model under aggressive perturbations, including extensive positional displacement, random font size variations, selective text element deletion, image reference removal, and arbitrary SVG scaling transformations.

**ZH** • Level-IV：在 Level-II 模型上施加剧烈扰动后严重退化的版式，包括大范围的位置位移、随机字号变化、选择性删除文本元素、移除图像引用，以及任意的 SVG 缩放变换。

**EN** This hierarchical construction enables comprehensive preference learning through systematic pairwise comparisons. For each layout generation prompt, we create layouts at all four quality levels, then form all possible pairwise comparisons between different levels. This yields 6 preference pairs per problem, establishing clear quality orderings that capture nuanced distinctions essential for effective reward model training. This strategy forces the reward model to move beyond simple binary (good/bad) judgments and learn the subtle distinctions that separate excellent layouts from merely acceptable ones. The resulting dataset provides a comprehensive and reliable basis for training a highly discerning layout reward model ⟦SLOT_14⟧.

**ZH** 这种分层构造通过系统性的成对比较实现了全面的偏好学习。对每个版式生成提示，我们在四个质量层级上各生成版式，再在不同层级之间构造所有可能的成对比较。这为每个问题产生 6 个偏好对，确立了清晰的质量序关系，捕捉到对奖励模型训练至关重要的细微差别。该策略迫使奖励模型超越简单的二元（好／坏）判断，去学习区分优秀版式与勉强可接受版式之间的细微差异。所得数据集为训练一个判别力很强的版式奖励模型 ⟦SLOT_14⟧ 提供了全面而可靠的基础。

**EN** Training: The method proposed in [33] is adopted for training the reward model. Specifically, the reward model is initialized with Qwen2.5-VL-3B. To adapt it for preference learning, the final layer is replaced with a linear layer yielding a scalar output. Subsequently, the reward model is trained via the negative log-likelihood loss function:

**ZH** 训练：我们采用 [33] 提出的方法训练奖励模型。具体地，奖励模型以 Qwen2.5-VL-3B 初始化；为适配偏好学习，把最后一层替换为输出标量的线性层。随后用负对数似然损失函数训练奖励模型：

<!-- [原子块 · table] ℒ RM ​ ( θ ) = − 𝔼 ( B , T , I + , I − ) ∼ 𝒟 ​ [ log ⁡ σ ⁡ ( r θ ​ ( B , T , I + ) − r θ ​ ( B , T , I − ) ) ] \mathcal{L}_{\mathrm{RM}}(\theta)=-\mathbb{E}_{(B,T,I^{+},I^{-})\sim\mathcal{D}}\left[\lo -->

**EN** where ⟦SLOT_15⟧ and ⟦SLOT_16⟧ denote the better-quality and lower-quality images, respectively, in a pairwise comparison.

**ZH** 其中 ⟦SLOT_15⟧ 与 ⟦SLOT_16⟧ 分别表示成对比较中质量较好的图像与质量较差的图像。

**EN** To provide stable reward values for the RL process, the raw output of ⟦SLOT_17⟧ is normalized before being used as the final layout reward ⟦SLOT_18⟧. Following the practice in [49], we standardize ⟦SLOT_19⟧ scores using the mean and standard deviation of the test set distribution. This procedure ensures that the reward signal maintains a consistent scale throughout training, which is crucial for effective policy optimization. The final reward is calculated as:

**ZH** 为给 RL 过程提供稳定的奖励值，⟦SLOT_17⟧ 的原始输出在用作最终版式奖励 ⟦SLOT_18⟧ 之前会先做归一化。沿用 [49] 的做法，我们用测试集分布的均值与标准差对 ⟦SLOT_19⟧ 分数做标准化。该过程确保奖励信号在整个训练过程中保持一致的尺度，这对有效的策略优化至关重要。最终奖励计算如下：

<!-- [原子块 · table] R layout = r θ − mean test ​ ( r θ ) std test ​ ( r θ ) . R_{\text{layout}}=\frac{r_{\theta}-\mathrm{mean}_{\text{test}}(r_{\theta})}{\mathrm{std}_{\text{test}}(r_{\theta})}. (7) -->

**EN** 4 Experiment

**ZH** 4 实验

**EN** 4.1 Experimental Setup

**ZH** 4.1 实验设置

**EN** Evaluation Datasets For evaluation, we randomly sample 1K examples from our TextLayout dataset as the primary test set, ensuring no overlap with training data. We also conduct additional experiments on the Crello [50] and DESIGNERINTENTION [22] benchmarks, preprocessed into background-text pairs.

**ZH** 评测数据集　评测时，我们从 TextLayout 数据集中随机采样 1K 个样本作为主测试集，并确保与训练数据无重叠。我们还在 Crello [50] 与 DESIGNERINTENTION [22] 基准上做了额外实验，二者已预处理为背景—文本对。

**EN** Evaluation metrics We adopt three groups of evaluation metrics. Text accuracy is measured using character-level F-measure based on OCR recognition. For graphic metrics, we adopt ⟦SLOT_20⟧, ⟦SLOT_21⟧, and ⟦SLOT_22⟧ [60, 35], which capture text position alignment, text-text overlap, and pixel gradient smoothness within text regions. Additionally, we employ GPT-4o as a judge [14] to evaluate four dimensions: Text Accuracy, Text-Background Harmony, Text Presentation Quality, and Meaning Expression Adaptability. Refer to the supplementary materials for details.

**ZH** 评测指标　我们采用三组评测指标。文本准确率以基于 OCR 识别的字符级 F 值度量。图形指标方面，我们采用 ⟦SLOT_20⟧、⟦SLOT_21⟧ 与 ⟦SLOT_22⟧ [60, 35]，分别刻画文本位置对齐、文本间重叠与文本区域内像素梯度的平滑度。此外，我们用 GPT-4o 作为裁判 [14]，评测四个维度：文本准确率、文本—背景协调性、文本呈现质量与语义表达适配性。详见补充材料。

**EN** Existing Methods We compare against three categories of existing methods: (1) Advanced MLLMs: GPT-4o [18], Claude 3.7 [2], Doubao-Seed-1.6[5], and Qwen2.5-VL-72B [4]; (2) Image editing models: GPT-4o(edit) [18], Qwen-Image-Edit [48], and FLUX-Kontext [23]; (3) Specialized layout generation: the open-source domain-specific model OpenCOLE [20] and IGD [35].

**ZH** 现有方法　我们与三类现有方法比较：（1）先进 MLLM：GPT-4o [18]、Claude 3.7 [2]、Doubao-Seed-1.6 [5] 与 Qwen2.5-VL-72B [4]；（2）图像编辑模型：GPT-4o(edit) [18]、Qwen-Image-Edit [48] 与 FLUX-Kontext [23]；（3）专用版式生成：开源领域专用模型 OpenCOLE [20] 与 IGD [35]。

**EN** Table 1: The Graphic quality metrics and OCR metrics on the TextLayout, Crello and DESIGNERINTENTION test set, where VFLM-step1 and VFLM respectively represent the metrics of our results in the first output and the final result output after iterative reflection.

**ZH** 表 1：TextLayout、Crello 与 DESIGNERINTENTION 测试集上的图形质量指标与 OCR 指标，其中 VFLM-step1 与 VFLM 分别表示我们首次输出与经迭代反思后最终输出的指标。

<!-- [原子块 · table] Method Model OCR Graphic GPT-4o Char-F ↑ \uparrow R a ​ l ​ i ↓ R_{ali}\downarrow R o ​ v ​ e ↓ R_{ove}\downarrow R c ​ o ​ m ↓ R_{com}\downarrow RM Score ↑ \uparrow Text Harmony Quality Meaning Overa -->

<!-- [原子块 · img]  -->

**EN** Figure 3: In comparison with existing methods, we selected one model from each category of methods as a representative. For a more comprehensive comparison, please refer to the supplementary materials.

**ZH** 图 3：与现有方法的对比中，我们从每类方法中各选一个模型作为代表。更全面的比较见补充材料。

**EN** 4.2 Comparison with Existing Methods

**ZH** 4.2 与现有方法的比较

**EN** As shown in Tab. 1, VFLM demonstrates a clear quantitative advantage. On the TextLayout dataset, VFLM’s initial generation (VFLM-step1) already achieves a higher OCR F1-score (0.9071) than the strongest MLLM competitor, Claude 3.7 (0.8672), and the specialized layout model IGD (0.8481). The final optimized output (VFLM) widens this gap further to 0.9376. This superiority extends across key graphic metrics: VFLM excels at minimizing element overlap (⟦SLOT_23⟧) and optimizing composition (⟦SLOT_24⟧), achieving the highest RM scores and overall GPT-4o evaluation. This strong performance generalizes robustly: VFLM consistently achieves state-of-the-art results on the Crello and DESIGNERINTENTION datasets, establishing a new SOTA on nearly all OCR and Graphic metrics.

**ZH** 如表 1 所示，VFLM 展现出明显的定量优势。在 TextLayout 数据集上，VFLM 的初始生成（VFLM-step1）已取得 0.9071 的 OCR F1 值，高于最强的 MLLM 竞争对手 Claude 3.7（0.8672）与专用版式模型 IGD（0.8481）；最终优化输出（VFLM）把这一差距进一步拉大到 0.9376。这一优势延伸到各项关键图形指标：VFLM 在最小化元素重叠（⟦SLOT_23⟧）与优化构图（⟦SLOT_24⟧）上表现优异，取得最高的 RM 分数与整体最好的 GPT-4o 评价。这种强劲表现具有良好的泛化性：VFLM 在 Crello 与 DESIGNERINTENTION 数据集上一致地取得当前最优结果，在几乎所有 OCR 与图形指标上确立了新的 SOTA。

**EN** Fig. 3 provides a qualitative comparison of VFLM against existing methods. Models like IGD and Claude 3.7, which generate layouts directly, inevitably suffer from visual artifacts such as text overlap and color conflicts. Meanwhile, image editing models like GPT4o-Image fundamentally conflict with our task, as they inevitably alter the background image. These editing models also struggle to guarantee quality in scenarios with dense text or Chinese characters. VFLM, in contrast, successfully integrates the element-wise consistency of code generation while further leveraging visual feedback to promptly discover and correct visual problems. This ensures a high-quality final output, overcoming the limitations of both competing approaches.

**ZH** 图 3 给出 VFLM 与现有方法的定性比较。IGD 与 Claude 3.7 这类直接生成版式的模型，不可避免地会出现文字重叠、颜色冲突等视觉瑕疵。同时，GPT4o-Image 这类图像编辑模型与我们的任务存在根本冲突，因为它们必然改动背景图像；这些编辑模型在文本密集或含汉字的场景下也难以保证质量。相比之下，VFLM 既保留了代码生成的元素级一致性，又进一步利用视觉反馈及时发现并纠正视觉问题，从而确保高质量的最终输出，克服了两类竞争方法各自的局限。

**EN** 4.3 Layout Reward Model Evaluation

**ZH** 4.3 版式奖励模型评测

**EN** The trained reward model achieves a high pairwise prediction accuracy of 97.4% on the preference data test set. To further validate our methodology, we conducted two key analyses presented in Tab. 2. First, we verify the integrity of our four-level data hierarchy using objective metrics. As shown, the external Graphic and OCR metrics exhibit a clear monotonic degradation from Level-I to Level-IV. Among them, ⟦SLOT_25⟧ and ⟦SLOT_26⟧ have slight improvement in Leval-III and Leval-IV because many texts in these two types of data have been lost in the layout, so text overlap and regional gradients will naturally decrease. This result confirms that our data construction process successfully creates a well-defined and reliable quality gradient.

**ZH** 训练得到的奖励模型在偏好数据测试集上取得了 97.4% 的高成对预测准确率。为验证我们方法的合理性，我们做了两项关键分析，见表 2。第一，我们用客观指标检验四级数据层级的完整性。如图所示，外部的图形指标与 OCR 指标从 Level-I 到 Level-IV 呈现清晰的单调退化。其中 ⟦SLOT_25⟧ 与 ⟦SLOT_26⟧ 在 Level-III 与 Level-IV 略有改善，因为这两类数据中许多文本在版式中已经丢失，文本重叠与区域梯度自然会下降。该结果证实我们的数据构造过程成功建立了定义清晰、可靠的质量梯度。

**EN** Table 2: Metrics and RM score across four quality-level datasets.

**ZH** 表 2：四个质量层级数据集上的指标与 RM 分数。

<!-- [原子块 · table] level OCR Graphic RM Score ↑ \uparrow Char-F ↑ \uparrow R a ​ l ​ i ↓ R_{ali}\downarrow R o ​ v ​ e ↓ R_{ove}\downarrow R c ​ o ​ m ↓ R_{com}\downarrow Level-I 0.9474 0.0089 0.0038 6.6795 1.0594 Level -->

**EN** Second, we evaluated whether our trained reward model internalizes this quality structure. The final column of the table reports the average RM Score, i.e., ⟦SLOT_27⟧, which aligns well with the established hierarchy, decreasing consistently from a high for Level-I to a low for Level-IV. This strong discriminative performance across distinct quality levels confirms that our model has learned a nuanced understanding of layout quality, enabling it to provide a reliable and effective supervision signal for reinforcement learning.

**ZH** 第二，我们评估训练出的奖励模型是否内化了这种质量结构。表格最后一列报告平均 RM Score，即 ⟦SLOT_27⟧，它与所建立的层级高度吻合，从 Level-I 的高值到 Level-IV 的低值持续下降。这种跨明显质量层级的强判别性能，证明我们的模型已习得对版式质量的细致理解，能够为强化学习提供可靠而有效的监督信号。

**EN** 4.4 Ablation Study

**ZH** 4.4 消融研究

**EN** In the ablation study, we conducted comparative experiments using TextLayout test set. To comprehensively compare the effects of our visual feedback method, we compared it against several training approaches: (1) Cold-Start Model: The cold start model mainly ensures the format of the iterative output and does not significantly improve the layout quality; (2) Single-Round RL: We trained the cold-start model using RL but restricted generation to only one step, enabling fair comparison between single-round generation and iterative visual reflection; (3) RL from Pre-trained Models: Direct RL training from the pre-trained Qwen2.5-VL-7B model without SFT initialization; (4) Direct Output: SFT+RL training was performed using the same source data as our visual feedback method for direct SVG code generation; (5) Direct Output SFT: For fair comparison with our 40K-sample SFT+RL approach, we trained a direct SFT model on 40K samples. Since these models only require a single round of generation training, we use the standard SFT loss and GRPO Advantage calculation method. For more ablation experiments on reward functions and advantage algorithms, as well as training details, please refer to the supplementary materials.

**ZH** 消融研究中，我们在 TextLayout 测试集上做了对比实验。为全面比较视觉反馈方法的效果，我们与若干训练方式对比：（1）冷启动模型：冷启动模型主要保证迭代输出的格式，对版式质量没有显著提升；（2）单轮 RL：用 RL 训练冷启动模型，但把生成限制为仅一步，以便在单轮生成与迭代视觉反思之间做公平比较；（3）从预训练模型做 RL：直接从预训练的 Qwen2.5-VL-7B 模型做 RL 训练，不经过 SFT 初始化；（4）直接输出：使用与视觉反馈方法相同的源数据做 SFT+RL 训练，直接生成 SVG 代码；（5）直接输出 SFT：为与我们 40K 样本的 SFT+RL 方案公平比较，我们在 40K 样本上训练了一个直接 SFT 模型。由于这些模型只需单轮生成训练，我们使用标准 SFT 损失与 GRPO 优势计算方法。关于奖励函数与优势算法的更多消融实验以及训练细节，见补充材料。

**EN** Table 3: Ablation experiments on Graphic quality metrics and OCR metrics on TextLayout test set.

**ZH** 表 3：TextLayout 测试集上图形质量指标与 OCR 指标的消融实验。

<!-- [原子块 · table] Model OCR Graphic RM Score ↑ \uparrow Char-F ↑ \uparrow R a ​ l ​ i ↓ R_{ali}\downarrow R o ​ v ​ e ↓ R_{ove}\downarrow R c ​ o ​ m ↓ R_{com}\downarrow VFLM-step1 0.9071 0.0035 0.0059 15.4583 0 .5415  -->

**EN** The results of our ablation study, presented in Tab. 3, demonstrate the clear superiority of our Visual Feedback method. Our VFLM achieves the best performance across the majority of metrics, substantially outperforming all RL baselines. More notably, the quality of our initial output (VFLM-step1) is already not inferior to any other competing methods. For instance, its RM score of 0.5415 even surpasses the second-best performing Direct Output SFT (0.5332). Subsequent iterative steps further widened this performance gap, increasing the RM score to 0.6018, and achieving top-notch results in both OCR and image quality. Our success highlights that our visual feedback framework is a more effective solution for layout generation, as it can establish a higher quality benchmark from the very first step and then optimize it to the state-of-the-art level.

**ZH** 表 3 给出的消融结果表明我们的视觉反馈方法具有明显优势。VFLM 在多数指标上取得最佳性能，大幅超越所有 RL 基线。更值得注意的是，我们初始输出（VFLM-step1）的质量已不逊于任何其他竞争方法：例如其 0.5415 的 RM 分数甚至超过表现第二的直接输出 SFT（0.5332）。随后的迭代进一步拉大了这一差距，把 RM 分数提升到 0.6018，并在 OCR 与图像质量上均取得顶尖结果。我们的成功凸显出：视觉反馈框架是版式生成更有效的解决方案，它能从第一步起就确立更高的质量基准，再将其优化到当前最优水平。

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

**EN** Figure 4: Comparison of training processes: simple outcom rewards vs. complex process rewards.

**ZH** 图 4：训练过程对比：简单的结果奖励 vs. 复杂的过程奖励。

**EN** 4.5 Discussion: Effectiveness of Simple Rewards

**ZH** 4.5 讨论：简单奖励的有效性

**EN** Can simple outcome-based rewards effectively stimulate self-improvement capabilities in MLLMs? Our empirical investigation provides compelling evidence that they can, and even outperform more sophisticated alternatives.

**ZH** 基于结果的简单奖励能否有效激发 MLLM 的自改进能力？我们的实证研究给出了令人信服的证据：能，而且甚至优于更精巧的替代方案。

**EN** We designed a sophisticated process-oriented reward function (Eq. 8–Eq. 10). This complex reward scheme incorporates three distinct optimization objectives: (1) first-round quality maximization using group-wise mean baselines, (2) iterative improvement encouragement via maximum-quality baselines from prior rounds, and (3) strategic termination control via reward and length penalties to prevent reward hacking. Subsequent advantages will be normalized through Eq. 5.

**ZH** 我们设计了一个精巧的面向过程的奖励函数（式 8～式 10）。该复杂奖励方案纳入三个不同的优化目标：（1）用组内均值基线最大化首轮质量；（2）用先前各轮的最高质量基线鼓励迭代改进；（3）通过奖励与长度惩罚做策略性终止控制，以防奖励劫持。随后的优势将经由式 5 归一化。

<!-- [原子块 · table] A q , o t i = { R q , o t 1 − mean group ​ ( R q , o t 1 ) if ​ i = 1 , 2 ⋅ ( R answer + R length ) if ​ i = last , 2 ⋅ ( R q , o t i − max ⁡ ( R q , o t ≤ i ) ) else , A_{q,o_{t_{i}}}=\begin{cases}R_ -->

**EN** where ⟦SLOT_28⟧ represents a complete generation path, and ⟦SLOT_29⟧ represents the response of the ⟦SLOT_30⟧-th round in this complete path. The terminal reward (⟦SLOT_31⟧) components are defined as:

**ZH** 其中 ⟦SLOT_28⟧ 表示一条完整的生成路径，⟦SLOT_29⟧ 表示该完整路径中第 ⟦SLOT_30⟧ 轮的响应。终止奖励（⟦SLOT_31⟧）的各分量定义如下：

<!-- [原子块 · table] R answer = { 0.7 if ​ R q , o t last ≥ max ⁡ ( R q , o t ≤ last ) , R q , o t last − max ⁡ ( R q , o t ≤ last ) else , R_{\text{answer}}=\begin{cases}0.7\qquad\quad\text{if }R_{q,o_{t_{\text{last}}}}\ -->

<!-- [原子块 · table] R length = − 2 ⋅ [ ( R q , o t last − max group ​ ( R q , o t last ) ) ⋅ max ( 0 , 4 − tool _ call _ count ) ] . \begin{split}R_{\text{length}}=-2\cdot\bigg[&\left(R_{q,o_{t_{\text{last}}}}-\text{max} -->

**EN** Fig. 4 illustrates the training dynamics of the two reward schemes. Before 250 steps, both algorithms improved stably: their final answer scores (middle subfigure) showed nearly identical trends, and first-round generation performance was comparable, the outcome-only reward algorithm even slightly outperform the complex process RL one. After 250 steps, the process RL converged and even suffered performance degradation, whereas the outcome-only reward continued to improve steadily until training concluded. The reward gap (right subfigure) reveals that process RL quickly widened this gap but plateaued later, which is likely due to restricted first-round learning in early training. In contrast, the outcome-only reward gradually mastered progressive iterative refinement. Tab. 4 quantifies these observations through comprehensive evaluation metrics. The simple outcome-based reward demonstrates superior effectiveness in stimulating self-improvement capabilities across all evaluation dimensions.

**ZH** 图 4 展示了两种奖励方案的训练动态。在 250 步之前，两种算法都稳定提升：它们的最终回答分数（中间子图）趋势几乎一致，首轮生成性能也相当，只采用结果奖励的算法甚至略微优于复杂的过程 RL。250 步之后，过程 RL 收敛甚至出现性能退化，而只采用结果奖励的算法则持续稳定提升直至训练结束。奖励差距（右子图）显示，过程 RL 很快拉大了这一差距但随后进入平台期，这很可能是早期训练中首轮学习受限所致。相比之下，只采用结果奖励的算法逐渐掌握了渐进式的迭代优化。表 4 用综合评测指标量化了这些观察。在所有评测维度上，简单的基于结果的奖励在激发自改进能力方面都表现出更优的效果。

**EN** Table 4: Comparison of simple outcome rewards and complex process rewards on our test set.

**ZH** 表 4：简单结果奖励与复杂过程奖励在我们测试集上的比较。

<!-- [原子块 · table] OCR Graphic level Char-F ↑ \uparrow R a ​ l ​ i ↓ R_{ali}\downarrow R o ​ v ​ e ↓ R_{ove}\downarrow R c ​ o ​ m ↓ R_{com}\downarrow RM Score ↑ \uparrow Outcome RL-step1 0.9071 0.0035 0.0059 1 5.4583 0 -->

**EN** These findings reveal a fundamental insight: under effective visual feedback mechanisms, simple outcome-based rewards can successfully harness the inherent visual understanding capabilities of MLLMs to elicit robust self-improvement behaviors, while complex process-oriented rewards may actually inhibit optimal performance, leading to the brittle local optima and “reward hacking” (policy collapse) observed in Fig. 4. This counterintuitive result suggests that the powerful internal representations and reasoning capabilities of modern MLLMs, when properly guided by clear outcome objectives and visual feedback, can autonomously develop sophisticated iterative refinement strategies without explicit process supervision.

**ZH** 这些发现揭示了一个根本性的认识：在有效的视觉反馈机制下，简单的基于结果的奖励能够成功借助 MLLM 固有的视觉理解能力，激发出稳健的自改进行为，而复杂的面向过程的奖励反而可能抑制最优性能，导致图 4 中观察到的脆弱局部最优与「奖励劫持」（策略崩塌）。这一反直觉的结果说明，现代 MLLM 强大的内部表示与推理能力，在清晰的结果目标与视觉反馈的恰当引导下，可以自主发展出精巧的迭代优化策略，而无需显式的过程监督。

**EN** 5 Conclusion

**ZH** 5 结论

**EN** This paper introduces VFLM, a self-improving framework for text layout design, bridging the critical “visual perception gap” of existing code-only methods. We implement a “generation, rendering, reflection, refinement” loop, which is trained via RL that leverages a novel, specialized layout reward model. A key finding is that rewarding only the final outcome, rather than complex intermediate steps, can more effectively stimulate the model’s self-improvement capabilities. Extensive experiments validate that VFLM consistently outperforms code-only methods, establishing visual feedback as essential for automated design and MLLM-based design agents.

**ZH** 本文提出 VFLM——一个用于文本版式设计的自改进框架，弥合了现有纯代码方法的关键「视觉感知缺口」。我们实现了「生成—渲染—反思—优化」的循环，并通过利用一个新颖的专用版式奖励模型的 RL 加以训练。一项关键发现是：只对最终结果给予奖励，而不是对复杂的中间步骤，能更有效地激发模型的自改进能力。大量实验验证了 VFLM 持续优于纯代码方法，确立了视觉反馈对自动化设计与基于 MLLM 的设计智能体的必要性。

**EN** Acknowledgments

**ZH** 致谢

**EN** This work is supported by the the National Nature Science Foundation of China (62425114, 62121002, U23B2028), and the Fundamental and Interdisciplinary Disciplines Breakthrough Plan of the Ministry of Education of China (JYB2025XDXM103).

**ZH** 本工作受国家自然科学基金（62425114、62121002、U23B2028）与教育部基础与交叉学科突破计划（JYB2025XDXM103）资助。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] [1] J. Achiam, S. Adler, S. Agarwal, L. Ahmad, I. Akkaya, F. L. Aleman, D. Almeida, J. Altenschmidt, S. Altman, S. Anadkat, et al. (2023) Gpt-4 technical report . arXiv preprint arXiv:2303.08774 . Cit -->

<!-- [原子块 · verbatim] [2] Anthropic (2025) Claude 3.7 sonnet system card . Note: https://www.anthropic.com/news/claude-3-7-sonnet Cited by: §2.1 , §4.1 . -->

<!-- [原子块 · verbatim] [3] J. Bai, S. Bai, S. Yang, S. Wang, S. Tan, P. Wang, J. Lin, C. Zhou, and J. Zhou (2023) Qwen-vl: a versatile vision-language model for understanding, localization, text reading, and beyond . arXiv  -->

<!-- [原子块 · verbatim] [4] S. Bai, K. Chen, X. Liu, J. Wang, W. Ge, S. Song, K. Dang, P. Wang, S. Wang, J. Tang, H. Zhong, Y. Zhu, M. Yang, Z. Li, J. Wan, P. Wang, W. Ding, Z. Fu, Y. Xu, J. Ye, X. Zhang, T. Xie, Z. Cheng, H -->

<!-- [原子块 · verbatim] [5] ByteDance (2025) Doubao-seed-1.6 . Note: https://research.doubao.com/zh/seed1_6 Cited by: §3.2 , §4.1 . -->

<!-- [原子块 · verbatim] [6] J. Chen, R. Zhang, Y. Zhou, J. Healey, J. Gu, Z. Xu, and C. Chen (2024) TextLap: customizing language models for text-to-layout planning . In Findings of the Association for Computational Linguist -->

<!-- [原子块 · verbatim] [7] Z. Chen, J. Wu, W. Wang, W. Su, G. Chen, S. Xing, M. Zhong, Q. Zhang, X. Zhu, L. Lu, et al. (2024) Internvl: scaling up vision foundation models and aligning for generic visual-linguistic tasks .  -->

<!-- [原子块 · verbatim] [8] Y. Cheng, Z. Zhang, M. Yang, N. Hui, C. Li, X. Wu, and J. Shao (2024) Graphic design with large multimodal model . arXiv preprint arXiv:2404.14368 . Cited by: §1 , §2.2 . -->

<!-- [原子块 · verbatim] [9] DeepSeek-AI (2025) DeepSeek-r1: incentivizing reasoning capability in llms via reinforcement learning . External Links: 2501.12948 , Link Cited by: §1 , §1 . -->

<!-- [原子块 · verbatim] [10] G. Dong, H. Mao, K. Ma, L. Bao, Y. Chen, Z. Wang, Z. Chen, J. Du, H. Wang, F. Zhang, et al. (2025) Agentic reinforced policy optimization . arXiv preprint arXiv:2507.19849 . Cited by: §1 . -->

<!-- [原子块 · verbatim] [11] W. Feng, W. Zhu, T. Fu, V. Jampani, A. Akula, X. He, S. Basu, X. E. Wang, and W. Y. Wang (2024) Layoutgpt: compositional visual planning and generation with large language models . Advances in Ne -->

<!-- [原子块 · verbatim] [12] K. Gandhi, A. Chakravarthy, A. Singh, N. Lile, and N. D. Goodman (2025) Cognitive behaviors that enable self-improving reasoners, or, four habits of highly effective stars . arXiv preprint arXiv: -->

<!-- [原子块 · verbatim] [13] Z. Gao, Z. Chen, E. Cui, Y. Ren, W. Wang, J. Zhu, H. Tian, S. Ye, J. He, X. Zhu, et al. (2024) Mini-internvl: a flexible-transfer pocket multi-modal model with 5% parameters and 90% performance . -->

<!-- [原子块 · verbatim] [14] D. Haraguchi, N. Inoue, W. Shimoda, H. Mitani, S. Uchida, and K. Yamaguchi (2024) Can gpts evaluate graphic design based on design principles? . In SIGGRAPH Asia 2024 Technical Communications , p -->

<!-- [原子块 · verbatim] [15] H. Hsu and Y. Peng (2025) PosterO: structuring layout trees to enable language models in generalized content-aware layout generation . In Proceedings of the Computer Vision and Pattern Recognitio -->

<!-- [原子块 · verbatim] [16] J. Hu, J. K. Liu, H. Xu, and W. Shen (2025) Reinforce++: an efficient rlhf algorithm with robustness to both prompt and reward models . arXiv preprint arXiv:2501.03262 . Cited by: §3.3.1 . -->

<!-- [原子块 · verbatim] [17] W. Huang, B. Jia, Z. Zhai, S. Cao, Z. Ye, F. Zhao, Z. Xu, Y. Hu, and S. Lin (2025) Vision-r1: incentivizing reasoning capability in multimodal large language models . arXiv preprint arXiv:2503.06 -->

<!-- [原子块 · verbatim] [18] A. Hurst, A. Lerer, A. P. Goucher, A. Perelman, A. Ramesh, A. Clark, A. Ostrow, A. Welihinda, A. Hayes, A. Radford, et al. (2024) Gpt-4o system card . arXiv preprint arXiv:2410.21276 . Cited by:  -->

<!-- [原子块 · verbatim] [19] N. Inoue, K. Kikuchi, E. Simo-Serra, M. Otani, and K. Yamaguchi (2023) Towards Flexible Multi-modal Document Models . In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Reco -->

<!-- [原子块 · verbatim] [20] N. Inoue, K. Masui, W. Shimoda, and K. Yamaguchi (2024) OpenCOLE: Towards Reproducible Automatic Graphic Design Generation . In Proceedings of the IEEE/CVF Conference on Computer Vision and Patte -->

<!-- [原子块 · verbatim] [21] A. Jaech, A. Kalai, A. Lerer, A. Richardson, A. El-Kishky, A. Low, A. Helyar, A. Madry, A. Beutel, A. Carney, et al. (2024) Openai o1 system card . arXiv preprint arXiv:2412.16720 . Cited by: §1  -->

<!-- [原子块 · verbatim] [22] P. Jia, C. Li, Y. Yuan, Z. Liu, Y. Shen, B. Chen, X. Chen, Y. Zheng, D. Chen, J. Li, et al. (2023) Cole: a hierarchical generation framework for multi-layered and editable graphic design . arXiv  -->

<!-- [原子块 · verbatim] [23] B. F. Labs, S. Batifol, A. Blattmann, F. Boesel, S. Consul, C. Diagne, T. Dockhorn, J. English, Z. English, P. Esser, et al. (2025) FLUX. 1 kontext: flow matching for in-context image generation  -->

<!-- [原子块 · verbatim] [24] J. Li, D. Li, S. Savarese, and S. Hoi (2023) BLIP-2: bootstrapping language-image pre-training with frozen image encoders and large language models . In ICML , Cited by: §2.1 . -->

<!-- [原子块 · verbatim] [25] X. Li, W. Jiao, J. Jin, G. Dong, J. Jin, Y. Wang, H. Wang, Y. Zhu, J. Wen, Y. Lu, et al. (2025) Deepagent: a general reasoning agent with scalable toolsets . arXiv preprint arXiv:2510.21618 . Cit -->

<!-- [原子块 · verbatim] [26] J. Lin, J. Guo, S. Sun, Z. J. Yang, J. Lou, and D. Zhang (2023) LayoutPrompter: awaken the design ability of large language models . In Thirty-seventh Conference on Neural Information Processing  -->

<!-- [原子块 · verbatim] [27] J. Lin, S. Sun, D. Huang, T. Liu, J. Li, and J. Bian (2025) From elements to design: a layered approach for automatic graphic design composition . In Proceedings of the Computer Vision and Patter -->

<!-- [原子块 · verbatim] [28] J. Lin, M. Zhou, Y. Ma, Y. Gao, C. Fei, Y. Chen, Z. Yu, and T. Ge (2023) Autoposter: a highly automatic and content-aware design system for advertising poster generation . In Proceedings of the 3 -->

<!-- [原子块 · verbatim] [29] H. Liu, C. Li, Y. Li, and Y. J. Lee (2024) Improved baselines with visual instruction tuning . In 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) , Vol. , pp. 26286–262 -->

<!-- [原子块 · verbatim] [30] H. Liu, C. Li, Y. Li, B. Li, Y. Zhang, S. Shen, and Y. J. Lee (2024) LLaVA-next: improved reasoning, ocr, and world knowledge . External Links: Link Cited by: §2.1 . -->

<!-- [原子块 · verbatim] [31] H. Liu, C. Li, Q. Wu, and Y. J. Lee (2023) Visual instruction tuning . In Advances in Neural Information Processing Systems , A. Oh, T. Naumann, A. Globerson, K. Saenko, M. Hardt, and S. Levine ( -->

<!-- [原子块 · verbatim] [32] OpenAI (2025) Thinking with images . Note: https://openai.com/index/thinking-with-images/ Cited by: §1 , §1 . -->

<!-- [原子块 · verbatim] [33] L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. Wainwright, P. Mishkin, C. Zhang, S. Agarwal, K. Slama, A. Ray, et al. (2022) Training language models to follow instructions with human feedback . Adva -->

<!-- [原子块 · verbatim] [34] L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. Wainwright, P. Mishkin, C. Zhang, S. Agarwal, K. Slama, A. Ray, J. Schulman, J. Hilton, F. Kelton, L. Miller, M. Simens, A. Askell, P. Welinder, P. F. C -->

<!-- [原子块 · verbatim] [35] Y. Qu, S. Fang, Y. Wang, X. Wang, Z. Chen, H. Xie, and Y. Zhang (2025) IGD: instructional graphic design with multimodal layer generation . arXiv preprint arXiv:2507.09910 . Cited by: §1 , §2.2 , -->

<!-- [原子块 · verbatim] [36] A. Radford, J. W. Kim, C. Hallacy, A. Ramesh, G. Goh, S. Agarwal, G. Sastry, A. Askell, P. Mishkin, J. Clark, et al. (2021) Learning transferable visual models from natural language supervision . -->

<!-- [原子块 · verbatim] [37] R. Rafailov, A. Sharma, E. Mitchell, C. D. Manning, S. Ermon, and C. Finn (2023) Direct preference optimization: your language model is secretly a reward model . Advances in neural information pr -->

<!-- [原子块 · verbatim] [38] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov (2017) Proximal policy optimization algorithms . arXiv preprint arXiv:1707.06347 . Cited by: §1 , §2.3 . -->

<!-- [原子块 · verbatim] [39] J. Seol, S. Kim, and J. Yoo (2024) Posterllama: bridging design ability of langauge model to contents-aware layout generation . arXiv preprint arXiv:2404.00995 . Cited by: §2.2 . -->

<!-- [原子块 · verbatim] [40] Z. Shao, P. Wang, Q. Zhu, R. Xu, J. Song, X. Bi, H. Zhang, M. Zhang, Y. Li, Y. Wu, et al. (2024) Deepseekmath: pushing the limits of mathematical reasoning in open language models . arXiv preprin -->

<!-- [原子块 · verbatim] [41] J. Singh, R. Magazine, Y. Pandya, and A. Nambi (2025) Agentic reasoning and tool integration for llms via reinforcement learning . arXiv preprint arXiv:2505.01441 . Cited by: §1 . -->

<!-- [原子块 · verbatim] [42] B. S. Team (2025) Seed1.5-vl technical report . arXiv preprint arXiv:2505.07062 . Cited by: §1 . -->

<!-- [原子块 · verbatim] [43] G. Team, R. Anil, S. Borgeaud, J. Alayrac, J. Yu, R. Soricut, J. Schalkwyk, A. M. Dai, A. Hauth, K. Millican, et al. (2023) Gemini: a family of highly capable multimodal models . arXiv preprint a -->

<!-- [原子块 · verbatim] [44] F. Wang, Z. Zhao, Y. Liu, D. Zhang, J. Gao, H. Sun, and X. Li (2025) SVGen: interpretable vector graphics generation with large language models . In Proceedings of the 33rd ACM International Conf -->

<!-- [原子块 · verbatim] [45] P. Wang, S. Bai, S. Tan, S. Wang, Z. Fan, J. Bai, K. Chen, X. Liu, J. Wang, W. Ge, Y. Fan, K. Dang, M. Du, X. Ren, R. Men, D. Liu, C. Zhou, J. Zhou, and J. Lin (2024) Qwen2-vl: enhancing vision-l -->

<!-- [原子块 · verbatim] [46] W. Wang, Z. Gao, L. Gu, H. Pu, L. Cui, X. Wei, Z. Liu, L. Jing, S. Ye, J. Shao, et al. (2025) InternVL3.5: advancing open-source multimodal models in versatility, reasoning, and efficiency . arXi -->

<!-- [原子块 · verbatim] [47] J. Wei, X. Wang, D. Schuurmans, M. Bosma, F. Xia, E. Chi, Q. V. Le, D. Zhou, et al. (2022) Chain-of-thought prompting elicits reasoning in large language models . Advances in neural information p -->

<!-- [原子块 · verbatim] [48] C. Wu, J. Li, J. Zhou, J. Lin, K. Gao, K. Yan, S. Yin, S. Bai, X. Xu, Y. Chen, Y. Chen, Z. Tang, Z. Zhang, Z. Wang, A. Yang, B. Yu, C. Cheng, D. Liu, D. Li, H. Zhang, H. Meng, H. Wei, J. Ni, K. C -->

<!-- [原子块 · verbatim] [49] J. Xu, X. Liu, Y. Wu, Y. Tong, Q. Li, M. Ding, J. Tang, and Y. Dong (2023) ImageReward: learning and evaluating human preferences for text-to-image generation . In Proceedings of the 37th Interna -->

<!-- [原子块 · verbatim] [50] K. Yamaguchi (2021) CanvasVAE: learning to generate vector graphic documents . ICCV . Cited by: §4.1 . -->

<!-- [原子块 · verbatim] [51] A. Yang, A. Li, B. Yang, B. Zhang, B. Hui, B. Zheng, B. Yu, C. Gao, C. Huang, C. Lv, et al. (2025) Qwen3 technical report . arXiv preprint arXiv:2505.09388 . Cited by: §1 . -->

<!-- [原子块 · verbatim] [52] T. Yang, Y. Luo, Z. Qi, Y. Wu, Y. Shan, and C. W. Chen (2024) PosterLLaVa: constructing a unified multi-modal layout generator with llm . External Links: 2406.02884 , Link Cited by: §1 , §2.2 . -->

<!-- [原子块 · verbatim] [53] Z. Yang, J. Wang, L. Li, K. Lin, C. Lin, Z. Liu, and L. Wang (2024) Idea2img: iterative self-refinement with gpt-4v for automatic image design and generation . In European Conference on Computer  -->

<!-- [原子块 · verbatim] [54] X. Zhai, B. Mustafa, A. Kolesnikov, and L. Beyer (2023) Sigmoid loss for language image pre-training . In Proceedings of the IEEE/CVF international conference on computer vision , pp. 11975–11986 -->

<!-- [原子块 · verbatim] [55] J. Zhang, R. Yoshihashi, S. Kitada, A. Osanai, and Y. Nakashima (2024) Vascar: content-aware layout generation via visual-aware self-correction . arXiv preprint arXiv:2412.04237 . Cited by: §2.2  -->

<!-- [原子块 · verbatim] [56] J. Zhang, J. Huang, H. Yao, S. Liu, X. Zhang, S. Lu, and D. Tao (2025) R1-vl: learning to reason with multimodal large language models via step-wise group relative policy optimization . arXiv pre -->

<!-- [原子块 · verbatim] [57] P. Zhang, J. Zhang, J. Cao, H. Li, and L. Jin (2025) Smaller But Better: Unifying Layout Generation with Smaller Large Language Models . International Journal of Computer Vision (IJCV) 133 , pp.  -->

<!-- [原子块 · verbatim] [58] Q. Zhang, F. Lyu, Z. Sun, L. Wang, W. Zhang, W. Hua, H. Wu, Z. Guo, Y. Wang, N. Muennighoff, et al. (2025) A survey on test-time scaling in large language models: what, how, where, and how well?  -->

<!-- [原子块 · verbatim] [59] Z. Zheng, M. Yang, J. Hong, C. Zhao, G. Xu, L. Yang, C. Shen, and X. Yu (2025) DeepEyes: incentivizing ”thinking with images” via reinforcement learning . arXiv preprint . External Links: 2507.xx -->

<!-- [原子块 · verbatim] [60] M. Zhou, C. Xu, Y. Ma, T. Ge, Y. Jiang, and W. Xu (2022) Composition-aware graphic layout gan for visual-textual presentation designs . arXiv preprint arXiv:2205.00303 . Cited by: §2.2 , §4.1 . -->

<!-- [原子块 · verbatim] [61] J. Zhu, W. Wang, Z. Chen, Z. Liu, S. Ye, L. Gu, H. Tian, Y. Duan, W. Su, J. Shao, et al. (2025) Internvl3: exploring advanced training and test-time recipes for open-source multimodal models . ar -->

**EN** Supplementary Material

**ZH** 补充材料

**EN** 1 Dataset Details

**ZH** 1 数据集细节

**EN** We collected approximately 200K samples, including free and paid data from the internet. Each sample contains a background image, target text, well-formatted SVG code, and the corresponding rendered image. Each sample has an average of 9.8 text boxes, with an average text length of 84.7. Fig. 5 is a data example. Based on these data, our training and testing data were constructed, including the dataset for the Cold-Start SFT phase, the queries for the reinforcement learning phase, the training and testing datasets for the reward model, and finally, the dataset used for evaluation.

**ZH** 我们收集了约 200K 个样本，包含来自互联网的自由与付费数据。每个样本包含一张背景图像、目标文本、格式良好的 SVG 代码，以及相应的渲染图像。每个样本平均有 9.8 个文本框，平均文本长度为 84.7。图 5 给出一个数据示例。在这些数据基础上，我们构造了训练与测试数据，包括冷启动 SFT 阶段的数据集、强化学习阶段的查询、奖励模型的训练与测试数据集，以及最终用于评测的数据集。

<!-- [原子块 · img]  -->

**EN** Figure 5: Data example, consisting of a background image, target text, SVG layout code, and the corresponding rendered image.

**ZH** 图 5：数据示例，由背景图像、目标文本、SVG 版式代码与相应的渲染图像构成。

**EN** 1.1 Cold-Start Dataset Details

**ZH** 1.1 冷启动数据集细节

**EN** We use the method described in the main text and set the maximum number of modifications to 3 during the data generation process. Since each data trajectory includes an initial generation and a final ”satisfied” output, the total number of turns is the number of modifications plus two. This process yielded a total of 8K trajectories, comprising 2,359 two-turn samples (0 modifications), 1,266 three-turn samples (1 modification), 2,030 four-turn samples (2 modifications), and 2,537 five-turn samples (3 modifications). Total data volume is 8K.

**ZH** 我们采用正文所述方法，并在数据生成过程中把最大修改次数设为 3。由于每条数据轨迹都包含一次初始生成与一次最终的「满意」输出，总轮数等于修改次数加二。该过程共产生 8K 条轨迹，包括 2,359 个两轮样本（0 次修改）、1,266 个三轮样本（1 次修改）、2,030 个四轮样本（2 次修改）与 2,537 个五轮样本（3 次修改）。数据总量为 8K。

**EN** During cold-start data construction, the prompts used to guide Doubao-Seed-1.6 are prompt 5 and prompt 5, where prompt 5 is utilized for Initial Reasoning synthesis and prompt 5 for Multi-round reflection synthesis.

**ZH** 冷启动数据构造中，用于引导 Doubao-Seed-1.6 的提示是 prompt 5 与 prompt 5，其中 prompt 5 用于初始推理合成，prompt 5 用于多轮反思合成。

**EN** 1.2 Layout Reward Model Dataset

**ZH** 1.2 版式奖励模型数据集

**EN** Herein, a qualitative comparison of data across the four quality levels (Level-I, Level-II, Level-III, Level-IV) is presented. These four levels exhibit distinct differences in typesetting quality: Level-I demonstrates the best typesetting quality, while Level-IV, by contrast, shows the worst.

**ZH** 此处给出四个质量层级（Level-I、Level-II、Level-III、Level-IV）数据的定性比较。这四个层级在排版质量上呈现明显差异：Level-I 的排版质量最好，而 Level-IV 最差。

<!-- [原子块 · img]  -->

**EN** Figure 6: Qualitative comparison of four levels of data in the training data of the reward model

**ZH** 图 6：奖励模型训练数据中四个层级数据的定性比较

**EN** 2 Training Details

**ZH** 2 训练细节

**EN** 2.1 VFLM

**ZH** 2.1 VFLM

**EN** All experiments are conducted on a cluster of 16 NVIDIA H200 GPUs. For the Cold-Start SFT stage, we trained the model with 8k data for 2 epochs with a learning rate of ⟦SLOT_32⟧ and a batch size of 64. During this stage, the image max_pixels was set to ⟦SLOT_33⟧.

**ZH** 所有实验在 16 块 NVIDIA H200 GPU 的集群上进行。冷启动 SFT 阶段，我们用 8k 数据训练模型 2 个 epoch，学习率为 ⟦SLOT_32⟧，批大小为 64。该阶段图像的 max_pixels 设为 ⟦SLOT_33⟧。

**EN** For the RL stage, we set the maximum number of tool calls to 4. The weights for ⟦SLOT_34⟧ and ⟦SLOT_35⟧ (denoted as ⟦SLOT_36⟧) were set to 0.25, while the weight for ⟦SLOT_37⟧ was set to 0.1. We prepare up to 32K samples for training, with early stopping based on reward metrics during RL training. We employed a strict on-policy training strategy with the following configuration: batch size of 64, 8 rollouts per sample, sampling temperature of 1.0, KL divergence coefficient of 1e-3, and learning rate of 1e-6.

**ZH** RL 阶段，我们把最大工具调用次数设为 4。⟦SLOT_34⟧ 与 ⟦SLOT_35⟧（记作 ⟦SLOT_36⟧）的权重设为 0.25，⟦SLOT_37⟧ 的权重设为 0.1。我们准备了最多 32K 个样本用于训练，并在 RL 训练中依据奖励指标早停。我们采用严格的同策略训练策略，配置如下：批大小 64、每样本 8 次 rollout、采样温度 1.0、KL 散度系数 1e-3、学习率 1e-6。

**EN** 2.2 Layout Reward Model

**ZH** 2.2 版式奖励模型

**EN** We trained the reward model on a preference dataset constructed from 200K layout samples. Four quality levels (Level-I, Level-II, Level-III, Level-IV) were generated for each query, yielding 1.2M preference pairs. We randomly select 25K pairs as the test set, using the remainder for training. During training, we use a batch size of 512 and train for 2100 steps.

**ZH** 我们在由 200K 个版式样本构造的偏好数据集上训练奖励模型。每个查询生成四个质量层级（Level-I、Level-II、Level-III、Level-IV），产出 1.2M 个偏好对。我们随机选取 25K 对作为测试集，其余用于训练。训练中批大小为 512，训练 2100 步。

**EN** 2.3 Ablation Study

**ZH** 2.3 消融研究

**EN** In the ablation experiments, Single-Round RL, RL from Pretrained, and Direct Output adopt the same hyperparameter configuration as VFLM. For Direct Output SFT, 40k samples are used for SFT, with a batch size of 128, a learning rate of 1e-5, and training conducted for 2 epochs.

**ZH** 消融实验中，单轮 RL、从预训练模型做 RL 与直接输出采用与 VFLM 相同的超参数配置。对直接输出 SFT，用 40k 样本做 SFT，批大小 128，学习率 1e-5，训练 2 个 epoch。

**EN** 3 Evaluation Details

**ZH** 3 评测细节

**EN** 3.1 Evaluation metrics

**ZH** 3.1 评测指标

**EN** We use an OCR engine11 1 https://github.com/PaddlePaddle/PaddleOCR to recognize text in design images and evaluate the accuracy of rendered text using character-level f-measure. In the RL reward function, ⟦SLOT_38⟧ and ⟦SLOT_39⟧ are evaluated using accuracy. Specifically, a character in the OCR recognition result is defined as a True Positive (TP) if it appears in the annotation; otherwise, it is classified as a False Positive (FP). A False Negative (FN) indicates that a character is only present in the annotation but absent from the OCR recognition result. Accordingly, character-level precision, recall, f-measure and accuracy can be formulated as follows:

**ZH** 我们使用一个 OCR 引擎11 1 https://github.com/PaddlePaddle/PaddleOCR 识别设计图像中的文本，并用字符级 F 值评估渲染文本的准确率。在 RL 奖励函数中，⟦SLOT_38⟧ 与 ⟦SLOT_39⟧ 用准确率评估。具体地，若 OCR 识别结果中的某个字符出现在标注中，则定义为真正例（TP），否则为假正例（FP）。假负例（FN）指某个字符只出现在标注中而未出现在 OCR 识别结果里。据此，字符级精确率、召回率、F 值与准确率可表述如下：

<!-- [原子块 · table] C ​ h ​ a ​ r ​ _ ​ P = T ​ P T ​ P + F ​ P , \displaystyle Char\_P=\frac{TP}{TP+FP}, (11) C ​ h ​ a ​ r ​ _ ​ R = T ​ P T ​ P + F ​ N , \displaystyle Char\_R=\frac{TP}{TP+FN}, C ​ h ​ a ​ r ​ _ ​ F = -->

**EN** For the GPT4o evaluation, we assess the effect along four dimensions: Text Accuracy, Text-Background Harmony, Text Presentation Quality, and Meaning Expression Adaptability. The evaluation prompt is shown in prompt 5. Fig. 7 is a detailed evaluation sample.

**ZH** 对 GPT4o 评测，我们从四个维度评估效果：文本准确率、文本—背景协调性、文本呈现质量与语义表达适配性。评测提示见 prompt 5。图 7 给出一个详细的评测样本。

<!-- [原子块 · img]  -->

**EN** Figure 7: A detailed GPT4o evaluation output.

**ZH** 图 7：一个详细的 GPT4o 评测输出。

**EN** 3.2 Model Prompt

**ZH** 3.2 模型提示

**EN** 3.2.1 VFLM System prompt

**ZH** 3.2.1 VFLM 系统提示

**EN** The VFLM system prompt is shown in prompt 5, includes tool definitions and task descriptions.

**ZH** VFLM 的系统提示见 prompt 5，包含工具定义与任务描述。

**EN** 3.2.2 MLLM System prompt

**ZH** 3.2.2 MLLM 系统提示

**EN** The system prompt of MLLM models, as shown in prompt 5, only omits the definition of tools and the statement of multi-round responses compared with that of VFLM.

**ZH** MLLM 模型的系统提示见 prompt 5，与 VFLM 的系统提示相比，只省略了工具定义与多轮响应的声明。

**EN** 4 More Experiments

**ZH** 4 更多实验

**EN** 4.1 Number of rounds of reflection

**ZH** 4.1 反思轮数

<!-- [原子块 · img]  -->

**EN** Figure 8: Training processes: reflection times of VFLM, constrained between 1 and 4.

**ZH** 图 8：训练过程：VFLM 的反思次数，限制在 1 到 4 之间。

**EN** Fig. 8 illustrates the dynamic evolution of reflection counts during training. While the complex process reward employs strategic termination control (Eq. (9)-Eq. (10)) to enforce stability, VFLM under the simple outcome reward exhibits a distinct, insightful trajectory. Specifically, in the initial phase (the first 100 steps), we observe a decline in reflection turns. Combining with Fig. 4, we can analyze this is attributed to the model’s initial instability in output formatting, where iterative attempts often degraded quality compared to the initial generation, prompting the model to curtail its reasoning depth. However, beyond 100 steps, as the output format stabilizes, the model discovers that iterative optimization yields superior rewards. Consequently, the reflection count begins to fluctuate and rise, reflecting the model’s autonomous realization that deeper reflection correlates with better layout quality, rather than relying on rigid, pre-defined constraints.

**ZH** 图 8 展示了训练过程中反思次数的动态演化。复杂的过程奖励采用策略性终止控制（式 (9)–式 (10)）来强制稳定性，而采用简单结果奖励的 VFLM 则呈现出一条独特而富有启发性的轨迹。具体地，在初始阶段（前 100 步）我们观察到反思轮数下降。结合图 4 可以分析出，这源于模型输出格式初期不稳定，迭代尝试往往比初始生成更差，促使模型缩减推理深度。但在 100 步之后，随着输出格式趋于稳定，模型发现迭代优化能带来更高的奖励。于是反思次数开始波动并上升，反映出模型自主地意识到更深的反思对应更好的版式质量，而不是依赖僵化的预定义约束。

<!-- [原子块 · img]  -->

**EN** Figure 9: Reflection Turns vs. Input Complexity. The positive trend (red line) demonstrates that VFLM autonomously increases reflection depth for more complex tasks.

**ZH** 图 9：反思轮数 vs. 输入复杂度。红色线条所示的正向趋势表明，VFLM 会针对更复杂的任务自主增加反思深度。

**EN** To further analyze the number of reflection rounds VFLM performs, we examined the correlation between input complexity (measured by the token length of the Target Text) and the number of reasoning rounds. As shown in Figure Fig. 9, which presents the model outputs of 1000 samples from VFLM on the TextLayout test set, the gray scatter points depict the raw distribution of inference steps, which are inherently discrete integers. To visualize the underlying trend amidst this variance, the red solid line tracks the average reflection turns across complexity intervals. A clear positive trend is observable: for concise inputs (⟦SLOT_40⟧ tokens), the model efficiently converges with fewer refinement steps (averaging ⟦SLOT_41⟧2.5 turns). In contrast, as input complexity increases to over 400 tokens, the model adaptively increases its reasoning depth, approaching the maximum of 4 turns. This confirms that VFLM actively perceives layout difficulty and allocates computational resources accordingly.

**ZH** 为进一步分析 VFLM 执行的反思轮数，我们考察了输入复杂度（以目标文本的词元长度度量）与推理轮数之间的相关性。如图 9 所示（该图展示 VFLM 在 TextLayout 测试集上 1,000 个样本的模型输出），灰色散点描绘了推理步数的原始分布，其取值本质上是离散整数。为在方差中呈现潜在趋势，红色实线跟踪各复杂度区间上的平均反思轮数。可以观察到清晰的正向趋势：对简洁输入（⟦SLOT_40⟧ 词元），模型以更少的优化步数高效收敛（平均 ⟦SLOT_41⟧2.5 轮）。相反，当输入复杂度增加到 400 词元以上时，模型自适应地加深推理深度，接近 4 轮的上限。这证实了 VFLM 会主动感知版式难度并相应地分配计算资源。

**EN** 4.2 Human Study

**ZH** 4.2 人工研究

**EN** To further enhance evaluation reliability, we supplement our analysis with a blind human study involving 16 participants, who evaluated outputs from Claude3.7, GPT4o-Image, OpenCOLE, and VFLM on three dimensions across 320 randomly selected queries from three datasets. A total of 960 votes were collected. As shown in the Figure 10, VFLM performed comparably to GPT4o-Image on text coordination and achieved the best results in text accuracy and overall aesthetics.

**ZH** 为进一步提升评测可靠性，我们补充了一项盲评人工研究：16 名参与者在三个维度上评测 Claude3.7、GPT4o-Image、OpenCOLE 与 VFLM 的输出，题目为从三个数据集中随机选取的 320 条查询，共收集 960 票。如图 10 所示，VFLM 在文本协调性上与 GPT4o-Image 相当，并在文本准确率与整体美学上取得最佳结果。

<!-- [原子块 · img]  -->

**EN** Figure 10: Results of human study.

**ZH** 图 10：人工研究结果。

**EN** 4.3 Compute Cost and Latency

**ZH** 4.3 计算成本与延迟

**EN** As shown in Figure 11, we report the average inference time of VFLM, OpenCOLE, and IGD on the TextLayout test set using 4×4090 GPUs. Although VFLM has the highest latency, it yields substantial performance gains.

**ZH** 如图 11 所示，我们报告了 VFLM、OpenCOLE 与 IGD 在 TextLayout 测试集上使用 4×4090 GPU 的平均推理时间。尽管 VFLM 延迟最高，它带来了显著的性能增益。

<!-- [原子块 · object]  -->

**EN** Figure 11: Comparison of inference time and latency with OpenCOLE and IGD.

**ZH** 图 11：与 OpenCOLE、IGD 的推理时间与延迟比较。

**EN** 4.4 More Baseline

**ZH** 4.4 更多基线

**EN** Table 5: Metrics and RM score on OpenCOLE* and MLLM feedback baseline.

**ZH** 表 5：OpenCOLE* 与 MLLM 反馈基线上的指标与 RM 分数。

<!-- [原子块 · table] Model Char-F ↑ \uparrow R a ​ l ​ i ↓ R_{ali}\downarrow R o ​ v ​ e ↓ R_{ove}\downarrow R c ​ o ​ m ↓ R_{com}\downarrow RM Score ↑ \uparrow OpenCOLE* 0.7671 0.7114 0.0143 21.8279 0.3620 VFLM 0.9071 0. -->

**EN** The table above shows the results of OpenCOLE trained on the same training set as VFLM. Although retraining brings substantial improvements over the original OpenCOLE, it still underperforms VFLM. We further integrate visual feedback into GPT-4o and Qwen2.5-VL-7B baselines. As shown in the table, without task-specific training, introducing visual feedback to MLLMs yields only marginal gains, with some metrics even showing slight declines.

**ZH** 上表给出在与 VFLM 相同训练集上训练的 OpenCOLE 的结果。尽管重新训练相比原始 OpenCOLE 带来大幅提升，它仍不及 VFLM。我们进一步把视觉反馈集成到 GPT-4o 与 Qwen2.5-VL-7B 基线中。如表所示，在没有任务专用训练的情况下，给 MLLM 引入视觉反馈只带来微小增益，某些指标甚至略有下降。

**EN** 4.5 Ablation on Other Datasets

**ZH** 4.5 其他数据集上的消融

**EN** Table 6: Ablation experiments on Graphic quality metrics and OCR metrics on Crello test set.

**ZH** 表 6：Crello 测试集上图形质量指标与 OCR 指标的消融实验。

<!-- [原子块 · table] Model OCR Graphic RM Score ↑ \uparrow Char-F ↑ \uparrow R a ​ l ​ i ↓ R_{ali}\downarrow R o ​ v ​ e ↓ R_{ove}\downarrow R c ​ o ​ m ↓ R_{com}\downarrow VFLM-step1 0.8774 0.0046 0.0061 19.5917 0.4392 V -->

**EN** Table 7: Ablation experiments on Graphic quality metrics and OCR metrics on DESIGNERINTENTION test set.

**ZH** 表 7：DESIGNERINTENTION 测试集上图形质量指标与 OCR 指标的消融实验。

<!-- [原子块 · table] Model OCR Graphic RM Score ↑ \uparrow Char-F ↑ \uparrow R a ​ l ​ i ↓ R_{ali}\downarrow R o ​ v ​ e ↓ R_{ove}\downarrow R c ​ o ​ m ↓ R_{com}\downarrow VFLM-step1 0.9415 0.0033 0.0023 14.1230 0.5285 V -->

**EN** Tab. 6 and Tab. 7 demonstrate the metrics of all models in the ablation experiments on the Crello and DESIGNERINTENTION test sets. Consistent with the conclusions in the TextLayout dataset, VFLM also achieves significant advantages over other baselines on these two datasets, fully demonstrating the generalization ability of our visual feedback method.

**ZH** 表 6 与表 7 给出各模型在 Crello 与 DESIGNERINTENTION 测试集上消融实验的指标。与 TextLayout 数据集上的结论一致，VFLM 在这两个数据集上也相对其他基线取得显著优势，充分证明了我们视觉反馈方法的泛化能力。

**EN** 4.6 Ablation on Reward Functions

**ZH** 4.6 奖励函数消融

**EN** In our RL training process, the score for layout performance (⟦SLOT_42⟧) from the reward model and two rewards based on text accuracy:

**ZH** 在我们的 RL 训练过程中，来自奖励模型的版式表现分数（⟦SLOT_42⟧）与两个基于文本准确率的奖励：

<!-- [原子块 · table] R score = R layout + α ⋅ ( R ocr + R svg ) . R_{\text{score}}=R_{\text{layout}}+\alpha\cdot\left(R_{\text{ocr}}+R_{\text{svg}}\right). (12) -->

**EN** We perform ablation to investigate whether using only ⟦SLOT_43⟧ from the reward model is effective. To save validation time, tests are conducted on the models of the two ablation experiments: Single-Round RL and Direct Output.

**ZH** 我们做消融以考察只使用奖励模型的 ⟦SLOT_43⟧ 是否有效。为节省验证时间，测试在单轮 RL 与直接输出这两个消融实验的模型上进行。

**EN** Table 8: Ablation experiments on the reward function on the TextLayout test set.

**ZH** 表 8：TextLayout 测试集上奖励函数的消融实验。

<!-- [原子块 · table] Model OCR Graphic RM Score ↑ \uparrow Char-F ↑ \uparrow R a ​ l ​ i ↓ R_{ali}\downarrow R o ​ v ​ e ↓ R_{ove}\downarrow R c ​ o ​ m ↓ R_{com}\downarrow Single-Round RL 0.8792 0.0024 0.0053 18.9428 0.4 -->

**EN** The results are presented in Tab. 8. It can be observed from the table that the two models exhibit little difference in RL training performance with and without the ⟦SLOT_44⟧ and ⟦SLOT_45⟧ rewards, with many metrics being relatively close. Since ⟦SLOT_46⟧ and ⟦SLOT_47⟧ have low computational costs and the task essentially involves text typesetting, these two reward functions are retained in the final training of VFLM.

**ZH** 结果见表 8。从表中可见，有 ⟦SLOT_44⟧ 与 ⟦SLOT_45⟧ 奖励和没有这两个奖励时，两个模型在 RL 训练性能上差异不大，许多指标相当接近。由于 ⟦SLOT_46⟧ 与 ⟦SLOT_47⟧ 计算成本低，且该任务本质上涉及文本排版，最终训练 VFLM 时保留了这两个奖励函数。

**EN** 5 Case Study

**ZH** 5 案例研究

**EN** Fig. 12 presents a detailed case generated by VFLM. The SVG initially produced by VFLM exhibits several obvious issues in terms of rendering effect; for instance, the main title ”Merry Christmas” is too large and overlaps with the silhouette of the castle. After receiving visual feedback from the rendered image, it can be observed from the model’s reasoning content (highlighted in the figure) that the model identified these problems and implemented appropriate improvements. Following the second round of visual feedback, the model deemed the current layout satisfactory and output it to user as the final result. Fig. 13 is another case.

**ZH** 图 12 给出 VFLM 生成的一个详细案例。VFLM 最初生成的 SVG 在渲染效果上存在若干明显问题：例如主标题「Merry Christmas」过大，并与城堡的剪影重叠。在接收到渲染图像的视觉反馈后，从模型的推理内容（图中高亮部分）可以看出，模型识别出了这些问题并实施了恰当的改进。在第二轮视觉反馈之后，模型认为当前版式已令人满意，便将其作为最终结果输出给用户。图 13 是另一个案例。

**EN** Fig. 14 show the more output cases of VFLM. Fig. 15 and Fig. 16 demonstrate the comparison between VFLM and all other models.

**ZH** 图 14 展示了 VFLM 的更多输出案例。图 15 与图 16 展示了 VFLM 与所有其他模型的比较。

<!-- [原子块 · img]  -->

**EN** Figure 12: A detailed VFLM output case.

**ZH** 图 12：一个详细的 VFLM 输出案例。

<!-- [原子块 · img]  -->

**EN** Figure 13: Another detailed VFLM output case.

**ZH** 图 13：另一个详细的 VFLM 输出案例。

<!-- [原子块 · img]  -->

**EN** Figure 14: More VFLM output cases.

**ZH** 图 14：更多 VFLM 输出案例。

<!-- [原子块 · img]  -->

**EN** Figure 15: In comparison with all existing methods(Part1).

**ZH** 图 15：与所有现有方法的比较（第一部分）。

<!-- [原子块 · img]  -->

**EN** Figure 16: In comparison with all existing methods(Part2).

**ZH** 图 16：与所有现有方法的比较（第二部分）。

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->

<!-- [原子块 · svg]  -->
