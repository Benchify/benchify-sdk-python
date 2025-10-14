# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["SandboxUpdateParams"]


class SandboxUpdateParams(TypedDict, total=False):
    idempotency_key: Required[Annotated[str, PropertyInfo(alias="Idempotency-Key")]]

    manifest: str
    """
    JSON string containing patch metadata: { base, proposed, files: {...changed
    hashes...} }. Required when packed is present.
    """

    ops: str
    """Optional JSON string containing array of patch operations"""

    packed: FileTypes
    """Optional gzipped tar archive containing changed/added files"""

    base_commit: Annotated[str, PropertyInfo(alias="Base-Commit")]

    base_etag: Annotated[str, PropertyInfo(alias="Base-Etag")]
