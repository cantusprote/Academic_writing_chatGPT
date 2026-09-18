# Analysis Plan

> 분석 전 반드시 작성하고 사용자 승인 후 진행합니다.
> **Research-mode routing:**
> - Clinical oncology / clinical translational → `docs/oncology_analysis_guide.md`
> - Basic / mechanistic experimental → `docs/basic_research_analysis_guide.md`
> - Hybrid → apply both guides to their respective components
> - `docs/statistical_analysis_guide.md` is generic background only; mode-specific guides override conflicting heuristics.

---

## 1. Research Question and Mode

- **Research question:** [구체적으로 기술]
- **Hypothesis / expected biological or clinical contrast:** [필요 시]
- **Mode:** [Clinical / Translational-Clinical / Basic-Mechanistic / Hybrid]
- **Confirmatory vs exploratory status:** [confirmatory / exploratory / mixed]

### Basic / Mechanistic Question (Basic-Mechanistic or Hybrid only)
- **Biological question:** [무엇을 검증하는가]
- **Planned biological contrast:** [control vs perturbation / genotype × treatment / time × condition / etc.]
- **Primary phenotype/readout:** [주요 기능/표현형 readout]
- **Desired claim class:** [descriptive / association / functional / necessity / sufficiency / mechanism]

---

## 2A. Clinical / Clinical-Translational Design (Clinical, Translational-Clinical, or Hybrid only)

- **Design:** [RCT / prospective cohort / retrospective cohort / case-control / biomarker study / other]
- **Population / setting:** [target population, institution(s), period]
- **Inclusion criteria:** [list]
- **Exclusion criteria:** [list]
- **Expected/available sample size:** [N + rationale if prospective]
- **Analysis population(s):** [ITT / modified ITT / per-protocol / safety / biomarker-evaluable / other]
- **Estimand:** [treatment/exposure contrast, target population, variable/endpoint, intercurrent-event handling, summary measure]
- **Oncology context:** [early/metastatic; neoadjuvant/adjuvant/advanced; subtype]

### Clinical Endpoint Definition Table

| Endpoint | Role | Operational definition | Time origin / assessment | Event | Censoring / competing event | Analysis population |
|---|---|---|---|---|---|---|
| [endpoint] | Primary/Secondary/Exploratory | [definition] | [origin/schedule] | [event] | [rule] | [population] |

### Oncology Response / Pathology Fields (if applicable)
- **RECIST:** [version; BOR/ORR/DCR/DoR; confirmation; investigator vs central review]
- **pCR:** [protocol-specific definition]
- **RCB:** [continuous index and/or class; assessment method]
- **Assessment schedule:** [timing]

### Biomarker / ctDNA Fields (if applicable)
- **Biomarker hypothesis/role:** [prognostic / predictive / pharmacodynamic / exploratory]
- **Assay/specimen:** [platform, specimen, collection time points, QC/evaluable criteria]
- **Cut-point:** [prespecified / validated / continuous primary / explicitly exploratory]
- **Predictive analysis:** [treatment × biomarker interaction or equivalent]
- **Longitudinal ctDNA:** [baseline / clearance / persistence / emergence; landmark or time-dependent strategy]

---

## 2B. Basic / Mechanistic Experimental Design (Basic-Mechanistic or Hybrid only)

- **Experimental system(s):** [cell line / primary cell / organoid / animal / tissue / imaging / omics / other]
- **Independent experimental unit:** [independent experiment / donor / animal / specimen / other]
- **Biological replicate:** [definition and planned/available n]
- **Technical replicate / subsample:** [wells / fields / cells / ROIs / repeated measurements]
- **Nested hierarchy:** [e.g., cells → fields → wells → experiment → donor]
- **Factor/intervention structure:** [treatment / genotype / time / dose / factorial design]
- **Primary planned contrast:** [exact comparison or interaction]
- **Batch/block factors:** [experimental day / plate / operator / litter / sequencing batch / other]
- **Repeated measures:** [none / time / region / repeated condition / other]
- **Randomization/allocation:** [method / not applicable + rationale]
- **Blinding/masking:** [acquisition / scoring / analysis / not feasible + rationale]
- **Sample-size rationale:** [prospective power / precision / exploratory-resource rationale / field convention]
- **Predefined exclusion/QC criteria:** [failed perturbation, contamination, assay QC, humane endpoint, imaging/omics QC, etc.]

### Experimental Readout Table

| Readout | Role | Scale / normalization | Unit of inference | Condition / time | Target-engagement separate? |
|---|---|---|---|---|---|
| [phenotype/assay] | Primary/Secondary/Exploratory | [raw/fold/normalized/transformed] | [biological unit] | [dose/time/context] | [yes/no + assay] |

### Model / Reagent Identity (if applicable)
- **Cell/model source and authentication:** [source, identity method, mycoplasma status, passage/provenance]
- **Critical reagents/constructs:** [clone/catalog/provider/sequence/vector as appropriate]
- **Animal model:** [species/strain/sex/age; housing/allocation/humane endpoint as appropriate]

---

## 3. Data Overview (all modes)

### Source Files
- **Raw/processed file(s):** [filename.csv/xlsx/etc.]
- **Rows / observations:** [n]
- **Columns / features:** [n]
- **Unit represented by one row:** [patient / animal / experiment / donor / cell / other]

### Variable / Feature Summary

| Variable / feature | Type | Description | Role | Missing/QC issue |
|---|---|---|---|---|
| [var] | Continuous/Categorical/Count/etc. | [description] | Primary/Secondary/Covariate/Factor | [details] |

---

## 4. Statistical Model and Effect Estimate

### Planned Analyses

| Scientific contrast / question | Experimental or analysis unit | Dependency structure | Model/test | Effect estimate | Justification |
|---|---|---|---|---|---|
| [comparison] | [unit] | [independent/paired/nested/repeated] | [model] | [difference/ratio/coefficient/interaction/etc.] | [reason] |

### Clinical-specific advanced methods (if applicable)
- [ ] Cox / flexible survival model — [purpose]
- [ ] Competing-risk analysis — [event/competing event; CIF/cause-specific/Fine-Gray as appropriate]
- [ ] Landmark analysis — [landmark; eligibility; target contrast]
- [ ] Time-dependent covariate analysis — [time alignment]
- [ ] Causal/propensity method — [estimand, variables, balance diagnostics]

### Basic / Mechanistic model structure (if applicable)
- **Primary model:** [linear / generalized / mixed-effects / paired / nonparametric / other]
- **Repeated/nested handling:** [model or summary strategy]
- **Batch/block handling:** [fixed/random/block factor / other]
- **Technical replicate handling:** [summary before inference / hierarchical model / other]
- **Effect estimate + uncertainty:** [difference / fold change with scale / coefficient / interaction / CI]
- **Robustness/sensitivity:** [alternative model/summary/exclusion strategy]

> Do not select parametric vs nonparametric methods from a normality-test p-value alone. For basic/mechanistic work, start from the experimental unit, contrast, dependency structure, and model assumptions.

---

## 5. Multiplicity and Error Control

- **Significance level / confidence level:** [if inferential testing is used]
- **Hypothesis family:** [define scientifically; do not define by raw comparison count]
- **Confirmatory vs exploratory:** [state]
- **Strategy:** [none justified / hierarchy / gatekeeping / Holm/Bonferroni / FDR / other]

| Family | Hypotheses / readouts | Role | Error-control strategy |
|---|---|---|---|
| [family] | [items] | Confirmatory/Exploratory | [strategy] |

---

## 6. Missingness, Exclusions, QC, and Sensitivity

### Clinical / patient data (if applicable)
- **Missing outcomes/covariates/specimens:** [extent/pattern]
- **Primary handling:** [complete case / MI / likelihood / censoring / other]
- **Sensitivity:** [alternative censoring/event/missing-data assumptions]
- **Bias checks:** [confounding, immortal-time, informative censoring, selection, etc.]

### Experimental data (if applicable)
- **Assay/model QC failure:** [rule]
- **Contamination/acquisition failure:** [rule]
- **Outlier handling:** [prespecified rule; do not exclude for unfavorable result]
- **Non-evaluable animal/specimen/image/omics sample:** [rule]
- **Sensitivity/robustness:** [alternative exclusions, summaries, models, batches]

---

## 7. Output Plan

### Analysis scripts
| Script | Purpose |
|---|---|
| [01_*.py / .R] | [mode-appropriate analysis] |
| [02_*.py / .R] | [mode-appropriate analysis] |

### Canonical result files (`results/`)
| File | Content |
|---|---|
| [result_*.csv] | [result values that may appear in manuscript/tables/figures] |

> **Numerical grounding:** study **result values** in the manuscript must trace to `results/*.csv`. Experimental-design constants (dose, incubation time, seeding density, planned replicate count, acquisition settings, etc.) are grounded in this approved analysis plan / Methods source, not in `results/*.csv`.

### Tables / Figures
| Artifact | Scientific purpose | Source |
|---|---|---|
| [table/figure] | [claim/readout] | [result CSV / analysis output] |

---

## Checklist Before Proceeding

### All modes
- [ ] Research mode is explicit.
- [ ] Research/biological question and planned contrast are clear.
- [ ] Statistical model follows the unit of inference and dependency structure.
- [ ] Multiplicity family/strategy is defined when applicable.
- [ ] Missingness/exclusion/QC and sensitivity rules are specified where applicable.

### Clinical / Clinical-Translational only
- [ ] Population, eligibility, and analysis population(s) are explicit.
- [ ] Estimand is defined where applicable.
- [ ] Primary/key endpoint(s) are operationally defined.
- [ ] TTE endpoints specify time origin/event/censoring/competing events.
- [ ] RECIST/pCR/RCB and biomarker/ctDNA timing are prespecified when applicable.

### Basic / Mechanistic only
- [ ] Independent experimental unit is explicit.
- [ ] Biological vs technical replicates and nested observations are separated.
- [ ] Planned contrast and primary phenotype/readout are explicit.
- [ ] Batch/block/repeated-measure structure is handled by design/model.
- [ ] Randomization/blinding/sample-size rationale/exclusion rules are documented when applicable.
- [ ] Target-engagement verification is separated from phenotype evidence.
- [ ] Model/reagent identity and authentication requirements are documented when applicable.

- [ ] **사용자 승인 완료** → 분석 진행
