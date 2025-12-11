import os
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv


load_dotenv()


def main():
    print("This is the main function")

if __name__ == '__main__':
    main()

    #1. loading the file 
    #2. Chunking the file 
    #3. Embedding the file
