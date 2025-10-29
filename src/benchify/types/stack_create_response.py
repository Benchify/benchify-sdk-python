# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["StackCreateResponse", "BuildStatus", "Service"]


class BuildStatus(BaseModel):
    phase: Literal["pending", "running", "completed", "failed"]
    """Build phase states"""

    duration: Optional[float] = None
    """Build duration in milliseconds"""

    error: Optional[str] = None
    """Error message if failed"""

    logs: Optional[str] = None
    """Build logs (truncated)"""


class Service(BaseModel):
    id: str
    """Service identifier"""

    name: str
    """Service name"""

    phase: Literal["starting", "building", "deploying", "running", "failed", "stopped"]
    """Stack lifecycle phases"""

    role: Literal["frontend", "backend", "fullstack", "worker", "database", "unknown"]
    """Service roles in a stack"""

    workspace_path: str = FieldInfo(alias="workspacePath")
    """Workspace path relative to project root"""

    port: Optional[float] = None
    """Port (if applicable)"""


class StackCreateResponse(BaseModel):
    id: str
    """Stack identifier"""

    content_hash: str = FieldInfo(alias="contentHash")
    """Content hash for deduplication"""

    etag: str
    """ETag for caching/optimistic updates"""

    kind: Literal["single", "stack"]
    """Stack kinds"""

    phase: Literal["starting", "building", "deploying", "running", "failed", "stopped"]
    """Stack lifecycle phases"""

    url: str
    """Live URL for the stack"""

    build_status: Optional[BuildStatus] = FieldInfo(alias="buildStatus", default=None)
    """Build status information"""

    idempotency_key: Optional[str] = FieldInfo(alias="idempotencyKey", default=None)
    """Idempotency key echo"""

    services: Optional[List[Service]] = None
    """Services in the stack"""
