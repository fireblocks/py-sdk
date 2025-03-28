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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ReissueMultichainTokenRequestDto(BaseModel):
    """
    ReissueMultichainTokenRequestDto
    """ # noqa: E501
    vault_account_id: StrictStr = Field(description="The id of the vault account that initiated the request to issue the token", alias="vaultAccountId")
    chains: List[StrictStr] = Field(description="The base asset identifiers of the blockchains you want to deploy to")
    use_gasless: Optional[StrictBool] = Field(default=None, description="Whether to use gasless deployment or not", alias="useGasless")
    fee: Optional[StrictStr] = Field(default=None, description="Max fee amount for the deploy request. Interchangeable with the 'feeLevel' field")
    fee_level: Optional[StrictStr] = Field(default=None, description="Fee level for the deploy request. Interchangeable with the 'fee' field", alias="feeLevel")
    __properties: ClassVar[List[str]] = ["vaultAccountId", "chains", "useGasless", "fee", "feeLevel"]

    @field_validator('fee_level')
    def fee_level_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['LOW', 'MEDIUM', 'HIGH']):
            raise ValueError("must be one of enum values ('LOW', 'MEDIUM', 'HIGH')")
        return value

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
        """Create an instance of ReissueMultichainTokenRequestDto from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReissueMultichainTokenRequestDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "vaultAccountId": obj.get("vaultAccountId"),
            "chains": obj.get("chains"),
            "useGasless": obj.get("useGasless"),
            "fee": obj.get("fee"),
            "feeLevel": obj.get("feeLevel")
        })
        return _obj


