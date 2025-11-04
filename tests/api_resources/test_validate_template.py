# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from benchify import Benchify, AsyncBenchify
from tests.utils import assert_matches_type
from benchify.types import ValidateTemplateValidateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestValidateTemplate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_validate(self, client: Benchify) -> None:
        validate_template = client.validate_template.validate()
        assert_matches_type(ValidateTemplateValidateResponse, validate_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_validate_with_all_params(self, client: Benchify) -> None:
        validate_template = client.validate_template.validate(
            meta={"external_id": "external_id"},
            response_format="DIFF",
            body_template_id_1="template_id",
            template_path="template_path",
            body_template_id_2="templateId",
            template_name="templateName",
        )
        assert_matches_type(ValidateTemplateValidateResponse, validate_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_validate(self, client: Benchify) -> None:
        response = client.validate_template.with_raw_response.validate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate_template = response.parse()
        assert_matches_type(ValidateTemplateValidateResponse, validate_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_validate(self, client: Benchify) -> None:
        with client.validate_template.with_streaming_response.validate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate_template = response.parse()
            assert_matches_type(ValidateTemplateValidateResponse, validate_template, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncValidateTemplate:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_validate(self, async_client: AsyncBenchify) -> None:
        validate_template = await async_client.validate_template.validate()
        assert_matches_type(ValidateTemplateValidateResponse, validate_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_validate_with_all_params(self, async_client: AsyncBenchify) -> None:
        validate_template = await async_client.validate_template.validate(
            meta={"external_id": "external_id"},
            response_format="DIFF",
            body_template_id_1="template_id",
            template_path="template_path",
            body_template_id_2="templateId",
            template_name="templateName",
        )
        assert_matches_type(ValidateTemplateValidateResponse, validate_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncBenchify) -> None:
        response = await async_client.validate_template.with_raw_response.validate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate_template = await response.parse()
        assert_matches_type(ValidateTemplateValidateResponse, validate_template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncBenchify) -> None:
        async with async_client.validate_template.with_streaming_response.validate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate_template = await response.parse()
            assert_matches_type(ValidateTemplateValidateResponse, validate_template, path=["response"])

        assert cast(Any, response.is_closed) is True
