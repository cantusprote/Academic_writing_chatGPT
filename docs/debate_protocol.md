# Debate Protocol (ChatGPT + Shellby Co-Author Review)

> 논문 작성의 사고 단계에서 **ChatGPT main agent**가 방향을 세우고, 필요할 때 **sSb/mSb의 독립 subagent 또는 second-model review**를 추가해 반론·대안을 검토한다. 토론은 선택적 품질 보조이며 실패해도 워크플로를 막지 않는다.

## 1. 기본 흐름

R0에서 ChatGPT main agent가 주제, 제약, 현재 근거를 바탕으로 접근법과 쟁점을 정리한다. R1에서 독립 검토가 가치가 있으면 sSb/mSb를 통해 fresh-context subagent 또는 사용 가능한 second-model reviewer에게 **read-only 의견**을 요청한다. R2에서는 main agent가 반론을 비교하고 수정안을 만든 뒤, 남은 핵심 불일치가 있으면 한 차례 추가 독립 검토를 수행한다. 최대 3라운드 후에도 중요한 불일치가 남으면 차이점과 근거를 사용자에게 제시해 결정받는다.

독립 reviewer는 파일을 수정하지 않고 의견만 제시한다. 동일한 산출물을 여러 reviewer에게 줄 때는 고정된 snapshot을 사용한다. reviewer 실패·도구 부재·빈 출력은 해당 reviewer를 건너뛰고 ChatGPT main agent가 계속 진행한다.

## 2. 단계별 reviewer 역할

| Mode | Independent reviewer focus | Main-agent synthesis |
|---|---|---|
| planning | novelty, scope, alternative structure, missing evidence | research question and manuscript architecture |
| stats | estimand, endpoint, censoring, model, multiplicity, bias, sensitivity | analysis strategy consistent with oncology protocol/SAP |
| revision | reviewer intent, defensible response options, manuscript impact | response strategy and exact revision plan |
| interpretation | competing explanations, overclaiming, external validity | calibrated Discussion/conclusion |

## 3. Shellby 실행

사용자가 “paper-debate …”라고 자연어로 요청하거나 main agent가 독립 검토가 유용하다고 판단하면, ChatGPT는 현재 Mac에 연결된 **sSb 또는 mSb**를 사용한다. reviewer에게는 주제, source-of-truth 파일, main-agent position, 검토 역할, 그리고 “read-only: 의견만 제시, 파일 수정 금지”를 전달한다. Shellby에서 subagent/second-model 기능을 사용할 수 없으면 별도 모델 토론을 필수로 만들지 않는다.

```text
Role: {ROLE}
Topic: {TOPIC}
Main-agent position:
{MAIN_POSITION}

Focus:
{FOCUS}

Independently challenge the position using only the supplied sources.
Identify concrete errors, missing alternatives, and decision-changing uncertainties.
Read-only: provide review only; do not modify files.
```

## 4. 수렴 판정

main agent는 사실/근거 충돌, 분석·논리 충돌, 단순 표현 차이를 구분한다. source-of-truth로 해결되지 않는 중요한 선택은 임의로 합의 처리하지 않는다. Oncology endpoint, estimand, biomarker interaction, causal bias처럼 결론을 바꿀 수 있는 쟁점은 명시적으로 남긴다.

## 5. 기록

토론 자체는 gate가 아니다. 결정이 draft plan, analysis plan, manuscript, 또는 revision response를 바꾸면 해당 산출물에 결정과 근거를 반영하고 정상 verification gate를 다시 수행한다.
