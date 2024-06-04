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


class ScreeningOperationType(str, Enum):
    """
    ScreeningOperationType
    """

    """
    allowed enum values
    """
    SCREENING = 'SCREENING'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ScreeningOperationType from a JSON string"""
        return cls(json.loads(json_str))

