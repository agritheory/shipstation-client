import json
import typing

import httpx
from httpx._types import AuthTypes, QueryParamTypes, RequestData

from shipstation.base import ShipStationBase


class ShipStationHTTP(ShipStationBase):
    url: typing.Optional[str] = None
    key: typing.Optional[str]
    secret: typing.Optional[str]
    debug: typing.Optional[bool] = False
    timeout: typing.Optional[int] = None

    def __init__(
        self, key: str, secret: str, debug: bool = False, timeout: int = 1
    ) -> None:
        self.url = "https://ssapi.shipstation.com"
        self.key = key
        self.secret = secret
        self.timeout = timeout
        self.debug = debug

    @property
    def auth(self) -> AuthTypes:
        return tuple([self.key, self.secret])  # type: ignore

    def get(self, payload: typing.Any = None, endpoint: str = "") -> httpx.Response:
        r = httpx.get(
            url=f"{self.url}{endpoint}",
            auth=self.auth,
            params=payload,
            timeout=self.timeout,
        )
        if self.debug:
            print(f"GET {r.url}")
            print(json.dumps(r.json(), indent=4, sort_keys=True))
        if r.is_error:
            r.raise_for_status()
        return r

    def post(self, data: typing.Any = None, endpoint: str = "") -> httpx.Response:
        r = httpx.post(
            url=f"{self.url}{endpoint}",
            auth=self.auth,
            data=data,
            headers={"content-type": "application/json"},
            timeout=self.timeout,
        )
        if self.debug:
            print(f"POST {r.url}")
            print(json.dumps(r.json(), indent=4, sort_keys=True))
        if r.is_error:
            r.raise_for_status()
        return r

    def put(self, data: typing.Any = None, endpoint: str = "") -> httpx.Response:
        r = httpx.put(
            url=f"{self.url}{endpoint}",
            auth=self.auth,
            data=data,
            headers={"content-type": "application/json"},
            timeout=self.timeout,
        )
        if self.debug:
            print(f"PUT {r.url}")
            print(json.dumps(r.json(), indent=4, sort_keys=True))
        if r.is_error:
            r.raise_for_status()
        return r

    def delete(self, payload: typing.Any = None, endpoint: str = "") -> httpx.Response:
        r = httpx.delete(
            url=f"{self.url}{endpoint}",
            auth=self.auth,
            params=payload,
            timeout=self.timeout,
        )
        if self.debug:
            print(f"DELETE {r.url}")
            print(json.dumps(r.json(), indent=4, sort_keys=True))
        if r.is_error:
            r.raise_for_status()
        return r
