# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["FixerRunParams", "File", "Meta"]


class FixerRunParams(TypedDict, total=False):
    bundle: bool
    """Whether to bundle the project (experimental)"""

    event_id: str
    """Unique identifier for the event"""

    files: Optional[Iterable[File]]
    """List of files to process (JSON format with inline contents).

    For large projects, use multipart/form-data with manifest + bundle instead.
    """

    fixes: List[Literal["dependency", "parsing", "css", "ai_fallback", "types", "ui", "sql"]]
    """Configuration for which fix types to apply"""

    meta: Optional[Meta]
    """Meta information for the request"""

    mode: Literal["project", "files"]
    """Fixer operating mode"""

    response_encoding: Literal["json", "multipart"]
    """
    Response encoding: "json" for inline file contents in JSON, "multipart" for
    multipart/form-data with tar.zst bundle + manifest
    """

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


class Meta(TypedDict, total=False):
    external_id: Optional[str]
    """Customer tracking identifier"""
