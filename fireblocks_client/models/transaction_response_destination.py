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

from pydantic import BaseModel, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from fireblocks_client.models.aml_screening_result import AmlScreeningResult
from fireblocks_client.models.authorization_info import AuthorizationInfo
from fireblocks_client.models.destination_transfer_peer_path_response import DestinationTransferPeerPathResponse
from typing import Optional, Set
from typing_extensions import Self

class TransactionResponseDestination(BaseModel):
    """
    TransactionResponseDestination
    """ # noqa: E501
    destination_address: Optional[Any] = Field(default=None, description="Address where the asset was transferred.", alias="destinationAddress")
    destination_address_description: Optional[Any] = Field(default=None, description="Description of the address.", alias="destinationAddressDescription")
    amount: Optional[StrictStr] = Field(default=None, description="The amount to be sent to this destination.")
    amount_usd: Optional[StrictStr] = Field(default=None, description="The USD value of the requested amount.", alias="amountUSD")
    aml_screening_result: Optional[AmlScreeningResult] = Field(default=None, alias="amlScreeningResult")
    destination: Optional[DestinationTransferPeerPathResponse] = None
    authorization_info: Optional[AuthorizationInfo] = Field(default=None, alias="authorizationInfo")
    __properties: ClassVar[List[str]] = ["destinationAddress", "destinationAddressDescription", "amount", "amountUSD", "amlScreeningResult", "destination", "authorizationInfo"]

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
        """Create an instance of TransactionResponseDestination from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of aml_screening_result
        if self.aml_screening_result:
            _dict['amlScreeningResult'] = self.aml_screening_result.to_dict()
        # override the default output from pydantic by calling `to_dict()` of destination
        if self.destination:
            _dict['destination'] = self.destination.to_dict()
        # override the default output from pydantic by calling `to_dict()` of authorization_info
        if self.authorization_info:
            _dict['authorizationInfo'] = self.authorization_info.to_dict()
        # set to None if destination_address (nullable) is None
        # and model_fields_set contains the field
        if self.destination_address is None and "destination_address" in self.model_fields_set:
            _dict['destinationAddress'] = None

        # set to None if destination_address_description (nullable) is None
        # and model_fields_set contains the field
        if self.destination_address_description is None and "destination_address_description" in self.model_fields_set:
            _dict['destinationAddressDescription'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionResponseDestination from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "destinationAddress": obj.get("destinationAddress"),
            "destinationAddressDescription": obj.get("destinationAddressDescription"),
            "amount": obj.get("amount"),
            "amountUSD": obj.get("amountUSD"),
            "amlScreeningResult": AmlScreeningResult.from_dict(obj["amlScreeningResult"]) if obj.get("amlScreeningResult") is not None else None,
            "destination": DestinationTransferPeerPathResponse.from_dict(obj["destination"]) if obj.get("destination") is not None else None,
            "authorizationInfo": AuthorizationInfo.from_dict(obj["authorizationInfo"]) if obj.get("authorizationInfo") is not None else None
        })
        return _obj


