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
from fireblocks.models.rewards_info import RewardsInfo
from typing import Optional, Set
from typing_extensions import Self

class VaultAsset(BaseModel):
    """
    VaultAsset
    """ # noqa: E501
    id: Optional[StrictStr] = None
    total: Optional[StrictStr] = Field(default=None, description="The total wallet balance. In EOS this value includes the network balance, self staking and pending refund. For all other coins it is the balance as it appears on the blockchain.")
    balance: Optional[StrictStr] = Field(default=None, description="Deprecated - replaced by \"total\"")
    available: Optional[StrictStr] = Field(default=None, description="Funds available for transfer. Equals the blockchain balance minus any locked amounts")
    pending: Optional[StrictStr] = Field(default=None, description="The cumulative balance of all transactions pending to be cleared")
    frozen: Optional[StrictStr] = Field(default=None, description="The cumulative frozen balance")
    locked_amount: Optional[StrictStr] = Field(default=None, description="Funds in outgoing transactions that are not yet published to the network", alias="lockedAmount")
    staked: Optional[StrictStr] = Field(default=None, description="Staked balance")
    total_staked_cpu: Optional[StrictStr] = Field(default=None, description="Deprecated", alias="totalStakedCPU")
    total_staked_network: Optional[StrictStr] = Field(default=None, description="Deprecated", alias="totalStakedNetwork")
    self_staked_cpu: Optional[StrictStr] = Field(default=None, description="Deprecated", alias="selfStakedCPU")
    self_staked_network: Optional[StrictStr] = Field(default=None, description="Deprecated", alias="selfStakedNetwork")
    pending_refund_cpu: Optional[StrictStr] = Field(default=None, description="Deprecated", alias="pendingRefundCPU")
    pending_refund_network: Optional[StrictStr] = Field(default=None, description="Deprecated", alias="pendingRefundNetwork")
    block_height: Optional[StrictStr] = Field(default=None, alias="blockHeight")
    block_hash: Optional[StrictStr] = Field(default=None, alias="blockHash")
    rewards_info: Optional[RewardsInfo] = Field(default=None, alias="rewardsInfo")
    __properties: ClassVar[List[str]] = ["id", "total", "balance", "available", "pending", "frozen", "lockedAmount", "staked", "totalStakedCPU", "totalStakedNetwork", "selfStakedCPU", "selfStakedNetwork", "pendingRefundCPU", "pendingRefundNetwork", "blockHeight", "blockHash", "rewardsInfo"]

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
        """Create an instance of VaultAsset from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of rewards_info
        if self.rewards_info:
            _dict['rewardsInfo'] = self.rewards_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VaultAsset from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "total": obj.get("total"),
            "balance": obj.get("balance"),
            "available": obj.get("available"),
            "pending": obj.get("pending"),
            "frozen": obj.get("frozen"),
            "lockedAmount": obj.get("lockedAmount"),
            "staked": obj.get("staked"),
            "totalStakedCPU": obj.get("totalStakedCPU"),
            "totalStakedNetwork": obj.get("totalStakedNetwork"),
            "selfStakedCPU": obj.get("selfStakedCPU"),
            "selfStakedNetwork": obj.get("selfStakedNetwork"),
            "pendingRefundCPU": obj.get("pendingRefundCPU"),
            "pendingRefundNetwork": obj.get("pendingRefundNetwork"),
            "blockHeight": obj.get("blockHeight"),
            "blockHash": obj.get("blockHash"),
            "rewardsInfo": RewardsInfo.from_dict(obj["rewardsInfo"]) if obj.get("rewardsInfo") is not None else None
        })
        return _obj


