# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ..types import (
    stack_create_params,
    stack_update_params,
    stack_get_logs_params,
    stack_create_and_run_params,
    stack_execute_command_params,
    stack_wait_for_dev_server_url_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, FileTypes, SequenceNotStr, omit, not_given
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
from ..types.stack_create_response import StackCreateResponse
from ..types.stack_update_response import StackUpdateResponse
from ..types.stack_get_logs_response import StackGetLogsResponse
from ..types.stack_retrieve_response import StackRetrieveResponse
from ..types.stack_create_and_run_response import StackCreateAndRunResponse
from ..types.stack_execute_command_response import StackExecuteCommandResponse
from ..types.stack_get_network_info_response import StackGetNetworkInfoResponse
from ..types.stack_wait_for_dev_server_url_response import StackWaitForDevServerURLResponse

__all__ = ["StacksResource", "AsyncStacksResource"]


class StacksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StacksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Benchify/benchify-sdk-python#accessing-raw-response-data-eg-headers
        """
        return StacksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StacksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Benchify/benchify-sdk-python#with_streaming_response
        """
        return StacksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        bundle: FileTypes,
        manifest: FileTypes,
        idempotency_key: str,
        options: str | Omit = omit,
        content_hash: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StackCreateResponse:
        """Create a new stack environment using manifest + bundle format.

        Upload a JSON
        manifest with file metadata and a tar.zst bundle containing your project files.
        For multi-service stacks, automatically detects and orchestrates multiple
        services.

        Args:
          bundle: Tar.zst bundle containing project files

          manifest: JSON manifest file containing file metadata and tree hashes

          idempotency_key: Unique key for idempotent requests

          options: Optional JSON configuration string

          content_hash: SHA-256 hash of the bundle for deduplication

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "idempotency-key": idempotency_key,
                    "content-hash": content_hash,
                }
            ),
            **(extra_headers or {}),
        }
        body = deepcopy_minimal(
            {
                "bundle": bundle,
                "manifest": manifest,
                "options": options,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["manifest"], ["bundle"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/v1/stacks",
            body=maybe_transform(body, stack_create_params.StackCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StackCreateResponse,
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
    ) -> StackRetrieveResponse:
        """
        Retrieve current status and information about a stack and its services

        Args:
          id: Stack identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/stacks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StackRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        idempotency_key: str,
        bundle: FileTypes | Omit = omit,
        manifest: FileTypes | Omit = omit,
        ops: str | Omit = omit,
        base_etag: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StackUpdateResponse:
        """
        Update stack files using manifest + bundle format and/or individual operations.
        For multi-service stacks, changes are routed to appropriate services.

        Args:
          id: Stack identifier

          idempotency_key: Unique key for idempotent requests

          bundle: Optional tar.zst bundle containing changed/added files

          manifest: Optional JSON manifest file with file metadata

          ops: Optional JSON string containing array of patch operations

          base_etag: Current stack etag for conflict detection

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
                    "idempotency-key": idempotency_key,
                    "base-etag": base_etag,
                }
            ),
            **(extra_headers or {}),
        }
        body = deepcopy_minimal(
            {
                "bundle": bundle,
                "manifest": manifest,
                "ops": ops,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["manifest"], ["bundle"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            f"/v1/stacks/{id}/patch",
            body=maybe_transform(body, stack_update_params.StackUpdateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StackUpdateResponse,
        )

    def create_and_run(
        self,
        *,
        command: SequenceNotStr[str],
        image: str,
        ttl_seconds: float | Omit = omit,
        wait: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StackCreateAndRunResponse:
        """
        Create a simple container sandbox with a custom image and command

        Args:
          command: Command to run

          image: Docker image to use

          ttl_seconds: Time to live in seconds

          wait: Wait for container to be ready

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/stacks/create-and-run",
            body=maybe_transform(
                {
                    "command": command,
                    "image": image,
                    "ttl_seconds": ttl_seconds,
                    "wait": wait,
                },
                stack_create_and_run_params.StackCreateAndRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StackCreateAndRunResponse,
        )

    def destroy(
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
          id: Stack identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/stacks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def execute_command(
        self,
        id: str,
        *,
        command: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StackExecuteCommandResponse:
        """
        Run a command in the sandbox container and get the output

        Args:
          id: Stack identifier

          command: Command to execute as array

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/v1/stacks/{id}/exec",
            body=maybe_transform({"command": command}, stack_execute_command_params.StackExecuteCommandParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StackExecuteCommandResponse,
        )

    def get_logs(
        self,
        id: str,
        *,
        tail: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StackGetLogsResponse:
        """
        Retrieve logs from all services in the stack

        Args:
          id: Stack identifier

          tail: Number of log lines to return per service

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/stacks/{id}/logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"tail": tail}, stack_get_logs_params.StackGetLogsParams),
            ),
            cast_to=StackGetLogsResponse,
        )

    def get_network_info(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StackGetNetworkInfoResponse:
        """
        Retrieve network details for a stack including URLs and connection info

        Args:
          id: Stack identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/stacks/{id}/network-info",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StackGetNetworkInfoResponse,
        )

    def wait_for_dev_server_url(
        self,
        id: str,
        *,
        interval: str | Omit = omit,
        api_timeout: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StackWaitForDevServerURLResponse:
        """
        Poll stack logs until a dev server URL is detected or timeout

        Args:
          id: Stack identifier

          interval: Polling interval in ms

          api_timeout: Timeout in seconds

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/stacks/{id}/wait-url",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "interval": interval,
                        "api_timeout": api_timeout,
                    },
                    stack_wait_for_dev_server_url_params.StackWaitForDevServerURLParams,
                ),
            ),
            cast_to=StackWaitForDevServerURLResponse,
        )


class AsyncStacksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStacksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Benchify/benchify-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStacksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStacksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Benchify/benchify-sdk-python#with_streaming_response
        """
        return AsyncStacksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        bundle: FileTypes,
        manifest: FileTypes,
        idempotency_key: str,
        options: str | Omit = omit,
        content_hash: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StackCreateResponse:
        """Create a new stack environment using manifest + bundle format.

        Upload a JSON
        manifest with file metadata and a tar.zst bundle containing your project files.
        For multi-service stacks, automatically detects and orchestrates multiple
        services.

        Args:
          bundle: Tar.zst bundle containing project files

          manifest: JSON manifest file containing file metadata and tree hashes

          idempotency_key: Unique key for idempotent requests

          options: Optional JSON configuration string

          content_hash: SHA-256 hash of the bundle for deduplication

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "idempotency-key": idempotency_key,
                    "content-hash": content_hash,
                }
            ),
            **(extra_headers or {}),
        }
        body = deepcopy_minimal(
            {
                "bundle": bundle,
                "manifest": manifest,
                "options": options,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["manifest"], ["bundle"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v1/stacks",
            body=await async_maybe_transform(body, stack_create_params.StackCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StackCreateResponse,
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
    ) -> StackRetrieveResponse:
        """
        Retrieve current status and information about a stack and its services

        Args:
          id: Stack identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/stacks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StackRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        idempotency_key: str,
        bundle: FileTypes | Omit = omit,
        manifest: FileTypes | Omit = omit,
        ops: str | Omit = omit,
        base_etag: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StackUpdateResponse:
        """
        Update stack files using manifest + bundle format and/or individual operations.
        For multi-service stacks, changes are routed to appropriate services.

        Args:
          id: Stack identifier

          idempotency_key: Unique key for idempotent requests

          bundle: Optional tar.zst bundle containing changed/added files

          manifest: Optional JSON manifest file with file metadata

          ops: Optional JSON string containing array of patch operations

          base_etag: Current stack etag for conflict detection

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
                    "idempotency-key": idempotency_key,
                    "base-etag": base_etag,
                }
            ),
            **(extra_headers or {}),
        }
        body = deepcopy_minimal(
            {
                "bundle": bundle,
                "manifest": manifest,
                "ops": ops,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["manifest"], ["bundle"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            f"/v1/stacks/{id}/patch",
            body=await async_maybe_transform(body, stack_update_params.StackUpdateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StackUpdateResponse,
        )

    async def create_and_run(
        self,
        *,
        command: SequenceNotStr[str],
        image: str,
        ttl_seconds: float | Omit = omit,
        wait: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StackCreateAndRunResponse:
        """
        Create a simple container sandbox with a custom image and command

        Args:
          command: Command to run

          image: Docker image to use

          ttl_seconds: Time to live in seconds

          wait: Wait for container to be ready

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/stacks/create-and-run",
            body=await async_maybe_transform(
                {
                    "command": command,
                    "image": image,
                    "ttl_seconds": ttl_seconds,
                    "wait": wait,
                },
                stack_create_and_run_params.StackCreateAndRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StackCreateAndRunResponse,
        )

    async def destroy(
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
          id: Stack identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/stacks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def execute_command(
        self,
        id: str,
        *,
        command: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StackExecuteCommandResponse:
        """
        Run a command in the sandbox container and get the output

        Args:
          id: Stack identifier

          command: Command to execute as array

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/v1/stacks/{id}/exec",
            body=await async_maybe_transform(
                {"command": command}, stack_execute_command_params.StackExecuteCommandParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StackExecuteCommandResponse,
        )

    async def get_logs(
        self,
        id: str,
        *,
        tail: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StackGetLogsResponse:
        """
        Retrieve logs from all services in the stack

        Args:
          id: Stack identifier

          tail: Number of log lines to return per service

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/stacks/{id}/logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"tail": tail}, stack_get_logs_params.StackGetLogsParams),
            ),
            cast_to=StackGetLogsResponse,
        )

    async def get_network_info(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StackGetNetworkInfoResponse:
        """
        Retrieve network details for a stack including URLs and connection info

        Args:
          id: Stack identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/stacks/{id}/network-info",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StackGetNetworkInfoResponse,
        )

    async def wait_for_dev_server_url(
        self,
        id: str,
        *,
        interval: str | Omit = omit,
        api_timeout: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StackWaitForDevServerURLResponse:
        """
        Poll stack logs until a dev server URL is detected or timeout

        Args:
          id: Stack identifier

          interval: Polling interval in ms

          api_timeout: Timeout in seconds

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/stacks/{id}/wait-url",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "interval": interval,
                        "api_timeout": api_timeout,
                    },
                    stack_wait_for_dev_server_url_params.StackWaitForDevServerURLParams,
                ),
            ),
            cast_to=StackWaitForDevServerURLResponse,
        )


class StacksResourceWithRawResponse:
    def __init__(self, stacks: StacksResource) -> None:
        self._stacks = stacks

        self.create = to_raw_response_wrapper(
            stacks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            stacks.retrieve,
        )
        self.update = to_raw_response_wrapper(
            stacks.update,
        )
        self.create_and_run = to_raw_response_wrapper(
            stacks.create_and_run,
        )
        self.destroy = to_raw_response_wrapper(
            stacks.destroy,
        )
        self.execute_command = to_raw_response_wrapper(
            stacks.execute_command,
        )
        self.get_logs = to_raw_response_wrapper(
            stacks.get_logs,
        )
        self.get_network_info = to_raw_response_wrapper(
            stacks.get_network_info,
        )
        self.wait_for_dev_server_url = to_raw_response_wrapper(
            stacks.wait_for_dev_server_url,
        )


class AsyncStacksResourceWithRawResponse:
    def __init__(self, stacks: AsyncStacksResource) -> None:
        self._stacks = stacks

        self.create = async_to_raw_response_wrapper(
            stacks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            stacks.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            stacks.update,
        )
        self.create_and_run = async_to_raw_response_wrapper(
            stacks.create_and_run,
        )
        self.destroy = async_to_raw_response_wrapper(
            stacks.destroy,
        )
        self.execute_command = async_to_raw_response_wrapper(
            stacks.execute_command,
        )
        self.get_logs = async_to_raw_response_wrapper(
            stacks.get_logs,
        )
        self.get_network_info = async_to_raw_response_wrapper(
            stacks.get_network_info,
        )
        self.wait_for_dev_server_url = async_to_raw_response_wrapper(
            stacks.wait_for_dev_server_url,
        )


class StacksResourceWithStreamingResponse:
    def __init__(self, stacks: StacksResource) -> None:
        self._stacks = stacks

        self.create = to_streamed_response_wrapper(
            stacks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            stacks.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            stacks.update,
        )
        self.create_and_run = to_streamed_response_wrapper(
            stacks.create_and_run,
        )
        self.destroy = to_streamed_response_wrapper(
            stacks.destroy,
        )
        self.execute_command = to_streamed_response_wrapper(
            stacks.execute_command,
        )
        self.get_logs = to_streamed_response_wrapper(
            stacks.get_logs,
        )
        self.get_network_info = to_streamed_response_wrapper(
            stacks.get_network_info,
        )
        self.wait_for_dev_server_url = to_streamed_response_wrapper(
            stacks.wait_for_dev_server_url,
        )


class AsyncStacksResourceWithStreamingResponse:
    def __init__(self, stacks: AsyncStacksResource) -> None:
        self._stacks = stacks

        self.create = async_to_streamed_response_wrapper(
            stacks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            stacks.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            stacks.update,
        )
        self.create_and_run = async_to_streamed_response_wrapper(
            stacks.create_and_run,
        )
        self.destroy = async_to_streamed_response_wrapper(
            stacks.destroy,
        )
        self.execute_command = async_to_streamed_response_wrapper(
            stacks.execute_command,
        )
        self.get_logs = async_to_streamed_response_wrapper(
            stacks.get_logs,
        )
        self.get_network_info = async_to_streamed_response_wrapper(
            stacks.get_network_info,
        )
        self.wait_for_dev_server_url = async_to_streamed_response_wrapper(
            stacks.wait_for_dev_server_url,
        )
