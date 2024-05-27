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
import json
import pprint
from pydantic import BaseModel, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from fireblocks_client.models.config_conversion_operation_snapshot import ConfigConversionOperationSnapshot
from fireblocks_client.models.config_disbursement_operation_snapshot import ConfigDisbursementOperationSnapshot
from fireblocks_client.models.config_transfer_operation_snapshot import ConfigTransferOperationSnapshot
from pydantic import StrictStr, Field
from typing import Union, List, Optional, Dict
from typing_extensions import Literal, Self

CONFIGOPERATIONSNAPSHOT_ONE_OF_SCHEMAS = ["ConfigConversionOperationSnapshot", "ConfigDisbursementOperationSnapshot", "ConfigTransferOperationSnapshot"]

class ConfigOperationSnapshot(BaseModel):
    """
    ConfigOperationSnapshot
    """
    # data type: ConfigConversionOperationSnapshot
    oneof_schema_1_validator: Optional[ConfigConversionOperationSnapshot] = None
    # data type: ConfigTransferOperationSnapshot
    oneof_schema_2_validator: Optional[ConfigTransferOperationSnapshot] = None
    # data type: ConfigDisbursementOperationSnapshot
    oneof_schema_3_validator: Optional[ConfigDisbursementOperationSnapshot] = None
    actual_instance: Optional[Union[ConfigConversionOperationSnapshot, ConfigDisbursementOperationSnapshot, ConfigTransferOperationSnapshot]] = None
    one_of_schemas: List[str] = Field(default=Literal["ConfigConversionOperationSnapshot", "ConfigDisbursementOperationSnapshot", "ConfigTransferOperationSnapshot"])

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = ConfigOperationSnapshot.model_construct()
        error_messages = []
        match = 0
        # validate data type: ConfigConversionOperationSnapshot
        if not isinstance(v, ConfigConversionOperationSnapshot):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ConfigConversionOperationSnapshot`")
        else:
            match += 1
        # validate data type: ConfigTransferOperationSnapshot
        if not isinstance(v, ConfigTransferOperationSnapshot):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ConfigTransferOperationSnapshot`")
        else:
            match += 1
        # validate data type: ConfigDisbursementOperationSnapshot
        if not isinstance(v, ConfigDisbursementOperationSnapshot):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ConfigDisbursementOperationSnapshot`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ConfigOperationSnapshot with oneOf schemas: ConfigConversionOperationSnapshot, ConfigDisbursementOperationSnapshot, ConfigTransferOperationSnapshot. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ConfigOperationSnapshot with oneOf schemas: ConfigConversionOperationSnapshot, ConfigDisbursementOperationSnapshot, ConfigTransferOperationSnapshot. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into ConfigConversionOperationSnapshot
        try:
            instance.actual_instance = ConfigConversionOperationSnapshot.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ConfigTransferOperationSnapshot
        try:
            instance.actual_instance = ConfigTransferOperationSnapshot.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ConfigDisbursementOperationSnapshot
        try:
            instance.actual_instance = ConfigDisbursementOperationSnapshot.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ConfigOperationSnapshot with oneOf schemas: ConfigConversionOperationSnapshot, ConfigDisbursementOperationSnapshot, ConfigTransferOperationSnapshot. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ConfigOperationSnapshot with oneOf schemas: ConfigConversionOperationSnapshot, ConfigDisbursementOperationSnapshot, ConfigTransferOperationSnapshot. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], ConfigConversionOperationSnapshot, ConfigDisbursementOperationSnapshot, ConfigTransferOperationSnapshot]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


