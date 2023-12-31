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


class Term(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            networkConnectionId = schemas.StrSchema
            outgoing = schemas.BoolSchema
            asset = schemas.StrSchema
            amount = schemas.StrSchema
            note = schemas.StrSchema
            operation = schemas.StrSchema
            __annotations__ = {
                "networkConnectionId": networkConnectionId,
                "outgoing": outgoing,
                "asset": asset,
                "amount": amount,
                "note": note,
                "operation": operation,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["networkConnectionId"]) -> MetaOapg.properties.networkConnectionId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["outgoing"]) -> MetaOapg.properties.outgoing: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["asset"]) -> MetaOapg.properties.asset: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["note"]) -> MetaOapg.properties.note: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["operation"]) -> MetaOapg.properties.operation: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["networkConnectionId", "outgoing", "asset", "amount", "note", "operation", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["networkConnectionId"]) -> typing.Union[MetaOapg.properties.networkConnectionId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["outgoing"]) -> typing.Union[MetaOapg.properties.outgoing, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["asset"]) -> typing.Union[MetaOapg.properties.asset, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["note"]) -> typing.Union[MetaOapg.properties.note, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["operation"]) -> typing.Union[MetaOapg.properties.operation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["networkConnectionId", "outgoing", "asset", "amount", "note", "operation", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        networkConnectionId: typing.Union[MetaOapg.properties.networkConnectionId, str, schemas.Unset] = schemas.unset,
        outgoing: typing.Union[MetaOapg.properties.outgoing, bool, schemas.Unset] = schemas.unset,
        asset: typing.Union[MetaOapg.properties.asset, str, schemas.Unset] = schemas.unset,
        amount: typing.Union[MetaOapg.properties.amount, str, schemas.Unset] = schemas.unset,
        note: typing.Union[MetaOapg.properties.note, str, schemas.Unset] = schemas.unset,
        operation: typing.Union[MetaOapg.properties.operation, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Term':
        return super().__new__(
            cls,
            *_args,
            networkConnectionId=networkConnectionId,
            outgoing=outgoing,
            asset=asset,
            amount=amount,
            note=note,
            operation=operation,
            _configuration=_configuration,
            **kwargs,
        )
