from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)

from app.config.qdrant import qdrant_client
from qdrant_client.models import Filter, FieldCondition, MatchValue

class VectorRepository:
    """
    Repository responsible for all Qdrant vector operations.
    """

    COLLECTION_NAME = "document_chunks"
    VECTOR_SIZE = 384

    def __init__(self):
        self._create_collection()

    # ---------------------------------------
    # Create Collection
    # ---------------------------------------
    def _create_collection(self):

        collections = qdrant_client.get_collections()

        collection_names = [
            collection.name
            for collection in collections.collections
        ]

        if self.COLLECTION_NAME not in collection_names:

            qdrant_client.create_collection(
                collection_name=self.COLLECTION_NAME,
                vectors_config=VectorParams(
                    size=self.VECTOR_SIZE,
                    distance=Distance.COSINE
                )
            )

            print(" Qdrant Collection Created")

    # ---------------------------------------
    # Save Embeddings
    # ---------------------------------------
    def save_embeddings(
        self,
        document_id: int,
        chunks,
        embeddings: list[list[float]]
    ):

        print("document_id",document_id)
        print("Chunks length",len(chunks))
        print("embedding",len(embeddings))


        points = []

        for chunk, embedding in zip(chunks, embeddings):

            points.append(
                PointStruct(
                    id=document_id * 100000 + chunk.chunk_index,
                    vector=embedding,
                    payload={
                        "document_id": document_id,
                        "chunk_index": chunk.chunk_index,
                        "chunk_text": chunk.chunk_text,
                        "token_count": chunk.token_count
                    }
                )
            )

        print("Points Created",len(points))
        print("Uploading to Qdrant......")

        result = qdrant_client.upsert(
            collection_name=self.COLLECTION_NAME,
            points=points,
            wait=True
        )

        print(result)

        print(f" Stored {len(points)} vectors in Qdrant")

# ---------------------------------------
# Search Embeddings
# ---------------------------------------
   
# ---------------------------------------
# Search Embeddings
# ---------------------------------------
    def search_embeddings(
    self,
    query_embedding: list[float],
    limit: int = 5,
    document_id: int | None = None
):

        search_filter = None

        if document_id is not None:

                search_filter = Filter(
                    must=[
                        FieldCondition(
                            key="document_id",
                            match=MatchValue(
                                value=document_id
                            )
                        )
                    ]
                )

        response = qdrant_client.query_points(
                collection_name=self.COLLECTION_NAME,
                query=query_embedding,
                query_filter=search_filter,
                limit=limit
            )

        return response.points
    # ---------------------------------------
    # Delete Embeddings
    # ---------------------------------------
    
    def delete_embeddings(
        self,
        document_id: int
    ):

        qdrant_client.delete(
            collection_name=self.COLLECTION_NAME,
            points_selector=Filter(
                must=[
                    FieldCondition(
                        key="document_id",
                        match=MatchValue(value=document_id)
                    )
                ]
            )
        )

        print(f"Deleted vectors for document {document_id}")