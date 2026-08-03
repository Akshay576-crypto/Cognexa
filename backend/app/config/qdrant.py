from qdrant_client import QdrantClient
from app.config.settings import Settings


qdrant_client = QdrantClient(
    host=Settings.QDRANT_HOST,
    port=Settings.QDRANT_PORT
)