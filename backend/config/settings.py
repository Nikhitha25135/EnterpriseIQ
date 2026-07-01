import os
from dotenv import load_dotenv

load_dotenv()

# Groq
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")

# MongoDB
MONGO_URI = os.getenv("MONGO_URI")

# Embedding Model
EMBEDDING_MODEL = "all-MiniLM-L6-v2"