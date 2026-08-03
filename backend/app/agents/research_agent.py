from pathlib import Path

from langchain_core.messages import HumanMessage, SystemMessage

from app.services.llm_service import LLMService
from app.services.tool_router_service import ToolRouterService
from app.services.tool_executer_service import ToolExecutorService


class ResearchAgent:
    """
    Project Helix Research Agent.

    Architecture:

        User Question
              ↓
        ToolRouterService
              ↓
        Gemma 3 4B
              ↓
        Tool Decision
              ↓
        ToolExecutorService
              ↓
        Actual Tool
              ↓
        Evidence
              ↓
        Gemma 3 4B
              ↓
        Final Research Answer

    IMPORTANT:
    This agent intentionally does NOT use native LangChain
    tool calling because Gemma 3 4B does not support
    Ollama native tool calling in our environment.
    """

    def __init__(
        self,
        model: str = "gemma3:4b",
        max_tool_calls: int = 5,
    ):
        self.llm_service = LLMService(
            model=model,
            temperature=0.2,
        )

        self.tool_router = ToolRouterService(
            model=model,
        )

        self.tool_executor = ToolExecutorService()

        self.max_tool_calls = max_tool_calls

        # ---------------------------------------------------------
        # PROMPTS
        # ---------------------------------------------------------

        self.app_dir = Path(__file__).resolve().parents[1]
        self.prompts_dir = self.app_dir / "prompts"

        self.system_prompt = self._load_prompt(
            "research_system.txt"
        )

        self.user_prompt_template = self._load_prompt(
            "research_user.txt"
        )

        self.fallback_prompt = self._load_prompt(
            "fallback.txt"
        )

    # -------------------------------------------------------------
    # PROMPT LOADING
    # -------------------------------------------------------------

    def _load_prompt(self, filename: str) -> str:
        """
        Load a prompt from app/prompts.
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
    # FINAL ANSWER GENERATION
    # -------------------------------------------------------------

    def _generate_final_answer(
        self,
        question: str,
        evidence,
        document_id: int | None,
        top_k: int,
    ) -> str:
        """
        Generate the final research answer using collected evidence.
        """

        user_prompt = self.user_prompt_template.format(
            question=question,
            document_id=document_id,
            top_k=top_k,
        )

        evidence_text = str(evidence)

        final_prompt = (
            f"{user_prompt}\n\n"
            "==================================================\n"
            "RESEARCH EVIDENCE\n"
            "==================================================\n\n"
            f"{evidence_text}\n\n"
            "==================================================\n"
            "INSTRUCTIONS\n"
            "==================================================\n\n"
            "Use the evidence above to answer the research question.\n"
            "Do not invent facts that are not supported by the evidence.\n"
            "Clearly distinguish evidence-based findings from uncertainty.\n"
            "Provide a useful, well-structured research answer."
        )

        messages = [
            SystemMessage(
                content=self.system_prompt
            ),
            HumanMessage(
                content=final_prompt
            ),
        ]

        return self.llm_service.generate_with_messages(
            messages
        )

    # -------------------------------------------------------------
    # FALLBACK
    # -------------------------------------------------------------

    def _fallback_answer(
        self,
        question: str,
    ) -> str:
        """
        Generate a safe fallback answer if routing or execution fails.
        """

        fallback_messages = [
            SystemMessage(
                content=self.system_prompt
            ),
            HumanMessage(
                content=(
                    f"{self.fallback_prompt}\n\n"
                    f"Research Question:\n{question}"
                )
            ),
        ]

        return self.llm_service.generate_with_messages(
            fallback_messages
        )

    # -------------------------------------------------------------
    # ANSWER
    # -------------------------------------------------------------

    def answer(
        self,
        question: str,
        document_id: int | None = None,
        top_k: int = 5,
    ) -> str:
        """
        Answer a research question using Project Helix.

        Flow:

            Question
                ↓
            Tool Router
                ↓
            Tool Decision
                ↓
            Tool Executor
                ↓
            Evidence
                ↓
            Final LLM Synthesis
        """

        question = question.strip()

        if not question:
            return "Research question cannot be empty."

        # ---------------------------------------------------------
        # TOOL ROUTING
        # ---------------------------------------------------------

        try:
            decision = self.tool_router.route(
                question=question,
                document_id=document_id,
                top_k=top_k,
            )

        except Exception:
            return self._fallback_answer(question)

        # ---------------------------------------------------------
        # VALIDATE ROUTER DECISION
        # ---------------------------------------------------------

        if not isinstance(decision, dict):
            return self._fallback_answer(question)

        tool_name = decision.get("tool")

        arguments = decision.get(
            "arguments",
            {},
        )

        if not tool_name:
            return self._fallback_answer(question)

        if not isinstance(arguments, dict):
            arguments = {}

        # ---------------------------------------------------------
        # DIRECT ANSWER
        # ---------------------------------------------------------

        if tool_name == "direct_answer":
            return self._generate_final_answer(
                question=question,
                evidence=(
                    "No external tool was required. "
                    "Answer using the model's general knowledge."
                ),
                document_id=document_id,
                top_k=top_k,
            )

        # ---------------------------------------------------------
        # TOOL EXECUTION
        # ---------------------------------------------------------

        try:
            execution_result = self.tool_executor.execute(
                tool_name=tool_name,
                arguments=arguments,
            )

        except Exception:
            return self._fallback_answer(question)

        # ---------------------------------------------------------
        # EXECUTION FAILURE
        # ---------------------------------------------------------

        if not isinstance(execution_result, dict):
            return self._fallback_answer(question)

        if execution_result.get("success") is False:
            error_message = execution_result.get(
                "error",
                "Tool execution failed.",
            )

            return self._generate_final_answer(
                question=question,
                evidence={
                    "tool": tool_name,
                    "success": False,
                    "error": error_message,
                },
                document_id=document_id,
                top_k=top_k,
            )

        # ---------------------------------------------------------
        # EVIDENCE
        # ---------------------------------------------------------

        evidence = execution_result.get(
            "result",
            execution_result,
        )

        # ---------------------------------------------------------
        # FINAL SYNTHESIS
        # ---------------------------------------------------------

        return self._generate_final_answer(
            question=question,
            evidence={
                "tool": tool_name,
                "router_reason": decision.get(
                    "reason",
                    "",
                ),
                "evidence": evidence,
            },
            document_id=document_id,
            top_k=top_k,
        )