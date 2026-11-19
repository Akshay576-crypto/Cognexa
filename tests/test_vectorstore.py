import hashlib
import uuid
from types import SimpleNamespace

import pytest

from app.vectorstore import qdrant_store


class MockVectorStore:
    def __init__(self):
        self.added_documents = None
        self.added_ids = None
        self.search_query = None
        self.search_k = None

    def add_documents(self, documents, ids):
        self.added_documents = documents
        self.added_ids = ids

    def similarity_search(self, query, k):
        self.search_query = query
        self.search_k = k
        return [
            SimpleNamespace(
                page_content="Retrieved document content.",
                metadata={"source": "sample.pdf", "page": 1},
            )
        ]


def test_store_documents(monkeypatch):
    documents = [
        SimpleNamespace(
            page_content="Sample document content.",
            metadata={
                "source": "sample.pdf",
                "page": 1,
                "chunk_id": 0,
            },
        )
    ]

    mock_store = MockVectorStore()

    monkeypatch.setattr(
        qdrant_store,
        "get_vector_store",
        lambda: mock_store,
    )

    result = qdrant_store.store_documents(documents)

    assert result is mock_store
    assert mock_store.added_documents == documents
    assert len(mock_store.added_ids) == 1

    identity = "sample.pdf:1:0:Sample document content."
    digest = hashlib.sha256(identity.encode("utf-8")).hexdigest()
    expected_id = str(uuid.UUID(digest[:32]))

    assert mock_store.added_ids[0] == expected_id


def test_store_documents_empty_input():
    with pytest.raises(ValueError, match="No documents provided"):
        qdrant_store.store_documents([])


def test_search_documents(monkeypatch):
    mock_store = MockVectorStore()

    monkeypatch.setattr(
        qdrant_store,
        "get_vector_store",
        lambda: mock_store,
    )

    results = qdrant_store.search_documents(
        "What is in the document?",
        top_k=5,
    )

    assert len(results) == 1
    assert results[0].page_content == "Retrieved document content."
    assert mock_store.search_query == "What is in the document?"
    assert mock_store.search_k == 5


def test_search_documents_empty_question():
    with pytest.raises(ValueError, match="Question cannot be empty"):
        qdrant_store.search_documents("   ")
