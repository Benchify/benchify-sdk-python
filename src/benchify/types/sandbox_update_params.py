# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["SandboxUpdateParams"]


class SandboxUpdateParams(TypedDict, total=False):
    ops: str
    """JSON array of patch operations"""

    packed: FileTypes
    """tar+zstd or tar+gz containing changed/added files"""

    base_etag: Annotated[str, PropertyInfo(alias="Base-Etag")]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
