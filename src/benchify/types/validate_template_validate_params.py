# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ValidateTemplateValidateParams", "Meta"]


class ValidateTemplateValidateParams(TypedDict, total=False):
    meta: Optional[Meta]
    """Meta information for the request"""

    response_format: Optional[Literal["DIFF", "CHANGED_FILES", "ALL_FILES"]]
    """Format for the response"""

    body_template_id_1: Annotated[Optional[str], PropertyInfo(alias="template_id")]
    """ID of the template"""

    template_path: Optional[str]
    """Full path to the template to use for validation"""

    body_template_id_2: Annotated[str, PropertyInfo(alias="templateId")]

    template_name: Annotated[str, PropertyInfo(alias="templateName")]


class Meta(TypedDict, total=False):
    external_id: Optional[str]
    """Customer tracking identifier"""
