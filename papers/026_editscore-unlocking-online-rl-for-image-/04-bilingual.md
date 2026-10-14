# EditScore：借助高保真奖励建模解锁图像编辑的在线强化学习

> 原标题：EditScore: Unlocking Online RL for Image Editing via High-Fidelity Reward Modeling
> 作者：Xin Luo, Jiahao Wang, Chenyuan Wu, Shitao Xiao, Xiyan Jiang, Defu Lian, Jiajun Zhang, Dong Liu, Zheng liu · arXiv:2509.23909 · 2025-09-28

<!-- [原子块 · verbatim] EditScore: Unlocking Online RL for Image Editing via High-Fidelity Reward Modeling -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] Instruction-guided image editing has achieved remarkable progress, yet current models still face challenges with complex instructions and often require multiple samples to produce a desired result. Re -->

<!-- [原子块 · table]  -->

**EN** 1 Introduction

**ZH** 1 引言

**EN** Recently, Reinforcement Learning (Li, 2017) has demonstrated immense power in advancing large language models and has also shown remarkable success in the text-to-image (T2I) domain. Works like FlowGRPO (Liu et al., 2025a) and DanceGRPO (Xue et al., 2025) have leveraged RL on flow-matching models to significantly enhance T2I generation across multiple dimensions. Despite these successes, the application of RL to the image editing domain remains largely underexplored. We posit that RL holds significant, untapped potential for image editing. By framing editing as a dynamic trial-and-error process, a policy model can discover novel and more effective editing strategies beyond what is captured in static datasets. Through a well-designed reward mechanism, the model can be progressively steered to better align with user intent and achieve a deeper, more robust editing capability across diverse scenarios.

**ZH** 近来，强化学习（Reinforcement Learning, RL）（Li, 2017）在推进大语言模型方面展现出巨大威力，在文生图（text-to-image, T2I）领域同样取得了引人注目的成功。FlowGRPO（Liu et al., 2025a）与 DanceGRPO（Xue et al., 2025）等工作把强化学习引入流匹配（flow-matching）模型，在多个维度上大幅提升了 T2I 生成效果。尽管进展斐然，强化学习在图像编辑领域的应用仍鲜有探索。我们的判断是，强化学习在图像编辑上蕴含着尚未释放的巨大潜力：把编辑建模为一个动态的试错过程，策略模型便有可能发现静态数据集未曾覆盖的、更新也更有效的编辑策略；借助精心设计的奖励机制，模型还能被逐步引导至更贴合用户意图的方向，从而在多样场景中获得更深入、更稳健的编辑能力。

**EN** Despite its theoretical promise, applying online RL to high-resolution image editing remains a formidable and largely unsolved challenge (Wei et al., 2025; Wu et al., 2025a; Ahmadi et al., 2025). The primary obstacle lies in the absence of a suitable reward function: a reliable, efficient, and scalable oracle that can accurately score the quality of an edit given an instruction. A natural consideration would be to employ state-of-the-art, general-purpose Visual Language Models (VLMs) like GPT-5 (OpenAI, 2025) or other proprietary APIs as reward providers. However, this approach is impractical for online RL, with these large VLMs are expensive to query at scale. The second alternative, using powerful open-source VLMs, resolves cost issues. However, our investigations reveal a critical performance gap. As we will demonstrate, even Qwen2.5-VL-72B (Bai et al., 2025b) fails to provide a sufficiently accurate and consistent reward signal to effectively guide the policy. Directly using such models as reward functions often causes unstable training or policy collapse, showing that scale alone cannot replace specialized accuracy. Progress thus hinges on an accurate reward model tailored to image editing, yet the community still lacks a powerful open-source option—posing a major barrier to advancing RL-based editing.

**ZH** 尽管理论前景可观，把在线强化学习应用于高分辨率图像编辑仍是一项艰巨且基本未被攻克的挑战（Wei et al., 2025; Wu et al., 2025a; Ahmadi et al., 2025）。主要障碍在于缺少合适的奖励函数——一个可靠、高效且可扩展，能根据给定指令准确为编辑质量打分的判别器。最自然的想法是采用 GPT-5（OpenAI, 2025）等最先进的通用视觉语言模型（VLM）或其他专有 API 充当奖励提供方；然而这类大模型的规模化调用成本高昂，对在线强化学习并不现实。第二种方案是改用强大的开源 VLM，成本问题由此消解，但我们的调研揭示出一道关键的性能鸿沟：正如后文所示，即便 Qwen2.5-VL-72B（Bai et al., 2025b）也无法提供足够准确且一致的奖励信号来有效引导策略，直接把这类模型当作奖励函数往往导致训练不稳甚至策略崩溃，说明模型规模本身无法替代专门化的准确性。因此，该领域的进展取决于一个面向图像编辑的精准奖励模型，而社区目前仍缺少强大的开源选项——这构成了推进基于强化学习的编辑研究的主要壁垒。

**EN** In this work, we argue that the key to unlocking online RL for image editing is the development of a specialized, high-fidelity, and efficient reward model. We present a systematic approach to build, validate, and deploy such a model. Our contributions are organized as follows:

**ZH** 本文主张，解锁图像编辑在线强化学习的关键，在于构建一个专门化、高保真且高效的奖励模型。我们给出一套系统方法来构建、验证并部署这样的模型，贡献组织如下。

**EN** First, to enable rigorous and reproducible research, we introduce EditReward-Bench, a comprehensive benchmark for evaluating reward models in image editing. It is organized into four main categories, comprising 13 diverse subtasks ranging from simple attribute edits to complex compositional changes. Each entry is evaluated by expert human raters across three key dimensions: prompt following, consistency, and overall quality. All annotations have passed rigorous inter-annotator agreement checks, establishing a reliable standard for measuring reward model quality.

**ZH** 其一，为支撑严谨且可复现的研究，我们提出 EditReward-Bench——一个面向图像编辑奖励模型评测的综合基准。它按四大类组织，涵盖 13 个多样化子任务，从简单的属性编辑到复杂的组合式改动不等。每条数据均由人类专家从指令遵循、一致性与总体质量三个关键维度评判，全部标注通过了严格的标注员间一致性检验，为衡量奖励模型质量确立了可靠标准。

**EN** Second, guided by our benchmark, we develop EditScore, a series of powerful reward models (7B–72B) for evaluating the quality of instruction-guided editing. Through careful data curation and filtering and inference-time scaling, EditScore sets a new state of the art for open-source reward models in this domain, even surpassing the accuracy of leading proprietary VLMs.

**ZH** 其二，在该基准的指导下，我们开发了 EditScore——一系列用于评估指令引导编辑质量的强大奖励模型（7B–72B）。通过细致的数据策管、筛选与推理时扩展，EditScore 在该领域创下开源奖励模型的新水平，准确率甚至超越了头部专有 VLM。

**EN** To validate its practical utility, we first apply EditScore in a Best-of-⟦SLOT_0⟧ selection experiment across several state-of-the-art editing models, which confirms that our reward model can effectively improve the performance of diverse editors. We further used EditScore for RL training, resulting in a model that shows a substantial and consistent performance uplift over its base model.

**ZH** 为验证其实用价值，我们首先在若干最先进编辑模型上开展 Best-of-⟦SLOT_0⟧ 选择实验，证实该奖励模型能够有效提升不同编辑器的表现；随后把 EditScore 用于强化学习训练，所得模型相较其基座模型呈现出显著且稳定的性能提升。

**EN** In summary, our key contributions are as follows.

**ZH** 综上，本文的核心贡献如下。

**EN** • We propose EditReward-Bench, a new public benchmark for the direct and reliable evaluation of reward models for instruction-guided image editing.

**ZH** • 提出 EditReward-Bench，一个新的公开基准，可直接、可靠地评测面向指令引导图像编辑的奖励模型。

**EN** • We develop and release EditScore, a series of state-of-the-art open-source reward models for instruction-based image editing that, through our self-ensembling strategy, surpasses the accuracy of leading proprietary VLMs on this task.

**ZH** • 开发并开源 EditScore，一系列面向指令式图像编辑的最先进开源奖励模型；借助自集成策略，其准确率在该任务上超越了头部专有 VLM。

**EN** • We demonstrate the broad, practical utility of EditScore through a Best-of-⟦SLOT_1⟧ selection experiment, successfully enhancing the performance of multiple diverse base models.

**ZH** • 通过 Best-of-⟦SLOT_1⟧ 选择实验展示 EditScore 广泛的实用价值，成功提升了多个不同基座模型的性能。

**EN** • We provide a comprehensive analysis of an end-to-end online RL application, identifying key factors for success, including the accuracy and variance of the reward signal.

**ZH** • 对端到端在线强化学习应用给出全面分析，识别出包括奖励信号准确性与方差在内的关键成功因素。

**EN** 2 Related Work

**ZH** 2 相关工作

**EN** Reward Models for Image Generation. Reward models provide signals based on specific preferences and can be applied in various scenarios such as automated evaluation and reinforcement learning. Most research has focused on text-to-image tasks, with works like Wu et al. (2023b); Kirstain et al. (2023); Zhang et al. (2024b) fine-tune CLIP-based model with human preference data and Ma et al. (2025); Wang et al. (2025b); Gao et al. (2025) employ VLMs as a core component for reward generation. Research on reward models for image editing is relatively underexplored: some works focused on controlled edits based on predefined masks (Ren et al., 2024; Gong et al., 2025). For instruction-guided editing, Zhang et al. (2024a) fine-tunes the BLIP model (Li et al., 2022) with human annotated reward signals for the image generated only by P2P Hertz et al. (2022) and IP2P Brooks et al. (2023), while Chen et al. (2025) leverages CLIP scores to automatically construct training data for training LLaVA-Next-8B Liu et al. (2024) as reward model. However, they used outdated editing models to generate images that needed to be evaluated, or simply used CLIP to annotate and score the images. Meanwhile, they use limited task categories as the prompt pool. The limitations in the narrow scope of task and generation model coverage make them struggle to support online RL for current models. Furthermore, they are not open-source and cannot be used and evaluated by the public. In contrast, our model enables broader evaluation of editing tasks (13 tasks) while supporting SOTA editing models (e.g., Gemini-2.5-image-preview). Moreover, its generative nature enables it to perform inference-time scaling to enhance scoring accuracy (Liu et al., 2025d).

**ZH** 面向图像生成的奖励模型。 奖励模型依据特定偏好提供信号，可应用于自动评测、强化学习等多种场景。多数研究聚焦于文生图任务：Wu et al. (2023b)、Kirstain et al. (2023)、Zhang et al. (2024b) 等用人类偏好数据微调基于 CLIP 的模型，Ma et al. (2025)、Wang et al. (2025b)、Gao et al. (2025) 则把 VLM 作为奖励生成的核心组件。面向图像编辑的奖励模型研究相对薄弱，部分工作关注基于预定义掩码的受控编辑（Ren et al., 2024; Gong et al., 2025）。在指令引导编辑方面，Zhang et al. (2024a) 用人工标注的奖励信号微调 BLIP 模型（Li et al., 2022），但被评测的图像仅由 P2P Hertz et al. (2022) 与 IP2P Brooks et al. (2023) 生成；Chen et al. (2025) 则利用 CLIP 分数自动构建训练数据，把 LLaVA-Next-8B Liu et al. (2024) 训练成奖励模型。然而，它们要么使用过时的编辑模型生成待评测图像，要么仅靠 CLIP 完成标注与打分，同时只用有限的任务类别构成提示池。任务与生成模型覆盖面的双重局限，使其难以支撑当前模型的在线强化学习；而且它们均未开源，公众无从使用与评测。相比之下，我们的模型支持更广泛的编辑任务评测（13 类），并覆盖最先进的编辑模型（如 Gemini-2.5-image-preview）；其生成式本质还使其能够通过推理时扩展来提升打分准确率（Liu et al., 2025d）。

**EN** Image Reward Model Evaluation. Establishing a reliable benchmark is critical as it ensures the objective measurement of reward modeling performance and offers clear guidance for optimization. In previous work, image reward models are evaluated on their accuracy in predicting human preferences for key generative tasks, such as text-to-image generation (Xu et al., 2023; Kirstain et al., 2023; Wu et al., 2023b; Wu et al., 2023a; Ma et al., 2025) and image editing (Ku et al., 2023b; Jiang et al., 2024). Over the past year, generative models such as GPT-Image-1 (Hurst et al., 2024), FLUX-Kontext (Batifol et al., 2025), Qwen-Image-Edit (Wu et al., 2025a) and Nano Banana (Google, 2025) have achieved significant breakthroughs in image editing, particularly in stylization, hybrid edit and text modification. With the growing power of generative models and their expanding editing capabilities, there is an urgent need for reward models that can accurately assess them. This, in turn, necessitates the development of a novel and more comprehensive benchmark for evaluating edit rewards.

**ZH** 图像奖励模型的评测。 建立可靠的基准至关重要，它既保证对奖励建模性能的客观度量，也为优化给出明确指引。既有工作以图像奖励模型在关键生成任务上预测人类偏好的准确率来评价它们，如文生图（Xu et al., 2023; Kirstain et al., 2023; Wu et al., 2023b; Wu et al., 2023a; Ma et al., 2025）与图像编辑（Ku et al., 2023b; Jiang et al., 2024）。过去一年间，GPT-Image-1（Hurst et al., 2024）、FLUX-Kontext（Batifol et al., 2025）、Qwen-Image-Edit（Wu et al., 2025a）与 Nano Banana（Google, 2025）等生成模型在图像编辑上取得重大突破，尤其在风格化、组合编辑与文字修改等方面。随着生成模型能力日益增强、编辑功能不断拓展，亟需能够准确评估它们的奖励模型；这又反过来要求构建更新、更全面的编辑奖励评测基准。

**EN** 3 EditReward-Bench

**ZH** 3 EditReward-Bench

**EN** 3.1 Overview

**ZH** 3.1 概述

**EN** EditReward-Bench is a benchmark specifically designed for systematic evaluation of reward modeling for image editing. It covers 13 diverse editing tasks and spans 11 heterogeneous editing models for data construction, ranging from open-source baselines to state-of-the-art proprietary models (see Table 1 for comparison). The benchmark is distinguished by the following features.

**ZH** EditReward-Bench 是专为系统评测图像编辑奖励建模而设计的基准。它覆盖 13 类多样化编辑任务，在数据构建上横跨 11 个异构编辑模型，从开源基线到最先进的专有模型不等（对比见表 1）。该基准具备如下特点。

**EN** Multi-dimensional Image Evaluation Framework. EditReward-Bench offers three key dimensions for evaluating editing outcomes. These includes Prompt Following (adherence to prompts), consistency (preservation of key visual elements) and overall quality (comparison across all aspects).

**ZH** 多维度图像评测框架。 EditReward-Bench 给出评估编辑结果的三个关键维度，即指令遵循（Prompt Following，对提示的遵循程度）、一致性（关键视觉元素的保留）与总体质量（跨所有方面的综合比较）。

**EN** Comprehensive Model Performance Spectrum. EditReward-Bench incorporates both state-of-the-art editing models and lower-peforming baselines. It effectively challenges the reward model’s distinguish ability and validates the reward model’s scoring performance on current SOTA models.

**ZH** 完整的模型性能谱系。 EditReward-Bench 同时纳入最先进的编辑模型与性能偏弱的基线，既有效考验奖励模型的辨别能力，也验证其对当前 SOTA 模型的打分表现。

**EN** Extensive Task Coverage with Real-world Applicability. EditReward-Bench also covers a diverse set of editing tasks that closely align with real-world application scenarios, ensuring authentic and comprehensive evaluation of reward models for image editing.

**ZH** 广泛的任务覆盖与真实适用性。 EditReward-Bench 覆盖的编辑任务紧贴真实应用场景，确保对图像编辑奖励模型的评测真实而全面。

**EN** Table 1: Comparison of EditReward-Bench against existing benchmarks, highlighting its superior scale, data sources, and comprehensive task coverage. The order of subtasks within each tuple under “Task Coverage” corresponds to the order of subtasks listed for each category in Section 3.2.

**ZH** 表 1：EditReward-Bench 与现有基准的对比，凸显其在规模、数据来源与任务覆盖度上的优势。“任务覆盖”一栏中各元组内子任务的排列顺序，对应第 3.2 节各类别所列子任务的顺序。

<!-- [原子块 · table] Feature ImagenHub ( Ku et al., 2023b ) GenAI-Bench ( Jiang et al., 2024 ) EditReward-Bench (ours) General Properties Size 2,864 919 3,072 Multi-Dimensional Eval. ✓ ✗ ✓ Proprietary Model Data ✗ ✗ ✓ Tas -->

**EN** 3.2 Construction Protocol

**ZH** 3.2 构建流程

**EN** To create a robust and comprehensive benchmark, we focused on three key pillars: the diversity of editing tasks, the variety of editing models, and the granularity of our evaluation criteria.

**ZH** 为构建稳健而全面的基准，我们聚焦三根支柱：编辑任务的多样性、编辑模型的多样性，以及评测标准的粒度。

**EN** First, to ensure comprehensive task coverage, we structure our benchmark into four main categories, comprising 13 distinct subtasks curated from established datasets like GEdit-Bench-EN (Liu et al., 2025b) and ImgEdit-Bench (Ye et al., 2025). These categories are designed to span a wide spectrum of complexity. They are: 1) Subject, which includes fundamental tasks like subject addition, subject removal and subject replace; 2) Appearance, covering shape-preserving edits such as color alteration, material modification, style transfer and tone transformation; 3) Scene, which tests understanding of image layout through tasks like background change and extract; and 4) Advanced, the most challenging category, which requires advanced reasoning for tasks like portrait beautification, text modification, motion change and hybrid edit.

**ZH** 首先，为保证任务覆盖的全面性，我们把基准组织为四大类，包含从 GEdit-Bench-EN（Liu et al., 2025b）与 ImgEdit-Bench（Ye et al., 2025）等既有数据集中精选出的 13 个不同子任务。各类别的复杂度跨度很大，分别是：1）主体（Subject），含主体添加、主体移除与主体替换等基础任务；2）外观（Appearance），含颜色更改、材质修改、风格迁移与色调变换等保持形状不变的编辑；3）场景（Scene），通过背景替换与主体提取等任务检验对图像布局的理解；4）高级（Advanced），难度最高的一类，需对人物美化、文字修改、动作变化与组合编辑等任务作高级推理。

**EN** Second, to populate our benchmark with a diverse distribution of edited images, the candidate pool of outputs were generated by a diverse array of 11 generative models for data construction: Step1X-Edit (Liu et al., 2025b), Step1X-Edit v1.1 (Liu et al., 2025b), Qwen-Image-Edit (Wu et al., 2025a), OmniGen2 (Wu et al., 2025b), FLUX-Kontext-dev (Batifol et al., 2025), FLUX-Kontext-pro (Batifol et al., 2025), Bagel (Deng et al., 2025), MagicBrush (Zhang et al., 2023), Omnigen (Xiao et al., 2025), gpt-image-1 (Hurst et al., 2024), and Gemini-2.5-image-preview (Google, 2025), including both open-source and state-of-the-art proprietary editors.

**ZH** 其次，为使基准中的编辑图像呈现多样化分布，我们用一个由 11 个生成模型构成的模型池产出候选输出，用于数据构建：Step1X-Edit（Liu et al., 2025b）、Step1X-Edit v1.1（Liu et al., 2025b）、Qwen-Image-Edit（Wu et al., 2025a）、OmniGen2（Wu et al., 2025b）、FLUX-Kontext-dev（Batifol et al., 2025）、FLUX-Kontext-pro（Batifol et al., 2025）、Bagel（Deng et al., 2025）、MagicBrush（Zhang et al., 2023）、Omnigen（Xiao et al., 2025）、gpt-image-1（Hurst et al., 2024）与 Gemini-2.5-image-preview（Google, 2025），开源编辑器与最先进专有编辑器兼而有之。

**EN** Finally, recognizing that the quality of editing results is not monolithic, we designed a multi-dimensional evaluation scheme for better interpretability as inspired by (Ku et al., 2023a; Liu et al., 2025b). Each editing result is assessed along three distinct axes: Prompt Following (PF): measuring how faithfully the edit executes the given instruction. Consistency (C): assessing the preservation of unedited image regions. Overall Quality (O): providing a holistic comparison of edits by accounting for all relevant aspects.

**ZH** 最后，鉴于编辑结果的质量并非单一维度，我们受（Ku et al., 2023a; Liu et al., 2025b）启发，设计了一套多维度评测方案以增强可解释性。每个编辑结果沿三条不同的轴线评估：指令遵循（Prompt Following, PF），衡量编辑执行给定指令的忠实程度；一致性（Consistency, C），评估未编辑图像区域的保留情况；总体质量（Overall Quality, O），在综合考量所有相关方面的基础上对编辑结果作整体比较。

**EN** 3.3 Annotation Pipeline

**ZH** 3.3 标注流程

**EN** To ensure the reliability of EditReward-Bench, we designed a rigorous human annotation pipeline conducted exclusively by experts in generative AI, as illustrated in Figure 1.

**ZH** 为保证 EditReward-Bench 的可靠性，我们设计了一套严格的人工标注流程，全部由生成式 AI 领域的专家完成，如图 1 所示。

**EN** To ensure high-quality ground truth, we implemented a Two-Annotator Discussion Protocol. Unlike standard crowdsourcing where raters work in isolation, our protocol assigns two experts to each sample. They engage in real-time discussion to analyze visual artifacts (e.g., attribute drift) and resolve discrepancies, finalizing the ranking only upon reaching a joint consensus. We validated this protocol through a controlled study comparing it against independent labeling. The results demonstrate that the discussion-based approach significantly reduces annotation noise: for instance, in the Consistency dimension, the inter-annotator convergence rate (at a 100% agreement threshold) improved by 12.12%. Furthermore, the rankings determined by a single annotator pair achieved over 97% consistency with the majority vote derived from the full expert pool, confirming that our efficient two-annotator setup yields results highly aligned with collective expert judgment. A detailed disagreement analysis is provided in Appendix B.

**ZH** 为确保获得高质量的真值，我们实施了双标注员讨论协议。与标注者各自独立作业的标准众包不同，该协议为每个样本指派两名专家，二人实时讨论、共同分析视觉瑕疵（例如属性漂移）并消解分歧，仅在达成共同共识后才最终敲定排序。我们通过一项对照研究将该协议与独立标注作比较以验证其有效性。结果表明，基于讨论的方法显著降低了标注噪声：例如在一致性维度上，标注员间的收敛率（以 100% 一致为阈值）提升了 12.12%。此外，单个标注员对给出的排序与全体专家池多数投票结果的一致性超过 97%，说明这种高效的双标注员设置所得结果与专家集体判断高度吻合。详细的分歧分析见附录 B。

**EN** Following this protocol, for each input with five output images randomly sampled from the candidate pool, the annotators were asked to rank them. Our system uniquely allowed them to group outputs of similar quality into the same tiers; for instance, a ranking of ⟦SLOT_2⟧ places output 3 in the top tier, outputs 1 and 2 tied in the second, and 4 and 5 tied in the third.

**ZH** 依照该协议，对每个输入我们从候选池中随机采样五张输出图像，请标注员对其排序。我们的系统还独特地允许标注员把质量相近的输出归入同一档位；例如排序 ⟦SLOT_2⟧ 表示输出 3 位于第一档，输出 1 与 2 并列第二档，输出 4 与 5 并列第三档。

**EN** These tiered rankings were then decomposed into pairwise preference tuples. Following the ⟦SLOT_3⟧ example, this conversion yields preference pairs where a higher-tiered item is preferred over a lower-tiered one, such as ⟦SLOT_4⟧, ⟦SLOT_5⟧, ⟦SLOT_6⟧ and ⟦SLOT_7⟧. Comparisons between items within the same tier (e.g., ⟦SLOT_8⟧) are excluded as they represent equal quality. This process resulted in a large-scale, high-fidelity dataset of 3,072 preference pairs, comprising 944 for prompt following, 890 for consistency, and 1,238 for overall quality. For the evaluation of reward models, we utilize the preference prediction accuracy metric, calculated by the proportion of pairs ⟦SLOT_9⟧ where the model scores the human-preferred output higher, i.e., ⟦SLOT_10⟧.

**ZH** 这些分层排序随后被拆解为成对的偏好元组。以上述 ⟦SLOT_3⟧ 为例，该转换得到的偏好对中，高档位项优于低档位项，如 ⟦SLOT_4⟧、⟦SLOT_5⟧、⟦SLOT_6⟧ 与 ⟦SLOT_7⟧。同档位内部的比较（例如 ⟦SLOT_8⟧）因代表质量相当而被排除。该过程产出一个大规模、高保真的偏好对数据集，共 3,072 对，其中指令遵循 944 对、一致性 890 对、总体质量 1,238 对。评测奖励模型时，我们采用偏好预测准确率指标，即在偏好对 ⟦SLOT_9⟧ 中模型给人类更偏好的输出打出更高分的比例，即 ⟦SLOT_10⟧。

<!-- [原子块 · img]  -->

**EN** Figure 1: Illustration of the annotation process. Annotators are presented with five candidate output images and are asked to rank them according to three evaluation dimensions. The final ranking is determined through consensus among multiple annotators. For example, ⟦SLOT_11⟧ indicates that the first image is preferred over images 2, 3 and 4, which are in turn preferred over image 5.

**ZH** 图 1：标注流程示意。向标注员呈现五张候选输出图像，请其按三个评测维度排序；最终排序由多名标注员协商达成一致后确定。例如 ⟦SLOT_11⟧ 表示第一张图优于第 2、3、4 张，而后者又优于第 5 张。

**EN** 4 Method

**ZH** 4 方法

**EN** 4.1 Edit Reward

**ZH** 4.1 编辑奖励

**EN** 4.1.1 The Approach to Reward Modeling

**ZH** 4.1.1 奖励建模的思路

**EN** Inspired by (Wang et al., 2025b; Wang et al., 2025a; Wu et al., 2025c), we formulate reward modeling as a conditional textual generation task. We fine-tune models from the powerful Qwen2.5-VL series (Bai et al., 2025b) on a standard autoregressive objective to act as specialized evaluators. Our model EditScore takes (Instruction, Input Image, Output Image) as input, (Reasoning, Scalar Score) as output. The chain-of-thought (Wei et al., 2022) process of output not only enhances the model’s interpretability but also demonstrably improves the accuracy of the final scores.

**ZH** 受（Wang et al., 2025b; Wang et al., 2025a; Wu et al., 2025c）启发，我们把奖励建模形式化为一个条件文本生成任务：在标准的自回归目标上微调 Qwen2.5-VL 系列（Bai et al., 2025b）中性能强大的模型，使其成为专门的评判器。我们的模型 EditScore 以（指令、输入图像、输出图像）为输入，以（推理过程、标量分数）为输出。输出中的思维链（chain-of-thought）（Wei et al., 2022）过程既增强了模型的可解释性，也切实提高了最终分数的准确性。

**EN** To ensure EditScore can perform a comprehensive evaluation of editing tasks, we adopt the VIEScore framework (Ku et al., 2023a), prompting the model in parallel to assess two orthogonal aspects. The first is Semantic Consistency (SC), which evaluates the degree of instruction following and consistency, ensuring specified objects are correctly modified while unmentioned regions remain preserved. The second is Perceptual Quality (PQ), which assesses overall image quality, focusing on photorealism and the absence of artifacts. The final score is the geometric mean of the SC and PQ scores (⟦SLOT_12⟧), yielding a balanced and granular reward signal.

**ZH** 为使 EditScore 能对编辑任务作全面评估，我们采用 VIEScore 框架（Ku et al., 2023a），并行提示模型评估两个正交的方面。其一是语义一致性（Semantic Consistency, SC），评估指令遵循与一致性的程度，确保指定对象被正确修改、未提及区域得以保留。其二是感知质量（Perceptual Quality, PQ），评估图像的整体质量，重点关注照片真实感与瑕疵的有无。最终分数取 SC 与 PQ 分数的几何平均（⟦SLOT_12⟧），得到均衡且细粒度的奖励信号。

**EN** 4.1.2 Inference-time ensembling Strategy

**ZH** 4.1.2 推理时集成策略

**EN** Recent work (Snell et al., 2024; Liu et al., 2025c) has shown that the performance of LLMs can be substantially improved by increasing the computational budget at test time. Building on this insight, we introduce an inference-time ensembling strategy for our generative reward model to systematically boost its evaluation accuracy and enhance reward stability. Our approach is straightforward: for a given input triplet ⟦SLOT_13⟧, we perform ⟦SLOT_14⟧ independent, stochastic forward passes through EditScore, and each pass ⟦SLOT_15⟧ generates a pair ⟦SLOT_16⟧. Then we aggregate only the scalar scores ⟦SLOT_17⟧ to compute the final ensembled score, ⟦SLOT_18⟧, using the arithmetic mean:

**ZH** 近期工作（Snell et al., 2024; Liu et al., 2025c）表明，增加测试时的计算预算可大幅提升大语言模型的性能。基于这一认识，我们为生成式奖励模型引入推理时集成策略，以系统性地提高评测准确率并增强奖励的稳定性。做法很直接：对给定输入三元组 ⟦SLOT_13⟧，我们通过 EditScore 执行 ⟦SLOT_14⟧ 次独立且随机的前向传播，每次传播 ⟦SLOT_15⟧ 生成一对 ⟦SLOT_16⟧；随后只汇总其中的标量分数 ⟦SLOT_17⟧，用算术平均计算最终集成分数 ⟦SLOT_18⟧：

<!-- [原子块 · table] S f ​ i ​ n ​ a ​ l ​ ( 𝐳 ) = 1 K ​ ∑ i = 1 K s i , where ​ ( reasoning i , s i ) = EditScore ​ ( 𝐳 ) . S_{final}(\mathbf{z})=\frac{1}{K}\sum_{i=1}^{K}s_{i},\quad\text{where }(\text{reasoning}_{i},s_{ -->

**EN** An intuitive explanation (Liu et al., 2025c) for this effectiveness is that each of the ⟦SLOT_19⟧ generated reasonings can be viewed as distinct judgment perspectives. Aggregating the scores derived from these diverse perspectives allows the final reward to more accurately reflect the true quality of an edit, leading to significant scaling effectiveness.

**ZH** 对其有效性有一种直观解释（Liu et al., 2025c）：⟦SLOT_19⟧ 次生成的推理过程可被视为各自不同的判断视角。汇总这些不同视角导出的分数，能使最终奖励更准确地反映一次编辑的真实质量，从而带来显著的扩展收益。

**EN** 4.2 Data Construction Pipeline

**ZH** 4.2 数据构建流程

**EN** The training data for reward model and subsequent reinforcement learning are constructed following the similar procedure. For reinforcement learning, the training data only requires the input images and instructions, whereas training the reward model additionally requires the generated outputs paired with their corresponding rewards. The construction process involves three steps as follows.

**ZH** 奖励模型与后续强化学习的训练数据按相近流程构建。强化学习只需输入图像与指令；训练奖励模型则额外需要生成输出及其对应的奖励。构建过程包含以下三个步骤。

**EN** Step I: Images selection and instructions creation. We start by selecting and filtering a diverse set of high-quality images as editing inputs. Next, we construct a series of reference instructions for various editing tasks. Using the input images and random selected reference instructions as guidance, we prompt Qwen-2.5-VL-72B to generate editing instructions that are task-consistent with the references. After generating a large set of image-instruction pairs, we applying a K-center greedy algorithm (Sener and Savarese, 2018) to select 1000 semantically diverse samples per task for reward generation.

**ZH** 步骤一：图像筛选与指令生成。 我们先筛选一组多样化的高质量图像作为编辑输入，再为各类编辑任务构造一系列参考指令。以输入图像与随机选中的参考指令为引导，提示 Qwen-2.5-VL-72B 生成与参考指令任务一致的编辑指令。得到大量图像—指令对后，用 K-center 贪心算法（Sener and Savarese, 2018）为每个任务挑选 1,000 个语义多样的样本，用于奖励生成。

**EN** Finally, we constructed 70,000 data samples for training the reward model and 60,000 samples for reinforcement learning training. The data for the reward model requires further annotation as follows.

**ZH** 最终我们构建了 70,000 条用于训练奖励模型的数据样本，以及 60,000 条用于强化学习训练的数据样本。奖励模型所用数据还需按如下方式作进一步标注。

**EN** Step II: Candidates output generation. We generate candidates output using 5 distinct editing models random selected from our model pool.

**ZH** 步骤二：候选输出生成。 从模型池中随机选取 5 个不同的编辑模型生成候选输出。

**EN** Step III: Annotate and filtering. For each candidate output, we use GPT-4.1 to annotate scores. Following VIEScore (Ku et al., 2023a), we score each output on SC and PQ and provide reasons for the assigned scores. Next, we apply filtering to the reward samples. It is conducted from two perspectives: (i) filtering based on group-wise maximum scores to remove unachievable editing tasks, and (ii) filtering by group standard deviation to remove cases with low discriminability.

**ZH** 步骤三：标注与筛选。 对每个候选输出，我们用 GPT-4.1 标注分数。依照 VIEScore（Ku et al., 2023a），为每个输出的 SC 与 PQ 打分，并给出打分理由。随后对奖励样本施加筛选，从两个角度展开：（i）依据组内最高分筛选，剔除无法完成的编辑任务；（ii）依据组内标准差筛选，剔除区分度低的样本。

**EN** 5 Reward Model Performance on EditReward-Bench

**ZH** 5 EditScore 在 EditReward-Bench 上的性能

**EN** 5.1 Experimental Setup

**ZH** 5.1 实验设置

**EN** Our final EditScore model is obtained by fine-tuning Qwen2.5-VL with LoRA (Hu et al., 2022) on our curated dataset (see Section 4.2). For evaluation, we adopt the VIEScore (Ku et al., 2024) prompt template with two key modifications: (i) enforcing a reasoning-before-scoring format, (ii) expanding the score range from ⟦SLOT_20⟧ to ⟦SLOT_21⟧. Following the formulation of VIEScore, we derive Prompt Following (⟦SLOT_22⟧) and Consistency (⟦SLOT_23⟧) from its Semantic Consistency metric ⟦SLOT_24⟧, while Overall Quality (⟦SLOT_25⟧) is directly taken from the final score ⟦SLOT_26⟧. The detailed prompt templates are shown in Appendix M.

**ZH** 最终的 EditScore 模型通过在所策管的数据集上以 LoRA（Hu et al., 2022）微调 Qwen2.5-VL 得到（见第 4.2 节）。评测时采用 VIEScore（Ku et al., 2024）的提示模板，并作两处关键修改：（i）强制“先推理、后打分”的格式；（ii）把分数区间从 ⟦SLOT_20⟧ 扩展到 ⟦SLOT_21⟧。依照 VIEScore 的形式化，我们从其语义一致性指标 ⟦SLOT_24⟧ 导出指令遵循（⟦SLOT_22⟧）与一致性（⟦SLOT_23⟧），总体质量（⟦SLOT_25⟧）则直接取最终分数 ⟦SLOT_26⟧。详细提示模板见附录 M。

**EN** Table 2: Benchmark results on EditReward-Bench, reporting both overall pairwise accuracy and a fine-grained breakdown across four categories of edit capabilities. Pairwise accuracy measures the proportion of pairs where the model correctly assigns a higher reward score to the human-preferred output. Notably, EditScore achieves superior performance even with its compact 7B size. Avg@4 denotes the average score over 4 forward passes.

**ZH** 表 2：EditReward-Bench 上的基准结果，同时报告总体成对准确率与四类编辑能力的细粒度分解。成对准确率衡量模型正确给人类偏好输出打出更高奖励分数的样本对占比。值得注意的是，EditScore 即便在 7B 这一紧凑规模下也取得了优越性能。Avg@4 表示 4 次前向传播的均分。

<!-- [原子块 · table] Model GPT-4.1 GPT-5 Gemini-2.5 Qwen2.5-VL EditScore-7B EditScore-32B EditScore-72B Metric Pro 7B 32B 72B Base Avg@4 Base Avg@4 Base Avg@4 Overall PF 0.673 0.777 0.703 0.458 0.498 0.540 0.592 0.722 0.6 -->

**EN** 5.2 Main Results

**ZH** 5.2 主要结果

**EN** Results summarized in Table 2 reveal a significant performance gap between proprietary models and open-source counterparts. Leading proprietary models such as GPT-4.1, GPT-5 and Gemini-2.5-Pro form a distinct upper tier, achieving pairwise accuracies in the 0.7-0.75 range across all dimensions. This confirms their strong, albeit imperfect, zero-shot capabilities for this nuanced task. In particular, we find that VLMs are generally stronger at assessing Prompt Following (PF) than Consistency (C), as the latter requires fine-grained comparisons between the input and output images.

**ZH** 表 2 的结果显示，专有模型与开源模型之间存在显著的性能差距。GPT-4.1、GPT-5 与 Gemini-2.5-Pro 等头部专有模型构成明显的上位梯队，各维度成对准确率处于 0.7–0.75 区间，印证了它们在这一细粒度任务上虽不完美却相当强大的零样本能力。我们特别发现，VLM 评估指令遵循（PF）通常强于一致性（C），因为后者需要在输入与输出图像之间作细粒度比对。

**EN** In stark contrast, even the largest and most capable open-source models exhibit notable limitations. The Qwen2.5-VL series shows a clear scaling trend, yet the 72B-parameter variant still falls short of 0.612 overall accuracy and performs worse than random chance in Consistency judgment. The smaller 7B and 32B models fare even worse, underscoring the inadequacy of off-the-shelf open-source VLMs as reliable reward signals for fine-grained editing tasks. By contrast, our EditScore achieves substantial improvements: the 7B variant surpasses the 10x larger Qwen2.5-VL-72B, while the 72B variant matching the score of GPT-4.1. Moreover, scaling inference-time compute with self-ensemble (Avg@4) further boosts performance across all model sizes, with EditScore-72B establishing the state of the art on EditReward-Bench.

**ZH** 与之形成鲜明反差的是，即便规模最大、能力最强的开源模型也暴露出明显局限。Qwen2.5-VL 系列呈现清晰的规模效应，但 72B 变体的总体准确率仍不足 0.612，在一致性判断上甚至劣于随机猜测；7B 与 32B 模型表现更差，说明现成的开源 VLM 不足以充当细粒度编辑任务的可靠奖励信号。相比之下，EditScore 取得了大幅提升：7B 变体超越了规模十倍于它的 Qwen2.5-VL-72B，72B 变体则与 GPT-4.1 打平。此外，用自集成（Avg@4）扩展推理时计算还能进一步提升各规模模型的性能，EditScore-72B 由此在 EditReward-Bench 上确立了最先进水平。

**EN** 5.3 Effective Inference-time scaling of EditScore

**ZH** 5.3 EditScore 的高效推理时扩展

<!-- [原子块 · object]  -->

**EN** (a) TFLOPs vs. Accuracy

**ZH** (a) TFLOPs 与准确率

<!-- [原子块 · object]  -->

**EN** (b) Latency vs. Accuracy

**ZH** (b) 时延与准确率

**EN** Figure 2: Self-ensembling offers a superior efficiency-performance trade-off compared to simply scaling model parameters. (a) TFLOPs vs. Accuracy: The colored solid lines (increasing ⟦SLOT_27⟧) show a steeper performance trajectory than the gray dashed line (scaling model size), indicating a higher return on computational investment. (b) Latency vs. Accuracy: Real-world measurements confirm that the latency cost of self-ensembling is sublinear due to shared KV-cache prefilling. Notably, EditScore-7B (⟦SLOT_28⟧) achieves higher accuracy than the single-pass EditScore-32B (⟦SLOT_29⟧) while requiring significantly less latency and hardware resources.

**ZH** 图 2：与单纯扩大模型参数相比，自集成提供了更优的效率—性能权衡。(a) TFLOPs 与准确率：彩色实线（⟦SLOT_27⟧ 递增）的性能轨迹比灰色虚线（扩大模型规模）更陡峭，说明计算投入的回报更高。(b) 时延与准确率：真实测量表明，得益于共享的 KV 缓存预填充，自集成的时延开销呈次线性。值得注意的是，EditScore-7B（⟦SLOT_28⟧）的准确率高于单次前向的 EditScore-32B（⟦SLOT_29⟧），而所需时延与硬件资源显著更少。

**EN** As shown in Table 2, both scaling model size and inference-time compute improve the performance of EditScore. To further investigate which dimension contributes more effectively, we normalize the comparison by using FLOPs as a proxy for inference cost. Figure 2 analyzes the scaling properties of EditScore from two perspectives: theoretical computational cost (TFLOPs, Left) and real-world inference latency (Right). In both plots, colored solid lines denote inference-time compute scaling (increasing ensemble size ⟦SLOT_30⟧), while the gray dashed lines represent parameter scaling (increasing model size from 7B to 72B). We observe that scaling inference-time compute yields significantly greater marginal gains than scaling model parameters. Moreover, as shown in Figure 2(b), the wall-clock latency grows sublinearly with ⟦SLOT_31⟧. This efficiency stems from the shared prefill stage across ensemble members within the attention mechanism, minimizing redundant computation. For a comprehensive breakdown of memory consumption, system throughput, and normalized hardware budgets, please refer to Appendix C.

**ZH** 如表 2 所示，扩大模型规模与增加推理时计算都能提升 EditScore 的性能。为探究哪一维度更为有效，我们以 FLOPs 作为推理成本的代理对比较作归一化。图 2 从两个角度分析 EditScore 的扩展特性：理论计算开销（TFLOPs，左）与真实推理时延（右）。两图中，彩色实线代表推理时计算的扩展（集成规模 ⟦SLOT_30⟧ 递增），灰色虚线代表参数扩展（模型规模由 7B 增至 72B）。我们观察到，扩展推理时计算的边际收益显著高于扩展模型参数。此外，如图 2(b) 所示，实际时延随 ⟦SLOT_31⟧ 呈次线性增长；这一效率源于集成成员在注意力机制中共享预填充阶段，从而把冗余计算降到最低。显存占用、系统吞吐量与归一化硬件预算的完整拆解见附录 C。

**EN** 5.4 Ablation Study

**ZH** 5.4 消融实验

**EN** We study two key factors in EditScore design: score range granularity and output format (Table 3). Increasing the target score range generally improves pairwise accuracy for both GPT-4.1 and GPT-5, peaking around ⟦SLOT_32⟧, while overly large ranges hurt performance due to regression difficulty. In parallel, requiring the model to generate a rationale before the numeric score (“reasoning + score”) consistently outperforms direct scoring, yielding a +0.038 accuracy gain for EditScore-7B (0.621 → 0.659). These findings highlight that both an appropriately chosen score range and reasoning-first output are crucial for maximizing accuracy.

**ZH** 我们考察 EditScore 设计中的两个关键因素：分数区间粒度与输出格式（表 3）。增大目标分数区间总体上会提升 GPT-4.1 与 GPT-5 的成对准确率，在 ⟦SLOT_32⟧ 附近达到峰值；区间过大则因回归难度上升而损害性能。与此同时，要求模型在给出数字分数前先生成推理依据（“推理 + 分数”）始终优于直接打分，为 EditScore-7B 带来 +0.038 的准确率增益（0.621 → 0.659）。这些发现表明，恰当的分数区间与推理优先的输出形式对最大化准确率都至关重要。

**EN** Table 3: The effect of score range granularity and reason first on the pairwise accuracy of VLMs on EditReward-Bench. The ranges (⟦SLOT_33⟧) indicate the target score space for model outputs. The lightly shaded column highlights our chosen configuration for optimal performance.

**ZH** 表 3：分数区间粒度与先推理对 VLM 在 EditReward-Bench 上成对准确率的影响。区间（⟦SLOT_33⟧）表示模型输出的目标分数空间。浅色底纹列标示我们为取得最优性能所选的配置。

<!-- [原子块 · table] Method Score Range Output Format [ 0 , 10 ] [0,10] [ 0 , 20 ] [0,20] [ 0 , 25 ] [0,25] [ 0 , 30 ] [0,30] reasoning + score score GPT-4.1 0.691 0.701 0.705 0.689 0.705 0.695 GPT-5 0.730 0.760 0.755 — 0 -->

**EN** 6 Application of EditScore in Image Editing

**ZH** 6 EditScore 在图像编辑中的应用

**EN** 6.1 Experimental Setup

**ZH** 6.1 实验设置

**EN** Evaluation Method. To evaluate the effectiveness of EditScore in improving image editing models, we design two experiments. (1) best-of-⟦SLOT_34⟧ selection: EditScore is used as a selector, where the editing model generates multiple candidate outputs per input and EditScore chooses the best one. We evaluate the gain on three popular models: OmniGen2 (Wu et al., 2025b), Flux.1-Kontext-dev Batifol et al. (2025) and Qwen-Image-Edit Wu et al. (2025a). (2) Reinforcement learning: EditScore is employed directly as a reward model to fine-tune OmniGen2 via an additional RL stage, demonstrating its utility as a training signal. We adopt two widely used image editing benchmarks—GEdit-Bench (Liu et al., 2025b) and ImgEdit-Bench (Ye et al., 2025)—which cover a diverse range of practical editing tasks, to assess the improvements brought by EditScore. For efficiency, we use 7B variant of EditScore for experiments with optional self-ensemble.

**ZH** 评测方法。 为评估 EditScore 提升图像编辑模型的效果，我们设计了两组实验。(1) best-of-⟦SLOT_34⟧ 选择：把 EditScore 用作选择器，编辑模型为每个输入生成多个候选输出，由 EditScore 挑出最佳者；我们在 OmniGen2（Wu et al., 2025b）、Flux.1-Kontext-dev Batifol et al. (2025) 与 Qwen-Image-Edit Wu et al. (2025a) 三个主流模型上评估增益。(2) 强化学习：直接以 EditScore 作为奖励模型，通过一个额外的 RL 阶段微调 OmniGen2，展示其作为训练信号的实用价值。我们采用两个广泛使用的图像编辑基准——GEdit-Bench（Liu et al., 2025b）与 ImgEdit-Bench（Ye et al., 2025）——来评估 EditScore 带来的改进，二者覆盖了多样化的实用编辑任务。出于效率考虑，实验使用 7B 版本的 EditScore，并可选地启用自集成。

**EN** RL Training. Our main experiments are conducted using OmniGen2 Wu et al. (2025b), while we also validate the generalization of our method on Flux-Kontext-dev Batifol et al. (2025). Flow-GRPO Liu et al. (2025a) is employed with hyperparameters: sampling steps ⟦SLOT_35⟧, group size ⟦SLOT_36⟧, number of unique prompts ⟦SLOT_37⟧, noise level ⟦SLOT_38⟧, and KL weight ⟦SLOT_39⟧. Ablation studies on hyperparameters are provided in Appendix E. We also reformulate the standard Flow-GRPO equation to align with OmniGen2’s notation; detailed derivations are given in Appendices F and G.

**ZH** 强化学习训练。 主要实验基于 OmniGen2 Wu et al. (2025b) 展开，同时也在 Flux-Kontext-dev Batifol et al. (2025) 上验证方法的泛化性。我们采用 Flow-GRPO Liu et al. (2025a)，超参数设置为：采样步数 ⟦SLOT_35⟧、组大小 ⟦SLOT_36⟧、唯一提示数 ⟦SLOT_37⟧、噪声水平 ⟦SLOT_38⟧、KL 权重 ⟦SLOT_39⟧。超参数的消融研究见附录 E。我们还重新表述了标准 Flow-GRPO 方程，使之与 OmniGen2 的记号一致；详细推导见附录 F 与附录 G。

**EN** 6.2 Validating EditScore Utility via best-of-⟦SLOT_40⟧ection

**ZH** 6.2 通过 best-of-⟦SLOT_40⟧ 选择验证 EditScore 的实用性

<!-- [原子块 · object]  -->

**EN** (a)

**ZH** (a)

<!-- [原子块 · object]  -->

**EN** (b)

**ZH** (b)

<!-- [原子块 · object]  -->

**EN** (c)

**ZH** (c)

**EN** Figure 3: EditScore as a superior reward signal for image editing. (a) Using EditScore to select the best sample among multiple outputs effectively improves VIEScore, with OmniGen2 showing the largest gain. (b) Incorporating EditScore into RL training yields stable and significant performance improvements, even surpassing the much larger Qwen2.5-VL-72B. (c) RL training benefits from self-ensembling, which enhances the evaluation accuracy of EditScore across diverse settings.

**ZH** 图 3：EditScore 作为优越的图像编辑奖励信号。(a) 用 EditScore 从多个输出中挑选最佳样本能有效提升 VIEScore，其中 OmniGen2 的增益最大。(b) 把 EditScore 引入强化学习训练带来稳定而显著的性能提升，甚至超过规模大得多的 Qwen2.5-VL-72B。(c) 自集成有助于强化学习训练，它在多种设置下提高了 EditScore 的评测准确率。

**EN** Before implementing full RL training, we first validate the utility of EditScore in a controlled setting. In this experiment, the editing model generates ⟦SLOT_41⟧ candidate outputs per input of GEdit-Bench, and EditScore selects the best one. This setup directly measures the reward model’s ability to identify high-quality edits. Figure 3(a) reports benchmark performance as a function of ⟦SLOT_42⟧. We evaluate three base models using both single-pass EditScore (solid lines) and the stronger Avg@4 version (dashed lines). The results highlight three key findings: (1) stronger reward models consistently yield better selections, (2) performance gains vary by base model, with Qwen-Image-Edit showing the least improvement due to prior post-training stage (Wu et al., 2025a), and (3) OmniGen2 exhibits the largest absolute potential for improvement, motivating its choice as the base model for subsequent RL experiments.

**ZH** 在推进完整的强化学习训练之前，我们先在受控条件下验证 EditScore 的实用性。该实验中，编辑模型为 GEdit-Bench 的每个输入生成 ⟦SLOT_41⟧ 个候选输出，由 EditScore 挑选最佳者；这一设置直接衡量奖励模型识别高质量编辑的能力。图 3(a) 给出基准性能随 ⟦SLOT_42⟧ 的变化。我们在三个基座模型上分别评测单次前向的 EditScore（实线）与更强的 Avg@4 版本（虚线）。结果凸显三点关键发现：(1) 奖励模型越强，选出的结果越好；(2) 增益因基座模型而异，Qwen-Image-Edit 因已有后训练阶段（Wu et al., 2025a）而提升最小；(3) OmniGen2 的绝对提升空间最大，因而被选作后续强化学习实验的基座模型。

**EN** 6.3 Online Reinforcement Learning with EditScore

**ZH** 6.3 用 EditScore 做在线强化学习

**EN** We now turn to the core application of our framework: using EditScore as a direct reward signal for online RL fine-tuning. This section systematically isolates the impact of reward quality, examines training stability, and evaluates generality across models and algorithms. We additionally provide qualitative visual comparisons in Appendix I.

**ZH** 下面转向框架的核心应用：把 EditScore 直接用作在线强化学习微调的奖励信号。本节系统地隔离奖励质量的影响、考察训练稳定性，并评估跨模型与跨算法的泛化性。定性视觉对比见附录 I。

**EN** 6.3.1 Unlocking Stable RL with a High-Fidelity Reward Signal

**ZH** 6.3.1 以高保真奖励信号解锁稳定的强化学习

**EN** To isolate the contribution of the reward signal, we conducted a controlled study using OmniGen2 as the policy model while varying the source of supervision. As summarized in Table 4, raw instruction-tuned VLMs prove ineffective as verifiers; even the large-scale Qwen2.5-VL-72B fails to provide meaningful guidance, resulting in unstable optimization trajectories (see Figure 3(b)). This underscores that parameter scale alone cannot substitute for task-specific alignment. In contrast, our specialized EditScore-7B not only stabilizes training but also demonstrates competitiveness with the proprietary GPT-4.1, surpassing it on the out-of-distribution EmuEdit benchmark (e.g., 0.900 vs. 0.884 CLIP-I). Furthermore, our approach benefits directly from stronger backbones: EditScore-8B (adapted from Qwen3-VL-8B (Bai et al., 2025a)) achieves the highest overall performance across metrics, confirming the method’s scalability with advancing VLMs.

**ZH** 为隔离奖励信号的贡献，我们以 OmniGen2 为策略模型、变换监督来源开展对照研究。如表 4 所示，未经处理的指令微调 VLM 无法充当有效的验证器；即便是大规模的 Qwen2.5-VL-72B 也无法提供有意义的指导，导致优化轨迹不稳（见图 3(b)）。这说明参数规模本身无法替代面向任务的对齐。相比之下，我们专门化的 EditScore-7B 不仅稳定了训练，还与专有模型 GPT-4.1 具有竞争力，并在分布外的 EmuEdit 基准上超越了它（例如 CLIP-I 为 0.900 对 0.884）。进一步地，本方法能直接受益于更强的骨干：EditScore-8B（改编自 Qwen3-VL-8B（Bai et al., 2025a））在各项指标上取得最高的总体性能，印证了该方法随 VLM 演进而扩展的能力。

**EN** Beyond the reward model, we further investigate the impact of test-time compute. Figure 3(c) compares policy learning curves guided by a single-pass EditScore versus a 4-pass self-ensemble strategy (Avg@4). The ensembled signal significantly improves evaluation accuracy, leading to faster convergence and superior final performance. As we discussed in Appendix L, single pass evaluation occasionally produces unstable reward signal, while self-ensemble alleviate it, thus providing a consistent gradient for the policy to traverse.

**ZH** 除奖励模型本身外，我们还考察测试时计算的影响。图 3(c) 比较了单次前向 EditScore 与 4 次自集成（Avg@4）引导下的策略学习曲线。集成后的信号显著提高了评测准确率，带来更快的收敛与更优的最终性能。正如附录 L 所讨论的，单次评测偶尔会产出不稳定的奖励信号，自集成则缓解了这一问题，从而为策略的演进提供一致的梯度。

**EN** Table 4: Controlled Evaluation of Reward Models. Using OmniGen2 as the fixed base, we compare policies trained with different reward signals. EditScore variants consistently outperform both raw VLMs and GPT-4.1, even on the out-of-distribution (OOD) EmuEdit benchmark. Note that raw Qwen2.5-VL baselines fail to provide effective guidance.

**ZH** 表 4：奖励模型的对照评测。以 OmniGen2 为固定基座，比较用不同奖励信号训练出的策略。即使在分布外（OOD）的 EmuEdit 基准上，EditScore 各变体也持续优于原始 VLM 与 GPT-4.1。注意，原始的 Qwen2.5-VL 基线无法提供有效指导。

<!-- [原子块 · table] Reward Signal GEdit-Bench ImgEdit EmuEdit (OOD) SC PQ Overall Overall CLIP-I CLIP-O DINO Baseline (No RL) 6.72 7.20 6.28 3.40 0.876 0.309 0.822 RL w/ Qwen2.5-VL-7B 6.87 6.86 6.22 - - - - RL w/ Qwen2.5 -->

**EN** 6.4 Generality Across Editors and Algorithms

**ZH** 6.4 跨编辑器与跨算法的泛化性

**EN** Table 5: Generality Analysis. Left: Consistent improvements on a different backbone (Flux-Kontext-dev). Right: Compatibility with advanced RL algorithms (TempFlow-GRPO (He et al., 2025)).

**ZH** 表 5：泛化性分析。左：在另一骨干（Flux-Kontext-dev）上的一致提升。右：与先进强化学习算法（TempFlow-GRPO（He et al., 2025））的兼容性。

**EN** (a) Flux-Kontext-dev Backbone

**ZH** (a) Flux-Kontext-dev 骨干

<!-- [原子块 · table] Method SC PQ O Baseline 6.59 7.61 6.15 RL w/ Ours 7.16 7.95 6.87 -->

**EN** (b) Algorithm Comparison (OmniGen2 base)

**ZH** (b) 算法对比（OmniGen2 基座）

<!-- [原子块 · table] Algorithm SC PQ O Flow-GRPO 7.20 7.46 6.68 TempFlow-GRPO 7.53 7.99 7.21 -->

**EN** We further assess the robustness of EditScore by varying both the underlying generative backbone and the RL optimization algorithm. Throughout the following experiments, we use EditScore-7B (Avg@4) as the reward signal.

**ZH** 我们进一步通过更换底层生成骨干与强化学习优化算法来评估 EditScore 的稳健性。以下实验中，统一使用 EditScore-7B（Avg@4）作为奖励信号。

**EN** Generality Across Editors. A reliable reward model should capture intrinsic editing quality rather than overfit to the behavior of a particular policy. To test this, we replace OmniGen2 with Flux-Kontext-dev (Batifol et al., 2025), a substantially different editing model. As shown in Table 5 (Left), EditScore-based RL consistently yields strong improvements across all metrics (e.g., +0.57 in SC and +0.72 in Overall). These results indicate that EditScore provides a model-agnostic, universally useful reward signal that effectively enhances editing policies regardless of their initialization.

**ZH** 跨编辑器的泛化性。 可靠的奖励模型应捕捉编辑质量的内在属性，而非过拟合到某一策略的行为特征。为此，我们把 OmniGen2 换成差异相当大的编辑模型 Flux-Kontext-dev（Batifol et al., 2025）。如表 5（左）所示，基于 EditScore 的强化学习在全部指标上均带来显著提升（例如 SC +0.57、Overall +0.72）。这些结果表明，EditScore 提供的是一种与模型无关、普遍可用的奖励信号，无论策略如何初始化都能有效增强其编辑能力。

**EN** Compatibility with Advanced RL Algorithms. We also study whether the reward landscape defined by EditScore supports more advanced optimization strategies. Beyond the standard Flow-GRPO, we evaluate TempFlow-GRPO (He et al., 2025), which introduces temporally aware loss reweighting to emphasize low–signal-to-noise segments during training. As shown in Table 5 (Right), combining EditScore with TempFlow-GRPO delivers further gains, achieving an Overall score of 7.21. This demonstrates that our reward signal is sufficiently stable and high-fidelity to benefit from stronger search algorithms, scaling gracefully without causing reward hacking or optimization instability.

**ZH** 与先进强化学习算法的兼容性。 我们还考察由 EditScore 定义的奖励景观能否支撑更高级的优化策略。除标准 Flow-GRPO 外，我们评估了 TempFlow-GRPO（He et al., 2025），它通过时序感知的损失重加权来强化训练中信噪比较低的分段。如表 5（右）所示，EditScore 与 TempFlow-GRPO 结合可带来进一步增益，总体得分达到 7.21。这说明我们的奖励信号足够稳定、保真度高，能够从更强的搜索算法中获益，且在扩展过程中不会引发奖励破解或优化不稳定。

**EN** 6.5 Analysis of Annotation Sources and Reward Variance

**ZH** 6.5 标注来源与奖励方差的分析

**EN** Table 6: Comparison of reward models based on annotator source. We analyze reward models (RMs) trained on data from two different annotators: GPT-4.1 and GPT-5. The resulting policy’s performance is evaluated by both annotators on GEdit-Bench (Liu et al., 2025b).

**ZH** 表 6：基于标注员来源的奖励模型对比。我们分析在两个不同标注者（GPT-4.1 与 GPT-5）标注的数据上训练出的奖励模型（RM），所得策略的性能由这两个标注者在 GEdit-Bench（Liu et al., 2025b）上评估。

<!-- [原子块 · table] Annotator Component Reward Model Metrics Policy Performance ↑ \uparrow Acc. (O) ↑ \uparrow Score Std. GPT-4.1 Score GPT-5 Score GPT-4.1 (Better for RL) Annotator (Itself) 0.705 3.309 — — ↪ \hookrighta -->

**EN** To understand the role of annotators in shaping RL performance, we trained two distinct EditScore-7B reward models on identical data subsets, annotated by GPT-4.1 and GPT-5 separately. While GPT-5 offers superior annotation accuracy, the higher score variance of GPT-4.1 provides a more effective learning signal. As shown in Table 6, EditScore trained on GPT-4.1’s labels, despite a marginal dip in accuracy (0.637 vs. 0.638), inherits a substantially higher score standard deviation (2.868 vs. 2.533). This high-variance reward signal leads to a demonstrably better policy after RL fine-tuning. Crucially, this improvement is consistent between both GPT-4.1 (6.375 vs. 6.292) and GPT-5 (5.834 vs. 5.768) evaluations, excluding potential evaluation bias from GEdit-Bench (Ye et al., 2025). Our results thus uncover a key insight: reward signal variance, rather than absolute annotator accuracy, can be the dominant factor for successful optimization of the RL-based model, corroborating similar findings from Razin et al. (2025).

**ZH** 为理解标注者在塑造强化学习性能中的作用，我们在相同的数据子集上训练了两个不同的 EditScore-7B 奖励模型，分别由 GPT-4.1 与 GPT-5 标注。GPT-5 的标注准确率更高，但 GPT-4.1 的分数方差更大，反而提供了更有效的学习信号。如表 6 所示，基于 GPT-4.1 标签训练的 EditScore 虽然准确率略有下降（0.637 对 0.638），却继承了显著更高的分数标准差（2.868 对 2.533）。这种高方差的奖励信号经强化学习微调后产出了明显更优的策略。关键在于，这一提升在 GPT-4.1（6.375 对 6.292）与 GPT-5（5.834 对 5.768）两种评测下都一致存在，排除了 GEdit-Bench（Ye et al., 2025）可能带来的评测偏差。由此我们得到一个关键认识：对基于强化学习的模型而言，奖励信号的方差（而非标注者的绝对准确率）可能才是决定优化成败的主导因素，这与 Razin et al. (2025) 的发现相印证。

**EN** 7 Conclusion

**ZH** 7 结论

**EN** In this work, we addressed the critical bottleneck for RL in image editing: the lack of a reliable reward signal. We established a comprehensive benchmark for reward model evaluation. Guided by our benchmark, we developed EditScore, a family of specialized generative reward models that deliver a robust, high-fidelity signal. Crucially, EditScore is not only efficient for Best-of-⟦SLOT_43⟧ selection but is the key to unlocking stable online RL where previous open-source models fail. By releasing both EditReward-Bench and EditScore, we provide a foundational toolkit for future research into RL-based image editing and more nuanced reward modeling.

**ZH** 本文着力解决图像编辑中强化学习的关键瓶颈：缺少可靠的奖励信号。我们建立了一个用于评测奖励模型的综合基准；在该基准的指导下，开发了 EditScore——一系列专门化的生成式奖励模型，能够提供稳健、高保真的奖励信号。关键在于，EditScore 不仅在 Best-of-⟦SLOT_43⟧ 选择中高效，更是解锁稳定在线强化学习的关键，而此前的开源模型在此均告失败。通过开源 EditReward-Bench 与 EditScore，我们为后续基于强化学习的图像编辑研究以及更精细的奖励建模提供了基础工具箱。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] Ahmadi et al. (2025) S. Ahmadi, R. Awal, A. Sikarwar, A. Kazemnejad, G. Y. Luo, J. A. Rodriguez, S. Rajeswar, S. Reddy, C. Pal, B. Krojer, et al. The promise of rl for autoregressive image editing . a -->

<!-- [原子块 · verbatim] Albergo et al. (2023) M. S. Albergo, N. M. Boffi, and E. Vanden-Eijnden Stochastic interpolants: A unifying framework for flows and diffusions . CoRR abs/2303.08797 . External Links: Link , Document , -->

<!-- [原子块 · verbatim] Bai et al. (2025a) S. Bai, Y. Cai, R. Chen, K. Chen, X. Chen, Z. Cheng, L. Deng, W. Ding, C. Gao, C. Ge, et al. Qwen3-vl technical report . arXiv preprint arXiv:2511.21631 . Cited by: §6.3.1 . -->

<!-- [原子块 · verbatim] Bai et al. (2025b) S. Bai, K. Chen, X. Liu, J. Wang, W. Ge, S. Song, K. Dang, P. Wang, S. Wang, J. Tang, et al. Qwen2. 5-vl technical report . arXiv preprint arXiv:2502.13923 . Cited by: §1 , §4.1.1 . -->

<!-- [原子块 · verbatim] Batifol et al. (2025) S. Batifol, A. Blattmann, F. Boesel, S. Consul, C. Diagne, T. Dockhorn, J. English, Z. English, P. Esser, S. Kulal, et al. FLUX. 1 kontext: flow matching for in-context image gen -->

<!-- [原子块 · verbatim] Brooks et al. (2023) T. Brooks, A. Holynski, and A. A. Efros Instructpix2pix: learning to follow image editing instructions . In Proceedings of the IEEE/CVF conference on computer vision and pattern r -->

<!-- [原子块 · verbatim] Chen et al. (2025) S. X. Chen, Y. Wei, L. Zhou, and S. Kumar ADIEE: automatic dataset creation and scorer for instruction-guided image editing evaluation . arXiv preprint arXiv:2507.07317 . Cited by:  -->

<!-- [原子块 · verbatim] Deng et al. (2025) C. Deng, D. Zhu, K. Li, C. Gou, F. Li, Z. Wang, S. Zhong, W. Yu, X. Nie, Z. Song, et al. Emerging properties in unified multimodal pretraining . arXiv preprint arXiv:2505.14683 . Ci -->

<!-- [原子块 · verbatim] Gao et al. (2025) Y. Gao, L. Gong, Q. Guo, X. Hou, Z. Lai, F. Li, L. Li, X. Lian, C. Liao, L. Liu, et al. Seedream 3.0 technical report . arXiv preprint arXiv:2504.11346 . Cited by: §2 . -->

<!-- [原子块 · verbatim] Gong et al. (2025) Y. Gong, X. Wang, J. Wu, S. Wang, Y. Wang, and X. Wu OneReward: unified mask-guided image generation via multi-task human preference learning . arXiv preprint arXiv:2508.21066 . Cit -->

<!-- [原子块 · verbatim] Google (2025) Google Introducing gemini 2.5 flash image . Note: https://developers.googleblog.com/en/introducing-gemini-2-5-flash-image/ Accessed: 2025-09-18 Cited by: §2 , §3.2 . -->

<!-- [原子块 · verbatim] He et al. (2025) X. He, S. Fu, Y. Zhao, W. Li, J. Yang, D. Yin, F. Rao, and B. Zhang Tempflow-grpo: when timing matters for grpo in flow models . arXiv preprint arXiv:2508.04324 . Cited by: §6.4 , Tab -->

<!-- [原子块 · verbatim] Hertz et al. (2022) A. Hertz, R. Mokady, J. Tenenbaum, K. Aberman, Y. Pritch, and D. Cohen-Or Prompt-to-prompt image editing with cross attention control . arXiv preprint arXiv:2208.01626 . Cited by:  -->

<!-- [原子块 · verbatim] Hu et al. (2022) E. J. Hu, Y. Shen, P. Wallis, Z. Allen-Zhu, Y. Li, S. Wang, L. Wang, W. Chen, et al. Lora: low-rank adaptation of large language models. . ICLR 1 ( 2 ), pp. 3 . Cited by: §K.1 , §5.1  -->

<!-- [原子块 · verbatim] Hurst et al. (2024) A. Hurst, A. Lerer, A. P. Goucher, A. Perelman, A. Ramesh, A. Clark, A. Ostrow, A. Welihinda, A. Hayes, A. Radford, et al. Gpt-4o system card . arXiv preprint arXiv:2410.21276 . Ci -->

<!-- [原子块 · verbatim] Jiang et al. (2024) D. Jiang, M. Ku, T. Li, Y. Ni, S. Sun, R. Fan, and W. Chen Genai arena: an open evaluation platform for generative models . Advances in Neural Information Processing Systems 37 , p -->

<!-- [原子块 · verbatim] Kirstain et al. (2023) Y. Kirstain, A. Polyak, U. Singer, S. Matiana, J. Penna, and O. Levy Pick-a-pic: an open dataset of user preferences for text-to-image generation . Advances in neural informatio -->

<!-- [原子块 · verbatim] Ku et al. (2023a) M. Ku, D. Jiang, C. Wei, X. Yue, and W. Chen Viescore: towards explainable metrics for conditional image synthesis evaluation . arXiv preprint arXiv:2312.14867 . Cited by: §3.2 , §4. -->

<!-- [原子块 · verbatim] Ku et al. (2024) M. Ku, D. Jiang, C. Wei, X. Yue, and W. Chen VIEScore: towards explainable metrics for conditional image synthesis evaluation . In Proceedings of the 62nd Annual Meeting of the Associ -->

<!-- [原子块 · verbatim] Ku et al. (2023b) M. Ku, T. Li, K. Zhang, Y. Lu, X. Fu, W. Zhuang, and W. Chen Imagenhub: standardizing the evaluation of conditional image generation models . arXiv preprint arXiv:2310.01596 . Cited  -->

<!-- [原子块 · verbatim] Li et al. (2022) J. Li, D. Li, C. Xiong, and S. Hoi Blip: bootstrapping language-image pre-training for unified vision-language understanding and generation . In International conference on machine le -->

<!-- [原子块 · verbatim] Li (2017) Y. Li Deep reinforcement learning: an overview . arXiv preprint arXiv:1701.07274 . Cited by: §1 . -->

<!-- [原子块 · verbatim] Lipman et al. (2023) Y. Lipman, R. T. Q. Chen, H. Ben-Hamu, M. Nickel, and M. Le Flow matching for generative modeling . In The Eleventh International Conference on Learning Representations, ICLR 2023 -->

<!-- [原子块 · verbatim] Liu et al. (2024) H. Liu, C. Li, Y. Li, B. Li, Y. Zhang, S. Shen, and Y. J. Lee Llavanext: improved reasoning, ocr, and world knowledge . Cited by: §2 . -->

<!-- [原子块 · verbatim] Liu et al. (2025a) J. Liu, G. Liu, J. Liang, Y. Li, J. Liu, X. Wang, P. Wan, D. Zhang, and W. Ouyang Flow-grpo: training flow matching models via online rl . arXiv preprint arXiv:2505.05470 . Cited by -->

<!-- [原子块 · verbatim] Liu et al. (2025b) S. Liu, Y. Han, P. Xing, F. Yin, R. Wang, W. Cheng, J. Liao, Y. Wang, H. Fu, C. Han, et al. Step1x-edit: a practical framework for general image editing . arXiv preprint arXiv:2504. -->

<!-- [原子块 · verbatim] Liu et al. (2025c) Z. Liu, P. Wang, R. Xu, S. Ma, C. Ruan, P. Li, Y. Liu, and Y. Wu Inference-time scaling for generalist reward modeling . External Links: 2504.02495 , Link Cited by: §4.1.2 , §4.1.2  -->

<!-- [原子块 · verbatim] Liu et al. (2025d) Z. Liu, P. Wang, R. Xu, S. Ma, C. Ruan, P. Li, Y. Liu, and Y. Wu Inference-time scaling for generalist reward modeling . arXiv preprint arXiv:2504.02495 . Cited by: §2 . -->

<!-- [原子块 · verbatim] Ma et al. (2025) Y. Ma, X. Wu, K. Sun, and H. Li HPSv3: towards wide-spectrum human preference score . arXiv preprint arXiv:2508.03789 . Cited by: §2 , §2 . -->

<!-- [原子块 · verbatim] OpenAI (2025) OpenAI GPT-5 is here . Note: https://openai.com/gpt-5/ Accessed: 2025-09-18 Cited by: §1 . -->

<!-- [原子块 · verbatim] Razin et al. (2025) N. Razin, Z. Wang, H. Strauss, S. Wei, J. D. Lee, and S. Arora What makes a reward model a good teacher? an optimization perspective . arXiv preprint arXiv:2503.15477 . Cited by: § -->

<!-- [原子块 · verbatim] Ren et al. (2024) Y. Ren, J. Wu, Y. Lu, H. Kuang, X. Xia, X. Wang, Q. Wang, Y. Zhu, P. Xie, S. Wang, et al. Byteedit: boost, comply and accelerate generative image editing . In European Conference on  -->

<!-- [原子块 · verbatim] Schulman et al. (2017) J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov Proximal policy optimization algorithms . CoRR abs/1707.06347 . External Links: Link , 1707.06347 Cited by: Append -->

<!-- [原子块 · verbatim] Sener and Savarese (2018) O. Sener and S. Savarese Active learning for convolutional neural networks: A core-set approach . In 6th International Conference on Learning Representations, ICLR 2018, Vanc -->

<!-- [原子块 · verbatim] Shao et al. (2024) Z. Shao, P. Wang, Q. Zhu, R. Xu, J. Song, M. Zhang, Y. K. Li, Y. Wu, and D. Guo DeepSeekMath: pushing the limits of mathematical reasoning in open language models . CoRR abs/2402.03 -->

<!-- [原子块 · verbatim] Snell et al. (2024) C. Snell, J. Lee, K. Xu, and A. Kumar Scaling llm test-time compute optimally can be more effective than scaling model parameters . External Links: 2408.03314 , Link Cited by: §4.1 -->

<!-- [原子块 · verbatim] Song et al. (2021) Y. Song, J. Sohl-Dickstein, D. P. Kingma, A. Kumar, S. Ermon, and B. Poole Score-based generative modeling through stochastic differential equations . In 9th International Conferenc -->

<!-- [原子块 · verbatim] Tibshirani and Efron (1993) R. J. Tibshirani and B. Efron An introduction to the bootstrap . Monographs on statistics and applied probability 57 ( 1 ), pp. 1–436 . Cited by: Appendix D . -->

<!-- [原子块 · verbatim] Wang et al. (2025a) Y. Wang, Z. Li, Y. Zang, C. Wang, Q. Lu, C. Jin, and J. Wang Unified multimodal chain-of-thought reward model through reinforcement fine-tuning . CoRR abs/2505.03318 . External Lin -->

<!-- [原子块 · verbatim] Wang et al. (2025b) Y. Wang, Y. Zang, H. Li, C. Jin, and J. Wang Unified reward model for multimodal understanding and generation . arXiv preprint arXiv:2503.05236 . Cited by: §2 , §4.1.1 . -->

<!-- [原子块 · verbatim] Wei et al. (2025) H. Wei, B. Xu, H. Liu, C. Wu, J. Liu, Y. Peng, P. Wang, Z. Liu, J. He, Y. Xietian, et al. Skywork unipic 2.0: building kontext model with online rl for unified multimodal model . arX -->

<!-- [原子块 · verbatim] Wei et al. (2022) J. Wei, X. Wang, D. Schuurmans, M. Bosma, B. Ichter, F. Xia, E. H. Chi, Q. V. Le, and D. Zhou Chain-of-thought prompting elicits reasoning in large language models . In Advances in N -->

<!-- [原子块 · verbatim] Wu et al. (2025a) C. Wu, J. Li, J. Zhou, J. Lin, K. Gao, K. Yan, S. Yin, S. Bai, X. Xu, Y. Chen, et al. Qwen-image technical report . arXiv preprint arXiv:2508.02324 . Cited by: §1 , §2 , §3.2 , §6.1  -->

<!-- [原子块 · verbatim] Wu et al. (2025b) C. Wu, P. Zheng, R. Yan, S. Xiao, X. Luo, Y. Wang, W. Li, X. Jiang, Y. Liu, J. Zhou, et al. OmniGen2: exploration to advanced multimodal generation . arXiv preprint arXiv:2506.18871  -->

<!-- [原子块 · verbatim] Wu et al. (2025c) J. Wu, Y. Gao, Z. Ye, M. Li, L. Li, H. Guo, J. Liu, Z. Xue, X. Hou, W. Liu, Y. Zeng, and W. Huang RewardDance: reward scaling in visual generation . External Links: 2509.08826 , Link -->

<!-- [原子块 · verbatim] Wu et al. (2023a) X. Wu, Y. Hao, K. Sun, Y. Chen, F. Zhu, R. Zhao, and H. Li Human preference score v2: a solid benchmark for evaluating human preferences of text-to-image synthesis . arXiv preprint a -->

<!-- [原子块 · verbatim] Wu et al. (2023b) X. Wu, K. Sun, F. Zhu, R. Zhao, and H. Li Human preference score: better aligning text-to-image models with human preference . In Proceedings of the IEEE/CVF International Conference -->

<!-- [原子块 · verbatim] Xiao et al. (2025) S. Xiao, Y. Wang, J. Zhou, H. Yuan, X. Xing, R. Yan, C. Li, S. Wang, T. Huang, and Z. Liu Omnigen: unified image generation . In Proceedings of the Computer Vision and Pattern Recog -->

<!-- [原子块 · verbatim] Xu et al. (2023) J. Xu, X. Liu, Y. Wu, Y. Tong, Q. Li, M. Ding, J. Tang, and Y. Dong Imagereward: learning and evaluating human preferences for text-to-image generation . Advances in Neural Informatio -->

<!-- [原子块 · verbatim] Xue et al. (2025) Z. Xue, J. Wu, Y. Gao, F. Kong, L. Zhu, M. Chen, Z. Liu, W. Liu, Q. Guo, W. Huang, et al. DanceGRPO: unleashing grpo on visual generation . arXiv preprint arXiv:2505.07818 . Cited by -->

<!-- [原子块 · verbatim] Ye et al. (2025) Y. Ye, X. He, Z. Li, B. Lin, S. Yuan, Z. Yan, B. Hou, and L. Yuan Imgedit: a unified image editing dataset and benchmark . arXiv preprint arXiv:2505.20275 . Cited by: §3.2 , §6.1 , §6 -->

<!-- [原子块 · verbatim] Zhang et al. (2023) K. Zhang, L. Mo, W. Chen, H. Sun, and Y. Su Magicbrush: a manually annotated dataset for instruction-guided image editing . Advances in Neural Information Processing Systems 36 , p -->

<!-- [原子块 · verbatim] Zhang et al. (2024a) S. Zhang, X. Yang, Y. Feng, C. Qin, C. Chen, N. Yu, Z. Chen, H. Wang, S. Savarese, S. Ermon, et al. Hive: harnessing human feedback for instructional visual editing . In Proceedin -->

<!-- [原子块 · verbatim] Zhang et al. (2024b) S. Zhang, B. Wang, J. Wu, Y. Li, T. Gao, D. Zhang, and Z. Wang Learning multi-dimensional human preference for text-to-image generation . In Proceedings of the IEEE/CVF Conference -->

<!-- [原子块 · verbatim] Zheng et al. (2024) Y. Zheng, R. Zhang, J. Zhang, Y. Ye, Z. Luo, Z. Feng, and Y. Ma LlamaFactory: unified efficient fine-tuning of 100+ language models . In Proceedings of the 62nd Annual Meeting of t -->

**EN** Appendix A Statement on the Use of Large Language Models (LLMs)

**ZH** 附录 A 关于使用大语言模型（LLM）的声明

**EN** In adherence to the ICLR 2026 submission guidelines, this section details the use of a Large Language Model (LLM) assistant during the preparation of this manuscript. The LLM, acting as a research and writing co-pilot, played a significant role in refining the manuscript’s structure, language, and presentation. The authors maintained full intellectual control throughout the process and take complete responsibility for all content.

**ZH** 遵照 ICLR 2026 投稿指南，本节说明在准备本稿件过程中使用大语言模型（LLM）助手的情况。该 LLM 作为研究与写作的协作者，在打磨稿件结构、语言与呈现方面发挥了重要作用。作者在整个过程中保持完全的智力主导，并对全部内容承担全部责任。

**EN** The precise role of the LLM can be categorized as follows:

**ZH** LLM 的确切作用可归类如下：

**EN** • Manuscript Writing and Polishing: The authors wrote the initial drafts for all sections of the paper, providing the key technical details, experimental results, and core arguments. The LLM was then used extensively as an interactive writing assistant to: – Enhance Clarity and Conciseness: Rephrasing long or complex sentences to improve readability and flow. – Improve Academic Tone: Suggesting more formal and professional vocabulary and sentence structures appropriate for a top-tier conference submission. – Correct Grammar and Syntax: Performing comprehensive proofreading to identify and correct grammatical errors, typos, and awkward phrasing. – Suggest Alternative Phrasing: Providing multiple options for expressing a single idea to avoid repetitive language).

**ZH** • 稿件撰写与润色：作者撰写了论文各部分的初稿，提供关键技术细节、实验结果与核心论点；随后广泛地将 LLM 用作交互式写作助手，以：– 提升清晰度与简洁性：改写冗长或复杂的句子，改善可读性与行文流畅度。– 改善学术语调：建议更正式、更专业、更契合顶会投稿要求的词汇与句式。– 修正语法与句法：进行全面校对，识别并纠正语法错误、笔误与生硬表述。– 提供替代表述：为同一意思给出多种表达选项，避免用词重复。

**EN** • Technical Formalization: For complex mathematical sections, such as the derivation of the SDE from the ODE in Appendix F, the authors provided the core mathematical steps and handwritten notes. The LLM assisted in translating these steps into a clear, well-structured narrative and formatting them professionally in LaTeX. The LLM did not generate novel mathematical proofs but rather helped in their presentation.

**ZH** • 技术形式化：对于复杂的数学部分（如附录 F 中由 ODE 推导 SDE），作者提供核心数学步骤与手写笔记，LLM 协助把这些步骤整理成清晰、结构良好的叙述，并以 LaTeX 作专业排版。LLM 并未生成新的数学证明，只是在呈现上提供了帮助。

**EN** Throughout this collaborative process, every suggestion and piece of text generated by the LLM was critically reviewed, edited, and approved by the human authors. The authors are solely responsible for the scientific validity, originality, and all claims made in this paper. The LLM is not considered an author.

**ZH** 在这一协作过程中，LLM 生成的每一条建议与每一段文本都经过作者的批判性审阅、编辑与确认。作者对本文的科学有效性、原创性以及全部论断负全责。LLM 不被视为作者。

**EN** Appendix B Disagreement Analysis of Annotation Protocol

**ZH** 附录 B 标注协议的分歧分析

**EN** To ensure the high fidelity of the EditReward-Bench dataset, we prioritized minimizing annotation noise and subjectivity. While standard crowdsourcing often relies on aggregating labels from independent workers, evaluating image editing involves subtle visual inspections that are prone to individual oversight.

**ZH** 为确保 EditReward-Bench 数据集的高保真度，我们把降低标注噪声与主观性放在首位。标准众包通常依赖聚合独立标注者的标签，而图像编辑的评测涉及细微的视觉审视，容易因个体差异产生疏漏。

**EN** To validate our choice of the Two-Annotator Discussion Protocol, we conducted a controlled study comparing it against a standard Single-Annotator baseline.

**ZH** 为验证双标注员讨论协议这一选择，我们开展了一项对照研究，将其与标准的单标注员基线作比较。

**EN** B.1 Controlled Study Setup

**ZH** B.1 对照研究设置

**EN** We recruited experts from our annotation pool and divided the validation process into two distinct rounds to annotate the same subset of samples across three evaluation dimensions: Prompt Following (PF), Consistency (C), and Overall Quality (O).

**ZH** 我们从标注员库中招募专家，把验证过程分为两轮，对同一批样本子集按三个评测维度——指令遵循（PF）、一致性（C）与总体质量（O）——进行标注。

**EN** • Baseline: Single Annotator. Four experts annotated the samples independently. We analyzed the consistency among these independent raters.

**ZH** • 基线：单标注员。四名专家独立标注样本，我们分析这些独立评分者之间的一致性。

**EN** • Ours: Annotator Pair (Two-Annotator Group). Eight experts were randomly formed into four pairs. Each pair followed our proposed protocol: they examined images together, discussed visual artifacts in real-time to reach a consensus. This process typically requires more time per sample than single-annotator approaches.

**ZH** • 本方法：标注员结对（双标注员组）。八名专家随机组成四对，每对遵循我们提出的协议：共同审视图像、实时讨论视觉瑕疵以达成共识。该过程通常比单标注员方式更耗时。

**EN** B.2 Metrics

**ZH** B.2 指标

**EN** We evaluate the reliability of our annotation process using two key metrics:

**ZH** 我们用两个关键指标评估标注流程的可靠性：

**EN** 1. Convergence Rate: This metric quantifies inter-annotator consistency. It calculates the probability that distinct annotation units—whether individual experts (Single Annotators) or discussion groups (Annotator Pairs)—assign identical rankings to the same input.

**ZH** 1. 收敛率：该指标量化标注员间的一致性，计算不同标注单元——无论是独立专家（单标注员）还是讨论组（标注员结对）——对同一输入给出相同排序的概率。

**EN** 2. Agreement with Majority Vote: Serving as a proxy for ground truth, the majority vote is derived by aggregating all available annotations for a sample. This metric measures the alignment between an individual unit’s ranking and the collective consensus. High agreement indicates that the judgment of a single unit reliably reflects the expert consensus, thereby justifying our efficient single-pass annotation strategy.

**ZH** 2. 与多数投票的一致率：多数投票由聚合某样本的全部可得标注得到，作为真值的代理。该指标衡量单个标注单元的排序与集体共识的吻合程度。高一致率说明单个单元的判断能可靠反映专家共识，从而为我们高效的单轮标注策略提供了依据。

**EN** B.3 Results and Analysis

**ZH** B.3 结果与分析

**EN** Impact of Discussion on Visual Consistency.

**ZH** 讨论对视觉一致性的影响。

**EN** As shown in Table 7, the Two-Annotator protocol consistently outperforms the Single-Annotator baseline across all dimensions. Notably, the most significant improvement is observed in the Consistency dimension, where the strict agreement rate (100% threshold) increased by 12.12% (from 82.88% to 95.00%). We attribute this to the inherent nature of image editing evaluation: inconsistency often manifests as subtle background distortions or minor structural artifacts that are easily overlooked by a single individual. The real-time discussion protocol acts as a verification mechanism, forcing annotators to cross-check visual details and effectively eliminating such oversights.

**ZH** 如表 7 所示，双标注员协议在各维度上均持续优于单标注员基线。最显著的提升出现在一致性维度：严格一致率（100% 阈值）提高了 12.12%（由 82.88% 升至 95.00%）。我们将其归因于图像编辑评测的固有特性——不一致往往表现为细微的背景畸变或轻微的结构瑕疵，单个人极易忽略。实时讨论协议充当了校验机制，迫使标注员交叉核对视觉细节，有效消除了此类疏漏。

**EN** Validation of Multi-Dimensional Evaluation.

**ZH** 多维度评测的有效性。

**EN** The results also highlight the importance of our decomposed evaluation strategy. Across both annotation settings, the agreement rates for Prompt Following and Consistency are consistently higher than for Overall Quality (e.g., 93-95% vs. 90% in strict agreement). This disparity underscores the fact that ”Overall Quality” is inherently more subjective and prone to rater bias. By explicitly separating the evaluation into specific, objective dimensions (PF and C), we ensure that the majority of EditReward-Bench relies on rigorous, reproducible criteria, rather than vague holistic impressions.

**ZH** 结果也凸显了我们分解式评测策略的重要性。在两种标注设置下，指令遵循与一致性的一致率都持续高于总体质量（严格一致率分别为 93–95% 与 90%）。这一差异说明“总体质量”天然更为主观、更易受评分者偏见影响。通过把评测显式拆分为具体、客观的维度（PF 与 C），我们确保 EditReward-Bench 的绝大部分内容依赖严谨、可复现的判据，而非模糊的整体印象。

**EN** Efficiency and Reliability of Single-Pass Annotation.

**ZH** 单轮标注的效率与可靠性。

**EN** Finally, Table 8 demonstrates that the rankings produced by a single Annotator Pair achieve near-perfect alignment with the collective majority vote, averaging over 97% across all dimensions (with Consistency reaching 99.55%). This finding is crucial for the scalability of our benchmark. It indicates that the consensus reached by one expert pair is statistically equivalent to the “ground truth” derived from a larger pool of annotators. Consequently, this justifies our strategy of annotating each sample only once (by a single pair), allowing us to maintain high-fidelity ground truth while significantly optimizing annotation costs compared to multi-pass crowdsourcing methods.

**ZH** 最后，表 8 显示，单个标注员结对给出的排序与集体多数投票几乎完全一致，各维度平均超过 97%（一致性维度达 99.55%）。这一发现对基准的可扩展性至关重要：它表明一对专家达成的共识在统计上等价于由更大规模标注员池导出的“真值”。因此，每个样本仅标注一次（由一对专家完成）的策略得以成立，使我们既能维持高保真真值，又能相比多轮众包方法大幅优化标注成本。

**EN** Table 7: Convergence Rate Comparison. The Annotator Pair protocol consistently outperforms the Single Annotator baseline. The substantial improvement in Consistency (+12.12%) confirms that the discussion protocol helps identify subtle visual artifacts often missed by individuals.

**ZH** 表 7：收敛率对比。标注员结对协议持续优于单标注员基线。一致性维度的大幅提升（+12.12%）证明，讨论协议有助于发现常被个人忽略的细微视觉瑕疵。

<!-- [原子块 · table] Metric Prompt Following (PF) Consistency (C) Overall Quality (O) Single Pair (Ours) Single Pair (Ours) Single Pair (Ours) 75% Threshold 92.23% 95.24% (+3.01%) 87.39% 95.71% (+8.32%) 84.97% 92.01% (+7. -->

**EN** Table 8: Agreement with Majority Vote. Comparing Single Annotators vs. Annotator Pairs against the collective majority vote. The high agreement (⟦SLOT_44⟧) of Annotator Pairs justifies our efficient single-pass annotation strategy.

**ZH** 表 8：与多数投票的一致率。比较单标注员与标注员结对相对集体多数投票的表现。标注员结对的高一致率（⟦SLOT_44⟧）证明我们高效的单轮标注策略是合理的。

<!-- [原子块 · table] Unit ID Prompt Following (PF) Consistency (C) Overall Quality (O) Single Pair (Ours) Single Pair (Ours) Single Pair (Ours) Unit 1 100.00% 97.80% 100.00% 100.00% 97.09% 97.18% Unit 2 100.00% 100.00% 93 -->

**EN** Appendix C Efficiency and Computational Cost Analysis of EditScore

**ZH** 附录 C EditScore 的效率与计算开销分析

**EN** While the self-ensemble strategy effectively boosts reward accuracy, it is crucial to evaluate its computational overhead to ensure practicality in real-world deployments. In this section, we provide a comprehensive analysis of memory consumption, wall-clock latency, and cost-normalized performance specifically for our EditScore models.

**ZH** 自集成策略虽能有效提升奖励准确率，但评估其计算开销对确保真实部署的可行性十分必要。本节针对 EditScore 模型，全面分析显存占用、实际时延与成本归一化后的性能。

**EN** C.1 Memory Consumption and Hardware Setup

**ZH** C.1 显存占用与硬件配置

**EN** A common concern with ensemble methods is the potential explosion in memory usage. However, our self-ensemble approach does not increase memory consumption relative to the base model. Since all ⟦SLOT_45⟧ queries are processed by the same underlying model instance, the weights are shared on the host GPU. The memory footprint is determined solely by the model parameters, not the ensemble size ⟦SLOT_46⟧.

**ZH** 集成方法常见的顾虑是显存占用可能暴涨，但我们的自集成方法并不会相对基座模型增加显存消耗。由于全部 ⟦SLOT_45⟧ 次查询都由同一个底层模型实例处理，权重在宿主 GPU 上共享，显存占用仅由模型参数决定，与集成规模 ⟦SLOT_46⟧ 无关。

**EN** In our experiments, we utilized NVIDIA H100 GPUs. To ensure efficient inference latency via Tensor Parallelism (TP), we adopted the following hosting configurations:

**ZH** 实验中我们使用 NVIDIA H100 GPU。为通过张量并行（Tensor Parallelism, TP）获得高效的推理时延，采用如下部署配置：

**EN** • EditScore-7B: Hosted on 1 ⟦SLOT_47⟧ NVIDIA H100.

**ZH** • EditScore-7B：部署在 1⟦SLOT_47⟧ 块 NVIDIA H100 上。

**EN** • EditScore-32B: Hosted on 2 ⟦SLOT_48⟧ NVIDIA H100 (TP=2).

**ZH** • EditScore-32B：部署在 2⟦SLOT_48⟧ 块 NVIDIA H100 上（TP=2）。

**EN** • EditScore-72B: Hosted on 4 ⟦SLOT_49⟧ NVIDIA H100 (TP=4).

**ZH** • EditScore-72B：部署在 4⟦SLOT_49⟧ 块 NVIDIA H100 上（TP=4）。

**EN** C.2 Wall-Clock Efficiency and Latency

**ZH** C.2 实际效率与时延

**EN** Although setting ⟦SLOT_50⟧ implies four logical forward passes, the impact on wall-clock latency is sublinear. In our deployment (using efficient serving frameworks like sglang), the prefill stage is shared across the ⟦SLOT_51⟧ diverse decoding paths. Consequently, increasing ⟦SLOT_52⟧ reduces throughput but does not simply multiply latency by ⟦SLOT_53⟧.

**ZH** 虽然设置 ⟦SLOT_50⟧ 意味着四次逻辑上的前向传播，但对实际时延的影响是次线性的。在使用 sglang 等高效服务框架的部署中，预填充阶段在 ⟦SLOT_51⟧ 条不同的解码路径之间共享。因此，增大 ⟦SLOT_52⟧ 会降低吞吐量，却并不会简单地把时延乘以 ⟦SLOT_53⟧。

**EN** Real-World RL Training Context.

**ZH** 真实强化学习训练场景。

**EN** To illustrate the practical impact, we measured latencies during our Reinforcement Learning (RL) fine-tuning pipeline. A single training step involves 576 reward queries. Using EditScore-7B-avg4 on an 8⟦SLOT_54⟧H100 cluster, the system completes all queries in approximately 18 seconds. This constitutes only ⟦SLOT_55⟧20% of the total training iteration time, confirming that the reward calculation is not a bottleneck.

**ZH** 为说明实际影响，我们测量了强化学习微调流水线中的时延。单个训练步涉及 576 次奖励查询；在 8⟦SLOT_54⟧H100 集群上使用 EditScore-7B-avg4，系统约在 18 秒内完成全部查询，仅占整个训练迭代时间的 ⟦SLOT_55⟧20%，说明奖励计算并非瓶颈。

**EN** C.3 Cost-Normalized Performance Trade-off

**ZH** C.3 成本归一化后的性能权衡

**EN** To provide a fair comparison under a fixed hardware budget, we normalize the throughput calculations to a standard compute node equipped with 4 ⟦SLOT_56⟧ NVIDIA H100 GPUs.

**ZH** 为在固定硬件预算下作公平比较，我们把吞吐量计算归一化到配备 4⟦SLOT_56⟧ 块 NVIDIA H100 GPU 的标准计算节点。

**EN** Based on our hosting configurations above:

**ZH** 基于上述部署配置：

**EN** • EditScore-7B (1 GPU/instance) allows hosting 4 parallel instances, quadrupling the system throughput.

**ZH** • EditScore-7B（每实例 1 块 GPU）可部署 4 个并行实例，使系统吞吐量翻两番。

**EN** • EditScore-32B (2 GPUs/instance) allows hosting 2 parallel instances.

**ZH** • EditScore-32B（每实例 2 块 GPU）可部署 2 个并行实例。

**EN** • EditScore-72B (4 GPUs/instance) allows hosting 1 instance.

**ZH** • EditScore-72B（每实例 4 块 GPU）可部署 1 个实例。

**EN** Table 9 presents the accuracy and the projected system throughput under this standardized budget.

**ZH** 表 9 给出该标准化预算下的准确率与系统吞吐量预估。

**EN** Table 9: Efficiency–Performance Trade-off under Fixed Budget (4⟦SLOT_57⟧H100). We compare accuracy against the total system throughput derived from a 4-GPU budget. By leveraging parallel instances, smaller models with self-ensemble (⟦SLOT_58⟧) achieve both superior accuracy and higher throughput than larger single models.

**ZH** 表 9：固定预算（4⟦SLOT_57⟧H100）下的效率—性能权衡。我们比较准确率与由 4 卡预算导出的系统总吞吐量。借助并行实例，采用自集成（⟦SLOT_58⟧）的小模型在准确率与吞吐量两方面都优于单次前向的大模型。

<!-- [原子块 · table] Model Size Ensemble ( K K ) Accuracy GPUs per Instance Parallel Instances System Throughput TFLOPs (Overall) (Used) (on 4 × \times H100) (samples/s) (per sample) EditScore-7B K = 1 K=1 0.659 1 4 37.84 -->

**EN** Key Observations.

**ZH** 主要观察。

**EN** 1. High Accuracy at Higher Throughput: The analysis reveals that EditScore-7B (⟦SLOT_59⟧) is a particularly efficient configuration. It achieves an accuracy of 0.727, which is significantly higher than the single-pass EditScore-32B (⟦SLOT_60⟧) at 0.680. More importantly, under the same 4-GPU budget, the 7B ensemble offers nearly double the throughput (16.24 vs. 9.48 samples/s) because the hardware can accommodate 4 parallel 7B instances versus only 2 32B instances.

**ZH** 1. 更高吞吐量下的高准确率：分析显示 EditScore-7B（⟦SLOT_59⟧）是特别高效的配置，其准确率达 0.727，显著高于单次前向的 EditScore-32B（⟦SLOT_60⟧）的 0.680。更重要的是，在同样的 4 卡预算下，7B 集成方案的吞吐量近乎翻倍（16.24 对 9.48 samples/s），因为硬件可容纳 4 个并行的 7B 实例，而 32B 只能容纳 2 个。

**EN** 2. Efficiency “Sweet Spot”: While larger models (72B) provide the highest absolute accuracy (0.763), they come at a steep cost in throughput (1.60 samples/s). For high-volume applications like RL training, the 7B (⟦SLOT_61⟧) setting provides the optimal balance, delivering state-of-the-art reward signals with acceptable latency.

**ZH** 2. 效率“甜点区”：更大规模的模型（72B）虽取得最高的绝对准确率（0.763），但吞吐量代价高昂（1.60 samples/s）。对于强化学习训练这类高吞吐需求的应用，7B（⟦SLOT_61⟧）设置处在最优平衡点上，以可接受的时延提供最先进的奖励信号。

**EN** 3. Scalability: The results confirm that increasing ⟦SLOT_62⟧ for smaller models is a more cost-effective strategy than scaling up model size. The self-ensemble approach effectively trades abundant parallel compute (which is often cheaper than high-memory nodes) for quality improvements.

**ZH** 3. 可扩展性：结果证实，对小模型增大 ⟦SLOT_62⟧ 比扩大模型规模更具性价比。自集成方法实际上是用充裕的并行算力（通常比大显存节点更便宜）换取质量提升。

**EN** In summary, when normalized for hardware budget, the self-ensemble strategy (⟦SLOT_63⟧) on smaller models proves to be highly efficient, outperforming larger baselines in both accuracy and system throughput.

**ZH** 综上，按硬件预算归一化后，小模型上的自集成策略（⟦SLOT_63⟧）效率极高，在准确率与系统吞吐量两方面都优于更大规模的基线。

**EN** Appendix D Statistical Significance Analysis

**ZH** 附录 D 统计显著性分析

**EN** To rigorously validate that the performance improvements reported in our main results (specifically for EditScore and the downstream RL fine-tuning) are not attributed to random variance, we conducted a comprehensive statistical significance analysis using paired bootstrap tests (Tibshirani and Efron, 1993).

**ZH** 为严格验证主要结果（特别是 EditScore 本身与下游强化学习微调）中的性能提升并非源于随机波动，我们用配对自助法检验（paired bootstrap tests）（Tibshirani and Efron, 1993）开展了全面的统计显著性分析。

**EN** D.1 Methodology

**ZH** D.1 方法

**EN** For every comparison between a baseline model ⟦SLOT_64⟧ and our method ⟦SLOT_65⟧, we performed 10,000 bootstrap resampling rounds. In each round, we resampled the evaluation pairs from the test set with replacement and recomputed the performance metric for both models to obtain the difference ⟦SLOT_66⟧.

**ZH** 对基线模型 ⟦SLOT_64⟧ 与本方法 ⟦SLOT_65⟧ 之间的每一次比较，我们执行 10,000 轮自助重采样。每轮从测试集中有放回地重采样评测样本对，并重新计算两个模型的性能指标，得到差值 ⟦SLOT_66⟧。

**EN** Based on the distribution of these 10,000 differences, we computed:

**ZH** 基于这 10,000 个差值的分布，我们计算：

**EN** 1. 95% Confidence Intervals (CI): The range within which the true performance difference lies with 95% probability. An interval strictly above zero indicates a significant improvement.

**ZH** 1. 95% 置信区间（CI）：真实性能差值以 95% 概率落入的范围。区间严格大于零即表示提升显著。

**EN** 2. One-sided p-values: The proportion of bootstrap resamples where our method failed to outperform the baseline (i.e., ⟦SLOT_67⟧). A p-value ⟦SLOT_68⟧ indicates statistical significance.

**ZH** 2. 单侧 p 值：本方法未能优于基线的自助重采样所占比例（即 ⟦SLOT_67⟧）。p 值 ⟦SLOT_68⟧ 表示具有统计显著性。

**EN** D.2 Significance of EditScore Performance

**ZH** D.2 EditScore 性能的显著性

**EN** We compared EditScore against the baseline reward model Qwen2.5-VL across three model scales (7B, 32B, and 72B) on EditReward-Bench. As detailed in Table 10, EditScore demonstrates statistically significant improvements across all metrics and scales. Notably:

**ZH** 我们在 EditReward-Bench 上、跨 7B、32B 与 72B 三个模型规模，把 EditScore 与基线奖励模型 Qwen2.5-VL 作比较。如表 10 所示，EditScore 在全部指标与全部规模上均取得统计显著的提升。值得注意的是：

**EN** • For the 7B and 32B models, the p-values are extremely low (⟦SLOT_69⟧), indicating robust superiority.

**ZH** • 对于 7B 与 32B 模型，p 值极低（⟦SLOT_69⟧），表明优势稳健。

**EN** • Even at the 72B scale, where baselines are stronger, EditScore maintains significance with ⟦SLOT_70⟧ across all dimensions, with the difference in Consistency (C) and Overall (O) being particularly significant (⟦SLOT_71⟧).

**ZH** • 即便在基线更强的 72B 规模上，EditScore 仍以 ⟦SLOT_70⟧ 在各维度保持显著性，其中一致性（C）与总体（O）的差异尤为显著（⟦SLOT_71⟧）。

**EN** Table 10: Statistical Significance on EditReward-Bench. We report the mean scores, the performance delta (⟦SLOT_72⟧), the 95% Confidence Interval (CI) of the delta, and the one-sided p-value. All improvements are statistically significant (⟦SLOT_73⟧).

**ZH** 表 10：EditReward-Bench 上的统计显著性。报告均值、性能差值（⟦SLOT_72⟧）、差值的 95% 置信区间（CI）与单侧 p 值。所有提升均具有统计显著性（⟦SLOT_73⟧）。

<!-- [原子块 · table] Size Metric Baseline (Qwen2.5-VL) EditScore (Ours) Δ \Delta (Ours - Base) 95% CI of Δ \Delta p-value 7B PF 0.458 0.592 + 0.134 \bm{+0.134} [ 0.0360 , 0.1271 ] [0.0360,0.1271] 0.0001 \bm{0.0001} C 0.32 -->

**EN** D.3 Significance of RL Fine-Tuning Improvements

**ZH** D.3 强化学习微调提升的显著性

**EN** We further validated the improvements observed in the Reinforcement Learning (RL) experiments on GEdit-Bench. Here, we compared the RL policy trained with the Baseline Reward Model (Qwen2.5-VL-72B) against the policy trained with EditScore-7B-avg4.

**ZH** 我们进一步在 GEdit-Bench 上验证强化学习实验中观察到的提升。此处比较用基线奖励模型（Qwen2.5-VL-72B）训练的策略与用 EditScore-7B-avg4 训练的策略。

**EN** Table 11 confirms that using EditScore as the reward signal leads to highly significant improvements (⟦SLOT_74⟧) across all evaluation metrics: Semantic Consistency (SC), Perceptual Quality (PQ), and Overall score (O). This indicates that the gains provided by EditScore are robust and translate effectively to downstream policy optimization.

**ZH** 表 11 证实，以 EditScore 作为奖励信号在全部评测指标——语义一致性（SC）、感知质量（PQ）与总体得分（O）——上带来高度显著的提升（⟦SLOT_74⟧）。这说明 EditScore 带来的增益是稳健的，并能有效传递到下游的策略优化中。

**EN** Table 11: Statistical Significance on GEdit-Bench (RL Fine-Tuning). Comparison between RL policies trained with the Baseline Reward vs. EditScore Reward. The high positive ⟦SLOT_75⟧ and low p-values confirm the robustness of our RL gains.

**ZH** 表 11：GEdit-Bench 上的统计显著性（强化学习微调）。比较用基线奖励与 EditScore 奖励训练的强化学习策略。高正值 ⟦SLOT_75⟧ 与低 p 值印证了我们强化学习增益的稳健性。

<!-- [原子块 · table] Metric RL (Baseline Reward) RL (EditScore Reward) Δ \Delta Improvement 95% CI of Δ \Delta p-value SC 6.89 7.20 +0.338 [ 0.1448 , 0.5276 ] [0.1448,0.5276] 0.0003 PQ 7.21 7.46 +0.235 [ 0.1121 , 0.3569 ] -->

**EN** Appendix E Additional Ablation Studies on Hyperparameters of RL

**ZH** 附录 E 强化学习超参数的补充消融研究

**EN** In this section, we present a detailed analysis of the influence of key RL hyperparameters on the performance of our proposed method. Specifically, we investigate the impact of the number of inference steps during sampling and the group size (i.e., the number of samples generated per prompt) used during Reinforcement Learning (RL) training. All results reported in this section are based on the GEdit-Bench Liu et al. (2025b).

**ZH** 本节详细分析关键强化学习超参数对所提方法性能的影响，具体考察采样阶段的推理步数以及强化学习训练中的组大小（即每个提示生成的样本数）。本节全部结果均基于 GEdit-Bench Liu et al. (2025b)。

**EN** E.1 Impact of Inference Steps

**ZH** E.1 推理步数的影响

**EN** Table 12: Ablation studies on RL hyperparameters evaluated on GEdit-Bench Liu et al. (2025b).

**ZH** 表 12：在 GEdit-Bench Liu et al. (2025b) 上评测的强化学习超参数消融研究。

**EN** (a) Impact of Inference Steps (⟦SLOT_76⟧).

**ZH** (a) 推理步数（⟦SLOT_76⟧）的影响。

<!-- [原子块 · table] Steps SC PQ O 12 7.35 7.75 6.98 16 7.42 7.80 7.11 20 7.53 7.99 7.21 -->

**EN** (b) Impact of Group Size (under fixed global batch size).

**ZH** (b) 组大小的影响（固定全局批大小下）。

<!-- [原子块 · table] Unique Prompts Group Size SC PQ O 36 8 7.36 7.89 7.07 24 12 7.53 7.99 7.21 18 16 7.26 7.80 6.90 -->

**EN** We first examine the effect of varying the number of inference steps (⟦SLOT_77⟧) employed by the flow model. Table 12(a) summarizes the model performance with ⟦SLOT_78⟧.

**ZH** 我们首先考察流模型所用推理步数（⟦SLOT_77⟧）变化带来的影响。表 12(a) 汇总了 ⟦SLOT_78⟧ 时模型的性能。

**EN** As illustrated in Table 12(a), increasing the number of inference steps leads to consistent improvements across all evaluated metrics (SC, PQ, and O). This trend aligns with expectations, as a larger number of steps enables the SDE solver to generate higher-fidelity samples that more accurately reflect the underlying model distribution. Consequently, this yields more reliable reward signals during training. Conversely, reducing the steps may introduce discretization errors or artifacts, thereby degrading the quality of reward estimation and subsequent policy updates.

**ZH** 如表 12(a) 所示，增加推理步数会在全部评测指标（SC、PQ 与 O）上带来一致提升。这一趋势符合预期：步数越多，SDE 求解器生成的样本保真度越高，越能准确反映底层模型分布，从而在训练中产生更可靠的奖励信号。反之，减少步数可能引入离散化误差或伪影，进而损害奖励估计与后续策略更新的质量。

**EN** E.2 Impact of Group Size

**ZH** E.2 组大小的影响

**EN** Next, we analyze the trade-off between the group size (i.e., the number of samples generated per prompt) and the diversity of prompts within a training batch. To ensure a fair comparison, we maintain a constant total computational budget (i.e., the total number of tokens processed per update remains fixed). Therefore, an increase in group size necessitates a proportional decrease in the number of unique prompts included in each batch.

**ZH** 接下来分析组大小（即每个提示生成的样本数）与训练批内提示多样性之间的权衡。为保证公平比较，我们保持总计算预算不变（即每次更新处理的 token 总数固定），因此组大小增大时，每批包含的唯一提示数须成比例减少。

**EN** The results are presented in Table 12(b). We observe an optimal configuration at a group size of 12:

**ZH** 结果见表 12(b)。我们观察到组大小为 12 时是最优配置：

**EN** • Small Group Size (8): While this setting allows the model to encounter a greater diversity of unique prompts (36), the variance in advantage estimation for each prompt increases due to fewer samples. This instability can lead to noisy and suboptimal policy updates.

**ZH** • 小组大小（8）：该设置让模型接触更多样化的唯一提示（36 个），但由于每个提示的样本数较少，优势估计的方差增大。这种不稳定性会导致策略更新噪声大、趋于次优。

**EN** • Large Group Size (16): Although advantage estimation becomes more stable with a larger group size, the significant reduction in unique prompts (18) limits batch diversity. This lack of diversity appears to hinder the model’s ability to generalize effectively, resulting in a notable performance drop (e.g., the O score decreases to 6.90).

**ZH** • 大组大小（16）：组大小增大后优势估计更为稳定，但唯一提示数显著减少（18 个），限制了批内多样性；多样性的缺乏似乎妨碍了模型的有效泛化，导致性能明显下降（例如 O 分数降至 6.90）。

**EN** • Optimal Group Size (12): Our empirical results indicate that a group size of 12 yields the best performance. This setting strikes an effective balance, providing sufficient samples for stable advantage estimation while maintaining adequate prompt diversity to ensure robust generalization.

**ZH** • 最优组大小（12）：实证结果表明组大小为 12 时性能最佳。该设置在“为稳定的优势估计提供充足样本”与“保持足够的提示多样性以确保稳健泛化”之间取得了有效平衡。

**EN** Appendix F Derivation of the SDE Formulation for Flow Matching

**ZH** 附录 F 流匹配的随机微分方程形式推导

**EN** This appendix derives the stochastic differential equation (SDE) underlying policy sampling in our Flow Matching model. Unlike prior work such as Flow-GRPO (Liu et al., 2025a), our base model OmniGen2 defines the probability path from noise at ⟦SLOT_79⟧ (⟦SLOT_80⟧) to data at ⟦SLOT_81⟧ (⟦SLOT_82⟧), reversing the convention in some other studies. This leads to a different drift term in the resulting SDE. The derivation proceeds in three steps: (i) connecting the deterministic ODE and a general SDE via the Fokker–Planck equation, (ii) relating the score term to the learned vector field, and (iii) constructing the discretized transition kernel.

**ZH** 本附录推导 Flow Matching 模型中策略采样所依据的随机微分方程（SDE）。与 Flow-GRPO（Liu et al., 2025a）等既有工作不同，我们的基座模型 OmniGen2 把概率路径定义为从 ⟦SLOT_79⟧（⟦SLOT_80⟧）处的噪声到 ⟦SLOT_81⟧（⟦SLOT_82⟧）处的数据，与另一些研究的约定相反，这导致所得 SDE 的漂移项不同。推导分三步进行：(i) 通过 Fokker–Planck 方程把确定性 ODE 与一般 SDE 联系起来；(ii) 把得分项与学习到的向量场关联起来；(iii) 构造离散化的转移核。

**EN** F.1 Connecting the Probability Flow ODE to an SDE

**ZH** F.1 把概率流 ODE 连接到 SDE

**EN** Our Flow Matching model (Lipman et al., 2023) is trained to approximate the vector field ⟦SLOT_83⟧ of a probability flow ODE, which deterministically transports samples from a noise distribution ⟦SLOT_84⟧ to a data distribution ⟦SLOT_85⟧:

**ZH** 我们的 Flow Matching 模型（Lipman et al., 2023）经训练用于近似概率流 ODE 的向量场 ⟦SLOT_83⟧，该 ODE 确定性地把样本从噪声分布 ⟦SLOT_84⟧ 传输到数据分布 ⟦SLOT_85⟧：

<!-- [原子块 · table] d ​ 𝐱 t = v t ​ ( 𝐱 t ) ​ d ​ t . d\mathbf{x}_{t}=v_{t}(\mathbf{x}_{t})dt. (2) -->

**EN** We wish to find an equivalent SDE of the general form

**ZH** 我们希望找到如下一般形式的一个等价 SDE

<!-- [原子块 · table] d ​ 𝐱 t = f ⁡ ( 𝐱 t , t ) ​ d ​ t + G ⁡ ( t ) ​ d ​ W t , d\mathbf{x}_{t}=f(\mathbf{x}_{t},t)dt+G(t)dW_{t}, (3) -->

**EN** that generates the same marginal probability density path ⟦SLOT_86⟧ for all ⟦SLOT_87⟧. Here, ⟦SLOT_88⟧ is the drift term, ⟦SLOT_89⟧ is the diffusion coefficient (we assume it is state-independent), and ⟦SLOT_90⟧ is a standard Wiener process.

**ZH** 使其对所有 ⟦SLOT_87⟧ 生成相同的边缘概率密度路径 ⟦SLOT_86⟧。其中 ⟦SLOT_88⟧ 为漂移项，⟦SLOT_89⟧ 为扩散系数（我们假定其与状态无关），⟦SLOT_90⟧ 为标准 Wiener 过程。

**EN** The evolution of the probability density ⟦SLOT_91⟧ is described by the Fokker-Planck equation (Song et al., 2021). For the deterministic ODE in equation 2, it is:

**ZH** 概率密度 ⟦SLOT_91⟧ 的演化由 Fokker-Planck 方程（Song et al., 2021）描述。对于式 2 中的确定性 ODE，其形式为：

<!-- [原子块 · table] ∂ p t ​ ( 𝐱 ) ∂ t = − ∇ ⋅ [ v t ( 𝐱 ) p t ( 𝐱 ) ] . \frac{\partial p_{t}(\mathbf{x})}{\partial t}=-\nabla\cdot\left[v_{t}(\mathbf{x})p_{t}(\mathbf{x})\right]. (4) -->

**EN** For the SDE in equation 3, the Fokker-Planck equation is:

**ZH** 对于式 3 中的 SDE，Fokker-Planck 方程为：

<!-- [原子块 · table] ∂ p t ​ ( 𝐱 ) ∂ t = − ∇ ⋅ [ f ( 𝐱 , t ) p t ( 𝐱 ) ] + 1 2 ∇ 2 [ G ( t ) 2 p t ( 𝐱 ) ] . \frac{\partial p_{t}(\mathbf{x})}{\partial t}=-\nabla\cdot\left[f(\mathbf{x},t)p_{t}(\mathbf{x})\right]+\frac{1} -->

**EN** For the two processes to be equivalent (i.e., to share the same ⟦SLOT_92⟧), the right-hand sides of equation 4 and equation 5 must be equal. This allows us to solve for the SDE drift term ⟦SLOT_93⟧:

**ZH** 为使两个过程等价（即共享相同的 ⟦SLOT_92⟧），式 4 与式 5 的右端必须相等。由此可解出 SDE 的漂移项 ⟦SLOT_93⟧：

<!-- [原子块 · table] − ∇ ⋅ [ v t p t ] \displaystyle-\nabla\cdot\left[v_{t}p_{t}\right] = − ∇ ⋅ [ f p t ] + 1 2 ∇ ⋅ [ ∇ ( G 2 p t ) ] \displaystyle=-\nabla\cdot\left[fp_{t}\right]+\frac{1}{2}\nabla\cdot\left[\nabla(G^{2}p -->

**EN** Dividing by ⟦SLOT_94⟧ and rearranging yields the expression for the drift:

**ZH** 两边除以 ⟦SLOT_94⟧ 并整理，得到漂移项的表达式：

<!-- [原子块 · table] f ( 𝐱 t , t ) = v t ( 𝐱 t ) + G ​ ( t ) 2 2 ∇ log p t ( 𝐱 t ) . f(\mathbf{x}_{t},t)=v_{t}(\mathbf{x}_{t})+\frac{G(t)^{2}}{2}\nabla\log p_{t}(\mathbf{x}_{t}). (9) -->

**EN** Substituting this back into equation 3, we obtain the equivalent SDE:

**ZH** 把它代回式 3，即得等价的 SDE：

<!-- [原子块 · table] d 𝐱 t = [ v t ( 𝐱 t ) + G ​ ( t ) 2 2 ∇ log p t ( 𝐱 t ) ] d t + G ( t ) d W t . d\mathbf{x}_{t}=\left[v_{t}(\mathbf{x}_{t})+\frac{G(t)^{2}}{2}\nabla\log p_{t}(\mathbf{x}_{t})\right]dt+G(t)dW_{t}. (10) -->

**EN** We define that noise at ⟦SLOT_95⟧ (⟦SLOT_96⟧) and ending with the data sample at ⟦SLOT_97⟧ (⟦SLOT_98⟧), so equation 10 don’t need a reverse SDE. This SDE’s drift consists of the original ODE vector field plus a term proportional to the score function, ⟦SLOT_99⟧.

**ZH** 我们定义噪声位于 ⟦SLOT_95⟧（⟦SLOT_96⟧）、数据样本位于 ⟦SLOT_97⟧（⟦SLOT_98⟧）作为终点，因此式 10 无需反向 SDE。该 SDE 的漂移由原始 ODE 向量场加上一个正比于得分函数 ⟦SLOT_99⟧ 的项构成。

**EN** F.2 Expressing the Score via the Learned Vector Field

**ZH** F.2 用学习到的向量场表示得分

**EN** The SDE in equation 10 is not yet practical for sampling, as the score function ⟦SLOT_100⟧ is unknown. However, for the specific probability path used in Flow Matching, this score can be expressed entirely in terms of the known vector field ⟦SLOT_101⟧, which is approximated by our trained model ⟦SLOT_102⟧.The derivation follows a similar approach to that for stochastic interpolants (Albergo et al., 2023).

**ZH** 式 10 中的 SDE 尚不能直接用于采样，因为得分函数 ⟦SLOT_100⟧ 未知。不过，对于 Flow Matching 所用的特定概率路径，该得分可以完全用已知的向量场 ⟦SLOT_101⟧（由训练模型 ⟦SLOT_102⟧ 近似）来表示。推导思路与随机插值（stochastic interpolants）（Albergo et al., 2023）相近。

**EN** Our derivation begins with the linear interpolation path: ⟦SLOT_103⟧, where ⟦SLOT_104⟧ and ⟦SLOT_105⟧ is a data sample. The velocity of this path is defined as the conditional expectation of the instantaneous change:

**ZH** 推导从线性插值路径 ⟦SLOT_103⟧ 出发，其中 ⟦SLOT_104⟧，⟦SLOT_105⟧ 为一个数据样本。该路径的速度定义为瞬时变化的条件期望：

<!-- [原子块 · table] v t ​ ( 𝐱 t ) = 𝔼 ⁡ [ d ​ 𝐱 t d ​ t | 𝐱 t ] . v_{t}(\mathbf{x}_{t})=\mathbb{E}\left[\frac{d\mathbf{x}_{t}}{dt}\Big|\mathbf{x}_{t}\right]. (11) -->

**EN** Since the time derivative is ⟦SLOT_106⟧, the vector field becomes:

**ZH** 由于时间导数为 ⟦SLOT_106⟧，向量场变为：

<!-- [原子块 · table] v t ​ ( 𝐱 t ) = 𝔼 ⁡ [ 𝐱 1 | 𝐱 t ] − 𝔼 ⁡ [ 𝐱 0 | 𝐱 t ] . v_{t}(\mathbf{x}_{t})=\mathbb{E}[\mathbf{x}_{1}|\mathbf{x}_{t}]-\mathbb{E}[\mathbf{x}_{0}|\mathbf{x}_{t}]. (12) -->

**EN** A key identity, derived from Tweedie’s formula in score-based modeling, connects the marginal score ⟦SLOT_107⟧ to the posterior mean of the initial noise sample ⟦SLOT_108⟧:

**ZH** 由基于得分建模中的 Tweedie 公式可导出一个关键恒等式，把边缘得分 ⟦SLOT_107⟧ 与初始噪声样本的后验均值 ⟦SLOT_108⟧ 联系起来：

<!-- [原子块 · table] ∇ log ⁡ p t ​ ( 𝐱 t ) = − 𝔼 ⁡ [ 𝐱 0 | 𝐱 t ] 1 − t . \nabla\log p_{t}(\mathbf{x}_{t})=-\frac{\mathbb{E}[\mathbf{x}_{0}|\mathbf{x}_{t}]}{1-t}. (13) -->

**EN** Our goal is thus to express ⟦SLOT_109⟧ using ⟦SLOT_110⟧. To do this, we take the conditional expectation of the path definition itself:

**ZH** 因此我们的目标是用 ⟦SLOT_110⟧ 表示 ⟦SLOT_109⟧。为此，对路径定义本身取条件期望：

<!-- [原子块 · table] 𝔼 ⁡ [ 𝐱 t | 𝐱 t ] = 𝐱 t = ( 1 − t ) ​ 𝔼 ​ [ 𝐱 0 | 𝐱 t ] + t ​ 𝔼 ​ [ 𝐱 1 | 𝐱 t ] . \mathbb{E}[\mathbf{x}_{t}|\mathbf{x}_{t}]=\mathbf{x}_{t}=(1-t)\mathbb{E}[\mathbf{x}_{0}|\mathbf{x}_{t}]+t\mathbb{E}[\m -->

**EN** We now have a system of two linear equations ( equation 12 and equation 14) with two unknowns (⟦SLOT_111⟧ and ⟦SLOT_112⟧). We can solve this system for ⟦SLOT_113⟧. Rearranging equation 12 gives ⟦SLOT_114⟧. Substituting this into equation 14:

**ZH** 于是得到一个由两个线性方程（式 12 与式 14）构成、含两个未知量（⟦SLOT_111⟧ 与 ⟦SLOT_112⟧）的方程组，可解出 ⟦SLOT_113⟧。整理式 12 得 ⟦SLOT_114⟧，代入式 14：

<!-- [原子块 · table] 𝐱 t \displaystyle\mathbf{x}_{t} = ( 1 − t ) ​ 𝔼 ​ [ 𝐱 0 | 𝐱 t ] + t ⁡ ( v t ​ ( 𝐱 t ) + 𝔼 ⁡ [ 𝐱 0 | 𝐱 t ] ) \displaystyle=(1-t)\mathbb{E}[\mathbf{x}_{0}|\mathbf{x}_{t}]+t(v_{t}(\mathbf{x}_{t})+\mathbb -->

**EN** This gives us the desired expression:

**ZH** 由此得到所需表达式：

<!-- [原子块 · table] 𝔼 ⁡ [ 𝐱 0 | 𝐱 t ] = 𝐱 t − t ​ v t ​ ( 𝐱 t ) . \mathbb{E}[\mathbf{x}_{0}|\mathbf{x}_{t}]=\mathbf{x}_{t}-tv_{t}(\mathbf{x}_{t}). (16) -->

**EN** Finally, substituting equation 16 back into the score identity ( equation 13), we arrive at the final, practical expression for the score function:

**ZH** 最后，把式 16 代回得分恒等式（式 13），得到得分函数的最终实用表达式：

<!-- [原子块 · table] ∇ log ⁡ p t ​ ( 𝐱 t ) = − 𝐱 t − t ​ v t ​ ( 𝐱 t ) 1 − t . \nabla\log p_{t}(\mathbf{x}_{t})=-\frac{\mathbf{x}_{t}-tv_{t}(\mathbf{x}_{t})}{1-t}. (17) -->

**EN** This result allows us to compute the score at any point ⟦SLOT_115⟧ using only the output of our trained vector field model ⟦SLOT_116⟧.

**ZH** 该结果使我们只需用训练好的向量场模型 ⟦SLOT_116⟧ 的输出，就能计算任意点 ⟦SLOT_115⟧ 处的得分。

**EN** F.3 Final SDE and Discretized Transition Probability

**ZH** F.3 最终 SDE 与离散化转移概率

**EN** We now substitute the practical expression for the score equation 17 into the SDE from equation 10. For simplicity, let’s assume a constant diffusion ⟦SLOT_117⟧:

**ZH** 现在把式 17 的得分实用表达式代入式 10 的 SDE。为简化，假设扩散系数为常数 ⟦SLOT_117⟧：

<!-- [原子块 · table] d ​ 𝐱 t = [ v t ​ ( 𝐱 t ) − σ 2 2 ​ 𝐱 t − t ​ v t ​ ( 𝐱 t ) 1 − t ] ​ d ​ t + σ ​ d ​ W t . d\mathbf{x}_{t}=\left[v_{t}(\mathbf{x}_{t})-\frac{\sigma^{2}}{2}\frac{\mathbf{x}_{t}-tv_{t}(\mathbf{x}_{t})} -->

**EN** This is our final SDE, where the drift is expressed entirely in terms of the learned vector field ⟦SLOT_118⟧ (approximated by ⟦SLOT_119⟧). Unlike some prior work that requires deriving a reverse-time SDE, we can directly use this forward-time SDE for model sampling.

**ZH** 这就是最终的 SDE，其漂移完全用学习到的向量场 ⟦SLOT_118⟧（由 ⟦SLOT_119⟧ 近似）表示。与某些需要推导反向时间 SDE 的前人工作不同，我们可以直接把这个前向时间 SDE 用于模型采样。

**EN** To implement this for our RL policy, we discretize equation 18 using the Euler-Maruyama scheme with a step size ⟦SLOT_120⟧:

**ZH** 为在强化学习策略中实现该式，我们用步长 ⟦SLOT_120⟧ 的 Euler-Maruyama 格式对式 18 作离散化：

<!-- [原子块 · table] 𝐱 t + Δ ​ t = 𝐱 t + [ v θ ​ ( 𝐱 t , t ) − σ 2 2 ​ 𝐱 t − t ​ v θ ​ ( 𝐱 t , t ) 1 − t ] ​ Δ ​ t + σ ​ Δ ​ t ⋅ ϵ , \mathbf{x}_{t+\Delta t}=\mathbf{x}_{t}+\left[v_{\theta}(\mathbf{x}_{t},t)-\frac{\sigma^{ -->

**EN** where ⟦SLOT_121⟧.

**ZH** 其中 ⟦SLOT_121⟧。

**EN** This defines the stochastic transition probability of our policy, ⟦SLOT_122⟧. It is a Gaussian distribution:

**ZH** 这定义了我们策略的随机转移概率 ⟦SLOT_122⟧，它是一个高斯分布：

<!-- [原子块 · table] π θ ​ ( 𝐱 t + Δ ​ t | 𝐱 t , 𝐜 ) = 𝒩 ⁡ ( 𝐱 t + Δ ​ t , 𝝁 ⁡ ( 𝐱 t , t ) , Σ ) , \pi_{\theta}(\mathbf{x}_{t+\Delta t}|\mathbf{x}_{t},\mathbf{c})=\mathcal{N}(\mathbf{x}_{t+\Delta t};\bm{\mu}(\mathbf{x}_{t -->

**EN** with mean and covariance given by:

**ZH** 其均值与协方差为：

<!-- [原子块 · table] 𝝁 ⁡ ( 𝐱 t , t ) \displaystyle\bm{\mu}(\mathbf{x}_{t},t) = 𝐱 t + [ v θ ​ ( 𝐱 t , t ) − σ 2 2 ​ 𝐱 t − t ​ v θ ​ ( 𝐱 t , t ) 1 − t ] ​ Δ ​ t \displaystyle=\mathbf{x}_{t}+\left[v_{\theta}(\mathbf{x}_{t},t -->

**EN** This completes the derivation from the deterministic ODE to a concrete, sampleable stochastic policy for reinforcement learning.

**ZH** 至此，从确定性 ODE 到可供采样的具体随机策略的推导完成。

**EN** Appendix G GRPO on SDE Flow Matching

**ZH** 附录 G SDE 流匹配上的 GRPO

**EN** With the stochastic policy ⟦SLOT_123⟧ defined by the SDE in Appendix F, we optimize our generative model using GRPO (Shao et al., 2024). GRPO is efficient online algorithm and lightweight than PPO (Schulman et al., 2017), well-suited for large generative models.

**ZH** 有了附录 F 中由 SDE 定义的随机策略 ⟦SLOT_123⟧，我们用 GRPO（Shao et al., 2024）优化生成模型。GRPO 是一种高效的在线算法，比 PPO（Schulman et al., 2017）更轻量，很适合大型生成模型。

**EN** The optimization process unfolds over trajectories generated by our SDE-based policy. For each input condition ⟦SLOT_124⟧, we generate a group of ⟦SLOT_125⟧ trajectories. Each trajectory consists of ⟦SLOT_126⟧ discrete steps, obtained by iteratively applying the Euler-Maruyama update from equation 19 to produce a final image ⟦SLOT_127⟧. Our EditScore model then assigns a terminal reward ⟦SLOT_128⟧ to each resulting image.

**ZH** 优化过程在我们基于 SDE 的策略所生成的轨迹上展开。对每个输入条件 ⟦SLOT_124⟧，生成一组 ⟦SLOT_125⟧ 条轨迹；每条轨迹由 ⟦SLOT_126⟧ 个离散步构成，通过迭代应用式 19 的 Euler-Maruyama 更新得到最终图像 ⟦SLOT_127⟧。随后由 EditScore 模型为每张结果图像赋予终止奖励 ⟦SLOT_128⟧。

**EN** The GRPO objective maximizes a clipped surrogate function over each step ⟦SLOT_129⟧ of the trajectories:

**ZH** GRPO 的目标是在轨迹的每一步 ⟦SLOT_129⟧ 上最大化一个截断的替代函数：

<!-- [原子块 · table] 𝒥 GRPO ​ ( θ ) = 𝔼 ^ t ​ [ min ⁡ ( ρ t ​ ( θ ) ​ A ^ t , clip ​ ( ρ t ​ ( θ ) , 1 − ϵ , 1 + ϵ ) ​ A ^ t ) ] , \mathcal{J}_{\text{GRPO}}(\theta)=\hat{\mathbb{E}}_{t}\left[\min\left(\rho_{t}(\theta)\hat -->

**EN** where ⟦SLOT_130⟧ is a clipping hyperparameter, and the advantage ⟦SLOT_131⟧ is computed based on the terminal rewards within the group. For the final step of the trajectory, the advantage is calculated as:

**ZH** 其中 ⟦SLOT_130⟧ 为截断超参数，优势 ⟦SLOT_131⟧ 依据组内的终止奖励计算。对轨迹的最后一步，优势计算为：

<!-- [原子块 · table] A ^ T i = r i − mean ​ ( { r 1 , … , r G } ) std ​ ( { r 1 , … , r G } ) , \hat{A}_{T}^{i}=\frac{r_{i}-\text{mean}(\{r_{1},\dots,r_{G}\})}{\text{std}(\{r_{1},\dots,r_{G}\})}, (24) -->

**EN** For intermediate timesteps (⟦SLOT_132⟧), the advantages are typically computed using Generalized Advantage Estimation (GAE).

**ZH** 对于中间时间步（⟦SLOT_132⟧），优势通常用广义优势估计（Generalized Advantage Estimation, GAE）计算。

**EN** Critically, in our SDE framework, the importance ratio ⟦SLOT_133⟧ is the ratio of the single-step state transition probabilities defined in equation 20, under the current policy ⟦SLOT_134⟧ and the old policy ⟦SLOT_135⟧ that generated the data:

**ZH** 关键的是，在我们的 SDE 框架中，重要性比 ⟦SLOT_133⟧ 是式 20 所定义的单步状态转移概率之比，分别在当前策略 ⟦SLOT_134⟧ 与生成数据的旧策略 ⟦SLOT_135⟧ 下计算：

<!-- [原子块 · table] ρ t ​ ( θ ) = π θ ​ ( 𝐱 t + Δ ​ t | 𝐱 t , 𝐜 ) π θ old ​ ( 𝐱 t + Δ ​ t | 𝐱 t , 𝐜 ) . \rho_{t}(\theta)=\frac{\pi_{\theta}(\mathbf{x}_{t+\Delta t}|\mathbf{x}_{t},\mathbf{c})}{\pi_{\theta_{\text{old}}}(\m -->

**EN** Appendix H Images categories

**ZH** 附录 H 图像类别

**EN** Figure 4 illustrates the distribution of input image categories in our editing dataset.

**ZH** 图 4 展示了我们编辑数据集中输入图像类别的分布。

<!-- [原子块 · object]  -->

**EN** Figure 4: Distribution of input image categories.

**ZH** 图 4：输入图像类别的分布。

**EN** Table 13: Benchmark results on EditReward-Bench, reporting both overall pairwise accuracy and a fine-grained breakdown across four categories of edit capabilities. Pairwise accuracy measures the proportion of pairs where the model correctly assigns a higher reward score to the human-preferred output. Notably, EditScore achieves superior performance even with its compact 7B size. Avg@4 denotes the average score over 4 forward passes.

**ZH** 表 13：EditReward-Bench 上的基准结果，同时报告总体成对准确率与四类编辑能力的细粒度分解。成对准确率衡量模型正确给人类偏好输出打出更高奖励分数的样本对占比。值得注意的是，EditScore 即便在 7B 这一紧凑规模下也取得了优越性能。Avg@4 表示 4 次前向传播的均分。

<!-- [原子块 · table] Model GPT-4.1 GPT-5 Gemini-2.5 Qwen2.5-VL EditScore-7B EditScore-32B EditScore-72B Metric Pro 7B 32B 72B Base Avg@4 Base Avg@4 Base Avg@4 Overall PF 0.654 0.750 0.697 0.493 0.490 0.624 0.615 0.735 0.6 -->

**EN** Appendix I Qualitative Results

**ZH** 附录 I 定性结果

**EN** In this section, we present qualitative results of OmniGen2 after reinforcement learning. The Figure 5 shows examples across several image editing tasks. These results validate the improvement of editing outcomes achieved by RL training on editing models.

**ZH** 本节给出 OmniGen2 经强化学习后的定性结果。图 5 展示了若干图像编辑任务上的样例，验证了在编辑模型上开展强化学习训练确实改善了编辑效果。

<!-- [原子块 · img]  -->

**EN** Figure 5: Qualitative results on image editing task.

**ZH** 图 5：图像编辑任务的定性结果。

**EN** Appendix J Data Annotation User Interface

**ZH** 附录 J 数据标注用户界面

**EN** To ensure the collection of high-quality, fine-grained preference data for EditRewardBench, we developed a specialized web-based annotation interface. This section provides a visual overview of the interface and its key features, designed to facilitate our multi-dimensional, tiered ranking protocol. The two main components of the interface are shown in Figure 6.

**ZH** 为确保为 EditRewardBench 采集到高质量、细粒度的偏好数据，我们开发了专用的网页标注界面。本节给出该界面的可视化概览及其关键特性，这些设计旨在支撑我们的多维度分层排序协议。界面的两个主要组成部分如图 6 所示。

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

**EN** Figure 6: Screenshots of our custom-built annotation interface for EditRewardBench. (Top) The upper panel presents the expert rater with the visual stimuli: the original input image and a set of five candidate edited outputs from various models. (Bottom) The lower panel contains the interactive components. It displays the user instruction (“Task Description”) and provides three separate input fields for our core evaluation dimensions: Instruction Following, Consistency, and Overall Quality. This panel clearly shows the tiered ranking mechanism, where the pipe symbol (‘⟦SLOT_136⟧’) is used to group images of similar quality.

**ZH** 图 6：我们为 EditRewardBench 自建标注界面的截图。（上）上部面板向专家评分者呈现视觉材料：原始输入图像，以及来自各模型的五张候选编辑输出。（下）下部面板包含交互组件，显示用户指令（“任务描述”），并为我们三个核心评测维度——指令遵循、一致性与总体质量——各提供一个独立输入框。该面板清晰展示了分层排序机制：用竖线符号（‘⟦SLOT_136⟧’）把质量相近的图像归为一组。

**EN** As illustrated in Figure 6, the interface presents expert raters with all necessary information for a single annotation task. The design is centered around two core principles of our methodology:

**ZH** 如图 6 所示，界面为专家评分者呈现单次标注任务所需的全部信息，其设计围绕我们方法论的两条核心原则展开：

**EN** • Multi-Dimensional Evaluation: The lower panel requires annotators to provide three independent rankings for Instruction Following, Consistency, and Overall Quality. This decomposed approach, clearly separated in the UI, ensures that each aspect of the edit is evaluated independently, preventing issues where, for example, a visually pleasing but semantically incorrect edit might be unfairly favored.

**ZH** • 多维度评测：下部面板要求标注员为指令遵循、一致性与总体质量分别给出三个独立排序。这种在 UI 上明确分离的分解式做法，确保编辑的每个方面都被独立评估，避免出现“视觉上讨喜但语义错误的编辑被不公正地偏爱”之类的问题。

**EN** • Tiered Ranking Support: A key feature of our design is the direct implementation of tiered ranking. As shown in the lower panel’s input fields, annotators are not forced into a strict linear order. Instead, they can group multiple images of perceived equal quality into the same tier using a pipe (‘⟦SLOT_137⟧’) separator. For instance, a ranking of ‘⟦SLOT_138⟧’ indicates that output 1 is in the top tier, outputs 4, 5, and 2 are tied in a middle tier, and output 3 is in the lowest tier. This method more accurately captures nuanced human judgments and allows for the efficient generation of a dense graph of preference pairs from a single annotation.

**ZH** • 分层排序支持：设计的另一个关键特性是直接实现了分层排序。如下部面板的输入框所示，标注员并不被强制给出严格线性序；他们可以用竖线（‘⟦SLOT_137⟧’）分隔符把主观质量相同的多张图像归入同一档位。例如排序 ‘⟦SLOT_138⟧’ 表示输出 1 位于最高档，输出 4、5、2 并列中间档，输出 3 位于最低档。这种方法更准确地捕捉了人类判断中的细微差别，并能从单次标注高效地生成稠密的偏好对图。

**EN** The interface also includes progress tracking and quality control features, ensuring a smooth and reliable annotation workflow for our expert raters.

**ZH** 界面还包含进度追踪与质量控制功能，确保专家评分者拥有顺畅、可靠的标注工作流程。

**EN** Appendix K Details on the Experimental Setup

**ZH** 附录 K 实验设置细节

**EN** This appendix provides detailed specifications for the training of our reward model, EditScore, and for the reinforcement learning of our policy model, OmniGen2-Edit.

**ZH** 本附录给出奖励模型 EditScore 的训练细节，以及策略模型 OmniGen2-Edit 的强化学习细节。

**EN** K.1 Reward Model Training (EditScore)

**ZH** K.1 奖励模型训练（EditScore）

**EN** Hyperparameters.

**ZH** 超参数。

**EN** Our reward models are fine-tuned from the Qwen2.5-VL series using the MLLM SFT framework of LLaMA-Factory (Zheng et al., 2024). For all model sizes, we use a consistent set of hyperparameters. We employ the AdamW optimizer with a learning rate of ⟦SLOT_139⟧ . The models are trained for 3 epochs with a maximum sequence length of 8192. We use a large effective batch size of 32, achieved with a per-device batch size of 1 and 4 gradient accumulation steps across our 32-GPU setup. To ensure efficient training, we utilize LoRA (Hu et al., 2022) with a rank (⟦SLOT_140⟧) of 32.

**ZH** 我们的奖励模型基于 Qwen2.5-VL 系列微调而成，使用 LLaMA-Factory（Zheng et al., 2024）的 MLLM SFT 框架。所有模型规模采用一致的超参数集：使用 AdamW 优化器，学习率为 ⟦SLOT_139⟧；训练 3 个 epoch，最大序列长度为 8192；有效批大小为 32（在 32 卡环境下以每卡批大小 1、梯度累积 4 步实现）。为保证训练高效，我们采用 LoRA（Hu et al., 2022），秩（⟦SLOT_140⟧）取 32。

**EN** Compute Resources.

**ZH** 计算资源。

**EN** We trained three versions of EditScore based on the 7B, 32B, and 72B variants of the Qwen2.5-VL model. All training was conducted on a high-performance cluster consisting of 4 interconnected nodes, totaling 32 NVIDIA H100 (80GB) GPUs.

**ZH** 我们基于 Qwen2.5-VL 的 7B、32B 与 72B 变体训练了三个版本的 EditScore。全部训练在一个由 4 个互连节点组成、共计 32 张 NVIDIA H100（80GB）GPU 的高性能集群上完成。

**EN** K.2 Reinforcement Learning Fine-tuning

**ZH** K.2 强化学习微调

**EN** Hyperparameters.

**ZH** 超参数。

**EN** For the online RL fine-tuning of OmniGen2-Edit, we use the GRPO algorithm. The SDE sampling process is configured with ⟦SLOT_141⟧ discrete timesteps and a diffusion coefficient ⟦SLOT_142⟧. Key GRPO hyperparameters are fixed across all experiments: in one step the global batch size is 288, the group size is ⟦SLOT_143⟧. The PPO clipping hyperparameter is ⟦SLOT_144⟧, and the learning rate is ⟦SLOT_145⟧. The KL penalty coefficient ⟦SLOT_146⟧, which regularizes the policy shift from the SFT initialization, is set to ⟦SLOT_147⟧. The policy model is also trained using LoRA with the same configuration as the reward model (⟦SLOT_148⟧).

**ZH** 对 OmniGen2-Edit 的在线强化学习微调采用 GRPO 算法。SDE 采样过程配置为 ⟦SLOT_141⟧ 个离散时间步，扩散系数为 ⟦SLOT_142⟧。GRPO 的关键超参数在所有实验中固定：每步全局批大小为 288，组大小为 ⟦SLOT_143⟧；PPO 截断超参数为 ⟦SLOT_144⟧，学习率为 ⟦SLOT_145⟧；用于约束策略相对 SFT 初始化偏移的 KL 惩罚系数 ⟦SLOT_146⟧ 设为 ⟦SLOT_147⟧。策略模型同样使用 LoRA 训练，配置与奖励模型一致（⟦SLOT_148⟧）。

**EN** Compute Resources.

**ZH** 计算资源。

**EN** The online RL fine-tuning phase, which involves iterative sampling from the policy model and subsequent updates, was performed on a cluster of 32 NVIDIA H100 (80GB) GPUs.

**ZH** 在线强化学习微调阶段需要在策略模型上迭代采样并作后续更新，在 32 张 NVIDIA H100（80GB）GPU 的集群上完成。

**EN** Appendix L Limitations

**ZH** 附录 L 局限性

**EN** While EditScore demonstrates robust performance across a wide range of editing scenarios, a granular analysis reveals specific limitations. Table 14 presents a detailed breakdown of pairwise accuracy across all 13 subtasks. We observe that while EditScore performs exceptionally well on objective tasks—such as Subject Removal and Text Modification—performance drops noticeably in the Advanced category. Specifically, highly subjective tasks like Portrait Beautification (Beaut) and complex compositional tasks like Hybrid Edit (Hyb) prove to be the most challenging. For instance, the baseline EditScore-7B achieves only 0.284 accuracy on Beaut and 0.519 on Hyb. However, it is worth noting that our self-ensemble strategy (Avg@4) significantly mitigates these weaknesses, boosting the accuracy on Beaut to 0.569 and Hyb to 0.571, demonstrating that the model possesses the latent knowledge to evaluate these tasks but requires multiple reasoning paths to reduce variance.

**ZH** EditScore 虽在广泛的编辑场景中表现稳健，细粒度分析仍揭示出若干具体局限。表 14 给出全部 13 个子任务上成对准确率的详细分解。我们观察到，EditScore 在主体移除、文字修改等客观任务上表现优异，但在高级（Advanced）类别中性能明显下滑。具体而言，人物美化（Beaut）这类高度主观的任务与组合编辑（Hyb）这类复杂组合任务最为棘手：基线 EditScore-7B 在 Beaut 上仅取得 0.284 的准确率，在 Hyb 上为 0.519。不过值得注意的是，我们的自集成策略（Avg@4）显著缓解了这些弱点，把 Beaut 的准确率提升至 0.569、Hyb 提升至 0.571，说明模型已具备评测这些任务的潜在知识，只是需要多条推理路径来降低方差。

**EN** Figure 7 further visualizes two representative failure cases that highlight these challenges.

**ZH** 图 7 进一步可视化了两个代表性失败案例，凸显上述挑战。

**EN** • The left case illustrates the difficulty of handling abstract and subjective instructions. Given the prompt “Make the man handsome,” the output image applies a subtle smoothing effect to the skin. However, EditScore fails to perceive this nuanced improvement, penalizing the edit with a Semantic Consistency (SC) score of 0/25 by stating “no visible difference.” This suggests that EditScore may be overly conservative or lack the fine-grained visual acuity required to detect subtle aesthetic enhancements.

**ZH** • 左侧案例说明了处理抽象、主观指令的困难。给定提示“让这个男人更帅”，输出图像对皮肤施加了细微的磨皮效果，但 EditScore 未能察觉这一细微改善，以“无明显差异”为由给出 0/25 的语义一致性（SC）分数并施以惩罚。这表明 EditScore 可能过于保守，或缺少察觉细微美学改善所需的精细视觉敏锐度。

**EN** • The right case demonstrates the limitations in processing compositional instructions. The prompt requires two distinct actions: removing the radiator and changing the cat’s color to brown. While the model successfully identifies the removal of the radiator, it fails to recognize that the second constraint was not met—the cat appears with severe orange artifacts rather than a natural brown. EditScore grants a high score (22/25), indicating a tendency to “over-reward” partial success in complex chains of thought, failing to strictly penalize the unfulfilled portion of the instruction.

**ZH** • 右侧案例展示了处理组合指令时的局限。该提示要求两个不同的动作：移除暖气片，并把猫的颜色改为棕色。模型虽成功识别出暖气片已被移除，却未能发现第二个约束没有满足——猫身上出现了严重的橙色伪影，而非自然的棕色。EditScore 给出了高分（22/25），说明在复杂思维链中存在“过度奖励部分成功”的倾向，未能严格惩罚指令中未落实的部分。

**EN** We attribute these failure modes to two primary factors. First, the inherent capability of the base VLM: even state-of-the-art VLMs struggle with high-resolution, pixel-level discernibility (needed for beautification). Second, the data distribution: the training data for subjective tasks like beautification naturally contains higher human disagreement, making it difficult for the reward model to learn a sharp decision boundary. Furthermore, complex compositional samples are less frequent in current datasets compared to simple single-step edits. Addressing these limitations through the curation of more granular, multi-step instruction data and leveraging stronger base models remains a critical direction for our future work.

**ZH** 我们把这些失败模式归结为两个主要因素。其一，基座 VLM 的固有能力：即便是最先进的 VLM，在高分辨率、像素级辨别力（人物美化所需）上依然吃力。其二，数据分布：人物美化等主观任务的训练数据天然包含更高的人类分歧，奖励模型难以学到清晰的决策边界；此外，复杂的组合式样本在当前数据集中的出现频率低于简单的单步编辑。通过策管更细粒度的多步指令数据、并借助更强的基座模型来克服这些局限，是我们未来工作的关键方向。

**EN** Table 14: Detailed of EditScore across 13 distinct editing subtasks on EditReward-Bench. While EditScore performs robustly on objective tasks (e.g., Subject Removal, Text Change), it exhibits limitations in highly subjective tasks like Portrait Beautification (Beaut) and complex compositional tasks like Hybrid Edit (Hyb). Abbreviations: Add: Subject Addition, Rmv: Removal, Rep: Replace; Col: Color Alt., Mat: Material Mod., Sty: Style Transfer, Tone: Tone Trans.; BG: Background Change, Ext: Extract; Beaut: Portrait Beautification (ps_human), Text: Text Mod., Mot: Motion Change, Hyb: Hybrid Edit (compose).

**ZH** 表 14：EditScore 在 EditReward-Bench 上 13 个不同编辑子任务中的详细表现。EditScore 在客观任务（如主体移除、文字更改）上表现稳健，但在人物美化（Beaut）等高度主观的任务与组合编辑（Hyb）等复杂组合任务上存在局限。缩写：Add：主体添加，Rmv：移除，Rep：替换；Col：颜色更改，Mat：材质修改，Sty：风格迁移，Tone：色调变换；BG：背景替换，Ext：主体提取；Beaut：人物美化（ps_human），Text：文字修改，Mot：动作变化，Hyb：组合编辑（合成）。

<!-- [原子块 · table] Model Subject Appearance Scene Advanced Avg. Add Rmv Rep Col Mat Sty Tone BG Ext Beaut Text Mot Hyb EditScore-7B (Base) 0.681 0.810 0.729 0.700 0.570 0.658 0.724 0.718 0.860 0.284 0.736 0.578 0.519 0. -->

<!-- [原子块 · img]  -->

**EN** Figure 7: Failure Analysis. Visualization of two representative failure cases. Left: In subjective tasks like Portrait Beautification, EditScore may be overly conservative, failing to detect subtle improvements (e.g., skin smoothing) and assigning a score of 0. Right: In complex Hybrid Edit tasks, EditScore tends to over-reward partial success, correctly identifying the object removal but failing to penalize the incorrect color change.

**ZH** 图 7：失败分析。两个代表性失败案例的可视化。左：在人物美化等主观任务中，EditScore 可能过于保守，无法察觉细微改善（如皮肤磨皮），因而给出 0 分。右：在复杂的组合编辑任务中，EditScore 倾向于过度奖励部分成功——正确识别出物体已被移除，却未能惩罚错误的颜色更改。

**EN** Appendix M VLM Evaluation Prompts

**ZH** 附录 M VLM 评测提示词

**EN** This appendix provides the complete structure and text of the prompts used for the zero-shot evaluation of Vision-Language Models (VLMs) on our EditRewardBench. Our prompt is based on VIEScore prompts (Ku et al., 2024), which designs a “reasoning-first” and score range changed in 0-25.

**ZH** 本附录给出在 EditRewardBench 上对视觉语言模型（VLM）作零样本评测所用提示词的完整结构与文本。我们的提示词基于 VIEScore 提示词（Ku et al., 2024），其设计为“推理优先”，并把分数区间改为 0–25。

**EN** M.1 Base Context and Output Format

**ZH** M.1 基础上下文与输出格式

**EN** All evaluation prompts are prefixed with a base context that establishes the VLM’s persona as a “professional digital artist” and, most importantly, specifies the required JSON output format. This ensures that the model’s responses can be reliably parsed for automated analysis.

**ZH** 所有评测提示词都以一段基础上下文开头，用以确立 VLM 作为“专业数字艺术家”的角色；更重要的是，它规定了所需的 JSON 输出格式，从而保证模型的回答可被可靠解析以作自动分析。

**EN** Listing 1: The base context prompt, defining the persona and mandatory JSON output structure.

**ZH** 清单 1：基础上下文提示词，定义角色与强制的 JSON 输出结构。

**EN** M.2 Semantic Conformity (SC) Prompt

**ZH** M.2 语义一致性（SC）提示词

**EN** The SC prompt is composed of two parts. First, a set of general rules explains the two-image comparison task. Second, a specific rubric details how to score “editing success” and “degree of overediting”.

**ZH** SC 提示词由两部分组成：其一是一组通用规则，说明双图比较任务；其二是具体评分细则，详述如何为“编辑成功程度”与“过度编辑程度”打分。

**EN** Listing 2: General rules for the two-image editing evaluation task.

**ZH** 清单 2：双图编辑评测任务的通用规则。

**EN** Listing 3: Specific scoring rubric for Semantic Conformity (SC).

**ZH** 清单 3：语义一致性（SC）的具体评分细则。

**EN** M.3 Perceptual Quality (PQ) Prompt

**ZH** M.3 感知质量（PQ）提示词

**EN** The PQ prompt is self-contained, providing both the general rules for single-image quality assessment and the specific rubric for scoring “naturalness” and “artifacts”.

**ZH** PQ 提示词自成一体，既提供单图质量评估的通用规则，也提供为“自然度”与“伪影”打分的具体细则。

**EN** Listing 4: Rules and scoring rubric for Perceptual Quality (PQ).

**ZH** 清单 4：感知质量（PQ）的规则与评分细则。

**EN** The final prompts sent to the VLM are constructed by concatenating the base context (Listing 1) with the respective rule and rubric sets for the SC (Listings 2 and 3) and PQ (Listing 4) evaluations. This modular design allows for clear and targeted assessment of each evaluation dimension.

**ZH** 最终发送给 VLM 的提示词由基础上下文（清单 1）与 SC（清单 2、3）和 PQ（清单 4）各自的规则与细则集拼接而成。这种模块化设计使每个评测维度都能得到清晰而有针对性的评估。
