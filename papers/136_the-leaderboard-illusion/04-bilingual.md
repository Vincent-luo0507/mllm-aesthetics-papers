# 排行榜幻象

> 原标题：The Leaderboard Illusion
> 作者：Shivalika Singh, Yiyang Nan, Alex Wang, Daniel D'Souza, Sayash Kapoor, Ahmet Üstün, Sanmi Koyejo, Yuntian Deng, Shayne Longpre, Noah A. Smith, Beyza Ermis, Marzieh Fadaee 等 · arXiv:2504.20879 · 2025-04-29

<!-- [原子块 · verbatim] The Leaderboard Illusion -->

<!-- [原子块 · verbatim] Abstract -->

<!-- [原子块 · verbatim] Measuring progress is fundamental to the advancement of any scientific field. As benchmarks play an increasingly central role, they also grow more susceptible to distortion. Chatbot Arena has emerged  -->

**EN** Cohere Labs Cohere Princeton University Stanford University University of Waterloo Massachusetts Institute of Technology Allen Institute for Artificial Intelligence University of Washington \corresponding[*]{shivalikasingh, marzieh, sarahooker}@cohere.com

**ZH** Cohere Labs、Cohere、普林斯顿大学、斯坦福大学、滑铁卢大学、麻省理工学院、艾伦人工智能研究院、华盛顿大学 \corresponding[*]{shivalikasingh, marzieh, sarahooker}@cohere.com

<!-- [原子块 · img]  -->

**EN** Figure 1: Overview of key insights. We investigate the prevalence of undisclosed private testing and selective score reporting on the Arena (Section 3), and highlight significant data access disparities between proprietary and open-source providers (Section 4.1). These disparities enable overfitting to the Arena (Section 4.2). Furthermore, model deprecation practices lack transparency, with many models silently deprecated without any notification to providers. We demonstrate how these deprecations contribute to unreliable rankings on the leaderboard (Section 5).

**ZH** 图 1：核心发现概览。我们考察了 Arena 上未披露的私有测试与选择性分数报告有多普遍（第 3 节），并指出专有与开源提供方之间显著的数据访问差距（第 4.1 节）。这些差距使提供方得以对 Arena 过拟合（第 4.2 节）。此外，模型下架实践缺乏透明度，许多模型被静默下架，且未向提供方发出任何通知。我们展示了这些下架如何导致排行榜排名不可靠（第 5 节）。

**EN** 1 Introduction

**ZH** 1 引言

**EN** Any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes. — Charles A. E. Goodhart

**ZH** 任何被观察到的统计规律性，一旦为控制目的而对其施加压力，就往往会崩塌。——Charles A. E. Goodhart

**EN** Benchmarks have long played an integral role in the development of machine learning systems (Church 2018; Koch & Peterson 2024), from the early days of NLP (Harman 1993; Koehn & Monz 2006, e.g., TREC competitions and WMT shared tasks,) to the recent flurry of deep learning models (Deng et al. 2009, e.g., ImageNet,), to the rise of large language models (Wang et al. 2018, e.g., GLUE,). A meaningful benchmark demonstrates the relative merits of new research ideas over existing ones, and thereby heavily influences research directions, funding decisions, and, ultimately, the shape of progress in our field. The recent meteoric rise of generative AI models—in terms of public attention, commercial adoption, and the scale of compute and funding involved (Kaplan et al. 2020; Hoffmann et al. 2022; Samsi et al. 2023; Hooker 2024)—has substantially increased the stakes and pressure placed on leaderboards (Orr & Kang 2024).

**ZH** 基准长期以来在机器学习系统的发展中扮演着不可或缺的角色（Church 2018; Koch & Peterson 2024），从 NLP 早期（Harman 1993; Koehn & Monz 2006，例如 TREC 竞赛与 WMT 共享任务），到近年深度学习模型的涌现（Deng et al. 2009，例如 ImageNet），再到大语言模型的兴起（Wang et al. 2018，例如 GLUE）。一个有意义的基准能展示新研究思路相对于已有思路的相对优势，因而深刻影响研究方向、资助决策，并最终塑造本领域的进步形态。生成式 AI 模型近年的急剧崛起——体现在公众关注、商业采用，以及所涉算力与资金的规模上（Kaplan et al. 2020; Hoffmann et al. 2022; Samsi et al. 2023; Hooker 2024）——大幅提高了押在排行榜上的赌注与压力（Orr & Kang 2024）。

**EN** Recently, Chatbot Arena has become the de facto standard for comparing generative AI models, holding enormous sway over media11 1 https://www.wsj.com/tech/ai/the-uc-berkeley-project-that-is-thewai-industrys-obsession-bc68b3e322 2 https://www.bloomberg.com/news/articles/2025-02-18/before-deepseek-blew-up-one-website-announced-its-arrival, the AI industry (Maslej et al. 2025), and academia (Grattafiori et al. 2024; Yang et al. 2024). Created in 2023, Chatbot Arena rates LLMs by allowing anyone to submit a prompt and subsequently rank two anonymous responses from different models. Chatbot Arena quickly rose to prominence because it helped fill a critical gap in evaluation at a time of rapid technological change. As generative AI technology has grown more capable, academic multiple-choice evaluations (Hendrycks et al. 2021; Liang et al. 2022; Romanou et al. 2024; Singh et al. 2024b; Wang et al. 2024; Adelani et al. 2025; Salazar et al. 2025) have failed to reflect the real-world open-ended use cases these models are now being used for (Üstün et al. 2024; Chiang et al. 2024; Mizrahi et al. 2024). As a dynamic, user-driven evaluation framework where new questions can be asked daily, Chatbot Arena can, at least in principle, evolve alongside model capabilities. Furthermore, the open-ended nature of the interaction can capture emerging real-world use cases that differ from those initially envisioned by model creators.

**ZH** 近来，Chatbot Arena 已成为比较生成式 AI 模型的事实标准，对媒体11 1 https://www.wsj.com/tech/ai/the-uc-berkeley-project-that-is-thewai-industrys-obsession-bc68b3e322 2 https://www.bloomberg.com/news/articles/2025-02-18/before-deepseek-blew-up-one-website-announced-its-arrival、AI 产业（Maslej et al. 2025）与学术界（Grattafiori et al. 2024; Yang et al. 2024）都握有巨大影响力。Chatbot Arena 创建于 2023 年，它通过让任何人提交提示、随后对来自不同模型的两个匿名回复排序，来对 LLM 评分。Chatbot Arena 之所以迅速崛起，是因为它在技术快速变革的时期填补了评测中的一项关键空白。随着生成式 AI 技术能力增强，学术型的多项选择评测（Hendrycks et al. 2021; Liang et al. 2022; Romanou et al. 2024; Singh et al. 2024b; Wang et al. 2024; Adelani et al. 2025; Salazar et al. 2025）已无法反映这些模型如今被投入使用的真实开放式场景（Üstün et al. 2024; Chiang et al. 2024; Mizrahi et al. 2024）。作为一个动态的、用户驱动的评测框架，新问题可以每天被提出，Chatbot Arena 至少在原则上能够与模型能力同步演进。此外，交互的开放式性质能捕捉到与模型创造者最初设想不同的新兴真实用例。

<!-- [原子块 · object]  -->

**EN** Figure 2: Number of public models vs. maximum arena score per provider. Marker size indicates total number of battles played. Proprietary model providers tend to achieve higher leaderboard scores, which appear to correlate with both the number of models they release and the number of Arena battles played. While model capability is an important factor, we explore in Section 3 and Section 4 how increased exposure to the Arena (through more models and battles) may confer additional advantages, such as better model selection or adaptation to the evaluation distribution. This figure summarizes publicly disclosed results as of April 23rd, 2025.

**ZH** 图 2：各提供方的公开模型数量 vs. 最高 Arena 分数。标记大小表示参与的对战总次数。专有模型提供方往往取得更高的排行榜分数，而这似乎与他们发布的模型数量以及在 Arena 上参与的对战次数都相关。虽然模型能力是重要因素，我们在第 3 节与第 4 节探讨了更多地暴露于 Arena（通过更多模型和更多对战）可能带来哪些额外优势，例如更好的模型选择或对评测分布的适应。本图汇总了截至 2025 年 4 月 23 日的公开披露结果。

**EN** However, the over-reliance on a single leaderboard creates a risk that providers may overfit to the aspects of leaderboard performance, without genuinely advancing the technology in meaningful ways (Ensmenger 2011; Thomas & Uminsky 2020; Raji et al. 2021; Bowman & Dahl 2021). As Goodhart’s Law states, when a measure becomes a target, it ceases to be a good measure. In this work, we show that willful engagement from a handful of providers along with preferential policies from Chatbot Arena towards the same small group have amplified the potential for gamification, in place of innovative progress.

**ZH** 然而，对单一排行榜的过度依赖带来一种风险：提供方可能对排行榜表现的某些方面过拟合，而没有以有意义的方式真正推进技术（Ensmenger 2011; Thomas & Uminsky 2020; Raji et al. 2021; Bowman & Dahl 2021）。正如古德哈特定律所言：当一项度量成为目标，它就不再是好的度量。在本文中，我们表明，少数提供方有意为之的参与，加上 Chatbot Arena 对同一小团体的倾斜性政策，放大了策略性博弈而非创新进步的空间。

**EN** Our systematic review of Chatbot Arena involves combining data sources encompassing 2M battles, auditing 42 providers and 243 models across a fixed time period (January 2024 - April 2025). This comprehensive analysis reveals that over an extended period, a handful of preferred providers have been granted disproportionate access to data and testing. In particular, we identify an undisclosed Chatbot Arena policy that allows a small group of preferred model providers to test many model variants in private before releasing only the best-performing checkpoint. Using Arena data, we simulate and demonstrate how this strategy distorts overall arena ratings by beneficially skewing results. In addition, we find substantial data asymmetries are apparent regarding the amount of feedback data given to proprietary vs. open-weight vs. open-source model providers. This is due to a combination of unequal sampling rates (how often a model appears in a Chatbot Arena battle) and deprecation policies (which models are retired from the arena). We show that these differences lead to distorted and unreliable Arena rankings and create conditions in which providers may be overfitting to Arena-specific dynamics rather than general model quality. We find:

**ZH** 我们对 Chatbot Arena 的系统性审查合并了涵盖 200 万场对战的数据源，在固定时间区间（2024 年 1 月—2025 年 4 月）内审计了 42 家提供方与 243 个模型。这一全面分析揭示，在相当长的一段时间内，少数受偏爱的提供方获得了不成比例的数据与测试机会。具体地，我们识别出 Chatbot Arena 一项未披露的政策：它允许一小部分受偏爱的模型提供方在私下测试许多模型变体，之后只发布表现最好的检查点。借助 Arena 数据，我们模拟并展示了这一策略如何通过有利地扭曲结果而扰乱整体 Arena 评分。此外，我们发现，在提供给专有、开放权重与开源模型提供方的反馈数据量上存在显著的数据不对称。这源于不平等的采样率（一个模型出现在 Chatbot Arena 对战中的频率）与下架政策（哪些模型被从 Arena 中退役）的共同作用。我们表明，这些差异导致 Arena 排名失真且不可靠，并造成了「提供方可能对 Arena 特有动态而非通用模型质量过拟合」的条件。我们发现：

<!-- [原子块 · object]  -->

**EN** Figure 3: Volume of Arena battles involving proprietary, open-weight, and fully open-source model providers from January 2024 to March 2025, based on leaderboard-stats. Proprietary models consistently received the largest share of data—ranging from 54.3% to 70.1%. Open-weight and fully open-source models receive significantly less data, in some cases receiving less than half the amount of data as proprietary developers. This imbalance in data access exacerbates the performance gap, reinforcing unequal access to high-quality in-distribution data.

**ZH** 图 3：2024 年 1 月至 2025 年 3 月，涉及专有、开放权重与完全开源模型提供方的 Arena 对战量，基于 leaderboard-stats。专有模型始终获得最大的数据份额——在 54.3% 到 70.1% 之间。开放权重与完全开源模型获得的数据显著更少，某些情况下不足专有开发者的一半。这种数据访问上的失衡加剧了性能差距，强化了对高质量同分布数据的不平等获取。

**EN** 1. Preferential treatment around private testing and retraction. Chatbot Arena has an unstated policy of allowing select providers to test many submissions privately in parallel. We show that certain model developers (most notably Meta, Google, Open AI and Amazon) have benefited from extensive private testing. In a single month, we observe as many as 27 models from Meta being tested privately on Chatbot Arena in the lead up to llama 4 release. Notably, we find that Chatbot Arena does not require all submitted models to be made public, and there is no guarantee that the version appearing on the public leaderboard matches the publicly available API33 3 https://x.com/lmarena_ai/status/190939781743481656244 4 https://www.theverge.com/meta/645012/meta-llama-4-maverick-benchmarks-gaming. We show with real-world experiments and simulations that the ability to select the best-scoring variant from ⟦SLOT_0⟧ models enables systematic gaming of the Arena rating.

**ZH** 1. 围绕私有测试与撤回的差别待遇。Chatbot Arena 有一项未言明的政策，允许部分提供方并行私下测试多个提交。我们表明，某些模型开发者（最明显的是 Meta、Google、OpenAI 和 Amazon）从大量私有测试中获益。在 Llama 4 发布前的一个月内，我们观察到 Meta 有多达 27 个模型在 Chatbot Arena 上被私下测试。值得注意的是，我们发现 Chatbot Arena 并不要求所有提交的模型都必须公开，也无法保证出现在公开排行榜上的版本与公开可用的 API 一致33 3 https://x.com/lmarena_ai/status/190939781743481656244 4 https://www.theverge.com/meta/645012/meta-llama-4-maverick-benchmarks-gaming。我们通过真实实验与模拟表明，从 ⟦SLOT_0⟧ 个模型中选择得分最高变体的能力，使系统性博弈 Arena 评分成为可能。

**EN** 2. Far more data is released to proprietary model providers. Chatbot Arena is a community-driven leaderboard that benefits from free, crowdsourced feedback provided by everyday users. However, proprietary model providers collect significantly more test prompts and model battle outcomes than others. Google and OpenAI have received an estimated 19.2% and 20.4% of all test prompts on the arena, respectively. We estimate this based on the share of total battles played by the models of different providers on the Arena (as shown in Figure 4). In contrast, a combined 41 fully open-source models have only received an estimated 8.9% of the total data, collectively.

**ZH** 2. 专有模型提供方获得的数据要多得多。Chatbot Arena 是一个社区驱动的排行榜，受益于普通用户免费提供的众包反馈。然而，专有模型提供方比其他方收集到多得多的测试提示与模型对战结果。据估计，Google 与 OpenAI 分别获得了 Arena 上全部测试提示的 19.2% 与 20.4%。我们依据不同提供方的模型在 Arena 上参与对战总量的占比做出这一估计（如图 4 所示）。相比之下，合计 41 个完全开源模型总共只获得了估计 8.9% 的数据。

**EN** 3. Chatbot Arena data access drives significant performance gains. The differences in data access between providers matter; we estimate that by training on Chatbot Arena data, model ranking can be improved significantly. In a controlled experimental setting, we observe that increasing the arena training data proportion from (0% ⟦SLOT_1⟧70%) more than doubles the win-rates from 23.5% to 49.9% on ArenaHard (Li et al. 2024c). We believe this is a conservative estimate, as a subset of providers have disproportionate access to private API data, which, if used, can potentially yield even greater performance gains.

**ZH** 3. Chatbot Arena 数据访问带来显著的性能增益。提供方之间的数据访问差异确实重要；我们估计，通过在 Chatbot Arena 数据上训练，模型排名可以被显著提升。在受控实验设定下，我们观察到把 Arena 训练数据占比从（0% ⟦SLOT_1⟧70%）提高，会使 ArenaHard（Li et al. 2024c）上的胜率从 23.5% 翻倍以上至 49.9%。我们认为这是一个保守估计，因为部分提供方拥有不成比例的私有 API 数据访问权，若加以利用，可能产生更大的性能增益。

**EN** 4. Deprecations can result in unreliable model rankings. As shown in Figure 18, out of 243 public models, 205 have been silently deprecated. This is a significantly higher number than the 47 models officially listed as deprecated as part of Chatbot Arena’s backend codebase, FastChat55 5 http://github.com/lm-sys/FastChat/blob/0e6d3e4beaab66f4d3f93db72541a4abab8af28d/fastchat/serve/monitor/monitor_md.py#L7 . We show that deprecation can violate key assumptions of the Bradley-Terry model (Bradley & Terry 1952), which underpins Arena scoring, thereby reducing the reliability of the leaderboard rankings. Critically, we find that open-weight and open-source models are far more likely to be deprecated and, hence, receive unreliable ratings. Among the models that are silently deprecated, 64% are open-weight or fully open-source.

**ZH** 4. 下架会导致模型排名不可靠。如图 18 所示，在 243 个公开模型中，有 205 个被静默下架。这一数字远高于 Chatbot Arena 后端代码库 FastChat55 5 http://github.com/lm-sys/FastChat/blob/0e6d3e4beaab66f4d3f93db72541a4abab8af28d/fastchat/serve/monitor/monitor_md.py#L7 中官方列为已下架的 47 个模型。我们表明，下架会违反 Bradley-Terry 模型（Bradley & Terry 1952）的关键假设，而该模型正是 Arena 评分的基础，因此会降低排行榜排名的可靠性。关键的是，我们发现开放权重与开源模型被下架的可能性远高于专有模型，因而获得不可靠的评分。在被静默下架的模型中，64% 是开放权重或完全开源的。

<!-- [原子块 · object]  -->

**EN** Figure 4: Data availability to model providers. We observe large differences in data access between providers, with 61.4% of all data going to proprietary providers.

**ZH** 图 4：各模型提供方的数据可得性。我们观察到提供方之间的数据访问差异巨大，全部数据的 61.4% 流向了专有提供方。

<!-- [原子块 · object]  -->

**EN** Figure 5: Maximum observed sampling rate for models from different providers. The sampling rate determines the amount of times a model is shown to everyday users, and the amount of data a provider receives. We observe large discrepancies across providers, with substantially higher sampling rates for OpenAI, Google, xAI, and Meta compared to others.

**ZH** 图 5：不同提供方模型观测到的最高采样率。采样率决定一个模型被展示给普通用户的次数，以及一个提供方获得的数据量。我们观察到各提供方之间差异巨大，OpenAI、Google、xAI 与 Meta 的采样率明显高于其他方。

**EN** Our role in both participating in the leaderboard and providing an overview of its limitations. It is important to acknowledge that a subset of the authors of this paper have submitted several open-weight models to Chatbot Arena: command-r (Cohere 2024), command-r-plus (Cohere 2024) in March 2024, aya-expanse (Dang et al. 2024b) in October 2024, aya-vision (Cohere 2025) in March 2025, command-a (Cohere et al. 2025) in March 2025. We started this extensive study driven by this submission experience with the leaderboard. While submitting Aya Expanse (Dang et al. 2024b) for testing, we observed that our open-weight model appeared to be notably undersampled compared to proprietary models — a discrepancy that is further reflected in Figures 3, 4, and 5. In response, we contacted the Chatbot Arena organizers to inquire about these differences in November 2024. In the course of our discussions, we learned that some providers were testing multiple variants privately, a practice that appeared to be selectively disclosed and limited to only a few model providers. We believe that our initial inquiries partly prompted Chatbot Arena to release a public blog in December 2024 detailing their benchmarking policy66 6 https://drive.google.com/file/d/1reook2cjwq81xD6Yn528KOLWeWRy0ZvN/view?usp=sharing, which committed to a consistent sampling rate across models. However, subsequent anecdotal observations of continued sampling disparities and the presence of numerous models with private aliases motivated us to undertake a more systematic analysis. As part of this analysis, we launched private variants to estimate the benefit of multiple submissions and retraction. We report on the results of this real-world study in Section 3.3. Consequently, Cohere appears in Figure 6 and Figure 9 as having private variants. Before this period, Cohere had not launched any private testing.

**ZH** 我们在参与排行榜并概述其局限中的双重角色。需要说明的是，本文部分作者曾向 Chatbot Arena 提交过若干开放权重模型：2024 年 3 月的 command-r（Cohere 2024）与 command-r-plus（Cohere 2024）、2024 年 10 月的 aya-expanse（Dang et al. 2024b）、2025 年 3 月的 aya-vision（Cohere 2025）与 command-a（Cohere et al. 2025）。我们开展这项大规模研究的起因正是这段提交经历。在提交 Aya Expanse（Dang et al. 2024b）测试时，我们注意到我们的开放权重模型相比专有模型似乎被明显低采样——这一差异也体现在图 3、图 4 与图 5 中。为此，我们于 2024 年 11 月联系了 Chatbot Arena 组织方，询问这些差异。在交流过程中，我们得知部分提供方正在私下测试多个变体，这一做法似乎是选择性披露的，且仅限于少数几家模型提供方。我们认为，我们最初的问询在一定程度上促使 Chatbot Arena 于 2024 年 12 月发布了一篇公开博客，详细说明其基准评测政策66 6 https://drive.google.com/file/d/1reook2cjwq81xD6Yn528KOLWeWRy0ZvN/view?usp=sharing，并承诺在各模型间采用一致的采样率。然而，此后关于采样差距持续存在的零星观察，以及大量带有私有别名的模型的出现，促使我们开展更系统的分析。作为分析的一部分，我们投放了私有变体，以估计多次提交与撤回的收益。我们在第 3.3 节报告这项真实研究的结果。因此，Cohere 在图 6 与图 9 中显示为拥有私有变体。在此之前，Cohere 从未发起过任何私有测试。

**EN** While our work points out limitations and unreliability issues with Chatbot Arena, it is important to acknowledge that Chatbot Arena originated as an academic-sponsored leaderboard that took on pronounced importance to the machine learning community. It takes considerable effort to coordinate a leaderboard, and arena organizers have often faced large demands on their time from supporting the addition of models from many different model providers. Hence, while we point out systematic issues with Chatbot Arena as it is now, we also believe some of these issues may have emerged gradually as successive design choices and concessions to certain large providers accumulated and introduced unreliability. We believe that there are reasonable interventions that the organizers can do to restore scientific accuracy and renew trust in the leaderboard. We have directly shared our recommendations with Chatbot Arena prior to releasing this work. We include these here and also share in Section 6 for a complete discussion.

**ZH** 虽然我们的工作指出了 Chatbot Arena 的局限与可靠性问题，但必须承认，Chatbot Arena 最初是一个由学术界发起的排行榜，后来对机器学习社区变得极为重要。协调运营一个排行榜需要付出巨大努力，而 Arena 组织者在支持来自众多不同模型提供方的模型接入上，常常面临时间上的巨大压力。因此，尽管我们指出了 Chatbot Arena 现状中的系统性问题，我们也认为其中一些问题可能是逐步出现的——随着一连串设计选择和对某些大提供方的让步不断累积，最终引入了不可靠性。我们相信，组织者可以采取合理的干预措施，以恢复排行榜的科学准确性并重获信任。在发布本工作之前，我们已直接向 Chatbot Arena 分享了我们的建议。我们把这些建议收录于此，并在第 6 节给出完整讨论。

<!-- [原子块 · svg]  -->

**EN** 2 Overview of Methodology

**ZH** 2 方法概述

**EN** To measure is to know — Lord Kelvin

**ZH** 测度即知。——开尔文勋爵

**EN** Leaderboards have played a pivotal role in the computer science field in driving technological progress (Koch & Peterson 2024). A desirable goal of a general benchmark is to reliably rank models according to real-world capabilities and preferences. Hence, if one system significantly outperforms another, then the result should be strong evidence that the higher-ranked system is better at the task (Bowman & Dahl 2021; Rodriguez et al. 2021). If a leaderboard is not representative of real performance gains, it can lead practitioners and researchers towards less impactful areas of intervention and inquiry. In some cases, this misalignment enables gaming of the system—where participants optimize for leaderboard metrics rather than real-world utility. As a result, the gap between reported performance and actual value in deployment can continue to widen. Ultimately, the goal of our work is to ask whether the rankings of Chatbot Arena are a reliable ranking of generative AI models. To answer this, across the sections that follow, we will consider and answer the following questions:

**ZH** 排行榜在计算机科学领域推动技术进步方面一直起着关键作用（Koch & Peterson 2024）。一个通用基准的理想目标，是依据真实世界的能力与偏好对模型做可靠排序。因此，若一个系统显著优于另一个，该结果就应当是有力证据，表明排名更高的系统在该任务上更好（Bowman & Dahl 2021; Rodriguez et al. 2021）。如果一个排行榜不能代表真实的性能增益，它就会把实践者与研究者引向影响力更弱的干预与探究方向。在某些情况下，这种错位会催生对系统的博弈——参与者针对排行榜指标而非真实效用做优化。结果，报告性能与部署中实际价值之间的鸿沟会持续扩大。归根结底，我们工作的目标是追问：Chatbot Arena 的排名是否是生成式 AI 模型的可靠排序。为回答这一问题，在后续各节中，我们将思考并回答以下问题：

**EN** 1. Private Testing and Selective Disclosure (Section 3) What is the impact of the undisclosed policy of multiple private variant testing and selective retraction on Arena scores?

**ZH** 1. 私有测试与选择性披露（第 3 节） 未披露的「多私有变体测试 + 选择性撤回」政策对 Arena 分数有何影响？

**EN** 2. Data Access Asymmetries (Section 4.1) What factors lead to large asymmetries between providers in data access on the Chatbot Arena?

**ZH** 2. 数据访问不对称（第 4.1 节） 哪些因素导致了 Chatbot Arena 上各提供方之间巨大的数据访问不对称？

**EN** 3. Risk of Overfitting (Section 4.2) How do asymmetries in data access impact Arena scores?

**ZH** 3. 过拟合风险（第 4.2 节） 数据访问的不对称如何影响 Arena 分数？

**EN** 4. Model Deprecation (Section 5) What is the impact of Chatbot Arena model deprecation policy on Arena score reliability?

**ZH** 4. 模型下架（第 5 节） Chatbot Arena 的模型下架政策对 Arena 分数的可靠性有何影响？

**EN** To gain insights and analyze various trends in the Chatbot Arena leaderboard, we leverage multiple data sources. In total, our real-world data sources encompass 2M battles and cover 243 models across 42 providers. We present the overview of each data source in Table 1 and describe the different datasets in more details in Appendix D. Across our analyses, we group models by the licenses reported on Chatbot Arena into proprietary, open-weights, and open source to understand overall trends. This allows us to gain insight into who benefits the most from the Chatbot Arena which is a free and open community resource. We report details of what licenses are grouped into each category in Appendix F. We note that many open-weights models are extremely performant and include Aya family of models (Dang et al. 2024b; Üstün et al. 2024), Meta models (Meta 2025) and Gemma family of models (Team et al. 2025).

**ZH** 为洞察并分析 Chatbot Arena 排行榜中的各种趋势，我们利用了多个数据源。总体来看，我们的真实数据源涵盖 200 万场对战，覆盖 42 家提供方的 243 个模型。我们在表 1 中给出各数据源的概览，并在附录 D 更详细地描述各个数据集。在所有分析中，我们按 Chatbot Arena 上申报的许可证把模型归为专有、开放权重与开源三类，以了解整体趋势。这使我们能够看清谁从 Chatbot Arena 这一免费开放的社区资源中获益最多。我们在附录 F 中报告了哪些许可证被归入各类的细节。我们注意到，许多开放权重模型性能极佳，其中包括 Aya 系列模型（Dang et al. 2024b; Üstün et al. 2024）、Meta 的模型（Meta 2025）以及 Gemma 系列模型（Team et al. 2025）。

**EN** Table 1: A summary of datasets we constructed, their sources, and the research questions they enabled us to answer. These datasets can be of one of the following types: battles only ( ), conversations only ( ), battles with conversations, ( ) and leaderboard updates ( ). Depending on the dataset type, it either contains prompts ( ) or doesn’t ( ). Accessibility of the datasets is indicated using public ( ) or private ( ).

**ZH** 表 1：我们构建的数据集、其来源，以及它们使我们得以回答的研究问题的摘要。这些数据集可属以下类型之一：仅对战、仅对话、含对话的对战，以及排行榜更新。视数据集类型而定，它可能包含提示，也可能不包含。数据集的可获取性用公开或私有表示。

<!-- [原子块 · table] Name Fields Source / Type Prompts? Size Period Historical Battles battle dates, category & language tags Arena-human-preference-100k 7 7 7 https://huggingface.co/datasets/lmarena-ai/arena-human-prefer -->

**EN** 2.1 Introduction to the Arena Score

**ZH** 2.1 Arena 分数简介

**EN** The Arena score is the key metric used in Chatbot Arena to rank models based on how humans judge their performance. In Arena, users engage in pairwise comparisons, voting on which of two models performs better (or declaring a tie) in a given interaction. A naive way to compute rankings would be to average each model’s win-rates, simply counting how often they win. However, this approach does not consider the strength of the opponents and requires all models to play against each other. Furthermore, averaging win-rates treats all wins equally, which can lead to misleading or unfair rankings, especially when models face opponents of varying strength levels.

**ZH** Arena 分数是 Chatbot Arena 用来依据人类对模型表现的评价对模型排序的核心指标。在 Arena 中，用户进行成对比较，在一次交互中投票选出两个模型中表现更好的一个（或宣布平局）。一种朴素的计算排名方式是取每个模型胜率的平均，只统计它们获胜的次数。然而，这种做法没有考虑对手的强弱，并且要求所有模型两两对战过。此外，平均胜率对所有胜利一视同仁，这会导致排名具有误导性或不公平，尤其当模型面对强弱不一的对手时。

**EN** Instead, Chatbot Arena ranks models based on their Arena Score, which is a normalized version of the Bradley-Terry (BT) model (Bradley & Terry 1952), a probabilistic framework for estimating skill levels based on pairwise comparisons. BT is a widely used model to estimate skill levels in diverse fields such as online gaming (e.g., StarCraft II) (Leitner et al. 2010; Liquipedia 2019; Wise 2021, i.a.) and sports rankings (Glickman 1999; Hunter 2004b). Compared to alternative systems like Elo (Elo 1978; Boubdir et al. 2024), which was initially used in the first version of Chatbot Arena, BT provides a more robust and statistically grounded basis for ranking. BT produces well-calibrated estimates while naturally accommodating ties and missing comparisons, and providing confidence intervals for the rankings as long as the underlying model conditions are met.

**ZH** 相反，Chatbot Arena 依据 Arena 分数对模型排名，这是 Bradley-Terry（BT）模型（Bradley & Terry 1952）的一个归一化版本——BT 是一种基于成对比较估计技能水平的概率框架。BT 被广泛用于估计不同领域的技能水平，如在线游戏（例如星际争霸 II）（Leitner et al. 2010; Liquipedia 2019; Wise 2021，等）与体育排名（Glickman 1999; Hunter 2004b）。相比 Elo（Elo 1978; Boubdir et al. 2024）等替代体系——Chatbot Arena 最初版本使用的就是 Elo——BT 为排名提供了更稳健、统计上更有依据的基础。只要底层模型条件得到满足，BT 就能给出良好校准的估计，同时自然地容纳平局与缺失的比较，并为排名提供置信区间。

**EN** While BT is considered to be a principled ranking system, its effectiveness depends on several key assumptions. Background on these assumptions will provide important context for our discussions in Section 5.1 and Section 5.2, where we examine how violations of BT’s assumptions affect the reliability of Arena rankings. The BT model assumes that pairwise comparisons are drawn from an unbiased sampling process, so that each model’s skill parameter is estimated independently and based on representative outcomes. It also does not require all players to play each other because of transitivity of rankings—if Model A is judged to beat Model B and Model B in turn beats Model C, then Model A is estimated to outperform Model C (even if they never actually play). Finally, it assumes that the comparison network is fully interconnected—that is, every model must be linked directly or indirectly through pairwise matchups. Deviations from these assumptions, such as biased comparisons or a fragmented graph, can compromise the reliability and consistency of the strength estimates. For further details, we include the mathematical formulation of the BT model in Appendix B.

**ZH** 虽然 BT 被视为一个有原则的排名体系，其有效性取决于若干关键假设。这些假设的背景将为我们第 5.1 节与第 5.2 节的讨论提供重要语境——在那里我们考察违反 BT 假设会如何影响 Arena 排名的可靠性。BT 模型假定成对比较来自无偏的采样过程，从而每个模型的技能参数被独立估计、且基于有代表性的结果。它也不要求所有选手彼此对战，因为排名具有传递性——若判定模型 A 胜过模型 B，而模型 B 又胜过模型 C，则估计模型 A 优于模型 C（即便它们从未真正对战）。最后，它假定比较网络是完全连通的——即每个模型都必须通过成对对局直接或间接地相连。偏离这些假设（例如有偏的比较或碎片化的图）会损害强度估计的可靠性与一致性。更多细节见附录 B 中 BT 模型的数学表述。

**EN** 3 Results: Impact of Private Testing and Selective Retraction on Arena Scores

**ZH** 3 结果：私有测试与选择性撤回对 Arena 分数的影响

<!-- [原子块 · svg]  -->

**EN** 3.1 Preferred Providers Frequently Use Private Testing

**ZH** 3.1 受偏爱的提供方频繁使用私有测试

**EN** Although not an officially stated policy6, our audit of Chatbot Arena data using random-sample- battles revealed that providers are permitted to test multiple private model variants simultaneously, without being required to publicly release or de-anonymize these submissions. In Figure 6, we plot the number of private variants we tracked as belonging to each provider from January to March 2025. Meta and Google had the most active private models during this period, with 27 and 10 models, respectively. Notably, Meta’s private testing occurred just before the release of the Llama 4 models (Meta 2025). For Google, the majority of private testing was driven by Gemini models (proprietary), with only one observed test involving Gemma 3 (open-weights) (Google 2025).

**ZH** 尽管并非官方明文政策6，我们使用 random-sample-battles 对 Chatbot Arena 数据的审计显示，提供方被允许同时测试多个私有模型变体，且不必公开发布或去匿名化这些提交。在图 6 中，我们绘制了 2025 年 1 月至 3 月追踪到的、属于各提供方的私有变体数量。在此期间，Meta 与 Google 的活跃私有模型最多，分别为 27 个与 10 个。值得注意的是，Meta 的私有测试恰好发生在 Llama 4 模型发布之前（Meta 2025）。对 Google 而言，大部分私有测试由 Gemini 模型（专有）驱动，仅观察到一次涉及 Gemma 3（开放权重）的测试（Google 2025）。

**EN** We note this is likely a very conservative estimate as it only tracks the private variants on the main Chatbot Arena, and does not take into account private variants on specialized leaderboards run by Arena such as for vision 1111 11 https://blog.lmarena.ai/blog/2024/multimodal/ or code.1212 12 https://blog.lmarena.ai/blog/2024/copilot-arena/1313 13 https://blog.lmarena.ai/blog/2025/repochat-arena/ Indeed, if we also consider the number of private models tested by Meta on the vision leaderboard, we observe an additional 16 variants, bringing the total to 43. In contrast, smaller startups, such as Reka, were found to have one active private variant live in the arena. We note that during the same period, Cohere submitted 4 private variants—these ablations were part of experiments measuring the lift that could be expected from private testing that we detail in the experiments in Section 3.2 and Section 4.1. Before this, Cohere had never submitted private variants for testing in the Chatbot Arena.

**ZH** 我们指出，这很可能是一个非常保守的估计，因为它只追踪了 Chatbot Arena 主榜上的私有变体，没有计入 Arena 运营的专用排行榜（如视觉 1111 11 https://blog.lmarena.ai/blog/2024/multimodal/ 或代码 1212 12 https://blog.lmarena.ai/blog/2024/copilot-arena/ 1313 13 https://blog.lmarena.ai/blog/2025/repochat-arena/）上的私有变体。事实上，若把 Meta 在视觉排行榜上测试的私有模型数也计入，我们观察到额外 16 个变体，总数达到 43 个。相比之下，Reka 等较小的初创公司被发现只有一个活跃的私有变体在 Arena 中运行。我们注意到，同期 Cohere 提交了 4 个私有变体——这些消融实验是为衡量私有测试可带来的增益而设计的，详见第 3.2 节与第 4.1 节的实验。在此之前，Cohere 从未向 Chatbot Arena 提交过私有变体。

<!-- [原子块 · object]  -->

**EN** Figure 6: Number of privately-tested models per provider based on random-sample- battles (January–March 2025). Meta, Google, and Amazon account for the highest number of private submissions, with Meta alone testing 27 anonymous models in March alone. We note that during the same period, Cohere submitted private variants—these ablations were part of experiments submitted by the authors of this work to measure the lift that could be expected from private testing that we detail in the experiments in Section 3.2 and Section 4.1.

**ZH** 图 6：基于 random-sample-battles（2025 年 1—3 月）的各提供方私有测试模型数量。Meta、Google 与 Amazon 的私有提交数量最多，仅 Meta 在 3 月一个月内就测试了 27 个匿名模型。我们注意到，同期 Cohere 也提交了私有变体——这些消融实验由本文作者提交，用于衡量私有测试可带来的增益，详见第 3.2 节与第 4.1 节的实验。

**EN** We only scraped data from January to March 2025, yet we anecdotally observed behavior that suggests submitting multiple variants was a long-standing practice amongst a subset of providers. Over the last year, we have observed that major LLM providers such as Google, xAI, and OpenAI are often announced as having the top-performing variant within just a few days of one another. For example, OpenAI’s GPT-4.5 and xAI’s Grok-3 reached the top of the Chatbot Arena leaderboard within the same day (March 4, 2025)1414 14 https://x.com/lmarena_ai/status/18966754009165663571515 15 https://x.com/lmarena_ai/status/1896590146465579105. Gemini (Exp 1114) from Google DeepMind reached the top of the leaderboard on November 14, 20241616 16 https://x.com/lmarena_ai/status/1857110672565494098 and shortly after, ChatGPT-4o (20241120) from OpenAI claimed the top position on November 20, 20241717 17 https://x.com/lmarena_ai/status/1859307979184689269. Just one day later, on November 21, 2024, Gemini (Exp 1121) regained the top spot1818 18 https://x.com/lmarena_ai/status/1859673146837827623. Given the time typically required to develop, refine, and test a foundation model, it is unlikely for the same provider to top the leaderboard twice in a single week unless they were testing multiple variants simultaneously. In Section 3.2, we demonstrate through simulated experiments that rapid leaderboard turnover can plausibly emerge from providers optimizing for the highest possible score by testing multiple model variants in parallel.

**ZH** 我们只抓取了 2025 年 1 月至 3 月的数据，但我们零星观察到的行为表明，提交多个变体在部分提供方中是一项长期做法。在过去一年里，我们观察到 Google、xAI 与 OpenAI 等主要 LLM 提供方常常在相隔仅数日内被宣布拥有表现最好的变体。例如，OpenAI 的 GPT-4.5 与 xAI 的 Grok-3 在同一天（2025 年 3 月 4 日）登顶 Chatbot Arena 排行榜1414 14 https://x.com/lmarena_ai/status/18966754009165663571515 15 https://x.com/lmarena_ai/status/1896590146465579105。Google DeepMind 的 Gemini（Exp 1114）于 2024 年 11 月 14 日登顶1616 16 https://x.com/lmarena_ai/status/1857110672565494098，此后不久，OpenAI 的 ChatGPT-4o（20241120）于 2024 年 11 月 20 日占据榜首1717 17 https://x.com/lmarena_ai/status/1859307979184689269。仅一天之后，即 2024 年 11 月 21 日，Gemini（Exp 1121）又重回榜首1818 18 https://x.com/lmarena_ai/status/1859673146837827623。考虑到开发、打磨与测试一个基础模型通常需要的时间，同一提供方在一周内两次登顶排行榜是不太可能的，除非他们在同时测试多个变体。在第 3.2 节，我们通过模拟实验证明，排行榜的快速更替很可能源自提供方通过并行测试多个模型变体来追求最高可能分数。

**EN** Notably, we found that no private models were tested by academic labs during the observed period. This leads us to believe only certain providers were made aware they could submit multiple private variants, as we observe clear differences in the number and frequency of private testing among providers.

**ZH** 值得注意的是，我们发现在观察期内没有任何学术实验室测试过私有模型。这使我们相信，只有某些提供方被告知可以提交多个私有变体，因为我们观察到各提供方在私有测试的数量与频率上存在明显差异。

**EN** 3.2 Simulated Experiments on Private Testing and Retraction

**ZH** 3.2 关于私有测试与撤回的模拟实验

**EN** Private testing coupled with the option to retract enables a best-of-N strategy, where an organization submits multiple model variants to Chatbot Arena, privately evaluates them, and retains only the top-performing variant to be publicly published on the leaderboard. In this section, we show that best-of-N submissions violate the BT unbiased sampling assumption. This systematically inflates model rankings and distorts the leaderboard ranking.

**ZH** 私有测试加上可撤回的选项，使一种 best-of-N 策略成为可能：机构向 Chatbot Arena 提交多个模型变体，私下评测它们，只保留表现最好的那个变体公开发布到排行榜上。在本节中，我们表明 best-of-N 提交违反了 BT 的无偏采样假设。这会系统性地抬高模型排名，并扭曲排行榜排序。

<!-- [原子块 · object]  -->

**EN** Figure 7: Impact of the number of private variants tested on the best Expected Arena Score. We simulate a family of model variants with a latent average Arena Score of 1200. As we progressively increase the number of private variants tested—and subsequently discover their corresponding Arena Scores—the probability of selecting models from the higher end of the performance distribution also rises. This enables the provider to effectively identify the model with the highest score.

**ZH** 图 7：被测试的私有变体数量对最佳期望 Arena 分数的影响。我们模拟了一个潜在平均 Arena 分数为 1200 的模型变体族。随着我们逐步增加被测试的私有变体数量——并随后发现它们相应的 Arena 分数——选中处于性能分布高端的模型的概率也随之上升。这使提供方能有效识别出分数最高的模型。

**EN** Unbiased Sampling Assumption. To study the selection bias scenario, assume a provider submits ⟦SLOT_2⟧ variants of a model, each variant ⟦SLOT_3⟧ having a true underlying skill parameter ⟦SLOT_4⟧, sampled from a distribution centered at some base skill level ⟦SLOT_5⟧. The probability of observing an exceptionally high-performing variant increases with the number of submissions ⟦SLOT_6⟧. Thus, the observed skill of the submitted model is: ⟦SLOT_7⟧.

**ZH** 无偏采样假设。为研究这一选择偏差场景，假设某提供方提交 ⟦SLOT_2⟧ 个模型变体，每个变体 ⟦SLOT_3⟧ 都有一个真实的潜在技能参数 ⟦SLOT_4⟧，采样自以某个基础技能水平 ⟦SLOT_5⟧ 为中心的分布。观察到表现异常出色的变体的概率随提交数量 ⟦SLOT_6⟧ 的增加而上升。因此，所提交模型被观测到的技能为：⟦SLOT_7⟧。

**EN** Since each ⟦SLOT_8⟧ is subject to statistical fluctuation due to finite match sampling, selecting the best variant based on observed performance introduces an upward bias. Specifically, the expected value of the best-performing variant is strictly greater than that of a regular submission:

**ZH** 由于每个 ⟦SLOT_8⟧ 都会因有限对局采样而受到统计波动的影响，依据观测表现挑选最佳变体会引入向上的偏差。具体地，表现最佳变体的期望值严格大于一次常规提交的期望值：

<!-- [原子块 · table] 𝔼 ⁡ [ β ^ Best ] > 𝔼 ⁡ [ β ^ k ] ​ , ∀ k ∈ { 1 , 2 , … , N } . \mathbb{E}[\hat{\beta}_{\text{Best}}]>\mathbb{E}[\hat{\beta}_{k}]\text{,}\qquad\forall k\in\{1,2,\dots,N\}. (1) -->

**EN** where the draws are non-degenerate (⟦SLOT_9⟧) and ⟦SLOT_10⟧ (See Appendix C for further details). This violates the BT model’s assumption of unbiased sampling and alters the likelihood landscape. The reported rating no longer reflects a single, unbiased estimate of skill, but an extreme value from multiple independent estimations. As a result, the BT estimator systematically inflates the ratings of models submitted under the best-of-N strategy, distorting leaderboard rankings.

**ZH** 其中抽样是非退化的（⟦SLOT_9⟧）且 ⟦SLOT_10⟧（详见附录 C）。这违反了 BT 模型的无偏采样假设，并改变了似然曲面。所报告的评分不再是对技能的单一无偏估计，而是多次独立估计中的极值。结果，BT 估计器会系统性抬高采用 best-of-N 策略提交的模型的评分，扭曲排行榜排序。

<!-- [原子块 · img]  -->

**EN** Figure 8: Simulated impact of best-of-N submission strategies on Arena leaderboard rankings. Model family A has a lower average Arena Score than Model family B, yet by submitting multiple private variants and selecting the best-performing one, it can surpass the sole public submission from Model family B. This simulation shows how providers can gain leaderboard advantage by evaluating several variants privately and publishing only the top-scoring one.

**ZH** 图 8：best-of-N 提交策略对 Arena 排行榜排名的模拟影响。模型族 A 的平均 Arena 分数低于模型族 B，但通过提交多个私有变体并挑选表现最好的那个，它可以超过模型族 B 的单一公开提交。该模拟展示了提供方如何通过私下评测若干变体、只发布得分最高的那个来获取排行榜优势。

**EN** Role of the number of private variants. In the Chatbot Arena, we observe that while only a handful of providers know about private testing, there is also an asymmetry in the number of private models tested. At an extreme, Meta tested 27 private variants in the lead up to Llama 4 launch. To investigate how the number of private tests affects model selection outcomes, we simulated the expected lift in Arena Score as the number of private variants increased from 0 to 50. This involved generating sample battles and estimating Arena Scores for the private variants using the Bradley-Terry model. We also employed bootstrapping to estimate the confidence intervals for the corresponding Arena Scores. Figure 7 presents the results, plotting the number of private variants tested (x-axis) against the average of the maximum discovered Arena Scores across simulations (y-axis). As the number of privately tested models increases, the expected maximum Arena Score discovered rises accordingly. In our simulation, testing just 20 variants yields a notable increase of approximately 50 points in the maximum score identified, compared to the baseline scenario with no private testing. We provide more details about this simulation in Appendix I.

**ZH** 私有变体数量的作用。在 Chatbot Arena 上，我们观察到，虽然只有少数提供方知道私有测试，但被测试的私有模型数量也存在不对称。极端情况下，Meta 在 Llama 4 发布前测试了 27 个私有变体。为研究私有测试次数如何影响模型选择结果，我们模拟了当私有变体数量从 0 增加到 50 时期望的 Arena 分数增益。这包括生成采样对战，并用 Bradley-Terry 模型估计各私有变体的 Arena 分数。我们还采用自助法来估计相应 Arena 分数的置信区间。图 7 给出了结果，横轴为被测试的私有变体数量，纵轴为各次模拟中发现的 Arena 分数最大值的平均。随着被私有测试的模型数量增加，被发现的最大 Arena 分数的期望也相应上升。在我们的模拟中，与不做任何私有测试的基线场景相比，仅测试 20 个变体就能使发现的最大分数显著增加约 50 分。关于该模拟的更多细节见附录 I。

**EN** Asymmetries in which providers have access to private testing. We observe in practice that only a few preferred providers were allowed to test many variants and handpick the best result. As we show in Figure 8, restricting private testing to a subset of providers can lead to scenarios where a weaker family of models (Family A) enabled with private testing can outperform a stronger family of models (Family B), which is restricted to a single submission. Although the performance of both model families is in a similar range, Family A’s models have a lower average Arena score across all models compared to Family B’s. In contrast to model provider B, who is unaware of the best-of-N strategy, model provider A evaluates multiple models on the Chatbot Arena distribution and selects the best-performing model. This allows provider A to evaluate multiple models on the Chatbot Arena distribution and select the best-performing model, leveraging the tail of the distribution, to achieve a higher leaderboard ranking. As a result, despite having a generally stronger model pool, Family B ranks lower than Family A on the leaderboard.

**ZH** 哪些提供方能使用私有测试的不对称。我们实践中观察到，只有少数受偏爱的提供方被允许测试许多变体并挑出最佳结果。如图 8 所示，把私有测试限制在部分提供方，可能造成这样的情形：启用了私有测试、但整体较弱的模型族（族 A），能够胜过被限制为单一提交的更强模型族（族 B）。虽然两个模型族的性能处于相近区间，但族 A 的模型在所有模型上的平均 Arena 分数低于族 B。与不知道 best-of-N 策略的模型提供方 B 不同，模型提供方 A 在 Chatbot Arena 分布上评测多个模型并选出表现最好的那个，从而利用分布的尾部取得更高的排行榜排名。结果，尽管族 B 的模型池总体上更强，它在排行榜上的排名却低于族 A。

**EN** Having to pick from multiple final “candidate” models is a very common scenario during the development of LLMs. At the end of the development process of a new model, a model provider typically ends up with multiple variants, each excelling in different tasks due to variations in post-training strategies or hyperparameter settings. They often perform well on different tasks, while still being within similar overall performance bands. Selecting a final “official” model often involves a compromise across a broad range of evaluation sets. A strong signal—such as a clear lead on an arena-style leaderboard—can significantly influence this decision, tipping the preference toward specific variants that perform best under the given evaluation framework. Hence, with an “informed selection” strategy for model variants, a model provider can improve its ranking and reach the top of the leaderboard compared to when it makes an “unguided selection” to choose the variant that can be released on the public leaderboard.

**ZH** 在 LLM 开发过程中，必须从多个最终「候选」模型中做挑选，这是非常常见的情形。在一个新模型开发流程的末尾，模型提供方通常会得到多个变体，由于后训练策略或超参数设置的不同，它们各在不同任务上表现突出。它们往往在不同任务上各有擅长，而整体性能仍处于相近的区间。挑选一个最终的「正式」模型，通常需要在广泛的评测集之间做出折中。一个强烈的信号——例如在 arena 式排行榜上的明显领先——会显著影响这一决策，使偏好倾向那些在给定评测框架下表现最好的特定变体。因此，与在公开排行榜上发布哪个变体时做「无引导的选择」相比，采用「有信息的选择」策略的模型提供方可以提升自己的排名并登上榜首。

<!-- [原子块 · object]  -->

**EN** Figure 9: Allowing retraction of scores allows providers to skew Arena scores upwards. We run a real-world experiment to measure the benefits of private testing. We show that it is possible to increase Arena scores even in the most conservative case of identical checkpoints, and further amplify the difference by strategically testing different checkpoints. Left: Identical Checkpoints. Arena Scores for Aya-Vision-8B yield different Arena scores (1069 vs. 1052). Right: Strategically Selected Checkpoints. Arena Scores for two different variants of Aya-Vision-32B, which were both considered high-performing final round candidates according to internal metrics. We observe large differences in final scores (1097 vs. 1059) for the two different model variants.

**ZH** 图 9：允许撤回分数使提供方得以把 Arena 分数向上偏移。我们开展了一项真实实验来衡量私有测试的收益。我们表明，即便在最保守的「相同检查点」情形下，也有可能提高 Arena 分数，并且通过策略性地测试不同检查点还能进一步放大这一差异。左：相同检查点。Aya-Vision-8B 的 Arena 分数出现差异（1069 vs. 1052）。右：策略性选择的检查点。Aya-Vision-32B 两个不同变体的 Arena 分数，二者按内部指标都被视为表现优秀的最终候选。我们观察到两个不同模型变体的最终分数存在较大差异（1097 vs. 1059）。

**EN** 3.3 Real-world Chatbot Arena Experiment

**ZH** 3.3 真实世界的 Chatbot Arena 实验

**EN** Our simulation previously demonstrated that when model submissions are not standardized across model providers, those who submit a larger number of private model variants gain a systematic advantage, creating an uneven playing field for ranking. Since we do not have access to the final scores of private model variants observed during our Arena scrape, we design a real-world experiment to complement and validate our simulation findings. Specifically, we model two scenarios of best-of-N testing to assess the impact of submitting multiple model variants.

**ZH** 我们此前的模拟表明，当模型提交在各提供方之间没有被标准化时，提交更多私有模型变体的一方会获得系统性优势，从而为排名制造了不公平的竞争环境。由于我们无法获得抓取 Arena 期间观察到的私有模型变体的最终分数，我们设计了一项真实实验来补充并验证模拟发现。具体地，我们建模了 best-of-N 测试的两种场景，以评估提交多个模型变体的影响。

**EN** Lower bound estimate of benefits of multiple submissions. We model the most conservative case – measuring the gain from submitting and then only releasing the best Arena score obtained by two identical checkpoints. For this purpose, we submitted two identical variants of Aya-Vision-8B to the Arena in March 2025. This scenario is a very conservative lower bound of gains, as any difference in Arena score can be attributed to the benefits of multiple submissions rather than differences in model quality. We used only two checkpoints because we wanted to limit the amount of human annotator time we diverted to this exercise. We did not disclose that these were identical checkpoints to Chatbot Arena. In Figure 9, we observe notable differences in final Arena scores between identical checkpoints: 1052 (±21/22) and 1069 (±19/23). As a result, 4 models are positioned between our two identical checkpoints. This suggests that even with identical variants, it is very feasible to obtain a biased positive advantage.

**ZH** 多次提交收益的下界估计。我们建模最保守的情形——衡量提交两个相同检查点、然后只发布其中获得的更高 Arena 分数所带来的增益。为此，我们于 2025 年 3 月向 Arena 提交了 Aya-Vision-8B 的两个相同变体。这一场景是增益的一个非常保守的下界，因为 Arena 分数的任何差异都可归因于多次提交的收益，而非模型质量的差异。我们只用了两个检查点，是因为希望限制这件事所占用的人类标注时间。我们没有向 Chatbot Arena 披露这是两个相同的检查点。在图 9 中，我们观察到相同检查点之间的最终 Arena 分数存在明显差异：1052（±21/22）与 1069（±19/23）。结果，有 4 个模型位于我们这两个相同检查点之间。这表明，即便使用相同的变体，获得正向的偏差优势也非常可行。

**EN** Realistic estimate of benefits of multiple submissions. In practice, a provider would likely optimize the differences in the variants they are testing to maximize the signal from the Arena users. To study this scenario, we compare two different variants of Aya-Vision-32B. The two checkpoints are variants of the same model, with each showing slightly better performance on different subsets of benchmarks. In Figure 9, we illustrate the extreme ends of the scores obtained by the two models (1097 (±29/25) vs. 1059 (±18/23)), with 9 models falling in between both variants on the leaderboard.

**ZH** 多次提交收益的现实估计。在实践中，提供方很可能会优化被测变体之间的差异，以最大化来自 Arena 用户的信号。为研究这一场景，我们比较了 Aya-Vision-32B 的两个不同变体。这两个检查点是同一模型的变体，各自在不同基准子集上表现略优。在图 9 中，我们展示了两个模型所得分数的极端两端（1097（±29/25）vs. 1059（±18/23）），排行榜上有 9 个模型落在这两个变体之间。

**EN** 4 Results: Impact of Data Access Asymmetries on Arena Scores

**ZH** 4 结果：数据访问不对称对 Arena 分数的影响

<!-- [原子块 · svg]  -->

**EN** 4.1 Disparity in access to Chatbot Arena Data

**ZH** 4.1 Chatbot Arena 数据访问上的差距

**EN** Prompts from a large and diverse user base, such as those from Chatbot Arena users, serve as a valuable signal for modeling user interests and preferences. This data is often accessible to model providers through API calls originating from Chatbot Arena battles. Multiple factors impact the amount of the data obtained by a given provider, some of which are determined by Chatbot Arena versus others which are within the control of the providers:

**ZH** 来自庞大而多样用户群（如 Chatbot Arena 用户）的提示，是建模用户兴趣与偏好的宝贵信号。这些数据通常通过源自 Chatbot Arena 对战的 API 调用为模型提供方所获取。有多个因素会影响某一提供方获得的数据量，其中一些由 Chatbot Arena 决定，另一些则在提供方自身的掌控之内：

**EN** 1. Number of private variants being tested on the arena: As shown in Figure 6, some providers deploy far more private variants, which can significantly increase the volume of data collected. We note that even with our experiment of launching multiple model variants, we increased the amount of prompts collected from 5.9% with 1 variant to 19.4% with 3 variants. Based on findings from Figure 6, the number of variants submitted is not uniform across all providers, and some providers may increase variants to further amplify the volume of data collected. This is of particular concern given Chatbot Arena is a community-driven leaderboard, however, the main beneficiaries of this free human feedback appear to be commercial entities who are frequently preferred for private testing.

**ZH** 1. 在 Arena 上被测试的私有变体数量：如图 6 所示，部分提供方部署的私有变体要多得多，这会显著增加收集到的数据量。我们注意到，即便在我们投放多个模型变体的实验中，收集到的提示占比也从 1 个变体时的 5.9% 提高到 3 个变体时的 19.4%。根据图 6 的发现，各提供方提交的变体数量并不统一，某些提供方可能会增加变体数量以进一步放大收集到的数据量。这一点尤其值得关注，因为 Chatbot Arena 是一个社区驱动的排行榜，然而这份免费人类反馈的主要受益者却似乎是那些在私有测试中常被优待的商业实体。

**EN** 2. Sampling rate applied to provider models: We define model sampling rate as the percentage of daily battles a model participates in. The maximum sampling rate for a provider is the highest rate achieved by any of its models on any given day. We determine the maximum sampling rate of providers based on scraped-random-sample, which is limited to the specific period during which we collected this data (January 2025 to March 2025). As shown in Figure 5, sampling rates vary significantly across providers. These rates are determined by Chatbot Arena, but are often entirely inconsistent with the stated policy and prior proposals by the organizers to automatically set sampling based upon which models have not converged in score (Chiang et al. 2024). At the extreme, Google and OpenAI reach a maximum daily sampling rate of 34%, while Reka registers the lowest at 3.3%. Other providers with relatively high sampling rates include xAI (22.0%) and Meta (17.9%), highlighting substantial variation across the board. We provide additional details about how sampling rates were determined for each provider in Section E.5.

**ZH** 2. 施加于提供方模型的采样率：我们把模型采样率定义为一个模型参与的对战占每日对战的百分比。某提供方的最大采样率是其任一模型在任一天达到的最高比率。我们依据 scraped-random-sample 确定各提供方的最大采样率，该数据源限于我们收集数据的特定时段（2025 年 1 月至 2025 年 3 月）。如图 5 所示，各提供方的采样率差异显著。这些比率由 Chatbot Arena 决定，但常常与明文政策以及组织者此前关于「依据哪些模型分数尚未收敛来自动设定采样」的提议（Chiang et al. 2024）完全不一致。极端情况下，Google 与 OpenAI 的日最高采样率达到 34%，而 Reka 最低，仅为 3.3%。采样率相对较高的其他提供方包括 xAI（22.0%）与 Meta（17.9%），体现出整体上的巨大差异。关于如何确定各提供方采样率的更多细节见第 E.5 节。

**EN** 3. Number of models publicly hosted on the arena: A model only receives traffic if it is live on the arena. However, Chatbot Arena frequently deprecates models. There are several reasons to deprecate models in a benchmark. Chatbot Arena may be forced to deprecate a model when a provider no longer supports it via its API. They also have policies for deprecating models under certain conditions6: Models may be retired after 3000 votes “if there are two more recent models in the same series and/or if there are more than 3 providers that offer models cheaper or same price and strictly better (according to overall Arena score)”. We note that the logic of this policy is difficult to audit in practice because many models are hosted for free on the Chatbot Arena, and the use of the “or” condition means it is not clear what criteria (price or quality) applies to decisions. We observe that many models are also silently deprecated, which means their sampling rate is reduced to nearly 0% without notification, even though some of them do not meet the stated criteria of the deprecation policy. We identify 205 models that have been silently deprecated, a number that substantially exceeds the 47 models officially marked as deprecated by Chatbot Arena. For a more detailed analysis, see Appendix K.

**ZH** 3. 在 Arena 上公开托管的模型数量：模型只有在 Arena 上运行才会获得流量。然而，Chatbot Arena 频繁下架模型。在一个基准中下架模型有若干理由。当提供方不再通过 API 支持某个模型时，Chatbot Arena 可能被迫下架它。他们也有在特定条件下下架模型的政策6：模型在获得 3000 票后可能被退役，「如果同系列中有两个更新的模型，和/或如果有超过 3 家提供方提供更便宜或同价且（按整体 Arena 分数）明显更好的模型」。我们注意到，这一政策的逻辑在实践中难以审计，因为许多模型在 Chatbot Arena 上是免费托管的，而且「或」条件的使用使得不清楚究竟适用哪个标准（价格还是质量）。我们还观察到许多模型被静默下架，即其采样率被降至接近 0% 且不发出通知，尽管其中一些并不符合下架政策的明文标准。我们识别出 205 个被静默下架的模型，这一数字大大超过了 Chatbot Arena 官方标记下架的 47 个模型。更详细的分析见附录 K。

**EN** 4. API Support for Models on the Arena: Developers who deploy a model and enable Chatbot Arena testing via an API have a default advantage. This allows providers to collect 100% of the test prompts submitted on the Arena. In contrast, providers whose models are hosted by a third party are often limited to publicly accessible data or must request access to only 20% of the data (including prompts and human preferences) involving their models from Chatbot Arena, as per their policy6.

**ZH** 4. 对 Arena 上模型的 API 支持：部署模型并通过 API 启用 Chatbot Arena 测试的开发者拥有默认优势。这使提供方能够收集 Arena 上提交的 100% 的测试提示。相比之下，模型由第三方托管的提供方往往只能获取公开可得的数据，或必须按其政策6 向 Chatbot Arena 申请涉及其模型的数据（包括提示与人类偏好）中的 20%。

**EN** We observe that the collective impact of these factors appears to be advantageous to a small handful of providers and is often inconsistent with the stated policy. For example, in Figure 4, we show that the combined share of OpenAI, Google, Meta, and Anthropic alone is 62.8% of the arena data, which is 68 times more than the share of top academic and non-profit labs including Allen AI, Stanford, Princeton, and UC Berkeley. These findings add to prior works that consistently show better corporate access to AI training data across the ecosystem (Longpre et al. 2024c; Longpre et al. 2024b).

**ZH** 我们观察到，这些因素的综合影响似乎对少数提供方有利，且常常与明文政策不一致。例如，在图 4 中，我们显示仅 OpenAI、Google、Meta 与 Anthropic 合计就占 Arena 数据的 62.8%，是 Allen AI、斯坦福、普林斯顿与 UC Berkeley 等顶尖学术与非营利实验室份额的 68 倍。这些发现补充了此前一致表明企业在整个生态中获得更好 AI 训练数据访问权的研究（Longpre et al. 2024c; Longpre et al. 2024b）。

**EN** We note that the prompt samples available to each provider may not be mutually exclusive, as each battle on the Arena involves two models (from the same or different model providers), allowing the same prompt to be sent to two different providers. Details about statistics in Figure 4 are available in Appendix G.

**ZH** 我们注意到，各提供方可得的提示样本可能并不互斥，因为 Arena 上的每场对战都涉及两个模型（来自相同或不同提供方），同一提示可能被发送给两个不同的提供方。图 4 中统计数据的细节见附录 G。

<!-- [原子块 · object]  -->

<!-- [原子块 · object]  -->

**EN** Figure 10: Use of Chatbot Arena dataset significantly improves win-rates on ArenaHard. Increasing the amount of arena data in a supervised fine-tuning mixture (0% ⟦SLOT_11⟧30% ⟦SLOT_12⟧ 70%) significantly improves win-rates of the resulting model against both the model variant where no Chatbot Arena data is used and also Llama-3.1-8B. The win-rates are measured on ArenaHard (Li et al. 2024c), which has a high correlation of 98.6% to Chatbot Arena.

**ZH** 图 10：使用 Chatbot Arena 数据集显著提升了 ArenaHard 上的胜率。在监督微调混合数据中提高 arena 数据的比例（0% ⟦SLOT_11⟧30% ⟦SLOT_12⟧ 70%），显著提升了所得模型相对于「未使用 Chatbot Arena 数据的模型变体」以及 Llama-3.1-8B 的胜率。胜率在 ArenaHard（Li et al. 2024c）上测量，该基准与 Chatbot Arena 的相关性高达 98.6%。

**EN** 4.2 Risk of Potential Overfitting

**ZH** 4.2 潜在过拟合风险

**EN** One of the questions we want to answer is “What are the implications of data asymmetries? Does having access to more data enable overfitting to the Arena?”. Overfitting refers to a phenomenon in which a model learns not only the generalizable patterns in its training data but also the specific noise or characteristics, resulting in strong performance on familiar or seen examples but degraded performance on unseen and out-of-distribution inputs.

**ZH** 我们想要回答的问题之一是「数据不对称意味着什么？获得更多数据是否会导致对 Arena 过拟合？」。过拟合指的是这样一种现象：模型不仅学到了训练数据中的可泛化模式，还学到了特定的噪声或特性，从而在熟悉或见过的样本上表现很好，但在未见与分布外输入上性能下降。

**EN** Overfitting is a particularly salient challenge in static evaluation settings, where fixed test sets are vulnerable to overfitting through repeated exposure, data contamination, or intentional tuning (Deng et al. 2024; Golchin & Surdeanu 2024; Roberts et al. 2023; Dong et al. 2024; Singh et al. 2024a). In contrast, Chatbot Arena has been widely adopted in part because it allows human users to ask any questions they want, which creates a non-static test set (Don-Yehiya et al. 2024). This means that, at least in principle, the test set is potentially harder to overfit to. However, this assumes that the distribution is constantly changing.

**ZH** 过拟合在静态评测设定中是一个尤为突出的问题，因为固定的测试集容易因反复暴露、数据污染或刻意调参而被过拟合（Deng et al. 2024; Golchin & Surdeanu 2024; Roberts et al. 2023; Dong et al. 2024; Singh et al. 2024a）。相比之下，Chatbot Arena 之所以被广泛采用，部分原因是它允许人类用户提出任何问题，从而形成一个非静态的测试集（Don-Yehiya et al. 2024）。这意味着，至少在原则上，该测试集可能更难被过拟合。然而，这假定分布是持续变化的。

**EN** To understand whether this is the case with data from Chatbot Arena, we do an exhaustive analysis and observe that the true picture on Chatbot Arena is more complex. We observe two phenomena: (1) The characteristics of prompts do shift notably over time, and (2) a non-trivial portion of prompts in one month are either exact duplicates or near-duplicates of prompts from previous months. This means that some test prompts are very similar to (or even the same as) prompts seen previously. Together, these suggest that having access to a large sample of last month’s data will enable a developer to perform significantly better on next month’s test set.

**ZH** 为弄清 Chatbot Arena 的数据是否如此，我们做了详尽的分析，观察到 Chatbot Arena 的真实图景更为复杂。我们观察到两种现象：（1）提示的特征确实随时间发生显著变化；（2）某一个月中的提示有相当一部分是此前月份提示的完全重复或近似重复。这意味着某些测试提示与此前见过的提示非常相似（甚至完全相同）。两者共同表明，获得上个月数据的较大样本，将使开发者在下个月的测试集上表现得显著更好。

<!-- [原子块 · object]  -->

**EN** Figure 11: Language distribution of prompts submitted to Chatbot Arena from April 2023 to January 2025. Based on the historical-battles dataset, this figure tracks the monthly share of prompt languages. Only languages with dedicated Chatbot Arena leaderboards are shown individually; the rest are grouped under “Other”. A clear shift is observed: English prompt share dropped from over 80% to nearly 50%, while usage of Chinese, Russian, and Korean prompts increased significantly.

**ZH** 图 11：2023 年 4 月至 2025 年 1 月提交到 Chatbot Arena 的提示的语言分布。基于 historical-battles 数据集，本图追踪各月提示语言的占比。仅单独列出在 Chatbot Arena 上有专门排行榜的语言，其余归入「其他」。可以观察到明显的变化：英语提示占比从 80% 以上降至接近 50%，而中文、俄文与韩文提示的使用显著增加。

**EN** 1) Long-term distribution shifts. Prior work clearly demonstrates how temporal distribution shifts affect performance (Luu et al. 2021; Longpre et al. 2024d). On Chatbot Arena, notable shifts have been observed in the distribution of prompts evaluated over longer periods, with a consistent increase in the proportion of prompts from more complex categories, such as mathematics, coding, and multi-turn conversations1919 19 https://blog.lmarena.ai/blog/2024/arena-category/. We also perform our own analysis of the change in language distribution in the Arena based on the “language“ tag available as part of historical-battles dataset. For example, in Figure 11, we observe that the proportion of languages outside of English has varied over time. For instance, the share of Russian prompts increased from 1% in April 2023 to 8.8% in April 2024, and further to 15.7% by December 2024. Chinese prompts more than doubled from 5-7% in 2023 to 16.4% in March 2024, coinciding with the introduction of the Chinese leaderboard on Chatbot Arena, before dropping back to 6.2% in January 2025. Overall, the number of multilingual prompts on the Arena has grown by 20% over 1.5 years, from 23.9% in April 2023 to 43.5% in January 2025. This indicates increased language diversity in submitted prompts.

**ZH** 1）长期分布漂移。已有研究清楚地展示了时间分布漂移如何影响性能（Luu et al. 2021; Longpre et al. 2024d）。在 Chatbot Arena 上，较长周期内的被评测提示分布已出现显著漂移，数学、编码与多轮对话等更复杂类别的提示占比持续上升1919 19 https://blog.lmarena.ai/blog/2024/arena-category/。我们也基于 historical-battles 数据集中的「language」标签，自行分析了 Arena 上语言分布的变化。例如，在图 11 中，我们观察到非英语语言的占比随时间变化。具体而言，俄语提示的占比从 2023 年 4 月的 1% 上升到 2024 年 4 月的 8.8%，并进一步升至 2024 年 12 月的 15.7%。中文提示从 2023 年的 5-7% 翻倍以上至 2024 年 3 月的 16.4%——这与 Chatbot Arena 推出中文排行榜的时间吻合——随后在 2025 年 1 月回落到 6.2%。总体而言，Arena 上多语言提示的数量在一年半内增长了 20%，从 2023 年 4 月的 23.9% 增至 2025 年 1 月的 43.5%。这表明所提交提示的语言多样性在提升。

<!-- [原子块 · object]  -->

**EN** Figure 12: Monthly prompt duplication rates. Prompts are from November 2024 to April 2025, excluding February 2025 due to insufficient data. Duplication is measured using two similarity metrics: Exact Match and High Similarity (cosine similarity of text embedding ⟦SLOT_13⟧). For simplicity, this analysis is limited to single-turn conversations. The chart presents the percentage of battles in which duplicate or near-duplicate prompts were detected each month.

**ZH** 图 12：各月的提示重复率。提示取自 2024 年 11 月至 2025 年 4 月，因数据不足剔除了 2025 年 2 月。重复率用两种相似度指标度量：精确匹配与高相似度（文本嵌入的余弦相似度 ⟦SLOT_13⟧）。为简洁起见，该分析限于单轮对话。图中给出每月检出重复或近似重复提示的对战占比。

**EN** 2) Prompt redundancy and duplication. In parallel, we observe high levels of prompt duplication. We analyze a proportion of raw API calls we receive from Chatbot Arena between November 2024 and April 2025 (197,217 single-turn conversations). We switch to this source given that the proprietary data Chatbot Arena releases are already de-duplicated, and so won’t capture the extent of similar or overlapping queries. Between November 2024 and April 2025, de-duplication resulted in an average prompt loss of 20.14%, peaking at 26.5% in March 2025 (Figure 12). While prompt distribution changes over time, prompts in one month often serve as a proxy for the next. For instance, 7.3% of prompts from December 2024 appear again in the exact form in January 2025. If we relax the condition and consider high semantic similarity of prompt embeddings (using the embed-multilingual-v3.0 model2020 20 https://huggingface.co/Cohere/Cohere-embed-multilingual-v3.0), the same cross-month duplication rate increases to 9%. Detailed cross-month duplication statistics can be found in Appendix H. Both trends above suggest that 1) sustained access to up-to-date prompt data and 2) the volume of sampled prompts in a given month offer a significant competitive advantage in predicting performance in subsequent months.

**ZH** 2）提示冗余与重复。与此同时，我们观察到高度的提示重复。我们分析了 2024 年 11 月至 2025 年 4 月间从 Chatbot Arena 收到的一部分原始 API 调用（197,217 条单轮对话）。我们改用这一数据源，是因为 Chatbot Arena 发布的专有数据已经过去重，因而无法体现相似或重叠查询的程度。在 2024 年 11 月至 2025 年 4 月间，去重平均导致 20.14% 的提示损失，在 2025 年 3 月达到 26.5% 的峰值（图 12）。虽然提示分布随时间变化，但某一月的提示常常可作为下一月的代理。例如，2024 年 12 月有 7.3% 的提示在 2025 年 1 月以完全相同的形式再次出现。若放宽条件、考虑提示嵌入的高语义相似度（使用 embed-multilingual-v3.0 模型2020 20 https://huggingface.co/Cohere/Cohere-embed-multilingual-v3.0），同样的跨月重复率上升到 9%。详细的跨月重复统计见附录 H。上述两种趋势共同表明：1）持续获取最新提示数据；2）某一月内采样提示的数量，都对预测后续月份的性能具有显著的竞争优势。

**EN** Uniqueness of Arena Data. One reason providers may be motivated to explicitly optimize for Chatbot Arena distribution is if it differs substantially from other evaluation settings that providers may care about. There is sufficient signal to suggest this is the case. There is a context length limit of 12000 characters on Chatbot Arena prompts, which excludes certain types of longer or more complex inputs from being evaluated2121 21 https://github.com/lm-sys/FastChat/blob/main/fastchat/constants.py, and can result in a selection bias of what is asked. The user base of the Arena leans towards developers, which could result in the over-indexing of puzzles, math problems, and questions such as How many r’s are there in strawberry?.2222 22 https://techcrunch.com/2024/09/05/the-ai-industry-is-obsessed-with-chatbot-arena-but-it-might-not-be-the-best-benchmark/ For example, in a released dataset from Arena (Zheng et al. 2024) with 33k samples, no questions are referencing Chaucer while dozens of questions are about Star Trek, highlighting the uneven distribution of topics in this test set2323 23 https://www.quantable.com/analytics/elos-and-benchmarking-llms/. For a global technology provider, real-world commercial applications may differ significantly from this distribution.

**ZH** Arena 数据的独特性。提供方可能有动力专门针对 Chatbot Arena 分布做优化的一个原因是，该分布可能与提供方关心的其他评测设定有实质差异。有充分信号表明情况确实如此。Chatbot Arena 的提示有 12000 字符的上下文长度限制2121 21 https://github.com/lm-sys/FastChat/blob/main/fastchat/constants.py，这把某些更长或更复杂的输入排除在评测之外，并可能造成「什么被提问」的选择偏差。Arena 的用户群偏向开发者，这可能导致谜题、数学问题以及诸如「strawberry 里有几个 r？」之类的问题被过度代表2222 22 https://techcrunch.com/2024/09/05/the-ai-industry-is-obsessed-with-chatbot-arena-but-it-might-not-be-the-best-benchmark/。例如，在 Arena 发布的一个含 33k 样本的数据集（Zheng et al. 2024）中，没有任何问题提及乔叟，却有几十个问题关于《星际迷航》，凸显了这一测试集中主题分布的不均衡2323 23 https://www.quantable.com/analytics/elos-and-benchmarking-llms/。对一家全球化技术提供方而言，真实世界的商业应用可能与这一分布有显著不同。

**EN** Experimental Setup: To estimate the potential for overfitting to Chatbot Arena using data from a similar distribution, we fine-tuned a language model with identical training setups that only differ in the composition of arena data used in the mixture. We construct our training dataset by sampling at different rations from two different data pools: 1) arena-mix, which consists of samples from Arena battles, and 2) other-sft-mix, a proprietary dataset which includes a variety of supervised fine-tuning datasets focusing on instruction following, multilingual tasks, math, and code. We fine-tuned a 7B base model that is used for the Cohere Command family (Cohere et al. 2025) in these experiments. We refer to the three different training mixes as 0_arena, 30_arena, 70_arena which have 0, 30%, 70% of the training dataset sampled from the arena-mix respectively. For all variants, the remainder percentage is sampled from other-sft-mix. All three models are fine-tuned for 1.3K steps using a batch size of 128. We note that our goal here is not to produce a state-of-the-art model but rather to estimate a lower bound for the performance gains that could be expected from asymmetries in access to Arena data. Hence, we do not optimize with ablations the correct weighting or data or conduct any hyperparameter sweeps.

**ZH** 实验设置：为估计使用相近分布的数据对 Chatbot Arena 过拟合的可能性，我们用完全相同的训练设置微调了一个语言模型，只是混合数据中 arena 数据的构成不同。我们通过从两个不同的数据池以不同比例采样来构建训练数据集：1）arena-mix，由 Arena 对战样本组成；2）other-sft-mix，一个专有数据集，包含聚焦指令跟随、多语言任务、数学与代码的多种监督微调数据集。我们在这些实验中微调了一个用于 Cohere Command 系列（Cohere et al. 2025）的 7B 基座模型。我们把三种不同的训练混合称为 0_arena、30_arena、70_arena，其训练数据集分别有 0、30%、70% 采样自 arena-mix。对所有变体，剩余百分比从 other-sft-mix 中采样。三个模型都以批大小 128 微调 1.3K 步。我们指出，此处我们的目标不是产出一个最先进模型，而是为「Arena 数据访问不对称可带来的性能增益」估计一个下界。因此，我们没有通过消融实验去优化正确的权重或数据配比，也没有做任何超参数扫描。

**EN** Evaluation method: Our goal is to measure the lift provided from the training on Arena data on the Arena held-out set. To do so, we measure relative improvements on the 500 English LMArena ArenaHard prompts, an in-distribution test set published by Chatbot Arena that demonstrates exceptionally high correlation (98.6%) with human preference rankings from Chatbot Arena battles (Li et al. 2024c). This dataset consists of challenging user-submitted prompts from Arena that have been carefully curated and evaluated against several criteria, including, but not limited to, domain knowledge, complexity, and problem-solving. This dataset is widely used to gauge expected performance on the Arena. To measure improvements, we simulate human preferences using LM-as-a-judge, which allows us to measure a reasonable estimate of the gains in a controlled setting. Various works have shown that this is correlated with human preferences (Dubois et al. 2023; Rafailov et al. 2023; Kim et al. 2023). We compare against Llama-3.1-8B-Instruct (Grattafiori et al. 2024) and measure win-rates using gpt-4o-2024-11-20 as our judge model2424 24 https://platform.openai.com/docs/models/gpt-4o.

**ZH** 评测方法：我们的目标是衡量在 Arena 数据上训练相对于 Arena 留出集所带来的增益。为此，我们测量在 500 条英文 LMArena ArenaHard 提示上的相对改进——这是 Chatbot Arena 发布的一个同分布测试集，与 Chatbot Arena 对战中的人类偏好排序表现出极高（98.6%）的相关性（Li et al. 2024c）。该数据集由 Arena 上具有挑战性的用户提交提示构成，经过精心筛选并依据多项判据评估，包括但不限于领域知识、复杂度与问题解决能力。该数据集被广泛用来估计模型在 Arena 上的预期表现。为衡量改进，我们用「以语言模型充当裁判」来模拟人类偏好，从而在受控设定下合理估计增益。多项工作表明这与人类偏好相关（Dubois et al. 2023; Rafailov et al. 2023; Kim et al. 2023）。我们与 Llama-3.1-8B-Instruct（Grattafiori et al. 2024）比较，并用 gpt-4o-2024-11-20 作为裁判模型测量胜率2424 24 https://platform.openai.com/docs/models/gpt-4o。

**EN** Results: From Figure 10, we observe that as the amount of arena-mix data increases, the models improve in their evaluation on the ArenaHard prompts. Variant 0_arena scores a win-rate of 23.5%, 30_arena scores a win-rate of 42.7%, and variant 70_arena, which is trained on the most arena-mix, data scores a win-rate of 49.9% against Llama-3.1-8B-Instruct. A win-rate of 50% indicates that the compared models (Llama 3.1 8B Instruct and 70_arena) are on par on the ArenaHard test set. The relative gains in win-rates are 81.7% for the 30_arena and 112.3% for the 70_arena variant. The gains we observe are striking in part because we do not heavily optimize these variants (we trained 3 variants in total and did no hyperparameter optimization or tuning of training steps). To assess whether performance gains generalize beyond the Arena benchmark, we evaluated the fine-tuned models on the out-of-distribution benchmark MMLU (Hendrycks et al. 2021). The results reveal a clear divergence in performance trends (Table 9): while increasing the proportion of Chatbot Arena data within a fixed training budget yielded consistent improvements on the Arena test set, MMLU performance slightly declined from 66.5% (0_arena) to 64.4% (30_arena) and 65.9% (70_arena). This suggests that gains from Chatbot Arena data are highly specific and do not translate to broader generalization, raising important questions about whether leaderboard improvements reflect meaningful progress or simply overfitting to a narrow evaluation distribution.

**ZH** 结果：从图 10 可以看到，随着 arena-mix 数据量增加，模型在 ArenaHard 提示上的评测表现提升。变体 0_arena 的胜率为 23.5%，30_arena 为 42.7%，而训练时使用 arena-mix 数据最多的变体 70_arena 相对 Llama-3.1-8B-Instruct 的胜率为 49.9%。50% 的胜率表示被比较的模型（Llama 3.1 8B Instruct 与 70_arena）在 ArenaHard 测试集上势均力敌。胜率的相对增益在 30_arena 上为 81.7%，在 70_arena 上为 112.3%。我们观察到的增益之所以引人注目，部分原因在于我们并没有对这些变体做重度优化（我们总共只训练了 3 个变体，没有做超参数优化或训练步数调整）。为评估性能增益是否泛化到 Arena 基准之外，我们在分布外基准 MMLU（Hendrycks et al. 2021）上评测了微调后的模型。结果显示出明显的性能趋势分化（表 9）：在固定训练预算内提高 Chatbot Arena 数据比例，能在 Arena 测试集上带来持续提升，而 MMLU 性能则从 66.5%（0_arena）略微下降至 64.4%（30_arena）与 65.9%（70_arena）。这表明来自 Chatbot Arena 数据的增益高度特定，并不能转化为更广泛的泛化，由此引出重要问题：排行榜上的提升究竟反映了有意义的进步，还是仅仅对狭窄评测分布的过拟合。

**EN** We also note that often it is not necessary to train explicitly on the data to gain from data access. For example, providers may use the composition of the data to make decisions about weighting different data sources (Üstün et al. 2024), or may use a small subset of the data to create high-quality synthetic data that is close to the original distribution (Odumakinde et al. 2024; Shimabucoro et al. 2024; Dang et al. 2024a; Aakanksha et al. 2024). Given the stakes behind ranking highly on Chatbot Arena, it is likely that the data at a provider’s disposal from Chatbot Arena is being actively leveraged by different providers to gain an advantage.

**ZH** 我们还注意到，往往并不需要显式地在数据上训练才能从数据访问中获益。例如，提供方可以利用数据的构成来决定不同数据源的权重（Üstün et al. 2024），或取一小部分数据来生成接近原始分布的高质量合成数据（Odumakinde et al. 2024; Shimabucoro et al. 2024; Dang et al. 2024a; Aakanksha et al. 2024）。鉴于在 Chatbot Arena 上取得高排名的利害关系，提供方手头来自 Chatbot Arena 的数据很可能正被不同提供方积极利用以获取优势。

**EN** 5 Results: Impact of Model Deprecation on Arena Scores

**ZH** 5 结果：模型下架对 Arena 分数的影响

<!-- [原子块 · svg]  -->

**EN** According to the backend codebase of Chatbot Arena 2525 25 http://github.com/lm-sys/FastChat/blob/0e6d3e4beaab66f4d3f93db72541a4abab8af28d/fastchat/serve/monitor/monitor_md.py#L7 , 47 models are publicly listed as deprecated. In addition, as discussed in Section 4.1, 205 models on Chatbot Arena have been silently deprecated by reducing their active sampling rates to near zero (see Figure 18). We observe that model deprecation disproportionately affects different types of models. Specifically, 87.8% of open weights and 89% of open-source models have been deprecated, in contrast to a lower deprecation rate of 80% for proprietary models.

**ZH** 根据 Chatbot Arena 的后端代码库 2525 25 http://github.com/lm-sys/FastChat/blob/0e6d3e4beaab66f4d3f93db72541a4abab8af28d/fastchat/serve/monitor/monitor_md.py#L7 ，有 47 个模型被公开列为已下架。此外，如第 4.1 节所讨论，Chatbot Arena 上有 205 个模型通过把活跃采样率降至接近零而被静默下架（见图 18）。我们观察到模型下架对不同类型的模型影响不同。具体地，87.8% 的开放权重模型与 89% 的开源模型已被下架，相比之下专有模型的下架率较低，为 80%。

<!-- [原子块 · object]  -->

**EN** Figure 13: Share of proprietary and open models that either officially deprecated or inactive on the arena based on leaderboard-stats during the period March 3rd-April 23rd, 2025. Overall, open-weight and fully open-source models are more likely to become deprecated or inactive compared to proprietary models.

**ZH** 图 13：2025 年 3 月 3 日至 4 月 23 日期间，基于 leaderboard-stats 的 Arena 上已正式下架或处于非活跃状态的专有与开放模型占比。总体上，开放权重与完全开源模型比专有模型更可能被下架或变为非活跃。

**EN** While deprecating older models is necessary to maintain a dynamic leaderboard, especially as new models are introduced regularly, we question how excessive deprecation may compromise the reliability and stability of model rankings. When models are deprecated, future models that enter the Arena will not have direct comparisons with them. However, in principle, the BT model should still handle this reliably because of the transitivity property (Boubdir et al. 2024). Intuitively, transitivity means that if model A is better than model B, and model B is better than model C, then model A should also be better than model C. Transitivity allows the BT model to infer missing outcomes—if two models share common opponents, their relative ranking can be deduced even without a direct comparison (Bradley & Terry 1952). Formally, in the BT model each competitor ⟦SLOT_14⟧ is associated with a positive parameter ⟦SLOT_15⟧, and the probability that model ⟦SLOT_16⟧ beats model ⟦SLOT_17⟧ is given by:

**ZH** 虽然下架旧模型对于维持一个动态排行榜是必要的——尤其在新模型不断涌入的情况下——我们质疑过度的下架会如何损害模型排名的可靠性与稳定性。当模型被下架后，之后进入 Arena 的新模型将无法与它们直接比较。然而，原则上 BT 模型应当仍能可靠地处理这一情况，因为它具有传递性（Boubdir et al. 2024）。直观地讲，传递性意味着：若模型 A 优于模型 B，且模型 B 优于模型 C，则模型 A 也应当优于模型 C。传递性使 BT 模型能够推断缺失的对局结果——如果两个模型有共同的对手，即便没有直接对局，也能推导出它们的相对排名（Bradley & Terry 1952）。形式化地，在 BT 模型中每个竞争者 ⟦SLOT_14⟧ 关联一个正参数 ⟦SLOT_15⟧，模型 ⟦SLOT_16⟧ 胜过模型 ⟦SLOT_17⟧ 的概率为：

<!-- [原子块 · table] P ⁡ ( i > j ) = π i π i + π j . P(i>j)=\frac{\pi_{i}}{\pi_{i}+\pi_{j}}. -->

**EN** Suppose ⟦SLOT_18⟧ and ⟦SLOT_19⟧. Then

**ZH** 假设 ⟦SLOT_18⟧ 与 ⟦SLOT_19⟧。那么

<!-- [原子块 · table] P ⁡ ( A > B ) = π A π A + π B > 0.5 and P ⁡ ( B > C ) = π B π B + π C > 0.5 . P(A>B)=\frac{\pi_{A}}{\pi_{A}+\pi_{B}}>0.5\quad\text{and}\quad P(B>C)=\frac{\pi_{B}}{\pi_{B}+\pi_{C}}>0.5. -->

**EN** Moreover, because ⟦SLOT_20⟧, we have:

**ZH** 此外，由于 ⟦SLOT_20⟧，我们有：

<!-- [原子块 · table] π A + π C < π A + π B ⟹ P ⁡ ( A > C ) = π A π A + π C > π A π A + π B . \pi_{A}+\pi_{C}<\pi_{A}+\pi_{B}\quad\Longrightarrow\quad P(A>C)=\frac{\pi_{A}}{\pi_{A}+\pi_{C}}>\frac{\pi_{A}}{\pi_{A}+\pi_{B}}. -->

**EN** Transitivity is a critical property that allows for inferring rankings using fewer data points. However, transitivity requires several underlying properties to hold. In particular, two of these properties are salient for our study of the impact of deprecation on reliability:

**ZH** 传递性是一项关键性质，它使得用更少的数据点推断排名成为可能。然而，传递性要求若干底层性质成立。其中有两项性质对我们研究下架对可靠性的影响尤为突出：

**EN** • Assumption 1: Evaluation conditions remain constant. Transitivity relies on the assumption that evaluation conditions remain constant—that is, paired comparisons must come from a consistent set of tasks or contexts. For example, consider a setting where Tom wins against Susan in chess, and Susan wins against Ronald in both chess and tennis. We can infer Tom’s ranking relative to Ronald in chess, but not in tennis. In practice, Chatbot Arena’s prompt categories and task types evolve over time, and some models become deprecated, meaning they are no longer re-evaluated under the current conditions. We show in Section 5.1 that when a model’s battle history is limited to outdated conditions, its comparisons no longer accurately reflect performance in the new context.

**ZH** • 假设 1：评测条件保持不变。传递性依赖于「评测条件保持不变」这一假设——即成对比较必须来自一致的任务或语境集合。例如，考虑这样一个设定：Tom 在国际象棋中战胜 Susan，而 Susan 在国际象棋和网球中都战胜 Ronald。我们可以推断 Tom 相对于 Ronald 在国际象棋上的排名，但在网球上不行。在实践中，Chatbot Arena 的提示类别与任务类型随时间演化，且一些模型被下架，意味着它们不再在当前条件下被重新评测。我们在第 5.1 节表明，当一个模型的对战历史局限于过时的条件时，它的比较结果就不再准确反映其在新语境下的表现。

**EN** • Assumption 2: Network of comparisons must be fully interconnected. Every model must be linked directly or indirectly through pairwise matchups. So in a chess example, we can estimate Tom’s performance against Ronald because they have each played at least one competitor in common (in this case, Susan). If Ronald has had no matches with anyone who has played Tom, we can no longer infer reliably what their rankings are relative to each other. Deviations from transitivity or a fragmented comparison graph can compromise the reliability and consistency of the strength estimates. In Section 5.2, we show that deprecations may result in these fragmented graphs.

**ZH** • 假设 2：比较网络必须完全连通。每个模型都必须通过成对对局直接或间接地相连。仍以国际象棋为例，我们之所以能估计 Tom 相对于 Ronald 的表现，是因为他们各自至少与一位共同竞争者（此处为 Susan）对局过。如果 Ronald 没有与任何和 Tom 对局过的人交手，我们就无法再可靠地推断二者的相对排名。偏离传递性或比较图碎片化，会损害强度估计的可靠性与一致性。在第 5.2 节，我们表明下架可能导致这类碎片化的图。

**EN** In Section 5.1 and Section 5.2 that follow, we will interrogate whether Chatbot Arena fulfills each of these assumptions.

**ZH** 在随后的第 5.1 节与第 5.2 节中，我们将检验 Chatbot Arena 是否满足这两项假设。

**EN** 5.1 Transitivity Under Changing Evaluation Conditions

**ZH** 5.1 评测条件变化下的传递性

**EN** As we have shown in Section 4.1, the distribution of Chatbot Arena is unique since long-term shifts occur in categories and use cases. This distributional shift contrasts with the static environments typically assumed in Elo and Bradley-Terry systems, such as chess, where the rules and game format remain fixed, ensuring a consistent set of evaluation conditions. If all models were continuously sampled across all points in time, the BT model would likely remain robust because every model would be evaluated on the evolving distribution of tasks. However, as shown in Figure 13, many models are deprecated over time, and their scores stop getting updated.

**ZH** 如第 4.1 节所示，Chatbot Arena 的分布是独特的，因为类别与用例会发生长期漂移。这种分布漂移与 Elo 和 Bradley-Terry 系统通常假设的静态环境形成对比——例如国际象棋，其规则与赛制保持固定，从而保证了一致的评测条件集合。如果所有模型在所有时间点上都持续被采样，BT 模型很可能仍然稳健，因为每个模型都会在演化的任务分布上被评测。然而，如图 13 所示，许多模型随时间被下架，其分数不再更新。

**EN** Experimental Setup: To investigate how model deprecations under a changing task distribution can impact model rankings, we simulate BT rankings of models under evolving evaluation conditions. We initialize four models—A, B, C, and D—each with distinct performance profiles across two task types, Task-1 and Task-2. These tasks represent different prompt categories, and each model’s relative strength is defined through task-specific win probabilities. For example, model B has a 90% chance of defeating model D on Task-1 but only a 20% chance on Task-2, with some pairs also allowing for ties. The task-specific win probabilities for different models are provided in Table 8. These probabilities reflect the models’ varying strengths across tasks, mirroring the real-world observation that models excel at different types of prompts.

**ZH** 实验设置：为研究在变化的任务分布下模型下架会如何影响模型排名，我们模拟了演化评测条件下模型的 BT 排名。我们初始化四个模型——A、B、C、D——它们在两类任务（Task-1 与 Task-2）上各有不同的性能剖面。这些任务代表不同的提示类别，每个模型的相对强弱通过任务特定的胜率定义。例如，模型 B 在 Task-1 上有 90% 的概率战胜模型 D，但在 Task-2 上只有 20% 的概率，某些配对还允许平局。不同模型的任务特定胜率见表 8。这些概率反映了模型在不同任务上的强弱差异，对应了「模型在不同类型提示上各有所长」这一真实观察。

**EN** The simulation is structured into two sequential phases to mimic the evolving task distribution observed on Chatbot Arena. During the first phase, battles are predominantly drawn from Task-1. Each of the four models participates in 1000 battles, and the resulting outcomes are used to compute initial rankings. In the second phase, the battle distribution gradually shifts toward Task-2. Since model win-rates are task-dependent, battle outcomes change accordingly. We simulate 1000 additional battles in this phase and examine two scenarios to investigate how shifts in prompt distribution and model deprecations jointly influence final rankings. We compute the BT Scores for all models under both scenarios using the implementation provided by Chatbot Arena in their official FastChat codebase2626 26 https://github.com/lm-sys/FastChat/blob/main/fastchat/serve/monitor/rating_systems.py . These scores are then used to determine the final model ranks.

**ZH** 模拟分为两个连续阶段，以模仿在 Chatbot Arena 上观察到的任务分布演化。第一阶段，对战主要取自 Task-1。四个模型各参与 1000 场对战，结果用于计算初始排名。第二阶段，对战分布逐渐向 Task-2 偏移。由于模型胜率依赖任务，对战结果随之改变。我们在该阶段模拟额外 1000 场对战，并考察两种场景，以研究提示分布偏移与模型下架如何共同影响最终排名。两种场景下，我们都使用 Chatbot Arena 在其官方 FastChat 代码库2626 26 https://github.com/lm-sys/FastChat/blob/main/fastchat/serve/monitor/rating_systems.py 中提供的实现来计算所有模型的 BT 分数。这些分数随后用于确定最终的模型排名。

<!-- [原子块 · object]  -->

<!-- [原子块 · table] Model w/o dep w/ dep A 1 2 B 2 1 D 3 4 C 4 3 -->

**EN** Figure 14: Impact of evolving task distributions and model deprecation on model rankings. Left: Two-phase task distribution used in the simulation. Phase 1 is Task-1 heavy, with most battles based on Task-1; Phase 2 is Task-2 heavy, with battles predominantly based on Task-2. Right: Model rankings under changing task distributions and deprecation settings. Scenario I only differs from Scenario II in that Model D is deprecated halfway through the battle history (after phase 1). This deprecation causes Scenario II to produce a completely different ranking over models as compared to Scenario I.

**ZH** 图 14：演化的任务分布与模型下架对模型排名的影响。左：模拟中使用的两阶段任务分布。阶段 1 以 Task-1 为主，大部分对战基于 Task-1；阶段 2 以 Task-2 为主，对战主要基于 Task-2。右：变化的任务分布与下架设定下的模型排名。场景 II 与场景 I 的唯一区别是模型 D 在对战历史的中途（阶段 1 之后）被下架。这一下架使场景 II 产生了与场景 I 完全不同的模型排名。

**EN** • Scenario I: without deprecation. We simulate all 2000 battles across both phases, with all four models participating throughout. This represents an ideal scenario where no model is deprecated, and all are evaluated across the evolving task distribution.

**ZH** • 场景 I：不下架。我们模拟两个阶段共 2000 场对战，四个模型全程参与。这代表没有模型被下架、所有模型都在演化的任务分布上被评测的理想场景。

**EN** • Scenario II: with deprecation. We simulate all 2000 battles across both phases. However, at the end of phase 1, model D is deprecated and does not participate in the second phase.

**ZH** • 场景 II：有下架。我们同样模拟两个阶段共 2000 场对战。但在阶段 1 结束时，模型 D 被下架，不再参与第二阶段。

**EN** Deprecation given changing distribution results in unreliable Arena rankings: As illustrated in Figure 14, our simulation shows that rankings produced by the BT model are highly sensitive to model deprecation, particularly when the prompt distribution changes over time. In the scenario without deprecation, we observe the true rankings given that the BT model remains reliable because it reflects performance across the full history of interactions. However, we observe the rankings differ if we deprecate Model D between stages. While its matchups from Phase 1 still influence BT scores, the absence of updated comparisons causes a skew in the rankings of remaining models. Models A and D are ranked lower, and Models B and C are ranked higher than their true performance merits. Comparing Scenarios I and II in Figure 14 reveals a clear divergence, with the scenario involving deprecation yielding unreliable rankings that no longer reflect true relative performance under the evolving task distribution.

**ZH** 分布变化下的下架导致 Arena 排名不可靠：如图 14 所示，我们的模拟表明 BT 模型产生的排名对模型下架高度敏感，尤其当提示分布随时间变化时。在不下架的场景中，我们观察到真实排名，因为 BT 模型保持可靠——它反映了全部交互历史中的表现。然而，如果我们在两个阶段之间下架模型 D，排名就会不同。虽然它来自阶段 1 的对局仍会影响 BT 分数，但缺少更新的比较会导致其余模型的排名出现偏斜。模型 A 与 D 被排得更低，而模型 B 与 C 被排得高于其真实表现应得的位置。比较图 14 中的场景 I 与 II 可以发现明显分歧：含下架的场景产生了不可靠的排名，不再反映演化任务分布下的真实相对表现。

**EN** This violates core assumptions of the BT model, namely, that rankings reflect transitive and consistently sampled matchups, ultimately compromising the validity of inferred rankings. When models are no longer sampled under current task distributions, historical pairwise comparisons cease to represent present-day performance. This issue is particularly problematic in real-world settings where user prompt distributions shift over time. For instance, a model tuned for multilingual prompts may improve ranking as non-English tasks become more common. However, if deprecated, its BT ranking will likely understate its true performance. Similarly, code-specialized models may benefit from the increasing volume of coding tasks, but only if they continue to participate in evaluation.

**ZH** 这违反了 BT 模型的核心假设，即排名应反映传递的、一致采样的对局，最终损害了推断排名的有效性。当模型不再在当前任务分布下被采样时，历史成对比较就不再代表当下的表现。在用户提示分布随时间变化的真实设定中，这一问题尤其突出。例如，一个针对多语言提示调优的模型，会随着非英语任务变得更常见而提升排名；但若被下架，其 BT 排名很可能低估它的真实表现。类似地，代码专用模型可能受益于编码任务量的增长，但前提是它们继续参与评测。

**EN** 5.2 Sparse Battle History Risks

**ZH** 5.2 稀疏对战历史的风险

**EN** In this section, we show that the deprecation policy can lead to a sparse matrix and disconnected comparison graphs, which in turn distort the resulting rankings. As demonstrated by Ford Jr 1957, the maximum likelihood estimate does not exist if models can be partitioned into two non-empty subsets without comparisons between them or if all comparisons between the two groups are one-sided (i.e., one group always wins). Therefore, to ensure a unique and finite estimation, the comparison graph must be connected. For any possible partition of models, there must be at least one win going in each direction across the partition. This ensures that no subset of models is entirely isolated in the win/loss structure. The Chatbot Arena comparison matrix can potentially become disconnected because of the extremely high levels of model removals over time (as discussed in Figure 13).

**ZH** 在本节中，我们表明下架政策会导致稀疏矩阵与不连通的比较图，进而扭曲所得排名。正如 Ford Jr 1957 所证明的，如果模型可以被划分为两个非空子集且二者之间没有比较，或者两组之间的所有比较都是单向的（即一组总是获胜），那么极大似然估计不存在。因此，为保证估计唯一且有限，比较图必须是连通的。对模型的任意一种划分，都必须至少各有一个方向的胜利跨越该划分。这确保没有哪个模型子集在胜负结构中是完全孤立的。Chatbot Arena 的比较矩阵可能因极高的模型移除率而变得不连通（如图 13 所述）。

<!-- [原子块 · table] Model Dense Disconnected A 1 1 B 2 2 C 3 3 D 4 5 F 5 4 E 6 7 G 7 6 -->

<!-- [原子块 · object]  -->

**EN** Figure 15: Impact of comparison graph sparsity on model rankings. Left: Rankings for models D, E, F, and G diverge from the gold rankings when the comparison graph is sparse, whereas model rankings fully align with the gold rankings when the comparison graph is dense. Right: Visualization of the comparison graphs in sparse and dense settings. An edge between two models indicates a head-to-head matchup, annotated with the number of wins for each model. For example, in the sparse graph, Model A and Model B played 437 matches, with Model A winning 266 and Model B winning 171.

**ZH** 图 15：比较图稀疏性对模型排名的影响。左：当比较图稀疏时，模型 D、E、F、G 的排名与金标准排名出现分歧；而当比较图稠密时，模型排名与金标准排名完全一致。右：稀疏与稠密设定下比较图的可视化。两个模型之间的边表示一次正面对局，标注了各自的胜场数。例如，在稀疏图中，模型 A 与模型 B 对局 437 场，模型 A 胜 266 场，模型 B 胜 171 场。

**EN** Experiment Setup: To investigate the impact of sparse comparison graphs on the rankings obtained via the Bradley-Terry model used by Chatbot Arena we simulate the following scenarios:

**ZH** 实验设置：为研究稀疏比较图对 Chatbot Arena 所用 Bradley-Terry 模型所得排名的影响，我们模拟了以下场景：

**EN** • Scenario I: Dense comparison graph. All models are allowed to compete against one another—albeit with varying numbers of head-to-head battles—resulting in a well-connected comparison graph in which every node (model) is linked to others via edges representing battle outcomes.

**ZH** • 场景 I：稠密比较图。所有模型都被允许相互竞争——尽管正面对局次数各不相同——从而形成一个连通良好的比较图，其中每个节点（模型）都通过代表对局结果的边与其他节点相连。

**EN** • Scenario II: Disconnected comparison graph. We create a disconnected battle history by imposing constraints on which pairs of models are allowed to engage in battles. This allows us to create a sparse battle history where each model ends up playing against a subset of models.

**ZH** • 场景 II：不连通的比较图。我们通过限制哪些模型对之间允许进行对战，构造出一个不连通的对战历史。这使我们能够创建稀疏的对战历史，其中每个模型最终只与部分模型对局。

**EN** The full comparison graph based on battle histories for both scenarios is shown in Figure 15. In both scenarios, a total of 2000 battles are played under the corresponding setting. For a paired match between models A and B, each with respective true skill ratings ⟦SLOT_21⟧ and ⟦SLOT_22⟧, the expected scores ⟦SLOT_23⟧ and ⟦SLOT_24⟧ can be computed as:

**ZH** 两种场景下基于对战历史的完整比较图见图 15。在两种场景中，各在相应设定下共进行了 2000 场对战。对于模型 A 与 B 之间的一场配对对局，二者各自的真实技能评分为 ⟦SLOT_21⟧ 与 ⟦SLOT_22⟧，其期望得分 ⟦SLOT_23⟧ 与 ⟦SLOT_24⟧ 可计算为：

<!-- [原子块 · table] E A = 1 1 + e α ⁡ ( r B − r A ) , E B = 1 1 + e α ⁡ ( r A − r B ) E_{A}=\frac{1}{1+e^{\alpha(r_{B}-r_{A})}},\quad E_{B}=\frac{1}{1+e^{\alpha(r_{A}-r_{B})}} (2) -->

**EN** The expected scores ⟦SLOT_25⟧ and ⟦SLOT_26⟧ are used to predict the winner of the battle. For simplicity, we exclude the possibility of ties in this experiment. We assign the following true skill ratings to the models: 1450 (Model A), 1390 (Model B), 1250 (Model C), 1200 (Model D), 1101 (Model E), 1150 (Model F), and 1000 (Model G). These ratings are used to calculate the expected scores and match outcomes. Finally, we compute BT Scores for all models under both scenarios using the official implementation, followed by Chatbot Arena 26. This is then used to determine the ranks for each model corresponding to both scenarios.

**ZH** 期望得分 ⟦SLOT_25⟧ 与 ⟦SLOT_26⟧ 被用于预测对战的胜者。为简洁起见，本实验排除平局的可能。我们为各模型设定如下真实技能评分：1450（模型 A）、1390（模型 B）、1250（模型 C）、1200（模型 D）、1101（模型 E）、1150（模型 F）与 1000（模型 G）。这些评分用于计算期望得分与对局结果。最后，我们使用官方实现计算两种场景下所有模型的 BT 分数26。据此确定两种场景下各模型的排名。

**EN** Sparse or disconnected graphs lead to unreliable rankings: Figure 15 illustrates the model rankings with sparse and dense battle history graphs. We observe that the rankings derived from the dense comparison graph align closely with the models’ rankings according to their true skill ratings. In contrast, a sparse or disconnected comparison graph results in an inaccurate estimation of the models’ skills. These results highlight that reliable rankings under the BT model require a connected comparison graph. While some level of model removal is inevitable (for example, models are no longer hosted on an API), preserving connectivity means ensuring that comparisons remain sufficiently distributed across active models and that transitions in and out of the pool do not isolate subsets of models from the broader comparison structure.

**ZH** 稀疏或不连通的图导致不可靠的排名：图 15 展示了稀疏与稠密对战历史图下的模型排名。我们观察到，从稠密比较图得出的排名与按真实技能评分得到的模型排名高度一致。相比之下，稀疏或不连通的比较图会导致对模型技能的不准确估计。这些结果凸显：在 BT 模型下获得可靠排名需要连通的比较图。虽然一定程度的模型移除不可避免（例如模型不再托管在 API 上），但保持连通性意味着要确保比较在活跃模型之间保持充分分布，并且模型进出评测池的更替不会把某些模型子集从更广泛的比较结构中孤立出去。

**EN** 6 Recommendations and Guidelines for Improving Leaderboards

**ZH** 6 改进排行榜的建议与准则

**EN** When my information changes, I alter my conclusions. What do you do, sir? — John Maynard Keynes

**ZH** 当我的信息改变时，我会改变我的结论。先生，您会怎么做？——约翰·梅纳德·凯恩斯

**EN** We include below recommendations that we believe are urgent and critical. However, we also believe these recommendations are very achievable and will restore scientific credibility and trust within the wider research ecosystem:

**ZH** 我们在下面列出我们认为紧迫且关键的建议。同时我们也相信，这些建议是切实可行的，并将在更广泛的研究生态中恢复科学可信度与信任：

**EN** Prohibit score retraction after submission. Currently, providers who have engaged in private testing are allowed to retract submissions and only submit the best variant to the public leaderboard. As we have shown in Section 4.1, this can lead to overfitting and obscures meaningful progress as it makes it difficult to distinguish between models that have legitimately improved versus those that have exploited statistical shortcuts (Ying 2019). We urge Chatbot Arena to prohibit retraction after submission, ensuring all tested variants’ scores are permanently visible on the leaderboard. Providers should also disclose the total number of private variants tested prior to public launch, including historical submissions, to contextualize their results.

**ZH** 禁止提交后撤回分数。目前，参与了私有测试的提供方被允许撤回提交，只把最好的变体提交到公开排行榜。如第 4.1 节所示，这会导致过拟合，并掩盖有意义的进步，因为它使「真正改进的模型」与「利用了统计捷径的模型」难以区分（Ying 2019）。我们敦促 Chatbot Arena 禁止提交后撤回，确保所有被测试变体的分数在排行榜上永久可见。提供方还应披露公开发布前测试的私有变体总数，包括历史提交，以便为他们的结果提供语境。

**EN** Establish transparent limits on the number of private variants per provider. As illustrated in Figure 6, private testing volume varies widely across providers, creating unfair advantages. To curb overfitting and level the playing field, Chatbot Arena should enforce a strict cap of private variants per provider for any given model launch. This should be enforced at a provider level, and not per model type and size as that is impossible to audit with API hosting. This strict limit should be disclosed to all providers (proprietary, open-weights, open-source) and to the wider Chatbot Arena community. This restriction would discourage excessive undisclosed testing while still allowing limited iteration.

**ZH** 为每个提供方的私有变体数量设定透明上限。如图 6 所示，各提供方的私有测试量差异极大，造成了不公平的优势。为抑制过拟合、拉平竞争环境，Chatbot Arena 应对任何一次模型发布中每个提供方的私有变体数量施加上限。这一上限应在提供方层面执行，而不是按模型类型与规模执行，因为在 API 托管的情形下后者无法审计。这一上限应向所有提供方（专有、开放权重、开源）以及更广泛的 Chatbot Arena 社区公开。该限制既能抑制过度的未披露测试，又仍允许有限的迭代。

**EN** Establish clear and auditable model deprecation criteria. The current criteria, which states “Models may be retired after 3000 votes if there are two more recent models in the same series and/or if there are more than 3 providers that offer models cheaper or same price and strictly better (according to overall Arena score) than this model” is ambiguous and make it impossible to audit the logic in practice. Key terms like “same series” and “more recent” lack formal definitions, making it unclear how to determine whether a model is eligible for retirement based on lineage. Additionally, the requirement that “more than 3 providers” must offer strictly better and cheaper models introduces confusion around what threshold of improvement in Arena Score is considered meaningful. The use of “and/or” further complicates interpretation, as it’s unclear whether meeting one condition is sufficient or if both must be satisfied. Lastly, using price as a filtering criterion is problematic since it’s subject to change, varies across hosting platforms, and is not inherently tied to a model’s performance or utility. We note that many of these models are hosted for free on the Arena, and so there should be clarity about what source of pricing is being used. This lack of precision makes it challenging to apply the rule consistently or verify retirement decisions.

**ZH** 建立清晰且可审计的模型下架标准。当前标准表述为「模型在获得 3000 票后可能被退役，如果同系列中有两个更新的模型，和/或如果有超过 3 家提供方提供更便宜或同价且（按整体 Arena 分数）明显更好的模型」，这一表述含糊不清，使该逻辑在实践中无法审计。「同系列」「更新」等关键术语缺乏正式定义，导致不清楚如何依据谱系判断一个模型是否符合退役条件。此外，「超过 3 家提供方」必须提供更优且更便宜的模型这一要求，也带来了困惑：究竟 Arena 分数提升多少才算有意义。「和/或」的使用进一步加剧了解释上的困难——不清楚满足其中一个条件是否足够，还是两个条件都必须满足。最后，用价格作为筛选标准是有问题的，因为价格会变动、在不同托管平台间不同，并且与模型的性能或效用没有内在关联。我们注意到这些模型中有许多在 Arena 上是免费托管的，因此应当明确所使用的是哪种价格来源。这种精确性的缺失使该规则难以被一致地适用，也难以验证退役决策。

**EN** We recommend a stratified approach that retires models proportionally across proprietary, open-weight, and open-source categories to preserve balance and fairness in the evaluation based on two criteria: availability and performance. We propose retiring the bottom 30th percentile within each category of open-source, open-weight, and proprietary after rankings converge. This stratified pruning prevents provider-type bias, keeps strong models from underrepresented groups visible, and maintains comparison graph connectivity. It also reduces ranking inconsistencies seen with uneven retirement, as discussed in Section 5.

**ZH** 我们建议采取一种分层方法，在专有、开放权重与开源三个类别中按比例退役模型，以在基于可用性与性能两项判据的评测中保持平衡与公平。我们提议在排名收敛后，在开源、开放权重与专有各类别中退役末位 30% 的模型。这种分层剪枝可避免提供方类型偏见，让来自代表性不足群体的强模型保持可见，并维持比较图的连通性。它还能减少第 5 节所讨论的、因退役不均造成的排名不一致。

**EN** Improve sampling fairness. As shown in Figure 5, the sampling rates vary greatly by providers, and also disproportionately undersample open-weight and open-source models, creating large asymmetries in data access over time and resulting in unstable Arena scores (Section 5). This is particularly important given that this is a community-driven voting benchmark, where at present free human feedback is primarily benefiting proprietary models. This avoids disparities over time and a status quo where proprietary models are benefiting more from valuable and freely given human data (Sambasivan et al. 2021). In their own work (Chiang et al. 2024) (Section 5, Equation 9), the Chatbot Arena authors introduce an active sampling rule designed to enhance the efficiency and statistical robustness of the leaderboard’s evaluation process. This rule selects model pairs based on the expected reduction in the confidence interval of the win-rate estimate, and is formally defined as:

**ZH** 提升采样公平性。如图 5 所示，各提供方的采样率差异巨大，并且不成比例地低采样开放权重与开源模型，随时间推移造成巨大的数据访问不对称，并导致 Arena 分数不稳定（第 5 节）。这一点尤其重要，因为这是一个社区驱动的投票基准，而目前免费的人类反馈主要惠及专有模型。这可以避免长期的不平等，以及专有模型从宝贵且无偿提供的人类数据中获益更多的现状（Sambasivan et al. 2021）。在他们自己的工作（Chiang et al. 2024）（第 5 节，式 9）中，Chatbot Arena 的作者提出了一种主动采样规则，旨在提升排行榜评测过程的效率与统计稳健性。该规则依据胜率估计置信区间的预期缩减量来选择模型对，其正式定义为：

<!-- [原子块 · table] P t ( a ) ∝ Σ t , a , a | { t : A t = a } | − Σ t , a , a | { t : A t = a } | + 1 P_{t}(a)\propto\sqrt{\frac{\Sigma_{t,a,a}}{|\{t:A_{t}=a\}|}}-\sqrt{\frac{\Sigma_{t,a,a}}{|\{t:A_{t}=a\}|+1}} -->

**EN** where ⟦SLOT_27⟧ is the sampling probability of model pair ⟦SLOT_28⟧ at time ⟦SLOT_29⟧, and ⟦SLOT_30⟧ is the estimated variance for the win-rate of pair ⟦SLOT_31⟧ at time ⟦SLOT_32⟧.

**ZH** 其中 ⟦SLOT_27⟧ 是模型对 ⟦SLOT_28⟧ 在时刻 ⟦SLOT_29⟧ 的采样概率，⟦SLOT_30⟧ 是模型对 ⟦SLOT_31⟧ 在时刻 ⟦SLOT_32⟧ 胜率估计的估计方差。

**EN** This formulation effectively prioritizes under-evaluated and high-variance pairs, aligning sampling with the goal of rapidly reducing uncertainty in rankings. While this sampling rule is clearly articulated in the paper, we have not seen evidence of its deployment in the current leaderboard. We recommend adopting this sampling strategy in practice and providing periodic reporting on its usage. Doing so would align the platform’s operations with its methodological innovations, support more balanced and transparent evaluations, and improve confidence in leaderboard dynamics over time.

**ZH** 这一公式有效地优先选择评测不足与高方差的模型对，使采样与「快速降低排名不确定性」的目标相一致。虽然该采样规则在论文中被清晰阐述，但我们没有在当前排行榜上看到它被部署的证据。我们建议在实践中采用这一采样策略，并对其使用情况进行定期报告。这样做将使平台的运营与其方法创新保持一致，支持更均衡、更透明的评测，并随时间提升对排行榜动态的信心。

**EN** Provide public transparency into all tested models, deprecations, and sampling rates. Most of these findings were only possible through access to private model testing, or crawling Chatbot Arena over a period of time. Providing transparency into the full suite of models that were tested, deprecated, and how often they were sampled against which other models, would enable the oversight and trust in the benchmark that Chatbot Arena affirms in their policies. This transparency could be provided on a rolling basis (e.g., every quarter, for the prior quarter of model battles). It would enable the community to help in the process of continuing to improve this community benchmark. For instance, the backend codebase of Chatbot Arena– FastChat – publicly lists deprecated models on GitHub25, where 47 models are explicitly marked as deprecated. However, four times that number have been silently deprecated without warning. We recommend Chatbot Arena expand the definition of “deprecated” to include models that are no longer being regularly sampled from, and list these deprecated models on their website to make it transparent for everyone which models are no longer active on Chatbot Arena.

**ZH** 为所有被测试的模型、下架情况与采样率提供公开透明度。这些发现大多只能通过访问私有模型测试，或持续爬取 Chatbot Arena 一段时间才得以获得。若能对被测试、被下架的全部模型，以及它们与哪些其他模型对战、被采样的频率提供透明度，将有助于实现 Chatbot Arena 在其政策中所宣称的对该基准的监督与信任。这种透明度可以按滚动方式提供（例如每季度公布上一季度的模型对战情况）。它将使社区得以参与持续改进这一社区基准的过程。例如，Chatbot Arena 的后端代码库 FastChat 在 GitHub 上公开列出了已下架的模型25，其中 47 个模型被明确标记为已下架。然而，有四倍于此数量的模型在毫无预警的情况下被静默下架。我们建议 Chatbot Arena 扩大「已下架」的定义，把那些不再被定期采样的模型也纳入其中，并在其网站上列出这些已下架模型，让所有人都能清楚看到哪些模型在 Chatbot Arena 上已不再活跃。

**EN** 7 Limitations

**ZH** 7 局限性

**EN** We do not have insight into Chatbot Arena’s raw data: A subset of the data sources utilized for this study have undergone pre-processing by Chatbot Arena, which as stated by Chatbot Arena often involves de-duplication, removal of battles corresponding to suspicious voting patterns, etc (Chiang et al. 2024). Through this work, we also establish that private battles are removed from the datasets released by Chatbot Arena. Although we also have proprietary API data for the models we test on the Arena, it only reveals a subset of battles. Without access to original and comprehensive raw data, it is hard to investigate patterns related to adversarial voting where users intentionally submit votes to manipulate rankings or undermine the system. Various previous works have shown that adversarial voting is a critical concern for the reliability of any crowd-sourced evaluation platform like Chatbot Arena (Huang et al. 2025) (Min et al. 2025). We do not explore this in this work, but see more investigation here as an important topic for future work.

**ZH** 我们无法看到 Chatbot Arena 的原始数据：本研究使用的部分数据源经过了 Chatbot Arena 的预处理，据 Chatbot Arena 说明，这通常包括去重、移除对应可疑投票模式的对战等（Chiang et al. 2024）。通过本工作我们还证实，私有对战会从 Chatbot Arena 发布的数据集中被移除。尽管我们也拥有我们在 Arena 上测试的模型的专有 API 数据，但它只揭示了一部分对战。在无法获得原始且完整的数据的情况下，很难研究与对抗性投票相关的模式——即用户故意提交投票以操纵排名或破坏系统。多项已有研究表明，对抗性投票是 Chatbot Arena 这类众包评测平台可靠性的关键隐患（Huang et al. 2025）（Min et al. 2025）。本文不对此展开探讨，但认为这方面的进一步研究是未来工作的重要课题。

**EN** Our scraped data snapshot only covers a limited period: Our scraped-random-sample was the only way to identify private variants being tested by various providers. However, it covers a limited time period from January–March, 2025. This time frame coincided with Meta’s launch of Llama 4, and so we find them to be the provider with the highest number of private variants in our analysis. We believe we might be underestimating the counts for providers having fewer model launches during this period.

**ZH** 我们抓取的数据快照只覆盖有限的时段：我们的 scraped-random-sample 是识别各提供方正在测试的私有变体的唯一途径。但它只覆盖 2025 年 1—3 月这一有限时段。这一时间窗口恰好与 Meta 发布 Llama 4 重合，因此我们发现它是我们分析中私有变体数量最多的提供方。我们认为，对于在该时段内模型发布较少的提供方，我们可能低估了其数量。

**EN** Our training experiments likely underestimate the potential to overfit: Our estimate of overfitting is likely conservative, as it is based on training with only a fraction of the data believed to be available to some proprietary model providers. This disparity suggests that proprietary models may be trained on 5 to 10 times more data than we use, potentially increasing the risk of overfitting to patterns not present in our smaller subset. These observations underscore the importance of further examining data scale and its implications for model overfitting to certain leaderboards.

**ZH** 我们的训练实验可能低估了过拟合的可能性：我们对过拟合的估计很可能是保守的，因为它是基于只用「据信某些专有模型提供方所能获得数据」的一小部分来训练得出的。这一差距意味着专有模型训练所用的数据可能是我们的 5 到 10 倍，从而可能提升对我们更小子集中所不存在的模式过拟合的风险。这些观察凸显了进一步考察数据规模及其对模型针对特定排行榜过拟合之影响的重要性。

**EN** We rely on the model’s self-identification to attribute private models to their respective providers: Since the identity of anonymous models is not publicly disclosed, we use model self-identification as a proxy—prompting each model directly and observing how it responds. When a model consistently names a particular provider across multiple prompts, we attribute it to that provider. While this method provides a reasonable signal, it is inherently approximate. Due to limited data and the potential for models to respond inconsistently or ambiguously, some misattributions may occur. To encourage validation of our estimates, we include the codename and our estimate of identity in Section E.4. We welcome correspondence with the authors from providers if any of the estimates of ownership are incorrect.

**ZH** 我们依赖模型的自我识别来把私有模型归属到各自提供方：由于匿名模型的身份未被公开披露，我们使用模型的自我识别作为代理——直接提示每个模型并观察它如何回答。当某个模型在多次提示中一致地自称属于某提供方时，我们就把它归属给该提供方。虽然这一方法提供了合理的信号，但它本质上是近似的。由于数据有限，且模型的回答可能不一致或含糊，可能会出现一些误判。为鼓励对我们的估计进行验证，我们在第 E.4 节中列出了代号与我们对身份的估计。若任何所有权估计有误，我们欢迎各提供方的作者来信指正。

**EN** 8 Related Work

**ZH** 8 相关工作

**EN** The strength of science lies in its ability to withstand challenge, verification, and replication. — Richard P. Feynman

**ZH** 科学的力量在于它能够经受挑战、验证与重复检验。——理查德·P·费曼

**EN** 8.1 Meta-studies on the Rigor of Benchmarking in AI

**ZH** 8.1 关于 AI 基准严谨性的元研究

**EN** Our work contributes to a wider body of work examining the role of benchmarks in determining progress in machine learning. Benchmarking has played a central role in shaping research priorities and incentives within the deep learning community (Koch & Peterson 2024). Research has found that benchmarks are rarely impartial and instead shaped by the environments in which the benchmarks are made, finding that assumptions, commitments, and dependencies can often have large implications in final outcomes (Aniba et al. 2010; Bartz-Beielstein et al. 2020). Creating a meaningful and reliable benchmark is challenging, and there has been critical work identifying key benchmark desiderata and open challenges.

**ZH** 我们的工作为「考察基准在决定机器学习进步中作用」的更广泛研究做出贡献。基准化在塑造深度学习社区的研究优先级与激励方面一直处于中心位置（Koch & Peterson 2024）。研究发现，基准很少是中立的，而是被其创建环境所塑造——假设、承诺与依赖关系往往对最终结果有重大影响（Aniba et al. 2010; Bartz-Beielstein et al. 2020）。创建一个有意义且可靠的基准极具挑战，已有批判性工作指出了关键的基准期望属性与开放挑战。

**EN** Propensity for overfitting. Static task-based leaderboards, such as Hugging Face’s Open LLM Leaderboard (Fourrier et al. 2024; Gao et al. 2024) and OpenCompass (Contributors 2023), aim to evaluate models across a broad range of skills but are often susceptible to data contamination and implicit overfitting (Deng et al. 2024; Golchin & Surdeanu 2024; Roberts et al. 2023; Dong et al. 2024; Singh et al. 2024a; Longpre et al. 2024a). Prior works (Deng et al. 2024; Golchin & Surdeanu 2024; Yang et al. 2023) have proposed various methods for detecting contamination, while Dong et al. 2024 discusses how such contamination impedes the ability to distinguish true generalization, ultimately hindering progress. Although dynamic, live benchmarks like Chatbot Arena significantly reduce the risk of overfitting, we report in this paper that certain practices—such as multiple submissions during the anonymous testing period and best-of-N submissions—tend to favor large, proprietary players with disproportionate access to data. As a result, model development may be deliberately optimized for performance on Chatbot Arena.

**ZH** 过拟合倾向。Hugging Face 的 Open LLM Leaderboard（Fourrier et al. 2024; Gao et al. 2024）与 OpenCompass（Contributors 2023）等静态任务型排行榜旨在跨广泛技能评测模型，但常常容易受到数据污染与隐性过拟合的影响（Deng et al. 2024; Golchin & Surdeanu 2024; Roberts et al. 2023; Dong et al. 2024; Singh et al. 2024a; Longpre et al. 2024a）。已有工作（Deng et al. 2024; Golchin & Surdeanu 2024; Yang et al. 2023）提出了多种污染检测方法，而 Dong et al. 2024 讨论了此类污染如何阻碍区分真正的泛化，最终阻碍进步。虽然 Chatbot Arena 这类动态的、实时的基准显著降低了过拟合风险，我们在本文中报告指出，某些做法——例如在匿名测试期内多次提交与 best-of-N 提交——往往有利于拥有不成比例数据访问权的大型专有参与者。结果，模型开发可能被刻意针对 Chatbot Arena 的表现做优化。

**EN** Lack of standardization across benchmarks. The lack of standardization in benchmarks complicates meaningful comparisons due to inconsistent metrics and task definitions. Ethayarajh & Jurafsky 2020 critique NLP leaderboards for prioritizing accuracy over dimensions like model compactness and fairness. Similarly, Ruder 2021 highlights that benchmarks such as SuperGLUE (Sarlin et al. 2020) are quickly saturated, with models reaching superhuman performance while still failing in real-world scenarios, underscoring the need for dynamic and standardized evaluation. This inconsistency risks misleading practitioners, as echoed in recent critiques (Bartz-Beielstein et al. 2020; Reuel et al. 2024).

**ZH** 跨基准缺乏标准化。基准缺乏标准化使有意义的比较变得复杂，原因是度量与任务定义不一致。Ethayarajh & Jurafsky 2020 批评 NLP 排行榜把准确率置于模型紧凑性与公平性等维度之上。类似地，Ruder 2021 指出 SuperGLUE（Sarlin et al. 2020）等基准很快饱和，模型达到超人性能却在真实场景中仍然失败，凸显了对动态与标准化评测的需求。这种不一致有可能误导实践者，近期批评（Bartz-Beielstein et al. 2020; Reuel et al. 2024）也呼应了这一点。

**EN** Quality of data and limited reproducibility. A recent study by Vendrow et al. 2025 revealed widespread label errors that compromise evaluation reliability, showing that even frontier LLMs can struggle with seemingly simple tasks. Similarly, Digan et al. 2021 identified reproducibility challenges arising from complex data streams, which affect result consistency. Related work (Bartz-Beielstein et al. 2020; Longpre et al. 2023; Reuel et al. 2024; Albalak et al. 2024) further emphasizes that poor data quality and limited reproducibility can lead to unreliable evaluations and undermine scientific credibility.

**ZH** 数据质量与可复现性有限。Vendrow et al. 2025 的一项近期研究揭示了普遍存在的标签错误损害评测可靠性，表明即便是最前沿的 LLM 也可能在看似简单的任务上表现不佳。类似地，Digan et al. 2021 指出了由复杂数据流带来的可复现性挑战，影响结果的一致性。相关工作（Bartz-Beielstein et al. 2020; Longpre et al. 2023; Reuel et al. 2024; Albalak et al. 2024）进一步强调，糟糕的数据质量与有限的可复现性会导致评测不可靠，并损害科学可信度。

**EN** Favored benchmarks may not capture performance in the real world. Commonly used benchmarks often fail to capture real-world performance, creating a gap between test scores and practical utility due to their tendency to overlook the dynamic and complex nature of real-world tasks. Recent studies (Ott et al. 2022; Parli 2022) highlight this disconnect, observing that models frequently excel on benchmarks while underperforming in practical applications, especially as benchmarks quickly reach saturation.

**ZH** 受偏爱的基准可能无法捕捉真实世界的性能。常用基准往往无法捕捉真实世界的表现，由于其倾向于忽视真实世界任务的动态性与复杂性，造成测试分数与实际效用之间的鸿沟。近期研究（Ott et al. 2022; Parli 2022）强调了这一脱节，观察到模型常常在基准上表现出色，却在真实应用中表现不佳，尤其当基准很快达到饱和时。

**EN** 8.2 Human Voting-based Benchmarks

**ZH** 8.2 基于人类投票的基准

**EN** Wider studies on the role and benefits of human voting-based benchmarks. Chatbot Arena is an example of a human voting-based benchmark. Human judgment has long been regarded as the gold standard for evaluating the quality of model-generated outputs. These models should ultimately align with human values, and certain nuanced qualities, such as coherence, harmlessness, and readability, are best assessed by humans (Van Der Lee et al. 2019; Boubdir et al. 2023). Platforms like Chatbot Arena (Chiang et al. 2024), Talk Arena (Li et al. 2024a), and Game Arena (Hu et al. 2024), Aya UI Interface (Singh et al. 2024c) effectively use crowdsourcing to gather large volumes of real-world user prompts and feedback. Many opt for Elo-like or BT-style rankings to rank models. Moreover, collecting human preference data has also proven invaluable for alignment techniques like Reinforcement Learning from Human Feedback (RLHF) (Christiano et al. 2017; Ouyang et al. 2022; Ahmadian et al. 2024; Dang et al. 2024a), which helps fine-tune models to generate more natural and human-preferred responses. Human voting has been shown to mitigate some of the biases associated with using LLM-as-a-judge approaches, which, while improving evaluation efficiency, may raise concerns about robustness (Raina et al. 2024) and introduce various forms of bias (Koo et al. 2023; Shimabucoro et al. 2023; Chen et al. 2024; Zheng et al. 2024). Furthermore, live leaderboards offer several advantages over static task benchmarks, including a lower risk of data contamination and greater adaptability to evolving evaluation needs.

**ZH** 关于基于人类投票的基准之作用与价值的更广泛研究。Chatbot Arena 是基于人类投票的基准的一个实例。人类判断长期以来被视为评价模型生成输出质量的金标准。这些模型最终应当与人类价值观一致，而某些细微品质——如连贯性、无害性与可读性——最好由人类评估（Van Der Lee et al. 2019; Boubdir et al. 2023）。Chatbot Arena（Chiang et al. 2024）、Talk Arena（Li et al. 2024a）、Game Arena（Hu et al. 2024）与 Aya UI Interface（Singh et al. 2024c）等平台有效地利用众包收集大量真实世界的用户提示与反馈。许多平台选择类 Elo 或 BT 式的排名来对模型排序。此外，收集人类偏好数据也被证明对 RLHF（Christiano et al. 2017; Ouyang et al. 2022; Ahmadian et al. 2024; Dang et al. 2024a）等对齐技术极有价值，有助于微调模型以生成更自然、更符合人类偏好的回复。人类投票已被证明能缓解使用「LLM 即裁判」方法所带来的某些偏见——后者虽提升了评测效率，却可能引发对稳健性的担忧（Raina et al. 2024）并引入各种形式的偏见（Koo et al. 2023; Shimabucoro et al. 2023; Chen et al. 2024; Zheng et al. 2024）。此外，实时排行榜相较静态任务基准有若干优势，包括更低的数据污染风险与对演化评测需求更强的适应性。

**EN** Critiques of Human-Voting Based Benchmarks. Voting-based live benchmarks like Chatbot Arena also face evaluation challenges not addressed in this paper. Chatbot Arena (Chiang et al. 2024) has made substantial efforts to ensure reliability and security, including malicious user detection, bot protection via Google reCAPTCHA v3, vote limits per IP address, prompt de-duplication, and other safeguards6. Nonetheless, recent work has focused on auditing the reliability of human-voting-based live leaderboards. For instance, studies have demonstrated that such leaderboards are vulnerable to low-cost manipulation, with adversarial users able to de-anonymize model responses and carry out targeted voting attacks (Huang et al. 2025). Additionally, Zhao et al. 2024; Min et al. 2025 suggest that Chatbot Arena rankings can be artificially inflated through various adversarial voting strategies. These vulnerabilities raise concerns about the overall trustworthiness of Chatbot Arena. While our study does not explicitly investigate adversarial voting, we note that Chatbot Arena ’s policy of informing model providers when testing begins and disclosing model aliases may create conditions conducive to leaderboard manipulation.

**ZH** 对基于人类投票的基准的批评。Chatbot Arena 这类基于投票的实时基准还面临本文未涉及的评测挑战。Chatbot Arena（Chiang et al. 2024）在保障可靠性与安全性方面做了大量工作，包括恶意用户检测、通过 Google reCAPTCHA v3 的机器人防护、按 IP 地址的投票限制、提示去重以及其他防护措施6。尽管如此，近期工作聚焦于审计基于人类投票的实时排行榜的可靠性。例如，有研究表明这类排行榜易受低成本操纵，对抗性用户能够去匿名化模型回复并实施定向投票攻击（Huang et al. 2025）。此外，Zhao et al. 2024; Min et al. 2025 指出，Chatbot Arena 的排名可以通过各种对抗性投票策略被人为抬高。这些漏洞引发了对 Chatbot Arena 整体可信度的担忧。虽然本研究没有专门考察对抗性投票，但我们指出，Chatbot Arena 在测试开始时告知模型提供方、并披露模型别名的政策，可能创造出有利于排行榜操纵的条件。

**EN** 9 Conclusion

**ZH** 9 结论

**EN** It is far easier to point out issues with the Arena than the huge amount of work that went into building it. While our work is motivated by the need to maintain scientific integrity in AI progress, we believe it is important to note the huge amount of work involved for a small group of organizers to build a hugely popular community benchmark. Their efforts have democratized access to many models and enabled a large and varied user base to weigh in on what matters in the real world for model selection. Hence, while we point out systematic issues with Chatbot Arena as it is now, we also acknowledge that many of these issues may have gradually emerged as the leaderboard took on outsized importance in visibility to providers.

**ZH** 指出 Arena 存在的问题，远比建设它所投入的巨大工作量要容易得多。虽然我们的工作出于维护 AI 进步中科学诚信的需要，我们认为有必要指出：由一小群组织者建立起一个极受欢迎的社区基准，其中蕴含着巨大的工作量。他们的努力使许多模型的获取变得民主化，并让庞大而多元的用户群得以对「在现实世界中模型选择究竟什么重要」发表意见。因此，尽管我们指出了 Chatbot Arena 现状中的系统性问题，我们也承认，其中许多问题可能是逐步产生的——随着排行榜在对提供方的可见度上获得了过大的重要性。

**EN** This work demonstrates the difficulty in maintaining fair evaluations, despite best intentions. We show that coordination among a handful of providers and preferential policies from Chatbot Arena towards the same small group have jeopardized scientific integrity and reliable Arena rankings. The widespread and apparent willful participation in the gamification of arena scores from a handful of top-tier industry labs is undoubtedly a new low for the AI research field. As scientists, we must do better. As a community, we must demand better.

**ZH** 本工作表明，即便出于最好的意图，维持公平的评测也是困难的。我们表明，少数提供方之间的协同，加上 Chatbot Arena 对同一小团体的倾斜性政策，已经损害了科学诚信与 Arena 排名的可靠性。来自少数顶级产业实验室对 arena 分数的广泛且明显的刻意参与式博弈，无疑是 AI 研究领域的一个新低。作为科学家，我们必须做得更好。作为一个共同体，我们必须要求更好。

**EN** We believe it is very feasible for the organizers of Chatbot Arena to continue to innovate and restore trust by revising their policies. We propose a series of very straightforward recommendations to help reinforce the reliability and fairness of the leaderboard. Most urgently, providers should not be allowed to choose which scores are made public. There should be strict and transparent limits to the number of private variants per provider. Providers, whether from academic or industry labs, should be aware of private testing and the limits should be the same across providers. There should be transparent criteria for model removal from the arena and fairer sampling that is motivated by reducing uncertainty in rankings instead of being skewed towards giving proprietary models more battles. We believe the implementation of these recommendations is critical for addressing ranking distortions, but also necessary in the long term to ensure the benefits from participating on the leaderboard are not concentrated in a handful of providers.

**ZH** 我们相信，Chatbot Arena 的组织者完全有可能继续创新并通过修订政策来重建信任。我们提出一系列非常直截了当的建议，以帮助强化排行榜的可靠性与公平性。最紧迫的是，不应允许提供方选择哪些分数被公开。每个提供方的私有变体数量应当有严格且透明的上限。提供方——无论来自学术实验室还是产业实验室——都应当知晓私有测试，且各提供方的上限应当一致。模型从 arena 中移除应当有透明的标准，采样也应当更公平，其动机应是降低排名中的不确定性，而不是偏向给专有模型更多对战。我们认为，落实这些建议对于纠正排名失真至关重要，并且从长远看也是必要的，以确保参与排行榜的收益不会集中在少数提供方手中。

**EN** 10 Acknowledgements

**ZH** 10 致谢

**EN** We thank our colleagues who have supported various aspects of this project: Madeline Smith, Brittwanya Prince, Thomas Euyang, and Shubham Shukla.

**ZH** 我们感谢在各方面支持本项目的同事：Madeline Smith、Brittwanya Prince、Thomas Euyang 与 Shubham Shukla。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] Aakanksha et al. (2024) Aakanksha, Arash Ahmadian, Beyza Ermis, Seraphina Goldfarb-Tarrant, Julia Kreutzer, Marzieh Fadaee, and Sara Hooker. The multilingual alignment prism: Aligning global and local -->

<!-- [原子块 · verbatim] Adelani et al. (2025) David Ifeoluwa Adelani, Jessica Ojo, Israel Abebe Azime, Jian Yun Zhuang, Jesujoba O. Alabi, Xuanli He, Millicent Ochieng, Sara Hooker, Andiswa Bukula, En-Shiun Annie Lee, Chiama -->

<!-- [原子块 · verbatim] Ahmadian et al. (2024) Arash Ahmadian, Chris Cremer, Matthias Gallé, Marzieh Fadaee, Julia Kreutzer, Olivier Pietquin, Ahmet Üstün, and Sara Hooker. Back to basics: Revisiting REINFORCE-style optimiza -->

<!-- [原子块 · verbatim] Albalak et al. (2024) Alon Albalak, Yanai Elazar, Sang Michael Xie, Shayne Longpre, Nathan Lambert, Xinyi Wang, Niklas Muennighoff, Bairu Hou, Liangming Pan, Haewon Jeong, Colin Raffel, Shiyu Chang, T -->

<!-- [原子块 · verbatim] Aniba et al. (2010) Mohamed Radhouene Aniba, Olivier Poch, and Julie D Thompson. Issues in bioinformatics benchmarking: the case study of multiple sequence alignment. Nucleic acids research , 38(21):7 -->

<!-- [原子块 · verbatim] Arnold et al. (1992) Barry C. Arnold, N. Balakrishnan, and H. N. Nagaraja. A First Course in Order Statistics . Wiley, Hoboken, NJ, 1992. -->

<!-- [原子块 · verbatim] Bartz-Beielstein et al. (2020) Thomas Bartz-Beielstein, Carola Doerr, Daan van den Berg, Jakob Bossek, Sowmya Chandrasekaran, Tome Eftimov, Andreas Fischbach, Pascal Kerschke, William La Cava, Manuel  -->

<!-- [原子块 · verbatim] Boubdir et al. (2023) Meriem Boubdir, Edward Kim, Beyza Ermis, Marzieh Fadaee, and Sara Hooker. Which prompts make the difference? data prioritization for efficient human llm evaluation, 2023. URL htt -->

<!-- [原子块 · verbatim] Boubdir et al. (2024) Meriem Boubdir, Edward Kim, Beyza Ermis, Sara Hooker, and Marzieh Fadaee. Elo uncovered: Robustness and best practices in language model evaluation. Advances in Neural Informatio -->

<!-- [原子块 · verbatim] Bowman & Dahl (2021) Samuel R. Bowman and George Dahl. What will it take to fix benchmarking in natural language understanding? In Kristina Toutanova, Anna Rumshisky, Luke Zettlemoyer, Dilek Hakkani-T -->

<!-- [原子块 · verbatim] Bradley & Terry (1952) Ralph Allan Bradley and Milton E. Terry. Rank analysis of incomplete block designs: I. the method of paired comparisons. Biometrika , 39(3/4):324–345, 1952. ISSN 00063444, 14643 -->

<!-- [原子块 · verbatim] Casella & Berger (2002) George Casella and Roger L. Berger. Statistical Inference . Duxbury Press, 2 edition, 2002. -->

<!-- [原子块 · verbatim] Chen et al. (2024) Guiming Hardy Chen, Shunian Chen, Ziche Liu, Feng Jiang, and Benyou Wang. Humans or LLMs as the judge? a study on judgement bias. In Yaser Al-Onaizan, Mohit Bansal, and Yun-Nung Che -->

<!-- [原子块 · verbatim] Chiang et al. (2024) Wei-Lin Chiang, Lianmin Zheng, Ying Sheng, Anastasios N. Angelopoulos, Tianle Li, Dacheng Li, Banghua Zhu, Hao Zhang, Michael I. Jordan, Joseph E. Gonzalez, and Ion Stoica. Chatbo -->

<!-- [原子块 · verbatim] Christiano et al. (2017) Paul F Christiano, Jan Leike, Tom Brown, Miljan Martic, Shane Legg, and Dario Amodei. Deep reinforcement learning from human preferences. Advances in neural information proces -->

<!-- [原子块 · verbatim] Church (2018) Kenneth Ward Church. Emerging trends: A tribute to charles wayne. Natural Language Engineering , 24(1):155–160, 2018. 10.1017/S1351324917000389 . -->

<!-- [原子块 · verbatim] Cohere (2024) Cohere. Command r and command r+ model card, 2024. URL https://docs.cohere.com/docs/responsible-use . -->

<!-- [原子块 · verbatim] Cohere (2025) Cohere. A deepdive into aya vision: Advancing the frontier of multilingual multimodality, 2025. URL https://huggingface.co/blog/aya-vision . -->

<!-- [原子块 · verbatim] Cohere et al. (2025) Team Cohere, Aakanksha, Arash Ahmadian, Marwan Ahmed, Jay Alammar, Yazeed Alnumay, Sophia Althammer, Arkady Arkhangorodsky, Viraat Aryabumi, Dennis Aumiller, Raphaël Avalos, Zahar -->

<!-- [原子块 · verbatim] Contributors (2023) OpenCompass Contributors. Opencompass: A universal evaluation platform for foundation models. https://github.com/open-compass/opencompass , 2023. -->

<!-- [原子块 · verbatim] Dang et al. (2024a) John Dang, Arash Ahmadian, Kelly Marchisio, Julia Kreutzer, Ahmet Üstün, and Sara Hooker. RLHF can speak many languages: Unlocking multilingual preference optimization for LLMs. In -->

<!-- [原子块 · verbatim] Dang et al. (2024b) John Dang, Shivalika Singh, Daniel D’souza, Arash Ahmadian, Alejandro Salamanca, Madeline Smith, Aidan Peppin, Sungjin Hong, Manoj Govindassamy, Terrence Zhao, Sandra Kublik, Meor  -->

<!-- [原子块 · verbatim] David & Nagaraja (2003) Herbert A. David and H. N. Nagaraja. Order Statistics . Wiley, Hoboken, NJ, 3 edition, 2003. -->

<!-- [原子块 · verbatim] Deng et al. (2024) Chunyuan Deng, Yilun Zhao, Xiangru Tang, Mark Gerstein, and Arman Cohan. Investigating data contamination in modern benchmarks for large language models. In Kevin Duh, Helena Gomez, -->

<!-- [原子块 · verbatim] Deng et al. (2009) Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li, and Li Fei-Fei. Imagenet: A large-scale hierarchical image database. In 2009 IEEE Conference on Computer Vision and Pattern Re -->

<!-- [原子块 · verbatim] Digan et al. (2021) William Digan, Aurélie Névéol, Antoine Neuraz, Maxime Wack, David Baudoin, Anita Burgun, and Bastien Rance. Can reproducibility be improved in clinical natural language processing? -->

<!-- [原子块 · verbatim] Don-Yehiya et al. (2024) Shachar Don-Yehiya, Ben Burtenshaw, Ramon Fernandez Astudillo, Cailean Osborne, Mimansa Jaiswal, Tzu-Sheng Kuo, Wenting Zhao, Idan Shenfeld, Andi Peng, Mikhail Yurochkin, Atoo -->

<!-- [原子块 · verbatim] Dong et al. (2024) Yihong Dong, Xue Jiang, Huanyu Liu, Zhi Jin, Bin Gu, Mengfei Yang, and Ge Li. Generalization or memorization: Data contamination and trustworthy evaluation for large language models -->

<!-- [原子块 · verbatim] Dubois et al. (2023) Yann Dubois, Chen Xuechen Li, Rohan Taori, Tianyi Zhang, Ishaan Gulrajani, Jimmy Ba, Carlos Guestrin, Percy S Liang, and Tatsunori B Hashimoto. Alpacafarm: A simulation framework  -->

<!-- [原子块 · verbatim] Elo (1978) Arpad E. Elo. The Rating of Chessplayers, Past and Present . Arco Pub., New York, 1978. ISBN 0668047216 9780668047210. URL http://www.amazon.com/Rating-Chess-Players-Past-Present/dp/0668047 -->

<!-- [原子块 · verbatim] Ensmenger (2011) Nathan Ensmenger. Is chess the drosophila of artificial intelligence? a social history of an algorithm. Social Studies of Science , 42(1):5–30, Oct 2011. https://doi.org/10.1177/03063 -->

<!-- [原子块 · verbatim] Ethayarajh & Jurafsky (2020) Kawin Ethayarajh and Dan Jurafsky. Utility is in the eye of the user: A critique of NLP leaderboards. In Bonnie Webber, Trevor Cohn, Yulan He, and Yang Liu (eds.), Proceed -->

<!-- [原子块 · verbatim] Ford Jr (1957) Lester R Ford Jr. Solution of a ranking problem from binary comparisons. The American Mathematical Monthly , 64(8P2):28–33, 1957. -->

<!-- [原子块 · verbatim] Fourrier et al. (2024) Clémentine Fourrier, Nathan Habib, Alina Lozovskaya, Konrad Szafer, and Thomas Wolf. Open llm leaderboard v2. https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderb -->

<!-- [原子块 · verbatim] Frick et al. (2025) Evan Frick, Connor Chen, Joseph Tennyson, Tianle Li, Wei-Lin Chiang, Anastasios N. Angelopoulos, and Ion Stoica. Prompt-to-leaderboard, 2025. URL https://arxiv.org/abs/2502.14855 . -->

<!-- [原子块 · verbatim] Gao et al. (2024) Leo Gao, Jonathan Tow, Baber Abbasi, Stella Biderman, Sid Black, Anthony DiPofi, Charles Foster, Laurence Golding, Jeffrey Hsu, Alain Le Noac’h, Haonan Li, Kyle McDonell, Niklas Muen -->

<!-- [原子块 · verbatim] Glickman (1999) Mark E Glickman. Parameter estimation in large dynamic paired comparison experiments. Applied Statistics , pp. 377–394, 1999. -->

<!-- [原子块 · verbatim] Golchin & Surdeanu (2024) Shahriar Golchin and Mihai Surdeanu. Time travel in LLMs: Tracing data contamination in large language models. In The Twelfth International Conference on Learning Representat -->

<!-- [原子块 · verbatim] Google (2025) Google. Introducing gemma 3: The most capable model you can run on a single gpu or tpu, 2025. URL https://blog.google/technology/developers/gemma-3/ . Accessed: 2025-04-09. -->

<!-- [原子块 · verbatim] Grattafiori et al. (2024) Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Alex Vaughan, et al. The llam -->

<!-- [原子块 · verbatim] Harman (1993) Donna Harman. Overview of the first trec conference. In Proceedings of the 16th annual international ACM SIGIR conference on Research and development in information retrieval , pp. 36–47 -->

<!-- [原子块 · verbatim] Hendrycks et al. (2021) Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, and Jacob Steinhardt. Measuring massive multitask language understanding. Proceedings of the In -->

<!-- [原子块 · verbatim] Hoffmann et al. (2022) Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, et al. -->

<!-- [原子块 · verbatim] Hooker (2024) Sara Hooker. On the limitations of compute thresholds as a governance strategy, 2024. URL https://arxiv.org/abs/2407.05694 . -->

<!-- [原子块 · verbatim] Hu et al. (2024) Lanxiang Hu, Qiyu Li, Anze Xie, Nan Jiang, Ion Stoica, Haojian Jin, and Hao Zhang. Gamearena: Evaluating llm reasoning through live computer games. ArXiv , abs/2412.06394, 2024. URL h -->

<!-- [原子块 · verbatim] Huang et al. (2025) Yangsibo Huang, Milad Nasr, Anastasios Angelopoulos, Nicholas Carlini, Wei-Lin Chiang, Christopher A Choquette-Choo, Daphne Ippolito, Matthew Jagielski, Katherine Lee, Ken Ziyu Liu -->

<!-- [原子块 · verbatim] Hunter (2004a) David R. Hunter. Mm algorithms for generalized bradley–terry models. The Annals of Statistics , 32(1):384–406, 2004a. 10.1214/aos/1079120130 . -->

<!-- [原子块 · verbatim] Hunter (2004b) David R Hunter. Mm algorithms for generalized bradley-terry models. The annals of statistics , 32(1):384–406, 2004b. -->

<!-- [原子块 · verbatim] Kaplan et al. (2020) Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, and Dario Amodei. Scaling laws for neural language mode -->

<!-- [原子块 · verbatim] Kim et al. (2023) Seungone Kim, Jamin Shin, Yejin Cho, Joel Jang, Shayne Longpre, Hwaran Lee, Sangdoo Yun, Seongjin Shin, Sungdong Kim, James Thorne, et al. Prometheus: Inducing fine-grained evaluatio -->

<!-- [原子块 · verbatim] Koch & Peterson (2024) Bernard J Koch and David Peterson. From protoscience to epistemic monoculture: How benchmarking set the stage for the deep learning revolution. arXiv preprint arXiv:2404.06647 , -->

<!-- [原子块 · verbatim] Koehn & Monz (2006) Philipp Koehn and Christof Monz. Manual and automatic evaluation of machine translation between european languages. In Proceedings on the Workshop on Statistical Machine Translatio -->

<!-- [原子块 · verbatim] Koo et al. (2023) Ryan Koo, Minhwa Lee, Vipul Raheja, Jong Inn Park, Zae Myung Kim, and Dongyeop Kang. Benchmarking cognitive biases in large language models as evaluators. arXiv preprint arXiv:2309.1 -->

<!-- [原子块 · verbatim] Leitner et al. (2010) Christoph Leitner, Achim Zeileis, and Kurt Hornik. Forecasting sports tournaments by ratings of (prob) abilities: A comparison for the euro 2008. International Journal of Forecas -->

<!-- [原子块 · verbatim] Li et al. (2024a) Minzhi Li, Will Held, Michael J. Ryan, Kunat Pipatanakul, Potsawee Manakul, Hao Zhu, and Diyi Yang. Talk arena: Interactive evaluation of large audio models, 2024a. -->

<!-- [原子块 · verbatim] Li et al. (2024b) Tianle Li, Wei-Lin Chiang, Evan Frick, Lisa Dunlap, Tianhao Wu, Banghua Zhu, Joseph E. Gonzalez, and Ion Stoica. From crowdsourced data to high-quality benchmarks: Arena-hard and ben -->

<!-- [原子块 · verbatim] Li et al. (2024c) Tianle Li, Wei-Lin Chiang, Evan Frick, Lisa Dunlap, Tianhao Wu, Banghua Zhu, Joseph E Gonzalez, and Ion Stoica. From crowdsourced data to high-quality benchmarks: Arena-hard and benc -->

<!-- [原子块 · verbatim] Liang et al. (2022) Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan, Yuhuai Wu, Ananya Kumar, Benjamin Newman, Binhang Yuan, Bo -->

<!-- [原子块 · verbatim] Liquipedia (2019) Liquipedia. Elo rating, 2019. URL https://liquipedia.net/starcraft/Elo_rating . Accessed: 2025-04-09. -->

<!-- [原子块 · verbatim] Longpre et al. (2023) Shayne Longpre, Robert Mahari, Anthony Chen, Naana Obeng-Marnu, Damien Sileo, William Brannon, Niklas Muennighoff, Nathan Khazam, Jad Kabbara, Kartik Perisetla, et al. The data p -->

<!-- [原子块 · verbatim] Longpre et al. (2024a) Shayne Longpre, Stella Biderman, Alon Albalak, Hailey Schoelkopf, Daniel McDuff, Sayash Kapoor, Kevin Klyman, Kyle Lo, Gabriel Ilharco, Nay San, Maribeth Rauh, Aviya Skowron, Be -->

<!-- [原子块 · verbatim] Longpre et al. (2024b) Shayne Longpre, Robert Mahari, Ariel Lee, Campbell Lund, Hamidah Oderinwale, William Brannon, Nayan Saxena, Naana Obeng-Marnu, Tobin South, Cole Hunter, et al. Consent in crisis -->

<!-- [原子块 · verbatim] Longpre et al. (2024c) Shayne Longpre, Nikhil Singh, Manuel Cherep, Kushagra Tiwary, Joanna Materzynska, William Brannon, Robert Mahari, Naana Obeng-Marnu, Manan Dey, Mohammed Hamdy, et al. Bridging t -->

<!-- [原子块 · verbatim] Longpre et al. (2024d) Shayne Longpre, Gregory Yauney, Emily Reif, Katherine Lee, Adam Roberts, Barret Zoph, Denny Zhou, Jason Wei, Kevin Robinson, David Mimno, et al. A pretrainer’s guide to training -->

<!-- [原子块 · verbatim] Luu et al. (2021) Kelvin Luu, Daniel Khashabi, Suchin Gururangan, Karishma Mandyam, and Noah A Smith. Time waits for no one! analysis and challenges of temporal misalignment. arXiv preprint arXiv:2111 -->

<!-- [原子块 · verbatim] Maslej et al. (2025) Nestor Maslej, Loredana Fattorini, Elif Kiesow Cortez, Julia Betts Lotufo, Anka Reuel, Alexandra Rome, Angelo Salatino, Lapo Santarlasci, Emily Capstick, Malou van Draanen Glisman -->

<!-- [原子块 · verbatim] Meta (2025) Meta. The llama 4 herd: The beginning of a new era of natively multimodal ai innovation, 2025. URL https://ai.meta.com/blog/llama-4-multimodal-intelligence . -->

<!-- [原子块 · verbatim] Min et al. (2025) Rui Min, Tianyu Pang, Chao Du, Qian Liu, Minhao Cheng, and Min Lin. Improving your model ranking on chatbot arena by vote rigging. arXiv preprint arXiv:2501.17858 , 2025. -->

<!-- [原子块 · verbatim] Mizrahi et al. (2024) Moran Mizrahi, Guy Kaplan, Dan Malkin, Rotem Dror, Dafna Shahaf, and Gabriel Stanovsky. State of what art? a call for multi-prompt llm evaluation, 2024. URL https://arxiv.org/abs -->

<!-- [原子块 · verbatim] Odumakinde et al. (2024) Ayomide Odumakinde, Daniel D’souza, Pat Verga, Beyza Ermis, and Sara Hooker. Multilingual arbitrage: Optimizing data pools to accelerate multilingual progress, 2024. URL https -->

<!-- [原子块 · verbatim] Orr & Kang (2024) Will Orr and Edward B Kang. Ai as a sport: On the competitive epistemologies of benchmarking. In Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency  -->

<!-- [原子块 · verbatim] Ott et al. (2022) Simon Ott, Adriano Barbosa-Silva, Kathrin Blagec, Jan Brauner, and Matthias Samwald. Mapping global dynamics of benchmark creation and saturation in artificial intelligence. Nature C -->

<!-- [原子块 · verbatim] Ouyang et al. (2022) Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. Training language models to f -->

<!-- [原子块 · verbatim] Parli (2022) Vanessa Parli. Ai benchmarks hit saturation, 2022. URL https://hai.stanford.edu/news/ai-benchmarks-hit-saturation . -->

<!-- [原子块 · verbatim] Rafailov et al. (2023) Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and Chelsea Finn. Direct preference optimization: Your language model is secretly a reward m -->

<!-- [原子块 · verbatim] Raina et al. (2024) Vyas Raina, Adian Liusie, and Mark Gales. Is llm-as-a-judge robust? investigating universal adversarial attacks on zero-shot llm assessment. arXiv preprint arXiv:2402.14016 , 2024. -->

<!-- [原子块 · verbatim] Raji et al. (2021) Inioluwa Deborah Raji, Emily M. Bender, Amandalynne Paullada, Emily Denton, and Alex Hanna. AI and the everything in the whole wide world benchmark. CoRR , abs/2111.15366, 2021. URL -->

<!-- [原子块 · verbatim] Reuel et al. (2024) Anka Reuel, Amelia Hardy, Chandler Smith, Max Lamparth, Malcolm Hardy, and Mykel J Kochenderfer. Betterbench: Assessing ai benchmarks, uncovering issues, and establishing best prac -->

<!-- [原子块 · verbatim] Roberts et al. (2023) Manley Roberts, Himanshu Thakur, Christine Herlihy, Colin White, and Samuel Dooley. To the cutoff… and beyond? a longitudinal perspective on llm data contamination. In The Twelft -->

<!-- [原子块 · verbatim] Rodriguez et al. (2021) Pedro Rodriguez, Joe Barrow, Alexander Miserlis Hoyle, John P. Lalor, Robin Jia, and Jordan Boyd-Graber. Evaluation examples are not equally informative: How should that change -->

<!-- [原子块 · verbatim] Romanou et al. (2024) Angelika Romanou, Negar Foroutan, Anna Sotnikova, Zeming Chen, Sree Harsha Nelaturu, Shivalika Singh, Rishabh Maheshwary, Micol Altomare, Mohamed A Haggag, Alfonso Amayuelas, et  -->

<!-- [原子块 · verbatim] Ruder (2021) Sebastian Ruder. Challenges and opportunities in nlp benchmarking, August 2021. URL https://www.ruder.io/nlp-benchmarking/ . Accessed: 2025-04-08. -->

<!-- [原子块 · verbatim] Salazar et al. (2025) Israfel Salazar, Manuel Fernández Burda, Shayekh Bin Islam, Arshia Soltani Moakhar, Shivalika Singh, Fabian Farestam, Angelika Romanou, Danylo Boiko, Dipika Khullar, Mike Zhang,  -->

<!-- [原子块 · verbatim] Sambasivan et al. (2021) Nithya Sambasivan, Shivani Kapania, Hannah Highfill, Diana Akrong, Praveen Paritosh, and Lora M Aroyo. “everyone wants to do the model work, not the data work”: Data cascades  -->

<!-- [原子块 · verbatim] Samsi et al. (2023) Siddharth Samsi, Dan Zhao, Joseph McDonald, Baolin Li, Adam Michaleas, Michael Jones, William Bergeron, Jeremy Kepner, Devesh Tiwari, and Vijay Gadepally. From words to watts: Benc -->

<!-- [原子块 · verbatim] Sarlin et al. (2020) Paul-Edouard Sarlin, Daniel DeTone, Tomasz Malisiewicz, and Andrew Rabinovich. Superglue: Learning feature matching with graph neural networks. In Proceedings of the IEEE/CVF conf -->

<!-- [原子块 · verbatim] Shimabucoro et al. (2023) Luísa Shimabucoro, Timothy Hospedales, and Henry Gouk. Evaluating the evaluators: Are current few-shot learning benchmarks fit for purpose? arXiv preprint arXiv:2307.02732 ,  -->

<!-- [原子块 · verbatim] Shimabucoro et al. (2024) Luísa Shimabucoro, Sebastian Ruder, Julia Kreutzer, Marzieh Fadaee, and Sara Hooker. LLM see, LLM do: Leveraging active inheritance to target non-differentiable objectives. I -->

<!-- [原子块 · verbatim] Singh et al. (2024a) Aaditya K. Singh, Muhammed Yusuf Kocyigit, Andrew Poulton, David Esiobu, Maria Lomeli, Gergely Szilvasy, and Dieuwke Hupkes. Evaluation data contamination in llms: how do we measu -->

<!-- [原子块 · verbatim] Singh et al. (2024b) Shivalika Singh, Angelika Romanou, Clémentine Fourrier, David I Adelani, Jian Gang Ngui, Daniel Vila-Suero, Peerat Limkonchotiwat, Kelly Marchisio, Wei Qi Leong, Yosephine Susanto -->

<!-- [原子块 · verbatim] Singh et al. (2024c) Shivalika Singh, Freddie Vargus, Daniel D’souza, Börje Karlsson, Abinaya Mahendiran, Wei-Yin Ko, Herumb Shandilya, Jay Patel, Deividas Mataciunas, Laura O’Mahony, Mike Zhang, Rami -->

<!-- [原子块 · verbatim] Tang et al. (2025) Kelly Tang, Wei-Lin Chiang, and Anastasios N. Angelopoulos. Arena explorer: A topic modeling pipeline for llm evals & analytics, 2025. -->

<!-- [原子块 · verbatim] Team et al. (2025) Gemma Team, Aishwarya Kamath, Johan Ferret, Shreya Pathak, Nino Vieillard, Ramona Merhej, Sarah Perrin, Tatiana Matejovicova, Alexandre Ramé, Morgane Rivière, Louis Rouillard, Thoma -->

<!-- [原子块 · verbatim] Thomas & Uminsky (2020) Rachel Thomas and David Uminsky. The problem with metrics is a fundamental problem for ai, 2020. URL https://arxiv.org/abs/2002.08512 . -->

<!-- [原子块 · verbatim] Üstün et al. (2024) Ahmet Üstün, Viraat Aryabumi, Zheng Yong, Wei-Yin Ko, Daniel D’souza, Gbemileke Onilude, Neel Bhandari, Shivalika Singh, Hui-Lee Ooi, Amr Kayid, Freddie Vargus, Phil Blunsom, Shayn -->

<!-- [原子块 · verbatim] Van Der Lee et al. (2019) Chris Van Der Lee, Albert Gatt, Emiel Van Miltenburg, Sander Wubben, and Emiel Krahmer. Best practices for the human evaluation of automatically generated text. In Proceeding -->

<!-- [原子块 · verbatim] Vendrow et al. (2025) Joshua Vendrow, Edward Vendrow, Sara Beery, and Aleksander Madry. Do large language model benchmarks test reliability? arXiv preprint arXiv:2502.03461 , 2025. -->

<!-- [原子块 · verbatim] Wang et al. (2018) Alex Wang, Amanpreet Singh, Julian Michael, Felix Hill, Omer Levy, and Samuel R Bowman. Glue: A multi-task benchmark and analysis platform for natural language understanding. arXiv  -->

<!-- [原子块 · verbatim] Wang et al. (2024) Yubo Wang, Xueguang Ma, Ge Zhang, Yuansheng Ni, Abhranil Chandra, Shiguang Guo, Weiming Ren, Aaran Arulraj, Xuan He, Ziyan Jiang, et al. Mmlu-pro: A more robust and challenging mult -->

<!-- [原子块 · verbatim] Wise (2021) Ben P. Wise. Elo ratings for large tournaments of software agents in asymmetric games. ArXiv , abs/2105.00839, 2021. URL https://api.semanticscholar.org/CorpusID:233481682 . -->

<!-- [原子块 · verbatim] Yang et al. (2024) An Yang, Baosong Yang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Zhou, Chengpeng Li, Chengyuan Li, Dayiheng Liu, Fei Huang, Guanting Dong, Haoran Wei, Huan Lin, Jialong Tang, Jialin Wa -->

<!-- [原子块 · verbatim] Yang et al. (2023) Shuo Yang, Wei-Lin Chiang, Lianmin Zheng, Joseph E Gonzalez, and Ion Stoica. Rethinking benchmark and contamination for language models with rephrased samples. arXiv preprint arXiv: -->

<!-- [原子块 · verbatim] Ying (2019) Xue Ying. An overview of overfitting and its solutions. Journal of Physics: Conference Series , 1168:022022, Feb 2019. https://doi.org/10.1088/1742-6596/1168/2/022022 . URL https://iopscie -->

<!-- [原子块 · verbatim] Zhao et al. (2024) Wenting Zhao, Alexander M. Rush, and Tanya Goyal. Challenges in trustworthy human evaluation of chatbots. ArXiv , abs/2412.04363, 2024. URL https://api.semanticscholar.org/CorpusID: -->

<!-- [原子块 · verbatim] Zheng et al. (2024) Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric Xing, et al. Judging llm-as-a-judge with mt-bench and ch -->

**EN** Appendix A Chatbot Arena Background

**ZH** 附录 A Chatbot Arena 背景

**EN** LMSYS originated from a multi-university collaboration involving UC Berkeley, Stanford, UCSD, CMU, and MBZUAI in 2023. It was established as a non-profit corporation in September 2024 to incubate early-stage open-source and research projects. Chatbot Arena was first launched in May 2023 under LMSYS and later evolved into a standalone project with its own dedicated website2727 27 https://lmsys.org/blog/2024-09-20-arena-new-site/ maintained under the name LMArena by researchers from UC Berkeley SkyLab. It has emerged as a critical platform for live, community-driven LLM evaluation, attracting millions of participants and collecting over 3 million votes to date.

**ZH** LMSYS 源于 2023 年由 UC Berkeley、斯坦福大学、UCSD、CMU 与 MBZUAI 参与的多校合作。它于 2024 年 9 月注册为非营利机构，以孵化早期阶段的开源与研究项目。Chatbot Arena 于 2023 年 5 月在 LMSYS 下首次上线，后来演变为一个拥有自己专门网站的独立项目2727 27 https://lmsys.org/blog/2024-09-20-arena-new-site/，由 UC Berkeley SkyLab 的研究人员以 LMArena 之名维护。它已成为实时、社区驱动的 LLM 评测的关键平台，吸引了数百万参与者，迄今收集了超过 300 万张投票。

**EN** LMArena operates based on human preferences. Chatbot Arena asks users to input prompts in battles. The user then votes for their preferred model based on the outputs generated by the models in the battle in response to the user’s prompts. These preferences are then used by Chatbot Arena to compute model ratings using algorithms like Online Elo and Bradley-Terry.

**ZH** LMArena 基于人类偏好运行。Chatbot Arena 要求用户在对战中输入提示。用户随后依据模型针对其提示生成的输出，投票选出自己更偏好的模型。Chatbot Arena 再用这些偏好，通过 Online Elo 与 Bradley-Terry 等算法计算模型评分。

**EN** Appendix B Bradley-Terry Rating Model

**ZH** 附录 B Bradley-Terry 评分模型

**EN** Consider a set of ⟦SLOT_33⟧ players (models) and ⟦SLOT_34⟧ pairwise comparisons between them. Let ⟦SLOT_35⟧ be the design matrix, where each column represents one pairwise comparison. In the Bradley-Terry model, the probability that player ⟦SLOT_36⟧ is preferred over player ⟦SLOT_37⟧ in a comparison is modeled as:

**ZH** 考虑一组 ⟦SLOT_33⟧ 个参与者（模型）与它们之间的 ⟦SLOT_34⟧ 次成对比较。设 ⟦SLOT_35⟧ 为设计矩阵，其中每一列代表一次成对比较。在 Bradley-Terry 模型中，参与者 ⟦SLOT_36⟧ 在一次比较中被认为优于参与者 ⟦SLOT_37⟧ 的概率建模为：

<!-- [原子块 · table] P ⁡ ( i preferred over j ) = 1 1 + e ( β j − β i ) P(\text{i preferred over j})=\frac{1}{1+e^{(\beta_{j}-\beta_{i})}} -->

**EN** Then, in the matrix ⟦SLOT_38⟧, column vector ⟦SLOT_39⟧ has a value of 1 at position ⟦SLOT_40⟧ , -1 at position ⟦SLOT_41⟧, and 0 elsewhere. Let ⟦SLOT_42⟧ be the vector of observed outcomes, where ⟦SLOT_43⟧ if player ⟦SLOT_44⟧ wins the ⟦SLOT_45⟧-th comparison and ⟦SLOT_46⟧ if player ⟦SLOT_47⟧ wins. Our goal is to estimate the Bradley-Terry coefficients ⟦SLOT_48⟧, which determine the relative strengths of the players. The coefficients ⟦SLOT_49⟧ are estimated via maximum likelihood estimation by minimizing the expected cross-entropy loss,

**ZH** 于是，在矩阵 ⟦SLOT_38⟧ 中，列向量 ⟦SLOT_39⟧ 在位置 ⟦SLOT_40⟧ 处取值为 1，在位置 ⟦SLOT_41⟧ 处取值为 -1，其余为 0。设 ⟦SLOT_42⟧ 为观测结果向量，取值 ⟦SLOT_43⟧ 表示参与者 ⟦SLOT_44⟧ 赢得第 ⟦SLOT_45⟧ 次比较，取值 ⟦SLOT_46⟧ 表示参与者 ⟦SLOT_47⟧ 获胜。我们的目标是估计 Bradley-Terry 系数 ⟦SLOT_48⟧，它们决定了参与者的相对强度。系数 ⟦SLOT_49⟧ 通过极大似然估计、最小化期望交叉熵损失来估计，

<!-- [原子块 · table] β ^ = arg ⁡ min β ∈ ℝ m ​ 1 n ​ ∑ k = 1 n ℓ ⁡ ( σ ​ ( X T ​ β ) k , Y k ) \hat{\beta}=\arg\min_{\beta\in\mathbb{R}^{m}}\frac{1}{n}\sum_{k=1}^{n}\ell\big(\sigma(X^{T}\beta)_{k},Y_{k}\big) -->

**EN** where ⟦SLOT_50⟧ is the logistic function that models the relative player strengths, and ⟦SLOT_51⟧ represents the binary cross-entropy loss between the predicted probabilities and the observed outcomes ⟦SLOT_52⟧. The estimated coefficient ⟦SLOT_53⟧ captures the latent strength of each player.

**ZH** 其中 ⟦SLOT_50⟧ 是建模参与者相对强度的 logistic 函数，⟦SLOT_51⟧ 表示预测概率与观测结果 ⟦SLOT_52⟧ 之间的二元交叉熵损失。估计出的系数 ⟦SLOT_53⟧ 捕捉了每个参与者的潜在强度。

**EN** Once the Bradley-Terry model estimates the coefficients, we can scale them to obtain Elo-like ratings using the transformation:

**ZH** 一旦 Bradley-Terry 模型估计出这些系数，我们就可以通过如下变换把它们缩放为类 Elo 的评分：

<!-- [原子块 · table] R m = scale ∗ β + initial rating R_{m}=\text{scale}*\beta+\text{initial rating} -->

**EN** In practice, Chatbot Arena does not rely solely on a model’s Arena Score for ranking. Instead, it also considers the confidence intervals associated with these scores. When the confidence intervals of two models overlap, it becomes difficult to determine which one is truly better. This uncertainty is reflected in the final ranking table, adding nuance and statistical rigor to the leaderboard (Chiang et al. 2024).

**ZH** 在实践中，Chatbot Arena 并不只依赖模型的 Arena 分数来排名。它还考虑与这些分数相关的置信区间。当两个模型的置信区间重叠时，很难判断哪一个真正更好。这种不确定性会反映在最终排名表中，为排行榜增添了细微差别与统计严谨性（Chiang et al. 2024）。

<!-- [原子块 · table] rank ( m ) = 1 + ∑ m ′ ∈ [ M ] 1 { m ′ > m } \text{rank}(m)=1+\sum_{m^{\prime}\in[M]}1\left\{m^{\prime}>m\right\} -->

**EN** Appendix C Unbiased Sampling: Why Selecting the Maximum Introduces Bias?

**ZH** 附录 C 无偏采样：为何选择最大值会引入偏差？

**EN** Let ⟦SLOT_54⟧ be i.i.d. real-valued random variables with common cumulative distribution function ⟦SLOT_55⟧ and finite expectation ⟦SLOT_56⟧. Assume the distribution is non-degenerate, i.e., ⟦SLOT_57⟧. The maximum is defined as:

**ZH** 设 ⟦SLOT_54⟧ 为独立同分布的实值随机变量，具有共同的累积分布函数 ⟦SLOT_55⟧ 与有限期望 ⟦SLOT_56⟧。假设分布是非退化的，即 ⟦SLOT_57⟧。最大值定义为：

<!-- [原子块 · table] β ^ Best := max ⁡ { β ^ 1 , … , β ^ N } , N ≥ 2 . \hat{\beta}_{\mathrm{Best}}:=\max\{\hat{\beta}_{1},\dots,\hat{\beta}_{N}\},\qquad N\geq 2. -->

**EN** Theorem 1

**ZH** 定理 1

**EN** For every ⟦SLOT_58⟧,

**ZH** 对于每一个 ⟦SLOT_58⟧，

<!-- [原子块 · table] 𝔼 ⁡ [ β ^ Best ] > 𝔼 ⁡ [ β ^ k ] ⇔ Var ⁡ ( β ^ k ) > 0 . \mathbb{E}[\hat{\beta}_{\mathrm{Best}}]>\mathbb{E}[\hat{\beta}_{k}]\iff\operatorname{Var}(\hat{\beta}_{k})>0. -->

**EN** Proof 1

**ZH** 证明 1

**EN** The cumulative distribution function (CDF) of the maximum is

**ZH** 最大值的累积分布函数（CDF）为

<!-- [原子块 · table] F β ^ Best ​ ( x ) = ℙ ⁡ ( β ^ Best ≤ x ) = F ​ ( x ) N . F_{\hat{\beta}_{\mathrm{Best}}}(x)=\mathbb{P}(\hat{\beta}_{\mathrm{Best}}\leq x)=F(x)^{N}. -->

**EN** Using integration by parts, we have:

**ZH** 用分部积分法，我们有：

<!-- [原子块 · table] 𝔼 ⁡ [ β ^ Best ] − 𝔼 ⁡ [ β ^ 1 ] \displaystyle\mathbb{E}[\hat{\beta}_{\mathrm{Best}}]-\mathbb{E}[\hat{\beta}_{1}] = ∫ − ∞ ∞ x ​ d ​ ( F ​ ( x ) N − F ⁡ ( x ) ) \displaystyle=\int_{-\infty}^{\infty}x\, -->

**EN** For all ⟦SLOT_59⟧ such that ⟦SLOT_60⟧, and ⟦SLOT_61⟧, we have ⟦SLOT_62⟧, so the integrand is strictly positive on a set of positive measure (since the distribution is non-degenerate). Thus, the integral – and hence the difference in expectations – is strictly positive.

**ZH** 对所有 ⟦SLOT_59⟧（满足 ⟦SLOT_60⟧ 且 ⟦SLOT_61⟧），我们有 ⟦SLOT_62⟧，因此被积函数在一个正测度集合上严格为正（因为分布是非退化的）。于是该积分——进而期望之差——严格为正。

**EN** If ⟦SLOT_63⟧, then ⟦SLOT_64⟧ is a step function with a single jump (a constant distribution), and ⟦SLOT_65⟧ for all ⟦SLOT_66⟧, yielding equality.

**ZH** 若 ⟦SLOT_63⟧，则 ⟦SLOT_64⟧ 是一个带单次跳跃的阶梯函数（常数分布），且 ⟦SLOT_65⟧ 对所有 ⟦SLOT_66⟧ 成立，从而取等号。

**EN** Remark 1

**ZH** 注记 1

**EN** This result formalizes the selection bias arising when one reports the best out of ⟦SLOT_67⟧ noisy skill estimates: statistical fluctuations ensure that the maximum overestimates the expected performance of a typical sample. This is especially relevant in leaderboard scenarios where multiple submissions are made and only the top-performing one is reported. This phenomenon is well-studied in the theory of order statistics (see Arnold et al. 1992; David & Nagaraja 2003).

**ZH** 这一结果形式化了「从 ⟦SLOT_67⟧ 个含噪技能估计中报告最优者」时产生的选择偏差：统计波动保证了最大值会高估一个典型样本的期望表现。这在排行榜场景中尤为相关——在那里会进行多次提交，且只报告表现最好的那一次。这一现象在次序统计理论中已有充分研究（参见 Arnold et al. 1992; David & Nagaraja 2003）。

**EN** Appendix D Data sources

**ZH** 附录 D 数据来源

**EN** To gain insights and analyze various trends in the Chatbot Arena leaderboard, we leverage multiple data sources. In total, our real-world data sources encompass 2M battles and cover 243 models across 42 providers. Below, we describe the different datasets used in our analyses.

**ZH** 为洞察并分析 Chatbot Arena 排行榜中的各种趋势，我们利用了多个数据源。总体来看，我们的真实数据源涵盖 200 万场对战，覆盖 42 家提供方的 243 个模型。下面描述我们分析中使用的各个数据集。

**EN** 1. Historical Battles (historical-battles): is a collection of 1.8 million battles from Chatbot Arena from April 2023 to January 2025. We build this resource by combining both released public battles by Chatbot Arena and proprietary battle dataset released by Chatbot Arena to providers such as Cohere based upon their policy6. We describe both datasets in more detail Section D.1. We leverage historical-battles dataset as a key resource for quantifying task distribution drift (see Figure 11): • How do Arena use cases change over time?

**ZH** 1. 历史对战（historical-battles）：这是 Chatbot Arena 从 2023 年 4 月到 2025 年 1 月的 180 万场对战的集合。我们通过合并 Chatbot Arena 公开发布的对战，以及 Chatbot Arena 依据其政策6 向 Cohere 等提供方发布的专有对战数据集，构建了这一资源。我们在第 D.1 节更详细地描述这两个数据集。我们把 historical-battles 数据集用作量化任务分布漂移的关键资源（见图 11）：• Arena 的用例随时间如何变化？

**EN** 2. API Prompts: Majority of historical-battles dataset does not contain prompts as shown in Table 1. Additionally, all datasets published by LMArena are already de-duplicated so they won’t be useful for capturing the extent of similar or overlapping queries. Hence we switch to prompts collected via Cohere’s API based on requests received via Chatbot Arena, comprising a total of 567,319 entries. For simplicity and the purposes of this study, we excluded records with null values and multi-turn data and analyzed 197,217 single-turn conversations collected between November 2024 and April 2025. The models include command-r-08-2024, command-r-plus-08-2024 (Cohere 2024), aya-expanse-8b, aya-expanse-32b (Üstün et al. 2024; Dang et al. 2024b), and command-a-03-2025 (Cohere et al. 2025), along with three private variants. Of these, 62% of the data was labeled as coming from Aya models, while the remaining 38% was attributed to Command models. We use this dataset for prompt duplication analysis (see Figure 12 and Appendix H): • How many prompts are duplicates or close duplicates?

**ZH** 2. API 提示：如表 1 所示，historical-battles 数据集的大部分不包含提示。此外，LMArena 发布的所有数据集都已去重，因此无法用于体现相似或重叠查询的程度。因此我们改用通过 Cohere API 收集的提示——这些提示来自经由 Chatbot Arena 收到的请求，共 567,319 条。为简洁起见并出于本研究的目的，我们剔除了含空值的记录与多轮数据，分析了 2024 年 11 月至 2025 年 4 月间收集的 197,217 条单轮对话。涉及的模型包括 command-r-08-2024、command-r-plus-08-2024（Cohere 2024）、aya-expanse-8b、aya-expanse-32b（Üstün et al. 2024; Dang et al. 2024b）以及 command-a-03-2025（Cohere et al. 2025），另有三个私有变体。其中 62% 的数据被标记为来自 Aya 模型，其余 38% 归属于 Command 模型。我们用这一数据集做提示重复分析（见图 12 与附录 H）：• 有多少提示是完全重复或近似重复的？

**EN** 3. Leaderboard Statistics (leaderboard-stats): is snapshots of ratings and rankings as well as the number of battles played over time by models published on Chatbot Arena’s public leaderboard since its inception. To build this resource, we consolidate historical leaderboard snapshots released by Chatbot Arena on Hugging Face2828 28 https://huggingface.co/spaces/lmarena-ai/chatbot-arena-leaderboard/tree/main. For fair assessment, we consider historical data starting from January 9 2024 – April 23 2025 for our analysis since Chatbot Arena switched to using the latest Bradley-Terry model in December 2023 to improve the reliability of model rankings30. By combining all leaderboard tables published by LMArena during this period, we obtained 14.3K records corresponding to 243 unique models evaluated on Chatbot Arena. We also enriched this dataset with additional metadata, such as categorizing models as proprietary, open-weight, or open-source based on the classification described in Appendix F. We use this data for analyzing trends related to no. of models, data access across providers (See Figures 2, 3 and 4) as well as model deprecation (See Figures 19, 18 and 13): • How does data access vary between providers? • How do models’ deprecations vary by provider and across proprietary, open-weight, and open-source models?

**ZH** 3. 排行榜统计（leaderboard-stats）：这是自 Chatbot Arena 公开排行榜上线以来，随时间发布的各模型的评分与排名以及参与对战次数的快照。为构建这一资源，我们整合了 Chatbot Arena 在 Hugging Face 上发布的历史排行榜快照2828 28 https://huggingface.co/spaces/lmarena-ai/chatbot-arena-leaderboard/tree/main。为保证评估公平，我们选取 2024 年 1 月 9 日至 2025 年 4 月 23 日的历史数据用于分析，因为 Chatbot Arena 已于 2023 年 12 月改用最新的 Bradley-Terry 模型，以提升模型排名的可靠性30。通过合并 LMArena 在此期间发布的所有排行榜表格，我们得到对应 Chatbot Arena 上 243 个唯一模型的 14.3K 条记录。我们还用额外元数据丰富了这一数据集，例如依据附录 F 所述的分类把模型归为专有、开放权重或开源。我们用该数据分析模型数量、各提供方数据访问相关的趋势（见图 2、图 3 与图 4），以及模型下架（见图 19、图 18 与图 13）：• 各提供方之间的数据访问如何变化？• 模型的下架在各提供方之间、以及在专有、开放权重与开源模型之间如何变化？

**EN** 4. Random Sample Battles (scraped-random-sample): The historical-battles and leade rboard-stats dataset does not provide insights into private testing being conducted by different providers. It appears private battles are removed by Chatbot Arena maintainers from the data before being released in both datasets. Furthermore, historical-battles contains the majority of samples from 2023 and 2024 and does not provide visibility in current sampling rate trends being followed on the Arena. To address this gap, we collected 5864 battles by crawling Chatbot Arena between January 2025 – March 2025 (approximately 150 a day). To avoid our collection from disrupting actual voting, we first ask models about their identity, which causes models to reveal their identities and automatically invalidates these battles for updating the scores.6 (Chiang et al. 2024) As a further precaution, we only scrape a low volume of daily samples and only vote for ties between models. Additionally, we use this identity prompt to identify model ownership of private variants, as detailed in the Section E.1. We store the identity revealed for each model to track the volume of private testing (more details included in Section E.4). We use this scraped-random-sample, which is a representative random sample over time, to answer a few critical questions: • Are different models sampled for battles at similar rates? • How many anonymous models are being tested by different model providers?

**ZH** 4. 随机采样对战（scraped-random-sample）：historical-battles 与 leaderboard-stats 数据集无法提供关于各提供方正在进行私有测试的洞察。看起来私有对战在发布前被 Chatbot Arena 维护者从这两个数据集的数据中移除。此外，historical-battles 的样本大多来自 2023 与 2024 年，无法反映 Arena 上当前的采样率趋势。为填补这一空白，我们在 2025 年 1 月至 2025 年 3 月间通过爬取 Chatbot Arena 收集了 5864 场对战（约每天 150 场）。为避免我们的收集干扰实际投票，我们首先询问模型的身份——这会使模型暴露身份，从而使这些对战自动失效、不用于更新分数6（Chiang et al. 2024）。作为进一步的预防措施，我们每天只抓取少量样本，且只对模型之间的平局投票。此外，我们用这一身份提示来识别私有变体的模型归属，详见第 E.1 节。我们存储每个模型显露的身份，以追踪私有测试的规模（更多细节见第 E.4 节）。我们用这一随时间具有代表性的随机样本 scraped-random-sample 来回答几个关键问题：• 不同模型是否以相近的比率被采样参与对战？• 不同模型提供方正在测试多少匿名模型？

**EN** We provide additional details about historical-battles dataset in the Section D.1. We also provide a detailed overview of all datasets in Table 1.

**ZH** 我们在第 D.1 节提供关于 historical-battles 数据集的更多细节。我们还在表 1 中给出所有数据集的详细概览。

**EN** D.1 Public and Private Battles

**ZH** D.1 公开与私有对战

**EN** Our historical-battles dataset includes snapshots of battles played on Chatbot Arena that have been released publicly or shared privately with model providers based on their policy6. We provide additional details about public and private subsets of historical-battles, for the reader’s consideration below.

**ZH** 我们的 historical-battles 数据集包含在 Chatbot Arena 上进行的对战快照，这些对战依据其政策6 被公开发布，或与模型提供方私下共享。下面我们就 historical-battles 的公开与私有子集提供更多细节，供读者参考。

**EN** • Public Battles: The public portion of our historical data comes from the officially released datasets by Chatbot Arena on Hugging Face or as part of notebook tutorials. We combine the arena-human-preference-100K2929 29 https://huggingface.co/datasets/lmarena-ai/arena-human-preference-100k (Chiang et al. 2024; Tang et al. 2025) dataset containing 106K samples from June 2024 -- August 2024 with datasets shared by Chatbot Arena as part of notebook tutorials on Bradley Terry3030 30 https://blog.lmarena.ai/blog/2023/leaderboard-elo-update/ and Elo Rating systems3131 31 https://blog.lmarena.ai/blog/2023/arena/. This resulted in around 2M samples from April 2023 to August 2024 in total. 90% of the data does not include any prompt or completion history, instead consisting only of the names of the two models battling and the winning model as well as language and task category tags. We exclude other public battles released by Chatbot Arena for inclusion in historical-battles dataset since they did not contain required columns or enough multilingual data points required for the analysis presented in Figure 11.

**ZH** • 公开对战：我们历史数据的公开部分来自 Chatbot Arena 在 Hugging Face 上正式发布的数据集，或作为 notebook 教程的一部分发布的数据。我们把 arena-human-preference-100K2929 29 https://huggingface.co/datasets/lmarena-ai/arena-human-preference-100k（Chiang et al. 2024; Tang et al. 2025）数据集（含 2024 年 6 月至 8 月的 106K 条样本）与 Chatbot Arena 作为 Bradley Terry3030 30 https://blog.lmarena.ai/blog/2023/leaderboard-elo-update/ 和 Elo 评分系统3131 31 https://blog.lmarena.ai/blog/2023/arena/ 的 notebook 教程分享的数据集合并。这总共得到 2023 年 4 月至 2024 年 8 月间约 200 万条样本。其中 90% 的数据不包含任何提示或补全历史，只由对战双方模型的名称、获胜模型以及语言与任务类别标签构成。我们排除了 Chatbot Arena 发布的其他公开对战，因为它们不含所需列，或缺少图 11 分析所需的多语言数据点。

**EN** • Proprietary Battles: We also obtain historical battle data from Chatbot Arena maintainers for battles that involve Command and Aya models. This data was shared based on Chatbot Arena’s policy6, which permits model providers to request access to 20% of the data collected involving their own models. The data we received consists of 43,729 battles played by the following models between March 2024 and March 2025: command-r, command-r-plus, command-r-08-2024, command-r-plus-08-2024 (Cohere 2024), aya-expanse-8b, aya-exp- anse-32b (Üstün et al. 2024; Dang et al. 2024b). In contrast to the public data, this proprietary data contains the complete model conversations. Since this data is 46% multilingual, we combine this with public battles to form historical-battles and use it for language distribution shift analysis presented in Figure 11.

**ZH** • 专有对战：我们还从 Chatbot Arena 维护者处获得了涉及 Command 与 Aya 模型的历史对战数据。这些数据的共享基于 Chatbot Arena 的政策6，该政策允许模型提供方申请获取涉及其自身模型所收集数据的 20%。我们收到的数据包含以下模型在 2024 年 3 月至 2025 年 3 月间进行的 43,729 场对战：command-r、command-r-plus、command-r-08-2024、command-r-plus-08-2024（Cohere 2024）、aya-expanse-8b、aya-expanse-32b（Üstün et al. 2024; Dang et al. 2024b）。与公开数据不同，这些专有数据包含完整的模型对话。由于该数据有 46% 是多语言的，我们把它与公开对战合并形成 historical-battles，并用于图 11 所示的语言分布漂移分析。

**EN** Appendix E Our Scraping Methodology of LMArena Statistics

**ZH** 附录 E 我们对 LMArena 统计数据的抓取方法

**EN** We collected 5.8K battles (scraped-random-sample) by crawling data from Chatbot Arena on a regular basis between January–March, 2025. For this purpose, we setup a scraping script using Selenium library with chrome browser driver. To identify anonymous models, we first sent a de-anonymizing prompt. While Chatbot Arena does discard battles where models reveal their identities, as an additional measure on our end, we ask a simple follow-up question designed to most likely result in ties, such as “What is the capital of England? Reply with one word only.” or “Is the Earth round? Reply with Yes/No only.” Our scraping script extracted the models’ names as well as their responses to the asked questions. In addition to the scraped-random-sample collected by crawling the main Chatbot Arena leaderboard, we also collected around 500 additional samples by scraping the Vision leaderboard between 9th March and 28th March, 2025. This helped us in identifying 35 private vision models which are shown in section E.2. We refer to this collected set of vision battles as scraped-vision-sample.

**ZH** 我们在 2025 年 1 月至 3 月间定期从 Chatbot Arena 爬取数据，收集了 5.8K 场对战（scraped-random-sample）。为此，我们用 Selenium 库配合 chrome 浏览器驱动搭建了一个抓取脚本。为识别匿名模型，我们先发送一条去匿名化的提示。虽然 Chatbot Arena 会丢弃模型暴露身份的对战，我们仍额外采取了一道措施：问一个很可能导致平局的简单追问，例如「英格兰的首都是什么？只用一个词回答。」或「地球是圆的吗？只回答是/否。」我们的抓取脚本提取了模型的名称以及它们对所提问题的回答。除通过爬取 Chatbot Arena 主排行榜收集的 scraped-random-sample 外，我们还在 2025 年 3 月 9 日至 3 月 28 日间抓取视觉排行榜收集了约 500 条额外样本。这帮助我们识别出第 E.2 节所示的 35 个私有视觉模型。我们把这批视觉对战称为 scraped-vision-sample。

**EN** E.1 De-anonymizing Model Identities

**ZH** E.1 去匿名化模型身份

**EN** While crawling battles to prepare scraped-random-sample, we ask the models about their identity. This helps in ensuring that our votes from scraping the arena don’t interfere with the leaderboard rankings since Chatbot Arena discards votes in which models reveal their identities (Chiang et al. 2024). We use either one of the following prompts to de-anonymize the model identity.

**ZH** 在抓取对战以构建 scraped-random-sample 时，我们会询问模型的身份。这有助于确保我们抓取 arena 时的投票不会干扰排行榜排名，因为 Chatbot Arena 会丢弃模型暴露身份的那些投票（Chiang et al. 2024）。我们使用以下提示之一来去匿名化模型身份。

<!-- [原子块 · svg]  -->

**EN** The model identities are then inferred based on the responses of the models. In Section E.4, we specify the responses of different private variants based on which they were assigned to their respective providers. Using this approach, we identified a total of 64 private models corresponding to 10 providers. We also captured 14 other private models as part of our scraping but weren’t able to de-anonymize them: kiwi, space, maxwell, luca, anonymous-engine-1, tippu, sky, pineapple, pegasus, dasher, dancer, blueprint, dry_goods, prancer.

**ZH** 模型身份随后依据模型的回答推断。在第 E.4 节，我们列出不同私有变体的回答，据此把它们归属到各自的提供方。用这一方法，我们共识别出对应 10 家提供方的 64 个私有模型。我们还在抓取中捕获了另外 14 个私有模型，但无法将它们去匿名化：kiwi、space、maxwell、luca、anonymous-engine-1、tippu、sky、pineapple、pegasus、dasher、dancer、blueprint、dry_goods、prancer。

**EN** E.2 Encountered Private Models in Scraping

**ZH** E.2 抓取中遇到的私有模型

**EN** Table 2: Private Models by Provider. We show the private models corresponding to each provider, which were identified by crawling overall and vision leaderboards (See Section E). The models highlighted in bold appear on both leaderboards. We find that Meta had an additional 16 private models active on the Vision leaderboard along with its 27 models on the Overall leaderboard, bringing its total count to 43. We show the models corresponding to overall leaderboard in Figure 6. We exclude models corresponding to LMArena from this figure, as they are associated with the Prompt-to-Leaderboard work led by Chatbot Arena (Frick et al. 2025).

**ZH** 表 2：各提供方的私有模型。我们展示通过爬取总榜与视觉榜（见第 E 节）识别出的、对应各提供方的私有模型。加粗的模型同时出现在两个排行榜上。我们发现 Meta 除在总榜上的 27 个模型外，还在视觉榜上有额外 16 个活跃的私有模型，使其总数达到 43。我们在图 6 中展示总榜对应的模型。我们把与 LMArena 相关的模型排除在该图之外，因为它们属于由 Chatbot Arena 主导的 Prompt-to-Leaderboard 工作（Frick et al. 2025）。

<!-- [原子块 · table] Provider No. of private models Private Models from Overall leaderboard Additional Private Models from Vision leaderboard Meta 43 polus aurora deep-inertia cresta goose discovery falcon ertiga jerky fl -->

**EN** E.3 Encountered Public Models in Scraping

**ZH** E.3 抓取中遇到的公开模型

**EN** Table 3: Public Models per Provider. This table shows the public models from each provider that appeared on the overall and vision leaderboards during our scraping period (January–March 2025). Models highlighted in bold appear on both leaderboards. Google and OpenAI had the most public models active during this period, with 15 and 9 models, respectively.

**ZH** 表 3：各提供方的公开模型。本表显示在抓取期间（2025 年 1—3 月）出现在总榜与视觉榜上的各提供方的公开模型。加粗的模型同时出现在两个排行榜上。Google 与 OpenAI 在此期间活跃的公开模型最多，分别为 15 个与 9 个。

<!-- [原子块 · table] Provider No. of public models Public Models from Overall leaderboard Additional Public Models from Vision leaderboard Meta 3 llama-3.1-405b-instruct-bf16 llama-3.2-vision-90b-instruct llama-3.3-70b-in -->

**EN** E.4 Assignment of Private Variants to Providers

**ZH** E.4 私有变体到提供方的归属

**EN** Table 4: Private variants identified for different providers. The table lists the private models captured in our scraped-random-sample or scraped-vision-sample, along with the number of responses revealing their identities and corresponding examples. Notably, the model raspberry withheld its identity in most responses (37 total) but disclosed “Amazon” as its provider in three instances. It’s possible that some private models appeared in more battles, but we couldn’t capture their responses to our de-anonymizing prompt due to scraping errors. Additionally, a few battles occurred early in the project before we introduced asking the de-anonymizing prompt in our scraping methodology. Note that models with prefixes "p2l" and "experimental-router" identify as OpenAI/Google models but we assign them to LMArena as they are part of prompt-to-leaderboard work being lead by LMArena.(Frick et al. 2025).

**ZH** 表 4：为不同提供方识别出的私有变体。本表列出在我们的 scraped-random-sample 或 scraped-vision-sample 中捕获的私有模型，以及暴露其身份的回答数量与相应示例。值得注意的是，raspberry 这个模型在多数回答中（共 37 条）隐瞒了自己的身份，但在三次回答中披露「Amazon」为其提供方。有可能某些私有模型出现在更多对战中，但由于抓取错误我们未能捕获它们对我们去匿名化提示的回答。此外，项目早期在我们于抓取方法中引入去匿名化提示之前，也发生过少量对战。注意带有 "p2l" 与 "experimental-router" 前缀的模型自称为 OpenAI/Google 模型，但我们把它们归给 LMArena，因为它们属于由 LMArena 主导的 prompt-to-leaderboard 工作（Frick et al. 2025）。

<!-- [原子块 · table] Identified Provider Model Name No. of Responses Revealing Identity Model Responses Meta kronus 73 Llama, trained by Meta. polus 57 Llama, trained by Meta. frost 47 I’m an artificial intelligence model -->

**EN** E.5 Sampling Rates

**ZH** E.5 采样率

**EN** Table 5: Maximum sampling rate observed for models of different providers. We define the model sampling rate as the percentage of daily battles a model participates in, with the maximum sampling rate for a provider being the highest rate achieved by any of its models on any given day. We determine the maximum sampling rate of providers based on scraped-random-sample, which is limited to the specific period during which we collected this data (January 2025 to March 2025). At the extreme, Google and OpenAI reach a maximum daily sampling rate of 34%, while Reka registers the lowest at 3.3%.To ensure a fair assessment, we only considered models that appeared in battles on days when we collected a minimum of 100 samples from Chatbot Arena.

**ZH** 表 5：观测到的各提供方模型的最高采样率。我们把模型采样率定义为一个模型参与的对战占每日对战的百分比，某提供方的最大采样率是其任一模型在任一天达到的最高比率。我们依据 scraped-random-sample 确定各提供方的最大采样率，该数据源限于我们收集数据的特定时段（2025 年 1 月至 2025 年 3 月）。极端情况下，Google 与 OpenAI 的日最高采样率达到 34%，而 Reka 最低，为 3.3%。为保证评估公平，我们只考虑在我们从 Chatbot Arena 至少收集了 100 条样本的日期里出现在对战中的模型。

<!-- [原子块 · table] Provider Model Name Num Model Battles Total Battles Date Sampling Rate Nvidia march-chatbot-r 18 143 2025-03-16 12.59% march-chatbot 19 143 2025-03-16 13.29% Meta frost 11 176 2025-02-17 6.25% anonymo -->

**EN** Appendix F License Categories

**ZH** 附录 F 许可证类别

**EN** As part of leaderboard-stats, LMArena releases details about models that appeared on the public leaderboard including their licenses. We group the licenses found for models available on the public leaderboard into 3 categories i.e. Proprietary, Open-Weights and Open-Source. 3232 32 https://opensource.org/ai This categorization is used to plot Figure 2 and Figure 3 and reporting related numbers. We show the exact categorization used for the model licenses in the table below.

**ZH** 作为 leaderboard-stats 的一部分，LMArena 发布了出现在公开排行榜上的模型的详细信息，包括其许可证。我们把公开排行榜上可得模型的许可证归为三类，即专有、开放权重与开源。3232 32 https://opensource.org/ai 该分类用于绘制图 2 与图 3 以及报告相关数字。我们在下表中给出用于模型许可证的具体分类。

<!-- [原子块 · table] License Category Model Licenses Open Source Apache 2.0, Apache-2.0, MIT, CC-BY-SA 3.0, Open Open Weights AI2 ImpACT Low-risk, CC-BY-NC-4.0, CC-BY-NC-SA-4.0, CogVLM2, DBRX LICENSE, DeepSeek, DeepSeek L -->

**EN** Table 6: License categories and their corresponding model licenses. We group the licenses for the models on the public Chatbot Arena leaderboard into 3 categories i.e. Proprietary, Open-Weights and Open-Source.

**ZH** 表 6：许可证类别及其对应的模型许可证。我们把 Chatbot Arena 公开排行榜上模型的许可证归为三类，即专有、开放权重与开源。

**EN** Appendix G Data Access Estimation for Different Providers

**ZH** 附录 G 各提供方的数据访问估计

**EN** In Figure 4, we show the estimates for the data available to different providers. LMArena has collected around 3M user votes via Chatbot Arena in total. Each of these 3M votes resulted in twice the number of model API calls i.e. 6M since each battle features two models. Each square in Figure 4 represents roughly 5K API calls, illustrating how proprietary providers collectively access a considerably greater volume of data compared to the broader research community, which receives only a fraction. This disparity underscores a significant competitive advantage for large-industry labs, making it increasingly challenging for open-source efforts and smaller institutions to match the scale and diversity of data available to proprietary model developers. Note that we only show a small number of providers in Figure 4 so the total no. of API calls used to represent the data available to the model providers is 5M, which is less than the total number of estimated API calls, which is 6 million.

**ZH** 在图 4 中，我们给出了各提供方可得数据的估计。LMArena 通过 Chatbot Arena 共收集了约 300 万张用户投票。由于每场对战涉及两个模型，这 300 万张投票对应两倍数量的模型 API 调用，即 600 万次。图 4 中每个方块约代表 5K 次 API 调用，说明专有提供方合计访问的数据量远大于更广泛的研究社区——后者只获得其中一小部分。这一差距凸显了大型产业实验室的显著竞争优势，使开源力量与较小的机构越来越难以匹敌专有模型开发者所能获得的数据规模与多样性。注意我们在图 4 中只展示了少量提供方，因此用于表示各模型提供方可得数据的 API 调用总数为 5M，小于估计的 API 调用总数 600 万。

**EN** Appendix H Analysis of Prompt Repetitions in Arena Data

**ZH** 附录 H Arena 数据中提示重复的分析

**EN** As discussed in Section 4.2, user queries in Chatbot Arena are often highly similar or duplicated. Such patterns can be readily learned by today’s large language models, potentially leading to overfitting on the Chatbot Arena leaderboard. Figure 16 presents detailed cross-month prompt duplication rates based on the API data described in Appendix D. The heatmap illustrates that, according to two metrics (exact string match and text embedding similarity) within-month duplication rates are generally high, indicating the presence of numerous repeated prompts. Additionally, the substantial cross-month duplication rates suggest recurring patterns or frequently asked questions among Chatbot Arena users, which can be identified through simple analysis.

**ZH** 如第 4.2 节所述，Chatbot Arena 中的用户查询往往高度相似或重复。这类模式很容易被当今的大语言模型学到，可能导致在 Chatbot Arena 排行榜上过拟合。图 16 给出了基于附录 D 所述 API 数据的详细跨月提示重复率。该热力图显示，按两种度量（精确字符串匹配与文本嵌入相似度），月内重复率普遍较高，说明存在大量重复提示。此外，可观的跨月重复率表明 Chatbot Arena 用户中存在反复出现的模式或常见问题，这些可以通过简单分析识别出来。

<!-- [原子块 · img]  -->

**EN** (a) Embedding cosine similarity.

**ZH** (a) 嵌入余弦相似度。

<!-- [原子块 · img]  -->

**EN** (b) Exact string match.

**ZH** (b) 精确字符串匹配。

**EN** Figure 16: Cross-month prompt duplication rates. Left: The heatmap illustrates the proportion of prompts in one month that are highly similar or nearly duplicate to prompts in another month. Diagonal values represent within-month similarity. Right: The heatmap shows the proportion of prompts in one month that are exact matches to prompts in another. Diagonal values indicate within-month duplication rates.

**ZH** 图 16：跨月提示重复率。左：热力图显示某月中与另一月提示高度相似或近似重复的比例。对角线数值表示月内相似度。右：热力图显示某月中与另一月提示完全匹配的比例。对角线数值表示月内重复率。

**EN** Appendix I Simulation for Expected Lift from Private Testing

**ZH** 附录 I 私有测试期望增益的模拟

**EN** In Figure 7, we illustrate the simulated impact of increasing the number of private variants tested on the best expected Arena Score, observing a lift of 50 when 20 non-identical private variants are tested. This section provides additional details about this simulation and the differing lifts observed for identical versus heterogeneous (non-identical) variants. While we consider the non-identical variants scenario examined in Figure 7 to be more realistic, we have included the identical variant assumption for completeness, despite its less practical nature.

**ZH** 在图 7 中，我们展示了增加被测试私有变体数量对最佳期望 Arena 分数的模拟影响，观察到当测试 20 个非完全相同的私有变体时增益为 50。本节提供关于该模拟的更多细节，以及相同变体与异质（非相同）变体所观察到的不同增益。虽然我们认为图 7 所考察的非相同变体场景更为现实，但为完整起见，我们仍纳入了相同变体的假设，尽管它在实践中意义较小。

**EN** I.1 Background

**ZH** I.1 背景

**EN** Arena battles and the Bradley-Terry (BT) model. Let models ⟦SLOT_68⟧ and ⟦SLOT_69⟧ possess latent skills ⟦SLOT_70⟧. Under the BT model a single conversation (“battle”) produces a winner with probability

**ZH** Arena 对战与 Bradley-Terry（BT）模型。设模型 ⟦SLOT_68⟧ 与 ⟦SLOT_69⟧ 具有潜在技能 ⟦SLOT_70⟧。在 BT 模型下，一次对话（「对战」）产生胜者的概率为

<!-- [原子块 · table] Pr ⁡ ( i ​ beats ​ j ) = θ i θ i + θ j , Pr ⁡ ( j ​ beats ​ i ) = θ j θ i + θ j . \Pr\bigl(i\text{ beats }j\bigr)=\frac{\theta_{i}}{\theta_{i}+\theta_{j}},\qquad\Pr\bigl(j\text{ beats }i\bigr)=\frac{\ -->

**EN** The log–odds parameter ⟦SLOT_71⟧ is the natural scale for inference. Arena Score (Chiang et al. 2024) is a linear re-parameterisation of ⟦SLOT_72⟧:

**ZH** 对数几率参数 ⟦SLOT_71⟧ 是推断的自然尺度。Arena 分数（Chiang et al. 2024）是 ⟦SLOT_72⟧ 的一个线性重参数化：

<!-- [原子块 · table] Arena Score = 1000 + 400 ln ⁡ 10 ​ β ^ , \text{Arena Score}=1000+\frac{400}{\ln 10}\,\hat{\beta}, (3) -->

**EN** so one Arena Score point equals ⟦SLOT_73⟧ on the log-odds scale.

**ZH** 因此一个 Arena 分数点等于对数几率尺度上的 ⟦SLOT_73⟧。

**EN** Statistical efficiency. For equiprobable battles (⟦SLOT_74⟧) the Fisher information per outcome is ⟦SLOT_75⟧ (See Appendix J), yielding a BT standard error for ⟦SLOT_76⟧ from ⟦SLOT_77⟧ independent votes

**ZH** 统计效率。对于等概率的对战（⟦SLOT_74⟧），每个结果的 Fisher 信息为 ⟦SLOT_75⟧（见附录 J），得到 ⟦SLOT_76⟧ 的 BT 标准误（来自 ⟦SLOT_77⟧ 次独立投票）为

<!-- [原子块 · table] σ β ​ ( n ) = 1 I ​ n = 2 n . \sigma_{\beta}(n)=\sqrt{\frac{1}{In}}=\frac{2}{\sqrt{n}}. (4) -->

**EN** Mapping through (3),

**ZH** 通过式 (3) 映射，

<!-- [原子块 · table] σ Elo ​ ( n ) = 400 ln ⁡ 10 ​ σ β ​ ( n ) ≈ 347.4 n (Arena scale). \sigma_{\text{Elo}}(n)=\frac{400}{\ln 10}\;\sigma_{\beta}(n)\approx\frac{347.4}{\sqrt{n}}\qquad\text{(Arena scale).} (5) -->

**EN** Pre-release best-of-N strategy. A provider trains ⟦SLOT_78⟧ private variants, evaluates each on a hidden Arena fork, and publicly submits only the one that scores highest. The selection creates an extreme–value bias because the retained estimate is conditioned on being the maximum of ⟦SLOT_79⟧ noisy measurements.

**ZH** 发布前的 best-of-N 策略。某提供方训练 ⟦SLOT_78⟧ 个私有变体，在一个隐藏的 Arena 分支上评测每一个，只公开提交得分最高的那个。这一选择造成极值偏差，因为被保留下来的估计是以「它是 ⟦SLOT_79⟧ 个含噪测量中的最大值」为条件的。

**EN** I.2 Identical Variants (⟦SLOT_80⟧)

**ZH** I.2 相同变体（⟦SLOT_80⟧）

**EN** In Figure 17, we show the esitmated lift in Arena Score if the checkpoints submitted by a provider are identical.

**ZH** 在图 17 中，我们展示了若提供方提交的检查点完全相同时，Arena 分数的估计增益。

**EN** Assume every private checkpoint has the same true Arena Score ⟦SLOT_81⟧. The only randomness is measurement noise

**ZH** 假设每个私有检查点都有相同的真实 Arena 分数 ⟦SLOT_81⟧。唯一的随机性是测量噪声

<!-- [原子块 · table] E ^ k = μ + ε k , ε k ∼ 𝒩 ( 0 , σ noise 2 ) , k = 1 , … , N , σ noise = σ Arena Score ( n ) . \hat{E}_{k}\;=\;\mu+\varepsilon_{k},\;\varepsilon_{k}\sim\mathcal{N}(0,\sigma_{\text{noise}}^{2}),\quad k= -->

**EN** I.2.1 Extreme-value uplift

**ZH** I.2.1 极值提升

**EN** Let ⟦SLOT_82⟧. Classical results for the maximum of ⟦SLOT_83⟧ i.i.d. Gaussians give the expected uplift

**ZH** 设 ⟦SLOT_82⟧。关于 ⟦SLOT_83⟧ 个独立同分布高斯变量最大值的经典结果给出期望提升

<!-- [原子块 · table] 𝔼 ⁡ [ E ^ max − μ ] ⏟ selection bias = σ noise ​ 2 ​ ln ⁡ N ( σ true = 0 ) . \underbrace{\mathbb{E}\!\bigl[\hat{E}_{\max}-\mu\bigr]}_{\text{selection bias}}=\boxed{\sigma_{\text{noise}}\;\sqrt{2\ln N} -->

**EN** Numerical illustration With the current Arena policy (⟦SLOT_84⟧, hence ⟦SLOT_85⟧Arena Score)

**ZH** 数值示例 在当前的 Arena 政策下（⟦SLOT_84⟧，因此 ⟦SLOT_85⟧ Arena 分数）

<!-- [原子块 · table] M = 50 ⟹ bias ≈ 6.34 ​ 2 ​ ln ⁡ 50 = 17.7 ​ Arena Score . M=50\;\Longrightarrow\;\text{bias}\approx 6.34\,\sqrt{2\ln 50}\;=\;17.7\text{ Arena Score}. -->

**EN** Asymptotics

**ZH** 渐近性质

**EN** Because ⟦SLOT_86⟧, (6) ⟦SLOT_87⟧ as ⟦SLOT_88⟧. If checkpoints are identical, selection bias eventually disappears.

**ZH** 因为 ⟦SLOT_86⟧，式 (6) ⟦SLOT_87⟧，⟦SLOT_88⟧。如果检查点完全相同，选择偏差最终会消失。

<!-- [原子块 · object]  -->

**EN** Figure 17: Impact of the number of identical private variants tested on the best Expected Arena Score.

**ZH** 图 17：被测试的相同私有变体数量对最佳期望 Arena 分数的影响。

**EN** I.3 Heterogeneous Variants (⟦SLOT_89⟧)

**ZH** I.3 异质变体（⟦SLOT_89⟧）

**EN** In realistic settings, model variants submitted for prerelease testing are not identical (as shown in Figure 7). They differ due to variations in initialization, training seeds, data curation, or hyperparameter choices. As a result, each variant has its own true Arena score, even before accounting for statistical noise in Arena battles.

**ZH** 在现实设定中，提交做发布前测试的模型变体并不相同（如图 7 所示）。它们因初始化、训练种子、数据筛选或超参数选择的不同而有差异。因此，即便不计 Arena 对战中的统计噪声，每个变体也有其自身的真实 Arena 分数。

**EN** These models are not merely subject to selection bias arising from multiple evaluations of a single variant (i.e., due to statistical noise). Instead, each represents a genuinely distinct checkpoint with its own underlying performance. This reflects meaningful variation in model quality – not just fluctuations from randomness.

**ZH** 这些模型所承受的，不只是「对单一变体多次评测」（即统计噪声）所带来的选择偏差。相反，每一个都代表一个真正不同的检查点，有其自身的底层性能。这反映的是模型质量上的实质差异，而不仅仅是随机性造成的波动。

**EN** We model this by assigning each of the ⟦SLOT_90⟧ private checkpoints a different true skill:

**ZH** 我们通过为 ⟦SLOT_90⟧ 个私有检查点各赋予一个不同的真实技能来建模这一点：

<!-- [原子块 · table] E k = μ + δ k , δ k ∼ 𝒩 ⁡ ( 0 , σ true 2 ) , E_{k}=\mu+\delta_{k},\qquad\delta_{k}\sim\mathcal{N}(0,\sigma_{\text{true}}^{2}), -->

**EN** where ⟦SLOT_91⟧ is the mean Arena Score across all variants and ⟦SLOT_92⟧ quantifies the spread in true skill.

**ZH** 其中 ⟦SLOT_91⟧ 是所有变体的平均 Arena 分数，⟦SLOT_92⟧ 量化真实技能的离散程度。

**EN** When evaluated in Arena, each model’s observed Arena Score estimate ⟦SLOT_93⟧ is affected by both its intrinsic skill and sampling noise:

**ZH** 当在 Arena 中被评测时，每个模型被观测到的 Arena 分数估计 ⟦SLOT_93⟧ 同时受其内在技能与采样噪声的影响：

<!-- [原子块 · table] E ^ k = μ + δ k ⏟ true skill + ε k ⏟ Arena noise , ε k ∼ 𝒩 ⁡ ( 0 , σ noise 2 ) . \hat{E}_{k}=\underbrace{\mu+\delta_{k}}_{\text{true skill}}+\underbrace{\varepsilon_{k}}_{\text{Arena noise}},\qquad\va -->

**EN** Thus, the total variance in Arena Scores among the ⟦SLOT_94⟧ candidates is:

**ZH** 因此，⟦SLOT_94⟧ 个候选者之间 Arena 分数的总方差为：

<!-- [原子块 · table] σ total 2 = σ true 2 + σ noise 2 . \sigma_{\text{total}}^{2}=\sigma_{\text{true}}^{2}+\sigma_{\text{noise}}^{2}. -->

**EN** I.3.1 Extreme-value uplift

**ZH** I.3.1 极值提升

**EN** As before, the organization retains only the model with the highest observed Arena Score. The expected uplift from this best-of-⟦SLOT_95⟧ selection is given by:

**ZH** 如前，机构只保留观测 Arena 分数最高的那个模型。这一 best-of-⟦SLOT_95⟧ 选择带来的期望提升为：

<!-- [原子块 · table] bias ​ ( N , n , σ true ) = σ true 2 + σ Elo ​ ( n ) 2 ⋅ 2 ​ ln ⁡ N \boxed{\text{bias}(N,n,\sigma_{\text{true}})=\sqrt{\sigma_{\text{true}}^{2}+\sigma_{\text{Elo}}(n)^{2}}\cdot\sqrt{2\ln N}} (7) -->

**EN** This is a generalization of the identical-variant case. It shows that when true skill differences exist among checkpoints, the expected leaderboard inflation grows significantly larger—and no longer vanishes asymptotically, even as ⟦SLOT_96⟧.

**ZH** 这是相同变体情形的推广。它表明，当各检查点之间存在真实技能差异时，期望的排行榜膨胀会显著变大——并且不再随 ⟦SLOT_96⟧ 渐近消失。

**EN** Key consequences.

**ZH** 关键结论。

**EN** • Finite-data: even modest ⟦SLOT_97⟧ multiplies the uplift, e.g. ⟦SLOT_98⟧Arena Score yields ⟦SLOT_99⟧Arena Score at ⟦SLOT_100⟧.

**ZH** • 有限数据：即便不大的 ⟦SLOT_97⟧ 也会成倍放大提升，例如 ⟦SLOT_98⟧ Arena 分数产生 ⟦SLOT_99⟧ Arena 分数，当 ⟦SLOT_100⟧。

**EN** • Asymptotic limit: letting ⟦SLOT_101⟧ removes only the noise term, leaving ⟦SLOT_102⟧. Selection bias does not vanish.

**ZH** • 渐近极限：令 ⟦SLOT_101⟧ 只消除了噪声项，留下 ⟦SLOT_102⟧。选择偏差不会消失。

**EN** Appendix J A. Fisher Information for a Single BT Match

**ZH** 附录 J A. 单场 BT 对局的 Fisher 信息

**EN** The Bradley-Terry model defines the probability of item ⟦SLOT_103⟧ beating item ⟦SLOT_104⟧ as:

**ZH** Bradley-Terry 模型把条目 ⟦SLOT_103⟧ 战胜条目 ⟦SLOT_104⟧ 的概率定义为：

<!-- [原子块 · table] P ⁡ ( i > j ) = 1 1 + e ( β j − β i ) P(i>j)=\frac{1}{1+e^{(\beta_{j}-\beta_{i})}} -->

**EN** We assume equal-strength items (⟦SLOT_105⟧) so that ⟦SLOT_106⟧ and:

**ZH** 我们假设条目等强（⟦SLOT_105⟧），从而 ⟦SLOT_106⟧ 且：

<!-- [原子块 · table] P = 1 1 + e 0 = 1 2 P=\frac{1}{1+e^{0}}=\frac{1}{2} -->

**EN** This assumption is both mathematically convenient and empirically grounded (Casella & Berger 2002; Hunter 2004a):

**ZH** 这一假设在数学上便于处理，也有经验依据（Casella & Berger 2002; Hunter 2004a）：

**EN** • It simplifies the information calculation, providing a closed-form.

**ZH** • 它简化了信息计算，给出闭式解。

**EN** • It represents the point of maximum uncertainty: for a Bernoulli variable, ⟦SLOT_107⟧ is maximized when ⟦SLOT_108⟧.

**ZH** • 它代表了不确定性最大的点：对于伯努利变量，⟦SLOT_107⟧ 在 ⟦SLOT_108⟧ 时取最大值。

**EN** • In practice (e.g., Chatbot Arena), many matchups occur between similarly-rated models, making ⟦SLOT_109⟧ a reasonable approximation.

**ZH** • 在实践中（例如 Chatbot Arena），许多对局发生在评分相近的模型之间，使 ⟦SLOT_109⟧ 成为合理的近似。

**EN** The Fisher information for one such observation is (Hunter 2004a):

**ZH** 一次这样的观测的 Fisher 信息为（Hunter 2004a）：

<!-- [原子块 · table] ℐ ⁡ ( Δ ) = ∂ 2 ∂ Δ 2 ​ log ⁡ P ⁡ ( i > j ) | Δ = 0 = e 0 ( 1 + e 0 ) 2 = 1 4 \mathcal{I}(\Delta)=\left.\frac{\partial^{2}}{\partial\Delta^{2}}\log P(i>j)\right|_{\Delta=0}=\frac{e^{0}}{(1+e^{0})^{2}} -->

**EN** Conclusion: Each equal-skill BT match contributes:

**ZH** 结论：每一场等技能 BT 对局贡献：

<!-- [原子块 · table] Fisher Information = 0.25 \boxed{\text{Fisher Information}=0.25} -->

**EN** Appendix K Silent Model Deprecation: Additional Details

**ZH** 附录 K 静默模型下架：补充细节

**EN** In Section 5, we noted that the actual number of deprecated models far exceeds the official count provided by Chatbot Arena. Figure 18 illustrates the distribution of active, officially deprecated, and silently deprecated models per provider. For this analysis, we examined battles played between March 3rd and April 23rd, 2025. Of the 243 public models, 205 participated in an average of 10 or fewer battles during this period, based on leaderboard-stats. This number is significantly higher than the 47 models officially listed as deprecated by Chatbot Arena 5 Since Chatbot Arena assigns higher sampling weights to top-10 models, providers like Google, OpenAI, Anthropic, Amazon, Meta, and DeepSeek AI have the most actively sampled public models, ranging from 3 to 10. Additionally, the limited number of daily votes on the Arena, combined with Chatbot Arena’s policy of assigning higher sampling weights to new models6, can lead to the silent deprecation of many public models. As private variants are also new models, they receive high sampling weights as well. This means that as the number of private variants (see Figure 6) being tested on the Arena increases, the sampling of public models can be significantly reduced.

**ZH** 在第 5 节中，我们指出实际被下架的模型数量远超 Chatbot Arena 官方给出的数字。图 18 展示了各提供方的活跃、官方下架与静默下架模型的分布。在这一分析中，我们考察了 2025 年 3 月 3 日至 4 月 23 日之间进行的对战。基于 leaderboard-stats，在 243 个公开模型中有 205 个在此期间平均只参与了 10 场或更少的对战。这一数字显著高于 Chatbot Arena 官方列为已下架的 47 个模型5。由于 Chatbot Arena 给排名前十的模型赋予更高的采样权重，Google、OpenAI、Anthropic、Amazon、Meta 与 DeepSeek AI 等提供方拥有最多被积极采样的公开模型，数量在 3 到 10 个之间。此外，Arena 上每日投票数量有限，加上 Chatbot Arena 给新模型赋予更高采样权重的政策6，可能导致许多公开模型被静默下架。由于私有变体同样属于新模型，它们也会获得高采样权重。这意味着，随着 Arena 上被测试的私有变体数量增加（见图 6），公开模型的采样量可能被显著降低。

**EN** Figure 13 illustrates that deprecations disproportionately affect open-weight and open-source models compared to proprietary ones. A more detailed breakdown is provided in Figure 19, distinguishing between official and silent deprecations. Among officially deprecated models, 30% are proprietary, while only 2.4% are open-weight. However, silent deprecations have a much greater impact on open-weight and open-source models. Specifically, 86.6% of open-weight models and 87.8% of open-source models on the Arena are silently deprecated.

**ZH** 图 13 说明，与专有模型相比，下架对开放权重与开源模型的影响尤为严重。图 19 给出了更细致的分解，区分官方下架与静默下架。在官方下架的模型中，30% 是专有的，而开放权重仅占 2.4%。然而，静默下架对开放权重与开源模型的影响要大得多。具体地，Arena 上 86.6% 的开放权重模型与 87.8% 的开源模型被静默下架。

<!-- [原子块 · object]  -->

**EN** Figure 18: Share of active and deprecated models by provider including official and silent deprecations based on model activity between March 3-April 23, 2025.

**ZH** 图 18：2025 年 3 月 3 日至 4 月 23 日期间，基于模型活跃度的各提供方活跃与已下架（含官方与静默下架）模型占比。

<!-- [原子块 · object]  -->

**EN** Figure 19: Share of official and silent deprecations for proprietary, open-weight and open-source models based on model activity between March 3-April 23, 2025.

**ZH** 图 19：2025 年 3 月 3 日至 4 月 23 日期间，基于模型活跃度的专有、开放权重与开源模型的官方下架与静默下架占比。

**EN** Appendix L Transitivity Under Changing Evaluation Conditions: Additional Details

**ZH** 附录 L 评测条件变化下的传递性：补充细节

**EN** As part of our simulation to study the impact of model deprecations under a changing task distribution, we assign task-specific win probabilities for each model pair that compete in the battles as part of our simulation. The tables below show the win probabilities for different model pairs corresponding to task-1 and task-2.

**ZH** 在我们研究「变化的任务分布下模型下架影响」的模拟中，我们为参与对战的每个模型对赋予了任务特定的胜率。下表给出了对应 Task-1 与 Task-2 的不同模型对的胜率。

<!-- [原子块 · table] Model A B C D A - 0.4 0.4 0.6 B 0.5 - 0.7 0.9 C 0.6 0.3 - 0.7 D 0.4 0.1 0.3 - -->

**EN** Table 7: Win-rates for Task 1 used in simulation. Note that A vs B has a tie rate of 0.1.

**ZH** 表 7：模拟中使用的 Task 1 胜率。注意 A 对 B 有 0.1 的平局率。

<!-- [原子块 · table] Model A B C D A - 0.5 0.5 0.8 B 0.3 - 0.6 0.2 C 0.3 0.4 - 0.1 D 0.2 0.8 0.9 - -->

**EN** Table 8: Win-rates for Task 2 used in simulation. Note that A vs B and A vs C both have a tie rate of 0.2.

**ZH** 表 8：模拟中使用的 Task 2 胜率。注意 A 对 B 与 A 对 C 都有 0.2 的平局率。

**EN** Appendix M Overfitting Experiments: Additional Evaluations

**ZH** 附录 M 过拟合实验：补充评测

**EN** To measure if training on arena-style data impacts evaluation on non-arena style tasks, we also benchmark these models on the original MMLU dataset (Hendrycks et al. 2021). From Table 9, we observe that all models achieve very similar scores. This further demonstrates how training on data from Arena Battles helps boost scores specific to the Arena evaluation but provides little to no effect on a non-arena style benchmark.

**ZH** 为衡量在 arena 式数据上训练是否会影响非 arena 式任务上的评测，我们还在原始 MMLU 数据集（Hendrycks et al. 2021）上对这些模型做了基准测试。从表 9 可以看到，所有模型取得了非常接近的分数。这进一步证明，在 Arena 对战数据上训练有助于提升 Arena 评测特有的分数，但对非 arena 式基准几乎没有影响。

<!-- [原子块 · table] Finetuning mixture 0_arena 30_arena 70_arena Accuracy 66.5% 64.4% 65.9% -->

**EN** Table 9: Accuracy on MMLU across models trained with varying amounts of Arena data.

**ZH** 表 9：使用不同量 Arena 数据训练的模型在 MMLU 上的准确率。
