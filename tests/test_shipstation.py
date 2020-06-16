import unittest

import pytest

from shipstation.api import ShipStation
from shipstation.models import *


class ShipStationApiTests(unittest.TestCase):
    # order fetch tests
    def setUp(self):
        self.ss = ShipStation("123", "456")

    def tearDown(self):
        self.ss = None

    @pytest.mark.xfail(raises=AttributeError)
    def test_fetch_orders_must_be_dict(self):
        self.ss.fetch_orders(parameters="non dict")

    @pytest.mark.xfail(raises=AttributeError)
    def test_fetch_orders_must_use_correct_parameter(self):
        self.ss.fetch_orders(parameters={"bad": "not good"})

    # ShipStation.list_customers()
    @pytest.mark.xfail(raises=AttributeError)
    def test_list_customers(self):
        self.ss.list_customers(parameters={"bad": "not good"})

    # ShipStation.list_fulfillments()
    @pytest.mark.xfail(raises=AttributeError)
    def test_list_fulfillments(self):
        self.ss.list_fulfillments(parameters={"bad": "not good"})

    # ShipStation.list_shipments()
    @pytest.mark.xfail(raises=AttributeError)
    def test_list_shipments(self):
        self.ss.list_shipments(parameters={"bad": "not good"})

    # ShipStation.create_shipment_label()
    @pytest.mark.xfail(raises=AttributeError)
    def test_create_shipment_label_parameters(self):
        self.ss.create_shipment_label(options={"bad": "not good"})

    # ShipStation.create_shipment_label()
    # def test_create_shipment_label_types(self):
    #     options = {
    #         "weight": ShipStationWeight(),
    #         "dimensions": ShipStationContainer(),
    #         "ship_to": ShipStationAddress(),
    #         "ship_from": ShipStationAddress(),
    #         "international_options": ShipStationInternationalOptions(),
    #         "advanced_options": ShipStationAdvancedOptions()
    #     }
    #     self.ss.create_shipment_label(options=options)

    # ShipStation.get_rates()
    @pytest.mark.xfail(raises=AttributeError)
    def test_get_rates_options(self):
        self.ss.get_rates(options={"bad": "not good"})

    # ShipStation.get_rates()
    @pytest.mark.xfail(raises=AttributeError)
    def test_get_rates_types(self):
        # carrier_code is a valid key
        self.ss.get_rates(options={"carrier_code": "not good"})

    #
    # # ShipStation.update_store()
    # @pytest.mark.xfail(raises=AttributeError)
    # def test_update_store(self):
    #     self.ss.update_store(parameters={"bad": "not good"})
    #
    # # ShipStation.update_store()
    # @pytest.mark.xfail(raises=AttributeError)
    # def test_update_store_attributes(self):
    #     # build valid params with bad types
    #     self.ss.get_rates(parameters={"bad": "not good"})
    #
    # # ShipStation.update_store()
    # @pytest.mark.xfail(raises=AttributeError)
    # def test_update_store_type(self):
    #     # build valid params with bad types
    #     self.ss.get_rates(parameters={"bad": "not good"})
    #
    # # ShipStation.update_store() => ShipStationStatusMapping
    # @pytest.mark.xfail(raises=AttributeError)
    # def test_update_store_status_mappings(self):
    #     # build valid params with bad types
    #     self.ss.get_rates(parameters={"bad": "not good"})
    #
    # # ShipStation.update_warehouse()
    # @pytest.mark.xfail(raises=AttributeError)
    # def test_update_warehouse_options(self):
    #     # build valid params with bad types
    #     self.ss.get_rates(parameters={"bad": "not good"})
    #
    # # ShipStation.update_warehouse()
    # @pytest.mark.xfail(raises=AttributeError)
    # def test_update_warehouse_attributes(self):
    #     # build valid params with bad types
    #     self.ss.get_rates(parameters={"bad": "not good"})
    #
    # # ShipStation.update_warehouse()
    # @pytest.mark.xfail(raises=AttributeError)
    # def test_update_warehouse_types(self):
    #     # build valid params with bad types
    #     self.ss.get_rates(parameters={"bad": "not good"})
    #
    # ShipStation.subscribe_to_webhook()
    @pytest.mark.xfail(raises=AttributeError)
    def test_subscribe_to_webhook_options(self):
        self.ss.get_rates(options={"bad": "not good"})

    # ShipStation.subscribe_to_webhook()
    @pytest.mark.xfail(raises=AttributeError)
    def test_subscribe_to_webhook_attributes(self):
        # target_url is a valid key
        self.ss.get_rates(options={"target_url": "not good"})
