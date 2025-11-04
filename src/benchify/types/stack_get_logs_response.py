# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["StackGetLogsResponse", "Service"]


class Service(BaseModel):
    id: str
    """Service ID"""

    line_count: float = FieldInfo(alias="lineCount")
    """Number of log lines"""

    logs: str
    """Logs for this service"""

    name: str
    """Service name"""

    role: Literal["frontend", "backend", "fullstack", "worker", "database", "unknown"]
    """Service roles in a stack"""


class StackGetLogsResponse(BaseModel):
    id: str
    """Stack ID"""

    services: List[Service]
    """Logs organized by service"""

    total_line_count: float = FieldInfo(alias="totalLineCount")
    """Total log lines across all services"""

    combined_logs: Optional[str] = FieldInfo(alias="combinedLogs", default=None)
    """Combined logs from all services (legacy support)"""
