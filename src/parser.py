import pymupdf4llm
from docx import Document
import pandas as pd
import os
import json


class DocumentParser():

    def __init__(self):
        pass

    def parse(self, file_path: str):
        """Determines the file type and call the appropriate serializer"""

        ext = os.path.splitext(file_path)[1].lower()

        if ext == ".pdf":
            return True
    

    def __parse_pdf(self, path: str):
        return pymupdf4llm.to_markdown(path, page_chunks=True)
    
    def __parse_docx(self, path: str):
        docs = Document(path)
        text = "\n".join([document.text for document in docs.paragraphs])
        return [{'text': text, "metadata": {'source': path}}]

    def __parse_csv(self, path):
        df = pd.read_csv(path)
        text = df.to_markdown(path, page_chunks = True)
        








