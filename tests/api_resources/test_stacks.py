# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from benchify import Benchify, AsyncBenchify
from tests.utils import assert_matches_type
from benchify.types import (
    StackCreateResponse,
    StackUpdateResponse,
    StackGetLogsResponse,
    StackRetrieveResponse,
    StackCreateAndRunResponse,
    StackExecuteCommandResponse,
    StackGetNetworkInfoResponse,
    StackWaitForDevServerURLResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStacks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Benchify) -> None:
        stack = client.stacks.create(
            bundle=b"raw file contents",
            manifest=b"raw file contents",
            idempotency_key="key-12345678",
        )
        assert_matches_type(StackCreateResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Benchify) -> None:
        stack = client.stacks.create(
            bundle=b"raw file contents",
            manifest=b"raw file contents",
            idempotency_key="key-12345678",
            options="options",
            content_hash="sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        )
        assert_matches_type(StackCreateResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Benchify) -> None:
        response = client.stacks.with_raw_response.create(
            bundle=b"raw file contents",
            manifest=b"raw file contents",
            idempotency_key="key-12345678",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stack = response.parse()
        assert_matches_type(StackCreateResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Benchify) -> None:
        with client.stacks.with_streaming_response.create(
            bundle=b"raw file contents",
            manifest=b"raw file contents",
            idempotency_key="key-12345678",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stack = response.parse()
            assert_matches_type(StackCreateResponse, stack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Benchify) -> None:
        stack = client.stacks.retrieve(
            "stk_abc123",
        )
        assert_matches_type(StackRetrieveResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Benchify) -> None:
        response = client.stacks.with_raw_response.retrieve(
            "stk_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stack = response.parse()
        assert_matches_type(StackRetrieveResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Benchify) -> None:
        with client.stacks.with_streaming_response.retrieve(
            "stk_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stack = response.parse()
            assert_matches_type(StackRetrieveResponse, stack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Benchify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.stacks.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Benchify) -> None:
        stack = client.stacks.update(
            id="stk_abc123",
            idempotency_key="key-12345678",
        )
        assert_matches_type(StackUpdateResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Benchify) -> None:
        stack = client.stacks.update(
            id="stk_abc123",
            idempotency_key="key-12345678",
            bundle=b"raw file contents",
            manifest=b"raw file contents",
            ops="ops",
            base_etag="sha256:abc123...",
        )
        assert_matches_type(StackUpdateResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Benchify) -> None:
        response = client.stacks.with_raw_response.update(
            id="stk_abc123",
            idempotency_key="key-12345678",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stack = response.parse()
        assert_matches_type(StackUpdateResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Benchify) -> None:
        with client.stacks.with_streaming_response.update(
            id="stk_abc123",
            idempotency_key="key-12345678",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stack = response.parse()
            assert_matches_type(StackUpdateResponse, stack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Benchify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.stacks.with_raw_response.update(
                id="",
                idempotency_key="key-12345678",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_and_run(self, client: Benchify) -> None:
        stack = client.stacks.create_and_run(
            command=["sleep", "3600"],
            image="curlimages/curl:latest",
        )
        assert_matches_type(StackCreateAndRunResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_and_run_with_all_params(self, client: Benchify) -> None:
        stack = client.stacks.create_and_run(
            command=["sleep", "3600"],
            image="curlimages/curl:latest",
            ttl_seconds=3600,
            wait=False,
        )
        assert_matches_type(StackCreateAndRunResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_and_run(self, client: Benchify) -> None:
        response = client.stacks.with_raw_response.create_and_run(
            command=["sleep", "3600"],
            image="curlimages/curl:latest",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stack = response.parse()
        assert_matches_type(StackCreateAndRunResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_and_run(self, client: Benchify) -> None:
        with client.stacks.with_streaming_response.create_and_run(
            command=["sleep", "3600"],
            image="curlimages/curl:latest",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stack = response.parse()
            assert_matches_type(StackCreateAndRunResponse, stack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_destroy(self, client: Benchify) -> None:
        stack = client.stacks.destroy(
            "stk_abc123",
        )
        assert stack is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_destroy(self, client: Benchify) -> None:
        response = client.stacks.with_raw_response.destroy(
            "stk_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stack = response.parse()
        assert stack is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_destroy(self, client: Benchify) -> None:
        with client.stacks.with_streaming_response.destroy(
            "stk_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stack = response.parse()
            assert stack is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_destroy(self, client: Benchify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.stacks.with_raw_response.destroy(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_execute_command(self, client: Benchify) -> None:
        stack = client.stacks.execute_command(
            id="stk_abc123",
            command=["curl", "-s", "https://example.com"],
        )
        assert_matches_type(StackExecuteCommandResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_execute_command(self, client: Benchify) -> None:
        response = client.stacks.with_raw_response.execute_command(
            id="stk_abc123",
            command=["curl", "-s", "https://example.com"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stack = response.parse()
        assert_matches_type(StackExecuteCommandResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_execute_command(self, client: Benchify) -> None:
        with client.stacks.with_streaming_response.execute_command(
            id="stk_abc123",
            command=["curl", "-s", "https://example.com"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stack = response.parse()
            assert_matches_type(StackExecuteCommandResponse, stack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_execute_command(self, client: Benchify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.stacks.with_raw_response.execute_command(
                id="",
                command=["curl", "-s", "https://example.com"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_logs(self, client: Benchify) -> None:
        stack = client.stacks.get_logs(
            id="stk_abc123",
        )
        assert_matches_type(StackGetLogsResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_logs_with_all_params(self, client: Benchify) -> None:
        stack = client.stacks.get_logs(
            id="stk_abc123",
            tail="100",
        )
        assert_matches_type(StackGetLogsResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_logs(self, client: Benchify) -> None:
        response = client.stacks.with_raw_response.get_logs(
            id="stk_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stack = response.parse()
        assert_matches_type(StackGetLogsResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_logs(self, client: Benchify) -> None:
        with client.stacks.with_streaming_response.get_logs(
            id="stk_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stack = response.parse()
            assert_matches_type(StackGetLogsResponse, stack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_logs(self, client: Benchify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.stacks.with_raw_response.get_logs(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_network_info(self, client: Benchify) -> None:
        stack = client.stacks.get_network_info(
            "stk_abc123",
        )
        assert_matches_type(StackGetNetworkInfoResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_network_info(self, client: Benchify) -> None:
        response = client.stacks.with_raw_response.get_network_info(
            "stk_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stack = response.parse()
        assert_matches_type(StackGetNetworkInfoResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_network_info(self, client: Benchify) -> None:
        with client.stacks.with_streaming_response.get_network_info(
            "stk_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stack = response.parse()
            assert_matches_type(StackGetNetworkInfoResponse, stack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_network_info(self, client: Benchify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.stacks.with_raw_response.get_network_info(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_wait_for_dev_server_url(self, client: Benchify) -> None:
        stack = client.stacks.wait_for_dev_server_url(
            id="stk_abc123",
        )
        assert_matches_type(StackWaitForDevServerURLResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_wait_for_dev_server_url_with_all_params(self, client: Benchify) -> None:
        stack = client.stacks.wait_for_dev_server_url(
            id="stk_abc123",
            interval="200",
            api_timeout="60",
        )
        assert_matches_type(StackWaitForDevServerURLResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_wait_for_dev_server_url(self, client: Benchify) -> None:
        response = client.stacks.with_raw_response.wait_for_dev_server_url(
            id="stk_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stack = response.parse()
        assert_matches_type(StackWaitForDevServerURLResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_wait_for_dev_server_url(self, client: Benchify) -> None:
        with client.stacks.with_streaming_response.wait_for_dev_server_url(
            id="stk_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stack = response.parse()
            assert_matches_type(StackWaitForDevServerURLResponse, stack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_wait_for_dev_server_url(self, client: Benchify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.stacks.with_raw_response.wait_for_dev_server_url(
                id="",
            )


class TestAsyncStacks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncBenchify) -> None:
        stack = await async_client.stacks.create(
            bundle=b"raw file contents",
            manifest=b"raw file contents",
            idempotency_key="key-12345678",
        )
        assert_matches_type(StackCreateResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBenchify) -> None:
        stack = await async_client.stacks.create(
            bundle=b"raw file contents",
            manifest=b"raw file contents",
            idempotency_key="key-12345678",
            options="options",
            content_hash="sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        )
        assert_matches_type(StackCreateResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBenchify) -> None:
        response = await async_client.stacks.with_raw_response.create(
            bundle=b"raw file contents",
            manifest=b"raw file contents",
            idempotency_key="key-12345678",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stack = await response.parse()
        assert_matches_type(StackCreateResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBenchify) -> None:
        async with async_client.stacks.with_streaming_response.create(
            bundle=b"raw file contents",
            manifest=b"raw file contents",
            idempotency_key="key-12345678",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stack = await response.parse()
            assert_matches_type(StackCreateResponse, stack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBenchify) -> None:
        stack = await async_client.stacks.retrieve(
            "stk_abc123",
        )
        assert_matches_type(StackRetrieveResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBenchify) -> None:
        response = await async_client.stacks.with_raw_response.retrieve(
            "stk_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stack = await response.parse()
        assert_matches_type(StackRetrieveResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBenchify) -> None:
        async with async_client.stacks.with_streaming_response.retrieve(
            "stk_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stack = await response.parse()
            assert_matches_type(StackRetrieveResponse, stack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBenchify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.stacks.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncBenchify) -> None:
        stack = await async_client.stacks.update(
            id="stk_abc123",
            idempotency_key="key-12345678",
        )
        assert_matches_type(StackUpdateResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBenchify) -> None:
        stack = await async_client.stacks.update(
            id="stk_abc123",
            idempotency_key="key-12345678",
            bundle=b"raw file contents",
            manifest=b"raw file contents",
            ops="ops",
            base_etag="sha256:abc123...",
        )
        assert_matches_type(StackUpdateResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBenchify) -> None:
        response = await async_client.stacks.with_raw_response.update(
            id="stk_abc123",
            idempotency_key="key-12345678",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stack = await response.parse()
        assert_matches_type(StackUpdateResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBenchify) -> None:
        async with async_client.stacks.with_streaming_response.update(
            id="stk_abc123",
            idempotency_key="key-12345678",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stack = await response.parse()
            assert_matches_type(StackUpdateResponse, stack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncBenchify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.stacks.with_raw_response.update(
                id="",
                idempotency_key="key-12345678",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_and_run(self, async_client: AsyncBenchify) -> None:
        stack = await async_client.stacks.create_and_run(
            command=["sleep", "3600"],
            image="curlimages/curl:latest",
        )
        assert_matches_type(StackCreateAndRunResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_and_run_with_all_params(self, async_client: AsyncBenchify) -> None:
        stack = await async_client.stacks.create_and_run(
            command=["sleep", "3600"],
            image="curlimages/curl:latest",
            ttl_seconds=3600,
            wait=False,
        )
        assert_matches_type(StackCreateAndRunResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_and_run(self, async_client: AsyncBenchify) -> None:
        response = await async_client.stacks.with_raw_response.create_and_run(
            command=["sleep", "3600"],
            image="curlimages/curl:latest",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stack = await response.parse()
        assert_matches_type(StackCreateAndRunResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_and_run(self, async_client: AsyncBenchify) -> None:
        async with async_client.stacks.with_streaming_response.create_and_run(
            command=["sleep", "3600"],
            image="curlimages/curl:latest",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stack = await response.parse()
            assert_matches_type(StackCreateAndRunResponse, stack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_destroy(self, async_client: AsyncBenchify) -> None:
        stack = await async_client.stacks.destroy(
            "stk_abc123",
        )
        assert stack is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_destroy(self, async_client: AsyncBenchify) -> None:
        response = await async_client.stacks.with_raw_response.destroy(
            "stk_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stack = await response.parse()
        assert stack is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_destroy(self, async_client: AsyncBenchify) -> None:
        async with async_client.stacks.with_streaming_response.destroy(
            "stk_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stack = await response.parse()
            assert stack is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_destroy(self, async_client: AsyncBenchify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.stacks.with_raw_response.destroy(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_execute_command(self, async_client: AsyncBenchify) -> None:
        stack = await async_client.stacks.execute_command(
            id="stk_abc123",
            command=["curl", "-s", "https://example.com"],
        )
        assert_matches_type(StackExecuteCommandResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_execute_command(self, async_client: AsyncBenchify) -> None:
        response = await async_client.stacks.with_raw_response.execute_command(
            id="stk_abc123",
            command=["curl", "-s", "https://example.com"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stack = await response.parse()
        assert_matches_type(StackExecuteCommandResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_execute_command(self, async_client: AsyncBenchify) -> None:
        async with async_client.stacks.with_streaming_response.execute_command(
            id="stk_abc123",
            command=["curl", "-s", "https://example.com"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stack = await response.parse()
            assert_matches_type(StackExecuteCommandResponse, stack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_execute_command(self, async_client: AsyncBenchify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.stacks.with_raw_response.execute_command(
                id="",
                command=["curl", "-s", "https://example.com"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_logs(self, async_client: AsyncBenchify) -> None:
        stack = await async_client.stacks.get_logs(
            id="stk_abc123",
        )
        assert_matches_type(StackGetLogsResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_logs_with_all_params(self, async_client: AsyncBenchify) -> None:
        stack = await async_client.stacks.get_logs(
            id="stk_abc123",
            tail="100",
        )
        assert_matches_type(StackGetLogsResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_logs(self, async_client: AsyncBenchify) -> None:
        response = await async_client.stacks.with_raw_response.get_logs(
            id="stk_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stack = await response.parse()
        assert_matches_type(StackGetLogsResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_logs(self, async_client: AsyncBenchify) -> None:
        async with async_client.stacks.with_streaming_response.get_logs(
            id="stk_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stack = await response.parse()
            assert_matches_type(StackGetLogsResponse, stack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_logs(self, async_client: AsyncBenchify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.stacks.with_raw_response.get_logs(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_network_info(self, async_client: AsyncBenchify) -> None:
        stack = await async_client.stacks.get_network_info(
            "stk_abc123",
        )
        assert_matches_type(StackGetNetworkInfoResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_network_info(self, async_client: AsyncBenchify) -> None:
        response = await async_client.stacks.with_raw_response.get_network_info(
            "stk_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stack = await response.parse()
        assert_matches_type(StackGetNetworkInfoResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_network_info(self, async_client: AsyncBenchify) -> None:
        async with async_client.stacks.with_streaming_response.get_network_info(
            "stk_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stack = await response.parse()
            assert_matches_type(StackGetNetworkInfoResponse, stack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_network_info(self, async_client: AsyncBenchify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.stacks.with_raw_response.get_network_info(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_wait_for_dev_server_url(self, async_client: AsyncBenchify) -> None:
        stack = await async_client.stacks.wait_for_dev_server_url(
            id="stk_abc123",
        )
        assert_matches_type(StackWaitForDevServerURLResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_wait_for_dev_server_url_with_all_params(self, async_client: AsyncBenchify) -> None:
        stack = await async_client.stacks.wait_for_dev_server_url(
            id="stk_abc123",
            interval="200",
            api_timeout="60",
        )
        assert_matches_type(StackWaitForDevServerURLResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_wait_for_dev_server_url(self, async_client: AsyncBenchify) -> None:
        response = await async_client.stacks.with_raw_response.wait_for_dev_server_url(
            id="stk_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stack = await response.parse()
        assert_matches_type(StackWaitForDevServerURLResponse, stack, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_wait_for_dev_server_url(self, async_client: AsyncBenchify) -> None:
        async with async_client.stacks.with_streaming_response.wait_for_dev_server_url(
            id="stk_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stack = await response.parse()
            assert_matches_type(StackWaitForDevServerURLResponse, stack, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_wait_for_dev_server_url(self, async_client: AsyncBenchify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.stacks.with_raw_response.wait_for_dev_server_url(
                id="",
            )
