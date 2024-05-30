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
from fireblocks_client.models.disbursement_operation_execution import DisbursementOperationExecution
from fireblocks_client.models.disbursement_operation_preview import DisbursementOperationPreview
from fireblocks_client.models.disbursement_operation_type import DisbursementOperationType
from fireblocks_client.models.disbursement_validation_failure import DisbursementValidationFailure
from fireblocks_client.models.execution_operation_status import ExecutionOperationStatus
from typing import Optional, Set
from typing_extensions import Self

class ExecutionDisbursementOperation(BaseModel):
    """
    ExecutionDisbursementOperation
    """ # noqa: E501
    operation_id: StrictStr = Field(alias="operationId")
    status: ExecutionOperationStatus
    validation_failure: Optional[DisbursementValidationFailure] = Field(default=None, alias="validationFailure")
    operation_type: DisbursementOperationType = Field(alias="operationType")
    preview: Optional[DisbursementOperationPreview] = None
    execution: Optional[DisbursementOperationExecution] = None
    __properties: ClassVar[List[str]] = ["operationId", "status", "validationFailure", "operationType", "preview", "execution"]

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
        """Create an instance of ExecutionDisbursementOperation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of validation_failure
        if self.validation_failure:
            _dict['validationFailure'] = self.validation_failure.to_dict()
        # override the default output from pydantic by calling `to_dict()` of preview
        if self.preview:
            _dict['preview'] = self.preview.to_dict()
        # override the default output from pydantic by calling `to_dict()` of execution
        if self.execution:
            _dict['execution'] = self.execution.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExecutionDisbursementOperation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "operationId": obj.get("operationId"),
            "status": obj.get("status"),
            "validationFailure": DisbursementValidationFailure.from_dict(obj["validationFailure"]) if obj.get("validationFailure") is not None else None,
            "operationType": obj.get("operationType"),
            "preview": DisbursementOperationPreview.from_dict(obj["preview"]) if obj.get("preview") is not None else None,
            "execution": DisbursementOperationExecution.from_dict(obj["execution"]) if obj.get("execution") is not None else None
        })
        return _obj


