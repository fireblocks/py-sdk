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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Union
from fireblocks.models.session_metadata import SessionMetadata
from typing import Optional, Set
from typing_extensions import Self

class SessionDTO(BaseModel):
    """
    SessionDTO
    """ # noqa: E501
    id: StrictStr = Field(description="Id of the connection")
    user_id: StrictStr = Field(description="Id of the user that created the connection", alias="userId")
    session_metadata: SessionMetadata = Field(description="Metadata of the connection (provided by the dapp)", alias="sessionMetadata")
    vault_account_id: Union[StrictFloat, StrictInt] = Field(description="The vault to connect", alias="vaultAccountId")
    fee_level: StrictStr = Field(description="The default fee level", alias="feeLevel")
    chain_ids: List[StrictStr] = Field(description="The chains approved for the connection", alias="chainIds")
    connection_type: StrictStr = Field(description="The connection's type", alias="connectionType")
    connection_method: StrictStr = Field(description="The method through which the connection was established", alias="connectionMethod")
    creation_date: datetime = Field(description="Timestamp of the session's creation", alias="creationDate")
    __properties: ClassVar[List[str]] = ["id", "userId", "sessionMetadata", "vaultAccountId", "feeLevel", "chainIds", "connectionType", "connectionMethod", "creationDate"]

    @field_validator('fee_level')
    def fee_level_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['MEDIUM', 'HIGH']):
            raise ValueError("must be one of enum values ('MEDIUM', 'HIGH')")
        return value

    @field_validator('connection_type')
    def connection_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['WalletConnect']):
            raise ValueError("must be one of enum values ('WalletConnect')")
        return value

    @field_validator('connection_method')
    def connection_method_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['DESKTOP', 'MOBILE', 'API']):
            raise ValueError("must be one of enum values ('DESKTOP', 'MOBILE', 'API')")
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
        """Create an instance of SessionDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of session_metadata
        if self.session_metadata:
            _dict['sessionMetadata'] = self.session_metadata.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SessionDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "userId": obj.get("userId"),
            "sessionMetadata": SessionMetadata.from_dict(obj["sessionMetadata"]) if obj.get("sessionMetadata") is not None else None,
            "vaultAccountId": obj.get("vaultAccountId"),
            "feeLevel": obj.get("feeLevel"),
            "chainIds": obj.get("chainIds"),
            "connectionType": obj.get("connectionType"),
            "connectionMethod": obj.get("connectionMethod"),
            "creationDate": obj.get("creationDate")
        })
        return _obj


