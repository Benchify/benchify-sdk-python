# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["StackUpdateParams"]


class StackUpdateParams(TypedDict, total=False):
    idempotency_key: Required[Annotated[str, PropertyInfo(alias="idempotency-key")]]
    """Unique key for idempotent requests"""

    bundle: FileTypes
    """Optional tar.zst bundle containing changed/added files"""

    manifest: FileTypes
    """Optional JSON manifest file with file metadata"""

    ops: str
    """Optional JSON string containing array of patch operations"""

    base_etag: Annotated[str, PropertyInfo(alias="base-etag")]
    """Current stack etag for conflict detection"""
