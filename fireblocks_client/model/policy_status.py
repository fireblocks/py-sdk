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


class PolicyStatus(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    * SUCCESS - success
* UNVALIDATED - not validated yet
* INVALID_CONFIGURATION - at least one rule is invalid
* PENDING - pending approval
* PENDING_CONSOLE_APPROVAL - pending approval from the console app
* AWAITING_QUORUM - pending quorum approval
* UNHANDLED_ERROR - unhandled error

    """


    class MetaOapg:
        enum_value_to_name = {
            "SUCCESS": "SUCCESS",
            "UNVALIDATED": "UNVALIDATED",
            "INVALID_CONFIGURATION": "INVALID_CONFIGURATION",
            "PENDING": "PENDING",
            "PENDING_CONSOLE_APPROVAL": "PENDING_CONSOLE_APPROVAL",
            "AWAITING_QUORUM": "AWAITING_QUORUM",
            "UNHANDLED_ERROR": "UNHANDLED_ERROR",
        }
        @schemas.classproperty
        def SUCCESS(cls):
            return cls("SUCCESS")
        @schemas.classproperty
        def UNVALIDATED(cls):
            return cls("UNVALIDATED")
        @schemas.classproperty
        def INVALID_CONFIGURATION(cls):
            return cls("INVALID_CONFIGURATION")
        @schemas.classproperty
        def PENDING(cls):
            return cls("PENDING")
        @schemas.classproperty
        def PENDING_CONSOLE_APPROVAL(cls):
            return cls("PENDING_CONSOLE_APPROVAL")
        @schemas.classproperty
        def AWAITING_QUORUM(cls):
            return cls("AWAITING_QUORUM")
        @schemas.classproperty
        def UNHANDLED_ERROR(cls):
            return cls("UNHANDLED_ERROR")