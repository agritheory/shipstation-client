import json

from httpx import BasicAuth, Client, Response
from httpx._types import QueryParamTypes, RequestData
from shipstation.base import ShipStationBase


class ShipStationHTTP(ShipStationBase):
    url: str | None = None
    key: str | None
    secret: str | None
    debug: bool | None = False
    timeout: int | None = None

    def __init__(
        self, key: str, secret: str, debug: bool = False, timeout: int = 1
    ) -> None:
        self.url = "https://ssapi.shipstation.com"
        self.key = key
        self.secret = secret
        self.timeout = timeout
        self.debug = debug

    @property
    def auth(self) -> BasicAuth:
        return BasicAuth(username=self.key, password=self.secret)

    @property
    def client(self) -> Client:
        return Client(
            base_url=self.url,
            auth=self.auth,
            headers={"content-type": "application/json"},
            timeout=self.timeout,
            event_hooks={
                "response": [
                    self.raise_for_status,
                    self.log_response,
                ]
            },
        )

    def log_response(self, response: Response) -> None:
        if self.debug:
            response.read()
            print(f"{response.request.method} {response.status_code} {response.url}")
            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, sort_keys=True))

    def raise_for_status(self, response: Response) -> None:
        response.raise_for_status()

    def get(
        self, endpoint: str = "", payload: QueryParamTypes | None = None
    ) -> Response:
        with self.client as client:
            return client.get(url=endpoint, params=payload)

    def post(self, endpoint: str = "", data: RequestData | None = None) -> Response:
        with self.client as client:
            return client.post(
                url=endpoint,
                data=data,
            )

    def put(self, endpoint: str = "", data: RequestData | None = None) -> Response:
        with self.client as client:
            return client.put(
                url=endpoint,
                data=data,
            )

    def delete(
        self, endpoint: str = "", payload: QueryParamTypes | None = None
    ) -> Response:
        with self.client as client:
            return client.delete(url=endpoint, params=payload)
