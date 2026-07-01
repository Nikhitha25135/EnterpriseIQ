from fastapi import APIRouter, UploadFile, File
from services.pdf_service import extract_text_from_pdf
from services.chunk_service import chunk_text
from services.embedding_service import generate_embeddings
from services.vector_service import store_embeddings
from database.mongodb import documents_collection
from models.document import create_document

import os
import shutil

router = APIRouter()

# Upload folder
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """
    Upload a PDF, extract text, generate embeddings,
    store vectors in ChromaDB and metadata in MongoDB.
    """

    # Save uploaded PDF
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text
    text = extract_text_from_pdf(file_path)

    # Split into chunks
    chunks = chunk_text(text)

    # Check for empty PDF
    if not chunks:
        return {
            "message": "No readable text found in the PDF.",
            "filename": file.filename
        }

    # Generate embeddings
    embeddings = generate_embeddings(chunks)

    # Store embeddings in ChromaDB
    document_id = store_embeddings(
        chunks=chunks,
        embeddings=embeddings,
        filename=file.filename
    )

    # Create document metadata
    document = create_document(
        document_id=document_id,
        filename=file.filename,
        total_chunks=len(chunks),
        file_size=os.path.getsize(file_path)
    )

    # Store metadata in MongoDB
    documents_collection.insert_one(document)

    return {
        "message": "Document uploaded and indexed successfully",
        "document_id": document_id,
        "filename": file.filename,
        "total_chunks": len(chunks),
        "embedding_dimension": len(embeddings[0]),
        "status": "Indexed"
    }