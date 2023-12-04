# app/models/database.py
from typing import List
from pydantic import BaseModel, Field
from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct
from core.config import settings

# Initialize the Qdrant client with configuration settings
# This client is used to interact with the Qdrant vector database
qdrant_client = QdrantClient(host=settings.QDRANT_HOST, port=settings.QDRANT_PORT)

class Embedding(BaseModel):
    """
    Data model for an embedding.

    Attributes:
        id (int): Unique identifier for the embedding.
        vector (List[float]): Vector embedding representing the data point.
    """
    id: int = Field(..., description="Unique identifier for the embedding")
    vector: List[float] = Field(..., description="Vector embedding")

def save_embedding(embedding: Embedding):
    """
    Save a new embedding to the Qdrant database.

    Args:
        embedding (Embedding): The embedding instance to be saved.

    This function creates a PointStruct from the embedding and replaces any existing
    point with the same ID in the specified Qdrant collection.
    """
    point = PointStruct(id=embedding.id, payload=None, vector=embedding.vector)
    qdrant_client.points.replace(points=[point], collection_name=settings.QDRANT_COLLECTION)

def get_embedding(embedding_id: int) -> Embedding:
    """
    Retrieve an embedding from the Qdrant database by its ID.

    Args:
        embedding_id (int): The unique identifier of the embedding to retrieve.

    Returns:
        Embedding: The retrieved embedding object.

    Raises:
        ValueError: If the embedding with the given ID is not found.

    This function searches for an embedding in the Qdrant collection by its ID
    and returns the embedding if found. If not found, it raises a ValueError.
    """
    response = qdrant_client.points.get(point_id=embedding_id, collection_name=settings.QDRANT_COLLECTION)
    if response.result:
        point = response.result
        return Embedding(id=point.id, vector=point.vector)
    else:
        raise ValueError(f"Embedding with id {embedding_id} not found")

# Additional functions to update and delete embeddings can be added to extend functionality.
