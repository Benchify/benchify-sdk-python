# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["StackGetLogsParams"]


class StackGetLogsParams(TypedDict, total=False):
    tail: str
    """Number of log lines to return per service"""
