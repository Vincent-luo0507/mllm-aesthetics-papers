# Multimodal RewardBench 2：面向图文交错的全模态奖励模型评测

> 原标题：Multimodal RewardBench 2: Evaluating Omni Reward Models for Interleaved Text and Image
> 作者：Yushi Hu, Reyhane Askari-Hemmat, Melissa Hall, Emily Dinan, Luke Zettlemoyer, Marjan Ghazvininejad · arXiv:2512.16899 · 2025-12-18

<!-- [原子块 · verbatim] Multimodal RewardBench 2: Evaluating Omni Reward Models for Interleaved Text and Image -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] Reward models (RMs) are essential for training large language models (LLMs), but remain underexplored for omni models that handle interleaved image and text sequences. We introduce Multimodal RewardBe -->

**EN** 1 Introduction

**ZH** 1 引言

<!-- [原子块 · img]  -->

**EN** Figure 1: Examples of multimodal preference pairs in MMRB2 across four subtasks: text-to-image generation, interleaved generation, image editing, and multimodal reasoning, showing human and model judgments on challenging prompts.

**ZH** 图 1：MMRB2 中四个子任务的图文偏好对示例，分别为文生图生成、交错生成、图像编辑与多模态推理，展示了人类与模型在挑战性提示词上的判断结果。

**EN** Reward models are central to the development of LLMs (Christiano et al., 2017; Bai et al., 2022; Jaech et al., 2024; Guo et al., 2025; Lambert et al., 2024; Yuan et al., 2024). They enable scalable evaluation that tracks model performance and surfaces systematic weaknesses (Zheng et al., 2023). They can be used to assess data quality, which is crucial for building synthetic data pipelines (Wang et al., 2022b). And, as reinforcement learning becomes increasingly important in post training, high quality reward models are crucial for surfacing or suppressing a range of different model capabilities (Christiano et al., 2017; Wu et al., 2023c; Guo et al., 2025). Recent work has focused on developing new classes of omni models, which enable understanding, generation, and reasoning with interleaved text and images (OpenAI, 2024; Chameleon Team, 2024; Ge et al., 2025; Zhou et al., 2024; Deng et al., 2025; Chen et al., 2025c; Wang et al., 2024b; Chen et al., 2025a; Google DeepMind, 2025a). However, reward modeling for omni models remains largely unexplored.

**ZH** 奖励模型是大语言模型研发的核心环节（Christiano et al., 2017; Bai et al., 2022; Jaech et al., 2024; Guo et al., 2025; Lambert et al., 2024; Yuan et al., 2024）。它支撑着可扩展的评测，既能跟踪模型表现，也能暴露系统性短板（Zheng et al., 2023）；可用于评估数据质量，这对构建合成数据流水线至关重要（Wang et al., 2022b）；而随着强化学习在后训练阶段的重要性不断上升，高质量奖励模型更是凸显或抑制各类模型能力的关键（Christiano et al., 2017; Wu et al., 2023c; Guo et al., 2025）。近期研究转向开发新型全模态模型，使之能够以交错图文序列完成理解、生成与推理（OpenAI, 2024; Chameleon Team, 2024; Ge et al., 2025; Zhou et al., 2024; Deng et al., 2025; Chen et al., 2025c; Wang et al., 2024b; Chen et al., 2025a; Google DeepMind, 2025a）。然而，面向全模态模型的奖励建模仍基本空白。

**EN** This omission is at least in part because there is no existing benchmark for omni reward models, making it nearly impossible to measure model quality. Unlike text-only models, omni models can generate and understand any number of texts and images together in a single arbitrarily ordered sequence. This generality creates unique challenges for reward modeling. Unlike domains such as math or coding, images are difficult to verify automatically (Hessel et al., 2021; Hu et al., 2023; Lin et al., 2024), and high-quality preference data requires carefully designed annotation protocols (Liang et al., 2024). Omni models can also be used for a very broad range of real-world applications, demanding diverse task coverage for both training and evaluation (Liu et al., 2024; Chen et al., 2024; Yao et al., 2025). Finally, gathering high-quality responses needed to train and evaluate omni reward models can be challenging, since omni model capabilities are not always as strong as the models used to develop previous text-only reward benches.

**ZH** 这一空白至少部分源于缺乏面向全模态奖励模型的评测基准，导致模型质量几乎无从度量。与纯文本模型不同，全模态模型可在单条任意排序的序列中生成并理解任意数量的文本与图像。这种通用性给奖励建模带来了独有的困难：不同于数学或代码等领域，图像难以自动验证（Hessel et al., 2021; Hu et al., 2023; Lin et al., 2024），高质量偏好数据依赖精心设计的标注规程（Liang et al., 2024）；全模态模型又覆盖极为广泛的真实应用，要求训练与评测都具备多样的任务覆盖（Liu et al., 2024; Chen et al., 2024; Yao et al., 2025）；此外，训练和评测全模态奖励模型所需的高质量响应本身就难以获取，因为全模态模型的能力未必达到此前构建纯文本奖励基准时所用模型的水平。

**EN** We introduce Multimodal RewardBench 2 (MMRB2) which overcomes all of these challenges to establish a foundation for future research on omni reward modeling. MMRB2 follows Multimodal RewardBench (MMRB1) (Yasunaga et al., 2025), which covered image-text-to-text tasks for multimodal large language models (MLLMs). MMRB2 instead covers the much more challenging case of omni models over four subtasks (Figure 1): text-to-image, image editing, interleaved generation, and multimodal reasoning (“thinking with images” (OpenAI, 2025d)). Each subtask contains 1,000 expert-annotated preference pairs, consisting of a task prompt, a preferred response, and a rejected response. To ensure that MMRB2 is comprehensive, reliable, and highly predictive of reward model quality, we design it with three key characteristics: (1) diverse, practical, yet challenging prompts near the capability boundary of frontier models, drawn from 21 existing and newly created tasks; (2) responses generated by state-of-the-art multimodal models, ranging from SD3.5 (Stability AI, 2024) to GPT-Image (OpenAI, 2025c) and Gemini 2.5 Flash Image (Google DeepMind, 2025a), along with specialized agents (Hu et al., 2024) for interleaved generation and visual reasoning tasks where even the best models often fail; and (3) preference pairs that have ¿90% agreement among human experts but which remain challenging for current judges (both MLLM-based judges and trained reward models), curated via an ensemble filtering strategy. A summary of all the prompts and multimodal models covered in MMRB2 are in Table 1.

**ZH** 我们提出 Multimodal RewardBench 2（MMRB2），逐一化解上述难题，为后续的全模态奖励建模研究奠定基础。MMRB2 沿承 Multimodal RewardBench（MMRB1）（Yasunaga et al., 2025）——后者面向多模态大语言模型（MLLM），仅覆盖图文到文本任务；MMRB2 则针对难度高得多的全模态模型，覆盖四个子任务（图 1）：文生图、图像编辑、交错生成与多模态推理（“用图像思考”（OpenAI, 2025d））。每个子任务含 1000 组专家标注的偏好对，由任务提示词、优选响应与淘汰响应构成。为保证 MMRB2 的全面性、可靠性以及对奖励模型质量的高预测力，我们在设计时贯彻三项要点：（1）提示词多样、实用且具挑战性，贴近前沿模型的能力边界，取自 21 个既有与新建任务；（2）响应由最先进的多模态模型生成，涵盖 SD3.5（Stability AI, 2024）、GPT-Image（OpenAI, 2025c）、Gemini 2.5 Flash Image（Google DeepMind, 2025a）等，并为交错生成与视觉推理任务引入专用智能体（Hu et al., 2024）——即便最强模型在这些任务上也常失败；（3）偏好对在人类专家中一致率超过 90%，同时对当前评判器（含基于 MLLM 的评判器与训练所得奖励模型）仍具挑战性，通过集成过滤策略筛选得到。MMRB2 所涉及的全部提示词与多模态模型汇总于表 1。

**EN** Category Source Response Models Task Description Text-to-Image WISE (Niu et al., 2025) EvalMuse (Han et al., 2024) OneIG-Bench (Chang et al., 2025) R2IBench (Chen et al., 2025b) RealUnify (Shi et al., 2025) Image Gemini 2.0 and 2.5 Flash Image (Google DeepMind, 2025c; Google DeepMind, 2025a) Imagen 3 (Baldridge et al., 2024) Imagen 4 and Ultra (Google DeepMind, 2025d) FLUX (Labs et al., 2025) GPT-image-1 (OpenAI, 2025c) SD 3.5-L (Stability AI, 2024) Image generation from text assessing creativity, composition, reasoning, text rendering, etc. Image Editing DreamBench (Peng et al., 2025) Emu-Edit (Sheynin et al., 2024) HQ-Edit (Hui et al., 2024) RISE-Bench (Zhao et al., 2025) Text-heavy edit Multi-Image edit Image Gemini-2.0 and 2.5 Flash Image (Google DeepMind, 2025c; Google DeepMind, 2025a) Imagen3-Edit (Baldridge et al., 2024) FLUX-Kontext (Labs et al., 2025) GPT-image-1 (OpenAI, 2025c) Object replacement, scene modification, style change, entity-preserving editing, reasoning-heavy editing, text-heavy editing, multi-image editing, etc. Interleaved Generation Chameleon (Chameleon Team, 2024) Interleaved-Eval (Liu et al., 2024) ISG-Bench (Chen et al., 2024) MMMG (Yao et al., 2025) Text+Image Gemini 2.0 and 2.5 Flash Image (Google DeepMind, 2025c; Google DeepMind, 2025a) Agents: GPT-Gemini-agent GPT-GPT-image-agent GPT-Imagen-agent GPT-FLUX-agent Interleaved text-image generation, storytelling, open-ended visual question answering, scene composition, 3D prediction, temporal prediction, etc. Reasoning BLINK (Fu et al., 2024) MindCube (Yin et al., 2025) VisuLogic (Xu et al., 2025) V∗ (Wu and Xie, 2023) MuirBench (Wang et al., 2024a) RealUnify (Shi et al., 2025) Text(+Image) GPT-5 (OpenAI, 2025b) GPT-4.1 (OpenAI, 2025a) GPT-4o (OpenAI, 2024) o3 (OpenAI, 2025d) Gemini 2.5 Flash (Gemini Team, 2025) Gemini 2.5 Pro (Gemini Team, 2025) Sketchpad Agents (Hu et al., 2024): o3-sketchpad-agent GPT-5-sketchpad-agent Thinking with images, spatial reasoning, multi-image reasoning, perception-heavy tasks, etc.

**ZH** 类别 来源 响应模型 任务描述 文生图 WISE (Niu et al., 2025) EvalMuse (Han et al., 2024) OneIG-Bench (Chang et al., 2025) R2IBench (Chen et al., 2025b) RealUnify (Shi et al., 2025) 图像 Gemini 2.0 与 2.5 Flash Image (Google DeepMind, 2025c; Google DeepMind, 2025a) Imagen 3 (Baldridge et al., 2024) Imagen 4 与 Ultra (Google DeepMind, 2025d) FLUX (Labs et al., 2025) GPT-image-1 (OpenAI, 2025c) SD 3.5-L (Stability AI, 2024) 由文本生成图像，考察创意、构图、推理、文字渲染等。 图像编辑 DreamBench (Peng et al., 2025) Emu-Edit (Sheynin et al., 2024) HQ-Edit (Hui et al., 2024) RISE-Bench (Zhao et al., 2025) 文本密集编辑 多图编辑 图像 Gemini-2.0 与 2.5 Flash Image (Google DeepMind, 2025c; Google DeepMind, 2025a) Imagen3-Edit (Baldridge et al., 2024) FLUX-Kontext (Labs et al., 2025) GPT-image-1 (OpenAI, 2025c) 物体替换、场景修改、风格变换、实体保持编辑、重推理编辑、文本密集编辑、多图编辑等。 交错生成 Chameleon (Chameleon Team, 2024) Interleaved-Eval (Liu et al., 2024) ISG-Bench (Chen et al., 2024) MMMG (Yao et al., 2025) 文本+图像 Gemini 2.0 与 2.5 Flash Image (Google DeepMind, 2025c; Google DeepMind, 2025a) 智能体：GPT-Gemini-agent GPT-GPT-image-agent GPT-Imagen-agent GPT-FLUX-agent 图文交错生成、故事叙述、开放式视觉问答、场景构图、三维预测、时序预测等。 推理 BLINK (Fu et al., 2024) MindCube (Yin et al., 2025) VisuLogic (Xu et al., 2025) V∗ (Wu and Xie, 2023) MuirBench (Wang et al., 2024a) RealUnify (Shi et al., 2025) 文本（+图像） GPT-5 (OpenAI, 2025b) GPT-4.1 (OpenAI, 2025a) GPT-4o (OpenAI, 2024) o3 (OpenAI, 2025d) Gemini 2.5 Flash (Gemini Team, 2025) Gemini 2.5 Pro (Gemini Team, 2025) Sketchpad 智能体 (Hu et al., 2024)：o3-sketchpad-agent GPT-5-sketchpad-agent 用图像思考、空间推理、多图推理、重感知任务等。

**EN** Table 1: Overview of the four subtask categories in MMRB2, including their prompt sources, response modalities, model that were used to synthesize the data, and task descriptions. The benchmark draws from a diverse set of public and newly created datasets to cover text-to-image generation, image editing, interleaved text–image generation, and multimodal reasoning (”thinking with images”).

**ZH** 表 1：MMRB2 四类子任务总览，包括提示词来源、响应模态、用于合成数据的模型以及任务描述。该基准汇集了多种公开数据集与新建数据集，覆盖文生图生成、图像编辑、图文交错生成与多模态推理（“用图像思考”）。

**EN** Using MMRB2, we conduct a comprehensive study of reward models for multimodal understanding and generation, including multimodal LLM-as-a-judge, task-specific metrics, and reward models trained with human preferences. Experiments show that:

**ZH** 借助 MMRB2，我们系统研究了面向多模态理解与生成的各类奖励模型，包括以多模态大模型充当评判器、任务专用指标，以及基于人类偏好训练得到的奖励模型。实验表明：

**EN** • MMRB2 poses significant challenges to current MLLM-as-a-judge approaches: the latest Gemini 3 Pro (Google DeepMind, 2025b) reaches 74-80% accuracy across all subtasks. GPT-5 (OpenAI, 2025b) and Gemini 2.5 Pro (Gemini Team, 2025) achieve only moderate performance (66-75% accuracy across all subtasks) compared to ¿90% for humans. The best open-source model, Qwen3-VL-32B (Qwen Team, 2025), achieves 55%-69% accuracy. Notably, GPT-4o (OpenAI, 2024), which is commonly used as an evaluator in existing benchmarks, attains only 51-65% accuracy, suggesting that it is no longer suitable for evaluating frontier multimodal models, especially on reasoning-heavy tasks.

**ZH** • MMRB2 对当前基于 MLLM 的评判器构成显著挑战：最新的 Gemini 3 Pro（Google DeepMind, 2025b）在各子任务上的准确率为 74–80%；GPT-5（OpenAI, 2025b）与 Gemini 2.5 Pro（Gemini Team, 2025）仅取得中等表现（各子任务 66–75%），而人类超过 90%；最优开源模型 Qwen3-VL-32B（Qwen Team, 2025）准确率为 55%–69%。值得注意的是，在既有基准中常备用作评测器的 GPT-4o（OpenAI, 2024）准确率仅有 51–65%，说明它已不再适用于评测前沿多模态模型，尤其在重推理任务上。

**EN** • We study task-specific metrics (e.g., VQAScore (Lin et al., 2024)) and reward models trained on human preferences (e.g., ImageReward (Xu et al., 2023), UnifiedReward (Wang et al., 2025b)), and find that they are no longer reliable on the challenging prompts and frontier models in MMRB2. For instance, VQAScore (with Qwen2.5-VL backbone) and ImageReward achieve 58.3% and 54.0% on text-to-image evaluation, respectively, well below MLLM-as-a-judge baselines such as Qwen3-VL-32B (64.1%) and Gemini 3 Pro (74.4%). While human preference training improves performance over heuristic metrics, these models still fall short of frontier MLLMs.

**ZH** • 我们考察了任务专用指标（如 VQAScore（Lin et al., 2024））与基于人类偏好训练的奖励模型（如 ImageReward（Xu et al., 2023）、UnifiedReward（Wang et al., 2025b）），发现二者在 MMRB2 的挑战性提示词与前沿模型面前已不再可靠。例如，VQAScore（以 Qwen2.5-VL 为骨干）与 ImageReward 在文生图评测上分别仅为 58.3% 与 54.0%，明显低于 Qwen3-VL-32B（64.1%）与 Gemini 3 Pro（74.4%）等基于 MLLM 的评判器基线。尽管人类偏好训练使其优于启发式指标，这些模型仍不及前沿 MLLM。

**EN** • We show that performance on MMRB2 strongly correlates with performance on GenAI-Bench (Li et al., 2024), GEdit-Bench (Liu et al., 2025), ISGBench (Chen et al., 2024), and EMMA (Hao et al., 2025) when using different reward models for best-of-⟦SLOT_0⟧ selection, suggesting that MMRB2 is a good proxy for downstream effectiveness.

**ZH** • 当把不同奖励模型用于 Best-of-⟦SLOT_0⟧ 选择时，MMRB2 上的表现与 GenAI-Bench（Li et al., 2024）、GEdit-Bench（Liu et al., 2025）、ISGBench（Chen et al., 2024）和 EMMA（Hao et al., 2025）上的下游表现强相关，说明 MMRB2 能够很好地代理下游有效性。

**EN** • Further analysis of test-time scaling and fine-grained error patterns reveals substantial remaining headroom for omni model reward modeling and highlights concrete failure modes that future methods should address. Judges show notably higher agreement with human preferences on different-model pairs than on same-model pairs, with differences of up to 12%. Moreover, in multimodal reasoning tasks, judges exhibit a strong bias toward responses that include images, with performance gaps of 27.7–49.3% between pairs where annotators preferred image-containing responses and those where the preferred response contained only text.

**ZH** • 对测试时扩展与细粒度错误模式的进一步分析表明，全模态奖励建模仍有巨大提升空间，并揭示了后续方法应当解决的若干具体失效形态。评判器在跨模型对比上与人类偏好的一致率明显高于同源模型对比，差距最高达 12%。此外，在多模态推理任务中，评判器对含图像的响应表现出强烈偏好：标注者偏好含图像响应与偏好纯文本响应的两类样本之间，性能差距达 27.7–49.3%。

**EN** Overall, MMRB2 establishes a challenging and informative benchmark that we hope will serve as a foundation for future research on omni model reward modeling, evaluation, and post-training.

**ZH** 总体而言，MMRB2 建立了一个兼具挑战性与信息量的基准，期望成为全模态奖励建模、评测与后训练研究的基石。

**EN** 2 Related Work

**ZH** 2 相关工作

**EN** Reward modeling for visual generation. Building on RLHF, reward modeling has been extended beyond text. ImageReward (Xu et al., 2023), HPSv2 and v3 (Wu et al., 2023b; Ma et al., 2025), PickScore (Kirstain et al., 2023) learn human preferences for text-to-image generation, improving correlation with human judgments and guiding diffusion models beyond CLIP-based proxies. For image editing, EditScore (Luo et al., 2025) and EditReward (Wu et al., 2025) adopt similar preference-learning frameworks. Unified approaches aim for cross-task generalization: Wang et al. (2025b) train a single multimodal reward across image, video, and understanding tasks. Despite progress, most multimodal RMs remain task-specific and lack a unified, stress-testing evaluation.

**ZH** 面向视觉生成的奖励建模。在 RLHF 的基础上，奖励建模已扩展到文本之外。ImageReward（Xu et al., 2023）、HPSv2 与 v3（Wu et al., 2023b; Ma et al., 2025）、PickScore（Kirstain et al., 2023）学习文生图生成中的人类偏好，提升了与人类判断的相关性，并把扩散模型的优化导向超越 CLIP 代理指标的方向。在图像编辑方面，EditScore（Luo et al., 2025）与 EditReward（Wu et al., 2025）采用了类似的偏好学习框架。统一化方法追求跨任务泛化：Wang et al.（2025b）在图像、视频与理解任务上训练单一的多模态奖励模型。尽管进展可观，多数多模态奖励模型仍局限于特定任务，缺乏统一的压力测试式评测。

**EN** Evaluating reward models. Benchmarking reward models has become an active research direction. In the text domain, RewardBench and RewardBench 2 (Lambert et al., 2025; Malik et al., 2025) systematically compare LLM reward functions across diverse axes (e.g., instruction following, reasoning, safety). VL-RewardBench (Li et al., 2025) and Multimodal RewardBench (Yasunaga et al., 2025) assess reward models for multimodal LLM. Llava-Critic series (Xiong et al., 2025; Wang et al., 2025a) focus on developing reward models for these reward benchmarks. EvalPlanner (Saha et al., 2025) and J1 (Whitehouse et al., 2025) further improve reward modeling by incentivizing test-time scaling in LLM-as-a-judge. However, existing benchmarks and judge training efforts still largely focus on image-text-to-text tasks. For image generation, researchers develop automatic evaluation metrics for text-to-image generation. CLIPScore (Hessel et al., 2021) offers a reference-free image–text similarity measure that correlates with human judgments but often misses compositional errors; TIFA (Hu et al., 2023), DSG (Cho et al., 2024), and VQAScore (Lin et al., 2024) address this by probing alignment via VQA, improving robustness on compositional cases. OmniVerifier (Zhang et al., 2025) further investigate on training better visual-outcome verification mdiirhtdkltrnlldrnvhbccugtflukgivodels. The human annotations collected in these works are often used as reward model evaluations. Most existing reward model evaluations focus either on text or text-to-image generation, offering little insight into interleaved text and image. To bridge this gap, Multimodal RewardBench 2 (MMRB2) provides a unified and challenging framework for assess reward modeling for omni models.

**ZH** 奖励模型评测。为奖励模型建立基准已成为活跃的研究方向。在文本领域，RewardBench 与 RewardBench 2（Lambert et al., 2025; Malik et al., 2025）沿多个维度（如指令遵循、推理、安全性）系统比较了各类大语言模型奖励函数。VL-RewardBench（Li et al., 2025）与 Multimodal RewardBench（Yasunaga et al., 2025）面向多模态大语言模型评估奖励模型；Llava-Critic 系列（Xiong et al., 2025; Wang et al., 2025a）专注于为这些奖励基准训练奖励模型。EvalPlanner（Saha et al., 2025）与 J1（Whitehouse et al., 2025）通过激励测试时扩展，进一步改进了“以大语言模型充当评判器”的奖励建模。然而，既有基准与评判器训练工作仍主要聚焦图文到文本任务。在图像生成方面，研究者为文生图定制了自动评测指标：CLIPScore（Hessel et al., 2021）提供无需参考图的图文相似度度量，与人类判断相关，但常遗漏组合性错误；TIFA（Hu et al., 2023）、DSG（Cho et al., 2024）与 VQAScore（Lin et al., 2024）借助视觉问答探测对齐关系，提升了组合场景下的稳健性。OmniVerifier（Zhang et al., 2025）进一步探索训练更优的视觉结果验证 mdiirhtdkltrnlldrnvhbccugtflukgivodels。这些工作收集的人类标注常被用于奖励模型评测。现有的奖励模型评测大多聚焦文本或文生图生成，对图文交错场景关注甚少。为弥补这一缺口，Multimodal RewardBench 2（MMRB2）提供了一个统一且具挑战性的框架，用于评估全模态模型的奖励建模能力。

**EN** 3 Multimodal RewardBench 2

**ZH** 3 Multimodal RewardBench 2

**EN** MMRB2 (Figure 3) is a comprehensive omni reward model evaluation benchmark spanning a range of tasks (§3.1) of four types: text-to-image generation, image editing, interleaved generation, and multimodal reasoning. Each datapoint in MMRB2 contains a task prompt (§3.2) and two model responses, chosen and rejected (§3.3). Reward models are evaluated based on their agreement with human annotators (§3.4).

**ZH** MMRB2（图 3）是一个面向全模态奖励模型的综合评测基准，覆盖四类任务（§3.1）：文生图生成、图像编辑、交错生成与多模态推理。MMRB2 中每条数据包含一个任务提示词（§3.2）与两条模型响应，即被选中的与被拒绝的（§3.3）。奖励模型依据其与人类标注者的一致程度接受评测（§3.4）。

**EN** 3.1 Tasks in MMRB2

**ZH** 3.1 MMRB2 中的任务

<!-- [原子块 · object]  -->

**EN** Figure 2: Breakdown of MMRB2 by task type and source, and detailed categories under each task.

**ZH** 图 2：MMRB2 按任务类型与来源的构成拆解，以及各任务下的细分类别。

**EN** Task 1. Text-to-Image. Text-to-image generation provides natural language prompts for which generators produce candidate images. Reward models see the prompt and the candidate images, and must prefer the human-preferred image based on factors such as object composition, spatial relationships, attribute binding, text rendering, and adherence to complex multi-object instructions.

**ZH** 任务 1. 文生图。文生图任务给出自然语言提示词，由生成器产出候选图像。评判器接收提示词与候选图像，需依据物体组合、空间关系、属性绑定、文字渲染以及对复杂多物体指令的遵循程度等因素，选出人类更偏好的图像。

**EN** Task 2. Image Editing. Image editing provides 1-3 input images and a textual edit instruction, along with candidate edited images from generators. Reward models must select the edit that best matches human preference, balancing faithfulness to the edit request with preservation of irrelevant regions. The edits include both single-image operations (e.g., changing attributes, scene modifications, adding/removing elements) and multi-image compositions where multiple inputs must be integrated.

**ZH** 任务 2. 图像编辑。图像编辑任务给出 1–3 张输入图像与一条文本编辑指令，以及生成器产出的候选编辑图像。评判器需选出最契合人类偏好的编辑结果，在忠于编辑请求与保留无关区域之间取得平衡。编辑操作既含单图操作（如属性修改、场景变换、元素增删），也包括需整合多张输入的多图合成。

**EN** Task 3. Interleaved Generation. Interleaved generation provides multimodal prompts that elicit mixed image–text sequences from generators (e.g., for storytelling, how-to guides, educational content, or multi-step reasoning). Reward models are asked to rank candidate interleaved outputs, capturing human preferences for coherence, global planning, and effective coordination between visual and textual content.

**ZH** 任务 3. 交错生成。交错生成任务给出多模态提示词，引导生成器输出图文混合序列（如故事叙述、操作指南、教学内容或多步推理）。评判器需对候选的交错输出排序，捕捉人类在连贯性、全局规划以及图文内容协同上的偏好。

**EN** Task 4. Multimodal Reasoning (Thinking with images). Multimodal reasoning provides complex problems that require visual understanding, logical inference, and multi-step problem solving. Generators may produce both text and intermediate thinking or sketchpad images; reward models must judge which candidate reasoning trajectory and final answer better aligns with human preference, emphasizing accurate perception, spatial reasoning, and clear explanation.

**ZH** 任务 4. 多模态推理（用图像思考）。多模态推理任务给出需要视觉理解、逻辑推断与多步求解的复杂问题。生成器可同时输出文本与中间思考或草图图像；评判器需判断哪条候选推理轨迹与最终答案更符合人类偏好，着重考察感知准确性、空间推理与解释清晰度。

**EN** See Figure 1 for examples of multimodal preference pairs in MMRB2 across these four subtasks.

**ZH** 图 1 给出了 MMRB2 在上述四个子任务中的图文偏好对示例。

**EN** 3.2 Prompt and response collection

**ZH** 3.2 提示词与响应采集

**EN** For each task, we sample prompts from existing benchmarks via stratified sampling over difficulty and subtask type, using only test splits to avoid train–test leakage. We additionally design new, practical tasks (e.g., multi-image editing) that are not covered in prior benchmarks. Benchmarks are weighted by coverage and difficulty, yielding 1,000 prompts per task. For each prompt, we generate multiple responses from 7–11 state-of-the-art models, including both API and open-source systems. We observe that even strong models such as Gemini 2.5 Flash Image struggle on interleaved generation and multimodal reasoning; for such cases, we further construct agents that can call Python and image generation/editing tools (Hu et al., 2024). Table 1 summarizes prompt sources and candidate models, with additional details in Appendix C.

**ZH** 对每个任务，我们从既有基准中按难度与子任务类型做分层抽样来选取提示词，且只使用测试集划分以避免训练—测试泄漏。我们另外设计了此前基准未覆盖的新型实用任务（如多图编辑）。各基准按覆盖度与难度加权，每个任务最终得到 1000 条提示词。对每条提示词，我们用 7–11 个最先进模型（含 API 与开源系统）各生成多条响应。我们观察到，即便是 Gemini 2.5 Flash Image 这样的强模型，在交错生成与多模态推理上仍显吃力；对此我们进一步构建了可调用 Python 与图像生成／编辑工具的智能体（Hu et al., 2024）。表 1 汇总了提示词来源与候选模型，更多细节见附录 C。

<!-- [原子块 · img]  -->

**EN** Figure 3: Overview of the MMRB2 data pipeline. The process combines ensemble MLLM judging, human verification, and multi-stage filtering to ensure high-quality, reasoning-consistent preference pairs across tasks.

**ZH** 图 3：MMRB2 数据流水线总览。该流程融合集成式 MLLM 评判、人工核验与多阶段过滤，以保证各类任务的偏好对兼具高质量与推理一致性。

**EN** 3.3 Human preference annotations

**ZH** 3.3 人类偏好标注

**EN** Given prompts and responses, we developed methods to gather human preferences for each task type.

**ZH** 在获得提示词与响应之后，我们针对各类任务设计了相应的人类偏好采集方法。

**EN** 3.3.1 Image generation, editing & interleaved tasks

**ZH** 3.3.1 图像生成、编辑与交错任务

**EN** We adopt a unified annotation protocol to ensure consistency across text-to-image generation, image editing, and interleaved generation tasks.

**ZH** 我们采用统一的标注规程，以保证文生图生成、图像编辑与交错生成三类任务之间的一致性。

**EN** Ensemble filtering. To focus human annotation on the most informative comparisons, we first apply an ensemble filtering pipeline that removes easy preference pairs where one response is almost unanimously preferred. We collect judgments from nine multimodal judges spanning API models (GPT-5, GPT-4.1, GPT-4o, Gemini 2.5 Flash, Gemini 2.5 Pro) and open-source VL models (Gemma-3-27B/12B/4B, Qwen-2.5-VL-7B), covering a wide range of capability. Each judge evaluates every pair twice, once in forward order (A vs. B) and once in reverse order (B vs. A), to mitigate position bias (see Appendix C for the exact prompts).

**ZH** 集成过滤。为使人工标注集中于信息量最大的对比，我们首先执行集成过滤流水线，剔除那些某一响应几乎被一致偏好的简单偏好对。我们收集九个多模态评判器的判断，涵盖 API 模型（GPT-5、GPT-4.1、GPT-4o、Gemini 2.5 Flash、Gemini 2.5 Pro）与开源视觉语言模型（Gemma-3-27B/12B/4B、Qwen-2.5-VL-7B），能力跨度很大。每个评判器对每组数据评判两次，一次按正序（A 对 B），一次按逆序（B 对 A），以缓解位置偏差（具体提示词见附录 C）。

**EN** We define easy pairs as those where the majority label appears in at least 90% of all judge evaluations across both orderings, and discard them because they provide little signal about fine-grained differences between reward models. While ensemble filtering can in principle introduce bias, the diversity of the judges and the high 90% threshold restrict filtering to near-trivial cases and mitigate systematic bias from any single model.

**ZH** 我们把多数标签在两种顺序下的全部评判结果中占比至少 90% 的样本定义为简单样本并予以剔除，因为它们几乎无法区分奖励模型之间的细微差别。集成过滤在原则上可能引入偏差，但评判器的多样性加上高达 90% 的阈值，把过滤范围限制在近乎平凡的样本上，从而抑制了来自单一模型的系统性偏差。

**EN** Human Preference Annotation. We employed professional annotators via the Surge AI platform to collect high-quality human preferences.11 1 Annotators were compensated at an hourly rate of $85. Each pair is independently evaluated by three annotators who have no knowledge of which model generated each response. Annotators assess each response using a comprehensive evaluation framework with different criteria tailored to each task category. Finally for each pair, annotators provide their overall preference for answer A vs B on a 7-point Likert scale where we convert these ratings to preferences. See details in Appendix C. We implement several additional quality control measures. First, we filter out annotations with high inter-annotator disagreement, specifically removing pairs where the rating spread (maximum rating minus minimum rating) exceeds 4 points on the 7-point scale. We also exclude ambiguous annotations where the average rating falls too close to the scale midpoint (within the 3.0-4.0 range), as these indicate genuine uncertainty rather than clear preferences from human annotations. Finally, we remove pairs where the majority vote results in a tie, as these provide limited signal for evaluating judge agreement.

**ZH** 人类偏好标注。我们通过 Surge AI 平台雇用专业标注者采集高质量人类偏好。11 1 标注者按每小时 85 美元的时薪计酬。每组数据由三位互不知晓响应来源模型的标注者独立评判。标注者依据一套综合评测框架打分，框架针对各类任务设有不同准则。最后，标注者在 7 点李克特量表上给出对答案 A 与 B 的总体偏好，我们把这些评分转换为偏好结果，详见附录 C。我们还实施了若干额外的质量控制措施：首先滤除标注者间分歧过大的样本，即剔除在 7 点量表上评分极差（最高分减最低分）超过 4 分的样本；其次排除平均评分过于接近量表中点（落在 3.0–4.0 区间）的模糊标注，因为这类标注反映的是真正的不确定，而非明确的人类偏好；最后剔除多数投票出现平局的样本，因为它们对评估评判器一致性提供的信息有限。

**EN** For the three generative tasks, we collected approximately 17,700 human preference judgments, each evaluated by three independent annotators, resulting in 5900 judgments overall. After filtering, we retain 1,000 pairs per task (approximately 50% of the initial set). Inter-annotator agreement on these filtered pairs is high: 95.6% overall (excluding ties), with task-specific rates of 95.3% for image generation, 96.3% for image editing, and 95.2% for interleaved generation.

**ZH** 针对三项生成任务，我们共采集约 17700 条人类偏好判断，每条由三位独立标注者评判，合计 5900 组判断。过滤后每个任务保留 1000 组偏好对（约占初始集合的 50%）。过滤后样本的标注者间一致率很高：整体为 95.6%（不含平局），其中图像生成 95.3%、图像编辑 96.3%、交错生成 95.2%。

**EN** 3.3.2 Multimodal reasoning task

**ZH** 3.3.2 多模态推理任务

**EN** Because multimodal reasoning prompts have ground truth answers, we collect human annotations per model response (rather than pairwise) then construct pairs.

**ZH** 由于多模态推理提示词带有标准答案，我们针对每条模型响应采集人类标注（而非成对标注），再据此构造偏好对。

**EN** Human annotation. We filter generated model responses from §3.2 to those that contain both the correct answer to the prompt and some form of reasoning. We then balance samples across responses that include text-only reasoning and those that reason with both images and text. We collect three human annotations per response that indicate whether the reasoning contained in the model response is correct. The annotator instructions are listed in Appendix B.2.

**ZH** 人类标注。我们从 §3.2 生成的模型响应中筛选出同时包含正确作答与某种推理过程的样本，并在纯文本推理与图文混合推理两类响应之间做均衡采样。每条响应收集三位标注者的判断，用以判定其中所含推理是否正确。标注者说明见附录 B.2。

**EN** Pair construction. With the annotated responses, we construct preference pairs. For the human-preferred sample of each pair, we select model responses in which all three human annotators agree that the reasoning contains no major errors and the model answer is correct. For the non-preferred sample of each pair, we utilize two kinds of responses: Correct answer, incorrect reasoning, where the model answer is correct but all three annotators consider the reasoning to contain major errors, and Incorrect answer, with reasoning, where the model answer is incorrect and some form of reasoning is included. For each pair, the two model responses may share the same modality (both text-only or both image+text) or be a combination. No model response is duplicated across pairs. For more details, see Appendix B.2.

**ZH** 偏好对构造。基于已标注的响应，我们构造偏好对。偏好对中的优选样本取自三位标注者一致认定推理无重大错误且作答正确的模型响应；淘汰样本则取自两类响应：其一是“答案正确、推理有误”，即模型答案正确但三位标注者均认为推理存在重大错误；其二是“答案错误、含推理”，即模型答案错误但包含某种形式的推理。每组偏好对的两条响应模态可以相同（同为纯文本或同为图像+文本），也可以不同。任何模型响应都不会在不同偏好对中重复出现，详见附录 B.2。

**EN** 3.4 Evaluation Method

**ZH** 3.4 评测方法

**EN** Finally, we use the preference pairs to evaluate reward models on MMRB2.

**ZH** 最后，我们用这些偏好对在 MMRB2 上评测奖励模型。

**EN** Positional consistent dual evaluation Position bias is common problem; models have a systematic preference for the first item in a pair (Min et al., 2022; Tan et al., 2025). To mitigate this, each pair is evaluated twice per judge: once in its original order (A vs. B) and once with responses swapped (B vs. A). Both forward and reverse judgments are retained as independent data points, doubling judge-human comparison instances. This protocol improves agreement statistics by increasing sample size and penalizes judges with high position bias.

**ZH** 位置一致的双次评测。位置偏差是常见问题：模型往往系统性地偏好成对样本中的第一项（Min et al., 2022; Tan et al., 2025）。为缓解这一点，每个评判器对每组数据评测两次，一次按原始顺序（A 对 B），一次交换响应顺序（B 对 A）。正序与逆序两次判断都作为独立数据点保留，使评判器—人类对比样本量翻倍。该方案既通过扩大样本量改善了统计量，也对位置偏差严重的评判器施加惩罚。

**EN** Judge-Human Agreement Computation We measure judge-human agreement by comparing each judge evaluation against the human preference for the corresponding pair. Human preference is determined by majority vote across three annotators for Tasks 1-3 and unanimous agreement of reasoning and answer correctness in Task 4. For each judge evaluation (whether forward or reverse), we compute a binary agreement score: 1.0 if the judge’s preference matches the human preference (including tie-to-tie matches), and 0.0 otherwise.

**ZH** 评判器—人类一致率计算。我们通过把评判器的每次判断与对应偏好对上的人类偏好作比较来度量一致率。人类偏好在任务 1–3 中由三位标注者多数投票决定，在任务 4 中则由推理与答案正确性的全体一致意见决定。对评判器的每次判断（无论正序或逆序），我们计算二值一致得分：若评判器偏好与人类偏好一致（含平局对平局的情形）记 1.0，否则记 0.0。

**EN** 4 Experiments

**ZH** 4 实验

**EN** We conduct a comprehensive study of omni reward modeling with MMRB2 along a number of dimensions: evaluation of MLLM-as-a-judge (§4.1), evaluation of other task-specific evaluators (§4.2), and in-depth analysis on various aspects of the benchmark and omni model reward modeling (§4.3 - 4.5).

**ZH** 我们沿多个维度用 MMRB2 对全模态奖励建模做了系统研究：以多模态大模型充当评判器的评测（§4.1）、其他任务专用评测器的评测（§4.2），以及针对基准本身与全模态奖励建模的多角度深入分析（§4.3–4.5）。

**EN** 4.1 Performance of MLLM-as-a-judge

**ZH** 4.1 以多模态大模型充当评判器的表现

<!-- [原子块 · table] Judge Text to Image Image Editing Interleaved Generation Multimodal Reasoning Avg. Open-source multimodal LLMs Gemma 3 4B ( Gemma Team et al., 2025 ) 51.7 51.0 51.3 48.8 50.7 Gemma 3 12B ( Gemma Team  -->

**EN** Table 2: MLLM-as-a-judge accuracies on MMRB2. The best numbers are bolded and the second best are underlined. Gemini 3 Pro is the best across all tasks. Qwen3-VL-32B is the best open-source model.

**ZH** 表 2：各 MLLM 评判器在 MMRB2 上的准确率。最优结果加粗，次优结果加下划线。Gemini 3 Pro 在所有任务上均居首位，Qwen3-VL-32B 是最优开源模型。

**EN** Setup. We evaluate all tasks on API-based models GPT-4o, GPT-4.1, GPT-5, Gemini 2.5 Flash, Gemini 2.5 Pro, Gemini 3 Pro and open-source models Qwen 2.5-VL (7B and 72B) (Bai et al., 2025), Qwen 3-VL (8B, 32B, 30BA3B, 235BA22B) (Qwen Team, 2025) and Gemma 3 (4B, 12B, and 27B) (Gemma Team et al., 2025). For each task type, we design task-specific evaluation prompts with detailed rubrics (see Appendix C). We follow the positional consistent dual evaluation method in §3.4 to mitigate positional bias.

**ZH** 设置。我们在 API 模型 GPT-4o、GPT-4.1、GPT-5、Gemini 2.5 Flash、Gemini 2.5 Pro、Gemini 3 Pro，以及开源模型 Qwen 2.5-VL（7B 与 72B）（Bai et al., 2025）、Qwen 3-VL（8B、32B、30BA3B、235BA22B）（Qwen Team, 2025）和 Gemma 3（4B、12B、27B）（Gemma Team et al., 2025）上评测全部任务。针对每类任务，我们设计了带细化评分准则的专用评测提示词（见附录 C），并遵循 §3.4 的位置一致双次评测方法以缓解位置偏差。

**EN** Results. Table 2 reveals substantial variation in judge-human agreement across models and tasks. API-based models generally outperform open-source alternatives, with Gemini 3 Pro achieving the strongest overall performance across all tasks. GPT-5 and Gemini 2.5 Pro also achieves decent accuracy on text-to-image generation, image editing, and interleaved generation (70 - 75% accuracy). Notably, multimodal reasoning proves to be the most challenging task across all models except Gemini 3 Pro, with even top API models achieving only 52-70% agreement on reasoning tasks (compared to 63-75% on multimodal generation tasks). This difficulty may stem from multiple valid solution paths, varying levels of explanation detail that humans may value differently, or the challenge of assessing both correctness and reasoning quality simultaneously.

**ZH** 结果。表 2 显示，不同模型与任务之间的评判器—人类一致率差异显著。API 模型总体优于开源模型，Gemini 3 Pro 在所有任务上表现最强。GPT-5 与 Gemini 2.5 Pro 在文生图、图像编辑与交错生成上也取得了不错的准确率（70–75%）。值得注意的是，除 Gemini 3 Pro 外，多模态推理是所有模型最难的任务：即便顶级 API 模型在推理任务上的一致率也只有 52–70%，而在多模态生成任务上可达 63–75%。这一困难可能源于解法路径不唯一、解释详略各异导致人类评价尺度不一，以及需同时判断正确性与推理质量。

**EN** Gemma 3, Qwen2.5-VL, and Qwen3-VL families of models all perform better on MMRB2 as number of parameters scales. Additionally, the performance gap between API-based and open-source models has narrowed with recent open-source advances. The top API models (Gemini 3 Pro, Gemini 2.5 Pro, GPT-5) achieve agreement rates of 65-80% across most tasks, while the best open-source models now reach competitive performance levels. Qwen3-VL-32B is the strongest open-source model, achieving 64.1-70.5% across tasks. Notably, its 70.5% agreement rate for interleaved generation approaches API-based model performance. While the Qwen3-VL series generally outperforms the Gemma 3 and Qwen2.5 families on image-related tasks, even some of the Gemma 3 and Qwen2.5 variants are within a few percentage points of API-based models. However, open-source models still show large gaps with API-based models on multimodal reasoning: the strongest, Qwen3-VL 30BA3B at 57.3%, trails Gemini 3 Pro by 22 percentage points.

**ZH** Gemma 3、Qwen2.5-VL 与 Qwen3-VL 三个系列在 MMRB2 上的表现都随参数量增长而提升。此外，随着近期开源模型的进步，API 模型与开源模型之间的差距已经收窄。顶级 API 模型（Gemini 3 Pro、Gemini 2.5 Pro、GPT-5）在多数任务上的一致率为 65–80%，而最优开源模型已达到可与之竞争的水平。Qwen3-VL-32B 是最强的开源模型，各任务一致率为 64.1–70.5%，其中交错生成的 70.5% 已逼近 API 模型。尽管 Qwen3-VL 系列在图像相关任务上整体优于 Gemma 3 与 Qwen2.5 系列，后两者的部分变体也已与 API 模型相差无几。不过在多模态推理上，开源模型与 API 模型仍有明显差距：最强的 Qwen3-VL 30BA3B 为 57.3%，落后 Gemini 3 Pro 达 22 个百分点。

**EN** 4.2 Performance of supervised reward models

**ZH** 4.2 有监督奖励模型的表现

<!-- [原子块 · table] Judge Text to Image Image Editing* Multimodal Reasoning* MLLM-as-a-judge Qwen2.5-VL-7B ( Bai et al., 2025 ) 50.4 57.8 53.7 Qwen3-VL-32B ( Qwen Team, 2025 ) 64.1 66.4 69.9 GPT-5 ( OpenAI, 2025b ) 70.5  -->

**EN** Table 3: Other evaluators’ accuracies on MMRB2. Note that all task-specific evaluators except CLIPScore and VQAScore have been trained with human preference pairs. *For editing we use the single-image subset; for reasoning we use the text-only-output subset, ensuring fair comparison among evaluators.

**ZH** 表 3：其他评测器在 MMRB2 上的准确率。注意除 CLIPScore 与 VQAScore 外，所有任务专用评测器都经人类偏好对训练。*编辑任务采用单图子集，推理任务采用纯文本输出子集，以保证各评测器之间公平比较。

**EN** Besides directly prompting MLLMs to act as judges, prior work has proposed a range of automatic metrics and preference-trained reward models targeting the tasks in MMRB2. We evaluate these methods on the three MMRB2 tasks—text-to-image generation, image editing, and multimodal reasoning. To the best of our knowledge, there are currently no evaluators specifically tailored for interleaved text–image outputs.

**ZH** 除直接提示 MLLM 充当评判器外，既有工作还提出了面向 MMRB2 各项任务的多种自动指标与偏好训练的奖励模型。我们在 MMRB2 的三个任务——文生图生成、图像编辑与多模态推理——上评测了这些方法。据我们所知，目前尚无专门面向图文交错输出的评测器。

**EN** Setup. Unless otherwise noted, we adopt the default metaprompt provided by each official library. For text-to-image, we consider two families of evaluators. The first is CLIP-based (Radford et al., 2021), including CLIPScore (Hessel et al., 2021) and its preference-trained variants ImageReward (Xu et al., 2023), HPSv2 (Wu et al., 2023a), and PickScore (Kirstain et al., 2023). The second family is based on Qwen2.5-VL-7B (Bai et al., 2025). We evaluate VQAScore (Lin et al., 2024), which scores generated images using model logits, as well as the preference-trained reward models HPSv3 (Ma et al., 2025) and UnifiedReward (Wang et al., 2025b). We evaluate all of the above models on the MMRB2 text-to-image task. Qwen2.5-VL-7B has also been used as the backbone for reward models on other tasks, including EditReward (Wu et al., 2025) for image editing and UnifiedReward (Wang et al., 2025b) for multimodal understanding. Because EditReward is trained only on single-image editing, and UnifiedReward is trained on single-image image-to-text tasks, we evaluate them on the corresponding single-image subsets of MMRB2 to ensure a fair comparison among evaluators. Table 3 summarizes the results.

**ZH** 设置。除特别说明外，我们采用各官方库提供的默认元提示词。文生图方面考虑两类评测器：第一类基于 CLIP（Radford et al., 2021），包括 CLIPScore（Hessel et al., 2021）及其偏好训练变体 ImageReward（Xu et al., 2023）、HPSv2（Wu et al., 2023a）与 PickScore（Kirstain et al., 2023）；第二类以 Qwen2.5-VL-7B（Bai et al., 2025）为基础，我们评测了利用模型 logits 为生成图像打分的 VQAScore（Lin et al., 2024），以及偏好训练的奖励模型 HPSv3（Ma et al., 2025）与 UnifiedReward（Wang et al., 2025b）。上述模型均在 MMRB2 文生图任务上评测。Qwen2.5-VL-7B 也用作其他任务奖励模型的骨干，包括面向图像编辑的 EditReward（Wu et al., 2025）与面向多模态理解的 UnifiedReward（Wang et al., 2025b）。由于 EditReward 仅在单图编辑上训练、UnifiedReward 在单图图到文本任务上训练，我们在 MMRB2 对应的单图子集上评测二者，以保证评测器之间公平比较。表 3 汇总了结果。

**EN** Preference training substantially improves reward-model accuracy. Several reward models share the same base architecture as our MLLM baselines (e.g., EditReward, UnifiedReward, and HPSv3 are based on Qwen2.5-VL-7B), and some are CLIP-based (ImageReward, HPSv2, PickScore). Relative to the Qwen2.5-VL-7B judge, EditReward yields a +9.4% gain on editing (57.8 ⟦SLOT_1⟧ 67.2), and UnifiedReward improves text-to-image by +9.4% (50.4 ⟦SLOT_2⟧ 59.8) and reasoning by +1.4% (53.7 ⟦SLOT_3⟧ 55.1). Similarly, compared to CLIPScore (51.0), CLIP-based preference models show consistent gains: ImageReward 54.0 (+3.0 %), HPSv2 54.7 (+3.7 %), and PickScore 58.6 (+7.6 %). These results indicate that training with human preferences is an effective way to boost evaluator performance on multimodal tasks.

**ZH** 偏好训练显著提升了奖励模型准确率。若干奖励模型与我们的 MLLM 基线共享同一基础架构（如 EditReward、UnifiedReward、HPSv3 均基于 Qwen2.5-VL-7B），另一些则基于 CLIP（ImageReward、HPSv2、PickScore）。相较 Qwen2.5-VL-7B 评判器，EditReward 在编辑任务上带来 +9.4% 增益（57.8 ⟦SLOT_1⟧ 67.2）；UnifiedReward 在文生图上提升 +9.4%（50.4 ⟦SLOT_2⟧ 59.8），在推理上提升 +1.4%（53.7 ⟦SLOT_3⟧ 55.1）。类似地，相较 CLIPScore（51.0），基于 CLIP 的偏好模型也有一致增益：ImageReward 54.0（+3.0%）、HPSv2 54.7（+3.7%）、PickScore 58.6（+7.6%）。这些结果表明，用人类偏好做训练是提升多模态任务评测器表现的有效途径。

**EN** Reward models can be out-of-distribution; strong MLLMs remain strong judges. Despite the above gains, most preference-trained reward models still underperform a larger open-source judge such as Qwen3-VL-32B across tasks; a notable exception is EditReward, which is competitive on editing (67.2 vs. 66.4). One plausible explanation is a distribution shift: several reward models were trained on data from earlier-generation systems (e.g., SD 2.1–era), and their accuracy diminishes when judging outputs from more capable, recent models. Overall, newer reward models (HPSv3, EditReward, UnifiedReward) are far better than older ones, yet stronger MLLM still set a high bar through simple prompting.

**ZH** 奖励模型可能存在分布外问题，强 MLLM 仍是更强的评判器。尽管有上述增益，多数偏好训练的奖励模型在各任务上仍不及 Qwen3-VL-32B 这类更大的开源评判器；一个显著例外是 EditReward，它在编辑任务上具备竞争力（67.2 对 66.4）。一种合理解释是分布偏移：部分奖励模型训练数据来自较早一代系统（如 SD 2.1 时期），在评判更新更强模型的输出时准确率下降。总体而言，较新的奖励模型（HPSv3、EditReward、UnifiedReward）远优于旧模型，但更强的 MLLM 仅凭简单提示就树立了很高的标杆。

**EN** 4.3 Correlation with downstream tasks

**ZH** 4.3 与下游任务的相关性

<!-- [原子块 · img]  -->

**EN** Figure 4: Downstream best-of-N score v.s. MMRB2 performance. We perform best-of-N sampling with 2 base models each on 4 tasks (GenAI-Bench (Li et al., 2024), GEdit-Bench (Liu et al., 2025), ISG-Bench (Chen et al., 2024), and EMMA (Hao et al., 2025)). A judge’s score on MMRB2 strongly correlates with improvement in downstream tasks when it is used in best-of-N sampling, highlighting MMRB2’s utility for downstream task success.

**ZH** 图 4：下游 Best-of-N 得分与 MMRB2 表现的对比。我们在 4 个任务（GenAI-Bench（Li et al., 2024）、GEdit-Bench（Liu et al., 2025）、ISG-Bench（Chen et al., 2024）与 EMMA（Hao et al., 2025））上各用 2 个基座模型做 Best-of-N 采样。评判器在 MMRB2 上的得分与其用于 Best-of-N 采样时下游任务的提升强相关，凸显了 MMRB2 对下游任务成败的指示价值。

**EN** A key research question is whether MMRB2 performance can predict downstream task performance. To address this question, following prior works (Lightman et al., 2023; Li et al., 2025), we conduct best-of-N sampling with different rewards. We experiment with 4 tasks: GenAI-Bench (Li et al., 2024), GEdit-Bench (Liu et al., 2025), ISG-Bench (Chen et al., 2024), and EMMA (Hao et al., 2025), each corresponds to one task in MMRB2. For each query, we generate ⟦SLOT_4⟧ candidate responses from two base models, one strong model and a weaker one, and we use 7 different MLLM-as-a-judge to select the best one via knockout tournaments. Then we evaluate the selected response with each task’s metrics.

**ZH** 一个关键研究问题是：MMRB2 上的表现能否预测下游任务表现。为回答这一问题，我们沿用前人做法（Lightman et al., 2023; Li et al., 2025），用不同奖励做 Best-of-N 采样。实验涵盖 4 个任务：GenAI-Bench（Li et al., 2024）、GEdit-Bench（Liu et al., 2025）、ISG-Bench（Chen et al., 2024）与 EMMA（Hao et al., 2025），各对应 MMRB2 中的一个任务。对每条查询，我们用两个基座模型——一个强模型与一个弱模型——各生成 ⟦SLOT_4⟧ 条候选响应，再用 7 个不同的 MLLM 评判器以淘汰赛方式选出最优者，最后用各任务自身的指标评测被选中的响应。

**EN** Figure 4 shows all the results. The x-axis is the MMRB2 performance, and Y-axis is the score of the best-of-N response selected by different rewards. We exclude GPT-4o and 4.1 because they are often used as evaluators. For interleaved generation, we remove ISGBench preference pairs when computing MMRB2 scores to avoid leakage. The results show that there is a strong correlation between best-of-N performance and MMRB2 scores. A good reward model can give great gains on downstream performance, even with the simple best-of-N sampling. For example, FLUX’s GenAI-Bench score improved from 73% to 79%, and GPT-4o’s accuracy on EMMA improved from 32% to 45%, when using GPT-5 as best-of-N selector. We can still see consistent gains even for strong base models like Gemini 2.5 Flash Image and o3-Sketchpad. The strong correlation (¿0.8 Pearson’s ⟦SLOT_5⟧ for all tasks and models) between MMRB2 and downstream task performance validates that MMRB2 is a good proxy for downstream effectiveness.

**ZH** 图 4 给出全部结果：横轴为 MMRB2 表现，纵轴为不同奖励选出的 Best-of-N 响应的得分。我们排除了 GPT-4o 与 4.1，因为它们常被用作评测器；在交错生成任务上，计算 MMRB2 得分时剔除 ISGBench 的偏好对以避免泄漏。结果显示 Best-of-N 表现与 MMRB2 得分之间存在强相关。即便只是简单的 Best-of-N 采样，优秀的奖励模型也能大幅提升下游表现。例如以 GPT-5 作 Best-of-N 选择器时，FLUX 的 GenAI-Bench 得分从 73% 提升到 79%，GPT-4o 在 EMMA 上的准确率从 32% 提升到 45%；即便是 Gemini 2.5 Flash Image 与 o3-Sketchpad 这样的强基座模型，也仍有稳定增益。MMRB2 与下游任务表现之间的强相关（各任务与各模型的 Pearson ⟦SLOT_5⟧ 均超过 0.8）验证了 MMRB2 是下游有效性的良好代理。

**EN** 4.4 Fine-grained analysis of errors

**ZH** 4.4 细粒度错误分析

**EN** Same-model pairs vs. different-model pairs. Our benchmark contains 57.4% same-model pairs (comparing two outputs from the same model) and 42.6% different-model pairs (comparing outputs from different models), allowing us to assess judge performance across both scenarios. See results in Table 4.

**ZH** 同源模型对与跨模型对。本基准包含 57.4% 的同源模型对（比较同一模型的两条输出）与 42.6% 的跨模型对（比较不同模型的输出），据此可评估评判器在两种情形下的表现，结果见表 4。

<!-- [原子块 · table] Task Judge Overall (%) Same-M (%) Diff-M (%) Image Generation Gemini 3 Pro 74.4 70.4 79.7 Gemini 2.5 Pro 70.5 68.4 73.4 GPT-5 70.5 66.8 75.6 GPT-4.1 65.8 61.6 71.4 Qwen3-VL-32B 64.1 59.1 71.0 Image Ed -->

**EN** Table 4: Detailed performance breakdown of top 5 judges per task showing overall agreement, same-model pairs, and different-model pairs with human preferences.

**ZH** 表 4：各任务前 5 名评判器的详细表现拆解，列出与人类偏好的整体一致率、同源模型对一致率与跨模型对一致率。

**EN** Across the image generation, editing, and interleaving tasks, we observe a consistent pattern for all judges: judges achieve higher agreement with human on different-model pairs compared to same-model pairs. For the best-performing judges, this gap ranges from 5-13 percentage points. For example, on image generation, Gemini 3 Pro achieves 79.7% agreement on different-model pairs but only 70.4% on same-model pairs (9.3 point gap). This pattern holds across tasks: same-model pairs demand fine-grained judgments within one model’s outputs, while different-model pairs reveal larger gaps rooted in capability differences.

**ZH** 在图像生成、编辑与交错任务上，所有评判器呈现一致规律：跨模型对上与人类的一致率高于同源模型对。对表现最好的评判器而言，这一差距在 5–13 个百分点之间。例如在图像生成任务上，Gemini 3 Pro 在跨模型对上达到 79.7%，在同源模型对上仅有 70.4%（相差 9.3 个百分点）。该规律在各任务上普遍成立：同源模型对要求在同一模型的输出之间做细粒度判断，而跨模型对的差异源自能力差距，因而更明显。

**EN** Same-modality pairs vs mixed-modality pairs. For the multimodal reasoning task, we study how judges perform differentially for pairs constructed with responses from the same modality (e.g., text response vs. text response) versus mixed modalities (e.g., text response vs. text-image response). Full results are reported in Table 5.

**ZH** 同模态对与混合模态对。针对多模态推理任务，我们考察了评判器在同模态偏好对（如文本响应对文本响应）与混合模态偏好对（如文本响应对图文响应）上的表现差异，完整结果见表 5。

<!-- [原子块 · table] Same modality: Image+text Same modality: Text Mixed modality: Pref: Image+text; Not Pref: Text Mixed modality: Pref: Text; Not Pref: Image+text Model Correct vs. incorrect reason Correct vs. incorrect -->

**EN** Table 5: Multimodal reasoning performance breakdown by pair modality and pair type.

**ZH** 表 5：按偏好对模态与类型拆解的多模态推理表现。

**EN** We find that for mixed-modal pairs, all judges exhibit a strong bias towards the response that contains images. This is true even of the highest performing models: the accuracy of GPT-5 for mixed-modal pairs when the preferred response contains an image is 49.3 points higher than pairs where the preferred response contains text (88.2% vs. 38.9%), and Gemini 2.5 Pro and Qwen3-VL-30BA3B have gaps of 27.7 and 36.0 points respectively. Gemini 3 Pro performs much better, but still has a 17.9 point gap. Additionally, we find that this trend holds for both pair types: those constructed with an incorrect response vs. a correct response and those with incorrect reasoning vs. correct reasoning.

**ZH** 我们发现，对混合模态偏好对，所有评判器都强烈偏向含图像的响应，即便表现最好的模型也不例外：GPT-5 在优选响应含图像的混合模态样本上，准确率比优选响应为纯文本的样本高出 49.3 个百分点（88.2% 对 38.9%）；Gemini 2.5 Pro 与 Qwen3-VL-30BA3B 的差距分别为 27.7 与 36.0 个百分点。Gemini 3 Pro 表现好得多，但仍有 17.9 个百分点的差距。此外，该趋势在两类偏好对上同样成立：一类由错误响应与正确响应构成，另一类由错误推理与正确推理构成。

**EN** 4.5 Test-time scaling of rewards

**ZH** 4.5 奖励的测试时扩展

<!-- [原子块 · img]  -->

**EN** Figure 5: Majority-vote accuracy of each MLLM as the number of samples ⟦SLOT_6⟧ varies. Test-time scaling yields small gains for GPT and Gemini models but no improvement for Qwen3-VL.

**ZH** 图 5：各 MLLM 的多数投票准确率随采样数 ⟦SLOT_6⟧ 的变化。测试时扩展给 GPT 与 Gemini 模型带来小幅增益，但对 Qwen3-VL 没有提升。

**EN** Prior work (Wang et al., 2022a; Brown et al., 2024) shows that test-time scaling can substantially improve LLM performance. We ask whether similar gains transfer to multimodal reward models. For each judge, we draw ⟦SLOT_7⟧ independent judgments and take a majority vote as the final decision. We report majority-vote accuracy averaged over the four MMRB2 tasks (300 examples per task) in Fig. 5.

**ZH** 前人工作（Wang et al., 2022a; Brown et al., 2024）表明，测试时扩展可大幅提升大语言模型的表现。我们考察同样的增益能否迁移到多模态奖励模型。对每个评判器，我们采样 ⟦SLOT_7⟧ 次独立判断并取多数投票作为最终决策。图 5 报告了在 MMRB2 四个任务上平均的多数投票准确率（每任务 300 个样例）。

**EN** The effects are model-dependent, echoing trends in prior observations (Li et al., 2025). Qwen3-VL models show no measurable improvement as ⟦SLOT_8⟧ increases. In contrast, GPT-4o, Gemini 2.5 Flash, GPT-5, and Gemini 2.5 Pro improve by roughly ⟦SLOT_9⟧–⟦SLOT_10⟧ at ⟦SLOT_11⟧, with Gemini 2.5 Pro showing the largest gain (from ⟦SLOT_12⟧ to ⟦SLOT_13⟧). Overall, test-time scaling provides only modest returns for multimodal reward models compared with text-only LLMs, suggesting that alternative scaling methods are needed for multimodal rewards.

**ZH** 效果因模型而异，与既有观察一致（Li et al., 2025）。Qwen3-VL 系列随 ⟦SLOT_8⟧ 增大没有可测的提升；相反，GPT-4o、Gemini 2.5 Flash、GPT-5 与 Gemini 2.5 Pro 在 ⟦SLOT_11⟧ 时提升约 ⟦SLOT_9⟧–⟦SLOT_10⟧，其中 Gemini 2.5 Pro 增益最大（从 ⟦SLOT_12⟧ 到 ⟦SLOT_13⟧）。总体而言，相比纯文本大语言模型，测试时扩展对多模态奖励模型的回报相当有限，说明多模态奖励需要其他扩展方法。

**EN** 5 Conclusion

**ZH** 5 结论

**EN** We introduce Multimodal RewardBench 2, the first comprehensive benchmark for omni reward models spanning four tasks: text-to-image, image editing, interleaved generation, and multimodal reasoning. Our analysis suggests that current omni reward models, particularly the latest Gemini 3 Pro, can serve as proxies for human evaluation on multimodal generation tasks, achieving 74-80% agreement. However, the substantial disagreement remaining (20-26%) indicates that human evaluation remains essential, , and that other models, including GPT-5, lag significantly behind Gemini 3 Pro. Overall, MMRB2 establishes a challenging and informative benchmark that we hope will serve as a foundation for future research on omni model reward modeling, evaluation, and post-training.

**ZH** 我们提出 Multimodal RewardBench 2，这是首个面向全模态奖励模型的综合基准，涵盖文生图、图像编辑、交错生成与多模态推理四项任务。分析表明，当前的全模态奖励模型——尤其是最新的 Gemini 3 Pro——可在多模态生成任务上充当人类评测的代理，一致率达 74–80%。但仍然存在 20–26% 的显著分歧，说明人类评测仍不可或缺，也说明包括 GPT-5 在内的其他模型明显落后于 Gemini 3 Pro。总体而言，MMRB2 建立了一个兼具挑战性与信息量的基准，期望成为全模态奖励建模、评测与后训练研究的基石。

**EN** Limitations and future extensions. As the first comprehensive benchmark targeting omni reward models, MMRB2 focuses on core settings and overall human preferences in interleaved text–image scenarios. The construction pipeline is modular and can be extended to additional evaluation dimensions (e.g., safety- and bias-sensitive preferences), richer task formats (e.g., multilingual tasks, in-the-wild prompts, multi-turn and agentic interactions), and further modalities (e.g., video and audio). Further discussion is provided in Appendix D.

**ZH** 局限与后续扩展。作为首个面向全模态奖励模型的综合基准，MMRB2 聚焦图文交错场景下的核心设置与整体人类偏好。其构建流程是模块化的，可进一步扩展到更多评测维度（如安全与偏见敏感的偏好）、更丰富的任务形式（如多语言任务、真实场景提示词、多轮与智能体交互）以及更多模态（如视频与音频）。更多讨论见附录 D。

**EN** 6 Acknowledgements

**ZH** 6 致谢

**EN** We would like to thank Mason Yu, Christophe Ropers, Nate Ekberg, Cynthia Gao, Justin Hovey, Jaimie Hsu, Samantha Snowden, and all annotators from Surge AI for their invaluable contributions to data annotation. We also thank Jonea Gordon and Vanessa Stark for their assistance with the approval process. Additionally, we are grateful to Mary Williamson, Xiaochuang Han, Adriana Romero Soriano, Michal Drozdzal, Xudong Wang, Michihiro Yasunaga, Ishan Misra, Amita Kamath, Inna Lin, and Karen Chen for their insightful discussions and support throughout this project.

**ZH** 感谢 Mason Yu、Christophe Ropers、Nate Ekberg、Cynthia Gao、Justin Hovey、Jaimie Hsu、Samantha Snowden 以及 Surge AI 全体标注者在数据标注上的宝贵贡献。感谢 Jonea Gordon 与 Vanessa Stark 在审批流程上的协助。同时感谢 Mary Williamson、Xiaochuang Han、Adriana Romero Soriano、Michal Drozdzal、Xudong Wang、Michihiro Yasunaga、Ishan Misra、Amita Kamath、Inna Lin 与 Karen Chen 在项目全程中的深入讨论与支持。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] Bai et al. (2025) Shuai Bai, Keqin Chen, Xuejing Liu, Jialin Wang, Wenbin Ge, Sibo Song, Kai Dang, Peng Wang, Shijie Wang, Jun Tang, et al. Qwen2. 5-vl technical report. arXiv preprint arXiv:2502.1392 -->

<!-- [原子块 · verbatim] Bai et al. (2022) Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn Drain, Stanislav Fort, Deep Ganguli, Tom Henighan, et al. Training a helpful and harmless assista -->

<!-- [原子块 · verbatim] Baldridge et al. (2024) Jason Baldridge, Jakob Bauer, Mukul Bhutani, Nicole Brichtova, Andrew Bunner, et al. Imagen 3. arXiv preprint arXiv:2408.07009 , 2024. https://arxiv.org/abs/2408.07009 . -->

<!-- [原子块 · verbatim] Brown et al. (2024) Bradley Brown, Jordan Juravsky, Ryan Ehrlich, Ronald Clark, Quoc V Le, Christopher Ré, and Azalia Mirhoseini. Large language monkeys: Scaling inference compute with repeated sampli -->

<!-- [原子块 · verbatim] Chameleon Team (2024) Chameleon Team. Chameleon: Mixed-modal early-fusion foundation models. arXiv preprint arXiv:2405.09818 , 2024. 10.48550/arXiv.2405.09818 . -->

<!-- [原子块 · verbatim] Chang et al. (2025) Jingjing Chang, Yixiao Fang, Peng Xing, Shuhan Wu, Wei Cheng, Rui Wang, Xianfang Zeng, Gang Yu, and Hai-Bao Chen. Oneig-bench: Omni-dimensional nuanced evaluation for image generat -->

<!-- [原子块 · verbatim] Chen et al. (2024) Dongping Chen, Ruoxi Chen, Shu Pu, Zhaoyi Liu, Yanru Wu, Caixi Chen, Benlin Liu, Yue Huang, Yao Wan, Pan Zhou, et al. Interleaved scene graphs for interleaved text-and-image generat -->

<!-- [原子块 · verbatim] Chen et al. (2025a) Jiuhai Chen, Zhiyang Xu, Xichen Pan, Yushi Hu, Can Qin, Tom Goldstein, Lifu Huang, Tianyi Zhou, Saining Xie, Silvio Savarese, Le Xue, Caiming Xiong, and Ran Xu. Blip3-o: A family o -->

<!-- [原子块 · verbatim] Chen et al. (2025b) Kaijie Chen, Zihao Lin, Zhiyang Xu, Ying Shen, Yuguang Yao, Joy Rimchala, Jiaxin Zhang, and Lifu Huang. R2I-bench: Benchmarking reasoning-driven text-to-image generation. In Christ -->

<!-- [原子块 · verbatim] Chen et al. (2025c) Xiaokang Chen, Zhiyu Wu, Xingchao Liu, Zizheng Pan, Wen Liu, Zhenda Xie, Xingkai Yu, and Chong Ruan. Janus-pro: Unified multimodal understanding and generation with data and model  -->

<!-- [原子块 · verbatim] Cho et al. (2024) Jaemin Cho, Yushi Hu, Roopal Garg, Peter Anderson, Ranjay Krishna, Jason Baldridge, Mohit Bansal, Jordi Pont-Tuset, and Su Wang. Davidsonian Scene Graph: Improving Reliability in Fin -->

<!-- [原子块 · verbatim] Christiano et al. (2017) Paul F. Christiano, Jan Leike, Tom B. Brown, Miljan Martic, Shane Legg, and Dario Amodei. Deep reinforcement learning from human preferences. In Advances in Neural Information -->

<!-- [原子块 · verbatim] Deng et al. (2025) Chaorui Deng, Deyao Zhu, Kunchang Li, Chenhui Gou, Feng Li, Zeyu Wang, Shu Zhong, Weihao Yu, Xiaonan Nie, Ziang Song, Guang Shi, and Haoqi Fan. Emerging properties in unified multim -->

<!-- [原子块 · verbatim] Fu et al. (2024) Xingyu Fu, Yushi Hu, Bangzheng Li, Yu Feng, Haoyu Wang, Xudong Lin, Dan Roth, Noah A Smith, Wei-Chiu Ma, and Ranjay Krishna. Blink: Multimodal large language models can see but not pe -->

<!-- [原子块 · verbatim] Ge et al. (2025) Yuying Ge, Sijie Zhao, Jinguo Zhu, Yixiao Ge, Kun Yi, Lin Song, Chen Li, Xiaohan Ding, and Ying Shan. Seed-x: Multimodal models with unified multi-granularity comprehension and genera -->

<!-- [原子块 · verbatim] Gemini Team (2025) Gemini Team. Gemini 2.5: Pushing the frontier with advanced reasoning, multimodality, long context, and next generation agentic capabilities, July 2025. https://arxiv.org/abs/2507.0 -->

<!-- [原子块 · verbatim] Gemma Team et al. (2025) Gemma Team, Aishwarya Kamath, Johan Ferret, Shreya Pathak, Nino Vieillard, Ramona Merhej, Sarah Perrin, Tatiana Matejovicova, Alexandre Ramé, Morgane Rivière, et al. Gemma 3 t -->

<!-- [原子块 · verbatim] Google DeepMind (2025a) Google DeepMind. Gemini 2.5 flash & 2.5 flash image: Model card. https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-2-5-Flash-Model-Card.pdf , September 2025a. -->

<!-- [原子块 · verbatim] Google DeepMind (2025b) Google DeepMind. Gemini 3 pro model card. Technical report, Google DeepMind, November 2025b. https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Pro-Model-Card.p -->

<!-- [原子块 · verbatim] Google DeepMind (2025c) Google DeepMind. Gemini 2.0 flash image: Native image generation with gemini 2.0 flash. https://developers.googleblog.com/experiment-with-gemini-20-flash-native-image-generatio -->

<!-- [原子块 · verbatim] Google DeepMind (2025d) Google DeepMind. Google gemini imagen 4: AI image generation. https://gemini.google/overview/image-generation/ , 2025d. -->

<!-- [原子块 · verbatim] Guo et al. (2025) Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al. Deepseek-r1: Incentivizing reasoning capability in llms  -->

<!-- [原子块 · verbatim] Han et al. (2024) Shuhao Han, Haotian Fan, Jiachen Fu, Liang Li, Tao Li, Junhui Cui, Yunqiu Wang, Yang Tai, Jingwei Sun, Chunle Guo, and Chongyi Li. Evalmuse-40k: A reliable and fine-grained benchmark -->

<!-- [原子块 · verbatim] Hao et al. (2025) Yunzhuo Hao, Jiawei Gu, Huichen Will Wang, Linjie Li, Zhengyuan Yang, Lijuan Wang, and Yu Cheng. Can mllms reason in multimodality? emma: An enhanced multimodal reasoning benchmark.  -->

<!-- [原子块 · verbatim] Hessel et al. (2021) Jack Hessel, Ari Holtzman, Maxwell Forbes, Ronan Le Bras, and Yejin Choi. Clipscore: A reference-free evaluation metric for image captioning. In Proceedings of the 2021 conference -->

<!-- [原子块 · verbatim] Hu et al. (2023) Yushi Hu, Benlin Liu, Jungo Kasai, Yizhong Wang, Mari Ostendorf, Ranjay Krishna, and Noah A Smith. Tifa: Accurate and interpretable text-to-image faithfulness evaluation with question -->

<!-- [原子块 · verbatim] Hu et al. (2024) Yushi Hu, Weijia Shi, Xingyu Fu, Dan Roth, Mari Ostendorf, Luke Zettlemoyer, Noah A Smith, and Ranjay Krishna. Visual sketchpad: Sketching as a visual chain of thought for multimodal  -->

<!-- [原子块 · verbatim] Hui et al. (2024) Mude Hui, Siwei Yang, Bingchen Zhao, Yichun Shi, Heng Wang, Peng Wang, Yuyin Zhou, and Cihang Xie. Hq-edit: A high-quality dataset for instruction-based image editing, 2024. https:// -->

<!-- [原子块 · verbatim] Jaech et al. (2024) Aaron Jaech, Adam Kalai, Adam Lerer, Adam Richardson, Ahmed El-Kishky, Aiden Low, Alec Helyar, Aleksander Madry, Alex Beutel, Alex Carney, et al. Openai o1 system card. arXiv prepr -->

<!-- [原子块 · verbatim] Kirstain et al. (2023) Yuval Kirstain, Adam Polyak, Uriel Singer, Shahbuland Matiana, Joe Penna, and Omer Levy. Pick-a-pic: An open dataset of user preferences for text-to-image generation. In Advance -->

<!-- [原子块 · verbatim] Labs et al. (2025) Black Forest Labs, Stephen Batifol, Andreas Blattmann, Frederic Boesel, Saksham Consul, Cyril Diagne, Tim Dockhorn, Jack English, Zion English, Patrick Esser, Sumith Kulal, Kyle Lac -->

<!-- [原子块 · verbatim] Lambert et al. (2024) Nathan Lambert, Jacob Morrison, Valentina Pyatkin, Shengyi Huang, Hamish Ivison, Faeze Brahman, Lester James V Miranda, Alisa Liu, Nouha Dziri, Shane Lyu, et al. Tulu 3: Pushing  -->

<!-- [原子块 · verbatim] Lambert et al. (2025) Nathan Lambert, Valentina Pyatkin, Jacob Morrison, Lester James Validad Miranda, Bill Yuchen Lin, Khyathi Chandu, Nouha Dziri, Sachin Kumar, Tom Zick, Yejin Choi, et al. Rewardbe -->

<!-- [原子块 · verbatim] Li et al. (2024) Baiqi Li, Zhiqiu Lin, Deepak Pathak, Jiayao Li, Yixin Fei, Kewen Wu, Tiffany Ling, Xide Xia, Pengchuan Zhang, Graham Neubig, et al. Genai-bench: Evaluating and improving compositional -->

<!-- [原子块 · verbatim] Li et al. (2025) Lei Li, Yuancheng Wei, Zhihui Xie, Xuqing Yang, Yifan Song, Peiyi Wang, Chenxin An, Tianyu Liu, Sujian Li, Bill Yuchen Lin, et al. Vl-rewardbench: A challenging benchmark for vision-l -->

<!-- [原子块 · verbatim] Liang et al. (2024) Youwei Liang, Junfeng He, Gang Li, Peizhao Li, Arseniy Klimovskiy, Nicholas Carolan, Jiao Sun, Jordi Pont-Tuset, Sarah Young, Feng Yang, Junjie Ke, Krishnamurthy Dj Dvijotham, Kati -->

<!-- [原子块 · verbatim] Lightman et al. (2023) Hunter Lightman, Vineet Kosaraju, Yuri Burda, Harrison Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. Let’s verify step by step. In T -->

<!-- [原子块 · verbatim] Lin et al. (2024) Zhiqiu Lin, Deepak Pathak, Baiqi Li, Jiayao Li, Xide Xia, Graham Neubig, Pengchuan Zhang, and Deva Ramanan. Evaluating text-to-visual generation with image-to-text generation. arXiv  -->

<!-- [原子块 · verbatim] Liu et al. (2024) Minqian Liu, Zhiyang Xu, Zihao Lin, Trevor Ashby, Joy Rimchala, Jiaxin Zhang, and Lifu Huang. Holistic evaluation for interleaved text-and-image generation, 2024. https://arxiv.org/a -->

<!-- [原子块 · verbatim] Liu et al. (2025) Shiyu Liu, Yucheng Han, Peng Xing, Fukun Yin, Rui Wang, Wei Cheng, Jiaqi Liao, Yingming Wang, Honghao Fu, Chunrui Han, et al. Step1x-edit: A practical framework for general image edi -->

<!-- [原子块 · verbatim] Luo et al. (2025) Xin Luo, Jiahao Wang, Chenyuan Wu, Shitao Xiao, Xiyan Jiang, Defu Lian, Jiajun Zhang, Dong Liu, and Zheng Liu. Editscore: Unlocking online rl for image editing via high-fidelity rewa -->

<!-- [原子块 · verbatim] Ma et al. (2025) Yuhang Ma, Xiaoshi Wu, Keqiang Sun, and Hongsheng Li. Hpsv3: Towards wide-spectrum human preference score. In Proceedings of the IEEE/CVF International Conference on Computer Vision ( -->

<!-- [原子块 · verbatim] Malik et al. (2025) Saumya Malik, Valentina Pyatkin, Sander Land, Jacob Morrison, Noah A Smith, Hannaneh Hajishirzi, and Nathan Lambert. Rewardbench 2: Advancing reward model evaluation. arXiv preprin -->

<!-- [原子块 · verbatim] Min et al. (2022) Sewon Min, Mike Lewis, Hannaneh Hajishirzi, and Luke Zettlemoyer. Noisy channel language model prompting for few-shot text classification. In Smaranda Muresan, Preslav Nakov, and Ali -->

<!-- [原子块 · verbatim] Niu et al. (2025) Yuwei Niu, Munan Ning, Mengren Zheng, Weiyang Jin, Bin Lin, Peng Jin, Jiaqi Liao, Kunpeng Ning, Chaoran Feng, Bin Zhu, and Li Yuan. Wise: A world knowledge-informed semantic evaluati -->

<!-- [原子块 · verbatim] OpenAI (2024) OpenAI. Gpt-4o system card. arXiv preprint arXiv:2410.21276 , 2024. -->

<!-- [原子块 · verbatim] OpenAI (2025a) OpenAI. Introducing gpt-4.1 in the api. https://openai.com/index/gpt-4-1/ , April 2025a. Blog post (no standalone technical report/system card published as of this date). -->

<!-- [原子块 · verbatim] OpenAI (2025b) OpenAI. Gpt-5 system card. https://cdn.openai.com/gpt-5-system-card.pdf , August 2025b. Version dated Aug 13, 2025. -->

<!-- [原子块 · verbatim] OpenAI (2025c) OpenAI. Gpt-image 1 (gpt-image-1) model card. https://platform.openai.com/docs/models/gpt-image-1 , April 2025c. API documentation and model card for GPT-Image 1, an image-generation mo -->

<!-- [原子块 · verbatim] OpenAI (2025d) OpenAI. Openai o3 and o4-mini system card. https://cdn.openai.com/pdf/2221c875-02dc-4789-800b-e7758f3722c1/o3-and-o4-mini-system-card.pdf , April 2025d. -->

<!-- [原子块 · verbatim] Peng et al. (2025) Yuang Peng, Yuxin Cui, Haomiao Tang, Zekun Qi, Runpei Dong, Jing Bai, Chunrui Han, Zheng Ge, Xiangyu Zhang, and Shu-Tao Xia. Dreambench++: A human-aligned benchmark for personalized -->

<!-- [原子块 · verbatim] Qwen Team (2025) Qwen Team. Qwen3-vl: Sharper vision, deeper thought, broader action. Qwen Blog. Accessed , pages 10–04, 2025. -->

<!-- [原子块 · verbatim] Radford et al. (2021) Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, et al. Learning transferable v -->

<!-- [原子块 · verbatim] Saha et al. (2025) Swarnadeep Saha, Xian Li, Marjan Ghazvininejad, Jason Weston, and Tianlu Wang. Learning to plan & reason for evaluation with thinking-llm-as-a-judge. 2025. 10.48550/arXiv.2501.18099 -->

<!-- [原子块 · verbatim] Sheynin et al. (2024) Shelly Sheynin, Adam Polyak, Uriel Singer, Yuval Kirstain, Amit Zohar, Oron Ashual, Devi Parikh, and Yaniv Taigman. Emu edit: Precise image editing via recognition and generation -->

<!-- [原子块 · verbatim] Shi et al. (2025) Yang Shi, Yuhao Dong, Yue Ding, Yuran Wang, Xuanyu Zhu, Sheng Zhou, Wenting Liu, Haochen Tian, Rundong Wang, Huanqian Wang, Zuyan Liu, Bohan Zeng, Ruizhe Chen, Qixun Wang, Zhuoran Zh -->

<!-- [原子块 · verbatim] Stability AI (2024) Stability AI. Introducing stable diffusion 3.5. https://stability.ai/news/introducing-stable-diffusion-3-5 , 2024. -->

<!-- [原子块 · verbatim] Tan et al. (2025) Sijun Tan, Siyuan Zhuang, Kyle Montgomery, William Y. Tang, Alejandro Cuadron, Chenguang Wang, Raluca Ada Popa, and Ion Stoica. Judgebench: A benchmark for evaluating llm-based judge -->

<!-- [原子块 · verbatim] Wang et al. (2024a) Fei Wang, Xingyu Fu, James Y Huang, Zekun Li, Qin Liu, Xiaogeng Liu, Mingyu Derek Ma, Nan Xu, Wenxuan Zhou, Kai Zhang, et al. Muirbench: A comprehensive benchmark for robust multi- -->

<!-- [原子块 · verbatim] Wang et al. (2024b) Xinlong Wang, Xiaosong Zhang, Zhengxiong Luo, Quan Sun, Yufeng Cui, Jinsheng Wang, Fan Zhang, Yueze Wang, Zhen Li, Qiying Yu, Yingli Zhao, Yulong Ao, Xuebin Min, Tao Li, Boya Wu, B -->

<!-- [原子块 · verbatim] Wang et al. (2025a) Xiyao Wang, Chunyuan Li, Jianwei Yang, Kai Zhang, Bo Liu, Tianyi Xiong, and Furong Huang. Llava-critic-r1: Your critic model is secretly a strong policy model. arXiv preprint arXiv -->

<!-- [原子块 · verbatim] Wang et al. (2022a) Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. Self-consistency improves chain of thought reasoning in language model -->

<!-- [原子块 · verbatim] Wang et al. (2025b) Yibin Wang, Yuhang Zang, Hao Li, Cheng Jin, and Jiaqi Wang. Unified reward model for multimodal understanding and generation. arXiv preprint arXiv:2503.05236 , 2025b. -->

<!-- [原子块 · verbatim] Wang et al. (2022b) Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa Liu, Noah A. Smith, Daniel Khashabi, and Hannaneh Hajishirzi. Self-instruct: Aligning language models with self-generated instruc -->

<!-- [原子块 · verbatim] Whitehouse et al. (2025) Chenxi Whitehouse, Tianlu Wang, Ping Yu, Xian Li, Jason Weston, Ilia Kulikov, and Swarnadeep Saha. J1: Incentivizing thinking in llm-as-a-judge via reinforcement learning. 202 -->

<!-- [原子块 · verbatim] Wu et al. (2025) Keming Wu, Sicong Jiang, Max Ku, Ping Nie, Minghao Liu, and Wenhu Chen. Editreward: A human-aligned reward model for instruction-guided image editing. arXiv preprint arXiv:2509.26346  -->

<!-- [原子块 · verbatim] Wu and Xie (2023) Penghao Wu and Saining Xie. V*: Guided visual search as a core mechanism in multimodal llms. arXiv preprint arXiv:2312.14135 , 2023. -->

<!-- [原子块 · verbatim] Wu et al. (2023a) Xiaoshi Wu, Yiming Hao, Keqiang Sun, Yixiong Chen, Feng Zhu, Rui Zhao, and Hongsheng Li. Human preference score v2: A solid benchmark for evaluating human preferences of text-to-imag -->

<!-- [原子块 · verbatim] Wu et al. (2023b) Xiaoshi Wu, Keqiang Sun, Feng Zhu, Rui Zhao, and Hongsheng Li. Human preference score: Better aligning text-to-image models with human preference. In Proceedings of the IEEE/CVF Inte -->

<!-- [原子块 · verbatim] Wu et al. (2023c) Zeqiu Wu, Yushi Hu, Weijia Shi, Nouha Dziri, Alane Suhr, Prithviraj Ammanabrolu, Noah A Smith, Mari Ostendorf, and Hannaneh Hajishirzi. Fine-grained human feedback gives better rewar -->

<!-- [原子块 · verbatim] Xiong et al. (2025) Tianyi Xiong, Xiyao Wang, Dong Guo, Qinghao Ye, Haoqi Fan, Quanquan Gu, Heng Huang, and Chunyuan Li. Llava-critic: Learning to evaluate multimodal models. In Proceedings of the Com -->

<!-- [原子块 · verbatim] Xu et al. (2023) Jiazheng Xu, Xiao Liu, Yuchen Wu, Yuxuan Tong, Qinkai Li, Ming Ding, Jie Tang, and Yuxiao Dong. Imagereward: Learning and evaluating human preferences for text-to-image generation. Ad -->

<!-- [原子块 · verbatim] Xu et al. (2025) Weiye Xu, Jiahao Wang, Weiyun Wang, Zhe Chen, Wengang Zhou, Aijun Yang, Lewei Lu, Houqiang Li, Xiaohua Wang, Xizhou Zhu, Wenhai Wang, Jifeng Dai, and Jinguo Zhu. Visulogic: A benchmar -->

<!-- [原子块 · verbatim] Yao et al. (2025) Jihan Yao, Yushi Hu, Yujie Yi, Bin Han, Shangbin Feng, Guang Yang, Bingbing Wen, Ranjay Krishna, Lucy Lu Wang, Yulia Tsvetkov, Noah A. Smith, and Banghua Zhu. Mmmg: a comprehensive a -->

<!-- [原子块 · verbatim] Yasunaga et al. (2025) Michihiro Yasunaga, Luke Zettlemoyer, and Marjan Ghazvininejad. Multimodal rewardbench: Holistic evaluation of reward models for vision language models. arXiv preprint arXiv:250 -->

<!-- [原子块 · verbatim] Yin et al. (2025) Baiqiao Yin, Qineng Wang, Pingyue Zhang, Jianshu Zhang, Kangrui Wang, Zihan Wang, Jieyu Zhang, Keshigeyan Chandrasegaran, Han Liu, Ranjay Krishna, et al. Spatial mental modeling from -->

<!-- [原子块 · verbatim] Yuan et al. (2024) Weizhe Yuan, Richard Yuanzhe Pang, Kyunghyun Cho, Xian Li, Sainbayar Sukhbaatar, Jing Xu, and Jason E Weston. Self-rewarding language models. In Forty-first International Conference -->

<!-- [原子块 · verbatim] Zhang et al. (2025) Xinchen Zhang, Xiaoying Zhang, Youbin Wu, Yanbin Cao, Renrui Zhang, Ruihang Chu, Ling Yang, and Yujiu Yang. Generative universal verifier as multimodal meta-reasoner. arXiv preprin -->

<!-- [原子块 · verbatim] Zhao et al. (2025) Xiangyu Zhao, Peiyuan Zhang, Kexian Tang, Xiaorong Zhu, Hao Li, Wenhao Chai, Zicheng Zhang, Renqiu Xia, Guangtao Zhai, Junchi Yan, et al. Envisioning beyond the pixels: Benchmarking -->

<!-- [原子块 · verbatim] Zheng et al. (2023) Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric P. Xing, Hao Zhang, Joseph E. Gonzalez, and Ion Stoica.  -->

<!-- [原子块 · verbatim] Zhou et al. (2024) Chunting Zhou, Lili Yu, Arun Babu, Kushal Tirumala, Michihiro Yasunaga, Leonid Shamis, Jacob Kahn, Xuezhe Ma, Luke Zettlemoyer, and Omer Levy. Transfusion: Predict the next token an -->

**EN** Contents of Supplementary Material

**ZH** 补充材料目录

**EN** Additional experimental results.A

**ZH** 补充实验结果 A

**EN** Details of annotation and pair construction.B

**ZH** 标注与偏好对构造细节 B

**EN** Additional details for prompts, response generation, and MLLM-as-a-judge.C

**ZH** 提示词、响应生成与 MLLM 评判器的补充细节 C

**EN** Limitations and Future Directions.D

**ZH** 局限与未来方向 D

**EN** Examples.E

**ZH** 示例 E

**EN** Appendix A Additional Experimental Results

**ZH** 附录 A 补充实验结果

**EN** A.1 Performance by task source and pair type

**ZH** A.1 按任务来源与偏好对类型的表现

**EN** The pairwise evaluation results presented in Tables 6, 7, 8, 9 distinct performance patterns across multimodal tasks and model capabilities.

**ZH** 表 6、7、8、9 给出的成对评测结果呈现出跨多模态任务与模型能力的差异化表现规律。

**EN** Image Generation: Performance varies moderately across benchmarks, with realunify (48-78.5%) and oneigbench (73-74% for top models) showing higher judge agreement rates, while wise consistently yields the lowest scores across all models (47-66%).

**ZH** 图像生成：各基准上的表现差异适中，realunify（48–78.5%）与 oneigbench（顶级模型 73–74%）的评判器一致率较高，而 wise 在所有模型上始终最低（47–66%）。

**EN** Image Editing: The breakdown reveals stark differences in benchmark difficulty, with text-based editing benchmarks (text: 54-83%, risebench: 48-83%) showing significantly higher agreement rates compared to general editing tasks (emu-edit: 49-72%, multi-image editing: 51-71%). This pattern holds consistently across all judge models, indicating that text rendering or text-focused editing provides clearer discriminative signals for pairwise evaluation than open-ended creative edits.

**ZH** 图像编辑：拆解结果揭示了基准难度上的显著差别，基于文本的编辑基准（text: 54–83%，risebench: 48–83%）一致率明显高于通用编辑任务（emu-edit: 49–72%，多图编辑: 51–71%）。这一规律在所有评判模型上一致成立，说明文字渲染或面向文本的编辑比开放式创意编辑提供了更清晰的成对评测判别信号。

**EN** Interleaved: Performance is relatively uniform across benchmarks for top models, with isgbench consistently scoring highest (76-79% for frontier models) and all benchmarks clustering within a 5-8 percentage point range for leading judges.

**ZH** 交错生成：顶级模型在各基准上的表现相对均匀，isgbench 始终最高（前沿模型 76–79%），对领先评判器而言所有基准都聚拢在 5–8 个百分点的区间内。

**EN** Reasoning: This task exhibits the most dramatic benchmark-level variance, with muirbench showing substantially higher scores (36-76%) compared to other benchmarks, while vstar proves exceptionally challenging (30-52%). The performance on blink and mindcube clusters tightly (44-55% for most models), suggesting these represent a baseline reasoning difficulty.

**ZH** 推理：该任务在基准层面的方差最为剧烈，muirbench 的分数明显更高（36–76%），而 vstar 异常困难（30–52%）。blink 与 mindcube 上的表现紧密聚拢（多数模型 44–55%），说明二者代表了一种基线推理难度。

<!-- [原子块 · table] Judge Model Overall % evalmuse oneigbench r2ibench realunify wise (n=390) (n=278) (n=128) (n=93) (n=111) Gemini 3 Pro 74.4% 74.5% 74.5% 72.7% 80.1% 71.2% Gemini 2.5 Pro 70.5% 69.6% 73.0% 70.7% 77.4% 6 -->

**EN** Table 6: Image Generation: Pairwise model evaluation breakdown by benchmark.

**ZH** 表 6：图像生成——按基准拆解的成对模型评测结果。

<!-- [原子块 · table] Judge Model Overall % dreambench emu-edit hq-edit multi-image editing risebench text (n=242) (n=329) (n=53) (n=178) (n=84) (n=114) Gemini 3 Pro 74.9% 70.0% 75.8% 79.2% 68.5% 82.1% 84.6% GPT5 73.8% 71. -->

**EN** Table 7: Image Editing: Pairwise model evaluation breakdown by benchmark.

**ZH** 表 7：图像编辑——按基准拆解的成对模型评测结果。

<!-- [原子块 · table] Judge Model Overall % chameleon interleavedeval isgbench mmmg (n=284) (n=267) (n=421) (n=28) Gemini 3 Pro 76.4% 76.4% 76.8% 76.1% 76.8% Gemini 2.5 Pro 75.1% 73.4% 71.5% 78.5% 75.0% GPT5 74.4% 72.9% 72 -->

**EN** Table 8: Interleaved: Pairwise model evaluation breakdown by benchmark.

**ZH** 表 8：交错生成——按基准拆解的成对模型评测结果。

<!-- [原子块 · table] Judge Model Overall % blink mindcube muirbench realunify visulogic vstar (n=355) (n=367) (n=137) (n=55) (n=49) (n=37) Qwen-3 vl32b 56.6% 52.4% 55.6% 71.5% 56.4% 61.2% 45.9% Qwen-3 vl30ba3b 56.5% 54.6% -->

**EN** Table 9: Reasoning: Pairwise model evaluation breakdown by benchmark.

**ZH** 表 9：推理——按基准拆解的成对模型评测结果。

**EN** A.2 Win rate analysis on generations

**ZH** A.2 生成结果的胜率分析

**EN** We also report the generation capabilities of MLLMs as content producers (models generating the multimodal content being evaluated, reported in Table 10). Judging requires discriminative understanding and alignment with human preferences, while generation requires creative synthesis and technical execution. A model may excel at one role while underperforming at the other, as we observe in our results.

**ZH** 我们也报告了 MLLM 作为内容生产者（即生成被评测的多模态内容的模型）的能力，见表 10。评判要求判别式理解与人类偏好契合，而生成要求创意合成与技术执行。一个模型可能在其中一种角色上出色、在另一种上欠佳，我们的结果正体现了这一点。

**EN** Table 10 presents the win rates of generative models across MMRB2’s three generation tasks (Tasks 1–3), where win rate is computed as ⟦SLOT_14⟧ comparisons based on human majority preferences. These are the same model outputs that judges evaluate in Table 2, allowing us to assess both generation quality and judgment accuracy within a unified framework.

**ZH** 表 10 给出各生成模型在 MMRB2 三项生成任务（任务 1–3）上的胜率，胜率按 ⟦SLOT_14⟧ 次基于人类多数偏好的比较计算。这些正是表 2 中评判器所评测的同一批模型输出，因此我们可以在统一框架内同时考察生成质量与判断准确率。

**EN** Image Generation. GPT-Image-1 (60.4%) narrowly leads text-to-image generation, closely followed by Imagen 4 (57.4%), Imagen 4 Ultra (56.5%), and Gemini 2.5 Flash (54.3%), indicating a highly competitive landscape among top proprietary models with less than 6 points separating the leaders. Open-source models lag substantially: Stable Diffusion 3.5 Large (41.0%) and FLUX (36.8%) trail by 19–24 points.

**ZH** 图像生成。GPT-Image-1（60.4%）以微弱优势领跑文生图，其后紧随 Imagen 4（57.4%）、Imagen 4 Ultra（56.5%）与 Gemini 2.5 Flash（54.3%），说明顶级闭源模型之间竞争极为激烈，领先者差距不足 6 个百分点。开源模型则明显落后：Stable Diffusion 3.5 Large（41.0%）与 FLUX（36.8%）相差 19–24 个百分点。

**EN** Image Editing. Interestingly, general-purpose multimodal models such as Gemini 2.5 Flash (59.2%) and GPT-Image-1 (53.2%) outperform specialized models. While Imagen Edit achieves only a 35.2% win rate despite being purpose-built for editing, the gap is less severe than earlier reports suggested. FLUX-Kontext (49.0%) demonstrates competitive performance for an open-source solution, though it still trails the leaders. These results suggest that strong vision–language understanding provides significant advantages for instruction-based editing, even if specialized architectures are not entirely obsolete.

**ZH** 图像编辑。有意思的是，Gemini 2.5 Flash（59.2%）与 GPT-Image-1（53.2%）这类通用多模态模型反而优于专用模型。尽管 Imagen Edit 专为编辑设计，胜率却只有 35.2%，不过差距没有早期报告所暗示的那般悬殊。FLUX-Kontext（49.0%）作为开源方案表现出竞争力，但仍落后于领先者。这些结果说明，强大的视觉—语言理解为指令式编辑带来显著优势，即便专用架构并未完全过时。

**EN** Interleaved Generation. Agent-based systems dominate, with GPT-Gemini Agent (57.1%) and GPT-Image Agent (56.9%) leading by narrow margins. Native multimodal models like Gemini 2.5 Flash (53.2%) perform competitively, narrowing the gap with agent architectures. GPT-FLUX Agent’s improved but still modest performance (40.4%) confirms that agent quality depends critically on component model quality, though the improvement suggests that better integration strategies can help.

**ZH** 交错生成。基于智能体的系统占据主导，GPT-Gemini Agent（57.1%）与 GPT-Image Agent（56.9%）以微弱优势领先。Gemini 2.5 Flash（53.2%）等原生多模态模型表现同样不俗，缩小了与智能体架构的差距。GPT-FLUX Agent 虽有改善但仍显一般（40.4%），印证了智能体质量严重依赖组件模型的质量，不过其进步也说明更优的集成策略可以带来帮助。

<!-- [原子块 · table] Rank Task Model Win Rate (%) 1 2 3 4 5 6 7 8 Image Gen. GPT-Image-1 60.4 Imagen 4 57.4 Imagen 4 Ultra 56.5 Gemini 2.5 Flash 54.3 Imagen 3 49.2 Gemini 2.0 Flash 45.6 SD 3.5 Large 41.0 FLUX 36.8 1 2 3 4 -->

**EN** Table 10: Model win rates (%) on Multimodal RewardBench 2 ranked by performance within each task. Win rate is computed as (wins + 0.5 × ties) / total comparisons.

**ZH** 表 10：各模型在 Multimodal RewardBench 2 上的胜率（%），按各任务内的表现排序。胜率计算为（胜场 + 0.5 × 平局）/ 总比较次数。

**EN** Appendix B Details for Annotation and Pair Construction

**ZH** 附录 B 标注与偏好对构造细节

**EN** B.1 Tasks 1-3

**ZH** B.1 任务 1–3

**EN** Figure 6 shows a sample of the annotation interface for the MMRB2 text-to-image task. In this section we provide additional details on the human annotation procedure.

**ZH** 图 6 展示了 MMRB2 文生图任务标注界面的样例。本节给出人类标注流程的补充细节。

<!-- [原子块 · img]  -->

**EN** Figure 6: Annotation interface for the MMRB2 text-to-image task. Note that for image editing and interleaved tasks, there are more fine-grained questions.

**ZH** 图 6：MMRB2 文生图任务的标注界面。注意图像编辑与交错任务包含更细粒度的问题。

**EN** For each annotation task, we provide a prompt and two responses, A and B, and the goal is to assess the quality of each response and then rate them. Annotators answer the following questions:

**ZH** 每项标注任务提供一个提示词与 A、B 两条响应，目标是评估每条响应的质量并为其打分。标注者需回答以下问题：

**EN** • Prompt Quality Check: Indicate whether the prompt is correct (Yes/No).

**ZH** • 提示词质量检查：指出提示词是否正确（是／否）。

**EN** • Pointwise Evaluation for Response A and Response B: For each response, rate the following dimensions on a 4-point scale (see Section B.1.1 for details): – Faithfulness to the text instruction – (Tasks 2 and 3) Faithfulness to the input image – Overall quality of the generated image – (Task 3 only) Cross-generation image congruence – (Task 3 only) Generated text-image alignment – (Task 3 only) Technical quality of generated text – (Conditional) Correctness of text rendering

**ZH** • 响应 A 与响应 B 的逐点评测：对每条响应，在 4 点量表上为下列维度打分（详见 B.1.1）：——对文本指令的忠实度 ——（任务 2 和 3）对输入图像的忠实度 ——生成图像的整体质量 ——（仅任务 3）跨生成图像的一致性 ——（仅任务 3）生成文本与图像的对齐度 ——（仅任务 3）生成文本的技术质量 ——（条件性）文字渲染的正确性

**EN** • Rationales: Provide a brief rationale for the overall quality rating of both Response A and Response B.

**ZH** • 理由：为响应 A 与响应 B 的整体质量评分各提供简要理由。

**EN** • Overall Preference: Indicate your overall preference between Response A and Response B, choosing one of the following: – A is significantly better – A is marginally better – Unsure or A is negligibly better – Unsure or B is negligibly better – B is marginally better – B is significantly better

**ZH** • 总体偏好：给出对响应 A 与响应 B 的总体偏好，从下列选项中选择其一：——A 明显更好 ——A 略好 ——不确定或 A 微弱更好 ——不确定或 B 微弱更好 ——B 略好 ——B 明显更好

**EN** • Rationale for Preference: Provide a brief explanation for your overall preference.

**ZH** • 偏好理由：为总体偏好提供简要解释。

**EN** B.1.1 Details of each question

**ZH** B.1.1 各问题详解

**EN** 1. (For all tasks) Faithfulness to the text instruction: How accurately and completely does the output follow the explicit and implicit text instructions in the prompt? Rating Label Description 0 Major deviations Key elements are missing, altered, or contradicted 1 Some mismatch Some key elements are missing or altered. 2 Minor mismatch Most key elements are present, but others are missing, incorrect, or incomplete 3 Full match All key elements are represented exactly as described, with no significant omissions or contradictions

**ZH** 1.（所有任务）对文本指令的忠实度：输出在多大程度上准确、完整地遵循了提示词中的显性与隐性文本指令？ 评分 标签 说明 0 重大偏离 关键元素缺失、被改动或被曲解 1 部分不符 部分关键元素缺失或被改动 2 轻微不符 多数关键元素存在，但另有元素缺失、错误或不完整 3 完全匹配 所有关键元素均按描述准确呈现，无显著遗漏或矛盾

**EN** 2. (For task 2 and 3) Faithfulness to the input image: When using an input image as context (e.g., editing, continuation, transformation), how well does the output incorporate the relevant elements of the input according to the instructions? Rating Label Description 0 Fails to use the input meaningfully Key elements are ignored, misinterpreted, or contradicted 1 Partial mismatch to the input Some elements are carried over or transformed correctly, but those are not key elements or important aspects 2 Minor mismatch to the input Most relevant elements are carried over or transformed correctly, but a few aspects are missing or incorrectly handled 3 Uses input fully All relevant elements from the input are accurately incorporated, extended, or transformed exactly as instructed

**ZH** 2.（任务 2 和 3）对输入图像的忠实度：在以输入图像为上下文时（如编辑、续写、变换），输出按指令对输入相关元素的融合程度如何？ 评分 标签 说明 0 未能有效利用输入 关键元素被忽略、误读或曲解 1 与输入部分不符 部分元素被正确沿用或变换，但这些并非关键元素或重要方面 2 与输入轻微不符 多数相关元素被正确沿用或变换，但少数方面缺失或处理不当 3 充分利用输入 输入中的所有相关元素均被准确融合、延展或按指令变换

**EN** 3. (For all tasks) Overall quality of generated image: Does the image contain significant technical errors that break composition (including style coherence and realism) or make it visually unappealing? For example, issues with impossible geometry, strange objects, garbled text, incorrect human anatomy (limbs bending the wrong way, wrong number of fingers) or unappealing aesthetics (distorted faces, large asymmetry in bodies)? Rating Label Description 0 Severe flaws , Very unappealing Obvious errors that strongly affect usability: Major physical or visual errors that most viewers would notice immediately, unbalanced composition, clashing colors, heavy jarringness 1 Some flaws, Somewhat unappealing Some errors that noticeably disrupt the image and jeopardize its usability regardless: Clear physical or visual errors that most viewers would eventually notice, the image isn’t an eye sore but something is wrong with its overall composition or color balance 2 Minor flaws, Somewhat appealing Small inaccuracies that are noticeable but are not strongly disruptive: Mostly plausible, but minor inconsistencies reduce believability, acceptable composition and color balance, but lacks artistic quality 3 No noticeable technical or logical flaws | Very appealing The image is free of noticeable technical errors: Fully coherent and physically plausible (if photorealistic, could be mistaken for a real photo; if stylized, maintains internal logic), strong composition, harmonious colors, and captivating style

**ZH** 3.（所有任务）生成图像的整体质量：图像是否存在破坏构图的显著技术错误（含风格一致性与真实感），或视觉上令人不适？例如不可能的几何结构、怪异物体、文字错乱、人体结构错误（肢体弯折方向错误、手指数量不对）或美感欠佳（面部扭曲、身体严重不对称）？ 评分 标签 说明 0 严重缺陷，非常不美观 明显错误严重影响可用性：多数观看者会立刻察觉的重大物理或视觉错误、构图失衡、色彩冲突、强烈违和感 1 有一定缺陷，略显不美观 明显干扰图像并危及其可用性的错误：多数观看者最终会察觉的清晰物理或视觉错误，图像虽不至于刺眼，但整体构图或色彩平衡存在问题 2 轻微缺陷，较为美观 可察觉但不具强破坏性的小瑕疵：大体合理，但细微不一致削弱可信度，构图与色彩平衡尚可，缺乏艺术品质 3 无明显技术或逻辑缺陷｜非常美观 图像无可见技术错误：完全自洽且物理上合理（若写实可被视为真实照片；若风格化则保持内在逻辑），构图考究、色彩和谐、风格动人

**EN** 4. (For task 3) Cross-generation image congruence: How well do the images relate to each other in a coherent way, maintaining consistency in recurring elements, style, and context, while allowing for appropriate variation when required? Rating Label Description 0 Very incoherent Many recurring elements change in unrealistic or unexplained ways, significantly breaking visual or thematic coherence 1 Rather incoherent Some recurring elements change in unrealistic or unexplained ways, breaking visual or thematic coherence 2 Mostly coherent Most recurring elements match, but there are noticeable mismatches or shifts that reduce cohesion 3 Full coherence Recurring elements, style, and context remain consistent where appropriate, and variations are clearly intentional and coherent

**ZH** 4.（任务 3）跨生成图像的一致性：各图像之间以连贯方式相互关联的程度如何？在需要时是否保持了复现元素、风格与语境的一致性，同时允许恰当的变化？ 评分 标签 说明 0 极不连贯 许多复现元素以不真实或无法解释的方式变化，显著破坏视觉或主题连贯性 1 较不连贯 部分复现元素以不真实或无法解释的方式变化，破坏视觉或主题连贯性 2 大体连贯 多数复现元素吻合，但存在明显的不匹配或偏移，削弱整体感 3 完全连贯 复现元素、风格与语境在恰当处保持一致，变化明显是有意为之且连贯的

**EN** 5. (For task 3) Generated Text-image alignment: How well does the generated text align with the visual content of the image(s), without contradictions or unsupported details? Rating Label Description 0 Very inconsistent Text contradicts or misrepresents key elements of the image(s) 1 Rather inconsistent Text aligns with some image content, but contains major mismatches or omissions 2 Mostly consistent Text aligns with most image content, but contains minor mismatches or omissions 3 Full consistency Text accurately and completely reflects the relevant details of the image(s) with no contradictions

**ZH** 5.（任务 3）生成文本与图像的对齐度：生成文本在多大程度上与图像的视觉内容吻合，不存在矛盾或无据的细节？ 评分 标签 说明 0 极不一致 文本与图像关键元素矛盾或歪曲 1 较不一致 文本与部分图像内容吻合，但存在重大不匹配或遗漏 2 大体一致 文本与多数图像内容吻合，但存在轻微不匹配或遗漏 3 完全一致 文本准确、完整地反映了图像的相关细节，无矛盾之处

**EN** 6. (For task 3) Technical quality of generated text: Does the text contain serious issues such as hallucinations, omissions, or logical errors that undermine accuracy or coherence? Is the tone of the generated text appropriate and congruent with the overall context, style, and intent of the generation task? Rating Label Description 0 Severe flaws (including tone) Contains clear hallucinations, major omissions, or serious logical inconsistencies; tone is clearly mismatched to the intended context or style, or contradicts the task’s purpose 1 Some flaws (including tone) Some factual gaps, unsupported claims, or reasoning errors: would be considered incorrect and incoherent overall; has some mismatches or inconsistencies in tone, and does not generally fit the context well 2 Minor flaws (including tone) Mostly correct and coherent, but has small factual gaps, minor unsupported claims, or slight reasoning errors; tone generally fits the context in spite of occasional minor mismatches 3 No noticeable flaws (including tone) Text is factually accurate, logically sound, and complete with no unsupported content; tone matches the intended context, style, and purpose throughout

**ZH** 6.（任务 3）生成文本的技术质量：文本是否存在幻觉、遗漏或逻辑错误等损害准确性或连贯性的严重问题？生成文本的语气是否与生成任务的整体语境、风格和意图相契合？ 评分 标签 说明 0 严重缺陷（含语气）存在明显幻觉、重大遗漏或严重逻辑矛盾；语气与预期语境或风格明显不符，或与任务目的相悖 1 有一定缺陷（含语气）存在部分事实空缺、无据主张或推理错误：整体上会被视为不正确且不连贯；语气有一定不匹配或不一致，总体上不太贴合语境 2 轻微缺陷（含语气）大体正确连贯，但存在轻微事实空缺、少量无据主张或轻微推理错误；尽管偶有细微不符，语气总体贴合语境 3 无明显缺陷（含语气）文本事实准确、逻辑严谨、完整且无无据内容；语气在全程中契合预期语境、风格与目的

**EN** 7. (For all tasks) Correctness of text rendering: (only if there are texts rendered in the image) Does the image render text correctly? For example, issues with misspellings, distorted text, and inconsistent capitalization? Rating Label Description 0 Major deviations | Many obvious errors The text is unreadable, severely distorted, or not rendered 1 Partial match | some errors The text rendered has major misspellings or distorted 2 mostly match | minor errors The text rendered is mostly correct, has minor misspellings or inconsistent capitalization 3 Full match | No noticeable error The rendered text is free of noticeable technical errors

**ZH** 7.（所有任务）文字渲染的正确性：（仅当图像中渲染了文字时）图像是否正确渲染了文字？例如是否存在拼写错误、文字扭曲、大小写不一致？ 评分 标签 说明 0 重大偏离｜大量明显错误 文字不可读、严重扭曲或未渲染 1 部分匹配｜有一定错误 渲染的文字存在重大拼写错误或扭曲 2 大体匹配｜轻微错误 渲染的文字大体正确，存在轻微拼写错误或大小写不一致 3 完全匹配｜无明显错误 渲染的文字无可见技术错误

**EN** For each pair, after answering the above pointwise evaluation questions, annotators provide their overall preference for answer A vs. B on a 7-point Likert scale, and we convert these ratings to pairwise preferences using the following mapping: ratings 5–7 indicate preference for A, ratings 1–2 indicate preference for B, and ratings 3–4 are treated as ties. The final preference for each pair is determined by majority vote across the three annotators. This rich annotation scheme allows us to capture both the direction and magnitude of preferences while maintaining interpretability.

**ZH** 每组数据在回答完上述逐点评测问题后，标注者在 7 点李克特量表上给出对答案 A 与 B 的总体偏好，我们按如下映射把评分转换为成对偏好：评分 5–7 表示偏好 A，评分 1–2 表示偏好 B，评分 3–4 视为平局。每组数据的最终偏好由三位标注者多数投票决定。这一丰富的标注方案使我们既能捕捉偏好的方向与强度，又保持了可解释性。

**EN** To ensure high-quality annotations, the annotator vendor applied a post-processing step designed to ensure accuracy, high quality, and oversight, blending automation with human review. Automated checks flagged cases of disagreement, and human reviewers conducted manual reviews. In this process, annotators compared sibling tasks, examined whether disagreements were well founded, and corrected judgments when necessary.

**ZH** 为保证标注质量，标注供应商实施了旨在确保准确性、高质量与可追溯的后处理环节，将自动检查与人工复核相结合。自动检查标记出分歧案例，人工复核员随后进行审查。在此过程中，标注者会比对同源任务、考察分歧是否有据，并在必要时修正判断。

**EN** B.2 Task 4

**ZH** B.2 任务 4

**EN** For the multimodal reasoning task, annotators are asked the following question with answer choices:

**ZH** 在多模态推理任务中，标注者需回答下列问题并作出选择：

**EN** Is the model’s reasoning / rationale for the answer correct and consistent? • Answer is correct and reasoning has no major errors, omissions, or inaccuracies affecting its correctness or completeness, with no additional improvement needed • Answer is correct and reasoning has no major errors, omissions, or inaccuracies affecting its correctness or completeness, but could benefit from minor improvements in reasoning • Answer is correct but reasoning has major errors, omissions, or inaccuracies affecting its correctness or completeness • Answer is correct, outputs did not include reasoning information • Answer is not correct / I cannot verify it

**ZH** 模型给出答案的推理／依据是否正确且自洽？ • 答案正确，且推理无影响其正确性或完整性的重大错误、遗漏或不准确之处，无需额外改进 • 答案正确，且推理无影响其正确性或完整性的重大错误、遗漏或不准确之处，但推理可小幅改进 • 答案正确，但推理存在影响其正确性或完整性的重大错误、遗漏或不准确之处 • 答案正确，输出未包含推理信息 • 答案不正确／我无法验证

<!-- [原子块 · img]  -->

**EN** Figure 7: Annotation interface for the multimodal reasoning tasks.

**ZH** 图 7：多模态推理任务的标注界面。

**EN** Figure 7 shows the annotation interface for MMRB2 multimodal reasoning tasks. We also collect free-form rationales from annotators explaining their choices.

**ZH** 图 7 展示了 MMRB2 多模态推理任务的标注界面。我们还收集了标注者解释其选择的自由文本理由。

**EN** Pair construction. We construct preference pairs from annotated model responses. For the human-preferred sample of each pair, we select model responses in which all three human annotators agree that the reasoning contains no major errors and the model answer is correct (i.e., all annotators select either the first or second answer choice above). For the non-preferred sample of each pair, we utilize two kinds of responses: Correct answer, incorrect reasoning, where the model answer is correct but all three annotators consider the reasoning to contain major errors (the third answer choice above), and Incorrect answer, with reasoning, where the model answer is incorrect and some form of reasoning is included. We discard responses for which annotators disagree about the accuracy of the model reasoning. For each pair, the two model responses may share the same modality (both text-only or both image+text) or be a combination. No model response is duplicated across pairs. Table 11 shows the breakdown of pairs across modalities and pair types.

**ZH** 偏好对构造。我们基于已标注的模型响应构造偏好对。偏好对中的优选样本取自三位标注者一致认定推理无重大错误且模型作答正确的响应（即全体标注者选择上述第一或第二项）；淘汰样本则取自两类响应：其一是“答案正确、推理有误”，即模型答案正确但三位标注者均认为推理存在重大错误（上述第三项）；其二是“答案错误、含推理”，即模型答案错误但包含某种形式的推理。若标注者对模型推理的准确性存在分歧，该响应予以丢弃。每组偏好对的两条响应模态可以相同（同为纯文本或同为图像+文本），也可以不同。任何模型响应都不会在不同偏好对中重复出现。表 11 给出按模态与偏好对类型拆解的样本分布。

<!-- [原子块 · table] Pair Type Same Modality Mixed Modality Text Image+Text Pref: Text Not Pref: Image+Text Pref: Image+Text Not Pref: Text Correct reason vs. Incorrect reason 112 115 53 44 Correct answer vs. Incorrect an -->

**EN** Table 11: Number of samples for each reasoning pair type and modality combination.

**ZH** 表 11：各推理偏好对类型与模态组合的样本数。

**EN** Appendix C Details for Prompts, Response Generation, and MLLM-as-a-judge

**ZH** 附录 C 提示词、响应生成与 MLLM 评判器的细节

**EN** C.1 Task Prompts

**ZH** C.1 任务提示词

**EN** Here we provide additional details for the newly synthesized tasks in MMRB2.

**ZH** 此处给出 MMRB2 中新建合成任务的补充细节。

**EN** Text-Heavy Editing. Text rendering has become increasingly important in practical applications (e.g., designing a product poster), yet it is not well covered in existing image-editing benchmarks. To construct this task, we first curate a set of object-centric images. We collect 200 real images from DreamBench++ (Peng et al., 2025), and additionally create 500 synthetic object images using state-of-the-art text-to-image models GPT-Image (OpenAI, 2025c) and Gemini-2.5-Flash-Image (Google DeepMind, 2025a). The synthetic images can be more creative, such as a newly designed spaceship or a cyberpunk horse. We manually inspect all images to ensure that they are of high quality.

**ZH** 文本密集编辑。文字渲染在实用场景中日益重要（如设计产品海报），但既有图像编辑基准对其覆盖不足。为构建该任务，我们首先整理了一组以物体为中心的图像：从 DreamBench++（Peng et al., 2025）收集 200 张真实图像，并用最先进的文生图模型 GPT-Image（OpenAI, 2025c）与 Gemini-2.5-Flash-Image（Google DeepMind, 2025a）额外生成 500 张合成物体图像。合成图像可以更具创意，例如一艘新设计的飞船或一匹赛博朋克风格的马。我们人工检查了全部图像以确保质量。

**EN** Given an object image, we prompt GPT-4o (OpenAI, 2024) to generate an editing instruction that heavily relies on text rendering, using the following prompt:

**ZH** 给定一张物体图像，我们用如下提示词让 GPT-4o（OpenAI, 2024）生成高度依赖文字渲染的编辑指令：

**EN** The final MMRB2 image-editing benchmark contains 114 text-heavy editing examples.

**ZH** 最终的 MMRB2 图像编辑基准包含 114 个文本密集编辑样例。

**EN** Multi-Image Editing. Recent models such as Gemini 2.5 Flash Image support taking multiple images as input for editing. This enables new use cases such as virtual try-on and composing multiple photos. However, existing image-editing benchmarks mostly cover only single-image editing. We therefore synthesize new multi-image editing examples. Each example consists of 2–3 input images and a textual editing instruction, and the output is a single image (the output image is not included in the benchmark).

**ZH** 多图编辑。Gemini 2.5 Flash Image 等近期模型支持以多张图像作为编辑输入，由此催生了虚拟试穿、多照片合成等新用例。但既有图像编辑基准大多只覆盖单图编辑。为此我们合成了新的多图编辑样例：每个样例包含 2–3 张输入图像与一条文本编辑指令，输出为单张图像（输出图像不计入基准）。

**EN** We generate the task prompts with our interleaved agents (§C.2), which can produce interleaved text and image responses given arbitrary multimodal prompts. We consider multiple settings for this task. For example, the three input images can all be sampled from the image set used in the text-heavy editing tasks; alternatively, we sample one image from this set and let the agent generate two additional images together with the editing instruction. Each of the 2–3 input images can be either real or synthetic. Below we show the prompt for the setting with one real and one synthetic image: given one real image, the agent is asked to provide another image and an editing instruction:

**ZH** 我们用交错智能体（§C.2）生成任务提示词，该智能体可在给定任意多模态提示词时产出图文交错的响应。我们为该任务考虑多种设置：例如三张输入图像可全部取自文本密集编辑任务所用的图像集；或者从该集合中取一张，再让智能体自行生成另外两张图像及编辑指令。2–3 张输入图像中的每一张都可为真实或合成。下面给出“一张真实图像 + 一张合成图像”设置的提示词：给定一张真实图像，要求智能体提供另一张图像及编辑指令：

**EN** Altogether, there are 178 multi-image editing examples in the MMRB2 image-editing task, among which 79 have 2 input images and 99 have 3 input images.

**ZH** MMRB2 图像编辑任务中共有 178 个多图编辑样例，其中 79 个含 2 张输入图像，99 个含 3 张输入图像。

**EN** C.2 Response generation

**ZH** C.2 响应生成

**EN** All responses are stored in a unified format that supports interleaved text and image content. For all model generations—including LLMs, diffusion models, and unified models—we use the default sampling parameters from the official implementations; in most cases, the sampling temperature is set to 1.0.

**ZH** 全部响应以统一格式存储，支持图文交错内容。对大语言模型、扩散模型与统一模型在内的所有生成，我们均采用官方实现中的默认采样参数；多数情况下采样温度设为 1.0。

**EN** Agents. Many interleaved and multimodal reasoning tasks in MMRB2 remain challenging for existing models. For example, we observe that Gemini 2.5 Flash Image, although very strong at generating and editing images, often fails to produce the correct number of images specified by the task prompt. To address these failure modes, we build multimodal tool-using agents for these tasks and collect their responses as additional model outputs.

**ZH** 智能体。MMRB2 中许多交错与多模态推理任务对现有模型仍很困难。例如我们观察到，Gemini 2.5 Flash Image 虽然生成与编辑图像的能力很强，却常无法按提示词要求产出正确数量的图像。为应对这些失效模式，我们为这些任务构建了多模态工具调用智能体，并采集其响应作为额外的模型输出。

**EN** Specifically, we follow the implementation of Visual Sketchpad (Hu et al., 2024), in which an LLM can write Python code and call tools to generate or edit images. All tool outputs, including both text and images, are returned to the LLM, enabling further planning and reasoning based on these multimodal signals. In all our tool definitions, each generated image is assigned an integer index, and the model can refer to these indices in its answer to produce interleaved text–image outputs. We use GPT-4.1 (OpenAI, 2025a), o3 (OpenAI, 2025d), and GPT-5 (OpenAI, 2025b) as the LLM backbone in these experiments.

**ZH** 具体地，我们沿用 Visual Sketchpad（Hu et al., 2024）的实现，让大语言模型编写 Python 代码并调用工具生成或编辑图像。全部工具输出（含文本与图像）都返回给大语言模型，使其能基于这些多模态信号继续规划与推理。在我们所有的工具定义中，每张生成的图像都被赋予一个整数索引，模型可在回答中引用这些索引以产生图文交错输出。实验中我们使用 GPT-4.1（OpenAI, 2025a）、o3（OpenAI, 2025d）与 GPT-5（OpenAI, 2025b）作为大语言模型骨干。

**EN** We instantiate multiple agent variants that differ in their image-generation components so that MMRB2 can cover a wide variety of interleaved outputs. For GPT-FLUX-agent, we use FLUX.1-dev as the text-to-image tool and FLUX.1-Kontext for image editing (Labs et al., 2025); for GPT-Imagen-agent, we use Imagen-4-Ultra (Google DeepMind, 2025d) as the text-to-image tool and Imagen-3-Edit (Baldridge et al., 2024) as the editing tool; for GPT-GPT-Image-Agent, we use GPT-Image-1 (OpenAI, 2025c) for both text-to-image generation and image editing; and for GPT-Gemini-Agent, we use Gemini 2.5 Flash Image (Google DeepMind, 2025a) as the image tool. The tool definitions are as follows.

**ZH** 我们实例化了多个图像生成组件各异的智能体变体，使 MMRB2 能覆盖丰富多样的交错输出：GPT-FLUX-agent 使用 FLUX.1-dev 作为文生图工具、FLUX.1-Kontext 作为图像编辑工具（Labs et al., 2025）；GPT-Imagen-agent 使用 Imagen-4-Ultra（Google DeepMind, 2025d）作为文生图工具、Imagen-3-Edit（Baldridge et al., 2024）作为编辑工具；GPT-GPT-Image-Agent 使用 GPT-Image-1（OpenAI, 2025c）同时完成文生图与图像编辑；GPT-Gemini-Agent 使用 Gemini 2.5 Flash Image（Google DeepMind, 2025a）作为图像工具。工具定义如下。

**EN** For interleaved tasks, we use the following system prompt. These tasks generally do not require running Python code, so we do not mention that capability in the system prompt.

**ZH** 交错任务使用如下系统提示词。这类任务通常不需要运行 Python 代码，因此系统提示词中未提及该能力。

**EN** For the multimodal reasoning task, we use the following system prompt.

**ZH** 多模态推理任务使用如下系统提示词。

**EN** We set the maximum number of turns for these agents to 15. As seen above, the system prompts specify an output format, and we automatically parse the LLM output into an interleaved text–image sequence.

**ZH** 我们把这些智能体的最大轮数设为 15。如上所示，系统提示词规定了输出格式，我们会自动把大语言模型的输出解析为图文交错序列。

**EN** C.3 MLLM-as-a-judge details

**ZH** C.3 MLLM 评判器细节

**EN** For the image-generation task, we use the following system prompt for the MLLM-as-a judge.

**ZH** 图像生成任务中，MLLM 评判器使用如下系统提示词。

**EN** For the image-editing task, we use the following system prompt for the MLLM-as-a judge.

**ZH** 图像编辑任务中，MLLM 评判器使用如下系统提示词。

**EN** For the interleaved generation task, we use the following system prompt for the MLLM-as-a judge.

**ZH** 交错生成任务中，MLLM 评判器使用如下系统提示词。

**EN** For the reasoning task, we use the following system prompt for the MLLM-as-a judge.

**ZH** 推理任务中，MLLM 评判器使用如下系统提示词。

**EN** As shown, these prompts are very close to the rubrics that were used for human annotations.

**ZH** 如所示，这些提示词与人工标注所用的评分准则高度接近。

**EN** Appendix D Limitations and Future Directions

**ZH** 附录 D 局限与未来方向

**EN** MMRB2 is designed as a first comprehensive benchmark for omni-model reward evaluation in text–image settings. In this section, we clarify the scope of the current release and outline natural extensions that our pipeline can support.

**ZH** MMRB2 被设计为首个面向图文场景下全模态奖励评测的综合基准。本节说明当前版本的覆盖范围，并勾勒该流水线可支持的自然扩展方向。

**EN** Scope and focus. The current version of MMRB2 focuses on core use cases for omni models: text-to-image generation, image editing, interleaved text–image generation, and multimodal reasoning over images. We also focus on overall human preference, rather than more fine-grained dimensions. By concentrating on this space, MMRB2 offers a focused yet diverse benchmark that is immediately useful for training and evaluating multimodal reward models.

**ZH** 范围与重心。当前版本的 MMRB2 聚焦全模态模型的核心用例：文生图生成、图像编辑、图文交错生成，以及基于图像的多模态推理；同时关注整体人类偏好，而非更细粒度的维度。通过聚焦这一空间，MMRB2 提供了一个既专注又多样的基准，可直接用于多模态奖励模型的训练与评测。

**EN** Modalities and task formats. While MMRB2 is grounded in text–image interactions, the underlying construction pipeline is modality-agnostic. The same recipe of prompt curation, multi-model candidate generation, ensemble filtering, and expert preference collection can be applied to additional modalities such as video, audio, or 3D content as these use cases and tools become more standardized. Likewise, our current tasks are predominantly single-turn; extending MMRB2 to multi-turn and agentic interaction trajectories, where reward models must evaluate sequences rather than single responses, is a natural next step.

**ZH** 模态与任务形式。尽管 MMRB2 立足于图文交互，其底层构建流水线并不绑定特定模态。同一套流程——提示词策划、多模型候选生成、集成过滤、专家偏好采集——可随相关用例与工具的标准化推广到视频、音频或三维内容等更多模态。同样地，当前任务以单轮为主；把 MMRB2 扩展到多轮与智能体交互轨迹，要求奖励模型评测序列而非单条响应，是自然的下一步。

**EN** Data sources and coverage. Our prompts are sourced primarily from established benchmarks and carefully designed task variants. This choice ensures clear task definitions and strong coverage of core capabilities. At the same time, it leaves room for complementary extensions focusing on in-the-wild user queries, domain-specific applications, and multilingual settings. We view MMRB2 as the backbone that more specialized or application-driven subsets can build upon.

**ZH** 数据来源与覆盖。我们的提示词主要取自成熟基准与精心设计的任务变体，这一选择保证了任务定义清晰、核心能力覆盖充分。同时也为互补性扩展留出了空间，例如面向真实用户查询、特定领域应用与多语言设置。我们把 MMRB2 视为一个主干，更专门或更贴近应用的子集可在其之上构建。

**EN** Evaluation dimensions. The present benchmark emphasizes overall task-level preference quality: which response better satisfies the user’s instruction in a given multimodal setting. Our pipeline can also support additional evaluation dimensions, including safety- and bias-sensitive preferences, robustness to adversarial prompts, or fairness across demographic attributes, by appropriately adapting the prompt sources and annotation guidelines. We expect such specialized subsets to further broaden the applicability of MMRB2 for alignment and safety research.

**ZH** 评测维度。本基准侧重任务层面的整体偏好质量：即在给定多模态场景下，哪条响应更好地满足了用户指令。通过适当调整提示词来源与标注指南，我们的流水线也可支持更多评测维度，包括安全与偏见敏感的偏好、对对抗性提示词的鲁棒性，或跨人口属性的公平性。我们预期这类专门子集将进一步拓宽 MMRB2 在对齐与安全研究中的适用范围。

**EN** Evolving judges and benchmarks. Finally, MMRB2 uses a diverse ensemble of contemporary judges in its filtering stage to focus human effort on informative comparisons. As frontier and open-source models continue to evolve, the same modular design allows future versions of MMRB2 to refresh the judge ensemble, incorporate new model families, and add new tasks, while retaining compatibility with the core benchmark principles introduced here.

**ZH** 不断演进的评判器与基准。最后，MMRB2 在过滤阶段使用了一组多样化的当代评判器集成，以使人力集中于信息量大的对比。随着前沿与开源模型持续演进，同样的模块化设计使 MMRB2 未来版本可以刷新评判器集成、纳入新的模型族、增加新任务，同时保持与本文所提出的核心基准原则兼容。

**EN** Appendix E Examples

**ZH** 附录 E 示例

**EN** Here we show two examples from each task in MMRB2. For each task prompt, there is a Response A and a Response B. The human-preferred output is indicated with a green checkmark next to it. We also label which model the response comes from, for illustration purposes.

**ZH** 此处展示 MMRB2 每个任务的两个示例。每个任务提示词对应响应 A 与响应 B，人类偏好的输出旁标有绿色对勾。我们也标注了每条响应的来源模型，便于说明。

<!-- [原子块 · img]  -->

**EN** Figure 8: An example of MMRB2 text-to-image task. Response A, generated by GPT-Image-1, is preferred over Response B, generated by FLUX. The rationale is that Response B is not a railway underpass.

**ZH** 图 8：MMRB2 文生图任务示例。由 GPT-Image-1 生成的响应 A 优于由 FLUX 生成的响应 B，理由是响应 B 并非铁路下穿通道。

<!-- [原子块 · img]  -->

**EN** Figure 9: An example of MMRB2 text-to-image task. Responses A and B are both generated by Gemini 2.5 Flash Image, while B is preferred over A. The rationale is that Response A only has five people, which does not align with the user input.

**ZH** 图 9：MMRB2 文生图任务示例。响应 A 与 B 均由 Gemini 2.5 Flash Image 生成，而 B 优于 A，理由是响应 A 只有五个人，与用户输入不符。

<!-- [原子块 · img]  -->

**EN** Figure 10: An example of MMRB2 image-editing task. Response A, generated by Gemini 2.5 Flash Image, is preferred over Response B, generated by GPT-Image. The rationale is that many important texts are missing in Response B. Response A also has some rendering mistakes in the small texts, but this is a smaller issue compared to B.

**ZH** 图 10：MMRB2 图像编辑任务示例。由 Gemini 2.5 Flash Image 生成的响应 A 优于由 GPT-Image 生成的响应 B，理由是响应 B 缺失了大量重要文字。响应 A 在小字号文字上也有些渲染错误，但与 B 相比问题较轻。

<!-- [原子块 · img]  -->

**EN** Figure 11: An example of MMRB2 image-editing task. Responses A and B are both generated by Gemini 2.0 Flash Image, while B is preferred over A. The rationale is that Response B follows the instruction better, and the backpack is more “anime-styled.”

**ZH** 图 11：MMRB2 图像编辑任务示例。响应 A 与 B 均由 Gemini 2.0 Flash Image 生成，而 B 优于 A，理由是响应 B 更好地遵循了指令，且背包更具“动漫风格”。

<!-- [原子块 · img]  -->

**EN** Figure 12: An example of MMRB2 interleaved task. Responses A and B are both generated by the agent with GPT-Image, while B is preferred over A. The rationale is that Response B better follows the instruction and is more consistent with the original image.

**ZH** 图 12：MMRB2 交错任务示例。响应 A 与 B 均由以 GPT-Image 为组件的智能体生成，而 B 优于 A，理由是响应 B 更好地遵循了指令，且与原图更一致。

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

**EN** Figure 13: An example of MMRB2 interleaved task. Responses A and B are both generated by Gemini 2.5 Flash Image, while A is preferred over B. The rationale is that in Response B the cat is barely changed across the images, while in A the cats are more natural while remaining consistent.

**ZH** 图 13：MMRB2 交错任务示例。响应 A 与 B 均由 Gemini 2.5 Flash Image 生成，而 A 优于 B，理由是响应 B 中的猫在各张图像间几乎没有变化，而 A 中的猫更自然且保持一致。

<!-- [原子块 · img]  -->

**EN** Figure 14: An example of MMRB2 multimodal reasoning task. Response A, generated by Gemini 2.5 Pro, is preferred over Response B, which is generated by GPT-4.1. Response A has correct reasoning and answer, while Response B’s reasoning has apparent problems. For example, “2nd circle: a veritcal and a diaglonal line” is incorrect.

**ZH** 图 14：MMRB2 多模态推理任务示例。由 Gemini 2.5 Pro 生成的响应 A 优于由 GPT-4.1 生成的响应 B。响应 A 的推理与答案均正确，而响应 B 的推理存在明显问题，例如“第 2 个圆：一条竖线和一条斜线”就是错误的。

<!-- [原子块 · img]  -->

<!-- [原子块 · img]  -->

**EN** Figure 15: An example of MMRB2 multimodal reasoning task. Responses A and B are both generated by sketchpad agents. A uses GPT-5 as the LLM backbone, and B uses o3 as the backbone. A is preferred over B. The rationale is that B does not contain analysis for the third image, so the reasoning process is incomplete.

**ZH** 图 15：MMRB2 多模态推理任务示例。响应 A 与 B 均由 sketchpad 智能体生成，A 以 GPT-5、B 以 o3 作为大语言模型骨干，A 优于 B。理由是 B 未包含对第三张图像的分析，推理过程不完整。
