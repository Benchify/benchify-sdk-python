# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["SandboxCreateParams"]


class SandboxCreateParams(TypedDict, total=False):
    packed: Required[FileTypes]
    """Binary packed file (tar+gz or tar+zstd) containing project files"""

    options: str
    """JSON string with sandbox options (optional)"""

    content_hash: Annotated[str, PropertyInfo(alias="Content-Hash")]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
