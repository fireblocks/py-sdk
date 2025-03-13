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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from fireblocks.models.smart_transfer_ticket_term import SmartTransferTicketTerm
from typing import Optional, Set
from typing_extensions import Self

class SmartTransferTicket(BaseModel):
    """
    Data object with result data
    """ # noqa: E501
    id: StrictStr = Field(description="Unique id of Smart Transfer ticket")
    type: StrictStr = Field(description="Kind of Smart Transfer. Can be either `ASYNC` or `DVP`")
    direction: Optional[StrictStr] = Field(default=None, description="Direction of Smart Transfer.")
    status: StrictStr = Field(description="Current status of Smart Transfer ticket")
    dvp_execution_status: Optional[StrictStr] = Field(default=None, description="Current status of DVP execution", alias="dvpExecutionStatus")
    order_created_by_network_id: Optional[StrictStr] = Field(default=None, description="ID of network profile that created order", alias="orderCreatedByNetworkId")
    terms: Optional[List[Optional[SmartTransferTicketTerm]]] = Field(default=None, description="Ticket terms (legs)")
    expires_in: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Number of hours for expiration.This data is valid only it ticket not in DRAFT state and it will be used to calculate expiresAt value", alias="expiresIn")
    expires_at: Optional[datetime] = Field(default=None, description="Date and time at which the ticket will expire if no funding is performed.", alias="expiresAt")
    submitted_at: Optional[datetime] = Field(default=None, description="Date and time when ticket is submitted.", alias="submittedAt")
    expired_at: Optional[datetime] = Field(default=None, description="Date and time when ticket is expired.", alias="expiredAt")
    canceled_at: Optional[datetime] = Field(default=None, description="Date and time when ticket is canceled.", alias="canceledAt")
    fulfilled_at: Optional[datetime] = Field(default=None, description="Date and time when ticket is fulfilled.", alias="fulfilledAt")
    external_ref_id: Optional[StrictStr] = Field(default=None, description="External Ref ID for Smart Transfer ticket.", alias="externalRefId")
    note: Optional[StrictStr] = Field(default=None, description="Note")
    created_by_network_id: StrictStr = Field(description="ID of network profile that created ticket", alias="createdByNetworkId")
    created_by_network_id_name: StrictStr = Field(description="Name of network profile that created ticket", alias="createdByNetworkIdName")
    canceled_by_network_id_name: Optional[StrictStr] = Field(default=None, description="Name of network profile that canceled ticket", alias="canceledByNetworkIdName")
    created_at: datetime = Field(description="Date and time at which the ticket is created.", alias="createdAt")
    updated_at: datetime = Field(description="Date and time of last ticket update.", alias="updatedAt")
    canceled_by_me: Optional[StrictBool] = Field(default=None, alias="canceledByMe")
    created_by_me: Optional[StrictBool] = Field(default=None, alias="createdByMe")
    __properties: ClassVar[List[str]] = ["id", "type", "direction", "status", "dvpExecutionStatus", "orderCreatedByNetworkId", "terms", "expiresIn", "expiresAt", "submittedAt", "expiredAt", "canceledAt", "fulfilledAt", "externalRefId", "note", "createdByNetworkId", "createdByNetworkIdName", "canceledByNetworkIdName", "createdAt", "updatedAt", "canceledByMe", "createdByMe"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['ASYNC', 'DVP']):
            raise ValueError("must be one of enum values ('ASYNC', 'DVP')")
        return value

    @field_validator('direction')
    def direction_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['EXCHANGE', 'SEND', 'RECEIVE', 'INTERMEDIATE']):
            raise ValueError("must be one of enum values ('EXCHANGE', 'SEND', 'RECEIVE', 'INTERMEDIATE')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['DRAFT', 'PENDING_APPROVAL', 'OPEN', 'IN_SETTLEMENT', 'FULFILLED', 'EXPIRED', 'CANCELED']):
            raise ValueError("must be one of enum values ('DRAFT', 'PENDING_APPROVAL', 'OPEN', 'IN_SETTLEMENT', 'FULFILLED', 'EXPIRED', 'CANCELED')")
        return value

    @field_validator('dvp_execution_status')
    def dvp_execution_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['STARTED', 'CREATING_ORDER', 'ORDER_CREATED', 'FULFILLING', 'FULFILLING_ORDER_FAILED', 'CREATING_ORDER_FAILED', 'FULFILLED']):
            raise ValueError("must be one of enum values ('STARTED', 'CREATING_ORDER', 'ORDER_CREATED', 'FULFILLING', 'FULFILLING_ORDER_FAILED', 'CREATING_ORDER_FAILED', 'FULFILLED')")
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
        """Create an instance of SmartTransferTicket from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in terms (list)
        _items = []
        if self.terms:
            for _item_terms in self.terms:
                if _item_terms:
                    _items.append(_item_terms.to_dict())
            _dict['terms'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SmartTransferTicket from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "direction": obj.get("direction"),
            "status": obj.get("status"),
            "dvpExecutionStatus": obj.get("dvpExecutionStatus"),
            "orderCreatedByNetworkId": obj.get("orderCreatedByNetworkId"),
            "terms": [SmartTransferTicketTerm.from_dict(_item) for _item in obj["terms"]] if obj.get("terms") is not None else None,
            "expiresIn": obj.get("expiresIn"),
            "expiresAt": obj.get("expiresAt"),
            "submittedAt": obj.get("submittedAt"),
            "expiredAt": obj.get("expiredAt"),
            "canceledAt": obj.get("canceledAt"),
            "fulfilledAt": obj.get("fulfilledAt"),
            "externalRefId": obj.get("externalRefId"),
            "note": obj.get("note"),
            "createdByNetworkId": obj.get("createdByNetworkId"),
            "createdByNetworkIdName": obj.get("createdByNetworkIdName"),
            "canceledByNetworkIdName": obj.get("canceledByNetworkIdName"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt"),
            "canceledByMe": obj.get("canceledByMe"),
            "createdByMe": obj.get("createdByMe")
        })
        return _obj


