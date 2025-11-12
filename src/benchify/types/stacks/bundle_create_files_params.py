# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["BundleCreateFilesParams", "File"]


class BundleCreateFilesParams(TypedDict, total=False):
    entrypoint: Required[str]

    files: Required[Iterable[File]]
    """Files to bundle"""

    tarball_filename: str


class File(TypedDict, total=False):
    content: Required[str]

    path: Required[str]
