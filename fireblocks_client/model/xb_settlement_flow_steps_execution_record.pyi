# coding: utf-8

"""
    Fireblocks API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.6.2
    Contact: support@fireblocks.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from fireblocks_client import schemas  # noqa: F401


class XBSettlementFlowStepsExecutionRecord(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def stepType() -> typing.Type['XBSettlementStepType']:
                return XBSettlementStepType
            __annotations__ = {
                "stepType": stepType,
            }
        
        @staticmethod
        def additional_properties() -> typing.Type['XBSettlementFlowExecutionStep']:
            return XBSettlementFlowExecutionStep
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stepType"]) -> 'XBSettlementStepType': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> 'XBSettlementFlowExecutionStep': ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["stepType"], str, ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stepType"]) -> typing.Union['XBSettlementStepType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union['XBSettlementFlowExecutionStep', schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["stepType"], str, ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        stepType: typing.Union['XBSettlementStepType', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: 'XBSettlementFlowExecutionStep',
    ) -> 'XBSettlementFlowStepsExecutionRecord':
        return super().__new__(
            cls,
            *_args,
            stepType=stepType,
            _configuration=_configuration,
            **kwargs,
        )

from fireblocks_client.model.xb_settlement_flow_execution_step import XBSettlementFlowExecutionStep
from fireblocks_client.model.xb_settlement_step_type import XBSettlementStepType
