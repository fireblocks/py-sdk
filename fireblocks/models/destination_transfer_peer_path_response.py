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
from fireblocks.models.transfer_peer_path_type import TransferPeerPathType
from typing import Optional, Set
from typing_extensions import Self

class DestinationTransferPeerPathResponse(BaseModel):
    """
    Destination of the transaction.  **Note:** In case the transaction is sent to multiple destinations, the `destinations` parameter is be used instead of this.
    """ # noqa: E501
    type: TransferPeerPathType
    sub_type: Optional[StrictStr] = Field(default=None, description="In case the type is set to `EXCHANGE_ACCOUNT` or `FIAT_ACCOUNT`, the specific exchange vendor name or fiat vendor name.In case the type is set to `INTERNAL_WALLET` or `EXTERNAL_WALLET`, the subType is set to `Internal` or `External`.", alias="subType")
    id: Optional[StrictStr] = Field(default=None, description="The ID of the peer. You can retrieve the ID of each venue object using the endpoints for [listing vault accounts](https://developers.fireblocks.com/reference/get_vault-accounts-paged), [listing exchange account](https://developers.fireblocks.com/reference/get_exchange-accounts), [listing fiat accounts](https://developers.fireblocks.com/reference/get_fiat-accounts), [listing internal wallets](https://developers.fireblocks.com/reference/get_internal-wallets), [listing external wallets](https://developers.fireblocks.com/reference/get_external-wallets), [listing network connections](https://developers.fireblocks.com/reference/get_network-connections). For the other types, this parameter is not needed.")
    name: Optional[StrictStr] = Field(default=None, description="The name of the peer.")
    wallet_id: Optional[StrictStr] = Field(default=None, alias="walletId")
    trading_account: Optional[StrictStr] = Field(default=None, description="If this transaction is an exchange internal transfer, this field will be populated with the type of that trading account.", alias="tradingAccount")
    __properties: ClassVar[List[str]] = ["type", "subType", "id", "name", "walletId", "tradingAccount"]

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
        """Create an instance of DestinationTransferPeerPathResponse from a JSON string"""
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
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if trading_account (nullable) is None
        # and model_fields_set contains the field
        if self.trading_account is None and "trading_account" in self.model_fields_set:
            _dict['tradingAccount'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DestinationTransferPeerPathResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "subType": obj.get("subType"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "walletId": obj.get("walletId"),
            "tradingAccount": obj.get("tradingAccount")
        })
        return _obj


