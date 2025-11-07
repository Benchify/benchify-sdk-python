# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "StandardCreateResponse",
    "Data",
    "DataChangedFile",
    "DataRemainingDiagnostics",
    "DataRemainingDiagnosticsFileToDiagnostic",
    "DataRemainingDiagnosticsFileToDiagnosticLocation",
    "DataBundledFile",
    "Error",
    "Meta",
]


class DataChangedFile(BaseModel):
    contents: str
    """Contents of the file"""

    path: str
    """Path of the file"""


class DataRemainingDiagnosticsFileToDiagnosticLocation(BaseModel):
    column: Optional[float] = None
    """Column number (1-based)"""

    line: Optional[float] = None
    """Line number (1-based)"""

    span: float
    """Span of the error"""

    starting_character_position: Optional[float] = None
    """Position of the first character of the error location in the source code"""


class DataRemainingDiagnosticsFileToDiagnostic(BaseModel):
    file_path: str
    """File where diagnostic occurs"""

    location: DataRemainingDiagnosticsFileToDiagnosticLocation
    """Location of the diagnostic"""

    message: str
    """Diagnostic message"""

    type: str
    """Type of the diagnostic"""

    code: Optional[float] = None
    """Code given by the diagnostic generator"""

    context: Optional[str] = None
    """Surrounding code context"""


class DataRemainingDiagnostics(BaseModel):
    file_to_diagnostics: Optional[Dict[str, List[DataRemainingDiagnosticsFileToDiagnostic]]] = None
    """Diagnostics grouped by file"""


class DataBundledFile(BaseModel):
    contents: str
    """Contents of the file"""

    path: str
    """Path of the file"""


class Data(BaseModel):
    changed_files: List[DataChangedFile]
    """Files that were modified during fixing"""

    execution_time: float
    """Total execution time in seconds"""

    files_fixed: float
    """Number of files that were fixed"""

    fix_types_applied: List[Literal["dependency", "parsing", "css", "ai_fallback", "types", "ui", "sql"]]
    """Types of fixes that were actually applied"""

    issues_remaining: float
    """Number of issues still remaining"""

    issues_resolved: float
    """Number of issues resolved"""

    remaining_diagnostics: DataRemainingDiagnostics
    """Remaining diagnostics after standard fixes"""

    success: bool
    """Whether fixes were successfully applied"""

    bundled_files: Optional[List[DataBundledFile]] = None
    """Bundled output files if bundling was requested"""


class Error(BaseModel):
    code: str
    """The error code"""

    message: str
    """The error message"""

    details: Optional[Dict[str, object]] = None
    """Details about what caused the error"""


class Meta(BaseModel):
    external_id: Optional[str] = None
    """Customer tracking identifier"""

    trace_id: Optional[str] = None
    """Unique trace identifier for the request"""


class StandardCreateResponse(BaseModel):
    data: Data
    """The actual response data"""

    error: Optional[Error] = None
    """The error from the API query"""

    meta: Optional[Meta] = None
    """Meta information"""
