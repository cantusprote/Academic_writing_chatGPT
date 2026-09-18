> Action purpose: 인용 출처가 claim을 지지/반박/언급하는지 분류하고 Discussion의 one-sided framing을 점검

**언제 사용:** Discussion 작성/QC.

`docs/citation_assist_protocol.md` Operation 3을 따른다.

1. claim과 `[EVID:id]`를 식별한다 (`extract_claims.py` 사용 가능).
2. registered evidence/source를 기준으로 각 citation을 **supporting / contrasting / mentioning**으로 분류한다.
3. 중요한/논쟁적 claim이면 PubMed에서 상반된 evidence를 추가 검색한다.
4. domain-matched optional conflict/KAG backend가 있으면 보조적으로 사용할 수 있으나 필수는 아니다.
5. material contrasting evidence가 존재하지만 정당한 이유 없이 빠져 있으면 **one-sided**로 flag한다.
