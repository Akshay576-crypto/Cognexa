from app.services.tool_router_service import ToolRouterService


router = ToolRouterService()


def run_router_test(question, document_id=None):
    print("\n" + "=" * 70)
    print("QUESTION:")
    print(question)

    result = router.route(
        question=question,
        document_id=document_id,
        top_k=5,
    )

    print("\nROUTER RESULT:")
    print(result)

    return result


def test_hac_router():
    result = run_router_test(
        "What is HAC?",
        document_id=7,
    )

    assert isinstance(result, dict)
    assert "tool" in result


def test_ev_market_router():
    result = run_router_test(
        "What is the current electric vehicle market growth in India?"
    )

    assert isinstance(result, dict)
    assert "tool" in result


def test_apple_financial_router():
    result = run_router_test(
        "Analyze Apple's latest financial performance."
    )

    assert isinstance(result, dict)
    assert "tool" in result


def test_general_question_router():
    result = run_router_test(
        "What is a database?"
    )

    assert isinstance(result, dict)
    assert "tool" in result


if __name__ == "__main__":

    run_router_test(
        "What is HAC?",
        document_id=7,
    )

    run_router_test(
        "What is the current electric vehicle market growth in India?"
    )

    run_router_test(
        "Analyze Apple's latest financial performance."
    )

    run_router_test(
        "What is a database?"
    )

    print("\nTOOL ROUTER TEST COMPLETED")