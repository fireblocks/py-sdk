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

from pydantic import BaseModel, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from fireblocks_client.models.abi_function import AbiFunction
from fireblocks_client.models.contract_attributes import ContractAttributes
from fireblocks_client.models.contract_doc import ContractDoc
from typing import Optional, Set
from typing_extensions import Self

class ContractUploadRequest(BaseModel):
    """
    ContractUploadRequest
    """ # noqa: E501
    name: StrictStr = Field(description="The name of the contract template")
    description: StrictStr = Field(description="A short description of the contract template")
    long_description: Optional[StrictStr] = Field(default=None, description="A full description of the contract template. May contain   to break the lines", alias="longDescription")
    bytecode: StrictStr = Field(description="The compiled artifact of this smart contract. Used for deployment of this contract template")
    sourcecode: Optional[StrictStr] = Field(default=None, description="The source code of the contract. Optional.")
    type: Optional[StrictStr] = Field(default=None, description="The type of the contract template")
    docs: Optional[ContractDoc] = Field(default=None, description="A `natspec` compliant documentation json. Can be retrieved from the output json after compilation")
    abi: List[List[AbiFunction]]
    attributes: Optional[ContractAttributes] = Field(default=None, description="The attributes related to this contract template. It will be displayed in the tokenization page")
    __properties: ClassVar[List[str]] = ["name", "description", "longDescription", "bytecode", "sourcecode", "type", "docs", "abi", "attributes"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['FUNGIBLE_TOKEN', 'NON_FUNGIBLE_TOKEN', 'NON_TOKEN', 'TOKEN_EXTENSION', 'TOKEN_UTILITY']):
            raise ValueError("must be one of enum values ('FUNGIBLE_TOKEN', 'NON_FUNGIBLE_TOKEN', 'NON_TOKEN', 'TOKEN_EXTENSION', 'TOKEN_UTILITY')")
        return value

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
        """Create an instance of ContractUploadRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of docs
        if self.docs:
            _dict['docs'] = self.docs.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in abi (list of list)
        _items = []
        if self.abi:
            for _item in self.abi:
                if _item:
                    _items.append(
                         [_inner_item.to_dict() for _inner_item in _item if _inner_item is not None]
                    )
            _dict['abi'] = _items
        # override the default output from pydantic by calling `to_dict()` of attributes
        if self.attributes:
            _dict['attributes'] = self.attributes.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ContractUploadRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "longDescription": obj.get("longDescription"),
            "bytecode": obj.get("bytecode"),
            "sourcecode": obj.get("sourcecode"),
            "type": obj.get("type"),
            "docs": ContractDoc.from_dict(obj["docs"]) if obj.get("docs") is not None else None,
            "abi": [
                    [AbiFunction.from_dict(_inner_item) for _inner_item in _item]
                    for _item in obj["abi"]
                ] if obj.get("abi") is not None else None,
            "attributes": ContractAttributes.from_dict(obj["attributes"]) if obj.get("attributes") is not None else None
        })
        return _obj


