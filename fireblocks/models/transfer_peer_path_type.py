# coding: utf-8

"""
    Fireblocks API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.6.2
    Contact: support@fireblocks.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class TransferPeerPathType(str, Enum):
    """
    TransferPeerPathType
    """

    """
    allowed enum values
    """
    VAULT_ACCOUNT = 'VAULT_ACCOUNT'
    EXCHANGE_ACCOUNT = 'EXCHANGE_ACCOUNT'
    INTERNAL_WALLET = 'INTERNAL_WALLET'
    EXTERNAL_WALLET = 'EXTERNAL_WALLET'
    CONTRACT = 'CONTRACT'
    NETWORK_CONNECTION = 'NETWORK_CONNECTION'
    FIAT_ACCOUNT = 'FIAT_ACCOUNT'
    COMPOUND = 'COMPOUND'
    GAS_STATION = 'GAS_STATION'
    ONE_TIME_ADDRESS = 'ONE_TIME_ADDRESS'
    UNKNOWN = 'UNKNOWN'
    END_USER_WALLET = 'END_USER_WALLET'
    PROGRAM_CALL = 'PROGRAM_CALL'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TransferPeerPathType from a JSON string"""
        return cls(json.loads(json_str))


