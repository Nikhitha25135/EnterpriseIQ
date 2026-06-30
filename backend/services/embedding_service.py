from sentence_transformers import SentenceTransformer

# Load the embedding model once when the application starts
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embeddings(chunks):
    """
    Generate embeddings for a list of text chunks.
    """
    embeddings = model.encode(chunks, convert_to_numpy=True)

    return embeddings