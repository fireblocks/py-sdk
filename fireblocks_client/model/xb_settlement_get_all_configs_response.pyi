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


class XBSettlementGetAllConfigsResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "configurations",
        }
        
        class properties:
            
            
            class configurations(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XBSettlementConfigModel']:
                        return XBSettlementConfigModel
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XBSettlementConfigModel'], typing.List['XBSettlementConfigModel']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'configurations':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XBSettlementConfigModel':
                    return super().__getitem__(i)
            __annotations__ = {
                "configurations": configurations,
            }
    
    configurations: MetaOapg.properties.configurations
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["configurations"]) -> MetaOapg.properties.configurations: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["configurations", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["configurations"]) -> MetaOapg.properties.configurations: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["configurations", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        configurations: typing.Union[MetaOapg.properties.configurations, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XBSettlementGetAllConfigsResponse':
        return super().__new__(
            cls,
            *_args,
            configurations=configurations,
            _configuration=_configuration,
            **kwargs,
        )

from fireblocks_client.model.xb_settlement_config_model import XBSettlementConfigModel