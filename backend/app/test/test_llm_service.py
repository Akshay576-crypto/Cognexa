from app.services.llm_service import LLMService


def test_llm_generation():
    llm_service = LLMService(
        model="gemma3:4b"
    )

    response = llm_service.generate(
        "Explain in one sentence what HAC is."
    )

    assert response
    assert isinstance(response, str)

    print("\n===== LLM RESPONSE =====")
    print(response)