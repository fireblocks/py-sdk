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
from fireblocks.models.travel_rule_persons import TravelRulePersons
from typing import Optional, Set
from typing_extensions import Self

class TravelRulePiiIVMS(BaseModel):
    """
    TravelRulePiiIVMS
    """ # noqa: E501
    originator_persons: Optional[List[TravelRulePersons]] = Field(default=None, alias="originatorPersons")
    beneficiary_persons: Optional[List[TravelRulePersons]] = Field(default=None, alias="beneficiaryPersons")
    account_number: Optional[List[StrictStr]] = Field(default=None, alias="accountNumber")
    __properties: ClassVar[List[str]] = ["originatorPersons", "beneficiaryPersons", "accountNumber"]

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
        """Create an instance of TravelRulePiiIVMS from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in originator_persons (list)
        _items = []
        if self.originator_persons:
            for _item in self.originator_persons:
                if _item:
                    _items.append(_item.to_dict())
            _dict['originatorPersons'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in beneficiary_persons (list)
        _items = []
        if self.beneficiary_persons:
            for _item in self.beneficiary_persons:
                if _item:
                    _items.append(_item.to_dict())
            _dict['beneficiaryPersons'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TravelRulePiiIVMS from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "originatorPersons": [TravelRulePersons.from_dict(_item) for _item in obj["originatorPersons"]] if obj.get("originatorPersons") is not None else None,
            "beneficiaryPersons": [TravelRulePersons.from_dict(_item) for _item in obj["beneficiaryPersons"]] if obj.get("beneficiaryPersons") is not None else None,
            "accountNumber": obj.get("accountNumber")
        })
        return _obj


