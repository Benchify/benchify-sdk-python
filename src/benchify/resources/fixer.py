# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import fixer_run_params
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
        bundle: bool | Omit = omit,
        event_id: str | Omit = omit,
        files: Optional[Iterable[fixer_run_params.File]] | Omit = omit,
        files_data: Optional[str] | Omit = omit,
        files_manifest: Optional[Iterable[fixer_run_params.FilesManifest]] | Omit = omit,
        fixes: List[Literal["dependency", "parsing", "css", "ai_fallback", "types", "ui", "sql"]] | Omit = omit,
        meta: Optional[fixer_run_params.Meta] | Omit = omit,
        mode: Literal["project", "files"] | Omit = omit,
        response_encoding: Literal["json", "blob"] | Omit = omit,
        response_format: Literal["DIFF", "CHANGED_FILES", "ALL_FILES"] | Omit = omit,
        template_id: Optional[str] | Omit = omit,
        template_path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FixerRunResponse:
        """
        Handle fixer requests - supports both legacy (embedded files) and new
        (manifest+blobs) formats.

        Args:
          bundle: Whether to bundle the project (experimental)

          event_id: Unique identifier for the event

          files: List of files to process (legacy format)

          files_data: Base64-encoded compressed file contents (packed format)

          files_manifest: File manifest for packed format: [{"path": "app.tsx", "size": 1024}, ...]

          fixes: Configuration for which fix types to apply

          meta: Meta information for the request

          mode: Fixer operating mode

          response_encoding: Response encoding format

          response_format: Format for the response (diff, changed_files, or all_files)

          template_id: ID of the template to use

          template_path: Full path to the template

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/fixer",
            body=maybe_transform(
                {
                    "bundle": bundle,
                    "event_id": event_id,
                    "files": files,
                    "files_data": files_data,
                    "files_manifest": files_manifest,
                    "fixes": fixes,
                    "meta": meta,
                    "mode": mode,
                    "response_encoding": response_encoding,
                    "response_format": response_format,
                    "template_id": template_id,
                    "template_path": template_path,
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
        bundle: bool | Omit = omit,
        event_id: str | Omit = omit,
        files: Optional[Iterable[fixer_run_params.File]] | Omit = omit,
        files_data: Optional[str] | Omit = omit,
        files_manifest: Optional[Iterable[fixer_run_params.FilesManifest]] | Omit = omit,
        fixes: List[Literal["dependency", "parsing", "css", "ai_fallback", "types", "ui", "sql"]] | Omit = omit,
        meta: Optional[fixer_run_params.Meta] | Omit = omit,
        mode: Literal["project", "files"] | Omit = omit,
        response_encoding: Literal["json", "blob"] | Omit = omit,
        response_format: Literal["DIFF", "CHANGED_FILES", "ALL_FILES"] | Omit = omit,
        template_id: Optional[str] | Omit = omit,
        template_path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FixerRunResponse:
        """
        Handle fixer requests - supports both legacy (embedded files) and new
        (manifest+blobs) formats.

        Args:
          bundle: Whether to bundle the project (experimental)

          event_id: Unique identifier for the event

          files: List of files to process (legacy format)

          files_data: Base64-encoded compressed file contents (packed format)

          files_manifest: File manifest for packed format: [{"path": "app.tsx", "size": 1024}, ...]

          fixes: Configuration for which fix types to apply

          meta: Meta information for the request

          mode: Fixer operating mode

          response_encoding: Response encoding format

          response_format: Format for the response (diff, changed_files, or all_files)

          template_id: ID of the template to use

          template_path: Full path to the template

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/fixer",
            body=await async_maybe_transform(
                {
                    "bundle": bundle,
                    "event_id": event_id,
                    "files": files,
                    "files_data": files_data,
                    "files_manifest": files_manifest,
                    "fixes": fixes,
                    "meta": meta,
                    "mode": mode,
                    "response_encoding": response_encoding,
                    "response_format": response_format,
                    "template_id": template_id,
                    "template_path": template_path,
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
