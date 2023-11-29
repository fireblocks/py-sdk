# coding: utf-8
from dataclasses import dataclass
import typing_extensions
from fireblocks_client.model.request_options import RequestOptions
import urllib3
from urllib3._collections import HTTPHeaderDict

from fireblocks_client import api_client, exceptions
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

from fireblocks_client.model.external_wallet_asset import ExternalWalletAsset
from fireblocks_client.model.error import Error

# Path params
WalletIdSchema = schemas.StrSchema
AssetIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'walletId': typing.Union[WalletIdSchema, str, ],
        'assetId': typing.Union[AssetIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_wallet_id = api_client.PathParameter(
    name="walletId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=WalletIdSchema,
    required=True,
)
request_path_asset_id = api_client.PathParameter(
    name="assetId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AssetIdSchema,
    required=True,
)
# body param


class SchemaForRequestBodyApplicationJson(
    schemas.ComposedSchema,
):


    class MetaOapg:
        
        
        class one_of_0(
            schemas.AnyTypeSchema,
        ):
        
        
            class MetaOapg:
                required = {
                    "address",
                }
                
                class properties:
                    address = schemas.StrSchema
                    tag = schemas.StrSchema
                    __annotations__ = {
                        "address": address,
                        "tag": tag,
                    }
        
            
            address: MetaOapg.properties.address
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["tag"]) -> MetaOapg.properties.tag: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["address", "tag", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["tag"]) -> typing.Union[MetaOapg.properties.tag, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["address", "tag", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                address: typing.Union[MetaOapg.properties.address, str, ],
                tag: typing.Union[MetaOapg.properties.tag, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'one_of_0':
                return super().__new__(
                    cls,
                    *_args,
                    address=address,
                    tag=tag,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class one_of_1(
            schemas.AnyTypeSchema,
        ):
        
        
            class MetaOapg:
                required = {
                    "additionalInfo",
                }
                
                class properties:
                    
                    
                    class additionalInfo(
                        schemas.ComposedBase,
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            
                            class one_of_0(
                                schemas.AnyTypeSchema,
                            ):
                            
                            
                                class MetaOapg:
                                    required = {
                                        "accountHolderCity",
                                        "ibanCity",
                                        "accountHolderPostalCode",
                                        "accountHolderCountry",
                                        "iban",
                                        "accountHolderGivenName",
                                        "ibanCountry",
                                        "accountHolderAddress1",
                                    }
                                    
                                    class properties:
                                        accountHolderGivenName = schemas.StrSchema
                                        accountHolderSurname = schemas.StrSchema
                                        accountHolderCity = schemas.StrSchema
                                        accountHolderCountry = schemas.StrSchema
                                        accountHolderAddress1 = schemas.StrSchema
                                        accountHolderAddress2 = schemas.StrSchema
                                        accountHolderDistrict = schemas.StrSchema
                                        accountHolderPostalCode = schemas.StrSchema
                                        iban = schemas.StrSchema
                                        ibanCity = schemas.StrSchema
                                        ibanCountry = schemas.StrSchema
                                        __annotations__ = {
                                            "accountHolderGivenName": accountHolderGivenName,
                                            "accountHolderSurname": accountHolderSurname,
                                            "accountHolderCity": accountHolderCity,
                                            "accountHolderCountry": accountHolderCountry,
                                            "accountHolderAddress1": accountHolderAddress1,
                                            "accountHolderAddress2": accountHolderAddress2,
                                            "accountHolderDistrict": accountHolderDistrict,
                                            "accountHolderPostalCode": accountHolderPostalCode,
                                            "iban": iban,
                                            "ibanCity": ibanCity,
                                            "ibanCountry": ibanCountry,
                                        }
                            
                                
                                accountHolderCity: MetaOapg.properties.accountHolderCity
                                ibanCity: MetaOapg.properties.ibanCity
                                accountHolderPostalCode: MetaOapg.properties.accountHolderPostalCode
                                accountHolderCountry: MetaOapg.properties.accountHolderCountry
                                iban: MetaOapg.properties.iban
                                accountHolderGivenName: MetaOapg.properties.accountHolderGivenName
                                ibanCountry: MetaOapg.properties.ibanCountry
                                accountHolderAddress1: MetaOapg.properties.accountHolderAddress1
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["accountHolderGivenName"]) -> MetaOapg.properties.accountHolderGivenName: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["accountHolderSurname"]) -> MetaOapg.properties.accountHolderSurname: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["accountHolderCity"]) -> MetaOapg.properties.accountHolderCity: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["accountHolderCountry"]) -> MetaOapg.properties.accountHolderCountry: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["accountHolderAddress1"]) -> MetaOapg.properties.accountHolderAddress1: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["accountHolderAddress2"]) -> MetaOapg.properties.accountHolderAddress2: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["accountHolderDistrict"]) -> MetaOapg.properties.accountHolderDistrict: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["accountHolderPostalCode"]) -> MetaOapg.properties.accountHolderPostalCode: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["iban"]) -> MetaOapg.properties.iban: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["ibanCity"]) -> MetaOapg.properties.ibanCity: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["ibanCountry"]) -> MetaOapg.properties.ibanCountry: ...
                                
                                @typing.overload
                                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                
                                def __getitem__(self, name: typing.Union[typing_extensions.Literal["accountHolderGivenName", "accountHolderSurname", "accountHolderCity", "accountHolderCountry", "accountHolderAddress1", "accountHolderAddress2", "accountHolderDistrict", "accountHolderPostalCode", "iban", "ibanCity", "ibanCountry", ], str]):
                                    # dict_instance[name] accessor
                                    return super().__getitem__(name)
                                
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["accountHolderGivenName"]) -> MetaOapg.properties.accountHolderGivenName: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["accountHolderSurname"]) -> typing.Union[MetaOapg.properties.accountHolderSurname, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["accountHolderCity"]) -> MetaOapg.properties.accountHolderCity: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["accountHolderCountry"]) -> MetaOapg.properties.accountHolderCountry: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["accountHolderAddress1"]) -> MetaOapg.properties.accountHolderAddress1: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["accountHolderAddress2"]) -> typing.Union[MetaOapg.properties.accountHolderAddress2, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["accountHolderDistrict"]) -> typing.Union[MetaOapg.properties.accountHolderDistrict, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["accountHolderPostalCode"]) -> MetaOapg.properties.accountHolderPostalCode: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["iban"]) -> MetaOapg.properties.iban: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["ibanCity"]) -> MetaOapg.properties.ibanCity: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["ibanCountry"]) -> MetaOapg.properties.ibanCountry: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                
                                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["accountHolderGivenName", "accountHolderSurname", "accountHolderCity", "accountHolderCountry", "accountHolderAddress1", "accountHolderAddress2", "accountHolderDistrict", "accountHolderPostalCode", "iban", "ibanCity", "ibanCountry", ], str]):
                                    return super().get_item_oapg(name)
                                
                            
                                def __new__(
                                    cls,
                                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                                    accountHolderCity: typing.Union[MetaOapg.properties.accountHolderCity, str, ],
                                    ibanCity: typing.Union[MetaOapg.properties.ibanCity, str, ],
                                    accountHolderPostalCode: typing.Union[MetaOapg.properties.accountHolderPostalCode, str, ],
                                    accountHolderCountry: typing.Union[MetaOapg.properties.accountHolderCountry, str, ],
                                    iban: typing.Union[MetaOapg.properties.iban, str, ],
                                    accountHolderGivenName: typing.Union[MetaOapg.properties.accountHolderGivenName, str, ],
                                    ibanCountry: typing.Union[MetaOapg.properties.ibanCountry, str, ],
                                    accountHolderAddress1: typing.Union[MetaOapg.properties.accountHolderAddress1, str, ],
                                    accountHolderSurname: typing.Union[MetaOapg.properties.accountHolderSurname, str, schemas.Unset] = schemas.unset,
                                    accountHolderAddress2: typing.Union[MetaOapg.properties.accountHolderAddress2, str, schemas.Unset] = schemas.unset,
                                    accountHolderDistrict: typing.Union[MetaOapg.properties.accountHolderDistrict, str, schemas.Unset] = schemas.unset,
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                ) -> 'one_of_0':
                                    return super().__new__(
                                        cls,
                                        *_args,
                                        accountHolderCity=accountHolderCity,
                                        ibanCity=ibanCity,
                                        accountHolderPostalCode=accountHolderPostalCode,
                                        accountHolderCountry=accountHolderCountry,
                                        iban=iban,
                                        accountHolderGivenName=accountHolderGivenName,
                                        ibanCountry=ibanCountry,
                                        accountHolderAddress1=accountHolderAddress1,
                                        accountHolderSurname=accountHolderSurname,
                                        accountHolderAddress2=accountHolderAddress2,
                                        accountHolderDistrict=accountHolderDistrict,
                                        _configuration=_configuration,
                                        **kwargs,
                                    )
                            
                            
                            class one_of_1(
                                schemas.AnyTypeSchema,
                            ):
                            
                            
                                class MetaOapg:
                                    required = {
                                        "abaAccountNumber",
                                        "accountHolderCity",
                                        "abaRoutingNumber",
                                        "accountHolderPostalCode",
                                        "accountHolderCountry",
                                        "accountHolderGivenName",
                                        "accountHolderAddress1",
                                        "abaCountry",
                                    }
                                    
                                    class properties:
                                        accountHolderGivenName = schemas.StrSchema
                                        accountHolderSurname = schemas.StrSchema
                                        accountHolderCity = schemas.StrSchema
                                        accountHolderCountry = schemas.StrSchema
                                        accountHolderAddress1 = schemas.StrSchema
                                        accountHolderAddress2 = schemas.StrSchema
                                        accountHolderDistrict = schemas.StrSchema
                                        accountHolderPostalCode = schemas.StrSchema
                                        abaRoutingNumber = schemas.StrSchema
                                        abaAccountNumber = schemas.StrSchema
                                        abaCountry = schemas.StrSchema
                                        __annotations__ = {
                                            "accountHolderGivenName": accountHolderGivenName,
                                            "accountHolderSurname": accountHolderSurname,
                                            "accountHolderCity": accountHolderCity,
                                            "accountHolderCountry": accountHolderCountry,
                                            "accountHolderAddress1": accountHolderAddress1,
                                            "accountHolderAddress2": accountHolderAddress2,
                                            "accountHolderDistrict": accountHolderDistrict,
                                            "accountHolderPostalCode": accountHolderPostalCode,
                                            "abaRoutingNumber": abaRoutingNumber,
                                            "abaAccountNumber": abaAccountNumber,
                                            "abaCountry": abaCountry,
                                        }
                            
                                
                                abaAccountNumber: MetaOapg.properties.abaAccountNumber
                                accountHolderCity: MetaOapg.properties.accountHolderCity
                                abaRoutingNumber: MetaOapg.properties.abaRoutingNumber
                                accountHolderPostalCode: MetaOapg.properties.accountHolderPostalCode
                                accountHolderCountry: MetaOapg.properties.accountHolderCountry
                                accountHolderGivenName: MetaOapg.properties.accountHolderGivenName
                                accountHolderAddress1: MetaOapg.properties.accountHolderAddress1
                                abaCountry: MetaOapg.properties.abaCountry
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["accountHolderGivenName"]) -> MetaOapg.properties.accountHolderGivenName: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["accountHolderSurname"]) -> MetaOapg.properties.accountHolderSurname: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["accountHolderCity"]) -> MetaOapg.properties.accountHolderCity: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["accountHolderCountry"]) -> MetaOapg.properties.accountHolderCountry: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["accountHolderAddress1"]) -> MetaOapg.properties.accountHolderAddress1: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["accountHolderAddress2"]) -> MetaOapg.properties.accountHolderAddress2: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["accountHolderDistrict"]) -> MetaOapg.properties.accountHolderDistrict: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["accountHolderPostalCode"]) -> MetaOapg.properties.accountHolderPostalCode: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["abaRoutingNumber"]) -> MetaOapg.properties.abaRoutingNumber: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["abaAccountNumber"]) -> MetaOapg.properties.abaAccountNumber: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["abaCountry"]) -> MetaOapg.properties.abaCountry: ...
                                
                                @typing.overload
                                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                
                                def __getitem__(self, name: typing.Union[typing_extensions.Literal["accountHolderGivenName", "accountHolderSurname", "accountHolderCity", "accountHolderCountry", "accountHolderAddress1", "accountHolderAddress2", "accountHolderDistrict", "accountHolderPostalCode", "abaRoutingNumber", "abaAccountNumber", "abaCountry", ], str]):
                                    # dict_instance[name] accessor
                                    return super().__getitem__(name)
                                
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["accountHolderGivenName"]) -> MetaOapg.properties.accountHolderGivenName: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["accountHolderSurname"]) -> typing.Union[MetaOapg.properties.accountHolderSurname, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["accountHolderCity"]) -> MetaOapg.properties.accountHolderCity: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["accountHolderCountry"]) -> MetaOapg.properties.accountHolderCountry: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["accountHolderAddress1"]) -> MetaOapg.properties.accountHolderAddress1: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["accountHolderAddress2"]) -> typing.Union[MetaOapg.properties.accountHolderAddress2, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["accountHolderDistrict"]) -> typing.Union[MetaOapg.properties.accountHolderDistrict, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["accountHolderPostalCode"]) -> MetaOapg.properties.accountHolderPostalCode: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["abaRoutingNumber"]) -> MetaOapg.properties.abaRoutingNumber: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["abaAccountNumber"]) -> MetaOapg.properties.abaAccountNumber: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["abaCountry"]) -> MetaOapg.properties.abaCountry: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                
                                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["accountHolderGivenName", "accountHolderSurname", "accountHolderCity", "accountHolderCountry", "accountHolderAddress1", "accountHolderAddress2", "accountHolderDistrict", "accountHolderPostalCode", "abaRoutingNumber", "abaAccountNumber", "abaCountry", ], str]):
                                    return super().get_item_oapg(name)
                                
                            
                                def __new__(
                                    cls,
                                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                                    abaAccountNumber: typing.Union[MetaOapg.properties.abaAccountNumber, str, ],
                                    accountHolderCity: typing.Union[MetaOapg.properties.accountHolderCity, str, ],
                                    abaRoutingNumber: typing.Union[MetaOapg.properties.abaRoutingNumber, str, ],
                                    accountHolderPostalCode: typing.Union[MetaOapg.properties.accountHolderPostalCode, str, ],
                                    accountHolderCountry: typing.Union[MetaOapg.properties.accountHolderCountry, str, ],
                                    accountHolderGivenName: typing.Union[MetaOapg.properties.accountHolderGivenName, str, ],
                                    accountHolderAddress1: typing.Union[MetaOapg.properties.accountHolderAddress1, str, ],
                                    abaCountry: typing.Union[MetaOapg.properties.abaCountry, str, ],
                                    accountHolderSurname: typing.Union[MetaOapg.properties.accountHolderSurname, str, schemas.Unset] = schemas.unset,
                                    accountHolderAddress2: typing.Union[MetaOapg.properties.accountHolderAddress2, str, schemas.Unset] = schemas.unset,
                                    accountHolderDistrict: typing.Union[MetaOapg.properties.accountHolderDistrict, str, schemas.Unset] = schemas.unset,
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                ) -> 'one_of_1':
                                    return super().__new__(
                                        cls,
                                        *_args,
                                        abaAccountNumber=abaAccountNumber,
                                        accountHolderCity=accountHolderCity,
                                        abaRoutingNumber=abaRoutingNumber,
                                        accountHolderPostalCode=accountHolderPostalCode,
                                        accountHolderCountry=accountHolderCountry,
                                        accountHolderGivenName=accountHolderGivenName,
                                        accountHolderAddress1=accountHolderAddress1,
                                        abaCountry=abaCountry,
                                        accountHolderSurname=accountHolderSurname,
                                        accountHolderAddress2=accountHolderAddress2,
                                        accountHolderDistrict=accountHolderDistrict,
                                        _configuration=_configuration,
                                        **kwargs,
                                    )
                            
                            
                            class one_of_2(
                                schemas.AnyTypeSchema,
                            ):
                            
                            
                                class MetaOapg:
                                    required = {
                                        "speiClabe",
                                    }
                                    
                                    class properties:
                                        speiClabe = schemas.StrSchema
                                        speiName = schemas.StrSchema
                                        __annotations__ = {
                                            "speiClabe": speiClabe,
                                            "speiName": speiName,
                                        }
                            
                                
                                speiClabe: MetaOapg.properties.speiClabe
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["speiClabe"]) -> MetaOapg.properties.speiClabe: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["speiName"]) -> MetaOapg.properties.speiName: ...
                                
                                @typing.overload
                                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                
                                def __getitem__(self, name: typing.Union[typing_extensions.Literal["speiClabe", "speiName", ], str]):
                                    # dict_instance[name] accessor
                                    return super().__getitem__(name)
                                
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["speiClabe"]) -> MetaOapg.properties.speiClabe: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["speiName"]) -> typing.Union[MetaOapg.properties.speiName, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                
                                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["speiClabe", "speiName", ], str]):
                                    return super().get_item_oapg(name)
                                
                            
                                def __new__(
                                    cls,
                                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                                    speiClabe: typing.Union[MetaOapg.properties.speiClabe, str, ],
                                    speiName: typing.Union[MetaOapg.properties.speiName, str, schemas.Unset] = schemas.unset,
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                ) -> 'one_of_2':
                                    return super().__new__(
                                        cls,
                                        *_args,
                                        speiClabe=speiClabe,
                                        speiName=speiName,
                                        _configuration=_configuration,
                                        **kwargs,
                                    )
                            
                            @classmethod
                            @functools.lru_cache()
                            def one_of(cls):
                                # we need this here to make our import statements work
                                # we must store _composed_schemas in here so the code is only run
                                # when we invoke this method. If we kept this at the class
                                # level we would get an error because the class level
                                # code would be run when this module is imported, and these composed
                                # classes don't exist yet because their module has not finished
                                # loading
                                return [
                                    cls.one_of_0,
                                    cls.one_of_1,
                                    cls.one_of_2,
                                ]
                    
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'additionalInfo':
                            return super().__new__(
                                cls,
                                *_args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    __annotations__ = {
                        "additionalInfo": additionalInfo,
                    }
        
            
            additionalInfo: MetaOapg.properties.additionalInfo
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["additionalInfo"]) -> MetaOapg.properties.additionalInfo: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["additionalInfo", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["additionalInfo"]) -> MetaOapg.properties.additionalInfo: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["additionalInfo", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                additionalInfo: typing.Union[MetaOapg.properties.additionalInfo, dict, frozendict.frozendict, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'one_of_1':
                return super().__new__(
                    cls,
                    *_args,
                    additionalInfo=additionalInfo,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def one_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                cls.one_of_0,
                cls.one_of_1,
            ]


    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaForRequestBodyApplicationJson':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )


request_body_any_type = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
XRequestIDSchema = schemas.StrSchema
SchemaFor200ResponseBody = ExternalWalletAsset
ResponseHeadersFor200 = typing_extensions.TypedDict(
    'ResponseHeadersFor200',
    {
        'X-Request-ID': XRequestIDSchema,
    }
)


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBody,
    ]
    headers: ResponseHeadersFor200


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        '*/*': api_client.MediaType(
            schema=SchemaFor200ResponseBody),
    },
    headers=[
        x_request_id_parameter,
    ]
)
XRequestIDSchema = schemas.StrSchema
SchemaFor0ResponseBodyApplicationJson = Error
ResponseHeadersFor0 = typing_extensions.TypedDict(
    'ResponseHeadersFor0',
    {
        'X-Request-ID': XRequestIDSchema,
    }
)


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor0ResponseBodyApplicationJson,
    ]
    headers: ResponseHeadersFor0


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationJson),
    },
    headers=[
        x_request_id_parameter,
    ]
)
_all_accept_content_types = (
    '*/*',
    'application/json',
)


class BaseApi(api_client.Api):

    def _add_asset_to_external_wallet_oapg(self, params: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, RequestPathParams] = None, request_options: RequestOptions = None):
        """
        Add an asset to an external wallet.
        """
        path_params = {}
        for parameter in (
            request_path_wallet_id,
            request_path_asset_id,
        ):
            path_params[parameter.name] = params.get(parameter.name)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value

        _path_params = {}
        for parameter in (
            request_path_wallet_id,
            request_path_asset_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)

        _headers = HTTPHeaderDict()

        _fields = None
        _body = None
        serialized_data = request_body_any_type.serialize(params, "application/json")
        _headers.add('Content-Type', "application/json")
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
        idempotency_key = request_options.get("idempotency_key")
        if idempotency_key:
            _headers.add("Idempotency-Key", idempotency_key)

        response = self.api_client.call_api(
            resource_path=used_path,
            method='post'.upper(),
            headers=_headers,
            fields=_fields,
            body=_body,
            timeout=10000,
        )

        response_for_status = _status_code_to_response.get(str(response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(response, self.api_client.configuration)
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response
            )

        return api_response


class AddAssetToExternalWallet(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def add_asset_to_external_wallet(self , params: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, RequestPathParams] = None, request_options: RequestOptions = None):
        return self._add_asset_to_external_wallet_oapg(params, request_options)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    def post(self , params: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, RequestPathParams] = None, request_options: RequestOptions = None):
        return self._add_asset_to_external_wallet_oapg(params, request_options)


