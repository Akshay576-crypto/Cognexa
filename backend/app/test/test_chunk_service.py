from app.services.chunking_service import ChunkingService

chunking_service = ChunkingService()

sample_text = """
Introduction

Artificial Intelligence is transforming healthcare. Hospitals use AI to detect diseases earlier. Machine learning models help doctors make better decisions.

Applications

AI is used in banking for fraud detection. Recommendation systems improve customer experience. Manufacturing companies use predictive maintenance to reduce downtime.

Future

AI will continue to evolve rapidly. Organizations that adopt AI responsibly will gain a competitive advantage.
"""

chunks = chunking_service.chunk_text(
    text=sample_text,
    chunk_size=30,
    overlap=10
)

for chunk in chunks:
    print("=" * 60)
    print(f"Chunk Index : {chunk.chunk_index}")
    print(f"Token Count : {chunk.token_count}")
    print(f"Start Char  : {chunk.start_char}")
    print(f"End Char    : {chunk.end_char}")
    print("\nChunk Text:\n")
    print(chunk.chunk_text)