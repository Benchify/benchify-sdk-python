# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["StackWriteFileParams"]


class StackWriteFileParams(TypedDict, total=False):
    content: Required[str]
    """File contents"""

    path: Required[str]
    """Absolute path inside the sandbox"""
