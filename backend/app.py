from fastapi import FastAPI
from api.upload import router as upload_router

app = FastAPI(title="EnterpriseIQ")

app.include_router(upload_router)


@app.get("/")
def home():
    return {"message": "EnterpriseIQ API Running"}