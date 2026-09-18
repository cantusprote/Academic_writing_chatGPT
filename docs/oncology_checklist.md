# Breast Oncology / Translational Research QC Checklist (Sim Custom v0.1.0)

> Use during Phase 3 planning and Phase 6 QC in addition to the general study-design checklist.

## A. Endpoint Definition — All Oncology Studies

- [ ] Primary/key secondary/exploratory endpoint roles are explicit.
- [ ] Every time-to-event endpoint has a time origin, event set, censoring rule, and analysis population.
- [ ] Competing events are identified when relevant.
- [ ] Endpoint terminology is used consistently; EFS/IDFS/RFS/PFS/OS are not interchanged.
- [ ] Effect measure and confidence interval are reported, not p-value alone.
- [ ] Confirmatory versus exploratory analyses are clearly separated.
- [ ] Multiplicity family and control strategy are stated when confirmatory inference involves multiple hypotheses.

## B. Randomized Trials

- [ ] CONSORT 2025 reporting framework used.
- [ ] Trial registration, protocol/SAP access, funding/conflicts, and data-sharing statement reported as applicable.
- [ ] Randomization, concealment, stratification factors, and blinding/assessment procedures reported.
- [ ] Estimand and intercurrent-event strategy are aligned with the clinical question.
- [ ] Analysis populations (ITT, safety, PP/other) are explicit.
- [ ] Missing-data handling is reported.
- [ ] Prespecified subgroup analyses use interaction tests for heterogeneity.
- [ ] Harms and treatment exposure/discontinuation are reported with appropriate denominators.

## C. Retrospective / Real-World Cohorts

- [ ] Cohort entry/time zero is clinically coherent and avoids immortal-time bias.
- [ ] Inclusion/exclusion criteria are reproducible.
- [ ] Treatment/exposure assignment timing is defined.
- [ ] Confounders are selected from clinical/causal knowledge rather than univariable p-value screening alone.
- [ ] If propensity methods are used, target estimand, overlap, balance diagnostics, weights/matching, and effective sample size are reported.
- [ ] Informative censoring and treatment-selection bias are considered.
- [ ] Missingness and sensitivity analyses are reported.
- [ ] Causal language is proportional to the design and assumptions.

## D. Neoadjuvant Breast Cancer

- [ ] Disease subtype and baseline stage are defined.
- [ ] Neoadjuvant regimen, cycles, dose modifications, and surgery timing are reported.
- [ ] pCR definition is explicit; preferred general framework is ypT0/Tis ypN0 when consistent with protocol/NeoSTEEP.
- [ ] Handling of no surgery, missing pathology, inadequate nodal evaluation, or unevaluable specimens is defined.
- [ ] RCB method/classification is reported if used.
- [ ] Imaging timing and criteria for progression before surgery are prespecified/reported.
- [ ] Time-to-event outcomes distinguish randomization-based endpoints from surgery-based endpoints.
- [ ] EFS events before surgery are captured according to the prespecified definition.
- [ ] Correlative tissue collection timing is reported when relevant.

## E. Adjuvant / Early Breast Cancer

- [ ] STEEP 2.0 terminology is used when appropriate.
- [ ] IDFS/RFS/DRFS/DDFS/IBCFS/OS event sets are explicitly defined.
- [ ] Surgery/randomization/treatment-start origin is stated.
- [ ] Second primary cancers and non-breast-cancer deaths are handled according to the prespecified endpoint definition.
- [ ] Absolute survival/event-free estimates at clinically relevant time points are shown when useful.

## F. Metastatic Breast Cancer

- [ ] RECIST version and assessment method are explicit.
- [ ] Investigator versus blinded independent review is reported when relevant.
- [ ] PFS time origin, progression definition, death handling, missed assessments, and censoring are explicit.
- [ ] ORR denominator and measurable-disease requirement are explicit.
- [ ] CR/PR confirmation requirement is stated.
- [ ] DoR start/end definitions are explicit.
- [ ] CBR definition includes the stable-disease duration threshold if used.
- [ ] OS and post-progression follow-up are reported appropriately.
- [ ] Treatment exposure, discontinuation, subsequent therapy, and safety are reported when relevant to interpretation.

## G. Survival / Competing-Risk QC

- [ ] Proportional-hazards assumption is considered for Cox models.
- [ ] A single HR is not overinterpreted when hazards are clearly non-proportional.
- [ ] RMST/time-specific survival differences or time-varying effects are considered when appropriate.
- [ ] Competing-risk endpoints use CIF rather than default Kaplan-Meier probability estimates.
- [ ] Cause-specific versus Fine-Gray model is selected according to the estimand and interpreted correctly.
- [ ] Landmark analyses start follow-up at the landmark and include only eligible patients at that point.
- [ ] Time-dependent covariates use only information available by each risk interval.

## H. Biomarker Studies / REMARK

- [ ] Biomarker hypothesis is labeled prognostic, predictive, pharmacodynamic, or exploratory.
- [ ] Assay/platform, specimen source, processing, QC, and evaluability are reported.
- [ ] Cut point is prespecified/validated, or data-derived status is explicitly exploratory.
- [ ] Continuous modeling is considered before dichotomization.
- [ ] Predictive claims are supported by treatment-by-biomarker interaction analyses.
- [ ] Subgroup significance differences are not used as substitutes for interaction tests.
- [ ] Discovery and validation cohorts/steps are separated where applicable.
- [ ] High-dimensional analyses address multiple testing/FDR and batch effects.
- [ ] REMARK reporting recommendations are used for prognostic tumor-marker studies.

## I. ctDNA / MRD Studies

- [ ] Tumor-informed versus tumor-naive assay is stated.
- [ ] Specimen type, collection, processing, and assay limit/threshold are reported.
- [ ] Sampling times are explicit relative to surgery/systemic therapy.
- [ ] Baseline positivity, clearance, persistence, and emergence definitions are prespecified.
- [ ] Evaluable denominator and assay failure/indeterminate results are reported.
- [ ] Landmark or time-dependent analysis strategy matches the biomarker timing.
- [ ] Immortal-time/guarantee-time bias is assessed.
- [ ] `ctDNA-negative` is not equated with absence of disease.
- [ ] Serial measurements account for repeated observations/patient clustering when modeled longitudinally.

## J. Translational / Omics Studies

- [ ] Biological question precedes feature selection/modeling.
- [ ] Discovery and validation are separated.
- [ ] Batch effects and technical covariates are addressed.
- [ ] Multiple specimens per patient are handled appropriately.
- [ ] Multiple testing strategy (often FDR for exploratory omics) is prespecified.
- [ ] Data-driven cut points, signatures, and model selection are transparently labeled.
- [ ] Internal validation and external validation are reported when applicable.
- [ ] Claims are limited to the validation level achieved.

## K. Final Oncology Manuscript Sign-off

- [ ] Abstract endpoint definitions and numbers match the main text/tables.
- [ ] All oncology endpoint terms match `Style/terminology.md`.
- [ ] All claims with citations are grounded in verified `[EVID:id]` sources.
- [ ] All result numbers trace to `results/*.csv`.
- [ ] Table/Figure references are valid and not duplicative.
- [ ] Interaction, competing-risk, landmark/time-dependent, and multiplicity claims are described with the correct interpretation.
- [ ] Limitations explicitly address the design-specific sources of bias.
- [ ] Generalizability is limited to the actual disease setting, subtype, population, assay, and treatment context.

## Reference Standards

- CONSORT 2025: doi:10.1136/bmj-2024-081123.
- ICH E9(R1) estimands and sensitivity analysis addendum (2019).
- STEEP 2.0: doi:10.1200/JCO.20.03613.
- NeoSTEEP: doi:10.1200/JCO.23.00435.
- FDA 2020 pCR neoadjuvant breast-cancer guidance.
- RECIST 1.1: PMID 19097774.
- REMARK: PMID 16106245.
