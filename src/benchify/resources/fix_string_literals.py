# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import fix_string_literal_create_params
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
from ..types.fix_string_literal_create_response import FixStringLiteralCreateResponse

__all__ = ["FixStringLiteralsResource", "AsyncFixStringLiteralsResource"]


class FixStringLiteralsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FixStringLiteralsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Benchify/benchify-sdk-python#accessing-raw-response-data-eg-headers
        """
        return FixStringLiteralsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FixStringLiteralsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Benchify/benchify-sdk-python#with_streaming_response
        """
        return FixStringLiteralsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        file: fix_string_literal_create_params.File,
        event_id: Optional[str] | Omit = omit,
        meta: Optional[fix_string_literal_create_params.Meta] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FixStringLiteralCreateResponse:
        """
        Fix string literal issues in TypeScript files.

        Args:
          file: File to process

          event_id: Unique identifier for the event

          meta: Meta information for the request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/fix-string-literals",
            body=maybe_transform(
                {
                    "file": file,
                    "event_id": event_id,
                    "meta": meta,
                },
                fix_string_literal_create_params.FixStringLiteralCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FixStringLiteralCreateResponse,
        )


class AsyncFixStringLiteralsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFixStringLiteralsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Benchify/benchify-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFixStringLiteralsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFixStringLiteralsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Benchify/benchify-sdk-python#with_streaming_response
        """
        return AsyncFixStringLiteralsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        file: fix_string_literal_create_params.File,
        event_id: Optional[str] | Omit = omit,
        meta: Optional[fix_string_literal_create_params.Meta] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FixStringLiteralCreateResponse:
        """
        Fix string literal issues in TypeScript files.

        Args:
          file: File to process

          event_id: Unique identifier for the event

          meta: Meta information for the request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/fix-string-literals",
            body=await async_maybe_transform(
                {
                    "file": file,
                    "event_id": event_id,
                    "meta": meta,
                },
                fix_string_literal_create_params.FixStringLiteralCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FixStringLiteralCreateResponse,
        )


class FixStringLiteralsResourceWithRawResponse:
    def __init__(self, fix_string_literals: FixStringLiteralsResource) -> None:
        self._fix_string_literals = fix_string_literals

        self.create = to_raw_response_wrapper(
            fix_string_literals.create,
        )


class AsyncFixStringLiteralsResourceWithRawResponse:
    def __init__(self, fix_string_literals: AsyncFixStringLiteralsResource) -> None:
        self._fix_string_literals = fix_string_literals

        self.create = async_to_raw_response_wrapper(
            fix_string_literals.create,
        )


class FixStringLiteralsResourceWithStreamingResponse:
    def __init__(self, fix_string_literals: FixStringLiteralsResource) -> None:
        self._fix_string_literals = fix_string_literals

        self.create = to_streamed_response_wrapper(
            fix_string_literals.create,
        )


class AsyncFixStringLiteralsResourceWithStreamingResponse:
    def __init__(self, fix_string_literals: AsyncFixStringLiteralsResource) -> None:
        self._fix_string_literals = fix_string_literals

        self.create = async_to_streamed_response_wrapper(
            fix_string_literals.create,
        )
