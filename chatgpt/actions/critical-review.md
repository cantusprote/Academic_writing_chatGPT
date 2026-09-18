# Critical Review Action

**When to use:** after drafting, especially Phase 6 QC or Phase 8 revision, for adversarial senior-reviewer critique.

Follow `docs/critical_review_protocol.md`.

Target: **[user-specified file(s), or full manuscript]**

1. Freeze the target artifact(s) for the review pass.
2. Run one strong ChatGPT review using the canonical prompt under `scripts/critical_prompts/`.
3. When useful, obtain independent review from fresh Shellby subagent/reviewer contexts.
4. Optional OpenRouter reviewers can be called with `scripts/critical_review.py` if credentials are available. An optional external Claude CLI reviewer exists only as an upstream compatibility feature; it is never required.
5. Merge duplicate findings, classify severity (Critical / Important / Minor), and distinguish deterministic grounding problems from judgment-based editorial concerns.
6. Save the integrated report and any raw external-review outputs under `review/critical/`.
7. Do not record a manuscript gate PASS based only on this review; citation/number/gate checks remain separate and authoritative.
