from app.schemas.chunk_schema import ChunkSchema
import re
class ChunkingService:

    """HAC v1 - Helix Adaptive Chunking

    Responsibilities:
    - Analyze cleaned text
    - Build logical chunks
    - Preserve document structure
    - Return ChunkSchema objects
    """
    

    def chunk_text(self,text:str,chunk_size:int=800,overlap:int=100)->list[ChunkSchema]:

        """Args:
            text: Cleaned document text.
            chunk_size: Maximum target size.
            overlap: Target overlap between chunks.

        Returns:
            List of ChunkSchema objects.
        """
        
        sections = self._split_into_sections(text)
        
        chunks = self._merge_paragraphs(sections,chunk_size)
        chunks = self._apply_overlap(chunks,overlap)
        chunk_objects = []
        
        for index ,chunk in enumerate(chunks):
        
            chunk_oject = self._build_chunk(index=index,text=chunk,start_char=None,end_char=None)
            chunk_objects.append(chunk_oject)
        
        return chunk_objects
        



    def _split_into_sections(self,text:str):
        """Split cleaned text into logical sections.
            HAC v1 Rules:
            - Split on two or more blank lines.
             """

        sections = re.split(r"\n\s*\n+",text)
        cleaned_section = []

        for section in sections:
            section = section.strip()

            if section:
                cleaned_section.append(section)

        return cleaned_section

    def _count_tokens(self,text:str)->int:

        """Estimate the number of tokens in a text.

            HAC v1:
            Uses whitespace-separated words as a lightweight
            approximation of token count.

            Args:
            text (str): Input text.

            Returns:
            int: Estimated token count.
        """

        if not text:
            return 0

        return len(text.split())


    def _merge_paragraphs(self,sections:list[str],chunk_size:int):
        """
        Merge paragraphs into logical chunks using
        a Greedy algorithm.
         """
        chunks = []
        current_chunks = []
        current_tokens = 0

        for section in sections:
            paragraphs = self._split_into_sections(section)

            for paragraph in paragraphs:
                paragraph_token = self._count_tokens(paragraph)

                if current_tokens + paragraph_token <= chunk_size:

                    current_chunks.append(paragraph)
                    current_tokens += paragraph_token

                else:

                    if current_chunks:
                        chunks.append("\n\n".join(current_chunks))

                    current_chunks = [paragraph]
                    current_tokens = paragraph_token

        if current_chunks:
            chunks.append("\n\n".join(current_chunks))

        return chunks
        
    def _get_overlap_paragraphs(self,chunks:str,over_lap:int):

        """
        Select paragraphs from the end of a chunk until
        the target overlap size is reached
        """
        paragraphs = chunks.split("\n\n")
        overlap_paragraphs = []
        current_overlap = 0

        for paragraph in reversed(paragraphs):

            paragraphs_token = self._count_tokens(paragraph)
            overlap_paragraphs.append(paragraph)
            current_overlap += paragraphs_token 

            if current_overlap >= over_lap:
                break

        overlap_paragraphs.reverse()
        return overlap_paragraphs

    def _apply_overlap(self, chunks: list[str], overlap: int):
        """
        Apply sliding window overlap between consecutive chunks.

        Args:
            chunks: List of chunks created by the Greedy Chunk Builder.
            overlap: Target overlap token count.

        Returns:
            List of chunks with overlap applied.
        """
        overlapped_chunks = []

        for i in range(len(chunks)):

            if i==0:
                overlapped_chunks.append(chunks[i])
                continue

            previous_chunk = chunks[i-1]
            current_chunk = chunks[i]

            overlap_paragraphs = self._get_overlap_paragraphs(
                previous_chunk,
                overlap)

            overlap_text = "\n\n".join(overlap_paragraphs)
            new_chunk = overlap_text + "\n\n" + current_chunk

            overlapped_chunks.append(new_chunk)

        return overlapped_chunks

    def _build_chunk( self,index: int, text: str,start_char: int,end_char: int):
        """
            Build a ChunkSchema object with metadata.
            Args:
                index: Position of the chunk.
                text: Chunk content.
                start_char: Starting character position.
                end_char: Ending character position.
            Returns:
                ChunkSchema object.
        """

        token_count = self._count_tokens(text)

        return ChunkSchema(
                chunk_index=index,
                chunk_text=text,
                token_count=token_count,
                start_char=start_char,
                end_char=end_char
            )
    