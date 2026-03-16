from __future__ import annotations

from typing import Any

import httpx

from src.config import Config

from .exceptions import APIError
from .models import User


class AsyncAPIClient:
    _instance: AsyncAPIClient | None = None

    def __init__(
        self,
        base_url: str,
        api_key: str,
        timeout: float = 10.0,
    ) -> None:
        self.base_url = base_url
        self.timeout = timeout

        headers = {"Content-Type": "application/json"}

        if api_key:
            headers["x-api-key"] = str(api_key)
        else:
            raise ValueError("API key is required for authentication")

        self._client = httpx.AsyncClient(
            base_url=self.base_url + "/v1", headers=headers, timeout=self.timeout
        )

    @staticmethod
    def instance() -> AsyncAPIClient:
        if not AsyncAPIClient._instance:
            config = Config.instance()
            AsyncAPIClient._instance = AsyncAPIClient(
                base_url=config.get_env_var("API_BASE_URL"),
                api_key=config.get_env_var("API_KEY"),
            )
            print("API client initialized successfully")
        return AsyncAPIClient._instance

    async def _request(
        self,
        method: str,
        endpoint: str,
        **kwargs: Any,
    ) -> Any:
        response = await self._client.request(method, endpoint, **kwargs)

        if response.status_code >= 400:
            raise APIError(response.status_code, response.text)

        if response.content:
            return response.json()

        return None

    async def get_user(self, user_id: int) -> User:
        data = await self._request("GET", f"/users/{str(user_id)}")
        return User(**data)

    async def sync_user(
        self,
        discord_id: int,
        username: str | None = None,
        global_name: str | None = None,
        avatar: str | None = None,
        banner: str | None = None,
    ) -> User:
        data = await self._request(
            "POST",
            "/users/sync",
            json={
                "discordId": str(discord_id),
                "username": username,
                "globalName": global_name,
                "avatar": avatar,
                "banner": banner,
            },
        )
        return User(**data)

    async def close(self) -> None:
        await self._client.aclose()
