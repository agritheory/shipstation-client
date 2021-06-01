list_tags = '[{"color": "#FFFFFF", "name": "Amazon Prime Order", "tagId": 12345}]'

list_marketplaces = """
    [
    {
    "canConfirmShipments":true,
    "canRefresh":true,
    "marketplaceId":23,
    "name":"3dcart",
    "supportsCustomMappings":true,
    "supportsCustomStatuses":false
    },
    {
    "canConfirmShipments":true,
    "canRefresh":true,
    "marketplaceId":115,
    "name":"Acumatica",
    "supportsCustomMappings":false,
    "supportsCustomStatuses":true
    }
    ]
    """

list_stores = """
    [
    {
    "accountName":"ABC123456789",
    "active":true,
    "autoRefresh":true,
    "companyName":"411Seasons",
    "createDate":"2017-03-01T13:57:49.033",
    "email":"",
    "integrationUrl":"",
    "lastRefreshAttempt":"2020-06-23T11:56:51.627",
    "marketplaceId":2,
    "marketplaceName":"Amazon",
    "modifyDate":"2017-05-15T07:28:54.357",
    "phone":"",
    "publicEmail":"",
    "refreshDate":"2020-06-23T11:56:51.377",
    "statusMappings":"",
    "storeId": 34567,
    "storeName":"Mexico Amazon Store",
    "website":""
    },
    {
    "accountName":"DEF123456789",
    "active":true,
    "autoRefresh":true,
    "companyName":"",
    "createDate":"2017-01-25T14:38:33.793",
    "email":"",
    "integrationUrl":"",
    "lastRefreshAttempt":"2020-06-23T07:12:32.217",
    "marketplaceId":2,
    "marketplaceName":"Amazon",
    "modifyDate":"2017-01-25T14:39:25.003",
    "phone":"",
    "publicEmail":"",
    "refreshDate":"2020-06-23T07:12:31.95",
    "statusMappings":"",
    "storeId":23456,
    "storeName":"CA Amazon Store",
    "website":""
    },
    {
    "accountName":"GHI123456789",
    "active":true,
    "autoRefresh":true,
    "companyName":"",
    "createDate":"2017-01-23T13:55:39.643",
    "email":"",
    "integrationUrl":"",
    "lastRefreshAttempt":"2020-06-23T11:43:20.947",
    "marketplaceId":2,
    "marketplaceName":"Amazon",
    "modifyDate":"2018-06-05T06:48:42.98",
    "phone":"",
    "publicEmail":"",
    "refreshDate":"2020-06-23T11:43:20.713",
    "statusMappings":"",
    "storeId": 12345,
    "storeName":"US Amazon Store",
    "website":""
    }
    ]
    """


get_store = """
    {
    "accountName":"GHI123456789",
    "active":true,
    "autoRefresh":true,
    "companyName":"",
    "createDate":"2017-01-23T13:55:39.643",
    "email":"",
    "integrationUrl":"",
    "lastRefreshAttempt":"2020-06-23T11:43:20.947",
    "marketplaceId":2,
    "marketplaceName":"Amazon",
    "modifyDate":"2018-06-05T06:48:42.98",
    "phone":"",
    "publicEmail":"",
    "refreshDate":"2020-06-23T11:43:20.713",
    "statusMappings":"",
    "storeId": 12345,
    "storeName":"US Amazon Store",
    "website":""
    }
    """

list_users = """
    [
    {
    "name": "Merchandising",
    "userId": "57f4e49d-777e-4708-8b26-fd836fc975e6",
    "userName": "merchandising@example.com"
    },
    {
    "name": "Marketing",
    "userId": "0dbc3f54-5cd4-4054-b2b5-92427e18d6cd",
    "userName": "marketing@example.com"
    }
    ]
    """


list_warehouses = """
    [
    {
    "createDate":"2020-04-07T12:03:46.4000000",
    "extInventoryIdentity":"",
    "isDefault":false,
    "originAddress":
    {
    "addressVerified":"",
    "city":"Anywhere",
    "company":"",
    "country":"US",
    "name":"Warehouse 1",
    "phone":"18005551234",
    "postalCode":"12345",
    "residential":false,
    "state":"WA",
    "street1":"123 Long St",
    "street2":"Unit 4",
    "street3":""
    },
    "registerFedexMeter":"",
    "returnAddress":
    {
    "addressVerified":"",
    "city":"Anywhere",
    "company":"Test Company",
    "country":"US",
    "name":"",
    "phone":"18005553214",
    "postalCode":"23456",
    "residential":"",
    "state":"ID",
    "street1":"0 Short St",
    "street2":"",
    "street3":""
    },
    "sellerIntegrationId":"",
    "warehouseId":456789,
    "warehouseName":"Test Company"
    },
    {
    "createDate":"2015-10-23T10:03:36.3130000",
    "extInventoryIdentity":"",
    "isDefault":false,
    "originAddress":
    {
    "addressVerified":"",
    "city":"Big City",
    "company":"Another LLC",
    "country":"US",
    "name":"Virtual Warehouse",
    "phone":"5555555555",
    "postalCode":"98765",
    "residential":false,
    "state":"OR",
    "street1":"150000000 900th Street SE",
    "street2":"Suite C",
    "street3":""
    },
    "registerFedexMeter":"",
    "returnAddress":
    {
    "addressVerified":"",
    "city":"Big City",
    "company":"Another LLC",
    "country":"US",
    "name":"Virtual Warehouse",
    "phone":"5555555555",
    "postalCode":"98765",
    "residential":false,
    "state":"OR",
    "street1":"150000000 900th Street SE",
    "street2":"Suite C",
    "street3":""
    },
    "sellerIntegrationId":"",
    "warehouseId":123456,
    "warehouseName":"Another LLC Warehouse"
    }
    ]
    """


list_webhooks = """{"webhooks": []}"""


list_carriers = """
    [
    {
    "accountNumber": "abc123456789",
    "balance": 15.01,
    "code": "stamps_com",
    "name": "Stamps.com",
    "nickname": "",
    "primary": true,
    "requiresFundedAccount": true,
    "shippingProviderId": 35725
    },
    {
    "accountNumber": "36598-7894",
    "balance": 0.21,
    "code": "ups",
    "name": "UPS",
    "nickname": "UPS",
    "primary": true,
    "requiresFundedAccount": false,
    "shippingProviderId": 57765
    }
    ]
    """


list_services = """
    [
    {
    "carrierCode": "stamps_com",
    "code": "usps_first_class_mail",
    "domestic": true,
    "international": false,
    "name": "USPS First Class Mail"
    },
    {
    "carrierCode": "stamps_com",
    "code": "usps_media_mail",
    "domestic": true,
    "international": false,
    "name": "USPS Media Mail"
    },
    {
    "carrierCode": "stamps_com",
    "code": "usps_parcel_select",
    "domestic": true,
    "international": false,
    "name": "USPS Parcel Select Ground"
    }
    ]
    """


list_packages = """
    [
    {
    "carrierCode": "stamps_com",
    "code": "package",
    "domestic": true,
    "international": true,
    "name": "Package"
    },
    {
    "carrierCode": "stamps_com",
    "code": "flat_rate_envelope",
    "domestic": true,
    "international": true,
    "name": "Flat Rate Envelope"
    }
    ]
    """


list_customers = """
    {"customers":
    [
    {
    "addressVerified": "Verified",
    "city": "BIG TOWN",
    "company": "",
    "countryCode": "US",
    "createDate": "2017-12-16T18:49:16.0070000",
    "customerId": 123456789,
    "email": "yep@example.com",
    "marketplaceUsernames":
    [
    {
    "createDate": "2017-12-16T18:49:16.0200000",
    "customerId": 123456789,
    "customerUserId": 123456789,
    "marketplace": "Amazon",
    "marketplaceId": 2,
    "modifyDate": "2017-12-16T18:49:16.0200000",
    "username": "yep@example.com"
    }
    ],
    "modifyDate": "2017-12-16T18:49:16.0070000",
    "name": "Yep Example",
    "phone": "",
    "postalCode": "99999-1234",
    "state": "FL",
    "street1": "1 E 1ST ST",
    "street2": "",
    "tags": ""
    },
    {
    "addressVerified": "Verified",
    "city": "KEY WEST",
    "company": "",
    "countryCode": "US",
    "createDate": "2017-05-26T06:12:02.6230000",
    "customerId": 987654321,
    "email": "nope@yahoo.com",
    "marketplaceUsernames":
    [
    {
    "createDate": "2017-05-26T06:12:02.6400000",
    "customerId": 987654321,
    "customerUserId": 987654321,
    "marketplace": "Amazon",
    "marketplaceId": 2,
    "modifyDate": "2017-05-26T06:12:02.6400000",
    "username": "nope@yahoo.com"
    }
    ],
    "modifyDate": "2017-05-26T06:12:02.6230000",
    "name": "Arbitrary LLC",
    "phone": "123 568 1234",
    "postalCode": "99999-1234",
    "state": "FL",
    "street1": "6000 Beach St",
    "street2": "",
    "tags": ""
    }
    ]
    }
    """


get_carrier = """
    {
    "accountNumber": "example",
    "balance": 15.01,
    "code": "stamps_com",
    "name": "Stamps.com",
    "nickname": "",
    "primary": true,
    "requiresFundedAccount": true,
    "shippingProviderId": 35725
    }
    """

get_customer = """
{
    "addressVerified": "Verified",
    "city": "BIG TOWN",
    "company": "",
    "countryCode": "US",
    "createDate": "2017-12-16T18:49:16.0070000",
    "customerId": 123456789,
    "email": "yep@example.com",
    "marketplaceUsernames":
    [
    {
    "createDate": "2017-12-16T18:49:16.0200000",
    "customerId": 123456789,
    "customerUserId": 123456789,
    "marketplace": "Amazon",
    "marketplaceId": 2,
    "modifyDate": "2017-12-16T18:49:16.0200000",
    "username": "yep@example.com"
    }
    ],
    "modifyDate": "2017-12-16T18:49:16.0070000",
    "name": "Yep Example",
    "phone": "",
    "postalCode": "99999-1234",
    "state": "FL",
    "street1": "1 E 1ST ST",
    "street2": "",
    "tags": ""
}
"""

list_orders = """
{
    "orders": [
        {
            "advancedOptions": {
                "billToAccount": null,
                "billToCountryCode": null,
                "billToMyOtherAccount": null,
                "billToParty": null,
                "billToPostalCode": null,
                "containsAlcohol": false,
                "customField1": "EARLY BIRD SPECIAL",
                "customField2": "",
                "customField3": null,
                "mergedIds": [],
                "mergedOrSplit": false,
                "nonMachinable": false,
                "parentId": null,
                "saturdayDelivery": false,
                "source": "Manual Orders",
                "storeId": 12345,
                "warehouseId": 12345
            },
            "amountPaid": 0.0,
            "billTo": {
                "addressVerified": null,
                "city": null,
                "company": null,
                "country": null,
                "name": "Todd Ledet",
                "phone": null,
                "postalCode": null,
                "residential": null,
                "state": null,
                "street1": null,
                "street2": null,
                "street3": null
            },
            "carrierCode": "stamps_com",
            "confirmation": "none",
            "createDate": "2015-06-29T13:05:13.4930000",
            "customerEmail": "nope@example.com",
            "customerId": null,
            "customerNotes": null,
            "customerUsername": null,
            "dimensions": null,
            "externallyFulfilled": false,
            "externallyFulfilledBy": null,
            "gift": false,
            "giftMessage": null,
            "holdUntilDate": null,
            "insuranceOptions": {
                "insureShipment": false,
                "insuredValue": 0.0,
                "provider": null
            },
            "internalNotes": null,
            "internationalOptions": {
                "contents": null,
                "customsItems": null,
                "nonDelivery": null
            },
            "items": [],
            "labelMessages": null,
            "modifyDate": "2015-06-29T14:30:07.8970000",
            "orderDate": "2015-05-19T15:35:00.0000000",
            "orderId": 123456789,
            "orderKey": "123456789",
            "orderNumber": "123456789",
            "orderStatus": "shipped",
            "orderTotal": 7.0,
            "packageCode": "package",
            "paymentDate": "2015-06-29T13:05:13.4930000",
            "paymentMethod": null,
            "requestedShippingService": "USPS First Class Mail",
            "serviceCode": "usps_first_class_mail",
            "shipByDate": null,
            "shipDate": "2015-06-29",
            "shipTo": {
                "addressVerified": "Address validated successfully",
                "city": "ST MUNICIPALITY",
                "company": null,
                "country": "US",
                "name": "Todd Ledet",
                "phone": null,
                "postalCode": "12345-9876",
                "residential": true,
                "state": "IA",
                "street1": "9 DUG ST",
                "street2": "",
                "street3": null
            },
            "shippingAmount": 0.0,
            "tagIds": null,
            "taxAmount": 0.0,
            "userId": null,
            "weight": {
                "WeightUnits": 1,
                "units": "ounces",
                "value": 5.0
            }
        },
        {
            "advancedOptions": {
                "billToAccount": null,
                "billToCountryCode": null,
                "billToMyOtherAccount": null,
                "billToParty": null,
                "billToPostalCode": null,
                "containsAlcohol": false,
                "customField1": "EARLY BIRD SPECIAL",
                "customField2": "",
                "customField3": null,
                "mergedIds": [],
                "mergedOrSplit": false,
                "nonMachinable": false,
                "parentId": null,
                "saturdayDelivery": false,
                "source": null,
                "storeId": 12345,
                "warehouseId": 12345
            },
            "amountPaid": 0.0,
            "billTo": {
                "addressVerified": null,
                "city": null,
                "company": null,
                "country": null,
                "name": "Nope Example",
                "phone": null,
                "postalCode": null,
                "residential": null,
                "state": null,
                "street1": null,
                "street2": null,
                "street3": null
            },
            "carrierCode": "express_1",
            "confirmation": "none",
            "createDate": "2015-06-30T15:20:26.7230000",
            "customerEmail": "nope@example.com",
            "customerId": null,
            "customerNotes": null,
            "customerUsername": null,
            "dimensions": null,
            "externallyFulfilled": false,
            "externallyFulfilledBy": null,
            "gift": false,
            "giftMessage": null,
            "holdUntilDate": null,
            "insuranceOptions": {
                "insureShipment": false,
                "insuredValue": 0.0,
                "provider": null
            },
            "internalNotes": null,
            "internationalOptions": {
                "contents": "merchandise",
                "customsItems": [
                    {
                        "countryOfOrigin": "CN",
                        "customsItemId": 13461125,
                        "description": "Suspicious Munitions",
                        "harmonizedTariffCode": "",
                        "quantity": 1,
                        "value": 7.0
                    }
                ],
                "nonDelivery": "return_to_sender"
            },
            "items": [],
            "labelMessages": null,
            "modifyDate": "2015-06-30T18:47:11.8870000",
            "orderDate": "2015-05-19T21:24:00.0000000",
            "orderId": 123456789,
            "orderKey": "123456789",
            "orderNumber": "123456789",
            "orderStatus": "shipped",
            "orderTotal": 0.0,
            "packageCode": "package",
            "paymentDate": "2015-06-30T15:20:26.7230000",
            "paymentMethod": null,
            "requestedShippingService": "USPS First Class Mail Intl",
            "serviceCode": "usps_first_class_package_international",
            "shipByDate": null,
            "shipDate": "2015-07-01",
            "shipTo": {
                "addressVerified": "Address not yet validated",
                "city": "Large City",
                "company": null,
                "country": "IN",
                "name": "Nope Example",
                "phone": null,
                "postalCode": "100000",
                "residential": false,
                "state": null,
                "street1": "6 Bustling St",
                "street2": "Near Flower Market",
                "street3": "Maharashtra"
            },
            "shippingAmount": 0.0,
            "tagIds": null,
            "taxAmount": 0.0,
            "userId": null,
            "weight": {
                "WeightUnits": 1,
                "units": "ounces",
                "value": 5.0
            }
        }
    ],
    "page": 1,
    "pages": 1,
    "total": 2
}

"""

create_label_for_order = """
{
    "shipmentId": 72513480,
    "shipmentCost": 7.3,
    "insuranceCost": 0,
    "trackingNumber": "248201115029520",
    "labelData": "JVBERi0xLjQKJeLjz9MKMiAwIG9iago8PC9MZW5ndGggNjIvRmlsdGVyL0ZsYXRlRGVjb2RlPj5zdHJlYW0KeJwr5HIK4TI2UzC2NFMISeFyDeEK5CpUMFQwAEJDBV0jCz0LBV1jY0M9I4XkXAX9iDRDBZd8hUAuAEdGC7cKZW5kc3RyZWFtCmVuZG9iago0IDAgb2JqCjw8L1R5cGUvUGFnZS9NZWRpYUJveFswIDAgMjg4IDQzMl0vUmVzb3VyY2VzPDwvUHJvY1NldCBbL1BERiAvVGV4dCAvSW1hZ2VCIC9JbWFnZUMgL0ltYWdlSV0vWE9iamVjdDw8L1hmMSAxIDAgUj4+Pj4vQ29udGVudHMgMiAwIFIvUGFyZW50....",
    "formData": null
}
"""


get_order = """
{
    "advancedOptions": {
    "billToAccount": null,
    "billToCountryCode": null,
    "billToMyOtherAccount": null,
    "billToParty": null,
    "billToPostalCode": null,
    "containsAlcohol": false,
    "customField1": "EARLY BIRD SPECIAL",
    "customField2": "",
    "customField3": null,
    "mergedIds": [],
    "mergedOrSplit": false,
    "nonMachinable": false,
    "parentId": null,
    "saturdayDelivery": false,
    "source": null,
    "storeId": 12345,
    "warehouseId": 12345
    },
    "amountPaid": 0.0,
    "billTo": {
    "addressVerified": null,
    "city": null,
    "company": null,
    "country": null,
    "name": "Sandro Pigoni",
    "phone": null,
    "postalCode": null,
    "residential": null,
    "state": null,
    "street1": null,
    "street2": null,
    "street3": null
    },
    "carrierCode": "stamps_com",
    "confirmation": "delivery",
    "createDate": "2015-06-30T15:20:26.7230000",
    "customerEmail": "s.pigoni@gmail.com",
    "customerId": null,
    "customerNotes": null,
    "customerUsername": null,
    "dimensions": null,
    "externallyFulfilled": false,
    "externallyFulfilledBy": null,
    "gift": false,
    "giftMessage": null,
    "holdUntilDate": null,
    "insuranceOptions": {
    "insureShipment": false,
    "insuredValue": 0.0,
    "provider": null
    },
    "internalNotes": null,
    "internationalOptions": {
    "contents": "merchandise",
    "customsItems": [
    {
    "countryOfOrigin": "CN",
    "customsItemId": 123456789,
    "description": "Example Item",
    "harmonizedTariffCode": "",
    "quantity": 1,
    "value": 7.0
    }
    ],
    "nonDelivery": "return_to_sender"
    },
    "items": [],
    "labelMessages": null,
    "modifyDate": "2015-06-30T18:47:32.9330000",
    "orderDate": "2015-06-02T05:58:00.0000000",
    "orderId": 123456789,
    "orderKey": "123456789",
    "orderNumber": "123456789",
    "orderStatus": "shipped",
    "orderTotal": 0.0,
    "packageCode": "package",
    "paymentDate": "2015-06-30T15:20:26.7230000",
    "paymentMethod": null,
    "requestedShippingService": "USPS First Class Mail Intl",
    "serviceCode": "usps_first_class_package_international",
    "shipByDate": null,
    "shipDate": "2015-07-01",
    "shipTo": {
    "addressVerified": "Address not yet validated",
    "city": "Luzern",
    "company": null,
    "country": "CH",
    "name": "Nope Example",
    "phone": null,
    "postalCode": "5000",
    "residential": false,
    "state": "",
    "street1": "Weystrasse",
    "street2": "0",
    "street3": null
    },
    "shippingAmount": 0.0,
    "tagIds": null,
    "taxAmount": 0.0,
    "userId": null,
    "weight": {
    "WeightUnits": 1,
    "units": "ounces",
    "value": 5.0
    }
}
"""

get_product = """
{
    "active": true,
    "aliases": null,
    "createDate": "2016-10-31T07:43:00.203",
    "customsCountryCode": null,
    "customsDescription": null,
    "customsTariffNo": null,
    "customsValue": null,
    "defaultCarrierCode": null,
    "defaultConfirmation": null,
    "defaultCost": null,
    "defaultIntlCarrierCode": null,
    "defaultIntlConfirmation": null,
    "defaultIntlPackageCode": null,
    "defaultIntlServiceCode": null,
    "defaultPackageCode": null,
    "defaultServiceCode": null,
    "fulfillmentSku": "019372892403",
    "height": null,
    "internalNotes": null,
    "length": null,
    "modifyDate": "2017-01-16T06:58:26.05",
    "name": "Example product",
    "noCustoms": null,
    "price": 0.0,
    "productCategory": null,
    "productId": 123456789,
    "productType": null,
    "sku": " ABC123456789",
    "tags": null,
    "warehouseLocation": null,
    "weightOz": 5.0,
    "width": null
}
"""

get_rates = """
[
    {
    "otherCost": 0.0,
    "serviceCode": "usps_first_class_mail",
    "serviceName": "USPS First Class Mail - Large Envelope or Flat",
    "shipmentCost": 3.2
    },
    {
    "otherCost": 0.0,
    "serviceCode": "usps_first_class_mail",
    "serviceName": "USPS First Class Mail - Package",
    "shipmentCost": 3.93
    },
    {
    "otherCost": 0.0,
    "serviceCode": "usps_priority_mail",
    "serviceName": "USPS Priority Mail - Package",
    "shipmentCost": 7.02
    },
    {
    "otherCost": 0.0,
    "serviceCode": "usps_priority_mail",
    "serviceName": "USPS Priority Mail - Medium Flat Rate Box",
    "shipmentCost": 13.2
    },
    {
    "otherCost": 0.0,
    "serviceCode": "usps_priority_mail",
    "serviceName": "USPS Priority Mail - Small Flat Rate Box",
    "shipmentCost": 7.65
    },
    {
    "otherCost": 0.0,
    "serviceCode": "usps_priority_mail",
    "serviceName": "USPS Priority Mail - Large Flat Rate Box",
    "shipmentCost": 18.3
    },
    {
    "otherCost": 0.0,
    "serviceCode": "usps_priority_mail",
    "serviceName": "USPS Priority Mail - Flat Rate Envelope",
    "shipmentCost": 7.15
    },
    {
    "otherCost": 0.0,
    "serviceCode": "usps_priority_mail",
    "serviceName": "USPS Priority Mail - Flat Rate Padded Envelope",
    "shipmentCost": 7.75
    },
    {
    "otherCost": 0.0,
    "serviceCode": "usps_priority_mail",
    "serviceName": "USPS Priority Mail - Regional Rate Box A",
    "shipmentCost": 7.68
    },
    {
    "otherCost": 0.0,
    "serviceCode": "usps_priority_mail",
    "serviceName": "USPS Priority Mail - Regional Rate Box B",
    "shipmentCost": 8.07
    },
    {
    "otherCost": 0.0,
    "serviceCode": "usps_priority_mail",
    "serviceName": "USPS Priority Mail - Legal Flat Rate Envelope",
    "shipmentCost": 7.45
    },
    {
    "otherCost": 0.0,
    "serviceCode": "usps_priority_mail_express",
    "serviceName": "USPS Priority Mail Express - Package",
    "shipmentCost": 23.0
    },
    {
    "otherCost": 0.0,
    "serviceCode": "usps_priority_mail_express",
    "serviceName": "USPS Priority Mail Express - Flat Rate Envelope",
    "shipmentCost": 22.75
    },
    {
    "otherCost": 0.0,
    "serviceCode": "usps_priority_mail_express",
    "serviceName": "USPS Priority Mail Express - Flat Rate Padded Envelope",
    "shipmentCost": 23.25
    },
    {
    "otherCost": 0.0,
    "serviceCode": "usps_priority_mail_express",
    "serviceName": "USPS Priority Mail Express - Legal Flat Rate Envelope",
    "shipmentCost": 22.95
    },
    {
    "otherCost": 0.0,
    "serviceCode": "usps_media_mail",
    "serviceName": "USPS Media Mail - Package",
    "shipmentCost": 2.8
    },
    {
    "otherCost": 0.0,
    "serviceCode": "usps_parcel_select",
    "serviceName": "USPS Parcel Select Ground - Package",
    "shipmentCost": 6.92
    }
]
"""

get_warehouse = """
{
    "createDate":"2020-04-07T12:03:46.4000000",
    "extInventoryIdentity":"",
    "isDefault":false,
    "originAddress":
    {
    "addressVerified":"",
    "city":"Anywhere",
    "company":"",
    "country":"US",
    "name":"Warehouse 1",
    "phone":"18005551234",
    "postalCode":"12345",
    "residential":false,
    "state":"WA",
    "street1":"123 Long St",
    "street2":"Unit 4",
    "street3":""
    },
    "registerFedexMeter":"",
    "returnAddress":
    {
    "addressVerified":"",
    "city":"Anywhere",
    "company":"Test Company",
    "country":"US",
    "name":"",
    "phone":"18005553214",
    "postalCode":"23456",
    "residential":"",
    "state":"ID",
    "street1":"0 Short St",
    "street2":"",
    "street3":""
    },
    "sellerIntegrationId":"",
    "warehouseId": 456789,
    "warehouseName":"Test Company"
}

"""


list_products = """
{
    "page": 1,
    "pages": 1,
    "products": [
{
    "active": true,
    "aliases": null,
    "createDate": "2015-08-13T14:30:31.007",
    "customsCountryCode": null,
    "customsDescription": null,
    "customsTariffNo": null,
    "customsValue": null,
    "defaultCarrierCode": null,
    "defaultConfirmation": null,
    "defaultCost": null,
    "defaultIntlCarrierCode": null,
    "defaultIntlConfirmation": null,
    "defaultIntlPackageCode": null,
    "defaultIntlServiceCode": null,
    "defaultPackageCode": null,
    "defaultServiceCode": null,
    "fulfillmentSku": "712392290692",
    "height": null,
    "internalNotes": null,
    "length": null,
    "modifyDate": "2016-12-13T07:29:05.937",
    "name": "Example Product 0",
    "noCustoms": null,
    "price": 11.99,
    "productCategory": null,
    "productId": 987654321,
    "productType": null,
    "sku": "987654321",
    "tags": null,
    "warehouseLocation": null,
    "weightOz": 3.0,
    "width": null
},
{
    "active": true,
    "aliases": null,
    "createDate": "2015-08-13T14:30:31.007",
    "customsCountryCode": null,
    "customsDescription": null,
    "customsTariffNo": null,
    "customsValue": null,
    "defaultCarrierCode": null,
    "defaultConfirmation": null,
    "defaultCost": null,
    "defaultIntlCarrierCode": null,
    "defaultIntlConfirmation": null,
    "defaultIntlPackageCode": null,
    "defaultIntlServiceCode": null,
    "defaultPackageCode": null,
    "defaultServiceCode": null,
    "fulfillmentSku": "712392289948",
    "height": null,
    "internalNotes": "0468437",
    "length": null,
    "modifyDate": "2015-10-01T07:06:53.82",
    "name": "Example Product 1",
    "noCustoms": null,
    "price": 11.99,
    "productCategory": null,
    "productId": 18139199,
    "productType": null,
    "sku": "KYGGBIP5",
    "tags": null,
    "warehouseLocation": null,
    "weightOz": 3.0,
    "width": null
}
],
"total": 2
}
"""

list_shipments = """
{
    "page": 1,
    "pages": 1,
    "shipments": [
{
            "advancedOptions": {
                "billToAccount": null,
                "billToCountryCode": null,
                "billToParty": null,
                "billToPostalCode": null,
                "storeId": 12345
            },
            "batchNumber": "100002",
            "carrierCode": "stamps_com",
            "confirmation": "delivery",
            "createDate": "2015-06-29T14:29:28.5830000",
            "customerEmail": "nope@example.com",
            "dimensions": null,
            "formData": null,
            "insuranceCost": 0.0,
            "insuranceOptions": {
                "insureShipment": false,
                "insuredValue": 0.0,
                "provider": null
            },
            "isReturnLabel": false,
            "labelData": null,
            "marketplaceNotified": true,
            "notifyErrorMessage": null,
            "orderId": 123456789,
            "orderKey": "123456789",
            "orderNumber": "123456789",
            "packageCode": "package",
            "serviceCode": "usps_first_class_mail",
            "shipDate": "2015-06-29",
            "shipTo": {
                "addressVerified": null,
                "city": "CUT OFF",
                "company": null,
                "country": "US",
                "name": "Nope Example",
                "phone": null,
                "postalCode": "99999-1234",
                "residential": null,
                "state": "NY",
                "street1": "123 First St",
                "street2": "",
                "street3": null
            },
            "shipmentCost": 2.35,
            "shipmentId": 123456789,
            "shipmentItems": null,
            "trackingNumber": "9400111899562764298812",
            "userId": "3c16cdda-af71-449f-b3da-0ea71f0f6954",
            "voidDate": null,
            "voided": false,
            "warehouseId": 37675,
            "weight": {
                "WeightUnits": 1,
                "units": "ounces",
                "value": 6.0
            }
        },
        {
            "advancedOptions": {
                "billToAccount": null,
                "billToCountryCode": null,
                "billToParty": null,
                "billToPostalCode": null,
                "storeId": 12345
            },
            "batchNumber": "100002",
            "carrierCode": "stamps_com",
            "confirmation": "delivery",
            "createDate": "2015-06-29T14:29:28.5830000",
            "customerEmail": "yep@example.com",
            "dimensions": null,
            "formData": null,
            "insuranceCost": 0.0,
            "insuranceOptions": {
                "insureShipment": false,
                "insuredValue": 0.0,
                "provider": null
            },
            "isReturnLabel": false,
            "labelData": null,
            "marketplaceNotified": true,
            "notifyErrorMessage": null,
            "orderId": 234567890,
            "orderKey": "234567890",
            "orderNumber": "234567890",
            "packageCode": "package",
            "serviceCode": "usps_first_class_mail",
            "shipDate": "2015-06-29",
            "shipTo": {
                "addressVerified": null,
                "city": "BOISE",
                "company": null,
                "country": "US",
                "name": "A. Nother Example",
                "phone": null,
                "postalCode": "12345-9999",
                "residential": null,
                "state": "ME",
                "street1": "0 Short St",
                "street2": "",
                "street3": null
            },
            "shipmentCost": 2.35,
            "shipmentId": 101027951,
            "shipmentItems": null,
            "trackingNumber": "9400111899562764290564",
            "userId": "2bc927bb-22ba-41e5-b24f-087164eb5cc8",
            "voidDate": null,
            "voided": false,
            "warehouseId": 12345,
            "weight": {
                "WeightUnits": 1,
                "units": "ounces",
                "value": 6.0
            }
        },
        {
            "advancedOptions": {
                "billToAccount": null,
                "billToCountryCode": null,
                "billToParty": null,
                "billToPostalCode": null,
                "storeId": 12345
            },
            "batchNumber": "100002",
            "carrierCode": "stamps_com",
            "confirmation": "delivery",
            "createDate": "2015-06-29T14:29:28.5830000",
            "customerEmail": "another@example.com",
            "dimensions": null,
            "formData": null,
            "insuranceCost": 0.0,
            "insuranceOptions": {
                "insureShipment": false,
                "insuredValue": 0.0,
                "provider": null
            },
            "isReturnLabel": false,
            "labelData": null,
            "marketplaceNotified": true,
            "notifyErrorMessage": null,
            "orderId": 345678901,
            "orderKey": "345678901",
            "orderNumber": "345678901",
            "packageCode": "package",
            "serviceCode": "usps_first_class_mail",
            "shipDate": "2015-06-29",
            "shipTo": {
                "addressVerified": null,
                "city": "JACKSONVILLE",
                "company": null,
                "country": "US",
                "name": "Yep Example",
                "phone": "",
                "postalCode": "34567-1234",
                "residential": null,
                "state": "MN",
                "street1": "4 March St",
                "street2": "",
                "street3": null
            },
            "shipmentCost": 2.35,
            "shipmentId": 123456789,
            "shipmentItems": null,
            "trackingNumber": "9400111899562764290090",
            "userId": "2be5d7cc-8f49-4250-9c77-dd1d5f259a3a",
            "voidDate": null,
            "voided": false,
            "warehouseId": 12345,
            "weight": {
                "WeightUnits": 1,
                "units": "ounces",
                "value": 6.0
            }
        }
    ],
    "total": 3
}
"""


list_fulfillments = """
{
    "fulfillments": [
        {
        "carrierCode": "UPS",
        "createDate": "2020-06-19T07:21:51.7730000",
        "customerEmail": "nope@example.net",
        "deliveryDate": null,
        "fulfillmentFee": 0.0,
        "fulfillmentId": 12345678,
        "fulfillmentProviderCode": null,
        "fulfillmentServiceCode": null,
        "marketplaceNotified": false,
        "notifyErrorMessage": null,
        "orderId": 123456789,
        "orderNumber": "4229",
        "shipDate": "2020-06-19T00:00:00.0000000",
        "shipTo":
            {
                "addressVerified": null,
                "city": "ROME",
                "company": "",
                "country": "US",
                "name": "Nope Example",
                "phone": "123456789",
                "postalCode": "99999-1234",
                "residential": null,
                "state": "CT",
                "street1": "0 Lost Way",
                "street2": "",
                "street3": null
            },
        "trackingNumber": "1Z4X53V5032442XXXX",
        "userId": "98f7eab4-4d54-43b3-81e9-187f79528765",
        "voidDate": null,
        "voidRequested": false,
        "voided": false
    },
    {
        "carrierCode": null,
        "createDate": "2020-06-24T10:32:33.3730000",
        "customerEmail": "yep@example.com",
        "deliveryDate": null,
        "fulfillmentFee": 0.0,
        "fulfillmentId": 23456789,
        "fulfillmentProviderCode": null,
        "fulfillmentServiceCode": null,
        "marketplaceNotified": false,
        "notifyErrorMessage": "IntegrationError: Shopify encountered an error and responded with StatusCode UnprocessableEntity",
        "orderId": 123456789,
        "orderNumber": "1234",
        "shipDate": "2020-06-24T10:32:33.6870000",
        "shipTo":
            {
                "addressVerified": null,
                "city": "CONCORD",
                "company": "Arbitrary LLC",
                "country": "US",
                "name": "Dan Arbitrary",
                "phone": "+12346789",
                "postalCode": "99999-1234",
                "residential": null,
                "state": "MT",
                "street1": "7 Some St",
                "street2": "",
                "street3": null
            },
        "trackingNumber": "",
        "userId": "2ce23917-3e8e-485b-9853-20fde97783ea",
        "voidDate": null,
        "voidRequested": false,
        "voided": false
        }
    ],
    "page": 1,
    "pages": 1,
    "total": 2
}
"""
