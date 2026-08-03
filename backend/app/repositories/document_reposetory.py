from app.database.db import get_db_connection


class DocumentRepository:

    # ----------------------------------------
    # Save Document Metadata
    # ----------------------------------------
    def create_document(
        self,
        project_id,
        user_id,
        original_filename,
        stored_filename,
        file_extension,
        mime_type,
        file_size,
        upload_path
    ):

        connection = get_db_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO documents
        (
            project_id,
            user_id,
            original_filename,
            stored_filename,
            file_extension,
            mime_type,
            file_size,
            upload_path
        )
        VALUES
        (%s,%s,%s,%s,%s,%s,%s,%s)
        """

        cursor.execute(
            query,
            (
                project_id,
                user_id,
                original_filename,
                stored_filename,
                file_extension,
                mime_type,
                file_size,
                upload_path
            )
        )

        connection.commit()

        print("Inside create_document()")
        print("Commit Successful")

        document_id = cursor.lastrowid

        cursor.close()
        connection.close()

        return document_id

    # ----------------------------------------
    # Get All Documents
    # ----------------------------------------
    def get_all_documents(self, project_id, user_id):

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        query = """
        SELECT *
        FROM documents
        WHERE project_id=%s
        AND user_id=%s
        ORDER BY created_at DESC
        """

        cursor.execute(
            query,
            (
                project_id,
                user_id
            )
        )

        documents = cursor.fetchall()

        cursor.close()
        connection.close()

        return documents

    # ----------------------------------------
    # Get Document By ID
    # ----------------------------------------
    def get_document_by_id(
        self,
        document_id,
        user_id
    ):

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        query = """
        SELECT *
        FROM documents
        WHERE document_id=%s
        AND user_id=%s
        """

        cursor.execute(
            query,
            (
                document_id,
                user_id
            )
        )

        document = cursor.fetchone()

        cursor.close()
        connection.close()

        return document

    # ----------------------------------------
    # Update Document Status
    # ----------------------------------------
    def update_status(
        self,
        document_id,
        status
    ):

        connection = get_db_connection()
        cursor = connection.cursor()

        query = """
        UPDATE documents
        SET upload_status=%s
        WHERE document_id=%s
        """

        cursor.execute(
            query,
            (
                status,
                document_id
            )
        )

        connection.commit()

        updated = cursor.rowcount

        cursor.close()
        connection.close()

        return updated

    # ----------------------------------------
    # Delete Document
    # ----------------------------------------
    def delete_document(
        self,
        document_id,
        user_id
    ):

        connection = get_db_connection()
        cursor = connection.cursor()

        query = """
        DELETE FROM documents
        WHERE document_id=%s
        AND user_id=%s
        """

        cursor.execute(
            query,
            (
                document_id,
                user_id
            )
        )

        connection.commit()

        deleted = cursor.rowcount

        cursor.close()
        connection.close()

        return deleted