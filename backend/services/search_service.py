import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB
client = chromadb.PersistentClient(path="./vector_db")

collection = client.get_or_create_collection(
    name="enterprise_documents"
)


def search_documents(question, top_k=3):
    """
    Search the most relevant document chunks from ChromaDB.
    Returns:
        - documents
        - metadatas
        - distances
    """

    # Convert user question into embedding
    query_embedding = model.encode(question).tolist()

    # Query ChromaDB
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return {
        "documents": results["documents"][0],
        "metadatas": results["metadatas"][0],
        "distances": results["distances"][0]
    }