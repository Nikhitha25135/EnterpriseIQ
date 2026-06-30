from fastapi import APIRouter, UploadFile, File
from services.pdf_service import extract_text_from_pdf
from services.chunk_service import chunk_text
from services.embedding_service import generate_embeddings
from services.vector_service import store_embeddings
import os
import shutil

router = APIRouter()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # Save uploaded file
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text
    text = extract_text_from_pdf(file_path)

    # Split into chunks
    chunks = chunk_text(text)

    # Handle empty PDFs
    if not chunks:
        return {
            "message": "No readable text found in the PDF.",
            "filename": file.filename
        }

    # Generate embeddings
    embeddings = generate_embeddings(chunks)

    # Store in ChromaDB
    store_embeddings(
        chunks=chunks,
        embeddings=embeddings,
        filename=file.filename
    )

    # Return response
    return {
        "message": "Document stored successfully",
        "filename": file.filename,
        "total_chunks": len(chunks),
        "embedding_dimension": len(embeddings[0])
    }