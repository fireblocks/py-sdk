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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from fireblocks.models.exchange_asset import ExchangeAsset
from fireblocks.models.exchange_trading_account import ExchangeTradingAccount
from fireblocks.models.exchange_type import ExchangeType
from typing import Optional, Set
from typing_extensions import Self

class ExchangeAccount(BaseModel):
    """
    ExchangeAccount
    """ # noqa: E501
    id: Optional[StrictStr] = None
    type: Optional[ExchangeType] = None
    name: Optional[StrictStr] = Field(default=None, description="Display name of the exchange account")
    status: Optional[StrictStr] = None
    assets: Optional[List[ExchangeAsset]] = None
    success: Optional[StrictBool] = Field(default=None, description="Did succeed in retrieve balance data")
    trading_accounts: Optional[List[ExchangeTradingAccount]] = Field(default=None, alias="tradingAccounts")
    is_subaccount: Optional[StrictBool] = Field(default=None, description="True if the account is a subaccount in an exchange", alias="isSubaccount")
    main_account_id: Optional[StrictStr] = Field(default=None, description="if the account is a sub-account, the ID of the main account", alias="mainAccountId")
    __properties: ClassVar[List[str]] = ["id", "type", "name", "status", "assets", "success", "tradingAccounts", "isSubaccount", "mainAccountId"]

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
        """Create an instance of ExchangeAccount from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in assets (list)
        _items = []
        if self.assets:
            for _item in self.assets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['assets'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in trading_accounts (list)
        _items = []
        if self.trading_accounts:
            for _item in self.trading_accounts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tradingAccounts'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExchangeAccount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "name": obj.get("name"),
            "status": obj.get("status"),
            "assets": [ExchangeAsset.from_dict(_item) for _item in obj["assets"]] if obj.get("assets") is not None else None,
            "success": obj.get("success"),
            "tradingAccounts": [ExchangeTradingAccount.from_dict(_item) for _item in obj["tradingAccounts"]] if obj.get("tradingAccounts") is not None else None,
            "isSubaccount": obj.get("isSubaccount"),
            "mainAccountId": obj.get("mainAccountId")
        })
        return _obj


