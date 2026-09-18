# Academic Writing for ChatGPT + Shellby

Breast medical oncology / translational research manuscript workflow for **ChatGPT working directly with local files through Shellby**.

- Mac Studio local work: **sSb**
- MacBook local work: **mSb**
- Core instructions: **`CHATGPT.md`**
- Upstream baseline: `grotyx/Academic_writing_c_claudecode` v1.6.3 (`e0527e2`)
- Custom workflow version: **Sim Oncology ChatGPT v0.2.0**

## What this project does

The workflow keeps the strong upstream verification harness while making ChatGPT the orchestrator. It supports:

- evidence registry with `[EVID:id]` citation grounding
- `results/*.csv` as the numerical source of truth
- analysis-plan and draft-plan approval gates
- breast-oncology endpoint/estimand guidance
- survival, competing-risk, landmark/time-dependent analyses
- biomarker interaction and ctDNA/MRD methodology
- style/terminology control
- citation, number, abstract, cross-reference and abbreviation checkers
- SHA-256 gate provenance and stale-gate detection
- revision/response-letter verification
- optional independent/multi-model critical review

## How ChatGPT should use it

The user does **not** need slash commands. Natural-language requests map to playbooks under `chatgpt/actions/`.

Examples:

| User says | ChatGPT does |
|---|---|
| “이 주제로 프로젝트 설정해줘” | reads `CHATGPT.md` and configures the project |
| “근거 찾아서 evidence에 등록해줘” | uses `chatgpt/actions/search-evidence.md` |
| “analysis plan 만들어줘” | creates `data/analysis_plan.md`, then waits for approval |
| “이 plan대로 분석해” | runs analysis only after approval and writes `results/` |
| “draft plan 만들어줘” | creates `drafts/draft_plan.md` |
| “Methods 작성해” | drafts from the approved plan and grounded sources |
| “전체 검증해” | runs deterministic + semantic verification and gate checks |
| “oncology checklist 돌려” | applies `docs/oncology_checklist.md` |
| “critical review 해” | uses `chatgpt/actions/critical-review.md` |
| “최종 DOCX 만들어줘” | follows `docs/docx_guide.md` |

## Workflow

1. **Setup & evidence** — define topic/journal/design; register verified references in `knowledge/evidence.md`.
2. **Analysis plan** — create and approve `data/analysis_plan.md` before analysis.
3. **Analysis** — scripts in `data/py/`; canonical numerical outputs in `results/`.
4. **Draft plan** — create and approve `drafts/draft_plan.md`, including claim-to-citation mapping.
5. **Draft** — Methods → Results → Introduction → Discussion → Conclusion → Abstract → Title.
6. **Style & QC** — terminology/style checks, oncology checklist, deterministic verification, semantic verifier passes.
7. **Finalize** — reference formatting and DOCX outputs.
8. **Revision** — reviewer-response coverage and ghost-revision checks.

## ChatGPT runtime rules

There are **no automatic runtime hooks** in this fork. ChatGPT must explicitly enforce the same safeguards:

- never analyze without an approved `analysis_plan.md`
- never draft without an approved `draft_plan.md`
- use only verified `[EVID:id]` citations
- use only result numbers traceable to `results/*.csv`
- run style/terminology checks explicitly
- run verification and record gate provenance explicitly
- if an artifact changes after PASS, treat the prior PASS as stale and re-run verification

For strategic tasks (analysis plan, draft plan, revision strategy, semantic verification), use a **higher reasoning effort** when available. Routine drafting can use normal reasoning effort if the plans and evidence are already complete.

## Oncology layer

For breast oncology/translational work, `docs/oncology_analysis_guide.md` overrides conflicting generic heuristics. The central analysis sequence is:

`clinical question → estimand → analysis population → endpoint definition → time origin/event/censoring → model → effect estimate/CI → multiplicity → sensitivity analysis`

Use `docs/oncology_checklist.md` during planning and Phase 6 QC.

## Important files

- `CHATGPT.md` — source of truth for workflow and rules
- `AGENTS.MD` — compact bootstrap summary
- `chatgpt/actions/` — natural-language task playbooks
- `docs/oncology_analysis_guide.md` — oncology statistics/methodology override
- `docs/oncology_checklist.md` — oncology QC checklist
- `Style/terminology.md` — breast oncology terminology registry
- `knowledge/evidence.md` — canonical citation ledger
- `data/analysis_plan.md` — mandatory analysis plan
- `drafts/draft_plan.md` — mandatory manuscript plan
- `review/gates/` — verification ledger

## Local project pattern

Keep this repository as the master template and copy it for each manuscript project. For example:

```text
/Users/sim/Dev/Academic_writing_chatGPT     # master template
/Users/sim/Dev/TNBC_AR                      # manuscript project
/Users/sim/Dev/HER2_Heterogeneity           # manuscript project
```

ChatGPT can create and manage those project copies through sSb/mSb.

## Verification

Run the test suite with:

```bash
.venv/bin/python -m pytest -q
```

The upstream v1.6.3 verification framework and its tests are retained unless explicitly superseded by the ChatGPT/oncology layer.

## Git safety

- `upstream` is read-only and must never receive pushes.
- `origin` is reserved for the user's own repository.
- PDFs, private style anchors, and profile information remain local/ignored.

See `docs/customization.md` for the fork history and design rationale.
