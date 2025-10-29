# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["StackCreateAndRunResponse"]


class StackCreateAndRunResponse(BaseModel):
    id: str

    command: List[str]

    image: str

    status: str
