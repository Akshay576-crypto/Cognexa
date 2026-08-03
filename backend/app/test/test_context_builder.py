from app.services.retrival_service import RetrievalService
from app.services.context_builder_service import ContextBuilderService
from app.services.retrival_service import RetrievalService
from app.services.context_builder_service import ContextBuilderService


retrieval_service = RetrievalService()
context_builder = ContextBuilderService(max_tokens=2500)


results = retrieval_service.retrieve(
    question="How does HAC work?",
    document_id=7,
    top_k=5
)


context = context_builder.build_context(results)


print("\n===== FINAL CONTEXT =====\n")

total_tokens = 0

for chunk in context:

    print(f"Document ID : {chunk['document_id']}")
    print(f"Chunk Index : {chunk['chunk_index']}")
    print(f"Score       : {chunk['score']}")
    print(f"Token Count : {chunk['token_count']}")
    print(f"Text        : {chunk['chunk_text']}")
    print("-" * 60)

    total_tokens += chunk["token_count"]


print(f"\nTotal Context Tokens: {total_tokens}")


retrieval_service = RetrievalService()
context_builder = ContextBuilderService(max_tokens=2500)


results = retrieval_service.retrieve(
    question="How does HAC work?",
    document_id=7,
    top_k=5
)


context_chunks = context_builder.build_context(results)

formatted_context = context_builder.format_context(
    context_chunks
)

print("\n===== LLM READY CONTEXT =====\n")
print(formatted_context)