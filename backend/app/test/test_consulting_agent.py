from app.agents.consulting_agent import ConsultingAgent


def test_consulting_agent_generation():

    agent = ConsultingAgent(
        model="qwen2.5:7b"
    )

    result = agent.analyze(
        question=(
            "Should a company expand into "
            "the Indian electric vehicle market?"
        ),
        context=(
            "The Indian EV market has shown strong "
            "growth in recent years. Competition is "
            "increasing among established manufacturers "
            "and new entrants."
        ),
        sources=(
            "Example Research - "
            "https://example.com"
        ),
    )

    assert isinstance(result, str)

    assert len(result.strip()) > 0

    print("\n===== CONSULTING ANALYSIS =====")
    print(result)


def test_empty_question():

    agent = ConsultingAgent(
        model="qwen2.5:7b"
    )

    result = agent.analyze(
        question="",
        context="Some research evidence.",
    )

    assert result == (
        "Consulting question cannot be empty."
    )


def test_empty_context():

    agent = ConsultingAgent(
        model="qwen2.5:7b"
    )

    result = agent.analyze(
        question="Should we expand?",
        context="",
    )

    assert result == (
        "Research evidence cannot be empty."
    )


def test_prompt_loading():

    agent = ConsultingAgent(
        model="qwen2.5:7b"
    )

    assert agent.system_prompt
    assert agent.user_prompt_template

    assert (
        "{question}"
        in agent.user_prompt_template
    )

    assert (
        "{context}"
        in agent.user_prompt_template
    )

    assert (
        "{sources}"
        in agent.user_prompt_template
    )
