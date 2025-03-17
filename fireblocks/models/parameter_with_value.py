# coding: utf-8

"""
    Fireblocks API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.6.2
    Contact: support@fireblocks.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from fireblocks.models.parameter import Parameter
from typing import Optional, Set
from typing_extensions import Self

class ParameterWithValue(BaseModel):
    """
    ParameterWithValue
    """ # noqa: E501
    name: StrictStr = Field(description="The name of the parameter as it appears in the ABI")
    description: Optional[StrictStr] = Field(default=None, description="A description of the parameter, fetched from the devdoc of this contract")
    internal_type: Optional[StrictStr] = Field(default=None, description="The  internal type of the parameter as it appears in the ABI", alias="internalType")
    type: StrictStr = Field(description="The type of the parameter as it appears in the ABI")
    components: Optional[List[Parameter]] = None
    value: Optional[StrictStr] = Field(default=None, description="The value of the parameter. can also be ParameterWithValue")
    function_value: Optional[LeanAbiFunction] = Field(default=None, description="The function value of this param (if has one). If this is set, the `value` shouldn`t be. Used for proxies", alias="functionValue")
    __properties: ClassVar[List[str]] = ["name", "description", "internalType", "type", "components", "value", "functionValue"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ParameterWithValue from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in components (list)
        _items = []
        if self.components:
            for _item_components in self.components:
                if _item_components:
                    _items.append(_item_components.to_dict())
            _dict['components'] = _items
        # override the default output from pydantic by calling `to_dict()` of function_value
        if self.function_value:
            _dict['functionValue'] = self.function_value.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ParameterWithValue from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "internalType": obj.get("internalType"),
            "type": obj.get("type"),
            "components": [Parameter.from_dict(_item) for _item in obj["components"]] if obj.get("components") is not None else None,
            "value": obj.get("value"),
            "functionValue": LeanAbiFunction.from_dict(obj["functionValue"]) if obj.get("functionValue") is not None else None
        })
        return _obj

from fireblocks.models.lean_abi_function import LeanAbiFunction
# TODO: Rewrite to not use raise_errors
ParameterWithValue.model_rebuild(raise_errors=False)

