# Figure Story & Evidence Architecture Guide (Sim Custom v0.1.0)

> This guide owns **scientific figure architecture**. `docs/figure_guide.md` owns visual production, file format, resolution, plotting, and export.

## 1. Start With the Figure-Level Claim

For a basic/mechanistic manuscript, each main figure should normally carry one dominant scientific claim. This is a strong planning default, not a rigid journal rule.

Before choosing plots or panel count, write:

- Results-level question
- Figure-level dominant claim
- Evidence level
- What could overturn the claim?
- Decisive/anchor evidence
- Minimum panel set needed
- Claim boundary
- Question generated for the next figure

If a figure cannot be summarized in one clear sentence, consider splitting it, narrowing the claim, or moving supporting material to supplement.

---

## 2. Panel Inferential Roles

Assign every panel one primary role.

| Role | Question answered |
|---|---|
| setup / schematic | What system or contrast is being tested? |
| baseline characterization | Is the relevant factor/state present before perturbation? |
| primary evidence | Does the central effect exist? |
| perturbation verification | Did the intervention actually change the intended target? |
| phenotype evidence | Did the biological phenotype change? |
| control | Is a key alternative explanation excluded? |
| orthogonal confirmation | Is the result reproduced with another assay/modality? |
| rescue / reversal | Is specificity/reversibility supported? |
| epistasis / dependency | Does the proposed mediator/pathway lie in the required chain? |
| context robustness | Does the claim hold in another meaningful model/condition? |
| in vivo support | Does the phenomenon operate in organismal context? |
| human/translational bridge | Is the supported biology connected to human disease/use case? |
| boundary / failure case | Where does the claim weaken or stop generalizing? |

A panel should not silently perform three unrelated inferential jobs.

---

## 3. Necessity Test for Main-Figure Panels

For each panel ask:

1. What unique inference disappears if this panel is removed?
2. Does that inference establish, advance, qualify, or bound the figure-level claim?
3. Is this a distinct evidence role or only another visualization/metric of the same evidence?

Route panels accordingly:

- **Main figure:** decisive evidence, necessary control, claim-changing boundary, or central falsification.
- **Supplement:** reassurance, secondary metrics, expanded replicates/views, alternative estimators, non-central robustness.
- **Another main figure:** genuinely new major claim or the next rung of the paper's evidence escalation.
- **Merge/delete:** repeated view with little independent inference gain.

Do not hide a negative result in supplement when it materially changes the claim.

---

## 4. Figure-Level Template

Use this block in `drafts/story_map.md`:

```markdown
## Figure N — [working title]

**Scientific question:**

**Dominant claim:**

**Evidence level:**

**Anchor/decisive panel:**

| Panel | Experiment/analysis | Inferential role | Independent unit / n | Unique inference | Main/Supp |
|---|---|---|---|---|---|
| A | | | | | |
| B | | | | | |

**Strongest alternative explanation:**

**Control/falsifier:**

**Claim boundary:**

**Next question created:**
```

---

## 5. Evidence Escalation Across Figures

The figure sequence should normally deepen the scientific question.

A common basic/translational pattern is:

1. **Define/discover** the biological state or association.
2. **Confirm** it independently or orthogonally.
3. **Perturb** the candidate factor and establish functional contribution.
4. **Discriminate mechanism** with rescue/dependency/alternative controls.
5. **Test context robustness** in a meaningfully different model.
6. **Extend** to in vivo and/or human relevance when these answer unresolved questions.

This is not a fixed six-figure template. Skip steps that the claim does not require.

A later figure should normally answer a question created by the previous figure. If Figure 3 and Figure 4 can both be summarized as "X is associated with Y," the architecture probably has not escalated.

---

## 6. Typical Figure Archetypes

### Discovery → validation

`signal/state definition → independent confirmation → biological consequence`

### Perturbation → specificity

`perturbation design/verification → phenotype → rescue/dependency → alternative control`

### Mechanism → context

`proximal pathway → mediator test → phenotype consequence → contrasting model/boundary`

### Translational bridge

`preclinical mechanism → human concordance → patient-level association/use-case framing`

Do not treat a clinical association as proof that the mechanism is clinically actionable.

---

## 7. Figure and Results Must Share the Same Claim

For each main figure:

- figure title reflects the supported claim, not merely the method
- Results subsection asks the same scientific question
- Results text states the main inference without becoming a panel-by-panel caption
- legend defines experimental details, groups, independent `n`, summary statistics, tests, error bars, and abbreviations
- Discussion does not upgrade the claim beyond the figure's evidence level

The figure carries dense evidence; the main text carries the inference.

---

## 8. Statistics and Replication in Figures

Every biological figure should make it possible to identify:

- independent experimental unit
- biological vs technical replicates
- number of independent experiments/donors/animals/samples
- what points/bars/error bars represent
- statistical test/model and multiplicity handling when relevant

Do not use individual cells, fields, wells, or repeated measurements as independent `n` unless that is truly the randomized/independent unit.

When lower-level observations are shown, make the nesting transparent.

---

## 9. Story Audit

Before Results drafting, check:

- [ ] Can each main figure be summarized by one dominant claim?
- [ ] Does each panel add a distinct inference?
- [ ] Is the anchor panel obvious?
- [ ] Is perturbation verification separated from phenotype evidence?
- [ ] Are required controls/falsifiers visible?
- [ ] Is rescue/dependency included when specificity is central?
- [ ] Are context limits visible rather than generalized away?
- [ ] Does figure order escalate rather than repeat?
- [ ] Does the next figure answer the question created by the previous figure?
- [ ] Are main vs supplement decisions based on inference value, not aesthetics?

After the scientific architecture passes, use `docs/figure_guide.md` for plotting and export.
