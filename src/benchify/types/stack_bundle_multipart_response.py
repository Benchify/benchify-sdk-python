# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["StackBundleMultipartResponse", "Manifest", "ManifestFile"]


class ManifestFile(BaseModel):
    contents: str

    path: str


class Manifest(BaseModel):
    files: List[ManifestFile]

    url: Optional[str] = None


class StackBundleMultipartResponse(BaseModel):
    content: str

    path: str

    manifest: Optional[Manifest] = None
