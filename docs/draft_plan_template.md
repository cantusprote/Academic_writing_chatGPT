# Draft Plan Template

> draft plan을 확정하기 전에 `paper-debate <논문 방향> planning`으로 ChatGPT main agent + optional sSb/mSb independent reviewer로 토론할 수 있다 (선택). 절차: `docs/debate_protocol.md`.

> Phase 3에서 이 파일을 복사하여 사용:
> `cp docs/draft_plan_template.md drafts/draft_plan.md`  (single paper)
> `cp docs/draft_plan_template.md drafts/paper1_xxx/draft_plan.md`  (multi-paper)
>
> **규칙:** 모든 항목 완결 후 사용자 승인 → Phase 4 진행
> **Basic/mechanistic conditional rule:** central contribution이 실험적 biology/mechanism이면 먼저 `chatgpt/actions/build-story-map.md`로 `drafts/story_map.md`를 만들고, 이 draft plan과 정렬시킨 뒤 승인받는다. `story_map.md`는 scientific architecture, `draft_plan.md`는 manuscript execution의 source of truth다.
> **권장 실행:** Phase 3는 논문 방향·논조·구성을 결정하는 핵심 단계이므로 ChatGPT에서 가능한 경우 **higher reasoning effort**를 사용한다.

---

## Step 0 — Socratic Brainstorming (작성 전 의도 정제)

> 아래 항목을 채우기 **전에**, 어시스턴트는 저자에게 **한 번에 하나씩** 질문하여 논문의 의도를 날카롭게 다듬는다.
> **규칙:** 질문은 한 개씩만 던지고, 저자의 답을 받은 **뒤에** 다음 질문으로 넘어간다 (한꺼번에 나열 금지).
> 예시 질문 (상황에 맞게 가감·재구성 가능) — ① 이 논문의 한 문장 핵심 메시지는? ② 독자가 기억해야 할 단 하나의 결과는? ③ 무엇이 새로운가 — 기존 연구와의 차별점은? ④ 회의적 심사자가 가장 먼저 공격할 지점은? ⑤ 이 결과로 바뀌는 임상·실무적 함의는?
>
> 수집된 답변의 용도:
> - **(a)** 아래 draft-plan 항목(1. Key Message, 2. Tone & Voice, 4. Evidence Gap, 8. Discussion Outline, 9. Limitation Points 등)을 직접 채우는 씨앗이 된다.
> - **(b)** 선택적 `paper-debate`의 **R0 준비 자료(prep material)**로 쓸 수 있다.
>
> **주의 (역할 구분):** 이 Step 0는 저자 의도를 끌어내는 **user-intake**이며, `paper-debate`와 **별개**다.
> `paper-debate`(`docs/debate_protocol.md`)는 ChatGPT + optional Shellby independent review이지 저자에게 묻는 절차가 아니다.
> 여기서 모은 답변은 이후 토론에 입력될 수 있는 **R0 입력값**일 뿐, 토론 프로토콜 자체의 일부는 아니다.

---

## 논문 기본 정보

- **논문 제목 (가안):**
- **목표 저널:**
- **원고 유형:** Original Article / Review / Letter / …
- **연구 설계:** RCT / Cohort / Cross-sectional / Case series / Meta-analysis / Basic/Mechanistic / Preclinical / …
- **Research mode:** Clinical / Translational / Basic-Mechanistic / Hybrid
- **질환/임상 setting (해당 시):** [breast cancer / other] — [early / neoadjuvant / adjuvant / metastatic / survivorship / other]
- **Subtype / biomarker context (해당 시):** [HR+/HER2− / HER2+ / TNBC / HER2-low / molecular or translational subgroup / other]
- **분석 대상/핵심 비교:** [population; intervention/exposure; comparator]
- **Reporting guideline:** [CONSORT 2025 / STROBE / REMARK / NeoSTEEP / STEEP 2.0 / PRISMA / other as applicable; 복수 선택 가능]
- **인용 형식:** `profile/journals.md` 확인 → [bracket / superscript / …], et al. after [N]명

### Endpoint Definitions (clinical/quantitative outcome studies as applicable)
| Endpoint | Role | Operational Definition | Time Origin / Assessment Time | Event / Censoring (if TTE) |
|---|---|---|---|---|
| [endpoint] | Primary/Secondary/Exploratory | [RECIST/pCR/RCB/STEEP/other as applicable] | [time zero or assessment schedule] | [event/censoring] |

### Basic / Mechanistic Story Alignment (해당 시)

> `docs/basic_research_guide.md`, `docs/basic_research_analysis_guide.md`, `docs/experimental_evidence_guide.md`, `docs/figure_story_guide.md`와 `drafts/story_map.md`를 사용한다.

- **Central biological question:**
- **Desired main claim:**
- **Current evidence level:**
- **Claim boundary / non-claim:**
- **Weakest evidence link:**
- **Independent experimental unit:**
- **Biological replicate definition:**
- **Technical replicate / nested subsample hierarchy:**
- **Primary validation route:** [necessary / recommended / optional 구분]
- **Allocation/randomization or blocking:** [applicable / not applicable + rationale]
- **Blinding/masking:** [applicable / not feasible + rationale]
- **Sample-size rationale:**
- **Predefined exclusion / QC rules:**
- **Important batch/block factors:**
- **Model/reagent identity & authentication:** [cell-line authentication/mycoplasma/construct/antibody/etc. when relevant]

---

## 1. Key Message

> 이 논문의 핵심 메시지 (1–2문장). 독자가 논문을 읽고 나서 기억해야 할 것.

[작성]

---

## 2. Tone & Voice

> 전체 원고에서 일관되게 유지할 논조·어조 선택.

- [ ] Conservative & evidence-based (기존 결과와 비교, 신중한 해석)
- [ ] Novel technique 강조 (처음 시도, 독창성 강조)
- [ ] 기존 방법과 동등성 주장 (non-inferiority / equivalence)
- [ ] Superiority 주장 (명확한 우월성 데이터 있을 때)
- [ ] 기타: [직접 기술]

**세부 설정:** [어떤 톤으로 어떤 주장을 어떻게 표현할지 1–3문장]

---

## 2A. Terminology Decisions

> `Style/terminology.md`를 확인하고, 이 논문에서 사용할 핵심 용어를 사전에 확정한다.
> 예외적으로 forbidden/default-preferred와 다른 용어를 써야 하면 이유를 기록한다.

| Concept | Term to Use | First Definition | Exception/Reason |
|---|---|---|---|
| Main intervention/exposure | | | |
| Comparator/control | | | |
| Primary outcome | | | |
| Key complication/safety term | | | |
| Study design term | | | |

---

## 3. Essential References

> evidence.md에서 선별한 필수 인용 참고문헌 + 각각의 인용 목적.
> 아직 evidence.md에 없는 것은 4번(Evidence gap)에 기재.

| # | Author Year | 인용 목적 |
|---|-------------|-----------|
| 1 | | Background — |
| 2 | | Background — |
| 3 | | Methods 근거 — |
| 4 | | 비교 대상 — |
| 5 | | 비교 대상 — |
| … | | |

---

## 4. Evidence Gap

> 추가로 필요한 근거 자료 (아직 evidence.md에 없는 것).
> 검색 후 evidence.md에 등록 후 Phase 4 진행.

- [ ] 검색 필요 주제: [키워드 or 필요한 논문 유형]
- [ ] 검색 필요 주제: [키워드 or 필요한 논문 유형]

---

## 5. Claim → Citation Mapping

> 핵심 주장(claim) ~20개와 그 근거 논문 매핑.
> **규칙:** claim을 작성하기 전에 citation을 먼저 확보할 것.
> 없으면 Phase 1로 돌아가 검색.
> Style/own/에서 본인 논문 스타일 앵커도 확인.
> **인용 형식:** citation은 `[EVID:author_year]` 태그로 적는다 (evidence.md id와 일치). 존재하지 않는 id는 게이트에서 차단된다.

### Introduction Background (5–8 claims)

| # | Claim (1문장 요약) | Citation (Author Year) |
|---|------------------|----------------------|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |
| 6 | | |

### Methods Rationale (2–3 claims)

| # | Claim | Citation |
|---|-------|---------|
| 1 | | |
| 2 | | |
| 3 | | |

### Discussion Comparisons (5–8 claims)

| # | Claim (선행연구와 비교) | Citation |
|---|----------------------|---------|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |

---

## 6. Table / Figure Plan

> 몇 개, 각각 어떤 내용, Table vs Figure 결정.
> 원칙: 동일 데이터를 Table과 Figure 모두에 제시하지 않음.
> Oncology/translational 연구에서는 해당되는 경우 patient flow, treatment/exposure, efficacy, safety, survival, subgroup/interaction, pathology response, biomarker/ctDNA dynamics를 미리 배치한다. 모든 항목을 기계적으로 포함하지 말고 연구 질문에 필요한 것만 선택한다.

| # | 제목 (가안) | 형식 | 내용 요약 |
|---|-------------|------|-----------|
| Table 1 | Baseline Characteristics | Table | Demographics, 기저치 비교 |
| Table 2 | | Table / Figure | |
| Table 3 | | Table / Figure | |
| Fig 1 | | Figure | |
| Fig 2 | | Figure | |
| Supp Table 1 | | Supplementary | |

**Oncology/translational candidates (해당 시):** patient flow; baseline disease/tumor characteristics; treatment exposure/discontinuation; RECIST waterfall/swimmer; pCR/RCB distribution; Kaplan–Meier or cumulative-incidence curves; subgroup/biomarker interaction forest plot; longitudinal ctDNA/biomarker dynamics with sampling times and evaluable denominators; safety with denominator/grading framework.

### Basic / Mechanistic Figure Story (해당 시)

> 단순 figure inventory가 아니라 `drafts/story_map.md`의 claim architecture와 동일해야 한다. 각 main figure는 보통 하나의 dominant claim을 담당한다.

| Figure | Scientific Question | Dominant Claim | Evidence Level | Anchor Panel | Required Control/Falsifier | Next Question |
|---|---|---|---|---|---|---|
| Fig 1 | | | | | | |
| Fig 2 | | | | | | |

Panel별 inferential role과 main-vs-supplement 판단은 `docs/figure_story_guide.md`를 따른다.

---

## 7. Introduction Outline

> Background → Gap → Purpose 흐름. 각 단락 1–2문장 요약.

**Paragraph 1 (Background — broad context):**
[인구집단/질환 소개; 유병률·임상적 중요성]

**Paragraph 2 (Background — current treatment):**
[현재 표준 치료; 기존 방법의 문제점]

**Paragraph 3 (Gap):**
[무엇이 아직 불확실한가; 기존 연구의 한계]

**Paragraph 4 (Purpose):**
[이 연구의 목적; 가설]

---

## 8. Discussion Outline

> 주요 논점 3–5개, 각각 비교할 선행연구 목록.

**논점 1 — 주요 결과 해석:**
[핵심 결과 요약 → 선행연구와 비교] → 참고: [Author Year]

**논점 2 — 이차 결과 또는 subgroup:**
[해석 → 비교] → 참고: [Author Year]

**논점 3 — 임상적 의의:**
[실제 진료에 미치는 영향]

**논점 4 — 한계점 대응:**
[아래 9번의 Limitation과 연결]

**논점 5 — 미래 방향 (선택):**
[추가 연구 필요 사항]

---

## 9. Limitation Points

> 예상 한계점과 각각에 대한 대응 논리.

| 한계점 | 대응 논리 |
|--------|-----------|
| | |
| | |
| | |

---

## 10. Target Word Count

> 저널 기준에 맞춘 섹션별 목표 분량. `profile/journals.md` 또는 저널 IFA 확인.

| 섹션 | 저널 제한 | 목표 |
|------|-----------|------|
| Abstract | ≤ words | words |
| Introduction | — | ~400 words |
| Methods | — | ~800 words |
| Results | — | ~600 words |
| Discussion | — | ~800 words |
| Conclusion | — | ~150 words |
| **Total body** | ≤ words | words |
| References | ≤ N | N |
| Tables | ≤ N | N |
| Figures | ≤ N | N |

---

## 승인 체크리스트 (Phase 4 진행 전 확인)

- [ ] 1. Key message — 명확한 1–2문장
- [ ] 2. Tone & voice — 선택 완료
- [ ] 3. Essential references — evidence.md에 등록됨
- [ ] 4. Evidence gap — 추가 검색 완료 또는 필요 없음 확인
- [ ] 5. Claim→Citation mapping — ~20개 claim에 citation 모두 확보 (`[EVID:id]` 형식, evidence.md 존재 확인)
- [ ] 6. Table/Figure plan — 개수·형식·내용 결정
- [ ] 질환 setting/subtype, endpoint operational definitions, reporting guideline 선택 완료
- [ ] **Basic/mechanistic 해당 시:** `drafts/story_map.md` 승인, claim boundary·experimental unit·validation route·figure dominant claim 정렬 완료
- [ ] **Basic/mechanistic 해당 시:** `chatgpt/actions/audit-mechanism.md` Phase 3 audit PASS
- [ ] 7. Introduction outline — 단락별 흐름 설계
- [ ] 8. Discussion outline — 논점 3–5개 + 비교 대상 확정
- [ ] 9. Limitation points — 대응 논리 포함
- [ ] 10. Target word count — 저널 기준 확인
- [ ] 사용자 승인 완료 → **Phase 4 시작**
