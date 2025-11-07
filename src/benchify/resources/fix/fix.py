# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ...types import fix_create_ai_fallback_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from .standard import (
    StandardResource,
    AsyncStandardResource,
    StandardResourceWithRawResponse,
    AsyncStandardResourceWithRawResponse,
    StandardResourceWithStreamingResponse,
    AsyncStandardResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.fix_create_ai_fallback_response import FixCreateAIFallbackResponse

__all__ = ["FixResource", "AsyncFixResource"]


class FixResource(SyncAPIResource):
    @cached_property
    def standard(self) -> StandardResource:
        return StandardResource(self._client)

    @cached_property
    def with_raw_response(self) -> FixResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Benchify/benchify-sdk-python#accessing-raw-response-data-eg-headers
        """
        return FixResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FixResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Benchify/benchify-sdk-python#with_streaming_response
        """
        return FixResourceWithStreamingResponse(self)

    def create_ai_fallback(
        self,
        *,
        files: Iterable[fix_create_ai_fallback_params.File],
        remaining_diagnostics: fix_create_ai_fallback_params.RemainingDiagnostics,
        template_path: str,
        event_id: str | Omit = omit,
        include_context: bool | Omit = omit,
        max_attempts: float | Omit = omit,
        meta: Optional[fix_create_ai_fallback_params.Meta] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FixCreateAIFallbackResponse:
        """AI-powered fallback for complex issues.

        Phase 3 of the 3-phase architecture.
        Handles issues that standard fixers cannot resolve. Uses LLM to understand and
        fix complex problems. Provides confidence scores and alternative suggestions.

        Args:
          files: List of files (potentially already fixed by standard fixers)

          remaining_diagnostics: Diagnostics that remain after standard fixing

          template_path: Full path to the template

          event_id: Unique identifier for the event

          include_context: Whether to include context in AI prompts

          max_attempts: Maximum number of AI fix attempts

          meta: Meta information for the request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/fix/ai-fallback",
            body=maybe_transform(
                {
                    "files": files,
                    "remaining_diagnostics": remaining_diagnostics,
                    "template_path": template_path,
                    "event_id": event_id,
                    "include_context": include_context,
                    "max_attempts": max_attempts,
                    "meta": meta,
                },
                fix_create_ai_fallback_params.FixCreateAIFallbackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FixCreateAIFallbackResponse,
        )


class AsyncFixResource(AsyncAPIResource):
    @cached_property
    def standard(self) -> AsyncStandardResource:
        return AsyncStandardResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFixResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Benchify/benchify-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFixResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFixResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Benchify/benchify-sdk-python#with_streaming_response
        """
        return AsyncFixResourceWithStreamingResponse(self)

    async def create_ai_fallback(
        self,
        *,
        files: Iterable[fix_create_ai_fallback_params.File],
        remaining_diagnostics: fix_create_ai_fallback_params.RemainingDiagnostics,
        template_path: str,
        event_id: str | Omit = omit,
        include_context: bool | Omit = omit,
        max_attempts: float | Omit = omit,
        meta: Optional[fix_create_ai_fallback_params.Meta] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FixCreateAIFallbackResponse:
        """AI-powered fallback for complex issues.

        Phase 3 of the 3-phase architecture.
        Handles issues that standard fixers cannot resolve. Uses LLM to understand and
        fix complex problems. Provides confidence scores and alternative suggestions.

        Args:
          files: List of files (potentially already fixed by standard fixers)

          remaining_diagnostics: Diagnostics that remain after standard fixing

          template_path: Full path to the template

          event_id: Unique identifier for the event

          include_context: Whether to include context in AI prompts

          max_attempts: Maximum number of AI fix attempts

          meta: Meta information for the request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/fix/ai-fallback",
            body=await async_maybe_transform(
                {
                    "files": files,
                    "remaining_diagnostics": remaining_diagnostics,
                    "template_path": template_path,
                    "event_id": event_id,
                    "include_context": include_context,
                    "max_attempts": max_attempts,
                    "meta": meta,
                },
                fix_create_ai_fallback_params.FixCreateAIFallbackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FixCreateAIFallbackResponse,
        )


class FixResourceWithRawResponse:
    def __init__(self, fix: FixResource) -> None:
        self._fix = fix

        self.create_ai_fallback = to_raw_response_wrapper(
            fix.create_ai_fallback,
        )

    @cached_property
    def standard(self) -> StandardResourceWithRawResponse:
        return StandardResourceWithRawResponse(self._fix.standard)


class AsyncFixResourceWithRawResponse:
    def __init__(self, fix: AsyncFixResource) -> None:
        self._fix = fix

        self.create_ai_fallback = async_to_raw_response_wrapper(
            fix.create_ai_fallback,
        )

    @cached_property
    def standard(self) -> AsyncStandardResourceWithRawResponse:
        return AsyncStandardResourceWithRawResponse(self._fix.standard)


class FixResourceWithStreamingResponse:
    def __init__(self, fix: FixResource) -> None:
        self._fix = fix

        self.create_ai_fallback = to_streamed_response_wrapper(
            fix.create_ai_fallback,
        )

    @cached_property
    def standard(self) -> StandardResourceWithStreamingResponse:
        return StandardResourceWithStreamingResponse(self._fix.standard)


class AsyncFixResourceWithStreamingResponse:
    def __init__(self, fix: AsyncFixResource) -> None:
        self._fix = fix

        self.create_ai_fallback = async_to_streamed_response_wrapper(
            fix.create_ai_fallback,
        )

    @cached_property
    def standard(self) -> AsyncStandardResourceWithStreamingResponse:
        return AsyncStandardResourceWithStreamingResponse(self._fix.standard)
