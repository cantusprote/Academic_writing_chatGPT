# Citation Assist Protocol

> Evidence operations for citation suggestion, claim verification, citation stance, and study-comparison tables. `knowledge/evidence.md` is always the canonical citation ledger.

## Backend and domain-routing rule

1. **Start with `knowledge/evidence.md`.** Reuse verified registered evidence when it supports the claim.
2. **For new biomedical evidence, use PubMed-first discovery** via `chatgpt/actions/search-evidence.md` / `scripts/search_pubmed.py` (and other user-authorized biomedical sources when explicitly available).
3. **`medical-kag-remote` is optional and domain-limited.** The bundled protocol describes a spine-surgery graph. Use it only when the project/topic actually matches that graph or the user explicitly requests it. Do **not** make it the primary retrieval route for breast oncology, tumor biology, or general basic/translational research.
4. Anything newly surfaced by any retrieval backend becomes citable only after PMID/DOI/source verification and registration in `knowledge/evidence.md` as `[EVID:id]`.
5. Retrieval systems never replace source-paper verification for exact claims or literature numbers.

---

## Operation 1 — Citation suggestion

Goal: given a draft claim, propose verified `[EVID:id]` candidates.

1. Scan `knowledge/evidence.md` for already-verified candidates.
2. If coverage is inadequate, search PubMed with claim-specific terms and study-type filters as appropriate.
3. If a domain-matched optional evidence backend exists (including the legacy spine medical-KAG), it may be used as an additional discovery/conflict source, not as the citation ledger.
4. Register any new candidate in `knowledge/evidence.md` after verifying identity/source.
5. Output candidate `[EVID:id]` values with a one-line support explanation (direction, population/model, intervention/exposure, outcome). Do not silently insert a citation.

Use in Phase 3 claim→citation mapping and Phase 4 drafting.

---

## Operation 2 — Claim-verification report

Goal: determine whether each cited sentence is actually supported by its registered source.

1. Extract `[EVID:id]` claims with `python3 scripts/extract_claims.py <section> --json`.
2. Retrieve the corresponding `knowledge/evidence.md` entry and, for important/ambiguous claims, the verified source paper/abstract/full text available to the workflow.
3. Run the Semantic-Citation Verifier in `docs/verifier_prompt_templates.md`.
4. Classify as `SUPPORTED`, `PARTIAL`, or `UNSUPPORTED` (or not enough information where the verifier schema calls for it).
5. Save `review/claim_verification.md` with `location | claim | [EVID:id] | verdict | action`.

A graph/KAG may supply supplementary context only when domain-matched; it is not required for verification.

---

## Operation 3 — Citation stance / balance

Goal: classify each source as supporting, contrasting, or mentioning a claim and identify one-sided literature framing.

1. Identify the claim and registered `[EVID:id]` sources.
2. Classify stance from the verified evidence/source material.
3. Search PubMed for plausible conflicting/contrasting evidence when the claim is important or contested.
4. A domain-matched conflict/graph tool may supplement this search, but absence of that tool must not block the audit.
5. Flag one-sided framing when material contrasting evidence exists but is omitted without justification.

---

## Operation 4 — Evidence comparison table

Goal: produce a structured comparison of selected papers for a Discussion or review supplement.

1. Gather structured fields from verified `knowledge/evidence.md` entries and the source papers as needed: study/design, n, model/population, intervention/exposure, outcome, result/effect, evidence level.
2. Optional domain-matched extraction tools may accelerate this step, but every manuscript-facing number must be checked against the source paper.
3. Format records with `python3 scripts/evidence_table.py <records.json> --columns study,design,n,intervention,outcome,result,loe`.
4. Save to `drafts/table_evidence.md` or the appropriate supplement.

---

## Guardrails

- Never invent a citation to satisfy a claim.
- `knowledge/evidence.md` is the canonical citation registry; retrieval backends are discovery aids.
- Literature numbers come from the cited source paper/evidence record, not from the study's `results/*.csv` unless they are results of the current study.
- The current study's own result values remain grounded in `results/*.csv`.
- If a retrieval backend is unavailable or domain-mismatched, continue with evidence.md + PubMed rather than blocking the workflow.
