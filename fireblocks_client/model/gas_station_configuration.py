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


class GasStationConfiguration(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            gasThreshold = schemas.StrSchema
            gasCap = schemas.StrSchema
            maxGasPrice = schemas.StrSchema
            __annotations__ = {
                "gasThreshold": gasThreshold,
                "gasCap": gasCap,
                "maxGasPrice": maxGasPrice,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gasThreshold"]) -> MetaOapg.properties.gasThreshold: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gasCap"]) -> MetaOapg.properties.gasCap: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxGasPrice"]) -> MetaOapg.properties.maxGasPrice: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["gasThreshold", "gasCap", "maxGasPrice", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gasThreshold"]) -> typing.Union[MetaOapg.properties.gasThreshold, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gasCap"]) -> typing.Union[MetaOapg.properties.gasCap, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxGasPrice"]) -> typing.Union[MetaOapg.properties.maxGasPrice, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["gasThreshold", "gasCap", "maxGasPrice", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        gasThreshold: typing.Union[MetaOapg.properties.gasThreshold, str, schemas.Unset] = schemas.unset,
        gasCap: typing.Union[MetaOapg.properties.gasCap, str, schemas.Unset] = schemas.unset,
        maxGasPrice: typing.Union[MetaOapg.properties.maxGasPrice, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GasStationConfiguration':
        return super().__new__(
            cls,
            *_args,
            gasThreshold=gasThreshold,
            gasCap=gasCap,
            maxGasPrice=maxGasPrice,
            _configuration=_configuration,
            **kwargs,
        )
