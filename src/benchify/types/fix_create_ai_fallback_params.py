# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = [
    "FixCreateAIFallbackParams",
    "File",
    "RemainingDiagnostics",
    "RemainingDiagnosticsFileToDiagnostic",
    "RemainingDiagnosticsFileToDiagnosticLocation",
    "Meta",
]


class FixCreateAIFallbackParams(TypedDict, total=False):
    files: Required[Iterable[File]]
    """List of files (potentially already fixed by standard fixers)"""

    remaining_diagnostics: Required[RemainingDiagnostics]
    """Diagnostics that remain after standard fixing"""

    template_path: Required[str]
    """Full path to the template"""

    event_id: str
    """Unique identifier for the event"""

    include_context: bool
    """Whether to include context in AI prompts"""

    max_attempts: float
    """Maximum number of AI fix attempts"""

    meta: Optional[Meta]
    """Meta information for the request"""


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
