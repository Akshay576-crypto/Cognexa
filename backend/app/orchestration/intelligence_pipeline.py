from typing import Any, Dict, Optional
from app.schemas.intelligence_result_schema import IntelligenceResult
from app.agents.research_agent import ResearchAgent
from app.agents.consulting_agent import ConsultingAgent
from app.services.intelligence_output_service import IntelligenceOutputService

class IntelligencePipeline:
    """
    Cognexa Intelligence Pipeline.

    Orchestrates the high-level intelligence flow:

        User Question
              ↓
        ResearchAgent
              ↓
        Research Evidence
              ↓
        ConsultingAgent
              ↓
        Structured Consulting Intelligence

    This class coordinates existing Cognexa components.
    It does not duplicate research or consulting logic.

    It does NOT:
    - Perform research itself
    - Perform web searches
    - Perform document retrieval
    - Perform LLM reasoning itself
    - Calculate analytics
    - Render charts
    - Render tables
    - Render dashboards
    """

    def __init__(
    self,
    research_agent: Optional[ResearchAgent] = None,
    consulting_agent: Optional[ConsultingAgent] = None,
    output_service: Optional[IntelligenceOutputService] = None,
    ):
        self.research_agent = (
            research_agent or ResearchAgent()
        )

        self.consulting_agent = (
            consulting_agent or ConsultingAgent()
        )

        self.output_service = (
            output_service or IntelligenceOutputService()
        )
    def research(
        self,
        question: str,
        document_id: Optional[int] = None,
        top_k: int = 5,
    ) -> str:
        """
        Execute the research stage.
        """

        question = question.strip()

        if not question:
            raise ValueError(
                "Research question cannot be empty."
            )

        return self.research_agent.answer(
            question=question,
            document_id=document_id,
            top_k=top_k,
        )

    def consult(
        self,
        question: str,
        research_evidence: str,
        sources: str = "",
    ):
        """
        Execute the consulting stage using research evidence.
        """

        question = question.strip()
        research_evidence = research_evidence.strip()

        if not question:
            raise ValueError(
                "Consulting question cannot be empty."
            )

        if not research_evidence:
            raise ValueError(
                "Research evidence cannot be empty."
            )

        return self.consulting_agent.analyze_structured(
            question=question,
            context=research_evidence,
            sources=sources,
        )

    def run_research(
        self,
        question: str,
        document_id: Optional[int] = None,
        top_k: int = 5,
    ) -> Dict[str, Any]:
        """
        Execute the research stage and return
        a standardized pipeline result.
        """

        research_evidence = self.research(
            question=question,
            document_id=document_id,
            top_k=top_k,
        )

        return {
            "question": question,
            "research": {
                "evidence": research_evidence,
            },
        }

    def run(
    self,
    question: str,
    document_id: Optional[int] = None,
    top_k: int = 5,
    sources: str = "",
    ) -> IntelligenceResult:
        """
        Execute the Cognexa intelligence pipeline.

        Current pipeline:

            Question
                ↓
            ResearchAgent
                ↓
            Research Evidence
                ↓
            ConsultingAgent
                ↓
            IntelligenceResult
        """

        question = question.strip()

        if not question:
            raise ValueError(
                "Pipeline question cannot be empty."
            )

        # ---------------------------------------------------------
        # RESEARCH
        # ---------------------------------------------------------

        research_evidence = self.research(
            question=question,
            document_id=document_id,
            top_k=top_k,
        )

        # ---------------------------------------------------------
        # CONSULTING
        # ---------------------------------------------------------

        # ---------------------------------------------------------
        # CONSULTING
        # ---------------------------------------------------------

        consulting_result = self.consult(
            question=question,
            research_evidence=research_evidence,
            sources=sources,
        )

        # ---------------------------------------------------------
        # INTELLIGENCE OUTPUT
        # ---------------------------------------------------------

        intelligence_output = (
            self.output_service.build_from_consulting_result(
                consulting_result
            )
        )

        # ---------------------------------------------------------
        # CANONICAL INTELLIGENCE RESULT
        # ---------------------------------------------------------

        return IntelligenceResult(
            question=question,
            research={
                "evidence": research_evidence,
            },
            consulting=consulting_result,
            analytics=intelligence_output.get(
                "analytics",
                {},
            ),
            charts=intelligence_output.get(
                "charts",
                {},
            ).get(
                "charts",
                [],
            ),
            tables=intelligence_output.get(
                "tables",
                {},
            ).get(
                "tables",
                [],
            ),
        )