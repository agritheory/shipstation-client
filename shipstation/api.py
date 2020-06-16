import base64
import datetime
import json
import pprint
from decimal import Decimal
from io import BytesIO

import requests

from shipstation.constants import *
from shipstation.http import ShipStationHTTP
from shipstation.models import *


class ShipStation(ShipStationHTTP):
    """
    Handles the details of connecting to and querying a ShipStation account.
    """

    def __init__(self, key=None, secret=None, debug=False, timeout=1):
        if key is None:
            raise AttributeError("Key must be supplied.")
        if secret is None:
            raise AttributeError("Secret must be supplied.")

        self.url = "https://ssapi.shipstation.com"

        self.key = key
        self.secret = secret
        self.orders = []
        self.timeout = timeout
        self.debug = debug

    def list_tags(self):
        tags = self.get(endpoint="/accounts/listtags")
        return [ShipStationOrderTag().json(tag) for tag in tags.json()]

    def create_orders(self, orders):
        self.require_type(orders, list)
        responses = []
        for order in orders:
            r = self.post(endpoint="/orders/createorder", data=order.json())
            responses.append(ShipStationOrder().json(r.text))
        return responses

    def create_order(self, order):
        self.require_type(order, ShipStationOrder)
        r = self.post(endpoint="/orders/createorder", data=order.json())
        return ShipStationOrder().json(r.text)

    def list_orders(self, parameters={}):
        self.require_type(parameters, dict)
        invalid_keys = set(parameters.keys()).difference(ORDER_LIST_PARAMETERS)
        if invalid_keys:
            raise AttributeError(
                "Invalid order list parameters: {}".format(", ".join(invalid_keys))
            )

        valid_parameters = {
            self.to_camel_case(key): value for key, value in parameters.items()
        }

        return self.get(endpoint="/orders/list", payload=valid_parameters)

    def get_order(self, order_id):
        r = self.get(endpoint="/orders/" + str(order_id))
        print(r.status_code)
        return ShipStationOrder().json(r.text)

    def delete_order(self, order_id):
        msg = self.delete(endpoint="/orders/" + str(order_id))
        return msg.json()

    def add_tag_to_order(self, order_id, tag_id):
        data = json.dumps({"orderId": str(order_id), "tagId": str(tag_id)})
        r = self.post(endpoint="/orders/addtag", data=data)
        return r.json()

    def assign_user_to_order(self, order_id, user_id):
        data = json.dumps({"orderId": str(order_id), "userId": str(user_id)})
        r = self.post(endpoint="/orders/assignuser", data=data)
        return r.json()

    def create_label_for_order(self, order, test_label=False, pdf=False):
        order.test_label = True if test_label else False
        label_data = order.json()
        r = self.post(endpoint="/orders/createlabelfororder", data=label_data)
        if not r.status_code == 200:
            return r
        new_data = self.convert_camel_case(r.json())
        if pdf:
            return BytesIO(base64.b64decode(new_data["label_data"]))
        for key, value in new_data:  # refactor to comprehension
            if value:
                setattr(order, key, value)
        return order

    def hold_order_until(self, order_id, hold_until_date):
        data = json.dumps(
            {"orderId": str(order_id), "holdUntilDate": str(hold_until_date)}
        )
        r = self.post(endpoint="/orders/holduntil", data=data)
        return r.json()

    # not working
    # def list_orders_by_tag(self, order_status=None, tag_id=None, page=None, page_size=None):
    #     orders = self.get(endpoint="/orders/listbytag", payload={
    #         'orderStatus': order_status, 'tagId': tag_id,
    #         'page': page, 'pageSize': page_size
    #     })
    #     print(orders.json())
    #     return [ShipStationOrder().json(order.text) for order in orders.json()]

    def mark_order_as_shipped(
        self,
        order_id,
        carrier_code,
        ship_date=None,
        tracking_number=None,
        notify_customer=False,
        notify_sales_channel=False,
    ):
        data = json.dumps(
            {
                "orderId": str(order_id),
                "carrierCode": str(carrier_code),
                "trackingNumber": str(tracking_number),
                "notifyCustomer": notify_customer,
                "notifySalesChannel": notify_sales_channel,
            }
        )
        r = self.post(endpoint="/orders/markasshipped", data=data)
        return r.json()

    def remove_tag_from_order(self):
        pass

    def restore_order_from_on_hold(self):
        pass

    def unassign_user_from_order(self):
        pass

    def get_product(self, product_id):
        r = self.get(endpoint="/products/" + str(product_id))
        return ShipStationItem().json(r.text)

    def list_products(self):
        r = self.get(endpoint="/products/")
        products = r.json().get("products") if r.status_code == 200 else None
        return [ShipStationItem().json(product) for product in products]

    def update_product(self, product):
        self.require_type(product, ShipStationItem)
        data = product.json()
        msg = self.put(endpoint="/products/" + str(product.product_id), data=data)
        return msg.json()

    def list_carriers(self):
        carriers = self.get(endpoint="/carriers/")
        return [ShipStationCarrier().json(carrier) for carrier in carriers.json()]

    def get_carrier(self, carrier_code):
        carrier = self.get(
            endpoint="/carriers/getcarrier", payload={"carrierCode": carrier_code}
        )
        return ShipStationCarrier(carrier.json())

    def list_packages(self, carrier_code):
        packages = self.get(
            endpoint="/carriers/listpackages", payload={"carrierCode": carrier_code}
        )
        return [
            ShipStationCarrierPackage().json(package) for package in packages.json()
        ]

    def list_services(self, carrier_code):
        services = self.get(
            endpoint="/carriers/listservices", payload={"carrierCode": carrier_code}
        )
        return [
            ShipStationCarrierService().json(service) for service in services.json()
        ]

    def get_customer(self, customer_id):
        customer = self.get(endpoint="/customers/" + str(customer_id))
        return ShipStationCustomer().json(customer.text)

    def list_customers(self, parameters={}):
        valid_parameters = self._validate_parameters(
            parameters, CUSTOMER_LIST_PARAMETERS
        )
        r = self.get(endpoint="/customers", payload=valid_parameters)
        customer_list = r.json().get("customers")
        # handle multiple pages?
        return [ShipStationCustomer().json(customer) for customer in customer_list]

    # TODO: return list of fulfillments as objects
    def list_fulfillments(self, parameters={}):
        valid_parameters = self._validate_parameters(
            parameters, FULFILLMENT_LIST_PARAMETERS
        )
        r = self.get(endpoint="/fulfillments", payload=valid_parameters)
        fulfillments = r.json().get("fulfillments")
        # handle multiple pages?
        return [
            ShipStationFulfillment().json(fulfillment) for fulfillment in fulfillments
        ]

    def list_shipments(self, parameters={}):
        valid_parameters = self._validate_parameters(
            parameters, SHIPMENT_LIST_PARAMETERS
        )
        r = self.get(endpoint="/shipments", payload=valid_parameters)
        shipments = r.json().get("shipments")
        return [ShipStationOrder().json(s) for s in shipments]

    # TODO: return shipment label as objects
    def create_shipment_label(self, order):
        self.require_type(order, ShipStationOrder)
        order.validate()
        return self.post(endpoint="/shipments/createlabel", data=order.json())

    # TODO: return list of rates as objects
    def get_rates(self, options):
        self.require_type(options.get("weight"), ShipStationWeight)
        self.require_type(options.get("dimensions"), ShipStationContainer)
        valid_options = self._validate_parameters(options, GET_RATE_OPTIONS)
        for required_option in REQUIRED_RATE_OPTIONS:
            if not options.get(required_option):
                raise AttributeError(f"'{required_option}' is required to get rates")
        return self.post(endpoint="/shipments/getrates", data=valid_options)

    # TODO: return status code
    def void_label(self, shipment_id):
        return self.post(endpoint="/shipments/voidlabel", data=shipment_id)

    def list_marketplaces(self):
        marketplaces = self.get(endpoint="/stores/marketplaces/")
        return [
            ShipStationMarketplace().json(marketplace)
            for marketplace in marketplaces.json()
        ]

    def list_stores(self, show_inactive=False, marketplace_id=None):
        self.require_type(show_inactive, bool)
        self.require_type(marketplace_id, int)
        parameters = {}
        if show_inactive:
            parameters["showInactive"] = show_inactive
        if marketplace_id:
            parameters["marketplaceId"] = marketplace_id
        stores = self.get(endpoint="/stores", payload=parameters)
        return [ShipStationStore().json(store) for store in stores.json()]

    def get_store(self, store_id):
        store = self.get(endpoint="/stores/" + str(store_id))
        return ShipStationStore().json(store.json())

    def update_store(self, options):
        options = self._validate_parameters(options, UPDATE_STORE_OPTIONS)
        [self.require_attribute(m) for m in UPDATE_STORE_OPTIONS]
        self.require_type(options.get("status_mappings"), list)
        for mapping in status_mappings:
            self.require_type(mapping, ShipStationStatusMapping)
            self.require_membership(mapping["orderStatus"], ORDER_STATUS_VALUES)
        store = self.put(endpoint="/stores/storeId", data=options)
        return ShipStationStore().json(store)

    def deactivate_store(self, store_id):
        store_id = json.dumps({"storeId": str(store_id)})
        store = self.post(endpoint="/stores/deactivate", data=store_id)
        return store.json()

    def reactivate_store(self, store_id):
        store_id = json.dumps({"storeId": str(store_id)})
        store = self.post(endpoint="/stores/reactivate", data=store_id)
        return store.json()

    def list_users(self, show_inactive=False):
        self.require_type(show_inactive, bool)
        show_inactive = json.dumps({"showInactive": show_inactive})
        users = self.get(endpoint="/users/", payload=show_inactive)
        return [ShipStationUser().json(user) for user in users.json()]

    def get_warehouse(self, warehouse_id):
        wh = self.get(endpoint="/warehouses/" + str(warehouse_id))
        return ShipStationWarehouse().json(wh.json())

    def list_warehouses(self):
        warehouses = self.get(endpoint="/warehouses")
        return [ShipStationWarehouse().json(wh) for wh in warehouses.json()]

    def create_warehouse(self, data):
        self.require_type(data, ShipStationWarehouse)
        wh = self.post(endpoint="/warehouses/createwarehouse", data=data.json())
        return ShipStationWarehouse().json(wh.json())

    def delete_warehouse(self, warehouse_id):
        msg = self.delete(endpoint="/warehouses/" + str(warehouse_id))
        return msg.json()

    def update_warehouse(self, warehouse):
        self.require_type(warehouse, ShipStationWarehouse)
        wh = warehouse.json()
        msg = self.put(endpoint="/warehouses/" + str(warehouse.warehouse_id), data=wh)
        return msg.json()

    def list_webhooks(self):
        r = self.get(endpoint="/webhooks")
        webhooks = r.json().get("webhooks") if r.status_code == 200 else None
        return [ShipStationWebhook().json(w) for w in webhooks]

    def unsubscribe_to_webhook(self, webhook_id):
        return self.delete(endpoint="/webhooks/" + str(webhook_id))

    # return same webhook object with new webhook id
    def subscribe_to_webhook(self, webhook):
        self.require_type(webhook, ShipStationWebhook)
        self.require_membership(webhook.event, SUBSCRIBE_TO_WEBHOOK_EVENT_OPTIONS)
        r = self.post(endpoint="/webhooks/subscribe", data=webhook.prepare())
        if r.status_code == 201:
            webhook.id = r.json().get("id")
            return webhook
        # consider raiseing error code here with werkzeug Aborter
