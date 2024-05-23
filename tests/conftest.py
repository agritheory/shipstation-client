import pytest
from api_data import *
from httpx import HTTPStatusError, Response
from respx import mock
from shipstation.api import ShipStation


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
        ).respond(200, json=GET_CARRIER)

        respx_mock.get(
            "/customers/123456789",
            name="get_customer",
        ).respond(200, json=GET_CUSTOMER)

        respx_mock.get("/orders/123456789", name="get_order").respond(
            200, json=GET_ORDER
        )
        respx_mock.get("/products/123456789", name="get_product").respond(
            200, json=GET_PRODUCT
        )
        respx_mock.post("/shipments/getrates", name="get_rates").respond(
            200, json=GET_RATES
        )
        respx_mock.get("/stores/12345", name="get_store").respond(200, json=GET_STORE)

        respx_mock.get(
            "/warehouses/456789",
            name="get_warehouse",
        ).respond(200, json=GET_WAREHOUSE)

        respx_mock.get("/carriers", name="list_carriers").respond(
            200, json=LIST_CARRIERS
        )

        respx_mock.get("/customers", name="list_customers").respond(
            200, json=LIST_CUSTOMERS
        )

        respx_mock.get(
            "/fulfillments",
            name="list_fulfillments",
        ).respond(200, json=LIST_FULFILLMENTS)

        respx_mock.get(
            "/stores/marketplaces",
            name="list_marketplaces",
        ).respond(200, json=LIST_MARKETPLACES)

        respx_mock.get(
            "/orders/list",
            name="list_orders",
        ).respond(200, json=LIST_ORDERS)

        respx_mock.get(
            "/carriers/listpackages?carrierCode=stamps_com",
            name="list_packages",
        ).respond(200, json=LIST_PACKAGES)

        # mocking with an exception: https://lundberg.github.io/respx/guide/#exceptions
        respx_mock.get(
            "/shipments",
            name="list_shipments",
        ).mock(
            side_effect=[
                Response(200, json=LIST_SHIPMENTS),
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
        ).respond(200, json=LIST_SERVICES)

        respx_mock.get(
            "/stores?marketplaceId=2",
            name="list_stores",
        ).respond(200, json=LIST_STORES)

        respx_mock.get("/accounts/listtags", name="list_tags").respond(
            200, json=LIST_TAGS
        )
        respx_mock.get("/users", name="list_users").respond(200, json=LIST_USERS)
        respx_mock.get("/warehouses", name="list_warehouses").respond(
            200, json=LIST_WAREHOUSES
        )

        respx_mock.get("/accounts/users", name="list_webhooks").respond(
            200, json=LIST_WEBHOOKS
        )

        yield respx_mock
