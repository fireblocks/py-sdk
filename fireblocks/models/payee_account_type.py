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


class PayeeAccountType(str, Enum):
    """
    - VAULT_ACCOUNT   a native Fireblocks vault account - EXCHANGE_ACCOUNT  a third-party exchange account - INTERNAL_WALLET  a whitelisted address marked as internal to the workspace/organization - EXTERNAL_WALLET a whitelisted address marked as external - NETWORK_CONNECTION a member of the Fireblocks network - FIAT_ACCOUNT a third-party account of a fiat bank (Signature, BCB, etc) 
    """

    """
    allowed enum values
    """
    VAULT_ACCOUNT = 'VAULT_ACCOUNT'
    EXCHANGE_ACCOUNT = 'EXCHANGE_ACCOUNT'
    INTERNAL_WALLET = 'INTERNAL_WALLET'
    EXTERNAL_WALLET = 'EXTERNAL_WALLET'
    NETWORK_CONNECTION = 'NETWORK_CONNECTION'
    FIAT_ACCOUNT = 'FIAT_ACCOUNT'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PayeeAccountType from a JSON string"""
        return cls(json.loads(json_str))

