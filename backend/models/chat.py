from datetime import datetime


def create_chat(question, answer, sources):
    return {
        "question": question,
        "answer": answer,
        "sources": sources,
        "created_at": datetime.utcnow()
    }