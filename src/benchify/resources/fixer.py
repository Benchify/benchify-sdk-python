# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import fixer_run_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.fixer_run_response import FixerRunResponse

__all__ = ["FixerResource", "AsyncFixerResource"]


class FixerResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FixerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Benchify/benchify-sdk-python#accessing-raw-response-data-eg-headers
        """
        return FixerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FixerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Benchify/benchify-sdk-python#with_streaming_response
        """
        return FixerResourceWithStreamingResponse(self)

    def run(
        self,
        *,
        files: Iterable[fixer_run_params.File],
        fix_types: List[
            Literal[
                "import_export", "string_literals", "ts_suggestions", "css", "tailwind", "react", "ai_fallback", "types"
            ]
        ]
        | NotGiven = NOT_GIVEN,
        fixes: Optional[fixer_run_params.Fixes] | NotGiven = NOT_GIVEN,
        meta: Optional[fixer_run_params.Meta] | NotGiven = NOT_GIVEN,
        response_format: Literal["DIFF", "CHANGED_FILES", "ALL_FILES"] | NotGiven = NOT_GIVEN,
        template_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FixerRunResponse:
        """
        Handle fixer requests to process and fix TypeScript files.

        Args:
          files: List of files to process

          fix_types: Configuration for which fix types to apply

          fixes: DEPRECATED: legacy boolean flags for which fixes to apply.

          meta: Meta information for API requests

          response_format: Format for the response (diff, changed_files, or all_files)

          template_id: ID of the template to use for the fixer process

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/fixer",
            body=maybe_transform(
                {
                    "files": files,
                    "fix_types": fix_types,
                    "fixes": fixes,
                    "meta": meta,
                    "response_format": response_format,
                    "template_id": template_id,
                },
                fixer_run_params.FixerRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FixerRunResponse,
        )


class AsyncFixerResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFixerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Benchify/benchify-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFixerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFixerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Benchify/benchify-sdk-python#with_streaming_response
        """
        return AsyncFixerResourceWithStreamingResponse(self)

    async def run(
        self,
        *,
        files: Iterable[fixer_run_params.File],
        fix_types: List[
            Literal[
                "import_export", "string_literals", "ts_suggestions", "css", "tailwind", "react", "ai_fallback", "types"
            ]
        ]
        | NotGiven = NOT_GIVEN,
        fixes: Optional[fixer_run_params.Fixes] | NotGiven = NOT_GIVEN,
        meta: Optional[fixer_run_params.Meta] | NotGiven = NOT_GIVEN,
        response_format: Literal["DIFF", "CHANGED_FILES", "ALL_FILES"] | NotGiven = NOT_GIVEN,
        template_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FixerRunResponse:
        """
        Handle fixer requests to process and fix TypeScript files.

        Args:
          files: List of files to process

          fix_types: Configuration for which fix types to apply

          fixes: DEPRECATED: legacy boolean flags for which fixes to apply.

          meta: Meta information for API requests

          response_format: Format for the response (diff, changed_files, or all_files)

          template_id: ID of the template to use for the fixer process

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/fixer",
            body=await async_maybe_transform(
                {
                    "files": files,
                    "fix_types": fix_types,
                    "fixes": fixes,
                    "meta": meta,
                    "response_format": response_format,
                    "template_id": template_id,
                },
                fixer_run_params.FixerRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FixerRunResponse,
        )


class FixerResourceWithRawResponse:
    def __init__(self, fixer: FixerResource) -> None:
        self._fixer = fixer

        self.run = to_raw_response_wrapper(
            fixer.run,
        )


class AsyncFixerResourceWithRawResponse:
    def __init__(self, fixer: AsyncFixerResource) -> None:
        self._fixer = fixer

        self.run = async_to_raw_response_wrapper(
            fixer.run,
        )


class FixerResourceWithStreamingResponse:
    def __init__(self, fixer: FixerResource) -> None:
        self._fixer = fixer

        self.run = to_streamed_response_wrapper(
            fixer.run,
        )


class AsyncFixerResourceWithStreamingResponse:
    def __init__(self, fixer: AsyncFixerResource) -> None:
        self._fixer = fixer

        self.run = async_to_streamed_response_wrapper(
            fixer.run,
        )
