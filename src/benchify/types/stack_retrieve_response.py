# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["StackRetrieveResponse"]


class StackRetrieveResponse(BaseModel):
    id: str
    """Stack identifier"""

    etag: str
    """ETag for caching"""

    phase: Literal["starting", "building", "deploying", "running", "failed", "stopped"]
    """Stack lifecycle phases"""

    last_error: Optional[str] = FieldInfo(alias="lastError", default=None)
    """Last error message (if failed)"""

    last_logs: Optional[List[str]] = FieldInfo(alias="lastLogs", default=None)
    """Recent log entries (truncated for size)"""

    ports: Optional[List[float]] = None
    """Active ports (if running)"""

    ready_at: Optional[str] = FieldInfo(alias="readyAt", default=None)
    """When stack became ready (ISO 8601)"""
