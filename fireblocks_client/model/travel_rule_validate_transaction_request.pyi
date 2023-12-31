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


class TravelRuleValidateTransactionRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "beneficiaryVASPname",
            "originatorEqualsBeneficiary",
            "transactionAsset",
            "beneficiaryAccountNumber",
            "beneficiaryName",
            "transactionAmount",
            "travelRuleBehavior",
            "destination",
            "beneficiaryAddress",
            "originatorVASPdid",
            "beneficiaryVASPdid",
        }
        
        class properties:
            transactionAsset = schemas.StrSchema
            destination = schemas.StrSchema
            transactionAmount = schemas.StrSchema
            originatorVASPdid = schemas.StrSchema
            originatorEqualsBeneficiary = schemas.BoolSchema
            travelRuleBehavior = schemas.BoolSchema
            beneficiaryVASPdid = schemas.StrSchema
            beneficiaryVASPname = schemas.StrSchema
            beneficiaryName = schemas.StrSchema
            beneficiaryAccountNumber = schemas.StrSchema
            
            
            class beneficiaryAddress(
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
                            TravelRuleAddress,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'beneficiaryAddress':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "transactionAsset": transactionAsset,
                "destination": destination,
                "transactionAmount": transactionAmount,
                "originatorVASPdid": originatorVASPdid,
                "originatorEqualsBeneficiary": originatorEqualsBeneficiary,
                "travelRuleBehavior": travelRuleBehavior,
                "beneficiaryVASPdid": beneficiaryVASPdid,
                "beneficiaryVASPname": beneficiaryVASPname,
                "beneficiaryName": beneficiaryName,
                "beneficiaryAccountNumber": beneficiaryAccountNumber,
                "beneficiaryAddress": beneficiaryAddress,
            }
    
    beneficiaryVASPname: MetaOapg.properties.beneficiaryVASPname
    originatorEqualsBeneficiary: MetaOapg.properties.originatorEqualsBeneficiary
    transactionAsset: MetaOapg.properties.transactionAsset
    beneficiaryAccountNumber: MetaOapg.properties.beneficiaryAccountNumber
    beneficiaryName: MetaOapg.properties.beneficiaryName
    transactionAmount: MetaOapg.properties.transactionAmount
    travelRuleBehavior: MetaOapg.properties.travelRuleBehavior
    destination: MetaOapg.properties.destination
    beneficiaryAddress: MetaOapg.properties.beneficiaryAddress
    originatorVASPdid: MetaOapg.properties.originatorVASPdid
    beneficiaryVASPdid: MetaOapg.properties.beneficiaryVASPdid
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transactionAsset"]) -> MetaOapg.properties.transactionAsset: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["destination"]) -> MetaOapg.properties.destination: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transactionAmount"]) -> MetaOapg.properties.transactionAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["originatorVASPdid"]) -> MetaOapg.properties.originatorVASPdid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["originatorEqualsBeneficiary"]) -> MetaOapg.properties.originatorEqualsBeneficiary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["travelRuleBehavior"]) -> MetaOapg.properties.travelRuleBehavior: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["beneficiaryVASPdid"]) -> MetaOapg.properties.beneficiaryVASPdid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["beneficiaryVASPname"]) -> MetaOapg.properties.beneficiaryVASPname: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["beneficiaryName"]) -> MetaOapg.properties.beneficiaryName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["beneficiaryAccountNumber"]) -> MetaOapg.properties.beneficiaryAccountNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["beneficiaryAddress"]) -> MetaOapg.properties.beneficiaryAddress: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["transactionAsset", "destination", "transactionAmount", "originatorVASPdid", "originatorEqualsBeneficiary", "travelRuleBehavior", "beneficiaryVASPdid", "beneficiaryVASPname", "beneficiaryName", "beneficiaryAccountNumber", "beneficiaryAddress", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transactionAsset"]) -> MetaOapg.properties.transactionAsset: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["destination"]) -> MetaOapg.properties.destination: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transactionAmount"]) -> MetaOapg.properties.transactionAmount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["originatorVASPdid"]) -> MetaOapg.properties.originatorVASPdid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["originatorEqualsBeneficiary"]) -> MetaOapg.properties.originatorEqualsBeneficiary: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["travelRuleBehavior"]) -> MetaOapg.properties.travelRuleBehavior: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["beneficiaryVASPdid"]) -> MetaOapg.properties.beneficiaryVASPdid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["beneficiaryVASPname"]) -> MetaOapg.properties.beneficiaryVASPname: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["beneficiaryName"]) -> MetaOapg.properties.beneficiaryName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["beneficiaryAccountNumber"]) -> MetaOapg.properties.beneficiaryAccountNumber: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["beneficiaryAddress"]) -> MetaOapg.properties.beneficiaryAddress: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["transactionAsset", "destination", "transactionAmount", "originatorVASPdid", "originatorEqualsBeneficiary", "travelRuleBehavior", "beneficiaryVASPdid", "beneficiaryVASPname", "beneficiaryName", "beneficiaryAccountNumber", "beneficiaryAddress", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        beneficiaryVASPname: typing.Union[MetaOapg.properties.beneficiaryVASPname, str, ],
        originatorEqualsBeneficiary: typing.Union[MetaOapg.properties.originatorEqualsBeneficiary, bool, ],
        transactionAsset: typing.Union[MetaOapg.properties.transactionAsset, str, ],
        beneficiaryAccountNumber: typing.Union[MetaOapg.properties.beneficiaryAccountNumber, str, ],
        beneficiaryName: typing.Union[MetaOapg.properties.beneficiaryName, str, ],
        transactionAmount: typing.Union[MetaOapg.properties.transactionAmount, str, ],
        travelRuleBehavior: typing.Union[MetaOapg.properties.travelRuleBehavior, bool, ],
        destination: typing.Union[MetaOapg.properties.destination, str, ],
        beneficiaryAddress: typing.Union[MetaOapg.properties.beneficiaryAddress, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        originatorVASPdid: typing.Union[MetaOapg.properties.originatorVASPdid, str, ],
        beneficiaryVASPdid: typing.Union[MetaOapg.properties.beneficiaryVASPdid, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TravelRuleValidateTransactionRequest':
        return super().__new__(
            cls,
            *_args,
            beneficiaryVASPname=beneficiaryVASPname,
            originatorEqualsBeneficiary=originatorEqualsBeneficiary,
            transactionAsset=transactionAsset,
            beneficiaryAccountNumber=beneficiaryAccountNumber,
            beneficiaryName=beneficiaryName,
            transactionAmount=transactionAmount,
            travelRuleBehavior=travelRuleBehavior,
            destination=destination,
            beneficiaryAddress=beneficiaryAddress,
            originatorVASPdid=originatorVASPdid,
            beneficiaryVASPdid=beneficiaryVASPdid,
            _configuration=_configuration,
            **kwargs,
        )

from fireblocks_client.model.travel_rule_address import TravelRuleAddress
