# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from benchify import Benchify, AsyncBenchify
from tests.utils import assert_matches_type
from benchify.types.fix import StandardCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStandard:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Benchify) -> None:
        standard = client.fix.standard.create(
            files=[
                {
                    "contents": "export const hello = 'world';",
                    "path": "src/index.ts",
                },
                {
                    "contents": ".container { widht: 100%; }",
                    "path": "src/styles.css",
                },
            ],
            remaining_diagnostics={},
        )
        assert_matches_type(StandardCreateResponse, standard, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Benchify) -> None:
        standard = client.fix.standard.create(
            files=[
                {
                    "contents": "export const hello = 'world';",
                    "path": "src/index.ts",
                },
                {
                    "contents": ".container { widht: 100%; }",
                    "path": "src/styles.css",
                },
            ],
            remaining_diagnostics={
                "file_to_diagnostics": {
                    "src/styles.css": [
                        {
                            "file_path": "src/styles.css",
                            "location": {
                                "column": 14,
                                "line": 1,
                                "span": 5,
                                "starting_character_position": 13,
                            },
                            "message": "Unknown property widht",
                            "type": "css",
                            "code": 0,
                            "context": "context",
                        }
                    ]
                }
            },
            bundle=True,
            event_id="",
            fix_types=["css", "ui", "dependency", "types"],
            meta={"external_id": "external_id"},
            mode="project",
            template_path="benchify/default-template",
        )
        assert_matches_type(StandardCreateResponse, standard, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Benchify) -> None:
        response = client.fix.standard.with_raw_response.create(
            files=[
                {
                    "contents": "export const hello = 'world';",
                    "path": "src/index.ts",
                },
                {
                    "contents": ".container { widht: 100%; }",
                    "path": "src/styles.css",
                },
            ],
            remaining_diagnostics={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        standard = response.parse()
        assert_matches_type(StandardCreateResponse, standard, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Benchify) -> None:
        with client.fix.standard.with_streaming_response.create(
            files=[
                {
                    "contents": "export const hello = 'world';",
                    "path": "src/index.ts",
                },
                {
                    "contents": ".container { widht: 100%; }",
                    "path": "src/styles.css",
                },
            ],
            remaining_diagnostics={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            standard = response.parse()
            assert_matches_type(StandardCreateResponse, standard, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStandard:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncBenchify) -> None:
        standard = await async_client.fix.standard.create(
            files=[
                {
                    "contents": "export const hello = 'world';",
                    "path": "src/index.ts",
                },
                {
                    "contents": ".container { widht: 100%; }",
                    "path": "src/styles.css",
                },
            ],
            remaining_diagnostics={},
        )
        assert_matches_type(StandardCreateResponse, standard, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBenchify) -> None:
        standard = await async_client.fix.standard.create(
            files=[
                {
                    "contents": "export const hello = 'world';",
                    "path": "src/index.ts",
                },
                {
                    "contents": ".container { widht: 100%; }",
                    "path": "src/styles.css",
                },
            ],
            remaining_diagnostics={
                "file_to_diagnostics": {
                    "src/styles.css": [
                        {
                            "file_path": "src/styles.css",
                            "location": {
                                "column": 14,
                                "line": 1,
                                "span": 5,
                                "starting_character_position": 13,
                            },
                            "message": "Unknown property widht",
                            "type": "css",
                            "code": 0,
                            "context": "context",
                        }
                    ]
                }
            },
            bundle=True,
            event_id="",
            fix_types=["css", "ui", "dependency", "types"],
            meta={"external_id": "external_id"},
            mode="project",
            template_path="benchify/default-template",
        )
        assert_matches_type(StandardCreateResponse, standard, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBenchify) -> None:
        response = await async_client.fix.standard.with_raw_response.create(
            files=[
                {
                    "contents": "export const hello = 'world';",
                    "path": "src/index.ts",
                },
                {
                    "contents": ".container { widht: 100%; }",
                    "path": "src/styles.css",
                },
            ],
            remaining_diagnostics={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        standard = await response.parse()
        assert_matches_type(StandardCreateResponse, standard, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBenchify) -> None:
        async with async_client.fix.standard.with_streaming_response.create(
            files=[
                {
                    "contents": "export const hello = 'world';",
                    "path": "src/index.ts",
                },
                {
                    "contents": ".container { widht: 100%; }",
                    "path": "src/styles.css",
                },
            ],
            remaining_diagnostics={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            standard = await response.parse()
            assert_matches_type(StandardCreateResponse, standard, path=["response"])

        assert cast(Any, response.is_closed) is True
