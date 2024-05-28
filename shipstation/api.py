from typing import Any

import base64
import json
from decimal import Decimal
from io import BytesIO

from shipstation.constants import *
from shipstation.http import ShipStationHTTP
from shipstation.models import *
from shipstation.pagination import Page

Stringable = str | int | float | Decimal


class ShipStation(ShipStationHTTP):
    """
    Handles the details of connecting to and querying a ShipStation account.
    """

    # ACCOUNTS
    def list_tags(self) -> list[str | ShipStationOrderTag]:
        """
        List all tags defined for this Shipstation account.

        Documentation: https://www.shipstation.com/docs/api/accounts/list-tags/
        """

        tags = self.get(endpoint="/accounts/listtags")
        return [
            ShipStationOrderTag().json(tag) for tag in tags.json(parse_float=Decimal)
        ]

    # CARRIERS
    def get_carrier(self, carrier_code: str) -> ShipStationCarrier:
        """
        Retrieves the shipping carrier account details for the specified carrierCode.
        Use this method to determine a carrier's account balance.

        :param carrier_code: The code for the carrier account to retrieve.

        Documentation: https://www.shipstation.com/docs/api/carriers/get/
        """

        carrier = self.get(
            endpoint="/carriers/getcarrier", payload={"carrierCode": carrier_code}
        )
        return ShipStationCarrier().json(carrier.text)

    def list_carriers(self) -> list[str | ShipStationCarrier]:
        """
        List all shipping providers connected to this account.

        Documentation: https://www.shipstation.com/docs/api/carriers/list/
        """

        carriers = self.get(endpoint="/carriers")
        return [
            ShipStationCarrier().json(carrier)
            for carrier in carriers.json(parse_float=Decimal)
            if carrier
        ]

    def list_packages(self, carrier_code: str) -> list[str | ShipStationCarrierPackage]:
        """
        Retrieves a list of packages for the specified carrier.

        :param carrier_code: The carrier's code

        Documentation: https://www.shipstation.com/docs/api/carriers/list-packages/
        """

        packages = self.get(
            endpoint="/carriers/listpackages", payload={"carrierCode": carrier_code}
        )
        return [
            ShipStationCarrierPackage().json(package)
            for package in packages.json(parse_float=Decimal)
        ]

    def list_services(self, carrier_code: str) -> list[str | ShipStationCarrierService]:
        """
        Retrieves the list of available shipping services provided by the specified carrier.

        :param carrier_code: The carrier's code

        Documentation: https://www.shipstation.com/docs/api/carriers/list-services/
        """

        services = self.get(
            endpoint="/carriers/listservices", payload={"carrierCode": carrier_code}
        )
        return [
            ShipStationCarrierService().json(service)
            for service in services.json(parse_float=Decimal)
        ]

    # CUSTOMERS
    def get_customer(self, customer_id: Stringable) -> str | ShipStationCustomer:
        """
        Retrieve a single customer from the database.

        :param customer_id: The system-generated identifier for the Customer.

        Documentation: https://www.shipstation.com/docs/api/customers/get-customer/
        """

        customer = self.get(endpoint=f"/customers/{customer_id}")
        return ShipStationCustomer().json(customer.text)

    def list_customers(self, parameters: dict[str, Any] = {}) -> Page:
        """
        Obtains a list of customers that match the specified criteria.

        :param parameters: The specified parameters, defaults to {}

        Documentation: https://www.shipstation.com/docs/api/customers/list/
        """

        valid_parameters = self._validate_parameters(
            parameters, CUSTOMER_LIST_PARAMETERS
        )
        return Page(
            type=ShipStationCustomer,
            key="customers",
            params=valid_parameters,
            call=(self.get, {"endpoint": "/customers"}),
        )

    # FULFILLMENTS
    def list_fulfillments(self, parameters: dict[str, Any] = {}) -> Page:
        """
        The List Fulfillments API call obtains a list of fulfillments that match
        the specified criteria.

        :param parameters: The specified parameters, defaults to {}

        Documentation: https://www.shipstation.com/docs/api/fulfillments/list-fulfillments/
        """

        valid_parameters = self._validate_parameters(
            parameters, FULFILLMENT_LIST_PARAMETERS
        )
        return Page(
            type=ShipStationFulfillment,
            key="fulfillments",
            params=valid_parameters,
            call=(self.get, {"endpoint": "/fulfillments"}),
        )

    # ORDERS
    def add_tag_to_order(self, order_id: Stringable, tag_id: Stringable) -> Any:
        """
        Adds a tag to an order.

        :param order_id: Identifies the order that will be tagged.
        :param tag_id: Identifies the tag that will be applied to the order.

        Documentation: https://www.shipstation.com/docs/api/orders/add-tag/
        """

        data = json.dumps({"orderId": str(order_id), "tagId": str(tag_id)})
        r = self.post(endpoint="/orders/addtag", data=data)
        return r.json(parse_float=Decimal)

    def assign_user_to_order(
        self, order_id: Stringable | list[Stringable], user_id: Stringable
    ) -> Any:
        """
        Assigns a user to an order.

        :param order_id: Identifies the set of orders that will be assigned to the user.
        NOTE: If ANY of the orders within the array are not found, no orders will have a
        user assigned to them.
        :param user_id: Identifies the user that will be applied to the orders.
        It should contain a GUID of the user to be assigned to the array of orders.

        Documentation: https://www.shipstation.com/docs/api/orders/assign-user/
        """

        data = json.dumps({"orderId": str(order_id), "userId": str(user_id)})
        r = self.post(endpoint="/orders/assignuser", data=data)
        return r.json(parse_float=Decimal)

    def create_label_for_order(
        self, order: ShipStationOrder, test_label: bool = False, pdf: bool = False
    ) -> Any | BytesIO | ShipStationOrder:
        """
        Creates a shipping label for a given order. The `labelData` field returned in the
        response is a base64-encoded PDF value. Simply decode and save the output as a PDF
        file to retrieve a printable label.

        :param order: Identifies which order to ship.
        :param test_label: Specifies whether or not to create a test label, defaults to False
        :param pdf: Specifies whether the output should be processed as PDF, defaults to False

        Documentation: https://www.shipstation.com/docs/api/orders/create-label/
        """

        if test_label:
            setattr(order, "test_label", True)
        label_data = order.json()
        r = self.post(endpoint="/orders/createlabelfororder", data=label_data)
        if r.status_code != 200:
            return r.json()
        new_data = self.convert_camel_case(r.json())
        if pdf:
            return BytesIO(base64.b64decode(new_data["label_data"]))
        if isinstance(new_data, dict):
            for key, value in new_data.items():
                if value:
                    setattr(order, key, value)
        elif isinstance(new_data, (list, set, tuple)):
            for key, value in new_data:
                if value:
                    setattr(order, key, value)
        return order

    def create_orders(
        self, orders: list[ShipStationOrder]
    ) -> list[str | ShipStationOrder]:
        """
        This endpoint can be used to create or update multiple orders in one request.
        If the `orderKey` is specified, ShipStation will attempt to locate the order with the
        specified `orderKey`. If found, the existing order with that key will be updated.
        If the `orderKey` is not found, a new order will be created with that `orderKey`.

        For split orders, the `orderKey` is always required when creating or updating orders,
        and the orderId is always required for updates.

        This call does not currently support partial updates; the entire resource must be
        provided in the body of the request.

        :param orders: An array of ShipStationOrder objects (maximum of 100 per request).

        # TODO: refactor to new API
        Documentation: https://www.shipstation.com/docs/api/orders/create-update-multiple-orders/
        """

        self.require_type(orders, list)
        responses = []  # refactor to generator
        for order in orders:
            r = self.post(endpoint="/orders/createorder", data=order.json())
            responses.append(ShipStationOrder().json(r.json(parse_float=Decimal)))
        return responses

    def create_order(self, order: ShipStationOrder) -> ShipStationOrder:
        """
        You can use this method to create a new order or update an existing order.
        If the `orderKey` is specified, ShipStation will attempt to locate the order with the
        specified `orderKey`. If found, the existing order with that key will be updated.
        If the `orderKey` is not found, a new order will be created with that `orderKey`.

        https://www.shipstation.com/docs/api/models/advanced-options/
        For split orders, see the mergedOrSplit property in Advanced Options. This
        property (key) is always required for merged or split orders.

        This call does not currently support partial updates. The entire resource must
        be provided in the body of the request.

        NOTE: For new order creation do not attempt to pass in the `orderId` property.

        :param order: A ShipStationOrder object.

        Documentation: https://www.shipstation.com/docs/api/orders/create-update-order/
        """

        self.require_type(order, ShipStationOrder)
        r = self.post(endpoint="/orders/createorder", data=order.json())
        return ShipStationOrder().json(r.json(parse_float=Decimal))

    def delete_order(self, order_id: Stringable) -> Any:
        """
        Removes order from ShipStation's UI. Note this is a "soft" delete action so the
        order will still exist in the database, but will be set to inactive.

        :param order_id: Identifies the order to be deleted.

        Documentation: https://www.shipstation.com/docs/api/orders/delete/
        """

        r = self.delete(endpoint=f"/orders/{order_id}")
        return r.json(parse_float=Decimal)

    def get_order(self, order_id: Stringable) -> str | ShipStationOrder:
        """
        Retrieve a single order from the database.

        :param order_id: Identifies the order to be retrieved.

        Documentation: https://www.shipstation.com/docs/api/orders/get-order/
        """

        r = self.get(endpoint=f"/orders/{order_id}")
        return ShipStationOrder().json(r.json(parse_float=Decimal))

    def hold_order_until(
        self, order_id: str, hold_until_date: str
    ) -> Any:  # TODO: make a date helper
        """
        This method will change the status of the given order to 'On Hold' status until
        the date you have specified, when the status will automatically change to
        'Awaiting Shipment' status.

        :param order_id: Identifies the order that will be held.
        :param hold_until_date: Date when order is moved from on_hold status to
        awaiting_shipment.

        Documentation: https://www.shipstation.com/docs/api/orders/hold-order-until/
        """

        data = json.dumps(
            {"orderId": str(order_id), "holdUntilDate": str(hold_until_date)}
        )
        r = self.post(endpoint="/orders/holduntil", data=data)
        return r.json(parse_float=Decimal)

    def list_orders_by_tag(
        self,
        parameters: dict[str, Any] = {},
    ) -> Page:
        """
        Lists all orders that match the specified order status (`orderStatus`) and
        tag ID (`tagId`).

        :param parameters: The specified parameters, defaults to {}

        Documentation: https://www.shipstation.com/docs/api/orders/list-by-tag/
        """

        valid_parameters = self._validate_parameters(
            parameters, ORDER_LIST_BY_TAG_PARAMETERS
        )
        return Page(
            type=ShipStationOrder,
            key="orders",
            params=valid_parameters,
            call=(self.get, {"endpoint": "/orders/listbytag"}),
        )

    def list_orders(self, parameters: dict[str, Any] = {}) -> Page:
        """
        Obtains a list of orders that match the specified criteria. All of the available
        filters are optional. They do not need to be included in the URL.

        :param parameters: The specified parameters, defaults to {}

        Documentation: https://www.shipstation.com/docs/api/orders/list-orders/
        """

        self.require_type(parameters, dict)
        valid_parameters = self._validate_parameters(parameters, ORDER_LIST_PARAMETERS)
        return Page(
            type=ShipStationOrder,
            key="orders",
            params=valid_parameters,
            call=(self.get, {"endpoint": "/orders"}),
        )

    def mark_order_as_shipped(
        self,
        order_id: str,
        carrier_code: str,
        ship_date: str | None = None,  # TODO: make a date helper
        tracking_number: str | None = None,
        notify_customer: bool = False,
        notify_sales_channel: bool = False,
    ) -> Any:
        """
        Marks an order as Shipped without creating a label in ShipStation.

        :param order_id: Identifies the order that will be marked as 'Shipped'.
        :param carrier_code: Code of the carrier that is marked as having shipped the order.
        :param ship_date: Date order was shipped, defaults to None
        :param tracking_number: Tracking number of shipment, defaults to None
        :param notify_customer: Specifies whether the customer should be notified of the
        shipment, defaults to False
        :param notify_sales_channel: Specifies whether the sales channel should be notified
        of the shipment, defaults to False

        Documentation: https://www.shipstation.com/docs/api/orders/mark-as-shipped/
        """

        data = json.dumps(
            {
                "orderId": str(order_id),
                "carrierCode": str(carrier_code),
                "shipDate": str(ship_date),
                "trackingNumber": str(tracking_number),
                "notifyCustomer": notify_customer,
                "notifySalesChannel": notify_sales_channel,
            }
        )
        r = self.post(endpoint="/orders/markasshipped", data=data)
        return r.json(parse_float=Decimal)

    def remove_tag_from_order(self, order_id: Stringable, tag_id: Stringable) -> Any:
        """
        Removes a tag from the specified order.

        :param order_id: Identifies the order whose tag will be removed.
        :param tag_id: Identifies the tag to remove.

        Documentation: https://www.shipstation.com/docs/api/orders/remove-tag/
        """

        data = json.dumps({"orderId": str(order_id), "tagId": str(tag_id)})
        r = self.post(endpoint="/orders/removetag", data=data)
        return r.json(parse_float=Decimal)

    def restore_order_from_on_hold(self, order_id: Stringable) -> Any:
        """
        This method will change the status of the given order from 'On Hold' status to
        'Awaiting Shipment' status. This endpoint is used when a `holdUntilDate` is
        attached to an order.

        :param order_id: Identifies the order that will be restored to `awaiting_shipment`
        status from `on_hold`.

        Documentation: https://www.shipstation.com/docs/api/orders/restore-from-hold/
        """

        data = json.dumps({"orderId": str(order_id)})
        r = self.post(endpoint="/orders/restorefromhold", data=data)
        return r.json(parse_float=Decimal)

    def unassign_user_from_order(self, order_id: Stringable | list[Stringable]) -> Any:
        """
        Unassigns a user from an order.

        :param order_id: Identifies an order or set of orders that will have the
        user unassigned.

        NOTE: If ANY of the orders within the array are not found, then no orders
        will have their users unassigned.

        Documentation: https://www.shipstation.com/docs/api/orders/unassign-user/
        """

        data = json.dumps({"orderId": str(order_id)})
        r = self.post(endpoint="/orders/unassignuser", data=data)
        return r.json(parse_float=Decimal)

    # PRODUCTS
    def get_product(self, product_id: Stringable) -> str | ShipStationItem:
        """
        Retrieve a single product from the database.

        :param product_id: The system-generated identifier for the Product.

        Documentation: https://www.shipstation.com/docs/api/products/get-product/
        """

        r = self.get(endpoint=f"/products/{product_id}")
        return ShipStationItem().json(
            r.text
        )  # TODO: switch to parse float and test deserialization

    def list_products(self, parameters: dict[str, Any] = {}) -> Page:
        """
        Obtains a list of products that match the specified criteria. All of the
        available filters are optional. They do not need to be included in the URL.

        :param parameters: The specified parameters, defaults to {}

        Documentation: https://www.shipstation.com/docs/api/products/list/
        """

        valid_parameters = self._validate_parameters(
            parameters, PRODUCT_LIST_PARAMETERS
        )
        return Page(
            type=ShipStationItem,
            key="products",
            params=valid_parameters,
            call=(self.get, {"endpoint": "/products"}),
        )

    def update_product(self, product: ShipStationItem) -> Any:
        """
        Updates an existing product. This call does not currently support partial
        updates. The entire resource must be provided in the body of the request.

        :param product: The product to be updated.

        Documentation: https://www.shipstation.com/docs/api/products/update/
        """

        self.require_type(product, ShipStationItem)
        data = product.json()
        r = self.put(endpoint=f"/products/{product.product_id}", data=data)
        return r.json(parse_float=Decimal)

    # SHIPMENTS
    def create_shipment_label(self, order: ShipStationOrder) -> ShipStationOrder:
        """
        Creates a shipping label. The `labelData` field returned in the response is a
        base64-encoded PDF value. You can decode and save the output as a PDF file
        to retrieve a printable label.

        :param order: Identifies which order to ship.

        Documentation: https://www.shipstation.com/docs/api/shipments/create-label/
        """

        self.require_type(order, ShipStationOrder)
        # TODO: return shipment label as objects
        return self.post(endpoint="/shipments/createlabel", data=order.json())

    def get_rates(self, options: ShipStationRateOptions) -> list[str | ShipStationRate]:
        """
        Retrieves shipping rates for the specified shipping details.

        :param options: The specified shipping details.

        Documentation: https://www.shipstation.com/docs/api/shipments/get-rates/
        """

        self.require_type(options, ShipStationRateOptions)
        self.require_type(options.weight, ShipStationWeight)
        if options.dimensions:
            self.require_type(options.dimensions, ShipStationContainer)
        rates = self.post(endpoint="/shipments/getrates", data=options.json())
        return [
            ShipStationRate().json(rate) for rate in rates.json(parse_float=Decimal)
        ]

    def list_shipments(self, parameters: dict[str, Any] = {}) -> Page:
        """
        Obtains a list of shipments that match the specified criteria.

        :param parameters: The specified parameters, defaults to {}

        Documentation: https://www.shipstation.com/docs/api/shipments/list/
        """

        valid_parameters = self._validate_parameters(
            parameters, SHIPMENT_LIST_PARAMETERS
        )
        return Page(
            type=ShipStationOrder,
            key="shipments",
            params=valid_parameters,
            call=(self.get, {"endpoint": "/shipments"}),
        )

    def void_label(self, shipment_id: str) -> Any:
        """
        Voids the specified label by `shipmentId`.

        :param shipment_id: ID of the shipment to void.

        Documentation: https://www.shipstation.com/docs/api/shipments/void-label/
        """

        # TODO: return status code
        return self.post(endpoint="/shipments/voidlabel", data=shipment_id)

    # STORES
    def deactivate_store(self, store_id: Stringable) -> Any:
        """
        Deactivates the specified store.

        :param store_id: ID of the store to deactivate.

        Documentation: https://www.shipstation.com/docs/api/stores/deactivate/
        """

        store_id = json.dumps({"storeId": str(store_id)})
        store = self.post(endpoint="/stores/deactivate", data=store_id)
        return store.json(parse_float=Decimal)

    def get_store(self, store_id: Stringable) -> str | ShipStationStore:
        """
        This Get Store API call uses the storeId property to retrieve information
        related to a specific store.

        :param store_id: Unique identifier for the store.

        Documentation: https://www.shipstation.com/docs/api/stores/get-store/
        """

        store = self.get(endpoint=f"/stores/{store_id}")
        return ShipStationStore().json(store.json(parse_float=Decimal))

    def list_marketplaces(self) -> list[str | ShipStationMarketplace]:
        """
        Lists the marketplaces that can be integrated with ShipStation.

        Documentation: https://www.shipstation.com/docs/api/stores/list-marketplaces/
        """

        marketplaces = self.get(endpoint="/stores/marketplaces")
        return [
            ShipStationMarketplace().json(m)
            for m in marketplaces.json(parse_float=Decimal)
            if m
        ]

    def list_stores(
        self, show_inactive: bool = False, marketplace_id: int | None = None
    ) -> list[str | ShipStationStore]:
        """
        Retrieve the list of installed stores on the account with this API call.

        :param show_inactive: Determines whether or not inactive stores will be
        returned in the list of stores, defaults to False
        :param marketplace_id: Returns stores of this marketplace type, defaults to None

        Documentation: https://www.shipstation.com/docs/api/stores/list/
        """

        parameters = {}
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

    def update_store(self, parameters: dict[str, Any]) -> str | ShipStationStore:
        """
        Updates an existing store. This call does not currently support partial updates.

        :param parameters: Unique identifier for the store

        Documentation: https://www.shipstation.com/docs/api/stores/update/
        """

        parameters = self._validate_parameters(parameters, UPDATE_STORE_OPTIONS)
        for m in UPDATE_STORE_OPTIONS:
            self.require_attribute(m)
        self.require_type(parameters.get("status_mappings"), list)
        for mapping in parameters.get("status_mappings"):
            self.require_type(mapping, ShipStationStatusMapping)
            self.require_membership(mapping["orderStatus"], ORDER_STATUS_VALUES)
        store = self.put(endpoint="/stores/storeId", data=parameters)
        return ShipStationStore().json(store.json(parse_float=Decimal))

    def reactivate_store(self, store_id: Stringable) -> Any:
        """
        Reactivates the specified store.

        :param store_id: ID of the store to reactivate.

        Documentation: https://www.shipstation.com/docs/api/stores/reactivate/
        """

        store_id = json.dumps({"storeId": str(store_id)})
        store = self.post(endpoint="/stores/reactivate", data=store_id)
        return store.json(parse_float=Decimal)

    # USERS
    def list_users(self, show_inactive: bool = False) -> list[str | ShipStationUser]:
        """
        Retrieves a list of users that match the specified criteria.

        :param show_inactive: Determines whether or not inactive users will be
        returned in the response, defaults to False

        Documentation: https://www.shipstation.com/docs/api/users/list/
        """

        self.require_type(show_inactive, bool)
        users = self.get(
            endpoint="/users", payload=json.dumps({"showInactive": show_inactive})
        )
        return [
            ShipStationUser().json(user)
            for user in users.json(parse_float=Decimal)
            if user
        ]

    # WAREHOUSES
    def create_warehouse(
        self, data: ShipStationWarehouse
    ) -> str | ShipStationWarehouse:
        """
        Adds a Ship From Location to your account.

        :param data: The warehouse data to be added.

        Documentation: https://www.shipstation.com/docs/api/warehouses/create/
        """

        self.require_type(data, ShipStationWarehouse)
        r = self.post(endpoint="/warehouses/createwarehouse", data=data.json())
        return ShipStationWarehouse().json(r.json(parse_float=Decimal))

    def delete_warehouse(self, warehouse_id: Stringable) -> Any:
        """
        Removes a warehouse from ShipStation's UI and sets it to Inactive status.

        :param warehouse_id: A unique ID generated by ShipStation and assigned
        to each Ship From Location.

        Documentation: https://www.shipstation.com/docs/api/warehouses/delete/
        """

        r = self.delete(endpoint=f"/warehouses/{warehouse_id}")
        return r.json(parse_float=Decimal)

    def get_warehouse(self, warehouse_id: Stringable) -> str | ShipStationWarehouse:
        """
        Returns a list of active Ship From Locations on the ShipStation account.

        :param warehouse_id: A unique ID generated by ShipStation and assigned to each
        Ship From Location.

        Documentation: https://www.shipstation.com/docs/api/warehouses/get/
        """

        r = self.get(endpoint=f"/warehouses/{warehouse_id}")
        return ShipStationWarehouse().json(r.json(parse_float=Decimal))

    def list_warehouses(self) -> list[str | ShipStationWarehouse]:
        """
        Retrieves a list of your Ship From Locations.

        Documentation: https://www.shipstation.com/docs/api/warehouses/list/
        """

        warehouses = self.get(endpoint="/warehouses")
        return [
            ShipStationWarehouse().json(wh)
            for wh in warehouses.json(parse_float=Decimal)
            if wh
        ]

    def update_warehouse(self, warehouse: ShipStationWarehouse) -> Any:
        """
        Updates an existing Ship From Location. This call does not currently support
        partial updates. The entire resource must be provided in the body of the
        request. If a "returnAddress" object is not specified, your "originAddress"
        will be used as your "returnAddress".

        :param warehouse: A unique ID generated by ShipStation and assigned to each
        Ship From Location.

        Documentation: https://www.shipstation.com/docs/api/warehouses/update/
        """

        self.require_type(warehouse, ShipStationWarehouse)
        wh = warehouse.json()
        r = self.put(endpoint=f"/warehouses/{warehouse.warehouse_id}", data=wh)
        return r.json(parse_float=Decimal)

    # WEBHOOKS
    def list_webhooks(self) -> list[str | ShipStationWebhook]:
        """
        Retrieves a list of registered webhooks for the account.

        Documentation: https://www.shipstation.com/docs/api/webhooks/list/
        """

        r = self.get(endpoint="/webhooks")
        webhooks = (
            r.json(parse_float=Decimal).get("webhooks")
            if r.status_code == 200
            else None
        )
        return [ShipStationWebhook().json(w) for w in webhooks if w]

    # return same webhook object with new webhook id
    def subscribe_to_webhook(self, webhook: ShipStationWebhook) -> ShipStationWebhook:
        """
        Subscribes to a specific type of webhook. If a `store_id` is passed in, the
        webhooks will only be triggered for that specific `store_id`. The `event` type
        that is passed in will determine what type of webhooks will be sent.

        :param webhook: The webhook to subscribe to.

        Documentation: https://www.shipstation.com/docs/api/webhooks/subscribe/
        """

        self.require_type(webhook, ShipStationWebhook)
        self.require_membership(webhook.event, SUBSCRIBE_TO_WEBHOOK_EVENT_OPTIONS)
        r = self.post(endpoint="/webhooks/subscribe", data=webhook.prepare())
        if r.status_code == 201:
            webhook.web_hook_id = r.json(parse_float=Decimal).get("id")
        return webhook
        # consider raising error code here with werkzeug Aborter

    def unsubscribe_to_webhook(self, webhook_id: Stringable) -> Any:
        """
        Unsubscribes from a certain webhook.

        :param webhook_id: A unique ID generated by ShipStation and assigned to
        each webhook.

        Documentation: https://www.shipstation.com/docs/api/webhooks/unsubscribe/
        """

        r = self.delete(endpoint=f"/webhooks/{webhook_id}")
        return r.json(parse_float=Decimal)
