# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = [
    "FixCreateAIFallbackResponse",
    "Data",
    "DataFileResult",
    "DataSuggestedChanges",
    "DataSuggestedChangesAllFile",
    "DataSuggestedChangesChangedFile",
    "Error",
    "Meta",
]


class DataFileResult(BaseModel):
    confidence_score: float
    """Confidence score of the fix (0-1)"""

    issues_remaining: float
    """Number of issues still remaining"""

    issues_resolved: float
    """Number of issues resolved"""

    path: str
    """Path of the file"""

    success: bool
    """Whether the AI fix was successful"""

    alternative_suggestions: Optional[List[str]] = None
    """Alternative fix suggestions"""


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


class Data(BaseModel):
    file_results: List[DataFileResult]
    """Per-file AI fix results"""

    files_fixed: float
    """Number of files that were fixed"""

    fixer_version: str
    """Version of the fixer"""

    issues_remaining: float
    """Total number of issues still remaining"""

    issues_resolved: float
    """Total number of issues resolved"""

    success: bool
    """Whether the AI fallback was successful overall"""

    suggested_changes: DataSuggestedChanges
    """Suggested changes from AI fixes"""


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
