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


class SessionDTO(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "vaultAccountId",
            "chainIds",
            "sessionMetadata",
            "feeLevel",
            "id",
            "creationDate",
            "connectionType",
            "userId",
            "connectionMethod",
        }
        
        class properties:
            id = schemas.StrSchema
            userId = schemas.StrSchema
            
            
            class sessionMetadata(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    @classmethod
                    @functools.lru_cache()
                    def all_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            SessionMetadata,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'sessionMetadata':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            vaultAccountId = schemas.NumberSchema
            
            
            class feeLevel(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "MEDIUM": "MEDIUM",
                        "HIGH": "HIGH",
                    }
                    @schemas.classproperty
                    def MEDIUM(cls):
                        return cls("MEDIUM")
                    @schemas.classproperty
                    def HIGH(cls):
                        return cls("HIGH")
            
            
            class chainIds(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'chainIds':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class connectionType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "WalletConnect": "WALLET_CONNECT",
                    }
                    @schemas.classproperty
                    def WALLET_CONNECT(cls):
                        return cls("WalletConnect")
            
            
            class connectionMethod(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "DESKTOP": "DESKTOP",
                        "MOBILE": "MOBILE",
                        "API": "API",
                    }
                    @schemas.classproperty
                    def DESKTOP(cls):
                        return cls("DESKTOP")
                    @schemas.classproperty
                    def MOBILE(cls):
                        return cls("MOBILE")
                    @schemas.classproperty
                    def API(cls):
                        return cls("API")
            creationDate = schemas.DateTimeSchema
            __annotations__ = {
                "id": id,
                "userId": userId,
                "sessionMetadata": sessionMetadata,
                "vaultAccountId": vaultAccountId,
                "feeLevel": feeLevel,
                "chainIds": chainIds,
                "connectionType": connectionType,
                "connectionMethod": connectionMethod,
                "creationDate": creationDate,
            }
    
    vaultAccountId: MetaOapg.properties.vaultAccountId
    chainIds: MetaOapg.properties.chainIds
    sessionMetadata: MetaOapg.properties.sessionMetadata
    feeLevel: MetaOapg.properties.feeLevel
    id: MetaOapg.properties.id
    creationDate: MetaOapg.properties.creationDate
    connectionType: MetaOapg.properties.connectionType
    userId: MetaOapg.properties.userId
    connectionMethod: MetaOapg.properties.connectionMethod
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userId"]) -> MetaOapg.properties.userId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sessionMetadata"]) -> MetaOapg.properties.sessionMetadata: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vaultAccountId"]) -> MetaOapg.properties.vaultAccountId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["feeLevel"]) -> MetaOapg.properties.feeLevel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["chainIds"]) -> MetaOapg.properties.chainIds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["connectionType"]) -> MetaOapg.properties.connectionType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["connectionMethod"]) -> MetaOapg.properties.connectionMethod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creationDate"]) -> MetaOapg.properties.creationDate: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "userId", "sessionMetadata", "vaultAccountId", "feeLevel", "chainIds", "connectionType", "connectionMethod", "creationDate", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userId"]) -> MetaOapg.properties.userId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sessionMetadata"]) -> MetaOapg.properties.sessionMetadata: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vaultAccountId"]) -> MetaOapg.properties.vaultAccountId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["feeLevel"]) -> MetaOapg.properties.feeLevel: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["chainIds"]) -> MetaOapg.properties.chainIds: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["connectionType"]) -> MetaOapg.properties.connectionType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["connectionMethod"]) -> MetaOapg.properties.connectionMethod: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creationDate"]) -> MetaOapg.properties.creationDate: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "userId", "sessionMetadata", "vaultAccountId", "feeLevel", "chainIds", "connectionType", "connectionMethod", "creationDate", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        vaultAccountId: typing.Union[MetaOapg.properties.vaultAccountId, decimal.Decimal, int, float, ],
        chainIds: typing.Union[MetaOapg.properties.chainIds, list, tuple, ],
        sessionMetadata: typing.Union[MetaOapg.properties.sessionMetadata, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        feeLevel: typing.Union[MetaOapg.properties.feeLevel, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        creationDate: typing.Union[MetaOapg.properties.creationDate, str, datetime, ],
        connectionType: typing.Union[MetaOapg.properties.connectionType, str, ],
        userId: typing.Union[MetaOapg.properties.userId, str, ],
        connectionMethod: typing.Union[MetaOapg.properties.connectionMethod, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SessionDTO':
        return super().__new__(
            cls,
            *_args,
            vaultAccountId=vaultAccountId,
            chainIds=chainIds,
            sessionMetadata=sessionMetadata,
            feeLevel=feeLevel,
            id=id,
            creationDate=creationDate,
            connectionType=connectionType,
            userId=userId,
            connectionMethod=connectionMethod,
            _configuration=_configuration,
            **kwargs,
        )

from fireblocks_client.model.session_metadata import SessionMetadata