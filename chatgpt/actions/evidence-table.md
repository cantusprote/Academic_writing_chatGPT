> Action purpose: verified literature를 구조화된 비교표로 정리

**언제 사용:** Discussion 비교 작성 또는 review supplement.

`docs/citation_assist_protocol.md` Operation 4를 따른다.

1. `knowledge/evidence.md`와 검증된 source paper에서 study/design/n/model or population/intervention/outcome/result/evidence level을 수집한다.
2. domain-matched optional extraction backend는 속도를 높이는 용도로만 사용하며, manuscript-facing 수치는 원문 대조한다.
3. `python3 scripts/evidence_table.py <records.json> --columns study,design,n,intervention,outcome,result,loe`로 표를 만든다.
4. `drafts/table_evidence.md` 또는 적절한 supplement에 저장한다.
