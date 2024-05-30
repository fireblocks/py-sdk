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
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Optional
from fireblocks.models.conversion_operation_execution_params import ConversionOperationExecutionParams
from fireblocks.models.disbursement_operation_execution_params import DisbursementOperationExecutionParams
from fireblocks.models.transfer_operation_execution_params import TransferOperationExecutionParams
from typing import Union, Any, List, Set, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field

CREATEWORKFLOWEXECUTIONREQUESTPARAMSINNER_ANY_OF_SCHEMAS = ["ConversionOperationExecutionParams", "DisbursementOperationExecutionParams", "TransferOperationExecutionParams"]

class CreateWorkflowExecutionRequestParamsInner(BaseModel):
    """
    CreateWorkflowExecutionRequestParamsInner
    """

    # data type: ConversionOperationExecutionParams
    anyof_schema_1_validator: Optional[ConversionOperationExecutionParams] = None
    # data type: TransferOperationExecutionParams
    anyof_schema_2_validator: Optional[TransferOperationExecutionParams] = None
    # data type: DisbursementOperationExecutionParams
    anyof_schema_3_validator: Optional[DisbursementOperationExecutionParams] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[ConversionOperationExecutionParams, DisbursementOperationExecutionParams, TransferOperationExecutionParams]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: Set[str] = { "ConversionOperationExecutionParams", "DisbursementOperationExecutionParams", "TransferOperationExecutionParams" }

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
    def actual_instance_must_validate_anyof(cls, v):
        instance = CreateWorkflowExecutionRequestParamsInner.model_construct()
        error_messages = []
        # validate data type: ConversionOperationExecutionParams
        if not isinstance(v, ConversionOperationExecutionParams):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ConversionOperationExecutionParams`")
        else:
            return v

        # validate data type: TransferOperationExecutionParams
        if not isinstance(v, TransferOperationExecutionParams):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransferOperationExecutionParams`")
        else:
            return v

        # validate data type: DisbursementOperationExecutionParams
        if not isinstance(v, DisbursementOperationExecutionParams):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DisbursementOperationExecutionParams`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in CreateWorkflowExecutionRequestParamsInner with anyOf schemas: ConversionOperationExecutionParams, DisbursementOperationExecutionParams, TransferOperationExecutionParams. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[ConversionOperationExecutionParams] = None
        try:
            instance.actual_instance = ConversionOperationExecutionParams.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[TransferOperationExecutionParams] = None
        try:
            instance.actual_instance = TransferOperationExecutionParams.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_3_validator: Optional[DisbursementOperationExecutionParams] = None
        try:
            instance.actual_instance = DisbursementOperationExecutionParams.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into CreateWorkflowExecutionRequestParamsInner with anyOf schemas: ConversionOperationExecutionParams, DisbursementOperationExecutionParams, TransferOperationExecutionParams. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], ConversionOperationExecutionParams, DisbursementOperationExecutionParams, TransferOperationExecutionParams]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


