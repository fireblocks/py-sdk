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


class TransactionRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def operation() -> typing.Type['TransactionOperation']:
                return TransactionOperation
            note = schemas.StrSchema
            externalTxId = schemas.StrSchema
            assetId = schemas.StrSchema
        
            @staticmethod
            def source() -> typing.Type['TransferPeerPath']:
                return TransferPeerPath
        
            @staticmethod
            def destination() -> typing.Type['DestinationTransferPeerPath']:
                return DestinationTransferPeerPath
            
            
            class destinations(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TransactionRequestDestination']:
                        return TransactionRequestDestination
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['TransactionRequestDestination'], typing.List['TransactionRequestDestination']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'destinations':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TransactionRequestDestination':
                    return super().__getitem__(i)
            
            
            class amount(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    one_of_0 = schemas.StrSchema
                    one_of_1 = schemas.NumberSchema
                    
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
                ) -> 'amount':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            treatAsGrossAmount = schemas.BoolSchema
            forceSweep = schemas.BoolSchema
            
            
            class feeLevel(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "LOW": "LOW",
                        "MEDIUM": "MEDIUM",
                        "HIGH": "HIGH",
                    }
                
                @schemas.classproperty
                def LOW(cls):
                    return cls("LOW")
                
                @schemas.classproperty
                def MEDIUM(cls):
                    return cls("MEDIUM")
                
                @schemas.classproperty
                def HIGH(cls):
                    return cls("HIGH")
            
            
            class fee(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    one_of_0 = schemas.StrSchema
                    one_of_1 = schemas.NumberSchema
                    
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
                ) -> 'fee':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class priorityFee(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    one_of_0 = schemas.StrSchema
                    one_of_1 = schemas.NumberSchema
                    
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
                ) -> 'priorityFee':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            failOnLowFee = schemas.BoolSchema
            maxFee = schemas.StrSchema
            
            
            class gasLimit(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    one_of_0 = schemas.StrSchema
                    one_of_1 = schemas.NumberSchema
                    
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
                ) -> 'gasLimit':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class gasPrice(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    one_of_0 = schemas.StrSchema
                    one_of_1 = schemas.NumberSchema
                    
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
                ) -> 'gasPrice':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class networkFee(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    one_of_0 = schemas.StrSchema
                    one_of_1 = schemas.NumberSchema
                    
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
                ) -> 'networkFee':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            replaceTxByHash = schemas.StrSchema
            extraParameters = schemas.DictSchema
            customerRefId = schemas.StrSchema
            autoStaking = schemas.BoolSchema
            
            
            class networkStaking(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    one_of_0 = schemas.StrSchema
                    one_of_1 = schemas.NumberSchema
                    
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
                ) -> 'networkStaking':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class cpuStaking(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    one_of_0 = schemas.StrSchema
                    one_of_1 = schemas.NumberSchema
                    
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
                ) -> 'cpuStaking':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "operation": operation,
                "note": note,
                "externalTxId": externalTxId,
                "assetId": assetId,
                "source": source,
                "destination": destination,
                "destinations": destinations,
                "amount": amount,
                "treatAsGrossAmount": treatAsGrossAmount,
                "forceSweep": forceSweep,
                "feeLevel": feeLevel,
                "fee": fee,
                "priorityFee": priorityFee,
                "failOnLowFee": failOnLowFee,
                "maxFee": maxFee,
                "gasLimit": gasLimit,
                "gasPrice": gasPrice,
                "networkFee": networkFee,
                "replaceTxByHash": replaceTxByHash,
                "extraParameters": extraParameters,
                "customerRefId": customerRefId,
                "autoStaking": autoStaking,
                "networkStaking": networkStaking,
                "cpuStaking": cpuStaking,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["operation"]) -> 'TransactionOperation': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["note"]) -> MetaOapg.properties.note: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["externalTxId"]) -> MetaOapg.properties.externalTxId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assetId"]) -> MetaOapg.properties.assetId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source"]) -> 'TransferPeerPath': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["destination"]) -> 'DestinationTransferPeerPath': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["destinations"]) -> MetaOapg.properties.destinations: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["treatAsGrossAmount"]) -> MetaOapg.properties.treatAsGrossAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["forceSweep"]) -> MetaOapg.properties.forceSweep: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["feeLevel"]) -> MetaOapg.properties.feeLevel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fee"]) -> MetaOapg.properties.fee: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["priorityFee"]) -> MetaOapg.properties.priorityFee: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["failOnLowFee"]) -> MetaOapg.properties.failOnLowFee: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxFee"]) -> MetaOapg.properties.maxFee: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gasLimit"]) -> MetaOapg.properties.gasLimit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gasPrice"]) -> MetaOapg.properties.gasPrice: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["networkFee"]) -> MetaOapg.properties.networkFee: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["replaceTxByHash"]) -> MetaOapg.properties.replaceTxByHash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["extraParameters"]) -> MetaOapg.properties.extraParameters: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customerRefId"]) -> MetaOapg.properties.customerRefId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["autoStaking"]) -> MetaOapg.properties.autoStaking: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["networkStaking"]) -> MetaOapg.properties.networkStaking: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cpuStaking"]) -> MetaOapg.properties.cpuStaking: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["operation", "note", "externalTxId", "assetId", "source", "destination", "destinations", "amount", "treatAsGrossAmount", "forceSweep", "feeLevel", "fee", "priorityFee", "failOnLowFee", "maxFee", "gasLimit", "gasPrice", "networkFee", "replaceTxByHash", "extraParameters", "customerRefId", "autoStaking", "networkStaking", "cpuStaking", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["operation"]) -> typing.Union['TransactionOperation', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["note"]) -> typing.Union[MetaOapg.properties.note, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["externalTxId"]) -> typing.Union[MetaOapg.properties.externalTxId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assetId"]) -> typing.Union[MetaOapg.properties.assetId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> typing.Union['TransferPeerPath', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["destination"]) -> typing.Union['DestinationTransferPeerPath', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["destinations"]) -> typing.Union[MetaOapg.properties.destinations, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["treatAsGrossAmount"]) -> typing.Union[MetaOapg.properties.treatAsGrossAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["forceSweep"]) -> typing.Union[MetaOapg.properties.forceSweep, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["feeLevel"]) -> typing.Union[MetaOapg.properties.feeLevel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fee"]) -> typing.Union[MetaOapg.properties.fee, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["priorityFee"]) -> typing.Union[MetaOapg.properties.priorityFee, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["failOnLowFee"]) -> typing.Union[MetaOapg.properties.failOnLowFee, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxFee"]) -> typing.Union[MetaOapg.properties.maxFee, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gasLimit"]) -> typing.Union[MetaOapg.properties.gasLimit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gasPrice"]) -> typing.Union[MetaOapg.properties.gasPrice, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["networkFee"]) -> typing.Union[MetaOapg.properties.networkFee, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["replaceTxByHash"]) -> typing.Union[MetaOapg.properties.replaceTxByHash, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["extraParameters"]) -> typing.Union[MetaOapg.properties.extraParameters, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customerRefId"]) -> typing.Union[MetaOapg.properties.customerRefId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["autoStaking"]) -> typing.Union[MetaOapg.properties.autoStaking, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["networkStaking"]) -> typing.Union[MetaOapg.properties.networkStaking, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cpuStaking"]) -> typing.Union[MetaOapg.properties.cpuStaking, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["operation", "note", "externalTxId", "assetId", "source", "destination", "destinations", "amount", "treatAsGrossAmount", "forceSweep", "feeLevel", "fee", "priorityFee", "failOnLowFee", "maxFee", "gasLimit", "gasPrice", "networkFee", "replaceTxByHash", "extraParameters", "customerRefId", "autoStaking", "networkStaking", "cpuStaking", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        operation: typing.Union['TransactionOperation', schemas.Unset] = schemas.unset,
        note: typing.Union[MetaOapg.properties.note, str, schemas.Unset] = schemas.unset,
        externalTxId: typing.Union[MetaOapg.properties.externalTxId, str, schemas.Unset] = schemas.unset,
        assetId: typing.Union[MetaOapg.properties.assetId, str, schemas.Unset] = schemas.unset,
        source: typing.Union['TransferPeerPath', schemas.Unset] = schemas.unset,
        destination: typing.Union['DestinationTransferPeerPath', schemas.Unset] = schemas.unset,
        destinations: typing.Union[MetaOapg.properties.destinations, list, tuple, schemas.Unset] = schemas.unset,
        amount: typing.Union[MetaOapg.properties.amount, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        treatAsGrossAmount: typing.Union[MetaOapg.properties.treatAsGrossAmount, bool, schemas.Unset] = schemas.unset,
        forceSweep: typing.Union[MetaOapg.properties.forceSweep, bool, schemas.Unset] = schemas.unset,
        feeLevel: typing.Union[MetaOapg.properties.feeLevel, str, schemas.Unset] = schemas.unset,
        fee: typing.Union[MetaOapg.properties.fee, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        priorityFee: typing.Union[MetaOapg.properties.priorityFee, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        failOnLowFee: typing.Union[MetaOapg.properties.failOnLowFee, bool, schemas.Unset] = schemas.unset,
        maxFee: typing.Union[MetaOapg.properties.maxFee, str, schemas.Unset] = schemas.unset,
        gasLimit: typing.Union[MetaOapg.properties.gasLimit, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        gasPrice: typing.Union[MetaOapg.properties.gasPrice, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        networkFee: typing.Union[MetaOapg.properties.networkFee, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        replaceTxByHash: typing.Union[MetaOapg.properties.replaceTxByHash, str, schemas.Unset] = schemas.unset,
        extraParameters: typing.Union[MetaOapg.properties.extraParameters, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        customerRefId: typing.Union[MetaOapg.properties.customerRefId, str, schemas.Unset] = schemas.unset,
        autoStaking: typing.Union[MetaOapg.properties.autoStaking, bool, schemas.Unset] = schemas.unset,
        networkStaking: typing.Union[MetaOapg.properties.networkStaking, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        cpuStaking: typing.Union[MetaOapg.properties.cpuStaking, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TransactionRequest':
        return super().__new__(
            cls,
            *_args,
            operation=operation,
            note=note,
            externalTxId=externalTxId,
            assetId=assetId,
            source=source,
            destination=destination,
            destinations=destinations,
            amount=amount,
            treatAsGrossAmount=treatAsGrossAmount,
            forceSweep=forceSweep,
            feeLevel=feeLevel,
            fee=fee,
            priorityFee=priorityFee,
            failOnLowFee=failOnLowFee,
            maxFee=maxFee,
            gasLimit=gasLimit,
            gasPrice=gasPrice,
            networkFee=networkFee,
            replaceTxByHash=replaceTxByHash,
            extraParameters=extraParameters,
            customerRefId=customerRefId,
            autoStaking=autoStaking,
            networkStaking=networkStaking,
            cpuStaking=cpuStaking,
            _configuration=_configuration,
            **kwargs,
        )

from fireblocks_client.model.destination_transfer_peer_path import DestinationTransferPeerPath
from fireblocks_client.model.transaction_operation import TransactionOperation
from fireblocks_client.model.transaction_request_destination import TransactionRequestDestination
from fireblocks_client.model.transfer_peer_path import TransferPeerPath
