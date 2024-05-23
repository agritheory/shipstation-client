from typing import Literal

__all__ = [
    "ADDRESS_VERIFIED_VALUES",
    "BILL_TO_PARTY_VALUES",
    "CONFIRMATION_VALUES",
    "CONTENTS_VALUES",
    "CREATE_ORDER_LABEL_OPTIONS",
    "CREATE_SHIPMENT_LABEL_OPTIONS",
    "CREATE_WAREHOUSE_OPTIONS",
    "CUSTOMER_LIST_PARAMETERS",
    "DIMENSIONS_UNIT_OPTIONS",
    "FULFILLMENT_LIST_PARAMETERS",
    "GET_RATE_OPTIONS",
    "NON_DELIVERY_OPTIONS",
    "ORDER_LIST_PARAMETERS",
    "ORDER_STATUS_VALUES",
    "PRODUCT_LIST_PARAMETERS",
    "PROVIDER_VALUES",
    "REQUIRED_RATE_OPTIONS",
    "SHIPMENT_LIST_PARAMETERS",
    "SUBSCRIBE_TO_WEBHOOK_EVENT_OPTIONS",
    "SUBSCRIBE_TO_WEBHOOK_OPTIONS",
    "UPDATE_STORE_OPTIONS",
    "WEIGHT_UNIT_OPTIONS",
]

# https://www.shipstation.com/docs/api/orders/create-update-order/
# orderStatus
ORDER_STATUS_VALUES = Literal[
    "awaiting_payment",
    "awaiting_shipment",
    "shipped",
    "on_hold",
    "cancelled",
    "pending_fulfillment",
]

# TODO: add method for adding confirmation which respects these values.
# https://www.shipstation.com/docs/api/orders/create-update-order/
# confirmation
CONFIRMATION_VALUES = Literal[
    "none",
    "delivery",
    "signature",
    "adult_signature",
    "direct_signature",
]

# https://www.shipstation.com/docs/api/orders/create-update-order/
# provider
PROVIDER_VALUES = Literal["shipsurance", "carrier", "provider", "xcover", "parcelguard"]

# https://www.shipstation.com/docs/api/orders/create-update-order/
# advancedOptions
BILL_TO_PARTY_VALUES = Literal[
    "my_account", "my_other_account", "recipient", "third_party"
]

# https://www.shipstation.com/docs/api/orders/create-update-order/
# billTo, shipTo
ADDRESS_VERIFIED_VALUES = Literal[
    "Address not yet validated",
    "Address validated successfully",
    "Address validation warning",
    "Address validation failed",
]

# https://www.shipstation.com/docs/api/products/list/
PRODUCT_LIST_PARAMETERS = (
    "sku",
    "name",
    "product_category_id",
    "product_type_id",
    "tag_id",
    "start_date",
    "end_date",
    "show_inactive",
    "sort_by",
    "sort_dir",
    "page",
    "page_size",
)

# https://www.shipstation.com/docs/api/orders/list-orders/
ORDER_LIST_PARAMETERS = (
    "customer_name",
    "item_keyword",
    "create_date_start",
    "create_date_end",
    "modify_date_start",
    "modify_date_end",
    "order_date_start",
    "order_date_end",
    "order_number",
    "order_status",
    "payment_date_start",
    "payment_date_end",
    "store_id",
    "sort_by",
    "sort_dir",
    "page",
    "page_size",
)


# https://www.shipstation.com/docs/api/orders/create-label/
CREATE_ORDER_LABEL_OPTIONS = (
    "order_id",
    "carrier_code",
    "service_code",
    "confirmation",
    "ship_date",
    "weight",
    "dimensions",
    "insurance_options",
    "international_options",
    "advanced_options",
    "test_label",
)


# https://www.shipstation.com/docs/api/customers/list/
CUSTOMER_LIST_PARAMETERS = (
    "state_code",
    "country_code",
    "marketplace_id",
    "tag_id",
    "sort_by",
    "sort_dir",
    "page_size",
)

# https://www.shipstation.com/docs/api/fulfillments/list-fulfillments/
FULFILLMENT_LIST_PARAMETERS = (
    "fulfillment_id",
    "order_id",
    "order_number",
    "tracking_number",
    "recipient_name",
    "create_date_start",
    "create_date_end",
    "ship_date_start",
    "ship_date_end",
    "sort_by",
    "sort_dir",
    "page",
    "page_size",
)

# https://www.shipstation.com/docs/api/shipments/list/
SHIPMENT_LIST_PARAMETERS = (
    "recipient_name",
    "recipient_country_code",
    "order_number",
    "order_id",
    "carrier_code",
    "service_code",
    "tracking_number",
    "create_date_start",
    "create_date_end",
    "ship_date_start",
    "ship_date_end",
    "void_date_start",
    "void_date_end",
    "store_id",
    "include_shipment_items",
    "sort_by",
    "sort_dir",
    "page",
    "page_size",
)

# https://www.shipstation.com/docs/api/shipments/create-label/
CREATE_SHIPMENT_LABEL_OPTIONS = (
    "carrier_code",
    "service_code",
    "package_code",
    "confirmation",
    "ship_date",
    "weight",
    "dimensions",
    "ship_from",
    "ship_to",
    "insurance_options",
    "international_options",
    "advanced_options",
    "test_label",
)

# https://www.shipstation.com/docs/api/shipments/get-rates/
GET_RATE_OPTIONS = (
    "carrier_code",
    "from_postal_code",
    "to_state",
    "to_country",
    "to_postal_code",
    "weight",
    "service_code",
    "package_code",
    "to_city",
    "dimensions",
    "confirmation",
    "residential",
)

REQUIRED_RATE_OPTIONS = (
    "carrier_code",
    "from_postal_code",
    "to_country",
    "to_postal_code",
    "weight",
)

CREATE_WAREHOUSE_OPTIONS = (
    "warehouse_name",
    "origin_address",
    "return_address",
    "is_default",
)

WEIGHT_UNIT_OPTIONS = Literal["pounds", "ounces", "grams"]
DIMENSIONS_UNIT_OPTIONS = Literal["inches", "centimeters"]

# https://www.shipstation.com/docs/api/stores/update/
UPDATE_STORE_OPTIONS = (
    "store_id",
    "store_name",
    "marketplace_id",
    "marketplace_name",
    "account_name",
    "email",
    "integration_url",
    "active",
    "company_name",
    "phone",
    "public_email",
    "website",
    "refresh_date",
    "last_refresh_attempt",
    "create_date",
    "modify_date",
    "auto_refresh",
    "status_mappings",
)

# https://www.shipstation.com/docs/api/webhooks/subscribe/
SUBSCRIBE_TO_WEBHOOK_OPTIONS = ("target_url", "event", "store_id", "friendly_name")
SUBSCRIBE_TO_WEBHOOK_EVENT_OPTIONS = Literal[
    "ORDER_NOTIFY",
    "ITEM_ORDER_NOTIFY",
    "SHIP_NOTIFY",
    "ITEM_SHIP_NOTIFY",
    "FULFILLMENT_SHIPPED",
    "FULFILLMENT_REJECTED",
]

# https://www.shipstation.com/docs/api/models/international-options/
CONTENTS_VALUES = Literal[
    "merchandise", "documents", "gift", "returned_goods", "sample"
]
NON_DELIVERY_OPTIONS = Literal["return_to_sender", "treat_as_abandoned"]
