from fastapi import APIRouter
from database.mongodb import chat_collection

router = APIRouter()


@router.get("/history")
def get_chat_history():

    chats = []

    for chat in chat_collection.find():

        chats.append({
            "id": str(chat["_id"]),
            "question": chat["question"],
            "answer": chat["answer"],
            "sources": chat["sources"],
            "created_at": chat["created_at"]
        })

    return {
        "total_chats": len(chats),
        "history": chats
    }