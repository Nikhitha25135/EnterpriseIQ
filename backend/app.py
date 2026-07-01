from fastapi import FastAPI

from api.upload import router as upload_router
from api.search import router as search_router
from api.chat import router as chat_router
from api.documents import router as documents_router
from api.history import router as history_router

app = FastAPI(title="EnterpriseIQ")

app.include_router(upload_router)
app.include_router(search_router)
app.include_router(chat_router)
app.include_router(documents_router)
app.include_router(history_router)


@app.get("/")
def home():
    return {"message": "EnterpriseIQ API Running"}