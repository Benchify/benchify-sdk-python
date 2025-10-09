# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["FixerRunParams", "File", "Meta"]


class FixerRunParams(TypedDict, total=False):
    bundle: bool
    """Whether to bundle the project (experimental)"""

    files: Optional[Iterable[File]]
    """List of files to process (legacy format)"""

    files_data: Optional[str]
    """Base64-encoded compressed file contents (packed format)"""

    files_manifest: Optional[Iterable[Dict[str, object]]]
    """File manifest for packed format: [{"path": "app.tsx", "size": 1024}, ...]"""

    fixes: List[Literal["dependency", "parsing", "css", "ai_fallback", "types", "ui", "sql"]]
    """Configuration for which fix types to apply"""

    meta: Optional[Meta]
    """Meta information for API requests"""

    mode: Literal["project", "files"]
    """Fixer operating mode: 'project' expects full project, 'files' expects subset"""

    response_format: Literal["DIFF", "CHANGED_FILES", "ALL_FILES"]
    """Format for the response (diff, changed_files, or all_files)"""

    template_id: Optional[str]
    """ID of the template to use for the fixer process"""


class File(TypedDict, total=False):
    contents: Required[str]
    """File contents"""

    path: Required[str]
    """Path to the file"""


class Meta(TypedDict, total=False):
    external_id: Optional[str]
    """Customer tracking identifier"""
