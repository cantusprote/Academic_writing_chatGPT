# Action — Build Basic/Mechanistic Story Map

Use this playbook when the user asks to build the story, figure story, mechanism paper structure, claim architecture, or basic-research manuscript plan.

## Purpose

Create the paper-specific story map, the source of truth for the scientific architecture of a basic/mechanistic paper.

- Single paper: `drafts/story_map.md`
- Multi-paper: `drafts/paper{N}_xxx/story_map.md` beside that paper's `draft_plan.md`

Do not write full manuscript prose before the story map and `drafts/draft_plan.md` are aligned and approved.

## Read First

1. `CHATGPT.md`
2. `docs/basic_research_guide.md`
3. `docs/basic_research_analysis_guide.md`
4. `docs/experimental_evidence_guide.md`
5. `docs/figure_story_guide.md`
6. `docs/basic_research_checklist.md`
7. existing `drafts/draft_plan.md` if present
8. the matching `data/analysis_plan.md` if present
9. available figure legends/results/analysis notes
10. `knowledge/evidence.md` only for literature-backed contextual claims

Use sSb for Mac Studio files and mSb for MacBook/local files. No auto-hook is assumed.

## Build Sequence

### 1. Establish the North Star

Write one sentence each for:
- biological problem
- central scientific question
- desired main claim
- contribution type
- boundary conditions

If the desired main claim cannot be stated accurately in one sentence, do not force a figure plan. Identify the ambiguity first.

### 2. Separate Confirmed / Assumed / Unresolved

Classify each important premise or result:
- **Confirmed** — directly supported by supplied data/results
- **Assumed** — plausible but not yet verified
- **Unresolved** — missing, conflicting, or ambiguous

Never promote Assumed to Confirmed to make the story cleaner.

### 3. Build the Claim Architecture

Use stable claim IDs.

```text
Main Claim
├── C1 — [claim]
│   └── evidence / figure
├── C2 — [claim]
│   └── evidence / figure
└── boundary / unresolved points
```

For each claim specify:
- exact wording
- claim class
- achieved evidence level
- evidence source
- weakest link
- strongest alternative explanation
- claim boundary

### 4. Design the Validation Route

For each weakest link decide whether the next useful layer is:
- association reinforcement
- orthogonal confirmation
- functional perturbation
- mechanistic specificity/rescue
- context robustness
- in vivo support
- human/translational bridge

Label each proposed step **necessary**, **recommended**, or **optional**. Do not prescribe a maximal validation stack.

### 5. Build the Figure Sequence

For each proposed main figure define:
- scientific question
- dominant claim
- evidence level
- anchor/decisive panel
- panel inferential roles
- control/falsifier
- claim boundary
- next question generated

Use `docs/figure_story_guide.md`.

### 6. Define Experimental Units

For every central experiment state:
- independent experimental unit
- biological replicate definition
- technical replicate/subsample hierarchy
- main statistical comparison/model if already determined
- allocation/randomization or blocking plan when applicable
- blinding/masking when applicable
- sample-size rationale
- predefined exclusion/QC rules
- important batch/block factors
- model/reagent identity and authentication requirements when relevant

Flag pseudo-replication and avoidable rigor risks explicitly.

### 7. Generate the paper-specific `story_map.md`

Use this structure:

```markdown
# Story Map

## North Star
- Biological problem:
- Central question:
- Desired main claim:
- Contribution:
- Boundary:

## Confirmed / Assumed / Unresolved

## Claim Architecture

## Claim-Evidence Matrix

## Validation Route

## Figure Story

## Experimental Unit / Replicate Map

## Experimental Rigor / Reproducibility Map

Record, when applicable:
- allocation/randomization or blocking
- blinding/masking
- sample-size rationale
- predefined exclusion/QC rules
- important batch/block factors
- model/cell-line identity, authentication, and mycoplasma status
- critical reagent/construct provenance
- animal-study ARRIVE items
- image/blot/source-data integrity plan

## Results Subsection Order

## Translational Bridge (if applicable)

## Scientific Blockers / Open Decisions
```

For substantial projects, also write the claim matrix to `review/claim_evidence_matrix.md` (multi-paper: the matching `review/paper{N}_xxx/claim_evidence_matrix.md`).

### 8. Alignment Check

Compare the resulting story map with `drafts/draft_plan.md` if it exists.

Flag and resolve mismatches in:
- key message
- claim strength
- figure order
- limitation/boundary
- terminology
- translational framing

## Hard Rules

- Do not invent experiments, results, figures, citations, or effect sizes.
- Do not turn association into function or mechanism.
- Do not make animal or human validation mandatory by default.
- Do not use technical replicates as biological `n`.
- Do not organize figures by experiment chronology when a claim-driven order is clearer.
- Do not begin full drafting until the user approves the story map and draft plan.

## Completion

Report:
- resolved paper-specific story-map path
- main claim
- number of main claim nodes
- proposed main figures
- weakest evidence link(s)
- unresolved blockers requiring author decision
