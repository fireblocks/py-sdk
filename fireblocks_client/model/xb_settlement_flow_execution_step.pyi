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


class XBSettlementFlowExecutionStep(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "accountId",
            "inputAmount",
            "id",
            "isSignRequired",
            "status",
        }
        
        class properties:
            id = schemas.StrSchema
            accountId = schemas.StrSchema
        
            @staticmethod
            def status() -> typing.Type['XBSettlementFlowExecutionStepStatus']:
                return XBSettlementFlowExecutionStepStatus
        
            @staticmethod
            def inputAmount() -> typing.Type['XBSettlementAsset']:
                return XBSettlementAsset
            isSignRequired = schemas.BoolSchema
        
            @staticmethod
            def outputAmount() -> typing.Type['XBSettlementAsset']:
                return XBSettlementAsset
        
            @staticmethod
            def fee() -> typing.Type['XBSettlementAsset']:
                return XBSettlementAsset
            startedAt = schemas.NumberSchema
            completedAt = schemas.NumberSchema
            __annotations__ = {
                "id": id,
                "accountId": accountId,
                "status": status,
                "inputAmount": inputAmount,
                "isSignRequired": isSignRequired,
                "outputAmount": outputAmount,
                "fee": fee,
                "startedAt": startedAt,
                "completedAt": completedAt,
            }
    
    accountId: MetaOapg.properties.accountId
    inputAmount: 'XBSettlementAsset'
    id: MetaOapg.properties.id
    isSignRequired: MetaOapg.properties.isSignRequired
    status: 'XBSettlementFlowExecutionStepStatus'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountId"]) -> MetaOapg.properties.accountId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'XBSettlementFlowExecutionStepStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inputAmount"]) -> 'XBSettlementAsset': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isSignRequired"]) -> MetaOapg.properties.isSignRequired: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["outputAmount"]) -> 'XBSettlementAsset': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fee"]) -> 'XBSettlementAsset': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startedAt"]) -> MetaOapg.properties.startedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["completedAt"]) -> MetaOapg.properties.completedAt: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "accountId", "status", "inputAmount", "isSignRequired", "outputAmount", "fee", "startedAt", "completedAt", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountId"]) -> MetaOapg.properties.accountId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> 'XBSettlementFlowExecutionStepStatus': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inputAmount"]) -> 'XBSettlementAsset': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isSignRequired"]) -> MetaOapg.properties.isSignRequired: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["outputAmount"]) -> typing.Union['XBSettlementAsset', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fee"]) -> typing.Union['XBSettlementAsset', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startedAt"]) -> typing.Union[MetaOapg.properties.startedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["completedAt"]) -> typing.Union[MetaOapg.properties.completedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "accountId", "status", "inputAmount", "isSignRequired", "outputAmount", "fee", "startedAt", "completedAt", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        accountId: typing.Union[MetaOapg.properties.accountId, str, ],
        inputAmount: 'XBSettlementAsset',
        id: typing.Union[MetaOapg.properties.id, str, ],
        isSignRequired: typing.Union[MetaOapg.properties.isSignRequired, bool, ],
        status: 'XBSettlementFlowExecutionStepStatus',
        outputAmount: typing.Union['XBSettlementAsset', schemas.Unset] = schemas.unset,
        fee: typing.Union['XBSettlementAsset', schemas.Unset] = schemas.unset,
        startedAt: typing.Union[MetaOapg.properties.startedAt, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        completedAt: typing.Union[MetaOapg.properties.completedAt, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XBSettlementFlowExecutionStep':
        return super().__new__(
            cls,
            *_args,
            accountId=accountId,
            inputAmount=inputAmount,
            id=id,
            isSignRequired=isSignRequired,
            status=status,
            outputAmount=outputAmount,
            fee=fee,
            startedAt=startedAt,
            completedAt=completedAt,
            _configuration=_configuration,
            **kwargs,
        )

from fireblocks_client.model.xb_settlement_asset import XBSettlementAsset
from fireblocks_client.model.xb_settlement_flow_execution_step_status import XBSettlementFlowExecutionStepStatus
