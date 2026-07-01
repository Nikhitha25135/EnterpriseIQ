from fastapi import APIRouter, HTTPException
from bson import ObjectId
from bson.errors import InvalidId
from database.mongodb import documents_collection
import os

router = APIRouter()

# Base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Uploads folder
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")


@router.get("/documents")
def get_documents():
    documents = []

    for doc in documents_collection.find():
        documents.append({
            "id": str(doc["_id"]),
            "filename": doc.get("filename"),
            "uploaded_at": doc.get("uploaded_at"),
            "total_chunks": doc.get("total_chunks"),
            "file_size": doc.get("file_size"),
            "status": doc.get("status")
        })

    return {
        "total_documents": len(documents),
        "documents": documents
    }


@router.get("/documents/{document_id}")
def get_document(document_id: str):

    try:
        object_id = ObjectId(document_id)
    except InvalidId:
        raise HTTPException(
            status_code=400,
            detail="Invalid document ID"
        )

    document = documents_collection.find_one({"_id": object_id})

    if document is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    return {
        "id": str(document["_id"]),
        "filename": document.get("filename"),
        "uploaded_at": document.get("uploaded_at"),
        "total_chunks": document.get("total_chunks"),
        "file_size": document.get("file_size"),
        "status": document.get("status")
    }


@router.delete("/documents/{document_id}")
def delete_document(document_id: str):

    try:
        object_id = ObjectId(document_id)
    except InvalidId:
        raise HTTPException(
            status_code=400,
            detail="Invalid document ID"
        )

    document = documents_collection.find_one({"_id": object_id})

    if document is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    # Delete PDF file from uploads folder
    filename = document.get("filename")
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    if os.path.exists(file_path):
        try:
            os.remove(file_path)
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to delete file: {str(e)}"
            )

    # Delete metadata from MongoDB
    result = documents_collection.delete_one({"_id": object_id})

    if result.deleted_count == 0:
        raise HTTPException(
            status_code=500,
            detail="Failed to delete document from database."
        )

    return {
        "message": "Document deleted successfully",
        "filename": filename
    }