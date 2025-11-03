# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["StackUpdateResponse"]


class StackUpdateResponse(BaseModel):
    id: str
    """Stack identifier"""

    applied: float
    """Number of operations applied"""

    etag: str
    """New ETag after changes"""

    phase: Literal["starting", "building", "deploying", "running", "failed", "stopped"]
    """Stack lifecycle phases"""

    restarted: bool
    """Whether stack was restarted"""

    affected_services: Optional[List[str]] = FieldInfo(alias="affectedServices", default=None)
    """Services affected by patch (for multi-service stacks)"""

    warnings: Optional[List[str]] = None
    """Optional warnings if patch partially failed"""
