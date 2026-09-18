> Action purpose: 초안의 각 `[EVID:id]` 문장을 registered evidence/source와 대조해 claim-support 리포트를 만든다.

**언제 사용:** Phase 6 QC 또는 중요한 literature claim 검증.

`docs/citation_assist_protocol.md` Operation 2를 따른다.

1. `python3 scripts/extract_claims.py <section> --json`으로 cited claim을 추출한다.
2. 각 `[EVID:id]`에 대해 `knowledge/evidence.md`와 필요 시 검증된 source paper/abstract/full text를 회수한다.
3. `docs/verifier_prompt_templates.md` Semantic-Citation Verifier로 `SUPPORTED / PARTIAL / UNSUPPORTED / NOT_ENOUGH_INFORMATION`을 판정한다.
4. `review/claim_verification.md`에 `위치 | claim | [EVID:id] | 판정 | 조치`를 기록한다.
5. Optional domain-matched retrieval/KAG는 보조 수단일 뿐이며 없어도 검증을 수행한다.
