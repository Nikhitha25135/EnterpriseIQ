from pymongo import MongoClient
from config.settings import MONGO_URI

client = MongoClient(MONGO_URI)

db = client["enterpriseiq"]

documents_collection = db["documents"]