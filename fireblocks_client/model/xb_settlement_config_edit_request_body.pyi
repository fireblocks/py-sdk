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


class XBSettlementConfigEditRequestBody(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "name",
            "steps",
        }
        
        class properties:
            name = schemas.StrSchema
        
            @staticmethod
            def steps() -> typing.Type['XBSettlementConfigStepsRecord']:
                return XBSettlementConfigStepsRecord
        
            @staticmethod
            def conversionSlippageBasisPoints() -> typing.Type['XBSettlementConversionSlippageBasisPoints']:
                return XBSettlementConversionSlippageBasisPoints
            __annotations__ = {
                "name": name,
                "steps": steps,
                "conversionSlippageBasisPoints": conversionSlippageBasisPoints,
            }
    
    name: MetaOapg.properties.name
    steps: 'XBSettlementConfigStepsRecord'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["steps"]) -> 'XBSettlementConfigStepsRecord': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conversionSlippageBasisPoints"]) -> 'XBSettlementConversionSlippageBasisPoints': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "steps", "conversionSlippageBasisPoints", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["steps"]) -> 'XBSettlementConfigStepsRecord': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conversionSlippageBasisPoints"]) -> typing.Union['XBSettlementConversionSlippageBasisPoints', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "steps", "conversionSlippageBasisPoints", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        steps: 'XBSettlementConfigStepsRecord',
        conversionSlippageBasisPoints: typing.Union['XBSettlementConversionSlippageBasisPoints', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XBSettlementConfigEditRequestBody':
        return super().__new__(
            cls,
            *_args,
            name=name,
            steps=steps,
            conversionSlippageBasisPoints=conversionSlippageBasisPoints,
            _configuration=_configuration,
            **kwargs,
        )

from fireblocks_client.model.xb_settlement_config_steps_record import XBSettlementConfigStepsRecord
from fireblocks_client.model.xb_settlement_conversion_slippage_basis_points import XBSettlementConversionSlippageBasisPoints