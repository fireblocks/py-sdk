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


class TravelRuleOwnershipProof(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "country",
            "name",
            "id",
            "issueDate",
            "type",
            "issuer",
        }
        
        class properties:
            type = schemas.StrSchema
            id = schemas.StrSchema
            name = schemas.StrSchema
            country = schemas.StrSchema
            issueDate = schemas.StrSchema
            issuer = schemas.StrSchema
            __annotations__ = {
                "type": type,
                "id": id,
                "name": name,
                "country": country,
                "issueDate": issueDate,
                "issuer": issuer,
            }
    
    country: MetaOapg.properties.country
    name: MetaOapg.properties.name
    id: MetaOapg.properties.id
    issueDate: MetaOapg.properties.issueDate
    type: MetaOapg.properties.type
    issuer: MetaOapg.properties.issuer
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["issueDate"]) -> MetaOapg.properties.issueDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["issuer"]) -> MetaOapg.properties.issuer: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "id", "name", "country", "issueDate", "issuer", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["issueDate"]) -> MetaOapg.properties.issueDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["issuer"]) -> MetaOapg.properties.issuer: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "id", "name", "country", "issueDate", "issuer", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        country: typing.Union[MetaOapg.properties.country, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        issueDate: typing.Union[MetaOapg.properties.issueDate, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        issuer: typing.Union[MetaOapg.properties.issuer, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TravelRuleOwnershipProof':
        return super().__new__(
            cls,
            *_args,
            country=country,
            name=name,
            id=id,
            issueDate=issueDate,
            type=type,
            issuer=issuer,
            _configuration=_configuration,
            **kwargs,
        )