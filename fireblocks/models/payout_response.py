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
from fireblocks.models.payment_account_response import PaymentAccountResponse
from fireblocks.models.payout_init_method import PayoutInitMethod
from fireblocks.models.payout_instruction_response import PayoutInstructionResponse
from fireblocks.models.payout_state import PayoutState
from fireblocks.models.payout_status import PayoutStatus
from typing import Optional, Set
from typing_extensions import Self

class PayoutResponse(BaseModel):
    """
    PayoutResponse
    """ # noqa: E501
    payout_id: StrictStr = Field(alias="payoutId")
    payment_account: PaymentAccountResponse = Field(alias="paymentAccount")
    created_at: Union[StrictFloat, StrictInt] = Field(alias="createdAt")
    state: PayoutState
    status: PayoutStatus
    reason_of_failure: Optional[StrictStr] = Field(default=None, description="<ul>  <li> INSUFFICIENT_BALANCE</li> <li> SOURCE_TRANSLATION</li> <li> SOURCE_NOT_UNIQUE</li> <li> SOURCE_NOT_FOUND</li> <li> SOURCE_TYPE_NOT_SUPPORTED</li> <li> EMPTY_SOURCE</li> <li> DESTINATION_TRANSLATION</li> <li> DESTINATION_NOT_UNIQUE</li> <li> DESTINATION_NOT_FOUND</li> <li> EMPTY_DESTINATION</li> <li> PARSING </li> <li> UNKNOWN</li> <li> FIREBLOCKS_CLIENT</li> <li> TRANSACTION_SUBMISSION</li> </ul> ", alias="reasonOfFailure")
    init_method: Optional[PayoutInitMethod] = Field(default=None, alias="initMethod")
    instruction_set: List[PayoutInstructionResponse] = Field(alias="instructionSet")
    report_url: Optional[StrictStr] = Field(default=None, alias="reportUrl")
    __properties: ClassVar[List[str]] = ["payoutId", "paymentAccount", "createdAt", "state", "status", "reasonOfFailure", "initMethod", "instructionSet", "reportUrl"]

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
        """Create an instance of PayoutResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of payment_account
        if self.payment_account:
            _dict['paymentAccount'] = self.payment_account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in instruction_set (list)
        _items = []
        if self.instruction_set:
            for _item_instruction_set in self.instruction_set:
                if _item_instruction_set:
                    _items.append(_item_instruction_set.to_dict())
            _dict['instructionSet'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PayoutResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "payoutId": obj.get("payoutId"),
            "paymentAccount": PaymentAccountResponse.from_dict(obj["paymentAccount"]) if obj.get("paymentAccount") is not None else None,
            "createdAt": obj.get("createdAt"),
            "state": obj.get("state"),
            "status": obj.get("status"),
            "reasonOfFailure": obj.get("reasonOfFailure"),
            "initMethod": obj.get("initMethod"),
            "instructionSet": [PayoutInstructionResponse.from_dict(_item) for _item in obj["instructionSet"]] if obj.get("instructionSet") is not None else None,
            "reportUrl": obj.get("reportUrl")
        })
        return _obj


