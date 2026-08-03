from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from app.config.settings import Settings

client = QdrantClient(host="localhost", port=6333)

client.upsert(
    collection_name="document_chunks",
    points=[
        PointStruct(
            id=999,
            vector=[0.1] * 384,
            payload={
                "test": "hello"
            }
        )
    ],
    wait=True
)

print("Inserted!")

collection = client.get_collection("document_chunks")

print("Points:", collection.points_count)



print(Settings.QDRANT_HOST)
print(Settings.QDRANT_PORT)