# Basic / Mechanistic Research QC Checklist (Sim Custom v0.1.0)

> Use during Phase 3 planning and Phase 6 QC for wet-lab, mechanistic, preclinical, molecular/cell biology, tumor-microenvironment, and discovery-to-validation manuscripts.

## A. Central Claim and Story

- [ ] Biological problem and central scientific question are explicit.
- [ ] Desired main claim can be stated in one sentence.
- [ ] `drafts/story_map.md` exists and matches `drafts/draft_plan.md`.
- [ ] Current evidence level is stated.
- [ ] Claim boundary / non-claim is explicit.
- [ ] Weakest evidence link is identified.
- [ ] Results architecture follows scientific questions/claims rather than laboratory chronology.

## B. Claim Strength

- [ ] Association is not written as causation.
- [ ] Expression/abundance confirmation is not labeled functional validation.
- [ ] Perturbation effect is not automatically labeled mechanism specificity.
- [ ] Necessity and sufficiency are not conflated.
- [ ] `mediates`, `drives`, `required for`, and `sufficient for` are used only when directly supported.
- [ ] Human concordance is not labeled clinical utility without appropriate clinical validation.
- [ ] Translational wording names the actual use case.

## C. Experimental Unit and Replication

- [ ] Independent experimental unit is defined for every central experiment.
- [ ] Biological and technical replicates are distinguished.
- [ ] Cells/fields/wells/repeated measurements are not silently counted as independent biological `n`.
- [ ] Nested data hierarchy is reported when applicable.
- [ ] Multiple donors/animals/models are handled at the correct inferential level.
- [ ] Statistical analysis matches the true experimental unit.


## D. Experimental Rigor and Reproducibility

- [ ] Sample-size rationale is stated (prospective power/precision/exploratory rationale as appropriate).
- [ ] Allocation/randomization is described when feasible and scientifically relevant.
- [ ] Blinding is described for subjective or analyst-dependent acquisition/scoring/annotation when applicable.
- [ ] Exclusion/QC criteria were defined independently of the preferred result; exclusions and reasons are reported.
- [ ] Batch/block factors (day, plate, operator, litter/cage, sequencing run, imaging session) are documented and handled.
- [ ] Sex is reported and considered as a biological variable when relevant to the model/question.
- [ ] Negative/null and context-dependent results that materially bound the main claim remain visible.

## E. Cell, Reagent, and Model Identity

- [ ] Cell-line/tissue/model source is traceable (repository/provider/catalog where applicable).
- [ ] Human cell lines are authenticated with an appropriate method when required by journal/field standards.
- [ ] Mycoplasma testing/status is documented for cultured-cell experiments when applicable.
- [ ] Passage range or culture history is reported when it could affect phenotype.
- [ ] Critical antibodies/reagents include enough identity information for reproducibility (target, clone/catalog/provider/lot as appropriate).
- [ ] Genetic constructs, CRISPR guides, si/shRNA, or overexpression systems are identifiable and target engagement is verified.
- [ ] Primary cells/organoids/PDX models retain donor/model provenance and are not treated as independent when derived from one source.

## F. Perturbation and Controls

- [ ] Perturbation target and method are explicit.
- [ ] Perturbation efficiency/target engagement is verified.
- [ ] Perturbation verification is separate from phenotype evidence.
- [ ] Appropriate negative/vehicle/non-targeting controls are present.
- [ ] Positive controls are included when needed to interpret assay performance.
- [ ] Generic toxicity/proliferation effects are considered when they could explain the phenotype.
- [ ] Ambiguous results have a predefined interpretation/redesign path rather than being forced into the preferred story.

## G. Mechanistic Specificity

- [ ] Strongest alternative mechanism is stated.
- [ ] At least one experiment/control directly addresses the most important alternative when required by the claim.
- [ ] Rescue/reversal is included when specificity or reversibility is central.
- [ ] Mediator/pathway dependency is tested when using mediation language.
- [ ] Epistasis/ordering is considered when the claim depends on pathway position.
- [ ] A single pharmacologic inhibitor is not treated as pathway proof without appropriate specificity evidence.

## H. Context Robustness and Generalization

- [ ] One cell line/model is not generalized to all breast cancer or all disease contexts.
- [ ] Subtype/lineage/genotype/treatment context is stated when relevant.
- [ ] A second model is used when it tests a meaningful boundary rather than merely repeating the first model.
- [ ] Negative/context-dependent findings remain visible.
- [ ] Generalization is limited to the actual models and conditions tested.

## I. In Vivo Evidence

- [ ] Animal work is included only when it answers a defined unresolved question.
- [ ] Experimental unit is correct and repeated measurements are not treated as independent animals.
- [ ] Model relevance and limitations are stated.
- [ ] In vitro success is not assumed to predict in vivo success.
- [ ] Animal evidence is not described as clinical efficacy.

## J. Human / Translational Bridge

- [ ] Human tissue/cohort analysis tests a defined bridge rather than serving as decorative validation.
- [ ] Patient is treated as the inferential unit where appropriate.
- [ ] Multiple ROIs/cells from one patient are not treated as independent patients.
- [ ] Prognostic, predictive, pharmacodynamic, and target-nomination claims are distinguished.
- [ ] Clinical association does not replace functional mechanism evidence.
- [ ] Mechanistic evidence does not replace clinical-performance validation.

## K. Omics / Single-Cell

- [ ] Discovery and validation are separated.
- [ ] High-dimensional multiplicity/FDR is addressed.
- [ ] Batch effects and repeated specimens are handled.
- [ ] Patient/sample-level inference is not replaced by cell-count significance.
- [ ] Pathway enrichment is not described as causal proof.
- [ ] Computational findings connect to a defined experimental validation route.

## L. Figure Story

- [ ] Each main figure has one dominant claim or one coherent higher-level claim.
- [ ] Every panel has a defined inferential role.
- [ ] Anchor/decisive panel is identifiable.
- [ ] Main vs supplement placement reflects inference value.
- [ ] Required controls, negative evidence, and failure boundaries are not hidden for narrative convenience.
- [ ] Figure sequence escalates the scientific question.
- [ ] Legend reports independent `n`, replicate type, statistics, and encodings.

## M. Manuscript Alignment

- [ ] Title states no stronger claim than the data support.
- [ ] Abstract claim strength matches the Results evidence.
- [ ] Introduction motivates the question without previewing unsupported mechanism.
- [ ] Methods permit reproduction and define experimental units/replicates.
- [ ] Results separate observation from interpretation.
- [ ] Discussion distinguishes direct finding, mechanistic interpretation, and hypothesis.
- [ ] Limitations identify model/context boundaries and unresolved alternatives.
- [ ] Conclusion does not upgrade preclinical evidence to clinical readiness.


## N. Animal-Study Rigor (when applicable)

- [ ] Ethics/animal-care approval and relevant institutional framework are reported.
- [ ] Species, strain/background, sex, age/developmental stage, source, housing-relevant factors, and health status are reported as needed.
- [ ] Experimental unit (animal vs cage/litter/other) is explicit.
- [ ] Allocation/randomization and blinding are reported or justified as not feasible.
- [ ] Sample-size rationale, humane endpoints, attrition/exclusions, and reasons are reported.
- [ ] Repeated tumor/physiologic measurements are analyzed as repeated observations within animal, not independent animals.
- [ ] ARRIVE 2.0 Essential 10 is checked for in vivo animal studies; use the Recommended Set when relevant.

## O. Image / Blot / Source-Data Integrity

- [ ] Representative images are selected by a stated, non-cherry-picked rule and are consistent with quantified data.
- [ ] Scale bars, acquisition settings, and image-processing/normalization are reported where relevant.
- [ ] Image adjustments are applied consistently and do not alter interpretation.
- [ ] Cropping/splicing of gels/blots is transparent; uncropped/source data are retained and supplied when required.
- [ ] Quantification is linked to the correct biological replicate rather than only the displayed representative image.
- [ ] Automated image analysis/segmentation has validation or QC sufficient for the claim.

## P. Ethics, Data, Code, and Materials Availability

- [ ] Human specimens have IRB/ethics/consent or waiver information when applicable.
- [ ] Sensitive human data are de-identified and access restrictions are stated appropriately.
- [ ] Omics datasets have accession/deposition plans or a justified controlled-access route.
- [ ] Analysis code and key parameters are versioned/available as appropriate.
- [ ] Critical materials/constructs/reagents have a realistic availability statement.
- [ ] Source data needed to verify central figures are retained and organized.

## Q. Final Sign-Off

- [ ] `chatgpt/actions/audit-mechanism.md` completed for central claims.
- [ ] Claim-evidence matrix has no unresolved central claim/evidence mismatch.
- [ ] Citation and number gates pass.
- [ ] Figure/text/legend claims agree.
- [ ] All unresolved scientific blockers are stated rather than smoothed over with prose.
