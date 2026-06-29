from fastapi import APIRouter, UploadFile, File
from services.pdf_service import extract_text_from_pdf
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

    # Return response
    return {
        "message": "File uploaded successfully",
        "filename": file.filename,
        "text_preview": text[:1000]  # First 1000 characters
    }