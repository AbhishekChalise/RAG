from typing import List


def read_filepath(file_path: str) -> str:
    try:
        with open(file_path, "r", encoding = "utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error! File not found")
        return ""


def chunk_text(text: str, chunk_size: int, overlap: int) -> List[str]:
    chunks = []
    start = 0
    
    while start < len(text):
        end = start + chunk_size
        chunks = text[start:end]
        start = end - overlap
        
    return chunks


if __name__ == "__main__":
    
    """Quick integration test"""
    
    sample_text = "This is a sample document to test the production RAG data ingestion pipeline workflow."
    
    chunks = chunk_text(sample_text, chunk_size=20, overlap=5)
    
    print(f"Processed {len(chunks)} chunks successfully.")