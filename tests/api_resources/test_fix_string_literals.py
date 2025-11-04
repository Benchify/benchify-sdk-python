# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from benchify import Benchify, AsyncBenchify
from tests.utils import assert_matches_type
from benchify.types import FixStringLiteralCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFixStringLiterals:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Benchify) -> None:
        fix_string_literal = client.fix_string_literals.create(
            file={
                "contents": "contents",
                "path": "path",
            },
        )
        assert_matches_type(FixStringLiteralCreateResponse, fix_string_literal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Benchify) -> None:
        fix_string_literal = client.fix_string_literals.create(
            file={
                "contents": "contents",
                "path": "path",
            },
            event_id="event_id",
            meta={"external_id": "external_id"},
        )
        assert_matches_type(FixStringLiteralCreateResponse, fix_string_literal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Benchify) -> None:
        response = client.fix_string_literals.with_raw_response.create(
            file={
                "contents": "contents",
                "path": "path",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fix_string_literal = response.parse()
        assert_matches_type(FixStringLiteralCreateResponse, fix_string_literal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Benchify) -> None:
        with client.fix_string_literals.with_streaming_response.create(
            file={
                "contents": "contents",
                "path": "path",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fix_string_literal = response.parse()
            assert_matches_type(FixStringLiteralCreateResponse, fix_string_literal, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFixStringLiterals:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncBenchify) -> None:
        fix_string_literal = await async_client.fix_string_literals.create(
            file={
                "contents": "contents",
                "path": "path",
            },
        )
        assert_matches_type(FixStringLiteralCreateResponse, fix_string_literal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBenchify) -> None:
        fix_string_literal = await async_client.fix_string_literals.create(
            file={
                "contents": "contents",
                "path": "path",
            },
            event_id="event_id",
            meta={"external_id": "external_id"},
        )
        assert_matches_type(FixStringLiteralCreateResponse, fix_string_literal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBenchify) -> None:
        response = await async_client.fix_string_literals.with_raw_response.create(
            file={
                "contents": "contents",
                "path": "path",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fix_string_literal = await response.parse()
        assert_matches_type(FixStringLiteralCreateResponse, fix_string_literal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBenchify) -> None:
        async with async_client.fix_string_literals.with_streaming_response.create(
            file={
                "contents": "contents",
                "path": "path",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fix_string_literal = await response.parse()
            assert_matches_type(FixStringLiteralCreateResponse, fix_string_literal, path=["response"])

        assert cast(Any, response.is_closed) is True
