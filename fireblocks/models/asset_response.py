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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from fireblocks.models.asset_metadata import AssetMetadata
from fireblocks.models.asset_onchain import AssetOnchain
from typing import Optional, Set
from typing_extensions import Self

class AssetResponse(BaseModel):
    """
    AssetResponse
    """ # noqa: E501
    legacy_id: StrictStr = Field(alias="legacyId")
    asset_class: StrictStr = Field(alias="assetClass")
    onchain: AssetOnchain
    metadata: AssetMetadata
    __properties: ClassVar[List[str]] = ["legacyId", "assetClass", "onchain", "metadata"]

    @field_validator('asset_class')
    def asset_class_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['NATIVE', 'FT', 'NFT', 'SFT']):
            raise ValueError("must be one of enum values ('NATIVE', 'FT', 'NFT', 'SFT')")
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
        """Create an instance of AssetResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of onchain
        if self.onchain:
            _dict['onchain'] = self.onchain.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AssetResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "legacyId": obj.get("legacyId"),
            "assetClass": obj.get("assetClass"),
            "onchain": AssetOnchain.from_dict(obj["onchain"]) if obj.get("onchain") is not None else None,
            "metadata": AssetMetadata.from_dict(obj["metadata"]) if obj.get("metadata") is not None else None
        })
        return _obj


