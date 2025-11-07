# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["StackResetResponse"]


class StackResetResponse(BaseModel):
    message: str

    id: Optional[str] = None
