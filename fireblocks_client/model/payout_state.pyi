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


class PayoutState(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    - CREATED - payout instruction set created with all its details
- FILE_FOUND - new file found in the FTP
- REQUESTED - payout requested with all its details
- TRANSLATED - payout instruction account IDs identified and translated
- PROCESSING - payout instruction set executed and is processing
- SUBMITTED - transactions submitted for payout instructions
- FINALIZED - payout finished processing, all transactions processed successfully
- INSUFFICIENT_BALANCE - insufficient balance in the payment account (can be a temporary state)
- FAILED - one or more of the payout instructions failed

    """
    
    @schemas.classproperty
    def CREATED(cls):
        return cls("CREATED")
    
    @schemas.classproperty
    def FILE_FOUND(cls):
        return cls("FILE_FOUND")
    
    @schemas.classproperty
    def REQUESTED(cls):
        return cls("REQUESTED")
    
    @schemas.classproperty
    def TRANSLATED(cls):
        return cls("TRANSLATED")
    
    @schemas.classproperty
    def PROCESSING(cls):
        return cls("PROCESSING")
    
    @schemas.classproperty
    def SUBMITTED(cls):
        return cls("SUBMITTED")
    
    @schemas.classproperty
    def FINALIZED(cls):
        return cls("FINALIZED")
    
    @schemas.classproperty
    def INSUFFICIENT_BALANCE(cls):
        return cls("INSUFFICIENT_BALANCE")
    
    @schemas.classproperty
    def FAILED(cls):
        return cls("FAILED")
