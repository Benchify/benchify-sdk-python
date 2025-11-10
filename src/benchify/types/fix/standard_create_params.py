# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "StandardCreateParams",
    "File",
    "RemainingDiagnostics",
    "RemainingDiagnosticsFileToDiagnostic",
    "RemainingDiagnosticsFileToDiagnosticLocation",
    "Meta",
]


class StandardCreateParams(TypedDict, total=False):
    files: Required[Iterable[File]]
    """List of files to fix (can be output from step 1)"""

    remaining_diagnostics: Required[RemainingDiagnostics]
    """Diagnostics to fix (output from step 1 or previous fixes)"""

    bundle: bool
    """Whether to bundle the project after fixes"""

    event_id: str
    """Unique identifier for tracking"""

    fix_types: List[Literal["dependency", "parsing", "css", "ai_fallback", "types", "ui", "sql"]]
    """Types of standard fixes to apply"""

    meta: Optional[Meta]
    """Meta information for the request"""

    mode: Literal["project", "files"]
    """Fixer mode: 'project' for full analysis, 'files' for incremental"""

    template_path: str
    """Template path for project context"""


class File(TypedDict, total=False):
    contents: Required[str]
    """File contents"""

    path: Required[str]
    """Path to the file"""


class RemainingDiagnosticsFileToDiagnosticLocation(TypedDict, total=False):
    column: Required[Optional[float]]
    """Column number (1-based)"""

    line: Required[Optional[float]]
    """Line number (1-based)"""

    span: Required[float]
    """Span of the error"""

    starting_character_position: Required[Optional[float]]
    """Position of the first character of the error location in the source code"""


class RemainingDiagnosticsFileToDiagnostic(TypedDict, total=False):
    file_path: Required[str]
    """File where diagnostic occurs"""

    location: Required[RemainingDiagnosticsFileToDiagnosticLocation]
    """Location of the diagnostic"""

    message: Required[str]
    """Diagnostic message"""

    type: Required[str]
    """Type of the diagnostic"""

    code: Optional[float]
    """Code given by the diagnostic generator"""

    context: Optional[str]
    """Surrounding code context"""


class RemainingDiagnostics(TypedDict, total=False):
    file_to_diagnostics: Dict[str, Iterable[RemainingDiagnosticsFileToDiagnostic]]
    """Diagnostics grouped by file"""


class Meta(TypedDict, total=False):
    external_id: Optional[str]
    """Customer tracking identifier"""
