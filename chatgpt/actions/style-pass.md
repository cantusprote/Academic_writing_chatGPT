# Style Pass Action

**When to use:** Phase 5 or revision when the user asks to make a section more academic, concise, journal-like, or consistent with a chosen exemplar.

Follow `docs/style_transform_protocol.md`. There is **no automatic hook** in the ChatGPT workflow.

Target: **[user-specified section(s)]**

1. Confirm `drafts/style_spec.md`; if missing, select an exemplar from `Style/own/` or `Style/target_journal/` with the user when needed, then create the spec from `docs/style_spec_template.md`.
2. Load the target section, Style Spec, relevant exemplar notes, `Style/terminology.md`, and section rules in `docs/writing_guide.md`.
3. Transform section-by-section without changing grounded claims or numerical results.
4. Run `python3 scripts/check_style.py check <section> --spec drafts/style_spec.md` plus the Style-Conformance semantic verifier.
5. Fix and re-verify up to 2 times, then record the style gate with provenance if PASS.
