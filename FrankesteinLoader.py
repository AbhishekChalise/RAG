import fitz
import pytesseract
import io
from PIL import Image
from langchain_core.documents import Document
from docling.document_converter import DocumentConverter


class ProductionPDFLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        final_documents = []
        doc = fitz.open(self.file_path)

        for page in doc:

            page_num = page.number + 1

            



