# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["FixerRunParams", "File", "FilesManifest", "Meta"]


class FixerRunParams(TypedDict, total=False):
    bundle: bool
    """Whether to bundle the project (experimental)"""

    event_id: str
    """Unique identifier for the event"""

    files: Optional[Iterable[File]]
    """List of files to process (legacy format)"""

    files_data: Optional[str]
    """Base64-encoded compressed file contents (packed format)"""

    files_manifest: Optional[Iterable[FilesManifest]]
    """File manifest for packed format: [{"path": "app.tsx", "size": 1024}, ...]"""

    fixes: List[Literal["dependency", "parsing", "css", "ai_fallback", "types", "ui", "sql"]]
    """Configuration for which fix types to apply"""

    meta: Optional[Meta]
    """Meta information for the request"""

    mode: Literal["project", "files"]
    """Fixer operating mode"""

    response_encoding: Literal["json", "blob"]
    """Response encoding format"""

    response_format: Literal["DIFF", "CHANGED_FILES", "ALL_FILES"]
    """Format for the response (diff, changed_files, or all_files)"""

    template_id: Optional[str]
    """ID of the template to use"""

    template_path: str
    """Full path to the template"""


class File(TypedDict, total=False):
    contents: Required[str]
    """File contents"""

    path: Required[str]
    """Path to the file"""


class FilesManifest(TypedDict, total=False):
    path: Required[str]
    """File path relative to project root"""

    size: Required[float]
    """File size in bytes"""

    digest: str
    """File content hash (optional)"""


class Meta(TypedDict, total=False):
    external_id: Optional[str]
    """Customer tracking identifier"""
