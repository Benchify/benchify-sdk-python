# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SandboxCreateResponse", "BuildStatus", "Runtime", "Service"]


class BuildStatus(BaseModel):
    phase: Literal["pending", "running", "completed", "failed"]

    duration: Optional[float] = None

    error: Optional[str] = None

    logs: Optional[str] = None


class Runtime(BaseModel):
    node_version: str = FieldInfo(alias="nodeVersion")

    package_manager: Literal["npm", "yarn", "pnpm"] = FieldInfo(alias="packageManager")

    port: float

    start_command: str = FieldInfo(alias="startCommand")

    type: Literal["node"]

    typescript: bool

    build_command: Optional[str] = FieldInfo(alias="buildCommand", default=None)

    framework: Optional[Literal["react", "nextjs", "vue", "nuxt", "express", "fastify", "nest", "vite", "vanilla"]] = (
        None
    )


class Service(BaseModel):
    id: str

    name: str

    phase: Literal["starting", "building", "deploying", "running", "failed", "stopped"]

    role: Literal["frontend", "backend", "worker", "database", "unknown"]

    workspace_path: str = FieldInfo(alias="workspacePath")

    port: Optional[float] = None


class SandboxCreateResponse(BaseModel):
    id: str

    content_hash: str = FieldInfo(alias="contentHash")

    etag: str

    kind: Literal["single", "stack"]

    phase: Literal["starting", "building", "deploying", "running", "failed", "stopped"]

    url: str

    build_status: Optional[BuildStatus] = FieldInfo(alias="buildStatus", default=None)

    idempotency_key: Optional[str] = FieldInfo(alias="idempotencyKey", default=None)

    runtime: Optional[Runtime] = None

    services: Optional[List[Service]] = None
