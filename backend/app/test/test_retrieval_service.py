from app.services.retrival_service import RetrievalService

service = RetrievalService()

results = service.retrieve(
    question="What is HAC?",
    top_k=3
)

for result in results:
    print("SCORE:", result.score)
    print("PAYLOAD:", result.payload)
    print("-" * 80)
    #test_retrieval_service

questions = [
    "How does chunking work?",
    "HARE",
    "HAC"
]

for question in questions:

    print("\n" + "=" * 80)
    print("QUESTION:", question)
    print("=" * 80)

    results = service.retrieve(
        question=question,
        top_k=3
    )

    for result in results:
        print("SCORE:", result.score)
        print("DOCUMENT:", result.payload.get("document_id"))
        print("CHUNK:", result.payload.get("chunk_index"))
        print("TEXT:", result.payload.get("chunk_text", "")[:500])
        print("-" * 80)