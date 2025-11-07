# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["StackResetParams"]


class StackResetParams(TypedDict, total=False):
    tarball_base64: Required[str]
    """Base64-encoded tarball content"""

    tarball_filename: str
    """Optional tarball filename"""
