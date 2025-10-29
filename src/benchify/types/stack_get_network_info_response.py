# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["StackGetNetworkInfoResponse"]


class StackGetNetworkInfoResponse(BaseModel):
    id: str

    domains: List[str]

    has_networking: bool

    namespace: str

    service_name: str

    service_url: str
