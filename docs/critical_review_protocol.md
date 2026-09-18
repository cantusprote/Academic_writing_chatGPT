# Critical-Review Protocol (외부 멀티모델 적대적 검토)

> 완성된 원고/response를 여러 리뷰어가 적대적으로 공격해 허점을 발굴하는 절차의 단일 기준. `chatgpt/actions/critical-review.md`와 `qc_guide.md`는 이 문서를 참조한다. QC Round 6 Critical Review의 독립/멀티모델 강화판.
> 공개 운영 기준은 이 문서가 원본입니다. 내부 설계 노트 경로는 런타임 의존성으로 두지 않습니다.

## 0. 원칙

- **review-only** — 허점을 발굴만 하고 자동 수정하지 않는다.
- **합의도 = 신뢰도** — 여러 리뷰어가 같은 허점을 지적하면 거의 확실한 약점.
- **기본/폴백** — ChatGPT main agent가 review를 조정하고 sSb/mSb independent reviewer를 우선 사용한다. 외부 reviewer가 없어도 workflow는 계속된다.

## 1. 절차

```
1. 대상 결정    기본 전체 원고 / 지정 부분 / revision: response letter + 원고
2. 리뷰어 선택 — ChatGPT higher-reasoning review를 기본으로 하고, 필요하면 sSb/mSb independent reviewer와 `critical_review.py`가 지원하는 OpenRouter 모델을 추가한다. 최소 1개
3. 병렬 공격
     - ChatGPT/Shellby independent reviewer → frozen artifact를 read-only로 검토
     - OpenRouter → python3 scripts/critical_review.py --target <file>
                    --models-file scripts/critical_models.txt --role <role>
                    --out review/critical/<run>/
4. 종합(메인)   중복 통합(합의도) + 심각도 분류(Critical/Important/Minor)
5. 저장         review/critical/YYYYMMDD_<slug>.md (통합 리포트) + 모델별 원본
```

## 2. 적대 프롬프트 (대상별)

프롬프트 본문은 `scripts/critical_prompts/<role>.txt`에 **단일 정본**으로 둔다 (`manuscript.txt`, `response.txt`). ChatGPT/Shellby review와 optional external reviewers 모두 이 파일을 출처로 쓴다. 프롬프트를 바꾸려면 이 파일만 수정한다.

- `manuscript.txt` — 원고를 적대적으로 공격 (overclaiming·방법론·논리 비약·일반화·재현성).
- `response.txt` — reviewer rebuttal 검토 (만족 여부·재반박 지점).
- `editor.txt` — **editor desk-screen** (§5).

(스크립트: `--role manuscript|response|editor`로 해당 파일 선택. independent reviewer에게도 같은 `.txt` 본문을 기준으로 제공한다.)

## 3. 종합 — 합의도 × 심각도

통합 리포트는 각 허점을 **심각도(Critical/Important/Minor)** 와 **합의도(몇 명의 리뷰어가 지적했는지)** 로 정렬한다. 여러 리뷰어가 동의한 허점을 위로. 단독 지적은 "다양성 참고"로 표기.

## 4. 에러 / 폴백

| 상황 | 처리 |
|------|------|
| `OPENROUTER_API_KEY` 없음 | OpenRouter만 skip, 나머지 리뷰어로 진행 + 알림 |
| 특정 모델 실패 | 그 모델만 skip (스크립트가 처리), 나머지 계속 |
| 리뷰어 0개 | 에러(최소 1개 필요) |

## 5. Editorial desk-screen (`editor` role; ask ChatGPT for an editor review)

기계적 QC·reviewer 적대 검토를 넘어 **편집장·임상 관점의 실질 평가**다: *이 논문이 임상적으로 타당한가, 분야 high-impact 저널 scope에 맞는가, 무엇을 추가해야 경쟁력이 생기는가, 안 되면 어느 하위 저널이 현실적인가.* 저자가 정한 target 저널이 아니라 **논문 주제 분야를 식별해 그 분야 high-impact 저널의 실제 게재물**을 기준으로 벤치마크한다(상위 tier 기준 = 의도적으로 높은 bar).

- **정본 프롬프트:** `scripts/critical_prompts/editor.txt` (5단계: 분야·벤치마크 식별 → 임상타당성 → scope/novelty → 방법·분석 적절성 → WHAT TO ADD + desk-screen 판정).
- **판정:** `SEND FOR PEER REVIEW` / `BORDERLINE` / `DESK REJECT` (at high-impact tier). DESK REJECT면 현실적 하위·specialty 저널을 근거와 함께 추천.
- **실행 — ChatGPT natural-language `critical-review` action**:
  - Shellby independent review = sSb/mSb fresh-context reviewer (가능한 경우).
  - OpenRouter = `python3 scripts/critical_review.py --target <file> --role editor --models <…>`.
  - 즉 모델 풀·선택 방식은 §1·§2의 reviewer 검토와 같고, 프롬프트만 `editor.txt`다.
- **벤치마크 강화(선택):** `knowledge/evidence.md`와 PubMed/search를 기본으로 해당 분야 high-impact 문헌을 확인한다. Bundled medical-kag는 spine-domain match일 때만 optional 보조로 사용한다; breast/basic oncology의 기본 벤치마크 도구로 사용하지 않는다.
- **성격:** grounded 게이트가 **아니라** 판정형 평가(임상·분야 지식 사용). **advisory** — 게이트를 대체하지 않는다. 수치·인용 grounding은 여전히 `check_numbers`/`check_citations` 담당. Phase 6에서 사용.
- 에러·폴백은 §4와 동일.
