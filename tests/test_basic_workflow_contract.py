from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def test_basic_workflow_required_files_exist() -> None:
    required = [
        "docs/basic_research_analysis_guide.md",
        "docs/basic_research_guide.md",
        "docs/basic_research_checklist.md",
        "docs/basic_section_templates.md",
        "docs/experimental_evidence_guide.md",
        "docs/figure_story_guide.md",
        "chatgpt/actions/build-story-map.md",
        "chatgpt/actions/audit-mechanism.md",
        "drafts/_templates/basic_methods.md",
        "drafts/_templates/basic_results.md",
        "profile.example/authors.example.md",
        "profile.example/journals.example.md",
    ]
    assert all((ROOT / path).exists() for path in required)


def test_analysis_plan_routes_clinical_and_basic_conditionally() -> None:
    text = read("data/analysis_plan.md")
    assert "## 2A. Clinical / Clinical-Translational Design" in text
    assert "## 2B. Basic / Mechanistic Experimental Design" in text
    assert "Clinical / Clinical-Translational only" in text
    assert "Basic / Mechanistic only" in text
    assert "Experimental-design constants" in text


def test_mechanism_audit_is_full_at_phase3_and_phase6_not_every_phase4_section() -> None:
    verification = read("docs/verification_protocol.md")
    drafting = read("docs/drafting_protocol.md")
    action = read("chatgpt/actions/verify.md")
    assert "Phase 3와 Phase 6" in verification
    assert "targeted mechanism re-audit" in drafting
    assert "Routine section drafting does not require a full mechanism audit after every section" in drafting
    assert "mandatory at **Phase 3** and **Phase 6**" in action


def test_citation_routing_is_pubmed_first_for_breast_basic_work() -> None:
    protocol = read("docs/citation_assist_protocol.md")
    legacy = read("docs/medical_kag_protocol.md")
    assert "PubMed-first discovery" in protocol
    assert "Do **not** make it the primary retrieval route for breast oncology" in protocol
    assert "spine-surgery-specific" in legacy
    assert "not** the primary evidence route for breast oncology" in legacy


def test_user_docs_are_v030_and_describe_basic_layer() -> None:
    for rel in ["README.md", "README.ko.md", "README.ja.md", "README.zh.md"]:
        text = read(rel)
        assert "v0.3.0" in text
        assert "basic" in text.lower()
    assert "v0.3.0" in read("docs/customization.md")


def test_qc_has_no_arbitrary_selfcitation_or_recency_thresholds() -> None:
    text = read("docs/qc_guide.md")
    assert "Self-citation 비율이 전체의 20% 이하" not in text
    assert "최근 5년 이내 문헌이 전체의 50% 이상" not in text
    assert "임의 cutoff" in text


def test_verifier_passes_do_not_require_subagents() -> None:
    agents = read("AGENTS.MD")
    protocol = read("docs/verification_protocol.md")
    assert "subagents **in parallel**" not in agents
    assert "fresh-context sSb/mSb subagents or second-model reviewers are optional" in agents
    assert "fresh-context reviewer를 추가할 수 있으나 필수는 아니다" in protocol


def test_core_execution_examples_are_macos_bash_paths() -> None:
    files = [
        "docs/verification_protocol.md",
        "docs/drafting_protocol.md",
        "review/gates/_TEMPLATE.GATE.md",
        "docs/verifier_prompt_templates.md",
        "docs/revision_guide.md",
        "docs/response_letter_template.md",
        "docs/docx_guide.md",
    ]
    for rel in files:
        text = read(rel)
        assert "```powershell" not in text, rel
        assert "review/gates\\" not in text, rel
        assert "drafts/revision\\REV1\\" not in text, rel


def test_verification_protocol_version_matches_workflow() -> None:
    assert "(v0.3.0)" in read("docs/verification_protocol.md").splitlines()[0]
