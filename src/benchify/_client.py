# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import fix, fixer, stacks, validate_template, fix_string_literals, fix_parsing_and_diagnose
    from .resources.fixer import FixerResource, AsyncFixerResource
    from .resources.fix.fix import FixResource, AsyncFixResource
    from .resources.stacks.stacks import StacksResource, AsyncStacksResource
    from .resources.validate_template import ValidateTemplateResource, AsyncValidateTemplateResource
    from .resources.fix_string_literals import FixStringLiteralsResource, AsyncFixStringLiteralsResource
    from .resources.fix_parsing_and_diagnose import FixParsingAndDiagnoseResource, AsyncFixParsingAndDiagnoseResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Benchify",
    "AsyncBenchify",
    "Client",
    "AsyncClient",
]


class Benchify(SyncAPIClient):
    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Benchify client instance.

        This automatically infers the `api_key` argument from the `BENCHIFY_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("BENCHIFY_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("BENCHIFY_BASE_URL")
        if base_url is None:
            base_url = f"https://api.benchify.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def fixer(self) -> FixerResource:
        from .resources.fixer import FixerResource

        return FixerResource(self)

    @cached_property
    def stacks(self) -> StacksResource:
        from .resources.stacks import StacksResource

        return StacksResource(self)

    @cached_property
    def fix_string_literals(self) -> FixStringLiteralsResource:
        from .resources.fix_string_literals import FixStringLiteralsResource

        return FixStringLiteralsResource(self)

    @cached_property
    def validate_template(self) -> ValidateTemplateResource:
        from .resources.validate_template import ValidateTemplateResource

        return ValidateTemplateResource(self)

    @cached_property
    def fix_parsing_and_diagnose(self) -> FixParsingAndDiagnoseResource:
        from .resources.fix_parsing_and_diagnose import FixParsingAndDiagnoseResource

        return FixParsingAndDiagnoseResource(self)

    @cached_property
    def fix(self) -> FixResource:
        from .resources.fix import FixResource

        return FixResource(self)

    @cached_property
    def with_raw_response(self) -> BenchifyWithRawResponse:
        return BenchifyWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BenchifyWithStreamedResponse:
        return BenchifyWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.api_key and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncBenchify(AsyncAPIClient):
    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncBenchify client instance.

        This automatically infers the `api_key` argument from the `BENCHIFY_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("BENCHIFY_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("BENCHIFY_BASE_URL")
        if base_url is None:
            base_url = f"https://api.benchify.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def fixer(self) -> AsyncFixerResource:
        from .resources.fixer import AsyncFixerResource

        return AsyncFixerResource(self)

    @cached_property
    def stacks(self) -> AsyncStacksResource:
        from .resources.stacks import AsyncStacksResource

        return AsyncStacksResource(self)

    @cached_property
    def fix_string_literals(self) -> AsyncFixStringLiteralsResource:
        from .resources.fix_string_literals import AsyncFixStringLiteralsResource

        return AsyncFixStringLiteralsResource(self)

    @cached_property
    def validate_template(self) -> AsyncValidateTemplateResource:
        from .resources.validate_template import AsyncValidateTemplateResource

        return AsyncValidateTemplateResource(self)

    @cached_property
    def fix_parsing_and_diagnose(self) -> AsyncFixParsingAndDiagnoseResource:
        from .resources.fix_parsing_and_diagnose import AsyncFixParsingAndDiagnoseResource

        return AsyncFixParsingAndDiagnoseResource(self)

    @cached_property
    def fix(self) -> AsyncFixResource:
        from .resources.fix import AsyncFixResource

        return AsyncFixResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncBenchifyWithRawResponse:
        return AsyncBenchifyWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBenchifyWithStreamedResponse:
        return AsyncBenchifyWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.api_key and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class BenchifyWithRawResponse:
    _client: Benchify

    def __init__(self, client: Benchify) -> None:
        self._client = client

    @cached_property
    def fixer(self) -> fixer.FixerResourceWithRawResponse:
        from .resources.fixer import FixerResourceWithRawResponse

        return FixerResourceWithRawResponse(self._client.fixer)

    @cached_property
    def stacks(self) -> stacks.StacksResourceWithRawResponse:
        from .resources.stacks import StacksResourceWithRawResponse

        return StacksResourceWithRawResponse(self._client.stacks)

    @cached_property
    def fix_string_literals(self) -> fix_string_literals.FixStringLiteralsResourceWithRawResponse:
        from .resources.fix_string_literals import FixStringLiteralsResourceWithRawResponse

        return FixStringLiteralsResourceWithRawResponse(self._client.fix_string_literals)

    @cached_property
    def validate_template(self) -> validate_template.ValidateTemplateResourceWithRawResponse:
        from .resources.validate_template import ValidateTemplateResourceWithRawResponse

        return ValidateTemplateResourceWithRawResponse(self._client.validate_template)

    @cached_property
    def fix_parsing_and_diagnose(self) -> fix_parsing_and_diagnose.FixParsingAndDiagnoseResourceWithRawResponse:
        from .resources.fix_parsing_and_diagnose import FixParsingAndDiagnoseResourceWithRawResponse

        return FixParsingAndDiagnoseResourceWithRawResponse(self._client.fix_parsing_and_diagnose)

    @cached_property
    def fix(self) -> fix.FixResourceWithRawResponse:
        from .resources.fix import FixResourceWithRawResponse

        return FixResourceWithRawResponse(self._client.fix)


class AsyncBenchifyWithRawResponse:
    _client: AsyncBenchify

    def __init__(self, client: AsyncBenchify) -> None:
        self._client = client

    @cached_property
    def fixer(self) -> fixer.AsyncFixerResourceWithRawResponse:
        from .resources.fixer import AsyncFixerResourceWithRawResponse

        return AsyncFixerResourceWithRawResponse(self._client.fixer)

    @cached_property
    def stacks(self) -> stacks.AsyncStacksResourceWithRawResponse:
        from .resources.stacks import AsyncStacksResourceWithRawResponse

        return AsyncStacksResourceWithRawResponse(self._client.stacks)

    @cached_property
    def fix_string_literals(self) -> fix_string_literals.AsyncFixStringLiteralsResourceWithRawResponse:
        from .resources.fix_string_literals import AsyncFixStringLiteralsResourceWithRawResponse

        return AsyncFixStringLiteralsResourceWithRawResponse(self._client.fix_string_literals)

    @cached_property
    def validate_template(self) -> validate_template.AsyncValidateTemplateResourceWithRawResponse:
        from .resources.validate_template import AsyncValidateTemplateResourceWithRawResponse

        return AsyncValidateTemplateResourceWithRawResponse(self._client.validate_template)

    @cached_property
    def fix_parsing_and_diagnose(self) -> fix_parsing_and_diagnose.AsyncFixParsingAndDiagnoseResourceWithRawResponse:
        from .resources.fix_parsing_and_diagnose import AsyncFixParsingAndDiagnoseResourceWithRawResponse

        return AsyncFixParsingAndDiagnoseResourceWithRawResponse(self._client.fix_parsing_and_diagnose)

    @cached_property
    def fix(self) -> fix.AsyncFixResourceWithRawResponse:
        from .resources.fix import AsyncFixResourceWithRawResponse

        return AsyncFixResourceWithRawResponse(self._client.fix)


class BenchifyWithStreamedResponse:
    _client: Benchify

    def __init__(self, client: Benchify) -> None:
        self._client = client

    @cached_property
    def fixer(self) -> fixer.FixerResourceWithStreamingResponse:
        from .resources.fixer import FixerResourceWithStreamingResponse

        return FixerResourceWithStreamingResponse(self._client.fixer)

    @cached_property
    def stacks(self) -> stacks.StacksResourceWithStreamingResponse:
        from .resources.stacks import StacksResourceWithStreamingResponse

        return StacksResourceWithStreamingResponse(self._client.stacks)

    @cached_property
    def fix_string_literals(self) -> fix_string_literals.FixStringLiteralsResourceWithStreamingResponse:
        from .resources.fix_string_literals import FixStringLiteralsResourceWithStreamingResponse

        return FixStringLiteralsResourceWithStreamingResponse(self._client.fix_string_literals)

    @cached_property
    def validate_template(self) -> validate_template.ValidateTemplateResourceWithStreamingResponse:
        from .resources.validate_template import ValidateTemplateResourceWithStreamingResponse

        return ValidateTemplateResourceWithStreamingResponse(self._client.validate_template)

    @cached_property
    def fix_parsing_and_diagnose(self) -> fix_parsing_and_diagnose.FixParsingAndDiagnoseResourceWithStreamingResponse:
        from .resources.fix_parsing_and_diagnose import FixParsingAndDiagnoseResourceWithStreamingResponse

        return FixParsingAndDiagnoseResourceWithStreamingResponse(self._client.fix_parsing_and_diagnose)

    @cached_property
    def fix(self) -> fix.FixResourceWithStreamingResponse:
        from .resources.fix import FixResourceWithStreamingResponse

        return FixResourceWithStreamingResponse(self._client.fix)


class AsyncBenchifyWithStreamedResponse:
    _client: AsyncBenchify

    def __init__(self, client: AsyncBenchify) -> None:
        self._client = client

    @cached_property
    def fixer(self) -> fixer.AsyncFixerResourceWithStreamingResponse:
        from .resources.fixer import AsyncFixerResourceWithStreamingResponse

        return AsyncFixerResourceWithStreamingResponse(self._client.fixer)

    @cached_property
    def stacks(self) -> stacks.AsyncStacksResourceWithStreamingResponse:
        from .resources.stacks import AsyncStacksResourceWithStreamingResponse

        return AsyncStacksResourceWithStreamingResponse(self._client.stacks)

    @cached_property
    def fix_string_literals(self) -> fix_string_literals.AsyncFixStringLiteralsResourceWithStreamingResponse:
        from .resources.fix_string_literals import AsyncFixStringLiteralsResourceWithStreamingResponse

        return AsyncFixStringLiteralsResourceWithStreamingResponse(self._client.fix_string_literals)

    @cached_property
    def validate_template(self) -> validate_template.AsyncValidateTemplateResourceWithStreamingResponse:
        from .resources.validate_template import AsyncValidateTemplateResourceWithStreamingResponse

        return AsyncValidateTemplateResourceWithStreamingResponse(self._client.validate_template)

    @cached_property
    def fix_parsing_and_diagnose(
        self,
    ) -> fix_parsing_and_diagnose.AsyncFixParsingAndDiagnoseResourceWithStreamingResponse:
        from .resources.fix_parsing_and_diagnose import AsyncFixParsingAndDiagnoseResourceWithStreamingResponse

        return AsyncFixParsingAndDiagnoseResourceWithStreamingResponse(self._client.fix_parsing_and_diagnose)

    @cached_property
    def fix(self) -> fix.AsyncFixResourceWithStreamingResponse:
        from .resources.fix import AsyncFixResourceWithStreamingResponse

        return AsyncFixResourceWithStreamingResponse(self._client.fix)


Client = Benchify

AsyncClient = AsyncBenchify
