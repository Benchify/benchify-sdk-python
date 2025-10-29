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
    "DataSuggestedChangesAllFilesManifest",
    "DataSuggestedChangesChangedFile",
    "DataSuggestedChangesChangedFilesManifest",
    "DataSuggestedChangesDiffManifest",
    "DataBundle",
    "DataBundleFile",
    "DataBundleFilesManifest",
    "DataFileToStrategyStatistic",
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


class DataSuggestedChangesAllFilesManifest(BaseModel):
    path: str
    """File path relative to project root"""

    size: float
    """File size in bytes"""

    digest: Optional[str] = None
    """File content hash (optional)"""


class DataSuggestedChangesChangedFile(BaseModel):
    contents: str
    """Contents of the file"""

    path: str
    """Path of the file"""


class DataSuggestedChangesChangedFilesManifest(BaseModel):
    path: str
    """File path relative to project root"""

    size: float
    """File size in bytes"""

    digest: Optional[str] = None
    """File content hash (optional)"""


class DataSuggestedChangesDiffManifest(BaseModel):
    path: str
    """File path relative to project root"""

    size: float
    """File size in bytes"""

    digest: Optional[str] = None
    """File content hash (optional)"""


class DataSuggestedChanges(BaseModel):
    all_files: Optional[List[DataSuggestedChangesAllFile]] = None
    """List of all files with their current contents"""

    all_files_data: Optional[str] = None
    """Base64-encoded compressed file contents"""

    all_files_manifest: Optional[List[DataSuggestedChangesAllFilesManifest]] = None
    """File manifest for blob format"""

    changed_files: Optional[List[DataSuggestedChangesChangedFile]] = None
    """List of changed files with their new contents"""

    changed_files_data: Optional[str] = None
    """Base64-encoded compressed file contents"""

    changed_files_manifest: Optional[List[DataSuggestedChangesChangedFilesManifest]] = None
    """File manifest for blob format"""

    diff: Optional[str] = None
    """Unified diff of changes"""

    diff_data: Optional[str] = None
    """Base64-encoded compressed diff data"""

    diff_manifest: Optional[List[DataSuggestedChangesDiffManifest]] = None
    """File manifest for blob format"""


class DataBundleFile(BaseModel):
    contents: str
    """Contents of the file"""

    path: str
    """Path of the file"""


class DataBundleFilesManifest(BaseModel):
    path: str
    """File path relative to project root"""

    size: float
    """File size in bytes"""

    digest: Optional[str] = None
    """File content hash (optional)"""


class DataBundle(BaseModel):
    build_system: str

    status: Literal["SUCCESS", "FAILED", "NOT_ATTEMPTED", "PARTIAL_SUCCESS"]

    template_path: str

    bundle_url: Optional[str] = None

    debug: Optional[Dict[str, str]] = None

    files: Optional[List[DataBundleFile]] = None

    files_data: Optional[str] = None

    files_manifest: Optional[List[DataBundleFilesManifest]] = None


class DataFileToStrategyStatistic(BaseModel):
    strategy_name: str

    version_hash: str

    fixes_applied: Optional[bool] = None

    fixes_fired: Optional[bool] = None


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

    final_diagnostics: Optional[object] = None
    """Diagnostics after fixing"""

    fix_types_used: Optional[List[Literal["dependency", "parsing", "css", "ai_fallback", "types", "ui", "sql"]]] = None
    """Fix types that were used"""

    initial_diagnostics: Optional[object] = None
    """Diagnostics before fixing"""


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
