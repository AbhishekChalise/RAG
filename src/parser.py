import pymupdf4llm
import os
from docx import Document
import pandas as pd

class DocumentParser:

    def __init__():
        return True
    
    def parser(self, file_path: str):

        ext = os.path.splitext(file_path)
        ext = ext[1].lower()

        if ext == ".pdf":
            return self.__parse_pdf()

        elif ext == ".docs":
            return self.__parse_docs()
        
        elif ext == ".csv":
            return self.__parse_csv()
        else:
            print("Unsupported Types")
            return None
        

    def __parse_pdf(self, path: str):
        return pymupdf4llm.to_markdown(path, page_chunks=True)
    

    def __parse_docs(self, path:str):
        doc = Document(path)
        text = '\n'.join([document.text for document in doc.paragraph])
        return [{'text': text, 'metadata': {
            "source": path,
            "page": 1
       }}]
    
    
    def __parse_csv(self, path: str):
        df = pd.read_csv(path)
        text = df.to_markdown(index = False)

        return [{"text": text, "metadata": {"source": path}}]