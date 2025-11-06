# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = [
    "FixParsingAndDiagnoseDetectIssuesResponse",
    "Data",
    "DataDiagnostics",
    "DataDiagnosticsNotRequested",
    "DataDiagnosticsNotRequestedFileToDiagnostic",
    "DataDiagnosticsNotRequestedFileToDiagnosticLocation",
    "DataDiagnosticsRequested",
    "DataDiagnosticsRequestedFileToDiagnostic",
    "DataDiagnosticsRequestedFileToDiagnosticLocation",
    "DataStatistics",
    "Error",
    "Meta",
]


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


class DataStatistics(BaseModel):
    by_severity: Dict[str, float]
    """Count of diagnostics by severity"""

    by_type: Dict[str, float]
    """Count of diagnostics by type"""

    total_diagnostics: float
    """Total number of diagnostics found"""

    estimated_fix_time_seconds: Optional[float] = None
    """Estimated time to fix in seconds"""


class Data(BaseModel):
    diagnostics: DataDiagnostics
    """Diagnostics split into fixable (requested) and other (not_requested) groups"""

    fixer_version: str
    """Version of the fixer"""

    statistics: DataStatistics
    """Statistics about the diagnostics"""


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
