
from types import SimpleNamespace

import pytest
from langchain_core.documents import Document

from app.ingestion import loader
from app.ingestion.chunker import split_documents
from app.ingestion.cleaner import clean_documents


def test_load_txt_document(tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("Hello RAG pipeline.", encoding="utf-8")

    documents = loader.load_document(str(file_path))

    assert len(documents) == 1
    assert documents[0].page_content == "Hello RAG pipeline."
    assert documents[0].metadata == {
        "source": "sample.txt",
        "page": 1,
        "file_type": "txt",
    }


def test_load_pdf_document(tmp_path, monkeypatch):
    file_path = tmp_path / "sample.pdf"
    file_path.touch()

    pages = [
        SimpleNamespace(extract_text=lambda: "First page content."),
        SimpleNamespace(extract_text=lambda: "Second page content."),
    ]

    monkeypatch.setattr(
        loader,
        "PdfReader",
        lambda path: SimpleNamespace(pages=pages),
    )

    documents = loader.load_document(str(file_path))

    assert len(documents) == 2
    assert documents[0].metadata["page"] == 1
    assert documents[1].metadata["page"] == 2
    assert documents[0].page_content == "First page content."


def test_load_docx_document(tmp_path, monkeypatch):
    file_path = tmp_path / "sample.docx"
    file_path.touch()

    paragraphs = [
        SimpleNamespace(text="First paragraph."),
        SimpleNamespace(text=""),
        SimpleNamespace(text="Second paragraph."),
    ]

    monkeypatch.setattr(
        loader,
        "DocxDocument",
        lambda path: SimpleNamespace(paragraphs=paragraphs),
    )

    documents = loader.load_document(str(file_path))

    assert len(documents) == 1
    assert documents[0].page_content == (
        "First paragraph.\nSecond paragraph."
    )
    assert documents[0].metadata["file_type"] == "docx"


def test_missing_file():
    with pytest.raises(FileNotFoundError):
        loader.load_document("missing_file.txt")


def test_unsupported_file_type(tmp_path):
    file_path = tmp_path / "sample.csv"
    file_path.touch()

    with pytest.raises(ValueError, match="Unsupported file type"):
        loader.load_document(str(file_path))


def test_empty_document(tmp_path):
    file_path = tmp_path / "empty.txt"
    file_path.write_text("   ", encoding="utf-8")

    with pytest.raises(ValueError, match="No readable text"):
        loader.load_document(str(file_path))


def test_clean_documents():
    documents = [
        Document(
            page_content="  Hello   world.\x00\r\n\r\n\r\nSecond line.  ",
            metadata={"source": "sample.txt", "page": 1},
        )
    ]

    cleaned = clean_documents(documents)

    assert len(cleaned) == 1
    assert cleaned[0].page_content == "Hello world.\n\nSecond line."
    assert cleaned[0].metadata == {
        "source": "sample.txt",
        "page": 1,
    }


def test_clean_documents_removes_empty_content():
    documents = [
        Document(page_content="   ", metadata={"page": 1}),
        Document(page_content="\n\n", metadata={"page": 2}),
    ]

    assert clean_documents(documents) == []


def test_clean_documents_preserves_original_metadata():
    metadata = {"source": "sample.pdf", "page": 3}
    document = Document(
        page_content="Original content.",
        metadata=metadata,
    )

    cleaned = clean_documents([document])

    assert cleaned[0].metadata == metadata
    assert cleaned[0].metadata is not metadata


def test_split_documents():
    document = Document(
        page_content="This is a sample document. " * 100,
        metadata={"source": "sample.txt", "page": 1},
    )

    chunks = split_documents(
        [document],
        chunk_size=100,
        chunk_overlap=20,
    )

    assert len(chunks) > 1
    assert all(len(chunk.page_content) <= 100 for chunk in chunks)
    assert [chunk.metadata["chunk_id"] for chunk in chunks] == list(
        range(len(chunks))
    )
    assert all(chunk.metadata["source"] == "sample.txt" for chunk in chunks)


def test_split_documents_invalid_chunk_size():
    with pytest.raises(ValueError, match="chunk_size must be positive"):
        split_documents([], chunk_size=0)


def test_split_documents_invalid_overlap():
    with pytest.raises(ValueError, match="chunk_overlap"):
        split_documents([], chunk_size=100, chunk_overlap=100)
