# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FixerRunParams", "File", "Fixes", "Meta"]


class FixerRunParams(TypedDict, total=False):
    files: Required[Iterable[File]]
    """List of files to process"""

    fixes: Optional[Fixes]
    """Configuration object for specifying which fixes to apply"""

    meta: Optional[Meta]
    """Meta information for API requests"""

    response_format: Literal["DIFF", "CHANGED_FILES", "ALL_FILES"]
    """Format for the response (diff, changed_files, or all_files)"""

    template_id: Optional[str]
    """ID of the template to use for the fixer process"""


class File(TypedDict, total=False):
    contents: Required[str]
    """Original contents of the file before any modifications"""

    path: Required[str]
    """Path to the file"""


class Fixes(TypedDict, total=False):
    css: bool
    """Whether to fix CSS issues"""

    imports: bool
    """Whether to fix import issues"""

    react: bool
    """Whether to fix React issues"""

    string_literals: Annotated[bool, PropertyInfo(alias="stringLiterals")]
    """Whether to fix string literal issues"""

    tailwind: bool
    """Whether to fix Tailwind issues"""

    ts_suggestions: Annotated[bool, PropertyInfo(alias="tsSuggestions")]
    """Whether to fix TypeScript suggestions"""


class Meta(TypedDict, total=False):
    external_id: Optional[str]
    """Customer tracking identifier"""
