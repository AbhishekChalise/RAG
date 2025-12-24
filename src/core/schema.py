from pydantic import BaseModel
from typing import Dict, Any

class RawDocument(BaseModel):
    content: str
    file_type: str
    metadata: Dict[str,Any]

