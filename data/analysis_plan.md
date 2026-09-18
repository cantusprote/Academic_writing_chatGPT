# Analysis Plan

> 통계 분석 전 반드시 작성하고 사용자 승인 후 진행합니다.
> 상세 통계 가이드: `docs/statistical_analysis_guide.md` 참조

---

## 1. Research Question & Hypothesis (연구 질문 및 가설)

**연구 질문:**
- [연구 질문을 구체적으로 기술]

**가설:**
- H0: [귀무가설]
- H1: [대립가설]

---

## 2. Study Population (대상 선정/제외 기준)

**Design:** `[연구 설계 입력: RCT / Cohort / Case-Control / etc.]`

**Inclusion Criteria:**
- [기준 1]
- [기준 2]

**Exclusion Criteria:**
- [기준 1]
- [기준 2]

**Expected Sample Size:** [N]

### Analysis Population / Estimand
- **Analysis population(s):** [ITT / modified ITT / per-protocol / safety / biomarker-evaluable / other]
- **Estimand:** [treatment/exposure contrast, target population, endpoint/variable, handling of intercurrent events, summary measure]
- **Oncology context (if applicable):** [early/metastatic; neoadjuvant/adjuvant/advanced; breast cancer subtype such as HR+/HER2−, HER2+, TNBC]

---

## 3. Data Overview

### Source File
- **File:** `[filename.csv/xlsx]`
- **Rows:** `[n rows]`
- **Columns:** `[n columns]`

### Variable Summary

| Variable | Type | Description | Role | Missing (%) |
|----------|------|-------------|------|-------------|
| `[var]` | Continuous/Categorical | `[설명]` | Primary/Secondary/Covariate | `[%]` |

---

## 4. Variable Definitions (변수 정의)

### Endpoint Definition Table

> Time-to-event endpoints must pre-specify time origin, event, and censoring. Use disease-specific consensus definitions (e.g., STEEP/NeoSTEEP) when applicable rather than relying on endpoint labels alone.

| Endpoint | Definition / Assessment | Time Origin | Event | Censoring / Competing Event | Analysis Population |
|----------|-------------------------|-------------|-------|-----------------------------|---------------------|
| [Primary/Secondary endpoint] | [operational definition] | [randomization/surgery/treatment start/etc.] | [event definition] | [censoring rule; competing event if relevant] | [population] |

### Primary Endpoint
- **Variable:** [변수명]
- **Definition:** [정의]
- **Measurement:** [측정 방법 및 시점]

### Secondary Endpoints
- [변수명]: [정의 및 측정 방법]
- [변수명]: [정의 및 측정 방법]

### Exploratory Endpoints (해당 시)
- [변수명]: [정의]

### Oncology Response / Pathology Fields (해당 시)
- **RECIST:** [version; BOR/ORR/DCR/DoR definition; confirmation requirement]
- **pCR:** [protocol-specific definition, e.g., ypT0/is ypN0]
- **RCB:** [continuous score and/or class 0/I/II/III; assessment method]
- **Assessment schedule / central review:** [timing; investigator vs independent review]

### Covariates / Confounders
- [변수명]: [정의 및 선정 근거]

---

## 5. Statistical Methods (통계 검정법 선택 및 근거)

### Descriptive Statistics
- Continuous: mean ± SD and/or median [IQR] according to distribution, scale, and scientific purpose; inspect graphical/distributional features when model assumptions matter
- Categorical: n (%)

### Comparative Analysis

| Comparison | Variable Type | Distribution | Test | Justification |
|------------|---------------|--------------|------|---------------|
| [비교 내용] | Continuous/Categorical | Normal/Non-normal | [검정법] | [선택 근거] |

### Advanced Analysis (해당 시)
- [ ] Linear regression — [목적]
- [ ] Logistic regression — [목적]
- [ ] Cox regression — [목적]
- [ ] Competing-risk analysis — [competing event; cumulative incidence / cause-specific hazard / Fine-Gray as appropriate]
- [ ] Landmark analysis — [pre-specified landmark; eligibility; target contrast]
- [ ] Time-dependent covariate analysis — [time-varying exposure/biomarker; model and time alignment]
- [ ] Other: [specify]

### Biomarker / Translational / ctDNA Plan (해당 시)
- **Biomarker hypothesis and role:** [prognostic / predictive / pharmacodynamic / exploratory]
- **Assay/specimen:** [tissue/plasma; platform; collection time points; QC/evaluable criteria]
- **Cut-point:** [pre-specified / validated / continuous primary; data-derived explicitly exploratory]
- **Predictive effect:** [treatment × biomarker interaction; do not infer interaction from subgroup p-values]
- **Longitudinal ctDNA:** [baseline; clearance/persistence/emergence; landmark or time-dependent strategy; immortal-time bias prevention]
- **High-dimensional analyses:** [feature filtering/model validation; FDR; internal/external validation as applicable]

---

## 6. Significance Level & Multiple Comparison (유의수준 및 다중비교 보정)

| Parameter | Value |
|-----------|-------|
| Significance level (α) | 0.05 |
| Confidence interval | 95% |
| Multiple comparison correction | [None / Bonferroni / Holm / FDR] |
| Correction 적용 대상 | [어떤 비교에 적용할지] |

### Multiplicity Families
| Family | Hypotheses / Endpoints | Confirmatory vs Exploratory | Error Control / Testing Strategy |
|--------|-------------------------|----------------------------|----------------------------------|
| [Primary] | [hypotheses] | [confirmatory] | [α allocation / hierarchy / gatekeeping / other] |
| [Secondary/subgroup/biomarker] | [hypotheses] | [confirmatory/exploratory] | [FWER/FDR/none with exploratory labeling] |

---

## 7. Missing Data & Sensitivity Analyses

- **Extent/pattern:** [variables/time points; summarize missingness]
- **Primary handling:** [complete case / multiple imputation / likelihood-based / endpoint-specific censoring / other, with assumptions]
- **Outcome/biomarker missingness:** [non-evaluable scans, missing pathology, unavailable tissue/plasma, assay failure]
- **Sensitivity analyses:** [alternative censoring/event definitions; missing-data assumptions; analysis population; model assumptions]
- **Causal-bias checks (observational/landmark studies):** [confounding; immortal-time/guarantee-time; selection; informative censoring; time-varying confounding as applicable]

---

## 8. Output Plan

### Scripts (→ data/py/)
| Script | Purpose |
|--------|---------|
| 01_descriptive.py | Baseline demographics |
| 02_comparative.py | Group comparisons |
| 03_regression.py | Advanced analysis (if needed) |

### Tables (→ drafts/)
| Table | Content | Source |
|-------|---------|--------|
| table_1.md | Demographics & Baseline | results/table1_demographics.csv |
| table_2.md | Primary Outcomes | results/table2_outcomes.csv |
| table_3.md | [Additional Analysis] | results/table3_*.csv |

### Figures (→ drafts/figures/)
| Figure | Content | Type |
|--------|---------|------|
| [fig_N.png] | [내용] | [Bar/Box/Line/Survival/Flow] |

---

## Checklist Before Proceeding

- [ ] 연구 질문과 가설이 명확한가?
- [ ] 선정/제외 기준이 구체적인가?
- [ ] Primary endpoint가 1개로 정의되었는가?
- [ ] Analysis population과 estimand가 명확한가?
- [ ] Time-to-event endpoint의 time origin/event/censoring이 명시되었는가?
- [ ] 해당 시 RECIST/pCR/RCB 및 competing-risk/landmark/time-dependent 분석이 사전 정의되었는가?
- [ ] Biomarker/ctDNA 가설, interaction, longitudinal analysis가 사전 정의되었는가?
- [ ] 통계 검정법이 데이터 유형에 적합한가?
- [ ] Multiplicity family와 error-control 전략이 정의되었는가?
- [ ] Missing data와 주요 sensitivity analysis가 계획되었는가?
- [ ] **사용자 승인 완료** → 분석 진행
