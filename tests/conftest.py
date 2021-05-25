import json

import pytest
import respx
from httpx import Response

import api_data
from shipstation.api import ShipStation
from shipstation.models import *


@pytest.fixture
def ss() -> ShipStation:
    yield ShipStation(key="123456789", secret="123456789", debug=False, timeout=1)


@pytest.fixture(scope="session")
def mocked_api() -> respx.MockTransport:
    base_url = "https://ssapi.shipstation.com"
    with respx.mock(base_url=base_url, assert_all_called=False) as respx_mock:
        respx_mock.get(
            "/carriers/getcarrier?carrierCode=stamps_com",
            content=api_data.get_carrier,
            alias="get_carrier",
        )
        respx_mock.get(
            "/customers/123456789", content=api_data.get_customer, alias="get_customer",
        )
        respx_mock.get(
            "/orders/123456789", content=api_data.get_order, alias="get_order"
        )
        respx_mock.get(
            "/products/123456789", content=api_data.get_product, alias="get_product"
        )
        respx_mock.post(
            "/shipments/getrates", content=api_data.get_rates, alias="get_rates"
        )
        respx_mock.get("/stores/12345", content=api_data.get_store, alias="get_store")
        respx_mock.get(
            "/warehouses/456789", content=api_data.get_warehouse, alias="get_warehouse",
        )
        respx_mock.get(
            "/carriers", content=api_data.list_carriers, alias="list_carriers"
        )
        respx_mock.get(
            "/customers", content=api_data.list_customers, alias="list_customers"
        )
        respx_mock.get(
            "/fulfillments",
            content=api_data.list_fulfillments,
            alias="list_fulfillments",
        )
        respx_mock.get(
            "/stores/marketplaces",
            content=api_data.list_marketplaces,
            alias="list_marketplaces",
        )
        respx_mock.get(
            "/orders/list", content=api_data.list_orders, alias="list_orders",
        )
        respx_mock.get(
            "/carriers/listpackages?carrierCode=stamps_com",
            content=api_data.list_packages,
            alias="list_packages",
        )
        # tested in test_pagination.py
        # respx_mock.get(
        #     "/products", content=api_data.list_products, alias="list_products",
        # )
        respx_mock.get(
            "/shipments", content=api_data.list_shipments, alias="list_shipments",
        )
        # mocking with an exception: https://lundberg.github.io/respx/guide/#modulo-shortcut
        respx_mock.get("/shipments", alias="list_shipments_error") % Response(500)
        respx_mock.get(
            "/carriers/listservices?carrierCode=stamps_com",
            content=api_data.list_services,
            alias="list_services",
        )
        respx_mock.get(
            "/stores?marketplaceId=2",
            content=api_data.list_stores,
            alias="list_stores",
        )
        respx_mock.get(
            "/accounts/listtags", content=api_data.list_tags, alias="list_tags"
        )
        respx_mock.get("/users", content=api_data.list_users, alias="list_users")
        respx_mock.get(
            "/warehouses", content=api_data.list_warehouses, alias="list_warehouses"
        )
        # respx_mock.get(
        #     "/accounts/users", content=api_data.list_webhooks, alias="list_webhooks"
        # )
        yield respx_mock
