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


class TradingAccountType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        enum_value_to_name = {
            "COIN_FUTURES": "COIN_FUTURES",
            "COIN_MARGINED_SWAP": "COIN_MARGINED_SWAP",
            "EXCHANGE": "EXCHANGE",
            "FUNDING": "FUNDING",
            "FUNDABLE": "FUNDABLE",
            "FUTURES": "FUTURES",
            "FUTURES_CROSS": "FUTURES_CROSS",
            "MARGIN": "MARGIN",
            "MARGIN_CROSS": "MARGIN_CROSS",
            "OPTIONS": "OPTIONS",
            "SPOT": "SPOT",
            "USDT_MARGINED_SWAP_CROSS": "USDT_MARGINED_SWAP_CROSS",
            "USDT_FUTURES": "USDT_FUTURES",
            "UNIFIED": "UNIFIED",
        }
    
    @schemas.classproperty
    def COIN_FUTURES(cls):
        return cls("COIN_FUTURES")
    
    @schemas.classproperty
    def COIN_MARGINED_SWAP(cls):
        return cls("COIN_MARGINED_SWAP")
    
    @schemas.classproperty
    def EXCHANGE(cls):
        return cls("EXCHANGE")
    
    @schemas.classproperty
    def FUNDING(cls):
        return cls("FUNDING")
    
    @schemas.classproperty
    def FUNDABLE(cls):
        return cls("FUNDABLE")
    
    @schemas.classproperty
    def FUTURES(cls):
        return cls("FUTURES")
    
    @schemas.classproperty
    def FUTURES_CROSS(cls):
        return cls("FUTURES_CROSS")
    
    @schemas.classproperty
    def MARGIN(cls):
        return cls("MARGIN")
    
    @schemas.classproperty
    def MARGIN_CROSS(cls):
        return cls("MARGIN_CROSS")
    
    @schemas.classproperty
    def OPTIONS(cls):
        return cls("OPTIONS")
    
    @schemas.classproperty
    def SPOT(cls):
        return cls("SPOT")
    
    @schemas.classproperty
    def USDT_MARGINED_SWAP_CROSS(cls):
        return cls("USDT_MARGINED_SWAP_CROSS")
    
    @schemas.classproperty
    def USDT_FUTURES(cls):
        return cls("USDT_FUTURES")
    
    @schemas.classproperty
    def UNIFIED(cls):
        return cls("UNIFIED")
