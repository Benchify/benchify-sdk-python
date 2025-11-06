# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from benchify import Benchify, AsyncBenchify
from tests.utils import assert_matches_type
from benchify.types import FixParsingAndDiagnoseDetectIssuesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFixParsingAndDiagnose:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_detect_issues(self, client: Benchify) -> None:
        fix_parsing_and_diagnose = client.fix_parsing_and_diagnose.detect_issues()
        assert_matches_type(FixParsingAndDiagnoseDetectIssuesResponse, fix_parsing_and_diagnose, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_detect_issues_with_all_params(self, client: Benchify) -> None:
        fix_parsing_and_diagnose = client.fix_parsing_and_diagnose.detect_issues(
            event_id="",
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
            meta={"external_id": "external_id"},
            template_path="benchify/default-template",
        )
        assert_matches_type(FixParsingAndDiagnoseDetectIssuesResponse, fix_parsing_and_diagnose, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_detect_issues(self, client: Benchify) -> None:
        response = client.fix_parsing_and_diagnose.with_raw_response.detect_issues()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fix_parsing_and_diagnose = response.parse()
        assert_matches_type(FixParsingAndDiagnoseDetectIssuesResponse, fix_parsing_and_diagnose, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_detect_issues(self, client: Benchify) -> None:
        with client.fix_parsing_and_diagnose.with_streaming_response.detect_issues() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fix_parsing_and_diagnose = response.parse()
            assert_matches_type(FixParsingAndDiagnoseDetectIssuesResponse, fix_parsing_and_diagnose, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFixParsingAndDiagnose:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_detect_issues(self, async_client: AsyncBenchify) -> None:
        fix_parsing_and_diagnose = await async_client.fix_parsing_and_diagnose.detect_issues()
        assert_matches_type(FixParsingAndDiagnoseDetectIssuesResponse, fix_parsing_and_diagnose, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_detect_issues_with_all_params(self, async_client: AsyncBenchify) -> None:
        fix_parsing_and_diagnose = await async_client.fix_parsing_and_diagnose.detect_issues(
            event_id="",
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
            meta={"external_id": "external_id"},
            template_path="benchify/default-template",
        )
        assert_matches_type(FixParsingAndDiagnoseDetectIssuesResponse, fix_parsing_and_diagnose, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_detect_issues(self, async_client: AsyncBenchify) -> None:
        response = await async_client.fix_parsing_and_diagnose.with_raw_response.detect_issues()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fix_parsing_and_diagnose = await response.parse()
        assert_matches_type(FixParsingAndDiagnoseDetectIssuesResponse, fix_parsing_and_diagnose, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_detect_issues(self, async_client: AsyncBenchify) -> None:
        async with async_client.fix_parsing_and_diagnose.with_streaming_response.detect_issues() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fix_parsing_and_diagnose = await response.parse()
            assert_matches_type(FixParsingAndDiagnoseDetectIssuesResponse, fix_parsing_and_diagnose, path=["response"])

        assert cast(Any, response.is_closed) is True
