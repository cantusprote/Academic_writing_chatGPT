# Paper Debate Action

**When to use:** before a high-impact decision in Phase 2, 3, 4, or 8: analysis approach, key message, argument structure, or revision strategy.

Follow `docs/debate_protocol.md`.

Topic: **[user-specified topic]**

1. Read the relevant source-of-truth files (`analysis_plan.md`, `draft_plan.md`, evidence/results as applicable).
2. The main ChatGPT pass states a proposed approach and its reasons.
3. Obtain at least one **independent critique** when useful. Prefer a fresh Shellby subagent/reviewer context available through sSb/mSb. Optional external model review may be used only when available and useful.
4. Run bounded rounds (normally no more than 3), focusing on disagreements that could materially change the paper.
5. Record the final synthesis under `review/debates/` and use it to update the relevant plan/artifact.
6. If an independent reviewer is unavailable, perform a clearly separated second-pass critique in ChatGPT rather than blocking the workflow.

Do not use debate to bypass deterministic verification or user approval gates.
