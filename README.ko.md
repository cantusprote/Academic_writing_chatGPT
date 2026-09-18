# ChatGPT + Shellby 의학논문 작성 워크플로

**ChatGPT가 sSb/mSb를 통해 Mac의 실제 파일을 직접 다루는** 유방암 임상·중개연구 논문 작성 시스템입니다.

- Mac Studio 파일 작업: **sSb**
- MacBook 파일 작업: **mSb**
- 핵심 규칙: **`CHATGPT.md`**
- Upstream 기준: `grotyx/Academic_writing_c_claudecode` v1.6.3 (`e0527e2`)
- 현재 커스텀 버전: **Sim Oncology ChatGPT v0.2.0**

## 어떻게 쓰나

별도 CLI나 slash command를 직접 사용할 필요가 없습니다. ChatGPT에 자연어로 요청하면 됩니다.

| 사용자가 말하는 예 | ChatGPT가 하는 일 |
|---|---|
| `이 주제로 프로젝트 설정해줘` | `CHATGPT.md`를 읽고 연구 설정 |
| `관련 근거 찾아서 evidence에 등록해줘` | `chatgpt/actions/search-evidence.md` 수행 |
| `analysis plan 만들어줘` | `data/analysis_plan.md` 작성 후 승인 대기 |
| `이 plan대로 분석해` | 승인 확인 후 분석 실행 → `results/` 저장 |
| `draft plan 만들어줘` | `drafts/draft_plan.md` 작성 |
| `Methods 작성해` | 승인된 plan/evidence/results에 근거해 작성 |
| `전체 검증해` | citation/number/gate + semantic verifier 실행 |
| `oncology checklist 돌려` | `docs/oncology_checklist.md` 적용 |
| `critical review 해` | 독립 reviewer/멀티모델 비판적 검토 |
| `최종 DOCX 만들어줘` | `docs/docx_guide.md`에 따라 출력 |

## 기본 워크플로

1. **Setup / Evidence** — 연구 설정, PubMed/evidence 등록
2. **Analysis Plan** — `data/analysis_plan.md` 작성·승인
3. **Analysis** — `data/py/` 실행, 숫자의 정본은 `results/*.csv`
4. **Draft Plan** — `drafts/draft_plan.md` 작성·승인, claim→citation mapping 포함
5. **Draft** — Methods → Results → Introduction → Discussion → Conclusion → Abstract → Title
6. **Style / QC** — terminology, style, oncology checklist, verification gate
7. **Finalize** — reference format + DOCX
8. **Revision** — reviewer response와 실제 수정사항 교차검증

## ChatGPT에서 반드시 지킬 규칙

이 fork에는 자동 hook이 없습니다. 따라서 ChatGPT가 sSb/mSb를 통해 다음을 **명시적으로** 확인합니다.

- 승인된 `analysis_plan.md` 없이 분석하지 않기
- 승인된 `draft_plan.md` 없이 본문 작성하지 않기
- `knowledge/evidence.md`에 검증된 `[EVID:id]`만 인용하기
- 결과 숫자는 `results/*.csv`에서만 가져오기
- style/terminology lint 명시적으로 실행하기
- deterministic checker + semantic verifier + gate provenance를 직접 실행/기록하기
- PASS 후 파일이 바뀌면 이전 PASS를 stale로 보고 다시 검증하기

Analysis Plan, Draft Plan, Revision 전략, semantic verification처럼 중요한 판단 단계는 가능하면 **높은 reasoning effort**를 사용하고, 계획이 확정된 routine drafting은 normal reasoning으로 수행할 수 있습니다.

## 유방암 특화 부분

`docs/oncology_analysis_guide.md`가 generic 통계 규칙보다 우선합니다.

중심 순서:

`clinical question → estimand → analysis population → endpoint 정의 → time origin/event/censoring → model → effect estimate/CI → multiplicity → sensitivity analysis`

다루는 주요 영역:

- pCR / RCB
- EFS / IDFS / RFS / PFS / OS
- ORR / CBR / DoR / RECIST 1.1
- competing risks
- landmark / time-dependent analysis
- prognostic vs predictive biomarker / interaction
- ctDNA / MRD longitudinal analysis
- multiplicity / missing data / sensitivity analysis

## 중요한 파일

- `CHATGPT.md` — 전체 workflow의 source of truth
- `AGENTS.MD` — 시작용 핵심 요약
- `chatgpt/actions/` — 자연어 요청별 실행 playbook
- `docs/oncology_analysis_guide.md` — oncology 통계·방법론
- `docs/oncology_checklist.md` — oncology QC
- `Style/terminology.md` — 유방암 용어 registry
- `knowledge/evidence.md` — citation 정본
- `data/analysis_plan.md` — 분석 전 필수
- `drafts/draft_plan.md` — 원고 작성 전 필수
- `review/gates/` — verification 기록

## 권장 폴더 운영

이 폴더는 **master template**으로 유지하고 논문마다 복제해 사용합니다.

```text
/Users/sim/Dev/Academic_writing_chatGPT     # master template
/Users/sim/Dev/TNBC_AR                      # 실제 논문
/Users/sim/Dev/HER2_Heterogeneity           # 실제 논문
```

이후 ChatGPT에서 예를 들어

> `sSb로 TNBC_AR 프로젝트의 analysis plan 만들어줘.`

처럼 요청하면 됩니다.

## 테스트

```bash
.venv/bin/python -m pytest -q
```

## Git 안전 규칙

- `upstream`에는 push하지 않습니다.
- 사용자 저장소는 `origin`으로 둡니다.
- PDF, 개인 profile, private style anchor는 Git에 올리지 않습니다.

fork 배경과 upstream 차이는 `docs/customization.md`를 참고하세요.
