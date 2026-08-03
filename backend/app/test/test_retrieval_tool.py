from app.tools.retrieval_tool import retrieval_tool


result = retrieval_tool.invoke(
    {
        "question": "What is HAC?",
        "document_id": 7,
        "top_k": 5
    }
)

print("\n===== LANGCHAIN RETRIEVAL TOOL =====\n")
print(result)
