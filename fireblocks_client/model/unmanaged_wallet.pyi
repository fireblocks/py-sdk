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


class UnmanagedWallet(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "name",
            "id",
            "status",
        }
        
        class properties:
            id = schemas.StrSchema
            name = schemas.StrSchema
            customerRefId = schemas.StrSchema
            
            
            class assets(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['WalletAsset']:
                        return WalletAsset
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['WalletAsset'], typing.List['WalletAsset']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'assets':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'WalletAsset':
                    return super().__getitem__(i)
            __annotations__ = {
                "id": id,
                "name": name,
                "customerRefId": customerRefId,
                "assets": assets,
            }
    
    name: MetaOapg.properties.name
    id: MetaOapg.properties.id
    status: schemas.AnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customerRefId"]) -> MetaOapg.properties.customerRefId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assets"]) -> MetaOapg.properties.assets: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "customerRefId", "assets", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customerRefId"]) -> typing.Union[MetaOapg.properties.customerRefId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assets"]) -> typing.Union[MetaOapg.properties.assets, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "customerRefId", "assets", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        status: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        customerRefId: typing.Union[MetaOapg.properties.customerRefId, str, schemas.Unset] = schemas.unset,
        assets: typing.Union[MetaOapg.properties.assets, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UnmanagedWallet':
        return super().__new__(
            cls,
            *_args,
            name=name,
            id=id,
            status=status,
            customerRefId=customerRefId,
            assets=assets,
            _configuration=_configuration,
            **kwargs,
        )

from fireblocks_client.model.wallet_asset import WalletAsset