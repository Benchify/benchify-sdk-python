# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FixerRunParams", "File", "Fixes", "Meta"]


class FixerRunParams(TypedDict, total=False):
    files: Required[Iterable[File]]
    """List of files to process"""

    bundle: bool
    """Whether to bundle the project (experimental)"""

    fix_types: List[Literal["import_export", "string_literals", "css", "tailwind", "ai_fallback", "types"]]
    """Configuration for which fix types to apply"""

    fixes: Optional[Fixes]
    """DEPRECATED: legacy boolean flags for which fixes to apply."""

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
    css: Optional[bool]
    """Whether to fix CSS issues"""

    imports: Optional[bool]
    """Whether to fix import issues"""

    react: Optional[bool]
    """Whether to fix React issues"""

    string_literals: Annotated[Optional[bool], PropertyInfo(alias="stringLiterals")]
    """Whether to fix string literal issues"""

    tailwind: Optional[bool]
    """Whether to fix Tailwind issues"""

    ts_suggestions: Annotated[Optional[bool], PropertyInfo(alias="tsSuggestions")]
    """Whether to fix TypeScript suggestions"""


class Meta(TypedDict, total=False):
    external_id: Optional[str]
    """Customer tracking identifier"""
