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


class EstimatedTransactionFeeResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "high",
            "low",
            "medium",
        }
        
        class properties:
        
            @staticmethod
            def low() -> typing.Type['TransactionFee']:
                return TransactionFee
        
            @staticmethod
            def medium() -> typing.Type['TransactionFee']:
                return TransactionFee
        
            @staticmethod
            def high() -> typing.Type['TransactionFee']:
                return TransactionFee
            __annotations__ = {
                "low": low,
                "medium": medium,
                "high": high,
            }
    
    high: 'TransactionFee'
    low: 'TransactionFee'
    medium: 'TransactionFee'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["low"]) -> 'TransactionFee': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["medium"]) -> 'TransactionFee': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["high"]) -> 'TransactionFee': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["low", "medium", "high", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["low"]) -> 'TransactionFee': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["medium"]) -> 'TransactionFee': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["high"]) -> 'TransactionFee': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["low", "medium", "high", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        high: 'TransactionFee',
        low: 'TransactionFee',
        medium: 'TransactionFee',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EstimatedTransactionFeeResponse':
        return super().__new__(
            cls,
            *_args,
            high=high,
            low=low,
            medium=medium,
            _configuration=_configuration,
            **kwargs,
        )

from fireblocks_client.model.transaction_fee import TransactionFee
