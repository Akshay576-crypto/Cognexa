from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException

from app.auth.dependencies import get_current_user
from app.presentations.pdf_engine import PDFEngine
from app.schemas.pdf_schema import PDFRequest, PDFResponse


router = APIRouter(
    prefix="/api/v1/pdf",
    tags=["PDF"],
)


pdf_engine = PDFEngine()

GENERATED_DIR = Path("generated")
GENERATED_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


@router.post(
    "/",
    response_model=PDFResponse,
)
def generate_pdf(
    request: PDFRequest,
    current_user=Depends(get_current_user),
):
    try:
        output_path = (
            GENERATED_DIR / request.output_filename
        )

        result = pdf_engine.generate(
            presentation_spec=request.presentation_spec,
            output_path=str(output_path),
            theme_id=request.theme_id,
        )

        return PDFResponse(
            type=result["type"],
            title=result["title"],
            slide_count=result["slide_count"],
            output_path=result["output_path"],
            theme_id=result["theme_id"],
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"PDF generation failed: {str(e)}",
        )