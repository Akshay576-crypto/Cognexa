from app.services.text_extrection_service import TextExtractionService
from app.services.text_cleaning_service import TextCleaningService
from app.services.chunking_service import ChunkingService
from app.services.embedding_service import EmbeddingService

from app.repositories.chunk_reposetory import ChunkRepository
from app.repositories.vector_repositories import VectorRepository

class DocumentProcessingService:
    

    def __init__(self):

        self.text_extraction_service = TextExtractionService()
        self.text_cleaning_service = TextCleaningService()
        self.chunking_service = ChunkingService()

        self.embedding_service = EmbeddingService()

        self.chunk_repository = ChunkRepository()
        self.vector_repository = VectorRepository()

    def process_document(
        self,
        document_id: int,
        upload_path: str
    ):

        print("\n========== DOCUMENT PROCESSING ==========")

        # ------------------------------------
        # Step 1 : Extract Text
        # ------------------------------------

        raw_text = self.text_extraction_service.extract_text(
            upload_path
        )

        print(f"Raw Text Length : {len(raw_text)}")

        # ------------------------------------
        # Step 2 : Clean Text
        # ------------------------------------

        clean_text = self.text_cleaning_service.clean_text(
            raw_text
        )

        print(f"Clean Text Length : {len(clean_text)}")

        # ------------------------------------
        # Step 3 : HAC Chunking
        # ------------------------------------

        chunks = self.chunking_service.chunk_text(
            clean_text
        )

        print(f"Chunks Generated : {len(chunks)}")

        # ------------------------------------
        # Step 4 : Save Chunks
        # ------------------------------------

        
        self.chunk_repository.save_chunks(
            document_id=document_id,
            chunks=chunks
        )

        print("Chunks Saved")

        
        # ------------------------------------
        # Step 5 : Generate Embeddings
        # ------------------------------------

        texts = [
            chunk.chunk_text
            for chunk in chunks
        ]

        embeddings = self.embedding_service.generate_embeddings(
            texts
        )

        print("Embeddings Generated:", len(embeddings))
        print("=" * 60)
        print("Document ID:", document_id)
        print("Chunk Count:", len(chunks))
        print("Embedding Count:", len(embeddings))
        print("First Chunk:")
        print(chunks[0].chunk_text[:150])
        print()
        print("First Embedding Length:", len(embeddings[0]))
        print("=" * 60)
        print(f"Embeddings Generated : {len(embeddings)}")

        # ------------------------------------
        # Step 6 : Store Vectors
        # ------------------------------------

        self.vector_repository.save_embeddings(
            document_id=document_id,
            chunks=chunks,
            embeddings=embeddings
        )

        print("Vectors Stored")

        print("========== PROCESS COMPLETE ==========\n")

        return True



        #print("Document ID:", document_id)
        #print("Chunks:", len(chunks))
        #print("Embeddings:", len(embeddings))
                #print("=" * 60)
                #print("Embedding Count:", len(embeddings))
                #print("Chunk Count:", len(chunks))
                #print("First Chunk:")
                #print(chunks[0].chunk_text[:150])
                #print()
                #print("First Embedding Length:")
                #print(len(embeddings[0]))
                #print("=" * 60)
                #print("Chunks Saved")
        
