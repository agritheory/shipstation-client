import json
from datetime import date, datetime
from decimal import Decimal
from uuid import UUID

from attrs import define
from shipstation.base import ShipStationBase
from shipstation.constants import *

__all__ = [
    "ShipStationAddress",
    "ShipStationAdvancedOptions",
    "ShipStationCarrier",
    "ShipStationCarrierPackage",
    "ShipStationCarrierService",
    "ShipStationContainer",
    "ShipStationCustomsItem",
    "ShipStationCustomer",
    "ShipStationFulfillment",
    "ShipStationInsuranceOptions",
    "ShipStationInternationalOptions",
    "ShipStationItem",
    "ShipStationMarketplace",
    "ShipStationOrder",
    "ShipStationOrderItem",
    "ShipStationOrderTag",
    "ShipStationProductCategory",
    "ShipStationProductTag",
    "ShipStationRate",
    "ShipStationRateOptions",
    "ShipStationStatusMapping",
    "ShipStationStore",
    "ShipStationUser",
    "ShipStationWarehouse",
    "ShipStationWebhook",
    "ShipStationWeight",
]


@define(auto_attribs=True)
class ShipStationCustomsItem(ShipStationBase):
    customs_item_id: str | None = None
    description: str | None = None
    quantity: Decimal | None = None
    value: Decimal | None = None
    harmonized_tariff_code: str | None = None
    country_of_origin: str | None = None


@define(auto_attribs=True)
class ShipStationInsuranceOptions(ShipStationBase):
    provider: str | None = None
    insure_shipment: bool | None = None
    insured_value: Decimal | None = None


@define(auto_attribs=True)
class ShipStationInternationalOptions(ShipStationBase):
    customs_items: list[ShipStationCustomsItem] | None = None
    contents: str | None = None
    non_delivery: str | None = None


@define(auto_attribs=True)
class ShipStationAdvancedOptions(ShipStationBase):
    warehouse_id: str | None = None
    non_machinable: bool | None = None
    saturday_delivery: str | None = None
    contains_alcohol: str | None = None
    store_id: str | None = None
    custom_field1: str | None = None
    custom_field2: str | None = None
    custom_field3: str | None = None
    source: str | None = None
    merged_or_split: str | None = None
    merged_ids: list[str] | None = None
    bill_to_party: str | None = None
    bill_to_account: str | None = None
    bill_to_postal_code: str | None = None
    bill_to_country_code: str | None = None
    bill_to_my_other_account: bool | None = None
    parent_id: str | None = None


@define(auto_attribs=True)
class ShipStationWeight(ShipStationBase):
    units: str | None = None
    value: Decimal | None = None
    weight_units: str | None = None


@define(auto_attribs=True)
class ShipStationContainer(ShipStationBase):
    units: str | None = None
    length: Decimal | None = None
    width: Decimal | None = None
    height: Decimal | None = None
    _weight: ShipStationWeight | None = None

    @property
    def weight(self) -> ShipStationWeight | None:
        if self._weight:
            return self._weight if self._weight.value else None
        return None

    @weight.setter
    def weight(self, val: ShipStationWeight) -> None:
        self.require_type(val, ShipStationWeight)
        self._weight = ShipStationWeight(**val)


@define(auto_attribs=True)
class ShipStationProductTag(ShipStationBase):
    tag_id: int | None = None
    name: str | None = None


@define(auto_attribs=True)
class ShipStationProductCategory(ShipStationBase):
    category_id: int | None = None
    name: str | None = None


@define(auto_attribs=True)
class ShipStationItem(ShipStationBase):
    aliases: list[str] | None = None
    product_id: int | None = None
    sku: str | None = None
    name: str | None = None
    price: Decimal | None = None
    default_cost: Decimal | None = None
    length: Decimal | None = None
    width: Decimal | None = None
    height: Decimal | None = None
    weight_oz: Decimal | None = None
    internal_notes: str | None = None
    fulfillment_sku: str | None = None
    create_date: datetime | None = None
    modify_date: datetime | None = None
    active: bool | None = None
    product_category: ShipStationProductCategory | None = None
    product_type: str | None = None
    warehouse_location: str | None = None
    default_carrier_code: str | None = None
    default_service_code: str | None = None
    default_package_code: str | None = None
    default_intl_carrier_code: str | None = None
    default_intl_service_code: str | None = None
    default_intl_package_code: str | None = None
    default_confirmation: str | None = None
    default_intl_confirmation: str | None = None
    customs_description: str | None = None
    customs_value: Decimal | None = None
    customs_tariff_no: str | None = None
    customs_country_code: str | None = None
    no_customs: bool | None = None
    tags: list[ShipStationProductTag] | None = None


@define(auto_attribs=True)
class ShipStationAddress(ShipStationBase):
    name: str | None = None
    company: str | None = None
    street1: str | None = None
    street2: str | None = None
    street3: str | None = None
    city: str | None = None
    state: str | None = None
    postal_code: str | None = None
    country: str | None = None
    phone: str | None = None
    residential: bool | None = None
    address_verified: bool | None = None


@define(auto_attribs=True)
class ShipStationOrderTag(ShipStationBase):
    tag_id: int | None = None
    name: str | None = None
    color: str | None = None


@define(auto_attribs=True)
class ShipStationItemOption(ShipStationBase):
    name: str | None = None
    value: str | None = None


@define(auto_attribs=True)
class ShipStationOrderItem(ShipStationBase):
    order_item_id: str | None = None
    line_item_key: str | None = None
    sku: str | None = None
    name: str | None = None
    image_url: str | None = None
    weight: ShipStationWeight | None = None
    quantity: int | None = None
    unit_price: Decimal | None = None
    tax_amount: Decimal | None = None
    shipping_amount: Decimal | None = None
    warehouse_location: str | None = None
    options: list[ShipStationItemOption] | None = None
    productId: str | None = None
    fulfillment_sku: str | None = None
    adjustment: bool | None = None
    upc: str | None = None
    create_date: datetime | None = None
    modify_date: datetime | None = None


@define(auto_attribs=True)
class ShipStationOrder(ShipStationBase):
    # Required attributes
    order_number: str | None = None
    order_date: datetime | None = None
    order_status: str | None = None
    bill_to: ShipStationAddress | None = None
    ship_to: ShipStationAddress | None = None
    # Optional attributes
    order_key: str | None = None
    payment_date: str | None = None
    customer_username: str | None = None
    customer_email: str | None = None
    items: list[ShipStationOrderItem] | None = None
    amount_paid: Decimal | None = None
    tax_amount: Decimal | None = None
    shipping_amount: Decimal | None = None
    customer_notes: str | None = None
    internal_notes: str | None = None
    gift: bool | None = None
    payment_method: str | None = None
    carrier_code: str | None = None
    service_code: str | None = None
    package_code: str | None = None
    confirmation: str | None = None
    ship_date: datetime | None = None
    dimensions: ShipStationContainer | None = None
    insurance_options: ShipStationInsuranceOptions | None = None
    international_options: ShipStationInternationalOptions | None = None
    advanced_options: ShipStationAdvancedOptions | None = None
    tracking_number: str | None = None
    voided: bool | None = None
    void_date: datetime | None = None
    order_id: str | None = None
    marketplace_notified: bool | None = None
    warehouse_id: str | None = None
    user_id: str | None = None
    label_data: str | None = None
    batch_number: str | None = None
    insurance_cost: Decimal | None = None
    form_data: str | None = None
    notify_error_message: bool | None = None
    is_return_label: bool | None = None
    shipment_id: str | None = None
    shipment_cost: Decimal | None = None
    weight: ShipStationWeight | None = None
    create_date: datetime | None = None
    modify_date: datetime | None = None
    shipment_items: str | None = None
    ship_by_date: str | None = None
    customer_id: str | None = None
    order_total: Decimal | None = None
    gift_message: str | None = None
    requested_shipping_service: str | None = None
    hold_until_date: datetime | None = None
    tag_ids: list[int] | None = None
    externally_fulfilled: bool | None = None
    externally_fulfilled_by: str | None = None
    label_messages: str | None = None
    test_label: bool | None = None


@define(auto_attribs=True)
class ShipStationStatusMapping(ShipStationBase):
    order_status: str | None = None
    status_key: str | None = None


@define(auto_attribs=True)
class ShipStationStore(ShipStationBase):
    store_id: str | None = None
    store_name: str | None = None
    marketplace_id: str | None = None
    marketplace_name: str | None = None
    account_name: str | None = None
    email: str | None = None
    integration_url: str | None = None
    active: bool | None = None
    company_name: str | None = None
    phone: str | None = None
    public_email: str | None = None
    website: str | None = None
    refresh_date: date | None = None
    last_refresh_attempt: date | None = None
    create_date: date | None = None
    modify_date: date | None = None
    auto_refresh: bool | None = None
    status_mappings: list[ShipStationStatusMapping] | None = None


@define(auto_attribs=True)
class ShipStationWarehouse(ShipStationBase):
    create_date: date | None = None
    ext_inventory_identity: str | None = None
    is_default: bool | None = None
    origin_address: ShipStationAddress | None = None
    return_address: ShipStationAddress | None = None
    register_fedex_meter: bool | None = None
    seller_integration_id: str | None = None
    warehouse_id: str | None = None
    warehouse_name: str | None = None


@define(auto_attribs=True)
class ShipStationWebhook(ShipStationBase):
    active: bool | None = None
    is_label_apihook: bool | None = None
    web_hook_id: str | None = None
    seller_id: str | None = None
    hook_type: str | None = None
    message_format: str | None = None
    url: str | None = None
    name: str | None = None
    bulk_copy_batch_id: str | None = None
    bulk_copy_record_id: str | None = None
    webhook_logs: str | None = None
    seller: str | None = None
    store_id: str | None = None
    target_url: str | None = None
    event: str | None = None
    friendly_name: str | None = None
    resource_url: str | None = None
    resource_type: str | None = None

    # this doesn't use the typical .json() method so as to not convert it to camel case
    def prepare(self) -> str:
        return json.dumps(
            {
                "target_url": self.target_url,
                "event": self.event,
                "store_id": self.store_id,
                "friendly_name": self.friendly_name,
            }
        )


@define(auto_attribs=True)
class ShipStationUser(ShipStationBase):
    name: str | None = None
    user_id: UUID | None = None
    user_name: str | None = None


@define(auto_attribs=True)
class ShipStationMarketplace(ShipStationBase):
    can_confirm_shipments: bool | None = None
    can_refresh: bool | None = None
    marketplace_id: str | None = None
    name: str | None = None
    supports_custom_mappings: bool | None = None
    supports_custom_statuses: bool | None = None


@define(auto_attribs=True)
class ShipStationMarketplaceUsername(ShipStationBase):
    create_date: date | None = None
    customer_id: int | None = None
    customer_user_id: str | None = None
    marketplace: str | None = None
    marketplace_id: str | None = None
    modify_date: date | None = None
    username: str | None = None


@define(auto_attribs=True)
class ShipStationCustomer(ShipStationBase):
    address_verified: bool | None = None
    city: str | None = None
    company: str | None = None
    country_code: str | None = None
    create_date: date | None = None
    customer_id: int | None = None
    email: str | None = None
    marketplace_usernames: None | (list[ShipStationMarketplaceUsername]) = None
    modify_date: date | None = None
    name: str | None = None
    phone: str | None = None
    postal_code: str | None = None
    state: str | None = None
    street1: str | None = None
    street2: str | None = None
    tags: list | None = None


@define(auto_attribs=True)
class ShipStationCarrier(ShipStationBase):
    account_number: str | None = None
    balance: Decimal | None = None
    code: str | None = None
    name: str | None = None
    nickname: str | None = None
    primary: bool | None = None
    requires_funded_account: bool | None = None
    shipping_provider_id: str | None = None


@define(auto_attribs=True)
class ShipStationCarrierPackage(ShipStationBase):
    carrier_code: str | None = None
    code: str | None = None
    domestic: bool | None = None
    international: bool | None = None
    name: str | None = None


@define(auto_attribs=True)
class ShipStationCarrierService(ShipStationBase):
    carrier_code: str | None = None
    code: str | None = None
    domestic: bool | None = None
    international: bool | None = None
    name: str | None = None


@define(auto_attribs=True)
class ShipStationFulfillment(ShipStationBase):
    fulfillment_id: str | None = None
    order_id: str | None = None
    order_number: str | None = None
    user_id: UUID | None = None
    customer_email: str | None = None
    tracking_number: str | None = None
    create_date: datetime | None = None
    ship_date: datetime | None = None
    void_date: datetime | None = None
    delivery_date: datetime | None = None
    carrier_code: str | None = None
    fulfillment_provider_code: str | None = None
    fulfillment_service_code: str | None = None
    fulfillment_fee: Decimal | None = None
    void_requested: bool | None = None
    voided: bool | None = None
    marketplace_notified: bool | None = None
    notify_error_message: str | None = None
    ship_to: ShipStationAddress | None = None


@define(auto_attribs=True)
class ShipStationRateOptions(ShipStationBase):
    carrier_code: str | None = None
    service_code: str | None = None
    package_code: str | None = None
    from_postal_code: str | None = None
    to_state: str | None = None
    to_country: str | None = None
    to_postal_code: str | None = None
    to_city: str | None = None
    weight: ShipStationWeight | None = None
    dimensions: ShipStationContainer | None = None
    confirmation: str | None = None
    residential: bool | None = None


@define(auto_attribs=True)
class ShipStationRate(ShipStationBase):
    other_cost: Decimal | None = None
    service_code: str | None = None
    service_name: str | None = None
    shipment_cost: Decimal | None = None
