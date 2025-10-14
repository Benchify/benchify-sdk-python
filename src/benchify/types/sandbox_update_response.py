# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SandboxUpdateResponse"]


class SandboxUpdateResponse(BaseModel):
    id: str

    applied: float

    etag: str

    phase: Literal["starting", "building", "deploying", "running", "failed", "stopped"]

    restarted: bool

    affected_services: Optional[List[str]] = FieldInfo(alias="affectedServices", default=None)

    warnings: Optional[List[str]] = None
