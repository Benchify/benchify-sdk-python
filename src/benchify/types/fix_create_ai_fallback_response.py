# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["FixCreateAIFallbackResponse", "Data", "DataFileResults", "Error", "Meta"]


class DataFileResults(BaseModel):
    confidence_scores: List[float]
    """Array of confidence scores for fixes applied"""

    fixed_content: str
    """The fixed file contents"""

    fixes_applied: float
    """Number of fixes applied"""

    remaining_issues: float
    """Number of issues still remaining"""

    status: str
    """Status of the fix operation (e.g., "FIXED", "NO_ISSUES", "FAILED")"""


class Data(BaseModel):
    execution_time: float
    """Time taken to execute AI fallback in seconds"""

    file_results: Dict[str, DataFileResults]
    """Per-file AI fix results keyed by file path"""

    files_fixed: float
    """Number of files that were fixed"""

    issues_remaining: float
    """Total number of issues still remaining"""

    issues_resolved: float
    """Total number of issues resolved"""

    success: bool
    """Whether the AI fallback was successful overall"""

    ai_suggestions: Optional[str] = None
    """Additional AI suggestions if available"""

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


class FixCreateAIFallbackResponse(BaseModel):
    data: Data
    """The actual response data"""

    error: Optional[Error] = None
    """The error from the API query"""

    meta: Optional[Meta] = None
    """Meta information"""
