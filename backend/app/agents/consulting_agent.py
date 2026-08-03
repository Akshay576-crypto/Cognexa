import json
from pathlib import Path

from langchain_core.messages import HumanMessage, SystemMessage

from app.services.llm_service import LLMService
from app.schemas.consulting_result_schema import ConsultingResult


class ConsultingAgent:
    """
    Cognexa Consulting Intelligence Engine.

    Responsibilities:
    - Transform research evidence into business analysis.
    - Distinguish facts, analysis, assumptions, and recommendations.
    - Identify KPIs, risks, opportunities, and strategic options.
    - Produce structured consulting intelligence.

    Does NOT:
    - Perform web searching.
    - Perform document retrieval.
    - Execute research tools.
    - Generate PPTX files.
    - Generate PDF files.
    """

    def __init__(
        self,
        model: str = "qwen2.5:7b",
    ):
        self.llm_service = LLMService(
            model=model,
            temperature=0.2,
        )

        # ---------------------------------------------------------
        # PROMPTS
        # ---------------------------------------------------------

        self.app_dir = Path(__file__).resolve().parents[1]
        self.prompts_dir = self.app_dir / "prompts"

        self.system_prompt = self._load_prompt(
            "consulting_system.txt"
        )

        self.user_prompt_template = self._load_prompt(
            "consulting_user.txt"
        )

    # -------------------------------------------------------------
    # PROMPT LOADING
    # -------------------------------------------------------------

    def _load_prompt(
        self,
        filename: str,
    ) -> str:
        """
        Load a consulting prompt from app/prompts.
        """

        prompt_path = self.prompts_dir / filename

        if not prompt_path.exists():
            raise FileNotFoundError(
                f"Prompt file not found: {prompt_path}"
            )

        return prompt_path.read_text(
            encoding="utf-8"
        )

    # -------------------------------------------------------------
    # INPUT VALIDATION
    # -------------------------------------------------------------

    def _validate_inputs(
        self,
        question: str,
        context: str,
    ):
        question = question.strip()
        context = context.strip()

        if not question:
            return (
                question,
                context,
                "Consulting question cannot be empty.",
            )

        if not context:
            return (
                question,
                context,
                "Research evidence cannot be empty.",
            )

        return question, context, None

    # -------------------------------------------------------------
    # CONSULTING ANALYSIS
    # -------------------------------------------------------------

    def analyze(
        self,
        question: str,
        context: str,
        sources: str = "",
    ) -> str:
        """
        Transform research evidence into consulting analysis.

        Returns the existing human-readable consulting response.
        """

        question, context, error = self._validate_inputs(
            question,
            context,
        )

        if error:
            return error

        sources = sources.strip()

        user_prompt = self.user_prompt_template.format(
            question=question,
            context=context,
            sources=sources,
        )

        messages = [
            SystemMessage(
                content=self.system_prompt
            ),
            HumanMessage(
                content=user_prompt
            ),
        ]

        return self.llm_service.generate_with_messages(
            messages
        )

    # -------------------------------------------------------------
    # STRUCTURED CONSULTING ANALYSIS
    # -------------------------------------------------------------

    def analyze_structured(
        self,
        question: str,
        context: str,
        sources: str = "",
    ) -> ConsultingResult:
        """
        Transform research evidence into structured
        Cognexa consulting intelligence.

        The LLM produces JSON which is validated by
        the ConsultingResult Pydantic schema.
        """

        question, context, error = self._validate_inputs(
            question,
            context,
        )

        if error:
            raise ValueError(error)

        sources = sources.strip()

        user_prompt = self.user_prompt_template.format(
            question=question,
            context=context,
            sources=sources,
        )

        structured_instruction = """
IMPORTANT OUTPUT REQUIREMENT

Return ONLY valid JSON.

Do not use Markdown.
Do not use ```json.
Do not add explanations before or after the JSON.

The JSON must follow this structure:

{
    "question": "string",
    "executive_summary": "string",
    "problem_definition": "string",
    "findings": [],
    "kpis": [],
    "trends": [],
    "comparisons": [],
    "opportunities": [],
    "risks": [],
    "recommendations": [],
    "data_limitations": [],
    "sources": []
}

For missing information, use empty arrays or empty strings.

Do not invent evidence, metrics, sources, URLs,
market figures, or numerical values.

Only include KPIs, trends, comparisons, opportunities,
and risks that are supported by the supplied evidence.

Return valid JSON only.
"""

        final_prompt = (
            f"{user_prompt}\n\n"
            "==================================================\n"
            "STRUCTURED OUTPUT INSTRUCTIONS\n"
            "==================================================\n"
            f"{structured_instruction}"
        )

        messages = [
            SystemMessage(
                content=self.system_prompt
            ),
            HumanMessage(
                content=final_prompt
            ),
        ]

        raw_response = self.llm_service.generate_with_messages(
            messages
        )

        # ---------------------------------------------------------
        # JSON CLEANING
        # ---------------------------------------------------------

        cleaned_response = raw_response.strip()

        if cleaned_response.startswith("```"):
            cleaned_response = cleaned_response.replace(
                "```json",
                "",
                1,
            ).replace(
                "```",
                "",
                1,
            ).strip()

        # ---------------------------------------------------------
        # JSON PARSING
        # ---------------------------------------------------------

        try:
            structured_data = json.loads(
                cleaned_response
            )
        except json.JSONDecodeError as exc:
            raise ValueError(
                "ConsultingAgent returned invalid JSON."
            ) from exc

        # ---------------------------------------------------------
        # PYDANTIC VALIDATION
        # ---------------------------------------------------------

        try:
            return ConsultingResult.model_validate(
                structured_data
            )
        except Exception as exc:
            raise ValueError(
                "ConsultingAgent returned JSON that does "
                "not match ConsultingResult schema."
            ) from exc