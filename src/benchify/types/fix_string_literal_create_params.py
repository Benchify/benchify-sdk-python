# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["FixStringLiteralCreateParams", "File", "Meta"]


class FixStringLiteralCreateParams(TypedDict, total=False):
    file: Required[File]
    """File to process"""

    event_id: Optional[str]
    """Unique identifier for the event"""

    meta: Optional[Meta]
    """Meta information for the request"""


class File(TypedDict, total=False):
    contents: Required[str]
    """File contents"""

    path: Required[str]
    """Path to the file"""


class Meta(TypedDict, total=False):
    external_id: Optional[str]
    """Customer tracking identifier"""
