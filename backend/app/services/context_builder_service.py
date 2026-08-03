class ContextBuilderService:
    """
    HARE Context Builder.

    Converts retrieved Qdrant results into
    structured context while respecting a
    maximum token budget.
    """

    def __init__(self, max_tokens: int = 2500):

        self.max_tokens = max_tokens

    def build_context(self, results):

        context_chunks = []
        seen_chunks = set()

        total_tokens = 0

        for result in results:

            payload = result.payload

            document_id = payload.get("document_id")
            chunk_index = payload.get("chunk_index")
            chunk_text = payload.get("chunk_text")
            token_count = payload.get("token_count", 0)

            # Prevent duplicate chunks
            chunk_key = (document_id, chunk_index)

            if chunk_key in seen_chunks:
                continue

            # Stop if adding this chunk exceeds the budget
            if total_tokens + token_count > self.max_tokens:
                continue

            context_chunks.append(
                {
                    "document_id": document_id,
                    "chunk_index": chunk_index,
                    "score": result.score,
                    "chunk_text": chunk_text,
                    "token_count": token_count,
                }
            )

            seen_chunks.add(chunk_key)

            total_tokens += token_count

        return context_chunks

    def format_context(self, context_chunks):

        if not context_chunks:
            return "CONTEXT:\n\nNo relevant context found."

        formatted_parts = ["CONTEXT:"]

        for chunk in context_chunks:

            header = (
                f"[Document {chunk['document_id']} | "
                f"Chunk {chunk['chunk_index']} | "
                f"Relevance: {chunk['score']:.4f}]"
            )

            formatted_parts.append(
                f"{header}\n\n"
                f"{chunk['chunk_text']}"
            )

        return "\n\n---\n\n".join(formatted_parts)