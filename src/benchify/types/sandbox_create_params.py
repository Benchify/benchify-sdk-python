# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import FileTypes, SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["SandboxCreateParams", "Blob", "BlobFilesManifest", "Options", "OptionsOptions", "OptionsOptionsRuntime"]


class SandboxCreateParams(TypedDict, total=False):
    blob: Blob

    files: SequenceNotStr[FileTypes]
    """Files to upload"""

    options: Options

    content_hash: Annotated[str, PropertyInfo(alias="Content-Hash")]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


class BlobFilesManifest(TypedDict, total=False):
    path: Required[str]

    size: Required[float]


class Blob(TypedDict, total=False):
    files_data: Required[str]

    files_manifest: Required[Iterable[BlobFilesManifest]]

    compressed_size: Annotated[float, PropertyInfo(alias="compressedSize")]

    format: Literal["gzip-base64"]


class OptionsOptionsRuntime(TypedDict, total=False):
    framework: Literal["react", "nextjs", "vue", "nuxt", "express", "fastify", "nest", "vite"]

    node_version: Annotated[str, PropertyInfo(alias="nodeVersion")]

    package_manager: Annotated[Literal["npm", "yarn", "pnpm"], PropertyInfo(alias="packageManager")]


class OptionsOptions(TypedDict, total=False):
    build_command: Annotated[str, PropertyInfo(alias="buildCommand")]

    environment: Dict[str, str]

    name: str

    port: float

    runtime: OptionsOptionsRuntime

    start_command: Annotated[str, PropertyInfo(alias="startCommand")]

    subdomain: str


class Options(TypedDict, total=False):
    options: OptionsOptions
