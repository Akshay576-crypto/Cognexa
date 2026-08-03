from qdrant_client import QdrantClient

client = QdrantClient(host="localhost", port=6333)

print(hasattr(client, "search"))
print(hasattr(client, "query_points"))