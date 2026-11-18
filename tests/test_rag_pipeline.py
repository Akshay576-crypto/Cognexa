from app.pipeline.rag_chain import ask_question


def test_rag_question_answering():

    question = (
        "What are the main AI/ML product concepts "
        "described in this document?"
    )

    result = ask_question(question, top_k=4)

    assert result["answer"]
    assert len(result["sources"]) > 0

    print("\n===== RAG ANSWER =====")
    print(result["answer"])

    print("\n===== SOURCES =====")

    for source in result["sources"]:
        print(
            f"{source['source']} | Page {source['page']}"
        )

    print("\nRAG PIPELINE TEST PASSED")


if __name__ == "__main__":
    test_rag_question_answering()
