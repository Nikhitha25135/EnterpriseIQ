from groq import Groq

from config.settings import GROQ_API_KEY, MODEL_NAME
from services.search_service import search_documents

# Create Groq client
client = Groq(api_key=GROQ_API_KEY)


def ask_question(question: str):
    """
    Retrieve relevant document chunks,
    generate an answer using Groq,
    and return source citations.
    """

    # Search ChromaDB
    results = search_documents(question)

    documents = results["documents"]
    metadatas = results["metadatas"]

    # Build context
    context = "\n\n".join(documents)

    # Prompt
    prompt = f"""
You are EnterpriseIQ, an AI Knowledge Assistant.

Answer ONLY using the information provided in the context.

If the answer is not available in the context, reply exactly:

"I couldn't find that information in the uploaded documents."

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": "You answer questions only from the provided context."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=300
    )

    # Prepare source citations
    sources = []

    for metadata in metadatas:
        sources.append({
            "filename": metadata["filename"],
            "chunk_id": metadata["chunk_id"]
        })

    return {
        "answer": response.choices[0].message.content,
        "sources": sources
    }