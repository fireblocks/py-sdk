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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class ComplianceScreeningResult(BaseModel):
    """
    ComplianceScreeningResult
    """ # noqa: E501
    provider: Optional[StrictStr] = None
    payload: Optional[Dict[str, Any]] = Field(default=None, description="The payload of the screening result. The payload is a JSON object that contains the screening result. The payload is different for each screening provider. ")
    bypass_reason: Optional[StrictStr] = Field(default=None, alias="bypassReason")
    screening_status: Optional[StrictStr] = Field(default=None, alias="screeningStatus")
    timestamp: Optional[Union[StrictFloat, StrictInt]] = None
    __properties: ClassVar[List[str]] = ["provider", "payload", "bypassReason", "screeningStatus", "timestamp"]

    @field_validator('screening_status')
    def screening_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['COMPLETED', 'PENDING', 'BYPASSED', 'FAILED', 'FROZEN']):
            raise ValueError("must be one of enum values ('COMPLETED', 'PENDING', 'BYPASSED', 'FAILED', 'FROZEN')")
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
        """Create an instance of ComplianceScreeningResult from a JSON string"""
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
        """Create an instance of ComplianceScreeningResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "provider": obj.get("provider"),
            "payload": obj.get("payload"),
            "bypassReason": obj.get("bypassReason"),
            "screeningStatus": obj.get("screeningStatus"),
            "timestamp": obj.get("timestamp")
        })
        return _obj

