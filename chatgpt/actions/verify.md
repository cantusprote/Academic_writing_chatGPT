# Verification Action

**When to use:** before recording a phase gate PASS, or whenever the user asks to verify a draft/result/revision.

Deterministic checks are run explicitly through sSb/mSb; there is no auto-hook.

Typical Phase 4 checks:

```bash
python3 scripts/check_citations.py drafts/05_results.md --evidence knowledge/evidence.md
python3 scripts/check_numbers.py drafts/05_results.md drafts/table_1.md --results results
python3 scripts/check_gate.py review/gates/phase_04_draft.GATE.md \
  --artifact drafts/05_results.md \
  --require-check constraint --require-check citation --require-check numbers --require-check logic \
  --verify-hash artifact=drafts/05_results.md \
  --cross-check citation=drafts/05_results.md \
  --cross-check numbers=drafts/05_results.md --results results
```

Or use the combined helper when appropriate:

```bash
python3 scripts/verify_all.py <artifacts> --results results --evidence knowledge/evidence.md [gate options]
```

After deterministic checks, run the semantic Constraint/Citation/Data/Logic verifier passes defined in `docs/verification_protocol.md`. Only then record `status: PASS` with provenance.
