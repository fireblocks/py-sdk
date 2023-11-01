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


class PayeeAccountType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

        - VAULT_ACCOUNT  	a native Fireblocks vault account
- EXCHANGE_ACCOUNT 	a third-party exchange account
- INTERNAL_WALLET 	a whitelisted address marked as internal to the workspace/organization
- EXTERNAL_WALLET	a whitelisted address marked as external
- NETWORK_CONNECTION	a member of the Fireblocks network
- FIAT_ACCOUNT	a third-party account of a fiat bank (Signature, BCB, etc)

    """


    class MetaOapg:
        enum_value_to_name = {
            "VAULT_ACCOUNT": "VAULT_ACCOUNT",
            "EXCHANGE_ACCOUNT": "EXCHANGE_ACCOUNT",
            "INTERNAL_WALLET": "INTERNAL_WALLET",
            "EXTERNAL_WALLET": "EXTERNAL_WALLET",
            "NETWORK_CONNECTION": "NETWORK_CONNECTION",
            "FIAT_ACCOUNT": "FIAT_ACCOUNT",
        }
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
