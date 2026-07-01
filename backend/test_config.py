
from database.mongodb import documents_collection

print("MongoDB Connected Successfully!")

print(documents_collection)

from config.settings import GROQ_API_KEY, MODEL_NAME

print("Groq Key:", GROQ_API_KEY[:10] + "...")
print("Model:", MODEL_NAME)
