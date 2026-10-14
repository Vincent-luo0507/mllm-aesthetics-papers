# 用大语言模型为 UI 原型稿生成自动反馈

> 原标题：Generating Automatic Feedback on UI Mockups with Large Language Models
> 作者：Peitong Duan, Jeremy Warner, Yang Li, Bjoern Hartmann · arXiv:2403.13139 · 2024-03-19

<!-- [原子块 · verbatim] Generating Automatic Feedback on UI Mockups with Large Language Models -->

<!-- [原子块 · img]  -->

**EN** Figure 1. Diagram illustrating the UI prototyping workflow using this plugin. First, the designer prototypes the UI in Figma (Box A) and then runs the plugin (Arrow A1). The designer then selects the guidelines to use for evaluation (Box B) and runs the evaluation with the selected guidelines (Arrow A2). The plugin obtains evaluation results from the LLM and renders them in an interpretable format (Box C). The designer uses these results to update their design and reruns the evaluation (Arrow A3). The designer iteratively revises their Figma UI mockup, following this process, until they have achieved the desired result.A flowchart with three boxes. The first Box contains a screenshot of Figma with a UI mockup. There is an arrow labeled “A1” pointing from the first Box to the second Box. The second Box contains this Figma screen with the plugin window open, which contains checkboxes for common guidelines, like NN Usability Heuristics, and a large text field to enter in custom guidelines. There is an arrow “A2” pointing from the second box to the third box and an arrow “A3” pointing from the third box to the second box. The third box contains a plugin screen with the evaluation results. There a list of violation explanation text on the left and the UI screenshot on the right.

**ZH** 图 1. 示意图，展示使用该插件的 UI 原型设计工作流程。设计师先在 Figma 中制作 UI 原型（框 A），随后运行插件（箭头 A1）；接着选择用于评估的准则（框 B），并按所选准则执行评估（箭头 A2）。插件从大语言模型获取评估结果，并以可理解的格式呈现（框 C）。设计师依据结果修改设计并重新运行评估（箭头 A3）。按此流程反复修订 Figma 中的 UI 原型稿，直至达到预期效果。一个包含三个框的流程图。第一个框中是带有 UI 原型稿的 Figma 截图。标有“A1”的箭头从第一个框指向第二个框。第二个框中是打开了插件窗口的 Figma 界面，窗口中列出了常见准则的复选框，如 NN 可用性启发式准则，以及一个用于输入自定义准则的大型文本框。标有“A2”的箭头从第二个框指向第三个框，“A3”箭头则从第三个框指回第二个框。第三个框中是显示评估结果的插件界面，左侧为违反项说明文字的列表，右侧为 UI 截图。

<!-- [原子块 · verbatim] Abstract. -->

<!-- [原子块 · verbatim] Feedback on user interface (UI) mockups is crucial in design. However, human feedback is not always readily available. We explore the potential of using large language models for automatic feedback. S -->

**EN** Keywords:

**ZH** 关键词：

**EN** 1. Introduction

**ZH** 1. 引言

**EN** User interface (UI) design is an essential domain that shapes how humans interact with technology and digital information. Designing user interfaces commonly involves iterative rounds of feedback and revision. Feedback is essential for guiding designers towards improving their UIs. While this feedback traditionally comes from humans (via user studies and expert evaluations), recent advances in computational UI design enable automated feedback. However, automated feedback is often limited in scope (e.g., the metric could only evaluate layout complexity) and can be challenging to interpret (Schoop et al., 2022). While human feedback is more informative, it is not readily available and requires time and resources for recruiting and compensating participants.

**ZH** 用户界面（UI）设计塑造了人与技术及数字信息的交互方式，是一个至关重要的领域。设计用户界面通常需要反复的反馈与修改，反馈对引导设计师改进其 UI 不可或缺。这类反馈传统上来自人类（经由用户研究与专家评估），而计算式 UI 设计的最新进展使自动化反馈成为可能。不过，自动化反馈的适用范围往往有限（例如某项指标只能评估布局复杂度），且解释起来并不容易（Schoop 等，2022）。人类反馈信息量更大，却不易获得，招募与酬谢参与者都需要时间与资源。

**EN** One method of evaluation that still relies on human participants today is heuristic evaluation, where an experienced evaluator checks an interface against a list of usability heuristics (rules of thumb) developed over time, such as Nielsen’s 10 Usability Heuristics (Nielsen, 1994). Despite appearing straightforward, heuristic evaluation is challenging and subjective (Nielsen and Molich, 1990), dependent on the evaluator’s previous training and personality-related factors (Ling and Salvendy, 2009). These limitations further suggest an opportunity for AI-assisted evaluation.

**ZH** 启发式评估至今仍依赖人类参与者：由经验丰富的评估者依据一组长期形成的可用性启发式准则（经验法则）检查界面，例如 Nielsen 的 10 条可用性启发式准则（Nielsen，1994）。启发式评估看似简单，实则具有挑战性和主观性（Nielsen 和 Molich，1990），取决于评估者此前所受训练以及人格相关因素（Ling 和 Salvendy，2009）。这些局限进一步说明，AI 辅助评估存在用武之地。

**EN** There are several reasons why LLMs could be suitable for automating heuristic evaluation. The evaluation process primarily involves rule-based reasoning, which LLMs have shown capacity for (OpenAI, 2023). Moreover, design guidelines are predominately in text form, making them amenable for LLMs, and the language model could also return its feedback as text-based explanations that designers prefer (Lee et al., 2020). Finally, LLMs have demonstrated the ability to understand and reason with mobile UIs (Wang et al., 2023), as well as generalize to new tasks and data (Lu et al., 2022; Sanh et al., 2022). However, there are also reasons that suggest caution for using LLMs for this task. For one, LLMs only accept text as input, while user interfaces are complex artifacts that combine text, images, and UI components into hierarchical layouts. In addition, LLMs have been shown to hallucinate (Lee et al., 2023) (i.e., generate false information) and may potentially identify incorrect guideline violations. This paper explores the potential of using LLMs to carry out heuristic evaluation automatically. In particular, we aim to determine their performance, strengths and limitations, and how an LLM-based tool can fit into existing design practices.

**ZH** 有多条理由表明大语言模型（Large Language Model，LLM）适合用于自动化启发式评估。评估过程主要涉及基于规则的推理，而 LLM 已展现出这方面的能力（OpenAI，2023）；设计准则主要以文本形式存在，天然适合 LLM 处理，语言模型也能把反馈以文本说明的形式返回，而这正是设计师偏好的形式（Lee 等，2020）。此外，LLM 已证明能够理解并推理移动端 UI（Wang 等，2023），也能泛化到新任务与新数据（Lu 等，2022；Sanh 等，2022）。不过也有理由提醒我们保持审慎：其一，LLM 只接受文本输入，而用户界面是把文本、图像与 UI 组件组合成层级布局的复杂产物；其二，LLM 已被证明会产生幻觉（Lee 等，2023），即生成虚假信息，可能识别出错误的准则违反项。本文探索利用 LLM 自动执行启发式评估的潜力，具体考察其性能、优势与局限，以及基于 LLM 的工具如何融入现有设计实践。

**EN** To explore the potential of LLMs in conducting heuristic evaluation, we built a tool that enables designers to run automatic evaluations on UI mockups and receive text-based feedback. We package this system as a plugin for Figma (fig, 2023), a popular UI design tool. Figure 1 illustrates the iterative usage of this plugin. The designer prototypes their UI in Figma, and then selects a set of guidelines they would like to use for evaluation in our plugin. The plugin returns the feedback, which the designer uses to revise their mockup. The designer can then repeat this process on their edited mockup. To improve the LLM’s performance and adapt to individual preferences, designers can provide feedback on each generated suggestion, which is integrated into the model for the next round of evaluation. The plugin produces UI mockup feedback by querying an LLM with the guidelines’ text and a JSON representation of the UI. The LLM then returns a set of detected guideline violations. Instead of directly stating the violations, they are phrased as constructive suggestions for improving the UI. As LLMs can only process text and have a limited context window, we developed a JSON representation of the UI that concisely captures the layout hierarchy and contains both semantic (text, semantic label, element type) and visual (location, size, and color) details of each element and group in the UI. To further accommodate context window limits, we scoped the plugin to evaluate only static (i.e., non-interactive) UI mockups, one screen at a time.

**ZH** 为探索 LLM 执行启发式评估的潜力，我们开发了一款工具，让设计师能对 UI 原型稿运行自动评估并收到文本形式的反馈，并将其打包为流行 UI 设计工具 Figma（fig，2023）的插件。图 1 展示了该插件的迭代使用方式：设计师在 Figma 中制作 UI 原型，然后在插件中选择一组希望用于评估的准则；插件返回反馈，设计师据此修改原型稿，并可在修改后的原型稿上重复这一过程。为提升 LLM 的表现并适应个人偏好，设计师可对每条生成的建议给出反馈，这些反馈会被整合进模型，用于下一轮评估。插件通过向 LLM 查询准则文本与 UI 的 JSON 表示来生成 UI 原型稿反馈，LLM 随后返回一组检测到的准则违反项；系统并不直接陈述违反项，而是将其表述为改进 UI 的建设性建议。由于 LLM 只能处理文本且上下文窗口有限，我们设计了一种 UI 的 JSON 表示，以简洁方式刻画布局层级，并同时包含每个元素与分组的语义信息（文本、语义标签、元素类型）与视觉信息（位置、尺寸、颜色）。为兼顾上下文窗口限制，插件被限定为一次只评估一个静态（即非交互式）的 UI 原型稿。

**EN** We conducted an exploration of how several current state of the art LLMs perform on this task and found that GPT-4 had the best performance by far. Hence, we solely focus on GPT-4 for the remaining studies. To assess GPT-4’s performance in conducting heuristic evaluation on a large scale, we carried out a study where three design experts rated the accuracy and helpfulness of its heuristic evaluation feedback for 51 distinct UIs. To compare GPT-4’s output with feedback provided by human experts, we conducted a heuristic evaluation study with 12 design experts, who manually identified guideline violations in a set of 12 UIs. Finally, to qualitatively determine GPT-4’s strengths and limitations and its performance as an iterative design tool, we conducted a study with another group of 12 design experts, who each used this tool to iteratively refine a set of 3 UIs and evaluated the LLM feedback each round. For all three studies, we used diverse guidelines covering visual design, usability, and semantic organization to generate design feedback.

**ZH** 我们考察了若干当前最先进的 LLM 在该任务上的表现，发现 GPT-4 的表现远超其他模型，因此在其余研究中只关注 GPT-4。为大规模评估 GPT-4 执行启发式评估的能力，我们开展了一项研究，由三位设计专家对 51 个不同 UI 的启发式评估反馈的准确性与有用性打分。为把 GPT-4 的输出与人类专家的反馈做比较，我们进行了一项启发式评估研究，请 12 位设计专家在一组 12 个 UI 上人工找出准则违反项。最后，为定性判断 GPT-4 的优势、局限及其作为迭代设计工具的表现，我们与另外 12 位设计专家开展研究，每人使用该工具迭代改进一组 3 个 UI，并对每一轮的 LLM 反馈做出评价。三项研究均使用覆盖视觉设计、可用性与语义组织的多类准则来生成设计反馈。

**EN** We found that GPT-4 was generally accurate and helpful in identifying issues in poor UI designs, but its performance became worse after iterations of edits that improved the design, making it unsuitable as an iterative tool. Furthermore, its performance varied, depending on the guideline. GPT-4 generally performed well on straightforward checks with the data available in the UI JSON and worse when the JSON differed from what was visually or semantically depicted in the UI. Finally, although GPT-4’s feedback is sometimes inaccurate, most study participants still found this tool useful for their own design practices, as it was able to catch subtle errors, improve the UI’s text, and reason with the UI’s semantics. They stated that the errors made by GPT-4 are not dangerous, as there is a human in the loop to catch them, and suggested various use cases for the tool. Finally, we also distilled a set of concrete limitations of GPT-4 for this task.

**ZH** 我们发现，GPT-4 在发现劣质 UI 设计中的问题时总体准确且有用，但在设计经过修改而变好之后表现下滑，因此并不适合用作迭代工具。其表现还随准则而异：对于能直接依据 UI JSON 中数据完成的检查，GPT-4 普遍表现良好；当 JSON 与 UI 的视觉或语义呈现不一致时则表现较差。此外，尽管 GPT-4 的反馈有时不够准确，多数参与者仍认为该工具对自己的设计实践有用，因为它能发现细微错误、改进 UI 文案，并对 UI 语义进行推理。参与者表示，GPT-4 犯的错误并不危险，因为有人工审核来兜底，他们还提出了该工具的多种使用场景。最后，我们也提炼出 GPT-4 在该任务上的一组具体局限。

**EN** In summary, even with today’s limitations, GPT-4 can already be used to automatically evaluate some heuristics for UI design; other heuristics may require more visual information or other technical advancements. However, designers accepted occasional imperfect suggestions and appreciated GPT-4’s attention to detail. This implies that while LLM tools will not replace human heuristic evaluation, they may nevertheless soon find a place in design practice.

**ZH** 综上，即便以今天的局限来看，GPT-4 已经可用于自动评估 UI 设计中的部分启发式准则；另一些准则则可能还需要更多视觉信息或其他技术进展。设计师能够接受偶尔不完美的建议，也认可 GPT-4 对细节的关注。这意味着，基于 LLM 的工具虽然不会取代人工启发式评估，却很可能很快在设计实践中占据一席之地。

**EN** Our contributions are as follows:

**ZH** 本文贡献如下：

**EN** • A Figma plugin that uses GPT-4 to automate heuristic evaluation of UI mockups with arbitrary design guidelines.

**ZH** • 一款使用 GPT-4、可按任意设计准则对 UI 原型稿自动执行启发式评估的 Figma 插件。

**EN** • An investigation of GPT-4’s capability to automate heuristic evaluations through a study where three human participants rated the accuracy and helpfulness of LLM-generated design suggestions for 51 UIs.

**ZH** • 对 GPT-4 自动化启发式评估能力的考察：在一项研究中，三位人类参与者对 51 个 UI 的 LLM 生成设计建议的准确性与有用性进行打分。

**EN** • A comparison of the violations found by this tool with those identified by human experts.

**ZH** • 将该工具发现的违反项与人类专家识别出的违反项进行比较。

**EN** • An exploration of how such a tool can fit into existing design practice via a study where 12 design experts used this tool to iteratively refine UIs, assessed the LLM-generated feedback, and discussed their experiences working with the plugin.

**ZH** • 对这类工具如何融入现有设计实践的探索：在一项研究中，12 位设计专家使用该工具迭代改进 UI、评价 LLM 生成的反馈，并讨论其使用插件的体验。

**EN** 2. Related Work

**ZH** 2. 相关工作

**EN** 2.1. AI-Enhanced Design Tools

**ZH** 2.1. AI 增强的设计工具

**EN** Before the widespread use of generative AI, research in AI-enhanced design tools explored a variety of model architectures to accomplish a wide range of tasks. For instance, Lee et al. built a prototyping assistance tool (GUIComp) that provides multi-faceted feedback for various stages of the prototyping process. GUIComp uses an auto-encoder to support querying UI examples for design inspiration and separate convolutional neural networks to evaluate the visual complexity of the UI prototypes and predict salient regions (Lee et al., 2020). Other studies have utilized computer vision techniques to predict saliency in graphical designs (Fosco et al., 2020) and perceived tappability (Schoop et al., 2022; Swearngin and Li, 2019). Deep learning models have been developed for generation (Cheng et al., 2023), autocompletion (Brückner et al., 2022), and optimization (Duan et al., 2020; Swearngin et al., 2020; Todi et al., 2016) of UI layouts. One limitation of these techniques is that a separate model is needed for each type of task. In addition, study participants had difficulty interpreting the feedback from these models (Schoop et al., 2022) and would have liked natural language explanations of detected design issues (Lee et al., 2020). Our work addresses both of these limitations. First, our system supports arbitrary guidelines that evaluate various aspects of the UI design as input. Furthermore, the language model uses natural language to explain each detected guideline violation.

**ZH** 在生成式 AI 广泛应用之前，AI 增强设计工具的研究尝试了多种模型架构来完成各类任务。例如，Lee 等人开发了原型设计辅助工具 GUIComp，可在原型设计的各个阶段提供多方位反馈；GUIComp 用自编码器支持查询 UI 示例以获取设计灵感，并用若干独立的卷积神经网络评估 UI 原型的视觉复杂度、预测显著区域（Lee 等，2020）。其他研究则利用计算机视觉技术预测平面设计中的显著性（Fosco 等，2020）与感知可点击性（Schoop 等，2022；Swearngin 和 Li，2019）。深度学习模型也被用于 UI 布局的生成（Cheng 等，2023）、自动补全（Brückner 等，2022）与优化（Duan 等，2020；Swearngin 等，2020；Todi 等，2016）。这类技术的一个局限在于每类任务都需要单独的模型；此外，研究参与者难以理解这些模型给出的反馈（Schoop 等，2022），并希望就检测到的设计问题获得自然语言解释（Lee 等，2020）。我们的工作同时应对了这两项局限：一方面，系统支持输入任意准则，从多个方面评估 UI 设计；另一方面，语言模型以自然语言解释每一处检测到的准则违反。

**EN** 2.2. Applications of Generative AI in Design

**ZH** 2.2. 生成式 AI 在设计中的应用

**EN** The recent emergence of generative AI, such as GPT, has led to various applications in design support. Park et al. carried out two studies that employ LLMs to simulate user personas in online social settings. They used GPT-3 to generate interactions on social media platforms as testing data for these platforms (Park et al., 2022). They later expanded on this work to build agents that could remember, reflect on, and retrieve memories from interacting with other agents to realistically simulate large-scale social interactions (Park et al., 2023). Hämäläinen et al. used GPT-3 to generate synthetic human-like responses to survey questionnaires about video game experiences (Hämäläinen et al., 2023). Finally, Wang et al. investigated the feasibility of using LLMs to interact with UIs via natural language (Wang et al., 2023). They developed prompting techniques for tasks like screen summarization, answering questions about the screen, generating questions about the screen, and mapping instructions to UI actions. Researchers have also begun to create design tools that use Generative AI. Lawton et al. built a system where a human and generative AI model collaborate in drawing, and ran an exploratory study on the capabilities of this tool (Lawton et al., 2023). Stylette allows users to specify design goals in natural language and uses GPT to infer relevant CSS properties (Kim et al., 2022). Perhaps most similar to our work is a study by Petridis et al. (Petridis et al., 2023), who explored using LLM prompting in creating functional LLM-based UI prototypes. Their study findings showed that LLM prompts sped up prototype creation and clarified LLM-based UI requirements, which led to the development of a Figma Plugin for automated content generation and determination of optimal frame changes. These existing studies, however, have not examined the application of LLMs as a general-purpose evaluator for mobile UIs of any category with a diverse set of heuristics.

**ZH** 以 GPT 为代表的生成式 AI 近来兴起，在设计支持领域催生了诸多应用。Park 等人开展了两项使用 LLM 模拟在线社交场景中用户角色的研究：先用 GPT-3 在社交媒体平台上生成交互内容，作为这些平台的测试数据（Park 等，2022）；随后扩展该工作，构建出能够记忆、反思并检索与其他智能体交互记忆的智能体，以逼真地模拟大规模社交互动（Park 等，2023）。Hämäläinen 等人用 GPT-3 生成类人合成回答，用于关于电子游戏体验的问卷调查（Hämäläinen 等，2023）。Wang 等人考察了用 LLM 以自然语言与 UI 交互的可行性（Wang 等，2023），针对屏幕摘要、屏幕问答、围绕屏幕生成问题以及把指令映射到 UI 操作等任务开发了提示技术。研究者也已开始构建使用生成式 AI 的设计工具：Lawton 等人搭建了人与生成式 AI 模型协同作画的系统，并对该工具的能力开展探索性研究（Lawton 等，2023）；Stylette 允许用户用自然语言指定设计目标，并用 GPT 推断相关的 CSS 属性（Kim 等，2022）。与本文最为接近的或许是 Petridis 等人的研究（Petridis 等，2023），他们探索了在创建基于 LLM 的功能性 UI 原型时使用 LLM 提示；其研究发现，LLM 提示加快了原型创建并澄清了基于 LLM 的 UI 需求，由此催生了一款用于自动内容生成与确定最佳画框改动的 Figma 插件。不过，这些已有研究均未考察把 LLM 用作通用评估器，以多样化的启发式准则评估任意类别的移动端 UI。

**EN** 2.3. AI-enhanced Software Testing

**ZH** 2.3. AI 增强的软件测试

**EN** Another domain of UI evaluation is testing the functionality of the GUI (i.e., “software testing”). Existing LLM-based approaches include Liu et al.’s method (Liu et al., 2023a), which uses GPT-3 to simulate a human tester that would interact with the GUI. Their system had greater coverage and found more bugs than existing baselines, and also identified new bugs on Google Play Store apps. Wang et al. conducted a comprehensive literature review on using LLMs for software testing. They analyzed various studies that used LLMs for unit test generation, validation of test outputs, test input generation, analyzing bugs, fixing identified bugs in code, and identifying and correcting bugs. Contrary to software testing, our study focuses on evaluating GUI mockups, which is at an earlier stage of the UI development process. Furthermore, evaluation of mockups and software are intrinsically different; mockup evaluation focuses on adherence to design guidelines and user feedback, whereas software testing focuses on finding bugs in the implementation. Prior to LLMs, Chen et al. utilized computer vision techniques to identify discrepancies between the UI mockup and implementation (Chen et al., 2017). Their system could identify differences in positioning, color, and size of corresponding elements. However, their evaluation requires a UI mockup as the benchmark, while our system could carry out evaluation using any set of heuristics.

**ZH** UI 评估的另一个领域是测试图形用户界面（GUI）的功能，即软件测试。已有的基于 LLM 的方法包括 Liu 等人的方法（Liu 等，2023a），其用 GPT-3 模拟与 GUI 交互的人类测试者；该系统覆盖面更广、发现的缺陷多于现有基线，还在 Google Play 商店的应用中发现了新缺陷。Wang 等人对使用 LLM 进行软件测试做了全面的文献综述，分析了各类研究在单元测试生成、测试输出校验、测试输入生成、缺陷分析、修复代码中已识别的缺陷，以及识别与纠正缺陷等方面的应用。与软件测试不同，我们的研究聚焦 GUI 原型稿的评估，处于 UI 开发流程中更早的阶段；而且原型稿评估与软件评估有着本质区别：前者关注是否遵循设计准则与用户反馈，后者关注在实现中发现缺陷。在 LLM 出现之前，Chen 等人利用计算机视觉技术识别 UI 原型稿与实现之间的差异（Chen 等，2017），其系统能定位对应元素在位置、颜色与尺寸上的差别；但该评估需要一个 UI 原型稿作为基准，而我们的系统可用任意一组启发式准则执行评估。

**EN** 2.4. Heuristics and Design Guidelines

**ZH** 2.4. 启发式准则与设计准则

**EN** An essential aspect of the design process is gathering feedback to improve future iterations. One central way designers generate feedback is to conduct heuristic evaluations (Nielsen and Molich, 1990; Nielsen, 1992), which uses a set of guidelines to identify and characterize undesired interface characteristics as violations of specific guidelines. While initially designed for desktop interfaces, other work has adapted heuristic evaluation to more devices and domains (Mankoff et al., 2003; Pinelle et al., 2008; Mi et al., 2014; de Lima Salgado et al., 2016). In general, researchers have developed design guidelines for a vast category of devices, tasks, and populations including accessible data visualizations (Elavsky et al., 2022), multi-modal touchscreen graphics (Gorlewicz et al., 2020), smart televisions (Weber et al., 2016), ambient lighting interactions (Matviienko et al., 2015), hands-free speech interaction (Murad et al., 2018), navigation in virtual environments (Vinson, 1999), website readability (Miniukovich et al., 2017), supporting web design for aging communities (Zaphiris et al., 2005; Kurniawan and Zaphiris, 2005), and for cross-cultural design considerations (Alexander et al., 2017). A widely-used set of guidelines is Nielsen’s 10 Usability Heuristics (Nielsen, 1994), a set of general principles for interaction design. Luther et al. surveyed design textbooks and other resources and compiled a comprehensive set of specific critique statements for the visual design of an interface, which were organized into 7 visual design principles (Luther et al., 2014). Recently, Duan et al. developed a set of 5 specific and actionable guidelines for organizing UI elements based on their semantics (i.e., functionality, content, or purpose) to help design clear and intuitive interfaces (Duan et al., 2023). While these guidelines are meant to encode common design patterns and errors distilled from design expert guidance, they still require a human to interpret and apply them, making adapting to a new set of guidelines time-consuming, especially for novice designers. Our work builds off of these design guidelines as a means of focusing and justifying the LLM’s design suggestions and feedback.

**ZH** 设计流程的一个关键环节是收集反馈以改进后续迭代。设计师获取反馈的一个主要途径是开展启发式评估（Nielsen 和 Molich，1990；Nielsen，1992），即用一组准则识别并刻画界面中的不良特征，将其归为对特定准则的违反。启发式评估最初面向桌面界面，后续工作已将其适配到更多设备与领域（Mankoff 等，2003；Pinelle 等，2008；Mi 等，2014；de Lima Salgado 等，2016）。总体而言，研究者已针对大量设备、任务与人群制定了设计准则，包括无障碍数据可视化（Elavsky 等，2022）、多模态触屏图形（Gorlewicz 等，2020）、智能电视（Weber 等，2016）、环境光交互（Matviienko 等，2015）、免提语音交互（Murad 等，2018）、虚拟环境中的导航（Vinson，1999）、网站可读性（Miniukovich 等，2017）、面向老龄化群体的网页设计支持（Zaphiris 等，2005；Kurniawan 和 Zaphiris，2005），以及跨文化设计考量（Alexander 等，2017）。其中被广泛使用的一套准则是 Nielsen 的 10 条可用性启发式准则（Nielsen，1994），即一组交互设计的通用原则。Luther 等人调研了设计教材及其他资料，汇总出一套针对界面视觉设计的具体批评语句，并将其组织为 7 条视觉设计原则（Luther 等，2014）。近期，Duan 等人提出了 5 条具体可操作的准则，用于按语义（即功能、内容或用途）组织 UI 元素，以帮助用户设计清晰直观的界面（Duan 等，2023）。这些准则旨在编码从设计专家指导中提炼出的常见设计模式与错误，但仍需要人来解释与运用，这使适应一套新准则颇为耗时，对新手设计师尤其如此。我们的工作以这些设计准则为基础，用以聚焦并支撑 LLM 的设计建议与反馈。

**EN** 2.5. User Interfaces for Design Feedback

**ZH** 2.5. 面向设计反馈的用户界面

**EN** Prior research has explored several ways to support designers as they both give and receive feedback across a range of media (Kulkarni et al., 2015; Luther et al., 2015; Warner et al., 2023; Yoon et al., 2014; Pavel et al., 2016). Cheng et al. explore the process of publicly gathering design feedback from online forums (Cheng et al., 2020) and list several design considerations for feedback systems. For supporting in-context feedback for graphic designs, CritiqueKit (Fraser et al., 2017) showcased a UI for providing and improving real-time design feedback, while Charrette (O’Leary et al., 2018) supported organizing and sharing feedback on longer histories and variations of a design. A study by Ngoon et al. showcased reusing expert feedback suggestions and adaptive guidance as two ways of improving creative feedback by making the feedback more specific, justified, and actionable (Ngoon et al., 2018). This notion of adaptive conceptual guidance is further explored by Shöwn (Ngoon et al., 2021), demonstrating the utility of adapting presented design suggestions and examples automatically given the user’s current working context. Our plugin provides in-context design feedback grounded by this prior work on user interfaces for design feedback, while automatically generating the provided feedback and design suggestions.

**ZH** 前人研究探索了多种方式，在各类媒介上支持设计师给出与接收反馈（Kulkarni 等，2015；Luther 等，2015；Warner 等，2023；Yoon 等，2014；Pavel 等，2016）。Cheng 等人考察了从在线论坛公开收集设计反馈的过程（Cheng 等，2020），并列出了反馈系统的若干设计考量。在支持平面设计的情境内反馈方面，CritiqueKit（Fraser 等，2017）展示了用于提供与改进实时设计反馈的界面，Charrette（O’Leary 等，2018）则支持对更长历史与多个设计变体的反馈进行组织与共享。Ngoon 等人的研究表明，复用专家反馈建议与自适应引导是改进创意反馈的两种途径，可使反馈更具体、更有依据、更可执行（Ngoon 等，2018）。这种自适应概念引导的思路在 Shöwn（Ngoon 等，2021）中得到进一步探索，证明根据用户当前工作情境自动调整所呈现的设计建议与示例是有效的。我们的插件在情境内提供设计反馈，其依据正是这些关于设计反馈界面的前人工作，区别在于反馈与设计建议由系统自动生成。

**EN** 3. System Details

**ZH** 3. 系统细节

**EN** In this section, we describe the set of design goals for an automatic LLM-driven heuristic evaluation tool, how they are realized in our system, the underlying implementation, techniques to improve the LLM’s performance, and explorations of alternative prompt designs and various LLM models for this task.

**ZH** 本节介绍自动化 LLM 驱动启发式评估工具的一组设计目标、这些目标在系统中的实现方式、底层实现、提升 LLM 表现的技术，以及对替代性提示设计和多种 LLM 模型在该任务上的探索。

**EN** 3.1. Design Goals

**ZH** 3.1. 设计目标

**EN** Based on design principles and expected LLM behavior, we came up with a set of goals that lay out what an automatic LLM-based heuristic evaluation tool should be able to do. The goals are as follows:

**ZH** 基于设计原则与 LLM 的预期行为，我们提出了一组目标，用以界定一个自动化、基于 LLM 的启发式评估工具应当具备的能力。目标如下：

**EN** (1) The tool should be able to accommodate arbitrary UI prototypes; designers should be able to use this tool to perform heuristic evaluations on their mockups and identify potential issues, before implementation.

**ZH** （1）工具应能适配任意 UI 原型：设计师可用它在实现之前对原型稿执行启发式评估并发现潜在问题。

**EN** (2) The tool should be heuristic-agnostic, so different guidelines or heuristics can be used.

**ZH** （2）工具应与具体启发式准则无关，从而可使用不同的准则或启发法。

**EN** (3) The guideline violations detected by the LLM should be presented in a way that adheres to the principles of effective feedback (Sadler, 1989).

**ZH** （3）LLM 检测到的准则违反项，其呈现方式应遵循有效反馈的原则（Sadler，1989）。

**EN** (4) The LLM generated feedback should be presented in the context of the critiqued design. This is to narrow the gulf of evaluation, making it easier for designers to interpret the feedback.

**ZH** （4）LLM 生成的反馈应置于被评审设计的情境中呈现，以缩小评估鸿沟，让设计师更容易理解反馈。

**EN** (5) Finally, in case the LLM makes a mistake, the designer should be able to hide feedback they find unhelpful. This data should also be sent to the LLM to improve its prediction accuracy.

**ZH** （5）万一 LLM 出错，设计师应能隐藏自己认为无用的反馈；这些数据也应回传给 LLM，以提升其预测准确性。

**EN** 3.2. Design Walkthrough

**ZH** 3.2. 设计走查

<!-- [原子块 · img]  -->

**EN** Figure 2. Illustration of plugin interactions that contextualize text feedback with the UI. “A” shows that clicking on a link in the violation text selects the corresponding group or element in the Figma mockup and Layers panel. “B” shows the “click to focus” feature, where clicking on a violation fades the other violations and draws a box around the corresponding group in the UI screenshot. “C” illustrates that hovering over a group or element link draws a blue box around the corresponding element in the screenshot. “D” points out that clicking on the ‘X’ icon of a violation hides it and adds this feedback to the LLM prompt for the next round of evaluation.Three side by side images. A screenshot of the violations text, a screenshot of a UI mockup, and a screenshot of the layers panel with a screenshot of the Figma mockup below. A box is drawn around ‘Group 406’ and it corresponds to the group selected in the layers panel and the Figma mockup.

**ZH** 图 2. 插件交互示意：把文本反馈与 UI 关联起来。“A”表示点击违反项文本中的链接，会在 Figma 原型稿和图层面板中选中对应的分组或元素；“B”表示点击聚焦功能，点击某条违反项会淡化其他违反项，并在 UI 截图中为该分组绘制边框；“C”表示悬停在分组或元素链接上时，会在截图中为对应元素绘制蓝色边框；“D”表示点击违反项的 X 图标会隐藏该条反馈，并把这条反馈加入下一轮评估的 LLM 提示中。三张并排的图：违反项文本截图、UI 原型稿截图，以及图层面板截图（其下方为 Figma 原型稿截图）。Group 406 周围画有边框，与图层面板和 Figma 原型稿中被选中的分组相对应。

**EN** We built our tool as a plugin for Figma, enabling designers to evaluate any Figma mockup (Goal 1). Figure 1 illustrates this plugin’s step-by-step usage with interface screenshots. The designer first prototypes their UI in Figma and runs the plugin (Figure 1 Box A). Due to context window limitations, the plugin only evaluates a single UI screen at a time. Furthermore, it only assesses static mockups, as evaluation of interactive mockups may require multiple screens as input or more complex UI representations, which could exceed the LLM’s context limit. After starting the plugin, it opens up a page to select guidelines to use for heuristic evaluation (Box B). Designers can select from a set of well-known guidelines, like Nielsen’s 10 Usability Heuristics, or enter any list of heuristics they would like to use (Goal 2). They can also select more than one set of guidelines for the evaluation.

**ZH** 我们把工具实现为 Figma 插件，使设计师能够评估任意 Figma 原型稿（目标 1）。图 1 以界面截图展示了该插件的分步使用方式：设计师先在 Figma 中制作 UI 原型并运行插件（图 1 框 A）。受上下文窗口限制，插件一次只评估一个 UI 屏幕，且只评估静态原型稿——评估交互式原型可能需要多个屏幕作为输入或更复杂的 UI 表示，从而超出 LLM 的上下文上限。启动插件后，会打开一个页面供选择用于启发式评估的准则（框 B）。设计师既可从若干知名准则中选择，如 Nielsen 的 10 条可用性启发式准则，也可输入自己想用的任意启发式准则列表（目标 2），还能为一次评估选择多套准则。

**EN** Once the LLM completes the heuristic evaluation, text explanations of all violations found and a UI screenshot are rendered back to the designer (Figure 1 Box C). This “UI Snapshot” serves as a reference to the state of the mockup at the time of evaluation, in case the designer makes any changes based on the evaluation results. Each violation explanation contains the name of the violated guideline and is phrased as constructive feedback, following the guidelines set by Sadler et al. (Sadler, 1989) (Goal 3). According to Sadler, effective feedback is specific and relevant, highlighting the performance gap and providing actionable guidance for improvement. To accomplish this, the feedback must include these three things: 1) the expected standard, 2) the gap between the quality of work and the standard, and 3) what needs to be done to close this gap. Our design feedback adheres to Sadler’s principles and starts by stating the standard set by the guideline, followed by the issue with the current design (the gap between the design and expected standard), and concludes with advice on fixing the issue. Figure 9 provides four examples of these explanations.

**ZH** LLM 完成启发式评估后，系统会把所有违反项的文本说明与一张 UI 截图呈现给设计师（图 1 框 C）。这张 UI 快照记录了评估时刻原型稿的状态，供设计师据评估结果做出修改后对照参考。每条违反项说明都包含被违反准则的名称，并按建设性反馈的方式表述，遵循 Sadler 提出的准则（Sadler，1989）（目标 3）。Sadler 认为，有效反馈应当具体且切题，指出表现差距并给出可执行的改进指导。为此，反馈须包含三件事：1）期望标准；2）当前工作质量与该标准之间的差距；3）为弥合差距需要做什么。我们的设计反馈遵循这一原则：先说明准则设定的标准，再指出当前设计的问题（设计与期望标准之间的差距），最后给出修复建议。图 9 给出了四条这类说明的示例。

**EN** The plugin also includes several features that help designers contextualize the text feedback with corresponding UI elements. (Goal 4). Figure 2 illustrates these features. Selecting a violation fades the other suggestions and draws a box around the relevant group or element in the screenshot, as shown in Figure 2 (B). In addition, all UI elements and groups mentioned are rendered as links. Hovering over a link draws a box over the corresponding group or element in the screenshot (C), and clicking on the link selects the item in the Figma mockup and Layers panel (A), streamlining the editing process. Finally, to address Goal 5, if the designer finds a suggestion incorrect or unhelpful, they can click on its ‘X’ icon to hide it (D). Hiding the violation sends feedback to the LLM for subsequent evaluation rounds so this violation will not be shown again.

**ZH** 插件还包含若干功能，帮助设计师把文本反馈与相应的 UI 元素对应起来（目标 4）。图 2 展示了这些功能：选中一条违反项会淡化其他建议，并在截图中为相关分组或元素绘制边框（图 2 B）。此外，所有被提及的 UI 元素与分组都渲染为链接——悬停在链接上会在截图中为对应分组或元素绘制边框（C），点击链接则会在 Figma 原型稿和图层面板中选中该条目（A），从而简化编辑流程。为满足目标 5，若设计师认为某条建议不正确或无用，可点击其 X 图标将其隐藏（D）；隐藏该违反项会把反馈发送给 LLM，用于后续轮次的评估，使该违反项不再出现。

**EN** After the designer revises their mockup based on LLM feedback, they can rerun the evaluation to generate new suggestions. This usage is intended to match the iterative feedback and revision process during design. The plugin uses the information from the Layers panel of Figma to create the text-based representation of the mockup (discussed in more detail in the next section). Hence, it relies on accurate names for groups in the Layers panel to convey semantic information about the UI; for instance, the group containing icons in the navbar should be named “navbar”. Designers must manually add these names, so they are often missing. To address this, we implemented an auxiliary label generation feature that can be run before evaluation to generate group names automatically (based on their contents).

**ZH** 设计师依据 LLM 反馈修改原型稿后，可重新运行评估以生成新的建议，旨在贴合设计中反复反馈与修改的过程。插件利用 Figma 图层面板中的信息构建原型稿的文本化表示（下一节详述），因此它依赖图层面板中准确的分组名称来传达 UI 的语义信息，例如导航栏中包含图标的分组应命名为 navbar。这些名称需要设计师手动添加，因此常常缺失。为此，我们实现了一项辅助的标签生成功能，可在评估前运行，根据分组内容自动生成分组名称。

**EN** 3.3. Implementation

**ZH** 3.3. 实现

<!-- [原子块 · img]  -->

**EN** Figure 3. Our LLM-based plugin system architecture. The designer prototypes a UI in Figma (Box 1), and the plugin generates a UI representation to send to an LLM (3). The designer also selects heuristics/guidelines to use for evaluating the prototype (2), and a prompt containing the UI representation (in JSON) and guidelines is created and sent to the LLM (4). After identifying all the guideline violations, another LLM query is made to rephrase the guideline violations into constructive design advice (4). The LLM response is then programmatically parsed (5), and the plugin produces an interpretable representation of the response to display (6). The designer dismisses incorrect suggestions, which are incorporated in the LLM prompt for the next round of evaluation, if there is room in the context window (7). A flow chart illustrating the system design of the plugin. Source design is labeled 1 and Heuristics is labeled 2. There is an arrow from Source Design to Generate Condensed JSON Representation for LLM (labeled 3). Generate Condensed JSON Representation for LLM and Heuristics both point to LLM Queries for Evaluation and Rephrasing (labeled 4), which points to Parse Result (5), which points to Generate Representation for Designer (6). Generate Representation for Designer points to LLLM Queries for Evaluation and Rephrasing going through a box label 7 saying Feedback from Designer

**ZH** 图 3. 基于 LLM 的插件系统架构。设计师在 Figma 中制作 UI 原型（框 1），插件生成 UI 表示并发送给 LLM（3）；设计师同时选择用于评估原型的启发式准则与设计准则（2），系统把包含 UI 表示（JSON 格式）与准则的提示发送给 LLM（4）。识别出所有准则违反项后，再发起一次 LLM 查询，把这些违反项改写为建设性的设计建议（4）。随后以程序解析 LLM 的响应（5），插件生成可理解的表示用于展示（6）。设计师关闭不正确的建议，若上下文窗口还有余量，这些建议会被纳入下一轮评估的 LLM 提示（7）。一幅说明插件系统设计的流程图：源设计标为 1，启发式准则标为 2；从源设计有箭头指向为 LLM 生成精简 JSON 表示（标为 3）；为 LLM 生成精简 JSON 表示与启发式准则共同指向评估与改写的 LLM 查询（标为 4），后者指向解析结果（5），再指向为设计师生成表示（6）；为设计师生成表示经一个标为 7、写着来自设计师反馈的框，回指到评估与改写的 LLM 查询。

<!-- [原子块 · img]  -->

**EN** Figure 4. An example portion of a UI JSON. It has a tree structure, where each node has a list of child nodes (the “children” field). Each node in this JSON is color-coded with its corresponding group or element in the UI screenshot. The node named “lyft event photo and logo” is a group (“type: GROUP”) consisting of a photo of the live chat event (“lyft live chat event photo”) and the Lyft logo (“lyft logo”). The JSON node for the photo contains its location information (“bounds”), type (“IMAGE”), and unique identifier (“id”). The JSON node for “lyft logo” contains its location and some stylistic information, like the stroke color and stroke weight for its white border. UI Mockup Screenshot on the left and a snippet of JSON on the right. There are boxes marking corresponding sections in the JSON and screenshot. There is a box around the photo and the section is highlighted in JSON, which contains the photo name, type (image), and bounding box coordinates. Similar correspondences are drawn between the Lyft logo and the group.

**ZH** 图 4. UI JSON 的一个片段示例。它呈树状结构，每个节点都有一个子节点列表（children 字段）。该 JSON 中的每个节点都以颜色与 UI 截图中对应的分组或元素相配。名为 lyft event photo and logo 的节点是一个分组（type: GROUP），由直播活动照片（lyft live chat event photo）和 Lyft 标志（lyft logo）组成。照片的 JSON 节点包含其位置信息（bounds）、类型（IMAGE）与唯一标识符（id）。lyft logo 的 JSON 节点包含其位置及部分样式信息，例如白色描边的描边颜色与描边粗细。左侧为 UI 原型稿截图，右侧为 JSON 片段，两者之间用方框标出对应部分：照片周围画有方框，并在 JSON 中高亮了相应片段，其中包含照片名称、类型（image）与边界框坐标；Lyft 标志与分组之间也画出了类似的对应关系。

**EN** We implemented this plugin in Typescript using the Figma Plugin API. The plugin makes an API request to OpenAI’s GPT-4 for LLM queries. Since LLMs can only accept text as input, the plugin takes in a JSON representation of the UI. While multi-modal models exist that could take in both the UI screenshot and guidelines text (e.g., (Liu et al., 2023b)), we found that its performance was considerably worse than GPT-4’s for this task (at the time).

**ZH** 我们用 TypeScript 借助 Figma 插件 API 实现了该插件，LLM 查询通过 API 请求调用 OpenAI 的 GPT-4。由于 LLM 只能接受文本输入，插件采用 UI 的 JSON 表示。虽然已有能同时接收 UI 截图与准则文本的多模态模型（例如 Liu 等，2023b），但我们发现当时其在该任务上的表现明显不如 GPT-4。

**EN** Our JSON format captures the DOM (Document Object Model) structure of the UI mockup, and is similar in structure and content to the HTML-based representation used by (Wang et al., 2023) that performed well on UI-related tasks. Figure 4 contains an example portion of a UI JSON with corresponding groups and elements marked in the UI screenshot. The tree structure is informative of the overall organization of the UI, with UI elements (buttons, icons, etc.) as leaves and groups (of elements and/or smaller groups) as intermediate nodes. Each node in this JSON tree contains semantic information (text labels, element or group names, and element type) and visual data (x,y-position of the top left corner, height, width, color, opacity, background color, font, etc.) of its element or group. Hence, this JSON representation captures both semantic and visual features of the UI, which supports the evaluation of various aspects of the design and differentiates it from the representation used by (Wang et al., 2023) that captures only semantic information. This JSON representation is constructed from the data (e.g., group/element names) and grouping structure found in the Layers panel of Figma, which are editable by designers.

**ZH** 我们的 JSON 格式刻画了 UI 原型稿的 DOM（文档对象模型）结构，在结构与内容上类似于 Wang 等人（Wang 等，2023）所使用的、在 UI 相关任务上表现良好的基于 HTML 的表示。图 4 给出了一个 UI JSON 的片段示例，并在 UI 截图中标出了对应的分组与元素。树状结构反映了 UI 的整体组织：UI 元素（按钮、图标等）位于叶节点，分组（由元素或更小的分组构成）位于中间节点。JSON 树中的每个节点都包含其元素或分组的语义信息（文本标签、元素或分组名称、元素类型）与视觉数据（左上角 x、y 坐标、高度、宽度、颜色、不透明度、背景色、字体等）。因此，这一 JSON 表示同时刻画了 UI 的语义与视觉特征，支持对设计多个方面的评估；这也区别于 Wang 等人（Wang 等，2023）所用的、只刻画语义信息的表示。该 JSON 表示由 Figma 图层面板中的数据（如分组与元素名称）与分组结构构建而成，设计师可对这些内容进行编辑。

**EN** Figure 3 shows the core system design of the plugin. Due to the context window limits of GPT-4, we remove all unnecessary or redundant information and condense verbose details into a concise JSON structure (Box 3). This condensed JSON representation and guideline text are combined into a prompt sent to the LLM. After the LLM returns the identified guideline violations, another query is sent to the LLM to convert these violations into constructive advice (Box 4). This chain of prompts is illustrated in Figure 12 (Appendix), which describes the components of each prompt. The LLM response is parsed by the TypeScript code (Box 5) and rendered into an interpretable format for designers (Box 6). Figma IDs for each element and group are stored internally, which supports selection of elements or groups in the mockup via links (Figure 2, A) and quick access to their layout information. Layout information is used to draw boxes around elements and groups in the screenshot, as shown in Figure 2 (B and C). Finally, unhelpful suggestions that were dismissed by the designer are incorporated into the prompt for the next round of evaluation (Box 7), if there is room in the context window. The label generation feature is also executed via an LLM call, with the prompt containing JSON data of all unnamed groups and instructions for the LLM to create a descriptive label for each JSON based on its contents.

**ZH** 图 3 展示了插件的核心系统设计。受 GPT-4 上下文窗口限制，我们剔除所有不必要或冗余的信息，并把冗长的细节压缩为精简的 JSON 结构（框 3）。这一精简 JSON 表示与准则文本被组合成提示发送给 LLM；LLM 返回识别出的准则违反项后，系统再发起一次查询，将这些违反项转换为建设性建议（框 4）。这一提示链如图 12（附录）所示，其中描述了每个提示的组成部分。LLM 的响应由 TypeScript 代码解析（框 5），并渲染为设计师可理解的格式（框 6）。系统内部保存每个元素与分组的 Figma ID，用以支持通过链接在原型稿中选中元素或分组（图 2 A），并快速访问其布局信息；布局信息则用于在截图中为元素和分组绘制边框，如图 2（B 和 C）所示。被设计师关闭的无用建议会被纳入下一轮评估的提示（框 7），前提是上下文窗口还有余量。标签生成功能同样通过一次 LLM 调用执行，其提示包含所有未命名分组的 JSON 数据，以及让 LLM 依据内容为每个 JSON 生成描述性标签的指令。

**EN** 3.4. Improving LLM Performance

**ZH** 3.4. 提升 LLM 表现

**EN** We chose the most advanced GPT version available (GPT-4), as it has the strongest reasoning abilities (OpenAI, 2023). However, GPT-4 does not support fine-tuning and has a context window limit of 8.1k tokens. This context window limit leaves inadequate room for few-shot and “chain-of-thought” (Wei et al., 2023) examples because each Figma UI JSON requires around 3-5k tokens, the guidelines text take up to 2k tokens, and few-shot and chain-of-thought examples both require the corresponding UI JSONs. Due to these limitations, our method for improving GPT-4’s performance entailed adding explicit instructions in the prompt to avoid common mistakes, as shown in Figure 12 (Appendix). Finally, we set the temperature to 0 to ensure GPT-4 returns the most probable violations.

**ZH** 我们选用了当时最先进的 GPT 版本（GPT-4），因为它具备最强的推理能力（OpenAI，2023）。不过，GPT-4 不支持微调，且上下文窗口上限为 8.1k token，这使少样本与思维链（Wei 等，2023）示例几乎没有可用空间：每个 Figma UI JSON 约需 3–5k token，准则文本最多占 2k token，而少样本与思维链示例又都需要相应的 UI JSON。受这些限制，我们提升 GPT-4 表现的方法是在提示中加入明确的指令以避免常见错误，如图 12（附录）所示。最后，我们把温度设为 0，以确保 GPT-4 返回最可能的违反项。

**EN** The remaining space in the context window was allocated to suggestions that were dismissed (hidden) by designers. Incorporating this feedback targets areas of poor performance specific to the UI being evaluated and also adapts GPT-4’s feedback to the designer’s preferences. Since the UI JSON is already provided in the prompt, this feedback does not require much space. However, the UI may have changed due to edits, so JSONs of the groups/elements for a dismissed violation are still included, but they are considerably smaller than the entire UI JSON. These items are incorporated in the conversation history of the next prompt, as examples of inaccurate suggestions (see Figure 12 in the Appendix). In addition, we ask GPT-4 to reflect on why it was wrong and add this prompt and its response to the conversation history. This “self-reflection” has been shown to improve LLM performance (Shinn et al., 2023).

**ZH** 上下文窗口的剩余空间被分配给设计师关闭（隐藏）的建议。纳入这些反馈，可针对当前被评估 UI 上表现不佳的方面加以改进，也能让 GPT-4 的反馈更贴合设计师的偏好。由于提示中已提供 UI JSON，这些反馈并不需要太多空间；但 UI 可能因编辑而发生变化，因此仍会包含被关闭违反项所涉及分组或元素的 JSON，不过其规模远小于完整 UI JSON。这些条目会以不准确建议示例的形式纳入下一次提示的对话历史（见附录图 12）。此外，我们要求 GPT-4 反思自己为何出错，并把这条提示及其响应加入对话历史；这种自我反思已被证明能提升 LLM 的表现（Shinn 等，2023）。

**EN** 3.5. Exploration of Alternative Prompt Compositions

**ZH** 3.5. 替代性提示构成的探索

<!-- [原子块 · table] Prompt Condition Total Violations Helpful Violations Complete (Plugin) 63 38 One Call 62 31 No Heuristics 50 14 General UI Feedback 57 24 -->

<!-- [原子块 · table] LLM Total Violations Helpful Violations GPT-4 (Plugin) 63 38 GPT-3.5-16k 228 23 Claude 2 7 1 PaLM 2 12 3 -->

**EN** Table 1. The top table compares the total number of violations and the number of helpful violations (based on the authors’ judgement) found in 12 UI mockups for different prompt compositions. The “Complete (Plugin)” condition refers to the prompt composition used in the plugin. The bottom table compares the total number of violations and the number of helpful violations (based on the authors’ judgement) found in the 12 UI mockups by each LLM, with GPT-4 being used in the plugin.

**ZH** 表 1. 上表比较了在 12 个 UI 原型稿上，不同提示构成下发现的违反项总数与有用违反项数量（依据作者判断）。完整（插件）条件指插件实际使用的提示构成。下表比较了各个 LLM 在这 12 个 UI 原型稿上发现的违反项总数与有用违反项数量（依据作者判断），其中 GPT-4 被用在插件中。

**EN** We investigate how different prompt components influence GPT-4’s output to identify potential opportunities for simplifying our complex prompt. For our analysis, we used 12 distinct mockups of mobile UIs taken from the Figma community. Furthermore, we used three sets of heuristics covering different aspects of UI design: Nielsen’s 10 Usability Heuristics (Nielsen, 1992), Luther et al.’s visual design principles compiled in “CrowdCrit” (Luther et al., 2014), and Duan et al.’s 5 semantic grouping guidelines (Duan et al., 2023). These 12 UIs and three sets of heuristics were consistently used in all subsequent analyses and studies in this paper, except for the Performance Study, which used a larger set of 51 UIs. We query the LLM with prompt variations and then compute the total number of reported violations and the number of helpful violations (based on the authors’ judgment), and we also qualitatively examine the violations. We consider a violation to be helpful if it is both accurate and would lead to an improvement in the design. Table 1 (“Prompt Condition”) compares violation counts for each condition with the complete prompt chain.

**ZH** 我们考察不同提示组件如何影响 GPT-4 的输出，以寻找简化这套复杂提示的可能。分析使用了取自 Figma 社区的 12 个不同移动端 UI 原型稿，并采用覆盖 UI 设计不同方面的三套启发式准则：Nielsen 的 10 条可用性启发式准则（Nielsen，1992）、Luther 等人在 CrowdCrit 中汇总的视觉设计原则（Luther 等，2014），以及 Duan 等人的 5 条语义分组准则（Duan 等，2023）。除性能研究使用了更大的 51 个 UI 集合外，本文后续所有分析与研究都统一使用这 12 个 UI 与三套启发式准则。我们用不同的提示变体查询 LLM，统计报告的违反项总数与有用违反项数量（依据作者判断），并对违反项做定性考察；我们把既准确又能带来设计改进的违反项视为有用。表 1（提示条件）比较了各条件下与完整提示链下的违反项数量。

**EN** 3.5.1. One Call

**ZH** 3.5.1. 单次调用

**EN** Our prompt chain makes two LLM calls – one to carry out the heuristic evaluation and the other to rephrase results into constructive feedback (Appendix Figure 12). We examine the effects of combining these two into a single call, as this would reduce latency. Quantitatively, the total number of violations remained similar, but the number of helpful violations was lower. However, more importantly, the output was never formatted correctly with one call, and the format also varied across different calls. Furthermore, GPT-4 sometimes omitted other important details, such as how to fix the violation. Since correct output formatting is necessary for the plugin to parse and render the violations, combining the two calls is not feasible.

**ZH** 我们的提示链包含两次 LLM 调用：一次执行启发式评估，另一次把结果改写为建设性反馈（附录图 12）。我们考察了把两者合并为单次调用的效果，因为这可以降低延迟。从数量上看，违反项总数基本不变，但有用违反项数量更少；更重要的是，单次调用时输出格式从未正确，且格式在不同调用之间还会变化。此外，GPT-4 有时会遗漏其他重要细节，例如如何修复该违反项。由于插件解析与渲染违反项需要正确的输出格式，合并两次调用并不可行。

**EN** 3.5.2. No Heuristics

**ZH** 3.5.2. 不提供启发式准则

**EN** The detailed heuristics text occupies a lot of space in the LLM’s context window, so we examined the performance without including them in the prompt. We edited prompts to look for “visual design issues”, “usability issues”, or “semantic group issues” instead of passing in the heuristics.

**ZH** 详细的启发式准则文本占用了 LLM 上下文窗口的大量空间，因此我们考察了不把它们放入提示时的表现：改写提示去查找视觉设计问题、可用性问题或语义分组问题，而不再传入启发式准则。

**EN** Table 1 (top) shows that GPT-4 provided fewer suggestions total (50 vs. 63) and considerably fewer helpful suggestions when heuristics were not included in the prompt (14 vs. 38). Qualitatively, the suggestions for Crowdcrit and Nielsen were similar to those from the complete prompt, though the suggestions were more thorough when the Crowdcrit heuristics were included. However, for Semantic Grouping, not passing in the heuristics resulted in only violations that concerned the semantic relatedness of group members, whereas passing in the guidelines resulted in a more diverse set of issues found. We conclude that while the LLM could give plausible UI feedback without passing in heuristics, the quality of the suggestions is worse.

**ZH** 表 1（上表）显示，提示中不放入启发式准则时，GPT-4 给出的建议总数更少（50 对 63），有用建议更是大幅减少（14 对 38）。定性来看，针对 CrowdCrit 与 Nielsen 的建议与完整提示下的结果相近，只是在纳入 CrowdCrit 启发式准则时建议更为详尽；但在语义分组方面，不传入准则时只发现了涉及分组成员语义相关性的违反项，而传入准则后发现的问题类型更为多样。我们的结论是：虽然 LLM 在不传入启发式准则时也能给出说得通的 UI 反馈，但建议质量更差。

**EN** 3.5.3. General UI Feedback

**ZH** 3.5.3. 通用 UI 反馈

**EN** Finally, we investigate how GPT-4 responds without specific guidance when prompted for general UI feedback. We removed all mentions of “guidelines” in the prompt and replaced “violations” with “feedback.” Quantitatively, the performance for this condition was worse. Qualitatively, GPT-4 still carried out heuristic evaluation to an extent, as the issues were grounded in existing design conventions, but in a less rigorous and organized manner. Compared to the complete prompt, the feedback was less diverse, and the LLM often focused on only one type of issue (e.g., misalignment) when there were other types of violations. We conclude that GPT-4 can produce plausible output when asked for general UI feedback, but specific guidance produces higher quality and more diverse suggestions.

**ZH** 我们还考察了在没有具体指引、只要求给出通用 UI 反馈时 GPT-4 的反应：移除提示中所有准则的提法，并把违反项换成反馈。从数量上看，该条件下的表现更差。定性来看，GPT-4 仍在一定程度上执行了启发式评估，因为它指出的问题都源于既有的设计惯例，只是不够严谨、不够有条理。与完整提示相比，反馈的多样性不足，且 LLM 常只聚焦于某一类问题（例如对齐问题），而无视其他类型的违反项。我们的结论是：GPT-4 在被要求给出通用 UI 反馈时能产出说得通的结果，但具体指引能带来质量更高、更丰富的建议。

**EN** 3.6. Comparison with other LLMs

**ZH** 3.6. 与其他 LLM 的比较

**EN** We explored the potential of other state-of-the-art LLMs in carrying out this task: Claude 2, GPT-3.5-turbo-16k, and PaLM 2. Llama 2 was considered but excluded because its 4k context window size is insufficient for the task. Similar to the prompt analysis, we compute the total number of violations found and the number of helpful violations.

**ZH** 我们考察了其他最先进 LLM 执行该任务的潜力：Claude 2、GPT-3.5-turbo-16k 与 PaLM 2。Llama 2 曾被考虑，但因其 4k 的上下文窗口不足以完成该任务而被排除。与提示分析类似，我们统计发现的违反项总数与有用违反项数量。

**EN** We found that Claude 2, GPT-3.5-turbo-16k, and PaLM 2 all had considerably worse performance than GPT-4, as shown in Table 1 (bottom). Claude 2 and PaLM 2 found very few violations; Claude 2 only found violations in 4 UIs, and PaLM 2 only identified one violation per UI, even after adjusting the prompt to indicate more than one violation per UI. In fact, all 12 UIs have multiple violations, as later confirmed in a heuristic evaluation by human experts. The few violations found by these two LLMs were mostly unhelpful, such as suggesting the dollar sign needs a text label. GPT-3.5-turbo-16k had the opposite behavior, finding nearly 4 times as many violations as GPT-4. However, most of the time, it indiscriminately applied the same guideline to every element of the appropriate type, regardless if there is an issue (e.g., stating the font is difficult to read for every text element). This behavior also meant that most of its helpful violations were found by chance, despite finding fewer helpful violations than GPT-4. Finally, GPT-3.5-turbo-16k and PaLM 2 had difficulty following the prompt’s instructions, often formatting the output incorrectly (with a separate rephrasing call) or making the mistakes they were told to avoid, such as returning violations regarding the mobile status bar.

**ZH** 如表 1（下表）所示，Claude 2、GPT-3.5-turbo-16k 与 PaLM 2 的表现都明显不如 GPT-4。Claude 2 与 PaLM 2 发现的违反项极少：Claude 2 只在 4 个 UI 中发现了违反项，PaLM 2 即便在调整提示以说明每个 UI 可有多处违反项后，也仍只报告一处。而事实上，正如后来人类专家的启发式评估所确认，全部 12 个 UI 都有多处违反项。这两个 LLM 找出的少量违反项大多并无用处，例如建议美元符号需要文本标签。GPT-3.5-turbo-16k 的表现则相反，它发现的违反项接近 GPT-4 的 4 倍；但在多数情况下，它不加区分地把同一条准则套用到每个相应类型的元素，而不管是否真有问题（例如对每个文本元素都说字体难以辨认）。这也意味着它发现的有用违反项大多是碰巧所得，其有用违反项总数仍少于 GPT-4。最后，GPT-3.5-turbo-16k 与 PaLM 2 难以遵循提示指令，常常输出格式出错（即便有独立的改写调用），或犯下被明确要求避免的错误，例如返回与手机状态栏有关的违反项。

**EN** These models are all smaller than GPT-4, with billions of parameters, compared to GPT-4’s 1.7 trillion (OpenAI, 2023). These models have also been shown to have worse reasoning skills (Borji and Mohammadian, 2023). These factors likely contributed to their poor performance in this task. Since GPT-4 has the best performance by far, we solely focus on GPT-4 for the remaining three studies on the plugin.

**ZH** 这些模型的规模都小于 GPT-4，参数量在数十亿级别，而 GPT-4 为 1.7 万亿（OpenAI，2023）；已有研究也表明它们的推理能力更弱（Borji 和 Mohammadian，2023）。这些因素很可能共同导致了它们在该任务上的糟糕表现。既然 GPT-4 的表现远超其他模型，我们在余下三项针对该插件的研究中只关注 GPT-4。

**EN** 4. Study Method

**ZH** 4. 研究方法

<!-- [原子块 · img]  -->

**EN** Figure 5. An illustration of the formats of the three studies. The Performance Study consists of 3 raters evaluating the accuracy and helpfulness of GPT-4-generated suggestions for 51 UI mockups. The Heuristic Evaluation Study with Human Experts consists of 12 design experts, who each looked for guideline violations in 6 UIs, and finishes with an interview asking them to compare their violations with those found by the LLM. Finally, the Iterative Usage study comprises of another group of 12 design experts, each working with 3 UI mockups. For each mockup, the expert iteratively revises the design based on the LLM’s valid suggestions and rates the LLM’s feedback, going through 2-3 rounds of this per UI. The Usage study concludes with an interview about the expert’s experience with the tool.Illustration of the three studies. For the performance study, there are arrows going from 51 UI mockups to 3 raters to 51 UIs x ~5 suggestions per UI x 3 raters = 765 ratings. For the heuristic evaluation with human experts study, there are arrows going from 6 UI mockups to 12 Design Experts to Guideline Violations in UI Mockups to Interview. For the usage study, there is a cycle starting with 3 UI mock ups going to 12 design experts going to accuracy and helpfulness ratings going to iterative redesign and then back to 3 UI mockups. There is also an arrow going from this cycle to interview.

**ZH** 图 5. 三项研究的形式示意。性能研究由 3 位评分者对 51 个 UI 原型稿的 GPT-4 生成建议的准确性与有用性打分。与人类专家的启发式评估研究由 12 位设计专家组成，每人查找 6 个 UI 中的准则违反项，最后通过访谈请他们把自己找到的违反项与 LLM 找到的做比较。迭代使用研究则由另外 12 位设计专家组成，每人处理 3 个 UI 原型稿：对每个原型稿，专家依据 LLM 的有效建议迭代修改设计并对 LLM 反馈打分，每个 UI 经历 2–3 轮；使用研究最后以访谈收尾，询问专家使用该工具的体验。三幅研究形式示意图：性能研究中，箭头从 51 个 UI 原型稿指向 3 位评分者，再指向 51 个 UI × 每 UI 约 5 条建议 × 3 位评分者 = 765 条评分；人类专家启发式评估研究中，箭头从 6 个 UI 原型稿指向 12 位设计专家，再指向 UI 原型稿中的准则违反项，最后指向访谈；使用研究则是一个循环，从 3 个 UI 原型稿到 12 位设计专家，到准确性与有用性评分，到迭代再设计，再回到 3 个 UI 原型稿，另有一条箭头从该循环指向访谈。

**EN** To explore the potential of GPT-4 in automating heuristic evaluation, we carried out three studies (see Figure 5). In the Performance study, three designers rated the accuracy and helpfulness of GPT-4’s generated suggestions for 51 diverse UI mockups to establish performance metrics across a variety of designs. Next, we conducted a heuristic evaluation study with 12 design experts, who each manually identified guideline violations in 6 UIs. Afterwards, they compared their identified violations with those found by GPT-4 in an interview. Finally, in the Iterative Usage study, another group of 12 designers iteratively refined three UIs each with the tool and discussed how the tool might fit into existing workflows in an interview. We obtained UIs from the Figma Community, where designers share their mockups publicly. To attain a diverse set of UIs, we searched for UIs from various app categories, such as finance and e-commerce. We selected UIs that have room for improvement (based on our guidelines) and have JSON representations that could fit into GPT-4’s context window. We only used mobile UIs because web UIs were usually too large. For each UI, we ensured that the grouping structure in the Layers panel matched the visual grouping structure in the UI screenshot. We also used our tool to automatically generate semantically informative names for unnamed groups in the Layers panel.

**ZH** 为探索 GPT-4 自动化启发式评估的潜力，我们开展了三项研究（见图 5）。在性能研究中，三位设计师对 51 个多样化 UI 原型稿上 GPT-4 生成建议的准确性与有用性打分，以在多种设计上建立性能指标。接着，我们开展了一项有 12 位设计专家参与的启发式评估研究：每人手工找出 6 个 UI 中的准则违反项，随后在访谈中把自己找到的违反项与 GPT-4 找到的做比较。最后，在迭代使用研究中，另外 12 位设计师借助该工具迭代改进各 3 个 UI，并在访谈中讨论该工具如何融入现有工作流程。这些 UI 取自 Figma 社区——设计师在其中公开发布自己的原型稿。为获得多样化的 UI，我们检索了金融、电商等不同应用类别，并筛选出（依我们的准则判断）仍有改进空间、且其 JSON 表示能放入 GPT-4 上下文窗口的 UI；我们只使用移动端 UI，因为网页 UI 通常过大。对每个 UI，我们确保图层面板中的分组结构与 UI 截图中的视觉分组结构一致，并用我们自己的工具为图层面板中未命名的分组自动生成具有语义信息的名称。

**EN** 4.1. Performance Study

**ZH** 4.1. 性能研究

**EN** We recruited three designers for the Performance study through advertising at an academic institution. Each participant had 3-4 years of design experience, and their areas of expertise include mobile, web, product, and UX design. This background information was collected during a brief instructional meeting conducted prior to participants starting this task. We precomputed the guideline violations for all 51 UIs to ensure that all participants saw the same suggestions, allowing us to calculate inter-rater agreement. The 51 UIs were split into three groups of 17, and each group was evaluated using one set of guidelines. Each participant saw the same set of 51 UIs and were given a week to rate the suggestions. Participants spent an average of 6.8 hours total on this task.

**ZH** 我们通过在一所学术机构发布广告，为性能研究招募了三位设计师。每位参与者都有 3–4 年设计经验，专长涵盖移动端、网页、产品与用户体验设计；这些背景信息在参与者开始任务前的简短说明会上采集。我们预先计算了全部 51 个 UI 的准则违反项，以确保所有参与者看到相同的建议，从而计算评分者间一致性。51 个 UI 被分成三组、每组 17 个，每组用一套准则评估；每位参与者都要看完同样的 51 个 UI，并有一周时间为建议打分。参与者在该任务上平均共花费 6.8 小时。

**EN** For each suggestion, participants were asked to select a rating for accuracy on a scale of 1 to 3 (“1 - not accurate”, “2 - partially accurate”, “3 - accurate”) and then provide a brief, one-sentence explanation for their rating. Participants were also asked to rate the suggestion’s helpfulness on a scale of 1 to 5, with 1 being “not at all helpful” and 5 being “very helpful”, and also provide a brief explanation. We stored all GPT-4 suggestions, along with the corresponding anonymized rating data, explanations, and UI JSONs from this study, and have made this dataset available in the Supplementary Materials.

**ZH** 对于每条建议，参与者需按 1 至 3 的等级选择准确性评分（1 - 不准确、2 - 部分准确、3 - 准确），并用一句话简要说明评分理由；还需按 1 至 5 的等级对该建议的有用性打分（1 为完全没用，5 为非常有用），同样给出简短说明。我们保存了本研究中 GPT-4 的全部建议，以及相应的匿名评分数据、说明与 UI JSON，并在补充材料中公开了这一数据集。

**EN** 4.2. Manual Heuristic Evaluation Study with Human Experts

**ZH** 4.2. 与人类专家的手工启发式评估研究

**EN** We recruited 12 participants through advertising at a large technology company and an academic institution. Two participants had less than 3 years of design experience, six had 3-5 years, two had 6-10 years, and one had 15 years. Their areas of expertise include mobile, web, product, UX, cross device, and UX and UI research. The study was conducted remotely during a 90-minute session, where participants looked for guideline violations in 6 UIs in a Figma file. Each UI was assigned one of the sets of guidelines for evaluation.

**ZH** 我们通过在一家大型科技公司与一所学术机构发布广告，招募了 12 位参与者。其中 2 位设计经验不足 3 年，6 位为 3–5 年，2 位为 6–10 年，1 位为 15 年；他们的专长涵盖移动端、网页、产品、用户体验、跨设备，以及用户体验与 UI 研究。研究以远程方式进行，时长 90 分钟，参与者在一个 Figma 文件中查找 6 个 UI 的准则违反项，每个 UI 分配一套准则用于评估。

**EN** The first 75 minutes consisted of the heuristic evaluation. Participants were instructed to provide the name of the guideline violated, an explanation of the violation following (Sadler, 1989), and a usability severity rating for each violation found. There were a total of 12 UIs used for this study, and each UI was evaluated by 6 participants. The remaining 15 minutes were allocated for a semi-structured interview, where we demoed the plugin and generated feedback for the same 6 UIs the participant evaluated. We then asked the participants to compare the LLM’s violations with their own.

**ZH** 前 75 分钟为启发式评估：参与者须为发现的每个违反项给出被违反准则的名称、按 Sadler（Sadler，1989）的方式撰写违反项说明，并给出可用性严重程度评级。本研究共使用 12 个 UI，每个 UI 由 6 位参与者评估。其余 15 分钟用于半结构化访谈：我们演示该插件，并针对参与者刚评估过的同样 6 个 UI 生成反馈，然后请参与者把 LLM 的违反项与自己的做比较。

**EN** 4.3. Iterative Usage Study

**ZH** 4.3. 迭代使用研究

**EN** We recruited another group of 12 participants through advertising at an academic institution and a large technology company. One participant had less than 3 years of design experience, five had 3-5 years, three had 6-10 years, two had 11-15 years, and one had over 32 years. Their areas of expertise include mobile, web, product, UX, mixed reality design, and UX and HCI research. The study was conducted either in-person or remotely during a 90-minute session. Participants were given three UIs in a Figma file, each with their corresponding heuristics assigned for the evaluation. Participants worked through one UI at a time. They first rated the accuracy and helpfulness of GPT-4’s suggestions, following the scales used in the Performance Study. However, participants in the Usage study were asked to follow helpful suggestions to edit the mockup, though they could skip revisions that require too much work, like restructuring the entire layout. After participants finished revising the UI, they would rerun the plugin to generate a new set of suggestions for the revised mockup and then re-rate the new suggestions. For UIs 1 and 3, participants did one round of edits and two rounds of ratings. For UI 2, participants did two rounds of edits and three rounds of ratings, which is meant to assess the LLM’s iterative performance. This study used the same set of 12 UIs as the manual heuristic evaluation study (with the same guideline assignments for each UI’s evaluation), and each UI was seen by three participants. To assess rater agreement, we again precomputed the first round suggestions for each UI. After participants finished all three tasks, we concluded with a semi-structured interview, focusing on overall impressions, potential drawbacks and dangers, potential for iterative use, and fit with their design workflow.

**ZH** 我们通过在一家学术机构与一家大型科技公司发布广告，招募了另外 12 位参与者。其中 1 位设计经验不足 3 年，5 位为 3–5 年，3 位为 6–10 年，2 位为 11–15 年，1 位超过 32 年；他们的专长涵盖移动端、网页、产品、用户体验、混合现实设计，以及用户体验与人机交互研究。研究以线下或远程方式进行，时长 90 分钟。参与者拿到一个 Figma 文件中的 3 个 UI，每个 UI 配有相应的启发式准则用于评估，并逐个 UI 完成：他们先按性能研究使用的量表对 GPT-4 建议的准确性与有用性打分；与使用研究不同的是，这里要求参与者依从有用的建议去修改原型稿，但可跳过工作量过大的修改，例如重构整个布局。修改完成后，参与者重新运行插件，为修改后的原型稿生成新一轮建议，并再次对新建议打分。对 UI 1 和 UI 3，参与者做一轮修改、两轮评分；对 UI 2，则做两轮修改、三轮评分，用以考察 LLM 的迭代表现。本研究使用与手工启发式评估研究相同的 12 个 UI（且每个 UI 的准则分配一致），每个 UI 由 3 位参与者评估；为衡量评分者一致性，我们同样预先计算了每个 UI 第一轮的建议。参与者完成三个任务后，我们以半结构化访谈收尾，围绕总体印象、潜在缺陷与风险、迭代使用的可能性，以及与自身设计流程的契合度展开。

**EN** 5. Results

**ZH** 5. 结果

**EN** 5.1. Quantitative Results: Performance Study

**ZH** 5.1. 定量结果：性能研究

<!-- [原子块 · img]  -->

**EN** Figure 6. Histogram showing the number of ratings in each category for accuracy and helpfulness, from the 3 participants in the Performance Study. For accuracy, the scale is: “1 - not accurate”, “2 - partially accurate”, and “3 - accurate”. The scale for helpfulness ranges from “1 - not at all helpful” to “5 - very helpful”. The rating data is also visualized as horizontal bar charts for this study and the Usage Study.Two histograms, one showing the accuracy ratings for each category, broken down by guidelines, and the other showing accuracy ratings. The majority of the ratings are concentrated at the two extremes (e.g. accurate and not accurate).

**ZH** 图 6. 直方图展示性能研究中 3 位参与者在准确性与有用性各等级上给出的评分数量。准确性量表为 1 - 不准确、2 - 部分准确、3 - 准确；有用性量表从 1 - 完全没用到 5 - 非常有用。本研究与使用研究的评分数据也以横向条形图的形式呈现。两张直方图，一张按准则展示各等级的准确性评分，另一张展示准确性评分。多数评分集中在两个极端（如准确与不准确）。

<!-- [原子块 · img]  -->

**EN** Figure 7. Horizontal bar charts showing the distribution of ratings from the Performance Study for each individual guideline. The ratings for accuracy are in the top row, and helpfulness is in the bottom row, and each chart has a horizontal black line depicting the average rating. We highlight several guidelines with high ratings in green, such as “Consistency and Standards” from Nielsen Norman’s 10 Usability Heuristics. We used orange to highlight an average performing guideline – “Emphasis” (from CrowdCrit), which had bimodal ratings for accuracy and helpfulness. Finally, we used red to highlight the worst performing guideline – “Aesthetic and Minimalist Design”, which had generally poor accuracy and helpfulness ratings.Three horizontal bar plots showing the distribution of accuracy and helpfulness ratings for each set of guidelines broken down by individual guideline. The accuracy ratings for recognition rather than recall, match between system and real world, and consistency and standards are highlighted in green because they are generally accurate. The consistency and standards helpfulness rating is also highlighted in green because it is generally helpful. The emphasis guideline is highlighted in yellow for both accuracy and helpfulness because it is bimodal, and aesthetic and minimalist design is highlighted in red for both ratings because it is generally negative.

**ZH** 图 7. 横向条形图展示性能研究中每条准则的评分分布。上排为准确性，下排为有用性，每张图中都有一条黑色横线标示平均评分。我们用绿色高亮了若干评分较高的准则，例如 Nielsen Norman 10 条可用性启发式准则中的一致性与标准；用橙色高亮了一条表现中等的准则——强调（来自 CrowdCrit），其在准确性与有用性上呈双峰分布；最后用红色高亮了表现最差的准则——审美与极简设计，其准确性与有用性评分普遍偏低。三张横向条形图，展示各套准则中每条准则的准确性与有用性评分分布：识别优于回忆、系统与现实世界的匹配、一致性与标准的准确性评分被标为绿色，因为它们总体准确；一致性与标准的有用性评分也标为绿色，因为它总体有用；强调准则在准确性与有用性上均标为黄色，因为呈双峰分布；审美与极简设计在两项评分上均标为红色，因为总体偏负面。

**EN** More GPT-4 generated suggestions were rated as accurate and helpful than not. Across all generated suggestions, 52 percent were rated Accurate, 19 percent Partially Accurate, and 29 percent Not Accurate; 49 percent were considered helpful or very helpful, 15 percent moderately helpful, and 36 percent slightly or not at all helpful. We show histograms of ratings given to all suggestions for each set of guidelines in Figure 6, along with averages. In line with the aggregate statistics, GPT-4 is more accurate and helpful than not for each set of guidelines. Furthermore, this difference is largest for CrowdCrit’s visual guidelines and smallest for the Semantic Grouping guidelines. Regarding the average rating for all suggestions, CrowdCrit outperformed the other guidelines for accuracy and helpfulness, with a greater outperformance in helpfulness. Semantic Grouping had the worst performance for accuracy, and Nielsen Norman performed the worst for helpfulness. Later, we show concrete examples of GPT-4 generated feedback in Figure 9 that includes accurate and helpful suggestions, as well as inaccurate and unhelpful ones.

**ZH** GPT-4 生成的建议中，被评为准确与有用的多于相反的评判。在所有生成的建议中，52% 被评为准确，19% 为部分准确，29% 为不准确；49% 被认为有用或非常有用，15% 为中等有用，36% 为略有作用或完全没用。图 6 给出各套准则下所有建议评分的直方图与均值。与总体统计一致，对每一套准则，GPT-4 准确、有用的情况都多于相反情况，且这一差距在 CrowdCrit 的视觉准则上最大，在语义分组准则上最小。就所有建议的平均评分而言，CrowdCrit 在准确性与有用性上均优于其他准则，其中有用性的优势更大；语义分组的准确性表现最差，Nielsen Norman 的有用性表现最差。后文图 9 给出了 GPT-4 生成反馈的具体示例，既包含准确有用的建议，也包含不准确、无用的建议。

**EN** We also grouped the ratings by individual guideline and visualized them in horizontal bar charts shown in Figure 7. This reveals finer-grained types of heuristics on which GPT-4 performed better than others. The accuracy was highest for the “Recognition rather than Recall”, “Match Between System and Real World”, and “Consistency and Standards” usability heuristics (highlighted in green in Figure 7), and participants generally found “Consistency and Standards” violations helpful. “Consistency and Standards” mostly caught inconsistencies in the visual layout of the UI, like misalignment and inconsistency in size. In contrast, the “Aesthetic and Minimalist Design” guideline was generally inaccurate and hence unhelpful, as shown in red in Figure 7. Finally, the “Emphasis” principle (shown in orange) from CrowdCrit was bimodal – a fairly even distribution of “accurate” and “inaccurate”, as well as “very helpful” and “unhelpful ratings”. The “Emphasis” principle mostly identified issues related to the visual hierarchy of the UI.

**ZH** 我们还按单条准则对评分分组，并以横向条形图呈现（图 7），由此看出 GPT-4 在哪些更细粒度的启发式准则上表现更好。准确性最高的是识别优于回忆、系统与现实世界的匹配与一致性与标准这三条可用性启发式准则（图 7 中以绿色高亮），参与者也普遍认为一致性与标准的违反项有用——该准则主要捕捉 UI 视觉布局上的不一致，如未对齐与尺寸不统一。相反，审美与极简设计准则普遍不准确，因而也无用（图 7 中以红色标出）。最后，CrowdCrit 的强调原则（以橙色标出）呈双峰分布：准确与不准确、非常有用与无用的评分大致各占一半；该原则主要识别与 UI 视觉层次有关的问题。

**EN** The subjective nature of heuristic evaluation was already highlighted by Nielsen (Nielsen and Molich, 1990). To characterize subjectivity in our study, we computed inter-rater reliability using Fleiss’ Kappa (Fleiss et al., 1971). Accuracy ratings had an agreement score of 0.112 and helpfulness ratings had a score of 0.100, which suggests only slight agreement. In addition to the subjective nature of this task, particular choices in the phrasing of the suggestions could have also lowered agreement scores. For example, the suggestion “The icons in this group … could be more user-friendly with the addition of text labels” calls for a subjective opinion on whether or not text labels are needed, and raters might reasonably disagree.

**ZH** Nielsen（Nielsen 和 Molich，1990）早已指出启发式评估具有主观性。为刻画本研究中的主观性，我们用 Fleiss Kappa（Fleiss 等，1971）计算了评分者间信度：准确性评分的一致性为 0.112，有用性评分为 0.100，说明评分者之间只有轻微一致。除了任务本身的主观性，建议的措辞方式也可能降低了评分者间信度。例如，这一组中的图标……若加上文本标签会更易用这条建议，等于要求评分者就是否需要文本标签给出主观判断，评分者之间产生分歧是合理的。

<!-- [原子块 · table] Performance Metrics GPT-4 Human Evaluator (Avg.) Precision 0.603 0.829 Recall 0.380 0.336 F1 0.466 0.478 -->

**EN** Table 2. Table showing the Precision, Recall, and F1 scores of GPT-4 and an individual human evaluator, computed from the ground truth dataset. The metrics for the human evaluator is computed by averaging these metrics across all participants in the study (for the 6 UIs they each evaluated).

**ZH** 表 2. 表格给出 GPT-4 与单个人类评估者在真值数据集上计算得到的精确率、召回率与 F1 分数。人类评估者的指标由研究中所有参与者（就各自评估的 6 个 UI）取平均得到。

**EN** 5.2. Quantitative Results: Comparison with Human Evaluators

**ZH** 5.2. 定量结果：与人类评估者的比较

**EN** We compiled all violations identified by the 12 experts from the manual heuristic evaluation study. In total, the experts found 72 distinct guideline violations in the 12 UIs. However, participants sometimes combined multiple violations for a single group or element (e.g., “The spacing between each icon is inconsistent, and the entire bottom menu is not centered.”). After splitting these combined violations into separate issues, the count increased to 91 distinct violations. GPT-4 found 38 helpful violations for the same set of 12 UIs (determined from the Usage study). Nine of these violations were missed by human experts, so in total, the experts and GPT-4 found 100 distinct violations. In summary, 9 violations were found by GPT-4 only, 29 were found by both GPT-4 and human experts, and 62 were found by human experts only.

**ZH** 我们汇总了手工启发式评估研究中 12 位专家发现的所有违反项。专家们在 12 个 UI 中共发现 72 处不同的准则违反项；不过，参与者有时会把同一分组或元素上的多个违反项合并表述（例如每个图标之间的间距不一致，且整个底部菜单没有居中），把这些合并的违反项拆分为独立问题后，数量增至 91 处。在同样这 12 个 UI 上，GPT-4 发现了 38 处有用违反项（由使用研究判定），其中 9 处为人类专家所遗漏，因此专家与 GPT-4 共发现 100 处不同的违反项。概括来说，9 处仅由 GPT-4 发现，29 处为 GPT-4 与人类专家共同发现，62 处仅为人类专家所发现。

**EN** We built a ground truth dataset consisting of these 100 violations and computed precision, recall, and F1 performance metrics for GPT-4, which can be found in Table 2. We also compute the average performance for an individual human evaluator, by averaging these metrics across all participants, which can also be found in Table 2. On average, a human evaluator had higher precision than GPT-4, which means the guideline violations they found were more likely to be helpful. The average human precision is less than 1, because study participants sometimes found issues irrelevant to the set of heuristics used (e.g., recorded visual grouping issues when using the Semantic Grouping guidelines). GPT-4 scored slightly higher in recall and slightly lower in the F1 score than the average human evaluator, though both these differences are much smaller than the difference in precision.

**ZH** 我们以这 100 处违反项构建真值数据集，并计算 GPT-4 的精确率、召回率与 F1 指标，结果见表 2；我们也同样计算了单个人类评估者的平均表现，即对所有参与者的指标取平均，结果亦见表 2。平均而言，人类评估者的精确率高于 GPT-4，这意味着他们发现的准则违反项更有可能是有用的；人类平均精确率小于 1，是因为参与者有时会找出与所用启发式准则集不相关的问题（例如在使用语义分组准则时记录视觉分组问题）。GPT-4 的召回率略高、F1 略低，但这两处差异都远小于精确率上的差距。

**EN** 5.3. Quantitative Results: Iterative Usage Study

**ZH** 5.3. 定量结果：迭代使用研究

<!-- [原子块 · img]  -->

**EN** Figure 8. Horizontal bar charts showing the distribution of ratings for each round of evaluation in the Usage study. The ratings are for suggestions from all participants and sets of guidelines. The average rating and standard deviation is marked for each round, and there is a general downward trend in performance as the number of rounds increases.Horizontal bar charts showing accuracy and helpfulness ratings across rounds. There is a general decrease in performance as the rounds increase.

**ZH** 图 8. 横向条形图展示使用研究中每一轮评估的评分分布。评分涵盖所有参与者与所有准则集的建议，每轮均标出平均评分与标准差；随着轮次增加，表现总体呈下降趋势。横向条形图展示各轮次的准确性与有用性评分，随着轮次增加，表现总体下降。

**EN** We collected accuracy and helpfulness scores in the Usage study. Statistics on ratings for suggestions on initial UIs, before participants made any changes, closely match that of the Performance Study: 52 percent were rated Accurate, 28 percent Partially Accurate, and 20 percent Not Accurate; 47 percent were considered helpful or very helpful, 19 percent moderately helpful, and 34 percent slightly or not at all helpful (see Figure 8).

**ZH** 我们在使用研究中收集了准确性与有用性评分。就参与者做任何修改之前的初始 UI 而言，其建议评分统计与性能研究高度吻合：52% 被评为准确，28% 为部分准确，20% 为不准确；47% 被认为有用或非常有用，19% 为中等有用，34% 为略有作用或完全没用（见图 8）。

**EN** However, score distributions were lower for later rounds, after participants edited the UIs. Namely, 39 percent were rated Accurate, 26 percent Partially Accurate, and 35 percent Not Accurate; 33 percent were considered helpful or very helpful, 16 percent moderately helpful, and 51 percent slightly or not at all helpful. This discrepancy suggests that participants’ opinions of suggestions changed during the iterative re-design process. To investigate this, we examined the ratings given per round of iteration in the Usage Study. Since GPT-4’s suggestions vary in accuracy and helpfulness, we used a horizontal bar chart to show the distributions of all ratings given to suggestions in each round. Figure 8 shows a general trend of decreasing performance per round for both accuracy and helpfulness. This trend also generally holds for both metrics when broken down by guidelines and participants (available in the Supplementary Materials).

**ZH** 然而，在参与者修改 UI 之后的后续轮次，评分分布更低：39% 被评为准确，26% 为部分准确，35% 为不准确；33% 被认为有用或非常有用，16% 为中等有用，51% 为略有作用或完全没用。这一差异说明，参与者对建议的看法在迭代再设计过程中发生了变化。为探究这一点，我们考察了使用研究中每一轮迭代给出的评分。由于 GPT-4 的建议在准确性与有用性上参差不齐，我们用横向条形图展示每一轮中所有建议评分的分布。图 8 显示，准确性与有用性均随轮次呈整体下降趋势；按准则与按参与者拆分后，这一趋势同样成立（详见补充材料）。

**EN** The average inter-rater reliability score, based on the first round of suggestions, is 0.155 for accuracy and 0.085 for helpfulness, which again indicates subjectivity in the experts’ opinions towards the suggestions.

**ZH** 基于第一轮建议计算的评分者间信度平均为：准确性 0.155，有用性 0.085，同样说明专家对建议的看法存在差异。

**EN** 5.4. Qualitative Results: GPT-4 Strengths and Weakness

**ZH** 5.4. 定性结果：GPT-4 的优势与不足

<!-- [原子块 · img]  -->

**EN** Figure 9. Examples of GPT-4 suggestions that all participants found very helpful or unhelpful, along with their corresponding UIs above (with the relevant group marked). The suggestions for UIs A and B received ratings of 5 for helpfulness and were rated as accurate by all three participants (from the Usage study). The “Contact:” field for UI B is slightly misaligned from the other fields, which GPT-4 caught. UIs C and D were rated 1 for helpfulness by all three participants. For UI C, the LLM stated that the line thickness was uneven under the “ADS” and “FAVORITES” tab, which is technically accurate (and some participants rated it as accurate) but unhelpful as the uneven line thickness is meant to indicate the selected tab.Four examples of GPT-4 suggestions with corresponding annotated UI screenshots. The two on the left are highly rated with and discuss further subgrouping a menu with unrelated items and aligning a slightly misaligned form. The two on the right are low rated. One says that the line thickness is uneven for a set of tabs what show which page is displayed, and the other says that a grid of images are overlapping when they are not visually.

**ZH** 图 9. 示例：所有参与者都认为非常有用或毫无用处的 GPT-4 建议，上方为对应的 UI（并标出相关分组）。UI A 与 UI B 的建议在有用性上均获 5 分，且三位参与者（来自使用研究）都评为准确；UI B 的 Contact: 字段与其他字段存在轻微错位，被 GPT-4 捕捉到。UI C 与 UI D 则被三位参与者一致评为有用性 1 分：对 UI C，LLM 指出 ADS 与 FAVORITES 标签下方线条粗细不均，这在技术上准确（部分参与者也评为准确），但并无用处，因为线条粗细不均正是用来标示当前选中标签的。四组 GPT-4 建议示例及对应的标注截图：左侧两条评价很高，分别讨论把含无关项的菜单进一步细分为子组，以及对齐一处轻微错位的表单；右侧两条评价很低，一条说一组用于指示当前页面的标签线条粗细不均，另一条说一组图片网格相互重叠，而视觉上其实并未重叠。

**EN** We analyzed GPT-4’s suggestions, corresponding expert ratings, explanations, and interview responses from the Usage study. Through grounded theory coding (Glaser and Strauss, 1967) of the qualitative data and subsequent thematic analysis (Braun and Clarke, 2006), we identified the following emerging themes on GPT-4’s strengths and weaknesses. Figure 9 contains examples of high and low-rated LLM suggestions to illustrate some of these themes.

**ZH** 我们分析了使用研究中 GPT-4 的建议、相应的专家评分与说明，以及访谈回答。通过对定性数据做扎根理论编码（Glaser 和 Strauss，1967）并继以主题分析（Braun 和 Clarke，2006），我们归纳出以下关于 GPT-4 优势与不足的主题。图 9 给出了高评分与低评分的 LLM 建议示例，用以说明其中若干主题。

**EN** 5.4.1. Strength 1: Identification of Subtle Issues (12/12 Participants)

**ZH** 5.4.1. 优势 1：识别细微问题（12/12 位参与者）

**EN** All participants found GPT-4’s ability to identify subtle, easy-to-miss issues helpful. This includes problems like misalignment, uneven spacing, poor color contrast, redundant elements, and uncommon icons without text labels. UI B in Figure 9 contains an example of a misalignment caught by GPT-4 that all three participants found very helpful. Seven participants mentioned this theme as a strength during the interview. For instance, P5 stated that the tool is “useful for pointing out things that are not obvious to the naked eye, like minor visual details”, and P4 said that they “liked the UI at first, but then the LLM found small issues with labels, etc.”

**ZH** 所有参与者都认为，GPT-4 能发现细微、易被忽略的问题，这一点很有用。这类问题包括未对齐、间距不均、色彩对比度差、元素冗余，以及缺少文本标签的非常见图标等。图 9 中的 UI B 即为一例：GPT-4 发现了一处错位，三位参与者都认为非常有用。有 7 位参与者在访谈中提到这一优势，例如 P5 表示该工具能指出肉眼不易察觉的地方，比如细微的视觉细节；P4 说自己一开始觉得这个 UI 挺好，但 LLM 找出了标签等方面的小问题。

**EN** 5.4.2. Strength 2: Fixing Text-related Issues in the UI (12/12 Participants)

**ZH** 5.4.2. 优势 2：修复 UI 中的文案问题（12/12 位参与者）

**EN** GPT-4 was also effective in identifying text-related issues, like incorrect grammar, unclear text labels, and text that is not user-friendly (e.g., uses too much jargon). In addition, GPT-4 would usually include the correct text to use in its feedback. For instance, one UI had a grammatically incorrect header: “what kind of pet your Looking?” and GPT-4 suggested revising it to “What kind of pet are you looking for?” P1 rated this suggestion as very helpful and explained that “it gave me the right content to copy and use in the design.”

**ZH** GPT-4 在识别文案相关问题上同样有效，例如语法错误、文本标签表意不清、文案不够友好（如使用过多行话）；此外，它通常会在反馈中直接给出应使用的正确文案。例如，某个 UI 的标题存在语法错误：what kind of pet your Looking?，GPT-4 建议改为 What kind of pet are you looking for?。P1 认为该建议非常有用，并解释说它给了我可以直接复制使用的正确内容。

**EN** 5.4.3. Strength 3: Reasoning with UI Semantics (8/12 Participants)

**ZH** 5.4.3. 优势 3：对 UI 语义进行推理（8/12 位参与者）

**EN** GPT-4 was skilled at reasoning with UI semantics. This includes identifying large groups of items that could be subgrouped into smaller, more semantically-related groups. This is illustrated in UI A of Figure 9, where the LLM suggested subgrouping the menu items into more related categories. P2 commented “Yes, I think it would be helpful to separate out the sections into categories, as some relate to the purpose of the application (traveling), and other parts are related to basic maintenance of the account (e.g., settings)”. Other semantics-related issues that GPT-4 identified include finding groups or subgroups with elements are not clearly related, groups or visualizations where the purpose is unclear and requires a text label to explain them, and confusing UIs that require documentation.

**ZH** GPT-4 擅长对 UI 语义进行推理，包括识别出可进一步细分为语义更相关的子组的大型条目集合。图 9 的 UI A 就展示了这一点：LLM 建议把菜单项细分为关联更紧密的类别。P2 评论道，是的，我认为把这些分区拆成不同类别会有帮助，因为有些与应用的核心用途（旅行）相关，另一些则与账号的基本维护（例如设置）相关。GPT-4 发现的其他语义相关问题包括：分组或子组中的元素关联不明确；分组或可视化的用途不清、需要文本标签加以说明；以及界面令人困惑、需要配备文档说明等。

**EN** 5.4.4. Other Strengths

**ZH** 5.4.4. 其他优势

**EN** For two participants, GPT-4 made clever, high-level suggestions. For instance, GPT-4 recommended that a product quantity value be changed to an editable field, so users will not have to rely on the ‘+’ or ‘-’ buttons to adjust the quantity, and cited Nielsen’s “Flexibility and Efficiency of Use” heuristic. In addition, GPT-4 suggested that a list of reviews for a cafe should display aggregate statistics, like the total number of reviews or an average star rating. P1 encountered both these suggestions and stated that GPT-4 “found two good ones that I would think about – with reviews and product quantity input field”. P12 encountered a violation where the selected tab in the navbar was called “strategies”, but the displayed page was about stock performance, which was unrelated to strategies. They commented that GPT-4 was “spot on”.

**ZH** 对两位参与者而言，GPT-4 还给出了巧妙的高层建议。例如，它建议把商品数量值改为可编辑字段，这样用户就不必依赖加号或减号按钮来调整数量，并援引了 Nielsen 的使用的灵活性与效率启发式准则；此外，它还建议某咖啡馆的评论列表应显示汇总统计，如评论总数或平均星级。P1 遇到了这两条建议，并表示 GPT-4 找到了两条我会认真考虑的不错建议——关于评论和商品数量输入字段。P12 遇到一处违反项：导航栏中名为 strategies 的标签被选中，但所显示页面讲的是股票表现，与策略无关；他评价 GPT-4 的判断完全正确。

**EN** 5.4.5. Weakness 1: Overapplication of Guidelines (12/12 Participants)

**ZH** 5.4.5. 不足 1：过度套用准则（12/12 位参与者）

**EN** GPT-4 sometimes over-applied guidelines too literally, without considering the context provided by the rest of the UI, popular design conventions, nor conflicts with other guidelines. UI C in Figure 9 shows an example where the LLM correctly identified that the line thickness is inconsistent for the two tabs; however, this was a conscious design decision to show the selected tab in the broader context of the UI. P7 commented “the line under favorites indicates that we are on the favorites tab/screen; making it consistent would eliminate this distinction”. Regarding popular design conventions, GPT-4 often recommended labels for common icons, like the ‘X’ and shopping bag icons, but “universal icons do not need to be labeled”, as stated by P1.

**ZH** GPT-4 有时会过于字面地套用准则，既不考虑 UI 其余部分提供的上下文，也不顾及流行的设计惯例，还忽视与其他准则的冲突。图 9 的 UI C 展示了一个例子：LLM 正确识别出两个标签下方线条粗细不一致，但在整个 UI 的更大语境中，这恰恰是标示当前选中标签的有意为之。P7 评论说，favorites 下方的线条表示我们正处于 favorites 标签页或屏幕；若改成一致，就会消除这一区分。在流行设计惯例方面，GPT-4 常为常见图标（如 X 和购物袋图标）推荐文本标签，而正如 P1 所说，通用图标不需要加标签。

**EN** 5.4.6. Weakness 2: Repetition of Feedback (6/12 Participants)

**ZH** 5.4.6. 不足 2：重复反馈（6/12 位参与者）

**EN** GPT-4 sometimes repeated the same feedback for every element of the same type. For instance, in the second UI of Figure 9, the LLM suggested increasing the spacing between the “Name:” label and the name “Suraj shakaya” and then repeated this same suggestion for both “Contact:” and “Location:”. P4 commented that the LLM “repeats the same type of issue, and it is especially annoying when it is incorrect.”

**ZH** GPT-4 有时会对同一类型的每个元素重复给出同样反馈。例如，在图 9 的第二个 UI 中，LLM 建议增大 Name: 标签与姓名 Suraj shakaya 之间的间距，随后又对 Contact: 与 Location: 重复了同一建议。P4 评论说，LLM 反复提同一类问题，而它还不正确时尤其让人恼火。

**EN** 5.4.7. Weakness 3: Limitations of the JSON Representation (8/12 Participants)

**ZH** 5.4.7. 不足 3：JSON 表示的局限（8/12 位参与者）

**EN** A limitation of using JSON to represent the UI is that GPT-4 cannot capture violations that would require processing the rendered image of a UI. For example, GPT-4 will call out issues with elements overlapping when there is no visual overlap. UI D in Figure 9 is an example where the LLM flagged an overlap issue because the bounding boxes overlap, but the photos do not overlap visually. Another error is that the LLM does not recognize center alignment for items of different sizes. This is explained by P9: “The elements are of different sizes and the bounding boxes of elements are not aligned, but the inner contents of the boxes are visually aligned.”

**ZH** 用 JSON 表示 UI 的一个局限在于，GPT-4 无法捕捉那些需要处理 UI 渲染图像的违反项。例如，GPT-4 会在并不存在视觉重叠的情况下指出元素重叠问题；图 9 的 UI D 即为一例，LLM 因边界框相交而报告了重叠问题，但照片在视觉上并未重叠。另一类错误是 LLM 无法识别不同尺寸元素的居中对齐，P9 对此的解释是：这些元素尺寸不同，边界框并未对齐，但框内的内容在视觉上是对齐的。

**EN** 5.4.8. Weakness 4: Vague Suggestions (5/12 Participants)

**ZH** 5.4.8. 不足 4：建议笼统（5/12 位参与者）

**EN** Five participants stated that GPT-4’s suggestions were too vague, specifically regarding how to fixing the violation. P1 stated that the LLM would “be more useful if it were more specific and gave more examples on how to fix things”, and P11 said they would “like to see more actionable suggestions, like change this color to a specific value”. The reason for this vagueness is due to our system implementation. We first attain a set of guideline violations from GPT-4 and then send the violation explanations only (without the UI) for the LLM to rephrase into constructive feedback. Since GPT-4 does not have information on the UI, it cannot suggest specific fixes in the UI to address each violation. We tried passing in the UI for the rephrasing call, but it led to high latency (several minutes), so we decided to not include the UI JSON from a usability perspective.

**ZH** 有五位参与者表示 GPT-4 的建议过于笼统，尤其是关于如何修复违反项的部分。P1 说，LLM 如果能更具体一些、多给出如何修复的示例，会更有用；P11 说希望看到更可执行的建议，比如把这个颜色改成某个具体值。造成笼统的原因在于我们的系统实现：我们先从 GPT-4 得到一组准则违反项，然后只把这些违反项说明（不含 UI）发给 LLM，请其改写为建设性反馈；由于 GPT-4 没有 UI 信息，它无法针对每个违反项在 UI 中给出具体修改方案。我们曾尝试在改写调用中一并传入 UI，但这导致延迟过高（数分钟），从可用性角度考虑，最终决定不纳入 UI JSON。

**EN** 5.4.9. Other Weaknesses

**ZH** 5.4.9. 其他不足

**EN** We noticed an interesting behavior of GPT-4 in response to designer feedback. When the LLM is notified that the guideline violation is incorrect for a group or element (from the designer hiding the suggestion), it would sometimes select a different guideline to explain the same issue. For instance, GPT-4 would often cite a violation of “Recognition over Recall” for unlabeled icons, but if the designer dismisses this suggestion, GPT-4 would repeat the same suggestion in the next round and cite “Match Between System and Real World” instead. This behavior was encountered by 5 participants.

**ZH** 我们注意到 GPT-4 在回应设计师反馈时有一种有趣行为：当 LLM 被告知某分组或元素的准则违反项不正确（源于设计师隐藏了该建议）时，它有时会换用另一条准则来解释同一个问题。例如，GPT-4 常对未加标签的图标援引识别优于回忆的违反项，但若设计师关闭该建议，它会在下一轮重复同一建议，并改引系统与现实世界的匹配。有 5 位参与者遇到了这一行为。

**EN** 5.5. Qualitative Results: Comparison with Human Evaluators

**ZH** 5.5. 定性结果：与人类评估者的比较

<!-- [原子块 · img]  -->

**EN** Figure 10. The screenshot on the left compares a high-level “global” violation found by a human expert with a similar, but more specific, violation found by the LLM. The right screenshot contains two violations found by human experts that require advanced visual understanding of the UI.Two screenshots with violations marked. The left screenshot has a box draw around the large image taking up most of the UI and the corresponding violation for this box describes how this large image hides important details of the UI. Another box is draw around the "Swipe up for details" text label and the corresponding violation talks about how the label should be edited to indicate what kind of details will be revealed. The right screenshot has a box drawn around a profile picture and a profile icon and it maps to a violation regarding redundant links to the profile, and the right screenshot also has a box draw around a tooltip in the graph, which talks about how the tooltip does not match the content nor axes of the graph.

**ZH** 图 10. 左侧截图把某位人类专家发现的一处高层全局性违反项，与 LLM 发现的一处相近但更具体的违反项做了比较；右侧截图包含两处人类专家发现、需要更高级视觉理解的违反项。两张带有违反项标注的截图：左侧截图中，占 UI 大部分区域的一张大图被框出，对应违反项说明这张大图遮住了 UI 中的重要细节；另一处框出 Swipe up for details 文本标签，对应违反项说明该标签应改写以表明将展开何种细节。右侧截图中，一张头像与一个个人资料图标被框出，对应一处关于指向个人资料的冗余链接的违反项；此外还框出了图表中的一个工具提示，说明该提示与图表内容、坐标轴都不相符。

**EN** We used grounded theory coding and thematic analysis to characterize key qualities for 1) issues violations found by GPT-4 only, 2) found by both GPT-4 and human experts, and 3) found by human experts only. Finally, we summarize participants’ feedback for the LLM from the concluding interview.

**ZH** 我们用扎根理论编码与主题分析，刻画以下三类违反项的关键特征：1）仅 GPT-4 发现的；2）GPT-4 与人类专家共同发现的；3）仅人类专家发现的。最后，我们总结了参与者在收尾访谈中对 LLM 的评价。

**EN** 5.5.1. Violations Found by GPT-4 only (9 percent)

**ZH** 5.5.1. 仅由 GPT-4 发现的违反项（9%）

**EN** A small fraction of the violations were found by the LLM only. Eight of the nine issues were quite subtle, covering poor text contrast, text labels that require clarification, and misalignment. The ninth suggestion missed by all participants recommended adding a new feature to filter through the cafe’s reviews, and participant H8 commented “this type of suggestion did not cross my mind during the manual evaluation”.

**ZH** 只有一小部分违反项为 LLM 单独发现。这 9 处问题中有 8 处相当细微，涉及文本对比度差、需要澄清的文本标签，以及未对齐等。第九处为所有参与者都遗漏的建议：为咖啡馆评论增加筛选功能，参与者 H8 评论说，这类建议在人工评估时我并没有想到。

**EN** 5.5.2. Violations Found by both Humans and GPT-4 (29 percent)

**ZH** 5.5.2. 人类与 GPT-4 共同发现的违反项（29%）

**EN** Twenty-nine issues were identified by both humans and the LLM. The majority of these violations (15 violations) involved text labels – labels that require clarification, and missing labels to explain an icon, element, or group. The second most common issue (6 issues) involved positioning and alignment, with four being quite obvious (e.g., the misaligned elements were scattered like in Figure 9C). Other issues found by both include problems with the UI text (e.g., the text had too much jargon) and the hierarchical subgrouping violation shown in Figure 9A.

**ZH** 有 29 处问题为人类与 LLM 共同发现。其中多数（15 处）涉及文本标签——需要澄清的标签，以及缺少解释图标、元素或分组的标签；第二常见的问题（6 处）涉及位置与对齐，其中 4 处相当明显（例如元素像图 9C 那样散乱未对齐）。两者共同发现的其他问题还包括 UI 文案问题（例如文案行话过多），以及图 9A 所示的层次化细分违反项。

**EN** 5.5.3. Violations Found by Humans only (62 percent)

**ZH** 5.5.3. 仅由人类发现的违反项（62%）

**EN** The majority of the violations were found by human experts only (62 violations). Common characteristics of violations in this category include “global” (i.e., high-level) issues of the UI, advanced visual issues, and violations consisting of multiple distinct issues. Participants found 11 high-level issues that require understanding of the UI’s purpose and context. Figure 10 (Violation H1) illustrates a global violation identified by a human expert, where a large image hides important content, and compares it to a similar, but more specific, violation found by GPT-4 (L1). While GPT-4 is able to find these “global” violations, as discussed in Sections 5.5.1 and 5.4.4, human experts found considerably more. Eight violations, found only by human experts, required advanced visual understanding of the UI. The right screenshot in Figure 10 illustrates two such violations. The tooltip (Figure 10 H3) displayed a monetary amount that not only exceeded the axes of the graph but also mismatched the graph’s content about sleep duration. Violation H2 highlighted redundant links to the user profile with via both a profile image and a profile icon. Finally, a few participants stated that parts of the UI shown in Figure 11 (Round 1) had clashing visual design and an overly complicated background.

**ZH** 多数违反项为人类专家单独发现（62 处）。这一类违反项的共同特征包括：UI 的全局性（即高层）问题、高级视觉问题，以及由多个不同问题组合而成的违反项。参与者发现了 11 处需要理解 UI 用途与上下文的高层问题。图 10（违反项 H1）展示了一位人类专家发现的全局性违反项——一张大图遮住了重要内容，并将其与 GPT-4 发现的一处相近但更具体的违反项（L1）做了比较。如 5.5.1 与 5.4.4 节所述，GPT-4 虽能发现这类全局性违反项，但人类专家发现的数量要多得多。有 8 处违反项仅为人类专家所发现，需要对 UI 有更高级的视觉理解。图 10 右侧截图展示了其中两处：工具提示（图 10 H3）显示的金额不仅超出了图表坐标轴范围，也与图表关于睡眠时长的内容不符；违反项 H2 指出了通过头像与个人资料图标两种途径指向用户资料的冗余链接。最后，部分参与者表示，图 11（第 1 轮）所示 UI 的部分区域存在视觉设计冲突，且背景过于复杂。

**EN** Ten of the violations recorded by the participants involved combinations of several distinct issues for a single group or element. For instance, a violation for the UI in Figure 11 (Round 1) stated that “The title has incorrect spelling and grammar, is not aligned on the page/has awkward margins, has inconsistent text styles for the same sentence, and includes clashing visual elements”. Finally, participants found 22 issues that were similar to the types of issues caught by GPT-4, such as misalignment, unclear labels, and redundancy. This implies that GPT-4 is less comprehensive than a group of 6 human experts, as each UI was evaluated by 6 study participants.

**ZH** 参与者记录的违反项中，有 10 处针对同一分组或元素组合了多个不同问题。例如，针对图 11（第 1 轮）UI 的一处违反项写道：标题拼写和语法有误，页面对齐不佳、边距别扭，同一句中文本样式不一致，且包含相互冲突的视觉元素。此外，参与者还发现了 22 处与 GPT-4 所捕捉类型相似的问题，如未对齐、标签不清与冗余等。由于每个 UI 由 6 位研究参与者评估，这意味着 GPT-4 的全面性不及一组 6 位人类专家。

**EN** 5.5.4. Interview Findings

**ZH** 5.5.4. 访谈发现

**EN** Participants were generally impressed by the convenience of this plugin, which could find helpful guideline violations at a much faster speed than manual evaluation. H6 said that it “can cut about 50 percent of your work, and is at the level of a good junior designer”, and H3 said they “wish it was already out for use”. Compared to the violations they found manually, several participants said GPT-4 was more thorough and detailed (H3, H4, H5, H6, H10). H1 “appreciated how the LLM could find subtle violations that were missed”, and P5 said they were “overwhelmed by the number of issues in some UIs” and appreciated how the LLM can catch violations that were “tedious to find”. H6 said GPT-4 “goes into a much lower level of resolution than is commercially feasible to do, since it takes a long time”. H1, H3, and H9 valued how GPT-4 could sometimes better articulate the violation. H9 stated that they were “pleasantly surprised at how it picked the right way to describe the problem”, regarding an issue they struggled with describing. Finally, H1, H2, H4, H7, and H8 all appreciated how GPT-4 found violations that were missed during their manual evaluation. H7 said “it was useful, as it captured more cases than I found”.

**ZH** 参与者普遍对该插件的便捷性印象深刻——它能以远快于人工评估的速度找出有用的准则违反项。H6 说它能省掉大约 50% 的工作量，水平相当于一位不错的初级设计师；H3 说希望它已经可以投入使用了。与手工发现的违反项相比，多位参与者认为 GPT-4 更全面、更细致（H3、H4、H5、H6、H10）。H1 很欣赏 LLM 能发现被漏掉的细微违反项；P5 说自己被某些 UI 中问题数量之多弄得有些招架不住，因而很认可 LLM 能捕捉那些找起来很烦人的违反项。H6 说 GPT-4 细到了商业上根本做不到的程度，因为那要花很长时间。H1、H3 与 H9 看重 GPT-4 有时能把违反项表述得更清楚；H9 说，对于一处自己难以描述的问题，LLM 选对了描述方式，让他颇感惊喜。最后，H1、H2、H4、H7 与 H8 都认可 GPT-4 发现了他们手工评估时遗漏的违反项，H7 说它很有用，捕捉到的情况比我发现的更多。

**EN** Participants brought up weaknesses of GPT-4’s feedback, which mostly aligned with the findings in Sections 5.4 and 5.5.3. These limitations include missing the majority of the “global” violations (H1, H5, H9), limited visual understanding of the UI (H2, H8, H11), and poor knowledge of popular design conventions (H2, H7, H8, H10, H11). Finally, like the participants in the Usage study, those in this study also did not consider the LLM’s mistakes to be a significant issue. H10 said “if the feedback is correct, then is it very helpful, and if not, it is not a big deal as you can just dismiss it”, and H6 said “the 60 percent success rate is not a problem, as it saves a lot of time in the end”.

**ZH** 参与者也提出了 GPT-4 反馈的不足，大多与 5.4 和 5.5.3 节的结果一致。这些局限包括：遗漏多数全局性违反项（H1、H5、H9）、对 UI 的视觉理解有限（H2、H8、H11），以及对流行设计惯例了解不足（H2、H7、H8、H10、H11）。与使用研究的参与者一样，本研究参与者也不认为 LLM 的失误是什么严重问题：H10 说如果反馈是对的，那就非常有用，如果不对，也不算大事，直接关掉就行；H6 说 60% 的成功率不是问题，因为它最终节省了大量时间。

**EN** 5.6. Qualitative Results: Integration into Existing Design Practices

**ZH** 5.6. 定性结果：融入现有设计实践

**EN** We analyzed the interview responses from the Usage study with grounded theory coding and thematic analysis to determine this tool’s fit into existing design practice. The emerging themes centered around how and when designers would integrate it in their practice, potential broader use cases, and possible dangers of an imperfect tool.

**ZH** 我们用扎根理论编码与主题分析，分析了使用研究的访谈回答，以判断该工具与现有设计实践的契合度。涌现的主题集中于：设计师会如何、在何时将其纳入实践，潜在的更广泛使用场景，以及一个不完美工具可能带来的风险。

**EN** 5.6.1. How and When Designers Would Integrate this Tool in Practice

**ZH** 5.6.1. 设计师会如何、在何时把该工具纳入实践

**EN** Nine out of 12 participants said they would use this tool. The three who would not cited inaccurate and vague suggestions as reasons. Of the nine participants who would use this tool, three said they would use it during the initial stages of the design. This includes tasks like determining the hierarchy of components in low-fidelity prototypes (P5, P7) and “exploring early stage concepts” (P7). The other six participants would use this tool in the later design stages. P5 said they would also use it “after the first draft of high fidelity for alignment issues”. P11 said “after finalizing their design, I would run a check before sending it to engineering”, and they would also run this tool “after making large design changes to see if any design considerations were missed”. Finally, P6 said they would run this tool “after prototyping and before usability testing; it is valuable to test the LLM’s recommendations during the user test”.

**ZH** 12 位参与者中有 9 位表示会使用这一工具；另外 3 位不会使用的理由是建议不准确且笼统。在会使用工具的 9 位中，有 3 位表示会在设计初期使用，包括确定低保真原型中组件的层次（P5、P7），以及探索早期概念（P7）。其余 6 位会在设计后期使用：P5 说也会在高保真初稿完成后用它检查对齐问题；P11 说在定稿之后、交付工程之前，我会跑一遍检查，并且会在做完大幅设计改动后运行，看是否遗漏了某些设计考量；P6 说会在原型制作之后、可用性测试之前运行，在用户测试中检验 LLM 的建议很有价值。

**EN** Regarding iterative or one-shot usage, seven participants preferred using this tool for a single check, and the other five preferred iterative usage. The participants who preferred one-shot usage stated that the LLM feedback was less accurate and helpful in later rounds (P4, P5, P7), found that the “first round of edits was sufficient” (P8), or preferred to use the LLM’s suggestions as “tips to start off the thinking process, but not rely on it” (P7).

**ZH** 在迭代使用还是一次性使用方面，7 位参与者倾向于只做一次检查，另外 5 位倾向于迭代使用。偏好一次性使用的参与者表示，LLM 反馈在后续轮次中准确性与有用性更低（P4、P5、P7），认为第一轮修改已经足够（P8），或更愿意把 LLM 的建议当作开启思路的提示，而不依赖它（P7）。

**EN** Participants also had positive feedback on the interaction design of the plugin. Six participants stated that they liked being able to click on the group or element’s name in the suggestion to select it in the mockup (Figure 2, A). Four participants stated they like the references to guidelines, as it “adds credibility” (P3), and they could reference the guideline’s source material for more context (P9). P3 liked the constructive framing of the violations, saying that “the type of language is encouraging, which is nice to see”. Finally, P4 liked the “built-in guideline options and the flexibility to specify my own guidelines”.

**ZH** 参与者对插件的交互设计也给出了正面评价。6 位表示喜欢点击建议中的分组或元素名称就能在原型稿中选中它（图 2 A）。4 位表示喜欢对准则的引用，因为这增加了可信度（P3），他们还能查阅准则的原始材料以获取更多上下文（P9）。P3 喜欢违反项的建设性表述，说这种语言让人受到鼓励，看着很舒服。最后，P4 喜欢内置的准则选项，以及指定自己准则的灵活性。

**EN** 5.6.2. Potential Broader Use Cases

**ZH** 5.6.2. 潜在的更广泛使用场景

**EN** The participants brainstormed a long list of use cases for this tool. Some use cases are based on real observations from the Usage study, and others are hypothetical (from speculation). For observed use cases, the most common was using this tool to save busywork, which was mentioned by 5 participants. P10 said this tool would “save time on mundane tasks”, for things like “spellcheck”, and 3 participants said it can catch small details like line spacing, size, and “small things you might miss” (P11). Other observed use cases include evaluating other people’s designs during teamwork (P3) and secondary research (P8), and using it “as a first round of usability testing” (P8). Common hypothetical use cases include using it for accessibility checks (4 participants) and training novices (10 participants). P5 stated that this tool can “help younger designers learn and reinforce these guidelines”, and P11 and P12 said the mistakes made by the LLM can train novices to carefully consider design suggestions and be more skeptical. Other speculative use cases include getting a second opinion on your UIs (for designers working solo) (P6), checking for compliance with brand standards (P10) and company rules (P12), and “large-scale evaluation, where you designed a lot of screens and want a quick evaluation” (P9).

**ZH** 参与者头脑风暴出了一长串该工具的使用场景，其中一些来自使用研究中的真实观察，另一些则是假设性的（源于推测）。就观察到的场景而言，最常被提及的是用它省下琐碎工作，有 5 位参与者提到；P10 说该工具能节省在琐碎任务上的时间，比如拼写检查，另有 3 位说它能捕捉行距、尺寸一类的小细节，以及你可能忽略的小地方（P11）。其他观察到的场景包括在团队协作中评估他人的设计（P3）、二手调研（P8），以及把它当作第一轮可用性测试（P8）。常见的假设性场景包括用于无障碍检查（4 位）与培训新手（10 位）：P5 表示该工具能帮助年轻设计师学习并巩固这些准则，P11 与 P12 则认为 LLM 犯的错误可以训练新手仔细审视设计建议、保持怀疑。其他推测性场景包括为独立工作的设计师提供对 UI 的第二意见（P6）、检查是否符合品牌规范（P10）与公司规定（P12），以及大规模评估——你设计了很多屏幕，想快速过一遍（P9）。

**EN** 5.6.3. Potential Dangers of this Tool

**ZH** 5.6.3. 该工具的潜在风险

**EN** Although the tool sometimes reported inaccurate violations, most participants (8 out of 12) considered the tool not dangerous because there is a human in the loop to catch errors. However, some potential dangers stated by participants include “thinking there is something wrong with the design when there might not be” (P2) and users who trust the LLM 100 percent (P1, P4, P6, P9). For instance, novices may fully follow the LLM’s advice (P1, P2, P3, P6, P11), and P3 suggested that they could use this tool with expert supervision. However, 4 participants felt that novices should be able to detect the LLM’s mistakes. P3 stated that “the wrong suggestions are outlandish enough that novices can tell that it does not make sense”. There were also some negative feedback regarding the plugin design. Three participants (P2, P8, P11) found the LLM suggestions too wordy, and P7 did not like how the tool “can only evaluate one screen at a time, as opposed to the whole flow.”

**ZH** 尽管该工具有时会报告不准确的违反项，多数参与者（12 位中的 8 位）认为它并不危险，因为有人工审核来发现错误。不过，参与者提到的潜在风险包括以为设计有问题，而其实未必（P2），以及百分百信任 LLM 的用户（P1、P4、P6、P9）；例如，新手可能完全照搬 LLM 的建议（P1、P2、P3、P6、P11），P3 建议新手应在专家监督下使用该工具。但也有 4 位参与者认为新手应当能察觉 LLM 的错误，P3 说错误的建议离谱到新手一眼就能看出说不通。关于插件设计也有一些负面反馈：3 位参与者（P2、P8、P11）认为 LLM 建议过于啰嗦；P7 不喜欢该工具一次只能评估一个屏幕，而不是整个流程。

**EN** 6. Discussion

**ZH** 6. 讨论

<!-- [原子块 · img]  -->

**EN** Figure 11. Plots of the average accuracy and helpfulness rating per round from P2, who used the CrowdCrit guidelines to evaluate the UI shown above. Paraphrased GPT-4 suggestions from each round and their average accuracy and helpfulness ratings are also provided. The suggestions P2 used to edit the UI are highlighted in gray, and the corresponding changes are annotated in the revised UI. Participants made at most 2 rounds of edits, so the “Feedback for UI After Second Revision” was never used for edits. Note that participants were instructed to approach this task as if they were using this plugin for their own design work and to put as much effort into the edits as they would like. This sometimes led them to fix issues in the design beyond what the LLM explicitly stated. The UI’s visual design improves per round, while the average accuracy and helpful ratings decrease.Three screenshots of the same UI after each round of revision and corresponding LLM suggestions per round. Line plots of the accuracy and performance ratings per round are also included. The UI improves visually across the three rounds while the performance drops. Also, the suggestions that were used by the participant for the revision are also highlighted.

**ZH** 图 11. 折线图展示 P2 使用 CrowdCrit 准则评估上图 UI 时，每一轮的平均准确性与有用性评分；图中同时给出各轮 GPT-4 建议的转述及其平均准确性与有用性评分，P2 用于修改 UI 的建议以灰色高亮，相应的改动也在修改后的 UI 中做了标注。参与者最多做两轮修改，因此第二次修改后的 UI 反馈从未被用于修改。需注意，参与者被要求按自己使用该插件做真实设计的方式来完成任务，并在修改上投入自己认为合适的精力，这有时会让他们修复 LLM 未明确指出的问题。UI 的视觉设计逐轮改善，而平均准确性与有用性评分逐轮下降。同一 UI 在每轮修改后的三张截图，以及各轮对应的 LLM 建议；还包含每轮准确性与表现评分的折线图。三轮之中 UI 在视觉上不断改善，而表现持续下滑；参与者用于修改的建议也被高亮标出。

**EN** We explored the potential of using LLMs for automated heuristic evaluation. In particular, we assessed the feasibility of the best performing LLM (GPT-4) and how a tool built on this can fit into existing design practice. We discuss interesting insights from our findings, and implications for its feasibility and integration into design practice.

**ZH** 我们探索了用 LLM 执行自动化启发式评估的潜力，重点评估表现最好的 LLM（GPT-4）的可行性，以及基于它构建的工具如何融入现有设计实践。下面讨论研究发现中若干有趣的洞察，以及这些洞察对可行性与融入设计实践的意义。

**EN** 6.1. Feasibility of GPT-4 for Heuristic Evaluation

**ZH** 6.1. GPT-4 用于启发式评估的可行性

**EN** We assessed GPT-4’s performance quantitatively and qualitatively. From our qualitative analysis, we identified a concrete set of strengths and weaknesses. Most of these weaknesses could potentially be addressed, which we will discuss in Future Work (Section 7). Quantitatively, the GPT-4 was judged to be more accurate and helpful than not during the Performance study and the first round of the Usage study. The authors selected the UIs for both studies because they identified issues according to the chosen guidelines. This suggests that the LLM can identify some weaknesses in poor UI designs. The decrease in performance after each iteration during the Usage study could be explained by the fact that the participants are design experts, so their edits likely improved the UI overall, leaving fewer guideline violations for GPT-4 to detect. As a result, the task becomes harder for the LLM, causing it to detect erroneous violations. Figure 11 illustrates this; GPT-4’s suggestions become less accurate and helpful as P2 iterates on the UI using the CrowdCrit guidelines, while the UI’s visual design becomes noticeably better going into each round of evaluation. This general decrease in performance as the UI improves implies that this tool is perhaps not yet suitable for iterative usage by expert designers. In addition to being affected by the quality of the UI mockup, the performance also varies depending on the guidelines used.

**ZH** 我们从定量与定性两方面评估了 GPT-4 的表现，并通过定性分析归纳出一组具体的优势与不足，其中多数不足有望被克服，我们将在第 7 节未来工作中讨论。定量上，在性能研究与使用研究的第一轮中，GPT-4 被认为准确、有用的情况多于相反情况。两项研究的 UI 都由作者依据所选准则挑出存在问题的界面，这说明 LLM 能发现劣质 UI 设计中的某些不足。而使用研究中每轮迭代后表现下降，可能是因为参与者本身是设计专家，其修改总体上提升了 UI，留给 GPT-4 检测的准则违反项随之减少；任务因此变得更难，导致 LLM 检测出错误的违反项。图 11 正说明了这一点：P2 用 CrowdCrit 准则迭代 UI 时，GPT-4 建议的准确性与有用性不断下降，而 UI 的视觉设计在进入每一轮评估时都明显变好。这种随 UI 改善而出现的表现下滑意味着，该工具目前或许还不适合专家设计师迭代使用。除了受 UI 原型稿质量影响，表现还随所用准则而异。

**EN** 6.1.1. CrowdCrit

**ZH** 6.1.1. CrowdCrit

**EN** GPT-4 performed the best with CrowdCrit’s visual design heuristics in both accuracy and helpfulness. This is likely due to the prevalence of specific visual design heuristics that rely on mathematical checks for alignment, spacing, and consistency in size – all checks that are straightforward to compute with layout information found in the UI JSON (except for center alignment and overlap). CrowdCrit also covers UI text accuracy (i.e., grammar and spelling), where LLMs excel in identifying and fixing issues. Regarding helpfulness, many visual design errors are subtle (like slight misalignment), and participants found it very useful when the LLM found them.

**ZH** GPT-4 在 CrowdCrit 的视觉设计启发式准则上表现最好，准确性与有用性俱佳。这可能得益于其中大量具体的视觉设计启发式准则依赖对对齐、间距与尺寸一致性的数学检查——这些检查用 UI JSON 中的布局信息即可直接完成（居中对齐与重叠除外）。CrowdCrit 还涵盖 UI 文案的正确性（即语法与拼写），而这正是 LLM 擅长发现与修复的方面。在有用性方面，许多视觉设计错误相当细微（如轻微错位），参与者认为 LLM 能发现它们非常有用。

**EN** 6.1.2. Nielsen Norman 10 Usability Heuristics

**ZH** 6.1.2. Nielsen Norman 10 条可用性启发式准则

**EN** We expected the Nielsen Norman 10 Usability Heuristics to have the best performance, as they are widespread on the web and would have appeared in GPT-4’s training data. However, its worse performance, especially for helpfulness, could be because many of its heuristics apply to interactions or flows (like “User Control and Freedom”, “Help and Documentation”, and “Error Prevention”) that are out of scope for single-screen, static mock-ups. In addition, the “Aesthetic and Minimalist Design” heuristic covers visual design but had poor performance. This is probably because this heuristic is quite vague, focusing on only presenting necessary information to the user; this is difficult to assess, especially without the context provided by other screens in the flow. On the other hand, GPT-4 performed well on “Consistency and Standards”, which mostly checked for consistency in the visual layout, like size and alignment, which are straightforward numerical checks.

**ZH** 我们原本预计 Nielsen Norman 的 10 条可用性启发式准则表现最好，因为它们在网上传播极广，很可能已出现在 GPT-4 的训练数据中。然而其表现更差、有用性尤甚，原因或在于其中多条启发式准则面向交互或流程（如用户的控制与自由、帮助与文档、错误预防），超出单屏静态原型稿的范围。此外，审美与极简设计虽涉及视觉设计，表现却不佳，可能是因为这条启发式准则本身相当笼统，只强调向用户呈现必要信息，难以评估，尤其在缺少流程中其他屏幕所提供的上下文时。另一方面，GPT-4 在一致性与标准上表现良好，该准则主要检查视觉布局的一致性，如尺寸与对齐，都是直接的数值检查。

**EN** 6.1.3. Semantic Grouping

**ZH** 6.1.3. 语义分组

**EN** The lack of training data on Semantic Grouping guidelines, which were recently developed, could explain their lower accuracy. In addition, the quality of group/element names in the UI JSON impacts the assessment of the UI’s semantic organization. Since designers must manually add these names, they may not always be accurate. While we can automate the naming of groups, they are determined from the labels of their members. Many leaf elements, like icons and images, are also missing labels, which may affect the accuracy of the automatically generated labels. While GPT-4 generally performed well for evaluating the relatedness of elements, as mentioned by study participants, the times it did not perform well for semantic grouping were probably for poorly annotated UIs.

**ZH** 语义分组准则提出较晚，训练数据不足，这或可解释其准确性偏低。此外，UI JSON 中分组与元素名称的质量会影响对 UI 语义组织的评估：这些名称需由设计师手动添加，因此未必总是准确。虽然我们能自动生成分组名称，但其依据的是成员标签，而图标、图像等许多叶元素本身也缺少标签，这会影响自动生成标签的准确性。参与者提到 GPT-4 在评估元素相关性上总体表现不错，因此它在语义分组上表现不佳的情形，很可能出现在标注质量差的 UI 上。

**EN** 6.2. General Insights into LLMs and their Future Development

**ZH** 6.2. 关于 LLM 及其未来发展的一般性洞察

**EN** The LLM comparison analysis revealed that this automated heuristic evaluation task of UIs in JSON form is hard enough to require the largest state-of-the-art model with the strongest reasoning skills (GPT-4). The other state-of-the-art models were smaller and struggled with this task; they either missed most of the violations or indiscriminately applied the guidelines and had difficulty following the detailed instructions. While these LLMs found some helpful violations, their performance falls short for building a system. The prompt exploration study showed that breaking tasks into smaller, simpler ones and providing the maximum amount of guidance yielded the strongest performance for GPT-4, and this insight probably applies to other LLMs.

**ZH** LLM 比较分析表明，对以 JSON 形式呈现的 UI 做自动化启发式评估，其难度足以要求使用规模最大、推理能力最强的最先进模型（GPT-4）。其他最先进模型规模更小，难以胜任：它们要么漏掉大部分违反项，要么不加区分地套用准则，且难以遵循细致的指令。虽然这些 LLM 也发现了一些有用的违反项，但其表现尚不足以支撑起一个系统。提示探索研究则显示，把任务拆分为更小、更简单的子任务，并提供尽可能充分的指引，能让 GPT-4 发挥最强性能，这一洞察很可能也适用于其他 LLM。

**EN** Furthermore, LLMs are rapidly advancing. Recent developments include multimodal models that can accept images as input (e.g., GPT-4V), and models with much larger context windows (e.g., GPT-4-Turbo). Multimodal LLMs could accept UI screenshots, which may give the model a better visual understanding of the UI; larger context windows would enable more complex UIs, an extensive list of few shot examples, or chain-of-thought prompting. These developments could address some of the limitations we discussed and may improve LLM performance for this task; however, this would have to be evaluated in future work, as our experiments with earlier multimodal models were not successful.

**ZH** 此外，LLM 正在快速演进。近期进展包括可接受图像输入的多模态模型（如 GPT-4V），以及上下文窗口大得多的模型（如 GPT-4-Turbo）。多模态 LLM 可以接收 UI 截图，可能让模型对 UI 有更好的视觉理解；更大的上下文窗口则能支持更复杂的 UI、更丰富的少样本示例，或思维链提示。这些进展有望解决我们讨论过的部分局限，并可能提升 LLM 在该任务上的表现，但这有待未来工作评估，因为我们早先对多模态模型的实验并不成功。

**EN** 6.3. Comparison with Human Evaluators

**ZH** 6.3. 与人类评估者的比较

**EN** While GPT-4 and a human evaluator had comparable F1 scores, human evaluators had higher precision, a better understanding of the UI’s context, found more “global” (i.e., high-level) violations, and had superior visual understanding of the UI. GPT-4, on the other hand, was more thorough, detailed, and specific, catching a greater number of helpful issues than an individual human evaluator. Furthermore, GPT-4 was better at catching detailed errors that were tedious for humans to find and was also better at finding subtle violations. These findings imply that the strengths of humans and GPT-4 are complementary for heuristic evaluation.

**ZH** 虽然 GPT-4 与人类评估者的 F1 分数相当，但人类评估者的精确率更高，对 UI 上下文的理解更好，能发现更多全局性（即高层）违反项，且对 UI 的视觉理解更胜一筹。而 GPT-4 更全面、更细致、更具体，捕捉到的有用问题多于单个人类评估者；它还更擅长捕捉人类查找起来十分繁琐的细节错误，也更善于发现细微的违反项。这些发现说明，在启发式评估上，人类与 GPT-4 的优势是互补的。

**EN** 6.4. Fit into Design Practice

**ZH** 6.4. 与设计实践的契合度

**EN** We found that even with its current performance, participants were generally positive towards this tool and would use it in their practice. They stated that the errors made by GPT-4 were easy to detect and not dangerous, as there is a human in the loop to ensure that updates to the UI mockup are based only on valid feedback. Given the LLM’s strengths, designers have brought up various use cases for this plugin, such as finding subtle visual design errors in their high-fidelity mockups and planning the grouping structure of their low-fidelity designs. The core capabilities of this plugin allow designers to evaluate their Figma mockup against any set of guidelines, and participants suggested extending it to check for accessibility and compliance with company/brand standards. The experts’ acceptance of the LLM’s imperfect suggestions, combined with numerous suggested use cases, implies that an automated LLM-driven heuristic evaluation tool may soon find a place in design practice, supporting human designers with various aspects of the design process.

**ZH** 我们发现，即便以当前的表现水平，参与者总体上对该工具持正面态度，并愿意在实践中用它。他们表示，GPT-4 的错误很容易被发现，并不危险，因为有人工审核来确保对 UI 原型稿的修改只基于有效反馈。鉴于 LLM 的这些优势，设计师提出了该插件的多种使用场景，例如在高保真原型稿中发现细微的视觉设计错误，以及为低保真设计规划分组结构。插件的核心能力是让设计师用任意一套准则评估自己的 Figma 原型稿，参与者还建议将其扩展到无障碍检查与对公司、品牌规范的合规性检查。专家对 LLM 不完美建议的接受度，加上他们提出的众多使用场景，意味着一个自动化、LLM 驱动的启发式评估工具可能很快会在设计实践中占据一席之地，在设计流程的多个方面为人类设计师提供支持。

**EN** 7. Limitations and Future Work

**ZH** 7. 局限与未来工作

**EN** There are several limitations with this system and studies. For the system, the LLM’s accuracy on semantic heuristics depends on the quality of the names designers manually add to elements. Furthermore, due to context window limitations (8.1k tokens for GPT-4), the plugin could only evaluate one static mobile UI screen at a time. This prevents the plugin from evaluating interactivity, design consistency across screens, and task flows. Larger UIs, like websites and desktop apps, are more complex and would also exceed this context window size. While there are models with larger context windows (Claude 2 and GPT-3.5-16k), they did not produce sufficiently helpful output in our exploration. Other LLMs with even smaller context windows, such as Llama 2 and GPT-3.5-turbo, are not suitable for realistic UIs. Regarding the studies, they captured the quality of the LLM’s feedback, and participants used the plugin to revise mostly high-fidelity mockups. These studies did not capture the impact of this plugin’s usage on a more realistic design scenario, where designers start with an idea and design a UI mockup based on it.

**ZH** 本系统与这些研究存在若干局限。就系统而言，LLM 在语义启发式准则上的准确性取决于设计师手动为元素添加的名称质量；此外，受上下文窗口限制（GPT-4 为 8.1k token），插件一次只能评估一个静态的移动端 UI 屏幕，因而无法评估交互性、跨屏幕的设计一致性以及任务流程。网页与桌面应用等更大的 UI 更为复杂，同样会超出这一上下文窗口。虽然有上下文窗口更大的模型（Claude 2 与 GPT-3.5-16k），但它们在我们的探索中并未产出足够有用的输出；而 Llama 2、GPT-3.5-turbo 等上下文窗口更小的模型，则不足以应对真实的 UI。就研究而言，这些研究刻画了 LLM 反馈的质量，且参与者主要用插件修改高保真原型稿，并未捕捉该插件在更真实设计情境中的影响——那种情境下设计师从一个想法出发，据此设计出 UI 原型稿。

**EN** These limitations suggest exciting opportunities for future work. To start with, we describe potential ways to address the LLM limitations discussed in Section 5.4. We have stored the data on LLM suggestions, ratings, rating explanations, and UI JSONs from both studies (available in the Supplementary Materials). Future work can use this data to fine-tune an LLM to improve performance. Furthermore, to address repetitive suggestions, P5 suggested grouping them into one long suggestion, which could be accomplished by some engineering effort to identify elements of the same type in the UI JSON. Future work should also evaluate the performance of emerging multimodal models (e.g., GPT-4V) with a prompt consisting of both the UI screenshot and JSON representation to see if it improves the LLM’s visual understanding of the UI. Models with larger context windows (e.g., GPT-4-turbo) should be evaluated to see if they can enable evaluation of task flows across multiple screens. Such models could also enable use of few-shot or chain-of-thought examples. Once these limitations of the plugin have been addressed, a study could be conducted where participants use this plugin to assist in creating a design from a given prompt. This study would more realistically simulate the tool’s usage in practice.

**ZH** 这些局限指向了令人期待的未来工作。我们首先给出克服 5.4 节所讨论的 LLM 局限的可能途径：我们已保存两项研究中 LLM 建议、评分、评分说明与 UI JSON 的数据（见补充材料），未来工作可用这些数据微调 LLM 以提升表现。针对重复建议问题，P5 建议把它们合并为一条长建议，这可通过一定的工程工作识别 UI JSON 中同类型的元素来实现。未来工作还应评估新兴多模态模型（如 GPT-4V）在提示同时包含 UI 截图与 JSON 表示时的表现，看能否改善 LLM 对 UI 的视觉理解；也应评估上下文窗口更大的模型（如 GPT-4-turbo）能否支持跨多屏幕的任务流程评估，这类模型还可能使少样本或思维链示例成为可能。待插件的这些局限被克服后，可开展一项研究，让参与者使用该插件辅助从给定提示出发创建设计，从而更真实地模拟该工具在实践中的使用方式。

**EN** 8. Conclusion

**ZH** 8. 结论

**EN** We designed and built a Figma plugin that uses LLMs to automate the heuristic evaluation of Figma mockups with arbitrary text-based design guidelines. After determining the optimal LLM for this task (GPT-4), we investigated its capability to automate heuristic evaluation through a study where three design experts rated the accuracy and helpfulness of GPT-4 generated design suggestions for 51 UIs, and also compared its feedback with those provided by human experts. Finally, we explored how this tool can fit into existing design practice via a study where 12 design experts used this tool to iteratively refine UIs, assessed the generated feedback, and discussed their experiences working with the plugin. We found that GPT-4 generally performs well on poor UI designs, but its utility decreases through iterations of revising the design. Participants generally do not find the LLM’s mistakes to be an issue, as they are easily detected by human designers. Most participants would already use this tool as part of their design practice.

**ZH** 我们设计并实现了一款 Figma 插件，用 LLM 按任意基于文本的设计准则，对 Figma 原型稿自动执行启发式评估。在确定该任务上最优的 LLM（GPT-4）之后，我们通过一项研究考察了其自动化启发式评估的能力——三位设计专家对 51 个 UI 的 GPT-4 生成设计建议的准确性与有用性打分，并把它的反馈与人类专家的反馈做了比较。最后，我们通过一项有 12 位设计专家参与的研究，探索该工具如何融入现有设计实践：他们使用该工具迭代改进 UI、评价生成的反馈，并讨论使用插件的体验。我们发现，GPT-4 在劣质 UI 设计上总体表现良好，但随着设计反复修改，其效用递减；参与者普遍不认为 LLM 的失误是个问题，因为人类设计师很容易发现它们。多数参与者已经愿意把该工具纳入自己的设计实践。

**EN** References

**ZH** 参考文献

<!-- [原子块 · verbatim] fig (2023) 2023. Figma: The Collaborative Interface Design Tool. https://www.figma.com/ -->

<!-- [原子块 · verbatim] Alexander et al . (2017) Rukshan Alexander, David Murray, and Nik Thompson. 2017. Cross-Cultural Web Design Guidelines. In Proceedings of the 14th International Web for All Conference (Perth, Western  -->

<!-- [原子块 · verbatim] Borji and Mohammadian (2023) Ali Borji and Mehrdad Mohammadian. 2023. Battle of the Wordsmiths: Comparing ChatGPT, GPT-4, Claude, and Bard. https://doi.org/10.2139/ssrn.4476855 -->

<!-- [原子块 · verbatim] Braun and Clarke (2006) Virginia Braun and Victoria Clarke. 2006. Using thematic analysis in psychology. Qualitative Research in Psychology 3 (01 2006), 77–101. https://doi.org/10.1191/1478088706qp063 -->

<!-- [原子块 · verbatim] Brückner et al . (2022) Lukas Brückner, Luis A. Leiva, and Antti Oulasvirta. 2022. Learning GUI Completions with User-Defined Constraints. ACM Transactions on Interactive Intelligent Systems (TiiS) 12 -->

<!-- [原子块 · verbatim] Chen et al . (2017) Chun-Fu (Richard) Chen, Marco Pistoia, Conglei Shi, Paolo Girolami, Joseph W. Ligman, and Yong Wang. 2017. UI X-Ray: Interactive Mobile UI Testing Based on Computer Vision (IUI ’17 -->

<!-- [原子块 · verbatim] Cheng et al . (2023) Chin-Yi Cheng, Forrest Huang, Gang Li, and Yang Li. 2023. PLay: Parametrically Conditioned Layout Generation using Latent Diffusion. arXiv:2301.11529 [cs.LG] -->

<!-- [原子块 · verbatim] Cheng et al . (2020) Ruijia Cheng, Ziwen Zeng, Maysnow Liu, and Steve W. Dow. 2020. Critique Me. Proceedings of the ACM on Human-Computer Interaction 4 (2020), 1–24. https://api.semanticscholar.org/Co -->

<!-- [原子块 · verbatim] de Lima Salgado et al . (2016) André de Lima Salgado, Sandra Souza Rodrigues, and Renata Pontin M. Fortes. 2016. Evolving Heuristic Evaluation for Multiple Contexts and Audiences: Perspectives from a  -->

<!-- [原子块 · verbatim] Duan et al . (2023) Peitong Duan, Björn Hartmann, Karina Nguyen, Yang Li, Marti Hearst, and Meredith Ringel Morris. 2023. Towards Semantically-Aware UI Design Tools: Design, Implementation and Evaluat -->

<!-- [原子块 · verbatim] Duan et al . (2020) Peitong Duan, Casimir Wierzynski, and Lama Nachman. 2020. Optimizing User Interface Layouts via Gradient Descent. In Proceedings of the 2020 CHI Conference on Human Factors in Comp -->

<!-- [原子块 · verbatim] Elavsky et al . (2022) Frank Elavsky, Cynthia Bennett, and Dominik Moritz. 2022. How accessible is my visualization? Evaluating visualization accessibility with Chartability. In Computer Graphics Foru -->

<!-- [原子块 · verbatim] Fleiss et al . (1971) J.L. Fleiss et al . 1971. Measuring nominal scale agreement among many raters. Psychological Bulletin 76, 5 (1971), 378–382. -->

<!-- [原子块 · verbatim] Fosco et al . (2020) Camilo Fosco, Vincent Casser, Amish Kumar Bedi, Peter O’Donovan, Aaron Hertzmann, and Zoya Bylinskii. 2020. Predicting Visual Importance Across Graphic Design Types. In Proceeding -->

<!-- [原子块 · verbatim] Fraser et al . (2017) C. Ailie Fraser, Tricia J. Ngoon, Ariel S. Weingarten, Mira Dontcheva, and Scott Klemmer. 2017. CritiqueKit: A Mixed-Initiative, Real-Time Interface For Improving Feedback. In Ad -->

<!-- [原子块 · verbatim] Glaser and Strauss (1967) Barney G. Glaser and Anselm L. Strauss. 1967. The Discovery of Grounded Theory: Strategies for Qualitative Research . Aldine de Gruyter, New York, NY. -->

<!-- [原子块 · verbatim] Gorlewicz et al . (2020) Jenna L. Gorlewicz, Jennifer L. Tennison, P. Merlin Uesbeck, Margaret E. Richard, Hari P. Palani, Andreas Stefik, Derrick W. Smith, and Nicholas A. Giudice. 2020. Design Guide -->

<!-- [原子块 · verbatim] Hämäläinen et al . (2023) Perttu Hämäläinen, Mikke Tavast, and Anton Kunnari. 2023. Evaluating Large Language Models in Generating Synthetic HCI Research Data: A Case Study. In Proceedings of the 2023 -->

<!-- [原子块 · verbatim] Kim et al . (2022) Tae Soo Kim, DaEun Choi, Yoonseo Choi, and Juho Kim. 2022. Stylette: Styling the Web with Natural Language. In Proceedings of the 2022 CHI Conference on Human Factors in Computing S -->

<!-- [原子块 · verbatim] Kulkarni et al . (2015) Chinmay E. Kulkarni, Michael S. Bernstein, and Scott R. Klemmer. 2015. PeerStudio: Rapid Peer Feedback Emphasizes Revision and Improves Performance. In Proceedings of the Secon -->

<!-- [原子块 · verbatim] Kurniawan and Zaphiris (2005) Sri Kurniawan and Panayiotis Zaphiris. 2005. Research-Derived Web Design Guidelines for Older People. In Proceedings of the 7th International ACM SIGACCESS Conference on  -->

<!-- [原子块 · verbatim] Lawton et al . (2023) Tomas Lawton, Kazjon Grace, and Francisco J Ibarrola. 2023. When is a Tool a Tool? User Perceptions of System Agency in Human–AI Co-Creative Drawing. In Proceedings of the 2023 A -->

<!-- [原子块 · verbatim] Lee et al . (2020) Chunggi Lee, Sanghoon Kim, Dongyun Han, Hongjun Yang, Young-Woo Park, Bum Chul Kwon, and Sungahn Ko. 2020. GUIComp: A GUI Design Assistant with Real-Time, Multi-Faceted Feedback. In -->

<!-- [原子块 · verbatim] Lee et al . (2023) Peter Lee, Sebastien Bubeck, and Joseph Petro. 2023. Benefits, limits, and risks of GPT-4 as an AI chatbot for medicine. New England Journal of Medicine 388, 13 (2023), 1233–1239. -->

<!-- [原子块 · verbatim] Ling and Salvendy (2009) Chen Ling and Gavriel Salvendy. 2009. Effect of evaluators’ cognitive style on heuristic evaluation: Field dependent and field independent evaluators. International Journal of -->

<!-- [原子块 · verbatim] Liu et al . (2023b) Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. 2023b. Visual Instruction Tuning. arXiv:2304.08485 [cs.CV] -->

<!-- [原子块 · verbatim] Liu et al . (2023a) Zhe Liu, Chunyang Chen, Junjie Wang, Mengzhuo Chen, Boyu Wu, Xing Che, Dandan Wang, and Qing Wang. 2023a. Chatting with GPT-3 for Zero-Shot Human-Like Mobile Automated GUI Testing. -->

<!-- [原子块 · verbatim] Lu et al . (2022) Kevin Lu, Aditya Grover, Pieter Abbeel, and Igor Mordatch. 2022. Frozen Pretrained Transformers as Universal Computation Engines. Proceedings of the AAAI Conference on Artificial Int -->

<!-- [原子块 · verbatim] Luther et al . (2014) Kurt Luther, Amy Pavel, Wei Wu, Jari-lee Tolentino, Maneesh Agrawala, Björn Hartmann, and Steven P. Dow. 2014. CrowdCrit: Crowdsourcing and Aggregating Visual Design Critique. In -->

<!-- [原子块 · verbatim] Luther et al . (2015) Kurt Luther, Jari-Lee Tolentino, Wei Wu, Amy Pavel, Brian P. Bailey, Maneesh Agrawala, Björn Hartmann, and Steven P. Dow. 2015. Structuring, Aggregating, and Evaluating Crowdsour -->

<!-- [原子块 · verbatim] Mankoff et al . (2003) Jennifer Mankoff, Anind K. Dey, Gary Hsieh, Julie Kientz, Scott Lederer, and Morgan Ames. 2003. Heuristic Evaluation of Ambient Displays. In Proceedings of the SIGCHI Conference -->

<!-- [原子块 · verbatim] Matviienko et al . (2015) Andrii Matviienko, Maria Rauschenberger, Vanessa Cobus, Janko Timmermann, Heiko Müller, Jutta Fortmann, Andreas Löcken, Christoph Trappe, Wilko Heuten, and Susanne Boll. 2015 -->

<!-- [原子块 · verbatim] Mi et al . (2014) Na Mi, Lora Anne Cavuoto, Kenneth Benson, Tonya L. Smith-Jackson, and Maury A. Nussbaum. 2014. A heuristic checklist for an accessible smartphone interface design. Universal Access i -->

<!-- [原子块 · verbatim] Miniukovich et al . (2017) Aliaksei Miniukovich, Antonella De Angeli, Simone Sulpizio, and Paola Venuti. 2017. Design Guidelines for Web Readability. In Proceedings of the 2017 Conference on Designing -->

<!-- [原子块 · verbatim] Murad et al . (2018) Christine Murad, Cosmin Munteanu, Leigh Clark, and Benjamin R. Cowan. 2018. Design Guidelines for Hands-Free Speech Interaction. In Proceedings of the 20th International Conferenc -->

<!-- [原子块 · verbatim] Ngoon et al . (2018) Tricia J. Ngoon, C. Ailie Fraser, Ariel S. Weingarten, Mira Dontcheva, and Scott Klemmer. 2018. Interactive Guidance Techniques for Improving Creative Feedback. In Proceedings of  -->

<!-- [原子块 · verbatim] Ngoon et al . (2021) Tricia J. Ngoon, Joy O Kim, and Scott Klemmer. 2021. Shöwn: Adaptive Conceptual Guidance Aids Example Use in Creative Tasks. In Proceedings of the 2021 ACM Designing Interactive S -->

<!-- [原子块 · verbatim] Nielsen (1992) Jakob Nielsen. 1992. Finding Usability Problems through Heuristic Evaluation. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (Monterey, California, USA) ( -->

<!-- [原子块 · verbatim] Nielsen (1994) Jakob Nielsen. 1994. 10 Usability Heuristics for User Interface Design. https://www.nngroup.com/articles/ten-usability-heuristics/ -->

<!-- [原子块 · verbatim] Nielsen and Molich (1990) Jakob Nielsen and Rolf Molich. 1990. Heuristic Evaluation of User Interfaces. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (Seattle, Washingt -->

<!-- [原子块 · verbatim] O’Leary et al . (2018) Jasper O’Leary, Holger Winnemöller, Wilmot Li, Mira Dontcheva, and Morgan Dixon. 2018. Charrette: Supporting In-Person Discussions around Iterations in User Interface Design. In -->

<!-- [原子块 · verbatim] OpenAI (2023) OpenAI. 2023. GPT-4 Technical Report. arXiv:2303.08774 [cs.CL] -->

<!-- [原子块 · verbatim] Park et al . (2023) Joon Sung Park, Joseph C. O’Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, and Michael S. Bernstein. 2023. Generative Agents: Interactive Simulacra of Human Behavior. a -->

<!-- [原子块 · verbatim] Park et al . (2022) Joon Sung Park, Lindsay Popowski, Carrie Cai, Meredith Ringel Morris, Percy Liang, and Michael S. Bernstein. 2022. Social Simulacra: Creating Populated Prototypes for Social Comput -->

<!-- [原子块 · verbatim] Pavel et al . (2016) Amy Pavel, Dan B. Goldman, Björn Hartmann, and Maneesh Agrawala. 2016. VidCrit: Video-Based Asynchronous Video Review. In Proceedings of the 29th Annual Symposium on User Interfac -->

<!-- [原子块 · verbatim] Petridis et al . (2023) Savvas Petridis, Michael Terry, and Carrie Jun Cai. 2023. PromptInfuser: Bringing User Interface Mock-Ups to Life with Large Language Models. In Extended Abstracts of the 2023  -->

<!-- [原子块 · verbatim] Pinelle et al . (2008) David Pinelle, Nelson Wong, and Tadeusz Stach. 2008. Heuristic Evaluation for Games: Usability Principles for Video Game Design. In Proceedings of the SIGCHI Conference on Human -->

<!-- [原子块 · verbatim] Sadler (1989) D Royce Sadler. 1989. Formative assessment and the design of instructional systems. Instructional science 18 (1989), 119–144. -->

<!-- [原子块 · verbatim] Sanh et al . (2022) Victor Sanh, Albert Webson, Colin Raffel, Stephen Bach, Lintang Sutawika, Zaid Alyafeai, Antoine Chaffin, Arnaud Stiegler, Arun Raja, Manan Dey, M Saiful Bari, Canwen Xu, Urmish Th -->

<!-- [原子块 · verbatim] Schoop et al . (2022) Eldon Schoop, Xin Zhou, Gang Li, Zhourong Chen, Bjoern Hartmann, and Yang Li. 2022. Predicting and Explaining Mobile UI Tappability with Vision Modeling and Saliency Analysis. In -->

<!-- [原子块 · verbatim] Shinn et al . (2023) Noah Shinn, Federico Cassano, Beck Labash, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. 2023. Reflexion: Language Agents with Verbal Reinforcement Learning. arXiv:2303.113 -->

<!-- [原子块 · verbatim] Swearngin and Li (2019) Amanda Swearngin and Yang Li. 2019. Modeling Mobile Interface Tappability Using Crowdsourcing and Deep Learning. In Proceedings of the 2019 CHI Conference on Human Factors in C -->

<!-- [原子块 · verbatim] Swearngin et al . (2020) Amanda Swearngin, Chenglong Wang, Alannah Oleson, James Fogarty, and Amy J. Ko. 2020. Scout: Rapid Exploration of Interface Layout Alternatives through High-Level Design Const -->

<!-- [原子块 · verbatim] Todi et al . (2016) Kashyap Todi, Daryl Weir, and Antti Oulasvirta. 2016. Sketchplore: Sketch and Explore with a Layout Optimiser. In Proceedings of the 2016 ACM Conference on Designing Interactive Sy -->

<!-- [原子块 · verbatim] Vinson (1999) Norman G. Vinson. 1999. Design Guidelines for Landmarks to Support Navigation in Virtual Environments. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (Pitt -->

<!-- [原子块 · verbatim] Wang et al . (2023) Bryan Wang, Gang Li, and Yang Li. 2023. Enabling Conversational Interaction with Mobile UI Using Large Language Models. In Proceedings of the 2023 CHI Conference on Human Factors i -->

<!-- [原子块 · verbatim] Warner et al . (2023) Jeremy Warner, Amy Pavel, Tonya Nguyen, Maneesh Agrawala, and Bjoern Hartmann. 2023. SlideSpecs: Automatic and Interactive Presentation Feedback Collation. In Proceedings of the  -->

<!-- [原子块 · verbatim] Weber et al . (2016) Dominik Weber, Sven Mayer, Alexandra Voit, Rodrigo Ventura Fierro, and Niels Henze. 2016. Design Guidelines for Notifications on Smart TVs. In Proceedings of the ACM International -->

<!-- [原子块 · verbatim] Wei et al . (2023) Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc Le, and Denny Zhou. 2023. Chain-of-Thought Prompting Elicits Reasoning in Large Language  -->

<!-- [原子块 · verbatim] Yoon et al . (2014) Dongwook Yoon, Nicholas Chen, François Guimbretière, and Abigail Sellen. 2014. RichReview: Blending Ink, Speech, and Gesture to Support Collaborative Document Review. In Proceeding -->

<!-- [原子块 · verbatim] Zaphiris et al . (2005) Panayiotis Zaphiris, Mariya Ghiawadwala, and Shabana Mughal. 2005. Age-Centered Research-Based Web Design Guidelines. In CHI ’05 Extended Abstracts on Human Factors in Computin -->

**EN** Appendix A Appendix

**ZH** 附录 A 附录

<!-- [原子块 · object]  -->

**EN** Figure 12. Diagram illustrating the components of each prompt. The Heuristic Evaluation Prompt and the LLM Eval. Response Rephrasing Prompt form a chain, where the Rephrasing Prompt takes the LLM response from the Heuristic Evaluation prompt and instructs the LLM to rephrase it. The Heuristic Evaluation prompt starts with system instructions to guide the LLM’s behavior and contains the set of guidelines for evaluation. It is followed by a conversation history with incorrect/unhelpful violations found by the LLM (as “Assistant”) that were denoted by the designer, a “User” query telling the LLM that these violations were wrong and to self-reflect, and the LLM’s response to the self-reflection. There may be zero to multiple sets of this conversation, depending on the number of evaluation rounds. The final component is the user message, which contains the UI JSON, instructions to identify guideline violations, a short description of the content available in the UI JSON, and specific instructions to avoid common errors. The Rephrasing prompt contains system instructions that direct the LLM to constructively rephrase the violation explanation (following (Sadler, 1989)) and also guides the LLM to format the response correctly. The user query contains the LLM Eval. response with the identified violations.Diagram illustrating different components of the prompt. The heuristic evaluation prompt is broken down into system instructions, which contains task instructions and the design guidelines. The Conversation history of the designer’s feedback contains a conversation about incorrect violations found by the assistant and the user telling the assistant to self reflect, along with the assistant’s self reflection response. Finally, there is a user message containing the JSON of the UI being evaluated, instructions for evaluating it, and explicit instructions for the LLM to avoid common errors. There is an arrow showing that the LLM heuristic evaluation response goes into the LLM rephrasing prompt, which contains system instructions to rephrase the guideline violations into constructive feedback and the violations found from the LLM heuristic evaluation call.

**ZH** 图 12. 示意图展示每个提示的组成。启发式评估提示与 LLM 评估响应改写提示构成一条链，后者接收前者的 LLM 响应并指示 LLM 进行改写。启发式评估提示以系统指令开头，用于引导 LLM 的行为，并包含用于评估的准则集合；随后是包含 LLM 发现的、被设计师标记为不正确或无用违反项的对话历史（作为 Assistant），一条 User 查询告知 LLM 这些违反项有误并要求其自我反思，以及 LLM 对自我反思的响应。这样的对话可出现零组或多组，取决于评估轮数。最后一部分是用户消息，包含 UI JSON、识别准则违反项的指令、UI JSON 中可用内容的简短描述，以及避免常见错误的具体指令。改写提示包含系统指令，引导 LLM 按建设性方式改写违反项说明（遵循 Sadler，1989），并指导 LLM 正确格式化响应；用户查询则包含带有已识别违反项的 LLM 评估响应。示意图展示提示的各个组成部分：启发式评估提示被拆分为系统指令（含任务指令与设计准则）、设计师反馈的对话历史（一段关于 assistant 发现错误违反项的对话，用户让 assistant 自我反思，以及 assistant 的自我反思响应），最后是包含待评估 UI 的 JSON、评估指令以及避免常见错误的明确指令的用户消息。有箭头表示 LLM 启发式评估响应流入 LLM 改写提示，后者包含把准则违反项改写为建设性反馈的系统指令，以及 LLM 启发式评估调用所发现的违反项。
