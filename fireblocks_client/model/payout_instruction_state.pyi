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


class PayoutInstructionState(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

        - NOT_STARTED	- waiting to start
- TRANSACTION_SENT - an underlying transaction was sent
- COMPLETED	- completed successfully
- FAILED - failed
- TRANSLATION_ERROR -lookup of the destination failed (due to changes in the underlying whitelisted external wallet or similar)
- SKIPPED- no transaction(s) created for this instruction

    """
        @schemas.classproperty
        def NOT_STARTED(cls):
            return cls("NOT_STARTED")
        @schemas.classproperty
        def TRANSACTION_SENT(cls):
            return cls("TRANSACTION_SENT")
        @schemas.classproperty
        def COMPLETED(cls):
            return cls("COMPLETED")
        @schemas.classproperty
        def FAILED(cls):
            return cls("FAILED")
        @schemas.classproperty
        def TRANSLATION_ERROR(cls):
            return cls("TRANSLATION_ERROR")
        @schemas.classproperty
        def SKIPPED(cls):
            return cls("SKIPPED")
