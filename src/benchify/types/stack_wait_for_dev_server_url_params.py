# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["StackWaitForDevServerURLParams"]


class StackWaitForDevServerURLParams(TypedDict, total=False):
    interval: float
    """Polling interval in milliseconds"""

    wait_timeout: float
    """Timeout in seconds"""
