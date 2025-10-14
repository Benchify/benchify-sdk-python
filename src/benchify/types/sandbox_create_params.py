# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["SandboxCreateParams"]


class SandboxCreateParams(TypedDict, total=False):
    packed: Required[FileTypes]
    """Binary gzipped tar archive containing project files"""

    content_hash: Required[Annotated[str, PropertyInfo(alias="Content-Hash")]]

    idempotency_key: Required[Annotated[str, PropertyInfo(alias="Idempotency-Key")]]

    manifest: str
    """Optional JSON metadata as string"""

    options: str
    """Optional JSON configuration as string"""
