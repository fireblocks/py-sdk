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

from pydantic import BaseModel, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from fireblocks_client.models.conversion_operation_config_params import ConversionOperationConfigParams
from fireblocks_client.models.conversion_operation_execution_output import ConversionOperationExecutionOutput
from fireblocks_client.models.conversion_operation_failure import ConversionOperationFailure
from typing import Optional, Set
from typing_extensions import Self

class ConversionOperationExecution(BaseModel):
    """
    ConversionOperationExecution
    """ # noqa: E501
    input: ConversionOperationConfigParams
    output: Optional[ConversionOperationExecutionOutput] = None
    started_at: Union[StrictFloat, StrictInt] = Field(alias="startedAt")
    finished_at: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="finishedAt")
    failure: Optional[ConversionOperationFailure] = None
    __properties: ClassVar[List[str]] = ["input", "output", "startedAt", "finishedAt", "failure"]

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
        """Create an instance of ConversionOperationExecution from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of input
        if self.input:
            _dict['input'] = self.input.to_dict()
        # override the default output from pydantic by calling `to_dict()` of output
        if self.output:
            _dict['output'] = self.output.to_dict()
        # override the default output from pydantic by calling `to_dict()` of failure
        if self.failure:
            _dict['failure'] = self.failure.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConversionOperationExecution from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "input": ConversionOperationConfigParams.from_dict(obj["input"]) if obj.get("input") is not None else None,
            "output": ConversionOperationExecutionOutput.from_dict(obj["output"]) if obj.get("output") is not None else None,
            "startedAt": obj.get("startedAt"),
            "finishedAt": obj.get("finishedAt"),
            "failure": ConversionOperationFailure.from_dict(obj["failure"]) if obj.get("failure") is not None else None
        })
        return _obj


