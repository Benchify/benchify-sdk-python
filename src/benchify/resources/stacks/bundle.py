# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

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
from ..._base_client import make_request_options
from ...types.stacks import bundle_create_files_params
from ...types.stacks.bundle_create_files_response import BundleCreateFilesResponse

__all__ = ["BundleResource", "AsyncBundleResource"]


class BundleResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BundleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Benchify/benchify-sdk-python#accessing-raw-response-data-eg-headers
        """
        return BundleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BundleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Benchify/benchify-sdk-python#with_streaming_response
        """
        return BundleResourceWithStreamingResponse(self)

    def create_files(
        self,
        *,
        entrypoint: str,
        files: Iterable[bundle_create_files_params.File],
        tarball_filename: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BundleCreateFilesResponse:
        """
        Accepts a JSON array of {path, content}, packs into a tar.zst, and forwards to
        the Sandbox Manager /sandbox/bundle endpoint.

        Args:
          files: Files to bundle

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/stacks/bundle/files",
            body=maybe_transform(
                {
                    "entrypoint": entrypoint,
                    "files": files,
                    "tarball_filename": tarball_filename,
                },
                bundle_create_files_params.BundleCreateFilesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BundleCreateFilesResponse,
        )


class AsyncBundleResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBundleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Benchify/benchify-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBundleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBundleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Benchify/benchify-sdk-python#with_streaming_response
        """
        return AsyncBundleResourceWithStreamingResponse(self)

    async def create_files(
        self,
        *,
        entrypoint: str,
        files: Iterable[bundle_create_files_params.File],
        tarball_filename: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BundleCreateFilesResponse:
        """
        Accepts a JSON array of {path, content}, packs into a tar.zst, and forwards to
        the Sandbox Manager /sandbox/bundle endpoint.

        Args:
          files: Files to bundle

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/stacks/bundle/files",
            body=await async_maybe_transform(
                {
                    "entrypoint": entrypoint,
                    "files": files,
                    "tarball_filename": tarball_filename,
                },
                bundle_create_files_params.BundleCreateFilesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BundleCreateFilesResponse,
        )


class BundleResourceWithRawResponse:
    def __init__(self, bundle: BundleResource) -> None:
        self._bundle = bundle

        self.create_files = to_raw_response_wrapper(
            bundle.create_files,
        )


class AsyncBundleResourceWithRawResponse:
    def __init__(self, bundle: AsyncBundleResource) -> None:
        self._bundle = bundle

        self.create_files = async_to_raw_response_wrapper(
            bundle.create_files,
        )


class BundleResourceWithStreamingResponse:
    def __init__(self, bundle: BundleResource) -> None:
        self._bundle = bundle

        self.create_files = to_streamed_response_wrapper(
            bundle.create_files,
        )


class AsyncBundleResourceWithStreamingResponse:
    def __init__(self, bundle: AsyncBundleResource) -> None:
        self._bundle = bundle

        self.create_files = async_to_streamed_response_wrapper(
            bundle.create_files,
        )
