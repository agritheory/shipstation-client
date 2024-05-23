from decimal import Decimal

import pytest
from respx import MockRouter, mock
from shipstation.api import ShipStation
from shipstation.models import *
from shipstation.pagination import Page


@pytest.fixture(scope="session")
def mocked_pagination():
    with mock(
        base_url="https://ssapi.shipstation.com", assert_all_called=False
    ) as respx_mock:
        respx_mock.get(
            "/products",
        ).respond(200, json=TEST_LIST_PRODUCTS_FIRST)
        respx_mock.get(
            "/products?page=2",
        ).respond(200, json=TEST_LIST_PRODUCTS_SECOND)
        respx_mock.get(
            "/products?page=3",
        ).respond(200, json=TEST_LIST_PRODUCTS_THIRD)
        respx_mock.get("/products", name="list_products_none").respond(
            200, json=LIST_PRODUCTS_NONE
        )
        respx_mock.get("/products?pageSize=3", name="list_products_params_1").respond(
            200, json=TEST_LIST_PRODUCTS_FIRST
        )
        respx_mock.get(
            "/products?pageSize=3&page=2",
        ).respond(200, json=TEST_LIST_PRODUCTS_SECOND)
        respx_mock.get(
            "/products?pageSize=3&page=3",
        ).respond(200, json=TEST_LIST_PRODUCTS_THIRD)
        yield respx_mock


@mock
def test_no_results(ss: ShipStation, mocked_pagination: MockRouter) -> None:
    request = mocked_pagination["list_products_none"]
    response = ss.list_products()
    assert isinstance(response, Page)
    for index, product in enumerate(response):
        assert True


@mock
def test_list_products(ss: ShipStation, mocked_pagination: MockRouter) -> None:
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


@mock
def test_list_products_ensure_params(
    ss: ShipStation, mocked_pagination: MockRouter
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


LIST_PRODUCTS_NONE = {"page": 1, "pages": 1, "products": [], "total": 1}

TEST_LIST_PRODUCTS_FIRST = {
    "page": 1,
    "pages": 3,
    "products": [
        {
            "active": True,
            "aliases": None,
            "createDate": "2015-08-13T14:30:31.007",
            "customsCountryCode": None,
            "customsDescription": None,
            "customsTariffNo": None,
            "customsValue": None,
            "defaultCarrierCode": None,
            "defaultConfirmation": None,
            "defaultCost": None,
            "defaultIntlCarrierCode": None,
            "defaultIntlConfirmation": None,
            "defaultIntlPackageCode": None,
            "defaultIntlServiceCode": None,
            "defaultPackageCode": None,
            "defaultServiceCode": None,
            "fulfillmentSku": "712392290692",
            "height": None,
            "internalNotes": None,
            "length": None,
            "modifyDate": "2016-12-13T07:29:05.937",
            "name": "Example Product 0",
            "noCustoms": None,
            "price": 11.99,
            "productCategory": None,
            "productId": 987654321,
            "productType": None,
            "sku": "987654321",
            "tags": None,
            "warehouseLocation": None,
            "weightOz": 3.0,
            "width": None,
        },
        {
            "active": True,
            "aliases": None,
            "createDate": "2015-08-13T14:30:31.007",
            "customsCountryCode": None,
            "customsDescription": None,
            "customsTariffNo": None,
            "customsValue": None,
            "defaultCarrierCode": None,
            "defaultConfirmation": None,
            "defaultCost": None,
            "defaultIntlCarrierCode": None,
            "defaultIntlConfirmation": None,
            "defaultIntlPackageCode": None,
            "defaultIntlServiceCode": None,
            "defaultPackageCode": None,
            "defaultServiceCode": None,
            "fulfillmentSku": "987654322",
            "height": None,
            "internalNotes": "0468437",
            "length": None,
            "modifyDate": "2015-10-01T07:06:53.82",
            "name": "Example Product 1",
            "noCustoms": None,
            "price": 11.99,
            "productCategory": None,
            "productId": 18139199,
            "productType": None,
            "sku": "987654322",
            "tags": None,
            "warehouseLocation": None,
            "weightOz": 3.0,
            "width": None,
        },
        {
            "active": True,
            "aliases": None,
            "createDate": "2015-08-13T14:30:31.007",
            "customsCountryCode": None,
            "customsDescription": None,
            "customsTariffNo": None,
            "customsValue": None,
            "defaultCarrierCode": None,
            "defaultConfirmation": None,
            "defaultCost": None,
            "defaultIntlCarrierCode": None,
            "defaultIntlConfirmation": None,
            "defaultIntlPackageCode": None,
            "defaultIntlServiceCode": None,
            "defaultPackageCode": None,
            "defaultServiceCode": None,
            "fulfillmentSku": "987654323",
            "height": None,
            "internalNotes": "0468437",
            "length": None,
            "modifyDate": "2015-10-01T07:06:53.82",
            "name": "Example Product 1",
            "noCustoms": None,
            "price": 11.99,
            "productCategory": None,
            "productId": 18139199,
            "productType": None,
            "sku": "987654323",
            "tags": None,
            "warehouseLocation": None,
            "weightOz": 3.0,
            "width": None,
        },
    ],
    "total": 8,
}

TEST_LIST_PRODUCTS_SECOND = {
    "page": 2,
    "pages": 3,
    "products": [
        {
            "active": True,
            "aliases": None,
            "createDate": "2015-08-13T14:30:31.007",
            "customsCountryCode": None,
            "customsDescription": None,
            "customsTariffNo": None,
            "customsValue": None,
            "defaultCarrierCode": None,
            "defaultConfirmation": None,
            "defaultCost": None,
            "defaultIntlCarrierCode": None,
            "defaultIntlConfirmation": None,
            "defaultIntlPackageCode": None,
            "defaultIntlServiceCode": None,
            "defaultPackageCode": None,
            "defaultServiceCode": None,
            "fulfillmentSku": "987654324",
            "height": None,
            "internalNotes": None,
            "length": None,
            "modifyDate": "2016-12-13T07:29:05.937",
            "name": "Example Product 0",
            "noCustoms": None,
            "price": 11.99,
            "productCategory": None,
            "productId": 987654321,
            "productType": None,
            "sku": "987654324",
            "tags": None,
            "warehouseLocation": None,
            "weightOz": 3.0,
            "width": None,
        },
        {
            "active": True,
            "aliases": None,
            "createDate": "2015-08-13T14:30:31.007",
            "customsCountryCode": None,
            "customsDescription": None,
            "customsTariffNo": None,
            "customsValue": None,
            "defaultCarrierCode": None,
            "defaultConfirmation": None,
            "defaultCost": None,
            "defaultIntlCarrierCode": None,
            "defaultIntlConfirmation": None,
            "defaultIntlPackageCode": None,
            "defaultIntlServiceCode": None,
            "defaultPackageCode": None,
            "defaultServiceCode": None,
            "fulfillmentSku": "987654325",
            "height": None,
            "internalNotes": "0468437",
            "length": None,
            "modifyDate": "2015-10-01T07:06:53.82",
            "name": "Example Product 1",
            "noCustoms": None,
            "price": 11.99,
            "productCategory": None,
            "productId": 18139199,
            "productType": None,
            "sku": "987654325",
            "tags": None,
            "warehouseLocation": None,
            "weightOz": 3.0,
            "width": None,
        },
        {
            "active": True,
            "aliases": None,
            "createDate": "2015-08-13T14:30:31.007",
            "customsCountryCode": None,
            "customsDescription": None,
            "customsTariffNo": None,
            "customsValue": None,
            "defaultCarrierCode": None,
            "defaultConfirmation": None,
            "defaultCost": None,
            "defaultIntlCarrierCode": None,
            "defaultIntlConfirmation": None,
            "defaultIntlPackageCode": None,
            "defaultIntlServiceCode": None,
            "defaultPackageCode": None,
            "defaultServiceCode": None,
            "fulfillmentSku": "987654326",
            "height": None,
            "internalNotes": "0468437",
            "length": None,
            "modifyDate": "2015-10-01T07:06:53.82",
            "name": "Example Product 1",
            "noCustoms": None,
            "price": 11.99,
            "productCategory": None,
            "productId": 18139199,
            "productType": None,
            "sku": "987654326",
            "tags": None,
            "warehouseLocation": None,
            "weightOz": 3.0,
            "width": None,
        },
    ],
    "total": 8,
}

TEST_LIST_PRODUCTS_THIRD = {
    "page": 3,
    "pages": 3,
    "products": [
        {
            "active": True,
            "aliases": None,
            "createDate": "2015-08-13T14:30:31.007",
            "customsCountryCode": None,
            "customsDescription": None,
            "customsTariffNo": None,
            "customsValue": None,
            "defaultCarrierCode": None,
            "defaultConfirmation": None,
            "defaultCost": None,
            "defaultIntlCarrierCode": None,
            "defaultIntlConfirmation": None,
            "defaultIntlPackageCode": None,
            "defaultIntlServiceCode": None,
            "defaultPackageCode": None,
            "defaultServiceCode": None,
            "fulfillmentSku": "987654327",
            "height": None,
            "internalNotes": None,
            "length": None,
            "modifyDate": "2016-12-13T07:29:05.937",
            "name": "Example Product 0",
            "noCustoms": None,
            "price": 11.99,
            "productCategory": None,
            "productId": 987654321,
            "productType": None,
            "sku": "987654327",
            "tags": None,
            "warehouseLocation": None,
            "weightOz": 3.0,
            "width": None,
        },
        {
            "active": True,
            "aliases": None,
            "createDate": "2015-08-13T14:30:31.007",
            "customsCountryCode": None,
            "customsDescription": None,
            "customsTariffNo": None,
            "customsValue": None,
            "defaultCarrierCode": None,
            "defaultConfirmation": None,
            "defaultCost": None,
            "defaultIntlCarrierCode": None,
            "defaultIntlConfirmation": None,
            "defaultIntlPackageCode": None,
            "defaultIntlServiceCode": None,
            "defaultPackageCode": None,
            "defaultServiceCode": None,
            "fulfillmentSku": "987654328",
            "height": None,
            "internalNotes": "0468437",
            "length": None,
            "modifyDate": "2015-10-01T07:06:53.82",
            "name": "Example Product 1",
            "noCustoms": None,
            "price": 11.99,
            "productCategory": None,
            "productId": 18139199,
            "productType": None,
            "sku": "987654328",
            "tags": None,
            "warehouseLocation": None,
            "weightOz": 3.0,
            "width": None,
        },
    ],
    "total": 8,
}
