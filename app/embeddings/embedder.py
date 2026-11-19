import os

from langchain_ollama import OllamaEmbeddings


def get_embeddings():
    """Initialize the local Ollama embedding model."""
    return OllamaEmbeddings(
        model="nomic-embed-text:latest",
        base_url=os.getenv(
            "OLLAMA_BASE_URL",
            "http://localhost:11434",
        ),
    )