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


class WalletAssetAdditionalInfo(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
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
            iban = schemas.StrSchema
            ibanCity = schemas.StrSchema
            ibanCountry = schemas.StrSchema
            speiClabe = schemas.StrSchema
            speiName = schemas.StrSchema
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
                "iban": iban,
                "ibanCity": ibanCity,
                "ibanCountry": ibanCountry,
                "speiClabe": speiClabe,
                "speiName": speiName,
            }
    
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
    def __getitem__(self, name: typing_extensions.Literal["iban"]) -> MetaOapg.properties.iban: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ibanCity"]) -> MetaOapg.properties.ibanCity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ibanCountry"]) -> MetaOapg.properties.ibanCountry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["speiClabe"]) -> MetaOapg.properties.speiClabe: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["speiName"]) -> MetaOapg.properties.speiName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["accountHolderGivenName", "accountHolderSurname", "accountHolderCity", "accountHolderCountry", "accountHolderAddress1", "accountHolderAddress2", "accountHolderDistrict", "accountHolderPostalCode", "abaRoutingNumber", "abaAccountNumber", "abaCountry", "iban", "ibanCity", "ibanCountry", "speiClabe", "speiName", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountHolderGivenName"]) -> typing.Union[MetaOapg.properties.accountHolderGivenName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountHolderSurname"]) -> typing.Union[MetaOapg.properties.accountHolderSurname, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountHolderCity"]) -> typing.Union[MetaOapg.properties.accountHolderCity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountHolderCountry"]) -> typing.Union[MetaOapg.properties.accountHolderCountry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountHolderAddress1"]) -> typing.Union[MetaOapg.properties.accountHolderAddress1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountHolderAddress2"]) -> typing.Union[MetaOapg.properties.accountHolderAddress2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountHolderDistrict"]) -> typing.Union[MetaOapg.properties.accountHolderDistrict, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountHolderPostalCode"]) -> typing.Union[MetaOapg.properties.accountHolderPostalCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["abaRoutingNumber"]) -> typing.Union[MetaOapg.properties.abaRoutingNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["abaAccountNumber"]) -> typing.Union[MetaOapg.properties.abaAccountNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["abaCountry"]) -> typing.Union[MetaOapg.properties.abaCountry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iban"]) -> typing.Union[MetaOapg.properties.iban, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ibanCity"]) -> typing.Union[MetaOapg.properties.ibanCity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ibanCountry"]) -> typing.Union[MetaOapg.properties.ibanCountry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["speiClabe"]) -> typing.Union[MetaOapg.properties.speiClabe, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["speiName"]) -> typing.Union[MetaOapg.properties.speiName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["accountHolderGivenName", "accountHolderSurname", "accountHolderCity", "accountHolderCountry", "accountHolderAddress1", "accountHolderAddress2", "accountHolderDistrict", "accountHolderPostalCode", "abaRoutingNumber", "abaAccountNumber", "abaCountry", "iban", "ibanCity", "ibanCountry", "speiClabe", "speiName", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        accountHolderGivenName: typing.Union[MetaOapg.properties.accountHolderGivenName, str, schemas.Unset] = schemas.unset,
        accountHolderSurname: typing.Union[MetaOapg.properties.accountHolderSurname, str, schemas.Unset] = schemas.unset,
        accountHolderCity: typing.Union[MetaOapg.properties.accountHolderCity, str, schemas.Unset] = schemas.unset,
        accountHolderCountry: typing.Union[MetaOapg.properties.accountHolderCountry, str, schemas.Unset] = schemas.unset,
        accountHolderAddress1: typing.Union[MetaOapg.properties.accountHolderAddress1, str, schemas.Unset] = schemas.unset,
        accountHolderAddress2: typing.Union[MetaOapg.properties.accountHolderAddress2, str, schemas.Unset] = schemas.unset,
        accountHolderDistrict: typing.Union[MetaOapg.properties.accountHolderDistrict, str, schemas.Unset] = schemas.unset,
        accountHolderPostalCode: typing.Union[MetaOapg.properties.accountHolderPostalCode, str, schemas.Unset] = schemas.unset,
        abaRoutingNumber: typing.Union[MetaOapg.properties.abaRoutingNumber, str, schemas.Unset] = schemas.unset,
        abaAccountNumber: typing.Union[MetaOapg.properties.abaAccountNumber, str, schemas.Unset] = schemas.unset,
        abaCountry: typing.Union[MetaOapg.properties.abaCountry, str, schemas.Unset] = schemas.unset,
        iban: typing.Union[MetaOapg.properties.iban, str, schemas.Unset] = schemas.unset,
        ibanCity: typing.Union[MetaOapg.properties.ibanCity, str, schemas.Unset] = schemas.unset,
        ibanCountry: typing.Union[MetaOapg.properties.ibanCountry, str, schemas.Unset] = schemas.unset,
        speiClabe: typing.Union[MetaOapg.properties.speiClabe, str, schemas.Unset] = schemas.unset,
        speiName: typing.Union[MetaOapg.properties.speiName, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WalletAssetAdditionalInfo':
        return super().__new__(
            cls,
            *_args,
            accountHolderGivenName=accountHolderGivenName,
            accountHolderSurname=accountHolderSurname,
            accountHolderCity=accountHolderCity,
            accountHolderCountry=accountHolderCountry,
            accountHolderAddress1=accountHolderAddress1,
            accountHolderAddress2=accountHolderAddress2,
            accountHolderDistrict=accountHolderDistrict,
            accountHolderPostalCode=accountHolderPostalCode,
            abaRoutingNumber=abaRoutingNumber,
            abaAccountNumber=abaAccountNumber,
            abaCountry=abaCountry,
            iban=iban,
            ibanCity=ibanCity,
            ibanCountry=ibanCountry,
            speiClabe=speiClabe,
            speiName=speiName,
            _configuration=_configuration,
            **kwargs,
        )
