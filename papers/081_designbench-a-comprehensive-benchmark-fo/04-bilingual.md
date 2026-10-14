# DesignBench：面向基于 MLLM 的前端代码生成的综合性基准

> 原标题：DesignBench: A Comprehensive Benchmark for MLLM-based Front-end Code Generation
> 作者：Jingyu Xiao, Ming Wang, Man Ho Lam, Yuxuan Wan, Junliang Liu, Yintong Huo, Michael R. Lyu · arXiv:2506.06251 · 2025-06-06

<!-- [原子块 · verbatim] DesignBench: A Comprehensive Benchmark for MLLM-based Front-end Code Generation -->

<!-- [原子块 · verbatim] Abstract. -->

<!-- [原子块 · verbatim] Multimodal Large Language Models (MLLMs) have demonstrated remarkable capabilities in automated front-end engineering, e.g., generating UI code from visual designs. However, existing front-end UI code -->

<!-- [原子块 · verbatim] To bridge these gaps, we introduce DesignBench, a multi-framework, multi-task evaluation benchmark for assessing MLLMs’ capabilities in automated front-end engineering. DesignBench encompasses three w -->

**EN** Keywords:

**ZH** 关键词：

**EN** 1. Introduction

**ZH** 1. 引言

**EN** Converting webpage designs into functional UI code is a critical yet labor-intensive step in web development. MLLMs have demonstrated remarkable performance on visually rich code generation tasks (Yang et al., 2025; Liu et al., 2025; Zhang et al., 2025; Li et al., 2024; Chen et al., 2020; Tang et al., 2025), creating new opportunities for automated design-to-code conversion that replicates webpage elements, layouts, text, and colors.

**ZH** 把网页设计稿转换为可用的 UI 代码，是 Web 开发中关键且费力的一环。多模态大语言模型在视觉信息丰富的代码生成任务上表现优异（Yang 等，2025；Liu 等，2025；Zhang 等，2025；Li 等，2024；Chen 等，2020；Tang 等，2025），为自动化的设计到代码（design-to-code）转换创造了新的可能：复现网页的元素、布局、文字与配色。

**EN** Several benchmarks have been proposed to evaluate MLLMs on front-end code generation. These benchmarks typically involve either synthesizing webpage code via LLMs (e.g., WebSight (Laurençon et al., 2024) and Web2Code (Yun et al., 2024)), or curating code by cleaning real-world webpages (e.g., Webcode2M (Gui et al., 2025) and Design2Code (Si et al., 2024)). However, while these evaluation benchmarks are effective in measuring certain MLLM capabilities, they do not adequately represent the complex challenges faced by developers in real-world development scenarios.

**ZH** 已有若干基准用于评测多模态大语言模型的前端代码生成能力。这些基准要么是借助大语言模型合成网页代码（如 WebSight（Laurençon 等，2024）与 Web2Code（Yun 等，2024）），要么是通过清洗真实网页来整理代码（如 Webcode2M（Gui 等，2025）与 Design2Code（Si 等，2024））。它们虽能有效度量模型的某些能力，却不足以反映开发者在真实开发场景中面临的复杂挑战。

**EN** (1) Lack of front-end framework integration. Current benchmarks fail to incorporate front-end frameworks, such as React, Vue, and Angular, which are integral to modern web development (as indicated in 2025 trends (Raju, 2025)). Consequently, MLLMs’ capabilities for practical framework-based website development remain unexplored.

**ZH** （1）缺少前端框架支持。现有基准未纳入 React、Vue、Angular 等前端框架，而这些框架已成为现代 Web 开发的组成部分（参见 2025 年的趋势报告（Raju，2025））。因此，多模态大语言模型在基于框架的实际网站开发中的能力仍未得到考察。

**EN** (2) Insufficient task coverage. Existing benchmarks inadequately cover the comprehensive spectrum of front-end development tasks. As illustrated in Fig. 1, development encompasses not only initial code generation from UI designs, but also iterative code editing for design refinement and repairing design-related issues (Liu et al., 2020; Liu et al., 2022). However, current evaluations focus exclusively on the generation phase, neglecting the critical edit and repair phases.

**ZH** （2）任务覆盖不足。现有基准未能覆盖前端开发任务的完整谱系。如图 1 所示，开发工作不仅包含依据 UI 设计稿生成初始代码，还包括为细化设计而反复进行的代码编辑，以及修复与设计相关的问题（Liu 等，2020；Liu 等，2022）。现有评测却只关注生成阶段，忽略了编辑与修复这两个关键阶段。

<!-- [原子块 · img]  -->

**EN** Figure 1. Pipeline of MLLM-based automated front-end engineering.

**ZH** 图 1. 基于 MLLM 的自动化前端工程流程。

**EN** (3) Limited evaluation dimensions. Most existing studies assess the overall quality of the generated webpage, lacking a detailed, multi-dimensional analysis of MLLM performance. Such an analysis could consider varying difficulty levels, input contexts, and code-level attributes like correctness and reusability. The comprehensive evaluation is crucial for identifying strengths and weaknesses of MLLMs, thereby fostering more reliable models for practical deployment.

**ZH** （3）评测维度有限。多数现有研究只评估所生成网页的整体质量，缺少对模型表现细致的多维分析。这类分析本可考察不同的难度层级、不同的输入上下文，以及正确性与可复用性等代码层面的属性。全面评测对于识别模型的长短板、进而推动更可靠模型的实际部署具有关键作用。

**EN** To address these limitations, we propose DesignBench, a comprehensive multi-framework multi-task benchmark for evaluating MLLMs across multiple dimensions. DesignBench covers three popular front-end frameworks (React, Vue, Angular) and encompasses three key tasks: design generation, edit, and repair. The benchmark contains 900 webpage samples spanning more than 11 topics, 9 edit types, and 6 issue categories, enabling detailed analysis of MLLM performance across difficulty levels, context, and code dimensions.

**ZH** 为弥补上述不足，我们提出 DesignBench——一个面向多维度评测的多框架、多任务基准。DesignBench 覆盖 React、Vue、Angular 三种主流前端框架，包含设计生成、编辑与修复三项核心任务。该基准含 900 个网页样本，涵盖 11 个以上主题、9 类编辑操作与 6 类问题，支持从难度、上下文与代码三个维度对模型表现做细粒度分析。

**EN** Our extensive experiments yield several key findings: (1) Framework-specific limitations. MLLMs exhibit substantially lower performance in framework-based development compared to vanilla HTML/CSS. They struggle with framework-specific syntax, such as JSX parsing (React), template syntax (Vue), and TypeScript architecture (Angular). Critically, these models fail to effectively leverage framework features and component-based paradigms, resulting in diminished code reusability. (2) Task-specific bottlenecks. Distinct performance bottlenecks were identified across the three core development tasks. Design generation task suffers from visual rendering inaccuracies and compilation errors, while design editing and repair tasks are primarily constrained by shortcomings in code localization and UI issue identification capabilities. (3) Performance variability under different conditions. MLLM efficacy significantly degrades under more challenging conditions, including large UI images for generation, complex instructions for editing, and severe UI issues for repair. Notably, an input context analysis on design edit and repair tasks reveals that code-only inputs consistently outperform image-only inputs. Multimodal combinations provide minimal additional improvement, suggesting that code representations convey more precise semantic information for these modification tasks than visual inputs.

**ZH** 大量实验带来若干关键发现。（1）框架相关的能力短板。与原生 HTML/CSS 相比，模型在基于框架的开发上表现明显更弱，难以驾驭框架特有的语法，例如 React 的 JSX 解析、Vue 的模板语法与 Angular 的 TypeScript 架构。更严重的是，这些模型无法有效利用框架特性与组件化范式，导致代码可复用性下降。（2）任务相关的性能瓶颈。三项核心开发任务各有不同的瓶颈：设计生成受困于视觉渲染偏差与编译错误，设计编辑与修复则主要受制于代码定位与 UI 问题识别能力的不足。（3）不同条件下的表现波动。在更具挑战的条件下，模型效果显著下滑——生成任务面对大幅 UI 图像、编辑任务面对复杂指令、修复任务面对严重 UI 问题时均是如此。对设计编辑与修复任务的输入上下文分析还显示，纯代码输入始终优于纯图像输入，而多模态组合带来的增益很小，这说明在这两类修改任务中，代码表征比视觉输入承载了更精确的语义信息。

**EN** Table 1. Comparison of existing UI-to-Code benchmark and DesignBench. Vanilla refers to plain HTML/CSS.

**ZH** 表 1. 现有 UI 到代码基准与 DesignBench 的对比。Vanilla 指纯 HTML/CSS。

<!-- [原子块 · table] Benchmark Sample Source Framework Task Dimension Pix2code ( Beltramelli, 2018 ) 1742 Synthetic Vanilla Generation ✗ WebSight ( Laurençon et al., 2024 ) 823K Synthetic Vanilla Generation ✗ Web2Code ( G -->

**EN** Our main contributions are summarized as follows:

**ZH** 本文的主要贡献如下：

**EN** • We introduce the first multi-framework, multi-task benchmark for evaluating MLLMs’ capabilities in automated front-end engineering across HTML/CSS, React, Vue, and Angular frameworks.

**ZH** • 首个多框架、多任务基准：在 HTML/CSS、React、Vue、Angular 四类技术栈上评测多模态大语言模型的自动化前端工程能力。

**EN** • We conduct an extensive evaluation of nine leading MLLMs across three fundamental tasks. The analysis considers multiple dimensions, including task difficulty (visual complexity, instruction complexity, and issue severity), input context modalities (code-only, image-only, and multimodal), and code metrics (correctness and reusability).

**ZH** • 对九款主流多模态大语言模型在三项基础任务上的系统评测：分析覆盖任务难度（视觉复杂度、指令复杂度、问题严重程度）、输入上下文模态（纯代码、纯图像、多模态）与代码指标（正确性、可复用性）多个维度。

**EN** • We reveal key insights into MLLMs’ framework-specific limitations, identify task-dependent performance bottlenecks, characterize performance variations under diverse conditions and identify 22 types of failure of the three tasks. These results provide important guidance for future research and practice in front-end development.

**ZH** • 揭示模型在框架层面的能力短板，识别与任务相关的性能瓶颈，刻画不同条件下的表现差异，并归纳三项任务中 22 类失败模式。这些结果为前端开发领域后续的研究与实践提供了重要参考。

**EN** 2. Background

**ZH** 2. 背景

**EN** 2.1. Web Development Process

**ZH** 2.1. Web 开发流程

**EN** Web application front-end development process includes the following stages: (1) Design stage: designers create high-fidelity mock-ups using prototyping tools such as Sketch (38) and Axure (5) during design stage. (2) Development stage: it involves transforming the design concepts into a functional application through coding. The development stage typically consists of the implementation of the GUI and the underlying functionalities. As shown in Fig. 1, the developer first prompts the MLLM to generate the front-end code based on the UI-Mockup. However, the version one code did not fully comply with the UI-Mockup. Then the user asked MLLM to edit the code to change the background color and add buttons to generate version two. Then during the actual deployment process, the front-end engineer found a display issue on the UI, that is, a collision between the avatar and the name, and asked MLLM to fix it and generate version three code.

**ZH** Web 应用的前端开发流程包含以下阶段：（1）设计阶段：设计师使用 Sketch（38）、Axure（5）等原型工具制作高保真设计稿。（2）开发阶段：通过编码把设计概念转化为可运行的应用，通常包括图形用户界面的实现与底层功能的实现。如图 1 所示，开发者首先提示多模态大语言模型依据 UI 设计稿生成前端代码，但第一版代码并未完全符合设计稿。随后用户要求模型修改代码、更换背景色并添加按钮，得到第二版。在实际部署过程中，前端工程师又发现 UI 存在显示问题——头像与姓名发生重叠——于是要求模型修复，得到第三版代码。

**EN** 2.2. Front-end Web Development Framework

**ZH** 2.2. 前端 Web 开发框架

**EN** Front-end frameworks are collections of pre-written, reusable code that provide a foundation for building the user interface of a website. These frameworks can save time and improve the quality of the final product by providing a standardized set of components and templates for front-end development. In 2025, React, Vue, and Angular have emerged as the predominant frameworks in web development (Raju, 2025), with 39.5%, 15.4%, and 17.1% popularity (Krotoff, 2024), respectively.

**ZH** 前端框架是预先编写、可复用的代码集合，为构建网站用户界面提供基础。这类框架为前端开发提供标准化的组件与模板，从而节省时间并提升成品质量。2025 年，React、Vue 与 Angular 已成为 Web 开发中的主流框架（Raju，2025），使用率分别为 39.5%、15.4% 与 17.1%（Krotoff，2024）。

**EN** 3. Related Work

**ZH** 3. 相关工作

**EN** 3.1. UI Code Generation

**ZH** 3.1. UI 代码生成

**EN** UI code generation techniques fall into three categories: Deep Learning (DL) based methods, Computer Vision (CV) based methods, and Multimodal Large Language Model (MLLM) based methods. (1) DL-based methods: (Aşıroğlu et al., 2019; Cizotto et al., 2023; Moran et al., 2018; Xu et al., 2021; Chen et al., 2018) leverages CNNs to automatically prototype software GUIs. Pix2code (Beltramelli, 2018) utilizes CNNs and LSTM to extract features from GUI images to generate a domain-specific language (DSL). (Chen et al., 2022) implements an encoder-decoder framework with an attention mechanism to generate the DSL. (2) CV-based methods: Sketch2Code (Jain et al., 2019) inputs hand-drawn sketches into object detection models to learn the object representation, which is read by the UI parser to generate code for targeted platforms. REMAUI (Nguyen and Csallner, 2015) identifies user interface elements via optical character recognition (OCR) techniques and then infers a suitable user interface hierarchy and exports the results as source code. (3) MLLM-based methods (Lu et al., 2025; Wan et al., 2025b; Zhou et al., 2025; Yuan et al., 2025; Wan et al., 2025a; Xiao et al., 2025; Xiao et al., 2026; Dang et al., 2025): to solve the element omission distortion and misarrangement problems during UI code generation, DCGen (Wan et al., 2025b) proposes a divide-and-conquer-based approach to generate the code of the submodules separately and then assemble them to construct the full webpage based on MLLMs. DeclarUI (Zhou et al., 2025) applies the element segmentation method to accurately generate elements and page transition graphs to prompt MLLMs to generate mobile app UI with jump logic. EfficientUICoder (Xiao et al., 2025) accelerates UI code generation by input and output token compression. ComUICoder (Xiao et al., 2026) apply semantic-aware segmentation and merging methods for reusable UI code generation. While prior works achieve decent performance in UI-to-code, none of them address the conventional framework-based development and other essential front-end procedures like design edit and repair.

**ZH** UI 代码生成技术可分为三类：基于深度学习（DL）的方法、基于计算机视觉（CV）的方法与基于多模态大语言模型（MLLM）的方法。（1）基于深度学习的方法：（Aşıroğlu 等，2019；Cizotto 等，2023；Moran 等，2018；Xu 等，2021；Chen 等，2018）利用卷积神经网络自动生成软件 GUI 原型。Pix2code（Beltramelli，2018）用卷积神经网络与 LSTM 从 GUI 图像中提取特征，生成领域特定语言（DSL）。（Chen 等，2022）实现了带注意力机制的编码器—解码器框架来生成 DSL。（2）基于计算机视觉的方法：Sketch2Code（Jain 等，2019）把手绘草图输入目标检测模型以学习目标表征，再由 UI 解析器读取并生成面向特定平台的代码。REMAUI（Nguyen 与 Csallner，2015）借助光学字符识别（OCR）技术识别界面元素，推断合适的界面层级，并将结果导出为源代码。（3）基于多模态大语言模型的方法（Lu 等，2025；Wan 等，2025b；Zhou 等，2025；Yuan 等，2025；Wan 等，2025a；Xiao 等，2025；Xiao 等，2026；Dang 等，2025）：为解决 UI 代码生成中的元素遗漏、形变与错排问题，DCGen（Wan 等，2025b）提出分而治之的思路，先分别生成各子模块的代码，再组装成完整网页。DeclarUI（Zhou 等，2025）采用元素分割方法精确生成元素，并用页面跳转图提示多模态大语言模型生成带跳转逻辑的移动应用 UI。EfficientUICoder（Xiao 等，2025）通过输入与输出 token 压缩加速 UI 代码生成。ComUICoder（Xiao 等，2026）运用语义感知的分割与合并方法生成可复用的 UI 代码。已有方法在 UI 到代码任务上虽已取得不错的效果，却都未涉及基于框架的传统开发方式，也未触及设计编辑与修复等其他关键前端环节。

**EN** 3.2. Benchmarks for UI Code Generation

**ZH** 3.2. UI 代码生成基准

**EN** Many benchmarks (Gu et al., 2024; Lam et al., 2025; Jain et al., 2024; Zhuo et al., 2024) have been proposed to evaluate the code generation, understanding and reasoning capabilities of LLMs, but there are only a limited number of benchmarks for UI code. To improve MLLMs’ UI-to-Code capabilities, Pix2code introduced a domain-specific language (DSL) and leveraged CNN and LSTM architectures to translate UI mockups into DSL code. However, due to the inherent limitations of DSL approaches, Pix2code suffers from poor scalability and limited real-world applicability. WebSight advanced the field by synthesizing high-quality HTML code for training, while Web2Code (Yun et al., 2024) proposed the Webpage Code Generation Benchmark (WCGB) to systematically evaluate MLLMs’ HTML parsing capabilities. Despite these contributions, both benchmarks rely on synthetic data, which may not capture the complexity and variability of real-world web development scenarios. Design2Code (Si et al., 2024) addressed this limitation by manually curating 484 authentic web pages from the Common Crawl dataset, constructing the first real-world benchmark for design-to-code evaluation. Building upon this foundation, WebCode2M (Gui et al., 2025) significantly expanded the scale with 20,000 samples, providing both comprehensive training data for model development and robust test sets for evaluation. Other Benchmarks like Interaction2Code (Xiao et al., 2024) and MRWeb (Wan et al., 2024) mainly focus on the interactive and multi-page web application generation, which is out of our scope.

**ZH** 已有诸多基准（Gu 等，2024；Lam 等，2025；Jain 等，2024；Zhuo 等，2024）用于评测大语言模型的代码生成、理解与推理能力，但面向 UI 代码的基准数量有限。为提升多模态大语言模型的 UI 到代码能力，Pix2code 引入了领域特定语言（DSL），并利用 CNN 与 LSTM 架构将 UI 设计稿转换为 DSL 代码。受 DSL 方法固有局限所限，Pix2code 可扩展性差，实际应用价值有限。WebSight 通过合成高质量 HTML 代码用于训练，推动了该领域的发展；Web2Code（Yun 等，2024）则提出网页代码生成基准（WCGB），系统评估多模态大语言模型的 HTML 解析能力。尽管这些工作颇具价值，两个基准都依赖合成数据，难以刻画真实 Web 开发场景的复杂性与多样性。Design2Code（Si 等，2024）针对这一不足，从 Common Crawl 数据集中人工筛选出 484 个真实网页，构建了首个面向设计到代码评测的真实场景基准。在此基础上，WebCode2M（Gui 等，2025）将规模大幅扩展至 20,000 个样本，既提供了完备的训练数据，也提供了稳健的评测集。Interaction2Code（Xiao 等，2024）与 MRWeb（Wan 等，2024）等其他基准主要关注交互式与多页 Web 应用的生成，不在本文讨论范围内。

**EN** Table 1 presents a comparison between existing benchmarks and our, in terms of the size, collection method, framework, target tasks, and evaluation dimension. DesignBench is distinct in incorporating varied front-end frameworks, multiple tasks, and diverse evaluation dimensions.

**ZH** 表 1 从规模、采集方式、框架、目标任务与评测维度五个方面，对比了现有基准与本文基准。DesignBench 的独到之处在于纳入了多样化的前端框架、多重任务与多个评测维度。

**EN** 4. DesignBench

**ZH** 4. DesignBench

**EN** 4.1. Task Definition

**ZH** 4.1. 任务定义

**EN** As shown in Fig. 1, the automated front-end development mainly contains the following three tasks: “Design Generation”, “Design Edit” and “Design Repair”.

**ZH** 如图 1 所示，自动化前端开发主要包含三项任务：「设计生成」「设计编辑」与「设计修复」。

**EN** Design Generation (⟦SLOT_0⟧). The objective of design generation is to generate expected code based on the UI Mockups. Formally, given a UI design image ⟦SLOT_1⟧, the task aims to generate corresponding UI code ⟦SLOT_2⟧ such that ⟦SLOT_3⟧. The input contains the UI design image ⟦SLOT_4⟧, and the output is the UI code ⟦SLOT_5⟧ that accurately reproduces the visual layout and styling.

**ZH** 设计生成（⟦SLOT_0⟧）。设计生成的目标是根据 UI 设计稿生成符合预期的代码。形式化地说，给定 UI 设计图像 ⟦SLOT_1⟧，该任务旨在生成相应的 UI 代码 ⟦SLOT_2⟧，使得 ⟦SLOT_3⟧。输入为 UI 设计图像 ⟦SLOT_4⟧，输出为能准确复现视觉布局与样式的 UI 代码 ⟦SLOT_5⟧。

**EN** Design Edit (⟦SLOT_6⟧). The goal of the design edit is to generate front-end code that complies with user modification instructions. Given the original UI design image ⟦SLOT_7⟧, original UI code ⟦SLOT_8⟧, and user instruction ⟦SLOT_9⟧ described in natural language, the task produces modified code ⟦SLOT_10⟧ such that ⟦SLOT_11⟧. The input contains the original UI design image ⟦SLOT_12⟧, original UI code ⟦SLOT_13⟧, and user instruction ⟦SLOT_14⟧, while the output is the updated code ⟦SLOT_15⟧ incorporating the requested modifications.

**ZH** 设计编辑（⟦SLOT_6⟧）。设计编辑的目标是生成符合用户修改指令的前端代码。给定原始 UI 设计图像 ⟦SLOT_7⟧、原始 UI 代码 ⟦SLOT_8⟧，以及以自然语言描述的用户指令 ⟦SLOT_9⟧，该任务输出修改后的代码 ⟦SLOT_10⟧，使得 ⟦SLOT_11⟧。输入包含原始 UI 设计图像 ⟦SLOT_12⟧、原始 UI 代码 ⟦SLOT_13⟧ 与用户指令 ⟦SLOT_14⟧，输出为已按要求做出修改的更新代码 ⟦SLOT_15⟧。

**EN** Design Repair (⟦SLOT_16⟧). The goal of the design repair is to repair the UI code with display issues. Given the problematic UI code ⟦SLOT_17⟧, the problematic UI image ⟦SLOT_18⟧, the task generates repaired UI code ⟦SLOT_19⟧ such that ⟦SLOT_20⟧. The input contains the problematic UI code ⟦SLOT_21⟧ and image ⟦SLOT_22⟧, the output is the repaired code ⟦SLOT_23⟧ that resolves visual design issues.

**ZH** 设计修复（⟦SLOT_16⟧）。设计修复的目标是修复存在显示问题的 UI 代码。给定有问题的 UI 代码 ⟦SLOT_17⟧ 与有问题的 UI 图像 ⟦SLOT_18⟧，该任务生成修复后的 UI 代码 ⟦SLOT_19⟧，使得 ⟦SLOT_20⟧。输入包含有问题的 UI 代码 ⟦SLOT_21⟧ 与图像 ⟦SLOT_22⟧，输出为消除视觉设计问题的修复代码 ⟦SLOT_23⟧。

**EN** 4.2. Data Collection

**ZH** 4.2. 数据采集

<!-- [原子块 · img]  -->

**EN** Figure 2. Pipeline of DesignBench construction.

**ZH** 图 2. DesignBench 的构建流程。

**EN** Design Generation. For websites developed by frameworks, we collect samples from GitHub and the top 500 globally visited websites. Existing reports (Raju, 2025; Krotoff, 2024) show that the three most popular front-end development frameworks are React, Vue, and Angular, so we collect data for these three frameworks to build our benchmark. (1) Github projects. We search for “React projects”, “Vue projects” and “Angular projects” to get a summary list of web projects with different frameworks, then we identify 152 popular projects with deployed links and higher star counts. These projects represent various real-world website uses, ranging from commercial product front-end websites to blogs, with 4055 average star counts and an average of 996 forks. Their popularity has proven their usefulness and quality. (2) Top 500 globally visited websites. These websites are ranked by Moz (42), and we collect 158 webpages that adopt frameworks as our dataset.

**ZH** 设计生成。对于采用框架开发的网站，我们从 GitHub 与全球访问量前 500 的网站中收集样本。已有报告（Raju，2025；Krotoff，2024）显示，最流行的三种前端开发框架是 React、Vue 与 Angular，因此我们针对这三种框架采集数据以构建基准。（1）GitHub 项目。我们分别检索「React projects」「Vue projects」「Angular projects」，得到使用不同框架的 Web 项目清单，再从中筛选出 152 个已部署、星标数较高的热门项目。这些项目覆盖了从商业产品官网到博客等多种真实网站用途，平均星标数 4055，平均 fork 数 996，其受欢迎程度印证了自身的实用性与质量。（2）全球访问量前 500 的网站。这些网站按 Moz（42）排名，我们从中采集 158 个采用框架的网页作为数据集。

**EN** For websites without applying frameworks, we sample 120 webpages with different lengths from the webcode2m dataset (Gui et al., 2025). Ultimately, we compile a dataset consisting of 430 webpages. After getting the link of the webpage, we apply single-file tool (Lormeau, 2023) to save the webpage as a stand-alone file, then replace the images in the web page with placeholders, and finally use selenium (Selenium, 2025) to take screenshots for constructing the input design image ⟦SLOT_24⟧ for task ⟦SLOT_25⟧.

**ZH** 对于未使用框架的网站，我们从 webcode2m 数据集（Gui 等，2025）中按不同长度采样 120 个网页，最终汇总得到 430 个网页的数据集。取得网页链接后，先用 single-file 工具（Lormeau，2023）将网页保存为独立文件，再把网页中的图片替换为占位符，最后用 selenium（Selenium，2025）截图，构造出输入设计图像 ⟦SLOT_24⟧，供任务 ⟦SLOT_25⟧ 使用。

**EN** Design Edit. To obtain real-world user instructions for UI design modification, we crawl 541 React-based projects from Vercel’s V0 platform (43) and 1,349 Vue-based projects from Vue0 (44). These projects contain comprehensive interaction histories, including user instructions and corresponding UI code implementations.

**ZH** 设计编辑。为获取真实世界中用户对 UI 设计修改的指令，我们从 Vercel 的 V0 平台（43）爬取 541 个基于 React 的项目，从 Vue0（44）爬取 1,349 个基于 Vue 的项目。这些项目包含完整的交互历史，含用户指令及对应的 UI 代码实现。

**EN** We first filter the projects that can compile successfully with at least two iteration rounds. For each project with consecutive editing steps ⟦SLOT_26⟧ and ⟦SLOT_27⟧, we construct evaluation pairs where the input consists of the previous version’s code ⟦SLOT_28⟧, rendered UI image ⟦SLOT_29⟧, and the user instruction ⟦SLOT_30⟧ that describes the desired modifications. The ground truth comprises the updated code ⟦SLOT_31⟧ and its corresponding rendered UI image ⟦SLOT_32⟧ that implements the requested changes.

**ZH** 我们首先筛选出能成功编译且至少有两轮迭代的项目。对于每个具有连续编辑步骤 ⟦SLOT_26⟧ 与 ⟦SLOT_27⟧ 的项目，我们构造评测样本对：输入由上一版本代码 ⟦SLOT_28⟧、渲染出的 UI 图像 ⟦SLOT_29⟧，以及描述预期修改的用户指令 ⟦SLOT_30⟧ 组成；真值则由更新后代码 ⟦SLOT_31⟧ 及其对应渲染出的 UI 图像 ⟦SLOT_32⟧ 组成，实现了所要求的改动。

**EN** However, some edit steps feature ambiguous user instructions or poorly UI modifications that fail to satisfy the intended requirements (here11 1 https://github.com/WebPAI/DesignBench/blob/main/assets/Unclear_Failed_Examples.md are some bad cases). To filter out low-quality samples, we employ five PhD students with three years of front-end development experience to conduct a comprehensive assessment.

**ZH** 不过，部分编辑步骤存在用户指令含糊、或 UI 修改质量不佳而未能满足预期需求的情况（此处11 1 https://github.com/WebPAI/DesignBench/blob/main/assets/Unclear_Failed_Examples.md 为若干劣质样例）。为滤除低质量样本，我们聘请五名具有三年前端开发经验的博士生做全面评估。

**EN** Specifically, the annotators classify user instructions into three levels of clarity: clear, moderate, and ambiguous, based on detailed assessment of instruction specificity, actionability, and comprehensibility. Similarly, they evaluate the quality of modified UI and categorize them into terrible, good, and excellent based on how well the changes align with the given instructions. The detailed annotation guidelines are in (Team, ). The final classifications for both instruction clarity and UI modification effectiveness are determined through a majority voting process among the annotators.

**ZH** 具体地，标注者依据对指令明确性、可操作性与可理解性的细致评估，把用户指令分为清晰（clear）、中等（moderate）与含糊（ambiguous）三个等级。类似地，他们评估修改后的 UI 质量，按改动与给定指令的契合程度分为糟糕（terrible）、良好（good）与优秀（excellent）。详细的标注指南见（Team，）。指令清晰度与 UI 修改有效性的最终分级，均由标注者投票多数决确定。

**EN** Finally, we curate 359 high-quality React and Vue samples that receive clear instruction ratings and excellent modification quality scores. To obtain Angular and vanilla HTML/CSS samples, we randomly select 146 samples from this curated set and translate them into Angular and vanilla HTML/CSS code implementations using GPT-4o (OpenAI, 2024). Following the automated translation, the same five PhD students verify the correctness of the translated implementations, and make necessary modifications to ensure the code meet users’ instructions.

**ZH** 最终，我们整理出 359 个高质量的 React 与 Vue 样本，它们的指令被评为清晰、修改质量被评为优秀。为获得 Angular 与原生 HTML/CSS 样本，我们从该精选集合中随机抽取 146 个样本，用 GPT-4o（OpenAI，2024）将其翻译为 Angular 与原生 HTML/CSS 实现。自动翻译之后，由同样的五名博士生校验翻译实现的正确性，并做必要的修改，以确保代码满足用户指令。

**EN** Design Repair. After collecting the webpages of the above two tasks, the five PhD students filter the samples with design issues. They follow comprehensive guidelines to identify display issues, including: (1) Layout issues such as misaligned elements and incorrect positioning; (2) Visual inconsistencies including improper spacing, incorrect font sizes, or color scheme violations; (3) Component rendering problems such as missing elements, overlapping content, or distorted images.

**ZH** 设计修复。采集完前两项任务的网页后，五名博士生筛选出存在设计问题的样本。他们遵循详尽的指南识别显示问题，包括：（1）布局问题，如元素错位与定位错误；（2）视觉不一致，如间距不当、字号错误或配色违例；（3）组件渲染问题，如元素缺失、内容重叠或图像失真。

**EN** Finally, we get 111 webpages with problematic UI code ⟦SLOT_33⟧ and image ⟦SLOT_34⟧. To obtain the repaired code ⟦SLOT_35⟧ for evaluation, 111 webpages are evenly assigned to the five PhD students to manually fix the issues. Each student spent about 5 hours to complete the repair of all assigned samples. The detailed annotation guidelines of these three tasks are in our repo22 2 https://github.com/WebPAI/DesignBench/blob/main/assets/Guideline.md.

**ZH** 最终得到 111 个带有问题 UI 代码 ⟦SLOT_33⟧ 与图像 ⟦SLOT_34⟧ 的网页。为获得用于评测的修复代码 ⟦SLOT_35⟧，111 个网页被均分给五名博士生手工修复，每人耗时约 5 小时完成所分配样本的修复。三项任务的详细标注指南见我们的代码仓库22 2 https://github.com/WebPAI/DesignBench/blob/main/assets/Guideline.md。

**EN** 4.3. Data Annotation

**ZH** 4.3. 数据标注

<!-- [原子块 · img]  -->

**EN** Figure 3. The UI issue types in DesignBench. The red bounding box marks the issue location.

**ZH** 图 3. DesignBench 中的 UI 问题类型。红色边界框标出了问题所在位置。

**EN** Design Generation. The annotators are employed to annotate the topics of the webpages based on their functions.

**ZH** 设计生成。标注者依据网页的功能对其主题进行标注。

**EN** Design Edit. The annotators are instructed to annotate both the type and difficulty level of UI modifications. The modification type encompasses two dimensions: the operation type and the corresponding UI attribute type being adjusted. The operation types include three fundamental categories: Add (introducing new UI elements), Change (modifying elements), and Delete (removing elements). The UI attribute types subject to adjustment comprise six main categories: text (including content, font, and typography modifications), color (encompassing background colors, text colors, and accent colors), position (spatial arrangement and layout adjustments), size (dimensional scaling and resizing operations), shape (geometric modifications and structural changes), and component-level (holistic modifications affecting entire UI components). The difficulty level reflects several factors, primarily the number of UI elements that require adjustment, the complexity of the interdependencies between modified elements, and the scope of cascading changes required to maintain design consistency and functionality throughout the interface.

**ZH** 设计编辑。标注者需同时标注 UI 修改的类型与难度等级。修改类型涵盖两个维度：操作类型，以及被调整的 UI 属性类型。操作类型包括三个基本类别：Add（新增 UI 元素）、Change（修改元素）与 Delete（删除元素）。可被调整的 UI 属性类型包括六大类：text（文字，含内容、字体与排版修改）、color（颜色，含背景色、文字色与强调色）、position（位置，即空间排布与布局调整）、size（尺寸，即缩放与尺寸调整操作）、shape（形状，即几何修改与结构变化）与 component-level（组件级，即影响整个 UI 组件的整体性修改）。难度等级则综合多个因素：需要调整的 UI 元素数量、被修改元素之间依赖关系的复杂程度，以及为保持界面整体设计一致性与功能性所需的级联改动范围。

**EN** Design Repair. The annotators are employed to annotate the UI issues. After collecting the webpages with display issues, we first randomly select 25% samples for analysis and then discuss, revise, and refine the UI issue type until everyone reaches a consensus. During annotating new data, if encountering a new issue type, annotators will communicate and update issue type in time to guide subsequent annotations. Finally, we classify 6 types of UI display issues as follows:

**ZH** 设计修复。标注者负责标注 UI 问题。在收集到存在显示问题的网页后，我们先随机抽取 25% 的样本做分析，再经讨论、修订与细化，直至所有人对 UI 问题类型达成共识。标注新数据时若遇到新的问题类型，标注者会及时沟通并更新问题类型，以指导后续标注。最终，我们将 UI 显示问题归为以下 6 类：

**EN** • Occlusion. Elements are hidden or partially covered by other elements, making content inaccessible or invisible to users. This includes overlapping components, modal dialogs blocking content, or elements positioned behind others. As shown in Fig. 3(a). The “Doctor Name” box partially covers the portrait frame.

**ZH** • 遮挡（Occlusion）。元素被其他元素隐藏或部分覆盖，导致内容无法访问或不可见，包括组件重叠、模态对话框遮挡内容、元素被置于其他元素之后等。如图 3(a) 所示，「Doctor Name」框部分覆盖了头像框。

**EN** • Crowding. Too many elements are packed into a small space without adequate spacing, making the interface feel cluttered and difficult to navigate. Fig. 3(b) shows an example that the “Start Test” and “Reset” buttons are tightly packed together.

**ZH** • 拥挤（Crowding）。过多元素挤在狭小空间内且间距不足，使界面显得杂乱、难以浏览。图 3(b) 给出一例：「Start Test」与「Reset」两个按钮紧挨在一起。

**EN** • Text overlap. Text content overlaps with other text or UI elements, making it unreadable or causing visual confusion. Fig. 3(c) shows that the “AI Chat” text and “Support Bot” text are overlapped.

**ZH** • 文字重叠（Text overlap）。文字内容与其他文字或 UI 元素重叠，导致不可读或造成视觉混乱。图 3(c) 中，「AI Chat」与「Support Bot」两段文字相互重叠。

**EN** • Alignment. Elements are not properly aligned with each other or the overall layout grid, creating a disorganized appearance. As shown in Fig. 3(d), the “Feature 1” and “Feature 2” titles are not aligned with icons.

**ZH** • 对齐（Alignment）。元素之间或与整体布局网格未正确对齐，显得杂乱无序。如图 3(d) 所示，「Feature 1」与「Feature 2」两个标题未与图标对齐。

**EN** • Color and contrast. Poor color choices that affect readability or accessibility, including insufficient contrast between text and background, or color combinations that are difficult for users with visual impairments to distinguish. As illustrated in Fig. 3(e), the text color and background color are too close to each other, making it difficult to distinguish.

**ZH** • 颜色与对比度（Color and contrast）。配色选择不当影响可读性或无障碍性，包括文字与背景对比度不足，或所用颜色组合令视觉障碍用户难以分辨。如图 3(e) 所示，文字颜色与背景颜色过于接近，难以区分。

**EN** • Overflow. Content extends beyond its intended container boundaries, causing horizontal scrollbars, cut-off text, or elements appearing outside their designated areas. For example, the text “Don’t have an account” exceeds the login container.

**ZH** • 溢出（Overflow）。内容超出其容器边界，引发横向滚动条、文字截断或元素出现在指定区域之外。例如，「Don’t have an account」这段文字超出了登录容器。

**EN** 4.4. Benchmark Statistics

**ZH** 4.4. 基准统计

**EN** Table 2 presents the sample counts of the three tasks with three frameworks, the Vanilla denotes the webpage developed by vanilla HTML/CSS.

**ZH** 表 2 给出三项任务在三种框架下的样本数量，Vanilla 表示用原生 HTML/CSS 开发的网页。

**EN** Table 2. Sample counts of three frameworks on three tasks.

**ZH** 表 2. 三种框架在三项任务上的样本数量。

<!-- [原子块 · table] Framework Design Generation DesignEdit Design Repair React 109 108 28 Vue 118 105 27 Angular 83 66 28 Vanilla 120 80 28 Total 430 359 111 -->

<!-- [原子块 · object]  -->

**EN** (a) Topic Distribution.

**ZH** (a) 主题分布。

<!-- [原子块 · object]  -->

**EN** (b) Operation Distribution.

**ZH** (b) 操作分布。

<!-- [原子块 · object]  -->

**EN** (c) Visual Distribution.

**ZH** (c) 视觉分布。

<!-- [原子块 · object]  -->

**EN** (d) Issue Distribution.

**ZH** (d) 问题分布。

**EN** Figure 4. Type distribution of three tasks.

**ZH** 图 4. 三项任务的类型分布。

**EN** Fig. 4(a) shows that DesignBench covers a diverse range of web topics with more than 11 types, including information, homepage, tool, product, news, and so on. This extensive topic coverage demonstrates that DesignBench encompasses a broad range of aspects of digital interface design, ensuring comprehensive evaluation across different domain requirements.

**ZH** 图 4(a) 显示，DesignBench 覆盖的网页主题丰富，类型超过 11 种，包括信息、首页、工具、产品、新闻等。广泛的主题覆盖表明 DesignBench 囊括了数字界面设计的诸多方面，可针对不同领域需求做全面评测。

**EN** Fig. 4 shows the distribution of the edit type of design edit tasks. The operation distribution reveals three main categories: Change (55.8%), Add (38.1%), and Delete (6.1%). The corresponding visual modifications encompass diverse types, including component-level changes (27.9%), text modifications (17.1%), position adjustments (16.0%), color alterations (15.2%), shape modifications (13.4%), and size adjustments (10.4%), indicating that design edit tasks cover a broad spectrum of modification requirements.

**ZH** 图 4 展示了设计编辑任务的编辑类型分布。操作分布显示三大类别：Change（55.8%）、Add（38.1%）与 Delete（6.1%）。相应的视觉修改涵盖多种类型，包括组件级改动（27.9%）、文字修改（17.1%）、位置调整（16.0%）、颜色变更（15.2%）、形状修改（13.4%）与尺寸调整（10.4%），说明设计编辑任务覆盖了广泛的修改需求。

**EN** Fig. 4(d) shows the distribution of the UI issues. The issue types span multiple dimensions with alignment being most prevalent (42.2%), followed by crowding (18.7%), occlusion (18.1%), overflow (11.4%), and other visual defects. This wide range of issue types demonstrates that design repair tasks address comprehensive quality assurance across multiple design issues dimensions.

**ZH** 图 4(d) 展示 UI 问题的分布。问题类型横跨多个维度，其中对齐类最为普遍（42.2%），其后依次是拥挤（18.7%）、遮挡（18.1%）、溢出（11.4%）及其他视觉缺陷。如此多样的问题类型表明，设计修复任务在多个设计缺陷维度上实现了全面的质量保障覆盖。

**EN** 5. Experiment Setup

**ZH** 5. 实验设置

**EN** 5.1. Prompt Design

**ZH** 5.1. 提示设计

**EN** The simplified prompts for the three tasks are illustrated in Fig.5, with detailed prompts available in our code (Team, ). Our prompts are designed with the following structure: (1) background description: a concise scene setting statement (“You are a senior vue/react/angular developer", "You are tasked with generating/editting/repairing") primes the model for the correct role and task description; (2) detailed and specific task requirements: For design generation, exactly reproduce the screenshot: fonts, colors, layout, spacing. For design edit, surgically alter only the elements specified in the natural-language instruction while leaving all other visuals untouched. For design repair, identify and correct the listed UI defects (occlusion, crowding, overlap, alignment, color/contrast, overflow). (3) framework-specific coding conventions: the prompts guide the model to import available UI components and follow framework-specific coding conventions, with a generic example to reduce ambiguity; (4) output format instructions and examples, each prompt includes strict output format requirements to ensure that the generated code can be reliably extracted and evaluated.

**ZH** 三项任务的简化提示如图 5 所示，完整提示见我们的代码（Team，）。提示按以下结构设计：（1）背景描述：一句简洁的场景设定（「You are a senior vue/react/angular developer」「You are tasked with generating/editting/repairing」），让模型进入正确的角色与任务语境；（2）具体细致的任务要求：设计生成要求精确复现截图的字体、颜色、布局与间距；设计编辑要求只精准改动自然语言指令所指定的元素，其余视觉部分保持不变；设计修复要求识别并修正列出的 UI 缺陷（遮挡、拥挤、重叠、对齐、颜色/对比度、溢出）；（3）框架特有的编码规范：提示引导模型导入可用的 UI 组件并遵循框架特有的编码约定，同时给出一个通用示例以降低歧义；（4）输出格式要求与示例：每个提示都包含严格的输出格式规定，确保生成的代码可被稳定抽取与评测。

<!-- [原子块 · object]  -->

**EN** Figure 5. Prompts of design generation, edit and repair task.

**ZH** 图 5. 设计生成、编辑与修复任务的提示。

**EN** 5.2. Models

**ZH** 5.2. 模型

**EN** The studied MLLMs are listed in Table 4. We select six state-of-the-art LLMs that have been widely explored in multimodal tasks, three from open-source models, namely Pixtral (Agrawal et al., 2024), Qwen (Bai et al., 2025), and LLama (Meta, 2024), three from commercial models like Gemini (Google, 2024), GPT (OpenAI, 2024) and Claude (Anthropic, 2024). In configuring the MLLM models, we set the temperature to 0 and the maximum number of tokens output as the upper limit of MLLMs’ maximum output token. All other parameters are kept at their default settings. The detailed prompts of the three tasks are available in our code repository (Team, ). The entire benchmark evaluation incurs an average API cost of $52 per model on average. The average processing times per sample with a single thread, are 49 seconds for generation, 29 seconds for editing, and 25 seconds for repair, respectively.

**ZH** 所评测的多模态大语言模型列于表 4。我们选取六款在多模态任务中被广泛考察的先进大语言模型，其中三款开源——Pixtral（Agrawal 等，2024）、Qwen（Bai 等，2025）与 LLama（Meta，2024），三款商用——Gemini（Google，2024）、GPT（OpenAI，2024）与 Claude（Anthropic，2024）。模型配置方面，温度设为 0，最大输出 token 数取各模型输出上限，其余参数保持默认。三项任务的完整提示见我们的代码仓库（Team，）。整套基准评测的 API 开销平均每模型 52 美元。单线程下每个样本的平均处理时间为：生成 49 秒、编辑 29 秒、修复 25 秒。

**EN** 5.3. Data Contamination Check

**ZH** 5.3. 数据污染检查

**EN** First, in terms of the data source, we review the technical reports and training datasets of open source MLLMs. The training datasets for Qwen (Bai et al., 2025), Pixtral (Agrawal et al., 2024) and LLama (Meta, 2024) includes image captions, interleaved image-text data, optical character recognition (OCR) data, visual knowledge, crawling plain text and web document for Q&A, but not web html code. Furthermore, data leakage is particularly unlikely for design edit and design repair, because for design edit task, the training datasets don’t contain “<instruction, image, react/vue/angular/html code>” triple corpora. For design repair, there is no ground-truth repair labels are publicly available, as the benchmark is generated and verified by our annotators. To confirm that MLLMs are not “cheating” by memorizing and reproducing the original webpage code, we measure the BLEU score (Papineni et al., 2002) between the generated and original webpage code in the following table. The low BLEU score indicates that the model generates code from the design images rather than directly copying the original webpage.

**ZH** 首先，从数据来源看，我们核查了开源多模态大语言模型的技术报告与训练数据集。Qwen（Bai 等，2025）、Pixtral（Agrawal 等，2024）与 LLama（Meta，2024）的训练数据包含图像描述、图文交错数据、光学字符识别（OCR）数据、视觉知识，以及用于问答的爬取纯文本与网页文档，但不包含网页 HTML 代码。此外，设计编辑与设计修复任务几乎不可能发生数据泄露：就设计编辑而言，训练数据中不存在「<指令, 图像, react/vue/angular/html 代码>」三元组语料；就设计修复而言，由于该基准由我们的标注者生成并校验，公开渠道并无真值修复标签。为确认多模态大语言模型并非靠记忆复现原始网页代码，我们计算了生成代码与原始网页代码之间的 BLEU 分数（Papineni 等，2002），结果见下表。较低的 BLEU 分数说明，模型是依据设计图像生成代码，而非直接照抄原始网页。

**EN** Table 3. The BLEU score between original webpage code and generated code.

**ZH** 表 3. 原始网页代码与生成代码之间的 BLEU 分数。

<!-- [原子块 · table] Claude-3.7 GPT-4o Gemini-2.0 Llama-90B Llama-11B Pixtral-124B Pixtral-12B Qwen-72B Qwen-7B 0.1531 0.1318 0.1200 0.0771 0.0562 0.1117 0.1151 0.1338 0.0907 -->

**EN** 5.4. Metric

**ZH** 5.4. 评测指标

**EN** Visual Metrics. (1) CLIP (Radford et al., 2021) is applied to measure the semantic similarity between the generated and original webpages. (2) SSIM (Wang et al., 2004) (Structural Similarity Index Measure) score is applied to calculate the structure similarity. It evaluates the layout and compositional accuracy, emphasizing the spatial arrangement and structural similarities between the generated and original webpages.

**ZH** 视觉指标。（1）CLIP（Radford 等，2021）用于度量生成网页与原始网页之间的语义相似度。（2）SSIM（Wang 等，2004）（结构相似性指数）用于计算结构相似度，衡量布局与构成的准确度，侧重生成网页与原始网页在空间排布与结构上的相似性。

**EN** Code Metrics. (1) Compilation Success Rate (CSR). This metric represents the percentage of generated code that compiles successfully without errors. Assume that the total number of samples is N and the number of samples compiled successfully is S, then ⟦SLOT_36⟧. (2) Code Modification Location Similarity (CMLS). We employ the Jaccard similarity (Thada and Jaglan, 2013) to quantify the precision of code modifications on design edit and design repair tasks by comparing the sets of code modification operations between the ground truth and generated code. We first parse the code into an Abstract Syntax Tree (AST), and then identify the operation (i.e., add, delete and modify) by the AST node comparison. Let ⟦SLOT_37⟧ represent the set of code modification operations in the ground truth code and ⟦SLOT_38⟧ represent the set of code modification operations in the generated code. The CMLS is formally defined as: ⟦SLOT_39⟧. (3) Code Modification Content Similarity (CMCS). While CMLS focuses on modification locations, CMCS evaluates the semantic correctness of modified code content. Given modification operation sets ⟦SLOT_40⟧ and ⟦SLOT_41⟧, we match operations based on AST node correspondence and denote the matched pairs as ⟦SLOT_42⟧. For each ⟦SLOT_43⟧, CodeBLEU (ren2020codebleu) is used to compute content similarity, while unmatched operations receive a score of zero. The CMCS is defined as: ⟦SLOT_44⟧.

**ZH** 代码指标。（1）编译成功率（CSR）。该指标表示生成代码中能够无错编译的比例。设样本总数为 N，编译成功的样本数为 S，则 ⟦SLOT_36⟧。（2）代码修改位置相似度（CMLS）。我们采用 Jaccard 相似度（Thada 与 Jaglan，2013），通过比较真值代码与生成代码之间的代码修改操作集合，量化设计编辑与设计修复任务中代码修改的精度。先将代码解析为抽象语法树（AST），再通过 AST 节点比对识别操作类型（即增、删、改）。令 ⟦SLOT_37⟧ 表示真值代码中的代码修改操作集合，⟦SLOT_38⟧ 表示生成代码中的代码修改操作集合，CMLS 的形式化定义为：⟦SLOT_39⟧。（3）代码修改内容相似度（CMCS）。CMLS 关注修改位置，CMCS 则评估被修改代码内容的语义正确性。给定修改操作集合 ⟦SLOT_40⟧ 与 ⟦SLOT_41⟧，我们依据 AST 节点对应关系匹配操作，并将匹配对记为 ⟦SLOT_42⟧。对每个 ⟦SLOT_43⟧，用 CodeBLEU（ren2020codebleu）计算内容相似度，未匹配的操作记为零分。CMCS 定义为：⟦SLOT_44⟧。

**EN** MLLM-as-Judge Metrics. MLLMs have shown great performance in assisting judges across diverse modalities (Chen et al., 2024; Wang et al., 2025). Therefore, we prompt GPT-4o (OpenAI, 2024) to determine whether the model meets the user’s requirements on the design edit task and resolve the design issues on the design repair task, and output an MLLM score between 0 and 10 with detailed explanations (0-3 denotes the poor edit/repair, 4-6 denotes partial edit/repair, 7-8 denotes Good edit/repair and 9-10 denotes excellent edit/repair). The detailed judge prompts can be found in our repo33 3 https://github.com/WebPAI/DesignBench/blob/main/code/evaluator/metric.py. We employ the same five PhD students to conduct human validation studies to verify the reliability and consistency of our MLLM-as-Judge approach. Final validation are determined by majority voting. The Kappa score for inter-annotator agreement is 0.8648 and 0.8428 on design edit and repair task respectively, indicating "almost perfect" consensus. For design edit task, we sample 359 samples and validate this MLLM score through human evaluation, which can achieve an average accuracy of 95.54%. For design repair task, we sample 111 samples and validate this MLLM score through human evaluation, which can achieve an average accuracy of 91.89%.

**ZH** MLLM 即裁判指标。多模态大语言模型在跨模态辅助评判方面表现突出（Chen 等，2024；Wang 等，2025）。因此我们提示 GPT-4o（OpenAI，2024）判断模型在设计编辑任务上是否满足用户需求、在设计修复任务上是否解决了设计问题，并输出 0 到 10 之间的 MLLM 分数及详细解释（0-3 表示编辑/修复效果差，4-6 表示部分完成，7-8 表示良好，9-10 表示优秀）。详细的评判提示见我们的代码仓库33 3 https://github.com/WebPAI/DesignBench/blob/main/code/evaluator/metric.py。我们让同样的五名博士生做人工校验，验证该 MLLM 即裁判方法的可靠性与一致性，最终结果由多数投票确定。标注者间一致性的 Kappa 系数在设计编辑与修复任务上分别为 0.8648 与 0.8428，达到「几乎完全一致」的水平。设计编辑任务抽取 359 个样本做人工验证，该 MLLM 分数的平均准确率为 95.54%；设计修复任务抽取 111 个样本做人工验证，平均准确率为 91.89%。

**EN** Table 4. Studied Multimodal Large Language Models.

**ZH** 表 4. 所评测的多模态大语言模型。

<!-- [原子块 · table] Base Model Model Abbreviation Size Pixtral ( Agrawal et al., 2024 ) Pixtral-12B-2409 Pixtral-12B 12B Pixtral ( Agrawal et al., 2024 ) Pixtral-large-latest Pixtral-124B 124B Qwen ( Bai et al., 2025 ) Q -->

**EN** 5.5. Research Questions

**ZH** 5.5. 研究问题

**EN** • RQ1: (Performance across tasks) How do MLLMs perform across distinct front-end tasks?

**ZH** • RQ1：（跨任务表现）多模态大语言模型在各项前端任务上的表现如何？

**EN** • RQ2: (Performance across frameworks) What is the comparative performance of MLLMs when applied to different development frameworks?

**ZH** • RQ2：（跨框架表现）面对不同开发框架时，多模态大语言模型的表现有何差异？

**EN** • RQ3: (Difficulty Influence) How does varying task difficulty impact MLLM performance?

**ZH** • RQ3：（难度影响）任务难度变化会如何影响多模态大语言模型的表现？

**EN** • RQ4: (Context Influence) To what extent do different input contexts affect MLLMs’ performance?

**ZH** • RQ4：（上下文影响）不同输入上下文在多大程度上影响多模态大语言模型的表现？

**EN** • RQ5: (Limitation analysis) What are the primary limitations of MLLMs in developing framework-based webpages?

**ZH** • RQ5：（局限性分析）多模态大语言模型在基于框架的网页开发中的主要局限是什么？

**EN** • RQ6: (Failure analysis) What mistakes do MLLMs make on the three tasks?

**ZH** • RQ6：（失败分析）多模态大语言模型在三项任务上会犯哪些错误？

**EN** 6. Experiment Results

**ZH** 6. 实验结果

**EN** Table 5. The model performance on DesignBench under different tasks and different frameworks. Bold numbers on a dark red background indicate the maximum values, and an underline with a light red background denotes the second-best value.

**ZH** 表 5. 各模型在 DesignBench 上不同任务、不同框架下的表现。深红底加粗数字表示最大值，浅红底加下划线表示次优值。

<!-- [原子块 · table] Metric Framework Claude GPT Gemini Llama Pixtral Qwen Claude-3.7 GPT-4o Gemini-2.0 Llama-90B Llama-11B Pixtral-124B Pixtral-12B Qwen-72B Qwen-7B Design Generation CLIP React 0.8083 0.7637 0.7611 0.704 -->

**EN** 6.1. RQ1: How do MLLMs perform across distinct front-end tasks?

**ZH** 6.1. RQ1：多模态大语言模型在各项前端任务上的表现如何？

**EN** Table 5 presents the performance of nine MLLMs on three tasks in three front-end frameworks React, Vue, and Angular. Vanilla denotes the webpage developed by vanilla HTML/CSS.

**ZH** 表 5 给出九款多模态大语言模型在 React、Vue、Angular 三种前端框架下三项任务上的表现。Vanilla 表示用原生 HTML/CSS 开发的网页。

**EN** Among all, Claude-3.7, GPT-4o, Gemini-2.0, and Pixtral-124B are the top-performing MLLMs in three tasks. Claude-3.7 achieves the highest performance across most metrics, including superior CLIP scores (0.6024-0.8319) for Design Generation and exceptional MLLM scores for Design Edit (8.01-9.15) and Design Repair (6.59-7.17). GPT-4o follows closely with strong CLIP scores (0.5963-0.7734) and outstanding compilation rates (0.7108-0.9725), alongside competitive MLLM scores across all tasks. Gemini-2.0 demonstrates solid performance with CLIP scores ranging from 0.6006-0.7611, reliable compilation success rates consistently above 0.71, and strong MLLM scores in Design Edit (7.81-9.13) and Design Repair (5.28-7.32). Pixtral-124B rounds out the top tier with competitive performance across multiple metrics, achieving strong CLIP scores (0.6324-0.7811), excellent compilation rates (0.7590-0.9746), and robust MLLM scores for Design Edit (8.01-9.11) and Design Repair (6.37-6.96).

**ZH** 在所有模型中，Claude-3.7、GPT-4o、Gemini-2.0 与 Pixtral-124B 在三项任务上表现最好。Claude-3.7 在多数指标上居首，包括设计生成上最优的 CLIP 分数（0.6024-0.8319），以及设计编辑（8.01-9.15）与设计修复（6.59-7.17）上出色的 MLLM 分数。GPT-4o 紧随其后，CLIP 分数（0.5963-0.7734）与编译率（0.7108-0.9725）表现突出，各任务的 MLLM 分数也具竞争力。Gemini-2.0 表现稳健，CLIP 分数在 0.6006-0.7611 之间，编译成功率稳定在 0.71 以上，设计编辑（7.81-9.13）与设计修复（5.28-7.32）的 MLLM 分数同样亮眼。Pixtral-124B 则在多个指标上具备竞争力，构成第一梯队：CLIP 分数 0.6324-0.7811，编译率 0.7590-0.9746，设计编辑（8.01-9.11）与设计修复（6.37-6.96）的 MLLM 分数也较为稳健。

<!-- [原子块 · svg]  -->

**EN** Larger variants consistently outperform their smaller counterparts within the same family. This is evident in comparisons such as Llama-90B versus Llama-11B, Pixtral-124B versus Pixtral-12B, and Qwen-72B versus Qwen-7B comparisons. The performance advantages are particularly pronounced in complex tasks requiring code localization and visual understanding, suggesting that increased model capacity enhances essential web development capabilities.

**ZH** 同一系列中，大参数版本始终优于小参数版本，Llama-90B 对 Llama-11B、Pixtral-124B 对 Pixtral-12B、Qwen-72B 对 Qwen-7B 的对比均印证了这一点。在需要代码定位与视觉理解的复杂任务上，这种优势尤为明显，说明模型容量的提升能强化 Web 开发所需的关键能力。

<!-- [原子块 · svg]  -->

**EN** In Design Generation tasks, MLLMs face two primary bottlenecks: compilation errors and visual inaccuracies. The compilation rates reveal significant framework-dependent challenges, with Angular showing the lowest success rates (0.6867-0.7590 for top models) compared to React and Vue (⟦SLOT_45⟧0.83 for top models). Additionally, the moderate CLIP scores (0.5963-0.6324 even for best performers) indicate substantial room for improvement in generating visually accurate webpage layouts. The performance gap between vanilla HTML (highest CLIP scores) and framework-based implementations further suggests that the syntactic complexity in modern frameworks exacerbates challenges in both compilation and visual rendering.

**ZH** 在设计生成任务中，多模态大语言模型面临两大瓶颈：编译错误与视觉偏差。编译率显示出明显的框架差异，Angular 的成功率最低（顶尖模型为 0.6867-0.7590），低于 React 与 Vue（顶尖模型 ⟦SLOT_45⟧0.83）。此外，即便是最优模型，CLIP 分数也只处在中等水平（0.5963-0.6324），说明生成视觉准确的网页布局仍有较大的提升空间。原生 HTML（CLIP 分数最高）与基于框架的实现之间存在性能落差，进一步表明现代框架的语法复杂性加剧了编译与视觉渲染两方面的困难。

**EN** In the Design Edit and Design Repair tasks, the primary bottleneck for MLLMs lies in accurately localizing and modifying the code segments that require changes. This limitation is reflected by the substantially lower CMLS and CMCS scores compared to compilation success rates across all models. In the Design Edit task, even top-performing models such as Claude-3.7 achieve CMLS scores of only 0.5555–0.7696 and CMCS scores of 0.4551–0.7080. A similar trend is observed in the Design Repair task, where Claude-3.7 attains CMLS values ranging from 0.5089 to 0.6759 and CMCS values from 0.3924 to 0.5859. These results indicate that, despite generating code that successfully compiles, MLLMs still struggle to precisely identify and semantically modify the target code regions.

**ZH** 在设计编辑与设计修复任务中，模型的主要瓶颈在于准确定位并修改需要改动的代码片段。与编译成功率相比，各模型的 CMLS 与 CMCS 分数明显偏低，正反映了这一局限。设计编辑任务中，即便 Claude-3.7 这样的顶尖模型，CMLS 也仅为 0.5555–0.7696，CMCS 为 0.4551–0.7080。设计修复任务呈现同样的趋势：Claude-3.7 的 CMLS 在 0.5089 至 0.6759 之间，CMCS 在 0.3924 至 0.5859 之间。这些结果说明，模型虽然能生成可编译的代码，却仍难以精确识别目标代码区域并做出语义正确的修改。

<!-- [原子块 · svg]  -->

**EN** 6.2. RQ2: What is the comparative performance of MLLMs when applied to different development frameworks?

**ZH** 6.2. RQ2：面对不同开发框架时，多模态大语言模型的表现有何差异？

<!-- [原子块 · img]  -->

**EN** (a) CLIP.

**ZH** (a) CLIP。

<!-- [原子块 · img]  -->

**EN** (b) Compilation.

**ZH** (b) 编译率。

**EN** Figure 6. Performance of webpages implemented by different frameworks. y-axis denotes the framework used to actually implement the webpage and x-axis represents the framework used by the model.

**ZH** 图 6. 采用不同框架实现的网页上的表现。y 轴表示实际用于实现网页的框架，x 轴表示模型所使用的框架。

**EN** To further explore the model’s proficiency across different front-end frameworks, we evaluate MLLMs’ ability to implement webpages using various framework combinations.

**ZH** 为进一步考察模型对不同前端框架的掌握程度，我们评测了多模态大语言模型在各种框架组合下实现网页的能力。

**EN** Fig. 6 presents the average CLIP scores and compilation success rates of nine MLLMs across different framework combinations. The results reveal distinct performance patterns across frameworks. MLLMs consistently achieve optimal performance when implementing webpages using vanilla HTML/CSS, attaining the highest CLIP scores above 0.72 and perfect compilation success rates. In contrast, Angular-based implementations demonstrate the poorest performance, with compilation success rates ranging from 0.6-0.7 and CLIP scores between 0.45-0.55. React and Vue frameworks show intermediate performance levels, with both achieving reasonable compilation rates and moderate CLIP scores, though still inferior to vanilla implementations.

**ZH** 图 6 给出九款多模态大语言模型在不同框架组合下的平均 CLIP 分数与编译成功率，结果呈现出清晰的框架差异。模型在使用原生 HTML/CSS 实现网页时表现最佳，CLIP 分数最高（0.72 以上）且编译成功率达到满分。相比之下，基于 Angular 的实现表现最差，编译成功率在 0.6-0.7 之间，CLIP 分数在 0.45-0.55 之间。React 与 Vue 处于中间水平，编译率尚可、CLIP 分数中等，但仍不及原生实现。

<!-- [原子块 · svg]  -->

**EN** 6.3. RQ3: How does varying task difficulty impact MLLM performance?

**ZH** 6.3. RQ3：任务难度变化会如何影响多模态大语言模型的表现？

**EN** Table 6. Performance under different difficulty levels.

**ZH** 表 6. 不同难度层级下的表现。

<!-- [原子块 · table] Model Design Generation Design Edit Design Repair Easy Medium Hard Easy Medium Hard Easy Medium Hard Claude-3.7 0.86 0.77 0.51 8.64 8.32 7.61 7.21 6.81 6.93 GPT-4o 0.84 0.74 0.43 8.73 7.95 8.19 6.93 6 -->

**EN** We categorize samples into different difficulty levels to systematically evaluate MLLMs’ performance across varying complexity scenarios.

**ZH** 我们把样本划分到不同的难度层级，以便系统评估多模态大语言模型在不同复杂度场景下的表现。

**EN** For Design Generation task, which requires generating code from scratch, we calculate the complexity based on the image size ⟦SLOT_46⟧, UI elements number ⟦SLOT_47⟧, color variety ⟦SLOT_48⟧ (i.e., the number of colors in the UI) and layout complexity ⟦SLOT_49⟧ (i.e., number of layout methods + number of nesting levels + number of CSS layout attributes). We then normalize these scores to between 0 and 100. The complexity score: ⟦SLOT_50⟧. Scores greater than 80 are complex, less than 30 are simple, and between 30 and 80 are medium.

**ZH** 设计生成任务要求从零生成代码，我们基于图像尺寸 ⟦SLOT_46⟧、UI 元素数量 ⟦SLOT_47⟧、色彩丰富度 ⟦SLOT_48⟧（即 UI 中颜色的数量）与布局复杂度 ⟦SLOT_49⟧（即布局方式数量 + 嵌套层级数 + CSS 布局属性数量）计算复杂度，再把这些分数归一化到 0 至 100 之间。复杂度分数为：⟦SLOT_50⟧。分数大于 80 为困难，小于 30 为简单，介于 30 与 80 之间为中等。

**EN** In Design Edit task, where models must modify existing code according to user instructions, difficulty correlates with the complexity and scope of the modification instructions. We adopt the annotator-provided difficulty labels from Section 4.3 as our ground truth difficulty classification.

**ZH** 设计编辑任务要求模型依据用户指令修改已有代码，其难度与修改指令的复杂度和影响范围相关。我们直接采用 4.3 节中标注者给出的难度标签作为真值难度分级。

**EN** For Design Repair task, difficulty is assessed based on the severity of UI issues, quantified by the extent of code modifications required to resolve the identified problems. Tasks requiring modifications to more than 30 lines of code are classified as hard, those requiring fewer than 10 lines as easy, and intermediate cases as medium difficulty.

**ZH** 设计修复任务的难度依据 UI 问题的严重程度评估，以解决所识别问题所需的代码修改量来量化。需要修改 30 行以上代码的任务归为困难，少于 10 行的归为简单，介于两者之间为中等难度。

**EN** Table 6 shows the CLIP score for Design Generation task and MLLM score for Design Edit and Design Repair task under different difficulty levels.

**ZH** 表 6 给出不同难度层级下设计生成任务的 CLIP 分数，以及设计编辑与设计修复任务的 MLLM 分数。

**EN** Table 6 reveals distinct difficulty-related performance patterns across the three design tasks. In Design Generation, where difficulty stems from image complexity and size, top models show moderate degradation from 0.79-0.83 (Easy) to 0.69-0.73 (Hard). Design Edit tasks, with difficulty determined by the number of required operations, exhibit more pronounced drops, particularly for complex multi-operation scenarios where top models decline from 8.64-9.05 to 7.51-8.19. Design Repair shows the most severe degradation, where UI issue severity and required code modifications cause performance to plummet from 6.93-7.21 (Easy) to 4.19-6.93 (Hard), with smaller models experiencing catastrophic failures. These patterns indicate that visual complexity moderately affects generation, operational complexity significantly impacts editing, while code-level debugging presents the steepest performance barriers for current MLLMs.

**ZH** 表 6 揭示出三项设计任务各自不同的难度相关表现规律。设计生成的难度来自图像复杂度与尺寸，顶尖模型从简单（0.79-0.83）到困难（0.69-0.73）呈中等幅度下滑。设计编辑的难度由所需操作数量决定，下滑更为明显，尤其在需要多步操作的复杂场景下，顶尖模型从 8.64-9.05 降至 7.51-8.19。设计修复的下滑最为剧烈：UI 问题严重程度与所需代码修改量使表现从简单（6.93-7.21）骤降至困难（4.19-6.93），小参数模型甚至出现灾难性失败。这些规律说明，视觉复杂度对生成影响适中，操作复杂度显著影响编辑，而代码级调试则是当前多模态大语言模型面前最陡峭的性能壁垒。

<!-- [原子块 · svg]  -->

**EN** 6.4. RQ4: To what extent do different input contexts affect MLLMs’ performance?

**ZH** 6.4. RQ4：不同输入上下文在多大程度上影响多模态大语言模型的表现？

**EN** For the Design Edit and Design Repair tasks, we explore the impact of input images and codes on the results. Table 7 shows the MLLM score on in Design Edit and Design Repair tasks under different context inputs. The results reveal distinct patterns regarding the utility of visual versus code information across different models and tasks.

**ZH** 针对设计编辑与设计修复任务，我们考察输入图像与输入代码对结果的影响。表 7 给出两项任务在不同上下文输入下的 MLLM 分数，结果显示出视觉信息与代码信息在不同模型、不同任务上各自的价值规律。

**EN** Code-only input consistently outperforms image-only input across both tasks and all models. For Design Edit, top models (Claude-3.7, GPT-4o, Gemini-2.0) achieve highest scores with code-only input (8.40-8.43) versus image-only (7.37-7.67). Design Repair shows similar code-only superiority (6.53-6.70 vs 5.47-5.81 for top models).

**ZH** 在两项任务、所有模型上，纯代码输入始终优于纯图像输入。设计编辑任务中，顶尖模型（Claude-3.7、GPT-4o、Gemini-2.0）在纯代码输入下得分最高（8.40-8.43），而纯图像输入为 7.37-7.67。设计修复任务同样呈现纯代码优势（顶尖模型 6.53-6.70 对 5.47-5.81）。

**EN** However, combining code and image inputs does not yield significant improvements and occasionally results in minor performance degradation, highlighting the limitations of MLLMs in accurately localizing modification points and identifying UI issues through visual analysis.

**ZH** 然而，把代码与图像同时输入并未带来显著提升，有时甚至造成轻微的性能下降，这凸显出多模态大语言模型在通过视觉分析准确定位修改点、识别 UI 问题方面的局限。

**EN** Table 7. Performance under different context inputs. Both denote combining image and code.

**ZH** 表 7. 不同上下文输入下的表现。Both 表示图像与代码组合输入。

<!-- [原子块 · table] Model Design Edit Design Repair Image Code Both Image Code Both Claude-3.7 7.6764 8.4326 8.4258 5.8142 6.7014 6.8535 GPT-4o 7.3728 8.4013 8.4258 5.6968 6.5304 6.4041 Gemini-2.0 7.6430 8.4105 8.5083 5. -->

<!-- [原子块 · svg]  -->

**EN** 6.5. RQ5: The limitations of MLLMs when developing framework-based webpages?

**ZH** 6.5. RQ5：多模态大语言模型开发基于框架的网页时存在哪些局限？

**EN** 6.5.1. Compilation Errors

**ZH** 6.5.1. 编译错误

**EN** The compilation error indicates that MLLM does not sufficiently understand the syntax of framework-based front-end development. As illustrated in Figure 7, different MLLMs exhibit distinct error patterns across frameworks, revealing specific weaknesses in their understanding of front-end development syntax.

**ZH** 编译错误说明多模态大语言模型对基于框架的前端开发语法理解不足。如图 7 所示，不同模型在各框架上呈现出不同的错误模式，暴露出它们在前端开发语法理解上的具体短板。

**EN** In React development, the top three errors are “Unexpected Token”, “Expression Expected”, and “Use Client Missing”, with Qwen-7B producing the highest number of compilation errors (95 total) while GPT-4o demonstrates superior performance with only 3 total errors. For Vue development, “Missing End Tag”, “Unexpected EOF”, and “Attribute Error” are dominated errors. Qwen-7B shows the most compilation issues (102), while Claude-3.7 achieves near-perfect compilation success with just 1 error. Angular development presents a different error profile, with “Incomplete Block”, “Component Import Error”, and “Component Export Error” as the primary issues. Qwen-7B continues to struggle with 73 total errors, while Pixtral-124B shows the best performance.

**ZH** 在 React 开发中，出现最多的三类错误是「Unexpected Token」「Expression Expected」与「Use Client Missing」，其中 Qwen-7B 的编译错误最多（共 95 处），GPT-4o 表现最好，仅 3 处。Vue 开发中，主要错误是「Missing End Tag」「Unexpected EOF」与「Attribute Error」，Qwen-7B 问题最多（102 处），Claude-3.7 几乎完全编译成功，仅 1 处错误。Angular 开发的错误构成不同，主要是「Incomplete Block」「Component Import Error」与「Component Export Error」，Qwen-7B 依然吃力（共 73 处），Pixtral-124B 表现最佳。

<!-- [原子块 · object]  -->

**EN** (a) React.

**ZH** (a) React。

<!-- [原子块 · object]  -->

**EN** (b) Vue.

**ZH** (b) Vue。

<!-- [原子块 · object]  -->

**EN** (c) Angular.

**ZH** (c) Angular。

**EN** Figure 7. Compilation error distribution.

**ZH** 图 7. 编译错误分布。

**EN** The error distribution reveals that MLLMs face distinct limitations when working with different frameworks: they struggle with JSX syntax parsing and React-specific expressions in React applications, encounter difficulties with template structure and attribute handling in Vue development, and show inadequate understanding of TypeScript module systems and component architecture in Angular projects. Advanced models like GPT-4o, Claude-3.7, and Pixtral-124B consistently demonstrate superior syntax understanding.

**ZH** 错误分布表明，多模态大语言模型在处理不同框架时面临各自的局限：React 应用中难以解析 JSX 语法与 React 特有的表达式；Vue 开发中在模板结构与属性处理上存在困难；Angular 项目中对 TypeScript 模块系统与组件架构理解不足。GPT-4o、Claude-3.7 与 Pixtral-124B 等先进模型则始终表现出更优的语法理解能力。

<!-- [原子块 · svg]  -->

**EN** To verify MLLM’s ability to solve compilation errors, we sample 30 webpages with diverse compilation errors and prompt MLLMs to fix them. The results are shown in the Table 9. The overall average repair rate across all models and frameworks is 0.53, indicating that MLLMs still face challenges in fixing front-end errors.

**ZH** 为验证多模态大语言模型解决编译错误的能力，我们抽取 30 个带有各类编译错误的网页，提示模型加以修复，结果见表 9。所有模型与框架的平均修复率为 0.53，说明模型在修复前端错误上仍面临挑战。

**EN** Table 8. Compile error fix ratio.

**ZH** 表 8. 编译错误修复比例。

<!-- [原子块 · table] Model React Vue Angular Claude-3.7 0.70 0.40 0.70 GPT-4o 0.60 0.50 0.50 Gemini-2.0 0.60 0.80 0.80 Llama-90B 0.50 0.60 0.80 Llama-11B 0.30 0.50 0.20 Pixtral-124B 0.70 0.70 0.70 Pixtral-12B 0.50 0.60 0. -->

**EN** Table 9. Ratio of using component-based design.

**ZH** 表 9. 采用组件化设计的比例。

<!-- [原子块 · table] Model React Vue Angular Claude-3.7 0.23% 6% 38% GPT-4o 0.71% 6.3% 10% Gemini-2.0 0.7% 0.23% 41% Llama-90B 0% 2% 5% Llama-11B 0.48% 0.47% 1.3% Pixtral-124B 0% 5.3% 7.7% Pixtral-12B 0% 1.4% 2.3% Qwen-72 -->

**EN** 6.5.2. Component-based Implementation Limitation

**ZH** 6.5.2. 组件化实现局限

**EN** Component-based design is a method of breaking down user interfaces into reusable, self-contained parts called components. This approach improves efficiency and scalability in website development. Table 9 shows the proportion of webpages implemented by MLLMs using component-based design across three frameworks. The result reveals that MLLMs demonstrate remarkably low adoption rates of component-based implementation, with average 0.24%, 5% and 19% rate on React, Vue and Angular, respectively.

**ZH** 组件化设计把用户界面拆分为可复用、自包含的部件（即组件），这种方式能提升网站开发的效率与可扩展性。表 9 给出各模型在三种框架下采用组件化设计实现的网页比例。结果显示，模型对组件化实现的采用率极低，在 React、Vue、Angular 上平均仅为 0.24%、5% 与 19%。

**EN** Case Study. Fig. 8 shows a screenshot of the BBC website’s recently live section. Each news item follows an identical structure, making it ideal for component-based implementation with iterative rendering. However, as shown in Listing 1, the Vue code generated by MLLMs contains hardcoded, repetitive structures instead of utilizing Vue’s v-for directive. This reveals MLLMs’ insufficient understanding of component-based architecture and framework-specific syntax.

**ZH** 案例分析。图 8 是 BBC 网站 recently live 栏目的截图。每条新闻结构完全相同，本应采用组件化实现配合迭代渲染。然而如清单 1 所示，模型生成的 Vue 代码却是硬编码的重复结构，并未使用 Vue 的 v-for 指令。这反映出多模态大语言模型对组件化架构与框架特有语法的理解不足。

<!-- [原子块 · img]  -->

**EN** Figure 8. A webpage with multiple elements of the same structure and style.

**ZH** 图 8. 含多个同结构、同样式元素的网页。

**EN** Listing 1: Vue implementation containing repeated items.

**ZH** 清单 1：包含重复条目的 Vue 实现。

<!-- [原子块 · svg]  -->

**EN** 6.5.3. Issue Detection Limitation

**ZH** 6.5.3. 问题检测局限

**EN** In Design Repair task, we also prompt MLLMs to judge the UI display issues described in Section 4.3. Then we calculate the issue detection accuracy by comparing the MLLMs’ outputs with the ground truth annotated by human experts. Table 10 presents the UI issue detection accuracy across different MLLM models. The results demonstrate consistently poor performance of MLLMs in identifying UI issues, with average 0.2972, 0.2205 and 0.2275, 0.3403 rate on React, Vue, Angular and Vanilla, respectively.

**ZH** 在设计修复任务中，我们还提示多模态大语言模型判断 4.3 节所述的 UI 显示问题，再把模型输出与人类专家标注的真值比对，计算问题检测准确率。表 10 给出各模型的 UI 问题检测准确率。结果显示，模型识别 UI 问题的表现始终不佳，在 React、Vue、Angular 与 Vanilla 上的平均准确率分别为 0.2972、0.2205、0.2275 与 0.3403。

**EN** Table 10. UI Issue Identification Accuracy of different MLLMs.

**ZH** 表 10. 各多模态大语言模型的 UI 问题识别准确率。

<!-- [原子块 · table] Model React Vue Angular Vanilla Average Claude-3.7 0.4155 0.2654 0.3929 0.4286 0.3756 GPT-4o 0.4369 0.2870 0.4101 0.4464 0.3951 Gemini-2.0 0.4250 0.3210 0.2649 0.5417 0.3882 Llama-90B 0.2827 0.3735 0. -->

<!-- [原子块 · svg]  -->

**EN** 6.6. RQ6: What mistakes do MLLMs make on the three tasks?

**ZH** 6.6. RQ6：多模态大语言模型在三项任务上会犯哪些错误？

**EN** We conduct systematic error analysis by randomly selecting 25% of results for examination. The annotation process involves iterative discussion and refinement of failure categories until consensus is reached, with continuous communication to identify emerging failure types during annotation.

**ZH** 我们随机抽取 25% 的结果做系统的错误分析。标注过程包括对失败类别的迭代讨论与细化，直至达成共识，并在标注中保持持续沟通，以及时发现新出现的失败类型。

**EN** For the design generation task, we define seven failure categories: (1) Compile error: generated code cannot be compiled successfully; (2) Layout disorder: UI arrangement deviates from the reference design; (3) Element missing: essential UI components are absent; (4-7) Element attribute errors: wrong position, color, text content, or size of UI elements. For design edit and repair tasks, we establish six failure types: (1) Compile error: modified code contains compilation errors; (2) No edit/repair: models make no modifications; (3) Wrong objects: models target incorrect elements; (4) Wrong edit/repair: models apply inappropriate modifications to correct elements; (5) Partial edit/repair: incomplete implementation of required changes; (6) Unnecessary modification: extraneous adjustments beyond specified requirements. The detailed annotation guideline and failure type examples are in our repo44 4 https://github.com/WebPAI/DesignBench/blob/main/assets/Failure_Annotation_Guideline.md.

**ZH** 针对设计生成任务，我们定义七类失败：（1）编译错误：生成的代码无法成功编译；（2）布局错乱：UI 排布偏离参考设计；（3）元素缺失：缺少必要的 UI 组件；（4-7）元素属性错误：UI 元素的位置、颜色、文字内容或尺寸有误。针对设计编辑与修复任务，我们确立六类失败：（1）编译错误：修改后的代码存在编译错误；（2）未编辑/未修复：模型未做任何修改；（3）对象错误：模型定位到错误的元素；（4）编辑/修复错误：模型对正确的元素施加了不当的修改；（5）编辑/修复不全：所需改动未完整实现；（6）多余修改：超出规定范围做了额外调整。详细的标注指南与失败类型示例见我们的代码仓库44 4 https://github.com/WebPAI/DesignBench/blob/main/assets/Failure_Annotation_Guideline.md。

<!-- [原子块 · object]  -->

**EN** (a) Design Generation.

**ZH** (a) 设计生成。

<!-- [原子块 · object]  -->

**EN** (b) Design Edit.

**ZH** (b) 设计编辑。

<!-- [原子块 · object]  -->

**EN** (c) Design Repair.

**ZH** (c) 设计修复。

**EN** Figure 9. Failure type distribution on three tasks of different MLLMs.

**ZH** 图 9. 各多模态大语言模型在三项任务上的失败类型分布。

<!-- [原子块 · svg]  -->

**EN** From Figure 9, we observe distinct failure patterns across tasks: (1) Design generation tasks are dominated by spatial and structural failures, with "wrong element size," "element missing," and "wrong element position" as the top three failure types, revealing MLLMs’ limitations in layout comprehension and spatial reasoning. (2) Design edit tasks show more controlled failure modes, with "unnecessary modifications," "partial edits," and "wrong edits" as primary concerns, indicating challenges in precise instruction following and modification scope control. (3) Design repair tasks exhibit the most severe limitations, with "no repair," "wrong repairs," and "partial repairs" as dominant failure types, demonstrating fundamental difficulties in defect identification and corrective action formulation.

**ZH** 从图 9 可看出各任务不同的失败模式：（1）设计生成任务以空间与结构类失败为主，「元素尺寸错误」「元素缺失」「元素位置错误」位居前三，暴露出多模态大语言模型在布局理解与空间推理上的不足。（2）设计编辑任务的失败形态相对可控，主要是「多余修改」「编辑不全」与「编辑错误」，反映模型在精确遵循指令与把控修改范围上存在困难。（3）设计修复任务的局限最为严重，「未修复」「修复错误」与「修复不全」占主导，说明模型在缺陷识别与制定纠正措施上存在根本性困难。

**EN** 7. Threats to Validity

**ZH** 7. 有效性威胁

**EN** Internal validity. (1) The MLLM-as-a-judge scores may have reliability concerns. To eliminate this, we carefully design the prompt and provide the model with a detailed guideline of evaluation criteria. The results of human evaluation in Section 5.4 also verified that the accuracy of MLLM’s score is above 90%. (2) Potential data leakage. Half of the webpages in our benchmark are sourced from closed applications (e.g., top 500 websites by Moz (42)), and the ground truth for design repair tasks is manually written by developers, minimizing data leakage risks. Moreover, the poor framework-based code generation performance, evident in syntax errors and limited use of framework-specific features, suggests that MLLM results in the benchmark are unlikely due to mere data memorization. We also demonstrate that there is a low risk of data contamination in Section 5.3.

**ZH** 内部有效性。（1）MLLM 即裁判的评分可能存在可靠性问题。为此我们精心设计提示，并向模型提供详尽的评判标准指南。5.4 节的人工评测结果也验证了 MLLM 评分的准确率在 90% 以上。（2）潜在的数据泄露。本基准中半数网页来自闭源应用（如 Moz（42）排名前 500 的网站），设计修复任务的真值由开发者手工编写，把数据泄露风险降到最低。此外，基于框架的代码生成表现不佳——语法错误频发、框架特有特性使用有限——也说明模型在本基准上的结果不太可能仅源于数据记忆。5.3 节同样论证了数据污染风险较低。

**EN** External validity. We only include limited frameworks of React, Vue, and Angular, due to their dominance in modern web development. These frameworks represent the majority of contemporary applications and offer diverse programming paradigms: from React’s JSX to Vue’s templates and Angular’s TypeScript approach, providing comprehensive evaluation coverage.

**ZH** 外部有效性。我们只纳入 React、Vue 与 Angular 这三种框架，因为它们在当代 Web 开发中占据主导地位。这些框架覆盖了当前应用的绝大部分，并提供多样的编程范式——从 React 的 JSX 到 Vue 的模板，再到 Angular 的 TypeScript 路线，从而提供了较为全面的评测覆盖。

**EN** 8. Discussion

**ZH** 8. 讨论

**EN** We elicit several actionable advice from our findings for researchers and developers in this field. (1) For researchers: (i) Enhance framework-specific MLLM training. The poor performance on framework-specific syntax and component-based implementations underscores the need for MLLM training datasets enriched with modern web development patterns and framework-specific best practices. This would improve their practical value for applying to diverse front-end ecosystems. (ii) Improve multimodal information fusion for UI tasks. Our findings reveal that for design edit and repair tasks, single code input and multimodal input perform equally well, suggesting that MLLMs currently underutilize visual information. Future work should prioritize developing more effective visual-code alignment for multimodal reasoning in front-end jobs.

**ZH** 基于上述发现，我们为领域内的研究者与开发者提炼出若干可操作的建议。（1）面向研究者：（i）加强面向框架的多模态大语言模型训练。模型在框架特有语法与组件化实现上的糟糕表现说明，训练数据中需要补充现代 Web 开发模式与框架最佳实践，以提升模型适配多样前端生态的实用价值。（ii）改进 UI 任务中的多模态信息融合。我们发现，在设计编辑与修复任务上，单一代码输入与多模态输入效果相当，说明模型目前未能充分利用视觉信息。后续工作应优先研究更有效的视觉—代码对齐机制，以支撑前端场景中的多模态推理。

**EN** (2) For developers: (i) Provide code edit location information for Design Edit and Design Repair tasks. Since MLLMs struggle with code localization, providing exact locations for edits or repairs would significantly enhance performance and reduce the cognitive burden on models to identify relevant code segments. (ii) Clearly state the repair issues for repair tasks. Given MLLMs’ low accuracy in UI issue identification, explicitly stating the problems allows models to focus on targeted solutions rather than inaccurate independent diagnosis. (iii) Decompose complex instructions and large designs. Given that MLLM performance degrades with complex instructions and large UI mockups, practitioners can improve the practicality by breaking down complex requirements into simpler, atomic tasks and segmenting large UI designs into smaller, manageable components.

**ZH** （2）面向开发者：（i）为设计编辑与设计修复任务提供代码修改位置信息。既然模型不擅长代码定位，直接给出编辑或修复的确切位置可显著提升表现，也免去模型自行检索相关代码段的负担。（ii）在修复任务中明确说明问题所在。鉴于模型识别 UI 问题的准确率偏低，明确指出问题可让模型专注于针对性的求解，避免自行做出不准确的诊断。（iii）拆分复杂指令与大型设计稿。模型表现会随指令复杂度与 UI 设计稿尺寸上升而下降，实践中可把复杂需求拆解为更简单的原子任务、把大型 UI 设计稿切分为更小的可管理模块，从而提升实用性。

**EN** 9. Conclusion

**ZH** 9. 结论

**EN** We introduce DesignBench, the first comprehensive multi-framework multi-task benchmark for front-end code generation, encompassing React, Vue, and Angular frameworks. Beyond traditional design generation, we pioneer design edit and repair tasks. Through extensive experiments across task complexity, framework compatibility, difficulty levels, contextual factors and in-depth code-level analysis, we reveal primary limitations in current MLLMs for framework-based development and elicit several actionable advice for researchers and developers.

**ZH** 我们提出 DesignBench——首个面向前端代码生成的综合性多框架、多任务基准，覆盖 React、Vue 与 Angular 框架。除传统的设计生成外，我们率先引入设计编辑与修复任务。通过在任务复杂度、框架适配性、难度层级、上下文因素以及深入的代码层面分析上开展大量实验，我们揭示了当前多模态大语言模型在基于框架的开发中的主要局限，并为研究者与开发者提炼出若干可操作的建议。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] Agrawal et al. (2024) P. Agrawal, S. Antoniak, E. B. Hanna, B. Bout, D. Chaplot, J. Chudnovsky, D. Costa, B. De Monicault, S. Garg, T. Gervet, et al. Pixtral 12b . arXiv preprint arXiv:2410.07073 . Ci -->

<!-- [原子块 · verbatim] AI (2025) M. AI Llama-3.2-90b-vision . Hugging Face . Note: https://huggingface.co/meta-llama/Llama-3.2-90B-Vision Accessed: May 2025 Cited by: Table 4 , Table 4 . -->

<!-- [原子块 · verbatim] Anthropic (2024) Anthropic Claude . Note: Accessed: 2024-06-06 External Links: Link Cited by: §5.2 , Table 4 . -->

<!-- [原子块 · verbatim] Aşıroğlu et al. (2019) B. Aşıroğlu, B. R. Mete, E. Yıldız, Y. Nalçakan, A. Sezen, M. Dağtekin, and T. Ensari Automatic html code generation from mock-up images using machine learning techniques . In 2 -->

<!-- [原子块 · verbatim] [5] Axure (Website) External Links: Link Cited by: §2.1 . -->

<!-- [原子块 · verbatim] Bai et al. (2025) S. Bai, K. Chen, X. Liu, J. Wang, W. Ge, S. Song, K. Dang, P. Wang, S. Wang, J. Tang, et al. Qwen2.5-vl technical report . arXiv preprint arXiv:2502.13923 . Cited by: §5.2 , §5.3 , T -->

<!-- [原子块 · verbatim] Beltramelli (2018) T. Beltramelli Pix2code: generating code from a graphical user interface screenshot . In Proceedings of the ACM SIGCHI symposium on engineering interactive computing systems , pp. 1 -->

<!-- [原子块 · verbatim] Chen et al. (2018) C. Chen, T. Su, G. Meng, Z. Xing, and Y. Liu From ui design image to gui skeleton: a neural machine translator to bootstrap mobile gui implementation . In Proceedings of the 40th In -->

<!-- [原子块 · verbatim] Chen et al. (2024) D. Chen, R. Chen, S. Zhang, Y. Wang, Y. Liu, H. Zhou, Q. Zhang, Y. Wan, P. Zhou, and L. Sun Mllm-as-a-judge: assessing multimodal llm-as-a-judge with vision-language benchmark . In  -->

<!-- [原子块 · verbatim] Chen et al. (2020) J. Chen, C. Chen, Z. Xing, X. Xia, L. Zhu, J. Grundy, and J. Wang Wireframe-based ui design search through image autoencoder . ACM Transactions on Software Engineering and Methodolo -->

<!-- [原子块 · verbatim] Chen et al. (2022) W. Chen, P. Podstreleny, W. Cheng, Y. Chen, and K. Hua Code generation from a graphical user interface via attention-based encoder–decoder model . Multimedia Systems 28 ( 1 ), pp. 1 -->

<!-- [原子块 · verbatim] Cizotto et al. (2023) A. A. J. Cizotto, R. C. T. de Souza, V. C. Mariani, and L. dos Santos Coelho Web pages from mockup design based on convolutional neural network and class activation mapping . Mul -->

<!-- [原子块 · verbatim] Dang et al. (2025) T. H. Dang, J. Xiao, and Y. Huo Envisioning future interactive web development: editing webpage with natural language . arXiv preprint arXiv:2510.26516 . Cited by: §3.1 . -->

<!-- [原子块 · verbatim] Google (2024) Google Gemini api . Note: Accessed: 2024-10-06 External Links: Link Cited by: §5.2 , Table 4 . -->

<!-- [原子块 · verbatim] Gu et al. (2024) A. Gu, B. Rozière, H. Leather, A. Solar-Lezama, G. Synnaeve, and S. I. Wang Cruxeval: a benchmark for code reasoning, understanding and execution . arXiv preprint arXiv:2401.03065 . C -->

<!-- [原子块 · verbatim] Gui et al. (2025) Y. Gui, Z. Li, Y. Wan, Y. Shi, H. Zhang, B. Chen, Y. Su, D. Chen, S. Wu, X. Zhou, et al. Webcode2m: a real-world dataset for code generation from webpage designs . In Proceedings of  -->

<!-- [原子块 · verbatim] Gui et al. (2024) Y. Gui, Z. Li, Y. Wan, Y. Shi, H. Zhang, Y. Su, S. Dong, X. Zhou, and W. Jiang VISION2UI: a real-world dataset with layout for code generation from ui designs . arXiv preprint arXiv: -->

<!-- [原子块 · verbatim] Jain et al. (2024) N. Jain, K. Han, A. Gu, W. Li, F. Yan, T. Zhang, S. Wang, A. Solar-Lezama, K. Sen, and I. Stoica Livecodebench: holistic and contamination free evaluation of large language models f -->

<!-- [原子块 · verbatim] Jain et al. (2019) V. Jain, P. Agrawal, S. Banga, R. Kapoor, and S. Gulyani Sketch2Code: transformation of sketches to ui in real-time using deep neural network . arXiv preprint arXiv:1910.08930 . Cit -->

<!-- [原子块 · verbatim] Krotoff (2024) T. Krotoff Frontend frameworks popularity . Note: https://gist.github.com/tkrotoff/b1caa4c3a185629299ec234d2314e190 Accessed: 2025-05-28 Cited by: §2.2 , §4.2 . -->

<!-- [原子块 · verbatim] Lam et al. (2025) M. H. Lam, C. Wang, J. Huang, and M. Lyu CodeCrash: exposing LLM fragility to misleading natural language in code reasoning . In The Thirty-ninth Annual Conference on Neural Informat -->

<!-- [原子块 · verbatim] Laurençon et al. (2024) H. Laurençon, L. Tronchon, and V. Sanh Unlocking the conversion of web screenshots into html code with the websight dataset . External Links: 2403.09029 Cited by: Table 1 , §1  -->

<!-- [原子块 · verbatim] Li et al. (2024) K. Li, Y. Tian, Q. Hu, Z. Luo, Z. Huang, and J. Ma MMCode: benchmarking multimodal large language models for code generation with visually rich programming problems . In Findings of t -->

<!-- [原子块 · verbatim] Liu et al. (2022) Liu, C. Chen, J. Wang, Y. Huang, J. Hu, and Q. Wang Nighthawk: fully automated localizing ui display issues via visual understanding . IEEE Transactions on Software Engineering (TSE) -->

<!-- [原子块 · verbatim] Liu et al. (2025) V. Liu, R. H. Kazi, L. Wei, M. Fisher, T. Langlois, S. Walker, and L. Chilton LogoMotion: visually-grounded code synthesis for creating and editing animation . In Proceedings of the  -->

<!-- [原子块 · verbatim] Liu et al. (2020) Z. Liu, C. Chen, J. Wang, Y. Huang, J. Hu, and Q. Wang Owl eyes: spotting ui display issues via visual understanding . In Proceedings of the 35th IEEE/ACM international conference on -->

<!-- [原子块 · verbatim] Lormeau (2023) G. Lormeau Single-file-cli: save a web page as a single html file . Note: https://github.com/gildas-lormeau/single-file-cli Accessed: 2025-5-26 Cited by: §4.2 . -->

<!-- [原子块 · verbatim] Lu et al. (2025) Y. Lu, A. Leung, A. Swearngin, J. Nichols, and T. Barik Misty: ui prototyping through interactive conceptual blending . In Proceedings of the 2025 CHI Conference on Human Factors in C -->

<!-- [原子块 · verbatim] Meta (2024) Meta Llama 3.2 vision . Note: Accessed: 2025-02-06 External Links: Link Cited by: §5.2 , §5.3 . -->

<!-- [原子块 · verbatim] Moran et al. (2018) K. Moran, C. Bernal-Cárdenas, M. Curcio, R. Bonett, and D. Poshyvanyk Machine learning-based prototyping of graphical user interfaces for mobile apps . IEEE Transactions on Softwar -->

<!-- [原子块 · verbatim] Nguyen and Csallner (2015) T. A. Nguyen and C. Csallner Reverse engineering mobile application user interfaces with remaui (t) . In 2015 30th IEEE/ACM International Conference on Automated Software En -->

<!-- [原子块 · verbatim] OpenAI (2024) OpenAI Hello gpt-4o . Note: Accessed: 2024-10-06 External Links: Link Cited by: §4.2 , §5.2 , §5.4 , Table 4 . -->

<!-- [原子块 · verbatim] Papineni et al. (2002) K. Papineni, S. Roukos, T. Ward, and W. Zhu Bleu: a method for automatic evaluation of machine translation . In Proceedings of the 40th annual meeting of the Association for Com -->

<!-- [原子块 · verbatim] Radford et al. (2021) A. Radford, J. W. Kim, C. Hallacy, A. Ramesh, G. Goh, S. Agarwal, G. Sastry, A. Askell, P. Mishkin, J. Clark, et al. Learning transferable visual models from natural language sup -->

<!-- [原子块 · verbatim] Raju (2025) M. Raju Best web development frameworks in 2025 . External Links: Link Cited by: §1 , §2.2 , §4.2 . -->

<!-- [原子块 · verbatim] Selenium (2025) Selenium Selenium . External Links: Link Cited by: §4.2 . -->

<!-- [原子块 · verbatim] Si et al. (2024) C. Si, Y. Zhang, Z. Yang, R. Liu, and D. Yang Design2Code: how far are we from automating front-end engineering? . arXiv preprint arXiv:2403.03163 . Cited by: Table 1 , §1 , §3.2 . -->

<!-- [原子块 · verbatim] [38] Sketch (Website) External Links: Link Cited by: §2.1 . -->

<!-- [原子块 · verbatim] Tang et al. (2025) W. Tang, J. Xiao, W. Jiang, X. Xiao, Y. Wang, X. Tang, Q. Li, Y. Ma, J. Liu, S. Tang, and M. R. Lyu SlideCoder: layout-aware RAG-enhanced hierarchical slide generation from design . -->

<!-- [原子块 · verbatim] [40] D. Team DesignBench repository . Note: https://github.com/WebPAI/DesignBench Cited by: §4.2 , §5.1 , §5.2 . -->

<!-- [原子块 · verbatim] Thada and Jaglan (2013) V. Thada and V. Jaglan Comparison of jaccard, dice, cosine similarity coefficient to find best fitness value for web retrieved documents using genetic algorithm . International -->

<!-- [原子块 · verbatim] [42] Top 500 often visited websites (Website) External Links: Link Cited by: §4.2 , §7 . -->

<!-- [原子块 · verbatim] [43] V0 by vercel (Website) External Links: Link Cited by: §4.2 . -->

<!-- [原子块 · verbatim] [44] Vue0 (Website) External Links: Link Cited by: §4.2 . -->

<!-- [原子块 · verbatim] Wan et al. (2024) Y. Wan, Y. Dong, J. Xiao, Y. Huo, W. Wang, and M. R. Lyu MRWeb: an exploration of generating multi-page resource-aware web code from ui designs . arXiv preprint arXiv:2412.15310 . Ci -->

<!-- [原子块 · verbatim] Wan et al. (2025a) Y. Wan, T. Liang, J. Xu, J. Xiao, Y. Huo, and M. R. Lyu Automatically generating web applications from requirements via multi-agent test-driven development . arXiv preprint arXiv:25 -->

<!-- [原子块 · verbatim] Wan et al. (2025b) Y. Wan, C. Wang, Y. Dong, W. Wang, S. Li, Y. Huo, and M. R. Lyu Automatically generating ui code from screenshot: a divide-and-conquer-based approach . Proceedings of the ACM on Sof -->

<!-- [原子块 · verbatim] Wang et al. (2025) R. Wang, J. Guo, C. Gao, G. Fan, C. Y. Chong, and X. Xia Can llms replace human evaluators? an empirical study of llm-as-a-judge in software engineering . In 2025 International Symp -->

<!-- [原子块 · verbatim] Wang et al. (2004) Z. Wang, A. C. Bovik, H. R. Sheikh, and E. P. Simoncelli Image quality assessment: from error visibility to structural similarity . IEEE transactions on image processing 13 ( 4 ), p -->

<!-- [原子块 · verbatim] Xiao et al. (2026) J. Xiao, J. Qin, S. Li, M. H. Lam, Y. Wan, J. Huang, Y. Huo, and M. R. Lyu ComUICoder: component-based reusable ui code generation for complex websites via semantic segmentation and -->

<!-- [原子块 · verbatim] Xiao et al. (2024) J. Xiao, Y. Wan, Y. Huo, Z. Xu, and M. R. Lyu Interaction2Code: how far are we from automatic interactive webpage generation? . arXiv preprint arXiv:2411.03292 . Cited by: §3.2 . -->

<!-- [原子块 · verbatim] Xiao et al. (2025) J. Xiao, Z. Zhang, Y. Wan, Y. Huo, Y. Liu, and M. R. Lyu Efficientuicoder: efficient mllm-based ui code generation via input and output token compression . arXiv preprint arXiv:2509 -->

<!-- [原子块 · verbatim] Xu et al. (2021) Y. Xu, L. Bo, X. Sun, B. Li, J. Jiang, and W. Zhou Image2emmet: automatic code generation from web user interface image . Journal of Software: Evolution and Process 33 ( 8 ), pp. e236 -->

<!-- [原子块 · verbatim] Yang et al. (2025) J. Yang, C. E. Jimenez, A. L. Zhang, K. Lieret, J. Yang, X. Wu, O. Press, N. Muennighoff, G. Synnaeve, K. R. Narasimhan, et al. SWE-bench multimodal: do ai systems generalize to vis -->

<!-- [原子块 · verbatim] Yuan et al. (2025) M. Yuan, J. Chen, Z. Xing, A. Quigley, Y. Luo, T. Luo, G. Mohammadi, Q. Lu, and L. Zhu DesignRepair: Dual-Stream Design Guideline-Aware Frontend Repair with Large Language Models .  -->

<!-- [原子块 · verbatim] Yun et al. (2024) S. Yun, H. Lin, R. Thushara, M. Q. Bhat, Y. Wang, Z. Jiang, M. Deng, J. Wang, T. Tao, J. Li, et al. Web2Code: a large-scale webpage-to-code dataset and evaluation framework for multi -->

<!-- [原子块 · verbatim] Zhang et al. (2025) S. Zhang, Z. Xing, R. Guo, F. Xu, L. Chen, Z. Zhang, X. Zhang, Z. Feng, and Z. Zhuang Empowering agile-based generative software development through human-ai teamwork . ACM Transac -->

<!-- [原子块 · verbatim] Zhou et al. (2025) T. Zhou, Y. Zhao, X. Hou, X. Sun, K. Chen, and H. Wang Bridging design and development with automated declarative ui code generation . Proceedings of the ACM on Software Engineering -->

<!-- [原子块 · verbatim] Zhuo et al. (2024) T. Y. Zhuo, M. C. Vu, J. Chim, H. Hu, W. Yu, R. Widyasari, I. N. B. Yusuf, H. Zhan, J. He, I. Paul, et al. Bigcodebench: benchmarking code generation with diverse function calls and -->
