from abc import ABC
from typing import Any, Union

import requests
from requests import Response

from framework.utils import Logger


class ApiBase(ABC):
    def _get(self, uri: Union[str, bytes]) -> Response:
        Logger().info(f"Send GET-request: {uri}")
        return requests.get(uri)

    def _post(self, uri: Union[str, bytes], data: Any = None, json: Any = None) -> Response:
        Logger().info(f"Send POST-request: {uri}, data: {data}, json: {json}")
        return requests.post(uri, data=data, json=json)

    def _put(self, uri: Union[str, bytes], data: Any = None, json: Any = None) -> Response:
        Logger().info(f"Send PUT-request: {uri}, data: {data}, json: {json}")
        return requests.put(uri, data=data, json=json)

    def _delete(self, uri: Union[str, bytes]) -> Response:
        Logger().info(f"Send DELETE-request: {uri}")
        return requests.delete(uri)
