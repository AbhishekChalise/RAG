"""
PDF parser for RAG: Production Level RAG

This uses best tool for each job:
- PyMuPDF(fitz)
- Tesseract OCR: For Scanned/ imagebased pdfs
- Docling: Best in class table extraction
"""

import re
import io
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
from pathlib import Path

# Data Structure: How we organize the extracted PDF contents




