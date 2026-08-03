from langchain_core.tools import tool

from app.services.retrival_service import RetrievalService
from app.services.context_builder_service import ContextBuilderService


retrieval_service = RetrievalService()
context_builder = ContextBuilderService(
    max_tokens=2500
)


@tool
def retrieval_tool(
    question: str,
    document_id: int | None = None,
    top_k: int = 5
) -> str:
    """
    Search Cognexa's internal knowledge using HARE.

    Use this tool when the user asks a question
    that requires information from uploaded documents.
    """

    results = retrieval_service.retrieve(
        question=question,
        document_id=document_id,
        top_k=top_k
    )

    context_chunks = context_builder.build_context(
        results
    )

    return context_builder.format_context(
        context_chunks
    )