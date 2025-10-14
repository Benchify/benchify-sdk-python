# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SandboxRetrieveResponse"]


class SandboxRetrieveResponse(BaseModel):
    id: str

    etag: str

    phase: Literal["starting", "building", "deploying", "running", "failed", "stopped"]

    last_error: Optional[str] = FieldInfo(alias="lastError", default=None)

    last_logs: Optional[List[str]] = FieldInfo(alias="lastLogs", default=None)

    ports: Optional[List[float]] = None

    ready_at: Optional[str] = FieldInfo(alias="readyAt", default=None)
