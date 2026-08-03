from app.services.embedding_service import EmbeddingService


service = EmbeddingService()

vector = service.generate_embedding(
    "Artificial Intelligence is transforming healthcare."
)

print(type(vector))
print(len(vector))
print(vector[:10])