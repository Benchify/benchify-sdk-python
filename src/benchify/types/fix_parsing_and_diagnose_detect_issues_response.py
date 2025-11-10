# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = [
    "FixParsingAndDiagnoseDetectIssuesResponse",
    "Data",
    "DataChangedFile",
    "DataDiagnostics",
    "DataDiagnosticsNotRequested",
    "DataDiagnosticsNotRequestedFileToDiagnostic",
    "DataDiagnosticsNotRequestedFileToDiagnosticLocation",
    "DataDiagnosticsRequested",
    "DataDiagnosticsRequestedFileToDiagnostic",
    "DataDiagnosticsRequestedFileToDiagnosticLocation",
    "DataFixTypesAvailable",
    "Error",
    "Meta",
]


class DataChangedFile(BaseModel):
    contents: str
    """Contents of the file"""

    path: str
    """Path of the file"""


class DataDiagnosticsNotRequestedFileToDiagnosticLocation(BaseModel):
    column: Optional[float] = None
    """Column number (1-based)"""

    line: Optional[float] = None
    """Line number (1-based)"""

    span: float
    """Span of the error"""

    starting_character_position: Optional[float] = None
    """Position of the first character of the error location in the source code"""


class DataDiagnosticsNotRequestedFileToDiagnostic(BaseModel):
    file_path: str
    """File where diagnostic occurs"""

    location: DataDiagnosticsNotRequestedFileToDiagnosticLocation
    """Location of the diagnostic"""

    message: str
    """Diagnostic message"""

    type: str
    """Type of the diagnostic"""

    code: Optional[float] = None
    """Code given by the diagnostic generator"""

    context: Optional[str] = None
    """Surrounding code context"""


class DataDiagnosticsNotRequested(BaseModel):
    file_to_diagnostics: Optional[Dict[str, List[DataDiagnosticsNotRequestedFileToDiagnostic]]] = None
    """Diagnostics grouped by file"""


class DataDiagnosticsRequestedFileToDiagnosticLocation(BaseModel):
    column: Optional[float] = None
    """Column number (1-based)"""

    line: Optional[float] = None
    """Line number (1-based)"""

    span: float
    """Span of the error"""

    starting_character_position: Optional[float] = None
    """Position of the first character of the error location in the source code"""


class DataDiagnosticsRequestedFileToDiagnostic(BaseModel):
    file_path: str
    """File where diagnostic occurs"""

    location: DataDiagnosticsRequestedFileToDiagnosticLocation
    """Location of the diagnostic"""

    message: str
    """Diagnostic message"""

    type: str
    """Type of the diagnostic"""

    code: Optional[float] = None
    """Code given by the diagnostic generator"""

    context: Optional[str] = None
    """Surrounding code context"""


class DataDiagnosticsRequested(BaseModel):
    file_to_diagnostics: Optional[Dict[str, List[DataDiagnosticsRequestedFileToDiagnostic]]] = None
    """Diagnostics grouped by file"""


class DataDiagnostics(BaseModel):
    not_requested: Optional[DataDiagnosticsNotRequested] = None
    """Diagnostics that do not match the requested fix types"""

    requested: Optional[DataDiagnosticsRequested] = None
    """Diagnostics that match the requested fix types"""


class DataFixTypesAvailable(BaseModel):
    estimated_time_seconds: float
    """Estimated time to fix in seconds"""

    fix_type: str
    """The type of fix available"""

    issue_count: float
    """Number of issues that can be fixed with this type"""

    priority: float
    """Priority of this fix type (lower is higher priority)"""


class Data(BaseModel):
    changed_files: List[DataChangedFile]
    """Files that were changed during detection"""

    detection_time: float
    """Time taken to detect issues in seconds"""

    diagnosis_iterations: float
    """Number of diagnostic iterations performed"""

    diagnostics: DataDiagnostics
    """Diagnostics split into fixable (requested) and other (not_requested) groups"""

    estimated_total_fix_time: float
    """Estimated total time to fix all issues in seconds"""

    files_analyzed: float
    """Number of files that were analyzed"""

    fix_types_available: List[DataFixTypesAvailable]
    """Available fix types with metadata"""

    fixable_issues: float
    """Number of issues that can be fixed"""

    fixes_applied: float
    """Number of fixes that were applied during detection"""

    total_issues: float
    """Total number of issues found"""

    fixer_version: Optional[str] = None
    """Version of the fixer"""


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


class FixParsingAndDiagnoseDetectIssuesResponse(BaseModel):
    data: Data
    """The actual response data"""

    error: Optional[Error] = None
    """The error from the API query"""

    meta: Optional[Meta] = None
    """Meta information"""
