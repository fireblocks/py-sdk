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


class XBSettlementStepType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    - ON_RAMP : A service that allows for the exchange of fiat currencies for cryptocurrencies. An OnRamp input value will always be fiat and output value crypto asset.
- VAULT_ACCOUNT : Fireblocks Vault account
- OFF_RAMP : A service that allows for the exchange of cryptocurrencies for fiat. An OffRamp input value will always be a crypto asset and output value be fiat.
- FIAT_DESTINATION : Fiat account

    """
        @schemas.classproperty
        def ON_RAMP(cls):
            return cls("ON_RAMP")
        @schemas.classproperty
        def VAULT_ACCOUNT(cls):
            return cls("VAULT_ACCOUNT")
        @schemas.classproperty
        def OFF_RAMP(cls):
            return cls("OFF_RAMP")
        @schemas.classproperty
        def FIAT_DESTINATION(cls):
            return cls("FIAT_DESTINATION")