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

from pydantic import BaseModel, Field
from typing import Any, ClassVar, Dict, List, Optional
from fireblocks_client.models.amount_aggregation_time_period_method import AmountAggregationTimePeriodMethod
from typing import Optional, Set
from typing_extensions import Self

class PolicyRuleAmountAggregation(BaseModel):
    """
    Defines the method by which the Policy Engine calculates accumulation. It uses the Initiator, Source, and Destination to calculate accumulation toward the value under Minimum, for the time under Time Period. 
    """ # noqa: E501
    operators: Optional[AmountAggregationTimePeriodMethod] = None
    src_transfer_peers: Optional[AmountAggregationTimePeriodMethod] = Field(default=None, alias="srcTransferPeers")
    dst_transfer_peers: Optional[AmountAggregationTimePeriodMethod] = Field(default=None, alias="dstTransferPeers")
    __properties: ClassVar[List[str]] = ["operators", "srcTransferPeers", "dstTransferPeers"]

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
        """Create an instance of PolicyRuleAmountAggregation from a JSON string"""
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
        """Create an instance of PolicyRuleAmountAggregation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "operators": obj.get("operators"),
            "srcTransferPeers": obj.get("srcTransferPeers"),
            "dstTransferPeers": obj.get("dstTransferPeers")
        })
        return _obj


