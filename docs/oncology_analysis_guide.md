# Breast Oncology & Translational Analysis Guide (Sim Custom v0.1.0)

> For breast oncology and translational projects, this guide takes precedence over conflicting generic heuristics in `docs/statistical_analysis_guide.md`.

## 1. Analysis Spine

Define the analysis in this order before selecting a statistical test:

1. Clinical/biological question
2. Estimand
3. Analysis population
4. Endpoint operational definition
5. Time origin / assessment time
6. Event, censoring, competing-event, and intercurrent-event rules
7. Model and effect measure
8. Multiplicity strategy
9. Missing-data handling
10. Sensitivity analyses

Do not begin with a menu of tests. The model follows the question and endpoint definition.

## 2. Rules That Override the Generic Guide

- Do **not** choose parametric versus nonparametric methods from a normality-test p-value alone. Use the data scale, design, graphical distribution, model residuals, and robustness considerations.
- Do **not** use `kstest(data, 'norm')` as a large-sample normality rule; it compares against a standard normal unless parameters are handled explicitly and is not an appropriate automatic selector here.
- Do **not** choose Bonferroni/FDR solely from the number of comparisons. Define the hypothesis family and whether inference is confirmatory or exploratory first.
- In observational treatment comparisons, baseline tables should be primarily descriptive. Use standardized differences when balance is relevant; do not treat baseline p-values as a randomization/balance test.
- A wide confidence interval indicates **imprecision**; do not automatically label a study "underpowered" after observing a nonsignificant result.
- For oncology outcomes, clinical relevance is usually expressed through absolute risks/rates, survival probabilities at clinically relevant times, response differences, duration of response, toxicity, and patient-relevant tradeoffs rather than an MCID framework alone.

## 3. Endpoint Definition Framework

Every primary and key secondary endpoint should have an operational definition table.

| Field | Required content |
|---|---|
| Name | Exact endpoint name used throughout the manuscript |
| Role | Primary / key secondary / secondary / exploratory |
| Population | ITT, safety, biomarker-evaluable, response-evaluable, etc. |
| Time origin | Randomization, treatment start, surgery, or another prespecified origin |
| Event/assessment | Exact event set or assessment rule |
| Censoring | Exact censoring rule and date |
| Competing events | Defined when clinically relevant |
| Effect measure | Difference, RR/OR, HR, RMST difference, rate, etc. |
| Assessment method | Pathology, RECIST, central review, assay, etc. |

Endpoint names are not interchangeable. `EFS`, `IDFS`, `RFS`, `PFS`, and `OS` must be defined operationally for the specific study.

## 4. Early / Adjuvant Breast Cancer

Use STEEP 2.0 concepts when applicable and state the exact included events.

- **IDFS**: define the event set explicitly; do not assume readers know which second primaries or deaths are included.
- **RFS/DRFS/DDFS/BCFS/IBCFS**: use only if the study definition is explicit and consistent with the protocol/source standard.
- **OS**: time origin and all-cause death definition must be explicit.
- Report absolute event-free/survival estimates at clinically interpretable time points in addition to relative effects when useful.

## 5. Neoadjuvant Breast Cancer

### Pathologic response

- Preferred pCR definition for a general neoadjuvant breast-cancer framework: **no residual invasive cancer in breast and sampled regional nodes, ypT0/Tis ypN0**.
- If the protocol uses another pCR definition, state it exactly and do not relabel it.
- Define how patients without surgery, missing pathology, inadequate nodal assessment, or non-evaluable specimens are handled.
- Consider **Residual Cancer Burden (RCB)** as continuous and/or class (0/I/II/III) when available; specify the calculation method.

### Time-to-event outcomes

- NeoSTEEP emphasizes outcomes beginning at randomization for neoadjuvant trials so presurgical progression/death can be captured.
- If postoperative endpoints are also used, distinguish their time origin from randomization-based EFS/OS.
- Predefine what constitutes progression during neoadjuvant treatment and how imaging/pathologic assessment is scheduled.

## 6. Metastatic Breast Cancer

### PFS / OS

- Define time origin, progression criteria, death handling, missed assessments, and censoring.
- Specify investigator assessment versus blinded independent central review when relevant.

### RECIST-based response

For ORR/CBR/DoR, record:

- RECIST version (typically RECIST 1.1 unless protocol specifies otherwise)
- measurable-disease population
- best overall response rules
- whether CR/PR confirmation is required
- investigator versus central review
- response-evaluable denominator
- DoR start and end definitions

Do not equate a response-evaluable analysis with the randomized/treated population unless the estimand explicitly calls for it.

## 7. Survival Analysis

### Minimum specification

Before fitting a Cox model, define:

- time origin
- event
- censoring
- competing events
- analysis population
- covariate adjustment strategy
- proportional-hazards assessment

### Non-proportional hazards

Do not report a single HR as a complete summary when treatment effects clearly vary over time. Depending on the estimand and design, consider:

- time-varying treatment effects
- prespecified landmark survival probabilities/differences
- restricted mean survival time (RMST) and RMST difference/ratio
- piecewise or flexible parametric approaches

The chosen alternative must answer the clinical question rather than merely repair a failed PH test.

## 8. Competing Risks

When a competing event changes the probability of the event of interest, avoid default Kaplan-Meier estimation for cumulative incidence.

- Use **cumulative incidence functions (CIF)** for event probability in the presence of competing risks.
- Use **cause-specific hazards** for etiologic/rate questions among those currently event-free.
- Use **Fine-Gray/subdistribution hazards** when the target estimand concerns the cumulative-incidence function and the model interpretation is appropriate.
- State the competing event explicitly.

## 9. Landmark and Time-Dependent Analyses

Serial measurements such as ctDNA clearance, treatment response, or toxicity can create immortal-time/guarantee-time bias if treated as baseline variables.

### Landmark analysis

Predefine the landmark time, eligibility at the landmark, exposure/biomarker definition using information available by the landmark, and a risk period beginning at the landmark.

### Time-dependent covariate analysis

Use when exposure/biomarker status changes over time and the scientific estimand concerns current or updated status. Align measurement time with the risk interval and avoid using future information.

## 10. Biomarker Analyses

### Prognostic versus predictive

- **Prognostic:** association between biomarker and outcome, adjusting for relevant covariates.
- **Predictive:** heterogeneity of treatment effect according to biomarker.

A predictive claim requires a treatment-by-biomarker interaction (or equivalent prespecified heterogeneity analysis). "Significant in biomarker-positive but not significant in biomarker-negative" is not evidence of interaction.

### Continuous biomarkers

- Prefer continuous modeling when biologically and statistically reasonable.
- Consider transformations or restricted cubic splines for nonlinearity.
- Avoid arbitrary/data-driven dichotomization as the primary analysis.
- If a data-derived cut point is explored, label it exploratory and validate independently before strong clinical claims.

### High-dimensional / omics

- Separate discovery from validation.
- Predefine feature filtering and model-building steps.
- Control false discoveries (often FDR) for high-dimensional exploratory families.
- Account for batch effects and repeated specimens/patient clustering.
- Report internal validation and external validation when applicable.

## 11. ctDNA / MRD

Record, at minimum:

- assay/platform and whether tumor-informed or tumor-naive
- specimen type and processing
- prespecified sampling times (baseline, on-treatment, postoperative, surveillance, etc.)
- positivity threshold / limit of detection / indeterminate definition
- evaluable denominator and assay failures
- baseline positivity, clearance, persistence, and emergence definitions
- whether analysis is landmark or time-dependent

Do not equate `ctDNA-negative` with absence of disease. Interpret it as an assay result conditional on assay sensitivity, sampling, and disease biology.

## 12. RCT-Specific Principles

- Define the estimand and intercurrent-event strategy before analysis.
- Identify ITT, safety, and other analysis populations explicitly.
- Adjust for prespecified stratification factors when appropriate to the analysis plan.
- Predefine multiplicity control across confirmatory hypotheses.
- Report treatment effect and uncertainty, not p-values alone.
- Use CONSORT 2025 for reporting randomized trials.

## 13. Retrospective / Real-World Comparative Studies

- Choose adjustment variables from subject-matter knowledge/causal structure, not univariable p-value screening alone.
- For propensity methods, report the estimand (ATE/ATT/other), overlap, balance diagnostics, weighting/matching details, and effective sample size when relevant.
- Check immortal-time bias, guarantee-time bias, informative treatment selection, missingness, and informative censoring.
- Distinguish descriptive association from causal claims.

## 14. Multiplicity

Define hypothesis families before choosing an adjustment.

| Situation | Typical strategy |
|---|---|
| One confirmatory primary hypothesis | Prespecified alpha, no automatic extra correction |
| Co-primary/key secondary confirmatory family | Alpha splitting, hierarchy, gatekeeping, closed testing, or another justified FWER strategy |
| Prespecified subgroup/biomarker hypotheses | Interaction-focused plan with multiplicity strategy if confirmatory |
| High-dimensional exploratory biomarkers | FDR is often more appropriate than FWER |
| Exploratory analyses | Label exploratory; do not convert multiplicity into pseudo-confirmatory certainty |

## 15. Missing Data and Sensitivity Analyses

- Describe extent and pattern of missing data.
- Distinguish missing outcomes, missing covariates, missing scans/pathology, unavailable tissue/plasma, and assay failure.
- State assumptions of complete-case, multiple-imputation, likelihood-based, or other methods.
- For time-to-event endpoints, justify censoring rules and test clinically plausible alternatives when informative censoring is possible.
- Prespecify sensitivity analyses that challenge the assumptions underlying the primary result.

## 16. Minimum Oncology Analysis-Plan Checklist

- [ ] Clinical question and estimand defined
- [ ] Analysis population defined
- [ ] Endpoint operational definition complete
- [ ] Time origin/event/censoring/competing event defined
- [ ] Effect measure and model justified
- [ ] PH assessment/alternative plan defined for TTE outcomes
- [ ] Response criteria/pCR/RCB rules defined if applicable
- [ ] Biomarker role (prognostic/predictive) and interaction plan defined
- [ ] ctDNA sampling timing and landmark/time-dependent strategy defined if applicable
- [ ] Multiplicity family defined
- [ ] Missing-data and sensitivity plan defined
- [ ] Confirmatory versus exploratory claims separated

## References / Standards

- Hopewell S, et al. CONSORT 2025 statement. *BMJ*. 2025;389:e081123. doi:10.1136/bmj-2024-081123.
- ICH E9(R1). Addendum on Estimands and Sensitivity Analysis in Clinical Trials to the Guideline on Statistical Principles for Clinical Trials. 2019.
- Tolaney SM, et al. STEEP Version 2.0. *J Clin Oncol*. 2021;39:2720-2731. doi:10.1200/JCO.20.03613.
- NeoSTEEP Working Group. Standardized Definitions for Efficacy End Points in Neoadjuvant Breast Cancer Clinical Trials: NeoSTEEP. *J Clin Oncol*. doi:10.1200/JCO.23.00435.
- US FDA. *Pathological Complete Response in Neoadjuvant Treatment of High-Risk Early-Stage Breast Cancer: Use as an Endpoint to Support Accelerated Approval*. Final Guidance, July 2020.
- Eisenhauer EA, et al. RECIST 1.1. *Eur J Cancer*. 2009. PMID: 19097774.
- McShane LM, et al. REMARK recommendations for tumour marker prognostic studies. *Br J Cancer*. 2005;93:387-391. PMID: 16106245.
