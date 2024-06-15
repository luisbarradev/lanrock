from src.domain.document_reader import DocumentReader

class ReadDocument:

    def __init__(self, reader: DocumentReader):
        self.reader = reader

    def execute(self, file_path: str, chunk_size: int) -> list:
        text = self.reader.read(file_path)
        return self.reader.chunk(text, chunk_size)
