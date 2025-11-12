# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from benchify import Benchify, AsyncBenchify
from tests.utils import assert_matches_type
from benchify.types.stacks import BundleCreateFilesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBundle:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_files(self, client: Benchify) -> None:
        bundle = client.stacks.bundle.create_files(
            entrypoint="x",
            files=[
                {
                    "content": "<html>...</html>",
                    "path": "index.html",
                }
            ],
        )
        assert_matches_type(BundleCreateFilesResponse, bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_files_with_all_params(self, client: Benchify) -> None:
        bundle = client.stacks.bundle.create_files(
            entrypoint="x",
            files=[
                {
                    "content": "<html>...</html>",
                    "path": "index.html",
                }
            ],
            tarball_filename="tarball_filename",
        )
        assert_matches_type(BundleCreateFilesResponse, bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_files(self, client: Benchify) -> None:
        response = client.stacks.bundle.with_raw_response.create_files(
            entrypoint="x",
            files=[
                {
                    "content": "<html>...</html>",
                    "path": "index.html",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bundle = response.parse()
        assert_matches_type(BundleCreateFilesResponse, bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_files(self, client: Benchify) -> None:
        with client.stacks.bundle.with_streaming_response.create_files(
            entrypoint="x",
            files=[
                {
                    "content": "<html>...</html>",
                    "path": "index.html",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bundle = response.parse()
            assert_matches_type(BundleCreateFilesResponse, bundle, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBundle:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_files(self, async_client: AsyncBenchify) -> None:
        bundle = await async_client.stacks.bundle.create_files(
            entrypoint="x",
            files=[
                {
                    "content": "<html>...</html>",
                    "path": "index.html",
                }
            ],
        )
        assert_matches_type(BundleCreateFilesResponse, bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_files_with_all_params(self, async_client: AsyncBenchify) -> None:
        bundle = await async_client.stacks.bundle.create_files(
            entrypoint="x",
            files=[
                {
                    "content": "<html>...</html>",
                    "path": "index.html",
                }
            ],
            tarball_filename="tarball_filename",
        )
        assert_matches_type(BundleCreateFilesResponse, bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_files(self, async_client: AsyncBenchify) -> None:
        response = await async_client.stacks.bundle.with_raw_response.create_files(
            entrypoint="x",
            files=[
                {
                    "content": "<html>...</html>",
                    "path": "index.html",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bundle = await response.parse()
        assert_matches_type(BundleCreateFilesResponse, bundle, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_files(self, async_client: AsyncBenchify) -> None:
        async with async_client.stacks.bundle.with_streaming_response.create_files(
            entrypoint="x",
            files=[
                {
                    "content": "<html>...</html>",
                    "path": "index.html",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bundle = await response.parse()
            assert_matches_type(BundleCreateFilesResponse, bundle, path=["response"])

        assert cast(Any, response.is_closed) is True
