import base64
import datetime
import json
import typing
from decimal import Decimal
from io import BytesIO

import requests

from shipstation.base import ShipStationBase
from shipstation.constants import *
from shipstation.http import ShipStationHTTP
from shipstation.models import *
from shipstation.pagination import Page


class ShipStation(ShipStationHTTP):
    """
    Handles the details of connecting to and querying a ShipStation account.
    """

    orders: typing.Optional[typing.List[typing.Union[str, ShipStationBase]]] = None

    def list_tags(self) -> typing.List[typing.Union[str, ShipStationBase, None]]:
        tags = self.get(endpoint="/accounts/listtags")
        return [
            ShipStationOrderTag().json(tag) for tag in tags.json(parse_float=Decimal)
        ]

    def create_orders(
        self, orders: typing.Sequence[ShipStationOrder]
    ) -> typing.List[typing.Union[str, ShipStationOrder]]:
        self.require_type(orders, list)
        responses = []  # refactor to generator
        for order in orders:
            r = self.post(endpoint="/orders/createorder", data=order.json())
            responses.append(ShipStationOrder().json(r.json(parse_float=Decimal)))
        return responses

    def create_order(self, order: ShipStationOrder) -> ShipStationOrder:
        self.require_type(order, ShipStationOrder)
        r = self.post(endpoint="/orders/createorder", data=order.json())
        return ShipStationOrder().json(r.json(parse_float=Decimal))

    # refactor
    def list_orders(self, parameters: typing.Dict[str, typing.Any] = {}) -> Page:
        self.require_type(parameters, dict)
        invalid_keys = set(parameters.keys()).difference(ORDER_LIST_PARAMETERS)
        if invalid_keys:
            raise AttributeError(
                "Invalid order list parameters: {}".format(", ".join(invalid_keys))
            )
        valid_parameters = {
            self.to_camel_case(key): value for key, value in parameters.items()
        }
        return Page(
            type=ShipStationOrder,
            key="orders",
            params=valid_parameters,
            call=(self.get, {"endpoint": "/orders/list"}),
        )

    def get_order(self, order_id: str) -> typing.Union[str, ShipStationBase, None]:
        r = self.get(endpoint=f"/orders/{order_id}")
        return ShipStationOrder().json(r.json(parse_float=Decimal))

    def delete_order(self, order_id: str) -> typing.Any:
        msg = self.delete(endpoint=f"/orders/{order_id}")
        return msg.json(parse_float=Decimal)

    def add_tag_to_order(self, order_id: str, tag_id: str) -> typing.Any:
        data = json.dumps({"orderId": str(order_id), "tagId": str(tag_id)})
        r = self.post(endpoint="/orders/addtag", data=data)
        return r.json(parse_float=Decimal)

    def assign_user_to_order(self, order_id: str, user_id: str) -> typing.Any:
        data = json.dumps({"orderId": str(order_id), "userId": str(user_id)})
        r = self.post(endpoint="/orders/assignuser", data=data)
        return r.json(parse_float=Decimal)

    def create_label_for_order(
        self, order: ShipStationOrder, test_label: bool = False, pdf: bool = False
    ) -> typing.Union[bytes, typing.Any, ShipStationBase, None]:
        setattr(order, "test_label", True) if test_label else False
        label_data = order.json()
        r = self.post(endpoint="/orders/createlabelfororder", data=label_data)
        if not r.status_code == 200:
            return r.json()
        new_data = self.convert_camel_case(r.json())
        if pdf:
            return BytesIO(base64.b64decode(new_data["label_data"]))  # type: ignore
        for key, value in new_data:  # refactor to generator
            if value:
                setattr(order, key, value)
        return order

    def hold_order_until(
        self, order_id: str, hold_until_date: str
    ) -> typing.Any:  # make a date helper
        data = json.dumps(
            {"orderId": str(order_id), "holdUntilDate": str(hold_until_date)}
        )
        r = self.post(endpoint="/orders/holduntil", data=data)
        return r.json(parse_float=Decimal)

    # not working
    def list_orders_by_tag(self, order_status, tag_id, page=None, page_size=None):
        payload = {"orderStatus": order_status, "tagId": tag_id}
        if page:
            payload["page"] = page
        if page_size:
            payload["pageSize"] = page_size
        return Page(
            type=ShipStationOrder,
            key="orders",
            call=(self.get, {"endpoint": "/orders/listbytag", "payload": payload}),
        )

    def mark_order_as_shipped(
        self,
        order_id: str,
        carrier_code: str,
        ship_date: typing.Optional[str] = None,  # make a date helper
        tracking_number: typing.Optional[str] = None,
        notify_customer: bool = False,
        notify_sales_channel: bool = False,
    ) -> typing.Any:
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
        return r.json(parse_float=Decimal)

    def remove_tag_from_order(self):
        pass

    def restore_order_from_on_hold(self):
        pass

    def unassign_user_from_order(self):
        pass

    def get_product(self, product_id: str) -> typing.Union[str, ShipStationBase, None]:
        r = self.get(endpoint=f"/products/{product_id}")
        return ShipStationItem().json(r.text) #TODO: switch to parse float and test deserialization

    def list_products(self, parameters: typing.Dict[str, typing.Any] = {}) -> Page:
        valid_parameters = self._validate_parameters(
            parameters, PRODUCT_LIST_PARAMETERS
        )
        return Page(
            type=ShipStationItem,
            key="products",
            params=valid_parameters,
            call=(self.get, {"endpoint": "/products"}),
        )

    def update_product(self, product: ShipStationItem) -> typing.Any:
        self.require_type(product, ShipStationItem)
        data = product.json()
        msg = self.put(endpoint=f"/products/{product.product_id}", data=data)
        return msg.json(parse_float=Decimal)

    def list_carriers(self) -> typing.List[typing.Union[str, ShipStationBase, None]]:
        carriers = self.get(endpoint="/carriers")
        return [
            ShipStationCarrier().json(carrier)
            for carrier in carriers.json(parse_float=Decimal)
            if carrier
        ]

    def get_carrier(self, carrier_code: str) -> typing.Optional[ShipStationCarrier]:
        carrier = self.get(
            endpoint="/carriers/getcarrier", payload={"carrierCode": carrier_code}
        )
        return ShipStationCarrier().json(carrier.text)  # type: ignore

    def list_packages(
        self, carrier_code: str
    ) -> typing.List[typing.Union[str, ShipStationBase, None]]:
        packages = self.get(
            endpoint="/carriers/listpackages", payload={"carrierCode": carrier_code}
        )
        return [
            ShipStationCarrierPackage().json(package)
            for package in packages.json(parse_float=Decimal)
        ]

    def list_services(
        self, carrier_code: str
    ) -> typing.List[typing.Union[str, ShipStationBase, None]]:
        services = self.get(
            endpoint="/carriers/listservices", payload={"carrierCode": carrier_code}
        )
        return [
            ShipStationCarrierService().json(service)
            for service in services.json(parse_float=Decimal)
        ]

    def get_customer(
        self, customer_id: str
    ) -> typing.Union[str, ShipStationBase, None]:
        customer = self.get(endpoint=f"/customers/{customer_id}")
        return ShipStationCustomer().json(customer.text)

    def list_customers(self, parameters: typing.Any = {}) -> Page:
        valid_parameters = self._validate_parameters(
            parameters, CUSTOMER_LIST_PARAMETERS
        )
        return Page(
            type=ShipStationCustomer,
            key="customers",
            params=valid_parameters,
            call=(self.get, {"endpoint": "/customers"}),
        )

    def list_fulfillments(self, parameters: typing.Any = {}) -> Page:
        valid_parameters = self._validate_parameters(
            parameters, FULFILLMENT_LIST_PARAMETERS
        )
        return Page(
            type=ShipStationFulfillment,
            key="fulfillments",
            params=valid_parameters,
            call=(self.get, {"endpoint": "/fulfillments"}),
        )

    def list_shipments(self, parameters: typing.Any = {}) -> Page:
        valid_parameters = self._validate_parameters(
            parameters, SHIPMENT_LIST_PARAMETERS
        )
        return Page(
            type=ShipStationOrder,
            key="shipments",
            params=valid_parameters,
            call=(self.get, {"endpoint": "/shipments"}),
        )

    # TODO: return shipment label as objects
    def create_shipment_label(self, order: str) -> ShipStationOrder:
        self.require_type(order, ShipStationOrder)
        order.validate()
        return self.post(endpoint="/shipments/createlabel", data=order.json())

    def get_rates(
        self, options: ShipStationRateOptions
    ) -> typing.List[typing.Union[str, ShipStationBase, None]]:
        self.require_type(options, ShipStationRateOptions)
        self.require_type(options.weight, ShipStationWeight)
        if options.dimensions:
            self.require_type(options.dimensions, ShipStationContainer)
        rates = self.post(endpoint="/shipments/getrates", data=options.json())
        return [
            ShipStationRate().json(rate) for rate in rates.json(parse_float=Decimal)
        ]

    # TODO: return status code
    def void_label(self, shipment_id):
        return self.post(endpoint="/shipments/voidlabel", data=shipment_id)

    def list_marketplaces(self):
        marketplaces = self.get(endpoint="/stores/marketplaces")
        return [
            ShipStationMarketplace().json(m)
            for m in marketplaces.json(parse_float=Decimal)
            if m
        ]

    def list_stores(
        self, show_inactive: bool = False, marketplace_id: typing.Optional[str] = None
    ) -> typing.List[typing.Union[str, ShipStationBase]]:
        parameters = {}  # type: ignore
        if show_inactive:
            self.require_type(show_inactive, bool)
            parameters["showInactive"] = show_inactive
        if marketplace_id:
            self.require_type(marketplace_id, int)
            parameters["marketplaceId"] = marketplace_id
        stores = self.get(endpoint="/stores", payload=parameters)
        return [
            ShipStationStore().json(s) for s in stores.json(parse_float=Decimal) if s
        ]

    def get_store(self, store_id: str) -> typing.Union[str, ShipStationBase, None]:
        store = self.get(endpoint=f"/stores/{store_id}")
        return ShipStationStore().json(store.json(parse_float=Decimal))

    def update_store(
        self, options: typing.Any
    ) -> typing.Union[str, ShipStationBase, None]:
        options = self._validate_parameters(options, UPDATE_STORE_OPTIONS)
        for m in UPDATE_STORE_OPTIONS:
            self.require_attribute(m)
        self.require_type(options.get("status_mappings"), list)
        for mapping in options.get("status_mappings"):
            self.require_type(mapping, ShipStationStatusMapping)
            self.require_membership(mapping["orderStatus"], ORDER_STATUS_VALUES)
        store = self.put(endpoint="/stores/storeId", data=options)
        return ShipStationStore().json(store.json(parse_float=Decimal))

    def deactivate_store(self, store_id: str) -> typing.Any:
        store_id = json.dumps({"storeId": str(store_id)})
        store = self.post(endpoint="/stores/deactivate", data=store_id)
        return store.json(parse_float=Decimal)

    def reactivate_store(self, store_id: str) -> typing.Any:
        store_id = json.dumps({"storeId": str(store_id)})
        store = self.post(endpoint="/stores/reactivate", data=store_id)
        return store.json(parse_float=Decimal)

    def list_users(
        self, show_inactive: bool = False
    ) -> typing.List[typing.Union[str, ShipStationBase]]:
        self.require_type(show_inactive, bool)
        users = self.get(
            endpoint="/users", payload=json.dumps({"showInactive": show_inactive})
        )
        return [
            ShipStationUser().json(user)
            for user in users.json(parse_float=Decimal)
            if user
        ]

    def get_warehouse(
        self, warehouse_id: str
    ) -> typing.Optional[typing.Union[str, ShipStationBase]]:
        wh = self.get(endpoint=f"/warehouses/{warehouse_id}")
        return ShipStationWarehouse().json(wh.json(parse_float=Decimal))

    def list_warehouses(self) -> typing.List[typing.Union[str, ShipStationBase]]:
        warehouses = self.get(endpoint="/warehouses")
        return [
            ShipStationWarehouse().json(wh)
            for wh in warehouses.json(parse_float=Decimal)
            if wh
        ]

    def create_warehouse(
        self, data: ShipStationWarehouse
    ) -> typing.Union[str, ShipStationBase]:
        self.require_type(data, ShipStationWarehouse)
        wh = self.post(endpoint="/warehouses/createwarehouse", data=data.json())
        return ShipStationWarehouse().json(wh.json(parse_float=Decimal))

    def delete_warehouse(self, warehouse_id: str) -> typing.Any:
        msg = self.delete(endpoint=f"/warehouses/{warehouse_id}")
        return msg.json(parse_float=Decimal)

    def update_warehouse(self, warehouse: ShipStationWarehouse) -> typing.Any:
        self.require_type(warehouse, ShipStationWarehouse)
        wh = warehouse.json()
        msg = self.put(endpoint=f"/warehouses/{warehouse.warehouse_id}", data=wh)
        return msg.json(parse_float=Decimal)

    def list_webhooks(self) -> typing.List[typing.Union[str, ShipStationBase]]:
        r = self.get(endpoint="/webhooks")
        webhooks = (
            r.json(parse_float=Decimal).get("webhooks")
            if r.status_code == 200
            else None
        )
        return [ShipStationWebhook().json(w) for w in webhooks if w]

    def unsubscribe_to_webhook(self, webhook_id: str) -> typing.Any:
        msg = self.delete(endpoint=f"/webhooks/{webhook_id}")
        return msg.json(parse_float=Decimal)

    # return same webhook object with new webhook id
    def subscribe_to_webhook(self, webhook: ShipStationWebhook) -> ShipStationWebhook:
        self.require_type(webhook, ShipStationWebhook)
        self.require_membership(webhook.event, SUBSCRIBE_TO_WEBHOOK_EVENT_OPTIONS)
        r = self.post(endpoint="/webhooks/subscribe", data=webhook.prepare())
        if r.status_code == 201:
            webhook.web_hook_id = r.json(parse_float=Decimal).get("id")
        return webhook
        # consider raising error code here with werkzeug Aborter
