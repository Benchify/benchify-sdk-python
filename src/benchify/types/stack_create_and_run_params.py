# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["StackCreateAndRunParams"]


class StackCreateAndRunParams(TypedDict, total=False):
    command: Required[SequenceNotStr[str]]
    """Command to run"""

    image: Required[str]
    """Docker image to use"""

    ttl_seconds: float
    """Time to live in seconds"""

    wait: bool
    """Wait for container to be ready"""
