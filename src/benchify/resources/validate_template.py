# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import validate_template_validate_params
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
from ..types.validate_template_validate_response import ValidateTemplateValidateResponse

__all__ = ["ValidateTemplateResource", "AsyncValidateTemplateResource"]


class ValidateTemplateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ValidateTemplateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Benchify/benchify-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ValidateTemplateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ValidateTemplateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Benchify/benchify-sdk-python#with_streaming_response
        """
        return ValidateTemplateResourceWithStreamingResponse(self)

    def validate(
        self,
        *,
        meta: Optional[validate_template_validate_params.Meta] | Omit = omit,
        response_format: Optional[Literal["DIFF", "CHANGED_FILES", "ALL_FILES"]] | Omit = omit,
        body_template_id_1: Optional[str] | Omit = omit,
        template_path: Optional[str] | Omit = omit,
        body_template_id_2: str | Omit = omit,
        template_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ValidateTemplateValidateResponse:
        """
        Validate a template configuration

        Args:
          meta: Meta information for the request

          response_format: Format for the response

          body_template_id_1: ID of the template

          template_path: Full path to the template to use for validation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/validate-template",
            body=maybe_transform(
                {
                    "meta": meta,
                    "response_format": response_format,
                    "body_template_id_1": body_template_id_1,
                    "template_path": template_path,
                    "body_template_id_2": body_template_id_2,
                    "template_name": template_name,
                },
                validate_template_validate_params.ValidateTemplateValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ValidateTemplateValidateResponse,
        )


class AsyncValidateTemplateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncValidateTemplateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Benchify/benchify-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncValidateTemplateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncValidateTemplateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Benchify/benchify-sdk-python#with_streaming_response
        """
        return AsyncValidateTemplateResourceWithStreamingResponse(self)

    async def validate(
        self,
        *,
        meta: Optional[validate_template_validate_params.Meta] | Omit = omit,
        response_format: Optional[Literal["DIFF", "CHANGED_FILES", "ALL_FILES"]] | Omit = omit,
        body_template_id_1: Optional[str] | Omit = omit,
        template_path: Optional[str] | Omit = omit,
        body_template_id_2: str | Omit = omit,
        template_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ValidateTemplateValidateResponse:
        """
        Validate a template configuration

        Args:
          meta: Meta information for the request

          response_format: Format for the response

          body_template_id_1: ID of the template

          template_path: Full path to the template to use for validation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/validate-template",
            body=await async_maybe_transform(
                {
                    "meta": meta,
                    "response_format": response_format,
                    "body_template_id_1": body_template_id_1,
                    "template_path": template_path,
                    "body_template_id_2": body_template_id_2,
                    "template_name": template_name,
                },
                validate_template_validate_params.ValidateTemplateValidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ValidateTemplateValidateResponse,
        )


class ValidateTemplateResourceWithRawResponse:
    def __init__(self, validate_template: ValidateTemplateResource) -> None:
        self._validate_template = validate_template

        self.validate = to_raw_response_wrapper(
            validate_template.validate,
        )


class AsyncValidateTemplateResourceWithRawResponse:
    def __init__(self, validate_template: AsyncValidateTemplateResource) -> None:
        self._validate_template = validate_template

        self.validate = async_to_raw_response_wrapper(
            validate_template.validate,
        )


class ValidateTemplateResourceWithStreamingResponse:
    def __init__(self, validate_template: ValidateTemplateResource) -> None:
        self._validate_template = validate_template

        self.validate = to_streamed_response_wrapper(
            validate_template.validate,
        )


class AsyncValidateTemplateResourceWithStreamingResponse:
    def __init__(self, validate_template: AsyncValidateTemplateResource) -> None:
        self._validate_template = validate_template

        self.validate = async_to_streamed_response_wrapper(
            validate_template.validate,
        )
