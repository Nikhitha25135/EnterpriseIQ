import chromadb
import uuid

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

    document_id = str(uuid.uuid4())

    ids = []
    metadatas = []

    for i, chunk in enumerate(chunks):

        ids.append(f"{document_id}_{i}")

        metadatas.append({
            "document_id": document_id,
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

    return document_id