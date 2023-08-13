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


class ToExchangeTransaction(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            assetId = schemas.StrSchema
            amount = schemas.StrSchema
            dstAddress = schemas.StrSchema
            dstTag = schemas.StrSchema
            __annotations__ = {
                "assetId": assetId,
                "amount": amount,
                "dstAddress": dstAddress,
                "dstTag": dstTag,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assetId"]) -> MetaOapg.properties.assetId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dstAddress"]) -> MetaOapg.properties.dstAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dstTag"]) -> MetaOapg.properties.dstTag: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["assetId", "amount", "dstAddress", "dstTag", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assetId"]) -> typing.Union[MetaOapg.properties.assetId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dstAddress"]) -> typing.Union[MetaOapg.properties.dstAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dstTag"]) -> typing.Union[MetaOapg.properties.dstTag, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["assetId", "amount", "dstAddress", "dstTag", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        assetId: typing.Union[MetaOapg.properties.assetId, str, schemas.Unset] = schemas.unset,
        amount: typing.Union[MetaOapg.properties.amount, str, schemas.Unset] = schemas.unset,
        dstAddress: typing.Union[MetaOapg.properties.dstAddress, str, schemas.Unset] = schemas.unset,
        dstTag: typing.Union[MetaOapg.properties.dstTag, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ToExchangeTransaction':
        return super().__new__(
            cls,
            *_args,
            assetId=assetId,
            amount=amount,
            dstAddress=dstAddress,
            dstTag=dstTag,
            _configuration=_configuration,
            **kwargs,
        )
