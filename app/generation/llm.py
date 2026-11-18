
from langchain_ollama import ChatOllama


def get_chat_model():
    """Initialize the local Qwen chat model."""

    return ChatOllama(
        model="qwen2.5:7b",
        base_url="http://localhost:11434",
        temperature=0,
    )
