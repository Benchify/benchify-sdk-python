# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import FileTypes

__all__ = ["StackBundleMultipartParams"]


class StackBundleMultipartParams(TypedDict, total=False):
    manifest: Required[str]
    """JSON string containing bundler manifest (must include entrypoint)"""

    tarball: Required[FileTypes]
    """Tar.zst project archive"""
