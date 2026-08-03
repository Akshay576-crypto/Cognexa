from app.database.db import get_db_connection
from app.schemas.chunk_schema import ChunkSchema


class ChunkRepository:

    # ----------------------------------------
    # Save All Chunks
    # ----------------------------------------
    def save_chunks(
        self,
        document_id: int,
        chunks: list[ChunkSchema]
    ):

        connection = get_db_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO document_chunks
        (
            document_id,
            chunk_index,
            chunk_text,
            token_count,
            character_count
        )
        VALUES
        (%s,%s,%s,%s,%s)
        """

        data = []

        for chunk in chunks:

            data.append(
                (
                    document_id,
                    chunk.chunk_index,
                    chunk.chunk_text,
                    chunk.token_count,
                    len(chunk.chunk_text)
                )
            )

        cursor.executemany(query, data)

        connection.commit()

        cursor.close()
        connection.close()

    # ----------------------------------------
    # Get Chunks
    # ----------------------------------------
    def get_chunks_by_document(
        self,
        document_id: int
    ):

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        query = """
        SELECT *
        FROM document_chunks
        WHERE document_id=%s
        ORDER BY chunk_index
        """

        cursor.execute(query, (document_id,))

        chunks = cursor.fetchall()

        cursor.close()
        connection.close()

        return chunks

    # ----------------------------------------
    # Delete Chunks
    # ----------------------------------------
    def delete_chunks_by_document(
        self,
        document_id: int
    ):

        connection = get_db_connection()
        cursor = connection.cursor()

        query = """
        DELETE FROM document_chunks
        WHERE document_id=%s
        """

        cursor.execute(query, (document_id,))

        connection.commit()

        deleted = cursor.rowcount

        cursor.close()
        connection.close()

        return deleted