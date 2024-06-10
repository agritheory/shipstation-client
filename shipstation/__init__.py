"""shipstation-client

This package allows you to interact with the Shipstation API in an object oriented way.

QUICKSTART:
ss = ShipStation(key="", secret="", debug=False, timeout="10")
stores = ss.get_stores()
"""

from shipstation.api import ShipStation
from shipstation.models import *
from shipstation.pagination import Page

__author__ = "Tyler Matteson"
