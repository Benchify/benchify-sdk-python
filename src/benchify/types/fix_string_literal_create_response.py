# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FixStringLiteralCreateResponse", "Data", "DataStrategyStatistic", "Error", "Meta"]


class DataStrategyStatistic(BaseModel):
    strategy_name: str

    version_hash: str

    fixes_applied: Optional[bool] = None

    fixes_fired: Optional[bool] = None


class Data(BaseModel):
    contents: str
    """The file contents (original or fixed)"""

    fixer_version: str
    """Version of the fixer"""

    status: Literal["FIXED", "ALREADY_FIXED", "NO_ISSUES_FOUND", "fix_applied"]
    """Status of the fix operation"""

    strategy_statistics: List[DataStrategyStatistic]
    """Strategy statistics for the single file"""

    error: Optional[str] = None
    """Error details if status is 'error'"""


class Error(BaseModel):
    code: str
    """The error code"""

    message: str
    """The error message"""

    details: Optional[Dict[str, object]] = None
    """Details about what caused the error"""


class Meta(BaseModel):
    external_id: Optional[str] = None
    """Customer tracking identifier"""

    trace_id: Optional[str] = None
    """Unique trace identifier for the request"""


class FixStringLiteralCreateResponse(BaseModel):
    data: Data
    """The actual response data"""

    error: Optional[Error] = None
    """The error from the API query"""

    meta: Optional[Meta] = None
    """Meta information"""
