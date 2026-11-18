
import re

from langchain_core.documents import Document


def clean_documents(
    documents: list[Document],
) -> list[Document]:
    """Clean extracted document text while preserving metadata."""

    cleaned_documents = []

    for document in documents:
        text = document.page_content

        # Normalize line breaks and whitespace
        text = text.replace("\x00", "")
        text = text.replace("\r\n", "\n")
        text = text.replace("\r", "\n")

        # Remove excessive spaces and blank lines
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r"\n{3,}", "\n\n", text)

        text = text.strip()

        if text:
            cleaned_documents.append(
                Document(
                    page_content=text,
                    metadata=document.metadata.copy(),
                )
            )

    return cleaned_documents
