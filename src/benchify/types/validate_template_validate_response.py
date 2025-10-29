# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ValidateTemplateValidateResponse"]


class ValidateTemplateValidateResponse(BaseModel):
    success: bool
    """Whether the template validation succeeded"""

    error: Optional[str] = None
    """Error message if validation failed"""
