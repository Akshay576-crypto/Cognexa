
from pathlib import Path

from docx import Document as DocxDocument
from langchain_core.documents import Document
from pypdf import PdfReader

SUPPORTED_EXTENSIONS = {".pdf", ".docx", ".txt"}


def load_document(file_path: str) -> list[Document]:
    """Load PDF, DOCX or TXT into LangChain Documents."""

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    extension = path.suffix.lower()

    if extension not in SUPPORTED_EXTENSIONS:
        raise ValueError(f"Unsupported file type: {extension}")

    documents = []

    if extension == ".pdf":
        reader = PdfReader(str(path))

        for page_number, page in enumerate(reader.pages, start=1):
            text = page.extract_text() or ""

            documents.append(
                Document(
                    page_content=text,
                    metadata={
                        "source": path.name,
                        "page": page_number,
                        "file_type": "pdf",
                    },
                )
            )

    elif extension == ".docx":
        doc = DocxDocument(str(path))

        text = "\n".join(
            paragraph.text
            for paragraph in doc.paragraphs
            if paragraph.text.strip()
        )

        documents.append(
            Document(
                page_content=text,
                metadata={
                    "source": path.name,
                    "page": 1,
                    "file_type": "docx",
                },
            )
        )

    elif extension == ".txt":
        text = path.read_text(encoding="utf-8")

        documents.append(
            Document(
                page_content=text,
                metadata={
                    "source": path.name,
                    "page": 1,
                    "file_type": "txt",
                },
            )
        )

    documents = [
        document
        for document in documents
        if document.page_content.strip()
    ]

    if not documents:
        raise ValueError("No readable text found in the document.")

    return documents
