import hashlib
import uuid

from qdrant_client import QdrantClient, models
from langchain_qdrant import QdrantVectorStore

from app.embeddings.embedder import get_embeddings


QDRANT_URL = "http://localhost:6333"
COLLECTION_NAME = "rag_documents"


def get_vector_store():
    """Connect to the existing Qdrant collection."""

    embeddings = get_embeddings()
    client = QdrantClient(url=QDRANT_URL)

    if not client.collection_exists(COLLECTION_NAME):
        vector_size = len(
            embeddings.embed_query("RAG initialization")
        )

        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=models.VectorParams(
                size=vector_size,
                distance=models.Distance.COSINE,
            ),
        )

    return QdrantVectorStore(
        client=client,
        collection_name=COLLECTION_NAME,
        embedding=embeddings,
    )


def store_documents(documents):
    """Embed and store document chunks in Qdrant."""

    if not documents:
        raise ValueError("No documents provided.")

    vector_store = get_vector_store()

    ids = []

    for document in documents:
        content = document.page_content

        identity = (
            f"{document.metadata.get('source', '')}:"
            f"{document.metadata.get('page', '')}:"
            f"{document.metadata.get('chunk_id', '')}:"
            f"{content}"
        )

        digest = hashlib.sha256(identity.encode("utf-8")).hexdigest()
        ids.append(str(uuid.UUID(digest[:32])))

    vector_store.add_documents(
        documents=documents,
        ids=ids,
    )

    return vector_store

def search_documents(question: str, top_k: int = 4):
    """Retrieve the most relevant document chunks."""

    if not question.strip():
        raise ValueError("Question cannot be empty.")

    vector_store = get_vector_store()

    return vector_store.similarity_search(
        query=question,
        k=top_k,
    )

def reset_collection():
    """Delete and recreate the RAG collection."""

    client = QdrantClient(url=QDRANT_URL)

    if client.collection_exists(COLLECTION_NAME):
        client.delete_collection(COLLECTION_NAME)

    embeddings = get_embeddings()

    vector_size = len(
        embeddings.embed_query("RAG initialization")
    )

    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=models.VectorParams(
            size=vector_size,
            distance=models.Distance.COSINE,
        ),
    )
