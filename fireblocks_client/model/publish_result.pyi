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


class PublishResult(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Response object of the publish policy operation
    """


    class MetaOapg:
        required = {
            "metadata",
            "rules",
            "checkResult",
            "status",
        }
        
        class properties:
        
            @staticmethod
            def status() -> typing.Type['PolicyStatus']:
                return PolicyStatus
            
            
            class rules(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['PolicyRule']:
                        return PolicyRule
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['PolicyRule'], typing.List['PolicyRule']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'rules':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'PolicyRule':
                    return super().__getitem__(i)
        
            @staticmethod
            def checkResult() -> typing.Type['PolicyCheckResult']:
                return PolicyCheckResult
        
            @staticmethod
            def metadata() -> typing.Type['PolicyMetadata']:
                return PolicyMetadata
            __annotations__ = {
                "status": status,
                "rules": rules,
                "checkResult": checkResult,
                "metadata": metadata,
            }
    
    metadata: 'PolicyMetadata'
    rules: MetaOapg.properties.rules
    checkResult: 'PolicyCheckResult'
    status: 'PolicyStatus'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'PolicyStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rules"]) -> MetaOapg.properties.rules: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["checkResult"]) -> 'PolicyCheckResult': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'PolicyMetadata': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["status", "rules", "checkResult", "metadata", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> 'PolicyStatus': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rules"]) -> MetaOapg.properties.rules: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["checkResult"]) -> 'PolicyCheckResult': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> 'PolicyMetadata': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["status", "rules", "checkResult", "metadata", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        metadata: 'PolicyMetadata',
        rules: typing.Union[MetaOapg.properties.rules, list, tuple, ],
        checkResult: 'PolicyCheckResult',
        status: 'PolicyStatus',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PublishResult':
        return super().__new__(
            cls,
            *_args,
            metadata=metadata,
            rules=rules,
            checkResult=checkResult,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

from fireblocks_client.model.policy_check_result import PolicyCheckResult
from fireblocks_client.model.policy_metadata import PolicyMetadata
from fireblocks_client.model.policy_rule import PolicyRule
from fireblocks_client.model.policy_status import PolicyStatus
