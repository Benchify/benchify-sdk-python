# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["FileChange"]


class FileChange(BaseModel):
    contents: str
    """Contents of the file"""

    path: str
    """Path of the file"""
