from app.orchestration.intelligence_pipeline import IntelligencePipeline
from app.schemas.consulting_result_schema import ConsultingResult

class FakeResearchAgent:
    def __init__(self):
        self.calls = []

    def answer(
        self,
        question,
        document_id=None,
        top_k=5,
    ):
        self.calls.append(
            {
                "question": question,
                "document_id": document_id,
                "top_k": top_k,
            }
        )

        return "Research evidence for testing."


class FakeConsultingAgent:
    def __init__(self):
        self.calls = []

    def analyze_structured(
        self,
        question,
        context,
        sources="",
    ):
        self.calls.append(
            {
                "question": question,
                "context": context,
                "sources": sources,
            }
        )

        return ConsultingResult(
    question=question,
    executive_summary="Test consulting result.",
    )


def create_pipeline():
    research_agent = FakeResearchAgent()
    consulting_agent = FakeConsultingAgent()

    pipeline = IntelligencePipeline(
        research_agent=research_agent,
        consulting_agent=consulting_agent,
    )

    return pipeline, research_agent, consulting_agent


def test_research_stage():
    pipeline, research_agent, _ = create_pipeline()

    result = pipeline.research(
        question="What is HAC?",
        document_id=7,
        top_k=5,
    )

    assert result == "Research evidence for testing."

    assert research_agent.calls == [
        {
            "question": "What is HAC?",
            "document_id": 7,
            "top_k": 5,
        }
    ]


def test_research_rejects_empty_question():
    pipeline, _, _ = create_pipeline()

    try:
        pipeline.research("")
        assert False
    except ValueError as exc:
        assert str(exc) == "Research question cannot be empty."


def test_consult_stage():
    pipeline, _, consulting_agent = create_pipeline()

    result = pipeline.consult(
        question="What should Cognexa do?",
        research_evidence="Revenue increased by 25%.",
        sources="Test Report",
    )

    assert result.question == "What should Cognexa do?"
    assert result.executive_summary == "Test consulting result."

    assert consulting_agent.calls == [
        {
            "question": "What should Cognexa do?",
            "context": "Revenue increased by 25%.",
            "sources": "Test Report",
        }
    ]


def test_consult_rejects_empty_question():
    pipeline, _, _ = create_pipeline()

    try:
        pipeline.consult(
            question="",
            research_evidence="Some evidence.",
        )
        assert False
    except ValueError as exc:
        assert str(exc) == "Consulting question cannot be empty."


def test_consult_rejects_empty_evidence():
    pipeline, _, _ = create_pipeline()

    try:
        pipeline.consult(
            question="What happened?",
            research_evidence="",
        )
        assert False
    except ValueError as exc:
        assert str(exc) == "Research evidence cannot be empty."


def test_run_research():
    pipeline, _, _ = create_pipeline()

    result = pipeline.run_research(
        question="What is HARE?",
        document_id=10,
        top_k=3,
    )

    assert result == {
        "question": "What is HARE?",
        "research": {
            "evidence": "Research evidence for testing.",
        },
    }

def test_full_pipeline():
    pipeline, research_agent, consulting_agent = create_pipeline()

    result = pipeline.run(
        question="Analyze the market.",
        document_id=12,
        top_k=5,
        sources="Market Report",
    )

    assert result.question == "Analyze the market."

    assert result.research.evidence == (
        "Research evidence for testing."
    )

    assert result.consulting.question == (
        "Analyze the market."
    )

    assert result.consulting.executive_summary == (
        "Test consulting result."
    )

    assert result.analytics == {}
    assert result.charts == []
    assert result.tables == []

    assert research_agent.calls == [
        {
            "question": "Analyze the market.",
            "document_id": 12,
            "top_k": 5,
        }
    ]

    assert consulting_agent.calls == [
        {
            "question": "Analyze the market.",
            "context": "Research evidence for testing.",
            "sources": "Market Report",
        }
    ]

def test_full_pipeline_rejects_empty_question():
    pipeline, _, _ = create_pipeline()

    try:
        pipeline.run("")
        assert False
    except ValueError as exc:
        assert str(exc) == "Pipeline question cannot be empty."