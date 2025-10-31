# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from benchify import Benchify, AsyncBenchify
from tests.utils import assert_matches_type
from benchify.types import FixerRunResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFixer:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run(self, client: Benchify) -> None:
        fixer = client.fixer.run()
        assert_matches_type(FixerRunResponse, fixer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_with_all_params(self, client: Benchify) -> None:
        fixer = client.fixer.run(
            bundle=False,
            event_id="event_id",
            files=[
                {
                    "contents": "export const hello = 'world';",
                    "path": "src/index.ts",
                },
                {
                    "contents": "export function helper() {}",
                    "path": "src/utils.ts",
                },
            ],
            fixes=["dependency"],
            meta={"external_id": "external_id"},
            mode="project",
            response_encoding="json",
            response_format="ALL_FILES",
            template_id="template_id",
            template_path="template_path",
        )
        assert_matches_type(FixerRunResponse, fixer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_run(self, client: Benchify) -> None:
        response = client.fixer.with_raw_response.run()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fixer = response.parse()
        assert_matches_type(FixerRunResponse, fixer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run(self, client: Benchify) -> None:
        with client.fixer.with_streaming_response.run() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fixer = response.parse()
            assert_matches_type(FixerRunResponse, fixer, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFixer:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run(self, async_client: AsyncBenchify) -> None:
        fixer = await async_client.fixer.run()
        assert_matches_type(FixerRunResponse, fixer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncBenchify) -> None:
        fixer = await async_client.fixer.run(
            bundle=False,
            event_id="event_id",
            files=[
                {
                    "contents": "export const hello = 'world';",
                    "path": "src/index.ts",
                },
                {
                    "contents": "export function helper() {}",
                    "path": "src/utils.ts",
                },
            ],
            fixes=["dependency"],
            meta={"external_id": "external_id"},
            mode="project",
            response_encoding="json",
            response_format="ALL_FILES",
            template_id="template_id",
            template_path="template_path",
        )
        assert_matches_type(FixerRunResponse, fixer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncBenchify) -> None:
        response = await async_client.fixer.with_raw_response.run()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fixer = await response.parse()
        assert_matches_type(FixerRunResponse, fixer, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncBenchify) -> None:
        async with async_client.fixer.with_streaming_response.run() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fixer = await response.parse()
            assert_matches_type(FixerRunResponse, fixer, path=["response"])

        assert cast(Any, response.is_closed) is True
