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

from pydantic import BaseModel, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from fireblocks_client.models.parameter_with_value import ParameterWithValue
from typing import Optional, Set
from typing_extensions import Self

class ContractDeployRequest(BaseModel):
    """
    ContractDeployRequest
    """ # noqa: E501
    asset_id: StrictStr = Field(description="The base asset identifier of the blockchain you want to deploy to", alias="assetId")
    vault_account_id: StrictStr = Field(description="The vault account id you wish to deploy from", alias="vaultAccountId")
    constructor_parameters: Optional[List[ParameterWithValue]] = Field(default=None, description="The constructor parameters of this contract", alias="constructorParameters")
    __properties: ClassVar[List[str]] = ["assetId", "vaultAccountId", "constructorParameters"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ContractDeployRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in constructor_parameters (list)
        _items = []
        if self.constructor_parameters:
            for _item in self.constructor_parameters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['constructorParameters'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ContractDeployRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "assetId": obj.get("assetId"),
            "vaultAccountId": obj.get("vaultAccountId"),
            "constructorParameters": [ParameterWithValue.from_dict(_item) for _item in obj["constructorParameters"]] if obj.get("constructorParameters") is not None else None
        })
        return _obj


