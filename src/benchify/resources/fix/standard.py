# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.fix import standard_create_params
from ..._base_client import make_request_options
from ...types.fix.standard_create_response import StandardCreateResponse

__all__ = ["StandardResource", "AsyncStandardResource"]


class StandardResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StandardResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Benchify/benchify-sdk-python#accessing-raw-response-data-eg-headers
        """
        return StandardResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StandardResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Benchify/benchify-sdk-python#with_streaming_response
        """
        return StandardResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        files: Iterable[standard_create_params.File],
        remaining_diagnostics: standard_create_params.RemainingDiagnostics,
        bundle: bool | Omit = omit,
        event_id: str | Omit = omit,
        fix_types: List[Literal["dependency", "parsing", "css", "ai_fallback", "types", "ui", "sql"]] | Omit = omit,
        meta: Optional[standard_create_params.Meta] | Omit = omit,
        mode: Literal["project", "files"] | Omit = omit,
        template_path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StandardCreateResponse:
        """Standard fixes endpoint - applies non-parsing fixes.

        Phase 2 of the 3-phase
        architecture. Takes the output from Phase 1 (detection) and applies CSS, UI,
        dependency, and type fixes. The output can be used as input to Phase 3 (AI
        fallback).

        Args:
          files: List of files to fix (can be output from step 1)

          remaining_diagnostics: Diagnostics to fix (output from step 1 or previous fixes)

          bundle: Whether to bundle the project after fixes

          event_id: Unique identifier for tracking

          fix_types: Types of standard fixes to apply

          meta: Meta information for the request

          mode: Fixer mode: 'project' for full analysis, 'files' for incremental

          template_path: Template path for project context

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/fix-standard",
            body=maybe_transform(
                {
                    "files": files,
                    "remaining_diagnostics": remaining_diagnostics,
                    "bundle": bundle,
                    "event_id": event_id,
                    "fix_types": fix_types,
                    "meta": meta,
                    "mode": mode,
                    "template_path": template_path,
                },
                standard_create_params.StandardCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StandardCreateResponse,
        )


class AsyncStandardResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStandardResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Benchify/benchify-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStandardResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStandardResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Benchify/benchify-sdk-python#with_streaming_response
        """
        return AsyncStandardResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        files: Iterable[standard_create_params.File],
        remaining_diagnostics: standard_create_params.RemainingDiagnostics,
        bundle: bool | Omit = omit,
        event_id: str | Omit = omit,
        fix_types: List[Literal["dependency", "parsing", "css", "ai_fallback", "types", "ui", "sql"]] | Omit = omit,
        meta: Optional[standard_create_params.Meta] | Omit = omit,
        mode: Literal["project", "files"] | Omit = omit,
        template_path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StandardCreateResponse:
        """Standard fixes endpoint - applies non-parsing fixes.

        Phase 2 of the 3-phase
        architecture. Takes the output from Phase 1 (detection) and applies CSS, UI,
        dependency, and type fixes. The output can be used as input to Phase 3 (AI
        fallback).

        Args:
          files: List of files to fix (can be output from step 1)

          remaining_diagnostics: Diagnostics to fix (output from step 1 or previous fixes)

          bundle: Whether to bundle the project after fixes

          event_id: Unique identifier for tracking

          fix_types: Types of standard fixes to apply

          meta: Meta information for the request

          mode: Fixer mode: 'project' for full analysis, 'files' for incremental

          template_path: Template path for project context

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/fix-standard",
            body=await async_maybe_transform(
                {
                    "files": files,
                    "remaining_diagnostics": remaining_diagnostics,
                    "bundle": bundle,
                    "event_id": event_id,
                    "fix_types": fix_types,
                    "meta": meta,
                    "mode": mode,
                    "template_path": template_path,
                },
                standard_create_params.StandardCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StandardCreateResponse,
        )


class StandardResourceWithRawResponse:
    def __init__(self, standard: StandardResource) -> None:
        self._standard = standard

        self.create = to_raw_response_wrapper(
            standard.create,
        )


class AsyncStandardResourceWithRawResponse:
    def __init__(self, standard: AsyncStandardResource) -> None:
        self._standard = standard

        self.create = async_to_raw_response_wrapper(
            standard.create,
        )


class StandardResourceWithStreamingResponse:
    def __init__(self, standard: StandardResource) -> None:
        self._standard = standard

        self.create = to_streamed_response_wrapper(
            standard.create,
        )


class AsyncStandardResourceWithStreamingResponse:
    def __init__(self, standard: AsyncStandardResource) -> None:
        self._standard = standard

        self.create = async_to_streamed_response_wrapper(
            standard.create,
        )
