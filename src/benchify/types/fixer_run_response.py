# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .file_change import FileChange
from .shared.response_meta import ResponseMeta

__all__ = [
    "FixerRunResponse",
    "Data",
    "DataStatus",
    "DataSuggestedChanges",
    "DataSuggestedChangesDiffFormat",
    "DataSuggestedChangesChangedFilesFormat",
    "DataSuggestedChangesAllFilesFormat",
    "Error",
]


class DataStatus(BaseModel):
    file_to_status: Optional[Dict[str, Literal["FIXED", "PARTIALLY_FIXED", "FAILED", "NO_ISSUES_FOUND"]]] = None
    """Fix status of each file sent."""


class DataSuggestedChangesDiffFormat(BaseModel):
    diff: Optional[str] = None
    """Git diff of changes made"""


class DataSuggestedChangesChangedFilesFormat(BaseModel):
    changed_files: Optional[List[FileChange]] = None
    """List of changed files with their new contents"""


class DataSuggestedChangesAllFilesFormat(BaseModel):
    all_files: Optional[List[FileChange]] = None
    """List of all files with their current contents"""


DataSuggestedChanges: TypeAlias = Union[
    DataSuggestedChangesDiffFormat, DataSuggestedChangesChangedFilesFormat, DataSuggestedChangesAllFilesFormat, None
]


class Data(BaseModel):
    files_processed: int
    """Number of files processed"""

    status: DataStatus
    """Final per-file status after fixing"""

    fixed_files: Optional[Dict[str, object]] = None
    """Information about fixed files"""

    suggested_changes: Optional[DataSuggestedChanges] = None
    """Changes made by the fixer in the requested format"""


class Error(BaseModel):
    code: str
    """The error code"""

    message: str
    """The error message"""

    details: Optional[str] = None
    """Details about what caused the error, if available"""

    suggestions: Optional[List[str]] = None
    """Potential suggestions about how to fix the error, if applicable"""


class FixerRunResponse(BaseModel):
    data: Data
    """The actual response data"""

    error: Optional[Error] = None
    """The error from the API query"""

    meta: Optional[ResponseMeta] = None
    """Meta information"""
