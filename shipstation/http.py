import pprint
import typing

import httpx
from httpx._types import AuthTypes, QueryParamTypes, RequestData

from shipstation.base import ShipStationBase


class ShipStationHTTP(ShipStationBase):
    url: typing.Optional[str] = None
    key: typing.Optional[str] = None
    secret: typing.Optional[str] = None
    debug: typing.Optional[bool] = False
    timeout: typing.Optional[int] = None

    def __init__(
        self, key: str, secret: str, debug: bool = False, timeout: int = 1
    ) -> None:
        if key is None:
            raise AttributeError("Key must be supplied.")
        if secret is None:
            raise AttributeError("Secret must be supplied.")
        self.url = "https://ssapi.shipstation.com"
        self.key = key
        self.secret = secret
        self.timeout = timeout
        self.debug = debug

    @property
    def auth(self) -> AuthTypes:
        return tuple([self.key, self.secret])  # type: ignore

    def get(self, payload: QueryParamTypes, endpoint: str = "") -> httpx.Response:
        r = httpx.get(
            url=f"{self.url}{endpoint}",
            auth=self.auth,
            params=payload,
            timeout=self.timeout,
        )
        if self.debug:
            pprint.PrettyPrinter(indent=4).pprint(f"GET {self.url}{endpoint}")
            pprint.PrettyPrinter(indent=4).pprint(r.json())
        return r

    def post(self, data: RequestData, endpoint: str = "") -> httpx.Response:
        r = httpx.post(
            url=f"{self.url}{endpoint}",
            auth=self.auth,
            data=data,
            headers={"content-type": "application/json"},
            timeout=self.timeout,
        )
        if self.debug:
            pprint.PrettyPrinter(indent=4).pprint(r.json())
        return r

    def put(self, data: RequestData, endpoint: str = "") -> httpx.Response:
        r = httpx.put(
            url=f"{self.url}{endpoint}",
            auth=self.auth,
            data=data,
            headers={"content-type": "application/json"},
            timeout=self.timeout,
        )
        if self.debug:
            pprint.PrettyPrinter(indent=4).pprint(f" PUT {self.url}{endpoint}")
            pprint.PrettyPrinter(indent=4).pprint(r.json())
        return r

    def delete(self, payload: QueryParamTypes, endpoint: str = "") -> httpx.Response:
        r = httpx.delete(
            url=f"{self.url}{endpoint}",
            auth=self.auth,
            params=payload,
            timeout=self.timeout,
        )
        if self.debug:
            pprint.PrettyPrinter(indent=4).pprint(f" DELETE {self.url}{endpoint}")
            pprint.PrettyPrinter(indent=4).pprint(r)
        return r
