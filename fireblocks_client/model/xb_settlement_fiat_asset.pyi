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


class XBSettlementFiatAsset(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
        @schemas.classproperty
        def USD(cls):
            return cls("USD")
        @schemas.classproperty
        def MXN(cls):
            return cls("MXN")
        @schemas.classproperty
        def COP(cls):
            return cls("COP")
        @schemas.classproperty
        def EUR(cls):
            return cls("EUR")
        @schemas.classproperty
        def GBP(cls):
            return cls("GBP")
