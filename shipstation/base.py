import json
import re
import typing
from datetime import date, datetime
from decimal import Decimal

import cattr
from dateutil import parser

snake_case_regex = re.compile("([a-z0-9])([A-Z])")


class ShipStationBase:
    @classmethod
    def to_camel_case(self, name: str) -> str:
        tokens = name.lower().split("_")
        first_word = tokens.pop(0)
        return first_word + "".join(x.title() for x in tokens)

    @classmethod
    def to_snake_case(self, name: str) -> str:
        return snake_case_regex.sub(r"\1_\2", name).lower()

    @classmethod
    def convert_camel_case(
        self, data: typing.Iterable[typing.Any]
    ) -> typing.Iterable[typing.Any]:
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
    def convert_snake_case(
        self, data: typing.Iterable[typing.Any]
    ) -> typing.Union[
        typing.Dict[str, typing.Any], typing.List[typing.Any], typing.Any
    ]:
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

    def require_attribute(self, attribute: str) -> typing.NoReturn:  # type: ignore
        if not getattr(self, attribute):
            raise AttributeError(f"'{attribute}' is a required attribute")

    def require_type(  # type: ignore
        self, item: typing.Any, required_type: typing.Any, message: str = ""
    ) -> typing.NoReturn:
        if item is None:
            pass
        if not isinstance(item, required_type):
            if message:
                raise AttributeError(message)
            raise AttributeError(f"must be of type {required_type}")

    def require_membership(  # type: ignore
        self, value: typing.Any, other: typing.Any
    ) -> typing.NoReturn:
        if value not in other:
            raise AttributeError(f"'{value}' is not one of {other}")

    def _validate_parameters(
        self, parameters: typing.Any, valid_parameters: typing.Any
    ) -> typing.Dict[str, typing.Any]:
        self.require_type(parameters, dict)
        return {self.to_camel_case(key): value for key, value in parameters.items()}

    def json(
        self, json_str: typing.Union[None, str, typing.Dict[str, typing.Any]] = None
    ) -> typing.Union[typing.Any, ShipStationBase]:
        if not json_str:
            return json.dumps(self.convert_snake_case(self._unstructure()))
        if isinstance(json_str, dict):
            return self._structure(self.convert_camel_case(json_str))
        return self._structure(
            json.loads(json_str, object_hook=self.convert_camel_case)
        )

    def _unstructure(self) -> typing.Any:
        conv = cattr.Converter(  # type: ignore
            unstruct_strat=cattr.UnstructureStrategy.AS_DICT
        )
        conv.register_unstructure_hook(Decimal, lambda d: str(d))
        conv.register_unstructure_hook(datetime, lambda d: d.isoformat())
        # might need a date to datetime conversion hook
        return conv.unstructure(self)

    def _structure(self, converted_json: typing.Iterable[typing.Any]) -> typing.Any:
        conv = cattr.Converter(  # type: ignore
            unstruct_strat=cattr.UnstructureStrategy.AS_DICT
        )
        conv.register_structure_hook(Decimal, lambda d, t: Decimal(d))
        conv.register_structure_hook(datetime, lambda dt, t: parser.parse(dt))
        conv.register_structure_hook(date, lambda dt, t: parser.parse(dt))
        return conv.structure(converted_json, type(self))
