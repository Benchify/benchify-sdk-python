# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["StackCreateParams"]


class StackCreateParams(TypedDict, total=False):
    bundle: Required[FileTypes]
    """Tar.zst bundle containing project files"""

    manifest: Required[FileTypes]
    """JSON manifest file containing file metadata and tree hashes"""

    idempotency_key: Required[Annotated[str, PropertyInfo(alias="idempotency-key")]]
    """Unique key for idempotent requests"""

    options: str
    """Optional JSON configuration string"""

    content_hash: Annotated[str, PropertyInfo(alias="content-hash")]
    """SHA-256 hash of the bundle for deduplication"""
