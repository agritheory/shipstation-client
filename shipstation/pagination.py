from typing import Any

from collections.abc import Callable
from decimal import Decimal

from attrs import define
from httpx import Response
from shipstation.base import ShipStationBase


@define(auto_attribs=True)
class Page:
    key: str
    type: type
    call: tuple[Callable, dict[str, Any]] | None
    results: list[ShipStationBase] = []
    params: dict[str, Any] | None = None
    page: int = 0
    pages: int = 0
    total: int = 0
    _index: int = 0

    def __attrs_post_init__(self) -> None:
        f, args = self.call[0], self.call[1]
        if self.params:
            args = {**self.call[1], "payload": self.params}
        response = f(**args)
        self.load_results(response)

    def load_results(self, response: Response) -> "Page":
        results = response.json(parse_float=Decimal)
        self.results = []
        self.results = [self.type().json(r) for r in results.get(self.key)]
        self.page = results.get("page", 0)
        self.pages = results.get("pages", 0)
        self.total = results.get("total", 0)
        self._index = 0
        return self

    def __iter__(self) -> "Page":
        return self

    def __next__(self) -> ShipStationBase | None:
        if not self.results:
            raise StopIteration
        if self.results and self._index == len(self.results):
            self = self.next_page()
        results = self.results[self._index] if self.results else None
        self._index += 1
        return results

    def next_page(self) -> "Page":
        if self.page >= self.pages:
            raise StopIteration
        api_method, args = self.call[0], self.call[1]
        args["payload"] = {**(self.params or {}), "page": str(self.page + 1)}
        return self.load_results(api_method(**args))

    def __getitem__(self, index) -> ShipStationBase:
        return self.results[index]

    def __len__(self) -> int:
        return len(self.results)
