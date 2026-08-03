import json
import re

from app.services.llm_service import LLMService


class ToolRouterService:
    """
    Project Helix Tool Router.

    Uses the LLM to decide which research capability
    should be used without relying on native Ollama
    tool-calling support.

    Supported routes:
        - retrieval_tool
        - web_search_tool
        - yahoo_finance_tool
        - direct_answer
    """

    VALID_TOOLS = {
        "retrieval_tool",
        "web_search_tool",
        "yahoo_finance_tool",
        "direct_answer",
    }

    def __init__(
        self,
        model: str = "gemma3:4b",
    ):
        self.llm_service = LLMService(
            model=model,
            temperature=0.0,
        )

    def route(
        self,
        question: str,
        document_id: int | None = None,
        top_k: int = 5,
    ) -> dict:
        """
        Decide which tool should handle the question.
        """

        question = question.strip()

        if not question:
            return {
                "tool": "direct_answer",
                "arguments": {
                    "question": question
                },
                "reason": "Empty question.",
            }

        prompt = f"""
You are the Project Helix Tool Router.

Your job is ONLY to decide which capability should
handle the user's research question.

Available capabilities:

1. retrieval_tool

Use when the question requires information from
Cognexa's uploaded/internal documents.

2. web_search_tool

Use when the question requires current external
information, recent news, market research, public
information, companies, industries, or live web data.

3. yahoo_finance_tool

Use when the question requires financial or stock-market
information about a publicly traded company.

4. direct_answer

Use when the question can be answered directly without
retrieving external or internal evidence.

Return ONLY valid JSON.

Required JSON format:

{{
    "tool": "retrieval_tool",
    "arguments": {{}},
    "reason": "short explanation"
}}

Rules:

- Never return markdown.
- Never return code fences.
- Never invent a stock symbol.
- For retrieval_tool include:
  "question", "document_id", and "top_k".
- For web_search_tool include:
  "query" and "max_results".
- For yahoo_finance_tool include:
  "symbol".
- For direct_answer include:
  "question".

User question:

{question}

Document ID:
{document_id}

Top K:
{top_k}
"""

        response = self.llm_service.generate(
            prompt
        )

        parsed = self._parse_response(
            response
        )

        return self._validate_route(
            parsed,
            question=question,
            document_id=document_id,
            top_k=top_k,
        )

    # ---------------------------------------------------------
    # RESPONSE PARSING
    # ---------------------------------------------------------

    def _parse_response(
        self,
        response: str,
    ) -> dict:
        """
        Parse JSON returned by the LLM.
        """

        response = response.strip()

        # Remove accidental markdown fences.
        response = re.sub(
            r"^```(?:json)?\s*",
            "",
            response,
            flags=re.IGNORECASE,
        )

        response = re.sub(
            r"\s*```$",
            "",
            response,
            flags=re.IGNORECASE,
        )

        try:
            return json.loads(response)

        except json.JSONDecodeError:

            # Try to recover the first JSON object.
            match = re.search(
                r"\{.*\}",
                response,
                flags=re.DOTALL,
            )

            if match:
                try:
                    return json.loads(
                        match.group(0)
                    )
                except json.JSONDecodeError:
                    pass

        return {
            "tool": "direct_answer",
            "arguments": {},
            "reason": (
                "Router returned invalid JSON."
            ),
        }

    # ---------------------------------------------------------
    # VALIDATION
    # ---------------------------------------------------------

    def _validate_route(
        self,
        route: dict,
        question: str,
        document_id: int | None,
        top_k: int,
    ) -> dict:

        tool_name = route.get(
            "tool",
            "direct_answer",
        )

        if tool_name not in self.VALID_TOOLS:
            return {
                "tool": "direct_answer",
                "arguments": {
                    "question": question
                },
                "reason": (
                    "Invalid tool selected by router."
                ),
            }

        arguments = route.get(
            "arguments",
            {}
        )

        if not isinstance(arguments, dict):
            arguments = {}

        # -----------------------------------------------------
        # RETRIEVAL
        # -----------------------------------------------------

        if tool_name == "retrieval_tool":

            return {
                "tool": tool_name,
                "arguments": {
                    "question": question,
                    "document_id": document_id,
                    "top_k": top_k,
                },
                "reason": route.get(
                    "reason",
                    "Internal document retrieval selected."
                ),
            }

        # -----------------------------------------------------
        # WEB SEARCH
        # -----------------------------------------------------

        if tool_name == "web_search_tool":

            query = arguments.get(
                "query",
                question,
            )

            max_results = arguments.get(
                "max_results",
                8,
            )

            try:
                max_results = int(
                    max_results
                )
            except (TypeError, ValueError):
                max_results = 8

            max_results = max(
                1,
                min(max_results, 20),
            )

            return {
                "tool": tool_name,
                "arguments": {
                    "query": query,
                    "max_results": max_results,
                },
                "reason": route.get(
                    "reason",
                    "Web search selected."
                ),
            }

        # -----------------------------------------------------
        # YAHOO FINANCE
        # -----------------------------------------------------

        if tool_name == "yahoo_finance_tool":

            symbol = arguments.get(
                "symbol"
            )

            if not symbol:
                return {
                    "tool": "direct_answer",
                    "arguments": {
                        "question": question
                    },
                    "reason": (
                        "Finance tool selected without "
                        "a valid stock symbol."
                    ),
                }

            return {
                "tool": tool_name,
                "arguments": {
                    "symbol": str(
                        symbol
                    ).strip().upper()
                },
                "reason": route.get(
                    "reason",
                    "Financial research selected."
                ),
            }

        # -----------------------------------------------------
        # DIRECT ANSWER
        # -----------------------------------------------------

        return {
            "tool": "direct_answer",
            "arguments": {
                "question": question
            },
            "reason": route.get(
                "reason",
                "Direct answer selected."
            ),
        }

