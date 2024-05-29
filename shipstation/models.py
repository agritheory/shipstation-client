import json
from datetime import date, datetime
from decimal import Decimal
from uuid import UUID

from attrs import define, field
from attrs.setters import frozen
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
    country_of_origin: str | None = None
    customs_item_id: str | None = field(default=None, on_setattr=frozen)
    description: str | None = None
    harmonized_tariff_code: str | None = None
    quantity: Decimal | None = None
    value: Decimal | None = None


@define(auto_attribs=True)
class ShipStationInsuranceOptions(ShipStationBase):
    provider: PROVIDER_VALUES | None = None
    insure_shipment: bool | None = None
    insured_value: Decimal | None = None


@define(auto_attribs=True)
class ShipStationInternationalOptions(ShipStationBase):
    customs_items: list[ShipStationCustomsItem] | None = None
    contents: CONTENTS_VALUES | None = None
    non_delivery: NON_DELIVERY_OPTIONS | None = None


@define(auto_attribs=True)
class ShipStationAdvancedOptions(ShipStationBase):
    bill_to_account: str | None = None
    bill_to_country_code: str | None = None
    bill_to_my_other_account: str | None = None
    bill_to_party: BILL_TO_PARTY_VALUES | None = None
    bill_to_postal_code: str | None = None
    contains_alcohol: bool | None = None
    custom_field1: str | None = None
    custom_field2: str | None = None
    custom_field3: str | None = None
    merged_ids: list[Decimal] | None = field(default=None, on_setattr=frozen)
    merged_or_split: bool | None = field(default=None, on_setattr=frozen)
    non_machinable: bool | None = None
    parent_id: Decimal | None = field(default=None, on_setattr=frozen)
    saturday_delivery: bool | None = None
    source: str | None = None
    store_id: Decimal | None = None
    warehouse_id: Decimal | None = None


@define(auto_attribs=True)
class ShipStationWeight(ShipStationBase):
    units: WEIGHT_UNIT_OPTIONS | None = None
    value: Decimal | None = None
    weight_units: Decimal | None = field(default=None, on_setattr=frozen)


@define(auto_attribs=True)
class ShipStationContainer(ShipStationBase):
    units: DIMENSIONS_UNIT_OPTIONS | None = None
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
    active: bool | None = None
    aliases: list[str] | None = None
    create_date: datetime | None = field(default=None, on_setattr=frozen)
    customs_country_code: str | None = None
    customs_description: str | None = None
    customs_tariff_no: str | None = None
    customs_value: Decimal | None = None
    default_carrier_code: str | None = None
    default_confirmation: str | None = None
    default_cost: Decimal | None = None
    default_intl_carrier_code: str | None = None
    default_intl_confirmation: str | None = None
    default_intl_package_code: str | None = None
    default_intl_service_code: str | None = None
    default_package_code: str | None = None
    default_service_code: str | None = None
    fulfillment_sku: str | None = None
    height: Decimal | None = None
    internal_notes: str | None = None
    length: Decimal | None = None
    modify_date: datetime | None = field(default=None, on_setattr=frozen)
    name: str | None = None
    no_customs: bool | None = None
    price: Decimal | None = None
    product_category: ShipStationProductCategory | None = None
    product_id: int | None = field(default=None, on_setattr=frozen)
    product_type: str | None = None
    sku: str | None = None
    tags: list[ShipStationProductTag] | None = None
    warehouse_location: str | None = None
    weight_oz: Decimal | None = None
    width: Decimal | None = None


@define(auto_attribs=True)
class ShipStationAddress(ShipStationBase):
    address_verified: ADDRESS_VERIFIED_VALUES | None = None
    city: str | None = None
    company: str | None = None
    country: str | None = None
    name: str | None = None
    phone: str | None = None
    postal_code: str | None = None
    residential: bool | None = None
    state: str | None = None
    street1: str | None = None
    street2: str | None = None
    street3: str | None = None


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
    name: str

    adjustment: bool | None = None
    create_date: datetime | None = field(default=None, on_setattr=frozen)
    fulfillment_sku: str | None = None
    image_url: str | None = None
    line_item_key: str | None = None
    modify_date: datetime | None = field(default=None, on_setattr=frozen)
    options: list[ShipStationItemOption] | None = None
    order_item_id: str | None = field(default=None, on_setattr=frozen)
    product_id: Decimal | None = None
    quantity: Decimal | None = None
    shipping_amount: Decimal | None = None
    sku: str | None = None
    tax_amount: Decimal | None = None
    unit_price: Decimal | None = None
    upc: str | None = None
    warehouse_location: str | None = None
    weight: ShipStationWeight | None = None


@define(auto_attribs=True)
class ShipStationOrder(ShipStationBase):
    advanced_options: ShipStationAdvancedOptions | None = None
    amount_paid: Decimal | None = None
    batch_number: str | None = None
    bill_to: ShipStationAddress | None = None
    carrier_code: str | None = None
    confirmation: CONFIRMATION_VALUES | None = None
    create_date: datetime | None = field(default=None, on_setattr=frozen)
    customer_email: str | None = None
    customer_id: str | None = field(default=None, on_setattr=frozen)
    customer_notes: str | None = None
    customer_username: str | None = None
    dimensions: ShipStationContainer | None = None
    externally_fulfilled_by: str | None = field(default=None, on_setattr=frozen)
    externally_fulfilled: bool | None = field(default=None, on_setattr=frozen)
    form_data: str | None = None
    gift_message: str | None = None
    gift: bool | None = None
    hold_until_date: datetime | None = None
    insurance_cost: Decimal | None = None
    insurance_options: ShipStationInsuranceOptions | None = None
    internal_notes: str | None = None
    international_options: ShipStationInternationalOptions | None = None
    is_return_label: bool | None = None
    items: list[ShipStationOrderItem] | None = None
    label_data: str | None = None
    label_messages: str | None = None
    marketplace_notified: bool | None = None
    modify_date: datetime | None = field(default=None, on_setattr=frozen)
    notify_error_message: bool | None = None
    order_date: datetime | None = None
    order_id: str | None = field(default=None, on_setattr=frozen)
    order_key: str | None = None
    order_number: str | None = None
    order_status: ORDER_STATUS_VALUES | None = None
    order_total: Decimal | None = field(default=None, on_setattr=frozen)
    package_code: str | None = None
    payment_date: datetime | None = None
    payment_method: str | None = None
    requested_shipping_service: str | None = None
    service_code: str | None = None
    ship_by_date: datetime | None = None
    ship_date: datetime | None = None
    ship_to: ShipStationAddress | None = None
    shipment_cost: Decimal | None = None
    shipment_id: str | None = None
    shipment_items: str | None = None
    shipping_amount: Decimal | None = None
    tag_ids: list[int] | None = None
    tax_amount: Decimal | None = None
    test_label: bool | None = None
    tracking_number: str | None = None
    user_id: str | None = field(default=None, on_setattr=frozen)
    void_date: datetime | None = None
    voided: bool | None = None
    warehouse_id: str | None = None
    weight: ShipStationWeight | None = None


@define(auto_attribs=True)
class ShipStationStatusMapping(ShipStationBase):
    order_status: str | None = None
    status_key: str | None = None


@define(auto_attribs=True)
class ShipStationStore(ShipStationBase):
    account_name: str | None = None
    active: bool | None = None
    auto_refresh: bool | None = None
    company_name: str | None = None
    create_date: date | None = None
    email: str | None = None
    integration_url: str | None = None
    last_refresh_attempt: date | None = None
    marketplace_id: str | None = None
    marketplace_name: str | None = None
    modify_date: date | None = None
    phone: str | None = None
    public_email: str | None = None
    refresh_date: date | None = None
    status_mappings: list[ShipStationStatusMapping] | None = None
    store_id: str | None = None
    store_name: str | None = None
    website: str | None = None


@define(auto_attribs=True)
class ShipStationWarehouse(ShipStationBase):
    create_date: date | None = None
    ext_inventory_identity: str | None = None
    is_default: bool | None = None
    origin_address: ShipStationAddress | None = None
    register_fedex_meter: bool | None = None
    return_address: ShipStationAddress | None = None
    seller_integration_id: str | None = None
    warehouse_id: str | None = None
    warehouse_name: str | None = None


@define(auto_attribs=True)
class ShipStationWebhook(ShipStationBase):
    active: bool | None = None
    bulk_copy_batch_id: str | None = None
    bulk_copy_record_id: str | None = None
    event: str | None = None
    friendly_name: str | None = None
    hook_type: str | None = None
    is_label_apihook: bool | None = None
    message_format: str | None = None
    name: str | None = None
    resource_type: SUBSCRIBE_TO_WEBHOOK_EVENT_OPTIONS | None = None
    resource_url: str | None = None
    seller_id: str | None = None
    seller: str | None = None
    store_id: str | None = None
    target_url: str | None = None
    url: str | None = None
    web_hook_id: str | None = None
    webhook_logs: str | None = None

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
    address_verified: str | None = None
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
    carrier_code: str | None = None
    create_date: datetime | None = None
    customer_email: str | None = None
    delivery_date: datetime | None = None
    fulfillment_fee: Decimal | None = None
    fulfillment_id: str | None = None
    fulfillment_provider_code: str | None = None
    fulfillment_service_code: str | None = None
    marketplace_notified: bool | None = None
    notify_error_message: str | None = None
    order_id: str | None = None
    order_number: str | None = None
    ship_date: datetime | None = None
    ship_to: ShipStationAddress | None = None
    tracking_number: str | None = None
    user_id: UUID | None = None
    void_date: datetime | None = None
    void_requested: bool | None = None
    voided: bool | None = None


@define(auto_attribs=True)
class ShipStationRateOptions(ShipStationBase):
    carrier_code: str | None = None
    confirmation: str | None = None
    dimensions: ShipStationContainer | None = None
    from_postal_code: str | None = None
    package_code: str | None = None
    residential: bool | None = None
    service_code: str | None = None
    to_city: str | None = None
    to_country: str | None = None
    to_postal_code: str | None = None
    to_state: str | None = None
    weight: ShipStationWeight | None = None


@define(auto_attribs=True)
class ShipStationRate(ShipStationBase):
    other_cost: Decimal | None = None
    service_code: str | None = None
    service_name: str | None = None
    shipment_cost: Decimal | None = None
