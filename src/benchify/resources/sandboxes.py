# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ..types import sandbox_create_params, sandbox_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, FileTypes, omit, not_given
from .._utils import extract_files, maybe_transform, strip_not_given, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.sandbox_create_response import SandboxCreateResponse
from ..types.sandbox_update_response import SandboxUpdateResponse
from ..types.sandbox_retrieve_response import SandboxRetrieveResponse

__all__ = ["SandboxesResource", "AsyncSandboxesResource"]


class SandboxesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SandboxesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Benchify/benchify-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SandboxesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SandboxesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Benchify/benchify-sdk-python#with_streaming_response
        """
        return SandboxesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        packed: FileTypes,
        content_hash: str,
        idempotency_key: str,
        manifest: str | Omit = omit,
        options: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxCreateResponse:
        """Upload a binary tar.gz file to create a new stack environment.

        For multi-service
        stacks, automatically detects and orchestrates multiple services.

        Args:
          packed: Binary gzipped tar archive containing project files

          manifest: Optional JSON metadata as string

          options: Optional JSON configuration as string

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Content-Hash": content_hash, "Idempotency-Key": idempotency_key, **(extra_headers or {})}
        body = deepcopy_minimal(
            {
                "packed": packed,
                "manifest": manifest,
                "options": options,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["packed"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers["Content-Type"] = "multipart/form-data"
        return self._post(
            "/sandboxes",
            body=maybe_transform(body, sandbox_create_params.SandboxCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxRetrieveResponse:
        """
        Retrieve current status and information about a stack and its services

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/sandboxes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        idempotency_key: str,
        manifest: str | Omit = omit,
        ops: str | Omit = omit,
        packed: FileTypes | Omit = omit,
        base_commit: str | Omit = omit,
        base_etag: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxUpdateResponse:
        """Update stack files using tar.gz blobs and/or individual operations.

        For
        multi-service stacks, changes are routed to appropriate services.

        Args:
          manifest: JSON string containing patch metadata: { base, proposed, files: {...changed
              hashes...} }. Required when packed is present.

          ops: Optional JSON string containing array of patch operations

          packed: Optional gzipped tar archive containing changed/added files

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "Idempotency-Key": idempotency_key,
                    "Base-Commit": base_commit,
                    "Base-Etag": base_etag,
                }
            ),
            **(extra_headers or {}),
        }
        body = deepcopy_minimal(
            {
                "manifest": manifest,
                "ops": ops,
                "packed": packed,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["packed"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            f"/sandboxes/{id}:patch",
            body=maybe_transform(body, sandbox_update_params.SandboxUpdateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxUpdateResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Permanently destroy a stack and all its services, cleaning up resources

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/sandboxes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSandboxesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSandboxesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Benchify/benchify-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSandboxesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSandboxesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Benchify/benchify-sdk-python#with_streaming_response
        """
        return AsyncSandboxesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        packed: FileTypes,
        content_hash: str,
        idempotency_key: str,
        manifest: str | Omit = omit,
        options: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxCreateResponse:
        """Upload a binary tar.gz file to create a new stack environment.

        For multi-service
        stacks, automatically detects and orchestrates multiple services.

        Args:
          packed: Binary gzipped tar archive containing project files

          manifest: Optional JSON metadata as string

          options: Optional JSON configuration as string

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Content-Hash": content_hash, "Idempotency-Key": idempotency_key, **(extra_headers or {})}
        body = deepcopy_minimal(
            {
                "packed": packed,
                "manifest": manifest,
                "options": options,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["packed"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers["Content-Type"] = "multipart/form-data"
        return await self._post(
            "/sandboxes",
            body=await async_maybe_transform(body, sandbox_create_params.SandboxCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxRetrieveResponse:
        """
        Retrieve current status and information about a stack and its services

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/sandboxes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        idempotency_key: str,
        manifest: str | Omit = omit,
        ops: str | Omit = omit,
        packed: FileTypes | Omit = omit,
        base_commit: str | Omit = omit,
        base_etag: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxUpdateResponse:
        """Update stack files using tar.gz blobs and/or individual operations.

        For
        multi-service stacks, changes are routed to appropriate services.

        Args:
          manifest: JSON string containing patch metadata: { base, proposed, files: {...changed
              hashes...} }. Required when packed is present.

          ops: Optional JSON string containing array of patch operations

          packed: Optional gzipped tar archive containing changed/added files

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "Idempotency-Key": idempotency_key,
                    "Base-Commit": base_commit,
                    "Base-Etag": base_etag,
                }
            ),
            **(extra_headers or {}),
        }
        body = deepcopy_minimal(
            {
                "manifest": manifest,
                "ops": ops,
                "packed": packed,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["packed"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            f"/sandboxes/{id}:patch",
            body=await async_maybe_transform(body, sandbox_update_params.SandboxUpdateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxUpdateResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Permanently destroy a stack and all its services, cleaning up resources

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/sandboxes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SandboxesResourceWithRawResponse:
    def __init__(self, sandboxes: SandboxesResource) -> None:
        self._sandboxes = sandboxes

        self.create = to_raw_response_wrapper(
            sandboxes.create,
        )
        self.retrieve = to_raw_response_wrapper(
            sandboxes.retrieve,
        )
        self.update = to_raw_response_wrapper(
            sandboxes.update,
        )
        self.delete = to_raw_response_wrapper(
            sandboxes.delete,
        )


class AsyncSandboxesResourceWithRawResponse:
    def __init__(self, sandboxes: AsyncSandboxesResource) -> None:
        self._sandboxes = sandboxes

        self.create = async_to_raw_response_wrapper(
            sandboxes.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            sandboxes.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            sandboxes.update,
        )
        self.delete = async_to_raw_response_wrapper(
            sandboxes.delete,
        )


class SandboxesResourceWithStreamingResponse:
    def __init__(self, sandboxes: SandboxesResource) -> None:
        self._sandboxes = sandboxes

        self.create = to_streamed_response_wrapper(
            sandboxes.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            sandboxes.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            sandboxes.update,
        )
        self.delete = to_streamed_response_wrapper(
            sandboxes.delete,
        )


class AsyncSandboxesResourceWithStreamingResponse:
    def __init__(self, sandboxes: AsyncSandboxesResource) -> None:
        self._sandboxes = sandboxes

        self.create = async_to_streamed_response_wrapper(
            sandboxes.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            sandboxes.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            sandboxes.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            sandboxes.delete,
        )
