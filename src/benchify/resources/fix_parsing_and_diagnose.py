# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import fix_parsing_and_diagnose_detect_issues_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.fix_parsing_and_diagnose_detect_issues_response import FixParsingAndDiagnoseDetectIssuesResponse

__all__ = ["FixParsingAndDiagnoseResource", "AsyncFixParsingAndDiagnoseResource"]


class FixParsingAndDiagnoseResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FixParsingAndDiagnoseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Benchify/benchify-sdk-python#accessing-raw-response-data-eg-headers
        """
        return FixParsingAndDiagnoseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FixParsingAndDiagnoseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Benchify/benchify-sdk-python#with_streaming_response
        """
        return FixParsingAndDiagnoseResourceWithStreamingResponse(self)

    def detect_issues(
        self,
        *,
        event_id: str | Omit = omit,
        files: Optional[Iterable[fix_parsing_and_diagnose_detect_issues_params.File]] | Omit = omit,
        meta: Optional[fix_parsing_and_diagnose_detect_issues_params.Meta] | Omit = omit,
        template_path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FixParsingAndDiagnoseDetectIssuesResponse:
        """Fast detection endpoint for quick diagnostic results.

        Phase 1 of the 3-phase
        architecture. Returns issues quickly (within 1-3 seconds) and provides metadata
        about available fixes and time estimates. Does not apply any fixes, only
        analyzes code.

        Args:
          event_id: Unique identifier for the event

          files: List of files to analyze (JSON format with inline contents). For large projects,
              use multipart/form-data with manifest + bundle instead.

          meta: Meta information for the request

          template_path: Full path to the template

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/fix-parsing-and-diagnose",
            body=maybe_transform(
                {
                    "event_id": event_id,
                    "files": files,
                    "meta": meta,
                    "template_path": template_path,
                },
                fix_parsing_and_diagnose_detect_issues_params.FixParsingAndDiagnoseDetectIssuesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FixParsingAndDiagnoseDetectIssuesResponse,
        )


class AsyncFixParsingAndDiagnoseResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFixParsingAndDiagnoseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Benchify/benchify-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFixParsingAndDiagnoseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFixParsingAndDiagnoseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Benchify/benchify-sdk-python#with_streaming_response
        """
        return AsyncFixParsingAndDiagnoseResourceWithStreamingResponse(self)

    async def detect_issues(
        self,
        *,
        event_id: str | Omit = omit,
        files: Optional[Iterable[fix_parsing_and_diagnose_detect_issues_params.File]] | Omit = omit,
        meta: Optional[fix_parsing_and_diagnose_detect_issues_params.Meta] | Omit = omit,
        template_path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FixParsingAndDiagnoseDetectIssuesResponse:
        """Fast detection endpoint for quick diagnostic results.

        Phase 1 of the 3-phase
        architecture. Returns issues quickly (within 1-3 seconds) and provides metadata
        about available fixes and time estimates. Does not apply any fixes, only
        analyzes code.

        Args:
          event_id: Unique identifier for the event

          files: List of files to analyze (JSON format with inline contents). For large projects,
              use multipart/form-data with manifest + bundle instead.

          meta: Meta information for the request

          template_path: Full path to the template

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/fix-parsing-and-diagnose",
            body=await async_maybe_transform(
                {
                    "event_id": event_id,
                    "files": files,
                    "meta": meta,
                    "template_path": template_path,
                },
                fix_parsing_and_diagnose_detect_issues_params.FixParsingAndDiagnoseDetectIssuesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FixParsingAndDiagnoseDetectIssuesResponse,
        )


class FixParsingAndDiagnoseResourceWithRawResponse:
    def __init__(self, fix_parsing_and_diagnose: FixParsingAndDiagnoseResource) -> None:
        self._fix_parsing_and_diagnose = fix_parsing_and_diagnose

        self.detect_issues = to_raw_response_wrapper(
            fix_parsing_and_diagnose.detect_issues,
        )


class AsyncFixParsingAndDiagnoseResourceWithRawResponse:
    def __init__(self, fix_parsing_and_diagnose: AsyncFixParsingAndDiagnoseResource) -> None:
        self._fix_parsing_and_diagnose = fix_parsing_and_diagnose

        self.detect_issues = async_to_raw_response_wrapper(
            fix_parsing_and_diagnose.detect_issues,
        )


class FixParsingAndDiagnoseResourceWithStreamingResponse:
    def __init__(self, fix_parsing_and_diagnose: FixParsingAndDiagnoseResource) -> None:
        self._fix_parsing_and_diagnose = fix_parsing_and_diagnose

        self.detect_issues = to_streamed_response_wrapper(
            fix_parsing_and_diagnose.detect_issues,
        )


class AsyncFixParsingAndDiagnoseResourceWithStreamingResponse:
    def __init__(self, fix_parsing_and_diagnose: AsyncFixParsingAndDiagnoseResource) -> None:
        self._fix_parsing_and_diagnose = fix_parsing_and_diagnose

        self.detect_issues = async_to_streamed_response_wrapper(
            fix_parsing_and_diagnose.detect_issues,
        )
