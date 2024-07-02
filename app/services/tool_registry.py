from pydantic import BaseModel
from app.services.logger import setup_logger
from typing import List, Any, Optional, Dict
from app.api.error_utilities import InputValidationError

logger = setup_logger(__name__)

class ToolInput(BaseModel):
    # Input from incoming request typically represent HTML Form elements
    name: str
    value: Any
    # When passing "files", the value field is an object with file details as properties
    
# Base model for all tools
class BaseTool(BaseModel):
    tool_id: int  # Unique identifier for each tool,
    inputs: List[ToolInput]

class ToolFile(BaseModel):
    filePath: Optional[str] = None
    url: str
    filename: Optional[str] = None
    filetype: str

class PDFFile(ToolFile):
    startPage: Optional[int] = None
    endPage: Optional[int] = None

class CSVFile(ToolFile):
    startRow: Optional[int] = None
    endRow: Optional[int] = None
    columns: Optional[List[int]] = None

class PPTXFile(ToolFile):
    startSlide: Optional[int] = None
    endSlide: Optional[int] = None

class TextFile(ToolFile):
    startLine: Optional[int] = None
    endLine: Optional[int] = None

class WebPage(ToolFile):
    tag: Optional[str] = None

class YouTube(ToolFile):
    start_timestamp: Optional[int] = None
    end_timestamp: Optional[int] = None



