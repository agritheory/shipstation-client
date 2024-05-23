import datetime

import pytest
from respx import MockRouter, mock
from shipstation.api import ShipStation
from shipstation.models import *


@pytest.fixture(scope="session")
def mocked_order_creation():
    with mock(
        base_url="https://ssapi.shipstation.com", assert_all_called=False
    ) as respx_mock:
        respx_mock.post("/orders/createorder", name="test_order_creation").respond(
            200, json=ORDER_CREATION
        )
        yield respx_mock


@pytest.fixture(scope="session")
def mock_order() -> ShipStationOrder:
    return ShipStationOrder(
        order_number="SI-08557",
        order_date=datetime.datetime(2020, 9, 28, 0, 0),
        order_status="awaiting_shipment",
        bill_to=ShipStationAddress(
            name="Random Customer",
            company=None,
            street1="Random Customer",
            street2="1600 Pennsylvania Avenue NW",
            street3=None,
            city="WASHINGTON",
            state="DC",
            postal_code="20500",
            country=None,
            phone="",
            address_verified=None,
        ),
        ship_to=ShipStationAddress(
            name="Random Customer",
            company=None,
            street1="Random Customer",
            street2="1600 Pennsylvania Avenue NW",
            street3=None,
            city="WASHINGTON",
            state="DC",
            postal_code="20500",
            country=None,
            phone="",
            address_verified=None,
        ),
        carrier_code="ups_walleted",
        service_code="ups_ground",
        package_code="package",
        confirmation=None,
        ship_date=datetime.datetime(2020, 9, 28, 0, 0),
    )


@mock
def test_create_order(
    ss: ShipStation,
    mocked_order_creation: MockRouter,
    mock_order: ShipStationOrder,
) -> None:
    request = mocked_order_creation["test_order_creation"]
    response = ss.create_order(mock_order)
    assert isinstance(response, ShipStationOrder)
    assert isinstance(response.bill_to, ShipStationAddress)
    assert isinstance(response.ship_to, ShipStationAddress)
    assert isinstance(response.ship_date, datetime.datetime)


ORDER_CREATION = {
    "advancedOptions": {
        "billToAccount": None,
        "billToCountryCode": None,
        "billToMyOtherAccount": None,
        "billToParty": None,
        "billToPostalCode": None,
        "containsAlcohol": False,
        "customField1": None,
        "customField2": None,
        "customField3": None,
        "mergedIds": [],
        "mergedOrSplit": False,
        "nonMachinable": False,
        "parentId": None,
        "saturdayDelivery": False,
        "source": None,
        "storeId": 176145,
        "warehouseId": 241631,
    },
    "amountPaid": 0.0,
    "billTo": {
        "addressVerified": None,
        "city": "WASHINGTON",
        "company": None,
        "country": None,
        "name": "Random Customer",
        "phone": None,
        "postalCode": "20500",
        "residential": None,
        "state": "DC",
        "street1": "Random Customer",
        "street2": "1600 Pennsylvania Avenue NW",
        "street3": None,
    },
    "carrierCode": "ups_walleted",
    "confirmation": "none",
    "createDate": "2020-10-21T11:47:05.7430000",
    "customerEmail": None,
    "customerId": None,
    "customerNotes": None,
    "customerUsername": None,
    "dimensions": None,
    "externallyFulfilled": False,
    "externallyFulfilledBy": None,
    "gift": False,
    "giftMessage": None,
    "holdUntilDate": None,
    "insuranceOptions": {
        "insureShipment": False,
        "insuredValue": 0.0,
        "provider": None,
    },
    "internalNotes": None,
    "internationalOptions": {
        "contents": None,
        "customsItems": None,
        "nonDelivery": None,
    },
    "items": [],
    "labelMessages": None,
    "modifyDate": "2020-10-21T11:47:05.6800000",
    "orderDate": "2020-09-28T00:00:00.0000000",
    "orderId": 143862300,
    "orderKey": "4c8cfb59e6df4872807e6b83bd98e566",
    "orderNumber": "SI-08557",
    "orderStatus": "awaiting_shipment",
    "orderTotal": 0.0,
    "packageCode": "package",
    "paymentDate": None,
    "paymentMethod": None,
    "requestedShippingService": None,
    "serviceCode": "ups_ground",
    "shipByDate": None,
    "shipDate": "2020-09-28",
    "shipTo": {
        "addressVerified": "Address validation warning",
        "city": "WASHINGTON",
        "company": None,
        "country": "US",
        "name": "Random Customer",
        "phone": None,
        "postalCode": "20500-0003",
        "residential": False,
        "state": "DC",
        "street1": "1600 PENNSYLVANIA AVE NW",
        "street2": "RANDOM CUSTOMER",
        "street3": None,
    },
    "shippingAmount": 0.0,
    "tagIds": None,
    "taxAmount": 0.0,
    "userId": None,
    "weight": {"WeightUnits": 1, "units": "ounces", "value": 0.0},
}


# duplicate_error_message = """
# {
#     "ExceptionMessage": "Ship To: Postal Code must be provided.",
#     "ExceptionType": "System.Exception",
#     "Message": "An error has occurred.",
#     "StackTrace": "   at SS.OpenApi.Controllers.OrdersController._CreateOrder(Order apiOrder, Guid ImportBatch, Boolean throwDuplicateException) in D:\\buildAgentFull\\work\\8e15a453e647e65a\\SS.OpenApi\\Controllers\\OrdersController.cs:line 1379\r\n   at SS.OpenApi.Controllers.OrdersController.CreateOrder(Order apiOrder) in D:\\buildAgentFull\\work\\8e15a453e647e65a\\SS.OpenApi\\Controllers\\OrdersController.cs:line 976\r\n   at lambda_method(Closure , Object , Object[] )\r\n   at System.Web.Http.Controllers.ReflectedHttpActionDescriptor.ActionExecutor.<>c__DisplayClass10.<GetExecutor>b__9(Object instance, Object[] methodParameters)\r\n   at System.Web.Http.Controllers.ReflectedHttpActionDescriptor.ExecuteAsync(HttpControllerContext controllerContext, IDictionary`2 arguments, CancellationToken cancellationToken)\r\n--- End of stack trace from previous location where exception was thrown ---\r\n   at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n   at System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)\r\n   at System.Runtime.CompilerServices.TaskAwaiter.ValidateEnd(Task task)\r\n   at System.Web.Http.Controllers.ApiControllerActionInvoker.<InvokeActionAsyncCore>d__0.MoveNext()\r\n--- End of stack trace from previous location where exception was thrown ---\r\n   at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n   at System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)\r\n   at System.Web.Http.Filters.ActionFilterAttribute.<CallOnActionExecutedAsync>d__5.MoveNext()\r\n--- End of stack trace from previous location where exception was thrown ---\r\n   at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n   at System.Web.Http.Filters.ActionFilterAttribute.<CallOnActionExecutedAsync>d__5.MoveNext()\r\n--- End of stack trace from previous location where exception was thrown ---\r\n   at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n   at System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)\r\n   at System.Web.Http.Filters.ActionFilterAttribute.<ExecuteActionFilterAsyncCore>d__0.MoveNext()\r\n--- End of stack trace from previous location where exception was thrown ---\r\n   at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n   at System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)\r\n   at System.Web.Http.Controllers.ActionFilterResult.<ExecuteAsync>d__2.MoveNext()\r\n--- End of stack trace from previous location where exception was thrown ---\r\n   at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n   at System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)\r\n   at System.Web.Http.Filters.AuthorizationFilterAttribute.<ExecuteAuthorizationFilterAsyncCore>d__2.MoveNext()\r\n--- End of stack trace from previous location where exception was thrown ---\r\n   at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n   at System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)\r\n   at System.Web.Http.Controllers.ExceptionFilterResult.<ExecuteAsync>d__0.MoveNext()\r\n--- End of stack trace from previous location where exception was thrown ---\r\n   at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n   at System.Web.Http.Controllers.ExceptionFilterResult.<ExecuteAsync>d__0.MoveNext()\r\n--- End of stack trace from previous location where exception was thrown ---\r\n   at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()\r\n   at System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(Task task)\r\n   at System.Runtime.CompilerServices.TaskAwaiter.ValidateEnd(Task task)\r\n   at System.Web.Http.Dispatcher.HttpControllerDispatcher.<SendAsync>d__1.MoveNext()"
# }
# """

# ShipStationOrder(
#     order_number="SI-08557",
#     order_date=datetime.datetime(2020, 9, 28, 0, 0),
#     order_status="awaiting_shipment",
#     bill_to=ShipStationAddress(
#         name="Melvin King - 22",
#         company=None,
#         street1="Lancaster Lanterns",
#         street2="5264 White Oak Rd",
#         street3=None,
#         city="PARADISE",
#         state="PA",
#         postal_code=None,
#         country=None,
#         phone="(717) 455-3765",
#         residential=None,
#         address_verified=None,
#     ),
#     ship_to=ShipStationAddress(
#         name="Melvin King - 22",
#         company=None,
#         street1="Lancaster Lanterns",
#         street2="5264 White Oak Rd",
#         street3=None,
#         city="PARADISE",
#         state="PA",
#         postal_code=None,
#         country=None,
#         phone="(717) 455-3765",
#         residential=None,
#         address_verified=None,
#     ),
#     order_key=None,
#     payment_date=None,
#     customer_username=None,
#     customer_email=None,
#     items=None,
#     amount_paid=None,
#     tax_amount=None,
#     shipping_amount=None,
#     customer_notes=None,
#     internal_notes=None,
#     gift=None,
#     payment_method=None,
#     carrier_code="ups_walleted",
#     service_code="ups_ground",
#     package_code="package",
#     confirmation=None,
#     ship_date=datetime.datetime(2020, 10, 21, 0, 0),
#     dimensions=None,
#     insurance_options=None,
#     international_options=None,
#     advanced_options=None,
#     tracking_number=None,
#     voided=None,
#     void_date=None,
#     order_id=None,
#     marketplace_notified=None,
#     warehouse_id=None,
#     user_id=None,
#     label_data=None,
#     batch_number=None,
#     insurance_cost=None,
#     form_data=None,
#     notify_error_message=None,
#     is_return_label=None,
#     shipment_id=None,
#     shipment_cost=None,
#     weight=None,
#     create_date=None,
#     modify_date=None,
#     shipment_items=None,
#     ship_by_date=None,
#     customer_id=None,
#     order_total=None,
#     gift_message=None,
#     requested_shipping_service=None,
#     hold_until_date=None,
#     tag_ids=None,
#     externally_fulfilled=None,
#     externally_fulfilled_by=None,
#     label_messages=None,
#     test_label=None,
# )
