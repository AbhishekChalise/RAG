from langchain_community.document_loaders import PyMuPDFLoader

file_path = "yourdocument.pdf"

loader = PyMuPDFLoader(file_path)

docs = loader.load(loader)

