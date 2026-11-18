from pathlib import Path

from app.ingestion.loader import load_document
from app.ingestion.cleaner import clean_documents
from app.ingestion.chunker import split_documents

from app.vectorstore.qdrant_store import (
    store_documents,
    search_documents,
)


def test_embedding_and_qdrant_storage():

    file_path = Path("data/uploads/sample.pdf")

    assert file_path.exists(), "Sample PDF not found."

    documents = load_document(str(file_path))
    cleaned = clean_documents(documents)
    chunks = split_documents(cleaned)

    vector_store = store_documents(chunks)

    assert vector_store is not None

    results = search_documents(
        "What is the main objective of this document?",
        top_k=4,
    )

    assert len(results) > 0

    print("\n===== QDRANT RETRIEVAL TEST =====")

    for result in results:
        print("\nSource:", result.metadata.get("source"))
        print("Page:", result.metadata.get("page"))
        print("Content:", result.page_content[:250])

    print("\nEMBEDDING AND QDRANT TEST PASSED")

if __name__ == "__main__":
    test_embedding_and_qdrant_storage()