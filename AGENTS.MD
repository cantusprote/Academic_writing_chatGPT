# Agent Instructions

Before doing any work, read `CHATGPT.md` in full. `CHATGPT.md` is the authoritative project instruction file; this `AGENTS.MD` file only summarizes non-negotiable rules for agent startup.

This repository is an academic manuscript-writing workflow. Treat `CHATGPT.md` as the source of truth for project structure, phase rules, citation integrity, statistical-analysis requirements, drafting order, QC, and finalization. If this file and `CHATGPT.md` ever conflict, follow `CHATGPT.md`.

## Core Rules

- Read and follow `CHATGPT.md` before making workflow, manuscript, analysis, or documentation changes.
- Do not fabricate references, citations, statistics, patient counts, p-values, confidence intervals, or journal requirements.
- Check `knowledge/evidence.md` before citing literature or adding new references.
- Evidence routing is domain-aware: start from `knowledge/evidence.md`; use PubMed-first discovery for breast oncology/basic/translational work. The bundled `medical-kag-remote` is a spine-specific optional legacy aid and must not be the primary route for unrelated domains. Anything newly surfaced by any backend must be verified and registered as `[EVID:id]` before citation. See `docs/citation_assist_protocol.md` and `docs/medical_kag_protocol.md`.
- Keep reference evidence under `knowledge/`; keep writing-style material under `Style/`.
- Do not commit copyrighted PDFs or private/local style-anchor summaries.
- Commit public workflow files such as `Style/style_guide.md`, `Style/terminology.md`, documentation, templates, and scripts when appropriate.
- **Runtime:** ChatGPT orchestrates repository work through Shellby: use **sSb for Mac Studio** local files and **mSb for MacBook/local files**. Do not rely on automatic runtime hooks or slash commands; use `chatgpt/actions/*.md` playbooks and run plan/style/gate/verification steps explicitly.

## Protected Local Files

Never stage or commit these unless the user explicitly overrides the rule:

- `knowledge/pdf/`
- `Style/PDF/**/*.pdf`
- `Style/PDF/**/*.PDF`
- `Style/own/*.md` except `Style/own/example_*.md`
- `Style/landmark/*.md`
- `Style/target_journal/*.md`
- `profile/`

## Manuscript Workflow

- Do not run statistical analysis before an approved `analysis_plan.md` exists. For oncology projects, read `docs/oncology_analysis_guide.md` first; for basic/mechanistic experiments, read `docs/basic_research_analysis_guide.md`; each overrides conflicting generic heuristics for its mode.
- Do not draft manuscript sections before an approved `draft_plan.md` exists (run the Step 0 Socratic brainstorming in `docs/draft_plan_template.md` before filling it). For substantial basic/mechanistic work, also require an approved paper-specific `story_map.md` and mechanism audit PASS.
- Draft sections in the order defined by `CHATGPT.md`: Methods, Results, Introduction, Discussion, Conclusion, Abstract, Title.
- Apply the breast oncology/translational terminology rules from `Style/terminology.md` during drafting and polishing.
- Use `docs/drafting_protocol.md`, `docs/section_templates.md`, and `docs/writing_guide.md` for manuscript work. Basic-Mechanistic/Hybrid projects additionally use `docs/basic_section_templates.md` and the mode-specific draft skeletons under `drafts/_templates/`.
- Run the manuscript lint script with `python3 scripts/lint_manuscript.py drafts --quiet` on macOS.
- Style transformation: when asked to make text academic/journal-style, follow `docs/style_transform_protocol.md` — load the bound `drafts/style_spec.md` + its exemplar and transform section-by-section. There are no automatic runtime hooks; ChatGPT must run the measurable check explicitly (`python3 scripts/check_style.py check <section> --spec drafts/style_spec.md`) and the Style-Conformance verifier (`docs/verifier_prompt_templates.md`).
- Pass the verification gate after each produce step (Phase 3/4/8): run independent Constraint/Citation/Data/Logic semantic verifier passes against the same frozen artifact per `docs/verification_protocol.md`; fresh-context sSb/mSb subagents or second-model reviewers are optional strengthening, not a requirement. Basic/mechanistic Phase 3/6 additionally requires the Mechanism/Experimental-Claim overlay (fix Constraint/spec violations first). Never proceed past a gate without a recorded `status: PASS` in `review/gates/`. On PASS, record a `provenance:` sha256 of the artifact (plus evidence/results where the gate depends on them; required for revision) and re-check freshness with `check_gate.py --verify-hash` — a changed file makes the PASS stale. For the deterministic dimensions (`citation` / `numbers` / `revision_claims`), also cross-check the ledger against a live re-run with `check_gate.py --cross-check LABEL=PATH` — a recorded `PASS` that disagrees with the live checker (stale or fabricated) fails the gate. On FAIL, fix and re-verify (max 2 retries) before escalating to the user.
- Tag citations as `[EVID:author_year]` during drafting; do not cite evidence entries whose Source Status is `todo` (unverified). Use only **study result values** traceable to `results/*.csv`; experimental-design constants (dose, time, replicate plan, acquisition settings, etc.) must trace to the approved analysis plan/Methods source.
- Complete and document mandatory QC rounds before final submission files are prepared.

## Git Hygiene

- Before committing, inspect `git status`, `git diff`, and recent commits.
- Stage only intentional public workflow files and manuscript templates.
- Verify no PDFs or private anchor summaries are staged before committing.
- Do not rewrite history, amend commits, force-push, or revert user changes unless explicitly requested.
- **Git safety (CHATGPT.md Rule 12):** `upstream` is read-only. Never push to it. Keep code/docs synchronized; commit intentional changes only after tests pass. Push only to a user-owned `origin` when explicitly requested.
