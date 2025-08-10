# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ResponseMeta"]


class ResponseMeta(BaseModel):
    external_id: Optional[str] = None
    """Customer tracking identifier"""

    trace_id: Optional[str] = None
    """Unique trace identifier for the request"""
