# Experimental Evidence & Claim-Boundary Guide (Sim Custom v0.1.0)

> Purpose: map each biological claim to the exact evidence that supports it, the evidence still missing, and the wording boundary allowed in the manuscript.

## 1. Claim → Evidence → Boundary

For every central basic/mechanistic claim, create this record before drafting prose:

| Field | Required content |
|---|---|
| Claim ID | Stable identifier, e.g. `C1`, `C2` |
| Exact claim | One sentence, with context |
| Claim class | descriptive / association / functional / necessity / sufficiency / mechanism / translational |
| Current evidence | figures, experiments, analyses already available |
| Evidence level | use `docs/basic_research_guide.md` |
| Required missing evidence | only what is needed for the intended claim |
| Decisive control / falsifier | result that would materially weaken the interpretation |
| Alternative explanation | strongest plausible competing explanation |
| Boundary | what the evidence cannot establish |
| Allowed wording | verbs/nouns that match the achieved level |
| Figure mapping | figure/panel supporting the claim |

A copy of this matrix may be saved as `review/claim_evidence_matrix.md` for substantial basic/mechanistic projects.

---

## 2. Claim Classes

### A. Observation / description

Examples:
- `BMP8A expression was enriched in...`
- `A CAF state characterized by X/Y/Z was observed...`

Required discipline:
- define sample/model and measurement
- report independent unit
- do not imply function

### B. Association

Examples:
- `X was associated with invasion.`
- `X-high tumors showed...`

Required discipline:
- define direction and magnitude
- distinguish correlation from prediction and causation
- consider confounding/context

### C. Functional contribution

Examples:
- `X contributes to phenotype Y.`
- `X promotes invasion in model Z.`

Typical evidence:
- intervention/perturbation of X
- verified perturbation
- phenotype change
- appropriate controls
- artifact/toxicity checks when relevant

### D. Necessity

Claim: X is required for Y under defined conditions.

Evidence should directly test loss/inhibition and show that Y is reduced/blocked in that context. Avoid necessity language when the intervention only partially changes a correlated marker without testing the phenotype.

### E. Sufficiency

Claim: X is sufficient to induce Y in an appropriate background.

Evidence should directly test gain/activation in a context where Y is not already maximally active. Sufficiency does not automatically establish physiological necessity.

### F. Mechanistic specificity / mediation

Claim: X acts through mediator/pathway M to produce Y.

Typical evidence may include:
- proximal pathway activation/inhibition
- mediator perturbation
- rescue/reversal
- epistasis/dependency logic
- temporal ordering when relevant
- alternative-pathway controls

A single inhibitor or single knockdown can support a mechanism hypothesis but may not establish specificity if off-target or parallel explanations remain credible.

### G. Translational relevance

Claims must name the bridge:
- relevance to human disease biology
- association with patient outcome
- treatment-response prediction
- stratification
- therapeutic target nomination
- monitoring/pharmacodynamic use

Do not use `clinical utility`, `predictive biomarker`, or `therapeutic target` as generic synonyms for interesting biology.

---

## 3. Evidence-Layer Matrix

Use this matrix to identify the weakest link rather than maximizing experiment count.

| Layer | Core question | Typical evidence | What it does NOT prove by itself |
|---|---|---|---|
| Association reinforcement | Is the signal reproducible? | second dataset/model/context | causation |
| Orthogonal confirmation | Is it assay/platform-specific? | independent assay/modality | function |
| Functional perturbation | Does changing X change Y? | KO/KD/OE/drug/blockade + phenotype | pathway specificity |
| Mechanistic specificity | Through what dependency does it act? | rescue, mediator perturbation, epistasis | organismal relevance |
| Context robustness | Does it hold beyond one model? | second lineage/model/condition | universal generality |
| In vivo support | Does it operate in organismal context? | appropriate animal/model system | clinical efficacy |
| Human bridge | Is it connected to human disease? | patient tissue/cohort/spatial/clinical association | clinical utility without performance/validation testing |

---

## 4. Orthogonal Evidence

Orthogonal evidence should reduce a distinct uncertainty, not merely repeat the same measurement.

Examples:
- RNA expression + protein-level confirmation
- bulk signal + spatial localization
- imaging phenotype + biochemical readout
- computational cell-state discovery + independent tissue assay

Three assays that all measure the same downstream marker may strengthen measurement confidence but do not necessarily add three mechanistic layers.

---

## 5. Perturbation Logic

For each perturbation block, define:

1. target/factor being changed
2. perturbation method
3. perturbation verification
4. primary phenotype
5. proximal mechanism readout
6. required controls
7. interpretation if positive
8. interpretation if negative
9. interpretation if ambiguous

Keep **perturbation verification** separate from **phenotype evidence**. Demonstrating that knockdown worked is not itself evidence that the biological phenotype changed.

---

## 6. Rescue, Reversal, and Epistasis

Use rescue/reversal when the central inference depends on specificity or causal chain structure.

Examples of logic:

`X loss → Y decreases; re-expression of X → Y restored`

`X activation → M activation → Y; M blockade breaks the X→Y link`

`drug effect → phenotype reversal; target-independent toxicity control remains negative`

A rescue is strongest when it addresses the most credible alternative explanation rather than being included ceremonially.

---

## 7. Alternative Explanations and Falsification

For each major claim, write the strongest alternative explanation before manuscript drafting.

Examples:
- phenotype is secondary to general cytotoxicity
- effect is cell-line specific
- signal reflects cell composition rather than cell state
- association is driven by tumor purity or treatment exposure
- pathway readout is downstream consequence rather than mediator
- apparent temporal association results from sampling timing

Then identify one or more observations that would materially weaken/refute the preferred interpretation.

The paper is stronger when negative controls and failure boundaries are visible rather than hidden in supplement purely for narrative neatness.

---

## 8. Context Robustness

Do not generalize one model beyond the evidence.

Ask whether the central claim depends on:
- cell lineage/subtype
- hormone/HER2 context
- mutation/genotype
- microenvironment composition
- treatment exposure
- culture condition
- species/model family
- disease stage

A second model is valuable when it tests a meaningful boundary. Repeating the same experiment in a nearly identical model without a scientific reason is weaker than a deliberately contrasting context.

---

## 9. Claim Verb Calibration

### Lower-strength verbs
`observed`, `detected`, `enriched`, `associated`, `correlated`, `consistent with`

### Functional verbs
`contributed to`, `promoted`, `attenuated`, `modulated`

### Strong mechanistic verbs — use only when directly earned
`required for`, `sufficient for`, `mediated`, `depended on`, `acted through`, `drove`

### Translational terms requiring separate evidence
`predictive biomarker`, `clinical utility`, `actionable`, `therapeutic target`, `practice-changing`

Do not solve an evidence gap with adverbs (`strongly`, `robustly`, `clearly`) or by adding a caveat after an inflated claim.

---

## 10. Claim-Evidence Audit Questions

For each main claim:

- What is the exact evidence unit?
- What is the independent `n`?
- What alternative explanation remains?
- Is there a control that directly attacks that alternative?
- Is the evidence associative, functional, specific, or translational?
- Does the wording exceed the achieved level?
- Would removing one panel/experiment change the inference?
- What evidence is central vs reassuring?
- What is the boundary condition?

Use `chatgpt/actions/audit-mechanism.md` for the structured audit.
