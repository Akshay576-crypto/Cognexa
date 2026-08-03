from app.services.embedding_service import EmbeddingService
from app.repositories.vector_repositories import VectorRepository

class RetrievalService:
    """
    HARE Retrieval Service.
    Responsible for semantic document retrieval.
    """

    def __init__(self):

        self.embedding_service = EmbeddingService()
        self.vector_repository = VectorRepository()

    def retrieve(
        self,
        question: str,
        document_id: int | None = None,
        top_k: int = 5
    ):

        query_embedding = self.embedding_service.generate_embedding(
            question
        )

        results = self.vector_repository.search_embeddings(
            query_embedding=query_embedding,
            limit=top_k,
            document_id=document_id
        )

        return results