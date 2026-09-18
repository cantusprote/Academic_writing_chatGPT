# Basic / Mechanistic Section Templates

> Conditional override for wet-lab, mechanistic, preclinical, cell/molecular biology, tumor-microenvironment, organoid, animal, imaging, and discovery-to-validation papers. Use with `docs/section_templates.md`; when the structures conflict for a basic/mechanistic project, this file takes precedence.

## Title

Purpose: state the biological system, central factor/process, and bounded claim without overstating mechanism or translational readiness.

Preferred patterns:
- `[Factor] Regulates [Phenotype] Through [Pathway] in [Model/Context]` only when mediation is directly supported.
- `[Factor] Promotes/Restrains [Phenotype] in [Disease/Model Context]` for perturbation-supported functional claims.
- `[State/Program] Is Associated With [Phenotype/Context]` for descriptive/association work.

Avoid `drives`, `essential`, `master regulator`, `therapeutic target`, or `predictive biomarker` unless the corresponding evidence is present.

## Abstract

Functions:
1. Biological problem/gap
2. Experimental systems and central strategy
3. Main findings in claim order
4. Bounded mechanism/translational implication

Report independent biological units where space permits. Do not turn human concordance into clinical utility or animal support into efficacy.

## Introduction

Paragraph functions:
1. Biological/disease problem
2. What is known about the relevant pathway/cell state/process
3. Exact mechanistic gap
4. Study question and bounded hypothesis

Do not preview unsupported mechanistic conclusions.

## Methods

Recommended subsection families; include only those used:

1. **Study/Experimental Overview** — systems, experimental sequence, preregistered/approved plan where applicable
2. **Cell Lines / Primary Cells / Organoids / Tissue Models** — source, identity, authentication, mycoplasma, culture conditions
3. **Human Specimens** — eligibility/source, consent/IRB, specimen handling, patient as inferential unit where relevant
4. **Animal Models** — species/strain/sex/age, allocation/randomization, blinding, sample-size rationale, humane endpoints, exclusions
5. **Perturbation / Intervention** — construct/reagent/drug, dose, timing, controls, target engagement
6. **Assays / Imaging / Molecular Measurements** — readout definition, acquisition, normalization, ROI/field selection, blinding
7. **Omics / Single-Cell / Spatial** — sample unit, QC, batch, normalization, clustering/modeling, multiplicity
8. **Experimental Units and Replication** — biological vs technical replicates, nested hierarchy
9. **Statistical Analysis** — planned contrasts, model, effect estimate/uncertainty, multiplicity, exclusions/sensitivity
10. **Data/Code/Material Availability** — repository/accession or planned availability statement as appropriate

Methods must distinguish target-engagement verification from phenotype measurement.

## Results

Organize by scientific question/claim, not by lab chronology.

Preferred subsection pattern:

`Question / claim title`
- why this question follows from the prior result
- experiment/analysis
- central observation
- bounded inference earned by the design
- control/boundary result when material
- next question

Typical progression, only when supported:
1. Define/discover state or association
2. Orthogonally confirm
3. Establish functional contribution by perturbation
4. Establish necessity/sufficiency when directly tested
5. Resolve specificity/mediation with rescue/dependency/epistasis
6. Test context robustness
7. Extend to in vivo/human relevance when scientifically necessary

Results may state a bounded functional/mechanistic inference when directly earned by the experimental design. They should not speculate beyond the data or import clinical implications.

## Discussion

Paragraph functions:
1. Principal biological finding and exact evidence level
2. Mechanistic interpretation: direct evidence vs inference
3. Comparison with prior literature and alternative explanations
4. Context robustness and boundaries
5. Translational relevance, only at the demonstrated level
6. Reproducibility/model limitations and unresolved mechanism
7. Concluding bounded statement

Explicitly separate `we observed`, `our experiments support`, and `we hypothesize`.

## Conclusion

Use the highest defensible claim from `story_map.md`. Do not upgrade preclinical work to practice-changing/clinical utility language.

## Figure Legends

For each panel report, as applicable:
- experimental system and condition
- independent biological `n`
- technical/nested observations if shown
- number of independent experiments
- what each point/bar/error bar represents
- exact statistical model/test and multiplicity handling
- definitions of significance markers
- scale bars and normalization
- source-data/representative-image statement where required
