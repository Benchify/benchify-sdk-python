# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "FixerRunResponse",
    "Data",
    "DataStatus",
    "DataSuggestedChanges",
    "DataSuggestedChangesAllFile",
    "DataSuggestedChangesChangedFile",
    "DataBundle",
    "DataBundleFile",
    "DataFileToStrategyStatistic",
    "DataFinalDiagnostics",
    "DataFinalDiagnosticsNotRequested",
    "DataFinalDiagnosticsNotRequestedFileToDiagnostic",
    "DataFinalDiagnosticsNotRequestedFileToDiagnosticLocation",
    "DataFinalDiagnosticsRequested",
    "DataFinalDiagnosticsRequestedFileToDiagnostic",
    "DataFinalDiagnosticsRequestedFileToDiagnosticLocation",
    "DataInitialDiagnostics",
    "DataInitialDiagnosticsNotRequested",
    "DataInitialDiagnosticsNotRequestedFileToDiagnostic",
    "DataInitialDiagnosticsNotRequestedFileToDiagnosticLocation",
    "DataInitialDiagnosticsRequested",
    "DataInitialDiagnosticsRequestedFileToDiagnostic",
    "DataInitialDiagnosticsRequestedFileToDiagnosticLocation",
    "Error",
    "Meta",
]


class DataStatus(BaseModel):
    composite_status: Literal[
        "FIXED_EVERYTHING", "FIXED_REQUESTED", "PARTIALLY_FIXED", "NO_REQUESTED_ISSUES", "NO_ISSUES", "FAILED"
    ]
    """Overall composite status"""

    file_to_composite_status: Optional[
        Dict[
            str,
            Literal[
                "FIXED_EVERYTHING", "FIXED_REQUESTED", "PARTIALLY_FIXED", "NO_REQUESTED_ISSUES", "NO_ISSUES", "FAILED"
            ],
        ]
    ] = None
    """Status of each file"""


class DataSuggestedChangesAllFile(BaseModel):
    contents: str
    """Contents of the file"""

    path: str
    """Path of the file"""


class DataSuggestedChangesChangedFile(BaseModel):
    contents: str
    """Contents of the file"""

    path: str
    """Path of the file"""


class DataSuggestedChanges(BaseModel):
    all_files: Optional[List[DataSuggestedChangesAllFile]] = None
    """List of all files with their current contents.

    Only present when response_encoding is "json".
    """

    changed_files: Optional[List[DataSuggestedChangesChangedFile]] = None
    """List of changed files with their new contents.

    Only present when response_encoding is "json".
    """

    diff: Optional[str] = None
    """Unified diff of changes. Only present when response_encoding is "json"."""


class DataBundleFile(BaseModel):
    contents: str
    """Contents of the file"""

    path: str
    """Path of the file"""


class DataBundle(BaseModel):
    build_system: str

    status: Literal["SUCCESS", "FAILED", "NOT_ATTEMPTED", "PARTIAL_SUCCESS"]

    template_path: str

    bundle_url: Optional[str] = None

    debug: Optional[Dict[str, str]] = None

    files: Optional[List[DataBundleFile]] = None


class DataFileToStrategyStatistic(BaseModel):
    strategy_name: str

    version_hash: str

    fixes_applied: Optional[bool] = None

    fixes_fired: Optional[bool] = None


class DataFinalDiagnosticsNotRequestedFileToDiagnosticLocation(BaseModel):
    column: Optional[float] = None
    """Column number (1-based)"""

    line: Optional[float] = None
    """Line number (1-based)"""

    span: float
    """Span of the error"""

    starting_character_position: Optional[float] = None
    """Position of the first character of the error location in the source code"""


class DataFinalDiagnosticsNotRequestedFileToDiagnostic(BaseModel):
    file_path: str
    """File where diagnostic occurs"""

    location: DataFinalDiagnosticsNotRequestedFileToDiagnosticLocation
    """Location of the diagnostic"""

    message: str
    """Diagnostic message"""

    type: str
    """Type of the diagnostic"""

    code: Optional[float] = None
    """Code given by the diagnostic generator"""

    context: Optional[str] = None
    """Surrounding code context"""


class DataFinalDiagnosticsNotRequested(BaseModel):
    file_to_diagnostics: Optional[Dict[str, List[DataFinalDiagnosticsNotRequestedFileToDiagnostic]]] = None
    """Diagnostics grouped by file"""


class DataFinalDiagnosticsRequestedFileToDiagnosticLocation(BaseModel):
    column: Optional[float] = None
    """Column number (1-based)"""

    line: Optional[float] = None
    """Line number (1-based)"""

    span: float
    """Span of the error"""

    starting_character_position: Optional[float] = None
    """Position of the first character of the error location in the source code"""


class DataFinalDiagnosticsRequestedFileToDiagnostic(BaseModel):
    file_path: str
    """File where diagnostic occurs"""

    location: DataFinalDiagnosticsRequestedFileToDiagnosticLocation
    """Location of the diagnostic"""

    message: str
    """Diagnostic message"""

    type: str
    """Type of the diagnostic"""

    code: Optional[float] = None
    """Code given by the diagnostic generator"""

    context: Optional[str] = None
    """Surrounding code context"""


class DataFinalDiagnosticsRequested(BaseModel):
    file_to_diagnostics: Optional[Dict[str, List[DataFinalDiagnosticsRequestedFileToDiagnostic]]] = None
    """Diagnostics grouped by file"""


class DataFinalDiagnostics(BaseModel):
    not_requested: Optional[DataFinalDiagnosticsNotRequested] = None
    """Diagnostics that do not match the requested fix types"""

    requested: Optional[DataFinalDiagnosticsRequested] = None
    """Diagnostics that match the requested fix types"""


class DataInitialDiagnosticsNotRequestedFileToDiagnosticLocation(BaseModel):
    column: Optional[float] = None
    """Column number (1-based)"""

    line: Optional[float] = None
    """Line number (1-based)"""

    span: float
    """Span of the error"""

    starting_character_position: Optional[float] = None
    """Position of the first character of the error location in the source code"""


class DataInitialDiagnosticsNotRequestedFileToDiagnostic(BaseModel):
    file_path: str
    """File where diagnostic occurs"""

    location: DataInitialDiagnosticsNotRequestedFileToDiagnosticLocation
    """Location of the diagnostic"""

    message: str
    """Diagnostic message"""

    type: str
    """Type of the diagnostic"""

    code: Optional[float] = None
    """Code given by the diagnostic generator"""

    context: Optional[str] = None
    """Surrounding code context"""


class DataInitialDiagnosticsNotRequested(BaseModel):
    file_to_diagnostics: Optional[Dict[str, List[DataInitialDiagnosticsNotRequestedFileToDiagnostic]]] = None
    """Diagnostics grouped by file"""


class DataInitialDiagnosticsRequestedFileToDiagnosticLocation(BaseModel):
    column: Optional[float] = None
    """Column number (1-based)"""

    line: Optional[float] = None
    """Line number (1-based)"""

    span: float
    """Span of the error"""

    starting_character_position: Optional[float] = None
    """Position of the first character of the error location in the source code"""


class DataInitialDiagnosticsRequestedFileToDiagnostic(BaseModel):
    file_path: str
    """File where diagnostic occurs"""

    location: DataInitialDiagnosticsRequestedFileToDiagnosticLocation
    """Location of the diagnostic"""

    message: str
    """Diagnostic message"""

    type: str
    """Type of the diagnostic"""

    code: Optional[float] = None
    """Code given by the diagnostic generator"""

    context: Optional[str] = None
    """Surrounding code context"""


class DataInitialDiagnosticsRequested(BaseModel):
    file_to_diagnostics: Optional[Dict[str, List[DataInitialDiagnosticsRequestedFileToDiagnostic]]] = None
    """Diagnostics grouped by file"""


class DataInitialDiagnostics(BaseModel):
    not_requested: Optional[DataInitialDiagnosticsNotRequested] = None
    """Diagnostics that do not match the requested fix types"""

    requested: Optional[DataInitialDiagnosticsRequested] = None
    """Diagnostics that match the requested fix types"""


class Data(BaseModel):
    fixer_version: str
    """Version of the fixer"""

    status: DataStatus
    """Final per-file status after fixing"""

    suggested_changes: DataSuggestedChanges
    """Suggested changes to fix the issues"""

    bundle: Optional[DataBundle] = None
    """Bundle information if bundling was requested"""

    file_to_strategy_statistics: Optional[Dict[str, List[DataFileToStrategyStatistic]]] = None
    """Per-file strategy statistics"""

    final_diagnostics: Optional[DataFinalDiagnostics] = None
    """
    Diagnostics after fixing, split into relevant vs other based on requested fix
    types
    """

    fix_types_used: Optional[List[Literal["dependency", "parsing", "css", "ai_fallback", "types", "ui", "sql"]]] = None
    """Fix types that were used"""

    initial_diagnostics: Optional[DataInitialDiagnostics] = None
    """
    Diagnostics before fixing, split into relevant vs other based on requested fix
    types
    """


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


class FixerRunResponse(BaseModel):
    data: Data
    """The actual response data"""

    error: Optional[Error] = None
    """The error from the API query"""

    meta: Optional[Meta] = None
    """Meta information"""
