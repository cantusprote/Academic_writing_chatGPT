# ChatGPT + Shellby Academic Writing Workflow

ChatGPT が Shellby を通じてローカルの医学論文プロジェクトを直接扱うためのワークフローです。主用途は乳癌の臨床・トランスレーショナル研究に加え、basic/mechanistic研究です。

- Mac Studio: **sSb**
- MacBook: **mSb**
- Source of truth: **`CHATGPT.md`**
- Custom version: **Sim Oncology ChatGPT v0.3.0**

専用 CLI やスラッシュコマンドは不要です。自然言語で「analysis plan を作成」「Methods を作成」「全体を検証」「oncology checklist を実行」などと依頼すると、ChatGPT が `chatgpt/actions/` と各 protocol を読み、sSb/mSb 経由で実行します。

重要な原則: 承認済み analysis plan 前に分析しない、承認済み draft plan 前に本文を書かない、引用は `knowledge/evidence.md`、結果数値は `results/*.csv` を正本とする、変更後は verification gate を再実行する。

乳癌研究では `docs/oncology_analysis_guide.md` と `docs/oncology_checklist.md` を使用します。詳細は英語版 `README.md` と `CHATGPT.md` を参照してください。


Basic/mechanistic研究では `docs/basic_research_analysis_guide.md`、`docs/basic_research_checklist.md`、`drafts/story_map.md` を使用します。Phase 3/6で mechanism audit を行い、study result values は `results/*.csv`、実験条件の定数は承認済み analysis plan/Methods を正本とします。
