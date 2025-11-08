# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from benchify import Benchify, AsyncBenchify
from tests.utils import assert_matches_type
from benchify.types import FixCreateAIFallbackResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFix:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_ai_fallback(self, client: Benchify) -> None:
        fix = client.fix.create_ai_fallback(
            files=[
                {
                    "contents": "export function complexFunction() { /* complex logic */ }",
                    "path": "src/complex.ts",
                }
            ],
            remaining_diagnostics={},
            template_path="benchify/default-template",
        )
        assert_matches_type(FixCreateAIFallbackResponse, fix, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_ai_fallback_with_all_params(self, client: Benchify) -> None:
        fix = client.fix.create_ai_fallback(
            files=[
                {
                    "contents": "export function complexFunction() { /* complex logic */ }",
                    "path": "src/complex.ts",
                }
            ],
            remaining_diagnostics={
                "file_to_diagnostics": {
                    "src/complex.ts": [
                        {
                            "file_path": "src/complex.ts",
                            "location": {
                                "column": 1,
                                "line": 1,
                                "span": 10,
                                "starting_character_position": 0,
                            },
                            "message": "Complex type inference issue",
                            "type": "types",
                            "code": 2000,
                            "context": "context",
                        }
                    ]
                }
            },
            template_path="benchify/default-template",
            event_id="",
            include_context=True,
            max_attempts=3,
            meta={"external_id": "external_id"},
        )
        assert_matches_type(FixCreateAIFallbackResponse, fix, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_ai_fallback(self, client: Benchify) -> None:
        response = client.fix.with_raw_response.create_ai_fallback(
            files=[
                {
                    "contents": "export function complexFunction() { /* complex logic */ }",
                    "path": "src/complex.ts",
                }
            ],
            remaining_diagnostics={},
            template_path="benchify/default-template",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fix = response.parse()
        assert_matches_type(FixCreateAIFallbackResponse, fix, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_ai_fallback(self, client: Benchify) -> None:
        with client.fix.with_streaming_response.create_ai_fallback(
            files=[
                {
                    "contents": "export function complexFunction() { /* complex logic */ }",
                    "path": "src/complex.ts",
                }
            ],
            remaining_diagnostics={},
            template_path="benchify/default-template",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fix = response.parse()
            assert_matches_type(FixCreateAIFallbackResponse, fix, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFix:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_ai_fallback(self, async_client: AsyncBenchify) -> None:
        fix = await async_client.fix.create_ai_fallback(
            files=[
                {
                    "contents": "export function complexFunction() { /* complex logic */ }",
                    "path": "src/complex.ts",
                }
            ],
            remaining_diagnostics={},
            template_path="benchify/default-template",
        )
        assert_matches_type(FixCreateAIFallbackResponse, fix, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_ai_fallback_with_all_params(self, async_client: AsyncBenchify) -> None:
        fix = await async_client.fix.create_ai_fallback(
            files=[
                {
                    "contents": "export function complexFunction() { /* complex logic */ }",
                    "path": "src/complex.ts",
                }
            ],
            remaining_diagnostics={
                "file_to_diagnostics": {
                    "src/complex.ts": [
                        {
                            "file_path": "src/complex.ts",
                            "location": {
                                "column": 1,
                                "line": 1,
                                "span": 10,
                                "starting_character_position": 0,
                            },
                            "message": "Complex type inference issue",
                            "type": "types",
                            "code": 2000,
                            "context": "context",
                        }
                    ]
                }
            },
            template_path="benchify/default-template",
            event_id="",
            include_context=True,
            max_attempts=3,
            meta={"external_id": "external_id"},
        )
        assert_matches_type(FixCreateAIFallbackResponse, fix, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_ai_fallback(self, async_client: AsyncBenchify) -> None:
        response = await async_client.fix.with_raw_response.create_ai_fallback(
            files=[
                {
                    "contents": "export function complexFunction() { /* complex logic */ }",
                    "path": "src/complex.ts",
                }
            ],
            remaining_diagnostics={},
            template_path="benchify/default-template",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fix = await response.parse()
        assert_matches_type(FixCreateAIFallbackResponse, fix, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_ai_fallback(self, async_client: AsyncBenchify) -> None:
        async with async_client.fix.with_streaming_response.create_ai_fallback(
            files=[
                {
                    "contents": "export function complexFunction() { /* complex logic */ }",
                    "path": "src/complex.ts",
                }
            ],
            remaining_diagnostics={},
            template_path="benchify/default-template",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fix = await response.parse()
            assert_matches_type(FixCreateAIFallbackResponse, fix, path=["response"])

        assert cast(Any, response.is_closed) is True
