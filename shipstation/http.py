import pprint

import httpx

from shipstation.base import ShipStationBase


class ShipStationHTTP(ShipStationBase):
    def get(self, endpoint="", payload=None):
        url = f"{self.url}{endpoint}"
        r = httpx.get(
            url, auth=(self.key, self.secret), params=payload, timeout=self.timeout
        )
        if self.debug:
            pprint.PrettyPrinter(indent=4).pprint("GET " + url)
            pprint.PrettyPrinter(indent=4).pprint(r.json())
        return r

    def post(self, endpoint="", data=None):
        url = f"{self.url}{endpoint}"
        headers = {"content-type": "application/json"}
        r = httpx.post(
            url,
            auth=(self.key, self.secret),
            data=data,
            headers=headers,
            timeout=self.timeout,
        )
        if self.debug:
            pprint.PrettyPrinter(indent=4).pprint(r.json())
        return r

    def put(self, endpoint="", data=None):
        url = f"{self.url}{endpoint}"
        headers = {"content-type": "application/json"}
        r = httpx.put(
            url,
            auth=(self.key, self.secret),
            data=data,
            headers=headers,
            timeout=self.timeout,
        )
        if self.debug:
            pprint.PrettyPrinter(indent=4).pprint("PUT " + url)
            pprint.PrettyPrinter(indent=4).pprint(r.json())
        return r

    def delete(self, endpoint="", payload=None):
        url = f"{self.url}{endpoint}"
        r = httpx.delete(
            url, auth=(self.key, self.secret), params=payload, timeout=self.timeout
        )
        if self.debug:
            pprint.PrettyPrinter(indent=4).pprint("DELETE " + url)
            pprint.PrettyPrinter(indent=4).pprint(r)
        return r
