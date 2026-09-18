# Basic / Mechanistic Experimental Analysis Guide (Sim Custom v0.1.0)

> Use this guide for wet-lab, preclinical, mechanistic, cell/molecular biology, tumor-microenvironment, imaging, organoid, animal, and discovery-to-validation projects. It overrides conflicting generic heuristics in `docs/statistical_analysis_guide.md` for basic/mechanistic work, just as `docs/oncology_analysis_guide.md` does for clinical oncology.

## 1. Analysis Spine

Define the analysis in this order before choosing a statistical test:

1. Biological question
2. Experimental unit
3. Factor/intervention structure
4. Biological replicate definition
5. Technical replicate / nested-observation hierarchy
6. Primary phenotype/readout
7. Planned contrast(s)
8. Batch/block/repeated-measure structure
9. Model/effect estimate and uncertainty
10. Multiplicity family, if any
11. Missingness/exclusion rules
12. Sensitivity/robustness analyses

Do **not** begin with a menu of tests.

## 2. Rules That Override the Generic Guide

- Do **not** select parametric versus nonparametric tests from a normality-test p-value alone.
- Do **not** use `kstest(data, 'norm')` as a large-sample decision rule.
- Do **not** choose Bonferroni, Holm, or FDR solely from the number of comparisons. Define the hypothesis family and scientific role first.
- Do **not** treat cells, fields, wells, ROIs, repeated measurements, or technical replicates as independent biological `n` unless they truly are independently assigned experimental units.
- Do **not** collapse a nested design into a flat t-test/ANOVA when the dependence structure materially affects inference.
- Do **not** infer mechanism from statistical significance alone; the inferential claim is determined by experimental design and controls.
- Report effect magnitude and uncertainty whenever feasible; a small p-value is not a substitute for biological effect size.

## 3. Experimental Unit First

For every central experiment, state:

| Field | Required content |
|---|---|
| Experimental unit | Smallest independently assigned/randomized unit |
| Biological replicate | Independent biological source or repeat appropriate to the design |
| Technical replicate | Repeated measurement of the same biological unit |
| Subsample | Cell/field/well/ROI/read nested within a higher-level unit |
| Assignment | How units were allocated to conditions |
| Blocking/batch | Plate, run, litter, operator, donor, sequencing batch, etc. |
| Repeated measures | Time/region/condition repeated within the same unit |

Examples: independent culture/experiment is commonly the unit for cell-line work; donor for primary-cell population inference; mouse for xenograft studies; patient/specimen for tissue imaging; and patient/sample rather than cell count for scRNA-seq population inference.

## 4. Planned Contrast Before Test Choice

Define the exact biological contrast first: control vs perturbation, gain vs loss, genotype × treatment, time × treatment, mediator rescue vs perturbation alone, or a prespecified dose/trend contrast. The model follows the contrast and dependency structure.

## 5. Common Designs

| Design | Typical analysis approach | Notes |
|---|---|---|
| Two independent biological groups | linear model / Welch t-test when appropriate; robust/nonparametric alternative if justified | technical replicates collapsed or modeled as nested |
| Paired donor/sample design | paired model / mixed model | preserve pairing |
| Repeated time points | mixed-effects / repeated-measure model | avoid separate tests at every time point as default |
| Multiple factors | factorial linear/generalized model | report interaction when scientifically relevant |
| Nested cells/fields within sample | sample-level summary or hierarchical/mixed model | do not use cell count as independent n |
| Longitudinal tumor volume | mixed-effects/growth-curve approach or prespecified summary endpoint | repeated measurements within animal |
| Count outcome | Poisson/negative-binomial or appropriate count model | assess overdispersion |
| Binary outcome | logistic/binomial model | preserve clustering if applicable |
| High-dimensional omics | platform-appropriate model + FDR/validation | separate discovery and validation |

## 6. Biological vs Technical Replicates

Technical replication reduces measurement noise; it does not automatically increase biological degrees of freedom. State the number of biological replicates, technical replicates per unit, whether technical replicates were summarized before inference, and whether hierarchical modeling retained lower-level observations.

## 7. Batch, Blocking, and Randomization

Predefine important nuisance structure such as plate/run/batch, operator, donor, litter/cage, imaging session, sequencing batch, and experimental day. Randomize/block at the design stage where feasible. If batch is confounded with condition, statistical adjustment cannot fully rescue the design; report this limitation.

## 8. Blinding

For subjective or analyst-dependent outcomes, state whether blinding was used for animal/group measurement, pathology/image scoring, manual ROI selection, data preprocessing/annotation, or endpoint adjudication. If not feasible, state why and identify safeguards when relevant.

## 9. Sample-Size Rationale

Avoid ritual post-hoc power calculations. Prefer prospective power based on a biologically meaningful effect/variance, a precision-based rationale, a clearly exploratory resource-constrained design, or a transparent field/design convention. For animal work, connect sample size to the actual experimental unit and ARRIVE-compatible reporting.

## 10. Exclusion and Missingness

Predefine failed perturbation/target engagement, assay QC failure, contaminated culture, acquisition failure, humane endpoint/non-evaluable sample, image/ROI quality exclusion, sequencing QC threshold, and any outlier rule. Do not exclude a biological replicate solely because it weakens the preferred conclusion. Report numbers and reasons.

## 11. Multiplicity

Define families by scientific purpose, not raw comparison count. One primary perturbation contrast may need no automatic adjustment; prespecified confirmatory pairwise families may require FWER control; high-dimensional exploratory families often use FDR. Not every panel in a mechanistic figure belongs to the same statistical family.

## 12. Effect Reporting

Prefer biologically interpretable estimates: absolute/relative difference, fold change with scale defined, regression coefficient, interaction estimate, odds/risk/rate ratio, or longitudinal slope/growth difference. Report uncertainty when feasible. Do not rely only on significance stars.

## 13. Image and Quantitative Assays

Define the biological unit, field/ROI selection, blinding, normalization/background subtraction, and what plotted points represent. Avoid cherry-picking representative images and preserve uncropped/raw source data when required by journal policy.

## 14. Omics / Single-Cell / Spatial

Specify discovery vs validation, biological sample unit, repeated-sample clustering, batch handling, feature filtering/normalization, multiplicity/FDR, model validation, and pseudobulk/sample-level inference when appropriate. Pathway enrichment remains hypothesis-generating unless experimentally validated.

## 15. Minimal Basic/Mechanistic Analysis-Plan Checklist

- [ ] Biological question and exact planned contrast defined
- [ ] Independent experimental unit defined
- [ ] Biological vs technical replicates separated
- [ ] Nested/repeated structure documented
- [ ] Batch/block structure documented
- [ ] Primary phenotype/readout defined
- [ ] Randomization/blinding stated when relevant
- [ ] Sample-size rationale documented
- [ ] Exclusion/QC rules predefined
- [ ] Model/effect estimate/uncertainty specified
- [ ] Multiplicity family defined when applicable
- [ ] Sensitivity/robustness analyses specified
- [ ] Claim strength remains separated from mere statistical significance
