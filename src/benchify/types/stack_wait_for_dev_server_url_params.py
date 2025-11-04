# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["StackWaitForDevServerURLParams"]


class StackWaitForDevServerURLParams(TypedDict, total=False):
    interval: str
    """Polling interval in ms"""

    api_timeout: Annotated[str, PropertyInfo(alias="timeout")]
    """Timeout in seconds"""
