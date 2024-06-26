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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class TransactionFee(BaseModel):
    """
    TransactionFee
    """ # noqa: E501
    fee_per_byte: Optional[StrictStr] = Field(default=None, alias="feePerByte")
    gas_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="gasPrice")
    gas_limit: Optional[StrictStr] = Field(default=None, alias="gasLimit")
    network_fee: Optional[StrictStr] = Field(default=None, alias="networkFee")
    base_fee: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="(optional) Base Fee according to EIP-1559 (ETH assets)", alias="baseFee")
    priority_fee: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="(optional) Priority Fee according to EIP-1559 (ETH assets)", alias="priorityFee")
    max_fee_per_gas_delta: Optional[StrictStr] = Field(default=None, description="Max Fee Per Gas Delta added only for EIP-1559 (ETH assets)", alias="maxFeePerGasDelta")
    l1_fee: Optional[StrictStr] = Field(default=None, description="Layer 1 fee for Layer 2 chains", alias="l1Fee")
    __properties: ClassVar[List[str]] = ["feePerByte", "gasPrice", "gasLimit", "networkFee", "baseFee", "priorityFee", "maxFeePerGasDelta", "l1Fee"]

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
        """Create an instance of TransactionFee from a JSON string"""
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
        """Create an instance of TransactionFee from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "feePerByte": obj.get("feePerByte"),
            "gasPrice": obj.get("gasPrice"),
            "gasLimit": obj.get("gasLimit"),
            "networkFee": obj.get("networkFee"),
            "baseFee": obj.get("baseFee"),
            "priorityFee": obj.get("priorityFee"),
            "maxFeePerGasDelta": obj.get("maxFeePerGasDelta"),
            "l1Fee": obj.get("l1Fee")
        })
        return _obj


