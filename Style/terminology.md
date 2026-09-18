# Terminology Registry — Breast Medical Oncology and Translational Research

> Durable terminology and reporting conventions for breast cancer clinical/translational manuscripts. Mutable drug labels, approvals, reimbursement, and treatment indications are intentionally excluded.
> The lint parser reads `Preferred Term` and semicolon-separated `Forbidden Terms`. Project-specific protocol/SAP definitions take precedence when more specific.

## Breast Subtypes and Receptors

| Concept | Preferred Term | Forbidden Terms | First Definition | Context | Notes |
|---|---|---|---|---|---|
| Hormone receptor status | hormone receptor-positive (HR-positive); hormone receptor-negative (HR-negative) | hormone-positive; hormone-negative | Define HR at first use | All sections | State ER/PR operational criteria when relevant. |
| Estrogen receptor | estrogen receptor (ER) | oestrogen receptor unless journal requires British spelling | Define ER at first use | All sections | Report assay/cutoff when relevant. |
| Progesterone receptor | progesterone receptor (PR) | progestin receptor | Define PR at first use | All sections | PR is not synonymous with HR. |
| HER2-positive | HER2-positive breast cancer | HER2+ cancer in formal prose | Define HER2 as required | All sections | Use study-era assay/scoring criteria; do not encode treatment eligibility here. |
| HER2-negative | HER2-negative breast cancer | HER2− as prose-only shorthand | Define HER2 as required | All sections | Keep assay result distinct from treatment eligibility. |
| HER2-low | HER2-low breast cancer | HER2-low-positive; HER2 weakly positive | Define operational IHC/ISH criteria | Methods, Results | Expression category, not conventional HER2-positive disease. |
| HER2-ultralow | HER2-ultralow breast cancer | ultra-low HER2; HER2 ultralow positive | Define operational criteria | Methods, Results | Use only if explicitly analyzed. |
| Triple-negative | triple-negative breast cancer (TNBC) | triple negative cancer; basal-like breast cancer as a synonym | Define TNBC at first use | All sections | TNBC and basal-like molecular subtype are not interchangeable. |
| HR+/HER2− subtype | HR-positive/HER2-negative breast cancer | luminal breast cancer as a synonym | Define HR and HER2 | All sections | Molecular luminal subtype requires an appropriate classifier. |
| Receptor change | receptor status conversion | receptor discordance as a synonym for directional change | Define paired specimens/time points | Methods, Results | State receptor and direction of change. |

## Disease Setting and Treatment Timing

| Concept | Preferred Term | Forbidden Terms | First Definition | Context | Notes |
|---|---|---|---|---|---|
| Nonmetastatic disease | early breast cancer (EBC) | early-stage metastatic breast cancer | Define stage eligibility | All sections | State anatomic stage/risk separately. |
| Locally advanced disease | locally advanced breast cancer | advanced breast cancer when specifically nonmetastatic | Define stage criteria | Methods | Do not imply metastatic disease. |
| Metastatic disease | metastatic breast cancer (MBC) | advanced breast cancer when metastatic status must be explicit | Define MBC | All sections | Distinguish de novo and recurrent MBC when relevant. |
| Recurrent disease | recurrent breast cancer | relapsed breast cancer as default wording | Define recurrence type | Methods, Results | Distinguish locoregional and distant recurrence. |
| Preoperative therapy | neoadjuvant systemic therapy | preoperative adjuvant therapy | Define modality/regimen | All sections | Use neoadjuvant chemotherapy only for chemotherapy. |
| Postoperative therapy | adjuvant systemic therapy | postoperative neoadjuvant therapy | Define modality/regimen | All sections | Specify endocrine/chemotherapy/targeted modality as applicable. |
| Residual disease | residual invasive disease | remnant cancer; treatment failure | Define assessed sites | Results | Distinguish breast and nodal residual disease. |
| Treatment line | first-line therapy; second-line therapy; later-line therapy | 1st line in prose; 2nd line in prose | Define rules if nonstandard | Methods, Results | Important in retrospective MBC cohorts. |

## Neoadjuvant Pathologic Response

| Concept | Preferred Term | Forbidden Terms | First Definition | Context | Notes |
|---|---|---|---|---|---|
| Pathologic complete response | pathologic complete response (pCR) | pathological CR; complete pathological response | Define exact ypT/ypN criterion | Abstract, Methods, Results | Do not assume pCR definitions are equivalent. |
| Residual Cancer Burden | Residual Cancer Burden (RCB) | residual cancer burden score when referring to class | Define RCB | Methods, Results | Distinguish RCB index from RCB class. |
| Continuous RCB | RCB index | RCB class when continuous score is analyzed | Define calculation | Methods, Results | Preserve continuous scale. |
| Categorical RCB | RCB class | RCB score when categorical class is analyzed | Define classes | Methods, Results | Report RCB-0 through RCB-III as applicable. |
| Post-treatment stage | ypTNM stage | postoperative clinical stage | Define staging edition | Methods, Results | Preserve y and p prefixes. |

## Time-to-Event Endpoints — Strict Non-interchangeability

| Concept | Preferred Term | Forbidden Terms | First Definition | Context | Notes |
|---|---|---|---|---|---|
| Event-free survival | event-free survival (EFS) | event free survival | Define time origin and event set | Abstract, Methods, Results | Never substitute IDFS, RFS, DFS, PFS, or OS. |
| Invasive disease-free survival | invasive disease-free survival (IDFS) | invasive disease free survival; iDFS | Define time origin and event set | Abstract, Methods, Results | Never substitute EFS, RFS, DFS, PFS, or OS. |
| Recurrence-free survival | recurrence-free survival (RFS) | relapse-free survival unless prespecified | Define recurrence/death rules | Abstract, Methods, Results | Definitions vary; never silently relabel another endpoint. |
| Disease-free survival | disease-free survival (DFS) | disease free survival | Define only if prespecified | Methods, Results | DFS is not automatically IDFS/EFS/RFS. |
| Progression-free survival | progression-free survival (PFS) | progression free survival | Define progression/death rules | Abstract, Methods, Results | Do not substitute EFS/IDFS/RFS/OS. |
| Overall survival | overall survival (OS) | overall mortality-free survival | Define time origin | Abstract, Methods, Results | Death from any cause unless explicitly defined otherwise. |
| Landmark estimate | landmark survival estimate | landmark analysis when only a fixed-time survival estimate is reported | Define time point | Results | A time-point estimate is not itself a landmark analysis. |
| Landmark analysis | landmark analysis | survival analysis from diagnosis when landmark eligibility is imposed later | Define landmark/risk set | Methods | Explain exclusion of pre-landmark events. |

## Tumor Response

| Concept | Preferred Term | Forbidden Terms | First Definition | Context | Notes |
|---|---|---|---|---|---|
| Objective response | objective response rate (ORR) | overall response rate | Define population/criteria | Methods, Results | Usually CR + PR under prespecified criteria. |
| Clinical benefit | clinical benefit rate (CBR) | clinical response rate | Define components and SD duration | Methods, Results | CBR is not inferred from ORR. |
| Response duration | duration of response (DoR) | response duration rate | Define start/event/censoring | Methods, Results | Analyze responders per protocol/SAP. |
| RECIST | Response Evaluation Criteria in Solid Tumors version 1.1 (RECIST 1.1) | RECIST criteria 1.1; RECIST v1.1 criteria | Define at first use | Methods | State investigator versus central review if relevant. |
| Complete response | complete response (CR) | complete remission when RECIST response is meant | Define at first response use | Results | Follow prespecified criteria. |
| Partial response | partial response (PR) | partial remission when RECIST response is meant | Define at first response use | Results | Context must distinguish PR from progesterone receptor. |
| Stable disease | stable disease (SD) | stable response | Define SD | Results | SD is not an objective response. |
| Progressive disease | progressive disease (PD) | progression response | Define PD | Results | Distinguish radiographic/clinical progression if needed. |

## Biomarkers and Interaction

| Concept | Preferred Term | Forbidden Terms | First Definition | Context | Notes |
|---|---|---|---|---|---|
| Prognostic biomarker | prognostic biomarker | predictive biomarker when no treatment interaction is demonstrated | Define biomarker/endpoint/population | All sections | Outcome association alone does not establish treatment-effect prediction. |
| Predictive biomarker | predictive biomarker | prognostic marker as a synonym | Define treatment comparison/endpoint | Methods, Results | Predictive claims require differential treatment-effect evidence. |
| Interaction | treatment-by-biomarker interaction | subgroup difference based only on separate within-group p-values | Define model/interaction term | Methods, Results | Report interaction estimate/test. |
| Subgroup analysis | subgroup analysis | interaction analysis unless an interaction is modeled | Define prespecified/exploratory status | Methods, Results | Do not claim heterogeneity from separate subgroup significance tests. |
| Biomarker positivity | biomarker-positive population | biomarker responder | Define assay/specimen/cutoff/timing | Methods | Biomarker status is not clinical response. |
| Exploratory biomarker | exploratory biomarker analysis | validated biomarker | Label as exploratory | Methods, Discussion | Address multiplicity and validation. |

## ctDNA and Molecular Residual Disease

| Concept | Preferred Term | Forbidden Terms | First Definition | Context | Notes |
|---|---|---|---|---|---|
| Circulating tumor DNA | circulating tumor DNA (ctDNA) | circulating DNA when tumor-derived DNA is meant; cfDNA as a synonym | Define ctDNA | All sections | ctDNA is a tumor-derived subset of cfDNA. |
| Cell-free DNA | cell-free DNA (cfDNA) | ctDNA when total cell-free DNA is measured | Define cfDNA | Methods | Keep analyte assay-specific. |
| Molecular residual disease | molecular residual disease (MRD) | minimal residual disease as default in solid-tumor ctDNA manuscripts | Define assay positivity/timing | Methods, Results | MRD positivity is an assay result, not automatically clinical recurrence. |
| ctDNA detection | ctDNA detected; ctDNA not detected | ctDNA-positive disease as proof of recurrence; ctDNA-negative disease as proof of cure | Define threshold | Results, Discussion | Prefer detected/not detected for assay observations. |
| ctDNA clearance | ctDNA clearance | molecular remission without definition | Define baseline positivity and negative time point(s) | Methods, Results | Specify single versus serial negativity. |
| Tumor-informed assay | tumor-informed ctDNA assay | personalized assay without describing tumor-informed design | Define approach | Methods | Distinguish from tumor-naive/plasma-only assays. |
| Tumor-naive assay | tumor-naive ctDNA assay | tumor-uninformed as a pejorative shorthand | Define approach | Methods | State measured feature classes as applicable. |

## ESR1 and Endocrine Resistance

| Concept | Preferred Term | Forbidden Terms | First Definition | Context | Notes |
|---|---|---|---|---|---|
| ESR1 alteration | ESR1 mutation | ESR1-positive unless assay definition is explicit | Define variant/assay/specimen | Methods, Results | Distinguish mutation from expression. |
| ESR1-mutant disease | ESR1-mutant breast cancer | ESR1 mutation-positive cancer as default prose | Define detection method | Results, Discussion | Do not assume clonality beyond measured data. |
| Endocrine resistance | endocrine resistance | hormone resistance | Define operational criteria | Methods, Results | Distinguish primary/secondary resistance if analyzed. |
| Endocrine sensitivity | endocrine-sensitive disease | hormone-sensitive breast cancer when endocrine sensitivity is intended | Define operational criteria | Methods, Results | HR positivity alone does not prove endocrine sensitivity. |
| Acquired resistance | acquired endocrine resistance | secondary mutation as a synonym | Define timing/criteria | Discussion | State mechanism only when supported. |

## Safety and ILD

| Concept | Preferred Term | Forbidden Terms | First Definition | Context | Notes |
|---|---|---|---|---|---|
| Adverse event | adverse event (AE) | side effect as formal safety endpoint | Define AE | Methods, Results | State grading system/version. |
| Serious adverse event | serious adverse event (SAE) | severe adverse event as a synonym | Define SAE | Methods, Results | Seriousness and severity differ. |
| Treatment-emergent AE | treatment-emergent adverse event (TEAE) | treatment-related adverse event as a synonym | Define TEAE | Methods, Results | Emergence and attribution differ. |
| Treatment-related AE | treatment-related adverse event (TRAE) | treatment-emergent adverse event as a synonym | Define attribution | Methods, Results | State attribution method. |
| High-grade AE | grade 3 or higher adverse event | severe toxicity without grade | Define grading system | Results | Prefer explicit grade. |
| Interstitial lung disease | interstitial lung disease (ILD)/pneumonitis | interstitial pneumonia as a generic synonym | Define diagnostic/adjudication method if relevant | Methods, Results | Report grade and attribution separately. |
| Fatal AE | grade 5 adverse event | fatal toxicity as proof of drug causality | Define grading/attribution | Results | Grade and causality are separate. |

## Statistical Reporting

| Concept | Preferred Term | Forbidden Terms | First Definition | Context | Notes |
|---|---|---|---|---|---|
| Confidence interval | 95% confidence interval (CI) | confidence limits as a synonym | Define CI | Methods, Results | Pair estimates with CIs when feasible. |
| Hazard ratio | hazard ratio (HR) | risk ratio when a Cox-model hazard ratio is reported | Define HR/reference | Methods, Results | HR is not a risk ratio. |
| Odds ratio | odds ratio (OR) | risk ratio when an odds ratio is reported | Define OR/reference | Methods, Results | Preserve the estimand. |
| Risk ratio | risk ratio (RR) | odds ratio as a synonym | Define RR/reference | Methods, Results | Preserve the estimand. |
| Exact p-value | p = 0.023 | p = NS; p = 0.000 | No definition required | Results, Tables | Use p < 0.001 rather than p = 0.000. |
| Statistical significance | statistically significant | significant trend; marginally significant | Define alpha | Results | Statistical significance is not clinical importance. |
| Multivariable model | multivariable model | multivariate model when one outcome has multiple predictors | Define model | Methods, Results | Reserve multivariate for multiple outcomes. |
| Univariable model | univariable analysis | univariate analysis when describing one predictor in regression | Define model | Methods, Results | Match multivariable terminology. |
| Cox model | Cox proportional hazards model | Cox regression without checking proportional hazards | Define at first use | Methods | Describe PH-assumption assessment. |
| Kaplan-Meier | Kaplan-Meier method | Kaplan Meier; Kaplan-Meier test | Define at first use | Methods, Results | Log-rank is the comparison test when applicable. |
| Competing risks | competing-risks analysis | Kaplan-Meier analysis when competing events are simply censored for cumulative incidence | Define event/competing event | Methods, Results | Specify CIF and cause-specific/subdistribution model as applicable. |
| Time-dependent covariate | time-dependent covariate | baseline covariate when exposure changes over follow-up | Define updating | Methods | Guard against immortal-time bias. |
| Time-varying effect | time-varying effect | time-dependent covariate as a synonym | Define model | Methods | Changing covariates and changing coefficients differ. |
| Multiple testing | multiplicity adjustment | multiple comparison correction as a generic substitute | Define family/method/error rate | Methods | State exploratory unadjusted analyses explicitly. |
| Interaction test | p for interaction | subgroup p-value as evidence of interaction | Define model | Results | Significance in one subgroup only is not evidence of interaction. |
| Missing data | missing data | missing values ignored | Define handling | Methods | State assumptions/sensitivity analyses as relevant. |
| Complete cases | complete-case analysis | available-case analysis as a synonym | Define included observations | Methods | Distinguish complete- from available-case analyses. |
| Multiple imputation | multiple imputation | mean imputation | Define model/number of imputations | Methods | Report pooling method as appropriate. |
| Effect estimate | effect estimate | effect size when the estimand is unclear | Define estimand/model | Results | Report CI and units/reference category. |

## General Oncology Reporting

| Concept | Preferred Term | Forbidden Terms | First Definition | Context | Notes |
|---|---|---|---|---|---|
| Clinical population | patients; participants | subjects in clinical manuscripts | No definition required | All sections | Follow study/journal convention. |
| Treatment discontinuation | treatment discontinuation | treatment dropout | Define reason categories | Results | Distinguish treatment discontinuation from study withdrawal. |
| Dose reduction | dose reduction | dose de-escalation when toxicity-driven dose modification is meant | Define if analyzed | Results | De-escalation usually denotes a strategy. |
| Relative dose intensity | relative dose intensity (RDI) | dose intensity ratio without definition | Define formula | Methods, Results | State planned-dose/time denominator. |
| Follow-up | median follow-up | observation period as a synonym | Define calculation if relevant | Results | Reverse Kaplan-Meier may be appropriate for follow-up estimation. |
| Unreached median | median not reached | median not achieved | No definition required | Results | Give CI if estimable. |
| Non-estimable value | not estimable (NE) | not available when statistical estimation failed | Define NE if frequent | Tables, Results | Distinguish from missing/not assessed. |
