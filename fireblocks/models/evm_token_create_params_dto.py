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
from fireblocks.models.parameter_with_value import ParameterWithValue
from typing import Optional, Set
from typing_extensions import Self

class EVMTokenCreateParamsDto(BaseModel):
    """
    EVMTokenCreateParamsDto
    """ # noqa: E501
    contract_id: StrictStr = Field(description="The id of the contract template that will be used to create the token", alias="contractId")
    constructor_params: Optional[List[List[ParameterWithValue]]] = Field(default=None, description="The constructor parameters and values of the contract template", alias="constructorParams")
    __properties: ClassVar[List[str]] = ["contractId", "constructorParams"]

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
        """Create an instance of EVMTokenCreateParamsDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in constructor_params (list of list)
        _items = []
        if self.constructor_params:
            for _item in self.constructor_params:
                if _item:
                    _items.append(
                         [_inner_item.to_dict() for _inner_item in _item if _inner_item is not None]
                    )
            _dict['constructorParams'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EVMTokenCreateParamsDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "contractId": obj.get("contractId"),
            "constructorParams": [
                    [ParameterWithValue.from_dict(_inner_item) for _inner_item in _item]
                    for _item in obj["constructorParams"]
                ] if obj.get("constructorParams") is not None else None
        })
        return _obj

