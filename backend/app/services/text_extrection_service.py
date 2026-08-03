from pathlib import Path
import fitz  # PyMuPDF


class TextExtractionService:
    """
    Enterprise Text Extraction Service.

    Responsibilities:
    - Validate uploaded files
    - Detect supported document types
    - Extract raw text
    """

    SUPPORTED_EXTENSIONS = {
        ".pdf",
        ".txt",
    }

    def extract_text(self, file_path: str) -> str:
        """
        Extract raw text from a supported document.

        Args:
            file_path: Absolute path to the uploaded file.

        Returns:
            Extracted raw text.

        Raises:
            FileNotFoundError
            ValueError
        """

        path = Path(file_path)

        self._validate_file(path)

        extension = path.suffix.lower()

        if extension == ".pdf":
            return self._extract_pdf(path)

        if extension == ".txt":
            return self._extract_txt(path)

        raise ValueError(f"Unsupported file type: {extension}")

    def _validate_file(self, path: Path):

        if not path.exists():
            raise FileNotFoundError(f"{path} not found.")

        if path.suffix.lower() not in self.SUPPORTED_EXTENSIONS:
            raise ValueError(f"Unsupported file type: {path.suffix}")

    def _extract_pdf(self, path: Path) -> str:

        document = fitz.open(path)

        text = ""

        for page in document:
            text += page.get_text()

        document.close()

        return text

    def _extract_txt(self, path: Path) -> str:

        encodings = [
            "utf-8",
            "utf-8-sig",
            "latin-1",
        ]

        for encoding in encodings:
            try:
                with open(path, "r", encoding=encoding) as file:
                    return file.read()
            except UnicodeDecodeError:
                continue

        raise ValueError("Unable to decode text file.")