import json
import re
from datetime import date, datetime
from decimal import Decimal
from typing import Type

import cattr
from dateutil import parser

snake_case_regex = re.compile("([a-z0-9])([A-Z])")


class ShipStationBase:
    @classmethod
    def to_camel_case(self, name):
        tokens = name.lower().split("_")
        first_word = tokens.pop(0)
        return first_word + "".join(x.title() for x in tokens)

    @classmethod
    def to_snake_case(self, name):
        return snake_case_regex.sub(r"\1_\2", name).lower()

    @classmethod
    def convert_camel_case(self, data):
        if isinstance(data, dict):
            new_dict = {}
            for key, value in data.items():
                value = self.convert_camel_case(value)
                snake_key = self.to_snake_case(key)
                new_dict[snake_key] = value
            return new_dict

        elif isinstance(data, (list, set, tuple)):
            new_list = []
            for value in data:
                new_list.append(self.convert_camel_case(value))
            return new_list
        return data

    @classmethod
    def convert_snake_case(self, data):
        if isinstance(data, dict):
            new_dict = {}
            for key, value in data.items():
                if isinstance(value, dict):
                    value = self.convert_snake_case(value)
                if value:
                    snake_key = self.to_camel_case(key)
                    new_dict[snake_key] = value
            return new_dict
        elif isinstance(data, (list, set, tuple)):
            new_list = []
            for value in data:
                new_list.append(self.convert_snake_case(value))
            return new_list
        return data

    def require_attribute(self, attribute):
        if not getattr(self, attribute):
            raise AttributeError(f"'{attribute}' is a required attribute")

    def require_type(self, item, required_type, message=""):
        if item is None:
            return
        if not isinstance(item, required_type):
            if message:
                raise AttributeError(message)
            raise AttributeError(f"must be of type {required_type}")

    def require_membership(self, value, other):
        if value not in other:
            raise AttributeError("'{}' is not one of {}".format(value, str(other)))

    def _validate_parameters(self, parameters, valid_parameters):
        self.require_type(parameters, dict)
        return {self.to_camel_case(key): value for key, value in parameters.items()}

    def json(self, json_str=None):
        if json_str:
            if isinstance(json_str, dict):
                return self._structure(self.convert_camel_case(json_str))
            return self._structure(
                json.loads(json_str, object_hook=self.convert_camel_case)
            )
        return json.dumps(self.convert_snake_case(self._unstructure()))

    def _unstructure(self):
        conv = cattr.Converter(unstruct_strat=cattr.UnstructureStrategy.AS_DICT)
        conv.register_unstructure_hook(Decimal, lambda d: str(d))
        conv.register_unstructure_hook(datetime, lambda d: d.isoformat())
        # might need a date to datetime conversion hook
        return conv.unstructure(self)

    def _structure(self, converted_json):
        conv = cattr.Converter(unstruct_strat=cattr.UnstructureStrategy.AS_DICT)
        conv.register_structure_hook(Decimal, lambda d, t: Decimal(d))
        conv.register_structure_hook(datetime, lambda dt, t: parser.parse(dt))
        conv.register_structure_hook(date, lambda dt, t: parser.parse(dt))
        return conv.structure(converted_json, type(self))
