# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BundleCreateParams"]


class BundleCreateParams(TypedDict, total=False):
    entrypoint: Required[str]

    tarball_base64: Required[str]

    tarball_filename: str
