import unittest
import os
import tempfile
from src.infrastructure.readers.txt_reader import TxtReader
from src.infrastructure.readers.pdf_reader import PdfReader
from src.application.use_cases.read_document import ReadDocument

class TestReadDocument(unittest.TestCase):

    def test_chunking_txt(self):
        reader = TxtReader()
        use_case = ReadDocument(reader)

        # Crear un archivo de texto temporal
        with tempfile.NamedTemporaryFile(delete=False, suffix='.txt') as temp_file:
            temp_file.write(b"Este es un texto de prueba. " * 5)
            temp_file_path = temp_file.name

        try:
            chunks = use_case.execute(temp_file_path, 25)
            self.assertEqual(len(chunks), 6)
            for chunk in chunks:
                print(chunk)
        finally:
            os.remove(temp_file_path)

    def test_chunking_pdf(self):
        reader = PdfReader()
        use_case = ReadDocument(reader)

        # Crear un archivo PDF temporal
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
            temp_file_path = temp_file.name

        try:
            import fitz
            document = fitz.open()
            page = document.new_page()
            page.insert_text((72, 72), "Este es un texto de prueba. " * 5)
            document.save(temp_file_path)

            chunks = use_case.execute(temp_file_path, 25)
            self.assertEqual(len(chunks), 5)
            for chunk in chunks:
                print(chunk)
        finally:
            os.remove(temp_file_path)

if __name__ == "__main__":
    unittest.main()
