from database.mongodb import chat_collection


def save_chat(chat):
    """
    Save a chat into MongoDB.
    """

    chat_collection.insert_one(chat)