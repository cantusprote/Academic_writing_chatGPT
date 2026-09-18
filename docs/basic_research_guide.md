# Basic / Mechanistic Research Guide (Sim Custom v0.1.0)

> Use this guide for wet-lab, mechanistic, preclinical, molecular/cell biology, tumor-microenvironment, and discovery-to-validation projects. Pair it with `docs/basic_research_analysis_guide.md` for experimental statistics/design and `docs/basic_section_templates.md` for drafting. It complements `docs/oncology_analysis_guide.md`; it does not replace the clinical workflow for cohort/RCT papers.

## 1. Core Principle — Desired Claim First

For a basic/mechanistic paper, do not start from a list of experiments. Start from the strongest claim the paper is intended to support, then ask what evidence is required to earn that claim.

**Required planning order:**

1. Biological problem
2. Central scientific question
3. Desired main claim
4. Current evidence level
5. Claim boundary — what is not yet established
6. Weakest evidence link
7. Validation route
8. Figure/story architecture
9. Results architecture
10. Manuscript wording calibrated to the achieved evidence level

> **Rule:** Experiments do not retroactively justify a stronger claim. The desired claim determines the evidence required.

For basic/mechanistic projects, `drafts/story_map.md` is the source of truth for the paper's scientific architecture. `drafts/draft_plan.md` remains the source of truth for manuscript execution, style, citations, section plan, and journal constraints. They must agree.

---

## 2. Evidence Ladder — Use Selectively, Not Mechanically

The following levels describe increasing evidentiary strength. They are **not a mandatory staircase** and not every project should reach every level.

| Level | Evidence layer | What it can usually support |
|---|---|---|
| 0 | Discovery / descriptive observation | X is present/enriched/changed under condition Y |
| 1 | Association reinforcement / orthogonal confirmation | The X–Y relationship is reproducible across another assay, dataset, modality, or context |
| 2 | Functional perturbation | Changing X alters phenotype/readout Y in model Z |
| 3 | Necessity and/or sufficiency evidence | X is required for and/or sufficient to produce Y in the tested context |
| 4 | Mechanistic specificity / rescue / epistasis | The effect depends on a specified mediator/pathway and plausible alternatives are narrowed |
| 5 | Context robustness | The evidence is reproduced across relevant models, lineages, conditions, or platforms |
| 6 | In vivo support | The mechanism/phenotype is supported in an organismal context |
| 7 | Human / translational bridge | The experimentally supported biology connects to human disease, specimens, or a defined translational use case |

### Do not confuse these levels

- replication ≠ mechanism
- expression change ≠ functional validation
- perturbation effect ≠ mechanistic specificity
- pathway enrichment ≠ causal proof
- animal support ≠ clinical efficacy
- patient association ≠ predictive biomarker utility
- human concordance ≠ implementation readiness

### Escalation rule

Move to the next evidence layer only when it addresses the current weakest link. Do not add animal, organoid, spatial, or multi-omics work merely because it appears more sophisticated.

---

## 3. Claim Classes and Evidence Requirements

### Descriptive / association claims

Typical wording: `enriched`, `associated with`, `correlated with`, `co-occurs with`.

Usually require:
- transparent sampling and measurement
- appropriate independent experimental unit
- effect size/uncertainty where applicable
- replication or orthogonal confirmation when the claim is central

### Functional contribution claims

Typical wording: `contributes to`, `promotes`, `attenuates`, `modulates`.

Usually require:
- perturbation of the proposed factor
- perturbation verification
- phenotype/readout measured independently of perturbation verification
- suitable negative/vehicle/non-targeting controls
- evidence that the result is not a simple viability, toxicity, or technical artifact when relevant

### Necessity / sufficiency claims

Use only when the design directly addresses the direction claimed.

- **Necessity:** loss/inhibition of X prevents or reduces Y under the relevant condition.
- **Sufficiency:** gain/activation of X can induce Y in an appropriate baseline context.

One does not automatically establish the other.

### Mechanism / mediation claims

Typical wording: `mediates`, `acts through`, `drives via`, `depends on`.

Usually require more than a perturbation effect. Depending on the claim, consider:
- proximal pathway/readout confirmation
- mediator perturbation
- rescue/reversal
- epistasis or dependency logic
- alternative-mechanism controls
- temporal ordering when biologically important

A rescue experiment is especially important when the paper's central claim depends on specificity or reversibility.

### Translational claims

A mechanistic observation becomes translationally relevant only when the bridge is defined. Specify the intended use case:
- disease biology relevance
- prognostic biomarker
- treatment-response prediction
- patient stratification
- therapeutic target nomination
- pharmacodynamic/monitoring marker

Do not collapse these use cases into one generic statement of "clinical relevance."

---

## 4. Experimental Unit and Replication

Before statistical analysis or figure drafting, state the hierarchy explicitly.

### Definitions

- **Independent experimental unit:** smallest unit independently assigned to the condition/intervention and capable of independent replication.
- **Biological replicate:** independent biological source or independently repeated biological experiment appropriate to the design.
- **Technical replicate:** repeated measurement of the same biological unit.
- **Subsample:** cell, field, image, well, region, read, or repeated observation nested within a higher-level unit.

### Common examples

| Setting | Usually the independent `n` | Common pseudo-replication error |
|---|---|---|
| Cell-line experiment | independent experiment / culture preparation, depending on design | treating wells, images, or cells as independent biological `n` |
| Primary cells | donor or independent biological preparation | treating multiple wells from one donor as multiple donors |
| Organoid / PDX-derived culture | donor/model source or independent preparation, depending on question | treating organoids from one source as fully independent |
| Mouse study | mouse, cage/litter in some designs, or other assigned unit | treating repeated tumor measurements as independent mice |
| Human tissue | patient/specimen source | treating multiple ROIs/cells from one patient as independent patients |
| scRNA-seq | usually biological sample/patient for population inference | using cell count as patient-level `n` |
| Imaging | biological source/experiment | using fields of view as independent biological replicates |

For nested data, record the hierarchy, for example:

`cells → fields → wells → independent experiment → biological source`

Use models/summary strategies that respect the actual hierarchy. Do not silently inflate `n` with lower-level observations.

---

## 4A. Experimental Rigor Before Claim Escalation

Before treating replication as mechanistic support, document the design features that make the experiment trustworthy:

- allocation/randomization or blocking when appropriate
- blinding for subjective acquisition/scoring/annotation when feasible
- sample-size rationale
- predefined exclusion/QC rules
- batch/operator/day/litter/cage effects
- cell/model authentication and contamination control when applicable
- reagent/construct identity and target engagement
- animal-study ARRIVE-compatible reporting when applicable
- representative-image/source-data integrity

These items do not create a stronger biological claim by themselves; they increase confidence that the evidence supporting the claim is reproducible and interpretable.

---

## 5. Validation Route Design

Build the route around the current evidence gap.

### Candidate validation layers

1. **Association reinforcement** — repeat across another dataset/model/condition.
2. **Orthogonal confirmation** — verify the same phenomenon with a different assay or measurement logic.
3. **Functional perturbation** — determine whether changing the factor changes the phenotype.
4. **Mechanistic specificity** — test mediator/dependency/rescue and relevant alternatives.
5. **Context robustness** — test whether the claim is model-, lineage-, stage-, or platform-dependent.
6. **In vivo support** — add organismal context when it answers an unresolved biological question.
7. **Human/translational extension** — connect supported biology to specimens or a defined clinical use case.

For each proposed step, state:
- question answered
- evidence layer added
- required control
- what result would support the claim
- what result would weaken/refute it
- whether the step is **necessary**, **recommended**, or **optional**

---

## 6. Model-System Strategy

Use the least complex system capable of answering the question credibly, then escalate only when needed.

Possible families include:
- immortalized cell lines
- primary cells
- co-culture / microenvironment-aware systems
- organoid-like or patient-derived models
- xenograft / syngeneic / genetically relevant animal models
- human tissue or spatial validation

### Model selection questions

- Does the model contain the biological feature required by the claim?
- Is the perturbation interpretable in this model?
- Is the phenotype measurable independently of generic toxicity or proliferation effects?
- Is a second model needed for context robustness?
- Would a more complex model answer a new question, or merely repeat the same result?

Do not assume that an animal model is automatically stronger evidence if it does not test the claim well.

---

## 7. Omics and Single-Cell Projects

Single-cell, bulk omics, spatial, proteomic, and multi-omics analyses are **optional discovery/validation layers**, not automatic proof of mechanism.

For omics-heavy papers:
- define discovery vs validation explicitly
- use the biological sample/patient as the inferential unit when appropriate
- account for batch effects and repeated samples
- control false discovery for high-dimensional hypothesis families
- avoid treating pathway enrichment as causal evidence
- connect computational discovery to an explicit validation ladder

Typical discovery-to-mechanism route:

`omics signal → independent/orthogonal confirmation → cell-state or spatial context → perturbation → functional phenotype → specificity/rescue → context or translational extension`

Use only the steps needed by the claim.

---

## 8. Figure-First Story Architecture

Before drafting Results, build `drafts/story_map.md` using `chatgpt/actions/build-story-map.md` and `docs/figure_story_guide.md`.

Each main figure should normally carry **one dominant claim**. This is a planning default, not a rigid publication rule.

For every main figure define:
- scientific question
- dominant claim
- evidence level
- anchor/decisive panel
- supporting panel roles
- falsification/alternative explanation
- claim boundary
- question generated for the next figure

A later figure should normally answer a deeper or different question rather than redraw the same claim with another assay.

---

## 9. Results Architecture

Results should read as a sequence of scientific questions and answers, not as a laboratory notebook.

Preferred pattern:

`Question → why it matters now → experiment/analysis → core observation → bounded inference → next question`

Avoid:

`We performed A → we performed B → we performed C`

when A/B/C exist only because they were done chronologically.

Organize subsections by claim or scientific question. Keep method detail in Methods/legends unless it is required to interpret the result.

---

## 10. Claim-Strength Language

Use the strongest wording directly supported by the evidence, not the strongest wording that can be hedged later.

| Evidence | Safer wording examples |
|---|---|
| descriptive | `was enriched`, `was observed`, `was associated with` |
| repeated/orthogonal | `was consistently associated`, `was reproduced using...` |
| perturbation-supported | `contributed to`, `promoted`, `attenuated` in the tested context |
| necessity/sufficiency | `was required for` / `was sufficient to` only if directly tested |
| specificity/rescue | `depended on`, `was mediated by`, `acted through` when the chain is directly supported |
| translational bridge | `supports biological/translational relevance` rather than `clinical utility` unless clinical performance is actually tested |

Always state context: model, disease setting, lineage, intervention, and boundary conditions when they materially limit generalization.

---

## 11. Minimum Basic/Mechanistic Planning Package

Before full drafting, a basic/mechanistic project should have:

- [ ] central biological question
- [ ] one-sentence desired main claim
- [ ] current evidence level
- [ ] claim boundary / non-claim
- [ ] weakest evidence link
- [ ] independent experimental unit and replicate hierarchy
- [ ] validation route with necessary/recommended/optional distinction
- [ ] `drafts/story_map.md`
- [ ] figure-level dominant claims and panel roles
- [ ] `drafts/draft_plan.md` aligned with the story map
- [ ] literature claims registered in `knowledge/evidence.md`

Use `docs/basic_research_checklist.md` during Phase 3 and Phase 6.

---

## 12. External Concept Sources

This guide was rewritten for the Sim ChatGPT workflow. Its design is conceptually informed by public claim-driven manuscript/figure planning patterns in Nature-Paper-Skills and validation-ladder concepts in AIPOCH medical-research-skills. No external workflow overrides this repository's source-of-truth, citation, verification, or user-approval rules.
