import os
import json
from src.parser import DocumentParser

def run_parsing_step():

    parser = DocumentParser()

    raw_dir = "data/raw"
    processed_dir = "data/processed"

    os.makedirs(processed_dir, exist_ok=True)

    for filename in os.listdir(raw_dir):
        file_path = os.path.join(raw_dir, filename)

        if os.path.isfile(file_path):
            