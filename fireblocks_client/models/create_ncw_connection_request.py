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

from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class CreateNcwConnectionRequest(BaseModel):
    """
    CreateNcwConnectionRequest
    """ # noqa: E501
    ncw_id: StrictStr = Field(description="The ID of the Non-Custodial Wallet to connect to the dApp.", alias="ncwId")
    ncw_account_id: Union[StrictFloat, StrictInt] = Field(description="The NCW account ID to connect to the dApp.", alias="ncwAccountId")
    fee_level: StrictStr = Field(description="The default fee level. Valid values are `MEDIUM` and `HIGH`.", alias="feeLevel")
    uri: StrictStr = Field(description="The WalletConnect uri provided by the dapp.")
    chain_ids: Optional[List[StrictStr]] = Field(default=None, description="The IDs of the blockchain networks used in the Web3 connection (Currently required in V1 connections only).", alias="chainIds")
    __properties: ClassVar[List[str]] = ["ncwId", "ncwAccountId", "feeLevel", "uri", "chainIds"]

    @field_validator('fee_level')
    def fee_level_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['MEDIUM', 'HIGH']):
            raise ValueError("must be one of enum values ('MEDIUM', 'HIGH')")
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
        """Create an instance of CreateNcwConnectionRequest from a JSON string"""
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
        """Create an instance of CreateNcwConnectionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ncwId": obj.get("ncwId"),
            "ncwAccountId": obj.get("ncwAccountId"),
            "feeLevel": obj.get("feeLevel"),
            "uri": obj.get("uri"),
            "chainIds": obj.get("chainIds")
        })
        return _obj


