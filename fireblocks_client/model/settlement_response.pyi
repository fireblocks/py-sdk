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


class SettlementResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
            initiator = schemas.StrSchema
            exchangeReply = schemas.StrSchema
            fireblocksInitiatedTransactions = schemas.DictSchema
        
            @staticmethod
            def exchangeRequestedTransactions() -> typing.Type['SettlementResponse']:
                return SettlementResponse
            __annotations__ = {
                "id": id,
                "initiator": initiator,
                "exchangeReply": exchangeReply,
                "fireblocksInitiatedTransactions": fireblocksInitiatedTransactions,
                "exchangeRequestedTransactions": exchangeRequestedTransactions,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["initiator"]) -> MetaOapg.properties.initiator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exchangeReply"]) -> MetaOapg.properties.exchangeReply: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fireblocksInitiatedTransactions"]) -> MetaOapg.properties.fireblocksInitiatedTransactions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exchangeRequestedTransactions"]) -> 'SettlementResponse': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "initiator", "exchangeReply", "fireblocksInitiatedTransactions", "exchangeRequestedTransactions", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["initiator"]) -> typing.Union[MetaOapg.properties.initiator, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exchangeReply"]) -> typing.Union[MetaOapg.properties.exchangeReply, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fireblocksInitiatedTransactions"]) -> typing.Union[MetaOapg.properties.fireblocksInitiatedTransactions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exchangeRequestedTransactions"]) -> typing.Union['SettlementResponse', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "initiator", "exchangeReply", "fireblocksInitiatedTransactions", "exchangeRequestedTransactions", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        initiator: typing.Union[MetaOapg.properties.initiator, str, schemas.Unset] = schemas.unset,
        exchangeReply: typing.Union[MetaOapg.properties.exchangeReply, str, schemas.Unset] = schemas.unset,
        fireblocksInitiatedTransactions: typing.Union[MetaOapg.properties.fireblocksInitiatedTransactions, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        exchangeRequestedTransactions: typing.Union['SettlementResponse', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SettlementResponse':
        return super().__new__(
            cls,
            *_args,
            id=id,
            initiator=initiator,
            exchangeReply=exchangeReply,
            fireblocksInitiatedTransactions=fireblocksInitiatedTransactions,
            exchangeRequestedTransactions=exchangeRequestedTransactions,
            _configuration=_configuration,
            **kwargs,
        )
