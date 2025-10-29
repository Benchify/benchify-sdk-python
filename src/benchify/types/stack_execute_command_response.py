# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["StackExecuteCommandResponse"]


class StackExecuteCommandResponse(BaseModel):
    exit_code: float = FieldInfo(alias="exitCode")

    stderr: str

    stdout: str
