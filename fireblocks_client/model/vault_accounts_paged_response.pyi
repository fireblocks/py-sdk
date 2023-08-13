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


class VaultAccountsPagedResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class accounts(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['VaultAccount']:
                        return VaultAccount
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['VaultAccount'], typing.List['VaultAccount']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'accounts':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'VaultAccount':
                    return super().__getitem__(i)
            
            
            class paging(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        before = schemas.StrSchema
                        after = schemas.StrSchema
                        __annotations__ = {
                            "before": before,
                            "after": after,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["before"]) -> MetaOapg.properties.before: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["after"]) -> MetaOapg.properties.after: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["before", "after", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["before"]) -> typing.Union[MetaOapg.properties.before, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["after"]) -> typing.Union[MetaOapg.properties.after, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["before", "after", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    before: typing.Union[MetaOapg.properties.before, str, schemas.Unset] = schemas.unset,
                    after: typing.Union[MetaOapg.properties.after, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'paging':
                    return super().__new__(
                        cls,
                        *_args,
                        before=before,
                        after=after,
                        _configuration=_configuration,
                        **kwargs,
                    )
            previousUrl = schemas.StrSchema
            nextUrl = schemas.StrSchema
            __annotations__ = {
                "accounts": accounts,
                "paging": paging,
                "previousUrl": previousUrl,
                "nextUrl": nextUrl,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accounts"]) -> MetaOapg.properties.accounts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paging"]) -> MetaOapg.properties.paging: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["previousUrl"]) -> MetaOapg.properties.previousUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nextUrl"]) -> MetaOapg.properties.nextUrl: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["accounts", "paging", "previousUrl", "nextUrl", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accounts"]) -> typing.Union[MetaOapg.properties.accounts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paging"]) -> typing.Union[MetaOapg.properties.paging, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["previousUrl"]) -> typing.Union[MetaOapg.properties.previousUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nextUrl"]) -> typing.Union[MetaOapg.properties.nextUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["accounts", "paging", "previousUrl", "nextUrl", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        accounts: typing.Union[MetaOapg.properties.accounts, list, tuple, schemas.Unset] = schemas.unset,
        paging: typing.Union[MetaOapg.properties.paging, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        previousUrl: typing.Union[MetaOapg.properties.previousUrl, str, schemas.Unset] = schemas.unset,
        nextUrl: typing.Union[MetaOapg.properties.nextUrl, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'VaultAccountsPagedResponse':
        return super().__new__(
            cls,
            *_args,
            accounts=accounts,
            paging=paging,
            previousUrl=previousUrl,
            nextUrl=nextUrl,
            _configuration=_configuration,
            **kwargs,
        )

from fireblocks_client.model.vault_account import VaultAccount
