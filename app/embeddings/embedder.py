from langchain_ollama import OllamaEmbeddings


def get_embeddings():
    """Initialize the local Ollama embedding model."""

    return OllamaEmbeddings(
        model="nomic-embed-text:latest",
        base_url="http://localhost:11434",
    )
