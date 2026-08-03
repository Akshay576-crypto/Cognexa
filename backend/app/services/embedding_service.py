from sentence_transformers import SentenceTransformer


class EmbeddingService:
    """
    Responsible for generating vector embeddings
    from document chunks.
    """

    def __init__(self):
        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def generate_embedding(
        self,
        text: str
    ) -> list[float]:

        embedding = self.model.encode(
            text,
            convert_to_numpy=True
        )

        return embedding.tolist()

    def generate_embeddings(
        self,
        texts: list[str]
    ) -> list[list[float]]:

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True
        )

        return embeddings.tolist()