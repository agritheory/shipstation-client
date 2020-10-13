import json
from decimal import Decimal

import pytest
import respx

import api_data
from conftest import ss
from shipstation.api import ShipStation
from shipstation.models import *
from shipstation.pagination import Page


@pytest.fixture(scope="session")
def mocked_pagination() -> respx.MockTransport:
    base_url = "https://ssapi.shipstation.com"
    with respx.mock(base_url=base_url, assert_all_called=False) as respx_mock:
        respx_mock.get(
            "/products", content=test_list_products_first,
        )
        respx_mock.get(
            "/products?page=2", content=test_list_products_second,
        )
        respx_mock.get(
            "/products?page=3", content=test_list_products_third,
        )
        respx_mock.get(
            "/products", content=list_products_none, alias="list_products_none"
        )
        respx_mock.get(
            "/products?pageSize=3", content=test_list_products_first,
        )
        respx_mock.get(
            "/products?pageSize=3&page=2", content=test_list_products_second,
        )
        respx_mock.get(
            "/products?pageSize=3&page=3", content=test_list_products_third,
        )
        yield respx_mock


@respx.mock
def test_no_results(ss: ShipStation, mocked_pagination: respx.MockTransport) -> None:
    request = mocked_pagination["list_products_none"]
    response = ss.list_products()
    assert isinstance(response, Page)
    for index, product in enumerate(response):
        assert True


@respx.mock
def test_list_products(ss: ShipStation, mocked_pagination: respx.MockTransport) -> None:
    response = ss.list_products()
    skus = (
        "987654321",
        "987654322",
        "987654323",
        "987654324",
        "987654325",
        "987654326",
        "987654327",
        "987654328",
    )
    assert isinstance(response, Page)
    for index, product in enumerate(response):
        assert isinstance(product, ShipStationItem)
        assert product.price == Decimal("11.99")
        assert product.sku == skus[index]


@respx.mock
def test_list_products_ensure_params(
    ss: ShipStation, mocked_pagination: respx.MockTransport
) -> None:
    request = mocked_pagination["list_products_params_1"]
    response = ss.list_products(parameters={"pageSize": "3"})
    skus = (
        "987654321",
        "987654322",
        "987654323",
        "987654324",
        "987654325",
        "987654326",
        "987654327",
        "987654328",
    )
    assert isinstance(response, Page)
    for index, product in enumerate(response):
        assert isinstance(product, ShipStationItem)
        assert product.price == Decimal("11.99")
        assert product.sku == skus[index]
        assert response.params == {"pageSize": "3"}


list_products_none = """
{
    "page": 1,
    "pages": 1,
    "products": [],
    "total": 1
}
"""


test_list_products_first = """
{
    "page": 1,
    "pages": 3,
    "products": [{
        "active": true,
        "aliases": null,
        "createDate": "2015-08-13T14:30:31.007",
        "customsCountryCode": null,
        "customsDescription": null,
        "customsTariffNo": null,
        "customsValue": null,
        "defaultCarrierCode": null,
        "defaultConfirmation": null,
        "defaultCost": null,
        "defaultIntlCarrierCode": null,
        "defaultIntlConfirmation": null,
        "defaultIntlPackageCode": null,
        "defaultIntlServiceCode": null,
        "defaultPackageCode": null,
        "defaultServiceCode": null,
        "fulfillmentSku": "712392290692",
        "height": null,
        "internalNotes": null,
        "length": null,
        "modifyDate": "2016-12-13T07:29:05.937",
        "name": "Example Product 0",
        "noCustoms": null,
        "price": 11.99,
        "productCategory": null,
        "productId": 987654321,
        "productType": null,
        "sku": "987654321",
        "tags": null,
        "warehouseLocation": null,
        "weightOz": 3.0,
        "width": null
    },
    {
        "active": true,
        "aliases": null,
        "createDate": "2015-08-13T14:30:31.007",
        "customsCountryCode": null,
        "customsDescription": null,
        "customsTariffNo": null,
        "customsValue": null,
        "defaultCarrierCode": null,
        "defaultConfirmation": null,
        "defaultCost": null,
        "defaultIntlCarrierCode": null,
        "defaultIntlConfirmation": null,
        "defaultIntlPackageCode": null,
        "defaultIntlServiceCode": null,
        "defaultPackageCode": null,
        "defaultServiceCode": null,
        "fulfillmentSku": "987654322",
        "height": null,
        "internalNotes": "0468437",
        "length": null,
        "modifyDate": "2015-10-01T07:06:53.82",
        "name": "Example Product 1",
        "noCustoms": null,
        "price": 11.99,
        "productCategory": null,
        "productId": 18139199,
        "productType": null,
        "sku": "987654322",
        "tags": null,
        "warehouseLocation": null,
        "weightOz": 3.0,
        "width": null
    },
    {
        "active": true,
        "aliases": null,
        "createDate": "2015-08-13T14:30:31.007",
        "customsCountryCode": null,
        "customsDescription": null,
        "customsTariffNo": null,
        "customsValue": null,
        "defaultCarrierCode": null,
        "defaultConfirmation": null,
        "defaultCost": null,
        "defaultIntlCarrierCode": null,
        "defaultIntlConfirmation": null,
        "defaultIntlPackageCode": null,
        "defaultIntlServiceCode": null,
        "defaultPackageCode": null,
        "defaultServiceCode": null,
        "fulfillmentSku": "987654323",
        "height": null,
        "internalNotes": "0468437",
        "length": null,
        "modifyDate": "2015-10-01T07:06:53.82",
        "name": "Example Product 1",
        "noCustoms": null,
        "price": 11.99,
        "productCategory": null,
        "productId": 18139199,
        "productType": null,
        "sku": "987654323",
        "tags": null,
        "warehouseLocation": null,
        "weightOz": 3.0,
        "width": null
    }
    ],
    "total": 8
}
"""

test_list_products_second = """
{
    "page": 2,
    "pages": 3,
    "products": [{
        "active": true,
        "aliases": null,
        "createDate": "2015-08-13T14:30:31.007",
        "customsCountryCode": null,
        "customsDescription": null,
        "customsTariffNo": null,
        "customsValue": null,
        "defaultCarrierCode": null,
        "defaultConfirmation": null,
        "defaultCost": null,
        "defaultIntlCarrierCode": null,
        "defaultIntlConfirmation": null,
        "defaultIntlPackageCode": null,
        "defaultIntlServiceCode": null,
        "defaultPackageCode": null,
        "defaultServiceCode": null,
        "fulfillmentSku": "987654324",
        "height": null,
        "internalNotes": null,
        "length": null,
        "modifyDate": "2016-12-13T07:29:05.937",
        "name": "Example Product 0",
        "noCustoms": null,
        "price": 11.99,
        "productCategory": null,
        "productId": 987654321,
        "productType": null,
        "sku": "987654324",
        "tags": null,
        "warehouseLocation": null,
        "weightOz": 3.0,
        "width": null
    },
    {
        "active": true,
        "aliases": null,
        "createDate": "2015-08-13T14:30:31.007",
        "customsCountryCode": null,
        "customsDescription": null,
        "customsTariffNo": null,
        "customsValue": null,
        "defaultCarrierCode": null,
        "defaultConfirmation": null,
        "defaultCost": null,
        "defaultIntlCarrierCode": null,
        "defaultIntlConfirmation": null,
        "defaultIntlPackageCode": null,
        "defaultIntlServiceCode": null,
        "defaultPackageCode": null,
        "defaultServiceCode": null,
        "fulfillmentSku": "987654325",
        "height": null,
        "internalNotes": "0468437",
        "length": null,
        "modifyDate": "2015-10-01T07:06:53.82",
        "name": "Example Product 1",
        "noCustoms": null,
        "price": 11.99,
        "productCategory": null,
        "productId": 18139199,
        "productType": null,
        "sku": "987654325",
        "tags": null,
        "warehouseLocation": null,
        "weightOz": 3.0,
        "width": null
    },
    {
        "active": true,
        "aliases": null,
        "createDate": "2015-08-13T14:30:31.007",
        "customsCountryCode": null,
        "customsDescription": null,
        "customsTariffNo": null,
        "customsValue": null,
        "defaultCarrierCode": null,
        "defaultConfirmation": null,
        "defaultCost": null,
        "defaultIntlCarrierCode": null,
        "defaultIntlConfirmation": null,
        "defaultIntlPackageCode": null,
        "defaultIntlServiceCode": null,
        "defaultPackageCode": null,
        "defaultServiceCode": null,
        "fulfillmentSku": "987654326",
        "height": null,
        "internalNotes": "0468437",
        "length": null,
        "modifyDate": "2015-10-01T07:06:53.82",
        "name": "Example Product 1",
        "noCustoms": null,
        "price": 11.99,
        "productCategory": null,
        "productId": 18139199,
        "productType": null,
        "sku": "987654326",
        "tags": null,
        "warehouseLocation": null,
        "weightOz": 3.0,
        "width": null
    }
    ],
    "total": 8
}
"""

test_list_products_third = """
{
    "page": 3,
    "pages": 3,
    "products": [{
        "active": true,
        "aliases": null,
        "createDate": "2015-08-13T14:30:31.007",
        "customsCountryCode": null,
        "customsDescription": null,
        "customsTariffNo": null,
        "customsValue": null,
        "defaultCarrierCode": null,
        "defaultConfirmation": null,
        "defaultCost": null,
        "defaultIntlCarrierCode": null,
        "defaultIntlConfirmation": null,
        "defaultIntlPackageCode": null,
        "defaultIntlServiceCode": null,
        "defaultPackageCode": null,
        "defaultServiceCode": null,
        "fulfillmentSku": "987654327",
        "height": null,
        "internalNotes": null,
        "length": null,
        "modifyDate": "2016-12-13T07:29:05.937",
        "name": "Example Product 0",
        "noCustoms": null,
        "price": 11.99,
        "productCategory": null,
        "productId": 987654321,
        "productType": null,
        "sku": "987654327",
        "tags": null,
        "warehouseLocation": null,
        "weightOz": 3.0,
        "width": null
    },
    {
        "active": true,
        "aliases": null,
        "createDate": "2015-08-13T14:30:31.007",
        "customsCountryCode": null,
        "customsDescription": null,
        "customsTariffNo": null,
        "customsValue": null,
        "defaultCarrierCode": null,
        "defaultConfirmation": null,
        "defaultCost": null,
        "defaultIntlCarrierCode": null,
        "defaultIntlConfirmation": null,
        "defaultIntlPackageCode": null,
        "defaultIntlServiceCode": null,
        "defaultPackageCode": null,
        "defaultServiceCode": null,
        "fulfillmentSku": "987654328",
        "height": null,
        "internalNotes": "0468437",
        "length": null,
        "modifyDate": "2015-10-01T07:06:53.82",
        "name": "Example Product 1",
        "noCustoms": null,
        "price": 11.99,
        "productCategory": null,
        "productId": 18139199,
        "productType": null,
        "sku": "987654328",
        "tags": null,
        "warehouseLocation": null,
        "weightOz": 3.0,
        "width": null
    }
    ],
    "total": 8
}
"""
