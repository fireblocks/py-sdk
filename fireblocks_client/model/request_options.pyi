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


class RequestOptions(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            idempotencyKey = schemas.StrSchema
        
            @staticmethod
            def ncw() -> typing.Type['Ncw']:
                return Ncw
            __annotations__ = {
                "idempotencyKey": idempotencyKey,
                "ncw": ncw,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["idempotencyKey"]) -> MetaOapg.properties.idempotencyKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ncw"]) -> 'Ncw': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["idempotencyKey", "ncw", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["idempotencyKey"]) -> typing.Union[MetaOapg.properties.idempotencyKey, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ncw"]) -> typing.Union['Ncw', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["idempotencyKey", "ncw", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        idempotencyKey: typing.Union[MetaOapg.properties.idempotencyKey, str, schemas.Unset] = schemas.unset,
        ncw: typing.Union['Ncw', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RequestOptions':
        return super().__new__(
            cls,
            *_args,
            idempotencyKey=idempotencyKey,
            ncw=ncw,
            _configuration=_configuration,
            **kwargs,
        )

from fireblocks_client.model.ncw import Ncw
