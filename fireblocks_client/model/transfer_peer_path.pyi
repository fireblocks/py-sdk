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


class TransferPeerPath(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "type",
        }
        
        class properties:
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def VAULT_ACCOUNT(cls):
                    return cls("VAULT_ACCOUNT")
                
                @schemas.classproperty
                def EXCHANGE_ACCOUNT(cls):
                    return cls("EXCHANGE_ACCOUNT")
                
                @schemas.classproperty
                def INTERNAL_WALLET(cls):
                    return cls("INTERNAL_WALLET")
                
                @schemas.classproperty
                def EXTERNAL_WALLET(cls):
                    return cls("EXTERNAL_WALLET")
                
                @schemas.classproperty
                def NETWORK_CONNECTION(cls):
                    return cls("NETWORK_CONNECTION")
                
                @schemas.classproperty
                def FIAT_ACCOUNT(cls):
                    return cls("FIAT_ACCOUNT")
                
                @schemas.classproperty
                def COMPOUND(cls):
                    return cls("COMPOUND")
                
                @schemas.classproperty
                def GAS_STATION(cls):
                    return cls("GAS_STATION")
                
                @schemas.classproperty
                def ONE_TIME_ADDRESS(cls):
                    return cls("ONE_TIME_ADDRESS")
                
                @schemas.classproperty
                def UNKNOWN(cls):
                    return cls("UNKNOWN")
                
                @schemas.classproperty
                def END_USER_WALLET(cls):
                    return cls("END_USER_WALLET")
            
            
            class subType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def BINANCE(cls):
                    return cls("BINANCE")
                
                @schemas.classproperty
                def BINANCEUS(cls):
                    return cls("BINANCEUS")
                
                @schemas.classproperty
                def BITFINEX(cls):
                    return cls("BITFINEX")
                
                @schemas.classproperty
                def BITHUMB(cls):
                    return cls("BITHUMB")
                
                @schemas.classproperty
                def BITMEX(cls):
                    return cls("BITMEX")
                
                @schemas.classproperty
                def BITSO(cls):
                    return cls("BITSO")
                
                @schemas.classproperty
                def BITSTAMP(cls):
                    return cls("BITSTAMP")
                
                @schemas.classproperty
                def BITTREX(cls):
                    return cls("BITTREX")
                
                @schemas.classproperty
                def BLINC(cls):
                    return cls("BLINC")
                
                @schemas.classproperty
                def BYBIT(cls):
                    return cls("BYBIT")
                
                @schemas.classproperty
                def CIRCLE(cls):
                    return cls("CIRCLE")
                
                @schemas.classproperty
                def COINBASEEXCHANGE(cls):
                    return cls("COINBASEEXCHANGE")
                
                @schemas.classproperty
                def COINBASEPRO(cls):
                    return cls("COINBASEPRO")
                
                @schemas.classproperty
                def COINMETRO(cls):
                    return cls("COINMETRO")
                
                @schemas.classproperty
                def COINSPRO(cls):
                    return cls("COINSPRO")
                
                @schemas.classproperty
                def CRYPTOCOM(cls):
                    return cls("CRYPTOCOM")
                
                @schemas.classproperty
                def DERIBIT(cls):
                    return cls("DERIBIT")
                
                @schemas.classproperty
                def GEMINI(cls):
                    return cls("GEMINI")
                
                @schemas.classproperty
                def HITBTC(cls):
                    return cls("HITBTC")
                
                @schemas.classproperty
                def HUOBI(cls):
                    return cls("HUOBI")
                
                @schemas.classproperty
                def INDEPENDENTRESERVE(cls):
                    return cls("INDEPENDENTRESERVE")
                
                @schemas.classproperty
                def KORBIT(cls):
                    return cls("KORBIT")
                
                @schemas.classproperty
                def KRAKEN(cls):
                    return cls("KRAKEN")
                
                @schemas.classproperty
                def KRAKENINTL(cls):
                    return cls("KRAKENINTL")
                
                @schemas.classproperty
                def KUCOIN(cls):
                    return cls("KUCOIN")
                
                @schemas.classproperty
                def LIQUID(cls):
                    return cls("LIQUID")
                
                @schemas.classproperty
                def OKCOIN(cls):
                    return cls("OKCOIN")
                
                @schemas.classproperty
                def OKEX(cls):
                    return cls("OKEX")
                
                @schemas.classproperty
                def PAXOS(cls):
                    return cls("PAXOS")
                
                @schemas.classproperty
                def POLONIEX(cls):
                    return cls("POLONIEX")
                
                @schemas.classproperty
                def EXTERNAL(cls):
                    return cls("External")
                
                @schemas.classproperty
                def INTERNAL(cls):
                    return cls("Internal")
            id = schemas.StrSchema
            name = schemas.StrSchema
            walletId = schemas.UUIDSchema
            __annotations__ = {
                "type": type,
                "subType": subType,
                "id": id,
                "name": name,
                "walletId": walletId,
            }
    
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subType"]) -> MetaOapg.properties.subType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["walletId"]) -> MetaOapg.properties.walletId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "subType", "id", "name", "walletId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subType"]) -> typing.Union[MetaOapg.properties.subType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["walletId"]) -> typing.Union[MetaOapg.properties.walletId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "subType", "id", "name", "walletId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        subType: typing.Union[MetaOapg.properties.subType, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        walletId: typing.Union[MetaOapg.properties.walletId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TransferPeerPath':
        return super().__new__(
            cls,
            *_args,
            type=type,
            subType=subType,
            id=id,
            name=name,
            walletId=walletId,
            _configuration=_configuration,
            **kwargs,
        )
