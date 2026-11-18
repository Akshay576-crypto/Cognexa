from types import SimpleNamespace

import pytest

from app.pipeline import rag_chain


class MockChatModel:
    def invoke(self, messages):
        self.messages = messages
        return SimpleNamespace(
            content="The document describes AI and ML product concepts."
        )


def test_rag_question_answering(monkeypatch):
    documents = [
        SimpleNamespace(
            page_content="The document describes AI and ML products.",
            metadata={"source": "sample.pdf", "page": 1},
        ),
        SimpleNamespace(
            page_content="It also discusses intelligent automation.",
            metadata={"source": "sample.pdf", "page": 1},
        ),
        SimpleNamespace(
            page_content="It explains machine learning applications.",
            metadata={"source": "sample.pdf", "page": 2},
        ),
    ]

    mock_model = MockChatModel()

    monkeypatch.setattr(
        rag_chain,
        "search_documents",
        lambda question, top_k: documents,
    )

    monkeypatch.setattr(
        rag_chain,
        "get_chat_model",
        lambda: mock_model,
    )

    result = rag_chain.ask_question(
        "What AI/ML concepts are described?",
        top_k=4,
    )

    assert result["answer"]
    assert result["answer"] == (
        "The document describes AI and ML product concepts."
    )

    assert result["sources"] == [
        {"source": "sample.pdf", "page": 1},
        {"source": "sample.pdf", "page": 2},
    ]

    assert len(mock_model.messages) == 2


def test_empty_question():
    with pytest.raises(ValueError, match="Question cannot be empty"):
        rag_chain.ask_question("   ")


def test_no_relevant_documents(monkeypatch):
    monkeypatch.setattr(
        rag_chain,
        "search_documents",
        lambda question, top_k: [],
    )

    def unexpected_model_call():
        raise AssertionError("LLM should not be called")

    monkeypatch.setattr(
        rag_chain,
        "get_chat_model",
        unexpected_model_call,
    )

    result = rag_chain.ask_question("Unknown topic")

    assert result == {
        "answer": "No relevant information was found.",
        "sources": [],
    }
