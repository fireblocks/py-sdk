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


class CreateAddressResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            address = schemas.StrSchema
            legacyAddress = schemas.StrSchema
            enterpriseAddress = schemas.StrSchema
            tag = schemas.StrSchema
            bip44AddressIndex = schemas.IntSchema
            __annotations__ = {
                "address": address,
                "legacyAddress": legacyAddress,
                "enterpriseAddress": enterpriseAddress,
                "tag": tag,
                "bip44AddressIndex": bip44AddressIndex,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["legacyAddress"]) -> MetaOapg.properties.legacyAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enterpriseAddress"]) -> MetaOapg.properties.enterpriseAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tag"]) -> MetaOapg.properties.tag: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bip44AddressIndex"]) -> MetaOapg.properties.bip44AddressIndex: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["address", "legacyAddress", "enterpriseAddress", "tag", "bip44AddressIndex", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> typing.Union[MetaOapg.properties.address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legacyAddress"]) -> typing.Union[MetaOapg.properties.legacyAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enterpriseAddress"]) -> typing.Union[MetaOapg.properties.enterpriseAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tag"]) -> typing.Union[MetaOapg.properties.tag, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bip44AddressIndex"]) -> typing.Union[MetaOapg.properties.bip44AddressIndex, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["address", "legacyAddress", "enterpriseAddress", "tag", "bip44AddressIndex", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        address: typing.Union[MetaOapg.properties.address, str, schemas.Unset] = schemas.unset,
        legacyAddress: typing.Union[MetaOapg.properties.legacyAddress, str, schemas.Unset] = schemas.unset,
        enterpriseAddress: typing.Union[MetaOapg.properties.enterpriseAddress, str, schemas.Unset] = schemas.unset,
        tag: typing.Union[MetaOapg.properties.tag, str, schemas.Unset] = schemas.unset,
        bip44AddressIndex: typing.Union[MetaOapg.properties.bip44AddressIndex, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateAddressResponse':
        return super().__new__(
            cls,
            *_args,
            address=address,
            legacyAddress=legacyAddress,
            enterpriseAddress=enterpriseAddress,
            tag=tag,
            bip44AddressIndex=bip44AddressIndex,
            _configuration=_configuration,
            **kwargs,
        )
