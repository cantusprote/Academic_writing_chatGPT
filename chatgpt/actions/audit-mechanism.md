# Action — Audit Mechanism and Experimental Claim Strength

Use this playbook when the user asks whether a basic/translational story is mechanistically convincing, whether a claim is overstrong, what experiment is missing, whether figures support the proposed mechanism, or for Phase 3/6 basic-research QC.

## Purpose

Audit the **claim → evidence → boundary** chain without inventing missing support. The goal is not to make the story sound stronger; it is to determine what the current evidence actually earns and where the evidence chain is weakest.

## Read First

1. the current paper's `story_map.md` (`drafts/story_map.md` or `drafts/paper{N}_xxx/story_map.md`)
2. the matching `draft_plan.md`
3. `docs/basic_research_guide.md`
4. `docs/basic_research_analysis_guide.md`
5. `docs/experimental_evidence_guide.md`
6. `docs/figure_story_guide.md`
7. `docs/basic_research_checklist.md`
8. the matching `data/analysis_plan.md` when experimental analysis is planned or reported
9. relevant Results, figure legends, tables/analysis outputs
10. `knowledge/evidence.md` only for literature-backed contextual claims

If the paper-specific `story_map.md` is missing for a substantial basic/mechanistic paper, the audit should return **BLOCKED** for story-level sign-off and recommend building it first.

## Audit Dimensions

### 1. Claim-level fit

For each central claim classify:
- supported
- partially supported
- unsupported
- unresolved because evidence is missing/ambiguous

State the achieved evidence level and the strongest wording allowed.

### 2. Experimental design

Check:
- independent experimental unit
- biological vs technical replication
- nesting/pseudo-replication
- planned contrast/statistical model vs experimental design
- batch/block factors and repeated-measure structure
- allocation/randomization and blinding when applicable
- sample-size rationale and predefined exclusion/QC rules
- cell/model identity, authentication, mycoplasma, and reagent provenance when applicable
- perturbation verification
- phenotype readout
- controls
- alternative explanations

### 3. Mechanistic specificity

Check whether the manuscript distinguishes:
- association
- functional contribution
- necessity
- sufficiency
- specificity/rescue
- pathway mediation
- context robustness
- translational relevance

Flag causal/mechanistic verbs that exceed the design.

### 4. Figure architecture

For every main figure check:
- dominant claim
- anchor panel
- unique inferential role of each panel
- decisive control/falsifier
- main-vs-supplement placement
- whether the next figure genuinely escalates the question

### 5. Translational boundary

Check that:
- animal evidence is not called clinical efficacy
- human concordance is not called clinical utility
- prognostic vs predictive vs target-nomination claims are separated
- clinical relevance is not used as a vague umbrella term

## Output Schema

Use:

```text
MECHANISM GATE: PASS | FAIL | BLOCKED
artifact: [story map / manuscript / figures reviewed]

Central claim:
Achieved evidence level:
Highest defensible wording:

Major claim-evidence mismatches:
- [claim ID] ...

Experimental-unit / replication issues:
- ...

Experimental rigor / reproducibility issues:
- ...

Mechanistic specificity gaps:
- ...

Figure-story issues:
- ...

Strongest alternative explanation:
- ...

Weakest evidence link:
- ...

Required before stronger claim:
- necessary: ...
- recommended: ...
- optional: ...

Claim boundary that must remain in manuscript:
- ...
```

## PASS Standard

PASS means:
- every central claim is supported at the wording level used
- no unresolved pseudo-replication issue materially affects a central inference
- no major unresolved rigor/reproducibility issue undermines the central experimental inference
- required controls/specification evidence for the claimed mechanism are present or the claim is appropriately narrowed
- story map, figures, Results, and Discussion are aligned
- translational wording matches the achieved evidence

PASS does **not** mean the study has every possible validation layer.

## FAIL Standard

FAIL if any central claim is stronger than the evidence, if a major experimental-unit or reproducibility/design error undermines inference, if a required mechanistic link is missing for the wording used, or if figure/text architecture hides a conclusion-changing boundary.

## BLOCKED Standard

BLOCKED when the supplied artifacts are insufficient to determine what the evidence supports, especially when key results/figure definitions or `story_map.md` are absent.

## Persistent Output

For Phase 3 or Phase 6 QC, save the audit to `review/mechanism_audit.md` (multi-paper: the matching `review/paper{N}_xxx/mechanism_audit.md`; revision: the relevant revision subfolder) and record the result in the applicable gate ledger using check key `mechanism`.

Do not create a PASS entry unless the audit was actually performed against the frozen artifacts.
