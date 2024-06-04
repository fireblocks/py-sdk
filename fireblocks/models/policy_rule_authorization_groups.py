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
from fireblocks.models.policy_rule_authorization_groups_groups_inner import PolicyRuleAuthorizationGroupsGroupsInner
from typing import Optional, Set
from typing_extensions import Self

class PolicyRuleAuthorizationGroups(BaseModel):
    """
    Defines the transaction approval terms
    """ # noqa: E501
    logic: Optional[StrictStr] = Field(default=None, description="* AND - requires approval of all authorization groups * OR - requires approval of at least one of the authorization groups ")
    allow_operator_as_authorizer: Optional[StrictBool] = Field(default=None, description="Defines whether the user who initiates a transaction can approve their own transaction and count toward the approval threshold for their transaction", alias="allowOperatorAsAuthorizer")
    groups: Optional[List[PolicyRuleAuthorizationGroupsGroupsInner]] = Field(default=None, description="Groups of entities which can approve the transaction")
    __properties: ClassVar[List[str]] = ["logic", "allowOperatorAsAuthorizer", "groups"]

    @field_validator('logic')
    def logic_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['AND', 'OR']):
            raise ValueError("must be one of enum values ('AND', 'OR')")
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
        """Create an instance of PolicyRuleAuthorizationGroups from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in groups (list)
        _items = []
        if self.groups:
            for _item in self.groups:
                if _item:
                    _items.append(_item.to_dict())
            _dict['groups'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PolicyRuleAuthorizationGroups from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "logic": obj.get("logic"),
            "allowOperatorAsAuthorizer": obj.get("allowOperatorAsAuthorizer"),
            "groups": [PolicyRuleAuthorizationGroupsGroupsInner.from_dict(_item) for _item in obj["groups"]] if obj.get("groups") is not None else None
        })
        return _obj

