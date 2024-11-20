# Copyright (c) 2024 RFull Development
# This source code is managed under the MIT license. See LICENSE in the project root.
from typing import Any

from kiota_abstractions.authentication.anonymous_authentication_provider import \
    AnonymousAuthenticationProvider
from kiota_http.httpx_request_adapter import HttpxRequestAdapter

from api.client.api_client import ApiClient


class RepoInfo:
    def __init__(self) -> None:
        self.namespace = ""
        self.repository = ""
        self.tag = ""


class RepoClient:
    def __init__(self) -> None:
        pass

    def __open(self) -> None:
        provider = AnonymousAuthenticationProvider()
        adapter = HttpxRequestAdapter(provider)
        client = ApiClient(adapter)
        return client

    async def get_info(self, repoInfo: RepoInfo) -> Any:
        client = self.__open()
        response = await client.v2.namespaces.by_namespace(repoInfo.namespace).repositories.by_repository(repoInfo.repository).tags.by_tag(repoInfo.tag).get()
        return response
