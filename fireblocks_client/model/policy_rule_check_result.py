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


class PolicyRuleCheckResult(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The rule validation result
    """


    class MetaOapg:
        required = {
            "index",
            "errors",
            "status",
        }
        
        class properties:
            index = schemas.NumberSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "ok": "OK",
                        "failure": "FAILURE",
                    }
                
                @schemas.classproperty
                def OK(cls):
                    return cls("ok")
                
                @schemas.classproperty
                def FAILURE(cls):
                    return cls("failure")
            
            
            class errors(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['PolicyRuleError']:
                        return PolicyRuleError
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['PolicyRuleError'], typing.List['PolicyRuleError']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'errors':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'PolicyRuleError':
                    return super().__getitem__(i)
            __annotations__ = {
                "index": index,
                "status": status,
                "errors": errors,
            }
    
    index: MetaOapg.properties.index
    errors: MetaOapg.properties.errors
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["index"]) -> MetaOapg.properties.index: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errors"]) -> MetaOapg.properties.errors: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["index", "status", "errors", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["index"]) -> MetaOapg.properties.index: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errors"]) -> MetaOapg.properties.errors: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["index", "status", "errors", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        index: typing.Union[MetaOapg.properties.index, decimal.Decimal, int, float, ],
        errors: typing.Union[MetaOapg.properties.errors, list, tuple, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PolicyRuleCheckResult':
        return super().__new__(
            cls,
            *_args,
            index=index,
            errors=errors,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

from fireblocks_client.model.policy_rule_error import PolicyRuleError
