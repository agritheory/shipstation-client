import api_data
import pytest
from httpx import HTTPStatusError, Response
from respx import mock
from shipstation.api import ShipStation
from shipstation.models import *


@pytest.fixture
def ss():
    yield ShipStation(key="123456789", secret="123456789", debug=False, timeout=1)


@pytest.fixture(scope="session")
def mocked_api():
    with mock(
        base_url="https://ssapi.shipstation.com", assert_all_called=False
    ) as respx_mock:
        respx_mock.get(
            "/carriers/getcarrier?carrierCode=stamps_com",
            name="get_carrier",
        ).respond(200, json=api_data.get_carrier)

        respx_mock.get(
            "/customers/123456789",
            name="get_customer",
        ).respond(200, json=api_data.get_customer)

        respx_mock.get("/orders/123456789", name="get_order").respond(
            200, json=api_data.get_order
        )
        respx_mock.get("/products/123456789", name="get_product").respond(
            200, json=api_data.get_product
        )
        respx_mock.post("/shipments/getrates", name="get_rates").respond(
            200, json=api_data.get_rates
        )
        respx_mock.get("/stores/12345", name="get_store").respond(
            200, json=api_data.get_store
        )

        respx_mock.get(
            "/warehouses/456789",
            name="get_warehouse",
        ).respond(200, json=api_data.get_warehouse)

        respx_mock.get("/carriers", name="list_carriers").respond(
            200, json=api_data.list_carriers
        )

        respx_mock.get("/customers", name="list_customers").respond(
            200, json=api_data.list_customers
        )

        respx_mock.get(
            "/fulfillments",
            name="list_fulfillments",
        ).respond(200, json=api_data.list_fulfillments)

        respx_mock.get(
            "/stores/marketplaces",
            name="list_marketplaces",
        ).respond(200, json=api_data.list_marketplaces)

        respx_mock.get(
            "/orders/list",
            name="list_orders",
        ).respond(200, json=api_data.list_orders)

        respx_mock.get(
            "/carriers/listpackages?carrierCode=stamps_com",
            name="list_packages",
        ).respond(200, json=api_data.list_packages)

        # mocking with an exception: https://lundberg.github.io/respx/guide/#exceptions
        respx_mock.get(
            "/shipments",
            name="list_shipments",
        ).mock(
            side_effect=[
                Response(200, json=api_data.list_shipments),
                HTTPStatusError(
                    message="Not Found",
                    request=None,
                    response=Response(404, json={"message": "Not Found"}),
                ),
            ]
        )

        respx_mock.get(
            "/carriers/listservices?carrierCode=stamps_com",
            name="list_services",
        ).respond(200, json=api_data.list_services)

        respx_mock.get(
            "/stores?marketplaceId=2",
            name="list_stores",
        ).respond(200, json=api_data.list_stores)

        respx_mock.get("/accounts/listtags", name="list_tags").respond(
            200, json=api_data.list_tags
        )
        respx_mock.get("/users", name="list_users").respond(
            200, json=api_data.list_users
        )
        respx_mock.get("/warehouses", name="list_warehouses").respond(
            200, json=api_data.list_warehouses
        )

        respx_mock.get("/accounts/users", name="list_webhooks").respond(
            200, json=api_data.list_webhooks
        )

        yield respx_mock
