# Academic Paper Writing Project — Sim Oncology ChatGPT (v0.3.0; upstream v1.6.3)

## Research Configuration
**Primary Domain:** Breast Medical Oncology / Translational & Mechanistic Research
**Topic:** [INSERT YOUR SPECIFIC RESEARCH TOPIC]
**Disease Setting:** [Early / Neoadjuvant / Adjuvant / Metastatic / Survivorship / Other]
**Subtype / Biomarker Context:** [HR+/HER2- / HER2+ / TNBC / HER2-low / biomarker-defined / pan-breast]
**Target Journal:** [INSERT TARGET JOURNAL]
**Study Design:** [RCT / Prospective Cohort / Retrospective Cohort / Biomarker / Translational / Basic/Mechanistic / Meta-analysis / etc.]

> ⚠️ Update this section for each new paper project

---

## Project Structure

### Single Paper Project (기본)
```
project/
├── CHATGPT.md                     # This file - core rules & config
├── AGENTS.MD                     # Agent bootstrap rules; points to CHATGPT.md as source of truth
├── .gitattributes                # Line-ending policy (text=auto eol=lf; prevents CRLF churn from OneDrive/Windows sync)
├── docs/                         # Reference guides (read when needed)
│   ├── writing_guide.md          # Section-by-section writing guide
│   ├── drafting_protocol.md      # Mandatory drafting sequence
│   ├── section_templates.md      # Section-specific sentence patterns
│   ├── expert_roles.md           # Expert team roles & responsibilities
│   ├── checklist_guide.md        # Study-type specific checklists (STROBE, CONSORT, etc.)
│   ├── qc_guide.md               # Quality control & consistency verification
│   ├── verification_protocol.md  # 검증 게이트·4 core Verifier + basic mechanism overlay·자율 루프·게이트 원장
│   ├── verifier_prompt_templates.md  # LLM semantic verifier prompts/output schema
│   ├── statistical_analysis_guide.md  # Generic statistical analysis guide
│   ├── oncology_analysis_guide.md     # Breast oncology endpoint/estimand/statistics override
│   ├── oncology_checklist.md          # Oncology-specific Phase 6 reporting/QC checklist
│   ├── basic_research_guide.md        # Basic/mechanistic claim→validation→story workflow
│   ├── basic_research_analysis_guide.md # Experimental unit/design/statistical override for basic research
│   ├── basic_section_templates.md     # Basic/mechanistic conditional manuscript structure
│   ├── basic_research_checklist.md    # Basic/mechanistic Phase 3/6 QC checklist
│   ├── experimental_evidence_guide.md # Claim strength, perturbation, rescue, evidence-boundary rules
│   ├── figure_story_guide.md          # One-claim-per-figure scientific evidence architecture
│   ├── evidence_guide.md         # Evidence 작성 가이드
│   ├── revision_guide.md        # Revision & reviewer response guide
│   ├── figure_guide.md          # Figure generation guide
│   ├── docx_guide.md            # DOCX 변환 가이드 (서식, 테이블, 네이밍)
│   ├── draft_plan_template.md    # Draft plan 10개 항목 템플릿 (Phase 3에서 복사)
│   ├── debate_protocol.md        # ChatGPT + independent reviewer 토론 절차
│   ├── critical_review_protocol.md  # 외부 멀티모델 적대적 검토 절차
│   ├── style_transform_protocol.md  # `chatgpt/actions/style-pass.md` action 변환 + Style Verifier
│   ├── style_spec_template.md    # Style Spec 템플릿 (exemplar 바인딩)
│   ├── citation_assist_protocol.md  # 출처 제안·claim 검증·stance·비교표 (evidence.md + PubMed-first; optional domain-matched retrieval)
│   └── medical_kag_protocol.md   # optional legacy spine-domain KAG integration; not primary for breast/basic
├── knowledge/                    # Reference materials
│   ├── evidence.md               # 참고문헌 요약 정리 자료집
│   ├── pdf/                      # Original PDF files
│   │   └── author_year_keyword.pdf
│   └── summaries/                # MD summaries of key papers
│       └── author_year_keyword.md
├── Style/                        # Writing-style anchors (separate from references)
│   ├── PDF/                      # Source PDFs for style analysis (gitignored)
│   │   ├── own/
│   │   ├── landmark/
│   │   └── target_journal/
│   ├── own/                      # Own-paper style extraction md
│   ├── landmark/                 # Argument/framing anchors
│   ├── target_journal/           # Journal house-style anchors
│   ├── style_guide.md            # Style anchor workflow and extraction rules
│   └── terminology.md            # Preferred/forbidden terminology registry
├── data/                         # Statistical analysis
│   ├── raw_data.csv              # Original dataset (CSV/XLSX)
│   ├── analysis_plan.md          # Analysis plan (required before analysis)
│   └── py/                       # Python analysis scripts
│       ├── 01_descriptive.py
│       ├── 02_comparative.py
│       └── 03_regression.py
├── results/                      # Analysis outputs
│   ├── table1_demographics.csv
│   ├── table2_outcomes.csv
│   └── statistics_summary.csv
├── drafts/                       # Manuscript sections & tables
│   ├── draft_plan.md            # Draft plan (required before drafting)
│   ├── story_map.md             # Basic/mechanistic scientific architecture (generated when applicable)
│   ├── _templates/              # Mode-specific draft skeletons
│   │   ├── basic_methods.md
│   │   └── basic_results.md
│   ├── 00_cover_letter.md       # Cover letter template
│   ├── 01_title.md ~ 09_figure_legends.md  # Writing guide templates
│   ├── table_*.md               # Table templates
│   └── figures/                 # Generated figures
├── scripts/                      # Utility scripts
│   ├── lint_manuscript.py        # Manuscript terminology/style lint checks
│   ├── check_citations.py        # Evidence citation gate
│   ├── check_numbers.py          # Results CSV number gate
│   ├── check_gate.py             # Phase gate ledger check
│   ├── check_revision_claims.py  # Revision claim gate
│   ├── compile_response_docx.py  # Author response DOCX compiler
│   ├── search_pubmed.py          # PubMed search tool (no external deps)
│   ├── check_style.py            # Style Spec 대비 측정형 게이트 (문장길이·인용밀도)
│   ├── extract_claims.py         # 초안의 [EVID:id] 문장 추출 (claim 검증 입력)
│   ├── evidence_table.py         # 구조화 study 레코드 → markdown 비교표
│   ├── critical_review.py        # OpenRouter 멀티모델 적대적 검토 호출
│   ├── critical_models.txt       # OpenRouter 모델 목록 (외부화)
│   ├── critical_prompts/         # 적대적 검토 프롬프트 (manuscript.txt, response.txt, editor.txt)
│   ├── verify_all.py             # `chatgpt/actions/verify.md` action — citation+number(+gate) 일괄 검증
│   ├── check_coverage.py         # 인용 coverage audit (과잉인용·미등록인용 주신호; 인용밀도; uncited는 중립)
│   ├── format_references.py       # [EVID:id]→저널형 서지목록 + 본문 태그 변환 (MCP 독립; Phase 7)
│   ├── check_abstract.py         # abstract↔본문 수치 일관성 (abstract-only 수치 차단; Phase 6, Rule 3)
│   ├── check_crossrefs.py        # Table/Figure 본문 참조 ↔ 실존 대조 (broken ref·미인용·순서; advisory)
│   ├── check_abbreviations.py    # 약어 첫 사용 정의 검사 (abstract/본문 scope 분리; advisory)
│   ├── check_response_coverage.py # 리뷰어 코멘트 전수 응답 확인 (Phase 8; ghost-revision 보완)
│   └── hooks/                    # upstream legacy hook scripts; ChatGPT workflow에서는 사용하지 않음
├── tests/                        # pytest suite for the verification scripts
│   └── test_*.py                 # Run: pytest  (python-docx required, see requirements.txt)
├── .github/workflows/tests.yml   # CI: pytest on push to main + PRs (Python 3.10/3.11/3.12)
├── review/                       # Review & QC documents
│   ├── qc_log.md                 # QC round tracking
│   ├── claim_evidence_matrix.md  # Generated for substantial basic/mechanistic projects
│   ├── mechanism_audit.md        # Phase 3/6 mechanism audit output when applicable
│   ├── gates/                    # 검증 게이트 원장 (phase_NN_*.GATE.md)
│   ├── debates/                  # ChatGPT–reviewer 토론 로그
│   └── critical/                 # 외부 멀티모델 적대적 검토 리포트
└── output/                       # Final compiled manuscript
    ├── title_page_YYMMDD.docx
    ├── manuscript_YYMMDD.docx
    └── table_N_YYMMDD.docx
```

### Multi-Paper Project (하나의 데이터에서 여러 논문 작성 시)

> 동일 데이터셋에서 여러 논문 작성 시 논문별 서브폴더로 정리 (상세 규칙: Rule 6).

기본(Single) 구조에서 **`data/`·`results/`·`drafts/`·`output/`·`review/` 각각에 `paper{N}_{keyword}/` 서브폴더**를 만들어 논문별로 분리한다. `docs/`·`knowledge/`·`scripts/`는 공유. 원본 데이터는 `data/` 루트, 논문별 필터링 데이터·`analysis_plan.md`·`draft_plan.md`는 각 서브폴더에 둔다.

**서브폴더 네이밍:** `paper{N}_{keyword}` (예: `paper1_infection`) — 저자 선호 이름 우선, keyword는 짧고 식별 가능하게.

### Revision 구조 (리뷰어 코멘트 수신 후)

> 각 논문 폴더 내 `revision/REV{N}/` 서브폴더로 정리 (상세 규칙: Rule 6).

- **`drafts/revision/REV{N}/`** — 수정된 섹션만 `_REV{N}` 접미사로 (예: `04_methods_REV1.md`) + `response_letter_REV{N}.md`
- **`review/`** — `reviewer_comments_REV{N}.md`, `gates/phase_08_revision.GATE.md`
- **`output/revision/REV{N}/`** — `manuscript_REV{N}_YYMMDD.docx`, 변경된 table, `response_letter_REV{N}_YYMMDD.docx`
- **Multi-paper:** 동일 구조가 각 `paper{N}_xxx/revision/REV{N}/`에 적용

---

## File Roles

| File/Folder | Purpose | When to Use |
|-------------|---------|-------------|
| `CHATGPT.md` | Core rules, project config, writing style | Read explicitly at task/session start |
| `.gitattributes` | Line-ending policy (`text=auto eol=lf`) — stores LF, normalizes on compare so OneDrive/Windows CRLF rewrites never produce content-free diffs | Git-managed (no manual edits needed) |
| `docs/writing_guide.md` | Detailed section guidelines | When drafting specific sections |
| `docs/drafting_protocol.md` | Mandatory outline → evidence-bound draft → style pass → QC workflow | Before drafting any section |
| `docs/section_templates.md` | Section-specific paragraph functions and sentence patterns | Phase 4 drafting |
| `docs/expert_roles.md` | Expert team descriptions | When drafting or reviewing (Phase 4-5) |
| `docs/checklist_guide.md` | Study-type checklists (STROBE, CONSORT, PRISMA, CARE) | Phase 6 (QC) and before submission |
| `docs/qc_guide.md` | Consistency & accuracy verification procedures | Phase 6 (QC rounds) |
| `docs/statistical_analysis_guide.md` | Generic statistical methods and templates | Phase 2 (analysis) |
| `docs/oncology_analysis_guide.md` | **Primary statistical guide for oncology projects**; endpoint/estimand, survival, competing risks, biomarkers, ctDNA, multiplicity | Phase 2 and Phase 6 |
| `docs/oncology_checklist.md` | Oncology-specific QC/reporting checklist (RCT, retrospective, neoadjuvant, metastatic, biomarker/ctDNA) | Phase 3 and Phase 6 |
| `docs/basic_research_guide.md` | **Primary planning guide for basic/mechanistic projects**; desired-claim-first design, validation ladder, experimental units, Results architecture | Phase 2-6 when applicable |
| `docs/basic_research_analysis_guide.md` | **Primary analysis/design override for basic/mechanistic experiments**; experimental unit, replication, nested/repeated designs, batch, randomization/blinding, multiplicity | Phase 2 and Phase 6 when applicable |
| `docs/basic_section_templates.md` | Conditional Methods/Results/Discussion structure for basic/mechanistic manuscripts | Phase 4 when applicable |
| `docs/basic_research_checklist.md` | Basic/mechanistic QC for claim strength, replication, perturbation, specificity, context, in vivo/human bridge, figure story | Phase 3 and Phase 6 when applicable |
| `docs/experimental_evidence_guide.md` | Claim→evidence→boundary map; necessity/sufficiency, rescue, alternatives, wording calibration | Phase 3-6 for mechanistic claims |
| `docs/figure_story_guide.md` | Scientific figure architecture: dominant claim, panel inferential roles, falsifiers, main-vs-supplement | Phase 3 before figure/Results drafting |
| `docs/evidence_guide.md` | Evidence 작성 가이드 (형식, 요약 방법, 워크플로우) | Phase 1 (setup) |
| `docs/revision_guide.md` | Reviewer response guide (응답서 작성, 외교적 표현) | Revision (리뷰어 코멘트 수신 후) |
| `docs/verification_protocol.md` | 검증 게이트·4 core Verifier + conditional mechanism overlay·자율 루프·게이트 원장 정의 | Phase 3·4·6·8 (게이트 수행 시 **반드시** 참조) |
| `docs/verifier_prompt_templates.md` | LLM semantic verifier prompt와 구조화 출력 schema | Constraint/logic/semantic citation/revision alignment 검증 시 |
| `docs/response_letter_template.md` | Author_response 양식으로 DOCX 변환하기 쉬운 response letter Markdown 템플릿 | Revision 응답서 작성 시작 시 복사 |
| `docs/figure_guide.md` | Figure generation guide (DPI, 팔레트, Python 템플릿) | Phase 2 (figure 생성 시) |
| `docs/docx_guide.md` | DOCX 변환 가이드 (서식, 테이블 스타일, 네이밍 규칙) | Phase 7 (DOCX 변환 시 **반드시** 읽고 따를 것) |
| `docs/draft_plan_template.md` | Draft plan 10개 항목 템플릿 (Phase 3에서 복사하여 사용) | Phase 3 시작 시 복사 → `drafts/draft_plan.md` |
| `docs/debate_protocol.md` | ChatGPT + independent reviewer co-author 토론 절차 (라운드·역할·로그·폴백) | Phase 2·3·4·8 (`paper debate` 요청 시) |
| `docs/critical_review_protocol.md` | 독립/멀티모델 적대적 검토 절차 (리뷰어 풀·합의도·폴백) | Phase 6 QC·Phase 8 (`critical review` 요청 시) |
| `profile/authors.md` | 저자 정보 (소속·연락처·ORCID·funding 문구 템플릿) | Title page 작성 시 **반드시** 참조 — 직접 입력 금지 |
| `profile/journals.md` | 저널별 인용 형식 (bracket vs superscript, et al. 기준, volume 형식) | 참고문헌 목록 작성 시 확인 |
| `profile.example/` | Git-safe bootstrap templates for the ignored local `profile/` folder | 새 manuscript project setup 시 복사하여 사용 |
| `knowledge/evidence.md` | 참고문헌 요약 정리 자료집 (논문별 요약·핵심·서지정보) | Phase 1 (setup) + 인용 시 참조 |
| `docs/medical_kag_protocol.md` | optional legacy spine-domain KAG integration; evidence.md 정본 유지 | Domain-matched project에서만 선택 사용 |
| `knowledge/pdf/` | Original reference PDFs (**gitignored**; copyright-protected, local only) | When verifying claims |
| `knowledge/summaries/` | 개별 논문 full-text 상세 요약 | 핵심 논문 상세 확인 시 |
| `Style/` | 논문 스타일 앵커 전용 폴더. `own/`, `landmark/`, `target_journal/` md와 `PDF/` 원본을 분리 보관 | Phase 3-5 (저널 스타일, 팀 voice, 논증 구조 정렬) |
| `Style/terminology.md` | Preferred/forbidden terminology registry (definition, context, notes) | Phase 3-6 (drafting, polish, lint/QC) |
| `data/` | Raw data (CSV/XLSX) | Phase 2 (statistical analysis) |
| `data/analysis_plan.md` | 분석 계획 (필수 작성·승인 후 분석 진행) | Phase 2 (before running analysis) |
| `data/py/` | Python analysis scripts | Phase 2 (statistical analysis) |
| `results/` | Analysis output CSV files | Phase 2 (after analysis) |
| `drafts/draft_plan.md` | 원고 구성 계획 (key message, table/figure plan, outline) | Phase 3 (drafting 전 필수) |
| `drafts/story_map.md` | Basic/mechanistic paper의 North Star, claim architecture, validation route, figure story source of truth | Phase 3 before drafting when applicable |
| `drafts/_templates/basic_methods.md`, `basic_results.md` | Basic/mechanistic mode-specific draft skeletons | Phase 4; use instead of clinical-default Methods/Results skeletons |
| `drafts/` | Individual section files, tables, figures | Phase 4-5 (drafting & polish) |
| `drafts/table_*.md` | Individual formatted tables | Phase 2 (from results CSV) |
| `drafts/figures/` | Generated figure files | Phase 2 (from analysis) |
| `scripts/search_pubmed.py` | PubMed 검색 스크립트 (NCBI E-utilities, 외부 패키지 불필요) | Phase 1 (reference search) |
| `scripts/compile_response_docx.py` | `response_letter_REV*.md`를 Author_response 양식 DOCX로 변환 | Phase 8 response letter finalize |
| `scripts/check_revision_claims.py` | `response_letter_REV*.md`의 `[CHANGE]` claims를 revised manuscript 파일과 대조 | Phase 8 ghost-revision gate |
| `scripts/check_citations.py` | `[EVID:id]` citations를 `knowledge/evidence.md`와 대조 | Phase 3·4·6 citation gate |
| `scripts/check_coverage.py` | 인용 coverage audit — **과잉인용**(한 문장 과다 인용)·**미등록인용** 주신호, 섹션별 인용밀도; uncited ref/미실현 claim은 중립 정보(낭비 아님) | Phase 6 QC (`Check coverage`) |
| `scripts/format_references.py` | `[EVID:id]` → 저널형 서지목록(numbered/author-year) + 본문 태그 변환(`*_formatted.md`); **MCP 독립**, evidence.md 정본 | Phase 7 (`Format references`) |
| `scripts/check_abstract.py` | abstract↔본문 수치 일관성 — abstract에만 있고 본문에 없는 수치 차단 (Rule 3; p값 기본 제외) | Phase 6 QC Round 1 (`Check abstract`) |
| `scripts/check_crossrefs.py` | 본문 "Table/Figure N" 언급 ↔ `table_*.md`·figure legends 대조 — **broken ref**(없는 것 참조, 주신호)·미인용 항목·첫 언급 순서; advisory 기본, `--fail-on-broken` 등으로 게이트화 | Phase 6 QC (`Check crossrefs`) |
| `scripts/check_abbreviations.py` | 약어 첫 사용 정의 검사 — abstract↔본문 별도 scope (UNDEFINED/DEFINED_AFTER_USE/REDEFINED/SINGLE_USE); 오탐 전제 advisory, `--allow`·`--strict` | Phase 6 QC (`Check abbreviations`) |
| `scripts/check_response_coverage.py` | response letter의 Comment↔Response 전수 매핑 + 원본 코멘트 파일 대조 — 미응답·빈 응답·placeholder 검출 (ghost-revision 게이트의 반대면; 기본 fail) | Phase 8 (`Check response coverage`) |
| `scripts/check_numbers.py` | manuscript/table 수치를 `results/*.csv`와 대조 | Phase 4·6 data gate |
| `scripts/check_gate.py` | `review/gates/*.GATE.md` 원장의 `status: PASS`와 필수 check를 검증 | 모든 phase gate 통과 직전 |
| `scripts/check_style.py` | manuscript를 `drafts/style_spec.md` 목표와 대조 (측정형 스타일 게이트) | Phase 5·6 (`style pass`, `Check style`) |
| `scripts/extract_claims.py` | 초안의 `[EVID:id]` 문장 추출 (claim-verification 입력) | Phase 6 (`verify claims`) |
| `scripts/evidence_table.py` | 구조화 study 레코드 → markdown 비교표 (included studies) | Phase 6 (`evidence table`) |
| `docs/citation_assist_protocol.md` | 출처 제안 + claim 검증 + stance + 비교표; evidence.md 정본 + PubMed-first discovery, optional domain-matched retrieval | Phase 3·4·6 |
| `docs/style_transform_protocol.md` | 초안→bound 학술/저널 스타일 변환 + Style Verifier·명시적 실행 | Phase 5 (`style pass`) |
| `docs/style_spec_template.md` | Style Spec 템플릿 (exemplar 바인딩, 목표 metric) | Phase 5 (Style Spec 작성) |
| `review/qc_log.md` | QC round documentation | Phase 6 (track all QC iterations) |
| `review/claim_evidence_matrix.md` | Central claim-to-evidence matrix generated for substantial basic/mechanistic projects | Phase 3/6 when applicable |
| `review/mechanism_audit.md` | `chatgpt/actions/audit-mechanism.md` persistent audit output | Phase 3/6 basic/mechanistic gate |
| `review/gates/` | 검증 게이트 원장 (Verifier PASS/FAIL 기록) | Phase 3·4·8 (게이트 통과 기록) |
| `output/` | Final compiled manuscript (docx only) | Phase 7 (finalize) |
| `review/reviewer_comments_REV{N}.md` | 리뷰어 코멘트 원문 | Phase 8 (revision) |
| `drafts/revision/REV{N}/` | Revision별 수정 원고 | Phase 8 (revision) |
| `output/revision/REV{N}/` | Revision별 최종 DOCX + response letter | Phase 8 (revision) |

---

## Critical Rules (MUST FOLLOW)

### 1. Citation Integrity

- **NEVER fabricate or hallucinate references**
- **ALWAYS check `knowledge/evidence.md` first** before searching (avoid duplicate work)
- **Evidence retrieval is domain-aware:** start with `knowledge/evidence.md`; use PubMed-first discovery for breast oncology/basic/translational work. The bundled `medical-kag` is spine-specific and optional only for domain-matched projects. Any newly surfaced paper from any backend must be verified and registered as `[EVID:id]` before citation. (`docs/citation_assist_protocol.md`, `docs/medical_kag_protocol.md`)
- **Reference PDFs are local only:** store PDFs under `knowledge/pdf/`; do not commit copyrighted PDFs.
- **Style anchors are separate from references:** keep writing-style material under `Style/`, not `knowledge/`.
- **Style anchor mirror rule:** use matching basenames between PDF and md (e.g., `Style/PDF/landmark/weber_2007_sciatica.pdf` ↔ `Style/landmark/weber_2007_sciatica.md`).
- **Terminology enforcement:** use `Style/terminology.md` as the vocabulary registry. Preferred terms are required; forbidden terms must be replaced unless an exception is documented in `drafts/draft_plan.md`.
- **New reference workflow:** (상세: `docs/evidence_guide.md`)
  1. Search → verify paper exists
  2. Save PDF to `knowledge/pdf/author_year_keyword.pdf`
  3. Register in `knowledge/evidence.md` with summary & key points
  4. 핵심 논문은 `knowledge/summaries/`에 상세 요약 추가
  5. Then cite in manuscript

### 1A. Oncology Method Override (Sim Custom)

For breast oncology / translational projects, **`docs/oncology_analysis_guide.md` takes precedence over generic statistical heuristics** in `docs/statistical_analysis_guide.md` when they conflict. In particular:

- Define the clinical question as **endpoint + estimand + analysis population + time origin + event/censoring/intercurrent-event rules** before choosing a test/model.
- Do not choose parametric vs nonparametric methods from a normality-test p-value alone. Do not use the old `kstest(data, 'norm')` rule.
- Do not choose multiplicity correction solely from the number of comparisons; define the hypothesis family and confirmatory/exploratory status first.
- For time-to-event outcomes, predefine PH assessment and alternatives (time-varying effects, landmark estimates, RMST) when appropriate.
- For competing events, use cumulative incidence and an estimand-appropriate cause-specific or subdistribution model rather than default Kaplan-Meier.
- A biomarker is **predictive** only when treatment-effect heterogeneity is supported by an interaction analysis; significance in one subgroup and non-significance in another is insufficient.
- Serial biomarkers/ctDNA require explicit sampling time, landmark/time-dependent handling, and immortal-time bias checks.
- Use `docs/oncology_checklist.md` in addition to the general reporting checklist.

### 1B. Basic / Mechanistic Research Override (Sim Custom)

For wet-lab, mechanistic, preclinical, molecular/cell biology, tumor-microenvironment, and discovery-to-validation papers, use `docs/basic_research_guide.md`, `docs/basic_research_analysis_guide.md`, and `docs/experimental_evidence_guide.md`; use `docs/basic_section_templates.md` for drafting.

- Start from the **desired biological claim**, not from an experiment list.
- For substantial basic/mechanistic projects, create `drafts/story_map.md` before Phase 4 using `chatgpt/actions/build-story-map.md` (multi-paper: `drafts/paper{N}_xxx/story_map.md`).
- `story_map.md` is the scientific-architecture source of truth; `draft_plan.md` remains the manuscript-execution source of truth. They must agree.
- Distinguish association → orthogonal confirmation → perturbation → specificity/rescue → context robustness → in vivo → human/translational bridge. **Do not force every project through every level.**
- Define the independent experimental unit and distinguish biological replicates, technical replicates, and nested subsamples before statistical interpretation.
- For basic/mechanistic Phase 2, `docs/basic_research_analysis_guide.md` overrides conflicting generic statistical heuristics; do not use normality-test p-values or raw comparison counts as automatic test/multiplicity selectors.
- Record randomization/allocation, blinding, sample-size rationale, predefined exclusions/QC, and important batch/block factors when applicable.
- One main figure should normally carry one dominant claim, with panel roles defined by inference rather than by plotting convenience (`docs/figure_story_guide.md`).
- Organize Results claim-by-claim / question-by-question, not as an experiment log.
- Mechanistic verbs (`required for`, `sufficient for`, `mediates`, `drives`) must match the achieved evidence level.
- Run `docs/basic_research_checklist.md` and `chatgpt/actions/audit-mechanism.md` during Phase 3 and again during Phase 6 when applicable.
- For Phase 4 Basic-Mechanistic/Hybrid drafting, use `docs/basic_section_templates.md` and the mode-specific skeletons under `drafts/_templates/`; do not force patient-flow/primary-endpoint clinical headings onto wet-lab Results.

---

### 2. Redundancy Prevention

**Section Content Rules:**

| Section | Contains | Does NOT Contain |
|---------|----------|------------------|
| Introduction | Background, gap, rationale | Your results interpretation |
| Discussion | Your findings interpretation | Repeated background info |
| Results (text) | Narrative of findings | Exact numbers from tables |
| Tables | All numerical data | Narrative interpretation |

**Avoid Triple Duplication**
> 동일 데이터가 Results 본문 + Table + Figure 세 곳에 모두 나타나는 것은 지양

| Recommended | Avoid (지양) |
|-------------|--------------|
| Table only | Text에 상세 숫자 + Table에 같은 숫자 |
| Figure only | Table + Figure에 동일 데이터 |
| Table + brief text reference | Results 본문에 Figure 내용 상세 기술 |

**Results Text Writing:**
- ✅ "Baseline characteristics are shown in Table 1"
- ✅ "Group A showed significantly better outcomes (Table 2, *p*=0.023)"
- ❌ "Mean age was 54.3±12.1 years in Group A and 52.1±11.8 in Group B..."

**Table vs Figure Decision (물어보기):**
> "이 데이터는 Table로 할까요, Figure로 할까요?"
- 정확한 수치 필요 → Table
- 추세/분포 강조 → Figure
- 둘 다 만들지 않음 (중복)

**Standard Table Structure:**

| Table # | Content |
|---------|---------|
| Table 1 | Baseline Characteristics (demographics) |
| Table 2 | Main Results (primary + key secondary) |
| Table 3+ | Additional Analyses (subgroup, regression) |

> **Table 개수 가이드:** 가급적 5개 이하 권장. 꼭 필요하지 않은 세부 분석은 Supplement로 분리. 단, 논문 흐름상 필수적인 경우 5개 초과도 가능.

### 3. Consistency Requirements
These must match across **Abstract ↔ Methods ↔ Results ↔ Tables**:
- Patient/sample numbers
- Statistical values (p-values, CIs, means, SDs)
- Time periods and follow-up duration
- Outcome measure names and definitions

### 4. QC Process (MANDATORY)
- Run **minimum 3 QC rounds** before submission
- Follow `docs/qc_guide.md` for detailed procedures
- Document all checks in `review/qc_log.md`
- **진행 추적(선택):** QC 라운드·게이트 항목은 ChatGPT의 세션 내 task tracking으로 보조 추적할 수 있다. 단 이는 **세션용 보조 수단일 뿐 정본(authoritative record)이 아니다** — 영속 기록은 `review/qc_log.md`와 `review/gates/`가 담당한다.

### 5. File Versioning (파일 버전 관리)

> 최종본, revision, 대규모 변경 시 파일명에 버전을 표기해야 함

**기본 규칙:** 저자가 별도 스타일을 지정하지 않으면 **날짜(YYMMDD)** 를 기본으로 사용

**버전 표기 형식:**

| 형식 | 용도 | 예시 |
|------|------|------|
| `_YYMMDD` | 기본 (날짜 기반) | `manuscript_260414.docx` |
| `_v1`, `_v2` | 저자 요청 시 (순차 버전) | `manuscript_v1.docx` |
| `_REV1`, `_REV2` | Revision 제출본 | `manuscript_REV1_260414.docx` |
| `_FINAL` | 최종 제출본 | `manuscript_FINAL_260414.docx` |

**적용 시점:**
- **Phase 7 (Finalize):** 최초 제출본에 날짜 또는 버전 부여
- **Revision:** `_REV1`, `_REV2` 표기 필수 (+ 날짜 병기 권장)
- **대규모 변경:** 기존 파일 덮어쓰지 않고 새 버전으로 저장
- **Minor 수정:** 동일 파일명 유지 가능 (git으로 추적)

**파일명 패턴:**
```
{내용}_{버전}_{날짜}.{확장자}
```
- 예: `manuscript_REV1_260414.docx`, `table_1_v2.docx`, `response_letter_REV1_260414.docx`
- 저자가 원하는 스타일이 있으면 그에 따름 (저자 지시 우선)

### 6. Multi-Paper Organization (멀티 논문 정리)

> 하나의 데이터에서 여러 논문을 작성할 때 반드시 서브폴더로 분리

**규칙:**
- `data/`, `results/`, `drafts/`, `output/`, `review/` 각각에 논문별 서브폴더 생성
- `docs/`, `knowledge/`, `scripts/`는 공유 (서브폴더 불필요)
- 서브폴더명: `paper{N}_{keyword}` 또는 저자가 지정한 이름
- 원본 데이터는 `data/` 루트에, 논문별 필터링 데이터는 서브폴더에 배치

**Revision 시:**
- 각 논문 서브폴더 안에 `revision/REV1/`, `revision/REV2/` 생성
- 수정된 섹션만 revision 폴더에 저장 (변경 없는 파일은 복사하지 않음)
- Response letter도 해당 revision 폴더에 포함
- output도 동일하게 `output/{paper}/revision/REV1/` 구조

### 7. Analysis Plan Mandatory (분석 계획 필수)

> **통계 분석 전에 반드시 analysis_plan.md를 작성하고 확인받아야 한다**

**규칙:**

- **NEVER run statistical analysis without first creating `analysis_plan.md`**
- `Analyze data` 명령 시 반드시 analysis_plan.md를 먼저 생성
- 사용자가 analysis_plan.md를 확인한 후에만 스크립트 생성/실행 진행
- analysis_plan.md가 존재하지 않으면 분석 스크립트 생성을 거부

**논문별 개별 작성:**

- **Single paper:** `data/analysis_plan.md`
- **Multi-paper:** 각 논문 서브폴더에 개별 작성
  - `data/paper1_xxx/analysis_plan.md`
  - `data/paper2_yyy/analysis_plan.md`
- 같은 데이터라도 논문마다 연구 질문·대상·분석이 다르므로 **반드시 별도 작성**
- 공유 데이터(`data/raw_data.csv`)에 대한 공통 analysis_plan은 만들지 않음

**analysis_plan.md 필수 포함 내용:**

1. 연구 질문 및 가설
2. 대상 선정/제외 기준 (해당 논문에 맞게)
3. 변수 정의 (primary/secondary/exploratory endpoints)
4. 통계 검정법 선택 및 근거
5. 유의수준 및 다중비교 보정 계획
6. **Basic/mechanistic 해당 시:** experimental unit, biological/technical replicate, planned contrast, nested/repeated structure, batch/block, randomization/blinding, sample-size rationale, predefined exclusions/QC

### 8. Draft Plan Mandatory (원고 구성 계획 필수)

> **원고 작성 전에 반드시 draft_plan.md를 작성하고 확인받아야 한다**

**규칙:**

- **NEVER start drafting sections without first creating `draft_plan.md`**
- 분석 결과(results/)를 확인한 후, 원고 작성 전에 전체 구성을 먼저 계획
- **Basic/mechanistic conditional requirement:** when the paper's central contribution is experimental mechanism/biology, also create and approve `drafts/story_map.md` before Phase 4 (multi-paper: the matching `drafts/paper{N}_xxx/story_map.md`). Build it with `chatgpt/actions/build-story-map.md`; do not substitute a figure list for the claim architecture.
- **Step 0 (Socratic 브레인스토밍):** 항목을 채우기 전, 사용자에게 **한 번에 하나씩** 질문해 의도를 정제한다 (`docs/draft_plan_template.md` 상단). 이 답변은 선택적 `paper debate`의 R0 준비자료로 쓰되 토론 자체와는 별개다.
- 사용자가 draft_plan.md를 확인한 후에만 섹션 작성 진행
- draft_plan.md가 존재하지 않으면 섹션 작성을 거부

**저장 위치:**

- **Single paper:** `drafts/draft_plan.md`
- **Multi-paper:** 각 논문 서브폴더에 개별 작성
  - `drafts/paper1_xxx/draft_plan.md`
  - `drafts/paper2_yyy/draft_plan.md`

**draft_plan.md 필수 포함 내용:**

1. **Key message** — 이 논문의 핵심 메시지 (1-2문장)
2. **Tone & voice** — 논문의 논조/어조 설정
   - 예: "conservative & evidence-based", "novel technique 강조", "기존 방법과 동등성 주장"
   - 전체 원고에서 일관되게 유지할 톤 명시
3. **Essential references** — 반드시 인용해야 할 핵심 참고문헌 목록
   - evidence.md에서 선별하거나, 추가 검색이 필요한 주제 명시
   - 각 reference의 인용 목적 기재 (배경, 방법론 근거, 비교 대상 등)
4. **Evidence gap** — 추가로 필요한 근거 자료 (아직 evidence.md에 없는 것)
   - 검색 키워드 또는 필요한 논문 유형 명시
5. **Table/Figure plan** — 몇 개, 각각 어떤 내용, Table vs Figure 결정
6. **Introduction outline** — Background → Gap → Purpose 흐름
7. **Discussion outline** — 주요 논점 3-5개, 비교할 선행연구 목록
8. **Limitation points** — 예상 한계점 및 대응 논리
9. **Target word count** — 저널 기준에 맞춘 섹션별 목표 분량 (선택)
10. **Claim→Citation mapping** — 핵심 주장 ~20개와 그 근거 논문 매핑 (쓰기 전에 확인 필수)
    - Introduction background: 5–8 claims (배경 지식의 근거)
    - Methods rationale: 2–3 claims (방법론 선택 근거)
    - Discussion comparisons: 5–8 claims (선행연구와의 비교 및 contextualisation)
    - 형식: `[Claim 요약] → Author Year (evidence.md 번호)`
    - **규칙:** claim을 작성하기 전에 citation을 먼저 확보할 것 — 없으면 Phase 1로 돌아가 검색

**Basic/mechanistic 추가 필수 항목 (해당 시):**

- central biological question + desired main claim
- current evidence level + claim boundary/non-claim
- independent experimental unit / biological-vs-technical replicate map
- weakest evidence link + necessary/recommended/optional validation route
- `drafts/story_map.md`의 claim architecture와 figure order
- each main figure's dominant claim, panel inferential roles, decisive control/falsifier, and next question

### 9. Verification Gates Mandatory (검증 게이트 필수)

> **각 산출 단계 뒤에 검증 게이트를 통과해야 다음으로 진행할 수 있다.**
> 상세: `docs/verification_protocol.md`

**규칙:**

- **NEVER proceed past a gate without a recorded PASS.** `review/gates/`의 해당 산출물 항목에 `status: PASS`가 없으면 다음 섹션/단계 진행을 거부한다.
- 검증은 **Verifier 서브에이전트**로 수행한다 (Draft: Constraint / Citation / Data / Logic 4종. Revision: Logic을 빼고 Revision-claims·Response-alignment를 더해 Constraint / Citation / Data / Revision-claims / Response-alignment). 외부지식 금지, 소스 오브 트루스(draft_plan·analysis_plan·evidence.md·results CSV, basic/mechanistic이면 story_map 포함)와만 대조.
- FAIL 시 **자율 수정 루프**: 지적사항을 고쳐 재검증. 최대 **2회(N=2)**, 이후 사용자에게 에스컬레이션.
- **Verifier reasoning:** semantic verifier는 higher reasoning effort를 기본으로 사용한다. 모델명에 의존하지 않고 현재 ChatGPT runtime에서 사용 가능한 높은 추론 수준을 선택한다.
- **인용 grounding:** 초안에서 모든 인용은 `[EVID:author_year]` 태그로 표기 (Phase 7에서 저널 형식 변환).
- **수치 grounding:** 원고의 **study result values**는 `results/*.csv`에 존재하는 값만 사용한다. Experimental-design constants(용량, 시간, replicate 계획, acquisition setting 등)는 승인된 `analysis_plan.md`/Methods source에 근거한다.
- **ChatGPT + Shellby 명시적 강제:** 자동 runtime hook은 사용하지 않는다. 따라서 plan-first, Style Spec/terminology lint, style-pass, deterministic verification, semantic verifiers, gate recording/freshness checks를 각 Phase에서 **명시적으로 실행**해야 한다. 파일 작업은 ChatGPT가 Shellby를 통해 수행하며, **Mac Studio의 로컬 파일은 sSb**, **MacBook/로컬 파일은 mSb**를 사용한다. 자동 훅이 없다는 이유로 Rule 7/8/9 또는 verification semantics를 완화하지 않는다.

**게이트 배치·병렬·freshness:** Phase별 게이트(3 Claim→Citation 사전검증 · 4 섹션 게이트 · 6 경량 · 8 응답 게이트), 병렬 검출, freshness 해시 규칙은 `docs/verification_protocol.md` §7/§3.1/§6 참조. PASS 시 산출물 sha256를 `provenance:`에 기록하고, 산출물이 바뀌면 stale로 보고 재검증(`check_gate.py --verify-hash`). **결정적 차원(citation/numbers/revision_claims)은 `check_gate.py --cross-check`로 원장의 `PASS`를 정본 checker 즉석 재실행과 대조** — 안 돌리고 적은 가짜 PASS나 stale PASS를 모순으로 차단(소스 미도달 시 loud FAIL).

### 10. STOP Signals (자기기만 차단)

> Verifier가 잡는 것은 산출물의 결함이다. 이 표는 그 **앞단** — 사람·에이전트가 검증을 건너뛰려는 *합리화의 순간*을 차단한다. 아래 생각이 들면 멈추고(STOP) 오른쪽 행동을 한다.

| 머릿속 생각 (STOP) | 현실 / 해야 할 행동 |
|---|---|
| "이 결과 숫자는 대충 맞을 거야" | study result value는 `results/*.csv`와 대조. CSV에 없으면 쓰지 않는다. (`check_numbers.py`) |
| "dose/time/replicate 수는 기억나는 대로 쓰면 돼" | experimental-design constant는 승인된 `analysis_plan.md`/Methods source와 대조한다. |
| "이 인용 어디서 본 것 같은데" | `knowledge/evidence.md`에서 `[EVID:id]` 확인. 없으면 인용 금지. (`check_citations.py`) |
| "검색 도구가 찾았으니 바로 인용해도 돼" | 아니다. 어떤 backend든 source identity를 확인하고 evidence.md에 `[EVID:id]`로 등록한 뒤에만 인용한다. (`docs/citation_assist_protocol.md`) |
| "한 번만 더 보면 통과겠지" | 게이트 먼저. `status: PASS` 없이는 다음 섹션 진행 금지. |
| "고친 김에 이 문장도 손봤어" | 검증 중 산출물 수정 금지. 판정을 모두 모은 뒤 한 번에, 그리고 전체 재검증. |
| "리뷰어 말이 맞지만 반박하고 싶다" | 근거 없는 반박 금지. 반박은 1-2개로 제한하고 문헌으로 뒷받침. |
| "이 정도면 novel하다고 써도 돼" | draft_plan의 tone·claim 범위 확인. 데이터가 지지하지 않는 주장 금지. |
| "knockdown에서 phenotype이 바뀌었으니 mechanism이 증명됐어" | perturbation은 기능 지지이지 자동으로 specificity/mediation 증명이 아니다. `experimental_evidence_guide.md`에서 rescue/dependency/alternative explanation을 점검한다. |
| "cell이 수천 개니까 n도 수천이야" | 독립 experimental unit을 먼저 정의한다. cells/fields/wells는 흔히 nested subsample이지 biological `n`이 아니다. |
| "animal/human validation을 넣으면 무조건 더 강해져" | 현재 weakest link를 해결하는지 먼저 본다. 새 evidence layer가 새 질문을 답하지 않으면 optional/supplement일 수 있다. |
| "Constraint는 나중에 봐도 돼" | 명세(scope/tone/forbidden) 위반은 1순위. 곧 폐기될 문장을 다듬지 않는다. |
| "PASS 받았으니 이제 안전해" | 산출물을 바꿨다면 그 PASS는 stale. `provenance` 해시로 재검증. |

### 11. Model Selection by Phase (단계별 모델 선택)

> **계획 단계는 high-quality 모델, 작성 단계는 mid-quality 모델도 가능**

**원칙:** Draft plan이 충분히 상세하면, 이후 작성은 plan을 따라가는 것이므로 비용 효율적 모델 사용 가능

| Phase                    | 권장 모델           | 대안 모델         | 이유                                       |
|--------------------------|---------------------|-------------------|--------------------------------------------|
| Phase | ChatGPT reasoning guidance |
|---|---|
| Phase 1: Setup | Normal reasoning for routine search, organization, and file preparation |
| **Phase 2: Analysis** | **Higher reasoning effort** for estimand, endpoint, statistical/biomarker/ctDNA analysis planning |
| **Phase 3: Draft Plan** | **Higher reasoning effort** for key message, structure, claim-citation map, oncology reporting strategy, and basic/mechanistic story-map architecture when applicable |
| Phase 4: Draft | Normal reasoning for routine evidence-grounded drafting; raise effort for difficult methodological/interpretive sections |
| Phase 5: Style Polish | Normal reasoning plus explicit Style Spec, terminology, and style checks |
| Phase 6: QC | Normal reasoning for deterministic checks; **higher reasoning effort for semantic verifiers** |
| Phase 7: Finalize | Normal reasoning for formatting/reference conversion |
| **Phase 8: Revision** | **Higher reasoning effort** for reviewer-response strategy and revision consistency |
| **Verifier** | **Higher reasoning effort** for semantic Constraint/Citation/Data/Logic or revision verifiers |

- Runtime-neutral principle: use the strongest reasoning effort available when strategic design, causal/statistical judgment, or semantic verification materially affects correctness.
- Routine drafting and mechanical transformations normally use normal reasoning once plans, evidence, and gates are established.

### 12. Documentation, Versioning & Git Safety (Sim Custom)

> Harness code/doc changes remain synchronized, but this custom fork must never push changes to the public upstream repository.

**Rules:**

- **Code ↔ docs together:** when changing harness behavior, CLI flags, hooks, or validation logic, update the affected documentation in the same change.
- **Custom versioning:** use `Sim Oncology Custom vX.Y.Z`; keep the upstream base recorded separately (`upstream-v1.6.3`).
- **Upstream is read-only:** remote `upstream` is only for `fetch`/comparison/merging. **Never push to `upstream`.**
- **User remote:** when a personal GitHub repository is created, configure it as `origin`. Push only to `origin`, and only when the user explicitly asks or a user-approved automation requires it.
- **Before commit/push:** inspect `git status`, `git diff`, tests, and ensure protected/private files are not staged.
- **STOP:** do not auto-push when manuscript WIP, private data, PDFs, profile files, destructive changes, or history rewriting are involved.

---

## Natural Academic Writing Style

> **상세 가이드: `docs/writing_guide.md`**
> 규칙·표·예시는 writing_guide.md에 있음. CHATGPT.md는 워크플로·Phase 조정만 담당 (중복 방지).

**Phase 5 (Style Polish)에서 적용할 writing_guide.md 섹션:**

| 영역 | writing_guide.md 섹션 | 주요 내용 |
|------|----------------------|-----------|
| 전역 규칙 | General Principles | 시제, Bold 금지, 약어 1회 정의, 임상 결과 주어, 동의어 혼용 금지, 숫자 서식, 문두 숫자 |
| 스타일 표 | Style Reference Tables | Voice & Tense / Transition / Verb Upgrades / Common Corrections / Statistical Notation / Hedging |
| AI 군살빼기 | AI-Draft De-bloat | -ing 피상분석·AI어휘·신호어 제거; 충돌 패턴(hedging/copula/passive) 적용 제외 |
| 작문 원칙 | Writing Principles (4 Pillars) | Clarity / Conciseness / Objectivity / Consistency |
| 섹션별 규칙 | 01. Title ~ 10. Tables | 각 섹션 구조·구체 규칙·예시 |

**Phase 5 워크플로:**
1. `docs/writing_guide.md` Style Reference Tables 읽기
2. 섹션별로 Transition/Verb/Corrections 적용
3. AI 초안인 경우 AI-Draft De-bloat 적용 (-ing 피상분석·AI어휘·신호어 제거; 충돌 패턴 제외)
4. Writing Principles (4 Pillars) 기준으로 검토
5. Dr. Editor 최종 polish

---

## Recommended Workflow

```
Phase 1: Setup
├── 새 project에서 profile/이 없으면 profile.example/*.example.md를 profile/authors.md, profile/journals.md로 복사 후 로컬 정보 입력
├── Define topic, journal, study design in CHATGPT.md
├── Check profile/journals.md — 목표 저널 인용 형식 확인 (et al. 규칙, volume 형식 등)
├── Check Style/own/ — 관련 스타일 앵커 논문 확인 (용어·톤 일관성 참고)
├── Search references: `chatgpt/actions/search-evidence.md` action [query] 또는 scripts/search_pubmed.py
├── Evidence discovery: evidence.md 우선 → PubMed/search_pubmed.py로 신규 근거 검색; bundled medical-kag는 spine-domain match일 때만 optional 보조로 사용
├── Import by DOI: `chatgpt/actions/import-doi.md` action [doi]
├── Save PDFs to knowledge/pdf/
├── Summarize & register in knowledge/evidence.md (docs/evidence_guide.md 참조)
├── 핵심 논문은 knowledge/summaries/에 상세 요약
└── Read docs/writing_guide.md for target sections

Phase 2: Statistical Analysis — higher reasoning effort 권장 (analysis_plan)
├── Research-mode analysis routing:
│   ├── Clinical oncology/translational → docs/oncology_analysis_guide.md
│   ├── Basic/mechanistic experimental → docs/basic_research_analysis_guide.md
│   └── Generic background only → docs/statistical_analysis_guide.md (mode-specific overrides take precedence)
├── Place raw data (CSV/XLSX) in data/
├── (선택) `chatgpt/actions/paper-debate.md` action — 분석 접근을 독립 reviewer와 토론 후 plan 작성
├── Create data/analysis_plan.md (필수, 사용자 승인 후 진행)
│   ├── ChatGPT reads data via Shellby → creates analysis plan → 사용자 확인
│   └── 포함 항목: estimand, analysis population, endpoint/time origin/censoring, model, multiplicity, missing data, sensitivity
├── Generate Python scripts in data/py/
│   ├── 01_descriptive.py (demographics, baseline)
│   ├── 02_comparative.py (group comparisons)
│   └── 03_regression.py (if needed)
├── Run analysis → export results to results/
│   └── table1_demographics.csv, table2_outcomes.csv, etc.
├── Generate drafts/table_*.md from results CSV
└── Generate figures → drafts/figures/

Phase 3: Draft Plan (원고 구성 계획) — higher reasoning effort 권장
├── Step 0: Socratic 브레인스토밍 — 항목을 채우기 전 사용자에게 한 번에 하나씩 질문해 의도(key message) 정제 (draft_plan_template.md 상단; `paper debate`와 별개, R0 준비자료로 활용)
├── (선택) `chatgpt/actions/paper-debate.md` action — key message·구조를 독립 reviewer와 토론 후 plan 작성
├── Basic/mechanistic project이면 `chatgpt/actions/build-story-map.md` 실행 → drafts/story_map.md (multi-paper: 해당 drafts/paper{N}_xxx/story_map.md)
│   ├── North Star: biological problem → central question → desired main claim → boundary
│   ├── Claim→Evidence matrix + weakest link
│   ├── independent experimental unit / replicate hierarchy
│   ├── validation route: necessary / recommended / optional
│   └── one dominant claim per main figure + panel inferential roles + falsifier + next question
├── Copy docs/draft_plan_template.md → drafts/draft_plan.md (또는 논문별 서브폴더)
│   ├── Key message (이 논문의 핵심 메시지 1-2문장)
│   ├── Tone & voice (논조/어조 설정)
│   ├── Essential references (필수 인용 참고문헌 + 인용 목적)
│   ├── Evidence gap (추가 필요 근거 자료)
│   ├── Claim→Citation mapping (핵심 주장 ~20개 + 각 근거 논문 — Style/own/ 참조 가능)
│   ├── Table/Figure plan (어떤 Table/Figure를 몇 개, 어떤 내용으로)
│   ├── Introduction outline (background → gap → purpose 흐름)
│   ├── Discussion outline (주요 논점 3-5개, 비교할 선행연구)
│   ├── Limitation points (예상 한계점)
│   └── Target word count (저널 기준, 선택)
├── 🔒 GATE: Claim→Citation 사전검증 (Citation Verifier) — 근거 없는 literature claim은 글쓰기 전 차단
├── 🔒 Basic/mechanistic overlay: `chatgpt/actions/audit-mechanism.md` → mechanism PASS/BLOCKED/FAIL 기록 (해당 시)
├── 사용자 확인 후 Phase 4 진행
└── Multi-paper: drafts/paper{N}_xxx/draft_plan.md

Phase 4: Draft (in this order)
├── Read docs/drafting_protocol.md + docs/section_templates.md before drafting
├── Basic/mechanistic이면 docs/basic_research_guide.md + basic_research_analysis_guide.md + experimental_evidence_guide.md + figure_story_guide.md + basic_section_templates.md와 승인된 story_map.md를 함께 적용
├── Basic/mechanistic Methods/Results는 drafts/_templates/basic_methods.md 및 basic_results.md 구조를 사용; clinical-default patient-flow skeleton을 강제하지 않음
├── Apply Style/terminology.md and relevant Style anchors during drafting
├── (선택) `chatgpt/actions/paper-debate.md` action — 핵심 섹션 논증 골격을 독립 reviewer와 토론 후 작성
├── 04_methods.md      → establishes framework
│   └── Expert: Dr. Researcher B (methodology)
├── 05_results.md      → narrative (refer to drafts/table_*.md)
│   └── Expert: Dr. Researcher B; basic/mechanistic이면 Experimental Biology PI와 claim-by-claim 구조 점검
├── 03_introduction.md → background & gap
│   └── Expert: Dr. Researcher A (clinical)
├── 06_discussion.md   → interpretation (check vs intro)
│   └── Expert: Dr. Researcher A
├── 07_conclusion.md   → brief takeaway
├── 02_abstract.md     → summary (write LAST)
├── 01_title.md        → finalize (profile/authors.md 참조하여 저자·소속·ORCID·funding 기입)
└── 🔒 GATE (각 섹션마다): Constraint + Citation + Data + Logic Verifier 자율 루프 (최대 2회) → review/gates/ 기록

Phase 5: Style Polish
├── `chatgpt/actions/style-pass.md` action — 초안을 bound Style Spec/exemplar에 맞춰 섹션별 변환 + Style Verifier (docs/style_transform_protocol.md; style transformation 요청 시 명시적으로 실행)
├── Apply writing_guide.md Style Reference Tables
│   ├── Transition Words 업그레이드 (but → nonetheless)
│   ├── Verb Upgrades (showed → demonstrated)
│   ├── Voice & Tense by Section 확인
│   ├── Common Corrections 적용
│   ├── Statistical Notation 검증 (*p* italic, en-dash 등)
│   └── Hedging Language 적정성 확인
├── Apply docs/section_templates.md sentence-pattern pass
├── Apply Style/terminology.md terminology pass
├── Run `python3 scripts/lint_manuscript.py drafts --quiet` on Windows and fix high-priority findings
├── Apply writing_guide.md Writing Principles (4 Pillars)
│   └── Clarity / Conciseness / Objectivity / Consistency
└── Expert: Dr. Editor (final polish)

Phase 6: QC (3 rounds CRITICAL, 6 rounds RECOMMENDED)
├── Round 1: Number consistency — ChatGPT 명시적 실행 + 사용자 확인 (qc_guide.md)
├── Round 2: Reference verification — ChatGPT + 사용자 (evidence.md 대조)
├── Round 3: Logic & flow check — Dr. Editor (section 간 흐름)
├── Round 4: Terminology/abbreviation/tense + style metrics — Dr. Editor + lint + check_style.py vs Style Spec (권장)
├── (권장) Check crossrefs / Check abbreviations — Table·Figure 참조 정합 + 약어 정의 advisory 점검
├── Round 5: Statistical quality — Dr. Statistician (권장)
├── Round 6: Critical review — 내부(Dr. Editor + Dr. Statistician) + (선택) `chatgpt/actions/critical-review.md` action 외부 멀티모델 (overclaiming/bias/일반화, 권장)
├── Basic/mechanistic overlay: `docs/basic_research_checklist.md` + `chatgpt/actions/audit-mechanism.md` 재실행 → claim strength, replicate hierarchy, specificity/rescue, figure-story alignment + randomization/blinding/exclusions/model identity/image/source-data rigor 확인
├── Round 6.5 (선택): Editorial desk-screen — `chatgpt/actions/editor-review.md` action: high-impact 저널 편집장 관점 (임상 타당성·분야 scope fit·추가검증 roadmap·하위저널 추천; advisory, `docs/critical_review_protocol.md` §5)
├── Claim verification (선택): `chatgpt/actions/verify-claims.md` action — 인용 문장별 SUPPORTED/PARTIAL/UNSUPPORTED 리포트 (docs/citation_assist_protocol.md; evidence.md 정본 + verified source, PubMed-first discovery)
├── Document all rounds in review/qc_log.md
├── Run study-specific checklist (checklist_guide.md — CONSORT/STROBE/PRISMA/CARE)
├── For oncology projects also run docs/oncology_checklist.md
└── For basic/mechanistic projects also run docs/basic_research_checklist.md

Phase 7: Finalize
├── Read docs/docx_guide.md (DOCX 변환 규칙 확인)
├── Compile to DOCX (docs/docx_guide.md 규칙대로)
│   ├── output/title_page_YYMMDD.docx (별도)
│   ├── output/manuscript_YYMMDD.docx (본문 병합, 테이블 제외)
│   └── output/table_N_YYMMDD.docx (각 테이블 별도)
├── 파일명에 버전 표기 (기본: _YYMMDD, 저자 지정 시 _v1 등)
├── Co-author review
└── Final read-through

Phase 8: Revision (리뷰어 코멘트 수신 후)
├── Read docs/revision_guide.md
├── 리뷰어 코멘트 저장: review/reviewer_comments_REV1.md
├── Revision 폴더 생성: drafts/revision/REV1/, output/revision/REV1/
├── 수정된 섹션만 _REV1 접미사로 저장
├── (선택) `chatgpt/actions/paper-debate.md` action — 대응 전략을 독립 reviewer와 토론 후 response 작성
├── Response letter 작성 → drafts/revision/REV1/response_letter_REV1.md
├── 🔒 GATE (각 응답마다): ghost-revision 검증 (응답 주장 ↔ 원고 diff 대조) 자율 루프
├── Check response coverage — 모든 리뷰어 코멘트에 응답 존재 확인 (check_response_coverage.py --comments)
├── QC re-run (최소 Round 1-2 재수행)
├── Compile revised DOCX → output/revision/REV1/
│   ├── manuscript_REV1_YYMMDD.docx
│   ├── table_N_REV1_YYMMDD.docx (변경된 테이블만)
│   └── response_letter_REV1_YYMMDD.docx
└── 2차 revision 시: REV2/ 폴더에 동일 구조 반복
```

### Phase Completion Criteria

| Phase | Move to Next When |
|-------|-------------------|
| 1 → 2 | knowledge/evidence.md has ≥10 verified refs, topic defined, data ready |
| 2 → 3 | analysis_plan.md created & approved, all analyses complete, tables generated |
| 3 → 4 | draft_plan.md created & approved — 10개 필수 항목 완결; **basic/mechanistic이면 story_map.md + mechanism audit PASS도 필요** — Rule 8 참조 |
| 4 → 5 | All sections drafted, numbers match tables |
| 5 → 6 | Writing style rules applied, Dr. Editor reviewed |
| 6 → 7 | Minimum 3 QC rounds passed (6 recommended), checklist complete |
| 7 → Submit | Co-author approved, journal requirements met, versioned files in output/ |
| Submit → 8 | Reviewer comments received |
| 8 → Resubmit | Revised manuscript + response letter complete, QC re-run passed |

---

## Natural-language ChatGPT Actions

> 사용자는 slash command를 외울 필요가 없다. 아래 표현을 자연어로 요청하면 ChatGPT가 `chatgpt/actions/` playbook과 관련 문서를 읽고 sSb/mSb를 통해 실행한다.

### Setup & Evidence
| User request example | ChatGPT action |
|---|---|
| `이 주제로 프로젝트 설정해줘` | Research configuration과 폴더 상태 확인/설정 |
| `관련 근거 찾아서 evidence에 등록해줘` | `chatgpt/actions/search-evidence.md` |
| `이 DOI 논문 evidence에 추가해줘` | `chatgpt/actions/import-doi.md` |
| `새 PDF 처리해줘` | `knowledge/pdf/` 확인 → evidence registry 반영 |

### Analysis & Planning
| User request example | ChatGPT action |
|---|---|
| `데이터 분석 계획 만들어줘` | `data/analysis_plan.md` 작성; 사용자 승인 전 분석 금지 |
| `이 analysis plan대로 분석해` | 승인 확인 후 `data/py/` 실행 → `results/` 생성 |
| `draft plan 만들어줘` | `docs/draft_plan_template.md` 기반 `drafts/draft_plan.md` 작성 |
| `basic research story map 만들어줘` / `figure story 짜줘` | `chatgpt/actions/build-story-map.md` → `drafts/story_map.md` |
| `논문 방향을 토론해봐` | `chatgpt/actions/paper-debate.md` |

### Drafting & Style
| User request example | ChatGPT action |
|---|---|
| `Methods 작성해` / `Discussion 작성해` | 승인된 draft plan에 맞춰 해당 섹션 작성 |
| `학술적으로 다듬어줘` / `저널 스타일로 바꿔줘` | `chatgpt/actions/style-pass.md` |
| `이 claim에 맞는 reference 찾아줘` | `chatgpt/actions/suggest-citation.md` |

### QC & Review
| User request example | ChatGPT action |
|---|---|
| `전체 검증해` | `chatgpt/actions/verify.md` + deterministic checkers + semantic verifier |
| `claim별 citation 검증해` | `chatgpt/actions/verify-claims.md` |
| `인용이 균형적인지 봐줘` | `chatgpt/actions/cite-stance.md` |
| `근거 비교표 만들어줘` | `chatgpt/actions/evidence-table.md` |
| `critical review 해` | `chatgpt/actions/critical-review.md` |
| `editor review 해` | `chatgpt/actions/editor-review.md` |
| `oncology checklist 돌려` | `docs/oncology_checklist.md` 적용 |
| `mechanism이 충분한지 봐줘` / `basic research audit 해` | `chatgpt/actions/audit-mechanism.md` + `docs/basic_research_checklist.md` |

### Revision & Finalization
| User request example | ChatGPT action |
|---|---|
| `reviewer comments 분석해` | comment triage + revision plan |
| `response letter 작성해` | response template + `[CHANGE]` tracking |
| `response coverage 검사해` | `check_response_coverage.py` + `check_revision_claims.py` |
| `최종 DOCX 만들어줘` | `docs/docx_guide.md`에 따라 output 생성 |
| `reference를 저널 형식으로 바꿔줘` | `scripts/format_references.py` 실행 |

### Core verification commands used by ChatGPT through Shellby

```bash
python3 scripts/check_citations.py drafts/03_introduction.md --evidence knowledge/evidence.md
python3 scripts/check_numbers.py drafts/05_results.md drafts/table_1.md --results results
python3 scripts/check_abstract.py drafts/04_methods.md drafts/05_results.md drafts/table_1.md drafts/table_2.md --abstract drafts/02_abstract.md
python3 scripts/check_crossrefs.py drafts/05_results.md drafts/06_discussion.md
python3 scripts/check_abbreviations.py drafts/02_abstract.md drafts/03_introduction.md drafts/04_methods.md drafts/05_results.md drafts/06_discussion.md
```

---

## Notes

### Key Reminders
- Detailed guides in `docs/` folder - read as needed to save context
- Always verify AI-generated citations against actual sources
- Minimum 3 QC rounds mandatory before submission
- Human expert review mandatory before submission

### PubMed Search Tool

`scripts/search_pubmed.py` - NCBI E-utilities API 직접 호출 (MCP 불필요, 외부 패키지 불필요)

**CLI 직접 사용:**

```bash
python3 scripts/search_pubmed.py search "query"           # 검색 (테이블 출력)
python3 scripts/search_pubmed.py fetch <PMID> [PMID2...]  # PMID로 가져오기
python3 scripts/search_pubmed.py doi <DOI>                # DOI로 가져오기
python3 scripts/search_pubmed.py related <PMID>           # 관련 논문 검색
```

**옵션:**
- `--max N`: 최대 결과 수 (기본 20)
- `--sort relevance|pub_date`: 정렬 기준
- `--format table|evidence|json`: 출력 형식
- `--start-num N`: evidence 형식 시작 번호

**ChatGPT action playbooks:**

- `chatgpt/actions/search-evidence.md`: 검색 → 선택 → abstract 기반 TODO 채우기 → evidence.md 등록
- `chatgpt/actions/import-doi.md`: DOI → evidence.md 등록

### Expert Simulation
When drafting, invoke experts from `docs/expert_roles.md`:
- **Dr. Researcher A**: Clinical perspective (Introduction, Discussion)
- **Dr. Researcher B**: Methodology (Methods, Results, Tables)
- **Dr. Statistician**: Statistical validation
- **Dr. Editor**: Final polish, consistency check

### Statistical Analysis (Phase 2)

> 워크플로·검정 선택은 Recommended Workflow Phase 2 + `docs/statistical_analysis_guide.md`(§1 워크플로, §5 검정 선택) 참조. 핵심: 분석 전 `analysis_plan.md` 필수(Rule 7, ChatGPT가 명시적으로 강제) → `data/py/` 스크립트 → `results/` CSV → table/figure (Table↔Figure 중복 확인).
