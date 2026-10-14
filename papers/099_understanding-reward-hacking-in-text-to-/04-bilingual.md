# 理解文本到图像强化学习中的奖励黑客

> 原标题：Understanding Reward Hacking in Text-to-Image Reinforcement Learning
> 作者：Yunqi Hong, Kuei-Chun Kao, Hengguang Zhou, Cho-Jui Hsieh · arXiv:2601.03468 · 2026-01-06

<!-- [原子块 · verbatim] Understanding Reward Hacking in Text-to-Image Reinforcement Learning -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] Reinforcement learning (RL) has become a standard approach for post-training large language models and, more recently, for improving image generation models, which uses reward functions to enhance gen -->

<!-- [原子块 · verbatim] In this work, we systematically analyze reward hacking behaviors in text-to-image (T2I) RL post-training. We investigate how both aesthetic/human preference rewards and prompt-image consistency reward -->

<!-- [原子块 · verbatim] Experiments demonstrate that incorporating our artifact reward significantly improves visual realism and reduces reward hacking across multiple T2I RL setups, demonstrating the effectiveness of lightw -->

**EN** 1 Introduction

**ZH** 1 引言

**EN** The use of reinforcement learning (RL) has proven highly effective for post-training large language models (LLMs), enabling stronger alignment with human preferences through methods such as reinforcement learning from human feedback (RLHF) 27 or more recently improving prediction accuracy via reinforcement learning with verifiable feedback (RLVF) 31; 13; 15. This success has motivated a growing interest in exploring RL-based fine-tuning for image generation tasks 18; 10; 47; 5; 39; 44.

**ZH** 强化学习（RL）已被证明在后训练大语言模型（LLM）上极为有效：借助基于人类反馈的强化学习（RLHF）27 等方法，模型能更好地与人类偏好对齐；近来又可通过带可验证反馈的强化学习（RLVF）31; 13; 15 提升预测准确率。这一成功激发了人们对基于 RL 的微调在图像生成任务上应用的浓厚兴趣 18; 10; 47; 5; 39; 44。

**EN** To guide the optimization of generative models, various types of reward functions have been proposed. Architecturally, many of these rewards are built on vision-language encoders such as CLIP or BLIP 42; 19; 43. Others leverage multimodal LLMs, either through direct scoring 20; 38; 47, additional prediction heads 50, or token-level probability signals 23; 40; 46; 14; 41; 22). A third category relies on external perception tools such as object detectors 25; 6; 51. Functionally, reward models are typically designed to measure aesthetic or perceptual quality 30; 46; 45, human preference alignment 42; 19; 43; 38, and prompt-image consistency 14; 22; 25; 23.

**ZH** 为引导生成模型的优化，研究者提出了各类奖励函数。在架构上，其中许多奖励建立在 CLIP 或 BLIP 等视觉-语言编码器之上 42; 19; 43；另一些则利用多模态大语言模型，或通过直接打分 20; 38; 47，或附加预测头 50，或借助词元级概率信号 23; 40; 46; 14; 41; 22。第三类依赖外部感知工具，例如目标检测器 25; 6; 51。在功能上，奖励模型通常被设计为衡量美学或感知质量 30; 46; 45、人类偏好对齐 42; 19; 43; 38，以及提示-图像一致性 14; 22; 25; 23。

**EN** However, unlike textual domains where verifiable signals (e.g., correctness or factuality) can be obtained, reward functions for visual generation are often non-verifiable imperfect proxies for human preferences 49; 24. Such imperfect reward design can inadvertently encourage models to exploit weaknesses in the reward signal rather than genuinely improving visual generation quality, which is a phenomenon known as reward hacking 1; 11; 34; 8. As a result, fine-tuned models may produce visually implausible or low-quality images that nonetheless receive high reward scores.

**ZH** 然而，与文本领域不同——后者可获得可验证信号（如正确性或事实性）——视觉生成的奖励函数往往是不可验证的、对人类偏好的不完美代理 49; 24。这种不完善的奖励设计会无意中鼓励模型去利用奖励信号的弱点，而非真正提升视觉生成质量，这一现象即所谓的奖励黑客（reward hacking）1; 11; 34; 8。结果是，微调后的模型可能生成视觉上不合理或低质量的图像，却依然获得很高的奖励分数。

**EN** In this work, we conduct the first systematic analysis of reward hacking behaviors in text-to-image (T2I) RL post-training. We investigate how different types of reward functions individually contribute to reward hacking, including those designed for aesthetics or human preference and those enforcing prompt-image consistency. Although ensembling multiple rewards partially mitigate this issue, it cannot fully prevent reward exploitation. Across all settings, we identify a universal pattern of reward hacking: the generation of unrealistic visual artifacts that nevertheless receive high reward scores. While prior studies have occasionally reported instances of reward exploitation or proposed regularization techniques to mitigate it 8; 49; 32; 24, ours is the first to systematically characterize how different reward types induce specific hacking behaviors and to identify their common pattern of artifact generation.

**ZH** 本文首次对文本到图像（T2I）强化学习后训练中的奖励黑客行为展开系统分析。我们考察各类奖励函数如何各自导致奖励黑客，既包括面向美学或人类偏好设计的奖励，也包括强制提示-图像一致性的奖励。虽然集成多个奖励能部分缓解这一问题，却无法完全阻止奖励被利用。在所有设置下，我们都识别出一种普遍的奖励黑客模式：生成带有不真实视觉伪影、却仍获得高奖励分数的图像。此前研究虽偶有报告奖励被利用的实例，或提出缓解它的正则化技术 8; 49; 32; 24，但本文首次系统刻画了不同奖励类型如何诱发特定的黑客行为，并识别出它们共同的伪影生成模式。

**EN** To address this reward hacking issue, we propose a lightweight and adaptive artifact reward model that can be seamlessly integrated into existing T2I RL pipelines. Our approach requires only a small dataset (approximately 200 samples) of model-generated images consisting of both artifact-free and artifact-containing examples. By using an LLM-based backbone, we automatically optimize a textual prompt that discriminates between these two categories, so as to assign higher scores to artifact-free images and lower scores to those containing artifacts.

**ZH** 针对这一奖励黑客问题，我们提出一种轻量、自适应的伪影奖励模型，可无缝接入现有的 T2I 强化学习流程。我们的方法只需一个小型数据集（约 200 个样本），由模型生成的图像组成，其中既含无伪影样本，也含含伪影样本。借助基于大语言模型的骨干网络，我们自动优化一条文本提示，用以区分这两类图像，从而给无伪影图像打高分、给含伪影图像打低分。

**EN** Extensive experiments demonstrate that using our artifact reward as a regularizer for existing reward models consistently improves visual realism and reduces reward hacking across multiple T2I RL setups. Evaluations on two benchmarks, WISE 26 and LLM4LLM 37, show that reliably boosts realism, consistency, and semantic alignment across all training configurations.

**ZH** 大量实验表明，把我们的伪影奖励用作现有奖励模型的正则项，能在多种 T2I 强化学习设置下稳定提升视觉真实感并减少奖励黑客。在 WISE 26 与 LLM4LLM 37 两个基准上的评测显示，该方法在所有训练配置下都能可靠地提升真实感、一致性与语义对齐。

**EN** 2 Related Work

**ZH** 2 相关工作

**EN** 2.1 Evaluation Metrics for T2I Generation

**ZH** 2.1 T2I 生成的评测指标

**EN** Unlike domains such as mathematics or programming, where ground-truth answers can serve as objective reward signals, evaluating the quality of generated images is inherently more complex and multi-dimensional. It may depend on factors such as aesthetic appeal, semantic alignment with the prompt, and overall visual realism, leading to a diverse landscape of reward functions and evaluation metrics.

**ZH** 与数学或编程等领域不同——那些领域的真值答案可以充当客观奖励信号——评价生成图像的质量本质上更为复杂、维度更多。它可能取决于美学吸引力、与提示的语义对齐、整体视觉真实感等因素，由此催生了形态各异的奖励函数与评测指标。

**EN** A major class of reward models is built upon vision-language encoders such as CLIP 29 and BLIP 21. HPSv2 42 and PickScore 19 fine-tune CLIP on human-preference datasets to predict visual quality based on human aesthetic appeal and preference. Aesthetic Score 30 predicts image aesthetics using a feedforward neural network over CLIP features. ImageReward 43 is built on BLIP to estimate preference scores via cross-attention between image and text features.

**ZH** 一大类奖励模型建立在 CLIP 29 与 BLIP 21 等视觉-语言编码器之上。HPSv2 42 与 PickScore 19 在人类偏好数据集上微调 CLIP，以依据人类美学吸引力与偏好预测视觉质量。Aesthetic Score 30 用前馈神经网络在 CLIP 特征之上预测图像美学。ImageReward 43 建立在 BLIP 之上，通过图像与文本特征之间的交叉注意力估计偏好分数。

**EN** With the emergence of MLLMs that exhibit strong visual reasoning abilities, many works have explored using them as image evaluators. Davidsonian Scene Graph 7 evaluates image-prompt consistency by answering questions corresponding to the prompt based on the generated image. VIEScore 20 utilizes the general knowledge of MLLMs to evaluate conditional image generation without additional finetuning. EvalAlign 35 finetunes MLLMs to evaluate image faithfulness and text-image alignment. UnifiedReward 38 finetunes MLLMs to directly output scalar image scores through comprehensive analyses. LLaVA-Reward 50 employs the Bradley-Terry objective to train an MLLM evaluator using pairwise preference data. Other works, such as Q-Align 40, VQAScore 23, DeQA 46, finetuned ORM 14, and RewardDance 41, estimate image quality based on the token probabilities of specific answer tokens, each emphasizing different evaluation aspects depending on their datasets and design choices.

**ZH** 随着具备强大视觉推理能力的多模态大语言模型（MLLM）出现，许多工作探索将其用作图像评估器。Davidsonian Scene Graph 7 通过基于生成图像回答与提示对应的问题来评估图像-提示一致性。VIEScore 20 利用 MLLM 的通用知识评估条件图像生成，无需额外微调。EvalAlign 35 微调 MLLM 以评估图像忠实度与文图对齐。UnifiedReward 38 微调 MLLM，使其通过综合分析直接输出标量图像分数。LLaVA-Reward 50 采用 Bradley-Terry 目标，用成对偏好数据训练 MLLM 评估器。Q-Align 40、VQAScore 23、DeQA 46、微调版 ORM 14 与 RewardDance 41 等工作则依据特定答案词元的词元概率估计图像质量，各自的侧重点随数据集与设计选择而不同。

**EN** 2.2 Existing Rewards for T2I Post-Training

**ZH** 2.2 T2I 后训练的现有奖励

**EN** Gradient-based finetuning methods.

**ZH** 基于梯度的微调方法。

**EN** ImageReward 43 introduces Reward Feedback Learning (ReFL), a direct optimization approach that uses gradients from reward models, to finetune diffusion models. DRaFT 8 further analyzes how rewards such as HPSv2 42 and PickScore 19 influence model behavior when applied through differentiable optimization. ROCM 32 compared training outcomes using different reward functions, including PickScore 19, HPSv2 42, CLIPScore 16, and Aesthetic Score 30, to study their individual effects.

**ZH** ImageReward 43 提出了奖励反馈学习（ReFL）——一种利用奖励模型梯度微调扩散模型的直接优化方法。DRaFT 8 进一步分析了 HPSv2 42 与 PickScore 19 等奖励在通过可微分优化施加时对模型行为的影响。ROCM 32 比较了使用 PickScore 19、HPSv2 42、CLIPScore 16 与 Aesthetic Score 30 等不同奖励函数的训练结果，以考察各自的效果。

**EN** RL-based optimization.

**ZH** 基于 RL 的优化。

**EN** Recent progress in RL for LLMs has renewed interest in applying RL-based finetuning to T2I models. Existing methods primarily differ in the choice of reward functions and optimization strategies.

**ZH** 大语言模型强化学习的最新进展，重新激发了把基于 RL 的微调应用于 T2I 模型的兴趣。现有方法的主要差异在于奖励函数与优化策略的选择。

**EN** RL Diffusion 49 adopts REINFORCE-style policy gradients to train diffusion models with various reward functions, including ImageReward 43 for human preference, UniDet 51 for compositionality, and a distribution-based statistical parity reward for diversity and fairness. DDPO 3 employs Aesthetic Score 30 and BERTScore 48, which measures the semantic similarity between the prompt and VLM-generated image captions, as reward signals. DanceGRPO 44 finetunes diffusion models with HPS-v2.1 42 and CLIP 29 rewards, while Flow-GRPO 24 improves the flow-matching models by using a combination of compositionality (GenEval 12) and human preference (PickScore 19) rewards. T2I-R1 18 ensembles multiple rewards, including HPS 42, Grounding DINO 25, a VQA model 36, and the finetuned ORM 14. AR-GRPO 47 incorporates HPS-v2.1 42 and CLIP 29 for conditional reward, MANIQA 45 for image quality, and prompting Qwen2.5-VL-3B-Instruct 2 for realism.

**ZH** RL Diffusion 49 采用 REINFORCE 风格的策略梯度，用多种奖励函数训练扩散模型，包括面向人类偏好的 ImageReward 43、面向组合性的 UniDet 51，以及面向多样性与公平性的基于分布的统计均等奖励。DDPO 3 使用 Aesthetic Score 30 与 BERTScore 48 作为奖励信号，后者衡量提示与视觉语言模型生成的图像描述之间的语义相似度。DanceGRPO 44 用 HPS-v2.1 42 与 CLIP 29 奖励微调扩散模型；Flow-GRPO 24 则组合使用组合性奖励（GenEval 12）与人类偏好奖励（PickScore 19）来改进流匹配模型。T2I-R1 18 集成了 HPS 42、Grounding DINO 25、一个 VQA 模型 36 以及微调版 ORM 14 等多个奖励。AR-GRPO 47 引入 HPS-v2.1 42 与 CLIP 29 作为条件奖励、MANIQA 45 作为图像质量奖励，并提示 Qwen2.5-VL-3B-Instruct 2 评估真实感。

**EN** Overall, existing T2I reward functions can be broadly categorized into three groups:

**ZH** 总体而言，现有的 T2I 奖励函数可大致归为三类：

**EN** • Human preference rewards such as HPS 42, PickScore 19, and ImageReward 43;

**ZH** • 人类偏好奖励，如 HPS 42、PickScore 19 与 ImageReward 43；

**EN** • Compositionality rewards such as Grounding DINO 25;

**ZH** • 组合性奖励，如 Grounding DINO 25；

**EN** • MLLM-based rewards derived from visual question answering or image scoring models 23; 14; 46; 38.

**ZH** • 基于 MLLM 的奖励，源自视觉问答或图像打分模型 23; 14; 46; 38。

**EN** Our work focuses on analyzing model behaviors when trained with rewards from these categories.

**ZH** 我们的工作聚焦于分析模型在使用这几类奖励训练时的行为。

**EN** 2.3 Reward Hacking in T2I RL training

**ZH** 2.3 T2I 强化学习训练中的奖励黑客

**EN** Although none of the existing work provides a detailed discussion and systematic analysis of reward hacking in T2I post-training, several studies have briefly discussed instances of reward hacking in their training experiments. DRaFT 8 reports that finetuned models sometimes lose diversity and produce reward-specific visual patterns. RL Diffusion 49 hypothesizes that gradient-based optimization methods (i.e. ReFL 43 and DRaFT 8) are more susceptible to reward hacking because they directly access reward gradients, and thus proposes an RL-based alternative to improve robustness. ROCM 32 introduces distributional regularization to stabilize training and mitigate reward exploitation. Flow-GRPO 24 uses KL regularization for similar purposes.

**ZH** 尽管现有工作都未对 T2I 后训练中的奖励黑客做过详细讨论与系统分析，若干研究已在训练实验中简要提及奖励黑客的实例。DRaFT 8 报告说，微调后的模型有时会丧失多样性并产生与特定奖励相关的视觉模式。RL Diffusion 49 假设基于梯度的优化方法（即 ReFL 43 与 DRaFT 8）更容易受到奖励黑客影响，因为它们可直接获取奖励梯度，并据此提出一种更鲁棒的基于 RL 的替代方案。ROCM 32 引入分布正则化以稳定训练、缓解奖励被利用。Flow-GRPO 24 则出于类似目的使用 KL 正则化。

**EN** 3 Reward hacking analysis

**ZH** 3 奖励黑客分析

**EN** In this section, we characterize the reward hacking behavior observed in T2I RL training. We first describe the definition of reward hacking and its relevance to T2I generation (Section 3.1), followed by a description of our experimental setup and the reward functions examined (Section 3.2). We then analyze the training behaviors under different reward models and reveal that the model consistently exploits these rewards to achieve high training rewards while producing visually unrealistic and artifact-heavy images. Notably, this behavior persists across a wide range of reward settings.

**ZH** 本节刻画 T2I 强化学习训练中观察到的奖励黑客行为。我们先给出奖励黑客的定义及其与 T2I 生成的关联（3.1 节），随后说明实验设置与所考察的奖励函数（3.2 节）。接着分析不同奖励模型下的训练行为，揭示模型会持续利用这些奖励以获得较高的训练奖励，同时生成视觉上不真实、充满伪影的图像。值得注意的是，这一行为在广泛的奖励设置下都持续存在。

**EN** 3.1 Definition of Reward Hacking

**ZH** 3.1 奖励黑客的定义

**EN** Reward hacking refers to the phenomenon where optimizing an imperfect proxy reward results in degraded performance with respect to the true underlying objective 34. In other words, reward hacking occurs when a model learns to exploit weaknesses in the reward function and achieve high scores under the designed proxy while performing poorly according to the true goal.

**ZH** 奖励黑客指的是这样一种现象：优化一个不完美的代理奖励，反而导致在真实底层目标上的性能下降 34。换言之，当模型学会利用奖励函数的弱点，在设计好的代理指标上取得高分，而按真实目标衡量却表现糟糕时，就发生了奖励黑客。

**EN** In the context of text-to-image generation, numerous reward functions have been proposed to guide model training. However, each reward is typically designed to capture a specific aspect of generation quality, such as aesthetic appeal, human preference, or prompt-image alignment. Since these rewards are predefined and inherently partial, they are vulnerable to reward hacking 24.

**ZH** 在文本到图像生成场景下，研究者已提出众多奖励函数来指导模型训练。然而每种奖励通常只针对生成质量的某一个方面设计，例如美学吸引力、人类偏好或提示-图像对齐。由于这些奖励是预先定义的、本质上只是部分刻画，它们很容易被奖励黑客利用 24。

**EN** 3.2 Reward Choice and Evaluation for T2I RL Training

**ZH** 3.2 T2I 强化学习训练的奖励选择与评测

**EN** As discussed in Section 2.1, one major class of reward models for T2I RL training is built upon vision-language encoders such as CLIP 29 and BLIP 21. These models primarily aim to capture aesthetic appeal and human preference. To analyze how such reward functions affect model behavior, we select HPS 42 as a representative. This reward model correlates strongly with human preference and aesthetic judgments, making it an ideal candidate to study potential reward hacking phenomena driven by subjective visual quality signals.

**ZH** 如 2.1 节所述，用于 T2I 强化学习训练的一大类奖励模型建立在 CLIP 29 与 BLIP 21 等视觉-语言编码器之上，主要目标是刻画美学吸引力与人类偏好。为分析这类奖励函数如何影响模型行为，我们选取 HPS 42 作为代表：该奖励模型与人类偏好及美学判断高度相关，是研究由主观视觉质量信号驱动的潜在奖励黑客现象的理想对象。

**EN** In contrast, another important dimension of T2I evaluation is image-prompt alignment, which measures how well the generated image reflects the semantics described in the text prompt. A common approach to enforcing this alignment is to employ an object detector as a compositionality reward 25; 6; 51. Alternatively, recent works fine-tune MLLMs to directly assess whether an image matches the given prompt 14; 23; 35; 38. In our study, we adopt Grounding DINO 25 as a representative object detection-based reward, and finetuned ORM 14 as a representative MLLM-based prompt-image alignment reward.

**ZH** 与之相对，T2I 评测的另一个重要维度是图像-提示对齐，即衡量生成图像在多大程度上反映了文本提示所描述的语义。强制这一对齐的常见做法是采用目标检测器作为组合性奖励 25; 6; 51；另一种做法是微调 MLLM，直接判断图像是否与给定提示匹配 14; 23; 35; 38。在我们的研究中，采用 Grounding DINO 25 作为基于目标检测的代表性奖励，采用微调版 ORM 14 作为基于 MLLM 的提示-图像对齐奖励的代表。

**EN** We train Janus-Pro-1B 4 with each of these reward functions independently and monitor the reward hacking behaviors. The training dynamics are evaluated using various kinds of metrics:

**ZH** 我们用上述每一种奖励函数分别训练 Janus-Pro-1B 4，并监测其奖励黑客行为。训练动态采用多类指标评估：

**EN** • Aesthetic/human preference-oriented: HPS 42, Aesthetic Score 30, PickScore 19, and DeQA 46;

**ZH** • 面向美学或人类偏好的：HPS 42、Aesthetic Score 30、PickScore 19 与 DeQA 46；

**EN** • Text-image alignment-based: GDino 25, ORM 14, and VQAScore 23;

**ZH** • 基于文图对齐的：GDino 25、ORM 14 与 VQAScore 23；

**EN** • Unified quality and alignment: UnifiedReward 38.

**ZH** • 统一的质量与对齐：UnifiedReward 38。

**EN** 3.3 Training Dynamics and Reward Hacking Behaviors

**ZH** 3.3 训练动态与奖励黑客行为

<!-- [原子块 · object]  -->

**EN** (a) HPS - Object

**ZH** (a) HPS - 物体

<!-- [原子块 · object]  -->

**EN** (b) Aesthetic Score - Object

**ZH** (b) Aesthetic Score - 物体

<!-- [原子块 · object]  -->

**EN** (c) DeQA - Spatial

**ZH** (c) DeQA - 空间

<!-- [原子块 · object]  -->

**EN** (d) PickScore - Object

**ZH** (d) PickScore - 物体

<!-- [原子块 · object]  -->

**EN** (e) GDino - Spatial

**ZH** (e) GDino - 空间

<!-- [原子块 · object]  -->

**EN** (f) ORM - Color

**ZH** (f) ORM - 颜色

<!-- [原子块 · object]  -->

**EN** (g) VQAScore - Object

**ZH** (g) VQAScore - 物体

<!-- [原子块 · object]  -->

**EN** (h) UnifiedReward - Object

**ZH** (h) UnifiedReward - 物体

<!-- [原子块 · object]  -->

**EN** (i) Artifacts - Object

**ZH** (i) 伪影 - 物体

<!-- [原子块 · object]  -->

**EN** (j) Artifacts - Shape

**ZH** (j) 伪影 - 形状

<!-- [原子块 · object]  -->

**EN** (k) Artifacts - Spatial

**ZH** (k) 伪影 - 空间

<!-- [原子块 · object]  -->

**EN** (l) Artifacts - Texture

**ZH** (l) 伪影 - 纹理

**EN** Figure 1: Evolution of metrics over training steps trained on Janus-Pro-1B 4. Blue color denotes the model trained with HPS 42; Orange color denotes the model trained with GDino 25; Green color denotes the model trained with HPS and GDino; Red color denotes the model trained with finetuned ORM 14.

**ZH** 图 1：在 Janus-Pro-1B 4 上训练时各指标随训练步长的演化。蓝色表示用 HPS 42 训练的模型；橙色表示用 GDino 25 训练的模型；绿色表示用 HPS 与 GDino 训练的模型；红色表示用微调版 ORM 14 训练的模型。

**EN** We finetune the Janus-Pro-1B model 4 on the same training set used in T2I-R1 18, running three epochs of RL training (approximately 3000 steps) under different reward configurations. Figure 1 shows the evolution of various evaluation metrics throughout training. We only visualize the first 1200 steps for the HPS 42 reward, as its metric values begin to collapse shortly after this point.

**ZH** 我们在 T2I-R1 18 所用的同一训练集上微调 Janus-Pro-1B 模型 4，在不同奖励配置下运行三轮强化学习训练（约 3000 步）。图 1 展示了训练过程中各评测指标的演化。对 HPS 42 奖励，我们只可视化前 1200 步，因为此后不久其指标值便开始崩溃。

**EN** Reward-specific improvements and cross-metric degradation.

**ZH** 奖励特定的提升与跨指标退化。

**EN** Across most metrics, each model primarily improves on the metric family aligned with its training reward, but fails to generalize to others. For instance, models trained with GDino 25 or ORM 14 show steady gains on their respective reward values, yet exhibit clear degrade in human preference, aesthetic quality, and DeQA scores (Figure 1(a)-1(c)). Conversely, the model trained with HPS 42 shows rising HPS reward and aesthetic scores but experiences clear drops on grounding accuracy and semantic consistency (Figure 1(e)-1(f)). Other evaluation metrics, such as PickScore (Figure 1(d)), VQAScore (Figure 1(g)), and UnifiedReward (Figure 1(h)), show no consistent upward trend across training steps, regardless of reward types. Training with combined rewards (HPS + GDino) yields more stable and moderate improvements, suggesting partial complementary effects between the two reward signals. However, this ensemble only partially mitigates the issue, as reward-specific biases still remain.

**ZH** 在多数指标上，每个模型主要在与自身训练奖励对应的指标族上提升，却无法泛化到其他指标。例如，用 GDino 25 或 ORM 14 训练的模型在各自奖励值上稳步上升，但在人类偏好、美学质量与 DeQA 分数上却明显退化（图 1(a)–1(c)）。反之，用 HPS 42 训练的模型 HPS 奖励与美学分数上升，定位准确率与语义一致性却明显下降（图 1(e)–1(f)）。PickScore（图 1(d)）、VQAScore（图 1(g)）与 UnifiedReward（图 1(h)）等其他评测指标则不论奖励类型如何，在整个训练过程中都没有呈现一致的上升趋势。用组合奖励（HPS + GDino）训练可获得更稳定、更温和的提升，说明两种奖励信号之间存在部分互补效应；但这种集成只能部分缓解问题，奖励特有的偏差依然存在。

**EN** Overall, this cross-metric mismatch reveals that the model is optimizing narrowly for the specific reward signals rather than true improvements in generation quality, which is a direct manifestation of reward hacking.

**ZH** 总体而言，这种跨指标的不匹配揭示出：模型是在狭隘地针对特定奖励信号做优化，而非真正提升生成质量，这正是奖励黑客的直接表现。

**EN** Table 1: Image Illustration. The first column is the prompt. The second and fourth columns are from models trained with existing rewards. The third and fifth columns are from models trained with the help of our ArtifactReward. The label above each image is the reward used in RL training.

**ZH** 表 1：图像示例。第一列为提示。第二列与第四列来自用现有奖励训练的模型，第三列与第五列来自借助我们的 ArtifactReward 训练的模型。每张图像上方的标签为强化学习训练中所用的奖励。

<!-- [原子块 · table] HPS HPS + artifacts GDino GDino + artifacts A photo of a cup above a tennis racket HPS + GDino HPS + GDino + artifacts ORM ORM + artifacts HPS HPS + artifacts GDino GDino + artifacts A photo of a pers -->

**EN** Visual inspection of reward-driven biases.

**ZH** 奖励驱动偏差的视觉考察。

**EN** By examining the generated images, distinct reward-induced tendencies become apparent (see Table 1). The HPS-trained model tends to produce vibrant backgrounds and visually striking colors, since HPS implicitly favors aesthetic appeal. However, over-emphasizing colorfulness often leads to unrealistic and over-saturated images, sacrificing spatial grounding and object fidelity. Even when combined with GDino, this issue persists, as training remains biased toward HPS gains (Figure 1(a) and 1(e)), and thus the images still look unrealistic and over-saturated. In contrast, GDino or ORM-trained models generate simpler, object-centered compositions. This behavior naturally reflects their design: object detectors like GDino focus solely on the presence and localization of specified entities, while ORM is essentially trained with object-centered prompts, giving high rewards to clear depiction of main objects. Thus, these models achieve stronger grounding but reduced background diversity and realism.

**ZH** 通过检视生成的图像，可以清楚看到由奖励导致的各种倾向（见表 1）。用 HPS 训练的模型倾向于生成鲜艳的背景与视觉上醒目的色彩，因为 HPS 隐含地偏好美学吸引力。然而，过分强调色彩丰富度往往导致图像不真实、过饱和，牺牲了空间定位与物体保真度。即便与 GDino 组合，这一问题依然存在——训练仍偏向 HPS 的增益（图 1(a) 与 1(e)），图像因而依旧不真实、过饱和。相比之下，用 GDino 或 ORM 训练的模型生成更简单、以物体为中心的构图。这一行为自然反映了它们的设计：GDino 之类的目标检测器只关注指定实体是否存在以及定位是否准确，而 ORM 本质上是以物体为中心的提示训练的，会对主体物体的清晰呈现给出高奖励。因此，这些模型定位能力更强，但背景多样性与真实感有所下降。

**EN** Universal reward failure: structural artifacts.

**ZH** 普遍的奖励失效：结构性伪影。

**EN** While the above analysis highlights reward-specific biases and cross-metric degradation, we further identify a more pervasive and universal reward failure pattern in T2I RL–structural artifacts. Across the qualitative results in Table 1, generated images frequently exhibit geometric distortions (e.g., physically implausible or distorted tennis rackets), object duplication or fragmentation (e.g., duplicated limbs or overlapping object outlines), and even blending between different entities (e.g., a human body merged with a bear head). Remarkably, these structural failures arise consistently under every reward configuration (HPS, GDino, ORM, and HPS + GDino), revealing a shared systematic blind spot in current reward formulations. None of these rewards reliably enforce local structure or fine-grained object correctness. As a result, the generative policy exploit this loophole, optimizing reward signals without genuinely learning to produce geometrically coherent images. This behavior illustrates a deeper form of reward hacking, where models achieve higher scores by bypassing true structural correctness.

**ZH** 上述分析突出了奖励特有的偏差与跨指标退化，而我们进一步识别出 T2I 强化学习中一种更普遍、更共通的奖励失效模式——结构性伪影。从表 1 的定性结果看，生成的图像频繁出现几何畸变（例如物理上不合理或扭曲的网球拍）、物体重复或碎裂（例如重复的肢体或重叠的物体轮廓），甚至不同实体之间的融合（例如人体长着熊头）。值得注意的是，这些结构性失效在每一种奖励配置下（HPS、GDino、ORM 以及 HPS + GDino）都一致出现，暴露出当前奖励形式化方式中一个共同的系统性盲区：没有任何一种奖励能可靠地强制局部结构或细粒度物体正确性。于是生成策略利用了这一漏洞，在不真正学会生成几何连贯图像的情况下优化奖励信号。这种行为体现了一种更深层的奖励黑客——模型通过绕过真正的结构正确性来取得更高分数。

**EN** Summary.

**ZH** 小结。

**EN** Together, these findings reveal clear and pervasive reward hacking in T2I RL training. Each reward guides the model toward narrow patterns that maximize its own metric while degrading other aspects of performance. The model learns to exploit superficial cues favored by the reward, such as over-saturated colors for HPS or object-centric simplifications for GDino and ORM. Even joint-optimization with multiple rewards (e.g., HPS + GDino) provides only partial mitigation, as the underlying biases remain. More fundamentally, current reward formulations lack any mechanism that discourages artifact-driven shortcuts. Without constraints enforcing structural plausibility or fine-grained correctness, the model is free to achieve higher scores through geometrically distorted and implausible generations.

**ZH** 综合来看，这些发现揭示了 T2I 强化学习训练中明显而普遍的奖励黑客现象。每一种奖励都把模型引向狭隘的模式，以最大化自身指标，同时损害其他方面的性能。模型学会了利用奖励所偏好的表层线索，例如为迎合 HPS 而使用过饱和色彩，或为迎合 GDino 与 ORM 而做以物体为中心的简化。即便用多个奖励联合优化（如 HPS + GDino），也只能部分缓解，因为底层偏差依然存在。更根本的问题在于，当前的奖励形式化方式缺乏任何抑制伪影式捷径的机制。没有强制结构合理性与细粒度正确性的约束，模型便可自由地通过几何畸变与不合理的生成来取得更高分数。

**EN** 4 Mitigating Reward Hacking via Artifact-Aware Reward Design

**ZH** 4 通过伪影感知的奖励设计缓解奖励黑客

**EN** Table 2: Accuracy of different reward models in assigning higher scores to artifact-free images compared to artifact-containing ones. Each image pair is scored as 1 if the reward assigns a higher score to the artifact-free image, 0.5 if the scores are tied, and 0 if the artifact-containing image receives a higher score. The accuracy is averaged across all pairs.

**ZH** 表 2：不同奖励模型在给无伪影图像打分高于含伪影图像时的准确率。每对图像中，若奖励给无伪影图像的分数更高则记 1 分，两者同分记 0.5 分，若含伪影图像得分更高则记 0 分。准确率在所有图像对上取平均。

<!-- [原子块 · table] Rewards Correct Tie Wrong Accuracy HPS 42 108 0 94 0.53 Aesthetic Score 30 84 0 118 0.42 ImageReward 43 133 7 62 0.68 MANIQA 45 80 0 122 0.39 DeQA 46 104 0 98 0.51 GDino 25 46 143 13 0.58 ORM 14 39 14 -->

**EN** Table 3: Examples of curated artifact diagnostic dataset. The upper images show no artifacts, while the lower images contain artifacts.

**ZH** 表 3：精心构建的伪影诊断数据集示例。上方图像不含伪影，下方图像含伪影。

<!-- [原子块 · table] rubber sole shoes and a wooden chair a wooden table and a fabric hat HPS: 0.3293 HPS: 0.2878 GDino: 0.4 GDino: 1.0 ORM: 1.0 ORM: 1.0 Artifact: 0.7549 Artifact: 0.9149 HPS: 0.3362 HPS: 0.2893 GDino: 0. -->

**EN** To quantify the prevalence of artifact generation, we curated a small diagnostic dataset comprising both artifact-containing and artifact-free images, annotated via human judgment. For each prompt, we formed pairs of one artifact-free image and one artifact-containing image, allowing controlled comparison of reward behaviors. Representative examples are provided in Table 3.

**ZH** 为量化伪影生成的普遍程度，我们构建了一个小型诊断数据集，包含含伪影与无伪影两类图像，并由人工判断标注。对每个提示，我们把一张无伪影图像与一张含伪影图像配成对，以便受控地比较奖励行为。代表性示例见表 3。

**EN** We then evaluate existing reward models on this curated dataset to assess whether they correctly assign higher scores to artifact-free images compared with artifact-containing images. As summarized in Table 2, none of the existing reward models consistently penalize images with clear structural failures. In many cases, they assign equal or even higher scores to flawed images. GDino, ORM and UnifiedReward, in particular, frequently produce identical scores across pairs (“Tie”), revealing an inability to detect fine-grained geometric inconsistencies. This results expose a centural limitation in current T2I reward designs: they lack sensitivity to fine-grained local structural coherence and object plausibility, allowing models to exploit reward loopholes and generate visually implausible yet high-reward images.

**ZH** 随后，我们在这套数据集上评估现有奖励模型，考察它们是否能正确地给无伪影图像打出高于含伪影图像的分数。如表 2 所示，没有任何现有奖励模型能稳定地惩罚存在明显结构失效的图像；在许多情况下，它们给有缺陷的图像打了相同甚至更高的分数。GDino、ORM 与 UnifiedReward 尤其频繁地在图像对上给出完全相同的分数（同分），暴露出它们无法检测细粒度的几何不一致。这一结果揭示了当前 T2I 奖励设计的一个核心局限：它们对细粒度局部结构连贯性与物体合理性缺乏敏感度，使模型得以利用奖励漏洞，生成视觉上不合理却获得高奖励的图像。

**EN** 4.1 ArtifactReward: Complementary Reward via Automatic Prompt Optimization

**ZH** 4.1 ArtifactReward：通过自动提示优化得到的互补奖励

**EN** To address this limitation, we introduce ArtifactReward, a complementary reward function explicitly designed to penalize unrealistic or artifact-containing generations.

**ZH** 为弥补这一局限，我们引入 ArtifactReward——一种明确用于惩罚不真实或含伪影生成结果的互补奖励函数。

**EN** Rather than relying on large-scale human annotation, we leverage automatic prompt optimization (APO) 28; 33; 52; 9 to construct a lightweight, data-efficient proxy reward from limited labeled examples.

**ZH** 我们不依赖大规模人工标注，而是利用自动提示优化（APO）28; 33; 52; 9，从有限的标注样本中构建一个轻量、数据高效的代理奖励。

**EN** Specificly, we use Qwen2.5-VL-7B-Instruct 2 as the backbone visual-language model. Details of the APO procedure for constructing ArtifactReward are provided in Supplementary 6. At inference time, the model is prompted with the optimized instruction and asked to determine whether the input image contains any unrealistic artifacts. The model outputs probabilities for the “yes” and “no” tokens. We define the ArtifactReward score as the normalized probability assigned to “no”, i.e., which corresponds to the estimated likelihood that the image is artifact-free:

**ZH** 具体而言，我们使用 Qwen2.5-VL-7B-Instruct 2 作为骨干视觉-语言模型。构建 ArtifactReward 的 APO 流程详见补充材料第 6 节。推理时，模型被输入优化后的指令，并被要求判断输入图像是否包含任何不真实的伪影；模型输出 yes 与 no 两个词元的概率。我们把 ArtifactReward 分数定义为赋给 no 的归一化概率，即图像无伪影的估计似然：

<!-- [原子块 · table] R ArtifactReward = 1 1 + e [ log ​ ( p yes ) − log ​ ( p no ) ] . R_{\text{ArtifactReward}}=\frac{1}{1+e^{[\text{log}(p_{\text{yes}})-\text{log}(p_{\text{no}})]}}. (1) -->

**EN** Through APO, the instruction is iteratively refined to maximize discrimination between artifact-free and artifact-containing samples. The resulting ArtifactReward demonstrates strong ability to detect structural inconsistencies and fine-grained artifacts (Table 2), outperforming existing rewards in recognizingunrealistic generations.

**ZH** 通过 APO，指令被迭代优化，以最大化对无伪影样本与含伪影样本的区分能力。所得的 ArtifactReward 在检测结构不一致与细粒度伪影上表现突出（表 2），在识别不真实生成结果方面优于现有奖励。

**EN** We further evaluate the ArtifactReward signal across different existing training reward configurations. As shown in Figure 1(i)-1(l), none of existing reward models produce a meaningful increase in ArtifactReward scores during training, reinforcing that current rewards do not effectively suppress artifact formation.

**ZH** 我们进一步在已有的不同训练奖励配置下考察 ArtifactReward 信号。如图 1(i)–1(l) 所示，现有奖励模型在训练过程中都未使 ArtifactReward 分数出现有意义的上升，这进一步印证了当前奖励并不能有效抑制伪影的形成。

**EN** 4.2 Integrating ArtifactReward into RL Training

**ZH** 4.2 把 ArtifactReward 整合进强化学习训练

**EN** Table 4: Performance on WISE 26 benchmark trained on Janus-Pro-1B 4. WiScore = 0.7 ⟦SLOT_0⟧ Consistency + 0.2 ⟦SLOT_1⟧ Realism + 0.1 ⟦SLOT_2⟧ Aesthetic by the default setting.

**ZH** 表 4：在 Janus-Pro-1B 4 上训练的模型在 WISE 26 基准上的表现。按默认设置，WiScore = 0.7 ⟦SLOT_0⟧ 一致性 + 0.2 ⟦SLOT_1⟧ 真实感 + 0.1 ⟦SLOT_2⟧ 美学。

<!-- [原子块 · table] Method Consistency Realism Aesthetic WiScore Janus-Pro-1B 4 0.2420 0.3550 0.3790 0.2783 HPS 42 0.2960 0.4515 0.6115 0.3587 HPS + Artifact 0.3000 0.5760 0.5470 0.3799 GDino 25 0.2905 0.4100 0.4395 0.32 -->

**EN** Table 5: Performance on LLM4LLM 37 benchmark trained on Janus-Pro-1B 4.

**ZH** 表 5：在 Janus-Pro-1B 4 上训练的模型在 LLM4LLM 37 基准上的表现。

<!-- [原子块 · table] Method Perception Correspondence All Janus-Pro-1B 4 0.4056 0.5058 0.9114 HPS 42 0.4240 0.5067 0.9307 HPS + Artifact 0.4464 0.5089 0.9553 GDino 25 0.4230 0.5371 0.9601 GDino + Artifact 0.4336 0.5416 0. -->

**EN** We incorporate ArtifactReward into the four prior RL settings (HPS, GDino, ORM, and HPS + GDino) and the T2I-R1 18 setting. As illustrated in Table 1, incorporating ArtifactReward consistently reduces the prevalence of visual artifacts in generated images. The resulting images exhibit reduced artifacts, improved realism and more balanced color composition.

**ZH** 我们把 ArtifactReward 引入此前四种强化学习设置（HPS、GDino、ORM 以及 HPS + GDino）以及 T2I-R1 18 设置。如表 1 所示，引入 ArtifactReward 能持续降低生成图像中视觉伪影的出现率；所得图像伪影更少、真实感更强，色彩构成也更均衡。

**EN** 4.3 Benchmark Evaluation

**ZH** 4.3 基准评测

**EN** To assess the generalizability of ArtifactReward, we evaluate all training variants on two recent benchmarks:

**ZH** 为评估 ArtifactReward 的泛化能力，我们在两个新近的基准上评测所有训练变体：

**EN** • WISE 26: uses GPT-4o 17 to evaluate consistency, realism, and aesthetic quality of generated images;

**ZH** • WISE 26：使用 GPT-4o 17 评估生成图像的一致性、真实感与美学质量；

**EN** • LLM4LLM 37: employs two fine-tuned LLM judges to compute Perception (clarity, authenticity, aesthetics) and Correspondence (text-image alignment).

**ZH** • LLM4LLM 37：使用两个微调后的大语言模型评判器计算 Perception（清晰度、真实感、美学）与 Correspondence（文图对齐）。

**EN** Table 4 shows the results on WISE benchmark. Across all reward configurations, integrating ArtifactReward leads to consistent performance improvements, particularly in realism and consistency. The primary gain originates from ArtifactReward’s explicit suppression of structural distortions and over-saturated appearances. Consequently, images appear more natural and coherent, despite sometimes at a modest cost to aesthetic scores, which is an expected tradeoff given the reduced emphasis on exaggerated colorfulness.

**ZH** 表 4 给出了在 WISE 基准上的结果。在所有奖励配置下，引入 ArtifactReward 都带来稳定的性能提升，真实感与一致性的提升尤为明显。主要增益来自 ArtifactReward 对结构畸变与过饱和外观的显式抑制；因此图像显得更自然、更连贯，代价有时是美学分数略有下降——考虑到对夸张色彩丰富度的强调被削弱，这是一种意料之中的权衡。

**EN** Table 5 shows the results on LLM4LLM benchmark. Incorporating ArtifactReward yields consistent gains across most training configurations. On the Perception dimension, ArtifactReward improves nearly all baselines, indicating that reducing structural artifacts directly enhances the perceived authenticity of generated images. Similarly, the Correspondence dimension also benefits from ArtifactReward, often achieving the best or near-best scores within each reward setting.

**ZH** 表 5 给出了在 LLM4LLM 基准上的结果。引入 ArtifactReward 在多数训练配置下都带来稳定增益。在 Perception 维度上，ArtifactReward 改进了几乎所有基线，说明减少结构性伪影能直接提升生成图像的感知真实度。Correspondence 维度同样受益于 ArtifactReward，往往在各自的奖励设置内取得最优或接近最优的分数。

<!-- [原子块 · img]  -->

**EN** (a) HPS

**ZH** (a) HPS

<!-- [原子块 · img]  -->

**EN** (b) HPS + Artifact

**ZH** (b) HPS + Artifact

<!-- [原子块 · img]  -->

**EN** (c) GDino

**ZH** (c) GDino

<!-- [原子块 · img]  -->

**EN** (d) GDino + Artifact

**ZH** (d) GDino + Artifact

<!-- [原子块 · img]  -->

**EN** (e) HPS + GDino

**ZH** (e) HPS + GDino

<!-- [原子块 · img]  -->

**EN** (f) HPS + GDino + Artifact

**ZH** (f) HPS + GDino + Artifact

<!-- [原子块 · img]  -->

**EN** (g) ORM

**ZH** (g) ORM

<!-- [原子块 · img]  -->

**EN** (h) ORM + Artifact

**ZH** (h) ORM + Artifact

**EN** Figure 2: Images generated with prompt “Traditional food of the Mid-Autumn Festival” in WISE 26 benchmark under different training reward configurations. This prompt expect the image to show mooncakes.

**ZH** 图 2：在 WISE 26 基准上，用提示“中秋节的传统食物”在不同训练奖励配置下生成的图像。该提示期望图像呈现月饼。

<!-- [原子块 · img]  -->

**EN** (a) HPS

**ZH** (a) HPS

<!-- [原子块 · img]  -->

**EN** (b) HPS + Artifact

**ZH** (b) HPS + Artifact

<!-- [原子块 · img]  -->

**EN** (c) GDino

**ZH** (c) GDino

<!-- [原子块 · img]  -->

**EN** (d) GDino + Artifact

**ZH** (d) GDino + Artifact

<!-- [原子块 · img]  -->

**EN** (e) HPS + GDino

**ZH** (e) HPS + GDino

<!-- [原子块 · img]  -->

**EN** (f) HPS + GDino + Artifact

**ZH** (f) HPS + GDino + Artifact

<!-- [原子块 · img]  -->

**EN** (g) ORM

**ZH** (g) ORM

<!-- [原子块 · img]  -->

**EN** (h) ORM + Artifact

**ZH** (h) ORM + Artifact

**EN** Figure 3: Images generated with prompt “a photo of a cow” in LLM4LLM 37 benchmark under different training reward configurations.

**ZH** 图 3：在 LLM4LLM 37 基准上，用提示“一张牛的照片”在不同训练奖励配置下生成的图像。

**EN** Figure 2 and Figure 3 illustrate qualitative examples from these two benchmarks. In Figure 2, images generated with the help of our ArtifactReward exhibit noticeably improved realism and better alignment with the prompt intent, while also reducing the excessive color saturation often produced by HPS-trained models. In Figure 3, we also observe that HPS-based training tends to introduce unnatural colors, whereas GDino and ORM-based training frequently results in duplicated or geometrically distorted objects. In contrast, incorporating our ArtifactReward effectively suppresses these issues, yielding images with more coherent structure and plausible visual attributes.

**ZH** 图 2 与图 3 展示了这两个基准上的定性示例。在图 2 中，借助我们的 ArtifactReward 生成的图像真实感明显更好，也更贴合提示意图，同时减轻了 HPS 训练模型常产生的过度色彩饱和。在图 3 中，我们还观察到基于 HPS 的训练倾向于引入不自然的色彩，而基于 GDino 与 ORM 的训练则频繁导致物体重复或几何畸变。相比之下，引入我们的 ArtifactReward 能有效抑制这些问题，生成结构更连贯、视觉属性更合理的图像。

**EN** Summary.

**ZH** 小结。

**EN** Together, these results demonstrate that ArtifactReward generalizes well across diverse reward settings and architectures, consistently improving both perceptual quality and semantic correspondence. By explicitly targeting perceptual and structural plausibility, failure modes that existing rewards systematically overlook, ArtifactReward acts as an effective and general-purpose regularizer against T2I reward hacking. It complements existing rewards that emphasize aesthetics or compositional alignment. Although aesthetic scores may slightly decrease due to reduced over-saturation, the substantial improvements in realism, alignment consistency, and cross-benchmark robustness highlight ArtifactReward’s value as a meaningful step toward more human-aligned T2I reward design.

**ZH** 综合来看，这些结果表明 ArtifactReward 在多样的奖励设置与架构上泛化良好，能持续提升感知质量与语义对应性。由于明确针对现有奖励系统性忽视的失效模式——感知与结构合理性——ArtifactReward 成为一种有效且通用的正则项，可对抗 T2I 奖励黑客。它对那些强调美学或组合对齐的现有奖励形成补充。尽管因过饱和被削弱，美学分数可能略有下降，但真实感、对齐一致性与跨基准鲁棒性上的显著改善，凸显了 ArtifactReward 作为迈向更贴合人类的 T2I 奖励设计的重要一步所具有的价值。

**EN** 5 Conclusion

**ZH** 5 结论

**EN** In this work, we present the first systematic study of reward hacking in Text-to-Image RL post-training. Through extensive analysis across widely used reward models, which spans aesthetics, human preference, and image-text alignment, we reveal that existing rewards not only induce reward-specific biases but also share a universal blind spot: the persistent production of structural artifacts that current reward functions fail to penalize. To address this gap, we introduce ArtifactReward, a complementary reward learned via automatic prompt optimization to detect fine-grained visual artifacts from limited supervision. When integrated into multiple RL training configurations, ArtifactReward consistently reduces artifact prevalence, improves realism, and enhances benchmark performance.

**ZH** 本文首次对文本到图像强化学习后训练中的奖励黑客展开系统研究。通过在覆盖美学、人类偏好与图文对齐的多种常用奖励模型上的广泛分析，我们揭示出：现有奖励不仅诱发各自特有的偏差，还共享一个普遍盲区——持续产生结构性伪影，而当前奖励函数未能对其加以惩罚。为弥补这一缺口，我们提出 ArtifactReward——一种通过自动提示优化学到的互补奖励，可从有限的监督信号中检测细粒度视觉伪影。当它被整合进多种强化学习训练配置时，能持续降低伪影出现率、提升真实感，并改善基准表现。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] Amodei et al. (2016) D. Amodei, C. Olah, J. Steinhardt, P. Christiano, J. Schulman, and D. Mané Concrete problems in ai safety . arXiv preprint arXiv:1606.06565 . Cited by: §1 . -->

<!-- [原子块 · verbatim] Bai et al. (2025) S. Bai, K. Chen, X. Liu, J. Wang, W. Ge, S. Song, K. Dang, P. Wang, S. Wang, J. Tang, et al. Qwen2. 5-vl technical report . arXiv preprint arXiv:2502.13923 . Cited by: §2.2 , §4.1 ,  -->

<!-- [原子块 · verbatim] Black et al. (2023) K. Black, M. Janner, Y. Du, I. Kostrikov, and S. Levine Training diffusion models with reinforcement learning . arXiv preprint arXiv:2305.13301 . Cited by: §2.2 . -->

<!-- [原子块 · verbatim] Chen et al. (2025a) X. Chen, Z. Wu, X. Liu, Z. Pan, W. Liu, Z. Xie, X. Yu, and C. Ruan Janus-pro: unified multimodal understanding and generation with data and model scaling . arXiv preprint arXiv:250 -->

<!-- [原子块 · verbatim] Chen et al. (2025b) Y. Chen, Y. Ban, Y. Hong, and C. Hsieh IRIS: intrinsic reward image synthesis . arXiv preprint arXiv:2509.25562 . Cited by: §1 . -->

<!-- [原子块 · verbatim] Cheng et al. (2024) T. Cheng, L. Song, Y. Ge, W. Liu, X. Wang, and Y. Shan Yolo-world: real-time open-vocabulary object detection . In Proceedings of the IEEE/CVF conference on computer vision and pat -->

<!-- [原子块 · verbatim] Cho et al. (2023) J. Cho, Y. Hu, R. Garg, P. Anderson, R. Krishna, J. Baldridge, M. Bansal, J. Pont-Tuset, and S. Wang Davidsonian scene graph: improving reliability in fine-grained evaluation for tex -->

<!-- [原子块 · verbatim] Clark et al. (2023) K. Clark, P. Vicol, K. Swersky, and D. J. Fleet Directly fine-tuning diffusion models on differentiable rewards . arXiv preprint arXiv:2309.17400 . Cited by: §1 , §1 , §2.2 , §2.3  -->

<!-- [原子块 · verbatim] Deng et al. (2022) M. Deng, J. Wang, C. Hsieh, Y. Wang, H. Guo, T. Shu, M. Song, E. P. Xing, and Z. Hu RLPrompt: optimizing discrete text prompts with reinforcement learning . External Links: 2205.125 -->

<!-- [原子块 · verbatim] Duan et al. (2025) C. Duan, R. Fang, Y. Wang, K. Wang, L. Huang, X. Zeng, H. Li, and X. Liu Got-r1: unleashing reasoning capability of mllm for visual generation with reinforcement learning . arXiv pr -->

<!-- [原子块 · verbatim] Gao et al. (2023) L. Gao, J. Schulman, and J. Hilton Scaling laws for reward model overoptimization . In International Conference on Machine Learning , pp. 10835–10866 . Cited by: §1 . -->

<!-- [原子块 · verbatim] Ghosh et al. (2023) D. Ghosh, H. Hajishirzi, and L. Schmidt Geneval: an object-focused framework for evaluating text-to-image alignment . Advances in Neural Information Processing Systems 36 , pp. 521 -->

<!-- [原子块 · verbatim] Guo et al. (2025a) D. Guo, D. Yang, H. Zhang, J. Song, R. Zhang, R. Xu, Q. Zhu, S. Ma, P. Wang, X. Bi, et al. Deepseek-r1: incentivizing reasoning capability in llms via reinforcement learning . arXiv -->

<!-- [原子块 · verbatim] Guo et al. (2025b) Z. Guo, R. Zhang, C. Tong, Z. Zhao, R. Huang, H. Zhang, M. Zhang, J. Liu, S. Zhang, P. Gao, et al. Can we generate images with cot? let’s verify and reinforce image generation step  -->

<!-- [原子块 · verbatim] He et al. (2025) J. He, J. Liu, C. Y. Liu, R. Yan, C. Wang, P. Cheng, X. Zhang, F. Zhang, J. Xu, W. Shen, et al. Skywork open reasoner 1 technical report . arXiv preprint arXiv:2505.22312 . Cited by:  -->

<!-- [原子块 · verbatim] Hessel et al. (2021) J. Hessel, A. Holtzman, M. Forbes, R. L. Bras, and Y. Choi Clipscore: a reference-free evaluation metric for image captioning . arXiv preprint arXiv:2104.08718 . Cited by: §2.2 . -->

<!-- [原子块 · verbatim] Hurst et al. (2024) A. Hurst, A. Lerer, A. P. Goucher, A. Perelman, A. Ramesh, A. Clark, A. Ostrow, A. Welihinda, A. Hayes, A. Radford, et al. Gpt-4o system card . arXiv preprint arXiv:2410.21276 . Ci -->

<!-- [原子块 · verbatim] Jiang et al. (2025) D. Jiang, Z. Guo, R. Zhang, Z. Zong, H. Li, L. Zhuo, S. Yan, P. Heng, and H. Li T2i-r1: reinforcing image generation with collaborative semantic-level and token-level cot . arXiv p -->

<!-- [原子块 · verbatim] Kirstain et al. (2023) Y. Kirstain, A. Polyak, U. Singer, S. Matiana, J. Penna, and O. Levy Pick-a-pic: an open dataset of user preferences for text-to-image generation . Advances in neural informatio -->

<!-- [原子块 · verbatim] Ku et al. (2023) M. Ku, D. Jiang, C. Wei, X. Yue, and W. Chen Viescore: towards explainable metrics for conditional image synthesis evaluation . arXiv preprint arXiv:2312.14867 . Cited by: §1 , §2.1 . -->

<!-- [原子块 · verbatim] Li et al. (2022) J. Li, D. Li, C. Xiong, and S. Hoi Blip: bootstrapping language-image pre-training for unified vision-language understanding and generation . In International conference on machine le -->

<!-- [原子块 · verbatim] Li et al. (2024) Y. Li, H. Liu, M. Cai, Y. Li, E. Shechtman, Z. Lin, Y. J. Lee, and K. K. Singh Removing distributional discrepancies in captions improves image-text alignment . In European Conference -->

<!-- [原子块 · verbatim] Lin et al. (2024) Z. Lin, D. Pathak, B. Li, J. Li, X. Xia, G. Neubig, P. Zhang, and D. Ramanan Evaluating text-to-visual generation with image-to-text generation . In European Conference on Computer V -->

<!-- [原子块 · verbatim] Liu et al. (2025) J. Liu, G. Liu, J. Liang, Y. Li, J. Liu, X. Wang, P. Wan, D. Zhang, and W. Ouyang Flow-grpo: training flow matching models via online rl . arXiv preprint arXiv:2505.05470 . Cited by: -->

<!-- [原子块 · verbatim] Liu et al. (2024) S. Liu, Z. Zeng, T. Ren, F. Li, H. Zhang, J. Yang, Q. Jiang, C. Li, J. Yang, H. Su, et al. Grounding dino: marrying dino with grounded pre-training for open-set object detection . In -->

<!-- [原子块 · verbatim] Niu et al. (2025) Y. Niu, M. Ning, M. Zheng, W. Jin, B. Lin, P. Jin, J. Liao, C. Feng, K. Ning, B. Zhu, et al. Wise: a world knowledge-informed semantic evaluation for text-to-image generation . arXiv -->

<!-- [原子块 · verbatim] Ouyang et al. (2022) L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. Wainwright, P. Mishkin, C. Zhang, S. Agarwal, K. Slama, A. Ray, et al. Training language models to follow instructions with human feedba -->

<!-- [原子块 · verbatim] Pryzant et al. (2023) R. Pryzant, D. Iter, J. Li, Y. T. Lee, C. Zhu, and M. Zeng Automatic prompt optimization with” gradient descent” and beam search . arXiv preprint arXiv:2305.03495 . Cited by: §4. -->

<!-- [原子块 · verbatim] Radford et al. (2021) A. Radford, J. W. Kim, C. Hallacy, A. Ramesh, G. Goh, S. Agarwal, G. Sastry, A. Askell, P. Mishkin, J. Clark, et al. Learning transferable visual models from natural language sup -->

<!-- [原子块 · verbatim] Schuhmann et al. (2022) C. Schuhmann, R. Beaumont, R. Vencu, C. Gordon, R. Wightman, M. Cherti, T. Coombes, A. Katta, C. Mullis, M. Wortsman, et al. Laion-5b: an open large-scale dataset for training  -->

<!-- [原子块 · verbatim] Shao et al. (2024) Z. Shao, P. Wang, Q. Zhu, R. Xu, J. Song, X. Bi, H. Zhang, M. Zhang, Y. Li, Y. Wu, et al. Deepseekmath: pushing the limits of mathematical reasoning in open language models . arXiv  -->

<!-- [原子块 · verbatim] Shekhar and Zhang (2025) S. Shekhar and T. Zhang ROCM: rlhf on consistency models . arXiv preprint arXiv:2503.06171 . Cited by: §1 , §2.2 , §2.3 . -->

<!-- [原子块 · verbatim] Shin et al. (2020) T. Shin, Y. Razeghi, R. L. L. IV, E. Wallace, and S. Singh AutoPrompt: eliciting knowledge from language models with automatically generated prompts . External Links: 2010.15980 , L -->

<!-- [原子块 · verbatim] Skalse et al. (2022) J. Skalse, N. Howe, D. Krasheninnikov, and D. Krueger Defining and characterizing reward gaming . Advances in Neural Information Processing Systems 35 , pp. 9460–9471 . Cited by:  -->

<!-- [原子块 · verbatim] Tan et al. (2024) Z. Tan, X. Yang, L. Qin, M. Yang, C. Zhang, and H. Li EvalAlign: evaluating text-to-image models through precision alignment of multimodal large models with supervised fine-tuning to -->

<!-- [原子块 · verbatim] Wang et al. (2022) J. Wang, Z. Yang, X. Hu, L. Li, K. Lin, Z. Gan, Z. Liu, C. Liu, and L. Wang Git: a generative image-to-text transformer for vision and language . arXiv preprint arXiv:2205.14100 . C -->

<!-- [原子块 · verbatim] Wang et al. (2025a) J. Wang, H. Duan, Y. Zhao, J. Wang, G. Zhai, and X. Min Lmm4lmm: benchmarking and evaluating large-multimodal image generation with lmms . arXiv preprint arXiv:2504.08358 . Cited b -->

<!-- [原子块 · verbatim] Wang et al. (2025b) Y. Wang, Y. Zang, H. Li, C. Jin, and J. Wang Unified reward model for multimodal understanding and generation . arXiv preprint arXiv:2503.05236 . Cited by: §1 , 3rd item , §2.1 , 3 -->

<!-- [原子块 · verbatim] Wei et al. (2025) H. Wei, B. Xu, H. Liu, C. Wu, J. Liu, Y. Peng, P. Wang, Z. Liu, J. He, Y. Xietian, et al. Skywork unipic 2.0: building kontext model with online rl for unified multimodal model . arX -->

<!-- [原子块 · verbatim] Wu et al. (2023a) H. Wu, Z. Zhang, W. Zhang, C. Chen, L. Liao, C. Li, Y. Gao, A. Wang, E. Zhang, W. Sun, et al. Q-align: teaching lmms for visual scoring via discrete text-defined levels . arXiv prepr -->

<!-- [原子块 · verbatim] Wu et al. (2025) J. Wu, Y. Gao, Z. Ye, M. Li, L. Li, H. Guo, J. Liu, Z. Xue, X. Hou, W. Liu, et al. Rewarddance: reward scaling in visual generation . arXiv preprint arXiv:2509.08826 . Cited by: §1 ,  -->

<!-- [原子块 · verbatim] Wu et al. (2023b) X. Wu, Y. Hao, K. Sun, Y. Chen, F. Zhu, R. Zhao, and H. Li Human preference score v2: a solid benchmark for evaluating human preferences of text-to-image synthesis . arXiv preprint a -->

<!-- [原子块 · verbatim] Xu et al. (2023) J. Xu, X. Liu, Y. Wu, Y. Tong, Q. Li, M. Ding, J. Tang, and Y. Dong Imagereward: learning and evaluating human preferences for text-to-image generation . Advances in Neural Informatio -->

<!-- [原子块 · verbatim] Xue et al. (2025) Z. Xue, J. Wu, Y. Gao, F. Kong, L. Zhu, M. Chen, Z. Liu, W. Liu, Q. Guo, W. Huang, et al. DanceGRPO: unleashing grpo on visual generation . arXiv preprint arXiv:2505.07818 . Cited by -->

<!-- [原子块 · verbatim] Yang et al. (2022) S. Yang, T. Wu, S. Shi, S. Lao, Y. Gong, M. Cao, J. Wang, and Y. Yang Maniqa: multi-dimension attention network for no-reference image quality assessment . In Proceedings of the IEE -->

<!-- [原子块 · verbatim] You et al. (2025) Z. You, X. Cai, J. Gu, T. Xue, and C. Dong Teaching large language models to regress accurate image quality scores using score distribution . In Proceedings of the Computer Vision an -->

<!-- [原子块 · verbatim] Yuan et al. (2025) S. Yuan, Y. Liu, Y. Yue, J. Zhang, W. Zuo, Q. Wang, F. Zhang, and G. Zhou Ar-grpo: training autoregressive image generation models via reinforcement learning . arXiv preprint arXiv: -->

<!-- [原子块 · verbatim] Zhang et al. (2019) T. Zhang, V. Kishore, F. Wu, K. Q. Weinberger, and Y. Artzi Bertscore: evaluating text generation with bert . arXiv preprint arXiv:1904.09675 . Cited by: §2.2 . -->

<!-- [原子块 · verbatim] Zhang et al. (2024) Y. Zhang, E. Tzeng, Y. Du, and D. Kislyuk Large-scale reinforcement learning for diffusion models . In European Conference on Computer Vision , pp. 1–17 . Cited by: §1 , §1 , §2.2  -->

<!-- [原子块 · verbatim] Zhou et al. (2025) S. Zhou, R. Zhang, H. Zhu, B. Kveton, Y. Zhou, J. Gu, J. Chen, and C. Chen Multimodal llms as customized reward models for text-to-image generation . In Proceedings of the IEEE/CVF  -->

<!-- [原子块 · verbatim] Zhou et al. (2022) X. Zhou, V. Koltun, and P. Krähenbühl Simple multi-dataset detection . In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition , pp. 7571–7580 . Cited b -->

<!-- [原子块 · verbatim] Zhou et al. (2023) Y. Zhou, A. I. Muresanu, Z. Han, K. Paster, S. Pitis, H. Chan, and J. Ba Large language models are human-level prompt engineers . External Links: 2211.01910 , Link Cited by: §4.1 . -->

**EN** Supplementary Material

**ZH** 补充材料

**EN** 6 Automatic Prompt Optimization for ArtifactReward

**ZH** 6 ArtifactReward 的自动提示优化

**EN** We employ automatic prompt optimization (APO) 28 to optimize the prompt used for ArtifactReward. Qwen2.5-VL-7B-Instruct 2 serves as our backbone vision-language model, and APO is used to optimize the prompt so that the model can more reliably distinguish artifact-containing images from artifact-free ones.

**ZH** 我们采用自动提示优化（APO）28 来优化 ArtifactReward 所用的提示。Qwen2.5-VL-7B-Instruct 2 作为骨干视觉-语言模型，APO 则用于优化提示，使模型能更可靠地区分含伪影图像与无伪影图像。

**EN** Our initial prompt is given as:

**ZH** 我们的初始提示如下：

<!-- [原子块 · svg]  -->

**EN** We compute the ArtifactReward using the normalized probability of the model answering “no”, where a higher “no” probability indicates a higher likelihood of being artifact-free (See Eq. 1). During optimization, we maximize the following log-likelihood objective:

**ZH** 我们用模型回答 no 的归一化概率计算 ArtifactReward，no 的概率越高表示图像无伪影的可能性越大（见式 1）。在优化过程中，我们最大化下述对数似然目标：

<!-- [原子块 · table] L ​ L = y ​ log ​ ( p yes ) + ( 1 − y ) ​ log ​ ( 1 − p yes ) , LL=y\text{log}(p_{\text{yes}})+(1-y)\text{log}(1-p_{\text{yes}}), (2) -->

**EN** where ⟦SLOT_3⟧ is the ground-truth label, and ⟦SLOT_4⟧ denotes the normalized probability assigned to the “yes” token. Algorithm 1 provides the complete APO procedure, with the scoring function ⟦SLOT_5⟧ defined as the log-likelihood above.

**ZH** 其中 ⟦SLOT_3⟧ 为真值标签，⟦SLOT_4⟧ 表示赋给 yes 词元的归一化概率。算法 1 给出了完整的 APO 流程，评分函数 ⟦SLOT_5⟧ 定义为上述对数似然。

**EN** Algorithm 1 Automatic Prompt Optimization for ArtifactReward

**ZH** 算法 1 ArtifactReward 的自动提示优化

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

**EN** An example of the optimized prompt is:

**ZH** 优化后提示的一个示例如下：

<!-- [原子块 · svg]  -->

**EN** This optimized prompt is more explicit and structurally aligned with common artifact patterns, enabling the model to produce more accurate and reliable artifact predictions. As shown in Table 3, our ArtifactReward consistently assigns higher scores to artifact-free images, clearly separating clean generations from those with distortions. This demonstrates the effectiveness of our optimized prompt in enabling a reward model that can reliably detect and penalize generated artifacts.

**ZH** 这一优化后的提示表述更明确，在结构上也更贴合常见的伪影模式，使模型能给出更准确、更可靠的伪影预测。如表 3 所示，我们的 ArtifactReward 能稳定地给无伪影图像打更高分数，把干净的生成结果与存在畸变的结果清楚地区分开来。这证明了我们优化后的提示能够有效支撑一个可靠检测并惩罚生成伪影的奖励模型。

**EN** 7 Additional Experiment Results

**ZH** 7 补充实验结果

**EN** 7.1 Additional Training Dynamics on Janus-Pro-7B

**ZH** 7.1 Janus-Pro-7B 上的补充训练动态

<!-- [原子块 · object]  -->

**EN** (a) HPS - Spatial

**ZH** (a) HPS - 空间

<!-- [原子块 · object]  -->

**EN** (b) Aesthetic Score - Color

**ZH** (b) Aesthetic Score - 颜色

<!-- [原子块 · object]  -->

**EN** (c) DeQA - Spatial

**ZH** (c) DeQA - 空间

<!-- [原子块 · object]  -->

**EN** (d) PickScore - Object

**ZH** (d) PickScore - 物体

<!-- [原子块 · object]  -->

**EN** (e) GDino - Texture

**ZH** (e) GDino - 纹理

<!-- [原子块 · object]  -->

**EN** (f) ORM - Spatial

**ZH** (f) ORM - 空间

<!-- [原子块 · object]  -->

**EN** (g) VQAScore - Numeracy

**ZH** (g) VQAScore - 数量

<!-- [原子块 · object]  -->

**EN** (h) Unified - Numeracy

**ZH** (h) Unified - 数量

<!-- [原子块 · object]  -->

**EN** (i) Artifacts - Object

**ZH** (i) 伪影 - 物体

<!-- [原子块 · object]  -->

**EN** (j) Artifacts - Shape

**ZH** (j) 伪影 - 形状

<!-- [原子块 · object]  -->

**EN** (k) Artifacts - Spatial

**ZH** (k) 伪影 - 空间

<!-- [原子块 · object]  -->

**EN** (l) Artifacts - Texture

**ZH** (l) 伪影 - 纹理

**EN** Figure 4: Evolution of metrics over training steps with different categories of prompts trained on Janus-Pro-7B 4. Blue color denotes the model trained with HPS 42; Orange color denotes the model trained with GDino 25; Green color denotes the model trained with HPS and GDino; Red color denotes the model trained with finetuned ORM 14.

**ZH** 图 4：在 Janus-Pro-7B 4 上训练时，各类提示下各指标随训练步长的演化。蓝色表示用 HPS 42 训练的模型；橙色表示用 GDino 25 训练的模型；绿色表示用 HPS 与 GDino 训练的模型；红色表示用微调版 ORM 14 训练的模型。

**EN** We conducted additional experiments using the larger 7B variant of Janus-Pro 4. The training dynamics of different evaluation metrics are shown in Figure 4. Overall, we observe trends similar to those seen with the 1B model. Optimization under a given reward tends to improve metrics with closely related inductive biases, while degrading performance on metrics that capture different aspects of image quality. For example, the model trained with the GDino reward shows increased GDino and ORM scores, as both scores emphasize object recognition in generated images. In contrast, the model fails to improve HPS, Aesthetic Score, and DeQA, which focus more on color quality and visual appeal. Moreover, across all reward settings, we find that none effectively reduce artifacts in the generated images (Figures 4(i)–4(l)).

**ZH** 我们还在更大的 Janus-Pro 7B 变体 4 上做了补充实验。各评测指标的训练动态如图 4 所示。总体而言，我们观察到的趋势与 1B 模型上的情形相似：在给定奖励下做优化，倾向于提升归纳偏置相近的指标，同时损害那些刻画图像质量其他方面的指标。例如，用 GDino 奖励训练的模型 GDino 与 ORM 分数上升，因为这两个分数都强调生成图像中的物体识别；相比之下，该模型在更关注色彩质量与视觉吸引力的 HPS、Aesthetic Score 与 DeQA 上没有提升。此外，在所有奖励设置下，我们发现没有任何一种奖励能有效减少生成图像中的伪影（图 4(i)–4(l)）。

**EN** 7.2 Detailed Results of WISE benchmark

**ZH** 7.2 WISE 基准的详细结果

**EN** Table 6: Performance on WISE 26 benchmark trained on Janus-Pro-7B 4. WiScore = 0.7 ⟦SLOT_6⟧ Consistency + 0.2 ⟦SLOT_7⟧ Realism + 0.1 ⟦SLOT_8⟧ Aesthetic by the default setting.

**ZH** 表 6：在 Janus-Pro-7B 4 上训练的模型在 WISE 26 基准上的表现。按默认设置，WiScore = 0.7 ⟦SLOT_6⟧ 一致性 + 0.2 ⟦SLOT_7⟧ 真实感 + 0.1 ⟦SLOT_8⟧ 美学。

<!-- [原子块 · table] Method Consistency Realism Aesthetic WiScore Janus-Pro-7B 4 0.4340 0.5470 0.5528 0.4685 HPS 42 0.4160 0.4745 0.6530 0.4514 HPS + Artifact 0.4255 0.6605 0.5815 0.4881 GDino 25 0.4445 0.5170 0.5435 0.46 -->

**EN** Figure 5 presents the full WISE 26 benchmark results across different prompt subcategories and evaluation metrics for Janus-Pro-1B 4 trained with various reward configurations. Across nearly all categories, incorporating our ArtifactReward leads to substantial improvements in image realism, consistently outperforming models trained with baseline rewards. In addition, ArtifactReward enhances image consistency in most subcategories, indicating that reducing structural artifacts not only improves visual plausibility but also strengthens text-image alignment across diverse prompt types. More image illustrations can be found in Figure 7 and Figure 8.

**ZH** 图 5 给出了 Janus-Pro-1B 4 在各种奖励配置下训练时，WISE 26 基准在不同提示子类与评测指标上的完整结果。在几乎所有类别上，引入我们的 ArtifactReward 都带来图像真实感的大幅提升，稳定优于用基线奖励训练的模型。此外，ArtifactReward 在多数子类上还提升了图像一致性，说明减少结构性伪影不仅能改善视觉合理性，也能在多样的提示类型上加强文图对齐。更多图像示例见图 7 与图 8。

**EN** We additionally evaluate our method on the larger Janus-Pro-7B 4 model. As shown in Table 6 and Figure 6, the results mirror those observed with the 1B model, demonstrating that ArtifactReward generalizes effectively across model scales.

**ZH** 我们还在更大的 Janus-Pro-7B 4 模型上评估了我们的方法。如表 6 与图 6 所示，结果与 1B 模型上的观察一致，说明 ArtifactReward 能有效跨模型规模泛化。

**EN** 7.3 Detailed Results of LLM4LLM benchmark

**ZH** 7.3 LLM4LLM 基准的详细结果

**EN** Table 7: Performance on LLM4LLM 37 benchmark trained on Janus-Pro-7B 4.

**ZH** 表 7：在 Janus-Pro-7B 4 上训练的模型在 LLM4LLM 37 基准上的表现。

<!-- [原子块 · table] Method Perception Correspondence All Janus-Pro-7B 4 0.4390 0.5416 0.9806 HPS 42 0.4360 0.5205 0.9564 HPS + Artifact 0.4454 0.5278 0.9732 GDino 25 0.4417 0.5570 0.9987 GDino + Artifact 0.4506 0.5519 1. -->

**EN** Figure 9 presents the LLM4LLM 37 benchmark results across different prompt subcategories and evaluation metrics for Janus-Pro-1B 4 trained with various reward configurations. More image illustrations can be found in Figure 11 and Figure 12.

**ZH** 图 9 给出了 Janus-Pro-1B 4 在各种奖励配置下训练时，LLM4LLM 37 基准在不同提示子类与评测指标上的结果。更多图像示例见图 11 与图 12。

**EN** Additional results trained on Janus-Pro-7B 4 are shown in Table 7 and Figure 10.

**ZH** 在 Janus-Pro-7B 4 上训练的补充结果见表 7 与图 10。

**EN** 7.4 Detailed Results of EVALALIGN benchmark

**ZH** 7.4 EVALALIGN 基准的详细结果

**EN** Table 8: Performance on EvalAlign 35 benchmark trained on Janus-Pro 4.

**ZH** 表 8：在 Janus-Pro 4 上训练的模型在 EvalAlign 35 基准上的表现。

<!-- [原子块 · table] Method Faithfulness 1B 7B Janus-Pro 4 0.7642 0.8694 HPS 42 0.7569 0.8538 HPS + Artifact 0.9302 1.0676 GDino 25 0.7832 0.8956 GDino + Artifact 0.8952 0.9837 ORM 14 0.7560 0.8607 ORM + Artifact 0.9140 0 -->

**EN** We additionally evaluate our method on EVALALIGN 35, a fine-grained, MLLM-based evaluation benchmark for text-to-image models. It uses image faithfulness, how accurately the visual content matches reality or semantics, as one of their image quality measurements. To highlight the impact of our method on reducing such artifacts, we focus on this faithfulness metric.

**ZH** 我们还在 EVALALIGN 35 上评估了我们的方法——这是一个面向文本到图像模型的、基于 MLLM 的细粒度评测基准。它把图像忠实度（即视觉内容在多大程度上准确匹配现实或语义）作为图像质量的衡量维度之一。为突出我们的方法在减少这类伪影上的作用，我们聚焦于这一忠实度指标。

**EN** As shown in Table 8, Figure 13 and 14, incorporating our ArtifactReward consistently leads to substantial improvements, achieving higher scores across nearly all subcategories. These results further confirm that ArtifactReward can enhance semantic plausibility and structural correctness beyond what existing reward models capture.

**ZH** 如表 8、图 13 与图 14 所示，引入我们的 ArtifactReward 能带来稳定而显著的改进，在几乎所有子类上都取得更高分数。这些结果进一步证实，ArtifactReward 能在现有奖励模型所能捕捉的范围之外，提升语义合理性与结构正确性。

<!-- [原子块 · object]  -->

**EN** (a) Realism

**ZH** (a) 真实感

<!-- [原子块 · object]  -->

**EN** (b) Consistency

**ZH** (b) 一致性

<!-- [原子块 · object]  -->

**EN** (c) WiScore

**ZH** (c) WiScore

**EN** Figure 5: Performance on WISE 26 benchmark across different categories trained on Janus-Pro-1B 4.

**ZH** 图 5：在 Janus-Pro-1B 4 上训练的模型在 WISE 26 基准上各类别的表现。

<!-- [原子块 · object]  -->

**EN** (a) Realism

**ZH** (a) 真实感

<!-- [原子块 · object]  -->

**EN** (b) Consistency

**ZH** (b) 一致性

<!-- [原子块 · object]  -->

**EN** (c) WiScore

**ZH** (c) WiScore

**EN** Figure 6: Performance on WISE 26 benchmark across different categories trained on Janus-Pro-7B 4

**ZH** 图 6：在 Janus-Pro-7B 4 上训练的模型在 WISE 26 基准上各类别的表现

<!-- [原子块 · img]  -->

**EN** (a) HPS

**ZH** (a) HPS

<!-- [原子块 · img]  -->

**EN** (b) HPS + Artifact

**ZH** (b) HPS + Artifact

<!-- [原子块 · img]  -->

**EN** (c) GDino

**ZH** (c) GDino

<!-- [原子块 · img]  -->

**EN** (d) GDino + Artifact

**ZH** (d) GDino + Artifact

<!-- [原子块 · img]  -->

**EN** (e) HPS + GDino

**ZH** (e) HPS + GDino

<!-- [原子块 · img]  -->

**EN** (f) HPS + GDino + Artifact

**ZH** (f) HPS + GDino + Artifact

<!-- [原子块 · img]  -->

**EN** (g) ORM

**ZH** (g) ORM

<!-- [原子块 · img]  -->

**EN** (h) ORM + Artifact

**ZH** (h) ORM + Artifact

**EN** Figure 7: Images generated with prompt “An iconic bridge, known for its red hue and location over a famous bay in San Francisco” in WISE 26 benchmark under different training reward configurations trained on Janus-Pro-1B 4.

**ZH** 图 7：在 Janus-Pro-1B 4 上训练时，用提示“一座标志性的桥梁，以红色著称，位于旧金山一处著名海湾之上”在 WISE 26 基准上、不同训练奖励配置下生成的图像。

<!-- [原子块 · img]  -->

**EN** (a) HPS

**ZH** (a) HPS

<!-- [原子块 · img]  -->

**EN** (b) HPS + Artifact

**ZH** (b) HPS + Artifact

<!-- [原子块 · img]  -->

**EN** (c) GDino

**ZH** (c) GDino

<!-- [原子块 · img]  -->

**EN** (d) GDino + Artifact

**ZH** (d) GDino + Artifact

<!-- [原子块 · img]  -->

**EN** (e) HPS + GDino

**ZH** (e) HPS + GDino

<!-- [原子块 · img]  -->

**EN** (f) HPS + GDino + Artifact

**ZH** (f) HPS + GDino + Artifact

<!-- [原子块 · img]  -->

**EN** (g) ORM

**ZH** (g) ORM

<!-- [原子块 · img]  -->

**EN** (h) ORM + Artifact

**ZH** (h) ORM + Artifact

**EN** Figure 8: Images generated with prompt “Siblings of identical twins” in WISE 26 benchmark under different training reward configurations trained on Janus-Pro-1B 4.

**ZH** 图 8：在 Janus-Pro-1B 4 上训练时，用提示“同卵双胞胎的兄弟姐妹”在 WISE 26 基准上、不同训练奖励配置下生成的图像。

<!-- [原子块 · object]  -->

**EN** (a) Perception

**ZH** (a) Perception

<!-- [原子块 · object]  -->

**EN** (b) Correspondence

**ZH** (b) Correspondence

**EN** Figure 9: Performance on LLM4LLM 37 benchmark across different categories trained on Janus-Pro-1B 4

**ZH** 图 9：在 Janus-Pro-1B 4 上训练的模型在 LLM4LLM 37 基准上各类别的表现

<!-- [原子块 · object]  -->

**EN** (a) Perception

**ZH** (a) Perception

<!-- [原子块 · object]  -->

**EN** (b) Correspondence

**ZH** (b) Correspondence

**EN** Figure 10: Performance on LLM4LLM 37 benchmark across different categories trained on Janus-Pro-7B 4

**ZH** 图 10：在 Janus-Pro-7B 4 上训练的模型在 LLM4LLM 37 基准上各类别的表现

<!-- [原子块 · img]  -->

**EN** (a) HPS

**ZH** (a) HPS

<!-- [原子块 · img]  -->

**EN** (b) HPS + Artifact

**ZH** (b) HPS + Artifact

<!-- [原子块 · img]  -->

**EN** (c) GDino

**ZH** (c) GDino

<!-- [原子块 · img]  -->

**EN** (d) GDino + Artifact

**ZH** (d) GDino + Artifact

<!-- [原子块 · img]  -->

**EN** (e) HPS + GDino

**ZH** (e) HPS + GDino

<!-- [原子块 · img]  -->

**EN** (f) HPS + GDino + Artifact

**ZH** (f) HPS + GDino + Artifact

<!-- [原子块 · img]  -->

**EN** (g) ORM

**ZH** (g) ORM

<!-- [原子块 · img]  -->

**EN** (h) ORM + Artifact

**ZH** (h) ORM + Artifact

**EN** Figure 11: Images generated with prompt “A teacher in a white blouse stands at the blackboard, her curly brown hair tied back in a ponytail.” in LLM4LLM 37 benchmark under different training reward configurations trained on Janus-Pro-1B 4.

**ZH** 图 11：在 Janus-Pro-1B 4 上训练时，用提示“一位穿白色衬衫的老师站在黑板前，她卷曲的棕色头发扎成马尾。”在 LLM4LLM 37 基准上、不同训练奖励配置下生成的图像。

<!-- [原子块 · img]  -->

**EN** (a) HPS

**ZH** (a) HPS

<!-- [原子块 · img]  -->

**EN** (b) HPS + Artifact

**ZH** (b) HPS + Artifact

<!-- [原子块 · img]  -->

**EN** (c) GDino

**ZH** (c) GDino

<!-- [原子块 · img]  -->

**EN** (d) GDino + Artifact

**ZH** (d) GDino + Artifact

<!-- [原子块 · img]  -->

**EN** (e) HPS + GDino

**ZH** (e) HPS + GDino

<!-- [原子块 · img]  -->

**EN** (f) HPS + GDino + Artifact

**ZH** (f) HPS + GDino + Artifact

<!-- [原子块 · img]  -->

**EN** (g) ORM

**ZH** (g) ORM

<!-- [原子块 · img]  -->

**EN** (h) ORM + Artifact

**ZH** (h) ORM + Artifact

**EN** Figure 12: Images generated with prompt “a dog is smiling with happy emotion. He find a lot of delicious food.” in LLM4LLM 37 benchmark under different training reward configurations trained on Janus-Pro-1B 4.

**ZH** 图 12：在 Janus-Pro-1B 4 上训练时，用提示“一只狗带着开心的情绪在微笑。他找到了很多美味的食物。”在 LLM4LLM 37 基准上、不同训练奖励配置下生成的图像。

**EN** Figure 13: Performance on EvalAlign 35 benchmark across different categories trained on Janus-Pro-1B 4.

**ZH** 图 13：在 Janus-Pro-1B 4 上训练的模型在 EvalAlign 35 基准上各类别的表现。

<!-- [原子块 · object]  -->

**EN** Figure 14: Performance on EvalAlign 35 benchmark across different categories trained on Janus-Pro-7B 4.

**ZH** 图 14：在 Janus-Pro-7B 4 上训练的模型在 EvalAlign 35 基准上各类别的表现。

<!-- [原子块 · object]  -->
