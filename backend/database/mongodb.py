from pymongo import MongoClient
from config.settings import MONGO_URI

client = MongoClient(MONGO_URI)

db = client["enterpriseiq"]

# Collections
documents_collection = db["documents"]
chat_collection = db["chat_history"]