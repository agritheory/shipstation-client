import datetime
import json
import os
from decimal import Decimal
from uuid import UUID

import httpx
import pytest
import respx

from conftest import *
from shipstation.api import ShipStation
from shipstation.models import *
from shipstation.pagination import Page


@respx.mock
def test_get_carrier(ss: ShipStation, mocked_api: respx.MockTransport) -> None:
    request = mocked_api["get_carrier"]
    response = ss.get_carrier("stamps_com")
    assert request.called
    assert isinstance(response, ShipStationCarrier)
    assert isinstance(response.primary, bool)
    assert response.name == "Stamps.com"
    assert response.account_number == "example"


@respx.mock
def test_get_customer(ss: ShipStation, mocked_api: respx.MockTransport) -> None:
    request = mocked_api["get_customer"]
    response = ss.get_customer(123456789)
    assert request.called
    assert isinstance(response, ShipStationCustomer)
    assert isinstance(response.address_verified, bool)
    assert response.address_verified is True
    assert response.create_date == datetime.datetime(2017, 12, 16, 18, 49, 16, 7000)
    assert response.marketplace_usernames[0].customer_id == 123456789


@respx.mock
def test_get_order(ss: ShipStation, mocked_api: respx.MockTransport) -> None:
    request = mocked_api["get_order"]
    response = ss.get_order(123456789)
    assert request.called
    assert isinstance(response, ShipStationOrder)
    assert isinstance(response.ship_to, ShipStationAddress)
    assert isinstance(response.advanced_options, ShipStationAdvancedOptions)
    assert isinstance(response.international_options, ShipStationInternationalOptions)
    assert isinstance(response.insurance_options, ShipStationInsuranceOptions)
    assert response.create_date == datetime.datetime(2015, 6, 30, 15, 20, 26, 723000)


@respx.mock
def test_get_product(ss: ShipStation, mocked_api: respx.MockTransport) -> None:
    request = mocked_api["get_product"]
    response = ss.get_product(123456789)
    assert request.called
    assert isinstance(response, ShipStationItem)
    assert response.create_date == datetime.datetime(2016, 10, 31, 7, 43, 0, 203000)


@respx.mock
def test_get_rates(ss: ShipStation, mocked_api: respx.MockTransport) -> None:
    request = mocked_api["get_rates"]
    response = ss.get_rates(
        ShipStationRateOptions(
            carrier_code="stamps_com",
            from_postal_code="20500",
            to_postal_code="20500",
            to_country="US",
            weight=ShipStationWeight(units="ounces", value=12),
        )
    )
    assert request.called
    assert isinstance(response[0], ShipStationRate)
    assert response[0].service_code == "usps_first_class_mail"
    assert response[0].shipment_cost == Decimal("3.2")


@respx.mock
def test_get_stores(ss: ShipStation, mocked_api: respx.MockTransport) -> None:
    request = mocked_api["get_store"]
    response = ss.get_store(12345)
    assert request.called
    assert isinstance(response, ShipStationStore)
    assert response.store_name == "US Amazon Store"
    assert response.account_name == "GHI123456789"


@respx.mock
def test_get_warehouse(ss: ShipStation, mocked_api: respx.MockTransport) -> None:
    request = mocked_api["get_warehouse"]
    response = ss.get_warehouse(456789)
    assert request.called
    assert isinstance(response, ShipStationWarehouse)
    assert isinstance(response.return_address, ShipStationAddress)
    assert response.warehouse_name == "Test Company"


@respx.mock
def test_list_carriers(ss: ShipStation, mocked_api: respx.MockTransport) -> None:
    request = mocked_api["list_carriers"]
    response = ss.list_carriers()
    assert request.called
    assert isinstance(response[0], ShipStationCarrier)
    assert response[0].code == "stamps_com"
    assert response[0].balance == Decimal("15.01")


@respx.mock
def test_list_tags(ss: ShipStation, mocked_api: respx.MockTransport) -> None:
    request = mocked_api["list_tags"]
    response = ss.list_tags()
    assert request.called
    assert isinstance(response[0], ShipStationOrderTag)
    assert response[0].tag_id == 12345
    assert response[0].name == "Amazon Prime Order"


@respx.mock
def test_list_marketplaces(ss: ShipStation, mocked_api: respx.MockTransport) -> None:
    request = mocked_api["list_marketplaces"]
    response = ss.list_marketplaces()
    assert request.called
    assert isinstance(response[0], ShipStationMarketplace)
    assert response[0].name == "3dcart"
    assert response[1].name == "Acumatica"


@respx.mock
def test_list_orders(ss: ShipStation, mocked_api: respx.MockTransport) -> None:
    request = mocked_api["list_orders"]
    response = ss.list_orders()
    assert request.called
    # for order in response:
    print("items", response[0].items)
    assert isinstance(response[0], ShipStationOrder)
    assert isinstance(response[0].ship_to, ShipStationAddress)
    # assert isinstance(response[0].items[0], ShipStationOrderItem)
    assert isinstance(response[0].advanced_options, ShipStationAdvancedOptions)
    assert isinstance(response[0].weight, ShipStationWeight)
    assert isinstance(
        response[1].international_options, ShipStationInternationalOptions
    )
    assert isinstance(
        response[1].international_options.customs_items[0], ShipStationCustomsItem
    )
    assert response[1].create_date == datetime.datetime(2015, 6, 30, 15, 20, 26, 723000)
    assert response[1].shipping_amount == Decimal("0.0")


@respx.mock
def test_list_stores(ss: ShipStation, mocked_api: respx.MockTransport) -> None:
    request = mocked_api["list_stores"]
    response = ss.list_stores(marketplace_id=2)
    assert request.called
    assert isinstance(response[0], ShipStationStore)
    assert response[0].store_name == "Mexico Amazon Store"
    assert response[1].account_name == "DEF123456789"


@respx.mock
def test_list_users(ss: ShipStation, mocked_api: respx.MockTransport) -> None:
    request = mocked_api["list_users"]
    response = ss.list_users()
    assert request.called
    assert isinstance(response[0], ShipStationUser)
    assert response[0].name == "Merchandising"
    assert isinstance(response[1].user_id, UUID)
    assert response[1].user_id == UUID("0dbc3f54-5cd4-4054-b2b5-92427e18d6cd")


@respx.mock
def test_list_warehouses(ss: ShipStation, mocked_api: respx.MockTransport) -> None:
    request = mocked_api["list_warehouses"]
    response = ss.list_warehouses()
    assert request.called
    assert isinstance(response[0], ShipStationWarehouse)
    assert isinstance(response[0].origin_address, ShipStationAddress)
    assert response[0].origin_address.name == "Warehouse 1"
    assert response[0].warehouse_id == "456789"
    assert response[0].origin_address.street2 == "Unit 4"


@pytest.mark.skip
@respx.mock
def test_list_webhooks(ss: ShipStation, mocked_api: respx.MockTransport) -> None:
    request = mocked_api["list_webhooks"]
    response = ss.list_webhooks()
    assert request.called
    # assert isinstance(response[0], ShipStationWarehouse)
    # assert isinstance(response[0].origin_address, ShipStationAddress)
    # assert response[0].origin_address.name == "Warehouse 1"
    # assert response[0].warehouse_id == '456789'
    # assert response[0].origin_address.street2 == "Unit 4"


@respx.mock
def test_list_services(ss: ShipStation, mocked_api: respx.MockTransport) -> None:
    request = mocked_api["list_services"]
    response = ss.list_services(carrier_code="stamps_com")
    assert request.called
    assert isinstance(response[0], ShipStationCarrierService)
    assert response[1].international is False


@respx.mock
def test_list_shipments(ss: ShipStation, mocked_api: respx.MockTransport) -> None:
    request = mocked_api["list_shipments"]
    response = ss.list_shipments()
    assert request.called
    assert isinstance(response, Page)
    assert isinstance(response[0], ShipStationOrder)
    assert isinstance(response[0].ship_to, ShipStationAddress)
    assert isinstance(response[0].advanced_options, ShipStationAdvancedOptions)
    assert isinstance(response[0].weight, ShipStationWeight)
    assert response[0].create_date == datetime.datetime(2015, 6, 29, 14, 29, 28, 583000)
    assert response[0].shipment_cost == Decimal("2.35")
    assert response[0].tracking_number == "9400111899562764298812"


@respx.mock
def test_list_shipments_error(ss: ShipStation, mocked_api: respx.MockTransport) -> None:
    request = mocked_api["list_shipments_error"]
    with pytest.raises(httpx.HTTPStatusError):
        ss.list_shipments()


@respx.mock
def test_list_packages(ss: ShipStation, mocked_api: respx.MockTransport) -> None:
    request = mocked_api["list_packages"]
    response = ss.list_packages(carrier_code="stamps_com")
    assert request.called
    assert isinstance(response[0], ShipStationCarrierPackage)
    assert isinstance(response[0].domestic, bool)
    assert response[1].domestic is True
    assert response[1].code == "flat_rate_envelope"


@respx.mock
def test_list_customers(ss: ShipStation, mocked_api: respx.MockTransport) -> None:
    request = mocked_api["list_customers"]
    response = ss.list_customers()
    assert request.called
    assert isinstance(response[0], ShipStationCustomer)
    assert isinstance(response[0].address_verified, bool)
    assert response[0].address_verified is True
    assert response[0].create_date == datetime.datetime(2017, 12, 16, 18, 49, 16, 7000)
    assert response[0].marketplace_usernames[0].customer_id == 123456789


@respx.mock
def test_list_fulfillments(ss: ShipStation, mocked_api: respx.MockTransport) -> None:
    request = mocked_api["list_fulfillments"]
    response = ss.list_fulfillments()
    assert request.called
    assert isinstance(response[0], ShipStationFulfillment)
    assert isinstance(response[0].ship_to, ShipStationAddress)
    assert isinstance(response[0].user_id, UUID)
    assert response[0].create_date == datetime.datetime(2020, 6, 19, 7, 21, 51, 773000)
    assert response[1].notify_error_message is not None


"""
test_list_products is tested in test_pagination.py
"""


# def test_label():
#     order = ss.get_order(481287142)
#     order.weight = ShipStationWeight(units="ounces", value=64)
#     order.carrier_code = "fedex"
#     order.service_code = "fedex_ground"
#     order.package_code = "package"
#     return ss.create_label_for_order(order, True, True)
#
#
# def test_webooks():
#     subscribe_to_webhook_options = {
#         "target_url": "http://someexamplewebhookurl.com/neworder",
#         "event": "ORDER_NOTIFY",
#         "friendly_name": "pyshipstation test",
#     }
#     subscribed_to_webhook = ss.subscribe_to_webhook(subscribe_to_webhook_options)
#     assert subscribed_to_webhook.status_code == 201
#     webhook_id = subscribed_to_webhook.json()["id"]
#     _list_webhooks_(webhook_id, found=True)
#     ss.unsubscribe_to_webhook(webhook_id)
#     _list_webhooks_(webhook_id, found=False)
#
#
# def _list_webhooks_(webhook_id=None, found=True):
#     webhook_list = ss.list_webhooks()
#     if found is False:
#         with pytest.raises("KeyError"):
#             webhook_list.json()["webhooks"]
#     webhooks_list = webhook_list.json()["webhooks"]
#     for webhook in webhooks_list:
#         if webhook["WebHookID"] == webhook_id:
#             assert webhook["WebHookID"] == webhook_id
#     else:
#         with pytest.raises("KeyError"):
#             webhook["WebHookID"]
#
#
# def test_stores():
#     marketplaces = ss.list_marketplaces()
#     assert marketplaces.status_code == 200
#     stores = ss.list_stores().json()
#     assert len(stores) >= 1
#     store_id = stores[-1].get("storeId")
#     specific_store = ss.get_store(store_id)
#     assert specific_store.status_code == 200
#     r = ss.deactivate_store(store_id)
#     assert r.status_code == 200
#     r = ss.reactivate_store(store_id)
#     assert r.status_code == 200
#
#
# def test_warehouses():
#     warehouses = ss.list_warehouses()
#     assert warehouses.status_code == 200
#     warehouses_id = warehouses.json()[0].get("warehouseId")
#     warehouse = ss.get_warehouse(warehouse_id)
#     assert warehouse.status_code == 200
#     new_warehouse = {
#         "warehouse_name": "New Ship From Location",
#         "origin_address": get_warehouse_address(),
#         "return_address": get_warehouse_address(),
#         "is_default": "false",
#     }
#     r = ss.create_warehouse(new_warehouse)
#     assert warehouse.status_code == 200
#     new_warehouse_id = r.json().get("warehouseId")
#
#     # new_warehouse = ss.get_warehouse(new_warehouse_id).json()
#     new_warehouse = ss.get_warehouse("2126606").json()
#     new_warehouse.warehouse_name = "Updated New Ship From Location"
#     ss.update_warehouse(new_warehouse)
#     # ss.delete_warehouse()
#
#     {
#         "warehouseId": 12345,
#         "warehouseName": "API Ship From Location",
#         "originAddress": {
#             "name": "API Warehouse",
#             "company": "ShipStation",
#             "street1": "2815 Exposition Blvd",
#             "street2": null,
#             "street3": null,
#             "city": "Austin",
#             "state": "TX",
#             "postalCode": "78703",
#             "country": "US",
#             "phone": "512-555-5555",
#             "residential": true,
#             "addressVerified": null,
#         },
#         "returnAddress": {
#             "name": "API Ship From Location",
#             "company": "ShipStation",
#             "street1": "2815 Exposition Blvd",
#             "street2": null,
#             "street3": null,
#             "city": "Austin",
#             "state": "TX",
#             "postalCode": "78703",
#             "country": "US",
#             "phone": "512-555-5555",
#             "residential": null,
#             "addressVerified": null,
#         },
#         "createDate": "2015-07-02T08:38:31.4870000",
#         "isDefault": true,
#     }
#
#
# def get_warehouse_address():
#     return ShipStationAddress(
#         name="NM Warehouse",
#         company="White Sands Co.",
#         street1="4704 Arabela Dr.",
#         city="Las Cruces",
#         state="NM",
#         postal_code="80012",
#         country="US",
#         phone="512-111-2222",
#         residential="true",
#     )
#
#
# def test_customers():
#     r = ss.list_customers()
#     assert r.status_code == 200
#     customer_id = r.json()["customers"][0].get("customerId")
#     r = ss.get_customer(customer_id)
#     assert r.status_code == 200
#
#
# def test_shipments_and_fulfillments():
#     r = ss.get_rates(carrier_code)
#     assert r.status_code == 200
#     r = ss.list_fulfillments()
#     assert r.status_code == 200
#     r = ss.list_shipments()
#     assert r.status_code == 200
#
#
# def test_label_creation():
#     pass
