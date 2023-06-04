from qdrant_client import QdrantClient

client = QdrantClient(":memory:")
# or
client = QdrantClient(path="path/to/db")  # Persists changes to disk

collection_info = client.get_collection(collection_name="my_collection")




pass