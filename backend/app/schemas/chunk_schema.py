from pydantic import BaseModel, Field
from typing import Optional


class ChunkSchema(BaseModel):
    """
    Represents a processed document chunk.
    """

    chunk_index: int = Field(..., ge=0)
    chunk_text: str
    token_count: int = Field(..., ge=0)

    # Character positions in the cleaned document
    start_char: Optional[int] = None
    end_char: Optional[int] = None

    class Config:
        from_attributes = True