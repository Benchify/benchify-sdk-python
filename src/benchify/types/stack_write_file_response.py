# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["StackWriteFileResponse"]


class StackWriteFileResponse(BaseModel):
    host_path: Optional[str] = None

    message: Optional[str] = None

    method: Optional[str] = None

    sandbox_path: Optional[str] = None
