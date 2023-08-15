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


class ExchangeAccount(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
        
            @staticmethod
            def type() -> typing.Type['ExchangeType']:
                return ExchangeType
            name = schemas.StrSchema
            status = schemas.StrSchema
            
            
            class assets(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ExchangeAsset']:
                        return ExchangeAsset
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ExchangeAsset'], typing.List['ExchangeAsset']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'assets':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ExchangeAsset':
                    return super().__getitem__(i)
            
            
            class tradingAccounts(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ExchangeTradingAccount']:
                        return ExchangeTradingAccount
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ExchangeTradingAccount'], typing.List['ExchangeTradingAccount']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tradingAccounts':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ExchangeTradingAccount':
                    return super().__getitem__(i)
            isSubaccount = schemas.BoolSchema
            mainAccountId = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "type": type,
                "name": name,
                "status": status,
                "assets": assets,
                "tradingAccounts": tradingAccounts,
                "isSubaccount": isSubaccount,
                "mainAccountId": mainAccountId,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'ExchangeType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assets"]) -> MetaOapg.properties.assets: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tradingAccounts"]) -> MetaOapg.properties.tradingAccounts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isSubaccount"]) -> MetaOapg.properties.isSubaccount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mainAccountId"]) -> MetaOapg.properties.mainAccountId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "type", "name", "status", "assets", "tradingAccounts", "isSubaccount", "mainAccountId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union['ExchangeType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assets"]) -> typing.Union[MetaOapg.properties.assets, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tradingAccounts"]) -> typing.Union[MetaOapg.properties.tradingAccounts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isSubaccount"]) -> typing.Union[MetaOapg.properties.isSubaccount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mainAccountId"]) -> typing.Union[MetaOapg.properties.mainAccountId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "type", "name", "status", "assets", "tradingAccounts", "isSubaccount", "mainAccountId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        type: typing.Union['ExchangeType', schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        assets: typing.Union[MetaOapg.properties.assets, list, tuple, schemas.Unset] = schemas.unset,
        tradingAccounts: typing.Union[MetaOapg.properties.tradingAccounts, list, tuple, schemas.Unset] = schemas.unset,
        isSubaccount: typing.Union[MetaOapg.properties.isSubaccount, bool, schemas.Unset] = schemas.unset,
        mainAccountId: typing.Union[MetaOapg.properties.mainAccountId, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ExchangeAccount':
        return super().__new__(
            cls,
            *_args,
            id=id,
            type=type,
            name=name,
            status=status,
            assets=assets,
            tradingAccounts=tradingAccounts,
            isSubaccount=isSubaccount,
            mainAccountId=mainAccountId,
            _configuration=_configuration,
            **kwargs,
        )

from fireblocks_client.model.exchange_asset import ExchangeAsset
from fireblocks_client.model.exchange_trading_account import ExchangeTradingAccount
from fireblocks_client.model.exchange_type import ExchangeType