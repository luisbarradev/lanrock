from src.infrastructure.readers.txt_reader import TxtReader
from src.infrastructure.readers.pdf_reader import PdfReader

from src.application.use_cases.read_document import ReadDocument

def main():
    txt_reader = PdfReader()
    read_document_use_case = ReadDocument(txt_reader)

    file_path = 'test_documents/document.pdf'

    chunks = read_document_use_case.execute(file_path, 100)
    
    print("Chunks del texto:")
    for chunk in chunks:
        print(chunk)
        print("-" * 20)

if __name__ == "__main__":
    main()


import shutil
import os

def eliminar_pycache(directorio):
    for root, dirs, files in os.walk(directorio):
        for nombre in dirs:
            if nombre == '__pycache__':
                shutil.rmtree(os.path.join(root, nombre))

# Tu código aquí

# Eliminar __pycache__ después de la ejecución
eliminar_pycache('.')