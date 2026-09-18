> Action purpose: claim에 맞는 verified `[EVID:id]` 출처 제안

**언제 사용:** Phase 3 claim→citation mapping / Phase 4 drafting에서 근거가 필요한 주장.

`docs/citation_assist_protocol.md` Operation 1을 따른다.

1. **기존 근거 우선:** `knowledge/evidence.md`에서 claim과 일치하는 verified entry를 찾는다.
2. **부족하면 PubMed 검색:** `chatgpt/actions/search-evidence.md` 또는 `python3 scripts/search_pubmed.py search "<claim terms>"`.
3. **Optional domain-matched backend:** 현재 주제가 실제 해당 도메인일 때만 추가 retrieval/KAG를 사용한다. Bundled `medical-kag`는 spine-specific이므로 breast/basic 연구의 primary route가 아니다.
4. **등록 후 인용:** 새 후보는 PMID/DOI/source를 확인하고 `[EVID:author_year]`로 `knowledge/evidence.md`에 등록한다.
5. **출력:** 후보 `[EVID:id]` + 각 1줄 근거(방향·대상/모델·중재/노출·결과). 자동 삽입하지 않는다.
