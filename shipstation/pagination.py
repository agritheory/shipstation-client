import typing
from decimal import Decimal
from functools import partial

from attr import attrib, attrs
from httpx import Response

from shipstation.base import ShipStationBase


@attrs(auto_attribs=True)
class Page:
    key: str
    type: type
    call: typing.Tuple[typing.Callable, typing.Dict[str, typing.Any]]
    results: typing.List[ShipStationBase] = []
    page: int = 0
    pages: int = 0
    total: int = 0
    _index: int = 0

    def __attrs_post_init__(self) -> None:
        f, args = self.call[0], self.call[1]
        response = f(**args).json(parse_float=Decimal)
        self.load_results(response)

    def load_results(self, response: Response) -> "Page":
        results = getattr(response, self.key, [])
        self.results = [self.type().json(r) for r in results]
        self.page = getattr(response, "page", 0)
        self.pages = getattr(response, "pages", 0)
        self.total = getattr(response, "total", 0)
        self._index = 0
        return self

    def __iter__(self) -> "Page":
        return self

    def __next__(self) -> typing.Optional[ShipStationBase]:
        if self.results and self._index >= len(self.results):
            self = self.next_page()
            return None
        results = self.results[self._index] if self.results else None
        self._index += 1
        return results

    def next_page(self) -> "Page":
        if self.page >= self.pages:
            raise StopIteration
        f, args = self.call[0], self.call[1]
        args["payload"] = str({"page": str(self.page + 1)})
        response = f(**args).json(parse_float=Decimal)
        return self.load_results(response)

    def __getitem__(self, index) -> ShipStationBase:
        return self.results[index]
