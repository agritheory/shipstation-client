import json
import typing
from datetime import date, datetime
from decimal import Decimal
from uuid import UUID

from attr import attrib, attrs

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


@attrs(auto_attribs=True)
class ShipStationCustomsItem(ShipStationBase):
    customs_item_id: typing.Optional[str] = None
    description: typing.Optional[str] = None
    quantity: typing.Optional[Decimal] = None
    value: typing.Optional[Decimal] = None
    harmonized_tariff_code: typing.Optional[str] = None
    country_of_origin: typing.Optional[str] = None


@attrs(auto_attribs=True)
class ShipStationInsuranceOptions(ShipStationBase):
    provider: typing.Optional[str] = None
    insure_shipment: typing.Optional[bool] = None
    insured_value: typing.Optional[Decimal] = None


@attrs(auto_attribs=True)
class ShipStationInternationalOptions(ShipStationBase):
    customs_items: typing.Optional[typing.List[ShipStationCustomsItem]] = None
    contents: typing.Optional[str] = None
    non_delivery: typing.Optional[str] = None


@attrs(auto_attribs=True)
class ShipStationAdvancedOptions(ShipStationBase):
    warehouse_id: typing.Optional[str] = None
    non_machinable: typing.Optional[bool] = None
    saturday_delivery: typing.Optional[str] = None
    contains_alcohol: typing.Optional[str] = None
    store_id: typing.Optional[str] = None
    custom_field1: typing.Optional[str] = None
    custom_field2: typing.Optional[str] = None
    custom_field3: typing.Optional[str] = None
    source: typing.Optional[str] = None
    merged_or_split: typing.Optional[str] = None
    merged_ids: typing.Optional[typing.List[str]] = None
    bill_to_party: typing.Optional[str] = None
    bill_to_account: typing.Optional[str] = None
    bill_to_postal_code: typing.Optional[str] = None
    bill_to_country_code: typing.Optional[str] = None
    bill_to_my_other_account: typing.Optional[bool] = None
    parent_id: typing.Optional[str] = None


@attrs(auto_attribs=True)
class ShipStationWeight(ShipStationBase):
    units: typing.Optional[str] = None
    value: typing.Optional[Decimal] = None
    weight_units: typing.Optional[str] = None


@attrs(auto_attribs=True)
class ShipStationContainer(ShipStationBase):
    units: typing.Optional[str] = None
    length: typing.Optional[Decimal] = None
    width: typing.Optional[Decimal] = None
    height: typing.Optional[Decimal] = None
    _weight: typing.Optional[ShipStationWeight] = None

    @property
    def weight(self) -> typing.Optional[ShipStationWeight]:
        if self._weight:
            return self._weight if self._weight.value else None
        return None

    @weight.setter
    def weight(self, val: ShipStationWeight) -> None:
        self.require_type(val, ShipStationWeight)
        self._weight = ShipStationWeight(**val)


@attrs(auto_attribs=True)
class ShipStationProductTag(ShipStationBase):
    tag_id: typing.Optional[int] = None
    name: typing.Optional[str] = None


@attrs(auto_attribs=True)
class ShipStationProductCategory(ShipStationBase):
    category_id: typing.Optional[int] = None
    name: typing.Optional[str] = None


@attrs(auto_attribs=True)
class ShipStationItem(ShipStationBase):
    aliases: typing.Optional[typing.List[str]] = None
    product_id: typing.Optional[int] = None
    sku: typing.Optional[str] = None
    name: typing.Optional[str] = None
    price: typing.Optional[Decimal] = None
    default_cost: typing.Optional[Decimal] = None
    length: typing.Optional[Decimal] = None
    width: typing.Optional[Decimal] = None
    height: typing.Optional[Decimal] = None
    weight_oz: typing.Optional[Decimal] = None
    internal_notes: typing.Optional[str] = None
    fulfillment_sku: typing.Optional[str] = None
    create_date: typing.Optional[datetime] = None
    modify_date: typing.Optional[datetime] = None
    active: typing.Optional[bool] = None
    product_category: typing.Optional[ShipStationProductCategory] = None
    product_type: typing.Optional[str] = None
    warehouse_location: typing.Optional[str] = None
    default_carrier_code: typing.Optional[str] = None
    default_service_code: typing.Optional[str] = None
    default_package_code: typing.Optional[str] = None
    default_intl_carrier_code: typing.Optional[str] = None
    default_intl_service_code: typing.Optional[str] = None
    default_intl_package_code: typing.Optional[str] = None
    default_confirmation: typing.Optional[str] = None
    default_intl_confirmation: typing.Optional[str] = None
    customs_description: typing.Optional[str] = None
    customs_value: typing.Optional[Decimal] = None
    customs_tariff_no: typing.Optional[str] = None
    customs_country_code: typing.Optional[str] = None
    no_customs: typing.Optional[bool] = None
    tags: typing.Optional[typing.List[ShipStationProductTag]] = None


@attrs(auto_attribs=True)
class ShipStationAddress(ShipStationBase):
    name: typing.Optional[str] = None
    company: typing.Optional[str] = None
    street1: typing.Optional[str] = None
    street2: typing.Optional[str] = None
    street3: typing.Optional[str] = None
    city: typing.Optional[str] = None
    state: typing.Optional[str] = None
    postal_code: typing.Optional[str] = None
    country: typing.Optional[str] = None
    phone: typing.Optional[str] = None
    residential: typing.Optional[bool] = None
    address_verified: typing.Optional[bool] = None


@attrs(auto_attribs=True)
class ShipStationOrderTag(ShipStationBase):
    tag_id: typing.Optional[int] = None
    name: typing.Optional[str] = None
    color: typing.Optional[str] = None


@attrs(auto_attribs=True)
class ShipStationItemOption(ShipStationBase):
    name: typing.Optional[str] = None
    value: typing.Optional[str] = None


@attrs(auto_attribs=True)
class ShipStationOrderItem(ShipStationBase):
    order_item_id: typing.Optional[str] = None
    line_item_key: typing.Optional[str] = None
    sku: typing.Optional[str] = None
    name: typing.Optional[str] = None
    image_url: typing.Optional[str] = None
    weight: typing.Optional[ShipStationWeight] = None
    quantity: typing.Optional[int] = None
    unit_price: typing.Optional[Decimal] = None
    tax_amount: typing.Optional[Decimal] = None
    shipping_amount: typing.Optional[Decimal] = None
    warehouse_location: typing.Optional[str] = None
    options: typing.Optional[typing.List[ShipStationItemOption]] = None
    productId: typing.Optional[str] = None
    fulfillment_sku: typing.Optional[str] = None
    adjustment: typing.Optional[bool] = None
    upc: typing.Optional[str] = None
    create_date: typing.Optional[datetime] = None
    modify_date: typing.Optional[datetime] = None


@attrs(auto_attribs=True)
class ShipStationOrder(ShipStationBase):
    # Required attributes
    order_number: typing.Optional[str] = None
    order_date: typing.Optional[datetime] = None
    order_status: typing.Optional[str] = None
    bill_to: typing.Optional[ShipStationAddress] = None
    ship_to: typing.Optional[ShipStationAddress] = None
    # Optional attributes
    order_key: typing.Optional[str] = None
    payment_date: typing.Optional[str] = None
    customer_username: typing.Optional[str] = None
    customer_email: typing.Optional[str] = None
    items: typing.Optional[typing.List[ShipStationOrderItem]] = None
    amount_paid: typing.Optional[Decimal] = None
    tax_amount: typing.Optional[Decimal] = None
    shipping_amount: typing.Optional[Decimal] = None
    customer_notes: typing.Optional[str] = None
    internal_notes: typing.Optional[str] = None
    gift: typing.Optional[bool] = None
    payment_method: typing.Optional[str] = None
    carrier_code: typing.Optional[str] = None
    service_code: typing.Optional[str] = None
    package_code: typing.Optional[str] = None
    confirmation: typing.Optional[str] = None
    ship_date: typing.Optional[datetime] = None
    dimensions: typing.Optional[ShipStationContainer] = None
    insurance_options: typing.Optional[ShipStationInsuranceOptions] = None
    international_options: typing.Optional[ShipStationInternationalOptions] = None
    advanced_options: typing.Optional[ShipStationAdvancedOptions] = None
    tracking_number: typing.Optional[str] = None
    voided: typing.Optional[bool] = None
    void_date: typing.Optional[datetime] = None
    order_id: typing.Optional[str] = None
    marketplace_notified: typing.Optional[bool] = None
    warehouse_id: typing.Optional[str] = None
    user_id: typing.Optional[str] = None
    label_data: typing.Optional[str] = None
    batch_number: typing.Optional[str] = None
    insurance_cost: typing.Optional[Decimal] = None
    form_data: typing.Optional[str] = None
    notify_error_message: typing.Optional[bool] = None
    is_return_label: typing.Optional[bool] = None
    shipment_id: typing.Optional[str] = None
    shipment_cost: typing.Optional[Decimal] = None
    weight: typing.Optional[ShipStationWeight] = None
    create_date: typing.Optional[datetime] = None
    modify_date: typing.Optional[datetime] = None
    shipment_items: typing.Optional[str] = None
    ship_by_date: typing.Optional[str] = None
    customer_id: typing.Optional[str] = None
    order_total: typing.Optional[Decimal] = None
    gift_message: typing.Optional[str] = None
    requested_shipping_service: typing.Optional[str] = None
    hold_until_date: typing.Optional[datetime] = None
    tag_ids: typing.Optional[typing.List[int]] = None
    externally_fulfilled: typing.Optional[bool] = None
    externally_fulfilled_by: typing.Optional[str] = None
    label_messages: typing.Optional[str] = None
    test_label: typing.Optional[bool] = None


@attrs(auto_attribs=True)
class ShipStationStatusMapping(ShipStationBase):
    order_status: typing.Optional[str] = None
    status_key: typing.Optional[str] = None


@attrs(auto_attribs=True)
class ShipStationStore(ShipStationBase):
    store_id: typing.Optional[str] = None
    store_name: typing.Optional[str] = None
    marketplace_id: typing.Optional[str] = None
    marketplace_name: typing.Optional[str] = None
    account_name: typing.Optional[str] = None
    email: typing.Optional[str] = None
    integration_url: typing.Optional[str] = None
    active: typing.Optional[bool] = None
    company_name: typing.Optional[str] = None
    phone: typing.Optional[str] = None
    public_email: typing.Optional[str] = None
    website: typing.Optional[str] = None
    refresh_date: typing.Optional[date] = None
    last_refresh_attempt: typing.Optional[date] = None
    create_date: typing.Optional[date] = None
    modify_date: typing.Optional[date] = None
    auto_refresh: typing.Optional[bool] = None
    status_mappings: typing.Optional[typing.List[ShipStationStatusMapping]] = None


@attrs(auto_attribs=True)
class ShipStationWarehouse(ShipStationBase):
    create_date: typing.Optional[date] = None
    ext_inventory_identity: typing.Optional[str] = None
    is_default: typing.Optional[bool] = None
    origin_address: typing.Optional[ShipStationAddress] = None
    return_address: typing.Optional[ShipStationAddress] = None
    register_fedex_meter: typing.Optional[bool] = None
    seller_integration_id: typing.Optional[str] = None
    warehouse_id: typing.Optional[str] = None
    warehouse_name: typing.Optional[str] = None


@attrs(auto_attribs=True)
class ShipStationWebhook(ShipStationBase):
    active: typing.Optional[bool] = None
    is_label_apihook: typing.Optional[bool] = None
    web_hook_id: typing.Optional[str] = None
    seller_id: typing.Optional[str] = None
    hook_type: typing.Optional[str] = None
    message_format: typing.Optional[str] = None
    url: typing.Optional[str] = None
    name: typing.Optional[str] = None
    bulk_copy_batch_id: typing.Optional[str] = None
    bulk_copy_record_id: typing.Optional[str] = None
    webhook_logs: typing.Optional[str] = None
    seller: typing.Optional[str] = None
    store_id: typing.Optional[str] = None
    target_url: typing.Optional[str] = None
    event: typing.Optional[str] = None
    friendly_name: typing.Optional[str] = None
    resource_url: typing.Optional[str] = None
    resource_type: typing.Optional[str] = None

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


@attrs(auto_attribs=True)
class ShipStationUser(ShipStationBase):
    name: typing.Optional[str] = None
    user_id: typing.Optional[UUID] = None
    user_name: typing.Optional[str] = None


@attrs(auto_attribs=True)
class ShipStationMarketplace(ShipStationBase):
    can_confirm_shipments: typing.Optional[bool] = None
    can_refresh: typing.Optional[bool] = None
    marketplace_id: typing.Optional[str] = None
    name: typing.Optional[str] = None
    supports_custom_mappings: typing.Optional[bool] = None
    supports_custom_statuses: typing.Optional[bool] = None


@attrs(auto_attribs=True)
class ShipStationMarketplaceUsername(ShipStationBase):
    create_date: typing.Optional[date] = None
    customer_id: typing.Optional[int] = None
    customer_user_id: typing.Optional[str] = None
    marketplace: typing.Optional[str] = None
    marketplace_id: typing.Optional[str] = None
    modify_date: typing.Optional[date] = None
    username: typing.Optional[str] = None


@attrs(auto_attribs=True)
class ShipStationCustomer(ShipStationBase):
    address_verified: typing.Optional[bool] = None
    city: typing.Optional[str] = None
    company: typing.Optional[str] = None
    country_code: typing.Optional[str] = None
    create_date: typing.Optional[date] = None
    customer_id: typing.Optional[int] = None
    email: typing.Optional[str] = None
    marketplace_usernames: typing.Optional[
        typing.List[ShipStationMarketplaceUsername]
    ] = None
    modify_date: typing.Optional[date] = None
    name: typing.Optional[str] = None
    phone: typing.Optional[str] = None
    postal_code: typing.Optional[str] = None
    state: typing.Optional[str] = None
    street1: typing.Optional[str] = None
    street2: typing.Optional[str] = None
    tags: typing.Optional[typing.List[typing.Any]] = None


@attrs(auto_attribs=True)
class ShipStationCarrier(ShipStationBase):
    account_number: typing.Optional[str] = None
    balance: typing.Optional[Decimal] = None
    code: typing.Optional[str] = None
    name: typing.Optional[str] = None
    nickname: typing.Optional[str] = None
    primary: typing.Optional[bool] = None
    requires_funded_account: typing.Optional[bool] = None
    shipping_provider_id: typing.Optional[str] = None


@attrs(auto_attribs=True)
class ShipStationCarrierPackage(ShipStationBase):
    carrier_code: typing.Optional[str] = None
    code: typing.Optional[str] = None
    domestic: typing.Optional[bool] = None
    international: typing.Optional[bool] = None
    name: typing.Optional[str] = None


@attrs(auto_attribs=True)
class ShipStationCarrierService(ShipStationBase):
    carrier_code: typing.Optional[str] = None
    code: typing.Optional[str] = None
    domestic: typing.Optional[bool] = None
    international: typing.Optional[bool] = None
    name: typing.Optional[str] = None


@attrs(auto_attribs=True)
class ShipStationFulfillment(ShipStationBase):
    fulfillment_id: typing.Optional[str] = None
    order_id: typing.Optional[str] = None
    order_number: typing.Optional[str] = None
    user_id: typing.Optional[UUID] = None
    customer_email: typing.Optional[str] = None
    tracking_number: typing.Optional[str] = None
    create_date: typing.Optional[datetime] = None
    ship_date: typing.Optional[datetime] = None
    void_date: typing.Optional[datetime] = None
    delivery_date: typing.Optional[datetime] = None
    carrier_code: typing.Optional[str] = None
    fulfillment_provider_code: typing.Optional[str] = None
    fulfillment_service_code: typing.Optional[str] = None
    fulfillment_fee: typing.Optional[Decimal] = None
    void_requested: typing.Optional[bool] = None
    voided: typing.Optional[bool] = None
    marketplace_notified: typing.Optional[bool] = None
    notify_error_message: typing.Optional[str] = None
    ship_to: typing.Optional[ShipStationAddress] = None


@attrs(auto_attribs=True)
class ShipStationRateOptions(ShipStationBase):
    carrier_code: typing.Optional[str] = None
    service_code: typing.Optional[str] = None
    package_code: typing.Optional[str] = None
    from_postal_code: typing.Optional[str] = None
    to_state: typing.Optional[str] = None
    to_country: typing.Optional[str] = None
    to_postal_code: typing.Optional[str] = None
    to_city: typing.Optional[str] = None
    weight: typing.Optional[ShipStationWeight] = None
    dimensions: typing.Optional[ShipStationContainer] = None
    confirmation: typing.Optional[str] = None
    residential: typing.Optional[bool] = None


@attrs(auto_attribs=True)
class ShipStationRate(ShipStationBase):
    other_cost: typing.Optional[Decimal] = None
    service_code: typing.Optional[str] = None
    service_name: typing.Optional[str] = None
    shipment_cost: typing.Optional[Decimal] = None
