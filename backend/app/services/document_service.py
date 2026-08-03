import os
import uuid
import shutil
from app.services.document_processing_service import DocumentProcessingService
from fastapi import UploadFile

from app.config.settings import settings
from app.repositories.document_reposetory import DocumentRepository


class DocumentService:

    UPLOAD_FOLDER = settings.UPLOAD_FOLDER

    def __init__(self):
        self.repository = DocumentRepository()
        self.processing_service = DocumentProcessingService()

    # ---------------------------------------
    # Upload Document
    # ---------------------------------------
    def upload_document(
        self,
        project_id,
        user_id,
        file: UploadFile
    ):

        # Create upload directory if it doesn't exist
        os.makedirs(self.UPLOAD_FOLDER, exist_ok=True)

        # File extension
        extension = os.path.splitext(file.filename)[1]

        # Generate unique filename
        unique_filename = f"{uuid.uuid4()}{extension}"

        # Complete storage path
        upload_path = os.path.join(
            self.UPLOAD_FOLDER,
            unique_filename
        )

        # Save file
        with open(upload_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Get file size
        file_size = os.path.getsize(upload_path)

        # Save metadata into database
        document_id = self.repository.create_document(
            project_id=project_id,
            user_id=user_id,
            original_filename=file.filename,
            stored_filename=unique_filename,
            file_extension=extension,
            mime_type=file.content_type,
            file_size=file_size,
            upload_path=upload_path
        )

        self.processing_service.process_document(
        document_id=document_id,
        upload_path=upload_path
        )

        return {
            "success": True,
            "message": "Document uploaded successfully.",
            "document_id": document_id
        }

    # ---------------------------------------
    # Get All Documents
    # ---------------------------------------
    def get_all_documents(
        self,
        project_id,
        user_id
    ):

        documents = self.repository.get_all_documents(
            project_id,
            user_id
        )

        return {
            "success": True,
            "data": documents
        }

    # ---------------------------------------
    # Delete Document
    # ---------------------------------------
    def delete_document(
        self,
        document_id,
        user_id
    ):

        document = self.repository.get_document_by_id(
            document_id,
            user_id
        )

        if not document:
            return {
                "success": False,
                "message": "Document not found."
            }

        # Delete physical file
        if os.path.exists(document["upload_path"]):
            os.remove(document["upload_path"])

        deleted = self.repository.delete_document(
            document_id,
            user_id
        )

        if deleted == 0:
            return {
                "success": False,
                "message": "Document not found."
            }

        return {
            "success": True,
            "message": "Document deleted successfully."
        }