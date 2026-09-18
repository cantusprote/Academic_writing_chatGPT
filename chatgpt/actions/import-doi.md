> Action purpose: Import article by DOI and register in evidence.md


**When to use:** Phase 1, when you ALREADY have a DOI and want to register that specific paper into `knowledge/evidence.md` (no search needed).

# Import Article by DOI

DOI: **[user-specified target/options]**

## Instructions

### Step 1: Check evidence.md

Read `knowledge/evidence.md` to find the next reference number and check if this DOI is already registered.

### Step 2: Fetch Article

```bash
python3 scripts/search_pubmed.py doi [user-specified target/options] --format evidence --start-num <next_ref_num>
```

### Step 3: Complete & Register

1. Fill all [TODO] fields using the abstract
2. Update the PDF filename KEYWORD
3. Append to `knowledge/evidence.md` (before "## Pending References")
4. Update the Search Log: `| date | DOI: [user-specified target/options] | PubMed | 1건 | [N] registered |`

Follow `docs/evidence_guide.md` formatting rules. Never fabricate information.
