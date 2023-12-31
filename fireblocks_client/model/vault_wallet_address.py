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


class VaultWalletAddress(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            assetId = schemas.StrSchema
            address = schemas.StrSchema
            description = schemas.StrSchema
            tag = schemas.StrSchema
            type = schemas.StrSchema
            customerRefId = schemas.StrSchema
            
            
            class addressFormat(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "SEGWIT": "SEGWIT",
                        "LEGACY": "LEGACY",
                    }
                
                @schemas.classproperty
                def SEGWIT(cls):
                    return cls("SEGWIT")
                
                @schemas.classproperty
                def LEGACY(cls):
                    return cls("LEGACY")
            legacyAddress = schemas.StrSchema
            enterpriseAddress = schemas.StrSchema
            bip44AddressIndex = schemas.IntSchema
            userDefined = schemas.BoolSchema
            __annotations__ = {
                "assetId": assetId,
                "address": address,
                "description": description,
                "tag": tag,
                "type": type,
                "customerRefId": customerRefId,
                "addressFormat": addressFormat,
                "legacyAddress": legacyAddress,
                "enterpriseAddress": enterpriseAddress,
                "bip44AddressIndex": bip44AddressIndex,
                "userDefined": userDefined,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assetId"]) -> MetaOapg.properties.assetId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tag"]) -> MetaOapg.properties.tag: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customerRefId"]) -> MetaOapg.properties.customerRefId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addressFormat"]) -> MetaOapg.properties.addressFormat: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["legacyAddress"]) -> MetaOapg.properties.legacyAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enterpriseAddress"]) -> MetaOapg.properties.enterpriseAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bip44AddressIndex"]) -> MetaOapg.properties.bip44AddressIndex: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userDefined"]) -> MetaOapg.properties.userDefined: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["assetId", "address", "description", "tag", "type", "customerRefId", "addressFormat", "legacyAddress", "enterpriseAddress", "bip44AddressIndex", "userDefined", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assetId"]) -> typing.Union[MetaOapg.properties.assetId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> typing.Union[MetaOapg.properties.address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tag"]) -> typing.Union[MetaOapg.properties.tag, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customerRefId"]) -> typing.Union[MetaOapg.properties.customerRefId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addressFormat"]) -> typing.Union[MetaOapg.properties.addressFormat, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legacyAddress"]) -> typing.Union[MetaOapg.properties.legacyAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enterpriseAddress"]) -> typing.Union[MetaOapg.properties.enterpriseAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bip44AddressIndex"]) -> typing.Union[MetaOapg.properties.bip44AddressIndex, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userDefined"]) -> typing.Union[MetaOapg.properties.userDefined, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["assetId", "address", "description", "tag", "type", "customerRefId", "addressFormat", "legacyAddress", "enterpriseAddress", "bip44AddressIndex", "userDefined", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        assetId: typing.Union[MetaOapg.properties.assetId, str, schemas.Unset] = schemas.unset,
        address: typing.Union[MetaOapg.properties.address, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        tag: typing.Union[MetaOapg.properties.tag, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        customerRefId: typing.Union[MetaOapg.properties.customerRefId, str, schemas.Unset] = schemas.unset,
        addressFormat: typing.Union[MetaOapg.properties.addressFormat, str, schemas.Unset] = schemas.unset,
        legacyAddress: typing.Union[MetaOapg.properties.legacyAddress, str, schemas.Unset] = schemas.unset,
        enterpriseAddress: typing.Union[MetaOapg.properties.enterpriseAddress, str, schemas.Unset] = schemas.unset,
        bip44AddressIndex: typing.Union[MetaOapg.properties.bip44AddressIndex, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        userDefined: typing.Union[MetaOapg.properties.userDefined, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'VaultWalletAddress':
        return super().__new__(
            cls,
            *_args,
            assetId=assetId,
            address=address,
            description=description,
            tag=tag,
            type=type,
            customerRefId=customerRefId,
            addressFormat=addressFormat,
            legacyAddress=legacyAddress,
            enterpriseAddress=enterpriseAddress,
            bip44AddressIndex=bip44AddressIndex,
            userDefined=userDefined,
            _configuration=_configuration,
            **kwargs,
        )
