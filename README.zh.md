# ChatGPT + Shellby Academic Writing Workflow

这是一个由 ChatGPT 通过 Shellby 直接操作本地医学论文项目的工作流，主要针对乳腺肿瘤学临床、转化以及 basic/mechanistic 研究。

- Mac Studio：**sSb**
- MacBook：**mSb**
- 核心规则：**`CHATGPT.md`**
- 自定义版本：**Sim Oncology ChatGPT v0.3.0**

不需要专用 CLI 或斜杠命令。用户可以直接用自然语言要求“制定 analysis plan”“撰写 Methods”“整体验证”“运行 oncology checklist”等；ChatGPT 会读取 `chatgpt/actions/` 和相关 protocol，并通过 sSb/mSb 执行。

核心原则：没有已批准的 analysis plan 不做分析；没有已批准的 draft plan 不写正文；引用以 `knowledge/evidence.md` 为准；结果数值以 `results/*.csv` 为准；任何已通过验证的文件修改后都必须重新运行 gate。

乳腺癌项目优先使用 `docs/oncology_analysis_guide.md` 和 `docs/oncology_checklist.md`。更多细节请参阅英文 `README.md` 和 `CHATGPT.md`。


Basic/mechanistic 项目使用 `docs/basic_research_analysis_guide.md`、`docs/basic_research_checklist.md` 和 `drafts/story_map.md`；Phase 3/6 运行 mechanism audit。研究结果数值以 `results/*.csv` 为准，实验设计常量以批准的 analysis plan/Methods 为准。
