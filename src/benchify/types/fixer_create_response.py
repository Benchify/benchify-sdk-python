# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .file_change import FileChange
from .fix_type_name import FixTypeName

__all__ = [
    "FixerCreateResponse",
    "Data",
    "DataStatus",
    "DataBundle",
    "DataSuggestedChanges",
    "DataSuggestedChangesDiffFormat",
    "DataSuggestedChangesChangedFilesFormat",
    "DataSuggestedChangesAllFilesFormat",
    "Error",
    "Meta",
]


class DataStatus(BaseModel):
    composite_status: Literal[
        "FIXED_EVERYTHING", "FIXED_REQUESTED", "PARTIALLY_FIXED", "NO_REQUESTED_ISSUES", "NO_ISSUES", "FAILED"
    ]

    file_to_composite_status: Optional[
        Dict[
            str,
            Literal[
                "FIXED_EVERYTHING", "FIXED_REQUESTED", "PARTIALLY_FIXED", "NO_REQUESTED_ISSUES", "NO_ISSUES", "FAILED"
            ],
        ]
    ] = None
    """Status of each file."""


class DataBundle(BaseModel):
    build_system: Literal[
        "OLIVE_TEMPLATE", "VITE_SUBDIR", "VITE_ROOT", "NEXT", "ESBUILD", "WEBPACK", "PARCEL", "UNKNOWN"
    ]
    """The detected project/build system type"""

    status: Literal["SUCCESS", "FAILED", "NOT_ATTEMPTED", "PARTIAL_SUCCESS"]
    """Overall status of the bundling operation"""

    template_path: str
    """Template path used for bundling"""

    files: Optional[List[FileChange]] = None
    """Successfully bundled files"""


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
    status: DataStatus
    """Final per-file status after fixing"""

    bundle: Optional[DataBundle] = None
    """Information about the bundling process and results"""

    fix_types_used: Optional[List[FixTypeName]] = None
    """List of fix types that were actually applied during the fixer run"""

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


class Meta(BaseModel):
    external_id: Optional[str] = None
    """Customer tracking identifier"""

    trace_id: Optional[str] = None
    """Unique trace identifier for the request"""


class FixerCreateResponse(BaseModel):
    data: Data
    """The actual response data"""

    error: Optional[Error] = None
    """The error from the API query"""

    meta: Optional[Meta] = None
    """Meta information"""
