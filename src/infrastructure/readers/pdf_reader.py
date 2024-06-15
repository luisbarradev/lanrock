import fitz  # PyMuPDF
from src.domain.document_reader import DocumentReader

class PdfReader(DocumentReader):

    def read(self, file_path: str) -> str:
        """Lee el contenido de un archivo PDF y lo convierte a texto plano."""
        document = fitz.open(file_path)
        text = ""
        for page_num in range(len(document)):
            page = document.load_page(page_num)
            text += page.get_text()
        return text

    def chunk(self, text: str, chunk_size: int) -> list:
        """Divide el texto en partes más pequeñas (chunks) de un tamaño específico."""
        return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
