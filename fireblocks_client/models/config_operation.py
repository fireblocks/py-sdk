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
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from fireblocks_client.models.conversion_config_operation import ConversionConfigOperation
from fireblocks_client.models.disbursement_config_operation import DisbursementConfigOperation
from fireblocks_client.models.transfer_config_operation import TransferConfigOperation
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

CONFIGOPERATION_ONE_OF_SCHEMAS = ["ConversionConfigOperation", "DisbursementConfigOperation", "TransferConfigOperation"]

class ConfigOperation(BaseModel):
    """
    ConfigOperation
    """
    # data type: ConversionConfigOperation
    oneof_schema_1_validator: Optional[ConversionConfigOperation] = None
    # data type: TransferConfigOperation
    oneof_schema_2_validator: Optional[TransferConfigOperation] = None
    # data type: DisbursementConfigOperation
    oneof_schema_3_validator: Optional[DisbursementConfigOperation] = None
    actual_instance: Optional[Union[ConversionConfigOperation, DisbursementConfigOperation, TransferConfigOperation]] = None
    one_of_schemas: Set[str] = { "ConversionConfigOperation", "DisbursementConfigOperation", "TransferConfigOperation" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


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
        instance = ConfigOperation.model_construct()
        error_messages = []
        match = 0
        # validate data type: ConversionConfigOperation
        if not isinstance(v, ConversionConfigOperation):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ConversionConfigOperation`")
        else:
            match += 1
        # validate data type: TransferConfigOperation
        if not isinstance(v, TransferConfigOperation):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransferConfigOperation`")
        else:
            match += 1
        # validate data type: DisbursementConfigOperation
        if not isinstance(v, DisbursementConfigOperation):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DisbursementConfigOperation`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ConfigOperation with oneOf schemas: ConversionConfigOperation, DisbursementConfigOperation, TransferConfigOperation. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ConfigOperation with oneOf schemas: ConversionConfigOperation, DisbursementConfigOperation, TransferConfigOperation. Details: " + ", ".join(error_messages))
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

        # deserialize data into ConversionConfigOperation
        try:
            instance.actual_instance = ConversionConfigOperation.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TransferConfigOperation
        try:
            instance.actual_instance = TransferConfigOperation.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into DisbursementConfigOperation
        try:
            instance.actual_instance = DisbursementConfigOperation.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ConfigOperation with oneOf schemas: ConversionConfigOperation, DisbursementConfigOperation, TransferConfigOperation. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ConfigOperation with oneOf schemas: ConversionConfigOperation, DisbursementConfigOperation, TransferConfigOperation. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], ConversionConfigOperation, DisbursementConfigOperation, TransferConfigOperation]]:
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


