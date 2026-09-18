# Sim Oncology Customization

## Baseline

- Custom project: `Academic_writing`
- Custom version: `v0.1.0`
- Upstream repository: `grotyx/Academic_writing_c_claudecode`
- Upstream baseline: **v1.6.3**, commit `e0527e2`
- Local tag preserving the baseline: `upstream-v1.6.3`

The upstream verification harness is intentionally preserved as much as possible. Domain-specific behavior is added as an oncology layer so future upstream changes can be reviewed and merged with fewer conflicts.

## What v1.6.3 Added Compared with v0.6.0

The upstream evolved from a manuscript template into a workflow-enforced production and verification harness. Major additions include:

1. `[EVID:id]` evidence-grounded citations and citation checkers.
2. `results/*.csv` as the numerical source of truth plus number checkers.
3. Phase gate ledgers with SHA-256 provenance, stale-gate detection, and live cross-checks.
4. Draft-plan and analysis-plan enforcement hooks.
5. Style anchors, terminology registry, `/style-pass`, and measurable style checking.
6. Citation-assist commands, claim verification, citation stance, and evidence tables.
7. Claude/Codex debate, multi-model critical review, and editor-style screening.
8. Revision ghost-change and reviewer-response coverage checks.
9. pytest test suite and GitHub Actions CI.

## Sim-Specific Layer

### Domain

Primary use is breast medical oncology and translational research, including early, neoadjuvant, adjuvant, metastatic, biomarker, ctDNA/MRD, and real-world studies.

### Statistical priority

For oncology work, `docs/oncology_analysis_guide.md` overrides conflicting generic heuristics in `docs/statistical_analysis_guide.md`.

The analysis sequence is:

`clinical question -> estimand -> analysis population -> endpoint definition -> time origin/event/censoring -> model -> effect estimate/CI -> multiplicity -> sensitivity analysis`

### Reporting/QC

Use `docs/oncology_checklist.md` in addition to the general study-design checklist. The oncology layer explicitly covers STEEP 2.0/NeoSTEEP concepts, RECIST-based response reporting, biomarker interaction, competing risks, and serial ctDNA timing.

### macOS

Claude Code hooks use `python3` rather than the upstream Windows-oriented `py` command.

### Git model

- `upstream`: read-only source repository.
- `origin`: reserved for the user's future personal GitHub repository.
- Never push to `upstream`.
- Sync upstream by `git fetch upstream` and review changes before merging/rebasing.

## Intentional Legacy Examples

`docs/writing_guide.md` and `docs/statistical_analysis_guide.md` retain some upstream spine/surgical examples to reduce future merge conflicts. They are examples only. Oncology terminology and methodology are governed by `Style/terminology.md` and `docs/oncology_analysis_guide.md`.
