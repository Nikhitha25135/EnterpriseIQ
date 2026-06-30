import chromadb

# Create a persistent ChromaDB client
client = chromadb.PersistentClient(path="./vector_db")

# Create or load the collection
collection = client.get_or_create_collection(
    name="enterprise_documents"
)


def store_embeddings(chunks, embeddings, filename):
    """
    Store document chunks and their embeddings in ChromaDB.
    """

    ids = []
    metadatas = []

    for i in range(len(chunks)):
        ids.append(f"{filename}_{i}")

        metadatas.append({
            "filename": filename,
            "chunk_id": i,
            "document_type": "pdf"
        })

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist(),
        metadatas=metadatas
    )