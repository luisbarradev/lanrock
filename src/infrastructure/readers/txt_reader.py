from src.domain.document_reader import DocumentReader

class TxtReader(DocumentReader):

    def read(self, file_path: str) -> str:
        """Lee el contenido de un archivo de texto y lo convierte a texto plano."""
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    def chunk(self, text: str, chunk_size: int) -> list:
        """Divide el texto en partes más pequeñas (chunks) de un tamaño específico."""
        return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
