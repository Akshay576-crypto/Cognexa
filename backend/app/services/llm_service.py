
from langchain_ollama import ChatOllama


class LLMService:
    """
    Central LLM service for Cognexa.

    Responsible only for communicating with the local Ollama LLM.
    Agent logic, retrieval, context building, and tools remain separate.
    """

    def __init__(
        self,
        model: str = "gemma3:4b",
        temperature: float = 0.2
    ):
        self.llm = ChatOllama(
            model=model,
            temperature=temperature
        )

    def generate(self, prompt: str) -> str:
        """
        Generate a response from the configured LLM.
        """

        response = self.llm.invoke(prompt)

        return response.content

    def generate_with_messages(self, messages: list) -> str:
        """
        Generate a response using LangChain messages.
        """

        response = self.llm.invoke(messages)

        return response.content

    def bind_tools(self, tools: list):
        """
        Bind LangChain tools to the configured LLM.

        Agent logic remains outside this service.
        """

        return self.llm.bind_tools(tools)

