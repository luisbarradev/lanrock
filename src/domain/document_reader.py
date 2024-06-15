from abc import ABC, abstractmethod

class DocumentReader(ABC):
    
    @abstractmethod
    def read(self, file_path: str) -> str:
        """Lee el contenido del documento y lo convierte a texto plano."""
        pass
    
    @abstractmethod
    def chunk(self, text: str, chunk_size: int) -> list:
        """Divide el texto en partes más pequeñas (chunks)."""
        pass
