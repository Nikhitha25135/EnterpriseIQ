from fastapi import APIRouter
from pydantic import BaseModel

from services.rag_service import ask_question
from services.history_service import save_chat
from models.chat import create_chat

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
def chat(request: ChatRequest):
    """
    Ask a question using RAG,
    return the answer,
    and save the conversation.
    """

    result = ask_question(request.question)

    # Create chat document
    chat_document = create_chat(
        question=request.question,
        answer=result["answer"],
        sources=result["sources"]
    )

    # Save to MongoDB
    save_chat(chat_document)

    return {
        "question": request.question,
        "answer": result["answer"],
        "sources": result["sources"]
    }