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


class XBSettlementFlowPreviewModel(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "estimatedOutputAmount",
            "totalEstimatedTime",
            "configId",
            "totalEstimatedFee",
            "inputAmount",
            "conversionRate",
            "flowId",
            "steps",
        }
        
        class properties:
            flowId = schemas.StrSchema
            configId = schemas.UUIDSchema
            conversionRate = schemas.StrSchema
        
            @staticmethod
            def inputAmount() -> typing.Type['XBSettlementAsset']:
                return XBSettlementAsset
        
            @staticmethod
            def estimatedOutputAmount() -> typing.Type['XBSettlementAsset']:
                return XBSettlementAsset
        
            @staticmethod
            def totalEstimatedFee() -> typing.Type['XBSettlementAsset']:
                return XBSettlementAsset
            totalEstimatedTime = schemas.NumberSchema
        
            @staticmethod
            def steps() -> typing.Type['XBSettlementFlowStepsRecord']:
                return XBSettlementFlowStepsRecord
            __annotations__ = {
                "flowId": flowId,
                "configId": configId,
                "conversionRate": conversionRate,
                "inputAmount": inputAmount,
                "estimatedOutputAmount": estimatedOutputAmount,
                "totalEstimatedFee": totalEstimatedFee,
                "totalEstimatedTime": totalEstimatedTime,
                "steps": steps,
            }
    
    estimatedOutputAmount: 'XBSettlementAsset'
    totalEstimatedTime: MetaOapg.properties.totalEstimatedTime
    configId: MetaOapg.properties.configId
    totalEstimatedFee: 'XBSettlementAsset'
    inputAmount: 'XBSettlementAsset'
    conversionRate: MetaOapg.properties.conversionRate
    flowId: MetaOapg.properties.flowId
    steps: 'XBSettlementFlowStepsRecord'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["flowId"]) -> MetaOapg.properties.flowId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["configId"]) -> MetaOapg.properties.configId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conversionRate"]) -> MetaOapg.properties.conversionRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inputAmount"]) -> 'XBSettlementAsset': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["estimatedOutputAmount"]) -> 'XBSettlementAsset': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalEstimatedFee"]) -> 'XBSettlementAsset': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalEstimatedTime"]) -> MetaOapg.properties.totalEstimatedTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["steps"]) -> 'XBSettlementFlowStepsRecord': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["flowId", "configId", "conversionRate", "inputAmount", "estimatedOutputAmount", "totalEstimatedFee", "totalEstimatedTime", "steps", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["flowId"]) -> MetaOapg.properties.flowId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["configId"]) -> MetaOapg.properties.configId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conversionRate"]) -> MetaOapg.properties.conversionRate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inputAmount"]) -> 'XBSettlementAsset': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["estimatedOutputAmount"]) -> 'XBSettlementAsset': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalEstimatedFee"]) -> 'XBSettlementAsset': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalEstimatedTime"]) -> MetaOapg.properties.totalEstimatedTime: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["steps"]) -> 'XBSettlementFlowStepsRecord': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["flowId", "configId", "conversionRate", "inputAmount", "estimatedOutputAmount", "totalEstimatedFee", "totalEstimatedTime", "steps", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        estimatedOutputAmount: 'XBSettlementAsset',
        totalEstimatedTime: typing.Union[MetaOapg.properties.totalEstimatedTime, decimal.Decimal, int, float, ],
        configId: typing.Union[MetaOapg.properties.configId, str, uuid.UUID, ],
        totalEstimatedFee: 'XBSettlementAsset',
        inputAmount: 'XBSettlementAsset',
        conversionRate: typing.Union[MetaOapg.properties.conversionRate, str, ],
        flowId: typing.Union[MetaOapg.properties.flowId, str, ],
        steps: 'XBSettlementFlowStepsRecord',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XBSettlementFlowPreviewModel':
        return super().__new__(
            cls,
            *_args,
            estimatedOutputAmount=estimatedOutputAmount,
            totalEstimatedTime=totalEstimatedTime,
            configId=configId,
            totalEstimatedFee=totalEstimatedFee,
            inputAmount=inputAmount,
            conversionRate=conversionRate,
            flowId=flowId,
            steps=steps,
            _configuration=_configuration,
            **kwargs,
        )

from fireblocks_client.model.xb_settlement_asset import XBSettlementAsset
from fireblocks_client.model.xb_settlement_flow_steps_record import XBSettlementFlowStepsRecord