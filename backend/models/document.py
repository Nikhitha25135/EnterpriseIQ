from datetime import datetime


def create_document(
    document_id,
    filename,
    total_chunks,
    file_size,
    status="Indexed"
):
    return {
        "document_id": document_id,
        "filename": filename,
        "uploaded_at": datetime.utcnow(),
        "total_chunks": total_chunks,
        "file_size": file_size,
        "status": status
    }