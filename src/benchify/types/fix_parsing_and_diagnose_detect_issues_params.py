# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["FixParsingAndDiagnoseDetectIssuesParams", "File", "Meta"]


class FixParsingAndDiagnoseDetectIssuesParams(TypedDict, total=False):
    event_id: str
    """Unique identifier for the event"""

    files: Optional[Iterable[File]]
    """List of files to analyze (JSON format with inline contents).

    For large projects, use multipart/form-data with manifest + bundle instead.
    """

    meta: Optional[Meta]
    """Meta information for the request"""

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
