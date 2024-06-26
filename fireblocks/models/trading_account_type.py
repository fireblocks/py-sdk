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


class TradingAccountType(str, Enum):
    """
    TradingAccountType
    """

    """
    allowed enum values
    """
    COIN_FUTURES = 'COIN_FUTURES'
    COIN_MARGINED_SWAP = 'COIN_MARGINED_SWAP'
    EXCHANGE = 'EXCHANGE'
    FUNDING = 'FUNDING'
    FUNDABLE = 'FUNDABLE'
    FUTURES = 'FUTURES'
    FUTURES_CROSS = 'FUTURES_CROSS'
    MARGIN = 'MARGIN'
    MARGIN_CROSS = 'MARGIN_CROSS'
    OPTIONS = 'OPTIONS'
    SPOT = 'SPOT'
    USDT_MARGINED_SWAP_CROSS = 'USDT_MARGINED_SWAP_CROSS'
    USDT_FUTURES = 'USDT_FUTURES'
    UNIFIED = 'UNIFIED'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TradingAccountType from a JSON string"""
        return cls(json.loads(json_str))


