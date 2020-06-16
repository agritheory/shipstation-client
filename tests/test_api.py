import json
import os

import pytest
from dotenv import load_dotenv

from shipstation.api import ShipStation
from shipstation.models import *

load_dotenv()
SHIPSTATION_KEY = os.getenv("SHIPSTATION_KEY")
SHIPSTATION_SECRET = os.getenv("SHIPSTATION_SECRET")
ss = ShipStation(SHIPSTATION_KEY, SHIPSTATION_SECRET, debug=True, timeout=5)


def test_label():
    order = ss.get_order(481287142)
    order.weight = ShipStationWeight(units="ounces", value=64)
    order.carrier_code = "fedex"
    order.service_code = "fedex_ground"
    order.package_code = "package"
    return ss.create_label_for_order(order, True, True)


def test_webooks():
    subscribe_to_webhook_options = {
        "target_url": "http://someexamplewebhookurl.com/neworder",
        "event": "ORDER_NOTIFY",
        "friendly_name": "pyshipstation test",
    }
    subscribed_to_webhook = ss.subscribe_to_webhook(subscribe_to_webhook_options)
    assert subscribed_to_webhook.status_code == 201
    webhook_id = subscribed_to_webhook.json()["id"]
    _list_webhooks_(webhook_id, found=True)
    ss.unsubscribe_to_webhook(webhook_id)
    _list_webhooks_(webhook_id, found=False)


def _list_webhooks_(webhook_id=None, found=True):
    webhook_list = ss.list_webhooks()
    if found is False:
        with pytest.raises("KeyError"):
            webhook_list.json()["webhooks"]
    webhooks_list = webhook_list.json()["webhooks"]
    for webhook in webhooks_list:
        if webhook["WebHookID"] == webhook_id:
            assert webhook["WebHookID"] == webhook_id
    else:
        with pytest.raises("KeyError"):
            webhook["WebHookID"]


def test_stores():
    marketplaces = ss.list_marketplaces()
    assert marketplaces.status_code == 200
    stores = ss.list_stores().json()
    assert len(stores) >= 1
    store_id = stores[-1].get("storeId")
    specific_store = ss.get_store(store_id)
    assert specific_store.status_code == 200
    r = ss.deactivate_store(store_id)
    assert r.status_code == 200
    r = ss.reactivate_store(store_id)
    assert r.status_code == 200


def test_warehouses():
    warehouses = ss.list_warehouses()
    assert warehouses.status_code == 200
    warehouses_id = warehouses.json()[0].get("warehouseId")
    warehouse = ss.get_warehouse(warehouse_id)
    assert warehouse.status_code == 200
    new_warehouse = {
        "warehouse_name": "New Ship From Location",
        "origin_address": get_warehouse_address(),
        "return_address": get_warehouse_address(),
        "is_default": "false",
    }
    r = ss.create_warehouse(new_warehouse)
    assert warehouse.status_code == 200
    new_warehouse_id = r.json().get("warehouseId")

    # new_warehouse = ss.get_warehouse(new_warehouse_id).json()
    new_warehouse = ss.get_warehouse("2126606").json()
    new_warehouse.warehouse_name = "Updated New Ship From Location"
    ss.update_warehouse(new_warehouse)
    # ss.delete_warehouse()

    {
        "warehouseId": 12345,
        "warehouseName": "API Ship From Location",
        "originAddress": {
            "name": "API Warehouse",
            "company": "ShipStation",
            "street1": "2815 Exposition Blvd",
            "street2": null,
            "street3": null,
            "city": "Austin",
            "state": "TX",
            "postalCode": "78703",
            "country": "US",
            "phone": "512-555-5555",
            "residential": true,
            "addressVerified": null,
        },
        "returnAddress": {
            "name": "API Ship From Location",
            "company": "ShipStation",
            "street1": "2815 Exposition Blvd",
            "street2": null,
            "street3": null,
            "city": "Austin",
            "state": "TX",
            "postalCode": "78703",
            "country": "US",
            "phone": "512-555-5555",
            "residential": null,
            "addressVerified": null,
        },
        "createDate": "2015-07-02T08:38:31.4870000",
        "isDefault": true,
    }


def get_warehouse_address():
    return ShipStationAddress(
        name="NM Warehouse",
        company="White Sands Co.",
        street1="4704 Arabela Dr.",
        city="Las Cruces",
        state="NM",
        postal_code="80012",
        country="US",
        phone="512-111-2222",
        residential="true",
    )


def test_users():
    r = ss.list_users()
    assert r.status_code == 200


def test_carriers():
    r = ss.list_carriers()
    assert r.status_code == 200
    carrier_code = r.json()[0].get("code")
    r = ss.get_carrier(carrier_code)
    assert r.status_code == 200
    r = ss.list_packages(carrier_code)
    assert r.status_code == 200
    r = ss.list_services(carrier_code)
    assert r.status_code == 200


def test_customers():
    r = ss.list_customers()
    assert r.status_code == 200
    customer_id = r.json()["customers"][0].get("customerId")
    r = ss.get_customer(customer_id)
    assert r.status_code == 200


def test_shipments_and_fulfillments():
    r = ss.get_rates(carrier_code)
    assert r.status_code == 200
    r = ss.list_fulfillments()
    assert r.status_code == 200
    r = ss.list_shipments()
    assert r.status_code == 200


def test_label_creation():
    pass
