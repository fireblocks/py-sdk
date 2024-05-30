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

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class DisbursementValidationFailure(BaseModel):
    """
    DisbursementValidationFailure
    """ # noqa: E501
    reason: StrictStr
    data: Optional[Dict[str, Any]] = None
    __properties: ClassVar[List[str]] = ["reason", "data"]

    @field_validator('reason')
    def reason_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['ACCOUNT_NOT_FOUND', 'ACCOUNT_TYPE_NOT_SUPPORTED', 'INSUFFICIENT_BALANCE', 'ASSET_NOT_FOUND', 'ASSETS_CONTINUITY_MISMATCH', 'EXCHANGE_BASKETS_MISMATCH', 'ACCOUNTS_CONTINUITY_MISMATCH', 'ONE_TIME_ADDRESS_CONTINUITY_NOT_ALLOWED', 'EQUAL_ACCOUNTS_NOT_ALLOWED', 'EQUAL_ASSETS_NOT_ALLOWED', 'INVALID_AMOUNT', 'UNMANAGED_WALLET_AS_SOURCE_NOT_ALLOWED', 'MANAGED_OPERATION_PARAMS_INVALID_SCHEMA', 'INSTRUCTIONS_EXCEED_HUNDRED_PERCENT', 'INSTRUCTIONS_ARRAY_EMPTY']):
            raise ValueError("must be one of enum values ('ACCOUNT_NOT_FOUND', 'ACCOUNT_TYPE_NOT_SUPPORTED', 'INSUFFICIENT_BALANCE', 'ASSET_NOT_FOUND', 'ASSETS_CONTINUITY_MISMATCH', 'EXCHANGE_BASKETS_MISMATCH', 'ACCOUNTS_CONTINUITY_MISMATCH', 'ONE_TIME_ADDRESS_CONTINUITY_NOT_ALLOWED', 'EQUAL_ACCOUNTS_NOT_ALLOWED', 'EQUAL_ASSETS_NOT_ALLOWED', 'INVALID_AMOUNT', 'UNMANAGED_WALLET_AS_SOURCE_NOT_ALLOWED', 'MANAGED_OPERATION_PARAMS_INVALID_SCHEMA', 'INSTRUCTIONS_EXCEED_HUNDRED_PERCENT', 'INSTRUCTIONS_ARRAY_EMPTY')")
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
        """Create an instance of DisbursementValidationFailure from a JSON string"""
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
        """Create an instance of DisbursementValidationFailure from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "reason": obj.get("reason"),
            "data": obj.get("data")
        })
        return _obj


