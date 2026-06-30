from fastapi import APIRouter, UploadFile, File
from services.pdf_service import extract_text_from_pdf
from services.chunk_service import chunk_text
import os
import shutil

router = APIRouter()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    # Save the uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text from the PDF
    text = extract_text_from_pdf(file_path)

    # Split the text into chunks
    chunks = chunk_text(text)

    # Return response
    return {
    "message": "File uploaded successfully",
    "filename": file.filename,
    "total_chunks": len(chunks),
    "first_chunk": chunks[0] if chunks else "No text found in PDF."
}